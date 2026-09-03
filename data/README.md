# Datos del proyecto — Dengue (SIVIGILA)

## Uso en el Taller 1

El EDA y el resumen de entrega usan **únicamente**:

```text
data/raw/Datos_2025_210.xlsx
```

(~120.5k notificaciones · evento 210 · hoja `Datos`). El dataset limpio se exporta a:

```text
data/processed/dengue_sivigila_2025_limpio.parquet
```

Los demás años (2019–2024) están disponibles para el dashboard y fases posteriores; no forman parte del análisis calificado del Taller 1.

## Fuentes oficiales

| Fuente | Datos | En este taller |
|--------|-------|----------------|
| INS / SIVIGILA | Casos notificados de dengue (evento 210) | **Sí** — Excel 2025 |
| IDEAM | Temperatura, lluvia, humedad | No integrado |
| DANE | Demografía y densidad | No integrado |
| Secretarías de Salud | Saneamiento / criaderos | No integrado |

## Fuente del equipo

[Google Drive — Grupo 3](https://drive.google.com/drive/u/1/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH)

### Descarga automática

Desde la raíz del repo:

```bash
uv run gdown --folder "https://drive.google.com/drive/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH" -O data/raw/
```

O descarga manual y copia los `.xlsx` a `data/raw/` **sin renombrar**.

## Inventario esperado en `data/raw/`

| Archivo | ~Registros | Rol |
|---------|------------|-----|
| `Datos_2019_210.xlsx` | 123,641 | Disponible (dashboard / futuro) |
| `Datos_2020_210.xlsx` | 76,419 | Disponible (dashboard / futuro) |
| `Datos_2021_210.xlsx` | 49,325 | Disponible (dashboard / futuro) |
| `Datos_2022_210.xlsx` | 65,691 | Disponible (dashboard / futuro) |
| `Datos_2023_210.xlsx` | 126,411 | Disponible (dashboard / futuro) |
| `Datos_2024_210.xlsx` | 309,627 | Disponible (dashboard / futuro) |
| `Datos_2025_210.xlsx` | 120,564 | **EDA Taller 1** |

**Total aproximado:** ~872k registros · 69 columnas · `COD_EVE = 210`.

## Estructura

| Carpeta | Uso |
|---------|-----|
| `data/raw/` | Excel originales SIVIGILA (`Datos_YYYY_210.xlsx`) |
| `data/processed/` | Parquet limpios (`dengue_sivigila_{año}_limpio.parquet`) |

Los archivos grandes **no** se versionan en git (ver `.gitignore`). Solo se versionan los `.gitkeep` de cada carpeta.

## Limpieza y carga

- Módulo: [`src/dengue_clean.py`](../src/dengue_clean.py) — parseo de fechas, filtro `FEC_NOT` al año, features (`edad_anios`, `hospitalizado`, etc.).
- Carga: [`src/load_data.py`](../src/load_data.py) — detecta Excel/CSV en `data/raw/`.
- Diccionario de columnas: [`docs/datos/fuentes_y_diccionario.md`](../docs/datos/fuentes_y_diccionario.md).

## Notas de calidad (2025)

| Aspecto | Hallazgo |
|---------|----------|
| `FEC_DEF` | 100 % nulo → no se analiza mortalidad en este taller |
| Fechas | Texto `dd/mm/yyyy` (a veces con a. m. / p. m.) → se convierten a `datetime` |
| Filas fuera de año | Se excluyen notificaciones cuyo `FEC_NOT` no coincide con el año del archivo |
| Columnas vacías | Se eliminan `GRU_POB`, `CBMTE`, campos militares, etc. |
