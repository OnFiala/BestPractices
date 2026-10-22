"""Validate untrusted proposals in a fresh checkout of a trusted base revision.

The scheduled workflow transfers JSON data, never an agent-produced executable
patch or files from the agent runner. This consumer is not a general-purpose sandbox.
"""

import argparse
import json
import os
import re
import stat
import subprocess
from pathlib import Path

MAX_PROPOSAL_BYTES = 100_000
MAX_FILE_BYTES = 60_000
MAX_FILES = 9


def allowed_path(name: str) -> bool:
    return name == "data/catalog.json" or bool(
        re.fullmatch(r"docs/(en|cs|de|es)/(?:guides/|reference/)?[a-z0-9-]+\.md", name)
    )


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON property")
        result[key] = value
    return result


def _json(text: str):
    return json.loads(text, object_pairs_hook=_unique_object)


def apply_proposal(payload: str, base: str, root: Path) -> list[str]:
    """Apply bounded plain-text changes; call only in a fresh trusted checkout.

    Path restrictions and schema checks constrain effects, not meaning or rights.
    Originality, applicability, and permission to publish still require a human.
    All proposed files are checked before any working-tree file is changed.
    """
    if not re.fullmatch(r"[0-9a-f]{40}", base):
        raise ValueError("Expected an immutable base commit")
    if not isinstance(payload, str) or len(payload.encode("utf-8")) > MAX_PROPOSAL_BYTES:
        raise ValueError("Proposal exceeds the transfer limit")
    proposal = _json(payload)
    required = {"schema_version", "base_commit", "human_review_required",
                "rights_status", "summary", "source_ids", "files"}
    if not isinstance(proposal, dict) or set(proposal) != required:
        raise ValueError("Unexpected proposal schema")
    if (type(proposal["schema_version"]) is not int or proposal["schema_version"] != 1
            or proposal["base_commit"] != base or proposal["human_review_required"] is not True
            or proposal["rights_status"] != "unreviewed"):
        raise ValueError("Proposal identity or review state is invalid")
    if not isinstance(proposal["summary"], str) or len(proposal["summary"]) > 1000:
        raise ValueError("Invalid proposal summary")
    files = proposal["files"]
    if not isinstance(files, list) or len(files) > MAX_FILES:
        raise ValueError("Invalid proposal file count")

    def git(*args):
        return subprocess.check_output(["git", "-C", str(root), *args])

    if git("rev-parse", "HEAD").decode().strip() != base:
        raise ValueError("Consumer checkout does not match the trusted base")
    if git("status", "--porcelain", "--untracked-files=all").strip():
        raise ValueError("Consumer checkout must be clean")
    known = set(git("ls-tree", "-r", "--name-only", "-z", base).decode().split("\0"))
    registry = _json((root / "data/sources.json").read_text(encoding="utf-8"))
    source_ids = proposal["source_ids"]
    if (not isinstance(source_ids, list) or len(source_ids) > 64
            or any(not isinstance(sid, str) for sid in source_ids)
            or len(set(source_ids)) != len(source_ids)
            or not set(source_ids) <= {s["id"] for s in registry["sources"]}
            or (files and not source_ids)):
        raise ValueError("Proposal must cite known source IDs")
    pending = []
    seen = set()
    root = root.resolve()
    for change in files:
        if not isinstance(change, dict) or set(change) != {"path", "content"}:
            raise ValueError("Invalid file proposal")
        name, content = change["path"], change["content"]
        if (not isinstance(name, str) or not allowed_path(name) or name not in known
                or name in seen):
            raise ValueError("Proposal names a forbidden or duplicate path")
        if (not isinstance(content, str) or not content or "\0" in content
                or len(content.encode("utf-8")) > MAX_FILE_BYTES):
            raise ValueError("Invalid or oversized proposed file")
        seen.add(name)
        path = root / name
        if (not path.resolve().is_relative_to(root)
                or any(p.is_symlink() for p in (path, *path.parents) if p != root)
                or not stat.S_ISREG(path.lstat().st_mode) or path.stat().st_nlink != 1):
            raise ValueError("Proposal destination must be a regular in-repository file")
        if name == "data/catalog.json":
            current, revised = _json(path.read_text(encoding="utf-8")), _json(content)
            if not isinstance(revised, dict):
                raise ValueError("Invalid proposed catalog")
            for key in ("schema_version", "canonical_language", "languages"):
                if revised.get(key) != current.get(key):
                    raise ValueError("An agent cannot change the catalog contract")
            before = {g["id"]: (g["path"], g["status"]) for g in current["guides"]}
            try:
                after = {g["id"]: (g["path"], g["status"]) for g in revised["guides"]}
            except (KeyError, TypeError) as exc:
                raise ValueError("Invalid proposed guide identities") from exc
            if before != after or len(after) != len(revised["guides"]):
                raise ValueError("Only a human may change guide identities or maturity")
        pending.append((path, content))
    for path, content in pending:
        path.write_text(content, encoding="utf-8")
    return [str(path.relative_to(root)) for path, _ in pending]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("base")
    proposal = parser.add_mutually_exclusive_group(required=True)
    proposal.add_argument("--proposal-env", help="Environment variable containing private JSON data")
    proposal.add_argument("--proposal-file", type=Path, help="Private JSON proposal")
    args = parser.parse_args()
    if args.proposal_env:
        payload = os.environ[args.proposal_env]
    else:
        with args.proposal_file.open("rb") as source:
            payload = source.read(MAX_PROPOSAL_BYTES + 1).decode("utf-8")
    changed = apply_proposal(payload, args.base, Path.cwd())
    print(f"Validated {len(changed)} proposed files; human rights/content review remains required.")
