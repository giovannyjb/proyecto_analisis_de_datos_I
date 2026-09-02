"""Utilidades para cargar datos desde data/raw."""

from pathlib import Path

import pandas as pd

from src.config import DATA_RAW, SUPPORTED_EXTENSIONS


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
