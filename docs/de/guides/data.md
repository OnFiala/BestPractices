---
{
  "id": "data",
  "language": "de",
  "revision": 3,
  "translation_revision": 3,
  "reviewed_on": "2026-10-22"
}
---
# Daten, Verträge und Migrationen

## Speicher anhand von Invarianten auswählen

Definiere Zugriffsmuster, Konsistenz, Aufbewahrung, Datenstandort und Wiederherstellungsbedarf vor der Technologieauswahl. Eine relationale Datenbank ist ein guter Kandidat für transaktionale Geschäftsdaten; Objektspeicher eignet sich häufig für große Binärdateien. Suchindizes und Caches enthalten abgeleitete Daten, sofern das System sie nicht ausdrücklich zur maßgeblichen Quelle erklärt. Dies sind Empfehlungen der Bibliothek, keine universellen Vorgaben.

Gib jedem Datensatz eine stabile Identität und einen Eigentümer. Benenne Eindeutigkeit, Reihenfolge und zulässige Zustandsübergänge einschließlich Löschung und Wiederherstellung. Erzwinge kritische Invarianten mit unterstützten Datenbank-Constraints und Transaktionen; alleinige Anwendungsprüfungen können durch konkurrierende Zugriffe unterlaufen werden. Verstehe das eingesetzte Isolationsniveau und wiederhole bei Bedarf eine gesamte betroffene Transaktion sicher statt eines beliebigen Teilstücks.

Die Mandantenidentität muss aus vertrauenswürdigem Autorisierungskontext stammen und Lese-, Schreib-, Export- und Hintergrundverarbeitung begleiten. Prüfe neben den Haupttabellen auch abgeleitete Sichten, Analysen, Logs und Backups. Aufbewahrungs- und Löschregeln müssen diese Kopien einschließen; die Löschung einer sichtbaren Zeile beweist nicht, dass jede Kopie entfernt wurde.

## Erweitern, migrieren, zurückbauen

| Phase | Erforderliche Entscheidung und Nachweise |
| --- | --- |
| Erweitern | Eine kompatible Darstellung ergänzen; Verhalten von Nullwerten, Standardwerten und alten Clients dokumentieren |
| Übergang | Maßgeblichen Schreiber und semantisch verlustfreies Lesen/Schreiben gemischter Versionen festlegen |
| Nachbefüllen | Begrenzte, wiederaufnehmbare Arbeit mit Checkpoints, Konfliktbehandlung sowie beobachteten Ressourcen- und Sperrgrenzen verwenden |
| Abgleichen | Geschäftliche Invarianten und repräsentative Datensätze vergleichen, nicht nur Zeilenzahlen |
| Umschalten | Verkehr bewusst auswählen, Fehler und Verzögerung beobachten und eine Abbruchbedingung beibehalten |
| Zurückbauen | Die alte Form erst entfernen, wenn alle unterstützten Clients und Worker migriert sind und die Wiederherstellung bereitsteht |

Doppeltes Schreiben ohne Konsistenzstrategie kann zwei widersprüchliche Wahrheiten erzeugen. Ein Code-Rollback macht eine destruktive Migration nicht rückgängig. Entscheide, ob die Wiederherstellung durch Rücknahme, Vorwärtskorrektur oder Wiederherstellung mit anschließendem Abgleich erfolgt, und probe den tatsächlichen Weg mit produktionsähnlichen synthetischen oder angemessen geschützten Daten.

## Parallelität und Kompatibilität testen

Führe vor einer Änderung an Schema oder öffentlichem Vertrag [Integrations- und Vertragstests](testing-strategy.md) mit alten und neuen Anwendungsversionen gegen das Übergangsschema aus. Beziehe konkurrierende Aktualisierungen, doppelte Anfragen, unterbrochene Nachbefüllung, Export mit anschließendem Import und fortgesetzte Jobs ein. In einem nützlichen Negativfall konkurrieren zwei Clients um dieselbe begrenzte Ressource; geprüft wird, ob die Invariante erhalten bleibt, nicht nur, ob eine Anfrage einen Fehler liefert.

Beobachte mit [Leistungstests](performance-testing.md) Sperren, Replikationsverzögerung, Verbindungspools und Migrationsdauer bei repräsentativem Volumen. Eine erfolgreiche Migration von zehn Zeilen belegt kein Verhalten auf dem echten Datenbestand. [Sicherheitstests](security-testing.md) müssen mandantenübergreifende Kennungen, Exportumfang und widerrufenen Zugriff nach der Aktualisierung von Indizes und Caches abdecken.

Stelle in einer isolierten Umgebung wieder her, prüfe nutzersichtbares Verhalten und gleiche externe Wirkungen ab, bevor die Verarbeitung fortgesetzt wird. Miss Wiederherstellungszeit und tatsächlichen Datenverlust gegenüber den vereinbarten RTO-/RPO-Zielen und dokumentiere Backup- und Artefaktversionen. Eine Replik kann versehentliche Löschungen mitreplizieren; sie ersetzt keine getestete Wiederherstellungskopie.

## Das Modell neu bewerten

Versioniere einen Vertrag, wenn Verbraucher koordiniert werden müssen; ändere Einheiten, Nullwertverhalten, Kennungen oder Bedeutung niemals stillschweigend. Führe eine weitere Datenbank nur für eine gemessene Anforderung ein, die Konsistenz-, Sicherungs- und Fachwissensaufwand rechtfertigt. Partitionierung benötigt ausdrückliche Regeln für Routing, Verantwortung und partitionsübergreifende Operationen. Separate Lesemodelle können bei nachgewiesenen Abfrageanforderungen helfen, benötigen bei asynchroner Aktualisierung aber einen Aktualitätsvertrag.

## Verwandte Entscheidungen

[Beständigkeit](durability.md) · [Sicherheit](security.md) · [Skalierung](scaling.md) · [Teststrategie](testing-strategy.md) · [Leistungstests](performance-testing.md)

## Primärbelege

[pekko-cqrs](https://raw.githubusercontent.com/apache/pekko-projection/d1bcc1ed09efd8a11ce3dca0a7edea306dff6e02/docs/src/main/paradox/use-cases.md) · [postgres-partitioning](https://raw.githubusercontent.com/postgres/postgres/5681f0cfa5acfdc5146e2b74ff5b7e940df039f3/doc/src/sgml/ddl.sgml) · [rabbitmq-reliability](https://raw.githubusercontent.com/rabbitmq/rabbitmq-website/483c5f73095c3d808e98840e50c1ed5f2b148369/docs/reliability.md) · [pekko-event-sourcing](https://raw.githubusercontent.com/apache/pekko/0b963c40b68bfb8788f91a265a13f6ce38947b63/docs/src/main/paradox/typed/persistence.md) · [debezium-outbox](https://raw.githubusercontent.com/debezium/debezium/d67bfa5a10efac6eb74c0d62f43777b1198ad454/documentation/modules/ROOT/pages/quarkus/outbox.adoc) · [owasp](https://raw.githubusercontent.com/OWASP/ASVS/2b47a9dd16760ee484a6672d197f1f7e25d9c632/README.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml)
