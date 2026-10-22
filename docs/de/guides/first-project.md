---
{
  "id": "first-project",
  "language": "de",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Den ersten Prüfpunkt mit Nachweisen abschließen

Erstellen Sie eine kurze Projektbeschreibung, lassen Sie deren tatsächlichen
Inhalt von jemand anderem prüfen und halten Sie diese Beobachtung fest. Wird die
Beschreibung bei der Prüfung akzeptiert, kann das vorhandene Bewertungsprogramm
einen Prüfpunkt als `supported-by-recorded-evidence` ausweisen. Alle anderen
Prüfpunkte und die Freigabe bleiben blockiert. Diese Übung erzeugt ein Dokument
über eine vorgeschlagene öffentliche Website; sie erstellt und testet diese
Website nicht.

Dies ist eine eigenständig verfasste, KI-unterstützte lokale Anleitung, die die
Auslieferungsregeln dieser Bibliothek zusammenführt. Ihre Befehle und ihr
Beispiel sind weder ein Standard der zitierten Quellen noch eine genehmigte
Projektrichtlinie. Lesen Sie [den Überblick zur Auslieferung](project-delivery.md)
für den umfassenderen Ablauf und [den Leitfaden zur Einführung](adoption.md),
wenn Sie ihn auf tatsächliche Anforderungen anwenden.

## 1. Ein kleines, versioniertes Artefakt erstellen

Verwenden Sie Python 3.12+, Git und eine POSIX-Shell und beginnen Sie im
Stammverzeichnis des BestPractices-Repositorys. Python-Pakete, ein Modell, ein
Anbieterkonto, ein Browser oder ein Deployment sind nicht erforderlich. Alle
folgenden Befehle werden aus demselben Stammverzeichnis ausgeführt. Sie erstellen
ein neues Verzeichnis `reports/first-project/`; verwenden Sie durchgängig ein
anderes Verzeichnis, falls dieses bereits existiert. Halten Sie es privat, wenn
Sie persönliche Namen eintragen.

Ersetzen Sie zunächst den folgenden Wert durch Ihren eigenen Namen oder die
tatsächliche Bezeichnung Ihrer Agentensitzung. Legen Sie die Urheberschaft des
Agenten offen, wenn ein Agent die Arbeit ausführt. Diese Bezeichnung benennt den
Urheber der lokalen Übung; sie belegt weder eine authentifizierte Identität noch
eine Entscheidungsbefugnis über eine echte Website.

```sh
export FIRST_PROJECT_AUTHOR='REPLACE_WITH_YOUR_ACTUAL_NAME_OR_AGENT_SESSION'
```

Das folgende Skript schreibt die Kurzbeschreibung und nimmt **nur diese
Kurzbeschreibung** in einen Commit in einem neuen lokalen Git-Repository auf.
Die expliziten Angaben zum Git-Autor sind als Metadaten einer Demonstration
gekennzeichnet. Damit wird weder die Identität einer prüfenden Person vorgetäuscht
noch Ihre Git-Konfiguration geändert. Das Profil übernimmt seine Revision aus diesem
tatsächlichen Commit, niemals aus dem fest vorgegebenen Beispiel-SHA der Vorlage.
Im Checkout der Bibliothek wird kein Commit erstellt.

```sh
python - <<'PY'
import json
import os
import subprocess
from pathlib import Path

author = os.environ.get("FIRST_PROJECT_AUTHOR", "").strip()
if not author or author.startswith("REPLACE_") or len(author) > 100:
    raise SystemExit("Set FIRST_PROJECT_AUTHOR to your actual author label first.")
work = Path("reports/first-project")
work.parent.mkdir(exist_ok=True)
work.mkdir()  # Refuse to overwrite an earlier exercise.
target = work / "target"
target.mkdir()
brief = f"""# A local community-events website: intent brief

Author and owner of this local document exercise: {author}
Human ownership and authorization for any real website remain unresolved.

Intended outcome: a visitor can find the next public community event, its date
and location without creating an account.

Proposed success check: given three fictional events with different dates, a
visitor can identify the next event and its location using keyboard navigation.
This check is a future acceptance case; no website exists and it has not run.

Scope now: write and independently review this brief in local files only.
Non-goals: accounts, payments, analytics, private event data and public hosting.
Use fictional public data only. No network calls, spending or publication are
authorized by this exercise.

Stop decision: the document owner stops work if private data, a paid service or
publication becomes necessary. A human must resolve ownership and authorize any
expanded scope before implementation. Unknown workload remains unmeasured.

Review criterion: the brief states an intended user outcome, a document owner,
non-goals, an observable future success check and a stop decision. Reject it if
any is absent or if it presents a planned website test as an observed result.

Limit: accepting this brief only supports the intent gate for this local
exercise. Requirements, design, implementation and all website tests are unrun.
"""
(target / "problem-brief.md").write_text(brief, encoding="utf-8")
subprocess.run(["git", "init", "--quiet", str(target)], check=True)
subprocess.run(["git", "-C", str(target), "add", "--", "problem-brief.md"], check=True)
subprocess.run([
    "git", "-C", str(target), "-c", "user.name=Local tutorial exercise",
    "-c", "user.email=local-tutorial@example.invalid", "-c", "commit.gpgsign=false",
    "commit", "--quiet", "-m", "Record the local intent brief",
], check=True)
revision = subprocess.check_output(
    ["git", "-C", str(target), "rev-parse", "HEAD"], text=True
).strip()
profile = json.loads(Path("templates/delivery-profile.json").read_text())
profile.update(
    project_id="first-project-local", revision=revision, hosting="local",
    workload="unmeasured",
    description="Local intent-document exercise for a proposed public website; no application exists.",
    objectives=["Independently inspect the brief's outcome, owner, non-goals, success check and stop decision."],
    constraints=[
        "Local document work only; fictional public data; no spending or publication.",
        "A document review is not evidence of a working website or human release approval.",
    ],
)
with (work / "profile.json").open("x", encoding="utf-8") as stream:
    json.dump(profile, stream, indent=2)
print("Created", target / "problem-brief.md", "at", revision)
PY
python -m library.project init --profile reports/first-project/profile.json --destination reports/first-project/packet
```

Das Profil beschreibt diese lokale Übung. Es behält die Pflichten zu
Browserprüfungen und Veröffentlichung für eine öffentliche Website bei; diese
sind künftige Aufgaben, keine Erlaubnis zur Veröffentlichung. Auch die
Kapazitätsaufgaben bleiben durch `workload: unmeasured` erforderlich. Klären Sie vor
dem Beginn einer tatsächlichen Website, welcher Mensch dafür verantwortlich ist,
und passen Sie das Profil an das tatsächliche Hosting, die Last und die
Rahmenbedingungen an. Die umfassendere Vorlage `templates/project-profile.yaml`
eignet sich, um diese Entscheidungen festzuhalten; die CLI hier liest das
JSON-Auslieferungsprofil.

Die Initialisierung erstellt `packet/project-plan.json`, leere Abnahmenachweise
und Platzhalterartefakte für die übrigen Arbeiten. Das tatsächliche Artefakt
dieser Übung ist `target/problem-brief.md`; seine Artefakt-ID lautet
`problem-brief`, und seine Prüfpunkt-ID lautet `intent-brief`. Der kopierte
Platzhalter ist nicht das geprüfte Dokument.

## 2. Den tatsächlichen Ausgangszustand feststellen

```sh
python -m library.delivery assess --profile reports/first-project/packet/project-profile.json --evidence reports/first-project/packet/project-evidence.json
```

Erwartet werden: Exit-Code **1**, `valid: true`, kein durch Nachweise gestützter
Prüfpunkt und der Status `blocked` für jeden Prüfpunkt. Exit-Code 1 bedeutet, dass
erforderliche Nachweise unvollständig sind; Exit-Code 2 bedeutet ungültige
Eingaben. `ready_for_human_review`, `production_ready` und
`human_authorization.verified` sind alle `false`. Das Erstellen einer Datei oder
das Kopieren eines Pakets schließt dessen Prüfung nicht ab.

Bereiten Sie für die prüfende Person einen unvollständigen Datensatz vor. Berechnen
Sie mit `read_bytes()` den Hash der tatsächlichen Bytes; berechnen Sie keinen Hash
eines Dateinamens und übernehmen Sie keinen Digest aus einem anderen Durchlauf.

```sh
python - <<'PY'
import hashlib
import json
import os
from pathlib import Path

work = Path("reports/first-project")
plan = json.loads((work / "packet/project-plan.json").read_text())
digest = hashlib.sha256((work / "target/problem-brief.md").read_bytes()).hexdigest()
record = {
    "gate_id": "intent-brief", "status": "unrun",
    "project_revision": plan["project_revision"],
    "producer": os.environ["FIRST_PROJECT_AUTHOR"],
    "reviewer": "", "review_status": "unreviewed",
    "artifacts": [{"id": "problem-brief", "sha256": digest,
                   "revision": plan["project_revision"]}],
    "observations": [{
        "id": "brief-reading-1", "artifact_id": "problem-brief",
        "artifact_sha256": digest, "observed_at": "", "environment": "",
        "method": "",
        "expected": "The brief states the user outcome, document owner, non-goals, observable future success check and stop decision, without claiming a website test ran.",
        "actual": "", "outcome": "unrun",
    }],
}
with (work / "review.json").open("x", encoding="utf-8") as stream:
    json.dump(record, stream, indent=2)
print("Artifact SHA-256:", digest)
print("Review is unreviewed; no observation or reviewer identity has been supplied.")
PY
```

Dieser Entwurf ist absichtlich unvollständig und wird dem Bewertungsprogramm noch
nicht vorgelegt. Die anfänglichen Nachweise bleiben leer. Ein Hash kennzeichnet
Bytes, kein Prüfergebnis.

## 3. Das Dokument zur unabhängigen Prüfung übergeben

Geben Sie einer anderen Person oder einem gesondert autorisierten
Agenten-Arbeitsstrang diese tatsächlichen Dateien unter `reports/first-project/`:
`target/problem-brief.md`, `packet/project-plan.json` und `review.json`. Die
prüfende Person beziehungsweise der prüfende Agent muss die Kurzbeschreibung
öffnen, die blockierenden Bedingungen für `intent-brief` im Plan untersuchen und
den Text am Kriterium messen. Eine zweite Identitätszeichenfolge oder die
Zustimmung zur Zusammenfassung des Autors ist keine unabhängige Prüfung. Eine
Prüfung durch einen Agenten ist keine menschliche Freigabe.

Die prüfende Person beziehungsweise der prüfende Agent kann die committeten Bytes,
die lokalen Bytes und den Hash unabhängig ausgeben:

```sh
python - <<'PY'
import hashlib
import subprocess
from pathlib import Path

target = Path("reports/first-project/target")
current = (target / "problem-brief.md").read_bytes()
committed = subprocess.check_output(
    ["git", "-C", str(target), "show", "HEAD:problem-brief.md"]
)
if current != committed:
    raise SystemExit("Brief differs from its commit. Stop and review a new revision.")
print(current.decode("utf-8"))
print("SHA-256:", hashlib.sha256(current).hexdigest())
PY
```

Erst nach dem Lesen bearbeitet die prüfende Person beziehungsweise der prüfende
Agent selbst die Datei `review.json`:

| Feld | Was bei der Prüfung festgehalten wird |
| --- | --- |
| `reviewer` | Der tatsächliche Name oder die Bezeichnung der Agentensitzung, abweichend von der erstellenden Rolle. |
| `observed_at` | Der tatsächliche Zeitpunkt der Dokumentprüfung als ISO-8601-Wert mit Zeitzonenangabe. |
| `environment` | Wo das Dokument gelesen wurde, einschließlich der lokalen Datei und des verwendeten Anzeigeprogramms beziehungsweise der relevanten Laufzeitumgebung. Keine Geheimnisse. |
| `method` | Was untersucht wurde und wie das Kriterium sowie fehlende oder widersprüchliche Angaben geprüft wurden. |
| `expected` | Das verwendete Kriterium; den Entwurf nur ändern, wenn es der vereinbarte Umfang erfordert. |
| `actual` | Eigene konkrete Befunde einschließlich ihrer Grenzen; ein bloßes „bestanden“ reicht nicht aus. |
| `outcome` | `passed` nur dann, wenn das tatsächlich geprüfte Dokument das Kriterium erfüllt; andernfalls `failed`. |
| `status`, `review_status` | `passed` und `accepted` nur bei einer akzeptierten Prüfung; andernfalls `failed` und `changes-requested`. |

Die Beobachtungsfelder befinden sich in `observations[0]`. Revision und Hashes
müssen an die tatsächlich gelesenen Bytes gebunden bleiben. Lassen Sie weder ein
Skript noch den Autor oder ein Modell eine erfolgreiche Prüfung vorab eintragen.
Die prüfende Person beziehungsweise der prüfende Agent sollte beispielsweise
erläutern, ob die vorgesehene Erfolgsprüfung auswertbar und ausdrücklich noch
nicht ausgeführt ist. Dabei darf nicht behauptet werden, die Tastaturnavigation
in einer Website beobachtet zu haben, die nicht existiert.

**Steht keine unabhängige Prüfung zur Verfügung? Halten Sie hier an.** Behalten
Sie `review_status: unreviewed`, `status: unrun`, das leere Feld für die prüfende
Rolle, die leeren Beobachtungsfelder und die anfänglich leeren Nachweise bei.
Eine Wiederholung von Schritt 2 ergibt weiterhin null durch Nachweise gestützte
Prüfpunkte und Exit-Code 1. Erfinden Sie keine weitere Identität und kopieren Sie
keinen Beispielbefund, um die Übung abzuschließen.

## 4. Die Prüfung einreichen und verbleibende Hindernisse untersuchen

Nachdem die prüfende Person beziehungsweise der prüfende Agent den ausgefüllten
Datensatz zurückgegeben hat, prüft das nächste Skript, ob die Kurzbeschreibung
weiterhin sowohl mit ihrem erfassten Hash als auch mit ihrer tatsächlichen
Git-Revision übereinstimmt. Es kopiert die Prüfung ohne Änderung ihrer Befunde
oder Entscheidung in eine neue Nachweisdatei und bewahrt dabei das anfänglich
leere Paket. Es führt selbst keine Prüfung des Inhalts durch.

```sh
python - <<'PY'
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

work = Path("reports/first-project")
target = work / "target"
record = json.loads((work / "review.json").read_text())
if record["review_status"] == "unreviewed" or not record["reviewer"].strip():
    raise SystemExit("No completed independent review. Keep the initial blocked evidence.")
evidence = json.loads((work / "packet/project-evidence.json").read_text())
revision = subprocess.check_output(
    ["git", "-C", str(target), "rev-parse", "HEAD"], text=True
).strip()
content = (target / "problem-brief.md").read_bytes()
committed = subprocess.check_output(
    ["git", "-C", str(target), "show", "HEAD:problem-brief.md"]
)
digest = hashlib.sha256(content).hexdigest()
if not (revision == evidence["project_revision"] == record["project_revision"]
        == record["artifacts"][0]["revision"]
        and content == committed
        and digest == record["artifacts"][0]["sha256"]
        == record["observations"][0]["artifact_sha256"]):
    raise SystemExit("Artifact or revision changed. Preserve this review and obtain a new one.")
evidence["as_of"] = datetime.now(timezone.utc).isoformat()
evidence["records"] = [record]
evidence["notes"] = "One actual document review only; website implementation and tests remain unrun."
with (work / "evidence-reviewed.json").open("x", encoding="utf-8") as stream:
    json.dump(evidence, stream, indent=2)
PY
```

Führen Sie den folgenden Befehl nur aus, wenn dieses Skript
`evidence-reviewed.json` erfolgreich erstellt hat:

```sh
python -m library.delivery assess --profile reports/first-project/packet/project-profile.json --evidence reports/first-project/evidence-reviewed.json
```

Bei einer gültigen, aktuellen und akzeptierten Prüfung ist genau ein Ergebnis
`supported-by-recorded-evidence` zu erwarten: `intent-brief`. Alle anderen
Prüfpunkte bleiben `blocked`; `release_blockers` ist nicht leer. Der Befehl
**endet weiterhin mit Exit-Code 1**, und alle drei booleschen Werte für Bereitschaft
und Autorisierung aus Schritt 2 bleiben `false`. Ein fehlgeschlagener,
unvollständiger, veralteter oder vom Autor selbst geprüfter Datensatz muss
blockiert bleiben. Untersuchen Sie die gemeldeten Probleme, statt Zeitstempel,
Bezeichnungen oder Ergebnisse zu ändern, um eine bestandene Prüfung zu erzielen.

Das Bewertungsprogramm prüft die Konsistenz der eingereichten Angaben. Es öffnet
weder die Kurzbeschreibung noch authentifiziert es die prüfende Person oder den
prüfenden Agenten oder reproduziert die Beobachtung. Die hier beobachtete Tatsache
ist, dass bestimmte Dokumentbytes anhand eines angegebenen Kriteriums geprüft
wurden. Der Nachweis einer funktionierenden Anwendung erfordert eine eigene
Implementierung, ausgeführte Tests und eine unabhängige Prüfung; Tests von
Testvorrichtungen sind kein Ersatz dafür.

Bewahren Sie bei Überarbeitungen jede frühere Kurzbeschreibung, jede Prüfung und
jeden Bericht auf. Eine geänderte Kurzbeschreibung erfordert einen neuen Commit
im Ziel-Repository und eine neue Prüfung; ein geändertes Profil oder geänderte
Bibliotheksrichtlinien erfordern einen neuen Plan und passende Nachweise.
Übertragen Sie alte Befunde nicht auf neue Hashes. Um diese lokale Übung
rückgängig zu machen, archivieren oder entfernen Sie ausschließlich ihr neu
angelegtes Verzeichnis; die Übung hat weder ein entferntes Repository noch ein
öffentliches Deployment erstellt.

Setzen Sie die Arbeit mit [dem Playbook für öffentliche Websites](playbook-public-website.md)
und dem nächsten blockierten Prüfpunkt im Plan fort. Echte Projektarbeit
benötigt vor der Implementierung eigene vereinbarte Ziele, eine verantwortliche
Person, Rahmenbedingungen und erlaubte Auswirkungen.

## Primärquellen

Die folgenden Quellen stützen die zugrunde liegenden Grundsätze zu Prüfung,
Arbeitsabläufen und Agentengrenzen. Die konkrete Kurzbeschreibung, die Befehle und
die Übung zu einem einzelnen Prüfpunkt oben sind eine eigenständige Ausarbeitung
dieser Bibliothek, keine aus den Quellen übernommene Anleitung.

[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [skills](https://raw.githubusercontent.com/openai/skills/49f948faa9258a0c61caceaf225e179651397431/README.md)
