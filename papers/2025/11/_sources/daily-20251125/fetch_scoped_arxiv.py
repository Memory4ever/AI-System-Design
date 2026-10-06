"""Retrieve bounded discovery queries; submission fields are not public dates."""
import datetime
import json
from pathlib import Path
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
NS = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}
DATE = 'submittedDate:[202511201900 TO 202511211900]'
QUERIES = {
    "model": '(cat:cs.CL OR cat:cs.LG) AND (ti:"language model" OR ti:transformer OR ti:MoE OR ti:attention OR ti:quantization OR ti:distillation OR ti:pretraining OR ti:"reinforcement learning")',
    "systems": '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:"language model" OR all:LLM OR all:GPU OR all:transformer)',
    "agents": '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (ti:agent OR ti:"language model" OR ti:retrieval OR ti:reasoning)',
    "multimodal": '(cat:cs.CV OR cat:cs.RO) AND (ti:"vision language" OR ti:multimodal OR ti:"world model" OR ti:VLA OR ti:diffusion OR ti:"foundation model")',
}
for name, theme in QUERIES.items():
    query = DATE + ' AND ' + theme
    args = {"search_query": query, "start": 0, "max_results": 100,
            "sortBy": "submittedDate", "sortOrder": "descending"}
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(args)
    event = {"query": query, "url": url, "requested": args,
             "executed_at": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(url, timeout=40) as response:
            raw = response.read()
        (ROOT / ("arxiv-" + name + "-page0.xml")).write_bytes(raw)
        feed = ET.fromstring(raw)
        event["returned_query"] = feed.findtext("a:title", namespaces=NS)
        event["total"] = int(feed.findtext("o:totalResults", namespaces=NS))
        event["start"] = int(feed.findtext("o:startIndex", namespaces=NS))
        entries = []
        for e in feed.findall("a:entry", NS):
            item = {key: e.findtext("a:" + key, namespaces=NS) for key in ("id", "title", "summary", "published", "updated")}
            item["categories"] = [c.attrib["term"] for c in e.findall("a:category", NS)]
            entries.append(item)
        event["entries"] = entries
        event["stop"] = "all returned" if len(entries) >= event["total"] else "page 0 only; further pagination ordinary pending"
    except Exception as error:
        event["error"] = repr(error)
    (ROOT / ("arxiv-" + name + "-query.json")).write_text(json.dumps(event, ensure_ascii=False, indent=2) + "\n")
    print(name, "total", event.get("total"), "stop", event.get("stop"), "error", event.get("error"), flush=True)
    for item in event.get("entries", []):
        print(item["id"], item["published"], " ".join(item["title"].split()), flush=True)
    time.sleep(3)
