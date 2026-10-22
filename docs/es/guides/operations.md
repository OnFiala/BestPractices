---
{
  "id": "operations",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Salud, recuperación y costes

## Observar resultados del usuario

Un SLI mide éxito o latencia visible; un SLO fija un objetivo y ventana. Elige metas por negocio y capacidad medida, no por porcentajes de moda. El presupuesto de errores orienta entregas, no permite ignorar incidentes. Separa readiness y liveness para evitar tormentas de reinicio ante fallos transitorios.

Usa logs estructurados, métricas y trazas correlacionadas; limita cardinalidad y datos personales. Las alertas necesitan síntomas accionables, responsable, gravedad, runbook y escalado. Un panel no sustituye alertas. Mide coste por transacción útil y tarea de agente, incluidos reintentos y tokens.

## Responder y recuperar

Asigna dirección del incidente, limita impacto, conserva pruebas, comunica y restaura. Después documenta factores y acciones con responsables sin culpabilizar. Ensaya restauraciones, rotación y fallos de proveedor. Registra última recuperación exitosa y RTO/RPO medidos.

## Cadencia

Semanalmente: alertas, fuentes, dependencias y costes. Mensualmente: objetivos, restauraciones, responsabilidad y capacidad. Trimestralmente o tras cambios importantes: amenazas, desastre, arquitectura y retirada. Son cadencias iniciales adaptables. Un sistema sano demuestra comportamiento y recuperación, no solo procesos vivos.

## Decisiones relacionadas

[Durabilidad y trabajo distribuido](durability.md) · [Escalar con mediciones](scaling.md) · [El ciclo de vida completo](lifecycle.md)

## Evidencia primaria

[observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml)
