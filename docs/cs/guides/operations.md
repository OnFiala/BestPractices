---
{
  "id": "operations",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Zdraví, obnova a náklady

## Sledujte výsledek uživatele

SLI vyjadřuje úspěch nebo latenci, SLO cíl v určeném okně. Cíle odvoďte od potřeb a měření, nekopírujte módní procento. Chybový rozpočet pomáhá řídit vydávání, ne ignorovat incidenty. Oddělte readiness a liveness, aby krátký výpadek závislosti nevyvolal bouři restartů.

Používejte strukturované logy, metriky a traces s korelačními ID; omezte kardinalitu a osobní data. Alarm musí mít řešitelný příznak, vlastníka, závažnost, runbook a eskalaci. Dashboard nenahrazuje alarm. Měřte cenu užitečné transakce i agentního úkolu včetně opakování a tokenů.

## Reakce a obnova

Určete vedení incidentu, omezte dopad, zachovejte důkazy, komunikujte a obnovte službu. Následuje neobviňující rozbor a opatření s vlastníkem. Cvičte obnovu záloh, rotaci i výpadek poskytovatele. Zapisujte poslední úspěšnou obnovu a naměřené RTO/RPO.

## Rytmus kontroly

Týdně: alarmy, změny zdrojů, závislosti a cena. Měsíčně: cíle služby, důkazy obnovy, odpovědnost a kapacita. Čtvrtletně či po velké změně: hrozby, havarijní obnova, architektura a kandidáti na ukončení. Jsou to upravitelné počáteční rytmy. Zdraví dokazuje chování a obnova, nikoli pouze běžící procesy.

## Související rozhodnutí

[Odolnost a distribuovaná práce](durability.md) · [Škálování podle měření](scaling.md) · [Celý životní cyklus projektu](lifecycle.md)

## Primární zdroje

[observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml)
