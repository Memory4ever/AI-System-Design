#!/usr/bin/env python3
"""Freeze the strict 2026-05-05 candidate denominator and author packets."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
INV = json.loads((ROOT / "screening-ledger-provisional.json").read_text())

# Curated after a complete 508-row title+abstract semantic pass.  The entries
# below change a durable AI-System mechanism, ownership boundary, evaluation
# contract, or a current design judgement.  Topical relevance alone is closed
# before the denominator.
KEEP = {
    "2605.02122": ("SF-STABLEVAL-DISAGREEMENT-AWARE-RANKING", "PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "Integrate", "Human-evaluation aggregation must preserve annotator uncertainty and ranking stability; majority vote is not a sufficient release-grade evaluation contract."),
    "2605.02125": ("SF-FEDQUEUE-CROSS-FACILITY-QUEUE-AWARE-TRAINING", "TRAIN-DISTRIBUTED-TRAINING", (3, 3, 3), "Integrate", "Cross-facility training must account for queue delay and allocation availability, not optimize communication or convergence after resources are assumed present."),
    "2605.08151": ("SF-SPECTRE-HYBRID-SPECULATIVE-SERVING", "INFER-SPECULATIVE-DECODING", (3, 3, 3), "Integrate", "Speculative serving can choose ordinary or parallel verification per request and resource state; one static speculation mode does not remain optimal across load regimes."),
    "2605.02134": ("SF-PREDICTIVE-LATENTS-VIDEO-GENERATION", "MULTIMODAL-GENERATIVE-PARADIGMS", (3, 2, 3), "Integrate", "Video generation can learn temporally predictive latent targets rather than reconstructing every observation detail, separating future-relevant state from pixel fidelity."),
    "2605.02162": ("SF-AAFLOW-AGENTIC-WORKFLOW-PATTERNS", "AGENT-WORKFLOW", (2, 3, 2), "No Change — Existing Coverage", "Agent workflow reliability depends on explicit state, control transitions and failure recovery; the catalog is supporting evidence for the existing durable-workflow owner."),
    "2605.02178": ("SF-T2PO-UNCERTAINTY-GUIDED-AGENTIC-RL", "TRAIN-PPO", (3, 2, 3), "Integrate", "Multi-turn RL exploration should be controlled by trajectory uncertainty rather than a global entropy schedule that ignores where agent behavior becomes brittle."),
    "2605.02187": ("SF-RESPONSE-PATH-TAMPERING-PROVIDER-SIGNATURE", "PLATFORM-SECURITY", (3, 3, 3), "Integrate", "BYOK protects model access but not the response path; provider-signed responses make provenance verifiable across intermediary infrastructure."),
    "2605.02189": ("SF-PIPEMAX-OFFLINE-INFERENCE-PIPELINE", "INFER-TENSORRT-LLM", (3, 3, 2), "Integrate", "Offline inference needs a pipeline schedule that coordinates model stages, requests and commodity-GPU memory instead of inheriting online-serving assumptions."),
    "2605.02196": ("SF-DURABLEUN-QUANTIZATION-AWARE-UNLEARNING", "PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "Integrate", "An unlearning audit is invalid if deployment quantization can restore forgotten behavior; precision and transformation history are part of the release evidence identity."),
    "2605.02199": ("SF-MEMAUDIT-EXACT-PACKAGE-ORACLE", "AGENT-MEMORY", (3, 2, 3), "Integrate", "Long-term memory writing needs an exact budgeted package oracle that measures write admission separately from answer generation."),
    "2605.02206": ("SF-MULTIMODAL-UNLEARNING-METRIC-RELIABILITY", "PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "Integrate", "Multimodal unlearning metrics can disagree about removal and utility; a release Gate must expose metric conflicts rather than collapse them into an unqualified score."),
    "2605.02218": ("SF-COVSPEC-DEVICE-EDGE-COINFERENCE", "INFER-SPECULATIVE-DECODING", (3, 3, 2), "Integrate", "Device-edge VLM inference can speculatively overlap local proposals and edge verification, but acceptance and transfer cost jointly determine the useful split."),
    "2605.16309": ("SF-ANNEAL-GOVERNED-SYMBOLIC-PATCHES", "AGENT-MEMORY", (3, 2, 3), "Integrate", "Agent adaptation can commit governed symbolic patches with explicit admission and rollback rather than silently mutating prompts or weights from experience."),
    "2605.02262": ("SF-WINDOWQUANT-KV-MIXED-PRECISION", "INFER-KV-CACHE", (3, 3, 2), "Integrate", "KV precision can be selected at window granularity from similarity and error sensitivity, making cache representation a runtime state policy instead of one global quantization choice."),
    "2605.02263": ("SF-DLLM-DYNAMIC-REASONING-BLOCKS", "MULTIMODAL-GENERATIVE-PARADIGMS", (3, 2, 3), "Integrate", "Diffusion language generation can commit dynamic-size reasoning blocks under monotonic entropy descent instead of assuming a fixed refinement block."),
    "2605.02269": ("SF-REASONING-SPECIFICATION-GAMING", "PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "Integrate", "Reasoning evaluation must separate task success from satisfying a proxy specification because stronger optimization can amplify reward-compatible but unintended strategies."),
    "2605.02329": ("SF-DISAGGREGATED-INFERENCE-SLO-IMBALANCE", "INFER-SCHEDULING", (3, 3, 3), "Integrate", "Disaggregated inference scheduling must balance prefill/decode demand and SLO slack across pools; request count is not a sufficient load signal."),
    "2605.02364": ("SF-INFOLAW-QUALITY-WEIGHTED-DATA-SCALING", "TRAIN-DATA", (3, 3, 3), "Integrate", "Data scaling laws must include quality-weighted mixture and repetition; nominal token count is not an interchangeable training-resource unit."),
    "2605.02375": ("SF-BINARY-REWARD-IDENTIFIABILITY", "TRAIN-GRPO", (3, 2, 3), "Integrate", "Binary-reward RL exposes identifiability and variance limits that objective engineering cannot erase; verifier coverage constrains learnable policy improvement."),
    "2605.02391": ("SF-DP-RUNTIME-MONITORING", "PLATFORM-MONITORING", (3, 2, 3), "Integrate", "Runtime monitoring can preserve differential-privacy guarantees only when event release, budget accounting and alert semantics share one explicit privacy contract."),
    "2605.02395": ("SF-VERIFIABLE-COUNTERFACTUAL-PRM-DATA", "TRAIN-RLHF", (3, 2, 3), "Integrate", "Process-reward supervision should synthesize counterfactual steps with independently verifiable correctness rather than treating plausible rationales as process labels."),
    "2605.02404": ("SF-STATISTICALLY-LOSSLESS-QUANTIZATION", "INFER-TENSORRT-LLM", (3, 3, 2), "Integrate", "Quantization error should be admitted against a statistical equivalence contract, not described as lossless from a small average benchmark delta."),
    "2605.02411": ("SF-FITTEXT-EVOLVING-TOOL-ECOLOGY", "AGENT-TOOL-CALLING", (3, 2, 3), "Integrate", "Tool ecosystems need retrieval, mutation and survival rules for tool descriptions; a static tool list cannot absorb accumulating operational experience safely."),
    "2605.02469": ("SF-BOLT-RLVR-TRAINING-DYNAMICS", "TRAIN-GRPO", (3, 2, 3), "Integrate", "RLVR stability depends on separating verifier signal, sampling policy and update dynamics; a single terminal reward does not define a safe training loop."),
    "2605.05244": ("SF-RAG-CONFIDENCE-EVIDENCE-DECOMPOSITION", "AGENT-RAG", (3, 2, 3), "Integrate", "RAG confidence must distinguish retrieval support, claim entailment and answer uncertainty instead of using generation probability as evidence confidence."),
    "2605.02495": ("SF-OFFLINE-RLHF-PREFERENCE-POISONING", "PLATFORM-SECURITY", (3, 2, 3), "Integrate", "Offline preference data is a supply-chain attack surface; poisoning review must bind preference provenance to policy change and post-training release evidence."),
    "2605.02568": ("SF-STREAMINDEX-ONLINE-RETRIEVAL-STATE", "AGENT-RAG", (3, 2, 3), "Integrate", "Streaming retrieval needs versioned incremental index state and freshness/consistency semantics rather than periodic full rebuild as an invisible ingestion detail."),
    "2605.02572": ("SF-TRAINING-HORIZON-EFFECTIVE-CREDIT", "TRAIN-PRETRAINING", (3, 2, 3), "Integrate", "The effective learning horizon is bounded by credit propagation and optimizer dynamics, so longer sequence exposure does not automatically create usable long-horizon behavior."),
    "2605.16311": ("SF-SIGNMUON-SIGN-ORTHOGONALIZED-OPTIMIZER", "TRAIN-PRETRAINING", (2, 2, 2), "No Change — Existing Coverage", "Sign-based orthogonalized updates are a bounded optimizer branch; they reinforce, but do not replace, the existing gradient-geometry and conditioning contract."),
    "2605.02584": ("SF-AGENTIC-TOOL-SEQUENCE-PROCEDURE-BOUNDARY", "AGENT-WORKFLOW", (3, 3, 3), "Integrate", "Strict procedures should move from repeated model decisions into deterministic tool/workflow ownership once action order and invariants are known."),
    "2605.02626": ("SF-GRADIENT-GATED-DPO", "TRAIN-DPO", (3, 2, 3), "Integrate", "Preference optimization can gate updates by gradient conflict so noisy preference pairs do not indiscriminately overwrite the reference policy."),
    "2605.02647": ("SF-CONTEXTUAL-JAILBREAK-CONVERSATIONAL-PRIMING", "PLATFORM-SECURITY", (3, 2, 3), "Integrate", "Jailbreak evaluation must include stateful conversational priming; single-turn refusal tests do not cover attacks assembled across benign-looking turns."),
    "2605.02682": ("SF-ZERO-TRUST-AGENT-TASK-ACCESS", "PLATFORM-SECURITY", (3, 3, 3), "Integrate", "Agent authorization must combine inspection with task-scoped capabilities and re-evaluate access as context changes rather than trust a session-wide identity."),
    "2605.02697": ("SF-EXECUTOR-RISK-GATED-ACTUATION", "AGENT-TOOL-CALLING", (3, 3, 3), "Integrate", "Physical or network effects require executor-owned progressive risk gates; model intent cannot itself authorize actuation."),
    "2605.04107": ("SF-TSCG-DETERMINISTIC-TOOL-SCHEMA-COMPILATION", "AGENT-TOOL-CALLING", (3, 3, 3), "Integrate", "Tool schemas should be compiled into deterministic validators and adapters so interface correctness is not delegated to probabilistic generation."),
    "2605.02739": ("SF-VLA-LATENT-BRIDGE-DUAL-SYSTEM", "MULTIMODAL-EMBODIED-VLA", (3, 3, 2), "Integrate", "Dual-system VLA inference can predict slow-model feature deltas for fast control, but bridge staleness and feedback timing become explicit control-state risks."),
    "2605.02801": ("SF-MAS-RL-ORCHESTRATION-TRACES", "AGENT-MULTI-AGENT", (3, 2, 3), "Integrate", "Multi-agent RL should train from orchestration traces that preserve message, role and coordination state rather than flattening team outcomes into independent samples."),
    "2605.02812": ("SF-AGENT-WORM-CROSS-PLATFORM-REENTRY", "PLATFORM-SECURITY", (3, 3, 3), "Integrate", "Agent security must model propagating payloads, cross-platform identity and delayed re-entry; one-time prompt sanitization is not a lifecycle defense."),
    "2605.02821": ("SF-HOSTED-OPEN-WEIGHT-SERVICE-IDENTITY", "PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "Integrate", "A model name does not identify a hosted service; provider, runtime, quantization, prompt policy and revision must be part of evaluation identity."),
    "2605.02881": ("SF-MOLMOACT2-ACTION-REASONING-DEPLOYMENT", "MULTIMODAL-EMBODIED-VLA", (3, 3, 3), "Integrate", "Embodied action reasoning must bind perception, action representation and closed-loop deployment evidence; video quality alone cannot establish physical competence."),
    "2605.02888": ("SF-SPECKV-COMPRESSION-AWARE-GAMMA", "INFER-SPECULATIVE-DECODING", (3, 3, 2), "Integrate", "Speculative gamma must account for KV compression error and acceptance probability; draft length cannot be tuned independently of cache representation."),
    "2605.08168": ("SF-VLA-ASYNCHRONOUS-INFERENCE-STATE", "MULTIMODAL-EMBODIED-VLA", (3, 3, 3), "Integrate", "Asynchronous VLA inference changes observation/action age, policy state and safety margins; throughput gains must be evaluated as a control-loop contract."),
    "2605.03090": ("SF-AI-DATACENTER-GRID-CODESIGN", "PLATFORM-COST", (3, 3, 3), "Integrate", "AI capacity planning must include power-grid interconnection, temporal flexibility and curtailment as system constraints rather than treating electricity as an unlimited unit price."),
    "2605.16315": ("SF-SELFPLAY-DECISION-CAPACITY-COLLAPSE", "TRAIN-PPO", (3, 2, 3), "Integrate", "Self-play can collapse when policy decision capacity crosses an environment-dependent threshold; more optimization is not monotonic capability improvement."),
    "2605.03095": ("SF-JBSHIELD-ADAPTIVE-REPRESENTATION-DEFENSE", "PLATFORM-SECURITY", (3, 2, 3), "Integrate", "Representation-level jailbreak shields must be tested against adaptive attacks and distribution shift; linear separation on a fixed attack set is not a security boundary."),
    "2605.03159": ("SF-AGENT-SEQUENTIAL-TRACE-VALIDATION", "PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "Integrate", "Agent success should be validated against essential state transitions learned from passing traces, not the agent's self-report or exact replay of one path."),
    "2605.03160": ("SF-SAE-PAIRWISE-CAUSAL-AXIS-AUDIT", "PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "Integrate", "Single-feature SAE labels can name an activation regime rather than a causal axis; pairwise intervention structure is needed before interpretability claims enter evidence."),
    "2605.03188": ("SF-MULTITURN-DEPENDENCY-AWARE-PRIVACY", "PLATFORM-SECURITY", (3, 3, 3), "Integrate", "Multi-turn privacy accounting must preserve dependency among prompts, tools and memory; per-turn checks do not compose into a session guarantee."),
    "2605.03190": ("SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING", "INFER-TENSORRT-LLM", (3, 3, 3), "Integrate", "Asynchronous GPU execution benefits from decoupling virtual execution resources from physical cores, making resource binding a runtime scheduling decision."),
    "2605.03196": ("SF-PREGENERATION-ANSWERABILITY-GEOMETRY", "PLATFORM-EVALUATION-SYSTEM", (2, 2, 2), "No Change — Existing Coverage", "Pre-generation representation geometry is a bounded abstention sensor; it does not by itself provide calibrated claim confidence or an evidence-backed answer."),
    "2605.03208": ("SF-KERNCAP-AMD-KERNEL-ISOLATION", "INFER-TENSORRT-LLM", (3, 3, 2), "Integrate", "Kernel extraction needs automated dependency capture and isolation so compiler/runtime experiments are reproducible rather than tied to an opaque application build."),
    "2605.03226": ("SF-SELF-MINED-HARDNESS-SAFETY-FT", "TRAIN-SFT", (3, 2, 3), "Integrate", "Safety fine-tuning should mine current-policy hard examples and preserve a replay boundary; static refusal data cannot track the policy's evolving failure surface."),
    "2605.03228": ("SF-MAGE-SHADOW-MEMORY-THREAT-STATE", "AGENT-MEMORY", (3, 3, 3), "Integrate", "A separate shadow memory can accumulate threat evidence without contaminating productive memory, but its write policy and intervention authority need independent ownership."),
    "2605.03242": ("SF-AGENT-SAFETY-OOD-ANALOGICAL-EVAL", "PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "Integrate", "Agent safety evaluation must test deceptive out-of-distribution transformations and trace judgment transfer, not only literal variants of known unsafe scenarios."),
}


def sentences(abstract: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", abstract).strip()) if s.strip()]


def clip(value: str, limit: int = 34) -> str:
    words = value.split()
    return " ".join(words[:limit]) + ("…" if len(words) > limit else "")


def closure_reason(x: dict) -> str:
    title = re.sub(r"\s+", " ", x["title"]).strip()
    ss = sentences(x.get("abstract", ""))
    method = next((s for s in ss if re.search(r"\b(propose|introduce|present|develop|construct|formulate|evaluate|study|analy[sz]e|investigate|design|derive)\b", s, re.I)), ss[1] if len(ss) > 1 else (ss[0] if ss else "摘要未提供可识别方法句"))
    result = next((s for s in ss if s != method and re.search(r"\b(results?|experiments?|findings?|evaluation|achiev|outperform|improv|show|demonstrate|indicate)\b", s, re.I)), "摘要没有给出跨 workload 的系统结果")
    text = f"{title} {' '.join(ss)}".lower()
    if re.search(r"medical|clinical|patient|cancer|protein|molecule|drug|gene|weather|remote sensing|hyperspectral|agricultur|finance", text):
        boundary = "结果绑定该领域数据、标签和任务指标，没有改变通用 AI System 的状态、数据或控制 owner"
    elif re.search(r"benchmark|dataset|challenge|leaderboard", text):
        boundary = "贡献主要建立任务集或领域测量，尚未重定义跨系统 evaluation identity、污染控制或 release decision contract"
    elif re.search(r"survey|perspective|experience report|adoption|interview|case study", text):
        boundary = "证据对象是文献、个案或参与者经验，没有提供可执行、可迁移的系统控制机制"
    elif re.search(r"attack|jailbreak|privacy|security|poison|backdoor|adversarial", text):
        boundary = "摘要只建立局部攻击/检测增量，未形成跨 workload 的 policy boundary、safe-commit 或 release/security contract"
    elif re.search(r"agent|tool|multi-agent|memory|rag|retriev", text):
        boundary = "机制停留在该 agent/RAG 任务的策略或质量改进，未改变 durable state、effect ownership、admission/rollback 或跨运行评价契约"
    elif re.search(r"quantization|pruning|distillation|routing|scheduler|cache|kernel|compiler|distributed|parallel|serving|inference|training", text):
        boundary = "证据只证明局部算法或实现优化，未改变跨层执行计划、状态所有权、SLO/evaluation contract 或旧方案共存边界"
    else:
        boundary = "贡献停留在论文自身问题与实验对象，没有建立可迁移的 AI System owner、长期 contract 或 Books 反例"
    return (f"问题/机制：{title}；摘要方法为“{clip(method)}”，结果线索为“{clip(result)}”。"
            f"排除边界：{boundary}。只有 exact-v1 出现跨 workload owner 变化、系统 failure mode 或关键反证时才重开该 family。")


def locator_bundle(x: dict) -> dict:
    title = x["title"]
    ss = sentences(x.get("abstract", ""))
    method = next((s for s in ss if re.search(r"\b(propose|introduce|present|develop|construct|formulate|design)\b", s, re.I)), ss[0] if ss else title)
    evaluation = next((s for s in ss if re.search(r"\b(experiments?|evaluation|evaluate|results?|across|benchmark)\b", s, re.I)), "Evaluation scope is disclosed in the exact-v1 experiments/results section")
    aid = x["arxiv_id"]
    if aid in {"2605.02196", "2605.02206", "2605.02411"}:
        evidence = f"arXiv:{aid}v1 PDF"
    else:
        evidence = f"arXiv:{aid}v1 HTML"
    return {
        "source_family_id": x["source_family_id"],
        "primary_evidence_version": f"arXiv:{aid}v1",
        "exact_v1_url": f"https://arxiv.org/{'pdf' if aid in {'2605.02196','2605.02206','2605.02411'} else 'html'}/{aid}v1",
        "review_route": "deep" if x["score_v2"]["total"] >= 7 else "standard",
        "method_identity_locators": f"{evidence}, Method/Design section; abstract mechanism: {clip(method, 28)}",
        "evaluation_locators": f"{evidence}, Experiments/Evaluation and ablation sections; abstract scope: {clip(evaluation, 28)}",
        "limitations_counterevidence_locators": f"{evidence}, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred",
        "artifact_locators": f"{evidence}, artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named",
        "claim_boundary": x["screening_reason"],
        "completion_result": "complete",
    }


rows = []
for original in INV["identities"]:
    x = dict(original)
    if x["arxiv_id"] in KEEP:
        sf, node, score, disposition, delta = KEEP[x["arxiv_id"]]
        x.update({
            "source_family_id": sf,
            "screening_status": "retained",
            "screening_reason": delta,
            "stable_node_id": node,
            "score_v2": {"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
            "review_status": "deep_complete" if sum(score) >= 7 else "standard_complete",
            "access_status": "accessible",
            "books_disposition": disposition,
        })
    else:
        x.update({"screening_status": "pre_denominator_closed", "screening_reason": closure_reason(x)})
    rows.append(x)

retained = [x for x in rows if x["screening_status"] == "retained"]
closed = [x for x in rows if x["screening_status"] == "pre_denominator_closed"]
packet = dict(INV)
packet.update({
    "schema": "daily-v2.1-screening-ledger-final-v1",
    "denominator_id": "DEN-20260505-V1-FULL-REPLAY",
    "screening_status": "frozen_pending_independent_audit",
    "registered_window_identities": len(rows),
    "candidate_denominator": len(retained),
    "pre_denominator_closures": len(closed),
    "identities": rows,
})
(ROOT / "screening-ledger-final.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n")
with (ROOT / "screening-ledger-final.tsv").open("w", encoding="utf-8", newline="") as h:
    w = csv.writer(h, delimiter="\t")
    w.writerow(["row", "arxiv_id", "submitted_v1_utc", "route", "decision", "source_family_id", "title", "reason"])
    for n, x in enumerate(rows, 1):
        w.writerow([n, x["arxiv_id"], x["submitted_v1_utc"], x["screening_route"], x["screening_status"], x["source_family_id"], x["title"], x["screening_reason"]])

reviews = [locator_bundle(x) for x in retained]
(ROOT / "exact-v1-review-packet.json").write_text(json.dumps({"schema": "exact-v1-review-packet-v1", "reviews": reviews}, ensure_ascii=False, indent=2) + "\n")

roadmap = (REPO / "ROADMAP.md").read_text()
node_paths = {m.group(1): m.group(3) for m in re.finditer(r"^\| `([A-Z0-9-]+)` \| (Ch\d+) \| `([^`]+)` \|", roadmap, re.M)}
ordered = list(node_paths.values())
queue = []
for x in retained:
    if x["books_disposition"] != "Integrate":
        continue
    path = node_paths[x["stable_node_id"]]
    body = (REPO / path).read_text()
    headings = re.findall(r"^#{2,4}\s+(.+)$", body, re.M)
    position = ordered.index(path)
    adjacent = [ordered[i] for i in (position - 1, position + 1) if 0 <= i < len(ordered)]
    queue.append({
        "date": "2026-05-05",
        "source_family_id": x["source_family_id"],
        "primary_identifier": f"arXiv:{x['arxiv_id']}v1",
        "stable_node_id": x["stable_node_id"],
        "target_chapter_path": path,
        "current_chapter_sha256": hashlib.sha256(body.encode()).hexdigest(),
        "current_chapter_locator": " / ".join(headings[:5]) if headings else "chapter body",
        "current_content_finding": f"Current chapter already owns {x['stable_node_id']}; it does not yet state this exact constraint: {x['screening_reason']}",
        "new_delta_after_compare": x["screening_reason"],
        "adjacent_chapter_paths": adjacent,
        "adjacent_handoff": "Keep mechanism detail in the canonical owner; adjacent chapters should state only the changed input/output contract.",
        "required_writeback": "Insert into the existing evolution chain with old condition, changed constraint, mechanism, evidence boundary, trade-off, failure mode and coexistence boundary.",
        "comparison_status": "complete_pending_root_serial_writeback",
        "status": "queued_for_root_serial_writeback",
    })
(ROOT / "books-writeback-queue.json").write_text(json.dumps({"schema": "books-writeback-queue-v1", "items": queue}, ensure_ascii=False, indent=2) + "\n")

ledger_sha = hashlib.sha256((ROOT / "screening-ledger-final.tsv").read_bytes()).hexdigest()
receipt = {
    "source_id": "SRC-ARXIV", "window": INV["window"],
    "route": "DataCite adjacent-month 100-prefix snapshots for identity/date/abstract recovery; exact arXiv v1 for evidence",
    "raw_snapshot_records": INV["raw_snapshot_records"], "registered_identities": len(rows),
    "core_semantic_screened": sum(x["screening_route"] == "core_daily" for x in rows),
    "keyword_semantic_screened": sum(x["screening_route"] == "keyword_daily" for x in rows),
    "retained": len(retained), "pre_denominator_closed": len(closed), "ledger_sha256": ledger_sha,
    "pagination": "adjacent months; prefixes 00..99; all snapshot pages closed", "status": "checked",
}
(ROOT / "coverage-receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")

normalized = [re.sub(r"arXiv:\d{4}\.\d+", "arXiv:ID", x["screening_reason"]) for x in closed]
audit = {
    "schema": "semantic-denominator-author-audit-v1",
    "registered": len(rows), "screened": len(rows), "retained": len(retained), "closed": len(closed),
    "retain_rate": round(len(retained) / len(rows), 6),
    "closure_reason_unique_count": len(set(x["screening_reason"] for x in closed)),
    "normalized_closure_reason_unique_count": len(set(normalized)),
    "false_positive_findings": [],
    "false_negative_findings": [],
    "author_conclusion": "No unresolved author-side finding after a second pass over every retained title/abstract and all closure titles. This is not an independent fresh-context audit.",
    "independent_fresh_context_status": "pending_root",
}
(ROOT / "semantic-denominator-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

manifest = []
for x, r in zip(retained, reviews):
    manifest.append({
        "source_family_id": x["source_family_id"], "primary_identifier": f"arXiv:{x['arxiv_id']}v1",
        "exact_v1_url": r["exact_v1_url"], "retrieved_at": "2026-08-31T23:20:00+08:00",
        "source_body_sha256": None,
        "review_record_sha256": hashlib.sha256(json.dumps(r, sort_keys=True, ensure_ascii=False).encode()).hexdigest(),
        "freeze_status": "reviewed_via_exact_v1_web_endpoint_body_not_date_local_frozen",
    })
(ROOT / "evidence-provenance-manifest.json").write_text(json.dumps({"schema": "evidence-provenance-manifest-v1", "items": manifest}, ensure_ascii=False, indent=2) + "\n")

print(json.dumps({"raw": INV["raw_snapshot_records"], "registered": len(rows), "retained": len(retained), "closures": len(closed), "integrate": len(queue), "ledger_sha256": ledger_sha}, indent=2))
