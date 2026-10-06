"""Read only the declared ID slice of the official month title list."""

from html.parser import HTMLParser
from pathlib import Path


class Titles(HTMLParser):
    def __init__(self):
        super().__init__()
        self.identifier = None
        self.depth = 0
        self.parts = []
        self.rows = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        href = attrs.get("href", "")
        if tag == "a" and href.startswith("/abs/"):
            self.identifier = href[5:]
        if self.depth:
            self.depth += 1
        elif tag == "div" and "list-title" in attrs.get("class", "").split():
            self.depth = 1
            self.parts = []

    def handle_data(self, data):
        if self.depth:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if self.depth:
            self.depth -= 1
            if not self.depth and self.identifier:
                if "2511.08700" <= self.identifier <= "2511.09599":
                    self.rows.append((self.identifier, " ".join("".join(self.parts).split())))


parser = Titles()
parser.feed(Path(__file__).with_name("raw-arxiv-cl-month.html").read_text())
print("Bounded title-only lookup: 2511.08700 through 2511.09599; not a day announcement")
print("Rows:", len(parser.rows))
for identifier, title in parser.rows:
    print(identifier, "|", title)
