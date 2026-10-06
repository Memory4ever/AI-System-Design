"""Extract numbered HTML sections for bounded evidence reading."""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag in ("p", "h1", "h2", "h3", "h4", "tr", "figcaption"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


path = Path(sys.argv[1])
parser = Text()
parser.feed(path.read_text())
lines = [re.sub(r"\s+", " ", line).strip()
         for line in "".join(parser.parts).splitlines()]
lines = [line for line in lines if line]
if len(sys.argv) == 2:
    for index, line in enumerate(lines):
        if re.match(r"^\d+(?:\.\d+)*\s", line) and len(line) < 180:
            print(str(index) + ": " + line)
else:
    start, end = map(int, sys.argv[2:4])
    for index, line in enumerate(lines[start:end], start):
        print(str(index) + ": " + line)
