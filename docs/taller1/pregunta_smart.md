# Pregunta SMART — Taller 1

> **Visión del proyecto vs alcance Taller 1:** la pregunta SMART orienta el proyecto completo (modelo predictivo, metas de precisión/mortalidad/respuesta). **En este taller** solo analizamos `data/raw/Datos_2025_210.xlsx` (SIVIGILA 2025): no medimos precisión del modelo ni mortalidad (`FEC_DEF` 100 % nulo) ni integramos IDEAM/DANE.

## Pregunta

> ¿Puede un sistema de analítica predictiva basado en inteligencia artificial anticipar brotes de dengue con una precisión superior al 80 %, permitiendo reducir en al menos 20 % la tasa de mortalidad y en 30 % el tiempo de respuesta sanitaria en los territorios priorizados durante un piloto de 6 meses, utilizando datos epidemiológicos, climáticos y demográficos del Instituto Nacional de Salud y el IDEAM?

## Desglose SMART

| Criterio | Cómo se cumple |
|----------|----------------|
| **Específica (Specific)** | Sistema de analítica predictiva con IA para anticipar brotes de dengue en territorios priorizados. Fuente usada hoy: INS/SIVIGILA; clima/demografía quedan para fases posteriores. |
| **Medible (Measurable)** | Visión: precisión > 80 %; mortalidad ≥ −20 %; respuesta ≥ −30 %. **Taller 1:** casos, % hospitalización, concentración territorial, perfil Valle vs nacional. |
| **Accionable (Achievable / Actionable)** | Permite generar alertas tempranas, priorizar territorios y orientar la respuesta sanitaria antes del pico del brote. |
| **Realista (Realistic)** | Excel SIVIGILA 2025 disponible y analizado; técnicas de regresión/ML validadas en literatura. IDEAM/DANE son realistas a futuro, no usados en este EDA. |
| **Temporal (Time-bound)** | Piloto de **6 meses** en territorios priorizados (visión); EDA acotado al año **2025**. |

## Indicadores vinculados a la pregunta

| Indicador | Definición | Meta / estado en Taller 1 |
|-----------|------------|---------------------------|
| Precisión del modelo | % de predicciones correctas de brotes | > 80 % — **pendiente de modelado** |
| Tasa de mortalidad | Fallecimientos / casos confirmados | ≥ −20 % — **no medible** con Excel 2025 (`FEC_DEF` nulo) |
| Tiempo de respuesta sanitaria | Horas/días desde alerta hasta intervención | ≥ −30 % — **fuera de alcance** del EDA |
| Casos / hospitalización | Volumen y % hosp. por territorio-periodo | **Medido** en el notebook |
| Concentración territorial | Share de casos en top deptos/municipios | **Medido** (H2) |

## Criterio de éxito del EDA (Taller 1)

El notebook [`notebooks/taller1_eda_dengue.ipynb`](../../notebooks/taller1_eda_dengue.ipynb) debe explorar:

1. Estructura y calidad del Excel SIVIGILA 2025 (~120.5k × ~70 vars).
2. Distribución de casos por territorio y periodo (H1, H2).
3. Perfil demográfico y hospitalización (incl. Valle vs nacional, H3).
4. Variables disponibles para alimentar un modelo de regresión de casos (municipio–semana).
5. Separar con claridad lo demostrable ahora de las metas del piloto de 6 meses.
