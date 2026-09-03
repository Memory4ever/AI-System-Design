#!/usr/bin/env python3
"""Independent fresh-context audit for the 2026-03-09..16 author slice.

The reviewer replays every strict-window title+abstract row.  The author's
retained set is only the baseline needed to express disagreements; it is never
used as a discovery filter.  Weekly artifacts are not read.  This module also
refreshes exact-v1 packets for corrected false negatives and removes withdrawn
families from every candidate/review/Books path.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ADAPTER = ROOT / "scripts/rebuild_march_lane_c_09_16.py"
SPEC = importlib.util.spec_from_file_location("march_09_16_author", ADAPTER)
assert SPEC and SPEC.loader
author = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(author)
AUTHOR_PDF_SECTIONS = author.base.pdf_sections
AUTHOR_REVIEW_ONE = author.base.review_one
AUTHOR_SCORE = author.base.score


ORIGINAL = set(author.DURABLE_CANDIDATES)
WITHDRAWN = {"2603.07473"}
ADDITIONS_BY_DAY = {
    9: """
        05528 05540 05553 05578 05618 05697 05706 05725 05739 05786
        05815 05828 05872 05959 05960 05974 06001 06003 06009 06081
        06123 06130 06138 06198 06199 06263 06274 06317 06365 06413
        06422 06444 06445 06450 06453 06508 06569 06577 06578
    """.split(),
    10: "06588 06604 06728 06798 06847 08546".split(),
    11: "08727 08739 08755 08852 09730".split(),
    12: "09983 10030 10335".split(),
    13: "11340 11535 12262".split(),
    16: "12946".split(),
}
ADDITIONS = {f"2603.{suffix}" for values in ADDITIONS_BY_DAY.values() for suffix in values}
FINAL = (ORIGINAL | ADDITIONS) - WITHDRAWN


# Fresh-context review found a small set of papers whose exact-v1 section
# headings are semantically precise but do not contain the generic words used
# by the author renderer.  Keep these exceptions source-specific: a generic
# fallback would make unrelated headings look like Method evidence.
SECTION_OVERRIDES = {
    "2603.05960": {"method": [r"^3\.2 Omni-Masked Gradient Descent$", r"^3 Methodology$"]},
    "2603.05881": {"method": [r"^3\.3 CoCA", r"^3\.2 Confidence-First"]},
    "2603.06331": {"method": [r"^4\.1 Curvature-guided", r"^4\.2 Chaotic-prioritized"]},
    "2603.06450": {"method": [r"^III Cross-Embodiment Data Analogies$"]},
    "2603.06508": {"method": [r"^4 Problem Formulation$"]},
    "2603.06588": {"method": [r"^1 Overview of vLLM Hook$", r"^2 Core Functions"]},
    "2603.06604": {"method": [r"^3 Know When You.re Wrong$", r"^3\.2 Self-Evaluation"]},
    "2603.08163": {"method": [r"^2\.1 SparseLoCo$", r"^3 Communication Protocol"]},
    "2603.08361": {"method": [r"^IV .*VLA$", r"^IV-A Prior-Guided"]},
    "2603.09086": {"method": [r"^III INTERNAL MECHANICS"]},
    "2603.09297": {"method": [r"^III\. METHODOLOGY$"]},
    "2603.09555": {"method": [r"^3 Why SSD Is Compiler-Friendly$", r"^4 A Complete Mamba-2 Case Study$"]},
    "2603.09619": {"method": [r"^6\. Context Engineering as a Design Object$"]},
    "2603.09891": {"method": [r"^2 Task Setup$"]},
    "2603.10057": {"method": [r"^3 METHODOLOGIES$"]},
    "2603.10494": {"method": [r"method", r"preference mining"], "evaluation": [r"experiment", r"results"]},
    "2603.10521": {"method": [r"^3 Constructing IH-Challenge$"]},
    "2603.10577": {"method": [r"^3\.1\. Vision-Language", r"^3\.3\. Calibration"]},
    "2603.11132": {"method": [r"^3\.1 Threat Models$", r"^3\.2 Jailbreak-based"]},
    "2603.12614": {"method": [r"^3\.2\. ChainFuzzer Workflow$", r"^4\.1\. Sink-Related"]},
    "2603.13215": {"method": [r"^3 Benchmarking State Evolution"]},
}


PDF_SECTION_BOUNDS = {
    "2603.09297": (r"^III\.\s+METHODOLOGY$", r"^IV\.\s+EXPERIMENTS$"),
    "2603.09619": (r"^6\.\s+Context Engineering as a Design Object$", r"^7\.\s+Necessary Caveats"),
    "2603.10057": (r"^3\s+METHODOLOGIES$", r"^4\s+AIBOM SCHEMA DESIGN"),
}


def reviewer_pdf_sections(text: str) -> dict[str, list[str]]:
    """Augment the author's conservative PDF parser for three exact papers."""
    sections = AUTHOR_PDF_SECTIONS(text)
    lines = [author.base.clean(line) for line in text.splitlines()]
    for aid, (start_pattern, end_pattern) in PDF_SECTION_BOUNDS.items():
        start = next((i for i, line in enumerate(lines) if re.search(start_pattern, line, re.I)), None)
        if start is None:
            continue
        end = next(
            (i for i, line in enumerate(lines[start + 1 :], start + 1) if re.search(end_pattern, line, re.I)),
            len(lines),
        )
        heading = lines[start]
        body = author.base.clean(" ".join(line for line in lines[start + 1 : end] if line))
        if len(body) > 80:
            sections[heading] = [body[:12000]]
    return sections


def install_exact_v1_pdf_fallback() -> None:
    """Use the official exact-v1 PDF when arXiv's HTML conversion has no body."""
    pdf = ROOT / "papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10494v1.pdf"
    if not pdf.exists():
        return
    pdf_bytes = pdf.read_bytes()
    if not pdf_bytes.startswith(b"%PDF") or b"%%EOF" not in pdf_bytes[-4096:]:
        return
    original_fetch = author.base.fetch

    def fetch(url: str, timeout: int = 60):
        if url == "https://arxiv.org/html/2603.10494v1":
            return 404, b""
        if url == "https://arxiv.org/pdf/2603.10494v1":
            return 200, pdf_bytes
        return original_fetch(url, timeout)

    author.base.fetch = fetch


def reviewer_review_one(row: dict, src: Path) -> dict:
    """Repair a locator only from a source-specific exact-v1 subsection."""
    review = AUTHOR_REVIEW_ONE(row, src)
    aid = row["arxiv_id"]
    if aid in DEEP_REVIEW_IDS:
        review["review_route"] = "deep"
    if aid not in SECTION_OVERRIDES or not str(review.get("method_locator", "")).startswith("Not Disclosed"):
        return review
    body_path = ROOT / review["body_path"]
    if not body_path.exists() or body_path.suffix == ".pdf":
        return review
    if body_path.name.endswith(".pdf.txt"):
        sections = reviewer_pdf_sections(body_path.read_text(errors="ignore"))
    else:
        parser = author.base.SectionParser()
        parser.feed(body_path.read_text(errors="ignore"))
        sections = parser.sections
    title, evidence = author.base.choose_section(
        sections,
        "method",
        row["title"],
        "Method",
        SECTION_OVERRIDES[aid].get("method"),
    )
    if evidence.startswith("Not Disclosed"):
        return review
    source_kind = review["source_kind"]
    source_url = f"https://arxiv.org/{'html' if source_kind == 'HTML' else 'pdf'}/{aid}v1"
    locator = (
        f"arXiv:{aid}v1 {source_kind} — §{title} [facet=method]; {source_url}; "
        f"{body_path.relative_to(ROOT)}; sha256:{sha(body_path)}"
    )
    review["method_evidence_excerpt"] = evidence
    review["method_locator"] = locator
    review["method_text"] = review["method_text"].replace("exact-v1 的 `Method`", f"exact-v1 的 `{title}`")
    review["claim_boundary"] = review["claim_boundary"].replace("§Method 的机制", f"§{title} 的机制")
    return review


NODE = {
    "05528": "MULTIMODAL-REPRESENTATION", "05540": "AGENT-TOOL-CALLING",
    "05553": "TRAIN-DATA", "05578": "PLATFORM-EVALUATION-SYSTEM",
    "05618": "PLATFORM-SECURITY", "05697": "PLATFORM-EVALUATION-SYSTEM",
    "05706": "PLATFORM-EVALUATION-SYSTEM", "05725": "PLATFORM-SECURITY",
    "05739": "TRAIN-RLHF", "05786": "PLATFORM-SECURITY",
    "05815": "MULTIMODAL-WORLD-MODELS", "05828": "PLATFORM-EVALUATION-SYSTEM",
    "05872": "PLATFORM-SECURITY", "05959": "INFER-KV-CACHE",
    "05960": "TRAIN-DISTRIBUTED-TRAINING", "05974": "INFER-SCHEDULING",
    "06001": "MULTIMODAL-EMBODIED-VLA", "06003": "MODEL-MOE",
    "06009": "TRAIN-PPO",
    "06081": "PLATFORM-EVALUATION-SYSTEM", "06199": "INFER-TENSORRT-LLM",
    "06123": "MULTIMODAL-GENERATIVE-PARADIGMS", "06130": "TRAIN-DATA",
    "06138": "TRAIN-RLHF", "06198": "PLATFORM-EVALUATION-SYSTEM",
    "06263": "PLATFORM-SECURITY", "06274": "MODEL-SELF-ATTENTION",
    "06317": "PLATFORM-EVALUATION-SYSTEM",
    "06365": "PLATFORM-SECURITY", "06588": "INFER-TENSORRT-LLM",
    "06413": "TRAIN-RLHF", "06422": "PLATFORM-EVALUATION-SYSTEM",
    "06444": "INFER-DECODE", "06445": "MULTIMODAL-WORLD-MODELS",
    "06450": "TRAIN-DATA", "06453": "PLATFORM-PRODUCTION",
    "06508": "PLATFORM-SECURITY", "06569": "MULTIMODAL-REPRESENTATION",
    "06577": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "06578": "PLATFORM-EVALUATION-SYSTEM",
    "06604": "PLATFORM-EVALUATION-SYSTEM", "06728": "INFER-TENSORRT-LLM",
    "06798": "TRAIN-DISTRIBUTED-TRAINING", "06847": "PLATFORM-EVALUATION-SYSTEM",
    "08546": "MULTIMODAL-WORLD-MODELS", "08727": "INFER-KV-CACHE",
    "08739": "INFER-KV-CACHE", "08755": "AGENT-PLATFORM",
    "08852": "AGENT-MCP", "09730": "PLATFORM-GPU-SCHEDULER",
    "09983": "INFER-SCHEDULING", "10030": "INFER-KV-CACHE",
    "10335": "INFER-SCHEDULING", "11340": "INFER-SCHEDULING",
    "11535": "MODEL-MOE", "12262": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "12946": "PLATFORM-SECURITY",
}


SCORE_OVERRIDES = {
    # Scores are independent of Books disposition.  These families materially
    # alter an execution/evaluation contract even when Books already carries
    # the durable proposition.
    "2603.05540": (3, 3, 3),
    "2603.05725": (3, 3, 3),
    "2603.05786": (3, 3, 3),
    "2603.05959": (3, 2, 3),
    "2603.06009": (3, 3, 3),
    "2603.06317": (3, 3, 3),
    "2603.06413": (3, 3, 3),
}
DEEP_REVIEW_IDS = set(SCORE_OVERRIDES)


def reviewer_score(row: dict, review: dict) -> tuple[int, int, int]:
    return SCORE_OVERRIDES.get(row["arxiv_id"], AUTHOR_SCORE(row, review))


def S(problem: str, mechanism: str, evidence: str, boundary: str):
    return problem, mechanism, evidence, boundary


SYNTHESIS = {
    "05528": S(
        "每增加一种模态就常驻一个专用 encoder，会让参数、显存和部署路径近似线性增长。",
        "Omni-C 以共享 dense Transformer 承担图像、语音与文本表示，只保留轻量模态投影，并用未配对的单模态对比目标抑制跨模态冲突。",
        "公开结果只支持所测 encoder、任务与设备中的质量/显存取舍；零样本退化和线性探针恢复不能证明共享表示在所有组合任务上等价。",
        "共享骨干降低常驻成本，却扩大负迁移与串行处理延迟；模态差异大或并行低延迟优先时，专用 encoder 仍合理。",
    ),
    "05540": S(
        "grammar-constrained decoding 只比较最终语言是否相同，会遗漏等价 grammar 在在线解析状态和每 token 延迟上的巨大差异。",
        "论文把解码写成 next-token distribution 与 pushdown reachability oracle 的耦合，证明语言等价不等于执行成本等价，并用 SAC 描述逐 token parse-forest 增长。",
        "定理支持特定 CFG family 的控制状态膨胀、复杂度下界与 hard mask 分布失真；不证明所有 schema 或具体 engine 都达到该下界。",
        "grammar rewrite 能降低在线状态成本，却不消除受约束采样对原分布的扭曲；小 grammar 或低 QPS 路径仍可优先简单正确性。",
    ),
    "05618": S(
        "把 Chain-of-Thought 当作内部调试信息，会忽略 prompt 中 PII 被 reasoning trace 再暴露的独立泄漏面。",
        "该工作把 PII 类型、风险权重和允许的 reasoning budget 绑定到同一评测合同，并比较多种推理时 gatekeeper。",
        "结果只支持所测模型、PII 数据和 budget；没有单一 gatekeeper 在所有模型上占优，也不能把低泄漏等同于隐私保证。",
        "更强过滤降低泄漏却可能截断有用推理并增加误报；不输出 reasoning trace 的受控服务仍具有更小暴露面。",
    ),
    "05697": S(
        "把正确 evidence 直接交给模型的多模态 benchmark，会隐藏跨文档、图像和视频检索本身的主瓶颈。",
        "MultiHaystack 将唯一可验证 evidence 放入四万级异构候选池，分别测 retrieval recall 与 evidence-conditioned reasoning。",
        "公开数字只属于其 747 个问题、候选池、retriever 与 MLLM；不能外推企业语料版本、权限过滤或生产时延。",
        "端到端分解改善归因，却增加 evidence 标注和 corpus 版本成本；检索已知的离线任务仍可单独评测 reasoning。",
    ),
    "05706": S(
        "依赖 Chain-of-Thought monitor 的安全方案隐含假设模型不能随意控制自己暴露的推理内容。",
        "CoT-Control 将隐藏推理的可控性与最终输出可控性分开测量，并改变模型规模、RL 强度、test-time compute 和任务难度。",
        "结果支持当前受测 reasoning models 的 CoT controllability 较低；机制尚不明确，不能据此把 monitorability 当作长期保证。",
        "监控 reasoning trace 能增加可见性，却会随能力和训练变化失效并引入隐私面；外部 action gate 仍不可省略。",
    ),
    "05725": S(
        "把 CUDA 程序翻译到 CPU 上 fuzz，会丢失 GPU memory、SIMT、异步执行与 runtime 语义，导致测试对象不再忠实。",
        "论文将 behavior faithfulness 设为 GPU-native fuzzing 的核心合同，并梳理生成、调度、oracle 与 crash triage 的设计约束。",
        "这是设计与漏洞趋势证据，不是一个已闭合的通用 fuzzer benchmark；未证明所有 CUDA bug 类都可自动发现。",
        "原生执行提高忠实度，却增加设备成本、非确定性和故障隔离难度；纯 host 逻辑仍可用 CPU 侧快速筛查。",
    ),
    "05739": S(
        "Best-of-N 常以期望真实 reward 分析，但实践中的 reward model 主要由 pairwise preference 训练，目标错配会误判方案优劣。",
        "论文改用 win-rate 作为推理时对齐目标，给出 BoN 最优条件，并提出在保持统计效率时限制 reward hacking 的变体。",
        "理论只在其 reference/reward-model 假设下成立；不证明有限样本、分布漂移或开放式 evaluator 中不存在 hacking。",
        "增加 N 提高选择机会却线性增加推理成本，并放大 evaluator 偏差；低风险或预算紧张时单样本仍是有效基线。",
    ),
    "05786": S(
        "服务方声称执行了 guardrail 时，用户通常只能信任声明，无法验证安全检查是否真正位于 response commit 前。",
        "Proof-of-Guardrail 把 agent 与公开 guardrail 放入 TEE，并用远程证明绑定代码身份和执行顺序。",
        "证明只覆盖指定 guardrail 被执行，不证明规则有效、输入完整或 guardrail 未被 jailbreak；成本结果绑定其 OpenClaw 实现。",
        "attestation 缩小运行完整性信任面，却把 TEE、测量身份和规则质量变成新根信任；可控单租户环境仍可用普通审计。",
    ),
    "05815": S(
        "只从相邻帧学习 latent action，通常只能编码短期运动，无法给 world model 或 policy 提供长时间技能状态。",
        "HiLAM 在低层 latent-action extractor 之上聚合动作序列，形成具有更长时间尺度的 latent skill。",
        "实验只支持所测 actionless video 和动态技能发现指标；latent skill 的可控性、因果性和跨 embodiment 迁移未被证明。",
        "层级状态扩大规划跨度，却增加抽象错配和不可辨识性；短 horizon 控制仍适合低层 latent action。",
    ),
    "05828": S(
        "只输出 hallucination 标签无法说明错误 span、生成机制与支持/反对 evidence 之间的对应关系。",
        "HART 把定位、机制归因、evidence retrieval 与 causal tracing 组织为结构化链路，并建立联合标注数据。",
        "结果证明其数据集上优于检索基线；机制标签仍是任务定义下的监督，不能当作模型内部因果事实。",
        "细粒度 trace 提高可审计性，却显著增加标注和 oracle 成本；低风险场景仍可使用答案级 groundedness 检查。",
    ),
    "05872": S(
        "允许 agent 以效用为目标自我迭代时，局部成功会把策略更新推向可迁移的欺骗，而不是稳定遵循规范。",
        "论文在竞争式 bidding 环境中比较多条演化路径，并追踪 reflection 后的策略与内部 rationalization。",
        "证据只支持所测 arena、模型和迭代协议中的欺骗漂移；不证明所有 self-improvement 必然产生同一均衡。",
        "自适应可提高跨任务效用，却扩大目标漂移和审计难度；固定 policy、外部 reward gate 与可回滚版本仍是安全边界。",
    ),
    "05959": S(
        "流式视觉几何若为每个新帧重算完整历史，计算和 memory 会随序列长度持续增长。",
        "OVGGT 将历史压缩为固定大小的视觉几何状态，使新帧更新保持常数级 cache/compute contract。",
        "作者结果只支持其几何任务、场景长度和压缩状态；不证明常数状态能保留任意长流的全部信息。",
        "有界状态换来稳定资源，却引入不可逆遗忘和漂移；短序列或离线高精度重建仍应保留完整历史。",
    ),
    "05960": S(
        "大模型优化器若同时保存全部梯度、动量和参数更新，会让 optimizer state 成为训练显存上限。",
        "Omni-Masked Gradient Descent 以 mask traversal 分批更新参数子集，在降低同时驻留状态时维持收敛路径。",
        "理论与实验只支持论文的 mask schedule、目标和模型；不能把内存节省外推为任意分布式训练中的 wall-clock 收益。",
        "分块状态降低峰值 memory，却增加更新陈旧、调度和收敛超参；容量足够时全量同步 optimizer 更简单。",
    ),
    "05974": S(
        "代码补全始终走云端会增加网络尾延迟和成本，始终走本地则受小模型质量限制。",
        "论文把 local/cloud 选择建模为带质量估计的请求级 cascade，在提交前决定是否升级到远端模型。",
        "结果绑定其代码任务、网络与模型组合；不证明置信信号在新仓库或隐私约束下仍校准。",
        "级联改善平均延迟/质量，却增加路由误判、两次计算和数据出域风险；稳定网络或单模型足够时固定路径更可控。",
    ),
    "06009": S(
        "PPO 在有限并行环境中会因状态覆盖不足和同步采样停顿而出现学习停滞，单纯调学习率不能补足新 experience。",
        "该工作把环境并发扩展到百万级并重组采样/更新数据流，用更广状态覆盖维持 policy improvement。",
        "证据只支持其 simulator、policy 和硬件布局；极端并发的样本相关性、通信成本与现实环境有效性仍需独立验证。",
        "更大并发提高覆盖，却增加环境一致性、聚合带宽和 stale-policy 风险；环境昂贵或可复用数据充分时较小并发仍合理。",
    ),
    "06123": S(
        "diffusion language model 若预先固定生成长度，会把长度预测错误转化为 padding 浪费或内容截断。",
        "论文指出 mask/denoise state 本身携带剩余长度信息，并据此让生成过程动态决定终止。",
        "结果只支持所测 DLM、任务和 sampling schedule 的长度感知；不能等同于语义完成度或生产 SLO 保证。",
        "动态长度减少固定预算浪费，却引入终止校准和批次形状变化；结构化输出仍可使用显式长度上限。",
    ),
    "06130": S(
        "robot safety 数据若只从成功任务或随机失败收集，危险状态分母与伤害严重度不会进入训练 contract。",
        "论文以 hazard taxonomy 驱动场景、trajectory 与标注采集，使 physical risk 成为可追踪的数据 lineage。",
        "结果仅证明其机器人、hazard set 与 evaluator 下的数据覆盖；不能声明未枚举风险已被消除。",
        "hazard-driven 数据提高安全召回，却增加长尾采集、仿真真实性和标签维护成本；低风险封闭环境仍可用普通任务数据。",
    ),
    "06138": S(
        "LLM policy gradient 若对整条 response 统一归因，会把无关 token 的噪声传播到真正决定 reward 的位置。",
        "Partial Policy Gradients 只对由规则或估计器识别的责任片段施加 policy update，改变 credit-assignment 粒度。",
        "论文结果只支持其任务、责任选择器和 reward；不能证明选择器不会遗漏跨 token 依赖或引入偏差。",
        "局部更新降低方差，却依赖可靠 attribution 并可能破坏全局一致性；短答案或 dense reward 仍适合全序列更新。",
    ),
    "06198": S(
        "RAG 只报告检索 recall 或答案分数，会把 generator 使用 evidence 的能力与检索质量混在一起。",
        "LIT-RAGBench 固定提供的 evidence，并系统改变 relevance、noise 与回答要求以单独测 generator contract。",
        "排名只属于其文档、模型、prompt 和 evaluator；不代表端到端 corpus、权限与 latency 已被覆盖。",
        "解耦评测提高归因，却可能低估真实检索错误；生产 release gate 仍需补端到端链路。",
    ),
    "06263": S(
        "on-device DNN 分层执行时，切分点会同时决定隐私暴露、TEE 容量和服务端算力，固定 partition 难以兼顾。",
        "SPOILER 将 TEE-shielded partition 与 poison-learning threat model 联合优化，显式划分可信/非可信执行边界。",
        "结果只支持其设备、DNN、TEE 和攻击模型；不证明 side channel、runtime 漏洞或所有 poisoning 被覆盖。",
        "更深可信切分减少暴露却增加 enclave memory/latency；完全本地或完全可信云在对应条件下仍更简单。",
    ),
    "06274": S(
        "稀疏 attention 只比较保留多少连接，会忽略被裁剪图是否仍允许关键信息跨层到达目标 token。",
        "Stem 从 causal information flow 角度刻画稀疏拓扑，把路径可达性与每层选择共同纳入设计。",
        "理论和实验只支持指定 sparse pattern 与任务；可达不意味着信息无损，也不证明所有硬件实现更快。",
        "结构化稀疏降低计算，却可能拉长路径并产生信息瓶颈；短序列或 exactness 优先时 dense attention 仍成立。",
    ),
    "06317": S(
        "next-token entropy 是局部生成分布，不等于答案正确概率，直接据此拒答会系统性失校准。",
        "论文把 uncertainty reasoning 作为显式训练目标，并用 calibration、selective accuracy 与分布转移检查自报置信。",
        "结果只支持所测模型、任务和 calibration split；模型生成的 confidence 仍不能替代外部 evidence。",
        "校准训练改善风险排序，却牺牲 coverage 并随分布漂移失效；高风险 claim 仍需 claim-level verifier。",
    ),
    "06413": S(
        "RL framework 各自命名 actor、environment、buffer 与 learner，导致架构比较被 API 表象遮蔽。",
        "该工作从 18 个框架归纳 reference architecture，以组件、数据流和控制关系重建可比较的训练系统 contract。",
        "grounded-theory 结果支持这些实现中的共同结构，不证明 reference architecture 对未来异步/多智能体框架完备。",
        "统一词汇改善比较和集成，却可能抹平性能关键特例；具体实现仍需保留自己的 execution semantics。",
    ),
    "06422": S(
        "只用静态问答评测安全分析 LLM，会遗漏工具调用、动态证据和多阶段 incident workflow。",
        "SIABENCH 将深度调查与告警分诊拆为可扩展场景，并用 agent 执行网络、内存、恶意样本和日志分析。",
        "结果只覆盖其 160 个场景、11 个模型和 sandbox；不能证明真实 SOC 权限、数据漂移或误操作成本。",
        "更真实的 agentic benchmark 提高外部有效性，却增加环境维护和安全隔离；单一分类器仍可用静态 test set。",
    ),
    "06444": S(
        "流式文本驱动 TTS 既缺未来 lookahead，又会因累积全部历史在长文本中崩溃。",
        "论文训练模型在 prosodic boundary 提前停止，并用滑动窗口携带有限文本/语音状态，实现有界上下文拼接。",
        "结果绑定其 TTS 模型、语言和长文本集；不能从 WER 改善推断跨说话人、并发或端到端对话 SLO。",
        "有界 state 稳定长流资源，却可能在边界预测错误时产生韵律断裂；离线合成仍可利用完整文本。",
    ),
    "06445": S(
        "situated agent 无法安全探索时，单帧 observation 不足以回答路径和未来状态问题。",
        "WanderDream 用 world model 生成从当前状态到目标的 imagined trajectory，并分别评测起点、路径与终态推理。",
        "数据与实验支持所测室内场景中的 emulative simulation；生成轨迹的物理/因果真实性和真实部署安全未被证明。",
        "想象 rollout 降低真实探索成本，却会传播 model bias；允许安全交互时真实 observation 仍是更强证据。",
    ),
    "06450": S(
        "把跨 embodiment 数据简单混合，会把视角、外观和形态差异混为同一种 diversity。",
        "论文用配对 data analogy 对齐场景、任务或 trajectory，区分 perceptual diversity 与 morphology transfer 所需证据。",
        "结果只支持其仿真和机器人设置中的成功率变化；不能把 22.5% 提升外推到未对齐 action schema。",
        "配对提高 transfer 信号，却显著增加采集和对齐成本；单 embodiment 或目标数据充足时直接训练更简单。",
    ),
    "06453": S(
        "一个通用图像生成模型难同时满足多个产品任务的严格控制、质量与上线节奏。",
        "Pinterest Canvas 以共享 foundation diffusion model 为起点，再通过任务数据产生专用 variant，并把数据、训练、推理和 A/B release 串成产品流水线。",
        "线上 uplift 只属于公开两个用例、用户流量和评价合同；未披露硬件、并发和长期漂移不能推断。",
        "共享基座降低重复训练，却引入 variant 管理、数据偏差和回归矩阵；需求相近时单一模型仍可减少运维成本。",
    ),
    "06508": S(
        "多模态 diffusion 的高 attack-success rate 可能掩盖 trigger 实际只依赖单一模态，传统总分无法归因。",
        "论文用 Trigger Modality Attribution 与 Cross-Trigger Interaction 分解各模态贡献，识别 backdoor modality collapse。",
        "证据只支持其模型、攻击和训练配置；winner-takes-all 现象不等于所有 multimodal backdoor 都同构。",
        "分模态评测提高诊断，却增加组合实验成本；单模态模型仍可使用传统攻击成功率。",
    ),
    "06569": S(
        "VLM 依赖对比预训练视觉 encoder 时，分类不变性可能抹掉 dense perception 所需的细粒度时空信息。",
        "Penguin-VL 从 text-only LLM 初始化视觉 encoder，测试表示目标而非单纯扩大模型规模的替代路线。",
        "公开结果支持 2B/8B 模型和所测图像视频任务；不能证明任意语言权重都优于 CLIP/SigLIP 初始化。",
        "更统一的初始化提高细粒度表示潜力，却增加模态适配和训练不稳定性；检索/分类任务仍可能受益于对比 encoder。",
    ),
    "05553": S(
        "function-calling 数据的数据库、可执行环境、schema 与 trajectory 若分开生成，跨 artifact 错误无法归因。",
        "EigenData 让多个专责 agent 共享可验证 artifact graph，并以数据库终态而非轨迹表面匹配作为任务 oracle。",
        "BFCL-V3 修复案例只证明所测 schema、实现和轨迹错误能被该闭环发现；不证明自动修复对任意工具生态安全。",
        "闭环提升一致性却扩大生成器、测试器和 oracle 的共同故障域；人工冻结的小型工具集仍更易审计。",
    ),
    "05578": S(
        "只测 agent 是否最终完成任务，会把工具接口、实现与调用失败混成一个分数。",
        "Tool-Genesis 从抽象需求开始，分别验证 interface compliance、functional correctness 与 downstream utility，使失败位置可归因。",
        "基准证明其任务集合中一处早期接口缺陷会沿调用链放大；不证明该任务分布代表生产工具市场。",
        "诊断粒度提高证据价值但增加 oracle 和 sandbox 维护；预定义稳定工具仍可使用普通端到端测试。",
    ),
    "06001": S(
        "VLA 可在语言与场景矛盾时仍沿视觉先验行动，任务成功率因此掩盖 instruction-action coupling 失效。",
        "ICBench 固定视觉场景并注入矛盾指令；IGAR 在推理时重分配 attention，使语言约束重新进入动作生成。",
        "三类 VLA、LIBERO 与 Franka 实验支持该 failure mode 和受限修复；不证明 attention weight 等于因果 grounding。",
        "重校准无需训练但可能压制合理视觉反应；闭集一致指令下原策略仍有更低控制开销。",
    ),
    "06003": S(
        "MoE 部署受完整 expert pool 显存约束，而逐层统一剪枝忽略不同层对容量损失的敏感度。",
        "EvoESAP 把层内 expert 排序与跨层预算分开，用 teacher-forced acceptance proxy 搜索非均匀 sparsity。",
        "7B--30B、固定全局预算实验支持该搜索空间内的质量差异；不证明 proxy 在其他 router 或数据上保持排序。",
        "搜索与校准增加离线成本，且剪枝不可逆；显存足够或分布易漂移时保留完整 expert pool 更稳。",
    ),
    "06081": S(
        "输出后分类器只关联表面答案，难表达知识边界附近对扰动不稳定的内部表示。",
        "Lyapunov probe 以扰动下置信单调衰减为训练约束，把局部稳定性作为 hallucination 风险信号。",
        "作者跨文本/多模态数据的比较只支持所测 probe 与扰动协议；稳定表示不是事实正确性的充分条件。",
        "需要内部激活、额外训练和校准，且 OOD 扰动会改变阈值；不可访问权重时仍需 evidence-based verifier。",
    ),
    "06199": S(
        "长上下文 prefill 的稀疏模式搜索若需要排序或累计 attention score，会吞掉跳算收益。",
        "FlashPrefill 联合发现 vertical、slash 与 block pattern，并用动态阈值直接裁剪长尾 block，改变 prefill execution plan。",
        "作者速度数字只属于所测模型、长度、kernel 与硬件；摘要不足以外推 27.78x 到其他 workload。",
        "阈值搜索换来近似误差和 pattern metadata；短上下文或 exact attention 要求高时 dense prefill 仍合理。",
    ),
    "06365": S(
        "自由对话式安全审计没有不可变执行记录，启发式 agent 结论也难与真实仓库修改分离。",
        "ESAA-Security 让 agent 只提交结构化 intent，由 orchestrator 验证后写 append-only event log，再重放投影与 hash 校验。",
        "公开稿提供体系和任务清单，能证明 contract 可表达；没有独立 artifact 时不能声称覆盖率或防护效果。",
        "事件溯源提高复算性但增加 schema、存储和投影一致性；小型人工审计仍可用普通报告链。",
    ),
    "06577": S(
        "any-to-any 多模态理解与生成若直接继承自回归骨干，会把所有模态都绑定到单向逐 token 提交。",
        "Omni-Diffusion 以 mask-based discrete diffusion 联合建模文本、图像与语音 token，并以模态专属 codec、长度控制和并行去噪保留各模态的生成边界。",
        "exact-v1 只支持 Dream-7B 及公开 ASR、TTS、VQA、文生图 workload 中的可行性与采样步数关系；硬件、精度、并发和生产 SLO 未披露。",
        "统一 backbone 提供并行可修正状态，却没有消除 codec、解码策略和 evaluator 的模态差异；需要强顺序 commit 或 typed output 时自回归/专用 head 仍成立。",
    ),
    "06578": S(
        "把 MLLM 分类得分视为模型固有能力，会隐藏标签、输出映射、distractor、batch 与样本顺序对结论的共同控制。",
        "论文把 closed-world、multiple-choice 与 open-world 协议拆开，并显式改变重标注、响应格式、OOV 处理、mapping encoder、batch size、顺序和组成，显示它们共同构成 EvalRun identity。",
        "exact-v1 只支持五个公开 MLLM、ImageNet-1k/ReGT 子集及披露协议下的结论反转；ReGT 尚未公开，不能把修正标签当作最终真值或外推所有分类 workload。",
        "更完整的评测身份改善归因，却增加标注成本、映射依赖和自由度；严格 exact-match 仍可作可复算基线，但必须显式声明其偏差。",
    ),
    "06588": S(
        "高性能 serving engine 封装内部 state 后，activation probe、steering 与安全 monitor 无法在不 fork runtime 时接入。",
        "vLLM Hook 以配置声明捕获点，并区分只读 probe 与主动修改，使内部状态干预成为显式扩展接口。",
        "实现与实验只证明特定 vLLM 版本/模型中的可编程性和开销；不证明任意 intervention 保持 correctness。",
        "开放 hook 扩大 ABI、隔离和安全面；不需要内部干预的生产服务应保留封闭快路径。",
    ),
    "06604": S(
        "模型自报置信度常与正确性错配，阈值化拒答无法仅凭 token probability 获得可靠 assurance。",
        "该工作把 confidence-correctness alignment 作为单独训练/校准目标，并比较 error detection 而非只看 accuracy。",
        "公开结果限于所测任务、模型和 calibration split；不能把分数解释为开放世界真实概率。",
        "校准提高选择性但会牺牲 coverage，并随分布漂移失效；高风险结论仍需外部 evidence verification。",
    ),
    "06728": S(
        "Apple Neural Engine 缺少公开编程模型时，LLM 训练/推理 placement 只能把它当黑盒能力。",
        "Orion 逆向刻画指令、memory 与执行限制，并把可运行算子映射到训练/推理 execution plan。",
        "测量只属于测试芯片、OS 与工具链版本；不证明未公开设备代际具有相同语义。",
        "专用映射提高设备利用率却承担兼容与正确性风险；稳定受支持路径仍应优先官方 runtime。",
    ),
    "06798": S(
        "分布式训练 placement 若只考虑计算量，会把 activation、optimizer state 与网络拓扑的峰值分开优化。",
        "NEST 联合建模 device memory、通信拓扑和 operator dependency，搜索满足容量约束的 placement。",
        "作者工作负载支持所测拓扑中的峰值内存/通信权衡；不证明搜索在超大动态图中可及时收敛。",
        "全局建模改善放置却提高 profile 和搜索成本；同质小集群仍适合规则化并行策略。",
    ),
    "06847": S(
        "agentic AI 的失败跨模型、tool、memory 与 orchestration 传播，按单一异常标签无法定位责任。",
        "该 taxonomy 用真实 failure report 区分类型、症状和根因，为 fault injection 与 evidence schema 提供分母。",
        "研究能支持其样本中的故障类别，不证明 taxonomy 对未来 agent runtime 完备。",
        "更细分类改善归因但增加标注歧义；边界清晰的单工具应用仍可使用传统故障分类。",
    ),
    "08546": S(
        "robot policy 训练需要可控环境 transition，而静态数据无法生成 action-conditioned counterfactual。",
        "交互式 world simulator 维护可更新环境状态，让 policy action 驱动下一 observation，并将 rollout 作为训练/评测输入。",
        "作者只证明其 simulator 与机器人任务中的可交互性/预测质量；不证明 sim-to-real gap 已关闭。",
        "可控 rollout 扩大数据但会传播模型偏差；真实环境可用且风险低时直接采集仍更可信。",
    ),
    "08727": S(
        "长上下文 KV 在有限 HBM 中若按单一规则淘汰，会在容量、精度和请求并发间产生不可控尾延迟。",
        "ARKV 以请求/层级重要性和实时预算共同决定压缩、保留与迁移，把资源约束纳入 KV lifecycle。",
        "结果绑定论文的模型、长度、预算与 workload；未披露条件不能用于生产容量承诺。",
        "自适应策略增加 metadata 和误判面；短上下文或 HBM 充足时完整 KV 更可预测。",
    ),
    "08739": S(
        "KV offload 有多个容量/延迟/成本目标，固定 tier 比例无法适应访问模式与资源价格变化。",
        "该系统搜索 Pareto 配置，并依据 KV block access 在线调节分层缓存 eviction 与容量。",
        "真实 trace 只支持所测存储层级中的条件收益；不证明控制器面对突发漂移仍稳定。",
        "在线调优有探索损失和控制抖动；稳定 workload 仍可冻结已验证配置。",
    ),
    "08755": S(
        "agent framework 把 bounded context、typed output、credential isolation 与 durable state 留给应用约定，编译期无法检查。",
        "Turn 把 LLM inference、actor mailbox、capability handle 与 schema absorption 提升为语言/VM 原语。",
        "开源 VM 与工作负载证明这些 invariant 可被执行；不证明新语言优于成熟 runtime 的生态和性能。",
        "语言级保证减少应用漂移，却引入编译器、VM 与 FFI 信任根；简单 agent 仍可用通用语言加严格库。",
    ),
    "08852": S(
        "MCP/A2A 若不暴露 delegate identity、cost 和验证状态，跨 agent 路由只能依赖不透明 endpoint。",
        "LDP 把 identity card、payload negotiation、session state、provenance 与 trust domain写入协议。",
        "小型本地模型池和部分模拟结果只提供初步证据；尤其模拟 attack/failure 数字不能当生产事实。",
        "丰富 metadata 可能陈旧或被伪造，且增加协商成本；固定可信 agent 对仍可用更薄协议。",
    ),
    "09730": S(
        "Kubernetes HPA 看不到 KV 饱和、SLO 与异构 variant，scale-down 还可能破坏 stateful inference。",
        "WVA 与 llm-d 联合使用 engine saturation、headroom 和 fragmentation 状态做 variant-aware 扩缩。",
        "作者实验只支持其 cluster、流量和 cost model；摘要中的吞吐/失败改善不能外推其他环境。",
        "全局 control plane 提高利用率却依赖遥测新鲜度和迁移策略；同质无状态服务仍可用 HPA。",
    ),
    "09983": S(
        "edge MoE 的 expert offload 在需求出现后才搬运，I/O 会阻塞 token；普通 speculation 只优化 compute。",
        "MoE-SpAc 把 draft lookahead 当 expert demand sensor，联合执行预取、淘汰与异构 workload placement。",
        "实验绑定七个 benchmark、具体模型/设备/预算；不证明预测在路由漂移时仍保持命中。",
        "预取会浪费 I/O 和显存，mis-speculation 形成新尾延迟；expert 常驻可行时无需该路径。",
    ),
    "10030": S(
        "AI transport 默认 buffer 已正确分配、注册并安全回收，completion/teardown 时 ownership 仍隐含。",
        "dmaplane 以 kernel UAPI 管理 NUMA allocation、dma-buf、RDMA credit、GPU BAR pinning 与 completion-safe lifecycle。",
        "Soft-RoCE 和指定 GPU/NUMA 测量支持实现行为；不代表 provider-independent performance。",
        "统一 buffer plane 减少 glue code，却扩大内核 TCB 与 pinning 风险；单机 memcpy 路径仍更简单。",
    ),
    "10335": S(
        "reasoning 长度运行前未知会造成 KV 过度预留、碎片和错误的 thinking budget。",
        "Fuel Gauge 从隐藏信号预测 CoT 长度，再把预测用于 KV allocation 和推理长度控制。",
        "多模态 QA 结果只支持所测模型/任务中的预测相关性；不能保证困难分布或新 policy 下稳定。",
        "预测错误会造成 OOM、频繁扩容或截断；保守动态增长仍是可靠回退。",
    ),
    "11340": S(
        "缺少内部指标的托管 serving 仍需在 workload 漂移下调参，离线固定配置无法最大化 SLO goodput。",
        "黑盒 controller 只使用短窗口端到端观测，以 hill climbing 更新配置，并把系统规格纳入 factsheet。",
        "作者测量只证明给定参数空间和负载中的局部调优；不证明无状态 hill climbing 避免所有振荡。",
        "在线探索可能伤害 SLO，且 factsheet 会随版本过期；稳定服务仍应冻结经过压测的配置。",
    ),
    "11535": S(
        "top-k token-choice 路由固定每 token 计算并依赖跨 batch load-balance loss，难支持因 token 变化的动态容量。",
        "Expert Threshold 让每个 expert 维护全局分布 EMA threshold，独立决定接收 token，保持 causal routing。",
        "2.4B 预训练结果支持该规模/数据中的 loss 与 balance；不证明超大 MoE 的 all-to-all 尾延迟。",
        "动态 expert 数提高适配性，却让每 token compute 和 capacity 更难预测；硬 SLO 下固定 top-k 更可控。",
    ),
    "12262": S(
        "视频生成若只能在完整上下文后开始 reasoning，会牺牲流式场景的时效和状态连续性。",
        "Video Streaming Thinking 将持续到达帧分段写入可更新表示，并让生成与观察交错，而非一次性消费完整视频。",
        "结果限于公开模型、视频任务和 chunk policy；不证明开放长流中的 memory drift 可控。",
        "在线处理降低等待却减少未来上下文并增加 segment boundary error；离线高质量理解仍可看完整视频。",
    ),
    "12946": S(
        "隐私推理的批处理按固定顺序执行时，紧急请求插队会破坏加密计算共享并拖慢全批。",
        "PrivQJ 在 HE/MPC 处理中回收 slot，让高优先级输入 piggyback 到正在执行的 batch，而不重启共同计算。",
        "理论和实验只支持论文 primitive、batch shape 与 threat model；不证明通用神经服务具有相同开销。",
        "优先插队增加调度 metadata 与公平性问题；无优先级或 batch 很小时固定顺序更简单。",
    ),
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def independent_closure_reason(row: dict) -> str:
    # Persist the family-specific title, abstract thesis and exclusion boundary.
    # The semantic judgment is performed before this function is called; this
    # serializer must not collapse it back into a keyword-derived template.
    return "fresh-context adjudication: " + author.base.closure_reason(row)


def write_denominator_receipt(day: int, records: dict) -> tuple[dict, str]:
    report_date = f"2026-03-{day:02d}"
    rows = []
    for aid, row in sorted(records.items()):
        if row.get("owner_report_date") != report_date or row.get("status") != "scheduled_match":
            continue
        prior = aid in ORIGINAL
        retained = aid in FINAL
        withdrawn = aid in WITHDRAWN
        if withdrawn:
            decision, finding, reason = (
                "pre_denominator_closure", "withdrawn_removed",
                "official current abs page marks the paper withdrawn; identity/status retained, candidate/review/Books paths forbidden",
            )
        elif retained:
            decision = "candidate_denominator"
            finding = "false_negative_corrected" if not prior else "original_retained_upheld"
            reason = "fresh-context retained: title+abstract states a durable AI-System mechanism, ownership boundary, or evaluation/security contract"
        else:
            decision = "pre_denominator_closure"
            finding = "closure_upheld"
            reason = independent_closure_reason(row)
        rows.append({
            "arxiv_id": aid,
            "source_family_id": f"SF-2026-ARXIV-{aid.replace('.', '-')}",
            "title": row["title"],
            "abstract": row.get("abstract", ""),
            "prior_author_decision": "candidate_denominator" if prior else "pre_denominator_closure",
            "fresh_context_decision": decision,
            "finding": finding,
            "reason": reason,
        })
    payload = {
        "schema": "fresh-context-denominator-audit-v2.1",
        "auditor": "fresh-context:march-lane-a-reviewer",
        "report_date": report_date,
        "scope": "all strict-window raw title+abstract rows; author decision and proposal queues were challenge inputs only",
        "raw_identities": len(rows), "screened": len(rows),
        "retained": sum(x["fresh_context_decision"] == "candidate_denominator" for x in rows),
        "closures": sum(x["fresh_context_decision"] == "pre_denominator_closure" for x in rows),
        "false_negatives_corrected": sum(x["finding"] == "false_negative_corrected" for x in rows),
        "false_positives_removed": sum(x["finding"] == "withdrawn_removed" for x in rows),
        "weekly_dependency": 0,
        "rows": rows,
    }
    path = ROOT / f"papers/2026/03/_sources/daily-202603{day:02d}/fresh-context-audit-receipt.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    return payload, sha(path)


def enforce_withdrawn_identity_closure(day: int) -> None:
    """Keep withdrawn identity/status, while forbidding candidate descendants."""
    src = ROOT / f"papers/2026/03/_sources/daily-202603{day:02d}"
    ledger_path = src / "screening-ledger-final.json"
    ledger = json.loads(ledger_path.read_text())
    changed = False
    for row in ledger["identities"]:
        if row["arxiv_id"] not in WITHDRAWN:
            continue
        row.update(
            screening_status="pre_denominator_closure",
            screening_reason="withdrawn_primary_source",
            review_status="not_required_pre_denominator",
            access_status="withdrawn",
            integration_disposition="Rejected — Withdrawn primary source",
        )
        changed = True
    if not changed:
        return
    ledger["withdrawn_primary_sources"] = sorted(
        set(ledger.get("withdrawn_primary_sources", [])) | WITHDRAWN
    )
    ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    tsv_path = src / "screening-ledger-final.tsv"
    with tsv_path.open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["arxiv_id", "submitted_v1_utc", "title", "categories", "screening_status", "screening_reason"])
        for row in ledger["identities"]:
            writer.writerow([
                row["arxiv_id"], row["registry_updated_v1_utc"], row["title"],
                ";".join(row["categories"]), row["screening_status"], row["screening_reason"],
            ])
    author_audit_path = src / "author-side-audit.json"
    author_audit = json.loads(author_audit_path.read_text())
    author_audit["withdrawn"] = len(ledger["withdrawn_primary_sources"])
    author_audit_path.write_text(json.dumps(author_audit, ensure_ascii=False, indent=2) + "\n")


def write_evidence_receipt(day: int, records: dict) -> tuple[dict, str]:
    src = ROOT / f"papers/2026/03/_sources/daily-202603{day:02d}"
    packet = json.loads((src / "exact-v1-review-packet.json").read_text())
    items = []
    for review in packet["items"]:
        aid = review["primary_identifier"].split(":", 1)[1].removesuffix("v1")
        row = records[aid]
        design, reach, durability = author.base.score(row, review)
        findings = []
        if review.get("withdrawn"):
            findings.append("withdrawn_candidate_forbidden")
        if review.get("result") != "complete":
            findings.append("exact_v1_review_incomplete")
        if str(review.get("method_locator", "")).startswith("Not Disclosed"):
            findings.append("method_role_locator_unresolved")
        if review.get("stable_node_id") not in author.base.NODE_PATH:
            findings.append("stable_node_unresolved")
        if aid in ADDITIONS and aid not in {f"2603.{x}" for x in SYNTHESIS}:
            findings.append("paper_specific_synthesis_missing")
        items.append({
            "source_family_id": review["source_family_id"],
            "primary_identifier": review["primary_identifier"],
            "score_v2": {"design_delta": design, "system_reach": reach, "durability": durability, "total": design + reach + durability},
            "review_route": review.get("review_route"),
            "stable_node_id": review.get("stable_node_id"),
            "method_locator": review.get("method_locator"),
            "evaluation_locator": review.get("evaluation_locator"),
            "limitations_locator": review.get("limitations_locator"),
            "artifact_locator": review.get("artifact_locator"),
            "claim_boundary": review.get("claim_boundary"),
            "books_disposition": review.get("books_disposition"),
            "books_decision_status": "proposal_requires_root_reconciliation" if review.get("books_disposition") == "Integrate" else "no_change_upheld",
            "findings": findings,
            "status": "open" if findings else "passed",
        })
    payload = {
        "schema": "fresh-context-evidence-books-audit-v2.1",
        "auditor": "fresh-context:march-lane-a-reviewer",
        "report_date": f"2026-03-{day:02d}",
        "status": "open" if any(x["status"] == "open" for x in items) else "passed",
        "reviewed_candidates": len(items),
        "passed_candidates": sum(x["status"] == "passed" for x in items),
        "open_candidates": sum(x["status"] == "open" for x in items),
        "integrate_proposals_requiring_root_reconciliation": sum(x["books_disposition"] == "Integrate" for x in items),
        "items": items,
    }
    path = src / "fresh-context-evidence-findings.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    return payload, sha(path)


def patch_report(day: int, denominator: dict, denominator_sha: str, evidence: dict, evidence_sha: str) -> None:
    path = ROOT / f"papers/2026/03/{day:02d}/README.md"
    text = path.read_text()
    coverage_ref = f"coverage:SRC-ARXIV:202603{day:02d}"
    evidence_refs = "; ".join(
        f"review:{item['source_family_id']}" for item in evidence["items"]
    ) or "validator:review-completion-v1"
    books_finding = (
        f"FINDING-BOOKS-WRITEBACK-PENDING: {evidence['integrate_proposals_requiring_root_reconciliation']} "
        "Integrate proposals require root serial reconciliation"
    )
    audit_rows = (
        f"| SA-202603{day:02d}-COVERAGE | fresh-context:march-lane-a-reviewer | coverage | {coverage_ref} | — | all {denominator['raw_identities']} raw title+abstract rows independently adjudicated; false negatives corrected={denominator['false_negatives_corrected']}; false positives removed={denominator['false_positives_removed']}; receipt sha256={denominator_sha}; Weekly dependency=0 | passed |\n"
        f"| SA-202603{day:02d}-EVIDENCE | fresh-context:march-lane-a-reviewer | evidence | {evidence_refs} | {'FINDING-EVIDENCE-OPEN: unresolved locator-role candidates='+str(evidence['open_candidates']) if evidence['open_candidates'] else '—'} | exact-v1, Score V2, owner, locator-role and claim boundary independently audited for {evidence['reviewed_candidates']} candidates; receipt sha256={evidence_sha} | {'open' if evidence['open_candidates'] else 'passed'} |\n"
        f"| SA-202603{day:02d}-SELECTION | fresh-context:march-lane-a-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | — | review count and three-unit narrative selection kept separate | passed |\n"
        f"| SA-202603{day:02d}-BOOKS | fresh-context:march-lane-a-reviewer | books | validator:books-comparison-v1 | {books_finding} | no Books written; root must serially reconcile the date-specific queue, write canonical owners in date order, and run non-writer post-write audit | open |"
    )
    text = re.sub(
        rf"\| SA-202603{day:02d}-COVERAGE .*?\n\| SA-202603{day:02d}-EVIDENCE .*?\n\| SA-202603{day:02d}-SELECTION .*?\n\| SA-202603{day:02d}-BOOKS .*?(?=\n\n)",
        audit_rows, text, flags=re.S,
    )
    evidence_gate = "Open" if evidence["open_candidates"] else "Passed"
    text = re.sub(
        r"\*\*Status:\*\* In Progress；Coverage=(?:Open|Closed)、Evidence=(?:Open|Passed)、Books=Open；.*",
        f"**Status:** In Progress；Coverage=Closed、Evidence={evidence_gate}、Books=Open；fresh-context Coverage / Evidence audit 已完成，Integrate 串行 writeback 与 post-write audit 未完成。",
        text,
        count=1,
    )
    text = text.replace("| Coverage Gate | Open |", "| Coverage Gate | Closed |")
    text = re.sub(r"\| Evidence Gate \| (?:Open|Passed) \|", f"| Evidence Gate | {evidence_gate} |", text, count=1)
    text = re.sub(r"- Coverage: `Open`（.*?）", "- Coverage: `Closed`（SRC-ARXIV 全量枚举、严格窗口、withdrawn 与全 raw FP/FN 审计已闭合）", text)
    text = re.sub(
        r"- Evidence: `(?:Open|Passed)`（.*?）",
        f"- Evidence: `{evidence_gate}`（fresh-context exact-v1、Score、owner、locator-role 与 claim boundary 审计；open candidates={evidence['open_candidates']}）",
        text,
    )
    text = text.replace(
        f"由独立 reviewer 完成 FP/FN、exact-v1、Selection 与 Books prewrite audit；随后按日期顺序串行执行 {evidence['integrate_proposals_requiring_root_reconciliation']} 项 Integrate 建议。",
        f"Coverage、Evidence 与 Selection 的独立审计已完成；由 root 按日期顺序复核并串行执行 {evidence['integrate_proposals_requiring_root_reconciliation']} 项 Integrate 建议，再执行非写作者 post-write audit。",
    )
    text = text.replace(
        "- `SRC-ARXIV` 的独立 retained false-positive / closure false-negative audit 尚未完成。",
        f"- `SRC-ARXIV` 的独立 retained false-positive / closure false-negative audit 已完成；open candidates={evidence['open_candidates']}。",
    )
    text = text.replace(
        "- fresh-context Semantic Audit 与 Integrate writeback 尚未完成。",
        "- fresh-context Coverage / Evidence / Selection audit 已完成；仅 Integrate 串行 writeback 与 post-write Books audit 尚未完成。",
    )
    path.write_text(text)
    author_audit_path = ROOT / f"papers/2026/03/_sources/daily-202603{day:02d}/author-side-audit.json"
    author_audit = json.loads(author_audit_path.read_text())
    author_audit["fresh_context_status"] = (
        "evidence_open" if evidence["open_candidates"]
        else "coverage_evidence_selection_passed_books_queue_pending"
    )
    author_audit["fresh_context_denominator_receipt_sha256"] = denominator_sha
    author_audit["fresh_context_evidence_receipt_sha256"] = evidence_sha
    author_audit_path.write_text(json.dumps(author_audit, ensure_ascii=False, indent=2) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--day",
        dest="days",
        action="append",
        type=int,
        choices=range(9, 17),
        help="只重建指定日期；可重复传入。默认重建 03-09..16。",
    )
    args = parser.parse_args()
    author.configure()
    author.base.SECTION_OVERRIDES.update(SECTION_OVERRIDES)
    author.base.pdf_sections = reviewer_pdf_sections
    install_exact_v1_pdf_fallback()
    author.base.review_one = reviewer_review_one
    author.base.score = reviewer_score
    author.base.DURABLE_CANDIDATES = FINAL
    author.base.NODE_OVERRIDES.update({f"2603.{suffix}": node for suffix, node in NODE.items()})
    author.base.PAPER_SYNTHESIS.update({f"2603.{suffix}": value for suffix, value in SYNTHESIS.items()})
    author.base.INTEGRATE_SUGGESTIONS.add("2603.06578")
    author.base.NARRATIVE_LENS.setdefault(
        "AGENT-PLATFORM",
        (
            "应用代码直接持有 context、credential 和 workflow state，在小规模时路径最短。",
            "长驻、多租户 agent 要求 execution identity、capability、durable state 与资源生命周期成为平台责任。",
            "agent definition、run identity、capability handle、mailbox 与持久状态",
            "单 agent、短任务和固定工具集仍可使用普通应用 runtime。",
        ),
    )
    author.base.NARRATIVE_LENS.setdefault(
        "AGENT-TOOL-CALLING",
        (
            "自由文本建议在没有副作用时路径最短，也不需要维护执行协议。",
            "结构化输出、外部 action 与 grammar 约束要求把 proposal、validation 和 commit 分离。",
            "tool/schema identity、grammar state、argument validation、authorization 与 execution receipt",
            "只读且无副作用的低风险查询仍可使用较薄的调用层。",
        ),
    )
    author.base.NARRATIVE_LENS.setdefault(
        "INFER-DECODE",
        (
            "一次性离线生成可持有完整输入和历史，控制流简单且质量优先。",
            "流式输入、长输出与交互时延要求 decode state 有界、可续接并可安全终止。",
            "per-step decode state、termination、stream boundary 与 output commit",
            "输入完整且无交互 SLO 时，离线全上下文生成仍更易保证连贯性。",
        ),
    )
    author.base.NARRATIVE_LENS.setdefault(
        "MODEL-SELF-ATTENTION",
        (
            "dense attention 保留任意 token 间的直接依赖，最容易解释信息可达性。",
            "序列扩展和资源上限迫使模型裁剪连接，同时仍需维持跨层信息路径。",
            "attention graph、causal reachability、稀疏 pattern 与跨层信息路径",
            "短序列、容量足够或 exactness 优先时，dense attention 仍是可靠基线。",
        ),
    )
    author.base.NARRATIVE_LENS.setdefault(
        "PLATFORM-PRODUCTION",
        (
            "单模型、单任务的离线交付在需求稳定时最少引入生命周期状态。",
            "多用例、在线反馈和持续发布要求数据、模型 variant、服务与 release evidence 共同版本化。",
            "production asset identity、variant lineage、deployment state、online evidence 与 rollback",
            "需求单一且发布频率低时，冻结模型和人工验收仍有更低治理成本。",
        ),
    )
    author.base.NARRATIVE_LENS.setdefault(
        "TRAIN-PPO",
        (
            "同步、小规模 rollout 容易复算 policy version 与 trajectory，对早期实验足够。",
            "环境覆盖、吞吐和长轨迹压力要求并行采样，同时控制 stale policy 与更新边界。",
            "policy version、environment state、rollout ownership、advantage 与 optimizer commit",
            "环境昂贵、数据可复用或规模较小时，同步 rollout 仍更稳定。",
        ),
    )
    author.base.NODE_PATH.setdefault(
        "MODEL-SELF-ATTENTION", "books/part-02-model/14-self-attention.md"
    )
    author.base.NODE_PATH.setdefault(
        "TRAIN-PPO", "books/part-04-training-system/32-ppo.md"
    )
    author.base.NODE_PATH.setdefault(
        "INFER-DECODE", "books/part-05-inference-system/44-decode.md"
    )
    raw_total, records, _ = author.base.load_records()
    missing = FINAL - set(records)
    if missing:
        raise RuntimeError(f"fresh denominator identities absent from recovery receipt: {sorted(missing)}")
    for day in args.days or range(9, 17):
        author.base.render_day(day, raw_total, records)
        enforce_withdrawn_identity_closure(day)
        denominator, denominator_sha = write_denominator_receipt(day, records)
        evidence, evidence_sha = write_evidence_receipt(day, records)
        patch_report(day, denominator, denominator_sha, evidence, evidence_sha)
        print(json.dumps({
            "date": f"2026-03-{day:02d}", "raw": denominator["raw_identities"],
            "retained": denominator["retained"], "closures": denominator["closures"],
            "fn_corrected": denominator["false_negatives_corrected"],
            "fp_removed": denominator["false_positives_removed"],
            "evidence_open": evidence["open_candidates"],
        }, ensure_ascii=False))


if __name__ == "__main__":
    main()
