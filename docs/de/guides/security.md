---
{
  "id": "security",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Sicherheit, Datenschutz und Lieferkette

## Risiken in durchsetzbare Grenzen übersetzen

Bevor sensible Daten verarbeitet oder Schreibrechte an Werkzeuge vergeben werden, müssen Schutzgüter, Akteure, Eintrittspunkte und Vertrauensgrenzen feststehen. Beschreibe plausiblen Missbrauch: Ein Nutzer übermittelt die Datensatz-ID eines anderen Mandanten, ein Dokument fordert einen Agenten zum Export von Secrets auf, ein CI-Job führt eine nicht vertrauenswürdige Abhängigkeit aus oder eine Wiederherstellung lädt Daten des falschen Kunden. Ordne jedem folgenreichen Risiko einen Verantwortlichen, eine vorbeugende Kontrolle, ein beobachtbares Fehlverhalten und eine Wiederherstellungsmaßnahme zu.

Wähle eine unterstützte Version eines Prüfstandards wie OWASP ASVS und die zur Anwendung passenden Anforderungen. Dokumentiere versionierte Anforderungskennungen und begründete Ausnahmen. Ein Link auf die ASVS-Übersicht oder eine ausgefüllte Checkliste ist keine Zertifizierung. Dieser Leitfaden ist ein eigenständiger Entscheidungsrahmen und keine Wiedergabe des Standards.

## Identität, Berechtigungen und Mandanten

Nutze gepflegte Authentifizierungskomponenten, statt ein eigenes Passwort-, Sitzungs- oder Tokenprotokoll zu erfinden. Dokumentiere Registrierung, Kontowiederherstellung, Entzug von Zugriffen und stärkere Authentifizierung für sensible Aktionen. Die Feststellung einer Identität und die Entscheidung über ihre Befugnisse sind getrennte Aufgaben.

Die vertrauenswürdige Ausführungsebene muss Akteur, Zielobjekt und gewünschte Operation prüfen. Eine schwer erratbare Kennung, eine ausgeblendete Schaltfläche, ein privates Netzwerk oder eine erfolgreiche Anmeldung belegen keine Berechtigung. Unbekannte Zugriffskombinationen müssen sicher abgewiesen werden. Teste Lese-, Schreib-, Such-, Export-, Verwaltungs- und Hintergrundpfade einschließlich des Zugriffs nach einer geänderten Mitgliedschaft.

Leite den Mandantenkontext aus einer geprüften Mitgliedschaft ab. Er muss Datenbankabfragen, Jobs, Caches, Dateispeicher, Suchindizes und Wiederherstellungen begleiten. Dienen Datenbank-Zeilenrichtlinien als zusätzliche Grenze, prüfe, dass die tatsächliche Laufzeitrolle sie nicht umgeht und wiederverwendete Verbindungen keinen fremden Mandantenkontext behalten. Mandantenübergreifende Verwaltung und globale Exporte für Betreiber sind eigenständige Befugnisse.

Verwende für Browsersitzungen unterstützte Cookie-Schutzmechanismen und bewusst definierte Regeln für Ablauf, Abmeldung, Rotation und Widerruf. Zustandsändernde Anfragen mit Cookie-Authentifizierung brauchen zum Framework passenden CSRF-Schutz; SameSite ist eine ergänzende Kontrolle. Kontowiederherstellung und Rechteänderungen verdienen dieselbe Sorgfalt wie die Anmeldung.

## Daten, Darstellung und ausgehende Anfragen

Private Datensätze, Zugangsdaten und Kundentestdaten gehören nicht in öffentliche Git-Historien, Website-Builds, Client-Bundles oder erzeugte Suchindizes. Eine Anmeldeseite macht öffentlich herunterladbare Dateien nicht privat. Klassifiziere Daten vor ihrer Erhebung und definiere Aufbewahrung, Löschung, Export, Sicherungskopien sowie die Berechtigung zur Untersuchung von Vorfällen.

Validiere Eingaben anhand des Anwendungsvertrags. Nutze parametrisierte Datenbankoperationen sowie gepflegte, zum Ausgabekontext passende Kodierungs- oder Bereinigungsverfahren. Validierung allein verhindert keine Skriptausführung, wenn Daten als HTML dargestellt werden. Beschränke bei Dateiuploads Größe, Typ, Speicherort und Ausführbarkeit.

Ein Server oder Agent, der vom Nutzer beeinflussbare URLs abruft, benötigt eine Richtlinie für ausgehende Anfragen. Begrenze Protokolle, Ziele, Weiterleitungen, Antwortgröße und Dauer. Verhindere Zugriff auf interne Dienste und Cloud-Metadaten, sofern er nicht ausdrücklich benötigt und autorisiert ist. Prüfe aufgelöste Ziele an der Netzwerkgrenze, damit DNS-Änderungen oder Weiterleitungen eine scheinbar erlaubte URL nicht in einen internen Zugriff verwandeln.

## Grenzen für Agenten und die Softwarelieferkette

Behandle abgerufene Texte, Werkzeugausgaben, Modellausgaben und delegierte Nachrichten als nicht vertrauenswürdige Daten. Erzwinge Werkzeugrechte außerhalb des Modells: Binde Identität und Ressourcenumfang, validiere Argumente und halte sensible Zugangsdaten im ausführenden Dienst. Eine Freigabe für eine folgenreiche Operation muss Aktion und Parameter festlegen, ablaufen und gegen Wiederverwendung geschützt sein. Weder eine Werkzeugannotation noch die Aussage „freigegeben“ eines Agenten verleiht Befugnisse.

Begrenze Laufzeit, Wiederholungen, Parallelität, Tokens und Ausgaben dort, wo sich diese Grenzen tatsächlich durchsetzen lassen. Trenne Gedächtnis und Retrieval nach berechtigten Nutzern oder Mandanten. Teste indirekte Prompt Injection, Informationsabfluss, Richtlinienänderungen und Übergaben zwischen Agenten. Guardrails können Fehler reduzieren, sind aber keine Sicherheitsgrenze.

Trenne Identitäten für Entwicklung, Build, Bereitstellung und Laufzeit. Halte Secrets aus dem Repository heraus und nutze nach Möglichkeit eingeschränkte, kurzlebige Zugangsdaten. Fixiere aufgelöste Abhängigkeitsversionen mit einer Lockdatei, prüfe Updateherkunft und Lizenzen und beobachte Schwachstellen. Fixiere CI-Actions auf unveränderliche Commits und prüfe, wer Workflows, Artefakte und die Auflösung von Abhängigkeiten ändern darf. Gib nicht vertrauenswürdigen PR-Ausführungen niemals Produktionszugangsdaten und Agenten keinen Zugriff auf den Docker-Socket des Hosts.

## Prüfen, reagieren und neu bewerten

Verbinde Bedrohungen mithilfe des [Leitfadens zu Sicherheitstests](security-testing.md) mit automatisierten und manuellen Nachweisen. Prüfe vor der Veröffentlichung sensibler Funktionen unbefugte Zugriffe, Mandantentrennung, Widerruf, Wiederherstellung und den Missbrauch privilegierter Werkzeuge. Logs müssen Untersuchungen ermöglichen, ohne Zugangsdaten oder unnötige personenbezogene Daten offenzulegen. Schütze auch Logzugriff und Aufbewahrung.

Dokumentiere Vorfallkontakt, Eindämmung, Widerruf von Zugangsdaten, Beweissicherung, Wiederherstellung und Meldung. Überarbeite das Bedrohungsmodell nach einer neuen Integration, Rechteänderung, Datenklasse, einem Vorfall oder einer geänderten Architekturgrenze. Rechtliche Pflichten und Risikoakzeptanz liegen bei qualifizierten menschlichen Verantwortlichen.

## Verwandte Entscheidungen

[Sicherheitstests](security-testing.md) · [Teststrategie](testing-strategy.md) · [Menschen steuern, Agenten führen aus](agents.md) · [Daten, Verträge und Migrationen](data.md) · [Eigene Server betreiben](self-hosting.md)

## Primärbelege

[owasp-asvs-requirements](https://raw.githubusercontent.com/OWASP/ASVS/3383877f732ce89a458a1af43288f2f1b1d7db0c/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-multi-tenant](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.md) · [owasp-authentication](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authentication_Cheat_Sheet.md) · [owasp-session](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Session_Management_Cheat_Sheet.md) · [owasp-csrf](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md) · [owasp-xss](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md) · [owasp-ssrf](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md)
