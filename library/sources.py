"""Bounded primary-source observation. Observations never rewrite recommendations."""

import argparse
import datetime as dt
import hashlib
import json
import re
import ssl
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from library.content import ROOT, read_json

MAX_BYTES = 2_000_000
ALLOWED_HOSTS = {"raw.githubusercontent.com"}


def validate_url(url: str):
    parsed = urllib.parse.urlsplit(url)
    if (parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS
            or parsed.username or parsed.password or parsed.port not in (None, 443)):
        raise ValueError("Source URL is outside the reviewed HTTPS fetch policy")


class SafeRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        validate_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def observe(source: dict, documents: Path | None = None) -> dict:
    try:
        validate_url(source["url"])
        # Preserve platform proxy configuration and system trust; never disable TLS.
        opener = urllib.request.build_opener(
            SafeRedirect(), urllib.request.HTTPSHandler(context=ssl.create_default_context())
        )
        request = urllib.request.Request(source["url"], headers={
            "User-Agent": "BestPractices-source-monitor/0.1 (+https://github.com/OnFiala/BestPractices)"
        })
        with opener.open(request, timeout=20) as response:
            data = response.read(MAX_BYTES + 1)
            if not data or len(data) > MAX_BYTES:
                raise ValueError("Empty or oversized source response")
            if documents is not None:
                if not re.fullmatch(r"[a-z0-9-]+", source["id"]):
                    raise ValueError("Invalid evidence filename")
                documents.mkdir(parents=True, exist_ok=True)
                (documents / (source["id"] + ".txt")).write_bytes(data)
            return {"status": "ok", "sha256": hashlib.sha256(data).hexdigest(),
                    "bytes": len(data), "url": source["url"]}
    except (OSError, ValueError) as exc:
        return {"status": "unavailable", "error": str(exc), "url": source["url"]}


def compare(sources: list[dict], baseline: dict, observations: dict,
            today: dt.date) -> dict:
    changed, unavailable, overdue = [], [], []
    for source in sources:
        sid = source["id"]
        current = observations[sid]
        if current["status"] != "ok":
            unavailable.append(sid)
        elif current["sha256"] != baseline.get(sid, {}).get("sha256"):
            changed.append(sid)
        age = (today - dt.date.fromisoformat(source["reviewed_on"])).days
        if age > source["review_days"]:
            overdue.append(sid)
    return {"changed": changed, "unavailable": unavailable, "overdue": overdue,
            "action_required": bool(changed or unavailable or overdue)}


def check(output: Path, candidate: Path | None = None, root: Path = ROOT,
          documents: Path | None = None) -> int:
    sources = read_json(root / "data/sources.json")["sources"]
    baseline = read_json(root / "data/source-baseline.json")["observations"]
    with ThreadPoolExecutor(max_workers=4) as pool:
        observations = dict(zip((s["id"] for s in sources),
                                pool.map(lambda s: observe(s, documents), sources)))
    now = dt.datetime.now(dt.timezone.utc)
    report = {"schema_version": 1, "checked_at": now.isoformat(),
              **compare(sources, baseline, observations, now.date()),
              "observations": observations,
              "meaning": "Retrieval and hash comparison only; not semantic approval."}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if candidate and report["action_required"]:
        candidate.parent.mkdir(parents=True, exist_ok=True)
        candidate.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("changed", "unavailable", "overdue")}))
    return 1 if report["unavailable"] else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["check"])
    parser.add_argument("--output", type=Path, default=ROOT / "reports/sources.json")
    parser.add_argument("--candidate", type=Path)
    parser.add_argument("--documents", type=Path,
                        help="Store bounded untrusted evidence for an offline agent run")
    args = parser.parse_args()
    return check(args.output, args.candidate, documents=args.documents)


if __name__ == "__main__":
    raise SystemExit(main())
