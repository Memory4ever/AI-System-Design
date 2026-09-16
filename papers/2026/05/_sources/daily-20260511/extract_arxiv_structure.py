#!/usr/bin/env python3
"""Print exact-v1 arXiv section and caption locators for the 2026-05-11 repair.

This is an evidence-reading helper. It does not mutate the report or Books.
"""

from __future__ import annotations

import html
import re
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser


class StructureParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.capture: tuple[str, str] | None = None
        self.parts: list[str] = []
        self.rows: list[tuple[str, str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        classes = set((attrs_dict.get("class") or "").split())
        if tag in {"h1", "h2", "h3", "h4"} or "ltx_caption" in classes:
            self.capture = (tag, attrs_dict.get("id") or "")
            self.parts = []

    def handle_data(self, data: str) -> None:
        if self.capture:
            self.parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.capture and tag == self.capture[0]:
            kind, anchor = self.capture
            text = re.sub(r"\s+", " ", html.unescape(" ".join(self.parts))).strip()
            if text:
                self.rows.append((kind, anchor, text))
            self.capture = None
            self.parts = []


def main() -> None:
    compact = "--compact" in sys.argv
    arxiv_ids = [value for value in sys.argv[1:] if value != "--compact"]
    for arxiv_id in arxiv_ids:
        url = f"https://arxiv.org/html/{arxiv_id}v1"
        print(f"\n===== {arxiv_id} {url} =====")
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "AI-System-Design evidence audit"})
            body = urllib.request.urlopen(request, timeout=45).read().decode("utf-8", "replace")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            print(f"ERROR {exc}")
            continue
        parser = StructureParser()
        parser.feed(body)
        if not compact:
            for kind, anchor, text in parser.rows:
                print(f"{kind}\t{anchor}\t{text}")
            continue

        headings = [text for kind, _anchor, text in parser.rows if kind in {"h2", "h3", "h4"}]
        captions = [text for kind, _anchor, text in parser.rows if kind == "figcaption"]

        def select(pattern: str, values: list[str], limit: int) -> list[str]:
            regex = re.compile(pattern, re.IGNORECASE)
            return [value for value in values if regex.search(value)][:limit]

        method = select(r"method|approach|framework|algorithm|formulation|architecture|objective|system|design", headings, 4)
        evaluation = select(r"experiment|evaluation|result|benchmark|ablation|analysis|setup|setting", headings, 5)
        limitations = select(r"limit|discussion|threat|broader impact|conclusion", headings, 4)
        useful_captions = select(r"table|figure|algorithm", captions, 6)
        print("METHOD\t" + " | ".join(method))
        print("EVAL\t" + " | ".join(evaluation))
        print("LIMIT\t" + " | ".join(limitations))
        print("CAPTION\t" + " | ".join(useful_captions))


if __name__ == "__main__":
    main()
