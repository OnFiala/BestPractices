---
{
  "id": "scaling",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Škálování podle měření

## Měřte před rozdělováním

Registrovaní uživatelé neměří kapacitu. Zaznamenejte souběžnost, špičkový příchod požadavků, velikost dat, poměr čtení/zápisů, nerovnoměrnost tenantů, percentily latence a práci na pozadí. Nejprve stanovte cíl služby a rozpočet.

## Pořadí kroků

1. Profilujte skutečnou zátěž; opravte drahé dotazy, indexy, neomezené seznamy a zbytečná volání.
2. U cache určete čerstvost, invalidaci, izolaci tenantů a chování při souběžném naplnění. Měřte zásahy i zátěž originu.
3. Přidejte omezené workery, zpětný tlak a kvóty. Bezpečně odmítejte práci před zhroucením závislostí.
4. Replikujte bezstavové procesy; vhodně přesuňte relace a soubory. Databázové connection pooly počítejte za všechny repliky.
5. Čtecí repliky vyžadují smlouvu o zastaralých datech. Data dělte po změření limitu a návrhu směrování, přesunů a operací přes oddíly.

## Ověření

Testujte reálné rozložení, špičku, pomalou závislost i zotavení. Sledujte propustnost, p95/p99, chyby, stáří fronty, saturaci a cenu užitečné operace. Souběžnost odhadněte jako příchody × dobu obsluhy a ověřte zátěží.

Škálujte při trvalém porušování cíle nebo doloženém úbytku rezervy. Uchovejte výchozí měření a návrat. Autoscaling omezují závislosti, starty, kvóty a cena; neopraví neefektivní transakci.

## Související rozhodnutí

[Hosting a cesta k migraci](hosting.md) · [Data, smlouvy a migrace](data.md) · [Zdraví, obnova a náklady](operations.md) · [Volba a propojení architektur](architecture.md)

## Primární zdroje

[observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md) · [kubernetes](https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/concepts/architecture/_index.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml)
