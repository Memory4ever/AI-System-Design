"""Capture exact-version metadata and current notices for scoped P/N, not Methods."""
import json
import sys
import urllib.parse

from REPAIR_dates_20261021 import BASE, capture


EX = {2,4,6,8,12,16,21,22,24,32,33,36,38,43,45,47,49,53,54,56,57,61,62,64,65,68,69,74,79,84,86,89,91,94,101}
NEW = set(range(95)) | {98,101,102}
items = json.loads((BASE / "REPAIR_discovery_20261021.json").read_text())
selected = [row["id"] for index, row in enumerate(items) if index in NEW - EX]
assert len(selected) == 63
if sys.argv[1] == "current":
    for key in selected:
        body, record = capture("abs-" + key, "https://arxiv.org/abs/" + key)
        print(key, record.get("status"), len(body), flush=True)
elif sys.argv[1] == "exact":
    for index in range(0, len(selected), 20):
        batch = selected[index:index + 20]
        params = {"id_list": ",".join(key + "v1" for key in batch), "max_results": len(batch)}
        body, record = capture("EXACT-NEW-" + str(index // 20 + 1), "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params))
        print(index, record.get("status"), len(body), flush=True)
