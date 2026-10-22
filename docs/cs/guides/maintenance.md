---
{
  "id": "maintenance",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Důkazy a automatická údržba

## Tok důkazů

`data/sources.json` eviduje primární zdroje, rozsah, datum a interval kontroly. Baseline obsahuje hashe úspěšných stažení. Plánovaný pozorovatel stahuje omezené HTTPS dokumenty a hlásí změny, nedostupnost a stáří. Změna hashe žádá kontrolu, nepovoluje přepis. Chyba stažení není shoda.

Workflow vytváří nebo obnovuje důkazní PR při potřebě zásahu. Nemění přijatou baseline ani neslučuje. Člověk přečte změnu zdroje, ověří tvrzení a použitelnost a rozhodne o společné aktualizaci průvodců, překladů, dat kontroly a baseline. HTTP 200 samo neobnovuje datum věcného posouzení.

## Agentní aktualizace

Volitelný Codex workflow navrhuje omezené změny dokumentace. Vyžaduje GitHub secret a výslovné zapnutí; místní validace a zdroje placené API nepotřebují. Agent smí měnit existující překlady a katalog. Samostatný job otevře draft PR; agent neslučuje. Rulesety a lidské review je nutné aktivovat na GitHubu.

## Platnost a chyby

Rychlé AI/protokoly kontrolujte častěji než stabilní principy. Označujte experimenty, deprecace a sporné rady, zachovejte migrační odkazy. Chybějící přístupy, síť, neúspěšné testy a staré překlady zůstávají viditelné. Měřte zpoždění posouzení a vyřešení změn. Chybné doporučení vraťte commitem a posuďte užívající projekty.

## Související rozhodnutí

[GitHub, verze a čisté stromy](github.md) · [Člověk řídí, agent vykonává](agents.md) · [Správa a otevřená rozhodnutí](governance.md)

## Primární zdroje

[codex-action](https://raw.githubusercontent.com/openai/codex-action/main/README.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/main/content/actions/reference/security/secure-use.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md)
