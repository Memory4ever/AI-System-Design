import json
from html.parser import HTMLParser
from pathlib import Path


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.links = []
        self.hidden = 0
        self.anchor = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("script", "style"):
            self.hidden += 1
        if tag == "a" and not self.hidden:
            self.anchor = {"href": attrs.get("href"), "text": []}

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden = max(0, self.hidden - 1)
        if tag == "a" and self.anchor:
            self.anchor["text"] = " ".join(self.anchor["text"])
            self.links.append(self.anchor)
            self.anchor = None

    def handle_data(self, data):
        if self.hidden or not data.strip():
            return
        value = data.strip()
        self.text.append(value)
        if self.anchor is not None:
            self.anchor["text"].append(value)


root = Path(__file__).resolve().parent
for path in root.glob("*.html"):
    parser = Page()
    parser.feed(path.read_text())
    target = path.with_suffix(".parsed.json")
    target.write_text(json.dumps({"source": path.name, "text": parser.text, "links": parser.links}, ensure_ascii=False, indent=2))
    print(json.dumps({"source": path.name, "textNodes": len(parser.text), "links": len(parser.links)}))
