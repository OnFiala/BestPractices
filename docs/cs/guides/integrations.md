---
{
  "id": "integrations",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Skills, pluginy, MCP a WebMCP

## Různé integrační možnosti

| Možnost | Úloha | Co je zde dodáno |
| --- | --- | --- |
| Skill | Opakovatelný postup agenta s rozsahem a kontrolami | Skills pro posouzení architektury a údržbu |
| Codex plugin | Manifest balící skills a volitelné nástroje | Lokální balíček obsahující pouze skills; instalaci je stále nutné ověřit v hostitelské aplikaci |
| MCP | Protokol nástrojů a zdrojů mezi hostitelem a serverem | Otestované vyhledávání a načítání průvodců pouze pro čtení přes stdio |
| ChatGPT Apps SDK | Integrace do ChatGPT pomocí MCP a volitelného rozhraní | Integrační průvodce; veřejný hosting ani autentizace nejsou zřízeny |
| WebMCP | Nástroje uvnitř stránky zprostředkované prohlížečem | Experimentální adaptér vyhledávání s detekcí podpory |

Dřívější repozitář OpenAI `skills` nyní odkazuje na `plugins`. Řiďte se aktuálními příklady manifestů pluginů; nepředpokládejte zaměnitelnost dřívějších ChatGPT pluginů, Codex pluginů a aplikací Apps SDK.

## Lokální MCP

V checkoutu spusťte `uv run python -m library.mcp_server`, nebo hostitele nakonfigurujte pomocí `uv --directory /absolute/path/BestPractices run --frozen python -m library.mcp_server`. Server zpřístupňuje katalog, vyhledávání a známé identifikátory průvodců bez nástroje pro zápis nebo přístup k libovolné cestě. Vzdálené připojení ChatGPT vyžaduje podporovaný přenos přes HTTPS, explicitní autentizaci a omezení četnosti požadavků, hosting a skutečný test kompatibility s hostitelem. GitHub Pages tento server spustit neumí.

## Experiment v prohlížeči

Prozkoumaný vysvětlující dokument WebMCP používá `document.modelContext.registerTool`, odregistrování pomocí abort signálu a oznámení `toolchange`. Jde o vyvíjející se návrh, nikoli univerzální záruku prohlížečů. Detekujte podporu, zachovejte běžné vyhledávání a testujte oprávnění, rušení operací, navigaci i nepřítomnost podpory. Z návrhů nevymýšlejte standardní události; telemetrie aplikace musí používat vlastní názvy. Přibalený adaptér zpřístupňuje pouze vyhledávání ve veřejné knihovně a neodesílá externí analytiku.

## Co musí integrace sdělovat

Vrácená doporučení vznikla s pomocí agentů, mají stav návrhu a vyžadují lidské posouzení. Při zobrazení nebo ukládání do cache zachovejte autorství, revizi, identifikátory zdrojů a metadata licence obsahu. Texty zůstávají pod CC BY 4.0 i při přenosu v JSON; texty zdrojů třetích stran nejsou zahrnuty ani přelicencovány. Anotace nástroje, například „pouze pro čtení“, je popisná a nepředstavuje autorizaci na serveru. Konektoru pro načítání dat nedávejte přihlašovací údaje pro zápis do produkce a nepředpokládejte, že instrukce v promptu vynucují hranici oprávnění.

Před přijetím proveďte skutečný test kompatibility s hostitelem: úspěšné vyhledání a čtení, neznámé ID, nepodporovaný jazyk, zrušení, chybný vstup a nedostupný server. Testy se simulovaným WebMCP nemohou doložit nativní podporu prohlížeče. Další hranice zvolte podle průvodců [strategií testování](testing-strategy.md) a [bezpečnostním testováním](security-testing.md). Veškeré generování využívající zdroje se musí řídit hranicí mezi soukromým posouzením a veřejným přenosem popsanou v [údržbě](maintenance.md).

## Související rozhodnutí

[Člověk určuje směr, agent vykonává](agents.md) · [Architektura frontendu a kontrakty](frontend.md) · [Bezpečnost, soukromí a dodavatelský řetězec softwaru](security.md) · [Důkazy a automatická údržba](maintenance.md)

## Primární zdroje


[plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [skills](https://raw.githubusercontent.com/openai/skills/49f948faa9258a0c61caceaf225e179651397431/README.md) · [openai-apps](https://raw.githubusercontent.com/openai/openai-apps-sdk-examples/18cc38e78a968712c357bacdc3c79fead5bfc6b4/README.md) · [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/2af9e3089ac66b35c1550c500aae86a82efb1e17/README.md) · [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/51ed75653aaa7f174f8dbe05d1bc327359bbc57c/README.md)
