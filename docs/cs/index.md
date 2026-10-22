---
{
  "id": "start",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Stavějte systémy, které vydrží

Pracovní knihovna pro celý život softwaru: od formulace problému přes spolehlivý provoz až po migraci a ukončení. Člověk určuje záměr a přijímá rizika. Agenti převádějí ohraničená rozhodnutí na ověřené změny. Angličtina je výchozí; česká, německá a španělská mutace sdílejí stejné identifikátory a revize.

## Začněte rozhodnutím

1. Do profilu projektu zapište cíl, citlivost dat, provozní rozpočet a přijatelný výpadek.
2. Vyberte nejmenší architekturu, která omezení splní. Osobní nástroj může zpracovávat citlivá data; milion registrovaných účtů nemusí znamenat vysokou souběžnost.
3. Důležité volby zachyťte v ADR, tedy záznamu architektonického rozhodnutí. Přidejte důkazy, alternativy a cestu zpět.
4. Dejte agentovi malý úkol s podmínkami přijetí. Vyžadujte nezávislou kontrolu a lidské schválení sloučení.
5. Provozujte to, co stavíte: sledujte skutečné chování, testujte obnovu a přehodnocujte předpoklady.

## Čtěte podle potřeby

Architektura a hosting pomohou vybrat podobu systému. Odolnost, data, bezpečnost a frontend popisují jeho vnitřní smlouvy. GitHub, kvalita a agenti řídí dodávání. Provoz a údržba udržují zdravé produkty i tuto knihovnu.

Každý průvodce vymezuje kontext, rozhodnutí, náklady, kontroly a signály změny. Stažení zdroje dokládá dostupnost, nikoli správnost doporučení. První vydání obsahuje návrhy čekající na lidské posouzení; také překlady potřebují redakční kontrolu. Experimentální integrace prohlížeče zůstávají označené.

Jazyk přepnete v nabídce, pojem najdete vyhledáváním a souvislosti přes navazující průvodce. Repozitář lze číst offline; web i MCP používají stejný obsah. Čtení, sestavení ani validace nevyžadují placené modelové API.

## Související rozhodnutí

[Principy rozhodování](guides/foundations.md) · [Celý životní cyklus projektu](guides/lifecycle.md) · [Volba a propojení architektur](guides/architecture.md) · [Použití knihovny v projektu](guides/adoption.md)

## Primární zdroje

[plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md)
