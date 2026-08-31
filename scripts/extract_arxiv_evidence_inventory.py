#!/usr/bin/env python3
"""Extract auditable section inventory from frozen exact-version arXiv files.

This helper only exposes source structure. It does not score a paper, choose a
knowledge owner, infer an undisclosed condition, or mark a Review complete.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from hashlib import sha256
from pathlib import Path


def clean(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def html_sections(path: Path) -> list[dict[str, str]]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    headings = list(re.finditer(r"<h([1-4])[^>]*>(.*?)</h\1>", raw, re.I | re.S))
    result: list[dict[str, str]] = []
    for index, match in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(raw)
        section = raw[match.end():end]
        paragraphs = [clean(item) for item in re.findall(r"<p[^>]*>(.*?)</p>", section, re.I | re.S)]
        excerpt = " ".join(item for item in paragraphs if len(item) >= 40)[:1200]
        result.append({
            "level": match.group(1),
            "heading": clean(match.group(2)),
            "excerpt": excerpt,
        })
    return result


def text_sections(path: Path) -> list[dict[str, str]]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    pages = re.split(r"^===== Page (\d+) =====$", raw, flags=re.M)
    result: list[dict[str, str]] = []
    for index in range(1, len(pages), 2):
        page = pages[index]
        content = re.sub(r"\s+", " ", pages[index + 1]).strip()
        result.append({"level": "page", "heading": f"Page {page}", "excerpt": content[:1600]})
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--packet", required=True, type=Path)
    parser.add_argument("--ids-file", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    rows = []
    for arxiv_id in [line.strip() for line in args.ids_file.read_text().splitlines() if line.strip()]:
        html_path = args.packet / "arxiv-v1" / f"{arxiv_id}v1.html"
        pdf_path = args.packet / "arxiv-v1" / f"{arxiv_id}v1.pdf"
        text_path = args.packet / "arxiv-v1" / f"{arxiv_id}v1.txt"
        if html_path.exists() and html_path.stat().st_size:
            primary, route, sections = html_path, "exact-v1-html", html_sections(html_path)
        elif pdf_path.exists() and pdf_path.stat().st_size and text_path.exists():
            primary, route, sections = pdf_path, "exact-v1-pdf-with-extracted-text", text_sections(text_path)
        else:
            primary, route, sections = None, "missing", []
        rows.append({
            "arxiv_id": arxiv_id,
            "route": route,
            "primary_path": primary.as_posix() if primary else None,
            "primary_sha256": sha256(primary.read_bytes()).hexdigest() if primary else None,
            "sections": sections,
        })

    payload = {
        "schema": "arxiv-exact-version-evidence-inventory-v1",
        "warning": "Structure extraction only; not a Source Review or semantic completion receipt.",
        "families": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "families": len(rows),
        "html": sum(row["route"] == "exact-v1-html" for row in rows),
        "pdf": sum(row["route"] == "exact-v1-pdf-with-extracted-text" for row in rows),
        "missing": sum(row["route"] == "missing" for row in rows),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
