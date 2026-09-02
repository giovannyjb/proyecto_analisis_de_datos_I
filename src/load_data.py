"""Utilidades para cargar datos desde data/raw."""

from __future__ import annotations

from pathlib import Path
from typing import Literal

import pandas as pd

from src.config import (
    DATA_PROCESSED,
    DATA_RAW,
    DENGUE_FILE_PATTERN,
    DENGUE_PARQUET,
    SUPPORTED_EXTENSIONS,
)

LoadMode = Literal["year", "parquet", "sample"]


def list_raw_files() -> list[Path]:
    """Lista archivos de datos soportados en data/raw."""
    if not DATA_RAW.exists():
        return []
    return sorted(
        p for p in DATA_RAW.iterdir()
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS
    )


def load_file(path: Path) -> pd.DataFrame:
    """Carga un CSV o Excel en un DataFrame."""
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(path)
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    raise ValueError(f"Formato no soportado: {suffix}")


def load_all_raw() -> dict[str, pd.DataFrame]:
    """Carga todos los archivos soportados de data/raw."""
    datasets: dict[str, pd.DataFrame] = {}
    for path in list_raw_files():
        datasets[path.stem] = load_file(path)
    return datasets


def raw_data_available() -> bool:
    """Indica si hay archivos de datos en data/raw."""
    return len(list_raw_files()) > 0


def list_dengue_files() -> list[Path]:
    """Lista archivos SIVIGILA de dengue (evento 210) en data/raw."""
    if not DATA_RAW.exists():
        return []
    return sorted(DATA_RAW.glob(DENGUE_FILE_PATTERN))


def list_dengue_years() -> list[int]:
    """Devuelve los años disponibles en los archivos de dengue."""
    years: list[int] = []
    for path in list_dengue_files():
        parts = path.stem.split("_")
        if len(parts) >= 2 and parts[1].isdigit():
            years.append(int(parts[1]))
    return years


def _dengue_path_for_year(year: int) -> Path:
    path = DATA_RAW / f"Datos_{year}_210.xlsx"
    if not path.exists():
        available = ", ".join(str(y) for y in list_dengue_years()) or "ninguno"
        raise FileNotFoundError(
            f"No existe {path.name}. Años disponibles: {available}"
        )
    return path


FECHA_COLS = {
    "FEC_NOT", "INI_SIN", "FEC_HOS", "FEC_CON", "FEC_DEF",
    "FECHA_NTO", "FEC_ARC_XL", "FEC_AJU",
}


def optimize_dengue_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """Reduce memoria convirtiendo textos repetidos a category."""
    df = df.copy()
    for col in df.select_dtypes(include="object").columns:
        if col in FECHA_COLS or col.startswith("FEC_"):
            continue
        nunique = df[col].nunique(dropna=False)
        if nunique <= max(50, len(df) * 0.5):
            df[col] = df[col].astype("category")
    return df


def load_dengue_year(
    year: int,
    *,
    columns: list[str] | None = None,
    optimize: bool = True,
) -> pd.DataFrame:
    """Carga un solo año de dengue desde Excel."""
    df = pd.read_excel(_dengue_path_for_year(year), usecols=columns)
    df["archivo_origen"] = str(year)
    return optimize_dengue_dtypes(df) if optimize else df


def build_dengue_parquet(
    *,
    force: bool = False,
    optimize: bool = True,
) -> Path:
    """
    Une todos los años SIVIGILA y guarda un Parquet en data/processed/.

    Ejecutar desde terminal (no en el notebook): tarda varios minutos
    leyendo Excel, pero luego la carga es mucho más rápida y liviana.
    """
    if DENGUE_PARQUET.exists() and not force:
        return DENGUE_PARQUET

    files = list_dengue_files()
    if not files:
        raise FileNotFoundError(f"No hay archivos {DENGUE_FILE_PATTERN} en {DATA_RAW}")

    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    frames: list[pd.DataFrame] = []
    for path in files:
        year = path.stem.split("_")[1]
        print(f"Cargando {path.name}...")
        df = pd.read_excel(path)
        df["archivo_origen"] = year
        frames.append(df)

    df_all = pd.concat(frames, ignore_index=True)
    if optimize:
        df_all = optimize_dengue_dtypes(df_all)

    df_all.to_parquet(DENGUE_PARQUET, index=False)
    print(f"Guardado: {DENGUE_PARQUET} ({len(df_all):,} filas)")
    return DENGUE_PARQUET


def load_dengue(
    mode: LoadMode = "year",
    *,
    year: int = 2022,
    sample_frac: float = 0.05,
    random_state: int = 42,
    columns: list[str] | None = None,
    optimize: bool = True,
) -> pd.DataFrame:
    """
    Carga dengue sin tumbar el notebook.

    - year: un solo año desde Excel (~1-2 min, ~150 MB RAM)
    - parquet: dataset completo desde Parquet (rápido; requiere build previo)
    - sample: muestra aleatoria del Parquet (ideal para probar gráficos)
    """
    if mode == "year":
        return load_dengue_year(year, columns=columns, optimize=optimize)

    if not DENGUE_PARQUET.exists():
        raise FileNotFoundError(
            f"No existe {DENGUE_PARQUET}. "
            "Genera el archivo con: uv run python -m src.load_data"
        )

    df = pd.read_parquet(DENGUE_PARQUET, columns=columns)
    if mode == "parquet":
        return df
    if mode == "sample":
        if not 0 < sample_frac <= 1:
            raise ValueError("sample_frac debe estar entre 0 y 1")
        return df.sample(frac=sample_frac, random_state=random_state).reset_index(drop=True)

    raise ValueError(f"Modo no soportado: {mode}")


def make_sample_dengue_data(n_municipios: int = 10) -> pd.DataFrame:
    """
    Dataset de ejemplo para validar el EDA cuando data/raw está vacío.
    Columnas alineadas con el caso de dengue (epidemiológico + climático).
    """
    import numpy as np

    rng = np.random.default_rng(42)
    municipios = [
        "Santa Marta", "Cartagena", "Barranquilla", "Montería", "Sincelejo",
        "Valledupar", "Riohacha", "Cúcuta", "Bucaramanga", "Cali",
    ][:n_municipios]

    return pd.DataFrame({
        "municipio": municipios,
        "casos": rng.integers(50, 800, size=n_municipios),
        "fallecimientos": rng.integers(0, 15, size=n_municipios),
        "temperatura_c": np.round(rng.uniform(24, 34, size=n_municipios), 1),
        "lluvia_mm": np.round(rng.uniform(50, 300, size=n_municipios), 1),
        "humedad_pct": np.round(rng.uniform(60, 95, size=n_municipios), 1),
    })


if __name__ == "__main__":
    build_dengue_parquet(force=True)
