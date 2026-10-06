import sys
from html.parser import HTMLParser
from recover_day import ROOT


class Titles(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and attrs.get("title") == "Abstract":
            print(attrs.get("href"), end=" ")
        if self.depth:
            self.depth += 1
        elif "list-title" in attrs.get("class", "").split():
            self.depth = 1
            self.parts = []

    def handle_endtag(self, tag):
        if self.depth:
            self.depth -= 1
            if not self.depth:
                print(" ".join("".join(self.parts).split()))

    def handle_data(self, data):
        if self.depth:
            self.parts.append(data)


Titles().feed((ROOT / sys.argv[1]).read_text())
