"""Recover only explicitly named exact-version primary abstracts."""

import json
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from inspect_raw import TextParser

root = Path(__file__).parent
records = []
for identity in sys.argv[1:]:
    url = f"https://arxiv.org/abs/{identity}"
    record = {"identity": identity, "url": url, "checked_at": datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            html = response.read().decode("utf-8")
            record["response_url"] = response.url
            record["status"] = response.status
            record["headers"] = dict(response.headers)
        (root / f"raw-abs-{identity}.html").write_text(html)
        parsed = TextParser()
        parsed.feed(html)
        lines = [" ".join(line.split()) for line in "".join(parsed.parts).splitlines() if line.strip()]
        text = "\n".join(lines)
        begin = text.find("Title:")
        end = text.find("Submission history")
        record["title_abstract_and_fields"] = text[begin:end] if 0 <= begin < end else text[:12000]
        record["history"] = text[end:text.find("References & Citations", end)] if end >= 0 else "Not recovered"
        records.append(record)
        print(identity, record["status"], record["title_abstract_and_fields"], record["history"], sep="\n", flush=True)
    except Exception as error:
        record["error"] = str(error)
        records.append(record)
        print(identity, "ERROR", error, flush=True)
    time.sleep(0.2)
output = root / ("raw-exact-ab-" + sys.argv[1].replace(".", "-") + ".json")
output.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n")
