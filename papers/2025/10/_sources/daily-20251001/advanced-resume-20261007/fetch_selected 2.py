import datetime
import json
from pathlib import Path
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


base = Path(__file__).resolve().parent
ids = ["2509.23962", "2509.24203", "2509.24269", "2509.24393",
       "2509.25133", "2509.25624", "2509.26354"]
url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({
    "id_list": ",".join(ids), "start": 0, "max_results": len(ids)})
record = {"url": url, "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "ids": ids, "stop": "seven named month-list leads; no expansion"}
try:
    with urllib.request.urlopen(url, timeout=30) as response:
        raw = response.read()
        record.update({"status": response.status, "headers": dict(response.headers.items()),
                       "final_url": response.url, "bytes": len(raw)})
    with (base / "selected-api.xml").open("xb") as out:
        out.write(raw)
    ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
    rows = []
    for entry in ET.fromstring(raw).findall("a:entry", ns):
        rows.append({name: " ".join(entry.findtext(tag, default="", namespaces=ns).split())
                     for name, tag in {"id": "a:id", "title": "a:title", "abstract": "a:summary",
                                       "published_submission": "a:published", "updated_submission": "a:updated",
                                       "comment": "x:comment"}.items()})
    with (base / "selected-api.parsed.json").open("x") as out:
        json.dump(rows, out, ensure_ascii=False, indent=2)
    print(json.dumps(rows, ensure_ascii=False, indent=2))
except Exception as error:
    record["error"] = repr(error)
    print(record["error"])
record["finished_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
with (base / "selected-api.request.json").open("x") as out:
    json.dump(record, out, ensure_ascii=False, indent=2)
