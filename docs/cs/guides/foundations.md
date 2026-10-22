---
{
  "id": "foundations",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Principy rozhodování

## Kontext a výchozí přístup

Odolná architektura znamená, že lze přežít změnu, selhání i ztrátu znalostí jednotlivce. Neslibuje, že jedna technologická sestava vydrží navždy. Začněte explicitními hranicemi, malým rozsahem závislostí a vlastníkem každé provozní povinnosti. Upřednostňujte vratná rozhodnutí, dokud silnější důkazy neodůvodní závazek.

## Profily projektů

| Profil | Výchozí řešení | Povinnosti |
| --- | --- | --- |
| Osobní nebo průzkumný | Statický web nebo jeden proces, podle potřeby spravované úložiště | Reprodukovatelné nastavení, bezpečná správa tajných údajů, export a obnova |
| Produkt se skutečnými uživateli | Modulární aplikace, spravovaná databáze, podle potřeby worker na pozadí | Cíle služby, test obnovy, návrat nasazení a odpovědná osoba pro podporu |
| Velký provoz nebo mnoho týmů | Rozdělení podle měření, explicitní kontrakty, plánování kapacity | Pohotovostní pokrytí, zátěžové testy, plány izolace a migrace |
| Závažné důsledky | Libovolná velikost včetně jediného uživatele | Model hrozeb, auditovatelnost, uchovávání dat, právní a doménové posouzení |

Profily popisují omezení, nikoli soutěž ve vyspělosti. Malá regulovaná služba může potřebovat silnější opatření než velký veřejný katalog. Zaznamenejte, co záměrně odkládáte a jaký signál si vynutí jeho doplnění.

## Záznam rozhodnutí

Každá významná volba pojmenuje problém, omezení, možnosti, důkazy, vlastníka, očekávané náklady, ověření a cestu ven. Oddělujte fakta od předpokladů a místní pravidla od externích standardů. Stanovte datum posouzení a pozorovatelný spouštěč, například soustavné překračování dohodnutého cíle stáří fronty.

## Ověřujte a přehodnocujte

Nový přispěvatel musí být schopen zopakovat vývojový postup, sledovat uživatelskou akci až k jejím datům a zotavit se z neúspěšného vydání. Pokud systém dokáže vysvětlit pouze původní autor nebo relace modelu, zlepšete dokumentaci a hranice před přidáním dalších komponent. Rozhodnutí přehodnocujte po incidentech, významných změnách nákladů, změnách směru produktu nebo právních povinností.

## Související rozhodnutí

[Volba a propojení architektur](architecture.md) · [Škálování podle měření](scaling.md) · [Správa a nezodpovězená rozhodnutí](governance.md)

## Primární zdroje


[owasp](https://raw.githubusercontent.com/OWASP/ASVS/2b47a9dd16760ee484a6672d197f1f7e25d9c632/README.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md)
