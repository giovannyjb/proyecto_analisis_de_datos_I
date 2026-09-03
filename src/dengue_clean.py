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
        .str.replace(r"\s*a\.\s*m\.", "", regex=True)
        .str.replace(r"\s*p\.\s*m\.", "", regex=True)
        .str.strip()
    )
    return pd.to_datetime(limpia, dayfirst=True, errors="coerce")


def _edad_en_anios(row: pd.Series) -> float:
    if row["UNI_MED"] == 1:
        return float(row["EDAD"])
    if row["UNI_MED"] == 2:
        return row["EDAD"] / 12
    return row["EDAD"] / 365


def limpiar_dengue(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica la limpieza del EDA: columnas vacías, nulos críticos, fechas y features."""
    df_limpio = df.copy()

    cols_vacias = [
        c for c in COLS_VACIAS if c in df_limpio.columns
    ] + [c for c in df_limpio.columns if c.startswith("FM_") and c not in COLS_VACIAS]
    df_limpio = df_limpio.drop(columns=cols_vacias, errors="ignore")

    df_limpio = df_limpio.dropna(subset=["COD_MUN_O", "FEC_NOT"])

    for col in COLS_FECHA:
        if col in df_limpio.columns:
            df_limpio[col] = parsear_fecha(df_limpio[col])

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


def load_dengue_limpio(year: int) -> pd.DataFrame:
    """Carga parquet limpio si existe; si no, limpia desde Excel y guarda."""
    path = dengue_parquet_path(year)
    if path.exists():
        return pd.read_parquet(path)

    df = load_dengue("year", year=year)
    df_limpio = limpiar_dengue(df)
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    df_limpio.to_parquet(path, index=False)
    return df_limpio
