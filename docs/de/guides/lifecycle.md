---
{
  "id": "lifecycle",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Der vollständige Projektlebenszyklus

## Jede Phase mit Nachweisen abschließen

Die folgenden Phasen bilden das vorgeschlagene Betriebsmodell dieser Bibliothek. Ihre Tiefe richtet sich nach Auswirkungen und Zuständigkeiten; die Bezeichnungen sind keine externe Zertifizierung. Für ein persönliches Skript kann eine kurze Aufzeichnung genügen, während ein Dienst mit schwerwiegenden Folgen unabhängige fachliche und sicherheitsbezogene Nachweise benötigt.

| Phase | Erforderliches Artefakt | Nachweis für den Abschluss |
| --- | --- | --- |
| Erkunden | Problembeschreibung, Übersicht über Beteiligte und Daten | Messbares Nutzerergebnis, ausdrückliche Nichtziele und verantwortlicher Eigentümer |
| Entwerfen | Projektprofil, Kontextdiagramm, ADR und Bedrohungsmodell | Menschliche Zustimmung zu Rahmenbedingungen, Budget und Wiederherstellungszielen |
| Planen | Kleiner Backlog und Testplan | Jede Aufgabe hat Umfang, Verantwortlichen, Fehlerfälle und Abbruchbedingungen |
| Bauen | Code, Migrationen, Tests und aktualisierte Erklärung | Reproduzierbare Prüfungen und für das Review sichtbarer Diff |
| Veröffentlichen | Versioniertes Artefakt, Einführungs- und Wiederherstellungsplan | Abnahme in Staging, Migrations-/Wiederherstellungsnachweise und menschliche Freigabe |
| Betreiben | Betriebshandbuch, Dienstmesswerte und Kostenverantwortung | Gemessene Ziele, handlungsrelevante Alarme und geprobte Wiederherstellung |
| Weiterentwickeln | Erkenntnisse aus Vorfällen und Migrations-/Abkündigungsaufzeichnung | Unterstützte Verbraucher migrieren vor der Entfernung |
| Stilllegen | Export-/Lösch- und Zugriffsentzugsplan | Aufbewahrungspflichten erfüllt, externe Integrationen geschlossen und Abrechnung geprüft |

Ein Artefakt ist nützlich, wenn es eine Entscheidung oder Handlung unterstützt. Ein erzeugtes Dokument, das niemand verwenden kann, belegt keine Einsatzbereitschaft.

## Kontinuierlich testen

Definiere während der Erkundung, woran ein verfehltes Nutzerergebnis erkennbar wäre. Benenne beim Entwurf Invarianten und Vertrauensgrenzen, die stärkere Tests verdienen. Lege Abnahmebeispiele und erwartetes Fehlerverhalten fest, bevor ein Agent Code schreibt; wähle mit der [Teststrategie](testing-strategy.md) den kleinsten nützlichen Prüfumfang.

Führe während der Implementierung gezielte Prüfungen für die geänderte Grenze aus. Prüfe bei Integration und Veröffentlichung Kompatibilität, verweigerte Aktionen und kritische Abläufe über öffentliche Schnittstellen. Nutze vor kapazitätssensiblen Veröffentlichungen und geplanten Migrationen [Leistungstests](performance-testing.md) mit ausdrücklichen Grenzen und Autorisierung. Führe [Sicherheitstests](security-testing.md) aus, wenn sich Identität, Datensensibilität, externe Eingaben, Abhängigkeiten oder Werkzeugbefugnisse ändern. Der Betrieb führt Wiederherstellungsübungen, Regressionstests aus Vorfällen und Beobachtungen der tatsächlichen Arbeitslast in die Planung zurück.

Ein grüner Build erfüllt kein offenes Abnahmekriterium. Dokumentiere fehlgeschlagene, übersprungene und nicht ausgeführte Prüfungen getrennt und benenne einen Verantwortlichen für ungeklärte Risiken. Eine Freigabe gilt für das getestete Artefakt und seinen Kontext; eine spätere wesentliche Änderung benötigt erneutes Review.

## Verantwortung von Menschen und Agenten

Der Mensch bestimmt Nutzen, Priorität, akzeptables Risiko, Architekturrichtung und Veröffentlichungsbefugnis. Agenten untersuchen, entwerfen, implementieren, testen und berichten Unsicherheiten innerhalb ihrer zugewiesenen Fähigkeiten. Trenne Implementierungs- und Prüfrollen, wenn die möglichen Folgen es rechtfertigen; mehrere Agenten, die dieselbe Annahme wiederholen, sind kein unabhängiger Nachweis.

Bewahre Entscheidungen, Lauf-IDs, Artefaktversionen und Wiederherstellungsinformationen im Repository auf, nicht nur im Chat. Eine begrenzte Aufgabe endet mit ihrem tatsächlichen Ergebnis und offenen Fragen, einschließlich des Grundes für einen verworfenen Entwurf. Bezeichne niemals einen nicht ausgeführten Test oder eine erzeugte Review-Checkliste als menschliche Freigabe.

## Kurs ändern und das System schließen

Zeige einen durchgängigen Ablauf einschließlich Fehlern und verweigertem Zugriff, bevor du den Funktionsumfang erweiterst. Ist das Ergebnis nicht messbar, kehre zur Erkundung zurück. Sind Zuständigkeit oder Betriebskosten nicht tragbar, vereinfache die Architektur, statt unbeaufsichtigte Automatisierung hinzuzufügen.

Plane die Stilllegung bei der Erstellung: Wie exportieren Nutzer ihre Daten, welche Datensätze müssen aufbewahrt werden und wie werden Zugangsdaten sowie delegierte Agentenzugriffe widerrufen? Teste Export und Schließung, bevor dies dringend wird. Lege geplante Jobs, Anbieterressourcen und Wiederherstellungskopien gemäß vereinbarter Aufbewahrungsrichtlinie still; das Löschen des Anwendungsrepositorys ist keine vollständige Abschaltung.

## Verwandte Entscheidungen

[Teststrategie](testing-strategy.md) · [Qualitätsprüfungen](quality.md) · [Betrieb](operations.md) · [Agenten](agents.md) · [Einführung](adoption.md)

## Primärbelege

[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml)
