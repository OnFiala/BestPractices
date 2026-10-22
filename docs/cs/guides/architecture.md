---
{
  "id": "architecture",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Volba a propojení architektur

## Rozhodujte podle vazeb a odpovědnosti

| Přístup | Kdy použít | Náklad a signál změny |
| --- | --- | --- |
| Statický web | Obsah se mění pomaleji než požadavky, bez serverových tajemství | Sestavení a redakce; backend pro důvěryhodné zápisy |
| Modulární monolit | Jeden produkt/tým potřebuje transakce a rychlé změny | Vynucujte hranice; oddělujte změřené omezení nebo samostatnou odpovědnost |
| Serverless funkce | Nárazové omezené úlohy vyhovují limitům poskytovatele | Studené starty, kvóty, trasování, závislost na dodavateli |
| Služby | Týmy nebo zátěže potřebují samostatná vydání a izolaci | Síťová selhání, smlouvy, konzistence a pohotovost |
| Událostní systém | Odložená práce a nezávislí odběratelé | Duplicity, pořadí, replay, vývoj schémat a ladění |
| Durable workflow engine | Dlouhé obchodní kroky musí pokračovat po selhání | Determinismus, verze, provoz a migrace workflow |

Volby lze kombinovat. Modulární monolit může obsluhovat statický frontend, používat workery a později oddělit doménu. Hexagonální/clean architektura řídí směr závislostí uvnitř komponenty; nevyžaduje mikroslužby. CQRS rozděluje model čtení a zápisu při rozdílných potřebách. Event sourcing navíc ukládá události jako zdroj pravdy a potřebuje plán přehrávání a retence.

## Hranice

Zakreslete prohlížeč, API, worker, databázi, poskytovatele a hranice důvěry. Modul vlastní zápisy; ostatní přistupují přes smlouvu. Sdílené knihovny držte malé. Neomezené zápisy více služeb do společné databáze narušují samostatnou odpovědnost.

## Ověření a vývoj

Otestujte selhání přes hranici a změnu smlouvy. Sledujte dobu dodání, cykly závislostí, konflikty transakcí a náročnost obnovy. Službu oddělte teprve tehdy, když přínos překoná cenu nasazování, konzistence a podpory. Zapište migraci spotřebitelů a odstranění původní cesty; samotný diagram není plán implementace.

## Související rozhodnutí

[Odolnost a distribuovaná práce](durability.md) · [Architektura frontendu a smlouvy](frontend.md) · [Škálování podle měření](scaling.md) · [Hosting a cesta k migraci](hosting.md)

## Primární zdroje

[kubernetes](https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/concepts/architecture/_index.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml) · [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/main/README.md)
