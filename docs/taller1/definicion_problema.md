# Definición del problema — Taller 1

## Tabla de análisis del problema

| Campo | Contenido |
|-------|-----------|
| **Descripción del problema e impacto en la organización (incluyendo métrica)** | La empresa cuenta con un catálogo de servicios de TI, pero la información puede presentar diferencias en su nivel de detalle, actualización y cumplimiento de los ANS. Esto dificulta identificar cuáles servicios tienen mayor demanda y cuáles presentan incumplimientos. **Áreas afectadas:** gestión de servicios TI, continuidad operativa y soporte a procesos estratégicos. **KPI relacionados:** cumplimiento ANS por servicio, volumen de demanda y métricas globales de disponibilidad y resolución. |
| **Tipo de analítica** | **Descriptiva** — se analizarán los datos actuales del catálogo para saber: qué servicios existen, cuáles tienen mayor demanda, cuáles cumplen o incumplen los ANS, qué servicios presentan mejores o peores resultados y cómo están distribuidos los servicios. La pregunta SMART orienta además un enfoque **predictivo** (clasificación) para 2026. |
| **Caso similar (estado del arte)** | Actualmente se utiliza el catálogo de servicios y los acuerdos de nivel de servicio (ANS) para organizar, medir y mejorar la prestación de servicios. En entidades públicas, estos instrumentos permiten identificar la demanda, evaluar el cumplimiento de los ANS y apoyar la toma de decisiones. |
| **Tipo de problema de IA** | **Clasificación** — variable objetivo: **Cumple ANS** (Sí/No). `1` = Cumple, `0` = No cumple. |
| **Datos necesarios y disponibilidad** | **Catálogo de servicios:** ID Servicio, Servicio, Categoría, Dueño del Servicio, Unidad Responsable, Horario de atención, Disponibilidad esperada, ANS Solicitud, ANS Incidente, ANS Incidente Crítico, Usuarios Objetivo. **Adicional para la pregunta SMART:** datos de la atención prestada (solicitudes/incidentes, tiempos, cumplimiento histórico). **Fuente:** [Google Drive — Grupo 3](https://drive.google.com/drive/u/1/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH). Ver [`docs/datos/fuentes_y_diccionario.md`](../../datos/fuentes_y_diccionario.md). |
| **Impacto en el negocio con métricas** | **Impacto:** garantizar la continuidad operativa, la disponibilidad de los servicios tecnológicos y el soporte a los procesos estratégicos de la empresa. **Métricas objetivo:** Disponibilidad de servicios TI ≥ 99.5%; Cumplimiento global de ANS ≥ 95%; Satisfacción de usuarios ≥ 90%; Tiempo promedio de resolución ≤ 8 horas. |
| **Pregunta SMART** | Ver documento dedicado: [`pregunta_smart.md`](pregunta_smart.md). |

## Complejidad del problema

| Aspecto | Descripción |
|---------|-------------|
| Variables involucradas | ID y nombre de servicio, categoría, dueño, unidad responsable, horarios, disponibilidad, ANS (solicitud, incidente, crítico), usuarios objetivo, datos de atención prestada, cumplimiento ANS |
| Procesos involucrados | Gestión del catálogo, atención de solicitudes e incidentes, monitoreo de ANS, reportes de cumplimiento y toma de decisiones |
| Dificultad técnica | Media-alta — integrar catálogo con datos operativos de atención; posibles inconsistencias en detalle, actualización y formatos; preparación de variable objetivo para clasificación |

## Notas del equipo

- Actualizar diccionario de datos cuando los archivos estén en `data/raw/`.
- El EDA (Taller 1) explora los datos antes de construir el modelo de clasificación.
