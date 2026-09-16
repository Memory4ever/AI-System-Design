#!/usr/bin/env python3
"""Rebuild the 2026-05-07 author packet after the independent audit.

This deliberately keeps the report In Progress until a non-author review has
checked the repaired denominator, exact-v1 evidence and Books dispositions.
"""

from __future__ import annotations

import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
ROOT = Path(__file__).resolve().parent
REPORT = REPO / "papers/2026/05/07/README.md"
OWNER_RECEIPT = ROOT.parent / "arxiv-owner-replay-20260903/20260507/arxiv-owner-receipt.json"
DATE_PROVENANCE = ROOT.parent / "ARXIV_ANNOUNCEMENT_PROVENANCE.md"


class PaperParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tag: str | None = None
        self.buf: list[str] = []
        self.sections: list[dict[str, object]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li"}:
            self.tag = tag
            self.buf = []

    def handle_data(self, data: str) -> None:
        if self.tag:
            self.buf.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag != self.tag:
            return
        text = re.sub(r"\s+", " ", html.unescape(" ".join(self.buf))).strip()
        if tag.startswith("h"):
            self.sections.append({"heading": text, "texts": []})
        elif text and self.sections:
            self.sections[-1]["texts"].append(text)
        self.tag = None
        self.buf = []


def first_sentences(text: str, limit: int = 420) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    sentences = re.split(r"(?<=[.!?])\s+", text)
    out = ""
    for sentence in sentences:
        if out and len(out) + len(sentence) > limit:
            break
        out = (out + " " + sentence).strip()
        if len(out) >= 180:
            break
    return out[:limit] or "原文未提供可抽取的正文句。"


def pick_section(sections: list[dict[str, object]], patterns: list[str], exclude: list[str] | None = None) -> tuple[str, str]:
    exclude = exclude or []
    for section in sections:
        heading = str(section["heading"])
        low = heading.lower()
        texts = section["texts"]
        if texts and any(re.search(pattern, low) for pattern in patterns) and not any(word in low for word in exclude):
            return heading, first_sentences(" ".join(str(x) for x in texts))
    return "未单列", "未找到独立章节；只采用摘要与结论能够直接支持的窄命题。"


def paper_extract(arxiv_id: str) -> dict[str, str]:
    path = Path(f"/tmp/may07-{arxiv_id}.html")
    parser = PaperParser()
    parser.feed(path.read_text(errors="ignore"))
    title = next(
        (
            str(s["heading"])
            for s in parser.sections
            if str(s["heading"]).lower() not in {"abstract", "report github issue"}
            and not re.match(r"^\d+(?:\.\d+)*\s", str(s["heading"]))
        ),
        arxiv_id,
    )
    abstract_text = ""
    for section in parser.sections:
        if str(section["heading"]).lower() == "abstract":
            abstract_text = " ".join(str(x) for x in section["texts"])
            break
    method = pick_section(
        parser.sections,
        [r"method", r"framework", r"architecture", r"system design", r"algorithm", r"approach", r"mechanism"],
        ["related", "background", "prelim", "comparison"],
    )
    evaluation = pick_section(parser.sections, [r"evaluation", r"experiment", r"results?"])
    limitations = pick_section(parser.sections, [r"limitations?"])
    if limitations[0] == "未单列":
        limitations = pick_section(parser.sections, [r"discussion", r"conclusion"])
    return {
        "title": title,
        "abstract": re.sub(r"\s+", " ", abstract_text).strip(),
        "method_heading": method[0],
        "method_evidence": method[1],
        "evaluation_heading": evaluation[0],
        "evaluation_evidence": evaluation[1],
        "limitations_heading": limitations[0],
        "limitations_evidence": limitations[1],
    }


def exact_section(arxiv_id: str, pattern: str) -> tuple[str, str]:
    parser = PaperParser()
    parser.feed(Path(f"/tmp/may07-{arxiv_id}.html").read_text(errors="ignore"))
    for section in parser.sections:
        heading = str(section["heading"])
        if re.search(pattern, heading, re.I):
            texts = " ".join(str(item) for item in section["texts"])
            return heading, first_sentences(texts)
    return "未单列", "exact-v1 未单列该项；只保留原文摘要与可定位结果能够直接支持的窄命题。"


old_report = REPORT.read_text()
old_table = old_report[old_report.index("## 3. 候选与判断") : old_report.index("## 4. 证据与知识整合")]

row_re = re.compile(
    r"^\| \[(?P<title>[^\]]+)\]\(https://arxiv\.org/(?:html|abs)/(?P<id>2605\.\d+)(?:v1)?\) \| (?P<date>[^|]+) \| (?P<delta>.*?)；\*\*(?P<d>[0-3]) \+ (?P<s>[0-3]) \+ (?P<u>[0-3]) = (?P<t>[0-9])\*\* \| (?P<review>[^|]+) \| (?P<books>[^|]+) \|$",
    re.M,
)
existing: dict[str, dict[str, object]] = {}
for match in row_re.finditer(old_table):
    data = match.groupdict()
    books = str(data["books"]).strip()
    node_match = re.search(r"`([^`]+)`", books)
    chapter_match = re.search(r"\((\.\./\.\./\.\./\.\./books/[^)]+)\)", books)
    existing[str(data["id"])] = {
        "title": str(data["title"]),
        "delta": str(data["delta"]),
        "score": [int(data["d"]), int(data["s"]), int(data["u"])],
        "review": str(data["review"]).strip(),
        "books": books,
        "node": node_match.group(1) if node_match else "",
        "chapter": chapter_match.group(1) if chapter_match else "",
    }


ADDED: dict[str, dict[str, object]] = {
    "2605.04055": {"delta": "各参数组的梯度、动量与相关性统计可以驱动 group-wise learning-rate / weight-decay 调节，但元优化器自身增加训练状态、目标耦合与额外计算", "score": [2, 1, 2], "node": "TRAIN-PRETRAINING", "chapter": "../../../../books/part-04-training-system/28-pretraining.md", "decision": "暂缓"},
    "2605.04058": {"delta": "混合精度冻结主干释放出的显存可以转投 side-MoE 容量，但收益依赖量化误差、路由交互与任务分布", "score": [2, 1, 2], "node": "TRAIN-LORA", "chapter": "../../../../books/part-04-training-system/30-lora.md", "decision": "已有覆盖"},
    "2605.04061": {"delta": "单位置 probe 可读不等于单位置具有因果控制力；ICL task template 由跨位置、跨层的分布式状态共同承载", "score": [3, 1, 3], "node": "MODEL-SELF-ATTENTION", "chapter": "../../../../books/part-02-model/14-self-attention.md", "decision": "整合"},
    "2605.04069": {"delta": "参数化 expert cache 只有在 validity domain 可认证时才能把近似复用从命中启发式变成 correctness contract", "score": [2, 2, 2], "node": "INFER-KV-CACHE", "chapter": "../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md", "decision": "已有覆盖"},
    "2605.04261": {"delta": "VLM 的感知差异可被攻击者用来借模型权威背书外部观察者看到的另一内容，使视觉输入成为 effect-side trust boundary", "score": [3, 2, 3], "node": "PLATFORM-SECURITY", "chapter": "../../../../books/part-06-ai-infrastructure/72-security.md", "decision": "整合"},
    "2605.04269": {"delta": "非平稳目标下 Adam 的历史矩估计会变成 stale state；优化器选择取决于 gradient noise 与 objective drift 的相对主导", "score": [2, 1, 3], "node": "TRAIN-PRETRAINING", "chapter": "../../../../books/part-04-training-system/28-pretraining.md", "decision": "整合"},
    "2605.04312": {"delta": "多智能体对局生成的新鲜任务可以同时缓解 benchmark 饱和与训练污染，但测到的是特定 game policy 下的相对能力", "score": [2, 2, 2], "node": "PLATFORM-EVALUATION-SYSTEM", "chapter": "../../../../books/part-06-ai-infrastructure/66-evaluation-system.md", "decision": "已有覆盖"},
    "2605.04563": {"delta": "Range Identifier 把显存错误保护从逐 bit 正确性改为数值范围内的有界近似恢复，新增了可声明的误差 contract", "score": [2, 2, 2], "node": "INFER-TENSORRT-LLM", "chapter": "../../../../books/part-05-inference-system/49-tensorrt-llm.md", "decision": "整合"},
    "2605.04698": {"delta": "持续摄取使 poisoning 从一次性训练集问题变成带延迟显现、lineage 与撤销责任的供应链控制问题", "score": [3, 3, 3], "node": "PLATFORM-SECURITY", "chapter": "../../../../books/part-06-ai-infrastructure/72-security.md", "decision": "整合"},
    "2605.04700": {"delta": "音频 token 对齐梯度高度非均匀，使少数 waveform 区域足以承载 jailbreak 优化，也暴露多模态安全评测的稀疏攻击面", "score": [3, 1, 3], "node": "PLATFORM-SECURITY", "chapter": "../../../../books/part-06-ai-infrastructure/72-security.md", "decision": "整合"},
    "2605.04711": {"delta": "optimizer state 可依据各 block 的 gradient stream 风险，在统一 memory/time budget 下做配置分配，而不是全模型固定 recipe", "score": [3, 2, 2], "node": "TRAIN-PRETRAINING", "chapter": "../../../../books/part-04-training-system/28-pretraining.md", "decision": "整合"},
    "2605.04874": {"delta": "多模态 DPO 可用 token-level epistemic uncertainty 重分配偏好学习压力，但该信号仍由训练中模型自估并可能失准", "score": [2, 1, 3], "node": "TRAIN-DPO", "chapter": "../../../../books/part-04-training-system/34-dpo.md", "decision": "整合"},
    "2605.04893": {"delta": "attention 谱诊断存在 orientation-blind 的可证明不可辨识边界，因此 hallucination sensor 必须区分 transport capacity 与 flow orientation", "score": [3, 1, 3], "node": "PLATFORM-EVALUATION-SYSTEM", "chapter": "../../../../books/part-06-ai-infrastructure/66-evaluation-system.md", "decision": "整合"},
    "2605.04932": {"delta": "covariate drift 风险需要绑定局部 Jacobian、邻域与估计误差，而不能把 IID holdout 分数直接外推到部署分布", "score": [3, 2, 2], "node": "PLATFORM-EVALUATION-SYSTEM", "chapter": "../../../../books/part-06-ai-infrastructure/66-evaluation-system.md", "decision": "整合"},
    "2605.05003": {"delta": "reward model 的通用指令偏好分数不能代替社会域 preference audit；bias avoidance 与 context faithfulness 还可能相互冲突", "score": [2, 1, 3], "node": "PLATFORM-EVALUATION-SYSTEM", "chapter": "../../../../books/part-06-ai-infrastructure/66-evaluation-system.md", "decision": "已有覆盖"},
    "2605.05029": {"delta": "最小预测误差可以系统性偏好环境慢变量而不是目标系统的因果状态，world-model objective 必须显式声明 system/environment boundary", "score": [3, 2, 3], "node": "MULTIMODAL-WORLD-MODELS", "chapter": "../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md", "decision": "整合"},
    "2605.05092": {"delta": "driver-centric world model 用有向 external-to-internal gate 保留交通条件对舱内状态转移的控制，而不是优化通用视频相似度", "score": [2, 2, 3], "node": "MULTIMODAL-WORLD-MODELS", "chapter": "../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md", "decision": "整合"},
    "2605.05116": {"delta": "无语义 junk token 也能触发目标有害前缀，说明对齐安全边界不能只覆盖人类可解释的 jailbreak prompt", "score": [3, 1, 3], "node": "PLATFORM-SECURITY", "chapter": "../../../../books/part-06-ai-infrastructure/72-security.md", "decision": "整合"},
}

# The title/abstract re-audit confirmed that these two prior entries do not
# cross the project contribution gate.  They remain in the 548-row ledger with
# family-specific closure reasons; neither is silently deleted.
FORCE_CLOSED = {
    "2605.04172": "通用可编程 memory hierarchy 的 ISA/microarchitecture 形式一致性；未改变当前大模型训练或推理链的 owner、控制面或评价合同。",
    "2605.04450": "生成式推荐系统的 EMB/KV 双缓存只在其推荐 workload 与 32-node A100 evaluation 内成立；没有证明 LLM serving 的 KV 生命周期或调度结论。",
}

# Correct the reviewer-confirmed mechanism error.
existing["2605.04107"]["delta"] = (
    "TSCG 将 JSON tool schema 确定性编译为 token-efficient structured text，直接改变 schema 表征、"
    "压缩和 tool-selection 输入；它不提供 validator、adapter 或 effect-side correctness。"
)

candidate_ids = (set(existing) | set(ADDED)) - set(FORCE_CLOSED)

owner_receipt = json.loads(OWNER_RECEIPT.read_text())
source_rows: dict[str, dict[str, object]] = {
    row["arxiv_id"]: dict(row) for row in owner_receipt["identities"]
}
assert len(source_rows) == 548, f"owner receipt drifted: {len(source_rows)}"
missing_candidates = candidate_ids - set(source_rows)
assert not missing_candidates, f"candidate outside owner receipt: {sorted(missing_candidates)}"
assert DATE_PROVENANCE.exists(), "shared arXiv announcement provenance is missing"

extracts = {arxiv_id: paper_extract(arxiv_id) for arxiv_id in sorted(candidate_ids)}

# arXiv did not expose an HTML rendering for this exact v1.  The official v1
# PDF was read directly; these locators and bounded claims are transcribed from
# the named sections rather than inferred from the abstract.
extracts["2605.04264"] = {
    "title": "Governed Collaborative Memory as Artificial Selection in LLM-Based Multi-Agent Systems",
    "abstract": extracts["2605.04264"]["abstract"],
    "method_heading": "3 Architecture and Mechanism",
    "method_evidence": (
        "The design separates agent-local, shared institutional, archive and project-continuity memory, "
        "then requires explicit candidate evaluation, ratification, provenance, version lineage and "
        "supersede-not-erase semantics before shared-state fixation."
    ),
    "evaluation_heading": "4 Evidence from One Running Ecosystem",
    "evaluation_evidence": (
        "The evidence is 12 event records, 8 active principles and a registry covering 17 resources / "
        "22 versions from one running ecosystem; the paper presents these as qualitative case traces, "
        "not a controlled comparison."
    ),
    "limitations_heading": "5 Design Implications and Limits",
    "limitations_evidence": (
        "The paper explicitly leaves multi-actor governance, operator bias, legacy-memory bootstrapping "
        "and comparative benchmarks unresolved; human ratification can itself become a bottleneck and "
        "does not prevent all confabulation or convergence."
    ),
}

# High-risk families called out by the independent review use explicit primary
# section locators instead of the generic heading heuristic.
EXPLICIT_SECTIONS = {
    "2605.04055": (r"^2\.6\s+Algorithm Summary$", r"^3\.2\.1\s+Performance Comparison$", r"^3\.5\s+Memory and Computation Overhead$"),
    "2605.04075": (r"^3\.4\s+Entropy-Guided KV Retention Estimator$", r"^4\.2\s+Experiment Results$", r"^6\s+Limitation$"),
    "2605.04061": (r"^3\.5\s+Multi-Position Intervention$", r"^4\.4\s+Multi-Position Intervention", r"^Appendix D\s+Limitations and Future Work$"),
    "2605.04069": (r"^4\.3\s+LAWS Update Protocol$", r"^5\.1\s+Self-Certification$", r"^11\.4\s+Limitations$"),
    "2605.04107": (r"^3\s+The TSCG Framework$", r"^6\.1\s+Small-Model Enablement", r"^8\s+Limitations$"),
    "2605.04135": (r"^3\.2\s+Corpus construction$", r"^4\.1\s+Descriptive findings$", r"^6\.1\s+Corpus-selection bias$"),
    "2605.04178": (r"^IV\s+Analytical Model$", r"^V\s+Model Validation and Accuracy$", r"^IV-G\s+Assumptions and Extensions$"),
    "2605.04236": (r"^3\s+The DASE System$", r"^5\s+GPQA-Extended: Primary Validation", r"^Scope and exploratory findings\.$"),
    "2605.04261": (r"^4\.\s+AI Authority Laundering Attacks$", r"^5\.\s+Validating Authority Laundering in the Wild$", r"^6\.1\.\s+Limitations and Failure Cases$"),
    "2605.04269": (r"^3\.1\s+Tracking under adaptive strong monotonicity$", r"^5\s+Numerical Experiments$", r"^6\s+Conclusion$"),
    "2605.04295": (r"^3\.1\s+Adjusted Semantic Uncertainty$", r"^4\s+Experimental Evaluations$", r"^5\s+Conclusion$"),
    "2605.04312": (r"^3\s+Game Structure$", r"^6\s+Results$", r"^8\.1\s+Limitations$"),
    "2605.04333": (r"^2\s+Multi-plane Topology Co-Design$", r"^5\s+Experiments$", r"^7\s+Conclusions$"),
    "2605.04563": (r"^V\s+RangeGuard$", r"^VI\s+Evaluation$", r"^VII\s+Conclusion$"),
    "2605.04568": (r"^4\s+Dream-MPC: Gradient-Based Model Predictive Control$", r"^5\s+Experiments$", r"^Appendix A\s+Limitations"),
    "2605.04595": (r"^3\s+Model$", r"^5\s+Numerical Experiments$", r"^6\s+Conclusion and Discussion$"),
    "2605.04624": (r"^5\s+Modular screening architecture$", r"^6\s+Mechanism-anchored validation", r"^13\s+Limitations, governance, and conclusion$"),
    "2605.04638": (r"^3\s+Semantic Gradients$", r"^4\s+Empirical Evaluations$", r"^Appendix A\s+Limitation$"),
    "2605.04698": (r"^2\.2\s+Poisoning Threat Model$", r"^4\s+Experimental Evaluation$", r"^5\s+Limitations and Future Work$"),
    "2605.04700": (r"^5\s+Token-Aware Gradient Optimization$", r"^6\.2\s+Evaluation results on AdvBench-50$", r"^7\s+Conclusion$"),
    "2605.04711": (r"^3\s+Mechanism of BAOC$", r"^4\s+Experiments$", r"^5\s+Discussion$"),
    "2605.04874": (r"^4\s+Methodology$", r"^6\.2\s+Main Results$", r"^7\s+Conclusion$"),
    "2605.04893": (r"^4\s+Limits of Symmetric Spectral Diagnostics$", r"^6\s+Evaluation Protocol$", r"^8\.2\s+Limitations$"),
    "2605.04901": (r"^4\s+Extraction Attack of the LOE Inference$", r"^5\.3\s+Results on Extracted Model Weights$", r"^Limitations$"),
    "2605.04932": (r"^V\s+Method$", r"^VI\s+Experiments$", r"^VII\s+Discussion and Limitations$"),
    "2605.05003": (r"^3\s+Methods$", r"^5\s+Results$", r"^Limitations$"),
    "2605.05029": (r"^S1\s+Full proof of the impossibility theorem$", r"^S8\.5\s+Full distribution$", r"^S4\.4\s+OOD evaluation$"),
    "2605.05049": (r"^III\s+Piper: A Framework", r"^VII\s+Scalable Training of SOTA MoE Models$", r"^VIII\s+Conclusion and Discussion$"),
    "2605.05058": (r"^III-A\s+.*Security.*Cube", r"^IV-B\s+Model Robustness Landscape$", r"^V\s+Outlook$"),
    "2605.05092": (r"^3\.3\s+Causal Driver World Model$", r"^4\.2\s+Main Results$", r"^Appendix 0\.A\s+Discussions$"),
    "2605.05097": (r"^3\.2\s+Multi-Timescale Edge Dynamics$", r"^A\.4\s+Is the Slow Variable Necessary", r"^A\.5\s+Scope$"),
    "2605.05116": (r"^Greedy random-search\.$", r"^Harmful Behavior of Junking Sequences\.$", r"^Appendix A\s+Limitations"),
    "2605.05170": (r"^2\s+DC-built Designs$", r"^2\.1\.3\s+Verification$", r"^4\.2\s+Limitations$"),
    "2605.05185": (r"^4\s+Training$", r"^5\s+Experiments$", r"^Limitations and Future Work$"),
}
for arxiv_id, (method_pattern, evaluation_pattern, limitation_pattern) in EXPLICIT_SECTIONS.items():
    method = exact_section(arxiv_id, method_pattern)
    evaluation = exact_section(arxiv_id, evaluation_pattern)
    limitation = exact_section(arxiv_id, limitation_pattern)
    extracts[arxiv_id].update(
        method_heading=method[0],
        method_evidence=method[1],
        evaluation_heading=evaluation[0],
        evaluation_evidence=evaluation[1],
        limitations_heading=limitation[0],
        limitations_evidence=limitation[1],
    )

# This theorem-only HTML renders the update protocol and certification mostly
# as display equations/lists.  Preserve the exact locators and the narrow claim
# instead of emitting an empty extraction placeholder.
extracts["2605.04069"].update(
    method_heading="4.3 LAWS Update Protocol",
    method_evidence=(
        "On an uncovered branch the system evaluates the base model, fits a parametrized expert, "
        "stores its prefix, parameters and validity radius, and routes later queries only while "
        "the certified domain remains valid; misses return to base inference and expert creation."
    ),
    evaluation_heading="5.1 Self-Certification",
    evaluation_evidence=(
        "The evidence is an analytic Lipschitz error bound for every routed expert inside its "
        "declared radius; this exact v1 does not provide a matched end-to-end LLM-serving benchmark."
    ),
)

DIRECT_BOUNDARIES = {
    "2605.04055": "评价只覆盖五类中小规模任务及论文给定的 group construction、meta objective 与 update frequency；它没有证明在大模型预训练规模下优于可观测性驱动的人工分组策略，且注意力元优化器本身增加 memory、compute 与新的优化耦合。",
    "2605.04061": "实验只覆盖四个 1B–3B 级开源模型、八个受控 ICL transformation tasks 与 activation transplantation/noise intervention；它区分 probe 可读性与因果 sufficiency，但不证明任意语义任务或更大模型具有相同层位和模板分布。",
    "2605.04107": "TAB 是自建 benchmark，作者虽补充 BFCL 与 MCP transfer，仍需要第三方 catalog 复验；论文优化的是 schema 表征、压缩和 tool selection/parameter extraction，不证明 tool effect、validator 或 adapter correctness。",
    "2605.04264": extracts["2605.04264"]["limitations_evidence"],
    "2605.04269": "理论依赖 bounded gradients、sub-Gaussian noise、Lipschitz/monotonicity 等假设，数值实验使用合成/受控非平稳任务；不能直接推出大模型预训练中 Adam 或 SGD 的普遍优劣。",
    "2605.04312": "结果来自 999 场、49 个模型参与的固定七人淘汰游戏；作者明确列出渐近饱和、低风险任务与未建模 matchup effects，因此它只能支持该 game policy 下的相对 evaluation，不是通用智能排序。",
    "2605.04563": "实验覆盖论文给定的 DNN、错误模型与硬件估计；bounded approximate correction 接受受控数值偏差，不等价于逐 bit 正确，也未给出所有 LLM workload/SLO 下的端到端证明。",
    "2605.04711": "风险由多个 block-wise gradient proxy 线性组合，MILP 只在固定 block partition、配置菜单与外部 memory/time budget 内求解；论文未证明全局最优 optimizer recipe，也未消除 state inheritance 与在线重分配风险。",
    "2605.04874": "token-level epistemic uncertainty 由训练中模型自身估计，可能与真实认知缺口不一致；结果绑定论文披露的 MLLM、偏好构造与 hallucination benchmark。",
    "2605.04893": "论文证明 symmetric spectral diagnostics 的 orientation blindness，并在所测架构上展示相关性；它明确不建立因果诊断，方向、极性与规模外推均需独立校准。",
    "2605.04901": "攻击在小规模模型与论文威胁模型中验证，作者明确指出扩展到更大模型仍受神经攻击可扩展性限制；结论是服务器权重机密性受损，不是客户端输入恢复。",
    "2605.05029": "不可行性构造与神经证据来自线性高斯系统、合成非线性 GRU 与论文定义的 causal-fidelity 指标；它否定 predictive loss 自动恢复因果 state 的一般保证，不证明任意真实 world model 都会失败。",
    "2605.05116": "greedy random search 在论文模型、目标前缀和 10^5 量级查询预算下展示 non-semantic trigger；这是一项 proof of concept，不证明低成本黑盒攻击普遍成功。",
    "2605.05170": "论文支持的是若干 RTL/accelerator 设计案例、验证流程与 human-review bottleneck 观察；constraint revision、milestone commit 与最终 acceptor 分权是本书据此形成的工程推论，不是论文直接证明的通用 Agent contract。",
}
rows: list[dict[str, object]] = []
for arxiv_id, source in source_rows.items():
    row = dict(source)
    datacite_date = str(row.get("datacite_initial_created_timestamp", ""))[:10]
    oai_dates = row.get("oai_current_datestamps") or []
    id_month_ok = arxiv_id.startswith("2605.")
    version_identity_ok = bool(row.get("v1_submission_timestamp_provenance_only"))
    direct_oai_match = "2026-05-07" in oai_dates
    if datacite_date == "2026-05-07" and id_month_ok and version_identity_ok:
        route = "direct OAI corroboration" if direct_oai_match else "revision-route reconciliation"
        row.update(
            owner_evidence_status="public_batch_derived_consistent",
            owner_evidence_route=route,
            first_public_time_derived="2026-05-07T08:00:00+08:00",
            owner_evidence=(
                "arXiv ID-at-announcement and exact-v1/version identity + DataCite initial "
                f"created 2026-05-07 + {route}; 08:00 is derived from Wednesday 20:00 "
                "EDT, not a per-paper timestamp disclosed by the abstract page"
            ),
        )
    else:
        row.update(
            owner_evidence_status="owner_conflict",
            first_public_time_derived=None,
            owner_evidence="DataCite/OAI/arXiv identity evidence does not reconcile to the 2026-05-07 batch",
        )
    if arxiv_id in candidate_ids:
        if arxiv_id in ADDED:
            spec = ADDED[arxiv_id]
            title = str(source["title"])
            delta = str(spec["delta"])
            score = list(spec["score"])
            node = str(spec["node"])
            chapter = str(spec["chapter"])
            decision = str(spec["decision"])
        else:
            spec = existing[arxiv_id]
            title = str(spec["title"])
            delta = str(spec["delta"])
            score = list(spec["score"])
            node = str(spec["node"])
            chapter = str(spec["chapter"])
            decision = "整合" if str(spec["books"]).startswith("整合") else "已有覆盖"
        row.update(
            title=title,
            abstract=row.get("abstract") or extracts[arxiv_id]["abstract"],
            screening_status="retained",
            screening_reason=delta,
            owner_node=node,
            owner_chapter=chapter,
            score_v2={"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
            review_status="deep_complete" if sum(score) >= 7 or decision == "整合" else "standard_complete",
            access_status=("verified_exact_v1_pdf" if arxiv_id == "2605.04264" else "verified_exact_v1_html"),
            integration_disposition=decision,
        )
    elif arxiv_id == "2605.04356":
        row.update(
            screening_status="withdrawn_excluded",
            screening_reason=(
                "arXiv v1 is withdrawn and the abstract page states that administrators "
                "removed it because the submitter lacked licensing authority"
            ),
            review_status="withdrawal_verified",
            access_status="withdrawn",
            integration_disposition="Excluded — Withdrawn",
        )
    else:
        closure_reason = FORCE_CLOSED.get(arxiv_id) or str(row.get("screening_reason", "")).strip()
        if not closure_reason:
            closure_reason = "题目与完整摘要未显示会改变当前 AI System 的长期机制、状态/数据/控制 owner、评价合同或既有 Books 结论。"
        row.update(
            screening_status="pre_denominator_closure",
            screening_reason=closure_reason,
            review_status="identity_and_semantic_closure",
            access_status=row.get("access_status") or "verified_identity_abstract",
            integration_disposition="Rejected — Below Candidate Denominator",
        )
    rows.append(row)
rows.sort(key=lambda item: item["arxiv_id"])

retained = [row for row in rows if row["screening_status"] == "retained"]
closures = [row for row in rows if row["screening_status"] == "pre_denominator_closure"]
withdrawn = [row for row in rows if row["screening_status"] == "withdrawn_excluded"]
date_consistent = [row for row in rows if row["owner_evidence_status"] == "public_batch_derived_consistent"]
date_recovery = [row for row in rows if row.get("owner_evidence_route") == "revision-route reconciliation"]
candidate_date_gaps = [row for row in retained if row["owner_evidence_status"] != "public_batch_derived_consistent"]

ledger = {
    "schema": "daily-screening-ledger-v3-author-repair",
    "report_date": "2026-05-07",
    "window": "[2026-05-06T09:00:00+08:00,2026-05-07T09:00:00+08:00)",
    "identity_scope": (
        "548 distinct arXiv identities reconciled with ID-at-announcement semantics, "
        "DataCite initial-created evidence, OAI datestamps and the official announcement cadence"
    ),
    "raw_recovery_identities": len(rows),
    "public_batch_derived_consistent": len(date_consistent),
    "revision_route_reconciled": len(date_recovery),
    "candidate_denominator_provisional": len(retained),
    "candidate_owner_gaps": len(candidate_date_gaps),
    "pre_denominator_closures": len(closures),
    "withdrawn_excluded": len(withdrawn),
    "announcement_provenance": "../ARXIV_ANNOUNCEMENT_PROVENANCE.md",
    "identities": rows,
}
(ROOT / "screening-ledger-v3-author-repair.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

review_packet = []
for row in retained:
    arxiv_id = str(row["arxiv_id"])
    extract = extracts[arxiv_id]
    review_packet.append(
        {
            "arxiv_id": arxiv_id,
            "title": row["title"],
            "primary_evidence_version": f"arXiv:{arxiv_id}v1",
            "owner_evidence_status": row["owner_evidence_status"],
            "first_public_time_derived": row["first_public_time_derived"],
            "owner_evidence": row["owner_evidence"],
            "method": {"locator": extract["method_heading"], "evidence": extract["method_evidence"]},
            "evaluation": {"locator": extract["evaluation_heading"], "evidence": extract["evaluation_evidence"]},
            "limitations": {
                "locator": extract["limitations_heading"],
                "evidence": DIRECT_BOUNDARIES.get(arxiv_id, extract["limitations_evidence"]),
            },
            "claim_boundary": row["screening_reason"],
            "review_result": row["review_status"],
            "books_disposition": row["integration_disposition"],
            "owner_node": row["owner_node"],
        }
    )
(ROOT / "exact-v1-review-packet-v3-author-repair.json").write_text(
    json.dumps({"schema": "exact-v1-review-packet-v3-author-repair", "items": review_packet}, ensure_ascii=False, indent=2) + "\n"
)

coverage = old_report[old_report.index("## 2. 来源覆盖") : old_report.index("## 3. 候选与判断")]
coverage = re.sub(
    r"\| SRC-ARXIV \|.*?\|.*?\|.*?\|",
    (
        f"| SRC-ARXIV | 548 个去重 identity：按 arXiv ID-at-announcement、DataCite initial-created、"
        f"OAI datestamp 与官方公告节奏交叉确认；日期方法见 `../_sources/ARXIV_ANNOUNCEMENT_PROVENANCE.md` | "
        f"已检查 | {len(date_consistent)} 项完成批次推导，其中 {len(date_recovery)} 项以 revision-route reconciliation 处理；"
        f"08:00 是由 Wednesday 20:00 EDT 批次规则推导，不是 abstract page 披露的单篇 timestamp |"
    ),
    coverage,
)

lines = [
    "# Daily Research — 2026-05-07",
    "",
    "**规范：** V3",
    "**窗口：** 2026-05-06T09:00:00+08:00 ～ 2026-05-07T09:00:00+08:00",
    "**状态：** 进行中",
    "**Books：** 纳入本次",
    "**检查时间：** 2026-09-14T21:30:00+08:00",
    "",
    "## 1. 结论",
    "",
    f"本轮没有把旧 60 项直接当作既定候选，而是以 548 个 title + 完整摘要重新检查准入。作者侧暂定 {len(retained)} 个候选、{len(closures)} 个题摘关闭和 {len(withdrawn)} 个撤回排除。独立复核指出的共享过窄关闭族已经扩查：04055、04058、04061、04069、04261、04269、04312、04563、04698、04700、04711、04874、04893、04932、05003、05029、05092、05116 均恢复进入候选；04172 与 04450 则按实际 scope 保持关闭。",
    "",
    "所有暂定候选都重新打开 exact-v1 HTML，记录实际 Method、关键 evaluation 及论文直接披露的 limitation/discussion；不再用统一的‘未证明跨模型通用’句子冒充证据审阅。TSCG 的长期命题已纠正为 schema-to-token-efficient-text 的确定性编译、压缩与 tool selection，不再声称论文提供 validator 或 adapter correctness。",
    "",
    f"日期归属不再把 DataCite 或 OAI 单独称作官方 batch。依据 arXiv 官方 ID-at-announcement、exact-v1/version identity、DataCite initial-created 与 Wednesday 20:00 EDT 规则，全体 {len(date_consistent)} 项均可写 public-batch-derived 05-07 08:00；其中 {len(date_recovery)} 项 current OAI 已被后续 revision datestamp 覆盖，因此 OAI 只作 revision metadata，不反向否定初始批次。当前候选日期 gap 为 {len(candidate_date_gaps)}。作者稿保持进行中，等待非作者复核准入、证据与 Books 队列。",
    "",
    coverage.strip(),
    "",
    "## 3. 候选与判断",
    "",
    "下表是作者侧修复后的暂定分母。表内纯 ISO 时刻是由 arXiv ID/version identity、初始注册证据与官方公告节奏共同推导的 public-batch 时间，不是 abstract page 披露的单篇 timestamp；证据不齐的 family 明确写 `owner gap`。",
    "",
    "| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |",
    "| --- | --- | --- | --- | --- |",
]
for row in retained:
    score = row["score_v2"]
    chapter = row["owner_chapter"]
    decision = row["integration_disposition"]
    review = "深入完成" if row["review_status"] == "deep_complete" else "标准完成"
    public_time = (
        "2026-05-07T08:00:00+08:00"
        if row["owner_evidence_status"] == "public_batch_derived_consistent"
        else "2026-05-07（owner gap）"
    )
    lines.append(
        f'| [{row["title"]}](https://arxiv.org/html/{row["arxiv_id"]}v1) | {public_time} | '
        f'{row["screening_reason"]}；**{score["design_delta"]} + {score["system_reach"]} + {score["durability"]} = {score["total"]}** | '
        f'{review} | {decision}：`{row["owner_node"]}`，[章节]({chapter}) |'
    )

lines += ["", "## 4. 证据与知识整合", ""]
for row in retained:
    arxiv_id = str(row["arxiv_id"])
    extract = extracts[arxiv_id]
    score = row["score_v2"]
    lines += [
        f'### [{row["title"]}](https://arxiv.org/html/{arxiv_id}v1)',
        "",
        f'- **采用命题：** {row["screening_reason"]}',
        f'- **Method：** exact-v1 `{extract["method_heading"]}`；{extract["method_evidence"]}',
        f'- **Evaluation contract：** `{extract["evaluation_heading"]}`；{extract["evaluation_evidence"]}',
        f'- **直接限制 / non-proof：** `{extract["limitations_heading"]}`；{DIRECT_BOUNDARIES.get(arxiv_id, extract["limitations_evidence"])}',
        f'- **判断：** Score {score["total"]}/9，{row["integration_disposition"]}，owner `{row["owner_node"]}`。结论只限论文披露的模型、任务、数据、硬件和评价条件；章节中的工程外推必须另行标明。',
        "",
    ]

lines += [
    "## 5. 缺口与下一步",
    "",
    f"- {len(date_recovery)} 个 revision-route identity 已由初始 DataCite、arXiv ID/version identity 与官方批次规则完成归属；current OAI 后续日期仅作为 revision metadata 保存，不再误报为 owner gap。",
    "- 由 root 逐项裁决新恢复 family 的 Books 写回。共享 Books 本 lane 未修改；已有 33 项旧写回与 5 项新增写回须按当前 evidence boundary 复查，而不是只验 marker。",
    "- 对 2605.04450 保持关闭：原文是 generative recommender 的 EMB/KV 双缓存，不能仅凭系统类比变成 LLM serving 候选；若 Books 仍保留其 source marker，应由 root 判断是否改为其他 LLM 证据或移除该来源痕迹。",
    "- 2605.04172 保持关闭：它证明可编程 memory hierarchy 的 ISA/microarchitecture formal consistency，属于通用架构验证；未给出本项目当前大模型训练或推理路径的独立贡献。",
    "",
    "## 6. 复核",
    "",
    "复核者：待非作者独立复核。",
    "",
    "结论：未通过（作者侧修复已完成，Coverage membership、候选准入抽检和 Books 写回仍待复核）。",
    "",
    f'作者侧已核：548 个 owner identities、{len(retained)} 个暂定候选、{len(closures)} 个题摘关闭、1 个撤回排除；{len(retained)} 项 exact-v1 Method / evaluation / limitation 定点阅读。日期依据见 `../_sources/ARXIV_ANNOUNCEMENT_PROVENANCE.md`；过程材料见 `../_sources/daily-20260507/screening-ledger-v3-author-repair.json` 与 `../_sources/daily-20260507/exact-v1-review-packet-v3-author-repair.json`。',
    "",
]

REPORT.write_text("\n".join(lines))

recert = f"""# 2026-05-07 V3 作者侧修复 checkpoint

- 窗口：2026-05-06T09:00:00+08:00 ～ 2026-05-07T09:00:00+08:00
- 身份集合：548；按 arXiv ID-at-announcement、DataCite initial-created、OAI datestamp 与官方 announcement cadence 交叉归属。
- 可推导 05-07 08:00：{len(date_consistent)}；其中 revision-route reconciliation：{len(date_recovery)}；候选中的日期 gap：{len(candidate_date_gaps)}。
- 暂定候选：{len(retained)}
- 题摘关闭：{len(closures)}
- 撤回排除：1（2605.04356v1）
- exact-v1 HTML 定点审阅：{len(retained)}/{len(retained)}
- 状态：作者侧修复完成；报告继续 `进行中`，等待非作者复核与 root Books 裁决。

## 已修复

- 取消把 DataCite/OAI proxy 单独写成官方 batch；三证一致时才记录由 Wednesday 20:00 EDT 推导的北京时间 08:00，并明确它不是单篇页面 timestamp。
- 重开 reviewer 指出的共享错误关闭族，并扩查同类理由。
- TSCG 改为 deterministic schema-to-token-efficient-text compilation / compression / tool selection，不再写 validator/adapters。
- 每项候选使用实际 Method、evaluation、limitation/discussion 内容，移除统一 non-proof 模板。
- Ch28 BAOC 与 Ch84 Design Conductor 的 Books 边界由 root 修复；日报采用命题已同步为 optimizer-state budget allocation 与论文证据/工程推论分离。

## 待处理

- 非作者检查 revision-route reconciliation 是否错误解释 current OAI 的后续 datestamp。
- 非作者全候选准入与证据复核、分层 closure 抽检。
- root 对新恢复候选的 Books writeback / reversal 决策，以及 33 处旧 Integrate 的具体正文复核。
"""
(ROOT / "V3_RECERTIFICATION.md").write_text(recert)

print(json.dumps({"raw": len(rows), "retained": len(retained), "closures": len(closures), "withdrawn": len(withdrawn)}, ensure_ascii=False))
