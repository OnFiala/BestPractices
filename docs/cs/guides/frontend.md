---
{
  "id": "frontend",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Architektura frontendu a smlouvy

## Renderování podle interakce

Statické generování použijte pro obsah, serverové při důležité čerstvosti či indexaci, klientské pro dlouhou interakci. Hybridní renderování rozhodujte po routách. Zapište hydrataci, cache, autentizaci a nasazování. Mikrofrontendy řeší nezávislou odpovědnost týmů, nejsou výchozí model komponent.

## Srozumitelný stav

Oddělte serverová data, URL/navigaci, místní interakci a trvalé preference. Každý stav má jasného vlastníka; nekopírujte serverová data do několika úložišť. Strukturu veďte podle funkcí produktu a smluv. Nejprve sdílejte přístupné primitivy, až potom rozsáhlý design systém.

Definujte schémata API, chyby, stránkování, rušení a zastaralá data. Server validuje vstupy a autorizuje každou chráněnou akci. Skryté tlačítko není oprávnění. Serverová tajemství nepatří do klientského balíku. Rušte efekty a uklízejte odběry; optimistické změny potřebují cestu selhání a sladění.

## Ověření a vývoj

Testujte klávesnici, fokus, přístupné názvy, kontrast, načítání, prázdný stav, chyby, offline a úzký displej. Měřte navigaci, velikost dat, odezvu a JS chyby. BFF přidejte při doložené agregaci nebo bezpečnostní hranici. Framework měňte, když omezení převáží cenu migrace včetně přístupnosti a podpory. WebMCP je doplněk: běžná obsluha musí fungovat i bez něj.

## Související rozhodnutí

[Volba a propojení architektur](architecture.md) · [Kontroly kvality dokazující chování](quality.md) · [Skills, pluginy, MCP a WebMCP](integrations.md)

## Primární zdroje

[wcag](https://raw.githubusercontent.com/w3c/wcag/main/guidelines/index.html) · [owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/main/README.md)
