---
{
  "id": "architecture",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Volba a propojení architektur

## Rozhodujte podle omezení a odpovědnosti

Zaznamenejte hranice transakcí, požadavky na latenci a obnovu, citlivost dat, charakter zátěže a osoby schopné systém provozovat. Porovnejte nejjednodušší životaschopný návrh s navrženou alternativou. Následující tabulka je původní rozhodovací rámec této knihovny; citované popisy vzorů dokládají příslušné mechanismy a kompromisy, nikoli univerzální pořadí řešení.

| Přístup | Vhodná výchozí podmínka | Náklady a důvod k přehodnocení |
| --- | --- | --- |
| Statický web | Veřejný obsah bez důvěryhodných serverových zápisů | Limity sestavení a cache; pro autentizované změny přidejte chráněné API |
| Modulární monolit | Jeden produkt potřebuje koordinované transakce a časté změny | Disciplína závislostí mezi moduly; oddělujte pouze změřené omezení nebo samostatně vlastněnou schopnost |
| Funkce | Ohraničená nárazová práce odpovídá podmínkám běhu poskytovatele | Studené starty, kvóty, tlak na počet spojení a opakování; přehodnoťte soustavnou nebo dlouhotrvající práci |
| Služby | Samostatná odpovědnost, vydávání nebo izolace selhání přinášejí konkrétní užitek | Síťová selhání, verzované kontrakty rozhraní, pozorovatelnost a provozní zajištění konzistence |
| Událostní zpracování | Práce může skončit později a odběratelé mají odlišné odpovědnosti | Duplicity, doručení mimo pořadí, zpoždění, opětovné přehrání a vývoj schémat |
| Odolná workflow | Dlouhotrvající obchodní kroky musejí přežít přerušení | Omezení enginu, uchování historie, aktualizace kódu a porovnání vnějších účinků |

Tyto volby lze kombinovat. Monolit může obsluhovat statický frontend a využívat frontu, aniž by se stal mikroslužbovým systémem. Směr závislostí v kódu a topologie nasazení jsou samostatná rozhodnutí: rozdělení procesů samo nevytvoří užitečné doménové hranice.

CQRS odděluje model čtení a zápisu; může začít uvnitř jedné databáze. Samostatná úložiště přidávají zpoždění synchronizace a dohodu o zastaralém čtení. Event sourcing určuje historii událostí jako autoritativní zdroj, což vyžaduje rozhodnutí o vývoji událostí, přehrávání, soukromí a retenci. Samotná fronta nebo auditní tabulka není event sourcing. Tyto vzory zavádějte výběrově, když jejich konkrétní přínos převýší dodatečné požadavky na obnovu a testování.

## Umožněte posouzení hranic

U každého propojení prohlížeče, API, workeru, úložiště a poskytovatele zaznamenejte:

| Kontrakt | Důkaz, který má posuzovatel vidět |
| --- | --- |
| Oprávnění | Která identita smí provést kterou akci a nad čími daty |
| Vlastnictví dat | Která komponenta smí měnit každý invariant a jak ostatní žádají o změnu |
| Selhání | Timeout, zrušení, odpovědnost za opakování, zacházení s duplicitami a uživatelsky viditelný čekající nebo chybový stav |
| Kompatibilita | Podporovaní producenti a spotřebitelé, verze schématu a podmínka odstranění |
| Provoz | Traces a metriky, odpovědnost za podporu, postup obnovy a porovnání stavu, rozpočet |

Sdílená databáze může být záměrnou přechodnou volbou. Neomezené zápisy z více služeb komplikují samostatnou odpovědnost i migraci; tuto vazbu zdokumentujte místo označování služeb za nezávislé.

## Prokažte změnu před oddělením komponenty

Před návrhem workeru nebo služby nejprve určete příznak: stáří fronty, soupeření o zámky, koordinaci nasazení nebo požadavek na izolaci. Zaznamenejte reprezentativní výchozí měření a porovnejte malý úplný průchod navrženým řešením se stávající cestou. Na nové hranici použijte [kontraktní a black-box kontroly](testing-strategy.md), [zátěžové testy a testy obnovy](performance-testing.md) a [bezpečnostní testy](security-testing.md). Zahrňte pomalou závislost, starého spotřebitele a opakovaný požadavek.

Plán migrace určuje vlastnictví dat během přechodu, výběr provozu, kompatibilitu a porovnání výsledného stavu. Zachovejte jediného autoritativního zapisovatele, pokud nebyl ověřen záměrný návrh řešení konfliktů. Určete důkazy umožňující přesun provozu, podmínku přerušení a postup obnovy po nových zápisech. Vrácení provozu samo nevrátí migrovaná data.

Pokud se přínos neprokáže, zachovejte jednodušší topologii a užitečnou vnitřní hranici. Výsledek zapište do ADR, aby další agent neopakoval nepodložený redesign.

## Související rozhodnutí

[Odolnost a distribuovaná práce](durability.md) · [Architektura frontendu](frontend.md) · [Škálování podle měření](scaling.md) · [Hosting](hosting.md) · [Strategie testování](testing-strategy.md)

## Primární zdroje

[azure-architecture-styles](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/guide/architecture-styles/index.md) · [azure-cqrs](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cqrs.md) · [azure-event-sourcing](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/event-sourcing.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/e8ee627110a98501103827745aab18aedf312dd0/README.md)
