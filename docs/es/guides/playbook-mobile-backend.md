---
{
  "id": "playbook-mobile-backend",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Entregar un backend para clientes móviles

## Aplicabilidad y contrato de clientes compatibles

Utiliza este perfil para un backend que atienda a clientes instalados que puedan permanecer sin conexión, reintentar escrituras y actualizarse en momentos distintos. Registra las versiones de cliente y API compatibles, el intervalo máximo sin conexión, los datos protegidos permitidos en dispositivos, la actualidad de sincronización, la política de revocación y los objetivos de recuperación. Esta propuesta redactada por agentes trata de la entrega del backend y del protocolo. No afirma que se hayan implementado un cliente nativo, almacenamiento seguro en dispositivos, integración de notificaciones push ni accesibilidad de plataforma.

Empieza con una API modular, datos relacionales canónicos y una vía de sincronización con límites. Una aplicación que funcione solo con conexión es una alternativa más sencilla si la tarea del usuario lo permite. La edición sin conexión añade identidad duradera de operación, gestión de conflictos, semántica de eliminación y coste de soporte. Añade ubicación regional, infraestructura de sincronización especializada o particionado solo después de medir retraso de sincronización, frecuencia de conflictos, contención de escrituras, tamaño de cargas de datos o latencia geográfica. El número de dispositivos instalados por sí solo no es un desencadenante de migración.

## Límites y modelo de datos

Separa `api/`, `policy/`, `domain/`, `sync/`, `contracts/` y `ops/`. El servidor es responsable del estado canónico y de la autorización. Un identificador de dispositivo es un atributo de enrutamiento y auditoría, no una prueba de autoridad del usuario. Valida el acceso en lecturas, descargas de sincronización, subidas y renovación de credenciales. Las notificaciones push deben indicar que puede haber datos permitidos disponibles, en lugar de transportar el contenido sensible de registros.

Para cada modificación sin conexión, define un identificador estable de operación, principal autenticado, identificador de registro, revisión de base y cambio previsto. Almacena los resultados de deduplicación dentro de la transacción que aplica la modificación. Reutilizar un identificador con otro cambio debe producir un conflicto. Utiliza revisiones controladas por el servidor para detectar ediciones desactualizadas; los relojes de los dispositivos no son adecuados como única autoridad para ordenar cambios de negocio.

Elige la política de conflictos por dominio. Una nota editable puede presentar ambas versiones para que una persona las combine. Una reserva de inventario debe rechazar una precondición obsoleta o imponer un invariante transaccional, en lugar de elegir silenciosamente el reloj más reciente. Los marcadores de eliminación o información equivalente sobre eliminaciones deben conservarse más allá del intervalo sin conexión admitido. Si un cursor de sincronización caduca, exige una resincronización completa documentada que no resucite silenciosamente registros eliminados ni pierda la intención local pendiente.

## Entregar en una secuencia segura

1. El descubrimiento describe recorridos de lectura, desconexión, edición y reconexión, clasificación de datos, versiones compatibles y ejemplos de conflictos. Un responsable humano acepta la política de retención sin conexión y actualización.
2. La implementación construye una API versionada y un banco de pruebas de clientes sintéticos antes de una vía completa de sincronización. Añade deduplicación de operaciones, actualizaciones condicionales, paginación y cursores, eliminación y estado observable de sincronización con contratos de error explícitos.
3. La verificación ejecuta consumidores antiguos y nuevos contra esquemas de transición y simula dos dispositivos, interrupción de red, revocación y restauración. El responsable de publicación establece los criterios de despliegue por etapas y retirada del soporte a clientes.

Entrega un perfil, esquema de API y sincronización, matriz de compatibilidad, ADR de conflictos, ejemplos de operaciones, requisitos de datos en dispositivos, plan de migración, resultados observados de contratos y recuperación, periodo de soporte y responsables identificados del backend y los clientes. `examples/durable_service` puede orientar experimentos locales de persistencia. No es un motor de sincronización móvil ni evidencia de comportamiento en dispositivos nativos; la verificación real de clientes y plataformas sigue siendo una entrega separada.

## Comprobar la ausencia de efectos no deseados

Utiliza pruebas unitarias para las reglas de combinación y estado, pruebas de integración para transacciones y autorización y pruebas de contrato para el cliente compatible más antiguo y el candidato. Una etiqueta de versión por sí sola no demuestra compatibilidad. Comprueba campos opcionales, tratamiento de valores desconocidos de enumeraciones, paginación, códigos de error, unidades y comportamiento de registros eliminados. Utiliza un dispositivo real o un emulador de plataforma para el comportamiento de caché nativa, almacenamiento de credenciales, trabajo en segundo plano y notificaciones push una vez que exista un cliente.

Haz que dos dispositivos sintéticos editen la misma revisión sin conexión y después se reconecten en ambos órdenes. El criterio de verificación es el resultado declarado del conflicto con la intención del usuario preservada, no simplemente dos respuestas exitosas. Interrumpe una subida después de confirmar la transacción, repítela e inspecciona los registros canónicos: no debe haber ningún efecto de negocio adicional. Reproduce el identificador de operación con contenido alterado y exige un conflicto. Elimina un registro mientras otro dispositivo está sin conexión; una actualización obsoleta no debe resucitarlo fuera de la regla declarada.

Revoca un dispositivo o sesión antes de renovar credenciales y realizar una sincronización protegida. No debe recuperar acceso mediante una vía de renovación; prueba explícitamente cualquier periodo de gracia documentado para tokens de acceso. Simula la caducidad de un cursor y la restauración a una copia de seguridad anterior del servidor: los clientes deben detectar un historial de sincronización incompatible, conciliar operaciones pendientes y resincronizarse de forma segura. Mide tiempo de recuperación, pérdida real de datos, retraso de sincronización, tasa de conflictos y ancho de banda en condiciones de red deficientes y limitadas. Mantén visible el comportamiento de plataformas que no se haya probado.

## Despliegue, operaciones y retirada

Amplía contratos y esquema antes de desplegar consumidores; admite versiones mixtas de clientes durante todo el periodo publicado. Rellena datos con puntos de control, valida invariantes de sincronización y elimina campos antiguos solo cuando la política de soporte lo permita. Revertir el backend no puede obligar a los clientes instalados a actualizarse ni borrar datos descargados. Restaura en aislamiento, establece una nueva época de sincronización o un marcador de recuperación equivalente cuando sea necesario y concilia operaciones antes de reabrir las escrituras.

Supervisa fallos por versión de cliente y API, la operación pendiente más antigua, la tasa de conflictos, el volumen de resincronización, las denegaciones de renovación y la entrega de notificaciones sin registrar cargas de datos protegidas. Asigna por separado responsables de incidentes del backend y de compatibilidad de clientes. Presupuesta almacenamiento, transferencia, uso del proveedor de notificaciones push, soporte de versiones antiguas y simulacros de recuperación. Los aspectos pendientes para producción incluyen identidad real, almacenamiento en dispositivos, seguridad de red, comportamiento nativo en segundo plano, credenciales de notificaciones push y consentimiento y retención. La retirada proporciona a los clientes una respuesta de fin de soporte que indique cómo actuar, ofrece exportación autorizada, completa el trabajo pendiente cuando sea posible, revoca credenciales y gestiona las copias conservadas sin conexión conforme a la política acordada.

## Continuar con decisiones relacionadas

[Contratos de frontend](frontend.md) · [Datos y migraciones](data.md) · [Seguridad](security.md) · [Estrategia de pruebas](testing-strategy.md)

## Evidencia primaria

[owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-session](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Session_Management_Cheat_Sheet.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [semver](https://raw.githubusercontent.com/semver/semver/f99d5485190a47c0863949e7da810a5553e0ed4d/semver.md)
