"""Run from the repository root with python -m examples.durable_service."""

import argparse
import json
import threading
from pathlib import Path

from .experiments import benchmark, demo, drills
from .service import FixtureServer


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("demo", "drills", "benchmark"):
        child = commands.add_parser(command)
        child.add_argument("--output", type=Path, help="optional JSON file under reports/ or /tmp/")
        if command == "benchmark":
            child.add_argument("--operations", type=int, default=120)
            child.add_argument("--concurrency", type=int, default=8)
            child.add_argument("--capacity", type=int, default=2)
            child.add_argument("--delay-ms", type=int, default=10)
            child.add_argument("--seconds", type=float, default=5)
    child = commands.add_parser("_crash-server", help=argparse.SUPPRESS)
    child.add_argument("--db", type=Path, required=True)
    child.add_argument("--fault", choices=("before_commit", "after_commit", "after_consumer_commit"), required=True)
    args = parser.parse_args()
    if args.command == "_crash-server":
        with FixtureServer(args.db, fault=args.fault) as fixture:
            print(json.dumps({"url": fixture.url}), flush=True)
            threading.Event().wait()
        return
    try:
        if args.output:
            output = args.output.resolve()
            roots = ((Path.cwd() / "reports").resolve(), Path("/tmp").resolve())
            if not any(output.is_relative_to(root) for root in roots):
                raise ValueError("output must be beneath reports/ or /tmp/")
        if args.command == "benchmark":
            result = benchmark(args.operations, args.concurrency, args.capacity, args.delay_ms, args.seconds)
        else:
            result = demo() if args.command == "demo" else drills()
        rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
        if args.output:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(rendered)
        print(rendered, end="")
        if args.command == "benchmark" and not result["passed"]:
            parser.exit(1, "experiment failed; inspect the recorded checks and response samples\n")
    except (ValueError, RuntimeError) as error:
        parser.exit(1, f"experiment failed: {error}\n")


if __name__ == "__main__":
    main()
