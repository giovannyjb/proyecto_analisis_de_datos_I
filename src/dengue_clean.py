"""Limpieza y carga del dataset SIVIGILA de dengue."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.config import DATA_PROCESSED
from src.load_data import load_dengue

COLS_VACIAS = ["GRU_POB", "CBMTE", "FEC_DEF", "FM_FUERZA", "FM_UNIDAD", "FM_GRADO", "COD_ASE"]
COLS_FECHA = ["FEC_NOT", "INI_SIN", "FEC_HOS", "FEC_CON", "FECHA_NTO"]


def parsear_fecha(serie: pd.Series) -> pd.Series:
    """Convierte fechas SIVIGILA (dd/mm/yyyy con 'a. m.' / 'p. m.') a datetime."""
    limpia = (
        serie.astype(str)
        .str.replace("\xa0", " ", regex=False)
        .str.replace(r"\s*a\.\s*m\.", "", regex=True)
        .str.replace(r"\s*p\.\s*m\.", "", regex=True)
        .str.strip()
    )
    dt = pd.to_datetime(limpia, format="%d/%m/%Y %H:%M:%S", errors="coerce")
    mask = dt.isna() & limpia.ne("nan") & limpia.ne("NaT") & limpia.ne("") & limpia.ne("None")
    if mask.any():
        dt = dt.copy()
        dt.loc[mask] = pd.to_datetime(limpia.loc[mask], format="%d/%m/%Y", errors="coerce")
    return dt


def _edad_en_anios(row: pd.Series) -> float:
    if row["UNI_MED"] == 1:
        return float(row["EDAD"])
    if row["UNI_MED"] == 2:
        return row["EDAD"] / 12
    return row["EDAD"] / 365


def limpiar_dengue(df: pd.DataFrame, anio: int | None = None) -> pd.DataFrame:
    """Aplica la limpieza del EDA: columnas vacías, nulos críticos, fechas y features.

    El filtro de `FEC_NOT` se acota al `anio` indicado (p. ej. 2024 o 2025).
    Si no se pasa, se toma la moda de la columna `ANO` del propio archivo.
    """
    df_limpio = df.copy()

    cols_vacias = [
        c for c in COLS_VACIAS if c in df_limpio.columns
    ] + [c for c in df_limpio.columns if c.startswith("FM_") and c not in COLS_VACIAS]
    df_limpio = df_limpio.drop(columns=cols_vacias, errors="ignore")

    df_limpio = df_limpio.dropna(subset=["COD_MUN_O", "FEC_NOT"])

    for col in COLS_FECHA:
        if col in df_limpio.columns:
            df_limpio[col] = parsear_fecha(df_limpio[col])

    # Acotar FEC_NOT al año del archivo (multi-año: 2019…2025, no solo 2025)
    if anio is None and "ANO" in df_limpio.columns and df_limpio["ANO"].notna().any():
        anio = int(df_limpio["ANO"].dropna().mode().iloc[0])
    if anio is not None and "FEC_NOT" in df_limpio.columns:
        fuera = df_limpio["FEC_NOT"].notna() & (df_limpio["FEC_NOT"].dt.year != int(anio))
        df_limpio = df_limpio.loc[~fuera].copy()

    df_limpio["edad_anios"] = df_limpio.apply(_edad_en_anios, axis=1)
    df_limpio["mes"] = df_limpio["FEC_NOT"].dt.month
    df_limpio["trimestre"] = df_limpio["FEC_NOT"].dt.quarter
    df_limpio["hospitalizado"] = df_limpio["PAC_HOS"] == 1
    df_limpio["confirmado"] = df_limpio["confirmados"] == 1
    df_limpio["depto_mun"] = (
        df_limpio["COD_DPTO_O"].astype(str).str.zfill(2)
        + df_limpio["COD_MUN_O"].astype(str).str.zfill(3)
    )

    return df_limpio


def dengue_parquet_path(year: int) -> Path:
    """Ruta del parquet limpio para un año."""
    return DATA_PROCESSED / f"dengue_sivigila_{year}_limpio.parquet"


def _parquet_inconsistente_con_anio(df: pd.DataFrame, year: int) -> bool:
    """True si el parquet guarda FEC_NOT fuera del año pedido (limpieza antigua)."""
    if "FEC_NOT" not in df.columns or not df["FEC_NOT"].notna().any():
        return False
    fec = pd.to_datetime(df["FEC_NOT"], errors="coerce")
    anios = set(fec.dt.year.dropna().astype(int).unique())
    return bool(anios) and anios != {int(year)}


def load_dengue_limpio(year: int, *, force: bool = False) -> pd.DataFrame:
    """Carga parquet limpio si existe; si no, limpia desde Excel y guarda.

    Si un parquet viejo tiene fechas fuera del `year` seleccionado, se regenera.
    """
    path = dengue_parquet_path(year)
    if path.exists() and not force:
        df_existente = pd.read_parquet(path)
        if not _parquet_inconsistente_con_anio(df_existente, year):
            return df_existente

    df = load_dengue("year", year=year)
    df_limpio = limpiar_dengue(df, anio=year)
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    df_limpio.to_parquet(path, index=False)
    return df_limpio
