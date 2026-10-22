---
{
  "id": "quality",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Qualitätsprüfungen mit Verhaltensnachweis

## Vertrag statt Implementationskopie testen

Ein grüner Formatter beweist kein funktionierendes Produkt. Tests nach Fehlerfolgen wählen: Einheitstests für Regeln, Integration für Datenbank und Dienste, Verträge für Verbraucher und wenige vollständige Nutzerpfade. Zugriffsverweigerung, ungültige Eingaben, Timeout, Duplikate und Wiederherstellung berücksichtigen. Synthetische Daten und isolierte Nebenwirkungen verwenden.

## Lieferprüfung

Reproduzierbare Installation, passende Build-/Typprüfungen, aussagekräftige Tests und Diff-Review verlangen. Erfolg, Fehler, übersprungen und nicht ausgeführt unterscheiden. Assertions nie für eine Freigabe abschwächen. Flaky Tests brauchen Verantwortung und befristete Quarantäne.

Bei KI-Arbeit prüfen, ob Tests den betreffenden Fehler erkennen können. Unabhängige Reviews betrachten Annahmen und negative Fälle. Snapshots benötigen semantische Prüfungen; Abdeckungsprozente allein beweisen nichts.

## Diese Bibliothek

Validator, Python-Tests, Lint und strikten Bau aller Sprachen ausführen. Fehlende Übersetzungen, alte Revisionen, unbekannte Quellen und kaputte Links werden abgelehnt. Quellenmonitoring ist eine separate Netzbeobachtung; CI beweist weder Fakten noch Übersetzungsqualität.

## Überdenken

Entwichene Fehler, fehlgeschlagene Änderungen, Wiederherstellungszeit und langsame Prüfungen verfolgen. Redundanz ohne Schutzwirkung entfernen, wichtige Nachweise behalten. Menschen entscheiden über ausreichende Evidenz.

## Verwandte Entscheidungen

[GitHub, Versionen und saubere Arbeitsbäume](github.md) · [Menschen steuern, Agenten führen aus](agents.md) · [Der vollständige Projektlebenszyklus](lifecycle.md)

## Primärbelege

[owasp](https://raw.githubusercontent.com/OWASP/ASVS/master/README.md) · [wcag](https://raw.githubusercontent.com/w3c/wcag/main/guidelines/index.html) · [github-workflows](https://raw.githubusercontent.com/github/docs/main/content/actions/reference/security/secure-use.md)
