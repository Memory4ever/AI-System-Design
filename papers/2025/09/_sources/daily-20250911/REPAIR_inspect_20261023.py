"""Read saved HTML blocks, preserving equation alttext and table row boundaries."""

from html.parser import HTMLParser
from pathlib import Path
import sys


class Blocks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = None
        self.depth = 0
        self.math_depth = 0
        self.text = []
        self.blocks = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if self.root and tag == self.root[0]:
            self.depth += 1
        classes = attrs.get("class", "").split()
        paper_block = tag in ("p", "h1", "h2", "h3", "h4", "h5", "h6", "table", "figcaption") and any(c.startswith("ltx_") for c in classes)
        event_block = ((tag == "h1" and "title" in classes)
                       or (tag == "blockquote" and "abstract" in classes)
                       or (tag == "div" and "submission-history" in classes)
                       or (tag == "td" and any(c in classes for c in ("comments", "jref", "doi"))))
        if not self.root and (paper_block or event_block):
            if paper_block or event_block:
                self.root = (tag, attrs.get("id", ""))
                self.depth = 1
                self.text = []
        if self.root:
            if tag == "math":
                self.math_depth += 1
                self.text.append(" " + attrs.get("alttext", "[math]") + " ")
            if tag == "tr":
                self.text.append("\n")
            elif tag in ("td", "th"):
                self.text.append(" | ")

    def handle_endtag(self, tag):
        if tag == "math" and self.math_depth:
            self.math_depth -= 1
        if self.root and tag == self.root[0]:
            self.depth -= 1
            if not self.depth:
                self.blocks.append((*self.root, "\n".join(
                    " ".join(line.split()) for line in "".join(self.text).splitlines())))
                self.root = None

    def handle_data(self, data):
        if self.root and not self.math_depth:
            self.text.append(data)


if __name__ == "__main__":
    parser = Blocks()
    parser.feed(Path(sys.argv[1]).read_text())
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    end = int(sys.argv[3]) if len(sys.argv) > 3 else len(parser.blocks)
    for index, (tag, identity, text) in enumerate(parser.blocks):
        if start <= index < end:
            print(index, tag, identity, text, "\n")
