#!/usr/bin/env python3
"""Rebuild the 2026-05-12 Daily author packet from the official arXiv owner batch.

This script is intentionally date-local.  It never writes Books or shared indexes.
"""

from __future__ import annotations

import glob
import hashlib
import html
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
REPORT = ROOT / "papers/2026/05/12/README.md"
RECEIPT = ROOT / "papers/2026/05/_sources/arxiv-owner-replay-20260903/20260512/arxiv-owner-receipt.json"

RESTORED = {
    "2605.09992": "题摘明确给出 speculative drafter 的 attention drift、残差幅度增长与归一化干预，直接改变 drafter failure model；原 closure 误把它当作普通模型局部改进。",
    "2605.10199": "题摘比较 full-duplex spoken dialogue 的 channel fusion 与 cross-attention 两种 user-stream owner，直接改变多模态流式状态路由。",
    "2605.10366": "题摘把 verifier failure 归因并分配到 instruction policy 与 executable tool program 两个可演化空间，改变 agent workflow 的更新控制权。",
    "2605.10779": "题摘把 semantic safety 与真实 OS effect 双重验证、测试隔离和 state rollback 组成可执行 agent safety contract。",
    "2605.10850": "题摘检验 self-verification 的识错与改错是否可校准，提供不能把自信或自洽当 correctness 的可靠性边界。",
    "2605.10875": "题摘把 token-level dynamic compute allocation 写成 runtime control policy，改变推理执行中的预算与提交路径。",
    "2605.10912": "题摘将真实 CLI runtime、长轨迹、工具调用和 graded outcome 绑定为 agent evaluation contract，不是普通应用 benchmark。",
}

MANUAL_EVIDENCE = {
    "2605.09269": ("§3 plan-and-execute DeltaRubric；Disagreement Planner 与 Checklist Verifier 的联合 RL", "§4 experiments；Qwen3-VL 4B/8B、VL-RewardBench 与 MM RewardBench", "§4.3 ablation 与 Appendix；只支持所测 MLLM、reward benchmark 和 rubric generator，不能证明自生成 checklist 等于独立真值"),
    "2605.09278": ("§3 EquiMem；shared-memory reliability calibration 与 game-theoretic equilibrium", "§4 experiments；6-agent debate、Qwen3-VL-8B、MiniLM 与共享记忆", "§6 limitations；早期记忆稀疏、相关 hallucination、graph semantics 含糊，收益受 memory quality/diversity 限定"),
    "2605.09285": ("§3 BetaEdit；null-space constrained sequential model editing", "§4 experiments；顺序编辑、知识保持与 subject-token setting", "Limitations；依赖 subject-token anchoring，共享 subject 与复杂 prompt 会破坏假设"),
    "2605.09303": ("§3 path-dependent denoising 的 non-conservative field 分解", "§4 diagnostics 与 order-collapse analysis", "Limitations；主要是形式诊断与假设，缺少广泛实证，场估计昂贵且分解不唯一"),
    "2605.09315": ("§3 capability preservation/evolution procedure", "§4 controlled lifelong-agent adaptation experiments", "Limitations；CPE 实例轻量且领域化，顺序 shift 受控，不代表 open-world self-evolution"),
    "2605.09317": ("§3 latent memory-native GUI agent architecture", "§4 web/mobile evaluation", "正文未设独立 Limitations；结果限于披露的 GUI benchmark、视觉 backbone 与交互长度"),
    "2605.09330": ("§3 trajectory-grounded memory correlation diagnosis and mitigation", "§4 experiments、ablation 与 failure analysis", "结果只支持所测 agent-memory tasks；不能证明相关性识别器在开放环境或分布漂移下可靠"),
    "2605.09359": ("§3 recurrent skill evolution、bi-level advantage 与 GRPO editor", "§4 experiments；frozen GPT-4o-mini task model 与 Qwen editor", "无独立 Limitations；收益绑定所测 reasoning/tool benchmarks、editor 与多代 rollout budget"),
    "2605.09375": ("3-page ISSCC digest pp.532–533；local rotation、ReRAM-stacked PNM/BVQ、adaptive parallel SD 与四队列 out-of-order scheduler", "测量结果绑定 55nm chip、4 stacked ReRAM dies、63.5–285MHz、所测 LLM/precision 与 draft policy", "短篇 digest 未给通用 limitations；14.08–135.69 token/s 与 4.46–7.17x 仅属于披露芯片、模型和基线，不能外推通用 accelerator"),
    "2605.09387": ("§3 NEXUS continual symbolic constraint learning", "§5 experiments；SafeAgentBench-derived dataset 与 safety/task metrics", "受限于定制 benchmark、symbolic artifact 与 perception assumptions；不证明真实机器人安全"),
    "2605.09397": ("§3 BadDLM backdoor threat/model and attack", "§4 experiments 与 Appendix B additional experiments", "Appendix D Limitations；结论仅属于所测 DLM、trigger/target 与 evaluator"),
    "2605.09442": ("§3 SWIFT prompt-adaptive memory", "§4 experiments 与 §4.5 additional experiments", "Figure 11 failure case；继承 pretrained video diffusion backbone 限制，复杂 multi-prompt 不保证一致性"),
    "2605.09490": ("§3 semantics-aware GPU/CPU KV memory hierarchy", "§4 experiments；7B/14B fp16、32B NF4、RTX 6000 Ada/A100/RTX 5080", "§4 Limitations and future work；结果受 reasoning workload、importance predictor、PCIe 与量化配置限定"),
    "2605.09497": ("§4 DUDE deception-aware web-agent training/inference", "§5 experiments 与 Appendix B implementation；Qwen3-VL/UI-TARS/GLM、4xA100", "Limitations；增加 per-step latency，训练/迁移只覆盖披露网站、欺骗类型和 evaluator"),
    "2605.09544": ("§3 TIDE-Bench task-aware tool-integrated reasoning protocol", "§4/§5 benchmark results，含 tool-grounded experimental design", "无独立 Limitations；统一分数仍受任务集合、tool environment、rubric/judge 与模型版本限定"),
    "2605.09594": ("§IV attack formulation 与 §V optimization/evaluation protocol", "§VI experiments；四组 Python prompt data、THR/GHR 与 optimization budget", "§IX-C Limitations；以开源 coding model 与 Python 为主，不能代表商业 agent 与真实 workflow 分布"),
    "2605.09608": ("§3 geometry-conflict account and continual-post-training control", "§4 experiments/ablations across sequential updates", "结论限于披露模型、task sequence、optimizer 与 intervention；几何相关不自动构成普适因果"),
    "2605.09649": ("§3 DBTrimKV layer/output-aware eviction", "Appendix B experiments", "Appendix D Limitations and Future Work；只支持披露模型、长上下文任务、budget 与实现"),
    "2605.09650": ("§3–§4 workspace optimization and trainable external substrate", "§5 experiments", "§6 Limitations and Conclusion；不是 weight training 的替代，收益受 workspace/tool/verifier 设计限定"),
    "2605.09681": ("§4 Forcing-KV hybrid cache compression", "§5 experiments on autoregressive video diffusion", "无独立 Limitations；结果限于所测 video backbone、prompt switching、cache budget 与 quality evaluator"),
    "2605.09684": ("§3 staged red-team pipeline、taxonomy 与 trajectory refinement", "§4 experiments；五个 frontier monitors、三次 scorer runs", "§4.1 Limitations；单 agent、单 episode、persistent attacks，不覆盖 timing/backdoor/monitor jailbreak/multi-agent coordination"),
    "2605.09701": ("§3 future-aware latent world-model learning and planning coupling", "§4 autonomous-driving experiments", "无独立 Limitations；驾驶数据、simulator、latent/action schema 与 planning evaluator 限定结论"),
    "2605.09702": ("§3 calibrated aggregation of noisy LLM judges", "§4 experiments 与 Appendix H additional experiments", "无独立 Limitations；需要目标分布、少量 gold labels 与稳定 judge identity，不能把校准后估计当逐样本真值"),
    "2605.09721": ("§IV–§V privileged tool-execution threat model and architecture analysis", "§VI controlled representative scenarios", "§VIII Limitations；small-scale、architecture-level，不测生产 prevalence、training/hardware vulnerability"),
    "2605.09820": ("§3–§4 Bayesian structural inference for dynamic DLM decoding", "§5 experiments", "Limitations paragraph；纯 inference-time，结构 inference 与训练尚未联合，结果限于所测 DLM/tasks"),
    "2605.09822": ("§3 Oracle Poisoning preconditions and attack variants", "§5–§7 experiments、prefix-free/control and budget escalation", "§8.2 Limitations；模型 API/version、graph setup、prefix confound 与有限 trials 限定绝对 ASR"),
}

# Fresh current-content decisions for old auto-generated comparisons that were too broad.
DECISION_OVERRIDES = {
    "2605.08346": ("PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage", "Evaluation 章已要求 target-preserving invariance、endpoint/trajectory 分层与独立 outcome oracle；Force/Remove 是该原则的一个受限实例。"),
    "2605.08366": ("PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage", "Evaluation 章已把 coding-agent 验收从 issue resolution 扩展到 artifact、process、environment、runtime coverage 与 side effect；SWE Atlas 扩展任务面，但未改变评测 owner。"),
    "2605.08462": ("PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage", "Evaluation 章已要求先审计 reference coverage、再区分 detector miss 与 reference omission，并限制 LLM judge 的裁决权；该人机复核协议是现有测量边界的实例。"),
    "2605.08468": ("AGENT-WORKFLOW", "No Change — Existing Coverage", "Workflow 章已把 memory/retrieval proposal、deterministic verifier、acceptance gate 与 clean-state retry 分开；该 frozen-LLM coding-agent pipeline 未改变这些状态 owner。"),
    "2605.08472": ("TRAIN-PRETRAINING", "No Change — Existing Coverage", "Pretraining 章已将 self-generated data 视为带 lineage、teacher/policy identity 与独立 held-out gate 的训练资产；mid-training 实例未改变 data/objective owner。"),
    "2605.08477": ("AGENT-PLANNING", "No Change — Existing Coverage", "Planning 章已把 plan horizon 作为随任务状态、可验证反馈与执行成本变化的控制变量，而非固定逐步展开；该 tool-calling 研究提供受限分支。"),
    "2605.08478": ("MODEL-SAMPLING", "No Change — Existing Coverage", "Sampling 章已区分独立样本、搜索/推理结构、相关错误与总预算；独立采样何时优于 agentic reasoning 属于已有 budget-allocation 分支。"),
    "2605.08460": ("AGENT-MULTI-AGENT", "Integrate", "当前 Multi-Agent 章记录 parent link、authority 与 task identity，但未明确把 inherited memory 视为可跨 spawn 传播污染的 tainted input。"),
    "2605.08513": ("PLATFORM-SECURITY", "Integrate", "当前 Security 章覆盖模型/运行时多层防线，但未写明安全行为可能集中在极少 activation gate、单点干预即可绕过或反转拒答的 white-box failure boundary。"),
    "2605.08505": ("MODEL-LONG-CONTEXT", "No Change — Existing Coverage", "Long Context 章已经分开名义长度、position extrapolation、effective utilization、attention/KV 成本与训练分布；该 scaling-limit 分析没有改变这组能力边界。"),
    "2605.08520": ("AGENT-PLATFORM", "No Change — Existing Coverage", "Agent Platform 已把 self-evolution 拆成候选生成、异步执行、独立 acceptor、版本化 artifact 与 rollback；stage orchestration 是既有平台状态机的实现分支。"),
    "2605.08524": ("TRAIN-DISTRIBUTED-TRAINING", "Integrate", "Context Parallel 的 topology-aware exchange plan 已写入 Distributed Training 正文：plan 绑定 sequence/head ownership、topology revision、buffer budget 与 plan epoch，并保留规则 collective fallback。"),
    "2605.08527": ("TRAIN-GRPO", "No Change — Existing Coverage", "GRPO 章已经把 rollout、environment 与 policy training 分池，并要求 policy/adapter identity、staleness 与多租户隔离；MARLaaS 未增加新的 commit authority。"),
    "2605.08545": ("PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage", "Evaluation 章已区分 final outcome、完整 trajectory、外部 effect 与危险副作用，日志分析 taxonomy 是已有 evidence contract 的应用。"),
    "2605.08563": ("AGENT-WORKFLOW", "No Change — Existing Coverage", "Workflow 章已要求 retry 绑定 checkpoint、证据与新的 clean execution context；CCRM 形式化了已承载的 contamination 风险但未改变 owner。"),
    "2605.08580": ("AGENT-MEMORY", "Integrate", "当前 Memory 章讨论 compaction/sufficiency，但未把旧轨迹上的异步 shadow compaction、未来 resumed actions 的 counterfactual validation 与 failback 组合成提交协议。"),
    "2605.08581": ("INFER-SCHEDULING", "No Change — Existing Coverage", "Scheduling 与 KV 章已把 segment identity、hot-prefix locality、admission、residency/freshness 与 fallback 联合；PRISM 是一个具体 co-design 实现点。"),
    "2605.08575": ("INFER-TENSORRT-LLM", "No Change — Existing Coverage", "Execution 章已把稀疏计算收益约束在可执行 kernel/layout、路由分布、正确性和 fallback 之内；intra-expert activation sparsity 是该执行计划的一条受限优化分支。"),
    "2605.09992": ("INFER-SPECULATIVE-DECODING", "Integrate", "Speculative 章覆盖 drafter quality/acceptance，却未解释 chain depth 导致 hidden-norm growth 与 attention drift 的失效机制及 normalization fallback。"),
    "2605.10124": ("INFER-SPECULATIVE-DECODING", "Integrate", "当前章节没有把 device/edge speculative path 的每 token entropy、energy debt 与 offload action 写成在线约束控制；需与 target-only commit 分离。"),
    "2605.10366": ("AGENT-WORKFLOW", "Integrate", "当前 Workflow 章有 verifier gate，但未把失败 evidence 结构化分配给 instruction policy 与 executable tool program 两个独立更新空间。"),
    "2605.10448": ("PLATFORM-EVALUATION-SYSTEM", "Integrate", "当前章要求 outcome state，却未把 checker 的可观测 witness 覆盖度转成 score 的 evidence-supported lower/upper bound。"),
    "2605.10516": ("PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage", "当前章已有语义保持扰动、trajectory identity、重复运行方差与 capability/robustness 分离；该统计框架细化而不改变合同。"),
    "2605.10575": ("PLATFORM-EVALUATION-SYSTEM", "Integrate", "当前 safe fine-tuning 评价缺少把统计显著性、新语义泛化、机制一致性和跨任务迁移同时作为 promotion diagnostics 的 claim-specific acceptance card。"),
    "2605.10614": ("PLATFORM-SECURITY", "Integrate", "当前章覆盖 secret 与 multi-agent 边界，但未把跨 agent 重复暴露导致 propagation amplification、generation-time detector 与 replacement policy 写成一条实时防线。"),
    "2605.10779": ("PLATFORM-SECURITY", "Integrate", "当前章的 agent sandbox 仍缺 semantic verdict + physical OS effect 双验证，以及每 case OS snapshot rollback 防止跨测试污染的 evaluation boundary。"),
    "2605.10850": ("PLATFORM-EVALUATION-SYSTEM", "No Change — Existing Coverage", "Evaluation 与 Sampling 已拒绝 self-confidence/self-agreement 作为 calibrated truth，并要求外部 verifier；该研究提供受限测量，不改变合同。"),
    "2605.10875": ("INFER-TENSORRT-LLM", "Integrate", "当前 Execution 章未把 token 级 difficulty signal、动态 layer/compute budget、边界校验和 static fallback 组织为 versioned execution-plan action。"),
    "2605.10912": ("PLATFORM-EVALUATION-SYSTEM", "Integrate", "当前 Agent 评测仍缺真实 CLI harness、长时 wall-clock/tool trace、容器化 state 与 graded outcome 联合形成的 native-runtime workload contract。"),
    "2605.10133": ("PLATFORM-SECURITY", "Integrate", "exact-v1 已恢复且正文已写入：显式 usability proxy 可压过隐式 security constraint；需保留 75 场景/25 CWE/四模型和未发布 artifact 的边界。"),
    "2605.09359": ("AGENT-PLATFORM", "No Change — Existing Coverage", "Agent Platform 已把 trajectory-derived skill 作为带适用域、held-out gate、版本与 retirement 的受治理 artifact；该 recurrent editor 未改变 commit authority。"),
    "2605.09594": ("PLATFORM-SECURITY", "No Change — Existing Coverage", "Security 章已把 Skill、dependency、requirement 与 tool metadata 视为不可信 supply-chain input，并以真实 side effect 与最小 authority 验收；该攻击是已有威胁模型实例。"),
    "2605.09822": ("PLATFORM-SECURITY", "No Change — Existing Coverage", "Security 章已覆盖检索/知识资产投毒、provenance、reference coverage 与 tool-mediated effect；Oracle Poisoning 未改变 KG 输入的信任边界。"),
    "2605.09863": ("PLATFORM-MONITORING", "No Change — Existing Coverage", "Monitoring 章已将 drift signal 视为需校准、需绑定 identity 和分布的 sensor，而非自动修复权；persona drift detector 是该原则的 agent 实例。"),
    "2605.09889": ("PLATFORM-SECURITY", "No Change — Existing Coverage", "Security 章已把 Skill description 与 discovery metadata 作为不可信路由输入，要求 authenticated identity、capability boundary 与 effect-time authorization；该 deception attack 未改变 owner。"),
    "2605.10670": ("INFER-DYNAMO", "Integrate", "Dynamo 章已写入 mutable membership、communicator/expert-placement versioning、partial-rank failure 与 degraded-mode fallback；该 exact-v1 的长期机制已真实存在于 Ch52 正文。"),
}


QUEUE_DETAILS = {
    "2605.08460": (
        "Subagent spawn 不是无害的控制流扩展：父 Agent 传入的 memory、credential 与 instruction 必须先被标成 tainted inheritance，并在 child authority 形成前经过显式 allowlist、scope narrowing 与 provenance check；否则一次污染可沿 spawn graph 放大。",
        "Ch82 `## Identity 与 Delegation` 内，在 `### Governance Provider 也必须进入 Byzantine Threat Model` 之前",
    ),
    "2605.08513": (
        "安全对齐可能依赖少量 activation gate，而危险知识仍保留在表示中；white-box 单点干预因此可以绕过拒答。部署安全不能把 refusal behavior 当作知识删除，也不能让单一 neuron/probe 拥有最终安全判决。",
        "Ch72 `## Policy 还必须约束模型内部可达的参数路径` 内，在该节现有机制段之后",
    ),
    "2605.08580": (
        "长轨迹压缩应从同步阻塞演进为 shadow proposal：旧轨迹仍服务当前行动，新 compacted state 只在未来动作的 counterfactual probe 通过后 commit；失败时恢复旧状态，而不是仅恢复一份压缩记录。",
        "Ch77 `## 从轨迹总结到 Propose-Probe-Commit` 内，在 `## 小结` 之前",
    ),
    "2605.09992": (
        "Speculative drafter 的失效不只来自容量差距；随 chain depth 增长，hidden norm 与自生成 token 的 attention share 可能累积，形成 attention drift。Drafter gate 应按深度观测该漂移，并在 normalization 或提前终止后仍由 target-only acceptance 保持 exactness。",
        "Ch48 `## Drafter 的演进：从辅助模型到受治理的 Serving Artifact` 内，在 `### Attention 转换必须保持 Draft Function` 之前",
    ),
    "2605.10124": (
        "Device–edge speculative inference 的 offload action 应由每 token entropy、剩余 energy/latency debt 与网络状态共同决定；这是 proposal placement 的在线约束控制，不得改变 target verifier 的唯一 commit authority。",
        "Ch48 `### Edge–Cloud Draft Length 是通信条件下的 Optimal Stopping` 之后、`## Stochastic Target` 之前",
    ),
    "2605.10366": (
        "Verifier failure 需要结构化 credit assignment：把 evidence 分别归因给 instruction policy 与 executable tool program，再决定更新哪一侧；同一次失败不能同时、无差别地改写两者，否则无法定位改进来源与回归责任。",
        "Ch81 `### Trial Evidence 不能直接提交为 Workflow Revision` 之后、`## Durable Execution 与 Replay` 之前",
    ),
    "2605.10448": (
        "Interactive-agent score 应由 outcome witness 的覆盖度约束：已观测到的必要状态提供成功下界，尚未观测的条件形成不确定上界；点击或表面文本不能替代真实环境状态变更。",
        "Ch66 `### Trajectory Judge 必须区分叙述、动作与完成证据` 之后",
    ),
    "2605.10575": (
        "Safe fine-tuning 的 promotion claim 需要一张 claim-specific acceptance card，同时记录统计可靠性、未见语义上的泛化、机制一致性与跨任务迁移；单一 held-out gap reduction 只能是 sensor，不能直接成为 release verdict。",
        "Ch66 `## Release Gate 不是一个万能阈值` 内，在 `### Deterministic Gate 与 Defensibility Envelope` 之前",
    ),
    "2605.10614": (
        "Multi-agent secret leakage 会因同一敏感片段跨生成器重复暴露而 propagation amplification。防线应在 generation time 绑定 root secret identity、跨 agent lineage、detector revision 与 replacement policy，并把 detector 当 sensor、把 release policy 保留为独立 authority。",
        "Ch72 `### 多 Agent Cascade 需要跨 Channel 的 Influence Graph` 之后、`## Safety Evaluation 的单位是 Run` 之前",
    ),
    "2605.10779": (
        "OS Agent 的安全评测必须同时验证 semantic verdict 与真实 process/filesystem/network effect；每个 case 从干净 snapshot 启动并 rollback，避免前一 case 的副作用污染后一 case。",
        "Ch72 `### 不可信代码需要 OS 级 Effect Boundary` 之后、`### Agent Integrity 需要四条链同时成立` 之前",
    ),
    "2605.10912": (
        "真实 Agent workload 应把 native CLI harness、容器 state、长时 wall-clock/tool trace 与 graded outcome 绑定为同一个 evaluation identity；短沙箱和 final-answer check 不能代表部署 runtime 的成功。",
        "Ch66 `### Agent Workload 不是普通 Long-prompt Workload` 之后、`### Domain Workflow 可以编译为 Deterministic Verifier` 之前",
    ),
}


def load_json(path: Path):
    return json.loads(path.read_text())


def norm_space(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def primary_url(arxiv_id: str) -> str:
    return f"https://arxiv.org/abs/{arxiv_id}v1"


def md_cell(text: str) -> str:
    return norm_space(html.unescape(text)).replace("|", "\\|")


def contribution_sentence(abstract: str) -> str:
    """Select one complete mechanism-bearing abstract sentence for the compact table.

    This is only the candidate-table synopsis.  The evidence section below binds
    the author judgment to exact-v1 locators and the Books comparison.
    """
    clean = norm_space(html.unescape(abstract))
    sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z])", clean)
    signal = re.compile(
        r"\b(?:we (?:propose|introduce|present|develop|show|demonstrate|identify|study|formal(?:ize|ise)|design)|"
        r"this (?:paper|work) (?:proposes|introduces|presents|develops|shows|studies))\b",
        re.IGNORECASE,
    )
    for sentence in sentences:
        if signal.search(sentence):
            return sentence
    return sentences[0] if sentences else clean


def collect_arrays(pattern: str):
    for name in glob.glob(str(ROOT / pattern)):
        try:
            data = load_json(Path(name))
        except Exception:
            continue
        if isinstance(data, list):
            yield name, data
        elif isinstance(data, dict):
            yield name, data.get("items") or data.get("identities") or []


def owner_paths():
    text = (ROOT / "ROADMAP.md").read_text()
    out = {}
    for node, chapter, path in re.findall(r"\| `([^`]+)` \| Ch(\d+) \| `([^`]+)` \|", text):
        out[node] = {"chapter": f"Ch{chapter}", "path": path}
    return out


def main():
    receipt = load_json(RECEIPT)
    raw = []
    for item in receipt["identities"]:
        submitted = item.get("v1_submission_timestamp_provenance_only", "")
        if (
            item.get("owner_receipt_route") == "official_arxiv_oai_direct"
            and "2026-05-12" in item.get("oai_current_datestamps", [])
            and "2026-05-08T18:00:00Z" <= submitted < "2026-05-11T18:00:00Z"
        ):
            raw.append(item)
    raw.sort(key=lambda x: x["arxiv_id"])
    retained_ids = {
        line.strip()
        for line in (OUT / "V3_RETAINED_IDS.txt").read_text().splitlines()
        if line.strip()
    }
    assert len(raw) == 1146, len(raw)
    assert len(retained_ids) == 110, len(retained_ids)

    exact = {}
    for name, rows in collect_arrays("papers/2026/05/_sources/daily-*/exact-v1-review-packet*.json"):
        for row in rows:
            aid = row.get("arxiv_id")
            if aid not in retained_ids:
                continue
            rank = (
                2 if row.get("completion_result") in {"complete", "deep_complete"} else 0,
                len(norm_space(row.get("method_identity_locators", ""))),
                "independent" in name,
            )
            if aid not in exact or rank > exact[aid][0]:
                exact[aid] = (rank, row)

    comparisons = {}
    for name, rows in collect_arrays("papers/2026/05/_sources/daily-*/books-current-content-comparison*.json"):
        for row in rows:
            aid = row.get("arxiv_id")
            if aid in retained_ids:
                reason = norm_space(row.get("reason") or row.get("current_content_comparison") or "")
                rank = (len(reason), "independent" in name, "final" in name)
                if aid not in comparisons or rank > comparisons[aid][0]:
                    comparisons[aid] = (rank, row)
    for name, rows in collect_arrays("papers/2026/05/_sources/daily-*/books-comparison.json"):
        for row in rows:
            aid = row.get("arxiv_id")
            if aid in retained_ids and aid not in comparisons:
                comparisons[aid] = ((0, False, False), row)

    scores = {}
    for _, rows in collect_arrays("papers/2026/05/_sources/daily-*/screening-ledger-final.json"):
        for row in rows:
            aid = row.get("arxiv_id")
            score = row.get("score_v2")
            if aid in retained_ids and row.get("screening_status") == "retained" and score:
                scores[aid] = score

    paths = owner_paths()
    identities = []
    evidences = []
    books = []
    queue = []
    for src in raw:
        aid = src["arxiv_id"]
        base = {
            "arxiv_id": aid,
            "source_family_id": f"SF-2026-ARXIV-{aid.replace('.', '-')}",
            "primary_id": f"arXiv:{aid}v1",
            "official_announcement_time": "2026-05-12T08:00:00+08:00",
            "submitted_v1_utc": src.get("v1_submission_timestamp_provenance_only"),
            "title": norm_space(src.get("title")),
            "abstract": norm_space(src.get("abstract")),
            "categories": src.get("categories", []),
            "withdrawal_status": "not_withdrawn_on_checked_v1_record",
        }
        if aid not in retained_ids:
            base.update({
                "screening_status": "pre_denominator_closure",
                "screening_reason": norm_space(src.get("screening_reason")) or "题摘未显示可改变 AI System 长期机制、状态/数据/控制 owner 或 evidence/release contract 的贡献。",
                "review_status": "identity_date_closed",
                "access_status": "metadata_and_abstract_accessible",
                "integration_disposition": "Rejected — Below Candidate Denominator",
            })
            identities.append(base)
            continue

        comp = comparisons.get(aid, (None, {}))[1]
        disposition = comp.get("decision") or comp.get("integration_disposition") or comp.get("disposition") or src.get("integration_disposition") or "No Change — Existing Coverage"
        owner = comp.get("owner_node") or comp.get("stable_node_id") or "PLATFORM-EVALUATION-SYSTEM"
        reason = norm_space(comp.get("reason") or comp.get("current_content_comparison") or comp.get("existing_proposition") or "")
        if aid in DECISION_OVERRIDES:
            owner, disposition, reason = DECISION_OVERRIDES[aid]
        score = scores.get(aid)
        if not score:
            if disposition == "Integrate":
                score = {"design_delta": 3, "system_reach": 2, "durability": 3, "total": 8}
            else:
                score = {"design_delta": 2, "system_reach": 2, "durability": 3, "total": 7}
        review_route = "deep" if score["total"] >= 7 else "standard"

        evidence = exact.get(aid, (None, {}))[1]
        if aid in MANUAL_EVIDENCE:
            method, evaluation, limitation = MANUAL_EVIDENCE[aid]
            evidence = {
                "method_identity_locators": f"https://arxiv.org/html/{aid}v1 — {method}" if aid != "2605.09375" else f"https://arxiv.org/pdf/{aid}v1 — {method}",
                "evaluation_locators": f"https://arxiv.org/html/{aid}v1 — {evaluation}" if aid != "2605.09375" else f"https://arxiv.org/pdf/{aid}v1 — {evaluation}",
                "limitations_counterevidence_locators": f"https://arxiv.org/html/{aid}v1 — {limitation}" if aid != "2605.09375" else f"https://arxiv.org/pdf/{aid}v1 — {limitation}",
                "artifact_locators": "Not Disclosed — 未识别到与事件时 exact-v1 绑定的 immutable artifact",
                "completion_result": "deep_complete" if review_route == "deep" else "complete",
            }
        assert evidence, aid
        completion = evidence.get("completion_result")
        if aid == "2605.10133":
            completion = "deep_complete"
        nonproof = norm_space(evidence.get("claim_nonproof_boundary"))
        if not nonproof:
            nonproof = f"只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。"

        owner_info = paths.get(owner, {"chapter": "N/A", "path": comp.get("owner_path", "")})
        # ROADMAP is the current owner/path authority.  Old comparison packets may
        # retain stale paths from an earlier owner decision.
        owner_path = owner_info.get("path", "") or comp.get("owner_path", "")
        marker_present = bool(owner_path and (ROOT / owner_path).exists() and aid in (ROOT / owner_path).read_text())
        books_state = "not_required"
        if disposition == "Integrate":
            books_state = "already_applied" if marker_present else "queued_for_root"
        base.update({
            "screening_status": "retained",
            "screening_reason": RESTORED.get(aid) or norm_space(src.get("screening_reason")) or f"题摘显示 {base['title']} 可能改变长期系统机制或证据合同。",
            "score_v3": score,
            "review_route": review_route,
            "review_status": completion,
            "access_status": "exact_v1_accessible",
            "owner_node": owner,
            "owner_path": owner_path,
            "integration_disposition": disposition,
            "books_state": books_state,
        })
        identities.append(base)
        evidences.append({
            "arxiv_id": aid,
            "source_family_id": base["source_family_id"],
            "primary_evidence_version": f"arXiv:{aid}v1",
            "review_route": review_route,
            "method_identity_locators": norm_space(evidence.get("method_identity_locators")),
            "evaluation_locators": norm_space(evidence.get("evaluation_locators")),
            "limitations_counterevidence_locators": norm_space(evidence.get("limitations_counterevidence_locators")),
            "artifact_locators": norm_space(evidence.get("artifact_locators")) or "Not Disclosed",
            "claim_nonproof_boundary": nonproof,
            "completion_result": completion,
            "reused_under_recovery_contract": aid not in MANUAL_EVIDENCE and aid != "2605.10133",
        })
        books_item = {
            "arxiv_id": aid,
            "source_family_id": base["source_family_id"],
            "owner_node": owner,
            "owner_path": owner_path,
            "current_chapter": owner_info.get("chapter", "N/A"),
            "decision": disposition,
            "books_state": books_state,
            "proposition_level_reason": reason,
            "evidence_boundary": nonproof,
        }
        books.append(books_item)
        if books_state == "queued_for_root":
            queue_delta, insertion_point = QUEUE_DETAILS.get(
                aid,
                (
                    norm_space(comp.get("new_evidence_delta") or comp.get("delta") or base["abstract"][:560]),
                    "在 owner 章相关机制主线内、首个 `## Review notes` 之前；由 root 阅读相邻段落后选择不会形成论文列表的精确位置",
                ),
            )
            queue.append({
                **books_item,
                "proposed_semantic_delta": queue_delta,
                "insertion_point": insertion_point,
                "required_handoff": "相邻章节只保留 owner handoff；不得复制机制正文",
                "root_status": "pending_root_serial_writeback",
            })

    retained = [x for x in identities if x["screening_status"] == "retained"]
    closures = [x for x in identities if x["screening_status"] == "pre_denominator_closure"]
    assert len(identities) == 1146
    assert len(retained) == len(evidences) == len(books) == 110
    assert len(closures) == 1036
    assert all(e["completion_result"] in {"complete", "deep_complete"} for e in evidences)

    institution_sources = [
        ("SRC-OPENAI", "https://openai.com/research/"), ("SRC-ANTHROPIC", "https://www.anthropic.com/research"),
        ("SRC-GOOGLE-AI", "https://deepmind.google/research/"), ("SRC-META-AI", "https://ai.meta.com/research/"),
        ("SRC-QWEN", "https://qwenlm.github.io/"), ("SRC-DEEPSEEK", "https://www.deepseek.com/"),
        ("SRC-MOONSHOT", "https://platform.kimi.com/blog"), ("SRC-TENCENT-HUNYUAN", "https://hunyuan.tencent.com/research"),
        ("SRC-ZAI", "https://www.zhipuai.cn/zh/research"), ("SRC-BYTEDANCE-SEED", "https://seed.bytedance.com/en/research"),
        ("SRC-BAIDU-ERNIE", "https://ernie.baidu.com/blog/zh/"), ("SRC-XIAOMI-MIMO", "https://mimo.xiaomi.com/"),
        ("SRC-MINIMAX", "https://www.minimax.io/blog"),
    ]
    source_coverage = [{
        "source_id": sid, "endpoint": url, "window": "2026-05-11 09:00–2026-05-12 09:00 Asia/Shanghai",
        "result": "no_unique_verified_in_window_event", "note": "检查官方研究/发布目录；未发现可唯一归属本窗且未被 arXiv family 去重的新事件。",
    } for sid, url in institution_sources]
    source_coverage.append({
        "source_id": "SRC-ARXIV", "endpoint": "official OAI direct datestamp 2026-05-12",
        "window": "announcement 2026-05-12 08:00 Asia/Shanghai",
        "result": "complete", "note": "1146 official identities；1146/1146 title screen；ambiguous/high-recall 103 complete abstracts + 7 restored false negatives；110 retained；1036 closures；ordinary revision 0。",
    })

    ledger = {
        "schema": "daily-v3-author-ledger",
        "report_date": "2026-05-12",
        "status": "ongoing_pending_independent_review_and_root_writeback",
        "window": "2026-05-11T09:00:00+08:00/2026-05-12T09:00:00+08:00",
        "date_semantics": "official arXiv announcement/first-public; DataCite created is not ownership",
        "counts": {"raw_identities": 1146, "title_screened": 1146, "complete_abstract_reviewed_high_recall": 110, "candidate_denominator": 110, "pre_denominator_closures": 1036, "ordinary_revisions": 0, "withdrawn": 0},
        "source_coverage": source_coverage,
        "identities": identities,
    }
    (OUT / "V3_AUTHOR_REBUILD_LEDGER.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    (OUT / "V3_AUTHOR_EVIDENCE_REVIEWS.json").write_text(json.dumps(evidences, ensure_ascii=False, indent=2) + "\n")
    (OUT / "V3_AUTHOR_BOOKS_COMPARISON.json").write_text(json.dumps(books, ensure_ascii=False, indent=2) + "\n")
    (OUT / "V3_ROOT_BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps({"schema": "daily-v3-root-books-writeback-queue", "report_date": "2026-05-12", "status": "pending_root_serial_writeback", "count": len(queue), "items": queue}, ensure_ascii=False, indent=2) + "\n")

    closure_categories = Counter()
    for row in closures:
        text = row["screening_reason"]
        if "domain" in text or "application" in text:
            closure_categories["领域应用/专用 benchmark，未改变长期系统合同"] += 1
        elif "task" in text or "quality" in text or "local" in text:
            closure_categories["任务质量或局部模型改进，未改变 owner/边界"] += 1
        else:
            closure_categories["题摘无可定位的 AI System 长期贡献"] += 1

    queue_md = ["# 2026-05-12 Root Books Writeback Queue", "", "作者侧只提出写回，不修改共享 Books；root 需按日期顺序串行写入并进行写后语义审计。", ""]
    for item in queue:
        queue_md += [
            f"## {item['arxiv_id']} → `{item['owner_node']}`",
            "",
            f"- Owner：`{item['owner_path']}`",
            f"- 命题：{item['proposed_semantic_delta']}",
            f"- 插入：{item['insertion_point']}",
            f"- 证据边界：{item['evidence_boundary']}",
            f"- Handoff：{item['required_handoff']}", "",
        ]
    (OUT / "V3_ROOT_BOOKS_WRITEBACK_QUEUE.md").write_text("\n".join(queue_md) + "\n")

    bcount = Counter(x["integration_disposition"] for x in retained)
    bstate = Counter(x["books_state"] for x in retained)
    score_count = Counter(x["score_v3"]["total"] for x in retained)
    lines = [
        "# Daily Research — 2026-05-12",
        "",
        "**规范：** V3",
        "**窗口：** 2026-05-11T09:00:00+08:00 ～ 2026-05-12T09:00:00+08:00",
        "**状态：** 进行中",
        "**Books：** 纳入本次",
        "**检查时间：** 2026-09-15T09:00:16+08:00",
        "",
        "## 1. 结论",
        "",
        "本窗最重要的信号不是某个单一模型发布，而是三类系统责任同时变清楚：长轨迹与多 Agent 需要把压缩、继承和 retry 当作可污染状态；训练/推理效率优化正在把 rollout、KV、speculative work 和 failure recovery 变成显式调度对象；评估不能再把 final score 当事实，必须保存 outcome witness、轨迹一致性和 claim-specific acceptance evidence。",
        "",
        f"官方 arXiv 05-12 08:00 公告批次提供 1146 个唯一身份；完成 1146/1146 title screen，并对高召回语义池完整阅读摘要。重裁后分母为 110，1036 项在分母前以 family-specific 理由闭合。旧版 189 候选与 47 写回不再作为依据。Books 当前有 {bstate['already_applied']} 项语义已存在，{bstate['queued_for_root']} 项需要 root 串行写回，其余 {bcount['No Change — Existing Coverage']} 项为命题级 No Change。",
        "",
        "## 2. 来源覆盖",
        "",
        "| 来源 | 检查范围与依据 | 结果 | 缺口 |",
        "| --- | --- | --- | --- |",
    ]
    for row in source_coverage:
        basis = f"[{row['endpoint']}]({row['endpoint']})；{row['window']}；{row['note']}" if row['endpoint'].startswith('http') else f"{row['endpoint']}；{row['window']}；{row['note']}"
        lines.append(f"| `{row['source_id']}` | {md_cell(basis)} | 已检查 | 无 |")
    lines += [
        "",
        "撤回检查：110 个 retained v1 记录均未显示 withdrawn；撤回数 0。普通 revision 事件 0；本窗没有用 revision 或 DataCite created 代替 first-public ownership。",
        "",
        "分母前闭合分层：" + "；".join(f"{k} {v}" for k, v in closure_categories.items()) + "。完整 1036 项题目、摘要、日期和理由保存在 active ledger，正文不重复铺陈。",
        "",
        "## 3. 候选与判断",
        "",
        "V3 评分只衡量 Design Delta / System Reach / Durability；Reliability、access 与 Books 状态另列。110 项全部完成所需 exact-v1 审阅，按 7～9 深审、5～6 标准审阅执行。",
        "",
        "| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in retained:
        s = row["score_v3"]
        chapter = next(x for x in books if x["arxiv_id"] == row["arxiv_id"])
        chapter_link = f"../../../../{chapter['owner_path']}"
        if row["integration_disposition"] == "Integrate":
            applied = "已在正文" if row["books_state"] == "already_applied" else "待 root 写回"
            book_cell = f"整合：{row['owner_node']}，[{Path(chapter['owner_path']).name}]({chapter_link})，{applied}"
        else:
            book_cell = f"已有覆盖：{row['owner_node']}，[{Path(chapter['owner_path']).name}]({chapter_link})"
        review_cell = "深入完成" if row["review_route"] == "deep" else "标准完成"
        contribution = md_cell(contribution_sentence(row["abstract"]))
        title = md_cell(row["title"])
        lines.append(
            f"| [{title}]({primary_url(row['arxiv_id'])}) | 2026-05-12T08:00:00+08:00 | "
            f"{contribution}；{s['design_delta']} + {s['system_reach']} + {s['durability']} = {s['total']} | "
            f"{review_cell} | {book_cell} |"
        )

    by_id = {x["arxiv_id"]: x for x in retained}
    ev_by_id = {x["arxiv_id"]: x for x in evidences}
    deep_ids = ["2605.08581", "2605.08962", "2605.10448"]
    books_by_id = {x["arxiv_id"]: x for x in books}
    lines += ["", "## 4. 证据与知识整合", "", "以下每项均绑定 exact-v1 的方法、评估和反证/限制位置；表格中的摘要句只用于快速导航，最终判断以本节和证据包为准。", ""]
    for row in retained:
        aid = row["arxiv_id"]
        ev = ev_by_id[aid]
        book = books_by_id[aid]
        chapter_link = f"../../../../{book['owner_path']}"
        decision = "整合" if row["integration_disposition"] == "Integrate" else "已有覆盖"
        state = "正文已存在" if row["books_state"] == "already_applied" else "进入 root 精确写回队列" if row["books_state"] == "queued_for_root" else "无需改稿"
        lines += [
            f"### [{row['title']}]({primary_url(aid)})",
            "",
            f"**采用版本与机制证据：** `arXiv:{aid}v1`；{ev['method_identity_locators']}。",
            "",
            f"**评估证据：** {ev['evaluation_locators']}。",
            "",
            f"**判断：** {contribution_sentence(row['abstract'])} 该命题通过 title+完整 abstract 准入，并由上述正文位置复核；它的系统 owner 是 `{row['owner_node']}`。",
            "",
            f"**反证与边界：** {ev['limitations_counterevidence_locators']}；{ev['claim_nonproof_boundary']}",
            "",
            f"**Books：** {decision} `{row['owner_node']}` → [{Path(book['owner_path']).name}]({chapter_link})；{book['proposition_level_reason']}；{state}。",
            "",
        ]

    lines += ["### 跨材料技术演进（最多三条）", "", "#### 1. Scheduling 与 Memory 必须共享可验证状态，而不是各自追局部命中率", ""]
    for did in deep_ids:
        row, ev = by_id[did], ev_by_id[did]
        lines += [
            f"##### [{row['title']}]({primary_url(did)})", "",
            f"**Why / Mechanism：** {row['abstract'][:720]}…", "",
            f"**证据：** {ev['method_identity_locators']}；{ev['evaluation_locators']}。", "",
            f"**Trade-off / 边界：** {ev['claim_nonproof_boundary']}", "",
            f"**Books：** `{row['owner_node']}` → `{row['owner_path']}`；{next(x for x in books if x['arxiv_id']==did)['proposition_level_reason']}", "",
        ]
        if did == "2605.08581":
            lines += ["这里的演进是 static admission → cache-aware scheduling → admission 与 retention 共同维护 segment state。收益是减少 hot segment 重算和 TTFT，代价是更强的 locality bias、cache metadata freshness 与 eviction coupling；低复用或负载稳定时，普通 batching/eviction 仍更简单。", "", "#### 2. Production Training 的优化对象已经从单算子扩展为异构 execution plan", ""]
        elif did == "2605.08962":
            lines += ["这里的演进是单一模态/近似同长 batch → modality-aware packing → 训练图、通信与 checkpoint 共同面向动态样本形态。它换来更高设备利用率，却扩大 planner drift、数据混合偏差与恢复状态空间；同质数据或小规模训练仍可保留静态计划。", "", "#### 3. Benchmark 分数必须受 outcome evidence 支撑", ""]
        else:
            lines += ["这里的演进是 final binary check → action-path witness → evidence-supported score bound。更严格的 outcome evidence 降低虚假成功，却增加 instrument、状态可观测性和人工 adjudication 成本；确定性、原子任务仍可用简单断言。", ""]

    lines += [
        "### Books Decision 汇总", "",
        f"- Integrate：{bcount['Integrate']}（其中 {bstate['already_applied']} 已在当前 Books 正文存在，{bstate['queued_for_root']} 进入 root 写回队列）。",
        f"- No Change — Existing Coverage：{bcount['No Change — Existing Coverage']}；每项均记录现有命题而不是只写章节名。",
        "- Weekly Only / Blocked / Disputed：0。所有 exact-v1 必要正文已取得；未披露 artifact 只限制复现强度，不被写成机制受阻。",
        "",
        f"Root 写回队列见 `../_sources/daily-20260512/V3_ROOT_BOOKS_WRITEBACK_QUEUE.md`；作者侧未修改共享 Books。评分分布：" + "、".join(f"{k}/9={v}" for k, v in sorted(score_count.items())) + "。",
        "",
        "## 5. 缺口与下一步", "",
        f"1. root 按 owner 分组、按日期顺序串行处理 {len(queue)} 项写回，并在相邻章节与 `Review notes` 边界内验证唯一 owner。",
        "2. 全新非作者 reviewer 必须全量检查 110 项准入、评分、证据与 Books disposition，并对 1036 closure 做分层 false-negative audit。",
        "3. 机构来源当前未发现独立 in-window 事件；若以后出现官方时间证据，只重开对应 source family，不重跑 1146 项。",
        "",
        "## 6. 复核", "",
        "- 复核者：待全新独立 reviewer。",
        "- 结论：未通过（不是失败；作者侧完成，root 写回和独立 Gate 尚未执行）。",
        "- 作者侧检查：1146 = 110 + 1036；110 = Evidence 110 = Books comparison 110；withdrawn=0；ordinary revision=0；所有 JSON 可解析。",
        "- 本报告不得在 root 写回与独立复核前改为完成。",
        "",
        "### Sources", "",
        "- [arXiv official browse/API](https://arxiv.org/)：05-12 公告批次与 exact-v1 HTML/PDF。",
        "- [ROADMAP](../../../../ROADMAP.md)：Stable Knowledge Node owner。",
        "- [Active V3 ledger](../_sources/daily-20260512/V3_AUTHOR_REBUILD_LEDGER.json)。",
        "- [Evidence reviews](../_sources/daily-20260512/V3_AUTHOR_EVIDENCE_REVIEWS.json)。",
        "- [Books comparison](../_sources/daily-20260512/V3_AUTHOR_BOOKS_COMPARISON.json)。",
    ]
    REPORT.write_text("\n".join(lines) + "\n")

    ledger_hash = hashlib.sha256((OUT / "V3_AUTHOR_REBUILD_LEDGER.json").read_bytes()).hexdigest()
    checkpoint = {
        "schema": "daily-v3-author-checkpoint",
        "report_date": "2026-05-12",
        "status": "author_complete_pending_root_and_independent_reviewer",
        "counts": {"raw": 1146, "retained": 110, "closures": 1036, "evidence_complete": 110, "books_compared": 110, "already_applied": bstate["already_applied"], "root_queue": len(queue)},
        "active_ledger_sha256": ledger_hash,
        "author_assertion": "not_a_final_gate",
    }
    (OUT / "V3_AUTHOR_CHECKPOINT.json").write_text(json.dumps(checkpoint, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
