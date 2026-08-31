#!/usr/bin/env python3
"""Independent, read-only semantic/interface checks for Daily 2026-06-01."""

from __future__ import annotations

import collections
import csv
import gzip
import html
import importlib.util
import re
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/01/README.md"
PACKET = ROOT / "papers/2026/06/_sources/daily-20260601"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_research", ROOT / "scripts/validate_research.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_validator()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def rows(marker: str) -> list[dict[str, str]]:
    return VALIDATOR._table_after_marker(REPORT.read_text(), marker)[0]


def clean(value: str) -> str:
    return value.strip().strip("`")


def atom_entries() -> dict[str, dict[str, str]]:
    with gzip.open(PACKET / "arxiv-overread-first-page.atom.gz", "rb") as handle:
        root = ET.parse(handle).getroot()
    ns = {"a": "http://www.w3.org/2005/Atom"}
    result: dict[str, dict[str, str]] = {}
    for entry in root.findall("a:entry", ns):
        raw_id = (entry.findtext("a:id", default="", namespaces=ns) or "").rsplit("/", 1)[-1]
        match = re.fullmatch(r"(\d{4}\.\d{4,5})v(\d+)", raw_id)
        if not match:
            continue
        arxiv_id, version = match.groups()
        result[arxiv_id] = {
            "version": version,
            "published": entry.findtext("a:published", default="", namespaces=ns),
            "title": " ".join((entry.findtext("a:title", default="", namespaces=ns) or "").split()),
            "summary": " ".join((entry.findtext("a:summary", default="", namespaces=ns) or "").split()),
        }
    return result


def exact_v1_title(path: Path) -> str | None:
    raw = path.read_text(errors="ignore")
    match = re.search(r'<h1 class="title mathjax">(.*?)</h1>', raw, re.S)
    if not match:
        return None
    value = re.sub(r"<[^>]+>", "", match.group(1)).replace("Title:", "")
    return " ".join(value.split())


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def normalized(value: str) -> str:
    value = html.unescape(value)
    value = value.replace("–", "-").replace("—", "-")
    value = re.sub(r"[^a-z0-9]+", " ", value.lower())
    return " ".join(value.split())


def exact_v1_text(arxiv_id: str) -> tuple[str, str]:
    source_dir = PACKET / "arxiv-v1"
    html_path = source_dir / f"{arxiv_id}v1.html"
    if html_path.exists() and html_path.stat().st_size >= 3_000:
        parser = TextExtractor()
        parser.feed(html_path.read_text(errors="ignore"))
        return "html", " ".join(parser.parts)
    pdf_path = source_dir / f"{arxiv_id}v1.pdf"
    if not pdf_path.exists():
        raise FileNotFoundError(arxiv_id)
    reader = PdfReader(str(pdf_path))
    return "pdf", "\n".join(page.extract_text() or "" for page in reader.pages)


def exact_heading_locators(row: dict[str, str]) -> list[str]:
    values = [
        row["Method / Identity Locators"],
        row["Evaluation Locators"],
        row["Limitations / Counterevidence Locators"],
    ]
    result: list[str] = []
    for value in values:
        result.extend(re.findall(r"exact heading `([^`]+)`", value))
    return result


def main() -> None:
    report = REPORT.read_text()
    ledger = read_tsv(PACKET / "screening-ledger.tsv")
    inventory = read_tsv(PACKET / "candidate-inventory.tsv")
    curation = read_tsv(PACKET / "fresh-audit-curation.tsv")
    atom = atom_entries()
    tables = {
        "candidate": rows("<!-- validator:candidate-ledger-v2.1 -->"),
        "review": rows("<!-- validator:review-completion-v1 -->"),
        "benchmark": rows("<!-- validator:benchmark-contract-v1 -->"),
        "selection": rows("<!-- validator:deep-analysis-selection-v1 -->"),
        "books": rows("<!-- validator:books-comparison-v1 -->"),
        "audit": rows("<!-- validator:semantic-audit-v1 -->"),
    }

    print("ledger", len(ledger), collections.Counter(r["decision"] for r in ledger))
    print("ledger family unique", len({r["source_family_id"] for r in ledger if r["decision"] == "include"}))
    print("inventory", len(inventory), "unique", len({r["source_family_id"] for r in inventory}))
    print("curation", len(curation), collections.Counter(r["review_route"] for r in curation))

    family_sets: dict[str, set[str]] = {}
    for name, table in tables.items():
        if name == "audit":
            continue
        ids = [clean(r["Source Family ID"]) for r in table]
        family_sets[name] = set(ids)
        print(name, len(table), "unique", len(set(ids)), "duplicates", len(ids) - len(set(ids)))

    candidates = family_sets["candidate"]
    inventory_ids = {r["source_family_id"] for r in inventory}
    print("candidate==inventory", candidates == inventory_ids, sorted(candidates ^ inventory_ids)[:20])
    for name in ("review",):
        print(f"candidate=={name}", candidates == family_sets[name], sorted(candidates ^ family_sets[name])[:20])
    benchmark_expected = {
        clean(r["Source Family ID"]) for r in tables["candidate"] if r["Benchmark Claim"] == "yes"
    }
    print("benchmark==claims-yes", family_sets["benchmark"] == benchmark_expected,
          sorted(family_sets["benchmark"] ^ benchmark_expected)[:20])

    cand = tables["candidate"]
    deep = {clean(r["Source Family ID"]) for r in cand if r["Review Status"] == "deep_complete"}
    standard = {clean(r["Source Family ID"]) for r in cand if r["Review Status"] == "standard_complete"}
    closure = {clean(r["Source Family ID"]) for r in cand if r["Review Status"] == "closure_complete"}
    print("routes", len(deep), len(standard), len(closure), len(deep | standard | closure))
    print("selection==deep", family_sets["selection"] == deep, sorted(family_sets["selection"] ^ deep)[:20])
    print("books==candidate-closure", family_sets["books"] == candidates - closure,
          sorted(family_sets["books"] ^ (candidates - closure))[:20])
    print("selection decisions", collections.Counter(r["Decision"] for r in tables["selection"]))
    print("books decisions", collections.Counter(r["Decision"] for r in tables["books"]))
    print("candidate dispositions", collections.Counter(r["Books Disposition"] for r in cand))
    print("access", collections.Counter(r["Access Status"] for r in cand))
    print("benchmark claims", sum(r["Benchmark Claim"] == "yes" for r in cand), len(tables["benchmark"]))

    review_refs = re.findall(r"<!-- review:([^:]+):start -->", report)
    sources = re.findall(r"<!-- source:([^:]+):start -->", report)
    knowledge = re.findall(r"<!-- knowledge:([^:]+):start -->", report)
    books_refs = re.findall(r"<!-- books-review:([^:]+):start -->", report)
    print("blocks", len(review_refs), len(set(review_refs)), len(sources), len(set(sources)),
          len(knowledge), len(set(knowledge)), len(books_refs), len(set(books_refs)))

    # Detect mechanically repeated closure language, including the currently visible recursive prefix defect.
    closure_rows = [r for r in ledger if r["decision"] == "exclude"]
    repeated = [r for r in closure_rows if r["screen_reason"].count("fresh-context exact-v1 identity/title-abstract closure") > 1]
    exact_duplicate_reasons = collections.Counter(r["screen_reason"] for r in closure_rows)
    print("closures", len(closure_rows), "recursive_prefix", len(repeated),
          "duplicate_reason_groups", sum(n > 1 for n in exact_duplicate_reasons.values()))
    if repeated:
        print("recursive examples", [(r["arxiv_id"], r["screen_reason"].count("fresh-context exact-v1 identity/title-abstract closure")) for r in repeated[:10]])

    ledger_ids = {r["arxiv_id"] for r in ledger}
    atom_ledger = {key: value for key, value in atom.items() if key in ledger_ids}
    print("atom identities", len(atom_ledger), "ledger set match", set(atom_ledger) == ledger_ids)
    date_mismatches = [
        (r["arxiv_id"], r["first_public_utc"], atom_ledger[r["arxiv_id"]]["published"])
        for r in ledger
        if atom_ledger[r["arxiv_id"]]["published"] != r["first_public_utc"]
    ]
    revised = {key for key, value in atom_ledger.items() if int(value["version"]) > 1}
    print("date mismatches", len(date_mismatches), date_mismatches[:10])
    print("revised atom identities", len(revised))
    metadata_paths = list((PACKET / "arxiv-v1-metadata").glob("*.abs.html"))
    metadata_ids = {path.name.removesuffix("v1.abs.html") for path in metadata_paths}
    print("exact-v1 metadata", len(metadata_ids), "revised covered", len(revised & metadata_ids),
          "revised missing metadata", len(revised - metadata_ids), sorted(revised - metadata_ids)[:20])
    title_mismatches = []
    ledger_by_id = {r["arxiv_id"]: r for r in ledger}
    for path in metadata_paths:
        arxiv_id = path.name.removesuffix("v1.abs.html")
        title = exact_v1_title(path)
        if title and title != ledger_by_id[arxiv_id]["title"]:
            title_mismatches.append((arxiv_id, ledger_by_id[arxiv_id]["title"], title))
    print("exact-v1 title mismatches", len(title_mismatches), title_mismatches[:10])

    review_by_family = {clean(r["Source Family ID"]): r for r in tables["review"]}
    material_counts: collections.Counter[str] = collections.Counter()
    missing_material: list[str] = []
    locator_mismatches: list[tuple[str, str, str]] = []
    locator_checks = 0
    for item in curation:
        arxiv_id = item["arxiv_id"]
        family = item["source_family_id"]
        try:
            kind, material = exact_v1_text(arxiv_id)
        except FileNotFoundError:
            missing_material.append(arxiv_id)
            continue
        material_counts[kind] += 1
        normalized_material = normalized(material)
        for locator in exact_heading_locators(review_by_family[family]):
            locator_checks += 1
            if normalized(locator) not in normalized_material:
                locator_mismatches.append((family, arxiv_id, locator))
    print("recovered exact-v1 material", dict(material_counts), "missing", missing_material)
    print("exact-heading locator checks", locator_checks, "mismatches", len(locator_mismatches), locator_mismatches[:20])


if __name__ == "__main__":
    main()
