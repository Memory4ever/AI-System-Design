"""Finish the finite language query and recover two bounded system slices."""

import datetime
import json
from pathlib import Path
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

root = Path(__file__).parent
base = '(cat:cs.CL OR cat:cs.LG OR cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:transformer OR all:"LLM" OR all:"foundation model")'
queries = {
    "language-tail": (base, 200),
    "systems-recovery": ('(cat:cs.DC OR cat:cs.PF OR cat:cs.AR OR cat:cs.LG) AND (all:GPU OR all:inference OR all:distributed OR all:compiler) AND (all:"language model" OR all:LLM OR all:transformer OR all:"foundation model")', 0),
    "multimodal-recovery": ('(cat:cs.CV OR cat:cs.RO OR cat:cs.SD OR cat:cs.AI) AND (all:"vision language" OR all:"world model" OR all:"foundation model" OR all:"diffusion transformer" OR all:"vision-language-action" OR all:"multimodal large")', 0),
}
ns = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}
for name, (scope, start) in queries.items():
    query = scope + ' AND submittedDate:[202508291800 TO 202509011800]'
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": query, "start": start, "max_results": 200, "sortBy": "submittedDate", "sortOrder": "ascending"})
    meta = {"url": url, "query": query, "start": start, "checked": datetime.datetime.now(datetime.timezone.utc).isoformat(), "role": "submission discovery, not first-public evidence"}
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "ResearchReview/1.0"}), timeout=30) as response:
            raw = response.read()
            meta.update(status=response.status, bytes=len(raw), final_url=response.url)
            (root / (name + ".atom")).write_bytes(raw)
        tree = ET.fromstring(raw)
        meta["total"] = tree.findtext("o:totalResults", namespaces=ns)
        entries = [{key: " ".join(item.findtext("a:" + key, default="", namespaces=ns).split()) for key in ("id", "title", "summary", "published", "updated")} for item in tree.findall("a:entry", ns)]
        (root / (name + ".json")).write_text(json.dumps({"request": meta, "entries": entries}, ensure_ascii=False, indent=2))
        meta["returned"] = len(entries)
    except Exception as error:
        meta["error"] = str(error)
    (root / (name + ".request.json")).write_text(json.dumps(meta, indent=2))
    print(json.dumps(meta), flush=True)
