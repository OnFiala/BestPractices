---
{
  "id": "tools",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Zdroje a nástroje

Jde o užší výběr pro konkrétní rozhodnutí, nikoli podporu produktu nebo pokyn nainstalovat všechny nástroje. Vybírejte podle omezení projektu a před přijetím prokažte jeden reprezentativní pracovní postup. Názvy nástrojů a strojové klíče stavů zůstávají ve všech jazycích stejné, aby lidé i agenti identifikovali tentýž produkt. `candidate` znamená posoudit před přijetím; `used-here` označuje možnost skutečně používanou touto knihovnou; `experimental` vyžaduje explicitní kontroly kompatibility. Používaný nástroj tím není vhodný pro každý projekt.

Kanonický inventář je `data/tools.json`; registr zdrojů je `data/sources.json`. Webové exporty nesou stejné inventáře. Záznamy zdrojů oddělují přesnou prozkoumanou verzi, URL sledovanou kvůli změnám a licenční podklady. Tyto údaje dokládají původ a hranici posouzení, nikoli schválení kopírování zdrojového textu. Počet zdrojů nedokládá technickou hloubku. Žádná neznámá licence se nepovažuje za svolení k přebírání dokumentace.

| Nástroj | Stav | Zdroj |
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

## Vybírejte podle úkolu

Playwright používejte pro pozorovatelné scénáře v prohlížeči s izolovaným stavem a smysluplnými ověřeními; skript prohlížeče není automaticky auditem přístupnosti ani bezpečnostním posouzením. k6 používejte, když je definována reprezentativní zátěž, prahy latence a chyb, povolené prostředí a rozpočet pro přerušení. Pouhé generování dalších požadavků není užitečným výsledkem o kapacitě. Než agent tyto nástroje spustí, prostudujte průvodce strategií testování, výkonnostním testováním a bezpečnostním testováním.

Orchestrace agentů potřebuje hranice oprávnění, vyhodnocená předání úloh a limit celkových nákladů. Používání cloudu nebo API může být zpoplatněno nezávisle na tom, zda je knihovna open source. Veřejný repozitář provádí sledování metadat; generování pomocí AI využívající zdroje patří do soukromého pracovního prostoru pro posouzení. Hosting MCP, instalace pluginu a nativní podpora WebMCP vyžadují skutečné integrační kontroly. Experimentální API ani novější model nikdy nepovyšujte jen kvůli jejich novosti. Před přijetím příkladu nebo koupí služby ověřte podporu produktu a oznámení o jeho ukončení.

Původní texty v JSON exportech průvodců jsou pod CC BY 4.0. Software třetích stran přibalený k webu si zachovává vlastní oznámení a licence. Pokud nový balíček mění povinnosti při redistribuci, musí se společně změnit lockfile běhových závislostí a inventář oznámení k prostředkům.

## Související rozhodnutí

[Skills, pluginy, MCP a WebMCP](../guides/integrations.md) · [Hosting a cesta k migraci](../guides/hosting.md) · [Důkazy a automatická údržba](../guides/maintenance.md) · [Výběr a kombinování testů](../guides/testing-strategy.md) · [Výkonnostní testování](../guides/performance-testing.md)

## Primární zdroje


[mkdocs-material](https://raw.githubusercontent.com/squidfunk/mkdocs-material/cbee8f352745a974e1bae7dc595793be9b6875d7/README.md) · [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/2af9e3089ac66b35c1550c500aae86a82efb1e17/README.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [k6-test-types](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/_index.md)
