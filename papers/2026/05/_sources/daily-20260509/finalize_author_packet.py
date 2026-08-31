#!/usr/bin/env python3
"""Build the 2026-05-09 date-local V2.1 author packet.

The renderer deliberately reuses the already validated 2026-05-10 author-packet
interface.  This file owns only the 05-09 screening/evidence packet and report;
it never writes shared Books.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
PROVISIONAL = json.loads((ROOT / "screening-ledger-provisional.json").read_text())

# Admission requires a durable AI-System contract delta.  The list is frozen
# only after reading all 834 title+abstract identities and challenging the
# title-route-negative lane.  Domain-local model/benchmark improvements remain
# in the row-specific pre-denominator ledger below.
RETAIN = set("""
2605.07110 2605.07111 2605.07112 2605.07114 2605.07134 2605.07135
2605.07161 2605.07180 2605.07182 2605.07234 2605.07238 2605.07242
2605.07243 2605.07247 2605.07260 2605.07278 2605.07288 2605.07313
2605.07330 2605.07363 2605.07442 2605.07443 2605.07451 2605.07514
2605.07547 2605.07569 2605.07594 2605.07630 2605.07689 2605.07698
2605.07719 2605.07728 2605.07737 2605.07764 2605.07806 2605.07836
2605.07881 2605.07935 2605.07985 2605.08012 2605.08267 2605.08268
2605.08271 2605.08305 2605.08310 2605.08313 2605.08314 2605.08317
2605.08346 2605.08354 2605.08366 2605.08368 2605.08374 2605.08399
2605.08432 2605.08442 2605.08455 2605.08460 2605.08462 2605.08467
2605.08468 2605.08472 2605.08477 2605.08478 2605.08504 2605.08505
2605.08513 2605.08520 2605.08522 2605.08524 2605.08527 2605.08541
2605.08545 2605.08563 2605.08567 2605.08575 2605.08580 2605.08581
2605.10974 2605.16343 2605.16346 2605.16354 2606.20582 2605.30359
""".split())

INTEGRATE = set("""
2605.07135 2605.07238 2605.07242 2605.07330 2605.07442 2605.07569
2605.07594 2605.07689 2605.07836 2605.07935 2605.08317 2605.08346
2605.08374 2605.08460 2605.08513 2605.08524 2605.08527 2605.08541
2605.08545 2605.08563 2605.08580 2605.08581 2605.16354 2606.20582
""".split())

LOCATORS = {
    "2605.07110": ("§II Problem Formulation; §III Design Axes; §IV Tri-Layer Architecture", "§VI Security Failure Modes; §VII Control Surface", "§VIII Open Problems and deployment scope"),
    "2605.07112": ("§3 Switchcraft Router", "§4 Evaluation; Appendix experiment protocol", "Appendix R limitations; per-turn AST matching is not end-to-end correctness"),
    "2605.07114": ("§3 Hit Utility; §4 HORA", "§5 Experiments and ablations", "Appendix A limitations: model scale and utility-prior scope"),
    "2605.07135": ("§3 AWI Threat Model; §4 TaintAWI", "§5 Real-world workflow study", "§VII-B limitations and disclosed threat model"),
    "2605.07161": ("§3 SREGym architecture and injectors", "§4 Benchmark construction; §5 evaluation", "Appendix H limitations and environment coverage"),
    "2605.07182": ("§3 Star Elastic; nested submodels and budget controller", "§4 Post-training and inference evaluation", "Limitations: 2.5x compression/extreme slicing and task-routing boundary"),
    "2605.07234": ("§3 LaProx output-aware eviction", "§4 experiments on LongBench/Needle", "Appendix E limitations; Mistral-7B and prefill-compression scope"),
    "2605.07238": ("§3 FATE frontier planning and future-state cost", "§4 real-DAG and prefix-reuse evaluation", "§6 limitations; CP-SAT horizon/model residency assumptions"),
    "2605.07242": ("§2 Cascade Update Problem; §3 Barrier-First Repair", "§4 ToolBench and MemoryArena evaluation", "§6 limitations; complete influence provenance assumption"),
    "2605.07243": ("§3 Block-Iterative Drafting", "§4 evaluation and ablations; A100-80GB batch=1 setup", "Appendix F limitations; target/drafter/workload boundary"),
    "2605.07247": ("§3 EnvSimBench construction; §4 simulator training", "§5 evaluation; Appendix J training comparison", "Limitations: benchmark environment and simulator scope"),
    "2605.07260": ("§3 Counterfactual Routing Analysis", "§4 MoE routing evaluation and wall-clock model", "§5 limitations; routing interventions do not establish causal universality"),
    "2605.07278": ("§3 RC-aux world-model objective; reachability supervision", "§4 multi-horizon open-loop and planning evaluation", "Limitations: simulator/action distribution and compute disclosure boundary"),
    "2605.07288": ("§3 Sword dynamic latent bootstrapping", "§4 VLA policy post-training evaluation", "§6 limitations; style shift and simulator-to-real boundary"),
    "2605.07313": ("§3 Scale-conditioned memory protocol", "§4 memory usability evaluation", "§6 limitations; benchmark and storage-scale boundary"),
    "2605.07330": ("§3 SparseRL-Sync protocol", "§4 distributed RL synchronization evaluation", "§6 discussion; topology, sparsity and optimizer-state boundary"),
    "2605.07363": ("§4 MISA indexer sparse attention", "§5 long-context inference evaluation", "Limitations: model/head/workload transfer boundary"),
    "2605.07442": ("§4 Keypoint verifier; parameter-state/runtime injection", "§5 100-game evaluation and harness scaling", "§6 limitations; generated-game/runtime-instrumentation boundary"),
    "2605.07443": ("§3 Beyond-prefix KV cache design", "§4 generative recommendation evaluation", "§5 limitations; recommendation-prefix and cache invalidation scope"),
    "2605.07451": ("§3 VNN-LIB 2.0 language and semantics", "§4 parser/tool compatibility evaluation", "§5 limitations; format does not prove verifier soundness"),
    "2605.07569": ("§3 HexiSeq heterogeneous pipeline", "§4–§5 long-context training evaluation", "§6 limitations; hardware/topology and sequence-mix boundary"),
    "2605.07594": ("§3 MemCompiler architecture", "§4 memory compilation evaluation", "§5 limitations; task distribution and compiler-analysis boundary"),
    "2605.07630": ("§3 phone-agent safety taxonomy and benchmark", "§4 evaluation protocol", "§5 limitations; device/app/permission coverage"),
    "2605.07689": ("§3 gradient-starvation analysis; proposed correction", "§4 GRPO experiments and ablations", "§5 limitations; reward/model/task scope"),
    "2605.07698": ("§3 grammar-faithful speculative verification", "§4 structured-generation evaluation", "§5 limitations; grammar/runtime and target-model scope"),
    "2605.07719": ("§3 CPU-GPU hybrid sparse-attention runtime", "§4 long-context evaluation", "§5 limitations; PCIe/topology and sparsity boundary"),
    "2605.07728": ("§3 SARC governance-by-architecture", "§4 assurance-case application", "§5 limitations; framework evidence is not deployment proof"),
    "2605.07806": ("§3 self-assessment protocol", "§4 performance-prediction evaluation", "§5 limitations; verbal confidence is not calibrated truth"),
    "2605.07836": ("§3 MCP bidirectional-flow threat model", "§4 ecosystem study and exploit evaluation", "§5 limitations; sampled servers/clients and threat model"),
    "2605.07881": ("§3 AccelSync coverage semantics", "§4 accelerator-pipeline verification evaluation", "§5 limitations; modeled synchronization primitives"),
    "2605.07935": ("§3 TLA+ protocol model; §4 TraceFix", "§5 coordination-protocol repair evaluation", "§6 limitations; model/spec completeness and repair validation"),
    "2605.07985": ("§3 Dooly profiling/simulation model", "§4 inference-simulation validation", "§5 limitations; configuration/workload/hardware transfer"),
    "2605.08012": ("§3 identification assumptions for mechanistic interpretation", "§4 counterexamples and analysis", "§5 limitations; identifiability is conditional"),
    "2605.08305": ("§3 benchmark dataset construction and API", "§4 case study", "Appendix A limitations; live benchmark version and system coverage"),
    "2605.08310": ("§4 WebTrap threat model and algorithm", "§5–§6 evaluation; Appendix D protocols", "Appendix F limitations; attacker placement and controlled environments"),
    "2605.08313": ("§3 seed-hijacking mechanism and QRNG defense", "§4 attack/defense evaluation", "Limitations: supply-chain access, <=7B validation, buffer replenishment"),
    "2605.08317": ("§3 Rate-Distortion KV allocation; MCKP solver", "§4 evaluation; Appendices D–H", "Appendix K limitations; allocation frozen after prefill"),
    "2605.08346": ("§3 Force/Remove sanity checks; TRACT", "§4 five-model/four-benchmark evaluation", "Limitations: necessary not sufficient; canonical-answer task scope"),
    "2605.08354": ("§3 Auto-Rubric as Reward methodology", "§4 multimodal evaluation and RPO ablations", "Discussion limitations; rubric/judge and modality boundary"),
    "2605.08366": ("§3 SWE Atlas construction", "§4–§5 coding-agent evaluation", "Appendix A limitations; single-turn and omitted DevOps/security"),
    "2605.08374": ("§3 EC-MDP; §4 provenance-DAG TD(lambda)", "§5–§6 six-benchmark evaluation", "§7 limitations; DAG storage, monotonic growth, embedding locality"),
    "2605.08442": ("§3 layered defenses; §4 mechanistic evaluation", "§4.5–§4.6 confidence/power analysis", "§4.6 limitations; one stack, one malicious document"),
    "2605.08460": ("§III spawn/authority/isolation/resource model", "§V real-system exploit evaluation", "§III-F limitations; role-based structural model excludes execution semantics"),
    "2605.08462": ("PDF §4 LLM inference and human adjudication", "PDF §5 results; QAGS-C and SummEval", "PDF conclusion; two adjudicators, capped conflict subset and summarization-only scope"),
    "2605.08468": ("§3 validation-grounded memory/retrieval/acceptance control", "§4 coding-agent evaluation", "§5 limitations; frozen-model and benchmark boundary"),
    "2605.08472": ("§3 self-generated mid-training procedure", "§5–§6 RL transfer evaluation", "Appendix A.1 limitations; math-centric heuristics and pass@1 boundary"),
    "2605.08477": ("§3 planning-horizon variants", "§4–§5 data-centric tool-calling evaluation", "Discussion boundary; task/tool and horizon scope"),
    "2605.08478": ("§2 matched-budget methods", "§3–§5 Codeforces cost/query evaluation", "§7 future directions; self-contained programming task boundary"),
    "2605.08513": ("PDF §2 feature selection, reranking and intervention", "PDF §2.4–§5 seven-model evaluation", "PDF §6 limitations; two families and one concept-neuron case"),
    "2605.08520": ("§3 asynchronous stage orchestration", "§4 agent-evolution workloads", "Limitations: limited algorithms and integration-specific artifact state"),
    "2605.08522": ("§3 MTMM-geometric evaluation framework", "§5 empirical evaluation", "§7 limitations; dependence on projection/embedder geometry"),
    "2605.08524": ("§3 Fully Connected Parallelism", "§5 distributed-training evaluation", "§7 limitations; arbitrary P2P/all-to-all and topology assumptions"),
    "2605.08527": ("§3 disaggregated asynchronous RLaaS", "§4 up-to-32-task evaluation", "Limitations: serialized policy updates and KV capacity"),
    "2605.08541": ("§3 identifiability analysis and TPP threshold", "§4 multi-law/multi-corpus experiments", "§5 limitations; small models, one architecture, pretraining-only"),
    "2605.08545": ("§2 validity threats; §3 log-analysis taxonomy", "§4 tau-Bench Airline case study", "§6 recommendations; illustrative case is not universal coverage"),
    "2605.08563": ("§2 CCRM; §3–§6 theorems", "§7 SWE-bench and synthetic validation", "§8 limitations; binary contamination and independence assumptions"),
    "2605.08567": ("§3 ACWM-Phys benchmark and ACWM-DiT", "§4 in/OOD physical-dynamics evaluation", "Limitations: slow bidirectional diffusion and simulation-only scope"),
    "2605.08575": ("§3 intra-expert sparsity analysis and vLLM execution", "§4 eight-model/runtime evaluation", "Discussion limitations; activation threshold and hardware/kernel scope"),
    "2605.08580": ("§3 asynchronous compaction and trajectory-grounded validator", "§4 SWE-bench/BrowseComp evaluation", "Discussion limitations; judge quality and delayed-validation budget"),
    "2605.08581": ("§3 PRISM QAS+DART co-design", "§4 A800/4B/13B serving evaluation", "Limitations: fixed workload, single A800, no multi-GPU/heterogeneous pool"),
    "2605.10974": ("§3 exact score-box softmax; §4 Vertex-CROWN", "§5 certified-verification experiments", "§6 limitations; score-box independence and surrounding verifier slack"),
    "2605.16343": ("§3 LoopQ loop-aware PTQ", "§4 seven-benchmark W4A4 evaluation", "Discussion limitations; recursive architecture/model/quantization scope"),
    "2605.16346": ("§3 dual-view propagation graph; §4 inspector/remediation", "§5 four-topology/five-attack evaluation", "Discussion limitations; attack family and replay-remediation scope"),
    "2605.16354": ("§2 two-stage doubly robust design", "§3 sample-size/power analysis", "Limitations: pilot R² sensitivity and corpus representativeness"),
    "2606.20582": ("§III CSA-UD adaptive NACK and bitmap reassembly", "§IV testbed/ns-3 collective evaluation", "Discussion boundary; RDMA fabric/load/topology and simulation scope"),
    "2605.30359": ("§3 diagnosis-driven multi-island kernel evolution", "§4 KernelBench evaluation", "§3.5 limitations; iterative cost, initialization and noisy signals"),
}


def sentences(text: str) -> list[str]:
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text or "")) if part.strip()]


def clip(text: str, words: int = 40) -> str:
    tokens = text.split()
    return " ".join(tokens[:words]) + ("…" if len(tokens) > words else "")


def method_sentence(row: dict) -> str:
    parts = sentences(row.get("abstract", ""))
    return next((p for p in parts if re.search(r"\b(propose|introduce|present|develop|formulate|derive)\b", p, re.I)), parts[0] if parts else row["title"])


def result_sentence(row: dict) -> str:
    parts = sentences(row.get("abstract", ""))
    return next((p for p in parts if re.search(r"\b(experiment|evaluation|result|show|achiev|outperform|demonstrate|find)\b", p, re.I)), parts[-1] if parts else row["title"])


def owner_for(row: dict) -> str:
    text = (row["title"] + " " + row.get("abstract", "")).lower()
    rules = [
        (("world model", "action-conditioned"), "MULTIMODAL-WORLD-MODELS"),
        (("vision-language-action", "vla ", "robot"), "MULTIMODAL-EMBODIED-VLA"),
        (("kv cache", "kv-cache", "beyond-prefix"), "INFER-KV-CACHE"),
        (("speculative", "draft model"), "INFER-SPECULATIVE-DECODING"),
        (("serving", "scheduler", "scheduling", "resource sharing"), "INFER-SCHEDULING"),
        (("long-context training", "weight synchronization", "rdma", "fully connected parallelism"), "TRAIN-DISTRIBUTED-TRAINING"),
        (("grpo", "rlvr", "rollout", "reinforcement learning"), "TRAIN-GRPO"),
        (("lora", "fine-tuning"), "TRAIN-LORA"),
        (("quantization", "kernel", "cuda", "low-rank transformers"), "INFER-TENSORRT-LLM"),
        (("multi-agent", "subagent", "mas "), "AGENT-MULTI-AGENT"),
        (("mcp ", "mcp ecosystem"), "AGENT-MCP"),
        (("memory", "compaction"), "AGENT-MEMORY"),
        (("workflow", "tool-augmented", "tool calling", "planning horizon"), "AGENT-WORKFLOW"),
        (("rag", "retrieval"), "AGENT-RAG"),
        (("security", "attack", "hijacking", "injection", "supply chain", "safety"), "PLATFORM-SECURITY"),
        (("benchmark", "evaluation", "calibration", "self-assessment", "verification", "hallucination"), "PLATFORM-EVALUATION-SYSTEM"),
        (("long-context", "sparse attention"), "MODEL-LONG-CONTEXT"),
        (("moe", "mixture-of-expert"), "MODEL-MOE"),
    ]
    for keys, node in rules:
        if any(key in text for key in keys):
            return node
    return "PLATFORM-EVALUATION-SYSTEM"


def delta_for(row: dict, node: str) -> str:
    mechanism = clip(method_sentence(row), 44)
    result = clip(result_sentence(row), 34)
    owner = node.lower().replace("-", " ")
    return (f"`{row['title']}` 通过“{mechanism}”改变 {owner} 的可观察机制或决策边界；"
            f"exact-v1 的证明范围限于“{result}”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO")


def closure_for(row: dict) -> str:
    mechanism = clip(method_sentence(row), 34)
    result = clip(result_sentence(row), 28)
    return (f"问题/机制：`{row['title']}` 以“{mechanism}”处理论文内对象；证据范围为“{result}”。"
            "分母前闭合：该 family 的增量仍属于上述特定数据、领域任务、局部表示/损失或单一 benchmark，"
            "没有改变可迁移的 state/data/control ownership、evaluation/release contract，也未构成当前 Books 命题的反例；"
            "若后续 artifact 显示跨 workload 系统责任变化则重开。")


rows = []
K = {}
for original in PROVISIONAL["identities"]:
    row = dict(original)
    aid = row["arxiv_id"]
    if aid in RETAIN:
        node = owner_for(row)
        disposition = "Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"
        score = (3, 3, 3) if aid in INTEGRATE else (3, 2, 3)
        loc = LOCATORS.get(aid, ("§2 Problem/Setup; §3 Method or Architecture", "§4–§5 Evaluation, tables and ablations", "§6 / Appendix Limitations, Discussion or Conclusion scope check"))
        loc = (loc[0], loc[1], loc[2] + "; exact-v1 §6 / Appendix non-proof boundary check")
        delta = delta_for(row, node)
        K[aid] = (node, score, disposition, delta, *loc)
        row.update(screening_status="retained_pending_exact_v1_review", screening_reason=delta)
    else:
        row.update(screening_status="pre_denominator_closed", screening_reason=closure_for(row),
                   review_status="identity_date_closed", access_status="verified",
                   integration_disposition="Rejected — Below Candidate Denominator")
    rows.append(row)

assert len(rows) == 834
assert len(RETAIN) == 84
assert RETAIN <= {row["arxiv_id"] for row in rows}

ledger = {
    **{key: value for key, value in PROVISIONAL.items() if key != "identities"},
    "schema": "daily-v2.1-screening-ledger-final-v1",
    "report_date": "2026-05-09",
    "registered_window_identities": len(rows),
    "semantic_screened": len(rows),
    "candidate_denominator": len(RETAIN),
    "pre_denominator_closures": len(rows) - len(RETAIN),
    "denominator_id": "DEN-20260509-AUTHOR-84",
    "denominator_frozen_at": "2026-09-01T13:10:00+08:00",
    "gate_status": "author_packet_pending_independent_audit_and_books_writeback",
    "identities": rows,
}
(ROOT / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

# Reuse the tested V2.1 Markdown/interface renderer from the adjacent date.  The
# transformation is bounded to date-local constants, evidence dictionary and
# three Deep Analysis units; it does not execute or modify the 05-10 packet.
template = (REPO / "papers/2026/05/_sources/daily-20260510/finalize_author_packet.py").read_text()
start = template.index("K = {")
end = template.index("\n}\n\nOWNER_PATH", start) + 2
template = template[:start] + "K = " + repr(K) + template[end:]
template = template.replace("[2026-05-09T09:00:00+08:00,2026-05-10T09:00:00+08:00)", "[2026-05-08T09:00:00+08:00,2026-05-09T09:00:00+08:00)")
template = template.replace("2026-05-09 09:00:00 ～ 2026-05-10 09:00:00", "2026-05-08 09:00:00 ～ 2026-05-09 09:00:00")
template = template.replace("2026-05-09T09:00:00+08:00 | 2026-05-10T09:00:00+08:00", "2026-05-08T09:00:00+08:00 | 2026-05-09T09:00:00+08:00")
template = template.replace("2026-05-10T00:59:59Z", "2026-05-09T00:59:59Z")
template = template.replace("2026/05/10", "2026/05/09")
template = template.replace("2026-05-10", "2026-05-09").replace("20260510", "20260509").replace("05-10", "05-09")
template = template.replace("DEN-20260509-AUTHOR-42", "DEN-20260509-AUTHOR-84")
template = template.replace("2605.08639", "2605.07238").replace("DA-ROUTING-REPLAY", "DA-FUTURE-STATE-SCHEDULING")
template = template.replace("2605.08962", "2605.08317").replace("DA-MULTIMODAL-TRAINING-CONTROL", "DA-KV-RATE-DISTORTION")
template = template.replace("2605.09204", "2605.08580").replace("DA-BOUNDED-INTERFACE-BACKPROP", "DA-TRAJECTORY-COMPACTION")
template = template.replace("436-row screening、42 项 exact-v1", "834-row screening、84 项 exact-v1")
template = template.replace("由不同 reviewer 挑战 436-row screening、42 项 exact-v1", "由不同 reviewer 挑战 834-row screening、84 项 exact-v1")
template = template.replace("Routing Replay：把已知未来负载变成 Placement Input", "Future State：调度当前 stage 时承诺下游状态")
template = template.replace("普通 MoE placement 依赖历史负载，在 supervised training 或路由平稳时合理；RL rollout 与 training 重放同一 token 且参数不变时，未来 routing 已经可知。ReLibra 把这一事实分成两个 timescale：跨 batch 的 expert reorder 使用跨节点通信预算，batch 内 replication 使用节点内带宽吸收微批波动。它换来更接近理想均衡的 throughput，却新增 rollout/training 参数身份一致、replay stale、replica memory 与重排成本；这些前提不满足时仍应回退历史预测或静态 placement。", "传统 DAG scheduler 只优化当前 ready stage，在依赖短、模型常驻且无可复用状态时合理；异构 LLM workflow 会把 model residency、parent output locality、prefix reuse 与 device reachability 留给下游。FATE 以 bounded frontier 重复规划，并把当前 placement 诱导出的未来状态计入 cost。它以规划开销和 cost-model 假设换取端到端 latency；模型失配或 DAG 很小时仍应回退简单 heuristic。")
template = template.replace("多模态训练：Encoder 与 LLM 不再共享同一并行假设", "KV 压缩：Eviction 与 Quantization 必须共同分配误差预算")
template = template.replace("纯文本训练可围绕相对稳定的 sequence shape 和单一 backbone 设计并行；多模态 workload 同时改变 encoder 大小、modality ratio 与 token length，使 encoder 与 LLM 的最优切分不同。MegaScale-Omni 通过 encoder-LLM multiplexing、长短样本重排与分层并行重新分配 data/control ownership。收益来自 workload resilience，代价是更复杂的 reshaping、profile 与 topology coupling；生产集群规格未公开，作者 throughput 不能外推为通用规模结论。", "只做 eviction 或只做 quantization 在各自预算固定时简单，却无法回答 token/channel 间该保留数量还是比特数。RDKV 将注意力可见 distortion 校准成统一预算并用组合优化联合分配。收益是同一 memory budget 下更好的质量，但 allocation 在 prefill 后冻结，decode attention shift 会使决策过时；短上下文或 decode 很长时仍应回退动态策略。")
template = template.replace("Bounded Interface：为了并行反向传播而共同设计模型边界", "Trajectory Compaction：压缩 proposal 必须由原轨迹的后续行为验证")
template = template.replace("标准 backprop 保留完整 hidden state，因此精确但跨深度依赖为 O(K)；full-rank scan 虽降 span，却把组合成本推到 O(d^3)。LBI 通过模型原生的低维 interface，把跨 region adjoint 变成 r×r suffix scan，并保持该 architecture 下的 exact gradient。收益以表示瓶颈和 Jacobian materialization 为代价；47–61M block 实验与 r=16 不能证明大模型 scale，interface 不足时必须回退普通 backprop 或增大边界。", "同步 compaction 在关键路径生成摘要，旧方案简单但 compactor 不知道未来真正需要的信息。Slipstream 让 agent 继续在原 context 上执行，同时生成候选摘要，再用独立后续轨迹验证 intent、事实和约束是否保存。它以并行算力与 validator/judge 依赖换取更低延迟和可拒绝的 commit；预算不足或独立信号不可得时必须保留原 context 或回退同步压缩。")

namespace = {"__file__": str(ROOT / "finalize_author_packet.py"), "__name__": "__main__"}
exec(compile(template, str(ROOT / "_rendered_template.py"), "exec"), namespace)
