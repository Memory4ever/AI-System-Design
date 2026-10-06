"""Inspect only the target publication slice from the actual Flight payload."""
import json
import pathlib
from html.parser import HTMLParser

class Scripts(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside = False
        self.parts = []
    def handle_starttag(self, tag, attrs):
        self.inside = tag == "script"
    def handle_endtag(self, tag):
        if tag == "script":
            self.inside = False
    def handle_data(self, data):
        if self.inside and data.startswith("self.__next_f.push("):
            self.parts.append(json.loads(data[len("self.__next_f.push("):-1])[1])

parser = Scripts()
parser.feed(pathlib.Path(__file__).with_name("anthropic_research.html").read_text())
decoder = json.JSONDecoder()
seen = set()
def walk(value):
    if isinstance(value, dict):
        date = value.get("publishedOn", "")
        slug = value.get("slug", {})
        if isinstance(slug, dict):
            slug = slug.get("current", "")
        if date and slug and (date, slug) not in seen:
            seen.add((date, slug))
            if "2025-11-20" <= date < "2025-11-23":
                print(json.dumps(value, ensure_ascii=False))
        for item in value.values():
            walk(item)
    elif isinstance(value, list):
        for item in value:
            walk(item)
for part in parser.parts:
    for line in part.splitlines():
        start = line.find(":") + 1
        try:
            obj, _ = decoder.raw_decode(line[start:])
        except (ValueError, TypeError):
            continue
        walk(obj)
print("Unique publication identities parsed:", len(seen))
