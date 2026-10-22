---
{
  "id": "playbook-saas",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Dodání SaaS s oddělenými tenanty

## Vhodnost a počáteční architektura

Tento profil použijte, když nezávislé zákaznické organizace sdílejí aplikaci a infrastrukturu. Zachyťte izolaci tenantů, význam účtování, umístění dat, cíle obnovy, podobu špičkové zátěže a vlastníka zákaznické podpory. Navrženým východiskem je modulární aplikace, relační databáze a ohraničený worker na pozadí. I jedno nasazení může vynucovat oddělené moduly členství, obchodních záznamů, účtování a doručování. Tato příručka vytvořená agentem je vlastní syntézou čekající na přijetí člověkem.

Databáze na jediném hostiteli se může hodit pro izolovaný prototyp s přijatými omezeními dostupnosti. Spravovaný relační hosting je alternativou, pokud jej vyžaduje obnova, souběžné zápisy a provozní podpora. Samostatné databáze tenantů mohou splnit izolaci nebo umístění dat, zvyšují však cenu migrací a podpory. Před přidáním replik, oddílů nebo služeb měřte latenci dotazů, čekání na zámky, stáří fronty a vzájemné rušení tenantů. Modul oddělte pouze s nezávislým kontraktem, vlastníkem a měřitelným přínosem; počet tenantů není architektonický práh.

## Zachyťte invarianty v repozitáři

Používejte hranice jako `domain/`, `api/`, `persistence/`, `billing/`, `workers/`, `contracts/` a `ops/`. Oprávněné členství v tenantu určuje autentizovaný subjekt; selektor tenantu dodaný klientem nikdy nezakládá oprávnění. Každé čtení, změna, export, pohled v cache i úloha ve frontě nese ověřený kontext tenantu. Převzetí identity podporou musí být explicitní a auditované.

Specifikujte identitu záznamu, jedinečnost v rámci tenantu, měnu a jednotky, přechody stavů, stránkování, chyby a uchovávání. U opakovaného příkazu svažte idempotentní klíč s tenantem, druhem operace a kanonickým otiskem požadavku. Opětovné použití klíče s jiným vstupem musí vyvolat konflikt. Obchodní změnu, uloženou odpověď a záznam outboxu potvrďte atomicky, pokud sdílejí databázi. Relay může doručit dvakrát; jeho konzument nebo kontrakt poskytovatele musí zabránit opakovaným obchodním účinkům. Lokální transakce nemůže učinit vzdálenou platbu atomickou.

## Pořadí agentů a artefaktů

1. Průzkumná role vytvoří matici subjekt/akce/objekt, obchodní invarianty, rozsah zátěže a případy nejistého účtování. Lidský vlastník přijme rozhodnutí o obnově a finančním riziku.
2. Implementátor dodá jeden svislý průřez: autentizovaný příkaz, transakci omezenou na tenant, trvalý stav a opakovatelnou cestu workeru. Do ADR zaznamená alternativy úložiště a tenancy a dodá kompatibilní migraci.
3. Ověřovatel testuje HTTP společně s perzistencí a následně napadá hranice tenantů, souběh, přerušení a obnovu. Role vydání připraví omezené nasazení a postup sjednocení stavů; přijetí do produkce řídí lidská kontrola.

Balíček obsahuje profil, ADR, schéma API, autorizační matici, pořadí migrace, příklady evidence operací a outboxu, pozorované výsledky testů, zprávu o obnově, pokyny ke sjednocení s poskytovatelem, odhad nákladů a jmenované vlastníky služby a dat. `examples/durable_service` je lokální reference k prozkoumání a úpravě. Její přítomnost nedokládá autentizaci, účtování poskytovatele, vysokou dostupnost ani cíle obnovy tohoto projektu.

## Testujte obchodní výsledky včetně zakázaných

Jednotkové testy použijte pro peněžní a stavová pravidla, kontraktní pro konzumenty a integrační se skutečně zvolenou databází pro izolaci a atomicitu. Výsledek SQLite nedokládá chování zámků ani izolace PostgreSQL. U dvou syntetických tenantů zaměňujte identifikátory ve čtení, zápisech, exportech a datech workerů. Orákulem je nepřítomnost neoprávněných dat v odpovědi a nezměněný stav cizího tenantu, nikoli pouze zamítavý HTTP kód.

Současně odešlete kopie příkazu a znovu použijte jeho klíč s jinou částkou. Zkontrolujte záznamy, uložené odpovědi a účinky: zůstává jedna zamýšlená obchodní operace a nesouhlasné opakování selže. Vyvolejte pád před commitem lokální databázové transakce, po jejím commitu a po úspěchu poskytovatele, ale před přijetím jeho odpovědi. Poslední případ musí vést k bezpečnému opakování podle zdokumentované záruky poskytovatele nebo k viditelnému stavu pro sjednocení, nikdy ke slepé druhé platbě. Obnovte izolovanou zálohu, porovnejte obchodní invarianty a sjednoťte záznamy poskytovatele před obnovením doručování. Zachovejte neúspěšné a neprovedené případy.

Zátěžové testy mají reprodukovat drahé dotazy, nerovnoměrné tenanty, souběžné zápisy a omezené zpracování nahromaděné práce. Před spuštěním dohodněte cíle latence, chyb a fronty i limity přerušení. Zahrňte testy prohlížeče pro zamítnuté, čekající a nejednoznačné výsledky, aby uživatelé nebyli vedeni k opakování nejisté platby.

## Nasazení a provoz přes datovou hranici

Nejprve rozšiřte schéma, nasaďte kompatibilní čtečky a zapisovače, doplňujte data v obnovitelných dávkách, sjednoťte je a starou reprezentaci odstraňte až po skončení období kompatibility. Přerušte při dohodnutých prazích chyb, čekání na zámky či nesrovnalostí. Návrat aplikačního kódu neobnoví smazaná data ani nevrátí platbu. Uchovejte předchozí artefakt, zálohy, checkpointy migrace a plán dopředné opravy nebo izolované obnovy.

Sledujte zamítnuté autorizace, selhání transakcí, stáří fronty, pokusy o doručení, nesrovnalosti účtování a aktuálnost obnovy pomocí korelačních ID šetrných k soukromí. Rozpočtujte databázovou kapacitu, zálohy, poplatky poskytovatele, přenos a provozní práci na užitečný obchodní výsledek. Určete oprávnění při incidentu pozastavit účtování a workery odděleně. Mezi produkční mezery patří životní cyklus identit, správa klíčů, platební kontrakty, ukončení tenantů, nácvik obnovy a pohotovost. Při ukončení zastavte nové zápisy, vyřešte čekající externí účinky, exportujte oprávněná zákaznická data, dodržte pravidla uchovávání a mazání a odeberte integrace bez zničení požadovaných finančních důkazů.

## Navazující rozhodnutí

[Data a migrace](data.md) · [Odolnost](durability.md) · [Bezpečnostní testování](security-testing.md) · [Škálování](scaling.md)

## Primární zdroje

[owasp-multi-tenant](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [azure-outbox](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/databases/guide/transactional-out-box-cosmos.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md)
