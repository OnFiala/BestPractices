---
{
  "id": "operations",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Zustand, Wiederherstellung und Kosten

## Nutzerergebnisse beobachten

SLIs messen sichtbaren Erfolg oder Latenz, SLOs Ziele in einem definierten Fenster. Ziele aus Bedarf und Messung ableiten, keine modischen Prozente übernehmen. Fehlerbudgets steuern Freigaberisiken, entschuldigen keine Vorfälle. Readiness und Liveness trennen, damit kurze Abhängigkeitsfehler keine Neustartwellen auslösen.

Strukturierte Logs, Metriken und Traces mit Korrelationskennungen verwenden; Kardinalität und persönliche Daten begrenzen. Alarme brauchen handlungsfähige Symptome, Verantwortung, Schweregrad, Runbook und Eskalation. Dashboards ersetzen keine Alarme. Kosten pro nützlicher Transaktion und Agentenaufgabe einschließlich Wiederholungen und Tokens messen.

## Reaktion und Wiederherstellung

Vorfallleitung bestimmen, Auswirkungen begrenzen, Belege sichern, kommunizieren und Dienst herstellen. Anschließend Ursachen und verantwortete Maßnahmen ohne Schuldzuweisung dokumentieren. Backups, Rotation und Anbieterausfälle üben. Letzte erfolgreiche Wiederherstellung sowie gemessene RTO/RPO festhalten.

## Prüfrhythmus

Wöchentlich Alarme, Quellenänderungen, Abhängigkeiten und Kosten prüfen. Monatlich Ziele, Wiederherstellungsnachweise, Verantwortung und Kapazität. Vierteljährlich oder nach großen Änderungen Bedrohungen, Notfallplan, Architektur und Stilllegungskandidaten. Diese Ausgangsrhythmen sind anpassbar. Gesundheit zeigt sich in Verhalten und Wiederherstellung, nicht nur laufenden Prozessen.

## Verwandte Entscheidungen

[Beständigkeit und verteilte Arbeit](durability.md) · [Anhand von Messungen skalieren](scaling.md) · [Der vollständige Projektlebenszyklus](lifecycle.md)

## Primärbelege

[observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml)
