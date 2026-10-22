---
{
  "id": "security-testing",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Bezpečnostní testování

## Začněte hranicí, která může selhat

Bezpečnostní testování poskytuje důkazy o výslovné hrozbě a kontrole. Před výběrem skeneru určete aktéra, vstupní bod, chráněné aktivum, očekávané oprávnění a možný účinek. Odkazujte na použitelné požadavky konkrétní verze standardu, například ASVS, a definujte test, jehož výsledek může vyvrátit tvrzení, že kontrola funguje.

Black-box označuje testování přes pozorovatelná rozhraní bez použití vnitřních detailů implementace. Není synonymem bezpečnostního testování. Gray-box může využívat testovací přístupy, znalost schématu nebo telemetrii; white-box pracuje s kódem a konfigurací. Podle potřeby pohledy kombinujte: review kódu může najít chybějící filtr tenanta, zatímco požadavek od jiného tenanta prokáže, zda nasazená cesta odhaluje data.

## Vybírejte doplňující se techniky

| Technika | Vhodný spouštěč | Co sama neprokáže |
| --- | --- | --- |
| Analýza zdrojového kódu a cílené review | Nové parsery, dotazy, vykreslování, přístup k souborům či síti nebo privilegované cesty | Skutečnou provozní konfiguraci, úplnou obchodní autorizaci ani absenci všech zranitelností |
| Analýza závislostí a obrazů | Nové závislosti, změny lockfilu či obrazů nebo nové záznamy zranitelností | Zneužitelnost v tomto nasazení ani správnost vlastní aplikační logiky |
| Hledání tajných údajů | Změněné soubory, artefakty sestavení a relevantní historie | Odhalení každého uniklého přístupu ani to, že smazání souboru přístup zneplatní |
| Review infrastruktury a konfigurace | Změny sítě, IAM, úložišť, TLS, CI nebo nasazování | Shodu skutečného nasazení s navrženou konfigurací bez dalšího ověření |
| Dynamické skenování vlastněného testovacího nasazení | Změna webových/API rozhraní nebo konfigurace | Úplné řízení přístupu či bezpečnost složitých workflow; autentizované pokrytí může být neúplné |
| Ruční scénáře zneužití a cílené kontroly API/prohlížeče | Změny autentizace, oprávnění, tenantů, obnovy, obchodní logiky nebo nástrojů agentů | Široké pokrytí, pokud nejsou zaznamenány cesty, role a vynechané případy |
| Fuzzing nebo property-based kontroly hranic | Parsery, formáty souborů, protokoly nebo validace přijímají nedůvěryhodná data | Správnost mimo model vstupů ani platnost tvrzené bezpečnostní vlastnosti |

Vybírejte nástroje kompatibilní s jazykem, frameworkem, protokolem a zamýšleným rozsahem testu. Výsledek skeneru je kandidátní nález: před určením závažnosti prověřte dosažitelnost, předpoklady, dopad a reprodukci. Prázdný report znamená žádné nálezy při dané konfiguraci; není bezpečnostním certifikátem.

## Konkrétní kontroly běžných hranic

Pro autorizaci objektů vytvořte dva oddělené tenanty a více rolí. Pomocí identifikátorů mimo rozsah aktéra otestujte čtení, aktualizaci, mazání, seznamy, vyhledávání, export a asynchronní cesty. Zahrňte odpovědi z cache a změny oprávnění. Ověřte odmítnutí i nepřítomnost úniku nebo změny dat; pouhé změny UI nestačí.

U relací pokryjte odhlášení a revokaci, expiraci, změny oprávnění, obnovu účtu i opakované použití starých přístupů. U zápisů autentizovaných pomocí cookies prověřte CSRF hranici frameworku. Pro vykreslování a vstupy zahrňte kontexty skutečně použité aplikací: HTML, databázové dotazy, cesty souborů, uploady a parsování strukturovaných zpráv. Ověřte omezené selhání bez volání nekontrolovaného externího endpointu.

Pro odchozí stahování použijte vlastněné testovací cíle k ověření přesměrování, změn adres a zakázaných cílů. Vedle validace vstupů kontrolujte skutečně vynucovaná síťová pravidla. Metadata cloudu, interní služby a skutečné tajné údaje ponechte mimo test, pokud nejsou výslovně zahrnuty do autorizovaného posouzení.

U agentů testujte nepřátelský načtený obsah, podvržené výstupy nástrojů, neoprávněné argumenty, opakované použití schválení, změnu parametrů po schválení, otrávenou trvalou paměť a delegované pokyny žádající širší přístup. Ověřte, že vykonávací vrstva odmítne zakázané účinky, i když o ně model požádá. Zahrňte legitimní úkoly, aby systém odmítající vše nebyl nesprávně vyhodnocen jako užitečný a bezpečný.

U dodavatelského řetězce nebo CI zkoumejte, jak by nedůvěryhodný kód, změny workflow, instalační hooky závislostí a stažené artefakty mohly získat přístupy nebo právo publikovat. Podle potřeby ověřte hranici na izolovaném testovacím podkladu. K důkazu možného úniku tajného údaje nepoužívejte skutečný tajný údaj.

## Pravidla testování pro agenty

Zadání uvádí vlastníkem schválené cíle, povolené identity, techniky, časové okno, limity provozu, pravidla dat, externí závislosti, podmínky zastavení a místo odevzdání reportu. Kde je to možné, používejte izolované nasazení a syntetické účty. Ověřte, že testovací přístupy nemohou omylem zasáhnout produkci.

Oprávnění číst repozitář neopravňuje k aktivnímu skenování jeho produkční služby. Široký přístup k projektu nepovoluje stresový provoz, destruktivní vstupy, externí zpětná volání ani cíle třetích stran. Před těmito operacemi si vyžádejte chybějící rozsah oprávnění; nezávisle pokračujte ve statickém review a přípravě.

Aktivní testy zastavte, pokud cíl opustí povolený rozsah, nečekaně se objeví skutečná uživatelská data, zdraví služby překročí dohodnutý limit nebo selže omezení dopadu či úklid. Uchovejte minimální důkazy s odstraněnými citlivými údaji a informujte odpovědného vlastníka povoleným kanálem. Nerozšiřujte dopad jen kvůli působivějšímu nálezu.

## Posuďte, opravte a ověřte

Užitečný nález obsahuje testovanou revizi a konfiguraci, přesnou dotčenou cestu, aktéra a předpoklady, pozorované chování, očekávanou ochranu, dopad a minimální reprodukci. Oddělujte potvrzené, vyvrácené a nevyřešené kandidáty. Ve veřejném issue nepublikujte přístupy, osobní záznamy ani produkční detaily použitelné k útoku.

Opravu ověřte proti původní reprodukci a povolené legitimní operaci. Přidejte regresní test odhalující základní porušení hranice, nikoli pouze jeden konkrétní vstup. Pokud selhání plyne ze sdíleného návrhu, znovu posuďte příbuzné cesty. Při odložené úplné nápravě zaznamenejte zbytkové riziko a jeho lidské přijetí.

O vydání rozhoduje model hrozeb a důkazy, nikoli univerzální skóre skeneru. Nevyřešená hranice se závažnými důsledky blokuje dotčené vydání, pokud kvalifikovaný člověk výslovně nepřevezme zdokumentovanou výjimku. Cílené posouzení opakujte při změně oprávnění, vystavených rozhraní, citlivosti dat, závislostí nebo schopností agentů.

## Důkazy a související rozhodnutí

OWASP ASVS poskytuje verzované ověřovací požadavky; doporučení pro autorizaci, více tenantů a agenty doplňují konkrétní kontext hrozeb a kontrol. GitHub vysvětluje hranice důvěry specifické pro workflow. Výběrová matice a pravidla testování jsou původní místní pravidla; žádnému zdroji není připisováno schválení tohoto projektu.

[Bezpečnostní architektura](security.md) · [Strategie testování](testing-strategy.md) · [Kontroly kvality](quality.md) · [Člověk určuje směr, agent vykonává](agents.md) · [Výkonnostní a zátěžové testování](performance-testing.md)

## Primární zdroje

[owasp-asvs-requirements](https://raw.githubusercontent.com/OWASP/ASVS/3383877f732ce89a458a1af43288f2f1b1d7db0c/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-multi-tenant](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.md) · [owasp-session](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Session_Management_Cheat_Sheet.md) · [owasp-ssrf](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md)
