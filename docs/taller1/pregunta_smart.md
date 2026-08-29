# Pregunta SMART — Taller 1

## Pregunta

> ¿Es posible predecir, durante el 2026, si un servicio de TI de la empresa cumplirá o incumplirá su ANS, utilizando los datos actuales en la atención prestada y características del servicio?

## Desglose SMART

| Criterio | Cómo se cumple |
|----------|----------------|
| **Específica (Specific)** | Se enfoca en servicios de TI de la empresa y su cumplimiento o incumplimiento de ANS, usando características del servicio y datos de atención prestada. |
| **Medible (Measurable)** | Resultado binario: cumple ANS (`1`) o no cumple (`0`); evaluable con métricas de clasificación (precisión, recall, F1) y cumplimiento global de ANS. |
| **Accionable (Achievable / Actionable)** | Permite anticipar servicios en riesgo de incumplimiento y priorizar acciones de mejora antes de que afecten la operación. |
| **Realista (Realistic)** | Los datos del catálogo y de atención están disponibles o en proceso de consolidación en el Drive del grupo; la clasificación es una técnica aplicable con esas variables. |
| **Temporal (Time-bound)** | El horizonte de predicción es el año **2026**. |

## Indicadores vinculados a la pregunta

| Indicador | Definición | Meta / referencia |
|-----------|------------|-------------------|
| Cumplimiento global de ANS | % de servicios/casos dentro del ANS | ≥ 95% |
| Disponibilidad de servicios TI | % de tiempo operativo | ≥ 99.5% |
| Satisfacción de usuarios | Nivel de satisfacción con el servicio | ≥ 90% |
| Tiempo promedio de resolución | Horas promedio de resolución | ≤ 8 horas |
| Variable objetivo (modelo) | Cumple ANS: 1 = Cumple, 0 = No cumple | Clasificación binaria |

## Criterio de éxito del EDA (Taller 1)

El notebook [`notebooks/taller1_eda_catalogo_ti.ipynb`](../../notebooks/taller1_eda_catalogo_ti.ipynb) debe explorar:

1. Estructura y calidad del catálogo y datos de atención.
2. Distribución de servicios, demanda y cumplimiento ANS.
3. Variables disponibles para alimentar un modelo de clasificación.
4. Conclusiones sobre viabilidad de la predicción para 2026.
