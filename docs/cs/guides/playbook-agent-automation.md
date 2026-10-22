---
{
  "id": "playbook-agent-automation",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Dodání ohraničené agentní automatizace

## Vhodnost a minimální řídicí vrstva

Tento profil použijte, když model navrhuje nebo koordinuje akce s trvalými důsledky: mění záznamy, připravuje vydání nebo obsluhuje externí nástroje. Zaznamenejte povolené cíle, vlastníka úkolu, maximální rozsah, požadavky na schválení, politiku opakování a limity času, tokenů i nákladů. Pokud je posloupnost rozhodnutí již známá, je vhodnější deterministický workflow. Začněte jedním ohraničeným workerem a trvalou evidencí běhů; uvažování modelu přidejte jen tam, kde zlepšuje měřený výsledek úkolu. Tento postup vytvořený agentem je navrženou vlastní syntézou.

Nezačínejte flotilou agentů. Workery, fronty nebo identity oddělte, když měření ukážou dlouhodobé vytlačování priorit, neslučitelná oprávnění nástrojů nebo nezávisle vlastněné závazky spolehlivosti. Delegace přidává náklady koordinace, přihlašovacích údajů a celkového rozpočtu. Podúloha dědí užší oprávnění a rozpočet, nikdy novou pravomoc jen proto, že ji požadoval jiný agent.

## Repozitář, kontrakty a trvalý stav

Oddělte `planner/`, `policy/`, `tool_gateway/`, `ledger/`, `reconciliation/` a `evaluation/`. Plánovač navrhuje typované akce. Komponenta politik nezávisle kontroluje aktéra, úkol, nástroj, přesný cíl, parametry a rozsah. Brána nástrojů vlastní přihlašovací údaje a vynucuje konečné rozhodnutí. Výstup nástroje a vyhledaný text jsou nedůvěryhodná pozorování; nemohou upravit politiku, obnovit schválení ani vybrat nepovolený cíl.

Trvale uložte identitu úkolu, otisk akce, identitu a expiraci schválení, pokusy, rezervace rozpočtu, odkazy na výsledky a přechody stavů. Rozlišujte naplánováno, čeká na schválení, autorizováno, provádí se, uspělo, selhalo, zrušeno a nejisté účinky. U práce vyžadující schválení svažte schválení s aktérem a přesnou akcí; spotřebujte nebo rezervujte je atomicky, aby je souběžné workery nemohly použít dvakrát. Změna parametrů vyžaduje nové rozhodnutí. Příznak schválení uvnitř textu modelu není důvěryhodným záznamem.

Pád po externím účinku, ale před potvrzením vytváří nejistotu. Pokud je podporován, použijte idempotentní klíč poskytovatele nebo dohledání u poskytovatele podle stabilní identity operace. Jinak zastavte a sjednoťte stav s oprávněným operátorem; nepřejmenujte nejistotu na selhání a neopakujte naslepo. Trvalost evidence nezajišťuje právě jedno provedení libovolné externí akce.

## Pořadí implementace a posouzení

1. Průzkumná role inventarizuje každý nástroj, účinky čtení a zápisu, cíl, potřebnou autorizaci, možnosti obnovy a vlastníka. Člověk vyřeší politiku nevratných akcí a explicitní hranice schvalování.
2. Implementace nejprve dokončí deterministický běh proti lokálním testovacím náhradám včetně uloženého stavu, zamítnutí, zrušení, restartu a sjednocení. Za tyto hranice přidá modelový plánovač a definuje jeho typovaný kontrakt.
3. Ověřovatel napadá okraje oprávnění a schválení, duplikuje práci a přerušuje vykonávání. Role vydání připraví omezené identity, nouzové vypnutí, monitoring a příručku operátora před zapnutím skutečného konektoru.

Dodejte profil úkolu, matici oprávnění, ADR stavového automatu, schémata nástrojů, příklady schválení přesné akce, evidenci běhů a účinků, pozorované výsledky testů, model rozpočtu, pokyny pro sjednocení a jmenovaného vlastníka eskalace. `examples/agent_workflow` je lokální reference pro studium této hranice. Připojení skutečného nástroje stále potřebuje jeho autentizaci, omezení cílů, politiku schválení a kontrakt obnovy účinků; běh s testovací náhradou nic z toho neuděluje.

## Testy s nezávislými orákuly účinků

Používejte jednotkové testy pro politiku a přechody stavů, integrační testy perzistence pro restart a souběh a end-to-end testy proti izolovaným cílům nástrojů. Veďte samostatnou evidenci účinků vlastněnou testovací náhradou, aby vyprávění modelu nemohlo doložit úspěch. Duplikujte tentýž úkol mezi workery: zkontrolujte záznamy běhů i skutečné účinky. Podle deklarovaného kontraktu je přijatelný jeden zamýšlený účinek nebo explicitní nevyřešený stav; tiché duplicity nikoli.

Nechte schválení vypršet, nahraďte jeho aktéra, upravte částku nebo cíl a zopakujte spotřebované schválení. Externí nástroj nesmí být zavolán. Dodejte vyhledaný text tvrdící administrátorské oprávnění a podvrženou odpověď nástroje požadující nový cíl. Brána musí nadále vynucovat původní oprávnění. Odeberte přístup k nástroji mezi plánováním a vykonáním, abyste ověřili kontrolu politiky na hranici účinku.

Vyvolejte pád poté, co náhrada zaznamená úspěch, ale před uložením potvrzení workerem. Restart musí akci sjednotit nebo pozdržet, nikoli automaticky zopakovat. Vyčerpejte rozpočty běhu i delegace a zrušte úkol ve frontě; další práci nelze plánovat, ale probíhající účinky je nutné sledovat až do konečného nebo nejistého výsledku. Fronty testujte dohodnutou omezenou zátěží a sledujte hladovění úloh, násobení opakování a frontu operátora. Zachovejte neúspěšné, přeskočené a neprovedené případy; dokončená konverzace modelu není úspěšný test.

## Vydání, obnova a ukončení

Konektory zavádějte jednotlivě s posouzeným rozsahem a omezenými cíli nasazení. Schémata nástrojů a migrace evidence verzujte kompatibilně, aby existující běhy zůstaly interpretovatelné; před odstraněním starých obsluh dokončete nebo explicitně migrujte běhy. Rollback aplikace nevrací účinky nástrojů ani neobnovuje schválení. Při incidentu zastavte odesílání, odeberte kompromitovaná oprávnění, zachovejte chráněné auditní důkazy a sjednoťte otevřené operace před pokračováním autorizované práce.

Sledujte zamítnuté akce, zastaralá schválení, stáří nejistých účinků, nevyřízené sjednocování, úspěšnost úkolů, lidské opravy a výdaje na přijatý výsledek. Rozpočtujte volání modelu, poplatky nástrojů, opakování, úložiště evidence a čas operátora. Produkční mezery zahrnují skutečnou identitu, chráněné úložiště schválení, izolaci přihlašovacích údajů, auditní uchovávání, záruky poskytovatele a pohotovostní reakci. Ukončení zastaví příjem práce, vyřeší nebo eskaluje čekající účinky, exportuje požadované důkazy, zruší všechny konektory a plánování a smaže citlivý kontext běhů podle dohodnuté politiky uchovávání.

## Navazující rozhodnutí

[Agenti](agents.md) · [Odolnost](durability.md) · [Integrace](integrations.md) · [Bezpečnostní testování](security-testing.md)

## Primární zdroje

[owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
