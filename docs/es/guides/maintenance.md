---
{
  "id": "maintenance",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Evidencia y mantenimiento automático

## Flujo de evidencia

`data/sources.json` registra fuentes primarias, alcance, fecha e intervalo. La referencia conserva hashes de descargas exitosas. Un observador programado obtiene documentos HTTPS limitados y señala cambios, indisponibilidad o revisión vencida. Un hash distinto pide revisión, no autoriza modificar recomendaciones. Un fallo no significa ausencia de cambios.

El workflow abre o actualiza un PR de evidencia cuando hace falta. No cambia la referencia aceptada ni fusiona. Una persona revisa diferencias, afirmaciones y aplicabilidad, y decide actualizar guías, traducciones, fechas y hashes juntos. HTTP 200 no renueva la revisión semántica.

## Mantenimiento con agentes

El workflow Codex opcional propone cambios acotados. Requiere secreto GitHub y activación explícita; validación y fuentes no necesitan API pagada. El agente edita guías traducidas existentes y catálogo. Otro job abre un PR borrador; el agente no fusiona. Activa rulesets y revisión humana en GitHub.

## Vigencia y fallos

Revisa fuentes rápidas de IA/protocolos más frecuentemente. Etiqueta experimentos, deprecaciones y desacuerdos; conserva migraciones. Credenciales ausentes, redes bloqueadas, checks fallidos y traducciones antiguas siguen visibles. Mide retraso y resolución. Revierte consejos erróneos por commit y evalúa proyectos que los adoptaron.

## Decisiones relacionadas

[GitHub, versiones y árboles limpios](github.md) · [Dirección humana, ejecución de agentes](agents.md) · [Gobierno y decisiones abiertas](governance.md)

## Evidencia primaria

[codex-action](https://raw.githubusercontent.com/openai/codex-action/main/README.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/main/content/actions/reference/security/secure-use.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md)
