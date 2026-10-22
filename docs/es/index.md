---
{
  "id": "start",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Construir sistemas que perduren

Una biblioteca de trabajo para toda la vida del software: desde la primera definición del problema hasta la operación fiable, la migración y la retirada. Las personas son responsables de la intención y el riesgo. Los agentes convierten decisiones acotadas en cambios probados. El inglés es la versión canónica; checo, alemán y español mantienen los mismos identificadores y revisiones de las guías.

Esta biblioteca es, en sí misma, un **sistema de decisiones mantenido por agentes**: los agentes de IA investigan, redactan, traducen y verifican; las personas son responsables de la aplicabilidad, la revisión de derechos, la fusión de cambios y la publicación. Las recomendaciones son propuestas contextualizadas, no reglas certificadas universalmente. Las explicaciones de ingeniería son una síntesis original; los documentos citados conservan sus propias licencias y no se reproducen como contenido nuestro.

## Empezar con una decisión

1. Define el resultado esperado, la sensibilidad de los datos, el presupuesto operativo y el tiempo de interrupción aceptable en un perfil de proyecto.
2. Elige la arquitectura más pequeña que cumpla esas restricciones. Una herramienta personal también puede tratar datos sensibles; un millón de cuentas registradas puede tener una concurrencia modesta.
3. Registra las elecciones importantes en un registro de decisión arquitectónica (ADR). Enlaza evidencia, alternativas y un plan de reversión.
4. Da al agente una tarea pequeña con criterios de aceptación. Exige una comprobación independiente y que una persona fusione los cambios.
5. Opera lo que construyes: observa el comportamiento real, prueba la recuperación y revisa los supuestos cuando cambie la evidencia.

## Leer según la necesidad

Las guías de arquitectura y alojamiento ayudan a elegir una forma del sistema. Durabilidad, datos, seguridad y frontend explican los contratos dentro de esa forma. GitHub, calidad y agentes rigen la entrega. Operación y mantenimiento conservan la salud tanto de los productos como de esta biblioteca.

Para verificar, empieza por la [selección de pruebas](guides/testing-strategy.md). Distingue el propósito, el nivel y el conocimiento disponible para quien prueba; caja negra no significa únicamente pruebas de penetración. Usa las [pruebas de rendimiento](guides/performance-testing.md) para experimentos de carga, estrés, picos, duración prolongada y capacidad, y las [pruebas de seguridad](guides/security-testing.md) para controles basados en riesgo y evaluaciones acotadas. Cada guía ofrece a los agentes criterios de selección, requisitos de evidencia y condiciones de parada.

Cada guía identifica el contexto aplicable, una decisión, sus compensaciones, las comprobaciones y las señales de cambio. Obtener una fuente demuestra que está disponible, no que una recomendación sea correcta. Esta edición inicial contiene propuestas pendientes de revisión humana; las traducciones también necesitan revisión editorial. Las integraciones experimentales del navegador siguen identificadas explícitamente como experimentales.

Usa el menú de idiomas para cambiar de lengua, la búsqueda para encontrar un concepto y las guías relacionadas para seguir sus consecuencias. Clona el repositorio para leer sin conexión; el sitio web y el adaptador MCP de solo lectura usan el mismo contenido. No se necesita una API de modelos de pago para leer, compilar o validar la biblioteca.

## Decisiones relacionadas

[Principios de decisión](guides/foundations.md) · [El ciclo de vida completo](guides/lifecycle.md) · [Elegir y conectar arquitecturas](guides/architecture.md) · [Adoptar la biblioteca en un proyecto](guides/adoption.md)

## Evidencia primaria

[plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
