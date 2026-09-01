#!/usr/bin/env python3
"""Build reproducible section indexes from locally cached official exact-v1 bodies.

This script does not make semantic admission or Books decisions.  It records the
real headings and body excerpts that a reviewer must use instead of placeholders.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
SOURCE_ROOT = ROOT / "papers/2026/04/_sources"

METHOD_HEADING_OVERRIDE = {
    "2604.14403": "3.2 ModelRepresentations",
    "2604.14434": "8 Causal Interventions",
    "2604.14612": "3 ConfLayers",
    "2604.14858": "3 Extending ATBench via Taxonomy-Guided Customization",
    "2604.15149": "3 Isomorphic Perturbation Testing",
    "2604.15464": "3.1 Preprocessing",
    "2604.15774": "3 MemEvoBench",
    "2604.17677": "5. The Semantic Disentanglement Pipeline",
    "2604.17861": "Persistent Kernel Executor",
    "2604.18529": "4.1. Overview & Challenges",
    "2604.18616": "3 Overviewof Argus",
    "2604.17283": "4 HorizonBench Data Generator",
    "2604.17337": "4 Autosearch",
    "2604.19503": "4.1 System Overview",
    "2604.19540": "3 MMP as Semantic Infrastructure",
    "2604.19667": "2.3 Dataset Construction",
    "2604.19844": "V Mitigating Trust Boundary Confusion",
    "2604.20105": "IV EnergAIzer Core: Kernel-level Predictions",
    "2604.20452": "III-B From Validation to Re-identification",
    "2604.20211": "3 Methodology",
    "2604.20795": "Methods and Architecture",
    "2604.20819": "2 Stream cyclic quorum sets attention",
    "2604.21003": "2 The Harness Evolution Loop",
    "2604.21072": "4. BloomBee Design Overview",
}

EVALUATION_HEADING_OVERRIDE = {
    "2604.14403": "5 ResultsandDiscussion",
    "2604.17677": "7. Empirical Evaluation",
    "2604.18616": "9 Evaluation",
    "2604.19533": "9. RESULTS",
    "2604.20211": "5 Results",
    "2604.20795": "Experiments and Results",
    "2604.19667": "3.2 Main Results",
    "2604.19844": "V-C Mitigation Strategy Evaluations",
    "2604.21003": "3.3 Evaluation Protocol",
}

LIMITATIONS_HEADING_OVERRIDE = {
    # The paper has no standalone limitations heading.  Its conclusion is the
    # explicit exact-v1 non-proof boundary; do not reuse the Results section.
    "2604.14403": "6 Conclusion",
}


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


class ExactHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_heading = False
        self.heading_level = ""
        self.heading_id = ""
        self.heading_parts: list[str] = []
        self.current: dict | None = None
        self.sections: list[dict] = []
        self.in_paragraph = False
        self.paragraph_parts: list[str] = []
        self.links: list[dict] = []
        self.current_href = ""
        self.current_link_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {key: value or "" for key, value in attrs}
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.in_heading = True
            self.heading_level = tag
            self.heading_id = attr.get("id", "")
            self.heading_parts = []
        elif tag == "p":
            self.in_paragraph = True
            self.paragraph_parts = []
        elif tag == "a" and attr.get("href"):
            self.current_href = attr["href"]
            self.current_link_parts = []

    def handle_endtag(self, tag: str) -> None:
        if self.in_heading and tag == self.heading_level:
            title = clean("".join(self.heading_parts))
            if title:
                self.current = {
                    "level": self.heading_level,
                    "heading": title,
                    "html_id": self.heading_id or "—",
                    "paragraphs": [],
                }
                self.sections.append(self.current)
            self.in_heading = False
        elif tag == "p" and self.in_paragraph:
            text = clean("".join(self.paragraph_parts))
            if text and self.current is not None:
                self.current["paragraphs"].append(text)
            self.in_paragraph = False
        elif tag == "a" and self.current_href:
            self.links.append({"href": self.current_href, "text": clean("".join(self.current_link_parts))})
            self.current_href = ""
            self.current_link_parts = []

    def handle_data(self, data: str) -> None:
        if self.in_heading:
            self.heading_parts.append(data)
        if self.in_paragraph:
            self.paragraph_parts.append(data)
        if self.current_href:
            self.current_link_parts.append(data)


def parse_html(path: Path) -> tuple[list[dict], list[dict]]:
    parser = ExactHTMLParser()
    parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
    return parser.sections, parser.links


def parse_pdf(path: Path) -> list[dict]:
    import pdfplumber

    with pdfplumber.open(path) as document:
        page_texts = [page.extract_text() or "" for page in document.pages]
    sections: list[dict] = []
    current: dict | None = None
    heading_pattern = re.compile(
        r"^(?:"
        r"(?:\d+(?:\.\d+)*|[IVX]+|[A-Z])\.?\s+[A-Z][A-Za-z0-9 &:/_.-]{2,}"
        r"|(?:Introduction|Background|Motivation|Methods?(?:ology)?|Approach|Design|Architecture|"
        r"Implementation|System|Evaluation|Experiments?|Results?|Analysis|Discussion|"
        r"Limitations?|Threats to Validity|Conclusion|Future Work)(?:\s+.*)?"
        r")$",
        re.IGNORECASE,
    )
    for page_number, page_text in enumerate(page_texts, 1):
        for raw_line in page_text.splitlines():
            line = clean(raw_line)
            if not line:
                continue
            if heading_pattern.match(line) and len(line) < 140:
                current = {
                    "level": "pdf-section",
                    "heading": line,
                    "html_id": f"page-{page_number}",
                    "paragraphs": [],
                }
                sections.append(current)
            elif current is not None:
                if current["paragraphs"] and len(current["paragraphs"][-1]) < 900:
                    current["paragraphs"][-1] = clean(current["paragraphs"][-1] + " " + line)
                else:
                    current["paragraphs"].append(line)
    if sections:
        return sections
    text = clean("\n".join(page_texts))
    return [{
        "level": "pdf",
        "heading": "PDF full text (layout extraction)",
        "html_id": "—",
        "paragraphs": [text[index:index + 1200] for index in range(0, min(len(text), 12000), 1200)],
    }]


def section_score(heading: str, keywords: tuple[str, ...], role: str) -> int:
    lower = heading.lower()
    score = max((100 - 3 * index for index, keyword in enumerate(keywords) if keyword in lower), default=0)
    if "appendix" in lower or re.match(r"^[a-z]\s", lower):
        score -= 30
    if role == "method" and any(token in lower for token in ("evaluation", "experiment", "result", "benchmark", "conclusion")):
        score -= 70
    if role == "evaluation" and any(token in lower for token in ("introduction", "background", "related work", "conclusion")):
        score -= 70
    if role == "limitations" and "instructions for reporting errors" in lower:
        score -= 200
    return score


def choose(sections: list[dict], keywords: tuple[str, ...], fallback: int, role: str) -> dict:
    candidates = [(section_score(section["heading"], keywords, role), index, section)
                  for index, section in enumerate(sections)]
    candidates = [entry for entry in candidates if entry[0] > 0 and entry[2]["paragraphs"]]
    if candidates:
        return max(candidates, key=lambda entry: (entry[0], -entry[1]))[2]
    useful = [section for section in sections if section["paragraphs"]]
    return useful[min(fallback, len(useful) - 1)] if useful else {
        "level": "—", "heading": "—", "html_id": "—", "paragraphs": []
    }


def excerpt(section: dict, limit: int = 1200) -> str:
    return clean(" ".join(section.get("paragraphs", [])[:3]))[:limit] or "—"


def heading_override(sections: list[dict], expected: str, fallback: dict) -> dict:
    normalized = clean(expected).lower()
    return next(
        (section for section in sections if clean(section["heading"]).lower() == normalized and section["paragraphs"]),
        fallback,
    )


def process(day: int) -> None:
    packet = SOURCE_ROOT / f"daily-202604{day:02d}"
    receipt = json.loads((packet / "exact-v1-access-receipt.json").read_text(encoding="utf-8"))
    rows = []
    for access in receipt["rows"]:
        if access["withdrawn"]:
            rows.append({
                "arxiv_id": access["arxiv_id"],
                "route": access["body_route"],
                "withdrawn": True,
                "withdrawal_phrase": access["withdrawal_phrase"],
                "body_sha256": "—",
                "method": {"locator": "—", "excerpt": "—"},
                "evaluation": {"locator": "—", "excerpt": "—"},
                "limitations": {"locator": "—", "excerpt": "—"},
                "artifact_links": [],
            })
            continue
        path = ROOT / access["body_path"]
        if path.suffix == ".html":
            sections, links = parse_html(path)
        else:
            sections, links = parse_pdf(path), []
        sections = [section for section in sections if "instructions for reporting errors" not in section["heading"].lower()]
        method = choose(sections, (
            "methodology", "method", "system design", "architecture", "approach", "framework",
            "algorithm", "protocol", "design", "implementation", "model",
        ), 2, "method")
        evaluation = choose(sections, (
            "evaluation", "experiments", "experiment", "results", "result", "benchmark", "performance", "analysis",
        ), max(2, len(sections) // 2), "evaluation")
        limitations = choose(sections, (
            "limitations", "limitation", "threats to validity", "discussion", "future work", "conclusion",
        ), max(2, len(sections) - 2), "limitations")
        if access["arxiv_id"] in LIMITATIONS_HEADING_OVERRIDE:
            limitations = next(
                section for section in sections
                if clean(section["heading"]) == LIMITATIONS_HEADING_OVERRIDE[access["arxiv_id"]]
            )
        method = heading_override(sections, METHOD_HEADING_OVERRIDE.get(access["arxiv_id"], ""), method)
        evaluation = heading_override(sections, EVALUATION_HEADING_OVERRIDE.get(access["arxiv_id"], ""), evaluation)
        artifacts = [link for link in links if any(token in link["href"].lower() for token in (
            "github.com", "gitlab.com", "huggingface.co", "codeberg.org", "zenodo.org",
        ))]
        rows.append({
            "arxiv_id": access["arxiv_id"],
            "route": access["body_route"],
            "withdrawn": False,
            "body_path": access["body_path"],
            "body_sha256": access["body_sha256"],
            "introduction": {
                "locator": f"{(intro := choose(sections, ('introduction', 'motivation', 'background'), 1, 'introduction'))['level']} {intro['heading']} [id={intro['html_id']}]",
                "excerpt": excerpt(intro),
            },
            "method": {
                "locator": f"{method['level']} {method['heading']} [id={method['html_id']}]",
                "excerpt": excerpt(method),
            },
            "evaluation": {
                "locator": f"{evaluation['level']} {evaluation['heading']} [id={evaluation['html_id']}]",
                "excerpt": excerpt(evaluation),
            },
            "limitations": {
                "locator": f"{limitations['level']} {limitations['heading']} [id={limitations['html_id']}]",
                "excerpt": excerpt(limitations),
            },
            "artifact_links": artifacts[:10],
            "section_headings": [section["heading"] for section in sections],
        })
    payload = {
        "schema": "exact-v1-section-index-v1",
        "report_date": f"2026-04-{day:02d}",
        "source_receipt": (packet / "exact-v1-access-receipt.json").relative_to(ROOT).as_posix(),
        "body_count": sum(not row["withdrawn"] for row in rows),
        "withdrawn_count": sum(row["withdrawn"] for row in rows),
        "rows": rows,
    }
    output = packet / "exact-v1-section-index.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"day": day, "bodies": payload["body_count"], "withdrawn": payload["withdrawn_count"]}))


def main() -> None:
    for day in range(16, 24):
        process(day)


if __name__ == "__main__":
    main()
