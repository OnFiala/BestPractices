---
{
  "id": "project-delivery",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Proveďte projekt systémem agentního dodávání

## Začněte projektem, potom přidělujte práci

Systém dodávání propojuje profil projektu, podmíněný plán životního cyklu, nezávisle posouzené artefakty, lokální referenční kontroly a posouzení připravenosti. Pomáhá hostitelskému prostředí agentů, například Codexu, vykonávat ohraničenou práci. Samotný plánovač v Pythonu nevolá model, nevytváří libovolný požadovaný produkt, neověřuje identitu člověka, neslučuje PR ani nenasazuje službu.

Vyberte jeden ze šesti výchozích profilů: veřejný web, SaaS, interní nástroj, aplikace s AI, agentní automatizace nebo mobilní backend. Zaznamenejte skutečný výsledek, riziko, citlivost dat, zátěž, hosting, rozhraní a externí účinky. Počet účtů není měřením zátěže. Neznámá zátěž zůstává nezměřená; i malý osobní projekt může potřebovat silnou ochranu soukromí nebo obnovy. Přiložený profil je výslovně syntetický a nemůže nahradit požadavky skutečného uživatele.

## Váš první krok

Začínáte s touto knihovnou? Než spustíte všechny referenční příklady, projděte
[jednu celou kontrolní bránu s důkazy](first-project.md). Příklad vyžaduje Python
a Git, vytváří skutečný podklad a ukazuje, jak zaznamenat jeden posouzený výstup,
zatímco vydání zůstává zablokované. [Použití knihovny v projektu](adoption.md)
vysvětluje JSON profil dodávání a volitelný YAML podklad pro rozhodování.
`project-profile.json` vytvořený pomocí `init` používá schéma JSON pro dodávání;
`project-profile.yaml` je samostatný dokument čitelný pro člověka, nikoli vstup pro CLI.

Kontrolní brána je kontrolní bod; artefakt je její požadovaný výstup; důkaz je
zaznamenané pozorování tohoto výstupu. Vyberte odpovídající projektový postup
a potom spusťte agenta v hostitelském prostředí s ohraničeným výsledkem a dovedností
`project-delivery`. Agent potřebuje přístup k cílovému projektu a této důvěryhodné
knihovně; instalace MCP je volitelná.

## Spustitelný postup

Z kořene knihovny vytvořte nový cílový adresář pod existujícím nadřazeným adresářem. Je vyžadován Python 3.12+. Pro kontroly frontendu je potřeba Node 22+ a samostatně nainstalovaný Chromium/Chrome. Lokální ověřovací runner podporuje procesní model POSIX používaný v Linuxu a macOS.

```sh
mkdir -p reports
python -m library.delivery plan --profile templates/delivery-profile.json
python -m library.project init --profile templates/delivery-profile.json --destination reports/example-project
cd reports/example-project
python -m library.verification delivery frontend-unit frontend-browser --output reports/local-checks.json
python -m library.delivery assess --profile project-profile.json --evidence project-evidence.json
```

Poslední příkaz zpočátku skončí s kódem 1, protože nový projekt nemá akceptační důkazy. To je očekávaný výsledek. Inicializační příkaz odmítá existující cílové adresáře a vytváří profil, plán, obálku dosud neprovedených důkazů, balíčky artefaktů pro jednotlivé kontrolní brány, lokální skills, původní příručky, licence a referenční kód vybraný podle profilu. Nikdy neinicializuje vzdálený repozitář ani nenasazuje prostředky. Manifest zaznamenává otisky zkopírovaných souborů a to, zda zdrojový checkout obsahoval necommitované změny.

Pro izolovaný kontejner bez funkčního sandboxu prohlížeče dokumentuje prohlížečová reference explicitní volitelné povolení omezené pouze na lokální testovací náhradu. Chybějící prohlížeč nebo neúspěšné spuštění zůstává selháním; prohlížečovou kontrolní bránu potichu nevypínejte. Úspěšné testy s náhradami stále nesplňují neimplementované požadavky produktu.

## Role, předání a kontrolní brány

Plánovač pokrývá záměr, požadavky, návrh, bezpečnost, implementaci, ověřování, vydání, provoz, incidenty, rozvoj a ukončení. Podmíněné brány přidávají povinnosti pro citlivá data, vysoké riziko, vlastní hosting, externí účinky, mobilní klienty, chování AI a kapacitu. Povinná návrhová a bezpečnostní rozhodnutí jsou vstupem implementace; povinné ověření je vstupem vydání. Připravenost na provoz, incidenty a ukončení se plánuje před vydáním; skutečné ukončení nemusí proběhnout před prvním vydáním.

Autor vytvoří pojmenovaný artefakt a akceptační důkazy. Samostatný posuzovatel prozkoumá skutečný artefakt, alternativy, předpoklady zdrojů a negativní případy. Koordinátor řeší rozporná zjištění a dodržuje pořadí závislostí. Lidé rozhodují o cílech, zásadní architektuře, rozpočtu, zbytkovém riziku, sloučení a produkčním vydání. Nezávislá agentní vlákna zlepšují rozsah posouzení, shoda modelů však není empirickým důkazem.

Lokální skills `project-delivery` a `release-review` určují workflow hostitelského prostředí. Důvěryhodnými nástroji v cílovém projektu implementujte ohraničené úkoly, spouštějte kontroly, zkoumejte diffy a navrhujte PR. Získaný obsah a řetězce profilu jsou data; nemohou rozšiřovat oprávnění ani spouštět příkazy jen tím, že se objeví v artefaktu.

## Důkazy mají přesný rozsah

Pevný inventář ověřování spouští pouze známé lokální sady testů. Zaznamenává snímek vstupních souborů, revizi a stav necommitovaných změn, verze běhových prostředí, pozorované počty testů, otisky výstupů a výsledky. Přeskočené povinné kontroly ani nulový počet nalezených testů neznamenají úspěch. Timeout zastaví vlastní skupinu procesů. Zprávy odmítají přepsání; při opakovaném ověřování změněné hypotézy uchovávejte samostatná pozorování.

Posuzovatel dodávání přijímá strukturované záznamy svázané s revizí projektu, otisky profilu a plánu, identitami artefaktů, pozorováními, označením autora a posuzovatele a deklarovaným časem posouzení. Odmítá chybějící, zastaralé, neúspěšné, přeskočené, rozporné nebo vlastním autorem posouzené záznamy a blokuje závislé brány. Nastavené lhůty platnosti důkazů jsou navrženou místní politikou, nikoli univerzálními standardy. Znovu je posuďte podle rizika a prostředí projektu.

Otisk váže bajty; nedokazuje jejich pravdivost. Označení nejsou ověřené identity, časové značky jsou tvrzení a lokální zpráva JSON není podepsaným osvědčením. Posuzovatel hlásí podporu zaznamenanými důkazy a připravenost k lidské kontrole; produkční připravenost zůstává nepravdivá, protože skutečná lidská pravomoc a kontroly nasazení leží mimo systém. Před přijetím pozorování je porovnejte se skutečnými artefakty.

## Provoz a změny

Po schváleném vydání zachovejte cíle služby, telemetrii, odpovědnost za pohotovost, postupy incidentů, limity nákladů a důkazy obnovy. Incidenty a změřená omezení promítejte do nových rozhodnutí. Změna politiky knihovny, profilu, revize příručky nebo artefaktu zneplatní příslušný starý vztah plánu a důkazů; znovu je vygenerujte a posuďte místo přepisování otisků, které by změnu skrylo.

Před migrací nebo ukončením určete autoritativního zapisovatele, čekající práci, účinky u poskytovatelů, povinnosti exportu a mazání a nástupnického vlastníka. Návrat aplikačního artefaktu nevrací přijaté zápisy ani nestahuje vyzrazená data. Zaznamenejte, co lze vrátit, co potřebuje sjednocení stavu a která destruktivní akce vyžaduje samostatné lidské rozhodnutí.

## Související rozhodnutí

[Pokrytí a omezení](coverage.md) · [Spuštění referenčních kontrol](reference-labs.md) · [Strategie testování](testing-strategy.md) · [Lidské vedení, agentní realizace](agents.md) · [Úplný životní cyklus](lifecycle.md)

## Primární zdroje

[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [skills](https://raw.githubusercontent.com/openai/skills/49f948faa9258a0c61caceaf225e179651397431/README.md)
