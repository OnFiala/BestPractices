---
{
  "id": "first-project",
  "language": "es",
  "revision": 1,
  "translation_revision": 1,
  "reviewed_on": "2026-10-22"
}
---
# Completar el primer punto de control con evidencias

Crea un breve documento de intención del proyecto, pide a otra persona que
inspeccione su contenido real y registra esa observación. Si la revisión lo
acepta, el evaluador existente puede mostrar un punto de control como
`supported-by-recorded-evidence`. Todos los demás puntos de control y la
publicación siguen bloqueados. Este ejercicio produce un documento sobre una
propuesta de sitio web público; no construye ni prueba ese sitio.

Este es un tutorial local original, elaborado con ayuda de IA, que sintetiza el
contrato de entrega de esta biblioteca. Sus comandos y su ejemplo no constituyen
un estándar de las fuentes citadas ni una política de proyecto aprobada. Lee
[la descripción general de la entrega](project-delivery.md) para conocer el flujo
de trabajo más amplio y [la guía de adopción](adoption.md) al aplicarlo a
requisitos reales.

## 1. Crear un artefacto pequeño con control de versiones

Utiliza Python 3.12+, Git y un intérprete de comandos POSIX, comenzando en la raíz
del repositorio BestPractices. No se necesitan paquetes de Python, un modelo,
una cuenta de proveedor, un navegador ni un despliegue. Todos los comandos
siguientes se ejecutan desde esa misma raíz. Crean un nuevo directorio
`reports/first-project/`; si ya existe, utiliza otro directorio en todo el
ejercicio. Mantenlo privado si introduces nombres de personas.

Primero sustituye el valor siguiente por tu propio nombre o por la etiqueta real
de la sesión del agente. Declara la autoría del agente si es quien realiza el
trabajo. Esta etiqueta identifica al autor del ejercicio local; no acredita una
identidad autenticada ni autoridad sobre un sitio web real.

```sh
export FIRST_PROJECT_AUTHOR='REPLACE_WITH_YOUR_ACTUAL_NAME_OR_AGENT_SESSION'
```

El siguiente script escribe el documento y registra **únicamente ese documento**
en un commit de un nuevo repositorio Git local. El autor explícito del commit se
identifica como metadato de demostración; no suplanta a un revisor ni cambia tu
configuración de Git. El perfil toma su revisión de este commit real, nunca del
SHA fijo de ejemplo de la plantilla. No se crea ningún commit en la copia de
trabajo de la biblioteca.

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

El perfil describe este ejercicio local. Mantiene las obligaciones relativas al
navegador y a la publicación propias de un sitio web público; son trabajo futuro,
no permiso para publicar. `workload: unmeasured` conserva también el trabajo de
capacidad. Antes de comenzar un sitio web real, determina quién es su responsable
humano y modifica el perfil para reflejar su alojamiento, carga de trabajo y
restricciones reales. La plantilla más amplia `templates/project-profile.yaml`
es un lugar útil para recoger esas decisiones; la CLI utilizada aquí lee el
perfil de entrega JSON.

El inicializador crea `packet/project-plan.json`, evidencias de aceptación vacías
y artefactos provisionales para el trabajo pendiente. El artefacto real de este
ejercicio es `target/problem-brief.md`; su ID de artefacto es `problem-brief` y
su ID de punto de control es `intent-brief`. El archivo provisional copiado no es
el documento revisado.

## 2. Observar el estado inicial con honestidad

```sh
python -m library.delivery assess --profile reports/first-project/packet/project-profile.json --evidence reports/first-project/packet/project-evidence.json
```

Resultado esperado: código de salida **1**, `valid: true`, cero puntos de control
respaldados y todos los puntos de control en estado `blocked`. El código de
salida 1 significa que las evidencias obligatorias están incompletas; el código
2 significa que la entrada no es válida. `ready_for_human_review`,
`production_ready` y `human_authorization.verified` tienen el valor `false`.
Crear un archivo o copiar un paquete no completa su revisión.

Prepara un registro incompleto para el revisor. Calcula el hash de los bytes
reales mediante `read_bytes()`; no calcules el hash de un nombre de archivo ni
pegues un resumen criptográfico de otra ejecución.

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

Este borrador está incompleto deliberadamente y todavía no se presenta al
evaluador. Las evidencias iniciales siguen vacías. Un hash identifica bytes; no
es el resultado de una revisión.

## 3. Entregar el documento a un revisor independiente

Entrega a otra persona, o a una línea de trabajo de un agente autorizada por
separado, estos archivos reales: `target/problem-brief.md`,
`packet/project-plan.json` y `review.json`, dentro de `reports/first-project/`.
El revisor debe abrir el documento, inspeccionar las condiciones de bloqueo de
`intent-brief` en el plan y comparar el texto con el criterio. Una segunda cadena
de identidad o estar de acuerdo con el resumen del autor no constituye una
revisión independiente. Una revisión de un agente no es una aprobación humana.

El revisor puede mostrar de forma independiente los bytes del commit, los bytes
locales y el hash:

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

Solo después de leer el documento, el propio revisor edita `review.json`:

| Campo | Qué registra el revisor |
| --- | --- |
| `reviewer` | Su nombre real o la etiqueta de su sesión de agente, diferente de la del productor. |
| `observed_at` | El momento en que inspeccionó realmente el documento, como valor ISO 8601 con zona horaria. |
| `environment` | Dónde lo leyó, incluidos el archivo local y el visor o entorno de ejecución pertinente. Sin secretos. |
| `method` | Qué inspeccionó y cómo comprobó el criterio y los casos ausentes o contradictorios. |
| `expected` | El criterio que utilizó; cambia el borrador solo si lo exige el alcance acordado. |
| `actual` | Sus propios hallazgos concretos, incluidas las limitaciones; indicar únicamente «passed» no basta. |
| `outcome` | `passed` solo cuando el documento observado cumple el criterio; en caso contrario, `failed`. |
| `status`, `review_status` | `passed` y `accepted` solo si la revisión se acepta; en caso contrario, `failed` y `changes-requested`. |

Los campos de la observación están dentro de `observations[0]`. Mantén la revisión
y los hashes vinculados a los bytes que se leyeron realmente. No permitas que un
script, el autor o un modelo rellenen de antemano una revisión favorable. El
revisor debe explicar, por ejemplo, si la comprobación de éxito se puede evaluar
y si se indica explícitamente que sigue sin ejecutarse; no debe afirmar que ha
observado navegación con teclado en un sitio web que no existe.

**Si no hay un revisor independiente disponible, detente aquí.** Conserva
`review_status: unreviewed`, `status: unrun`, los campos vacíos de revisor y de
observación y las evidencias iniciales vacías. Repetir el paso 2 sigue dando cero
puntos de control respaldados y el código de salida 1. No inventes otra identidad
ni copies un hallazgo de ejemplo para terminar el ejercicio.

## 4. Presentar esa revisión e inspeccionar los bloqueos restantes

Una vez que el revisor haya devuelto su registro completado, el siguiente script
comprueba que el documento sigue coincidiendo tanto con su hash registrado como
con su revisión Git real. Copia la revisión en un nuevo archivo de evidencias,
sin cambiar sus hallazgos ni su decisión, y conserva el paquete inicial vacío.
No realiza la revisión.

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

Solo si ese script ha creado correctamente `evidence-reviewed.json`, ejecuta:

```sh
python -m library.delivery assess --profile reports/first-project/packet/project-profile.json --evidence reports/first-project/evidence-reviewed.json
```

Con una revisión válida, vigente y aceptada, el resultado esperado es exactamente
un punto de control `supported-by-recorded-evidence`: `intent-brief`. Todos los
demás puntos de control siguen en estado `blocked`; `release_blockers` no está
vacío. El comando **sigue terminando con el código 1**, y los tres valores
booleanos de preparación y autorización del paso 2 siguen siendo `false`. Un
registro fallido, incompleto, caducado o revisado por su propio autor debe seguir
bloqueado. Inspecciona los problemas indicados en lugar de cambiar marcas
temporales, etiquetas o resultados para obtener una evaluación favorable.

El evaluador comprueba la coherencia de las afirmaciones presentadas. No abre el
documento ni autentica al revisor ni reproduce la observación. Aquí, el hecho
observado es que un revisor inspeccionó unos bytes concretos del documento según
un criterio declarado. La evidencia de una aplicación funcional necesitará su
propia implementación, pruebas ejecutadas y revisión independiente; las pruebas
con componentes de referencia no las sustituyen.

Conserva cada documento, revisión e informe anteriores cuando hagas cambios. Un
documento modificado necesita un nuevo commit en el repositorio de destino y una
nueva revisión; un cambio en el perfil o en la política de la biblioteca necesita
un nuevo plan y evidencias correspondientes. No trasplantes hallazgos antiguos a
hashes nuevos. Para deshacer este ejercicio local, archiva o elimina únicamente
el directorio nuevo que creó; no se ha creado ningún repositorio remoto ni
despliegue público.

Continúa con [la guía de entrega de un sitio web público](playbook-public-website.md)
y el siguiente punto de control bloqueado del plan. El trabajo de un proyecto
real necesita sus propios resultados acordados, responsable, restricciones y
efectos permitidos antes de la implementación.

## Evidencia primaria

Las fuentes siguientes respaldan los principios de revisión, flujo de trabajo y
límites de los agentes que rodean este ejercicio. El documento, los comandos y
el ejercicio de un único punto de control anteriores son una síntesis local de
esta biblioteca, no una receta de las fuentes citadas.

[github-rulesets](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets.md) · [github-workflows](https://raw.githubusercontent.com/github/docs/5815d11586b0796688963a98c889680e60d72dc4/content/actions/reference/security/secure-use.md) · [owasp-ai-agent](https://raw.githubusercontent.com/OWASP/CheatSheetSeries/4a2852f456ccac403e140b6b48beb53ce505a550/cheatsheets/AI_Agent_Security_Cheat_Sheet.md) · [skills](https://raw.githubusercontent.com/openai/skills/49f948faa9258a0c61caceaf225e179651397431/README.md)
