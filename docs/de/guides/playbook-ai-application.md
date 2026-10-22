---
{
  "id": "playbook-ai-application",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Eine KI-Anwendung bereitstellen

## Eignung und begrenztes Ergebnis

Verwenden Sie dieses Profil für eine authentifizierte Anwendung, die Informationen abruft oder mithilfe eines Modells eine Antwort erzeugt. Definieren Sie die Nutzeraufgabe, akzeptable Fehler, verbotene Offenlegungen, Latenzfrist, Kostenobergrenze, Datenresidenz und einen gewöhnlichen Ersatzablauf ohne Modell. Beginnen Sie mit einer begrenzten Anfragepipeline, einem Adapter um den Anbieter und einem Evaluationsdatensatz. Dieser von Agenten verfasste Vorschlag verbindet lokalen technischen Sachverstand mit den zitierten Nachweisen; er ist kein Beweis für die Zuverlässigkeit eines Modells.

Suche oder deterministische Regeln sind Alternativen, wenn sie die Aufgabe vorhersehbarer erfüllen. Retrieval kann Antworten stützen, die auf Projektdaten beruhen; Fine-Tuning ersetzt weder Dokumentzugriffsregeln noch Aktualität. Ergänzen Sie Modelle, Anbieter, Caches oder asynchrone Stufen erst, wenn gemessene Anforderungen an Qualität, Verzögerung, Durchsatz oder Datenresidenz ihre Evaluations- und Betriebskosten rechtfertigen. Eine größere Nutzerzahl allein rechtfertigt keine Agentenschleife.

## Berechtigung, Daten und Modellverhalten trennen

Gliedern Sie `api/`, `policy/`, `retrieval/`, `model_adapter/`, `evaluation/` und `telemetry/`. Der Server authentifiziert den Aufrufenden und filtert mögliche Dokumente anhand aktueller Zugriffsrechte, bevor Inhalte ein Modell erreichen. Berücksichtigen Sie Mandant, Richtlinienversion, Dokumentversion und Löschstatus bei Cache- und Retrieval-Entscheidungen. Ein globaler Antwortcache, dessen Schlüssel nur aus der Suchanfrage besteht, kann den Kontext eines anderen Nutzers offenlegen. Definieren Sie, wie Widerruf und Löschung unter dem gewählten Anbietervertrag Indizes, gespeicherte Prompts, generierte Antworten und beim Anbieter gespeicherte Daten erreichen.

Das Modell liefert nicht vertrauenswürdige Inhalte. Validieren Sie strukturierte Ausgaben, rendern Sie Text sicher und halten Sie die Werkzeugausführung hinter einer unabhängigen Autorisierung. Abgerufene Anweisungen, Quellenangaben und die Konfidenz des Modells erteilen niemals Berechtigungen. Definieren Sie Antwortverträge für eine quellenbelegte Antwort, unzureichende Belege, einen nicht verfügbaren Anbieter, Budgeterschöpfung und Abbruch. Eine Quellenangabe muss eine abgerufene Quelle identifizieren, die die zugehörige Aussage tatsächlich stützt; eine plausibel aussehende URL ist keine Quellenstützung. Halten Sie rohe Zugangsdaten aus Prompts heraus und geben Sie der Protokollierung ausdrückliche Datenschutz- und Aufbewahrungsregeln.

## Arbeit und Nachweise aufeinander abstimmen

1. Die Erkundung legt vor der Modellauswahl repräsentative Aufgaben, Fehlerschwere, rechtmäßige Datenverarbeitung und ein Bewertungsraster fest. Die menschliche Verantwortung vereinbart akzeptable Fehlerraten und entscheidet mehrdeutige Fälle.
2. Die Implementierung baut eine Pipeline mit autorisiertem Retrieval, begrenztem Kontext, Anbieterfrist, Ausgabevalidierung und Ersatzablauf. Versionieren Sie Modelleinstellungen, Prompt, Retrieval- und Indexkonfiguration sowie Werkzeugschemata gemeinsam.
3. Die Verifikation führt eine getrennt gehaltene, datenschutzgerechte Evaluationsmenge und Angriffsfälle aus und untersucht anschließend Berechtigungs- und Kostenspuren. Die Release-Vorbereitung vergleicht den Kandidaten mit einer festen Ausgangsversion und dokumentiert menschliche Prüfung und ungeklärte Fehler.

Das Übergabepaket enthält Profil, Datenfluss-ADR, Entscheidung zu Anbieter und Datenverarbeitung, Zugriffsmatrix, Identität des Evaluationsdatensatzes, Bewertungen pro Fall und menschliche Einzelfallentscheidungen, Versionsmanifest, Verteilung von Latenz und Kosten, Nachweise zum Ersatzablauf und Incident-Verantwortung. `examples/frontend` und `examples/agent_workflow` bieten lokale Referenzen für Interaktion und Kontrollgrenzen zur Untersuchung. Keine davon belegt die semantische Antwortqualität, die Compliance des Anbieters oder die Sicherheit eines produktiven Retrieval-Dienstes.

## Prüfkriterien außerhalb des Modells verwenden

Wählen Sie Unit-Tests für Schema und Budgetberechnung, Integrationstests für Zugriffsfilter und Anbieterfehler sowie Evaluationen für Nützlichkeit und Quellenstützung. Halten Sie Trainings- und Abstimmungsbeispiele von getrennten Abnahmefällen fern. Bewerten Sie Antwortkorrektheit, unbelegte Aussagen, angemessenes Nichtantworten und schädliche Auslassungen getrennt; Mittelwerte können eine schwere Offenlegung verdecken. Menschlich geprüfte Bewertungsraster bleiben erforderlich, wenn Ergebnisse subjektiv sind. Modellbasierte Bewertung ist eine Messhilfe, keine unabhängige Abnahmeinstanz.

Legen Sie eine eindeutige synthetische Markierung in ein nicht zugängliches Dokument. Fragen Sie direkt, indirekt und über ein zugängliches Dokument mit feindseligen Anweisungen danach. Die Markierung darf weder im abgerufenen Kontext noch in Anbieteranfragen, zurückgegebenen Antworten oder zugänglichen Logs vorkommen. Wiederholen Sie den Versuch nach Widerruf oder Löschung mit bereits gefüllten Caches und Indizes. Versuchen Sie schemawidrige Ausgaben und skriptartige Quellenangaben: Sie dürfen weder ausgeführt werden noch den Zugriff erweitern. Dies sind negative Prüfkriterien, keine Kontrollen, ob das Modell höflich ablehnt.

Erzwingen Sie Anbieter-Timeouts, trennen Sie die Browserverbindung und erschöpfen Sie ein durchgesetztes Anfragebudget. Die Anwendung muss aufhören, weitere Aufrufe einzuplanen, einen klaren Nutzerzustand erhalten und bereits angefallene Arbeit erfassen; ein Abbruch garantiert nicht, dass der Anbieter die Abrechnung beendet hat. Vergleichen Sie wiederholte Läufe auf Qualitätsschwankungen und messen Sie die Latenz in hohen Perzentilen sowie Kosten pro akzeptierter Aufgabe unter begrenzter Last. Erfassen Sie tatsächliche Stichprobengrößen, fehlgeschlagene Fälle und nicht getestete Sprachen oder Fachgebiete.

## Veröffentlichung und langfristiger Betrieb

Führen Sie die Funktion für eine vereinbarte Gruppe mit Abschaltmöglichkeit ein und überwachen Sie Schwellen für Qualität, Nichtantworten, Fehler, Latenz und Ausgaben. Eine Änderung an Modell, Prompt, Retrieval oder Ersatzablauf ist ein Verhaltensrelease, das eine erneute Evaluation verlangt. Bewahren Sie das vorherige Versionsmanifest und eine kompatible Indexdarstellung auf. Ein Rollback kann Verhalten wiederherstellen, aber weder offengelegte Informationen zurückholen noch gesendete Anbieteranfragen zurücknehmen. Eine Offenlegung benötigt Incident-Bearbeitung sowie eine Zugriffs- und Datenprüfung; nur ein lokales Log zu löschen genügt nicht.

Benennen Sie Verantwortliche für veränderte Evaluationsergebnisse, Zugriffsrichtlinien, Anbieter-Incidents und Kosteneskalation. Planen Sie neben Inferenz auch Embedding- und Indexaktualisierungen, Wiederholungen, Evaluationsläufe, Speicher und menschliche Prüfung ein. Klären Sie vor Produktion Aufbewahrung und Residenz beim Anbieter, echte Identitäten, Verschlüsselung, Weitergabe von Löschungen, Missbrauchsgrenzen und betriebliche Betreuung. Die Stilllegung deaktiviert Einstiegspunkte, arbeitet sichere Restaufgaben ab, löscht oder bewahrt abgeleitete Artefakte entsprechend der Richtlinie, widerruft Anbieterzugriff und erhält nur die für Rechenschaft erforderlichen Nachweise.

## Mit verwandten Entscheidungen fortfahren

[Agenten](agents.md) · [Sicherheit](security.md) · [Qualitätsprüfungen](quality.md) · [Teststrategie](testing-strategy.md)

## Primärquellen

[owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-xss](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
