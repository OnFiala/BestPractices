---
{
  "id": "playbook-ai-application",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Dodání aplikace s AI

## Vhodnost a ohraničený výsledek

Tento profil použijte pro autentizovanou aplikaci, která vyhledává informace nebo vytváří odpověď pomocí modelu. Definujte uživatelský úkol, přijatelné chyby, zakázané úniky, časový limit latence, strop nákladů, umístění dat a běžný náhradní postup bez modelu. Začněte jedním ohraničeným zpracováním požadavku, adaptérem poskytovatele a evaluační datovou sadou. Tento návrh vytvořený agentem kombinuje vlastní technický úsudek s citovanými důkazy; nedokládá spolehlivost modelu.

Vyhledávání nebo deterministická pravidla jsou alternativou, pokud plní úkol předvídatelněji. Retrieval může podpořit odpovědi ukotvené v projektových datech; dotrénování nenahrazuje politiku přístupu k dokumentům ani aktuálnost. Modely, poskytovatele, cache nebo asynchronní fáze přidávejte, pouze když jejich evaluační a provozní cenu odůvodňují změřená omezení kvality, zpoždění, propustnosti nebo umístění dat. Samotná větší uživatelská základna neodůvodňuje agentní smyčku.

## Oddělte oprávnění, data a chování modelu

Uspořádejte `api/`, `policy/`, `retrieval/`, `model_adapter/`, `evaluation/` a `telemetry/`. Server autentizuje volajícího a filtruje kandidátní dokumenty podle aktuálního přístupu dříve, než obsah dorazí k modelu. Do návrhu cache a vyhledávání zahrňte tenant, verzi politiky, verzi dokumentu a stav smazání. Globální cache odpovědí klíčovaná jen dotazem může vyzradit kontext jiného uživatele. Definujte, jak se odebrání přístupu a smazání promítají do indexů, uložených promptů, vygenerovaných odpovědí a dat u poskytovatele podle zvoleného kontraktu.

Model vrací nedůvěryhodný obsah. Validujte strukturovaný výstup, bezpečně vykreslujte text a vykonávání nástrojů držte za nezávislou autorizací. Nalezené instrukce, citace ani sebejistota modelu nikdy neudělují oprávnění. Definujte kontrakty odpovědí pro podloženou odpověď, nedostatek důkazů, nedostupného poskytovatele, vyčerpaný rozpočet a zrušení. Citace musí označit nalezený zdroj, který skutečně podporuje příslušné tvrzení; věrohodně vypadající URL není podložení. Surové přihlašovací údaje udržujte mimo prompty a logování vybavte explicitní politikou soukromí a uchovávání.

## Pořadí práce a její důkazy

1. Průzkum před výběrem modelu určí reprezentativní úlohy, závažnost selhání, zákonné nakládání s daty a hodnoticí rubriku. Lidský vlastník dohodne přijatelné chybovosti a rozhoduje nejednoznačné případy.
2. Implementace vytvoří jedno zpracování s autorizovaným vyhledáváním, omezeným kontextem, lhůtou poskytovatele, validací výstupu a náhradním postupem. Nastavení modelu, prompt, konfiguraci vyhledávání a indexu a schémata nástrojů verzujte společně.
3. Ověření spustí vyhrazenou evaluační sadu bezpečnou pro soukromí a adversariální případy, následně prozkoumá stopy autorizace a nákladů. Příprava vydání porovná kandidáta s pevnou základnou a zdokumentuje lidské posouzení i nevyřešená selhání.

Předávací balíček obsahuje profil, ADR datových toků, rozhodnutí o poskytovateli a zpracování dat, přístupovou matici, identitu evaluační sady, skóre jednotlivých případů a lidská rozhodnutí, manifest verzí, rozložení latence a nákladů, důkazy náhradního postupu a vlastníka incidentů. `examples/frontend` a `examples/agent_workflow` nabízejí lokální reference interakcí a řídicích hranic k prozkoumání. Žádná nedokládá významovou kvalitu odpovědí, soulad poskytovatele s požadavky ani bezpečnost produkční retrieval služby.

## Používejte orákula mimo model

Vyberte jednotkové testy pro schéma a účtování rozpočtu, integrační pro filtrování přístupu a selhání poskytovatele a evaluace pro užitečnost a podložení. Trénovací a ladicí příklady držte odděleně od vyhrazených akceptačních případů. Správnost odpovědi, nepodložená tvrzení, vhodné zdržení se odpovědi a škodlivé opomenutí skórujte samostatně; průměr může skrýt závažný únik. U subjektivních výsledků jsou nadále nutné rubriky posouzené člověkem. Hodnocení modelem je pomůcka měření, nikoli nezávislá autorita pro přijetí.

Do nepřístupného dokumentu vložte jedinečnou syntetickou značku. Dotazujte se na ni přímo, nepřímo a přes povolený dokument s nepřátelskými instrukcemi. Značka musí chybět ve vyhledaném kontextu, požadavcích poskytovateli, vrácených odpovědích i zpřístupněných lozích. Po odebrání přístupu nebo smazání opakujte se zahřátými cache a indexy. Zkuste výstup porušující schéma a citace podobné skriptům: nesmějí se vykonat ani rozšířit přístup. Jde o negativní orákula, nikoli kontroly zdvořilého odmítnutí modelem.

Vynucujte timeouty poskytovatele, odpojte prohlížeč a vyčerpejte vynucovaný rozpočet požadavku. Aplikace musí přestat plánovat další volání, zachovat srozumitelný uživatelský stav a zaznamenat již provedenou práci; zrušení nezaručuje, že poskytovatel přestal účtovat. Porovnejte opakované běhy kvůli variabilitě kvality a při omezené zátěži měřte latenci v horních percentilech i náklady na přijatý úkol. Zaznamenejte skutečné velikosti vzorků, neúspěšné případy a netestované jazyky či domény.

## Vydání a dlouhodobý provoz

Zavádějte pro dohodnutou skupinu s vypínačem funkce a sledujte prahy kvality, zdržení se odpovědi, chyb, latence a výdajů. Změna modelu, promptu, vyhledávání či náhradního postupu je vydáním chování vyžadujícím novou evaluaci. Uchovejte předchozí manifest verzí a kompatibilní reprezentaci indexu. Rollback může vrátit chování, ale nemůže stáhnout zveřejněné informace ani odeslané požadavky poskytovateli. Únik vyžaduje řešení incidentu a posouzení přístupu a dat; smazání lokálního logu nestačí.

Určete vlastníky posunu výsledků evaluace, přístupové politiky, incidentů poskytovatele a eskalace nákladů. Vedle inference rozpočtujte aktualizace embeddingů a indexů, opakování, evaluační běhy, úložiště a lidskou kontrolu. Před produkcí vyřešte uchovávání a umístění dat poskytovatele, skutečnou identitu, šifrování, propagaci smazání, limity zneužití a provozní pokrytí. Ukončení vypne vstupy, dokončí bezpečnou práci, smaže nebo uchová odvozené artefakty podle politiky, odebere přístup poskytovatele a zachová pouze důkazy nutné pro odpovědnost.

## Navazující rozhodnutí

[Agenti](agents.md) · [Bezpečnost](security.md) · [Kontroly kvality](quality.md) · [Strategie testování](testing-strategy.md)

## Primární zdroje

[owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-xss](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
