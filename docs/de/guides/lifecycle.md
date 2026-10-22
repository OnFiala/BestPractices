---
{
  "id": "lifecycle",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Der vollständige Projektlebenszyklus

## Phasen mit Abnahmekriterien

| Phase | Erforderliches Ergebnis | Nachweis |
| --- | --- | --- |
| Erkunden | Problem, Beteiligte und Datenkarte | Messbarer Nutzen und ausdrückliche Nichtziele |
| Entwerfen | Profil, Kontextdiagramm, ADR, Bedrohungsmodell | Menschlich akzeptierte Einschränkungen und Wiederherstellungsziele |
| Planen | Kleine Aufgaben, Abhängigkeiten, Abnahmebeispiele | Verantwortung, Umfang, Tests und Abbruchbedingungen |
| Bauen | Code, Migrationen, Tests, Erklärungen | Reproduzierbare Prüfungen und sichtbarer Diff |
| Veröffentlichen | Version, Hinweise, Rollout und Rollback | Staging-Smoke-Test, Wiederherstellungsbereitschaft, Freigabe |
| Betreiben | Runbook, Dashboards, Support- und Kostenverantwortung | Gemessene Ziele und geübte Wiederherstellung |
| Weiterentwickeln | Vorfallwissen, Abkündigung und Migration | Verbraucher wechseln vor der Entfernung |
| Stilllegen | Datenexport/Löschung und Zugriffsentzug | Aufbewahrung erfüllt; Abrechnung und Zugänge beendet |

Die gleichen Prüfpunkte haben unterschiedliche Tiefe. Ein persönliches Skript kann mit einem kurzen Dokument auskommen; folgenreiche Systeme brauchen stärkere unabhängige Nachweise. Jedes Dokument muss einer Entscheidung oder Betriebsaktion dienen.

## Vertrag zwischen Mensch und Agent

Menschen bestimmen Nutzen, Prioritäten, Risikotoleranz und Freigaberecht. Agenten untersuchen, schlagen vor, implementieren, testen und benennen Unsicherheit. Eine Aufgabe endet mit Belegen. Annahmen gehören ins Repository statt ausschließlich in Chatverläufe.

## Prüfen und umsteuern

Vor weiteren Funktionen einen vollständigen Nutzerpfad demonstrieren, einschließlich Fehlern, verweigertem Zugriff, Leerzustand und Wiederherstellung. Ohne messbaren Nutzen zurück zur Erkundung. Übersteigen Betriebskosten oder Verantwortung die Kapazität, zuerst vereinfachen. Die Stilllegung beginnt bereits bei der Planung: Nutzer brauchen einen Ausstieg und Zugang zu ihren Daten.

## Verwandte Entscheidungen

[Qualitätsprüfungen mit Verhaltensnachweis](quality.md) · [Zustand, Wiederherstellung und Kosten](operations.md) · [Menschen steuern, Agenten führen aus](agents.md) · [Die Bibliothek im Projekt einsetzen](adoption.md)

## Primärbelege

[github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md) · [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/backup.sgml)
