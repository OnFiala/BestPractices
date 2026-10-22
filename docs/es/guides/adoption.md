---
{
  "id": "adoption",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Adoptar la biblioteca en un proyecto

## Paquete portable

Copia las plantillas necesarias. Completa `project-profile.yaml` con restricciones, responsables, sensibilidad, presupuesto, carga, SLO y recuperación. Referencia la biblioteca por release/commit e IDs; no sigas `main` silenciosamente para políticas productivas.

Crea un diagrama de contexto y el primer ADR. Registra reglas aceptadas, excepciones justificadas, responsable, caducidad y controles compensatorios. Mantén instrucciones breves en `AGENTS.md` con enlaces. Usa el paquete de tarea y checklist de entrega.

## Tres comienzos

- Una web personal puede usar hosting estático, historial Git y build reproducible. Las notas privadas requieren acceso apropiado.
- Un SaaS pequeño puede partir de aplicación modular, base gestionada y worker limitado. Antes de clientes reales necesita autorización por tenant, reconciliación de pagos, restauración y responsable operativo.
- Una plataforma grande mide particiones y aísla caminos críticos. Despliegues independientes y recuperación regional exigen consistencia, guardias y propiedad de migración; contar cuentas no basta.

## Uso continuo

Consulta guías al planificar, enlaza decisiones y pruebas al revisar, comprueba migración y recuperación al publicar. Devuelve mediciones e incidentes a los ADR. Actualiza la versión fijada mediante PR que explique obligaciones y proyectos afectados. Una plantilla existente no demuestra cumplimiento.

## Decisiones relacionadas

[Principios de decisión](foundations.md) · [El ciclo de vida completo](lifecycle.md) · [Dirección humana, ejecución de agentes](agents.md) · [Gobierno y decisiones abiertas](governance.md)

## Evidencia primaria

[plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md)
