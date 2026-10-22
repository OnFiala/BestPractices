---
{
  "id": "durability",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Durabilidad y trabajo distribuido

## Definir qué debe sobrevivir

Distingue la durabilidad de los datos almacenados, la disponibilidad del servicio y el trabajo que puede reanudarse. Una réplica no es una copia de seguridad, y entregar un mensaje con éxito no demuestra que sus efectos de negocio ocurran exactamente una vez. Acuerda para cada capacidad la ventana de pérdida de datos aceptable (RPO), el tiempo de recuperación (RTO) y las reglas de conciliación visibles externamente. El contrato de ejecución y pruebas siguiente es una síntesis original de esta biblioteca; el comportamiento del proveedor debe verificarse para la versión desplegada.

## Dar un modelo de estados a cada efecto

Una operación duradera necesita un identificador estable, un propietario autenticado, datos de entrada validados, un estado actual y un resultado observable. Limita el ámbito de las claves de idempotencia al inquilino y la acción de negocio. Define qué ocurre cuando se reutiliza una clave con datos distintos, cuando una solicitud sigue en ejecución y cuando caducan los registros. Conserva la información de deduplicación al menos durante todo el intervalo en que se admitan reintentos o repeticiones; para trabajo anterior, exige un proceso separado y autorizado de conciliación.

Para una transición local de negocio, guarda su resultado y la restricción de unicidad de forma atómica. Cuando una publicación deba reflejar una transición confirmada, un outbox transaccional puede guardar juntos el cambio de negocio y el evento. Un proceso de retransmisión puede publicar dos veces si pierde la confirmación; por tanto, la deduplicación del consumidor debe formar parte de su propia escritura duradera. Esto no convierte en transaccionales las llamadas externas que no participan en esa transacción.

Clasifica los fallos antes de reintentar. Los errores de validación y las denegaciones de autorización necesitan una respuesta definitiva; los fallos transitorios pueden permitir reintentos acotados. Asigna a una capa la responsabilidad sobre el plazo total y el presupuesto de reintentos, y ten en cuenta los reintentos que haga el SDK por debajo. La espera progresiva y su variación aleatoria reducen la presión de reintentos sincronizados; no justifican repetir un efecto que no sea seguro. Una cancelación después de enviar una solicitud externa puede dejar un resultado desconocido que requiera conciliación.

## Secuencia de fallos de ejemplo

Considera un pedido con un proveedor de pagos y un evento posterior para tramitar su entrega:

| Interrupción | Comportamiento observable requerido |
| --- | --- |
| Antes de confirmar la transacción del pedido y el outbox | Ninguno se hace visible; un reintento puede empezar de forma segura |
| Después de confirmar, antes de publicar el evento | Un proceso de retransmisión encuentra finalmente el evento pendiente; ningún pedido desaparece |
| Después de publicar, antes de confirmar al proceso de retransmisión | La entrega duplicada produce una sola transición prevista en el consumidor |
| Después de completar el pago, antes de recibir la respuesta | Reutiliza la identidad de operación admitida por el proveedor o consulta y concilia su estado; no generes a ciegas un cobro nuevo |
| Durante una actualización del proceso en segundo plano | El trabajo en curso se reanuda bajo un contrato de estado y versión explícitamente compatible, o se deriva a conciliación |

Estas son condiciones de aceptación, no evidencia de que un sistema desplegado las haya superado. En un entorno de preproducción, provoca cada interrupción con un comportamiento controlado del proveedor, repite la solicitud e inspecciona después el estado duradero y los registros del proveedor. Comprueba tanto la recuperación correcta como los estados sin resolver que necesitan intervención humana. Sigue la [estrategia de pruebas](testing-strategy.md) para definir el criterio que determina el resultado correcto y el conjunto de evidencias.

## Operar la repetición y la recuperación

Aísla en cuarentena los mensajes que provocan fallos reiterados, con una persona responsable y un motivo. Limita el volumen de reintentos y repeticiones, y autoriza la repetición por separado de la lectura ordinaria. Quien opere el sistema debe conocer el esquema, el ámbito de ordenación y la ventana de deduplicación aplicables. Una compensación es una nueva acción de negocio; los reembolsos, las notificaciones y la entrega física pueden no ser reversibles.

Restaura en un entorno aislado, concilia los totales de negocio y los efectos externos y, después, reanuda el trabajo deliberadamente. Prueba la recuperación con una cola atrasada y dependencias lentas mediante el [plan de pruebas de rendimiento](performance-testing.md). Un motor de flujos duraderos se justifica cuando reduce una complejidad de coordinación demostrada; una tabla transaccional de trabajos puede bastar para un proceso más sencillo con recuperación manual aceptable. Ninguna alternativa elimina la necesidad de copias de seguridad, responsabilidades o pruebas de compatibilidad.

## Decisiones relacionadas

[Datos y migraciones](data.md) · [Salud y recuperación](operations.md) · [Elección de arquitectura](architecture.md) · [Estrategia de pruebas](testing-strategy.md)

## Evidencia primaria

[postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/e8ee627110a98501103827745aab18aedf312dd0/README.md) · [azure-retry](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/retry-content.md) · [azure-cqrs](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cqrs.md) · [azure-outbox](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/databases/guide/transactional-out-box-cosmos.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md)
