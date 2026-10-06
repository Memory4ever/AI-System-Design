"""Capture finite monthly title frontiers after fixing the official URL form."""

import datetime
import json
from pathlib import Path
import urllib.request

out = Path(__file__).parent
for category in ["cs.CL", "cs.LG", "cs.DC", "cs.CV"]:
    name = "month-frontier-" + category
    url = "https://arxiv.org/list/" + category + "/2025-09?skip=0&show=2000"
    meta = {"url": url, "checked": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "ResearchReview/1.0"})
        with urllib.request.urlopen(request, timeout=25) as response:
            raw = response.read()
            meta.update(status=response.status, bytes=len(raw), final_url=response.url)
            (out / (name + ".raw")).write_bytes(raw)
    except Exception as error:
        meta["error"] = str(error)
    (out / (name + ".request.json")).write_text(json.dumps(meta, indent=2))
    print(name, meta.get("status"), meta.get("bytes"), meta.get("error"), flush=True)
