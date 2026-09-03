# Proyecto Análisis de Datos I — Taller 1

**Grupo 3** | Predicción de brotes de dengue  
**Entrega:** 3 de septiembre de 2026

Repositorio del equipo para el Taller 1: definición del problema, pregunta SMART, justificación de IA y análisis exploratorio (EDA) sobre notificaciones SIVIGILA 2025.

## Entregables del taller

| Entregable | Ubicación |
|------------|-----------|
| Notebook EDA (principal) | [`notebooks/taller1_eda_dengue.ipynb`](notebooks/taller1_eda_dengue.ipynb) |
| Resumen consolidado (Moodle) | [`docs/taller1/resumen_entrega.md`](docs/taller1/resumen_entrega.md) |
| Definición del problema | [`docs/taller1/definicion_problema.md`](docs/taller1/definicion_problema.md) |
| Pregunta SMART | [`docs/taller1/pregunta_smart.md`](docs/taller1/pregunta_smart.md) |
| Justificación IA / Ciencia de Datos | [`docs/taller1/justificacion_ia.md`](docs/taller1/justificacion_ia.md) |
| Fuentes y diccionario | [`docs/datos/fuentes_y_diccionario.md`](docs/datos/fuentes_y_diccionario.md) |
| Dashboard interactivo (opcional) | [`app/dashboard.py`](app/dashboard.py) |

> El notebook es el entregable canónico: incluye problema, SMART, justificación, diccionario, limpieza, EDA (H1–H3) y evidencia de uso de IA.

## Problema

El aumento recurrente de casos de dengue genera sobrecarga hospitalaria y presión sobre la red de atención. Con datos SIVIGILA (evento 210) se caracteriza **cuándo** y **dónde** se concentran los casos para orientar vigilancia y priorización territorial.

En este taller **no** se mide mortalidad (`FEC_DEF` está 100 % nulo en el Excel 2025) ni se entrena el modelo predictivo.

## Pregunta SMART (resumen)

¿Puede un sistema de analítica predictiva basado en IA anticipar brotes de dengue con precisión > 80 %, reduciendo ≥ 20 % la mortalidad y ≥ 30 % el tiempo de respuesta sanitaria en un piloto de 6 meses, usando datos epidemiológicos de SIVIGILA (INS)?

**Alcance Taller 1:** EDA sobre `Datos_2025_210.xlsx` (casos, hospitalización, territorio, perfil Valle vs nacional). Las metas de precisión/mortalidad/respuesta quedan para modelado.

Desglose completo: [`docs/taller1/pregunta_smart.md`](docs/taller1/pregunta_smart.md).

## Hallazgos clave del EDA (2025)

- **H1 (estacionalidad):** pico de casos en ene–feb / primeras semanas epidemiológicas.
- **H2 (heterogeneidad territorial):** top 10 departamentos ≈ 70 % de los casos (p. ej. Bolívar, Santander, Córdoba).
- **H3 (perfil Valle):** ~7.4k casos; edad media más alta, sexo equilibrado, hospitalización menor que el promedio nacional.
- **Confirmados:** ≈ 75 % de los casos.

## Fuente de datos

| Fuente | Uso en Taller 1 |
|--------|-----------------|
| **INS / SIVIGILA** — `Datos_2025_210.xlsx` (~120.5k filas) | Única fuente del EDA |
| IDEAM, DANE | Previstas para el proyecto; no integradas aún |

Archivos multi-año (2019–2025) en Drive del equipo: [Google Drive — Grupo 3](https://drive.google.com/drive/u/1/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH).

Coloca los Excel en `data/raw/`. Instrucciones: [`data/README.md`](data/README.md).

## Configuración del entorno

Con [uv](https://docs.astral.sh/uv/) (recomendado):

```bash
uv sync
```

Crea `.venv` e instala las dependencias de `pyproject.toml`.

### Notebook EDA

```bash
uv run jupyter lab notebooks/taller1_eda_dengue.ipynb
```

O abre el notebook en Cursor/VS Code y selecciona el intérprete `.venv` / kernel del proyecto.

### Dashboard Streamlit (opcional)

Exploración interactiva con filtros territoriales y temporales (foco 2025; soporta 2019–2025):

```bash
uv run streamlit run app/dashboard.py
```

Carga `data/processed/dengue_sivigila_{año}_limpio.parquet` o lo genera desde `data/raw/` la primera vez.

### Alternativa con pip

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab notebooks/taller1_eda_dengue.ipynb
```

### Descargar datos (si no están en `data/raw/`)

```bash
uv run gdown --folder "https://drive.google.com/drive/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH" -O data/raw/
```

Para el EDA del Taller 1 basta con `Datos_2025_210.xlsx`.

## Estado actual

| Área | Estado |
|------|--------|
| Documentación (`docs/taller1/`) | Lista para entrega |
| Datos en `data/raw/` | 7 Excel (2019–2025); EDA usa 2025 |
| Notebook EDA | `notebooks/taller1_eda_dengue.ipynb` — secciones 1–9 ejecutadas |
| Datos limpios | `data/processed/dengue_sivigila_2025_limpio.parquet` |
| Dashboard Streamlit | `app/dashboard.py` — listo |
| Modelo de regresión | Pendiente (fases posteriores) |

## Estructura del repositorio

| Carpeta / archivo | Contenido |
|-------------------|-----------|
| [`docs/taller1/`](docs/taller1/) | Problema, SMART, justificación IA y resumen de entrega |
| [`docs/datos/`](docs/datos/) | Fuentes y diccionario de columnas SIVIGILA |
| [`data/raw/`](data/raw/) | Excel originales (no versionados en git) |
| [`data/processed/`](data/processed/) | Parquet limpios exportados del EDA |
| [`notebooks/`](notebooks/) | Notebook del EDA (entregable principal) |
| [`src/`](src/) | Carga, limpieza y rutas (`dengue_clean.py`, `load_data.py`) |
| [`app/`](app/) | Dashboard Streamlit |

## Integrantes (Grupo 3)

Juan Manuel Román Villa · Dora Valencia Martínez · Julian Aguilar Mayorga · Camilo Percy Ocampo · Viviana Fernández Payan · Giovanni Jaramillo Bolaños · Victor Manuel Hurtado López
