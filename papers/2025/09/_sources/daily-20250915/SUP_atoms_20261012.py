"""Compare bounded Sep14 discovery fields with this day's prior abstracts."""
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as E

BASE = Path(__file__).parent
NS = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/", "x": "http://arxiv.org/schemas/atom"}


def identity(url):
    return re.search(r"\d{4}\.\d{4,5}", url).group()


def normalize(value):
    return " ".join((value or "").split())


def load():
    rows = {}
    for theme in ("model", "systems", "agents", "multimodal"):
        root = E.parse(BASE / ("SUP_arxiv-" + theme + "_20261012.raw")).getroot()
        entries = root.findall("a:entry", NS)
        print(theme, "total", root.findtext("o:totalResults", namespaces=NS), "returned", len(entries))
        for entry in entries:
            row = {field: normalize(entry.findtext("a:" + field, namespaces=NS)) for field in ("id", "title", "summary", "published", "updated")}
            row["comment"] = normalize(entry.findtext("x:comment", namespaces=NS))
            row["journal_ref"] = normalize(entry.findtext("x:journal_ref", namespaces=NS))
            key = identity(row["id"])
            if key not in rows:
                rows[key] = row
    old = {identity(r["id"]): r for r in json.loads((BASE / "scoped-abstracts.json").read_text())}
    result = []
    for key, row in sorted(rows.items()):
        row["identity"] = key
        prior = old.get(key)
        row["prior_state"] = "new" if prior is None else "same" if all(normalize(prior.get(f)) == row[f] for f in ("id", "title", "summary")) else "changed"
        row["prior_id"] = prior["id"] if prior else None
        result.append(row)
    return result


if __name__ == "__main__":
    rows = load()
    if sys.argv[1] == "save":
        (BASE / "SUP_atoms_20261012.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")
    else:
        lo, hi = map(int, sys.argv[1].split("-"))
        for i, row in enumerate(rows[lo:hi + 1], lo):
            print(i, row["identity"], row["prior_state"], row["id"], "submitted", row["published"])
            print(row["title"])
            print(row["summary"])
            print("comment:", row["comment"], "journal:", row["journal_ref"])
