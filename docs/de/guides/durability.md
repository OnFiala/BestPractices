---
{
  "id": "durability",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Beständigkeit und verteilte Arbeit

## Was überleben muss

Datenpersistenz, Dienstverfügbarkeit und Wiederaufnahme von Arbeit unterscheiden. Eine Replik ist kein Backup; eine Warteschlange garantiert keine genau einmalige Geschäftswirkung. Akzeptierten Datenverlust (RPO) und Wiederherstellungszeit (RTO) je Geschäftsfähigkeit festlegen. Das sind Geschäftsentscheidungen, keine Produkteigenschaften eines Namens.

## Zuverlässige Ausführung

- Stabile Idempotenzschlüssel auf Mandant und Aktion begrenzen. Ergebnis oder Zustandswechsel mit Eindeutigkeitsconstraint speichern; Ablauf und abweichende Nutzlast definieren.
- Timeouts und Wiederholungen begrenzen. Nur geeignete Fehler mit exponentieller Pause, Jitter und Gesamtfrist wiederholen; Validierungsfehler gesondert behandeln.
- Geschäftszustand und Outbox-Eintrag gemeinsam transaktional speichern. Veröffentlichung kann Duplikate erzeugen; Verbraucher deduplizieren und definierte Reihenfolge behandeln.
- Fortschritt langer Arbeit speichern. Abbruch, Kompensation und manuelle Abstimmung festhalten. Kompensation ist eine neue Geschäftsaktion, keine garantierte Rücknahme externer Wirkung.
- Fehlerhafte Nachrichten isolieren; Replay autorisieren, beobachten, begrenzen und duplikatsicher gestalten. Schemakompatibilität und Deduplikationsfrist bestimmen.

## Fehlerbeispiel

Eine Bestellung wird gespeichert, der Prozess stirbt vor dem Ereignisversand. Die Outbox setzt fort. Ist eine Zahlung erfolgreich, aber ihre Antwort verloren, Anbieter-Idempotenz verwenden und dessen Zustand vor Wiederholung abgleichen. Ein lokaler Schlüssel garantiert keine einmalige externe Zahlung.

## Prüfen und vereinfachen

Worker vor und nach dauerhaften Grenzen beenden; Nachrichten doppelt und vertauscht zustellen. Isoliert wiederherstellen und Summen abgleichen. Eine Workflow-Engine einsetzen, wenn sie belegte Fehlerkomplexität reduziert; Upgrades laufender Abläufe testen. Bei akzeptabler manueller Wiederholung kann eine transaktionale Jobtabelle genügen.

## Verwandte Entscheidungen

[Daten, Verträge und Migrationen](data.md) · [Zustand, Wiederherstellung und Kosten](operations.md) · [Architekturen auswählen und verbinden](architecture.md)

## Primärbelege

[postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml) · [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/main/README.md)
