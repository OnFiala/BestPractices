---
{
  "id": "first-project",
  "language": "en",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Complete your first evidence gate

Create a short project brief, have someone else inspect its actual contents, and
record that observation. If the review accepts it, the existing assessor can show
one gate as `supported-by-recorded-evidence`. Every other gate and release remain
blocked. This exercise produces a document about a proposed public website; it
does not build or test that website.

This is an original, AI-assisted local tutorial and synthesis of this library's
delivery contract. Its commands and example are not an upstream standard or an
approved project policy. Read [the delivery overview](project-delivery.md) for the
broader workflow and [adoption](adoption.md) when applying it to real requirements.

## 1. Create a small, versioned artifact

Use Python 3.12+, Git and a POSIX shell, starting in the BestPractices repository
root. No Python packages, model, provider account, browser or deployment are
needed. All commands below run from that same root. They create a new
`reports/first-project/` directory; use a different directory throughout if that
one already exists. Keep it private if you enter personal names.

First replace the value below with your own name or actual agent session label.
Disclose agent authorship if an agent is doing the work. This label identifies the
author of the local exercise; it does not establish authenticated identity or
authority over a real website.

```sh
export FIRST_PROJECT_AUTHOR='REPLACE_WITH_YOUR_ACTUAL_NAME_OR_AGENT_SESSION'
```

The following script writes the brief and commits **only that brief** in a new
local Git repository. The explicit Git author is labeled as demonstration
metadata; it does not impersonate a reviewer or change your Git configuration.
The profile takes its revision from this actual commit, never from the fixed
example SHA in the template. No commit is made in the library checkout.

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

The profile describes this local exercise. It retains the public-website browser
and publishing obligations; they are future work, not permission to publish.
`workload: unmeasured` retains capacity work too. Before starting an actual website,
resolve its human owner and revise the profile to match its real hosting, workload
and constraints. The broader `templates/project-profile.yaml` is a useful place
to capture those decisions; the CLI here reads the JSON delivery profile.

The initializer creates `packet/project-plan.json`, empty acceptance evidence,
and placeholder artifacts for the remaining work. The real artifact in this
exercise is `target/problem-brief.md`; its artifact ID is `problem-brief`, and its
gate ID is `intent-brief`. The copied placeholder is not the reviewed document.

## 2. Observe the honest starting state

```sh
python -m library.delivery assess --profile reports/first-project/packet/project-profile.json --evidence reports/first-project/packet/project-evidence.json
```

Expected: exit code **1**, `valid: true`, zero supported gates, and every gate
`blocked`. Exit 1 means required evidence is incomplete; exit 2 means invalid
input. `ready_for_human_review`, `production_ready` and
`human_authorization.verified` are all `false`. Creating a file or copying a
packet does not complete its review.

Prepare an incomplete record for the reviewer. Hash the actual bytes with
`read_bytes()`; do not hash a filename or paste a digest from another run.

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

This draft is deliberately incomplete and is not yet submitted to the assessor.
The initial evidence remains empty. A hash is a byte identity, not a review result.

## 3. Hand the document to an independent reviewer

Give another person, or a separately authorized agent workstream, these actual
files: `target/problem-brief.md`, `packet/project-plan.json` and `review.json`
under `reports/first-project/`. The reviewer must open the brief, inspect the
`intent-brief` blocking conditions in the plan, and compare the text against the
criterion. A second identity string or agreement with the author's summary is
not independent review. An agent review is not human approval.

The reviewer can independently print the committed bytes, local bytes and hash:

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

Only after reading, the reviewer edits `review.json` themselves:

| Field | What the reviewer records |
| --- | --- |
| `reviewer` | Their actual name or agent session label, distinct from the producer. |
| `observed_at` | When they actually inspected the document, as a timezone-aware ISO 8601 value. |
| `environment` | Where they read it, including the local file and relevant viewer/runtime. No secrets. |
| `method` | What they inspected and how they checked the criterion and missing/contradictory cases. |
| `expected` | The criterion they used; change the draft only if the agreed scope requires it. |
| `actual` | Their own concrete findings, including limitations; a bare “passed” is insufficient. |
| `outcome` | `passed` only when their observed document satisfies the criterion; otherwise `failed`. |
| `status`, `review_status` | `passed` and `accepted` only for an accepted review; otherwise `failed` and `changes-requested`. |

The observation fields are inside `observations[0]`. Keep the revision and hashes
bound to the bytes actually read. Do not have a script, the author or a model
pre-fill a successful review. The reviewer should explain, for example, whether
the success check is evaluable and explicitly still unrun; they must not claim to
have observed keyboard navigation in a website that does not exist.

**No independent reviewer available? Stop here.** Keep `review_status: unreviewed`,
`status: unrun`, the empty reviewer and observation fields, and the initial empty
evidence. Repeating step 2 still yields zero supported gates and exit 1. Do not
invent another identity or copy a sample finding to finish the exercise.

## 4. Submit that review and inspect the remaining blockers

After the reviewer has returned their completed record, the next script checks
that the brief still matches both its recorded hash and its real Git revision.
It copies the review without changing its findings or decision into a new
evidence file, preserving the initial empty packet. It does not perform review.

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

Only if that script successfully created `evidence-reviewed.json`, run:

```sh
python -m library.delivery assess --profile reports/first-project/packet/project-profile.json --evidence reports/first-project/evidence-reviewed.json
```

For a valid, fresh, accepted review, expect exactly one
`supported-by-recorded-evidence` result: `intent-brief`. All other gates remain
`blocked`; `release_blockers` is nonempty. The command **still exits 1**, and all
three readiness/authorization booleans from step 2 remain `false`. A failed,
incomplete, stale or self-reviewed record must remain blocked. Inspect the
reported issues instead of changing timestamps, labels or outcomes to get a pass.

The assessor checks the consistency of submitted assertions. It does not open the
brief, authenticate the reviewer or reproduce the observation. Here the observed
fact is that a reviewer inspected specified document bytes against a stated
criterion. Evidence of a working application will need its own implementation,
executed tests and independent review; fixture tests are not a substitute.

Keep each earlier brief, review and report when revising. A changed brief needs a
new target commit and review; a changed profile or library policy needs a new
plan and matching evidence. Do not transplant old findings onto new hashes. To
reverse this local exercise, archive or remove only its newly created directory;
it created no remote repository or public deployment.

Continue with [the public-website playbook](playbook-public-website.md) and the
next blocked gate in the plan. Real project work needs its own agreed outcomes,
owner, constraints and permitted effects before implementation.

## Primary evidence

The sources below support the surrounding review, workflow and agent-boundary
principles. The particular brief, commands and single-gate exercise above are
this library's local synthesis, not an upstream recipe.

[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [skills](https://raw.githubusercontent.com/openai/skills/49f948faa9258a0c61caceaf225e179651397431/README.md)
