---
{
  "id": "agents",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Dirección humana, ejecución de agentes

## Delegación acotada

Una tarea incluye resultado, IDs de guías, restricciones, archivos/herramientas permitidos, aceptación, presupuesto y parada. La persona decide arquitectura y riesgo; el agente investiga y construye. Separa implementación, verificación y revisión humana, incluso usando varias pasadas del mismo modelo. Repetir una conclusión no aporta independencia.

Usa Responses API para controlar el bucle; considera Agents SDK si resuelve orquestación demostrada. Empieza con un agente. El paralelismo necesita tareas independientes, propiedad de escrituras, coordinación y presupuesto global.

## Control

Define autorización de herramientas, identidades limitadas, timeouts, iteraciones, tokens/coste e IDs auditables. Los guardrails no sustituyen autorización ni aislamiento. Fuentes y respuestas pueden contener prompt injection. Detente ante conflictos, prerrequisitos ausentes, destrucción inesperada o checks obligatorios fallidos.

## Aceptación y evaluación

Exige diff, pruebas ejecutadas, incertidumbres y recuperación. Evalúa casos representativos, adversarios y fallos. Mide éxito, correcciones humanas, defectos escapados, latencia y coste, no volumen de código. Conserva regresiones para prompts, modelos, herramientas y políticas. No adoptes modelos nuevos solo por nombre o fecha.

## Decisiones relacionadas

[Controles que demuestran comportamiento](quality.md) · [Seguridad, privacidad y dependencias](security.md) · [Evidencia y mantenimiento automático](maintenance.md) · [Skills, plugins, MCP y WebMCP](integrations.md)

## Evidencia primaria

[openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/main/docs/agents.md) · [agents-guardrails](https://raw.githubusercontent.com/openai/openai-agents-python/main/docs/guardrails.md) · [codex-action](https://raw.githubusercontent.com/openai/codex-action/main/README.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md)
