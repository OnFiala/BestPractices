---
{
  "id": "data",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Data, kontrakty a migrace

## Volte úložiště podle invariantů

Před výběrem technologie definujte způsoby přístupu, konzistenci, uchovávání, umístění dat a potřeby obnovy. Relační databáze je silným kandidátem pro transakční obchodní záznamy; objektové úložiště často vyhovuje velkým binárním objektům. Vyhledávací indexy a cache jsou odvozená data, pokud je systém výslovně neurčí jako autoritativní. Tyto výchozí volby jsou doporučeními knihovny, nikoli univerzálními příkazy.

Každému záznamu určete stabilní identitu a vlastníka. Vymezte unikátnost, pořadí a povolené přechody stavů včetně odstranění a obnovy. Kritické invarianty vynucujte pomocí omezení a transakcí, které databáze podporuje; samotné aplikační kontroly mohou podléhat souběhu. Rozumějte nasazené úrovni izolace a podle potřeby bezpečně opakujte celou dotčenou transakci místo opakování její libovolné části.

Identita tenanta musí pocházet z důvěryhodného autorizačního kontextu a provázet čtení, zápisy, exporty i zpracování na pozadí. Vedle hlavních tabulek prověřte i odvozené pohledy, analytiku, logy a zálohy. Pravidla uchovávání a mazání musí zahrnovat i tyto kopie; odstranění viditelného řádku nedokládá odstranění všech kopií.

## Rozšíření, migrace, odstranění staré podoby

| Fáze | Potřebné rozhodnutí a důkaz |
| --- | --- |
| Rozšíření | Přidejte kompatibilní podobu; zdokumentujte chování hodnot null, výchozích hodnot a starých klientů |
| Přechod | Určete autoritativního zapisovatele a způsob, jak smíšené verze čtou a zapisují bez ztráty významu |
| Doplnění dat | Použijte ohraničenou, obnovitelnou práci s kontrolními body, řešením konfliktů a sledováním limitů prostředků a zámků |
| Kontrola shody | Porovnejte obchodní invarianty a reprezentativní záznamy, nikoli jen počty řádků |
| Přepnutí | Záměrně zvolte přepínaný provoz, sledujte chyby a zpoždění a udržujte podmínku přerušení |
| Odstranění staré podoby | Starou podobu odstraňte až po migraci všech podporovaných klientů a workerů a přípravě obnovy |

Dvojí zápis bez strategie konzistence může vytvořit dvě vzájemně rozporné pravdy. Návrat ke staré verzi kódu nevrátí destruktivní migraci. Rozhodněte, zda obnova znamená návrat zpět, opravu vpřed, nebo obnovení ze zálohy s následným sjednocením stavu, a nacvičte skutečný postup na syntetických datech odpovídajících produkci nebo na odpovídajícím způsobem chráněných datech.

## Testujte souběh a kompatibilitu

Před změnou schématu nebo veřejného kontraktu spusťte [integrační a kontraktní testy](testing-strategy.md) se starými i novými verzemi aplikace nad přechodovým schématem. Zahrňte souběžné aktualizace, duplicitní požadavky, přerušené doplňování dat, export následovaný importem a obnovené úlohy. Užitečný negativní případ nechá dva klienty soupeřit o stejný omezený prostředek a ověří zachování invariantu, nikoli jen to, že jeden požadavek vrátí chybu.

Pomocí [výkonnostního testování](performance-testing.md) sledujte zámky, zpoždění replikace, pooly připojení a délku migrace při reprezentativním objemu. Migrace úspěšná na deseti řádcích nedokládá chování na skutečné datové sadě. [Bezpečnostní testy](security-testing.md) musí zahrnovat identifikátory jiných tenantů, rozsah exportu a odebrání přístupu po obnovení indexů a cache.

Obnovujte do izolovaného prostředí, ověřte uživatelsky viditelné chování a před opětovným spuštěním zpracování sjednoťte stav s externími účinky. Změřte dobu obnovy a skutečnou ztrátu dat vůči dohodnutým RTO/RPO a zaznamenejte verze záloh a artefaktů. Replika může replikovat náhodné smazání; nenahrazuje otestovanou kopii určenou k obnově.

## Přehodnocujte model

Kontrakt verzujte, pokud se konzumenti musí koordinovat; nikdy potichu neměňte jednotky, přípustnost hodnoty null, identifikátory ani význam. Další databázi zaveďte jen pro změřený požadavek, který ospravedlní náklady na konzistenci, zálohování a potřebnou odbornost. Rozdělení dat do oddílů vyžaduje explicitní pravidla směrování, vlastnictví a operací napříč oddíly. Oddělené modely pro čtení mohou pomoci se změřeným požadavkem na dotazy, ale při asynchronních aktualizacích přidávají kontrakt aktuálnosti dat.

## Související rozhodnutí

[Odolnost](durability.md) · [Bezpečnost](security.md) · [Škálování](scaling.md) · [Strategie testování](testing-strategy.md) · [Výkonnostní testování](performance-testing.md)

## Primární zdroje


[postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [owasp](https://raw.githubusercontent.com/OWASP/ASVS/2b47a9dd16760ee484a6672d197f1f7e25d9c632/README.md) · [azure-cqrs](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cqrs.md) · [azure-data-partitioning](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/best-practices/data-partitioning-strategies-content.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md) · [azure-outbox](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/databases/guide/transactional-out-box-cosmos.md)
