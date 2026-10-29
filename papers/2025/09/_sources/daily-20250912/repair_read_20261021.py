"""Read bounded text/math/table blocks from saved primary HTML, without mutation."""

import argparse
from html.parser import HTMLParser
from pathlib import Path


class Blocks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.frames = []
        self.blocks = []
        self.skip_math = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if self.skip_math:
            self.skip_math += 1
            return
        if tag == "math":
            for frame in self.frames:
                frame[2].append(" " + attrs.get("alttext", "[math without alttext]") + " ")
            self.skip_math = 1
            return
        self.stack.append(tag)
        if tag in {"p", "h1", "h2", "h3", "h4", "table", "figure"}:
            self.frames.append([tag, len(self.stack), [], attrs.get("id", "")])
        if tag in {"br", "tr", "td", "th"}:
            for frame in self.frames:
                frame[2].append(" | ")

    def handle_endtag(self, tag):
        if self.skip_math:
            self.skip_math -= 1
            return
        if self.frames and self.frames[-1][0] == tag:
            frame = self.frames.pop()
            if not any(parent[0] in {"table", "figure"} for parent in self.frames):
                self.blocks.append((tag, frame[3], " ".join("".join(frame[2]).split())))
        if tag in self.stack:
            self.stack = self.stack[:len(self.stack) - 1 - self.stack[::-1].index(tag)]

    def handle_data(self, data):
        if not self.skip_math and "script" not in self.stack and "style" not in self.stack:
            for frame in self.frames:
                frame[2].append(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--headings", action="store_true")
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int)
    args = parser.parse_args()
    document = Blocks()
    document.feed(args.path.read_text())
    for index, (tag, identity, text) in enumerate(document.blocks):
        if args.headings and not tag.startswith("h"):
            continue
        if index >= args.start and (args.stop is None or index < args.stop):
            print(index, tag, identity, text)


if __name__ == "__main__":
    main()
