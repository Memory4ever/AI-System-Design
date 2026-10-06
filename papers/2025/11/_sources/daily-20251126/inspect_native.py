"""Project fresh native responses onto this window's metadata boundaries."""
import datetime as dt
import json
import pathlib
import re
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).parent


class Scripts(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.scripts = []
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag == "script":
            self.active = True
            self.parts = []

    def handle_data(self, data):
        if self.active:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.active:
            self.scripts.append("".join(self.parts))
            self.active = False


parser = Scripts()
parser.feed((ROOT / "anthropic.html").read_text())
decoder = json.JSONDecoder()
records = {}
for script in parser.scripts:
    marker = "self.__next_f.push("
    if not script.startswith(marker):
        continue
    try:
        payload, _ = decoder.raw_decode(script[len(marker):])
    except ValueError:
        continue
    if len(payload) < 2 or not isinstance(payload[1], str):
        continue
    flight = payload[1]
    for match in re.finditer(r'\{"_type":"post"', flight):
        try:
            obj, _ = decoder.raw_decode(flight[match.start():])
        except ValueError:
            continue
        if isinstance(obj, dict) and obj.get("publishedOn"):
            records[obj["slug"]["current"]] = {k: obj.get(k) for k in ("title", "publishedOn", "slug")}
nearby = [x for x in records.values() if "2025-11-20" <= x["publishedOn"] < "2025-12-02"]
result = {"source": "fresh anthropic.html; actual decoded JSON Flight objects",
          "unique_dated_records": len(records), "nearby_metadata": sorted(nearby, key=lambda x: x["publishedOn"]),
          "window_utc": ["2025-11-25T01:00:00Z", "2025-11-26T01:00:00Z"],
          "limitations": "current CMS; not a deletion-completeness or immutable-history guarantee"}
(ROOT / "anthropic-window-metadata.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
print(json.dumps(result, ensure_ascii=False, indent=2))

for kind in (1, 2):
    obj = json.loads((ROOT / f"seed-type{kind}-page0.json").read_text())
    rows = []
    for item in obj["sub_article_list"]:
        meta = item["ArticleMeta"]
        rows.append({"title": item["ArticleSubContentEn"]["Title"], "date_ms": meta["PublishDate"],
                     "utc": dt.datetime.fromtimestamp(meta["PublishDate"] / 1000, dt.timezone.utc).isoformat(),
                     "pinned": meta["IsPinned"]})
    result = {"article_type": kind, "returned": len(rows), "has_more": obj["has_more"],
              "next_page_token": obj["next_page_token"], "total": obj["total"], "metadata_only": rows}
    (ROOT / f"seed-type{kind}-metadata.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))

# Flight text records specify UTF-8 byte lengths and may contain arbitrary newlines.
data = (ROOT / "zai-page2.rsc").read_bytes()
pos = 0
components = []
while pos < len(data):
    header = re.match(rb"[0-9a-f]+:T([0-9a-f]+),", data[pos:])
    if header:
        pos += header.end() + int(header.group(1), 16)
        continue
    end = data.find(b"\n", pos)
    if end < 0:
        end = len(data)
    line = data[pos:end]
    pos = end + 1
    _, sep, body = line.partition(b":")
    if sep and body[:1] in (b"[", b"{"):
        try:
            components.append(json.loads(body))
        except (ValueError, UnicodeDecodeError):
            pass


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


for component in components:
    for obj in walk(component):
        if "hasMore" in obj:
            print("ZAI_PAGE_PROPS", list(obj), obj["hasMore"], obj.get("nextPage"))
            rows = []
            for key, value in obj.items():
                if isinstance(value, list):
                    for row in value:
                        if isinstance(row, dict):
                            rows.append({k: v for k, v in row.items()
                                         if k in ("id", "title_zh", "title_en", "date", "publishDate", "publishedAt", "createAt", "createdAt")})
            result = {"parser": "Flight JSON with length-prefixed text skipped in bytes",
                      "nextPage": obj.get("nextPage"), "hasMore": obj["hasMore"], "metadata": rows}
            (ROOT / "zai-page2-metadata.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
            print(json.dumps(result, ensure_ascii=False, indent=2))
