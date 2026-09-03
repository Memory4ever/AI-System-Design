#!/usr/bin/env python3
"""Create a reviewable section index for exact-v1 HTML snapshots."""

from __future__ import annotations

import gzip
import json
import re
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PACKET = ROOT / "papers/2026/07/_sources/daily-20260713"
HTML_DIR = PACKET / "exact-v1-html"
OUT = PACKET / "exact-v1-section-index-v2.1.json.gz"


class ArxivHTML(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.section_stack: list[str] = []
        self.section_titles: dict[str, str] = {}
        self.section_text: dict[str, list[str]] = {}
        self.heading_level: str | None = None
        self.heading_section: str | None = None
        self.heading_parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag in {"script", "style", "math", "svg", "noscript"}:
            self.skip_depth += 1
            return
        if tag == "section" and attrs_dict.get("id"):
            section_id = attrs_dict["id"]
            self.section_stack.append(section_id)
            self.section_text.setdefault(section_id, [])
        if tag in {"h2", "h3"}:
            self.heading_level = tag
            self.heading_section = self.section_stack[-1] if self.section_stack else None
            self.heading_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "math", "svg", "noscript"} and self.skip_depth:
            self.skip_depth -= 1
            return
        if tag in {"h2", "h3"} and self.heading_level == tag:
            if self.heading_section:
                title = re.sub(r"\s+", " ", " ".join(self.heading_parts)).strip()
                self.section_titles[self.heading_section] = title
            self.heading_level = None
            self.heading_section = None
            self.heading_parts = []
        if tag == "section" and self.section_stack:
            self.section_stack.pop()

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        text = re.sub(r"\s+", " ", data).strip()
        if not text:
            return
        if self.heading_level:
            self.heading_parts.append(text)
        if self.section_stack:
            self.section_text[self.section_stack[-1]].append(text)


def classify(title: str) -> list[str]:
    low = title.lower()
    labels = []
    if re.search(r"method|approach|framework|architecture|system|design|algorithm|implementation|model", low):
        labels.append("method")
    if re.search(r"experiment|evaluation|result|benchmark|analysis|study", low):
        labels.append("evaluation")
    if re.search(r"limitation|discussion|failure|threat|conclusion|future", low):
        labels.append("limitation_or_boundary")
    return labels


def main() -> None:
    papers = []
    for path in sorted(HTML_DIR.glob("*v1.html.gz")):
        parser = ArxivHTML()
        with gzip.open(path, "rt", encoding="utf-8", errors="replace") as handle:
            parser.feed(handle.read())
        sections = []
        for section_id, parts in parser.section_text.items():
            title = parser.section_titles.get(section_id)
            if not title:
                continue
            text = re.sub(r"\s+", " ", " ".join(parts)).strip()
            sections.append({
                "section_id": section_id,
                "title": title,
                "roles": classify(title),
                "word_count": len(text.split()),
                "text": text,
            })
        arxiv_id = path.name.removesuffix("v1.html.gz")
        papers.append({
            "arxiv_id": arxiv_id,
            "snapshot": path.relative_to(ROOT).as_posix(),
            "section_count": len(sections),
            "sections": sections,
        })
    payload = {
        "schema": "exact-v1-section-index-v2.1",
        "report_date": "2026-07-13",
        "status": "complete" if len(papers) == 62 else "incomplete",
        "paper_count": len(papers),
        "papers": papers,
    }
    with gzip.open(OUT, "wt", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(json.dumps({
        "papers": len(papers),
        "sections": sum(paper["section_count"] for paper in papers),
        "without_method_route": [paper["arxiv_id"] for paper in papers if not any("method" in section["roles"] for section in paper["sections"])],
        "without_evaluation_route": [paper["arxiv_id"] for paper in papers if not any("evaluation" in section["roles"] for section in paper["sections"])],
        "without_boundary_route": [paper["arxiv_id"] for paper in papers if not any("limitation_or_boundary" in section["roles"] for section in paper["sections"])],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
