"""Persist this day's bounded discovery identities, not public-date admission."""
import json
import re
from pathlib import Path
import xml.etree.ElementTree as E

BASE = Path(__file__).parent
NS = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/",
      "x": "http://arxiv.org/schemas/atom"}
items = {}
for theme in ("model", "systems", "agents", "multimodal"):
    root = E.fromstring((BASE / ("SUP_arxiv-" + theme + "_20261012.raw")).read_bytes())
    entries = root.findall("a:entry", NS)
    print(theme, root.findtext("o:totalResults", namespaces=NS), len(entries))
    for entry in entries:
        identity = entry.findtext("a:id", namespaces=NS)
        item = {field: " ".join((entry.findtext(tag, namespaces=NS) or "").split())
                for field, tag in (("id", "a:id"), ("title", "a:title"), ("summary", "a:summary"),
                                  ("submitted", "a:published"), ("updated", "a:updated"),
                                  ("comment", "x:comment"), ("journal", "x:journal_ref"), ("doi", "x:doi"))}
        item["links"] = [link.attrib for link in entry.findall("a:link", NS)]
        item["categories"] = [category.get("term") for category in entry.findall("a:category", NS)]
        items[re.sub(r"v\d+$", "", identity.rsplit("/", 1)[-1])] = item
result = [items[key] for key in sorted(items)]
(BASE / "SUP_atoms_20261012.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print("unique", len(result))
for index, item in enumerate(result):
    print(index, item["id"], item["title"])
