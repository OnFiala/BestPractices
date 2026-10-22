---
{
  "id": "adoption",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Die Bibliothek im Projekt einsetzen

## Portables Projektpaket

Nur benötigte Vorlagen kopieren. `project-profile.yaml` mit Einschränkungen, Verantwortung, Sensibilität, Budget, Last, SLO und Wiederherstellung ausfüllen. Bibliothek per Release/Commit und Leitfaden-ID referenzieren; Produktionsrichtlinien nicht unbemerkt dem veränderlichen `main` folgen lassen.

Kontextdiagramm und erstes ADR erstellen. Akzeptierte Regeln, begründete Ausnahmen, Verantwortung, Ablauf und Ersatzkontrollen festhalten. Kurze projektspezifische Agentenanweisungen in `AGENTS.md` mit Verweisen pflegen. Aufgabenpaket und Releasecheckliste verwenden.

## Drei Anfänge

- Eine persönliche Wissensseite nutzt statisches Hosting, Git-Historie und reproduzierbaren Bau. Private Notizen benötigen passenden Zugriffsschutz.
- Ein kleines SaaS beginnt mit modularer Anwendung, verwalteter Datenbank und begrenztem Worker. Vor echten Kunden braucht es Mandantenrechte, Zahlungsabgleich, Wiederherstellung und Betriebsverantwortung.
- Eine große Plattform misst Partitionen und isoliert kritische Pfade. Unabhängige Releases und regionale Wiederherstellung brauchen Konsistenz-, Bereitschafts- und Migrationsverantwortung; Kontenzahlen reichen nicht.

## Laufende Nutzung

Bei Planung Leitfäden konsultieren, im Review Entscheidungen und Nachweise verlinken, beim Release Migration und Wiederherstellung prüfen. Betriebserkenntnisse in ADRs zurückführen. Bibliotheksversionen mit einem PR aktualisieren, der geänderte Pflichten und betroffene Projekte erklärt. Vorhandene Vorlagen beweisen keine Einhaltung.

## Verwandte Entscheidungen

[Entscheidungsprinzipien](foundations.md) · [Der vollständige Projektlebenszyklus](lifecycle.md) · [Menschen steuern, Agenten führen aus](agents.md) · [Verantwortung und offene Entscheidungen](governance.md)

## Primärbelege

[plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md) · [github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md)
