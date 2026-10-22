---
{
  "id": "agents",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Člověk řídí, agent vykonává

## Ohraničené delegování

Úkol obsahuje přínos, ID průvodců, omezení, povolené soubory/nástroje, příklady přijetí, rozpočet a podmínky zastavení. Člověk vlastní architekturu a riziko; agent zkoumá a staví. Oddělte implementaci, ověření a lidské review i při více průchodech stejného modelu. Opakovaný závěr není nezávislý důkaz.

Responses API použijte při vlastní řídicí smyčce; Agents SDK při doložené potřebě orchestrace a předávání. Začněte jedním agentem. Paralelní agenti potřebují nezávislé úkoly, vlastníky zápisů, koordinaci a celkový limit ceny.

## Řízení

Nastavte oprávnění nástrojů, omezené identity, timeouty, počet iterací, tokeny/cenu a ID běhů. Guardrails nenahrazují autorizaci ani izolaci. Zdroje a výsledky nástrojů mohou obsahovat prompt injection. Zastavte při konfliktu, chybějícím předpokladu, nečekané destrukci nebo neúspěšné povinné kontrole.

## Přijetí a evaluace

Vyžadujte diff, skutečně spuštěné kontroly, nejistoty a obnovu. Hodnoťte reprezentativní i útočné vstupy a selhání. Měřte úspěch úkolů, lidské opravy, uniklé chyby, latenci a cenu, ne množství kódu. Udržujte regresní sadu pro změny promptů, modelů, nástrojů a pravidel. Novější model nepromujte pouze podle jména nebo data.

## Související rozhodnutí

[Kontroly kvality dokazující chování](quality.md) · [Bezpečnost, soukromí a závislosti](security.md) · [Důkazy a automatická údržba](maintenance.md) · [Skills, pluginy, MCP a WebMCP](integrations.md)

## Primární zdroje

[openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/main/docs/agents.md) · [agents-guardrails](https://raw.githubusercontent.com/openai/openai-agents-python/main/docs/guardrails.md) · [codex-action](https://raw.githubusercontent.com/openai/codex-action/main/README.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md)
