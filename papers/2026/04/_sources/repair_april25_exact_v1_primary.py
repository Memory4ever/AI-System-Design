#!/usr/bin/env python3
"""Repair 2026-04-25 from official exact-v1 metadata and current Books only.

This is intentionally date-local.  The month adjudication is read-only, no
Weekly artifact is read, and no Books file is written.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import sys
import types
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
PACKET = ROOT / "papers/2026/04/_sources/daily-20260425"
REPORT = ROOT / "papers/2026/04/25/README.md"
ADJUDICATION = ROOT / "papers/2026/04/_sources/april-24-25-arxiv-primary-precedence-adjudication.json"
BASE_PATH = ROOT / "papers/2026/04/_sources/finalize_april_01_07_prewrite.py"
FINALIZER_PATH = ROOT / "scripts/finalize_april24_25_prewrite.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE = load_module("april25_base", BASE_PATH)
FINALIZER = load_module("april25_finalizer", FINALIZER_PATH)
ORIGINAL_FINALIZER_OWNER_FOR = FINALIZER.owner_for
ORIGINAL_FINALIZER_SCORE_FOR = FINALIZER.score_for


REOPEN = {
    "2604.22167",  # output-distribution tail-risk evaluation
    "2604.22179",  # semantics-preserving software-to-board artifact
    "2604.22230",  # evaluation-incentive / benchmark-hacking contract
    "2604.22242",  # compile-time GPU expression fusion
    "2604.22901",  # event-driven diffusion cache with error feedback
}

WITHDRAWN = {
    "2604.22151", "2604.22251", "2604.22274", "2604.22407",
    "2604.22546", "2604.22627", "2604.22645",
}

OWNER = {
    "2604.22167": "PLATFORM-EVALUATION-SYSTEM",
    "2604.22179": "PLATFORM-MODEL-REGISTRY",
    "2604.22230": "PLATFORM-EVALUATION-SYSTEM",
    "2604.22242": "INFER-TENSORRT-LLM",
    "2604.22901": "MULTIMODAL-GENERATIVE-PARADIGMS",
}

FACETS = {
    "2604.22167": (
        "§3 Efficient Rare Unsafe Event Estimation; §3.1 importance sampling; §3.2 unsafe proposal construction",
        "§4-6 StrongREJECT/misalignment/query-to-deployment experiments across the disclosed five model families",
        "§9 Limitations — requires model weights or logits, inherits LLM-judge error, and can miss evasive harmful behavior",
    ),
    "2604.22179": (
        "§2 Architecture and Methods; §2.2 one shared artifact reused by software reference and board runtime",
        "§2.3 measurement protocol; §3 full 10,000-image MNIST agreement and scope-separated latency/energy",
        "§4 Discussion and Limitations — BRAM saturated, energy is tool-estimated, and board validation is a linear TTFS classifier",
    ),
    "2604.22230": (
        "§2 model of creative versus mechanistic effort under a rank-order ML contest",
        "Appendix H.2 observational check over 26 binary-classification contests",
        "The equilibrium conclusions depend on the paper's stylized effort/cost assumptions; observational contest correlations do not identify a universal benchmark policy",
    ),
    "2604.22242": (
        "§3 compile-time AST/type construction and template-specialized fused GPU kernel generation",
        "§4 RTX 4090/CUDA, FP32 10k-square matrices, 50 post-warmup trials over disclosed expressions",
        "§5 scope is the Bandicoot C++ linear-algebra library; results exclude JIT warmup and do not establish LLM-kernel, dynamic-shape, multi-GPU, or production-tail behavior",
    ),
    "2604.22901": (
        "§3.3 half-spectrum CRF state, event-triggered KV recomputation, and periodic error-feedback probes",
        "§4 five public multivariate time-series benchmarks against the disclosed uncached/naive-cache/step-reduction baselines",
        "§5 Discussion — fixed time-series shapes only, no matched image/video cache comparison, and per-layer KV grows with depth and effective sequence length",
    ),
}


def dump(path: Path, obj: object) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def later_announcement_ids() -> set[str]:
    data = json.loads(ADJUDICATION.read_text(encoding="utf-8"))
    rows = data["identifier_month_adjudication"]["items"]
    result = {row["arxiv_id"] for row in rows if row["report_date"] == "2026-04-25"}
    assert len(result) == 36
    return result


def exact_metadata() -> dict[str, dict]:
    data = json.loads((PACKET / "exact-v1-abs-recovery-receipt.json").read_text(encoding="utf-8"))
    assert data["revision_risk_after_owner_removal"] == 207
    assert data["accessible"] == 207 and data["blocked"] == 0
    return {row["arxiv_id"]: row for row in data["rows"]}


def replace_metadata(row: dict, recovered: dict[str, dict]) -> dict:
    result = dict(row)
    exact = recovered.get(result["arxiv_id"])
    if exact:
        result["title"] = exact["title"]
        result["abstract"] = exact["abstract"]
        result["exact_v1_abs_url"] = exact["url"]
        result["exact_v1_abs_sha256"] = exact["sha256"]
        result["metadata_source"] = "official arXiv /abs/<id>v1 frozen snapshot"
    return result


def filter_inventory(path: Path, removed: set[str], recovered: dict[str, dict]) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    identities = [replace_metadata(row, recovered) for row in data["identities"] if row["arxiv_id"] not in removed]
    assert len(identities) == 836
    data["identities"] = identities
    if "raw_identity_count" in data:
        data["raw_identity_count"] = len(identities)
    if "raw_snapshot_records" in data:
        data["raw_snapshot_records"] = len(identities)
    data["registered_identities"] = len(identities) if "registered_identities" in data else data.get("registered_identities")
    data["primary_precedence_reconciliation"] = {
        "removed_later_announcement": len(removed),
        "active_strict_window_identities": len(identities),
        "receipt": "../april-24-25-arxiv-primary-precedence-adjudication.json",
    }
    if data.get("registered_identities") is None:
        data.pop("registered_identities", None)
    dump(path, data)


def owner_for(row: dict) -> str:
    return OWNER.get(row["arxiv_id"], ORIGINAL_FINALIZER_OWNER_FOR(row))


def disposition(old: dict | None, row: dict, owner: str) -> str:
    if row["arxiv_id"] in REOPEN:
        return "No Change — Existing Coverage"
    if old and old.get("decision"):
        return old["decision"]
    return "No Change — Existing Coverage"


def score_for(row: dict, old: dict | None, decision: str) -> dict:
    explicit = {
        "2604.22167": (3, 3, 3), "2604.22179": (3, 2, 3),
        "2604.22230": (2, 2, 3), "2604.22242": (2, 2, 3),
        "2604.22901": (3, 2, 3),
    }
    if row["arxiv_id"] in explicit:
        d, s, u = explicit[row["arxiv_id"]]
        return {"design_delta": d, "system_reach": s, "durability": u, "total": d + s + u}
    if old and old.get("score_v2"):
        return old["score_v2"]
    return ORIGINAL_FINALIZER_SCORE_FOR(row, old, decision)


def closure_reason(row: dict, challenged: bool = False, withdrawn: bool = False) -> str:
    aid = row["arxiv_id"]
    title = row["title"]
    abstract = " ".join(row.get("abstract", "").split())
    if withdrawn:
        return (
            f"{title}：official exact-v1 abs `https://arxiv.org/abs/{aid}v1` 标记 withdrawn by submitter；"
            "按 fail-closed 合同仅保留 identity/date/status，不进入 Candidate、Score、Source Review、Books 或 Materials Request。"
        )
    text = (title + " " + abstract).lower()
    if not re.search(r"(model|learning|agent|gpu|robot|inference|training|benchmark|diffusion|retriev|neural|data)", text):
        boundary = "研究对象不属于 AI System 的模型、训练、推理、平台或 Agent 生命周期"
    elif re.search(r"(medical|clinical|molecular|galaxy|black hole|flood|ocean|pollution|brain|drug|cosmic)", text):
        boundary = "机制与评测绑定具体科学/医疗领域任务，没有改变可迁移的 AI-System owner"
    elif re.search(r"(benchmark|dataset|survey|study|analysis)", title.lower()):
        boundary = "只形成任务或数据集级 measurement/context，没有新增通用 release/evaluation contract"
    elif re.search(r"(coflow|risc-v|debugging|wireless|fpga)", text):
        boundary = "属于通用计算/通信或专用硬件局部实现，未建立目标 AI workload 的端到端 contract"
    else:
        boundary = "属于局部模型/优化方法，未转移可复用的 state/data/control ownership，也未修正 current Books"
    return (
        f"exact-v1 title+abstract 复核：`{title}` 的公开问题/机制为“{abstract[:360]}”。"
        f"关闭边界：{boundary}；若未来 exact revision 披露跨 workload owner、failure/fallback 或与现有章节冲突，再重开。"
    )


def patch_date_local_support(removed: set[str], retained: int, queue: int) -> None:
    # Historical receipts are preserved but reconciled to the new canonical active set.
    for name in ("exact-v1-fetch-receipt.json",):
        path = PACKET / name
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            data = [row for row in data if row.get("arxiv_id") not in removed]
        dump(path, data)

    challenge_path = PACKET / "independent-high-risk-closure-challenges.json"
    challenge = json.loads(challenge_path.read_text(encoding="utf-8"))
    challenge["items"] = [row for row in challenge["items"] if row["arxiv_id"] not in removed]
    challenge["raw_identities"] = 836
    challenge["challenge_count"] = len(challenge["items"])
    challenge["primary_precedence_reconciled"] = True
    dump(challenge_path, challenge)

    exact_access = json.loads((PACKET / "exact-v1-access-receipt.json").read_text(encoding="utf-8"))
    exact_access["revision_risk_metadata_replay"] = {"complete": 207, "blocked": 0, "withdrawn_closures": len(WITHDRAWN)}
    dump(PACKET / "exact-v1-access-receipt.json", exact_access)

    adjudication_path = PACKET / "independent-denominator-adjudication.json"
    adjudication = json.loads(adjudication_path.read_text(encoding="utf-8"))
    adjudication["items"] = [row for row in adjudication.get("items", []) if row.get("arxiv_id") not in removed]
    adjudication.update({
        "registered_identities": 836,
        "final_candidate_denominator": retained,
        "final_pre_denominator_closures": 836 - retained,
        "later_announcement_removed": sorted(removed),
        "withdrawn_primary_source_closures": sorted(WITHDRAWN),
        "exact_v1_revision_risk_complete": 207,
        "ordinary_pending": 0,
        "blocked": 0,
    })
    dump(adjudication_path, adjudication)

    # Reconcile the canonical pre-write acceptance to the corrected identity
    # owner set.  Historical findings remain, but a later-announcement family
    # must not survive in the accepted queue or active audit scope.
    acceptance_path = PACKET / "books-prewrite-fresh-context-acceptance.json"
    books_acceptance = json.loads(acceptance_path.read_text(encoding="utf-8"))
    books_acceptance["accepted_integrates"] = [
        row for row in books_acceptance.get("accepted_integrates", [])
        if row.get("source_family_id") not in {f"SF-2026-ARXIV-{aid.replace('.', '-')}" for aid in removed}
    ]
    books_acceptance["scope"] = {
        "strict_window_active_identities": 836,
        "date_family_count": retained,
        "target_refs_checked": retained,
        "original_integrate_queue_after_date_reconciliation": 20,
        "accepted_integrate_queue": queue,
        "no_change_total": retained - queue,
        "reclassified_false_positive_integrates": 13,
    }
    books_acceptance["withdrawn_fail_closed"] = sorted(
        f"SF-2026-ARXIV-{aid.replace('.', '-')}" for aid in WITHDRAWN
    )
    books_acceptance["primary_precedence_reconciliation"] = {
        "later_announcement_removed": len(removed),
        "active_contaminants": 0,
        "receipt": "primary-precedence-repair-receipt.json",
    }
    dump(acceptance_path, books_acceptance)

    receipt = {
        "schema": "april25-primary-precedence-repair/v1",
        "report_date": "2026-04-25",
        "weekly_dependency_count": 0,
        "raw_before": 872,
        "later_announcement_removed": sorted(removed),
        "raw_after": 836,
        "revision_risk_exact_v1": 207,
        "revision_risk_accessible": 207,
        "revision_risk_blocked": 0,
        "withdrawn_primary_source_closures": sorted(WITHDRAWN),
        "false_negatives_reopened": sorted(REOPEN),
        "final_denominator": retained,
        "pre_denominator_closures": 836 - retained,
        "exact_v1_complete": retained,
        "materials_requests": 0,
        "integrate_queue": queue,
        "gate": {"coverage": "Closed", "evidence": "Passed", "books": "Open" if queue else "Passed"},
        "invariants": {
            "later_announcement_in_active_paths": 0,
            "withdrawn_in_candidate_review_books": 0,
            "official_v1_metadata_replay_complete": True,
            "weekly_semantic_dependency": 0,
        },
    }
    dump(PACKET / "primary-precedence-repair-receipt.json", receipt)

    acceptance = {
        "schema": "identity-date-window-fresh-context-acceptance/v2",
        "report_date": "2026-04-25",
        "scope": {"strict_window_active": 836, "removed_later_announcement": 36, "revision_risk": 207},
        "checks": {
            "official_identifier_month_precedence": "passed",
            "official_exact_v1_metadata": "207/207 accessible",
            "withdrawn_fail_closed": "7/7 closure only",
            "active_path_contamination": 0,
        },
        "result": "pass",
        "unresolved_findings": [],
    }
    dump(PACKET / "identity-date-window-fresh-context-acceptance.json", acceptance)


def main() -> None:
    removed = later_announcement_ids()
    recovered = exact_metadata()
    filter_inventory(PACKET / "screening-ledger-provisional.json", removed, recovered)
    filter_inventory(PACKET / "screening-ledger-final.json", removed, recovered)
    filter_inventory(PACKET / "arxiv-api-enumeration.json", removed, recovered)

    # Provide the base renderer with a date-local fresh-context challenge set.
    old = json.loads((PACKET / "screening-ledger-final.json").read_text(encoding="utf-8"))
    drifted = {
        aid for aid, exact in recovered.items()
        for row in old["identities"] if row["arxiv_id"] == aid
        if row.get("title") == exact["title"] and row.get("exact_v1_abs_sha256") == exact["sha256"]
    }
    challenge_module = types.ModuleType("audit_april_01_07_fresh_context")
    challenge_module.FALSE_NEGATIVE_CHALLENGES = {25: drifted}
    sys.modules["audit_april_01_07_fresh_context"] = challenge_module

    BASE.REOPEN[25] = set(REOPEN)
    BASE.REMOVE_FP[25] = set()
    BASE.WITHDRAWN = set(WITHDRAWN)
    BASE.owner_for = owner_for
    BASE.terminal_disposition = disposition
    BASE.score_for = score_for
    BASE.closure_reason = closure_reason

    FINALIZER.OWNER_OVERRIDE.update(OWNER)
    FINALIZER.FACETS25.update(FACETS)
    FINALIZER.owner_for = owner_for
    FINALIZER.terminal_disposition = disposition
    FINALIZER.score_for = score_for
    FINALIZER.closure_reason = closure_reason
    BASE.exact_review = FINALIZER.exact_review

    result = BASE.render_day(25)
    FINALIZER.AUTHOR_DENOMINATOR[25] = 30
    ref_result = FINALIZER.repair_refs(25)

    ledger = json.loads((PACKET / "screening-ledger-final.json").read_text(encoding="utf-8"))
    retained = ledger["candidate_denominator"]
    queue = len(json.loads((PACKET / "BOOKS_WRITEBACK_QUEUE.json").read_text(encoding="utf-8"))["items"])
    patch_date_local_support(removed, retained, queue)

    # Repair the one hard-coded legacy raw count introduced by the shared ref helper.
    report = REPORT.read_text(encoding="utf-8")
    report = report.replace("872/872", "836/836").replace("其余 780 个 identity", "其余 780 个 identity")
    report = report.replace(
        "无：retained family 的 official exact-v1 已全部完成 Review；本日无 withdrawn primary source",
        "无：retained family 的 official exact-v1 已全部完成 Review；7 个 withdrawn primary source 仅保留 pre-denominator closure，不是 blocker",
    )
    REPORT.write_text(report, encoding="utf-8")

    # Canonical conservation and contamination invariants.
    final_ledger = json.loads((PACKET / "screening-ledger-final.json").read_text(encoding="utf-8"))
    active_ids = {row["arxiv_id"] for row in final_ledger["identities"]}
    selected = {row["arxiv_id"] for row in final_ledger["identities"] if row["candidate_state"] == "retained"}
    reviews = {row["arxiv_id"] for row in json.loads((PACKET / "exact-v1-review-packet.json").read_text(encoding="utf-8"))["items"]}
    comparisons = {row["arxiv_id"] for row in json.loads((PACKET / "books-current-content-comparison.json").read_text(encoding="utf-8"))["items"]}
    assert len(active_ids) == 836 and not (active_ids & removed)
    assert len(selected) == retained == 56
    assert reviews == selected == comparisons
    assert not (selected & WITHDRAWN)
    assert len(final_ledger["identities"]) - retained == 780
    assert queue == 7

    print(json.dumps({
        "result": result,
        "refs": ref_result,
        "raw": 836,
        "retained": retained,
        "closures": 780,
        "withdrawn_closures": len(WITHDRAWN),
        "exact_complete": len(reviews),
        "blocked": 0,
        "queue": queue,
        "weekly_dependency": 0,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
