#!/usr/bin/env python3
"""Extract auditable plain text and section locators from exact-v1 arXiv HTML."""

from __future__ import annotations

import argparse
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PaperParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.skip_depth = 0
        self.section_stack: list[str] = []
        self.section_text: dict[str, list[str]] = {}
        self.heading_depth = 0
        self.heading_section: str | None = None
        self.heading_buffer: list[str] = []
        self.headings: dict[str, str] = {}
        self.all_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag in {"script", "style", "svg", "math"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag == "section":
            section_id = values.get("id") or f"anonymous-{len(self.section_text) + 1}"
            self.section_stack.append(section_id)
            self.section_text.setdefault(section_id, [])
        if tag in {"h1", "h2", "h3", "h4"}:
            self.heading_depth += 1
            self.heading_section = self.section_stack[-1] if self.section_stack else "document"
            self.heading_buffer = []
        if tag in {"p", "li", "tr", "figcaption", "h1", "h2", "h3", "h4", "br"}:
            self._append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "svg", "math"}:
            if self.skip_depth:
                self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag in {"h1", "h2", "h3", "h4"} and self.heading_depth:
            heading = " ".join("".join(self.heading_buffer).split())
            if self.heading_section:
                self.headings[self.heading_section] = heading
            self.heading_depth -= 1
            self.heading_section = None
            self.heading_buffer = []
        if tag == "section" and self.section_stack:
            self.section_stack.pop()
        if tag in {"p", "li", "tr", "figcaption", "h1", "h2", "h3", "h4"}:
            self._append("\n")

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        value = html.unescape(data)
        if self.heading_depth:
            self.heading_buffer.append(value)
        self._append(value)

    def _append(self, value: str) -> None:
        self.all_text.append(value)
        for section_id in self.section_stack:
            self.section_text.setdefault(section_id, []).append(value)


def normalize(value: str) -> str:
    value = re.sub(r"[ \t\f\v]+", " ", value)
    value = re.sub(r" *\n *", "\n", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("dates", nargs="+", help="report dates as YYYY-MM-DD")
    return parser.parse_args()


def process(raw_date: str) -> None:
    compact = raw_date.replace("-", "")
    packet = ROOT / f"papers/2026/04/_sources/daily-{compact}"
    access = json.loads((packet / "exact-v1-access-receipt.json").read_text(encoding="utf-8"))
    records = []
    text_dir = packet / "review-text"
    text_dir.mkdir(parents=True, exist_ok=True)
    for row in access["rows"]:
        if row["body_route"] != "official_html_v1":
            records.append({
                "arxiv_id": row["arxiv_id"],
                "body_route": row["body_route"],
                "headings": [],
                "sections": [],
                "text_path": "—",
            })
            continue
        body_path = ROOT / row["body_path"]
        parser = PaperParser()
        parser.feed(body_path.read_text(encoding="utf-8", errors="replace"))
        full_text = normalize("".join(parser.all_text))
        text_path = text_dir / f"{row['arxiv_id']}v1.txt"
        text_path.write_text(full_text + "\n", encoding="utf-8")
        sections = []
        for section_id, chunks in parser.section_text.items():
            section_text = normalize("".join(chunks))
            if not section_text:
                continue
            sections.append({
                "id": section_id,
                "heading": parser.headings.get(section_id, "—"),
                "characters": len(section_text),
                "preview": section_text[:1600],
            })
        records.append({
            "arxiv_id": row["arxiv_id"],
            "body_route": row["body_route"],
            "headings": [{"id": key, "heading": value} for key, value in parser.headings.items()],
            "sections": sections,
            "text_path": text_path.relative_to(ROOT).as_posix(),
        })
    payload = {
        "schema": "daily-v2.1-exact-v1-review-extract-v1",
        "report_date": raw_date,
        "records": records,
    }
    (packet / "review-extract.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"report_date": raw_date, "records": len(records)}))


def main() -> None:
    for raw_date in arguments().dates:
        process(raw_date)


if __name__ == "__main__":
    main()
