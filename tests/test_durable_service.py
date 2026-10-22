"""HTTP contract/security oracles plus explicitly gray-box SQLite recovery drills."""

import json
import sqlite3
import tempfile
import threading
import unittest
from concurrent.futures import ThreadPoolExecutor
from http.client import HTTPConnection
from pathlib import Path
from urllib.parse import urlsplit

from examples.durable_service import TOKEN_ALPHA, TOKEN_BETA, FixtureServer
from examples.durable_service.experiments import benchmark, drills
from examples.durable_service.service import backup


def http(fixture, method, path, payload=None, key=None, token=TOKEN_ALPHA, raw=None):
    """Independent HTTP client: does not call Store or the example's client helper."""
    client = HTTPConnection("127.0.0.1", urlsplit(fixture.url).port, timeout=3)
    headers = {}
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"
    if key is not None:
        headers["Idempotency-Key"] = key
    if payload is not None or raw is not None:
        headers["Content-Type"] = "application/json"
    body = raw if raw is not None else json.dumps(payload) if payload is not None else None
    try:
        client.request(method, path, body, headers)
        response = client.getresponse()
        return response.status, json.loads(response.read())
    finally:
        client.close()


def item(item_id="record", value=7, version=0):
    return {"id": item_id, "value": value, "expected_version": version}


class DurableHTTPContractTests(unittest.TestCase):
    """Black-box API cases: assertions depend only on documented HTTP semantics."""

    def setUp(self):
        self.fixture = FixtureServer(capacity=16).__enter__()
        self.addCleanup(self.fixture.__exit__, None, None, None)

    def post(self, payload=None, key="operation", tenant="alpha", token=TOKEN_ALPHA):
        return http(self.fixture, "POST", f"/tenants/{tenant}/items",
                    item() if payload is None else payload, key, token)

    def test_replay_payload_conflict_and_optimistic_version(self):
        original = self.post()
        self.assertEqual(original, (200, {"tenant": "alpha", "id": "record", "value": 7, "version": 1}))
        self.assertEqual(self.post(), original)
        self.assertEqual(self.post(item(value=8))[0], 409)
        self.assertEqual(self.post(item(value=8), key="stale")[1], {"error": "version_conflict"})
        changed = self.post(item(value=8, version=1), key="update")
        self.assertEqual(changed[1]["version"], 2)
        self.assertEqual(self.post(), original)  # Stable replay even after subsequent changes.
        self.assertEqual(http(self.fixture, "GET", "/tenants/alpha/items/record"), changed)

    def test_missing_invalid_and_duplicate_authentication(self):
        for token in (None, "invented", TOKEN_ALPHA + " "):
            with self.subTest(token=token):
                self.assertEqual(http(self.fixture, "GET", "/tenants/alpha/export", token=token)[0], 401)
        self.assertEqual(self.post(token=None)[0], 401)
        client = HTTPConnection("127.0.0.1", urlsplit(self.fixture.url).port, timeout=3)
        try:
            client.putrequest("GET", "/tenants/alpha/export")
            client.putheader("Authorization", f"Bearer {TOKEN_ALPHA}")
            client.putheader("Authorization", f"Bearer {TOKEN_BETA}")
            client.endheaders()
            response = client.getresponse()
            self.assertEqual(response.status, 401)
            response.read()
        finally:
            client.close()
        self.assertEqual(http(self.fixture, "GET", "/tenants/alpha/export")[1], {"items": []})

    def test_cross_tenant_reads_writes_export_and_worker_are_denied_without_effect(self):
        beta = self.post(item("beta-record", 91), tenant="beta", token=TOKEN_BETA)
        self.assertEqual(beta[0], 200)
        cases = (("GET", "/tenants/beta/items/beta-record", None),
                 ("GET", "/tenants/beta/export", None),
                 ("POST", "/tenants/beta/items", item("beta-record", 99, 1)),
                 ("POST", "/tenants/beta/consume", {}))
        for method, path, payload in cases:
            with self.subTest(path=path):
                self.assertEqual(http(self.fixture, method, path, payload, "attack"),
                                 (403, {"error": "tenant_denied"}))
        self.assertEqual(http(self.fixture, "GET", "/tenants/alpha/items/beta-record")[0], 404)
        self.assertEqual(http(self.fixture, "GET", "/tenants/alpha/export")[1], {"items": []})
        self.assertEqual(http(self.fixture, "GET", "/tenants/beta/items/beta-record", token=TOKEN_BETA), beta)
        self.assertEqual(http(self.fixture, "POST", "/tenants/beta/consume", {}, token=TOKEN_BETA)[1],
                         {"processed": 1, "effects": 1, "pending": 0})

    def test_same_operation_key_and_object_id_are_separate_between_tenants(self):
        alpha = self.post(item(value=10))
        beta = self.post(item(value=20), tenant="beta", token=TOKEN_BETA)
        self.assertEqual((alpha[0], beta[0]), (200, 200))
        self.assertEqual(self.post(item(value=10)), alpha)
        self.assertEqual(self.post(item(value=20), tenant="beta", token=TOKEN_BETA), beta)
        self.assertEqual(http(self.fixture, "GET", "/tenants/alpha/export")[1]["items"], [alpha[1]])
        self.assertEqual(http(self.fixture, "GET", "/tenants/beta/export", token=TOKEN_BETA)[1]["items"], [beta[1]])

    def test_invalid_payloads_never_create_records(self):
        invalid = ([], {}, item(value=True), item(version=True), item(value=1_000_001),
                   item(version=-1), item("../../escape"), {**item(), "tenant": "beta"})
        for payload in invalid:
            with self.subTest(payload=payload):
                self.assertEqual(self.post(payload)[0], 400)
        self.assertEqual(self.post(key="bad'key")[0], 400)
        self.assertEqual(http(self.fixture, "POST", "/tenants/alpha/items", key="a", raw="{")[0], 400)
        self.assertEqual(http(self.fixture, "POST", "/tenants/alpha/items", key="a",
                              raw='{"id":"x","id":"y","value":1,"expected_version":0}')[0], 400)
        self.assertEqual(http(self.fixture, "POST", "/tenants/alpha/items", key="a",
                              raw="[" * 1100 + "]" * 1100)[0], 400)
        self.assertEqual(http(self.fixture, "POST", "/tenants/alpha/items", key="a", raw=" " * 4097)[0], 413)
        self.assertEqual(http(self.fixture, "GET", "/tenants/alpha/export")[1], {"items": []})

    def test_simultaneous_identical_retries_have_one_result_and_effect(self):
        barrier = threading.Barrier(8)

        def retry(_):
            barrier.wait(timeout=3)
            return self.post()

        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(retry, range(8)))
        self.assertTrue(all(result == results[0] for result in results))
        self.assertEqual(results[0][0], 200)
        self.assertEqual(http(self.fixture, "GET", "/tenants/alpha/export")[1]["items"], [results[0][1]])
        self.assertEqual(http(self.fixture, "POST", "/tenants/alpha/consume", {})[1],
                         {"processed": 1, "effects": 1, "pending": 0})

    def test_simultaneous_version_writers_have_one_winner(self):
        barrier = threading.Barrier(2)

        def contender(value):
            barrier.wait(timeout=3)
            return self.post(item(value=value), key=f"writer-{value}")

        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(contender, (11, 22)))
        self.assertEqual(sorted(result[0] for result in results), [200, 409])
        winner = next(result for result in results if result[0] == 200)
        self.assertEqual(http(self.fixture, "GET", "/tenants/alpha/items/record"), winner)
        self.assertEqual(http(self.fixture, "POST", "/tenants/alpha/consume", {})[1]["effects"], 1)


class DurableIntegrationTests(unittest.TestCase):
    """Gray-box integration: real SQLite state and controlled process failures."""

    def test_transactional_outbox_and_concurrent_consumers(self):
        with FixtureServer(capacity=4) as fixture:
            self.assertEqual(http(fixture, "POST", "/tenants/alpha/items", item(), "once")[0], 200)
            with sqlite3.connect(fixture.db_path) as db:
                for table in ("items", "operations", "outbox"):
                    self.assertEqual(db.execute(f"SELECT count(*) FROM {table}").fetchone()[0], 1)
                self.assertEqual(db.execute("SELECT count(*) FROM effects").fetchone()[0], 0)
            with ThreadPoolExecutor(max_workers=2) as pool:
                results = list(pool.map(lambda _: http(fixture, "POST", "/tenants/alpha/consume", {}), range(2)))
            self.assertTrue(all(status == 200 for status, _ in results))
            self.assertEqual(http(fixture, "POST", "/tenants/alpha/consume", {})[1],
                             {"processed": 0, "effects": 1, "pending": 0})
            with sqlite3.connect(fixture.db_path) as db:
                self.assertEqual(db.execute("SELECT count(*) FROM effects").fetchone()[0], 1)
                self.assertEqual(db.execute("SELECT total FROM delivery_totals").fetchone()[0], 1)
                self.assertEqual(db.execute("SELECT delivered FROM outbox").fetchone()[0], 1)

    def test_process_crashes_restart_restore_and_schema_compatibility(self):
        evidence = drills()
        self.assertEqual(len(evidence["crashes"]), 3)
        for case in evidence["crashes"]:
            self.assertEqual(case["child_exit"], 86)
            self.assertEqual(case["after_recovery"]["effects"], 1)
            self.assertEqual(case["after_recovery"]["pending"], 0)
        self.assertEqual(evidence["restore"]["source"]["items"], 2)
        self.assertEqual(evidence["restore"]["restored"]["items"], 1)
        self.assertEqual(evidence["migration"]["before"]["schema_version"], 1)
        self.assertEqual(evidence["migration"]["after"]["schema_version"], 2)
        self.assertTrue(evidence["migration"]["v1_sql_compatible"])
        self.assertTrue(evidence["migration"]["future_rejected"])

    def test_unknown_event_schema_is_not_acknowledged_or_applied(self):
        with FixtureServer() as fixture:
            self.assertEqual(http(fixture, "POST", "/tenants/alpha/items", item(), "once")[0], 200)
            with sqlite3.connect(fixture.db_path) as db:
                db.execute("UPDATE outbox SET schema_version=99")
            self.assertEqual(http(fixture, "POST", "/tenants/alpha/consume", {}),
                             (409, {"error": "unsupported_event_schema"}))
            with sqlite3.connect(fixture.db_path) as db:
                self.assertEqual(db.execute("SELECT delivered FROM outbox").fetchone()[0], 0)
                self.assertEqual(db.execute("SELECT count(*) FROM effects").fetchone()[0], 0)

    def test_bounded_overload_recovers_without_data_loss(self):
        evidence = benchmark(operations=40, concurrency=8, capacity=1, delay_ms=100, seconds=3)
        self.assertTrue(evidence["passed"], {k: v for k, v in evidence.items() if k != "samples"})
        self.assertGreater(evidence["successful"], 0)
        self.assertGreater(evidence["rejected"], 0)
        self.assertEqual(evidence["offered"], 40)
        self.assertEqual(evidence["started"], evidence["completed"])
        self.assertEqual(evidence["successful"] + evidence["rejected"], 40)
        self.assertEqual(evidence["server"]["peak_active"], 1)
        self.assertEqual(evidence["server"]["active"], 0)
        self.assertEqual(evidence["server"]["offered"], evidence["server"]["started"] + evidence["server"]["rejected"])
        self.assertTrue(evidence["recovery"]["integrity"])
        self.assertEqual(evidence["recovery"]["state"]["effects"], evidence["successful"] + 1)

    def test_unsafe_experiment_limits_and_overwriting_backup_are_rejected(self):
        for kwargs in ({"operations": 501}, {"concurrency": 17}, {"seconds": 11},
                       {"seconds": float("nan")}, {"capacity": 17}, {"delay_ms": 251}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                benchmark(**kwargs)
        with FixtureServer() as fixture, tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "backup.db"
            backup(fixture.db_path, destination)
            with self.assertRaises(ValueError):
                backup(fixture.db_path, destination)
            dangling = Path(directory) / "dangling.db"
            missing = Path(directory) / "missing.db"
            dangling.symlink_to(missing)
            with self.assertRaises(ValueError):
                backup(fixture.db_path, dangling)
            self.assertFalse(missing.exists())


if __name__ == "__main__":
    unittest.main()
