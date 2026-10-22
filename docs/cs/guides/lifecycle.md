---
{
  "id": "lifecycle",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Celý životní cyklus projektu

## Etapy a podmínky dokončení

| Etapa | Potřebný podklad | Důkaz dokončení |
| --- | --- | --- |
| Objevování | Zadání problému, mapa účastníků a dat | Měřitelný přínos a výslovně vyloučené cíle |
| Návrh | Profil, kontextový diagram, ADR, model hrozeb | Člověkem přijatá omezení a cíle obnovy |
| Plán | Malý backlog, závislosti, příklady přijetí | Vlastník, rozsah, testy a podmínky zastavení každého úkolu |
| Stavba | Kód, migrace, testy, vysvětlení | Opakovatelné kontroly a přehledný diff |
| Vydání | Verze, poznámky, nasazení a návrat | Smoke test, připravená obnova, schválení |
| Provoz | Runbook, přehledy, odpovědnost za podporu a cenu | Měřené cíle služby a vyzkoušená obnova |
| Vývoj | Poučení z incidentů, deprecace a migrace | Přechod spotřebitelů před odstraněním |
| Ukončení | Export/smazání dat a odebrání přístupů | Splněná retence; ukončené platby a přístupy |

Stejné brány mají různou hloubku. Osobní skript může mít jeden krátký dokument; závažný systém potřebuje nezávislejší důkazy. Nevytvářejte dokumenty pro dokumenty: každý musí pomáhat rozhodnutí nebo provoznímu zásahu.

## Dohoda člověka a agenta

Člověk určuje hodnotu, priority, toleranci rizika a oprávnění vydat změnu. Agent zkoumá, navrhuje, implementuje, testuje a uvádí nejistoty. Úkol končí důkazy, ne prohlášením hotovo. Předpoklady patří do repozitáře, ne pouze do historie chatu.

## Ověření a změna směru

Před rozšiřováním funkcí předveďte jeden úplný uživatelský průchod včetně chyb, odmítnutého přístupu, prázdného stavu a obnovy. Neměřitelný přínos vraťte do objevování. Příliš drahý provoz nebo chybějící kapacitu řešte zjednodušením návrhu. Ukončení plánujte od začátku: uživatel musí mít cestu ven i ke svým datům.

## Související rozhodnutí

[Kontroly kvality dokazující chování](quality.md) · [Zdraví, obnova a náklady](operations.md) · [Člověk řídí, agent vykonává](agents.md) · [Použití knihovny v projektu](adoption.md)

## Primární zdroje

[github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml)
