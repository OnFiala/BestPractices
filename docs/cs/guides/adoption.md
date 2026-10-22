---
{
  "id": "adoption",
  "language": "cs",
  "revision": 3,
  "translation_revision": 3,
  "reviewed_on": "2026-10-22"
}
---
# Použití knihovny v projektu

## Začněte doporučeným postupem

Pokud s knihovnou začínáte, projděte [první kontrolní bránu s důkazy](first-project.md)
a potom pokračujte [postupem realizace projektu](project-delivery.md) a průvodcem pro svůj typ projektu.
Vytvoříte plán a malý konkrétní výstup, zaznamenáte skutečné pozorování a posouzení.
**Kontrolní brána** je kontrolní bod s požadovanými výstupy a podmínkami, které blokují
pokračování. **Artefakt** je výstup, například záznam rozhodnutí, změna zdrojového kódu
nebo zpráva o testu. **Důkazy** zaznamenávají, co někdo na tomto výstupu skutečně
posoudil nebo spustil. Naplánovaná kontrola není pozorování a vyplněná šablona není schválení.

## Použijte správný profil

| Soubor | Účel | Kdo jej čte |
| --- | --- | --- |
| `templates/delivery-profile.json` | Příklad vstupu s přísným schématem JSON: typ projektu, přesná cílová revize, riziko, data, zátěž, hosting, rozhraní, účinky a cíle | `library.delivery plan`, `library.delivery assess` a `library.project init` |
| `project-profile.json` | Vyplněný JSON profil dodávání vašeho projektu; tento název generuje `init` | Stejné nástroje; název souboru se liší, schéma ne |
| `templates/project-profile.yaml` | Volitelný podrobný podklad pro rozhodování: vlastník, rozpočet, cíle služby, umístění dat, obnova a výjimky | Lidé a agenti; CLI jej nečte ani nepřevádí |

Pro plánování spouštěné nástroji začněte šablonou JSON. Nahraďte její syntetické
požadavky skutečnými rozhodnutími projektu. U existujícího projektu uchovávejte
profil a důkazy na schváleném místě daného projektu a spouštějte CLI knihovny
s výslovně uvedenými cestami. Nespouštějte `init` nad existujícím projektem:
vytváří pouze nový cílový adresář. Do nového přenosného balíčku `init` zkopíruje
potřebné nástroje, průvodce, licence a vybrané referenční příklady; ty nejsou vaším hotovým produktem.
Pro samotné čtení a podporu rozhodování odkazujte na příslušné průvodce a kopírujte
jen potřebné šablony; generování balíčku ani MCP není nutné.

Pokud vedete i podklad v YAML, přenášejte rozhodnutí uvážlivě:

| Podklad pro rozhodování | Profil dodávání | Co vyžaduje interpretaci |
| --- | --- | --- |
| `name`, `outcome`, `non_goals` | `project_id`, `description`, `objectives`, `constraints` | Zvolte platné stabilní ID a pozorovatelné výsledky; nestačí jen přejmenovat klíče |
| `data.classification` | `data_sensitivity` | Po posouzení skutečných dat vyberte podporovanou kategorii |
| Naměřená pole `workload` | `workload` | Zvolte odůvodněnou kategorii; pokud měření chybí, použijte `unmeasured` |
| `library_revision` | Žádné odpovídající pole profilu | Revizi knihovny připněte samostatně; `revision` v JSON znamená Git commit cílového projektu |
| Vlastník, rozpočet, cíle služby, umístění dat, obnova, výjimky | Uchovejte v podkladu a příslušných artefaktech kontrolních bran | Tyto povinnosti stále platí; plánovač tato pole YAML nevyhodnocuje |

Typ projektu, hosting, rozhraní, účinky a riziko také vyžadují výslovná rozhodnutí
v JSON. Automatický převod ani synchronizace neexistuje. Při změně společných
předpokladů aktualizujte oba dokumenty, znovu vygenerujte plán a přehodnoťte dotčené důkazy.
Do přísného schématu JSON nepřidávejte pole určená pouze pro YAML. Knihovnu připněte
k posouzenému vydání nebo úplnému commitu a používejte stabilní ID průvodců.
Tiché sledování proměnlivé větve `main` může změnit pravidla projektu bez jeho schválení.

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
