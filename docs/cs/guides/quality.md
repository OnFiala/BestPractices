---
{
  "id": "quality",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Kontroly kvality dokazující chování

## Testujte smlouvu, ne kopii implementace

Zelený formatter nedokazuje funkční produkt. Volte testy podle následků: jednotkové pro pravidla, integrační pro databázi a hranice služeb, smluvní pro spotřebitele a několik úplných průchodů. Zahrňte zamítnutí přístupu, vadný vstup, timeout, duplicitu a obnovu. Používejte syntetická data a izolujte externí účinky.

## Brána dodání

Vyžadujte opakovatelnou instalaci, vhodné build/type kontroly, smysluplné testy a review skutečného diffu. Rozlišujte úspěch, chybu, přeskočení a nespuštění. Neoslabujte assertion kvůli vydání. Nestabilní test má vlastníka a termín karantény, nesmí potichu zmizet.

U AI práce zkoumejte, zda test odhalí navrženou chybu. Nezávislý reviewer ověřuje předpoklady a negativní případy. Snapshot potřebuje významové kontroly; samotné procento pokrytí kvalitu nedokazuje.

## Tato knihovna

Spouštějte validátor, Python testy, lint a přísné sestavení čtyř jazyků. Kontrola odmítá chybějící překlady, staré revize, neznámé zdroje a rozbité odkazy. Síťový monitoring zdrojů je oddělený; CI nedokazuje faktickou správnost ani kvalitu překladu.

## Přezkoumání

Sledujte uniklé chyby, neúspěšná nasazení, obnovu a pomalé kontroly. Odstraňujte nadbytečné testy bez přínosu, zachovejte důkazy závažných cest. O dostatečnosti rozhoduje člověk.

## Související rozhodnutí

[GitHub, verze a čisté stromy](github.md) · [Člověk řídí, agent vykonává](agents.md) · [Celý životní cyklus projektu](lifecycle.md)

## Primární zdroje

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [wcag](https://raw.githubusercontent.com/w3c/wcag/main/guidelines/index.html) · [github-workflows](https://raw.githubusercontent.com/github/docs/main/content/actions/reference/security/secure-use.md)
