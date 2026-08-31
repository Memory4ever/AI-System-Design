#!/usr/bin/env python3
"""Normalize 2026-06-01 benchmark omissions to the canonical literal value."""

from __future__ import annotations

import argparse
import csv
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/01/README.md"
PACKET = ROOT / "papers/2026/06/_sources/daily-20260601"
BENCH_TSV = PACKET / "benchmark-disclosure-v9-retained.tsv"
MODEL_TSV = PACKET / "benchmark-model-identity-audit-v9.tsv"
FIELDS = [
    "Workload",
    "Model",
    "Hardware",
    "Precision",
    "Input Length",
    "Output Length",
    "Batch",
    "Concurrency",
    "SLO",
    "Evaluator",
]


def load_repair():
    spec = importlib.util.spec_from_file_location("june01_repair", ROOT / "scripts/repair_june01_semantic_audit.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def canonical(value: str) -> str:
    return "Not Disclosed" if value.strip().startswith("Not Disclosed") else value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    repair = load_repair()
    report = REPORT.read_text()
    headers, rows = repair.parse_table(report, repair.VALIDATOR.BENCHMARK_MARKER)
    changed = 0
    normalized_by_family: dict[str, dict[str, str]] = {}
    for row in rows:
        family = row["Source Family ID"]
        for field in FIELDS:
            new_value = canonical(row[field])
            changed += new_value != row[field]
            row[field] = new_value
        normalized_by_family[family] = row
    report = repair.replace_table(report, repair.VALIDATOR.BENCHMARK_MARKER, headers, rows)

    bench_fields, bench_rows = read_tsv(BENCH_TSV)
    tsv_map = {
        "workload": "Workload",
        "model": "Model",
        "hardware": "Hardware",
        "precision": "Precision",
        "input_length": "Input Length",
        "output_length": "Output Length",
        "batch": "Batch",
        "concurrency": "Concurrency",
        "slo": "SLO",
        "evaluator": "Evaluator",
    }
    for row in bench_rows:
        source = normalized_by_family[row["source_family_id"]]
        for tsv_field, report_field in tsv_map.items():
            row[tsv_field] = source[report_field]

    model_fields, model_rows = read_tsv(MODEL_TSV)
    for row in model_rows:
        row["post_audit_model"] = normalized_by_family[row["source_family_id"]]["Model"]

    if args.apply:
        REPORT.write_text(report)
        write_tsv(BENCH_TSV, bench_fields, bench_rows)
        write_tsv(MODEL_TSV, model_fields, model_rows)
    print(f"rows={len(rows)} normalized_cells={changed} mode={'apply' if args.apply else 'dry-run'}")


if __name__ == "__main__":
    main()
