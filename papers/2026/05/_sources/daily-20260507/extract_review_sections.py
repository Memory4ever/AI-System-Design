#!/usr/bin/env python3
"""Print bounded exact-v1 sections for the May 7 author review.

This is a read-only navigation helper.  It never decides a claim or mutates a
report; the author still checks the emitted passages against the paper.
"""

from __future__ import annotations

import argparse
import html
import re
from html.parser import HTMLParser
from pathlib import Path


class PaperParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.active: str | None = None
        self.buffer: list[str] = []
        self.sections: list[tuple[str, list[str]]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "figcaption"}:
            self.active = tag
            self.buffer = []

    def handle_data(self, data: str) -> None:
        if self.active:
            self.buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag != self.active:
            return
        text = re.sub(r"\s+", " ", html.unescape(" ".join(self.buffer))).strip()
        if tag.startswith("h"):
            self.sections.append((text, []))
        elif text and self.sections:
            self.sections[-1][1].append(text)
        self.active = None
        self.buffer = []


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="+")
    parser.add_argument("--chars", type=int, default=1100)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    wanted = re.compile(
        r"abstract|method|approach|architecture|framework|algorithm|experiment|"
        r"evaluation|result|limitation|discussion|conclusion|theorem|proof|ablation",
        re.I,
    )
    for arxiv_id in args.ids:
        source = Path(f"/tmp/may07-{arxiv_id}.html")
        parsed = PaperParser()
        parsed.feed(source.read_text(errors="ignore"))
        print(f"\n### {arxiv_id}")
        if args.compact:
            groups = [
                ("abstract", re.compile(r"^abstract$", re.I)),
                ("method", re.compile(r"method|approach|architecture|framework|algorithm", re.I)),
                ("evaluation", re.compile(r"experiment|evaluation|main results?", re.I)),
                ("limitations", re.compile(r"limitation", re.I)),
                ("conclusion", re.compile(r"conclusion", re.I)),
            ]
            emitted: set[str] = set()
            for _, pattern in groups:
                for heading, texts in parsed.sections:
                    if heading not in emitted and pattern.search(heading):
                        body = " ".join(texts)
                        print(f"## {heading}\n{body[: args.chars]}")
                        emitted.add(heading)
                        break
            print("## Headings\n" + " | ".join(h for h, _ in parsed.sections))
            continue
        for heading, texts in parsed.sections:
            if wanted.search(heading):
                body = " ".join(texts)
                print(f"## {heading}\n{body[: args.chars]}")


if __name__ == "__main__":
    main()
