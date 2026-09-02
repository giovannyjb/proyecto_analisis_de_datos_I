# Proyecto Análisis de Datos I — Taller 1

**Grupo 3** | Predicción de brotes de dengue

Repositorio de trabajo del equipo. Documentación del taller completada; el EDA y el modelo predictivo se desarrollarán cuando los datos estén en `data/raw/`.

## Problema

El aumento recurrente de casos de dengue en el territorio nacional genera sobrecarga hospitalaria e incremento en la mortalidad. Se requiere validar la tasa de mortalidad frente a la incidencia del vector y determinar territorios con mayores fallecimientos para orientar políticas de prevención y respuesta sanitaria.

## Objetivo del taller

1. Definir el problema, justificación y pregunta SMART.
2. Construir un análisis exploratorio de datos (EDA) que responda la pregunta SMART.

## Pregunta SMART (resumen)

¿Puede un sistema de analítica predictiva basado en IA anticipar brotes de dengue con precisión > 80 %, reduciendo ≥ 20 % la mortalidad y ≥ 30 % el tiempo de respuesta sanitaria en un piloto de 6 meses, usando datos del INS y el IDEAM?

Ver desglose completo en [`docs/taller1/pregunta_smart.md`](docs/taller1/pregunta_smart.md).

## Fuente de datos

- **Oficiales:** INS/SIVIGILA, IDEAM, DANE, Secretarías de Salud
- **Equipo:** [Google Drive — Grupo 3](https://drive.google.com/drive/u/1/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH)

Coloca los archivos descargados en `data/raw/`. Ver [`data/README.md`](data/README.md).

## Configuración del entorno

Con [uv](https://docs.astral.sh/uv/) (recomendado):

```bash
uv sync
```

Eso crea `.venv` e instala las dependencias de `pyproject.toml`. En Cursor/VS Code el intérprete apunta a `.venv` vía `.vscode/settings.json`.

Para abrir el notebook de datos:

```bash
uv run jupyter lab docs/datos/datos.ipynb
```

O abre `docs/datos/datos.ipynb` en Cursor y selecciona el kernel **Python (proyecto_analisis_de_datos_I)** / intérprete `.venv`.

Alternativa con pip:

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Kernel: **Python (proyecto_analisis_de_datos_I)**.

## Estado actual

| Área | Estado |
|------|--------|
| Estructura del repo | Lista |
| Documentación (`docs/taller1/`) | Respuestas del taller — dengue |
| Datos en `data/raw/` | 7 archivos descargados (2019–2025, ~872k registros) |
| Notebook EDA | Estructura completa (secciones 1–9); código EDA pendiente por sección |
| Modelo de regresión | Pendiente |

## Estructura del repositorio

| Carpeta / archivo | Contenido |
|-------------------|-----------|
| [`docs/taller1/`](docs/taller1/) | Definición del problema, pregunta SMART, justificación IA y resumen para entrega |
| [`docs/datos/`](docs/datos/) | Fuentes de datos y diccionario de columnas |
| [`data/raw/`](data/raw/) | Datos originales (no versionados si son grandes) |
| [`data/processed/`](data/processed/) | Datos limpios exportados del EDA |
| [`notebooks/`](notebooks/) | Notebook Jupyter del EDA |
| [`src/`](src/) | Utilidades de carga y configuración de rutas |

## Documentación del taller

- [Definición del problema](docs/taller1/definicion_problema.md)
- [Pregunta SMART](docs/taller1/pregunta_smart.md)
- [Justificación IA / Ciencia de Datos](docs/taller1/justificacion_ia.md)
- [Resumen para entrega](docs/taller1/resumen_entrega.md)
