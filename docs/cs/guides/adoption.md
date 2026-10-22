---
{
  "id": "adoption",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Použití knihovny v projektu

## Sestavte přenosný soubor rozhodnutí

Kopírujte potřebné šablony, ne celou knihovnu. Do `project-profile.yaml` zapište zamýšlený výsledek, citlivost dat, odpovědného vlastníka, zátěž, rozpočet, cíle služby a předpoklady obnovy. Knihovnu připněte k posouzenému vydání nebo úplnému commitu a stabilním ID průvodců. Tiché sledování proměnlivé větve `main` může změnit produkční pravidla bez schválení v projektu.

Vytvořte kontextový diagram a ADR pro první zásadní rozhodnutí. Zaznamenejte přijatá doporučení, záměrně odložené kontroly, vlastníka, termín platnosti a náhradní kontroly. Projektové pokyny pro agenty udržujte v `AGENTS.md` a odkazujte na podpůrné materiály. Tato knihovna je zdroj návrhů udržovaný agenty. Její doporučení se stávají pravidly projektu až prostřednictvím lidského rozhodování v daném projektu.

## Tři výchozí příklady

- **Osobní veřejný web:** použijte statické sestavení, historii obsahu a opakovatelné nasazení. Soukromé poznámky, přístupové údaje a osobní zdrojová data nesmějí být ve veřejné historii Gitu ani ve veřejných výstupech sestavení včetně vyhledávacích indexů. Přihlašovací obrazovka neochrání veřejně stahovatelné soubory. Soukromá znalostní báze potřebuje soukromé úložiště a serverem vynucované kontroly přístupu k dokumentům, souborům, stahování i vyhledávání; soukromý repozitář sám nezajistí soukromí zveřejněných výstupů.
- **Malý SaaS:** začněte modulární aplikací, transakční databází a workerem pouze tam, kde je potřebný. Určete hranice tenantů, postup porovnání platebních záznamů a odpovědnost za provoz. Před přijetím skutečných zákazníků prokažte odmítnutí přístupu mezi tenanty, kompatibilitu během nasazování a obnovu do izolovaného prostředí.
- **Platforma s vysokým provozem:** nejprve změřte skladbu provozu, nerovnoměrnost zátěže, růst dat a limity závislostí. Zátěž rozdělte nebo izolujte až po prokázání omezení a určení odpovědnosti za konzistenci, migraci, pohotovost i obnovu. Velký počet účtů sám nevyjadřuje potřebnou kapacitu.

Jde o původní výchozí doporučení této knihovny, nikoli univerzální předpisy nebo nasazovací šablony ověřené výkonnostním měřením.

## Převádějte doporučení na důkazy přijetí

Pro každý přijatý průvodce určete pozorovatelnou povinnost a kontrolu, která by mohla vyvrátit její splnění. Například „izolace tenantů“ se promění v test, v němž přihlášená relace tenanta A žádá objekt tenanta B přes API, export i cestu workeru a žádná z těchto cest nevrátí data B. Prostředí testu, očekávaný výsledek, skutečně testovanou revizi a uchované důkazy zaznamenejte podle [strategie testování](testing-strategy.md).

Pomocí [referenčních profilů](../reference/examples.md) odhalte chybějící hranice. Dosud nespuštěný scénář přijetí je plán testu, nikoli důkaz. Netvrďte, že je systém bezpečný, protože je vyplněná šablona nebo generované shrnutí říká „prošlo“. Posuďte skutečný výsledek včetně selhání a vynechaných kontrol.

## Přehodnocujte bez ztráty kontroly

Při plánování čtěte příslušné průvodce a odkazujte na ně v implementačním úkolu. Při review porovnejte diff se zvoleným rozhodnutím a scénáři selhání. Před vydáním ověřte migraci a obnovu; během provozu vracejte měření a incidenty do ADR. Připnutou verzi knihovny aktualizujte prostřednictvím PR, které vysvětlí změněné povinnosti, dotčené projekty a plán migrace nebo výjimky.

Pokud nové doporučení nelze ověřit v rámci rozpočtu nebo kapacity odpovědných osob, zaznamenejte tuto mezeru a zjednodušte návrh. Nepřijímejte tiše pravidlo, podle kterého nikdo nedokáže systém provozovat.

## Související rozhodnutí

[Principy rozhodování](foundations.md) · [Úplný životní cyklus projektu](lifecycle.md) · [Strategie testování](testing-strategy.md) · [Člověk určuje směr, agent vykonává](agents.md) · [Správa a nezodpovězená rozhodnutí](governance.md)

## Primární zdroje

[plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md)
