---
{
  "id": "lifecycle",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Úplný životní cyklus projektu

## Do další fáze postupujte na základě důkazů

Následující fáze tvoří navrhovaný provozní model této knihovny. Jejich hloubka se mění podle dopadu a odpovědnosti; jejich názvy nejsou externí certifikací. Osobní skript může vystačit s jedním stručným záznamem, zatímco služba se závažnými důsledky potřebuje nezávislé důkazy z domény a bezpečnosti.

| Fáze | Požadovaný artefakt | Důkaz pro uzavření fáze |
| --- | --- | --- |
| Průzkum | Vymezení problému, mapa zainteresovaných stran a dat | Měřitelný uživatelský výsledek, výslovně vyloučené cíle a odpovědný vlastník |
| Návrh | Profil projektu, kontextový diagram, ADR a model hrozeb | Člověk přijal omezení, rozpočet a cíle obnovy |
| Plánování | Malý backlog a plán testování | Každý úkol má rozsah, vlastníka, chybové případy a podmínky zastavení |
| Tvorba | Kód, migrace, testy a aktualizované vysvětlení | Reprodukovatelné kontroly a diff dostupný posuzovateli |
| Vydání | Verzovaný artefakt, plán zavedení a obnovy | Akceptace v předprodukčním prostředí, důkazy o migraci a obnově a lidské schválení |
| Provoz | Provozní příručka, měření služby a odpovědnost za náklady | Cíle se měří, upozornění vedou ke konkrétní reakci a obnova se procvičuje |
| Rozvoj | Poučení z incidentů a záznam migrací a vyřazování | Podporovaní konzumenti migrují před odstraněním funkcí |
| Ukončení | Plán exportu, mazání a odebrání přístupu | Splněné povinnosti uchovávání, uzavřené externí integrace a ověřené účtování |

Artefakt má své místo, pokud podporuje rozhodnutí nebo akci. Vygenerovaný dokument, který nikdo nedokáže použít, není důkazem připravenosti.

## Testování je průběžná činnost

Při průzkumu definujte, co by prokázalo nesplnění uživatelského výsledku. Při návrhu určete invarianty a hranice důvěry, které si zaslouží důkladnější testy. Než agent napíše kód, stanovte akceptační příklady a očekávané chování při selhání; pomocí [strategie testování](testing-strategy.md) zvolte nejmenší užitečnou sadu.

Při implementaci spouštějte cílené kontroly měněné hranice. Při integraci a vydání ověřujte kompatibilitu, zamítnuté akce a kritické uživatelské scénáře přes veřejná rozhraní. Před vydáním citlivým na kapacitu a plánovanými migracemi použijte [výkonnostní testování](performance-testing.md) s explicitními limity a oprávněním. [Bezpečnostní testování](security-testing.md) zařaďte při změnách identity, citlivosti dat, externích vstupů, závislostí nebo pravomoci nástrojů. Provoz do plánu vrací nácviky obnovy, regresní testy incidentů a pozorování skutečné zátěže.

Úspěšné sestavení neuzavírá nesplněné akceptační kritérium. Neúspěšné, přeskočené a nespuštěné kontroly zaznamenávejte odděleně a u nevyřešeného rizika určete odpovědnou osobu. Schválení se vztahuje k testovanému artefaktu a kontextu; pozdější významná změna vyžaduje nové posouzení.

## Odpovědnost člověka a agentů

Člověk volí hodnotu, priority, přijatelné riziko, směr architektury a pravomoc k vydání. Agenti zkoumají, navrhují, implementují, testují a hlásí nejistoty v rámci přidělených možností. Pokud to závažnost důsledků vyžaduje, oddělte implementaci od ověřování; několik agentů opakujících stejný předpoklad netvoří nezávislý důkaz.

Rozhodnutí, identifikátory běhů, verze artefaktů a informace k obnově uchovávejte v repozitáři, nikoli pouze v chatu. Ohraničený úkol končí skutečným výsledkem a nevyřešenými otázkami včetně důvodu odmítnutí navrženého řešení. Nikdy neoznačujte neprovedený test nebo vygenerovaný kontrolní seznam jako lidské schválení.

## Měňte směr a uzavřete systém

Před rozšiřováním funkcí předveďte jeden scénář napříč vrstvami včetně chyb a odepřeného přístupu. Pokud výsledek nelze měřit, vraťte se k průzkumu. Pokud odpovědnost nebo provozní náklady nejsou udržitelné, zjednodušte architekturu místo přidávání bezobslužné automatizace.

Ukončení plánujte již při vzniku: jak uživatelé vyexportují data, které záznamy musí zůstat zachovány a jak se odvolají přihlašovací údaje a delegovaný přístup agentů? Cestu exportu a uzavření otestujte dřív, než začne být naléhavá. Plánované úlohy, prostředky poskytovatelů a obnovovací kopie vyřaďte podle dohodnutých pravidel uchovávání; smazání aplikačního repozitáře není úplným vypnutím.

## Související rozhodnutí

[Strategie testování](testing-strategy.md) · [Kontroly kvality](quality.md) · [Provoz](operations.md) · [Agenti](agents.md) · [Zavedení](adoption.md)

## Primární zdroje


[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml)
