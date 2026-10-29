"""Bounded downloads for this day's named materials; no semantic screening."""
import concurrent.futures
import json
from pathlib import Path
import sys
import urllib.request

ROOT = Path(__file__).resolve().parent
def fetch(task):
    name, url = task
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "DailyResearch/1.0"}), timeout=25) as response:
            data = response.read()
        (ROOT / name).write_bytes(data)
        return {"name": name, "url": url, "bytes": len(data), "error": None}
    except Exception as error:
        return {"name": name, "url": url, "bytes": 0, "error": str(error)}

if __name__ == "__main__":
    ids = sys.argv[2:]
    mode = sys.argv[1]
    tasks = [(f"datacite-{item}.raw.json", f"https://api.datacite.org/dois/10.48550/arxiv.2610.{item}") if mode == "date" else (f"core-{item}v1.raw.html", f"https://arxiv.org/html/2610.{item}v1") for item in ids]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(fetch, tasks))
    print(json.dumps(results, indent=2))
