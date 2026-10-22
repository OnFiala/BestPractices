---
{
  "id": "agents",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Menschen steuern, Agenten führen aus

## Begrenzte Delegation

Ein Aufgabenpaket enthält Nutzen, Leitfaden-IDs, Grenzen, erlaubte Dateien/Werkzeuge, Abnahmebeispiele, Budget und Abbruchbedingungen. Menschen besitzen Architektur und Risiko; Agenten untersuchen und bauen. Implementierung, Prüfung und menschliches Review trennen, auch bei mehreren Durchläufen eines Modells. Wiederholung ist kein unabhängiger Beleg.

Responses API für eine selbst gesteuerte Ausführungsschleife verwenden; Agents SDK bei belegtem Orchestrierungsbedarf erwägen. Mit einem Agenten beginnen. Parallele Arbeit braucht unabhängige Aufgaben, Schreibverantwortung, Koordination und Gesamtbudget.

## Steuerung

Werkzeugrechte, eingeschränkte Identitäten, Timeouts, Iterations-, Token- und Kostenlimits sowie Laufkennungen festlegen. Guardrails ersetzen weder Autorisierung noch Isolation. Quellen und Werkzeugantworten können Prompt Injection enthalten. Bei Konflikten, fehlenden Voraussetzungen, unerwarteter Zerstörung oder fehlgeschlagenen Pflichtprüfungen stoppen.

## Abnahme und Evaluation

Diff, ausgeführte Prüfungen, Unsicherheiten und Wiederherstellung verlangen. Repräsentative, adversarielle und Fehlerfälle auswerten. Aufgabenerfolg, menschliche Korrekturen, entwichene Fehler, Latenz und Kosten messen, nicht Codeumfang. Regressionen für Prompt-, Modell-, Werkzeug- und Richtlinienwechsel halten. Neuere Modelle nicht allein wegen ihres Namens oder Datums übernehmen.

## Verwandte Entscheidungen

[Qualitätsprüfungen mit Verhaltensnachweis](quality.md) · [Sicherheit, Datenschutz und Lieferkette](security.md) · [Belege und automatische Pflege](maintenance.md) · [Skills, Plugins, MCP und WebMCP](integrations.md)

## Primärbelege

[openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/main/docs/agents.md) · [agents-guardrails](https://raw.githubusercontent.com/openai/openai-agents-python/main/docs/guardrails.md) · [codex-action](https://raw.githubusercontent.com/openai/codex-action/main/README.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/main/README.md)
