#!/usr/bin/env python3
"""Rebuild June 23 exact-v1 TOC and bounded disclosure receipts.

This is a recovery-only structure extractor.  It does not choose candidates,
score them, or mark reviews complete; the date finalizer performs those checks.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

from finalize_june23_v21 import OWNERS, PACKET


def clean(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--html-dir", required=True, type=Path)
    args = parser.parse_args()

    toc: dict[str, list[str]] = {}
    disclosures: dict[str, str] = {}
    patterns = ("NVIDIA", "GPU", "batch size", "precision", "sequence length")

    for arxiv_id in sorted(OWNERS):
        path = args.html_dir / f"{arxiv_id}v1.html"
        if not path.is_file() or path.stat().st_size < 5000:
            raise SystemExit(f"missing or incomplete exact-v1 HTML: {arxiv_id}")
        raw = path.read_text(encoding="utf-8", errors="replace")
        headings = [
            clean(match.group(2))
            for match in re.finditer(r"<h([1-4])[^>]*>(.*?)</h\1>", raw, re.I | re.S)
        ]
        headings = [heading for heading in headings if heading]
        if not headings:
            raise SystemExit(f"no section headings extracted: {arxiv_id}")
        toc[arxiv_id] = headings

        visible = clean(raw)
        sentences = re.split(r"(?<=[.!?])\s+", visible)
        blocks = []
        for pattern in patterns:
            hits = [sentence[:1000] for sentence in sentences if pattern.lower() in sentence.lower()][:2]
            lines = [f'{{"pattern":"{pattern}"}}']
            if hits:
                lines.extend(f"L{index + 1}: {hit}" for index, hit in enumerate(hits))
            else:
                lines.append("No matching text found")
            blocks.append("\n".join(lines))
        disclosures[arxiv_id] = "\n--------------------------------------------------------------------------------\n".join(blocks)

    if set(toc) != set(OWNERS) or set(disclosures) != set(OWNERS):
        raise SystemExit("recovered evidence identity set differs from frozen denominator")
    (PACKET / "exact-v1-toc.json").write_text(
        json.dumps(toc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (PACKET / "exact-v1-disclosure-hits.json").write_text(
        json.dumps(disclosures, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"toc": len(toc), "disclosures": len(disclosures)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
