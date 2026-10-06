"""Bounded raw retrieval for this day's named identities and native RSS."""
import datetime
from email.utils import parsedate_to_datetime
import json
from pathlib import Path
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
START = datetime.datetime.fromisoformat("2025-11-24T01:00:00+00:00")
END = datetime.datetime.fromisoformat("2025-11-25T01:00:00+00:00")
URLS = {"openai-rss": "https://openai.com/news/rss.xml"}
for identity in ("2511.17473", "2511.16947", "2511.17131", "2511.17671", "2511.17502"):
    URLS["date-" + identity] = "https://api.datacite.org/dois/10.48550/arXiv." + identity
for name, url in URLS.items():
    receipt = {"url": url, "executed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "pagination": "single named record or native feed; no recursive requests"}
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "HistoricalDailyResearch/1.0"})
        with urllib.request.urlopen(req, timeout=30) as response:
            raw = response.read()
            receipt["http_status"] = response.status
        ext = ".xml" if name == "openai-rss" else ".json"
        (ROOT / (name + ext)).write_bytes(raw)
        if name == "openai-rss":
            items = ET.fromstring(raw).findall(".//item")
            receipt["total_feed_items"] = len(items)
            receipt["neighbors"] = []
            for item in items:
                date = item.findtext("pubDate", "")
                instant = parsedate_to_datetime(date)
                if START - datetime.timedelta(days=1) <= instant < END + datetime.timedelta(days=1):
                    receipt["neighbors"].append({"title": item.findtext("title"), "url": item.findtext("link"),
                                                "pubDate": date, "in_window": START <= instant < END})
        else:
            data = json.loads(raw)["data"]["attributes"]
            receipt["dates"] = data.get("dates")
            receipt["created"] = data.get("created")
            receipt["registered"] = data.get("registered")
            receipt["updated"] = data.get("updated")
            receipt["descriptions"] = data.get("descriptions")
        receipt["stop"] = "raw saved; submission/metadata fields are not first-public claims"
    except Exception as error:
        receipt["error"] = repr(error)
        receipt["stop"] = "one attempt failed; use another verified primary identity route only"
    (ROOT / (name + "-receipt.json")).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v for k, v in receipt.items() if k != "descriptions"}, ensure_ascii=False), flush=True)
