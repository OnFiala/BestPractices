---
{
  "id": "scaling",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Škálování podle měření

## Popisujte práci, nikoli počet účtů

Zaznamenejte špičkovou rychlost příchodu práce, souběžné zpracování, velikost vstupů, poměr čtení a zápisů, nejzatíženější tenanty nebo klíče, růst dat, úlohy na pozadí a kvóty závislostí. Před volbou kapacity určete uživatelský průchod, cíl služby, nákladový rámec a potřebnou rezervu při selhání. Milion převážně neaktivních účtů může být snazší obsloužit než několik nákladných souběžných úloh.

Následující pořadí změn je doporučení této knihovny, nikoli záruka, že každá zátěž má projít všemi kroky. Měření a zamítnuté alternativy uchovávejte v ADR.

## Měňte vždy jedno omezení

| Pozorované omezení | Kandidátní změna | Důkaz a kompromis |
| --- | --- | --- |
| Pomalé dotazy nebo příliš mnoho síťových volání | Profilujte, doplňte indexy, omezte velikosti výsledků a opatrně dávkujte | Na reprezentativních datech porovnejte plány dotazů, latenci a náklady zápisů |
| Opakované nákladné čtení | Cache s výslovnými klíči tenantů a pravidly čerstvosti | Ověřte studený start, invalidaci a souběžné nenalezení v cache; měřte zatížení původního zdroje |
| Práce přichází rychleji, než ji lze dokončit | Omezené fronty a workery, kvóty a řízení přijímání práce | Kontrolujte stáří fronty, spravedlivé sdílení a obnovu; před vyčerpáním zdrojů předvídatelně odmítejte |
| Je saturován procesor aplikace nebo nezávislé I/O | Přidejte bezstavové repliky | Přepočítejte celkový počet databázových spojení a rychlost požadavků do závislostí |
| Převažuje čtení | Replika nebo projekce pro dotazy | Určete zpoždění a chování čtení po zápisu; testujte zastaralé i nedostupné čtení |
| Přetrvává změřený limit úložiště, zápisů nebo směrování | Rozdělte data nebo izolujte část zátěže | Prokažte směrování, chování zatížených klíčů, vyvažování, migraci a význam operací přes více oddílů |

Nepředpokládejte, že cache zajistí bezpečnou autorizaci: vymezte klíče a správně invalidujte oprávnění. Vlna nenalezených položek může přetížit původní zdroj. Přidání aplikačních replik může zhoršit výpadek databáze, pokud každá replika otevře velký pool spojení nebo opakuje stejnou práci.

## Experiment určete před generováním provozu

Pomocí [průvodce výkonnostním testováním](performance-testing.md) rozlište výchozí zátěž, náraz, stresový test, dlouhodobou zátěž a experiment obnovy. Určete cílové prostředí, oprávnění k testu, syntetická data, rozložení provozu, podmínky zastavení a cenový limit. Kromě běžné cesty testujte zamítnuté i nákladné operace. Uchovejte výsledky jednotlivých požadavků, metriky zdrojů, stáří fronty a verzovaný popis zátěže.

Odděleně měřte úspěšnou propustnost, latenci p95/p99, chyby a odmítnutou práci. Systém, který vykazuje skvělou latenci jen díky zahození většiny požadavků, nesplnil cíl. Zahrňte jednu pomalou závislost a sledujte, zda nevyčerpá veškerou souběžnost nebo nevyvolá násobení opakovaných pokusů. Po snížení provozu potvrďte vyprázdnění front a návrat k cílům služby bez ručního restartu.

Pro hrubou kontrolu ve stabilním systému platí, že průměrný počet rozpracovaných operací je průměrná rychlost příchodů vynásobená průměrnou dobou pobytu uvnitř téže měřené hranice. Nejde o odhad krajních latencí ani příslib kapacity; přetížená rostoucí fronta porušuje předpoklad ustáleného stavu. Každý odhad ověřte se skutečným rozložením a způsobem selhání.

## Rozhodněte a připravte cestu zpět

Škálujte, když trvalé měření nebo zdůvodněná předpověď ohrožuje dohodnutý cíl či rezervu při selhání. Zaznamenejte spouštěč, očekávaný přínos, provozní náklad, vlastníka změny a plán návratu nebo dopředné opravy. Autoscaling potřebuje horní meze, započítanou dobu startu, kapacitu závislostí a řízení rozpočtu. Neopraví neefektivní transakci ani nezaručí dostupnost.

Zápisy ve více regionech a sharding přidávají rozhodnutí o směrování a konzistenci. Zavádějte je až po ověření převzetí při selhání, konfliktů či porovnání stavu a migrace na reprezentativních datech. Níže uvedený zdroj o dělení dat u konkrétního poskytovatele tyto povinnosti ilustruje; limity jeho produktu nejsou univerzálními limity jiné databáze.

## Související rozhodnutí

[Výkonnostní testování](performance-testing.md) · [Hosting](hosting.md) · [Data](data.md) · [Provoz](operations.md) · [Architektura](architecture.md)

## Primární zdroje

[observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [azure-cache-aside](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cache-aside-content.md) · [azure-data-partitioning](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/best-practices/data-partitioning-strategies-content.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml)
