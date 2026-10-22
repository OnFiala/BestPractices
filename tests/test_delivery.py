"""Fail-closed delivery evidence and planner invariants, using synthetic fixtures."""

import copy
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from library.content import ROOT
from library.delivery import PROJECT_TYPES, STAGES, assess_project, plan_project, validate_profile


def profile():
    return json.loads((ROOT / "templates/delivery-profile.json").read_text())


def evidence_for(plan):
    """Assert synthetic complete evidence; this does not execute project tests."""
    records = []
    for gate in plan["gates"]:
        artifacts = [{"id": item, "sha256": hashlib.sha256(item.encode()).hexdigest(),
                      "revision": plan["project_revision"]} for item in gate["artifacts"]]
        records.append({
            "gate_id": gate["id"], "status": "passed", "project_revision": plan["project_revision"],
            "producer": "synthetic-producer", "reviewer": "synthetic-reviewer",
            "review_status": "accepted", "artifacts": artifacts,
            "observations": [{
                "id": f"observation-{item['id']}", "artifact_id": item["id"],
                "artifact_sha256": item["sha256"], "observed_at": "2026-10-22T10:00:00Z",
                "environment": "Synthetic unit-test fixture; no external system tested.",
                "method": "A fabricated assertion used to test evaluator branches.",
                "expected": "Expected assertion for the unit-test branch.",
                "actual": "Matching assertion; this is not empirical project evidence.",
                "outcome": "passed",
            } for item in artifacts],
        })
    return {"schema_version": 1, "project_id": plan["project_id"],
            "project_revision": plan["project_revision"], "profile_digest": plan["profile_digest"],
            "plan_digest": plan["plan_digest"], "as_of": "2026-10-22T12:00:00Z", "records": records}


class DeliveryTests(unittest.TestCase):
    def setUp(self):
        self.profile = profile()
        self.plan = plan_project(self.profile)
        self.assertTrue(self.plan["valid"], self.plan.get("errors"))
        self.evidence = evidence_for(self.plan)

    def result(self, gate_id, assessment=None):
        assessment = assessment or assess_project(self.profile, self.evidence)
        return next(result for result in assessment["gate_results"] if result["gate_id"] == gate_id)

    def record(self, gate_id):
        return next(record for record in self.evidence["records"] if record["gate_id"] == gate_id)

    def temporary_config(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "data").mkdir()
        for filename in ("delivery.json", "catalog.json", "blueprints.json"):
            shutil.copyfile(ROOT / "data" / filename, root / "data" / filename)
        return root

    def test_six_project_types_have_full_deterministic_lifecycle(self):
        for project_type in PROJECT_TYPES:
            with self.subTest(project_type=project_type):
                current = {**self.profile, "project_type": project_type}
                plan = plan_project(current)
                self.assertTrue(plan["valid"], plan.get("errors"))
                self.assertEqual(plan, plan_project(current))
                self.assertEqual(set(STAGES), {g["stage"] for g in plan["gates"]})
                seen = set()
                for gate in plan["gates"]:
                    self.assertLessEqual(set(gate["prerequisites"]), seen)
                    self.assertNotEqual(gate["producer_role"], gate["reviewer_role"])
                    self.assertTrue(gate["artifacts"])
                    self.assertTrue(gate["blocking_conditions"])
                    self.assertTrue(gate["guide_revisions"])
                    seen.add(gate["id"])

    def test_invalid_profiles_are_bounded_json_failures(self):
        invalid = [None, [], {**self.profile, "project_type": "unknown"},
                   {**self.profile, "surfaces": ["spacecraft"]},
                   {**self.profile, "approved": True},
                   {**self.profile, "revision": "main"},
                   {**self.profile, "schema_version": True},
                   {**self.profile, "workload": float("nan")},
                   {**self.profile, "description": "x" * 5000},
                   {**self.profile, "surfaces": ["browser", "browser"]},
                   {**self.profile, "hosting": {"unexpected": True}}]
        circular = {}
        circular["loop"] = circular
        invalid.append(circular)
        for item in invalid:
            with self.subTest(item_type=type(item).__name__):
                self.assertFalse(validate_profile(item)["valid"])
                result = plan_project(item)
                self.assertFalse(result["valid"])
                self.assertFalse(result["production_ready"])
                self.assertLess(len(json.dumps(result)), 10000)

    def test_profile_variants_add_gates_and_inherit_blueprint_boundaries(self):
        current = {**self.profile, "project_type": "saas", "risk": "high",
                   "data_sensitivity": "restricted", "hosting": "hybrid", "workload": "high",
                   "surfaces": ["cli"], "external_side_effects": []}
        plan = plan_project(current)
        ids = {g["id"] for g in plan["gates"]}
        self.assertLessEqual({"privacy-lifecycle", "high-consequence-review", "host-operations",
                              "provider-exit", "capacity-envelope", "external-effects",
                              "tenant-isolation"}, ids)
        self.assertIn("payments", plan["effective_profile"]["external_side_effects"])
        self.assertEqual({7}, {g["max_evidence_age_days"] for g in plan["gates"]})
        implementation = next(g for g in plan["gates"] if g["id"] == "implementation-packet")
        self.assertIn("privacy-lifecycle", implementation["prerequisites"])
        release = next(g for g in plan["gates"] if g["id"] == "release-candidate")
        self.assertIn("tenant-isolation", release["prerequisites"])
        mobile = plan_project({**self.profile, "project_type": "mobile-backend", "surfaces": ["api"]})
        self.assertIn("mobile-compatibility", {g["id"] for g in mobile["gates"]})

    def test_complete_assertions_only_enable_human_review_never_production(self):
        self.evidence["human_approval"] = {"approved": True, "actor": "agent", "signed": True}
        result = assess_project(self.profile, self.evidence)
        self.assertTrue(result["valid"])
        self.assertTrue(result["ready_for_human_review"])
        self.assertFalse(result["production_ready"])
        self.assertFalse(result["human_authorization"]["verified"])
        self.assertTrue(result["human_authorization"]["required"])
        self.assertTrue(result["human_approval_claim_present"])
        self.assertTrue(all(r["status"] == "supported-by-recorded-evidence"
                            for r in result["gate_results"]))

    def test_illustrative_template_and_assertions_never_support_readiness(self):
        template = json.loads((ROOT / "templates/delivery-evidence.json").read_text())
        result = assess_project(self.profile, template)
        self.assertTrue(result["valid"], result.get("errors"))
        self.assertFalse(result["ready_for_human_review"])
        self.assertFalse(result["production_ready"])
        self.evidence["example"] = True
        self.assertFalse(assess_project(self.profile, self.evidence)["ready_for_human_review"])

    def test_post_release_work_does_not_require_prior_production_execution(self):
        release_ids = {g["id"] for g in self.plan["gates"] if g["release_required"]}
        self.evidence["records"] = [r for r in self.evidence["records"] if r["gate_id"] in release_ids]
        result = assess_project(self.profile, self.evidence)
        self.assertTrue(result["ready_for_human_review"])
        self.assertEqual("blocked", self.result("retirement-rehearsal", result)["status"])
        readiness = next(g for g in self.plan["gates"] if g["id"] == "operational-readiness")
        self.assertIn("incident-readiness", readiness["artifacts"])
        self.assertIn("retirement-readiness", readiness["artifacts"])

    def test_missing_failed_skipped_unrun_and_self_review_block_dependents(self):
        for status in ("failed", "skipped", "unrun"):
            with self.subTest(status=status):
                self.record("intent-brief")["status"] = status
                result = assess_project(self.profile, self.evidence)
                self.assertFalse(result["ready_for_human_review"])
                self.assertEqual("blocked", self.result("release-candidate", result)["status"])
        self.evidence = evidence_for(self.plan)
        self.record("intent-brief")["reviewer"] = "  SYNTHETIC-PRODUCER  "
        self.assertIn("self-review", " ".join(self.result("intent-brief")["issues"]))
        self.record("intent-brief")["reviewer"] = "ＳＹＮＴＨＥＴＩＣ-ＰＲＯＤＵＣＥＲ"
        self.assertIn("self-review", " ".join(self.result("intent-brief")["issues"]))
        self.evidence["records"] = []
        self.assertFalse(assess_project(self.profile, self.evidence)["ready_for_human_review"])

    def test_wrong_envelope_revision_profile_and_plan_fail_closed(self):
        for field in ("project_revision", "profile_digest", "plan_digest", "project_id"):
            with self.subTest(field=field):
                current = copy.deepcopy(self.evidence)
                current[field] = "wrong"
                result = assess_project(self.profile, current)
                self.assertFalse(result["valid"])
                self.assertFalse(result["ready_for_human_review"])
        current = {**self.profile, "description": "Changed context invalidates earlier evidence."}
        self.assertFalse(assess_project(current, self.evidence)["valid"])

    def test_artifact_revision_identity_and_observation_binding_are_required(self):
        for mutation in ("revision", "digest", "observation-binding", "missing-observation",
                         "missing-artifact", "duplicate-artifact", "unknown-artifact"):
            with self.subTest(mutation=mutation):
                self.evidence = evidence_for(self.plan)
                record = self.record("intent-brief")
                if mutation == "revision":
                    record["artifacts"][0]["revision"] = "f" * 40
                elif mutation == "digest":
                    record["artifacts"][0]["sha256"] = "main"
                elif mutation == "observation-binding":
                    record["observations"][0]["artifact_sha256"] = "0" * 64
                elif mutation == "missing-observation":
                    record["observations"] = []
                elif mutation == "missing-artifact":
                    record["artifacts"] = []
                elif mutation == "duplicate-artifact":
                    record["artifacts"].append(copy.deepcopy(record["artifacts"][0]))
                else:
                    record["artifacts"][0]["id"] = "unknown-artifact"
                self.assertEqual("blocked", self.result("intent-brief")["status"])

    def test_stale_future_naive_failed_and_empty_observations_block(self):
        for field, value in (("observed_at", "2020-01-01T00:00:00Z"),
                             ("observed_at", "2026-10-23T00:00:00Z"),
                             ("observed_at", "2026-10-22T10:00:00"),
                             ("observed_at", "not a time"), ("outcome", "failed"),
                             ("outcome", "unrun"), ("actual", ""), ("method", " ")):
            with self.subTest(field=field, value=value):
                self.evidence = evidence_for(self.plan)
                self.record("intent-brief")["observations"][0][field] = value
                self.assertEqual("blocked", self.result("intent-brief")["status"])
        self.evidence["as_of"] = "2026-10-22"
        self.assertFalse(assess_project(self.profile, self.evidence)["valid"])

    def test_duplicate_records_do_not_allow_pass_to_hide_later_failure(self):
        failed = copy.deepcopy(self.record("intent-brief"))
        failed["status"] = "failed"
        self.evidence["records"].append(failed)
        result = assess_project(self.profile, self.evidence)
        self.assertFalse(result["valid"])
        self.assertIn("duplicates", " ".join(result["errors"]))
        self.evidence["records"].reverse()
        self.assertFalse(assess_project(self.profile, self.evidence)["valid"])

    def test_duplicate_observation_and_failed_observation_cannot_be_hidden(self):
        first = self.record("intent-brief")["observations"][0]
        second = self.record("requirements-contract")["observations"][0]
        second["id"] = first["id"]
        self.assertEqual("blocked", self.result("requirements-contract")["status"])
        self.evidence = evidence_for(self.plan)
        bad = copy.deepcopy(self.record("intent-brief")["observations"][0])
        bad.update(id="later-failed-observation", outcome="failed")
        self.record("intent-brief")["observations"].append(bad)
        self.assertFalse(assess_project(self.profile, self.evidence)["ready_for_human_review"])

    def test_evidence_unknown_fields_inactive_gates_and_size_are_rejected(self):
        invalid = [None, [], {**self.evidence, "execute": "rm"},
                   {**self.evidence, "records": self.evidence["records"] * 4}]
        for item in invalid:
            self.assertFalse(assess_project(self.profile, item)["valid"])
        self.record("intent-brief")["gate_id"] = "tenant-isolation"
        self.assertFalse(assess_project(self.profile, self.evidence)["valid"])

    def test_unknown_prerequisites_and_cycles_fail_even_when_inactive(self):
        for mutation in ("unknown", "cycle", "inactive-cycle", "later-stage", "unknown-guide"):
            with self.subTest(mutation=mutation):
                root = self.temporary_config()
                path = root / "data/delivery.json"
                config = json.loads(path.read_text())
                gates = {g["id"]: g for g in config["gates"]}
                if mutation == "unknown":
                    gates["intent-brief"]["prerequisites"] = ["unknown-gate"]
                elif mutation == "cycle":
                    gates["intent-brief"]["prerequisites"] = ["intent-brief"]
                elif mutation == "inactive-cycle":
                    gates["high-consequence-review"]["prerequisites"] = ["high-consequence-review"]
                elif mutation == "later-stage":
                    gates["intent-brief"]["prerequisites"] = ["release-candidate"]
                else:
                    gates["intent-brief"]["guides"] = ["unknown-guide"]
                path.write_text(json.dumps(config))
                self.assertFalse(plan_project(self.profile, root)["valid"])

    def test_guide_revision_change_invalidates_prior_plan_digest(self):
        root = self.temporary_config()
        path = root / "data/catalog.json"
        catalog = json.loads(path.read_text())
        next(g for g in catalog["guides"] if g["id"] == "lifecycle")["revision"] += 1
        path.write_text(json.dumps(catalog))
        self.assertFalse(assess_project(self.profile, self.evidence, root)["valid"])

    def test_duplicate_blueprint_and_missing_stage_are_configuration_errors(self):
        root = self.temporary_config()
        path = root / "data/blueprints.json"
        blueprints = json.loads(path.read_text())
        blueprints["profiles"].append(copy.deepcopy(blueprints["profiles"][0]))
        path.write_text(json.dumps(blueprints))
        self.assertFalse(plan_project(self.profile, root)["valid"])
        root = self.temporary_config()
        path = root / "data/delivery.json"
        config = json.loads(path.read_text())
        config["gates"] = [g for g in config["gates"] if g["stage"] != "retirement"]
        path.write_text(json.dumps(config))
        self.assertFalse(plan_project(self.profile, root)["valid"])

    def test_registry_symlink_cannot_read_outside_library_root(self):
        root = self.temporary_config()
        path = root / "data/delivery.json"
        path.unlink()
        path.symlink_to(ROOT / "data/delivery.json")
        self.assertFalse(plan_project(self.profile, root)["valid"])

    def test_evidence_strings_never_become_paths_or_commands(self):
        dangerous = "file:///etc/passwd; $(printf should-never-execute)"
        self.record("intent-brief")["observations"][0]["method"] = dangerous
        result = assess_project(self.profile, self.evidence)
        self.assertTrue(result["valid"])
        self.assertNotIn(dangerous, json.dumps(result))
        self.assertFalse(result["production_ready"])

    def test_cli_plan_and_blocked_assessment_have_documented_exit_codes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "evidence.json"
            path.write_text(json.dumps({**self.evidence, "records": []}))
            args = [sys.executable, "-m", "library.delivery"]
            planned = subprocess.run(args + ["plan", "--profile", "templates/delivery-profile.json"],
                                     cwd=ROOT, capture_output=True, text=True, check=False)
            self.assertEqual(0, planned.returncode, planned.stderr)
            self.assertTrue(json.loads(planned.stdout)["valid"])
            assessed = subprocess.run(args + ["assess", "--profile", "templates/delivery-profile.json",
                                              "--evidence", str(path)],
                                      cwd=ROOT, capture_output=True, text=True, check=False)
            self.assertEqual(1, assessed.returncode, assessed.stderr)
            self.assertFalse(json.loads(assessed.stdout)["ready_for_human_review"])
            path.write_text('{"schema_version":1,"schema_version":1}')
            invalid = subprocess.run(args + ["plan", "--profile", str(path)], cwd=ROOT,
                                     capture_output=True, text=True, check=False)
            self.assertEqual(2, invalid.returncode)
            self.assertFalse(json.loads(invalid.stdout)["valid"])


if __name__ == "__main__":
    unittest.main()
