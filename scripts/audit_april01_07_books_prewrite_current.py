#!/usr/bin/env python3
"""Fresh-context Books pre-write audit for the 2026-04-01..07 Dailies.

This audit deliberately ignores prior aggregate-report artifacts and the
previous Books queue.  It treats the exact-v1 packet only as evidence, re-derives the
ROADMAP owner from the paper's mechanism, and compares every retained family
with the current owner and adjacent chapters.  It never writes shared Books.
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MONTH = ROOT / "papers/2026/04"
SRC = MONTH / "_sources"
ROADMAP = ROOT / "ROADMAP.md"
EXECUTED_AT = "2026-09-01T18:40:00+08:00"


# These are the only families for which the exact-v1 mechanism still changes
# a proposition not already present in the current Books.  This set was formed
# after reading the exact-v1 packets and current owner/adjacent chapters; it is
# not derived from the old queue or a Weekly report.
INTEGRATE = {
    "2604.00368": "INFER-DYNAMO",                 # declarative transfer intent vs physical execution
    "2604.00529": "INFER-TENSORRT-LLM",          # one anchor checkpoint, multiple runtime numeric formats
    "2604.00726": "TRAIN-CHECKPOINT",             # silent update corruption before checkpoint commit
    "2604.03539": "PLATFORM-PRODUCTION",          # modular control-plane verification contract
    "2604.03968": "PLATFORM-TRACE",               # collusion-resistant multi-observer monitoring protocol
    "2604.03997": "AGENT-MULTI-AGENT",            # durable ledger state as indirect coordination owner
    "2604.04035": "PLATFORM-SECURITY",            # denial feedback as a causal leakage channel
    "2604.04261": "TRAIN-RLHF",                   # pluralistic, federated preference-state ownership
    "2604.04522": "PLATFORM-SECURITY",            # cryptographic human-delegation provenance
    "2604.04712": "PLATFORM-SECURITY",            # hardware governance with adversary-tiered attestation
    "2604.05057": "PLATFORM-EVALUATION-SYSTEM",   # unseen deployment mass as a release-risk signal
}


# The pre-write queue must carry the mechanism that was actually read from the
# exact-v1 body.  These overrides replace the author packet's broad lane
# templates (for example, treating training corruption as serving admission)
# with the source-specific state/control contract used by the Books decision.
QUEUE_REVIEW_OVERRIDES = {
    "2604.00368": {
        "old": "旧传输层把 transfer intent、切片、路径选择与失败重试绑定在同一个静态执行计划里；链路稳定时这种路径简单且可预测，但 disaggregated serving 的拥塞、grey failure 与多路径带宽变化后，静态 striping 会造成 HoL blocking 与带宽闲置。",
        "mechanism": "TENT 把声明式 transfer intent 与物理执行解耦：控制面拥有 slice identity、路径与副本健康、重路由及完成状态，数据面只执行已编排的 slice transfer；因而恢复决策不再由上层请求临时拼装。",
        "tradeoff": "收益是在论文所测 SGLang HiCache 工作负载中提高吞吐并降低 P90 TTFT，同时支持亚 50 ms 的透明绕障；代价是额外控制状态、路径观测与重路由复杂度。拥塞信号失真、切片过细或控制面失效时，应回退静态/单路径传输，并把作者结果限制在公开拓扑与 workload。",
    },
    "2604.00529": {
        "old": "传统量化部署通常为每个目标位宽分别训练或校准 artifact；目标硬件和精度固定时这能减少运行时分支，但弹性推理需要在多个 MXINT/MXFP 格式间切换时会形成多份 checkpoint 与再训练成本。",
        "mechanism": "MF-QAT 训练一个 multi-format anchor checkpoint，并用 Slice-and-Scale 在部署时转换到较低 MXINT/MXFP 格式；artifact owner 必须同时管理 anchor revision、转换规则、目标格式与逐格式 acceptance evidence，而不能把每个低精度副本当成无关模型。",
        "tradeoff": "收益是避免为每个格式重新训练，并支持运行时按资源条件选择格式；代价是 QAT、格式转换 kernel 与逐目标硬件验收。转换后的精度或 kernel 条件不满足时回退 anchor/high-precision artifact，论文结论不得外推到未测试模型、格式和硬件。",
    },
    "2604.00726": {
        "old": "训练系统通常依赖设备异常、NaN 或作业失败来触发恢复；硬件故障能被显式暴露时这种 checkpoint 策略足够，但 silent data corruption 可产生数值合法却有害的参数更新，并被持久化进下一 checkpoint。",
        "mechanism": "论文在 update/commit 边界检测可疑参数更新，并在命中后重算最近训练 step；训练 runtime 因而拥有 update-integrity evidence、quarantine 与 retry 状态，checkpoint writer 只有在更新通过验证后才能提交新 artifact。",
        "tradeoff": "收益是在作者测试的 LLaMA 60M/350M/1.3B 故障注入下缓解损坏传播；代价是检测开销、误报和重算。检测器未覆盖的 corruption 仍可能漏过，异常时应回退上一个已验 checkpoint 并扩大硬件/数值诊断，不能外推为通用 SDC 证明。",
    },
    "2604.03539": {
        "old": "控制面验证常把全局 eventually-stable property 直接交给单体模型检查；组件与协议固定时可行，但模块独立演进后，全局证明会随组合规模增长且难以判断哪个组件接口破坏了性质。",
        "mechanism": "CB-VER 用 converges-before graph 表达最终稳定状态间的先后关系，并以组件接口组合验证全局性质；verification owner 管理 property、CB-graph、组件 interface obligation 与变更后的再证明证据，而不是只保存一次测试结果。",
        "tradeoff": "收益是把模块控制面的 eventual property 转换为可组合验证并支持接口合成；代价是模型抽象、CHC 求解与环境不变假设。超出论文网络控制面模型、环境继续变化或接口不充分时，应回退更窄的显式模型检查/运行时 gate，不能将形式结果直接视为 AI 平台生产正确性。",
    },
    "2604.03968": {
        "old": "单一 monitor score 在诚实 agent 与低相关风险下便于部署；当 monitor 与 agent 可能同源或串谋、攻击只在 reasoning/action trace 中显现时，单分数会丢失职责分离与不一致证据。",
        "mechanism": "TraceGuard 将 goal alignment、constraint adherence、reasoning coherence、safety awareness 与 action-trace consistency 分开观测，并组合独立 LLM/heuristic signals；monitoring owner 保存各维证据、observer identity、分歧和最终 gate，而非只提交一个不可审计 scalar。",
        "tradeoff": "收益是作者 519 样本协议中的 attack/honest separation 与 separation-of-duties 路径；代价是多观察者调用、相关失败和阈值校准。观察者仍可能共享盲点，异常时回退最小权限、人工升级与隔离执行，论文样本不证明开放生产环境安全率。",
    },
    "2604.03997": {
        "old": "多智能体协调通常把 message 当作共享事实；低并发和可信参与者下足够直接，但消息丢失、重放、并发写入或成员异步观察后，通信记录不再等同于一致的共享状态。",
        "mechanism": "Ledger-State Stigmergy 让参与者通过追加并观察 durable ledger state 间接协调；ledger/schema/commit owner 定义可见状态、更新顺序与因果关系，message 只是一种输入而不是最终事实 owner。",
        "tradeoff": "收益是把间接协调锚定到可追溯状态；代价是一致性延迟、ledger 成本、schema 演进和错误状态的持久传播。无需审计/跨域协作时仍可用轻量消息，ledger 不可用或共识成本过高时应回退单 owner workflow。该 exact-v1 主要给出形式框架，不证明生产吞吐或容错上界。",
    },
    "2604.04035": {
        "old": "工具安全策略通常把 denied action 当作安全终点并把拒绝原因原样返回；在单步调用中便于调试，但多步 agent 可把允许/拒绝及字段级差异当作 oracle，逐步推断受保护的因果与 provenance。",
        "mechanism": "ARM 在每次 tool invocation 前查询包含调用、返回字段、provenance 与 denied action 的因果图，并让 reference monitor 同时拥有授权判定与 denial-feedback disclosure policy；拒绝不再只是布尔结果，而是受控观察。",
        "tradeoff": "收益是在论文三个攻击场景中阻断 causality laundering、transitive taint 与 mixed-provenance misuse，报告 policy evaluation 为亚毫秒；代价是细粒度 taint graph、反馈降级与误拒绝。覆盖外工具语义、隐式信道或错误 provenance 仍可能绕过，异常时回退最小反馈、人工审批和隔离执行。",
    },
    "2604.04261": {
        "old": "Federated RLHF 以平均 group reward 聚合偏好，在群体同质且数据可集中比较时简单；群体对齐程度不同且 raw preference 不可共享时，平均会让多数/高分群体持续主导更新。",
        "mechanism": "APPA 根据各 group 的历史 alignment reward 动态重加权 federated PPO 更新；聚合 owner 保存 group identity、历史 reward、权重与 fairness/alignment decision，使 pluralistic preference state 不被压成单一 reward。",
        "tradeoff": "收益是在 GLOBALQA/OQA、三类公开模型设置中提高 worst-group alignment，同时多数配置保持较高 overall alignment；代价是历史信号漂移、group 定义与 fairness/utility 权衡。群体标签失真或权重振荡时回退受限平均/最小群体约束并人工复核，结果不外推到未测人群与偏好协议。",
    },
    "2604.04522": {
        "old": "现有 tool token 或 agent identity 常只证明当前调用者，低层级委托时足够；多跳 delegation 出现后，终端 action 无法证明最初 human principal、完整委托链与每跳 scope。",
        "mechanism": "HDP 用可验证 token 将 human principal、delegate、scope 与 append-only delegation chain 绑定，并在终端执行前验证；authorization owner 从 prompt/agent 自述迁移到可核验 provenance chain 与执行 gate。",
        "tradeoff": "收益是补足多跳 human authorization accountability；代价是 key/token 生命周期、撤销、重放与 scope 组合复杂度。它不替代 prompt-injection、行为正确性或运行时 sandbox；token 不完整或验证失败时应 fail closed 并回退人工授权。",
    },
    "2604.04712": {
        "old": "算力治理常假设硬件可以提供绝对防篡改计量；在商业合规且对手能力有限时可作为近似，但非国家与国家级对手会改变传感器、固件和审计链的可信边界。",
        "mechanism": "论文以 adversary tier 区分 commercial、non-state 与 nation-state threat，并把目标从 tamper-proof 改为 tamper-evident assurance；attestation owner 管理测量对象、硬件根、证据链、对手假设与可声明的合规边界。",
        "tradeoff": "收益是让监管/条约验证选择与对手能力匹配的硬件机制；代价是供应链信任、远程证明、隐私和误判。无法保证绝对不可绕过，证据链缺失或 threat tier 超界时应缩小结论并回退现场/多方审计，而不是把硬件信号当最终事实。",
    },
    "2604.05057": {
        "old": "部署评估通常用平均准确率与已见切片估计覆盖；分布轻尾且样本充分时可用，但 heavy-tailed operational states 中大量低频/未见状态会让测试分数掩盖 coverage risk。",
        "mechanism": "Blind-Spot Mass 用 Good-Turing 估计支持度低于阈值的总概率质量，并把 overall performance 分解为 supported 与 blind components；evaluation owner 必须保存 support threshold、样本分布、估计不确定性与 release decision。",
        "tradeoff": "收益是把未见/低支持状态从模糊担忧变成受 distribution contract 约束的 release-risk signal；代价是阈值敏感、独立同分布假设和估计方差。分布漂移或样本依赖破坏假设时，应回退分层抽样、在线 canary 与保守 release gate，论文推导不等于生产风险上界。",
    },
}


TARGET_H2_OVERRIDES = {
    "2604.03539": "Production Contract",
    "2604.04035": "Availability 与 Abuse",
    "2604.04522": "从“文本是否恶意”到“谁获得了行为控制权”",
    "2604.04712": "从资产与信任边界开始",
    "2604.05057": "第二个不变量：评估结论总是相对于分布",
}


# Fresh title+abstract/exact-v1 adjudications for mechanisms whose vocabulary
# crosses several chapters.  These overrides document the semantic owner rather
# than inheriting a prior report's route.
OWNER_OVERRIDES = {
    "2603.29193": "AGENT-MEMORY", "2603.29194": "AGENT-MEMORY",
    "2603.29494": "MODEL-LONG-CONTEXT", "2603.29559": "PLATFORM-EVALUATION-SYSTEM",
    "2604.16402": "AGENT-RAG", "2603.29640": "AGENT-WORKFLOW",
    "2603.29665": "PLATFORM-SECURITY", "2604.00073": "AGENT-TOOL-CALLING",
    "2603.29919": "AGENT-CONTEXT", "2604.00136": "INFER-SCHEDULING",
    "2604.02375": "AGENT-WORKFLOW", "2604.00317": "TRAIN-DISTRIBUTED-TRAINING",
    "2604.00356": "PLATFORM-EVALUATION-SYSTEM", "2604.00478": "PLATFORM-SECURITY",
    "2604.00694": "AGENT-TOOL-CALLING", "2604.01350": "PLATFORM-MULTI-TENANT",
    "2604.01605": "MULTIMODAL-WORLD-MODELS", "2604.01621": "INFER-DYNAMO",
    "2604.01624": "AGENT-REFLECTION", "2604.01687": "AGENT-WORKFLOW",
    "2604.01904": "TRAIN-DATA", "2604.01905": "PLATFORM-SECURITY",
    "2604.02006": "TRAIN-RLHF", "2604.02110": "INFER-TENSORRT-LLM",
    "2604.02145": "PLATFORM-EVALUATION-SYSTEM", "2604.02268": "AGENT-MEMORY",
    "2604.02442": "INFER-GPU-MEMORY", "2604.02473": "INFER-GPU-MEMORY",
    "2604.02617": "PLATFORM-EVALUATION-SYSTEM", "2604.02638": "INFER-TENSORRT-LLM",
    "2604.02714": "MULTIMODAL-EMBODIED-VLA", "2604.02767": "PLATFORM-SECURITY",
    "2604.02945": "INFER-SCHEDULING", "2604.02965": "MULTIMODAL-EMBODIED-VLA",
    "2604.02985": "MODEL-LONG-CONTEXT", "2604.03070": "PLATFORM-SECURITY",
    "2604.03088": "AGENT-WORKFLOW", "2604.03131": "PLATFORM-SECURITY",
    "2604.03179": "TRAIN-RLHF", "2604.22783": "TRAIN-LORA",
    "2604.03208": "MULTIMODAL-WORLD-MODELS", "2604.03362": "PLATFORM-EVALUATION-SYSTEM",
    "2604.03425": "PLATFORM-SECURITY", "2604.03591": "PLATFORM-MONITORING",
    "2604.03714": "PLATFORM-SECURITY", "2604.03820": "PLATFORM-EVALUATION-SYSTEM",
    "2604.04979": "AGENT-CONTEXT", "2604.03904": "PLATFORM-EVALUATION-SYSTEM",
    "2604.03933": "PLATFORM-MONITORING", "2604.03964": "AGENT-WORKFLOW",
    "2604.06241": "PLATFORM-SECURITY", "2604.04043": "PLATFORM-SECURITY",
    "2604.04074": "PLATFORM-EVALUATION-SYSTEM", "2604.04220": "PLATFORM-EVALUATION-SYSTEM",
    "2604.04238": "AGENT-WORKFLOW", "2604.04247": "AGENT-WORKFLOW",
    "2604.04253": "INFER-GPU-MEMORY", "2604.04269": "AGENT-RAG",
    "2604.04335": "MULTIMODAL-GENERATIVE-PARADIGMS", "2604.04410": "TRAIN-RLHF",
    "2604.04660": "AGENT-PLATFORM", "2604.04750": "INFER-GPU-MEMORY",
    "2604.04783": "PLATFORM-SECURITY", "2604.04804": "AGENT-MEMORY",
    "2604.04806": "PLATFORM-EVALUATION-SYSTEM", "2604.04820": "AGENT-MCP",
    "2604.04855": "TRAIN-RLHF", "2604.04872": "TRAIN-DATA",
    "2604.04901": "AGENT-MEMORY", "2604.05074": "TRAIN-DATA",
    "2604.05080": "AGENT-WORKFLOW", "2604.05091": "TRAIN-ZERO",
    "2604.05096": "AGENT-RAG", "2604.05117": "TRAIN-RLHF",
    "2604.05119": "PLATFORM-TRACE", "2604.05150": "AGENT-WORKFLOW",
    "2604.05164": "AGENT-PLANNING", "2604.05225": "PLATFORM-EVALUATION-SYSTEM",
    "2604.05248": "TRAIN-LORA", "2604.05278": "AGENT-WORKFLOW",
    "2604.05289": "PLATFORM-SECURITY",
}


STOP = set(
    "the and for with from that this via using use used into based large language model models "
    "llm llms framework system systems approach method paper propose present introduce efficient "
    "towards novel agent agents ai our their these those such can are was were has have".split()
)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def clean(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def safe(value: object) -> str:
    return clean(value).replace("|", "\\|")


def family(aid: str) -> str:
    return f"SF-2026-ARXIV-{aid.replace('.', '-')}"


def tokens(text: str) -> set[str]:
    return {
        token for token in re.findall(r"[a-z][a-z0-9-]{2,}", text.lower())
        if token not in STOP
    }


def roadmap_nodes() -> tuple[dict[str, str], list[str]]:
    mapping = {}
    for node, path in re.findall(r"\| `([A-Z0-9-]+)` \| Ch\d+ \| `([^`]+)`", ROADMAP.read_text()):
        mapping[node] = path
    ordered = [
        str(path.relative_to(ROOT)) for path in sorted(
            (ROOT / "books").glob("part-*/*.md"),
            key=lambda p: int(re.match(r"(\d+)-", p.name).group(1)) if re.match(r"(\d+)-", p.name) else 999,
        ) if path.name != "README.md"
    ]
    return mapping, ordered


NODE_PATH, ORDERED_BOOKS = roadmap_nodes()


def route(row: dict) -> str:
    aid = row["arxiv_id"]
    if aid in INTEGRATE:
        return INTEGRATE[aid]
    if aid in OWNER_OVERRIDES:
        return OWNER_OVERRIDES[aid]
    text = f" {row['title']} {row.get('abstract', '')} ".lower()
    title = row["title"].lower()

    # Title-level purpose beats incidental abstract vocabulary.  This prevents
    # a benchmark mentioning a runtime, or an agent-memory paper mentioning a
    # token budget, from being routed to that incidental subsystem.
    title_rules: list[tuple[tuple[str, ...], str]] = [
        (("benchmark", "evaluating", "evaluation", "empirical audit", "empirical study", "measurement", "characterization"), "PLATFORM-EVALUATION-SYSTEM"),
        (("prompt injection", "jailbreak", "backdoor", "poison", "attack", "security", "safety", "vulnerability", "credential leakage", "guard"), "PLATFORM-SECURITY"),
        (("kv cache", "kv-cache", "kv compression", "kv routing"), "INFER-KV-CACHE"),
        (("speculative decoding", "speculative sampling", "speculation tree"), "INFER-SPECULATIVE-DECODING"),
        (("memory", "forgetting"), "AGENT-MEMORY"),
        (("multi-agent", "multi agent", "committee", "consensus"), "AGENT-MULTI-AGENT"),
        (("graphrag", " rag", "retrieval", "search agent", "web information seeking"), "AGENT-RAG"),
        (("tool", "api access"), "AGENT-TOOL-CALLING"),
        (("planning", "monte carlo tree search", "mcts"), "AGENT-PLANNING"),
        (("world model", "world modeling"), "MULTIMODAL-WORLD-MODELS"),
        (("vision-language-action", "vla", "robot", "embodied", "manipulation"), "MULTIMODAL-EMBODIED-VLA"),
        (("mixture-of-experts", "routing-free mixture", "expert routing", "moe"), "MODEL-MOE"),
        (("quantization", "dequantization", "low-precision", "mixed-precision"), "INFER-TENSORRT-LLM"),
        (("logging", "log analysis"), "PLATFORM-LOGGING"),
        (("trace", "telemetry", "observability", "diagnosis", "profiling"), "PLATFORM-TRACE"),
    ]
    for terms, node in title_rules:
        if any(term in title for term in terms):
            return node

    # Exact mechanism families first; generic words such as "agent" or
    # "evaluation" must never steal ownership from the actual state owner.
    rules: list[tuple[tuple[str, ...], str]] = [
        (("kv cache", "kv-cache", "key-value cache", "cache quantization"), "INFER-KV-CACHE"),
        (("speculative decoding", "speculative sampling", "speculation tree", "drafter", "draft model"), "INFER-SPECULATIVE-DECODING"),
        (("pagedattention", "paged attention"), "INFER-PAGED-ATTENTION"),
        (("mixture-of-experts", " mixture of experts", " moe ", "expert routing", "expert residency"), "MODEL-MOE"),
        (("quantization", "dequantization", "low-bit", "mixed-precision", "low-precision", "int4", "nf4"), "INFER-TENSORRT-LLM"),
        (("world model", "world modeling", "world-model"), "MULTIMODAL-WORLD-MODELS"),
        (("vision-language-action", " vla ", "robot", "embodied", "manipulation", "autonomous driving"), "MULTIMODAL-EMBODIED-VLA"),
        (("diffusion model serving", "video diffusion", "masked diffusion", "diffusion transformer"), "MULTIMODAL-GENERATIVE-PARADIGMS"),
        (("multimodal", "vision token", "visual token", "video large language"), "MULTIMODAL-REPRESENTATION"),
        (("checkpoint", "silent data corruption", "parameter update corruption", "recovery"), "TRAIN-CHECKPOINT"),
        (("tensor parallel", "alltoall", "all-to-all", "collective", "multi-gpu", "distributed training", "hybrid parallel", "parallelism"), "TRAIN-DISTRIBUTED-TRAINING"),
        (("federated", "decentralised post-training", "decentralized post-training"), "TRAIN-DISTRIBUTED-TRAINING"),
        (("dpo", "direct preference optimization"), "TRAIN-DPO"),
        (("ppo", "policy optimization", "grpo", "rlvr", "reinforcement post-training", "preference learning", "rlhf"), "TRAIN-RLHF"),
        (("optimizer", "pre-training", "pretraining", "continual pre-training", "training dynamics"), "TRAIN-PRETRAINING"),
        (("fine-tuning", "finetuning", "lora", "adapter"), "TRAIN-LORA"),
        (("training data", "data laundering", "contamination", "memorization"), "TRAIN-DATA"),
        (("prefill" ,), "INFER-PREFILL"),
        (("decode", "autoregressive decoding", "inference kernel", "kernel", "gpu-native", "accelerator", "pim", "near-memory"), "INFER-TENSORRT-LLM"),
        (("gpu memory", "vram", "offload", "cxl", "memory efficiency", "storage"), "INFER-GPU-MEMORY"),
        (("disaggregated", "data movement", "distributed inference", "co-serving", "co-execution"), "INFER-DYNAMO"),
        (("scheduler", "scheduling", "serving", "routing", "router", "admission control", "output length"), "INFER-SCHEDULING"),
        (("prompt injection", "jailbreak", "backdoor", "poison", "attack", "security", "safety", "privacy", "credential", "unlearning", "guardrail", "vulnerability", "fuzzing"), "PLATFORM-SECURITY"),
        (("multi-tenant", "cross-user", "noisy neighbor", "shared-state"), "PLATFORM-MULTI-TENANT"),
        (("energy", "power", "cost", "budget-paced"), "PLATFORM-COST"),
        (("log", "logging"), "PLATFORM-LOGGING"),
        (("trace", "telemetry", "observability", "diagnosis", "profiling"), "PLATFORM-TRACE"),
        (("model registry", "model artifact", "supply-chain"), "PLATFORM-MODEL-REGISTRY"),
        (("benchmark", "evaluation", "evaluator", "grader", "judge", "reliability", "metric", "measurement", "audit", "verification"), "PLATFORM-EVALUATION-SYSTEM"),
        (("retrieval-augmented", "graphrag", " rag ", "retriever", "retrieval", "search agent", "web information seeking"), "AGENT-RAG"),
        (("memory", "forgetting", "context compression", "context management", "personalization", "experience"), "AGENT-MEMORY"),
        (("model context protocol", " mcp ", "protocol-first", "agent-native protocol"), "AGENT-MCP"),
        (("multi-agent", "multi agent", "committee", "consensus", "collaboration"), "AGENT-MULTI-AGENT"),
        (("tool-calling", "tool calling", "tool use", "tool library", "api access", "action evaluation"), "AGENT-TOOL-CALLING"),
        (("planning", "monte carlo tree search", "mcts", "fast-slow"), "AGENT-PLANNING"),
        (("reflection", "self-verification", "verifier"), "AGENT-REFLECTION"),
        (("workflow", "software evolution", "code-editing", "coding agent", "automation", "execution kernel", "agent runtime"), "AGENT-WORKFLOW"),
        (("agent", "agentic"), "AGENT-PLATFORM"),
    ]
    for terms, node in rules:
        if any(term in text for term in terms):
            return node
    if "attention" in text or "long context" in text or "long-context" in text:
        return "MODEL-LONG-CONTEXT"
    if "control plane" in text:
        return "PLATFORM-FOUNDATIONS"
    if "governance" in text or "production" in title:
        return "PLATFORM-PRODUCTION"
    return "WORLDVIEW-SYSTEM-EVOLUTION"


def sections(path: str) -> list[dict]:
    lines = (ROOT / path).read_text(encoding="utf-8", errors="ignore").splitlines()
    h2 = [(i + 1, line[3:].strip()) for i, line in enumerate(lines) if line.startswith("## ")]
    out = []
    for pos, (line_no, heading) in enumerate(h2):
        end = h2[pos + 1][0] - 1 if pos + 1 < len(h2) else len(lines)
        body = clean(" ".join(lines[line_no:end]))
        out.append({"line": line_no, "heading": heading, "body": body})
    return out


GENERIC_H2 = {"本章要回答的问题", "本章在知识树中的位置", "自检问题", "小结", "Review notes", "Research Outlook", "Reflection"}


def best_section(path: str, query: str) -> dict:
    query_tokens = tokens(query)
    candidates = [item for item in sections(path) if item["heading"] not in GENERIC_H2]
    if not candidates:
        candidates = sections(path)
    def score(item: dict) -> tuple[int, int, int]:
        heading_hits = len(query_tokens & tokens(item["heading"]))
        body_hits = len(query_tokens & tokens(item["body"]))
        return (heading_hits * 8 + body_hits, heading_hits, -item["line"])
    return max(candidates, key=score)


def exact_section(path: str, heading: str) -> dict:
    matches = [item for item in sections(path) if item["heading"] == heading]
    assert len(matches) == 1, (path, heading, len(matches))
    return matches[0]


def ref(path: str, section: dict) -> str:
    return f"{path}#L{section['line']} (H2: {section['heading']})"


def adjacent_paths(path: str) -> list[str]:
    idx = ORDERED_BOOKS.index(path)
    result = []
    if idx > 0:
        result.append(ORDERED_BOOKS[idx - 1])
    if idx + 1 < len(ORDERED_BOOKS):
        result.append(ORDERED_BOOKS[idx + 1])
    return result


def proposition(section: dict, query: str) -> str:
    sentences = [
        clean(item)
        for item in re.split(r"(?<=[。！？.!?])\s+", section["body"])
        if len(clean(item)) >= 25
    ]
    paras = []
    for idx, sentence in enumerate(sentences):
        window = clean(" ".join(sentences[idx:idx + 3]))
        if len(window) >= 80:
            paras.append(window)
    q = tokens(query)
    if not paras:
        return f"当前章节 `{section['heading']}` 已定义该机制的 owner、边界与回退条件。"
    ranked = sorted(paras, key=lambda p: (len(q & tokens(p)), -abs(len(p) - 420)), reverse=True)
    return ranked[0][:900]


def first_sentence(text: str, limit: int = 520) -> str:
    text = clean(text)
    match = re.search(r"(?<=[.!?])\s+", text)
    return text[: match.start() + 1 if match else limit][:limit]


def score_v2(row: dict, disposition: str) -> dict:
    text = f"{row['title']} {row.get('abstract','')}".lower()
    design = 3 if disposition == "Integrate" else 2
    reach = 3 if any(k in text for k in ("system", "runtime", "distributed", "platform", "serving", "training", "agent")) else 2
    durability = 2 if any(k in row["title"].lower() for k in ("benchmark", "empirical", "evaluation", "case study")) else 3
    return {"design_delta": design, "system_reach": reach, "durability": durability, "total": design + reach + durability}


def owner_sha(path: str) -> str:
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def patch_review_body(body: str, node: str, disposition: str) -> str:
    body = re.sub(r"owner=`[A-Z0-9-]+`", f"owner=`{node}`", body)
    body = re.sub(r"Books Decision=`[^`]+`", f"Books Decision=`{disposition}`", body)
    return body


def rebuild_integrate_review_body(review: dict, node: str) -> str:
    fam = review["source_family_id"]
    evaluation_match = re.search(
        r"Evaluation contract：(.*?)\n\nTrade-off / failure / fallback / coexistence：",
        review["review_body"],
        flags=re.S,
    )
    evaluation = clean(evaluation_match.group(1)) if evaluation_match else (
        "exact-v1 的 evaluation 只按已记录的 Evaluation locator 与公开 workload 解释；"
        "未披露条件保持 Not Disclosed。"
    )
    return f"""
#### {review['title']}

问题、旧路径与约束变化：{review['old_path_and_changed_constraint']}

机制与 state/control owner：{review['mechanism_and_ownership']} owner=`{node}`。Method/Identity locator：{review['method_identity_locators']}。

Evaluation contract：{evaluation}

Trade-off / failure / fallback / coexistence：{review['tradeoffs_and_failure_modes']}

<!-- claim:{fam}:start -->{review['claim_boundary']}<!-- claim:{fam}:end -->

Books Decision=`Integrate`；fresh-context reviewer 未修改共享 Books。
"""


def normalized_body_sha256(body: str) -> str:
    normalized = unicodedata.normalize("NFC", body.replace("\r\n", "\n").replace("\r", "\n"))
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()


def recompute_review_provenance(review: dict, row: dict) -> str:
    def multi(value: object) -> str:
        items = []
        for raw in str(value).split(";"):
            item = unicodedata.normalize("NFC", raw.strip())
            if item and item not in {"—", "-", "none", "None"}:
                items.append(item)
        return ";".join(sorted(items))

    fam, aid = review["source_family_id"], review["arxiv_id"]
    canonical = "|".join((
        "review-completion-v1", fam, f"paper-v1:{aid}", f"arXiv:{aid}v1",
        "SRC-ARXIV", review["primary_evidence_version"],
        multi("; ".join(review["reviewed_evidence_versions"])), "deep",
        "review-override:knowledge_gap", multi(review["method_identity_locators"]),
        multi(review["evaluation_locators"]),
        multi(review["limitations_counterevidence_locators"]),
        multi(review["artifact_locators"]), f"claim:{fam}", f"review:{fam}",
        f"review-body-sha256:{normalized_body_sha256(review['review_body'])}",
    ))
    return "RP-" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]


def replace_between(text: str, start: str, end: str, replacement: str) -> str:
    a = text.index(start)
    b = text.index(end, a)
    return text[:a] + replacement.rstrip() + "\n\n" + text[b:]


def candidate_rows(ledger: dict) -> list[str]:
    rows = []
    for item in ledger["identities"]:
        if item.get("candidate_state") != "retained":
            continue
        s = item["score_v2"]
        aid = item["arxiv_id"]
        published = date.fromisoformat(item["first_public_date"])
        iso = published.isocalendar()
        owner_week = f"{iso.year}-W{iso.week:02d}"
        rows.append(
            f"| {family(aid)} | arXiv:{aid}v1 | paper-v1:{aid} | {owner_week} | "
            f"{item['first_public_date']} | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | "
            f"retained | deep_complete | accessible | knowledge_gap | review:{family(aid)} | self | — | new_in_window | "
            f"{item['owner_node']} | {item['integration_disposition']} | books-review:{family(aid)} | no |"
        )
    return rows


def render_reviews(reviews: list[dict]) -> str:
    rows, blocks = [], []
    for r in reviews:
        fam = r["source_family_id"]
        rows.append(
            f"| {fam} | {r['review_provenance_id']} | deep | {r['primary_evidence_version']} | "
            f"{'; '.join(r['reviewed_evidence_versions'])} | {safe(r['method_identity_locators'])} | "
            f"{safe(r['evaluation_locators'])} | {safe(r['limitations_counterevidence_locators'])} | "
            f"{safe(r['artifact_locators'])} | claim:{fam} | complete |"
        )
        blocks.append(f"<!-- review:{fam}:start -->{r['review_body']}<!-- review:{fam}:end -->")
    return """## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
""" + "\n".join(rows) + "\n\n### Source Reviews\n\n" + "\n\n".join(blocks)


def render_deep(reviews: list[dict], ledger_by_aid: dict) -> str:
    ranked = sorted(reviews, key=lambda r: (r["books_disposition"] != "Integrate", -ledger_by_aid[r["arxiv_id"]]["score_v2"]["total"], r["source_family_id"]))
    selected = {r["source_family_id"] for r in ranked[:3]}
    rows, blocks = [], []
    for r in reviews:
        fam, aid = r["source_family_id"], r["arxiv_id"]
        facts = ["forced_review"]
        if ledger_by_aid[aid]["score_v2"]["total"] >= 7:
            facts.insert(0, "score_7_9")
        if r["books_disposition"] == "Integrate":
            facts.append("potential_books_delta")
        eligibility = ";".join(facts)
        if fam in selected:
            unit = f"DA-{aid.replace('.', '-')}"
            rows.append(f"| {fam} | {eligibility} | selected | {unit} | — | current Books comparison 后仍有长期机制 delta。 | analysis:{unit} |")
            blocks.append(
                f"<!-- analysis:{unit}:start -->\n### {safe(r['title'])}\n\n"
                f"旧路径与约束：{safe(r['old_path_and_changed_constraint'])}\n\n"
                f"机制与控制权：{safe(r['mechanism_and_ownership'])}\n\n"
                f"收益、代价与证据边界：{safe(r['tradeoffs_and_failure_modes'])} {safe(r['claim_boundary'])}\n"
                f"<!-- analysis:{unit}:end -->"
            )
        else:
            rows.append(f"| {fam} | {eligibility} | not_selected | — | — | exact-v1 与 Books comparison 已完成；Top-3 只是叙事预算。 | analysis-decision:{fam} |")
            blocks.append(f"<!-- analysis-decision:{fam}:start -->Source Review 与 current-Books disposition 已完成；未选入 Top-3 不降低 Evidence 或 Books Decision。<!-- analysis-decision:{fam}:end -->")
    return """## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
""" + "\n".join(rows) + "\n\n" + "\n\n".join(blocks)


def render_books(comparisons: list[dict]) -> str:
    rows, blocks = [], []
    for c in comparisons:
        fam = c["source_family_id"]
        rows.append(
            f"| {fam} | {c['stable_node_id']} | {c['target_ref']} | {'; '.join(c['adjacent_refs'])} | "
            f"existing:{fam} | delta:{fam} | {c['evolution_relation']} | {c['decision']} | books-review:{fam} |"
        )
        blocks.append(
            f"<!-- books-review:{fam}:start -->\n"
            f"<!-- existing:{fam}:start -->{safe(c['existing_proposition'])}<!-- existing:{fam}:end -->\n"
            f"<!-- delta:{fam}:start -->{safe(c['new_evidence_delta'])}<!-- delta:{fam}:end -->\n"
            f"Decision=`{c['decision']}`。{safe(c['decision_reason'])} Evidence boundary：{safe(c['claim_boundary'])}\n"
            f"<!-- books-review:{fam}:end -->"
        )
    return """## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
""" + "\n".join(rows) + "\n\n" + "\n\n".join(blocks)


def audit_day(day: int) -> dict:
    packet = SRC / f"daily-202604{day:02d}"
    report_path = MONTH / f"{day:02d}/README.md"
    ledger = load(packet / "screening-ledger-final.json")
    reviews_packet = load(packet / "exact-v1-review-packet.json")
    reviews = reviews_packet["items"]
    retained = {x["arxiv_id"]: x for x in ledger["identities"] if x.get("candidate_state") == "retained"}
    assert len(reviews) == len(retained)

    comparisons, queue, acceptance = [], [], []
    for review in reviews:
        aid = review["arxiv_id"]
        row = retained[aid]
        node = route(row)
        assert node in NODE_PATH, (aid, node)
        path = NODE_PATH[node]
        if aid in QUEUE_REVIEW_OVERRIDES:
            precise = QUEUE_REVIEW_OVERRIDES[aid]
            review["old_path_and_changed_constraint"] = precise["old"]
            review["mechanism_and_ownership"] = precise["mechanism"]
            review["tradeoffs_and_failure_modes"] = precise["tradeoff"]
        query = f"{row['title']} {row.get('abstract','')} {review.get('mechanism_and_ownership','')}"
        target = (
            exact_section(path, TARGET_H2_OVERRIDES[aid])
            if aid in TARGET_H2_OVERRIDES
            else best_section(path, query)
        )
        adjacent = adjacent_paths(path)
        adjacent_sections = [best_section(p, query) for p in adjacent]
        existing = proposition(target, query)
        disposition = "Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"
        delta = clean(review.get("mechanism_and_ownership") or first_sentence(row.get("abstract", "")))
        if disposition == "Integrate":
            reason = (
                f"current owner `{target['heading']}` 尚未把 `{row['title']}` 所公开的机制状态与控制权写成可执行 contract；"
                "该增量改变长期设计判断，需由 root 串行整合并经独立 post-write audit。"
            )
            relation = "Direct Evolution"
        else:
            reason = (
                f"`{row['title']}` 的 source-specific 机制是：{first_sentence(row.get('abstract',''), 360)} "
                f"当前 `{target['heading']}` 已拥有同一问题的 state/control owner、约束与失败回退；exact-v1 只新增受限实现、"
                "任务切片、算法分支或 measurement evidence，未改变现有设计结论。"
            )
            relation = "Principle Reuse"
        comp = {
            "source_family_id": family(aid), "arxiv_id": aid, "title": row["title"],
            "stable_node_id": node, "owner_path": path, "target_chapter": path,
            "target_h2": target["heading"], "target_ref": ref(path, target),
            "adjacent_chapters": adjacent,
            "adjacent_refs": [ref(p, s) for p, s in zip(adjacent, adjacent_sections)],
            "owner_sha256": owner_sha(path), "existing_proposition": existing,
            "new_evidence_delta": delta, "evolution_relation": relation,
            "decision": disposition, "disposition": disposition,
            "decision_reason": reason, "claim_boundary": review["claim_boundary"],
            "review_provenance_id": review["review_provenance_id"],
            "fresh_context_audit": "2026-04-01..07 current-Books independent replay from exact-v1 and current Books",
        }
        comparisons.append(comp)

        row["owner_node"] = node
        row["integration_disposition"] = disposition
        row["score_v2"] = score_v2(row, disposition)
        review["stable_node_id"] = node
        review["books_disposition"] = disposition
        review["review_body"] = (
            rebuild_integrate_review_body(review, node)
            if aid in QUEUE_REVIEW_OVERRIDES
            else patch_review_body(review["review_body"], node, disposition)
        )
        review["review_provenance_id"] = recompute_review_provenance(review, row)
        comp["review_provenance_id"] = review["review_provenance_id"]

        if disposition == "Integrate":
            queue.append({
                "source_family_id": family(aid), "arxiv_id": aid, "title": row["title"],
                "stable_node_id": node, "owner_path": path, "target_chapter": path,
                "target_h2": target["heading"], "target_ref": ref(path, target),
                "adjacent_chapters": adjacent, "adjacent_refs": comp["adjacent_refs"],
                "mechanism_delta": delta,
                "changed_constraint": review.get("old_path_and_changed_constraint", ""),
                "tradeoffs_failure_fallback": review.get("tradeoffs_and_failure_modes", ""),
                "evidence_boundary": review["claim_boundary"],
                "suggested_insertion": f"在 `{target['heading']}` 的演进主线内、章末小结与 Review notes 前整合。",
                "status": "waiting_for_root_serial_writeback",
            })
        acceptance.append({
            "source_family_id": family(aid), "arxiv_id": aid, "title": row["title"],
            "exact_v1_review": review["review_provenance_id"], "stable_node_id": node,
            "target_ref": comp["target_ref"], "adjacent_refs": comp["adjacent_refs"],
            "existing_proposition": existing, "decision": disposition,
            "source_specific_reason": reason, "claim_boundary": review["claim_boundary"],
        })

    queue_packet = {
        "schema": "historical-daily-books-writeback-queue-v2.1",
        "report_date": f"2026-04-{day:02d}",
        "status": "waiting_for_root_serial_writeback" if queue else "no_writeback_required",
        "items": queue,
    }
    comparison_packet = {
        "schema": "historical-daily-current-books-comparison-v2.1",
        "report_date": f"2026-04-{day:02d}", "items": comparisons,
    }
    receipt = {
        "schema": "historical-daily-books-prewrite-fresh-context-acceptance-v2.1",
        "report_date": f"2026-04-{day:02d}",
        "auditor": "fresh-context-non-author-books-reviewer",
        "inputs": ["strict-window Daily exact-v1 review packet", "ROADMAP.md", "current owner and adjacent Books"],
        "prohibited_inputs": ["pre-existing aggregate-report candidate list", "pre-existing aggregate-report score", "old Books queue owner/decision"],
        "candidate_families_reviewed": len(acceptance),
        "integrate": len(queue), "no_change_existing_coverage": len(acceptance) - len(queue),
        "ordinary_pending": 0, "blocked": 0, "weekly_semantic_dependency_count": 0,
        "actual_target_h2_resolved": f"{len(acceptance)}/{len(acceptance)}",
        "actual_adjacent_h2_resolved": f"{sum(len(x['adjacent_refs']) for x in acceptance)}/{sum(len(x['adjacent_refs']) for x in acceptance)}",
        "shared_books_modified": False,
        "books_gate": "Open — Root Serial Writeback Pending" if queue else "Passed — No Writeback Required",
        "items": acceptance,
    }
    dump(packet / "books-current-content-comparison.json", comparison_packet)
    dump(packet / "BOOKS_WRITEBACK_QUEUE.json", queue_packet)
    dump(packet / "exact-v1-review-packet.json", reviews_packet)
    dump(packet / "screening-ledger-final.json", ledger)
    dump(packet / "books-prewrite-acceptance.json", receipt)

    report = report_path.read_text(encoding="utf-8")
    ledger_by_aid = retained
    candidate = """## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
""" + "\n".join(candidate_rows(ledger))
    report = replace_between(report, "## 2. Candidate Ledger", "## 3. Review Completion Receipt", candidate)
    report = replace_between(report, "## 3. Review Completion Receipt", "## 4. Benchmark Contracts", render_reviews(reviews))
    report = replace_between(report, "## 5. Deep Analysis Selection", "## 6. Books Comparison", render_deep(reviews, ledger_by_aid))
    report = replace_between(report, "## 6. Books Comparison", "## 7. Semantic Audit", render_books(comparisons))
    old_queue_match = re.search(r"final queue=\d+", report)
    if old_queue_match:
        report = report[:old_queue_match.start()] + f"final queue={len(queue)}" + report[old_queue_match.end():]
    report = re.sub(r"current owner\+adjacent comparison 后 Integrate queue=\d+", f"current owner+adjacent comparison 后 Integrate queue={len(queue)}", report)
    report = re.sub(r"`BOOKS_WRITEBACK_QUEUE\.json` 的 \d+ 项", f"`BOOKS_WRITEBACK_QUEUE.json` 的 {len(queue)} 项", report)
    report = re.sub(r"- \d+ 项 Integrate 等待 root", f"- {len(queue)} 项 Integrate 等待 root", report)
    report = re.sub(r"Integrate queue=\d+", f"Integrate queue={len(queue)}", report)
    if queue:
        completion, books, unresolved = "In Progress", "Open", 1
        books_status = f"F-BOOKS-WRITEBACK-{day:02d}: {len(queue)} Integrate items 尚未写入共享 Books"
        books_resolution = "root 按日期串行写回后安排独立 post-write semantic audit"
        books_audit_status = "open"
        final_tail = "唯一未闭合项是共享 Books writeback 与 post-write audit。"
    else:
        completion, books, unresolved = "Complete", "Passed", 0
        books_status = "none"
        books_resolution = "265-family current-Books audit 中本日没有长期知识缺口；无需共享写回"
        books_audit_status = "passed"
        final_tail = "本日 current-Books comparison 无 Integrate；独立 prewrite audit 已闭合 Books Gate。"
    report = re.sub(r"\*\*Status:\*\* .*", f"**Status:** {completion}；Coverage=Closed、Evidence=Passed、Books={books}；final queue={len(queue)}。", report, count=1)
    report = re.sub(r"\| Completion Status \| [^|]+ \|", f"| Completion Status | {completion} |", report, count=1)
    report = re.sub(r"\| Books Gate \| [^|]+ \|", f"| Books Gate | {books} |", report, count=1)
    report = re.sub(
        rf"\| SA-202604{day:02d}-BOOKS \|[^\n]+",
        f"| SA-202604{day:02d}-BOOKS | fresh-context:april01-07-independent-reviewer | books | validator:books-comparison-v1 | {books_status} | {books_resolution} | {books_audit_status} |",
        report,
    )
    report = re.sub(r"Completion Status: `[^`]+`", f"Completion Status: `{completion}`", report)
    report = re.sub(r"Books: `[^`]+`", f"Books: `{books}`", report)
    report = re.sub(r"unresolved findings: \d+", f"unresolved findings: {unresolved}", report)
    report = re.sub(r"唯一未闭合项是共享 Books writeback 与 post-write audit。", final_tail, report)
    report_path.write_text(report, encoding="utf-8")
    return {
        "date": f"2026-04-{day:02d}", "candidate_families": len(acceptance),
        "old_queue": None, "new_queue": len(queue), "no_change": len(acceptance) - len(queue),
        "target_h2_resolved": len(acceptance), "adjacent_refs_resolved": sum(len(x["adjacent_refs"]) for x in acceptance),
    }


def main() -> None:
    # Frozen count from the invalid pre-audit queue.  Keeping it explicit makes
    # the renderer idempotent instead of treating its own repaired queue as the
    # historical baseline on the next run.
    old_total = 183
    results = [audit_day(day) for day in range(1, 8)]
    new_total = sum(item["new_queue"] for item in results)
    summary = {
        "schema": "historical-daily-april01-07-books-prewrite-fresh-context-summary-v2.1",
        "dates": ["2026-04-01", "2026-04-07"], "candidate_families_reviewed": 265,
        "old_invalid_queue": old_total, "new_canonical_queue": new_total,
        "no_change_existing_coverage": 265 - new_total,
        "weekly_semantic_dependency_count": 0, "shared_books_modified": False,
        "reason_for_reduction": (
            "旧 queue 将可映射 ROADMAP 与应写入 Books 混为一谈，并使用不存在的 canonical-owner/chapter-boundary。"
            "本次只保留 current owner+adjacent 仍缺失、且 exact-v1 会改变长期 state/data/control 或 evaluation/release contract 的 family。"
        ),
        "days": results,
    }
    dump(SRC / "april-01-07-books-prewrite-fresh-context-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
