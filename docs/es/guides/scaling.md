---
{
  "id": "scaling",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Escalar con mediciones

## Describir el trabajo, no el número de cuentas

Registra la tasa máxima de llegadas, el trabajo concurrente, los tamaños de las solicitudes, la mezcla de lecturas y escrituras, los inquilinos o las claves que concentran carga, el crecimiento de los datos, los trabajos en segundo plano y las cuotas de las dependencias. Define el recorrido del usuario, el objetivo del servicio, el margen de costes y la capacidad de reserva necesaria ante fallos antes de elegir capacidad. Un millón de cuentas mayoritariamente inactivas puede ser más fácil de atender que un pequeño conjunto de trabajos concurrentes costosos.

El orden de crecimiento siguiente es una recomendación de la biblioteca, no una garantía de que todas las cargas deban pasar por cada paso. Conserva las mediciones y las alternativas descartadas en un ADR.

## Cambiar una restricción cada vez

| Restricción observada | Cambio candidato | Demostración y compensación |
| --- | --- | --- |
| Consultas lentas o demasiados viajes de ida y vuelta | Analizar perfiles, añadir índices, acotar resultados y agrupar con cuidado | Comparar planes de consulta, latencia y coste de escritura con datos representativos |
| Lecturas costosas repetidas | Caché con claves explícitas por inquilino y reglas de vigencia | Probar arranque en frío, invalidación y fallos de caché simultáneos; medir la carga sobre el origen |
| El trabajo llega más rápido de lo que termina | Colas y procesos acotados, cuotas y control de admisión | Comprobar antigüedad de la cola, reparto justo y recuperación; rechazar de forma previsible antes del agotamiento |
| CPU de la aplicación o E/S independiente saturadas | Añadir réplicas sin estado | Recalcular el total de conexiones a la base de datos y la tasa de solicitudes a dependencias |
| Predomina el tráfico de lectura | Réplica o proyección de consultas | Definir retraso y comportamiento de lectura tras escritura; probar lecturas desactualizadas y no disponibles |
| Persiste un límite medido de almacenamiento, escritura o enrutamiento | Particionar o aislar una carga de trabajo | Demostrar enrutamiento, comportamiento de claves muy solicitadas, redistribución, migración y semántica entre particiones |

No supongas que una caché hace segura la autorización: delimita el ámbito de sus claves e invalida los permisos cuando corresponda. Una avalancha de fallos de caché puede sobrecargar el origen. Añadir réplicas de aplicación puede empeorar una caída de la base de datos si cada réplica abre un gran conjunto de conexiones o reintenta el mismo trabajo.

## Especificar el experimento antes de generar tráfico

Usa la [guía de pruebas de rendimiento](performance-testing.md) para distinguir los experimentos de carga de referencia, picos, estrés, duración prolongada y recuperación. Define el entorno objetivo, la autorización, el conjunto de datos sintéticos, la distribución del tráfico, las condiciones de parada y el límite de coste. Prueba operaciones denegadas y costosas además del recorrido habitual. Conserva los resultados de cada solicitud, las métricas de recursos, la antigüedad de la cola y una descripción versionada de la carga.

Mide por separado el rendimiento de operaciones completadas correctamente, la latencia p95/p99, los errores y el trabajo rechazado. Un sistema que solo muestra una latencia excelente porque descarta casi todas las solicitudes no ha cumplido su objetivo. Incluye una dependencia lenta y observa si consume toda la concurrencia o multiplica los reintentos. Después de reducir el tráfico, confirma que las colas se vacían y se recuperan los objetivos del servicio sin reiniciar manualmente.

Como comprobación aproximada en un sistema estable, el promedio de trabajo en curso equivale a la tasa media de llegadas multiplicada por el tiempo medio dentro del mismo límite medido. No es una estimación de latencia de los percentiles altos ni una promesa de capacidad; una cola sobrecargada que sigue creciendo rompe el supuesto de estado estable. Valida cualquier estimación con la distribución real y el modo de fallo.

## Decidir y revertir

Escala cuando las mediciones sostenidas o una previsión justificada amenacen el objetivo acordado o la capacidad de reserva ante fallos. Registra la condición de activación, la mejora prevista, el coste operativo, la persona responsable del cambio y el plan de reversión o reparación hacia delante. El escalado automático necesita máximos acotados, tiempo de arranque, capacidad de las dependencias y controles de presupuesto. No puede corregir una transacción ineficiente ni garantizar disponibilidad.

Las escrituras multirregión y la fragmentación añaden decisiones de enrutamiento y coherencia. Introdúcelas solo después de probar la conmutación ante fallos, los conflictos o la conciliación y la migración con datos representativos. La fuente sobre partición específica de un proveedor ilustra esas obligaciones; los límites de su producto no son límites universales para otra base de datos.

## Decisiones relacionadas

[Pruebas de rendimiento](performance-testing.md) · [Alojamiento](hosting.md) · [Datos](data.md) · [Operación](operations.md) · [Arquitectura](architecture.md)

## Evidencia primaria

[observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [azure-cache-aside](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cache-aside-content.md) · [azure-data-partitioning](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/best-practices/data-partitioning-strategies-content.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml)
