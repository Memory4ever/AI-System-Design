import json
import sys

from SUP_CAPTURE import ROOT

old = json.loads((ROOT / "arxiv-query-entries.json").read_text())
old += json.loads((ROOT / "month-v1-title-abstract.json").read_text())
keys = {x["id"].split("/")[-1].split("v")[0]: x for x in old}
rows = json.loads((ROOT / "SUP_DISCOVERY.json").read_text())
new = [dict(x, index=i) for i, x in enumerate(rows)
       if x["id"].split("/")[-1].split("v")[0] not in keys]
(ROOT / "SUP_NEW_DISCOVERY.json").write_text(json.dumps(new, ensure_ascii=False, indent=2) + "\n")
print("New", len(new), "identity reuse", len(rows) - len(new))
for x in new[int(sys.argv[1]):int(sys.argv[2])]:
    print(x["index"], x["id"], x["title"], "\n", x["summary"], "\n")
