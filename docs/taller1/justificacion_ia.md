# Justificación del uso de IA / Ciencia de Datos

## Problema que aborda el análisis

El dengue genera sobrecarga hospitalaria y mortalidad evitable. Integrar manualmente datos epidemiológicos, climáticos y demográficos de múltiples fuentes (INS, IDEAM, DANE) es lento y no permite anticipar brotes. La ciencia de datos e IA permiten modelar riesgo territorial, generar alertas tempranas y orientar la respuesta sanitaria.

## Técnicas aplicadas en este proyecto

| Técnica | Uso en este proyecto | Por qué es pertinente |
|---------|----------------------|----------------------|
| **Análisis exploratorio de datos (EDA)** | Perfilado de casos, fallecimientos, variables climáticas y demográficas | Primera fase para validar calidad y relaciones antes del modelo |
| **Analítica predictiva** | Anticipar territorios y periodos con mayor riesgo de brotes y fallecimientos | Responde directamente a la pregunta SMART |
| **Regresión** | Estimar número esperado de casos y fallecimientos por municipio | Variable continua (conteo de casos/muertes); alineada con el tipo de problema definido |
| **Análisis espacial** | Mapas de riesgo con coordenadas geográficas | Identificar territorios prioritarios para el piloto |
| **IA generativa** | Asistencia en notebook, integración de datos y documentación | Acelera el prototipo del taller; el equipo valida resultados |

## Estado del arte — Referencias

1. **Delpino, F. M., et al. (2026).** Global performance of predictive models for dengue severity, hospitalization and mortality: A systematic review and meta-analysis of 146 studies. *International Journal of Infectious Diseases*. https://doi.org/10.1016/j.ijid.2026.07.014  
   Valida modelos predictivos (regresión logística, redes neuronales, árboles de decisión) con capacidad para anticipar hospitalización y mortalidad por dengue.

2. **Martin, M. E., et al. (2026).** Assessing environmental and climatic predictors of dengue fever in Santa Marta, Colombia: Implications for One Health surveillance. *Science in One Health*, 5, 100164.  
   Identifica factores ambientales (temperatura, humedad y lluvias) como indicadores predictivos de brotes.

3. **Kumar, A., et al. (2026).** Automated detection and prediction of dengue fever: A systematic review (2013–2025). *Engineering Applications of Artificial Intelligence*, 136, 106234.  
   Concluye que los sistemas automatizados basados en machine learning mejoran la detección temprana y permiten alertas predictivas más precisas.

## Contribución esperada al negocio

- Anticipar brotes con precisión > 80 % en el piloto de 6 meses.
- Reducir mortalidad ≥ 20 % en territorios priorizados.
- Reducir tiempo de respuesta sanitaria ≥ 30 %.
- Incrementar cobertura de vigilancia en municipios de alto riesgo.
- Integrar datos epidemiológicos y climáticos para decisiones basadas en evidencia.

## Evidencia de uso de IA generativa

Documentar en el notebook (sección final):

- Herramienta usada (ej. Cursor, ChatGPT, Copilot).
- Qué partes del código o análisis fueron asistidas por IA.
- Qué validaciones realizó el equipo (datos, lógica, conclusiones).
