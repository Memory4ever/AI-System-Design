#!/usr/bin/env python3
"""Create a section-level evidence index for 2026-07-14 exact-v1 HTML."""

from __future__ import annotations

import gzip
import json
import re
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PACKET = ROOT / "papers/2026/07/_sources/daily-20260714"
REPORT_DATE = "2026-07-14"
HTML_DIR = PACKET / "exact-v1-html"
PDF_TEXT_DIR = PACKET / "exact-v1-pdf-text"
OUT = PACKET / "exact-v1-section-index-v2.1.json.gz"
DENOMINATOR = PACKET / "candidate-denominator-v2.1.json"


class ArxivHTML(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.titles: dict[str, str] = {}
        self.text: dict[str, list[str]] = {}
        self.heading: str | None = None
        self.heading_section: str | None = None
        self.heading_parts: list[str] = []
        self.skip = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if tag in {"script", "style", "math", "svg", "noscript"}:
            self.skip += 1
            return
        if tag == "section" and data.get("id"):
            self.stack.append(data["id"])
            self.text.setdefault(data["id"], [])
        if tag in {"h2", "h3"}:
            self.heading = tag
            self.heading_section = self.stack[-1] if self.stack else None
            self.heading_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "math", "svg", "noscript"} and self.skip:
            self.skip -= 1
            return
        if tag in {"h2", "h3"} and self.heading == tag:
            if self.heading_section:
                self.titles[self.heading_section] = re.sub(r"\s+", " ", " ".join(self.heading_parts)).strip()
            self.heading = self.heading_section = None
            self.heading_parts = []
        if tag == "section" and self.stack:
            self.stack.pop()

    def handle_data(self, data: str) -> None:
        if self.skip:
            return
        data = re.sub(r"\s+", " ", data).strip()
        if not data:
            return
        if self.heading:
            self.heading_parts.append(data)
        if self.stack:
            self.text[self.stack[-1]].append(data)


def roles(title: str) -> list[str]:
    low = title.lower()
    found = []
    if re.search(r"method|approach|framework|architecture|system|design|algorithm|implementation|model", low): found.append("method")
    if re.search(r"experiment|evaluation|result|benchmark|analysis|study|ablation", low): found.append("evaluation")
    if re.search(r"limitation|discussion|failure|threat|conclusion|future", low): found.append("limitation_or_boundary")
    return found


def main() -> None:
    expected = json.loads(DENOMINATOR.read_text())["retained_candidate_count"]
    papers = []
    for path in sorted(HTML_DIR.glob("*v1.html.gz")):
        parser = ArxivHTML()
        with gzip.open(path, "rt", encoding="utf-8", errors="replace") as handle:
            parser.feed(handle.read())
        sections = []
        for sid, parts in parser.text.items():
            title = parser.titles.get(sid)
            if not title:
                continue
            text = re.sub(r"\s+", " ", " ".join(parts)).strip()
            sections.append({"section_id": sid, "title": title, "roles": roles(title), "word_count": len(text.split()), "text": text})
        # An HTTP-successful HTML shell with only acknowledgements/references is
        # not reviewable primary material.  Leave it out so an official v1 PDF
        # text snapshot can own the section index instead.
        if len(sections) >= 3:
            papers.append({"arxiv_id": path.name.removesuffix("v1.html.gz"), "snapshot": path.relative_to(ROOT).as_posix(), "section_count": len(sections), "sections": sections})
    indexed = {paper["arxiv_id"] for paper in papers}
    for path in sorted(PDF_TEXT_DIR.glob("*v1.txt.gz")):
        aid = path.name.removesuffix("v1.txt.gz")
        if aid in indexed:
            continue
        with gzip.open(path, "rt", encoding="utf-8", errors="replace") as handle:
            text = handle.read()
        sections = []
        for match in re.finditer(r"<<<PAGE (\d+)>>>\n(.*?)(?=\n\n<<<PAGE |\Z)", text, re.S):
            page_number, page_text = match.groups()
            page_text = re.sub(r"\s+", " ", page_text).strip()
            sections.append({
                "section_id": f"page-{page_number}",
                "title": f"PDF page {page_number}",
                "roles": ["pdf_page"],
                "word_count": len(page_text.split()),
                "text": page_text,
            })
        papers.append({
            "arxiv_id": aid,
            "snapshot": path.relative_to(ROOT).as_posix(),
            "section_count": len(sections),
            "sections": sections,
        })
    papers.sort(key=lambda paper: paper["arxiv_id"])
    payload = {"schema": "exact-v1-section-index-v2.1", "report_date": REPORT_DATE, "status": "complete" if len(papers) == expected else "incomplete", "paper_count": len(papers), "expected": expected, "papers": papers}
    with gzip.open(OUT, "wt", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(json.dumps({"papers": len(papers), "expected": expected, "sections": sum(x["section_count"] for x in papers)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
