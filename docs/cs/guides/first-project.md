---
{
  "id": "first-project",
  "language": "cs",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Dokončete první kontrolní bránu s důkazy

Vytvořte stručný podklad projektu, nechte někoho jiného posoudit jeho skutečný obsah
a zaznamenejte toto pozorování. Pokud posouzení podklad přijme, stávající vyhodnocovač
může u jedné kontrolní brány zobrazit stav `supported-by-recorded-evidence`. Všechny
ostatní brány i vydání zůstávají zablokované. Toto cvičení vytváří dokument o navrhovaném
veřejném webu; tento web nevytváří ani netestuje.

Tento místní návod je původní text vytvořený s pomocí AI a shrnuje pravidla dodávání
této knihovny. Jeho příkazy a příklad nejsou standardem převzatým ze zdrojů ani
schválenými pravidly projektu. Širší postup popisuje [přehled dodávání](project-delivery.md);
při použití pro skutečné požadavky si přečtěte [použití knihovny v projektu](adoption.md).

## 1. Vytvořte malý artefakt pod správou verzí

Použijte Python 3.12+, Git a POSIX shell a začněte v kořeni repozitáře BestPractices.
Nejsou potřeba balíčky Pythonu, model, účet u poskytovatele, prohlížeč ani nasazení.
Všechny následující příkazy spouštějte z téhož kořene. Vytvoří nový adresář
`reports/first-project/`; pokud už existuje, používejte v celém postupu jiný adresář.
Pokud zadáte osobní jména, uchovávejte jej neveřejně.

Nejprve nahraďte níže uvedenou hodnotu svým jménem nebo skutečným označením relace
agenta. Pokud práci vykonává agent, uveďte jeho autorství. Toto označení identifikuje
autora místního cvičení; nedokládá ověřenou identitu ani oprávnění ke skutečnému webu.

```sh
export FIRST_PROJECT_AUTHOR='REPLACE_WITH_YOUR_ACTUAL_NAME_OR_AGENT_SESSION'
```

Následující skript zapíše podklad a v novém místním repozitáři Git vytvoří commit
obsahující **pouze tento podklad**. Výslovně uvedený autor Gitu je označen jako
ukázková metadata; nevydává se za posuzovatele ani nemění vaši konfiguraci Gitu.
Profil přebírá revizi z tohoto skutečného commitu, nikdy z pevně zadaného ukázkového
SHA v šabloně. V pracovní kopii knihovny nevznikne žádný commit.

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

Profil popisuje toto místní cvičení. Zachovává povinnosti veřejného webu týkající
se prohlížeče a zveřejnění; jde o budoucí práci, nikoli o povolení ke zveřejnění.
`workload: unmeasured` zachovává také práci na kapacitě. Před zahájením skutečného
webu určete odpovědného člověka a upravte profil podle jeho skutečného hostingu,
zátěže a omezení. Podrobnější `templates/project-profile.yaml` je vhodné místo
pro zachycení těchto rozhodnutí; zde používané CLI čte JSON profil dodávání.

Inicializátor vytvoří `packet/project-plan.json`, prázdné akceptační důkazy
a zástupné artefakty pro zbývající práci. Skutečným artefaktem tohoto cvičení
je `target/problem-brief.md`; jeho ID artefaktu je `problem-brief` a ID jeho
kontrolní brány je `intent-brief`. Zkopírovaný zástupný artefakt není posuzovaným dokumentem.

## 2. Pozorujte pravdivý výchozí stav

```sh
python -m library.delivery assess --profile reports/first-project/packet/project-profile.json --evidence reports/first-project/packet/project-evidence.json
```

Očekávaný výsledek: návratový kód **1**, `valid: true`, žádná brána podložená důkazy
a všechny brány ve stavu `blocked`. Kód 1 znamená, že požadované důkazy nejsou úplné;
kód 2 znamená neplatný vstup. `ready_for_human_review`, `production_ready`
a `human_authorization.verified` mají všechny hodnotu `false`. Vytvořením souboru
ani zkopírováním balíčku není jeho posouzení dokončeno.

Připravte neúplný záznam pro posuzovatele. Vypočítejte hash skutečných bajtů pomocí
`read_bytes()`; nepočítejte hash názvu souboru ani nevkládejte otisk z jiného běhu.

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

Tento návrh je záměrně neúplný a zatím se nepředává vyhodnocovači. Výchozí důkazy
zůstávají prázdné. Hash určuje identitu bajtů, není výsledkem posouzení.

## 3. Předejte dokument nezávislému posuzovateli

Předejte jiné osobě nebo samostatně oprávněné pracovní větvi agenta tyto skutečné
soubory z adresáře `reports/first-project/`: `target/problem-brief.md`,
`packet/project-plan.json` a `review.json`. Posuzovatel musí otevřít podklad,
prozkoumat blokující podmínky `intent-brief` v plánu a porovnat text s kritériem.
Druhý řetězec označující identitu ani souhlas s autorovým shrnutím nejsou nezávislým
posouzením. Posouzení agentem není schválením člověkem.

Posuzovatel může nezávisle vypsat bajty uložené v commitu, místní bajty a hash:

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

Teprve po přečtení posuzovatel sám upraví `review.json`:

| Pole | Co posuzovatel zaznamená |
| --- | --- |
| `reviewer` | Své skutečné jméno nebo označení relace agenta, odlišné od autora. |
| `observed_at` | Kdy dokument skutečně posoudil, jako hodnotu ISO 8601 s časovým pásmem. |
| `environment` | Kde jej četl, včetně místního souboru a příslušného prohlížeče či běhového prostředí. Bez tajných údajů. |
| `method` | Co posoudil a jak ověřil kritérium i případy chybějících či rozporných údajů. |
| `expected` | Použité kritérium; návrh změňte pouze tehdy, vyžaduje-li to dohodnutý rozsah. |
| `actual` | Své vlastní konkrétní závěry včetně omezení; samotné „prošlo“ nestačí. |
| `outcome` | `passed` pouze tehdy, když pozorovaný dokument splňuje kritérium; jinak `failed`. |
| `status`, `review_status` | `passed` a `accepted` pouze pro přijaté posouzení; jinak `failed` a `changes-requested`. |

Pole pozorování jsou uvnitř `observations[0]`. Revize a hashe musí zůstat svázané
s bajty, které byly skutečně přečteny. Nenechte skript, autora ani model předvyplnit
úspěšné posouzení. Posuzovatel by měl například vysvětlit, zda je kontrola úspěchu
vyhodnotitelná a stále výslovně označená jako neprovedená; nesmí tvrdit, že pozoroval
ovládání klávesnicí na webu, který neexistuje.

**Není k dispozici nezávislý posuzovatel? Zde skončete.** Zachovejte
`review_status: unreviewed`, `status: unrun`, prázdné pole posuzovatele i pozorování
a výchozí prázdné důkazy. Opakování kroku 2 stále vrátí žádné brány podložené důkazy
a kód 1. Nevymýšlejte další identitu ani nekopírujte ukázkový závěr, abyste cvičení dokončili.

## 4. Předložte posouzení a prozkoumejte zbývající překážky

Až posuzovatel vrátí dokončený záznam, následující skript ověří, že podklad stále
odpovídá svému zaznamenanému hashi i skutečné revizi Gitu. Zkopíruje posouzení do
nového souboru důkazů beze změny jeho závěrů nebo rozhodnutí a zachová výchozí
prázdný balíček. Samotné posouzení neprovádí.

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

Pouze pokud tento skript úspěšně vytvořil `evidence-reviewed.json`, spusťte:

```sh
python -m library.delivery assess --profile reports/first-project/packet/project-profile.json --evidence reports/first-project/evidence-reviewed.json
```

U platného, aktuálního a přijatého posouzení očekávejte právě jeden výsledek
`supported-by-recorded-evidence`: `intent-brief`. Všechny ostatní brány zůstávají
ve stavu `blocked`; `release_blockers` není prázdné. Příkaz **stále končí kódem 1**
a všechny tři logické hodnoty připravenosti a oprávnění z kroku 2 zůstávají `false`.
Neúspěšný, neúplný, zastaralý nebo vlastním autorem posouzený záznam musí zůstat
zablokovaný. Prozkoumejte hlášené problémy; neměňte časová razítka, označení ani
výsledky jen proto, aby kontrola prošla.

Vyhodnocovač kontroluje konzistenci předložených tvrzení. Neotevírá podklad, neověřuje
identitu posuzovatele ani neopakuje pozorování. Pozorovaným faktem je zde to, že
posuzovatel zkontroloval konkrétní bajty dokumentu podle uvedeného kritéria.
Důkazy o funkční aplikaci budou vyžadovat vlastní implementaci, provedené testy
a nezávislé posouzení; testy ukázkových komponent je nenahrazují.

Při úpravách uchovávejte všechny předchozí podklady, posouzení a zprávy. Změněný
podklad potřebuje nový commit v cílovém projektu a nové posouzení; změněný profil
nebo pravidla knihovny potřebují nový plán a odpovídající důkazy. Nepřenášejte staré
závěry na nové hashe. Pro odstranění výsledků tohoto místního cvičení archivujte
nebo odstraňte pouze jeho nově vytvořený adresář; nevytvořilo vzdálený repozitář
ani veřejné nasazení.

Pokračujte [postupem pro veřejný web](playbook-public-website.md) a další
zablokovanou branou v plánu. Skutečná projektová práce potřebuje před implementací
vlastní dohodnuté výsledky, vlastníka, omezení a povolené účinky.

## Primární zdroje

Následující zdroje podporují související principy posuzování, pracovních postupů
a hranic oprávnění agentů. Konkrétní podklad, příkazy a výše uvedené cvičení jedné
kontrolní brány jsou místní syntézou této knihovny, nikoli postupem převzatým ze zdrojů.

[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [skills](https://raw.githubusercontent.com/openai/skills/49f948faa9258a0c61caceaf225e179651397431/README.md)
