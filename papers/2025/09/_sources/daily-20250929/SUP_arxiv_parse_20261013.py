"""Preserve current-version discovery and explanation fields for Sep28 only."""
import json
from pathlib import Path
import xml.etree.ElementTree as ET

BASE = Path(__file__).parent
NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}
output = BASE / "SUP_arxiv_discovery_20261013.json"
if output.exists():
    raise FileExistsError("Existing discovery protected")
queries = []
unique = {}
occurrences = 0
for name in ("model", "systems", "agents", "multimodal"):
    raw = BASE / f"SUP_curl-arxiv-{name}_20261013.raw"
    request = json.loads(raw.with_suffix(".request.json").read_text())
    if request.get("status") != 200 or request.get("exit_code") != 0:
        queries.append({"theme": name, "request": request, "processed": False})
        continue
    root = ET.fromstring(raw.read_bytes())
    entries = root.findall("a:entry", NS)
    queries.append({"theme": name, "request": request, "returned": len(entries),
                    "total": int(root.findtext("o:totalResults", "0", NS)), "processed": True})
    for entry in entries:
        occurrences += 1
        identity = entry.findtext("a:id", "", NS).rsplit("/", 1)[-1]
        family = identity.rsplit("v", 1)[0]
        fields = {"id": identity, "family": family, "title": entry.findtext("a:title", "", NS),
                  "summary": entry.findtext("a:summary", "", NS),
                  "published_submission": entry.findtext("a:published", "", NS),
                  "updated": entry.findtext("a:updated", "", NS),
                  "comment": entry.findtext("x:comment", "", NS),
                  "journal_ref": entry.findtext("x:journal_ref", "", NS),
                  "authors": [a.findtext("a:name", "", NS) for a in entry.findall("a:author", NS)],
                  "themes": [name]}
        if family in unique:
            unique[family]["themes"].append(name)
        else:
            unique[family] = fields
result = {"bjt_discovery_day": "2025-09-28", "permission": "Submission/current metadata; not public announcement",
          "queries": queries, "occurrences": occurrences, "unique_families": len(unique),
          "items": list(unique.values())}
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print("queries", [(q["theme"], q.get("returned"), q.get("total")) for q in queries])
print("occurrences", occurrences, "unique", len(unique))
for item in unique.values():
    print(item["id"], " ".join(item["title"].split()), "COMMENT", item["comment"], "JOURNAL", item["journal_ref"])
