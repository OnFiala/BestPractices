---
{
  "id": "self-hosting",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Eigene Server betreiben

## Topologie und Grenzen festlegen

Ein kleiner öffentlicher Dienst kann einen TLS-Reverse-Proxy an der Eingangsgrenze, eine Anwendung in einem privaten Netzwerk und eine Datenbank einsetzen, die nur für autorisierte Anwendungs- und Verwaltungsidentitäten erreichbar ist. Die Netzwerkplatzierung ergänzt die Authentifizierung; sie ersetzt keine Autorisierung. Trenne Produktion von Experimenten und richte einen protokollierten, eingeschränkten Verwaltungszugang ein. Ein einzelner Rechner bleibt ein einzelner Ausfallbereich, auch wenn auf ihm mehrere Container laufen.

Der folgende minimale Betriebsvertrag ist eine Empfehlung der Bibliothek auf Grundlage von Dokumentation zu Containersicherheit und Wiederherstellung. Passe ihn an Plattform und Auswirkungen an; er ist keine gehärtete, unmittelbar einsetzbare Serverkonfiguration.

| Verpflichtung | Dokumentieren und prüfen |
| --- | --- |
| Verwaltung | Verantwortlicher, eingeschränkter Zugriff, Widerrufsweg und Nachweis verweigerten Zugriffs |
| Softwareupdates | Unterstütztes Betriebssystem und Laufzeit, Patchverantwortlicher, Wartungsfenster und Wiederherstellungsartefakt |
| Ressourcenisolation | CPU-, Speicher- und Datenträgergrenzen, Kapazitätsalarme und Verhalten bei Erschöpfung |
| Secrets | Bereitstellungs- und Rotationsmechanismus sowie getrennte Identitäten für Deployment, Migration und Anwendung |
| Persistenz | Ausdrückliche Daten-Volumes, Sicherungsumfang, Verschlüsselung und Schlüsselzugriff sowie Aufbewahrung |
| Öffentliche Grenze | TLS-Erneuerung, erlaubte Ports, Authentifizierung und sichere Fehlerantworten |
| Wiederherstellung | Backup außerhalb des Hosts, letzte erfolgreiche Wiederherstellung, RTO/RPO und Vorfallkontakt |

Bevorzuge nach Möglichkeit ein separates Backup-Konto oder einen anderen Ausfallbereich. Ein Backup auf demselben beschreibbaren Datenträger kann mit dem Server ausfallen oder durch dieselbe kompromittierte Identität gelöscht werden. Prüfe, dass die Wiederherstellung nicht von Zugangsdaten abhängt, die ausschließlich auf dem verlorenen Host gespeichert sind.

## Eine reproduzierbare Einheit bereitstellen

Nutze Infrastructure as Code und fixiere das bereitstellbare Image anhand seines Digests. Speichere Anwendungszustand in ausdrücklich verwalteter Persistenz statt versehentlich in einer Container-Schicht. Stelle der Anwendung oder einem Agenten keinen Docker-Socket bereit und betrachte einen Container nicht als starke Sandbox für feindlichen Code. Beschränke Privilegien und Ressourcen auf den Bedarf der Arbeitslast.

Compose kann für wenige Dienste mit verstandenem Fehler- und Updateverhalten passen. Führe Orchestrierung ein, wenn Anforderungen an Planung, Verfügbarkeit oder Zusammenarbeit ihren Betriebsaufwand rechtfertigen. Mehr Replikate auf einem Rechner machen diesen nicht hochverfügbar. Ein Heimserver erfordert zusätzlich eine Bewertung von Stromversorgung, Netzanbindung, physischem Zugriff und Wiederherstellung an einem anderen Standort.

## Wiederherstellung und Ausfälle proben

Erstelle den Host auf einem separaten Testrechner anhand der dokumentierten Konfiguration neu und stelle ein aktuelles Backup wieder her. Deaktiviere echte E-Mails, Zahlungen und andere externe Nebenwirkungen. Prüfe einen repräsentativen Nutzerablauf, Mandantenberechtigungen, Geschäftssummen und wartende Arbeit, bevor die Wiederherstellung als erfolgreich gilt. Miss Wiederherstellungszeit und tatsächlichen Verlustzeitraum gegenüber den vereinbarten Zielen.

Prüfe vor einer wesentlichen Hosting-Änderung mit [Leistungstests](performance-testing.md) begrenzte Überlast und Wiederherstellung in einer autorisierten Umgebung. Teste sicher knappen Datenträgerplatz, eine gestoppte Anwendung, eine nicht erreichbare Datenbank und die Zertifikatserneuerung. Prüfe mit [Sicherheitstests](security-testing.md) von der öffentlichen Grenze aus, dass Verwaltungs- und Datenbankports geschlossen sowie Zugangsdaten widerrufen sind.

Ein Test besteht erst, wenn nutzersichtbares Verhalten und gespeicherter Zustand den Abnahmevertrag erfüllen. Hängt die Wiederherstellung von undokumentierten manuellen Schritten ab, dokumentiere sie und wiederhole die Übung. Wechsle zu einem verwalteten Dienst oder reduziere den Umfang, wenn die Verantwortlichen Patch-, Reaktions- oder Wiederherstellungspflichten nicht erfüllen können; zusätzliche Technik schließt keine Verantwortungslücke.

## Verwandte Entscheidungen

[Sicherheit](security.md) · [Hosting](hosting.md) · [Betrieb](operations.md) · [Leistungstests](performance-testing.md) · [Sicherheitstests](security-testing.md)

## Primärbelege

[docker-security](https://raw.githubusercontent.com/docker/docs/4d64a8e4f0a59967fc0b391120d54a90e9ccb60d/content/manuals/engine/security/_index.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml) · [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/ec773ed37be4d07e00d4a2fbb237d0c0fe1ca3ce/README.md)
