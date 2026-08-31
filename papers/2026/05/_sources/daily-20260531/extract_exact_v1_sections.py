#!/usr/bin/env python3
"""Build a date-local, read-only-derived section index for exact-v1 evidence review."""
from __future__ import annotations

import hashlib
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE_DIR = HERE / "exact-v1-html"


class ArxivHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.capture: str | None = None
        self.buffer: list[str] = []
        self.current_heading = "Preamble"
        self.title = ""
        self.sections: list[dict[str, object]] = []
        self.current_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "figcaption"}:
            self.flush_capture()
            self.capture = tag
            self.buffer = []

    def handle_endtag(self, tag: str) -> None:
        if self.capture == tag:
            text = re.sub(r"\s+", " ", html.unescape(" ".join(self.buffer))).strip()
            if tag.startswith("h") and text:
                self.flush_section()
                self.current_heading = text
                if tag == "h1" and not self.title:
                    self.title = text
            elif text:
                self.current_text.append(text)
            self.capture = None
            self.buffer = []

    def handle_data(self, data: str) -> None:
        if self.capture:
            self.buffer.append(data)

    def flush_capture(self) -> None:
        if self.capture and self.buffer:
            text = re.sub(r"\s+", " ", html.unescape(" ".join(self.buffer))).strip()
            if text:
                self.current_text.append(text)
        self.capture = None
        self.buffer = []

    def flush_section(self) -> None:
        if self.current_text:
            body = " ".join(self.current_text)
            self.sections.append({"heading": self.current_heading, "text": body})
        self.current_text = []


def html_record(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    parser = ArxivHTMLParser()
    parser.feed(raw.decode("utf-8", errors="replace"))
    parser.flush_capture()
    parser.flush_section()
    return {
        "arxiv_id": path.stem,
        "route": "official arXiv exact-v1 HTML",
        "sha256": hashlib.sha256(raw).hexdigest(),
        "title": parser.title,
        "sections": parser.sections,
    }


def pdf_text_record(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    text = path.with_suffix(".txt").read_text(errors="replace")
    headings = []
    for match in re.finditer(r"(?m)^(\d+(?:\.\d+)*\.?\s+[^\n]{3,100}|Appendix\s+[A-Z][^\n]{0,90}|Limitations[^\n]{0,90})$", text):
        headings.append({"heading": re.sub(r"\s+", " ", match.group(1)).strip(), "offset": match.start()})
    sections = []
    for index, item in enumerate(headings):
        start = int(item["offset"])
        end = int(headings[index + 1]["offset"]) if index + 1 < len(headings) else len(text)
        sections.append({"heading": item["heading"], "text": re.sub(r"\s+", " ", text[start:end]).strip()})
    return {
        "arxiv_id": path.stem,
        "route": "official arXiv exact-v1 PDF",
        "sha256": hashlib.sha256(raw).hexdigest(),
        "title": text.splitlines()[0].strip(),
        "sections": sections,
    }


records = [html_record(path) for path in sorted(SOURCE_DIR.glob("*.html")) if path.stat().st_size > 1000]
pdf_path = SOURCE_DIR / "2606.20634.pdf"
if pdf_path.exists() and pdf_path.with_suffix(".txt").exists():
    records.append(pdf_text_record(pdf_path))
records.sort(key=lambda item: str(item["arxiv_id"]))
(HERE / "exact-v1-section-index.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"records": len(records), "html": sum(r["route"].endswith("HTML") for r in records), "pdf": sum(r["route"].endswith("PDF") for r in records)}, ensure_ascii=False))
