"""Read exact-version arXiv HTML from stdin; emit readable numbered blocks.

This is an inspection helper, not semantic review or a file-writing downloader.
"""
from html.parser import HTMLParser
import sys


class Blocks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hide = 0
        self.buf = []
        self.blocks = []

    def flush(self):
        s = " ".join(" ".join(self.buf).split())
        if s:
            self.blocks.append(s)
        self.buf = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "nav"):
            self.hide += 1
        if tag in ("h1", "h2", "h3", "h4", "h5", "p", "table", "figure"):
            self.flush()

    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav"):
            self.hide -= 1
        if tag in ("h1", "h2", "h3", "h4", "h5", "p", "table", "figure", "li", "tr"):
            self.flush()

    def handle_data(self, s):
        if not self.hide:
            self.buf.append(s)


p = Blocks()
p.feed(sys.stdin.read())
p.flush()
start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
end = int(sys.argv[2]) if len(sys.argv) > 2 else len(p.blocks)
for i, s in enumerate(p.blocks):
    if start <= i < end:
        print(f"B{i}: {s}")
