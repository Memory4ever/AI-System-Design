"""Bounded Sep13 BJT discovery and exact DOI recovery; no review claims."""

import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from urllib.parse import urlencode

BASE = Path(__file__).parent
WINDOW = "registered:[2025-09-12T16:00:00Z TO 2025-09-13T15:59:59Z]"
TERMS = {
    "MODEL": '"language model" OR transformer OR "mixture of experts" OR "foundation model"',
    "SYSTEM": '("language model" OR LLM OR GPU) AND (inference OR serving OR communication OR kernel OR parallel OR compiler)',
    "AGENT": '("language model" OR LLM) AND (agent OR retrieval OR memory OR safety OR jailbreak OR "tool calling")',
    "MULTI": '"vision language" OR "vision-language-action" OR "world model" OR "video generation" OR diffusion',
}
LANGUAGE = '"language model" OR "language models" OR LLM OR LLMs'
EXPANDED = {
    "MODEL": LANGUAGE + ' OR transformer OR transformers OR "mixture of experts" OR "mixtures of experts" OR MoE OR MoEs OR "foundation model" OR "foundation models"',
    "SYSTEM": '(' + LANGUAGE + ' OR GPU OR GPUs) AND (inference OR serving OR communication OR communications OR kernel OR kernels OR parallel OR parallelism OR compiler OR compilers OR training OR pretraining)',
    "AGENT": '(' + LANGUAGE + ') AND (agent OR agents OR retrieval OR memory OR memories OR safety OR jailbreak OR jailbreaks OR "tool calling" OR "tool use" OR "tool calls")',
    "MULTI": '"vision language" OR "vision-language model" OR "vision-language models" OR VLM OR VLMs OR "vision-language-action" OR VLA OR VLAs OR "multimodal model" OR "multimodal models" OR "world model" OR "world models" OR "video generation" OR "video generator" OR "video generators" OR diffusion',
}


def capture(name, url, headers=None):
    stem = BASE / ("REPAIR_" + name + "_20261021")
    raw = Path(str(stem) + ".raw")
    response_headers = Path(str(stem) + ".headers.raw")
    request = Path(str(stem) + ".request.json")
    if any(path.exists() for path in (raw, response_headers, request)):
        raise SystemExit("Refusing to overwrite existing capture: " + name)
    checked = datetime.datetime.now(datetime.timezone.utc).isoformat()
    started = time.monotonic()
    command = [
        "curl", "--location", "--silent", "--show-error", "--max-time", "90",
        "--user-agent", "AI-System-Design/1.0", "--dump-header", str(response_headers),
        "--output", str(raw), "--write-out", "%{http_code}",
    ]
    for key, value in (headers or {}).items():
        command.extend(["--header", key + ": " + value])
    result = subprocess.run(command + [url], capture_output=True, text=True)
    body = raw.read_bytes() if raw.exists() else b""
    record = {
        "method": "GET", "url": url, "checked_utc": checked,
        "request_headers": headers or {},
        "exit_code": result.returncode, "status": result.stdout,
        "seconds": time.monotonic() - started, "bytes": len(body),
        "sha256": hashlib.sha256(body).hexdigest(), "stderr": result.stderr,
        "scope": "Sep13 BJT discovery/date only; manuscript review recorded separately",
    }
    request.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({key: record[key] for key in ("status", "exit_code", "seconds", "bytes")}), name, flush=True)


def registry(query):
    return "https://api.datacite.org/dois?" + urlencode({
        "client-id": "arxiv.content", "page[size]": 100, "query": query,
    })


if __name__ == "__main__":
    name = sys.argv[1]
    if name.startswith("EXP_") and name[4:] in EXPANDED:
        term = EXPANDED[name[4:]]
        capture("DISCOVERY_" + name, registry(WINDOW + " AND (titles.title:(" + term + ") OR descriptions.description:(" + term + "))"))
    elif name.startswith("CONTROL_EXP_") and name[12:] in EXPANDED:
        group = name[12:]
        term = EXPANDED[group]
        suffix = {"MODEL": "10369", "SYSTEM": "10371", "AGENT": "10446", "MULTI": "10441"}[group]
        control_window = "registered:[2025-09-14T16:00:00Z TO 2025-09-15T15:59:59Z]"
        capture(name, registry(control_window + " AND (titles.title:(" + term + ") OR descriptions.description:(" + term + ")) AND doi:10.48550/arxiv.2509." + suffix))
    elif name in TERMS:
        term = TERMS[name]
        capture("DISCOVERY_" + name, registry(WINDOW + " AND (titles.title:(" + term + ") OR descriptions.description:(" + term + "))"))
    elif name == "DATE_FIRST3":
        capture(name, registry(" OR ".join("doi:10.48550/arxiv." + identity for identity in ["2509.10369", "2509.10371", "2509.10613"])))
    elif name == "CONTROL":
        capture(name, registry(WINDOW + " AND doi:10.48550/arxiv.2509.10371"))
    elif name in ("POSITIVE_MODEL", "POSITIVE_SYSTEM"):
        group = name.removeprefix("POSITIVE_")
        term = TERMS[group]
        control_window = "registered:[2025-09-14T16:00:00Z TO 2025-09-15T15:59:59Z]"
        capture(name, registry(control_window + " AND (titles.title:(" + term + ") OR descriptions.description:(" + term + ")) AND doi:10.48550/arxiv.2509.10371"))
    elif name in ("POSITIVE_MODEL_10369", "POSITIVE_AGENT_10446", "POSITIVE_MULTI_10441"):
        _, group, suffix = name.split("_")
        term = TERMS[group]
        control_window = "registered:[2025-09-14T16:00:00Z TO 2025-09-15T15:59:59Z]"
        capture(name, registry(control_window + " AND (titles.title:(" + term + ") OR descriptions.description:(" + term + ")) AND doi:10.48550/arxiv.2509." + suffix))
    elif name == "POSITIVE_AGENT_10761":
        term = TERMS["AGENT"]
        control_window = "registered:[2025-09-15T16:00:00Z TO 2025-09-16T15:59:59Z]"
        capture(name, registry(control_window + " AND (titles.title:(" + term + ") OR descriptions.description:(" + term + ")) AND doi:10.48550/arxiv.2509.10761"))
    elif name == "DATE_REMAIN55":
        import re

        screen = (BASE / "SCREEN.md").read_text()
        old = [re.search(r"2509\.\d+", line).group() for line in screen.splitlines()
               if line.startswith("| [2509.") and "| 潜力；" in line]
        old = [identity for identity in old if identity not in ("2509.10651", "2509.19322")]
        old.append("2509.10860")
        added = ["2509." + suffix for suffix in (
            "10369 10371 10372 10377 10396 10401 10406 10408 10416 10417 "
            "10423 10426 10439 10441 10446 10452 10694 10784 12267").split()]
        identities = sorted(set(old + added) - {"2509.10369", "2509.10371", "2509.10613"})
        assert len(identities) == 55
        capture(name, registry(" OR ".join("doi:10.48550/arxiv." + identity for identity in identities)))
    else:
        raise SystemExit("Unknown bounded capture: " + name)
