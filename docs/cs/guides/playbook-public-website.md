---
{
  "id": "playbook-public-website",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Dodání veřejného webu

## Vhodnost a první rozhodnutí

Tento profil použijte pro veřejný redakční obsah, dokumentaci nebo kampaň, jejichž hlavním scénářem je čtení, vyhledávání a následování odkazů. Zaznamenejte jazyky, četnost publikování, požadavky na přístupnost, vlastníka domény, rozpočet přenášených prostředků a přijatelnou dobu nápravy škodlivého zveřejnění. Výchozím návrhem je statické sestavení z posouzeného obsahu, neměnné artefakty vydání a CDN. Jde o návrh vytvořený agentem a vlastní syntézu, nikoli přijatou politiku či potvrzení připravenosti k produkci.

Serverově vykreslovaná routa je alternativou, když aktuálnost nemůže čekat na sestavení. Autentizované odesílání dat vyžaduje explicitní serverovou hranici; službu pro zápis neschovávejte za detail statického webu. Malý web může mít obsah a prezentaci společně. Při růstu doby sestavení nebo konfliktů redakční práce nejprve oddělte validaci obsahu a zavádějte inkrementální sestavení. Služby přidávejte teprve tehdy, když jejich provozní cenu odůvodní změřené zpoždění publikace, dynamická práce nebo požadavky na odpovědnost; samotný počet návštěvníků nestačí.

## Hranice a kontrakty

Uspořádejte `content/`, `ui/`, `build/`, `tests/` a `ops/` podle odpovědnosti, i když sdílejí repozitář. Schéma obsahu vlastní stabilní ID stránek, jazyk, přesměrování, stav publikace a veřejná metadata. UI vlastní navigaci, stavy vyhledávání, fokus a přístupné chybové zprávy. Sestavení vlastní deterministickou transformaci a explicitní seznam povolených prostředků. Soukromé koncepty, přihlašovací údaje a interní komentáře nikdy nesmějí vstoupit do nasazovaného HTML, vyhledávacích indexů JSON, source map ani stahovatelných balíčků zdrojů.

Specifikujte trvalost URL, chování přesměrování, chybějící překlady, verzi vyhledávacího indexu a životnost cache. Index a stránky sestavujte jako stejné vydání. Identity pro náhled mohou číst koncepty; identita pro produkční publikování musí dostat pouze schválený artefakt. Vytvořené HTML, importovaný Markdown a text dotazu považujte při vykreslování za nedůvěryhodné; používejte bezpečné vykreslení textu nebo explicitně posouzenou politiku sanitizace.

## Pořadí práce

1. Průzkumný agent zaznamená do profilu projektu tři veřejné scénáře, inventář rout a jazyků, vlastnictví obsahu a číselné cíle publikování a výkonu. Člověk vyřeší rozhodnutí o značce, přístupnosti a riziku publikace.
2. Návrhová a implementační role vytvoří jeden úplný scénář včetně prázdného vyhledávání, neexistující routy, mobilního zobrazení a ovládání klávesnicí. Před rozmnožením šablon stránek zaznamená volbu vykreslování a náklady závislostí do ADR.
3. Ověřovatel zkontroluje sestavený artefakt v izolovaném skutečném prohlížeči, posoudí výstupní data a vyzkouší starší vydání. Vlastník vydání zvolí schválený otisk a řídí přístup k údajům pro nasazení.

Předejte konkrétní balíček: profil, ADR, schéma obsahu, seznam rout, otisk artefaktu a commit, pozorování z prohlížeče, mezery posouzení přístupnosti, kontrolu výstupních dat, pokyny k nasazení a obnově a jmenované vlastníky obsahu a domény. Oddělte plánované, provedené, neúspěšné a přeskočené kontroly. Lokální referenční adresář `examples/frontend` je východiskem pro práci na interakcích, nikoli důkazem ověření rout či přístupnosti tohoto projektu.

## Vyberte kontroly, které mohou připravenost vyvrátit

Jednotkovými kontrolami ověřujte parser a pravidla rout, integračními konzistenci obsahu s indexem a black-box testy v prohlížeči veřejné scénáře. U přejmenované stránky musí stará URL vést na zamýšlenou náhradu, nikoli na uvěřitelnou, ale chybnou stránku. Ve všech generovaných prostředcích hledejte syntetickou soukromou značku: nález znamená neúspěch vydání, i když značka není na viditelných stránkách. Do vyhledávání a importovaných nadpisů vložte značkovací kód; musí zůstat neškodným textem nebo projít posouzeným pravidlem sanitizace bez spuštění skriptu.

Zpomalte síť, nechte selhat stažení vyhledávacích dat a odejděte dříve, než skončí. Aktuální stránka musí zůstat rozhodující; opožděný výsledek nesmí přepsat novější dotaz a chyba musí umožnit zotavení. Ověřte dokončení úlohy klávesnicí a viditelný fokus v každém podporovaném jazyce; samotné automatické výsledky přístupnosti nedokládají shodu. Na reprezentativních zařízeních měřte první přenos bez cache, zpoždění interakce, dobu sestavení a chování zásahů cache vůči cílům projektu. Testy zastavte na dohodnutém limitu provozu nebo výdajů.

## Vydání, provoz a ukončení

Prohlédněte přesný artefakt, nasaďte jej omezenému publiku nebo na testovací doménu a před povýšením ověřte klíčové routy a hlavičky. Zachovejte předchozí artefakt a konfiguraci směrování. Rollback může obnovit stránky, ale nemůže stáhnout kopie z cache, vyhledávačů, stažených souborů či historie Gitu; únik vyžaduje reakci na incident a případně rotaci tajných údajů. Migrace přesměrování potřebují uchovanou mapu; odstranění jazyka vyžaduje explicitní posouzení odkazů a dopadu na uživatele.

Určete vlastníka neúspěšných sestavení, obnovy domény a certifikátu, zneužívajícího provozu a nouzové opravy obsahu. Sledujte chyby rout, chyby vyhledávání, stáří publikace a dostupnost syntetických scénářů bez uchovávání zbytečných údajů o návštěvnících. Rozpočtujte přenos CDN, minuty sestavení, logy, závislosti a redakční údržbu. Před produkcí uzavřete mezery konfigurace hostingu, politiky hlaviček, záloh a exportu, přístupnosti i pohotovosti; reference je nedodává. Při ukončení zachovejte dohodnuté exporty obsahu a přesměrování, odeberte publikační přístup, odstraňte sledování a po dohodnutou přechodnou dobu si ponechte kontrolu nad doménou.

## Navazující rozhodnutí

[Kontrakty frontendu](frontend.md) · [Hosting](hosting.md) · [Dodávání přes GitHub](github.md) · [Strategie testování](testing-strategy.md)

## Primární zdroje

[github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [owasp-xss](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md) · [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [wcag-keyboard](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/keyboard.html) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
