---
{
  "id": "scaling",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-21"
}
---
# Anhand von Messungen skalieren

## Vor der Verteilung messen

Registrierte Nutzer messen keine Kapazität. Parallelität, Spitzenrate, Nutzlastgröße, Lese-/Schreibanteil, Mandantenverteilung, Latenzperzentile und Hintergrundarbeit erfassen. Dienstziel und Kostenrahmen zuerst festlegen.

## Eskalationsfolge

1. Repräsentative Last profilieren; teure Abfragen, fehlende Indizes, unbegrenzte Listen und unnötige Aufrufe beheben.
2. Caches nur mit Frische-, Invalidierungs-, Mandanten- und Stampede-Regeln nutzen. Treffer und Ursprungslast messen.
3. Begrenzte Worker, Rückdruck, Quoten und Zulassungskontrolle ergänzen. Vor Überlast sicher ablehnen.
4. Zustandslose Prozesse replizieren; Sitzungen und Dateien passend auslagern. Verbindungspools über alle Replikate dimensionieren.
5. Lesereplikate benötigen einen Vertrag zu veralteten Daten. Erst nach gemessenen Schreib-/Speichergrenzen partitionieren; Routing, Umverteilung und übergreifende Vorgänge planen.

## Prüfen

Reale Verteilung, Lastspitze, langsame Abhängigkeit und Erholung testen. Durchsatz, p95/p99, Fehler, Warteschlangenalter, Sättigung und Kosten pro nützlicher Operation messen. Parallelität als Ankunftsrate × Bearbeitungszeit schätzen und unter Last prüfen.

Bei dauerhafter Zielverletzung oder belegtem Verlust der Reserve skalieren. Ausgangswert und Rollback dokumentieren. Autoscaling bleibt durch nachgelagerte Kapazität, Startzeit, Quoten und Budget begrenzt; ineffiziente Transaktionen repariert es nicht.

## Verwandte Entscheidungen

[Hosting und Ausstiegswege](hosting.md) · [Daten, Verträge und Migrationen](data.md) · [Zustand, Wiederherstellung und Kosten](operations.md) · [Architekturen auswählen und verbinden](architecture.md)

## Primärbelege

[observability](https://raw.githubusercontent.com/open-telemetry/opentelemetry.io/main/content/en/docs/concepts/observability-primer.md) · [kubernetes](https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/concepts/architecture/_index.md) · [postgres-isolation](https://raw.githubusercontent.com/postgres/postgres/master/doc/src/sgml/mvcc.sgml)
