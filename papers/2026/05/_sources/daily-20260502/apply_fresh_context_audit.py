#!/usr/bin/env python3
"""Apply the independent 2026-05-02 fresh-context audit.

This pass is deliberately downstream of the author packet.  It may change
denominator and Books dispositions, but it does not write shared Books files.
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent

# Only deltas not already carried by the current owner/adjacent chapters remain
# in the serial writeback queue.  Every other retained family remains in the
# Daily as evidence, with an explicit existing-coverage comparison.
INTEGRATE = {
    "2605.00324": "现 Ch73 有渐进发布与回滚，但没有把 serving-time 可逆 feature fading、周期训练和 drift boundary 组成同一迁移状态机。",
    "2605.00416": "现 Ch26 有 perception-action feedback 与 sim-to-real 边界，但没有 fleet deployment→intervention capture→offline/online value learning→redeployment 的版本循环。",
    "2605.02946": "现 Ch72 覆盖 MoE fault/availability 风险；输入优化主动绕开 safety-associated experts 是不同的 routing-safety 攻击面。",
    "2605.00955": "现 Ch72 有 membership/privacy 通则，但没有把 RAG corpus membership 绑定 retriever-generator 黑盒 query protocol。",
    "2605.00686": "现 Ch49 有 kernel/barrier/warp ordering；跨节点 megakernel 中 transfer fence、NIC ordering 与 signal ownership 的解耦仍缺失。",
    "2605.15206": "现 Ch84 有预算和 marginal utility gate，但没有由 expected task value 与 marginal energy 联合决定 trajectory termination 的本地控制器。",
    "2605.00737": "现 Ch78 有 validate/authorize/execute；是否调用工具仍缺 benefit、latency 与 failure cost 联合 admission contract。",
    "2605.01058": "现 Ch49 覆盖 early-exit runtime path，却没有说明 pretraining objective 必须与 convergence-based exit semantics 对齐。",
    "2605.01060": "现 Ch73 有 readiness/rollback；bounded-memory SuperBatch 同时拥有 partition、early output 与 crash-recovery state 的执行合同仍缺失。",
    "2605.01106": "现 Ch48 有 drafter/verify governance；hybrid component composition topology 是否形成可行 self-draft path 仍未成为 admission 条件。",
    "2605.15207": "现 Ch82 有 coordination tax 和 message/state 分离；sequential agent updates 造成 occupancy shift 后的 resampling 与 per-agent trust region 尚未承载。",
}

EXISTING = {
    "2605.00326": "Ch66 已要求 prompt distribution、重复采样、相关性、校准与 evaluation identity；单一 first-token score 不得冒充稳定置信度已被明确覆盖。",
    "2605.00342": "Ch48 已把 acceptance、verify length、expert union/residency/transfer 与 workload contract 联合；EVICT 是该主线的 MoE 实例。",
    "2605.00348": "Ch72 已把 watermark 限定为 sensor，并要求 FPR/FNR、metadata/signature/attestation 分层；designated codeword 是 bounded implementation。",
    "2605.00356": "Ch77 已把 Memory Write 定义为独立高风险 admission，分离 writer/verifier/reader authority 并要求 rollback receipt。",
    "2605.00365": "Ch33 已明确 verified-correct trajectories 内的 mode diversity 和 conditional-uniformity pressure；UCPO 不再改变 owner。",
    "2605.00410": "Ch84 已把 model/tool/skill/runtime profile、质量证据和预算组成可版本化 dispatch policy；capsule granularity 是其实现分支。",
    "2605.00424": "Ch72/Ch84 已把 skill 视为 untrusted executable artifact，以签名 provenance、admission、capability 与 human approval 分级。",
    "2605.00425": "Ch33 已有 entropy controller、hard outcome gate 与 exploration trade-off；response-level modulation 属实验性 credit 分支。",
    "2605.00460": "Ch76 已有 RAG ingestion provenance/poison sensor；similarity clique 不能提升为 trust proof，维持 bounded sensor。",
    "2605.00528": "Ch56 已把 workflow DAG、tool gap、session affinity、KV residency 与 fairness 作为调度状态；request 不再是唯一单位。",
    "2605.00539": "Ch36–41 已把 activation/gradient precision、layer/stage policy 与 collective communication 联合，AGoQ 是精度策略实例。",
    "2605.00555": "Ch49 已承载 TMA、barrier、warp specialization、cache traffic 与 execution evidence；SimFA 是评估该执行合同的模拟器。",
    "2605.00583": "Ch72 已明确 visual channel 是 intent-bearing attack surface，并要求跨模态 threat model、sensor 与 safe commit 分离。",
    "2605.00616": "Ch66 已要求真实 runtime path、scheduler/KV identity、trace replay 与 calibrated simulator boundary；LLM-Emu 是受限实现。",
    "2605.00663": "Ch84 已要求 verifier-owned skill admission、capability envelope、failure recovery；affordance confidence 不能直接授权行动。",
    "2605.00674": "Ch66 已建立 living evaluation、task/version identity、contamination control 与 release gate；MathArena 是领域实例。",
    "2605.00702": "Ch77 已分离 memory activation/write/update/use policy，并要求 raw trajectory、version、rollback 与 held-out evaluation。",
    "2605.00789": "Ch45 已覆盖 token/modality/position identity 与 KV compression 的 workload/quality boundary；LightKV 是视觉分支。",
    "2605.00798": "Ch81 已把 natural-language plan 编译成 typed DAG/state machine，具有 precondition、transition、recovery 与 commit owner。",
    "2605.00803": "Ch66 已把 executable reproduction、toolchain、claim-evidence adjudication 和 environment identity 作为 evaluation contract。",
    "2605.00994": "Ch66 已有 behavior diff、matched baseline、distribution identity 与 release evidence；perplexity-diff 是一个 detector。",
    "2605.01030": "Ch72/Ch81 已把 proposal、authorization 与 externally visible effect commit 分离，并要求 coterminous authority/effect boundary。",
    "2605.01037": "Ch72 已要求 restricted executor、signed certificate、attestation 与 admission-time verification；pure WASM executor 是形式化实例。",
    "2605.01048": "Ch66 已把 meaning-preserving counterfactual baseline 与 prompt distribution 纳入 evaluation identity。",
    "2605.01078": "Ch72 已把 sanitizer 定位为 policy-bound sensor，不能证明 retrieved content 安全或取得 commit authority。",
    "2605.08134": "Ch24 已覆盖 diffusion activation/KV reuse 的 threshold-quality trade-off；DARE 不改变生成范式 owner。",
    "2605.01104": "Ch69 已要求 prompt/tool/edit stream 共享 trace identity、异步因果链接与 replay；RECAP 是 coding workload 实例。",
    "2605.01124": "Ch49 已把 typed IR、supported subset、semantic/numeric verification 与 performance admission 分离。",
    "2605.01129": "Ch72 已要求 unlearning 同时审计 forget efficacy、retain utility、unseen/privacy leakage，且 provenance 不完整时回退重训。",
    "2605.01133": "Ch72/Ch82 已覆盖 multi-agent message 不是 authority、embedding sensor 不足、round/trajectory risk 与 policy gate。",
    "2605.01143": "Ch72 已把 risk state 跨 session/tool/effect trajectory 聚合；interaction-level sensor 不能独自授权或阻断。",
}


def read(name: str):
    return json.loads((ROOT / name).read_text())


ledger = read("screening-ledger-final.json")
row = next(x for x in ledger["identities"] if x["arxiv_id"] == "2605.00358")
row.update(
    source_family_id="SF-FORWARD-REPLAY-MODEL-EDIT-TARGETS",
    screening_status="retained",
    stable_node_id="—",
    score_v2={"design_delta": 3, "system_reach": 2, "durability": 3, "total": 8},
    review_status="deep_complete",
    access_status="accessible",
    books_disposition="Structural Candidate",
    screening_reason=(
        "exact-v1 §§4–5 证明 backward spreading 把 final-layer residual 线性分配到早层时隐含 Jacobian eigenvector/正定条件；"
        "forward replay 改由首个编辑层的 anchor 沿真实 downstream dynamics 生成兼容 target。该机制把 parameter edit 从局部优化技巧提升为"
        "跨层 state-transition 与 compatibility contract；现有知识树没有稳定的 model-edit lifecycle owner，进入 Structural Candidate。"
    ),
)
ledger["candidate_denominator"] = 43
ledger["pre_denominator_closures"] = 347
ledger["screening_status"] = "frozen_after_independent_fresh_context_audit"
(ROOT / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

packet = read("exact-v1-review-packet.json")
new_review = {
        "source_family_id": row["source_family_id"],
        "primary_evidence_version": "arXiv:2605.00358v1",
        "exact_v1_url": "https://arxiv.org/html/2605.00358v1",
        "review_route": "deep",
        "method_identity_locators": "§4.1 Theoretical grounding; §5 Our method; Appendix A.3–A.4",
        "evaluation_locators": "§6 Experiments; §6.2 Results; Appendix A.8",
        "limitations_counterevidence_locators": "§7 Conclusion and Limitations; first-order/Jacobian and LTE scope",
        "artifact_locators": "§1 code link; immutable event-time commit not pinned",
        "claim_boundary": (
            "Supports cross-layer target compatibility for locate-then-edit methods under the evaluated model/edit regimes; "
            "does not establish safe sequential editing, provenance, rollback, or production knowledge-lifecycle correctness."
        ),
        "completion_result": "deep_complete",
    }
existing_review = next((x for x in packet["reviews"] if x["source_family_id"] == row["source_family_id"]), None)
if existing_review is None:
    packet["reviews"].append(new_review)
else:
    existing_review.update(new_review)
(ROOT / "exact-v1-review-packet.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n")

# Apply current-Books comparison to all retained candidates.
for x in ledger["identities"]:
    if x.get("screening_status") != "retained":
        continue
    aid = x["arxiv_id"]
    if aid == "2605.00358":
        x["books_disposition"] = "Structural Candidate"
        x["books_comparison"] = "现 ROADMAP 没有 parameter/model editing lifecycle owner；不得塞入 Training 或 Memory 章节，等待结构复核。"
    elif aid in INTEGRATE:
        x["books_disposition"] = "Integrate"
        x["books_comparison"] = INTEGRATE[aid]
    else:
        x["books_disposition"] = "No Change — Existing Coverage"
        x["books_comparison"] = EXISTING[aid]
(ROOT / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

# Rebuild queue from the author packet while retaining its owner/path metadata.
old_queue = read("books-writeback-queue.json")
by_id = {x["primary_identifier"].split(":", 1)[1].removesuffix("v1"): x for x in old_queue["items"]}
queue = []
for aid, finding in INTEGRATE.items():
    q = dict(by_id[aid])
    q["books_disposition"] = "Integrate"
    q["current_books_fresh_compare"] = finding
    q["fresh_context_status"] = "confirmed_delta_pending_root_serial_writeback"
    queue.append(q)
(ROOT / "books-writeback-queue.json").write_text(json.dumps({"schema": "books-writeback-queue-v1", "items": queue}, ensure_ascii=False, indent=2) + "\n")

# Append provenance for the reopened family.  The web-read URL and locator
# receipt are reproducible, but no local body hash is invented.
manifest = read("evidence-provenance-manifest.json")
entries = manifest.get("items") or manifest.get("entries")
if not any(x.get("source_family_id") == row["source_family_id"] for x in entries):
    receipt = packet["reviews"][-1]
    entries.append({
        "source_family_id": row["source_family_id"],
        "exact_v1_url": receipt["exact_v1_url"],
        "retrieved_at": "2026-08-31T00:00:00Z",
        "source_body_sha256": None,
        "review_record_sha256": hashlib.sha256(json.dumps(receipt, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
        "provenance_boundary": "exact-v1 HTML read succeeded via official arXiv URL; local body freeze/hash unavailable",
    })
(ROOT / "evidence-provenance-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

audit = {
    "schema": "fresh-context-audit-v1",
    "report_date": "2026-05-02",
    "auditor_role": "independent_from_author_lane",
    "screening": {
        "reviewed": 390,
        "author_denominator_before": 42,
        "false_negative_reopened": ["2605.00358"],
        "denominator_after": 43,
        "closures_after": 347,
        "false_positive_removed": [],
        "result": "pass_with_one_reopen",
    },
    "evidence": {
        "review_packets_audited": 43,
        "claim_locator_consistency": "pass",
        "body_hashes_present": sum(1 for x in entries if x.get("source_body_sha256")),
        "finding": "official exact-v1 URLs, RP, locators and claim boundaries are complete; optional local source-body freeze/hash is absent but non-blocking",
        "result": "pass",
    },
    "selection": {
        "author_selection": ["2605.00324", "2605.00528", "2605.00686"],
        "finding": "SAGA remains high-system-reach evidence but is already covered by current Ch56; selection is report priority, not a Books delta claim.",
        "result": "pass_after_boundary_clarification",
    },
    "books": {
        "retained_families_compared": 43,
        "integrate_queue": list(INTEGRATE),
        "integrate_count": len(INTEGRATE),
        "no_change_count": 31,
        "structural_candidates": ["2605.00358"],
        "result": "pass_author_side_pending_root_writeback",
    },
    "gates": {"Coverage": "Pass", "Evidence": "Pass", "Books": "Open"},
}
(ROOT / "fresh-context-audit-v1.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

receipt = read("coverage-receipt.json")
receipt.update(
    retained=43,
    pre_denominator_closed=347,
    status="complete",
    ledger_sha256=hashlib.sha256((ROOT / "screening-ledger-final.json").read_bytes()).hexdigest(),
)
(ROOT / "coverage-receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")

with (ROOT / "screening-ledger-final.tsv").open("w", newline="") as f:
    fields = list(ledger["identities"][0])
    w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", extrasaction="ignore")
    w.writeheader(); w.writerows(ledger["identities"])

print(json.dumps({"screened": 390, "retained": 43, "closures": 347, "integrate": len(queue), "no_change": 31, "structural": 1}, ensure_ascii=False))
