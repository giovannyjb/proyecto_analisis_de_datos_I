# Justificación del uso de IA / Ciencia de Datos

## Problema que aborda el análisis

El catálogo de servicios TI contiene muchos registros con varias dimensiones (categoría, demanda, cumplimiento ANS, actualización). Revisar esto manualmente es lento y propenso a omitir patrones. La ciencia de datos y herramientas de IA permiten explorar, visualizar y sintetizar esa información de forma sistemática.

## Técnica aplicada en el Taller 1

| Técnica | Uso en este proyecto | Por qué es pertinente |
|---------|----------------------|----------------------|
| **Análisis exploratorio de datos (EDA)** | Perfilado de tablas, conteos, distribuciones, nulos, duplicados | Primera fase obligatoria para entender calidad y estructura del catálogo antes de cualquier modelo |
| **Análisis descriptivo** | Rankings de demanda, % cumplimiento ANS, distribución por categoría | Responde directamente la pregunta SMART sin necesidad de predicción |
| **Visualización** | Barras (top servicios), heatmaps (demanda vs cumplimiento) | Facilita comunicar hallazgos a gestión TI no técnica |
| **IA generativa (asistente de código)** | Generación y refinamiento del notebook, limpieza de datos, narrativa del análisis | Acelera el prototipo funcional exigido por el taller; el equipo valida y adapta el código |

## Por qué no usar ML en esta fase

El taller 1 pide una **foto del estado actual** (analítica descriptiva). Un modelo predictivo o de clasificación requeriría datos históricos limpios y una pregunta orientada al futuro. El EDA valida si esos datos existen y son suficientes para una fase 2.

## Técnicas futuras (si el problema evoluciona)

| Tipo de problema IA | Escenario | Datos necesarios |
|-----------------------|-----------|------------------|
| **Clasificación** | Predecir si un ticket cumplirá o no el ANS | Historial de tickets con etiqueta cumple/incumple |
| **Regresión** | Estimar tiempo de resolución | Tiempos reales, categoría, prioridad, carga |
| **Clustering** | Agrupar servicios por perfil similar | Matriz servicio × métricas de demanda y SLA |

## Contribución esperada al negocio

- Identificar servicios de **alta demanda y bajo cumplimiento** para acción inmediata.
- Detectar **inconsistencias en el catálogo** (datos faltantes, desactualizados).
- Base cuantitativa para **priorizar mejoras** en ANS y actualización del catálogo.

## Evidencia de uso de IA generativa

Documentar en el notebook (sección final):

- Herramienta usada (ej. Cursor, ChatGPT, Copilot).
- Qué partes del código o análisis fueron asistidas por IA.
- Qué validaciones realizó el equipo (datos, lógica, conclusiones).
