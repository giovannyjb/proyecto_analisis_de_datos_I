# Definición del problema — Taller 1

## Tabla de análisis del problema

| Campo | Contenido |
|-------|-----------|
| **Descripción del problema e impacto en la organización (incluyendo métrica)** | La empresa cuenta con un catálogo de servicios de TI, pero la información puede presentar diferencias en su nivel de detalle, actualización y cumplimiento de los ANS. Esto dificulta identificar cuáles servicios tienen mayor demanda y cuáles presentan incumplimientos. **Áreas afectadas:** gestión de servicios TI, mesa de ayuda, planificación de capacidad y cumplimiento de SLAs. **KPI propuesto:** porcentaje de cumplimiento ANS por servicio y volumen de demanda (solicitudes/tickets por servicio). |
| **Tipo de analítica** | **Descriptiva** — se analizan los datos actuales del catálogo para conocer: qué servicios existen, cuáles tienen mayor demanda, cuáles cumplen o incumplen los ANS, qué servicios presentan mejores o peores resultados y cómo están distribuidos los servicios. |
| **Caso similar (estado del arte)** | La gestión de servicios de TI utiliza catálogos de servicio bajo marcos como **ITIL** (Service Catalog Management). Herramientas ITSM (ServiceNow, BMC Helix, Jira Service Management) centralizan catálogos y métricas de SLA. **TODO:** agregar 1–2 referencias o casos documentados (artículo, benchmark o caso de estudio). |
| **Tipo de problema de IA** | **Fase actual (Taller 1):** análisis exploratorio / descriptivo — no requiere modelo de ML. **Fase futura posible:** clasificación (cumple / no cumple ANS), regresión (tiempo de resolución) o clustering (agrupar servicios por perfil de demanda y cumplimiento). |
| **Datos necesarios y disponibilidad** | Catálogo de servicios (nombre, categoría, descripción, ANS definidos), registro de solicitudes/tickets por servicio, métricas de cumplimiento ANS/SLA, fechas de actualización del catálogo. **Fuente:** [Google Drive — Grupo 3](https://drive.google.com/drive/u/1/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH). **TODO:** completar tras descargar archivos (ver [`docs/datos/fuentes_y_diccionario.md`](../../datos/fuentes_y_diccionario.md)). |
| **Impacto en el negocio con métricas** | Mejor visibilidad del catálogo permite priorizar servicios de alta demanda, reducir incumplimientos ANS y optimizar recursos de TI. **Impacto esperado:** reducción del % de incumplimiento ANS en servicios críticos, mejor planificación de capacidad. **TODO:** cuantificar objetivo (ej. reducir incumplimiento del X% al Y% en N meses). |
| **Pregunta SMART** | Ver documento dedicado: [`pregunta_smart.md`](pregunta_smart.md). |

## Complejidad del problema

| Aspecto | Descripción |
|---------|-------------|
| Variables involucradas | Servicio, categoría, volumen de solicitudes, tiempo de respuesta/resolución, cumplimiento ANS, fecha de registro, estado del ticket |
| Procesos involucrados | Gestión del catálogo, atención de solicitudes, monitoreo de SLAs, reportes de cumplimiento |
| Dificultad técnica | Media — requiere integrar catálogo con datos operativos; posibles inconsistencias en nombres, formatos y actualización |

## Notas del equipo

- Completar referencias de estado del arte.
- Actualizar diccionario de datos cuando los archivos estén en `data/raw/`.
- Ajustar KPIs con números objetivo acordados con el contexto organizacional.
