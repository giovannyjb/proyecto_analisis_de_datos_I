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

## Origen y contexto

Los datos provienen de **SIVIGILA** (Sistema de Vigilancia en Salud Pública de Colombia), evento **210 — Dengue**. Cada fila representa una notificación individual de caso. Los archivos se organizan por año (`Datos_YYYY_210.xlsx`).

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

### Diccionario — Datos básicos y clínicos

| Columna | Tipo | Descripción | % nulos |
|---------|------|-------------|---------|
| CONSECUTIVE | int | Identificador único del registro | 0.0 |
| COD_EVE | int | Código del evento (210 = Dengue) | 0.0 |
| FEC_NOT | texto | Fecha de notificación | 0.0 |
| SEMANA | int | Semana epidemiológica | 0.0 |
| ANO | int | Año de notificación | 0.0 |
| COD_PRE | int | Código del prestador de salud | 0.0 |
| COD_SUB | int | Código de sede/subsede del prestador | 0.0 |
| EDAD | int | Edad del paciente | 0.0 |
| UNI_MED | int | Unidad de edad (1=años, 2=meses, 3=días) | 0.0 |
| SEXO | texto | Sexo (M/F) | 0.0 |
| FEC_CON | texto | Fecha de confirmación | 0.0 |
| INI_SIN | texto | Fecha de inicio de síntomas | 0.0 |
| TIP_CAS | int | Tipo de caso (2=Probable, 3=Confirmado) | 0.0 |
| PAC_HOS | int | Hospitalizado (1=Sí, 2=No) | 0.0 |
| FEC_HOS | texto | Fecha de hospitalización | 47.2 |
| CON_FIN | int | Condición final del paciente | 0.0 |
| FEC_DEF | float | Fecha de defunción | 100.0 |
| confirmados | int | Caso confirmado (1=Sí, 0=No) | 0.0 |
| Estado_final_de_caso | int | Código estado final | 0.0 |
| nom_est_f_caso | texto | Estado final (ej. Confirmado por laboratorio) | 0.0 |

### Diccionario — Ubicación geográfica

| Columna | Tipo | Descripción |
|---------|------|-------------|
| COD_PAIS_O / Pais_ocurrencia | int / texto | País de ocurrencia |
| COD_DPTO_O / Departamento_ocurrencia | int / texto | Departamento de ocurrencia |
| COD_MUN_O / Municipio_ocurrencia | int / texto | Municipio de ocurrencia |
| COD_PAIS_R / Pais_residencia | int / texto | País de residencia |
| COD_DPTO_R / Departamento_residencia | int / texto | Departamento de residencia |
| COD_MUN_R / Municipio_residencia | int / texto | Municipio de residencia |
| COD_DPTO_N / Departamento_Notificacion | int / texto | Departamento de notificación |
| COD_MUN_N / Municipio_notificacion | int / texto | Municipio de notificación |
| AREA | int | Área (1=Urbana, 2=Rural, 3=Urbana-rural) |

### Diccionario — Población y afiliación

| Columna | Tipo | Descripción | % nulos |
|---------|------|-------------|---------|
| OCUPACION | texto | Código de ocupación | 0.0 |
| TIP_SS | texto | Régimen (C/S/P/N/I/E) | 0.0 |
| COD_ASE | texto | Código EPS | 3.4 |
| PER_ETN | int | Pertenencia étnica | 0.0 |
| GRU_POB | float | Grupo poblacional | 100.0 |
| nom_grupo | texto | Nombre del grupo poblacional | 0.0 |
| estrato | texto | Estrato socioeconómico | 0.0 |
| GP_DISCAPA … GP_OTROS | int | Grupos poblacionales especiales (1=Sí, 2=No) | 0.0 |
| sem_ges | texto | Semanas de gestación | 0.0 |
| FECHA_NTO | texto | Fecha de nacimiento | 0.03 |

### Diccionario — Metadatos del registro

| Columna | Tipo | Descripción | % nulos |
|---------|------|-------------|---------|
| fuente | int | Fuente de notificación | 0.0 |
| AJUSTE | int | Tipo de ajuste del registro | 0.0 |
| FEC_ARC_XL | texto | Fecha de archivo/exportación | 0.0 |
| FEC_AJU | texto | Fecha del último ajuste | 0.0 |
| va_sispro | int | Validado en SISPRO | 0.0 |
| Nombre_upgd | texto | Unidad Primaria Generadora de Datos | 0.0 |
| Nombre_evento | texto | Nombre del evento (DENGUE) | 0.0 |
| CBMTE | float | Comorbilidad | 100.0 |
| FM_FUERZA / FM_UNIDAD / FM_GRADO | float | Datos de fuerza militar (si aplica) | ~99.5 |

### Valores relevantes observados (muestra 2022)

| Variable | Valores principales |
|----------|---------------------|
| Nombre_evento | DENGUE (100%) |
| nom_est_f_caso | Confirmado por laboratorio (72.6%), Probable (24.0%), Confirmado por Nexo Epidemiológico (3.4%) |
| SEXO | M (53.1%), F (46.9%) |
| PAC_HOS | No hospitalizado (47.2%), Hospitalizado (52.8%) |
| confirmados | 1 (76.0%), 0 (24.0%) |
| TIP_SS | S=Subsidiado, C=Contributivo, P=Particular, N, I, E |

## Variables pendientes (otras fuentes)

| Fuente | Variables | Estado |
|--------|-----------|--------|
| IDEAM | Temperatura, lluvia, humedad | Pendiente integrar |
| DANE | Población, densidad | Pendiente integrar |
| Secretarías de Salud | Saneamiento, criaderos | Pendiente integrar |

## Calidad de datos observada

| Aspecto | Hallazgo | Acción |
|---------|----------|--------|
| Valores nulos | GRU_POB, FEC_DEF, CBMTE al 100%; campos militares ~99.5% | Evaluar exclusión o imputación según análisis |
| Duplicados | CONSECUTIVE es único por archivo | Usar como clave primaria |
| Formato de fechas | Texto con formato `dd/mm/yyyy hh:mm:ss` | Convertir a `datetime` en limpieza |
| Tipos mixtos | OCUPACION tiene tipos mixtos al leer CSV | Usar `low_memory=False` o definir `dtype` |
| Consistencia territorial | *Pendiente* | Unificar códigos DANE/municipio |
| Granularidad temporal | *Pendiente* | Alinear periodos entre fuentes |

## Generación del diccionario

El diccionario completo (con ejemplos por columna) se genera en el notebook `docs/datos/datos.ipynb` y se exporta a `diccionario_Datos_2022_210.csv`.

## Notas

- Los archivos no se versionan en git (~555 MB total); cada persona los descarga con `gdown` o manualmente.
- Descarga automática: `gdown --folder "https://drive.google.com/drive/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH" -O data/raw/`
- Referencia metodológica: [sivirep — datos SIVIGILA](https://epiverse-trace.github.io/sivirep/) y diccionario oficial INS/SIVIGILA.
