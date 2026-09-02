# Datos del proyecto — Dengue

## Fuentes oficiales

| Fuente | Datos |
|--------|-------|
| INS / SIVIGILA | Casos y fallecimientos históricos por dengue |
| IDEAM | Temperatura, lluvia, humedad |
| DANE | Datos demográficos y densidad poblacional |
| Secretarías de Salud | Saneamiento y presencia de criaderos |

## Fuente del equipo

[Google Drive — Grupo 3](https://drive.google.com/drive/u/1/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH)

## Cómo agregar los datos

1. Descarga los archivos del Drive o de las fuentes oficiales.
2. Copia los archivos originales en `data/raw/` **sin renombrar** (o documenta cambios en [`docs/datos/fuentes_y_diccionario.md`](../docs/datos/fuentes_y_diccionario.md)).
3. No subas a git archivos mayores a ~10 MB; el `.gitignore` excluye el contenido de `raw/` y `processed/`.

## Estructura

| Carpeta | Uso |
|---------|-----|
| `data/raw/` | Archivos originales (CSV, Excel, etc.) |
| `data/processed/` | Tablas limpias o agregadas exportadas desde el notebook |

## Formatos esperados

- CSV (`.csv`)
- Excel (`.xlsx`, `.xls`)

El módulo `src/load_data.py` detecta automáticamente estos formatos en `data/raw/`.

## Próximo paso

Tras colocar los archivos, actualiza el diccionario en [`docs/datos/fuentes_y_diccionario.md`](../docs/datos/fuentes_y_diccionario.md).
