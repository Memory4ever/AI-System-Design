"""One bounded request per named primary artifact; preserve original raw fields."""
import datetime
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parent
URLS = {
    "rynn-releases": "https://api.github.com/repos/alibaba-damo-academy/RynnVLA-002/releases?per_page=10",
    "ui-releases": "https://api.github.com/repos/UiPath/uipath_enterprise_benchmark/releases?per_page=10",
    "political-releases": "https://api.github.com/repos/anthropics/political-neutrality-eval/releases?per_page=10",
    "murmur-openreview": "https://api2.openreview.net/notes?id=wwXP9eqWeW",
    "tbik-releases": "https://api.github.com/repos/nanomaoli/llm_reproducibility/releases?per_page=10",
}
for name, url in URLS.items():
    receipt = {"url": url, "executed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "stop": "one exact identity, first page only; commit dates are not public release dates"}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "HistoricalDailyResearch/1.0"})
        with urllib.request.urlopen(request, timeout=25) as response:
            raw = response.read()
            receipt["status"] = response.status
        (ROOT / (name + ".json")).write_bytes(raw)
        result = json.loads(raw)
        if isinstance(result, list):
            receipt["items"] = [{key: item.get(key) for key in
                                 ("id", "name", "tag_name", "created_at", "published_at", "html_url")}
                                for item in result]
        else:
            receipt["notes"] = result.get("notes", [])
    except Exception as error:
        receipt["error"] = repr(error)
    (ROOT / (name + "-receipt.json")).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(receipt, ensure_ascii=False), flush=True)
