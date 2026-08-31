#!/usr/bin/env python3
"""Fetch and freeze exact-v1 arXiv HTML for the 2026-05-29 retained set."""
from __future__ import annotations

import concurrent.futures
import gzip
import hashlib
import json
import re
import subprocess
import time
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = json.loads((HERE / "screening-ledger-provisional.json").read_text())
BY_ID = {row["arxiv_id"]: row for row in SOURCE["identities"]}

# Admission is intentionally explicit.  Full-window screening is broader than
# the denominator; this set contains only durable state/control/evidence or
# execution-contract changes.  Domain-only methods remain pre-denominator.
CANDIDATES = """
2605.29224 2605.29233 2605.29251 2605.29262 2605.29267 2605.29275
2605.29313 2605.29343 2605.29350 2605.29359 2605.29360 2605.29387
2605.29438 2605.29442 2605.29454 2605.29463 2605.29489 2605.29495
2605.29517 2605.29524 2605.29548 2605.29561 2605.29577 2605.29585
2605.29601 2605.29605 2605.29629 2605.29639 2605.29640 2605.29664
2605.29682 2605.29697 2605.29707 2605.29708 2605.29727 2605.29752
2605.29786 2605.29790 2605.29843 2605.29873 2605.29888 2605.29956
2605.29960 2605.29979 2605.30011 2605.30040 2605.30052 2605.30070
2605.30083 2605.30085 2605.30087 2605.30102 2605.30104 2605.30117
2605.30152 2605.30155 2605.30159 2605.30169 2605.30202 2605.30218
2605.30219 2605.30226 2605.30227 2605.30251 2605.30260 2605.30263
2605.30280 2605.30288 2605.30290 2605.30294 2605.30322 2605.30329
2605.30334 2605.30335 2605.30337 2605.30343 2605.30346 2605.30348
2605.30351 2605.30381 2605.30392 2605.30393 2605.30406 2605.30434
2605.30448 2605.30451 2605.30454 2605.30484 2605.30501 2605.30504
2605.30514 2605.30519 2605.30521 2605.30523 2605.30524 2605.30537
2605.30542 2605.30557 2605.30568 2605.30571 2605.30574 2605.30580
2605.30604 2605.30613 2605.30619 2605.30621 2605.30628 2605.30640
2605.30653 2605.30656 2605.30660 2605.30675 2605.30686 2605.30690
2605.30693 2605.30698
""".split()

assert set(CANDIDATES) <= set(BY_ID)
BODY_DIR = HERE / "exact-v1-html"
BODY_DIR.mkdir(exist_ok=True)


def textify(raw: bytes) -> str:
    s = raw.decode("utf-8", "replace")
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.I | re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", unescape(s)).strip()


def headings(raw: bytes) -> list[str]:
    s = raw.decode("utf-8", "replace")
    out = []
    for m in re.finditer(r"<h([1-6])[^>]*>(.*?)</h\1>", s, flags=re.I | re.S):
        t = re.sub(r"<[^>]+>", " ", m.group(2))
        t = re.sub(r"\s+", " ", unescape(t)).strip()
        if t and t not in out:
            out.append(t[:220])
    return out


def fetch(aid: str) -> dict:
    url = f"https://arxiv.org/html/{aid}v1"
    target = BODY_DIR / f"{aid}v1.html.gz"
    if target.exists():
        raw = gzip.decompress(target.read_bytes())
        route = "reused_date_local_frozen_html"
    else:
        last = ""
        raw = b""
        for delay in (0, 2, 5):
            if delay:
                time.sleep(delay)
            try:
                cp = subprocess.run(
                    ["curl", "-L", "--fail", "--silent", "--show-error", "--max-time", "60", url],
                    check=False,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                raw = cp.stdout
                if cp.returncode:
                    raise RuntimeError(cp.stderr.decode("utf-8", "replace")[:400])
                if len(raw) > 10000 and b"<html" in raw[:2000].lower():
                    break
            except Exception as exc:  # recorded, never converted to a permanent blocker here
                last = f"{type(exc).__name__}: {exc}"
        if not raw or len(raw) <= 10000:
            return {"arxiv_id": aid, "url": url, "status": "transient_fetch_failed", "error": last, "bytes": len(raw)}
        target.write_bytes(gzip.compress(raw, compresslevel=9))
        route = "official_arxiv_html_v1"
    body = textify(raw)
    hs = headings(raw)
    return {
        "arxiv_id": aid,
        "source_family_id": "SF-2026-ARXIV-" + aid.replace(".", "-"),
        "url": url,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "status": "complete",
        "route": route,
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "normalized_text_sha256": hashlib.sha256(body.encode()).hexdigest(),
        "headings": hs,
        "opening_excerpt": body[:1200],
        "frozen_path": str(target.relative_to(HERE)),
    }


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    items = list(pool.map(fetch, CANDIDATES))

(HERE / "exact-v1-provenance.json").write_text(
    json.dumps({"schema": "exact-v1-provenance-v2.1", "report_date": "2026-05-29", "items": items}, ensure_ascii=False, indent=2) + "\n"
)
print(json.dumps({"requested": len(items), "complete": sum(x["status"] == "complete" for x in items), "failed": [x["arxiv_id"] for x in items if x["status"] != "complete"]}, ensure_ascii=False))
