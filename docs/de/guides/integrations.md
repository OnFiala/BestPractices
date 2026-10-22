---
{
  "id": "integrations",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Skills, Plugins, MCP und WebMCP

## Unterschiedliche Integrationsflächen

| Fläche | Aufgabe | Hier vorhanden |
| --- | --- | --- |
| Skill | Wiederholbares Agentenverfahren | Architekturprüfung und Pflege |
| Codex-Plugin | Manifest für Skills und Werkzeuge | Lokales Paket; Installation im Host noch zu prüfen |
| MCP | Werkzeug-/Ressourcenprotokoll | Getestete lesende stdio-Suche |
| ChatGPT Apps SDK | MCP und optionale Oberfläche in ChatGPT | Anleitung; kein öffentliches Hosting/Auth eingerichtet |
| WebMCP | Werkzeuge innerhalb einer Webseite | Experimenteller Suchadapter mit Erkennung |

OpenAIs früheres `skills`-Repository verweist nun auf `plugins`. Aktuelle Manifeste beachten; historische ChatGPT-Plugins, Codex-Plugins und Apps SDK sind nicht austauschbar.

## Lokales MCP

Im Checkout `uv run python -m library.mcp_server` starten; Hosts können `uv --directory /absolute/path/BestPractices run --frozen python -m library.mcp_server` nutzen. Katalog, Suche und bekannte IDs sind lesbar; Schreiben und freie Dateipfade fehlen. Entferntes ChatGPT benötigt unterstütztes HTTPS, Authentifizierung/Limits, Hosting und einen echten Kompatibilitätstest. Pages betreibt diesen Server nicht.

## Browserexperiment

Der geprüfte WebMCP-Entwurf nutzt `document.modelContext.registerTool`, Abmeldung per Abort-Signal und `toolchange`. Das ist Entwicklungsarbeit, keine allgemeine Browsergarantie. Funktionen erkennen, normale Suche erhalten und Rechte, Abbruch, Navigation sowie fehlende Unterstützung testen. Vorgeschlagene Ereignisse nicht als Standard ausgeben; eigene Telemetrie separat benennen. Der Adapter durchsucht nur öffentliche Inhalte ohne externe Analytik.

## Verwandte Entscheidungen

[Menschen steuern, Agenten führen aus](agents.md) · [Frontendarchitektur und Verträge](frontend.md) · [Sicherheit, Datenschutz und Lieferkette](security.md) · [Belege und automatische Pflege](maintenance.md)

## Primärbelege

[plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md) · [skills](https://raw.githubusercontent.com/openai/skills/main/README.md) · [openai-apps](https://raw.githubusercontent.com/openai/openai-apps-sdk-examples/main/README.md) · [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md) · [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/main/README.md)
