# Pregunta SMART — Taller 1

## Pregunta

> ¿Puede un sistema de analítica predictiva basado en inteligencia artificial anticipar brotes de dengue con una precisión superior al 80 %, permitiendo reducir en al menos 20 % la tasa de mortalidad y en 30 % el tiempo de respuesta sanitaria en los territorios priorizados durante un piloto de 6 meses, utilizando datos epidemiológicos, climáticos y demográficos del Instituto Nacional de Salud y el IDEAM?

## Desglose SMART

| Criterio | Cómo se cumple |
|----------|----------------|
| **Específica (Specific)** | Sistema de analítica predictiva con IA para anticipar brotes de dengue en territorios priorizados, usando datos del INS y el IDEAM. |
| **Medible (Measurable)** | Precisión del modelo > 80 %; reducción de mortalidad ≥ 20 %; reducción del tiempo de respuesta sanitaria ≥ 30 %. |
| **Accionable (Achievable / Actionable)** | Permite generar alertas tempranas, priorizar territorios y orientar la respuesta sanitaria antes del pico del brote. |
| **Realista (Realistic)** | Fuentes oficiales disponibles (INS/SIVIGILA, IDEAM, DANE); técnicas de regresión y ML validadas en literatura sobre dengue. |
| **Temporal (Time-bound)** | Piloto de **6 meses** en territorios priorizados. |

## Indicadores vinculados a la pregunta

| Indicador | Definición | Meta |
|-----------|------------|------|
| Precisión del modelo | % de predicciones correctas de brotes | > 80 % |
| Tasa de mortalidad | Fallecimientos / casos confirmados por territorio | Reducción ≥ 20 % |
| Tiempo de respuesta sanitaria | Horas/días desde alerta hasta intervención | Reducción ≥ 30 % |
| Cobertura de vigilancia | Municipios de alto riesgo monitoreados | Incrementar cobertura |
| Casos y fallecimientos | Número esperado por municipio (regresión) | Estimación para planificación |

## Criterio de éxito del EDA (Taller 1)

El notebook [`notebooks/taller1_eda_dengue.ipynb`](../../notebooks/taller1_eda_dengue.ipynb) debe explorar:

1. Estructura y calidad de datos epidemiológicos, climáticos y demográficos.
2. Distribución de casos y fallecimientos por territorio y periodo.
3. Relación entre variables climáticas y brotes históricos.
4. Variables disponibles para alimentar un modelo de regresión predictivo.
5. Viabilidad del piloto de 6 meses con precisión > 80 %.
