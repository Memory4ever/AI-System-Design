#!/usr/bin/env python3
"""Verify official exact-v1 PDF fallbacks and persist page-addressable text."""

from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[5]
PACKET = ROOT / "papers/2026/07/_sources/daily-20260714"
PDF_DIR = PACKET / "exact-v1-pdf"
TEXT_DIR = PACKET / "exact-v1-pdf-text"
MANIFEST = PACKET / "exact-v1-access-manifest-v2.1.json"


def main() -> None:
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    by_id = {item["arxiv_id"]: item for item in manifest["items"]}
    for pdf in sorted(PDF_DIR.glob("*v1.pdf")):
        aid = pdf.name.removesuffix("v1.pdf")
        body = pdf.read_bytes()
        reader = PdfReader(str(pdf))
        pages = []
        for page_number, page in enumerate(reader.pages, 1):
            text = (page.extract_text() or "").strip()
            pages.append(f"<<<PAGE {page_number}>>>\n{text}")
        extracted = "\n\n".join(pages)
        if len(extracted) < 5_000:
            raise RuntimeError(f"insufficient extracted text for {aid}: {len(extracted)}")
        target = TEXT_DIR / f"{aid}v1.txt.gz"
        with gzip.open(target, "wt", encoding="utf-8") as handle:
            handle.write(extracted)
            handle.write("\n")
        by_id[aid] = {
            "arxiv_id": aid,
            "url": f"https://arxiv.org/pdf/{aid}v1",
            "status": "accessible",
            "medium": "official_exact_v1_pdf",
            "bytes": len(body),
            "pages": len(reader.pages),
            "sha256": hashlib.sha256(body).hexdigest(),
            "snapshot": pdf.relative_to(ROOT).as_posix(),
            "text_snapshot": target.relative_to(ROOT).as_posix(),
            "text_chars": len(extracted),
        }
    items = [by_id[item["arxiv_id"]] for item in manifest["items"]]
    manifest.update({
        "status": "complete" if all(item["status"] == "accessible" for item in items) else "fallback_pending",
        "accessible": sum(item["status"] == "accessible" for item in items),
        "pending": sum(item["status"] != "accessible" for item in items),
        "items": items,
    })
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": manifest["status"], "accessible": manifest["accessible"], "pending": manifest["pending"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
