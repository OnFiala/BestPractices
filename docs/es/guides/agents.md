---
{
  "id": "agents",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Dirección humana, ejecución de agentes

## Delegación acotada

El paquete de una tarea contiene el resultado esperado para el usuario, los identificadores de guías relevantes, las restricciones, los archivos y herramientas permitidos, ejemplos de aceptación, presupuesto y condiciones de parada. La persona responsable decide sobre arquitectura y riesgo; el agente investiga e implementa. Separa las responsabilidades de implementación, verificación y revisión humana, incluso cuando un modelo haga varias pasadas. Repetir la misma conclusión no constituye evidencia independiente.

Esta biblioteca aplica ese modelo de mantenimiento por agentes y declara su autoría asistida por agentes. Todas las recomendaciones y traducciones iniciales siguen siendo propuestas. Quien revise debe distinguir la evidencia del criterio local de ingeniería; la confianza de un modelo no sustituye ninguno de los dos.

Usa directamente la Responses API cuando necesites controlar el bucle de ejecución; considera el Agents SDK cuando su coordinación, herramientas y traspasos resuelvan una necesidad demostrada. Empieza con un agente. Los agentes paralelos necesitan trabajo independiente, responsabilidad explícita sobre las escrituras, coordinación de integración y un coste total acotado.

## Plano de control

Establece autorización a nivel de herramienta, credenciales acotadas, tiempos límite, máximo de iteraciones, presupuestos de tokens y coste e identificadores de ejecución auditables. Las medidas de supervisión del comportamiento lo mejoran, pero no sustituyen la autorización ni el aislamiento. Trata las fuentes y respuestas de herramientas como datos que pueden contener inyección de instrucciones. Detente ante instrucciones incompatibles, requisitos previos inaccesibles, efectos destructivos inesperados o fallos de comprobaciones obligatorias.

## Aceptación y evaluación

Exige un diff, comprobaciones ejecutadas, supuestos sin resolver y notas de recuperación. Evalúa las tareas con ejemplos representativos, incluidas entradas adversariales y rutas de fallo. Mide éxito de la tarea, corrección humana, defectos detectados en producción, latencia y coste, no volumen de código. Mantén un pequeño conjunto de regresión para cambios de prompts, modelos, herramientas y políticas. No promociones automáticamente un modelo más reciente porque cambien su nombre o su fecha de publicación.

Selecciona las pruebas explícitamente mediante la [estrategia de pruebas](testing-strategy.md): conocimiento —caja negra, gris o blanca—, nivel —unidad, integración, contrato o extremo a extremo— y objetivo son elecciones distintas. Usa los planes de [rendimiento](performance-testing.md) y [seguridad](security-testing.md) para sus riesgos respectivos. Registra autorización, objetivo y entorno, carga, umbrales de aceptación, condiciones de interrupción y limpieza antes de que un agente ejecute experimentos perturbadores o costosos.

## Originalidad y límite de publicación

Lee las fuentes como evidencia y explica la decisión con lenguaje y ejemplos originales. No copies, traduzcas ni parafrasees de cerca la prosa de las fuentes externas para incluirla en una guía; enlazarla no concede permiso de reutilización. La generación desatendida alimentada con fuentes se ejecuta en un repositorio o espacio de trabajo privado porque los registros sin procesar, las salidas del modelo, los resúmenes y los artefactos pueden divulgar texto de las fuentes antes de revisarlo. Una persona comprueba originalidad, derechos, datos sensibles y significado técnico antes de trasladar la salida aprobada a un PR público. Los trabajos públicos de observación de fuentes publican solo metadatos. Ni una comprobación de coincidencias ni un segundo agente otorgan conformidad legal.

## Decisiones relacionadas

[Controles de calidad que demuestran comportamiento](quality.md) · [Seguridad, privacidad y cadena de suministro](security.md) · [Evidencia y mantenimiento automático](maintenance.md) · [Skills, plugins, MCP y WebMCP](integrations.md)

## Evidencia primaria

[openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/agents.md) · [agents-guardrails](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/guardrails.md) · [codex-action](https://raw.githubusercontent.com/openai/codex-action/c05cfd74ad95c626cdf05c6685e62becc3bf7813/README.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md)
