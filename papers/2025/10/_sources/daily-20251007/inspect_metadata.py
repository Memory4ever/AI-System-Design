"""Bounded metadata display, not a semantic read record."""
from pathlib import Path
from datetime import datetime, timezone
import json
import re

d = Path(__file__).parent
for f in sorted(d.glob("seed-*.raw")):
    if "us" not in f.name and "blogs" not in f.name:
        continue
    obj = json.loads(f.read_text())
    rows = obj.get("sub_article_list", [])
    print(f.name, len(rows), {k: v for k, v in obj.items() if k != "sub_article_list"})
    dates = sorted({r["ArticleMeta"]["PublishDate"] for r in rows})
    print("Neighbors", [datetime.fromtimestamp(x / 1000, timezone.utc).isoformat() for x in dates if 1757000000000 < x < 1762000000000])
for name in ["qwen-articles", "qwen-legacy", "hunyuan-page1"]:
    obj = json.loads((d / (name + ".raw")).read_text())
    rows = []
    def walk(value):
        if isinstance(value, dict):
            if any(k in value for k in ["date", "publish_time", "publishTime"]):
                rows.append({k: v for k, v in value.items() if k in ["date", "title", "publish_time", "publishTime"]})
            for v in value.values():
                walk(v)
        elif isinstance(value, list):
            for v in value:
                walk(v)
        elif isinstance(value, str) and value[:1] in ["[", "{"]:
            try:
                walk(json.loads(value))
            except ValueError:
                pass
    walk(obj)
    print(name, len(rows))
    for r in rows:
        date = str(r.get("date", r.get("publish_time", r.get("publishTime", ""))))
        if name.startswith("hunyuan") or "2025-09" in date or "2025-10" in date or "2025-11" in date:
            print(r)
s = (d / "google-pubs.text.txt").read_text()
print("Google publication headings")
for m in re.finditer("View details\n([^\n]+)", s):
    print(m.group(1))
print("Meta", (d / "meta-research.text.txt").read_text()[1500:4000])
