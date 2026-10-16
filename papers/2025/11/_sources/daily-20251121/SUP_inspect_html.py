"""Read-only HTML projection for actual reading, never semantic validation."""
import argparse
from html.parser import HTMLParser
from pathlib import Path


class Blocks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.current = []
        self.skip = 0

    def flush(self):
        value = " ".join(" ".join(self.current).split())
        self.current = []
        if value:
            self.blocks.append(value)

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag in ("p", "h1", "h2", "h3", "h4", "li", "table", "figure"):
            self.flush()

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
        if tag in ("p", "h1", "h2", "h3", "h4", "li", "table", "figure"):
            self.flush()

    def handle_data(self, data):
        if not self.skip:
            self.current.append(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--end", type=int)
    args = parser.parse_args()
    reader = Blocks()
    reader.feed((Path(__file__).parent / args.name).read_text())
    reader.flush()
    print(f"{args.name}: {len(reader.blocks)} blocks")
    for index in range(args.start, min(args.end or len(reader.blocks), len(reader.blocks))):
        print(index, reader.blocks[index])
