---
{
  "id": "github",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# GitHub, verze a čisté stromy

## Postup, který lze posoudit

Udržujte `main` připravený k vydání. Pro jednu změnu používejte krátkodobé větve a malé soudržné commity, které vysvětlují záměr. Commitujte, když lze smysluplný přírůstek pochopit a ověřit; nečekejte na celý projekt a necommitujte vygenerované tajné údaje ani cache. `feat:`, `fix:` a `docs:` jsou užitečné místní konvence, nikoli náhrada jasného popisu.

Otevřete PR s problémem, chováním, důkazy, riziky a návratem zpět. Posuzujte konečný diff, nikoli pouze shrnutí agenta. Vyžadujte stavové kontroly, posouzení vlastníkem kódu tam, kde je relevantní, vyřešené diskuse a nové schválení po významných změnách. Agenti nikdy neschvalují ani neslučují svou vlastní práci. Nastavte sadu pravidel blokující force-push, mazání a přímé změny větve `main`; samotné soubory ji neaktivují.

SemVer používejte pro definovaný veřejný kontrakt. Záměrná vydání označujte tagy, publikujte přehled změn a migrační poznámky a nikdy potichu nenahrazujte tag vydání. Interní commity nemusejí být vydáními. V této knihovně jsou identifikátory průvodců a metadata kontrakty: jejich nekompatibilní změna vyžaduje migraci a rozhodnutí o verzi.

## Čistota

Před úpravami zkontrolujte stav a zachovejte ostatní práci. Generované výstupy ignorujte; před commitem posuďte připravené soubory a nechtěná smazání. Nikdy nepoužívejte plošné příkazy reset nebo clean. Sloučené větve smažte až po ověření, že neobsahují práci existující pouze lokálně; reference promazávejte samostatně. Worktrees v tomto cloudovém prostředí používejte pouze v případě potřeby a na výslovnou žádost. Opuštěné větve evidujte s vlastníkem a koncem platnosti.

## Související rozhodnutí

[Kontroly kvality prokazující chování](quality.md) · [Člověk určuje směr, agent vykonává](agents.md) · [Důkazy a automatická údržba](maintenance.md)

## Primární zdroje


[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [semver](https://raw.githubusercontent.com/semver/semver/f99d5485190a47c0863949e7da810a5553e0ed4d/semver.md)
