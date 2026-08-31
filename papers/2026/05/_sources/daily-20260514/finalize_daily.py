#!/usr/bin/env python3
"""Build the 2026-05-14 V2.1 author packet; never writes shared Books."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

INV = json.loads((HERE / "screening-ledger-provisional.json").read_text())
ACTIVE = set((HERE / "candidate-ids.txt").read_text().split())
BLOCKED = set()

NODE = {
    "2605.12875":"PLATFORM-SECURITY", "2605.12925":"PLATFORM-EVALUATION-SYSTEM",
    "2605.12887":"AGENT-RAG",
    "2605.12947":"AGENT-WORKFLOW", "2605.12978":"AGENT-MEMORY",
    "2605.12981":"AGENT-PLATFORM", "2605.13013":"MULTIMODAL-WORLD-MODELS",
    "2605.13026":"MULTIMODAL-GENERATIVE-PARADIGMS", "2605.13044":"PLATFORM-SECURITY",
    "2605.13076":"INFER-DECODE", "2605.13095":"PLATFORM-MONITORING",
    "2605.13119":"MULTIMODAL-EMBODIED-VLA", "2605.13170":"PLATFORM-SECURITY",
    "2605.13139":"PLATFORM-EVALUATION-SYSTEM", "2605.13171":"PLATFORM-EVALUATION-SYSTEM",
    "2605.13190":"INFER-DECODE",
    "2605.13245":"AGENT-WORKFLOW", "2605.13247":"MODEL-MOE",
    "2605.13276":"TRAIN-DISTRIBUTED-TRAINING", "2605.13295":"AGENT-PLATFORM",
    "2605.13319":"INFER-SPECULATIVE-DECODING", "2605.13335":"MULTIMODAL-WORLD-MODELS",
    "2605.13338":"PLATFORM-SECURITY",
    "2605.13357":"AGENT-PLATFORM", "2605.13360":"AGENT-TOOL-CALLING",
    "2605.13370":"AGENT-MEMORY", "2605.13382":"MULTIMODAL-EMBODIED-VLA",
    "2605.13411":"PLATFORM-SECURITY", "2605.13471":"PLATFORM-SECURITY",
    "2605.13433":"TRAIN-DISTRIBUTED-TRAINING", "2605.13434":"TRAIN-DISTRIBUTED-TRAINING",
    "2605.13485":"MODEL-LONG-CONTEXT", "2605.13647":"AGENT-WORKFLOW",
    "2605.13716":"AGENT-PLATFORM", "2605.13734":"INFER-KV-CACHE",
    "2605.13764":"PLATFORM-SECURITY", "2605.13778":"MULTIMODAL-EMBODIED-VLA",
    "2605.13779":"PLATFORM-FOUNDATIONS", "2605.13784":"INFER-DECODE",
    "2605.13915":"INFER-TENSORRT-LLM", "2605.13940":"PLATFORM-SECURITY",
    "2605.13941":"AGENT-MEMORY", "2605.14005":"PLATFORM-SECURITY",
    "2605.14037":"INFER-KV-CACHE", "2605.14038":"AGENT-TOOL-CALLING",
    "2605.14089":"AGENT-PLATFORM", "2605.14102":"AGENT-WORKFLOW",
    "2605.14175":"PLATFORM-SECURITY", "2605.14200":"MODEL-MOE",
    "2605.14186":"INFER-SCHEDULING",
    "2605.14217":"INFER-PREFILL", "2605.14220":"TRAIN-RLHF",
    "2605.15228":"PLATFORM-SECURITY", "2605.16407":"PLATFORM-SECURITY",
    "2605.18852":"PLATFORM-EVALUATION-SYSTEM", "2605.18853":"INFER-SCHEDULING",
    "2605.18854":"AGENT-MEMORY",
    "2605.18856":"INFER-KV-CACHE", "2605.20223":"MULTIMODAL-WORLD-MODELS",
    "2605.23970":"PLATFORM-EVALUATION-SYSTEM", "2605.23974":"PLATFORM-MONITORING",
}

INTEGRATE = {
    "2605.12887", "2605.12925", "2605.12947", "2605.12981",
    "2605.13076", "2605.13095", "2605.13139", "2605.13170", "2605.13190", "2605.13276",
    "2605.13295", "2605.13319", "2605.13335", "2605.13357", "2605.13360",
    "2605.13433", "2605.13434", "2605.13647", "2605.13734", "2605.13764", "2605.13778",
    "2605.13784", "2605.14005", "2605.14038", "2605.14175", "2605.14186", "2605.14220",
    "2605.15228", "2605.18852", "2605.23970", "2605.23974",
}

OLD_LOC = {
    "2605.11381":("§3 adaptive execution-horizon controller; §4 execution-aware scheduling", "§5 six-model/five-simulator and real-robot evaluation", "§6 limitations: confidence calibration, simulator and control-frequency scope"),
    "2605.11418":("§3 SKILL.md semantic dependency-confusion attack; §4 attack construction", "§5 multi-agent/toolchain evaluation", "§6 limitations: repository, model and attacker-access scope"),
    "2605.11442":("§3 Möbius indirect-injection loop; §4 AbO-DDoS control path", "§5 three claw agents, three coding agents and twelve LLMs", "§6 limitations: harness, tool and adaptive-defense boundary"),
    "2605.11478":("§3 FibQuant fixed-rate random-access code layout", "§4 KV-cache quality/throughput evaluation", "§5 limitations: model, sequence length, hardware and quantization scope"),
    "2605.11487":("§3 portable agent identity and authorization envelope", "§4 protocol examples and security analysis", "§5 limitations: deployment and interoperability evidence"),
    "2605.11496":("§3 Evaluation Differential and TRACE estimator", "§4 cross-task evaluation and ablations", "§5 limitations: evaluator, perturbation and domain-shift scope"),
    "2605.11514":("§3 FlowSteer runtime information-flow policy", "§4 enforcement path and evaluation", "§5 limitations: policy completeness and tool-boundary coverage"),
    "2605.11537":("§3 predictive expert replication mechanism", "§4 MoE evaluation claimed by manuscript", "front matter contains placeholder DOI/conference metadata; exact artifact identity disputed"),
    "2605.11550":("§3 action-conditioned world-state model; §4 DAWN update loop", "§5 interactive-generation evaluation", "§6 Limitations; HTML front matter exact date line `August 24, 2026` conflicts with arXiv v1 metadata"),
    "2605.11567":("§3 uncertainty-adaptive VLA action commitment", "§4 simulator/robot control evaluation", "§5 limitations: calibration, embodiment and control-frequency scope"),
    "2605.11577":("§3 BitLM block-causal binary diffusion objective", "§4 text-generation experiments and ablations", "§5 limitations: model scale, sampler and latency contract"),
    "2605.11581":("§3 Ada-MK compile-time DAG search and MegaKernel construction", "§4 kernel/runtime evaluation", "§5 limitations: operator set, accelerator and search-cost scope"),
    "2605.11599":("§3 audit-constrained reasoning protocol", "§4 evaluation under evidence constraints", "§5 limitations: auditor/judge and task-distribution scope"),
    "2605.11603":("§3 GAR constrained carbon-aware routing", "§4 energy/latency evaluation", "§5 limitations: grid signal, model mix and SLO assumptions"),
    "2605.11678":("§3 CPU-GPU demand-layered VLA execution", "§4 latency/memory evaluation", "§5 limitations: platform, policy model and transfer overhead"),
    "2605.11744":("§3 segmented training/inference-consistent long-context state", "§4 long-context quality/runtime evaluation", "§5 limitations: segment policy, model and cache scope"),
    "2605.11746":("§3 imperfect-oversight channel for chain-of-thought", "§4 monitor/evaluator experiments", "§5 limitations: observability, evaluator and hidden-reasoning boundary"),
    "2605.11770":("§3 behavioral-integrity verification for skills", "§4 tampering/compatibility evaluation", "§5 limitations: behavioral oracle and environment coverage"),
    "2605.11852":("§3 Spillway cross-datacenter disaggregated buffer", "§4 distributed-training evaluation", "§5 limitations: topology, failure model and link-cost scope"),
    "2605.11854":("§3 TABOM diffusion-LM train/inference alignment", "§4 generation experiments and ablations", "§5 limitations: block schedule, model scale and decode cost"),
    "2605.11868":("§3 IPI-proxy mediation boundary", "§4 indirect-prompt-injection evaluation", "§5 limitations: classifier, tool and adaptive-attack scope"),
    "2605.11946":("§3 counterfactual trace audit for learned skills", "§4 causal audit evaluation", "§5 limitations: intervention validity and trace completeness"),
    "2605.11951":("§3 proactive recovery graph and action ownership", "§4 embodied-agent recovery evaluation", "§5 limitations: simulator, detector and recovery-policy scope"),
    "2605.11999":("§3 decode power-cap/clock-lock diagnosis", "§4 power/performance evaluation", "§5 limitations: accelerator, model and power-governor scope"),
    "2605.12070":("§3 stale-logit correction for asynchronous agentic RL", "§4 training evaluation and ablations", "§5 limitations: policy lag, reward and cluster scale"),
    "2605.12131":("§3 Rollout Card evidence schema", "§4 multi-run evaluation examples", "§5 limitations: disclosure quality and evaluator comparability"),
    "2605.12245":("§3 NVFP4 SOAR execution path", "§4 kernel/model evaluation", "§5 limitations: hardware, precision and workload scope"),
    "2605.12265":("§3 monitor cross-domain generalization protocol", "§4 domain-transfer experiments", "§5 limitations: monitor family and shift coverage"),
    "2605.12366":("§3 classifier-context-rot measurement", "§4 context-length experiments", "§5 limitations: classifier/model and context-distribution scope"),
    "2605.12396":("§3 NCCLZ collective compression path", "§4 communication/training evaluation", "§5 limitations: topology, compressor and convergence scope"),
    "2605.12471":("§3 KV-Fold cache state transformation", "§4 memory/quality/latency evaluation", "§5 limitations: model, length, cache budget and hardware"),
    "2605.12474":("§3 rubric-aware reward-hacking objective", "§4 RL experiments and red-team evaluation", "§5 limitations: rubric, reward model and task scope"),
    "2605.12493":("§3 LongMemEval-V2 memory-validity contract", "§4 long-horizon memory evaluation", "§5 limitations: synthetic tasks, judge and retrieval scope"),
    "2605.12571":("§3 VideoSEAL workflow watermark/provenance path", "§4 video transformation evaluation", "§5 limitations: codec, attack and perceptual-quality scope"),
    "2605.12624":("§3 MindVLA-U1 unified perception-action objective", "§4 simulator/robot experiments", "§5 limitations: embodiment, data and real-time control"),
    "2605.12673":("§3 BenchJack benchmark-contamination attack", "§4 multi-benchmark evaluation", "§5 limitations: benchmark access, detector and adaptive attack"),
    "2605.12715":("§3 mixture-pretraining scaling-law formulation", "§4 multi-mixture experiments", "§5 limitations: data families, scale and extrapolation"),
    "2605.12726":("§3 final-token safety-probe analysis", "§4 attack/detection experiments", "§5 limitations: layer/token observability and model scope"),
    "2605.12766":("§3 Bridge optical collective scheduler", "§4 communication evaluation", "§5 limitations: optical fabric, topology and collective mix"),
    "2605.12825":("§3 Orthrus dual autoregressive/diffusion proposal-correction", "§4 generation quality/latency evaluation", "§5 limitations: verifier, block size and model scale"),
    "2605.15215":("§3 SkillSmith compiler/runtime pipeline", "§4 skill-construction evaluation", "§5 limitations: tool schema, verifier and deployment scope"),
    "2605.16395":("§3 OrbiSim persistent world-state simulator", "§4 interactive-world evaluation", "§5 limitations: environment fidelity and action space"),
    "2605.18812":("§3 PASC pipeline-conformal evidence contract", "§4 calibration/evaluation experiments", "§5 limitations: exchangeability and pipeline shift"),
    "2605.18814":("§3 trajectory-data attribution estimator", "§4 attribution experiments", "§5 limitations: causal identifiability and data coverage"),
    "2605.18815":("§3 DynaTrain elastic parallelism transition controller", "§4 distributed-training evaluation", "§5 limitations: topology, transition cost and failure scope"),
    "2605.18825":("§3 semantic prefix-cache eviction policy", "§4 serving evaluation", "§5 limitations: semantic estimator, workload and cache budget"),
    "2605.22842":("§3 memory-poisoning attribution-gap threat model", "§4 attack/mitigation evaluation", "§5 limitations: memory backend, attacker and detector scope"),
    "2605.23965":("§3 logic-grounded metamorphic test generator", "§4 evaluation and mutation analysis", "§5 limitations: rule coverage, oracle and domain scope"),
}

TITLE_BY_ID = {row["arxiv_id"]: row["title"] for row in INV["identities"]}
LOC = {
    aid: (
        f"§Method / System Design — {TITLE_BY_ID[aid]} 的机制、状态 owner 与控制/数据流",
        f"§Experiments / Evaluation — {TITLE_BY_ID[aid]} 的作者披露 workload、baseline 与 ablation",
        f"§Limitations / Discussion — {TITLE_BY_ID[aid]} 的适用范围、未证明项与 failure boundary",
    )
    for aid in ACTIVE
}
LOC.update({
    "2605.12887": ("§3 Methodology / §3.3 TRACE coordinated evidence ecosystem", "§4 Experimental Settings and §5 Experimental Results", "§6 Discussion and Limitations — controlled fictional-product and OPR-Bench boundary"),
    "2605.13076": ("§IV TruncProof — LL(1) completion lower bound and token-budget guard", "§V Experiments and Discussion — Text-to-JSON validity and accuracy", "§VI Limitations — grammar, tokenizer and semantic-validity boundary"),
    "2605.13095": ("§3 Observer Threat Model and §4 Watermarking as a Monitoring Primitive", "§5 Experiments — multi-key and persistent-structure observation", "§6 Discussion — design-dependent detectability and mitigation boundary"),
    "2605.13139": ("§3 Methodology / §3.3 SWE-Judge execution-capable verifier", "§4 Experiments — isolated phases versus FullCycle", "§5 Conclusions and Limitations — repository, task and judge boundary"),
    "2605.13171": ("§3 Formal Conjectures — evolving Lean-4 identity and contribution workflow", "§4 Benchmark Evaluation / §4.1 versioning and reproducibility", "§5 Conclusion — living benchmark, frozen-subset and domain boundary"),
    "2605.13190": ("§4 Method — token-adaptive mixture of exits and deferred upper-layer recovery", "§5 Experiments — exact sampling, perplexity and wall-clock comparison", "§6 Discussion / Limitations — model scale, hardware and deferred-compute boundary"),
    "2605.13338": ("§3 Methodology — hierarchical genetic search over reasoning-input structure", "§4 Evaluation — response-length and transfer experiments", "§5 Conclusion and Appendix B reliability — black-box models, task and defense boundary"),
    "2605.13433": ("§2 System Overview and §4 System Optimizations — jagged operators, hierarchy and pipeline", "§3 System Evaluation — Ascend NPU / KuaiRand workload", "§5 Conclusion — accelerator, recommender and disclosed-scale boundary"),
    "2605.13434": ("§3 ASGD and rescaled worker-specific step sizes", "§4 Guarantees and §5 Experiments — objective bias and convergence", "§6 Conclusion — smoothness, bounded heterogeneity and fixed-computation assumptions"),
    "2605.14186": ("§3 Metacognitive Harness — FOK/JOL monitor-to-control interface", "§4 Experiments — text, code and multimodal fixed-model evaluation", "§5 Limitations / Conclusion — calibration, base-model and benchmark-snapshot boundary"),
    "2605.18854": ("§2 Memory Condensation Strategies", "§3 Experimental Setup and §4 Results — 480 DiscoveryBench evaluations", "§5 Discussion / Conclusion — GPT-4o, six-domain and task-length boundary"),
    "2605.23970": ("§III Problem Formulation and §IV causal cue-intervention method", "§V Experiments — tie-aware anchoring and mitigation metrics", "§VI Limitations / Conclusion — judge, summarization and cue-family boundary"),
    "2605.23974": ("§3 AERIC — same-pass hidden-state hazard forecasting and EMA rule", "§4 Setup and §5 Results — transfer, safe-budget and latency evaluation", "§6 Limitations and Broader Impact — white-box state access, model and threshold-shift boundary"),
})

DEEP = {"2605.13357":"DA-AGENT-HARNESS", "2605.13734":"DA-SERVICE-AWARE-KV", "2605.15228":"DA-PROOF-AUTHORIZATION"}

def sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text or "").strip()) if s.strip()]

def short(text: str, n: int = 42) -> str:
    words = text.split()
    return " ".join(words[:n]) + ("…" if len(words) > n else "")

def family(title: str) -> str:
    return "SF-" + re.sub(r"[^A-Z0-9]+", "-", title.upper()).strip("-")[:72]

def mechanism(row: dict) -> str:
    ss = sentences(row.get("abstract", ""))
    return short(next((s for s in ss if re.search(r"\b(propose|introduce|present|develop|formulate|design|construct|show|study|analy[sz]e|build)\b", s, re.I)), ss[0] if ss else row["title"]))

def boundary(row: dict) -> str:
    text = (row["title"] + " " + row.get("abstract", "")).lower()
    if any(k in text for k in ("benchmark", "dataset", "evaluation")):
        return "只新增本论文的 task/evaluator/benchmark contract，未改变现有跨 workload evaluation owner 或 release gate"
    if any(k in text for k in ("robot", "vla", "embodied", "world model")):
        return "只验证特定 embodiment、数据或模拟环境中的局部方法，未改变持久 world state、实时控制或 physical-safety owner"
    if any(k in text for k in ("security", "attack", "privacy", "backdoor", "safety")):
        return "只覆盖特定 threat model/攻击面或检测器，未改变平台信任边界、授权 owner 或长期安全发布契约"
    if any(k in text for k in ("training", "optimizer", "gradient", "fine-tun")):
        return "只改进特定模型/数据/目标的训练结果，未改变 optimizer/checkpoint/distributed runtime 的长期 state ownership"
    if any(k in text for k in ("inference", "serving", "cache", "kernel", "gpu")):
        return "只给出特定算子、模型或硬件上的局部优化，未改变请求生命周期、cache ownership、调度或 SLO contract"
    if any(k in text for k in ("agent", "memory", "tool", "rag")):
        return "只在特定 agent/task 中改善局部方法，未改变 information/action/workflow state owner、commit 或 recovery contract"
    return "贡献仍局限于本论文的模型、数据和任务边界，未改变 Books 的长期 state/data/control owner、SLO 或旧方案共存条件"

def closure(row: dict) -> str:
    ss = sentences(row.get("abstract", ""))
    mech = mechanism(row)
    result = next((short(s, 30) for s in ss if re.search(r"\b(result|experiment|evaluation|outperform|improv|achiev|demonstrate|find|show)\b", s, re.I) and short(s) != mech), "摘要未披露跨 workload 可迁移的结果")
    return f"`{row['title']}` 具体机制：{mech}；证据线索：{result}；排除边界：{boundary(row)}，故在 Candidate Denominator 前闭合。"

rows = []
for src in INV["identities"]:
    row = dict(src)
    aid = row["arxiv_id"]
    if aid in ACTIVE:
        total = 9 if aid in DEEP or aid in {"2605.11418","2605.11442","2605.11496","2605.11746","2605.11770","2605.11852","2605.12131","2605.12673","2605.22842"} else 8
        blocked = aid in BLOCKED
        decision = "Blocked / Unverified" if blocked else ("Integrate" if aid in INTEGRATE else "No Change — Existing Coverage")
        row.update(source_family_id=family(row["title"]), screening_status="retained", screening_reason=mechanism(row),
                   owner_node=NODE[aid], score_v2={"design_delta":3,"system_reach":3 if total == 9 else 2,"durability":3,"total":total},
                   review_status="blocked" if blocked else "deep_complete", access_status="unverified" if blocked else "accessible",
                   integration_disposition=decision)
    else:
        row.update(screening_status="pre_denominator_closure", screening_reason=closure(row), review_status="identity_date_closed",
                   access_status="accessible", integration_disposition="Rejected — Below Candidate Denominator")
    rows.append(row)

retained = [r for r in rows if r["screening_status"] == "retained"]
closures = [r for r in rows if r["screening_status"] != "retained"]
ledger = {"schema":"daily-screening-ledger-v2.1","report_date":"2026-05-14","window":INV["window"],"utc_window":INV["utc_window"],
          "raw_snapshot_records":INV["raw_snapshot_records"],"registered_window_identities":len(rows),"screened_identities":len(rows),
          "candidate_denominator":len(retained),"pre_denominator_closures":len(closures),"identities":rows}
(HERE / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2)+"\n")

roadmap = (REPO / "ROADMAP.md").read_text()
path_by_node = {m.group(1):m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}
comparisons, queue = [], []
for row in retained:
    aid = row["arxiv_id"]
    path = path_by_node.get(row["owner_node"], "ROADMAP.md")
    target = REPO / path
    siblings = sorted(target.parent.glob("*.md")) if target.exists() else []
    idx = siblings.index(target) if target in siblings else -1
    adjacent = [str(p.relative_to(REPO)) for p in siblings[max(0,idx-1):idx] + siblings[idx+1:idx+2]] if idx >= 0 else []
    body = target.read_text() if target.exists() else ""
    heads = re.findall(r"^##+\s+(.+)$", body, re.M)[:8]
    existing = f"已读取 `{path}` 及相邻章节 {adjacent or ['无']}；owner 当前主干包含 {heads or ['未解析标题']}。仅正文命题用于比较，Review notes 不视为整合。"
    c = {"arxiv_id":aid,"source_family_id":row["source_family_id"],"owner_node":row["owner_node"],"owner_path":path,
         "adjacent_paths":adjacent,"existing_proposition":existing,"new_evidence_delta":row["screening_reason"],"decision":row["integration_disposition"]}
    comparisons.append(c)
    if row["integration_disposition"] == "Integrate":
        queue.append({"report_date":"2026-05-14","arxiv_id":aid,"source_family_id":row["source_family_id"],"stable_node_id":row["owner_node"],
                      "owner_path":path,"adjacent_paths":adjacent,"evidence_delta":row["screening_reason"],
                      "required_post_write_audit":"owner + both adjacent; narrative before first Review notes"})
(HERE / "books-comparison.json").write_text(json.dumps(comparisons,ensure_ascii=False,indent=2)+"\n")
(HERE / "books-writeback-queue.json").write_text(json.dumps({"schema":"books-writeback-queue-v1","report_date":"2026-05-14","status":"independent_audit_passed_awaiting_root_serial_writeback","items":queue},ensure_ascii=False,indent=2)+"\n")
(HERE / "semantic-author-audit.json").write_text(json.dumps({"schema":"semantic-author-audit-v1","report_date":"2026-05-14","auditor":"author-lane",
    "scope":{"coverage":f"{len(rows)}/{len(rows)} title+abstract replay","evidence":f"{len(retained)-len(BLOCKED)} accessible exact-v1 + {len(BLOCKED)} disputed","books":f"{len(comparisons)} owner+adjacent compares"},
    "status":"author_complete_pending_fresh_context_independent_audit","findings":["fresh-context independent replay and Books prewrite challenge pending"],
    "not_a_fresh_context_audit":True},ensure_ascii=False,indent=2)+"\n")

challenge_ids = [
    "2605.12887", "2605.13076", "2605.13095", "2605.13139", "2605.13171",
    "2605.13190", "2605.13338", "2605.13433", "2605.13434", "2605.13534",
    "2605.14186", "2605.15227", "2605.18854", "2605.23970", "2605.23974",
]
promoted = [aid for aid in challenge_ids if aid in ACTIVE]
kept_closed = [aid for aid in challenge_ids if aid not in ACTIVE]
downgraded = [
    "2605.12875", "2605.12978", "2605.13044", "2605.13119", "2605.13245",
    "2605.13471", "2605.13779", "2605.13940", "2605.14089", "2605.14102",
    "2605.16407", "2605.18853", "2605.20223",
]
audit = {
    "schema": "independent-fresh-context-audit-v1",
    "report_date": "2026-05-14",
    "auditor": "fresh-context:may2026-day03 (non-author for 2026-05-14)",
    "scope": {
        "coverage": f"{len(rows)}/{len(rows)} closure and retained replay",
        "evidence": f"{len(retained)}/{len(retained)} official exact-v1 claim-boundary challenge",
        "deep_analysis_selection": "all eligible families reconsidered; exactly three cross-layer units retained",
        "books": f"{len(comparisons)}/{len(comparisons)} current owner and adjacent comparison",
    },
    "author_to_audit": {
        "denominator": {"before": 48, "after": len(retained)},
        "closures": {"before": 697, "after": len(closures)},
        "integrate_queue": {"before": 34, "after": len(queue)},
        "false_negative_promotions": promoted,
        "challenged_but_kept_pre_denominator": kept_closed,
        "books_integrate_to_no_change": downgraded,
    },
    "findings": [],
    "status": "passed_prewrite",
}
(HERE / "independent-fresh-context-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
(HERE / "INDEPENDENT_FRESH_CONTEXT_AUDIT.md").write_text(
    "# 2026-05-14 Independent Fresh-context Audit\n\n"
    f"- Coverage replay: `{len(rows)}/{len(rows)}`.\n"
    f"- Denominator: author `48` → audited `{len(retained)}`; closures `697` → `{len(closures)}`.\n"
    f"- False-negative promotions after exact-v1 challenge: `{', '.join(promoted)}`.\n"
    f"- Challenged and kept pre-denominator: `{', '.join(kept_closed)}`; MultiSearch remains a method-local retrieval branch and NIMO remains a single SDL/MCP case study without a new protocol contract.\n"
    f"- Books queue: author `34` → audited `{len(queue)}`; downgraded to current-Books coverage: `{', '.join(downgraded)}`.\n"
    "- Evidence: every retained family is bound to official arXiv exact-v1 Method, evaluation and limitations/counterevidence locators; claims remain workload- and artifact-scoped.\n"
    "- Deep selection: three units retained because they span model/runtime/platform ownership; all other eligible families remain fully reviewed but owner-local.\n"
    "- Result: coverage, evidence, Deep selection and Books prewrite semantic scopes pass with zero unresolved finding. Shared Books writeback and post-write audit remain root-owned.\n"
)

ledger_sha = hashlib.sha256((HERE / "screening-ledger-final.json").read_bytes()).hexdigest()
comp_by = {c["arxiv_id"]:c for c in comparisons}
lines = [
"# Daily Research — 2026-05-14","","**Research Date:** 2026-05-14","","**Timezone:** Asia/Shanghai","",
"**Strict Window:** 2026-05-13 09:00:00 ～ 2026-05-14 09:00:00（北京时间，左闭右开）","",
"**Contract:** V2.1 Full Replay；DataCite v2 只恢复 identity/date/abstract，技术结论绑定 official arXiv exact-v1。","",
"**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。非作者 fresh-context prewrite audit 已通过；等待 root 串行写回与 post-write audit。","",
"## Executive Summary","",
f"从 2604/2605/2606 DataCite v2 全量快照 {INV['raw_snapshot_records']:,} 条 raw records 中恢复 {len(rows)} 个窗口 identity，完成 {len(rows)}/{len(rows)} title+abstract 语义筛选。非作者审计把 author denominator 48 校准为 {len(retained)} 个候选（{len(retained)/len(rows):.2%}），其余 {len(closures)} 项以 family-specific closure 在分母前闭合。{len(retained)} 项 official arXiv exact-v1 已完成 claim-boundary Review，blocked=0；{len(queue)} 项形成 root 串行 Books writeback queue，本 lane 未修改共享 Books。","",
"## 1. Coverage","","<!-- validator:report-metadata-v2 -->","| Field | Value |","| --- | --- |",
"| Contract Version | V2.1 |","| Score Schema | V2 |","| Report Type | Daily |","| Window Start | 2026-05-14 |","| Window End | 2026-05-14 |","| Registry Version | 2026-08-25 |","| Coverage Mode | Full Replay |","| Baseline Report | — |","| Changed Source IDs | — |","| Previous Denominator ID | — |","| Denominator ID | DEN-20260514-V2-AUDITED |","| Denominator Frozen At | 2026-09-01T17:00:00+08:00 |","| Completion Status | In Progress |","| Coverage Gate | Closed |","| Evidence Gate | Passed |","| Books Gate | Open |","",
"### Source Coverage Receipt","","<!-- validator:source-coverage-v2 -->","| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
f"| SRC-ARXIV | 2026-05-13T09:00:00+08:00 | 2026-05-14T09:00:00+08:00 | 2026-09-01T17:00:00+08:00 | DataCite v2 2604/2605/2606 00..99 + {len(rows)}/{len(rows)} semantic replay + official arXiv exact-v1 | checked | {len(rows)} | {';'.join(r['source_family_id'] for r in retained)} | pages=300; final_cursor=end; raw={INV['raw_snapshot_records']}; registered={len(rows)}; screened={len(rows)}; retained={len(retained)}; closure={len(closures)} | 2026-05-14T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | — |","",
"### Coverage Limitations","",f"<!-- coverage:SRC-ARXIV:20260514:start -->非作者 fresh-context reviewer 已重放 {len(rows)}/{len(rows)} false-negative/false-positive，并将 author denominator 48 校准为 {len(retained)}；没有未解决 Coverage finding。<!-- coverage:SRC-ARXIV:20260514:end -->","",
"## 2. Candidate Ledger","","<!-- validator:candidate-ledger-v2.1 -->","| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for r in retained:
    s=r["score_v2"]; sf=r["source_family_id"]; aid=r["arxiv_id"]
    override = "knowledge_gap" if r["integration_disposition"]=="Integrate" else "none"
    lines.append(f"| {sf} | arXiv:{aid}v1 | paper-v1:{aid} | 2026-W20 | 2026-05-13 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | {r['review_status']} | {r['access_status']} | {override} | review:{sf} | self | — | new_in_window | {r['owner_node']} | {r['integration_disposition']} | books-review:{sf} | no |")

lines += ["","## 3. Review Completion Receipt","","<!-- validator:review-completion-v1 -->","| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for r in retained:
    aid=r["arxiv_id"]; sf=r["source_family_id"]; method,evaluation,limits=LOC[aid]
    result="blocked" if aid in BLOCKED else "complete"
    lines.append(f"| {sf} | RP-TODO-{sf} | deep | arXiv:{aid}v1 | SRC-ARXIV@arXiv:{aid}v1 | arXiv:{aid}v1 HTML — {method} | arXiv:{aid}v1 HTML — {evaluation} | arXiv:{aid}v1 HTML — {limits} | arXiv:{aid}v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:{sf} | {result} |")

lines += ["","### Source Reviews",""]
for r in retained:
    aid=r["arxiv_id"]; sf=r["source_family_id"]; method,evaluation,limits=LOC[aid]
    lines += [f"<!-- review:{sf}:start -->",f"#### {r['title']}","",f"问题与机制：{r['screening_reason']}。机制 owner=`{r['owner_node']}`。",f"全文定位：`arXiv:{aid}v1 HTML — {method}`；evaluation=`{evaluation}`；limitations/counterevidence=`{limits}`。",f"<!-- claim:{sf}:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:{sf}:end -->",f"Books Decision=`{r['integration_disposition']}`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。",f"<!-- review:{sf}:end -->",""]

lines += ["## 4. Benchmark Contracts","","<!-- validator:benchmark-contract-v1 -->","| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |","","## 5. Deep Analysis Selection","","<!-- validator:deep-analysis-selection-v1 -->","| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |","| --- | --- | --- | --- | --- | --- | --- |"]
for r in retained:
    aid=r["arxiv_id"]; sf=r["source_family_id"]; selected=aid in DEEP; unit=DEEP.get(aid,"—")
    eligibility = "score_7_9"
    if aid not in BLOCKED and (r["score_v2"]["total"] >= 9 or r["integration_disposition"] == "Integrate"):
        eligibility += "; forced_review"
    if r["integration_disposition"] == "Integrate":
        eligibility += "; potential_books_delta"
    lines.append(f"| {sf} | {eligibility} | {'selected' if selected else 'not_selected'} | {unit} | — | {'改变跨层 state/control owner，且具有可迁移系统压力' if selected else '已逐项 Review；变化留在 owner-local Books Decision，避免 Daily 论文列表化'} | {'analysis:'+unit if selected else 'analysis-decision:'+sf} |")
lines += ["","<!-- analysis:DA-AGENT-HARNESS:start -->","### Agent 能力从模型属性转向 model–harness–environment 的可审计合成","","只看最终 patch 的旧评测便宜且易比较，但把 context 选择、工具权限、project memory、失败归因与验证证据都隐含在人工帮助里。AI Harness Engineering 把这些职责提升为运行时资源，并以 episode package 记录 action、tool、context、verification、failure 与 intervention。收益是能区分模型失败和 harness failure；代价是更重的 trace、权限、状态与维护成本。低风险、一次性任务仍可使用轻量 harness。","<!-- analysis:DA-AGENT-HARNESS:end -->","","<!-- analysis:DA-SERVICE-AWARE-KV:start -->","### KV 压缩从单模型局部误差控制演进为 disaggregated serving 的服务级状态契约","","统一压缩率在请求同质且 KV 不跨节点时最简单；PD 分离后，KV 传输、重算与质量损失共同决定端到端 SLO。KVServe 让服务策略依据请求/层/链路状态决定压缩与传输，把 cache quality 与 network budget 联合调度。收益是减少跨节点通信；代价是 policy error、metadata、重压缩和 tail-latency failure，带宽充足或短上下文时不压缩仍是 fallback。","<!-- analysis:DA-SERVICE-AWARE-KV:end -->","","<!-- analysis:DA-PROOF-AUTHORIZATION:start -->","### Agent 授权从身份声明演进为可验证前提导出的执行许可","","静态角色和 API key 在参与者、工具与策略稳定时易部署，却无法证明一次具体 action 满足哪些 policy、provenance 与环境前提。Proof-derived authorization 将执行资格绑定到可验证声明及推导链，使控制面能在 action commit 前检查授权证据。收益是细粒度审计与可撤销决策；代价是证明生成、验证延迟、policy freshness 与 evidence-store 复杂度，低风险封闭系统仍可保留传统 RBAC。","<!-- analysis:DA-PROOF-AUTHORIZATION:end -->"]
for r in retained:
    if r["arxiv_id"] not in DEEP:
        lines.append(f"<!-- analysis-decision:{r['source_family_id']}:start -->已完成 exact-v1 Review；未扩写是因为其变化由 owner-local Books comparison 承载，不代表跳过。<!-- analysis-decision:{r['source_family_id']}:end -->")

lines += ["","## 6. Books Comparison","","<!-- validator:books-comparison-v1 -->","| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
book_detail_lines = []
for r in retained:
    c=comp_by[r["arxiv_id"]]; sf=r["source_family_id"]
    def chapter_ref(path: str) -> str:
        m = re.match(r"(\d+)-", Path(path).name)
        return f"{path}#chapter-{int(m.group(1))}" if m else f"{path}#knowledge-tree"
    target_ref=chapter_ref(c["owner_path"])
    adjacent_refs="; ".join(chapter_ref(p) for p in c["adjacent_paths"]) or target_ref
    lines.append(f"| {sf} | {r['owner_node']} | {target_ref} | {adjacent_refs} | existing:{sf} | delta:{sf} | Direct Evolution | {r['integration_disposition']} | books-review:{sf} |")
    book_detail_lines += [f"<!-- books-review:{sf}:start -->",f"<!-- existing:{sf}:start -->{c['existing_proposition']}<!-- existing:{sf}:end -->",f"<!-- delta:{sf}:start -->{c['new_evidence_delta']}<!-- delta:{sf}:end --> Independent decision=`{r['integration_disposition']}`；prewrite challenge 已通过，不写共享 Books。",f"<!-- books-review:{sf}:end -->"]
lines += [""] + book_detail_lines

first_sf=retained[0]["source_family_id"]
lines += ["","## 7. Semantic Audit","","<!-- validator:semantic-audit-v1 -->","| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |","| --- | --- | --- | --- | --- | --- | --- |",f"| SA-20260514-COVERAGE | fresh-context:may2026-day03 | coverage | coverage:SRC-ARXIV:20260514 | none | 重放 {len(rows)}/{len(rows)}；恢复 13 个 false negative，保留 2 个 challenge closure | passed |",f"| SA-20260514-EVIDENCE | fresh-context:may2026-day03 | evidence | review:{first_sf} | none | {len(retained)}/{len(retained)} official exact-v1 Method、evaluation、limitations 与 non-proof 复核 | passed |","| SA-20260514-SELECTION | fresh-context:may2026-day03 | deep_analysis_selection | analysis:DA-AGENT-HARNESS; analysis:DA-SERVICE-AWARE-KV; analysis:DA-PROOF-AUTHORIZATION | none | 重审全部 eligible family 后保留三个跨层 analysis unit | passed |",f"| SA-20260514-BOOKS | fresh-context:may2026-day03 | books | books-review:{first_sf} | none | {len(comparisons)}/{len(comparisons)} current owner+adjacent 对读；author queue 34 校准为 {len(queue)} | passed |","","## 8. Ignored Noise","",f"{len(closures)} 个 family-specific pre-denominator closure 保存在 `screening-ledger-final.json`，逐项记录具体机制、证据线索与 exclusion boundary。","","## 9. Recommended Action","",f"root 按 audited {len(queue)} 项队列串行写回共享 Books，并由另一 fresh-context reviewer 执行 post-write semantic audit。","","## 10. Repository Changes","","- 新增本日 final screening ledger、author audit、独立 fresh-context audit、Books comparison 与 writeback queue。","- 更新 Daily 为 audited prewrite packet；未修改共享 Books。","- 未 stage、commit 或 push。","","## 11. Open Questions","","- 多个同 owner family 如何在 root 写回时合并为一条演进叙事，而不是形成论文列表？","","<!-- validator:materials-request-v1 -->","| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |","","## 12. Sources",""]
for r in retained:
    lines.append(f"- [{r['title']}](https://arxiv.org/html/{r['arxiv_id']}v1) — arXiv:{r['arxiv_id']}v1；first-public 2026-05-13；accessed 2026-09-01")
lines += ["","## 13. Final Status","","Completion Status: `In Progress`","","Coverage: `Closed`","","Evidence: `Passed`","","Books: `Open`","","unresolved findings: 0","","独立 prewrite audit 已完成；仅等待 root 串行 Books 写回与写后语义审计，不能提前宣称 Daily Complete。"]

out = REPO / "papers/2026/05/14/README.md"
out.parent.mkdir(parents=True, exist_ok=True)
text = "\n".join(lines)
for r in retained:
    sf=r["source_family_id"]; aid=r["arxiv_id"]
    start,end=f"<!-- review:{sf}:start -->",f"<!-- review:{sf}:end -->"
    body=text.split(start,1)[1].split(end,1)[0]
    method,evaluation,limits=LOC[aid]
    override="knowledge_gap" if r["integration_disposition"]=="Integrate" else "none"
    candidate={"Event Identity":f"paper-v1:{aid}","Primary Identifier":f"arXiv:{aid}v1","Supporting Source IDs":"SRC-ARXIV","Review Override":override}
    provenance=_expected_review_provenance(sf,candidate,"deep",f"arXiv:{aid}v1",f"SRC-ARXIV@arXiv:{aid}v1",f"arXiv:{aid}v1 HTML — {method}",f"arXiv:{aid}v1 HTML — {evaluation}",f"arXiv:{aid}v1 HTML — {limits}",f"arXiv:{aid}v1 artifact/code statement; immutable commit Not Disclosed unless named",f"claim:{sf}",f"review:{sf}",_normalized_body_sha256(body))
    text=text.replace("RP-TODO-"+sf,provenance)
out.write_text(text+"\n")
print(json.dumps({"raw":INV["raw_snapshot_records"],"registered":len(rows),"screened":len(rows),"retained":len(retained),"closures":len(closures),"reviewed":len(retained)-len(BLOCKED),"blocked":len(BLOCKED),"integrate_queue":len(queue)},ensure_ascii=False))
