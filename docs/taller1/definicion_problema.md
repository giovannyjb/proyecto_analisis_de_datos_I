# Definición del problema — Taller 1

## Tabla de análisis del problema

| Campo | Contenido |
|-------|-----------|
| **Descripción del problema e impacto en la organización (incluyendo métrica)** | El aumento recurrente de casos de dengue en el territorio nacional genera una sobrecarga hospitalaria y un incremento en la mortalidad de la población afectada, lo que constituye una amenaza directa para la salud pública. Se requiere validar la tasa de mortalidad en relación con la incidencia de picaduras del vector y determinar los territorios con mayores índices de fallecimientos, con el fin de orientar políticas de prevención y respuesta sanitaria. **Métricas clave:** tasa de mortalidad, incidencia de casos, índice de fallecimientos por territorio. |
| **Tipo de analítica** | **Predictiva** — el análisis busca anticipar los territorios y periodos con mayor riesgo de brotes de dengue y fallecimientos, utilizando variables epidemiológicas, climáticas y demográficas. Esto permite generar alertas tempranas y orientar la toma de decisiones en salud pública. |
| **Caso similar (estado del arte)** | Ver referencias en [`justificacion_ia.md`](justificacion_ia.md). Resumen: modelos predictivos (regresión logística, redes neuronales, árboles de decisión) para anticipar hospitalización y mortalidad; factores ambientales (temperatura, humedad, lluvias) como indicadores de brotes; sistemas automatizados con machine learning para detección temprana y alertas predictivas. |
| **Tipo de problema de IA** | **Regresión** — estimar el número esperado de casos y fallecimientos en los diferentes municipios del país. |
| **Datos necesarios y disponibilidad** | Datos históricos de casos y fallecimientos por dengue (INS, SIVIGILA); variables meteorológicas (IDEAM): temperatura, lluvia, humedad; datos demográficos y de densidad poblacional (DANE); información sobre saneamiento y presencia de criaderos (Secretarías de Salud); coordenadas geográficas para análisis espacial y mapas de riesgo. **Fuente del equipo:** [Google Drive — Grupo 3](https://drive.google.com/drive/u/1/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH). Ver [`docs/datos/fuentes_y_diccionario.md`](../../datos/fuentes_y_diccionario.md). |
| **Impacto en el negocio con métricas** | 1. Reducción de la tasa de mortalidad por el vector en los territorios con mayores incidencias para los meses continuos. 2. Disminuir la respuesta sanitaria ante brotes de dengue mediante la integración de datos epidemiológicos y climáticos. 3. Incrementar la cobertura de vigilancia de municipios con alto riesgo de brotes. |
| **Pregunta SMART** | Ver documento dedicado: [`pregunta_smart.md`](pregunta_smart.md). |

## Complejidad del problema

| Aspecto | Descripción |
|---------|-------------|
| Variables involucradas | Casos y fallecimientos por municipio, temperatura, lluvia, humedad, densidad poblacional, saneamiento, criaderos, coordenadas geográficas, periodo temporal |
| Procesos involucrados | Vigilancia epidemiológica (SIVIGILA), monitoreo climático, respuesta sanitaria territorial, políticas de prevención |
| Dificultad técnica | Alta — integración de múltiples fuentes (INS, IDEAM, DANE, Secretarías de Salud), análisis espacial y modelos predictivos |

## Notas del equipo

- Actualizar diccionario de datos cuando los archivos estén en `data/raw/`.
- El EDA (Taller 1) explora los datos antes de construir el modelo de regresión.
