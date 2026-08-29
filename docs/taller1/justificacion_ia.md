# Justificación del uso de IA / Ciencia de Datos

## Problema que aborda el análisis

El catálogo de servicios TI y los registros de atención contienen múltiples variables (categoría, ANS, demanda, tiempos, cumplimiento). Revisar esto manualmente es lento y no permite anticipar incumplimientos. La ciencia de datos e IA permiten explorar patrones, medir cumplimiento y construir modelos de clasificación.

## Técnicas aplicadas en este proyecto

| Técnica | Uso en este proyecto | Por qué es pertinente |
|---------|----------------------|----------------------|
| **Análisis exploratorio de datos (EDA)** | Perfilado del catálogo y datos de atención; nulos, distribuciones, relaciones | Primera fase para validar calidad y variables antes del modelo |
| **Análisis descriptivo** | Servicios existentes, demanda, cumplimiento ANS, mejores/peores resultados, distribución | Responde al estado actual del catálogo y contexto del problema |
| **Clasificación (IA)** | Predecir si un servicio cumplirá o incumplirá ANS en 2026 | Variable objetivo binaria (1 = Cumple, 0 = No cumple); alineada con la pregunta SMART |
| **Visualización** | Distribución de servicios, demanda vs cumplimiento | Comunicar hallazgos a gestión TI |
| **IA generativa** | Asistencia en notebook, limpieza de datos y documentación | Acelera el prototipo del taller; el equipo valida resultados |

## Por qué clasificación es pertinente

La pregunta SMART pide **predecir** cumplimiento o incumplimiento de ANS. Eso corresponde a un problema de **clasificación binaria**: la variable objetivo es Cumple ANS (Sí/No). Con datos de atención prestada y características del servicio, un modelo puede identificar patrones asociados al incumplimiento y alertar servicios en riesgo durante 2026.

## Contribución esperada al negocio

- Anticipar servicios con riesgo de incumplimiento ANS.
- Priorizar recursos en servicios de alta demanda y bajo cumplimiento.
- Apoyar metas de: disponibilidad ≥ 99.5%, cumplimiento ANS ≥ 95%, satisfacción ≥ 90%, resolución ≤ 8 h.
- Fortalecer continuidad operativa y soporte a procesos estratégicos.

## Evidencia de uso de IA generativa

Documentar en el notebook (sección final):

- Herramienta usada (ej. Cursor, ChatGPT, Copilot).
- Qué partes del código o análisis fueron asistidas por IA.
- Qué validaciones realizó el equipo (datos, lógica, conclusiones).
