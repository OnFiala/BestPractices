---
{
  "id": "lifecycle",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# El ciclo de vida completo

## Etapas con criterios de salida

| Etapa | Entregable | Evidencia |
| --- | --- | --- |
| Descubrir | Problema, participantes y mapa de datos | Resultado medible y objetivos excluidos |
| Diseñar | Perfil, diagrama de contexto, ADR, amenazas | Restricciones y recuperación aceptadas por una persona |
| Planificar | Tareas pequeñas, dependencias y ejemplos | Responsable, alcance, pruebas y condiciones de parada |
| Construir | Código, migraciones, pruebas y explicación | Comprobaciones reproducibles y diff revisable |
| Publicar | Versión, notas, despliegue y reversión | Smoke test, recuperación preparada y aprobación |
| Operar | Runbook, paneles, soporte y costes | Objetivos medidos y recuperación ensayada |
| Evolucionar | Aprendizaje, deprecación y migraciones | Consumidores migrados antes de eliminar |
| Retirar | Exportación/borrado y revocación de accesos | Retención cumplida; facturación y credenciales cerradas |

La profundidad cambia, no los criterios. Un script personal puede usar un documento breve; un sistema de consecuencias graves necesita más evidencia independiente. Cada documento debe servir a una decisión o acción operativa.

## Contrato entre persona y agente

La persona define valor, prioridades, tolerancia al riesgo y autoridad de publicación. El agente investiga, propone, implementa, prueba y comunica incertidumbre. Una tarea termina con pruebas, no con una declaración. Guarda los supuestos en el repositorio, sin depender del historial del chat.

## Verificar y cambiar de rumbo

Demuestra un recorrido completo antes de ampliar funciones: incluye errores, acceso denegado, estados vacíos y recuperación. Si el resultado no es medible, vuelve al descubrimiento. Cuando costes o responsabilidades superen la capacidad disponible, simplifica antes de automatizar más. Planifica la retirada desde el principio: los usuarios necesitan salir y recuperar sus datos.

## Decisiones relacionadas

[Controles que demuestran comportamiento](quality.md) · [Salud, recuperación y costes](operations.md) · [Dirección humana, ejecución de agentes](agents.md) · [Adoptar la biblioteca en un proyecto](adoption.md)

## Evidencia primaria

[github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml)
