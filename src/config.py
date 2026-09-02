"""Configuración de rutas del proyecto."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

SUPPORTED_EXTENSIONS = {".csv", ".xlsx", ".xls"}

DENGUE_FILE_PATTERN = "Datos_*_210.xlsx"
DENGUE_PARQUET = DATA_PROCESSED / "dengue_sivigila.parquet"
