---
{
  "id": "integrations",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Skills, pluginy, MCP a WebMCP

## Různé integrační plochy

| Plocha | Úloha | Co je zde |
| --- | --- | --- |
| Skill | Opakovatelný postup agenta | Architektonické review a údržba |
| Codex plugin | Manifest pro skills a nástroje | Místní balíček; instalaci musí ověřit hostitel |
| MCP | Protokol nástrojů a zdrojů | Otestované čtení a hledání přes stdio |
| ChatGPT Apps SDK | Integrace ChatGPT přes MCP a případné UI | Návod; veřejný hosting a autentizace nejsou zřízeny |
| WebMCP | Nástroje přímo ve stránce | Experimentální hledání s detekcí podpory |

Původní OpenAI `skills` nyní odkazuje na `plugins`. Řiďte se aktuálním manifestem; historické ChatGPT pluginy, Codex pluginy a Apps SDK nejsou zaměnitelné.

## Místní MCP

V checkoutu spusťte `uv run python -m library.mcp_server`; host může použít `uv --directory /absolute/path/BestPractices run --frozen python -m library.mcp_server`. Rozhraní nabízí katalog, hledání a známá ID bez zápisu a libovolných cest. Vzdálený ChatGPT vyžaduje podporovaný HTTPS transport, autentizaci/limity, hosting a skutečný test hostitele. Pages tento server nespustí.

## Experiment prohlížeče

Ověřený návrh WebMCP používá `document.modelContext.registerTool`, odregistrování přes abort signal a `toolchange`. Jde o vyvíjený návrh, ne univerzální podporu. Detekujte funkce, zachovejte běžné hledání a testujte oprávnění, rušení, navigaci i chybějící podporu. Nevydávejte návrhy událostí za standard; vlastní telemetrie má vlastní jména. Adaptér hledá jen veřejnou knihovnu a neposílá externí analytiku.

## Související rozhodnutí

[Člověk řídí, agent vykonává](agents.md) · [Architektura frontendu a smlouvy](frontend.md) · [Bezpečnost, soukromí a závislosti](security.md) · [Důkazy a automatická údržba](maintenance.md)

## Primární zdroje

[plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md) · [skills](https://raw.githubusercontent.com/openai/skills/main/README.md) · [openai-apps](https://raw.githubusercontent.com/openai/openai-apps-sdk-examples/main/README.md) · [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md) · [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/main/README.md)
