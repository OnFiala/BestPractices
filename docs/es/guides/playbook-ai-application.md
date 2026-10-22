---
{
  "id": "playbook-ai-application",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Entregar una aplicación de IA

## Aplicabilidad y resultado acotado

Utiliza este perfil para una aplicación autenticada que recupere información o produzca una respuesta con un modelo. Define la tarea del usuario, los errores aceptables, las divulgaciones prohibidas, el plazo de latencia, el techo de coste, la residencia de datos y una alternativa convencional sin modelo. Empieza con una única cadena de procesamiento de solicitudes con límites, un adaptador alrededor del proveedor y un conjunto de datos de evaluación. Esta propuesta redactada por agentes combina criterio de ingeniería local con la evidencia citada; no es una prueba de fiabilidad del modelo.

La búsqueda o las reglas deterministas son alternativas cuando resuelven la tarea de forma más predecible. La recuperación puede respaldar respuestas fundamentadas en datos del proyecto; el ajuste fino no sustituye la política de acceso a documentos ni su actualidad. Añade modelos, proveedores, cachés o etapas asíncronas solo cuando las restricciones medidas de calidad, demora, rendimiento o residencia justifiquen su coste de evaluación y operación. Una población de usuarios mayor por sí sola no justifica un bucle de agente.

## Separar autoridad, datos y comportamiento del modelo

Organiza `api/`, `policy/`, `retrieval/`, `model_adapter/`, `evaluation/` y `telemetry/`. El servidor autentica al solicitante y filtra los documentos candidatos según el acceso vigente antes de que el contenido llegue al modelo. Incluye inquilino, versión de política, versión de documento y estado de eliminación en el diseño de caché y recuperación. Una caché global de respuestas cuya clave sea solo la consulta puede filtrar el contexto de otro usuario. Define cómo llegan la revocación y la eliminación a índices, prompts almacenados, respuestas generadas y datos conservados por el proveedor conforme al contrato elegido.

El modelo devuelve contenido no confiable. Valida la salida estructurada, representa el texto de forma segura y mantén la ejecución de herramientas detrás de una autorización independiente. Las instrucciones recuperadas, las citas y la confianza del modelo nunca conceden permisos. Define contratos de respuesta para respuesta fundamentada, evidencia insuficiente, proveedor no disponible, presupuesto agotado y cancelación. Una cita debe identificar una fuente recuperada que respalde realmente la afirmación asociada; una URL de apariencia plausible no aporta fundamento. Mantén las credenciales sin procesar fuera de los prompts y establece una política explícita de privacidad y retención para los registros.

## Ordenar el trabajo y su evidencia

1. El descubrimiento especifica tareas representativas, gravedad de fallos, tratamiento lícito de datos y una rúbrica de puntuación antes de elegir el modelo. El responsable humano acuerda las tasas de error aceptables y resuelve los casos ambiguos.
2. La implementación construye una cadena de procesamiento con recuperación autorizada, contexto limitado, plazo para el proveedor, validación de salida y alternativa. Versiona conjuntamente la configuración del modelo, el prompt, la configuración de recuperación e índices y los esquemas de herramientas.
3. La verificación ejecuta un conjunto de evaluación reservado, protegido desde el punto de vista de la privacidad, y casos adversariales, y después inspecciona las trazas de autorización y coste. La preparación de la publicación compara el candidato con una referencia fija y documenta la revisión humana y los fallos pendientes.

El conjunto de traspaso incluye perfil, ADR de flujo de datos, decisión sobre proveedor y tratamiento de datos, matriz de acceso, identidad del conjunto de evaluación, puntuaciones por caso y decisiones humanas, manifiesto de versiones, distribución de latencia y coste, evidencia de la alternativa y responsable de incidentes. `examples/frontend` y `examples/agent_workflow` ofrecen referencias locales de interacción y límites de control que se pueden inspeccionar. Ninguna demuestra calidad semántica de las respuestas, cumplimiento del proveedor ni seguridad de un servicio de recuperación en producción.

## Utilizar criterios de verificación externos al modelo

Elige pruebas unitarias para el esquema y la contabilidad del presupuesto, pruebas de integración para el filtrado de acceso y los fallos del proveedor y evaluaciones para utilidad y fundamentación. Mantén los ejemplos de entrenamiento y ajuste separados de los casos reservados de aceptación. Puntúa por separado la corrección de respuestas, las afirmaciones sin respaldo, la abstención adecuada y las omisiones perjudiciales; un promedio puede ocultar una divulgación grave. Siguen siendo necesarias rúbricas revisadas por personas cuando los resultados son subjetivos. La puntuación mediante modelos ayuda a medir, pero no tiene autoridad independiente de aceptación.

Introduce un marcador sintético único en un documento cuyo acceso esté denegado. Consulta sobre él de forma directa, indirecta y a través de un documento permitido que contenga instrucciones hostiles. El marcador debe estar ausente del contexto recuperado, de las solicitudes al proveedor, de las respuestas devueltas y de los registros expuestos. Tras una revocación o eliminación, repite con cachés e índices ya cargados. Intenta obtener salidas que incumplan el esquema y citas con apariencia de script: no deben ejecutarse ni ampliar el acceso. Son criterios negativos de verificación, no comprobaciones de que el modelo se niegue cortésmente.

Fuerza timeouts del proveedor, desconecta el navegador y agota un presupuesto de solicitud aplicado efectivamente. La aplicación debe dejar de programar más llamadas, mantener un estado claro para el usuario y registrar el trabajo ya incurrido; la cancelación no garantiza que el proveedor haya dejado de facturar. Compara ejecuciones repetidas para observar variaciones de calidad y mide la latencia de los percentiles altos y el coste por tarea aceptada bajo una carga limitada. Registra los tamaños reales de las muestras, los casos fallidos y los idiomas o dominios no probados.

## Publicación y operación a largo plazo

Despliega para un grupo acordado con un interruptor de desactivación y observa los umbrales de calidad, abstención, errores, latencia y gasto. Cambiar el modelo, el prompt, la recuperación o la alternativa constituye una publicación de comportamiento que requiere repetir la evaluación. Conserva el manifiesto anterior de versiones y una representación compatible del índice. La reversión puede restaurar el comportamiento, pero no retirar información divulgada ni deshacer el envío de solicitudes al proveedor. Una divulgación necesita gestión de incidentes y revisión de acceso y datos; eliminar únicamente un registro local es insuficiente.

Asigna responsables de la deriva de evaluación, la política de acceso, los incidentes del proveedor y la escalada de costes. Presupuesta actualizaciones de embeddings e índices, reintentos, ejecuciones de evaluación, almacenamiento y revisión humana junto con la inferencia. Antes de producción, resuelve retención y residencia del proveedor, identidad real, cifrado, propagación de eliminaciones, límites contra el abuso y cobertura operativa. La retirada deshabilita puntos de entrada, termina el trabajo que pueda completarse de forma segura, elimina o conserva artefactos derivados según la política, revoca el acceso al proveedor y preserva solo la evidencia necesaria para rendir cuentas.

## Continuar con decisiones relacionadas

[Agentes](agents.md) · [Seguridad](security.md) · [Controles de calidad](quality.md) · [Estrategia de pruebas](testing-strategy.md)

## Evidencia primaria

[owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-xss](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
