---
{
  "id": "playbook-internal-tool",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Entregar una herramienta interna de operaciones

## Aplicabilidad y restricciones

Utiliza este perfil para una aplicación del personal que revise registros, exporte datos o modifique un sistema de negocio del que depende. Una audiencia pequeña también puede tener permisos de gran impacto. Registra el proveedor de identidad, los aprobadores de negocio, la clasificación de datos, el plazo de revocación, los límites de solicitudes de los sistemas externos y el tiempo máximo aceptable para trabajo sin resolver. Este procedimiento redactado por agentes propone un enfoque local de entrega; no es una política adoptada por la organización.

Empieza con una aplicación y adaptadores de integración explícitos. Utiliza el SSO de la organización para la autenticación y una política de aplicación separada para las acciones y el alcance de los registros. Una hoja de cálculo o un producto existente de flujos de trabajo sigue siendo una alternativa cuando sus permisos, auditoría y comportamiento de exportación satisfacen la necesidad real. Un trabajador se justifica por operaciones que duran más que el plazo de la solicitud o necesitan reintentos duraderos. Separa integraciones solo cuando las mediciones de propagación de fallos, demoras en cola o responsabilidad independiente compensen el coste adicional de despliegue.

## Límites del repositorio y de autoridad

Mantén diferenciados en el código `identity/`, `policy/`, `cases/`, `integrations/`, `exports/` y `audit/`. Define qué sistema es responsable de cada campo; un valor importado de un sistema externo no debe convertirse silenciosamente en una verdad editable de forma independiente. Un registro de operaciones recoge solicitante, acción, alcance de objetos, versión de entrada, identidad de aprobación, identificador estable de operación y estado. Almacena los hechos necesarios para auditoría con controles de acceso y retención, no copias sin restricciones de cargas de datos confidenciales.

La autenticación demuestra identidad, no permiso. Comprueba la acción y el alcance al entrar en la API, crear la exportación, descargarla y ejecutar el trabajador. El trabajo en cola necesita una política de delegación declarada: revalida los derechos actuales del solicitante o utiliza un mandato de servicio autorizado por separado. No conserves accidentalmente la autoridad de un antiguo empleado en los datos de un trabajo. Define el plazo de revocación en sesiones de aplicación, permisos en caché, enlaces de descarga y trabajos en ejecución. Para escrituras relevantes en sistemas externos, vincula cualquier aprobación de negocio necesaria al cambio exacto previsto.

## Secuencia de entrega y traspaso

1. El descubrimiento describe un recorrido de negocio, los campos que constituyen su fuente de verdad, una matriz de autorización y la alternativa manual cuando los sistemas externos no estén disponibles. Un responsable humano de negocio resuelve las aprobaciones ambiguas y la retención.
2. La implementación construye una funcionalidad vertical limitada con inspección de solo lectura, modificación de alcance restringido, estado pendiente duradero y consulta de operaciones. Introduce la exportación solo después de definir su contrato separado de autorización y caducidad.
3. La verificación pone a prueba cambios de acceso durante una sesión y durante trabajo en cola y después simula la pérdida de la respuesta de un sistema externo tras una operación exitosa. El rol de operaciones redacta un procedimiento de conciliación mediante identificadores estables de operación y prepara el despliegue a un grupo identificado del personal.

Entrega un perfil, ADR, matriz de políticas, inventario de contratos con sistemas externos, diagrama de transiciones de estado, especificación de exportación, evidencia con resultados esperados y observados, procedimiento de publicación y recuperación y responsable de soporte. Los agentes pueden desempeñar estos roles secuencialmente; añadir agentes no aporta por sí mismo garantías independientes. Los directorios locales `examples/durable_service` y `examples/agent_workflow` pueden orientar experimentos de persistencia y trabajo sujeto a controles. No proporcionan un proveedor de identidad empresarial ni la aprobación de los responsables de negocio.

## Elegir comprobaciones adversariales y operativas

Prueba de forma unitaria las decisiones de política y las transiciones de estado. Utiliza pruebas de integración para la invalidación de sesiones, los adaptadores externos, la materialización de exportaciones y los trabajos duraderos. Las pruebas de navegador deben cubrir acceso denegado, datos externos no disponibles, una lista de casos vacía y trabajo pendiente que siga visible después de recargar. Un botón deshabilitado nunca es un criterio de verificación de autorización.

Crea un empleado con permisos restringidos y un administrador sobre registros sintéticos. Llama directamente a los endpoints protegidos; solicita una exportación excesiva y manipula sus filtros y el identificador de descarga. Los bytes exportados y los cambios resultantes deben mantenerse dentro del alcance del solicitante. Revoca al empleado mientras existan una sesión, un enlace firmado y una operación en cola; transcurrido el plazo acordado, el acceso protegido debe fallar y los trabajos deben seguir la política de delegación declarada. Observa el estado y los efectos en los sistemas externos, no solo los códigos de respuesta.

Haz que el sistema externo acepte un cambio y descarta su respuesta. El reintento debe reutilizar una identidad de idempotencia admitida o dejar la operación pendiente de conciliación. Un proveedor no disponible no debe aparecer como éxito, y un timeout no debe borrar la incertidumbre. Prueba reintentos limitados, saturación de cola y ritmo de recuperación frente a las cuotas del proveedor; detente antes de alcanzar los límites de recursos acordados. Registra los casos bloqueados y omitidos con el requisito previo que falta.

## Publicar, recuperar y asumir la responsabilidad del servicio

Publica para un grupo definido del personal con un artefacto conocido al que revertir y con las escrituras externas limitadas inicialmente por el plan de despliegue aceptado. Para cambios de esquema, admite versiones mixtas y rellena los datos con puntos de control antes de eliminar campos. Revertir la aplicación no puede deshacer una acción externa. Pausa el envío, inspecciona el registro de operaciones, consulta el estado del proveedor y aplica una corrección aprobada por negocio cuando sea posible revertir. Restaura juntos los registros de auditoría y de aplicación o explica cómo se concilian las lagunas.

Supervisa trabajo pendiente antiguo, operaciones denegadas, demora de revocación, volumen de exportación, limitaciones de solicitudes del proveedor y casos que requieren reparación manual. Asigna responsables de negocio y técnicos separados y un plazo de escalamiento para efectos inciertos. Incluye licencias de integración, tiempo del personal, almacenamiento de auditoría y trabajo de guardia en las estimaciones de costes. Los aspectos pendientes para producción incluyen integración real con SSO, política de sesiones, acceso de emergencia, disponibilidad de aprobadores, retención y simulacros de incidentes. La retirada requiere cerrar casos pendientes, transferir los registros de auditoría necesarios, avisar a los responsables de procesos, revocar el acceso del servicio y verificar que los trabajos programados ya no emitan escrituras.

## Continuar con decisiones relacionadas

[Seguridad](security.md) · [Operaciones](operations.md) · [Estrategia de pruebas](testing-strategy.md) · [Durabilidad](durability.md)

## Evidencia primaria

[owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-session](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Session_Management_Cheat_Sheet.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
