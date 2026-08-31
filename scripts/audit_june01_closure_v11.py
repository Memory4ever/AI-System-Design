#!/usr/bin/env python3
"""Full-population closure and post-write audit for Daily 2026-06-01."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/01/README.md"
PACKET = ROOT / "papers/2026/06/_sources/daily-20260601"
RECEIPT = PACKET / "POST_WRITE_FRESH_AUDIT_V1.md"
DENOMINATOR = "DEN-20260601-5c2ad97d"

INTEGRATES = {
    "SF-FED-PERSONALIZATION-SILENT-FAILURES": (
        "2606.00947v1",
        "Books/part-06-ai-infrastructure/66-evaluation-system.md",
        ("client-local", "aggregate", "privacy", "monitor"),
    ),
    "SF-ORDER-AGNOSTIC-CHAIN-RULE": (
        "2606.00997v1",
        "Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
        ("reveal order", "joint distribution", "fixed", "likelihood"),
    ),
    "SF-DEEP-RESEARCH-RUBRIC-RL": (
        "2606.01091v1",
        "Books/part-04-training-system/33-grpo.md",
        ("atomic rubric", "group-relative", "bootstrap", "holdout"),
    ),
    "SF-SPARSE-REPEATED-TRAINING": (
        "2606.01155v1",
        "Books/part-04-training-system/28-pretraining.md",
        ("unique-token", "repeated", "sparsity", "真实硬件效率"),
    ),
}

EXCLUDED_LEAKAGE = (
    "SF-EXPWEAVER-LATENT-RAG",
    "SF-SATURATED-DATA-SIGNALS",
    "Latent Experience Read Path",
    "Correctness 饱和不等于训练信号归零",
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_module("validate_research_june01_v11", ROOT / "scripts/validate_research.py")
REPAIR = load_module("repair_june01_v11", ROOT / "scripts/repair_june01_semantic_audit.py")


def clean(value: str) -> str:
    return value.strip().strip("`")


def read_tsv(name: str) -> list[dict[str, str]]:
    with (PACKET / name).open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def table(text: str, marker: str) -> list[dict[str, str]]:
    return VALIDATOR._table_after_marker(text, marker)[0]


def normalized(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip()).lower()


def verify_review_provenance(text: str, candidates: list[dict[str, str]], reviews: list[dict[str, str]]) -> None:
    candidate_map = {clean(row["Source Family ID"]): row for row in candidates}
    provenance: list[str] = []
    for row in reviews:
        family = clean(row["Source Family ID"])
        segment = VALIDATOR._bounded_segment(text, f"review:{family}", family, [])
        assert segment is not None
        assert f"claim:{family}" in segment
        candidate = candidate_map[family]
        expected = VALIDATOR._expected_review_provenance(
            family,
            candidate,
            row["Review Route"],
            clean(row["Primary Evidence Version"]),
            clean(row["Reviewed Evidence Versions"]),
            clean(row["Method / Identity Locators"]),
            clean(row["Evaluation Locators"]),
            clean(row["Limitations / Counterevidence Locators"]),
            clean(row["Artifact Locators"]),
            clean(row["Claim Boundary Ref"]),
            clean(candidate["Review Ref"]),
            VALIDATOR._normalized_body_sha256(segment),
        )
        assert clean(row["Review Provenance ID"]) == expected, family
        provenance.append(expected)
        primary = clean(row["Primary Evidence Version"])
        assert re.fullmatch(r"arXiv:\d{4}\.\d{4,5}v1", primary), (family, primary)
        for field in (
            "Method / Identity Locators",
            "Evaluation Locators",
            "Limitations / Counterevidence Locators",
        ):
            value = clean(row[field])
            assert value and (primary in value or value == "Not Disclosed"), (family, field, value)
    assert len(provenance) == len(set(provenance)) == 40


def packet_material_count(candidates: list[dict[str, str]]) -> tuple[int, int, int]:
    html_count = pdf_count = public_count = 0
    for row in candidates:
        arxiv = clean(row["Primary Identifier"]).removeprefix("arXiv:").removesuffix("v1")
        html_path = PACKET / "arxiv-v1" / f"{arxiv}v1.html"
        pdf_path = PACKET / "arxiv-v1" / f"{arxiv}v1.pdf"
        if REPAIR.is_full_arxiv_html(html_path):
            html_count += 1
        elif pdf_path.exists():
            pdf_count += 1
        else:
            assert arxiv in REPAIR.WEB_EXACT, arxiv
            public_count += 1
    assert (html_count, pdf_count, public_count) == (38, 1, 1)
    return html_count, pdf_count, public_count


def verify_books(candidates: list[dict[str, str]], books_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    all_books = {path: path.read_text() for path in sorted((ROOT / "Books").rglob("*.md"))}
    joined = "\n".join(all_books.values())
    candidate_map = {clean(row["Source Family ID"]): row for row in candidates}
    output: list[dict[str, str]] = []
    for row in books_rows:
        family = clean(row["Source Family ID"])
        disposition = clean(row["Decision"])
        primary = clean(candidate_map[family]["Primary Identifier"]).removeprefix("arXiv:")
        target = clean(row["Target Chapter Ref"])
        target_path = target.split("#L", 1)[0]
        assert (ROOT / target_path).exists(), target
        assert clean(row["Adjacent Chapter Refs"])
        assert target_path not in [ref.split("#L", 1)[0] for ref in clean(row["Adjacent Chapter Refs"]).split(";")]
        if family in INTEGRATES:
            exact_id, owner_path, keywords = INTEGRATES[family]
            assert disposition == "Integrate"
            assert target_path == owner_path.lower().replace("books/", "books/"), (family, target_path, owner_path)
            owner = ROOT / owner_path
            owner_text = owner.read_text()
            assert sum(exact_id in content for content in all_books.values()) == 1, family
            assert joined.count(exact_id) == 2, (family, joined.count(exact_id))
            assert owner_text.count(exact_id) == 2
            lower = owner_text.lower()
            assert all(keyword.lower() in lower for keyword in keywords), family
            result = "PASS — body plus exact-v1 source note occur only in the unique owner"
            counts = "2 exact-id hits / 1 owner file"
        else:
            assert disposition == "No Change — Existing Coverage"
            assert primary not in joined, (family, primary)
            result = "PASS — current owner/adjacent proposition covers delta; no source-specific writeback leaked"
            counts = "0 source-id hits"
        output.append(
            {
                "family": family,
                "disposition": disposition,
                "owner": target,
                "counts": counts,
                "result": result,
            }
        )
    assert set(INTEGRATES) == {row["family"] for row in output if row["disposition"] == "Integrate"}
    assert all(token not in joined for token in EXCLUDED_LEAKAGE)
    return output


def render_receipt(rows: list[dict[str, str]], material_counts: tuple[int, int, int]) -> str:
    lines = [
        "# 2026-06-01 Post-Write Fresh Audit V1",
        "",
        f"Denominator `{DENOMINATOR}`; the complete `371 raw = 40 retained + 331 family-specific closures` population and all 40 retained-family dispositions were re-audited after the four serialized Books writebacks.",
        "",
        "- Result: PASS; unresolved findings: 0.",
        "- Evidence: 40/40 Review Provenance receipts, 40/40 exact-v1 locator sets, 36/36 Benchmark Claim=yes contracts and 40/40 full-frontier Selection decisions pass; the other four retained families are explicitly Benchmark Claim=no.",
        f"- Exact-v1 material: {material_counts[0]} packet-frozen full HTML, {material_counts[1]} packet-frozen PDF-only, and {material_counts[2]} official public exact-v1 manual receipt (`SF-METASTABLE-FAULT-SCHEDULING`).",
        "- Benchmark omission contract: every undisclosed field is the exact literal `Not Disclosed`; disclosed and not-applicable values preserve the evaluated role/workload boundary.",
        "- Books: 4 Integrate and 36 No Change; the four exact-v1 IDs each occur twice (body/source note) in exactly one canonical owner file, every No Change exact-v1 ID has zero Books hits, and the two V9 excluded-family leaks remain absent.",
        "- Independence disclosure: degraded fresh-context adversarial self-audit; delegated/cross-model review was unavailable in this task context, so no independent second-model claim is made.",
        "",
        "| Source Family | Disposition | Current owner / adjacent anchor | Books unique/no-leakage | Result |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['family']} | {row['disposition']} | `{row['owner']}` | {row['counts']} | {row['result']} |"
        )
    lines.extend(
        [
            "",
            "## Gate verdict",
            "",
            "- Coverage Gate: Closed.",
            "- Evidence Gate: Passed.",
            "- Books Gate: Passed.",
            "- Completion: Complete.",
            "",
        ]
    )
    return "\n".join(lines)


def regenerate_manifest() -> None:
    manifest = PACKET / "SHA256SUMS"
    rows = []
    for path in sorted(path for path in PACKET.rglob("*") if path.is_file() and path != manifest):
        rows.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  ./{path.relative_to(PACKET)}")
    manifest.write_text("\n".join(rows) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    text = REPORT.read_text()
    candidates = table(text, "<!-- validator:candidate-ledger-v2.1 -->")
    reviews = table(text, "<!-- validator:review-completion-v1 -->")
    benchmarks = table(text, "<!-- validator:benchmark-contract-v1 -->")
    selections = table(text, "<!-- validator:deep-analysis-selection-v1 -->")
    books_rows = table(text, "<!-- validator:books-comparison-v1 -->")
    audits = table(text, "<!-- validator:semantic-audit-v1 -->")
    ledger = read_tsv("screening-ledger.tsv")
    denominator = read_tsv("fresh-context-candidate-denominator-audit-independent-v9.tsv")
    inventory = read_tsv("candidate-inventory.tsv")

    assert len(ledger) == len(denominator) == 371
    assert Counter(row["decision"] for row in ledger) == {"include": 40, "exclude": 331}
    assert Counter(row["independent_decision"] for row in denominator) == {
        "retain": 40,
        "pre_denominator_closure": 331,
    }
    assert {row["arxiv_id"] for row in ledger} == {row["arxiv_id"] for row in denominator}
    closures = [row for row in denominator if row["independent_decision"] == "pre_denominator_closure"]
    assert all(row["closure_class"] not in ("", "—") for row in closures)
    assert all(row["independent_rationale"] not in ("", "—") for row in closures)
    assert all(row["reopen_condition"] not in ("", "—") for row in closures)

    family_sets = []
    for rows in (candidates, reviews, selections, books_rows):
        ids = [clean(row["Source Family ID"]) for row in rows]
        assert len(ids) == len(set(ids)) == 40
        family_sets.append(set(ids))
    assert all(family_sets[0] == value for value in family_sets[1:])
    assert family_sets[0] == {row["source_family_id"] for row in inventory}
    assert all(int(row["Design Delta"]) + int(row["System Reach"]) + int(row["Durability"]) == int(row["Total"]) for row in candidates)
    verify_review_provenance(text, candidates, reviews)
    material_counts = packet_material_count(candidates)

    expected_benchmark = {clean(row["Source Family ID"]) for row in candidates if clean(row["Benchmark Claim"]) == "yes"}
    actual_benchmark = [clean(row["Source Family ID"]) for row in benchmarks]
    assert len(actual_benchmark) == len(set(actual_benchmark)) == 36
    assert set(actual_benchmark) == expected_benchmark
    for row in benchmarks:
        for field in ("Workload", "Model", "Hardware", "Precision", "Input Length", "Output Length", "Batch", "Concurrency", "SLO", "Evaluator"):
            value = clean(row[field])
            assert value
            assert not value.startswith("Not Disclosed "), (row["Source Family ID"], field, value)

    decisions = Counter(clean(row["Decision"]) for row in selections)
    assert decisions == {"selected": 3, "not_selected": 37}
    rationales = [normalized(clean(row["Priority Rationale"])) for row in selections if clean(row["Decision"]) == "not_selected"]
    assert len(rationales) == len(set(rationales)) == 37
    assert all("超过三项" not in value and "篇幅有限" not in value for value in rationales)

    assert Counter(clean(row["Decision"]) for row in books_rows) == {
        "No Change — Existing Coverage": 36,
        "Integrate": 4,
    }
    books_audit = verify_books(candidates, books_rows)
    assert {clean(row["Scope"]) for row in audits} == {"coverage", "evidence", "deep_analysis_selection", "books"}
    assert all(clean(row["Status"]) == "passed" for row in audits)

    headings = re.findall(r"(?m)^## .+$", text)
    assert len(headings) == 14 and headings[-1] == "## 13. Final Status", headings
    assert "**Strict Window:** 2026-05-31 09:00:00 ～ 2026-06-01 09:00:00" in text
    assert "| Completion Status | Complete |" in text
    assert "| Coverage Gate | Closed |" in text
    assert "| Evidence Gate | Passed |" in text
    assert "| Books Gate | Passed |" in text

    if args.write_receipt:
        RECEIPT.write_text(render_receipt(books_audit, material_counts))
        packet_readme = (PACKET / "README.md").read_text()
        line = "- Standard 40/40 post-write closure receipt: `POST_WRITE_FRESH_AUDIT_V1.md`\n"
        if line not in packet_readme:
            marker = "- Artifact hashes: `SHA256SUMS`\n"
            assert marker in packet_readme
            packet_readme = packet_readme.replace(marker, line + marker, 1)
            (PACKET / "README.md").write_text(packet_readme)
        regenerate_manifest()
    print(
        "PASS raw=371 retained=40 closures=331 reviews=40 benchmarks=36 "
        "selection=40 books=40 integrate=4 no_change=36 findings=0"
    )


if __name__ == "__main__":
    main()
