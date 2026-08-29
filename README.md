# Proyecto Análisis de Datos I — Taller 1

**Grupo 3** | Catálogo de servicios de TI

Repositorio de trabajo del equipo. El contenido (documentación, notebook y análisis) está **en construcción**; iremos completándolo según tengamos la información del caso y los datos del Drive.

## Problema (borrador)

La empresa cuenta con un catálogo de servicios de TI, pero la información puede presentar diferencias en su nivel de detalle, actualización y cumplimiento de los ANS. Esto dificulta identificar cuáles servicios tienen mayor demanda y cuáles presentan incumplimientos.

## Objetivo del taller

1. Definir el problema, justificación y pregunta SMART.
2. Construir un análisis exploratorio de datos (EDA) que responda la pregunta SMART.

## Fuente de datos

[Google Drive — Grupo 3](https://drive.google.com/drive/u/1/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH)

Descarga los archivos y colócalos en `data/raw/`. Ver instrucciones en [`data/README.md`](data/README.md).

## Configuración del entorno

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

El entorno `.venv` puede ya existir en el repo. En Cursor/VS Code el intérprete apunta a `.venv` vía `.vscode/settings.json`.

Para abrir el notebook:

```bash
source .venv/bin/activate
jupyter lab
```

Kernel: **Python (proyecto_analisis_de_datos_I)**.

## Estado actual

| Área | Estado |
|------|--------|
| Estructura del repo | Lista |
| Documentación (`docs/taller1/`) | Respuestas del taller completadas |
| Datos en `data/raw/` | Pendiente descarga del Drive |
| Notebook EDA | Esqueleto — sección D pendiente |
| Análisis final | Pendiente |

## Estructura del repositorio

| Carpeta / archivo | Contenido |
|-------------------|-----------|
| [`docs/taller1/`](docs/taller1/) | Definición del problema, pregunta SMART, justificación IA y resumen para entrega |
| [`docs/datos/`](docs/datos/) | Fuentes de datos y diccionario de columnas |
| [`data/raw/`](data/raw/) | Datos originales del Drive (no versionados si son grandes) |
| [`data/processed/`](data/processed/) | Datos limpios exportados del EDA |
| [`notebooks/`](notebooks/) | Notebook Jupyter del EDA |
| [`src/`](src/) | Utilidades de carga y configuración de rutas |

## Documentación del taller

- [Definición del problema](docs/taller1/definicion_problema.md)
- [Pregunta SMART](docs/taller1/pregunta_smart.md)
- [Justificación IA / Ciencia de Datos](docs/taller1/justificacion_ia.md)
- [Resumen para entrega](docs/taller1/resumen_entrega.md)
