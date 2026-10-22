---
{
  "id": "tools",
  "language": "es",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Fuentes y herramientas

Esta es una selección para una decisión definida, no un aval ni una instrucción de instalar todas las herramientas. Elige según las restricciones del proyecto y demuestra un flujo representativo antes de adoptar. Los nombres de herramientas y las claves de estado legibles por máquinas permanecen estables entre idiomas para que agentes y personas identifiquen el mismo producto. `candidate` significa evaluar antes de adoptar; `used-here` describe una capacidad realmente utilizada por esta biblioteca; `experimental` requiere comprobaciones explícitas de compatibilidad. Utilizar una herramienta aquí no la hace adecuada para todos los proyectos.

El inventario canónico es `data/tools.json`; el registro de fuentes es `data/sources.json`. Las exportaciones del sitio contienen los mismos inventarios. Los registros de fuentes separan la versión exacta inspeccionada, la URL supervisada para detectar cambios y la evidencia de licencia. Estos hechos establecen procedencia y un límite de revisión, no permiso para copiar la prosa de una fuente. El número de fuentes no demuestra profundidad técnica. Ninguna licencia desconocida se interpreta como permiso para reproducir documentación.

| Herramienta | Estado | Fuente |
| --- | --- | --- |
| Codex | `candidate` | [codex](https://raw.githubusercontent.com/openai/codex/b337fe06b7d8d6e5b42295e04c5e92c2b9c46567/README.md), [plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) |
| OpenAI Agents SDK | `candidate` | [openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/agents.md), [agents-guardrails](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/guardrails.md) |
| MCP Python SDK | `used-here` | [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/2af9e3089ac66b35c1550c500aae86a82efb1e17/README.md) |
| WebMCP | `experimental` | [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/51ed75653aaa7f174f8dbe05d1bc327359bbc57c/README.md) |
| MkDocs Material | `used-here` | [mkdocs-material](https://raw.githubusercontent.com/squidfunk/mkdocs-material/cbee8f352745a974e1bae7dc595793be9b6875d7/README.md) |
| GitHub Actions | `used-here` | [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md), [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) |
| PostgreSQL | `candidate` | [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml), [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) |
| Docker / Compose | `candidate` | [docker-security](https://raw.githubusercontent.com/docker/docs/4d64a8e4f0a59967fc0b391120d54a90e9ccb60d/content/manuals/engine/security/_index.md) |
| Kubernetes | `candidate` | [kubernetes](https://raw.githubusercontent.com/kubernetes/website/bc7f3479bc8b0af48097b155c22c8d58e8e1afe4/content/en/docs/concepts/architecture/_index.md) |
| OpenTofu | `candidate` | [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/ec773ed37be4d07e00d4a2fbb237d0c0fe1ca3ce/README.md) |
| OpenTelemetry | `candidate` | [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) |
| Temporal | `candidate` | [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/e8ee627110a98501103827745aab18aedf312dd0/README.md) |
| Playwright | `candidate` | [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) |
| Grafana k6 | `candidate` | [k6-test-types](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/_index.md), [k6-thresholds](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/using-k6/thresholds.md) |

## Elegir según la tarea

Usa Playwright para recorridos observables del navegador, con estado aislado y aserciones significativas; un script de navegador no es automáticamente una auditoría de accesibilidad ni una evaluación de seguridad. Usa k6 cuando se hayan definido una carga representativa, umbrales de latencia y error, un entorno permitido y un presupuesto de interrupción. Generar más solicitudes no produce por sí solo un resultado útil de capacidad. Consulta las guías de estrategia de pruebas, rendimiento y seguridad antes de que un agente ejecute estas herramientas.

La coordinación de agentes necesita límites de permisos, traspasos evaluados y un límite de coste total. El uso de nube y API puede generar cargos independientemente de que una biblioteca sea de código abierto. El repositorio público ejecuta observación de metadatos; la generación de IA alimentada con fuentes corresponde a un espacio de revisión privado. El alojamiento MCP, la instalación de plugins y el soporte nativo de WebMCP requieren comprobaciones reales de integración. Nunca promociones una API experimental o un modelo más nuevo solo por ser reciente. Confirma el soporte del producto y sus avisos de retirada antes de adoptar un ejemplo o contratar un servicio.

La prosa original en las exportaciones JSON de guías está bajo CC BY 4.0. El software de terceros incluido en el sitio conserva sus propios avisos y licencias. El archivo de bloqueo de dependencias de ejecución y el inventario de avisos de recursos deben cambiar juntos cuando un nuevo paquete modifique las obligaciones de redistribución.

## Decisiones relacionadas

[Skills, plugins, MCP y WebMCP](../guides/integrations.md) · [Alojamiento y estrategias de salida](../guides/hosting.md) · [Evidencia y mantenimiento automático](../guides/maintenance.md) · [Seleccionar y combinar pruebas](../guides/testing-strategy.md) · [Pruebas de rendimiento](../guides/performance-testing.md)

## Evidencia primaria

[mkdocs-material](https://raw.githubusercontent.com/squidfunk/mkdocs-material/cbee8f352745a974e1bae7dc595793be9b6875d7/README.md) · [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/2af9e3089ac66b35c1550c500aae86a82efb1e17/README.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [k6-test-types](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/_index.md)
