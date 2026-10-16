"""Project saved search HTML; extraction does not assign semantic review status."""
import json
from html.parser import HTMLParser
from pathlib import Path


class Search(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.rows = []
        self.current = None
        self.heading = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        if tag == "li" and "arxiv-result" in classes:
            self.current = {"id": "", "version": "", "title": [], "abstract": [], "record": []}
            self.rows.append(self.current)
        if self.current:
            if tag == "a" and "/abs/" in attrs.get("href", ""):
                self.current["id"] = attrs["href"].split("/abs/")[-1]
            if "abstract-full" in classes:
                self.current["version"] = attrs.get("id", "").removesuffix("-abstract-full")
        if tag not in {"input", "img", "br", "meta", "link", "hr"}:
            self.stack.append((tag, classes))

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                self.stack = self.stack[:index]
                break
        if tag == "li":
            self.current = None

    def handle_data(self, data):
        if any(tag == "h1" for tag, _ in self.stack):
            self.heading.append(data)
        if self.current is None:
            return
        self.current["record"].append(data)
        for field, marker in [("title", "title"), ("abstract", "abstract-full")]:
            if any(marker in classes for _, classes in self.stack):
                self.current[field].append(data)


root = Path(__file__).parent
output = {}
for topic in ["MODEL", "LEARNING", "SYSTEM", "AGENT", "MULTI"]:
    parser = Search()
    parser.feed((root / f"SUP_ARXIV_{topic}_20261015.html").read_text())
    rows = [{key: " ".join(value).strip() if isinstance(value, list) else value
             for key, value in row.items()} for row in parser.rows]
    output[topic] = {"heading": " ".join(parser.heading).strip(), "rows": rows}
destination = root / "SUP_ARXIV_SEARCH_FIELDS_20261015.json"
with destination.open("x") as stream:
    json.dump(output, stream, ensure_ascii=False, indent=2)
    stream.write("\n")
print(json.dumps({topic: {"heading": value["heading"], "rows": len(value["rows"])}
                  for topic, value in output.items()}, ensure_ascii=False))
