"""Sep08 DataCite plural-form delta; preserve the four original field combinations."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from urllib.parse import parse_qs, urlencode, urlsplit

BASE = Path(__file__).parent
WINDOW = "registered:[2025-09-07T16:00:00Z TO 2025-09-08T15:59:59Z]"
MODEL = '"language model" OR "language models" OR transformer OR transformers OR "mixture of experts" OR "mixtures of experts" OR "foundation model" OR "foundation models"'
TERMS = {
    "MODEL": "titles.title:(" + MODEL + ") OR descriptions.description:(" + MODEL + ")",
    "SYSTEM": 'titles.title:(inference OR GPU OR GPUs OR kernel OR kernels OR "KV cache" OR "KV caches" OR "distributed training") OR descriptions.description:("large language" AND (inference OR GPU OR GPUs OR kernel OR kernels OR scheduling OR parallel))',
    "AGENT": 'titles.title:(agent OR agents OR RAG OR "retrieval augmented" OR reasoning) OR descriptions.description:(("language model" OR "language models") AND (agent OR agents OR retrieval OR memory OR memories OR reasoning))',
    "MULTI": 'titles.title:(multimodal OR "vision language" OR diffusion OR "world model" OR "world models" OR "vision language action") OR descriptions.description:(("foundation model" OR "foundation models") AND (vision OR video OR videos OR speech OR robot OR robots))',
}
CONTROLS = {"MODEL": "04576", "SYSTEM": "04576", "AGENT": "04876", "MULTI": "04996"}
ALIASES = {
    "MODEL": "LLM OR LLMs OR MoE OR MoEs",
    "MULTI": 'VLM OR VLMs OR VLA OR VLAs OR "vision-language" OR "vision-language model" OR "vision-language models" OR "vision language model" OR "vision language models" OR "vision-language-action"',
}


def capture(name, url, original_query, query, scope=None, suffix=".raw.json"):
    stem = BASE / ("REPAIR_STEM_" + name + "_20261021")
    raw = Path(str(stem) + suffix)
    headers = stem.with_suffix(".headers.raw")
    request = stem.with_suffix(".request.json")
    if any(p.exists() for p in (raw, headers, request)):
        raise SystemExit("Refusing to overwrite " + name)
    checked = datetime.datetime.now(datetime.timezone.utc).isoformat()
    started = time.monotonic()
    result = subprocess.run([
        "curl", "--location", "--silent", "--show-error", "--max-time", "90",
        "--user-agent", "AI-System-Design/1.0", "--dump-header", str(headers),
        "--output", str(raw), "--write-out", "%{http_code}", url,
    ], capture_output=True, text=True)
    body = raw.read_bytes() if raw.exists() else b""
    record = {
        "method": "GET", "url": url, "checked_utc": checked,
        "original_query": original_query, "query": query,
        "scope": scope or "Sep08 BJT plural forms only; original title/description Boolean structure retained",
        "status": result.stdout, "exit_code": result.returncode,
        "seconds": time.monotonic() - started, "bytes": len(body),
        "sha256": hashlib.sha256(body).hexdigest(), "stderr": result.stderr,
    }
    request.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(name, json.dumps({k: record[k] for k in ("status", "exit_code", "bytes", "seconds")}), flush=True)


if __name__ == "__main__":
    for mode in sys.argv[1:]:
        control = mode.startswith("CONTROL_")
        name = mode.removeprefix("CONTROL_") if control else mode
        alias = name.startswith("ALIAS_")
        group = name.removeprefix("ALIAS_") if alias else name
        old = json.loads((BASE / ("REPAIR_DISCOVERY_" + group + "_20261019.raw.json")).read_text())
        original = parse_qs(urlsplit(old["links"]["self"]).query)["query"][0]
        assert original.startswith(WINDOW + " AND (")
        terms = TERMS[group]
        scope = None
        if alias:
            terms = "titles.title:(" + ALIASES[group] + ") OR descriptions.description:(" + ALIASES[group] + ")"
            scope = "Sep08 BJT bounded MODEL/MULTI alias complement; not attributed to plural-form-only repair"
        query = WINDOW + " AND (" + terms + ")"
        if control:
            query += " AND doi:10.48550/arxiv.2509." + CONTROLS[group]
        url = "https://api.datacite.org/dois?" + urlencode({
            "client-id": "arxiv.content", "page[size]": 200, "query": query,
        })
        capture(mode, url, original, query, scope=scope)
