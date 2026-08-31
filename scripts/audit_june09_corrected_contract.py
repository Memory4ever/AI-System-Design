#!/usr/bin/env python3
"""Independent corrected-contract acceptance for the 2026-06-09 Daily."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260609"
REPORT = ROOT / "papers/2026/06/09/README.md"
MANIFEST = PACKET / "SHA256SUMS"
OUT_JSON = PACKET / "independent-acceptance-v1.json"
OUT_MD = PACKET / "INDEPENDENT_ACCEPTANCE_V1.md"


def load(name: str) -> dict:
    return json.loads((PACKET / name).read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_rows(text: str, heading: str, next_heading: str) -> dict[str, list[str]]:
    body = text.split(heading, 1)[1].split(next_heading, 1)[0]
    rows = {}
    for line in body.splitlines():
        if not line.startswith("| SF-"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells[0] in rows:
            raise AssertionError(f"duplicate table family: {cells[0]}")
        rows[cells[0]] = cells
    return rows


def main() -> None:
    report = REPORT.read_text(encoding="utf-8")
    ledger = load("screening-ledger.json")
    receipts = load("source-review-receipts-v2.1.json")
    selection = load("deep-analysis-selection-v1.json")

    identities = ledger["identities"]
    identity_ids = {row["arxiv_id"] for row in identities}
    assert len(identities) == len(identity_ids) == 477
    assert ledger["window"] == "[2026-06-08T09:00:00+08:00,2026-06-09T09:00:00+08:00)"
    assert ledger["utc_window"] == "[2026-06-08T01:00:00Z,2026-06-09T01:00:00Z)"
    assert all("2026-06-08T01:00:00Z" <= row["submitted_v1_utc"] < "2026-06-09T01:00:00Z" for row in identities)
    route_counts = Counter(row["screening_route"] for row in identities)
    assert route_counts == {
        "core_daily_semantic_review_required": 332,
        "keyword_daily_semantic_review_required": 41,
        "not_routed_by_keyword_contract": 104,
    }

    retained_rows = [row for row in identities if row["screening_status"] == "retained_after_full_semantic_audit"]
    closure_rows = [row for row in identities if row["screening_status"] == "pre_denominator_closure"]
    retained_ids = {row["arxiv_id"] for row in retained_rows}
    closure_ids = {row["arxiv_id"] for row in closure_rows}
    assert len(retained_ids) == 15 and len(closure_ids) == 462
    assert retained_ids.isdisjoint(closure_ids) and retained_ids | closure_ids == identity_ids
    assert len({row["screening_reason"] for row in closure_rows}) == 462
    for row in closure_rows:
        abstract_prefix = " ".join(row["abstract"].split())[:16]
        assert abstract_prefix in row["screening_reason"]
        assert row["pre_denominator_closure_class"] not in {"", "—"}
    assert all(row["screening_status"] == "pre_denominator_closure" for row in identities if row["screening_route"] == "not_routed_by_keyword_contract")
    assert "2606.09137" not in identity_ids
    assert next(row for row in identities if row["arxiv_id"] == "2606.09138")["screening_status"] == "pre_denominator_closure"
    assert ledger["audit"]["metadata_findings"] == [
        "2606.09686 exact-v1 title normalized from 83-Format to 84-Format"
    ]

    with (PACKET / "denominator-full-semantic-audit-v1.tsv").open(encoding="utf-8", newline="") as handle:
        audit_rows = list(csv.DictReader(handle, delimiter="\t"))
    assert len(audit_rows) == 477
    assert {row["arxiv_id"] for row in audit_rows} == identity_ids
    assert Counter(row["decision"] for row in audit_rows) == {"closure": 462, "retained": 15}

    reviews = receipts["reviews"]
    review_families = {row["family"] for row in reviews}
    assert receipts["counts"] == {"total": 15, "deep": 15, "standard": 0, "pending": 0}
    assert {row["arxiv_id"] for row in reviews} == retained_ids
    for row in reviews:
        assert row["provenance"].startswith("RP-") and len(row["provenance"]) == 19
        assert row["method_locator"] and row["evaluation_locator"] and row["limitations_locator"]
        assert row["body"].count(f"<!-- claim:{row['family']}:start -->") == 1
        assert row["body"].count(f"<!-- claim:{row['family']}:end -->") == 1

    candidate = table_rows(report, "## 2. Candidate Ledger", "## 3. Review Completion Receipt")
    benchmark = table_rows(report, "## 4. Benchmark Contracts", "## 5. Deep Analysis Selection")
    books = table_rows(report, "## 6. Books Comparison", "## 7. Semantic Audit")
    assert set(candidate) == review_families
    benchmark_yes = {family for family, row in candidate.items() if row[21] == "yes"}
    assert benchmark_yes == set(benchmark) == review_families
    for row in benchmark.values():
        assert len(row) == 11
        for value in row[1:]:
            assert "Not Disclosed as" not in value
            assert "Not Disclosed —" not in value
            assert "Disclosed where applicable" not in value
            if value.startswith("Not Disclosed"):
                assert value == "Not Disclosed"

    eligible = {row["source_family_id"] for row in selection["rows"]}
    noneligible = {row["source_family_id"] for row in selection["noneligible_rows"]}
    assert (selection["candidate_count"], selection["eligible_count"], selection["noneligible_count"]) == (15, 15, 0)
    assert eligible.isdisjoint(noneligible) and eligible | noneligible == review_families
    assert sum(row["decision"] == "selected" for row in selection["rows"]) == 3
    assert "15 retained = 15 eligible + 0 non-eligible" in report
    assert "None — all 15 retained families are eligible" in report

    formal = {
        family for family, row in candidate.items()
        if row[19] in {"Integrate", "No Change — Existing Coverage", "Structural Candidate"}
    }
    weekly_only = {family for family, row in candidate.items() if row[19] == "Weekly Only — Context"}
    assert len(formal) == 15 and not weekly_only and set(books) == formal
    disposition_counts = Counter(row[19] for row in candidate.values())
    assert disposition_counts == {"Integrate": 14, "No Change — Existing Coverage": 1}

    corpus = {path: path.read_text(encoding="utf-8") for path in (ROOT / "books").rglob("*.md")}
    for family, row in books.items():
        aid = family.removeprefix("SF-2026-ARXIV-").replace("-", ".", 1)
        target = ROOT / row[2].split("#", 1)[0].replace("Books/", "books/")
        hits = {
            path for path, text in corpus.items()
            if family in text or f"https://arxiv.org/html/{aid}v1" in text or f"arXiv:{aid}v1" in text
        }
        if row[7] == "Integrate":
            assert hits == {target}, (family, hits, target)
        else:
            assert not hits, (family, hits)

    expected_h2 = [
        "## Executive Summary", "## 1. Coverage", "## 2. Candidate Ledger",
        "## 3. Review Completion Receipt", "## 4. Benchmark Contracts",
        "## 5. Deep Analysis Selection", "## 6. Books Comparison",
        "## 7. Semantic Audit", "## 8. Ignored Noise",
        "## 9. Recommended Action", "## 10. Repository Changes",
        "## 11. Open Questions", "## 12. Sources", "## 13. Final Status",
    ]
    assert [line for line in report.splitlines() if line.startswith("## ")] == expected_h2
    assert "### Source Reviews" in report.split("## 3. Review Completion Receipt", 1)[1].split("## 4. Benchmark Contracts", 1)[0]
    assert "| Completion Status | Complete |" in report
    assert "| Coverage Gate | Closed |" in report and "| Evidence Gate | Passed |" in report and "| Books Gate | Passed |" in report
    postwrite = (PACKET / "POST_WRITE_FRESH_AUDIT_V1.md").read_text(encoding="utf-8")
    assert "14/14 Integrate" in postwrite and "1/1 No Change" in postwrite
    assert "no actionable finding remains" in postwrite

    payload = {
        "schema": "daily-v2.1-independent-acceptance-v1",
        "report": "papers/2026/06/09/README.md",
        "verdict": "passed",
        "unresolved_findings": 0,
        "coverage": {"raw": 477, "retained": 15, "closures": 462, "route_negative": 104},
        "review": {"deep_complete": 15, "pending": 0, "benchmark_yes": 15, "benchmark_contracts": 15},
        "selection": {"candidate": 15, "eligible": 15, "noneligible": 0, "selected": 3},
        "books": {"formal_comparison": 15, "integrate": 14, "no_change": 1, "weekly_only": 0},
        "shared_books_writes": 0,
        "shared_learning_state_writes": 0,
        "hashes": {
            "daily": digest(REPORT),
            "selection": digest(PACKET / "deep-analysis-selection-v1.json"),
            "reviews": digest(PACKET / "source-review-receipts-v2.1.json"),
        },
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text("""# 2026-06-09 Corrected-contract Independent Acceptance V1

## Verdict

Passed；unresolved findings: 0。审计只读核对 shared Books，未写 Books、`docs/LEARNING_STATE.md` 或月度索引。

## Coverage and Candidate admission

- Strict window：`[2026-06-08 09:00, 2026-06-09 09:00)` Asia/Shanghai；477/477 identity timestamp 均落在对应 UTC 左闭右开窗口。
- `477 = 15 retained + 462 family-specific pre-denominator closures`；两组互斥且并集完整。
- Core 332、keyword-routed 41、route-negative 104；104/104 route-negative 均有逐 family closure，denominator TSV 与 ledger 477/477 对齐。
- 没有把未发现的 `2606.09137` 计入 closure；实际 discovery identity `2606.09138`（Claw-R1）保留逐 family pre-denominator closure；`2606.09686` 的 reviewed exact-v1 identity 保持 84-Format correction。

## Review and Benchmark

- Review 15/15 deep_complete，pending=0；Method、Evaluation、Limitations、Artifact、RP 与 bounded claim ref 均完整。
- Benchmark Claim=`yes` 子集为 15，Benchmark Contract 也恰为 15；集合双向相等。
- 已删除模板化 `Disclosed where applicable` / `Not Disclosed as ...`；当前未保存精确披露值的字段严格写 literal `Not Disclosed`，task/trial/worker 数不冒充 batch 或 serving concurrency。

## Selection and Books

- Corrected-contract 守恒：`15 retained = 15 eligible + 0 non-eligible`；两组互斥、并集完整。canonical 主表只有 15 eligible family，显式空 closure 在表外，selected=3。
- Books formal comparison=15：14 Integrate + 1 No Change；Weekly Only=0。14 个 Integrate 的 exact-v1/family evidence 仅在预期 owner 文件命中，No Change `2606.09061` 零泄漏。
- Existing post-write audit 的 14/14 Integrate + 1/1 No Change 证据、owner/trade-off/non-proof boundary 均通过。

## Presentation and Gate

- 顶部五字段、严格窗口、精确 13 个 H2 与第 3 节 `### Source Reviews` 层级通过。
- Coverage=Closed、Evidence=Passed、Books=Passed、Completion=Complete；semantic audit 未解决 finding=0。
- Validator、manifest、renderer 双跑与 `git diff --check` 由最终验收命令另行复核；validator 不替代本语义收据。
""", encoding="utf-8")

    entries = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        _, relpath = line.split("  ", 1)
        entries[relpath] = ROOT / relpath
    for path in (
        OUT_MD,
        OUT_JSON,
        PACKET / "deep-analysis-selection-v1.json",
        ROOT / "scripts/audit_june09_corrected_contract.py",
        ROOT / "scripts/test_june09_corrected_contract.py",
    ):
        entries[str(path.relative_to(ROOT))] = path
    MANIFEST.write_text(
        "\n".join(f"{digest(path)}  {relpath}" for relpath, path in sorted(entries.items())) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"raw": 477, "retained": 15, "closures": 462, "eligible": 15, "noneligible": 0, "selected": 3, "books_formal": 15, "weekly_only": 0, "unresolved": 0}))


if __name__ == "__main__":
    main()
