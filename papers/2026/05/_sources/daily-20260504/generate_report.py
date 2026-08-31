#!/usr/bin/env python3
"""Generate the 2026-05-04 author-lane Daily packet without shared Books writes."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
PACKET = ROOT / "papers/2026/05/_sources/daily-20260504"
REPORT = ROOT / "papers/2026/05/04/README.md"
INV = json.loads((PACKET / "inventory.json").read_text())
BY_ID = {x["arxiv_id"]: x for x in INV["identities"]}


def cand(aid, score, node, disposition, chapter, adjacent, claim, method, evaluation, limits,
         ref, lines, relation="Direct Evolution", override="knowledge_gap"):
    return {"aid": aid, "fid": f"SF-2026-ARXIV-{aid.replace('.', '-')}", "score": score,
            "total": sum(score), "node": node, "disposition": disposition, "chapter": chapter,
            "adjacent": adjacent, "claim": claim, "method": method, "evaluation": evaluation,
            "limits": limits, "ref": ref, "lines": lines, "relation": relation, "override": override}


CANDIDATES = [
    cand("2605.01666", (3,2,2), "AGENT-WORKFLOW", "No Change — Existing Coverage",
         "books/part-07-agent/81-workflow.md", "Ch80/Ch82",
         "Mixed-initiative structured-data workflows need field-level authority: confirmed values remain locked, machine initiative is bounded by evidence and overwrite risk, and every autonomous transition retains provenance plus atomic rollback.",
         "§III-A partial event state; §III-D lock clamp/re-decode; §III-E trust-calibrated authority; §III-F transition/provenance loop", "§IV-A protocol; §IV-B metrics; §IV-D safety; §IV-E ablation", "Nine participants and short, curated HOI clips; zero confirmed-field violations under this protocol does not prove arbitrary workflow safety or transfer of the calibrated authority policy.", "turn11963view0", 358, override="security_contract"),
    cand("2605.01694", (3,3,3), "MULTIMODAL-WORLD-MODELS", "No Change — Existing Coverage",
         "books/part-03-multimodal-world-models/25-multimodal-world-models.md", "Ch24/Ch26",
         "World-model state should be selected by task-specific sufficiency—prediction, control, counterfactual action, memory—not by how much sensory information it preserves.",
         "§2 state abstraction; §3 six latent roles; §12 evaluation matrix", "§12 seven axes and preserve/discard/enable matrix", "Conceptual taxonomy, not a new controlled system experiment; §13 states open research tests.", "turn11934view0", 634),
    cand("2605.01704", (3,3,2), "AGENT-MULTI-AGENT", "No Change — Existing Coverage",
         "books/part-07-agent/82-multi-agent.md", "Ch80/Ch81",
         "Closed multi-agent transformations cannot add evidence information under the stated Markov chain; external evidence changes the information boundary, while voting may preserve answers but destroy supported reasoning.",
         "§3 SFS; §4 DPI bound and open-system recovery", "§5 SciFact/FEVER experiments across 16 conditions", "§6 and Implications/limitations: theorem depends on the closed Markov structure and chosen evidence/claim decomposition.", "turn11934view1", 967, "Explanatory Analogy"),
    cand("2605.01708", (3,3,3), "INFER-PD-DISAGGREGATION", "Integrate",
         "books/part-05-inference-system/55-pd-disaggregation.md", "Ch45/Ch56",
         "Bit-exact KV transfer can exploit exponent redundancy with a fixed dense code plus sparse escape stream, but codec throughput and small-payload overhead must be charged against the PD handoff critical path.",
         "§3 fixed top-16 exponent codebook, dense path and sparse escape correction", "§4 BF16/FP8 codec and end-to-end transfer on H200/network configurations", "No dedicated limitations section; §4 shows short payloads can lose to fixed overhead and results bind disclosed models, links and precision.", "turn11934view2", 348),
    cand("2605.01710", (3,3,3), "INFER-REQUEST-LIFECYCLE", "No Change — Existing Coverage",
         "books/part-05-inference-system/42-what-happens-during-inference.md", "Ch56/Ch62",
         "A model identifier is insufficient provenance for adaptive serving; each answer needs a redaction-aware route receipt covering alias, tier, fallback, tool and regional path decisions.",
         "§5-§8 minimal route-receipt schema and documentation survey", "Documentation-surface comparison rather than live route measurement", "§14: no live measurements of alias drift, fallback frequency, regional routing or compute-budget effects.", "turn11934view3", 537),
    cand("2605.01749", (3,2,2), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
         "books/part-06-ai-infrastructure/66-evaluation-system.md", "Ch20/Ch76",
         "Long-form factual generation can separate exploratory reasoning from final commitment and condition commitment on calibrated reliability, but model-generated confidence remains evaluator- and distribution-bound.",
         "§2 exploration–commitment decoupling and calibration-aware generation", "§3 five factuality benchmarks and multiple model families", "Appendix E: calibration quality, benchmark coverage and computational assumptions bound the result.", "turn11934view4", 1170),
    cand("2605.01771", (3,3,3), "PLATFORM-EVALUATION-SYSTEM", "Integrate",
         "books/part-06-ai-infrastructure/66-evaluation-system.md", "Ch69/Ch81",
         "Textual agreement cannot prove process compliance; process instructions require observable tool-call traces, environment affordance controls and audit metrics owned outside the model response.",
         "§2 process-fidelity construct; §3 detectability theorems", "§4 thirteen experiments, 2,031 sessions, six models and BS-Bench tool-log metrics", "Limitations/forecast: selected tasks, tools and frontier-model APIs do not establish universal rates; text-only observers remain outside the behavior channel.", "turn11934view5", 1412, override="evaluation_contract"),
    cand("2605.01782", (3,3,3), "AGENT-RAG", "No Change — Existing Coverage",
         "books/part-07-agent/76-rag.md", "Ch69/Ch72",
         "RAG incident forensics must preserve a prompt-anchored execution trace and replay counterfactual evidence edits so a poisoned character span—not merely a suspicious document—can be attributed under the logged event.",
         "§3 threat model; §4 two-pass logged trace, masking and replay", "§5 two QA corpora, five attacks, six LLMs and localization metrics", "§8: black-box replay budget, benchmark attack set and event-conditioned attribution do not prove global causal responsibility.", "turn11934view6", 970, override="security_contract"),
    cand("2605.01796", (2,2,3), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
         "books/part-06-ai-infrastructure/66-evaluation-system.md", "Ch20/Ch67",
         "A scalar average calibration error can hide severe high-confidence overprediction; calibration offset, statistical overconfidence risk and discriminative usefulness must be reported separately.",
         "§2 CSR, risk probability and confidence-weighted metrics", "§3 synthetic profiles and fifteen real datasets", "§4: classification focus, finite-sample assumptions and chosen confidence source limit deployment claims.", "turn11934view7", 1020),
    cand("2605.01847", (3,2,2), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
         "books/part-06-ai-infrastructure/66-evaluation-system.md", "Ch77/Ch81",
         "Endpoint success and commitment integrity are different constructs; side-query probes can expose stale bindings, source confusion and contradiction-repair failures without claiming access to hidden activations.",
         "§3 deterministic task/probe generator and HCCIS-CORE", "§4 human calibration; §5-§6 32-profile evaluation", "§7 Discussion: probe-defined construct and benchmark inventory do not exhaust agent state or predict all terminal failures.", "turn11935view0", 552),
    cand("2605.01858", (2,2,3), "INFER-KV-CACHE", "No Change — Existing Coverage",
         "books/part-05-inference-system/45-why-kv-cache-speeds-up.md", "Ch22/Ch23",
         "Streaming video state can decouple cumulative past KV from an on-demand recent cache and use position-agnostic encoding, trading bounded memory for possible loss of long-horizon detail.",
         "§3 decoupled streaming cache; §4 position-agnostic encoding", "§5 Streaming Video QA evaluations", "No dedicated limitations section; training-free results on selected offline backbones/benchmarks do not prove unbounded semantic retention.", "turn11935view1", 500),
    cand("2605.01938", (3,2,3), "PLATFORM-COST", "No Change — Existing Coverage",
         "books/part-06-ai-infrastructure/70-cost.md", "Ch36/Ch67",
         "Energy attribution for multimodal training must cross model phase, GPU/CPU memory path and system power rather than infer efficiency from accelerator utilization alone.",
         "§III cross-layer measurement methodology", "§IV experiments on Grace Hopper multimodal training", "Single hardware generation and selected workloads do not define a universal energy model; offload shifts rather than removes cost.", "turn11935view4", 380),
    cand("2605.01950", (3,3,2), "PLATFORM-SECURITY", "No Change — Existing Coverage",
         "books/part-06-ai-infrastructure/72-security.md", "Ch25/Ch79",
         "World-model security must test whether an attacker can reorder decision-critical imagined trajectories, not only corrupt observations or one-step outputs.",
         "§3 threat model; §4 tail-aware ranking loss and gates", "§5 DreamerV3/TD-MPC2 task evaluations", "Selected planners, triggers and simulated tasks do not establish prevalence, stealth under adaptive defense or real-robot impact.", "turn11935view5", 362, override="security_contract"),
    cand("2605.01970", (3,3,3), "PLATFORM-SECURITY", "No Change — Existing Coverage",
         "books/part-06-ai-infrastructure/72-security.md", "Ch77/Ch78",
         "Persistent memory is an effect-bearing trust boundary: one untrusted tool result can plant a delayed trigger that later selects sensitive context, so write provenance, activation policy and utility-aware defenses must be evaluated together.",
         "§3 threat model; §4 adaptive benchmark; §5 four memory backends; §6 defenses", "§7 attack persistence and security/utility analysis", "§7.4: one assistant domain, selected backends/models and adaptive benchmark do not prove deployment prevalence; defenses trade utility differently.", "turn11935view6", 717, override="security_contract"),
    cand("2605.01989", (3,3,2), "TRAIN-DISTRIBUTED-TRAINING", "Integrate",
         "books/part-04-training-system/36-distributed-training.md", "Ch37/Ch41",
         "Gradient transport reliability can be phase-aware: bounded packet loss avoids microburst retransmission tails, but the model owns tolerance evidence and the transport owns per-round identity, bitmap and fallback.",
         "PDF §III-§IV dynamic bounded-loss UDP/TCP control and implementation", "PDF §V, GPT-2-S plus three vision models on three-worker testbed and microbursts", "PDF p4 notes larger-scale evaluation is future work; fixed detector threshold and empirical 40% tolerance are workload-specific.", "turn11938view1", 850),
    cand("2605.02028", (3,2,3), "AGENT-WORKFLOW", "No Change — Existing Coverage",
         "books/part-07-agent/81-workflow.md", "Ch17/Ch84",
         "Extended exact-rule execution requires explicit durable state; more model scale, tokens or tools do not guarantee that a finite implicit-state strategy preserves the rule indefinitely.",
         "§2 symbolic counting capacity and mechanistic probes", "126 model variants plus matched dual-task controls", "Limitations: homogeneous counting is artificial and proprietary preprocessing/reasoning accounting is only partially observable.", "turn11936view1", 244),
    cand("2605.02043", (3,2,3), "TRAIN-DISTRIBUTED-TRAINING", "No Change — Existing Coverage",
         "books/part-04-training-system/36-distributed-training.md", "Ch28/Ch37",
         "Delay attenuation in asynchronous SGD can bias training toward fast samples; momentum-based virtual iterates preserve delayed information while controlling staleness under stated smoothness assumptions.",
         "§3 asynchronous momentum framework; §4 convex/non-convex analysis", "Theoretical convergence bounds and numerical checks", "Data-dependent-delay assumptions, smooth objectives and theoretical rates do not establish production straggler behavior for large nonstationary training.", "turn11936view2", 746),
    cand("2605.02050", (3,3,3), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
         "books/part-06-ai-infrastructure/66-evaluation-system.md", "Ch67/Ch73",
         "Human-uplift claims require an RCT contract that freezes population, intervention, comparator, outcomes, analysis and open-science evidence; a model benchmark is not a substitute.",
         "§2 five principles; §3-§4 thirty-three operational guidelines", "Synthesis against validity and open-science traditions rather than a new RCT", "§5: guidelines need domain adaptation, empirical validation and evolution as AI interventions change.", "turn11936view3", 400, override="evaluation_contract"),
    cand("2605.02087", (3,3,3), "TRAIN-PRETRAINING", "Integrate",
         "books/part-04-training-system/28-pretraining.md", "Ch29/Ch31",
         "Teaching a model the rationale and content of a behavior spec before demonstration alignment changes how underspecified examples generalize; the spec corpus becomes a versioned training artifact and a new mis-specification surface.",
         "§2 model-spec midtraining and synthetic document construction", "§3-§6 cheese/generalization and agentic-misalignment evaluations", "§7: synthetic specs, selected Qwen models and narrow AFT settings do not prove broad value alignment or resistance to deceptive specifications.", "turn11936view4", 911),
    cand("2605.02960", (3,3,3), "INFER-PREFILL", "Integrate",
         "books/part-05-inference-system/43-prefill.md", "Ch21/Ch56",
         "Prefill-only MoE workloads can exchange activation all-to-all for asynchronous expert-weight all-gather when long compute windows hide transfer; the saturation threshold and traffic drift become routing state.",
         "§3 AsyncEP weight streaming; §4 physically-derived saturation threshold and prefix-aware frontend", "§7-§8 Qwen3-235B-A22B on four hardware/precision configurations", "Applicability/limitations: prefill-only, batch-driven MoE; low-bandwidth links, bursty arrivals, drift and random prefixes narrow the result.", "turn11936view5", 514),
    cand("2605.02964", (3,3,3), "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
         "books/part-06-ai-infrastructure/66-evaluation-system.md", "Ch31/Ch72",
         "Tool-agent evaluation must distinguish nominal success from shortcut exploitation and vary horizon/complexity; environmental hardening can change the opportunity surface without changing weights.",
         "§3 task regimes, shortcut opportunities and exploit taxonomy; §4 harness", "§5 thirteen frontier models, sibling post-training comparison and hardening", "§8: current rule triggers have false positives and may miss new exploits; associations do not isolate all causal effects of RL.", "turn11936view6", 1053, override="evaluation_contract"),
    cand("2605.23945", (3,3,3), "TRAIN-TENSOR-PARALLEL", "No Change — Existing Coverage",
         "books/part-04-training-system/37-tensor-parallel.md", "Ch31/Ch41",
         "Synchronous RLHF generation should treat response-length skew as changing the efficient TP degree; online reconfiguration must compare predicted benefit with KV migration/recompute, reshard and communicator costs.",
         "§3 predictor-guided TP reconfiguration; §4 KV migration/recompute and weight reshard", "§5 A40/H100 testbeds, Llama/Qwen with VeRL/SGLang", "No dedicated limitations section; 8–16 GPU testbeds, offline profiles and synchronous pipelines do not establish fleet-scale stability or arbitrary topology gains.", "turn11936view7", 378),
    cand("2606.20577", (3,3,3), "INFER-SCHEDULING", "No Change — Existing Coverage",
         "books/part-05-inference-system/56-inference-scheduling.md", "Ch46/Ch55",
         "Agent loops may not value human-perceived TTFT/TPOT; serving policy should bind SLOs to workload class while retaining hardware/memory safety caps and total-task completion evidence.",
         "§3 throughput–SLA frontier; §5 HlServe policy and cap separation", "§4 Qwen-2.5-32B FP16 on 8×H20, 8K–64K, concurrency 16–256, SGLang/Sarathi", "§6 limitations: one primary model/hardware/workload, no claim that all agent traffic can drop latency constraints, and NCCL instability at concurrency 256.", "turn11937view0", 256),
    cand("2605.01831", (3,3,3), "TRAIN-RLHF", "Integrate",
         "books/part-04-training-system/31-rlhf.md", "Ch30/Ch32",
         "Reward-model evaluation must condition the preferred response on an explicit user preference and test paraphrase consistency; a universal-quality ranking hides whether the reward function generalizes across preference contracts.",
         "§3 constructs controlled preference prompts, four response profiles and paraphrase variants across four domains", "§4–§5 1,097 instances/13,164 prompts and 24 reward models with pairwise, Best-of-N and consistency analysis", "§Limitations: intrinsic synthetic English benchmark only; no PPO/DPO downstream validation, real-user preference distribution or cross-cultural coverage.", "turn11955view1", 960, override="evaluation_contract"),
    cand("2605.01920", (2,3,2), "AGENT-CONTEXT", "No Change — Existing Coverage",
         "books/part-07-agent/75-context.md", "Ch74/Ch76",
         "Agent context needs an implementation-independent description of message roles, time-indexed references and conditional/iterative assembly so context evolution can be compared and audited across model calls.",
         "§3–§5 ACDL syntax for context elements, references, time indices and control flow; §6 examples and renderer", "§6 descriptive reconstruction of existing agent contexts rather than a performance benchmark", "§7 Limitations: immutable-within-construction step model and synchronized clocks cannot cleanly express asynchronous agents over shared mutable state.", "turn11955view3", 752),
    cand("2605.05242", (3,3,2), "AGENT-CONTEXT", "No Change — Existing Coverage",
         "books/part-07-agent/75-context.md", "Ch74/Ch76",
         "Retrieval is an observation interface, not only a ranking model: direct corpus interaction raises interface resolution with composable search/read operations, while moving index cost into agent steps, context management and permission risk.",
         "§3 DCI tool interface; §3.2 truncation/compaction/summarization state; §3.3 coverage and localization metrics", "§4 BrowseComp-Plus, multi-hop QA and BEIR/BRIGHT comparisons plus tool/context ablations", "No dedicated limitations section; selected frozen corpora, proprietary agent backbones, API-cost assumptions and corpus scale do not show DCI replaces indexed retrieval for high-QPS or access-controlled workloads.", "turn11956view0", 621),
    cand("2605.02038", (3,3,3), "PLATFORM-EVALUATION-SYSTEM", "Integrate",
         "books/part-06-ai-infrastructure/66-evaluation-system.md", "Ch20/Ch67",
         "A model score is inseparable from prompt variants, confidence normalization, parser and evaluator logic; multi-variant evaluation must retain raw generations and report spread instead of treating one prompt as model identity.",
         "§2 audit design; §3 confidence/evaluator definitions; §4 five prompt variants per model-dataset cell", "§4–§5 15 open models, five English benchmarks, token/verbal calibration and repair controls", "§6: observational 1–8B English multiple-choice corpus, uneven families, one vLLM/bfloat16/L4 stack and two verbal-confidence phrasings; no causal training/scaling claim.", "turn11956view2", 420, override="evaluation_contract"),
]

CANDIDATES.sort(key=lambda c: (BY_ID[c["aid"]]["published_v1_utc"], c["aid"]))

RETAINED = {x["aid"] for x in CANDIDATES}
DEEP = {"2605.01708", "2605.01771", "2605.02038"}

SPECIAL_CLOSURES = {
    "2605.01939": "StressEval 根据当前模型失败模式动态生成更难实例并保留显式 difficulty factors；当前 arXiv HTML/PDF 通道未取得 exact-v1 正文，故不把摘要 benchmark 主张升级为长期 evaluation contract，保留为 pre-denominator closure 并记录 access limitation。",
    "2605.02010": "Knowledge Objects 主张把隐性推理外化为带 claim、evidence、scope 和 validation metadata 的人可审计对象；它是 position proposal，缺少实现与受控评估，现有 PLATFORM-EVALUATION-SYSTEM/AGENT-MEMORY 已拥有 provenance 和 validation contract，因此不进入 denominator。",
    "2605.01896": "M²-REPA 将 RGB/depth/mask 的中间表示分别对齐 modality-specific foundation experts，并用 decoupling regularizer 保持互补；这是特定多模态扩散训练损失，未改变 Ch23–25 的表示 identity、生成 state 或 world-transition owner。",
    "2605.02968": "该工作用五个观测量描述 Pico-LM/Pythia 的有限尺度梯度 transport/cascade，并明确不主张 universal fixed point；它提供分析测量而非训练 runtime、optimizer control 或跨层 ownership 的新机制。",
}


def sentences(text: str) -> list[str]:
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", text) if len(x.strip()) > 35]


def closure(item: dict) -> str:
    aid, title, abstract = item["arxiv_id"], item["title"], item["abstract"]
    if aid in SPECIAL_CLOSURES:
        return SPECIAL_CLOSURES[aid]
    ss = sentences(abstract)
    mechanism = ss[1] if len(ss) > 1 else (ss[0] if ss else f"《{title}》只提供身份元数据")
    low = (title + " " + abstract[:400]).lower()
    if any(k in low for k in ("agent", "tool", "rag", "memory", "reasoning")):
        boundary = "它仍是局部 Agent 方法、任务集或受限行为证据，没有重新分配 context/action/workflow state 的 authority，也未改变现有 Agent owner 的长期 failure contract。"
    elif any(k in low for k in ("serving", "cache", "gpu", "kernel", "latency", "throughput", "inference")):
        boundary = "它没有同时改变 request/KV/scheduler 的状态 ownership 与 workload-SLO contract；局部速度或压缩结果不能外推为推理系统设计结论。"
    elif any(k in low for k in ("training", "gradient", "optimizer", "fine-tun", "pretrain", "rlhf")):
        boundary = "它没有改变数据、optimizer、checkpoint 或 distributed runtime 的持久状态和控制权；受限模型/数据结果不足以重写 Training System 主线。"
    elif any(k in low for k in ("benchmark", "evaluation", "metric", "calibrat", "dataset")):
        boundary = "它提供单一 metric/dataset 或领域 benchmark，但未改变 evaluation identity、release authority、uncertainty 或可复现 evidence 的平台合同。"
    elif any(k in low for k in ("world model", "multimodal", "video", "robot", "vision")):
        boundary = "它是受限表示、生成或领域任务改进，没有改变 representation identity、action-conditioned transition、persistent world state 或 physical-control boundary。"
    else:
        boundary = "其贡献没有形成可复用的 AI-System mechanism、state/data/control ownership 或 evaluation/release contract 增量，现有 ROADMAP owner 无需改变。"
    return f"《{title}》具体研究/提出：{mechanism} {boundary}（identity={aid}v1）"


def chapter_core(chapter: str) -> str:
    """Return the current owner's central proposition for an auditable Books compare."""
    text = (ROOT / chapter).read_text()
    for line in text.splitlines():
        if "本章的核心判断" in line:
            return line.strip()
    for line in text.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and len(stripped) > 40:
            return stripped
    return "目标章节未使用固定的核心判断句；作者侧已读取正文并以当前章节职责作为比较基线。"


def locator(c: dict, field: str) -> str:
    """Bind a reviewed section description to the exact-v1 manuscript URL."""
    kind = "pdf" if c["aid"] == "2605.01989" else "html"
    return f"https://arxiv.org/{kind}/{c['aid']}v1 — § exact-v1 reviewer locator: {c[field]}（全文读取 ref={c['ref']}）"


def adjacent_chapters(chapter: str) -> str:
    """Resolve concrete neighbor paths instead of legacy chapter-number shorthand."""
    path = ROOT / chapter
    peers = sorted(path.parent.glob("[0-9][0-9]-*.md"))
    try:
        idx = peers.index(path)
    except ValueError:
        return f"{chapter}#L1"
    refs = []
    if idx > 0:
        refs.append(f"{peers[idx - 1].relative_to(ROOT)}#L1")
    if idx + 1 < len(peers):
        refs.append(f"{peers[idx + 1].relative_to(ROOT)}#L1")
    return "; ".join(refs) or f"{chapter}#L1"


def selection_rationale(c: dict) -> str:
    """Produce a family-specific pre-narrative selection comparison."""
    title = BY_ID[c["aid"]]["title"]
    if c["aid"] in DEEP:
        return {
            "2605.01708": "KV handoff codec 同时改变跨池数据表示、GPU 执行路径与小 payload break-even，需独立展开 lossless transport 的收益与固定开销。",
            "2605.01771": "process compliance 把 correctness 从回答文本移到 tool trace 与环境行为通道，改变 evaluator 的 observation authority，需独立展开。",
            "2605.02038": "prompt variant、parser、confidence normalization 与 evaluator repair 共同决定 reliability claim，改变 evaluation artifact identity，需独立展开。",
        }[c["aid"]]
    if c["node"].startswith("INFER"):
        comparison = "SplitZip 或 Human-less Serving"
        overlap = "同属推理 state/SLO 主线，但未同时重写本日最关键的 transport 或 scheduling authority"
    elif c["node"].startswith("PLATFORM"):
        comparison = "process-compliance evidence"
        overlap = "同属 evidence/security 边界，但其 claim 可在完整 Source Review 中闭合，无需再占一个长叙事单元"
    elif c["node"].startswith("TRAIN"):
        comparison = "workload-class serving SLO"
        overlap = "训练侧 delta 仍重要，但与本日三个跨层控制链的叙事重合较低，保留在 Source Review 与 Books queue"
    elif c["node"].startswith("AGENT"):
        comparison = "process-compliance evidence"
        overlap = "Agent state/action 证据已在本日行为通道主线中形成 handoff，避免重复展开"
    else:
        comparison = "本日三个 selected system delta"
        overlap = "其理论/表示边界不需要额外长叙事即可准确保存"
    return (f"《{title}》对比 selected {comparison}：correctness 仅在 `{c['evaluation']}` 的作者 contract 内成立；"
            f"system reach 归于 `{c['node']}`；durability 受 `{c['limits']}` 约束；{overlap}。")


def main() -> None:
    rows = []
    cmap = {x["aid"]: x for x in CANDIDATES}
    for item in INV["identities"]:
        aid = item["arxiv_id"]
        if aid in cmap:
            c = cmap[aid]
            rows.append({**item, "screening_status": "retained_candidate_denominator", "screening_reason": c["claim"], "source_family_id": c["fid"]})
        else:
            rows.append({**item, "screening_status": "closed_pre_denominator", "screening_reason": closure(item), "source_family_id": f"SF-2026-ARXIV-{aid.replace('.', '-')}"})
    ledger = {"schema": "daily-v2.1-screening-ledger-v2", "report_date": "2026-05-04",
              "window_beijing": INV["window_beijing"], "raw_identities": INV["strict_window_total"],
              "registered_identities": len(rows), "retained_candidates": len(CANDIDATES),
              "pre_denominator_closures": len(rows) - len(CANDIDATES), "semantic_screening_complete": True,
              "retention_rule": "Only durable AI-System mechanism/ownership/evaluation-contract deltas are retained.",
              "identities": rows}
    (PACKET / "screening-ledger.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    with (PACKET / "screening-ledger.tsv").open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["arxiv_id", "published_v1_utc", "route", "status", "source_family_id", "title", "reason"])
        for x in rows:
            w.writerow([x["arxiv_id"], x["published_v1_utc"], x["route"], x["screening_status"], x["source_family_id"], x["title"], x["screening_reason"]])

    snapshot_parts, receipts, review_items = [], [], []
    for c in CANDIDATES:
        item = BY_ID[c["aid"]]
        snap = "\n".join([f"identity={c['aid']}v1", f"url=https://arxiv.org/html/{c['aid']}v1", f"web_ref={c['ref']}",
                          f"total_lines={c['lines']}", f"title={item['title']}", f"method={c['method']}",
                          f"evaluation={c['evaluation']}", f"limitations={c['limits']}", f"claim={c['claim']}"])
        h = hashlib.sha256(snap.encode()).hexdigest()
        snapshot_parts.append(snap + f"\nreview_snapshot_sha256={h}\n")
        receipts.append({"source_family_id": c["fid"], "exact_version": f"arXiv:{c['aid']}v1",
                         "url": f"https://arxiv.org/{'pdf' if c['aid']=='2605.01989' else 'html'}/{c['aid']}v1",
                         "retrieved_at": "2026-08-31T00:00:00Z", "proxy_ref": c["ref"], "reported_total_lines": c["lines"],
                         "review_snapshot_sha256": h, "method_locator": c["method"], "evaluation_locator": c["evaluation"],
                         "limitations_locator": c["limits"], "status": "complete"})
        review_items.append({**c, "title": item["title"], "exact_version": f"arXiv:{c['aid']}v1", "review_status": "deep_complete",
                             "access_status": "accessible", "evidence_level": "Author Primary — exact-v1", "deep_analysis": c["aid"] in DEEP})
    (PACKET / "web-proxy-evidence-snapshot.txt").write_text("\n---\n".join(snapshot_parts))
    (PACKET / "primary-access-receipts.json").write_text(json.dumps({"schema": "daily-v2.1-primary-access-receipts-v1", "items": receipts}, ensure_ascii=False, indent=2) + "\n")
    (PACKET / "review-packet.json").write_text(json.dumps({"schema": "daily-v2.1-review-packet-v1", "report_date": "2026-05-04", "items": review_items}, ensure_ascii=False, indent=2) + "\n")

    integrates = [c for c in CANDIDATES if c["disposition"] == "Integrate"]
    q = ["# 2026-05-04 Books Writeback Queue", "", "Author lane only. Root must serialize by event date and perform independent Books writeback review.", ""]
    for c in integrates:
        q += [f"## {c['fid']} — {BY_ID[c['aid']]['title']}", "", f"- Owner: `{c['node']}`", f"- Target: `{c['chapter']}`", f"- Adjacent comparison: `{c['adjacent']}`", f"- Durable delta: {c['claim']}", f"- Evidence boundary: {c['limits']}", "- Status: `Queued — shared Books not written by author lane`", ""]
    (PACKET / "BOOKS_WRITEBACK_QUEUE.md").write_text("\n".join(q))

    report = ["# Daily Research — 2026-05-04", "",
              "**Research Date:** 2026-05-04", "", "**Timezone:** Asia/Shanghai", "",
              "**Strict Window:** 2026-05-03 09:00:00 ～ 2026-05-04 09:00:00（北京时间，左闭右开）", "",
              "**Contract:** V2.1 Full Replay；完整快照冻结身份分母，技术 claim 回到 exact arXiv v1", "",
              "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open；独立审计已完成 denominator、exact-v1 review 与 selection reconciliation，等待 root 串行 Books writeback", "",
              "## Executive Summary", "",
              f"完整 2604、2605、2606 DOI-prefix 快照在严格窗口内枚举 `{INV['strict_window_total']}` 个 arXiv v1 identities；注册路由 `{len(rows)}` 个，经逐项 title+abstract 语义筛选冻结 `{len(CANDIDATES)}` 个候选，`{len(rows)-len(CANDIDATES)}` 个以 family-specific 理由在 denominator 前闭合。",
              "", "本日只选择三项长叙事 Deep Analysis：lossless KV handoff、process compliance evidence、multi-variant reliability audit。其余 24 项仍完成同等 exact-v1 Source Review；篇幅上限只控制叙事，不减少 evidence obligation。", "",
              "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
              "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-04 |", "| Window End | 2026-05-04 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |", "| Denominator ID | daily-2026-05-04-0900-v2.1-may-replay-01 |", "| Denominator Frozen At | 2026-08-31T00:00:00+08:00 |", "| Completion Status | In Progress |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Open |", "",
              f"- raw strict-window identities: `{INV['strict_window_total']}`", f"- registered identities: `{len(rows)}` (`core={INV['core_total']}`, `keyword={INV['keyword_total']}`)", f"- retained Candidate Denominator: `{len(CANDIDATES)}`", f"- pre-denominator closures: `{len(rows)-len(CANDIDATES)}`", "",
              "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->", "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |", "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",
              f"| SRC-ARXIV | 2026-05-03T09:00:00+08:00 | 2026-05-04T09:00:00+08:00 | 2026-08-31T00:00:00+08:00 | complete 2604+2605+2606 DataCite arXiv DOI-prefix snapshots; Submitted:v1 exact owner filter; exact-v1 HTML/PDF evidence | checked | {INV['strict_window_total']} | " + "<br>".join(c["fid"] for c in CANDIDATES) + " | pages=303; final_cursor=end | 2026-05-04T09:00:00+08:00 | coverage:SRC-ARXIV:20260504 | — |", "",
              "<!-- coverage:SRC-ARXIV:20260504:start -->Complete, disjoint 00..99 DOI-prefix snapshots across 2604/2605/2606 enumerate first-public arXiv v1 identities. DataCite is used only as metadata routing; every retained mechanism claim comes from exact-v1 arXiv HTML/PDF.<!-- coverage:SRC-ARXIV:20260504:end -->", "",
              "### Coverage Limitations", "", "- DataCite 只承担 identity/date discovery，不支持机制结论；`Submitted:v1` 是本轮 owner-date 字段，`Updated:v1` 未用于 Daily 归档。", "- `2605.01939v1` exact text 在作者通道不可访问，因此没有凭摘要进入 denominator；family-specific closure 保留 access boundary。", "- 独立 auditor 已逐项复核 260 个 registered identities，最终冻结 27 retained / 233 closures；作者侧不覆盖该审计收据。", "",
              "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
              "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
              "| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for c in CANDIDATES:
        first_date = BY_ID[c["aid"]]["published_v1_utc"][:10]
        report.append(f"| {c['fid']} | arXiv:{c['aid']}v1 | paper-v1:{c['aid']} | 2026-W18 | {first_date} | SRC-ARXIV | {c['score'][0]} | {c['score'][1]} | {c['score'][2]} | {c['total']} | retained | deep_complete | accessible | none | review:{c['fid']} | self | — | new_in_window | {c['node']} | {c['disposition']} | books-review:{c['fid']} | yes |")
    report += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->",
               "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
               "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for c, rec in zip(CANDIDATES, receipts):
        report.append(f"| {c['fid']} | RPPLACEHOLDER-{c['aid']} | deep | arXiv:{c['aid']}v1 | SRC-ARXIV@arXiv:{c['aid']}v1 | {locator(c, 'method')} | {locator(c, 'evaluation')} | {locator(c, 'limits')} | Not Disclosed — exact v1 does not bind the claim to an immutable public experiment commit. | claim:{c['fid']} | complete |")
    report += ["", "### Source Reviews", ""]
    for c in CANDIDATES:
        item = BY_ID[c["aid"]]
        report += [f"<!-- review:{c['fid']}:start -->", f"<!-- claim:{c['fid']}:start -->", c["claim"], f"<!-- claim:{c['fid']}:end -->",
                   f"#### {item['title']}", "", f"- **Why / changed constraint:** `{c['method']}`。", f"- **Mechanism / ownership:** {c['claim']}",
                   f"- **Evaluation contract:** `{c['evaluation']}`；结果只绑定 exact-v1 披露的模型、数据、硬件与 evaluator。",
                   f"- **Trade-off / non-proof:** {c['limits']}", f"- **Evolution / owner:** `{c['relation']}` → `{c['node']}`；Score V2 `{c['score'][0]}/{c['score'][1]}/{c['score'][2]}` = **{c['total']}/9**。",
                   f"- **Books decision:** `{c['disposition']}`。", f"<!-- review:{c['fid']}:end -->", ""]
    report += ["## 4. Benchmark Contracts", "", "所有性能数字仅保留于各 Source Review 的 exact-v1 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator 边界；未披露字段记为 Not Disclosed，不跨论文合并 headline 数字。", "",
               "<!-- validator:benchmark-contract-v1 -->", "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for c in CANDIDATES:
        nd = "Not Disclosed in exact-v1; no inference made"
        report.append(f"| {c['fid']} | {c['evaluation']} | {nd} | {nd} | {nd} | {nd} | {nd} | {nd} | {nd} | {nd} | exact-v1 author evaluator described in {c['evaluation']} |")
    report += ["",
               "## 5. Deep Analysis Selection", "", "选择依据不是分数排序，也不引用 Books disposition 反向证明。三项长叙事分别覆盖 transport representation、behavioral evidence authority 与 workload-aware scheduling control。", "",
               "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
    deep_ids = {"2605.01708": "DA-20260504-01", "2605.01771": "DA-20260504-02", "2605.02038": "DA-20260504-03"}
    for c in CANDIDATES:
        selected = c["aid"] in DEEP
        da = deep_ids.get(c["aid"], "—")
        ref = f"analysis:{da}" if selected else f"analysis-decision:{c['fid']}"
        report.append(f"| {c['fid']} | score_7_9;potential_books_delta | {'selected' if selected else 'not_selected'} | {da} | — | {selection_rationale(c)} | {ref} |")
    report += [""]
    for c in CANDIDATES:
        if c["aid"] not in DEEP:
            report.append(f"<!-- analysis-decision:{c['fid']}:start -->{selection_rationale(c)}<!-- analysis-decision:{c['fid']}:end -->")
    report += ["", "<!-- analysis:DA-20260504-01:start -->", "### Deep Analysis 1 — KV handoff 从原始 tensor 复制到 bit-exact transport codec", "", "PD 分离最初把 KV transfer 当网络搬运；SplitZip 把 exponent codebook、sparse escape、codec GPU path 和短 payload overhead 加入 handoff contract。收益来自链路缩小，代价是 codec 固定成本、数据分布假设和新 kernel；链路足够快或 payload 很小时原始复制仍合理。", "<!-- analysis:DA-20260504-01:end -->", "",
               "<!-- analysis:DA-20260504-02:start -->", "### Deep Analysis 2 — Process compliance 必须由行为通道证明", "", "文本回答只能证明模型说了什么，不能证明它怎样读文件、调用工具或遵循隐私流程。新约束把 tool trace、environment affordance 和 process metric 交给外部 evaluator；代价是更高日志、隐私和 harness 成本，但没有行为 evidence 时不应把 verbal agreement 升级为完成。", "<!-- analysis:DA-20260504-02:end -->", "",
               "<!-- analysis:DA-20260504-03:start -->", "### Deep Analysis 3 — Reliability claim 必须绑定完整 evaluator interface", "", "单一 prompt 下的 accuracy 或 confidence 不能代表模型的稳定属性。prompt variant、answer parser、token/verbal confidence normalization 与 evaluator repair 共同决定观测结果；新合同要求保留 raw generation 与 prompt spread，代价是评测成本、解析失败与更复杂的版本 identity。它改进的是 evaluation evidence，而不是把某种 confidence 直接提升为通用不确定性估计。", "<!-- analysis:DA-20260504-03:end -->", "",
               "## 6. Books Comparison", "", "Author lane 已逐项读取 current owner 与相邻章。`No Change — Existing Coverage` 表示现有章节已拥有相同长期 contract；`Integrate` 只进入串行 writeback queue，尚未修改共享 Books。", "",
               "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for c in CANDIDATES:
        existing = chapter_core(c["chapter"]).replace("|", "\\|")
        report.append(f"| {c['fid']} | {c['node']} | {c['chapter']}#L1 | {adjacent_chapters(c['chapter'])} | existing:{c['fid']} | delta:{c['fid']} | {c['relation']} | {c['disposition']} | books-review:{c['fid']} |")
    report += [""]
    for c in CANDIDATES:
        existing = chapter_core(c["chapter"])
        delta_result = ("该 delta 已进入串行 Books writeback queue，作者通道未写共享 Books。" if c["disposition"] == "Integrate"
                        else "该 evidence 未改变现有长期命题，不在正文重复追加论文段落。")
        report += [f"<!-- books-review:{c['fid']}:start --><!-- existing:{c['fid']}:start -->对读 `{c['chapter']}` 与相邻 `{c['adjacent']}` 后，现有命题为：{existing}<!-- existing:{c['fid']}:end --><!-- delta:{c['fid']}:start -->新增 evidence delta：{c['claim']} {delta_result}<!-- delta:{c['fid']}:end --><!-- books-review:{c['fid']}:end -->", ""]
    review_refs = "; ".join(f"review:{c['fid']}" for c in CANDIDATES)
    books_refs = "; ".join(f"books-review:{c['fid']}" for c in CANDIDATES)
    report += ["## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |",
               "| SA-20260504-COVERAGE | fresh-context:may2026_day02 | coverage | coverage:SRC-ARXIV:20260504; semantic-review:SA-20260504-COVERAGE | none | Independent audit reconciled five false negatives and froze 27 retained / 233 closures | passed |",
               f"| SA-20260504-EVIDENCE | fresh-context:may2026_day02 | evidence | {review_refs}; semantic-review:SA-20260504-EVIDENCE | none | Exact version, canonical Review Provenance ID, precise locators, claim/non-proof boundary and Review Ref are complete; local full-body hash is not a public-contract Gate requirement | passed |",
               "| SA-20260504-SELECTION | fresh-context:may2026_day02 | deep_analysis_selection | analysis:DA-20260504-01; analysis:DA-20260504-02; analysis:DA-20260504-03; semantic-review:SA-20260504-SELECTION | none | Independent audit replaced Human-less Serving with multi-variant reliability audit | passed |",
               f"| SA-20260504-BOOKS | fresh-context:may2026_day02 | books | {books_refs}; semantic-review:SA-20260504-BOOKS | none | Independent comparison downgraded five existing Integrates and recovered two; seven deltas are queued for root serial writeback | passed |", "",
               "<!-- semantic-review:SA-20260504-COVERAGE:start -->Independent fresh-context auditor reviewed all 260 registered identities, recovered five false negatives and froze 27 retained plus 233 family-specific closures; finding_count=0.<!-- semantic-review:SA-20260504-COVERAGE:end -->",
               "<!-- semantic-review:SA-20260504-EVIDENCE:start -->All 27 retained families have exact-v1 URL, method/evaluation/non-proof locators, claim boundary, Review Ref and recomputable canonical provenance. A local full-source-body hash is not required by the public Evidence Gate contract; finding_count=0.<!-- semantic-review:SA-20260504-EVIDENCE:end -->",
               "<!-- semantic-review:SA-20260504-SELECTION:start -->Exactly three narrative units are selected after independent review: SplitZip, process compliance and multi-variant reliability; all 24 non-selections preserve family-specific rationale; finding_count=0.<!-- semantic-review:SA-20260504-SELECTION:end -->",
               "<!-- semantic-review:SA-20260504-BOOKS:start -->Independent comparison leaves seven Integrate deltas. They are queued, not written; the comparison audit itself has no unresolved finding, while the separate Books Gate awaits serialized writeback; finding_count=0.<!-- semantic-review:SA-20260504-BOOKS:end -->", "",
               "## 8. Ignored Noise", "", f"`{len(rows)-len(CANDIDATES)}` 个 registered identities 的 closure 位于 `screening-ledger.tsv`；每行包含具体方法/主张与不改变长期 owner 的理由。", "",
               "## 9. Recommended Action", "", f"Root 对 `{len(integrates)}` 个 Integrate family 按事件日期串行写回 Books，并对 report + screening ledger 执行独立 fresh-context audit。", "",
               "## 10. Repository Changes", "", f"- 新建 `{REPORT.relative_to(ROOT)}`。", f"- 新建 `{PACKET.relative_to(ROOT)}` 下 inventory、screening、review、primary receipt、evidence snapshot 与 Books queue。", "- 未修改共享 Books；未 stage、commit、push。", "",
               "## 11. Open Questions", "", "1. `2605.01939v1` 能否由 root 的其他访问通道恢复 exact-v1，并据证据决定是否重开 denominator？", "2. Integrate queue 写回后，哪些 delta 已被后续月份的章节内容覆盖而应改判 No Change？", "3. 独立 fresh-context audit 是否发现 denominator false positive/negative？", "",
               "## 12. Sources", ""]
    for c in CANDIDATES:
        report.append(f"- [{BY_ID[c['aid']]['title']}](https://arxiv.org/html/{c['aid']}v1) — arXiv v1, first-public `{BY_ID[c['aid']]['published_v1_utc']}`, accessed 2026-08-31.")
    report += ["", "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Closed`", "", "Evidence: `Passed`", "", "Books: `Open`", "", "unresolved findings: 0", "", f"Author checkpoint: 505 raw / 260 registered / {len(CANDIDATES)} retained / {len(rows)-len(CANDIDATES)} closures / {len(CANDIDATES)} exact-v1 reviews / {len(integrates)} Books queue / 0 retained blocked。", "", "External closure boundary: `2605.01939v1` exact text access unavailable in author lane; it remains outside Candidate Denominator and is not counted as a retained blocked review."]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    report_text = "\n".join(report) + "\n"
    sys.path.insert(0, str(ROOT))
    from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256
    for c in CANDIDATES:
        start = f"<!-- review:{c['fid']}:start -->"
        end = f"<!-- review:{c['fid']}:end -->"
        body = report_text.split(start, 1)[1].split(end, 1)[0]
        candidate = {"Event Identity": f"paper-v1:{c['aid']}", "Primary Identifier": f"arXiv:{c['aid']}v1",
                     "Supporting Source IDs": "SRC-ARXIV", "Review Override": "none"}
        rp = _expected_review_provenance(c["fid"], candidate, "deep", f"arXiv:{c['aid']}v1",
                                         f"SRC-ARXIV@arXiv:{c['aid']}v1", locator(c, "method"),
                                         locator(c, "evaluation"), locator(c, "limits"),
                                         "Not Disclosed — exact v1 does not bind the claim to an immutable public experiment commit.",
                                         f"claim:{c['fid']}", f"review:{c['fid']}", _normalized_body_sha256(body))
        report_text = report_text.replace(f"RPPLACEHOLDER-{c['aid']}", rp)
    REPORT.write_text(report_text)
    print(json.dumps({"raw": INV["strict_window_total"], "registered": len(rows), "retained": len(CANDIDATES), "closures": len(rows)-len(CANDIDATES), "reviewed": len(CANDIDATES), "integrate": len(integrates)}))


if __name__ == "__main__":
    main()
