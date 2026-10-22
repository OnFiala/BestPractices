---
{
  "id": "hosting",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Hosting und Ausstiegswege

## Die gesamte Verpflichtung vergleichen

Beginne mit Datenklassifikation und Datenstandort, Lastprofil, Wiederherstellungszielen, verfügbaren Betreibern und Budget. Der folgende Vergleich ist eine eigenständige Auswahlhilfe der Bibliothek. Die Produktdokumentation muss aktuelle Angaben zu Regionen, Quoten, Support und Preisen für die konkrete Bereitstellung liefern; eine Produktkategorie ist keine Dienstgarantie.

| Option | Geeigneter Einsatz | Zu prüfende Kosten und Verantwortung |
| --- | --- | --- |
| Statisches Hosting/CDN | Öffentliche Dokumentation und unveränderliche Dateien | Build-Grenzen, Cache-Regeln, Domainkontrolle und Ausschluss privater Ausgaben |
| Verwaltete Anwendungsplattform | Ein kleines Team stellt eine Anwendung bereit | Unterstützte Laufzeiten, Netzwerk, Sicherungsumfang, Export und ausgehender Datentransfer |
| Verwaltete Funktionen | Begrenzte, schubweise Operationen | Ausführungslimits, Kaltstarts, Parallelität, Verbindungspools und Wiederholungsverhalten |
| VPS-/Container-Host | Vorhersehbare Arbeit mit verantwortlichem Betreiber | Patches, Zertifikate, Überwachung, Backups, Wiederherstellungszeit und Reservekapazität |
| Verwaltetes Kubernetes | Mehrere Arbeitslasten mit begründetem Bedarf an Planung oder Isolation | Cluster- und Workload-Richtlinien, Upgrades, Netzwerk, Kapazität und Erfahrung mit Vorfällen |

Verwaltete Dienste übertragen ausgewählte Betriebsaufgaben, aber keine Verantwortung für Anwendungsautorisierung, Datenklassifikation oder Wiederherstellungsnachweise. Vergleiche Rechenleistung, Speicher, ausgehenden Transfer, Beobachtbarkeit, Support, bezahlte Modellaufrufe und menschliche Arbeitszeit. Beziehe Spitzenlast sowie fehlgeschlagene Anfragen und Wiederholungen ein, statt nur einen monatlichen Leerlaufpreis zu schätzen.

## Ein Hosting-Entscheidungspaket dokumentieren

Benenne Dienstverantwortlichen, Ausfallbereiche, unterstützte Laufzeitversionen, Bereitstellungsidentität und Artefakt-Digest. Beschreibe, wie Produktion von Experimenten getrennt ist, wie Secrets bereitgestellt werden, wie öffentlicher Zugriff authentifiziert wird und welche Datenspeicher privat sind. Vergleiche Quoten und dokumentierte Wiederherstellungsmöglichkeiten mit RTO und RPO der Anwendung. Berücksichtige neben einem Regionsausfall auch die Sperrung des Anbieterkontos.

Halte Konfiguration außerhalb des Codes und Infrastruktur reproduzierbar. Behalte Kontrolle über Domain und Datenexportformat. Liste anbieterspezifische Funktionen und akzeptierte Migrationskosten auf; Portabilität ist eine Abwägung und verlangt nicht, jeden verwalteten Dienst zu vermeiden. Auch automatische Plattform-Backups erfordern eine Wiederherstellungsübung auf Anwendungsebene.

## Die gewählte Option nachweisen

Stelle vor dem ersten Produktionsrelease eine isolierte Umgebung bereit und durchlaufe einen echten Nutzerablauf. Prüfe verweigerten Zugriff, Rotation von Zugangsdaten, eine fehlgeschlagene Bereitstellung und Datenwiederherstellung. Ermittle mit [Leistungstests](performance-testing.md) dauerhaft tragbaren Verkehr und prüfe mit [Sicherheitstests](security-testing.md) Eingangs-, Mandanten- und Identitätsgrenzen. Dokumentiere eingesetzte Version, relevante Plattformeinstellungen und beobachtete Ergebnisse; ein Dashboard mit der Anzeige „gesund“ genügt nicht.

Vergleiche zur Veranschaulichung eine verwaltete Anwendung mit Datenbank und einen einzelnen VPS für dasselbe kleine SaaS. Der VPS kann geringere Infrastrukturkosten haben, erfordert aber einen Verantwortlichen für Patches und Wiederherstellung. Entscheide nach gemessenen Kosten und der Fähigkeit, den Betriebsvertrag zu erfüllen, nicht nach dem günstigeren Werbepreis. Dieses Beispiel ist eine Entscheidungsübung, keine bepreiste oder durch Benchmarks geprüfte Referenzbereitstellung.

## Ausstieg und Wiederherstellung

Probe Export und Import mit einer Kopie produktionsähnlicher Daten. Prüfe Datensatzzahlen, Geschäftssummen, Identitätszuordnungen, Secrets, Objektspeicher und Worker-Zustand. Plane den maßgeblichen Schreiber während der Umschaltung, das Beobachtungsfenster und die Bedingungen zum Stoppen der Verkehrsverlagerung. Halte den alten Pfad nur so lange wiederherstellbar, wie seine Daten zum gewählten Wiederherstellungsplan konsistent bleiben.

Ein DNS-Rollback kann vom neuen System angenommene Schreibvorgänge nicht rückgängig machen. Nach der Umschaltung kann ein Rollback Schreibsperren, Abgleich oder Vorwärtskorrektur erfordern. Teste diesen Plan vor einer folgenreichen Migration. Die Website dieser Bibliothek nutzt statisches Hosting; die Veröffentlichung über Pages stellt ihren lokalen MCP-Server nicht bereit.

## Verwandte Entscheidungen

[Eigene Server betreiben](self-hosting.md) · [Skalierung](scaling.md) · [Betrieb](operations.md) · [Leistungstests](performance-testing.md) · [Sicherheitstests](security-testing.md)

## Primärbelege

[docker-security](https://raw.githubusercontent.com/docker/docs/4d64a8e4f0a59967fc0b391120d54a90e9ccb60d/content/manuals/engine/security/_index.md) · [kubernetes](https://raw.githubusercontent.com/kubernetes/website/bc7f3479bc8b0af48097b155c22c8d58e8e1afe4/content/en/docs/concepts/architecture/_index.md) · [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/ec773ed37be4d07e00d4a2fbb237d0c0fe1ca3ce/README.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml)
