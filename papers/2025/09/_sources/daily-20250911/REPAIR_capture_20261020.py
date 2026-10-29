"""Bounded Sep10 discovery and exact DOI recovery; no automatic review claims."""

import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from urllib.parse import urlencode

BASE = Path(__file__).parent
WINDOW = "registered:[2025-09-09T16:00:00Z TO 2025-09-10T15:59:59Z]"
TERMS = {
    "MODEL": '"language model" OR transformer OR "mixture of experts" OR "foundation model"',
    "SYSTEM": '("language model" OR LLM OR GPU) AND (inference OR serving OR communication OR kernel OR parallel OR compiler)',
    "AGENT": '("language model" OR LLM) AND (agent OR retrieval OR memory OR safety OR jailbreak OR "tool calling")',
    "MULTI": '"vision language" OR "vision-language-action" OR "world model" OR "video generation" OR diffusion',
}


def capture(name, url):
    stem = BASE / ("REPAIR_" + name + "_20261020")
    raw = Path(str(stem) + ".raw")
    headers = Path(str(stem) + ".headers.raw")
    request = Path(str(stem) + ".request.json")
    if any(p.exists() for p in (raw, headers, request)):
        raise SystemExit("Refusing to refetch/overwrite existing capture: " + name)
    start = time.monotonic()
    checked = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = subprocess.run([
        "curl", "--location", "--silent", "--show-error", "--max-time", "90",
        "--user-agent", "AI-System-Design/1.0", "--dump-header", str(headers),
        "--output", str(raw), "--write-out", "%{http_code}", url,
    ], capture_output=True, text=True)
    body = raw.read_bytes() if raw.exists() else b""
    record = {"method": "GET", "url": url, "checked_utc": checked,
              "exit_code": result.returncode, "status": result.stdout,
              "seconds": time.monotonic() - start, "bytes": len(body),
              "sha256": hashlib.sha256(body).hexdigest(), "stderr": result.stderr,
              "scope": "Sep10 BJT; discovery/identity only, not manuscript review"}
    request.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: record[k] for k in ("status", "exit_code", "seconds", "bytes")}), name, flush=True)


def datacite(query):
    return "https://api.datacite.org/dois?" + urlencode({
        "client-id": "arxiv.content", "page[size]": 100, "query": query,
    })


if __name__ == "__main__":
    name = sys.argv[1]
    if name == "DATE13":
        ids = ["2509.07963", "2509.07945", "2509.07936", "2509.07966",
               "2509.07962", "2509.07941", "2509.07908", "2509.08032",
               "2509.07980", "2509.07979", "2509.07920", "2509.07957", "2509.07955"]
        capture(name, datacite(" OR ".join("doi:10.48550/arxiv." + i for i in ids)))
    elif name == "DATE_OLD10":
        ids = ["2509.08000", "2509.08004", "2509.08008", "2509.08010", "2509.08016",
               "2509.08022", "2509.08031", "2509.08697", "2509.08750", "2509.08829"]
        capture(name, datacite(" OR ".join("doi:10.48550/arxiv." + i for i in ids)))
    elif name == "CURRENT13":
        ids = ["2509.07963", "2509.07945", "2509.07936", "2509.07966",
               "2509.07962", "2509.07941", "2509.07908", "2509.08032",
               "2509.07980", "2509.07979", "2509.07920", "2509.07957", "2509.07955"]
        capture(name, "https://export.arxiv.org/api/query?" + urlencode({"id_list": ",".join(ids), "max_results": 30}))
    elif name == "FIRST5_V1":
        capture(name, "https://export.arxiv.org/api/query?" + urlencode({
            "id_list": ",".join(i + "v1" for i in ["2509.07295", "2509.07379", "2509.07506", "2509.07596", "2509.07727"]),
            "max_results": 20,
        }))
    elif name in TERMS:
        term = TERMS[name]
        query = WINDOW + " AND (titles.title:(" + term + ") OR descriptions.description:(" + term + "))"
        capture("DISCOVERY_" + name, datacite(query))
    elif name == "CONTROL":
        capture(name, datacite(WINDOW + " AND doi:10.48550/arxiv.2509.07968"))
    elif name == "RULE2025":
        capture(name, "https://raw.githubusercontent.com/arXiv/arxiv-docs/46793211923f3e84140efe04524a250a93b2577b/source/help/availability.md")
    elif name == "GOOGLE2025_NLP":
        capture(name, "https://research.google/pubs/?category=2025&category=natural-language-processing")
    else:
        raise SystemExit("Unknown bounded capture")
