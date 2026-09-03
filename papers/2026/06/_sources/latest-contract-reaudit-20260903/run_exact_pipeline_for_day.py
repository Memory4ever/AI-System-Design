#!/usr/bin/env python3
"""Reuse the exact-v1 fetch/index/review pipeline for one frozen Daily."""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


def bind(module, packet: Path, date: str) -> None:
    module.PACKET = packet
    module.REPORT_DATE = date
    if hasattr(module, "DECISIONS"): module.DECISIONS = packet / "fresh-context-semantic-decisions-v2.1.json.gz"
    if hasattr(module, "DENOMINATOR"): module.DENOMINATOR = packet / "candidate-denominator-v2.1.json"
    if hasattr(module, "RAW"): module.RAW = packet / "canonical-raw-identity-inventory-v2.1.json.gz"
    if hasattr(module, "INDEX"): module.INDEX = packet / "exact-v1-section-index-v2.1.json.gz"
    if hasattr(module, "OUT"):
        module.OUT = packet / ("exact-v1-section-index-v2.1.json.gz" if "index" in module.__name__ else "exact-v1-html")
    if hasattr(module, "HTML_DIR"): module.HTML_DIR = packet / "exact-v1-html"
    if hasattr(module, "PDF_DIR"): module.PDF_DIR = packet / "exact-v1-pdf"
    if hasattr(module, "PDF_TEXT_DIR"): module.PDF_TEXT_DIR = packet / "exact-v1-pdf-text"
    if hasattr(module, "TEXT_DIR"): module.TEXT_DIR = packet / "exact-v1-pdf-text"
    if hasattr(module, "MANIFEST"): module.MANIFEST = packet / "exact-v1-access-manifest-v2.1.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("date", help="YYYY-MM-DD")
    parser.add_argument("stage", choices=("fetch", "pdf", "index", "review", "all"), default="all", nargs="?")
    args = parser.parse_args()
    compact = args.date.replace("-", "")
    packet = ROOT / f"papers/{args.date[:4]}/{args.date[5:7]}/_sources/daily-{compact}"
    stages = ("fetch", "pdf", "index", "review") if args.stage == "all" else (args.stage,)
    files = {"fetch": "fetch_day_20260714_exact_v1.py", "pdf": "recover_day_20260714_pdf_fallbacks.py", "index": "index_day_20260714_exact_v1.py", "review": "build_day_20260714_reviews.py"}
    for stage in stages:
        module = load(f"daily_exact_{stage}", files[stage])
        bind(module, packet, args.date)
        module.main()


if __name__ == "__main__": main()
