"""Capture this day's already-screened potential families, not the NAV union."""
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

BASE = Path(__file__).parent
ROOT = BASE.parents[4]
NS = {"a": "http://www.w3.org/2005/Atom"}
NEW_P = [0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,22,23,24,25,26,31,32,33,34,36,37,39,41,43,44,45,46,48,49,51,52,53,54,55,57,58,59,60,61,63,67,68,71,73,76,78,80,82,83,84,86,87,88]
OLD_EX = {"2511.11572", "2509.09869", "2509.09918", "2509.21336", "2509.10000", "2509.10147", "2509.10284", "2509.10289", "2509.10366", "2509.09810", "2509.10345"}
OLD_REOPEN = {"2509.09792", "2509.09852", "2509.09977", "2509.10010", "2509.10059", "2509.10127", "2509.10184", "2509.10259", "2509.10426"}


def identity(value):
    return re.search(r"\d{4}\.\d{4,5}", value).group()


def save(path, body):
    with path.open("xb") as handle:
        handle.write(body)


def capture(name, url, purpose="2025-09-12 BJT; finite same-day potential family date/signal recovery"):
    target = BASE / ("REPAIR_" + name + "_20261021.raw")
    record_path = target.with_suffix(".request.json")
    if target.exists() and record_path.exists():
        body = target.read_bytes()
        record = json.loads(record_path.read_text())
        assert len(body) == record["bytes"] and hashlib.sha256(body).hexdigest() == record["sha256"]
        return body, record
    record = {"url": url, "method": "GET", "checked_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "timeout_seconds": 30, "purpose": purpose}
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30) as response:
            body = response.read()
            record.update(status=response.status, final_url=response.url)
    except urllib.error.HTTPError as error:
        body = error.read()
        record.update(status=error.code, error=str(error))
    except Exception as error:
        body = b""
        record["error"] = str(error)
    record.update(bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
    save(target, body)
    save(record_path, (json.dumps(record, ensure_ascii=False, indent=2) + "\n").encode())
    return body, record


def manifest():
    entries = ET.parse(BASE / "SUP_exact-v1_20261012.raw").findall("a:entry", NS)
    old = json.loads((BASE / "scoped-abstracts.json").read_text())
    old_p = {identity(item["id"]): item for item in old if identity(item["id"]) not in OLD_EX}
    original = ET.parse(BASE / "arxiv-api.raw").findall("a:entry", NS)
    for item in original:
        key = identity(item.findtext("a:id", namespaces=NS))
        if key in OLD_REOPEN:
            old_p[key] = {"id": key, "title": item.findtext("a:title", namespaces=NS)}
    assert len(old_p) == 67
    output = {}
    for index in NEW_P:
        item = entries[index]
        key = identity(item.findtext("a:id", namespaces=NS))
        output[key] = {"id": key, "title": " ".join(item.findtext("a:title", namespaces=NS).split()), "new_p_index": index, "exact_v1_submitted": item.findtext("a:published", namespaces=NS), "old_p": key in old_p}
    for key, item in old_p.items():
        if key not in output:
            output[key] = {"id": key, "title": " ".join(item["title"].split()), "new_p_index": None, "old_p": True}
    return sorted(output.values(), key=lambda item: item["id"])


def main():
    spec = importlib.util.spec_from_file_location("arxiv_date", ROOT / "scripts/arxiv_publication_date.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    items = manifest()
    print("finite_P_union", len(items), "new", len(NEW_P), "old", sum(item["old_p"] for item in items), flush=True)
    for item in items:
        body, record = capture("datacite-" + item["id"], "https://api.datacite.org/dois/10.48550/arXiv." + item["id"])
        try:
            result = module.publication_date_envelope(json.loads(body), item["id"])
        except (ValueError, TypeError) as error:
            result = {"status": "unresolved", "error": str(error)}
        item.update(date_result=result, request=record)
        print(item["id"], record.get("status"), result.get("bounded_bjt_date"), result.get("reasons"), flush=True)
    target = BASE / "REPAIR_P_dates_20261021.json"
    payload = (json.dumps(items, ensure_ascii=False, indent=2) + "\n").encode()
    if target.exists():
        assert target.read_bytes() == payload
    else:
        save(target, payload)


if __name__ == "__main__":
    main()
