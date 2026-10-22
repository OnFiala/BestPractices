---
{
  "id": "quality",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Qualitätsprüfungen mit Verhaltensnachweis

## Nachweise aus der Änderung ableiten

Tests gehören zur Aufgabendefinition eines Agenten. Benenne vor der Implementierung das gefährdete Verhalten, die Folgen eines Fehlers und die Beobachtung, die einen Defekt nachweisen würde. Wähle mit der [Teststrategie](testing-strategy.md) angemessene Prüfungen. Sicherheitsrelevante Grenzen benötigen zusätzlich [Sicherheitstests](security-testing.md); Änderungen an Parallelität, Ressourcen oder Kapazität benötigen [Leistungstests](performance-testing.md).

Eine Textkorrektur braucht redaktionelle Prüfungen und Linkkontrollen, keine neue Testbibliothek voller Mocks. Eine Zahlungswiederholung, ein Mandantenfilter, eine Datenbankmigration oder ein privilegiertes Werkzeug braucht Nachweise zu seinen Fehlerpfaden. „Alle bisherigen Tests bestehen“ beantwortet nicht, ob der geänderte Vertrag geprüft wird.

## Nachweise vor der Implementierung planen

Das Aufgabenpaket nennt betroffene Verbraucher, erwartetes Erfolgs- und Ablehnungsverhalten, repräsentative Daten, Ausführungsumgebung und akzeptables Ergebnis. Nimm mindestens einen relevanten Negativ- oder Grenzfall auf, wenn ein Fehler folgenreich sein kann. Erwartungswerte müssen unabhängig vom implementierten Algorithmus sein: Ein Test, der dieselbe falsche Formel erneut berechnet, kann mit dem Fehler übereinstimmen.

Zeige bei einer Fehlerbehebung nach Möglichkeit, dass die gezielte Prüfung das ursprüngliche Fehlverhalten erkennt. Fordere bei einer neuen Invariante den Test mit absichtlich ungültigen Testdaten oder einer vorübergehenden lokalen Codeveränderung heraus. Entferne diese Veränderung vor dem Änderungsvorschlag. Diese Bibliothek empfiehlt solche Prüfungen nach Risiko; sie verlangt weder Mutationstests für jede Bearbeitung noch einen universellen Prozentsatz der Testabdeckung.

## Einen nützlichen Auslieferungsprozess aufbauen

Verlange eine reproduzierbare Installation der Abhängigkeiten und einen zum Stack passenden Build. Ergänze Typ-, Lint- und statische Prüfungen, wenn sie plausible Fehler erkennen. Führe zuerst gezielte Verhaltenstests und danach die betroffene Integrations- oder Vertragstestsuite aus. Nutze echte Implementierungen der Schnittstellen, wenn Isolation, Transaktionen, Serialisierung, Browserereignisse oder Berechtigungen untersucht werden. Mocks allein können diese Eigenschaften nicht nachweisen.

Pflege wenige Ende-zu-Ende-Abläufe für wertvolle Nutzerergebnisse und ihre kritischen Fehlerzustände. Verwende isolierte Konten und synthetische Daten. Kontrolliere externe Abhängigkeiten in wiederholbaren Tests; prüfe die tatsächliche Kompatibilität mit Anbieter-Sandboxen gesondert und klar begrenzt. Ein E-Mail- oder Zahlungstest darf nicht versehentlich echte Kunden kontaktieren oder ein reales Konto belasten.

Ein fehlgeschlagener Pflichtcheck muss den Auslieferungsjob fehlschlagen lassen. Berichte bestandene, fehlgeschlagene, übersprungene, vorübergehend ausgesetzte und nicht ausgeführte Fälle getrennt. Senke keinen Grenzwert und entferne keine Prüfung allein, um eine Änderung durchzubringen. Eine tatsächlich geänderte Anforderung benötigt Begründung und menschliches Review. Vorübergehend ausgesetzte instabile Tests benötigen Verantwortlichen, Grund, Ablaufdatum und Ersatznachweise für das geschützte Verhalten.

## Nachweise für KI-erzeugte Änderungen

Prüfe den endgültigen Diff und die Tests gemeinsam. Das Review soll Annahmen der Implementierung hinterfragen, nicht nur denselben Prompt wiederholen. Nutze repräsentative Regressionen für Änderungen an Modellen, Prompts, Werkzeugen, Retrieval und Richtlinien. Trenne Entwicklungsbeispiele von zurückgehaltenen Evaluationsfällen. Bewerte sowohl die nützliche Aufgabenerfüllung als auch unerwünschte Effekte. Eine überzeugende Antwort beweist keine sichere Werkzeugausführung.

Halte Modell und Konfiguration, Testdatenversion, Werkzeugrichtlinie, Wiederholungen, Bewertungsmaßstab und beobachtete Streuung fest. Kalibriere modellgestützte Bewertungen mit menschlich geprüften Beispielen und nach Möglichkeit deterministischen Prüfungen. Schütze Evaluationsdaten vor mandantenübergreifendem Abfluss und Prompt Injection. Ein Wechsel des Evaluationsprodukts oder Anbieters hebt diese Anforderungen nicht auf.

## Veröffentlichung und langfristige Pflege

Der Agent liefert die genaue Revision, Befehle, Umgebung, Ergebnisse, bekannte Lücken und den Wiederherstellungsplan. Stoppe die betroffene Veröffentlichung, wenn ein Pflichtcheck fehlschlägt, folgenreiches Verhalten ungeprüft bleibt oder Nachweise dem behaupteten Ergebnis widersprechen. Ein Mensch kann eine befristete Ausnahme mit Verantwortlichem und ausgleichender Kontrolle dokumentieren. Der Agent darf einen Fehler nicht stillschweigend zum Erfolg umdeuten.

Verfolge unentdeckte und erst später auftretende Defekte, instabile Prüfungen, langsame Rückmeldungen und die Wiederherstellung nach Änderungen. Ergänze nach einem bedeutsamen Vorfall eine gezielte Regression. Entferne Prüfungen nur, wenn ihr Schutzzweck entfällt oder anders besser abgedeckt wird. Ziel sind belastbare Nachweise zu tragbaren Kosten, nicht möglichst viele Tests.

## Diese Bibliothek und der Umfang ihrer Belege

Dieses Repository prüft Inhaltsidentitäten, Quellenverweise, Übersetzungsrevisionen, Links, Integrationsverhalten und Website-Erzeugung. Diese Prüfungen zertifizieren weder Architekturhinweise noch die Bedeutung von Übersetzungen. Menschliches redaktionelles Review bleibt eine eigenständige Voraussetzung.

Der beschriebene Ablauf ist eine eigenständige lokale Zusammenführung. Playwright stützt isolierte, nutzerorientierte Browsertests; OWASP behandelt Autorisierungs- und Agentenmissbrauchstests; GitHub dokumentiert Vertrauensgrenzen in Workflows. Diese Quellen sind weder ein universeller Teststandard noch eine Empfehlung dieser Bibliothek durch die Herausgeber.

## Verwandte Entscheidungen

[Teststrategie](testing-strategy.md) · [Leistungs- und Stresstests](performance-testing.md) · [Sicherheitstests](security-testing.md) · [Menschen steuern, Agenten führen aus](agents.md) · [Der vollständige Projektlebenszyklus](lifecycle.md)

## Primärbelege

[playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [owasp-authorization](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/Authorization_Cheat_Sheet.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md)
