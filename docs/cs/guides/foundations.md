---
{
  "id": "foundations",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Principy rozhodování

## Kontext a výchozí přístup

Trvanlivá architektura umožňuje přežít změny, selhání i ztrátu znalostí jednotlivce. Neslibuje věčný technologický stack. Začněte jasnými hranicemi, malým počtem závislostí a vlastníkem každé provozní povinnosti. Upřednostněte vratná rozhodnutí, dokud nemáte důvod k většímu závazku.

## Profily projektů

| Profil | Výchozí řešení | Povinnosti |
| --- | --- | --- |
| Osobní nebo průzkumný | Statický web nebo jeden proces, případně spravované úložiště | Opakovatelný setup, ochrana tajemství, export a obnova |
| Produkt s uživateli | Modulární aplikace, spravovaná databáze, worker podle potřeby | Cíle služby, test obnovy, návrat nasazení, odpovědnost za podporu |
| Velký provoz nebo více týmů | Rozdělení podle měření, explicitní smlouvy, kapacitní plán | Pohotovost, zátěžové testy, izolace a migrace |
| Vysoké důsledky | Jakékoli měřítko včetně jednoho uživatele | Model hrozeb, audit, retence, právní a oborová kontrola |

Profily popisují omezení, nikoli soutěž vyspělosti. Malá regulovaná služba může potřebovat silnější kontroly než rozsáhlý veřejný katalog. Zapište odložené kroky a signál, který je vyvolá.

## Záznam rozhodnutí

Každá zásadní volba má problém, omezení, alternativy, důkazy, vlastníka, náklady, ověření a cestu ven. Oddělte fakta od předpokladů a místní pravidla od externích standardů. Určete termín přezkoumání i pozorovatelný spouštěč, například dlouhodobě překročené stáří fronty.

## Ověření a změna

Nový přispěvatel musí zopakovat vývojové prostředí, dohledat cestu uživatelské akce k datům a obnovit neúspěšné nasazení. Pokud systému rozumí pouze původní autor nebo jedno modelové sezení, nejprve zlepšete dokumentaci a hranice. Rozhodnutí přezkoumávejte po incidentech, změnách nákladů, směru produktu či právních povinností.

## Související rozhodnutí

[Volba a propojení architektur](architecture.md) · [Škálování podle měření](scaling.md) · [Správa a otevřená rozhodnutí](governance.md)

## Primární zdroje

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md)
