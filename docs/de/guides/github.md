---
{
  "id": "github",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# GitHub, Versionen und saubere Arbeitsbäume

## Ein prüfbarer Ablauf

Halte `main` veröffentlichbar. Nutze kurzlebige Branches für jeweils eine Änderung und kleine zusammenhängende Commits, die die Absicht erklären. Committe, sobald ein sinnvoller Schritt verstanden und geprüft werden kann; warte nicht auf das gesamte Projekt und committe keine erzeugten Secrets oder Caches. `feat:`, `fix:` und `docs:` sind nützliche lokale Konventionen, kein Ersatz für eine klare Beschreibung.

Eröffne einen PR mit Problem, Verhalten, Nachweisen, Risiken und Rollback. Prüfe den endgültigen Diff, nicht nur die Agentenzusammenfassung. Verlange Statusprüfungen, gegebenenfalls Code-Owner-Review, geklärte Diskussionen und eine erneute Freigabe nach wesentlichen Änderungen. Agenten genehmigen oder mergen niemals ihre eigene Arbeit. Konfiguriere einen Regelsatz, der Force-Push, Löschung und direkte Änderungen an `main` blockiert; Dateien allein aktivieren ihn nicht.

Nutze SemVer für einen definierten öffentlichen Vertrag. Markiere bewusste Veröffentlichungen mit Tags, veröffentliche Changelog und Migrationshinweise und ersetze einen Release-Tag niemals stillschweigend. Interne Commits müssen keine Releases sein. In dieser Bibliothek sind Leitfaden-IDs und Metadaten Verträge: Ihre inkompatible Änderung benötigt eine Migration und Versionsentscheidung.

## Sauberkeit

Prüfe vor Änderungen den Status und bewahre andere Arbeit. Ignoriere erzeugte Ausgaben; prüfe vor einem Commit vorgemerkte Dateien und versehentliche Löschungen. Nutze niemals pauschale Reset-/Clean-Befehle. Lösche gemergte Branches erst, nachdem du geprüft hast, dass keine nur lokal vorhandene Arbeit verbleibt; bereinige Referenzen getrennt. Nutze Worktrees in dieser Cloud-Umgebung nur bei Bedarf und auf ausdrückliche Anforderung. Erfasse aufgegebene Branches mit Verantwortlichem und Ablaufdatum.

## Verwandte Entscheidungen

[Qualitätsprüfungen mit Verhaltensnachweis](quality.md) · [Menschen steuern, Agenten führen aus](agents.md) · [Belege und automatische Pflege](maintenance.md)

## Primärbelege

[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [semver](https://raw.githubusercontent.com/semver/semver/f99d5485190a47c0863949e7da810a5553e0ed4d/semver.md)
