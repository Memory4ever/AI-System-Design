"""Save finite topic discovery responses, not public-date or review judgments."""

import datetime
import json
from pathlib import Path
import sys
import urllib.parse
import urllib.request

out = Path(sys.argv[1])
date_range = sys.argv[2]
anchor = '(all:"language model" OR all:LLM OR all:"foundation model")'
queries = {
    "model-narrow": '(cat:cs.CL OR cat:cs.LG) AND (' + anchor +
    ' AND (all:transformer OR all:attention OR all:tokenizer OR all:embedding '
    'OR all:optimization OR all:pretraining OR all:unlearning) '
    'OR all:"sparse autoencoder" OR ti:SAE OR ti:SAEs OR all:"next-token")',
    "systems-narrow": '(cat:cs.DC OR cat:cs.LG OR cat:cs.PF OR cat:cs.AR '
    'OR cat:cs.PL OR cat:cs.OS) AND (' + anchor +
    ' AND (all:inference OR all:training OR all:cache OR all:parallel '
    'OR all:routing OR all:communication OR all:kernel) '
    'OR all:GPU AND (all:"model training" OR all:"model inference"))',
    "agents-narrow": '(cat:cs.CL OR cat:cs.AI OR cat:cs.IR OR cat:cs.LG '
    'OR cat:cs.MA) AND ' + anchor +
    ' AND (all:agent OR all:memory OR all:reasoning OR all:"tool use" '
    'OR all:"tool calling" OR all:"retrieval augmented" '
    'OR all:"reinforcement learning" OR all:reward)',
    "multimodal-narrow": '(cat:cs.CV OR cat:cs.RO OR cat:cs.LG OR cat:cs.CL) '
    'AND (all:"multimodal language model" OR all:"vision language model" '
    'OR all:MLLM OR all:"foundation model" OR all:"world model" '
    'OR all:"vision language action" OR all:VLA '
    'OR (all:diffusion OR all:"flow matching") AND (all:"image generation" '
    'OR all:"video generation" OR all:"language model" OR all:"generative model"))',
}
out.mkdir(parents=True, exist_ok=True)
for name, topic in queries.items():
    query = topic + " AND submittedDate:[" + date_range + "]"
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({
        "search_query": query, "start": 0, "max_results": 100,
        "sortBy": "submittedDate", "sortOrder": "ascending"})
    meta = {"url": url, "query": query, "start": 0, "max_results": 100,
            "checked": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            raw = response.read()
            meta.update(status=response.status, bytes=len(raw))
            (out / (name + ".xml")).write_bytes(raw)
    except Exception as error:
        meta["error"] = str(error)
    (out / (name + ".request.json")).write_text(json.dumps(meta, indent=2))
    print(name, meta.get("status"), meta.get("bytes"), meta.get("error"), flush=True)
