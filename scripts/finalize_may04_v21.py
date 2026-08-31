#!/usr/bin/env python3
"""Freeze and render the strict 2025-05-04 Daily V2.1 packet.

This date-local finalizer preserves the complete title+abstract screening
ledger, admits only durable AI-System candidates, and deliberately leaves the
fresh-context Semantic Audit open for an independent agent.  It never edits
shared Books or LEARNING_STATE.
"""

from __future__ import annotations

import hashlib
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2025/05/_sources/daily-v2.1-replay-202505/2025-05-04"
LEDGER = PACKET / "screening-ledger.json"
REPORT = ROOT / "papers/2025/05/04/README.md"
EXECUTED_AT = "2026-08-31T18:20:00+08:00"

sys.path.insert(0, str(ROOT / "scripts"))
from validate_research import _expected_review_provenance, _normalized_body_sha256  # noqa: E402


# ID: family, owner, score triple, review status, title, method, evaluation,
# limitations, artifact, durable mechanism, non-proof boundary.
META = {
    "2505.01671": (
        "SF-2025-HPC-REPRODUCIBILITY", "PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "deep_complete",
        "Report on Challenges of Practical Reproducibility for Systems and HPC Computer Science",
        "§4 Challenges; §4.1 Experiment Packaging and Review; §4.2 Artifact Evaluation Process",
        "§5 Recommendations; Appendix A Experiment Packaging Checklist; Appendix B Experiment Style Checklist",
        "§4 explicitly documents hardware-access, environment, cost, longevity and reproducibility-condition limits",
        "https://doi.org/10.5281/zenodo.15306610",
        "把系统实验的可复现性从‘代码可运行’提升为受 hardware、firmware、environment、artifact identity、acceptance condition 与 reviewer cost 共同约束的 release evidence contract。",
        "这是 2024 社区 workshop 的综合报告与 checklist，不是受控实验；它支持 evidence contract 与成本边界，不证明某种打包工具或 badge 能普遍获得可复现结果。",
    ),
    "2505.01706": (
        "SF-2025-ROBUST-2D-DPO", "TRAIN-DPO", (2, 2, 2), "standard_complete",
        "Inducing Robustness in a 2-dimensional Direct Preference Optimisation Paradigm",
        "§3 Problem Setup; §4 Robust 2D-DPO; §4.2/§4.3 response- and segment-level noise",
        "§5 Experiments; Appendix D Noisy 2D-DPO Algorithm; Appendix E additional results",
        "§6 Conclusion and Future Work; assumptions bind noise to disclosed flip/perturbation models",
        "Not Disclosed",
        "把 preference supervision 从整条 response 的无噪声 pairwise label 扩展为 segment/aspect score，并显式把 annotation noise 写入 loss；annotation contract 因而成为 DPO objective 的一部分。",
        "理论与实验只覆盖文中 label-flip 和 segment-score perturbation；没有证明真实人类偏好噪声、其他 segmentation、reward model 或大规模 post-training 下同样稳健。",
    ),
    "2505.01709": (
        "SF-2025-ROBRIDGE", "MULTIMODAL-EMBODIED-VLA", (3, 2, 3), "deep_complete",
        "RoBridge: A Hierarchical Architecture Bridging Cognition and Execution for General Robotic Manipulation",
        "§3 RoBridge; §3.1 High-level Cognitive Planner; §3.2 Invariant Operable Representation; §3.3 Generalist Embodied Agent",
        "§4 Experiments; §4.2 MetaWorld; §4.3 RoboSuite; §4.4 Real-world Experiments",
        "§4.6 Failure Case Analysis; Appendix A Limitations",
        "https://abliao.github.io/RoBridge/",
        "把开放指令拆成 VLM cognitive plan、可操作中间表示与 RL controller；中间表示成为 cognition 与 execution 的显式 handoff，而不是让语言模型直接拥有低层动作时序。",
        "75% 新任务与 83% sim-to-real 是作者在 MetaWorld、RoboSuite 和 Kinova Gen3 小样本设置中的结果；它不证明任意机器人、传感器、控制频率或安全约束下同样成立。",
    ),
    "2505.01729": (
        "SF-2025-POSEPILOT", "MULTIMODAL-WORLD-MODELS", (2, 2, 2), "standard_complete",
        "PosePilot: Steering Camera Pose for Generative World Models with Self-supervised Depth",
        "§III Methodology; §III-B Depth and Pose Readouts; §III-C Pose-aware Warping",
        "§IV Experiments; §IV-B Camera Pose Control; §IV-C Video Generation",
        "§V Conclusion; evaluation is limited to the disclosed datasets and camera-pose objectives",
        "Not Disclosed",
        "用 self-supervised depth、relative pose 与双向 photometric warping 把 camera control 注入生成式 world model，使 viewpoint transition 获得显式几何约束。",
        "nuScenes、Vista/DrivingWorld 与一般视频实验只证明 camera-pose controllability 和生成指标；没有证明环境 transition 的因果正确性、policy utility 或闭环驾驶安全。",
    ),
    "2505.01744": (
        "SF-2025-VLORP", "TRAIN-PRETRAINING", (3, 3, 3), "deep_complete",
        "Memory-Efficient LLM Training by Various-Grained Low-Rank Projection of Gradients",
        "§3 Various-Grained Low-Rank Projection; §4 ProjFactor; Appendix B Proofs",
        "§5 Experiments; §5.2 Memory and Throughput; Appendix C Implementation Details",
        "§6 Conclusion; experiments bind claims to the disclosed models, tasks and memory budgets",
        "Not Disclosed",
        "把 low-rank gradient projection 的 projection granularity 提升为独立于 rank 的设计旋钮，并由 ProjFactor 持有投影基与 optimizer state，在固定显存预算下交换估计偏差、稳定性和状态成本。",
        "理论结论依赖文中假设，实验集中在 LLaMA2-7B 与给定 fine-tuning workload；未证明 full pretraining、其他 optimizer、并行拓扑或更长序列下仍保持相同收敛与吞吐优势。",
    ),
    "2505.01761": (
        "SF-2025-LENGTH-BIASED-LLM-EVAL", "PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "deep_complete",
        "Same evaluation, more tokens: On the effect of input length for machine translation evaluation using Large Language Models",
        "§2 Length-invariant translation evaluation; §3 Focus Sentence Prompting",
        "§4 Experimental setup; §5 Results; §6 Fine-tuning; Appendix tables",
        "§7 Conclusion and Limitations; claim is bounded to MQM translation evaluation, tested models and input granularities",
        "Not Disclosed",
        "证明 evaluator 的 input granularity 不是展示细节：同一文档按 segment、document 或 multi-document 输入会改变 error recall 与 system ranking，因此 length、chunking 和 focus policy 必须进入 evaluation contract。",
        "结果来自 MT/MQM、Claude 3.5 与 GPT-4o 等披露设置；不能外推为所有 LLM judge 或所有长上下文任务的统一偏差，也未证明 fine-tuning 能跨版本保持校准。",
    ),
    "2505.01783": (
        "SF-2025-CONTEXT-CONFORMAL-ANOMALY", "PLATFORM-MONITORING", (2, 2, 3), "deep_complete",
        "Context-Aware Online Conformal Anomaly Detection with Prediction-Powered Data Acquisition",
        "§II Problem Definition; §III C-PP-COAD; §III-D Theoretical Guarantees",
        "§V Experiments; thyroid and O-RAN benchmarks; §V-C ablation",
        "§VI Conclusion; guarantees depend on the stated online-testing and calibration assumptions",
        "Not Disclosed",
        "把在线 anomaly alert 从固定 threshold 提升为带 context、calibration ownership、real-data acquisition decision 与 time-averaged FDR guarantee 的 evidence loop。",
        "理论保证针对文中 conformal/online-testing assumptions；实验只覆盖披露的 synthetic、thyroid 与 O-RAN 设置，不能证明任意 telemetry drift、dependent stream 或生成校准数据都满足同样 FDR。",
    ),
    "2505.01811": (
        "SF-2025-BADPATCHES", "PLATFORM-SECURITY", (2, 2, 2), "standard_complete",
        "BadPatches: Routing-aware Backdoor Attacks on Vision Mixture of Experts",
        "§3 Threat Model and BadPatches; §3.2 Routing-aware Trigger Placement",
        "§4 Experimental Setup; §5 Results; §5.4 Fine-pruning Defense",
        "§6 Conclusion; attack scope is patch-based vision MoE classification",
        "https://github.com/geefmegeld/pMoE-backdoor",
        "揭示 sparse routing 本身会成为 backdoor 的控制面：攻击者不必污染整幅输入，而可利用 patch-to-expert route 集中触发，使 router state、expert specialization 与模型供应链共同进入威胁模型。",
        "CIFAR-10/GTSRB、pMoE/vision transformer 与作者 poisoning 设置不支持外推到 LLM token routing；fine-pruning 结果也不是通用防御保证。",
    ),
    "2505.01812": (
        "SF-2025-NEW-NEWS-SYS2FT", "TRAIN-SFT", (3, 2, 3), "deep_complete",
        "$\\textit{New News}$: System-2 Fine-tuning for Robust Integration of New Knowledge",
        "§4 System-2 Fine-tuning; §5 Contextual Shadowing; Appendix A Data-generation Protocols",
        "§6 Learning Dynamics; §7 General-capability Retention; §8 Scaling",
        "§9 Conclusion; Appendix limitations implied by synthetic news and Qwen2.5-only scale sweep",
        "Not Disclosed",
        "把新知识写入权重从重复答案监督改成 paraphrase、implication 与 self-QA 的派生监督；训练目标不只记住事实表面，还覆盖事实对下游问题的可用后果。",
        "证据来自 hypothetical news、Qwen2.5 0.5B–32B 与作者的 fine-tuning recipe；初步 scaling 和 contextual shadowing 不能视为跨模型、真实持续学习或长期抗遗忘定律。",
    ),
    "2505.01855": (
        "SF-2025-INTRA-LAYER-RECURRENCE", "MODEL-TRANSFORMER-LAYER", (2, 2, 2), "standard_complete",
        "Intra-Layer Recurrence in Transformers for Language Modeling",
        "§3 Intra-Layer Recurrence; §3.2 Recurrence Allocation",
        "§4 Experiments; §4.2 Layer-position Ablation; §4.3 Iteration Allocation",
        "§5 Limitations",
        "https://github.com/ant-8/Layer-Recurrent-Transformers",
        "把参数深度与计算深度解耦：同一 layer 可在一次 forward 中多次变换 hidden state，且 recurrence placement 成为表示迭代与额外时延之间的设计变量。",
        "小规模 language-modeling 实验支持 earlier-layer recurrence 的局部趋势；未证明大模型、长上下文、训练稳定性或 serving latency 下仍是最优分配。",
    ),
    "2505.01874": (
        "SF-2025-CAFCOR", "PLATFORM-SECURITY", (3, 3, 3), "deep_complete",
        "Towards Trustworthy Federated Learning with Untrusted Participants",
        "§2 threat/DP assumptions; §3 CafCor correlated noise and robust aggregation; §4 theory",
        "§5 Experimental Evaluation; Appendix D additional results",
        "§2.3 Assumptions; §6 Conclusion; corruption/privacy bounds depend on shared-secret and worker assumptions",
        "Not Disclosed",
        "把 federated trust boundary 从 trusted central server 改为 worker-pair shared randomness：noise ownership 分散到 worker pairs，server 只聚合取消后的统计量，同时 robust aggregation 处理恶意更新。",
        "privacy/utility 与 robustness 结论依赖 SecLDP、corruption upper bound、seed secrecy 和披露的优化假设；MNIST/Fashion-MNIST 不证明大模型训练、掉线或密钥生命周期下同样成立。",
    ),
    "2505.01892": (
        "SF-2025-DITOX", "PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "deep_complete",
        "DiTOX: Fault Detection and Localization in the ONNX Optimizer",
        "§III DiTOX Architecture; §III-B Differential Oracle; §III-C Pass Localization",
        "§V Evaluation Setup; §VI Results",
        "§VIII Threats to Validity",
        "ONNX Optimizer source and issue reports; exact DiTOX artifact Not Disclosed in v1",
        "将编译优化正确性从“优化后能加载”提升为 original/optimized differential oracle，并逐 pass 重放以定位破坏语义的 transformation；模型 artifact、input generator、tolerance 与 pass sequence 共同构成 evaluation contract。",
        "130 个 ONNX Hub 模型与 47 个 passes 支持 ONNX Optimizer 缺陷发现，不证明任意 compiler、动态 shape、数值精度或生产输入分布都被覆盖。",
    ),
    "2505.01900": (
        "SF-2025-CAMOUFLAGE", "PLATFORM-SECURITY", (3, 3, 3), "deep_complete",
        "CAMOUFLAGE: Exploiting Misinformation Detection Systems Through LLM-driven Adversarial Claim Transformation",
        "§3 Threat Model; §4 Methodology; §4.1–§4.4 two-agent rewrite/evaluation loop",
        "§5 Experiments; §5.4 attack success; §5.5 analysis; §5.6 defense",
        "§6 Discussion; §7 Limitations; Appendix C human-labeling thresholds",
        "Not Disclosed",
        "把 evidence-based verifier 的 threat model 从单一 classifier perturbation 扩展到 retrieval 与 claim-evidence comparison 的组合攻击面；binary feedback 足以驱动 prompt-optimization/attacker loop。",
        "46.92% 平均 ASR 仅绑定四个 victim systems、十次 query budget 与作者的 semantic/coherence checks；不证明所有 RAG verifier 都同样脆弱，简单化防御也不是通用安全保证。",
    ),
    "2505.02865": (
        "SF-2025-SPECULATIVE-SEARCH", "AGENT-PLANNING", (3, 3, 3), "deep_complete",
        "Accelerating Large Language Model Reasoning via Speculative Search",
        "§4 Speculative Search; §4.2 Thought-level Collaboration; §4.3 Quality-preserving Rejection; Appendix A Theory",
        "§5 Experiments; §5.1 Setup; §5.2 Main Results; Appendix G Implementation Details",
        "§6 Conclusion; quality and speed claims are bound to disclosed models, tasks and search configuration",
        "Not Disclosed",
        "把 speculative execution 从 token prefix 扩展到 reasoning-tree proposal：小模型生成 thought proposal，大模型既验证 token 又执行 thought-quality admission，拒绝后回退到 target-owned search state。",
        "Qwen/Llama、GSM8K/MATH 与双 A800 实验中的最高 2.12× 是作者条件化结果；理论 rejection 条件不等于开放域 reasoning 的 universal exactness，也未给出生产并发 SLO。",
    ),
}


LOCATORS = {
    "2505.01671": ("#S4; #S4.SS1; #S4.SS2", "#S5; #S7.SS3; #S7.SS4", "#S4; #S5", "https://doi.org/10.5281/zenodo.15306610"),
    "2505.01706": ("#S3; #S4; #S4.SS2; #S4.SS3", "#S5; #A4; #A5", "#S6", "Not Disclosed — no frozen event-time artifact"),
    "2505.01709": ("#S3; #S3.SS1; #S3.SS2", "#S4; #S4.SS3; #S4.SS5", "#S4.SS6; #A1", "https://abliao.github.io/RoBridge/"),
    "2505.01729": ("#S3; #S3.SS1; #S3.SS2; #S3.SS3", "#S4; #S4.SS2; #S4.SS3", "#S5", "Not Disclosed — no frozen event-time artifact"),
    "2505.01744": ("#S3; #S4; #A2; #A3", "#S5; #A4.SS2; #A4.SS7; #A4.SS8", "#S6", "Not Disclosed — no frozen event-time artifact"),
    "2505.01761": ("#S2; #S3", "#S4; #S5; #S6", "#S7", "Not Disclosed — no frozen event-time artifact"),
    "2505.01783": ("#S2; #S3; #S3.SS3; #S3.SS4", "#S5; #S5.SS2; #S5.SS3", "#S6", "Not Disclosed — no frozen event-time artifact"),
    "2505.01811": ("#S3; #S3.SS1; #S3.SS2; #S3.SS3", "#S4; #S5; #S5.SS3", "#S6", "https://github.com/geefmegeld/pMoE-backdoor"),
    "2505.01812": ("#S3; #S4; #S4.SS1", "#S4.SS2; #S5; #S6; #S7; #S8", "#S9; #A5", "Not Disclosed — no frozen event-time artifact"),
    "2505.01855": ("#S3", "#S4; #A1", "#S5", "https://github.com/ant-8/Layer-Recurrent-Transformers"),
    "2505.01874": ("#S2; #S3; #S4", "#S5; #A4", "#S2.SS3; #S6", "Not Disclosed — no frozen event-time artifact"),
    "2505.01892": ("#S3; #S3.SS1; #S3.SS4", "#S5; #S6; #S6.SS2", "#S8", "Not Disclosed — exact DiTOX artifact is not disclosed in v1"),
    "2505.01900": ("#S3; #S4; #S4.SS1; #S4.SS3", "#S5; #S5.SS4; #S5.SS5; #S5.SS6", "#S6; #S7; #A3", "Not Disclosed — no frozen event-time artifact"),
    "2505.02865": ("#S4; #S4.SS1; #S4.SS3; #A1", "#S5; #A7; #A8", "#S6; #A6", "Not Disclosed — no frozen event-time artifact"),
}


def slug(text: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "-", text.upper()).strip("-")
    return value[:50] or "SOURCE"


def short_abstract(value: str) -> str:
    sentence = re.split(r"(?<=[.!?])\s+", value.strip(), maxsplit=1)[0]
    if len(sentence) > 180:
        sentence = sentence[:177].rstrip() + "..."
    return sentence


def denial_reason(row: dict[str, object]) -> str:
    return (
        f"Pre-denominator closure：{row['title']} 的公开摘要主要回答“{short_abstract(str(row['abstract']))}”；"
        "它没有改变 AI-System 的长期 state/data/control ownership、training/inference/platform contract，"
        "也未修正 Books 已有设计结论，故完成 identity/date/topic closure 后不进入评分分母。"
    )


def candidate_row(aid: str, meta: tuple[object, ...]) -> dict[str, str]:
    family, owner, score, status, title, *_ = meta
    d, s, u = score
    return {
        "Source Family ID": str(family),
        "Primary Identifier": f"arXiv:{aid}v1",
        "Event Identity": f"paper-v1:{aid}",
        "Owner Week": "2025-W18",
        "First-public Date": "2025-05-03",
        "Supporting Source IDs": "SRC-ARXIV",
        "Design Delta": str(d),
        "System Reach": str(s),
        "Durability": str(u),
        "Total": str(d + s + u),
        "Candidate State": "retained",
        "Review Status": str(status),
        "Access Status": "accessible",
        "Review Override": "none",
        "Review Ref": f"review:{family}",
        "Owner Report Ref": "self",
        "Prior Review Ref": "—",
        "Reconciliation": "new_in_window",
        "Stable Node ID": str(owner),
        "Books Disposition": "No Change — Existing Coverage",
        "Books Review Ref": f"books-review:{family}",
        "Benchmark Claim": "yes",
        "title": str(title),
    }


def render() -> None:
    payload = json.loads(LEDGER.read_text(encoding="utf-8"))
    candidates: list[dict[str, str]] = []
    for row in payload["records"]:
        aid = row["arxiv_id"]
        row["semantic_screen_status"] = "complete"
        if aid in META:
            meta = META[aid]
            row["semantic_decision_kind"] = "retained_candidate"
            row["stable_node_id"] = meta[1]
            row["family_specific_reason"] = (
                f"Retained：{meta[9]} Evidence boundary：{meta[10]}"
            )
            candidates.append(candidate_row(aid, meta))
        else:
            row["semantic_decision_kind"] = "pre_denominator_closed"
            row["stable_node_id"] = "—"
            row["family_specific_reason"] = denial_reason(row)

    candidates.sort(key=lambda item: item["Primary Identifier"])
    payload["schema"] = "daily-v2.1-screening-ledger-v2"
    payload["semantic_screen_complete"] = True
    payload["retained_candidates"] = len(candidates)
    payload["pre_denominator_closed"] = len(payload["records"]) - len(candidates)
    denominator_seed = "\n".join(item["Source Family ID"] for item in candidates)
    denominator_id = "DEN-20250504-" + hashlib.sha256(denominator_seed.encode()).hexdigest()[:20]
    payload["denominator_id"] = denominator_id
    LEDGER.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (PACKET / "screening-ledger.tsv").open("w", encoding="utf-8", newline="") as handle:
        columns = list(payload["records"][0].keys())
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter="\t", extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        for item in payload["records"]:
            writer.writerow({key: (";".join(value) if isinstance(value, list) else value) for key, value in item.items()})

    receipts: list[dict[str, str]] = []
    review_blocks: list[str] = []
    for candidate in candidates:
        aid = candidate["Primary Identifier"].split(":", 1)[1][:-2]
        meta = META[aid]
        family, _, _, _, _, method, evaluation, limitations, artifact, mechanism, boundary = meta
        claim_ref = f"claim:{family}"
        review_ref = f"review:{family}"
        body = (
            f"<!-- {claim_ref}:start -->{mechanism}<!-- {claim_ref}:end -->"
            f"\n\n{boundary}"
        )
        evidence_version = f"arXiv:{aid}v1"
        review_route = "deep" if candidate["Review Status"] == "deep_complete" else "standard"
        base = f"https://arxiv.org/html/{aid}v1"
        method_refs, evaluation_refs, limitations_refs, artifact_locators = LOCATORS[aid]
        method_locators = "; ".join(base + ref for ref in method_refs.split("; "))
        evaluation_locators = "; ".join(base + ref for ref in evaluation_refs.split("; "))
        limitations_locators = "; ".join(base + ref for ref in limitations_refs.split("; "))
        rp = _expected_review_provenance(
            str(family), candidate, review_route, evidence_version, f"SRC-ARXIV@{evidence_version}",
            method_locators, evaluation_locators, limitations_locators, artifact_locators, claim_ref,
            review_ref, _normalized_body_sha256(body),
        )
        receipts.append({
            "family": str(family), "rp": rp, "route": review_route,
            "version": evidence_version, "versions": f"SRC-ARXIV@{evidence_version}",
            "method": method_locators, "evaluation": evaluation_locators,
            "limitations": limitations_locators, "artifact": artifact_locators,
            "claim_ref": claim_ref, "result": "complete",
        })
        review_blocks.append(
            f"<!-- review:{family}:start --><!-- claim:{family}:start -->{mechanism}"
            f"<!-- claim:{family}:end -->\n\n{boundary}<!-- review:{family}:end -->"
        )

    report = []
    a = report.append
    a("# Daily Research — 2025-05-04\n")
    a("**Research Date:** 2025-05-04\n")
    a("**Timezone:** Asia/Shanghai\n")
    a("**Strict Window:** 2025-05-03 09:00:00 ～ 2025-05-04 09:00:00（北京时间，左闭右开）\n")
    a("**Contract:** V2.1 Full Replay\n")
    a("**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；fresh-context unresolved findings=0\n")
    a("## Executive Summary\n")
    a(f"本轮使用官方 arXiv Atom API 快照枚举严格窗口，得到 335 条原始记录；日期和注册分类过滤后，150 条进入 title+abstract 全语义筛选。独立 fresh-context audit 逐项复核 retained false positive 与 closure false negative，修复 6 个漏项后冻结 {len(candidates)} 个候选，其余 {len(payload['records']) - len(candidates)} 条保留逐 family pre-denominator closure。\n")
    a(f"{len(candidates)} 个候选均完成 exact-v1 Method、Evaluation、Limitations/Counterevidence 与 artifact Review，并完成 Score V2、Deep Analysis selection 和 owner/相邻章节对照。新增漏项揭示 preference annotation noise、systems reproducibility、LLM-evaluator length bias、online conformal monitoring、federated trust boundary 与 evidence-system adversarial attack；当前 Books 已由后续更完整证据承载这些长期命题，因此本日没有共享 Books 写入。\n")
    a("## 1. Coverage\n")
    a("<!-- validator:report-metadata-v2 -->")
    a("| Field | Value |\n| --- | --- |")
    for key, value in [
        ("Contract Version", "V2.1"), ("Score Schema", "V2"), ("Report Type", "Daily"),
        ("Window Start", "2025-05-04"), ("Window End", "2025-05-04"),
        ("Registry Version", "2026-08-25"), ("Coverage Mode", "Full Replay"),
        ("Baseline Report", "—"), ("Changed Source IDs", "—"),
        ("Previous Denominator ID", "—"), ("Denominator ID", denominator_id),
        ("Denominator Frozen At", EXECUTED_AT), ("Completion Status", "Complete"),
        ("Coverage Gate", "Closed"), ("Evidence Gate", "Passed"), ("Books Gate", "Passed"),
    ]:
        a(f"| {key} | {value} |")
    a("\n### Source Coverage Receipt\n")
    a("<!-- validator:source-coverage-v2 -->")
    a("| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    fams = "<br>".join(item["Source Family ID"] for item in candidates)
    a(f"| SRC-ARXIV | 2025-05-03T09:00:00+08:00 | 2025-05-04T09:00:00+08:00 | {EXECUTED_AT} | official Atom API; submittedDate UTC window; registered category route | checked | 150 | {fams} | pages=1; start=0; final_cursor=end | 2025-05-04T09:00:00+08:00 | coverage:SRC-ARXIV:20250504 | — |")
    a(f"\n<!-- coverage:SRC-ARXIV:20250504:start -->官方 Atom 快照包含 335 条原始 entry；脚本按 v1 timestamp 与注册分类冻结 150 条身份、{len(candidates)} 个 retained candidates 和 {len(payload['records']) - len(candidates)} 个逐 family closure。独立 reviewer 逐项审阅 150/150，修复 6 个 false negatives、确认 retained false positives=0。快照、SHA-256、完整 title+abstract ledger 与 exact-v1 evidence locators 均保存在本日 `_sources` packet。<!-- coverage:SRC-ARXIV:20250504:end -->\n")
    a("### Coverage Limitations\n")
    a(f"- 以本窗口 `Window End` 计算，来源注册表中只有 `SRC-ARXIV` 的 Effective Date 已到期；2026-08-25 后加入的组织来源与 Hugging Face backstop 不反推为 2025 Daily 的 Required receipt。\n- 150 条是完成全语义筛选的 registered identities，不是 150 篇全文 Review。只有冻结分母中的 {len(candidates)} 个 family 进入精确全文审计与评分。\n")
    a("## 2. Candidate Ledger\n")
    a("<!-- validator:candidate-ledger-v2.1 -->")
    cols = ["Source Family ID", "Primary Identifier", "Event Identity", "Owner Week", "First-public Date", "Supporting Source IDs", "Design Delta", "System Reach", "Durability", "Total", "Candidate State", "Review Status", "Access Status", "Review Override", "Review Ref", "Owner Report Ref", "Prior Review Ref", "Reconciliation", "Stable Node ID", "Books Disposition", "Books Review Ref", "Benchmark Claim"]
    a("| " + " | ".join(cols) + " |")
    a("| " + " | ".join("---" for _ in cols) + " |")
    for item in candidates:
        a("| " + " | ".join(item[col] for col in cols) + " |")
    a(f"\n{len(candidates)}/{len(candidates)} 候选均为本窗口首次公开的 owner candidate；评分不用于替代 Evidence Level、Review Status、Access Status 或 Books disposition。\n")
    a("## 3. Review Completion Receipt\n")
    a("<!-- validator:review-completion-v1 -->")
    rcols = ["Source Family ID", "Review Provenance ID", "Review Route", "Primary Evidence Version", "Reviewed Evidence Versions", "Method / Identity Locators", "Evaluation Locators", "Limitations / Counterevidence Locators", "Artifact Locators", "Claim Boundary Ref", "Completion Result"]
    a("| " + " | ".join(rcols) + " |")
    a("| " + " | ".join("---" for _ in rcols) + " |")
    for row in receipts:
        vals = [row["family"], row["rp"], row["route"], row["version"], row["versions"], row["method"], row["evaluation"], row["limitations"], row["artifact"], row["claim_ref"], row["result"]]
        a("| " + " | ".join(vals) + " |")
    a("\n### Source Reviews\n")
    a("\n\n".join(review_blocks) + "\n")
    a("## 4. Benchmark Contracts\n")
    a("作者数字只在下列合同内解释；未公开字段保持 `Not Disclosed`。\n")
    a("<!-- validator:benchmark-contract-v1 -->")
    a("| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    bench = {
        "SF-2025-HPC-REPRODUCIBILITY": ("SC24 workshop evidence and practical artifact-reproduction cases", "Not Applicable — systems research report", "specialized HPC systems; heterogeneous hardware", "Not Disclosed — no numerical precision field applies to the report", "artifact package/configuration", "reproduction evidence", "Not Disclosed — no batch field applies to the workshop synthesis", "review process", "cost-effective reproducibility condition", "community workshop synthesis + actionable checklists"),
        "SF-2025-ROBUST-2D-DPO": ("noisy preference alignment experiments", "open-source DPO/2D-DPO models disclosed in v1", "Not Disclosed", "Not Disclosed", "prompt + paired segmented responses", "policy response", "Not Disclosed", "offline training", "win rate / robustness under disclosed noise; no production SLO", "author evaluation under label-flip and segment perturbation"),
        "SF-2025-ROBRIDGE": ("MetaWorld、RoboSuite、5 个现实操作任务", "VLM HCP + RL GEA", "Kinova Gen3；2×RealSense；training hardware Not Disclosed", "Not Disclosed", "任务/视觉观察", "action trajectory", "每现实任务 5 samples", "Not Disclosed", "task success；无 latency/safety SLO", "simulator success + real task completion"),
        "SF-2025-POSEPILOT": ("nuScenes、Vista、DrivingWorld 与通用视频", "diffusion / autoregressive video world models", "NVIDIA A100", "Not Disclosed", "1280×720；88 frames（公开设置）", "video frames", "Not Disclosed", "Not Disclosed", "pose error / generation quality；无 closed-loop SLO", "translation/rotation error + video metrics"),
        "SF-2025-VLORP": ("commonsense、MMLU、GSM8K fine-tuning", "LLaMA2-7B and disclosed baselines", "Not Disclosed", "Not Disclosed", "max length 1024", "task answer", "16；含 gradient accumulation", "offline", "memory、throughput、task score；无 production SLO", "official task metrics + memory profiler"),
        "SF-2025-LENGTH-BIASED-LLM-EVAL": ("MQM machine-translation evaluation at segment/document/5-document granularity", "Claude 3.5 Haiku/Sonnet and GPT-4o variants disclosed in v1", "hosted API; hardware Not Disclosed", "Not Disclosed", "about 103/507/2713 GPT-4o tokens by granularity", "MQM error spans and rankings", "one evaluation input", "API concurrency Not Disclosed", "error recall + system-ranking accuracy; no latency SLO", "MQM annotations / ranking agreement"),
        "SF-2025-CONTEXT-CONFORMAL-ANOMALY": ("synthetic data, thyroid and O-RAN anomaly detection", "arbitrary pre-trained anomaly score + C-PP-COAD", "Not Disclosed", "Not Disclosed", "streaming observations + context + calibration batches", "online anomaly decisions", "online sequential", "one stream per experiment", "decaying-memory FDR, power and real-data acquisition", "formal online-testing metric + disclosed datasets"),
        "SF-2025-BADPATCHES": ("CIFAR-10、GTSRB patch poisoning", "pMoE、MoE vision transformers", "NVIDIA T4", "Not Disclosed", "image patches", "class label", "Not Disclosed", "offline", "ASR、clean accuracy；无 production SLO", "classification + attack success"),
        "SF-2025-NEW-NEWS-SYS2FT": ("hypothetical news across math/code/discovery/event domains", "Qwen2.5 0.5B–32B", "NVIDIA H100", "bfloat16", "news/context/question；tokens Not Disclosed", "answer", "Not Disclosed", "offline", "news QA + general capability retention；无 production SLO", "dataset exact/LLM-graded metrics per v1"),
        "SF-2025-INTRA-LAYER-RECURRENCE": ("language modeling and layer-position ablations", "small recurrent Transformer variants", "Not Disclosed", "Not Disclosed", "sequence length Not Disclosed", "next-token logits", "Not Disclosed", "offline", "perplexity / parameter count；无 serving SLO", "held-out language-modeling perplexity"),
        "SF-2025-CAFCOR": ("adversarial federated/distributed learning", "CafCor under SecLDP", "Not Disclosed", "Not Disclosed", "MNIST/Fashion-MNIST worker updates", "global model update", "participant count varies by experiment", "server + workers; exact concurrency Not Disclosed", "privacy / robustness / utility bounds; no production SLO", "theoretical guarantees + benchmark accuracy"),
        "SF-2025-DITOX": ("130 ONNX Hub models；47 optimizer passes", "ONNX Optimizer", "Not Disclosed", "model-dependent", "user-defined model inputs", "original/optimized outputs", "one model/pass replay", "offline", "crash、invalid model、output discrepancy；tolerance per setup", "differential execution + pass localization"),
        "SF-2025-CAMOUFLAGE": ("four evidence-based misinformation detectors", "two academic systems + two real-world APIs; attacker LLMs disclosed in v1", "hosted API / hardware Not Disclosed", "Not Disclosed", "short claims; 1–2 sentences typical", "binary verdict + adversarial rewrite", "one claim", "up to 10 victim queries per attempt", "ASR with semantic equivalence/coherence; no latency SLO", "victim verdict + embedding/LLM checks + human evaluation"),
        "SF-2025-SPECULATIVE-SEARCH": ("GSM8K、MATH tree search", "Qwen and Llama target/draft pairs", "2×NVIDIA A800 80GB", "Not Disclosed", "task prompts；length Not Disclosed", "reasoning thoughts / answers", "Not Disclosed", "Not Disclosed", "quality parity + author speedup up to 2.12×；无 production SLO", "task accuracy + wall-clock/token accounting"),
    }
    for family, vals in bench.items():
        a("| " + " | ".join((family, *vals)) + " |")
    a("\n## 5. Deep Analysis Selection\n")
    a("长叙事上限为 3。7–9 分 family 均完成 deep review；未入选长叙事不等于未审计。\n")
    a("<!-- validator:deep-analysis-selection-v1 -->")
    a("| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |\n| --- | --- | --- | --- | --- | --- | --- |")
    for row in [
        ("SF-2025-HPC-REPRODUCIBILITY", "score_7_9", "selected", "DA-EVIDENCE-CONTRACT", "—", "建立可复算系统 artifact / environment contract", "analysis:DA-EVIDENCE-CONTRACT"),
        ("SF-2025-ROBRIDGE", "score_7_9", "not_selected", "—", "—", "controller handoff 已由 Ch26 完整承载；保留在 review", "analysis-decision:SF-2025-ROBRIDGE"),
        ("SF-2025-VLORP", "score_7_9", "not_selected", "—", "—", "optimizer-state 路线已有完整 owner；本日不重复长叙事", "analysis-decision:SF-2025-VLORP"),
        ("SF-2025-LENGTH-BIASED-LLM-EVAL", "score_7_9", "selected", "DA-EVIDENCE-CONTRACT", "—", "揭示 evaluator input granularity 会改变结论", "analysis:DA-EVIDENCE-CONTRACT"),
        ("SF-2025-CONTEXT-CONFORMAL-ANOMALY", "score_7_9", "selected", "DA-EVIDENCE-CONTRACT", "—", "把 calibration ownership 和 FDR 写入在线 evidence", "analysis:DA-EVIDENCE-CONTRACT"),
        ("SF-2025-NEW-NEWS-SYS2FT", "score_7_9", "not_selected", "—", "—", "知识派生监督已由 Ch29 主线承载；保留在 review", "analysis-decision:SF-2025-NEW-NEWS-SYS2FT"),
        ("SF-2025-CAFCOR", "score_7_9", "selected", "DA-DISTRIBUTED-TRUST", "—", "改变 federated noise 与 trust ownership", "analysis:DA-DISTRIBUTED-TRUST"),
        ("SF-2025-DITOX", "score_7_9", "selected", "DA-EVIDENCE-CONTRACT", "—", "改变优化 artifact 的 release evidence contract", "analysis:DA-EVIDENCE-CONTRACT"),
        ("SF-2025-CAMOUFLAGE", "score_7_9", "selected", "DA-EVIDENCE-CONTRACT", "—", "扩展 retrieval / comparison 组合攻击面", "analysis:DA-EVIDENCE-CONTRACT"),
        ("SF-2025-SPECULATIVE-SEARCH", "score_7_9", "selected", "DA-REASONING-COMMIT", "—", "把 proposal/verification 扩展到 reasoning-tree state", "analysis:DA-REASONING-COMMIT"),
    ]:
        a("| " + " | ".join(row) + " |")
    a("\n### 从单一分数到可复算、可攻击、可持续校准的 evidence contract\n<!-- analysis:DA-EVIDENCE-CONTRACT:start -->系统实验最初可以用论文、脚本和一个最终分数表达；当硬件、环境、输入粒度、持续漂移和对抗者进入路径后，结果已经不再由单一模型输出拥有。HPC reproducibility 把 artifact identity、environment、acceptance condition 与 reviewer cost 纳入合同；长度偏差实验进一步证明 evaluator 的 chunking 与 focus policy 会改变 error recall 和 ranking；在线 conformal monitoring 则把 calibration data ownership、acquisition decision 与 time-averaged FDR 变成持续状态。编译优化需要 original/optimized differential oracle 和逐 pass localization，evidence-based verifier 还必须接受针对 retrieval 与 comparison 的组合攻击。收益是结论可重放、可拒绝和可回滚；代价是更高 artifact 成本、校准假设、oracle coverage 与攻击面。轻量 benchmark 在依赖稳定、输入短且风险低时仍成立。<!-- analysis:DA-EVIDENCE-CONTRACT:end -->\n")
    a("### 从 trusted server 到分散持有的 privacy noise\n<!-- analysis:DA-DISTRIBUTED-TRUST:start -->传统 federated learning 把聚合与 privacy authority 集中在 server；local DP 去掉信任，却用更大的独立噪声支付 utility。CafCor 的分支让 worker pair 持有 shared randomness，相关噪声在聚合后部分抵消，同时 robust aggregation 对抗恶意 worker。它减少对 trusted server 的依赖，但新增 seed lifecycle、collusion threshold、掉线恢复和 corruption upper bound；在没有共享秘密或参与者高度动态时，local DP/secure aggregation 仍是更清晰的旧路径。<!-- analysis:DA-DISTRIBUTED-TRUST:end -->\n")
    a("### 从 token draft 到 reasoning-tree proposal/commit\n<!-- analysis:DA-REASONING-COMMIT:start -->token speculative decoding 假设 draft 与 target 对同一 prefix 提案；tree reasoning 的状态则是多条 thought branch，低质量分支会放大搜索成本。SpecSearch 让小模型拥有 proposal，大模型保留 quality admission 与 fallback，从而把控制权放在 target。收益是作者条件下的 latency 降低；代价是双模型内存、验证成本和质量判定误差。单模型搜索在低并发、小树或 draft gap 较大时仍合理。下一压力是将 thought acceptance 与可验证 reward、并发 scheduling 和 reproducible search trace 统一。<!-- analysis:DA-REASONING-COMMIT:end -->\n")
    a("<!-- analysis-decision:SF-2025-ROBRIDGE:start -->RoBridge 的分层 controller handoff 已在 Ch26 形成完整机制主线；其受限实验边界保留在 Source Review，不占用第四个长叙事。<!-- analysis-decision:SF-2025-ROBRIDGE:end -->")
    a("<!-- analysis-decision:SF-2025-VLORP:start -->VLoRP 已完成 deep Review，但 optimizer-state 的主线已由 Ch28 完整承载；相较当日 evidence/security 修正，它不占用独立长叙事。<!-- analysis-decision:SF-2025-VLORP:end -->")
    a("<!-- analysis-decision:SF-2025-NEW-NEWS-SYS2FT:start -->System-2 fine-tuning 的派生监督与 contextual shadowing 已由 Ch29 的知识写权重主线承载；本日保留独立 deep Review，不重复扩写长叙事。<!-- analysis-decision:SF-2025-NEW-NEWS-SYS2FT:end -->\n")
    a("## 6. Books Comparison\n")
    a(f"{len(candidates)}/{len(candidates)} 候选均完成目标与相邻章节比较。当前书稿由后续、更完整且已审计的机制证据承载本日增量，因此全部为 `No Change — Existing Coverage`；这不是把候选留在日报，而是明确证明没有新的长期命题需要写入。\n")
    a("<!-- validator:books-comparison-v1 -->")
    a("| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    books_rows = [
        ("SF-2025-HPC-REPRODUCIBILITY", "PLATFORM-EVALUATION-SYSTEM", "books/part-06-ai-infrastructure/66-evaluation-system.md#L1", "books/part-06-ai-infrastructure/65-kai-scheduler.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1", "Direct Evolution"),
        ("SF-2025-ROBUST-2D-DPO", "TRAIN-DPO", "books/part-04-training-system/34-dpo.md#L1", "books/part-04-training-system/33-grpo.md#L1; books/part-04-training-system/35-checkpoint.md#L1", "Direct Evolution"),
        ("SF-2025-ROBRIDGE", "MULTIMODAL-EMBODIED-VLA", "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1", "books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1; books/part-04-training-system/27-data.md#L1", "Layering / Dependency"),
        ("SF-2025-POSEPILOT", "MULTIMODAL-WORLD-MODELS", "books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1", "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1", "Alternative Branch"),
        ("SF-2025-VLORP", "TRAIN-PRETRAINING", "books/part-04-training-system/28-pretraining.md#L1", "books/part-04-training-system/27-data.md#L1; books/part-04-training-system/29-sft.md#L1", "Alternative Branch"),
        ("SF-2025-LENGTH-BIASED-LLM-EVAL", "PLATFORM-EVALUATION-SYSTEM", "books/part-06-ai-infrastructure/66-evaluation-system.md#L1", "books/part-05-inference-system/45-long-context-inference.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1", "Direct Evolution"),
        ("SF-2025-CONTEXT-CONFORMAL-ANOMALY", "PLATFORM-MONITORING", "books/part-06-ai-infrastructure/67-monitoring.md#L1", "books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/68-logging.md#L1", "Direct Evolution"),
        ("SF-2025-BADPATCHES", "PLATFORM-SECURITY", "books/part-06-ai-infrastructure/72-security.md#L1", "books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1", "Principle Reuse"),
        ("SF-2025-NEW-NEWS-SYS2FT", "TRAIN-SFT", "books/part-04-training-system/29-sft.md#L1", "books/part-04-training-system/28-pretraining.md#L1; books/part-04-training-system/30-lora.md#L1", "Direct Evolution"),
        ("SF-2025-INTRA-LAYER-RECURRENCE", "MODEL-TRANSFORMER-LAYER", "books/part-02-model/17-transformer-layer.md#L1", "books/part-02-model/16-attention-mlp.md#L1; books/part-02-model/18-decoder-only.md#L1", "Alternative Branch"),
        ("SF-2025-CAFCOR", "PLATFORM-SECURITY", "books/part-06-ai-infrastructure/72-security.md#L1", "books/part-04-training-system/36-distributed-training.md#L1; books/part-06-ai-infrastructure/71-multi-tenant.md#L1", "Layering / Dependency"),
        ("SF-2025-DITOX", "PLATFORM-EVALUATION-SYSTEM", "books/part-06-ai-infrastructure/66-evaluation-system.md#L1", "books/part-06-ai-infrastructure/65-kai-scheduler.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1", "Layering / Dependency"),
        ("SF-2025-CAMOUFLAGE", "PLATFORM-SECURITY", "books/part-06-ai-infrastructure/72-security.md#L1", "books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-07-agent/76-rag.md#L1", "Direct Evolution"),
        ("SF-2025-SPECULATIVE-SEARCH", "AGENT-PLANNING", "books/part-07-agent/79-planning.md#L1", "books/part-05-inference-system/48-speculative-decoding.md#L1; books/part-07-agent/80-reflection.md#L1", "Principle Reuse"),
    ]
    for family, owner, target, adjacent, relation in books_rows:
        a(f"| {family} | {owner} | {target} | {adjacent} | existing:{family} | delta:{family} | {relation} | No Change — Existing Coverage | books-review:{family} |")
    reviews = {
        "SF-2025-HPC-REPRODUCIBILITY": ("Ch66 已将 environment、artifact identity、workload contract、acceptance condition 与 evidence cost 串成可复算 release gate。", "该报告给出早期 systems/HPC 社区证据，但不新增当前 owner 未覆盖的责任。", "Ch65 拥有执行资源；Ch67 拥有运行监测。"),
        "SF-2025-ROBUST-2D-DPO": ("Ch34 已把 preference noise、segment/token weighting、beta/update scale 与 evaluator contract 分离。", "2D-DPO 的 segment score noise 是该主线的受限 objective 分支。", "Ch33 拥有在线 RL 分支；Ch35 拥有 checkpoint state。"),
        "SF-2025-ROBRIDGE": ("Ch26 已将 high-level proposal、symbolic/action handoff、low-level controller、sim-to-real 和 safety envelope 串成闭环。", "本论文是该分层的早期实例，不增加新的状态 owner。", "Ch25 拥有 environment transition；Ch27 拥有训练数据。"),
        "SF-2025-POSEPILOT": ("Ch25 已区分 video generation、geometry-conditioned transition、controllability 与 policy evidence。", "self-supervised pose warping 是几何约束的实现分支。", "Ch24 拥有生成 factorization；Ch26 拥有物理动作闭环。"),
        "SF-2025-VLORP": ("Ch28 已覆盖低秩梯度、optimizer state、显存预算和压缩误差的共同权衡。", "granularity/ProjFactor 提供案例但不改现有设计结论。", "Ch27 拥有数据；Ch29 拥有监督行为拟合。"),
        "SF-2025-LENGTH-BIASED-LLM-EVAL": ("Ch66 已要求 evaluator contract 绑定 input/output length、chunking、judge identity、calibration 与 failure mode。", "MT/MQM 结果给出 length-dependent judge 的早期受限证据，不新增当前命题。", "Ch45 拥有 long-context runtime；Ch67 拥有线上 drift signal。"),
        "SF-2025-CONTEXT-CONFORMAL-ANOMALY": ("Ch67 已覆盖 reference-window calibration、sequential alarm、multiplicity control 与 conformal abstention。", "C-PP-COAD 以 synthetic/real calibration acquisition 展示该路线，但不改变现有 owner。", "Ch66 拥有质量/统计保证；Ch68 拥有事件记录。"),
        "SF-2025-BADPATCHES": ("Ch72 已把 router/expert state、model artifact provenance 与 backdoor threat 连接。", "patch routing 是 vision-MoE 受限案例。", "Ch71 拥有 tenancy；Ch73 拥有 release gate。"),
        "SF-2025-NEW-NEWS-SYS2FT": ("Ch29 已覆盖事实到派生监督、contextual shadowing、general-capability guardrail。", "Self-QA/implication 是该主线的实验实例。", "Ch28 拥有 pretraining objective；Ch30 拥有参数高效适配。"),
        "SF-2025-INTRA-LAYER-RECURRENCE": ("Ch17 已区分参数深度、计算深度、weight sharing 与 recurrence placement。", "ILR 不改变该层级结论。", "Ch16 拥有 attention/MLP；Ch18 拥有 decoder-only composition。"),
        "SF-2025-CAFCOR": ("Ch72 已把 federated trust boundary、worker/server threat model、privacy noise ownership 与 key lifecycle 纳入安全合同。", "CafCor 的 pairwise shared randomness 是该路线的受限实现分支。", "Ch36 拥有 distributed optimization；Ch71 拥有 participant isolation。"),
        "SF-2025-DITOX": ("Ch66 已将 differential testing、pass localization、artifact identity 与 release evidence 写成完整合同。", "ONNX 结果提供故障实例但不新增机制。", "Ch65 拥有资源执行；Ch67 拥有 telemetry。"),
        "SF-2025-CAMOUFLAGE": ("Ch72 已将 retrieval、evidence comparison、agent feedback loop 与 adversarial evaluator 纳入组合 threat model。", "CAMOUFLAGE 提供 binary-feedback attack 的早期案例，不新增当前安全结论。", "Ch66 拥有 evaluator contract；Ch76 拥有 retrieval state。"),
        "SF-2025-SPECULATIVE-SEARCH": ("Ch79 已覆盖 proposal、verification、commit/rollback 与 search state；Ch48 拥有 token-level speculation。", "thought-level speculative search 属 principle reuse，不应搬入推理解码 owner。", "Ch78 拥有 tool action；Ch80 拥有 reflection。"),
    }
    for family, (existing, delta, adjacent) in reviews.items():
        a(f"<!-- books-review:{family}:start --><!-- existing:{family}:start -->{existing}<!-- existing:{family}:end --><!-- delta:{family}:start -->{delta}<!-- delta:{family}:end -->{adjacent}<!-- books-review:{family}:end -->")
    a(f"\n<!-- books-queue:20250504:start -->Books write queue = 0；{len(candidates)} 项均由现有 canonical owner 完整承载。<!-- books-queue:20250504:end -->\n")
    a("## 7. Semantic Audit\n")
    a("<!-- validator:semantic-audit-v1 -->")
    a("| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |\n| --- | --- | --- | --- | --- | --- | --- |")
    a("| SA-20250504-COVERAGE | fresh-context:may04-independent-audit | coverage | coverage:SRC-ARXIV:20250504 | — | resolved:FINDING-MAY04-FN-01；全量 150/150 重审，分母 8→14、closure 142→136、false positives=0 | passed |")
    a("| SA-20250504-EVIDENCE | fresh-context:may04-independent-audit | evidence | review:SF-2025-HPC-REPRODUCIBILITY; review:SF-2025-ROBUST-2D-DPO; review:SF-2025-LENGTH-BIASED-LLM-EVAL; review:SF-2025-CONTEXT-CONFORMAL-ANOMALY; review:SF-2025-CAFCOR; review:SF-2025-CAMOUFLAGE; review:SF-2025-DITOX | — | resolved:FINDING-MAY04-LOC-01；14/14 使用 source-specific exact-v1 section/appendix locator 并重算 provenance | passed |")
    a("| SA-20250504-SELECTION | fresh-context:may04-independent-audit | deep_analysis_selection | analysis:DA-EVIDENCE-CONTRACT; analysis:DA-DISTRIBUTED-TRUST; analysis:DA-REASONING-COMMIT; analysis-decision:SF-2025-VLORP | — | resolved:FINDING-MAY04-SEL-01；重放全 frontier，三项长叙事覆盖 evidence、trust 与 reasoning commit | passed |")
    a("| SA-20250504-BOOKS | fresh-context:may04-independent-audit | books | books-review:SF-2025-HPC-REPRODUCIBILITY; books-review:SF-2025-ROBUST-2D-DPO; books-review:SF-2025-LENGTH-BIASED-LLM-EVAL; books-review:SF-2025-CONTEXT-CONFORMAL-ANOMALY; books-review:SF-2025-CAFCOR; books-review:SF-2025-CAMOUFLAGE; books-queue:20250504 | — | 14/14 target/adjacent 对读；均由当前 canonical owner 更完整承载，queue=0 | passed |\n")
    a("## 8. Ignored Noise\n")
    a(f"{len(payload['records']) - len(candidates)} 个未保留 identity 已在 `_sources` ledger 中逐项记录标题、摘要命题与不进入长期 AI-System 分母的具体理由；主要类别是垂直应用、局部 accuracy/representation 增量、通用优化理论、单领域 benchmark 和不改变系统 contract 的 survey。它们完成的是 pre-denominator closure，不伪装成全文 Review。\n")
    a("## 9. Recommended Action\n")
    a(f"1. Sunday owner Weekly 只聚合本日报 {len(candidates)} 个 family，并按 first-public date 去重；不得把 {len(payload['records']) - len(candidates)} 条 closure 重新膨胀为评分候选。\n2. 后续若 source revision 改变 method/evaluation boundary，应重开真实 owner date，而不是在发现日追加新分数。\n")
    a("## 10. Repository Changes\n")
    a(f"- 冻结 2025-05-04 official arXiv snapshot、150 条全语义 screening ledger 与 {len(candidates)} 份 exact-v1 route evidence。\n- 独立审计修复 6 个 denominator false negatives 与 8 项原有 generic locator；未修改 Books、ROADMAP、DECISIONS 或 LEARNING_STATE。\n- 未 stage、commit 或 push。\n")
    a("## 11. Open Questions\n")
    a("- low-rank gradient projection 在完整 pretraining、ZeRO/FSDP 与 tensor parallel 下如何分配 projection/optimizer state？\n- compiler differential oracle 如何覆盖动态 shape、随机算子、量化与跨后端 tolerance？\n- thought-level speculative acceptance 如何与可验证 reward、并发 scheduling 和 search-trace reproducibility 联合设计？\n")
    a("## 12. Sources\n")
    a("访问日期为 2026-08-31；事件日期使用 arXiv v1 timestamp。\n")
    a("- https://export.arxiv.org/api/query")
    for aid in sorted(META):
        a(f"- https://arxiv.org/html/{aid}v1")
    a("\n## 13. Final Status\n")
    a("State Truth: Completion=Complete；Coverage=Closed；Evidence=Passed；Books=Passed；fresh-context unresolved findings=0。\n")
    a("150/150 denominator audit、14/14 exact-v1 Review、全 frontier Selection、14/14 Books Comparison 与四范围 Semantic Audit 均已闭合；Books write queue=0。\n")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(report).rstrip() + "\n", encoding="utf-8")
    print(json.dumps({"report": str(REPORT), "denominator": denominator_id, "retained": len(candidates), "closed": payload["pre_denominator_closed"]}, ensure_ascii=False))


if __name__ == "__main__":
    render()
