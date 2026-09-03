# Justificación del uso de IA / Ciencia de Datos

> **Visión del proyecto vs alcance Taller 1:** la justificación de largo plazo contempla clima (IDEAM), demografía (DANE) y mortalidad. **En este taller** el EDA usa únicamente `Datos_2025_210.xlsx` (SIVIGILA 2025): casos, hospitalización, territorio y perfil demográfico. No integramos IDEAM/DANE ni analizamos fallecimientos (`FEC_DEF` 100 % nulo).

## Problema que aborda el análisis

El dengue genera sobrecarga hospitalaria. Con SIVIGILA podemos caracterizar **cuándo** y **dónde** se concentran los casos. La ciencia de datos permite, primero, explorar esa carga (EDA) y, después, modelar el número esperado de casos por municipio–semana para anticipar brotes.

## Técnicas aplicadas en este proyecto

| Técnica | Uso ahora (Taller 1) | Uso previsto después | Por qué es pertinente |
|---------|----------------------|----------------------|------------------------|
| **EDA** | Perfilado de casos, hospitalización, temporalidad y territorio en Excel 2025 | — | Valida calidad y relaciones antes del modelo |
| **Analítica predictiva** | Motivación / alcance del proyecto | Anticipar territorios y periodos de mayor riesgo | Responde a la pregunta SMART |
| **Regresión** | No entrenada aún | Estimar casos agregados municipio–semana | Variable continua alineada al problema |
| **Análisis territorial** | Ranking depto/municipio (sin shapefiles) | Mapas de riesgo si hay geometrías | Priorizar vigilancia donde hay más carga |
| **IA generativa** | Asistencia en notebook y documentación (Cursor) | Prototipado continuo | Acelera el taller; el equipo valida resultados |

## Estado del arte — Referencias

1. **Delpino, F. M., et al. (2026).** Global performance of predictive models for dengue severity, hospitalization and mortality: A systematic review and meta-analysis of 146 studies. *International Journal of Infectious Diseases*. https://doi.org/10.1016/j.ijid.2026.07.014  
   Valida modelos predictivos con capacidad para anticipar hospitalización y mortalidad por dengue.

2. **Martin, M. E., et al. (2026).** Assessing environmental and climatic predictors of dengue fever in Santa Marta, Colombia: Implications for One Health surveillance. *Science in One Health*, 5, 100164.  
   Identifica factores ambientales como indicadores predictivos de brotes (visión futura del proyecto).

3. **Kumar, A., et al. (2026).** Automated detection and prediction of dengue fever: A systematic review (2013–2025). *Engineering Applications of Artificial Intelligence*, 136, 106234.  
   Concluye que sistemas basados en ML mejoran la detección temprana y las alertas predictivas.

## Contribución esperada al negocio

- **Ahora (EDA 2025):** evidenciar estacionalidad, concentración territorial y perfiles distintos por departamento (p. ej. Valle).
- **Después:** anticipar brotes con precisión > 80 % en un piloto de 6 meses; reducir mortalidad y tiempo de respuesta cuando haya variables y modelo adecuados.

## Evidencia de uso de IA generativa

Documentado en el notebook (sección 9):

- Herramienta: Cursor.
- Partes asistidas: estructura, limpieza, gráficos, H3, borradores de interpretación.
- Validación del equipo: datos, cifras (confirmados ≈ 75 %), hipótesis H1–H3 y alcance Excel 2025.
