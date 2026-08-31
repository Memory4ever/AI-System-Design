#!/usr/bin/env python3
"""Read-only structural and disclosure-candidate audit for Daily 2026-06-01 V9.

This script does not declare semantic Gates passed. It verifies denominator and
downstream interface accounting, then flags exact-v1 text that may contradict a
`Not Disclosed` benchmark field for source-by-source human resolution.
"""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/01/README.md"
PACKET = ROOT / "papers/2026/06/_sources/daily-20260601"


def load_repair():
    path = ROOT / "scripts/repair_june01_semantic_audit.py"
    spec = importlib.util.spec_from_file_location("repair_june01_semantic_audit", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def compact(value: str) -> str:
    return " ".join(value.split())


def candidate_snippets(source: str, pattern: str, limit: int = 3) -> list[str]:
    flat = compact(source)
    snippets: list[str] = []
    for match in re.finditer(pattern, flat, flags=re.I):
        start = max(0, match.start() - 90)
        end = min(len(flat), match.end() + 120)
        snippet = flat[start:end]
        if snippet not in snippets:
            snippets.append(snippet)
        if len(snippets) == limit:
            break
    return snippets


POTENTIAL_PATTERNS = {
    "model": r"\b(?:GPT[- ]?\d|GPT-4o|Llama|Qwen|DeepSeek|Claude|Gemma|Mistral|Mixtral|BERT|DeBERTa|RoBERTa|Phi[- ]?\d|OLMo|Yi[- ]?\d|MoE|Transformer)\b",
    "hardware": r"\b(?:H100|H200|A100|A800|A30|V100|L40S|RTX\s?\d{4}|TPU\s?v?\d+|GPU|NPU|CPU|Apple\s+M\d)\b",
    "precision": r"\b(?:FP32|FP16|BF16|FP8|INT8|INT4|float32|float16|bfloat16|4-bit|8-bit|quantization)\b",
    "input_length": r"\b(?:input|prompt|context|sequence|source|lookback|max(?:imum)? input)\b.{0,55}\b\d[\d,]*(?:k|K)?\s*(?:tokens?|steps?|words?|characters?|frames?|seconds?|dimensions?|nodes?)\b",
    "output_length": r"\b(?:output|generation|response|decode|max(?:imum)? new|horizon)\b.{0,55}\b\d[\d,]*(?:k|K)?\s*(?:tokens?|steps?|words?|characters?|frames?|seconds?)\b",
    "batch": r"\bbatch(?: size)?\s*(?:of|=|:|is|was)?\s*\d+\b|\bmini-?batch(?: size)?\s*(?:of|=|:)?\s*\d+\b",
    "concurrency": r"\b(?:concurrency|concurrent requests?|parallel requests?|simultaneous requests?|clients?|tenants?|QPS|requests? per second)\b.{0,45}\b\d+[\d,]*\b|\b\d+[\d,]*\s+(?:concurrent requests?|clients?|tenants?)\b",
}

# Source-specific resolutions from the exact-v1 setup/results audit.  These
# tokens occur in bibliography/related-work prose or protocol examples, not in
# the evaluated configuration for the named field.
RESOLVED_LEXICAL_FALSE_ALARMS = {
    ("SF-PRISM-DP-LORA", "precision"): "quantization appears in the LoftQ bibliography entry; the PRISM setup does not disclose tensor precision",
    ("SF-HYBRID-VERIFIED-DECODING", "concurrency"): "high-concurrency appears only in related-work titles; the evaluated serving cells are batch=1 without a concurrency sweep",
    ("SF-MEMORYWIRE", "concurrency"): "tenant/client vocabulary describes the threat model and governance boundary; no simultaneous-client workload is measured",
    ("SF-RESIDENT-KV-CLAIMS", "hardware"): "GPU/CPU/storage are protocol tiers and lowering examples; no physical benchmark host is evaluated",
}


def main() -> None:
    repair = load_repair()
    text = REPORT.read_text()
    _, candidates = repair.parse_table(text, repair.VALIDATOR.CANDIDATE_LEDGER_MARKER)
    _, reviews = repair.parse_table(text, repair.VALIDATOR.REVIEW_COMPLETION_MARKER)
    _, benchmarks = repair.parse_table(text, repair.VALIDATOR.BENCHMARK_MARKER)
    _, selections = repair.parse_table(text, repair.VALIDATOR.DEEP_ANALYSIS_SELECTION_MARKER)
    _, books = repair.parse_table(text, repair.VALIDATOR.BOOKS_COMPARISON_MARKER)
    ledger = read_tsv(PACKET / "screening-ledger.tsv")
    inventory = read_tsv(PACKET / "candidate-inventory.tsv")
    denominator = read_tsv(PACKET / "fresh-context-candidate-denominator-audit-independent-v9.tsv")
    model_audit = read_tsv(PACKET / "benchmark-model-identity-audit-v9.tsv")

    candidate_ids = [row["Source Family ID"] for row in candidates]
    assert len(ledger) == 371
    assert sum(row["decision"] == "include" for row in ledger) == 40
    assert sum(row["decision"] == "exclude" for row in ledger) == 331
    assert len(inventory) == len({row["source_family_id"] for row in inventory}) == 40
    assert len(candidate_ids) == len(set(candidate_ids)) == 40
    assert {row["source_family_id"] for row in inventory} == set(candidate_ids)
    assert len(reviews) == len({row["Source Family ID"] for row in reviews}) == 40
    assert len(selections) == len({row["Source Family ID"] for row in selections}) == 40
    assert sum(row["Decision"] == "selected" for row in selections) == 3
    assert len(books) == len({row["Source Family ID"] for row in books}) == 40
    assert len(denominator) == 371
    assert sum(row["independent_decision"] == "retain" for row in denominator) == 40
    assert sum(row["independent_decision"] == "pre_denominator_closure" for row in denominator) == 331

    payload = "\n".join(
        f"{row['source_family_id']}\t{row['arxiv_v1']}\t{row['first_public_utc']}"
        for row in inventory
    )
    expected_denominator = "DEN-20260601-" + hashlib.sha256(payload.encode()).hexdigest()[:8]
    assert expected_denominator == "DEN-20260601-5c2ad97d"

    candidate_by_family = {row["Source Family ID"]: row for row in candidates}
    expected_benchmarks = {
        row["Source Family ID"] for row in candidates if row["Benchmark Claim"] == "yes"
    }
    assert {row["Source Family ID"] for row in benchmarks} == expected_benchmarks
    assert len(model_audit) == len({row["source_family_id"] for row in model_audit}) == 40
    assert {row["source_family_id"] for row in model_audit} == expected_benchmarks
    assert sum(row["model_action"] == "corrected_or_precisified" for row in model_audit) == 39
    assert sum(row["model_action"] == "confirmed_exact" for row in model_audit) == 1
    assert all(row["post_audit_result"].endswith("no unresolved unsafe model extraction") for row in model_audit)

    potential: list[tuple[str, str, str]] = []
    resolved_false_alarm_count = 0
    public_exact_pending: list[str] = []
    for row in benchmarks:
        family = row["Source Family ID"]
        arxiv_id = candidate_by_family[family]["Primary Identifier"].removeprefix("arXiv:").removesuffix("v1")
        try:
            source, _ = repair.exact_text(arxiv_id)
        except RuntimeError:
            # One retained family is deliberately reviewed from the official
            # exact-v1 HTML because the packet copy failed.  Keep that row in
            # the accounting and force an explicit manual receipt rather than
            # crashing or pretending that an empty packet proves disclosure.
            public_exact_pending.append(f"{family}\tarXiv:{arxiv_id}v1")
            continue
        for field, pattern in POTENTIAL_PATTERNS.items():
            report_field = {
                "input_length": "Input Length",
                "output_length": "Output Length",
            }.get(field, field.title())
            if not row[report_field].startswith("Not Disclosed"):
                continue
            snippets = candidate_snippets(source, pattern)
            if (family, field) in RESOLVED_LEXICAL_FALSE_ALARMS:
                resolved_false_alarm_count += len(snippets)
                continue
            for snippet in snippets:
                potential.append((family, field, snippet))

    print(
        f"canonical=40/371 closure=331 reviews={len(reviews)} benchmarks={len(benchmarks)} "
        f"selection={len(selections)} books={len(books)} denominator={expected_denominator}"
    )
    print(f"potential_not_disclosed_contradictions={len(potential)}")
    print(f"resolved_lexical_false_alarms={resolved_false_alarm_count}")
    for family, field, snippet in potential:
        print(f"POTENTIAL\t{family}\t{field}\t{snippet}")
    print(f"public_exact_manual_receipts={len(public_exact_pending)}")
    for receipt in public_exact_pending:
        print(f"PUBLIC_EXACT_MANUAL\t{receipt}")


if __name__ == "__main__":
    main()
