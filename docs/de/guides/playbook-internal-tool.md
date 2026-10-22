---
{
  "id": "playbook-internal-tool",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Ein internes Betriebswerkzeug bereitstellen

## Eignung und Rahmenbedingungen

Verwenden Sie dieses Profil für eine Mitarbeiteranwendung, die Datensätze prüft, Daten exportiert oder ein vorgelagertes Geschäftssystem verändert. Auch ein kleiner Nutzerkreis kann Berechtigungen mit großer Tragweite besitzen. Erfassen Sie Identitätsanbieter, fachlich Freigabeberechtigte, Datenklassifizierung, Widerrufsfrist, Ratenlimits vorgelagerter Systeme und die maximal akzeptable Dauer ungeklärter Arbeit. Dieser von Agenten verfasste Leitfaden schlägt ein lokales Vorgehen zur Auslieferung vor; er ist keine verabschiedete Organisationsrichtlinie.

Beginnen Sie mit einer Anwendung und ausdrücklichen Integrationsadaptern. Verwenden Sie das SSO der Organisation zur Authentifizierung und eine getrennte Anwendungsrichtlinie für Aktionen und Datensatzumfang. Eine Tabellenkalkulation oder ein vorhandenes Workflow-Produkt bleibt eine Alternative, wenn dessen Berechtigungs-, Audit- und Exportverhalten den tatsächlichen Bedarf erfüllt. Ein Worker ist gerechtfertigt, wenn Operationen die Frist einer Anfrage überschreiten oder dauerhaft abgesicherte Wiederholungen benötigen. Trennen Sie Integrationen erst, wenn gemessene Fehlerkopplung, Warteschlangenverzögerungen oder unabhängige Verantwortung den zusätzlichen Deployment-Aufwand aufwiegen.

## Repository und Berechtigungsgrenzen

Halten Sie `identity/`, `policy/`, `cases/`, `integrations/`, `exports/` und `audit/` im Code getrennt. Legen Sie fest, welches System für jedes Feld maßgeblich ist; ein importierter Wert aus einem vorgelagerten System darf nicht stillschweigend zu einer unabhängig bearbeitbaren Wahrheit werden. Ein Operationsprotokoll erfasst anfragende Person, Aktion, Objektumfang, Eingabeversion, Freigabeidentität, stabile Operations-ID und Status. Speichern Sie erforderliche Audit-Fakten mit Zugriffskontrollen und Aufbewahrungsregeln, keine uneingeschränkten Kopien vertraulicher Nutzdaten.

Authentifizierung belegt Identität, keine Berechtigung. Prüfen Sie Aktion und Umfang am API-Eingang, bei der Exporterstellung, beim Exportdownload und bei der Worker-Ausführung. Eingereihte Arbeit benötigt eine erklärte Delegationsrichtlinie: Prüfen Sie entweder die aktuellen Rechte der anfragenden Person erneut oder verwenden Sie einen gesondert autorisierten Dienstauftrag. Bewahren Sie die Befugnisse ehemaliger Beschäftigter nicht versehentlich in Auftragsnutzdaten auf. Definieren Sie die Wirksamkeitsfristen für Widerrufe über Anwendungssitzungen, zwischengespeicherte Berechtigungen, Downloadlinks und laufende Aufträge hinweg. Binden Sie bei folgenreichen Schreibvorgängen in vorgelagerten Systemen jede erforderliche fachliche Freigabe an die genau beabsichtigte Änderung.

## Auslieferungsfolge und Übergabe

1. Die Erkundungsrolle erfasst einen fachlichen Ablauf, dessen maßgebliche Datenfelder, eine Berechtigungsmatrix und den manuellen Ersatzablauf bei nicht verfügbaren vorgelagerten Systemen. Eine menschliche Fachverantwortung klärt unklare Freigaben und Aufbewahrung.
2. Die Implementierung erstellt einen schmalen vertikalen Ausschnitt mit schreibgeschützter Einsicht, begrenzter Änderung, dauerhaft gespeichertem Status für ausstehende Arbeit und einer Operationsabfrage. Führen Sie Exporte erst ein, nachdem deren gesonderter Berechtigungs- und Ablaufvertrag festgelegt wurde.
3. Die Verifikation prüft Zugriffsänderungen während einer Sitzung und bei eingereihter Arbeit und simuliert anschließend eine nach erfolgreicher Ausführung verlorene Antwort des vorgelagerten Systems. Die Betriebsrolle erstellt anhand stabiler Operations-IDs eine Abgleichanleitung und bereitet die Einführung für eine benannte Mitarbeitergruppe vor.

Liefern Sie Profil, ADR, Richtlinienmatrix, Verzeichnis der Verträge vorgelagerter Systeme, Zustandsdiagramm, Exportspezifikation, Nachweise mit erwarteten und beobachteten Ergebnissen, Release- und Wiederherstellungsverfahren sowie Supportverantwortung. Agenten können diese Rollen nacheinander übernehmen; zusätzliche Agenten schaffen keine unabhängige Gewissheit. Die lokalen Verzeichnisse `examples/durable_service` und `examples/agent_workflow` können Experimente zu Persistenz und freigabegesteuerter Arbeit unterstützen. Sie liefern weder einen Unternehmensidentitätsanbieter noch eine Genehmigung durch Fachverantwortliche.

## Angriffsorientierte und betriebliche Prüfungen auswählen

Prüfen Sie Richtlinienentscheidungen und Zustandsübergänge mit Unit-Tests. Verwenden Sie Integrationstests für Sitzungsinvalidierung, Adapter vorgelagerter Systeme, die tatsächliche Erstellung von Exporten und dauerhaft gespeicherte Aufträge. Browsertests sollten verweigerten Zugriff, nicht verfügbare vorgelagerte Daten, eine leere Vorgangsliste und ausstehende Arbeit abdecken, die nach dem Neuladen sichtbar bleibt. Ein deaktiviertes Bedienelement ist niemals ein Prüfkriterium für Autorisierung.

Erstellen Sie einen eingeschränkten Mitarbeiterzugang und einen Administratorzugang für synthetische Datensätze. Rufen Sie geschützte Endpunkte direkt auf; fordern Sie einen übergroßen Export an und manipulieren Sie dessen Filter und Downloadkennung. Die exportierten Bytes und die resultierenden Änderungen müssen im Berechtigungsumfang des Aufrufenden bleiben. Widerrufen Sie den Mitarbeiterzugang, während eine Sitzung, ein signierter Link und eine eingereihte Operation existieren; nach dem vereinbarten Zeitfenster muss geschützter Zugriff fehlschlagen, und Aufträge müssen der erklärten Delegationsrichtlinie folgen. Beobachten Sie Zustand und Effekte im vorgelagerten System, nicht nur Antwortcodes.

Lassen Sie das vorgelagerte System eine Änderung annehmen und verwerfen Sie dessen Antwort. Eine Wiederholung muss eine unterstützte Idempotenzidentität wiederverwenden oder die Operation zum Abgleich zurückhalten. Ein nicht verfügbarer Anbieter darf nicht als Erfolg erscheinen, und ein Timeout darf Ungewissheit nicht beseitigen. Testen Sie begrenzte Wiederholungen, Warteschlangensättigung und die Geschwindigkeit der Wiederaufnahme anhand der Anbieterquoten; stoppen Sie vor den vereinbarten Ressourcengrenzen. Erfassen Sie blockierte und übersprungene Fälle mit der jeweils fehlenden Voraussetzung.

## Veröffentlichen, wiederherstellen und Verantwortung tragen

Veröffentlichen Sie für eine definierte Mitarbeitergruppe mit einem bekannten Rollback-Artefakt und Schreibvorgängen in vorgelagerten Systemen, die zunächst durch den akzeptierten Einführungsplan begrenzt sind. Unterstützen Sie bei Schemaänderungen gemischte Versionen und ergänzen Sie Daten mit Kontrollpunkten, bevor Felder entfernt werden. Ein Anwendungsrollback kann keine Aktion im vorgelagerten System rückgängig machen. Pausieren Sie die Weitergabe von Aufträgen, prüfen Sie das Protokoll, fragen Sie den Anbieterzustand ab und führen Sie eine fachlich genehmigte Korrektur durch, soweit eine Rücknahme möglich ist. Stellen Sie Audit- und Anwendungsdatensätze gemeinsam wieder her oder erklären Sie, wie Lücken abgeglichen werden.

Überwachen Sie überalterte ausstehende Arbeit, verweigerte Operationen, Widerrufsverzögerung, Exportvolumen, Anbieterdrosselung und Fälle mit manuellem Reparaturbedarf. Benennen Sie getrennte fachliche und technische Verantwortliche sowie eine Eskalationsfrist für unklare Effekte. Berücksichtigen Sie Integrationslizenzen, Mitarbeiterzeit, Audit-Speicher und Rufbereitschaft in Kostenschätzungen. Zu den Produktionslücken gehören eine echte SSO-Integration, Sitzungsrichtlinie, Notfallzugriff, verfügbare Freigabeverantwortliche, Aufbewahrung und Incident-Übungen. Die Stilllegung erfordert den Abschluss ausstehender Vorgänge, die Übergabe notwendiger Audit-Datensätze, die Benachrichtigung der Prozessverantwortlichen, den Widerruf des Dienstzugriffs und den Nachweis, dass geplante Aufträge keine Schreibvorgänge mehr auslösen.

## Mit verwandten Entscheidungen fortfahren

[Sicherheit](security.md) · [Betrieb](operations.md) · [Teststrategie](testing-strategy.md) · [Dauerhaftigkeit](durability.md)

## Primärquellen

[owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-session](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Session_Management_Cheat_Sheet.md) · [azure-idempotent-consumer](https://raw.githubusercontent.com/MicrosoftDocs/architecture-center/afb6a29f8871e2d9a49bfe407ef980a0db3aabd9/docs/patterns/idempotent-consumer.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md)
