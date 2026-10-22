"""Original loopback-only, synthetic frontend fixture. Never a production server."""

import argparse
import json
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parent
STATIC = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/index.html": ("index.html", "text/html; charset=utf-8"),
    "/styles.css": ("styles.css", "text/css; charset=utf-8"),
    "/app.mjs": ("app.mjs", "text/javascript; charset=utf-8"),
    "/state.mjs": ("state.mjs", "text/javascript; charset=utf-8"),
    "/controller.mjs": ("controller.mjs", "text/javascript; charset=utf-8"),
}
SCENARIOS = {"normal", "empty", "error", "retry", "slow", "injection"}
RESOURCES = [
    {"id": "r1", "title": "Make state ownership visible",
     "summary": "Give navigation, remote results, and temporary interaction state one owner each."},
    {"id": "r2", "title": "Testing the recovery path",
     "summary": "Try an empty response, a failure, and a late result before calling a journey done."},
    {"id": "r3", "title": "Measure the journey",
     "summary": "Record what a person waits for before choosing what to optimize."},
]


class FixtureHandler(BaseHTTPRequestHandler):
    def log_message(self, _format, *_args):
        # Queries can contain user text. The fixture does not log request contents.
        pass

    def respond(self, status, body, content_type="application/json; charset=utf-8"):
        if not isinstance(body, bytes):
            body = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Content-Security-Policy", "default-src 'none'; script-src 'self'; "
                         "style-src 'self'; connect-src 'self'; base-uri 'none'; "
                         "form-action 'self'; frame-ancestors 'none'")
        self.end_headers()
        try:
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            pass  # Expected when a browser cancels an in-flight fixture response.

    def do_GET(self):  # noqa: N802 - stdlib handler API
        expected_host = f"127.0.0.1:{self.server.server_port}"
        if self.headers.get("Host") != expected_host:
            self.respond(403, {"error": "Use the printed loopback URL."})
            return
        if len(self.path) > 2048:
            self.respond(414, {"error": "Request too long."})
            return
        parsed = urlsplit(self.path)
        if parsed.scheme or parsed.netloc:
            self.respond(400, {"error": "Relative request paths required."})
            return
        if parsed.path in STATIC:
            name, content_type = STATIC[parsed.path]
            self.respond(200, (ROOT / name).read_bytes(), content_type)
        elif parsed.path == "/api/resources":
            self.resources(parsed.query)
        else:
            self.respond(404, {"error": "Not found."})

    def resources(self, raw_query):
        try:
            params = parse_qs(raw_query, keep_blank_values=True, max_num_fields=3)
            if set(params) - {"q", "scenario", "attempt"} or any(
                len(values) != 1 for values in params.values()
            ):
                raise ValueError
            q = params.get("q", [""])[0]
            scenario = params.get("scenario", ["normal"])[0]
            attempt = params.get("attempt", ["1"])[0]
            if len(q) > 80 or scenario not in SCENARIOS or attempt not in {"1", "2"}:
                raise ValueError
        except ValueError:
            self.respond(400, {"error": "Invalid fixture query."})
            return
        time.sleep(0.9 if scenario == "slow" else 0.12)
        if scenario == "error" or (scenario == "retry" and attempt == "1"):
            self.respond(503, {"error": "Synthetic unavailable response."})
            return
        items = RESOURCES
        if scenario == "empty":
            items = []
        elif scenario == "injection":
            items = [{"id": "text", "title": '<img src=x onerror="window.__injected=true">',
                      "summary": '<script>window.__injected=true</script> & "quoted" text'}]
        elif scenario == "slow":
            items = [{"id": "slow", "title": "Slow response arrived",
                      "summary": "A deliberately delayed synthetic result."}]
        elif q:
            items = [item for item in items if q.casefold() in
                     f"{item['title']} {item['summary']}".casefold()]
        self.respond(200, {"items": items})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=0, help="Loopback port; 0 selects a free port.")
    args = parser.parse_args()
    if not 0 <= args.port <= 65535:
        parser.error("port must be between 0 and 65535")
    with ThreadingHTTPServer(("127.0.0.1", args.port), FixtureHandler) as server:
        print(f"http://127.0.0.1:{server.server_port}", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
