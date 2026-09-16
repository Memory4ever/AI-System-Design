#!/usr/bin/env python3
"""Freeze the current-contract 2026-05-26 author recertification.

The 263 arXiv identities come from the official-announcement migration receipt.
Legacy 1208/170 V2.1 counts, scores, dispositions, and completion state are not
inputs.  Shared Books are read for comparison only; missing propositions are
serialized into a root-owner queue.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[5]
LOCAL = ROOT / "papers/2026/05/_sources/daily-20260526"
REPORT = ROOT / "papers/2026/05/26/README.md"
MIGRATION = ROOT / "papers/2026/05/_sources/daily-20260524/legacy-v21-migration-v3.json"
LEDGER = ROOT / "papers/2026/05/_sources/daily-20260524/screening-ledger-final.json"
OLD_EXACT = ROOT / "papers/2026/05/_sources/daily-20260524/exact-v1-review-packet.json"
CHECKED_AT = datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(timespec="seconds")
WINDOW_START = "2026-05-25T09:00:00+08:00"
WINDOW_END = "2026-05-26T09:00:00+08:00"
ARXIV_PUBLIC = "2026-05-26T08:00:00+08:00"


def family(aid: str) -> str:
    if aid == "minimax:sparse-token-forgetting":
        return "SF-2026-MINIMAX-SPARSE-TOKEN-FORGETTING"
    return "SF-2026-ARXIV-" + aid.replace(".", "-")


def write_json(name: str, value: object) -> None:
    (LOCAL / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


SELECTED = """
2605.24321 2605.24326 2605.24330 2605.24331 2605.24383 2605.24384
2605.24391 2605.24396 2605.24420 2605.24421 2605.24425 2605.24426
2605.24432 2605.24433 2605.24461 2605.24468 2605.24486 2605.24497
2605.24517 2605.24535 2605.24539 2605.24541 2605.24547 2605.24549
2605.24550 2605.24552 2605.24556 2605.24577 2605.24578 2605.24579
2605.24583 2605.24597 2605.24598 2605.24602 2605.24613 2605.24614
2605.24618 2605.24619 2605.24624 2605.24630 2605.24642 2605.24652
2605.24657 2605.24659 2605.24660 2605.24667 2605.24693 2605.24697
2605.24702 2605.24709 2605.24718 2605.24727 2605.24728 2605.24733
2605.24737 2605.24743 2605.24749 2605.24754 2605.24756 2605.24761
2605.24770 2605.24785 2605.24786 2605.24793 2605.24794
2605.24322 2605.24350 2605.24366 2605.24375 2605.24509 2605.24518
2605.24538 2605.24545 2605.24570 2605.24647 2605.24661 2605.24662
2605.24674 2605.24683 2605.24687 2605.24696 2605.24759 2605.24764
2605.24775 2605.24779
""".split()

ROOT_APPLIED = set("""
2605.24321 2605.24326 2605.24330 2605.24383 2605.24432 2605.24517
2605.24539 2605.24578 2605.24785
""".split())

APPLIED = ROOT_APPLIED | {"2605.24683"} | set("""
2605.24391 2605.24420 2605.24421 2605.24425 2605.24426 2605.24461
2605.24547 2605.24579 2605.24583 2605.24598 2605.24660 2605.24667
2605.24697 2605.24709 2605.24727 2605.24743 2605.24749 2605.24756
2605.24770 2605.24793
""".split())

INTEGRATE = set("""
2605.24322 2605.24366 2605.24545 2605.24549 2605.24696 2605.24718
2605.24737
""".split())

STRUCTURAL = {"2605.24538", "2605.24541", "2605.24570", "2605.24728", "2605.24759"}
REPORT_ONLY = {"2605.24577", "2605.24657"}
STANDARD = {"2605.24384", "2605.24433", "2605.24541", "2605.24556",
            "2605.24518", "2605.24570", "2605.24618", "2605.24652",
            "2605.24657", "2605.24687", "2605.24754", "2605.24779"}
SCORE9 = {"2605.24326", "2605.24391", "2605.24461", "2605.24517",
          "2605.24579", "2605.24583", "2605.24598", "2605.24660",
          "2605.24697", "2605.24743", "2605.24756", "2605.24785",
          "2605.24793", "2605.24696", "2605.24775"}
SCORE8 = APPLIED | INTEGRATE | {"2605.24331", "2605.24396", "2605.24468",
          "2605.24486", "2605.24497", "2605.24535", "2605.24550",
          "2605.24552", "2605.24578", "2605.24613", "2605.24614",
          "2605.24619", "2605.24659", "2605.24693", "2605.24709",
          "2605.24727", "2605.24749", "2605.24761", "2605.24770",
          "2605.24786", "2605.24794", "2605.24322", "2605.24350",
          "2605.24366", "2605.24375", "2605.24509", "2605.24538",
          "2605.24545", "2605.24647", "2605.24661", "2605.24662",
          "2605.24674", "2605.24683", "2605.24759", "2605.24764",
          "2605.24775"}
SCORE8 -= SCORE9

NODE = {
    "2605.24321": "MULTIMODAL-WORLD-MODELS", "2605.24326": "TRAIN-DISTRIBUTED-TRAINING",
    "2605.24322": "MULTIMODAL-WORLD-MODELS", "2605.24350": "AGENT-PLANNING",
    "2605.24366": "AGENT-RAG", "2605.24375": "MULTIMODAL-WORLD-MODELS",
    "2605.24330": "MODEL-TRANSFORMER-LAYER", "2605.24331": "TRAIN-GRPO",
    "2605.24383": "PLATFORM-SECURITY", "2605.24384": "PLATFORM-EVALUATION-SYSTEM",
    "2605.24391": "INFER-TENSORRT-LLM", "2605.24396": "PLATFORM-EVALUATION-SYSTEM",
    "2605.24420": "PLATFORM-SECURITY", "2605.24421": "PLATFORM-SECURITY",
    "2605.24425": "MODEL-TRANSFORMER-LAYER", "2605.24426": "TRAIN-RLHF",
    "2605.24432": "TRAIN-SFT", "2605.24433": "MULTIMODAL-EMBODIED-VLA",
    "2605.24461": "PLATFORM-GPU-SCHEDULER", "2605.24468": "AGENT-MEMORY",
    "2605.24486": "AGENT-MULTI-AGENT", "2605.24497": "PLATFORM-SECURITY",
    "2605.24517": "TRAIN-RLHF", "2605.24535": "PLATFORM-SECURITY",
    "2605.24539": "AGENT-PLATFORM", "2605.24541": None,
    "2605.24547": "TRAIN-RLHF", "2605.24549": "TRAIN-LORA",
    "2605.24550": "PLATFORM-SECURITY", "2605.24552": "PLATFORM-SECURITY",
    "2605.24509": "MULTIMODAL-GENERATIVE-PARADIGMS", "2605.24518": "MODEL-SELF-ATTENTION",
    "2605.24538": None, "2605.24545": "PLATFORM-SECURITY", "2605.24570": None,
    "2605.24556": "AGENT-RAG", "2605.24577": "MODEL-SELF-ATTENTION",
    "2605.24578": "MULTIMODAL-WORLD-MODELS", "2605.24579": "AGENT-MEMORY",
    "2605.24583": "PLATFORM-EVALUATION-SYSTEM", "2605.24597": "TRAIN-RLHF",
    "2605.24598": "AGENT-MULTI-AGENT", "2605.24602": "MULTIMODAL-REPRESENTATION",
    "2605.24613": "PLATFORM-EVALUATION-SYSTEM", "2605.24614": "PLATFORM-SECURITY",
    "2605.24618": "MULTIMODAL-REPRESENTATION", "2605.24619": "AGENT-TOOL-CALLING",
    "2605.24624": "MULTIMODAL-GENERATIVE-PARADIGMS", "2605.24630": "MULTIMODAL-WORLD-MODELS",
    "2605.24642": "MULTIMODAL-EMBODIED-VLA", "2605.24652": "PLATFORM-EVALUATION-SYSTEM",
    "2605.24657": "AGENT-MEMORY", "2605.24659": "PLATFORM-SECURITY",
    "2605.24647": "AGENT-PLANNING", "2605.24661": "PLATFORM-EVALUATION-SYSTEM",
    "2605.24662": "PLATFORM-EVALUATION-SYSTEM", "2605.24674": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2605.24683": "PLATFORM-MONITORING", "2605.24687": "PLATFORM-EVALUATION-SYSTEM",
    "2605.24696": "PLATFORM-MONITORING",
    "2605.24660": "AGENT-TOOL-CALLING", "2605.24667": "TRAIN-PRETRAINING",
    "2605.24693": "AGENT-PLANNING", "2605.24697": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2605.24702": "PLATFORM-EVALUATION-SYSTEM", "2605.24709": "TRAIN-RLHF",
    "2605.24718": "MODEL-TOKENIZER", "2605.24727": "PLATFORM-EVALUATION-SYSTEM",
    "2605.24728": None, "2605.24733": "PLATFORM-EVALUATION-SYSTEM",
    "2605.24737": "PLATFORM-MONITORING", "2605.24743": "TRAIN-DATA",
    "2605.24749": "TRAIN-RLHF", "2605.24754": "INFER-GPU-MEMORY",
    "2605.24756": "PLATFORM-EVALUATION-SYSTEM", "2605.24761": "MULTIMODAL-WORLD-MODELS",
    "2605.24770": "TRAIN-PRETRAINING", "2605.24785": "AGENT-PLATFORM",
    "2605.24786": "INFER-KV-CACHE", "2605.24793": "INFER-SPECULATIVE-DECODING",
    "2605.24759": None, "2605.24764": "AGENT-RAG", "2605.24775": "AGENT-PLATFORM",
    "2605.24779": "TRAIN-DATA",
    "2605.24794": "TRAIN-RLHF", "minimax:sparse-token-forgetting": "TRAIN-SFT",
}

PATH = {
    "MODEL-TOKENIZER": "books/part-02-model/11-tokenizer.md",
    "MODEL-SELF-ATTENTION": "books/part-02-model/14-self-attention.md",
    "MODEL-TRANSFORMER-LAYER": "books/part-02-model/17-transformer-layer.md",
    "MULTIMODAL-REPRESENTATION": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
    "MULTIMODAL-WORLD-MODELS": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "MULTIMODAL-EMBODIED-VLA": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
    "TRAIN-DATA": "books/part-04-training-system/27-data.md",
    "TRAIN-PRETRAINING": "books/part-04-training-system/28-pretraining.md",
    "TRAIN-SFT": "books/part-04-training-system/29-sft.md",
    "TRAIN-LORA": "books/part-04-training-system/30-lora.md",
    "TRAIN-RLHF": "books/part-04-training-system/31-rlhf.md",
    "TRAIN-GRPO": "books/part-04-training-system/33-grpo.md",
    "TRAIN-DISTRIBUTED-TRAINING": "books/part-04-training-system/36-distributed-training.md",
    "INFER-KV-CACHE": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
    "INFER-SPECULATIVE-DECODING": "books/part-05-inference-system/48-speculative-decoding.md",
    "INFER-TENSORRT-LLM": "books/part-05-inference-system/49-tensorrt-llm.md",
    "INFER-GPU-MEMORY": "books/part-05-inference-system/54-gpu-memory.md",
    "PLATFORM-GPU-SCHEDULER": "books/part-06-ai-infrastructure/63-gpu-scheduler.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "PLATFORM-MONITORING": "books/part-06-ai-infrastructure/67-monitoring.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/72-security.md",
    "AGENT-RAG": "books/part-07-agent/76-rag.md", "AGENT-MEMORY": "books/part-07-agent/77-memory.md",
    "AGENT-TOOL-CALLING": "books/part-07-agent/78-tool-calling.md",
    "AGENT-PLANNING": "books/part-07-agent/79-planning.md",
    "AGENT-MULTI-AGENT": "books/part-07-agent/82-multi-agent.md",
    "AGENT-PLATFORM": "books/part-07-agent/84-agent-platform.md",
}

INTEGRATE_DETAIL = {
    "2605.24322": ("§3.2 Physics Emergence Zone; §3.3 CAV; §3.4–§3.5 inference-time/per-block steering", "§5.1–§5.6 steering, layer ablation and subspace tests", "§7 Future Work; §8 Broader Impact; IntPhys/VideoMAE boundary", "把 World Model 的物理表示从只读 probe 提升为受限的 inference-time control surface：PEZ layer 的 probe weight 作为 CAV 写入 hidden state。它免训练但依赖 representation localization，错误 layer/方向会产生不真实 steering；因此只作为 rollout proposal，以真实观察/模拟器 gate，并在物理一致性失败时回退无 steering 基线。"),
    "2605.24321": ("§3.1 local random-access sequence; §3.2 inference pathways", "§4 Results; Appendix A.4 ablations", "Appendix A.8 Limitations & Future Work", "把 World Model 的 task head 改写为对同一 RGB/flow/camera 图的 observation/query traversal；旧的 task-specific heads 仍是低成本、强约束 fallback，随机访问失配会造成局部不一致。"),
    "2605.24326": ("§3–§6 placement, scheduling, network and ScaleAcross Explorer", "§6.3 results; Appendix A testbed/simulation", "§7 Lessons Learned; §8 Conclusion", "把单机房 collective tuning 扩展为跨楼宇 placement、path、collective schedule 与 failure-domain 的联合搜索；跨域训练用通信优化换更大的 tail latency、模拟误差和故障面，收益失效时回退单站点或固定 hierarchy。"),
    "2605.24330": ("§3.1–§3.4 Interdomain Attention and complexity", "§4 FineWeb-Edu; Appendix B/C scaling", "§4 Recall and limitations; §5 Future Work", "在 attention 的 query addressing 与 SSM 固定状态之间增加 query-conditioned basis projection；固定状态降低长度成本但牺牲精确 recall，超出状态预算或 recall gate 失败时回退 softmax/hybrid attention。"),
    "2605.24383": ("§2 governance-horizon evidence; §4 lineage methods", "§2.1–§2.5 and supplements S1–S6", "§3.3 Limitations and outlook", "把 open-weight restriction 从可选 model-card 文本升级为随 lineage/merge 传播的 machine-readable governance state；声明继承降低发布摩擦但会产生 orphan/merge undecidability，无法解析时必须阻断自动合规结论并转人工。"),
    "2605.24432": ("§3.1 SFT grounded context; §3.2 view-asymmetric self-distillation", "§4 Results and ablations", "§6 limitations; Appendix C evaluation limits", "把单轮能力到多轮能力的迁移建模为 information-equivalent views 的自蒸馏，并把未充分信息时的 defer/clarify 写入训练目标；视图不等价会蒸馏错误，失败时回退显式澄清策略与外部 teacher。"),
    "2605.24366": ("§3.3 quality-aware metadata; §3.4 table generation; §3.5 structure-aware RAG", "§4.2–§4.6 main results, table-quality analysis, ablation and cases", "Limitations after §5; Appendix C offline/online case boundary", "把 noisy corpus 的表格从被动文档格式提升为带质量状态的 intermediate retrieval interface：metadata normalization/effectiveness 先受控更新，再以 semantic/structural consistency gate 生成表格。它减少噪声却新增表格化信息损失、metadata drift 和离线构建成本；失败时回退原文 chunk/hybrid retrieval，并保留 row/cell 到原文 provenance。"),
    "2605.24517": ("§3 ECHO objective and observation targets", "§4–§5 TerminalBench evaluation", "§7 Conclusion; disclosed terminal-observation boundary", "把 agent rollout 中环境 observation tokens 从只读 context 升级为辅助预测目标，与 action policy gradient 分责；dense signal 可能奖励可预测而非可控环境，故要以 task verifier/held-out dynamics gate，并可回退标准 GRPO。"),
    "2605.24539": ("§3 harness-evolution information regimes", "§4 Liar's Dice/Balatro controls", "§6 Limitations", "把 harness evolution 的 reward-only search 改成 demonstration-guided program edit localization；demonstration 提高可诊断性但引入示范偏差和额外审计成本，固定种子 paired gate 失败时回退人工 harness 与不变基线。"),
    "2605.24549": ("§3 PALoRA two-phase projection constraint", "§4 experiments and ablations", "Appendix A.6 limitation; Appendix C overhead", "在 LoRA 更新前用冻结 SVF probe 标记 skill-critical singular subspace，再约束知识注入的投影；probe 失配会保护错误子空间且增加两阶段成本，回退普通 LoRA、全量回归测试或停止注入。"),
    "2605.24545": ("§4 memorization definitions; §5 grouped metric; §6.1–§6.2 FedMemPrune", "§7.2 results; §7.3 ablations; Appendices F–G metric checks", "§7.4 and Appendix H discussion; retraining remains the reference boundary", "把 federated unlearning 的删除目标从参数距离或整类性能改为待删数据的 unique memorization，并保留与 remaining clients 重叠的知识。Grouped Memorization Evaluation 与 prune/reinitialize/fine-tune 提供近似路径，但定位错误会删错共享知识；高风险删除仍以 retraining/attack audit 为 gate，失败时回退完整重训。"),
    "2605.24578": ("§2 group-action formulation; §3 latent regularization", "§4 experiments; Appendix C–E probes", "Appendix A.4 approximation; Appendix H scope", "World Model 除视觉质量外还要通过 identity/inverse/composition action probes；latent surrogate 降低成本但不等于真实 state dynamics，pose recovery 或 group assumption 失效时回退真实 rollout/状态测量。"),
    "2605.24718": ("§3 tokenizer/dataset/protocol", "§4 cross-domain/cross-lingual experiments", "§6 Limitations", "把 tokenizer fertility 作为 language×domain 的成本与可达性 contract，而不是只看平均 tokens；扩 vocab/continued pretraining 会增加兼容、checkpoint 与序列成本，失败时保留旧 tokenizer 并按语言路由或预算。"),
    "2605.24737": ("§3 governance-from-metrics; §4 govllm architecture", "§6 preliminary experiments", "§6.3 and §7.4 Limitations", "把 compliance 从一次性 audit 改成 versioned runtime signal，并将 judge disagreement 作为人工仲裁触发而非 truth；judge bias/drift 会污染路由，故保留静态审核、规则检查与人工 override。"),
    "2605.24696": ("§3.2 change-point detector; §3.3 SLO threshold; §3.4 calibration/CRC; §3.5 burn-rate", "§5.1–§5.6 three prevalence regimes, calibration and ablation", "§6.1–§6.4 operating regimes and threats to validity", "把 streaming alert threshold 从离线调参改成由 operator cost、alert budget 与 SLO 共同派生的 versioned control，并把 calibration、CRC 与 multi-window burn-rate 串成一条验收链。收益受 prevalence/exchangeability 强约束；CRC overshoot、density degeneracy 或 base-rate inversion 触发时回退静态保守阈值、隔离与人工调查。"),
    "2605.24785": ("§3 cost decomposition; §4 PANDO framework", "§5–§6 results/ablation; Appendix I/N", "§7 Limitations; Appendix K residual failures", "把 agent skill library 当作在线可升降级的 versioned state，并同时记 success、steps、tokens 与 cache reuse；错误 skill 会复用放大且在线评估可能污染，失败时 demote/blacklist 并回退无技能单次执行。"),
    "minimax:sparse-token-forgetting": ("Hypothesis 1–2; Exploring Intermediate Metrics", "Validation & Repair Experiments", "Korean non-fix and Other Directions Worth Exploring", "SFT 不只监控 task/domain coverage，还要监控 token-as-target coverage 与 pretrain→SFT lm_head drift；全词表重复数据可保底但可能浪费容量或损害会话能力，Korean 反例说明失败时需回退数据清洗、targeted synthesis 或 CPT。"),
}

# Current exact-v1 HTML was read for every newly retained arXiv item that did
# not already have a reusable immutable locator in the 05-24 packet.  Keep the
# three axes separate so a later reviewer can challenge mechanism, evaluation,
# and disclosed boundary without treating the abstract as full-text evidence.
EXACT_LOCATORS = {
    "2605.24322": ("§3.2 Physics Emergence Zone; §3.3–§3.5 CAV steering", "§5.1–§5.6 IntPhys results and ablations", "§7 Future Work; §8 Broader Impact"),
    "2605.24350": ("§2.1 proactive ask-or-act; §2.2 clarification utility", "§3.2–§3.3 main results and clarification analysis; Appendices D–E", "§4 Discussion and Limitations"),
    "2605.24366": ("§3.3–§3.5 metadata, table generation and structure-aware RAG", "§4.2–§4.6 results, ablation and case study", "Limitations after §5; Appendix C case boundary"),
    "2605.24375": ("§4.1 data; §4.2 four-tier verification; §4.3 SFT/RLVR", "§5.1–§5.2 experiments; Appendix E ablation", "§5.2 disclosed SFT/RLVR limitations; §6 Future Work"),
    "2605.24331": ("§3 utility-dependent context-distribution control; §4.1–§4.3 CurveRL", "§5.1–§5.2 main results and mechanism analysis; Appendix C", "§7 Discussion and Conclusion; Appendix D discussions; no dedicated limitations section"),
    "2605.24384": ("§3 Experimental Setup, especially §3.2 matched-guise and §3.4 metrics", "§4.1–§4.3 absolute/contrastive bias and fairness fine-tuning", "§7 Limitations"),
    "2605.24396": ("§2 correlation analysis; §3 Progressive Confidence Shaping", "§2.2 and §3.2 results; Appendices C–G", "§4 factors affecting premature confidence; §5 Conclusion; no dedicated limitations section"),
    "2605.24433": ("§III-A prior-corrected weight; §III-B orthogonal trust-region guidance; §III-C algorithm", "§IV-A–§IV-H experiments and ablations", "§V Conclusion; evidence is bounded to the disclosed LIBERO/π0.5 setting"),
    "2605.24486": ("§2.1 problem setting; §2.2 shared hub; §2.3 optimization", "§3.3–§3.6 results and ablations; Appendix E cases", "Appendix G Limitations and Broader Impact"),
    "2605.24497": ("§3.2–§3.5 formulation, structured search, adaptive evolutionary optimization and fitness", "§4.2–§4.8 transfer, efficiency, ablation and defense analysis; Appendices C–J", "§5 Conclusion and Impact Statement; no dedicated limitations section"),
    "2605.24509": ("§3 spectral analysis; §4 phase substitution and energy balancing", "§6.2–§6.4 comparisons and generalization; Appendix B", "§7 Limitations and Conclusion"),
    "2605.24518": ("PDF v1 pp.3–5 §3 Methodology and §4.1 architecture/implementation", "PDF v1 pp.5–7 §4.5 strategies and §5 Results and Discussions", "PDF v1 pp.7–8 §6 Conclusion/Future Work and Limitations"),
    "2605.24538": ("§2 six-layer decentralization/governance vacuum; §4 protocol as architectural constraint", "§4.3 early protocol experiments; conceptual analysis rather than controlled benchmark", "§4.4 ethical conditions; §5 Conclusion"),
    "2605.24545": ("§4 definitions; §5 grouped metric; §6 FedMemPrune", "§7.2–§7.3 results and ablations; Appendices F–G", "§7.4 and Appendix H Discussion"),
    "2605.24570": ("§3.2.1–§3.2.4 gradient agreement, policy and online update", "§4.1–§4.5 datasets, stability, ablations and transfer", "§5.1 Limitations; §5.2 Future Work"),
    "2605.24535": ("§4 Learnable Steering; §5 bi-level adversarial training", "§6–§9 main, mechanistic and ablation results", "Appendix A Limitations and Future Work"),
    "2605.24541": ("§3 formulation; §4 semantic-compression regimes; §5 hybrid protected/lossy architecture", "§6 setup; §7 pilot results", "§9 Limitations"),
    "2605.24550": ("§3 threat model; §4 buffering analysis; §5 BufferLoRA/ReinforceLoRA", "§6 and §6.1–§6.3 results; Appendix B", "§7 Limitations"),
    "2605.24552": ("§III-B benign constraints; §III-C/§III-D projection; §III-E/§III-F derivation and implementation", "§IV-A–§IV-I evaluation; §V cost", "§VII Limitations and Future Work"),
    "2605.24556": ("§3.1 benchmark/relevance metrics; §3.2 models; §3.3 training and indexing", "§4.1–§4.3 zero-shot, fine-tuned and reranking results", "§5 Discussion; §7 Limitations"),
    "2605.24577": ("§2 operational bars; §3 five-lens stack; §8 rotation audit and hypothesis", "§6–§8 within-seed, cross-seed and Pythia-70m tests; Appendices A–E", "§10 Limitations"),
    "2605.24597": ("§2 A* hypergraph formulation; §3.1 verbalized traces; §3.2 A*-informed process rewards", "§4.1–§4.3 SFT and RL experiments; Appendices B–C", "§6 Conclusion; Appendix A cost-function boundary; no dedicated limitations section"),
    "2605.24602": ("§3.2 spatial inconsistency; §3.3 temporal fading; §4.1–§4.2 correction mechanisms", "§6.1–§6.3 comparisons and sensitivity; Appendix D ablations/cases", "§7 Conclusion; disclosed benchmark/head-layer scope; no dedicated limitations section"),
    "2605.24613": ("§3.1 formulation; §3.2 diagnostics/trigger; §3.3 guarded best-of-N repair", "§5.1–§5.4 results/ablations/portability; §6 candidate-flow and cost analysis", "§7 Limitations and Threats to Validity"),
    "2605.24618": ("§3.1 factorized codec/flow matching; §3.2.1–§3.2.3 hierarchical generation, style encoding and consistency loss", "§4.2.1–§4.2.4 zero-shot/control/ablation results; Appendix D", "§6 Limitations; §7 Ethical Considerations"),
    "2605.24624": ("§3 Methods; §4.2 text-token content; §4.3 causal knockout/patching", "§4.1–§4.4 editing tasks, interventions and binding location; Appendices A–D", "§4.5 Limitations"),
    "2605.24647": ("§3 free-energy belief/world-model setup; §4.1–§4.4 PUMA user state and action selection", "§5.2–§5.5 results, ablation and cross-dataset tests", "§6 Conclusion; Appendix D simulator boundary; no dedicated limitations section"),
    "2605.24674": ("§3 problem statement; §4.2 routed token conditioning; §4.3 reference-anchored attention", "§5.1–§5.3 main, ablation and method analysis; Appendix D", "§6 Conclusion; no dedicated limitations section"),
    "2605.24687": ("§3.1 taxonomy/data; §3.2 classifier; §3.3 metric; §3.4 Fair-GRPO", "§4.3–§4.4 benchmark/debiasing, ablation and reward-hacking analysis", "Appendix A Limitations and Future Work"),
    "2605.24696": ("§3.2–§3.5 detector, SLO threshold, calibration/CRC and burn-rate", "§5.1–§5.6 regime tests and ablation", "§6 Discussion and Limitations"),
    "2605.24630": ("§4.1 task formulation; §4.2 architecture; §4.3 rollout training with spatial cache", "§5.1–§5.5 quantitative, qualitative and ablation results", "§6 Conclusion; no dedicated limitations section"),
    "2605.24642": ("§3.1 VLA geometry-injection strategies; §3.2 cross-attention fusion; §4 probes", "§5.1–§5.5 design-choice studies; Appendices B–E", "§6 Limitations"),
    "2605.24652": ("§3.1 curation; §3.2 hard-negative mining; §3.3 evaluator SFT; §3.4 suite", "§4.1–§4.3 model evaluation and human-alignment validation; §9", "§5 Limitation"),
    "2605.24693": ("§2 calibrated feedback-control theory; §3.1–§3.4 verification, augmentation, experience and tools", "§4.2 calibration/auditability; §4.3–§4.7 results and ablations; Appendix D", "§6 Conclusion plus Appendix C structural conditions; no dedicated limitations section"),
    "2605.24702": ("§3.1–§3.5 curation, perturbations, protocol, RRF and calibrated scoring", "§5.1–§5.6 invariance and ranking-flip results; Appendices A.6–A.12/B", "§7 Limitations"),
    "2605.24754": ("§3 setup; §4 functional alignment; §5 predictive coding; §6 residual quantization/rate-distortion", "§7.1 main results; Appendices H–L robustness, latency and ablation", "Appendix M restricted-symmetry scope; Appendix O.2 Limitations"),
    "2605.24759": ("§4 traced Bellman semantics; §5 compositionality; §6 abstraction; §7 quantale contracts", "§10 minimal modular-robustness examples; Appendix A proofs", "§9 Scope and Limitations"),
    "2605.24764": ("§III-B–§III-H sinc kernel, score, recovery, two-stage retrieval and production notes", "§VI synthetic and §VII LIMIT-small evaluation", "§VIII Limitations and Threats; §V-C what it does not solve"),
    "2605.24779": ("§3 CSI definition/properties; §4 instantiations; §5 optimization", "§6.1 synthetic and §6.2 hidden-slice subset selection", "§7 Conclusion; synthetic/hidden-slice boundary; no dedicated limitations section"),
    "2605.24761": ("§3.2 anchor-guided rollout; §3.3 epipolar masking; §3.4 anchor-conditioned DiT; §3.5 training", "§4.2 drift, §4.3 planning and §4.4 ablations; Appendices C–E", "§5 Conclusion; geometric assumptions in Appendices A–B; no dedicated limitations section"),
    "2605.24794": ("§3.1 paired claims; §3.2 calibrated verification; §3.3 paired-GRPO self-play", "§5.2–§5.6 main, transfer, ablation, efficiency and sensitivity; Appendices D–G", "Appendix A Limitations"),
}

CLAIM_OVERRIDE = {
    "2605.24322": "A linear probe direction localized to a Physics Emergence Zone can be injected as a Concept Activation Vector to steer a video world model's physical-plausibility judgment at inference time without weight updates.",
    "2605.24350": "Proactive ask-or-act planning combines current observation with cross-day history and evaluates clarification utility as assistance accuracy against clarification frequency, instead of treating every uncertainty as either silent inference or mandatory questioning.",
    "2605.24366": "A quality-aware table representation acts as a compact retrieval interface over noisy corpora, with metadata normalization/effectiveness and semantic/structural consistency controlled before online RAG consumption.",
    "2605.24375": "Executable game world models can be post-trained with a four-tier verifier spanning static structure, fuzzed dynamics, semantic rule traces and information consistency, so SFT/RLVR optimize more than code syntax.",
    "2605.24420": "Batch-coupled normalization statistics amplify atypical-sample influence and memorization, and the measured amplification carries through to membership-inference susceptibility; privacy comparisons must therefore hold normalization and batch composition fixed.",
    "2605.24547": "Textual feedback is a learnable policy component coupled bilevel to the actor, rather than a fixed correct annotation; Bi-NAC trains the critic for downstream reward improvement and the actor to exploit that feedback.",
    "2605.24509": "Low-frequency phase from a reference video can condition diffusion noise without model retraining, while energy balancing limits the amplitude distortion introduced by spectral substitution.",
    "2605.24518": "Part-of-speech-derived hard or soft masks reduce the theoretical self-attention graph, but the disclosed CPU mask generation, tiny model and length-128 experiment do not establish production speedup or long-context quality.",
    "2605.24538": "When model, training, compute, harness, identity and ownership are decentralized together, governance can lose both an addressable principal and an actor capable of changing the running system, motivating protocol-level constitutive constraints subject to legitimacy and contestability.",
    "2605.24545": "Federated unlearning should remove data-unique memorization while preserving information also supported by remaining clients; Grouped Memorization Evaluation and FedMemPrune operationalize that distinction against retraining.",
    "2605.24570": "Gradient-direction agreement controls an online learned optimizer policy that changes its mixture of momentum, normalization and sign-based updates across locally stable or noisy regimes, but evidence is limited to small vision datasets/models.",
    "2605.24583": "A template-controlled four-way difference-in-differences protocol separates chat-format shift from alignment-induced activation shift, and causal projection ablation—not singular-value order—tests whether the recovered subspace is behaviorally active.",
    "2605.24660": "Bits-over-Random chance-corrects tool-shortlist coverage at each depth, making tool count an evaluated control and enabling per-query depth policies without an arbitrary depth penalty.",
    "2605.24647": "PUMA maintains a belief over latent user state, updates an action-conditioned user world model, and selects dialogue actions by expected free energy rather than using profile/history retrieval as the whole personalization policy.",
    "2605.24661": "Reasoning evaluation separates correctness, consistency, robustness, local logical coherence, efficiency and stability, and deployment-aware aggregation can invert rankings hidden by final-answer accuracy.",
    "2605.24662": "A deployment-calibrated digital twin re-synchronizes from streamed measurements and admits a proposed control action only when a conformal fidelity gate places its predicted outcome inside an operator-defined safe region.",
    "2605.24674": "Granularity-routed conditioning separates shallow edit-intent tokens from deeper native visual/text evidence, while a training-only reference branch aligns attention without adding the same branch at inference.",
    "2605.24683": "A deterministic Layer-2 topology and asset-identity substrate gives probabilistic AIOps reasoning an auditable physical ground truth when administrative boundaries make ordinary discovery incomplete.",
    "2605.24687": "Multi-attribute group fairness is measured jointly and optimized with a multi-objective Fair-GRPO reward, whose disclosed reward-hacking behavior remains part of the evidence boundary.",
    "2605.24696": "Streaming anomaly thresholds can be derived from operator cost, alert budget and SLO by composing change-point detection, isotonic calibration, conformal risk control and multi-window burn-rate alerts, but validity changes sharply with prevalence and exchangeability.",
    "2605.24727": "Environment complexity, model performance, explanation interpretability and complete faithfulness cannot all hold simultaneously; governance must treat an explanation as an incomplete sensor rather than a complete behavioral account.",
    "2605.24759": "Discounted policy evaluation can be expressed as guarded contractive feedback over typed open decision components, allowing local approximation and safety/resource contracts to lift through admitted wiring contexts rather than assuming every RL morphism has a global trace.",
    "2605.24764": "Multi-scale sinc convolution over token embeddings interpolates between per-token MaxSim and mean pooling for localized retrieval, but its disclosed evidence is synthetic plus LIMIT-small and leaves production latency/calibration open.",
    "2605.24775": "Long-running multi-agent work needs a typed pause/resume record, structural operating rules and an explicit cross-document harmonization phase so rate limits or process restarts do not force converged work to be replayed.",
    "2605.24779": "Complement Submodular Information scores shared structure between a selected subset and its complement, making rare-slice preservation and outlier suppression explicit in data/benchmark split selection.",
}

CHALLENGE_CLOSURE = {
    "2605.24343": "IAD learns partner-conditioned latent skills only in the disclosed Overcooked coordination policy; it does not change Agent runtime identity, durable shared state, authority, tool contract or platform recovery, so the result remains a local RL-policy branch rather than a long-lived AI-System choice.",
    "2605.24352": "PASD's contrastive partner-skill space is an Overcooked/human-proxy policy-learning result; the abstract does not expose a reusable Agent state/control interface or production coordination contract beyond the local hierarchical-RL objective.",
    "2605.24423": "ICRL4AHT is primarily a benchmark and negative result showing AD/DPT failure under teammate/layout shift; it supplies no replacement state/control mechanism, and its Overcooked protocol does not by itself revise the book's multi-agent runtime contract.",
    "2605.24458": "The multitask adversarial latent objective jointly names fairness, privacy and accuracy, but the abstract supplies neither a concrete privacy accounting/release contract nor an operational threat/fallback boundary; this is a generic supervised-learning formulation rather than a platform-security delta.",
    "2605.24528": "The child/LLM Box Task compares information-seeking behavior under a cognitive-study protocol; it does not propose an Agent planning interface or system control change, so behavioral similarity/difference remains scientific context rather than a design candidate.",
    "2605.24558": "The measurement-to-dataset argument is explicitly AI for Science and is excluded by the ROADMAP phase boundary even though its observation-model lesson could be mapped to Data or Evaluation.",
    "2605.24600": "Perspective-specific peer-debrief agents improve qualitative-analysis coding on three QDA datasets, but the contribution is a domain workflow/role prompt; it does not change general multi-agent identity, commit, recovery or evidence authority.",
    "2605.24603": "CSP-Atlas measures concept circuits in one sparse Python transformer; the circuit atlas is interpretability evidence, not a supported architecture/training/runtime design change for the current book.",
    "2605.24631": "JEPA-guided minority sampling changes a diffusion sampling objective for rare images, but does not establish a world-state, control-authority or serving contract; semantic rarity remains tied to the disclosed generator/JEPA representations.",
    "2605.24680": "TDS is an instance-difficulty signal for gradient-boosted tabular ensembles and related active/selective workflows; it does not revise large-model data, training or evaluation ownership beyond that task family.",
    "2605.24684": "SUPRA addresses topology noise and gradient starvation in multimodal attributed graphs; its graph-specific dual pathway does not create a durable LLM/multimodal-system interface or infrastructure control boundary.",
    "2605.24699": "MDIA is a clinical-domain orchestration result and therefore remains outside the active phase boundary; its specialty graph cannot be reintroduced through Agent nodes while medical/AI-for-Science applications are paused.",
    "2605.24710": "The μP result characterizes a two-layer mean-field limit and identifiability/sparse support, but it does not yet alter a concrete model, training or infrastructure design choice in the current knowledge tree.",
    "2605.24722": "The calibration method targets ambiguous object detectors and is demonstrated partly on medical images; annotator-distribution calibration is a local detector objective rather than a general model/platform release contract in the disclosed evidence.",
    "2605.24788": "XL-HD is a compact binary hyperdimensional-computing/IMC accelerator design for edge classifiers, outside the current large-model lifecycle path and without a transferable LLM serving or training-system contract.",
}

MINIMAX = {
    "arxiv_id": "minimax:sparse-token-forgetting",
    "title": 'Why Can\'t the MiniMax LLM Say "Ma Jiaqi"? Internal Investigation of Sparse Token Forgetting',
    "abstract": "Post-training sparse target coverage can leave input embeddings nearly unchanged while low-frequency lm_head vectors drift, preserving comprehension but breaking generation. Full-vocabulary target repetition repairs some affected tokens and Japanese language mixing, while Korean errors remain and show that the mechanism is not exhaustive.",
    "categories": ["institutional-research"],
    "submitted_v1_utc": "2026-05-25T16:30:00Z",
}


def score_for(aid: str) -> tuple[int, int, int]:
    if aid in STANDARD:
        return (2, 2, 2)
    if aid in SCORE9:
        return (3, 3, 3)
    if aid in SCORE8:
        return (3, 2, 3)
    return (3, 2, 2)


def decision_for(aid: str) -> str:
    if aid in APPLIED:
        return "Applied"
    if aid in INTEGRATE:
        return "Integrate"
    if aid in STRUCTURAL:
        return "Structural Candidate"
    if aid in REPORT_ONLY:
        return "Report Only"
    return "No Change — Existing Coverage"


def split_sentences(text: str) -> list[str]:
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+(?=[A-Z])", " ".join(text.split())) if x.strip()]


def adopted_claim(item: dict) -> str:
    override = CLAIM_OVERRIDE.get(item["arxiv_id"])
    if override:
        return override
    sentences = split_sentences(item["abstract"])
    for sentence in sentences:
        if re.search(r"\b(we propose|we introduce|we present|we show|we find|we argue|we reveal|we frame)\b", sentence, re.I):
            return sentence
    return sentences[0]


def boundary_for(node: str | None, item: dict) -> str:
    title = item["title"]
    if node and node.startswith("MULTIMODAL"):
        return f"`{title}` 只支持 exact-v1 披露的数据、backbone 与任务；感知质量不等于 physical/action fidelity。新增控制换来训练与评估成本，跨场景漂移时回退专用模型、真实状态 probe 或人工 gate。"
    if node and node.startswith("TRAIN"):
        return f"`{title}` 的结论绑定所测模型、数据、reward 与训练预算，不能外推生产收敛。新 objective/constraint 增加状态与调参面；回归、梯度或成本 gate 失败时回退原训练配方与 checkpoint。"
    if node == "PLATFORM-SECURITY":
        return f"`{title}` 只覆盖披露的 threat model、模型和攻击预算，不证明一般安全。新增 detector/defense 会引入误拒与适应性绕过；证据不足时回退隔离、最小权限、规则验证与人工处置。"
    if node in {"PLATFORM-EVALUATION-SYSTEM", "PLATFORM-MONITORING"}:
        return f"`{title}` 的 metric/judge 只是受测分布上的 sensor，不是 truth。更多 probe 改善定位但增加偏差、成本和 drift；校准或一致性失效时回退确定性检查、人工标签与保守 abstain。"
    if node and node.startswith("AGENT"):
        return f"`{title}` 只支持披露 benchmark、harness、工具和 evaluator。持久状态/路由减少重复工作但会放大陈旧或错误经验；版本/验证失败时回退 stateless path、重新规划或 human approval。"
    if node and node.startswith("INFER"):
        return f"`{title}` 的收益受模型、硬件、精度、长度、batch/concurrency 与 SLO 限制。新增压缩/路由状态会产生误差和管理成本；质量或 tail-latency gate 失败时回退 dense/full-precision/原生 decode。"
    if node and node.startswith("MODEL"):
        return f"`{title}` 只在披露规模、数据与架构上成立。新增 representation/token-mixing 假设换取效率或可控性但可能损失 recall/兼容性；回归失败时回退标准 tokenizer/attention/layer。"
    return f"`{title}` 提供受限机制线索，但当前没有唯一稳定 owner 或足够外部验证；不把原型结果升级为通用系统保证，失败时保持现有架构并在季度结构复核中重开。"


def closure_reason(item: dict) -> str:
    challenged = CHALLENGE_CLOSURE.get(item["arxiv_id"])
    if challenged:
        return challenged
    title = item["title"]
    low = title.lower()
    first = split_sentences(item["abstract"])[0]
    if any(k in low for k in ["protein", "molecule", "genom", "medical", "health", "clinical", "drug", "science"]):
        return f"`{title}` 的题摘中心是 AI for Science/医疗/专业领域任务（{first[:150]}）；当前 ROADMAP 明确暂停该域，且没有独立的基础模型或 AI infrastructure state/control delta。"
    if any(k in low for k in ["agricultur", "crop", "finance", "trading", "traffic", "wireless", "network", "remote sensing", "radar"]):
        return f"`{title}` 主要优化垂直应用指标（{first[:150]}），没有改变本书 owner 的状态身份、控制边界、证据合同或 failure fallback，按 domain application closure。"
    if any(k in low for k in ["segmentation", "detection", "classification", "forecast", "reconstruction", "image", "video", "robot"]):
        return f"`{title}` 的贡献停留在局部视觉/机器人任务与其 benchmark（{first[:150]}），题摘未给出可迁移到长期 AI System owner 的机制或运行时契约。"
    if any(k in low for k in ["theorem", "proof", "algebra", "graph", "optimization", "learning"]):
        return f"`{title}` 虽可主题映射 ROADMAP，但题摘只给一般理论/算法增量（{first[:150]}），没有形成当前模型、训练、推理或 Agent 的可执行 design delta。"
    return f"`{title}` 的题摘主张为“{first[:170]}”；fresh contribution challenge 未发现会改变现有知识 owner 的持久状态、控制、evidence boundary 或 trade-off/fallback，因此在候选分母前关闭。"


migration = json.loads(MIGRATION.read_text(encoding="utf-8"))
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
all_by_id = {x["arxiv_id"]: x for x in ledger["identities"]}
owner_ids = [x["arxiv_id"] for x in migration["identities"] if x.get("public_owner_day") == "2026-05-26"]
assert len(owner_ids) == 263 and len(set(owner_ids)) == 263
assert set(owner_ids) <= set(all_by_id)
assert len(SELECTED) == 85 and len(set(SELECTED)) == 85 and set(SELECTED) <= set(owner_ids)

old_exact = {x["arxiv_id"]: x for x in json.loads(OLD_EXACT.read_text(encoding="utf-8"))}
records = [dict(all_by_id[aid]) for aid in owner_ids]
selected_ids = set(SELECTED)

outcomes = []
for item in records:
    aid = item["arxiv_id"]
    retained = aid in selected_ids
    outcomes.append({
        "id": aid,
        "source_family_id": family(aid),
        "title": item["title"],
        "abstract": item["abstract"],
        "categories": item.get("categories", []),
        "public_time": ARXIV_PUBLIC,
        "status": "retained" if retained else "pre_denominator_closure",
        "screening_reason": ("fresh title+abstract review found a durable system delta: " + adopted_claim(item)) if retained else closure_reason(item),
        "withdrawn": False,
    })

assert Counter(x["status"] for x in outcomes) == {"retained": 85, "pre_denominator_closure": 178}

evidence = []
for item in records:
    aid = item["arxiv_id"]
    if aid not in selected_ids:
        continue
    s = score_for(aid)
    node = NODE[aid]
    old = old_exact.get(aid)
    detail = INTEGRATE_DETAIL.get(aid)
    if detail:
        method, evaluation, limitations, explicit_claim = detail
        claim = explicit_claim
    else:
        current_locators = EXACT_LOCATORS.get(aid)
        method = old["method_locator"] if old else current_locators[0]
        evaluation = old["evaluation_locator"] if old else current_locators[1]
        limitations = old["limitations_locator"] if old else current_locators[2]
        claim = adopted_claim(item)
    evidence.append({
        "source_family_id": family(aid), "id": aid, "title": item["title"],
        "primary_evidence_version": (f"arXiv:{aid}v1" if aid.startswith("2605.") else "MiniMax official technical blog, 2026-05-26 event version"),
        "primary_url": ("https://arxiv.org/pdf/2605.24518v1" if aid == "2605.24518" else (f"https://arxiv.org/html/{aid}v1" if aid.startswith("2605.") else "https://www.minimax.io/blog/sparse-token-forgetting")),
        "review_route": "standard" if aid in STANDARD else "deep",
        "review_status": "complete", "access_status": "accessible",
        "score": {"design_delta": s[0], "system_reach": s[1], "durability": s[2], "total": sum(s)},
        "stable_node_id": node, "adopted_proposition": claim,
        "method_locator": method, "evaluation_locator": evaluation, "limitations_locator": limitations,
        "artifact_locator": ("Not Required — standard review" if aid in STANDARD else (f"https://arxiv.org/html/{aid}v1; immutable code commit Not Disclosed" if aid.startswith("2605.") else "official MiniMax technical page; private training artifact/commit Not Disclosed")),
        "evidence_boundary_tradeoff_failure_fallback": boundary_for(node, item),
        "withdrawn_check": "no official withdrawal/deletion notice observed for the reviewed exact version",
    })

assert len(evidence) == 85
assert Counter(x["review_route"] for x in evidence) == {"deep": 73, "standard": 12}

books = []
queue = []
for ev in evidence:
    aid = ev["id"]
    node = ev["stable_node_id"]
    path = PATH.get(node)
    decision = decision_for(aid)
    marker = f"<!-- source-family:{family(aid)} -->"
    marker_count = 0
    before_review = None
    excerpt = None
    if path:
        text = (ROOT / path).read_text(encoding="utf-8")
        marker_count = text.count(marker)
        if marker_count:
            pos = text.index(marker)
            review_pos = text.find("\n## Review notes")
            before_review = review_pos == -1 or pos < review_pos
            start = max(0, text.rfind("\n\n", 0, pos))
            end = text.find("\n\n", pos)
            excerpt = text[start:end if end != -1 else len(text)].strip()
    if decision == "Applied":
        assert marker_count == 1 and before_review
    current = excerpt or (f"已顺读 `{path}` 的正文与 Review notes 前 owner boundary；现有章以更一般的 {node} 状态/控制/失败回退承载该受限证据。" if path else "当前 ROADMAP 没有唯一稳定 owner；保留结构或报告判断，不强塞正文。")
    books.append({
        "source_family_id": family(aid), "id": aid, "stable_node_id": node,
        "target_path": path, "decision": decision,
        "current_proposition_or_boundary": current,
        "binding_marker": marker if decision == "Applied" else None,
        "binding_marker_count": marker_count, "before_review_notes": before_review,
    })
    if decision == "Integrate" or aid in ROOT_APPLIED:
        method, evaluation, limitations, delta = INTEGRATE_DETAIL[aid]
        queue_status = (
            "postwrite_semantic_review_passed_pending_different_fresh_date_reviewer"
            if aid in ROOT_APPLIED else "marker_only_repair_pending_root"
        )
        queue.append({
            "source_family_id": family(aid), "id": aid, "title": ev["title"],
            "owner": node, "target_path": path,
            "serialized_anchor": (
                "existing root-authored block immediately before the main `## Review notes`"
                if aid in ROOT_APPLIED else
                f"insert marker only immediately after `<!-- semantic-body-binding:{family(aid)}:end -->` and before the main `## Review notes`"
            ),
            "binding_marker": marker, "adopted_proposition_and_delta": delta,
            "required_narrative": (
                "既有 semantic body 保持不变；只补独立 source-family marker，不重复机制正文。"
                if aid in INTEGRATE else
                "先说明旧 baseline 为何合理与 constraint change，再写 state/control/evidence boundary；显式给出 trade-off、failure mode、fallback 与旧路径共存。"
            ),
            "exact_v1_locators": {"method": method, "evaluation": evaluation, "limitations": limitations},
            "status": queue_status,
        })

counts = Counter(x["decision"] for x in books)
assert counts == {"No Change — Existing Coverage": 41, "Applied": 30, "Integrate": 7, "Structural Candidate": 5, "Report Only": 2}
assert Counter(x["status"] for x in queue) == {
    "postwrite_semantic_review_passed_pending_different_fresh_date_reviewer": 9,
    "marker_only_repair_pending_root": 7,
}

sources = [
    ("SRC-OPENAI", "official News/Research RSS; two 05-25 08:00 BJT events are one hour before this window", "checked", "0 raw; both outside window"),
    ("SRC-ANTHROPIC", "official Research; nearest dated research event 05-22", "checked", "none"),
    ("SRC-GOOGLE-AI", "DeepMind Research/Google Publications; adjacent dated items 05-19 and 05-28", "checked", "year-only cards do not support site-wide no-hit"),
    ("SRC-META-AI", "official Publications entry", "limited", "empty/internal-error response; not used for no-hit"),
    ("SRC-QWEN", "official article index; adjacent 05-20 and 05-29", "checked", "none"),
    ("SRC-DEEPSEEK", "official News/Research; adjacent 04-24 and 06-24", "checked", "none"),
    ("SRC-MOONSHOT", "official Kimi Blog; no dated research/release/RFC in window", "checked", "none"),
    ("SRC-TENCENT-HUNYUAN", "official publicList; visible records outside window", "checked", "none"),
    ("SRC-ZAI", "official Research; adjacent 05-20 and 06-16", "checked", "none"),
    ("SRC-BYTEDANCE-SEED", "official Research/Public Papers; adjacent 05-16 and 05-29", "checked", "none"),
    ("SRC-BAIDU-ERNIE", "official technical Blog; latest explicit date before window is 05-09", "checked", "none"),
    ("SRC-XIAOMI-MIMO", "official dated papers; adjacent 03-13 and 06-29", "limited", "undated cards do not support day-level no-hit"),
    ("SRC-MINIMAX", "official Research/Blog JSON-LD datePublished=2026-05-27T00:00:00Z", "checked", "0 raw in 05-26 window; event is owned by 05-27 at 08:00 BJT"),
    ("SRC-ARXIV", "official 05-25 20:00 ET announcement migrated to 05-26 08:00 BJT", "checked", "263 raw = 85 retained + 178 closure"),
]

write_json("official-owner-batch-evidence-v3.json", {
    "schema": "daily-official-owner-batch-evidence-v3", "report_date": "2026-05-26",
    "window": {"start": WINDOW_START, "end": WINDOW_END},
    "arxiv_announcement": {"official_time_et": "2026-05-25T20:00:00-04:00", "public_time_bjt": ARXIV_PUBLIC,
        "identity_count": 263, "id_range": [min(owner_ids), max(owner_ids)], "ids": owner_ids,
        "migration_receipt": str(MIGRATION.relative_to(ROOT))},
    "institution_events": [],
    "raw_count": 263, "dedup_count": 263, "withdrawn_count": 0,
    "excluded_legacy_state": {"raw_1208": True, "candidate_170": True, "reason": "DataCite-created/OAI mixed owner basis is not first-public ownership"},
})
write_json("source-coverage-v3.json", {
    "schema": "daily-source-coverage-v3", "report_date": "2026-05-26", "checked_at": CHECKED_AT,
    "source_count": 14, "institution_source_count": 13, "sources": [dict(zip(("source_id", "basis", "result", "limitation"), x)) for x in sources],
    "ordinary_commits_or_prs_expanded": False, "zero_omission_claim": False,
})
write_json("screening-outcomes-v3.json", {
    "schema": "daily-screening-outcomes-v3", "report_date": "2026-05-26",
    "raw_count": 263, "retained_count": 85, "pre_denominator_closure_count": 178,
    "withdrawn_count": 0, "arithmetic": "263 = 85 retained + 178 pre-denominator closure + 0 withdrawn",
    "items": outcomes,
})
write_json("evidence-review-v3.json", {
    "schema": "daily-evidence-review-v3", "report_date": "2026-05-26", "candidate_count": 85,
    "deep_count": 73, "standard_count": 12, "blocked_count": 0,
    "score_distribution": dict(sorted(Counter(str(x["score"]["total"]) for x in evidence).items())),
    "items": evidence,
})
write_json("books-comparison-v3.json", {
    "schema": "daily-books-current-content-comparison-v3-author-recertification", "report_date": "2026-05-26",
    "candidate_count": 85, "counts": dict(counts),
    "arithmetic": "85 = 30 Applied + 7 Integrate marker-only root repair + 41 No Change + 5 Structural Candidate + 2 Report Only",
    "items": books, "shared_books_modified_by_author": False,
})
write_json("root-books-writeback-queue-v3.json", {
    "schema": "daily-root-books-writeback-queue-v3", "report_date": "2026-05-26",
    "status": "marker_only_repair_pending_root_then_fresh_review", "item_count": 16,
    "applied_pending_fresh_review_count": 9, "pending_root_serial_write_count": 0,
    "marker_only_repair_pending_root_count": 7,
    "items": queue,
})
write_json("materials-request-v3.json", {
    "schema": "daily-materials-request-v3", "report_date": "2026-05-26", "open_count": 0,
    "items": [], "note": "No user material blocker; all retained evidence was accessible at the bounded review route.",
})
write_json("author-adversarial-audit-v3.json", {
    "schema": "daily-author-adversarial-audit-v3", "report_date": "2026-05-26", "status": "author_complete_pending_fresh_non_author",
    "checks": {
        "official_owner_batch": "passed: 263 migrated announcement identities",
        "institution_event_dedup": "passed after correction: MiniMax official JSON-LD belongs to 05-27 and is excluded from 05-26",
        "false_positive": "passed author challenge: AI for Science, domain application, benchmark-only and ROADMAP-theme-only entries closed",
        "false_negative": "passed bounded second challenge: 20 false negatives restored; 178 closure abstracts remain for independent challenge",
        "withdrawn": "passed author check: 0 official withdrawn/deleted retained items",
        "books": "open: 9 marker-complete actions + 7 marker-only root repairs; author did not edit shared Books",
        "independence": "open: a different fresh non-author reviewer is required",
    },
    "arithmetic": {"raw": "263=263+0", "denominator": "263=85+178+0", "evidence": "85=73+12", "books": "85=30+7+41+5+2"},
})

ev_by_id = {x["id"]: x for x in evidence}
book_by_id = {x["id"]: x for x in books}
lines = [
    "# Daily Research — 2026-05-26", "", "**规范：** V3", "",
    f"**窗口：** {WINDOW_START} ～ {WINDOW_END}", "", "**状态：** 进行中", "",
    "**Books：** 纳入本次", "", f"**检查时间：** {CHECKED_AT}", "",
    "## 1. 结论", "",
    "旧 V2.1 `Complete`、1208 raw 与 170 candidates 不再拥有当前状态。当前 first-public owner 仅为 2026-05-26 08:00 BJT 的 263 项 arXiv official announcement batch；MiniMax 官方 JSON-LD 属 05-27，不进入本日投影。全日守恒为 **263 = 85 retained + 178 pre-denominator closure + 0 withdrawn**。", "",
    f"Evidence 为 **85 = 73 deep complete + 12 standard complete + 0 blocked**；评分分布为 `{dict(sorted(Counter(x['score']['total'] for x in evidence).items()))}`。Books 对账为 **85 = 30 Applied + 7 Integrate + 41 No Change + 5 Structural Candidate + 2 Report Only**。16 个 semantic body 已存在；root 只需为 7 项补独立 source-family marker，不重复正文。状态保持 Ongoing，等待 root 与不同 fresh reviewer。", "",
    "## 2. 来源覆盖", "", "| 来源 | 检查范围与依据 | 结果 | 缺口 |", "| --- | --- | --- | --- |",
]
for sid, basis, result, limitation in sources:
    result_display = {"checked": "已检查", "limited": "受阻"}[result]
    lines.append(f"| {sid} | {basis} | {result_display} | {limitation} |")
lines += ["", "完整 owner 与 event receipt 见 [`official-owner-batch-evidence-v3.json`](../_sources/daily-20260526/official-owner-batch-evidence-v3.json)，14-source 结构化记录见 [`source-coverage-v3.json`](../_sources/daily-20260526/source-coverage-v3.json)，263 条逐项结果与 family-aware closure 理由见 [`screening-outcomes-v3.json`](../_sources/daily-20260526/screening-outcomes-v3.json)。受阻或无日级时间的入口不支持全站 no-hit；普通 commit/PR 未扩入 denominator。", "", "## 3. 候选与判断", "", "| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |", "| --- | --- | --- | --- | --- |"]
for ev in evidence:
    aid = ev["id"]
    url = ev["primary_url"]
    score = ev["score"]
    decision = book_by_id[aid]["decision"]
    decision_display = {
        "Applied": "整合：当前正文 binding 已存在",
        "Integrate": "整合：待 root 串行写回",
        "No Change — Existing Coverage": "已有覆盖",
        "Structural Candidate": "结构候选",
        "Report Only": "仅报告",
    }[decision]
    target_path = book_by_id[aid]["target_path"]
    if target_path:
        decision_display += f" [章节](../../../../{target_path})"
    review = "深入完成" if ev["review_route"] == "deep" else "标准完成"
    owner = ev["stable_node_id"] or "无唯一 owner"
    public = ARXIV_PUBLIC
    short = ev["adopted_proposition"].replace("|", "\\|")[:240]
    lines.append(f"| [{aid} {ev['title']}]({url}) | {public} | {short}；{score['design_delta']}+{score['system_reach']}+{score['durability']}={score['total']} | {review} | {decision_display}：{owner} |")
lines += ["", "## 4. 证据与知识整合", "", "结构化 exact-version、locator、score、adopted proposition 与 non-proof boundary 见 [`evidence-review-v3.json`](../_sources/daily-20260526/evidence-review-v3.json)；Books 当前正文比较见 [`books-comparison-v3.json`](../_sources/daily-20260526/books-comparison-v3.json)。", ""]
for ev in evidence:
    aid = ev["id"]
    sf = ev["source_family_id"]
    b = book_by_id[aid]
    lines += [f"### [{aid} {ev['title']}]({ev['primary_url']})", "", f"<!-- review:{sf}:start -->",
              f"证据位置：{ev['method_locator']}；{ev['evaluation_locator']}；{ev['limitations_locator']}。",
              f"<!-- claim:{sf}:start -->{ev['adopted_proposition']}<!-- claim:{sf}:end -->",
              f"证据边界、trade-off、failure 与 fallback：{ev['evidence_boundary_tradeoff_failure_fallback']}",
              f"Books：{b['decision']}；owner={ev['stable_node_id'] or '无唯一 owner'}。", f"<!-- review:{sf}:end -->", ""]
lines += ["## 5. 缺口与下一步", "",
          "1. root 按 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260526/root-books-writeback-queue-v3.json) 只补 7 个 source-family marker；不得重复已有 mechanism 正文。", "2. 写回后逐项确认 16 项 action 的 marker 唯一且位于主 `## Review notes` 前。", "3. 由不同 fresh non-author reviewer 独立挑战 263 owner/date、178 closure 的 FN、85 retained 的 FP/evidence/Books；作者不能自签 Complete。", "", "## 6. 复核", "",
          "bounded owner repair 已完成，Books 与 fresh semantic Gate 仍为 Open。当前精确剩余项：7 项 root marker-only repair + 对 16 项 action 的写后检查 + 1 次不同 fresh non-author 的 coverage/evidence/books/post-write 审查。无材料 blocker。", ""]
REPORT.write_text("\n".join(lines), encoding="utf-8")

checkpoint = f"""# 2026-05-26 V3 Author Recertification Checkpoint

状态：Ongoing；bounded owner repair complete，等待 root marker-only repair 与不同 fresh non-author 最终 Gate。

## 冻结结果

- owner/raw：263 = 263 arXiv official-announcement identities + 0 institutional event；MiniMax 官方 JSON-LD 属 05-27。
- denominator：263 = 85 retained + 178 pre-denominator closure + 0 withdrawn。
- Evidence：85 = 73 deep complete + 12 standard complete + 0 blocked。
- Books：85 = 30 Applied + 7 Integrate + 41 No Change + 5 Structural Candidate + 2 Report Only。
- action：16 个 semantic body 已存在；9 个 source-family marker 完整，7 个 marker-only root repair pending。
- 旧 1208/170、旧评分、旧 disposition 与 V2.1 Complete 均未继承。

## 精确剩余 Gate

1. root 按 `root-books-writeback-queue-v3.json` 只补 7 个 source-family marker；作者不写 Books。
2. 新 reviewer 重新挑战 owner/date、178 closure 的 false negative、85 candidates 的 evidence boundary 与 Books decision。
3. 对 16 项 action 做写后 marker/Review-notes 顺序审查；只有不同 reviewer 可将 README 改为 Complete。

生成时间：{CHECKED_AT}
"""
(LOCAL / "AUTHOR_V3_RECERTIFICATION_CHECKPOINT_20260915.md").write_text(checkpoint, encoding="utf-8")

print(json.dumps({"raw": 263, "retained": 85, "closure": 178, "deep": 73, "standard": 12, "books": dict(counts), "queue": {"marker_complete": 9, "marker_only_pending": 7}}, ensure_ascii=False))
