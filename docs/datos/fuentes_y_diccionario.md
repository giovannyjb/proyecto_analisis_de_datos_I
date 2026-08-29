# Fuentes de datos y diccionario

## Enlace principal

[Google Drive — Grupo 3](https://drive.google.com/drive/u/1/folders/1NzXBrdwk3EW74dB6GLmYZ_qp86arPvtH)

## Inventario de archivos

Completar tras descargar los datos en `data/raw/`.

| Archivo | Formato | Descripción | Uso en el análisis |
|---------|---------|-------------|-------------------|
| *Pendiente* | | Catálogo de servicios | Variables del servicio, ANS definidos |
| *Pendiente* | | Datos de atención prestada | Demanda, tiempos, cumplimiento ANS |

## Diccionario — Catálogo de servicios

Columnas identificadas por el equipo:

| Columna | Tipo esperado | Descripción | Uso en el análisis |
|---------|---------------|-------------|-------------------|
| ID Servicio | | Identificador único del servicio | Clave para cruzar con atención |
| Servicio | texto | Nombre del servicio | Identificación y reportes |
| Categoría | texto | Categoría del servicio | Distribución y agrupación |
| Dueño del Servicio | texto | Responsable del servicio | Contexto organizacional |
| Unidad Responsable | texto | Unidad que opera el servicio | Contexto organizacional |
| Horario de atención | texto / hora | Ventana de atención | Característica del servicio |
| Disponibilidad esperada | numérico / % | Disponibilidad definida | KPI y features del modelo |
| ANS Solicitud | texto / tiempo | ANS para solicitudes | Referencia de cumplimiento |
| ANS Incidente | texto / tiempo | ANS para incidentes | Referencia de cumplimiento |
| ANS Incidente Crítico | texto / tiempo | ANS para incidentes críticos | Referencia de cumplimiento |
| Usuarios Objetivo | texto | Perfil de usuarios del servicio | Característica del servicio |

## Variable objetivo (modelo de clasificación)

| Variable | Valores | Descripción |
|----------|---------|-------------|
| Cumple ANS | `1` = Cumple, `0` = No cumple | Variable objetivo para predicción 2026 |

## Relaciones entre archivos

| Archivo A | Columna | Archivo B | Columna | Tipo de relación |
|-----------|---------|-----------|---------|------------------|
| Catálogo | ID Servicio | Atención prestada | ID Servicio (o equivalente) | Uno a muchos |

## Calidad de datos observada

| Aspecto | Hallazgo | Acción |
|---------|----------|--------|
| Valores nulos | *Pendiente* | |
| Duplicados | *Pendiente* | |
| Formato de fechas | *Pendiente* | |
| Consistencia de nombres de servicio | *Pendiente* | |

## Notas

- Actualizar este documento cuando los archivos estén en `data/raw/`.
- Validar nombres exactos de columnas al cargar los archivos del Drive.
