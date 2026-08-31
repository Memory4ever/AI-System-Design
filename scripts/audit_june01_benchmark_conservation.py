#!/usr/bin/env python3
"""Fresh audit and manifest finalizer for the 2026-06-01 benchmark repair."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/01/README.md"
PACKET = ROOT / "papers/2026/06/_sources/daily-20260601"
AUDIT = PACKET / "MONTHLY_CONSERVATION_FRESH_AUDIT_V1.md"
MANIFEST = PACKET / "SHA256SUMS"
REQUIRED = {
    "SF-AGENT-OPERATING-SYSTEM",
    "SF-AIREP",
    "SF-FED-PERSONALIZATION-SILENT-FAILURES",
    "SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY",
}
EXPECTED_H2 = [
    "## Executive Summary", "## 1. Coverage", "## 2. Candidate Ledger",
    "## 3. Review Completion Receipt", "## 4. Benchmark Contracts",
    "## 5. Deep Analysis Selection", "## 6. Books Comparison",
    "## 7. Semantic Audit", "## 8. Ignored Noise",
    "## 9. Recommended Action", "## 10. Repository Changes",
    "## 11. Open Questions", "## 12. Sources", "## 13. Final Status",
]
FIELDS = (
    "Workload", "Model", "Hardware", "Precision", "Input Length",
    "Output Length", "Batch", "Concurrency", "SLO", "Evaluator",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_repair():
    path = ROOT / "scripts/repair_june01_semantic_audit.py"
    spec = importlib.util.spec_from_file_location("repair_june01", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main() -> None:
    repair = load_repair()
    text = REPORT.read_text(encoding="utf-8")
    assert [line for line in text.splitlines() if line.startswith("## ")] == EXPECTED_H2
    assert all(re.search(rf"^\*\*{re.escape(field)}:\*\*", text, re.MULTILINE) for field in (
        "Research Date", "Timezone", "Strict Window", "Contract", "Status",
    ))
    tables = []
    for marker in (
        repair.VALIDATOR.CANDIDATE_LEDGER_MARKER,
        repair.VALIDATOR.REVIEW_COMPLETION_MARKER,
        repair.VALIDATOR.BENCHMARK_MARKER,
        repair.VALIDATOR.DEEP_ANALYSIS_SELECTION_MARKER,
        repair.VALIDATOR.BOOKS_COMPARISON_MARKER,
    ):
        _, rows = repair.parse_table(text, marker)
        tables.append(rows)
    surfaces = [{row["Source Family ID"] for row in rows} for rows in tables]
    assert all(len(rows) == 40 for rows in tables)
    assert all(surface == surfaces[0] for surface in surfaces[1:])
    assert all(row["Benchmark Claim"] == "yes" for row in tables[0])

    benchmark_by_family = {row["Source Family ID"]: row for row in tables[2]}
    assert REQUIRED <= set(benchmark_by_family)
    for family in REQUIRED:
        row = benchmark_by_family[family]
        assert all(row[field] and (row[field] == "Not Disclosed" or not row[field].startswith("Not Disclosed")) for field in FIELDS)
    assert benchmark_by_family["SF-AGENT-OPERATING-SYSTEM"]["Workload"] == "Not Disclosed"
    assert benchmark_by_family["SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY"]["Workload"] == "Not Disclosed"
    assert "twelve representative" in benchmark_by_family["SF-FED-PERSONALIZATION-SILENT-FAILURES"]["Workload"]
    assert "conformance-kit" in benchmark_by_family["SF-AIREP"]["Workload"]

    disclosure = read_tsv(PACKET / "benchmark-disclosure-v9-retained.tsv")
    model_audit = read_tsv(PACKET / "benchmark-model-identity-audit-v9.tsv")
    assert len(disclosure) == len(model_audit) == 40
    assert {row["source_family_id"] for row in disclosure} == surfaces[0]
    assert {row["source_family_id"] for row in model_audit} == surfaces[0]
    disclosure_by_family = {row["source_family_id"]: row for row in disclosure}
    for family in REQUIRED:
        report_row = benchmark_by_family[family]
        packet_row = disclosure_by_family[family]
        assert [packet_row[field] for field in (
            "workload", "model", "hardware", "precision", "input_length",
            "output_length", "batch", "concurrency", "slo", "evaluator",
        )] == [report_row[field] for field in FIELDS]

    # Review bodies/RP identities and Books decisions are immutable surfaces.
    assert len(set(re.findall(r"\bRP-[0-9a-f]{16}\b", text))) == 40
    assert len(set(re.findall(r"<!-- review:([^:]+):start -->", text))) == 40
    assert len(set(re.findall(r"<!-- books-review:([^:]+):start -->", text))) == 40
    assert sum(row["Decision"] == "selected" for row in tables[3]) == 3
    assert sum(row["Decision"] == "Integrate" for row in tables[4]) == 4
    assert sum(row["Decision"] == "No Change — Existing Coverage" for row in tables[4]) == 36
    assert "40/40 benchmark contracts" in text and "MONTHLY_CONSERVATION_FRESH_AUDIT_V1.md" in text

    AUDIT.write_text(
        f"""# 2026-06-01 Monthly Conservation Fresh Audit V1

## Scope

Fresh-context audit of the monthly retained-surface conservation finding only. The frozen denominator, bounded Source Review bodies, Review Provenance identities, Score V2, Selection decisions, Books comparisons, shared Books, `docs/LEARNING_STATE.md`, and monthly indexes were immutable inputs.

## Finding and repair

- Before repair: Candidate=`40`, Review=`40`, Benchmark=`36`, Selection=`40`, Books=`40`.
- Root cause: `repair_june01_semantic_audit.py` filtered Benchmark rows by the historical `Benchmark Claim == yes` flag, while the canonical monthly contract requires a ten-field row for every retained family.
- Restored families: `{', '.join(sorted(REQUIRED))}`.
- Each restored row uses exact-v1 disclosed values where present and literal `Not Disclosed` for every undisclosed field; no task count was promoted to batch or concurrency.

## Result

- Set conservation: Candidate=Review=Benchmark=Selection=Books=`40/40`, with identical Source Family sets.
- Packet conservation: `benchmark-disclosure-v9-retained.tsv` and `benchmark-model-identity-audit-v9.tsv` are each `40/40` and set-equal to the Daily.
- Preserved Review surface: `40/40` bounded Review markers and `40/40` unique RP identities.
- Preserved Selection/Books: `3` selected; `4 Integrate + 36 No Change`; no shared Books write occurred.
- Canonical presentation: top fields `5/5`; canonical heading sequence preserved.
- Current Daily SHA-256: `{sha(REPORT)}`.
- Unresolved findings: `0`.

## Gate

Monthly conservation repair=`Passed`; Coverage=`Closed`, Evidence=`Passed`, Books=`Passed`, Completion=`Complete` remain unchanged.
""",
        encoding="utf-8",
    )

    files = sorted(path for path in PACKET.rglob("*") if path.is_file() and path != MANIFEST)
    files += [
        REPORT,
        ROOT / "scripts/repair_june01_semantic_audit.py",
        ROOT / "scripts/repair_june01_benchmark_conservation.py",
        ROOT / "scripts/migrate_june01_canonical_daily.py",
        ROOT / "scripts/normalize_june01_benchmark_contract.py",
        ROOT / "scripts/audit_june01_v9_downstream.py",
        ROOT / "scripts/test_june01_benchmark_conservation.py",
        Path(__file__).resolve(),
    ]
    MANIFEST.write_text(
        "".join(
            f"{sha(path)}  {Path(os.path.relpath(path, PACKET)).as_posix()}\n"
            for path in files
        ),
        encoding="utf-8",
    )
    print({"surfaces": 40, "restored": 4, "manifest_entries": len(files), "unresolved_findings": 0})


if __name__ == "__main__":
    main()
