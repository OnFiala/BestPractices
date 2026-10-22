---
{
  "id": "integrations",
  "language": "es",
  "revision": 3,
  "translation_revision": 3,
  "reviewed_on": "2026-10-22"
}
---
# Skills, plugins, MCP y WebMCP

## Superficies de integración distintas

| Superficie | Función | Qué se entrega aquí |
| --- | --- | --- |
| Skill | Procedimiento repetible de agente con ámbito y comprobaciones | `architecture-review`, `maintain-library`, `test-strategy`, `project-delivery` y `release-review` |
| Plugin de Codex | Manifiesto que empaqueta skills y herramientas opcionales | Paquete local compuesto solo por skills; la instalación todavía requiere verificación en el anfitrión |
| MCP | Protocolo de herramientas y recursos entre anfitrión y servidor | Búsqueda, lectura de guías, planificación y evaluación de entregas, y cobertura de solo lectura por stdio |
| ChatGPT Apps SDK | Integración con ChatGPT mediante MCP e interfaz opcional | Guía de integración; no se han provisionado alojamiento público ni autenticación |
| WebMCP | Herramientas dentro de una página mediadas por el navegador | Adaptador experimental de búsqueda con detección de capacidades |

El antiguo repositorio `skills` de OpenAI apunta actualmente a `plugins`. Sigue los ejemplos actuales de manifiestos de plugins; no supongas que los plugins antiguos de ChatGPT, los plugins de Codex y las aplicaciones del Apps SDK sean intercambiables.

## MCP local

Ejecuta `uv run python -m library.mcp_server` desde el repositorio local, o configura un anfitrión con `uv --directory /absolute/path/BestPractices run --frozen python -m library.mcp_server`. El servidor stdio expone el recurso de catálogo y `search_guides`, `get_guide`, `plan_delivery`, `assess_delivery` y `get_coverage`, sin herramientas de escritura ni acceso a rutas arbitrarias. Una conexión remota de ChatGPT necesita un transporte HTTPS compatible, autenticación y límites de tasa explícitos, alojamiento y una prueba real de compatibilidad con el anfitrión. GitHub Pages no puede ejecutar ese servidor.

La planificación devuelve un plan condicional del ciclo de vida; la evaluación examina los registros de evidencia aportados; la cobertura describe el ámbito declarado de las guías y referencias y sus carencias. Consulta el [flujo de entrega de proyectos](project-delivery.md) y los [límites de cobertura](coverage.md). Estas herramientas no ejecutan tareas ni pruebas, no autentican las etiquetas de los revisores ni la aprobación humana, no fusionan PR ni despliegan servicios. El anfitrión realiza el trabajo autorizado mediante herramientas separadas; las observaciones locales no son certificaciones firmadas.

## Experimento en navegador

La explicación de WebMCP inspeccionada usa `document.modelContext.registerTool`, cancelación del registro mediante una señal de interrupción y notificaciones `toolchange`. Es un trabajo en evolución, no una garantía universal de compatibilidad de navegadores. Detecta capacidades, conserva la búsqueda ordinaria y prueba permisos, cancelación, navegación y ausencia de soporte. No inventes eventos estándar a partir de propuestas; la telemetría de la aplicación debe usar nombres propios. El adaptador incluido solo expone búsqueda en la biblioteca pública y no emite analítica externa.

## Qué debe declarar una integración

Las recomendaciones devueltas son contenido propuesto y asistido por agentes que requiere revisión humana. Conserva la autoría, la revisión, los identificadores de fuentes y los metadatos de licencia del contenido cuando lo muestres o almacenes en caché. La prosa sigue bajo CC BY 4.0 cuando se transporta en JSON; los textos de las fuentes externas no se incluyen ni se relicencian. Una anotación de herramienta como solo lectura es descriptiva, no autorización aplicada en servidor. No des a un conector de recuperación credenciales de escritura en producción ni supongas que las instrucciones de un prompt imponen un límite de permisos.

Antes de adoptar, ejecuta una prueba real de compatibilidad con el anfitrión: búsqueda y lectura correctas, identificador desconocido, idioma no admitido, cancelación, entrada mal formada y servidor no disponible. Las pruebas simuladas de WebMCP no demuestran soporte nativo del navegador. Usa las guías de [estrategia de pruebas](testing-strategy.md) y [pruebas de seguridad](security-testing.md) para elegir otros límites. Toda generación alimentada con fuentes debe respetar el límite de revisión privada y traslado público descrito en [mantenimiento](maintenance.md).

## Decisiones relacionadas

[Dirección humana, ejecución de agentes](agents.md) · [Arquitectura y contratos del frontend](frontend.md) · [Seguridad, privacidad y cadena de suministro](security.md) · [Evidencia y mantenimiento automático](maintenance.md)

## Evidencia primaria

[plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [skills](https://raw.githubusercontent.com/openai/skills/49f948faa9258a0c61caceaf225e179651397431/README.md) · [openai-apps](https://raw.githubusercontent.com/openai/openai-apps-sdk-examples/18cc38e78a968712c357bacdc3c79fead5bfc6b4/README.md) · [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/2af9e3089ac66b35c1550c500aae86a82efb1e17/README.md) · [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/51ed75653aaa7f174f8dbe05d1bc327359bbc57c/README.md)
