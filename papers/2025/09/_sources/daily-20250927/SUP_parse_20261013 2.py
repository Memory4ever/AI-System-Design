"""Derive text and bounded metadata without modifying primary captures."""
import datetime
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

BASE = Path(__file__).parent


class Body(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = 0
        self.in_script = False
        self.text = []
        self.scripts = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.hidden += 1
        if tag == "script":
            self.in_script = True

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden = max(0, self.hidden - 1)
        if tag == "script":
            self.in_script = False

    def handle_data(self, data):
        if self.in_script:
            self.scripts.append(data)
        elif not self.hidden and data.strip():
            self.text.append(data.strip())


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)
    elif isinstance(value, str) and value.startswith(("{", "[")):
        try:
            yield from walk(json.loads(value))
        except (ValueError, RecursionError):
            pass


def save(path, value):
    if not path.exists():
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


for raw in sorted(BASE.glob("SUP_curl-*_20261013.raw")):
    request = json.loads(raw.with_suffix(".request.json").read_text())
    if request.get("status") != 200 or request.get("exit_code") != 0:
        continue
    if raw.with_suffix(".summary.json").exists() or raw.with_suffix(".txt").exists():
        continue
    data = raw.read_bytes()
    if not data or data.startswith(b"%PDF"):
        continue
    if "openai-rss" in raw.name:
        root = ET.fromstring(data)
        items = root.findall("./channel/item")
        window = []
        for item in items:
            original = item.findtext("pubDate", "")
            if original and parsedate_to_datetime(original).astimezone(datetime.timezone(datetime.timedelta(hours=8))).date().isoformat() == "2025-09-26":
                window.append({"title": item.findtext("title"), "link": item.findtext("link"), "pubDate": original, "description": item.findtext("description")})
        save(raw.with_suffix(".summary.json"), {"total_items": len(items), "bjt_day": "2025-09-26", "window": window})
        print(raw.name, "RSS", len(items), "window", len(window))
        continue
    if data.lstrip().startswith((b"{", b"[")):
        obj = json.loads(data)
        records = []
        fields = ("id", "title", "slug", "date", "PublishDate", "publish_date", "publishedAt", "publicAt", "displayPublishTime", "publish_time", "has_more", "hasMore", "total", "totalNum", "next_page_token")
        for item in walk(obj):
            selected = {key: item[key] for key in fields if key in item and not isinstance(item[key], (dict, list))}
            if selected:
                records.append(selected)
        save(raw.with_suffix(".summary.json"), records)
        print(raw.name, "metadata", len(records))
        continue
    parser = Body()
    parser.feed(data.decode("utf-8", "replace"))
    text = raw.with_suffix(".txt")
    if not text.exists():
        text.write_text("\n".join(parser.text) + "\n")
    if "anthropic" in raw.name:
        records = []
        decoder = json.JSONDecoder()
        for script in parser.scripts:
            for match in re.finditer(r"self\.__next_f\.push\(", script):
                try:
                    pushed, _ = decoder.raw_decode(script[match.end():])
                except ValueError:
                    continue
                for payload in pushed:
                    if not isinstance(payload, str):
                        continue
                    for line in payload.splitlines():
                        body = line.partition(":")[2]
                        if not body.startswith(("[", "{")):
                            continue
                        try:
                            obj, _ = decoder.raw_decode(body)
                        except ValueError:
                            continue
                        for item in walk(obj):
                            if "publishedOn" in item:
                                records.append({key: item.get(key) for key in ("slug", "title", "publishedOn")})
        save(raw.with_suffix(".summary.json"), {"occurrences": len(records), "unique_slugs": len({str(x["slug"]) for x in records}), "unique_titles": len({str(x["title"]) for x in records}), "unique_date_values": len({str(x["publishedOn"]) for x in records}), "records": records})
        print(raw.name, "publishedOn", len(records), "slugs", len({str(x["slug"]) for x in records}), "dates", len({str(x["publishedOn"]) for x in records}))
