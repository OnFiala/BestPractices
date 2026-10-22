---
{
  "id": "github",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# GitHub, verze a čisté stromy

## Přehledný tok

Udržujte `main` vydatelnou. Jedna změna patří na krátkou větev a do srozumitelných commitů. Commitujte smysluplný ověřitelný krok; nečekejte na celý projekt a nepřidávejte tajemství ani cache. Prefixy `feat:`, `fix:`, `docs:` jsou místní dohoda, ne náhrada vysvětlení.

PR obsahuje problém, chování, důkazy, rizika a návrat. Kontrolujte konečný diff, ne jen souhrn agenta. Vyžadujte checks, vhodné code-owner review, vyřešené diskuse a nové schválení významných změn. Agent neschvaluje ani neslučuje vlastní práci. Ruleset má zakázat force-push, mazání a přímé změny `main`; soubory ho samy nezapnou.

SemVer použijte pro určenou veřejnou smlouvu. Tagujte vědomá vydání s changelogem a migrací; tag tiše nenahrazujte. Každý commit nemusí být release. ID průvodců a metadata této knihovny jsou smlouva: nekompatibilní změna vyžaduje migraci a rozhodnutí o verzi.

## Čistota

Před úpravou čtěte status a chraňte cizí práci. Ignorujte generované výstupy, kontrolujte staging i smazání. Nepoužívejte plošný reset/clean. Sloučené větve smažte po ověření místních commitů; reference prořezávejte zvlášť. Worktree v cloudu jen při výslovném zadání. Opuštěné větve mají vlastníka a termín.

## Související rozhodnutí

[Kontroly kvality dokazující chování](quality.md) · [Člověk řídí, agent vykonává](agents.md) · [Důkazy a automatická údržba](maintenance.md)

## Primární zdroje

[github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/main/content/actions/reference/security/secure-use.md) · [semver](https://raw.githubusercontent.com/semver/semver/master/semver.md)
