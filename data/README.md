# Datos del proyecto

## Fuente

[Google Drive — Grupo 3](https://drive.google.com/drive/u/1/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH)

## Cómo agregar los datos

1. Abre el enlace del Drive y descarga la carpeta o los archivos del grupo.
2. Copia los archivos originales en `data/raw/` **sin renombrar** (o documenta cualquier cambio en [`docs/datos/fuentes_y_diccionario.md`](../../docs/datos/fuentes_y_diccionario.md)).
3. No subas a git archivos mayores a ~10 MB; el `.gitignore` excluye el contenido de `raw/` y `processed/`.

## Estructura

| Carpeta | Uso |
|---------|-----|
| `data/raw/` | Archivos originales del Drive (CSV, Excel, etc.) |
| `data/processed/` | Tablas limpias o agregadas exportadas desde el notebook |

## Formatos esperados

- CSV (`.csv`)
- Excel (`.xlsx`, `.xls`)

El módulo `src/load_data.py` detecta automáticamente estos formatos en `data/raw/`.

## Si `data/raw/` está vacío

El notebook `notebooks/taller1_eda_catalogo_ti.ipynb` puede generar un **dataset de ejemplo** para validar el flujo del análisis. Reemplázalo con datos reales cuando estén disponibles.

## Próximo paso

Tras colocar los archivos, actualiza el diccionario en [`docs/datos/fuentes_y_diccionario.md`](../../docs/datos/fuentes_y_diccionario.md) con: nombre de archivo, columnas, tipos y uso en el EDA.
