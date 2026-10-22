---
{
  "id": "frontend",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Architektura frontendu a kontrakty

## Volte způsob vykreslování pro každou interakci

Statické generování se hodí pro veřejný obsah, který lze znovu sestavit. Serverové vykreslování může pomoci s aktuálností prvního zobrazení nebo dohledatelností, zatímco klientské vykreslování se hodí pro soustavnou interakci. Hybridní routy mohou tyto přístupy kombinovat. Jde o vlastní rozhodovací rámec této knihovny: před jeho přijetím změřte příslušný uživatelský scénář a prozkoumejte aktuální chování zvoleného frameworku.

Zaznamenejte odpovědnost za cache, náklady na hydrataci a JavaScript, autentizaci a hranice nasazení. Soukromou odpověď vykreslenou na serveru pro jednoho uživatele neukládejte do cache sdílené s jiným subjektem. Mikrofrontendy mohou podpořit nezávislou odpovědnost týmů, ale přidávají náklady na směrování, závislosti a konzistenci designu; nejsou výchozím způsobem dělení komponent.

## Každému stavu určete jednoho vlastníka

Rozlišujte stav na serveru, stav URL a navigace, lokální stav interakce a trvalé uživatelské preference. Určete, který stav přežije obnovení stránky nebo práci offline a jak se zneplatní po odhlášení či změně oprávnění. Organizujte funkce kolem explicitních rozhraní a sdílených přístupných primitiv. Kopírování stejných serverových dat do několika úložišť vytváří práci s jejich sjednocováním, nikoli odolnost.

Pro každou interakci využívající API definujte:

| Kontrakt | Příklad důkazu splnění |
| --- | --- |
| Autorizace | Přímé požadavky na API selžou, pokud uživatel nemá oprávnění, i když obejde uživatelské rozhraní |
| Podoba odpovědi | Staří i noví klienti zpracují dokumentovaná pole, chyby, stránkování a jednotky |
| Načítání a zrušení | Opuštění stránky zastaví zbytečnou práci nebo bezpečně ignoruje opožděný výsledek |
| Optimistická změna | Zamítnutí obnoví nebo sjednotí viditelný stav bez ztráty uživatelského vstupu |
| Offline a konflikt | Změna ve frontě má stabilní identitu a explicitní pravidlo řešení konfliktu po opětovném připojení |
| Soukromí | Odhlášení a odebrání přístupu odstraní nebo zneplatní příslušná soukromá data v cache |

Za důvěryhodnou validaci a autorizaci odpovídá server. Skrytá tlačítka a klientská schémata zlepšují použitelnost, ale nemohou vynucovat řízení přístupu. Tajné údaje backendu nesmějí být v balíčcích pro prohlížeč, souborech source map ani generovaných indexech. Kód prohlížeče a výstupy modelů či nástrojů jsou na hranici serveru nedůvěryhodné.

## Testujte pozorovatelný uživatelský scénář

Během implementace testujte doménová pravidla odděleně od detailů vykreslování. Při změnách API spouštějte testy kompatibility konzumentů. Před vydáním projděte hlavní scénáře jako [uživatel při black-box testování](testing-strategy.md): ovládání klávesnicí a pořadí fokusu, přístupné názvy, kontrast, úzké zobrazení, stavy načítání, prázdného výsledku a chyby, odepřený přístup a přerušené požadavky. Automatické kontroly přístupnosti podle potřeby doplňte posouzením konkrétních úloh pomocí klávesnice a asistivních technologií; úspěch automatického kontrolního nástroje nedokládá úplnou shodu s požadavky.

Pomocí [výkonnostního testování](performance-testing.md) ověřujte reprezentativní podmínky zařízení a sítě i dlouhodobé zatížení API; měřte navigaci, latenci interakce, přenesené prostředky a chyby. Ověřte, že frontend při opakování požadavků, pravidelném dotazování nebo opětovném připojení nenásobí volání backendu. Hranice autentizace a cache testujte podle [plánu bezpečnostních testů](security-testing.md).

## Rozvíjejte záměrně

Backend-for-frontend může být užitečný, pokud konkrétní klient potřebuje agregaci nebo silnější hranici na straně serveru. Uveďte přínos a odpovědnost za další nasazovanou službu. Framework měňte nebo mikrofrontendy zavádějte pouze tehdy, když migraci odůvodňují změřená omezení, včetně nákladů na přístupnost, kompatibilitu a podporu závislostí. Udržujte plán vydávání a zneplatňování cache, aby staré prostředky v prohlížeči zůstaly kompatibilní s nasazeným API.

WebMCP je zde postupné rozšíření možností. Běžné čtení a vyhledávání musí fungovat i bez něj; podporované prohlížeče stále vyžadují testy oprávnění, rušení operací a navigace. Experimentální zpřístupnění nástrojů nesmí udělit přístup, který uživatel již nemá.

## Související rozhodnutí

[Architektura](architecture.md) · [Strategie testování](testing-strategy.md) · [Výkonnostní testování](performance-testing.md) · [Bezpečnostní testování](security-testing.md) · [Integrace](integrations.md)

## Primární zdroje


[wcag](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/index.html) · [owasp](https://raw.githubusercontent.com/OWASP/ASVS/2b47a9dd16760ee484a6672d197f1f7e25d9c632/README.md) · [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/51ed75653aaa7f174f8dbe05d1bc327359bbc57c/README.md) · [wcag-keyboard](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/keyboard.html) · [wcag-focus-order](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/focus-order.html) · [wcag-focus-visible](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/focus-visible.html) · [wcag-contrast](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/contrast-minimum.html) · [azure-cqrs](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cqrs.md)
