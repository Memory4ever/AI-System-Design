"""Parse only this day's immutable official recovery responses."""
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

BASE = Path(__file__).parent
NS = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}
with_tail = "--with-tail" in sys.argv
output = BASE / ("SUP_arxiv_with_tail_20261013.json" if with_tail else "SUP_arxiv_recovery_20261013.json")
if output.exists():
    raise FileExistsError(output)
old = set()
for name in ("arxiv-narrow12-items.json", "arxiv-narrow12-tail-items.json"):
    data = json.loads((BASE / name).read_text())
    for item in data["items"] if isinstance(data, dict) else data:
        old.add(re.sub(r"v\d+$", "", item["id"].rsplit("/", 1)[-1]))
queries = []
items = {}
captures = list(BASE.glob("SUP_curl-arxiv-*-official-recovery_20261013.raw"))
if with_tail:
    captures.extend(BASE.glob("SUP_curl-arxiv-*-bounded-tail_20261013.raw"))
for raw in sorted(captures):
    receipt = json.loads(raw.with_suffix(".request.json").read_text())
    if receipt.get("status") != 200 or receipt.get("exit_code") != 0:
        queries.append({"request": raw.with_suffix(".request.json").name, "valid_atom": False})
        continue
    root = ET.fromstring(raw.read_bytes())
    entries = root.findall("a:entry", NS)
    queries.append({"request": raw.with_suffix(".request.json").name,
                    "total": root.findtext("o:totalResults", namespaces=NS),
                    "returned": len(entries), "start": root.findtext("o:startIndex", namespaces=NS)})
    for entry in entries:
        url = entry.findtext("a:id", namespaces=NS)
        identity = re.sub(r"v\d+$", "", url.rsplit("/", 1)[-1])
        record = items.setdefault(identity, {
            "id": identity, "version_url": url,
            "title": " ".join(entry.findtext("a:title", namespaces=NS).split()),
            "abstract": " ".join(entry.findtext("a:summary", namespaces=NS).split()),
            "published_submission": entry.findtext("a:published", namespaces=NS),
            "updated": entry.findtext("a:updated", namespaces=NS),
            "categories": [x.get("term") for x in entry.findall("a:category", NS)],
            "authors": [x.findtext("a:name", namespaces=NS) for x in entry.findall("a:author", NS)],
            "in_old_discovery": identity in old, "queries": []})
        record["queries"].append(raw.name)
result = {"purpose": "Sep26 BJT submitted discovery only; not public-day proof",
          "queries": queries, "unique": len(items),
          "overlap_with_old_discovery": sum(x["in_old_discovery"] for x in items.values()),
          "items": list(items.values())}
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items() if k != "items"}, indent=2))
