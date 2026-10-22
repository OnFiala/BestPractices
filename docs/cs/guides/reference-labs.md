---
{
  "id": "reference-labs",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Spouštění a interpretace referenčních projektů

## Tři spustitelné hranice

Referenční projekty jsou původní výukové implementace s vlastními lokálními testovacími náhradami. Umožňují agentům prozkoumat konkrétní kontrakty, záměrně vyvolávat selhání a uchovávat naměřené výsledky bez účtu u poskytovatele nebo placeného volání modelu. Jde o komponenty vybírané šesti projektovými postupy, nikoli o šest hotových produktů nebo šablon produkčního nasazení.

| Reference | Skutečná implementace | Záměrná náhrada a omezení |
| --- | --- | --- |
| `examples/durable_service` | Loopback HTTP, testovací identita svázaná s tenantem, transakce SQLite, pravidla idempotence a verzí, outbox a konzument, nácviky pádu podřízeného procesu, obnova snímku a omezené přetížení | Syntetické bearer přihlašovací údaje; lokální SQLite a jediný počítač; žádné skutečné platby, poskytovatel identity, broker ani regionální přepnutí při selhání |
| `examples/agent_workflow` | Trvale ukládaný workflow a samostatná evidence účinků, autorizace před sestavením kontextu, kontroly oprávnění pro přesnou akci, zrušení, rozpočty a sjednocení stavu | Deterministický testovací model, důvěryhodný testovací vydavatel schválení, simulovaný pád a opětovné otevření, syntetické jednotky rozpočtu; žádná kvalita skutečného modelu ani produkční autentizace |
| `examples/frontend` | Sémantické HTML a nativní moduly, stav URL a lokální i vzdálený stav, rušení podle identity požadavku, bezpečné vykreslení textu a skutečné kontroly v Chromiu | Syntetické API pouze pro čtení, jeden pozorovaný prohlížeč a prostředí, částečné kontroly přístupnosti; žádná produkční autentizace, zápisy ani nativní mobilní klient |

Každý README uvádí předpoklady, příkazy, výchozí podmínky, negativní orákula, úklid a vynechanou produkční práci. Při úpravě příkladu používejte tyto kontrakty; zkopírování kódu automaticky nepřijímá jeho předpoklady.

## Spouštějte kontroly a uchovávejte pozorování

Z kořene repozitáře:

```sh
python -m examples.durable_service demo
python -m examples.durable_service drills
python -m examples.durable_service benchmark --operations 120 --concurrency 8 --capacity 2 --delay-ms 10 --seconds 5
python -m examples.agent_workflow demo
python -m examples.agent_workflow evaluate
python -m library.verification delivery durable-service agent-workflow frontend-unit frontend-browser --output reports/reference-checks.json
```

Benchmark spouští pouze vlastní loopback testovací náhradu, přijímá omezené lokální parametry a nepřijímá URL vzdáleného cíle. Výše uvedená čísla definují malý výukový experiment; nejsou doporučenými produkčními limity ani cíli služby. Společně zkoumejte počty nabídnutých, zahájených, dokončených a odmítnutých operací i transportních chyb, naměřenou latenci, dobu testu a následnou integritu a obnovu. Chování generátoru a uzavřený model zátěže omezují interpretaci.

Evaluace agenta hlásí deterministické případy politik odděleně od položky kvality živého modelu, která je výslovně neprovedená. Úspěch provedených případů je užitečným důkazem těchto lokálních pravidel, nikoli důvodem započítat přeskočenou položku jako úspěšnou. Model i vydavatel schválení v demu jsou jasně pojmenované testovací náhrady.

Ověřovatel vyžaduje skutečně provedené testy, zaznamenává verze běhových prostředí a snímek vstupů a považuje chybějící, neúspěšné nebo přeskočené povinné kontroly za neúplné. Jeho prohlížečová sada potřebuje Node 22+ a nainstalovaný Chromium/Chrome. Výslovné volitelné povolení pro sandbox v řízeném kontejneru je zdokumentováno v README frontendu; platí pouze pro vlastní lokální testovací náhradu. Zprávy jsou lokální pozorování, nikoli autentizovaná osvědčení nebo lidské schválení.

## Ověřujte hranici selhání a obnovy

U trvalých zápisů porovnávejte povolené výsledky a zamítnuté vedlejší účinky. Opakované požadavky se stejným tenantem, akcí, klíčem a obsahem mají vrátit jeden uložený výsledek; konfliktní obsah musí selhat. Souběžní zapisovatelé verzí potřebují definovaný výsledek vítězství a konfliktu. Záznam outboxu a obchodní zápis sdílejí lokální transakci; konzumenti nesmějí potvrzovat neznámá schémata událostí. Obnova snímku ztrácí pozdější lokální zápisy a nevrací externí účinky.

U agentních akcí zkoumejte, co vstupuje do kontextu před vznikem návrhu, a poté co vykonavatel validuje nezávisle. Upravená akce ani akce s vypršeným nebo odvolaným oprávněním se nesmějí vykonat. Po nejistém účinku prozkoumejte nezávislé potvrzení o provedení a sjednoťte stav; chybějící nebo nesouhlasné potvrzení musí zůstat nevyřešené, nikoli spustit slepé opakování. U zrušeného běhu nebo běhu ukončeného timeoutem je stále potřeba započítat již provedenou práci.

V prohlížeči testujte skutečné veřejné ovládací prvky a souběhy transportu. I přerušený transport může dokončit získání těla odpovědi; identita požadavku musí zabránit nahrazení aktuálního stavu zastaralým dokončením. Zamítnutá nebo chybně strukturovaná data se nesmějí stát aktivním značkovacím kódem. Kontroly klávesnice, fokusu a úzkého rozvržení pokrývají konkrétní scénáře, nikoli všechny asistivní technologie nebo zařízení.

## Přejděte od reference k produktu

Vygenerujte balíček dodání, uveďte, které části znovu používáte, a nahraďte každou hranici testovací náhrady posouzeným projektovým kontraktem. Přidejte vybrané integrace úložiště, poskytovatele, identity a klienta i testy. Znovu spusťte negativní případy a případy obnovy proti těmto skutečným hranicím, měřte reprezentativní zátěž a zajistěte nezávislé posouzení nasazení a provozní odpovědnosti. Uchovejte neúspěšná a neprovedená pozorování. Produkční vydání je samostatné lidské rozhodnutí poté, co existují projektové důkazy.

## Související rozhodnutí

[Workflow agentního dodávání](project-delivery.md) · [Pokrytí a omezení](coverage.md) · [Odolnost](durability.md) · [Bezpečnostní testování](security-testing.md) · [Výkonnostní testování](performance-testing.md)

## Primární zdroje

[azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md) · [azure-outbox](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/databases/guide/transactional-out-box-cosmos.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [k6-open-vs-closed](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/using-k6/scenarios/concepts/open-vs-closed.md)
