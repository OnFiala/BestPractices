---
{
  "id": "maintenance",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Důkazy a automatická údržba

## Tok důkazů

`data/sources.json` odděluje neměnný prozkoumaný zdroj od URL sledované kvůli pozdějším změnám. Zaznamenává vydavatele, rozsah, interval posuzování a licenční podklady. Výchozí stav načtení zaznamenává úspěšné hashe, nikoli lidské schválení. Plánovaný pozorovatel načítá dokumenty přes HTTPS s limity a hlásí změněné, nedostupné nebo k posouzení opožděné zdroje. Změněný hash je signálem k posouzení, nikdy oprávněním změnit doporučení. Neúspěšné načtení zůstává nedostupné; není označeno jako beze změny.

Workflow zdrojů vytváří nebo aktualizuje PR s důkazy, když je nutná reakce. Nemění přijatý výchozí stav a neslučuje změny. Člověk přečte relevantní diff zdroje, ověří tvrzení a použitelnost a rozhodne, zda společně aktualizovat průvodce, překlady, data posouzení a výchozí stav. Datum posouzení neposouvejte jen proto, že URL vrátila HTTP 200.

## Aktualizace s pomocí agentů

Veřejný repozitář sleduje metadata zdrojů. Generování modelem a úlohy navrhující změny na základě zdrojů jsou omezeny na samostatný soukromý repozitář, zrcadlo nebo pracovní prostor: logy, shrnutí, patche a artefakty mohou obsahovat původní zdrojový text před kontrolou práv. Volitelný soukromý Codex workflow vyžaduje nastavené tajemství a explicitní zapnutí; lokální validace a kontroly zdrojů nepotřebují placené API. Model vrací ohraničená strukturovaná data návrhu. Čerstvě spuštěný důvěryhodný konzument tato data validuje namísto spuštění skriptu vytvořeného agentem nebo důvěry v agentova Git metadata.

Člověk před přenesením schváleného obsahu do veřejného PR posoudí soukromý výstup z hlediska vlastního vyjádření, licencování, citlivých dat, důkazů a významu překladů. Automatický přenos na veřejnost neexistuje. Pište nezávislá vysvětlení a příklady; nekopírujte ani nepřekládejte zdrojové texty a těsně neparafrázujte jejich osobité vyjádření. Povinná oznámení k softwaru třetích stran zůstávají pod vlastními licencemi. Citace zdroje ani kontrola podobnosti neudělují práva k převzetí.

Agent nemá pravomoc schvalovat, slučovat ani zveřejňovat. Sady pravidel a povinné posouzení stále vyžadují skutečné nastavení na GitHubu; soubor workflow je nevynucuje. Soukromá generovací služba nebyla v rámci této knihovny nasazena.

## Aktuálnost a selhání

Rychle se měnící zdroje k AI a protokolům kontrolujte častěji než stabilní principy. Označujte experimenty a vyřazované postupy, zachovávejte migrační odkazy a zaznamenávejte sporná doporučení. Chybějící přihlašovací údaje, blokované sítě, neúspěšné kontroly a zastaralé překlady zůstávají viditelnými překážkami. Sledujte dobu překročení termínu posouzení a čas řešení změn zdrojů. Chybné doporučení vraťte commitem a posuďte projekty, které je přijaly.

README ani index vkládající jiné soubory nepovažujte za pokrytí podkladové specifikace. Zaregistrujte konkrétní věcnou kontrolu nebo mechanismus, o který se skutečně opíráte. Mapování tvrzení musí oddělovat chování podložené zdrojem od místní syntézy, zaznamenávat použitelnost a zůstávat svázané s posouzenou verzí. Před přijetím AI platformy obnovte podklady o životním cyklu produktu; metodika může zůstat užitečná i po ukončení produktu použitého v jejím příkladu.

## Související rozhodnutí

[GitHub, verze a čisté stromy](github.md) · [Člověk určuje směr, agent vykonává](agents.md) · [Správa a nezodpovězená rozhodnutí](governance.md)

## Primární zdroje


[codex-action](https://raw.githubusercontent.com/openai/codex-action/c05cfd74ad95c626cdf05c6685e62becc3bf7813/README.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md)
