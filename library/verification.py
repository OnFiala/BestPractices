"""Run a fixed local reference-check inventory and record the exact input image.

Reports are reproducible observations, not signed attestations or human approval.
No profile text or caller-provided command is executed.
"""

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import signal
import stat
import subprocess
import sys
import time
from pathlib import Path

from library.content import ROOT

SUITES = {
    "delivery": {"entry": "tests/test_delivery.py", "kind": "python",
                 "scope": "Local planning and recorded-evidence policy; no authenticated approval."},
    "durable-service": {"entry": "tests/test_durable_service.py", "kind": "python",
                        "scope": "Synthetic loopback HTTP and local SQLite invariants."},
    "agent-workflow": {"entry": "tests/test_agent_workflow.py", "kind": "python",
                       "scope": "Deterministic local policy, retrieval and side-effect fixtures; no model-quality claim."},
    "frontend-unit": {"entry": "tests/frontend.test.cjs", "kind": "node",
                      "scope": "Frontend state and local fixture contracts."},
    "frontend-browser": {"entry": "examples/frontend/browser-smoke.mjs", "kind": "browser",
                         "scope": "Selected real-browser journeys, not full accessibility certification."},
}
INPUT_DIRS = ("library", "examples", "tests", "data", "templates", "plugins", "docs", "delivery",
              "web", ".github/workflows")
INPUT_FILES = ("pyproject.toml", "uv.lock", "AGENTS.md", "PROVENANCE.md", "SECURITY.md",
               "LICENSE-CODE", "LICENSE-CONTENT", "README.md", "AGENT_SYSTEM.md",
               "project-profile.json", "project-plan.json", "reference-manifest.json")
MAX_FILES = 3000
MAX_INPUT_BYTES = 32 * 1024 * 1024
TIMEOUT_SECONDS = 120


def _json_digest(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     separators=(",", ":")).encode()).hexdigest()


def input_image(root: Path = ROOT) -> dict:
    """Hash code, configuration and guidance, excluding caches and generated reports."""
    root = root.resolve(strict=True)
    candidates = []
    for name in INPUT_DIRS:
        start = root / name
        if start.is_symlink():
            raise ValueError(f"Input directory is a symlink: {name}")
        if not start.exists():
            continue
        for directory, dirs, files in os.walk(start, followlinks=False):
            base = Path(directory)
            dirs[:] = sorted(d for d in dirs if d not in {"__pycache__", ".pytest_cache"})
            for child in dirs:
                if (base / child).is_symlink():
                    raise ValueError("Input image cannot traverse symlink directories")
            candidates.extend(base / filename for filename in sorted(files)
                              if not filename.endswith((".pyc", ".pyo")))
    candidates.extend(root / name for name in INPUT_FILES if os.path.lexists(root / name))
    if len(candidates) > MAX_FILES:
        raise ValueError("Input image exceeds file budget")
    records, total = [], 0
    for path in sorted(set(candidates)):
        if path.is_symlink() or not stat.S_ISREG(path.lstat().st_mode):
            raise ValueError("Input image must contain regular files")
        if not path.resolve().is_relative_to(root):
            raise ValueError("Input image escaped the project")
        total += path.stat().st_size
        if total > MAX_INPUT_BYTES:
            raise ValueError("Input image exceeds byte budget")
        records.append({"path": str(path.relative_to(root)),
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    revision, dirty = None, None
    if os.path.lexists(root / ".git"):
        try:
            revision = subprocess.check_output(
                ["git", "-C", str(root), "rev-parse", "--verify", "HEAD^{commit}"],
                text=True, stderr=subprocess.DEVNULL, timeout=10).strip()
            dirty = bool(subprocess.check_output(
                ["git", "-C", str(root), "status", "--porcelain", "--untracked-files=all"],
                stderr=subprocess.DEVNULL, timeout=10).strip())
        except (subprocess.SubprocessError, OSError) as exc:
            raise ValueError("Existing Git metadata could not be inspected") from exc
    return {"digest": _json_digest(records), "files": records,
            "revision": revision, "dirty": dirty,
            "scope": "Listed code/configuration/guidance inputs; excludes reports, reviews, caches and runtime state."}


def report_matches(report: dict, root: Path = ROOT) -> bool:
    """Check content binding only; a matching report is still an unauthenticated record."""
    if (not isinstance(report, dict) or not isinstance(report.get("input_image"), dict)
            or not isinstance(report["input_image"].get("files"), list)):
        return False
    return (isinstance(report, dict) and report.get("schema_version") == 1
            and report.get("kind") == "local-reference-verification"
            and report.get("input_changed") is False
            and _json_digest(report.get("input_image", {}).get("files", []))
            == report.get("input_image", {}).get("digest")
            == input_image(root)["digest"])


def run_suites(suite_ids: list[str], root: Path = ROOT) -> dict:
    if (not isinstance(suite_ids, list) or not suite_ids or len(suite_ids) > len(SUITES)
            or any(not isinstance(sid, str) or sid not in SUITES for sid in suite_ids)
            or len(set(suite_ids)) != len(suite_ids)):
        raise ValueError("Choose distinct known local suite IDs")
    root = root.resolve(strict=True)
    before = input_image(root)
    results = []
    for sid in suite_ids:
        spec = SUITES[sid]
        entry = root / spec["entry"]
        command = ([sys.executable, "-m", "library.check_runner", "--pattern", entry.name]
                   if spec["kind"] == "python" else
                   ["node", *(["--test", "--test-reporter=tap"]
                              if spec["kind"] == "node" else []), spec["entry"]])
        result = {"suite_id": sid, "scope": spec["scope"], "command": command,
                  "status": "not-run", "returncode": None, "duration_seconds": 0.0}
        if not entry.is_file():
            result["reason"] = "Required reference entry point is absent"
            results.append(result)
            continue
        if spec["kind"] != "python" and shutil.which("node") is None:
            result["reason"] = "Node is unavailable"
            results.append(result)
            continue
        start = time.monotonic()
        try:
            environment = dict(os.environ, BP_PYTHON=sys.executable)
            process = subprocess.Popen(command, cwd=root, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, env=environment, start_new_session=True)
            try:
                stdout, stderr = process.communicate(timeout=TIMEOUT_SECONDS)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.communicate()
                raise
            count = None
            if spec["kind"] == "python":
                lines = [line for line in stdout.splitlines()
                         if line.startswith(b"BESTPRACTICES_RESULT=")]
                observation = json.loads(lines[-1].split(b"=", 1)[1]) if lines else {}
                count = observation.get("tests_run", 0)
                result["test_observation"] = observation
            elif spec["kind"] == "node":
                counters = {name: re.findall(fr"^# {name} (\d+)\r?$".encode(), stdout,
                                            flags=re.MULTILINE)
                            for name in ("tests", "pass", "fail", "skipped", "todo", "cancelled")}
                observed = {name: int(values[0]) if len(values) == 1 else None
                            for name, values in counters.items()}
                count = observed["tests"] or 0
                result["node_observation"] = observed
                if (observed["pass"] != count or any(observed[name] != 0
                        for name in ("fail", "skipped", "todo", "cancelled"))):
                    count = 0
            else:
                try:
                    observation = json.loads(stdout.splitlines()[-1])
                except (ValueError, IndexError):
                    observation = {}
                count = observation.get("check_count", 0)
                result["browser_observation"] = observation
                if (observation.get("status") != "passed" or not observation.get("browser_version")
                        or not isinstance(count, int) or count != len(observation.get("checks", []))):
                    count = 0
            result.update(status="passed" if process.returncode == 0 and count != 0 else "failed",
                          returncode=process.returncode, tests_observed=count,
                          stdout_sha256=hashlib.sha256(stdout).hexdigest(),
                          stderr_sha256=hashlib.sha256(stderr).hexdigest())
            if count == 0:
                result["reason"] = "No executed tests were observed"
            # Keep diagnostics local: the reusable report contains hashes, not fixture data.
            if process.returncode:
                print(f"{sid} failed:\n" + stderr[-4000:].decode(errors="replace"),
                      file=sys.stderr)
        except subprocess.TimeoutExpired:
            result.update(status="timeout", reason=f"Local suite exceeded {TIMEOUT_SECONDS}s")
        except OSError as exc:
            result.update(status="not-run", reason=type(exc).__name__)
        result["duration_seconds"] = round(time.monotonic() - start, 6)
        results.append(result)
    after = input_image(root)
    changed = before["digest"] != after["digest"]
    return {"schema_version": 1, "kind": "local-reference-verification",
            "observed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "runtime": {"python": sys.version, "platform": sys.platform,
                        "node": subprocess.check_output(["node", "--version"], text=True,
                                                        timeout=10).strip()
                        if shutil.which("node") else None},
            "input_image": before, "input_changed": changed, "results": results,
            "all_selected_passed": not changed and all(r["status"] == "passed" for r in results),
            "human_approval": False, "authenticated_execution": False,
            "limits": "Local recorded observations, not signed attestations, production readiness, model quality or human approval."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("suite", nargs="+", choices=sorted(SUITES))
    parser.add_argument("--output", type=Path, help="New local JSON report; refuses overwrite")
    args = parser.parse_args()
    try:
        report = run_suites(args.suite)
        text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with args.output.open("x", encoding="utf-8") as stream:
                stream.write(text)
        else:
            print(text, end="")
    except (ValueError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 0 if report["all_selected_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
