# Resumen para entrega — Taller 1

Documento consolidado para Moodle.

---

## 1. Descripción del problema e impacto

La empresa cuenta con un catálogo de servicios de TI, pero la información puede presentar diferencias en su nivel de detalle, actualización y cumplimiento de los ANS. Esto dificulta identificar cuáles servicios tienen mayor demanda y cuáles presentan incumplimientos.

- **Impacto:** continuidad operativa, disponibilidad de servicios tecnológicos y soporte a procesos estratégicos.
- **KPI:** cumplimiento ANS por servicio, volumen de demanda, disponibilidad, satisfacción y tiempo de resolución.

## 2. Complejidad y disponibilidad de datos

- **Catálogo:** ID Servicio, Servicio, Categoría, Dueño del Servicio, Unidad Responsable, Horario de atención, Disponibilidad esperada, ANS Solicitud, ANS Incidente, ANS Incidente Crítico, Usuarios Objetivo.
- **Atención prestada:** datos de solicitudes/incidentes y cumplimiento (para predicción).
- **Fuente:** [Google Drive — Grupo 3](https://drive.google.com/drive/u/1/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH).
- **Complejidad:** media-alta — múltiples variables y posibles inconsistencias entre catálogo y operación.

## 3. Tipo de analítica y problema de IA

- **Analítica descriptiva:** explorar qué servicios existen, demanda, cumplimiento ANS, resultados y distribución.
- **Problema de IA:** clasificación — variable objetivo Cumple ANS (1 = Cumple, 0 = No cumple).

## 4. Caso similar (estado del arte)

Se utiliza el catálogo de servicios y los ANS para organizar, medir y mejorar la prestación de servicios. En entidades públicas, estos instrumentos permiten identificar demanda, evaluar cumplimiento y apoyar la toma de decisiones.

## 5. Impacto en el negocio con métricas

- Disponibilidad de servicios TI ≥ 99.5%
- Cumplimiento global de ANS ≥ 95%
- Satisfacción de usuarios ≥ 90%
- Tiempo promedio de resolución ≤ 8 horas

## 6. Pregunta SMART

**Pregunta:** ¿Es posible predecir, durante el 2026, si un servicio de TI de la empresa cumplirá o incumplirá su ANS, utilizando los datos actuales en la atención prestada y características del servicio?

| SMART | Cumplimiento |
|-------|--------------|
| Específica | Servicios TI, cumplimiento/incumplimiento ANS, atención prestada y características del servicio |
| Medible | Cumple ANS (1/0); métricas de clasificación y KPIs de ANS |
| Accionable | Anticipar riesgo e priorizar mejoras |
| Realista | Datos del catálogo y atención disponibles o en consolidación |
| Temporal | Horizonte 2026 |

## 7. Justificación IA / Ciencia de Datos

EDA y análisis descriptivo para entender el catálogo; clasificación binaria para predecir cumplimiento ANS. La IA generativa asiste en el prototipo del taller; el equipo valida resultados.

## 8. Análisis exploratorio de datos (entregable)

- **Herramienta:** Jupyter Notebook — `notebooks/taller1_eda_catalogo_ti.ipynb`
- **Estado:** esqueleto con respuestas del taller; EDA pendiente de ejecutar con datos en `data/raw/`.

---

*Completar fecha y nombres del equipo antes de entregar.*
