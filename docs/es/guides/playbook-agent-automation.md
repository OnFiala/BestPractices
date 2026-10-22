---
{
  "id": "playbook-agent-automation",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Entregar automatización de agentes con límites

## Aplicabilidad y plano de control mínimo

Utiliza este perfil cuando un modelo proponga o coordine acciones con consecuencias duraderas: modificar registros, preparar publicaciones u operar herramientas externas. Registra los destinos permitidos, el responsable de la tarea, el alcance máximo, los requisitos de aprobación, la política de reintentos y los límites de tiempo, tokens y coste. Es preferible un flujo de trabajo determinista cuando ya se conoce la secuencia de decisiones. Empieza con un trabajador limitado y un registro duradero de ejecuciones; añade razonamiento del modelo solo donde mejore un resultado medido de la tarea. Este procedimiento redactado por agentes es una propuesta de síntesis local.

No empieces con una flota de agentes. Separa trabajadores, colas o identidades cuando las mediciones muestren que algunas prioridades quedan sin servicio, permisos de herramientas incompatibles u obligaciones de fiabilidad con responsables independientes. Delegar añade costes de coordinación, credenciales y presupuesto total. Una subtarea hereda una capacidad y un presupuesto más restringidos, nunca autoridad nueva solo porque otro agente la haya solicitado.

## Repositorio, contratos y estado persistente

Separa `planner/`, `policy/`, `tool_gateway/`, `ledger/`, `reconciliation/` y `evaluation/`. El planificador propone acciones tipadas. El componente de políticas comprueba de forma independiente actor, tarea, herramienta, destino exacto, parámetros y alcance. La pasarela de herramientas es responsable de las credenciales y hace cumplir la decisión final. Las salidas de herramientas y el texto recuperado son observaciones no confiables; no pueden modificar políticas, renovar aprobaciones ni seleccionar un destino no autorizado.

Persiste la identidad de tarea, la huella de la acción, la identidad y caducidad de la aprobación, los intentos, las reservas de presupuesto, las referencias de resultados y las transiciones de estado. Distingue los estados planificado, pendiente de aprobación, autorizado, en ejecución, exitoso, fallido y cancelado, y los efectos inciertos. Para trabajo que requiera aprobación, vincúlala al actor y a la acción exacta; consúmela o resérvala de forma atómica para que trabajadores concurrentes no puedan utilizarla dos veces. Los cambios de parámetros requieren una decisión nueva. Un indicador de aprobación dentro del texto del modelo no es un registro confiable.

Una caída después de un efecto externo pero antes del acuse de recibo genera incertidumbre. Utiliza una clave de idempotencia del proveedor o una consulta al proveedor basada en una identidad estable de operación cuando se admitan. En caso contrario, detente y concilia con un operador autorizado; no reclasifiques la incertidumbre como fallo ni reintentes a ciegas. La durabilidad del registro no hace que una acción externa arbitraria ocurra exactamente una vez.

## Ordenar implementación y revisión

1. El rol de descubrimiento hace un inventario de cada herramienta, efecto de lectura o escritura, destino, autorización necesaria, posibilidad de recuperación y responsable. Una persona resuelve la política sobre acciones irreversibles y los límites explícitos de aprobación.
2. La implementación completa primero una ejecución determinista contra componentes de prueba locales que incluya estado persistido, denegación, cancelación, reinicio y conciliación. Añade el planificador del modelo detrás de esos límites y define su contrato tipado.
3. El verificador ataca los límites de capacidades y aprobaciones, duplica trabajo e interrumpe la ejecución. El rol de publicación prepara identidades con alcance restringido, un interruptor de parada, supervisión y un procedimiento para operadores antes de habilitar cualquier conector real.

Entrega el perfil de tarea, la matriz de capacidades, el ADR de la máquina de estados, los esquemas de herramientas, ejemplos de aprobación de acciones exactas, registros de ejecuciones y efectos, resultados observados de pruebas, modelo de presupuesto, instrucciones de conciliación y un responsable identificado de escalamiento. `examples/agent_workflow` es una referencia local para estudiar este límite. Conectar una herramienta real sigue requiriendo su autenticación, restricciones de destino, política de aprobación y contrato de recuperación de efectos; una ejecución con componentes de prueba no concede nada de ello.

## Pruebas con criterios independientes sobre los efectos

Utiliza pruebas unitarias para políticas y transiciones de estado, pruebas de integración de persistencia para reinicio y concurrencia y pruebas de extremo a extremo contra destinos de herramientas aislados. Mantén un registro de efectos separado controlado por el componente de prueba para que el relato del modelo no pueda establecer el éxito. Duplica la misma tarea entre trabajadores: inspecciona tanto los registros de ejecución como los efectos reales. Un único efecto previsto o un estado explícito sin resolver es aceptable bajo el contrato declarado; los duplicados silenciosos no lo son.

Haz caducar la aprobación, sustituye su actor, modifica un importe o destino y reproduce una aprobación ya consumida. No se debe llamar a la herramienta externa. Proporciona texto recuperado que afirme disponer de permisos de administrador y una respuesta falsificada de herramienta que solicite un destino nuevo. La pasarela debe seguir haciendo cumplir la capacidad original. Revoca el acceso a la herramienta entre planificación y ejecución para comprobar que la política se valida en el límite donde se produce el efecto.

Provoca una caída después de que el componente de prueba registre el éxito pero antes de que el trabajador almacene el acuse de recibo. El reinicio debe conciliar o mantener la acción en espera, no repetirla automáticamente. Agota los presupuestos de ejecución y delegados y cancela una tarea en cola; no se puede programar trabajo adicional, mientras que los efectos en curso deben seguirse hasta su resultado final o incierto. Prueba las colas con una carga limitada acordada y observa la falta de servicio a determinadas tareas, la amplificación por reintentos y el trabajo acumulado para operadores. Conserva los casos fallidos, omitidos y no ejecutados en lugar de considerar aprobada una prueba porque haya terminado una conversación con el modelo.

## Publicar, recuperar y retirar

Introduce los conectores de uno en uno con alcances revisados y objetivos de despliegue limitados. Versiona de forma compatible los esquemas de herramientas y las migraciones del registro para que las ejecuciones existentes sigan siendo interpretables; termina o migra explícitamente las ejecuciones antes de eliminar los manejadores antiguos. Revertir la aplicación no revierte los efectos de herramientas ni renueva aprobaciones. Durante un incidente, detén el envío de trabajo, revoca las capacidades comprometidas, conserva evidencia de auditoría protegida y concilia las operaciones pendientes antes de reanudar trabajo autorizado.

Observa acciones denegadas, aprobaciones obsoletas, antigüedad de efectos inciertos, trabajo acumulado de conciliación, éxito de tareas, correcciones humanas y gasto por resultado aceptado. Presupuesta llamadas al modelo, tarifas de herramientas, reintentos, almacenamiento del registro y tiempo de operadores. Los aspectos pendientes para producción incluyen identidad real, almacenamiento protegido de aprobaciones, aislamiento de credenciales, retención de auditoría, garantías del proveedor y respuesta de guardia. La retirada detiene la recepción de trabajo, resuelve o escala efectos pendientes, exporta la evidencia necesaria, revoca todos los conectores y programaciones y elimina el contexto sensible de ejecuciones conforme a la política de retención acordada.

## Continuar con decisiones relacionadas

[Agentes](agents.md) · [Durabilidad](durability.md) · [Integraciones](integrations.md) · [Pruebas de seguridad](security-testing.md)

## Evidencia primaria

[owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
