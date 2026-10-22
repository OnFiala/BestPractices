---
{
  "id": "quality",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Controles de calidad que demuestran comportamiento

## Elegir la evidencia según el cambio

Las pruebas forman parte de la definición de la tarea del agente. Antes de implementar, identifica el comportamiento en riesgo, la consecuencia de un fallo y la observación que demostraría un defecto. Elige un conjunto proporcionado de comprobaciones mediante la [estrategia de pruebas](testing-strategy.md). Los límites sensibles para la seguridad también requieren [pruebas de seguridad](security-testing.md); los cambios en concurrencia, recursos o capacidad requieren [pruebas de rendimiento](performance-testing.md).

Una corrección de texto necesita revisión editorial y comprobación de enlaces, no una nueva batería de pruebas basada en simulaciones. Un reintento de pago, un filtro por inquilino, una migración de base de datos o un cambio en una herramienta con privilegios necesita evidencia sobre sus rutas de fallo. «Todas las pruebas existentes pasan» no responde a si el contrato modificado tiene una prueba.

## Evidencia antes de implementar

El paquete de la tarea registra el consumidor afectado, el comportamiento esperado de éxito y de rechazo, los datos representativos, el entorno de ejecución y el resultado aceptable. Incluye al menos un caso negativo o de límite relevante cuando un comportamiento pueda fallar con consecuencias importantes. Mantén los resultados esperados independientes del algoritmo que se implementa: una prueba que vuelva a calcular la misma fórmula defectuosa puede coincidir con el error.

Para corregir un fallo, demuestra cuando sea práctico que la comprobación específica detecta el problema original. Para un nuevo invariante, desafía la prueba con datos deliberadamente inválidos o una alteración local temporal. Elimina esa alteración antes de proponer el cambio. Esta biblioteca recomienda estas comprobaciones según el riesgo; no exige pruebas de mutación para cada edición ni un porcentaje universal de cobertura.

## Crear un control de entrega útil

Exige una instalación reproducible de dependencias y una compilación adecuada a las tecnologías utilizadas. Añade comprobaciones de tipos, estilo y análisis estático cuando detecten defectos plausibles. Ejecuta primero comprobaciones específicas de comportamiento y, después, la batería de integración o de contratos afectada. Usa implementaciones reales de los límites cuando se comprueben aislamiento, transacciones, serialización, eventos del navegador o permisos; las simulaciones por sí solas no demuestran esas propiedades.

Mantén un pequeño conjunto de recorridos de extremo a extremo que cubran resultados valiosos para el usuario y sus estados críticos de fallo. Utiliza cuentas aisladas y datos sintéticos. Controla las dependencias externas en las pruebas repetibles y ejecuta, por separado y con un ámbito definido, comprobaciones de compatibilidad contra los entornos de prueba de los proveedores. Una prueba de correo o de pagos no debe contactar con clientes reales ni cobrar accidentalmente a una cuenta real.

Las comprobaciones obligatorias deben hacer fallar el trabajo de entrega cuando fallen. Informa por separado de los casos superados, fallidos, omitidos, en cuarentena y no ejecutados. No rebajes un umbral ni elimines una aserción solo para hacer pasar un cambio. Un requisito que realmente haya cambiado necesita su propia explicación y revisión humana. Las pruebas inestables en cuarentena necesitan una persona responsable, un motivo, una fecha de caducidad y evidencia sustitutiva para el comportamiento que protegían.

## Evidencia para cambios generados por IA

Revisa conjuntamente el diff final y las pruebas. Quien revise debe cuestionar los supuestos de quien implementa, no limitarse a repetir el mismo prompt. Usa un conjunto representativo de regresión para los cambios en modelos, prompts, herramientas, recuperación de información y políticas. Separa los ejemplos de desarrollo de los casos reservados para evaluación. Evalúa tanto la finalización útil de la tarea como los efectos no deseados; una respuesta convincente no demuestra que una herramienta se haya ejecutado con seguridad.

Registra el modelo y su configuración, la versión de los datos de prueba, la política de herramientas, las repeticiones, la rúbrica de puntuación y la variabilidad observada. Calibra la evaluación realizada por modelos con ejemplos revisados por personas y comprobaciones deterministas cuando sea posible. Protege los datos de evaluación frente a filtraciones entre inquilinos e inyección de instrucciones. Cambiar de producto o proveedor de evaluación no elimina la necesidad de estos registros.

## Decisión de publicación y mantenimiento

El agente entrega la revisión exacta, los comandos, el entorno, los resultados, las omisiones conocidas y el plan de recuperación. Detén la publicación afectada cuando falle una comprobación obligatoria, un comportamiento importante siga sin probarse o la evidencia disponible contradiga el resultado declarado. Una persona puede registrar una excepción limitada en el tiempo, con una persona responsable y un control compensatorio; el agente no debe reinterpretar silenciosamente un fallo como un éxito.

Lleva un seguimiento de los defectos detectados en producción, las comprobaciones inestables, la lentitud de la respuesta y la recuperación de cambios. Añade una prueba de regresión específica después de un incidente significativo. Elimina comprobaciones solo cuando su finalidad protectora haya quedado obsoleta o esté mejor cubierta de otra manera. El objetivo es obtener evidencia creíble con un coste sostenible, no maximizar el número de pruebas.

## Esta biblioteca y el alcance de su evidencia

Este repositorio valida la identidad del contenido, las referencias a fuentes, las revisiones de las traducciones, los enlaces, el comportamiento de las integraciones y la generación del sitio. Esas comprobaciones no certifican las recomendaciones arquitectónicas ni el significado de las traducciones. La revisión editorial humana sigue siendo un control separado.

El flujo anterior es una síntesis local original. Playwright respalda las comprobaciones de navegador aisladas y orientadas al comportamiento visible; OWASP respalda las pruebas de autorización y de abuso de agentes; GitHub documenta los límites de confianza de los workflows. Estas fuentes no constituyen un estándar universal de pruebas ni un aval de esta biblioteca.

## Decisiones relacionadas

[Estrategia de pruebas](testing-strategy.md) · [Pruebas de rendimiento y estrés](performance-testing.md) · [Pruebas de seguridad](security-testing.md) · [Dirección humana, ejecución de agentes](agents.md) · [El ciclo de vida completo](lifecycle.md)

## Evidencia primaria

[playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md)
