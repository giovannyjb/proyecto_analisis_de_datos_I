"""Dashboard interactivo EDA — Dengue SIVIGILA (Grupo 3)."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Permite importar src/ al ejecutar con streamlit run app/dashboard.py
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.dengue_clean import dengue_parquet_path, load_dengue_limpio
from src.load_data import list_dengue_years

MESES = {
    1: "Ene", 2: "Feb", 3: "Mar", 4: "Abr", 5: "May", 6: "Jun",
    7: "Jul", 8: "Ago", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dic",
}
AREA_LABELS = {1: "Urbana", 2: "Rural", 3: "Urbana-rural"}
# Solo numéricas/temporales reales (alineado al notebook del taller)
COLS_NUM = ["edad_anios", "SEMANA", "mes"]
ANIO_TALLER = 2025


@st.cache_data(show_spinner="Cargando datos de dengue...")
def cargar_datos(year: int) -> pd.DataFrame:
    """Carga un año limpio. El filtro FEC_NOT se aplica al año elegido (no solo 2025)."""
    return load_dengue_limpio(year)


def aplicar_filtros(
    df: pd.DataFrame,
    departamentos: list[str],
    municipios: list[str],
    meses: list[int],
    sexos: list[str],
    solo_confirmados: bool,
) -> pd.DataFrame:
    filtrado = df.copy()
    if departamentos:
        filtrado = filtrado[filtrado["Departamento_ocurrencia"].astype(str).isin(departamentos)]
    if municipios:
        filtrado = filtrado[filtrado["Municipio_ocurrencia"].astype(str).isin(municipios)]
    if meses:
        filtrado = filtrado[filtrado["mes"].isin(meses)]
    if sexos:
        filtrado = filtrado[filtrado["SEXO"].astype(str).isin(sexos)]
    if solo_confirmados:
        filtrado = filtrado[filtrado["confirmado"]]
    return filtrado


def sidebar_filtros() -> tuple[int, pd.DataFrame]:
    st.sidebar.header("Filtros")
    st.sidebar.caption(
        f"El **Taller 1** se centra en **{ANIO_TALLER}**. "
        "Puedes cambiar el año para explorar otros Excel SIVIGILA disponibles."
    )

    years = list_dengue_years() or [ANIO_TALLER]
    default_idx = years.index(ANIO_TALLER) if ANIO_TALLER in years else len(years) - 1
    year = st.sidebar.selectbox("Año", years, index=default_idx)

    if year == ANIO_TALLER:
        st.sidebar.success(f"Año del taller ({ANIO_TALLER})")
    else:
        st.sidebar.info(f"Explorando {year} (fuera del foco del Taller 1)")

    if not dengue_parquet_path(year).exists():
        st.sidebar.info(
            "Primera carga de este año: puede tardar 1–2 min mientras se genera el parquet. "
            f"Se filtrarán notificaciones con FEC_NOT fuera de {year}."
        )

    df_year = cargar_datos(year)

    deptos = sorted(df_year["Departamento_ocurrencia"].astype(str).unique())
    sel_deptos = st.sidebar.multiselect("Departamento", deptos)

    mun_base = df_year
    if sel_deptos:
        mun_base = mun_base[mun_base["Departamento_ocurrencia"].astype(str).isin(sel_deptos)]
    municipios = sorted(mun_base["Municipio_ocurrencia"].astype(str).unique())
    sel_mun = st.sidebar.multiselect("Municipio", municipios)

    sel_meses = st.sidebar.multiselect(
        "Mes",
        options=list(MESES.keys()),
        format_func=lambda m: MESES[m],
    )

    sexos = sorted(df_year["SEXO"].astype(str).unique())
    sel_sexo = st.sidebar.multiselect("Sexo", sexos)

    solo_conf = st.sidebar.checkbox("Solo casos confirmados", value=False)

    df_filtrado = aplicar_filtros(
        df_year, sel_deptos, sel_mun, sel_meses, sel_sexo, solo_conf
    )
    return year, df_filtrado


def tab_resumen(df: pd.DataFrame, year: int) -> None:
    st.subheader("Resumen general")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total casos", f"{len(df):,}")
    c2.metric("% confirmados", f"{df['confirmado'].mean() * 100:.1f}%")
    c3.metric("% hospitalizados", f"{df['hospitalizado'].mean() * 100:.1f}%")
    c4.metric("Departamentos", df["Departamento_ocurrencia"].nunique())

    c5, c6 = st.columns(2)
    c5.metric("Municipios", df["Municipio_ocurrencia"].nunique())
    if df["FEC_NOT"].notna().any():
        c6.metric(
            "Rango FEC_NOT",
            f"{df['FEC_NOT'].min():%Y-%m-%d} → {df['FEC_NOT'].max():%Y-%m-%d}",
        )
        anios_fec = sorted(df["FEC_NOT"].dt.year.dropna().astype(int).unique())
        if anios_fec != [year]:
            st.warning(
                f"Hay fechas de notificación fuera de {year}: {anios_fec}. "
                "Regenera el parquet o revisa la limpieza."
            )
        else:
            st.caption(f"Fechas de notificación acotadas al año seleccionado ({year}).")

    st.markdown("#### Calidad de datos — columnas con más nulos")
    nulos = (df.isnull().mean() * 100).round(2)
    nulos = nulos[nulos > 0].sort_values(ascending=False).head(15)
    if len(nulos):
        st.dataframe(nulos.rename("% nulos").to_frame(), use_container_width=True)
    else:
        st.success("Sin valores nulos en las columnas restantes.")


def tab_temporal(df: pd.DataFrame, year: int) -> None:
    st.subheader(f"Análisis temporal — {year} (H1)")

    casos_mes = df.groupby("mes").size().reset_index(name="casos")
    casos_mes["mes_nombre"] = casos_mes["mes"].map(MESES)
    fig_mes = px.bar(
        casos_mes, x="mes_nombre", y="casos",
        title="Casos por mes", labels={"mes_nombre": "Mes", "casos": "Casos"},
    )
    st.plotly_chart(fig_mes, use_container_width=True)

    casos_sem = df.groupby("SEMANA").size().reset_index(name="casos")
    fig_sem = px.line(
        casos_sem, x="SEMANA", y="casos",
        title="Casos por semana epidemiológica", markers=True,
    )
    st.plotly_chart(fig_sem, use_container_width=True)

    resumen_semana = (
        df.groupby("SEMANA")
        .agg(casos=("CONSECUTIVE", "count"), pct_hospitalizado=("hospitalizado", "mean"))
        .reset_index()
    )
    fig_dual = go.Figure()
    fig_dual.add_trace(
        go.Scatter(
            x=resumen_semana["SEMANA"], y=resumen_semana["casos"],
            name="Casos", line=dict(color="steelblue"),
        )
    )
    fig_dual.add_trace(
        go.Scatter(
            x=resumen_semana["SEMANA"],
            y=resumen_semana["pct_hospitalizado"] * 100,
            name="% hospitalización",
            yaxis="y2",
            line=dict(color="darkorange"),
        )
    )
    fig_dual.update_layout(
        title="Carga semanal y % hospitalización",
        xaxis_title="Semana epidemiológica",
        yaxis=dict(title="Casos"),
        yaxis2=dict(title="% hospitalización", overlaying="y", side="right"),
        legend=dict(orientation="h"),
    )
    st.plotly_chart(fig_dual, use_container_width=True)
    st.caption(
        "Los casos pueden bajar tras el pico, pero el % de hospitalización no necesariamente sigue la misma curva."
    )

    if "AREA" in df.columns:
        area_df = df.copy()
        area_df["area_label"] = area_df["AREA"].map(AREA_LABELS).fillna("Otro")
        casos_area = (
            area_df.groupby(["mes", "area_label"]).size().reset_index(name="casos")
        )
        casos_area["mes_nombre"] = casos_area["mes"].map(MESES)
        fig_area = px.bar(
            casos_area, x="mes_nombre", y="casos", color="area_label",
            title="Casos por mes según área", barmode="stack",
        )
        st.plotly_chart(fig_area, use_container_width=True)


def tab_territorial(df: pd.DataFrame, year: int) -> None:
    st.subheader(f"Análisis territorial — {year} (H2)")
    top_n = st.slider("Top N departamentos", 5, 20, 10)

    top_deptos = (
        df["Departamento_ocurrencia"].astype(str).value_counts().head(top_n).index.tolist()
    )
    df_top = df[df["Departamento_ocurrencia"].astype(str).isin(top_deptos)]

    fig = px.bar(
        df_top["Departamento_ocurrencia"].astype(str).value_counts().reset_index(),
        x="count", y="Departamento_ocurrencia", orientation="h",
        title=f"Top {top_n} departamentos por casos",
        labels={"count": "Casos", "Departamento_ocurrencia": "Departamento"},
    )
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig, use_container_width=True)

    top_mun = (
        df.groupby(["Departamento_ocurrencia", "Municipio_ocurrencia"])
        .size()
        .reset_index(name="casos")
        .sort_values("casos", ascending=False)
        .head(top_n)
    )
    st.markdown("#### Top municipios")
    st.dataframe(top_mun, use_container_width=True)

    hosp = (
        df_top.groupby("Departamento_ocurrencia")["hospitalizado"]
        .mean()
        .reset_index(name="pct_hospitalizado")
    )
    hosp["pct_hospitalizado"] = (hosp["pct_hospitalizado"] * 100).round(1)
    fig_hosp = px.bar(
        hosp.sort_values("pct_hospitalizado", ascending=True),
        x="pct_hospitalizado", y="Departamento_ocurrencia", orientation="h",
        title="% hospitalización por departamento (top)",
        labels={"pct_hospitalizado": "% hospitalizados"},
    )
    st.plotly_chart(fig_hosp, use_container_width=True)


def tab_perfil(df: pd.DataFrame, year: int) -> None:
    st.subheader(f"Perfil epidemiológico — {year} (H3)")

    fig_edad = px.histogram(
        df, x="edad_anios", nbins=40,
        title="Distribución de edad (años)",
        labels={"edad_anios": "Edad (años)"},
    )
    st.plotly_chart(fig_edad, use_container_width=True)

    c1, c2 = st.columns(2)
    with c1:
        sexo = df["SEXO"].astype(str).value_counts().reset_index()
        sexo.columns = ["SEXO", "casos"]
        st.plotly_chart(px.pie(sexo, names="SEXO", values="casos", title="Por sexo"), use_container_width=True)
    with c2:
        if "AREA" in df.columns:
            area = df["AREA"].map(AREA_LABELS).fillna("Otro").value_counts().reset_index()
            area.columns = ["AREA", "casos"]
            st.plotly_chart(px.pie(area, names="AREA", values="casos", title="Por área"), use_container_width=True)

    deptos = df["Departamento_ocurrencia"].astype(str)
    if (deptos == "VALLE").any():
        st.markdown("#### Comparación Valle vs resto (H3)")
        es_valle = deptos == "VALLE"
        cmp = pd.DataFrame({
            "casos": [int(es_valle.sum()), int((~es_valle).sum())],
            "edad_media": [
                df.loc[es_valle, "edad_anios"].mean(),
                df.loc[~es_valle, "edad_anios"].mean(),
            ],
            "pct_hospitalizado": [
                df.loc[es_valle, "hospitalizado"].mean() * 100,
                df.loc[~es_valle, "hospitalizado"].mean() * 100,
            ],
        }, index=["VALLE", "Resto"])
        st.dataframe(cmp.round(2), use_container_width=True)

    estado = (
        df["nom_est_f_caso"].astype(str).value_counts().head(8).reset_index()
    )
    estado.columns = ["estado", "casos"]
    st.plotly_chart(
        px.bar(estado, x="casos", y="estado", orientation="h", title="Estado final del caso"),
        use_container_width=True,
    )

    resumen_sexo = (
        df.groupby("SEXO")
        .agg(
            casos=("CONSECUTIVE", "count"),
            edad_media=("edad_anios", "mean"),
            pct_hospitalizado=("hospitalizado", "mean"),
            pct_confirmado=("confirmado", "mean"),
        )
        .round(3)
    )
    resumen_sexo["pct_hospitalizado"] = (resumen_sexo["pct_hospitalizado"] * 100).round(1)
    resumen_sexo["pct_confirmado"] = (resumen_sexo["pct_confirmado"] * 100).round(1)
    st.markdown("#### Resumen por sexo")
    st.dataframe(resumen_sexo, use_container_width=True)


def tab_correlaciones(df: pd.DataFrame, year: int) -> None:
    st.subheader(f"Análisis bivariado — {year}")
    st.caption(
        "Correlación solo con variables numéricas/temporales "
        "(`edad_anios`, `SEMANA`, `mes`). Códigos como `PAC_HOS`/`AREA` se exploran en otras pestañas."
    )

    cols = [c for c in COLS_NUM if c in df.columns]
    corr = df[cols].corr()
    fig = go.Figure(
        data=go.Heatmap(
            z=corr.values, x=corr.columns, y=corr.columns,
            colorscale="RdBu", zmid=0,
            text=corr.round(2).values, texttemplate="%{text}",
        )
    )
    fig.update_layout(title="Matriz de correlación", height=500)
    st.plotly_chart(fig, use_container_width=True)

    muestra = df.sample(min(3000, len(df)), random_state=42) if len(df) > 0 else df
    fig_sc = px.scatter(
        muestra, x="edad_anios", y="SEMANA", color="hospitalizado",
        title="Edad vs. semana epidemiológica (muestra ≤3k)",
        labels={"edad_anios": "Edad (años)", "SEMANA": "Semana", "hospitalizado": "Hospitalizado"},
        opacity=0.45,
    )
    st.plotly_chart(fig_sc, use_container_width=True)
    st.caption("Si hospitalizado/no se superponen, no hay separación clara a nivel individual.")


def tab_explorador(df: pd.DataFrame, year: int) -> None:
    st.subheader(f"Explorador de datos — {year}")
    st.caption(f"{len(df):,} registros con los filtros aplicados")

    columnas = st.multiselect(
        "Columnas a mostrar",
        options=sorted(df.columns.tolist()),
        default=[
            "FEC_NOT", "SEMANA", "EDAD", "SEXO", "Departamento_ocurrencia",
            "Municipio_ocurrencia", "confirmado", "hospitalizado", "nom_est_f_caso",
        ],
    )
    vista = df[columnas] if columnas else df
    st.dataframe(vista.head(500), use_container_width=True)

    csv = vista.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Descargar CSV filtrado",
        data=csv,
        file_name=f"dengue_{year}_filtrado.csv",
        mime="text/csv",
    )


def main() -> None:
    st.set_page_config(
        page_title="EDA Dengue — Grupo 3",
        page_icon="🦟",
        layout="wide",
    )
    st.title("Dashboard EDA — Dengue SIVIGILA")
    st.caption(
        f"Exploración interactiva de casos dengue (evento 210). "
        f"El notebook del Taller 1 se enfoca en **{ANIO_TALLER}**; "
        "este dashboard permite revisar **cualquier año** disponible en `data/raw/`. "
        "Cada año se limpia filtrando `FEC_NOT` al año seleccionado."
    )

    year, df = sidebar_filtros()

    if df.empty:
        st.warning("No hay datos con los filtros seleccionados.")
        return

    tabs = st.tabs([
        "Resumen", "Temporal", "Territorial", "Perfil", "Correlaciones", "Explorador",
    ])
    with tabs[0]:
        tab_resumen(df, year)
    with tabs[1]:
        tab_temporal(df, year)
    with tabs[2]:
        tab_territorial(df, year)
    with tabs[3]:
        tab_perfil(df, year)
    with tabs[4]:
        tab_correlaciones(df, year)
    with tabs[5]:
        tab_explorador(df, year)


if __name__ == "__main__":
    main()
