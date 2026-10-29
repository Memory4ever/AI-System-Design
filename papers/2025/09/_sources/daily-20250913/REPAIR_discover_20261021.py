"""Fresh Sep12 BJT registered-theme discovery; results are not review decisions."""
import json
import importlib.util
import sys
import urllib.parse

from REPAIR_dates_20261021 import BASE, ROOT, capture


def text(terms):
    return "(titles.title:(" + terms + ") OR descriptions.description:(" + terms + "))"


lm = text('"language model" OR "language models" OR LLM OR transformer OR "mixture of experts"')
THEMES = {
    "MODEL": lm + " AND " + text("architecture OR attention OR optimizer OR training OR alignment OR quantization"),
    "SYSTEM": text('"language model" OR LLM OR GPU') + " AND " + text("inference OR communication OR kernel OR serving OR parallel OR training"),
    "MULTI": text('"foundation model" OR "world model" OR "vision language" OR "vision-language" OR "vision-language-action" OR multimodal OR VLA') + " AND " + text("representation OR generation OR diffusion OR flow OR action OR training OR fusion"),
    "AGENT": text('"language model" OR LLM OR agent') + " AND " + text("agent OR retrieval OR memory OR safety OR jailbreak OR planning"),
    "LM": text('LM OR "language models"') + " AND " + text("training OR reinforcement OR confidence OR calibration OR alignment"),
    "VLM": text('VLM OR MLLM OR "vision-language" OR "vision-language models"') + " AND " + text("representation OR evaluation OR reasoning OR navigation OR action OR fusion"),
}
THEMES["CONTROL"] = THEMES["MODEL"] + ' AND doi:"10.48550/arxiv.2509.09629"'


for name in sys.argv[1:] or THEMES:
    params = {"client-id": "arxiv.content", "query": THEMES[name] + ' AND registered:[2025-09-11T16:00:00Z TO 2025-09-12T15:59:59.999Z]', "page[size]": 100, "sort": "registered"}
    url = "https://api.datacite.org/dois?" + urllib.parse.urlencode(params)
    body, record = capture("DISCOVER-" + name, url)
    payload = json.loads(body)
    print(name, record.get("status"), "returned", len(payload.get("data", [])), "total", payload.get("meta", {}).get("total"), "next", payload.get("links", {}).get("next"), flush=True)

spec = importlib.util.spec_from_file_location("arxiv_date", ROOT / "scripts/arxiv_publication_date.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
rows = {}
for path in sorted(BASE.glob("REPAIR_DISCOVER-*_20261021.raw")):
    if "CONTROL" in path.name:
        continue
    payload = json.loads(path.read_text())
    assert len(payload["data"]) == payload["meta"]["total"] and not payload.get("links", {}).get("next")
    for resource in payload["data"]:
        key = resource["id"].lower().split("arxiv.")[-1]
        if key not in rows:
            rows[key] = {"id": key, "resource": resource, "themes": [], "date_result": module.publication_date_envelope(resource, key)}
        rows[key]["themes"].append(path.name)
target = BASE / "REPAIR_discovery_20261021.json"
encoded = (json.dumps(list(sorted(rows.values(), key=lambda row: row["id"])), ensure_ascii=False, indent=2) + "\n").encode()
if target.exists():
    assert target.read_bytes() == encoded
else:
    with target.open("xb") as handle:
        handle.write(encoded)
print("fresh_discovery_union", len(rows), flush=True)
