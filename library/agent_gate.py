"""Export only modifications to known prose/catalog files from an agent checkout."""

import argparse
import re
import subprocess
from pathlib import Path


def allowed_path(name: str) -> bool:
    return name == "data/catalog.json" or bool(
        re.fullmatch(r"docs/(en|cs|de|es)/(?:guides/|reference/)?[a-z0-9-]+\.md", name)
    )


def export_patch(base: str, output: Path, root: Path):
    if not re.fullmatch(r"[0-9a-f]{40}", base):
        raise ValueError("Expected an immutable base commit")

    def git(*args):
        return subprocess.check_output(["git", "-C", str(root), *args])

    known = set(git("ls-tree", "-r", "--name-only", "-z", base).decode().split("\0"))
    changed = set(git("diff", "--name-only", "-z", base).decode().split("\0")) - {""}
    untracked = set(git("ls-files", "--others", "--exclude-standard", "-z")
                    .decode().split("\0")) - {""}
    for name in changed | untracked:
        path = root / name
        if (not allowed_path(name) or name not in known or not path.is_file()
                or path.is_symlink() or not path.resolve().is_relative_to(root.resolve())):
            raise ValueError(f"Agent changed a forbidden path: {name}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(git("diff", "--binary", base, "--", "docs", "data/catalog.json"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("base")
    parser.add_argument("--output", type=Path, default=Path("reports/agent.patch"))
    args = parser.parse_args()
    export_patch(args.base, args.output, Path.cwd())
