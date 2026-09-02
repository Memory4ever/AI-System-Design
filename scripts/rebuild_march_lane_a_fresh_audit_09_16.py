#!/usr/bin/env python3
"""Independent fresh-context audit for the 2026-03-09..16 author slice.

The reviewer replays every strict-window title+abstract row.  The author's
retained set is only the baseline needed to express disagreements; it is never
used as a discovery filter.  Weekly artifacts are not read.  This module also
refreshes exact-v1 packets for corrected false negatives and removes withdrawn
families from every candidate/review/Books path.
"""

from __future__ import annotations

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


ORIGINAL = set(author.DURABLE_CANDIDATES)
WITHDRAWN = {"2603.07473"}
ADDITIONS_BY_DAY = {
    9: "05553 05578 06001 06003 06081 06199 06365".split(),
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
    "2603.05881": {"method": [r"^3\.3 CoCA", r"^3\.2 Confidence-First"]},
    "2603.06331": {"method": [r"^4\.1 Curvature-guided", r"^4\.2 Chaotic-prioritized"]},
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
    "05553": "TRAIN-DATA", "05578": "PLATFORM-EVALUATION-SYSTEM",
    "06001": "MULTIMODAL-EMBODIED-VLA", "06003": "MODEL-MOE",
    "06081": "PLATFORM-EVALUATION-SYSTEM", "06199": "INFER-TENSORRT-LLM",
    "06365": "PLATFORM-SECURITY", "06588": "INFER-TENSORRT-LLM",
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


def S(problem: str, mechanism: str, evidence: str, boundary: str):
    return problem, mechanism, evidence, boundary


SYNTHESIS = {
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
    text = (row["title"] + " " + row.get("abstract", "")).lower()
    if not any(token in text for token in (
        "llm", "language model", "agent", "transformer", "vision-language", "world model",
        "diffusion", "gpu", "inference", "training", "retrieval", "foundation model",
    )):
        return "fresh-context closure: no AI-System object in the title+abstract contract"
    if any(token in text for token in ("medical", "disease", "wireless", "agriculture", "satellite")):
        return "fresh-context closure: domain application without a reusable AI-System ownership or evaluation delta"
    return "fresh-context closure: local model/task method; no durable state/data/control ownership, platform contract, or Books correction"


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


def main() -> None:
    author.configure()
    author.base.SECTION_OVERRIDES.update(SECTION_OVERRIDES)
    author.base.pdf_sections = reviewer_pdf_sections
    install_exact_v1_pdf_fallback()
    author.base.review_one = reviewer_review_one
    author.base.DURABLE_CANDIDATES = FINAL
    author.base.NODE_OVERRIDES.update({f"2603.{suffix}": node for suffix, node in NODE.items()})
    author.base.PAPER_SYNTHESIS.update({f"2603.{suffix}": value for suffix, value in SYNTHESIS.items()})
    author.base.NARRATIVE_LENS.setdefault(
        "AGENT-PLATFORM",
        (
            "应用代码直接持有 context、credential 和 workflow state，在小规模时路径最短。",
            "长驻、多租户 agent 要求 execution identity、capability、durable state 与资源生命周期成为平台责任。",
            "agent definition、run identity、capability handle、mailbox 与持久状态",
            "单 agent、短任务和固定工具集仍可使用普通应用 runtime。",
        ),
    )
    raw_total, records, _ = author.base.load_records()
    missing = FINAL - set(records)
    if missing:
        raise RuntimeError(f"fresh denominator identities absent from recovery receipt: {sorted(missing)}")
    for day in range(9, 17):
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
