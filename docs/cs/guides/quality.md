---
{
  "id": "quality",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Kontroly kvality dokazující chování

## Vybírejte důkazy podle změny

Testování je součástí zadání úkolu agenta. Před implementací určete ohrožené chování, následek selhání a pozorování, které by prokázalo chybu. Přiměřenou sadu kontrol vyberte podle [strategie testování](testing-strategy.md). Bezpečnostně citlivé hranice vyžadují také [bezpečnostní testy](security-testing.md); změny souběžnosti, zdrojů nebo kapacity vyžadují [výkonnostní testování](performance-testing.md).

Textová oprava potřebuje redakční kontrolu a kontrolu odkazů, nikoli novou sadu testů postavenou převážně na mock objektech. Opakování platby, filtr tenanta, databázová migrace nebo změna privilegovaného nástroje potřebují důkazy o chybových cestách. Výrok „všechny dosavadní testy prošly“ neříká, zda je otestován změněný kontrakt.

## Důkazy před implementací

Zadání úkolu zaznamenává dotčeného spotřebitele, očekávané úspěšné i odmítavé chování, reprezentativní data, vykonávací prostředí a přijatelný výsledek. Pokud může selhání chování mít závažné důsledky, zahrňte alespoň jeden relevantní negativní nebo hraniční případ. Očekávané výsledky musí být nezávislé na implementovaném algoritmu: test, který znovu vypočítá stejný chybný vzorec, se může s chybou shodnout.

Při opravě chyby podle možností prokažte, že cílená kontrola odhalí původní selhání. U nového invariantu prověřte test záměrně neplatnými testovacími daty nebo dočasnou místní mutací kódu. Tuto mutaci před návrhem změny odstraňte. Knihovna tyto kontroly doporučuje podle rizika; nevyžaduje mutační testování každé úpravy ani univerzální procento pokrytí.

## Vytvořte užitečnou bránu dodání

Vyžadujte opakovatelnou instalaci závislostí a sestavení odpovídající stacku. Typové, lintovací a statické kontroly přidejte tam, kde odhalují realistické chyby. Nejprve spusťte cílené kontroly chování, poté dotčenou integrační nebo kontraktní sadu. Pokud jde o izolaci, transakce, serializaci, události prohlížeče nebo oprávnění, používejte skutečné implementace na hranicích; samotné mock objekty tyto vlastnosti neprokážou.

Udržujte malou sadu úplných uživatelských průchodů, která pokrývá hodnotné výsledky a jejich kritické chybové stavy. Používejte izolované účty a syntetická data. V opakovatelných testech mějte pod kontrolou externí závislosti a samostatně provádějte vymezené testy kompatibility proti sandboxům poskytovatelů. Test e-mailu nebo platby nesmí omylem kontaktovat skutečné zákazníky ani strhnout peníze z živého účtu.

Selhání povinné kontroly musí způsobit selhání úlohy dodání. Odděleně vykazujte úspěšné, neúspěšné, přeskočené, karanténované a nespuštěné případy. Nesnižujte práh ani neodstraňujte assertion jen proto, aby změna prošla. Skutečně změněný požadavek potřebuje vlastní vysvětlení a lidské posouzení. Nestabilní testy v karanténě potřebují vlastníka, důvod, konec platnosti a náhradní důkazy pro chráněné chování.

## Důkazy pro změny vytvořené AI

Konečný diff a testy posuzujte společně. Posuzovatel má zpochybnit předpoklady implementátora, nikoli pouze zopakovat stejný prompt. Pro změny modelů, promptů, nástrojů, vyhledávání podkladů a pravidel používejte reprezentativní regresní sadu. Vývojové příklady oddělte od vyhrazených evaluačních případů. Hodnoťte užitečné dokončení úkolu i nežádoucí účinky; přesvědčivá odpověď nedokazuje bezpečné vykonání nástroje.

Zaznamenejte model a konfiguraci, verzi testovacích dat, pravidla nástrojů, počet opakování, hodnoticí kritéria a pozorovanou variabilitu. Hodnocení modelem podle možností kalibrujte na lidsky posouzených příkladech a deterministických kontrolách. Evaluační data chraňte před úniky mezi tenanty a prompt injection. Změna evaluačního produktu nebo poskytovatele potřebu těchto záznamů neodstraňuje.

## Rozhodnutí o vydání a údržba

Agent vrací přesnou revizi, příkazy, prostředí, výsledky, známé vynechané kroky a plán obnovy. Dotčené vydání zastavte, když selže povinná kontrola, závažné chování zůstane netestované nebo dostupné důkazy odporují tvrzenému výsledku. Člověk může zaznamenat časově omezenou výjimku s vlastníkem a náhradní kontrolou; agent nesmí potichu předefinovat selhání na úspěch.

Sledujte chyby odhalené až v provozu, nestabilní kontroly, pomalou zpětnou vazbu a obnovu po změnách. Po významném incidentu přidejte cílený regresní test. Kontroly odstraňujte jen tehdy, když je jejich ochranný účel zastaralý nebo lépe pokrytý jinde. Cílem jsou věrohodné důkazy při udržitelných nákladech, nikoli největší počet testů.

## Tato knihovna a rozsah důkazů

Repozitář ověřuje identitu obsahu, odkazy na zdroje, revize překladů, odkazy, chování integrací a generování webu. Tyto kontroly necertifikují architektonická doporučení ani význam překladů. Lidská redakční kontrola zůstává samostatnou podmínkou.

Výše popsaný postup je původní místní syntéza. Playwright podporuje izolované kontroly chování prohlížeče z pohledu uživatele; OWASP podporuje testování autorizace a zneužití agentů; GitHub popisuje hranice důvěry workflow. Tyto zdroje nepředstavují univerzální standard testování ani schválení této knihovny.

## Související rozhodnutí

[Strategie testování](testing-strategy.md) · [Výkonnostní a zátěžové testování](performance-testing.md) · [Bezpečnostní testování](security-testing.md) · [Člověk určuje směr, agent vykonává](agents.md) · [Úplný životní cyklus projektu](lifecycle.md)

## Primární zdroje

[playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md)
