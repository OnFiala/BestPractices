---
{
  "id": "durability",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Durabilidad y trabajo distribuido

## Define qué debe sobrevivir

Distingue persistencia, disponibilidad y reanudación del trabajo. Una réplica no es una copia de seguridad; una cola no demuestra efectos de negocio exactamente una vez. Define pérdida aceptable de datos (RPO) y tiempo de recuperación (RTO) por capacidad. Son decisiones de negocio, no propiedades heredadas del nombre de una herramienta.

## Ejecución fiable

- Usa una clave estable de idempotencia por tenant y acción. Guarda resultado o transición con restricción única; define caducidad y payload diferente con la misma clave.
- Limita tiempos y reintentos. Repite solo errores apropiados con espera exponencial, jitter y plazo total; los errores permanentes siguen otra ruta.
- Guarda estado de negocio y outbox en una transacción. El publicador puede duplicar mensajes; los consumidores deduplican y manejan el orden definido.
- Persiste el progreso de tareas largas. Registra cancelación, compensación y reconciliación manual. Compensar es otra acción de negocio, no una reversión garantizada de efectos externos.
- Aísla mensajes problemáticos; la reproducción debe estar autorizada, observada, limitada y tolerar duplicados. Define compatibilidad y retención de deduplicación.

## Ejemplo de fallo

Se guarda un pedido y el proceso cae antes de publicar. El outbox continúa. Si un pago se completa pero se pierde la respuesta, usa la idempotencia del proveedor y reconcilia su estado antes de reintentar. Una clave local no garantiza un único pago externo.

## Verificar y simplificar

Detén workers antes y después de cada escritura duradera; entrega mensajes duplicados y desordenados. Restaura en un entorno aislado y compara totales. Adopta un motor de workflows cuando reduzca complejidad demostrada; prueba actualizaciones con trabajo en curso. Si se tolera repetir manualmente, puede bastar una tabla transaccional de tareas.

## Decisiones relacionadas

[Datos, contratos y migraciones](data.md) · [Salud, recuperación y costes](operations.md) · [Elegir y conectar arquitecturas](architecture.md)

## Evidencia primaria

[postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml) · [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/main/README.md)
