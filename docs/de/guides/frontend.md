---
{
  "id": "frontend",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Frontendarchitektur und Verträge

## Darstellung für jede Interaktion auswählen

Statische Generierung eignet sich für öffentliche Inhalte, die neu gebaut werden können. Serverseitige Darstellung kann anfängliche Aktualität oder Auffindbarkeit unterstützen, während clientseitige Darstellung fortlaufende Interaktion ermöglicht. Hybride Routen können diese Ansätze verbinden. Dies ist der eigenständige Entscheidungsrahmen der Bibliothek: Miss den relevanten Ablauf und prüfe das aktuelle Verhalten des gewählten Frameworks vor seiner Übernahme.

Dokumentiere Cache-Verantwortung, Hydrierungs- und JavaScript-Aufwand sowie Authentifizierungs- und Bereitstellungsgrenzen. Lege keine private, serverseitig erzeugte Nutzerantwort in einem Cache ab, den ein anderer Akteur mitbenutzt. Microfrontends können unabhängige Zuständigkeiten unterstützen, bringen aber Aufwand für Routing, Abhängigkeiten und einheitliche Gestaltung mit sich; sie sind kein Standardverfahren zum Aufteilen von Komponenten.

## Jedem Zustand einen Eigentümer geben

Unterscheide Serverzustand, URL-/Navigationszustand, lokalen Interaktionszustand und dauerhafte Einstellungen. Entscheide, welcher Zustand Neuladen oder Offline-Nutzung übersteht und wie er nach Abmeldung oder Rechteänderung ungültig wird. Organisiere Funktionen um ausdrückliche Schnittstellen und gemeinsame barrierefreie Grundbausteine. Dieselben Serverdaten in mehrere Speicher zu kopieren erzeugt Abgleicharbeit statt Widerstandsfähigkeit.

Definiere für jede API-gestützte Interaktion:

| Vertrag | Beispiel für Abnahmenachweise |
| --- | --- |
| Autorisierung | Direkte API-Anfragen scheitern bei fehlender Berechtigung, auch wenn die Oberfläche umgangen wird |
| Antwortstruktur | Alte und neue Clients verarbeiten dokumentierte Felder, Fehler, Paginierung und Einheiten |
| Laden und Abbruch | Das Verlassen der Seite beendet unnötige Arbeit oder ignoriert ein verspätetes Ergebnis sicher |
| Optimistische Änderung | Bei Ablehnung wird der sichtbare Zustand wiederhergestellt oder abgeglichen, ohne Nutzereingaben zu verlieren |
| Offline-Nutzung und Konflikte | Eine wartende Änderung besitzt eine stabile Identität und eine ausdrückliche Konfliktregel beim Wiederverbinden |
| Datenschutz | Abmeldung und Zugriffsentzug löschen relevante private Cache-Daten oder machen sie ungültig |

Der Server verantwortet vertrauenswürdige Validierung und Autorisierung. Versteckte Schaltflächen und Client-Schemas verbessern die Bedienbarkeit, können aber keine Zugriffskontrolle erzwingen. Backend-Secrets gehören nicht in Browser-Bundles, Source Maps oder erzeugte Indizes. Browsercode sowie Modell- und Werkzeugausgaben sind an der Servergrenze nicht vertrauenswürdig.

## Den beobachtbaren Ablauf testen

Teste fachliche Regeln während der Implementierung getrennt von Darstellungsdetails. Führe bei API-Änderungen Kompatibilitätstests für Verbraucher aus. Prüfe wichtige Abläufe vor der Veröffentlichung als [Black-Box-Nutzer](testing-strategy.md): Tastatur- und Fokusreihenfolge, zugängliche Namen, Kontrast, schmales Ansichtsfenster, Lade-, Leer- und Fehlerzustände, verweigerten Zugriff und unterbrochene Anfragen. Verbinde automatisierte Barrierefreiheitsprüfungen bei Bedarf mit aufgabenbezogenen Tests per Tastatur und assistiver Technik; ein bestandener automatisierter Check belegt keine vollständige Konformität.

Nutze [Leistungstests](performance-testing.md) für repräsentative Geräte- und Netzwerkbedingungen sowie anhaltende API-Last und miss Navigation, Interaktionslatenz, übertragene Dateien und Fehler. Prüfe, dass das Frontend bei Wiederholungen, Polling oder Wiederverbindung keine übermäßigen Backend-Aufrufe erzeugt. Prüfe Authentifizierungs- und Cache-Grenzen anhand des [Sicherheitstestplans](security-testing.md).

## Bewusst weiterentwickeln

Ein Backend-for-Frontend kann sinnvoll sein, wenn ein bestimmter Client Aggregation oder eine stärkere serverseitige Grenze benötigt. Benenne Nutzen und Verantwortung für die zusätzliche Bereitstellung. Wechsle das Framework oder führe Microfrontends erst ein, wenn gemessene Grenzen die Migration einschließlich Barrierefreiheits-, Kompatibilitäts- und Abhängigkeitspflegeaufwand rechtfertigen. Halte einen Veröffentlichungs- und Cache-Invalidierungsplan bereit, damit alte Browserdateien mit der bereitgestellten API kompatibel bleiben.

WebMCP ist hier eine progressive Erweiterung. Gewöhnliches Lesen und Suchen muss ohne WebMCP funktionieren; auch unterstützte Browser benötigen Berechtigungs-, Abbruch- und Navigationstests. Experimentell bereitgestellte Werkzeuge dürfen keinen Zugriff gewähren, den der Nutzer nicht bereits besitzt.

## Verwandte Entscheidungen

[Architektur](architecture.md) · [Teststrategie](testing-strategy.md) · [Leistungstests](performance-testing.md) · [Sicherheitstests](security-testing.md) · [Integrationen](integrations.md)

## Primärbelege

[wcag](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/index.html) · [owasp](https://raw.githubusercontent.com/OWASP/ASVS/2b47a9dd16760ee484a6672d197f1f7e25d9c632/README.md) · [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/51ed75653aaa7f174f8dbe05d1bc327359bbc57c/README.md) · [wcag-keyboard](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/keyboard.html) · [wcag-focus-order](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/focus-order.html) · [wcag-focus-visible](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/focus-visible.html) · [wcag-contrast](https://raw.githubusercontent.com/w3c/wcag/457cece22d8219be32d29c5c1313e71aa6b61eae/guidelines/sc/20/contrast-minimum.html) · [azure-cqrs](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/cqrs.md)
