#!/usr/bin/env python3
"""Finalize the non-writing Books prewrite challenge for 2026-05-09.

This script only updates date-local research artifacts.  It never edits Books.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LEDGER_PATH = ROOT / "screening-ledger-independent-final.json"
COMPARE_PATH = ROOT / "books-current-content-comparison.json"
AUDIT_PATH = ROOT / "independent-semantic-audit.json"

FINAL_INTEGRATE = {
    "2605.07330": {
        "owner": "TRAIN-DISTRIBUTED-TRAINING",
        "owner_path": "books/part-04-training-system/36-distributed-training.md",
        "reason": "现有正文分别覆盖 policy freshness 与 optimizer-aware sparse support，但没有把解耦 Trainer→Rollout 的发布对象改写成由 base checkpoint、稀疏 index/value payload、target replica epoch 与重构 hash 共同标识的无损 policy update。",
    },
    "2605.08524": {
        "owner": "TRAIN-DISTRIBUTED-TRAINING",
        "owner_path": "books/part-04-training-system/36-distributed-training.md",
        "reason": "现有 Context Parallel 主线解释 Ulysses All-to-All、buffer staging 与 workload pools，但尚未把通信图从固定 collective 进一步提升为由 topology、head/sequence ownership、buffer capacity 与 plan epoch 共同约束的 fully-connected exchange plan。",
    },
    "2606.20582": {
        "owner": "TRAIN-DISTRIBUTED-TRAINING",
        "owner_path": "books/part-04-training-system/36-distributed-training.md",
        "reason": "现有正文覆盖可靠重传与训练容忍的有界丢包分支，但没有区分 byte-level recovery 与 collective-semantic recovery：恢复状态需要理解 message/round ownership，同时保持 exact collective completion 与可靠路径 fallback。",
    },
}

DOWNGRADE = {
    "2605.07135": "Ch72 已把不可信 source、跨委派 semantic taint、irreversible sink 与 effect-time deterministic authorization 串成端到端 authority path；GitHub Actions 只增加一个受限场景。",
    "2605.07238": "Ch56 已用 future KV feasibility、time-indexed occupancy、prefix locality、downstream reachability 与 bounded reservation 表达当前 placement 对未来可达性的影响。",
    "2605.07242": "Ch77 已拥有 provenance/dependency tracing、descendant invalidation、quarantine、selective replay 与 regenerated memory version，覆盖 barrier-first cascade repair 的长期合同。",
    "2605.07569": "Ch36 已把 raw-sample membership、sequence/head tile placement、heterogeneous workload pool、topology-sensitive plan 与 fallback 写入长上下文训练主线。",
    "2605.07594": "Ch77 已把 raw evidence、query-conditioned derived view、versioned materialization、validation、supersession 与 raw-retrieval fallback 分层。",
    "2605.07689": "Ch33 已明确 binary reward 的全对/全错组会失去可学习差异，并要求 pass-rate controller、verifier identity 与普通 GRPO/PPO fallback。",
    "2605.07836": "Ch83 已明确跨 server 双向 information flow、principal/server/taint identity 与 effect-time authorizer；论文只增加 ecosystem case。",
    "2605.07935": "Ch83 已把 protocol lowering 为带 source/type evidence 的有限状态 IR，并用 composition、trace replay、counterexample 与 executable regression 形成修复 Gate；无需在 Ch82 重复一条 formal-repair 主线。",
    "2605.08317": "Ch45 已在统一质量预算下联合建模 token 保留与 feature/precision allocation，并明确 layout、kernel、update、drift 与 FullKV fallback。",
    "2605.08374": "Ch77 已把 provenance DAG、tree-based credit、derived-state lineage、reward 非因果真值及缺 trace 时禁止长期更新写入主线。",
    "2605.08460": "Ch82 已把 spawn/delegation 表达为 capability artifact × runtime/credential identity × task lease，并禁止复制父 Agent 权限。",
    "2605.08513": "Ch72 已明确 attention/activation/learned monitor 只能作为 policy-bound sensor，最终 allow/deny 属于独立 reference monitor。",
    "2605.08527": "Ch33 已完整承载 rollout-as-a-service、环境/actor/update owner、policy epoch/freshness、异步 lag、KV capacity 与同步 fallback。",
    "2605.08541": "Ch7 与 Ch28 已明确 token-per-parameter 覆盖、Chinchilla/Kaplan 差异、undertraining 与实验覆盖决定 scaling extrapolation，而非固定比例。",
    "2605.08545": "Ch66 已把 run identity、per-step observation/tool/retry/recovery trace、failure taxonomy 与 release evidence 分开，final score 不能替代过程证据。",
    "2605.08563": "Ch81 已把 failed trace、runtime contamination、joint context/environment checkpoint、clean replay、retry/compensation 与 external-effect reconciliation 串成恢复主线。",
    "2605.08580": "Ch77 已把 summary 视为可失效 derived state，保留 raw archive、future execution evidence、independent validation、reject-commit 与原 Context fallback。",
    "2605.08581": "Ch56 已联合处理 queue admission、future KV occupancy、prefix reuse、routing 与 cache policy；Ch45 拥有 radix/KV identity 与物理布局，当前 owner handoff 已覆盖 PRISM 的长期结论。",
}


def dump(path: Path, payload: object) -> None:
    encoded = (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode()
    path.write_bytes(encoded)
    path.with_suffix(path.suffix + ".sha256").write_text(hashlib.sha256(encoded).hexdigest() + "\n")


ledger = json.loads(LEDGER_PATH.read_text())
for row in ledger["identities"]:
    aid = row["arxiv_id"]
    if aid in FINAL_INTEGRATE:
        row["integration_disposition"] = "Integrate"
        row["owner_node"] = FINAL_INTEGRATE[aid]["owner"]
    elif aid in DOWNGRADE:
        row["integration_disposition"] = "No Change — Existing Coverage"
ledger["gate_status"] = "coverage_reconciled_evidence_conditional_books_prewrite_challenged"
dump(LEDGER_PATH, ledger)

comparison = json.loads(COMPARE_PATH.read_text())
for item in comparison["items"]:
    aid = item["arxiv_id"]
    if aid in FINAL_INTEGRATE:
        spec = FINAL_INTEGRATE[aid]
        item.update(
            owner_node=spec["owner"],
            owner_path=spec["owner_path"],
            disposition="Integrate",
            current_content_comparison=spec["reason"],
        )
    elif aid in DOWNGRADE:
        item.update(
            disposition="No Change — Existing Coverage",
            current_content_comparison=DOWNGRADE[aid],
        )
dump(COMPARE_PATH, comparison)

audit = json.loads(AUDIT_PATH.read_text())
audit["schema"] = "daily-v2.1-independent-semantic-audit-with-books-prewrite-v2"
audit["reconciled_counts"]["root_writeback_ready_integrates"] = len(FINAL_INTEGRATE)
audit["books_prewrite_challenge"] = {
    "reviewer_role": "fresh-context non-author and non-writer",
    "scope": "21 evidence-complete provisional Integrates against current owner and adjacent chapters",
    "provisional_integrates": 21,
    "final_integrates": len(FINAL_INTEGRATE),
    "downgraded_no_change": len(DOWNGRADE),
    "shared_books_modified": False,
    "survivors": sorted(FINAL_INTEGRATE),
    "owner_merged_narrative_ref": "BOOKS_WRITEBACK_QUEUE_FINAL.md",
    "unresolved_findings": [],
}
audit["books_disposition_corrections"].update({aid: "No Change — Existing Coverage" for aid in DOWNGRADE})
audit["gate_result"]["reason"] = (
    "Coverage is Closed on the independently reconciled 834-row screen. Evidence remains Conditional Pass because "
    "17 exact-v1 bodies are blocked with precise Materials Requests. Current-content comparison reduced the 21 "
    "evidence-complete provisional Integrates to three owner-merged TRAIN-DISTRIBUTED-TRAINING deltas; Books stays "
    "Open until root writes and a different reviewer completes post-write semantic audit."
)
dump(AUDIT_PATH, audit)

prewrite_audit = {
    "schema": "daily-v2.1-books-prewrite-challenge-v1",
    "report_date": "2026-05-09",
    "reviewer_role": "fresh-context non-author and non-writer",
    "scope": {
        "provisional_integrates": 21,
        "owner_and_adjacent_reviewed": 21,
        "current_books_paths": sorted({spec["owner_path"] for spec in FINAL_INTEGRATE.values()} | {
            "books/part-01-worldview/07-scaling-law.md",
            "books/part-04-training-system/28-pretraining.md",
            "books/part-04-training-system/33-grpo.md",
            "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
            "books/part-05-inference-system/56-inference-scheduling.md",
            "books/part-06-ai-infrastructure/66-evaluation-system.md",
            "books/part-06-ai-infrastructure/72-security.md",
            "books/part-07-agent/77-memory.md",
            "books/part-07-agent/81-workflow.md",
            "books/part-07-agent/82-multi-agent.md",
            "books/part-07-agent/83-mcp.md",
        }),
    },
    "result": {
        "integrate": sorted(FINAL_INTEGRATE),
        "no_change": sorted(DOWNGRADE),
        "integrate_count": len(FINAL_INTEGRATE),
        "no_change_count": len(DOWNGRADE),
        "shared_books_modified": False,
    },
    "decisions": [
        {
            "arxiv_id": aid,
            "source_family_id": f"SF-2026-ARXIV-{aid.replace('.', '-')}",
            "final_disposition": "Integrate" if aid in FINAL_INTEGRATE else "No Change — Existing Coverage",
            "owner_node": FINAL_INTEGRATE.get(aid, {}).get("owner"),
            "reason": FINAL_INTEGRATE.get(aid, {}).get("reason", DOWNGRADE.get(aid)),
        }
        for aid in sorted(FINAL_INTEGRATE | DOWNGRADE)
    ],
    "gate": {
        "books_prewrite": "Passed",
        "books": "Open",
        "completion": "In Progress",
        "next_condition": "root serial writeback for three families, followed by independent post-write semantic audit",
    },
    "unresolved_findings": [],
}
dump(ROOT / "books-prewrite-challenge.json", prewrite_audit)

queue = """# 2026-05-09 Books Writeback Queue — Final Prewrite Challenge

状态：`Root-serialized / not written`。独立 current-content challenge 将 21 项 evidence-complete provisional Integrate 收紧为 **3 项**；其余 18 项均由当前 Books 主线完整承载。本文件不表示 Books 已修改。

## Owner-merged narrative

三项只形成一条 `TRAIN-DISTRIBUTED-TRAINING` 演进链：训练通信最初把 payload 当作无类型 bytes；规模、异构拓扑与解耦 rollout 使真正需要维护的是 **typed communication state**。policy 发布应绑定 base checkpoint、稀疏 update、target epoch 与重构验证；Context Parallel plan 应绑定 sequence/head ownership、topology、buffer 与 plan epoch；loss recovery 应理解 collective message/round ownership，但仍保持 exact completion 和可靠 fallback。三者不能被写成三个产品段落。

| Source Family | Durable delta | Required boundary |
| --- | --- | --- |
| `SF-2026-ARXIV-2605-07330` | Trainer→Rollout 从完整 weight copy 演进为可验证重构的 sparse policy update。 | 稀疏性漂移、index/bucket/control overhead 或重构失败时回退完整 snapshot；不外推作者压缩率。 |
| `SF-2026-ARXIV-2605-08524` | CP 从固定 All-to-All 演进为 topology-aware fully-connected exchange plan。 | fabric/buffer/ordering/plan epoch 不满足时回退规则 collective；不外推特定 topology throughput。 |
| `SF-2026-ARXIV-2606-20582` | recovery 从 transport-byte retransmit 演进为 collective-semantic-aware round recovery。 | 语义/round identity 不完整、loss 超界或恢复证据不足时回退可靠重传/整轮 retry；模拟不构成生产 tail 保证。 |

## No Change closure

其余 18 项的逐 family current-content comparison 位于 `books-current-content-comparison.json` 与 `books-prewrite-challenge.json`。它们不是低分或被忽略，而是经 owner+adjacent 重读后判定现有正文已覆盖长期机制。
"""
(ROOT / "BOOKS_WRITEBACK_QUEUE_FINAL.md").write_text(queue)

print("05-09 books prewrite challenge: 21 -> 3 Integrate, 18 No Change; Books untouched")
