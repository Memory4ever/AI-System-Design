"""Exact-identity date recovery only; no contribution or adoption decisions."""
import datetime
import hashlib
import importlib.util
import json
import re
from pathlib import Path
import sys
import urllib.error
import urllib.request

BASE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location("publication_date", ROOT / "scripts/arxiv_publication_date.py")
dates = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dates)


def capture(label, url):
    raw = BASE / ("REPAIR_" + label + "_20261023.raw")
    receipt = raw.with_suffix(".request.json")
    if raw.exists() or receipt.exists():
        raise FileExistsError(raw)
    record = {"url": url, "method": "GET", "checked_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "timeout_seconds": 30}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "AI-System-Design date recovery"})
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read()
            record.update(status=response.status, final_url=response.url)
    except urllib.error.HTTPError as error:
        body = error.read()
        record.update(status=error.code, error=str(error))
    except Exception as error:
        body = b""
        record["error"] = str(error)
    record.update(bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
    raw.write_bytes(body)
    receipt.write_text(json.dumps(record, indent=2) + "\n")
    return body, record


if __name__ == "__main__":
    identities = sys.argv[1:]
    if identities == ["--summarize"]:
        results = []
        for raw in sorted(BASE.glob("REPAIR_DATACITE_*.raw")):
            receipt = json.loads(raw.with_suffix(".request.json").read_text())
            body = raw.read_bytes()
            assert receipt["bytes"] == len(body)
            assert receipt["sha256"] == hashlib.sha256(body).hexdigest()
            record = json.loads(body, object_pairs_hook=dates._unique_keys)
            identity = raw.name.split("_")[2]
            result = dates.publication_date_envelope(record, identity)
            result["raw"] = raw.name
            result["title"] = record["data"]["attributes"].get("titles")
            result["current_comments"] = [item for item in record["data"]["attributes"].get("descriptions", []) if item.get("descriptionType") == "Other"]
            result["version_metadata"] = record["data"]["attributes"].get("dates")
            results.append(result)
        target = BASE / "REPAIR_DATE78_20261023.json"
        target.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")
        print("Saved", len(results), "mechanical envelopes; not reader adoption", flush=True)
        sys.exit(0)
    if identities == ["--remaining"]:
        text = (BASE / "FIRST_BATCH.md").read_text()
        old = set(re.findall(r"https://arxiv.org/html/(2509\.\d+)v1", text))
        old.update("2509." + value for value in re.findall(r"^\| (\d{5}) \|", text, re.M))
        old.update("2509." + value for value in ("14834", "14851", "15027", "14943", "15089"))
        new = set(re.findall(r"https://arxiv.org/abs/(2509\.\d+)v1", (BASE / "SUP_AB_20261012.md").read_text())) - {"2509.12989", "2509.13353"}
        assert len(old) == 63 and len(new) == 15 and not old & new
        identities = [value for value in sorted(old | new) if not (BASE / ("REPAIR_DATACITE_" + value + "_20261023.raw")).exists()]
    for identity in identities:
        body, receipt = capture("DATACITE_" + identity, "https://api.datacite.org/dois/10.48550/arxiv." + identity)
        result = {"arxiv_id": identity, "receipt": receipt}
        if receipt.get("status") == 200:
            try:
                result["envelope"] = dates.publication_date_envelope(json.loads(body, object_pairs_hook=dates._unique_keys), identity)
            except ValueError as error:
                result["parse_error"] = str(error)
        print(json.dumps(result), flush=True)
