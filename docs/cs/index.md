---
{
  "id": "start",
  "language": "cs",
  "revision": 3,
  "translation_revision": 3,
  "reviewed_on": "2026-10-22"
}
---
# Budujte systémy, které vydrží

Pracovní knihovna pro celý život softwaru: od prvního vymezení problému po spolehlivý provoz, migraci a ukončení. Člověk odpovídá za záměr a riziko. Agenti převádějí ohraničená rozhodnutí na otestované změny. Kanonickým jazykem je angličtina; čeština, němčina a španělština se udržují se stejnými identifikátory průvodců a revizemi.

Sama knihovna je **rozhodovací systém udržovaný agenty**: AI agenti zkoumají, píší, překládají a ověřují; lidé odpovídají za použitelnost, posouzení práv, sloučení a zveřejnění. Doporučení jsou návrhy závislé na kontextu, nikoli univerzálně certifikovaná pravidla. Technická vysvětlení jsou původní syntézou; citované dokumenty si ponechávají své licence a nejsou přebírány jako náš obsah.

## Mám projekt: kde začít?

Pomocí této knihovny dejte agentovi jasný úkol, vyberte vhodný přístup a posuďte
výsledek. Knihovna poskytuje doporučení, plán a kontroly důkazů. Skutečný produkt
vytváří váš agent ve vašem vývojovém prostředí.

1. Přečtěte si [použití knihovny v projektu](guides/adoption.md): zvolte JSON profil
   dodávání pro nástroje a případně YAML podklad pro podrobnější rozhodování.
2. Projděte [první kontrolní bránu s důkazy](guides/first-project.md): vytvořte jeden
   skutečný výstup, nechte jej posoudit a zjistěte, co zůstává zablokované. API modelu není potřeba.
3. Níže vyberte svůj projekt a potom pokračujte podle [postupu dodávání](guides/project-delivery.md).

| Co vytváříte? | Začněte zde |
| --- | --- |
| Veřejný web | [Veřejný web](guides/playbook-public-website.md) |
| SaaS | [SaaS](guides/playbook-saas.md) |
| Interní provozní nástroj | [Interní nástroj](guides/playbook-internal-tool.md) |
| Aplikace s AI | [Aplikace s AI](guides/playbook-ai-application.md) |
| Agentní automatizace | [Agentní automatizace](guides/playbook-agent-automation.md) |
| Backend a mobilní klienti | [Mobilní backend](guides/playbook-mobile-backend.md) |

## Zadejte agentovi první úkol

Nahraďte hodnoty v hranatých závorkách a předejte tento text agentovi, který může
číst váš projekt a důvěryhodnou místní pracovní kopii této knihovny. Instalace pluginu ani MCP není potřeba.

```text
Pracuj v [cílový projekt]. Používej [pracovní kopie BestPractices] jako referenci.
Přečti pokyny cílového projektu, potom soubor knihovny
plugins/bestpractices/skills/project-delivery/SKILL.md a odpovídající projektový postup.
Výsledek: [pozorovatelný výsledek]. Omezení: [data, rozpočet, povolené účinky].
Zaznamenej revizi knihovny. Vytvoř JSON profil dodávání podle skutečných
požadavků a cílové revize Gitu; neznámé údaje ponech výslovně označené.
Spusť plánovač a vezmi první nesplněnou kontrolní bránu. Vytvoř její skutečný artefakt,
proveď odpovídající kontrolu a zajisti nezávislé posouzení, pokud je dostupné.
Nevymýšlej výsledky ani posuzovatele. Uveď důkazy a zbývající překážky.
Pracuj lokálně; nic nenasazuj ani neupravuj referenční knihovnu.
```

**Kontrolní brána** je kontrolní bod s požadovanými výstupy. **Artefakt** je dokument,
změna kódu nebo zpráva. **Důkazy** popisují skutečné posouzení nebo test tohoto výstupu.
Vytvoření plánu projekt neimplementuje ani neopravňuje k vydání.
Co je prokázáno lokálně a co ještě vyžaduje důkazy pro konkrétní projekt,
vysvětluje [pokrytí a omezení](guides/coverage.md).

## Čtěte podle potřeby

Průvodci architekturou a hostingem pomohou zvolit podobu systému. Odolnost, data, bezpečnost a frontend vysvětlují kontrakty uvnitř této podoby. GitHub, kvalita a agenti řídí dodávání změn. Provoz a údržba udržují zdravé produkty i tuto knihovnu.

Při ověřování začněte [výběrem testů](guides/testing-strategy.md). Rozlišuje účel, úroveň a znalosti dostupné testujícímu; black-box neznamená pouze penetrační testování. [Výkonnostní testování](guides/performance-testing.md) použijte pro experimenty s běžnou zátěží, přetížením, náhlými špičkami, dlouhodobým zatížením a kapacitou; [bezpečnostní testování](guides/security-testing.md) pro kontroly podle rizik a ohraničené posuzování. Každý průvodce dává agentům kritéria výběru, požadavky na důkazy a podmínky zastavení.

Každý průvodce uvádí použitelný kontext, rozhodnutí, kompromisy, kontroly a signály ke změně. Načtení zdroje dokládá dostupnost, nikoli správnost doporučení. Toto první vydání obsahuje navržená doporučení čekající na lidské posouzení; překlady také vyžadují redakční kontrolu. Experimentální integrace prohlížeče zůstávají výslovně experimentální.

Nabídkou jazyků přepnete jazyk, vyhledáváním najdete pojem a souvisejícími průvodci budete sledovat důsledky. Pro čtení offline naklonujte repozitář; web a MCP adaptér pouze pro čtení používají stejný obsah. Ke čtení, sestavení ani validaci knihovny nepotřebujete placené API modelu.

## Související rozhodnutí

[Principy rozhodování](guides/foundations.md) · [Úplný životní cyklus projektu](guides/lifecycle.md) · [Volba a propojení architektur](guides/architecture.md) · [Zavedení knihovny v projektu](guides/adoption.md)

## Primární zdroje


[plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
