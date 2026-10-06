"""Read selected exact-HTML text blocks; offsets are local navigation, not evidence."""
import sys
from pathlib import Path
from html.parser import HTMLParser

root = Path(__file__).resolve().parent
paper, start, stop = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
class Blocks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.tag = None
        self.depth = 0
        self.buf = []
        self.blocks = []
    def handle_starttag(self, tag, attrs):
        if tag == "article": self.active = True
        if not self.active: return
        if self.tag:
            if tag == self.tag: self.depth += 1
        elif tag in {"h1","h2","h3","h4","h5","h6","p","table","figure"}:
            self.tag, self.depth, self.buf = tag, 1, []
        if self.tag and tag == "img":
            self.buf.append(dict(attrs).get("alt", ""))
    def handle_data(self, data):
        if self.tag: self.buf.append(data)
    def handle_endtag(self, tag):
        if tag == self.tag:
            self.depth -= 1
            if not self.depth:
                self.blocks.append(" ".join(" ".join(self.buf).split()))
                self.tag = None
parser = Blocks()
parser.feed((root / f"core-{paper}v1.raw.html").read_text())
for i, text in enumerate(parser.blocks):
    if start <= i < stop: print(f"[{i}] {text}")
