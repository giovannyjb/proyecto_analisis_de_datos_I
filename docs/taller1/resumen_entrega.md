# Resumen para entrega — Taller 1

Documento consolidado para Moodle · **Grupo 3** · Fecha de entrega: **3 de septiembre de 2026**

## Integrantes

| Integrante |
|------------|
| Juan Manuel Román Villa |
| Dora Valencia Martínez |
| Julian Aguilar Mayorga |
| Camilo Percy Ocampo |
| Viviana Fernández Payan |
| Giovanni Jaramillo Bolaños |
| Victor Manuel Hurtado López |

---

## 1. Descripción del problema e impacto

El dengue genera sobrecarga hospitalaria y presión sobre la red de atención en varios departamentos. Nosotros trabajamos con notificaciones SIVIGILA (INS, evento 210) para orientar la vigilancia epidemiológica y la priorización territorial.

- **Procesos afectados:** vigilancia de casos, hospitalización y respuesta sanitaria territorial.
- **KPI medibles en este taller (Excel 2025):** volumen de casos; % confirmados; % hospitalización; concentración territorial (top departamentos/municipios); perfil demográfico Valle vs nacional.
- **KPI de proyecto futuro:** precisión del modelo > 80 %; reducción de mortalidad y de tiempo de respuesta (requieren modelado y, en su caso, otras fuentes). En el Excel 2025, `FEC_DEF` está 100 % nulo: **no medimos mortalidad aquí**.

## 2. Tipo de analítica

**Predictiva** (visión del proyecto) — anticipar territorios y periodos con mayor riesgo de brotes. En Taller 1 entregamos el **EDA** que sustenta esa fase.

## 3. Caso similar (estado del arte)

- Delpino et al. (2026): modelos predictivos para severidad, hospitalización y mortalidad por dengue.
- Martin et al. (2026): factores climáticos como predictores de brotes en Colombia.
- Kumar et al. (2026): ML para detección temprana y alertas predictivas.

## 4. Tipo de problema de IA

**Regresión** — en fases posteriores, estimar el número esperado de casos agregados por municipio–semana a partir de SIVIGILA (y otras fuentes si el equipo las incorpora después).

## 5. Datos necesarios y disponibilidad

**Fuente única usada en este EDA:** `data/raw/Datos_2025_210.xlsx` (~120.5k filas × ~70 variables en crudo; ~118k tras filtrar `FEC_NOT` fuera de 2025; códigos enteros; fechas en texto; nulos estructurales).

Fuentes previstas para el **proyecto** (no analizadas en este taller): IDEAM (clima), DANE (demografía). Drive del equipo: [Google Drive — Grupo 3](https://drive.google.com/drive/u/1/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH).

## 6. Impacto en el negocio con métricas

1. Priorizar departamentos/municipios de alta carga (evidencia EDA: top 10 ≈ 70 % de casos).
2. Anticipar ventanas temporales de pico (evidencia EDA: ene–feb / primeras semanas epidemiológicas).
3. Diferenciar perfiles territoriales (evidencia EDA: Valle vs nacional en edad, sexo y hospitalización).

## 7. Pregunta SMART

> ¿Puede un sistema de analítica predictiva basado en inteligencia artificial anticipar brotes de dengue con una precisión superior al 80 %, permitiendo reducir en al menos 20 % la tasa de mortalidad y en 30 % el tiempo de respuesta sanitaria en los territorios priorizados durante un piloto de 6 meses, utilizando datos epidemiológicos de SIVIGILA (INS)?

| SMART | Cumplimiento |
|-------|--------------|
| Específica | Sistema predictivo con IA, brotes de dengue, fuente INS/SIVIGILA |
| Medible | Visión: precisión > 80 %, mortalidad −20 %, respuesta −30 %. **Taller 1:** casos, % hosp., concentración territorial, perfil Valle |
| Accionable | Alertas tempranas y priorización territorial |
| Realista | En este taller usamos únicamente el Excel SIVIGILA 2025 |
| Temporal | Piloto de 6 meses (visión); EDA acotado a 2025 |

**Qué responde el notebook ahora:** calidad de datos, H1 (estacionalidad), H2 (heterogeneidad territorial), H3 (perfil Valle).  
**Qué queda para modelado:** precisión > 80 %, mortalidad, tiempos de respuesta, clima/demografía externa.

## 8. Justificación IA / Ciencia de Datos

EDA ahora para validar calidad, temporalidad, territorio y perfil demográfico. Después: regresión agregada municipio–semana sobre SIVIGILA. La predicción es pertinente porque la carga no es uniforme en el tiempo ni en el espacio (hallazgos 2025). La IA generativa (Cursor) asistió el prototipo; el equipo validó cifras, hipótesis y alcance.

## 9. Análisis exploratorio de datos (entregable)

- **Herramienta:** Jupyter Notebook — [`notebooks/taller1_eda_dengue.ipynb`](../../notebooks/taller1_eda_dengue.ipynb)
- **Estado:** ejecutado con `data/raw/Datos_2025_210.xlsx` (SIVIGILA 2025).
- **Hallazgos clave:** H1 confirmada (pico ene–feb); H2 confirmada (Bolívar, Santander, Córdoba; top 10 ≈ 70 %); H3 confirmada vs nacional (Valle ≈7.4k casos: edad ↑, sexo equilibrado, hosp. ↓); confirmados ≈ **75 %**.
