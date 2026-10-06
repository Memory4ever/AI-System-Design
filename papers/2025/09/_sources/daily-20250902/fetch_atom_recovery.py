"""Retry the failed thematic discovery with a simpler bounded Atom query."""

import datetime
import json
from pathlib import Path
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

root = Path(__file__).parent
query = '(cat:cs.CL OR cat:cs.LG OR cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:transformer OR all:"LLM" OR all:"foundation model") AND submittedDate:[202508291800 TO 202509011800]'
url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": query, "start": 0, "max_results": 200, "sortBy": "submittedDate", "sortOrder": "ascending"})
meta = {"url": url, "query": query, "checked": datetime.datetime.now(datetime.timezone.utc).isoformat(), "role": "submission discovery, not first-public evidence"}
try:
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "ResearchReview/1.0"}), timeout=30) as response:
        raw = response.read()
        meta.update(status=response.status, bytes=len(raw), final_url=response.url)
        (root / "language-recovery.atom").write_bytes(raw)
    tree = ET.fromstring(raw)
    ns = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}
    meta["total"] = tree.findtext("o:totalResults", namespaces=ns)
    entries = [{key: " ".join(item.findtext("a:" + key, default="", namespaces=ns).split()) for key in ("id", "title", "summary", "published", "updated")} for item in tree.findall("a:entry", ns)]
    (root / "language-recovery.json").write_text(json.dumps({"request": meta, "entries": entries}, ensure_ascii=False, indent=2))
except Exception as error:
    meta["error"] = str(error)
(root / "language-recovery.request.json").write_text(json.dumps(meta, indent=2))
print(json.dumps(meta), flush=True)
