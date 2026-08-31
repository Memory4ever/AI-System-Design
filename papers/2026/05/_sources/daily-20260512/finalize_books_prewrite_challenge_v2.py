#!/usr/bin/env python3
"""Finalize the 2026-05-12 current-Books adversarial prewrite challenge.

This script does not write shared Books.  It narrows the independent reviewer’s
provisional queue against the current semantic body of the owner and adjacent
chapters, then emits the root-only writeback packet.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]

SURVIVORS = {
    "2605.09994": (
        "TRAIN-DATA",
        "现有 Ch27 已有 immutable manifest 与消费 cursor，但尚未把对象存储中跨 producer/consumer 的全局 batch 作为原子发布、可见性与回收的共同 commit unit；应补入 batch-level atomic publication，并保留 manifest 协调、读放大与 GC 状态代价。",
    ),
    "2605.10199": (
        "MULTIMODAL-REPRESENTATION",
        "现有 Ch23 已有 modality stream、timestamp 与融合，但尚未处理 assistant 正在生成时并发 user stream 的路由：channel fusion 与 external cross-attention 改变 interruption latency、生成一致性和状态归属。",
    ),
    "2605.10501": (
        "TRAIN-DISTRIBUTED-TRAINING",
        "现有 Ch36 覆盖 collective、topology 与并行策略，但尚未把参数规模、forward-only/forward-backward、序列长度及 input-conditioned activation 不同的 compound sections 视为需要各自 execution config 的运行时计划状态。",
    ),
    "2605.10670": (
        "INFER-DYNAMO",
        "现有 Ch52 已有 distributed request/state/control path 与部分故障边界，但未把 live membership 收缩、expert coverage 修复和 CUDA-graph execution identity 作为宽 EP MoE partial-rank recovery 的联合 runtime contract。",
    ),
    "2605.10875": (
        "INFER-TENSORRT-LLM",
        "现有 Ch49 分别讨论 activation sparsity 与 mixed precision，但尚未形成按 token 联合控制 attention sparsity、structured pruning 与 precision 的质量/算力预算控制器。",
    ),
    "2605.11093": (
        "PLATFORM-MONITORING",
        "现有 Ch67 已有 metrics、probes 与 activation-monitor validation，但尚未把模型内部 tensor capture 通过异步 GPU→CPU staged sensor substrate 从 inference hot path 解耦，并作为 policy-controlled observability contract。",
    ),
    "2605.11215": (
        "TRAIN-DISTRIBUTED-TRAINING",
        "现有 Ch36 已有 checkpoint、elastic recovery 与 failure state，但尚未保留固定 microbatch count 这一 in-step recovery invariant，用来维持每次迭代梯度与 failure-free run 的随机等价边界。",
    ),
}

DOWNGRADE_REASONS = {
    "2605.09992": "Ch48 已拥有 drafter 表示差异、训练分布漂移、target acceptance 与 rollback；hidden-state scale/attention drift 是该 contract 的诊断证据，不是新控制面。",
    "2605.10075": "Ch66 已按不确定性、方差与 slice 分配评测预算；approximate Neyman active testing 是 estimator 分支，不改变 evaluation owner。",
    "2605.10094": "Ch26 已允许经验证的 action chunk/episode latent 作为有 admission、版本和 fallback 的部署期先验。",
    "2605.10124": "Ch48 已覆盖受 network、acceptance、rollback 与 workload 条件约束的 edge-cloud speculation；GELATO 是路由策略实例。",
    "2605.10246": "Ch66 已要求 integrity/failure scenario、honest abstention、process/outcome evidence；该 benchmark 是领域 slice。",
    "2605.10347": "Ch25 已区分 training predictive prior 与经验证的 action-conditioned transition；mobile GUI 只是 workload 实例。",
    "2605.10366": "Ch81 已拥有 verifier feedback、artifact lineage 与 bounded mutation/commit；graph credit assignment 是优化器实例。",
    "2605.10426": "Ch26 已把 predictive latent/world signal 作为 VLA planning input，并由 controller/environment 保留 truth 与 commit authority。",
    "2605.10448": "Ch66 已明确分离 task design 与 outcome detector/verifier reliability，并要求 bounded evidence。",
    "2605.10516": "Ch66 已要求 repeated-run consistency 与 semantic/environment perturbation 下的稳健性。",
    "2605.10555": "Ch78 已拥有 proposal→validate/simulate→authorize→execute→observe→recover；six verbs/NTC 只是协议命名与细化。",
    "2605.10556": "Ch70 已把 parallelism、batch、length 纳入能耗模型及 energy-quality-latency contract。",
    "2605.10575": "Ch66 已有 claim-specific EvalSpec、可执行 verifier/audit package 与 release authority。",
    "2605.10614": "Ch72 已将 shared-context 的跨 agent 信息流建模为 provenance/taint，并在 sink/effect time 执行策略。",
    "2605.10779": "Ch72 已分离 proposal、authorization、commit 与 bounded rollback；该数据集只是 computer-use 检查实例。",
    "2605.10819": "Ch26 已拥有 latent action supervision 与 action-state identity。",
    "2605.10832": "Ch81 已拥有 versioned workflow state 与 verifier-gated tactic/experience derivation。",
    "2605.10912": "Ch66 已冻结 native environment、trajectory、side effects 与 outcome evidence。",
    "2605.10913": "Ch81 已要求 durable event state、replay 与 reversible effects，而非 transcript-only reconstruction。",
    "2605.10923": "Ch84 已拥有 Skill admission、retain、supersede、rollback 与 promotion 生命周期。",
    "2605.10933": "Ch21 已分离 router choice 与 capacity/topology-aware expert placement。",
    "2605.11039": "Ch72 已把 provenance/semantic taint 带入 typed capability 与 effect-time checks。",
    "2605.11047": "Ch72 已把 open-world deployment context 与 residual risk 纳入 security contract。",
    "2605.11053": "Ch72 已把 cross-tool traffic 与 taint graph 视为可观测 security surface。",
    "2605.11086": "Ch66/Ch72 已要求 executable security environment、task budget、verifier 与 mitigation state；该 benchmark 是受限 slice。",
    "2605.11186": "Ch48 已拥有 tree proposal allocation、memory、target verification 与 rollback。",
    "2605.11202": "Ch42/Ch66 已拥有 timed request trace、failure state、replay 与 independent oracle；greybox fuzzer 是实现分支。",
    "2605.11209": "Ch66 已有 search-based failure-mass sampling 与 residual-mass disclosure；CEM 是方法分支。",
    "2605.11212": "Ch75 已把 visual/observation history selection 作为有预算的 context state，并保留 raw-evidence fallback。",
    "2605.11229": "Ch72 已有跨 workflow 的 path-sensitive provenance/taint 与 effect-time commit。",
    "2605.11234": "Ch78 已拥有 ontology/typed schema、preconditions、validation 与 compatibility fallback。",
    "2605.11277": "Ch49 已拥有 expert working set、动态 MoE execution mapping 与 hardware-specific plan；GPU/PIM scheduling 是实现实例。",
    "2605.11325": "Ch77 已拒绝把 similarity 当作 belief truth，并用 structured belief、provenance 与 supersession 保证 precision。",
    "2605.11330": "Ch66 已把 hallucination/RAG evaluation 绑定 context length、label quality、evaluator 与 run identity。",
    "2605.11333": "Ch66 已保存 workload trace/schema/replay 与 production run identity，支撑可复现和软硬件协同。",
    "2605.11360": "Ch83 已分离 protocol permission、principal authorization、consent 与 effect-time policy/escalation。",
    "2605.11367": "Ch25 已定义与 generated frames 分离的 persistent、revisable 3D belief。",
    "2605.13880": "Ch77 已要求 proposer/validator-gated experience write，并绑定 source episode 与 rollback。",
    "2605.18803": "Ch25 已把 planner-induced rare-state coverage 与 prioritized failure discovery 作为训练/评测压力。",
    "2605.23956": "Ch9/Ch66 已拥有 typed pipeline stages、feedback/error propagation 与 evaluation evidence；QUIVER 是分析框架分支。",
}


def load(name: str):
    return json.loads((ROOT / name).read_text())


def write(name: str, payload) -> None:
    (ROOT / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def body_outline(path: str) -> str:
    text = (REPO / path).read_text()
    semantic = text.split("## Review notes", 1)[0]
    return " → ".join(line.strip() for line in semantic.splitlines() if re.match(r"^#{2,4} ", line))


def roadmap() -> dict[str, str]:
    result: dict[str, str] = {}
    for line in (REPO / "ROADMAP.md").read_text().splitlines():
        match = re.match(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)` \|", line)
        if match:
            result[match.group(1)] = match.group(2)
    return result


def adjacent_paths(owner_path: str) -> list[str]:
    match = re.search(r"/(\d+)-[^/]+\.md$", owner_path)
    if not match:
        return []
    chapter = int(match.group(1))
    parent = REPO / Path(owner_path).parent
    found: list[str] = []
    for number in (chapter - 1, chapter + 1):
        candidates = sorted(parent.glob(f"{number}-*.md"))
        if candidates:
            found.append(str(candidates[0].relative_to(REPO)))
    return found


def main() -> None:
    comparisons = load("books-current-content-comparison-independent.json")
    queue_old = load("books-writeback-queue-independent-reconciled.json")
    packet = {row["arxiv_id"]: row for row in load("exact-v1-review-packet-independent.json")}
    ledger = load("screening-ledger-independent-reconciled.json")
    paths = roadmap()
    by_id = {row["arxiv_id"]: row for row in comparisons}

    provisional = {row["arxiv_id"] for row in comparisons if row["decision"] == "Integrate"}
    assert provisional == set(SURVIVORS) | set(DOWNGRADE_REASONS), (len(provisional), provisional - set(SURVIVORS) - set(DOWNGRADE_REASONS))

    for aid, reason in DOWNGRADE_REASONS.items():
        by_id[aid]["decision"] = "No Change — Existing Coverage"
        by_id[aid]["reason"] = reason
        by_id[aid]["prewrite_challenge"] = "downgraded_after_current_books_semantic_body_review"

    for aid, (owner, reason) in SURVIVORS.items():
        row = by_id[aid]
        row["owner_node"] = owner
        row["owner_path"] = paths[owner]
        row["adjacent_paths"] = adjacent_paths(row["owner_path"])
        row["owner_body_outline_before_review_notes"] = body_outline(row["owner_path"])
        row["adjacent_body_outlines_before_review_notes"] = {
            path: body_outline(path) for path in row["adjacent_paths"]
        }
        row["decision"] = "Integrate"
        row["reason"] = reason
        row["prewrite_challenge"] = "retained_after_current_books_semantic_body_review"

    for identity in ledger["identities"]:
        aid = identity["arxiv_id"]
        if aid not in by_id:
            continue
        identity["owner_node"] = by_id[aid].get("owner_node")
        identity["books_disposition"] = by_id[aid]["decision"]

    final_rows = [by_id[row["arxiv_id"]] for row in comparisons]
    write("books-current-content-comparison-final.json", final_rows)
    write("screening-ledger-independent-reconciled.json", ledger)

    old_items = {row["arxiv_id"]: row for row in queue_old["items"]}
    final_items = []
    for aid in sorted(SURVIVORS):
        comp = by_id[aid]
        review = packet[aid]
        old = old_items[aid]
        final_items.append({
            "arxiv_id": aid,
            "source_family_id": comp["source_family_id"],
            "stable_node_id": comp["owner_node"],
            "owner_path": comp["owner_path"],
            "adjacent_paths": comp["adjacent_paths"],
            "review_provenance_id": comp["review_provenance_id"],
            "books_review_ref": comp["books_review_ref"],
            "integration_delta": comp["reason"],
            "nonproof_boundary": review["claim_nonproof_boundary"],
            "writeback_state": "awaiting_root_serial_writeback",
            "owner_merge_group": "TRAIN-DISTRIBUTED-TRAINING-COMPOUND-RECOVERY" if aid in {"2605.10501", "2605.11215"} else f"{comp['owner_node']}-{aid}",
        })

    queue = {
        "schema": "books-writeback-queue-v2.1-final-prewrite-challenge",
        "report_date": "2026-05-12",
        "status": "ready_for_root_serial_writeback",
        "counts": {"retained": 76, "integrate": 7, "no_change": 68, "blocked": 1, "ordinary_pending": 0},
        "items": final_items,
        "blocked": queue_old["blocked"],
        "writeback_rule": "Write one owner-merged mechanism narrative per owner group before the first Review notes; do not append one paragraph per paper.",
    }
    write("books-writeback-queue-final.json", queue)

    groups: dict[str, list[dict]] = defaultdict(list)
    for item in final_items:
        groups[item["stable_node_id"]].append(item)
    md = [
        "# 2026-05-12 Books Writeback Queue — Final Prewrite Challenge",
        "",
        "**State:** Ready for root serial writeback；shared Books 尚未修改。",
        "",
        "47 个 provisional Integrate 经 current owner + adjacent semantic-body challenge 收紧为 7；另 68 个为 `No Change — Existing Coverage`，1 个 exact-v1 blocker 保持冻结。写回必须按 owner 合并成机制演进，不得逐论文追加。",
        "",
    ]
    for owner, items in groups.items():
        md += [f"## `{owner}`", "", f"Target: `{items[0]['owner_path']}`", ""]
        for item in items:
            md += [
                f"- `{item['source_family_id']}` / arXiv:{item['arxiv_id']}v1",
                f"  - Delta: {item['integration_delta']}",
                f"  - Evidence: `{item['review_provenance_id']}`；`{item['books_review_ref']}`",
                f"  - Non-proof: {item['nonproof_boundary']}",
            ]
        if owner == "TRAIN-DISTRIBUTED-TRAINING":
            md += ["", "合并叙事：compound section 的 execution-plan state 先扩展正常执行配置空间；partial failure 随后要求 recovery 在该计划内保持 fixed-microbatch gradient invariant。两项必须写成同一条 execution→failure→recovery 演进链。"]
        md.append("")
    md += ["## Blocked", "", "- `SF-2026-ARXIV-2605-10133`：exact-v1 正文不可取得；不得依据 abstract 进入 Books。", ""]
    (ROOT / "BOOKS_WRITEBACK_QUEUE_FINAL.md").write_text("\n".join(md))

    challenge = {
        "schema": "books-prewrite-challenge-v2.1",
        "report_date": "2026-05-12",
        "reviewer_relation": "non-books-writer-prewrite",
        "scope": "current owner and adjacent semantic body before first Review notes",
        "counts": {"provisional_integrate": 47, "final_integrate": 7, "downgraded_to_no_change": 40, "blocked": 1},
        "owner_corrections": [{"arxiv_id": "2605.10670", "from": "INFER-SCHEDULING", "to": "INFER-DYNAMO"}],
        "survivors": [{"arxiv_id": aid, "owner": owner, "reason": reason} for aid, (owner, reason) in SURVIVORS.items()],
        "downgrades": [{"arxiv_id": aid, "reason": reason} for aid, reason in DOWNGRADE_REASONS.items()],
        "largest_provisional_owner_group": {"owner": "PLATFORM-EVALUATION-SYSTEM", "items": 10, "final_integrate": 0},
        "largest_final_owner_group": {"owner": "TRAIN-DISTRIBUTED-TRAINING", "items": 2, "write_as_one_owner_merged_narrative": True},
        "shared_books_written": False,
    }
    write("books-prewrite-challenge-final.json", challenge)

    audit = load("independent-semantic-audit.json")
    audit["books_prewrite_receipt"] = {
        "comparison": "books-current-content-comparison-final.json",
        "challenge": "books-prewrite-challenge-final.json",
        "queue": "books-writeback-queue-final.json",
        "current_owner_adjacent_review": "76/76 (7 Integrate; 68 No Change; 1 Blocked)",
        "provisional_queue_challenged": "47/47; 40 downgraded; 1 owner corrected",
        "shared_books_written": False,
    }
    audit["gate"]["books"] = "Open — final 7-item owner-merged queue is ready, but root serial Books writeback and non-writer post-write audit have not occurred."
    audit["gate"]["completion"] = "In Progress — root Books writeback/post-write audit pending; 1 exact-v1 external blocker remains Conditional."
    write("independent-semantic-audit.json", audit)


if __name__ == "__main__":
    main()
