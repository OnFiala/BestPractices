---
{
  "id": "data",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Datos, contratos y migraciones

## Elegir el almacenamiento según los invariantes

Define los patrones de acceso, la coherencia, la retención, la residencia y las necesidades de recuperación antes de elegir tecnología. Una base de datos relacional es una candidata sólida para registros transaccionales de negocio; el almacenamiento de objetos suele encajar con grandes objetos binarios. Los índices de búsqueda y las cachés son datos derivados salvo que el sistema los convierta explícitamente en autoritativos. Estos criterios iniciales son recomendaciones de la biblioteca, no mandatos universales.

Da a cada registro una identidad estable y una persona o entidad propietaria. Identifica unicidad, ordenación y transiciones de estado permitidas, incluidas eliminación y restauración. Impón los invariantes críticos mediante restricciones y transacciones admitidas por la base de datos; las comprobaciones de aplicación por sí solas pueden sufrir condiciones de carrera. Comprende el nivel de aislamiento desplegado y, cuando haga falta, reintenta de forma segura toda la transacción afectada en lugar de repetir un fragmento arbitrario.

La identidad del inquilino debe proceder de un contexto de autorización de confianza y acompañar lecturas, escrituras, exportaciones y procesamiento en segundo plano. Comprueba vistas derivadas, analítica, registros y copias de seguridad además de las tablas principales. Las reglas de retención y eliminación deben abarcar esas copias; borrar una fila visible no demuestra que se hayan eliminado todas las copias.

## Ampliar, migrar y retirar

| Etapa | Decisión y evidencia requeridas |
| --- | --- |
| Ampliar | Añadir una representación compatible; documentar valores nulos, predeterminados y comportamiento de clientes antiguos |
| Transición | Definir el escritor autoritativo y cómo leen y escriben las versiones mezcladas sin perder significado |
| Rellenar datos históricos | Usar trabajo acotado y reanudable con puntos de control, tratamiento de conflictos y límites observados de recursos y bloqueos |
| Conciliar | Comparar invariantes de negocio y registros representativos, no solo recuentos de filas |
| Cambiar la ruta activa | Seleccionar el tráfico deliberadamente, observar errores y retrasos y conservar una condición de interrupción |
| Retirar | Eliminar la forma antigua solo después de migrar todos los clientes y procesos en segundo plano admitidos y preparar la recuperación |

La escritura doble sin una estrategia de coherencia puede crear dos verdades contradictorias. Revertir el código no deshace una migración destructiva. Decide si la recuperación será una reversión, una reparación hacia delante o una restauración con conciliación, y ensaya la ruta real con datos sintéticos que tengan características de producción o con datos adecuadamente protegidos.

## Probar concurrencia y compatibilidad

Antes de cambiar un esquema o contrato público, ejecuta [pruebas de integración y contratos](testing-strategy.md) con versiones antiguas y nuevas de la aplicación sobre el esquema transitorio. Incluye actualizaciones concurrentes, solicitudes duplicadas, rellenos históricos interrumpidos, ciclos completos de importación y exportación y trabajos reanudados. Un caso negativo útil hace competir a dos clientes por el mismo recurso restringido y verifica que el invariante se mantenga, no solo que una solicitud devuelva un error.

Usa [pruebas de rendimiento](performance-testing.md) para observar bloqueos, retraso de replicación, conjuntos de conexiones y duración de la migración con un volumen representativo. Que una migración funcione con diez filas no demuestra su comportamiento con el conjunto real. Las [pruebas de seguridad](security-testing.md) deben cubrir identificadores de otros inquilinos, ámbito de las exportaciones y acceso revocado después de actualizar índices y cachés.

Restaura en un entorno aislado, valida el comportamiento visible para el usuario y concilia los efectos externos antes de reanudar el procesamiento. Mide el tiempo de recuperación y la pérdida real de datos frente al RTO/RPO, y registra las versiones de copias de seguridad y artefactos. Una réplica puede replicar un borrado accidental; no sustituye una copia de recuperación probada.

## Revisar el modelo

Versiona un contrato cuando los consumidores necesiten coordinación; nunca cambies silenciosamente unidades, admisión de valores nulos, identificadores o significado. Introduce otra base de datos solo para un requisito medido que justifique los costes de coherencia, copias de seguridad y conocimiento especializado. La partición necesita reglas explícitas de enrutamiento, propiedad y operaciones entre particiones. Los modelos de lectura separados pueden ayudar a una necesidad medida de consultas, pero introducen un contrato de vigencia cuando se actualizan asíncronamente.

## Decisiones relacionadas

[Durabilidad](durability.md) · [Seguridad](security.md) · [Escalado](scaling.md) · [Estrategia de pruebas](testing-strategy.md) · [Pruebas de rendimiento](performance-testing.md)

## Evidencia primaria

[postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [owasp](https://raw.githubusercontent.com/OWASP/ASVS/2b47a9dd16760ee484a6672d197f1f7e25d9c632/README.md) · [azure-cqrs](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cqrs.md) · [azure-data-partitioning](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/best-practices/data-partitioning-strategies-content.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md) · [azure-outbox](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/databases/guide/transactional-out-box-cosmos.md)
