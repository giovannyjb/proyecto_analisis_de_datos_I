# Definición del problema — Taller 1

> Contenido canónico para entrega: está **incrustado** en `notebooks/taller1_eda_dengue.ipynb` (sección 1). Este archivo es copia de respaldo en el repo.

## Tabla de análisis del problema

| Campo | Contenido |
|-------|-----------|
| **Descripción del problema e impacto (con métrica)** | El aumento recurrente de casos de dengue genera sobrecarga hospitalaria y presión sobre la red de atención territorial. KPI del taller (Excel 2025): volumen de casos; % confirmados; % hospitalización; concentración territorial; perfil Valle vs nacional. No medimos mortalidad (`FEC_DEF` 100 % nulo). |
| **Tipo de analítica** | Predictiva (visión del proyecto). En Taller 1 entregamos el EDA. |
| **Caso similar (estado del arte)** | Delpino et al. (2026); Martin et al. (2026); Kumar et al. (2026). |
| **Tipo de problema de IA** | Regresión de casos agregados municipio–semana (fases posteriores). |
| **Datos usados en este taller** | Única fuente: `Datos_2025_210.xlsx` (SIVIGILA 2025). |
| **Impacto en el negocio con métricas** | Priorizar territorios de alta carga; anticipar picos temporales; diferenciar perfiles territoriales. |
| **Pregunta SMART** | Ver sección 1.3 del notebook. |

## Complejidad del problema

| Aspecto | Descripción |
|---------|-------------|
| Variables involucradas | ~70 columnas SIVIGILA (tiempo, territorio, demografía, clínica) |
| Procesos involucrados | Vigilancia epidemiológica, hospitalización, priorización territorial |
| Dificultad técnica | Media–alta (fechas texto, códigos, UNI_MED, nulos estructurales) |

## Notas del equipo

- El entregable principal es el notebook; no se requieren los `.md` para calificar.
- El EDA (Taller 1) explora los datos antes de construir el modelo de regresión.
