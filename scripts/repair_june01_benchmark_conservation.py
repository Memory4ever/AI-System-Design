#!/usr/bin/env python3
"""Restore claim-scoped 2026-06-01 benchmark conservation."""

from __future__ import annotations

import csv
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/01/README.md"
PACKET = ROOT / "papers/2026/06/_sources/daily-20260601"
NON_BENCHMARK = {
    "SF-FED-PERSONALIZATION-SILENT-FAILURES": "Landscape/research-vision evidence only; no newly executed model benchmark.",
    "SF-AIREP": "Schema/conformance/neutrality checks only; no author-controlled empirical model benchmark.",
    "SF-AGENT-OPERATING-SYSTEM": "Architecture and evaluation criteria only; no executed evaluator or benchmark result.",
    "SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY": "Position/architecture agenda only; the empirical testbed remains future work.",
}


def load_repair():
    path = ROOT / "scripts/repair_june01_semantic_audit.py"
    spec = importlib.util.spec_from_file_location("repair_june01", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def render_audit() -> str:
    boundaries = "\n".join(f"- `{family}` — {boundary}" for family, boundary in NON_BENCHMARK.items())
    return f"""# 2026-06-01 Benchmark Claim Conservation Fresh Audit V1

## Scope

Fresh-context, full-population audit of the frozen 40-family Candidate Ledger and the claim-scoped Benchmark Contracts surface. Books, `docs/LEARNING_STATE.md`, and the monthly index were read-only.

## Conservation Result

- Candidate Ledger: 40 unique families.
- Benchmark Claim=yes: 36 unique families.
- Benchmark Claim=no: 4 unique families.
- Benchmark Contracts: 36 unique rows.
- Bidirectional set check: the Benchmark Contract family set exactly equals the Candidate Ledger `Benchmark Claim=yes` set.
- Review Completion, Selection, and Books Comparison remain 40/40; Selection remains 3 selected + 37 not_selected; Books remains 4 Integrate + 36 No Change.

## Restored Non-Benchmark Families

{boundaries}

These families remain retained because their durable system mechanisms or ownership contracts survive Evidence and Books review. Retention does not imply an empirical benchmark claim, and no ten-field benchmark row is synthesized for them.

## Fresh Audit

- Renderer guard: the semantic owner explicitly freezes these four families to `Benchmark Claim=no` and emits rows only for Claim=yes families.
- Regression guard: the test requires 40 candidates, 36 yes, 4 no, 36 rows, exact set equality, and zero leakage from the four-family no set.
- Exact-v1 Evidence, Review bodies, Score V2, Selection rationales, and Books dispositions were not changed by this repair.
- Cross-model review: skipped in this non-interactive child lane; the result is instead guarded by deterministic full-population assertions and a fresh closure audit.
- Unresolved findings: 0.

## Gate

Evidence remains Passed only under the restored claim-scoped contract. Completion remains Complete.
"""


def main() -> None:
    repair = load_repair()
    text = REPORT.read_text(encoding="utf-8")
    candidate_headers, candidates = repair.parse_table(text, repair.VALIDATOR.CANDIDATE_LEDGER_MARKER)
    benchmark_headers, benchmarks = repair.parse_table(text, repair.VALIDATOR.BENCHMARK_MARKER)
    candidate_ids = [row["Source Family ID"] for row in candidates]
    assert len(candidate_ids) == len(set(candidate_ids)) == 40
    assert set(NON_BENCHMARK) <= set(candidate_ids)

    benchmark_by_family = {row["Source Family ID"]: row for row in benchmarks}
    assert set(benchmark_by_family) <= set(candidate_ids)
    for candidate in candidates:
        family = candidate["Source Family ID"]
        candidate["Benchmark Claim"] = "no" if family in NON_BENCHMARK else "yes"
    yes_ids = {row["Source Family ID"] for row in candidates if row["Benchmark Claim"] == "yes"}
    assert len(yes_ids) == 36
    assert yes_ids <= set(benchmark_by_family), "cannot restore a missing legitimate benchmark row"
    benchmarks = [benchmark_by_family[family] for family in candidate_ids if family in yes_ids]
    assert len(benchmarks) == 36

    text = repair.replace_table(text, repair.VALIDATOR.CANDIDATE_LEDGER_MARKER, candidate_headers, candidates)
    text = repair.replace_table(text, repair.VALIDATOR.BENCHMARK_MARKER, benchmark_headers, benchmarks)
    replacements = {
        "all 40 benchmark contracts": "all 36 Benchmark Claim=yes contracts",
        "40/40 benchmark contracts": "36/36 Benchmark Claim=yes contracts",
        "`40/40` benchmark contracts": "`36/36` Benchmark Claim=yes contracts",
        "40 项 Books Comparison 与 40 项 benchmark contract": "40 项 Books Comparison 与 36 项 Benchmark Claim=yes contract",
        "归一原有 36 条并补齐 4 条 benchmark contract": "归一 36 条 Benchmark Claim=yes contract",
        "Re-audited all 40 Reviews/scores and all 40 benchmark contracts after rewriting 18 bodies; RP receipts recomputed, FED/SABER truncation removed, and no unresolved model/hardware/precision/batch/SLO or exact-v1 locator finding remains; receipt `fresh-context-downstream-audit-independent-v10.md`": "Re-audited all 40 Reviews/scores and all 36 Benchmark Claim=yes contracts after rewriting 18 bodies; RP receipts recomputed, FED/SABER truncation removed, and no unresolved model/hardware/precision/batch/SLO or exact-v1 locator finding remains; receipts `fresh-context-downstream-audit-independent-v10.md` and `MONTHLY_CONSERVATION_FRESH_AUDIT_V1.md`",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = text.replace(
        "原有 36 个 benchmark contract 和 371=40+331 accounting；月度守恒修复随后补齐并复核四个漏项，使 retained Benchmark surface 达到 40/40。",
        "36 个 Benchmark Claim=yes contract 和 371=40+331 accounting；月度守恒复核确认其余四个 retained family 为 Benchmark Claim=no。",
    )
    text = text.replace(
        "原有 36 个 benchmark contract 与 40-family selection frontier 的审计；月度守恒修复又逐项补齐并复核四个 retained benchmark contract，最终五个 retained surfaces 均为 40/40。",
        "36 个 Benchmark Claim=yes contract 与 40-family selection frontier 的审计；月度守恒复核确认另外四个 retained family 没有 empirical benchmark claim，因此不生成 benchmark row。",
    )
    source_anchor = "- Standard post-write closure receipt: `papers/2026/06/_sources/daily-20260601/POST_WRITE_FRESH_AUDIT_V1.md`"
    monthly_source = "- Benchmark-claim conservation fresh audit: `papers/2026/06/_sources/daily-20260601/MONTHLY_CONSERVATION_FRESH_AUDIT_V1.md`"
    if monthly_source not in text:
        text = text.replace(source_anchor, source_anchor + "\n" + monthly_source)
    REPORT.write_text(text, encoding="utf-8")

    disclosure_path = PACKET / "benchmark-disclosure-v9-retained.tsv"
    disclosure_fields, disclosure_rows = read_tsv(disclosure_path)
    disclosure_by_family = {row["source_family_id"]: row for row in disclosure_rows}
    assert yes_ids <= set(disclosure_by_family)
    write_tsv(disclosure_path, [disclosure_by_family[family] for family in candidate_ids if family in yes_ids], disclosure_fields)

    model_path = PACKET / "benchmark-model-identity-audit-v9.tsv"
    model_fields, model_rows = read_tsv(model_path)
    model_by_family = {row["source_family_id"]: row for row in model_rows}
    assert yes_ids <= set(model_by_family)
    write_tsv(model_path, [model_by_family[family] for family in candidate_ids if family in yes_ids], model_fields)

    packet_readme_path = PACKET / "README.md"
    packet_readme = packet_readme_path.read_text(encoding="utf-8")
    packet_readme = packet_readme.replace("40 benchmark contracts", "36 Benchmark Claim=yes contracts")
    packet_readme_path.write_text(packet_readme, encoding="utf-8")
    (PACKET / "MONTHLY_CONSERVATION_FRESH_AUDIT_V1.md").write_text(render_audit(), encoding="utf-8")

    assert {row["Source Family ID"] for row in benchmarks} == yes_ids
    print("candidate=40 review=40 benchmark_yes=36 benchmark_no=4 benchmark_rows=36 selection=40 books=40 restored_no=4")


if __name__ == "__main__":
    main()
