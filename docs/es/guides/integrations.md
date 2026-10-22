---
{
  "id": "integrations",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Skills, plugins, MCP y WebMCP

## Superficies distintas

| Superficie | Función | Entregado aquí |
| --- | --- | --- |
| Skill | Procedimiento repetible | Revisión arquitectónica y mantenimiento |
| Plugin Codex | Manifest de skills y herramientas | Paquete local; falta verificar instalación en host |
| MCP | Protocolo de herramientas/recursos | Búsqueda y lectura stdio probadas |
| ChatGPT Apps SDK | MCP e interfaz opcional en ChatGPT | Guía; sin hosting público ni autenticación configurados |
| WebMCP | Herramientas dentro de la página | Búsqueda experimental con detección |

El antiguo repositorio `skills` de OpenAI remite a `plugins`. Sigue los manifests actuales; plugins históricos de ChatGPT, plugins Codex y Apps SDK no son intercambiables.

## MCP local

Ejecuta `uv run python -m library.mcp_server`; un host puede usar `uv --directory /absolute/path/BestPractices run --frozen python -m library.mcp_server`. Expone catálogo, búsqueda e IDs conocidos, sin escritura ni rutas arbitrarias. ChatGPT remoto necesita HTTPS compatible, autenticación/límites, hosting y una prueba real. Pages no ejecuta ese servidor.

## Experimento de navegador

El documento inspeccionado usa `document.modelContext.registerTool`, baja mediante AbortSignal y `toolchange`. Es una propuesta cambiante, no garantía universal. Detecta soporte, conserva búsqueda normal y prueba permisos, cancelación, navegación y ausencia de API. No presentes eventos propuestos como estándar; usa nombres propios para telemetría. El adaptador busca contenido público sin analítica externa.

## Decisiones relacionadas

[Dirección humana, ejecución de agentes](agents.md) · [Arquitectura frontend y contratos](frontend.md) · [Seguridad, privacidad y dependencias](security.md) · [Evidencia y mantenimiento automático](maintenance.md)

## Evidencia primaria

[plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md) · [skills](https://raw.githubusercontent.com/openai/skills/main/README.md) · [openai-apps](https://raw.githubusercontent.com/openai/openai-apps-sdk-examples/main/README.md) · [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md) · [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/main/README.md)
