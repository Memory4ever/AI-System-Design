"""Finite Sep10 BJT morphology discovery; preserve old field conjunctions."""

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
EDGE = "registered:[2025-09-10T15:59:59Z TO 2025-09-10T16:00:00Z}"
MODELS = '"language model" OR "language models" OR LLM OR LLMs'
TERMS = {
    "MODEL": MODELS + ' OR transformer OR transformers OR "mixture of experts" OR "mixtures of experts" OR "foundation model" OR "foundation models"',
    "SYSTEM": '(' + MODELS + ' OR GPU OR GPUs) AND (inference OR serving OR communication OR communications OR kernel OR kernels OR parallel OR parallelism OR compiler OR compilers OR compilation)',
    "AGENT": '(' + MODELS + ') AND (agent OR agents OR agentic OR retrieval OR memory OR memories OR safety OR jailbreak OR jailbreaks OR "tool calling" OR "tool use" OR "tool calls" OR tool OR tools)',
    "MULTI": '"vision language" OR "vision-language" OR "vision language models" OR "vision-language-action" OR "vision-language-actions" OR VLA OR VLAs OR "world model" OR "world models" OR "video generation" OR diffusion OR diffusions OR "diffusion model" OR "diffusion models"',
}


def clause(term):
    return "(titles.title:(" + term + ") OR descriptions.description:(" + term + "))"


def capture(name, query, page=1, url=None):
    stem = BASE / ("REPAIR_FORMS_" + name + "_20261023")
    paths = {suffix: Path(str(stem) + suffix) for suffix in (
        ".raw", ".headers.raw", ".request.json")}
    if any(path.exists() for path in paths.values()):
        raise SystemExit("Refusing overwrite/refetch: " + name)
    url = url or "https://api.datacite.org/dois?" + urlencode({
        "client-id": "arxiv.content", "page[size]": 100,
        "page[number]": page, "query": query,
    })
    started = time.monotonic()
    checked = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = subprocess.run([
        "curl", "--location", "--silent", "--show-error", "--max-time", "90",
        "--user-agent", "AI-System-Design/1.0", "--dump-header", str(paths[".headers.raw"]),
        "--output", str(paths[".raw"]), "--write-out", "%{http_code}", url,
    ], capture_output=True, text=True)
    body = paths[".raw"].read_bytes() if paths[".raw"].exists() else b""
    record = dict(method="GET", url=url, query=query, page=page,
                  checked_utc=checked, exit_code=result.returncode,
                  status=result.stdout, seconds=time.monotonic() - started,
                  bytes=len(body), sha256=hashlib.sha256(body).hexdigest(),
                  stderr=result.stderr, scope="Sep10 BJT morphology/navigation only")
    paths[".request.json"].write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({key: record[key] for key in (
        "status", "exit_code", "seconds", "bytes")}), name, flush=True)
    if result.returncode or result.stdout != "200":
        raise SystemExit("Stopped at actual failed request: " + name)
    if "api.datacite.org" not in url:
        return body
    payload = json.loads(body)
    print(json.dumps({"returned": len(payload["data"]), "meta": payload.get("meta"),
                      "next": payload.get("links", {}).get("next")}), flush=True)
    return payload


def pages(name, query):
    for page in range(1, 6):
        payload = capture(name + "_P" + str(page), query, page)
        if not payload.get("links", {}).get("next"):
            return
    raise SystemExit("Finite five-page bound reached; preserve next as ordinary work")


if __name__ == "__main__":
    name = sys.argv[1]
    if name in TERMS:
        pages(name, WINDOW + " AND " + clause(TERMS[name]))
    elif name == "EDGE":
        pages(name, EDGE + " AND (" + " OR ".join(map(clause, TERMS.values())) + ")")
    elif name == "CONTROL":
        if len(sys.argv) != 5:
            raise SystemExit("CONTROL requires label, exact DOI suffix and new-form clause")
        capture("CONTROL_" + sys.argv[2], WINDOW + " AND doi:10.48550/arxiv."
                + sys.argv[3] + " AND " + clause(sys.argv[4]))
    elif name == "PREPARED":
        print(json.dumps({"window": WINDOW, "edge": EDGE,
                          "queries": {key: clause(value) for key, value in TERMS.items()}}, indent=2))
    elif name == "ATOM":
        identities = sys.argv[3].split(",")
        if not 1 <= len(identities) <= 20:
            raise SystemExit("Only an explicit finite batch of 1-20 exact versions")
        capture("AB_" + sys.argv[2], "explicit exact-version abstract batch", url=
                "https://export.arxiv.org/api/query?" + urlencode({
                    "id_list": ",".join(identities), "max_results": len(identities)}))
    else:
        raise SystemExit("Unknown finite discovery task")
