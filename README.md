# Proyecto Análisis de Datos I — Predicción de brotes de dengue

**Grupo 3** · Curso Análisis de Datos I  
**Estado:** entregas de Taller 1, Taller 2 y Taller 3 **terminadas**

Repositorio del equipo: definición del problema, EDA nacional y departamental, arquitectura de datos y comparación de modelos de clasificación sobre notificaciones SIVIGILA (evento 210 — Dengue).

**Video explicativo:** [https://www.youtube.com/watch?v=ATXBgDIwhS8](https://www.youtube.com/watch?v=ATXBgDIwhS8)

## Entregables

| Taller | Entregable | Ubicación |
|--------|------------|-----------|
| 1 | Notebook EDA nacional 2025 | [`notebooks/taller1_eda_dengue.ipynb`](notebooks/taller1_eda_dengue.ipynb) |
| 1 | Documentación (problema, SMART, IA) | [`docs/taller1/`](docs/taller1/) |
| 2 | Notebook EDA Valle del Cauca 2025 | [`notebooks/taller2_eda_dengue.ipynb`](notebooks/taller2_eda_dengue.ipynb) |
| 2 | Arquitectura de datos | [`docs/Propuesta_arquitectura_datos_dengue_taller2.pdf`](docs/Propuesta_arquitectura_datos_dengue_taller2.pdf) |
| 3 | Comparación de modelos de clasificación | [`notebooks/taller3_modelos_clasificacion.ipynb`](notebooks/taller3_modelos_clasificacion.ipynb) |
| Complemento | Dashboard interactivo | [`app/dashboard.py`](app/dashboard.py) |
| Datos | Fuentes y diccionario SIVIGILA | [`docs/datos/fuentes_y_diccionario.md`](docs/datos/fuentes_y_diccionario.md) |

## Problema

El aumento recurrente de casos de dengue genera sobrecarga hospitalaria y presión sobre la red de atención. Con datos SIVIGILA (INS, evento 210) se caracteriza **cuándo** y **dónde** se concentran los casos, y se clasifica riesgo de hospitalización y semanas de alta transmisión para orientar vigilancia y priorización territorial.

No se mide mortalidad: `FEC_DEF` está 100 % nulo en el Excel 2025.

### Pregunta SMART (visión del proyecto)

¿Puede un sistema de analítica predictiva basado en IA anticipar brotes de dengue con precisión > 80 %, reduciendo ≥ 20 % la mortalidad y ≥ 30 % el tiempo de respuesta sanitaria en un piloto de 6 meses, usando datos epidemiológicos de SIVIGILA (INS)?

En los talleres esa visión se baja a lo medible con el Excel: EDA 2025 (nacional y Valle) y modelos de clasificación en el Valle. La meta de precisión > 80 % **no se alcanza** con las variables clínicas disponibles en SIVIGILA (ver Taller 3).

## Qué hicimos

### Taller 1 — EDA nacional 2025

Notebook: [`notebooks/taller1_eda_dengue.ipynb`](notebooks/taller1_eda_dengue.ipynb)

- Definición del problema, pregunta SMART, justificación de IA y diccionario de variables.
- Limpieza de `Datos_2025_210.xlsx` (~120,5 mil filas crudas; ~118 mil con `FEC_NOT` en 2025).
- Análisis univariado y bivariado (tiempo, territorio, demografía, hospitalización).

**Hallazgos**

- **H1 (estacionalidad):** pico de casos en ene–feb / primeras semanas epidemiológicas.
- **H2 (heterogeneidad territorial):** top 10 departamentos ≈ 70 % de los casos (Bolívar, Santander, Córdoba).
- **H3 (perfil Valle):** ~7.441 casos (6,3 % del país); edad media más alta, sexo equilibrado, hospitalización menor que el promedio nacional.
- **Confirmados:** ≈ 75 % de los casos.

### Taller 2 — EDA Valle del Cauca 2025

Notebook: [`notebooks/taller2_eda_dengue.ipynb`](notebooks/taller2_eda_dengue.ipynb)

Baja el alcance de lo nacional a **un año y un departamento**. Universo: notificaciones con ocurrencia en Valle del Cauca y `FEC_NOT` 2025 (7.441 casos). Incluye propuesta de arquitectura (obtención → almacenes → ETL → tipos → muestra).

**Pregunta SMART del taller:** ¿el top 10 de municipios concentra ≥ 60 % de las notificaciones, con una ventana de pico y un perfil (edad, sexo, % hospitalización, gestantes) que permita priorizar focos municipales?

**Hallazgos**

- **H1:** estacionalidad intra-anual en el Valle (ventana de pico identificable).
- **H2:** heterogeneidad municipal (focos; hospitalización desigual entre municipios).
- **H3:** perfil demográfico y de poblaciones (edad, sexo, gestantes) no homogéneo entre focos.

Exporta `data/processed/dengue_sivigila_2025_valle_limpio.parquet` (no pisa el parquet nacional del Taller 1).

### Taller 3 — Modelos de clasificación (Valle 2025)

Notebook: [`notebooks/taller3_modelos_clasificacion.ipynb`](notebooks/taller3_modelos_clasificacion.ipynb)

Continúa el EDA del Taller 2. Se comparan, en las mismas condiciones, línea base, regresión logística, Naive Bayes, KNN, árbol de decisión, Random Forest, Gradient Boosting y SVM. Métricas prioritarias: ROC-AUC, PR-AUC, recall, F1 y accuracy balanceada (clases desbalanceadas).

| Enfoque | Unidad | Objetivo | Pregunta de negocio |
|---------|--------|----------|---------------------|
| **A. Hospitalización** | Caso (7.441 filas; 26 % hospitalizados) | `hospitalizado` | Al notificar, ¿el caso requerirá cama? |
| **B. Alerta de brote** | Municipio × semana (top 10) | semana siguiente > P75 del municipio | ¿Se puede anticipar alta transmisión? |

**Resultados**

- **A:** mejor modelo **Random Forest** (afinado): ROC-AUC CV **0,741**; en prueba ROC-AUC 0,715, recall 0,55. Variables que más pesan: municipio, régimen de salud, edad y días entre síntomas y consulta. Gradient Boosting queda casi empatado; logística si se prioriza interpretabilidad.
- **B:** la **regresión logística** ordena bien el riesgo (ROC-AUC ≈ 0,79), pero con un solo año **ningún modelo es aún confiable para emitir alertas**; la regla de persistencia funciona igual o mejor en la práctica.
- No se usa la institución notificadora (`Nombre_upgd`) en el modelo principal: sube el AUC (~0,88) por tipo de IPS, no por el paciente (fuga / no generalizable a riesgo individual).

**Limitación:** SIVIGILA no trae signos de alarma, plaquetas ni comorbilidades. Extensión natural: años 2019–2025 (ya en Drive) y clima IDEAM.

## Fuente de datos

| Fuente | Uso |
|--------|-----|
| **INS / SIVIGILA** — `Datos_2025_210.xlsx` (~120,5 k filas) | EDA Taller 1 (nacional) y Taller 2–3 (filtro Valle) |
| Excel 2019–2024 | Disponibles para dashboard y trabajo futuro; no calificados en estos talleres |
| IDEAM, DANE | Identificados; **no integrados** |

Archivos multi-año (2019–2025) en Drive del equipo: [Google Drive — Grupo 3](https://drive.google.com/drive/u/1/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH).

Coloca los Excel en `data/raw/`. Instrucciones: [`data/README.md`](data/README.md).

## Configuración del entorno

Con [uv](https://docs.astral.sh/uv/) (recomendado):

```bash
uv sync
```

Crea `.venv` e instala las dependencias de `pyproject.toml`.

### Notebooks

```bash
uv run jupyter lab notebooks/taller1_eda_dengue.ipynb
uv run jupyter lab notebooks/taller2_eda_dengue.ipynb
uv run jupyter lab notebooks/taller3_modelos_clasificacion.ipynb
```

O abre el notebook en Cursor/VS Code y selecciona el intérprete `.venv` / kernel del proyecto.

El Taller 3 espera el parquet del Valle generado en el Taller 2:

```text
data/processed/dengue_sivigila_2025_valle_limpio.parquet
```

### Dashboard Streamlit

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

Para reproducir los tres talleres basta con `Datos_2025_210.xlsx`.

## Estado

| Área | Estado |
|------|--------|
| Taller 1 — EDA nacional 2025 | **Terminado** |
| Taller 2 — EDA Valle 2025 + arquitectura | **Terminado** |
| Taller 3 — modelos de clasificación | **Terminado** |
| Video explicativo | [YouTube](https://www.youtube.com/watch?v=ATXBgDIwhS8) |
| Datos en `data/raw/` | 7 Excel (2019–2025); análisis calificado usa 2025 |
| Datos limpios | `dengue_sivigila_2025_limpio.parquet` y `dengue_sivigila_2025_valle_limpio.parquet` |
| Dashboard Streamlit | Listo |
| Clima IDEAM / demografía DANE / mortalidad | Fuera de alcance (datos no disponibles o no integrados) |

## Estructura del repositorio

| Carpeta / archivo | Contenido |
|-------------------|-----------|
| [`docs/taller1/`](docs/taller1/) | Problema, SMART, justificación IA y resumen de entrega |
| [`docs/datos/`](docs/datos/) | Fuentes y diccionario de columnas SIVIGILA |
| [`docs/Propuesta_arquitectura_datos_dengue_taller2.pdf`](docs/Propuesta_arquitectura_datos_dengue_taller2.pdf) | Arquitectura Taller 2 |
| [`data/raw/`](data/raw/) | Excel originales (no versionados en git) |
| [`data/processed/`](data/processed/) | Parquet limpios exportados del EDA |
| [`notebooks/`](notebooks/) | Taller 1, Taller 2 y Taller 3 |
| [`src/`](src/) | Carga, limpieza y rutas (`dengue_clean.py`, `load_data.py`) |
| [`app/`](app/) | Dashboard Streamlit |

## Integrantes (Grupo 3)

Juan Manuel Román Villa · Dora Valencia Martínez · Julian Aguilar Mayorga · Camilo Percy Ocampo · Viviana Fernández Payan · Giovanni Jaramillo Bolaños · Victor Manuel Hurtado López
