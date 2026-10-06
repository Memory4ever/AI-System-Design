"""Public API metadata capture only; stdout, no local read/write."""
import datetime
import json
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

window = "submittedDate:[202601051900 TO 202601061859]"
queries = {
    "model": '(ti:"language model" OR ti:LLM OR ti:"large language" OR ti:"foundation model" OR ti:MoE OR ti:"test-time" OR ti:post-training OR ti:pretraining)',
    "system": '(all:"language model" AND (ti:inference OR ti:serving OR ti:kernel OR ti:cache OR ti:distributed OR ti:parallel))',
    "multimodal": '(ti:"vision-language" OR ti:"diffusion model" OR ti:"world model" OR ti:VLA OR ti:multimodal OR ti:"video generation")',
    "agent": '(ti:agent AND (all:"language model" OR all:LLM))',
}
ns = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}
start = 80 if sys.argv[1:] == ["model-tail"] else 0
if start:
    queries = {"model": queries["model"]}
for name, theme in queries.items():
    query = theme + " AND " + window
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": query, "start": start, "max_results": 80, "sortBy": "submittedDate", "sortOrder": "ascending"})
    record = {"name": name, "query": query, "url": url, "checked": datetime.datetime.now(datetime.timezone.utc).isoformat(), "date_use": "submission buffer for discovery, not first public event"}
    try:
        with urllib.request.urlopen(url, timeout=35) as response:
            root = ET.fromstring(response.read())
        record["total_results"] = root.findtext("o:totalResults", namespaces=ns)
        record["entries"] = [{"id": entry.findtext("a:id", namespaces=ns), "title": " ".join(entry.findtext("a:title", default="", namespaces=ns).split()), "published": entry.findtext("a:published", namespaces=ns), "updated": entry.findtext("a:updated", namespaces=ns), "categories": [c.get("term") for c in entry.findall("a:category", ns)]} for entry in root.findall("a:entry", ns)]
        record["capture"] = "metadata only; no abstracts selected or reviewed automatically"
    except Exception as error:
        record["error"] = str(error)
    print(json.dumps(record, ensure_ascii=False), flush=True)
    time.sleep(3)
