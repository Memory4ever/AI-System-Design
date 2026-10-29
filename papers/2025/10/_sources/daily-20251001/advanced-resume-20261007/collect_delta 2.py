"""Retain identities for bounded discovery, not a full-text work queue."""

import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET


base = Path(__file__).resolve().parent
definitions = (base / "fetch_discovery.py").read_text().split("BASE =")[0]
exec(compile(definitions, str(base / "fetch_discovery.py"), "exec"))
topics = ["inference", "quantization", "posttraining", "world-model", "agent-memory", "multimodal"]
rows = {}
pages = []
for topic in topics:
    parsed = parse((base / "boundary" / (topic + ".html")).read_bytes())
    pages.append({"topic": topic, "headings": parsed["headings"], "next": parsed["next"],
                  "returned": len(parsed["rows"]), "start": 0, "last_id": parsed["rows"][-1]["id"]})
    for row in parsed["rows"]:
        rows.setdefault(row["id"], row)

tree = Tree()
tree.feed((base / "repair/cl-month-tail.html").read_text())
nodes = tree.root.find(lambda n: n.tag in {"dt", "dd"})
month = []
for index in range(0, len(nodes), 2):
    month.append({"id": re.search(r"arXiv:(\d{4}\.\d+)", nodes[index].text()).group(1),
                  "title": nodes[index + 1].find(class_has("list-title"))[0].text(),
                  "comments": [n.text() for n in nodes[index + 1].find(class_has("list-comments"))]})

ns = {"a": "http://www.w3.org/2005/Atom"}
old = set()
for topic in ["models", "systems", "multimodal", "agents"]:
    for entry in ET.parse(base.parent / "supplement-20261007" / ("arxiv-" + topic + ".raw")).getroot().findall("a:entry", ns):
        old.add(entry.find("a:id", ns).text.split("/abs/")[-1].split("v")[0])

selected_ids = ["2509.23958", "2509.24116", "2509.24418", "2509.24804", "2509.24832",
                "2509.24957", "2509.24967", "2509.25050", "2509.25175", "2509.25448",
                "2509.25598", "2509.25678", "2509.25689", "2509.25762", "2509.25911", "2509.26114"]
selected = [rows[identity] for identity in selected_ids]
for row in json.loads((base / "selected-api.parsed.json").read_text()):
    identity = row["id"].split("/abs/")[-1]
    selected.append({**row, "id": identity.split("v")[0], "abstract_version": identity})
assert len(selected) == 23 and len({r["id"] for r in selected}) == 23
assert not ({r["id"] for r in selected} & old)
union = set(rows) | {r["id"] for r in month}
result = {"pages": pages, "advanced_unique": len(rows), "month_title_rows": len(month),
          "combined_unique": len(union), "overlap_old_125": len(union & old),
          "additional_raw_ids": sorted(union - old), "advanced_title_inventory": [
              {k: row[k] for k in ["id", "title", "abstract_version", "version_fields", "comments"]}
              for row in rows.values()], "month_title_inventory": month,
          "selected_complete_abstracts": selected,
          "permission": "Discovery/abstract admission only. No public day, score, Evidence or Books adoption."}
with (base / "bounded-discovery-delta.json").open("x") as out:
    json.dump(result, out, ensure_ascii=False, indent=2)
print(json.dumps({k: result[k] for k in ["advanced_unique", "month_title_rows", "combined_unique", "overlap_old_125"]}))
print("selected versions:", [r["abstract_version"] for r in selected])
