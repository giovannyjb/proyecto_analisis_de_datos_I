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


def make_sample_catalog_data(n_services: int = 15) -> pd.DataFrame:
    """
    Dataset de ejemplo para validar el EDA cuando data/raw está vacío.
    Columnas alineadas con el caso de negocio del catálogo TI.
    """
    import numpy as np

    rng = np.random.default_rng(42)
    services = [f"Servicio TI {i:02d}" for i in range(1, n_services + 1)]
    categories = rng.choice(
        ["Infraestructura", "Aplicaciones", "Soporte", "Seguridad", "Redes"],
        size=n_services,
    )
    demand = rng.integers(20, 500, size=n_services)
    compliance = rng.uniform(0.55, 0.98, size=n_services)

    return pd.DataFrame({
        "servicio": services,
        "categoria": categories,
        "volumen_solicitudes": demand,
        "pct_cumplimiento_ans": np.round(compliance * 100, 1),
    })
