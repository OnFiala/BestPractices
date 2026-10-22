---
{
  "id": "security",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Bezpečnost, soukromí a dodavatelský řetězec softwaru

## Převádějte rizika na vynutitelné hranice

Před zpracováním citlivých dat nebo přidělením práva zápisu nástrojům určete aktiva, aktéry, vstupní body a hranice důvěry. Popište realistické zneužití: uživatel zadá ID záznamu jiného tenanta, dokument vyzve agenta k exportu tajných údajů, úloha CI spustí nedůvěryhodnou závislost nebo obnova vrátí data nesprávného zákazníka. Každému riziku se závažnými důsledky přiřaďte vlastníka, preventivní kontrolu, pozorovatelné selhání a nápravnou akci.

Zvolte podporovanou verzi ověřovacího standardu, například OWASP ASVS, a vyberte požadavky odpovídající aplikaci. Zaznamenejte identifikátory požadavků včetně verze a místní výjimky; odkaz na přehled ASVS ani vyplněný checklist nejsou certifikace. Tento průvodce je původní rozhodovací rámec, nikoli reprodukce uvedeného standardu.

## Identita, oprávnění a tenanty

Používejte udržované autentizační komponenty místo vlastního návrhu protokolu hesel, relací nebo tokenů. Zdokumentujte založení účtu, obnovu přístupu, odebrání oprávnění a silnější autentizaci pro citlivé akce. Oddělte rozpoznání identity od rozhodování, co tato identita smí dělat.

Důvěryhodná vykonávací vrstva musí kontrolovat aktéra, cílový objekt a požadovanou operaci. Neprůhledný identifikátor, skryté tlačítko, privátní síť ani úspěšné přihlášení nejsou dostatečným důkazem oprávnění. Neznámé kombinace přístupů musejí bezpečně selhat. Testujte čtení, zápis, vyhledávání, export, správu i zpracování na pozadí včetně přístupu po změně členství.

Kontext tenanta odvozujte od ověřeného členství. Uplatňujte ho v databázových dotazech, úlohách, cache, souborovém úložišti, indexech pro vyhledávání podkladů i obnově. Pokud databázová pravidla pro řádky tvoří další hranici, ověřte, že je skutečná provozní role neobchází a spojení v poolu neuchovává kontext jiného tenanta. Exporty napříč zákazníky a správa přes hranice tenantů jsou samostatné schopnosti s vlastními oprávněními.

U relací v prohlížeči používejte podporovanou ochranu cookies a výslovně navržené chování expirace, odhlášení, rotace a revokace. Změny stavu autentizované pomocí cookies potřebují ochranu CSRF odpovídající frameworku; SameSite je doplňková kontrola. Obnova přístupu a změny oprávnění vyžadují stejnou pozornost jako přihlášení.

## Data, vykreslování a odchozí požadavky

Soukromé záznamy, přístupové údaje a zákaznické testovací podklady nesmějí být ve veřejné historii Gitu, výstupech webového sestavení, klientských balíčcích ani generovaných vyhledávacích indexech. Přihlašovací obrazovka nad veřejně stahovatelnými soubory je neudělá soukromými. Data klasifikujte před sběrem; určete retenci, mazání, export, zacházení se zálohami a osoby oprávněné vyšetřovat incidenty.

Vstupy ověřujte proti kontraktu aplikace. Používejte parametrizované databázové operace a udržované prostředky výstupního kódování nebo sanitizace odpovídající kontextu výstupu. Samotná validace nezabrání spuštění skriptu při vykreslení dat jako HTML. Omezte velikost a typ nahrávaných souborů, místo uložení a chování při jejich případném spouštění.

Server nebo agent stahující URL ovlivněná uživatelem potřebuje pravidla odchozích požadavků. Omezte schémata, cíle, přesměrování, velikost odpovědi i dobu běhu; zabraňte přístupu k interním službám a metadatům cloudu, pokud nejsou výslovně potřebné a povolené. DNS názvy cílů překládejte na adresy a ty kontrolujte na síťové hranici, aby změny DNS a přesměrování neproměnily zdánlivě povolené URL v přístup k internímu systému.

## Hranice agentů a dodavatelského řetězce

Získaný text, výstupy nástrojů, výstupy modelu a delegované zprávy považujte za nedůvěryhodná data. Přístup k nástrojům vynucujte mimo model: svažte identitu s rozsahem zdrojů, ověřujte argumenty a citlivé přístupové údaje držte ve vykonávací službě. Schválení závažné operace musí určit akci a parametry, mít omezenou platnost a bránit opakovanému použití. Anotace nástroje ani výrok agenta „schváleno“ nepřidělují oprávnění.

Dobu běhu, opakování, souběžnost, tokeny a útratu omezujte ve vrstvách, které to dokážou vynutit. Paměť a vyhledávání podkladů izolujte podle oprávněného uživatele nebo tenanta. Testujte nepřímou prompt injection, únik informací, změny pravidel a předávání práce mezi agenty. Guardrails mohou omezit selhání, nejsou však bezpečnostním perimetrem.

Oddělte identity vývoje, sestavení, nasazování a provozu. Tajné údaje nepatří do repozitáře; kde je to podporováno, používejte krátkodobé přístupové údaje s omezeným rozsahem. Výsledné konkrétní verze závislostí připněte pomocí lockfilu, ověřujte původ aktualizací a licence a sledujte zranitelnosti. Akce CI připínejte k neměnným commitům a kontrolujte, kdo může měnit workflow, artefakty a řešení závislostí. Nikdy nevystavujte produkční přístupy vykonávání nedůvěryhodného PR ani agentovi nepřipojujte Docker socket hostitele.

## Ověřujte, reagujte a přehodnocujte

Pomocí [průvodce bezpečnostním testováním](security-testing.md) propojte hrozby s automatickými a ručními důkazy. Před vydáním citlivého chování nacvičte neoprávněný přístup, oddělení tenantů, revokaci, obnovu a zneužití privilegovaných nástrojů. Zajistěte, aby logy podporovaly vyšetřování, aniž by zveřejňovaly přístupové údaje či zbytečné osobní údaje; chraňte také přístup k logům a jejich uchování.

Zaznamenejte kontakt pro incidenty, kroky omezení dopadu, odebrání přístupů, uchování důkazů, postup obnovy a vyřizování oznámení. Model hrozeb znovu posuďte po nové integraci, změně oprávnění, nové třídě dat, incidentu nebo změně architektonické hranice. Regulatorní povinnosti a přijetí rizika patří kvalifikovaným lidským vlastníkům.

## Související rozhodnutí

[Bezpečnostní testování](security-testing.md) · [Strategie testování](testing-strategy.md) · [Člověk určuje směr, agent vykonává](agents.md) · [Data, kontrakty a migrace](data.md) · [Provoz vlastních serverů](self-hosting.md)

## Primární zdroje

[owasp-asvs-requirements](https://raw.githubusercontent.com/OWASP/ASVS/3383877f732ce89a458a1af43288f2f1b1d7db0c/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-multi-tenant](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.md) · [owasp-authentication](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authentication_Cheat_Sheet.md) · [owasp-session](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Session_Management_Cheat_Sheet.md) · [owasp-csrf](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md) · [owasp-xss](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md) · [owasp-ssrf](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md)
