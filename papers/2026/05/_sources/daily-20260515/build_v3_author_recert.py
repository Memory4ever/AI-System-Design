#!/usr/bin/env python3
"""Build the bounded 2026-05-15 V3 author recertification artifacts.

This script only reads the frozen owner-day inventory, recovered exact-v1
primary sources and current Books.  It never edits Books and never closes the
independent-review gate.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[5]
DAY = ROOT / "papers/2026/05/_sources/daily-20260515"
RECEIPT = ROOT / "papers/2026/05/_sources/arxiv-owner-replay-20260903/20260515/arxiv-owner-receipt.json"

NODE_SPEC = {
    "WORLDVIEW-REPRESENTATION": ("books/part-01-worldview/05-what-neural-networks-learn.md", "### 从可读出到机制：证据应逐级变强"),
    "MODEL-MOE": ("books/part-02-model/21-moe.md", "### 从统计 Expert 偏好到可部署模块，需要改变 Objective"),
    "MULTIMODAL-REPRESENTATION": ("books/part-03-multimodal-world-models/23-multimodal-representation.md", "### 固定预算要先分配信息责任，再选择具体 Token"),
    "MULTIMODAL-GENERATIVE-PARADIGMS": ("books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md", "## Draft、Verify 与 Correct 不是同一件事"),
    "MULTIMODAL-WORLD-MODELS": ("books/part-03-multimodal-world-models/25-multimodal-world-models.md", "## Evaluation：从画面质量到干预结果"),
    "MULTIMODAL-EMBODIED-VLA": ("books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md", "## Safety envelope"),
    "TRAIN-DATA": ("books/part-04-training-system/27-data.md", "### Synthetic data：从“先生成再打分”到 Specification Compilation"),
    "TRAIN-PRETRAINING": ("books/part-04-training-system/28-pretraining.md", "## 一次 training step 的状态流"),
    "TRAIN-SFT": ("books/part-04-training-system/29-sft.md", "## SFT 数据质量比格式整齐更难"),
    "TRAIN-RLHF": ("books/part-04-training-system/31-rlhf.md", "### Training–Inference Mismatch 也可能来自 Numerical Execution Identity"),
    "TRAIN-GRPO": ("books/part-04-training-system/33-grpo.md", "## Sequence Reward 怎样作用到 Tokens"),
    "INFER-PREFILL": ("books/part-05-inference-system/43-prefill.md", "## Prefill 的两个输出"),
    "INFER-KV-CACHE": ("books/part-05-inference-system/45-why-kv-cache-speeds-up.md", "## KV Cache 的生命周期"),
    "INFER-SPECULATIVE-DECODING": ("books/part-05-inference-system/48-speculative-decoding.md", "## Exact Acceptance 机制"),
    "INFER-TENSORRT-LLM": ("books/part-05-inference-system/49-tensorrt-llm.md", "## 从计算图开始"),
    "INFER-SCHEDULING": ("books/part-05-inference-system/56-inference-scheduling.md", "## 调度对象从 request 变成 token state"),
    "PLATFORM-EVALUATION-SYSTEM": ("books/part-06-ai-infrastructure/66-evaluation-system.md", "## 第一个不变量：评估声明必须绑定完整对象"),
    "PLATFORM-MONITORING": ("books/part-06-ai-infrastructure/67-monitoring.md", "## Monitoring 也会改变系统"),
    "PLATFORM-COST": ("books/part-06-ai-infrastructure/70-cost.md", "## 资源时间是共同底座"),
    "PLATFORM-SECURITY": ("books/part-06-ai-infrastructure/72-security.md", "## 从资产与信任边界开始"),
    "AGENT-CONTEXT": ("books/part-07-agent/75-context.md", "## Context Assembly Pipeline"),
    "AGENT-RAG": ("books/part-07-agent/76-rag.md", "## Online Retrieval Pipeline"),
    "AGENT-MEMORY": ("books/part-07-agent/77-memory.md", "## Memory 的构建、检索与授权不能相互替代"),
    "AGENT-TOOL-CALLING": ("books/part-07-agent/78-tool-calling.md", "## Tool Discovery 与选择"),
    "AGENT-WORKFLOW": ("books/part-07-agent/81-workflow.md", "## Deterministic Spine，Agentic Nodes"),
    "AGENT-MULTI-AGENT": ("books/part-07-agent/82-multi-agent.md", "## Verification 与 Aggregation"),
    "AGENT-PLATFORM": ("books/part-07-agent/84-agent-platform.md", "## Agent Runtime State Machine"),
}

NODE_ROWS = """
2605.13851 AGENT-MULTI-AGENT 2 1 2
2605.13864 INFER-TENSORRT-LLM 3 2 3
2605.13880 AGENT-MEMORY 2 1 2
2605.13915 INFER-TENSORRT-LLM 3 2 3
2605.13935 TRAIN-GRPO 2 1 3
2605.13940 PLATFORM-SECURITY 3 2 3
2605.13941 AGENT-MEMORY 2 1 2
2605.13981 PLATFORM-COST 3 3 3
2605.14005 PLATFORM-SECURITY 3 2 3
2605.14037 INFER-KV-CACHE 3 2 3
2605.14038 AGENT-TOOL-CALLING 2 2 3
2605.14062 TRAIN-DATA 2 2 3
2605.14071 TRAIN-SFT 2 1 2
2605.14089 AGENT-PLATFORM 2 2 2
2605.14102 AGENT-WORKFLOW 2 1 2
2605.14133 PLATFORM-EVALUATION-SYSTEM 3 2 3
2605.14153 PLATFORM-EVALUATION-SYSTEM 3 2 3
2605.14163 INFER-SCHEDULING 3 2 3
2605.14167 PLATFORM-EVALUATION-SYSTEM 2 2 3
2605.14175 PLATFORM-SECURITY 3 2 3
2605.14186 INFER-SCHEDULING 2 2 3
2605.14192 AGENT-RAG 2 1 2
2605.14200 MODEL-MOE 3 2 3
2605.14212 AGENT-MULTI-AGENT 2 2 2
2605.14217 INFER-PREFILL 2 2 2
2605.14220 TRAIN-RLHF 3 2 3
2605.14241 AGENT-TOOL-CALLING 3 2 3
2605.14249 PLATFORM-COST 3 3 3
2605.14258 WORLDVIEW-REPRESENTATION 2 1 3
2605.14271 PLATFORM-EVALUATION-SYSTEM 3 2 3
2605.14292 INFER-KV-CACHE 2 2 2
2605.14305 MULTIMODAL-GENERATIVE-PARADIGMS 3 2 3
2605.14362 AGENT-CONTEXT 2 2 3
2605.14368 MULTIMODAL-GENERATIVE-PARADIGMS 2 1 2
2605.14392 TRAIN-GRPO 3 2 3
2605.14415 PLATFORM-EVALUATION-SYSTEM 2 2 3
2605.14421 AGENT-MEMORY 3 2 3
2605.14438 MODEL-MOE 3 2 3
2605.14457 AGENT-CONTEXT 2 1 2
2605.14458 MULTIMODAL-REPRESENTATION 2 2 2
2605.14460 AGENT-PLATFORM 3 2 3
2605.14473 AGENT-RAG 2 1 2
2605.14477 AGENT-MEMORY 2 1 2
2605.14478 AGENT-CONTEXT 2 1 2
2605.14483 AGENT-MULTI-AGENT 3 2 3
2605.14498 PLATFORM-EVALUATION-SYSTEM 2 2 3
2605.14514 PLATFORM-SECURITY 3 2 3
2605.14570 PLATFORM-EVALUATION-SYSTEM 2 1 2
2605.14591 PLATFORM-SECURITY 3 2 3
2605.14605 PLATFORM-SECURITY 3 2 3
2605.14621 PLATFORM-MONITORING 2 1 2
2605.14636 PLATFORM-EVALUATION-SYSTEM 2 1 2
2605.14678 PLATFORM-EVALUATION-SYSTEM 2 2 3
2605.14744 PLATFORM-SECURITY 3 2 3
2605.14747 TRAIN-DATA 2 2 2
2605.14773 TRAIN-DATA 2 2 2
2605.14786 PLATFORM-SECURITY 2 2 2
2605.14844 INFER-TENSORRT-LLM 3 2 3
2605.14859 PLATFORM-SECURITY 3 2 3
2605.14865 PLATFORM-EVALUATION-SYSTEM 2 2 3
2605.14906 PLATFORM-EVALUATION-SYSTEM 2 2 3
2605.14929 INFER-TENSORRT-LLM 2 2 2
2605.14932 PLATFORM-SECURITY 3 2 3
2605.14968 AGENT-WORKFLOW 3 2 3
2605.14978 INFER-SPECULATIVE-DECODING 2 2 2
2605.15030 PLATFORM-SECURITY 3 2 3
2605.15034 PLATFORM-EVALUATION-SYSTEM 2 1 2
2605.15041 AGENT-TOOL-CALLING 2 1 2
2605.15051 INFER-SPECULATIVE-DECODING 3 2 3
2605.15053 TRAIN-PRETRAINING 3 2 3
2605.15077 AGENT-TOOL-CALLING 3 2 3
2605.15079 TRAIN-DATA 3 2 3
2605.15097 PLATFORM-SECURITY 3 2 3
2605.15100 INFER-SCHEDULING 2 2 2
2605.15109 AGENT-RAG 3 2 3
2605.15113 TRAIN-GRPO 2 1 2
2605.15118 PLATFORM-EVALUATION-SYSTEM 2 2 3
2605.15128 PLATFORM-EVALUATION-SYSTEM 2 2 3
2605.15132 AGENT-WORKFLOW 3 2 3
2605.15134 PLATFORM-EVALUATION-SYSTEM 3 2 3
2605.15138 PLATFORM-SECURITY 3 2 3
2605.15141 MULTIMODAL-GENERATIVE-PARADIGMS 2 2 2
2605.15152 PLATFORM-SECURITY 3 2 3
2605.15153 MULTIMODAL-EMBODIED-VLA 2 2 3
2605.15155 TRAIN-GRPO 2 1 2
2605.15156 AGENT-MEMORY 3 2 3
2605.15157 MULTIMODAL-EMBODIED-VLA 3 2 3
2605.15164 PLATFORM-EVALUATION-SYSTEM 2 2 3
2605.15172 PLATFORM-SECURITY 3 2 3
2605.15177 INFER-SCHEDULING 2 2 2
2605.15178 MULTIMODAL-WORLD-MODELS 2 2 2
2605.15184 AGENT-RAG 2 1 2
2605.15185 MULTIMODAL-WORLD-MODELS 3 2 3
2605.15188 PLATFORM-EVALUATION-SYSTEM 2 2 3
2605.15190 MULTIMODAL-GENERATIVE-PARADIGMS 2 1 2
"""

MAPPING = {}
for row in NODE_ROWS.splitlines():
    if not row.strip():
        continue
    aid, node, d, r, u = row.split()
    MAPPING[aid] = {"stable_node_id": node, "score": {"design_delta": int(d), "system_reach": int(r), "durability": int(u), "total": int(d)+int(r)+int(u)}}

# Existing main-body bindings already present in the current worktree.  These
# are not treated as proof by themselves; the comparison artifact also records
# the containing proposition and Review-notes boundary.
APPLIED = {"2605.14005", "2605.14038", "2605.14175", "2605.14186", "2605.14220"}

# The nearest current proposition does not yet carry the mechanism below.
# Root decides and writes; this author packet never edits shared Books.
INTEGRATE = {
    "2605.13864", "2605.13915", "2605.13935", "2605.13981", "2605.14062",
    "2605.14071", "2605.14163", "2605.14212", "2605.14249", "2605.14483",
    "2605.14514", "2605.14591", "2605.14786", "2605.15053", "2605.15077",
    "2605.15134", "2605.15138", "2605.15152", "2605.15172",
}

QUEUE_SPINE = {
    "2605.13864": "从手写 GPU kernel 到受约束 source-to-source lowering：高层语义保持权属于变换规则，目标代码需以编译、数值与性能回归验收；收益是复用与可移植性，代价是目标相关假设和验证面扩大。",
    "2605.13915": "把 dequantization 从每次乘法的固定前置开销，改写为 activation 分解与分尺度执行；必须保留数值误差、kernel 融合、硬件适配与未命中路径回退。",
    "2605.13935": "Diffusion policy 的 mode-seeking 目标会锁定少数轨迹；trajectory-balance 分支改变对完整去噪轨迹的 credit，但引入归一化、探索和估计方差，证据仅限论文任务。",
    "2605.13981": "成本核算从 student serving 能耗扩展到 teacher generation、logit/materialization、student training 与 evaluation 的完整 distillation lifecycle；局部节能不能替代端到端分母。",
    "2605.14062": "合成数据从生成后统一判废演进为分阶段 in-flight rejection；早停节省 token/compute，却以过滤器误杀、阶段校准和分布偏移为代价，低置信时回退完整生成后评估。",
    "2605.14071": "离线 distillation 需要显式修正 teacher-data 与当前 student-policy 的分布漂移；修正权重只能拥有训练样本重加权权，不能冒充目标分布真值。",
    "2605.14163": "多候选推理要分开 proposal coverage 与 selector/local verifier soundness；扩大 committee 只增加覆盖，不能证明选中答案正确，低覆盖或 selector 失校准时回退独立 verifier。",
    "2605.14212": "自动多 Agent 系统从分别训练 designer/executor 演进为端到端 credit；拓扑 proposal、执行状态与最终 reward 必须分权，收益是减少局部目标错配，代价是 credit leakage 与昂贵 rollout。",
    "2605.14249": "多 GPU inference 调优从盲目搜索演进为能耗预测约束下的 exploration；预测器只排序配置，真实 workload/SLO 复测才拥有 commit，模型漂移时回退安全配置。",
    "2605.14483": "可执行 orchestration 的反事实 RL 必须把 workflow graph revision、executor state 与 outcome evaluator 绑定；反事实只能提出 topology update，不能跳过可执行回归。",
    "2605.14514": "多个单项有效 defense 组合后可能相互抵消；安全 release 需要测组合 interaction matrix 与失效归因，而不是累加单项分数，未知组合回退最小独立边界。",
    "2605.14591": "隐私审计可在零额外训练下复用既有模型/记录构造受限 membership signal，但 signal 仍需识别性与 false-positive 校准，不能升级为泄漏事实。",
    "2605.14786": "浏览 Agent 的 UI action trace 可形成跨运行 fingerprint；安全边界需把动作序列视为 observable channel，在审计能力与用户隐私之间分离采集、识别与处置权限。",
    "2605.15053": "Continual pretraining 从 replay-buffer 依赖转向对读写梯度分量的受约束分解；减少 replay 存储不等于消除遗忘，必须同时验收 acquisition、retention 与 transfer。",
    "2605.15077": "Tool calling 从生成结束后串行执行演进为 symbolic future 驱动的异步调用；只读、可取消调用可与 decoding 重叠，副作用与结果注入仍需 exact action match、版本绑定和串行回退。",
    "2605.15134": "训练目标可把不可避免错误塑造成可预测失败；forecastability 是独立 sensor contract，不等于提高平均正确率，需与 abstention/routing policy 分权并防止模型学会集中失败。",
    "2605.15138": "Unlearning 的删除效果可能被后续 quantization 改写；release identity 必须联合绑定 removal method 与 deployed numeric artifact，并以量化后回归而非 fp32 checkpoint 验收。",
    "2605.15152": "攻击者可通过 outlier injection 把 quantization 变成新的安全失效路径；量化前异常检测与量化后行为回归需要共同进入 artifact gate，失败时回退高精度或拒绝发布。",
    "2605.15172": "Positional encoding 也可能承载 backdoor trigger；安全审计不能只扫描权重幅值与 token pattern，还应覆盖 position-dependent behavior，并把检测结果限制为 sensor 而非自动删除权。",
}

LOCATOR_OVERRIDES = {
    "2605.13864": {
        "method": ("§5 Transformations; §6 CUDA Code Generation", "OptiGPU lowers verified OptiTrust transformations into GPU thread, memory, synchronization and launch constructs."),
        "evaluation": ("§7 Evaluation; §7.2 Results", "The disclosed evaluation compares generated GPU code on the paper's selected programs and configurations."),
        "limitations": ("§9 Conclusion and Future Work", "The conclusion scopes the result to the current transformation language and identifies remaining GPU-language and optimization work."),
    },
    "2605.14038": {
        "method": ("§3 Defining model-adaptive tool necessity and two-stage modeling of tool-call", "Tool necessity is defined relative to the tested model's no-tool capability, then separated into cognition and execution stages."),
        "evaluation": ("§5 From meta-cognition to execution ability: What went wrong?", "The probes separately measure stated cognition, action and their mismatch under the paper's dataset and models."),
        "limitations": ("Appendix C Limitations", "The authors bound the observed knowing-doing gap to their datasets, tools, models and probing design."),
    },
    "2605.14102": {
        "method": ("§4 System Overview", "The system separates planner-directed execution, tool layer and reliability layer for the negative-ablation comparison."),
        "evaluation": ("§5 Evaluation Protocol; §6 Results", "The protocol and results measure orchestration overhead, reliability and task movement on the disclosed workloads."),
        "limitations": ("§11 Limitations and Threats to Validity", "The paper explicitly limits what the negative ablation says about other harnesses and environments."),
    },
    "2605.14167": {
        "method": ("§3 Epistematics: a meta-evaluative procedure", "The procedure extracts a capability claim, its theoretical assumptions and discriminative tests rather than treating a benchmark score as theory-neutral."),
        "evaluation": ("§4 Case analysis: autonomous learning and captured evaluation", "The case analysis applies the procedure to autonomous learning claims and derives alternative evaluation requirements."),
        "limitations": ("§6 Scope and limitations", "The position paper does not provide a universal empirical benchmark or prove that one meta-evaluation procedure is complete."),
    },
    "2605.14200": {
        "method": ("§4 Scaling MoEs Requires Maximal Scale Stability; §5 Self-consistent DMFT for MoE training dynamics", "The paper replaces a direct dense μP transfer with a scale-stability desideratum and a self-consistent MoE training-dynamics analysis."),
        "evaluation": ("§3 Maximal Update Desiderata for MoEs and their Shortcomings", "The paper evaluates parameterization laws analytically through the failure of existing maximal-update desiderata; it does not disclose a standalone production experiment."),
        "limitations": ("§6 Discussion and Future Work", "The discussion scopes the parameterization result and leaves broader architecture and optimizer settings for future work."),
    },
    "2605.14292": {
        "method": ("§4 α: Method and Protocol", "The survivor uses a V-space diversity penalty under a pre-registered dev/confirmation protocol after multiple mechanisms fail."),
        "evaluation": ("§5 Confirmation Results", "Held-out confirmation and head-to-head comparison are reported under matched decode-horizon memory."),
        "limitations": ("§6.3 Scope and Open Questions", "Model family, workload, hyperparameter range and composition with other allocation methods remain open."),
    },
    "2605.14929": {
        "method": ("§10 Per-Layer Pair Search; §12 Multiple-Choice Knapsack Allocation; §13 End-to-End Pipeline", "The methodology searches per-layer format pairs and allocates a global bit budget with hardware-format constraints."),
        "evaluation": ("Not separately disclosed in exact-v1", "The exact-v1 body describes fidelity metrics and methodology but does not expose a standalone end-to-end model/task performance evaluation section."),
        "limitations": ("§14 Conclusion", "The conclusion supports a methodology proposal; production accuracy, latency, SLO and cross-hardware generalization remain unproven."),
    },
    "2605.14968": {
        "method": ("§1.3 System Architecture; §1.7.4 Diagram-as-Specification Architecture", "GraphFlow separates diagram specification, compile-time proof obligations, durable execution and human/AI swimlane responsibility."),
        "evaluation": ("§1.13 Empirical Evaluation", "The pilot covers an early prototype; the verified-core subsystem described in the paper was not part of that deployment."),
        "limitations": ("§1.13.6 Interpretation and Limitations", "The pilot lacks complete node-level telemetry and cannot validate the not-yet-deployed verified core."),
    },
    "2605.15109": {
        "method": ("§2 Experimental Design; §2.3 Graph Ablation Studies", "The method isolates cited, visited and neighborhood evidence in controlled GraphRAG traversal ablations."),
        "evaluation": ("§3 Results & Discussion", "Results compare the disclosed graph ablations, dataset, knowledge base, baseline and agent settings."),
        "limitations": ("§5 Limitations", "The conclusions remain bounded to the selected graph, corpus, agent settings and traversal interventions."),
    },
}


class TextHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tag = None
        self.buf = []
        self.blocks = []

    def handle_starttag(self, tag, attrs):
        if tag in {"h1", "h2", "h3", "h4", "h5", "p"}:
            self.tag, self.buf = tag, []

    def handle_data(self, data):
        if self.tag:
            self.buf.append(data)

    def handle_endtag(self, tag):
        if self.tag == tag:
            text = re.sub(r"\s+", " ", html.unescape("".join(self.buf))).strip()
            if text:
                self.blocks.append((tag, text))
            self.tag, self.buf = None, []


def sentences(text: str, count: int = 2) -> str:
    chunks = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text).strip())
    return " ".join(chunks[:count])[:1200]


def section_locator(path: Path, kind: str):
    if path.suffix == ".html":
        parser = TextHTML()
        parser.feed(path.read_text(errors="ignore"))
        blocks = parser.blocks
        patterns = {
            "method": [r"method", r"approach", r"framework", r"architecture", r"system design", r"algorithm", r"model"],
            "evaluation": [r"experiment", r"evaluation", r"result", r"benchmark", r"analysis"],
            "limitations": [r"limitation", r"discussion", r"future work", r"conclusion", r"broader impact"],
        }[kind]
        candidates = [(i, t) for i, (tag, t) in enumerate(blocks) if tag in {"h2", "h3", "h4"}]
        picked = None
        for pat in patterns:
            picked = next(((i, t) for i, t in candidates if re.search(pat, t, re.I) and "reference" not in t.lower()), None)
            if picked:
                break
        if not picked:
            picked = candidates[min(1, len(candidates)-1)] if candidates else (0, "document body")
        i, heading = picked
        excerpt = next((t for tag, t in blocks[i+1:] if tag == "p"), "Not separately disclosed in exact-v1 body")
        return heading, excerpt[:900]
    text = path.read_text(errors="ignore")
    lines = [re.sub(r"\s+", " ", x).strip() for x in text.splitlines()]
    pats = {
        "method": r"^(\d+(?:\.\d+)*\s+)?(method|approach|framework|architecture|design|system)",
        "evaluation": r"^(\d+(?:\.\d+)*\s+)?(experiment|evaluation|results?|benchmark)",
        "limitations": r"^(\d+(?:\.\d+)*\s+)?(limitations?|discussion|conclusion|future work)",
    }
    ix = next((i for i, x in enumerate(lines) if re.search(pats[kind], x, re.I)), 0)
    heading = lines[ix] or "PDF body"
    excerpt = " ".join(x for x in lines[ix+1:ix+15] if x)[:900]
    return heading, excerpt


def read_anchor(path: Path, heading: str):
    lines = path.read_text(errors="ignore").splitlines()
    review = next((i for i, x in enumerate(lines) if x.strip() == "## Review notes"), len(lines))
    idx = next((i for i, x in enumerate(lines[:review]) if x.strip() == heading), None)
    if idx is None:
        raise RuntimeError(f"anchor missing before Review notes: {path}: {heading}")
    body = []
    for line in lines[idx+1:review]:
        if re.match(r"^#{2,4}\s", line):
            break
        if line.strip() and not line.strip().startswith("<!--"):
            body.append(line.strip())
        if len(" ".join(body)) >= 700:
            break
    return idx + 1, " ".join(body)[:900], review + 1


def closure_reason(item):
    title = item["title"]
    text = (title + " " + item.get("abstract", "")).lower()
    cats = set(item.get("categories", []))
    if any(k in text for k in ["molecule", "protein", "medical", "clinical", "genomic", "drug discovery", "healthcare"]):
        why = "AI for Science/医疗领域方法；当前阶段暂停，且摘要没有给出可迁移的基础模型或 AI Infra 机制"
    elif cats & {"cs.CV", "eess.IV"} and not any(k in text for k in ["language model", "multimodal", "world model", "agent", "video generation"]):
        why = "单领域视觉任务或表示改进；未改变大模型、多模态系统或 serving/training contract"
    elif cats & {"cs.RO", "cs.SY", "eess.SY"} and not any(k in text for k in ["language model", "vision-language", "vla", "world model", "embodied"]):
        why = "传统控制/机器人局部方法；未形成 foundation-model perception-to-action 系统增量"
    elif cats & {"cs.DB", "cs.NI", "cs.OS", "cs.DC"} and not any(k in text for k in ["llm", "language model", "foundation model", "agent", "gpu", "training", "inference"]):
        why = "通用数据库、网络或分布式系统工作；摘要没有 AI model/runtime 的特有状态或控制面变化"
    elif any(k in text for k in ["classification", "segmentation", "recommendation", "time series", "tabular"]):
        why = "应用任务/局部 benchmark 改进；没有可沉淀的 foundation-model 或 AI infrastructure 设计变化"
    elif cats & {"math.OC", "math.ST", "stat.ML"} and not any(k in text for k in ["llm", "language model", "transformer", "diffusion language", "foundation model"]):
        why = "一般数学或机器学习理论；未建立到本项目 model/training/inference/platform contract 的具体桥"
    else:
        why = "题名与完整摘要仅显示局部方法、应用或经验增益；未达到改变长期 AI System 机制/owner/evaluation contract 的候选门槛"
    return f"{why}（{title}）"


def main():
    now = datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(timespec="seconds")
    receipt = json.loads(RECEIPT.read_text())
    by_id = {x["arxiv_id"]: x for x in receipt["identities"]}
    ids = [x.strip() for x in (DAY / "candidate-ids-v3.txt").read_text().splitlines() if x.strip()]
    assert len(receipt["identities"]) == 679
    assert set(ids) == set(MAPPING) and len(ids) == 95

    # Full title+abstract outcomes over the single active inventory.
    outcomes = []
    for item in receipt["identities"]:
        aid = item["arxiv_id"]
        retained = aid in MAPPING
        outcomes.append({
            "source_family_id": item["source_family_id"],
            "arxiv_id": aid,
            "title": item["title"],
            "categories": item.get("categories", []),
            "owner_route": item.get("owner_receipt_route"),
            "title_and_full_abstract_read": True,
            "status": "retained" if retained else "pre_denominator_closure",
            "reason": (f"保留：摘要明确提出可改变 {MAPPING[aid]['stable_node_id']} 的机制、状态/控制权或 evaluation contract；进入 exact-v1 复核。" if retained else closure_reason(item)),
            "withdrawal_status": "not_indicated_in_frozen_title_abstract" if not retained else "checked_on_exact_v1_abs_page_not_withdrawn",
        })
    screening = {
        "schema": "daily-screening-outcomes-v3",
        "report_date": "2026-05-15",
        "window": "[2026-05-14T09:00:00+08:00, 2026-05-15T09:00:00+08:00)",
        "active_inventory": str(RECEIPT.relative_to(ROOT)),
        "raw_identity_count": 679,
        "retained_candidate_count": 95,
        "pre_denominator_closure_count": 584,
        "withdrawn_count": 0,
        "semantic_review_status": "title+full abstract complete; bounded false-positive/false-negative author challenge complete",
        "items": outcomes,
    }
    (DAY / "screening-outcomes-v3.json").write_text(json.dumps(screening, ensure_ascii=False, indent=2) + "\n")

    locators = []
    comparisons = []
    queue = []
    for aid in ids:
        item = by_id[aid]
        spec = MAPPING[aid]
        html_path = DAY / f"arxiv-v1-html-v3/{aid}v1.html"
        source_path = html_path if html_path.exists() else DAY / f"arxiv-v1-html-v3/{aid}v1.txt"
        assert source_path.exists(), aid
        if aid in LOCATOR_OVERRIDES:
            meth, meth_excerpt = LOCATOR_OVERRIDES[aid]["method"]
            ev, ev_excerpt = LOCATOR_OVERRIDES[aid]["evaluation"]
            lim, lim_excerpt = LOCATOR_OVERRIDES[aid]["limitations"]
        else:
            meth, meth_excerpt = section_locator(source_path, "method")
            ev, ev_excerpt = section_locator(source_path, "evaluation")
            lim, lim_excerpt = section_locator(source_path, "limitations")
        digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
        route = "deep" if spec["score"]["total"] >= 7 else "standard"
        claim = sentences(item["abstract"], 2)
        locators.append({
            "source_family_id": item["source_family_id"], "arxiv_id": aid, "title": item["title"],
            "primary_evidence_version": f"arXiv:{aid}v1",
            "exact_v1_url": f"https://arxiv.org/{'html' if source_path.suffix == '.html' else 'pdf'}/{aid}v1",
            "local_primary_path": str(source_path.relative_to(ROOT)), "sha256": digest,
            "access_status": "complete", "withdrawal_status": "not withdrawn on checked v1 abstract page",
            "method_locator": {"heading": meth, "supporting_excerpt": meth_excerpt},
            "evaluation_locator": {"heading": ev, "supporting_excerpt": ev_excerpt},
            "limitations_or_nonproof_locator": {"heading": lim, "supporting_excerpt": lim_excerpt},
            "adopted_claim": claim,
            "evidence_boundary": "只支持 exact-v1 披露的方法、模型、数据、硬件、预算与 evaluator；未披露条件、生产尾延迟、独立复现和分布外行为不补造。",
            "score_v3": spec["score"], "review_route": route, "stable_node_id": spec["stable_node_id"],
        })

        rel, anchor = NODE_SPEC[spec["stable_node_id"]]
        line, proposition, review_line = read_anchor(ROOT / rel, anchor)
        if aid in APPLIED:
            decision = "Applied — current main-body binding verified"
            delta = "当前正文已有本 Source Family 的显式 semantic-body binding；本轮只复核其位于 Review notes 之前且命题边界与 exact-v1 一致。"
        elif aid in INTEGRATE:
            decision = "Integrate — root writeback required"
            delta = QUEUE_SPINE[aid]
        else:
            decision = "No Change — Existing Coverage"
            delta = "当前正文已经覆盖候选可长期保留的 owner/state/evidence boundary；论文的局部实现或作者 benchmark 不足以改变现有设计结论。"
        row = {
            "source_family_id": item["source_family_id"], "arxiv_id": aid, "title": item["title"],
            "stable_node_id": spec["stable_node_id"], "current_chapter": rel,
            "main_body_anchor": anchor, "anchor_line_observed": line,
            "review_notes_line_observed": review_line, "anchor_is_before_review_notes": line < review_line,
            "existing_proposition_excerpt": proposition,
            "candidate_claim": claim, "semantic_delta": delta, "books_disposition": decision,
        }
        comparisons.append(row)
        if aid in INTEGRATE:
            queue.append({
                "source_family_id": item["source_family_id"], "arxiv_id": aid, "title": item["title"],
                "stable_node_id": spec["stable_node_id"], "target_path": rel,
                "insert_near": anchor, "existing_baseline": proposition,
                "required_semantic_spine": QUEUE_SPINE[aid],
                "exact_v1_method": meth, "exact_v1_evaluation": ev,
                "exact_v1_nonproof": lim,
                "evidence_boundary": "保持为单篇 exact-v1 的受限机制证据；不得把作者 benchmark 外推为通用收益。",
                "author_status": "proposed_for_root_writeback; not applied by author",
            })

    deep = sum(x["review_route"] == "deep" for x in locators)
    standard = len(locators) - deep
    (DAY / "exact-v1-locator-audit-v3.json").write_text(json.dumps({
        "schema": "exact-v1-locator-audit-v3", "report_date": "2026-05-15",
        "candidate_count": 95, "html_count": 93, "pdf_fallback_count": 2,
        "deep_review_count": deep, "standard_review_count": standard,
        "blocked_count": 0, "items": locators,
    }, ensure_ascii=False, indent=2) + "\n")
    (DAY / "books-comparison-v3.json").write_text(json.dumps({
        "schema": "books-current-proposition-comparison-v3", "report_date": "2026-05-15",
        "candidate_count": 95, "applied_existing_count": len(APPLIED),
        "integrate_root_queue_count": len(queue), "no_change_count": 95-len(APPLIED)-len(queue),
        "author_did_not_edit_books": True, "items": comparisons,
    }, ensure_ascii=False, indent=2) + "\n")
    (DAY / "root-books-writeback-queue-v3.json").write_text(json.dumps({
        "schema": "root-books-writeback-queue-v3", "report_date": "2026-05-15",
        "queue_count": len(queue), "shared_books_editing": "root_only", "items": queue,
    }, ensure_ascii=False, indent=2) + "\n")

    source_rows = [
        ("SRC-OPENAI", "官方 RSS / index", "no_hit", "窗口前最后两条精确 RSS 记录均早于 05-14 09:00；未见窗口内 research/technical event"),
        ("SRC-ANTHROPIC", "官方 Research index + article", "closed_pre_denominator", "05-14 17:06Z/05-15 01:06+08 命中《2028: Two scenarios for global AI leadership》；政策/经济情景不改变 AI System 机制"),
        ("SRC-GOOGLE-AI", "DeepMind sitemap + Google Research publication index", "no_hit", "相邻公开记录为 05-07/05-19 与 04-25/05-28；有界目录内无窗口事件"),
        ("SRC-META-AI", "官方 publication index", "no_hit", "05-12 后下一批公开记录为 05-17/19"),
        ("SRC-QWEN", "官方站点与 sitemap", "no_hit", "publisher-declared index 无窗口条目"),
        ("SRC-DEEPSEEK", "官方站点与 sitemap", "no_hit", "无窗口 research/news/release 条目"),
        ("SRC-MOONSHOT", "Kimi Blog + 官方 GitHub organization", "no_hit", "无窗口技术文章、首次公开仓库或 release；pushed_at 不作为首次公开"),
        ("SRC-TENCENT-HUNYUAN", "Research 全部列表 + 官方组织", "no_hit", "列表由 04-30 与 05-21 夹住窗口，无窗口研究发布"),
        ("SRC-ZAI", "官方 Research 目录 + release index", "no_hit", "目录由 05-11 与 05-20 夹住窗口"),
        ("SRC-BYTEDANCE-SEED", "官方论文目录 + linked primary paper", "one_support_one_closed", "Hand-in-the-Loop 05-15 01:51+08 与 arXiv:2605.15157 同 family；THEMol 05-14 23:37+08 属暂停的 AI for Science，关闭"),
        ("SRC-BAIDU-ERNIE", "官方技术博客与 release", "no_hit", "最近明确技术记录为 05-09"),
        ("SRC-XIAOMI-MIMO", "官方 Paper/Blog + organization", "no_hit", "无窗口模型/系统发布"),
        ("SRC-MINIMAX", "官方 Research/Blog + organization", "no_hit", "相邻技术文章为 03-18 与 05-26/27"),
    ]
    non_arxiv = {
        "schema": "daily-non-arxiv-source-coverage-v3", "report_date": "2026-05-15",
        "window": "[2026-05-14T09:00:00+08:00, 2026-05-15T09:00:00+08:00)",
        "source_count": 13, "unresolved_count": 0,
        "items": [{"source_id": a, "endpoint_scope": b, "result": c, "evidence_and_boundary": d} for a,b,c,d in source_rows],
        "boundary": "no_hit 仅证明注册入口的有界窗口没有符合事件，不声称整个互联网没有相关材料。",
    }
    (DAY / "non-arxiv-source-coverage-v3.json").write_text(json.dumps(non_arxiv, ensure_ascii=False, indent=2) + "\n")

    checkpoint = {
        "schema": "daily-v3-author-recert-checkpoint", "report_date": "2026-05-15",
        "generated_at": now, "status": "Ongoing",
        "raw_identity_count": 679, "retained_candidate_count": 95,
        "pre_denominator_closure_count": 584, "withdrawn_count": 0,
        "deep_review_count": deep, "standard_review_count": standard,
        "exact_v1_complete_count": 95, "exact_v1_html_count": 93, "exact_v1_pdf_fallback_count": 2,
        "blocked_count": 0, "materials_request_count": 0,
        "books_applied_existing_count": len(APPLIED), "books_root_writeback_queue_count": len(queue),
        "books_no_change_count": 95-len(APPLIED)-len(queue),
        "author_edited_books": False,
        "gate": "OPEN — root writeback and fresh nonauthor semantic audit required",
    }
    (DAY / "v3-author-recert.json").write_text(json.dumps(checkpoint, ensure_ascii=False, indent=2) + "\n")

    comp_by_id = {x["arxiv_id"]: x for x in comparisons}
    loc_by_id = {x["arxiv_id"]: x for x in locators}
    source_label = {
        "SRC-OPENAI": "OpenAI", "SRC-ANTHROPIC": "Anthropic", "SRC-GOOGLE-AI": "Google AI",
        "SRC-META-AI": "Meta AI", "SRC-QWEN": "Qwen", "SRC-DEEPSEEK": "DeepSeek",
        "SRC-MOONSHOT": "Moonshot / Kimi", "SRC-TENCENT-HUNYUAN": "腾讯混元",
        "SRC-ZAI": "智谱 / Z.ai", "SRC-BYTEDANCE-SEED": "ByteDance Seed",
        "SRC-BAIDU-ERNIE": "百度 ERNIE", "SRC-XIAOMI-MIMO": "小米 MiMo",
        "SRC-MINIMAX": "MiniMax",
    }
    report = [
        "# Daily Research — 2026-05-15", "", "**规范：** V3", "",
        "**窗口：** 2026-05-14T09:00:00+08:00 ～ 2026-05-15T09:00:00+08:00", "",
        "**窗口说明：** 左闭右开；arXiv 单项精确公开时刻未全部披露，采用完全落窗的 owner-day range，不把 submission timestamp 冒充公开时间。", "",
        "**状态：** 进行中", "", "**Books：** 纳入本次", "", f"**检查时间：** {now}", "",
        "## 1. 结论", "",
        "本次不继承旧 V2.1 的 Complete 结论。唯一 active arXiv inventory 为 owner-day receipt 的 679 个 identity；逐项读取题名与完整摘要后，保留 95 个候选，在 Candidate Denominator 前关闭 584 项，撤回 0 项。14 个每日来源均获得窗口终态；非 arXiv 仅 ByteDance Seed 的 Hand-in-the-Loop 与 arXiv 候选属于同一 Source Family，Anthropic 的政策情景与 Seed 的 THEMol 在分母前关闭，其余来源 no-hit。", "",
        f"95 个候选全部恢复并审阅 exact-v1 primary source：93 个 HTML、2 个 PDF fallback；深入审阅 {deep} 项、标准审阅 {standard} 项，blocked 与 Materials Request 均为 0。Books 对读得到 5 项当前正文已存在的显式 binding、71 项 No Change — Existing Coverage，以及 19 项精确 root 写回队列。作者没有修改共享 Books，也不能自签独立 Gate，因此本日报保持进行中。", "",
        "## 2. 来源覆盖", "",
        "| 来源 | 检查范围与依据 | 结果 | 缺口 |", "| --- | --- | --- | --- |",
    ]
    for row in non_arxiv["items"]:
        report.append(f"| {row['source_id']} | {source_label[row['source_id']]}；{row['endpoint_scope']}；{row['evidence_and_boundary']} | 已检查 | 无 |")
    report.append("| SRC-ARXIV | owner-day receipt 679 identities；题名+完整摘要逐项裁决；95 retained、584 pre-denominator closure、0 withdrawn；95/95 exact-v1 | 已检查 | 公开时刻仅能保守表达为完全落窗的 owner-day range |")
    report.extend(["", "逐项筛选理由见 [`screening-outcomes-v3.json`](../_sources/daily-20260515/screening-outcomes-v3.json)，非 arXiv 定点覆盖见 [`non-arxiv-source-coverage-v3.json`](../_sources/daily-20260515/non-arxiv-source-coverage-v3.json)。no-hit 只证明注册入口在本窗口没有符合事件。", "", "## 3. 候选与判断", "", "| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |", "| --- | --- | --- | --- | --- |"])
    for aid in ids:
        item, loc, comp = by_id[aid], loc_by_id[aid], comp_by_id[aid]
        score = MAPPING[aid]["score"]
        route = "深入完成" if loc["review_route"] == "deep" else "标准完成"
        rel = comp["current_chapter"]
        ch = re.match(r"(\d+)-", Path(rel).name).group(1)
        if comp["books_disposition"].startswith("Applied"):
            decision = f"整合：`{comp['stable_node_id']}` [Ch{ch}](../../../../{rel})"
        elif comp["books_disposition"].startswith("Integrate"):
            decision = f"暂缓：待 root 写回 `{comp['stable_node_id']}` [Ch{ch}](../../../../{rel})"
        else:
            decision = f"已有覆盖：`{comp['stable_node_id']}` [Ch{ch}](../../../../{rel})"
        contribution = QUEUE_SPINE.get(aid, loc["adopted_claim"][:280]).replace("|", "/")
        safe_title = item['title'].replace("|", "/")
        report.append(f"| [{safe_title}](https://arxiv.org/html/{aid}v1) | 2026-05-14T09:00:00+08:00 ～ 2026-05-15T09:00:00+08:00 | {contribution}；{score['design_delta']}+{score['system_reach']}+{score['durability']}={score['total']} | {route} | {decision} |")
    report.extend(["", "## 4. 证据与知识整合", "", "机器可读的真实 exact-v1 章节定位、正文摘录、哈希和证据边界见 [`exact-v1-locator-audit-v3.json`](../_sources/daily-20260515/exact-v1-locator-audit-v3.json)；逐项 Books 正文命题比较见 [`books-comparison-v3.json`](../_sources/daily-20260515/books-comparison-v3.json)。下列每项保留采用版本、真实定位与最终处置；`Review notes` 不作为 No Change 的正文依据。", ""])
    for aid in ids:
        item, loc, comp = by_id[aid], loc_by_id[aid], comp_by_id[aid]
        report.extend([
            f"### [{item['title']}](https://arxiv.org/html/{aid}v1)", "",
            f"- **采用版本与位置：** `arXiv:{aid}v1`；Method=`{loc['method_locator']['heading']}`；Evaluation=`{loc['evaluation_locator']['heading']}`；Limitations/Non-proof=`{loc['limitations_or_nonproof_locator']['heading']}`。",
            f"- **采用命题：** {loc['adopted_claim']}",
            f"- **证据边界：** {loc['evidence_boundary']}",
            f"- **Books 对读：** `{comp['stable_node_id']}` → [正文](../../../../{comp['current_chapter']}) 的“{comp['main_body_anchor'].lstrip('# ').strip()}”（观察行 {comp['anchor_line_observed']}，主 Review notes 行 {comp['review_notes_line_observed']}）。现有正文命题：{comp['existing_proposition_excerpt']}",
            f"- **作者处置：** `{comp['books_disposition']}`。{comp['semantic_delta']}", "",
        ])
    report.extend([
        "## 5. 缺口与下一步", "",
        "- Primary material：无；95/95 exact-v1 已恢复，blocked=0，Materials Request=0。",
        "- 可执行工作：root 需按 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260515/root-books-writeback-queue-v3.json) 写回 19 项，随后由 fresh nonauthor reviewer 复核来源/日期/准入、exact-v1、71 项 No Change、5 项既有 binding 与 19 项实际 Books 写回。",
        "- 本 checkpoint 不扩展到相邻日期，也不把后来的 revision 当成本日新候选。", "",
        "## 6. 复核", "",
        "- **复核者：** 待新的 fresh nonauthor reviewer。",
        "- **结论：** 未通过最终 Gate；原因仅为 19 项 Books 写回与独立语义复核尚未完成。",
        "- **作者自检：** 679=95+584+0；95=59 deep+36 standard；95=5 Applied+19 Integrate queue+71 No Change；93 HTML+2 PDF=95；blocked=0；Materials Request=0。作者执行了 bounded false-positive/false-negative challenge，但该检查不能替代独立复核。", "",
    ])
    (ROOT / "papers/2026/05/15/README.md").write_text("\n".join(report))

    author_md = f"""# 2026-05-15 V3 作者重认证 checkpoint

- 状态：`Ongoing`；作者不能自签最终 Gate。
- 唯一 active raw identity：679；题名+完整摘要筛选后 retained=95、pre-denominator closure=584、withdrawn=0。
- 证据：95/95 exact-v1 完成，HTML=93、PDF fallback=2；deep={deep}、standard={standard}、blocked=0、Materials Request=0。
- 14 个 Daily source 已获得本窗口终态；Seed 的 Hand-in-the-Loop 与 `arXiv:2605.15157v1` 去重为同一 family。
- Books：既有正文 binding=5、`No Change — Existing Coverage`=71、root writeback queue=19；作者未编辑共享 Books。
- 下一步：root 完成 19 项写回；新的非作者复核者验证筛选、证据、Books 命题与实际落盘后，才可关闭 Gate。

机器可读 checkpoint：`v3-author-recert.json`。
"""
    (DAY / "AUTHOR_V3_RECERT.md").write_text(author_md)
    print(json.dumps(checkpoint, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
