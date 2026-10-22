---
{
  "id": "testing-strategy",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Strategie testování

## Popište test na třech nezávislých osách

Agent má uvést, co o systému ví, kterou hranici zkouší a jaké selhání hledá. Jde o odlišné volby. Black-box test může ověřovat běžnou funkčnost, výkon i bezpečnost; tento pojem neznamená penetrační testování.

| Osa | Možnosti | Co volba sděluje posuzovateli |
| --- | --- | --- |
| Dostupné znalosti | Black box: pozorovatelná rozhraní; gray box: vybrané vnitřní informace nebo instrumentace; white box: kód a vnitřní cesty | Které informace ovlivnily návrh testu a která slepá místa zůstávají |
| Testovaná hranice | Jednotkový test, integrace, kontrakt spotřebitele a poskytovatele, úplný průchod end-to-end | Jak velká část skutečného systému se účastní a kde lze selhání lokalizovat |
| Cíl | Funkční správnost, bezpečnost, výkon, obnova, přístupnost, kompatibilita | Které riziko výsledek pokrývá; úspěch v jednom cíli nedokazuje jiný |

Například black-box test API může ověřit, že dva totožné požadavky na nákup vrátí jediný obchodní výsledek. White-box jednotkový test může projít každou větev opakování. Gray-box integrační test může navíc prohlédnout transakci a outbox. Poskytují doplňující se důkazy. Pokud tým chápe „integraci“ nebo „kontrakt“ odlišně, zdokumentujte místní terminologii.

## Vybírejte podle změny a jejích důsledků

Následující matice je doporučené výchozí pravidlo této knihovny, nikoli univerzální povinná testovací sada. Kontroly přidávejte nebo odebírejte s výslovným zdůvodněním rizika.

| Změna nebo riziko | Užitečné první kontroly | Rozšíření a důkazy přijetí |
| --- | --- | --- |
| Dokumentace nebo překlad | Význam, terminologie, odkazy, shoda jazykových verzí | Při změně rozvržení nebo navigace vykreslete změněnou podobu; neškodná slovní úprava nepotřebuje novou sadu běhových testů |
| Obchodní výpočet nebo změna stavu | Jednotkové příklady, hranice, neplatné vstupy; property-based případy pro skutečné invarianty | Ukažte, že porušující vstup selže; pokud ke správnosti patří persistence nebo vnější stav, přidejte integraci |
| Databázové schéma nebo transakce | Integrace se skutečnou databází, omezení, souběžnost, kompatibilita migrace | Reprezentativní objem dat, zámky, restart a pokračování i obnova; podporovaní starší spotřebitelé zůstávají kompatibilní |
| Schéma API nebo události | Kontraktní příklady producenta a spotřebitele, kontroly kompatibility | Skutečná serializace a přenosová cesta; neplatné vstupy odmítejte bez nežádoucích účinků |
| Uživatelský průchod nebo stav frontendu | Kontroly komponent a malý průchod prohlížečem pomocí veřejně pozorovatelného chování | Načítání, prázdný stav, chyba, zrušení, klávesnice a úzké zobrazení; ověřte skutečné události prohlížeče |
| Autentizace, oprávnění, rozsah tenanta | Testy pravidel a neoprávněný přístup k API a objektům s odlišnými identitami | Posuďte netestované vstupy a proveďte cílené bezpečnostní testy; zamítnutý požadavek nesmí odhalit chráněná data ani vyvolat vedlejší účinek |
| Worker, platba nebo odolné workflow | Integrační případy duplicit, změněného pořadí, timeoutů a pádů na trvalých hranicích | Po opakování či restartu porovnejte zamýšlené účinky; podle potřeby ověřte kompatibilitu v sandboxu poskytovatele |
| Souběžnost, cache, plánování, kapacita | Funkční kontroly při souběhu a změřený výchozí stav | Podle výkonnostního průvodce zvolte zátěžové, stresové, nárazové nebo dlouhodobé testy; zachovejte správnost a časově ohraničenou obnovu |
| Model, prompt, retrieval, nástroj nebo pravidlo agenta | Verzované evaluace úkolů, útočné případy, deterministické testy pravidel | Porovnejte s vyhrazenými evaluačními případy, prohlédněte skutečné účinky nástrojů, opakujte stochastické případy a uveďte variabilitu |

## Plánujte před výběrem nástroje

Sepište krátké zadání testu: dotčený požadavek; hypotézu selhání; model znalostí, hranici a cíl; testovací podklady a prostředí; očekávané výsledky; bezpečné limity vykonání; a důkazy k uchování. Nástroj vybírejte podle zadání. Ovladač prohlížeče, HTTP klient, generátor vlastností, generátor zátěže, skener a lidské review pozorují odlišné věci.

Použijte nejmenší hranici, která odhalí chybu, a přidejte realistickou kontrolu hranice tam, kde by náhrady mohly problém skrýt. Mock databáze neprokáže databázové omezení unikátnosti a mock události prohlížeče neprokáže nativní podporu prohlížeče. V deterministických testech mějte poskytovatele pod kontrolou; kompatibilitní test v sandboxu označte odděleně od simulované odpovědi.

Testovací podklady musí být nezávislé a opakovatelné. Řiďte relevantní hodiny a náhodnost, zapisujte počáteční hodnoty generátorů (seedy) a izolujte účty, tenanty, stav i úklid. Mezi paralelními běhy nesdílejte měnitelný testovací účet, pokud právě tento souběh není předmětem testu. Podklady a traces chraňte jako data; nekopírujte produkční záznamy jen pro větší realističnost testu.

## Kontroly musí umět vyvrátit splnění požadavku

Kontrolujte výstupy, uložený stav a zakázané účinky relevantní pro požadavek. Samotný úspěšný HTTP kód nedokazuje vrácení správného objektu. Test autorizace má projít povolenou i zamítnutou akcí a potom ověřit, že odmítnutí nezměnilo chráněný stav.

U závažné opravy prokažte, že test odhalí původní chybu nebo záměrně porušenou místní variantu. Kde je to vhodné, používejte hraniční hodnoty a příklady tříd ekvivalence. Property-based testy zkoumají definovaný invariant; stále závisejí na správném invariantu a modelu vstupů. Pokrytí může ukázat neprošlý kód, ale vysoké pokrytí neprokazuje správnost požadavků ani úplnost bezpečnostních hranic.

## Rozhodněte, kdy je důkazů dost

Dotčené vydání zastavte, pokud selžou povinné kontroly, cíl leží mimo schválený rozsah, testovací data opustí svou hranici nebo závažnému tvrzení chybí důkazy. Uveďte vynechané kroky a nejistotu. Člověk může přijmout zdokumentované, časově omezené zbytkové riziko; agent nesmí nespuštěnou kontrolu označit za úspěšnou.

Dokončení znamená, že dohodnuté chování podporují interpretovatelné výsledky, známá omezení a plán obnovy. Uchovejte testovanou revizi, konfiguraci, verzi podkladů, příkazy, výsledky a příslušné traces s odstraněnými citlivými hodnotami. Další testování přidejte, když ho odůvodní nová hypotéza selhání, místo nekonečného opakování stejné zelené sady.

## Důkazy a související rozhodnutí

Model tří os a výběrová matice jsou původní místní syntéza. OWASP podporuje testování autorizace na více hranicích; Playwright podporuje izolované testy prohlížeče podle viditelného chování; PostgreSQL popisuje vlastnosti souběžnosti, které mají ověřovat testy skutečné databáze. Tyto zdroje necertifikují každou buňku matice.

[Kontroly kvality](quality.md) · [Výkonnostní a zátěžové testování](performance-testing.md) · [Bezpečnostní testování](security-testing.md) · [Data a migrace](data.md) · [Odolnost](durability.md)

## Primární zdroje

[owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [owasp-multi-tenant](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.md)
