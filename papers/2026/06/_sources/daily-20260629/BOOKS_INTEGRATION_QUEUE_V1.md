# 2026-06-29 Books Integration Queue V1

Status: PREWRITE ONLY. Denominator `daily-v2.1:2026-06-29:3f607817d0a16d2b`; 13 Integrate / 67 No Change / 6 Weekly Only across 9 write owners.

## `AGENT-CONTEXT` → `books/part-07-agent/75-context.md`

- `SF-2026-ARXIV-2606-29522` — Do Models Read What They Write? Causal Registers in Scratchpad Reasoning
  - Delta: Scratchpad 不能仅按可见文本保存；因果干预结果应把其中哪些 register 实际驱动后续输出记录成 request-local diagnostic state。该 probe 只拥有观测/路由权，干预不稳定时回退原始 scratchpad 与外部 verifier，不能据此删除未被识别的约束。
  - Boundary: 只在 Q8/D8 合成 transition task、Qwen2.5-Coder-7B 与 Mistral-7B-v0.3 上证明特定 written state 被因果读取；显式 scratchpad 的其他 token、自然语言推理和真实 Agent memory 均未被证明忠实。probe 不稳定时保留原文本与外部 verifier。

## `AGENT-MULTI-AGENT` → `books/part-07-agent/82-multi-agent.md`

- `SF-2026-ARXIV-2606-29270` — Minority Sentinel: When to Overturn Majority Voting in Multi-Agent LLM Debates
  - Delta: 多数投票不再自动提交；aggregation owner 保存 minority-sentinel evidence、override criterion 与最终 commit receipt，只在少数意见显示独立且校准的反证时推翻多数。相关错误或 sentinel 失准时回退独立 verifier/人工，而不是继续增加同源 Agent。
  - Boundary: 只证明三异构 Agent、两轮、六 benchmark 的 debate-log classifier 能在已测阈值上安全翻转；共享训练导致的相关错误、换模型和换协议都可能破坏 81.2% Flip Precision。失配时不翻转并交给独立 verifier/人工。

- `SF-2026-ARXIV-2606-29601` — Langshaw: Declarative Interaction Protocols Based on Sayso and Conflict
  - Delta: 异步多 Agent 协议应把 attribute-setting priority、action conflict 与禁止组合编译为 sayso/nono/nogo 等声明式状态，再由协议 runtime 决定可提交 transition。规则冲突或编译覆盖不足时回退串行 coordinator/人工仲裁。
  - Boundary: 只验证有限 Langshaw examples 到 BSPL tableau 的 safety/liveness 与编译时间；未证明开放网络中的 delivery、identity、Byzantine role 或工具副作用。协议编译/验证超界时回到串行 coordinator 与人工仲裁。

- `SF-2026-ARXIV-2606-29654` — Budgeted Act-or-Defer Multi-Agent LLM Deliberation with Local Reliability Bounds
  - Delta: 多 Agent deliberation 的 automation 权由预先声明的 wrong-action budget 和 local reliability lower bound 决定；controller 记录 act/defer 与预算消耗，低于下界即升级或拒答。校准失效时回退全 defer/人工，不用事后挑阈值美化覆盖率。
  - Boundary: 保证依赖 local bias envelope、representation-gap bound 与 calibration split，并非 distribution-free；六个选择题 benchmark 与训练期 difficulty-normalized budget 未证明开放式任务或分布漂移。诊断失败时全 defer/人工。

## `AGENT-PLATFORM` → `books/part-07-agent/84-agent-platform.md`

- `SF-2026-ARXIV-2606-29472` — Agent-Computer Observation Interfaces Enable Dynamic Computer Use
  - Delta: Computer-use 平台需要把 gated keyframe、audio transcript、persistent narration 与动作回执定义为版本化 observation interface，而不是让模型任意读取连续桌面流。接口 owner 管理 capture/retention 与 action-state identity；视觉 token 稀释或漏帧时回退高保真 capture/人工确认。
  - Boundary: 只覆盖 DynaCU-Bench 浏览器任务与已测 CU models；Gemini 3 Flash 上 keyframe image-token dilution 已构成反例，因此 AOI 不是固定 bundle，也未证明桌面 OS、权限副作用或持续会议场景安全。退回高保真 capture 与人工确认。

## `AGENT-RAG` → `books/part-07-agent/76-rag.md`

- `SF-2026-ARXIV-2606-29151` — CADENZA: Compiling Natural-Language Intent into Task-Specific Operator DAGs for Semantic Query Processing
  - Delta: 旧 RAG 路径把自然语言直接送入固定 retriever；CADENZA 先编译 task-specific operator DAG，再由 logical rewrite 与 physical planner 按 quality/latency/cost 选择 backend。RAG owner 持有 DAG、operator identity 与 plan commit；统计或 backend profile 漂移时回退固定检索计划。
  - Boundary: 只证明 SemBench 上 intent-specific operator DAG 与异构 backend 的 quality/latency/cost 计划选择；未证明跨 operator 的联合最优、teacher-noise 之外的 label shift，或 Azure/API 与本地模型间可移植性。失配时固定到已校准 retrieval plan。

- `SF-2026-ARXIV-2606-29571` — Anisotropy Decides Cosine vs. Rank Metrics for Text Embeddings
  - Delta: Embedding distance 不应固定为 cosine；retrieval owner 先测 anisotropy，再在同一 corpus/query revision 上选择 cosine、rank 或 L1 类 metric，并把 metric 写入 index identity。诊断漂移或收益不稳时回退已校准 cosine/混合检索。
  - Boundary: 只比较 19 个 parameter-free metric、19 encoder 与七个静态数据集；0.01 crowded split、dominant-direction removal 和相关性未证明在线 corpus 漂移下的因果门槛，也未覆盖 learned metric。收益消失时恢复已校准 cosine/混合检索。

## `INFER-REQUEST-LIFECYCLE` → `books/part-05-inference-system/42-what-happens-during-inference.md`

- `SF-2026-ARXIV-2606-29565` — Speculative Pre-Positioning: Decoding Stateful Sessions to the Next Decision Point Off the Critical Path
  - Delta: 有状态会话的 idle time 可用于推演到下个 decision point；request lifecycle owner 保存 speculative state、acceptance confidence 与 base-state identity，命中后才原子提交。False accept、用户输入或 state drift 立即作废预推进并回退正常 decode。
  - Boundary: 只在 LayerScale 专有 engine、单 H100、70B-class 4-bit target 上测得 capability-gated fast path；8B BF16 不触发 gate，且大量收益为测量常数上的闭式推导。任何 state mutation 或置信漂移都必须 invalidate 并恢复普通 decode。

## `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md`

- `SF-2026-ARXIV-2606-29196` — Representational Depth of Evaluation Awareness Shifts With Scale in Open-Weight Language Models
  - Delta: 能力评测不能假设模型对 evaluation context 无感；evaluation-awareness probe 必须作为 contamination sensor，按模型尺度和表示深度版本化，并在异常时阻止 pooled score 直接取得 release authority。Probe 迁移失败时回退 blind/held-out protocol 与外部 outcome。
  - Boundary: SAD 上的线性可恢复性只是一种 operational evaluation-awareness signal；white-box AUROC 与黑盒行为会分离，且 Qwen/Gemma 的深度迁移不构成跨 family scaling law。异常只触发额外 held-out evaluation，不授予直接拒绝权。

- `SF-2026-ARXIV-2606-29623` — SCARCE: Scalable Cascade Analysis for Rare-event Characterisation via Embeddings
  - Delta: 高风险 release 不能用普通 Monte Carlo 的零观察失败推断安全；SCARCE 类 cascade 将 rare-event region、latent ruler、停止条件与概率上界保存为验收证据。Ruler/分布假设失效时恢复更保守采样或保持 Gate Open。
  - Boundary: MNIST 与 Llama-Guard hidden-state jailbreak fleet 只验证经校准 ruler 的 rare-event estimate；论文明确指出 behavioral fleet 约 2,000 variants 仍不足、Mahalanobis ruler 可结构性失效，跨 corpus 必须重新校准。否则 Gate 保持 Open。

## `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md`

- `SF-2026-ARXIV-2606-29581` — The Joint Effect of Quantization and Sampling Temperature on LLM Safety Alignment: A Factorial Analysis
  - Delta: 量化验收与 sampling temperature 不能分开：security release matrix 必须联合保存 model/quantization/sampler/multi-sample identity，并在多个 safety benchmark 上检查交互失稳。任一切片回归时回退已验收 precision/decoding 配置，而不是只恢复 greedy 单次测试。
  - Boundary: 当前 official exact-v1 的 Abstract 与 §3 一致披露 9 models、161 configurations、AdvBench+XSTest 与约 322k responses；证据只覆盖以 Pile validation calibration 的 AWQ INT4/GPTQ INT8、2B–8B 模型与静态 AdvBench，未证明 NF4/GGUF/对抗式 calibration、>70B、adaptive jailbreak/prompt injection 或 judge 完美可靠。任一切片回归即恢复已验收 precision/sampler。

## `TRAIN-DATA` → `books/part-04-training-system/27-data.md`

- `SF-2026-ARXIV-2606-29171` — Symbolic Mechanistic Data Attribution: Tracing Training Influence to Learned Behavioral Policies
  - Delta: 普通 sample lineage 只能回答数据来自哪里；symbolic mechanistic attribution 进一步把样本影响连接到可解释 behavioral policy，使数据 owner 能把选择、删除或复核请求落到行为证据链。归因仍是模型化证据，符号解释不稳定时保留原数据并回退重训/对照实验。
  - Boundary: 只在 Llama-3.2-3B-Instruct refusal proxy、特定 SAE 与 200 个 SFT pair 上验证一阶符号归因；feature label、Ridge fidelity 与 first-order approximation 不等于真实删除/重训因果。保留原样本与重训对照。

## `TRAIN-PRETRAINING` → `books/part-04-training-system/28-pretraining.md`

- `SF-2026-ARXIV-2606-29158` — On the Nonlinearity of Learning Rate Scaling for LLM Training
  - Delta: 固定比例或单变量外推学习率会把 width、depth、token budget 与 schedule 的非线性交互折叠掉；训练控制面应把这些轴和 optimizer/schedule revision 一起冻结后再外推。额外 sweep 提高成本，超出已测尺度时回退邻近规模校准而非沿幂律盲推。
  - Boundary: 只覆盖 GPT-2-style 22M-707M、FineWeb 5B-100B tokens、WSD 与 AdamW/AdamH；论文明确显示 log-linear LR 仅局部成立，不能外推到其他架构、optimizer 或更大规模。超界时重新 sweep 邻近尺度。

