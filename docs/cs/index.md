---
{
  "id": "start",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Budujte systémy, které vydrží

Pracovní knihovna pro celý život softwaru: od prvního vymezení problému po spolehlivý provoz, migraci a ukončení. Člověk odpovídá za záměr a riziko. Agenti převádějí ohraničená rozhodnutí na otestované změny. Kanonickým jazykem je angličtina; čeština, němčina a španělština se udržují se stejnými identifikátory průvodců a revizemi.

Sama knihovna je **rozhodovací systém udržovaný agenty**: AI agenti zkoumají, píší, překládají a ověřují; lidé odpovídají za použitelnost, posouzení práv, sloučení a zveřejnění. Doporučení jsou návrhy závislé na kontextu, nikoli univerzálně certifikovaná pravidla. Technická vysvětlení jsou původní syntézou; citované dokumenty si ponechávají své licence a nejsou přebírány jako náš obsah.

## Začněte rozhodnutím

1. V profilu projektu definujte výsledek, citlivost dat, provozní rozpočet a přijatelnou dobu výpadku.
2. Zvolte nejmenší architekturu, která tato omezení splní. I osobní nástroj může zpracovávat citlivá data; i milion registrovaných účtů může znamenat jen malý souběh.
3. Významné volby zachyťte v záznamu architektonického rozhodnutí (ADR). Připojte důkazy, alternativy a plán návratu.
4. Dejte agentovi malý úkol s akceptačními kritérii. Vyžadujte nezávislou kontrolu a sloučení člověkem.
5. Provozujte, co vytvoříte: sledujte skutečné chování, testujte obnovu a při změně důkazů přehodnocujte předpoklady.

## Čtěte podle potřeby

Průvodci architekturou a hostingem pomohou zvolit podobu systému. Odolnost, data, bezpečnost a frontend vysvětlují kontrakty uvnitř této podoby. GitHub, kvalita a agenti řídí dodávání změn. Provoz a údržba udržují zdravé produkty i tuto knihovnu.

Při ověřování začněte [výběrem testů](guides/testing-strategy.md). Rozlišuje účel, úroveň a znalosti dostupné testujícímu; black-box neznamená pouze penetrační testování. [Výkonnostní testování](guides/performance-testing.md) použijte pro experimenty s běžnou zátěží, přetížením, náhlými špičkami, dlouhodobým zatížením a kapacitou; [bezpečnostní testování](guides/security-testing.md) pro kontroly podle rizik a ohraničené posuzování. Každý průvodce dává agentům kritéria výběru, požadavky na důkazy a podmínky zastavení.

Každý průvodce uvádí použitelný kontext, rozhodnutí, kompromisy, kontroly a signály ke změně. Načtení zdroje dokládá dostupnost, nikoli správnost doporučení. Toto první vydání obsahuje navržená doporučení čekající na lidské posouzení; překlady také vyžadují redakční kontrolu. Experimentální integrace prohlížeče zůstávají výslovně experimentální.

Nabídkou jazyků přepnete jazyk, vyhledáváním najdete pojem a souvisejícími průvodci budete sledovat důsledky. Pro čtení offline naklonujte repozitář; web a MCP adaptér pouze pro čtení používají stejný obsah. Ke čtení, sestavení ani validaci knihovny nepotřebujete placené API modelu.

## Související rozhodnutí

[Principy rozhodování](guides/foundations.md) · [Úplný životní cyklus projektu](guides/lifecycle.md) · [Volba a propojení architektur](guides/architecture.md) · [Zavedení knihovny v projektu](guides/adoption.md)

## Primární zdroje


[plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
