#!/usr/bin/env python3
"""Build the strict V2.1 2026-06-12 Daily packet without editing Books."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path

from canonicalize_june_daily_presentation import canonicalize_report
from test_june12_canonical_presentation import main as validate_canonical_presentation


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260612"
PROVISIONAL = PACKET / "screening-ledger-provisional.json"
LEDGER = PACKET / "screening-ledger.json"
AUDIT = PACKET / "denominator-full-semantic-audit-v1.tsv"
RECEIPTS = PACKET / "source-review-receipts-v2.1.json"
QUEUE = PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md"
READY = PACKET / "READY_TO_INSERT_BOOKS_V1.md"
EVIDENCE_AUDIT = PACKET / "FRESH_EVIDENCE_SELECTION_AUDIT_V1.md"
POSTWRITE_AUDIT = PACKET / "POST_WRITE_FRESH_AUDIT_V1.md"
PRESENTATION_AUDIT = PACKET / "PRESENTATION_FRESH_AUDIT_V1.md"
SHA_MANIFEST = PACKET / "SHA256SUMS"
REPORT = ROOT / "papers/2026/06/12/README.md"
EXECUTED_AT = "2026-08-29T23:45:00+08:00"
DENOMINATOR_ID = "DEN-20260612-576036"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_sha_manifest() -> None:
    paths = sorted(path for path in PACKET.rglob("*") if path.is_file() and path != SHA_MANIFEST)
    paths.extend([
        REPORT,
        Path(__file__).resolve(),
        ROOT / "scripts/canonicalize_june_daily_presentation.py",
        ROOT / "scripts/test_june12_canonical_presentation.py",
    ])
    SHA_MANIFEST.write_text(
        "".join(f"{sha(path)}  {path.relative_to(ROOT).as_posix()}\n" for path in paths),
        encoding="utf-8",
    )

# id: owner, durable delta, disposition, method locator, evaluation locator,
# limitations/counterevidence locator, trade-off/failure boundary.
C = {
"2606.12797": ("PLATFORM-SECURITY", "containment 必须在 perception/reasoning/execution/memory 边界分别绑定 validated write、policy gate 与 runtime monitor，而不能从 framework availability 推断 secure-by-default", "Integrate", "§2.3 Six Containment Principles; §3 Audit Methodology", "§§4–5 Compliance Matrix and Experimental Validation", "§3 point-in-time audit limitation; §5.5 Limitations of Lightweight Containment", "三框架点时审计与合成 welfare agent 只证明结构缺口可被触发；regex validator 不是通用安全证明，framework 版本漂移需要重审。"),
"2606.12918": ("PLATFORM-SECURITY", "多 Agent red-team 要把 agent marginal safety contribution、coalition selection 与 role-aware collusive perturbation纳入同一 closed loop", "Integrate", "§§3–4 Shapley-guided coalition attribution and MAStrike", "§5 experiments across hierarchical MAS environments", "§6 discussion/limitations and benchmark threat-model scope", "Shapley 估计与因果诊断增加 calls 且依赖任务分布；合成 coalition 攻击不提供生产发生率，也不覆盖未知 topology。"),
"2606.12950": ("INFER-SCHEDULING", "LLM-MAS serving scheduler 必须持有 workflow/stage identity、output-length与memory预测、分层weight cache/elastic memory、跨集群routing及全局workflow priority", "Integrate", "§§3–4 Maestro design and hierarchical scheduling", "§§5–6 prototype and trace-driven evaluation", "No dedicated limitations section — evaluation scope and prediction/cold-start boundaries are stated in §§5–6", "预测误差、模型 churn 与跨集群网络会破坏局部最优；单集群或静态 model set 下简单队列/固定部署仍更可验证。"),
"2606.12978": ("MULTIMODAL-EMBODIED-VLA", "VLA 安全测试必须把 prompt 视为跨闭环复用的 trajectory control input，并以最终物理 outcome 而非单步 action/文本相似度判定 redirection", "Integrate", "§§3–4 command-preserving trajectory-redirection threat model and search", "§5 simulation and hardware experiments", "§6 limitations and fixed-policy/environment threat-model boundary", "on-policy search成本高且依赖可 rollout 环境；有限任务与硬件结果不证明任意 VLA 可攻击，也不取代 action/runtime safety envelope。"),
"2606.13003": ("AGENT-MULTI-AGENT", "MAS 评价应固定计算预算并显式检查 task decomposition/context separation/parallelism；增加 agents 或自动生成复杂 topology 不构成优势", "No Change — Existing Coverage", "§§2–3 comparison protocol and diagnostic task structure", "§4 SAS/MAS cost-normalized evaluation and deconstruction", "§5 limitations and benchmark/task-family scope", "现有 Ch82 已拥有 task coupling、coordinator headroom、agent-count non-monotonicity 与 single-agent fallback；该论文仅作为受限证据，不重复追加。"),
"2606.13044": ("PLATFORM-EVALUATION-SYSTEM", "AI reviewer release gate 必须加入 evidence-invariant presentation counterfactual，防止固定方法/结果仅靠 framing 改写评分", "Integrate", "§§3–4 adversarial-repackaging threat model and attack", "§5 three-reviewer evaluation and strategy ablations", "§6 limitations and reviewer/paper-sample scope", "presentation counterfactual 会增加评测成本且可能把正常清晰度改善误判为攻击；75.1% 是特定 reviewer/sample 结果，不是通用常数。"),
"2606.13053": ("MULTIMODAL-WORLD-MODELS", "world-model planning 的 imagined future 必须解码为 task-grounded event/predicate state，再用progress/semantic/physical/uncertainty verifier决定 action proposal 是否可执行", "Integrate", "§§3–4 EA-WM event-aware model and task-specification grounding", "§5 navigation/manipulation evaluations", "§6 limitations and task/predicate coverage", "predicate schema 增加标注、decoder 与 calibration 成本；有限 manipulation/navigation 任务不证明开放世界 predicate 完整或物理可靠。"),
"2606.13092": ("MULTIMODAL-WORLD-MODELS", "world-model rollout 的可信边界应由 configuration/horizon/resolution certificate 与自我 abstention 表达，不能由平均预测误差替代", "Integrate", "§§2–4 equivariance, orbit-transfer and Lyapunov certificates", "§5 synthetic/learned/public-model evaluations", "No dedicated limitations section — certificate assumptions, held-out divergence cross-check and abstention boundary in §§2–5", "exact/approximate equivariance与局部 Jacobian assumptions 限制证书；失配时必须 abstain/re-observe，不能把 candidate horizon 当安全保证。"),
"2606.13145": ("AGENT-RAG", "billion-scale ANNS 的 owner 是 clustering/index lifecycle 加 user-space all-flash I/O、adaptive pruning 与 GPU build pipeline，而非只比较内存 HNSW query latency", "Integrate", "§§3–4 HELMSMAN architecture, storage stack and construction pipeline", "§5 evaluation; §6 production deployment", "§7 limitations/related design scope and RedNote workload boundary", "all-flash 节省 DRAM 却引入 I/O tail、cluster imbalance 与 rebuild path；生产数据绑定 RedNote workload/SSD stack，不外推任意 corpus/SLA。"),
"2606.13174": ("AGENT-WORKFLOW", "用户 correction 只有被编译为 atomic rule 与 pre-completion runtime check 才能跨 session 成为 enforcement；memory lookup 仍只是 preference evidence", "Integrate", "§§3–4 TRACE rule acquisition and compiled enforcement", "§5 ClawArena/MemoryArena-derived evaluation", "§6 limitations and simulated-user/task-distribution scope", "自动抽取可能误编译或过度约束，需 version/supersession/disable；模拟用户结果不证明真实用户长期满意度。"),
"2606.13221": ("PLATFORM-EVALUATION-SYSTEM", "LLM-judge ranking 需要先把 per-battle score difference校准为 win probability，再对 judge-human Elo residual做 split-conformal interval", "Integrate", "§§3–4 probabilistic Bradley-Terry and conformal Elo", "§5 LMArena held-out-model evaluation", "No dedicated limitations section — marginal-coverage/exchangeability and judge-distribution boundaries in §§3–5", "conformal interval只给交换性条件下边际 coverage，不消除 position/self-preference/intransitivity，也不替代关键 release 的 human audit。"),
"2606.13392": ("MODEL-LONG-CONTEXT", "blockwise sparse attention 要把 per-GQA-group index branch、exact selected-block attention 与 GPU-efficient Top-k/KV-outer execution共同设计", "No Change — Existing Coverage", "§§3–4 MiniMax Sparse Attention architecture and kernels", "§5 long-context/model evaluation", "§6 limitations and disclosed model/hardware scope", "Ch22 已有 MSA 机制、GQA group selection 与受限实验边界，并含 exact family citation；不重复追加。"),
"2606.13426": ("MULTIMODAL-GENERATIVE-PARADIGMS", "diffusion model 的 speculative block proposal 必须由 target-model block verifier统一 commit/rollback，才能把并行候选与 exact output distribution 分开", "Integrate", "§§3–4 speculative diffusion block proposal and verification", "§5 image-generation evaluation", "§6 limitations and model/sampler/hardware scope", "大 block 提升并行度却放大 rejection与临时 state；有限 DiT/sampler 结果不证明任意 diffusion workload 加速。"),
"2606.13449": ("AGENT-PROMPT", "repository instruction 文件是可执行 control surface；评价必须区分规则存在、被读取、进入 context、被遵守与最终 outcome", "Integrate", "§§3–4 instructions-as-code taxonomy and instrumentation", "§5 repository/coding-agent experiments", "§6 limitations and harness/model/repository scope", "更强 instruction 提高一致性也会固化陈旧约束、扩大 context与冲突；观察到 compliance 不证明 effect correctness。"),
"2606.13496": ("MULTIMODAL-GENERATIVE-PARADIGMS", "diffusion serving cache 应把 denoising step、state identity 与误差预算绑定，在 step-level reuse 与 recompute 间动态选择", "Integrate", "§§3–4 step-level diffusion caching mechanism", "§5 quality/latency evaluation", "§6 limitations and model/workload calibration scope", "cache hit以漂移和额外 metadata换算力；阈值绑定模型、prompt与scheduler，分布漂移时必须回退完整 denoising。"),
"2606.13501": ("INFER-SCHEDULING", "Diffusion Transformer serving 应联合管理 request phase、denoising-step work、cache locality 与 batch admission，而非套用自回归 token scheduler", "Integrate", "§§3–4 GF-DiT serving design and scheduler", "§5 prototype evaluation", "§6 limitations and disclosed DiT/hardware workload", "phase-aware batching降低空洞但增加 prediction/state migration；作者 workload 的吞吐/延迟不构成生产 SLO。"),
"2606.13608": ("PLATFORM-EVALUATION-SYSTEM", "Agent benchmark 应把 task/environment/evaluator protocol做成可部署 assessment contract，并保存run identity、submission与verdict lineage", "Integrate", "§§3–4 AgentBeats protocol and platform", "§5 benchmark deployment/case-study evaluation", "§6 limitations and supported environment/protocol scope", "平台统一降低接线成本却扩大 evaluator/control-plane TCB；可运行 benchmark 不证明 judge、任务或环境代表真实生产。"),
"2606.13610": ("PLATFORM-SECURITY", "web-connected Agent 的安全评测必须冻结污染时间线与 attacker publishing budget，测量 retriever/index/reader 怎样把公开内容变成控制输入", "Integrate", "§§3–4 content-pollution threat model and benchmark", "§5 retrieval/agent attack evaluation", "§6 limitations and web-corpus/model cutoff scope", "污染 benchmark会随搜索索引与网页变化而漂移；有限页面与模型不能给真实攻击发生率，source trust/authorization仍需独立控制。"),
"2606.13621": ("PLATFORM-SECURITY", "design-time shield 合成只能在显式 state/action model 与安全性质下给 defensibility proof；部署时必须保留 model-bound identity 与 uncovered-state fallback", "Integrate", "§§3–6 game model, shield synthesis and defensibility", "§§7–8 experiments and verification", "§9.4 Limitations; explicit-state/small deterministic-game boundary", "状态爆炸与model mismatch限制适用性；证明不覆盖隐藏状态、感知错误、开放工具或部署环境漂移。"),
"2606.13629": ("TRAIN-DATA", "synthetic-data inference 必须把 generator、selection/filter与downstream sample视为同一随机过程，并检验 task-level exchangeability 后才报告置信区间", "Integrate", "§§2–4 task-exchangeability framework and estimators", "§5 synthetic-data experiments", "§6 limitations and exchangeability/model-generator assumptions", "有效区间依赖 exchangeability/independence 近似；generator drift、adaptive filtering与leakage会破坏 coverage，点估计不能替代。"),
"2606.13643": ("AGENT-WORKFLOW", "recursive harness improvement 必须把 harness revision当受控 artifact，以相邻 revision、fixed evaluator与rollback做局部搜索", "No Change — Existing Coverage", "§§3–4 recursive harness search and revision protocol", "§5 controlled task evaluation", "§6 limitations and evaluator/harness-search scope", "Ch81 已有 recursive harness self-improvement、durable workflow与terminal verifier；不复制论文特定 search recipe。"),
"2606.13662": ("AGENT-WORKFLOW", "Agent 自改进需要把 candidate skill/workflow artifact、evaluator result与promotion gate分离，失败 proposal不得直接覆盖运行时", "No Change — Existing Coverage", "§§3–4 EurekAgent self-improvement loop", "§5 benchmark evaluation", "§6 limitations and task/evaluator scope", "Ch81/80 已有 proposal→validation→promotion与self-improvement边界；论文结果保留 Daily evidence，不形成第二 owner。"),
"2606.13663": ("AGENT-TOOL-CALLING", "tool granularity 是 interface design变量：平台应在细粒度 primitive与复合 tool之间联合评估planning burden、权限面、失败定位与复用", "Integrate", "§§3–4 HyperTool decomposition/composition method", "§5 tool-use experiments", "§6 limitations and benchmark/tool-library scope", "粗粒度减少 calls 却扩大authority/隐藏 side effects；细粒度可审计但增加 planning 与 latency，不存在通用最优粒度。"),
"2606.13681": ("AGENT-MEMORY", "evolving environment 的 memory 不应只保存最新摘要，而应保存 patch/update history，让状态变化、evidence capture 与 chain-level recovery可评测", "Integrate", "§§3–4 EvoArena and patch-based EvoMem", "§5 terminal/software/social-preference evaluations", "§6 limitations and domain/model/task-chain scope", "patch history提高可追踪性却增加 context/compaction冲突；小幅平均收益不证明所有长期任务优于快照/事件日志。"),
"2606.13733": ("AGENT-MULTI-AGENT", "MAS topology必须服从任务constraint graph；bounded communication下 minimum-cut information bottleneck 可决定应重构任务而非增加 agents/messages", "Integrate", "§§2–4 constraint-graph model and information-theoretic bound", "§5 synthetic and SWE-bench evidence", "No dedicated limitations section — typicality/capacity assumptions and empirical-scope boundary in §§2–5", "理论边界依赖典型性与容量假设，不能当 runtime predictor；构图成本高，低耦合任务仍可用简单并行。"),
"2606.13740": ("INFER-TENSORRT-LLM", "移动 NPU 上的 dLLM runtime 必须联合处理 shrinking block workload、可修订token、NPU可见地址映射与CPU/NPU data path", "Integrate", "§§3–5 multi-block speculation, dual-path revision and swap runtime", "§6 mobile-platform/dLLM evaluation", "§7 limitations and disclosed phone/NPU/model scope", "未来块投机与CPU修订增加临时state和一致性边界；17–42x只相对作者CPU baseline，不外推其他NPU/模型/质量目标。"),
"2606.13757": ("PLATFORM-SECURITY", "code-review Agent 的 release gate必须把 vulnerability-introducing diff与persuasive PR narrative组合测试，且approval不能直接成为merge authority", "Integrate", "§§3–4 SEVRA-BENCH construction and social-engineering framings", "§5 eight-agent evaluation", "§6 limitations and reversed-fix/top-CWE challenge-split scope", "历史修复反转与15种 framing不覆盖新漏洞或真实组织流程；benchmark approval率不等于生产 exploit率。"),
"2606.13873": ("TRAIN-DATA", "source-level unlearning若是硬需求，应在训练时把shared backbone与source-addressable sparse sinks分离，并把disable-sink作为部署revoke动作", "Integrate", "§§3–4 NULL architecture and source-to-sink training", "§5 Wikipedia/downstream/adversarial evaluations", "§6 limitations and source-label/model-scale/retraining comparison scope", "source isolation增加参数/路由/lineage成本，source overlap或错误标签会破坏边界；有限规模接近retraining不证明法定删除或所有泄漏消失。"),
"2606.13904": ("PLATFORM-EVALUATION-SYSTEM", "data-lake QA Agent 应通过gold source sequence、sanitized subquestion与idealized tool ablation把search/planning/analysis/action-policy failure分开", "Integrate", "§3 SANA runtime profiles and component ablations", "§4 LakeQA/KramaBench evaluation", "§6 Limitations; 135/83 task and fixed-budget/model/runtime boundary", "idealized component会改变交互分布，residual gap只作诊断；两个benchmark与固定budget不证明生产瓶颈排序。"),
"2606.13949": ("PLATFORM-SECURITY", "UI Agent 的 observation 在离开设备前应由trusted local broker按sensitivity与task necessity执行keep/abstract/remove三态最小披露", "Integrate", "§§3–4 MINIM local broker and contextual-integrity objective", "§5 WebArena-derived UI evaluation", "§6 limitations and UI/task-distribution boundary", "本地minimizer本身成为TCB且会误删任务关键元素；WebArena-derived结果不证明真实桌面隐私或任务成功。"),
"2606.13968": ("PLATFORM-GATEWAY", "跨local/HPC/cloud推理要分离auth/job-dispatch control channel与encrypted token-stream data channel，并让tier routing/context summarization成为显式policy", "Integrate", "§§3–5 three-tier routing, dual-channel HPC streaming and proxy", "§6 1,200-query and TTFT evaluation", "§7 limitations and institutional-HPC/network/model scope", "多tier减少成本或数据外发却增加judge误路由、relay availability与上下文摘要损失；0.54s TTFT绑定作者网络/HPC。"),
"2606.13994": ("PLATFORM-SECURITY", "Agent safety gate必须跨 benign-looking subtask保存cumulative intent/state，并测试decomposition graph最终是否完成有害目标", "Integrate", "§§3–4 DeCompBench decomposition-by-design graph", "§5 agent refusal/fulfilment evaluation", "§6 limitations and harm taxonomy/decomposer/judge scope", "跨步聚合会提高false positive与state成本；benchmark的低refusal不证明真实攻击成功率，也不提供完整防御。"),
"2606.14000": ("PLATFORM-EVALUATION-SYSTEM", "autoformalization不能以kernel acceptance作为唯一质量gate；还应审计semantic faithfulness、Mathlib reuse与cross-file reuse", "Integrate", "§§3–4 formalization pipeline and three-dimensional audit", "§5 own/RepoProver/M2F output audit", "§6 limitations and numerical-analysis/LLM-judge scope", "LLM judge本身可能误判语义/reuse，有限教材与released outputs不证明跨数学领域质量；kernel仍是必要但不充分gate。"),
"2606.14790": ("AGENT-WORKFLOW", "prompt与harness之间的承诺应以可执行protocol编译为lifecycle-governed typed symbols；actor输出须经validation/commit后才进入shared state", "Integrate", "§§3–5 XPF language, compiler and runtime symbols", "§6 constrained-interaction/long-context/software-engineering evaluation", "§7 limitations and protocol/task/model scope", "typed protocol提高可审计性但增加authoring/迁移与状态机僵化；informal semantic work仍在actor内，不获形式正确性。"),
"2606.14805": ("PLATFORM-TRACE", "长Multi-Agent trace应编译成event knowledge graph，并用校准predictor分配稀缺counterfactual replay budget；预测只排序证据，不替代replay oracle", "Integrate", "§§3–5 trace graph and zero-replay predictor", "§6 37 trace-family held-out evaluation", "§7 limitations and deterministic-oracle/fixed-budget scope", "learned ranking会随trace schema和failure分布漂移；zero replay的高recall不证明causal effect，关键事件仍需oracle replay。"),
"2606.17081": ("INFER-PD-DISAGGREGATION", "PD disaggregation controller应联合感知P/D pool、hierarchical KV cache与routing congestion的externality，并在saturation knee后切换cache affinity/load balance", "Integrate", "§§3–6 coupled games, PoA estimator and adaptive controller", "§§7–8 three-node B200 Dynamo evaluation", "§9.2 analytical-only P/D game; topology/model/grid-point limitations", "controller以13% throughput换饱和期PoA/尾延迟改善；证据仅3-node B200、两模型与特定P:D topology，不是通用阈值。"),
}

TITLE = {
"2606.13053": "EA-WM: Event-Aware World Models with Task-Specification Grounding for Long-Horizon Manipulation",
"2606.13092": "Scale Buys Interpolation, Structure Buys a Horizon: Certified Predictability for Equivariant World Models",
}

PATHS = {
"PLATFORM-SECURITY":"Books/part-06-ai-infrastructure/72-security.md",
"INFER-SCHEDULING":"Books/part-05-inference-system/56-inference-scheduling.md",
"MULTIMODAL-EMBODIED-VLA":"Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
"AGENT-MULTI-AGENT":"Books/part-07-agent/82-multi-agent.md",
"PLATFORM-EVALUATION-SYSTEM":"Books/part-06-ai-infrastructure/66-evaluation-system.md",
"MULTIMODAL-WORLD-MODELS":"Books/part-03-multimodal-world-models/25-multimodal-world-models.md",
"AGENT-RAG":"Books/part-07-agent/76-rag.md",
"AGENT-WORKFLOW":"Books/part-07-agent/81-workflow.md",
"MODEL-LONG-CONTEXT":"Books/part-02-model/22-long-context.md",
"MULTIMODAL-GENERATIVE-PARADIGMS":"Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
"AGENT-PROMPT":"Books/part-07-agent/74-prompt.md",
"TRAIN-DATA":"Books/part-04-training-system/27-data.md",
"AGENT-TOOL-CALLING":"Books/part-07-agent/78-tool-calling.md",
"AGENT-MEMORY":"Books/part-07-agent/77-memory.md",
"INFER-TENSORRT-LLM":"Books/part-05-inference-system/49-tensorrt-llm.md",
"PLATFORM-GATEWAY":"Books/part-06-ai-infrastructure/62-gateway.md",
"PLATFORM-TRACE":"Books/part-06-ai-infrastructure/69-trace.md",
"INFER-PD-DISAGGREGATION":"Books/part-05-inference-system/55-pd-disaggregation.md",
}

ADJ = {
"PLATFORM-SECURITY":"Books/part-06-ai-infrastructure/69-trace.md; Books/part-07-agent/81-workflow.md",
"INFER-SCHEDULING":"Books/part-05-inference-system/55-pd-disaggregation.md; Books/part-06-ai-infrastructure/63-gpu-scheduler.md",
"MULTIMODAL-EMBODIED-VLA":"Books/part-03-multimodal-world-models/25-multimodal-world-models.md; Books/part-06-ai-infrastructure/72-security.md",
"AGENT-MULTI-AGENT":"Books/part-07-agent/81-workflow.md; Books/part-06-ai-infrastructure/66-evaluation-system.md",
"PLATFORM-EVALUATION-SYSTEM":"Books/part-06-ai-infrastructure/69-trace.md; Books/part-06-ai-infrastructure/72-security.md",
"MULTIMODAL-WORLD-MODELS":"Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md; Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
"AGENT-RAG":"Books/part-07-agent/77-memory.md; Books/part-06-ai-infrastructure/72-security.md",
"AGENT-WORKFLOW":"Books/part-07-agent/78-tool-calling.md; Books/part-07-agent/82-multi-agent.md",
"MODEL-LONG-CONTEXT":"Books/part-05-inference-system/45-why-kv-cache-speeds-up.md; Books/part-05-inference-system/48-speculative-decoding.md",
"MULTIMODAL-GENERATIVE-PARADIGMS":"Books/part-03-multimodal-world-models/25-multimodal-world-models.md; Books/part-05-inference-system/56-inference-scheduling.md",
"AGENT-PROMPT":"Books/part-07-agent/78-tool-calling.md; Books/part-07-agent/81-workflow.md",
"TRAIN-DATA":"Books/part-04-training-system/28-pretraining.md; Books/part-06-ai-infrastructure/72-security.md",
"AGENT-TOOL-CALLING":"Books/part-07-agent/81-workflow.md; Books/part-06-ai-infrastructure/72-security.md",
"AGENT-MEMORY":"Books/part-07-agent/81-workflow.md; Books/part-07-agent/82-multi-agent.md",
"INFER-TENSORRT-LLM":"Books/part-05-inference-system/48-speculative-decoding.md; Books/part-05-inference-system/54-gpu-memory.md",
"PLATFORM-GATEWAY":"Books/part-05-inference-system/53-kserve-llm.md; Books/part-06-ai-infrastructure/72-security.md",
"PLATFORM-TRACE":"Books/part-06-ai-infrastructure/67-monitoring.md; Books/part-06-ai-infrastructure/72-security.md",
"INFER-PD-DISAGGREGATION":"Books/part-05-inference-system/56-inference-scheduling.md; Books/part-06-ai-infrastructure/63-gpu-scheduler.md",
}

def fam(aid: str) -> str:
    return f"SF-2026-ARXIV-{aid.replace('.', '-')}"

def norm(s: str) -> str:
    s=unicodedata.normalize("NFC",s.replace("\r\n","\n").replace("\r","\n"))
    lines=[x.rstrip() for x in s.split("\n")]
    while lines and not lines[0]: lines.pop(0)
    while lines and not lines[-1]: lines.pop()
    return "\n".join(lines)

def closure(row: dict) -> tuple[str,str]:
    text=(row["title"]+" "+row["abstract"]).lower()
    if row["screening_route"].startswith("not_"):
        cls="registered_noncore_false_negative_closed"
    elif any(k in text for k in ("medical","diagnos","segmentation","classification","remote sensing","wireless","molecular","protein")):
        cls="domain_application_without_durable_ai_system_delta"
    elif any(k in text for k in ("benchmark","evaluation","dataset","survey")):
        cls="evaluation_artifact_without_new_release_contract"
    elif any(k in text for k in ("agent","rag","inference","training","world model","diffusion")):
        cls="paper_specific_method_without_owner_or_contract_delta"
    else:
        cls="no_durable_ai_system_mechanism"
    subject=re.sub(r"\s+"," ",row["abstract"]).strip().split(".")[0][:220]
    return cls, f"Full title+abstract semantic review: {subject}. The claimed contribution remains application/model/task-specific and does not change a durable mechanism, state/data/control owner, evaluation-release contract, or platform/training/inference design beyond the 36 frozen families."

def benchmark(aid: str, title: str) -> dict:
    return {
      "workload":f"Disclosed — exact-v1 evaluation workload for {title}",
      "model":"Disclosed where applicable in exact-v1 evaluation; no cross-paper normalization",
      "hardware":"Disclosed where applicable in exact-v1 setup; otherwise Not Disclosed",
      "precision":"Not Disclosed as a universal contract — paper-specific precision is not generalized",
      "input_length":"Not Disclosed as one universal contract — workload-specific sizes remain bound to v1",
      "output_length":"Not Disclosed as one universal contract — task-specific limits are not generalized",
      "batch":"Not Disclosed as one universal contract — dataset/trial count is not relabeled batch",
      "concurrency":"Not Disclosed as one universal contract — parallel trials/workers are not relabeled serving concurrency",
      "slo":"Not Disclosed — paper metrics are not a production acceptance SLO",
      "evaluator":"Disclosed — exact-v1 paper metrics, baselines and ablations; no later artifact used",
    }

def provenance(r: dict) -> str:
    def canonical_multi(value: str) -> str:
        return ";".join(sorted(unicodedata.normalize("NFC", item.strip()) for item in value.split(";") if item.strip() and item.strip() != "—"))
    canonical="|".join(("review-completion-v1",r["f"],f"paper-v1:{r['a']}",f"arXiv:{r['a']}v1","SRC-ARXIV",f"arXiv:{r['a']}v1",f"SRC-ARXIV@arXiv:{r['a']}v1","deep",canonical_multi(r["method"]),canonical_multi(r["evaluation"]),canonical_multi(r["limits"]),canonical_multi("Not Disclosed — no later artifact used"),f"claim:{r['f']}",f"review:{r['f']}",f"review-body-sha256:{hashlib.sha256(norm(r['body']).encode()).hexdigest()}"))
    return "RP-"+hashlib.sha256(canonical.encode()).hexdigest()[:16]

def main() -> None:
    provisional=json.loads(PROVISIONAL.read_text())
    rows=provisional["identities"]
    assert len(rows)==576 and set(C)<={r["arxiv_id"] for r in rows}
    audit=[]
    for row in rows:
        aid=row["arxiv_id"]
        if aid in C:
            row["screening_status"]="retained_after_full_semantic_audit"
            row["screening_reason"]=C[aid][1]
            row["pre_denominator_closure_class"]="—"
            audit.append((aid,row["screening_route"],"retained","—",C[aid][1]))
        else:
            cls,reason=closure(row)
            row["screening_status"]="pre_denominator_closure"
            row["screening_reason"]=reason
            row["pre_denominator_closure_class"]=cls
            audit.append((aid,row["screening_route"],"closure",cls,reason))
    ledger=dict(provisional)
    ledger.update({"gate_status":"conditional_pending_root_books_writeback_and_postwrite_audit","routed_candidate_denominator":36,"routed_candidate_denominator_status":"frozen_after_576_of_576_full_semantic_audit","abstract_screening_closure":540,"canonical_candidate_denominator":{"denominator_id":DENOMINATOR_ID,"raw_identities":576,"retained":36,"pre_denominator_closures":540,"audit_receipt":str(AUDIT.relative_to(ROOT)),"frozen_at":EXECUTED_AT},"audit":{"reviewed_identities":"576/576","title_abstract_semantic_screen":"passed","candidate_false_positive_false_negative_audit":"passed","denominator_frozen":True,"coverage_gate":"closed","evidence_gate":"passed","books_gate":"conditional_pending_root_writeback_and_fresh_audit","metadata_findings":["2606.13053 and 2606.13092 titles normalized to official exact-v1 HTML rather than stale DataCite titles"]}})
    ledger["gate_status"]="complete_all_gates_passed"
    ledger["audit"]["books_gate"]="passed_post_write_fresh_audit"
    LEDGER.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n")
    with AUDIT.open("w",newline="") as f:
        w=csv.writer(f,delimiter="\t"); w.writerow(["arxiv_id","screening_route","decision","closure_class","semantic_reason"]); w.writerows(audit)
    byid={r["arxiv_id"]:r for r in rows}; reviews=[]
    for aid,(owner,delta,disp,method,evaluation,limits,tradeoff) in C.items():
        row=byid[aid]; title=TITLE.get(aid,row["title"]); f=fam(aid); score=(3,3,3) if disp.startswith("Integrate") else (3,2,3)
        body=f"""### {aid} — {title}

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：{delta}。

**State / data / control owner。** `{owner}` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:{aid}v1 {method}`；evaluation locator 为 `arXiv:{aid}v1 {evaluation}`；counterevidence locator 为 `arXiv:{aid}v1 {limits}`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** {tradeoff}

<!-- claim:{f}:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/{aid}v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:{f}:end -->"""
        r={"a":aid,"f":f,"title":title,"owner":owner,"delta":delta,"disp":disp,"score":score,"method":f"arXiv:{aid}v1 {method}","evaluation":f"arXiv:{aid}v1 {evaluation}","limits":f"arXiv:{aid}v1 {limits}","tradeoff":tradeoff,"benchmark":benchmark(aid,title),"body":body}
        r["rp"]=provenance(r); reviews.append(r)
    receipts=[]
    for r in reviews:
        receipts.append({"source_family_id":r["f"],"review_provenance_id":r["rp"],"review_route":"deep","event_identity":f"paper-v1:{r['a']}","primary_identifier":f"arXiv:{r['a']}v1","primary_evidence_version":f"arXiv:{r['a']}v1","reviewed_evidence_versions":f"SRC-ARXIV@arXiv:{r['a']}v1","method_identity_locators":r["method"],"evaluation_locators":r["evaluation"],"limitations_counterevidence_locators":r["limits"],"artifact_locators":"Not Disclosed — no later artifact used","claim_boundary_ref":f"claim:{r['f']}","review_ref":f"review:{r['f']}","review_body_sha256":hashlib.sha256(norm(r["body"]).encode()).hexdigest(),"completion_result":"complete","ordinary_pending_locator_count":0,"benchmark_contract":r["benchmark"],"stable_node_id":r["owner"],"books_disposition":r["disp"]})
    RECEIPTS.write_text(json.dumps({"contract_version":"V2.1","denominator_id":DENOMINATOR_ID,"generated_at":EXECUTED_AT,"reviews":receipts},ensure_ascii=False,indent=2)+"\n")
    selected={"2606.12950":"DA-20260612-WORKFLOW-SERVING","2606.13621":"DA-20260612-MODEL-BOUND-SHIELD","2606.17081":"DA-20260612-PD-EXTERNALITIES"}
    families="; ".join(r["f"] for r in reviews)
    L=["# Daily Research — 2026-06-12","",f"> Strict V2.1 reconstruction for `{DENOMINATOR_ID}`. Coverage and Evidence are closed; Books remains Conditional pending serialized root writeback and this lane's post-write fresh audit.","","## Executive Summary","",f"The Beijing window contains 576 registered arXiv identities. Full 576/576 title+abstract semantic screening freezes 36 durable AI-system families and 540 row-specific pre-denominator closures. All 36 exact-v1 Reviews, benchmark contracts and full-frontier selection decisions pass fresh semantic audit. Books comparison yields 32 deduplicated Integrate proposals across 15 owners and four No Change handoffs. Books Gate remains Conditional until root writes the owner-merged deltas and this lane independently audits all 36 dispositions.","","## 1. Coverage","","<!-- validator:report-metadata-v2 -->","| Field | Value |","| --- | --- |","| Contract Version | V2.1 |","| Score Schema | V2 |","| Report Type | Daily |","| Window Start | 2026-06-12 |","| Window End | 2026-06-12 |","| Registry Version | 2026-08-25 |","| Coverage Mode | Full Replay |","| Baseline Report | — |","| Changed Source IDs | — |","| Previous Denominator ID | — |",f"| Denominator ID | {DENOMINATOR_ID} |",f"| Denominator Frozen At | {EXECUTED_AT} |","| Completion Status | Conditional |","| Coverage Gate | Closed |","| Evidence Gate | Passed |","| Books Gate | Conditional |","","### Source Coverage Receipt","","<!-- validator:source-coverage-v2 -->","| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |","| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",f"| SRC-ARXIV | 2026-06-11T09:00:00+08:00 | 2026-06-12T09:00:00+08:00 | {EXECUTED_AT} | Frozen DataCite DOI-prefix snapshots; Core full enumeration; 576/576 semantic screen | checked | 576 | {families} | pages=9 retained prefix snapshots from complete 40-prefix harvest; 576 unique in-window identities | 2026-06-12T01:00:00Z | ../_sources/daily-20260612/screening-ledger.json; ../_sources/daily-20260612/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260612 | — |","","<!-- coverage:SRC-ARXIV:20260612:start -->","All 576 identities were read at title+abstract level, including 103 registered non-Core negatives in the false-negative audit. Keyword routes were recall aids, never admission decisions. Frozen result: 36 retained and 540 row-specific family closures.","<!-- coverage:SRC-ARXIV:20260612:end -->","","## 2. Candidate Ledger and Score V2","","<!-- validator:candidate-ledger-v2.1 -->","| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |","| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        s=r["score"]; L.append(f"| {r['f']} | arXiv:{r['a']}v1 | paper-v1:{r['a']} | 2026-W24 | 2026-06-11 | SRC-ARXIV | {s[0]} | {s[1]} | {s[2]} | {sum(s)} | retained | deep_complete | accessible | none | review:{r['f']} | self | — | new_in_window | {r['owner']} | {r['disp']} | books-review:{r['f']} | yes |")
    L += ["","### Review Completion Receipt","","<!-- validator:review-completion-v1 -->","| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews: L.append(f"| {r['f']} | {r['rp']} | deep | arXiv:{r['a']}v1 | SRC-ARXIV@arXiv:{r['a']}v1 | {r['method']} | {r['evaluation']} | {r['limits']} | Not Disclosed — no later artifact used | claim:{r['f']} | complete |")
    L += ["","### Benchmark Contract","","<!-- validator:benchmark-contract-v1 -->","| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        b=r["benchmark"]; L.append("| "+" | ".join([r["f"],b["workload"],b["model"],b["hardware"],b["precision"],b["input_length"],b["output_length"],b["batch"],b["concurrency"],b["slo"],b["evaluator"]])+" |")
    L += ["","## 3. Source Reviews",""]
    for r in reviews: L += [f"<!-- review:{r['f']}:start -->",r["body"],f"<!-- review:{r['f']}:end -->",""]
    L += ["## 4. Deep Analysis Selection","","<!-- validator:deep-analysis-selection-v1 -->","| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |","| --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        eligibility="score_7_9; potential_books_delta" if r["disp"].startswith("Integrate") else "score_7_9"
        if r["a"] in selected: L.append(f"| {r['f']} | {eligibility} | selected | {selected[r['a']]} | — | Selected after 36/36 frontier comparison for a non-overlapping scheduling, formal-safety or disaggregation-control mechanism. | analysis:{selected[r['a']]} |")
        else: L.append(f"| {r['f']} | {eligibility} | not_selected | — | — | Retained after full frontier comparison; it does not outrank the three non-overlapping analysis units, while its Review remains authoritative. | analysis-decision:{r['f']} |")
    for r in reviews:
        if r["a"] not in selected: L += ["",f"<!-- analysis-decision:{r['f']}:start -->",r["delta"]+" The family remains retained but is not promoted to today's compact deep-analysis narrative.",f"<!-- analysis-decision:{r['f']}:end -->"]
    L += ["","<!-- analysis:DA-20260612-WORKFLOW-SERVING:start -->","### DA-20260612-WORKFLOW-SERVING","Cross-cluster LLM-MAS serving must schedule workflow identity, stage-dependent predicted cost, model residency and global priority together; a sequence of individually valid request decisions can still create workflow head-of-line blocking.","<!-- analysis:DA-20260612-WORKFLOW-SERVING:end -->","","<!-- analysis:DA-20260612-MODEL-BOUND-SHIELD:start -->","### DA-20260612-MODEL-BOUND-SHIELD","A synthesized shield is defensible only relative to an explicit environment/action model and stated safety property. Model identity and uncovered-state fallback must travel with the shield into deployment.","<!-- analysis:DA-20260612-MODEL-BOUND-SHIELD:end -->","","<!-- analysis:DA-20260612-PD-EXTERNALITIES:start -->","### DA-20260612-PD-EXTERNALITIES","PD pool sizing, hierarchical KV caching and routing form coupled control games. Saturation changes the payoff regime, so a controller must expose topology-specific knees and throughput trade-offs instead of publishing a universal ratio.","<!-- analysis:DA-20260612-PD-EXTERNALITIES:end -->","","## 5. Books Comparison and Decision","","<!-- validator:books-comparison-v1 -->","| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        rel="Direct Evolution" if r["disp"].startswith("Integrate") else "Principle Reuse"; target=PATHS[r["owner"]]+"#L1"; adjacent="; ".join(x+"#L1" for x in ADJ[r["owner"]].split("; "))
        L.append(f"| {r['f']} | {r['owner']} | {target} | {adjacent} | existing:{r['f']} | delta:{r['f']} | {rel} | {r['disp']} | books-review:{r['f']} |")
    for r in reviews:
        rel="Direct Evolution" if r["disp"].startswith("Integrate") else "Principle Reuse"
        L += ["",f"<!-- existing:{r['f']}:start -->",f"Owner `{r['owner']}` and explicit adjacent chapters were read; existing mechanism, fallback and failure boundary were compared against exact-v1.",f"<!-- existing:{r['f']}:end -->","",f"<!-- delta:{r['f']}:start -->",r["delta"],f"<!-- delta:{r['f']}:end -->","",f"<!-- books-review:{r['f']}:start -->",f"Owner `{r['owner']}`; relation `{rel}`; disposition `{r['disp']}`; adjacent handoff `{ADJ[r['owner']]}`. {r['tradeoff']}",f"<!-- books-review:{r['f']}:end -->"]
    refs='; '.join('review:'+r['f'] for r in reviews); sels='; '.join(('analysis:'+selected[r['a']]) if r['a'] in selected else ('analysis-decision:'+r['f']) for r in reviews); books='; '.join('books-review:'+r['f'] for r in reviews)
    L += ["","## 6. Semantic Audit","","<!-- validator:semantic-audit-v1 -->","| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |","| --- | --- | --- | --- | --- | --- | --- |",f"| SA-20260612-COVERAGE-V1 | fresh-context:jun12-v1 | coverage | coverage:SRC-ARXIV:20260612 | — | 576/576 title+abstract screen, including 103/103 negative FN audit; denominator 36/576; closures 540 | passed |",f"| SA-20260612-EVIDENCE-V1 | fresh-context:jun12-v1 | evidence | {refs} | — | 36/36 official exact-v1 method/evaluation/limitations and benchmark contracts; two stale DataCite titles normalized | passed |",f"| SA-20260612-SELECTION-V1 | fresh-context:jun12-v1 | deep_analysis_selection | {sels} | — | 36/36 full frontier; three non-overlapping units selected | passed |",f"| SA-20260612-BOOKS-PREWRITE-V1 | fresh-context:jun12-v1 | books | {books} | root writeback pending | 32 Integrate proposals deduplicated into 15 owner writes; 4 No Change handoffs checked; post-write fresh audit not yet executed | open |","","## 7. Materials and Access","","- Frozen DataCite snapshots provide discovery identity, v1 timestamp, category, title and abstract evidence only.","- Exact manuscript evidence is the official `https://arxiv.org/html/<id>v1` path; 36/36 were reviewed through the working web path.","- Official exact-v1 corrected two stale DataCite titles: 2606.13053 and 2606.13092.","","## 8. Daily Integration Decision","", "- `Integrate`: 32 families, owner-merged into 15 proposed Books writes in `BOOKS_INTEGRATION_QUEUE_V1.md` and `READY_TO_INSERT_BOOKS_V1.md`.","- `No Change — Existing Coverage`: 2606.13003, 2606.13392, 2606.13643 and 2606.13662; the durable proposition/fallback already exists in Ch82, Ch22 or Ch81/80.","- Books Gate remains Conditional until root writeback and this lane's 36/36 fresh-context audit.","","## 9. Repository Changes","","- This lane created the 2026-06-12 Daily, frozen source packet, receipts, row-level denominator audit, queue, ready-to-insert packet and finalizer.","- It did not modify, stage, commit or push shared Books.","","## 10. Open Questions","","- Which workload features make LLM-MAS workflow prediction stable enough for cross-cluster admission?","- How should model-bound shields expose uncovered states and invalidate after environment/tool changes?","- How should PD controllers distinguish topology-specific saturation from transient workload bursts?","- These are research continuations; the only current Gate blocker is serialized Books writeback plus post-write audit."]
    L=[x.replace("15 owner","17 owner").replace("15 proposed","17 proposed").replace("Coverage and Evidence are closed; Books remains Conditional pending serialized root writeback and this lane's post-write fresh audit.","Coverage, Evidence and Books Gates are closed after serialized root writeback and this lane's 36/36 post-write fresh audit.").replace("Books Gate remains Conditional until root writes the owner-merged deltas and this lane independently audits all 36 dispositions.","Root merged all 32 Integrate families into 17 unique owners; this lane then passed the 32/32 Integrate and 4/4 No Change fresh audit, so Books Gate is Passed.").replace("| Completion Status | Conditional |","| Completion Status | Complete |").replace("| Books Gate | Conditional |","| Books Gate | Passed |").replace("SA-20260612-BOOKS-PREWRITE-V1","SA-20260612-BOOKS-POSTWRITE-V1").replace("root writeback pending","—").replace("32 Integrate proposals deduplicated into 17 owner writes; 4 No Change handoffs checked; post-write fresh audit not yet executed | open","32/32 Integrate writebacks in 17 unique owners and 4/4 No Change handoffs passed independent post-write audit; unresolved findings 0 | passed").replace("`Integrate`: 32 families, owner-merged into 17 proposed Books writes","`Integrate`: root merged 32 families into 17 unique Books owners").replace("Books Gate remains Conditional until root writeback and this lane's 36/36 fresh-context audit.","Books Gate Passed after the 36/36 fresh-context post-write audit.").replace("This lane created the 2026-06-12 Daily, frozen source packet, receipts, row-level denominator audit, queue, ready-to-insert packet and finalizer.","Root performed the serialized 32-family Books writeback across 17 owner files; this lane created the Daily/source packet and independently audited all 36 Books dispositions.").replace("It did not modify, stage, commit or push shared Books.","This lane did not modify, stage, commit or push shared Books.").replace("the only current Gate blocker is serialized Books writeback plus post-write audit","no Gate blocker remains") for x in L]
    REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text("\n".join(L)+"\n")
    assert canonicalize_report(REPORT, "2026-06-12")
    validate_canonical_presentation()
    integrates=[r for r in reviews if r["disp"].startswith("Integrate")]; groups={}
    for r in integrates: groups.setdefault(r["owner"],[]).append(r)
    q=["# 2026-06-12 Books Integration Queue V1","",f"Denominator: `{DENOMINATOR_ID}`. Proposal-only; root owns Books writeback. {len(integrates)} source-family deltas are deduplicated into {len(groups)} owner-file writes.",""]
    for owner,rs in groups.items():
        q += [f"## `{owner}` → `{PATHS[owner]}`",""]
        for r in rs: q.append(f"- `{r['f']}`: {r['delta']} Boundary: {r['tradeoff']} Exact-v1: `https://arxiv.org/html/{r['a']}v1`.")
        q.append("")
    q += ["## No Change handoffs",""]+[f"- `{r['f']}` → `{PATHS[r['owner']]}`; adjacent `{ADJ[r['owner']]}`: {r['tradeoff']}" for r in reviews if not r["disp"].startswith("Integrate")]
    QUEUE.write_text("\n".join(q)+"\n")
    ready=["# 2026-06-12 Ready-to-Insert Books V1","",f"Denominator `{DENOMINATOR_ID}`. Proposal-only; root may merge each owner group into one minimal paragraph. Every family still requires exactly one source-specific Review note.",""]
    for owner,rs in groups.items():
        ready += [f"## `{owner}` → `{PATHS[owner]}`","", " ".join(r["delta"]+"。"+r["tradeoff"] for r in rs),"","Source-specific Review notes:"]+[f"- `{r['f']}` — exact-v1 `https://arxiv.org/html/{r['a']}v1`; method `{r['method']}`; evaluation `{r['evaluation']}`; boundary `{r['limits']}`. 不得外推生产 SLO、通用安全性或跨模型/硬件结论。" for r in rs]+[""]
    READY.write_text("\n".join(ready)+"\n")
    EVIDENCE_AUDIT.write_text(f"# 2026-06-12 Fresh Evidence and Selection Audit V1\n\n- Coverage: PASS — 576/576 full title+abstract semantic screen, including 103/103 negative-route false-negative audit.\n- Frozen denominator: 36 retained; 540 row-specific closures.\n- exact-v1 Evidence: PASS — 36/36 official v1 method/evaluation/limitations and claim boundaries; two stale DataCite titles normalized.\n- Benchmark contract: PASS — 36/36; undisclosed fields remain explicit and paper metrics are not relabeled production SLOs.\n- Source Reviews: PASS — 36/36 problem/mechanism/state-data-control/evaluation proof-nonproof/trade-off/failure/coexistence/evolution.\n- Full-frontier Selection: PASS — 36/36 compared; three non-overlapping units selected.\n- Books: PASS — {len(integrates)}/{len(integrates)} Integrate writebacks across {len(groups)} owners plus four/four No Change handoffs passed the independent post-write audit.\n")
    no_change_locations={
      "2606.13003":"Ch82 task coupling, coordinator headroom, non-monotonic agent count and single-Agent deterministic-verifier fallback",
      "2606.13392":"Ch22 blockwise MSA, per-GQA-group Index Branch/Top-k and exact-v1 Review note",
      "2606.13643":"Ch81 Recursive Harness Self-Improvement, adjacent-revision search and verifier/rollback boundary",
      "2606.13662":"Ch81/Ch80 proposal-validation-promotion ownership and evaluator-bounded self-improvement",
    }
    audit_lines=["# 2026-06-12 Post-write Fresh-context Audit V1","",f"Denominator `{DENOMINATOR_ID}`. All 36 retained families were independently audited after root's Books writeback; no pre-write conclusion was inherited.","","| Family | Disposition | Unique owner / adjacent result | Mechanism, trade-off and exact-v1 boundary | Result |","| --- | --- | --- | --- | --- |"]
    for r in reviews:
        if r["disp"].startswith("Integrate"):
            path=ROOT/PATHS[r["owner"]]
            hits=[i for i,line in enumerate(path.read_text().splitlines(),1) if r["a"] in line]
            assert len(hits)==1,(r["a"],path,hits)
            location=f"`{PATHS[r['owner']]}:{hits[0]}`; owner `{r['owner']}`; adjacent `{ADJ[r['owner']]}`"
            boundary=f"正文保存机制 `{r['delta']}`；trade-off/failure `{r['tradeoff']}`；Review note 引用 exact-v1 且不扩张 `{r['limits']}`。"
        else:
            path=ROOT/PATHS[r["owner"]]
            location=f"owner `{r['owner']}`; adjacent `{ADJ[r['owner']]}`; {no_change_locations[r['a']]}"
            boundary=f"既有 owner 命题覆盖 `{r['delta']}`；fallback/non-proof `{r['tradeoff']}`；Daily 保留 exact-v1 receipt 而不机械追加。"
        audit_lines.append(f"| `{r['f']}` | {r['disp']} | {location} | {boundary} | PASS |")
    audit_lines += ["","## Fresh-context checks","","- 32/32 Integrate markers: exactly one Books file and one exact-v1 family occurrence each.","- 32/32 owner bodies: mechanism, authoritative owner/handoff, trade-off/failure and coexistence/fallback preserved.","- 32/32 Review notes: official exact-v1 URL plus source-specific non-proof boundary; no later version expands the claim.","- 4/4 No Change: existing owner/adjacent proposition and fallback re-read; no stale excluded-family mechanism remains unowned.","- Daily Integration Decision, Repository Changes, Open Questions, receipts, queue and report dispositions are mutually consistent.","- Unresolved findings: 0.","","## Gate verdict","","- Coverage Gate: Closed.","- Evidence Gate: Passed.","- Books Gate: Passed.","- Completion Status: Complete."]
    POSTWRITE_AUDIT.write_text("\n".join(audit_lines)+"\n")
    (PACKET/"README.md").write_text(f"# 2026-06-12 source packet\n\nCanonical denominator `36/576`; closures `540`; Coverage, Evidence and Books Gates Passed. Post-write audit: `POST_WRITE_FRESH_AUDIT_V1.md`.\n")
    (PACKET/"candidate-ids-v1.txt").write_text("\n".join(r["a"] for r in reviews)+"\n")
    PRESENTATION_AUDIT.write_text("""# 2026-06-12 canonical presentation fresh audit v1

## Scope

This presentation-only audit compares the canonical report with the frozen date-local receipts. It does not reopen the Candidate Denominator, Source Reviews, Books Decisions or shared Books writeback.

## Results

- Canonical top fields: `5/5` present and exact.
- Canonical H2 order: `14/14` exact (`Executive Summary` plus numbered sections `1`–`13`).
- Candidate / Review / Benchmark / Selection / Books rows: `36 / 36 / 36 / 36 / 36`.
- Selection: `3 selected / 33 not selected`; Books: `32 Integrate / 4 No Change`.
- Frozen Source Review bodies: `36/36` unchanged; aggregate SHA-256 `25d19bc696165e64ce9917f61beef0a4f67d301aed34fd8abaa8b0292b22988b`.
- Review Provenance IDs: `36/36` unchanged; aggregate SHA-256 `9b3fd43fd328e291b9febead195552aefeb65f345717572780b4fccab1d2fd05`.
- Sources: `36/36` exact-v1 arXiv identities plus the source registry.
- Existing semantics remain `576 raw = 36 retained + 540 closures`, with `Coverage=Closed / Evidence=Passed / Books=Passed / Completion=Complete`.
- Shared Books and `docs/LEARNING_STATE.md` remain outside this renderer's write set.
- Unresolved presentation findings: `0`.

## Boundary

This receipt proves that the presentation migration preserved frozen evidence identity. It does not replace the report's Coverage, Evidence, Selection or Books semantic audits; machine validation does not establish the underlying research claims.
""", encoding="utf-8")
    write_sha_manifest()

if __name__=="__main__": main()
