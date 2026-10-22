"""Run fixed local scenarios; accepts no filesystem, network, or credential input."""

import argparse
import json

from .evaluate import demo, evaluate


def main():
    parser = argparse.ArgumentParser(description="Local agent workflow policy fixtures")
    parser.add_argument("command", choices=("demo", "evaluate"))
    args = parser.parse_args()
    report = demo() if args.command == "demo" else evaluate()
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if report["counts"]["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
