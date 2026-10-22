---
{
  "id": "start",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Construye sistemas que perduren

Una biblioteca de trabajo para toda la vida del software: desde definir el problema hasta operar, migrar y retirar un sistema. Las personas deciden el propósito y aceptan el riesgo. Los agentes convierten decisiones acotadas en cambios comprobados. El inglés es canónico; checo, alemán y español comparten identificadores y revisiones.

## Empieza por una decisión

1. Documenta el resultado, la sensibilidad de los datos, el presupuesto operativo y la interrupción tolerable en un perfil de proyecto.
2. Elige la arquitectura más pequeña que satisfaga esas restricciones. Una herramienta personal puede tratar datos sensibles; un millón de cuentas registradas no implica gran concurrencia.
3. Registra las decisiones importantes en un ADR con pruebas, alternativas y una forma de revertirlas.
4. Asigna al agente una tarea pequeña con criterios de aceptación. Exige una comprobación independiente y aprobación humana para fusionar.
5. Opera lo construido: observa el comportamiento real, prueba la recuperación y revisa los supuestos cuando cambie la evidencia.

## Lee según la necesidad

Arquitectura y alojamiento ayudan a elegir la forma del sistema. Durabilidad, datos, seguridad y frontend describen sus contratos internos. GitHub, calidad y agentes gobiernan las entregas. Operación y mantenimiento mantienen sanos los productos y la biblioteca.

Cada guía explica contexto, decisión, costes, comprobaciones y señales de cambio. Descargar una fuente demuestra disponibilidad, no que una recomendación sea correcta. Esta primera edición propone orientaciones pendientes de revisión humana; las traducciones también necesitan revisión editorial. Las integraciones experimentales del navegador conservan esa etiqueta.

Cambia de idioma con el menú, busca conceptos y sigue las guías relacionadas. Clona el repositorio para leer sin conexión; el sitio y el adaptador MCP de lectura usan el mismo contenido. Leer, construir y validar no requiere una API de modelos de pago.

## Decisiones relacionadas

[Principios de decisión](guides/foundations.md) · [El ciclo de vida completo](guides/lifecycle.md) · [Elegir y conectar arquitecturas](guides/architecture.md) · [Adoptar la biblioteca en un proyecto](guides/adoption.md)

## Evidencia primaria

[plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md)
