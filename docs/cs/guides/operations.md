---
{
  "id": "operations",
  "language": "cs",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Zdraví systému, obnova a náklady

## Sledujte uživatelský výsledek

Zvolte ukazatel úrovně služby (SLI) pro smysluplný uživatelský scénář, například úspěšné dokončení v rámci limitu latence. Definujte jeho čitatele, jmenovatele, časové okno sledování a výjimky a poté s vlastníkem dohodněte cíl úrovně služby (SLO). Zahrňte neúspěšnou i odmítnutou práci, pokud to kontrakt vyžaduje; rychlá chyba není úspěšná transakce.

Chybový rozpočet vyjadřuje povolené nesplnění cíle v tomto okně. Pro ilustraci: cíl založený na požadavcích ve výši 99,9 % ze 100 000 započítaných požadavků připouští 100 požadavků mimo cíl; jde o aritmetický příklad, nikoli doporučenou hodnotu. Pozorovanou rychlost čerpání a obchodní dopad používejte k úpravě rizika při vydávání. Pravidla reakce definujte před incidentem, místo abyste vyčerpaný rozpočet chápali jen jako barvu na přehledu.

Tento provozní model je syntézou knihovny. Citované materiály o pozorovatelnosti a zdravotních koncových bodech podporují mechanismy měření; četnost kontrol a eskalační prahy zůstávají rozhodnutími projektu.

## Oddělujte signály zdraví

| Signál | Účel a omezení |
| --- | --- |
| Spuštění (startup) | Umožnit dokončení inicializace v explicitním limitu |
| Živost (liveness) | Odhalit proces, který nedokáže pokračovat; restart musí být užitečnou reakcí |
| Připravenost (readiness) | Rozhodnout, zda má instance přijímat konkrétní provoz |
| Syntetický uživatelský scénář | Ověřit chování viditelné uživateli přes řízené veřejné rozhraní |
| Metriky a traces služby | Vysvětlovat výsledky, saturaci a podíl závislostí v čase |

Nedovolte, aby každé přechodné selhání závislosti způsobilo selhání kontroly živosti a restart zdravých procesů. Hluboké kontroly připravenosti mohou při výpadku sdílené závislosti také vyřadit všechny instance; definujte omezený režim a limity specifické pro jednotlivé závislosti. Zdravotní sondy nesmějí vyčerpat prostředky, které měří. Podrobné diagnostické údaje chraňte a zabraňte tomu, aby sondy vyvolávaly skutečné platby nebo zprávy.

Používejte strukturované logy, metriky a traces s korelačními identifikátory, omezenou kardinalitou štítků a redakcí citlivých dat. Upozorňujte na příznaky vyžadující konkrétní reakci nebo soustavné čerpání chybového rozpočtu; uveďte závažnost, vlastníka, provozní postup a eskalaci. Ověřte, že upozornění dorazí někomu, kdo může reagovat. Samotný přehled nebo HTTP 200 nedokládá dostupnost.

## Proveďte nácvik incidentu a obnovy

Určete vedoucího incidentu, zjistěte dopad na uživatele, stabilizujte systém, uchovejte potřebné důkazy a sdělujte nejistoty. Vypněte riziková opakování nebo akce agentů, pokud zvětšují škodu. Dejte přednost známému bezpečnému postupu obnovy před neotestovanou nouzovou změnou návrhu. Po obnovení sjednoťte trvalou práci a účinky u poskytovatelů před opětovným spuštěním automatizace.

V izolovaném prostředí obnovte zálohu, odvolejte nebo obměňte přihlašovací údaje a simulujte nedostupného poskytovatele. Změřte dobu obnovy a interval ztracených dat, pak ověřte skutečný uživatelský scénář a obchodní invarianty. Pro pozorovatelné chování použijte [black-box kontroly](testing-strategy.md) a pro zpracování nahromaděné práce po saturaci [testy výkonu a obnovy](performance-testing.md). Zaznamenejte skutečné výsledky, verze artefaktů a zbývající ruční kroky.

Po incidentu zaznamenejte přispívající okolnosti a opatření s vlastníky a termíny. Přidejte regresní test, pokud dokáže prokázat opravené chování. Zachovejte užitečné provozní poznatky bez zveřejnění osobních údajů nebo přihlašovacích údajů.

## Zviditelněte odpovědnost a výdaje

Měřte náklady na užitečnou transakci a úkol agenta včetně opakování, tokenů, odchozích dat a pozorovatelnosti. Definujte upozornění a vynucené zastavení nebo omezení funkčnosti; samotné e-mailové varování není výdajovým stropem. Pravidelně kontrolujte nevyřešená upozornění, změny zdrojů a závislostí a výdaje. Po podstatných změnách posuďte cíle, kapacitu a důkazy obnovy; zvolte pravidelný rytmus, který vlastník dokáže udržet.

Systém je zdravý, pokud jeho vlastníci dokážou prokázat chování, obnovu a udržitelnou provozní odpovědnost. Více replik nenahradí vlastníka a jediný testovací běh nezaručuje budoucí spolehlivost.

## Související rozhodnutí

[Odolnost](durability.md) · [Škálování](scaling.md) · [Životní cyklus](lifecycle.md) · [Strategie testování](testing-strategy.md) · [Výkonnostní testování](performance-testing.md)

## Primární zdroje


[observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [azure-health-endpoints](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/health-endpoint-monitoring.md)
