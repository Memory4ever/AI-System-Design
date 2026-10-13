import json
import sys

from SUP_CAPTURE import ROOT

def key(value):
    return value.rsplit("/", 1)[-1].split("v")[0]

old = json.loads((ROOT / "arxiv-query-entries.json").read_text())
old += json.loads((ROOT / "month-v1-title-abstract.json").read_text())
ab = json.loads((ROOT / "arxiv-related-selection.json").read_text())
ab += json.loads((ROOT / "month-v1-title-abstract.json").read_text())
old_ids = {key(x["id"]) for x in old}
ab_ids = {key(x["id"]) for x in ab}
rows = [x for x in json.loads((ROOT / "SUP_DISCOVERY.json").read_text())
        if key(x["id"]) in old_ids and key(x["id"]) not in ab_ids]
(ROOT / "SUP_OLD_TITLE_ONLY.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")
print("TITLE_ONLY", len(rows))
for x in rows[int(sys.argv[1]):int(sys.argv[2])]:
    print(x["id"], x["title"], "\n", x["summary"], "\n")
