---
{
  "id": "playbook-saas",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Entregar un SaaS con aislamiento entre inquilinos

## Aplicabilidad y arquitectura inicial

Utiliza este perfil cuando organizaciones cliente independientes compartan una aplicación y su infraestructura. Recoge el aislamiento entre inquilinos, la semántica de facturación, la residencia de datos, los objetivos de recuperación, la forma de la carga máxima y quién es responsable del soporte al cliente. El punto de partida propuesto es una aplicación modular, una base de datos relacional y un trabajador en segundo plano con límites. Un único despliegue puede seguir imponiendo módulos separados de pertenencia, registros de negocio, facturación y entrega. Esta guía redactada por agentes es una síntesis local pendiente de adopción humana.

Una base de datos en un solo host puede encajar en un prototipo aislado con límites de disponibilidad aceptados. El hosting relacional gestionado es una alternativa cuando la recuperación, las escrituras concurrentes y el soporte operativo lo requieren. Separar las bases de datos por inquilino puede satisfacer restricciones de aislamiento o residencia, pero aumenta el coste de migración y soporte. Mide la latencia de consultas, las esperas por bloqueos, la antigüedad de la cola y los efectos de vecinos ruidosos antes de añadir réplicas, particiones o servicios. Extrae un módulo solo si tiene un contrato independiente, un responsable y una mejora medible; el número de inquilinos no es un umbral arquitectónico.

## Incluir invariantes en el repositorio

Utiliza límites como `domain/`, `api/`, `persistence/`, `billing/`, `workers/`, `contracts/` y `ops/`. El principal autenticado determina la pertenencia autorizada a inquilinos; un selector de inquilino suministrado por el cliente nunca establece autoridad. Cada lectura, modificación, exportación, vista en caché y trabajo en cola lleva un contexto de inquilino verificado. Mantén explícita y auditada la suplantación de usuarios por parte del soporte.

Especifica la identidad de los registros, la unicidad dentro de cada inquilino, las monedas y unidades, las transiciones de estado, la paginación, los errores y la retención. Para un comando reintentado, vincula su clave de idempotencia al inquilino, al tipo de operación y a una huella canónica de la solicitud. Reutilizar la clave con otra entrada debe producir un conflicto. Confirma de forma atómica el cambio de negocio, la respuesta almacenada y la entrada de outbox cuando compartan una base de datos. El proceso de retransmisión puede entregar dos veces; el contrato del consumidor o del proveedor debe evitar efectos de negocio duplicados. Una transacción local no puede hacer atómico un cargo remoto.

## Ordenar agentes y artefactos

1. El rol de descubrimiento redacta una matriz de principal, acción y objeto, invariantes de negocio, límites de carga y casos de incertidumbre de facturación. El responsable humano acepta las decisiones de recuperación y riesgo financiero.
2. El implementador entrega una funcionalidad vertical completa: comando autenticado, transacción limitada al inquilino, estado duradero y una vía de ejecución por trabajador que admite reintentos. Registra en un ADR las alternativas de almacenamiento y separación entre inquilinos y proporciona una migración compatible.
3. El verificador prueba HTTP y persistencia conjuntamente y después pone a prueba los límites entre inquilinos, la concurrencia, las interrupciones y la restauración. El rol de publicación prepara un despliegue limitado y un procedimiento de conciliación; la revisión humana controla la aceptación para producción.

El conjunto de entrega incluye el perfil, el ADR, el esquema de API, la matriz de autorización, el orden de migración, ejemplos de registros de operaciones y outbox, evidencia observada de pruebas, informe de restauración, instrucciones de conciliación con el proveedor, estimación de costes y responsables identificados del servicio y los datos. `examples/durable_service` es una referencia local que se debe inspeccionar y adaptar. Su presencia no demuestra autenticación, facturación con proveedores, alta disponibilidad ni los objetivos de recuperación de este proyecto.

## Probar resultados de negocio, incluidos los prohibidos

Utiliza pruebas unitarias para las reglas monetarias y de estado, pruebas de contrato para los consumidores y pruebas de integración con la base de datos realmente elegida para el aislamiento y la atomicidad. Un resultado con SQLite no demuestra el comportamiento de bloqueos o aislamiento de PostgreSQL. En dos inquilinos sintéticos, sustituye identificadores en lecturas, escrituras, exportaciones y cargas de trabajo de los trabajadores. El criterio de verificación es que no haya datos de respuesta no autorizados ni cambios en el estado de otro inquilino, no simplemente una denegación HTTP.

Envía copias simultáneas de un comando y reutiliza su clave con un importe diferente. Inspecciona registros, respuestas almacenadas y efectos: debe quedar una única operación de negocio prevista, y la reutilización incompatible debe fallar. Provoca caídas antes de confirmar la transacción, después de confirmarla y después del éxito del proveedor pero antes del acuse de recibo. El último caso debe producir un reintento seguro bajo una garantía documentada del proveedor o un estado visible de conciliación, nunca un segundo cargo a ciegas. Restaura una copia de seguridad aislada, compara invariantes de negocio y concilia los registros del proveedor antes de reiniciar las entregas. Conserva los casos fallidos y no ejecutados.

Las pruebas de carga deben reproducir consultas costosas, distribución desigual entre inquilinos, escrituras concurrentes y recuperación del trabajo acumulado con límites. Acuerda objetivos de latencia, errores y cola y límites de interrupción antes de ejecutarlas. Incluye pruebas de navegador para resultados denegados, pendientes y ambiguos, de modo que no se anime a los usuarios a volver a enviar un pago incierto.

## Desplegar y operar a través del límite de datos

Amplía primero el esquema, despliega lectores y escritores compatibles, rellena los datos en lotes reanudables, concilia y solo entonces elimina la representación antigua, una vez transcurrido el periodo de compatibilidad. Interrumpe al alcanzar los umbrales acordados de errores, espera por bloqueos o conciliación. Revertir el código de la aplicación no restaura datos eliminados ni revierte un cargo. Conserva el artefacto anterior, las copias de seguridad, los puntos de control de la migración y un plan de reparación hacia delante o restauración aislada.

Supervisa las denegaciones de autorización, los fallos de transacción, la antigüedad de la cola, los intentos de entrega, las discrepancias de facturación y la actualidad de la capacidad de recuperación con identificadores de correlación que protejan la privacidad. Presupuesta capacidad de base de datos, copias de seguridad, tarifas del proveedor, transferencia y trabajo operativo por resultado útil de negocio. Asigna autoridad durante incidentes para pausar por separado la facturación y los trabajadores. Los aspectos pendientes para producción incluyen el ciclo de vida de las identidades, la gestión de claves, los contratos de pago, la baja de inquilinos, los ensayos de restauración y la cobertura de guardias. Al retirar el servicio, detén nuevas escrituras, resuelve los efectos externos pendientes, exporta los datos autorizados de clientes, respeta las reglas de retención y eliminación y revoca integraciones sin destruir la evidencia financiera obligatoria.

## Continuar con decisiones relacionadas

[Datos y migraciones](data.md) · [Durabilidad](durability.md) · [Pruebas de seguridad](security-testing.md) · [Escalado](scaling.md)

## Evidencia primaria

[owasp-multi-tenant](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [azure-outbox](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/databases/guide/transactional-out-box-cosmos.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md)
