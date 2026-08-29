# Pregunta SMART — Taller 1

## Pregunta propuesta (orientativa)

> ¿Cuáles son los 10 servicios del catálogo de TI con mayor volumen de solicitudes y qué porcentaje de cumplimiento ANS presentan en el último trimestre disponible en los datos?

**TODO:** Ajustar la pregunta cuando conozcan las columnas y el periodo real de los datos en `data/raw/`.

## Desglose SMART

| Criterio | Cómo se cumple |
|----------|----------------|
| **Específica (Specific)** | Se enfoca en servicios del catálogo TI, medidos por volumen de solicitudes y cumplimiento ANS. |
| **Medible (Measurable)** | Volumen = conteo de solicitudes/tickets; cumplimiento = % de casos dentro del ANS definido. |
| **Accionable (Achievable / Actionable)** | Los resultados permiten priorizar servicios críticos (alta demanda + bajo cumplimiento) y definir acciones de mejora. |
| **Realista (Realistic)** | Los datos están disponibles en el Drive del grupo; el análisis descriptivo es factible con pandas y visualización. |
| **Temporal (Time-bound)** | El análisis cubre el último trimestre disponible en los datos (ajustar fecha concreta al cargar archivos). |

## Indicadores vinculados a la pregunta

| Indicador | Definición | Fuente esperada |
|-----------|------------|-----------------|
| Volumen de demanda | Número de solicitudes/tickets por servicio | Registro de tickets |
| % cumplimiento ANS | (Casos dentro del ANS / total casos) × 100 por servicio | Métricas SLA/ANS |
| Ranking top 10 | Servicios ordenados por volumen de demanda | Derivado del análisis |

## Criterio de éxito del EDA

El notebook [`notebooks/taller1_eda_catalogo_ti.ipynb`](../../notebooks/taller1_eda_catalogo_ti.ipynb) debe mostrar:

1. Lista o gráfico del top 10 servicios por demanda.
2. % de cumplimiento ANS asociado a esos servicios.
3. Conclusiones que respondan directamente la pregunta SMART.
