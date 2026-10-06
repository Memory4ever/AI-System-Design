"""Render local primary HTML to bounded reviewable text; no network or writes."""
import sys
from html.parser import HTMLParser


class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if not self.skip and tag in ("p", "h1", "h2", "h3", "h4", "tr", "li", "section"):
            print()
        if not self.skip and tag == "section":
            print("[SECTION " + dict(attrs).get("id", "") + "]")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
        if not self.skip and tag in ("p", "h1", "h2", "h3", "h4", "tr", "li"):
            print()

    def handle_data(self, data):
        if not self.skip:
            print(data, end=" ")


TextParser().feed(sys.stdin.read())
