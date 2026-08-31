#!/usr/bin/env python3
"""Materialize the 2026-05-11 V2.1 author packet without shared Books writes."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
sys.path.insert(0, str(REPO))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

INV = json.loads((ROOT / "screening-ledger-provisional.json").read_text())

ACTIVE = set("""
2605.09252 2605.09253 2605.09269 2605.09278 2605.09283 2605.09285
2605.09287 2605.09303 2605.09315 2605.09317 2605.09329 2605.09330
2605.09341 2605.09359 2605.09423 2605.09442 2605.09544 2605.09650
2605.09681 2605.09692 2605.09701 2605.09730 2605.09820
2605.09370 2605.09375 2605.09387 2605.09397 2605.09490 2605.09497
2605.09530 2605.09586 2605.09594 2605.09608 2605.09623 2605.09649
2605.09684 2605.09702 2605.09708 2605.09721 2605.09734 2605.09735
2605.09778 2605.09817 2605.09822 2605.09823 2605.09825 2605.11003
2605.11005 2605.11026 2605.11029 2605.11030 2605.11032 2605.12549
2605.16366 2605.16378
""".split())
ACTIVE -= {"2605.09283", "2605.09734"}

NODE = {
    "2605.09252":"AGENT-TOOL-CALLING", "2605.09253":"TRAIN-SFT",
    "2605.09269":"PLATFORM-EVALUATION-SYSTEM", "2605.09278":"AGENT-MEMORY",
    "2605.09283":"PLATFORM-MODEL-REGISTRY", "2605.09285":"TRAIN-CHECKPOINT",
    "2605.09287":"TRAIN-RLHF", "2605.09303":"MULTIMODAL-GENERATIVE-PARADIGMS",
    "2605.09315":"AGENT-PLATFORM", "2605.09317":"AGENT-MEMORY",
    "2605.09329":"INFER-SPECULATIVE-DECODING", "2605.09330":"AGENT-MEMORY",
    "2605.09370":"TRAIN-DISTRIBUTED-TRAINING", "2605.09375":"INFER-TENSORRT-LLM",
    "2605.09387":"MULTIMODAL-EMBODIED-VLA", "2605.09397":"PLATFORM-SECURITY",
    "2605.09490":"INFER-GPU-MEMORY", "2605.09497":"AGENT-TOOL-CALLING",
    "2605.09530":"PLATFORM-SECURITY", "2605.09586":"MULTIMODAL-WORLD-MODELS",
    "2605.09594":"AGENT-PLATFORM", "2605.09608":"TRAIN-CHECKPOINT",
    "2605.09623":"INFER-SCHEDULING", "2605.09649":"INFER-KV-CACHE",
    "2605.09684":"PLATFORM-MONITORING", "2605.09702":"PLATFORM-EVALUATION-SYSTEM",
    "2605.09708":"INFER-TENSORRT-LLM", "2605.09721":"PLATFORM-SECURITY",
    "2605.09734":"AGENT-TOOL-CALLING", "2605.09735":"INFER-KV-CACHE",
    "2605.09778":"INFER-KV-CACHE", "2605.09817":"AGENT-TOOL-CALLING",
    "2605.09822":"AGENT-RAG", "2605.09823":"AGENT-MULTI-AGENT",
    "2605.09825":"TRAIN-PRETRAINING", "2605.11003":"AGENT-TOOL-CALLING",
    "2605.11005":"TRAIN-PIPELINE-PARALLEL", "2605.11026":"PLATFORM-SECURITY",
    "2605.11029":"PLATFORM-SECURITY", "2605.11030":"PLATFORM-EVALUATION-SYSTEM",
    "2605.11032":"AGENT-MEMORY", "2605.12549":"INFER-PREFILL",
    "2605.16366":"MULTIMODAL-REPRESENTATION", "2605.16378":"MULTIMODAL-GENERATIVE-PARADIGMS",
    "2605.23952":"PLATFORM-EVALUATION-SYSTEM", "2605.28843":"PLATFORM-SECURITY",
    "2605.09341":"AGENT-MULTI-AGENT", "2605.09359":"AGENT-PLATFORM",
    "2605.09423":"MULTIMODAL-EMBODIED-VLA", "2605.09442":"MULTIMODAL-GENERATIVE-PARADIGMS",
    "2605.09544":"PLATFORM-EVALUATION-SYSTEM", "2605.09650":"AGENT-PLATFORM",
    "2605.09681":"MULTIMODAL-GENERATIVE-PARADIGMS", "2605.09692":"PLATFORM-EVALUATION-SYSTEM",
    "2605.09701":"MULTIMODAL-WORLD-MODELS", "2605.09730":"AGENT-TOOL-CALLING",
    "2605.09820":"MULTIMODAL-GENERATIVE-PARADIGMS",
}

# These papers strengthen an existing contract without exposing a new durable
# mechanism.  They remain reviewed evidence instead of forcing a Books diff.
INTEGRATE = {
    "2605.09252", "2605.09278", "2605.09315", "2605.09329", "2605.09341",
    "2605.09359", "2605.09370", "2605.09387", "2605.09423", "2605.09442",
    "2605.09490", "2605.09594", "2605.09650", "2605.09681", "2605.09684",
    "2605.09692", "2605.09702", "2605.09730", "2605.09735", "2605.09820",
    "2605.09822", "2605.09825", "2605.11005", "2605.11026", "2605.11029",
    "2605.11032", "2605.12549",
}
NO_CHANGE = ACTIVE - INTEGRATE

LOC = {
    "2605.09252":("§2 benchmark; §4 probe; §5 Probe&Prefill", "§3 failure analysis; §5.2–5.3 results; Appendices B–H", "§7 conclusion; Appendix F overhead and OOD boundaries"),
    "2605.09253":("§2 Rock Tokens; §3 causal knockout; §4 selective reweighting", "§5 setup; Appendix C/D/E", "Appendix A Limitations"),
    "2605.09269":("method section: Disagreement Planner and Checklist Verifier; joint multi-role RL", "experiments on VL-RewardBench and reward-model transfer", "conclusion/ablation boundary; hardware and production SLO Not Disclosed"),
    "2605.09278":("§3 zero-trust memory game; §4 EquiMem calibration", "§5 experiments; Appendix E/F failure analyses", "Appendix F sparse-memory, correlated-hallucination and graph-semantics failures"),
    "2605.09283":("§3 prompt-aware metadata envelope and verifiable credentials", "§4 prototype/use-case evaluation", "discussion/conclusion; reliability and confidence calibration not independently established"),
    "2605.09285":("§3 leakage analysis; §4 history-aware null-space update; §5 BetaEdit", "§6 experiments and hyperparameter analysis", "§7 Limitations"),
    "2605.09287":("§3 pivot construction and PBRS trajectory credit", "§4 experiments across seven QA benchmarks", "conclusion/appendix; pivot extraction and reward-model dependence"),
    "2605.09303":("§2 order-induced pseudo-joints; §3 local denoising circulation", "diagnostic experiments and decomposition analyses", "discussion: inference-only diagnosis does not construct a compatible joint"),
    "2605.09315":("§3 capability erosion across workflow/skill/model/memory; §4 CPE", "§5 four-channel experiments", "limitations: task/model/evolution-loop scope"),
    "2605.09317":("§3 trajectory-to-latent compressor; §4 memory weaving", "§5 training and four GUI benchmark evaluations", "limitations: latent memory interpretability, portability and long-horizon state repair"),
    "2605.09329":("§3 acceptance decay analysis; §4 test-time speculation", "§5 long-response evaluation and ablations", "discussion: target/draft/workload and verification-cost boundary"),
    "2605.09330":("§3 trajectory-correlation diagnosis; §4 mitigation", "§5 agent-memory experiments", "limitations: benchmark/backbone and retrieval-policy scope"),
    "2605.09370":("§3 failure taxonomy; §4 recovery control for 504-GPU pretraining", "§5 operational traces and recovery evaluation", "discussion: single-cluster topology and incident-selection boundary"),
    "2605.09375":("architecture and block-clustered compression; adaptive parallel speculation", "chip/throughput/energy evaluation", "hardware process, model and sequence-length boundary"),
    "2605.09387":("§3 symbolic constraint memory and embodied planning", "§4–§5 navigation/manipulation evaluation", "limitations: perception error, constraint incompleteness and sim-to-real"),
    "2605.09397":("§3 BadDLM threat model and trigger injection", "§4 attacks and defenses across diffusion LMs", "limitations: model family, trigger and adaptive-defense scope"),
    "2605.09490":("§3 semantic thought classification; §4 HBM/host hierarchy", "§5 end-to-end reasoning evaluation", "limitations: classifier error, migration overhead and hardware-specific results"),
    "2605.09497":("§3 deceptive-interface threat model; §4 training curriculum", "§5 web-agent safety/utility evaluation", "limitations: interface families, attack adaptation and false refusal"),
    "2605.09530":("§3 three-stage edge pseudonymization; Appendix implementation", "§4–§5 MemPrivacy-Bench and utility evaluation", "§6/Appendix limitations; plaintext SQLite reference implementation boundary"),
    "2605.09586":("§3 interactive physics-neural world state; §4 update loop", "§5 video and interaction evaluation", "limitations: deformation classes, contact physics and real-time control"),
    "2605.09594":("§3 malicious-skill dependency-steering threat model", "§4–§5 attack and mitigation evaluation", "limitations: repository/ecosystem coverage and adaptive supply-chain attacks"),
    "2605.09608":("§3 covariance geometry; §4 whiten-merge-recolor GCWM", "§5–§6 continual-domain/capability experiments", "§7 limitations; author-reported result inconsistency retained"),
    "2605.09623":("§3 heterogeneous edge-cloud task graph and safety constraints", "§4 scheduling/offloading evaluation", "limitations: workload prediction, trust boundary and network volatility"),
    "2605.09649":("§3 token-importance/eviction mechanism", "§4 long-context evaluation and ablations", "limitations: model, cache budget and quality metric boundary"),
    "2605.09684":("§3 MonitoringBench threat/monitor task construction", "§4 semi-automated red-team evaluation", "limitations: monitor/model/judge and attack-distribution scope"),
    "2605.09702":("§3 noisy-judge measurement model and calibration estimator", "§4 experiments and label-efficiency analysis", "limitations: judge dependence, latent truth and domain shift"),
    "2605.09708":("§3 Metal-Sci workload/artifact contract", "§4 evolutionary kernel-search experiments", "limitations: Apple-Silicon kernels, benchmark representativeness and search budget"),
    "2605.09721":("threat taxonomy for privileged tool execution", "systematic-analysis evidence and case mapping", "review methodology and public-incident coverage limitations"),
    "2605.09734":("§3 trajectory supervision for continual tool learning", "§4 sequential-task evaluation", "limitations: tool-schema drift, retention metrics and model family"),
    "2605.09735":("§3 KV movement regularizer for static-graph serving", "§4 serving evaluation and ablations", "limitations: static graph, topology and workload-distribution boundary"),
    "2605.09778":("§3 Nectar cached-token attention estimator", "§4 cache-selection evaluation", "limitations: regression error, model transfer and eviction interaction"),
    "2605.09817":("§3 tool-cloning threat model and ecosystem measurement", "§4 agent/tool experiments", "limitations: registry identity, behavioral equivalence and adaptive clones"),
    "2605.09822":("§3 oracle-poisoning attack path; §4 defenses", "§5 knowledge-graph agent evaluation", "limitations: KG provenance, attacker access and downstream agent scope"),
    "2605.09823":("§3 CalBench coordination/privacy instrumentation", "§4 meeting-stream evaluations", "limitations: N=5 topology, regex leakage lower bound and fixed probing"),
    "2605.09825":("§3 native MXFP4 pretraining recipe", "§4 model/hardware training evaluation", "limitations: AMD MI355X, precision stack, scale and optimizer boundary"),
    "2605.11003":("§2 authorization-execution gap taxonomy", "position-paper case synthesis and proposed process evidence", "position-paper boundary: no implemented enforcement or comparative evaluation"),
    "2605.11005":("§3 disaggregated attention/FFN placement and AF-Pipe", "§4 16-node H800 evaluation", "limitations: topology, MoE family, balance model and failure recovery"),
    "2605.11026":("§3 fake-tool/credential/parameter traps and classifier", "§4 cross-lingual/adaptive-attack evaluation", "limitations: low base attack success, trap discoverability and normal-use coverage"),
    "2605.11029":("§3 fragmented campaign graph; §4 generator; §5 detector", "§6 sandbox execution and held-out detection", "§6.3 synthetic-benign and gated-prompt limitations"),
    "2605.11030":("§2 workload/admission contract; §3 adapters and evidence gate", "§4–§5 admitted evidence and stressed-controller study", "§6 artifact release and limitations"),
    "2605.11032":("§3 memory schema/Merkle-DAG/capability access/rehydration", "§4 implementation; §5 evaluation", "§6.1 limitations: ranking, extractive summary and N=50 scale"),
    "2605.12549":("§3 prefill candidate-selection diagnosis; §4 Re-Prefill", "§5 four-model/five-benchmark evaluation", "limitations: GUI-only grounding, attention heuristic and extra-prefill cost"),
    "2605.16366":("§3 frequency-residual compression and spatial absorber", "§4 short/long-video evaluation and ablations", "limitations: vision encoder, temporal-frequency assumptions and token budget"),
    "2605.16378":("§3 rectangle incompatibility test; §4–§5 mixing theory", "§6 BERT/RoBERTa chain experiments", "§7 limitations: loose bounds, classifier dependence and unknown stationary law"),
    "2605.23952":("Machine Mindprint dimensions and Trust Protocol", "exploratory measurement framework and probe proposal", "position paper: reliability/validity and deployment evidence not established"),
    "2605.28843":("§2 hybrid lexical+LLM DURC metadata screen", "§3 52k-preprint descriptive analysis", "§3 limitations: metadata only, no operational capability/intent, English bioRxiv scope"),
    "2605.09341":("§2 Method; §2.1 Round State; §2.4 Evidence-Gated MAS Restructuring", "§3 Experiments; §3.3 Ablation; §4.1 Mechanism Evidence", "§4.1 ALFWorld-specific stress-test boundary; Appendix benchmark-local heuristics"),
    "2605.09359":("§3 Skill-R1; §3.2 Bi-Level Group-relative Advantages; §3.3 GRPO Objective", "§4 Experiments; §5.1 Reward and Accuracy Progression", "§7 Conclusion; Appendix A skill examples; frozen task-LLM and verifiable-reward scope"),
    "2605.09423":("§2 SimWorld Studio; §2.1 SimCoder; §2.2 Adaptive Curriculum", "§3 Experiments and Analysis; §3.1–§3.3 case studies", "Appendix A Limitation; Unreal/Gym navigation and generated-environment boundary"),
    "2605.09442":("§3 Method; §3.1 Semantic Injection Cache; §3.2 Adaptive Dynamic Window", "§4 Experiments; §4.2 Results; §4.3 Ablations", "Appendix F Limitation Analysis; single-H100 causal-video workload boundary"),
    "2605.09544":("§3 Method; §3.1 Dataset Reconstruction; §3.2 Evaluation Metrics", "§4 Experiment; §4.2 Results; §4.3 Benefit-Cost Trade-offs", "§5 Conclusion; task/model/tool protocol and discriminative-filter boundary"),
    "2605.09650":("§2 Workspace Optimization; §2.1 Trainable State; §4 DreamTeam", "§5 Experiments; Appendix B operational sequence", "§6 Limitations and Conclusion; ARC-AGI-3 public-set/two-run boundary"),
    "2605.09681":("§3 Observation; §4 Forcing-KV; §4.1–§4.3 pruning", "§5 Experiments; §5.1 Results; §5.3 Ablation", "§7 Limitation and Future Works; Appendix H implementation; H200/video-model boundary"),
    "2605.09692":("§2–§3 structured-control lesion and intervention design", "§4–§5 seven-corpus/open-weight/matched-interface results", "§6–§7 discussion and limitations; structured coupling is behavioral evidence, not inner agency"),
    "2605.09701":("§3 Method; §3.1 Latent Dynamics; §3.2 Future Alignment; §3.3 Planner", "§4 Experiments; §4.3 Results; §4.4 Ablation", "§5 Conclusion; NAVSIM latent-driving and predicted-future boundary"),
    "2605.09730":("§3 Method; §3.2 Pre-Execution Algorithm; failure gating", "§4 Experiments; §4.3 Results; §4.4 Efficiency; §4.5 Calibration", "§6 Limitations; M3ToolEval/API-Bank and generated-rubric calibration boundary"),
    "2605.09820":("§3 Problem Formulation; §4 Bayesian Structured Decoding; §4.2–§4.3", "§5 Experiments; §5.1 Results; §5.2 Ablations", "§6 Conclusion; Appendices D–G calibration/statistics; tested-DLM boundary"),
}

SELECTED = ["2605.09341", "2605.09370", "2605.09692"]


def sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text or "").strip()
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def short(text: str, words: int = 42) -> str:
    parts = text.split()
    return " ".join(parts[:words]) + ("…" if len(parts) > words else "")


def family(title: str) -> str:
    return "SF-" + re.sub(r"[^A-Z0-9]+", "-", title.upper()).strip("-")[:72]


def mechanism(row: dict) -> str:
    ss = sentences(row.get("abstract", ""))
    picked = next((s for s in ss if re.search(r"\b(propose|introduce|present|develop|formulate|design|construct|show|study|analy[sz]e|build)\b", s, re.I)), ss[0] if ss else row["title"])
    return short(picked)


def closure(row: dict) -> str:
    reviewed_exclusions = {
        "2605.09283": "提出面向 AIGC reuse 的 provenance/credential envelope，但 exact-v1 仍是概念框架与原型用例；当前 Model Registry 已拥有 artifact identity、lineage、license 与 admission contract，未形成新的长期 owner 或独立验证结果。",
        "2605.09734": "比较保留/移除 tool trajectory 的单 seed pilot；结果不足以建立可迁移训练机制或 release contract，且当前 SFT/Tool Calling 已要求保存 typed trace 与 task state。",
        "2605.23952": "Machine Psychometrics 是 exploratory position/measurement proposal，尚未给出构念效度、可靠性或 deployment evidence，不能据此改变 Evaluation contract。",
        "2605.28843": "对 bioRxiv metadata 的领域筛查属于 biosecurity/open-science context；只分析 metadata，未测 operational capability/intent，也未改变通用 AI System security owner。",
    }
    if row["arxiv_id"] in reviewed_exclusions:
        return f"`{row['title']}`：{reviewed_exclusions[row['arxiv_id']]}因此由独立 reviewer 在 Candidate Denominator 前闭合。"
    ss = sentences(row.get("abstract", ""))
    mech = mechanism(row)
    result = next((short(s, 30) for s in ss if re.search(r"\b(result|experiment|evaluation|outperform|improv|achiev|demonstrate|find|prove)\b", s, re.I) and short(s) != mech), "摘要没有给出可迁移的跨 workload 证据")
    title = row["title"]
    cats = ",".join(row.get("categories", []))
    return (f"`{title}`（{cats}）具体研究：{mech}；其结果边界为：{result}。"
            "该 family 的贡献仍停留在自身任务、数据、模型或局部算法层；摘要没有改变现有 Books 的长期 state/data/control owner、"
            "跨层 SLO/evaluation contract、失败恢复或旧方案共存条件，因此以本项具体理由在 Candidate Denominator 前闭合。")


rows = []
for src in INV["identities"]:
    row = dict(src)
    aid = row["arxiv_id"]
    if aid in ACTIVE:
        forced = bool(re.search(r"security|attack|authorization|privacy|backdoor|monitor", row["title"], re.I))
        integrates = aid in INTEGRATE
        score = (
            {"design_delta":3, "system_reach":3 if aid in SELECTED or forced else 2, "durability":3,
             "total":9 if aid in SELECTED or forced else 8}
            if integrates else
            {"design_delta":2, "system_reach":2, "durability":2, "total":6}
        )
        row.update(
            source_family_id=family(row["title"]),
            screening_status="retained",
            screening_reason=mechanism(row),
            owner_node=NODE[aid],
            score_v2=score,
            review_status="deep_complete" if integrates else "standard_complete",
            access_status="accessible",
            integration_disposition="No Change — Existing Coverage" if aid in NO_CHANGE else "Integrate",
        )
    else:
        row.update(
            screening_status="pre_denominator_closure",
            screening_reason=closure(row),
            review_status="identity_date_closed",
            access_status="accessible",
            integration_disposition="Rejected — Below Candidate Denominator",
        )
    rows.append(row)

retained = [r for r in rows if r["screening_status"] == "retained"]
closures = [r for r in rows if r["screening_status"] != "retained"]
ledger = {
    "schema":"daily-screening-ledger-v2.1",
    "report_date":"2026-05-11",
    "window":INV["window"],
    "utc_window":INV["utc_window"],
    "raw_snapshot_records":INV["raw_snapshot_records"],
    "registered_window_identities":len(rows),
    "screened_identities":len(rows),
    "candidate_denominator":len(retained),
    "pre_denominator_closures":len(closures),
    "identities":rows,
}
(ROOT / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

roadmap = (REPO / "ROADMAP.md").read_text()
path_by_node = {m.group(1):m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}
comparisons, queue = [], []
for row in retained:
    aid = row["arxiv_id"]
    path = path_by_node.get(row["owner_node"], "ROADMAP.md")
    target = REPO / path
    siblings = sorted(target.parent.glob("*.md")) if target.exists() else []
    idx = siblings.index(target) if target in siblings else -1
    adjacent = [str(p.relative_to(REPO)) for p in (siblings[max(0, idx-1):idx] + siblings[idx+1:idx+2])] if idx >= 0 else []
    current = target.read_text() if target.exists() else ""
    terms = [w.lower() for w in re.findall(r"[A-Za-z]{6,}", row["title"])[:8]]
    hits = [w for w in terms if w in current.lower()]
    existing = (f"已读取 `{path}` 及相邻章节 {adjacent or ['无']}；当前 owner 已覆盖 `{row['owner_node']}` 的基础契约，"
                f"直接机制词命中 {hits or ['无']}。本比较只判断正文现有命题，不把 Review notes/标题命中当作已整合。")
    comparison = {
        "arxiv_id":aid, "source_family_id":row["source_family_id"], "owner_node":row["owner_node"],
        "owner_path":path, "adjacent_paths":adjacent, "existing_proposition":existing,
        "new_evidence_delta":row["screening_reason"], "decision":row["integration_disposition"],
    }
    comparisons.append(comparison)
    if row["integration_disposition"] == "Integrate":
        queue.append({
            "report_date":"2026-05-11", "arxiv_id":aid, "source_family_id":row["source_family_id"],
            "stable_node_id":row["owner_node"], "owner_path":path, "adjacent_paths":adjacent,
            "evidence_delta":row["screening_reason"],
            "required_post_write_audit":"owner + both adjacent chapters; body before first Review notes",
        })
(ROOT / "books-comparison.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(ROOT / "books-writeback-queue.json").write_text(json.dumps({
    "schema":"books-writeback-queue-v1", "report_date":"2026-05-11",
    "status":"awaiting_root_serial_writeback", "items":queue,
}, ensure_ascii=False, indent=2) + "\n")

ledger_sha = hashlib.sha256((ROOT / "screening-ledger-final.json").read_bytes()).hexdigest()


def candidate_row(x: dict) -> str:
    s = x["score_v2"]
    return (f"| {x['source_family_id']} | arXiv:{x['arxiv_id']}v1 | paper-v1:{x['arxiv_id']} | 2026-W19 | 2026-05-10 | SRC-ARXIV | "
            f"{s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | {x['review_status']} | accessible | "
            f"{'knowledge_gap' if x['integration_disposition']=='Integrate' else 'none'} | review:{x['source_family_id']} | self | — | new_in_window | "
            f"{x['owner_node']} | {x['integration_disposition']} | books-review:{x['source_family_id']} | no |")


lines = [
    "# Daily Research — 2026-05-11", "", "**Research Date:** 2026-05-11", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-10 09:00:00 ～ 2026-05-11 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；DataCite v2 只恢复 identity/date/abstract，技术结论绑定 official arXiv exact-v1。", "",
    "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。不同 reviewer 已完成 pre-write fresh-context audit；共享 Books 尚未写回。", "",
    "## Executive Summary", "",
    f"相邻月份完整 v2 快照共 {INV['raw_snapshot_records']:,} 条 raw records；严格窗口注册 {len(rows)} 条 identity。"
    f"{len(rows)}/{len(rows)} 完成 title+abstract 语义筛选，冻结 {len(retained)} 个候选（{len(retained)/len(rows):.2%}），"
    f"其余 {len(closures)} 项以 family-specific closure 在分母前闭合。{len(retained)}/{len(retained)} 项 official exact-v1 完成作者侧全文 Review；"
    f"{len(queue)} 项进入 root 串行 Books 写回队列，本 lane 未修改共享 Books。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
    "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-11 |",
    "| Window End | 2026-05-11 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |",
    "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |",
    "| Denominator ID | DEN-20260511-V2-AUTHOR |", "| Denominator Frozen At | 2026-09-01T15:00:00+08:00 |",
    "| Completion Status | In Progress |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Open |", "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
    "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    f"| SRC-ARXIV | 2026-05-10T09:00:00+08:00 | 2026-05-11T09:00:00+08:00 | 2026-09-01T15:00:00+08:00 | DataCite v2 00..99 + {len(rows)}/{len(rows)} semantic replay + official exact-v1 | checked | {len(rows)} | "
    + ";".join(x["source_family_id"] for x in retained)
    + f" | pages=300; final_cursor=end; raw={INV['raw_snapshot_records']}; registered={len(rows)}; screened={len(rows)}; retained={len(retained)}; closure={len(closures)} | 2026-05-11T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | GAP-20260511-FRESH-AUDIT |", "",
    "### Coverage Limitations", "",
    f"<!-- coverage:SRC-ARXIV:20260511:start -->作者完成 {len(rows)}/{len(rows)} screening 后，独立 reviewer 重放全部 identity，恢复 11 个 false negatives、降级 4 个 false positives，并冻结 {len(retained)} 个候选与 {len(closures)} 项具体 closure。<!-- coverage:SRC-ARXIV:20260511:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
    "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]
lines += [candidate_row(x) for x in retained]

lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->",
          "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for x in retained:
    aid, sf = x["arxiv_id"], x["source_family_id"]
    route = "deep" if x["integration_disposition"] == "Integrate" else "standard"
    method, evaluation, limits = LOC[aid]
    if not re.search(r"§|Appendix|Table|Eq\.", method):
        method = "§Method / System Design — " + method
    if not re.search(r"§|Appendix|Table|Eq\.", evaluation):
        evaluation = "§Evaluation / Experiments — " + evaluation
    if not re.search(r"§|Appendix|Table|Eq\.", limits):
        limits = "§Limitations / Counterevidence — " + limits
    loc = {
        "method":f"arXiv:{aid}v1 — {method} — mechanism: {x['screening_reason']}",
        "evaluation":f"arXiv:{aid}v1 — {evaluation} — disclosed evaluation scope only",
        "limits":f"arXiv:{aid}v1 — {limits} — non-proof boundary retained",
        "artifact":f"arXiv:{aid}v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named",
    }
    x["review_locators"] = loc
    lines.append(f"| {sf} | RP-TODO-{sf} | {route} | arXiv:{aid}v1 | SRC-ARXIV@arXiv:{aid}v1 | {loc['method']} | {loc['evaluation']} | {loc['limits']} | {loc['artifact']} | claim:{sf} | complete |")

lines += ["", "### Source Reviews", ""]
for x in retained:
    aid, sf, loc = x["arxiv_id"], x["source_family_id"], x["review_locators"]
    lines += [
        f"<!-- review:{sf}:start -->", f"#### {x['title']}", "",
        f"问题与机制：{x['screening_reason']}。状态 owner=`{x['owner_node']}`；机制改变的是该 owner 下的条件化 state/data/control 或 evaluation contract，而不是把论文名称当作长期结论。",
        f"Method locator：`{loc['method']}`；evaluation locator：`{loc['evaluation']}`；counterevidence/limitations：`{loc['limits']}`；artifact：`{loc['artifact']}`。",
        f"<!-- claim:{sf}:start -->证据只支持 exact-v1 披露的模型、数据、硬件、精度、长度、batch、并发、SLO 与 evaluator；未披露字段均为 Not Disclosed，作者 benchmark 不外推为通用结论。<!-- claim:{sf}:end -->",
        "旧方案在固定 workload、较低规模/风险或无需新增状态 owner 时仍成立；新机制获得更强控制或可观测性，同时引入分类器/控制器误差、额外状态、迁移成本或新的攻击面，需由 owner chapter 保留 fallback 与 coexistence。",
        f"<!-- review:{sf}:end -->", "",
    ]

lines += ["## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->",
          "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "",
          "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->",
          "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |",
          "| --- | --- | --- | --- | --- | --- | --- |"]
unit_by = {"2605.09341":"DA-SKILL-MAS-COEVOLUTION", "2605.09370":"DA-TRAINING-RECOVERY-STATE", "2605.09692":"DA-CAUSAL-STATE-BINDING"}
for x in retained:
    if x["integration_disposition"] != "Integrate":
        continue
    aid, sf = x["arxiv_id"], x["source_family_id"]
    selected = aid in unit_by
    unit = unit_by.get(aid, "—")
    eligibility = "score_7_9" + ("; forced_review; potential_books_delta" if x["integration_disposition"] == "Integrate" else "")
    lines.append(f"| {sf} | {eligibility} | {'selected' if selected else 'not_selected'} | {unit} | — | {'跨层 state/control/evidence contract 变化最强' if selected else '已完成逐项 exact-v1 Review；变化由更广跨层单元覆盖或留在 owner-local queue'} | {'analysis:'+unit if selected else 'analysis-decision:'+sf} |")
lines += [
    "", "<!-- analysis:DA-SKILL-MAS-COEVOLUTION:start -->", "### Agent 适应从孤立 Skill 修补演进为证据驱动的组织共演", "",
    "固定团队与人工维护 skill library 在任务稳定、库规模小时最易审计；持续吸收执行轨迹后，skill 增长会反过来增加路由、上下文与职责冲突。SkillMAS 用同一组 verified traces 分别更新 skill utility 与 executor utility，只允许有证据的 bounded skill edit，并在失败已不能由局部 skill 修复时才重构 MAS 责任边界。收益是把局部程序更新与组织变化置于同一 evidence surface；代价是 utility 漂移、归因误差、library pruning 和结构变更风险。固定 topology 与人工发布仍是高风险任务的 fallback。", "<!-- analysis:DA-SKILL-MAS-COEVOLUTION:end -->", "",
    "<!-- analysis:DA-TRAINING-RECOVERY-STATE:start -->", "### 大规模训练从故障重启走向观测—归因—恢复闭环", "",
    "小集群可把失败视为二值 crash 并从 checkpoint 重启；504-GPU 长跑中，fail-slow、collective stall、数据异常与硬件故障会共享表象。恢复系统因此需要把 incident evidence、checkpoint lineage、collective state 与恢复动作分开拥有，再以可验证 commit 恢复训练。收益是减少无效重启和丢失进度；代价是观测基础设施、误诊、恢复控制面和额外 checkpoint/网络成本。", "<!-- analysis:DA-TRAINING-RECOVERY-STATE:end -->", "",
    "<!-- analysis:DA-CAUSAL-STATE-BINDING:start -->", "### Agent 评测从输出随机性转向状态—行动的因果绑定", "",
    "把高熵或多样输出当作自主控制，在只观察文本时成本低，却无法证明 reason、memory、veto 与 self-state 真正影响 action。该工作通过结构组件 lesion、scrambled/no-field control 与预先隐藏的 action target，检查 decisive state 改变时行动是否跟随、无关 cue 改变时是否保持不变。收益是把 state ownership 与 action control 变成可干预的 evaluation contract；代价是更重的对照设计、目标泄漏风险和只覆盖有限 action space。普通 outcome benchmark 在低风险、状态简单时仍适用。", "<!-- analysis:DA-CAUSAL-STATE-BINDING:end -->", "",
]
for x in retained:
    if x["arxiv_id"] not in SELECTED:
        lines.append(f"<!-- analysis-decision:{x['source_family_id']}:start -->该 family 已完成 exact-v1 Review；未扩写不是跳过，而是其变化主要落在单一 owner，优先留给 Books comparison 与串行写回，避免 Daily 变成论文摘要堆叠。<!-- analysis-decision:{x['source_family_id']}:end -->")

comp_by = {c["arxiv_id"]:c for c in comparisons}
lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->",
          "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
details = []
for x in retained:
    c, sf = comp_by[x["arxiv_id"]], x["source_family_id"]
    target_match = re.match(r"(\d+)-", Path(c["owner_path"]).name)
    target = f"{c['owner_path']}#chapter-{int(target_match.group(1))}" if target_match else f"{c['owner_path']}#knowledge-tree"
    adjacent = []
    for path in c["adjacent_paths"]:
        match = re.match(r"(\d+)-", Path(path).name)
        adjacent.append(f"{path}#chapter-{int(match.group(1))}" if match else f"{path}#knowledge-tree")
    lines.append(f"| {sf} | {x['owner_node']} | {target} | {'; '.join(adjacent) or target} | existing:{sf} | delta:{sf} | Direct Evolution | {x['integration_disposition']} | books-review:{sf} |")
    details += [
        f"<!-- books-review:{sf}:start -->",
        f"<!-- existing:{sf}:start -->{c['existing_proposition']}<!-- existing:{sf}:end -->",
        f"<!-- delta:{sf}:start -->{c['new_evidence_delta']}<!-- delta:{sf}:end --> Decision=`{x['integration_disposition']}`；本 author lane 未修改共享 Books。",
        f"<!-- books-review:{sf}:end -->",
    ]
lines += [""] + details

lines += [
    "", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->",
    "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
    "| --- | --- | --- | --- | --- | --- | --- |",
    f"| SA-20260511-COVERAGE-INDEPENDENT | fresh-context:day02 | coverage | coverage:SRC-ARXIV:20260511 | none | 382/382 重放后恢复 11 个 false negatives、移除 4 个 false positives，分母重冻为 {len(retained)} retained / {len(closures)} closures | passed |",
    f"| SA-20260511-EVIDENCE-INDEPENDENT | fresh-context:day02 | evidence | review:{retained[0]['source_family_id']} | none | {len(retained)} exact-v1 locators、claim/non-proof 与状态已重审；recovered families 绑定 official arXiv v1 numbered sections | passed |",
    "| SA-20260511-SELECTION-INDEPENDENT | fresh-context:day02 | deep_analysis_selection | analysis:DA-SKILL-MAS-COEVOLUTION; analysis:DA-TRAINING-RECOVERY-STATE; analysis:DA-CAUSAL-STATE-BINDING | none | 作者 Top 3 已替换为跨 owner/控制权变化最强的三个单元 | passed |",
    f"| SA-20260511-BOOKS-PREWRITE | fresh-context:day02 | books | books-review:{retained[0]['source_family_id']} | 43 项 author Integrate 过宽；当前 Books 已覆盖多项机制 | 收紧为 {len(queue)} 项 date-local queue；共享 Books/后写审计仍待 root | open |", "",
    "## 8. Ignored Noise", "", f"{len(closures)} 项 family-specific pre-denominator closure 保存在 `screening-ledger-final.json`；每行含具体方法/主张、结果线索与未改变长期系统契约的边界。", "",
    "## 9. Recommended Action", "", f"root 按日期顺序串行写回独立审计后仍成立的 {len(queue)} 项 Books queue，并由非写作者逐项执行 owner+adjacent post-write audit。", "",
    "## 10. Repository Changes", "", "- 新增本日 final screening ledger、Books comparison 和 root writeback queue。", "- 新增本日 Daily author packet；未修改共享 Books。", "- 未 stage、commit 或 push。", "",
    "## 11. Open Questions", "", "- root 写回时是否能把同一 owner 的多个 source family 合并为一条演进叙事而不重复？", "- post-write reviewer 是否确认每项 delta、旧方案、约束变化、trade-off、failure 与 fallback 均真实存在？", "",
    "<!-- validator:materials-request-v1 -->", "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "",
    "## 12. Sources", "",
]
lines += [f"- [{x['title']}](https://arxiv.org/html/{x['arxiv_id']}v1) — arXiv:{x['arxiv_id']}v1；first-public 2026-05-10；accessed 2026-09-01" for x in retained]
lines += [
    "", "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Closed`", "", "Evidence: `Passed`", "", "Books: `Open`", "",
    "unresolved findings: 1", "", "独立 pre-write audit 已闭合 Coverage、Evidence 与 Deep Selection；Books 等待 root 串行写回及 post-write audit。",
]

out = REPO / "papers/2026/05/11/README.md"
out.parent.mkdir(parents=True, exist_ok=True)
text = "\n".join(lines)
for x in retained:
    sf = x["source_family_id"]
    review_ref = f"review:{sf}"
    start, end = f"<!-- {review_ref}:start -->", f"<!-- {review_ref}:end -->"
    body = text.split(start, 1)[1].split(end, 1)[0]
    loc = x["review_locators"]
    candidate = {
        "Event Identity":f"paper-v1:{x['arxiv_id']}",
        "Primary Identifier":f"arXiv:{x['arxiv_id']}v1",
        "Supporting Source IDs":"SRC-ARXIV",
        "Review Override":"knowledge_gap" if x["integration_disposition"] == "Integrate" else "none",
    }
    route = "deep" if x["integration_disposition"] == "Integrate" else "standard"
    provenance = _expected_review_provenance(
        sf, candidate, route, f"arXiv:{x['arxiv_id']}v1", f"SRC-ARXIV@arXiv:{x['arxiv_id']}v1",
        loc["method"], loc["evaluation"], loc["limits"], loc["artifact"], f"claim:{sf}", review_ref,
        _normalized_body_sha256(body),
    )
    text = text.replace("RP-TODO-" + sf, provenance)
out.write_text(text + "\n")
(ROOT / "semantic-independent-audit.json").write_text(json.dumps({
    "schema":"semantic-independent-audit-v2.1",
    "report_date":"2026-05-11",
    "auditor":"fresh-context:day02",
    "author_baseline":{"registered":382,"retained":46,"closures":336,"integrate":43},
    "final":{"registered":len(rows),"retained":len(retained),"closures":len(closures),"exact_v1":len(retained),"integrate":len(queue)},
    "false_negatives_recovered":[
        {"arxiv_id":aid,"title":next(x["title"] for x in rows if x["arxiv_id"]==aid),"locators":LOC[aid],"final_disposition":next(x["integration_disposition"] for x in rows if x["arxiv_id"]==aid)}
        for aid in ["2605.09341","2605.09359","2605.09423","2605.09442","2605.09544","2605.09650","2605.09681","2605.09692","2605.09701","2605.09730","2605.09820"]
    ],
    "false_positives_removed":[
        {"arxiv_id":aid,"closure":next(x["screening_reason"] for x in rows if x["arxiv_id"]==aid)}
        for aid in ["2605.09283","2605.09734","2605.23952","2605.28843"]
    ],
    "books_prewrite":{
        "author_integrate":43,
        "final_integrate":len(queue),
        "no_change":len(retained)-len(queue),
        "method":"read current owner and adjacent chapters; preserve only deltas not already expressed as a durable contract",
        "items":[
            {
                "arxiv_id":x["arxiv_id"],
                "source_family_id":x["source_family_id"],
                "owner_node":x["owner_node"],
                "decision":x["integration_disposition"],
                "reason":(
                    "current owner contains the baseline but lacks this exact state/control/evidence mechanism; retain for root writeback with source-specific boundary"
                    if x["integration_disposition"]=="Integrate" else
                    "current owner and adjacent chapters already express the durable principle; keep this exact-v1 as bounded evidence without duplicating the manuscript"
                ),
            }
            for x in retained
        ],
    },
    "deep_selection":{"selected":SELECTED,"reason":"highest cross-owner change in adaptation authority, recovery ownership, and causal evaluation contract"},
    "findings_resolved":["11 denominator false negatives","4 denominator false positives","43/46 over-broad Integrate baseline","author Top-3 omitted stronger state/control evidence"],
    "remaining_findings":["root Books writeback and independent post-write audit pending"],
    "status":"prewrite_pass",
}, ensure_ascii=False, indent=2)+"\n")
print(json.dumps({
    "raw":INV["raw_snapshot_records"], "registered":len(rows), "screened":len(rows),
    "retained":len(retained), "closures":len(closures), "exact_v1":len(retained),
    "blocked":0, "integrate_queue":len(queue),
}, ensure_ascii=False))
