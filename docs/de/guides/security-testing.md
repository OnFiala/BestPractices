---
{
  "id": "security-testing",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Sicherheitstests auswählen und durchführen

## Mit der gefährdeten Grenze beginnen

Sicherheitstests liefern Belege zu einer ausdrücklichen Bedrohung und Kontrolle. Bestimme vor der Scannerwahl Akteur, Eintrittspunkt, geschütztes Gut, erwartete Berechtigung und mögliche Wirkung. Verknüpfe passende Anforderungen aus einer benannten Standardversion wie ASVS und entwirf einen Test, dessen Ergebnis die behauptete Wirksamkeit der Kontrolle widerlegen kann.

Black-Box-Tests nutzen beobachtbare Schnittstellen ohne Implementierungsinterna. Sie sind kein Synonym für Sicherheitstests. Gray-Box-Prüfungen können Testzugangsdaten, Schemawissen oder Telemetrie verwenden; White-Box-Prüfungen beziehen Code und Konfiguration ein. Verbinde Perspektiven, wenn es sinnvoll ist: Ein Codereview kann einen fehlenden Mandantenfilter erkennen, während eine Anfrage aus einem anderen Mandanten zeigt, ob der bereitgestellte Pfad Daten offenlegt.

## Sich ergänzende Verfahren auswählen

| Verfahren | Passender Anlass | Was es allein nicht belegt |
| --- | --- | --- |
| Quellcodeanalyse und gezieltes Codereview | Neue Parser, Abfragen, Darstellung, Datei-/Netzwerkzugriffe oder privilegierte Pfade | Tatsächliche Laufzeitkonfiguration, vollständige fachliche Autorisierung oder Abwesenheit aller Schwachstellen |
| Abhängigkeits- und Imageanalyse | Neue Abhängigkeiten, Lockdatei-/Imageupdates oder neue Schwachstellenmeldungen | Ausnutzbarkeit in dieser Bereitstellung oder Korrektheit eigener Anwendungslogik |
| Secret-Scanning | Geänderte Dateien, Build-Artefakte und relevante Historie | Erkennung sämtlicher offengelegter Zugangsdaten oder deren Widerruf durch Löschen einer Datei |
| Infrastruktur- und Konfigurationsreview | Änderungen an Netzwerk, IAM, Speicher, TLS, CI oder Bereitstellung | Übereinstimmung tatsächlich bereitgestellter Einstellungen mit dem Vorschlag ohne gesonderte Prüfung |
| Dynamischer Scan einer kontrollierten Testbereitstellung | Geänderte Web-/API-Oberfläche oder Konfiguration | Vollständige Zugriffskontrolle oder Sicherheit komplexer Abläufe; authentifizierte Abdeckung kann lückenhaft sein |
| Manuelle Missbrauchsfälle und gezielte API-/Browsertests | Änderungen an Authentifizierung, Berechtigungen, Mandanten, Wiederherstellung, Geschäftslogik oder Agentenwerkzeugen | Breite Abdeckung, solange Pfade, Rollen und ausgelassene Fälle nicht dokumentiert sind |
| Fuzzing oder eigenschaftsbasierte Grenzprüfungen | Parser, Dateiformate, Protokolle oder Validierung verarbeiten nicht vertrauenswürdige Daten | Korrektheit außerhalb des Eingabemodells oder Gültigkeit der angenommenen Sicherheitseigenschaft |

Wähle Werkzeuge passend zu Sprache, Framework, Protokoll und beabsichtigtem Prüfumfang. Ein Scannerergebnis ist zunächst ein möglicher Befund. Prüfe Erreichbarkeit, Voraussetzungen, Auswirkungen und Reproduzierbarkeit vor der Einstufung. Ein leerer Bericht bedeutet, dass unter dieser Konfiguration nichts gefunden wurde; er ist kein Sicherheitszertifikat.

## Konkrete Prüfungen für häufige Grenzen

Erzeuge für Objektberechtigungen zwei verschiedene Mandanten und mehrere Rollen. Prüfe Lesen, Ändern, Löschen, Auflisten, Suche, Export und asynchrone Pfade mit Kennungen außerhalb des erlaubten Bereichs. Beziehe zwischengespeicherte Antworten und Rechteänderungen ein. Kontrolliere die Ablehnung sowie das Ausbleiben von Offenlegung und Veränderung. Nur die Benutzeroberfläche zu variieren reicht nicht.

Prüfe bei Sitzungen Abmeldung, Widerruf, Ablauf, Rechteänderungen, Kontowiederherstellung und die Wiederverwendung alter Zugangsdaten. Teste bei Cookie-authentifizierten Schreibzugriffen den CSRF-Schutz des Frameworks. Beziehe bei Darstellung und Eingaben die tatsächlichen Anwendungskontexte ein: HTML, Datenbankabfragen, Dateipfade, Uploads und strukturierte Nachrichten. Prüfe begrenztes Fehlverhalten, ohne einen unkontrollierten externen Endpunkt aufzurufen.

Nutze für ausgehende Abrufe kontrollierte Testziele, um Weiterleitungen, Adressänderungen und unerlaubte Ziele zu prüfen. Untersuche die wirksame Netzwerkrichtlinie ebenso wie die Eingabevalidierung. Cloud-Metadaten, interne Dienste und echte Secrets bleiben außerhalb des Tests, sofern sie nicht ausdrücklich Teil einer autorisierten Prüfung sind.

Teste bei Agenten feindselige abgerufene Inhalte, gefälschte Werkzeugausgaben, unberechtigte Argumente, wiederverwendete Freigaben, nachträglich veränderte Parameter, vergiftetes dauerhaftes Gedächtnis und delegierte Aufforderungen zu weitergehenden Rechten. Prüfe, dass die Ausführungsebene verbotene Wirkungen verhindert, selbst wenn das Modell sie anfordert. Nimm legitime Aufgaben auf, damit ein System, das alles abweist, nicht fälschlich als nützlich und sicher gilt.

Untersuche bei Lieferketten- und CI-Grenzen, wie nicht vertrauenswürdiger Code, Workflowänderungen, Installationsskripte von Abhängigkeiten oder heruntergeladene Artefakte Zugangsdaten beziehungsweise Veröffentlichungsrechte erreichen könnten. Prüfe die Grenze nötigenfalls mit isolierten Testdaten. Nutze kein echtes Secret, um einen möglichen Secret-Abfluss zu beweisen.

## Einsatzregeln für Agenten

Das Aufgabenpaket nennt vom Verantwortlichen genehmigte Ziele, erlaubte Identitäten und Verfahren, Zeitfenster, Lastgrenzen, Datenregeln, externe Abhängigkeiten, Abbruchbedingungen und Meldestelle. Verwende nach Möglichkeit eine isolierte Bereitstellung mit synthetischen Konten. Prüfe, dass Testzugangsdaten nicht versehentlich die Produktion erreichen können.

Die Erlaubnis, ein Repository zu lesen, autorisiert keinen aktiven Scan seines Produktionsdienstes. Umfassender Projektzugriff autorisiert weder Stressverkehr noch zerstörerische Eingaben, externe Rückrufe oder fremde Ziele. Kläre vor solchen Operationen den fehlenden Umfang; statische Analyse und Vorbereitung können unabhängig fortgesetzt werden.

Stoppe aktive Prüfungen, wenn das Ziel den erlaubten Umfang verlässt, unerwartet echte Nutzerdaten auftauchen, der Dienstzustand vereinbarte Grenzen überschreitet oder Eindämmung beziehungsweise Bereinigung scheitert. Sichere minimale, bereinigte Belege und informiere den Verantwortlichen über den autorisierten Kanal. Vergrößere nicht den Schaden, um einen Befund eindrucksvoller zu machen.

## Bewerten, beheben und nachprüfen

Ein nützlicher Befund nennt getestete Revision und Konfiguration, exakten betroffenen Pfad, Akteur, Voraussetzungen, beobachtetes Verhalten, erwarteten Schutz, Auswirkungen und eine minimale Reproduktion. Trenne bestätigte, widerlegte und ungeklärte Kandidaten. Veröffentliche in öffentlichen Issues weder Zugangsdaten noch personenbezogene Datensätze oder unmittelbar missbrauchbare Produktionsdetails.

Prüfe eine Korrektur gegen die ursprüngliche Reproduktion und eine erlaubte legitime Operation. Ergänze eine Regression, die das zugrunde liegende Grenzversagen erkennt, nicht nur eine einzelne Eingabe. Untersuche verwandte Pfade, wenn der Fehler aus einem gemeinsamen Entwurf stammt. Dokumentiere Restrisiko und menschliche Annahme, wenn die vollständige Behebung aufgeschoben wird.

Veröffentlichungsentscheidungen beruhen auf Bedrohungsmodell und Belegen, nicht auf einem universellen Scannerwert. Eine ungeklärte Grenze mit schwerwiegenden Folgen blockiert die betroffene Veröffentlichung, sofern kein qualifizierter Mensch eine dokumentierte Ausnahme ausdrücklich verantwortet. Wiederhole gezielte Prüfungen bei Änderungen an Rechten, exponierten Oberflächen, Datensensibilität, Abhängigkeiten oder Agentenfähigkeiten.

## Belege und verwandte Entscheidungen

OWASP ASVS liefert versionierte Prüfanforderungen; die Leitfäden zu Autorisierung, Mandanten und Agenten liefern konkrete Bedrohungs- und Kontrollzusammenhänge. GitHub erläutert Vertrauensgrenzen von Workflows. Auswahlmatrix und Einsatzregeln sind eigenständige lokale Richtlinien. Keine Quelle wird als Empfehlung dieses konkreten Projekts ausgegeben.

[Sicherheitsarchitektur](security.md) · [Teststrategie](testing-strategy.md) · [Qualitätsprüfungen](quality.md) · [Menschen steuern, Agenten führen aus](agents.md) · [Leistungs- und Stresstests](performance-testing.md)

## Primärbelege

[owasp-asvs-requirements](https://raw.githubusercontent.com/OWASP/ASVS/3383877f732ce89a458a1af43288f2f1b1d7db0c/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-multi-tenant](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.md) · [owasp-session](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Session_Management_Cheat_Sheet.md) · [owasp-ssrf](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md)
