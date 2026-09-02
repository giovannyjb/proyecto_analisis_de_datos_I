# Resumen para entrega — Taller 1

Documento consolidado para Moodle.

---

## 1. Descripción del problema e impacto

El aumento recurrente de casos de dengue en el territorio nacional genera sobrecarga hospitalaria e incremento en la mortalidad, constituyendo una amenaza para la salud pública. Se requiere validar la tasa de mortalidad frente a la incidencia del vector y determinar territorios con mayores fallecimientos para orientar políticas de prevención y respuesta sanitaria.

- **Métricas clave:** tasa de mortalidad, incidencia de casos, fallecimientos por territorio.

## 2. Tipo de analítica

**Predictiva** — anticipar territorios y periodos con mayor riesgo de brotes y fallecimientos usando variables epidemiológicas, climáticas y demográficas. Genera alertas tempranas para la toma de decisiones en salud pública.

## 3. Caso similar (estado del arte)

- Delpino et al. (2026): modelos predictivos para severidad, hospitalización y mortalidad por dengue.
- Martin et al. (2026): factores climáticos (temperatura, humedad, lluvias) como predictores de brotes en Colombia.
- Kumar et al. (2026): ML para detección temprana y alertas predictivas.

## 4. Tipo de problema de IA

**Regresión** — estimar el número esperado de casos y fallecimientos en los municipios del país.

## 5. Datos necesarios y disponibilidad

- Casos y fallecimientos (INS, SIVIGILA)
- Variables meteorológicas: temperatura, lluvia, humedad (IDEAM)
- Datos demográficos y densidad poblacional (DANE)
- Saneamiento y criaderos (Secretarías de Salud)
- Coordenadas geográficas para análisis espacial

**Fuente del equipo:** [Google Drive — Grupo 3](https://drive.google.com/drive/u/1/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH)

## 6. Impacto en el negocio con métricas

1. Reducir tasa de mortalidad por el vector en territorios de mayor incidencia.
2. Disminuir tiempo de respuesta sanitaria ante brotes mediante integración de datos epidemiológicos y climáticos.
3. Incrementar cobertura de vigilancia en municipios de alto riesgo.

## 7. Pregunta SMART

**Pregunta:** ¿Puede un sistema de analítica predictiva basado en inteligencia artificial anticipar brotes de dengue con una precisión superior al 80 %, permitiendo reducir en al menos 20 % la tasa de mortalidad y en 30 % el tiempo de respuesta sanitaria en los territorios priorizados durante un piloto de 6 meses, utilizando datos epidemiológicos, climáticos y demográficos del Instituto Nacional de Salud y el IDEAM?

| SMART | Cumplimiento |
|-------|--------------|
| Específica | Sistema predictivo con IA, brotes de dengue, datos INS e IDEAM |
| Medible | Precisión > 80 %, mortalidad −20 %, respuesta −30 % |
| Accionable | Alertas tempranas y priorización territorial |
| Realista | Fuentes oficiales y técnicas validadas en literatura |
| Temporal | Piloto de 6 meses |

## 8. Justificación IA / Ciencia de Datos

EDA para explorar datos; regresión y analítica predictiva para estimar casos/fallecimientos y anticipar brotes. La IA generativa asiste en el prototipo; el equipo valida resultados.

## 9. Análisis exploratorio de datos (entregable)

- **Herramienta:** Jupyter Notebook — `notebooks/taller1_eda_dengue.ipynb`
- **Estado:** respuestas documentadas; EDA pendiente de ejecutar con datos en `data/raw/`.

---

*Completar fecha y nombres del equipo antes de entregar.*
