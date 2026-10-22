---
{
  "id": "playbook-internal-tool",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Dodání interního provozního nástroje

## Vhodnost a omezení

Tento profil použijte pro zaměstnaneckou aplikaci, která posuzuje záznamy, exportuje data nebo mění nadřazený podnikový systém. I malé publikum může mít oprávnění s velkým dopadem. Zaznamenejte poskytovatele identity, schvalovatele obchodních akcí, klasifikaci dat, lhůtu odebrání přístupu, limity nadřazených systémů a maximální přijatelnou dobu nevyřešené práce. Tento postup vytvořený agentem navrhuje místní způsob dodání; není přijatou politikou organizace.

Začněte jednou aplikací a explicitními integračními adaptéry. Organizační SSO používejte k autentizaci a oddělenou aplikační politiku pro akce a rozsah záznamů. Tabulka nebo existující produkt pro workflow zůstává alternativou, pokud jeho oprávnění, audit a export odpovídají skutečné potřebě. Worker je odůvodněný operacemi, které přesahují časový limit požadavku nebo vyžadují trvalé opakování. Integrace oddělujte, pouze když změřené šíření selhání, zpoždění front nebo nezávislé vlastnictví vyváží další náklady nasazení.

## Hranice repozitáře a oprávnění

V kódu oddělte `identity/`, `policy/`, `cases/`, `integrations/`, `exports/` a `audit/`. Definujte, který systém vlastní jednotlivá pole; importovaná hodnota nadřazeného systému se nesmí potichu stát nezávisle editovatelnou pravdou. Evidence operací zaznamenává žadatele, akci, rozsah objektů, verzi vstupu, identitu schválení, stabilní ID operace a stav. Nezbytné auditní skutečnosti ukládejte s řízeným přístupem a dobou uchování, nikoli jako neomezené kopie důvěrných dat.

Autentizace dokládá identitu, nikoli oprávnění. Akci a rozsah kontrolujte při vstupu do API, vytvoření exportu, stažení exportu a vykonání workeru. Práce ve frontě vyžaduje deklarovanou politiku delegace: buď znovu ověřte aktuální práva žadatele, nebo použijte samostatně schválené oprávnění služby. V datech úlohy nezachovávejte nechtěně oprávnění bývalého zaměstnance. Definujte čas odebrání přístupu napříč aplikačními relacemi, cache oprávnění, odkazy ke stažení a běžícími úlohami. U významných zápisů do nadřazeného systému svažte požadované obchodní schválení s přesnou zamýšlenou změnou.

## Pořadí dodání a předání

1. Průzkum mapuje jeden obchodní scénář, pole se zdrojem pravdy, autorizační matici a ruční náhradní postup při nedostupnosti nadřazených systémů. Lidský obchodní vlastník vyřeší nejasná schválení a uchovávání.
2. Implementace vytvoří úzký svislý průřez s prohlížením pouze pro čtení, změnou v povoleném rozsahu, trvalým stavem čekání a dohledáním operace. Export přidejte až po definování jeho oddělené autorizace a expirace.
3. Ověření zpochybní změny přístupu během relace i práce ve frontě a poté simuluje ztracenou odpověď po úspěchu nadřazené operace. Provozní role sepíše postup sjednocení pomocí stabilních ID operací a připraví nasazení pro jmenovanou skupinu zaměstnanců.

Dodejte profil, ADR, matici politik, inventář kontraktů nadřazených systémů, diagram přechodů stavů, specifikaci exportu, důkazy s očekávanými a pozorovanými výsledky, postup vydání a obnovy a vlastníka podpory. Agenti mohou role zastávat postupně; další agenti nevytvářejí nezávislé ujištění. Lokální adresáře `examples/durable_service` a `examples/agent_workflow` mohou pomoci při experimentech s perzistencí a prací podléhající schválení. Nedodávají podnikového poskytovatele identity ani schválení obchodních vlastníků.

## Vyberte adversariální a provozní kontroly

Jednotkově testujte rozhodnutí politik a přechody stavů. Integrační testy použijte pro zneplatnění relací, adaptéry nadřazených systémů, vytvoření exportů a trvalé úlohy. Testy prohlížeče mají zahrnovat zamítnutý přístup, nedostupná nadřazená data, prázdný seznam případů a čekající práci viditelnou i po obnovení stránky. Vypnuté tlačítko nikdy není autorizačním orákulem.

Nad syntetickými záznamy vytvořte omezeného zaměstnance a administrátora. Volejte chráněné endpointy přímo; požadujte příliš široký export a manipulujte s filtry i identifikátorem stažení. Exportované bajty a výsledné změny musejí zůstat v rozsahu volajícího. Odeberte zaměstnanci přístup, když existuje relace, podepsaný odkaz a operace ve frontě; po dohodnuté lhůtě musí chráněný přístup selhat a úlohy musejí dodržet deklarovanou politiku delegace. Sledujte stav a účinky v nadřazeném systému, nejen kódy odpovědí.

Nechte nadřazený systém přijmout změnu a zahodit odpověď. Opakování musí použít podporovanou idempotentní identitu nebo pozdržet operaci pro sjednocení. Nedostupný poskytovatel nesmí vypadat jako úspěch a timeout nesmí vymazat nejistotu. Testujte omezené opakování, zaplnění fronty a tempo obnovy vůči kvótám poskytovatele; zastavte před dohodnutými limity zdrojů. U blokovaných a přeskočených případů zaznamenejte chybějící předpoklad.

## Vydání, obnova a vlastnictví služby

Vydávejte definované skupině zaměstnanců se známým artefaktem pro rollback a zápisy do nadřazeného systému zpočátku omezenými schváleným plánem zavádění. U změn schématu podporujte smíšené verze a doplňujte data s checkpointy před odstraněním polí. Rollback aplikace nevrátí nadřazenou akci. Pozastavte odesílání, zkontrolujte evidenci, dotazujte stav poskytovatele a tam, kde je návrat možný, proveďte obchodně schválenou opravu. Auditní a aplikační záznamy obnovujte společně nebo vysvětlete vyrovnání mezer.

Sledujte dlouho čekající práci, zamítnuté operace, zpoždění odebrání přístupu, objem exportů, omezení poskytovatelem a případy vyžadující ruční opravu. Určete oddělené obchodní a technické vlastníky a lhůtu eskalace nejistých účinků. Do odhadů nákladů zahrňte integrační licence, čas zaměstnanců, auditní úložiště a pohotovost. Produkční mezery zahrnují skutečné SSO, politiku relací, nouzový přístup, pokrytí schvalovateli, uchovávání a nácviky incidentů. Ukončení vyžaduje uzavření čekajících případů, převod potřebných auditních záznamů, informování vlastníků procesů, odebrání přístupu služeb a ověření, že naplánované úlohy již nezapisují.

## Navazující rozhodnutí

[Bezpečnost](security.md) · [Provoz](operations.md) · [Strategie testování](testing-strategy.md) · [Odolnost](durability.md)

## Primární zdroje

[owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-session](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Session_Management_Cheat_Sheet.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
