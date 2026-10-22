---
{
  "id": "adoption",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Použití knihovny v projektu

## Přenosný projektový balíček

Kopírujte potřebné šablony, ne celou knihovnu. V `project-profile.yaml` vyplňte omezení, vlastníka, citlivost, rozpočet, zátěž, SLO a obnovu. Knihovnu odkazujte releasem nebo commitem a ID průvodců; produkční pravidla nesmí tiše sledovat pohyblivou `main`.

Vytvořte kontextový diagram a první ADR. Zapište přijatá pravidla, zdůvodněné výjimky, vlastníka, expiraci a náhradní kontroly. Do `AGENTS.md` dejte krátké projektové pokyny s odkazy. Pro změnu použijte balíček úkolu a před vydáním checklist.

## Tři počátky

- Osobní znalostní web může mít statický hosting, historii v Gitu a opakovatelný build. Soukromé poznámky potřebují odpovídající přístup.
- Malý SaaS začíná modulární aplikací, spravovanou databází a omezeným workerem. Před skutečnými zákazníky potřebuje tenantovou autorizaci, sladění plateb, obnovu a provozního vlastníka.
- Velká platforma měří oddíly a izoluje kritické cesty. Samostatná vydání a regionální obnova potřebují konzistenci, pohotovost a vlastníky migrace; počet účtů nestačí.

## Průběžné použití

Při plánování čtěte příslušné průvodce, v review odkazujte rozhodnutí a důkazy, při vydání ověřte migraci a obnovu. Provozní měření vracejte do ADR. Připnutou knihovnu aktualizujte přes PR vysvětlující dopad. Existence šablony nedokazuje splnění pravidel.

## Související rozhodnutí

[Principy rozhodování](foundations.md) · [Celý životní cyklus projektu](lifecycle.md) · [Člověk řídí, agent vykonává](agents.md) · [Správa a otevřená rozhodnutí](governance.md)

## Primární zdroje

[plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md)
