---
{
  "id": "architecture",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Architekturen auswählen und verbinden

## Nach Kopplung und Verantwortung wählen

| Ansatz | Geeignet, wenn | Kosten und Änderungssignal |
| --- | --- | --- |
| Statische Seite | Inhalt selten wechselt, keine Servergeheimnisse nötig sind | Bau- und Redaktionsprozess; Backend für vertrauenswürdige Schreibvorgänge |
| Modularer Monolith | Ein Produkt/Team Transaktionen und schnelle Änderungen braucht | Grenzen erzwingen; gemessenen Engpass oder eigenständige Verantwortung ausgliedern |
| Serverless-Funktionen | Kurze, stoßweise Arbeit in Anbieterlimits passt | Kaltstarts, Quoten, Tracing und Bindung |
| Dienste | Teams oder Lasten unabhängig veröffentlichen müssen | Netzfehler, Verträge, Konsistenz und Bereitschaft |
| Ereignisorientiert | Verzögerte Arbeit und unabhängige Verbraucher passen | Duplikate, Reihenfolge, Replay, Schemaentwicklung und Fehlersuche |
| Dauerhafte Workflows | Lange Geschäftsabläufe nach Fehlern weiterlaufen müssen | Determinismus, Versionierung, Betrieb und Migration |

Die Ansätze sind kombinierbar. Ein modularer Monolith kann ein statisches Frontend bedienen, Worker einsetzen und später eine Domäne ausgliedern. Hexagonale/Clean Architecture regelt Abhängigkeitsrichtungen innerhalb einer Komponente und verlangt keine Microservices. CQRS trennt Lese- und Schreibmodelle bei unterschiedlichen Anforderungen. Event Sourcing speichert zusätzlich Ereignisse als Wahrheit und benötigt Replay- und Aufbewahrungsregeln.

## Grenzen

Browser, API, Worker, Datenbank, Anbieter und Vertrauensgrenzen zeichnen. Jedes Modul besitzt seine Schreibvorgänge; andere nutzen eine explizite Schnittstelle. Gemeinsame Bibliotheken klein halten. Unbeschränkte Schreibzugriffe mehrerer Dienste auf eine Datenbank schwächen unabhängige Verantwortung.

## Prüfen und weiterentwickeln

Einen grenzüberschreitenden Fehler und eine Vertragsänderung testen. Lieferzeit, Abhängigkeitszyklen, Transaktionskonflikte und Wiederherstellungsaufwand messen. Einen Dienst erst ausgliedern, wenn der Nutzen Betriebs- und Konsistenzkosten übersteigt. Migration und Stilllegung des alten Pfads dokumentieren; ein Diagramm allein ist kein Umsetzungsplan.

## Verwandte Entscheidungen

[Beständigkeit und verteilte Arbeit](durability.md) · [Frontendarchitektur und Verträge](frontend.md) · [Anhand von Messungen skalieren](scaling.md) · [Hosting und Ausstiegswege](hosting.md)

## Primärbelege

[kubernetes](https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/concepts/architecture/_index.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml) · [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/main/README.md)
