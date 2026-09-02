# Fuentes de datos y diccionario

## Enlace del equipo

[Google Drive — Grupo 3](https://drive.google.com/drive/u/1/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH)

## Fuentes oficiales identificadas

| Fuente | Datos | Uso en el análisis |
|--------|-------|-------------------|
| **INS / SIVIGILA** | Casos y fallecimientos históricos por dengue | Variable dependiente, incidencia, mortalidad |
| **IDEAM** | Temperatura, lluvia, humedad | Variables climáticas predictoras |
| **DANE** | Datos demográficos, densidad poblacional | Contexto territorial y riesgo poblacional |
| **Secretarías de Salud** | Saneamiento, presencia de criaderos | Factores ambientales y de vector |

## Inventario de archivos (descargados en `data/raw/`)

| Archivo | Registros | Descripción | Estado |
|---------|-----------|-------------|--------|
| `Datos_2019_210.xlsx` | 123,641 | Casos dengue (evento 210) — 2019 | Descargado |
| `Datos_2020_210.xlsx` | 76,419 | Casos dengue (evento 210) — 2020 | Descargado |
| `Datos_2021_210.xlsx` | 49,325 | Casos dengue (evento 210) — 2021 | Descargado |
| `Datos_2022_210.xlsx` | 65,691 | Casos dengue (evento 210) — 2022 | Descargado |
| `Datos_2023_210.xlsx` | 126,411 | Casos dengue (evento 210) — 2023 | Descargado |
| `Datos_2024_210.xlsx` | 309,627 | Casos dengue (evento 210) — 2024 | Descargado |
| `Datos_2025_210.xlsx` | 120,564 | Casos dengue (evento 210) — 2025 | Descargado |

**Total:** ~871,678 registros · Hoja: `Datos` · 69 columnas · `COD_EVE = 210` (dengue)

## Diccionario de columnas (SIVIGILA — evento 210)

| Columna | Descripción | Uso en el análisis |
|---------|-------------|-------------------|
| `CONSECUTIVE` | Consecutivo del caso | Identificador |
| `COD_EVE` | Código del evento (210 = dengue) | Filtro |
| `FEC_NOT`, `SEMANA`, `ANO` | Fecha de notificación, semana, año | Serie temporal |
| `EDAD`, `SEXO` | Edad y sexo del paciente | Perfil epidemiológico |
| `COD_DPTO_O`, `COD_MUN_O` | Depto/municipio de ocurrencia | Análisis territorial |
| `Departamento_ocurrencia`, `Municipio_ocurrencia` | Nombres territorio ocurrencia | Reportes y mapas |
| `CON_FIN`, `FEC_DEF` | Condición final, fecha de defunción | Mortalidad |
| `Estado_final_de_caso`, `nom_est_f_caso` | Estado final del caso | Clasificación desenlace |
| `PAC_HOS`, `FEC_HOS` | Hospitalización y fecha | Severidad |
| `confirmados` | Caso confirmado | Filtro de casos |
| `TIP_CAS` | Tipo de caso | Clasificación |

_Columnas completas (69):_ ver archivo Excel o listado en repo.

## Variables pendientes (otras fuentes)

| Fuente | Variables | Estado |
|--------|-----------|--------|
| IDEAM | Temperatura, lluvia, humedad | Pendiente integrar |
| DANE | Población, densidad | Pendiente integrar |
| Secretarías de Salud | Saneamiento, criaderos | Pendiente integrar |

## Calidad de datos observada

| Aspecto | Hallazgo | Acción |
|---------|----------|--------|
| Valores nulos | *Pendiente* | Revisar en EDA |
| Duplicados | *Pendiente* | Revisar en EDA |
| Consistencia territorial | *Pendiente* | Unificar códigos DANE/municipio |
| Granularidad temporal | *Pendiente* | Alinear periodos entre fuentes |

## Notas

- Los archivos no se versionan en git (~555 MB total); cada persona los descarga con `gdown` o manualmente.
- Descarga automática: `gdown --folder "https://drive.google.com/drive/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH" -O data/raw/`
