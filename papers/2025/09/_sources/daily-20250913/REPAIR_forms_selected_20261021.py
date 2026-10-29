"""Only new P/N exact metadata and notices after morphology-delta calibration."""
import json
import sys
import urllib.parse

from REPAIR_dates_20261021 import BASE, capture


items = json.loads((BASE / "REPAIR_forms_delta_calibrated_20261021.json").read_text())["rows"]
selected = [row["id"] for row in items if row.get("initial_gate") in ("P", "N")]
assert len(selected) == 18
if sys.argv[1] == "exact":
    params = {"id_list": ",".join(key + "v1" for key in selected), "max_results": len(selected)}
    body, record = capture("FORMS-EXACT-PN", "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params))
    print(record, flush=True)
elif sys.argv[1] == "current":
    for key in selected:
        body, record = capture("FORMS-ABS-" + key, "https://arxiv.org/abs/" + key)
        print(key, record.get("status"), len(body), flush=True)
