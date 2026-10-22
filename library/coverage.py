"""Expose scoped guidance/reference coverage without inventing production maturity."""

import argparse
import ast
import json
import re
from pathlib import Path

from library.content import ROOT, catalog, read_json
from library.verification import SUITES, report_matches


def validate_coverage(root: Path = ROOT) -> list[str]:
    registry = read_json(root / "data/coverage.json")
    errors = []
    if registry.get("schema_version") != 1 or not registry.get("scope"):
        errors.append("Coverage schema/scope is missing")
    sources = {s["id"] for s in read_json(root / "data/sources.json")["sources"]}
    guides = {g["id"]: g for g in catalog(root)}
    seen = set()
    cases = set()
    for path in (root / "tests").glob("test_*.py"):
        for cls in ast.parse(path.read_text()).body:
            if isinstance(cls, ast.ClassDef):
                for node in cls.body:
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        cases.add(f"{path.stem}.{cls.name}.{node.name}")
    for item in registry.get("domains", []):
        did = item.get("id", "")
        if not re.fullmatch(r"[a-z0-9-]+", did) or did in seen:
            errors.append(f"Invalid/duplicate coverage domain: {did}")
        seen.add(did)
        if (not item.get("claim_scope") or not item.get("adopter_evidence_required")
                or item.get("human_adoption_required") is not True
                or item.get("support") != "local-synthesis"):
            errors.append(f"Unscoped coverage claim: {did}")
        if (not item.get("guides") or not set(item["guides"]) <= set(guides)
                or not item.get("sources") or not set(item["sources"]) <= sources):
            errors.append(f"Unknown coverage guidance/source: {did}")
        for gid in item.get("guides", []):
            if gid in guides and not (root / "docs/en" / guides[gid]["path"]).is_file():
                errors.append(f"Missing coverage guide body: {did}/{gid}")
        if not set(item.get("suite_ids", [])) <= set(SUITES):
            errors.append(f"Unknown coverage suite: {did}")
        for sid in item.get("suite_ids", []):
            if sid in SUITES:
                entry = root / SUITES[sid]["entry"]
                if (entry.is_symlink() or not entry.is_file()
                        or not entry.resolve().is_relative_to(root.resolve())):
                    errors.append(f"Missing/unsafe coverage suite entry: {did}/{sid}")
        if bool(item.get("suite_ids")) != bool(item.get("reference_paths")):
            errors.append(f"Incomplete coverage reference: {did}")
        if not set(item.get("test_ids", [])) <= cases:
            errors.append(f"Missing coverage test case: {did}")
        for relative in item.get("reference_paths", []):
            path = root / relative
            if (path.is_symlink() or not path.resolve().is_relative_to(root.resolve())
                    or not path.is_file()):
                errors.append(f"Missing/unsafe coverage reference: {did}")
    if not seen or not registry.get("extensions_requiring_separate_project_evidence"):
        errors.append("Coverage must declare domains and outstanding specialized evidence")
    return errors


def _passed(result: dict) -> bool:
    if not isinstance(result, dict):
        return False
    count = result.get("tests_observed")
    if (result.get("status") != "passed" or type(result.get("returncode")) is not int
            or result["returncode"] != 0
            or type(count) is not int or count <= 0):
        return False
    sid = result.get("suite_id")
    if not isinstance(sid, str) or sid not in SUITES:
        return False
    kind = SUITES[sid]["kind"]
    if kind == "python":
        receipt = result.get("test_observation", {})
        return (isinstance(receipt, dict) and isinstance(receipt.get("case_ids"), list)
                and all(isinstance(case, str) for case in receipt["case_ids"])
                and len(set(receipt["case_ids"])) == count
                and receipt.get("tests_run") == count and len(receipt["case_ids"]) == count
                and all(receipt.get(key) == 0 for key in ("skipped", "failures", "errors",
                                                         "expected_failures", "unexpected_successes")))
    if kind == "node":
        receipt = result.get("node_observation", {})
        return (isinstance(receipt, dict) and receipt.get("tests") == count
                and receipt.get("pass") == count and all(
                    receipt.get(key) == 0 for key in ("fail", "skipped", "todo", "cancelled")))
    receipt = result.get("browser_observation", {})
    return (isinstance(receipt, dict) and isinstance(receipt.get("checks"), list)
            and receipt.get("status") == "passed" and bool(receipt.get("browser_version"))
            and receipt.get("check_count") == count == len(receipt.get("checks", [])))


def coverage(domain_id: str = "", report: dict | None = None, root: Path = ROOT) -> dict:
    if not isinstance(domain_id, str) or len(domain_id) > 80:
        raise ValueError("Invalid coverage domain")
    errors = validate_coverage(root)
    if errors:
        raise ValueError("; ".join(errors[:10]))
    registry = read_json(root / "data/coverage.json")
    domains = registry["domains"]
    if domain_id:
        domains = [d for d in domains if d["id"] == domain_id]
        if not domains:
            raise ValueError("Unknown coverage domain")
    matches = report_matches(report, root) if report is not None else False
    results = {}
    if matches:
        if not isinstance(report.get("results"), list):
            raise ValueError("Invalid suite observations")
        for result in report["results"]:
            if not isinstance(result, dict) or not isinstance(result.get("suite_id"), str):
                raise ValueError("Invalid suite observation")
            sid = result.get("suite_id")
            if sid in results:
                raise ValueError("Duplicate suite observation")
            results[sid] = result
    output = []
    for domain in domains:
        item = dict(domain)
        item["status"] = "executable-reference" if item["suite_ids"] else "documented-guidance"
        item["source_support"] = "Context references for original synthesis; not external proof of implementation."
        if report is not None and item["suite_ids"]:
            item["status"] = "stale-or-missing-observation"
            selected = [results.get(sid, {}) for sid in item["suite_ids"]]
            if matches and all(_passed(r) for r in selected):
                cases = {case for r in selected
                         for case in r.get("test_observation", {}).get("case_ids", [])}
                if set(item["test_ids"]) <= cases:
                    item["status"] = "observed-local-reference"
            elif matches and any(r.get("status") in {"failed", "timeout"} for r in selected):
                item["status"] = "failed-local-reference"
        output.append(item)
    return {"schema_version": 1, "scope": registry["scope"], "domains": output,
            "report_matches_current_inputs": matches,
            "observation_authority": "Unauthenticated local record; no human approval or adopter production evidence.",
            "extensions_requiring_separate_project_evidence": registry[
                "extensions_requiring_separate_project_evidence"], "production_ready": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--domain", default="")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = None
    if args.report:
        if args.report.stat().st_size > 2_000_000:
            parser.error("Observation report exceeds size budget")
        report = read_json(args.report)
    print(json.dumps(coverage(args.domain, report), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
