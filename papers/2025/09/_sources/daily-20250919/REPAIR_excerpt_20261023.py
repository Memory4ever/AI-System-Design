"""Read local arXiv HTML blocks; block numbers are navigation, not evidence IDs."""
from html.parser import HTMLParser
from pathlib import Path
import sys


class Blocks(HTMLParser):
    VOID = set("area base br col embed hr img input link meta param source track wbr".split())

    def __init__(self):
        super().__init__()
        self.stack = []
        self.current = None
        self.blocks = []

    def handle_starttag(self, tag, attrs):
        if tag in self.VOID:
            return
        self.stack.append(tag)
        attrs = dict(attrs)
        if self.current is None and (tag in ("h1", "h2", "h3", "h4") or (tag == "p" and "ltx_p" in attrs.get("class", "").split())):
            self.current = (len(self.stack), tag, attrs.get("id", ""), [])

    def handle_endtag(self, tag):
        if tag not in self.stack:
            return
        level = len(self.stack) - self.stack[::-1].index(tag)
        if self.current and level <= self.current[0]:
            self.blocks.append((self.current[1], self.current[2], " ".join(self.current[3])))
            self.current = None
        self.stack = self.stack[:level - 1]

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_data(self, data):
        if self.current and data.strip():
            self.current[3].append(data.strip())


if __name__ == "__main__":
    parser = Blocks()
    parser.feed(Path(sys.argv[1]).read_text())
    ranges = []
    for value in sys.argv[2:]:
        start, end = value.split(":")
        ranges.append((int(start), int(end)))
    for index, (tag, identity, text) in enumerate(parser.blocks):
        if (not ranges and tag.startswith("h")) or any(start <= index < end for start, end in ranges):
            print(index, tag, identity, text)
