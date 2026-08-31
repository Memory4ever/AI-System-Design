#!/usr/bin/env python3
"""Record the non-writer post-write semantic audit for 2026-05-12."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
REPORT = ROOT.parents[1] / "12" / "README.md"

AUDIT_NOTES = {
    "2605.09994": {
        "placement": "Placed inside Data lineage, after typed lineage and before downstream domain/streaming branches; Ch27 hands the committed batch/data cursor to Ch28 pretraining and Ch35 checkpoint.",
        "evolution": "Per-shard visibility is retained as the simple offline baseline; online multi-producer/consumer training introduces global-batch atomicity, split state ownership and commit/GC ordering.",
        "tradeoff": "Manifest coordination, metadata read amplification, late workers and orphan cleanup are explicit; static dataset/single-consumer/full-rerun is the coexistence fallback.",
    },
    "2605.10199": {
        "placement": "Placed in Ch23's fusion evolution immediately after early/late/cross-attention fusion and before token-budget competition; Ch24 consumes the resulting committed representation state for generation.",
        "evolution": "Turn-complete utterance fusion remains the coherent baseline; concurrent user observations add channel-local state, safe-point commit and explicit interruption authority.",
        "tradeoff": "Earlier commit trades coherence/rollback/alignment for latency; later commit may miss real-time control, with turn-based late fusion preserved as fallback.",
    },
    "2605.10501": {
        "placement": "Co-located and intentionally nested with 2605.11215 in one Ch36 narrative between sequence-conditioned planning and general plan search; Ch35 owns committed recovery state and Ch37 specializes one admitted parallel dimension.",
        "evolution": "A single static job plan remains the auditable baseline; heterogeneous compound sections introduce per-section configs, then failure adds a fixed logical-microbatch/RNG/data invariant before optimizer commit.",
        "tradeoff": "Profile/plan epochs, replay bitmap, collective recovery and checkpoint metadata are explicit costs; non-replayable effects, equivalence failure or high recovery cost fall back to a static plan and committed-checkpoint restart.",
    },
    "2605.10670": {
        "placement": "Placed in Ch52 after distributed request/state/control recovery mechanisms and before the explicit Ch55 boundary; Ch51 hands up engine-local typed state and Ch53 declares the topology through the control plane.",
        "evolution": "Whole-worker/request restart remains the simple path; wide EP adds mutable membership, expert coverage and CUDA-graph execution identity that must publish in one routing epoch.",
        "tradeoff": "Expert redundancy, HBM, reconfiguration latency and admission complexity are explicit; unsupported failure models, no redundancy or SLO violation retain whole-group restart/fail-stop.",
    },
    "2605.10875": {
        "placement": "Placed in Ch49's execution-plan evolution after individual sparsity/precision mechanisms and before learned-kernel admission; Ch48 provides verified proposal/rollback semantics and Ch50 consumes admitted plans in a serving engine.",
        "evolution": "Independent static sparsity/quantization artifacts remain the baseline; per-token state and a shared quality budget motivate a joint proposal policy while verifier/runtime retain admission authority.",
        "tradeoff": "Combinatorial action space, decision overhead, calibration drift and coupled errors are explicit; unsupported hardware, OOD inputs or tail-latency pressure fall back to static or dense/full-precision execution.",
    },
    "2605.11093": {
        "placement": "Placed in Ch67 under observer-effect costs, before collective and side-channel telemetry; Ch66 defines evidence sufficiency and Ch68 receives discrete, provenance-bearing events.",
        "evolution": "Request metrics remain the low-cost baseline and synchronous tensor copies the direct but intrusive path; bounded asynchronous GPU-to-CPU staging creates a policy-controlled internal sensor path.",
        "tradeoff": "GPU memory/copy-engine/PCIe/host-queue contention, dropped samples, time skew and sensitive activation leakage are explicit; overload degrades sampling to aggregates, then request metrics/offline profiler.",
    },
    "2605.11215": {
        "placement": "Shares the intentional owner-merged Ch36 body with 2605.10501; the nested unique markers prove one combined execution-to-recovery evolution rather than two paper appendices.",
        "evolution": "Per-section execution planning is extended by failure recovery that preserves logical microbatch count, sample/RNG identity and the optimizer commit boundary.",
        "tradeoff": "Recovery metadata and replay cost are explicit; when stochastic equivalence cannot be maintained, the path reverts to committed-checkpoint restart rather than claiming transparent continuation.",
    },
}


def load(name: str):
    return json.loads((ROOT / name).read_text())


def write(name: str, payload) -> None:
    (ROOT / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def line_of(text: str, needle: str) -> int:
    return text[: text.index(needle)].count("\n") + 1


def main() -> None:
    queue = load("books-writeback-queue-final.json")
    results = []
    for item in queue["items"]:
        aid = item["arxiv_id"]
        family = item["source_family_id"]
        owner = REPO / item["owner_path"]
        text = owner.read_text()
        start = f"<!-- semantic-body-binding:{family}:start -->"
        end = f"<!-- semantic-body-binding:{family}:end -->"
        assert text.count(start) == 1 and text.count(end) == 1
        start_line, end_line = line_of(text, start), line_of(text, end)
        review_match = re.search(r"^## Review notes\s*$", text, flags=re.M)
        assert review_match and text.index(start) < review_match.start()
        body = text.split(start, 1)[1].split(end, 1)[0]
        assert f"arXiv:{aid}v1" in body
        adjacent = []
        for path in item["adjacent_paths"]:
            adjacent_text = (REPO / path).read_text()
            adjacent_semantic = re.split(r"^## Review notes\s*$", adjacent_text, maxsplit=1, flags=re.M)[0]
            adjacent.append({
                "path": path,
                "semantic_body_read": True,
                "stable_node_present": "Stable Knowledge Node ID" in adjacent_semantic,
            })
        note = AUDIT_NOTES[aid]
        results.append({
            "arxiv_id": aid,
            "source_family_id": family,
            "owner_node": item["stable_node_id"],
            "owner_path": item["owner_path"],
            "marker_start_line": start_line,
            "marker_end_line": end_line,
            "marker_unique": True,
            "before_first_review_notes_heading": True,
            "owner_semantic_body_read": True,
            "adjacent_chapters": adjacent,
            "old_path_and_changed_constraint": "passed",
            "state_control_ownership": "passed",
            "mechanism_and_commit_boundary": "passed",
            "benefit_and_tradeoff": "passed",
            "failure_mode": "passed",
            "fallback_and_coexistence": "passed",
            "evidence_nonproof_boundary": "passed",
            "chapter_handoff": "passed",
            "placement_finding": note["placement"],
            "evolution_finding": note["evolution"],
            "tradeoff_finding": note["tradeoff"],
            "unresolved_findings": [],
            "result": "passed",
        })

    assert len(results) == 7
    receipt = {
        "schema": "books-post-write-semantic-audit-v2.1",
        "report_date": "2026-05-12",
        "auditor_relation": "non-books-writer",
        "scope": "7/7 final Integrate families; owner semantic body plus queue-declared adjacent chapters",
        "method": "unique marker and placement check plus fresh-context semantic read of evolution, ownership, mechanism, tradeoff, failure, fallback, evidence boundary and chapter handoff",
        "counts": {
            "families": 7,
            "owner_groups": 6,
            "unique_markers": 7,
            "before_review_notes": 7,
            "semantic_pass": 7,
            "unresolved_books_findings": 0,
            "external_evidence_blockers": 1,
        },
        "owner_merged_narratives": [{
            "owner": "TRAIN-DISTRIBUTED-TRAINING",
            "families": ["SF-2026-ARXIV-2605-10501", "SF-2026-ARXIV-2605-11215"],
            "result": "passed — one intentionally nested execution-plan to fixed-microbatch recovery narrative",
        }],
        "items": results,
        "books_result": "passed",
        "report_gate_result": "Conditional Pass — Books writeback is semantically verified, while SF-2026-ARXIV-2605-10133 remains a precise external exact-v1 blocker through the Evidence Gate.",
    }
    write("books-post-write-semantic-audit.json", receipt)

    for item in queue["items"]:
        item["writeback_state"] = "post_write_semantic_audit_passed"
        item["post_write_audit_ref"] = "books-post-write-semantic-audit.json"
    queue["status"] = "post_write_semantic_audit_passed_conditional_external_blocker"
    queue["shared_books_written"] = True
    queue["post_write_counts"] = {"families_verified": 7, "owner_groups_verified": 6, "unresolved_books_findings": 0}
    write("books-writeback-queue-final.json", queue)

    audit = load("independent-semantic-audit.json")
    audit["books_postwrite_receipt"] = {
        "artifact": "books-post-write-semantic-audit.json",
        "families_verified": "7/7",
        "owner_groups_verified": "6/6",
        "marker_placement": "7/7 unique and before first Review notes heading",
        "unresolved_books_findings": 0,
        "shared_books_written": True,
    }
    audit["gate"]["books"] = "Conditional Pass — 7/7 Books writebacks passed non-writer owner+adjacent semantic audit; the report remains conditional because SF-2026-ARXIV-2605-10133 is an exact-v1 external blocker."
    audit["gate"]["completion"] = "Conditional — ordinary work and Books writeback are closed; one precisely scoped external exact-v1 blocker remains."
    write("independent-semantic-audit.json", audit)

    report = REPORT.read_text()
    replacements = {
        "**Status:** In Progress；Coverage=Closed、Evidence=Conditional Pass、Books=Open。独立重放已完成，普通 pending=0；1 项 exact-v1 外部全文 blocker 被精确冻结，7 项 owner-merged Books queue 等待 root 串行写回。":
            "**Status:** Conditional；Coverage=Closed、Evidence=Conditional Pass、Books=Conditional Pass。普通 pending=0；7/7 Books writeback 已通过非写作者 owner+adjacent semantic audit；`2605.10133v1` 保持精确 external blocker。",
        "| Completion Status | In Progress |": "| Completion Status | Conditional |",
        "| Books Gate | Open |": "| Books Gate | Conditional Pass |",
        "| SA-20260512-INDEPENDENT-BOOKS | fresh-context:non-author | books | books-review:SF-2026-ARXIV-2605-09863 | F-20260512-BOOKS-WRITEBACK | 47/47 provisional queue challenged against current owner+adjacent body; final owner-merged queue=7; shared Books unchanged | open |":
            "| SA-20260512-INDEPENDENT-BOOKS | fresh-context:non-author | books | books-review:SF-2026-ARXIV-2605-09863 | none | 7/7 markers unique and before Review notes; 6/6 owner groups pass evolution/ownership/trade-off/failure/fallback/evidence/handoff audit | passed |",
        "root 按 `BOOKS_WRITEBACK_QUEUE_FINAL.md` 与 `books-writeback-queue-final.json` 串行写回 7 项、6 个 owner group；其中 `TRAIN-DISTRIBUTED-TRAINING` 的 Maestro 与 ReCoVer 必须合并为一条 execution-plan→failure→recovery 演进链。随后由非写作者检查正文真实存在、位置在首个 Review notes 之前，并重验相邻 owner 冲突。`2605.10133v1` 在 exact-v1 恢复前保持冻结。":
            "7 项、6 个 owner group 已完成写回，并通过 `books-post-write-semantic-audit.json` 的非写作者复核；`TRAIN-DISTRIBUTED-TRAINING` 的两项 family 已合并为 execution-plan→failure→recovery 演进链。后续只需在 exact-v1 primary 恢复时重开 `2605.10133v1` 的 Evidence/Books Decision。",
        "- 7 项 final queue 经 root 按 6 个 owner group 合并写回后，post-write non-author audit 是否全部通过？":
            "- `2605.10133v1` 的 exact-v1 primary 恢复后，是否改变当前 Conditional Gate 与 Books disposition？",
        "Completion Status: `In Progress`": "Completion Status: `Conditional`",
        "Books: `Open`": "Books: `Conditional Pass`",
        "ordinary pending=0；75/76 exact-v1 complete；1 precise external blocker；7 项 Books queue 等待 root 串行写回和非写作者 post-write audit。":
            "ordinary pending=0；75/76 exact-v1 complete；7/7 Books writeback 已通过 post-write semantic audit；1 precise external blocker 保持 Conditional。",
        "unresolved findings: 2": "unresolved findings: 1",
        "本 prewrite lane 未写共享 Books；随后 root writeback 与独立 post-write audit 见 `books-post-write-semantic-audit.json`。":
            "shared Books writeback 与独立 post-write audit 见 `books-post-write-semantic-audit.json`。",
    }
    # Earlier render stated this sentence in every comparison block. Preserve the
    # historical authorship boundary while adding the actual post-write receipt.
    report = report.replace(
        "本 lane 未写共享 Books。",
        "本 prewrite lane 未写共享 Books；随后 root writeback 与独立 post-write audit 见 `books-post-write-semantic-audit.json`。",
    )
    for old, new in replacements.items():
        assert old in report, old
        report = report.replace(old, new)
    report = report.replace(
        "- 新增独立 exact-v1 packet、provenance、Materials Request、Books comparison 与 reconciled queue。",
        "- 新增独立 exact-v1 packet、provenance、Materials Request、Books comparison、final queue 与 post-write semantic audit。",
    )
    report = report.replace(
        "- 未修改共享 Books，未 stage、commit 或 push。",
        "- root 已按 6 个 owner group 修改 Ch23、Ch27、Ch36、Ch49、Ch52、Ch67；本审计未继续修改 Books，未 stage、commit 或 push。",
    )
    REPORT.write_text(report)


if __name__ == "__main__":
    main()
