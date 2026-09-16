#!/usr/bin/env python3
"""Extract auditable section evidence from the bounded exact-v1 HTML set."""

from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path


HERE = Path(__file__).resolve().parent
HTML_DIR = HERE / "exact-v1-html-bounded"
DIRECT_HTML_DIR = HERE / "exact-v1-html-direct"


class TextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.stack: list[str] = []
        self.current_tag: str | None = None
        self.buffer: list[str] = []
        self.blocks: list[dict] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        tag = tag.lower()
        self.stack.append(tag)
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "figcaption"}:
            self.current_tag = tag
            self.buffer = []

    def handle_data(self, data: str) -> None:
        if self.current_tag:
            self.buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if self.current_tag == tag:
            text = re.sub(r"\s+", " ", " ".join(self.buffer)).strip()
            if text:
                self.blocks.append({"tag": tag, "text": text})
            self.current_tag = None
            self.buffer = []
        if self.stack:
            for index in range(len(self.stack) - 1, -1, -1):
                if self.stack[index] == tag:
                    del self.stack[index:]
                    break


def normalize(text: str, limit: int = 1500) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit] + ("…" if len(text) > limit else "")


def choose_section(blocks: list[dict], patterns: list[str], fallback: str | None = None) -> dict:
    heading_indices = [i for i, block in enumerate(blocks) if block["tag"].startswith("h")]
    selected = None
    for index in heading_indices:
        heading = blocks[index]["text"]
        if any(re.search(pattern, heading, re.I) for pattern in patterns):
            selected = index
            break
    if selected is None and fallback == "mechanism":
        # Some manuscripts use a domain-specific section name rather than
        # "Method".  Select the first substantive numbered section after the
        # introduction, never the page title/abstract/related-work section.
        for index in heading_indices:
            heading = blocks[index]["text"]
            if re.match(r"^[2-4](?:\.|\s)", heading) and not re.search(
                r"related|background|prelim|experiment|evaluation|result|setup|dataset",
                heading,
                re.I,
            ):
                selected = index
                break
    if selected is None and fallback == "evaluation":
        for index in heading_indices:
            heading = blocks[index]["text"]
            if re.search(r"study|analysis|setup|case|data|finding|measurement", heading, re.I):
                selected = index
                break
    if selected is not None:
        heading = blocks[selected]["text"]
        level = int(blocks[selected]["tag"][1])
        body = []
        for block in blocks[selected + 1:]:
            # A section includes its subordinate headings.  Stopping at the
            # first h3/h4 made many real Method/Evaluation sections appear
            # empty because arXiv puts the prose below a subsection title.
            if block["tag"].startswith("h"):
                if int(block["tag"][1]) <= level:
                    break
                continue
            if block["tag"] in {"p", "li", "figcaption"} and len(block["text"]) >= 40:
                body.append(block["text"])
            if len(body) >= 4:
                break
        return {"heading": normalize(heading, 300), "excerpt": normalize(" ".join(body))}
    return {"heading": "Not separately disclosed", "excerpt": ""}


def main() -> None:
    rows = []
    paths = {path.name: path for path in HTML_DIR.glob("*v1.html")}
    paths.update({path.name: path for path in DIRECT_HTML_DIR.glob("*v1.html")})
    for path in sorted(paths.values(), key=lambda item: item.name):
        parser = TextParser()
        parser.feed(path.read_text(errors="replace"))
        blocks = parser.blocks
        headings = [normalize(block["text"], 240) for block in blocks if block["tag"].startswith("h")]
        title = next(
            (heading for heading in headings if heading.lower() != "report github issue"),
            path.stem,
        )
        withdrawal = any("withdraw" in block["text"].lower() for block in blocks[:30])
        rows.append({
            "arxiv_id": path.stem.removesuffix("v1"),
            "exact_version": path.stem,
            "title": title,
            "bytes": path.stat().st_size,
            "withdrawal_signal": withdrawal,
            "mechanism": choose_section(blocks, [r"method", r"approach", r"framework", r"system design", r"algorithm", r"architecture", r"proposed", r"adaptive", r"training objective", r"SkillScope", r"TruncProof", r"weight quantization: practice", r"AI Harness Engineering"], "mechanism"),
            "evaluation": choose_section(blocks, [r"experiment", r"evaluation", r"result", r"empirical", r"benchmark", r"Quantizing Llama"], "evaluation"),
            "limitations": choose_section(blocks, [r"limitation", r"discussion", r"threat", r"conclusion", r"outlook", r"future of"]),
            "headings": headings,
        })
    out = {"schema": "bounded-exact-v1-section-evidence-v1", "report_date": "2026-05-14", "count": len(rows), "items": rows}
    (HERE / "bounded-evidence-extract.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
