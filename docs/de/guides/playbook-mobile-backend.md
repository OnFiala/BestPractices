---
{
  "id": "playbook-mobile-backend",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Ein Backend für mobile Clients bereitstellen

## Eignung und Vertrag für unterstützte Clients

Verwenden Sie dieses Profil für ein Backend, das installierte Clients bedient, die offline bleiben, Schreibvorgänge wiederholen und zu unterschiedlichen Zeiten aktualisiert werden können. Erfassen Sie unterstützte Client- und API-Versionen, das maximale Offline-Intervall, auf Geräten zulässige geschützte Daten, Synchronisationsaktualität, Widerrufsrichtlinie und Wiederherstellungsziele. Dieser von Agenten verfasste Vorschlag betrifft die Bereitstellung von Backend und Protokoll. Er behauptet nicht, dass ein nativer Client, sichere Gerätespeicherung, Push-Integration oder plattformspezifische Barrierefreiheit implementiert wurde.

Beginnen Sie mit einer modularen API, kanonischen relationalen Daten und einem begrenzten Synchronisationspfad. Eine ausschließlich online nutzbare Anwendung ist eine einfachere Alternative, wenn die Nutzeraufgabe es erlaubt. Offline-Bearbeitung bringt dauerhafte Operationsidentität, Konfliktbehandlung, Löschsemantik und Supportkosten mit sich. Ergänzen Sie regionale Platzierung, spezialisierte Synchronisationsinfrastruktur oder Partitionierung erst nach Messungen von Synchronisationsverzögerung, Konflikthäufigkeit, Konkurrenz bei Schreibvorgängen, Nutzdatengröße oder geografisch bedingter Latenz. Die Zahl installierter Geräte allein ist kein Migrationsauslöser.

## Grenzen und Datenmodell

Trennen Sie `api/`, `policy/`, `domain/`, `sync/`, `contracts/` und `ops/`. Der Server verantwortet kanonischen Zustand und Autorisierung. Eine Gerätekennung ist ein Routing- und Audit-Attribut, kein Nachweis einer Nutzerberechtigung. Validieren Sie Zugriff beim Lesen, bei Synchronisationsdownloads, Uploads und der Erneuerung von Zugangsdaten. Push-Nachrichten sollten signalisieren, dass zulässige Daten verfügbar sein könnten, statt sensible Datensatzinhalte zu enthalten.

Definieren Sie für jede Offline-Änderung eine stabile Operations-ID, eine authentifizierte Identität, Datensatz-ID, Ausgangsrevision und beabsichtigte Änderung. Speichern Sie Deduplizierungsergebnisse in derselben Transaktion, die die Änderung anwendet. Die Wiederverwendung einer ID mit einer anderen Änderung muss einen Konflikt auslösen. Verwenden Sie servergesteuerte Revisionen, um veraltete Änderungen zu erkennen; Geräteuhren eignen sich nicht als alleinige Instanz für die Reihenfolge geschäftlicher Änderungen.

Wählen Sie die Konfliktrichtlinie je Domäne. Eine bearbeitbare Notiz kann beide Versionen zur menschlichen Zusammenführung anbieten. Eine Bestandsreservierung sollte eine veraltete Vorbedingung ablehnen oder eine transaktionale Invariante durchsetzen, statt stillschweigend den jüngsten Zeitstempel zu wählen. Löschmarkierungen oder gleichwertiges Löschwissen müssen länger als das unterstützte Offline-Intervall erhalten bleiben. Wenn ein Synchronisationscursor abläuft, verlangen Sie eine dokumentierte vollständige Neusynchronisation, die weder stillschweigend gelöschte Datensätze wiederbelebt noch ausstehende lokale Änderungsabsichten verliert.

## In sicherer Reihenfolge liefern

1. Die Erkundung erfasst Abläufe für Lesen, Offline-Nutzung, Bearbeitung und Wiederverbindung, Datenklassifizierung, unterstützte Versionen und Konfliktbeispiele. Eine menschliche Verantwortung akzeptiert die Richtlinien für Offline-Aufbewahrung und Aktualisierungen.
2. Die Implementierung erstellt eine versionierte API und eine synthetische Client-Testumgebung vor dem vollständigen Synchronisationspfad. Ergänzen Sie Operationsdeduplizierung, bedingte Aktualisierungen, Seitennavigation und Cursor, Löschung sowie beobachtbaren Synchronisationsstatus mit ausdrücklichen Fehlerverträgen.
3. Die Verifikation führt alte und neue Konsumenten gegen Übergangsschemata aus und simuliert zwei Geräte, Netzwerkunterbrechung, Widerruf und Wiederherstellung. Die Release-Verantwortung legt eine stufenweise Einführung und Kriterien zur Beendigung des Client-Supports fest.

Übergeben Sie Profil, API- und Synchronisationsschema, Kompatibilitätsmatrix, Konflikt-ADR, Operationsbeispiele, Anforderungen an Gerätedaten, Migrationsplan, beobachtete Vertrags- und Wiederherstellungsergebnisse, Supportzeitraum und benannte Backend- und Client-Verantwortliche. `examples/durable_service` kann lokale Persistenzexperimente unterstützen. Es ist weder eine mobile Synchronisationsengine noch ein Nachweis nativen Geräteverhaltens; die Prüfung echter Clients und Plattformen bleibt ein gesondertes Arbeitsergebnis.

## Das Ausbleiben unbeabsichtigter Effekte prüfen

Verwenden Sie Unit-Tests für Zusammenführungs- und Zustandsregeln, Integrationstests für Transaktionen und Autorisierung sowie Vertragstests für den ältesten unterstützten Client und den Kandidaten. Eine Versionsbezeichnung allein belegt keine Kompatibilität. Prüfen Sie optionale Felder, den Umgang mit unbekannten Enum-Werten, Seitennavigation, Fehlercodes, Einheiten und das Verhalten gelöschter Datensätze. Sobald ein Client existiert, verwenden Sie ein echtes Gerät oder einen Plattformemulator für natives Cache-Verhalten, Zugangsdatenablage, Hintergrundarbeit und Push-Verhalten.

Lassen Sie zwei synthetische Geräte dieselbe Revision offline bearbeiten und anschließend in beiden möglichen Reihenfolgen wieder verbinden. Das Prüfkriterium ist das erklärte Konfliktergebnis mit erhaltener Nutzerabsicht, nicht bloß zwei erfolgreiche Antworten. Unterbrechen Sie einen Upload nach dem Commit, wiederholen Sie ihn und prüfen Sie die kanonischen Datensätze: Es darf keinen zusätzlichen Geschäftseffekt geben. Wiederholen Sie die Operations-ID mit verändertem Inhalt und verlangen Sie einen Konflikt. Löschen Sie einen Datensatz, während ein anderes Gerät offline ist; eine veraltete Aktualisierung darf ihn nicht außerhalb der erklärten Regel wiederherstellen.

Widerrufen Sie ein Gerät oder eine Sitzung vor der Erneuerung der Zugangsdaten und der geschützten Synchronisation. Über den Erneuerungspfad darf der Zugriff nicht zurückgewonnen werden; testen Sie ausdrücklich jede dokumentierte Übergangsfrist für Zugriffstoken. Simulieren Sie den Ablauf eines Cursors und die Wiederherstellung einer älteren Serversicherung: Clients müssen eine inkompatible Synchronisationshistorie erkennen, ausstehende Operationen abgleichen und sicher neu synchronisieren. Messen Sie Wiederherstellungszeit, tatsächlichen Datenverlust, Synchronisationsverzögerung, Konfliktrate und Bandbreite unter begrenzten schlechten Netzwerkbedingungen. Halten Sie nicht getestetes Plattformverhalten sichtbar.

## Einführung, Betrieb und Stilllegung

Erweitern Sie Verträge und Schema, bevor Sie Konsumenten ausliefern; unterstützen Sie während des gesamten veröffentlichten Zeitfensters gemischte Client-Versionen. Ergänzen Sie Daten mit Kontrollpunkten, validieren Sie Synchronisationsinvarianten und entfernen Sie alte Felder erst, wenn die Supportrichtlinie es erlaubt. Ein Backend-Rollback kann installierte Clients weder zur Aktualisierung zwingen noch heruntergeladene Daten löschen. Stellen Sie isoliert wieder her, führen Sie bei Bedarf eine neue Synchronisationsepoche oder eine gleichwertige Wiederherstellungsmarkierung ein und gleichen Sie Operationen ab, bevor Schreibvorgänge wieder zugelassen werden.

Überwachen Sie Fehler nach Client- und API-Version, die älteste ausstehende Operation, Konfliktrate, Neusynchronisationsvolumen, verweigerte Erneuerungen und Benachrichtigungszustellung, ohne geschützte Nutzdaten zu protokollieren. Weisen Sie Backend-Incidents und Client-Kompatibilität getrennte Verantwortliche zu. Planen Sie Speicher, Übertragung, Push-Anbieternutzung, Unterstützung alter Versionen und Wiederherstellungsübungen ein. Zu den Produktionslücken gehören echte Identitäten, Gerätespeicherung, Netzwerksicherheit, natives Hintergrundverhalten, Push-Zugangsdaten sowie Einwilligung und Aufbewahrung. Bei der Stilllegung erhalten Clients eine handlungsorientierte Antwort zum Supportende, ein autorisierter Export wird angeboten, ausstehende Arbeit wird soweit möglich abgearbeitet, Zugangsdaten werden widerrufen und verbleibende Offline-Kopien nach der vereinbarten Richtlinie behandelt.

## Mit verwandten Entscheidungen fortfahren

[Frontend-Verträge](frontend.md) · [Daten und Migrationen](data.md) · [Sicherheit](security.md) · [Teststrategie](testing-strategy.md)

## Primärquellen

[owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-session](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Session_Management_Cheat_Sheet.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [semver](https://raw.githubusercontent.com/semver/semver/f99d5485190a47c0863949e7da810a5553e0ed4d/semver.md)
