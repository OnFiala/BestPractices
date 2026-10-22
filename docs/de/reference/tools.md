---
{
  "id": "tools",
  "language": "de",
  "revision": 2,
  "translation_revision": 2,
  "reviewed_on": "2026-10-22"
}
---
# Quellen und Werkzeuge

Dies ist eine Auswahlliste für eine konkrete Entscheidung, keine Empfehlung für jedes Produkt oder Anweisung, alle Werkzeuge zu installieren. Entscheide anhand der Projektanforderungen und prüfe vor der Übernahme einen repräsentativen Ablauf. Werkzeugnamen und maschinelle Statusschlüssel bleiben über die Sprachen hinweg stabil, damit Menschen und Agenten dasselbe Produkt identifizieren. `candidate` bedeutet: vor der Übernahme evaluieren; `used-here` bezeichnet eine von dieser Bibliothek tatsächlich genutzte Fähigkeit; `experimental` verlangt ausdrückliche Kompatibilitätsprüfungen. Ein eingesetztes Werkzeug eignet sich dadurch nicht automatisch für jedes Projekt.

Das maßgebliche Inventar liegt in `data/tools.json`, das Quellenregister in `data/sources.json`. Website-Exporte enthalten dieselben Inventare. Quellenaufzeichnungen trennen die genau geprüfte Version, die auf Änderungen überwachte URL und Lizenznachweise. Diese Angaben belegen Herkunft und Prüfgrenze, keine Erlaubnis zum Kopieren von Quellentexten. Quellenzahlen belegen keine fachliche Tiefe. Keine unbekannte Lizenz wird als Erlaubnis zur Wiedergabe von Dokumentation behandelt.

| Werkzeug | Status | Quelle |
| --- | --- | --- |
| Codex | `candidate` | [codex](https://raw.githubusercontent.com/openai/codex/b337fe06b7d8d6e5b42295e04c5e92c2b9c46567/README.md), [plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) |
| OpenAI Agents SDK | `candidate` | [openai-agents](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/agents.md), [agents-guardrails](https://raw.githubusercontent.com/openai/openai-agents-python/841dfdd938bfd4ca052475eb76d6245a356868e0/docs/guardrails.md) |
| MCP Python SDK | `used-here` | [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/2af9e3089ac66b35c1550c500aae86a82efb1e17/README.md) |
| WebMCP | `experimental` | [webmcp](https://raw.githubusercontent.com/webmachinelearning/webmcp/51ed75653aaa7f174f8dbe05d1bc327359bbc57c/README.md) |
| MkDocs Material | `used-here` | [mkdocs-material](https://raw.githubusercontent.com/squidfunk/mkdocs-material/cbee8f352745a974e1bae7dc595793be9b6875d7/README.md) |
| GitHub Actions | `used-here` | [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md), [github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) |
| PostgreSQL | `candidate` | [postgres-backup](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/backup.sgml), [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/5ffb8c7409385c58e5c1abaa22ee77ba4c1b5c33/doc/src/sgml/mvcc.sgml) |
| Docker / Compose | `candidate` | [docker-security](https://raw.githubusercontent.com/docker/docs/4d64a8e4f0a59967fc0b391120d54a90e9ccb60d/content/manuals/engine/security/_index.md) |
| Kubernetes | `candidate` | [kubernetes](https://raw.githubusercontent.com/kubernetes/website/bc7f3479bc8b0af48097b155c22c8d58e8e1afe4/content/en/docs/concepts/architecture/_index.md) |
| OpenTofu | `candidate` | [opentofu](https://raw.githubusercontent.com/opentofu/opentofu/ec773ed37be4d07e00d4a2fbb237d0c0fe1ca3ce/README.md) |
| OpenTelemetry | `candidate` | [observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/2cc7b050cecdab1a7daadb6b78ce51b15a18bec8/content/en/docs/concepts/observability-primer.md) |
| Temporal | `candidate` | [durable-workflows](https://raw.githubusercontent.com/temporalio/temporal/e8ee627110a98501103827745aab18aedf312dd0/README.md) |
| Playwright | `candidate` | [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) |
| Grafana k6 | `candidate` | [k6-test-types](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/_index.md), [k6-thresholds](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/using-k6/thresholds.md) |

## Nach der Aufgabe auswählen

Nutze Playwright für beobachtbare Browserabläufe mit isoliertem Zustand und aussagekräftigen Assertions; ein Browserskript ist nicht automatisch eine Barrierefreiheits- oder Sicherheitsprüfung. Nutze k6, wenn repräsentative Arbeitslast, Latenz- und Fehlerschwellen, erlaubte Umgebung und Abbruchbudget festgelegt sind. Bloß mehr Anfragen zu erzeugen ergibt kein nützliches Kapazitätsergebnis. Lies die Leitfäden zu Teststrategie, Leistungs- und Sicherheitstests, bevor ein Agent diese Werkzeuge ausführt.

Agentenorchestrierung benötigt Berechtigungsgrenzen, evaluierte Übergaben und ein Gesamtkostenlimit. Cloud- und API-Nutzung können Kosten verursachen, unabhängig davon, ob eine Bibliothek Open Source ist. Das öffentliche Repository beobachtet Metadaten; KI-Generierung mit Quelleninhalten gehört in einen privaten Review-Arbeitsbereich. MCP-Hosting, Plugin-Installation und native WebMCP-Unterstützung benötigen echte Integrationsprüfungen. Bevorzuge keine experimentelle API und kein neueres Modell allein wegen seiner Aktualität. Prüfe Produktunterstützung und Abkündigungen, bevor du ein Beispiel übernimmst oder einen Dienst kaufst.

Eigenständig verfasste Texte in Leitfaden-JSON-Exporten stehen unter CC BY 4.0. Mit der Website ausgelieferte Drittanbietersoftware behält ihre eigenen Hinweise und Lizenzen. Die Lockdatei der Laufzeitabhängigkeiten und das Inventar der Asset-Hinweise müssen zusammen geändert werden, wenn ein neues Bundle die Pflichten bei der Weitergabe verändert.

## Verwandte Entscheidungen

[Skills, Plugins, MCP und WebMCP](../guides/integrations.md) · [Hosting und Ausstiegswege](../guides/hosting.md) · [Belege und automatische Pflege](../guides/maintenance.md) · [Tests auswählen und kombinieren](../guides/testing-strategy.md) · [Leistungstests](../guides/performance-testing.md)

## Primärbelege

[mkdocs-material](https://raw.githubusercontent.com/squidfunk/mkdocs-material/cbee8f352745a974e1bae7dc595793be9b6875d7/README.md) · [mcp-python](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/2af9e3089ac66b35c1550c500aae86a82efb1e17/README.md) · [plugins](https://raw.githubusercontent.com/openai/plugins/0722921d5542fc593105c27bd52630babd8b8c2a/README.md) · [playwright-testing](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/docs/src/best-practices-js.md) · [k6-test-types](https://raw.githubusercontent.com/grafana/k6-docs/151bf3efc34b5a23b5f338d6ea341af48f1f4d69/docs/sources/k6/v2.3.x/testing-guides/test-types/_index.md)
