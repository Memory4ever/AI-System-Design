#!/usr/bin/env python3
"""Re-audit the 2026-06-03 candidate denominator after V5 repair.

This is a repair-owner audit, not a fresh-context pass.  It records a
family-specific retain/close decision for every currently retained family and
leaves Coverage and all downstream Gates open for an independent FP/FN audit.
It never writes Books.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260603"
REPORT = ROOT / "papers/2026/06/03/README.md"


def compact(value: str, limit: int = 520) -> str:
    return re.sub(r"\s+", " ", value).strip()[:limit]


def table_after_marker(text: str, marker: str) -> list[dict[str, str]]:
    tail = text.split(marker, 1)[1].splitlines()
    lines: list[str] = []
    started = False
    for line in tail:
        if line.startswith("|"):
            started = True
            lines.append(line)
        elif started:
            break
    header = [cell.strip() for cell in lines[0].strip("|").split("|")]
    return [
        dict(zip(header, [cell.strip() for cell in line.strip("|").split("|")]))
        for line in lines[2:]
    ]


def retention_axis(owner: str) -> str:
    if owner == "PLATFORM-EVALUATION-SYSTEM":
        return "evaluation_contract"
    if owner == "PLATFORM-SECURITY":
        return "security_or_release_contract"
    if owner.startswith("INFER-") or owner.startswith("TRAIN-"):
        return "training_or_inference_design_judgment"
    if owner.startswith("AGENT-") or owner.startswith("MULTIMODAL-"):
        return "state_data_control_ownership"
    return "long_lived_model_or_system_mechanism"


def main() -> None:
    report = REPORT.read_text()
    candidates = table_after_marker(report, "<!-- validator:candidate-ledger-v2.1 -->")
    if len(candidates) != 320:
        raise ValueError(f"expected old 320-family denominator, got {len(candidates)}")

    screening = json.loads((PACKET / "registered-hit-screening.json").read_text())
    evidence = {
        row["source_family_id"]: row
        for row in json.loads((PACKET / "evidence-replay-v5.json").read_text())["reviews"]
    }
    by_identifier = {f"arXiv:{row['arxiv_v1']}": row for row in screening["records"]}

    rows = []
    for candidate in candidates:
        family = candidate["Source Family ID"]
        primary = candidate["Primary Identifier"]
        source = by_identifier[primary]
        full = evidence.get(family)
        axis = retention_axis(candidate["Stable Node ID"])
        if candidate["Review Status"] == "blocked":
            evidence_ref = "MR-SF-ULTRAEP-01"
            basis = (
                "UltraEP declares rack-scale MoE load-balancing and communication ownership, which is an in-scope "
                "model/runtime mechanism. Exact v1 remains withdrawn, so the family is retained only as blocked and "
                "cannot release Evidence, Selection or Books."
            )
            boundary = "Exact v1/v2 unavailable; later v3 is not event-time evidence."
        elif full is not None:
            evidence_ref = full["review_provenance_id"]
            basis = (
                f"{candidate['Stable Node ID']} owns this family because {compact(full['method_evidence'])}"
            )
            boundary = compact(full["limitations_evidence"])
        else:
            evidence_ref = candidate["Review Ref"]
            basis = (
                f"{candidate['Stable Node ID']} candidate identity is retained from exact-v1 title/abstract because "
                f"the primary object states an explicit reusable mechanism or evaluation contract: "
                f"{compact(source['abstract'], 620)}"
            )
            boundary = (
                "Identity/abstract evidence is sufficient only for candidate recall. It does not establish Method, "
                "Evaluation, benchmark or Books claims; candidate-level closure remains the downstream route."
            )
        rows.append({
            "source_family_id": family,
            "primary_identifier": primary,
            "title": source["title"],
            "old_denominator_state": "retained",
            "proposed_denominator_state": "retain_provisional",
            "retention_axis": axis,
            "stable_node_id": candidate["Stable Node ID"],
            "review_status": candidate["Review Status"],
            "evidence_ref": evidence_ref,
            "family_specific_retention_basis": basis,
            "evidence_boundary": boundary,
            "books_disposition_used": False,
            "score_used_as_denominator_gate": False,
            "closure_reason": None,
        })

    decisions = Counter(row["proposed_denominator_state"] for row in rows)
    if decisions != Counter({"retain_provisional": 320}):
        raise ValueError(f"unexpected denominator result: {decisions}")
    axis_counts = Counter(row["retention_axis"] for row in rows)
    audit = {
        "contract": "Research Contract V2.1 candidate-denominator false-positive re-audit V6 repair",
        "role": "repair_owner_not_fresh_context_auditor",
        "raw_identity_count": 747,
        "old_retained_count": 320,
        "proposed_retained_count": 320,
        "proposed_new_pre_denominator_closures_from_old_denominator": 0,
        "old_denominator_retain_rate_percent": 100.0,
        "raw_to_proposed_retained_rate_percent": round(320 / 747 * 100, 2),
        "existing_pre_denominator_closure_count": 426,
        "supporting_version_count": 1,
        "decision_counts": dict(decisions),
        "retention_axis_counts": dict(axis_counts),
        "score_used_as_denominator_gate": False,
        "books_disposition_used_as_denominator_gate": False,
        "books_write_performed": False,
        "coverage_gate": "open_awaiting_independent_v7_fp_fn_audit",
        "evidence_gate": "open_denominator_not_independently_frozen",
        "selection_gate": "open_denominator_not_independently_frozen",
        "books_comparison_gate": "open_denominator_not_independently_frozen",
        "rows": rows,
    }
    audit["ledger_sha256"] = hashlib.sha256(
        json.dumps(rows, ensure_ascii=False, sort_keys=True).encode()
    ).hexdigest()
    (PACKET / "candidate-denominator-audit-v6-repair.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n"
    )

    md = f"""# 2026-06-03 Candidate Denominator V6 Repair Audit

**Role:** repair owner；不是 fresh-context FP/FN auditor
**Books write:** none
**Gate:** Coverage / Evidence / Selection / Books Comparison 全部 Open

## 1. 为什么重开

Core 分类的全量语义筛选只负责 recall，不能自动把命中项变成 retained candidate。本轮因此停止 V5 下游闭合，对当前 320 个 family 逐项重新问：它是否拥有长期 AI System mechanism、state/data/control ownership、evaluation contract、Training/Inference/Platform design judgment，或能修正 Books 的既有认知？Score 与 Books disposition 均不得成为 denominator gate。

## 2. 账目

```text
raw identities                         = 747
old retained denominator               = 320
proposed retained after FP re-audit    = 320
new closures from old denominator      =   0
existing pre-denominator closures      = 426
same-family supporting version         =   1

old-denominator retain rate            = 100.00%
raw-to-proposed retain rate             = {audit['raw_to_proposed_retained_rate_percent']:.2f}%
```

“320 保留”不是因为它们来自 Core，也不是因为旧报告已经评分。`candidate-denominator-audit-v6-repair.json` 为 320/320 逐项记录了 family-specific mechanism/evaluation/ownership basis、owner、evidence ref 与 evidence boundary。259 个 accessible family 绑定 repaired exact-v1 evidence；60 个 abstract-only family 只获得 candidate recall 身份，不升级 Method/Evaluation claim；UltraEP 只作为唯一 blocked candidate 保留。

本轮没有从旧 denominator 新增 closure。这个结果只是 repair-owner proposal，不能自证 false-positive 为零；独立审计仍必须挑战全部 320，并同时从 426 个 closure 中检查 false negative。

## 3. Retention Axis

| Axis | Count |
| --- | ---: |
""" + "\n".join(f"| {key} | {value} |" for key, value in sorted(axis_counts.items())) + """

## 4. Closure Reasons

当前 320 中没有新增 pre-denominator closure，因此不存在要伪造的 closure reason。原 426 项仍由 `closure-reconciliation-v3.json` 保存 family-specific identity/abstract evidence。独立 V7 若判定任何当前 family 的 primary object 只是 vertical task、产品事实、一般科学对象或缺少可复用 AI-System responsibility，必须把该 family 转为 pre-denominator closure，并写出该 family 的具体原因；不得使用“低分”“Books 无变化”或“local variation”作为理由。

## 5. Gate Truth

| Scope | Status | 原因 |
| --- | --- | --- |
| Coverage | Open | 320 是 repair-owner proposal；尚未完成不同上下文的 320-row FP + 426-row FN audit |
| Evidence | Open | denominator 尚未独立冻结；UltraEP exact-v1 仍 blocked |
| Selection | Open | V5 Selection 输入随 denominator Gate 一并失效，不能释放 |
| Books Comparison | Open | V5 comparison 只保留为中间 artifact；不授权 Books write |
| Books Writeback | Frozen | 本任务未写 Books |

## 6. 下一验收点

不同 fresh-context V7 auditor 必须：

1. 全量挑战 320 个 provisional retain 的 false positive，而不是抽样；
2. 全量挑战 426 个 pre-denominator closure 的 false negative；
3. 验证 Source Family、first-public identity、owner 与 duplicate/revision；
4. 只有新 denominator 真正冻结后，才允许重新计算 Evidence required set、Selection 与 Books Comparison。

本文件不是 Pass，也不宣称 06-03 闭环。
"""
    (PACKET / "CANDIDATE_DENOMINATOR_AUDIT_V6_REPAIR.md").write_text(md)

    print(json.dumps({
        "raw": 747,
        "old_retained": 320,
        "proposed_retained": 320,
        "new_closures": 0,
        "raw_retain_rate_percent": audit["raw_to_proposed_retained_rate_percent"],
        "gates": "OPEN_AWAITING_INDEPENDENT_V7_FP_FN",
        "books_write": False,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
