# 2026-06-29 Ready-to-Insert Books Packet V1

Status: READY FOR INDEPENDENT PREWRITE REVIEW; shared Books not modified.

## `AGENT-CONTEXT` → `books/part-07-agent/75-context.md`

**Owner-merged 正文（覆盖 `SF-2026-ARXIV-2606-29522`）。** 现有 Context 正文区分 raw evidence、derived view 与 compression fidelity，但没有验证 scratchpad register 是否被后续计算因果读取的 intervention contract。 因此本次把这些增量合并到同一知识 owner：Scratchpad 不能仅按可见文本保存；因果干预结果应把其中哪些 register 实际驱动后续输出记录成 request-local diagnostic state。该 probe 只拥有观测/路由权，干预不稳定时回退原始 scratchpad 与外部 verifier，不能据此删除未被识别的约束。 共同代价与回退边界是：只在 Q8/D8 合成 transition task、Qwen2.5-Coder-7B 与 Mistral-7B-v0.3 上证明特定 written state 被因果读取；显式 scratchpad 的其他 token、自然语言推理和真实 Agent memory 均未被证明忠实。probe 不稳定时保留原文本与外部 verifier。

Review note：`SF-2026-ARXIV-2606-29522`；Method `https://arxiv.org/html/2606.29522v1 — §6 Mechanism and alignment interpretation; scratchpad intervention`；Evaluation `https://arxiv.org/html/2606.29522v1 — §5 Results`；未证明边界 `https://arxiv.org/html/2606.29522v1 — §Conclusion and intervention-identifiability scope`。

## `AGENT-MULTI-AGENT` → `books/part-07-agent/82-multi-agent.md`

**Owner-merged 正文（覆盖 `SF-2026-ARXIV-2606-29270`、`SF-2026-ARXIV-2606-29601`、`SF-2026-ARXIV-2606-29654`）。** 现有 Multi-Agent 正文有 aggregation 与 independent verification，但缺少在多数错误相关时保存 minority evidence、以预校准 Flip Precision 决定是否推翻 majority commit 的协议状态。 现有 Multi-Agent 正文有 topology、message state 与 delegation，却没有把 attribute sayso、action nono/nogo 编译为可做 safety/liveness 检查的异步协议。 现有 Multi-Agent 正文有 verifier 与 coordination tax，却没有在部署前将 wrong-action budget 分解为校准失败、残余行动风险和 representation gap，并据 local lower bound 决定 act/defer。 因此本次把这些增量合并到同一知识 owner：多数投票不再自动提交；aggregation owner 保存 minority-sentinel evidence、override criterion 与最终 commit receipt，只在少数意见显示独立且校准的反证时推翻多数。相关错误或 sentinel 失准时回退独立 verifier/人工，而不是继续增加同源 Agent。 异步多 Agent 协议应把 attribute-setting priority、action conflict 与禁止组合编译为 sayso/nono/nogo 等声明式状态，再由协议 runtime 决定可提交 transition。规则冲突或编译覆盖不足时回退串行 coordinator/人工仲裁。 多 Agent deliberation 的 automation 权由预先声明的 wrong-action budget 和 local reliability lower bound 决定；controller 记录 act/defer 与预算消耗，低于下界即升级或拒答。校准失效时回退全 defer/人工，不用事后挑阈值美化覆盖率。 共同代价与回退边界是：只证明三异构 Agent、两轮、六 benchmark 的 debate-log classifier 能在已测阈值上安全翻转；共享训练导致的相关错误、换模型和换协议都可能破坏 81.2% Flip Precision。失配时不翻转并交给独立 verifier/人工。 只验证有限 Langshaw examples 到 BSPL tableau 的 safety/liveness 与编译时间；未证明开放网络中的 delivery、identity、Byzantine role 或工具副作用。协议编译/验证超界时回到串行 coordinator 与人工仲裁。 保证依赖 local bias envelope、representation-gap bound 与 calibration split，并非 distribution-free；六个选择题 benchmark 与训练期 difficulty-normalized budget 未证明开放式任务或分布漂移。诊断失败时全 defer/人工。

Review note：`SF-2026-ARXIV-2606-29270`；Method `https://arxiv.org/html/2606.29270v1 — §3 Our Method; 3.3 The Debate Fingerprint; 3.4 Cure Phase: Meta-Classifier and Threshold Strategy`；Evaluation `https://arxiv.org/html/2606.29270v1 — §4 Experiments and Results; 4.1 Datasets and Debate Configuration; 5.5 Multi-Seed Stability`；未证明边界 `https://arxiv.org/html/2606.29270v1 — §6.2 Limitations`。

Review note：`SF-2026-ARXIV-2606-29601`；Method `https://arxiv.org/html/2606.29601v1 — §Approach; sayso, nono and nogo protocol semantics`；Evaluation `https://arxiv.org/html/2606.29601v1 — §6.2 Empirical Results; safety and liveness procedures`；未证明边界 `https://arxiv.org/html/2606.29601v1 — §7 Discussion: Conclusion and Perspectives`。

Review note：`SF-2026-ARXIV-2606-29654`；Method `https://arxiv.org/html/2606.29654v1 — §3 Method; Offline: calibration; Online: k-NN lookup; Stopping rule`；Evaluation `https://arxiv.org/html/2606.29654v1 — §6 Experiments; Benchmarks; Difficulty-normalized deployment budgets; 6.1 Main results`；未证明边界 `https://arxiv.org/html/2606.29654v1 — §7 Discussion and Limitations; H Detailed Assumption Diagnostics; N Failure-case decomposition`。

## `AGENT-PLATFORM` → `books/part-07-agent/84-agent-platform.md`

**Owner-merged 正文（覆盖 `SF-2026-ARXIV-2606-29472`）。** 现有 Agent Platform 正文有 observation/action history 与 replay，却没有把连续 gated capture、audio transcript、persistent narration 与离散动作解耦成版本化 observation interface。 因此本次把这些增量合并到同一知识 owner：Computer-use 平台需要把 gated keyframe、audio transcript、persistent narration 与动作回执定义为版本化 observation interface，而不是让模型任意读取连续桌面流。接口 owner 管理 capture/retention 与 action-state identity；视觉 token 稀释或漏帧时回退高保真 capture/人工确认。 共同代价与回退边界是：只覆盖 DynaCU-Bench 浏览器任务与已测 CU models；Gemini 3 Flash 上 keyframe image-token dilution 已构成反例，因此 AOI 不是固定 bundle，也未证明桌面 OS、权限副作用或持续会议场景安全。退回高保真 capture 与人工确认。

Review note：`SF-2026-ARXIV-2606-29472`；Method `https://arxiv.org/pdf/2606.29472v1 — §3 Agent-Computer Observation Interface: gated keyframes, audio transcription and persistent narration`；Evaluation `https://arxiv.org/pdf/2606.29472v1 — §4 DynaCU-Bench design; 5 Main results and ablations`；未证明边界 `https://arxiv.org/pdf/2606.29472v1 — §5 per-model component ablation: keyframe regression through image-token dilution`。

## `AGENT-RAG` → `books/part-07-agent/76-rag.md`

**Owner-merged 正文（覆盖 `SF-2026-ARXIV-2606-29151`、`SF-2026-ARXIV-2606-29571`）。** 现有 RAG 正文有 typed query plan 与固定/校准检索回退，但没有把自然语言 semantic operator 编译为可重写 logical DAG、再由 physical planner 联合提交 backend/router/threshold 的计划对象。 现有 RAG 正文版本化 metric/index identity，但没有把 encoder anisotropy 变成上线前 cosine-versus-rank/L1 的 metric selection diagnostic。 因此本次把这些增量合并到同一知识 owner：旧 RAG 路径把自然语言直接送入固定 retriever；CADENZA 先编译 task-specific operator DAG，再由 logical rewrite 与 physical planner 按 quality/latency/cost 选择 backend。RAG owner 持有 DAG、operator identity 与 plan commit；统计或 backend profile 漂移时回退固定检索计划。 Embedding distance 不应固定为 cosine；retrieval owner 先测 anisotropy，再在同一 corpus/query revision 上选择 cosine、rank 或 L1 类 metric，并把 metric 写入 index identity。诊断漂移或收益不稳时回退已校准 cosine/混合检索。 共同代价与回退边界是：只证明 SemBench 上 intent-specific operator DAG 与异构 backend 的 quality/latency/cost 计划选择；未证明跨 operator 的联合最优、teacher-noise 之外的 label shift，或 Azure/API 与本地模型间可移植性。失配时固定到已校准 retrieval plan。 只比较 19 个 parameter-free metric、19 encoder 与七个静态数据集；0.01 crowded split、dominant-direction removal 和相关性未证明在线 corpus 漂移下的因果门槛，也未覆盖 learned metric。收益消失时恢复已校准 cosine/混合检索。

Review note：`SF-2026-ARXIV-2606-29151`；Method `https://arxiv.org/html/2606.29151v1 — §2.2 System Architecture; 4 Logical Planner; 5 Physical Planner`；Evaluation `https://arxiv.org/html/2606.29151v1 — §7 Experiments; 7.1 Experimental Setup`；未证明边界 `https://arxiv.org/html/2606.29151v1 — §6.3 Robustness; G Validation Set Noise`。

Review note：`SF-2026-ARXIV-2606-29571`；Method `https://arxiv.org/html/2606.29571v1 — §3.4 Geometry measures; 4.3 The cause: a few crowded directions; 4.4 Mechanism and consequences`；Evaluation `https://arxiv.org/html/2606.29571v1 — §3.1 Encoders; 3.3 Datasets; 3.5 Scoring`；未证明边界 `https://arxiv.org/html/2606.29571v1 — §6 Limitations`。

## `INFER-REQUEST-LIFECYCLE` → `books/part-05-inference-system/42-what-happens-during-inference.md`

**Owner-merged 正文（覆盖 `SF-2026-ARXIV-2606-29565`）。** 现有 request state machine 到 RELEASED 为止，没有持有跨请求 idle-window speculative state、base-state identity、confidence gate 与 mutation invalidation。 因此本次把这些增量合并到同一知识 owner：有状态会话的 idle time 可用于推演到下个 decision point；request lifecycle owner 保存 speculative state、acceptance confidence 与 base-state identity，命中后才原子提交。False accept、用户输入或 state drift 立即作废预推进并回退正常 decode。 共同代价与回退边界是：只在 LayerScale 专有 engine、单 H100、70B-class 4-bit target 上测得 capability-gated fast path；8B BF16 不触发 gate，且大量收益为测量常数上的闭式推导。任何 state mutation 或置信漂移都必须 invalidate 并恢复普通 decode。

Review note：`SF-2026-ARXIV-2606-29565`；Method `https://arxiv.org/html/2606.29565v1 — §2 Problem Formulation; speculative pre-positioning state machine`；Evaluation `https://arxiv.org/html/2606.29565v1 — §4 Experimental Setup; 5 Evaluation`；未证明边界 `https://arxiv.org/html/2606.29565v1 — §6 Discussion`。

## `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md`

**Owner-merged 正文（覆盖 `SF-2026-ARXIV-2606-29196`、`SF-2026-ARXIV-2606-29623`）。** 现有 Evaluation 正文管理 dataset/model/evaluator/metric/release 分权，却未把模型识别 evaluation context 的内部 signal 作为 benchmark 污染诊断，并限制其只能触发额外评测。 现有 Evaluation 正文要求 slice、校准与反例，但缺少在零失败观测下以 adaptive rare-event cascade、ruler revision 与 anytime-valid upper envelope持有风险证据。 因此本次把这些增量合并到同一知识 owner：能力评测不能假设模型对 evaluation context 无感；evaluation-awareness probe 必须作为 contamination sensor，按模型尺度和表示深度版本化，并在异常时阻止 pooled score 直接取得 release authority。Probe 迁移失败时回退 blind/held-out protocol 与外部 outcome。 高风险 release 不能用普通 Monte Carlo 的零观察失败推断安全；SCARCE 类 cascade 将 rare-event region、latent ruler、停止条件与概率上界保存为验收证据。Ruler/分布假设失效时恢复更保守采样或保持 Gate Open。 共同代价与回退边界是：SAD 上的线性可恢复性只是一种 operational evaluation-awareness signal；white-box AUROC 与黑盒行为会分离，且 Qwen/Gemma 的深度迁移不构成跨 family scaling law。异常只触发额外 held-out evaluation，不授予直接拒绝权。 MNIST 与 Llama-Guard hidden-state jailbreak fleet 只验证经校准 ruler 的 rare-event estimate；论文明确指出 behavioral fleet 约 2,000 variants 仍不足、Mahalanobis ruler 可结构性失效，跨 corpus 必须重新校准。否则 Gate 保持 Open。

Review note：`SF-2026-ARXIV-2606-29196`；Method `https://arxiv.org/html/2606.29196v1 — §2 Evaluation-Awareness Representations; scale-dependent probe construction`；Evaluation `https://arxiv.org/html/2606.29196v1 — §3 Experimental Setup; 4 Results`；未证明边界 `https://arxiv.org/html/2606.29196v1 — §5 Discussion`。

Review note：`SF-2026-ARXIV-2606-29623`；Method `https://arxiv.org/html/2606.29623v1 — §3 Data-Driven Subset Simulation; 4 Theoretical Guarantees; C Martingale Theory for SCARCE`；Evaluation `https://arxiv.org/html/2606.29623v1 — §5.1 Experiment Setup; 6.1 Experiment Setup; 6.2 Simulation Results`；未证明边界 `https://arxiv.org/html/2606.29623v1 — §7 Conclusion, Limitations, and Extensions; E LLM Transfer Challenges`。

## `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md`

**Owner-merged 正文（覆盖 `SF-2026-ARXIV-2606-29581`）。** 现有 Security 正文有 threat matrix 与 fail-closed release，但未把 quantization precision、sampling temperature、multi-sample stability 与多 benchmark safety slice 联合成同一 release identity。 因此本次把这些增量合并到同一知识 owner：量化验收与 sampling temperature 不能分开：security release matrix 必须联合保存 model/quantization/sampler/multi-sample identity，并在多个 safety benchmark 上检查交互失稳。任一切片回归时回退已验收 precision/decoding 配置，而不是只恢复 greedy 单次测试。 共同代价与回退边界是：当前 official exact-v1 的 Abstract 与 §3 一致披露 9 models、161 configurations、AdvBench+XSTest 与约 322k responses；证据只覆盖以 Pile validation calibration 的 AWQ INT4/GPTQ INT8、2B–8B 模型与静态 AdvBench，未证明 NF4/GGUF/对抗式 calibration、>70B、adaptive jailbreak/prompt injection 或 judge 完美可靠。任一切片回归即恢复已验收 precision/sampler。

Review note：`SF-2026-ARXIV-2606-29581`；Method `https://arxiv.org/html/2606.29581v1 — §3 Methodology; quantization-temperature factorial design`；Evaluation `https://arxiv.org/html/2606.29581v1 — §3.1 Experimental Design; 4 Results`；未证明边界 `https://arxiv.org/html/2606.29581v1 — §5 Discussion`。

## `TRAIN-DATA` → `books/part-04-training-system/27-data.md`

**Owner-merged 正文（覆盖 `SF-2026-ARXIV-2606-29171`）。** 现有 Data 正文拥有 lineage、dedup、contamination 与删除证据，却缺少从训练 pair 经 SAE feature 归因到 learned behavioral policy 的中间可审计层。 因此本次把这些增量合并到同一知识 owner：普通 sample lineage 只能回答数据来自哪里；symbolic mechanistic attribution 进一步把样本影响连接到可解释 behavioral policy，使数据 owner 能把选择、删除或复核请求落到行为证据链。归因仍是模型化证据，符号解释不稳定时保留原数据并回退重训/对照实验。 共同代价与回退边界是：只在 Llama-3.2-3B-Instruct refusal proxy、特定 SAE 与 200 个 SFT pair 上验证一阶符号归因；feature label、Ridge fidelity 与 first-order approximation 不等于真实删除/重训因果。保留原样本与重训对照。

Review note：`SF-2026-ARXIV-2606-29171`；Method `https://arxiv.org/html/2606.29171v1 — §3 Symbolic Mechanistic Data Attribution Framework; 3.2 Symbolic Policy Model; 3.3 Influence Computation`；Evaluation `https://arxiv.org/html/2606.29171v1 — §4 Experimental Setup; 5 Results`；未证明边界 `https://arxiv.org/html/2606.29171v1 — §6 Discussion; Symbolic model fidelity and scope; First-order approximation`。

## `TRAIN-PRETRAINING` → `books/part-04-training-system/28-pretraining.md`

**Owner-merged 正文（覆盖 `SF-2026-ARXIV-2606-29158`）。** 现有 Pretraining 正文分离 optimizer、schedule、batch/tokens 与 scaling identity，但没有记录普通 LR 对 model/data scale 的非线性以及 effective LR 与 D-axis 外推的不同可靠域。 因此本次把这些增量合并到同一知识 owner：固定比例或单变量外推学习率会把 width、depth、token budget 与 schedule 的非线性交互折叠掉；训练控制面应把这些轴和 optimizer/schedule revision 一起冻结后再外推。额外 sweep 提高成本，超出已测尺度时回退邻近规模校准而非沿幂律盲推。 共同代价与回退边界是：只覆盖 GPT-2-style 22M-707M、FineWeb 5B-100B tokens、WSD 与 AdamW/AdamH；论文明确显示 log-linear LR 仅局部成立，不能外推到其他架构、optimizer 或更大规模。超界时重新 sweep 邻近尺度。

Review note：`SF-2026-ARXIV-2606-29158`；Method `https://arxiv.org/html/2606.29158v1 — §3 Power Laws for Optimal Learning Rates; 6 Explaining Nonlinear Scaling via Implicit Effective Learning Rate Schedule`；Evaluation `https://arxiv.org/html/2606.29158v1 — §4 Experiment Design; 5 Main Results`；未证明边界 `https://arxiv.org/html/2606.29158v1 — §7 Conclusions and Limitations`。

