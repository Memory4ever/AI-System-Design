#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the current-contract 2026-05-25 author recertification.

The preserved owner receipt is reused only for identity/title/abstract data.  Public-day
ownership, contribution screening, evidence status and Books decisions are all V3
projections produced by this bounded re-audit.
"""

from __future__ import annotations

import json
import re
import shutil
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from full_rescreen_config_v3 import (
    CONFIRMED_FALSE_NEGATIVES,
    DEFERRED as FULL_RESCREEN_DEFERRED,
    INTEGRATIONS as FULL_RESCREEN_INTEGRATIONS,
    OWNER_BY_ID as FULL_RESCREEN_OWNER_BY_ID,
    REPORT_ONLY as FULL_RESCREEN_REPORT_ONLY,
    RESTORE_IDS as FULL_RESCREEN_RESTORE_IDS,
    STRUCTURAL as FULL_RESCREEN_STRUCTURAL,
)


ROOT = Path(__file__).resolve().parents[5]
LOCAL = ROOT / "papers/2026/05/_sources/daily-20260525"
REPORT = ROOT / "papers/2026/05/25/README.md"
LEGACY = LOCAL / "legacy-v21-report-snapshot.md"
OWNER = ROOT / "papers/2026/05/_sources/arxiv-owner-replay-20260903/20260525/arxiv-owner-receipt.json"
CHECKED_AT = datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(timespec="seconds")
HEADING_INDEX_PATH = LOCAL / "full-rescreen-source-heading-index-v3.json"
HEADING_INDEX = {
    item["arxiv_id"]: item
    for item in json.loads(HEADING_INDEX_PATH.read_text(encoding="utf-8"))["items"]
}
EXISTING_ROOT_QUEUE_PATH = LOCAL / "root-books-writeback-queue-v3.json"
EXISTING_ROOT_QUEUE_ITEMS = (
    json.loads(EXISTING_ROOT_QUEUE_PATH.read_text(encoding="utf-8")).get("items", [])
    if EXISTING_ROOT_QUEUE_PATH.exists()
    else []
)
ROOT_APPLIED_INTEGRATIONS = {
    item["arxiv_id"]
    for item in EXISTING_ROOT_QUEUE_ITEMS
    if item.get("action") == "integrate_new_proposition" and item.get("status") == "applied_pending_fresh_review"
}


def family(arxiv_id: str) -> str:
    return "SF-2026-ARXIV-" + arxiv_id.replace(".", "-")


def write_json(name: str, value: object) -> None:
    (LOCAL / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if not LEGACY.exists():
    shutil.copyfile(REPORT, LEGACY)
legacy_text = LEGACY.read_text(encoding="utf-8")
owner = json.loads(OWNER.read_text(encoding="utf-8"))
by_id = {item["arxiv_id"]: item for item in owner["identities"]}


# The 56 prior candidates were rechecked against their preserved exact-v1 review
# locators.  This parses identity/score/owner/disposition only; no V2.1 completion
# status is inherited.
old_candidates: dict[str, dict] = {}
for line in legacy_text.splitlines():
    if not line.startswith("| SF-"):
        continue
    cells = [cell.strip() for cell in line.strip("|").split("|")]
    if len(cells) != 22 or not cells[1].startswith("arXiv:2605."):
        continue
    arxiv_id = cells[1].removeprefix("arXiv:").removesuffix("v1")
    old_candidates[arxiv_id] = {
        "legacy_family_id": cells[0],
        "score": [int(cells[6]), int(cells[7]), int(cells[8])],
        "stable_node_id": cells[18] if cells[18] != "—" else None,
        "legacy_books_disposition": cells[19],
        "legacy_review_ref": cells[14],
        "legacy_books_review_ref": cells[20],
    }


RESTORED = {
    "2605.22834": {
        "score": [2, 2, 2], "node": "AGENT-RAG", "decision": "Integrate",
        "locators": ["PDF §3 Query-Adaptive Semantic Chunking", "PDF §4–§5 Experiments", "PDF §6–§7 Discussion and future work"],
        "claim": "把 chunk boundary 从 ingestion 固定产物改成 query-conditioned 派生状态：先以 query–seed similarity 定位证据，再扩展上下文并聚合；query、parser、embedding model 与 document revision 必须共同进入 chunk identity。",
        "boundary": "证据仅覆盖 100 份技术文档、200 个查询与作者的 MiniLM/合成设置；每查询重切分增加延迟与 cache fragmentation，query 偏差会切断必要上下文，失败时回退版本化固定 chunk 或结构化 section retrieval。",
    },
    "2605.22855": {
        "score": [2, 2, 3], "node": "PLATFORM-EVALUATION-SYSTEM", "decision": "No Change — Existing Coverage",
        "locators": ["HTML §§3–5 task formulation, simulator assets, LLM protocol and baselines", "HTML §6 Experiments; Table 3 main results; Table 4 prompt/reasoning analyses", "HTML §8 Limitations and Future Work; Appendix D uncertainty and heuristic details"],
        "claim": "Agent evaluation 必须分离 structured-action contract compliance、agreement/completion rate 与 intended business/environment outcome：在作者固定的 7,500-episode stream 中，合法 JSON action 与高于 0.99 的 deal rate 可以同时对应接近 random baseline、远低于 concession heuristic 的 seller profit。",
        "boundary": "证据只覆盖 PrefBench 的半合成车辆定价 simulator、benchmark-defined hidden buyer model、披露的 zero-shot prompts/providers 与 seller-profit objective；不证明真实谈判收入、一般 Agent 无能，亦未评估 fairness、privacy、welfare。更详细 prompt 在作者 ablation 中提高成交率却降低利润，因此 contract completion 只能作为诊断，不可冒充成功判据；外部有效性或 objective identity 不清时，保留原始 trajectory 与独立 outcome metrics。",
        "existing": "books/part-06-ai-infrastructure/66-evaluation-system.md §HTTP 成功只是质量判断的第一道门 与 §从目标到证据，而不是从指标到目标：Contract success、Semantic/Policy quality 与 Outcome success 必须分层，且目标与判定条件先于指标。",
    },
    "2605.22869": {
        "score": [2, 2, 2], "node": "TRAIN-LORA", "decision": "No Change — Existing Coverage",
        "locators": ["PDF §3–§5 FuRA spectral PEFT", "PDF §6 Experiments", "PDF Appendix E scope and ablations"],
        "claim": "用 block tensor-train/SVD basis 预条件化低秩更新，使有限 rank 的可用方向不只由 nominal rank 决定。",
        "boundary": "收益绑定受测 LLaMA/VLM 任务、SVD basis 与预计算；basis 陈旧或额外分解成本超界时回退普通 LoRA/full tuning。Ch30 已明确 adapter capacity 同时取决于 rank、optimizer transform 与实际更新谱。",
    },
    "2605.22870": {
        "score": [3, 2, 2], "node": "MODEL-DECODER-ONLY", "decision": "No Change — Existing Coverage",
        "locators": ["PDF §2–§6 Readout Shortcut analyses", "PDF arithmetic experiments", "PDF §Limitations (p.8)"],
        "claim": "dense per-step/per-loop loss 只约束 readout 可见方向，模型可能把可解中间状态藏在 readout null space，并在最后一步才形成答案。",
        "boundary": "证据限于 1–3B arithmetic、numeric trailing answer 与受测架构；不能外推开放任务。Ch18 已写明 looped LM 的 per-loop cross-entropy 只控制 readout-visible variables，hidden recurrent state 仍可携带信息。",
    },
    "2605.22873": {
        "score": [2, 3, 2], "node": "INFER-SCHEDULING", "decision": "Integrate",
        "locators": ["PDF §3 EDRM entropy trajectory and early probe", "PDF §4 experiments on 15 benchmarks", "PDF §11 limitations"],
        "claim": "以早期 token entropy trajectory 和轻量 probe 估计当前请求是否值得进入高成本 reasoning path；probe 只拥有 route proposal，质量/预算 Gate 决定 commit。",
        "boundary": "只支持 3B–8B 开源文本模型与作者 benchmark；probe overhead、domain drift 和 confident-wrong 会误路由，故必须保留固定模型/固定预算 fallback 与逐 slice calibration。",
    },
    "2605.22903": {
        "score": [3, 2, 2], "node": "PLATFORM-EVALUATION-SYSTEM", "decision": "No Change — Existing Coverage",
        "locators": ["HTML §3 Vision is not Needed", "HTML §4–§6 intervention experiments", "HTML §7 Discussion; §8 Conclusion"],
        "claim": "top-1 benchmark accuracy 对视觉 token 删除、遮挡与 entity swap 可能不敏感，必须把保持输入/问题而干预视觉证据的 counterfactual test 纳入 grounding evaluation。",
        "boundary": "七个开源 VLM、四类 benchmark 与作者干预不证明所有视觉任务失真；实体定位/生成式替换也引入误差。Ch66 已要求同一 Evaluation Identity 下执行证据干预并把 sensor 与 truth authority 分开。",
    },
    "2605.22964": {
        "score": [3, 2, 3], "node": "PLATFORM-EVALUATION-SYSTEM", "decision": "No Change — Existing Coverage",
        "locators": ["PDF main certification-hardness theorems", "PDF trained/constructed addition cases", "PDF assumptions and appendices"],
        "claim": "有限样例通过不能升级成精确算法证书；对受限 threshold-circuit/log-precision Transformer 类，exact certification 仍可能需要指数证据。",
        "boundary": "结论依赖形式模型、精度与开销定义，不证明所有神经网络验证都指数困难。Ch66 已区分 tests、translation certificate 与 machine proof，并要求 specification/parser/solver 边界保留。",
    },
    "2605.22967": {
        "score": [2, 3, 2], "node": "MULTIMODAL-GENERATIVE-PARADIGMS", "decision": "Integrate",
        "locators": ["PDF §3 learned relay representations and truncated BPTT", "PDF §4 experiments", "PDF §5 limitations"],
        "claim": "在多阶段 diffusion/iterative generator 中，用 learned relay state 传递跨阶段信息并截断反向图，把端到端 gradient memory 换成显式 relay-interface fidelity。",
        "boundary": "relay 会丢失未编码依赖并引入阶段/版本兼容；作者承认两类额外 compute。relay validation 或跨阶段一致性失败时回退 full backprop、较短 unroll 或静态显式 state。",
    },
    "2605.22981": {
        "score": [2, 2, 2], "node": "TRAIN-DATA", "decision": "No Change — Existing Coverage",
        "locators": ["PDF §3–§4 FIM memorization experiments", "PDF §5.1 Limitations", "PDF appendices"],
        "claim": "fill-in-the-middle objective 与重复片段共同改变 memorization surface，必须按 corruption/objective、重复次数和 extraction probe 区分记忆风险。",
        "boundary": "仅从头训练的小模型与重复次数不超过 128，attribution 未闭合；Ch27 已要求 corruption policy、dedup/repetition 与 memorization probe 共同版本化。",
    },
    "2605.23023": {
        "score": [2, 2, 2], "node": "AGENT-PLANNING", "decision": "No Change — Existing Coverage",
        "locators": ["PDF §3–§4 co-planning design space", "PDF §5–§6 user study and controlled experiments", "PDF §7.2 Limitations"],
        "claim": "human–LLM co-planning 应把 proposal、critique、selection 与 final commit authority 分开，而不是让对话流畅度代理计划质量。",
        "boundary": "用户研究与任务集不能证明跨领域最优交互；Ch79 已拥有 proposal/verification/commit、branch budget 与 human gate。高风险动作失败时回退人工计划与显式批准。",
    },
    "2605.23040": {
        "score": [2, 2, 2], "node": None, "decision": "Structural Candidate",
        "locators": ["PDF §2 sparse query-feature steering", "PDF experiments and ablations", "PDF scope/limitations"],
        "claim": "从 query-conditioned sparse features 中优化小规模干预方向，可把全局 steering vector 改成输入相关控制，但需要独立因果与任务回归 Gate。",
        "boundary": "SAE/model/task 与优化成本限制结论；feature 相关不等于因果，错误 direction 会破坏未测行为。当前 ROADMAP 没有唯一 model-internals intervention owner，先保留结构候选，不强塞 Prompt 或 Evaluation。",
    },
    "2605.23054": {
        "score": [3, 2, 2], "node": "TRAIN-DATA", "decision": "No Change — Existing Coverage",
        "locators": ["PDF iterated self-training design", "PDF experiments and five predictions", "PDF §7 Limitations"],
        "claim": "recursive synthetic training 的漂移可呈非单调 cultural-attractor dynamics，不能只用单代质量或单一 supplier share 解释 model collapse。",
        "boundary": "文化演化只是分析对应而非形式等价，模型/代数有限；Ch27 已要求同时冻结 base checkpoint、supplier mixture、human anchor、generation 与 seed，并避免单变量因果。",
    },
    "2605.23061": {
        "score": [2, 3, 2], "node": "TRAIN-PRETRAINING", "decision": "No Change — Existing Coverage",
        "locators": ["PDF §2–§4 SF-NorMuon", "PDF language-model experiments; Appendix E", "PDF compute/scale omissions"],
        "claim": "schedule-free matrix optimizer 的 averaging、spectral update 与 weight decay 必须作为同一 state transition 验收，而非把 horizon-free 当作无状态。",
        "boundary": "证据只到 125M/772M 与披露 token budgets，最大 8x 运行因计算未完成；Ch28 已覆盖 schedule-free averaging、weight-decay interaction、optimizer-state/checkpoint identity 与 WSD/cosine fallback。",
    },
    "2605.23081": {
        "score": [3, 3, 2], "node": "INFER-KV-CACHE", "decision": "No Change — Existing Coverage",
        "locators": ["PDF ThriftAttention method", "PDF experiments", "PDF §5 limitations"],
        "claim": "保留完整低精度 attention/KV 路径，只为 query-dependent 少量重要 blocks 晋升精度；selector 与 paired-cache identity 必须一致。",
        "boundary": "作者结果限 consumer Blackwell 与指定模型，5% FP16 headline 不证明 production goodput。Ch45 已逐字承载 selective precision promotion、双路径 kernel/footprint/fallback，并列 ThriftAttention。",
    },
    "2605.23109": {
        "score": [3, 3, 2], "node": "AGENT-TOOL-CALLING", "decision": "No Change — Existing Coverage",
        "locators": ["PDF §3–§4 IDS synthesis", "PDF §5 and Appendix E evaluation", "PDF main limitations; Appendix H"],
        "claim": "把 LLM synthesis proposal 与 Rocq specification/proof kernel 交替执行，只有独立 checker 能把候选升级为 verified artifact。",
        "boundary": "依赖形式规格、Rocq 环境与受测 benchmark；proof 不覆盖现实语义映射。Ch78 已规定 tool evidence 与 formal proof 在 typed claim 汇合、失败时 Abstain。",
    },
    "2605.23147": {
        "score": [3, 2, 2], "node": "MODEL-SELF-ATTENTION", "decision": "No Change — Existing Coverage",
        "locators": ["HTML §3–§5 persona/task representation analyses", "HTML experiments", "HTML discussion/limitations"],
        "claim": "persona 与 task 在局部 residual site 上近似可加，不推出 persona prompt 可被单一 activation 或短 prefix 压缩；功能状态可能跨 token、层与 KV 分布。",
        "boundary": "受测 instruction-tuned models/personas 不证明统一线性控制。Ch14 已明确单位置可读不等于单位置控制，task template 可能跨 demo positions、层和 residual 路径共同承载。",
    },
    "2605.23278": {
        "score": [3, 2, 2], "node": "MODEL-DECODER-ONLY", "decision": "Report Only",
        "locators": ["PDF §2–§7 next-token marginal/local-sufficiency analysis", "PDF conceptual examples", "PDF assumptions and open questions"],
        "claim": "next-token marginals 能支持哪些全局能力取决于 local sufficiency、ergodicity 与可查询外部状态等假设，不能从 factorization 本身推出。",
        "boundary": "这是概念/理论综合，没有新的受控模型实验或可执行设计；Ch18 已解释 causal factorization 的局部边界。仅报告，不把假设性推演写成架构保证。",
    },
    "2605.23463": {
        "score": [3, 3, 2], "node": "MULTIMODAL-REPRESENTATION", "decision": "No Change — Existing Coverage",
        "locators": ["PDF §2 StepAudio 2.5 architecture", "PDF §3–§5 evaluations", "PDF limitations/evaluator caveats (p.10)"],
        "claim": "统一 audio backbone 仍需把语义 token、acoustic detail、task-specific RLHF 与 streaming decode state 分责，ASR multi-token prediction 只是受限训练分支。",
        "boundary": "厂商报告的模型、数据和 evaluator 不证明生产 streaming/SLO 或任意语种；Ch23 已覆盖 semantic/acoustic codebooks、speaker/turn identity、streaming backpressure 与不对称 audio representation。",
    },
    "2605.23476": {
        "score": [3, 2, 2], "node": "TRAIN-PRETRAINING", "decision": "Integrate",
        "locators": ["PDF non-normal update theory", "PDF numerical two-layer experiments", "PDF appendices and proof-of-concept scope"],
        "claim": "optimizer update matrix 非 normal 时，eigenvalue/spectral-radius 稳定并不控制瞬态放大；应把 eigenvector conditioning/pseudospectral sensitivity 作为诊断而非自动控制权。",
        "boundary": "只支持理论构造和小型 two-layer 数值实验，不能证明大型 Transformer 收敛或墙钟收益；诊断成本高或 basis 不稳时回退 singular-value/update-norm、loss trajectory 与 matched optimizer baseline。",
    },
    "2605.23491": {
        "score": [3, 3, 2], "node": "AGENT-REFLECTION", "decision": "Deferred",
        "locators": ["official arXiv abstract only; exact-v1 HTML/PDF unavailable during bounded retries", "evaluation details pending exact-v1 body", "limitations pending exact-v1 body"],
        "claim": "摘要提出让 code pool 与 self-generated unit-test pool 通过双向 pass-count matrix 协同修正；该命题在正文取得前不能被采用。",
        "boundary": "摘要不足以核验 benchmark、预算、ablation、错误 test 共偏与 fallback；精确隔离，不进入 Books，也不支撑正面结论。",
    },
    "2605.23603": {
        "score": [3, 2, 3], "node": "MODEL-SELF-ATTENTION", "decision": "Report Only",
        "locators": ["HTML §3 Preisach Attention", "HTML §4–§7 theory", "HTML §10 open questions"],
        "claim": "以 hysteretic relay operators 替代部分 attention interaction 可获得理论表达力与复杂性结果。",
        "boundary": "只在 arbitrary-precision/formal setting 下证明性质，没有训练语言模型或 benchmark；仅报告为理论设计线索，不把 Turing completeness 写成可部署优势。",
    },
    "2605.23721": {
        "score": [3, 2, 2], "node": "TRAIN-DATA", "decision": "No Change — Existing Coverage",
        "locators": ["PDF §3 classifier-quality filtering bypass", "PDF §4 manual annotation/experiments", "PDF §5 conclusion and limitations"],
        "claim": "quality classifier 可被表面格式操纵，使内容质量不变时 retention 决策翻转；filter release 应包含 policy-preserving style counterfactual。",
        "boundary": "只覆盖 FineWeb-Edu classifier 与受测 reformatting；Ch27 已写明模型过滤器继承偏好、教科书风格损失多样性，并要求 retention/distribution shift 联合报告。",
    },
    "2605.23751": {
        "score": [3, 2, 2], "node": "MODEL-SELF-ATTENTION", "decision": "Report Only",
        "locators": ["PDF §2 I/O model", "PDF approximate-attention algorithms/lower bounds", "PDF theory boundary"],
        "claim": "在特定 external-memory/I/O model 与 additive approximation error 下构造 attention 算法及 lower bound。",
        "boundary": "没有生产 kernel 或端到端模型实验，且不是 exact softmax；仅报告，不从渐近 I/O 界推出 GPU latency。实现前仍以 dense/exact attention 为 fidelity fallback。",
    },
    "2605.23772": {
        "score": [3, 2, 2], "node": "PLATFORM-EVALUATION-SYSTEM", "decision": "No Change — Existing Coverage",
        "locators": ["PDF §2 methodology", "PDF §4 CLEVER experiments", "PDF benchmark-isomorphism limitations"],
        "claim": "program-verification benchmark 的自然语言题与形式规格可能不等价；必须将 specification normalization、patched versions 与 executable checker 绑定到 Evaluation Identity。",
        "boundary": "结果绑定 Claude/API 与 CLEVER 版本，ambiguous specs 仍需人工裁决；Ch66 已把 specification、parser、toolchain、tests 与 proof kernel 分层，任何一层通过都不覆盖其余边界。",
    },
    "2605.23857": {
        "score": [3, 2, 2], "node": "TRAIN-SFT", "decision": "Integrate",
        "locators": ["PDF distillation method", "PDF §6 experiments; Appendix G ablations", "PDF fixed student/scale boundary"],
        "claim": "teacher 的 aggregate capability 更强不保证固定 student 在固定 token/compute budget 下学得更多；teacher–student compatibility 与 target difficulty 应成为 distillation selection contract。",
        "boundary": "主实验固定约 1.7B student、受测 teachers/tokens 与混合 LM/KD loss，不支持普遍选择弱 teacher；兼容性或 held-out gate 失效时回退 matched stronger teacher、ensemble/mixture 或直接 ground-truth SFT。",
    },
    "2605.23872": {
        "score": [3, 2, 2], "node": "MODEL-TRANSFORMER-LAYER", "decision": "No Change — Existing Coverage",
        "locators": ["PDF §2 damped substeps/Runge–Kutta loop", "PDF §3 experiments", "PDF fixed-recipe and failure cases"],
        "claim": "training-free looped Transformer 通过 damped substeps/RK-style refinement 改变有效深度，但必须有收敛、预算与退化 fallback。",
        "boundary": "知识型选择题、约 20k H100 hours 与受测 checkpoints 不证明通用收益；Ch17 已覆盖 fixed-loop/fixed-point refinement、收敛失败、迭代上限和固定深度 fallback。",
    },
    "2605.23901": {
        "score": [3, 2, 2], "node": "TRAIN-PRETRAINING", "decision": "Report Only",
        "locators": ["PDF §3 noisy-channel scaling theory", "PDF §4 Pythia/OLMo2 experiments", "PDF selected-noise/fit boundary"],
        "claim": "把训练噪声、量化或 SFT 扰动拟合为 noisy-channel capacity 可形成诊断性 scaling relation。",
        "boundary": "选定 perturbations 和模型上的拟合不是普遍 Shannon law，也没有建立因果控制接口；仅报告为分析假说，训练决策仍回退 matched loss/quality/compute curves。",
    },
}


def repaired_entry(score, node, decision, method, evaluation, nonproof, claim, boundary, *, existing=None, anchor=None, delta=None):
    item = {
        "score": score,
        "node": node,
        "decision": decision,
        "locators": [method, evaluation, nonproof],
        "claim": claim,
        "boundary": boundary,
    }
    if existing:
        item["existing"] = existing
    if anchor:
        item["anchor"] = anchor
    if delta:
        item["delta"] = delta
    return item


# Fresh non-author review on 2026-09-16 found 20 definite false negatives and
# named 21 same-reason closures for bounded reopen.  All 41 passed the current
# title + full-abstract contribution gate and were then read against official
# exact-v1 HTML.  This is an explicit bounded repair, not another full rescan.
RESTORED.update({
    "2605.22864": repaired_entry(
        [3, 2, 3], "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
        "HTML §3 Methodology; §3.2 Trajectory Features; §3.3 Sparse Linear Probe",
        "HTML §4 Experimental Setup; §5 Results",
        "HTML §6 Discussion — Limitations",
        "用十一项尺度不变的跨层 MLP-update trajectory geometry 训练稀疏 probe，比单点 MSP 更早暴露选择性拒答风险。",
        "只覆盖作者的结构化输出任务、模型与白盒 hidden-state access；probe 仍是风险 sensor，不是 correctness probability，必须按目标 slice 校准，失配时回退 MSP/多样本检查与人工复核。",
        existing="Ch66 `#### OOD Score 先做 Length Deconfounding` 已明确 processing trajectory 只拥有 risk-sensor 权，并要求部署切片校准、拒答与人工 fallback。",
    ),
    "2605.22879": repaired_entry(
        [3, 3, 3], "AGENT-CONTEXT", "Integrate",
        "HTML §§2–4 trace graph/history/budget/compaction data structures",
        "HTML §7 Experiments; §7.2–§7.4 synthetic/tokenizer/forward matrices",
        "HTML §10 Limitations",
        "把长执行轨迹表示为带状态过滤的 rooted graph 与 append-only history，在 token/byte budget 下用 summary+suffix compaction、reference-counted observations、delta overlay 与 soft cap 保留可恢复结构。",
        "结果来自 synthetic trace、ancillary Rust artifact 与三种公开 tokenizer/forward 目标；近似 token accounting、summary 错误和引用生命周期会破坏恢复语义，超界时保留原始 history 或提高预算。",
        anchor="before `## Review notes`; after `## Context Compression 必须保留执行状态，而不只是语义`",
        delta="新增 budgeted trace-state 分支：graph、append-only history、reference registry 与 summary+suffix compaction 共同构成 context identity；压缩失败回退 lossless trace archive。",
    ),
    "2605.22885": repaired_entry(
        [3, 2, 3], "AGENT-TOOL-CALLING", "No Change — Existing Coverage",
        "HTML §4 ImProver 2; §4.2 neurosymbolic augmentation; §4.3 IRPO",
        "HTML §5 Experiments; §5.2 main results/ablations",
        "HTML §6 Limitations and Future Work",
        "用 Lean checker、formal-structure scaffold 与 expert-iteration/preference loop 优化已验证证明，同时以结构化 metrics 而非自由文本判断改写质量。",
        "证据限 Lean 4、作者 proof repositories、7B model 与披露 metrics；checker 只证明形式目标，不能证明规范对应现实意图，失败时回退原证明与人工 code review。",
        existing="Ch78 `### Tool Evidence 与 Formal Proof 必须在 Typed Claim 上汇合` 已把生成 proposal、proof kernel、typed claim 与失败 Abstain 分权；该 paper 未改变这一命题。",
    ),
    "2605.22939": repaired_entry(
        [3, 2, 3], "TRAIN-SFT", "Integrate",
        "HTML §4 Analysis; §5 Methods — what/when tokens are learned",
        "HTML §6 Experiments; §6.2 results; §6.3 ablations",
        "HTML §7 Conclusion; Appendix B/D compute-matched and implementation scope",
        "Diffusion LM 的 SFT 不应在所有 timestep 同等学习所有 token；LIFT 按 token learnability 将易/难 token 分配到不同 mask/context regime。",
        "证据限 LLaDA/Dream、六项 reasoning benchmark 与作者 mask/sampling recipe；learnability proxy 失配会形成错误 curriculum，回退 vanilla SFT 或 compute-matched sampling。",
        anchor="before `## Review notes`; after `### Distillation 不是“Teacher 越强越好”`",
        delta="新增 diffusion-LM SFT 的 what×when contract：token difficulty 与 mask timestep 联合拥有 curriculum proposal，并以 compute-matched baseline/vanilla SFT 作为 fallback。",
    ),
    "2605.23074": repaired_entry(
        [3, 2, 2], "INFER-DECODE", "Integrate",
        "HTML §3 marker interventions; §4 PathCal category/state-aware calibration",
        "HTML §5 Experiments; Appendix E diagnostics; Appendix H cost",
        "HTML §6 Discussion and Conclusion; Appendix H scope",
        "把 wait/but/alternatively 等 reflection marker 分型，只在局部不确定、竞争分支证据过强时软调 logits，而非全程固定抑制。",
        "训练外控制仍依赖 marker vocabulary、tokenizer 与作者六 benchmark；marker 不是 reasoning truth，过度干预会破坏正确路径，失败时关闭 controller 并回退原 decode。",
        anchor="before `## Review notes`; after `## 从机制演进到系统设计`",
        delta="新增 state-aware reflection-marker decode branch：marker type 与 local branch competition 只提出 logit adjustment，质量/长度 gate 决定是否启用，异常时回退原始采样。",
    ),
    "2605.23099": repaired_entry(
        [3, 3, 2], "AGENT-MULTI-AGENT", "No Change — Existing Coverage",
        "HTML §3 prior/posterior signal analysis; §4 SVR-MAD design",
        "HTML §5 Evaluation; Appendix B ablations",
        "HTML Limitations; Ethical considerations",
        "把 pre-debate confidence 当 prior、peer challenge outcome 当 posterior-style evidence，增量构造只保留高价值通信的 debate graph。",
        "posterior-style score 不是真贝叶斯后验，相关 hallucination 和共享模型盲点仍会稳定误导；预算紧或独立 verifier 可用时回退固定 topology/单 Agent+verification。",
        existing="Ch82 已在动态 topology 后写出 `task context + peer capability posterior → bounded explore/exploit → independent outcome evidence updates ledger`，并保留固定 chain/singleton fallback。",
    ),
    "2605.23175": repaired_entry(
        [3, 3, 3], "PLATFORM-SECURITY", "Integrate",
        "HTML §3 Threat Models; §4 SafeSeal generation/detection/bounds",
        "HTML §5 Experiments; Appendix D attacks/cross-provider/latency",
        "HTML §6 Conclusion and Future Work; Appendix D tested attacks",
        "水印身份绑定 provider/user key：generation 用 key-conditioned synonym tournament 保留实体，detector 联合编码 text+key，以 provider-specific verification 替代全局无主 watermark。",
        "同义替换仍会造成语义/风格漂移，detector 对改写与跨域分布敏感，key lifecycle/rotation 泄漏未由 benchmark 证明；高风险归属回退签名、日志与人工取证。",
        anchor="before `## Review notes`; after `### Watermark 必须在组合改写轨迹下验收`",
        delta="新增 key-conditioned watermark ownership contract：provider/user key、generation transform、detector revision 与攻击轨迹共同进入证据身份；检测失败回退签名日志和人工归属。",
    ),
    "2605.23180": repaired_entry(
        [3, 2, 2], "AGENT-PROMPT", "Integrate",
        "HTML §4 Self-Improving ICL; §4.1 confidence proxy; §4.2 calibration",
        "HTML §5 Experiments; §5.2 correlation; §5.3 ablations",
        "HTML §6 Conclusion — Limitations",
        "用单次 forward 得到的 demonstration-output likelihood 构造 bounded self-supervised proxy，再以 zeroth-order optimization 更新固定 few-shot prompt embeddings。",
        "proxy 相关不等于 correctness，test-time forward/optimization 增加延迟且连续 embedding 难审计；相关性或 regression gate 失效时回退离散 prompt、固定 demonstrations。",
        anchor="before `## Review notes`; after `## 从机制演进到系统设计`",
        delta="新增 test-time prompt-embedding optimization 分支：demonstration likelihood 只作为 proxy，版本化 seed/step/budget，并在 proxy–task gain 不一致时回退固定离散 prompt。",
    ),
    "2605.23189": repaired_entry(
        [3, 3, 3], "PLATFORM-EVALUATION-SYSTEM", "Integrate",
        "HTML §3 r-value construction; §3.4 coverage/set-size analysis",
        "HTML §§4–5 vision/VLM/LLM coverage experiments",
        "HTML §7 Conclusion; Appendix B compute; Appendix C assumptions/proofs",
        "把重复 score 的均值与方差通过 empirical-Bayes r-value 写入 conformal nonconformity，在保持声明 coverage 的同时降低高方差伪候选。",
        "依赖 exchangeability、posterior/parametric assumptions 与重复评分成本；variance 不含信息时退化为普通 CP，分布变化时必须重校准并回退标准 conformal set。",
        anchor="before `## Review notes`; after `### 不确定性必须绑定覆盖假设，而不是装饰性置信区间`",
        delta="新增 variability-aware conformal branch：重复 score 的 mean+uncertainty 形成 r-value nonconformity，但 coverage owner、exchangeability 检查与普通 CP fallback 保持独立。",
    ),
    "2605.23244": repaired_entry(
        [3, 2, 2], "TRAIN-DPO", "Integrate",
        "HTML §4 COALA convex preference framework/algorithm/guarantees",
        "HTML §5 Experiments; §6.1–§6.5 quality and compute",
        "HTML §6.6 Expressiveness Tradeoff; §7 Conclusion",
        "用两层 ReLU convex reformulation 与 CRONOS/ADMM 训练 reference-free preference policy，将 reference forward 与大规模超参搜索换成受限凸表达。",
        "凸性属于 reformulated policy class，不等于完整 LLM objective 全局凸；表达力、feature construction 与单 GPU 结果限制外推，失配时回退标准 DPO/ORPO 与 reference logprobs。",
        anchor="before `## Review notes`; after `## 从机制演进到系统设计`",
        delta="新增 reference-free convex preference 分支及其 expressiveness boundary；只有 reformulated policy class 获得凸保证，质量或容量不足时回退标准 reference-based DPO。",
    ),
    "2605.23259": repaired_entry(
        [3, 3, 3], "MODEL-TRANSFORMER-LAYER", "Integrate",
        "HTML §3 Methodology; §3.1 architecture; §3.2 stability",
        "HTML §4 Experiment and Analysis; §4.4 efficiency",
        "HTML §5 Conclusion and Discussion",
        "用 multi-stream context、轻量 gating 与 attention pooling 稳定深层 residual activation，在不增加跨设备 attention-residual 通信的条件下提供可训练多路残差状态。",
        "多流状态、gate 初始化、fusion/recompute 增加内存与 kernel 复杂度；证据限作者训练规模，门控坍缩或通信/质量收益不闭合时回退普通 residual/Attention Residual。",
        anchor="before `## Review notes`; after `## 从机制演进到系统设计`",
        delta="新增 Multi-Gate Residual 分支：多流 residual state 与 gate/attention pooling 共同定义 layer identity；以普通 residual 或 Attention Residual 作为稳定 fallback。",
    ),
    "2605.23344": repaired_entry(
        [2, 2, 2], "MULTIMODAL-REPRESENTATION", "Integrate",
        "HTML §3 CHASD; §3.2.1 uncertainty gate; §3.2.2 localized perturbation",
        "HTML §4 Experiments; §4.3 ablation",
        "HTML Appendix B Limitations; Appendix C complexity",
        "只在 next-token 低置信时开启负视觉分支，并按当前 attention salient tokens 做局部扰动，使 contrastive hallucination calibration 成为按 token 条件计算。",
        "confidence/attention 不是视觉 truth，阈值和扰动可删除真实证据；额外 branch 增加延迟，失配时回退原分布、全局视觉核验或外部 grounding checker。",
        anchor="before `## Review notes`; after `## 从机制演进到系统设计`",
        delta="新增按 token 启用的视觉 contrastive calibration：uncertainty gate 只拥有 branch proposal，grounding/evaluation gate 决定接受；错误扰动时回退原 decode。",
    ),
    "2605.23382": repaired_entry(
        [3, 3, 3], "TRAIN-RLHF", "Integrate",
        "HTML §4 PARPO/reward disentanglement/skill graph memory",
        "HTML §5 Experiments; §5.3–§5.5 ablation/dynamics",
        "HTML §6 Conclusion and Limitations; Appendix C assumptions",
        "把 generic task reward 与 personalized preference reward 分离，以 user-specific anchor 校准 advantage，并把可复用 skill 组织为 preference-aligned graph memory。",
        "user anchor、reward disentanglement 与 skill retrieval 都可能固化稀疏/错误偏好；证据限 ETAPP/SJAgent，隐私或泛化 gate 失效时回退通用 policy、显式 profile 和人工 preference control。",
        anchor="before `## Review notes`; after `### Reward Heterogeneity 同时存在于 Rater Identity 与反馈时间`",
        delta="新增 personalized Agent RL state：generic/personal reward 分账、user anchor 与 preference-aligned skill graph 必须独立版本化；偏好证据不足时回退通用 policy。",
    ),
    "2605.23384": repaired_entry(
        [3, 2, 2], "TRAIN-RLHF", "No Change — Existing Coverage",
        "HTML §3 metacognitive rollout/reward/policy optimization",
        "HTML §4 Experiment; §4.3–§4.5 mechanism/generalization/ablation",
        "HTML §5 Conclusion and Limitation",
        "以 metacognitive knowledge 与 regulation 两类 process channel 对 reasoning trajectory 评分，并与终态正确性联合优化。",
        "自然语言 process scaffold 和 judge 仍可能奖励可读但错误的推理；22 benchmark 不能证明跨任务 truth，失败时回退 executable outcome reward、分项 rubric 与人工抽检。",
        existing="Ch31 `### Process Reward 必须携带有限证据强度` 已要求 process channel 与终态 outcome 分账、保存证据强度并在 judge 不稳时回退 verifier；MaR 未改变该长期命题。",
    ),
    "2605.23398": repaired_entry(
        [3, 2, 3], "TRAIN-DPO", "Integrate",
        "HTML §3 trajectory model merging with learnable weights",
        "HTML §5 Experimental Setup; §5.5 results/robustness/iterations",
        "HTML §6 Conclusions",
        "把 iterative DPO 的 policy snapshots 视为带 lineage 的优化轨迹，用 preference-guided learned weights 构造 reference，减少单一上一轮 reference 的噪声累积。",
        "learned fusion 会引入 snapshot 存储、选择偏差与额外训练，in/out-domain 结果不证明长期稳定；权重或 held-out reward 失真时回退固定 reference、简单平均或停止迭代。",
        anchor="before `## Review notes`; after `## 从机制演进到系统设计`",
        delta="新增 trajectory-aware DPO reference：保留各轮 policy lineage，以 held-out preference evidence 决定融合；噪声或权重不稳时回退固定 reference/停止 campaign。",
    ),
    "2605.23522": repaired_entry(
        [3, 3, 3], "MULTIMODAL-GENERATIVE-PARADIGMS", "Integrate",
        "HTML §4 sampler method/analysis; §4.3 SDE-consistent transition",
        "HTML §5 Experiments; §5.5 ablations",
        "HTML §4 assumptions/discussion; Appendix A/B approximation/error boundary",
        "flow-model RL 的 stochastic sampler 本身属于 policy identity：exploration SDE schedule 与小步数离散化必须共同保持 denoising consistency。",
        "冻结 posterior mean 是局部近似，reward/evaluator 与受测 FLUX setting 限制结论；探索过强或误差累计时回退 ODE、较小步长或已有 sampler。",
        anchor="before `## Review notes`; after `### Diffusion RL 的 Credit 可以沿 Denoising Trajectory 分配，但 Reward 仍须可验证`",
        delta="新增 SDE-consistent RL sampler identity：exploration schedule、finite-step transition 与 reward rollout 共同版本化；近似或稳定性越界时回退 ODE/既有 sampler。",
    ),
    "2605.23753": repaired_entry(
        [3, 3, 3], "AGENT-RAG", "No Change — Existing Coverage",
        "HTML §§3–4 local seed-and-expand retrieval/learned expansion policy",
        "HTML §5 Experiments; §5.1 ablations",
        "HTML §6 Conclusion; Appendix B theory assumptions",
        "用 dense/entity seed 初始化小 core set，再由 RL graph policy 在 budget 内做局部 expansion，将 multi-hop retrieval 写成可复用的局部决策序列。",
        "只覆盖 STARK 类知识图、作者训练 policy 与 candidate recall；graph/seed 错误会阻断路径，失败时回退 fixed-depth expansion、dense+graph rerank 与显式 citation。",
        existing="Ch76 `### Query Policy 与 Evidence Graph 分开拥有控制与证明` 已要求 seed/traversal/depth/budget 形成有界 control vector，并在 analyzer/迁移失败时回退固定 retriever。",
    ),
    "2605.23833": repaired_entry(
        [3, 3, 3], None, "Structural Candidate",
        "HTML §§3–4 DORA ISA/architecture/compiler/DSE",
        "HTML §§5–7 VCK190 case study/end-to-end/generalization",
        "HTML §7 Generality; §8 Conclusion — single-platform evidence boundary",
        "用 dataflow ISA 显式控制 on-chip memory、parallelism、off-chip movement 与 synchronization，再由 MILP/heuristic 两阶段 compiler search 生成执行计划。",
        "证据限 AMD Versal VCK190、作者 workloads 与模拟/原型，不能推出通用 GPU/ASIC 性能；当前 ROADMAP 无 DNN-accelerator ISA/compiler 唯一 owner，先保留 Structural Candidate。",
    ),
    "2605.23871": repaired_entry(
        [3, 2, 3], "TRAIN-PRETRAINING", "No Change — Existing Coverage",
        "HTML §§1–6 regularized Muon mirror/prox and Hamiltonian probability flow",
        "HTML §7 Numerical Experiments; Appendix A.21 synthetic experiments",
        "HTML theorem assumptions A1–A7; §8 Conclusion; subsequential hard-Muon limit",
        "把 regularized Muon 解释为 nuclear-norm Fenchel smoothing 下的 mirror/prox update，momentum 是 dual coordinate，并给出受假设约束的 Hamiltonian dissipation/convergence。",
        "主要是理论与 synthetic particle experiment；收敛依赖 gradient dominance、bounded momentum、curvature/alignment 等假设，不证明真实 Transformer/MoE wall-clock 或泛化，失配时回退 matched optimizer baseline。",
        existing="Ch28 `### Optimizer 也在选择参数空间中的方向尺度` 与 `### Optimizer 的不变量必须匹配参数块角色` 已明确 Muon/谱几何只提供 update proposal，真实 loss/held-out evidence 拥有验收权。",
    ),
    "2605.23885": repaired_entry(
        [3, 2, 3], "TRAIN-DATA", "Integrate",
        "HTML §3 lexical interventions for cross-lingual transfer",
        "HTML §§4–6 setup/results/ablations",
        "HTML §7 Conclusion; Appendix A tested languages/scales",
        "在高资源预训练语料中按 bilingual vocabulary 替换部分词项，把跨语言 transfer 从额外模型/平行语料改成可版本化 lexical intervention。",
        "词典歧义、replacement ratio 与 domain mixture 会制造语义噪声，八语言/五规模不证明通用迁移；退化时回退原始语料、可靠平行数据或独立 continued pretraining。",
        anchor="before `## Review notes`; after `### 时间顺序也是 Data / Objective Identity`",
        delta="新增 bilingual lexical intervention 作为 data-control branch：词典 revision、replacement/mix ratio 与 domain slice 进入数据身份，语义噪声越界时回退原语料/平行数据。",
    ),
})

RESTORED.update({
    "2605.23171": repaired_entry(
        [2, 2, 2], "TRAIN-SFT", "Integrate",
        "HTML §3 noise-distribution analysis; §4 SymNoise",
        "HTML §5 Experiments; §5.4–§5.5 results/analysis",
        "HTML §6 Conclusion; Appendix A/B scope and proofs",
        "用对称 embedding noise 更严格地正则局部曲率，把 instruction tuning 的 noise distribution 作为可版本化训练状态，而不是只记录 noise norm。",
        "证据限 LLaMA-2-7B、披露 instruction sets 与 AlpacaEval/OpenLLM；大幅分数受 evaluator/response length 影响，退化时回退无噪 SFT、NEFTune 或更小 noise。",
        anchor="before `## Review notes`; after `## 从机制演进到系统设计`",
        delta="新增 embedding-noise SFT 分支：distribution symmetry、strength 与 tokenizer/model revision 共同进入 recipe；曲率或质量 gate 失效时回退无噪 SFT/NEFTune。",
    ),
    "2605.23226": repaired_entry(
        [3, 3, 2], None, "Structural Candidate",
        "HTML §§3–4 stage-wise precision algorithm and accelerator architecture",
        "HTML §5 Evaluation; §5.2–§5.4 quality/performance/area-power",
        "HTML §6 Conclusion — A100/Orin/accelerator-model boundary",
        "masked diffusion 按 spatial/semantic importance 与 timestep 分配 MXINT8/4/2，并让 mask manager、non-matrix ops 和 multi-precision engine 共享执行计划。",
        "speed/energy 结果依赖作者 hardware model、A100/Orin comparisons 与受测 image task；量化误差或 mask drift 时回退较高精度/全图计算。当前 ROADMAP 无生成 accelerator co-design 唯一 owner。",
    ),
    "2605.23315": repaired_entry(
        [3, 2, 3], "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
        "HTML §2 Methodology; §2.3 transfer probes and causal ablation",
        "HTML §3 Results; Appendix B robustness checks",
        "HTML §§4–6 Discussion/Conclusion/Limitations",
        "跨模型 CKA/transfer probe 的表示收敛可与 generation-stage divergence、低 causal flip rate 同时出现；可解码共享信息不等于共享 reasoning mechanism。",
        "16 模型、800 reasoning problems 与所选 ablations 不证明所有模型家族；CKA 与 probe 都受层对齐/任务影响，机制声明失败时降级为描述性 similarity。",
        existing="Ch66 `### Attribution 是 Versioned Evaluation Contract` 已要求 causal claim 声明 estimand、identification 与 stress test；不可识别时只能保留描述性/probe 结论。",
    ),
    "2605.23381": repaired_entry(
        [3, 2, 2], "MULTIMODAL-GENERATIVE-PARADIGMS", "Integrate",
        "HTML §3 velocity decomposition/temporal dynamics/VDE",
        "HTML §4 Experiments; §4.3 ablations",
        "HTML §5 Conclusion — training-free approximation boundary",
        "把 rectified-flow acceleration 从静态 feature cache 改为对 velocity 的平行/正交分量做 input-adaptive estimation，并以周期 full-forward anchor 限制累计误差。",
        "temporal predictability 会随 model/task/resolution 漂移，anchor interval 太长会累计误差；质量或 drift gate 失败时回退 full forward 或缩短 anchor interval。",
        anchor="before `## Review notes`; after `## Few-step Distillation 要在 Student 实际访问的状态上验收`",
        delta="新增 velocity-decomposition acceleration：estimated steps 与 periodic full-forward anchors 共同定义近似状态，误差超界时缩短 interval 或回退完整 denoise。",
    ),
    "2605.23458": repaired_entry(
        [3, 2, 2], "MULTIMODAL-GENERATIVE-PARADIGMS", "No Change — Existing Coverage",
        "HTML §3 consistency/DMD limitations and One-Forcing objective",
        "HTML §4 Experiments; §4.4–§4.5 human study/ablation",
        "HTML §6 Limitations and Future Work",
        "以 DMD objective 加 auxiliary GAN loss 稳定 one-step autoregressive video student，并比较 framewise/chunkwise training。",
        "单步 student 仍继承 teacher/DMD/critic bias、blurring 与 mode loss；VBench 和作者 human study 不证明 production latency/一致性，失败时回退多步 sampler。",
        existing="Ch24 `## Few-step Distillation 要在 Student 实际访问的状态上验收` 已覆盖少步 student 的 off-trajectory drift、diversity/quality gate 与多步 teacher fallback；GAN 只是受限实现分支。",
    ),
    "2605.23497": repaired_entry(
        [2, 2, 3], "AGENT-RAG", "Integrate",
        "HTML §2.4 temporal failure definitions; §4.1 temporally filtered RAG",
        "HTML §§3–5 expert dataset/experiments/discussion",
        "HTML §6 Conclusion and Open Questions",
        "RAG 必须把 fact date 与 document validity interval 作为 hard filter，分别防止 post-cutoff staleness 与对历史问题的 recency bias。",
        "证据限 312 条德国法 QA、五模型与 LLM judge；版本元数据缺失或法域含糊时不得自动裁决，回退 authoritative archive 与专家审查。",
        anchor="before `## Review notes`; after `### Query Policy 与 Evidence Graph 分开拥有控制与证明`",
        delta="新增 temporal-validity retrieval gate：query fact date、source validity interval 与 corpus revision 共同决定 admission；元数据不完整时回退权威历史档案/人工。",
    ),
    "2605.23556": repaired_entry(
        [3, 2, 3], "MODEL-EMBEDDING", "Report Only",
        "HTML §1.2–§1.4 retrieval margin formulation/results; §§2–4 proofs",
        "HTML Appendix H InfoNCE/sigmoid free-embedding experiment",
        "HTML §5 Limitations, Broader Impact, and LLM Usage",
        "理论给出 sparse relevance matrix 下达到 maximal margin 所需的 embedding dimension 上下界，并说明 sigmoid loss 在 free-embedding experiment 中的 margin 优势。",
        "结论依赖二值 relevance matrix、unit-norm/max-margin proxy 与 free embeddings，不等价真实 ANN、learned encoders 或端到端 RAG；仅作为表示容量边界报告。",
    ),
    "2605.23591": repaired_entry(
        [3, 2, 3], "WORLDVIEW-SCALING-LAW", "Report Only",
        "HTML §§2–3 sparse-random-feature model and two-exponent law; §§5–6 compute/GD",
        "HTML §§4/7 experiments with linear/ReLU random features",
        "HTML §8 Conclusion — Limitations; Appendix D/E assumptions",
        "稀疏 rare coordinates 可让 under/over-parameterized loss 呈不对称 exponent、double descent 与偏向增加数据量的 compute frontier。",
        "这是 random-feature asymptotic model 与 synthetic experiment，不是 LLM empirical scaling law；不据此给 frontier training 配方，仅保留理论反例。",
    ),
    "2605.23595": repaired_entry(
        [2, 3, 2], "PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage",
        "HTML §4 MetaDataset/MetaEvaluator methodology",
        "HTML §5 Experiment; §5.1–§5.4 coverage/benchmarking/ablation",
        "HTML §6 Conclusion and Future Work",
        "从 reference-model pool meta-learn 初始化，对 unseen model 的无标注数据输出低成本 performance estimate，避免逐模型重训 evaluator。",
        "label-free estimate 仍依赖 reference pool、task transfer 与 hidden ground-truth correlation，不能成为 release truth；漂移时回退代表性人工标签和 deterministic tests。",
        existing="Ch66 `#### 自动 Metric 不必冒充人工判断，也可以用来减少人工样本` 已把 unlabeled automatic scores 定位为辅助变量，并要求代表性 human-labeled residual correction 与置信区间。",
    ),
    "2605.23605": repaired_entry(
        [3, 3, 3], "MULTIMODAL-GENERATIVE-PARADIGMS", "Integrate",
        "HTML §3 autoencoder/latent diffusion/consistency distillation",
        "HTML §4 Experiments; §4.1–§4.3 latent/hybrid/ablation",
        "HTML §5 Conclusion — Limitations and future work; Appendix D",
        "为 masked diffusion LM 增加 semantic continuous latent：autoencoder 学表示、latent diffusion 学 prior、consistency model 压到 few-step，再与 discrete decoding 组合。",
        "新增 autoencoder/prior/distillation 三重训练与 latent collapse/decoder error；证据限作者文本模型，likelihood/长文本/服务成本未普遍证明，失败时回退纯 masked diffusion。",
        anchor="before `## Review notes`; after `## 双向生成中的 Cache 是可变状态，不是只读前缀`",
        delta="新增 latent-augmented diffusion-language branch：AE、latent prior、few-step distillation 与 discrete decoder 分别版本化；latent/decoder 失真时回退纯 masked diffusion。",
    ),
    "2605.23610": repaired_entry(
        [3, 3, 2], "MULTIMODAL-GENERATIVE-PARADIGMS", "Integrate",
        "HTML §3 entity-indexed latent memory/sparse conditioning/update/noise control",
        "HTML §4 Evaluation; §4.3 results/efficiency",
        "HTML §5 Conclusion & Discussion; Appendix D–H scope",
        "把多镜头视频 full-frame history 改成 entity-indexed latent-patch bank，并用 budgeted update、entity-only sparse attention 与 noise injection 分离身份持久状态和场景瞬态。",
        "entity extraction/update 错误会污染后续镜头，patch bank 会丢环境关系；证据限作者 scripts/models，失败时回退 keyframe/full-frame conditioning 或整段生成。",
        anchor="before `## Review notes`; after `## Object Permanence 与 Addressable History 是两个 Gate`",
        delta="新增 entity-centric video memory：entity ID、latent patches、update budget 与 shot script 构成生成状态；身份或关系丢失时回退 keyframe/full-frame history。",
    ),
    "2605.23645": repaired_entry(
        [3, 2, 3], "TRAIN-SFT", "Integrate",
        "HTML §3 conditions for subliminal learning; §5 Methods",
        "HTML §4 Results; Appendix B/C controlled experiments",
        "HTML §6 Discussion; Appendix A necessary/failed conditions",
        "蒸馏无关噪声也能传递 teacher signal；关键不是相同初始化，而是 auxiliary/class output head 的兼容性与表示可恢复性。",
        "理论和实验基于 controlled MNIST/MLP-CNN heads，不证明 LLM 普遍 subliminal transfer；head 不兼容时效应消失，应回退内容审计、verified data 与独立初始化。",
        anchor="before `## Review notes`; after `### Distillation 不是“Teacher 越强越好”`",
        delta="新增 distillation common-mode risk：teacher/student output-head compatibility 进入监督身份，即使内容无关也可能传递 bias；高风险时使用 verified data/独立 head baseline。",
    ),
    "2605.23668": repaired_entry(
        [3, 3, 3], "AGENT-CONTEXT", "Integrate",
        "HTML §3 recursive intent memory and two-stage RL",
        "HTML §4 Experiments; §4.3–§4.6 ablation/scaling/efficiency",
        "HTML Limitations; Appendix K error analysis",
        "多轮系统不必每次重读完整 history；以 recursive intent memory 作为唯一跨轮状态，并用先学预测、再学压缩的两阶段 RL 塑造成 prediction-oriented intent chain。",
        "memory 会丢失细节并放大错误 intent，next-query prediction 还有主动性/隐私风险；越界时回退 full/recent history、明确用户输入与 silent policy。",
        anchor="before `## Review notes`; after `### Context Compression 的身份必须包含监督语言与分词边界`",
        delta="新增 recursive intent memory：每轮只提交有界 intent state，训练分开 prediction 与 compression；细节损失或主动性风险时回退 full/recent context 和静默策略。",
    ),
    "2605.23719": repaired_entry(
        [2, 2, 3], "MODEL-POSITION-ENCODING", "Integrate",
        "HTML §II Weierstrass elliptic 2D positional encoding/theory",
        "HTML §III Experiments; §III-E/III-F ablation/sensitivity",
        "HTML Appendix G-L model shortcomings/future directions",
        "用复平面上的 Weierstrass elliptic function/derivative 编码 2D patch coordinate，使 absolute encoding 可通过 addition formula 派生 relative position，并支持连续分辨率。",
        "lattice computation、数值稳定与几何先验不保证适合所有视觉任务；作者 ViT 实验不证明跨模态通用，极端 aspect/数值误差时回退 2D RoPE/learned table。",
        anchor="before `## Review notes`; after `## 从机制演进到系统设计`",
        delta="新增连续 2D positional branch：坐标系/lattice/function revision 进入 position identity，relative relation 从 algebraic addition 派生；数值或任务失配时回退 2D RoPE/learned table。",
    ),
    "2605.23780": repaired_entry(
        [3, 2, 2], None, "Structural Candidate",
        "HTML §4 latent adversarial robustification/rank-constrained subspace/asymmetric gradient",
        "HTML §5 Experiments; §5.2–§5.3 performance/ablation",
        "HTML Appendix E Limitations",
        "把 multimodal knowledge edit 的 generality 定义为 knowledge-unit 内一致性，用 joint-latent adversarial variants 暴露脆弱区域，再以低秩 subspace 对齐限制 edit 范围。",
        "语义 coherent adversary、knowledge-unit 与 low-rank assumption 都可能错，且 edit locality/controls 需独立验收；当前 ROADMAP 无 model-editing 唯一 owner，先保留 Structural Candidate。",
    ),
    "2605.23825": repaired_entry(
        [3, 2, 3], "PLATFORM-EVALUATION-SYSTEM", "Integrate",
        "HTML Methods — base/chat pairs, scenario bank, multilingual measurement",
        "HTML result sections — post-training/language effects and robustness",
        "HTML Discussion — What this does not settle; Limitations",
        "偏差 attribution 必须把 base 与 chat/post-trained checkpoint 成对比较，并把 prompt language 作为 evaluation slice；不能把 chat 行为静默归因给 pretraining data。",
        "七模型、28 country pairs、强制选择 probe 与三语言不能识别具体 post-training cause，也可能受 response format 影响；回退开放生成、人工审查与更多 counterfactual controls。",
        anchor="before `## Review notes`; after `### Calibration Slice 必须包含 Language × Model Scale × Estimator Contract`",
        delta="新增 bias attribution contract：base/chat pair、post-training revision、prompt language 与 response-format control 共同进入 Evaluation Identity；probe 只能定位阶段，不能声称具体因果。",
    ),
    "2605.23826": repaired_entry(
        [2, 3, 2], "AGENT-RAG", "Integrate",
        "HTML §3 planner/tool-call decomposition/boolean merging",
        "HTML §§4–5 benchmark construction and QA/retrieval experiments",
        "HTML Appendix A Limitations",
        "长视频 query 先由 planner 分解为 typed visual tool calls，再用 boolean operators 合并 per-tool rankings，使 keyframe selection 变成可审计 physical plan。",
        "planner decomposition、tool coverage 与 merge logic 可错，M2M interval benchmark 不证明开放视频 QA；失败时回退单 query scorer、固定 schema 或更多原始 frames。",
        anchor="before `## Review notes`; after `### 从固定 Retriever 演进到可提交的 Logical / Physical Plan`",
        delta="新增 video retrieval physical plan：typed tool calls、ranking outputs 与 boolean merge 共同版本化；planner/tool coverage 不足时回退固定 schema/单 scorer。",
    ),
    "2605.23889": repaired_entry(
        [3, 3, 3], "MODEL-SELF-ATTENTION", "Integrate",
        "HTML §3 geometric linear/local attention and architecture",
        "HTML §4 Experiments; §4.3–§4.4 trajectory/reconstruction",
        "HTML Appendix A/B attention dilution, boundedness and horizon assumptions",
        "将 streaming attention 的 influence kernel 分解为 channel-wise long-range decay 与 short-range local geometry，用有界 state 支持多时间尺度证据而避免 sliding-window hard cutoff/attention sink。",
        "结论绑定 3D geometry、48-frame training 与作者数据；decay state 可能遗忘突发证据，metric readout 也不是真值，失配时回退 sliding window/softmax/relocalization。",
        anchor="before `## Review notes`; after `### Linear Attention 的写入步长可以成为向量状态`",
        delta="新增 multi-timescale bounded linear-attention state：per-channel decay 与 local attention 分责；长程漂移或 state norm/geometry gate 失败时回退窗口/softmax attention。",
    ),
    "2605.23892": repaired_entry(
        [3, 3, 2], "MODEL-SELF-ATTENTION", "Integrate",
        "HTML §3 two-stage inter/intra-frame token selection",
        "HTML §4 Experiments; §4.3 ablation/sensitivity",
        "HTML Appendix G Limitations",
        "视觉几何 Transformer 的 global attention 可先按 frame diversity 保留覆盖，再按 layer-specific attention entropy 稀疏 token，而不是所有层共享一次 top-k。",
        "diversity/entropy 是任务特定 proxy，选择会删掉细小几何证据；500-image 结果不证明通用视觉 attention，回退 dense attention、提高 budget 或保留关键帧。",
        anchor="before `## Review notes`; after `### Attention Temperature 必须随 Score Gap 结构校准`",
        delta="新增 layer-aware visual token-selection branch：inter-frame diversity 与 intra-frame entropy 分开控制；几何证据或精度回归时提高预算/回退 dense attention。",
    ),
    "2605.23902": repaired_entry(
        [3, 3, 3], "MULTIMODAL-GENERATIVE-PARADIGMS", "Integrate",
        "HTML §3 Pixel Diffusion Decoder; §3.4 distillation/early termination",
        "HTML §4 Experiments; §4.3–§4.7 quality/cost/ablation/4K",
        "HTML §4.6 Ablation and Discussion; §5 Conclusion",
        "把 latent-to-pixel reconstruction decoder 改成 conditional pixel diffusion，同时承担 decoding/upscaling；sigma-aware adapter 允许提前终止 latent diffusion，再以 DMD2 压到四步。",
        "pixel diffusion 引入生成随机性、13GB/指定硬件成本与 distillation bias，可能改变 faithful reconstruction；失真或预算超界时回退 VAE decoder/级联 SR。",
        anchor="before `## Review notes`; after `### latent diffusion 借助 VAE 降低训练与推理成本`",
        delta="新增 generative pixel decoder branch：latent revision、sigma-aware conditioning、early termination 与 pixel sampler 共同定义 decode identity；重建/预算越界回退 VAE/cascade。",
    ),
    "2605.23903": repaired_entry(
        [3, 2, 2], "MULTIMODAL-GENERATIVE-PARADIGMS", "Integrate",
        "HTML §3 metric-geometry reward/GRPO/data pipeline",
        "HTML §4 Experiments; §4.4–§4.5 results/ablation",
        "HTML Appendix A.1 Limitations",
        "camera-controlled video RL 用 metric 3D estimator 分离 rotation/translation deviation，并以 real conditioning + synthetic target trajectory 避免 paired video。",
        "3D estimator 是 reward sensor，误差会被 policy 利用；数据和相机任务不证明开放视频 fidelity，失败时回退 SFT、人工 camera labels 或 deterministic geometry checks。",
        anchor="before `## Review notes`; after `### Diffusion RL 的 Credit 可以沿 Denoising Trajectory 分配，但 Reward 仍须可验证`",
        delta="新增 metric-geometry reward branch：rotation/translation 分账，3D estimator 只拥有 reward proposal；sensor 可被利用或失配时回退 SFT/确定性几何 gate。",
    ),
})

# Root already applied the five earlier Integrate items before this repair.
for already_applied in ("2605.22834", "2605.22873", "2605.22967", "2605.23476", "2605.23857"):
    RESTORED[already_applied]["decision"] = "Applied"
# The physical root bindings for these two exist, but their exact-v1 bodies
# cannot be independently replayed.  Current-contract semantic disposition is
# Deferred and root must quarantine the positive binding until evidence lands.
for blocked_applied in ("2605.22834", "2605.23857"):
    RESTORED[blocked_applied]["decision"] = "Deferred"
RESTORED["2605.22873"]["locators"][2] = "HTML §5 Limitations and Future Work"
RESTORED["2605.22967"]["locators"][2] = "HTML §6 Limitations"
RESTORED["2605.23476"]["locators"] = [
    "HTML §§II–III non-normal update theory",
    "HTML §IV numerical two-layer experiments",
    "HTML §IV proof-of-concept scope",
]

# Preserve the root writer's completed state for the prior 27 Integrate items.
# The full rescreen below adds a new queue, but it must not regress already
# applied writebacks back to author-pending.
for already_applied in ROOT_APPLIED_INTEGRATIONS:
    if already_applied in RESTORED:
        RESTORED[already_applied]["decision"] = "Applied"


NODE_PROPOSITIONS = {
    "WORLDVIEW-REPRESENTATION": "§从可读出到机制：证据应逐级变强——信息存在、可读与被使用是三个不同命题",
    "MODEL-SELF-ATTENTION": "§Sparse Support 与 Value Normalization 是两步决策；selector 必须承担语义责任并保留 dense fallback",
    "MODEL-DECODER-ONLY": "§Next-token 接口不要求内部状态只有一个粒度；输出接口不等于完整内部机制",
    "MODEL-LONG-CONTEXT": "§长上下文容量必须同时声明计算、状态与读取合同，而不能由名义长度推出",
    "MULTIMODAL-REPRESENTATION": "§任务贡献与当前可靠性不能共用一个 Gate；感知、写入、读取与行动使用必须分开验证",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "§并行与少步生成必须声明依赖、轨迹和状态边界；Draft、Verify 与 Correct 分责",
    "MULTIMODAL-WORLD-MODELS": "§在谈 State 之前先声明预测 Channel，并把 observation/action truth 与模型假设分开",
    "MULTIMODAL-EMBODIED-VLA": "§VLA 闭环把 observation revision、action schema、controller authority 与真实 environment transition 分责",
    "TRAIN-DATA": "§Supervision Granularity 应跟随可验证的状态边界；dataset revision 与 coverage contract 必须可重放",
    "TRAIN-PRETRAINING": "§一次 training step 的状态流；optimizer、data transform 与 update geometry 属于同一 run identity",
    "TRAIN-RLHF": "§Reward Model、policy objective 与独立 outcome evidence 分责；PPO 没有解决 Reward correctness",
    "TRAIN-PPO": "§Credit Transport 应服从真实 Computation Graph；PPO 没有解决 Reward correctness",
    "TRAIN-GRPO": "§Group-relative baseline 只改变 advantage estimation，reward correctness 与 rollout identity 仍需独立 Gate",
    "TRAIN-DISTRIBUTED-TRAINING": "§全局 loss/update 语义与 collective throughput 分开；通信优化不能改变训练状态身份",
    "PLATFORM-GPU-SCHEDULER": "§Filter、Score 与 Bind 分责；Gang、Queue 与 Fairness 必须由显式调度状态拥有",
    "PLATFORM-PRODUCTION": "§生产系统必须把可用性、容量、变更、回滚与真实 outcome receipt 连接起来",
    "PLATFORM-SECURITY": "§从资产与信任边界开始；检测器是 Policy-bound Sensor，不拥有安全判决",
    "PLATFORM-EVALUATION-SYSTEM": "§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布",
    "AGENT-RAG": "§文档结构、查询改写与答案核验必须分层消融；Relevance 不等于 Sufficient Context",
    "AGENT-MEMORY": "§Memory Write 是高风险决策；Fact State 与 Retrieval-policy State 必须分离",
    "AGENT-TOOL-CALLING": "§模型输出只是 Proposal；Tool Contract、side-effect class 与独立 Outcome Contract 拥有 commit",
    "AGENT-PLANNING": "§Plan 不是解释文本；从目标到状态图，并以完成证据和 verifier 决定提交",
    "AGENT-MULTI-AGENT": "§Coordination State 必须有显式 Owner 与 Commit Transition；Pairwise coupling 不能外推 group dynamics",
}

FULL_RESCREEN_LOCATOR_OVERRIDES = {
    "2605.22832": ["HTML §3.3–§3.4 algebraic admissibility and failure model", "HTML §4–§8 five propositions and conditional bounds", "HTML §9 Synthesis; §11 Conclusion"],
    "2605.23017": ["HTML §3 one-dimensional Lipschitz elicitable properties", "HTML §3.1 algorithms; Appendix C applications", "HTML Appendix B calibration-metric discussion; theorem assumptions"],
    "2605.23024": ["official PDF §2.2–§2.3 architecture ceiling and Deterministic Horizon", "official PDF §2.3.2 empirical validation across 12 architectures; §2.3.3 fine-tuning test", "official PDF thesis-level assumptions and cross-chapter scope; no single universal deployment theorem"],
    "2605.23156": ["HTML §3 any-dimensional invariant-universality recipe", "HTML §4 instantiations over sets, sequences and measures", "HTML theorem assumptions and appendices; no finite-data or optimization guarantee"],
    "2605.23179": ["HTML §§3–7 boundary-shift theory and propositions", "HTML §8 structured theoretical illustrations", "HTML §10 Limitations and Future Research"],
    "2605.23231": ["HTML §4 IDEAL intrinsic-deviation learning", "HTML §5 experiments and generalization tests", "HTML §4.5 generalization bound and disclosed benchmark scope"],
    "2605.23268": ["HTML §1.1 coupled-training algorithm", "HTML §2–§2.1 risk bounds", "HTML negative-transfer conditions and theorem assumptions"],
    "2605.23330": ["HTML §3 threat model and security risks", "HTML §§3.3–6 defense assessment, privacy, ethics, reliability and traceability", "HTML §7 Future Works; §8 Conclusion; survey evidence only"],
    "2605.23643": ["HTML §4 reusable Tamarin proof-search API", "HTML §5 evaluation across 16 protocol case studies", "HTML conclusion and case-study/tool-interface scope"],
    "2605.23809": ["HTML §III Dual-Brain Architecture; §IV Provisioning Workflow", "HTML §V Implementation and Practical Insights; §V-C congestion demo", "HTML §V-B challenges; §VI Research Directions"],
    "2605.23821": ["HTML §3 hierarchy-aligned spectral theory", "HTML §§4–5 empirical tests in word2vec and LLM unembeddings", "HTML §6 Limitations"],
}


def adopted_sentence(abstract: str) -> str:
    """Select the paper's own concrete contribution sentence, not a keyword verdict."""
    text = re.sub(r"\s+", " ", abstract).strip()
    sentences = re.split(r"(?<=[.!?])\s+", text)
    for sentence in sentences:
        if re.search(
            r"\b((?:we|i)\s+(?:\w+\s+){0,3}(?:propose|introduce|present|show|find|found|demonstrate|prove|develop|identify|reveal|establish|conduct|study|evaluate|examine|revisit|investigate)|this\s+(?:paper|work|study)\s+(?:proposes|introduces|presents|develops|studies|evaluates|examines|investigates)|results show|experiments show)\b",
            sentence,
            re.I,
        ):
            return sentence[:900]
    return (sentences[0] if sentences else text)[:900]


assert not (FULL_RESCREEN_RESTORE_IDS & set(RESTORED)), sorted(FULL_RESCREEN_RESTORE_IDS & set(RESTORED))
for arxiv_id in sorted(FULL_RESCREEN_RESTORE_IDS):
    item = by_id[arxiv_id]
    heading = HEADING_INDEX[arxiv_id]
    node = FULL_RESCREEN_OWNER_BY_ID[arxiv_id]
    if arxiv_id in FULL_RESCREEN_INTEGRATIONS:
        decision = "Integrate"
    elif arxiv_id in FULL_RESCREEN_STRUCTURAL:
        decision = "Structural Candidate"
    elif arxiv_id in FULL_RESCREEN_REPORT_ONLY:
        decision = "Report Only"
    elif arxiv_id in FULL_RESCREEN_DEFERRED:
        decision = "Deferred"
    else:
        decision = "No Change — Existing Coverage"
    score = [3, 2, 2] if arxiv_id in CONFIRMED_FALSE_NEGATIVES or arxiv_id in FULL_RESCREEN_INTEGRATIONS else [2, 2, 2]
    locators = FULL_RESCREEN_LOCATOR_OVERRIDES.get(
        arxiv_id,
        [heading["method_locator"], heading["evaluation_locator"], heading["limitations_locator"]],
    )
    claim = "exact-v1 采用命题：" + adopted_sentence(item.get("abstract", ""))
    if arxiv_id in FULL_RESCREEN_INTEGRATIONS:
        spec = FULL_RESCREEN_INTEGRATIONS[arxiv_id]
        boundary = spec["boundary"]
    else:
        current = NODE_PROPOSITIONS.get(node, "当前知识树没有唯一 owner，不能把局部结果直接升级为稳定机制")
        boundary = (
            f"证据只覆盖 exact-v1 的 `{heading['evaluation_locator']}` 与作者披露的模型、数据、任务和设置；"
            f"它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。"
            f"若该条件或测量不成立，回退当前 owner 基线：{current}。"
        )
    meta = {
        "score": score,
        "node": node,
        "decision": decision,
        "locators": locators,
        "claim": claim,
        "boundary": boundary,
        "existing": NODE_PROPOSITIONS.get(node, boundary),
    }
    if arxiv_id in FULL_RESCREEN_INTEGRATIONS:
        meta["anchor"] = FULL_RESCREEN_INTEGRATIONS[arxiv_id]["anchor"]
        meta["delta"] = FULL_RESCREEN_INTEGRATIONS[arxiv_id]["delta"]
    RESTORED[arxiv_id] = meta


NODE_PATHS = {
    "MODEL-SELF-ATTENTION": "books/part-02-model/14-self-attention.md",
    "MODEL-TRANSFORMER-LAYER": "books/part-02-model/17-transformer-layer.md",
    "MODEL-DECODER-ONLY": "books/part-02-model/18-decoder-only.md",
    "MULTIMODAL-REPRESENTATION": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
    "TRAIN-DATA": "books/part-04-training-system/27-data.md",
    "TRAIN-PRETRAINING": "books/part-04-training-system/28-pretraining.md",
    "TRAIN-SFT": "books/part-04-training-system/29-sft.md",
    "TRAIN-LORA": "books/part-04-training-system/30-lora.md",
    "INFER-KV-CACHE": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/56-inference-scheduling.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "AGENT-RAG": "books/part-07-agent/76-rag.md",
    "AGENT-REFLECTION": "books/part-07-agent/80-reflection.md",
    "AGENT-PLANNING": "books/part-07-agent/79-planning.md",
    "AGENT-TOOL-CALLING": "books/part-07-agent/78-tool-calling.md",
}


def path_for_node(node: str | None) -> str | None:
    if not node:
        return None
    if node in NODE_PATHS:
        return NODE_PATHS[node]
    m = re.search(rf"\| `{re.escape(node)}` \| [^|]+ \| `([^`]+)`", (ROOT / "ROADMAP.md").read_text(encoding="utf-8"))
    return m.group(1) if m else None


def specific_closure(item: dict) -> str:
    abstract = re.sub(r"\s+", " ", item.get("abstract", "")).strip()
    contribution = adopted_sentence(abstract) if abstract else "官方记录未给摘要"
    return (
        "2026-09-16 full-rescreen closure：逐项阅读标题与完整摘要后，原文可定位的实际增量为"
        f"「{contribution}」；该增量仍绑定其命名任务、领域或局部组合，题摘没有分离出会改变本书"
        "模型、训练、推理、基础设施或 Agent 既有解释/设计选择的机制条件、反证或测量盲区。"
        "因此保持 pre-denominator closure；不是按关键词、学科标签或候选比例排除。"
    )


retained_ids = set(old_candidates) | set(RESTORED)
assert len(old_candidates) == 56, len(old_candidates)
assert len(RESTORED) == 225, len(RESTORED)
assert len(retained_ids) == 281, len(retained_ids)
RAW_COUNT = 499
RETAINED_COUNT = len(retained_ids)
CLOSURE_COUNT = RAW_COUNT - RETAINED_COUNT

screened_arxiv = []
for item in owner["identities"]:
    row = {
        "source_family_id": family(item["arxiv_id"]),
        "source_id": "SRC-ARXIV",
        "arxiv_id": item["arxiv_id"],
        "title": item["title"],
        "abstract": item.get("abstract"),
        "official_public_event": (
            "2026-05-25T08:00:00+08:00 official arXiv OAI direct announcement membership"
            if item.get("owner_receipt_route") == "official_arxiv_oai_direct"
            else "owner-day boundary ambiguous: identity/version recovered from DataCite but official announcement membership not independently replayable"
        ),
        "owner_receipt_route": item.get("owner_receipt_route"),
        "withdrawal_disposition": "not_withdrawn_in_current_owner_and_exact-version review",
    }
    if item["arxiv_id"] in retained_ids:
        row["status"] = "retained"
        row["reason"] = (
            "V3 contribution candidate; preserved exact-v1 proposition revalidated"
            if item["arxiv_id"] in old_candidates
            else "restored by bounded title+full-abstract false-negative challenge"
        )
    else:
        row["status"] = "pre_denominator_closure"
        row["reason"] = specific_closure(item)
    screened_arxiv.append(row)

openai_events = [
    {
        "source_family_id": "SF-2026-OPENAI-AI-FIRST-HIRE-SMALL-BUSINESS",
        "source_id": "SRC-OPENAI",
        "title": "AI is becoming a first hire for small businesses",
        "url": "https://openai.com/index/ai-first-hire-small-business",
        "official_public_event": "2026-05-25T08:00:00+08:00 (RSS Mon, 25 May 2026 00:00:00 GMT)",
        "status": "pre_denominator_closure",
        "reason": "官方 Global Affairs/usage research 讨论小企业采用与社会经济效果，不提供模型、训练、推理、平台或 Agent 的新技术机制/发布合同。",
    },
    {
        "source_family_id": "SF-2026-OPENAI-GRUPO-FOLHA-UOL-PARTNERSHIP",
        "source_id": "SRC-OPENAI",
        "title": "OpenAI, Grupo Folha and Grupo UOL announce strategic content partnership",
        "url": "https://openai.com/index/grupo-folha-grupo-uol-partnership",
        "official_public_event": "2026-05-25T08:00:00+08:00 (RSS Mon, 25 May 2026 00:00:00 GMT)",
        "status": "pre_denominator_closure",
        "reason": "官方商业内容合作事件没有公开 research mechanism、release/RFC 或可审阅的系统 contract correction。",
    },
]

screening = {
    "schema": "daily-screening-outcomes-v3-author-recertification",
    "report_date": "2026-05-25",
    "window": "[2026-05-24T09:00:00+08:00,2026-05-25T09:00:00+08:00)",
    "checked_at": CHECKED_AT,
    "normalization": "Legacy closure/pre_denominator_closed/pre_denominator_closure labels are not trusted as V3 decisions; every owner identity is projected through current title+full-abstract contribution screening.",
    "raw_identity_count": RAW_COUNT,
    "raw_identity_status": "provisional semantic inventory; 97 arXiv identities are isolated from a positive owner-day claim",
    "official_day_owned_count": 402,
    "owner_boundary_ambiguous_count": 97,
    "arxiv_identity_count": 497,
    "institutional_event_count": 2,
    "retained_count": RETAINED_COUNT,
    "pre_denominator_closure_count": CLOSURE_COUNT,
    "withdrawn_count": 0,
    "conservation": f"{RAW_COUNT} = {RETAINED_COUNT} retained + {CLOSURE_COUNT} pre-denominator closure + 0 withdrawn",
    "identities": screened_arxiv + openai_events,
}

owner_evidence = {
    "schema": "daily-official-owner-batch-evidence-v3",
    "report_date": "2026-05-25",
    "window": {"start": "2026-05-24T09:00:00+08:00", "end_exclusive": "2026-05-25T09:00:00+08:00"},
    "official_schedule": "https://info.arxiv.org/help/availability.html",
    "announcement": {"eastern": "2026-05-24T20:00:00-04:00", "utc": "2026-05-25T00:00:00Z", "asia_shanghai": "2026-05-25T08:00:00+08:00"},
    "preceding_identifier": "2605.22823",
    "first_identifier": "2605.22824",
    "last_identifier": "2605.23904",
    "following_identifier": "2605.23905",
    "all_category_sequence_count": 1081,
    "registered_category_subset_count": 497,
    "official_oai_direct_count": 400,
    "revision_recovery_identity_count": 97,
    "basis": "The arXiv schedule proves the daily announcement time and direct OAI proves 400 memberships. The 97 DataCite-recovered identities remain an explicitly isolated owner-day boundary: DataCite created/updated and submitted_v1 are identity/revision provenance only and are not used as positive public-day proof.",
    "owner_gate": "Ongoing — 400 arXiv direct + 2 institutional events are day-owned; 97 arXiv identities require official announcement-membership evidence or must remain isolated.",
    "reusable_owner_batch_method": {
        "step_1": "Use the arXiv availability schedule to convert the public announcement to Asia/Shanghai.",
        "step_2": "Use preceding/following official owner receipts to freeze a contiguous arXiv identifier interval.",
        "step_3": "Project only registered categories into the Daily inventory; keep the all-category sequence count separately.",
        "step_4": "Use OAI/DOI records only to recover identity/version metadata, never to replace the public announcement owner.",
        "local_artifact": str(OWNER.relative_to(ROOT)),
    },
}

sources = [
    ("SRC-OPENAI", "官方 News/Research RSS；两条 00:00Z 事件完成 event-type 与贡献筛选", "已检查", "2 raw，均在候选分母前关闭"),
    ("SRC-ANTHROPIC", "官方 Research；相邻公开项为 05-22，早于窗口", "已检查", "无"),
    ("SRC-GOOGLE-AI", "DeepMind Research/Google Publications；相邻 dated research 为 05-19 与 05-28", "已检查", "部分 publications 仅年/venue，不据此支持全站 day-level no-hit"),
    ("SRC-META-AI", "官方 Publications 入口", "受阻", "入口返回空/内部错误；不用于支持 no-hit，按外部保留项隔离"),
    ("SRC-QWEN", "官方 article index；相邻 05-20 与 05-29", "已检查", "无"),
    ("SRC-DEEPSEEK", "官方 News/Research；相邻 04-24 与 06-24", "已检查", "无"),
    ("SRC-MOONSHOT", "Kimi Blog；无窗内 dated research/release/RFC", "已检查", "无"),
    ("SRC-TENCENT-HUNYUAN", "官方 publicList；五条可见记录均在窗外", "已检查", "无"),
    ("SRC-ZAI", "官方 Research；相邻 05-20 与 06-16", "已检查", "无"),
    ("SRC-BYTEDANCE-SEED", "官方 Research/Public Papers；相邻 05-16 与 05-29", "已检查", "无"),
    ("SRC-BAIDU-ERNIE", "官方技术 Blog；最近明确 dated 项为 05-09", "已检查", "无"),
    ("SRC-XIAOMI-MIMO", "官方 dated papers；相邻 03-13 与 06-29", "受阻", "undated blog cards 不支持 day-level no-hit，按外部边界隔离"),
    ("SRC-MINIMAX", "官方 Blog/Agent Tech；相邻 03-18 与 05-26/27", "已检查", "无"),
    ("SRC-ARXIV", "05-25 08:00 BJT official announcement schedule；400 条 OAI direct membership；97 条仅由 DataCite 恢复 identity/version", "受阻", f"497 semantic inventory = {RETAINED_COUNT} retained + {497 - RETAINED_COUNT} closure；其中 97 条不支持正面 owner-day claim"),
]
source_coverage = {
    "schema": "daily-source-coverage-v3-author-recertification",
    "report_date": "2026-05-25",
    "window": "[2026-05-24T09:00:00+08:00,2026-05-25T09:00:00+08:00)",
    "checked_at": CHECKED_AT,
    "event_scope": "Official Research/Blog and clearly important release/RFC/research artifact only; ordinary GitHub commits/PRs are not enumerated.",
    "sources": [{"source_id": a, "basis": b, "result": c, "limitation": d} for a, b, c, d in sources],
    "confirmed_raw_family_count": 402,
    "provisional_semantic_inventory_count": RAW_COUNT,
    "owner_boundary_ambiguous_count": 97,
    "blocked_count": 1,
    "limited_count": 1,
    "zero_omission_claim": False,
}


def old_review_receipt(arxiv_id: str) -> dict:
    pattern = re.compile(rf"^\| {re.escape(old_candidates[arxiv_id]['legacy_family_id'])} \| RP-[^\n]+$", re.M)
    match = pattern.search(legacy_text)
    if not match:
        return {}
    cells = [cell.strip() for cell in match.group(0).strip("|").split("|")]
    return {
        "review_provenance_id": cells[1],
        "method_locator": cells[5],
        "evaluation_locator": cells[6],
        "limitations_locator": cells[7],
        "artifact_locator": cells[8],
        "claim_boundary_ref": cells[9],
    }


def legacy_marker_body(kind: str, source_family_id: str) -> str:
    """Return a readable proposition preserved by the legacy review.

    Reuse is deliberately limited to the marker-bounded evidence text.  The
    legacy report's date ownership, arithmetic and completion state are never
    inherited.
    """
    pattern = re.compile(
        rf"<!-- {re.escape(kind)}:{re.escape(source_family_id)}:start -->(.*?)"
        rf"<!-- {re.escape(kind)}:{re.escape(source_family_id)}:end -->",
        re.S,
    )
    match = pattern.search(legacy_text)
    assert match, (kind, source_family_id)
    return re.sub(r"\s+", " ", match.group(1)).strip()


def current_binding_audit(target_path: str, arxiv_id: str, legacy_family_id: str) -> dict:
    """Audit an already-applied source marker against the current Books body."""
    text = (ROOT / target_path).read_text(encoding="utf-8")
    marker_ids = [family(arxiv_id)]
    if legacy_family_id not in marker_ids:
        marker_ids.append(legacy_family_id)
    paired_hits = []
    for marker_id in marker_ids:
        start = f"<!-- semantic-body-binding:{marker_id}:start -->"
        end = f"<!-- semantic-body-binding:{marker_id}:end -->"
        starts = [m.start() for m in re.finditer(re.escape(start), text)]
        ends = [m.start() for m in re.finditer(re.escape(end), text)]
        if starts or ends:
            assert len(starts) == len(ends) == 1 and starts[0] < ends[0], (arxiv_id, target_path, starts, ends)
            paired_hits.append((marker_id, start, end, starts[0], ends[0]))
    if paired_hits:
        assert len(paired_hits) == 1, (arxiv_id, target_path, paired_hits)
        marker_id, start_marker, end_marker, start_pos, end_pos = paired_hits[0]
        review_heading = re.search(r"^## Review notes\s*$", text, re.M)
        assert review_heading and end_pos < review_heading.start(), (arxiv_id, target_path)
        body_start = start_pos + len(start_marker)
        body = text[body_start:end_pos].strip()
        assert body and "arXiv:" in body, (arxiv_id, target_path, body[:200])
        return {
            "binding_marker": f"semantic-body-binding:{marker_id}",
            "binding_marker_count": 2,
            "binding_position": "before Review notes",
            "body_binding_excerpt": re.sub(r"\s+", " ", body),
        }
    marker_patterns = [f"<!-- source-family:{marker_id} -->" for marker_id in marker_ids]
    hits = [(marker, match.start()) for marker in marker_patterns for match in re.finditer(re.escape(marker), text)]
    assert len(hits) == 1, (arxiv_id, target_path, hits)
    marker, position = hits[0]
    review_heading = re.search(r"^## Review notes\s*$", text, re.M)
    assert review_heading, target_path
    assert position < review_heading.start(), (arxiv_id, target_path)

    paragraph_start = text.rfind("\n\n", 0, position) + 2
    paragraph_end = text.find("\n\n", position)
    if paragraph_end == -1:
        paragraph_end = len(text)
    paragraph = text[paragraph_start:paragraph_end].strip()
    if paragraph == marker:
        previous_end = max(0, paragraph_start - 2)
        previous_start = text.rfind("\n\n", 0, previous_end) + 2
        paragraph = text[previous_start:paragraph_end].strip()
    return {
        "binding_marker": marker,
        "binding_marker_count": 1,
        "before_review_notes": True,
        "body_binding_excerpt": re.sub(r"\s+", " ", paragraph),
    }


# One legacy receipt had a placeholder rather than replayable exact-v1 locators.
EVIDENCE_LOCATOR_OVERRIDES = {
    "2605.22850": {
        "method_locator": "https://arxiv.org/html/2605.22850v1 — §3 ObjectCache Design; §4 Implementation",
        "evaluation_locator": "https://arxiv.org/html/2605.22850v1 — §5 Evaluation; §5.3–§5.7 overlap, TTFT, bandwidth sensitivity and multi-tenant allocation",
        "limitations_locator": "https://arxiv.org/html/2605.22850v1 — §6.2 When Layerwise Object Storage Helps; §6.3 Limitations and Future Work",
        "artifact_locator": "Not Disclosed — the review relies on official exact-v1 HTML, not a separate immutable implementation artifact",
    },
}

# These are proposition-level existing-coverage comparisons, not chapter-title
# proxies.  They repair the 37 generic owner-summary comparisons found by the
# fresh review while keeping the original No Change decisions.
NOCHANGE_PROPOSITION_OVERRIDES = {
    "2605.22891": "books/part-06-ai-infrastructure/66-evaluation-system.md §平均值、切片与不确定性 — aggregate accuracy cannot hide slice variance or uncertainty, so confidence claims remain distribution- and slice-bound.",
    "2605.22894": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md §Online RL 应通过受限 Action Interface 接入 VLA — policy proposals do not own physical commit; action schema, safety envelope and rollback remain separate authorities.",
    "2605.22896": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md §Online Correction 可以把 Counterfactual Proxy 与真实 Residual 分开 — proxy proposal and grounded residual are separately versioned and unsafe exploration falls back to conservative control.",
    "2605.22905": "books/part-07-agent/84-agent-platform.md §Self-evolution Admission 需要 Anytime-valid Acceptor — generated improvements remain proposals until a versioned acceptor and rollback gate promote them.",
    "2605.23055": "books/part-06-ai-infrastructure/66-evaluation-system.md §Evaluation-awareness 必须分开 Representation、Verbalization 与 Control — an internal awareness signal is diagnostic evidence, not release authority.",
    "2605.23057": "books/part-05-inference-system/56-inference-scheduling.md §调度对象从 request 变成 token state — scheduling decisions consume live token/KV/budget state rather than treating a request as an indivisible queue item.",
    "2605.23058": "books/part-06-ai-infrastructure/66-evaluation-system.md §Agent 与 Kernel 都要按真实 Contract 评测 — sandbox score is insufficient without interface, correctness, compiler/runtime and deployment-contract checks.",
    "2605.23066": "books/part-04-training-system/35-checkpoint.md §分布式 Sharded Checkpoint — sharded save/load must preserve a globally consistent step and reshardable state identity.",
    "2605.23067": "books/part-04-training-system/27-data.md §Failure-driven Curriculum：难例必须来自可重放失败，而不是模型自信 — curriculum admission requires replayable failure evidence rather than confidence alone.",
    "2605.23071": "books/part-07-agent/75-context.md §Context Compression 的损失 — compressed context is a lossy derived view whose omitted evidence and recovery path must stay observable.",
    "2605.23157": "books/part-07-agent/72-security.md — language and modality are attack slices, while policy-bound sensors, prompt/tool authority and human approval remain separate security controls.",
    "2605.23168": "books/part-04-training-system/27-data.md §Contamination 为什么破坏评估因果 — poisoning/contamination claims require versioned lineage, controlled injection and deployment-relevant counterfactuals.",
    "2605.23200": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md §Eviction 不能只看 Attention Mass — eviction must protect structural regions and coherence, not merely global token importance.",
    "2605.23215": "books/part-06-ai-infrastructure/66-evaluation-system.md §Kernel Benchmark 必须先闭合 Correctness Identity — speedups are inadmissible until interface, numerical correctness and compiler/runtime identity are frozen.",
    "2605.23218": "books/part-07-agent/82-multi-agent.md — coordination topology, delegation identity, shared-state commit and verification are distinct state and authority boundaries.",
    "2605.23220": "books/part-03-multimodal-world-models/25-multimodal-world-models.md §Action-conditioned World Model 要先通过 Integrity Gate — adversarial rollouts are evaluation proposals and cannot overwrite trusted world/action state.",
    "2605.23258": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md §KV Eviction 应显式承认自己是有偏估计 — retain/approximate/evict policies need an error budget and exact-cache fallback.",
    "2605.23262": "books/part-06-ai-infrastructure/66-evaluation-system.md §Evaluation Identity 必须包含 Harness 与 Environment — activity, setting, work product and outcome are part of the same versioned evaluation claim.",
    "2605.23294": "books/part-05-inference-system/49-tensorrt-llm.md — MoE backend claims must bind router, expert topology, lowering, device and correctness fallback rather than promote a device-only operating point.",
    "2605.23311": "books/part-07-agent/78-tool-calling.md — effect class, committed receipt and semantically recoverable boundary determine whether a failed tool step may resume.",
    "2605.23348": "books/part-05-inference-system/56-inference-scheduling.md — a power/network oracle proposes a placement score; admission, SLO and rollback remain scheduler authorities.",
    "2605.23362": "books/part-06-ai-infrastructure/66-evaluation-system.md — judge budget is allocated against heteroskedastic variance, while rubric/common-mode error cannot be repaired by adding homogeneous raters.",
    "2605.23414": "books/part-07-agent/82-multi-agent.md — epistemic support is coordination evidence, not feasibility truth; executable verification and commit authority remain independent.",
    "2605.23454": "books/part-04-training-system/31-rlhf.md §Reward Proposal、Phase Handoff 与 Exploration 都需要独立 Gate — generated rubrics are versioned reward proposals requiring held-out promotion and rollback.",
    "2605.23493": "books/part-04-training-system/31-rlhf.md §后训练分支的本质差异是 State Distribution — on-policy distillation must bind rollout distribution, evidence mask and teacher/student revisions.",
    "2605.23574": "books/part-07-agent/81-workflow.md — completion is a verifier-owned state transition, not a model-declared intent; distinct valid outputs require durable receipts.",
    "2605.23590": "books/part-07-agent/81-workflow.md — step-level rubric guidance may propose the next action, but workflow state, effect receipt and outcome verifier own commit.",
    "2605.23628": "books/part-06-ai-infrastructure/66-evaluation-system.md — leaderboard aggregation and training objectives are measurement choices, not a natural total order; original per-task evidence stays available.",
    "2605.23640": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md §非 Prefix 复用必须绑定 Position-aligned Segment 与 Correction State — cross-request reuse needs positional identity, privacy policy and exact recompute fallback.",
    "2605.23657": "books/part-07-agent/84-agent-platform.md §被审计的 Skill 必须与实际执行 Artifact 同一 — skill evaluation binds the installed artifact, target profile, runtime and permission envelope.",
    "2605.23701": "books/part-06-ai-infrastructure/66-evaluation-system.md §Judge 先证明看见了目标变化，再谈总体准确率 — evidence intervention tests whether the evaluator responds to causal support before aggregate scoring.",
    "2605.23723": "books/part-07-agent/77-memory.md §用干预矩阵定位写入、检索与阅读失败 — causal interventions separate memory write, retrieval and reading failures.",
    "2605.23764": "books/part-04-training-system/36-distributed-training.md §Expert Placement 与 Sample Packing 可以共享 Rollout Routing State — topology and routing state can coordinate placement and packing while preserving distributed-state correctness.",
    "2605.23856": "books/part-03-multimodal-world-models/25-multimodal-world-models.md §从 RGB Rollout 到 Projective 4D Predictive State — pixel, track, geometry and action predictions share a versioned predictive-state identity and observation rollback.",
    "2605.23899": "books/part-07-agent/84-agent-platform.md §Skill Lifecycle 从人工文件演进为受验证的 Policy — generation, extraction, admission, consumption and retirement form one governed lifecycle.",
    "2605.23904": "books/part-07-agent/84-agent-platform.md §Skill Library 的生命周期必须包含 Drift Retirement — cross-model transfer is a new target-profile evaluation, not proof of universal skill portability.",
    "2605.22842": "books/part-07-agent/77-memory.md — memory provenance and intervention evidence separate poisoned memory state from base-model failure and preserve rollback.",
}
assert len(NOCHANGE_PROPOSITION_OVERRIDES) == 37


evidence_items = []
for arxiv_id in sorted(retained_ids, key=lambda x: [int(v) for v in x.split(".")]):
    item = by_id[arxiv_id]
    if arxiv_id in old_candidates:
        meta = old_candidates[arxiv_id]
        receipt = old_review_receipt(arxiv_id)
        receipt.update(EVIDENCE_LOCATOR_OVERRIDES.get(arxiv_id, {}))
        score = meta["score"]
        adopted_proposition = legacy_marker_body("delta", meta["legacy_family_id"])
        evidence_items.append({
            "source_family_id": family(arxiv_id), "legacy_marker_alias": meta["legacy_family_id"],
            "arxiv_id": arxiv_id, "title": item["title"], "primary_evidence_version": f"arXiv:{arxiv_id}v1",
            "review_route": "deep", "score": {"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
            "review_status": "complete_revalidated", "access_status": "accessible",
            "adopted_proposition": adopted_proposition,
            "evidence_boundary": "Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.",
            "reuse_basis": {"identity_unchanged": True, "exact_version_unchanged": True, "adopted_proposition_unchanged": True, "legacy_snapshot": str(LEGACY.relative_to(ROOT))},
            **receipt,
        })
    else:
        meta = RESTORED[arxiv_id]
        score = meta["score"]
        full_rescreen_heading = HEADING_INDEX.get(arxiv_id)
        primary_url = (
            f"https://arxiv.org/pdf/{arxiv_id}v1"
            if arxiv_id == "2605.23024" or (full_rescreen_heading and full_rescreen_heading["review_route_source"] == "official_pdf_exact_v1")
            else f"https://arxiv.org/html/{arxiv_id}v1"
        )
        evidence_items.append({
            "source_family_id": family(arxiv_id), "arxiv_id": arxiv_id, "title": item["title"],
            "primary_evidence_version": f"arXiv:{arxiv_id}v1", "primary_url": primary_url,
            "review_route": "deep" if sum(score) >= 7 or meta["decision"] in {"Integrate", "Applied"} or arxiv_id in {"2605.22834", "2605.23491", "2605.23857"} else "standard",
            "score": {"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
            "review_status": "blocked_exact_v1_body" if arxiv_id in {"2605.22834", "2605.23491", "2605.23857"} else "complete",
            "access_status": "official_abstract_only; exact-v1 body replay exhausted" if arxiv_id in {"2605.22834", "2605.23491", "2605.23857"} else "accessible_exact_v1",
            "method_locator": meta["locators"][0], "evaluation_locator": meta["locators"][1], "limitations_locator": meta["locators"][2],
            "artifact_locator": "Not Disclosed — no immutable artifact was relied upon for this review",
            "adopted_proposition": meta["claim"], "evidence_boundary": meta["boundary"],
            "restoration_reason": "The legacy closure required a system-interface delta; current contract also admits durable model/training/evaluation mechanisms and negative boundaries.",
        })

evidence_complete_count = sum(item["review_status"].startswith("complete") for item in evidence_items)
evidence_blocked_count = len(evidence_items) - evidence_complete_count
deep_complete_count = sum(item["review_route"] == "deep" and item["review_status"].startswith("complete") for item in evidence_items)
standard_complete_count = sum(item["review_route"] == "standard" and item["review_status"].startswith("complete") for item in evidence_items)
deep_blocked_count = sum(item["review_route"] == "deep" and item["review_status"].startswith("blocked") for item in evidence_items)
score_distribution = Counter(str(item["score"]["total"]) for item in evidence_items)
evidence = {
    "schema": "daily-evidence-review-v3-author-recertification", "report_date": "2026-05-25",
    "candidate_count": RETAINED_COUNT, "evidence_complete_count": evidence_complete_count, "evidence_blocked_count": evidence_blocked_count,
    "deep_complete_count": deep_complete_count, "standard_complete_count": standard_complete_count, "deep_blocked_count": deep_blocked_count,
    "score_distribution": dict(sorted(score_distribution.items())),
    "items": evidence_items,
}


OLD_APPLIED = {arxiv_id for arxiv_id, meta in old_candidates.items() if meta["legacy_books_disposition"] == "Integrate"}
assert len(OLD_APPLIED) == 17

books_items = []
for arxiv_id in sorted(retained_ids, key=lambda x: [int(v) for v in x.split(".")]):
    if arxiv_id in old_candidates:
        meta = old_candidates[arxiv_id]
        if arxiv_id in OLD_APPLIED:
            decision = "Applied"
            target_path = path_for_node(meta["stable_node_id"])
            assert target_path, (arxiv_id, meta["stable_node_id"])
            binding_audit = current_binding_audit(target_path, arxiv_id, meta["legacy_family_id"])
            current = binding_audit["body_binding_excerpt"]
        elif meta["legacy_books_disposition"] == "Structural Candidate":
            decision = "Structural Candidate"
            binding_audit = {}
            current = legacy_marker_body("existing", meta["legacy_family_id"])
        else:
            decision = "No Change — Existing Coverage"
            binding_audit = {}
            current = NOCHANGE_PROPOSITION_OVERRIDES.get(
                arxiv_id, legacy_marker_body("existing", meta["legacy_family_id"])
            )
        node = meta["stable_node_id"]
    else:
        meta = RESTORED[arxiv_id]
        decision = meta["decision"]
        node = meta["node"]
        current = meta.get("existing", meta["boundary"])
        binding_audit = {}
    books_items.append({
        "source_family_id": family(arxiv_id), "arxiv_id": arxiv_id, "stable_node_id": node,
        "target_path": path_for_node(node), "decision": decision, "current_proposition_or_boundary": current,
        **binding_audit,
    })

decision_counts = Counter(item["decision"] for item in books_items)
books = {
    "schema": "daily-books-current-content-comparison-v3-author-recertification", "report_date": "2026-05-25",
    "candidate_count": RETAINED_COUNT,
    "counts": dict(decision_counts),
    "arithmetic": f"{RETAINED_COUNT} = " + " + ".join(f"{count} {decision}" for decision, count in sorted(decision_counts.items())),
    "items": books_items,
}

queue_items = []
for arxiv_id, meta in sorted(RESTORED.items()):
    if meta["decision"] != "Integrate":
        continue
    path = path_for_node(meta["node"])
    node = meta["node"]
    anchor = meta.get("anchor")
    delta = meta.get("delta")
    assert path and node and anchor and delta, (arxiv_id, path, node, anchor, delta)
    meta = RESTORED[arxiv_id]
    queue_items.append({
        "action": "integrate_new_proposition",
        "source_family_id": family(arxiv_id), "arxiv_id": arxiv_id, "owner": node, "target_path": path,
        "unique_anchor": anchor, "proposed_delta": delta,
        "evidence_boundary_tradeoff_failure_fallback": meta["boundary"],
        "exact_v1_locators": meta["locators"], "status": "pending_root_serialized_writeback_and_fresh_postwrite_review",
        "author_must_not_edit_books": True,
    })
queue_items.extend([
    {
        "action": "repair_existing_binding_only",
        "source_family_id": family("2605.22949"), "arxiv_id": "2605.22949", "owner": "INFER-SCHEDULING",
        "target_path": "books/part-05-inference-system/56-inference-scheduling.md",
        "unique_anchor": "the paragraph ending with `arXiv:2605.22949v1` immediately before `### Route Calibration 不应抹平 Model Identity`",
        "proposed_delta": "Move the 2605.22949 marker from the later 2606.19376 paragraph and wrap only the online-calibration proposition with one paired semantic-body-binding start/end marker.",
        "evidence_boundary_tradeoff_failure_fallback": "The existing paragraph already states chosen-answer feedback bias, cold start, delayed feedback and static-policy fallback; this queue item changes binding only, not prose or decision.",
        "exact_v1_locators": ["HTML §2.4 and §3–§3.1", "HTML §5, §5.2 and §5.4", "HTML §11–§12"],
        "status": "pending_root_binding_repair_and_fresh_postwrite_review", "author_must_not_edit_books": True,
    },
    {
        "action": "repair_existing_binding_only",
        "source_family_id": family("2605.23893"), "arxiv_id": "2605.23893", "owner": "MODEL-MOE",
        "target_path": "books/part-02-model/21-moe.md",
        "unique_anchor": "the paragraph ending with `arXiv:2605.23893v1` immediately before `### Activation Ratio 需要把统计量升级为控制量`",
        "proposed_delta": "Move the 2605.23893 marker from the later 2609.08690 paragraph and wrap only the Complete-muE dense-to-MoE hyperparameter-transfer proposition with one paired semantic-body-binding start/end marker.",
        "evidence_boundary_tradeoff_failure_fallback": "The existing paragraph already limits the rule to disclosed dense/MoE configurations and preserves per-configuration tuning as fallback; this queue item changes binding only.",
        "exact_v1_locators": ["HTML §3 Complete-μE MoE Parameterization", "HTML §5 Hyperparameter-Transfer/Scaling Evaluation", "HTML §6 Limitations"],
        "status": "pending_root_binding_repair_and_fresh_postwrite_review", "author_must_not_edit_books": True,
    },
])
queue_items.extend([
    {
        "action": "quarantine_existing_binding_pending_evidence",
        "source_family_id": family("2605.22834"), "arxiv_id": "2605.22834", "owner": "AGENT-RAG",
        "target_path": "books/part-07-agent/76-rag.md",
        "unique_anchor": "the paired semantic-body-binding for SF-2026-ARXIV-2605-22834 before `## Review notes`",
        "proposed_delta": "Remove the positive query-adaptive chunking paragraph and its paired marker from stable body, or replace it with a clearly non-adopted evidence-pending note outside the mechanism chain. Reopen only after exact-v1 body replay.",
        "evidence_boundary_tradeoff_failure_fallback": "Official abstract is insufficient to verify the claimed 100-document/200-query evaluation, overhead, cache-fragmentation failure and fixed-chunk fallback; physical presence is not semantic acceptance.",
        "exact_v1_locators": ["requested: method for query-adaptive semantic chunking", "requested: evaluation protocol/results", "requested: limitations/fallback"],
        "status": "pending_root_quarantine_and_fresh_postwrite_review", "author_must_not_edit_books": True,
    },
    {
        "action": "quarantine_existing_binding_pending_evidence",
        "source_family_id": family("2605.23857"), "arxiv_id": "2605.23857", "owner": "TRAIN-SFT",
        "target_path": "books/part-04-training-system/29-sft.md",
        "unique_anchor": "the paired semantic-body-binding for SF-2026-ARXIV-2605-23857 before `## Review notes`",
        "proposed_delta": "Remove the positive teacher/student compatibility paragraph and its paired marker from stable body, or replace it with a clearly non-adopted evidence-pending note outside the mechanism chain. Reopen only after exact-v1 body replay.",
        "evidence_boundary_tradeoff_failure_fallback": "Official abstract is insufficient to verify distillation method, experiments, ablations, fixed-student boundary or stronger-teacher/mixture/ground-truth fallback; physical presence is not semantic acceptance.",
        "exact_v1_locators": ["requested: distillation method", "requested: model/task experiments and ablations", "requested: limitations/fallback"],
        "status": "pending_root_quarantine_and_fresh_postwrite_review", "author_must_not_edit_books": True,
    },
])
# Keep the root writer's previous 31-item receipt in the same ledger, while
# adding only the five newly discovered semantic deltas as pending work.
combined_queue = {
    (item["arxiv_id"], item["action"]): item
    for item in EXISTING_ROOT_QUEUE_ITEMS
}
for item in queue_items:
    combined_queue.setdefault((item["arxiv_id"], item["action"]), item)
queue_items = list(combined_queue.values())
integration_queue_count = sum(item["action"] == "integrate_new_proposition" for item in queue_items)
pending_integration_count = sum(
    item["action"] == "integrate_new_proposition" and item["status"].startswith("pending_root")
    for item in queue_items
)
root_applied_integration_count = sum(
    item["action"] == "integrate_new_proposition" and item["status"] == "applied_pending_fresh_review"
    for item in queue_items
)
binding_repair_count = sum(item["action"] == "repair_existing_binding_only" for item in queue_items)
binding_quarantine_count = sum(item["action"] == "quarantine_existing_binding_pending_evidence" for item in queue_items)
assert pending_integration_count == decision_counts["Integrate"] == 5
assert root_applied_integration_count == len(ROOT_APPLIED_INTEGRATIONS) == 27
assert binding_repair_count == 2
assert binding_quarantine_count == 2
queue = {
    "schema": "daily-root-books-writeback-queue-v3", "report_date": "2026-05-25",
    "owner": "root_serialized_books_writer", "item_count": len(queue_items),
    "integration_count": integration_queue_count, "pending_integration_count": pending_integration_count,
    "root_applied_integration_count": root_applied_integration_count,
    "binding_repair_count": binding_repair_count,
    "binding_quarantine_count": binding_quarantine_count,
    "status": "new_full_rescreen_queue_pending_root_writeback",
    "items": queue_items,
}

material_items = [
    {
        "request_id": "MR-20260525-2605.22834-EXACT-V1", "source_family_id": family("2605.22834"),
        "known_url": "https://arxiv.org/abs/2605.22834", "missing_material": "replayable official exact-v1 HTML or PDF body",
        "why_needed": "The abstract supports query-adaptive chunking, but the method, evaluation and limitations needed to independently verify the existing Ch76 binding are not replayable.",
        "attempts": ["official exact-v1 HTML returned no body", "official PDF transfer reset", "official abstract remained accessible"],
        "acceptable_substitute": "official arXiv v1 HTML/PDF or author-hosted byte-identical v1 manuscript with version identity",
        "current_disposition": "Deferred; physical root binding is queued for quarantine and no positive claim may be derived",
        "reopen_locator": "query-adaptive construction method, 100-document/200-query evaluation, limitations and fallback boundary",
    },
    {
        "request_id": "MR-20260525-2605.23491-EXACT-V1", "source_family_id": family("2605.23491"),
        "known_url": "https://arxiv.org/abs/2605.23491", "missing_material": "official exact-v1 HTML or PDF body",
        "why_needed": "The abstract exposes the candidate mechanism but cannot verify the execution-matrix algorithm, four-benchmark protocol, ablations, test/code common-mode failure or limitations.",
        "attempts": ["official HTML timed out", "official PDF fetch reset", "official abstract remained accessible"],
        "acceptable_substitute": "official arXiv v1 HTML/PDF or author-hosted byte-identical v1 manuscript with version identity",
        "current_disposition": "Deferred; no positive evidence or Books use",
        "reopen_locator": "Method, evaluation setup/results, ablations/failure analysis and limitations for CoSPlay v1 only",
    },
    {
        "request_id": "MR-20260525-2605.23857-EXACT-V1", "source_family_id": family("2605.23857"),
        "known_url": "https://arxiv.org/abs/2605.23857", "missing_material": "replayable official exact-v1 HTML or PDF body",
        "why_needed": "The abstract supports teacher/student compatibility, but the distillation method, experiments, ablations and fixed-student boundary needed to independently verify the existing Ch29 binding are not replayable.",
        "attempts": ["official exact-v1 HTML exposed no body", "official PDF transfer reset", "official abstract remained accessible"],
        "acceptable_substitute": "official arXiv v1 HTML/PDF or author-hosted byte-identical v1 manuscript with version identity",
        "current_disposition": "Deferred; physical root binding is queued for quarantine and no positive claim may be derived",
        "reopen_locator": "distillation method, model/task evaluation, ablations and stronger-teacher/mixture/ground-truth fallback",
    },
]
materials = {
    "schema": "daily-materials-request-v3", "report_date": "2026-05-25", "open_count": len(material_items),
    "items": material_items,
}

audit = {
    "schema": "daily-author-adversarial-audit-v3", "report_date": "2026-05-25", "author": "delegated V3 repair author",
    "legacy_claim_challenged": "V2.1 Complete and DataCite-created-day denominator are not accepted.",
    "false_negative_challenge": {"affected_closure_count": 374, "scope": "every arXiv identity that remained pre-denominator closure after the prior repair; title plus full abstract reviewed item by item, then every restored item received exact-v1 review", "restored_count": len(FULL_RESCREEN_RESTORE_IDS), "restored_ids": sorted(FULL_RESCREEN_RESTORE_IDS), "total_restored_from_legacy_closures": len(RESTORED), "remaining_closure_count_arxiv": 497 - RETAINED_COUNT},
    "false_positive_challenge": {"retained_count": RETAINED_COUNT, "result": f"All {RETAINED_COUNT} candidates now project to current Evidence and Books ownership; the full-rescreen additions are 157 exact-v1 reviews with 0 access blockers."},
    "withdrawal_check": {"withdrawn_count": 0, "boundary": "No official withdrawn/deleted disposition was encountered in the owner identities or retained exact-version pages; this is not a claim that absence of a page marker proves non-withdrawal."},
    "books_challenge": {"prior_root_integrations_preserved": root_applied_integration_count, "binding_repairs_preserved": binding_repair_count, "binding_quarantines_preserved": binding_quarantine_count, "new_integrate_queue": pending_integration_count, "counts": dict(decision_counts), "no_change_proposition_repairs": len(NOCHANGE_PROPOSITION_OVERRIDES)},
    "gate": {"coverage": "Ongoing: 97 owner-day memberships remain isolated plus the pre-existing Meta/Xiaomi source limitations", "evidence": "277 complete; three pre-existing exact-v1 body blockers remain isolated; full-rescreen Access Blocked=0", "books": f"pending root writeback for {pending_integration_count} new integrations; prior 31-item root receipt preserved", "fresh_semantic": "pending different non-author reviewer after root writeback", "status": "Ongoing"},
}

repair_receipt = {
    "schema": "daily-v3-author-repair-receipt", "report_date": "2026-05-25", "checked_at": CHECKED_AT,
    "status": "Ongoing", "role": "repair author; not authorized to self-sign Complete",
    "repair_scope": {"arxiv_closures_reopened": 374, "reviewed": 374, "restored": len(FULL_RESCREEN_RESTORE_IDS), "kept_closed": 374 - len(FULL_RESCREEN_RESTORE_IDS), "confirmed_false_negatives_recovered": len(CONFIRMED_FALSE_NEGATIVES)},
    "arithmetic": screening["conservation"], "evidence": {key: evidence[key] for key in ("candidate_count", "evidence_complete_count", "evidence_blocked_count", "deep_complete_count", "standard_complete_count", "deep_blocked_count", "score_distribution")},
    "books": {"counts": dict(decision_counts), "new_root_integrations": pending_integration_count, "prior_root_integrations_preserved": root_applied_integration_count, "binding_repairs": binding_repair_count, "binding_quarantines": binding_quarantine_count},
    "open_gates": ["97 arXiv owner-day memberships remain explicitly isolated", "three pre-existing exact-v1 bodies remain requested", f"root Books queue for {pending_integration_count} new deltas", "different fresh non-author final review"],
    "supersedes_for_current_state": "fresh-nonauthor-final-review-v3.json remains the historical FAIL receipt that triggered this repair; it is not a current PASS receipt.",
}

for name, value in [
    ("official-owner-batch-evidence-v3.json", owner_evidence),
    ("source-coverage-v3.json", source_coverage),
    ("screening-outcomes-v3.json", screening),
    ("evidence-review-v3.json", evidence),
    ("books-comparison-v3.json", books),
    ("root-books-writeback-queue-v3.json", queue),
    ("materials-request-v3.json", materials),
    ("author-adversarial-audit-v3.json", audit),
    ("author-repair-receipt-v3.json", repair_receipt),
]:
    write_json(name, value)


candidate_lines = []
for ev in evidence_items:
    arxiv_id = ev["arxiv_id"]
    score = ev["score"]
    book = next(item for item in books_items if item["arxiv_id"] == arxiv_id)
    if arxiv_id in RESTORED:
        contribution = "FN challenge 恢复；" + RESTORED[arxiv_id]["claim"]
    else:
        contribution = "V3 复核沿用 identity/version/命题不变的 exact-v1 证据"
    review = "受阻" if ev["review_status"].startswith("blocked") else ("深入完成" if ev["review_route"] == "deep" else "标准完成")
    decision_map = {"Applied": "整合：当前正文 binding 已存在", "Integrate": "整合：待 root 串行写回", "No Change — Existing Coverage": "已有覆盖", "Structural Candidate": "结构候选", "Report Only": "仅报告", "Deferred": "暂缓"}
    target = book["target_path"]
    if target:
        rel = "../../../../" + target
        decision = f"{decision_map[book['decision']]}：{book['stable_node_id']} [章节]({rel})"
    else:
        decision = decision_map[book["decision"]]
    public_event = "2026-05-25T08:00:00+08:00"
    if by_id[arxiv_id].get("owner_receipt_route") != "official_arxiv_oai_direct":
        contribution = "DataCite identity timestamp only；owner-day 边界未证实；" + contribution
    candidate_lines.append(
        f"| [{arxiv_id} {ev['title']}](https://arxiv.org/abs/{arxiv_id}) | {public_event} | {contribution}；{score['design_delta']}+{score['system_reach']}+{score['durability']}={score['total']} | {review} | {decision} |"
    )

source_lines = [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in sources]

review_lines = []
for ev in evidence_items:
    arxiv_id = ev["arxiv_id"]
    sf = ev["source_family_id"]
    if arxiv_id in old_candidates:
        review_lines.extend([
            f"### [{arxiv_id} {ev['title']}](https://arxiv.org/abs/{arxiv_id})",
            "",
            f"<!-- review:{sf}:start -->",
            f"exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `{ev.get('legacy_marker_alias')}` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。",
            f"<!-- claim:{sf}:start -->{ev['adopted_proposition']}<!-- claim:{sf}:end -->",
            f"证据边界：{ev['evidence_boundary']}",
            f"<!-- review:{sf}:end -->", "",
        ])
    else:
        meta = RESTORED[arxiv_id]
        review_lines.extend([
            f"### [{arxiv_id} {ev['title']}](https://arxiv.org/abs/{arxiv_id})", "",
            f"<!-- review:{sf}:start -->",
            f"证据位置：{'; '.join(meta['locators'])}。",
            f"<!-- claim:{sf}:start -->{meta['claim']}<!-- claim:{sf}:end -->",
            f"证据边界、trade-off、failure 与 fallback：{meta['boundary']}",
            f"Books：{meta['decision']}；owner={meta['node'] or '尚无唯一 owner'}。",
            f"<!-- review:{sf}:end -->", "",
        ])

readme = f"""# Daily Research — 2026-05-25

**规范：** V3

**窗口：** 2026-05-24T09:00:00+08:00 ～ 2026-05-25T09:00:00+08:00

**状态：** 进行中

**Books：** 纳入本次

**检查时间：** {CHECKED_AT}

## 1. 结论

旧 V2.1 `Complete` 与 DataCite `created-day=497` 不再拥有当前状态。当前语义 inventory 为 **{screening['conservation']}**：其中 400 条 arXiv identity 具有官方 OAI direct membership，OpenAI 官方 RSS 的 2 条事件也具有日级时间；另有 97 条只能用 DataCite 恢复 identity/version，不能冒充官方 announcement membership，故单独隔离为 owner-day boundary。全类别连续 ID 区间仅用于边界核对，不把连续性当作逐项公开日证明。

作者按 current V3 重新打开前轮仍为 closure 的 **374/374** 个 arXiv identity，逐项阅读 title+完整 abstract；fresh non-author 反例检查又恢复 2605.22855，因此当前 **158** 项恢复、**216** 项保持 closure。158 个恢复项完成 official exact-v1 Evidence：154 个走 HTML，4 个改走官方 PDF，**新增 Access Blocked=0**。连同前轮 67 项，legacy closure 中累计恢复 225 项；旧 56 项仅在 identity、exact-v1 与 adopted proposition 未变时复用。当前 Evidence 为 **{RETAINED_COUNT} = {deep_complete_count} deep complete + {standard_complete_count} standard complete + {deep_blocked_count} deep blocked**，score distribution 为 `{dict(sorted(score_distribution.items()))}`。2605.22834、2605.23857 的 root binding 已存在但 exact-v1 body 无法独立回放；2605.23491 仍为 Deferred。三项是前轮遗留材料隔离，不用于扩张正面证据。

Books 对账为 **{books['arithmetic']}**。作者未编辑共享 Books；root queue 保留既有 {root_applied_integration_count} 个已写回 Integrate、{binding_repair_count} 个 binding-only 修复与 {binding_quarantine_count} 个 quarantine receipt，并新增 **{pending_integration_count}** 个待 root 串行写回的真实 delta。所有本轮 No Change 都绑定具体 Stable Knowledge Node 与当前 proposition，而不是用泛化 locator 冒充 comparison。Coverage 仍保留 97 条 owner-day、Meta 入口和 Xiaomi undated cards 三类不支持正面 no-hit 的边界。状态保持 Ongoing，等待 5 项 root 写回与另一位 fresh non-author 终审。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
{chr(10).join(source_lines)}

完整 owner 证据见 [`official-owner-batch-evidence-v3.json`](../_sources/daily-20260525/official-owner-batch-evidence-v3.json)，14-source 结构化记录见 [`source-coverage-v3.json`](../_sources/daily-20260525/source-coverage-v3.json)，499 条逐项题摘与非模板理由见 [`screening-outcomes-v3.json`](../_sources/daily-20260525/screening-outcomes-v3.json)。`已检查` 仅指注册入口的有界核验；受阻/无日级时间的入口不支持“无遗漏”。普通 GitHub commit/PR 未扩入 Daily denominator。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
{chr(10).join(candidate_lines)}

## 4. 证据与知识整合

{RETAINED_COUNT} 项逐项版本、评分、method/evaluation/non-proof locator、采用命题与证据边界见 [`evidence-review-v3.json`](../_sources/daily-20260525/evidence-review-v3.json)。旧 56 项的可读原始 Source Review 冻结在 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md)，复用不携带旧日期 owner、分母、Books 状态或 Complete 结论；2605.22850 的 placeholder locator 已用官方 exact-v1 HTML §3–§6.3 修复。当前 Books 对读见 [`books-comparison-v3.json`](../_sources/daily-20260525/books-comparison-v3.json)。

{chr(10).join(review_lines)}
## 5. 缺口与下一步

1. root 按 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260525/root-books-writeback-queue-v3.json) 串行处理 {pending_integration_count} 个新 Integrate。既有 {root_applied_integration_count} 个 root 写回、2605.22949/2605.23893 的 binding-only 修复和 2605.22834/2605.23857 的 quarantine receipt 只作为历史已执行状态保留，不得回退为待办。作者不编辑共享 Books。
2. [`materials-request-v3.json`](../_sources/daily-20260525/materials-request-v3.json) 精确请求 2605.22834、2605.23491、2605.23857 的 official exact-v1 body。材料到达前 22834/23857 物理写回不等于语义终审通过，23491 保持 Deferred。
3. 97 条 DataCite-recovered identities 缺官方 announcement membership；Meta Publications 入口受阻、Xiaomi Blog cards 无日级时间。三类均不支持正面 no-hit 或 Complete，恢复证据后只重开对应 slice。
4. 当前 fresh non-author 终审恢复了 2605.22855，必须由另一位 fresh reviewer 只复核该有界恢复、281 项算术投影、97 条 owner-day 隔离呈现与五个新 binding 的当前物理位置；不重跑 499 条。

## 6. 复核

复核者：待分配的 fresh non-author（不能是本轮作者）
结论：作者返修已落盘但未通过最终 Gate。当前语义 inventory、374/374 full closure rescreen、{evidence_complete_count} 项 complete evidence、{evidence_blocked_count} 项前轮精确材料隔离、Books comparison 与 {len(queue_items)} 项 root ledger 已冻结；其中真正新增待 root 写回为 {pending_integration_count} 项，owner-day 仍有 97 项隔离。机器 validator、JSON、marker 与 scoped diff-check 的执行结果记录在作者 checkpoint，不替代独立语义复核。
"""

REPORT.write_text(readme, encoding="utf-8")

checkpoint = f"""# 2026-05-25 V3 author repair checkpoint

- checked_at: {CHECKED_AT}
- status: Ongoing; repair-author Gate frozen, pending root serialized Books writeback and a different fresh non-author review.
- owner: 400 arXiv OAI-direct + 2 OpenAI RSS events are day-owned; 97 DataCite-recovered arXiv identities remain owner-day isolated. DataCite is identity/revision evidence only.
- denominator projection: `{screening['conservation']}`; this is a semantic inventory, not a positive public-day proof for the 97 isolated identities.
- full closure rescreen: reopened `374/374` arXiv closures; restored `158`, kept closed `216`. Cumulative restored legacy closures=225.
- Evidence: `{RETAINED_COUNT} = {deep_complete_count} deep complete + {standard_complete_count} standard complete + {deep_blocked_count} deep blocked`; this full-rescreen batch used 153 official HTML + 4 official PDF routes with Access Blocked=0. The three blocked bodies (2605.22834, 2605.23491, 2605.23857) are pre-existing isolated candidates.
- Books: `{books['arithmetic']}`; shared Books not edited by author. Root ledger preserves {root_applied_integration_count} applied integrations + {binding_repair_count} binding repairs + {binding_quarantine_count} quarantines and adds {pending_integration_count} pending integrations.
- No Change repair: every full-rescreen No Change item carries an explicit Stable Knowledge Node and current proposition; closure reasons quote each paper's actual contribution sentence and do not use a keyword classifier.
- remaining Gate: root writeback for {pending_integration_count} new deltas; continued isolation for 97 owner-day identities and three pre-existing material requests; fresh non-author final semantic review.
- reusable owner-batch method and local receipt: `official-owner-batch-evidence-v3.json` → `papers/2026/05/_sources/arxiv-owner-replay-20260903/20260525/arxiv-owner-receipt.json`.
"""
(LOCAL / "AUTHOR_V3_REPAIR_CHECKPOINT_20260916.md").write_text(checkpoint, encoding="utf-8")

print(json.dumps({"raw": RAW_COUNT, "retained": RETAINED_COUNT, "closure": CLOSURE_COUNT, "withdrawn": 0, "evidence_complete": evidence_complete_count, "evidence_blocked": evidence_blocked_count, "root_integrate_pending": pending_integration_count, "root_integrate_applied_preserved": root_applied_integration_count, "root_binding_repair": binding_repair_count, "root_binding_quarantine": binding_quarantine_count}, ensure_ascii=False))
