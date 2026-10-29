from html.parser import HTMLParser
from pathlib import Path
import sys


class Sections(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.selected_depth = None
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "section":
            self.depth += 1
            if attrs.get("id") in sys.argv[2:]:
                self.selected_depth = self.depth
                print("\nSECTION", attrs["id"])
        if tag in ("math", "script", "style"):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ("math", "script", "style"):
            self.skip = max(0, self.skip - 1)
        if tag == "section":
            if self.selected_depth == self.depth:
                self.selected_depth = None
            self.depth -= 1

    def handle_data(self, data):
        if self.selected_depth is not None and not self.skip and data.strip():
            print(data.strip(), end=" ")


Sections().feed(Path(sys.argv[1]).read_text())
