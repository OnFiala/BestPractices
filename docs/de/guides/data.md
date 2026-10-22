---
{
  "id": "data",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Daten, Verträge und Migrationen

## Explizite Invarianten

Speicher nach Zugriffsmustern, Konsistenz, Aufbewahrung und Wiederherstellung wählen. Relationale Datenbanken eignen sich als Ausgangspunkt für transaktionale Geschäftsdaten; Objektspeicher für große Dateien. Suchindizes und Caches sind abgeleitete Ansichten, sofern nicht anders geplant. Identitäten, Eigentum, Eindeutigkeit und Löschung vor dem Framework klären.

Constraints und Transaktionen schützen Invarianten. Isolationsniveau verstehen und Serialisierungsfehler sicher wiederholen. Mandantenautorisierung gilt für jeden Zugriff; fremde IDs, Exporte und Hintergrundjobs testen. Auch Logs, Analyse und Backups brauchen Aufbewahrungsregeln.

## Erweitern, migrieren, entfernen

Zuerst kompatibles Schema hinzufügen. Leser und Schreiber mit beiden Formen betreiben, begrenzt und fortsetzbar nachfüllen, Konsistenz messen und alte Form nach Verbrauchermigration entfernen. Reale Datenmengen und Sperren prüfen. Code-Rollback macht destruktive Datenmigrationen nicht rückgängig; Vorwärtsreparatur und getestete Wiederherstellung vorsehen.

## Prüfen

Alte/neue Versionen, doppelte Anfragen, Parallelität, Export/Import und Wiederherstellung testen. RPO/RTO messen. Öffentliche Verträge bei Koordinationsbedarf versionieren; Einheiten, Nullbarkeit und Bedeutung nicht still ändern. Eine weitere Datenbank benötigt einen gemessenen Nutzen, der Betriebs- und Konsistenzkosten rechtfertigt.

## Verwandte Entscheidungen

[Beständigkeit und verteilte Arbeit](durability.md) · [Sicherheit, Datenschutz und Lieferkette](security.md) · [Anhand von Messungen skalieren](scaling.md)

## Primärbelege

[postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml) · [owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md)
