---
{
  "id": "integrations",
  "language": "de",
  "revision": 3,
  "translation_revision": 3,
  "reviewed_on": "2026-10-22"
}
---
# Skills, Plugins, MCP und WebMCP

## Unterschiedliche Integrationsflächen

| Fläche | Aufgabe | Hier vorhanden |
| --- | --- | --- |
| Skill | Wiederholbares Agentenverfahren mit Umfang und Prüfungen | `architecture-review`, `maintain-library`, `test-strategy`, `project-delivery` und `release-review` |
| Codex-Plugin | Manifest für Skills und optionale Werkzeuge | Lokales Paket ausschließlich mit Skills; Installation im Host noch zu verifizieren |
| MCP | Werkzeug- und Ressourcenprotokoll zwischen Host und Server | Schreibgeschützte Suche, Leitfadenabrufe, Auslieferungsplanung und -bewertung sowie Abdeckung über stdio |
| ChatGPT Apps SDK | ChatGPT-Integration mit MCP und optionaler Oberfläche | Integrationsleitfaden; öffentliches Hosting und Authentifizierung nicht eingerichtet |
| WebMCP | Durch den Browser vermittelte Werkzeuge innerhalb einer Seite | Experimenteller Suchadapter mit Fähigkeitserkennung |

OpenAIs früheres Repository `skills` verweist derzeit auf `plugins`. Orientiere dich an aktuellen Plugin-Manifestbeispielen. Frühere ChatGPT-Plugins, Codex-Plugins und Apps-SDK-Anwendungen sind nicht austauschbar.

## Lokales MCP

Starte `uv run python -m library.mcp_server` im Checkout oder konfiguriere einen Host mit `uv --directory /absolute/path/BestPractices run --frozen python -m library.mcp_server`. Der stdio-Server bietet die Katalogressource sowie `search_guides`, `get_guide`, `plan_delivery`, `assess_delivery` und `get_coverage`, ohne Schreibwerkzeug oder Zugriff auf beliebige Pfade. Eine entfernte ChatGPT-Verbindung braucht unterstützten HTTPS-Transport, ausdrückliche Authentifizierung und Ratenbegrenzung, Hosting sowie einen echten Kompatibilitätstest im Host. GitHub Pages kann diesen Server nicht ausführen.

Die Planung liefert einen bedingungsabhängigen Lebenszyklusplan; die Bewertung untersucht übermittelte Nachweisdatensätze; die Abdeckung beschreibt den erklärten Umfang der Leitfäden und Referenzen sowie Lücken. Siehe den [Projektauslieferungsablauf](project-delivery.md) und die [Abdeckungsgrenzen](coverage.md). Diese Werkzeuge führen weder Aufgaben noch Tests aus, authentifizieren weder Prüferbezeichnungen noch menschliche Genehmigungen, führen keine PRs zusammen und stellen keine Dienste bereit. Der Host erledigt autorisierte Arbeit mit getrennten Werkzeugen; lokale Beobachtungen sind keine signierten Bescheinigungen.

## Browserexperiment

Die untersuchte WebMCP-Beschreibung verwendet `document.modelContext.registerTool`, Abmeldung über Abort-Signal und `toolchange`-Benachrichtigungen. Das ist eine sich entwickelnde Spezifikation, keine allgemeine Browsergarantie. Erkenne Unterstützung zur Laufzeit, erhalte die gewöhnliche Suche und teste Berechtigungen, Abbruch, Navigation sowie fehlende Unterstützung. Erfinde keine Standardereignisse aus Vorschlägen; Anwendungstelemetrie benötigt eigene Namen. Der mitgelieferte Adapter bietet nur öffentliche Bibliothekssuche und sendet keine externe Analytik.

## Was eine Integration offenlegen muss

Die zurückgegebenen Hinweise sind agentengestützte Vorschläge und benötigen menschliches Review. Erhalte beim Anzeigen oder Zwischenspeichern Urheberschaft, Revision, Quellenkennungen und Inhaltslizenz. Fließtext bleibt auch im JSON-Transport CC BY 4.0. Fremde Quelltexte sind nicht enthalten und werden nicht neu lizenziert. Eine Werkzeugannotation wie „schreibgeschützt“ beschreibt Verhalten, erzwingt aber keine serverseitige Autorisierung. Gib einem Abrufkonnektor keine Produktionsschreibrechte und verlasse dich nicht auf Prompts als Berechtigungsgrenze.

Prüfe vor der Übernahme die tatsächliche Hostkompatibilität: erfolgreiche Suche und Abrufe, unbekannte Kennung, nicht unterstützte Sprache, Abbruch, fehlerhafte Eingabe und nicht verfügbarer Server. Simulierte WebMCP-Tests belegen keine native Browserunterstützung. Wähle weitere Grenzen mithilfe der [Teststrategie](testing-strategy.md) und [Sicherheitstests](security-testing.md). Jede aus Quellen gespeiste Generierung muss die in [Pflege](maintenance.md) beschriebene Grenze zwischen privatem Review und öffentlicher Übertragung beachten.

## Verwandte Entscheidungen

[Menschen steuern, Agenten führen aus](agents.md) · [Frontendarchitektur und Verträge](frontend.md) · [Sicherheit, Datenschutz und Lieferkette](security.md) · [Belege und automatische Pflege](maintenance.md)

## Primärbelege

[plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [skills](https://raw.githubusercontent.com/openai/skills/49f948faa9258a0c61caceaf225e179651397431/README.md) · [openai-apps](https://raw.githubusercontent.com/openai/openai-apps-sdk-examples/18cc38e78a968712c357bacdc3c79fead5bfc6b4/README.md) · [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/2af9e3089ac66b35c1550c500aae86a82efb1e17/README.md) · [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/51ed75653aaa7f174f8dbe05d1bc327359bbc57c/README.md)
