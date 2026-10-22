"""Loopback HTTP, real SQLite transactions, and deliberately synthetic identity."""

import json
import os
import re
import sqlite3
import tempfile
import threading
import time
import uuid
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

TOKEN_ALPHA = "synthetic-alpha-only"
TOKEN_BETA = "synthetic-beta-only"
TOKENS = {TOKEN_ALPHA: "alpha", TOKEN_BETA: "beta"}
IDENTIFIER = re.compile(r"[A-Za-z0-9_-]{1,64}\Z")
MAX_BODY = 4096
SCHEMA_VERSION = 2


class Rejected(Exception):
    def __init__(self, status, reason):
        self.status, self.reason = status, reason


def encode(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def unique_object(pairs):
    result = dict(pairs)
    if len(result) != len(pairs):
        raise ValueError("duplicate JSON property")
    return result


@contextmanager
def connect(path):
    db = sqlite3.connect(path, timeout=1, isolation_level=None)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys=ON")
    db.execute("PRAGMA synchronous=FULL")
    try:
        yield db
    finally:
        db.close()


def initialize(path, target_version=SCHEMA_VERSION):
    """Expand v1 to v2 atomically; reject unknown versions before serving."""
    if target_version not in (1, 2):
        raise ValueError("supported schema versions are 1 and 2")
    with connect(path) as db:
        version = db.execute("PRAGMA user_version").fetchone()[0]
        if version > target_version:
            raise ValueError("database is newer than this reader")
        db.execute("PRAGMA journal_mode=WAL")
        db.execute("BEGIN IMMEDIATE")
        try:
            if version == 0:
                statements = (
                    "CREATE TABLE items (tenant TEXT, id TEXT, value INTEGER NOT NULL, "
                    "version INTEGER NOT NULL CHECK(version>0), PRIMARY KEY(tenant,id))",
                    "CREATE TABLE operations (tenant TEXT, action TEXT, key TEXT, "
                    "payload TEXT NOT NULL, result TEXT NOT NULL, PRIMARY KEY(tenant,action,key))",
                    "CREATE TABLE outbox (event_id TEXT PRIMARY KEY, tenant TEXT NOT NULL, "
                    "payload TEXT NOT NULL, delivered INTEGER NOT NULL DEFAULT 0)",
                    "CREATE TABLE effects (tenant TEXT, event_id TEXT, payload TEXT NOT NULL, "
                    "PRIMARY KEY(tenant,event_id), FOREIGN KEY(event_id) REFERENCES outbox(event_id))",
                    "CREATE TABLE delivery_totals (tenant TEXT PRIMARY KEY, total INTEGER NOT NULL)",
                )
                for statement in statements:
                    db.execute(statement)
                db.execute("PRAGMA user_version=1")
                version = 1
            if version == 1 and target_version == 2:
                db.execute("ALTER TABLE items ADD COLUMN label TEXT NOT NULL DEFAULT ''")
                db.execute("ALTER TABLE outbox ADD COLUMN schema_version INTEGER NOT NULL DEFAULT 1")
                db.execute("PRAGMA user_version=2")
            db.commit()
        except BaseException:
            db.rollback()
            raise


def backup(source, destination):
    """Consistent local snapshot, always into a new file; also used for restore."""
    source, destination = Path(source), Path(destination)
    if not source.is_file():
        raise ValueError("source must exist")
    try:
        with destination.open("xb"):
            pass  # Reserve exclusively; dangling symlinks also count as existing.
    except FileExistsError:
        raise ValueError("destination must be new") from None
    with connect(source) as original, connect(destination) as copy:
        original.backup(copy)
        if copy.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise ValueError("snapshot integrity check failed")


class Store:
    def __init__(self, path, fault=None, schema_version=SCHEMA_VERSION):
        self.path, self.fault = path, fault
        initialize(path, schema_version)

    def checkpoint(self, point):
        if self.fault == point:
            # Only the private fault-drill child enables this. No HTTP fault switch.
            os._exit(86)

    def write(self, tenant, key, payload):
        if not isinstance(key, str) or not IDENTIFIER.fullmatch(key):
            raise Rejected(400, "invalid_idempotency_key")
        if (not isinstance(payload, dict) or set(payload) != {"id", "value", "expected_version"}
                or not isinstance(payload["id"], str)
                or not IDENTIFIER.fullmatch(payload["id"])
                or type(payload["value"]) is not int or abs(payload["value"]) > 1_000_000
                or type(payload["expected_version"]) is not int
                or not 0 <= payload["expected_version"] <= 1_000_000):
            raise Rejected(400, "invalid_item")
        canonical = encode(payload)
        with connect(self.path) as db:
            db.execute("BEGIN IMMEDIATE")
            old = db.execute("SELECT payload,result FROM operations WHERE tenant=? AND "
                             "action='items.upsert' AND key=?", (tenant, key)).fetchone()
            if old:
                if old["payload"] != canonical:
                    raise Rejected(409, "idempotency_conflict")
                return json.loads(old["result"])
            row = db.execute("SELECT version FROM items WHERE tenant=? AND id=?",
                             (tenant, payload["id"])).fetchone()
            version = row["version"] if row else 0
            if version != payload["expected_version"]:
                raise Rejected(409, "version_conflict")
            result = {"tenant": tenant, "id": payload["id"], "value": payload["value"],
                      "version": version + 1}
            db.execute("INSERT INTO items(tenant,id,value,version) VALUES(?,?,?,?) "
                       "ON CONFLICT(tenant,id) DO UPDATE SET value=excluded.value, "
                       "version=excluded.version", tuple(result.values()))
            db.execute("INSERT INTO operations VALUES(?,'items.upsert',?,?,?)",
                       (tenant, key, canonical, encode(result)))
            # Common columns remain writable by the v1 writer after the v2 expansion.
            db.execute("INSERT INTO outbox(event_id,tenant,payload) VALUES(?,?,?)",
                       (uuid.uuid4().hex, tenant, encode(result)))
            self.checkpoint("before_commit")
            db.commit()
            self.checkpoint("after_commit")
            return result

    def read(self, tenant, item_id=None):
        with connect(self.path) as db:
            if item_id is not None:
                row = db.execute("SELECT tenant,id,value,version FROM items WHERE tenant=? AND id=?",
                                 (tenant, item_id)).fetchone()
                if row is None:
                    raise Rejected(404, "not_found")
                return dict(row)
            return {"items": [dict(row) for row in db.execute(
                "SELECT tenant,id,value,version FROM items WHERE tenant=? ORDER BY id", (tenant,))]}

    def consume(self, tenant):
        """At-least-once relay, idempotent local consumer, separate acknowledgement."""
        with connect(self.path) as db:
            events = db.execute("SELECT * FROM outbox WHERE tenant=? AND delivered=0 "
                                "ORDER BY rowid LIMIT 100", (tenant,)).fetchall()
        processed = 0
        for event in events:
            if "schema_version" in event.keys() and event["schema_version"] != 1:
                raise Rejected(409, "unsupported_event_schema")
            with connect(self.path) as db:
                db.execute("BEGIN IMMEDIATE")
                inserted = db.execute("INSERT OR IGNORE INTO effects VALUES(?,?,?)",
                                      (tenant, event["event_id"], event["payload"])).rowcount
                if inserted:
                    db.execute("INSERT INTO delivery_totals VALUES(?,1) ON CONFLICT(tenant) "
                               "DO UPDATE SET total=total+1", (tenant,))
                db.commit()
            self.checkpoint("after_consumer_commit")
            with connect(self.path) as db:
                db.execute("UPDATE outbox SET delivered=1 WHERE tenant=? AND event_id=?",
                           (tenant, event["event_id"]))
            processed += 1
        with connect(self.path) as db:
            row = db.execute("SELECT total FROM delivery_totals WHERE tenant=?", (tenant,)).fetchone()
            pending = db.execute("SELECT count(*) FROM outbox WHERE tenant=? AND delivered=0",
                                 (tenant,)).fetchone()[0]
        return {"processed": processed, "effects": row[0] if row else 0, "pending": pending}


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.0"

    def log_message(self, *args):
        pass  # No credentials, payloads, or noisy access logs in the teaching fixture.

    def reply(self, status, body):
        data = encode(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Connection", "close")
        if status == 503:
            self.send_header("Retry-After", "1")
        self.end_headers()
        self.wfile.write(data)

    def body(self):
        if self.headers.get("Transfer-Encoding"):
            raise Rejected(400, "unsupported_transfer_encoding")
        lengths = self.headers.get_all("Content-Length", [])
        if len(lengths) != 1 or not lengths[0].isascii() or not lengths[0].isdigit():
            raise Rejected(400, "invalid_content_length")
        if len(lengths[0]) > 10:
            raise Rejected(413, "body_too_large")
        length = int(lengths[0])
        if length > MAX_BODY:
            raise Rejected(413, "body_too_large")
        if self.headers.get("Content-Type") != "application/json":
            raise Rejected(415, "expected_json")
        try:
            raw = self.rfile.read(length)
            if len(raw) != length:
                raise ValueError("truncated")
            return json.loads(raw, object_pairs_hook=unique_object)
        except (ValueError, UnicodeError, RecursionError):
            raise Rejected(400, "invalid_json") from None

    def dispatch(self):
        tokens = self.headers.get_all("Authorization", [])
        tenant = TOKENS.get(tokens[0][7:]) if len(tokens) == 1 and tokens[0].startswith("Bearer ") else None
        if tenant is None:
            raise Rejected(401, "unauthenticated")
        parts = self.path.split("/")
        if len(parts) < 4 or parts[:2] != ["", "tenants"]:
            raise Rejected(404, "not_found")
        if parts[2] != tenant:
            raise Rejected(403, "tenant_denied")
        if self.command == "GET" and parts[3:] == ["export"]:
            return self.server.store.read(tenant)
        if self.command == "GET" and len(parts) == 5 and parts[3] == "items":
            if not IDENTIFIER.fullmatch(parts[4]):
                raise Rejected(400, "invalid_id")
            return self.server.store.read(tenant, parts[4])
        if self.command == "POST" and parts[3:] == ["items"]:
            keys = self.headers.get_all("Idempotency-Key", [])
            return self.server.store.write(tenant, keys[0] if len(keys) == 1 else None, self.body())
        if self.command == "POST" and parts[3:] == ["consume"]:
            if self.body() != {}:
                raise Rejected(400, "expected_empty_object")
            return self.server.store.consume(tenant)
        raise Rejected(404, "not_found")

    def do_GET(self):
        try:
            if self.server.delay_ms:
                time.sleep(self.server.delay_ms / 1000)
            self.reply(200, self.dispatch())
        except Rejected as error:
            self.reply(error.status, {"error": error.reason})
        except sqlite3.OperationalError:
            self.reply(503, {"error": "storage_unavailable"})
        except (BrokenPipeError, ConnectionResetError, TimeoutError):
            pass

    do_POST = do_GET


class BoundedServer(ThreadingHTTPServer):
    daemon_threads = False
    request_queue_size = 32

    def __init__(self, store, capacity, delay_ms):
        self.store, self.delay_ms = store, delay_ms
        self.slots = threading.BoundedSemaphore(capacity)
        self.lock = threading.Lock()
        self.counters = dict(offered=0, started=0, completed=0, rejected=0, active=0, peak_active=0)
        super().__init__(("127.0.0.1", 0), Handler)

    def process_request(self, request, client_address):
        request.settimeout(2)
        with self.lock:
            self.counters["offered"] += 1
        if not self.slots.acquire(blocking=False):
            with self.lock:
                self.counters["rejected"] += 1
            try:
                # Consume a bounded fixture request before closing so clients see
                # HTTP 503 rather than a reset from an unread request body.
                BusyHandler(request, client_address, self)
            except OSError:
                pass
            self.shutdown_request(request)
            return
        with self.lock:
            self.counters["started"] += 1
            self.counters["active"] += 1
            self.counters["peak_active"] = max(self.counters["peak_active"], self.counters["active"])
        try:
            super().process_request(request, client_address)
        except BaseException:
            self.release()
            raise

    def release(self):
        with self.lock:
            self.counters["active"] -= 1
            self.counters["completed"] += 1
            self.slots.release()

    def process_request_thread(self, request, client_address):
        try:
            super().process_request_thread(request, client_address)
        finally:
            self.release()


class BusyHandler(Handler):
    def do_GET(self):
        length = self.headers.get("Content-Length", "0")
        if length.isascii() and length.isdigit() and len(length) <= 10 and int(length) <= MAX_BODY:
            self.rfile.read(int(length))
        self.reply(503, {"error": "overloaded"})

    do_POST = do_GET


class FixtureServer:
    """Context manager: fixed loopback address, ephemeral port, temporary DB by default."""

    def __init__(self, db_path=None, capacity=4, delay_ms=0, *, fault=None, schema_version=2):
        if type(capacity) is not int or not 1 <= capacity <= 16:
            raise ValueError("capacity must be 1..16")
        if type(delay_ms) is not int or not 0 <= delay_ms <= 250:
            raise ValueError("delay_ms must be 0..250")
        if fault not in (None, "before_commit", "after_commit", "after_consumer_commit"):
            raise ValueError("unknown fault point")
        self.temporary = tempfile.TemporaryDirectory(prefix="durable-service-") if db_path is None else None
        self.db_path = Path(db_path) if db_path is not None else Path(self.temporary.name) / "state.db"
        self.server = BoundedServer(Store(self.db_path, fault, schema_version), capacity, delay_ms)
        self.url = f"http://127.0.0.1:{self.server.server_port}"
        self.thread = threading.Thread(target=self.server.serve_forever, kwargs={"poll_interval": 0.02})

    def __enter__(self):
        self.thread.start()
        return self

    @property
    def metrics(self):
        with self.server.lock:
            return dict(self.server.counters)

    def __exit__(self, *args):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=3)
        if self.temporary:
            self.temporary.cleanup()
