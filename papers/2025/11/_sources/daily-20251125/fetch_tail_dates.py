"""One named metadata request per tail identity; no public-date inference."""
import datetime
import json
from pathlib import Path
import urllib.request

root = Path(__file__).resolve().parent
for identity in ("2511.17235", "2511.17127", "2511.16964", "2511.19457"):
    url = "https://api.datacite.org/dois/10.48550/arXiv." + identity
    receipt = {"url": url, "executed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "stop": "one exact identity, no pagination; metadata is not first-public lower bound"}
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "HistoricalDailyResearch/1.0"})
        with urllib.request.urlopen(req, timeout=25) as response:
            raw = response.read()
            receipt["status"] = response.status
        (root / ("date-" + identity + ".json")).write_bytes(raw)
        fields = json.loads(raw)["data"]["attributes"]
        receipt.update({key: fields.get(key) for key in ("dates", "created", "registered", "updated")})
    except Exception as error:
        receipt["error"] = repr(error)
    (root / ("date-" + identity + "-receipt.json")).write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(receipt, ensure_ascii=False), flush=True)
