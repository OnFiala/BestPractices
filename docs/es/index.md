---
{
  "id": "start",
  "language": "es",
  "revision": 3,
  "translation_revision": 3,
  "reviewed_on": "2026-10-22"
}
---
# Construir sistemas que perduren

Una biblioteca de trabajo para toda la vida del software: desde la primera definición del problema hasta la operación fiable, la migración y la retirada. Las personas son responsables de la intención y el riesgo. Los agentes convierten decisiones acotadas en cambios probados. El inglés es la versión canónica; checo, alemán y español mantienen los mismos identificadores y revisiones de las guías.

Esta biblioteca es, en sí misma, un **sistema de decisiones mantenido por agentes**: los agentes de IA investigan, redactan, traducen y verifican; las personas son responsables de la aplicabilidad, la revisión de derechos, la fusión de cambios y la publicación. Las recomendaciones son propuestas contextualizadas, no reglas certificadas universalmente. Las explicaciones de ingeniería son una síntesis original; los documentos citados conservan sus propias licencias y no se reproducen como contenido nuestro.

## Tengo un proyecto: ¿por dónde empiezo?

Usa esta biblioteca para dar al agente una tarea clara, elegir un enfoque adecuado
y revisar el resultado. Proporciona recomendaciones, un plan y comprobaciones de
evidencias. Tu agente construye el producto real en tu entorno de desarrollo.

1. Lee [cómo adoptar la biblioteca](guides/adoption.md): elige el perfil de entrega
   JSON para las herramientas y, si lo necesitas, un documento YAML para decisiones más detalladas.
2. Sigue [tu primer punto de control con evidencias](guides/first-project.md):
   crea un resultado real, solicita su revisión y comprueba qué sigue bloqueado. No se necesita una API de modelos.
3. Elige tu proyecto a continuación y sigue [el flujo de entrega](guides/project-delivery.md).

| ¿Qué estás construyendo? | Empieza aquí |
| --- | --- |
| Sitio web público | [Sitio web público](guides/playbook-public-website.md) |
| SaaS | [SaaS](guides/playbook-saas.md) |
| Herramienta interna de operaciones | [Herramienta interna](guides/playbook-internal-tool.md) |
| Aplicación de IA | [Aplicación de IA](guides/playbook-ai-application.md) |
| Automatización de agentes | [Automatización de agentes](guides/playbook-agent-automation.md) |
| Backend y clientes móviles | [Backend móvil](guides/playbook-mobile-backend.md) |

## Asigna al agente su primera tarea

Sustituye los valores entre corchetes y entrega este texto a un agente que pueda
leer tu proyecto y una copia local confiable de esta biblioteca. No es necesario
instalar un plugin ni MCP.

```text
Trabaja en [proyecto de destino]. Usa [copia local de BestPractices] como referencia.
Lee las instrucciones del proyecto de destino y después, en la biblioteca,
plugins/bestpractices/skills/project-delivery/SKILL.md y la guía del tipo de proyecto correspondiente.
Resultado: [resultado observable]. Restricciones: [datos, presupuesto, efectos permitidos].
Registra la revisión de la biblioteca. Crea un perfil de entrega JSON con los
requisitos reales y la revisión Git de destino; deja explícitos los datos desconocidos.
Ejecuta el planificador y aborda el primer punto de control sin completar. Produce
su artefacto real, realiza una comprobación pertinente y obtén una revisión independiente
cuando esté disponible.
No inventes resultados ni revisores. Informa de las evidencias y los bloqueos pendientes.
Trabaja en local; no despliegues ni modifiques la biblioteca de referencia.
```

Un **punto de control** exige determinados resultados. Un **artefacto** es un documento,
un cambio de código o un informe. Las **evidencias** describen una inspección o prueba
real de ese resultado. Crear un plan no implementa el proyecto ni autoriza una publicación.
Para conocer lo que se demuestra en local y lo que aún necesita pruebas específicas
del proyecto, consulta [cobertura y límites](guides/coverage.md).

## Leer según la necesidad

Las guías de arquitectura y alojamiento ayudan a elegir una forma del sistema. Durabilidad, datos, seguridad y frontend explican los contratos dentro de esa forma. GitHub, calidad y agentes rigen la entrega. Operación y mantenimiento conservan la salud tanto de los productos como de esta biblioteca.

Para verificar, empieza por la [selección de pruebas](guides/testing-strategy.md). Distingue el propósito, el nivel y el conocimiento disponible para quien prueba; caja negra no significa únicamente pruebas de penetración. Usa las [pruebas de rendimiento](guides/performance-testing.md) para experimentos de carga, estrés, picos, duración prolongada y capacidad, y las [pruebas de seguridad](guides/security-testing.md) para controles basados en riesgo y evaluaciones acotadas. Cada guía ofrece a los agentes criterios de selección, requisitos de evidencia y condiciones de parada.

Cada guía identifica el contexto aplicable, una decisión, sus compensaciones, las comprobaciones y las señales de cambio. Obtener una fuente demuestra que está disponible, no que una recomendación sea correcta. Esta edición inicial contiene propuestas pendientes de revisión humana; las traducciones también necesitan revisión editorial. Las integraciones experimentales del navegador siguen identificadas explícitamente como experimentales.

Usa el menú de idiomas para cambiar de lengua, la búsqueda para encontrar un concepto y las guías relacionadas para seguir sus consecuencias. Clona el repositorio para leer sin conexión; el sitio web y el adaptador MCP de solo lectura usan el mismo contenido. No se necesita una API de modelos de pago para leer, compilar o validar la biblioteca.

## Decisiones relacionadas

[Principios de decisión](guides/foundations.md) · [El ciclo de vida completo](guides/lifecycle.md) · [Elegir y conectar arquitecturas](guides/architecture.md) · [Adoptar la biblioteca en un proyecto](guides/adoption.md)

## Evidencia primaria

[plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
