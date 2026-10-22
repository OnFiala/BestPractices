"""Bounded, self-owned local experiments. No arbitrary network target option."""

import http.client
import json
import math
import platform
import queue
import sqlite3
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from pathlib import Path
from urllib.parse import urlsplit

from .service import TOKEN_ALPHA, FixtureServer, backup, connect, encode


def request(url, method, path, payload=None, key=None, token=TOKEN_ALPHA):
    parsed = urlsplit(url)
    if parsed.scheme != "http" or parsed.hostname != "127.0.0.1" or not parsed.port:
        raise ValueError("fixture client requires a loopback HTTP server")
    headers = {"Authorization": f"Bearer {token}"}
    body = None
    if payload is not None:
        body = encode(payload)
        headers["Content-Type"] = "application/json"
    if key is not None:
        headers["Idempotency-Key"] = key
    client = http.client.HTTPConnection("127.0.0.1", parsed.port, timeout=2)
    try:
        client.request(method, path, body, headers)
        response = client.getresponse()
        return response.status, json.loads(response.read())
    finally:
        client.close()


def write(url, item_id="demo", value=7, version=0, key="demo"):
    return request(url, "POST", "/tenants/alpha/items",
                   {"id": item_id, "value": value, "expected_version": version}, key)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def state(path):
    with connect(path) as db:
        return {
            "integrity": db.execute("PRAGMA integrity_check").fetchone()[0],
            "schema_version": db.execute("PRAGMA user_version").fetchone()[0],
            **{table: db.execute(f"SELECT count(*) FROM {table}").fetchone()[0]
               for table in ("items", "operations", "outbox", "effects")},
            "pending": db.execute("SELECT count(*) FROM outbox WHERE delivered=0").fetchone()[0],
            "effect_total": db.execute("SELECT coalesce(sum(total),0) FROM delivery_totals").fetchone()[0],
        }


def demo():
    with FixtureServer() as fixture:
        first = write(fixture.url)
        replay = write(fixture.url)
        consumed = request(fixture.url, "POST", "/tenants/alpha/consume", {})
        require(first == replay and first[0] == 200, "replay changed the result")
        return {"first": first, "replay": replay, "consumer": consumed, "state": state(fixture.db_path)}


@contextmanager
def crashing_server(db_path, fault):
    process = subprocess.Popen(
        [sys.executable, "-m", "examples.durable_service", "_crash-server",
         "--db", str(db_path), "--fault", fault],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
    )
    lines = queue.Queue()
    reader = threading.Thread(target=lambda: lines.put(process.stdout.readline()), daemon=True)
    reader.start()
    try:
        try:
            line = lines.get(timeout=5)
        except queue.Empty:
            raise RuntimeError("fault fixture did not become ready in five seconds") from None
        require(bool(line), "fault fixture exited before readiness")
        yield process, json.loads(line)["url"]
    finally:
        if process.poll() is None:
            process.terminate()
        try:
            process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=3)
        reader.join(timeout=1)
        process.stdout.close()
        process.stderr.close()


def crash_drill(directory, fault):
    path = Path(directory) / f"{fault}.db"
    started = time.perf_counter()
    with crashing_server(path, fault) as (process, url):
        if fault == "after_consumer_commit":
            require(write(url)[0] == 200, "fault fixture setup failed")
        try:
            if fault == "after_consumer_commit":
                request(url, "POST", "/tenants/alpha/consume", {})
            else:
                write(url)
            raise RuntimeError("fault request unexpectedly returned a response")
        except (OSError, http.client.HTTPException):
            pass
        require(process.wait(timeout=5) == 86, "child did not exit at the crash checkpoint")
    crashed = state(path)
    expected_items = 0 if fault == "before_commit" else 1
    require(crashed["items"] == crashed["operations"] == crashed["outbox"] == expected_items,
            "transaction recovery invariant failed")
    if fault == "after_consumer_commit":
        require(crashed["effects"] == crashed["effect_total"] == 1 and crashed["pending"] == 1,
                "consumer effect/ack interruption was not observed")
    with FixtureServer(path) as restarted:
        require(write(restarted.url)[0] == 200, "restart replay failed")
        require(request(restarted.url, "POST", "/tenants/alpha/consume", {})[0] == 200,
                "outbox recovery failed")
        recovered = state(path)
    require(recovered["items"] == recovered["operations"] == recovered["outbox"]
            == recovered["effects"] == recovered["effect_total"] == 1
            and recovered["pending"] == 0 and recovered["integrity"] == "ok",
            "recovery duplicated or lost an effect")
    return {"fault": fault, "child_exit": 86, "after_crash": crashed, "after_recovery": recovered,
            "elapsed_ms": round((time.perf_counter() - started) * 1000, 3)}


def migration_drill(directory):
    path = Path(directory) / "migration.db"
    with FixtureServer(path, schema_version=1) as legacy:
        require(write(legacy.url, item_id="old", key="old")[0] == 200, "v1 write failed")
    before = state(path)
    with FixtureServer(path) as upgraded:
        # Replaying v1 state and processing its pending v1 event must remain valid.
        require(write(upgraded.url, item_id="old", key="old")[1]["version"] == 1,
                "old idempotency result changed")
        require(write(upgraded.url, item_id="new", key="new")[0] == 200, "v2 write failed")
        require(request(upgraded.url, "POST", "/tenants/alpha/consume", {})[1]["effects"] == 2,
                "expanded schema cannot consume old events")
        # The exact v1 SQL column contract remains writable after expansion.
        with connect(path) as db:
            db.execute("BEGIN IMMEDIATE")
            db.execute("INSERT INTO items(tenant,id,value,version) VALUES('beta','legacy-sql',5,1)")
            legacy_row = db.execute("SELECT tenant,id,value,version FROM items "
                                    "WHERE tenant='beta'").fetchone()
            require(tuple(legacy_row) == ("beta", "legacy-sql", 5, 1), "old reader contract broke")
            db.rollback()  # This is a column-compatibility probe, not a business write.
    after = state(path)
    # A future schema is rejected; no silent down-migration is attempted.
    with connect(path) as db:
        db.execute("PRAGMA user_version=99")
    try:
        FixtureServer(path)
    except ValueError:
        future_rejected = True
    else:
        future_rejected = False
    require(future_rejected, "unsupported future schema was accepted")
    return {"before": before, "after": after, "v1_sql_compatible": True, "future_rejected": True}


def restore_drill(directory):
    source, snapshot, restored = (Path(directory) / name for name in ("source.db", "backup.db", "restored.db"))
    with FixtureServer(source) as original:
        require(write(original.url, "snapshotted", key="snapshotted")[0] == 200, "setup failed")
        backup(source, snapshot)
        require(write(original.url, "after-backup", key="after-backup")[0] == 200, "setup failed")
    backup(snapshot, restored)
    with FixtureServer(restored) as isolated:
        exported = request(isolated.url, "GET", "/tenants/alpha/export")[1]["items"]
        require([item["id"] for item in exported] == ["snapshotted"], "restore point mismatch")
        require(request(isolated.url, "POST", "/tenants/alpha/consume", {})[1]["effects"] == 1,
                "restored outbox did not recover")
        restored_state = state(restored)
    return {"source": state(source), "restored": restored_state,
            "known_post_backup_operations_absent": 1,
            "external_effects": "none; replay safety here applies only to this snapshot's local ledger"}


def drills():
    with tempfile.TemporaryDirectory(prefix="durable-drills-") as directory:
        return {"crashes": [crash_drill(directory, point) for point in
                            ("before_commit", "after_commit", "after_consumer_commit")],
                "restore": restore_drill(directory), "migration": migration_drill(directory)}


def percentiles(values):
    ordered = sorted(values)
    return {f"p{percentile}_ms": round(ordered[max(0, math.ceil(len(ordered) * percentile / 100) - 1)], 3)
            if ordered else None for percentile in (50, 95, 99)}


def benchmark(operations=120, concurrency=8, capacity=2, delay_ms=10, seconds=5):
    if type(operations) is not int or not 1 <= operations <= 500:
        raise ValueError("operations must be 1..500")
    if type(concurrency) is not int or not 1 <= concurrency <= 16:
        raise ValueError("concurrency must be 1..16")
    if type(seconds) not in (int, float) or not math.isfinite(seconds) or not 0.1 <= seconds <= 10:
        raise ValueError("seconds must be 0.1..10")
    samples, guard = [], threading.Lock()
    next_operation = 0
    start = time.perf_counter()
    cpu_start = time.process_time()
    with FixtureServer(capacity=capacity, delay_ms=delay_ms) as fixture:
        ready = threading.Barrier(concurrency)

        def worker():
            nonlocal next_operation
            ready.wait(timeout=3)
            while True:
                with guard:
                    if next_operation >= operations or time.perf_counter() - start >= seconds:
                        return
                    operation = next_operation
                    next_operation += 1
                began = time.perf_counter()
                try:
                    status, _ = write(fixture.url, item_id=f"item-{operation}", key=f"op-{operation}")
                    error = None
                except (OSError, http.client.HTTPException, ValueError) as failure:
                    status, error = 0, type(failure).__name__
                sample = {"operation": operation, "status": status, "error": error,
                          "latency_ms": round((time.perf_counter() - began) * 1000, 3)}
                with guard:
                    samples.append(sample)

        with ThreadPoolExecutor(max_workers=concurrency) as pool:
            futures = [pool.submit(worker) for _ in range(concurrency)]
            for future in futures:
                future.result(timeout=seconds + 5)
        elapsed = time.perf_counter() - start
        # Socket deadlines cap outstanding work; this drain is bounded separately.
        drain_deadline = time.perf_counter() + 3
        while fixture.metrics["active"] and time.perf_counter() < drain_deadline:
            time.sleep(0.005)
        server = fixture.metrics
        successes = sum(sample["status"] == 200 for sample in samples)
        rejected = sum(sample["status"] == 503 for sample in samples)
        recovery_start = time.perf_counter()
        recovery_deadline = recovery_start + 3
        recovery_status = status = 0
        recovery_error = None
        try:
            recovery_status, _ = write(fixture.url, item_id="recovery", key="recovery")
            recovery_ms = (time.perf_counter() - recovery_start) * 1000
            for _ in range(6):
                # A client can receive the final byte before its server worker
                # releases admission. Recovery starts each next request at idle.
                while fixture.metrics["active"] and time.perf_counter() < recovery_deadline:
                    time.sleep(0.005)
                status, consumed = request(fixture.url, "POST", "/tenants/alpha/consume", {})
                if status != 200 or consumed["pending"] == 0:
                    break
        except (OSError, http.client.HTTPException, ValueError) as failure:
            recovery_ms = (time.perf_counter() - recovery_start) * 1000
            recovery_error = type(failure).__name__
        persisted = state(fixture.db_path)
        integrity = (persisted["integrity"] == "ok" and persisted["pending"] == 0
                     and persisted["items"] == persisted["operations"] == persisted["outbox"]
                     == persisted["effects"] == persisted["effect_total"] == successes + 1)
        checks = {"recovery_integrity": recovery_status == status == 200 and integrity,
                  "expected_responses": all(sample["status"] in (200, 503) for sample in samples),
                  "bounded_admission": server["peak_active"] <= capacity and server["active"] == 0}
        size_bytes = sum(path.stat().st_size for path in fixture.db_path.parent.glob("state.db*"))
    return {
        "fixture_version": 1, "passed": all(checks.values()), "checks": checks,
        "model": "closed-loop burst; each worker waits for its response",
        "configuration": {"operations": operations, "concurrency": concurrency, "capacity": capacity,
                          "delay_ms": delay_ms, "scheduling_seconds_cap": seconds,
                          "request_timeout_seconds": 2, "drain_seconds_cap": 3},
        "environment": {"python": platform.python_version(), "sqlite": sqlite3.sqlite_version,
                        "platform": platform.platform(), "transport": "127.0.0.1 HTTP, fresh connection per request"},
        "offered": next_operation, "started": len(samples), "completed": sum(s["status"] > 0 for s in samples),
        "successful": successes, "rejected": rejected, "transport_errors": sum(s["status"] == 0 for s in samples),
        "not_offered_due_to_deadline": operations - next_operation, "server": server,
        "elapsed_seconds": round(elapsed, 6), "successful_operations_per_second": round(successes / elapsed, 3),
        "latency_all_responses": {"samples": len(samples), **percentiles([s["latency_ms"] for s in samples])},
        "latency_success": {"samples": successes, **percentiles([s["latency_ms"] for s in samples if s["status"] == 200])},
        "latency_rejected": {"samples": rejected, **percentiles([s["latency_ms"] for s in samples if s["status"] == 503])},
        "recovery": {"status": recovery_status, "error": recovery_error,
                     "request_ms": round(recovery_ms, 3), "integrity": integrity,
                     "state": persisted},
        "process_cpu_seconds_including_server": round(time.process_time() - cpu_start, 6),
        "database_bytes_after_recovery": size_bytes, "samples": sorted(samples, key=lambda sample: sample["operation"]),
        "limits": ["Tail percentiles are nearest-rank sample estimates; small samples cannot establish a tail SLO.",
                   "Generator and server share one process/CPU; no independent generator saturation or RSS measurement.",
                   "Closed-loop offering slows with responses; this is not an open arrival-rate or production capacity test.",
                   "Artificial bounded delay makes admission visible; it does not model a measured dependency.",
                   "Scheduling deadline stops new work; requests may drain afterward. No remote services or costs."],
    }
