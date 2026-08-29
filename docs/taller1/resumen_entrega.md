# Resumen para entrega — Taller 1

Documento consolidado para Moodle. Actualizar antes de entregar.

---

## 1. Descripción del problema e impacto

La empresa cuenta con un catálogo de servicios de TI, pero la información puede presentar diferencias en su nivel de detalle, actualización y cumplimiento de los ANS. Esto dificulta identificar cuáles servicios tienen mayor demanda y cuáles presentan incumplimientos.

- **Áreas/procesos afectados:** gestión de servicios TI, mesa de ayuda, cumplimiento de SLAs, planificación de capacidad.
- **KPI:** porcentaje de cumplimiento ANS por servicio y volumen de demanda (solicitudes/tickets por servicio).

## 2. Complejidad y disponibilidad de datos

- **Datos necesarios:** catálogo de servicios, registro de solicitudes/tickets, métricas ANS/SLA, fechas de actualización.
- **Fuente:** [Google Drive — Grupo 3](https://drive.google.com/drive/u/1/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH).
- **Complejidad:** media — múltiples variables (servicio, categoría, volumen, cumplimiento, fechas); posibles inconsistencias entre fuentes.

## 3. Justificación del uso de IA / Ciencia de Datos

Se aplicará **análisis exploratorio y descriptivo** (pandas, visualización) para perfilar el catálogo, rankear demanda y medir cumplimiento ANS. La IA generativa asiste en la construcción del notebook y la limpieza inicial; el equipo valida resultados. Técnicas futuras posibles: clasificación de cumplimiento ANS o regresión de tiempos de resolución.

## 4. Pregunta SMART

**Pregunta:** ¿Cuáles son los 10 servicios del catálogo de TI con mayor volumen de solicitudes y qué porcentaje de cumplimiento ANS presentan en el último trimestre disponible en los datos?

| SMART | Cumplimiento |
|-------|--------------|
| Específica | Servicios del catálogo TI, demanda y cumplimiento ANS |
| Medible | Conteo de solicitudes y % cumplimiento ANS |
| Accionable | Priorización de servicios críticos para mejora |
| Realista | Datos en Drive del grupo; EDA con herramientas estándar |
| Temporal | Último trimestre disponible en los datos |

## 5. Análisis exploratorio de datos (entregable)

- **Herramienta:** Jupyter Notebook — `notebooks/taller1_eda_catalogo_ti.ipynb`
- **Evidencia:** ejecutar el notebook con datos en `data/raw/` y adjuntar capturas o enlace al repositorio.

---

*Última actualización: completar fecha y nombres del equipo antes de entregar.*
