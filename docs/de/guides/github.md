---
{
  "id": "github",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# GitHub, Versionen und saubere Arbeitsbäume

## Nachvollziehbarer Ablauf

`main` veröffentlichbar halten. Kurze Zweige pro Änderung und kleine verständliche Commits verwenden. Einen sinnvollen prüfbaren Schritt committen, keine Geheimnisse oder Caches. `feat:`, `fix:` und `docs:` sind lokale Konventionen, keine Erklärung.

PRs beschreiben Problem, Verhalten, Nachweise, Risiken und Rollback. Den endgültigen Diff prüfen, nicht nur Agentenzusammenfassungen. Checks, passende Code-Owner-Prüfung, geklärte Diskussionen und neue Freigabe wesentlicher Änderungen verlangen. Agenten genehmigen oder mergen nicht selbst. Rulesets müssen Force-Push, Löschen und direkte Änderungen an `main` sperren; Dateien aktivieren sie nicht.

SemVer für definierte öffentliche Verträge verwenden. Bewusste Releases taggen, Änderungen und Migration dokumentieren; Tags nicht still ersetzen. Nicht jeder Commit ist ein Release. Leitfaden-IDs und Metadaten sind hier Verträge; Brüche benötigen Migration und Versionsentscheidung.

## Sauberkeit

Vor Änderungen Status prüfen und fremde Arbeit bewahren. Ausgaben ignorieren; Staging und Löschungen kontrollieren. Kein pauschales Reset/Clean. Gemergte Zweige erst ohne lokale Restarbeit löschen; Referenzen separat bereinigen. Worktrees in dieser Cloud nur auf ausdrücklichen Wunsch. Verlassene Zweige benötigen Verantwortung und Frist.

## Verwandte Entscheidungen

[Qualitätsprüfungen mit Verhaltensnachweis](quality.md) · [Menschen steuern, Agenten führen aus](agents.md) · [Belege und automatische Pflege](maintenance.md)

## Primärbelege

[github-rulesets](https://raw.githubusercontent.com/github/docs/main/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/main/content/actions/reference/security/secure-use.md) · [semver](https://raw.githubusercontent.com/semver/semver/master/semver.md)
