"""Structured unittest observations for the fixed verification inventory."""

import argparse
import json
import re
import unittest


class RecordedResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.case_ids = []

    def startTest(self, test):
        self.case_ids.append(test.id())
        super().startTest(test)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pattern", required=True)
    args = parser.parse_args()
    if not re.fullmatch(r"test_[a-z_]+\.py", args.pattern):
        parser.error("Expected a concrete Python test filename")
    suite = unittest.defaultTestLoader.discover("tests", pattern=args.pattern)
    result = unittest.TextTestRunner(verbosity=2, resultclass=RecordedResult).run(suite)
    record = {"tests_run": result.testsRun, "skipped": len(result.skipped),
              "failures": len(result.failures), "errors": len(result.errors),
              "expected_failures": len(result.expectedFailures),
              "unexpected_successes": len(result.unexpectedSuccesses),
              "case_ids": result.case_ids}
    complete = result.testsRun > 0 and result.wasSuccessful() and not (
        result.skipped or result.expectedFailures or result.unexpectedSuccesses)
    print("BESTPRACTICES_RESULT=" + json.dumps(record, sort_keys=True))
    return 0 if complete else 1


if __name__ == "__main__":
    raise SystemExit(main())
