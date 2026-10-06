"""Read a bounded title frontier; IDs are not first-public dates."""

from html.parser import HTMLParser
import json
from pathlib import Path


class FrontierParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paper = None
        self.title_depth = 0
        self.parts = []
        self.items = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and attrs.get("title") == "Abstract":
            self.paper = attrs.get("href", "").rsplit("/", 1)[-1]
        if tag == "div" and "list-title" in attrs.get("class", ""):
            self.title_depth = 1
            self.parts = []
        elif self.title_depth and tag == "div":
            self.title_depth += 1

    def handle_data(self, data):
        if self.title_depth:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if tag == "div" and self.title_depth:
            self.title_depth -= 1
            if not self.title_depth and self.paper:
                title = " ".join(" ".join(self.parts).split()).removeprefix("Title: ")
                self.items.append({"id": self.paper, "title": title})


root = Path(__file__).parent
for category in ("cs.CL", "cs.LG", "cs.DC", "cs.CV"):
    parser = FrontierParser()
    parser.feed((root / f"month-frontier-{category}.raw").read_text())
    selected = [x for x in parser.items if x["id"].startswith("2509.") and int(x["id"].split(".")[1]) <= 1850]
    print(category, len(parser.items), "bounded title clues", len(selected))
    for item in selected:
        print(json.dumps(item, ensure_ascii=False))
