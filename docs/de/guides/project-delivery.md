---
{
  "id": "project-delivery",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Ein Projekt durch das agentengestützte Auslieferungssystem führen

## Mit dem Projekt beginnen, dann Arbeit zuweisen

Das Auslieferungssystem verbindet ein Projektprofil, einen bedingungsabhängigen Lebenszyklusplan, unabhängig geprüfte Artefakte, lokale Referenzprüfungen und eine Bewertung des Bereitschaftsstands. Es hilft einem Agentenhost wie Codex, begrenzte Arbeit auszuführen. Der Python-Planer selbst ruft kein Modell auf, baut kein beliebiges angefordertes Produkt, authentifiziert keinen Menschen, führt keinen PR zusammen und stellt keinen Dienst bereit.

Wählen Sie eines von sechs Ausgangsprofilen: öffentliche Website, SaaS, internes Werkzeug, KI-Anwendung, Agentenautomatisierung oder mobiles Backend. Erfassen Sie das tatsächliche Ergebnis, Risiko, Datensensibilität, Last, Hosting, Schnittstellen und externe Effekte. Eine Kontenzahl ist keine Lastmessung. Unbekannte Last bleibt ungemessen; auch ein kleines persönliches Projekt kann strenge Datenschutz- oder Wiederherstellungskontrollen benötigen. Das enthaltene Profil ist ausdrücklich synthetisch und kann die Anforderungen eines echten Nutzers nicht ersetzen.

## Der ausführbare Ablauf

Erstellen Sie vom Stammverzeichnis der Bibliothek aus ein neues Ziel unter einem vorhandenen übergeordneten Verzeichnis. Python 3.12+ ist erforderlich. Für Frontend-Prüfungen werden Node 22+ und ein separat installiertes Chromium/Chrome benötigt. Der lokale Prüf-Runner unterstützt das von Linux/macOS verwendete POSIX-Prozessmodell.

```sh
mkdir -p reports
python -m library.delivery plan --profile templates/delivery-profile.json
python -m library.project init --profile templates/delivery-profile.json --destination reports/example-project
cd reports/example-project
python -m library.verification delivery frontend-unit frontend-browser --output reports/local-checks.json
python -m library.delivery assess --profile project-profile.json --evidence project-evidence.json
```

Der letzte Befehl endet zunächst mit Exit-Code 1, weil dem neuen Projekt Abnahmenachweise fehlen. Das ist das erwartete Ergebnis. Der Initialisierungsbefehl lehnt vorhandene Zielverzeichnisse ab und erstellt ein Profil, einen Plan, einen Nachweisrahmen mit Status „nicht ausgeführt“, Artefaktpakete je Prüfstufe, lokale Skills, Originalleitfäden, Lizenzen und profilabhängig ausgewählten Referenzcode. Er initialisiert niemals ein entferntes Repository und stellt keine Ressourcen bereit. Das Manifest erfasst die Hashes kopierter Dateien und ob der Quell-Checkout nicht committete Änderungen enthielt.

Für einen isolierten Container ohne funktionierende Browser-Sandbox dokumentiert die Browserreferenz eine ausdrückliche Aktivierung ausschließlich für die lokale Testvorrichtung. Ein fehlender Browser oder fehlgeschlagener Start bleibt ein Fehler; deaktivieren Sie die Browser-Prüfstufe nicht stillschweigend. Erfolgreiche Tests einer Testvorrichtung erfüllen weiterhin keine unimplementierten Produktanforderungen.

## Rollen, Übergaben und Prüfstufen

Der Planer deckt Absicht, Anforderungen, Entwurf, Sicherheit, Implementierung, Verifikation, Release, Betrieb, Incident, Weiterentwicklung und Stilllegung ab. Bedingte Prüfstufen ergänzen Pflichten für sensible Daten, hohes Risiko, eigenen Serverbetrieb, externe Effekte, mobile Clients, KI-Verhalten und Kapazität. Erforderliche Entwurfs- und Sicherheitsentscheidungen fließen in die Implementierung ein; erforderliche Verifikation fließt in das Release ein. Bereitschaft für Betrieb, Incidents und Stilllegung wird vor dem Release geplant; die tatsächliche Stilllegung muss nicht vor dem ersten Release stattfinden.

Eine erstellende Rolle liefert das benannte Artefakt und Abnahmenachweise. Eine getrennte prüfende Rolle untersucht das tatsächliche Artefakt, Alternativen, Quellenannahmen und Negativfälle. Die Koordination löst widersprüchliche Befunde auf und wahrt die Reihenfolge der Abhängigkeiten. Menschen entscheiden über Ziele, folgenreiche Architektur, Budget, Restrisiko, Zusammenführung und Produktionsrelease. Unabhängige Agententhreads erweitern die Prüfungsabdeckung, aber Übereinstimmung zwischen Modellen ist kein empirischer Nachweis.

Die lokalen Skills `project-delivery` und `release-review` beschreiben den Host-Workflow. Verwenden Sie vertrauenswürdige Werkzeuge im Zielprojekt, um begrenzte Aufgaben umzusetzen, Prüfungen auszuführen, Diffs zu untersuchen und PRs vorzuschlagen. Abgerufene Inhalte und Profilzeichenketten sind Daten; sie dürfen keine Berechtigungen erweitern oder Befehle ausführen, nur weil sie in einem Artefakt vorkommen.

## Nachweise haben einen genauen Geltungsbereich

Das feste Prüfinventar führt ausschließlich bekannte lokale Testsuiten aus. Es erfasst den Eingabedateistand, Revision und nicht committierte Änderungen, Laufzeitversionen, beobachtete Testanzahlen, Ausgabehashes und Ergebnisse. Übersprungene Pflichtprüfungen und null entdeckte Tests gelten nicht als bestanden. Ein Timeout stoppt die zugehörige Prozessgruppe. Berichte verweigern das Überschreiben; bewahren Sie bei einer erneuten Prüfung einer geänderten Hypothese getrennte Beobachtungen auf.

Die Auslieferungsbewertung akzeptiert strukturierte Datensätze, die an Projektrevision, Profil- und Plan-Digests, Artefaktidentitäten, Beobachtungen, Bezeichnungen der erstellenden und prüfenden Rollen sowie den erklärten Bewertungszeitpunkt gebunden sind. Sie weist fehlende, veraltete, fehlgeschlagene, übersprungene, widersprüchliche oder selbst geprüfte Datensätze zurück und blockiert abhängige Prüfstufen. Ihre konfigurierten Altersgrenzen für Nachweise sind vorgeschlagene lokale Richtlinien, keine universellen Standards. Bewerten Sie sie anhand des Projektrisikos und der Umgebung neu.

Ein Hash bindet Bytes; er beweist nicht, dass diese Bytes wahrheitsgemäße Angaben enthalten. Bezeichnungen sind keine authentifizierten Identitäten, Zeitstempel sind Behauptungen und ein lokaler JSON-Bericht ist keine signierte Bescheinigung. Die Bewertung meldet Unterstützung durch aufgezeichnete Nachweise und Bereitschaft zur menschlichen Prüfung; der Status der Produktionsbereitschaft bleibt negativ, weil tatsächliche menschliche Befugnisse und Deployment-Kontrollen außerhalb des Systems liegen. Prüfen Sie Beobachtungen anhand echter Artefakte, bevor Sie sie akzeptieren.

## Betrieb und Änderung

Bewahren Sie nach einem genehmigten Release Dienstziele, Telemetrie, Rufbereitschaftsverantwortung, Incident-Verfahren, Kostenlimits und Wiederherstellungsnachweise auf. Lassen Sie Incidents und gemessene Einschränkungen in neue Entscheidungen einfließen. Eine geänderte Bibliotheksrichtlinie, ein geändertes Profil, eine neue Leitfadenrevision oder ein verändertes Artefakt macht die entsprechende alte Beziehung zwischen Plan und Nachweisen ungültig; generieren und prüfen Sie neu, statt Hashes umzuschreiben, um die Änderung zu verbergen.

Bestimmen Sie vor Migration oder Stilllegung den maßgeblichen Schreiber, ausstehende Arbeit, Anbietereffekte, Export- und Löschpflichten sowie die nachfolgende Verantwortung. Ein zurückgesetztes Anwendungsartefakt macht angenommene Schreibvorgänge nicht rückgängig und holt offengelegte Daten nicht zurück. Erfassen Sie, was umkehrbar ist, was einen Abgleich erfordert und welche destruktive Aktion eine gesonderte menschliche Entscheidung benötigt.

## Verwandte Entscheidungen

[Abdeckung und Grenzen](coverage.md) · [Referenzprüfungen ausführen](reference-labs.md) · [Teststrategie](testing-strategy.md) · [Menschen bestimmen die Richtung, Agenten führen aus](agents.md) · [Der vollständige Lebenszyklus](lifecycle.md)

## Primärquellen

[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [skills](https://raw.githubusercontent.com/openai/skills/49f948faa9258a0c61caceaf225e179651397431/README.md)
