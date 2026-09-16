#!/usr/bin/env python3
"""Apply the bounded 28-item 2026-05-11 author screening repair.

The script mutates only the active Daily report and its V3 author-side artifacts.
It never writes shared Books files.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
SRC = Path(__file__).resolve().parent
REPORT = ROOT / "papers/2026/05/11/README.md"
LEDGER = SRC / "V3_SCREENING_LEDGER_20260914.json"
EVIDENCE = SRC / "V3_EVIDENCE_REVIEWS_20260914.json"
COMPARISON = SRC / "V3_BOUNDED_REPAIR_BOOKS_COMPARISON_20260915.json"
QUEUE_JSON = SRC / "V3_BOOKS_WRITEBACK_QUEUE_20260914.json"
QUEUE_MD = SRC / "V3_SCREENING_REPAIR_ROOT_BOOKS_QUEUE_20260915.md"
CHECKPOINT = SRC / "V3_SCREENING_REPAIR_AUTHOR_CHECKPOINT_20260915.md"

CHECKED_AT = "2026-09-15T23:55:00+08:00"
PUBLIC_EVENT = "2026-05-11T08:00:00+08:00 scheduled arXiv announcement"

OWNER_PATHS = {
    "AGENT-REFLECTION": "books/part-07-agent/80-reflection.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/56-inference-scheduling.md",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
    "AGENT-MULTI-AGENT": "books/part-07-agent/82-multi-agent.md",
    "AGENT-CONTEXT": "books/part-07-agent/75-context.md",
    "MODEL-TRANSFORMER-LAYER": "books/part-02-model/17-transformer-layer.md",
    "TRAIN-PPO": "books/part-04-training-system/32-ppo.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "INFER-KV-CACHE": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
    "TRAIN-LORA": "books/part-04-training-system/30-lora.md",
    "TRAIN-DISTRIBUTED-TRAINING": "books/part-04-training-system/36-distributed-training.md",
    "TRAIN-GRPO": "books/part-04-training-system/33-grpo.md",
    "AGENT-MEMORY": "books/part-07-agent/77-memory.md",
    "MULTIMODAL-WORLD-MODELS": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/72-security.md",
    "AGENT-TOOL-CALLING": "books/part-07-agent/78-tool-calling.md",
    "AGENT-PLATFORM": "books/part-07-agent/84-agent-platform.md",
    "MULTIMODAL-EMBODIED-VLA": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
}


def spec(score, owner, decision, claim, mechanism, boundary, comparison, locators, artifact, binding=None, insertion=None, prose=None):
    return {
        "score": score,
        "owner": owner,
        "decision": decision,
        "claim": claim,
        "mechanism": mechanism,
        "boundary": boundary,
        "comparison": comparison,
        "locators": locators,
        "artifact": artifact,
        "binding": binding,
        "insertion": insertion,
        "prose": prose,
    }


N = "No Change — Existing Coverage"
I = "Integrate"
A = {
    "2605.06690": spec((2, 2, 3), "AGENT-REFLECTION", N,
        "递归推理必须显式保存 epistemic state，并把 expand/consolidate order-gap 只当作局部停止诊断，而不是 truth 或全局收敛证明。",
        "论文把 claim、evidence relation、open question 与 confidence 组织成 epistemic state graph；比较 expand→consolidate 与 consolidate→expand 的状态距离，并给出线性化 order-gap 在 fixed point 邻域非退化的充要条件。Algorithm 1 与 Table 1 是算法/说明性轨迹，不是生产实验。",
        "条件只在 fixed point 邻域且针对线性化 gap；作者明确不声称全局收敛。图抽取与 confidence 可能错误，gap 小也可能是两个顺序共同遗漏；证据冲突、抽取不稳或高风险时回退固定预算、外部 verifier 与人工升级。",
        "Ch80 已有“Reflection 的停止条件需要 Typed Epistemic State”，逐项保存 claim/evidence/conflict/unknown 与 order gap，并明确 local diagnostic、预算、hard cap、evidence gate 和人工回退；该 exact-v1 是现有正文所承载命题的原始受限证据。",
        ("§2–§6；Algorithm 1 Recursive Reasoning with Order-Gap Termination", "§7 application analysis；Table 1 为 expository trajectory", "§5 local non-degeneracy theorem；§9 discussion；§10 Conclusion；无全局收敛证明"),
        "not required for the adopted theoretical claim; exact-v1 discloses no immutable implementation artifact consumed by this review"),
    "2605.06908": spec((3, 3, 3), "INFER-SCHEDULING", I,
        "test-time compute gate 必须区分 compute need 与 compute suitability；同一 uncertainty/difficulty signal 的效用方向会随 environment 与 backbone 反转。",
        "DIAL 先用 base/rollout 的 counterfactual exploration 得到 utility difference，再从通用与任务特征中以稀疏 logistic gate 学习每个 environment/backbone 的方向。Table 1 显示跨六环境、三骨干的 signal–utility 方向不稳定；Table 2–3 与 ablation 检查成功率—成本及反向 gate 的退化。",
        "稀疏 gate 依赖探索数据、reward 与环境/骨干身份；关联方向不是因果机制，错误方向会专门选择有害状态。冷启动、分布漂移或高风险请求回退固定预算、独立 verifier 或保守不追加 compute。",
        "Ch56 已有 reasoning budget、solvability、marginal value 与 monitor calibration，但仍把 gate signal 主要写成单调可校准输入；没有保存“同一 signal 在不同 environment/backbone 上方向反转”的 gate-direction identity。",
        ("§3 Problem Formulation；§4 DIAL", "§5.1–§5.3；Table 1–3；Figure 1–3", "§6 Limitations；§7 Conclusion；Appendix H Broader Impact"),
        "no immutable implementation identity captured; no reproduction claim adopted",
        "same-signal-opposite-compute-gate-direction", "Ch56 ‘Reasoning Budget 必须进入调度与评估身份’，在 monitor calibration 与按 solvability/marginal value 分配之间。",
        "Reasoning gate 不能预设 uncertainty 或 difficulty 与追加计算价值同向。Scheduler 应把 environment、backbone、base/rollout policy、reward 与 counterfactual utility 一起写入 gate calibration：先区分“需要更多计算”与“当前状态适合通过 rollout 获益”，再学习该 slice 的方向。这样能避免 wrong-direction gate 专门挑中会被 rollout 伤害的状态，却增加探索成本、稀疏特征漂移与 reward 依赖；方向不稳、样本不足或高风险时，回退固定预算、独立 verifier 或保守不追加计算。 [受限证据：arXiv:2605.06908v1]"),
    "2605.06924": spec((3, 2, 3), "MULTIMODAL-GENERATIVE-PARADIGMS", I,
        "长视频 segment generation 应从 open-loop chaining 演进为读取持久 multimodal memory、选择生成模式并在提交前分层修正的闭环。",
        "A2RD 对每个 segment 执行 Retrieve–Synthesize–Refine–Update：MVMem 跟踪跨模态进展，adaptive generator 在 extrapolation/interpolation 间切换，frame/video 两级 self-improvement 抑制误差传播；VBench-Long、LVBench-C 与人工评价覆盖一到十分钟视频。",
        "证据绑定 Veo 3.1、作者 prompt/workflow 与 benchmark；self-refinement 共享 generator/judge 偏差，memory/mode switch 会引入 drift、额外调用和错误累积。边界状态或 evaluator 不可靠时回退短 segment、固定 mode、人工 storyboard 或重新生成。",
        "Ch24 已有视频 temporal state、segment commit 与 plan→draft→inspect→refine 的通用分支，但未把跨 segment multimodal memory、mode switch、双层 refine/update 组合成可恢复的长视频闭环状态。",
        ("§3–§4；§3.1 MVMem Design；Appendix E prompts", "§5.1–§6；Table 2–5；Figure 1–4；人工评价", "§7 Conclusions；Limitations；Appendix B.2 methodology analysis"),
        "supplementary videos are referenced, but no immutable artifact identity was captured; no reproduction claim adopted",
        "long-video-closed-loop-segment-memory", "Ch24 视频的 temporal state / segment commit 主线，在 open-loop segment generation 后。",
        "长视频不能只把上一段末帧当下一段条件；一旦主体离场再出现、环境发生非线性变化，open-loop chaining 会把早期误差持续放大。生成 runtime 可为每段执行 `retrieve → synthesize → frame/video-level refine → update`，由版本化 multimodal memory 保存实体、环境与叙事进展，mode controller 只在已声明的 extrapolation/interpolation 分支中选择，最终 clip gate 才提交可见段。它用额外生成、检索与 self-review 换长程一致性，也会继承同源 evaluator 偏差、memory drift 和 mode-switch 错误；状态不可信或预算不足时回退短段、固定模式、人工 storyboard 或整段重生成。 [受限证据：arXiv:2605.06924v1]"),
    "2605.06988": spec((3, 2, 3), "AGENT-MULTI-AGENT", I,
        "Multi-Agent communication 评价必须把 consensus 与 alignment-to-truth 分开；低分歧可能是 confident-but-wrong herding。",
        "论文把 agent belief 写成分布状态，联合操纵消息频率与内容，比较持续广播、定期通信与 uncertainty-gated protocols；JSD/rate-to-consensus 与 alignment-to-truth 分开报告，失败 episode 中持续通信可低 JSD 地共同错误。",
        "grid-world、Bayesian fusion、同步执行和已知 truth 不外推开放 Agent；truth alignment 在生产往往不可观测，通信延迟/丢包又改变结果。拿不到独立 truth 时保留 dissent、provenance 与独立 verifier，不能用 consensus 自证正确。",
        "Ch82 已警告 correlated hallucination、同源报告和 voting 不能构成独立证据，但尚未把 communication frequency/content、collective belief state 与 truth-alignment/JSD 双指标绑定成 protocol-level evaluation identity。",
        ("§3 System Model；§3.2 Agent Architecture；§4 metrics/design", "§4.6；§5；Figure 2–4；Appendix A", "§6 Discussion；§6.5 Limitations；§7 Conclusion"),
        "not required for the adopted mechanism; no immutable simulator artifact captured",
        "epistemic-alignment-vs-consensus", "Ch82 ‘Verification 与 Aggregation’，在 correlated error / consensus 不等于 truth 的段落后。",
        "Multi-Agent 协议不能把快速共识当作协作正确性。Evaluation identity 应同时记录通信频率、消息内容、collective belief divergence 与对独立 truth/effect receipt 的 alignment：低 JSD 或高 consensus rate 只说明内部一致，仍可能是 confidently-wrong herding。增加 truth-alignment 与失败 episode 切片会提高标注和重放成本，开放任务还常拿不到真值；此时必须保留 dissent、provenance 和独立 verifier，不能让团队共识自签完成。 [受限证据：arXiv:2605.06988v1]"),
    "2605.07042": spec((3, 3, 3), "AGENT-CONTEXT", I,
        "agentic search 应以持久 predicate-based belief state 拥有已知/未知与未解条件，并用 programmatic exhaustion gate 终止空转。",
        "CGDP 把超大隐藏环境中的 context gathering 建模为 POMDP，并以 approximate Thompson Sampling 解释行为；PBAI loop 将隐式 search 拆成 predicate operations，PBBS 注入 belief state，exhaustion detector 读取程序信号。三域四种 harness 的实验分别检查准确率恢复与 token 节省。",
        "belief extractor 与 predicate schema 会遗漏证据；exhaustion 只检测所建模的停滞，不证明任务已解。状态不完整、开放搜索或高风险时扩大检索、保留 hard budget，并向人工暴露 unresolved predicates。",
        "Ch75 已有 Active Information Foraging 的显式 epistemic state、遗漏风险与停止原因，但尚缺把 predicate closure 与 programmatic exhaustion 分离、并要求 gate 不把‘无新结果’解释为‘任务已完成’。",
        ("§3 Framework；§4 Abstract Algorithm；Algorithm 1", "§6–§6.2；Table 2–4；Appendix D/F/G", "§7 Discussion and Conclusion；Limitations and Future Work"),
        "no immutable implementation identity captured; no reproduction claim adopted",
        "predicate-belief-search-exhaustion-gate", "Ch75 ‘长上下文从被动堆积演进为 Active Information Foraging’，紧接显式 epistemic state 段。",
        "Context gathering 不应只把搜索历史压成摘要。Agent 要持有 predicate-based belief state，显式记录已满足条件、未解问题、证据来源和下一观察；programmatic exhaustion gate 只能根据重复查询、无新 predicate closure 与预算判断“继续搜索的边际价值耗尽”，不能把它升级为答案正确。这个状态减少重复搜索和 Context 膨胀，却依赖 extractor/schema 完整性；开放域或高风险中应扩大检索、保留 hard cap，并将 unresolved predicates 交给 verifier 或人工。 [受限证据：arXiv:2605.07042v1]"),
    "2605.07073": spec((3, 3, 3), "AGENT-MULTI-AGENT", I,
        "Multi-Agent evaluation 必须用 enforcement 区分角色声明与真实 capability separation，并把 team pass、越权尝试和 verifier false accept 分开。",
        "TeamBench 以 OS sandbox 分离 Planner 的 spec access、Executor 的 workspace edit 与 Verifier 的 final attestation；851 templates/931 instances 比较 Solo、prompt-only、sandbox-enforced 与 role ablations，并用 deterministic grader 审计 verifier。相近 pass rate 下，prompt-only 越权编辑更多，verifier 仍大量 false accept。",
        "benchmark 的文件权限与 deterministic grader 不覆盖真实网络、credentials、隐式 side effects；强分权增加 coordination/missing-information cost，团队在易任务还可能劣于单 Agent。隔离或 verifier 不可靠时回退 single owner、最小权限与人工 certification。",
        "Ch82 已有 role/topology/version、verifier 与 commit owner，但未要求 evaluation 以 OS-enforced capability separation 验证 prompt role，也未把 team success 与 unauthorized attempt/false accept 分列。",
        ("§2 benchmark/roles；§2.3 Ablation Conditions；Appendix F.2", "§3.1–§3.7；Table 1；Figure 1–5；human study", "§4 Discussion；§5 Conclusion；H2 step-limit exhaustion"),
        "no immutable benchmark release identity captured; no reproduction claim adopted",
        "os-enforced-role-separation-eval", "Ch82 role/verification 主线，在角色与 commit owner 定义后、Verification 与 Aggregation 前。",
        "角色提示不等于权限边界：团队 pass 可能来自某一角色偷偷读取完整规格、修改 workspace 或自行认证。Multi-Agent EvalSpec 应同时冻结 prompt roles 与 OS/runtime enforcement，分别报告 team outcome、unauthorized access/edit attempt、verifier false accept/reject 和相对 single-agent value。强隔离提高可审计性，却增加缺失信息协调和易任务的团队开销；sandbox 覆盖不全或 verifier 不可信时，回退单一最小权限 owner、deterministic grader 与人工 certification。 [受限证据：arXiv:2605.07073v1]"),
    "2605.07271": spec((2, 2, 3), "MODEL-TRANSFORMER-LAYER", I,
        "layer pruning 的质量崩塌应按 decision representation transition 诊断；hidden representation 仍相似不代表模型仍能进入 Decisive phase。",
        "论文用 iterative pruning 追踪 zero-shot accuracy、CKA、decision representation similarity 与 layer-wise Decision Margin；在 Llama3-8B、Llama2-7B、Qwen3-4B 上观察 Silent/Decisive phase 与 pruning cliff，并用噪声敏感性分析结构脆弱性。",
        "Decision Margin 绑定多选任务、选项 logit 与作者模型，不是所有生成任务的通用因果解释；iterative pruning 是分析 probe。指标失配或开放生成时回退任务级评测、activation/gradient probes 与保守少剪枝。",
        "Ch17 解释 attention/MLP/residual 的层职责，却未表达 pruning 会保留表面 feature similarity 但截断深层 decision transition，也没有 Silent/Decisive phase 的结构性验收。",
        ("§3 Method；Appendix A.3", "§4–§4.3；Figure 1–6；Appendix A.1", "§5 Conclusion；Appendix A.12 Limitations and Future Work"),
        "no immutable implementation identity captured; no reproduction claim adopted",
        "layer-pruning-decision-phase-collapse", "Ch17 residual/层职责之后，作为 layer pruning 的 decision-level failure branch。",
        "Layer pruning 不能只比较平均 activation/CKA 相似度：深层表示仍看似保留时，模型也可能因前置层被删而无法跨过 decision-margin transition。压缩验收应沿层深记录 Silent phase 到 Decisive phase 的任务相关 transition，并把 pruning mask、模型、task 与 margin probe 绑定；它能解释突发 accuracy cliff，却依赖多选 logit 和作者定义，不能当通用因果证明。开放生成或 probe 不适用时，回退任务级回归、保守剪枝与完整模型。 [受限证据：arXiv:2605.07271v1]"),
    "2605.07331": spec((3, 2, 3), "TRAIN-PPO", I,
        "LLM policy optimization 的 IS ratio 可以对 prefix action likelihood 累乘，但必须用 position-adaptive clipping 控制随序列长度增长的 log-ratio 方差。",
        "CTPO 以 cumulative token IS ratio 对齐当前 token 所在 prefix state，理论比较 token/sequence/cumulative ratio 的 bias–variance；固定 clip 下越后位置越易截断，故按 sqrt(position) 调节 log-space threshold。数学 tool-use benchmark、Figure 1 与 Table 2–3 检查位置 clip rate和结果。",
        "累积 ratio 的方差随长度放大，approximation 与 clipping schedule 依赖 policy lag、长度和任务；作者未证明其对任意长文本或异步 rollout 稳定。估计爆炸、off-policy gap 大或短序列时回退 token-level PPO、sequence ratio 或更频繁同步。",
        "Ch32 定义 token prefix state 与 clipped ratio，Ch33 比较 token/sequence ratio granularity，但没有把 cumulative prefix ratio 与 position-adaptive clip 作为同一 bias–variance branch。",
        ("§2 setup；§3 cumulative ratio/position-adaptive clipping", "§3.2–§4.2；Table 1–3；Figure 1–2", "§5 analysis；§6 Conclusion；无独立 Limitations 标题，按模型/任务/长度范围收窄"),
        "no immutable implementation identity captured; no reproduction claim adopted",
        "cumulative-token-is-position-adaptive-clip", "Ch32 PPO probability ratio 与 clipping 主线，在 token-level ratio 定义后。",
        "逐 token ratio 只比较当前 action probability，不能直接表达更早 token 已改变当前 prefix state；把截至位置 t 的 ratios 累乘可更贴近 prefix-level policy shift，却让 log-ratio variance 随位置增长。PPO branch 因而要把 ratio granularity 与 position-adaptive clipping 一起版本化：后部 token 使用按校准长度增长的 log-space bound，并分别报告位置 clip rate。它以较低 state mismatch 换更高方差和长度敏感性；policy lag 过大、长序列比率爆炸或校准不足时，回退 token ratio、sequence ratio 或更频繁 rollout 同步。 [受限证据：arXiv:2605.07331v1]"),
    "2605.07395": spec((3, 3, 2), "PLATFORM-EVALUATION-SYSTEM", I,
        "multi-LLM router 的 oracle/unsolvability ceiling 必须先去除 judge misalignment、truncation 与 format artifact，否则错误标签会训练出 routing collapse。",
        "论文将 routing ceiling 分成 genuine evaluator disagreement 与共同 measurement failures；在 MMLU、MedQA、ShareGPT 和 Gemma tiers 上用 exact match/重判分、context overflow 与 formatting decomposition 修正 solvable labels，并显示 judge-derived oracle 分布会偏向小模型。",
        "证据限特定 Gemma tiers、datasets、judge 和 4,096 context；exact match 也只适合结构化答案。无法取得可靠 adjudication 时应保留 Unknown、扩大 context/解析校验，不能用伪 oracle 训练 router。",
        "Ch66 已有 judge bias、truncation、format/schema 与 observed/elicitation ceiling，但尚未明确这些 artifact 会污染 multi-model router 的 oracle labels，并把评估错误固化为 routing policy。",
        ("§2 routing ceiling；§3.3 Evaluation Framework and Artifact Decomposition", "§3 setup；§4–§8；Table 3–7", "§9 Discussion；§9.4 Limitations；§11 Conclusion"),
        "no immutable implementation identity captured; no reproduction claim adopted",
        "router-label-artifact-ceiling", "Ch66 observed capability / evaluation ceiling 主线，在 judge 与 truncation/format artifact 讨论后。",
        "Multi-model routing 的“oracle label”也可能是测量产物。Evaluation owner 应先把 unsolvable ceiling 分解为 genuine capability gap、judge misalignment、context truncation/empty response 与 format/parser failure；只有经独立 outcome 或适配 metric 复核的 label 才能训练 router。否则 judge 对某个 tier 的系统偏差会变成 routing collapse。分解增加重判分和多 evaluator 成本，开放回答也没有统一 exact match；证据不足时保留 Unknown、扩大 context 或使用保守静态 routing，不能用伪 oracle 自证上限。 [受限证据：arXiv:2605.07395v1]"),
    "2605.07443": spec((3, 3, 3), "INFER-KV-CACHE", N,
        "非连续知识复用需要把 prefix cache 扩展为有身份的 reusable block，并联合 tiered residency、locality placement 与 selective-attention correction。",
        "RcLLM 将 system/context 与 item KV 分池，分析 item cache 规模，以 similarity-aware placement 建立全局副本并配合选择性 attention；evaluation 覆盖推荐准确率、延迟/吞吐、cache pool 与 placement ablation。",
        "结果绑定推荐 workload、Qwen3-8B 与作者实现；相似 item 不保证 position/conditioning 等价，分层搬运、选择 miss 与 correction 都可能返还收益。identity 或 repair 不成立时回退完整 prefix prefill/FullKV。",
        "Ch45 当前已完整拥有 exact prefix identity、immutable blocks、CPU/SSD tier、prefix-tree locality/prefetch、document/chunk packet、任意位置 position-conditioning seam repair 与 selective recompute；RcLLM 的组合不再增加长期命题。",
        ("§III System Design；§III-A–§III-D；Algorithm 1", "§IV–§IV-D；Table I–III", "§V discussion；§VI Conclusion；无独立 Limitations 标题，按 workload/model/implementation 收窄"),
        "no immutable implementation identity captured; no reproduction claim adopted"),
    "2605.07494": spec((3, 2, 3), "TRAIN-LORA", I,
        "continual VLM adapter 应把固定专家池拆成可演化 sparse pool，并分离 train-time expert evolution 与 inference-time prototype selection。",
        "DIMoE-Adapters 为新任务增加 task router/experts 并冻结旧分支；SCEE 依据动态指标扩展/更新 expert pool，PGES 以 task prototypes 决定进入 adapter 或 frozen CLIP zero-shot path。MTIL/few-shot、cost 与 module ablation 检查 transfer、average/last score。",
        "pool 会持续增长，prototype drift/错误 task ID 会误路由，冻结旧专家也不保证消除遗忘；证据限 CLIP/VLM 与 MTIL。预算或识别失败时回退固定 adapter、共享 LoRA、rehearsal 或 frozen base。",
        "Ch30 有 adapter routing、rank/组合/冲突与持续更新边界，但没有把 expert pool lifecycle 与 prototype-based selection 拆成两个 owner/state。",
        ("§3 Methodology；Figure 1–2", "§4–§4.3；Table 1–4；DIMoE/SCEE analysis", "§5 Conclusion；正文未单列 limitations，按 continual-VLM/benchmark 范围收窄"),
        "no immutable implementation identity captured; no reproduction claim adopted",
        "continual-adapter-expert-evolution-selection", "Ch30 多 Adapter routing/组合之后，作为 continual adapter pool lifecycle 分支。",
        "Continual VLM 不应把固定 MoE adapter pool 当作永久能力目录。训练面要独立拥有 expert evolution：何时复用、扩展、冻结或淘汰 expert；推理面只根据版本化 task prototype 提出 sparse selection，并保留 frozen base 的 zero-shot fallback。分权能限制遗忘和无关 adapter 干扰，却会造成 pool growth、prototype drift、错误 task identification 与额外路由成本；识别或预算不可靠时回退固定 adapter、共享 LoRA、rehearsal 或 frozen base。 [受限证据：arXiv:2605.07494v1]"),
    "2605.07569": spec((3, 3, 2), "TRAIN-DISTRIBUTED-TRAINING", I,
        "异构长上下文训练的 CP/HP plan 应按 GPU compute、memory 与 network 共同生成 fully asymmetric partition，而不是强制同构 mesh。",
        "HexiSeq 以 hierarchical scheduler 先决定跨设备 context/head ownership，再生成不对称 exchange；在混合 GPU testbeds 的 3B/7B/13B 与 simulation 的 70B 上对比 throughput，并做长 context、heterogeneity 与 scheduler analysis。",
        "收益依赖 profile、模型 shape、拓扑与计划一致提交；simulation 不是生产 70B 证明，不对称 plan 增加建图/缓冲/同步与 straggler 风险。profile 过期或成员无法一致提交时回退规则 Ulysses/同构 CP。",
        "Ch36 已有 topology-aware fully-connected exchange plan，但当前命题更具体：partition 本身需同时消费异构 compute、memory、network，并允许 CP/HP 维度完全不对称，而非只重排通信图。",
        ("§2 formulation；§3 System Design and Implementation；Appendix B", "§5–§5.1；Figure 1–5", "§6 Conclusion；Appendix D Limitations"),
        "no immutable implementation identity captured; no reproduction claim adopted",
        "heterogeneous-cp-hp-asymmetric-partition", "Ch36 Context Parallel 的 topology-aware exchange plan 后。",
        "规则 Ulysses/同构 mesh 假定各 GPU 的 compute、memory 与 link capacity 近似一致；混合设备中，平均切分会让最弱维度决定整个 step。Parallel planner 应联合建模设备算力、可用显存、网络层级与 head/sequence ownership，生成可版本化的 fully asymmetric CP/HP partition；所有 rank 一致提交 plan epoch 后才能执行。它用更高建图、profile、buffer 和同步成本换减少 straggler 的机会；profile 过期、拓扑变化或计划无法一致提交时，回退规则 Ulysses、同构 CP 或缩小成员集。 [受限证据：arXiv:2605.07569v1]"),
    "2605.07630": spec((3, 3, 3), "PLATFORM-EVALUATION-SYSTEM", I,
        "phone-use Agent safety 必须把 harmless outcome 分成 safe action、unsafe action 与 inability-to-act；不行动造成的无害不能计作安全。",
        "PhoneSafety 从真实 Android 轨迹抽取 700 个 safety-critical moments，提供 protocol-grounded safe/unsafe references，并把 outcome 分解为 Safe-action、Unsafe-action 与 CFR；700 cases、130+ apps、多模型/agent 和 protocol ablation 比较能力、安全与行动能力。",
        "reference protocol、app state 与辅助 classifier 可能误标；真实设备覆盖仍有限，safe reference 不证明长期 outcome。低行动能力模型可能虚高 harmlessness，高风险发布需 effect receipt、人工 adjudication 与任务完成率共同验收。",
        "Ch66 有 outcome/abstention/no-op 与 safety slice，但尚未把 phone Agent 的 unsafe、safe、irrelevant/no useful action 三分并明确 harmlessness false positive。",
        ("§2.1 Evaluation Unit；§2.4 PhoneSafety；§2.6 setup", "§3–§3.5；Figure 1–3；Table 1–3", "§4 Conclusion；Appendix H Limitations；Appendix J"),
        "no immutable dataset release identity captured; no reproduction claim adopted",
        "phone-agent-three-way-safety-outcome", "Ch66 Agent outcome/abstention contract，在 no-op/行动偏差切片之后。",
        "‘没有造成伤害’不是充分的 Agent safety 证据：模型可能做出合规安全动作，也可能选择危险动作，或只是无法完成任何相关动作。Phone-use EvalSpec 应把 safety-critical moment 的结果拆成 safe action、unsafe action 与 inability-to-act/CFR，并与任务成功和 effect receipt 联合报告；否则低能力模型会因不行动得到虚高 harmlessness。三分法增加 protocol 标注与真实设备重放成本，reference 也会有争议；高风险或状态不确定时应保留人工 adjudication，而不能用 harmless outcome 自签安全。 [受限证据：arXiv:2605.07630v1]"),
    "2605.07776": spec((2, 2, 3), "PLATFORM-EVALUATION-SYSTEM", I,
        "reasoning failure sensor 应读取整条 uncertainty trace 的阶段、斜率与形态，而不是只用终局 confidence。",
        "作者在 GSM8K/ProntoQA、五模型上抽取 distributional/consistency/epistemic uncertainty 的 early/mid/late mean、slope 与 fit quality，用 LR/GB 分类正确/错误，并逐步增加可见轨迹比例测试 early detection；另定位首错附近的轨迹变化。",
        "uncertainty feature 是相关 sensor，不是首错因果或 truth；需要 token probabilities/多采样，跨模型/任务校准会漂移。访问受限或 AUROC 不稳时回退终局 verifier、外部 evidence 与保守 abstain。",
        "Ch66 已有多 uncertainty sensor 与 deployment-slice calibration，却未把 trace 当 evolving state、按 early/mid/late profile 验证早期 failure sensing。",
        ("§3 Methods；§3.2 Experimental Procedure", "§4–§4.3；Figure 1–5；Table 1；Appendix D", "§5 Discussion；Limitations and future work；§6 Conclusion"),
        "no immutable implementation identity captured; no reproduction claim adopted",
        "reasoning-uncertainty-trace-early-failure", "Ch66 uncertainty / confidence sensor 主线，在终局 confidence 校准之后。",
        "终局 confidence 会丢掉推理过程中的转折：错误可能在中段出现，随后语言表面重新变得确定。Evaluation owner 可把 reasoning trace 视为 evolving measurement state，保存 early/mid/late uncertainty、slope、fit quality 与首错位置，再验证在多少前缀比例下可预测失败。它支持 early stop/escalation proposal，却不是因果归因或 truth；token probability 不可见、跨模型校准漂移或 AUROC 不稳时，应回退终局 verifier、外部 evidence 与保守 abstain。 [受限证据：arXiv:2605.07776v1]"),
    "2605.07850": spec((2, 2, 3), "TRAIN-LORA", I,
        "动态 LoRA rank 可由同一 adapter 的 nested sub-ranks 提供，但训练和验收必须覆盖整个 rank curve，而非只优化最大 rank。",
        "MatryoshkaLoRA 构造共享 ordered low-rank factors，使前 k 个方向形成可独立使用的 sub-adapter，并给出兼容既有 LoRA 方法的多 rank objective；AURAC 汇总 rank–accuracy curve。GSM8K、ARC-C、HellaSwag 与 scaling ablation 检查各 rank。",
        "sub-rank ordering与任务相关，低 rank 可能退化，AURAC 会掩盖关键 operating point；证据限 Llama 与所测任务。固定预算/单部署 rank 时普通 LoRA 更简单，关键 rank 仍需单点 gate。",
        "Ch30 已有 rank budgeting、adapter identity 与组合冲突，但没有把单个 adapter 训练成 nested sub-ranks，也未定义跨 rank curve 的 AURAC 验收。",
        ("§2–§2.3.3；Algorithm 1；Appendix B", "§2.5；§3–§3.4；Table 1–3", "§4 Conclusion, Limitations and Broader Impact"),
        "no immutable implementation identity captured; no reproduction claim adopted",
        "hierarchical-lora-subrank-aurac", "Ch30 rank 选择与 adapter identity 段，在固定 rank baseline 后。",
        "为每个预算单独训练 LoRA 最清楚，却会产生多个不可共享的 adapter revision。若部署需要动态 rank，可让同一 adapter 的 ordered factors 形成 nested sub-ranks，并把训练目标和 artifact identity 绑定到可用 rank set；验收同时报告关键 rank 的单点质量与 rank–accuracy curve/AURAC，不能让平均曲线掩盖低 rank collapse。该路径减少多 checkpoint 成本，却依赖方向 ordering、任务分布和 kernel 支持；固定预算或某一关键 rank 不合格时，回退普通固定-rank LoRA。 [受限证据：arXiv:2605.07850v1]"),
    "2605.07924": spec((3, 2, 3), "MULTIMODAL-GENERATIVE-PARADIGMS", I,
        "few-step discrete flow distillation 的瓶颈可能在 teacher trajectory target；training-only energy navigator 可在 midpoint 候选中选择较可信路径。",
        "TS-DFM 在小步距直接使用 frozen teacher，大步距用 RK-4 semi-teacher 构造候选，并以 energy compass 在 t≥tau 时选择 midpoint；主结果覆盖不同 source distributions/NFE，Table 2 检查 tau 与 diversity，Table 3 报训练开销。",
        "energy 只在训练中评价候选且可能偏向低熵路径；更早启用可降低 perplexity却损失 diversity，teacher/energy bias 会传给 student。指标或分布漂移时回退普通 DFM trajectory、更多 sampling steps 或统一 distillation。",
        "Ch24 已讨论 teacher trajectory、off-trajectory state 与 temporal-aware distillation，但没有 training-only midpoint energy selection 以及 quality–diversity/tau 的控制边界。",
        ("§3 background；§4 Method: navigation shaping；Appendix A/C.5", "§5–§5.2；Table 1–3；Figure 1–3；Appendix E", "§6 Conclusion；无独立 Limitations 标题，按 teacher/energy/diversity/NFE 范围收窄"),
        "no immutable implementation identity captured; no reproduction claim adopted",
        "flow-distillation-energy-midpoint-trajectory", "Ch24 trajectory distillation 主线，在 teacher-target/off-trajectory 讨论后。",
        "Few-step flow distillation 不一定受 student capacity 限制；若 teacher trajectory 用盲目随机 midpoint 构造，target 本身就可能偏离高质量路径。训练端可让冻结 teacher 生成多个 midpoint candidate，再由仅训练期可见的 energy navigator 选择 target，student runtime 不携带该 navigator。它用额外 teacher/energy compute 换更好的低 NFE trajectory，也会继承 energy bias并压低 diversity；tau、teacher、energy 与 source distribution 必须进入训练身份，entropy 或任务质量越界时回退普通 DFM trajectory、更多 sampling steps 或统一 distillation。 [受限证据：arXiv:2605.07924v1]"),
    "2605.07933": spec((3, 2, 3), "MULTIMODAL-GENERATIVE-PARADIGMS", I,
        "latent diffusion language model 联合训练 encoder、diffusion 与 decoder 时需要 staged warmup/noise/objective contract，避免表示与生成共同 collapse。",
        "LDLM 以 frozen token encoder、trainable latent encoder/diffusion/latent decoder/token decoder联合目标训练；实验比较 decoder losses、diffusion-to-encoder warmup、decoder noise 与 time sampling，并在 OWT/LM1B 等测 generation perplexity、entropy 与 NFE。",
        "联合目标增加 reconstruction、smoothness、diffusion 与 decoder 的耦合；warmup/noise 失配会 collapse，PPL/entropy 不等于语义事实或 serving SLO。训练不稳时回退 staged freeze、离散 diffusion 或 AR。",
        "Ch24 已有 text VAE→latent diffusion→decoder factorization 与各阶段 failure，但没有说明端到端 joint objective 的 warmup/noise 如何防止 latent/decoder 共塌缩。",
        ("§4–§4.3；Appendix A/A.1", "§6；§8；Figure 1–5；Table 1；Appendix B/D", "§9 Conclusion；Appendix G Limitations"),
        "no immutable implementation identity captured; no reproduction claim adopted",
        "joint-latent-diffusion-staged-training", "Ch24 continuous latent diffusion 文本分支，在 Text VAE/latent/decoder factorization 后。",
        "把 Text VAE、latent diffusion 和 token decoder 分阶段冻结训练最容易定位失败；端到端 joint training 能让表示与生成共同适配，却也可能让 encoder 缩放、diffusion loss 和 decoder reconstruction 相互追逐而 collapse。训练 artifact 应保存 encoder/diffusion/decoder revisions、diffusion-to-encoder warmup、decoder noise、loss weights 与 time sampling，并分别验收 reconstruction、latent smoothness、PPL/diversity 和 NFE。任一阶段不稳时回退 staged freeze、离散 diffusion 或 AR，不能用单一生成分数掩盖表示塌缩。 [受限证据：arXiv:2605.07933v1]"),
    "2605.08061": spec((3, 3, 3), "TRAIN-GRPO", I,
        "GRPO reward 可由 policy 不可见的 grounding passage 与 weighted rubric 生成 criterion-level credit，但 judge 只能拥有受限评分，不能拥有事实或发布 authority。",
        "Rubric-Grounded RL 离线从技术文档合成 question/grounding/weighted-rubric，在线 policy 只见 question；冻结 judge 读取隐藏 grounding 和 rubric，输出 criterion scores 聚合为 normalized reward供 GRPO。held-out rubric reward、reasoning transfer 与 reward dynamics 是评价边界。",
        "同一 judge 参与训练与主评价会产生 shared-bias/overoptimization，合成 rubric/weight 可能错误，hidden passage 不代表开放世界真值；证据限作者 8B policy、GPT-OSS judge 与语料。高风险或 judge 漂移时回退 executable verifier、人工 rubric、outcome-only reward 或保留 Unknown。",
        "Ch33 已分离 reward/verifier 与 policy，并讨论 token/step credit；但尚未定义 policy-invisible grounding、weighted criteria、criterion-level scores 与 judge authority 的接口。",
        ("§3 Method；Judge Prompt Architecture；Training Objective；Appendix A", "§4–§5；Table 1–2；Figure 1–3；Algorithm 1", "§6 Discussion；§7 Limitations；§8 Conclusion"),
        "no immutable corpus/code identity captured; no reproduction claim adopted",
        "hidden-grounding-rubric-reward-authority", "Ch33 ‘Sequence Reward 怎样作用到 Tokens’，在 process reward/verifier 边界之前。",
        "Outcome verifier 稀缺时，可以让 policy 不可见的 grounding passage 与 weighted rubric 产生 criterion-level reward：policy 只生成答案，冻结 judge 读取受控证据并逐项打分，trainer 再按声明权重聚合给 GRPO。Grounding、rubric、weight、judge 与 policy revision 必须共同标识；judge 只拥有该协议内的 score，不拥有事实或发布 authority。同一 judge 同时训练和评价会造成 shared-bias 与 reward overoptimization，合成 criteria 也可能错误；高风险或漂移时回退 executable verifier、人工 rubric、outcome-only reward 或 Unknown。 [受限证据：arXiv:2605.08061v1]"),
}

B = {
    "2605.07068": spec((3, 2, 3), "AGENT-MEMORY", N,
        "持久 wiki-memory 的编译必须以 probe 驱动的 counterexample/refinement 检查事实丢失，不能把压缩率或 TTFT 当完整性证明。",
        "WiCER 在 17 RepLiQA domains/6,800 questions 上先测 full-context、RAG 与 blind compilation，再以 diagnostic probes 定位 dropped facts，迭代 pinning/refine；ablation 显示 targeted diagnosis 而非 generic pinning 贡献恢复。",
        "probe coverage 决定能发现哪些丢失，LLM judge 与 curated knowledge 限制外推；attention dilution 和编译误差并未消失。关键事实、来源更新或 probe 不足时回退原文 retrieval/full context。",
        "Ch77 已规定 memory write 必须由 non-writing distillation 产出 candidate、用只读 counterexample/precondition/freshness probes 验证，再由唯一 writer commit；也保留 source revision、compiler/judge 与 retrieval fallback。WiCER 是该合同的 wiki 编译实例。",
        ("§3 setup/config/evaluation；§7.1 Algorithm 1；§7.2", "§5–§6；Table 1–5", "§7.4 Analysis and Limitations；§8 Discussion and Conclusion"),
        "exact-v1 says code/benchmarks are released, but no immutable artifact revision was captured; no reproduction claim adopted"),
    "2605.07079": spec((3, 2, 3), "MULTIMODAL-WORLD-MODELS", N,
        "feature-space World Model 应把可预测 residual transition 压成 latent action，并用 action-conditioned outcome 而非视觉清晰度验证其可规划性。",
        "RLA 从 DINO residual 学 compact latent action，RLA-WM 以 flow matching 预测 residual，再用于 actionless-video imitation 与 offline-video world-model RL；future-frame、latent-action 与 policy success 分层评价。",
        "DINO residual/flow metric 不等于物理真值，offline world rollout 仍受 support gap 与 hallucination；真实 controller 拥有 action commit。表示或 action support 越界时回退 pixel/structured simulator 或真实短 horizon observation。",
        "Ch25 已明确 feature/latent prediction 的 encoder identity、representation collapse、action-conditioned outcome 与 closed-loop task gate，并要求 unsupported action 回退高保真 simulator/真实 observation；RLA 是现有 residual latent branch 的具体实现。",
        ("§3 Method", "§4–§4.1；Table 1–2；Figure 1–4", "§5 Limitations and Conclusion；Appendix A.3"),
        "project page disclosed in abstract; no immutable code/model revision captured; no reproduction claim adopted"),
    "2605.07110": spec((2, 2, 2), "PLATFORM-SECURITY", N,
        "Computer-Use Agent 安全应沿 perception/decision/execution 与 creation/deployment/operation/maintenance 的交叉面定位 authority-bearing failure。",
        "该综述把 software interaction 写成 partially observable control，建立 architecture–lifecycle coordinate system，并映射 capability formation、permission binding、runtime trajectory 与 maintenance drift 的威胁/控制面；OpenClaw 只是公开例子。",
        "这是分析框架，不提供系统实证或 OpenClaw 内部验证；分类不能证明控制充分。生产仍需 effect-time authorization、trace/evidence、sandbox 与人工 gate。",
        "Ch72 已按 input/context/model/tool/memory/output 与 build/deploy/runtime/maintenance 串联 threat、authority、preventive/evidential gate，且明确 benchmark success 不等于 release readiness；该综述不改变现有安全 owner。",
        ("§II Problem Definition and Design Axes；§III Analytical Framework", "§VI Security and Privacy Analysis；§VIII-C", "§VI-A–§VI-D threat scope；综述性非实证边界"),
        "not required for the adopted survey framework; no implementation claim adopted"),
    "2605.07112": spec((3, 3, 2), "AGENT-TOOL-CALLING", N,
        "tool-calling model router 应在 correctness hard condition 下选择最低总成本模型，并把 token-intensive reasoning、router latency 与 function-call structure 纳入成本。",
        "Switchcraft 用五个 function-calling benchmarks、AST scorer 与 model outputs 训练 DistilBERT router；held-out 12,282 examples 比较 accuracy/cost Pareto、latency、robustness 与 token packing。",
        "训练 label 继承 scorer/model pool 偏差，price 与 tool schema 会漂移；成本最优不授权具体 tool effect。分布外、高风险或 classifier 不确定时回退已认证大模型、deterministic tool gate 或人工。",
        "Ch78 已把 tool necessity、catalog/routing、benefit-latency-failure-risk 与 preventive/evidential execution gates 分离；router 只提议模型/工具，correctness 与 effect authority 仍独立。该成本分类器不新增 owner。",
        ("§3 Design；Appendix B/E.1", "§4–§4.6；Table 1–3；Figure 1–3", "§5 Limitations；§7 Conclusions；Appendix J.4"),
        "no immutable router/checkpoint artifact captured; no reproduction claim adopted"),
    "2605.07180": spec((3, 2, 3), "AGENT-PLATFORM", N,
        "LLM→Agent escalation router 可用少量 early paired experience 建立能力边界，但经验 memory 只提供 routing evidence，不拥有任务结果。",
        "BoundaryRouter 在 seed set 上同时执行 direct LLM 与 full Agent，构建 compact experience memory，检索相似案例并用 rubric-guided reasoning 路由；RouteBench 覆盖 in-domain、paraphrase、OOD 与 solver-balanced F1/accuracy/time。",
        "early experience 会稀疏、过期并受 benchmark label/rubric 偏差影响；相似任务不保证同一最优 solver。冷启动或高风险时回退静态能力表、全 Agent 或人工 escalation。",
        "Ch84 已把 capability routing、paired marginal-utility gate、task/skill compatibility、versioned outcome ledger 与静态 fallback 写入 Agent platform；该 early-memory router 是现有 admission 分支。",
        ("§3 BoundaryRouter；Appendix A.3", "§4–§5；Table 1；Figure 1–5", "§6 Discussion and Conclusion；按 cold-start/benchmark/model 范围收窄"),
        "no immutable implementation identity captured; no reproduction claim adopted"),
    "2605.07288": spec((3, 2, 3), "MULTIMODAL-WORLD-MODELS", N,
        "用 World Model 作为 VLA simulator 时，style perturbation 与 long-horizon error accumulation 必须作为独立可靠性切片，并保持训练/推理 latent-state 一致。",
        "Sword 用 structure-guided style augmentation 解耦视觉 texture 与 task dynamics，以 Dynamic Latent Bootstrapping 维持 rollout state并控制 memory；LIBERO 上比较 OOD style、prediction fidelity、long horizon 与 RL post-training success。",
        "style augmentation 不覆盖动力学/接触 OOD，bootstrapping 会自举错误；simulator success 不证明 sim-to-real。状态/动作 support 越界时回退真实 observation、显式 simulator 或短 horizon replanning。",
        "Ch25 已要求 observed/latent/imagined state 分离、style/visual plausibility 不能替代 action consequence、long-horizon calibration 与 closed-loop outcome，并定义 simulator/support fallback；Sword 未改变该合同。",
        ("§3–§3.3；training objective", "§4–§5.2；Figure 1–4；Table 1–2", "§6 Conclusion and Limitations"),
        "no immutable implementation identity captured; no reproduction claim adopted"),
    "2605.07442": spec((3, 3, 3), "PLATFORM-EVALUATION-SYSTEM", N,
        "长程交互程序的验证应把 specification 分解为 keypoints，以 runtime state injection 到达目标状态，再执行有界 interaction 并返回 falsifying witness。",
        "GameGen-Verifier 将 game spec ground 成 state/interaction/expected-outcome units，白盒 patch runtime 后并行执行；GGV-Harness 提供 isolation、concurrency、fault recovery，VeriGame 100 games 上与 human judgment/AaaV 对比。",
        "state injection 可能绕过真实 reachability，keypoint extraction/judge 会漏掉组合规则；只证明独立断言不等于完整游戏正确。无法白盒注入或关键状态耦合时回退真实 gameplay、property tests 与人工。",
        "Ch66 已规定 EvalSpec 要分解可执行断言、用独立 environment/effect state 验证、保留 reachability/coverage 与 falsifying evidence，且 no-op/outcome 不由 Agent 自证；该 game harness 是现有 contract 的领域实例。",
        ("§3–§4 GameGen-Verifier/GGV-Harness；Figure 3", "§5–§5.2；Table 1–2", "§6 Limitations；§7 Conclusion；Broader Impact"),
        "no immutable harness/dataset revision captured; no reproduction claim adopted"),
    "2605.07451": spec((2, 2, 3), "PLATFORM-EVALUATION-SYSTEM", N,
        "verification query 标准必须把 syntax、types 与 model semantics 分开版本化，不能把不断变化的外部 ONNX 语义当作隐式真值。",
        "VNN-LIB 2.0 定义 abstract network theory、查询 syntax/type system/formal semantics，并用 Agda mechanization 检查内部一致；Figures 1–6 给出 declaration 与 semantics 结构。",
        "形式化只相对 network theory 与实例化 model-format semantics；不证明任意 ONNX exporter/solver/浮点 kernel正确，也没有 benchmark。实例化不完整时回退固定版本 translator、solver cross-check 与 concrete execution。",
        "Ch66 已要求 evaluation/spec schema、artifact/backend/version 与 deterministic semantics 共同冻结，并区分形式 verifier 与真实 runtime outcome；VNN-LIB 2.0 是该 versioned interface 原则的专用标准。",
        ("§2–§9 formal foundations；Figure 1–6", "formal mechanization consistency only; exact-v1 has no empirical evaluation section", "§10 Conclusion；network-theory instantiation/ONNX semantics boundary"),
        "Agda mechanization is stated, but no immutable artifact revision captured; no proof-reproduction claim adopted"),
    "2605.07514": spec((3, 2, 3), "MULTIMODAL-EMBODIED-VLA", N,
        "World Action Model 的 imagined future 必须评估 action–state dynamic consistency，并防止静态 background collapse 伪造高一致性。",
        "论文跨 joint-prediction/inverse-dynamics models 比较 consistency 与 rollout success/value，定位低 dynamics failure 的 background collapse，并用 candidate-future consensus 做 value-free test-time selection；RoboCasa/RoboTwin 2.0 分任务评价。",
        "consistency 是相关 signal，不是可达性或安全真值；多个候选共享 model bias 时 consensus 仍会共同错误。低 dynamics、contact-critical 或 OOD action 时回退 value/physics verifier、真实 observation 与短 horizon planning。",
        "Ch26 已要求 VLA imagined rollout 同时验证 action consequence、state transition、closed-loop outcome 与真实 controller authority，并把 visual plausibility/latent similarity 降为 sensor；Ch25 又明确 background/latent collapse 与 simulator fallback。该一致性指标不新增 owner。",
        ("§3–§4 dynamic consistency；Appendix E", "§5–§5.2；Figure 1–6；Appendix C", "§6 Conclusion and Future Work；Appendix H Limitations and Failure Analysis"),
        "no immutable implementation identity captured; no reproduction claim adopted"),
    "2605.07547": spec((3, 3, 2), "INFER-SCHEDULING", N,
        "deadline workload 的资源控制应分离慢时标 placement 与快时标 allocation，并让 migration critic 比较中断成本与 SLO 收益。",
        "HAF 以 LLM agent 做 epoch-level AI/RAN placement，以 closed-form deadline-aware convex algorithm 做 event-level GPU/CPU allocation，再由 predictive critic 过滤不划算 migration；simulation 做 load sweep、critic ablation 与 SLO/migration 对比。",
        "结果来自 AI-RAN simulation，LLM placement 与 critic 预测会漂移；平均 SLO 不证明硬实时安全。预测不稳、迁移不可恢复或关键 RAN deadline 时回退静态 placement、保守 reservation 与 hard deadline policy。",
        "Ch56 已分层 offline/profiled templates 与 online allocation，联合 placement/capacity/deadline/migration cost，并要求 predictor 只提议、hard SLO/policy 保留 authority；HAF 是该 slow/fast controller 的领域实现。",
        ("§II System Model；§III Hierarchical Agentic Framework", "§IV；Table I–III；Figure 1–2；critic ablation/load sweep", "§V Conclusion；正文未单列 limitations，按 simulation/AI-RAN/LLM-critic 范围收窄"),
        "no immutable implementation identity captured; no reproduction claim adopted"),
}

SPECS = A | B
assert len(A) == 18 and len(B) == 10 and len(SPECS) == 28


def read_json(path):
    return json.loads(path.read_text())


def write_json(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def score_obj(values):
    a, b, c = values
    return {"design_delta": a, "system_reach": b, "durability": c, "total": a + b + c}


def evidence_item(entry, data):
    m, e, l = data["locators"]
    return {
        "arxiv_id": entry["arxiv_id"],
        "source_family_id": entry["source_family_id"],
        "title": entry["title"],
        "primary": f"https://arxiv.org/html/{entry['arxiv_id']}v1",
        "public_event": PUBLIC_EVENT,
        "review_depth": "deep" if sum(data["score"]) >= 7 else "standard",
        "access_status": "accessible_exact_v1",
        "withdrawal_status": "not_withdrawn_on_official_exact_v1_checked_2026-09-15",
        "score": score_obj(data["score"]),
        "adopted_claim": data["claim"],
        "mechanism_and_evaluation": data["mechanism"],
        "non_proof_tradeoff_and_fallback": data["boundary"],
        "owner": data["owner"],
        "owner_path": OWNER_PATHS[data["owner"]],
        "books_disposition": data["decision"],
        "books_comparison": data["comparison"],
        "evidence_locators": {"method": m, "evaluation": e, "limitations_and_non_proof": l},
        "artifact_status": data["artifact"],
        "reviewed_at": CHECKED_AT,
    }


def decision_label(item, queued):
    owner = item["owner"]
    path = item["owner_path"]
    rel = "../../../../" + path
    if item["books_disposition"] == I:
        suffix = "等待 root 串行写回" if item["arxiv_id"] in queued else "已存在 Books 正文"
        return f"整合：`{owner}`，[{Path(path).name}]({rel})；{suffix}"
    return f"已有覆盖：`{owner}`，[{Path(path).name}]({rel})"


def report_section(item, queued):
    loc = item["evidence_locators"]
    score = item["score"]
    return (
        f"### [{item['title']}]({item['primary']})\n\n"
        f"**采用命题：** {item['adopted_claim']}\n\n"
        f"**机制与评价：** {item['mechanism_and_evaluation']}\n\n"
        f"**证据位置：** Method：{loc['method']}；Evaluation：{loc['evaluation']}；"
        f"Limitations / non-proof：{loc['limitations_and_non_proof']}。Artifact：{item['artifact_status']}。\n\n"
        f"**未证明、代价与回退：** {item['non_proof_tradeoff_and_fallback']}\n\n"
        f"**Books 比较：** {item['books_comparison']}\n\n"
        f"**最终处置：** {decision_label(item, queued)}。\n"
    )


def update_report(evidence_items, queued):
    text = REPORT.read_text()
    text = re.sub(r"\*\*检查时间：\*\* .*", f"**检查时间：** {CHECKED_AT}", text, count=1)
    conclusion = """## 1. 结论

本轮严格只执行 `V3_FRESH_NONAUTHOR_SCREENING_REPAIR_QUEUE_20260915.md` 点名的 28 项，没有扩窗、扩来源或重扫其余 identity。A 组 18 项全部恢复 retained，并逐项完成 official arXiv HTML exact-v1 的 method/evaluation/non-proof 定位；B 组 10 项也全部恢复 retained，因为逐项旧证据与当前 owner 对照仍通过 contribution gate，不能用 generic closure 回退。direct 算术现冻结为 `635 = 102 retained + 533 pre-denominator closure`，整体为 `826 = 102 + 533 + 191`。

102 个候选均有 exact-v1 Evidence Review；Books 判断重冻为 42 Integrate、58 No Change、2 仅报告。既有 26 个 Integrate 已由 root 写回并通过此前写后复核；本次新增 16 个 Integrate 仅进入精确 root queue，作者未编辑共享 Books。`2605.06690` 的 typed epistemic stopping 与 `2605.07443` 的任意块 KV 复用/分层存储/position-conditioning 修复已由当前 Books owner 完整承载，A 组恢复 retained 不等于强制制造重复正文；B 组 10 项均给出命题级 No Change 对照。

Daily 保持进行中。下一 Gate 是 root 对新增 16 项执行串行 Books 写回，再由未参与本次返修的新 non-author reviewer 核验 exact-v1、正文 binding 与 denominator；作者侧不自签 Complete。
"""
    text = re.sub(r"## 1\. 结论\n.*?(?=\n## 2\.)", conclusion.rstrip() + "\n", text, count=1, flags=re.S)

    evidence_by_id = {x["arxiv_id"]: x for x in evidence_items}
    table_start = text.index("| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |")
    table_end = text.index("\n\n## 4. 证据与知识整合", table_start)
    header = "| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |\n| --- | --- | --- | --- | --- |"
    rows = []
    for aid in sorted(evidence_by_id):
        item = evidence_by_id[aid]
        s = item["score"]
        depth = "深入完成" if item["review_depth"] == "deep" else "标准完成"
        rows.append(
            f"| [{item['title']}]({item['primary']}) | {PUBLIC_EVENT.split(' scheduled')[0]} | "
            f"{item['adopted_claim']}；{s['design_delta']} + {s['system_reach']} + {s['durability']} = {s['total']} | "
            f"{depth} | {decision_label(item, queued)} |"
        )
    text = text[:table_start] + header + "\n" + "\n".join(rows) + text[table_end:]

    section_start = text.index("## 4. 证据与知识整合")
    section_end = text.index("\n## 5. 缺口与下一步", section_start)
    section_text = text[section_start:section_end]
    for aid in SPECS:
        title = re.escape(evidence_by_id[aid]["title"])
        section_text = re.sub(rf"\n### \[{title}\].*?(?=\n### \[|\Z)", "", section_text, flags=re.S)
    appended = "\n\n".join(report_section(evidence_by_id[aid], queued) for aid in sorted(SPECS))
    section_text = section_text.rstrip() + "\n\n" + appended + "\n"
    text = text[:section_start] + section_text + text[section_end:]

    tail = """## 5. 缺口与下一步

1. screening denominator 已按有界 28 项返修并冻结：`826 = 102 retained + 533 direct closure + 191 owner-day isolation`；没有重开 11 个 DataCite isolation control，也没有扩窗/扩源。
2. 102/102 retained 已有 exact-v1 Evidence Review 与 Books comparison；本轮无材料 blocker。
3. Books 当前为 42 Integrate / 58 No Change / 2 仅报告；26 个旧 Integrate 已写回，本次 16 个新 Integrate 只列入 `V3_SCREENING_REPAIR_ROOT_BOOKS_QUEUE_20260915.md` 与 JSON queue，等待 root 串行写回。
4. root 写回后必须由新的 non-author fresh-context reviewer 核验 28 项 screening repair、16 个 Books binding、算术与 Complete Gate；作者侧保持 Ongoing。
5. 后续事件日 owner 继续分别处理 `2605.06738`、`2605.06772`、`2605.07210`、`2605.07527`、`2605.07818`、`2605.08051` 的官方后续修订信号；它们不计作 2026-05-11 的新 revision event。

## 6. 复核

**返修者：** 2026-05-11 author lane；严格按 fresh non-author queue 执行，不具备本轮独立完成签字权。

**结论：** author repair checkpoint 已落盘；screening 算术、28 项 exact-v1 Evidence 与 Books comparison 已重冻。由于 16 项 Books 写回及其 fresh non-author 复核尚未完成，Daily 保持 Ongoing，不签 Complete。

机器校验只能证明 JSON、评分、分母算术、版本 basis 引用、唯一 owner、链接字段与 Markdown 结构一致；不能替代 root Books 写回或独立语义复核。

**Repository Changes：** 本轮只更新 2026-05-11 Daily、active screening ledger、Evidence/Books comparison、root queue 与作者 checkpoint；未修改 Books，未 stage、commit 或 push。
"""
    text = re.sub(r"## 5\. 缺口与下一步\n.*\Z", tail, text, count=1, flags=re.S)
    REPORT.write_text(text)


def main():
    ledger = read_json(LEDGER)
    evidence_doc = read_json(EVIDENCE)
    comparison_doc = read_json(COMPARISON)
    queue_doc = read_json(QUEUE_JSON)

    ledger_by_id = {x["arxiv_id"]: x for x in ledger["entries"]}
    evidence_by_id = {x["arxiv_id"]: x for x in evidence_doc["items"]}
    comparison_by_id = {x["arxiv_id"]: x for x in comparison_doc["items"]}
    queue_by_id = {x["arxiv_id"]: x for x in queue_doc["items"]}

    for aid, data in SPECS.items():
        entry = ledger_by_id[aid]
        entry["v3_status"] = "retained"
        entry["withdrawal_signal"] = "none_in_official_exact_v1_checked_2026-09-15"
        group = "A definite false-negative" if aid in A else "B retained-regression"
        entry["reason"] = f"按 fresh non-author 有界 queue 重审为 {group}。完整题名与摘要触发 contribution gate：{data['claim']}；已读取 official arXiv HTML exact-v1，不得在候选分母前用 generic closure 关闭。"
        evidence_by_id[aid] = evidence_item(entry, data)
        comparison_by_id[aid] = {
            "arxiv_id": aid,
            "source_family_id": entry["source_family_id"],
            "owner": data["owner"],
            "owner_path": OWNER_PATHS[data["owner"]],
            "disposition": data["decision"],
            "adopted_claim": data["claim"],
            "proposition_level_comparison": data["comparison"],
        }
        if data["decision"] == I:
            queue_by_id[aid] = {
                "source_family_id": entry["source_family_id"],
                "arxiv_id": aid,
                "owner": data["owner"],
                "target_path": OWNER_PATHS[data["owner"]],
                "binding_id": data["binding"],
                "insertion_point": data["insertion"],
                "final_prose": data["prose"],
                "tradeoff_and_fallback": data["boundary"],
                "evidence_boundary": f"https://arxiv.org/html/{aid}v1；Method={data['locators'][0]}；Evaluation={data['locators'][1]}；non-proof={data['locators'][2]}；Artifact={data['artifact']}。",
                "write_status": "pending_root_serialized_books_writeback",
            }

    evidence_doc["items"] = sorted(evidence_by_id.values(), key=lambda x: x["arxiv_id"])
    evidence_doc["reviewed_at"] = CHECKED_AT
    comparison_doc["items"] = sorted(comparison_by_id.values(), key=lambda x: x["arxiv_id"])
    comparison_doc["reviewed_at"] = CHECKED_AT
    comparison_doc["scope"] = "bounded author-side Books comparison for the 14 prior repair items plus the fresh non-author 28-item screening queue; no shared Books mutation"
    queue_doc["items"] = sorted(queue_by_id.values(), key=lambda x: x["arxiv_id"])
    queue_doc["status"] = "16_new_items_awaiting_root_serialized_books_writeback_report_ongoing"

    summary = ledger["summary"]
    summary.update({
        "retained_candidates": 102,
        "pre_denominator_closed_direct": 533,
        "evidence_accessible_exact_v1": 102,
        "false_negatives_restored": 73,
        "books_integrate": 42,
        "books_applied": 26,
        "books_pending_root": 16,
        "books_no_change": 58,
        "books_report_only": 2,
    })
    ledger["screening_repair_20260915"] = {
        "review_basis": "V3_FRESH_NONAUTHOR_SCREENING_REPAIR_QUEUE_20260915.md",
        "scope": "28 named official-announcement-direct identities only; no window/source expansion or denominator rescan",
        "group_a_restored_retained": sorted(A),
        "group_b_restored_retained": sorted(B),
        "exact_v1_reviewed": 28,
        "new_integrate_pending_root": sorted(aid for aid, data in SPECS.items() if data["decision"] == I),
        "no_change_after_current_owner_comparison": sorted(aid for aid, data in SPECS.items() if data["decision"] == N),
        "checked_at": CHECKED_AT,
        "state": "author_repair_complete_report_ongoing_pending_root_books_and_fresh_nonauthor_review",
    }

    queued = {aid for aid, data in SPECS.items() if data["decision"] == I}
    assert len(queued) == 16
    assert sum(1 for x in ledger["entries"] if x["v3_status"] == "retained") == 102
    assert summary["retained_candidates"] + summary["pre_denominator_closed_direct"] == summary["official_announcement_direct"] == 635
    assert summary["retained_candidates"] + summary["pre_denominator_closed_direct"] + summary["owner_day_recovery_closed"] == 826
    assert len(evidence_doc["items"]) == 102
    assert sum(1 for x in evidence_doc["items"] if x["books_disposition"] == I) == 42
    assert sum(1 for x in evidence_doc["items"] if x["books_disposition"] == N) == 58
    assert sum(1 for x in evidence_doc["items"] if x["books_disposition"] == "仅报告") == 2
    assert sum(1 for x in queue_doc["items"] if x["write_status"] == "pending_root_serialized_books_writeback") == 16

    write_json(LEDGER, ledger)
    write_json(EVIDENCE, evidence_doc)
    write_json(COMPARISON, comparison_doc)
    write_json(QUEUE_JSON, queue_doc)

    queue_lines = [
        "# 2026-05-11 screening 返修：root Books 写回清单",
        "",
        "本文件只列本次 28 项有界 screening 返修产生的 16 个真实 Integrate。权威 prose、唯一 binding、位置与 evidence boundary 位于 `V3_BOOKS_WRITEBACK_QUEUE_20260914.json`；作者侧未编辑共享 Books。",
        "",
    ]
    for aid in sorted(queued):
        data = SPECS[aid]
        queue_lines.append(f"- `{aid}` → `{data['owner']}` / `{OWNER_PATHS[data['owner']]}`；binding=`{data['binding']}`；位置：{data['insertion']}")
    queue_lines += [
        "",
        "root 写回后需新的 non-author fresh-context reviewer 逐项核验 exact-v1 adopted claim、正文唯一 binding、trade-off/failure/fallback 与相邻 owner；当前 Daily 保持 Ongoing。",
        "",
    ]
    QUEUE_MD.write_text("\n".join(queue_lines))

    checkpoint = f"""# 2026-05-11 screening 有界作者返修 checkpoint

- checked at: {CHECKED_AT}
- authority: author-side repair only；不得自签 Complete
- scope: fresh non-author queue 点名 28 项（A18 + B10）；未扩窗、扩源、重扫或触碰 11 个 DataCite isolation controls
- exact-v1: 28/28 official arXiv HTML v1 可访问并完成 method/evaluation/non-proof 定位；material blockers=0
- denominator: `826 = 102 retained + 533 direct closure + 191 owner-day isolation`；direct=`635 = 102 + 533`
- A group: 18/18 restored retained；16 Integrate / 2 No Change
- B group: 10/10 restored retained；0 Integrate / 10 No Change；无 generic closure
- Books disposition: 42 Integrate / 58 No Change / 2 仅报告；26 prior applied / 16 pending root
- root queue: `V3_SCREENING_REPAIR_ROOT_BOOKS_QUEUE_20260915.md`；共享 Books 未修改
- state: Ongoing；等待 root 串行写回 16 项与新的 non-author fresh review

## Degraded doubt-driven note

本 author lane 不能同时充当独立 reviewer。已进行逐项反证式自查（denominator、owner、非证明边界与 fallback），但根据独立性合同跳过同上下文/同作者的自签；fresh challenge 必须由 root 后续交给未参与本次返修的 reviewer。
"""
    CHECKPOINT.write_text(checkpoint)
    update_report(evidence_doc["items"], queued)


if __name__ == "__main__":
    main()
