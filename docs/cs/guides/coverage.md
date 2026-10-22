---
{
  "id": "coverage",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Posuzujte pokrytí a ověření poctivě

## Používejte deklarovanou mapu pokrytí

Strojově čitelný registr pokrytí popisuje oblasti životního cyklu podporované tímto vydáním. Každý záznam propojuje doporučení a primární zdroje, pojmenovává případnou spustitelnou referenci a přesné testovací případy, definuje úzce vymezené tvrzení a uvádí důkazy, které v přejímajícím projektu stále chybějí. Mapa je deklarovaným rozsahem, nikoli tvrzením, že vyjmenovává celé softwarové inženýrství.

Čtěte ji pomocí `python -m library.coverage`, nástroje MCP pouze pro čtení nebo exportovaných webových dat. Volitelná lokální ověřovací zpráva může přidat pozorování svázaná s aktuálním snímkem vstupů. Statický registr webu se nestává čerstvě provedeným výsledkem tím, že jej čtenář otevře.

## Rozlišujte druhy podpory

| Podpora | Co existuje | Co zůstává neznámé |
| --- | --- | --- |
| Zdokumentované doporučení | Původní vysvětlení rozhodnutí a odkazy na zdroje s vymezeným rozsahem | Zda se vysvětlení vztahuje na tento projekt nebo bylo implementováno |
| Spustitelná reference | Původní kód a pojmenované kontroly, které mohou prověřit deklarovanou lokální hranici | Zda tyto kontroly proběhly nad těmito přesnými vstupy a co se stalo |
| Aktuální zaznamenané pozorování | Odpovídající otisky vstupů a úspěšná zaznamenaná sada s požadovanými pojmenovanými případy | Zda je zpráva autentická, orákulum dostatečné nebo jiný cíl vykazuje stejné chování |
| Chybějící, zastaralé, neúspěšné nebo částečné pozorování | Požadované důkazy chybějí, změnily se, selhaly nebo jsou neúplné | Nepodložené tvrzení zůstává nepodložené; z mlčení nevyvozujte úspěch |

Každý lokální výsledek zůstává podřízen svému rozsahu. Důkaz restartu procesu se SQLite nedokládá obnovu replikovaného úložiště. Krátký loopback běh s uzavřeným modelem zátěže nedokládá zátěž milionu uživatelů. Deterministický testovací model nedokládá kvalitu skutečného modelu. Jediná základní kontrola v Chromiu nedokládá úplnou přístupnost ani matici podporovaných prohlížečů.

## Ptejte se správně na dokončení

U konkrétního projektu určete důležité požadavky a následky selhání. Vyberte odpovídající postup dodání a brány plánovače, pak přiřaďte každé akceptační povinnosti pozorovatelný výsledek. Vedle úspěšných odpovědí kontrolujte zamítnuté účinky, uložený stav a obnovu. Zaznamenejte záměrně vynechané testy a jejich riziko místo označení celé oblasti za dokončenou na základě jednoho úspěšného příkladu.

Posuzovatel má prozkoumat tvrzení zdroje, hranici implementace, testovací orákulum, spuštěný artefakt a prostředí. Shodný otisk dokládá pouze identitu. Počty zdrojů, přeložených stránek a zelený dashboard tento řetězec nenahradí. Lokální zprávy a označení rolí nejsou podepsanými osvědčeními ani autentizovaným lidským schválením.

## Mezery udržujte explicitní

Registr pojmenovává rozšíření vyžadující další projektovou práci: nativní klienty a zařízení, regulované chování nebo chování kritické pro bezpečnost, systémy s tvrdými časovými požadavky, přepnutí při selhání mezi regiony, rozsáhlé datové a trénovací pipeline, produkční integrace identity a plateb a dlouhodobou kapacitu. Obecná doporučení mohou těmto projektům stále pomáhat, toto vydání však neobsahuje provedenou referenci pro každou specializovanou hranici.

Při rozšiřování oblasti přidejte původní doporučení, podporu zdrojů, případně referenci umožňující vyvrácení tvrzení, negativní případy, omezení a všechny čtyři jazykové verze. Změna zdroje spouští významové posouzení; nový výsledek testu náleží svým přesným vstupům. Historické zprávy uchovávejte jako datované důkazy místo tichého nahrazení jejich významu. Přijetí člověkem zůstává samostatným rozhodnutím.

## Související rozhodnutí

[Workflow agentního dodávání](project-delivery.md) · [Referenční kontroly](reference-labs.md) · [Kontroly kvality](quality.md) · [Údržba důkazů](maintenance.md)

## Primární zdroje

[github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [owasp-asvs-requirements](https://raw.githubusercontent.com/OWASP/ASVS/3383877f732ce89a458a1af43288f2f1b1d7db0c/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv)
