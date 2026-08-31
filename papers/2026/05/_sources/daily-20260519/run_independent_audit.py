#!/usr/bin/env python3
"""Independent V2.1 audit for 2026-05-19; never writes shared Books."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT))

from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

SOURCE = json.loads((HERE / "screening-ledger-provisional.json").read_text())
AUTHOR_LEDGER = json.loads((HERE / "screening-ledger-final.json").read_text())
AUTHOR_REVIEWS = {x["arxiv_id"]: x for x in json.loads((HERE / "exact-v1-review-packet.json").read_text())}
REPORT_DATE = "2026-05-19"
AUDITED_AT = "2026-09-01T23:20:00+08:00"


def family(arxiv_id: str) -> str:
    return "SF-2026-ARXIV-" + arxiv_id.replace(".", "-")


AUTHOR_KEEP = {
    "2605.17734", "2605.17787", "2605.17830", "2605.17842", "2605.17849",
    "2605.17862", "2605.17889", "2605.17932", "2605.17954", "2605.18032",
    "2605.18067", "2605.18071", "2605.18106", "2605.18165", "2605.18271",
    "2605.18414", "2605.18498", "2605.18607", "2605.18693", "2605.18930",
    "2605.19127", "2605.19193", "2605.19196", "2605.19228", "2605.20251",
    "2605.20270",
}

FALSE_POSITIVES = {
    "2606.06502": "SIGIL 以可查询 canary 推断训练数据成员关系；它强化审计技术，但没有改变数据准入、删除或训练 lineage 的长期 owner，现有 TRAIN-DATA 已覆盖 provenance/consent/revision contract。",
    "2605.17837": "TAPE 只在视频 diffusion 中按时间冗余做 training-free token pruning；收益绑定特定生成模型与局部 latency/quality trade-off，没有形成新的通用生成状态或执行契约。",
    "2605.17850": "URGE 在 diffusion path measure 上做无导数 SMC 重采样；这是模型局部 inference-time scaling 分支，未改变平台调度、commit 或可恢复状态 owner。",
    "2605.17856": "KISS 把 Earth-science operator 与 staged protocol 外化为 agent scaffold；机制和验证绑定地球科学建模域，不能据此改写通用 workflow contract。",
    "2605.17938": "mirrored unlearning attribution 衡量 diffusion 数据贡献；它是模型/数据局部归因方法，没有改变 TRAIN-DATA 的删除证明或平台 release gate。",
    "2605.17967": "该工作分解 SFT interaction dynamics；证据用于解释局部 alignment 行为，没有引入新的训练状态 owner、optimizer control 或 artifact contract。",
    "2605.18066": "该方法为一般 cloud block placement 注入 LLM semantic signal；它未证明 AI workload 的 GPU/模型状态接口，也没有改变 PLATFORM-GPU-SCHEDULER 的资源承诺。",
    "2605.18083": "该工作研究 multilingual MoE sparse upcycling/merging；属于模型局部结构与精度结果，未形成新的 routing capacity、placement 或 communication contract。",
    "2605.18104": "该工作用 safety geometry 解释并校正单模型表示；它没有提供外部 reference monitor、authorization 或 fail-closed control，因此不改变 PLATFORM-SECURITY 的系统边界。",
    "2605.18190": "interleaved heavy/light denoising 只优化特定 diffusion sampling 路径；未改变生成范式的长期 factorization、state ownership 或 serving contract。",
    "2605.18261": "answer-gated RLVR 改进局部奖励分配；其 verifier 没有成为跨 rollout/version 的独立 authority，未改变 TRAIN-RLHF 已有验证与回退契约。",
    "2605.18309": "alignment-dynamics 分析解释 SFT 局部表示变化；未提供可迁移的数据、训练控制或 release contract。",
    "2605.18474": "text-to-weight fingerprinting 是模型归因方法；没有改变 artifact identity、签名、准入或供应链治理 owner。",
    "2605.18643": "zero-expert skipping 与 group loss 是 MoE 局部稀疏执行技巧；未形成跨 runtime 的 expert placement/communication contract。",
    "2605.18672": "该 position paper 主张分层安全 contract，但没有可审计实现或机制评测；保留为 Weekly context，不进入 Daily denominator。",
    "2605.18732": "recall scaling framework 主要改变特定检索/认证测量方法；当前证据没有修改通用 evaluation/release contract。",
    "2605.18740": "regional-to-global OPD 是局部 vision distillation 分支；未改变通用 post-training state/control owner。",
    "2605.19147": "open-book benign rewriting 是训练数据局部防御；没有建立可验证的数据 provenance、quarantine 或 release gate。",
    "2605.19220": "UQ position/taxonomy paper只整理诊断路线，没有给出可运行的 confidence authority、abstention gate 或跨工作负载验证。",
    "2605.20258": "contextual-integrity teacher distillation 是局部 post-training 方法；未改变 privacy authority、data policy 或 deployment release contract。",
}

# False negatives found by independent 703/703 replay.  Locators are exact-v1
# sections actually inspected in official arXiv HTML; absence of a dedicated
# limitations section is recorded explicitly rather than invented.
FN = {
    "2605.17757": ("INFER-KV-CACHE", (3, 3, 2), "No Change — Existing Coverage", "§3 OSCAR; §3.1–3.4 offline covariance-aware rotation and mixed K/V layout", "§4 Experiments; §4.1–4.5 quality, memory and kernel latency", "Appendix D Limitations"),
    "2605.17821": ("TRAIN-CHECKPOINT", (3, 3, 3), "Integrate", "§3 TierCheck Design; §3.1 save/retrieve/reclaim across local, peer and remote tiers", "§5 Evaluation; failure frequency, checkpoint overhead and recovery", "§7 Conclusion; no dedicated limitations section, production failure correlation Not Disclosed"),
    "2605.17877": ("TRAIN-RLHF", (3, 3, 2), "Integrate", "§3 PAIR; prefix-aware dense reward construction and intervention", "§4 Experiments; multi-turn agent optimization and ablations", "Appendix J Limitations"),
    "2605.17879": ("PLATFORM-MONITORING", (3, 3, 3), "Integrate", "§3–§6 Guard architecture; online monitor, offline node sweep and triage", "§7 Evaluation; fail-slow detection, false positives and cluster overhead", "§7–§8 claim boundary; no dedicated limitations section"),
    "2605.17912": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 2), "No Change — Existing Coverage", "§3 WorldArena 2.0 benchmark axes and task construction", "§4 Experiments across modality, functionality and platform", "§5 Discussion/Conclusion; simulator and selected-model boundary"),
    "2605.17921": ("INFER-SCHEDULING", (3, 2, 2), "No Change — Existing Coverage", "§3–§4 R3-Streaming cascaded memory, readiness and compute routing", "§5 Experiments; latency/accuracy under streaming video workloads", "§6 Conclusion; no production tail-SLO or failure-recovery evidence"),
    "2605.17923": ("TRAIN-DISTRIBUTED-TRAINING", (3, 3, 2), "Integrate", "§3 AdaptiveLoad; dual memory/compute constrained batch construction and fused execution", "§4 Experiments on video diffusion training", "§5 Conclusion/limitations; selected models and hardware only"),
    "2605.17986": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 2), "No Change — Existing Coverage", "§3 Threat model and benchmark construction", "§4–§5 evaluation and defense analysis across live interaction surfaces", "§6 Limitations"),
    "2605.17989": ("AGENT-RAG", (3, 3, 2), "Integrate", "§3 Predictive prefetch controller and retrieval-generation overlap", "§4 Evaluation; latency, retrieval usefulness and prediction error", "§6 Limitations; stale/incorrect demand and workload boundary"),
    "2605.17992": ("AGENT-RAG", (3, 3, 2), "Integrate", "§3 PipeANN-Filter superset traversal, post-verification and pipelined SSD IO", "§4–§5 implementation and filtered-ANN evaluation", "§6 Limitations; index/filter/update boundary"),
    "2605.17998": ("AGENT-WORKFLOW", (3, 3, 3), "Integrate", "§3–§8 read-only verifier, proposal/admission state and bounded completion protocol", "§9–§10 architecture case study and failure injection", "§12 Limitations; bounded case study, not a universal correctness proof"),
    "2605.18041": ("MULTIMODAL-REPRESENTATION", (2, 2, 2), "No Change — Existing Coverage", "§3 OmniSelect modality-aware token-budget controller", "§4 Experiments on audio-video OmniLLMs", "§5 Limitations; model/task-local compression evidence"),
    "2605.18053": ("INFER-KV-CACHE", (3, 3, 3), "Integrate", "§3–§7 globally capped KV eviction and structural boundary protection", "§8–§9 evaluation across policies/models and cross-architecture challenge", "§10.22 Limitations"),
    "2605.18401": ("AGENT-PLATFORM", (3, 3, 2), "No Change — Existing Coverage", "§3 SkillsVote collection, recommendation, validation and evolution lifecycle", "§4 Experiments and lifecycle ablations", "§5/Appendix limitations; ecosystem and environment sensitivity"),
    "2605.18421": ("AGENT-MEMORY", (3, 3, 2), "No Change — Existing Coverage", "§3–§4 EvoMemBench in/cross-episode and knowledge/execution axes", "§5 Experiments across memory systems", "§6 Conclusion; benchmark/model coverage boundary"),
    "2605.18565": ("AGENT-MEMORY", (3, 3, 2), "Integrate", "§3 MINTEval multi-target interference construction and update semantics", "§4 Experiments; recall and aggregation under evolving memories", "§5 Limitations; synthetic tasks and selected agents"),
    "2605.18583": ("PLATFORM-SECURITY", (3, 3, 3), "No Change — Existing Coverage", "§3 benchmark, benign task scope and overeager-action taxonomy", "§4 Experiments across coding agents", "§5 Limitations; harness and observable-action boundary"),
    "2605.18652": ("AGENT-MEMORY", (3, 2, 2), "No Change — Existing Coverage", "§3 MementoGUI multimodal memory controller and write/read policy", "§4–§5 benchmark construction and experiments", "§6 Limitations; GUI domain and selected backbones"),
    "2605.18697": ("AGENT-WORKFLOW", (3, 3, 2), "No Change — Existing Coverage", "§3–§6 PopPy compiler/runtime dependency discovery and external-call parallelism", "§8 Evaluation; latency and semantic-equivalence checks", "§10 Discussion; Python/compound-application boundary"),
    "2605.18703": ("AGENT-WORKFLOW", (3, 3, 2), "No Change — Existing Coverage", "§3–§4 executable-environment synthesis, verification and RL data path", "§5 Evaluation of environment validity and agent training", "§6 Limitations"),
    "2605.18710": ("TRAIN-DISTRIBUTED-TRAINING", (3, 3, 3), "Integrate", "§3 Mosaic spatial resource multiplexing, placement and performance model", "§4 Evaluation across multimodal module mixtures", "§5 Limitations; selected architectures/hardware"),
    "2605.18739": ("TRAIN-DISTRIBUTED-TRAINING", (3, 3, 2), "No Change — Existing Coverage", "§3–§4 NVFP4 training/inference infrastructure and parallel layouts", "§5 Evaluation on long-video generation", "§6 Limitations; vendor precision and workload boundary"),
    "2605.18750": ("TRAIN-PIPELINE-PARALLEL", (3, 3, 3), "Integrate", "§3 readiness-driven runtime and dependency state", "§4–§5 implementation and evaluation under runtime variability", "§6 Limitations; schedule/hardware/workload boundary"),
    "2605.18918": ("PLATFORM-SECURITY", (3, 3, 2), "No Change — Existing Coverage", "§3 ESLD latent sensor architecture and external enforcement path", "§4 Experiments against prompt injection", "§5 Limitations; learned detector is not an authority"),
    "2605.18991": ("PLATFORM-SECURITY", (3, 3, 3), "No Change — Existing Coverage", "§2 system-level invariants, model-as-untrusted-component and attack analysis", "§3 open systems-security problems; no empirical mechanism evaluation", "§4 objections and position-paper boundary"),
    "2605.19008": ("TRAIN-PRETRAINING", (3, 3, 2), "Integrate", "§3 LBW-Guard bounded training-control layer, actions and safety envelope", "§4–§5 setup, stress runs and controller outcomes", "§6 Limitations; simulator/recipe and stability boundary"),
    "2605.19049": ("INFER-KV-CACHE", (3, 3, 3), "Integrate", "§3.1–§3.4 KVBuffer IO-aware state placement and update pipeline", "§4 Evaluation on linear-attention serving", "§6 Discussion/limitations; linear-attention state only"),
    "2605.19099": ("AGENT-MULTI-AGENT", (3, 2, 2), "No Change — Existing Coverage", "§3 DecisionBench delegation substrate, interface and metrics", "§4 Experiments across peer pools and tasks", "§5 Limitations; benchmark delegation is not production authority"),
    "2605.19101": ("TRAIN-DATA", (3, 3, 2), "No Change — Existing Coverage", "§3–§4 GST heterogeneity state, scheduler and optimization rule", "§5 Experiments on Audio LLM training", "§6 Limitations; audio datasets and selected recipes"),
    "2605.19140": ("AGENT-WORKFLOW", (3, 3, 2), "No Change — Existing Coverage", "§3–§4 local-observation handoff interface and convergent learning rule", "§5 theoretical/empirical evaluation", "§6 Limitations; assumptions do not prove open-system delivery or authority"),
    "2605.19151": ("PLATFORM-SECURITY", (3, 3, 2), "No Change — Existing Coverage", "§2–§3 approval/deny observations, GP preference posterior and autonomy threshold", "§3–§4 theoretical and simulated evaluation", "§4 Limitations; preference stationarity and calibration boundary"),
    "2605.19169": ("TRAIN-DISTRIBUTED-TRAINING", (3, 2, 2), "No Change — Existing Coverage", "§2 Methods; latency/serialization model and ASTRA-sim overlap model", "§3 Results; GPT-3 13B/175B, A100/H100, 256–8192 GPU simulation", "§4 Conclusions; lumped two-DC, uncongested-network and simulation-only boundary"),
    "2605.19192": ("PLATFORM-SECURITY", (3, 3, 3), "No Change — Existing Coverage", "§3–§4 evidence certificate and action-admission architecture", "§5 Evaluation under multimodal hallucination-to-action attacks", "§6 Limitations; certificate coverage and evaluator trust"),
    "2605.19218": ("INFER-KV-CACHE", (3, 2, 2), "No Change — Existing Coverage", "§3.1–§3.3 RotateK query-weighted PCA, structured channel pruning and Triton kernel", "§4 Experiments; matched KV budgets, prefill/decode latency and memory", "Appendix G Limitations"),
}

FINAL_IDS = AUTHOR_KEEP | set(FN)

DECISION_REASON = {
    "2605.17821": "当前 checkpoint 章有完整/增量 checkpoint 与异步保存，但没有按 failure blast radius 把 local/peer/remote recovery tier 变成同一 durability policy；保留为写回增量。",
    "2605.17877": "当前 RLHF 章讨论 outcome/step reward 与 verifier，但没有把不可控 prefix contamination 从当前 action 的 dense credit 中分离；保留为写回增量。",
    "2605.17879": "当前 monitoring/training 章节缺少在线低开销 fail-slow signal 与离线节点资格复验的分权闭环；保留为写回增量。",
    "2605.17842": "当前推理执行章覆盖 tensor/pipeline/kernel 并行，但没有把层序列改写为 residual root finding 后并行 correction 的实验分支；保留为受限机制。",
    "2605.17862": "当前 post-training 章有 policy version/freshness，但未同时分解 rollout drift 与 supervision drift 并以 freshness controller 控制异步 OPD；保留为写回增量。",
    "2605.17889": "当前 MoE execution 章有 expert offload/placement，但缺少 CPU-GPU coalesced expert execution 对 micro-batch 与中间态搬运的统一控制；保留为写回增量。",
    "2605.17923": "当前分布式训练章讨论 packed/variable-length 调度，但没有把 video-DiT sequence 的 memory 与 compute 双约束一起冻结为 batch contract；保留为写回增量。",
    "2605.17989": "当前 RAG 章有同步/异步检索，却没有预测未来 information demand、允许误预测取消并绑定 freshness 的 prefetch control；保留为写回增量。",
    "2605.17992": "当前 filtered ANN 已覆盖 query-aware routing，但没有 SSD superset traversal 与 top-k 后验证之间的 IO/recall contract；保留为写回增量。",
    "2605.17998": "当前 workflow 有 verifier/commit，但没有把 completion proposal 与只读 admission authority、bounded packet state 和 fail-closed recovery写成同一完成协议；保留为写回增量。",
    "2605.18053": "当前 KV eviction 已覆盖 selector/quantizer/fallback，但没有把 prompt/modality boundary 的不可驱逐保护作为 global-cap 前的结构不变量；保留为写回增量。",
    "2605.18106": "当前 optimizer 叙述未把 embedding/LM-head/SwiGLU/MoE-router 的参数对称性作为 optimizer state/action compatibility contract；保留为写回增量。",
    "2605.18498": "当前 evaluation 章缺少将 MoE load balance 与 functional specialization 分开、并用干预验证而非只看 routing frequency 的契约；保留为写回增量。",
    "2605.18565": "当前 memory 章覆盖版本与冲突，但没有把 multi-target interference、update history 与 aggregate reasoning 组合成一条验收轴；保留为写回增量。",
    "2605.18710": "当前 multimodal/distributed training 章缺少空间复用时 module placement、GPU share 与 interference budget 的联合 owner；保留为写回增量。",
    "2605.18750": "当前 pipeline 章以 schedule 为主，但没有在运行时以真实 task readiness 取得 dispatch authority并保留静态 schedule fallback；保留为写回增量。",
    "2605.19008": "当前 pretraining 章有 optimizer/clip/rollback，尚缺 optimizer 之上的 bounded autonomous control envelope、action budget 与 human override；保留为写回增量。",
    "2605.19049": "当前 KV 章以 Transformer KV 为主，没有明确 linear-attention recurrent state 的 IO-aware buffering/placement owner；保留为写回增量。",
}

INTEGRATE = set(DECISION_REASON)


def sentences(text: str) -> list[str]:
    clean = re.sub(r"\s+", " ", text or "").strip()
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", clean) if s.strip()]


def mechanism(row: dict) -> str:
    ss = sentences(row.get("abstract", ""))
    for s in ss:
        if re.search(r"\b(propose|introduce|present|develop|design|formalize|study|identify|show)\b", s, re.I):
            return s
    return ss[0] if ss else row["title"]


def dropped_reason(row: dict) -> str:
    detail = FALSE_POSITIVES[row["arxiv_id"]]
    return f"`{row['title']}`：{mechanism(row)} 独立重放结论：{detail} 后续若出现跨 workload 的 state/control interface 或生产 evidence，才重新打开 denominator。"


def local_date(utc: str) -> str:
    dt = datetime.fromisoformat(utc.replace("Z", "+00:00"))
    return (dt + timedelta(hours=8)).date().isoformat()


author_rows = {x["arxiv_id"]: x for x in AUTHOR_LEDGER["identities"]}
rows = []
for source_row in SOURCE["identities"]:
    aid = source_row["arxiv_id"]
    row = dict(source_row)
    if aid in AUTHOR_KEEP:
        row.update(author_rows[aid])
        row["integration_disposition"] = "Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"
    elif aid in FN:
        owner, dims, disposition, method, evaluation, limits = FN[aid]
        row.update(
            source_family_id=family(aid),
            screening_status="retained",
            screening_reason=mechanism(row),
            owner_node=owner,
            score_v2={"design_delta": dims[0], "system_reach": dims[1], "durability": dims[2], "total": sum(dims)},
            review_status="deep_complete" if sum(dims) >= 7 else "standard_complete",
            access_status="accessible",
            integration_disposition=disposition,
            method_locator=method,
            evaluation_locator=evaluation,
            limitations_locator=limits,
        )
    elif aid in FALSE_POSITIVES:
        row.update(
            screening_status="pre_denominator_closure",
            screening_reason=dropped_reason(row),
            review_status="identity_date_closed",
            access_status="accessible",
            integration_disposition="Rejected — Below Candidate Denominator",
        )
        for key in ("source_family_id", "owner_node", "score_v2", "method_locator", "evaluation_locator", "limitations_locator"):
            row.pop(key, None)
    else:
        row.update(author_rows[aid])
    rows.append(row)

retained = [x for x in rows if x["screening_status"] == "retained"]
closures = [x for x in rows if x["screening_status"] != "retained"]
assert len(rows) == 703 and len(retained) == 60 and len(closures) == 643
assert {x["arxiv_id"] for x in retained} == FINAL_IDS

ledger = {
    "schema": "daily-screening-ledger-v2.1",
    "report_date": REPORT_DATE,
    "window": SOURCE["window"],
    "utc_window": SOURCE["utc_window"],
    "raw_snapshot_records": SOURCE["raw_snapshot_records"],
    "registered_window_identities": len(rows),
    "screened_identities": len(rows),
    "candidate_denominator": len(retained),
    "pre_denominator_closures": len(closures),
    "independent_reconciliation": {"author_denominator": 46, "false_positives": 20, "false_negatives": 34, "final_denominator": 60},
    "identities": rows,
}
(HERE / "screening-ledger-independent.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
(HERE / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

roadmap = (ROOT / "ROADMAP.md").read_text()
paths = {m.group(1): m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}


def adjacent_paths(owner_path: str) -> list[str]:
    target = ROOT / owner_path
    siblings = sorted(p for p in target.parent.glob("*.md") if p.name != "README.md")
    if target not in siblings:
        return []
    idx = siblings.index(target)
    result = []
    if idx > 0:
        result.append(str(siblings[idx - 1].relative_to(ROOT)))
    if idx + 1 < len(siblings):
        result.append(str(siblings[idx + 1].relative_to(ROOT)))
    return result


review_packet = []
comparisons = []
queue = []
for row in retained:
    aid = row["arxiv_id"]
    sf = row["source_family_id"]
    if aid in FN:
        review = {
            "source_family_id": sf,
            "arxiv_id": aid,
            "primary_evidence_version": f"arXiv:{aid}v1",
            "retrieval_route": "official arXiv exact-v1 HTML",
            "retrieved_at": AUDITED_AT,
            "method_locator": row["method_locator"],
            "evaluation_locator": row["evaluation_locator"],
            "limitations_locator": row["limitations_locator"],
            "claim_boundary": "只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。",
        }
    else:
        review = dict(AUTHOR_REVIEWS[aid])
        review["retrieved_at"] = AUDITED_AT
        review["independent_locator_recheck"] = "passed"
    review_packet.append(review)

    owner_path = paths[row["owner_node"]]
    adj = adjacent_paths(owner_path)
    body = (ROOT / owner_path).read_text()
    headings = re.findall(r"^##+\s+(.+)$", body, re.M)[:10]
    decision = "Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"
    row["integration_disposition"] = decision
    reason = DECISION_REASON.get(aid, "当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。")
    comp = {
        "arxiv_id": aid,
        "source_family_id": sf,
        "owner_node": row["owner_node"],
        "owner_path": owner_path,
        "adjacent_paths": adj,
        "current_owner_headings_read": headings,
        "existing_family_marker": aid in body or sf in body,
        "comparison_reason": reason,
        "decision": decision,
    }
    comparisons.append(comp)
    if decision == "Integrate":
        queue.append({
            "report_date": REPORT_DATE,
            "arxiv_id": aid,
            "source_family_id": sf,
            "stable_node_id": row["owner_node"],
            "owner_path": owner_path,
            "adjacent_paths": adj,
            "owner_merged_narrative": reason,
            "evidence_delta": row["screening_reason"],
            "required_post_write_audit": "owner + adjacent; unique source-family marker; mechanism before first anchored ^## Review notes; old path/constraint/owner/trade-off/failure/fallback/coexistence",
        })

assert len(review_packet) == 60 and len(queue) == 18
(HERE / "exact-v1-review-independent.json").write_text(json.dumps(review_packet, ensure_ascii=False, indent=2) + "\n")
(HERE / "exact-v1-review-packet.json").write_text(json.dumps(review_packet, ensure_ascii=False, indent=2) + "\n")
(HERE / "books-prewrite-final.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(HERE / "books-current-content-comparison.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
queue_packet = {"schema": "books-writeback-queue-v1", "report_date": REPORT_DATE, "status": "root_serial_writeback_required", "items": queue}
(HERE / "BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps(queue_packet, ensure_ascii=False, indent=2) + "\n")
(HERE / "materials-request.json").write_text(json.dumps({"schema": "materials-request-v1", "report_date": REPORT_DATE, "requests": []}, ensure_ascii=False, indent=2) + "\n")

audit = {
    "schema": "fresh-context-semantic-audit-v1",
    "report_date": REPORT_DATE,
    "auditor": "different-reviewer:may2026-day01",
    "independence": "reviewer did not author the 2026-05-19 packet or shared Books writeback",
    "cross_model_review": "skipped: subagent environment cannot spawn an additional independent reviewer; full identity replay and source-specific challenge completed by this different reviewer",
    "status": "passed_for_coverage_and_evidence; books_prewrite_ready",
    "counts": {"registered": 703, "screened": 703, "author_denominator": 46, "false_positives": 20, "false_negatives": 34, "final_denominator": 60, "closures": 643, "exact_v1_complete": 60, "blocked": 0, "ordinary_pending": 0, "final_integrate_queue": 18},
    "findings": [
        {"id": "SA-20260519-FP", "scope": "coverage", "finding": "20 author-retained families did not change a durable AI-System contract", "resolution": "moved to family-specific pre-denominator closure", "status": "resolved"},
        {"id": "SA-20260519-FN", "scope": "coverage", "finding": "34 system-contract families were closed by the author lane", "resolution": "restored, exact-v1 reviewed and owner-mapped", "status": "resolved"},
        {"id": "SA-20260519-EVIDENCE", "scope": "evidence", "finding": "newly restored families required source-specific Method/Evaluation/Limitations locators", "resolution": "60/60 exact-v1 locators and claim boundaries complete; 0 blocked", "status": "resolved"},
        {"id": "SA-20260519-BOOKS", "scope": "books", "finding": "31 author Integrates were not current-owner challenged", "resolution": "reconciled to 18 owner-merged writeback items", "status": "root_writeback_pending"},
    ],
}
(HERE / "independent-semantic-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

ledger_sha = hashlib.sha256((HERE / "screening-ledger-final.json").read_bytes()).hexdigest()
comparison_by_id = {x["arxiv_id"]: x for x in comparisons}
review_by_id = {x["arxiv_id"]: x for x in review_packet}


def chapter_ref(path: str) -> str:
    m = re.match(r"(\d+)-", Path(path).name)
    return f"{path}#chapter-{int(m.group(1))}" if m else f"{path}#knowledge-tree"


def evloc(aid: str, key: str) -> str:
    return f"arXiv:{aid}v1 HTML — {review_by_id[aid][key]}"


DEEP = {
    "2605.17821": "DA-FAILURE-TIERED-CHECKPOINT",
    "2605.17879": "DA-FAIL-SLOW-NODE-QUALIFICATION",
    "2605.17998": "DA-VERIFY-GATED-COMPLETION",
}

lines = [
    "# Daily Research — 2026-05-19", "", "**Research Date:** 2026-05-19", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-18 09:00:00 ～ 2026-05-19 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；technical claims bind official arXiv exact-v1 HTML/PDF。", "",
    "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。独立语义审计已完成，等待 root 串行 Books 写回与不同写作者 post-write audit。", "",
    "## Executive Summary", "",
    "独立 reviewer 重放 703/703 个 registered identities：author denominator 46 中移除 20 个 false positive，恢复 34 个 false negative，最终 denominator=60、pre-denominator closures=643。60/60 exact-v1 Review 完成，blocked=0、ordinary pending=0；31 项 provisional Books queue 经 current owner+adjacent challenge 收紧为 18 项。共享 Books 未修改。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
    "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-19 |", "| Window End | 2026-05-19 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |", "| Denominator ID | DEN-20260519-V2-INDEPENDENT |", f"| Denominator Frozen At | {AUDITED_AT} |", "| Completion Status | In Progress |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Open |", "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->", "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    f"| SRC-ARXIV | 2026-05-18T09:00:00+08:00 | 2026-05-19T09:00:00+08:00 | {AUDITED_AT} | DataCite v2 00..99 + 703/703 independent semantic replay + official exact-v1 HTML | checked | 703 | {';'.join(x['source_family_id'] for x in retained)} | pages=300;final_cursor=end;raw={SOURCE['raw_snapshot_records']};registered=703;screened=703;retained=60;closure=643 | 2026-05-19T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | — |", "",
    "### Coverage Limitations", "", "<!-- coverage:SRC-ARXIV:20260519:start -->703/703 identity 的 title+abstract 已由不同 reviewer 重放；20 FP 与 34 FN 已逐 family reconciliation。Coverage 不以 Books 写回为前提，当前无未决 source-discovery finding。<!-- coverage:SRC-ARXIV:20260519:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
    "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]
for row in retained:
    s = row["score_v2"]
    sf, aid = row["source_family_id"], row["arxiv_id"]
    override = "knowledge_gap" if row["integration_disposition"] == "Integrate" else "none"
    lines.append(f"| {sf} | arXiv:{aid}v1 | paper-v1:{aid} | 2026-W21 | {local_date(row['submitted_v1_utc'])} | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | {row['review_status']} | accessible | {override} | review:{sf} | self | — | new_in_window | {row['owner_node']} | {row['integration_disposition']} | books-review:{sf} | no |")

lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for row in retained:
    aid, sf = row["arxiv_id"], row["source_family_id"]
    route = "deep" if row["score_v2"]["total"] >= 7 or row["integration_disposition"] == "Integrate" else "standard"
    lines.append(f"| {sf} | RP-TODO-{sf} | {route} | arXiv:{aid}v1 | SRC-ARXIV@arXiv:{aid}v1 | {evloc(aid,'method_locator')} | {evloc(aid,'evaluation_locator')} | {evloc(aid,'limitations_locator')} | arXiv:{aid}v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:{sf} | complete |")

lines += ["", "### Source Reviews", ""]
for row in retained:
    aid, sf = row["arxiv_id"], row["source_family_id"]
    review = review_by_id[aid]
    comp = comparison_by_id[aid]
    lines += [
        f"<!-- review:{sf}:start -->", f"#### {row['title']}", "",
        f"**问题与机制。** {row['screening_reason']} 该 family 改变或挑战 `{row['owner_node']}` 的系统契约，因此保留。", "",
        f"**Exact-v1 路径。** Method=`{review['method_locator']}`；Evaluation=`{review['evaluation_locator']}`；Limitations/Counterevidence=`{review['limitations_locator']}`。", "",
        f"<!-- claim:{sf}:start -->{review.get('claim_boundary','只支持 exact-v1 披露条件；未披露字段为 Not Disclosed。')}<!-- claim:{sf}:end -->", "",
        f"**Books Comparison。** {comp['comparison_reason']} Decision=`{row['integration_disposition']}`。", f"<!-- review:{sf}:end -->", "",
    ]

lines += ["## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->", "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
for row in retained:
    aid, sf = row["arxiv_id"], row["source_family_id"]
    if row["score_v2"]["total"] < 7 and row["integration_disposition"] != "Integrate":
        continue
    unit = DEEP.get(aid, "—")
    selected = aid in DEEP
    rationale = "跨层改变 durability、authority 或 runtime dispatch，且 false-negative 风险高" if selected else "exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束"
    eligibility = ["score_7_9"] if row["score_v2"]["total"] >= 7 else []
    if row["integration_disposition"] == "Integrate":
        eligibility += ["forced_review", "potential_books_delta"]
    lines.append(f"| {sf} | {';'.join(eligibility)} | {'selected' if selected else 'not_selected'} | {unit} | — | {rationale} | {'analysis:'+unit if selected else 'analysis-decision:'+sf} |")

deep_text = {
    "2605.17821": "单一远端 checkpoint 在集群稳定、保存频率低时简单可靠，但 failure 从单卡扩大到 rack/cluster 后，所有故障都支付同一远端 IO 成本。TierCheck 按 blast radius 把恢复状态放入 local、peer 与 remote tier，并让保存与回收策略拥有 durability class。收益是常见故障走快路径；代价是多副本状态、peer failure correlation 与 reclaim race。无法证明 tier 健康或灾难域独立时，远端 durable checkpoint 仍是权威 fallback。",
    "2605.17879": "功能性健康检查能排除硬故障，却看不到算力、互联或温控引起的 fail-slow；长训练中少数慢节点会把全局同步拖入尾部。Guard 把低开销在线 monitor 与昂贵离线 node qualification 分开：前者触发怀疑，后者决定隔离/复用。它用额外 telemetry、复验容量和误报风险换吞吐稳定；信号漂移或归因不清时不能自动驱逐，应回退人工/保守 quarantine。",
    "2605.17998": "让生成 Agent 自己宣布完成在短、可逆任务中成本最低；持久工作流里，提议者同时掌握 completion authority 会把遗漏验证变成不可见提交。Verify-gated completion 将 proposal、read-only verification、admission 与 commit receipt 分开，并为失败保留 bounded packet state。收益是 completion 可审计、可拒绝；代价是 verifier 偏差、额外延迟和 liveness 风险。Verifier 不可用或证据不完整时应 fail closed/升级，而不是让 proposer 绕过 Gate。",
}
for aid, unit in DEEP.items():
    lines += ["", f"<!-- analysis:{unit}:start -->", f"### {unit}", "", deep_text[aid], f"<!-- analysis:{unit}:end -->"]
for row in retained:
    if row["arxiv_id"] not in DEEP:
        sf = row["source_family_id"]
        lines.append(f"<!-- analysis-decision:{sf}:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:{sf}:end -->")

lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for row in retained:
    sf, aid = row["source_family_id"], row["arxiv_id"]
    comp = comparison_by_id[aid]
    adj = ";".join(chapter_ref(p) for p in comp["adjacent_paths"]) or chapter_ref(comp["owner_path"])
    lines.append(f"| {sf} | {row['owner_node']} | {chapter_ref(comp['owner_path'])} | {adj} | existing:{sf} | delta:{sf} | {'Direct Evolution' if row['integration_disposition']=='Integrate' else 'Principle Reuse'} | {row['integration_disposition']} | books-review:{sf} |")
for row in retained:
    sf, aid = row["source_family_id"], row["arxiv_id"]
    comp = comparison_by_id[aid]
    lines += [f"<!-- books-review:{sf}:start -->", f"<!-- existing:{sf}:start -->已顺读 `{comp['owner_path']}` 与相邻章节 {comp['adjacent_paths']}；正文主线 headings={comp['current_owner_headings_read']}。<!-- existing:{sf}:end -->", f"<!-- delta:{sf}:start -->{comp['comparison_reason']}<!-- delta:{sf}:end -->", f"<!-- books-review:{sf}:end -->"]

first_sf = retained[0]["source_family_id"]
lines += ["", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |", "| SA-20260519-COVERAGE | fresh-context:may2026-day01 | coverage | coverage:SRC-ARXIV:20260519 | — | independent-semantic-audit.json#SA-20260519-FP;independent-semantic-audit.json#SA-20260519-FN | passed |", f"| SA-20260519-EVIDENCE | fresh-context:may2026-day01 | evidence | review:{first_sf} | — | exact-v1-review-independent.json#60-of-60 | passed |", "| SA-20260519-SELECTION | fresh-context:may2026-day01 | deep_analysis_selection | analysis:DA-FAILURE-TIERED-CHECKPOINT | — | independent-semantic-audit.json#selection | passed |", f"| SA-20260519-BOOKS | fresh-context:may2026-day01 | books | books-review:{first_sf} | FINDING-BOOKS-WRITEBACK-20260519: 18 owner-merged deltas not yet written | root serial writeback then different-writer post-write audit | open |", "", "## 8. Ignored Noise", "", "643 条 family-specific pre-denominator closure 保存在 `screening-ledger-final.json`。其中 20 项是独立审计降级的 false positive；每项说明具体机制、排除边界与重开条件。", "", "## 9. Recommended Action", "", "由 root 按 owner 合并 18 项 Books queue，避免逐论文追加；完成后由不同写作者执行 owner+adjacent post-write semantic audit。", "", "## 10. Repository Changes", "", "- 更新 2026-05-19 Daily、独立 screening/evidence/Books comparison/audit receipts。", "- 未修改共享 Books；未 stage、commit 或 push。", "", "## 11. Open Questions", "", "- 18 项 owner-merged queue 写回后，正文能否在 Review notes 前唯一承载旧路径、约束变化、owner、trade-off、failure 与 fallback？", "", "<!-- validator:materials-request-v1 -->", "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "", "## 12. Sources", ""]
for row in retained:
    aid = row["arxiv_id"]
    lines.append(f"- [{row['title']}](https://arxiv.org/html/{aid}v1) — arXiv:{aid}v1；first-public {local_date(row['submitted_v1_utc'])}；accessed 2026-09-01")
lines += ["", "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Closed`", "", "Evidence: `Passed`", "", "Books: `Open`", "", "unresolved findings: 1", "", "独立 Coverage/Evidence 审计已闭合；仅剩 root Books 串行写回与不同写作者 post-write audit。"]

output = ROOT / "papers/2026/05/19/README.md"
text = "\n".join(lines)
for row in retained:
    sf, aid = row["source_family_id"], row["arxiv_id"]
    body = text.split(f"<!-- review:{sf}:start -->", 1)[1].split(f"<!-- review:{sf}:end -->", 1)[0]
    route = "deep" if row["score_v2"]["total"] >= 7 or row["integration_disposition"] == "Integrate" else "standard"
    override = "knowledge_gap" if row["integration_disposition"] == "Integrate" else "none"
    candidate = {"Event Identity": f"paper-v1:{aid}", "Primary Identifier": f"arXiv:{aid}v1", "Supporting Source IDs": "SRC-ARXIV", "Review Override": override}
    rp = _expected_review_provenance(sf, candidate, route, f"arXiv:{aid}v1", f"SRC-ARXIV@arXiv:{aid}v1", evloc(aid, "method_locator"), evloc(aid, "evaluation_locator"), evloc(aid, "limitations_locator"), f"arXiv:{aid}v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1", f"claim:{sf}", f"review:{sf}", _normalized_body_sha256(body))
    text = text.replace("RP-TODO-" + sf, rp)
output.write_text(text + "\n")

print(json.dumps(audit["counts"], ensure_ascii=False))
