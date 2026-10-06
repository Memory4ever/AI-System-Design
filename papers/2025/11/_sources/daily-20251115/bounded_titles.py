"""Inspect only an explicit ID slice of the official month title list."""

from html.parser import HTMLParser
from pathlib import Path
import re


class Titles(HTMLParser):
    def __init__(self):
        super().__init__()
        self.identity = None
        self.title_depth = 0
        self.parts = []
        self.rows = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "dt":
            self.identity = None
        if tag == "a" and re.fullmatch(r"2511\.\d{5}", attrs.get("id", "")):
            self.identity = attrs["id"]
        if self.title_depth:
            self.title_depth += 1
        elif tag == "div" and "list-title" in attrs.get("class", ""):
            self.title_depth = 1
            self.parts = []

    def handle_endtag(self, tag):
        if self.title_depth:
            self.title_depth -= 1
            if not self.title_depth and self.identity:
                if "2511.09700" <= self.identity <= "2511.10699":
                    self.rows.append((self.identity, " ".join("".join(self.parts).split())))

    def handle_data(self, data):
        if self.title_depth:
            self.parts.append(data)


parser = Titles()
parser.feed((Path(__file__).parent / "raw-arxiv-cl-month-canonical.html").read_text())
print("Explicit slice: 2511.09700-10699; title-only rows:", len(parser.rows))
for identity, title in parser.rows:
    print(identity, title)
