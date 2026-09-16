# Daily Research — 2026-05-13

**规范：** V3
**窗口：** 2026-05-12T09:00:00+08:00 ～ 2026-05-13T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-15T19:20:00+08:00

Round 7 的 6 项 root 写回已由 fresh non-author reviewer 逐项通过，83 项既有写回均不得重复追加。随后独立复核在冻结 closure 中确认 6 个 false negative；Round 8 只重开这些 family，未扩日期、来源或 838 个 identity。六项 exact-v1 均可访问且未见官方 withdrawal banner，已完成相应深度 Evidence Review、V3 score、Stable Node owner 与逐命题 Books comparison：`2605.11059` 的 No Change 对读通过，5 项 root 写回及其定点修复均已通过 fresh non-author review。当前没有未处理的可执行工作，Daily 完成。

## 1. 结论

原始身份和窗口范围不变：838 个 identity 中 647 个 official-owner-day、191 个 revision/non-owner-route isolation。Round 8 冻结分母为 163 retained / 484 pre-denominator closure / 0 withdrawn；163 项均有 V3 score、Evidence Review、Stable Node owner 与 Books comparison。83 项既有 Integrate 已由 root 写入并通过 Round 7 独立写后复核；新增 5 项 Integrate 均已写入并通过 fresh non-author 写后复核。`2605.10981` 的方法与 evidence-boundary 两次定点修复均已核验，Books Gate 关闭。

## 2. 来源覆盖

本轮只执行 Daily 来源。动态历史入口无法稳定回到本窗时，只隔离该入口，不用空响应证明全站无遗漏；也不因此扩张 arXiv 候选。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 历史入口；本轮无法取得稳定的日级分页停止点 | 受阻 | 只隔离该入口，不支持全站无遗漏；恢复官方历史归档时定点重开 |
| SRC-ANTHROPIC | Research 日期列表；相邻公开事件 05-08 与 05-14，未见落窗条目 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind 与 Google Research 官方 publication 入口；相邻可见事件 04-25 与 05-28，未见落窗条目 | 已检查 | 无 |
| SRC-META-AI | Meta/FAIR publication 历史页；可见后续 05-19 条目，未见落窗条目；范围限公开目录 | 已检查 | 无 |
| SRC-QWEN | Qwen 官方历史入口 | 受阻 | 旧入口不能稳定回溯到本窗；不据空响应判零 |
| SRC-DEEPSEEK | News/Research 历史索引；相邻事件 04-24 与 05-14，未见落窗条目 | 已检查 | 无 |
| SRC-MOONSHOT | Kimi Blog 与 MoonshotAI 官方仓库历史入口 | 受阻 | 缺稳定日级发现页；不据仓库 pushed_at 判首发 |
| SRC-TENCENT-HUNYUAN | Research ‘全部’列表；相邻条目 04-30 与 05-21，未见落窗条目；范围限公开目录 | 已检查 | 无 |
| SRC-ZAI | 智谱 Research 日期列表；相邻条目 04-29 与 05-20，未见落窗条目 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Seed Research/Publication 目录与 arXiv identity 交叉；目录回填日期不替代 first-public | 已检查 | 无 |
| SRC-BAIDU-ERNIE | ERNIE Blog；相邻官方事件 05-09 08:00+08，早于本窗 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | MiMo Papers 与 Blog 历史入口 | 受阻 | Papers 可排除本窗；Blog 缺可复查历史时刻 |
| SRC-MINIMAX | Research/Blog 历史列表；相邻事件 03-18 与 05-26，未见落窗条目 | 已检查 | 无 |
| SRC-ARXIV | official OAI direct owner route 647 项，title + 完整 abstract 语义筛选；191 项恢复路由单独隔离 | 已检查 | 163 retained、484 closure、0 withdrawn、191 isolated；exact-v1 证据均可访问 |

### 分母边界

保留条件不是‘能映射 ROADMAP’，而是材料明确改变模型/训练/推理/平台/Agent 的长期机制、状态或控制权、evaluation/release contract，或修正 Books 已有设计判断。局部任务、单领域方法、只有 benchmark 数字或只表示模型局部改进者均保留 family-specific closure 在 active ledger，不进入正文候选表。

## 3. 候选与判断

评分为 Design Delta + System Reach + Durability（0～3）。7～9 为 Deep Review，5～6 为标准 Review；分数不替代 exact-v1 证据边界。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [QuIDE: Mastering the Quantized Intelligence Trade-off via Active Optimization](https://arxiv.org/html/2605.10959v1) | 2026-05-13T08:00:00+08:00 | quantization decisions need workload-specific accuracy, compression and realized latency measurements, but collapsing them into one scalar intelligence index hides Pareto preferences and cannot be a universal execution objective；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：正文已承载，`INFER-TENSORRT-LLM` → [量化为什么不自动带来加速](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Context-Gated Associative Retrieval: From Theory to Transformers](https://arxiv.org/html/2605.10970v1) | 2026-05-13T08:00:00+08:00 | 把 context-dependent gating 纳入 associative retrieval 的写入与读取规则，改变 attention/memory 的条件更新机制。；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：正文已承载，`MODEL-SELF-ATTENTION` → [从固定写入规则到目标导出的递归更新](../../../../books/part-02-model/14-self-attention.md) |
| [Steering Without Breaking: Mechanistically Informed Interventions for Discrete Diffusion Language Models](https://arxiv.org/html/2605.10971v1) | 2026-05-13T08:00:00+08:00 | attribute-specific commit schedule 让离散 diffusion 的 steering 时点成为逐属性控制状态，而不是统一 timestep。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`MULTIMODAL-GENERATIVE-PARADIGMS` → [Commitment Policy 可以从未来稳定轨迹学习](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Rotation-Preserving Supervised Fine-Tuning](https://arxiv.org/html/2605.10973v1) | 2026-05-13T08:00:00+08:00 | rotation-preserving SFT 以敏感 pretrained directions 为约束，重写 adaptation 与 forgetting 的可观测权衡。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`TRAIN-SFT` → [Trainable Subspace 也是 Continual SFT 的评估变量](../../../../books/part-04-training-system/29-sft.md) |
| [Vertex-Softmax: Tight Transformer Verification via Exact Softmax Optimization](https://arxiv.org/html/2605.10974v1) | 2026-05-13T08:00:00+08:00 | interval-only exact softmax bound 达到该抽象下的最紧 sound bound，继续收紧须引入 correlation/coupling；2 + 2 + 3 = 7 | 深入完成 | 整合：已写入并通过独立写后复核，`PLATFORM-EVALUATION-SYSTEM` → [Verification Bound 必须写清输入抽象的信息上限](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [LEAP: Unlocking dLLM Parallelism via Lookahead Early-Convergence Token Detection](https://arxiv.org/html/2605.10980v1) | 2026-05-13T08:00:00+08:00 | diffusion LM parallel decode 应检测 early-converged token，而不是把 high confidence 当作唯一安全 commit 条件；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`MULTIMODAL-GENERATIVE-PARADIGMS` → [Early convergence 与 high confidence 不是同一个 Commit 证据](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [AESOP: Adversarial Execution-path Selection to Overload Deep Learning Pipelines](https://arxiv.org/html/2605.10987v1) | 2026-05-13T08:00:00+08:00 | 动态 ML pipeline 的 availability attack surface 由 execution-path fan-out 与 downstream workload volume 共同决定，单模型 perturbation 预算不足以描述风险；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`PLATFORM-SECURITY` → [Availability 攻击从单模型开销扩展到动态路径](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Skill Drift Is Contract Violation: Proactive Maintenance for LLM Agent Skill Libraries](https://arxiv.org/html/2605.10990v1) | 2026-05-13T08:00:00+08:00 | skill drift 应以 role-bearing environment contract violation 检测，而不是对版本字符串或任意值变化报警；2 + 2 + 3 = 7 | 深入完成 | 整合：已写入待终审，`AGENT-PLATFORM` → [Skill Drift 应检测角色契约，而不是任意变化](../../../../books/part-07-agent/84-agent-platform.md) |
| [Test-Time Personalization: A Diagnostic Framework and Probabilistic Fix for Scaling Failures](https://arxiv.org/html/2605.10991v1) | 2026-05-13T08:00:00+08:00 | Best-of-N personalization 的收益取决于 reward-model 的 user/query-level calibration，候选数本身不是可兑现的 scaling law。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：正文已承载，`INFER-SCHEDULING` → [当前 Confidence 不等于继续计算的 Residual Value](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [ECHO: Continuous Hierarchical Memory for Vision-Language-Action Models](https://arxiv.org/html/2605.10993v1) | 2026-05-13T08:00:00+08:00 | VLA 长任务记忆需要层次化 semantic tree、top-down retrieval 与 background consolidation，而不只是线性历史 buffer；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：正文已承载，`MULTIMODAL-EMBODIED-VLA` → [Policy 内部的 Latent Memory 是 Episode State，不是 Agent Memory](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Few-Shot Truly Benign DPO Attack for Jailbreaking LLMs](https://arxiv.org/html/2605.10998v1) | 2026-05-13T08:00:00+08:00 | benign-looking DPO data 能在分布外压低 refusal，因此 preference-data admission 必须把 safety redistribution 当成发布风险。；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`PLATFORM-SECURITY` → [Capability Access Control 可以前移到训练状态](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SkillGen: Verified Inference-Time Agent Skill Synthesis](https://arxiv.org/html/2605.10999v1) | 2026-05-13T08:00:00+08:00 | inference-time skill synthesis 必须比较同一实例有/无 skill 的 repairs 与 regressions，生成 artifact 只是 proposal 而非 admission；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：正文已承载，`AGENT-PLATFORM` → [从 Trajectory 到 Skill 是一次受治理的 Compilation](../../../../books/part-07-agent/84-agent-platform.md) |
| [MT-JailBench: A Modular Benchmark for Understanding Multi-Turn Jailbreak Attacks](https://arxiv.org/html/2605.11002v1) | 2026-05-13T08:00:00+08:00 | 多轮 jailbreak benchmark 必须冻结 turn/retry/interaction/strategy/judge budget，并把 strategy、prompt generation、refinement 与 flow control 拆成可重组模块；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`PLATFORM-EVALUATION-SYSTEM` → [Evidence Chain 与在线干预](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [The Authorization-Execution Gap Is a Major Safety and Security Problem in Open-World Agents](https://arxiv.org/html/2605.11003v1) | 2026-05-13T08:00:00+08:00 | This position paper argues that the Authorization-Execution Gap (AEG) is a major safety and security problem in open-world agents.；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：正文已承载，`AGENT-TOOL-CALLING` → [模型输出只是 Proposal](../../../../books/part-07-agent/78-tool-calling.md) |
| [DisagMoE: Computation-Communication overlapped MoE Training via Disaggregated AF-Pipe Parallelism](https://arxiv.org/html/2605.11005v1) | 2026-05-13T08:00:00+08:00 | We present DisagMoE, a disaggregated MoE training system that jointly optimizes model placement and scheduling for maximal efficiency.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`TRAIN-PIPELINE-PARALLEL` → [异步 Pipeline：去掉 Bubble 会把成本移到参数版本](../../../../books/part-04-training-system/38-pipeline-parallel.md) |
| [LoopUS: Recasting Pretrained LLMs into Looped Latent Refinement Models](https://arxiv.org/html/2605.11011v1) | 2026-05-13T08:00:00+08:00 | latent recurrent refinement 可在不增加参数深度时增加执行深度，但收敛与停止策略成为新的运行状态。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`MODEL-TRANSFORMER-LAYER` → [Parameter Depth 与 Execution Depth 可以分离](../../../../books/part-02-model/17-transformer-layer.md) |
| [AgentShield: Deception-based Compromise Detection for Tool-using LLM Agents](https://arxiv.org/html/2605.11026v1) | 2026-05-13T08:00:00+08:00 | Defenses against indirect prompt injection (IPI) in tool-using LLM agents share two structural weaknesses.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`PLATFORM-SECURITY` → [从资产与信任边界开始](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [FragBench: Cross-Session Attacks Hidden in Benign-Looking Fragments](https://arxiv.org/html/2605.11029v1) | 2026-05-13T08:00:00+08:00 | We build FragBench, a benchmark drawn from 24 real-world cyber-incident campaigns, which keeps the full attack trail: the multi-fragment kill chain, the per-fragment safety-judge verdicts, sandboxed execution traces, and a matched set of benign cover sessions.；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：正文已承载，`PLATFORM-SECURITY` → [跨会话分解会绕过 Prompt-local Guard](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Portable Agent Memory: A Protocol for Cryptographically-Verified Memory Transfer Across Heterogeneous AI Agents](https://arxiv.org/html/2605.11032v1) | 2026-05-13T08:00:00+08:00 | We present Portable Agent Memory, an open protocol and reference implementation for transferring persistent memory state across heterogeneous AI agents.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`AGENT-MEMORY` → [Memory Write 是高风险决策](../../../../books/part-07-agent/77-memory.md) |
| [Sequential Behavioral Watermarking for LLM Agents](https://arxiv.org/html/2605.11036v1) | 2026-05-13T08:00:00+08:00 | sequential behavioral watermark 把 Agent 多步行为与挑战序列绑定，身份判断从单次文本迁移到有状态轨迹。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`PLATFORM-SECURITY` → [Behavioral Contract 把 Invariant、Drift 与 Recovery 变成运行期状态](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [The Granularity Mismatch in Agent Security: Argument-Level Provenance Solves Enforcement and Isolates the LLM Reasoning Bottleneck](https://arxiv.org/html/2605.11039v1) | 2026-05-13T08:00:00+08:00 | We present \textsc{PACT} (\emph{Provenance-Aware Capability Contracts}), a runtime monitor that assigns semantic roles to tool arguments, tracks value provenance across replanning steps, and checks whether each argument's origin satisfies its role-specific trust contract.；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：正文已承载，`PLATFORM-SECURITY` → [Canonical Action 与 Effect-time Authorization](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [On Problems of Implicit Context Compression for Software Engineering Agents](https://arxiv.org/html/2605.11051v1) | 2026-05-13T08:00:00+08:00 | implicit context compression 在 single-shot 可成立却在 multi-step Agent 失败，给出压缩适用性的负面边界。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`AGENT-CONTEXT` → [Context Compression 必须保留执行状态，而不只是语义](../../../../books/part-07-agent/75-context.md) |
| [HiDream-O1-Image: A Natively Unified Image Generative Foundation Model with Pixel-level Unified Transformer](https://arxiv.org/html/2605.11061v1) | 2026-05-13T08:00:00+08:00 | 统一 pixel-space 生成把理解与生成的表示、训练数据和 decoder 责任放入同一 native multimodal contract。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`MULTIMODAL-REPRESENTATION` → [阶段四：native multimodal representation](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Enabling Performant and Flexible Model-Internal Observability for LLM Inference](https://arxiv.org/html/2605.11093v1) | 2026-05-13T08:00:00+08:00 | We present DMI-Lib, a high-speed deep model inspector that treats internal observability as a first-class systems primitive, decoupling it from the inference hot path via an asynchronous observability substrate built from Ring^2, a GPU-CPU memory abstraction for capturing and staging tensors, and a policy-controlled…；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`PLATFORM-MONITORING` → [Model-internal Sensor 必须从 Inference Hot Path 解耦](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [SEVO: Semantic-Enhanced Virtual Observation for Robust VLA Manipulation via Active Illumination and Data-Centric Collection](https://arxiv.org/html/2605.11114v1) | 2026-05-13T08:00:00+08:00 | VLA 的 observation design 与 data diversity 共同决定 action policy 可见状态，更多数据不能替代观测接口。；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：正文已承载，`MULTIMODAL-EMBODIED-VLA` → [State ownership 与 freshness](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Sampling More, Getting Less: Calibration is the Diversity Bottleneck in LLMs](https://arxiv.org/html/2605.11128v1) | 2026-05-13T08:00:00+08:00 | order 与 shape miscalibration 会把局部 token 选择误差复合为 sequence-level diversity collapse，需联合验收局部与整体分布。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`MODEL-SAMPLING` → [Sampling 为什么会影响长程行为](../../../../books/part-02-model/20-sampling.md) |
| [CATS: Cascaded Adaptive Tree Speculation for Memory-Limited LLM Inference Acceleration](https://arxiv.org/html/2605.11186v1) | 2026-05-13T08:00:00+08:00 | memory-constrained speculative inference 必须联合选择 draft/verify 长度与状态驻留，不能只最大化 acceptance。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`INFER-SPECULATIVE-DECODING` → [Verify Length 不是孤立的固定超参数](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [How Does Differential Privacy Affect Social Bias in LLMs? A Systematic Evaluation](https://arxiv.org/html/2605.11195v1) | 2026-05-13T08:00:00+08:00 | DP 对 logit-level 与 output-level social bias 的影响不一致，说明 privacy claim 与 fairness claim 必须按行为层级分开验收。；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入待终审，`PLATFORM-EVALUATION-SYSTEM` → [评估对象有四个层次](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Variational Linear Attention: Stable Associative Memory for Long-Context Transformers](https://arxiv.org/html/2605.11196v1) | 2026-05-13T08:00:00+08:00 | variational linear attention 把 associative memory 更新变成受正则化的在线状态，稳定性来自写入规则而非线性复杂度口号。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`MODEL-LONG-CONTEXT` → [路线六：让模型在 Test Time 更新内部记忆](../../../../books/part-02-model/22-long-context.md) |
| [Continuous Discovery of Vulnerabilities in LLM Serving Systems with Fuzzing](https://arxiv.org/html/2605.11202v1) | 2026-05-13T08:00:00+08:00 | We present GRIEF, a greybox fuzzer for LLM inference engines that treats timed multi-request traces as first-class inputs, uses lightweight oracles to detect crashes, hangs, performance pathologies, and silent output corruption, and applies controlled replay with log-probability checks to confirm reproducible serving-layer failures.；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`PLATFORM-EVALUATION-SYSTEM` → [Runtime and Service Evaluation](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [The Scaling Law of Evaluation Failure: Why Simple Averaging Collapses Under Data Sparsity and Item Difficulty Gaps, and How Item Response Theory Recovers Ground Truth Across Domains](https://arxiv.org/html/2605.11205v1) | 2026-05-13T08:00:00+08:00 | Through controlled simulation experiments across four domains -- NLP (GLUE), clinical drug trials, autonomous vehicle safety, and cybersecurity -- we show that Spearman rank correlation $ρ$ between simple-average rankings and ground-truth rankings degrades from $ρ= 1.000$ at 100% coverage to $ρ= 0.809$ at 67%…；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`PLATFORM-EVALUATION-SYSTEM` → [平均值、切片与不确定性](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Measuring Five-Nines Reliability: Sample-Efficient LLM Evaluation in Saturated Benchmarks](https://arxiv.org/html/2605.11209v1) | 2026-05-13T08:00:00+08:00 | Leveraging this observation, we propose to learn a sampling distribution concentrated on failure-prone inputs via the cross-entropy method (CEM).；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`PLATFORM-EVALUATION-SYSTEM` → [Agent Regression Testing 需要分配 Evidence Budget](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Enforcing Constraints in Generative Sampling via Adaptive Correction Scheduling](https://arxiv.org/html/2605.11214v1) | 2026-05-13T08:00:00+08:00 | adaptive correction scheduling 根据当前生成状态分配修正步骤，把统一迭代数改为有边界的控制策略。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`MULTIMODAL-GENERATIVE-PARADIGMS` → [Refinement 位置也可以成为条件计算状态](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Leveraging RAG for Training-Free Alignment of LLMs](https://arxiv.org/html/2605.11217v1) | 2026-05-13T08:00:00+08:00 | RAG-Pref 将 preferred/dispreferred retrieval 在推理时变成 alignment actuator，改变 offline weight alignment 与 online refusal guardrail 的分工。；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入待终审，`TRAIN-RLHF` → [从持久权重更新到条件化 Activation Intervention](../../../../books/part-04-training-system/31-rlhf.md) |
| [Comment and Control: Hijacking Agentic Workflows via Context-Grounded Evolution](https://arxiv.org/html/2605.11229v1) | 2026-05-13T08:00:00+08:00 | In this paper, we design the first detection and exploitation framework, called JAW, to hijack agentic workflows hosted on automation platforms via a novel approach called Context-Grounded Evolution.；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：正文已承载，`PLATFORM-SECURITY` → [局部合理动作会累积成有害轨迹](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Sieve: Dynamic Expert-Aware PIM Acceleration for Evolving Mixture-of-Experts Models](https://arxiv.org/html/2605.11277v1) | 2026-05-13T08:00:00+08:00 | MoE expert 热度双峰化使静态 PIM placement 失效，Sieve 依据演化的 token-to-expert 分布动态分配执行位置。；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`INFER-TENSORRT-LLM` → [MoE Dispatch 应平衡时间，而不是固定代理量](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [LatentRouter: Can We Choose the Right Multimodal Model Before Seeing Its Answer?](https://arxiv.org/html/2605.11301v1) | 2026-05-13T08:00:00+08:00 | multimodal routing 被表述为 answer 前的 counterfactual utility prediction，使路由器拥有选择 proposal 而非质量真值。；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`INFER-SCHEDULING` → [Calibration 是在线 Routing State](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [SOMA: Efficient Multi-turn LLM Serving via Small Language Model](https://arxiv.org/html/2605.11317v1) | 2026-05-13T08:00:00+08:00 | early turns 估计 local response manifold 并适配小 surrogate，session 必须保留 switch/rollback；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入并通过独立写后复核，`INFER-REQUEST-LIFECYCLE` → [Session 局部模型与回退](../../../../books/part-05-inference-system/42-what-happens-during-inference.md) |
| [Rethinking Evaluation for LLM Hallucination Detection: A Desiderata, A New RAG-based Benchmark, New Insights](https://arxiv.org/html/2605.11330v1) | 2026-05-13T08:00:00+08:00 | hallucination detection benchmark 需要冻结 label noise、RAG context 与长上下文切片，单一 aggregate 不足以签发 detector 结论。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`PLATFORM-EVALUATION-SYSTEM` → [幻觉指标改善前，先排除 decoding 与输出分布的等价替代解释](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [VERDI: Single-Call Confidence Estimation for Verification-Based LLM Judges via Decomposed Inference](https://arxiv.org/html/2605.11334v1) | 2026-05-13T08:00:00+08:00 | VERDI 从 judge 已生成的结构化 reasoning 分解一次调用的 confidence，但该值仍是可校准 sensor，不是 verdict authority。；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`PLATFORM-EVALUATION-SYSTEM` → [Confidence 要在 Belief、Action 与 Outcome 三层校准](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ChunkFlow: Communication-Aware Chunked Prefetching for Layerwise Offloading in Distributed Diffusion Transformer Inference](https://arxiv.org/html/2605.11335v1) | 2026-05-13T08:00:00+08:00 | Building on this model, we design ChunkFlow, a communication-aware, chunk-granular offloading runtime that adaptively yields to collective communication and smoothly trades GPU memory for prefetch volume.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`INFER-GPU-MEMORY` → [扩展层级](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Options, Not Clicks: Lattice Refinement for Consent-Driven MCP Authorization](https://arxiv.org/html/2605.11360v1) | 2026-05-13T08:00:00+08:00 | In this work, we present Conleash, a client-side middleware that enforces boundary-scoped authorization by utilizing a risk lattice to auto-permit safe calls within known boundaries while escalating risks, a policy engine for user-defined invariants, and a refinement loop that converts user decisions into reusable…；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：正文已承载，`AGENT-MCP` → [MCP 不等于 Tool Authorization](../../../../books/part-07-agent/83-mcp.md) |
| [The tractability landscape of diffusion alignment: regularization, rewards, and computational primitives](https://arxiv.org/html/2605.11361v1) | 2026-05-13T08:00:00+08:00 | diffusion alignment 的可实现性取决于 KL/Wasserstein 目标与可用 sampling primitive，而不是抽象 reward 存在性。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`MULTIMODAL-GENERATIVE-PARADIGMS` → [Distributional Distance 可以成为受限训练目标](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [LLM-X: A Scalable Negotiation-Oriented Exchange for Communication Among Personal LLM Agents](https://arxiv.org/html/2605.11376v1) | 2026-05-13T08:00:00+08:00 | We propose a personal-LLM exchange (LLM-X), a scalable negotiation-oriented environment that enables direct, structured communication across populations of personal agents (LLMs), each representing an individual user.；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`AGENT-MULTI-AGENT` → [Coordination State 必须有显式 Owner 与 Commit Transition](../../../../books/part-07-agent/82-multi-agent.md) |
| [Kairos: A Scalable Serving System for Physical AI](https://arxiv.org/html/2605.11381v1) | 2026-05-13T08:00:00+08:00 | To fill this gap, we design Kairos, the first multi-robot serving system that makes the generate-execute loop a first-class citizen, with active involvement in the execution phase.；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`INFER-SCHEDULING` → [Physical AI 把 Execution Horizon 变成调度状态](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Behavioral Mode Discovery for Fine-tuning Multimodal Generative Policies](https://arxiv.org/html/2605.11387v1) | 2026-05-13T08:00:00+08:00 | RL 微调生成式 policy 时，成功率优化会压缩原有多模态行为；轨迹级 mode discovery 与互信息奖励改变了 diversity state 的训练责任。；3 + 2 + 2 = 7 | 深入完成 | 整合：已写入待终审，`TRAIN-RLHF` → [Reverse KL 会把“找到高奖励”收缩成单一路径](../../../../books/part-04-training-system/31-rlhf.md) |
| [Deep Reasoning in General Purpose Agents via Structured Meta-Cognition](https://arxiv.org/html/2605.11388v1) | 2026-05-13T08:00:00+08:00 | DOLORES 用可执行 decomposition language 和受控 reasoning threads 改变通用 Agent 的计划、执行与 goal revision 控制流。；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入待终审，`AGENT-PLANNING` → [从目标到状态图](../../../../books/part-07-agent/79-planning.md) |
| [fg-expo: Frontier-guided exploration-prioritized policy optimization via adaptive kl and gaussian curriculum](https://arxiv.org/html/2605.11403v1) | 2026-05-13T08:00:00+08:00 | adaptive KL 与基于逐题历史通过率的 Gaussian curriculum 改变 GRPO/RLVR 的探索控制变量。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：正文已承载，`TRAIN-GRPO` → [多任务 RL 的 curriculum/KL controller（正文段落）](../../../../books/part-04-training-system/33-grpo.md) |
| [Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry](https://arxiv.org/html/2605.11418v1) | 2026-05-13T08:00:00+08:00 | While this design enables scalable, on-demand capability expansion, it also introduces a semantic supply-chain risk in which natural-language metadata and instructions can affect which skills are admitted, surfaced, selected, and loaded.；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：正文已承载，`AGENT-PLATFORM` → [被审计的 Skill 必须与实际执行 Artifact 同一](../../../../books/part-07-agent/84-agent-platform.md) |
| [A Mechanistic Investigation of Supervised Fine Tuning](https://arxiv.org/html/2605.11426v1) | 2026-05-13T08:00:00+08:00 | SFT 前后整体 activation 高相似仍可掩盖 sparse latent 的 task/layer-specific 漂移，因此表面保持不能证明内部能力未重排。；2 + 2 + 3 = 7 | 深入完成 | 整合：已写入待终审，`TRAIN-SFT` → [Evaluation 应分开能力与行为](../../../../books/part-04-training-system/29-sft.md) |
| [Agent-BRACE: Decoupling Beliefs from Actions in Long-Horizon Tasks via Verbalized State Uncertainty](https://arxiv.org/html/2605.11436v1) | 2026-05-13T08:00:00+08:00 | Therefore, we introduce Agent-BRACE: Agent Belief state Representation via Abstraction and Confidence Estimation, a method that decouples an LLM agent into a belief state model and a policy model, jointly optimized via reinforcement learning.；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：正文已承载，`AGENT-MEMORY` → [Belief State：先保存竞争假设，再决定事实](../../../../books/part-07-agent/77-memory.md) |
| [Can a Single Message Paralyze the AI Infrastructure? The Rise of AbO-DDoS Attacks through Targeted Mobius Injection](https://arxiv.org/html/2605.11442v1) | 2026-05-13T08:00:00+08:00 | To mitigate Mobius Injection, we propose a proactive defense mechanism using Agent Component Energy (ACE) Analysis, which detects malicious recursive triggers by measuring anomalous energy in the agent's component graph.；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`PLATFORM-SECURITY` → [Exactness 保持不变时，加速路径仍可能被定向击穿](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [FibQuant: Universal Vector Quantization for Random-Access KV-Cache Compression](https://arxiv.org/html/2605.11478v1) | 2026-05-13T08:00:00+08:00 | We introduce \textsc{FibQuant}, a universal fixed-rate vector quantizer that keeps the same normalize--rotate--store interface while replacing scalar tables by a shared radial--angular codebook matched to this canonical source.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`INFER-KV-CACHE` → [Quantization Objective 应对齐 Attention Distortion](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Digital Identity for Agentic Systems: Toward a Portable Authorization Standard for Autonomous Agents](https://arxiv.org/html/2605.11487v1) | 2026-05-13T08:00:00+08:00 | Enterprise AI is shifting from copilots to autonomous agents capable of executing workflows, negotiating outcomes, and making decisions with limited human oversight.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`PLATFORM-SECURITY` → [从资产与信任边界开始](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Understanding and Preventing Entropy Collapse in RLVR with On-Policy Entropy Flow Optimization](https://arxiv.org/html/2605.11491v1) | 2026-05-13T08:00:00+08:00 | RLVR entropy collapse 可分解为 token-level entropy-increasing/decreasing update flow 不平衡，控制器需要在严格 on-policy 边界内调节。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`TRAIN-GRPO` → [Verifiable Reward 不等于每个样本都可学习](../../../../books/part-04-training-system/33-grpo.md) |
| [STRIDE: Training-Free Diversity Guidance via PCA-Directed Feature Perturbation in Single-Step Diffusion Models](https://arxiv.org/html/2605.11494v1) | 2026-05-13T08:00:00+08:00 | 单步/少步 diffusion 失去多步 trajectory 中可注入随机性的接口；PCA 定向 feature perturbation 把 diversity control 移入 student 的内部表示几何。；2 + 1 + 2 = 5 | 深入完成 | 整合：已写入待终审，`MULTIMODAL-GENERATIVE-PARADIGMS` → [Few-step Distillation 要在 Student 实际访问的状态上验收](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [The Evaluation Differential: When Frontier AI Models Recognise They Are Being Tested](https://arxiv.org/html/2605.11496v1) | 2026-05-13T08:00:00+08:00 | We introduce the Evaluation Differential (ED), a conditional divergence in a target behavioural property between recognised-evaluation and deployment-continuous contexts, define a normalised effect-size form (nED) for cross-property comparison, and prove that marginal evaluation scores cannot identify ED.；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`PLATFORM-EVALUATION-SYSTEM` → [从目标到证据，而不是从指标到目标](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [FlowSteer: Prompt-Only Workflow Steering Exposes Planning-Time Vulnerabilities in Multi-Agent LLM Systems](https://arxiv.org/html/2605.11514v1) | 2026-05-13T08:00:00+08:00 | We study this risk through social influence probing workflows to identify high-impact subtasks and malicious-signal propagation.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`PLATFORM-SECURITY` → [从资产与信任边界开始](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [NAVIS: Concurrent Search and Update with Low Position-Seeking Overhead in On-SSD Graph-Based Vector Search](https://arxiv.org/html/2605.11523v1) | 2026-05-13T08:00:00+08:00 | We present NAVIS, an on-SSD GVS system that drives down position-seeking overhead through (i) a layout-supported selective vector read that breaks the packed-page coupling without losing its locality benefits, (ii) a dynamic lightweight entrance graph update mechanism that reuses traversal information already produced by concurrent updates, and (iii) an entrance graph-aware edgelist cache that…；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`AGENT-RAG` → [Concurrent Update 让 SSD Index 同时拥有 Search 与 Maintenance State](../../../../books/part-07-agent/76-rag.md) |
| [PRISM: : Planning and Reasoning with Intent in Simulated Embodied Environments](https://arxiv.org/html/2605.11534v1) | 2026-05-13T08:00:00+08:00 | PRISM 把 embodied-agent 单一 success rate 拆成 perception、intent reasoning 与 long-horizon coordination 的可替换诊断 probe。；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入待终审，`PLATFORM-EVALUATION-SYSTEM` → [Agent and Outcome Evaluation](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Fast MoE Inference via Predictive Prefetching and Expert Replication](https://arxiv.org/html/2605.11537v1) | 2026-05-13T08:00:00+08:00 | To address these challenges, we propose a dynamic expert replication strategy that predicts which experts are likely to be overloaded and replicates them for upcoming batches of tokens.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`INFER-TENSORRT-LLM` → [Expert Placement 必须跟随热度演化](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Taming Extreme Tokens: Covariance-Aware GRPO with Gaussian-Kernel Advantage Reweighting](https://arxiv.org/html/2605.11538v1) | 2026-05-13T08:00:00+08:00 | covariance-aware token reweighting 改变 GRPO 中 extreme token 的更新权重与训练稳定性。；2 + 1 + 2 = 5 | 深入完成 | 整合：已写入待终审，`TRAIN-GRPO` → [Group-relative Gradient 不是独立样本均值](../../../../books/part-04-training-system/33-grpo.md) |
| [Sharpen Your Flow: Sharpness-Aware Sampling for Flow Matching](https://arxiv.org/html/2605.11547v1) | 2026-05-13T08:00:00+08:00 | sharpness-aware sampler 把 flow generation 的 timestep 预算改为由离线局部敏感度校准的非均匀调度。；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：正文已承载，`MULTIMODAL-GENERATIVE-PARADIGMS` → [Diffusion trajectory 的 sensitivity calibration profile（正文段落）](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [The DAWN of World-Action Interactive Models](https://arxiv.org/html/2605.11550v1) | 2026-05-13T08:00:00+08:00 | Experiments show that DAWN achieves strong planning performance and favorable safety-related results across multiple autonomous driving benchmarks.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`MULTIMODAL-WORLD-MODELS` → [Action-conditioned transition](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Hindsight Hint Distillation: Scaffolded Reasoning for SWE Agents from CoT-free Answers](https://arxiv.org/html/2605.11556v1) | 2026-05-13T08:00:00+08:00 | Hindsight Hint Distillation 从当前 Agent 失败 rollout 生成针对性 hint，再蒸馏成功轨迹，改变 agentic SFT 的数据生成闭环。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`TRAIN-SFT` → [Rollout-conditioned Distillation 应按证据归因，而不是整段照抄](../../../../books/part-04-training-system/29-sft.md) |
| [When Looking Is Not Enough: Visual Attention Structure Reveals Hallucination in MLLMs](https://arxiv.org/html/2605.11559v1) | 2026-05-13T08:00:00+08:00 | attention-spectrum sensor 将多模态幻觉检测与 decoding correction 绑定到可观测的视觉注意力结构。；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入待终审，`MULTIMODAL-REPRESENTATION` → [任务贡献与当前可靠性不能共用一个 Gate](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [RIO: Flexible Real-Time Robot I/O for Cross-Embodiment Robot Learning](https://arxiv.org/html/2605.11564v1) | 2026-05-13T08:00:00+08:00 | Despite recent efforts to collect multi-task, multi-embodiment datasets, to design recipes for training Vision-Language-Action models (VLAs), and to showcase these models on different robot platforms, generalist cross-embodiment robot capabilities remains a largely elusive ideal.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`MULTIMODAL-EMBODIED-VLA` → [State ownership 与 freshness](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [OUI as a Structural Observable: Towards an Activation-Centric View of Neural Network Training](https://arxiv.org/html/2605.11570v1) | 2026-05-13T08:00:00+08:00 | loss/accuracy 只能从训练外部看到结果，无法及早定位层内结构是否进入坏区间；OUI 把 activation pattern 作为 label-free early observable。；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入待终审，`TRAIN-PRETRAINING` → [训练稳定性是多层系统问题](../../../../books/part-04-training-system/28-pretraining.md) |
| [BitLM: Unlocking Multi-Token Language Generation with Bitwise Continuous Diffusion](https://arxiv.org/html/2605.11577v1) | 2026-05-13T08:00:00+08:00 | We propose BitLM, a language model that represents each token as a fixed-length binary code and employs a lightweight diffusion head to denoise multiple tokens in parallel within each block.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`MULTIMODAL-GENERATIVE-PARADIGMS` → [Editable tokens 与 commit boundary](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Ada-MK: Adaptive MegaKernel Optimization via Automated DAG-based Search for LLM Inference](https://arxiv.org/html/2605.11581v1) | 2026-05-13T08:00:00+08:00 | However, existing MegaKernel implementations face a fundamental tension between portability and efficiency on resource-constrained GPUs such as NVIDIA Ada: hand-tuned solutions are tightly coupled to specific architectures and lack portability, while auto-compiled approaches introduce runtime dynamic scheduling whose branch penalties are unacceptable…；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`INFER-TENSORRT-LLM` → [从逐 Kernel Launch 到 Persistent Executor](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [SoK: Unlearnability and Unlearning for Model Dememorization](https://arxiv.org/html/2605.11592v1) | 2026-05-13T08:00:00+08:00 | unlearnability 与 unlearning 共享 shallow dememorization 风险且会相互干扰，单阶段遗忘分数不能证明 knowledge withholding。；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`PLATFORM-SECURITY` → [Unlearning 必须分开参数擦除与推理拒答](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [GAR: Carbon-Aware Routing for LLM Inference via Constrained Optimization](https://arxiv.org/html/2605.11603v1) | 2026-05-13T08:00:00+08:00 | To address this gap, we introduce Green-Aware Routing (GAR), a constrained multi-objective optimization framework that minimizes per-request CO2 emissions subject to explicit accuracy floors and p95-latency service-level objectives (SLOs).；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`INFER-SCHEDULING` → [目标函数不止吞吐](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Keep What Audio Cannot Say: Context-Preserving Token Pruning for Omni-LLMs](https://arxiv.org/html/2605.11605v1) | 2026-05-13T08:00:00+08:00 | audio-explainability-aware pruning 将 Omni-LLM 的 visual token 保留规则从单模态重要性改为跨模态冗余条件。；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入待终审，`MULTIMODAL-REPRESENTATION` → [固定预算要先分配信息责任，再选择具体 Token](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [PRISM: A Geometric Risk Bound that Decomposes Drift into Scale, Shape, and Head](https://arxiv.org/html/2605.11608v1) | 2026-05-13T08:00:00+08:00 | PRISM 将 post-training model drift 分解为 scale、shape 与 output-head 三轴，并把诊断轴映射到不同修复选择。；2 + 2 + 3 = 7 | 深入完成 | 整合：已写入待终审，`PLATFORM-EVALUATION-SYSTEM` → [第一个不变量：评估声明必须绑定完整对象](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Nice Fold or Hero Call: Learning Budget-Efficient Thinking for Adaptive Reasoning](https://arxiv.org/html/2605.11625v1) | 2026-05-13T08:00:00+08:00 | reasoning budget 应按 solvability 的预期回报而非 perceived difficulty 分配，并显式允许 solve/fold/hero-call。；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`INFER-SCHEDULING` → [Reasoning Budget 必须进入调度与评估身份](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Safety Context Injection: Inference-Time Safety Alignment via Static Filtering and Agentic Analysis](https://arxiv.org/html/2605.11664v1) | 2026-05-13T08:00:00+08:00 | inference safety 将 assessment 与 generation 分离，并在 static filter 与 agentic analyzer 之间交换 latency、context coverage 与攻击面。；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`PLATFORM-SECURITY` → [Pre-guard 可以前移，但最终 Authority 不能前移给 Draft Model](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Evolutionary Task Discovery: Advancing Reasoning Frontiers via Skill Composition and Complexity Scaling](https://arxiv.org/html/2605.11666v1) | 2026-05-13T08:00:00+08:00 | 无结构 mutation 会导致合成 reasoning task 同质化；EvoTD 以 skill × complexity 双轴、crossover/mutation 和 policy-relative ZPD 组织 curriculum。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：正文已承载，`TRAIN-DATA` → [从样本数量到 Coverage Contract：Curriculum 必须同时管理内容、能力与环境](../../../../books/part-04-training-system/27-data.md) |
| [OOM-Free Alpamayo via CPU-GPU Memory Swapping for Vision-Language-Action Models](https://arxiv.org/html/2605.11678v1) | 2026-05-13T08:00:00+08:00 | We present a framework, which enables memory-efficient VLA inference on VRAM-constrained GPUs through system-level optimization alone, without model modification.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`INFER-GPU-MEMORY` → [扩展层级](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Robust LLM Unlearning Against Relearning Attacks: The Minor Components in Representations Matter](https://arxiv.org/html/2605.11685v1) | 2026-05-13T08:00:00+08:00 | unlearning 只修改 dominant representation components 容易被 relearning 逆转，minor components 也必须进入删除与攻击验收。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`PLATFORM-SECURITY` → [Unlearning 必须分开参数擦除与推理拒答](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [GRAFT: Graph-Tokenized LLMs for Tool Planning](https://arxiv.org/html/2605.11706v1) | 2026-05-13T08:00:00+08:00 | 把 tool graph 作为检索/序列化 prompt 只能做语义 matching，早期选错后会进入非法 graph state；GRAFT 将节点与有向依赖编码进模型表示。；3 + 2 + 2 = 7 | 深入完成 | 整合：已写入待终审，`AGENT-PLANNING` → [从目标到状态图](../../../../books/part-07-agent/79-planning.md) |
| [Toward Stable Value Alignment: Introducing Independent Modules for Consistent Value Guidance](https://arxiv.org/html/2605.11712v1) | 2026-05-13T08:00:00+08:00 | 独立 value module 与 bridge token 将 alignment steering 从修改 backbone 权重改为可刷新的外部 value state。；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入待终审，`TRAIN-RLHF` → [从持久权重更新到条件化 Activation Intervention](../../../../books/part-04-training-system/31-rlhf.md) |
| [SafeSteer: A Decoding-level Defense Mechanism for Multimodal Large Language Models](https://arxiv.org/html/2605.11716v1) | 2026-05-13T08:00:00+08:00 | decoding-level probe 将 MLLM safety 从生成后过滤前移到候选 token hidden-state 的在线筛选。；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入待终审，`PLATFORM-SECURITY` → [Learned Security Sensor 与 Reference Monitor 必须分层](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [EPIC: Efficient Predicate-Guided Inference-Time Control for Compositional Text-to-Image Generation](https://arxiv.org/html/2605.11722v1) | 2026-05-13T08:00:00+08:00 | 一次生成无法可靠满足多对象、计数、属性与关系；EPIC 将 prompt 固化为 typed visual program，并以 predicate failure 路由 edit 或 resample。；3 + 2 + 2 = 7 | 深入完成 | 整合：已写入待终审，`MULTIMODAL-GENERATIVE-PARADIGMS` → [从一次生成到 Plan → Generate → Validate → Retry](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Allegory of the Cave: Measurement-Grounded Vision-Language Learning](https://arxiv.org/html/2605.11727v1) | 2026-05-13T08:00:00+08:00 | measurement-domain input 把 ISP 前原始传感证据、camera conditioning 与 exposure supervision 纳入 VLM representation identity。；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入待终审，`MULTIMODAL-REPRESENTATION` → [时间、空间与 provenance 必须进入状态](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Persona-Conditioned Adversarial Prompting: Multi-Identity Red-Teaming for Adversarial Discovery and Mitigation](https://arxiv.org/html/2605.11730v1) | 2026-05-13T08:00:00+08:00 | persona-conditioned adversarial search 连接 attack discovery、带 metadata 的 defense dataset 与 adapter fine-tuning。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：正文已承载，`PLATFORM-SECURITY` → [安全数据闭环还可由当前 policy 生成 adversarial candidates（正文段落）](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Position: LLM Inference Should Be Evaluated as Energy-to-Token Production](https://arxiv.org/html/2605.11733v1) | 2026-05-13T08:00:00+08:00 | quality/SLO-conditioned energy-to-token contract 把 compute、delivered power、cooling、PUE 与 utilization 放进同一产能上界。；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`PLATFORM-COST` → [Installed Power 不是可部署 AI Capacity](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [Training-Inference Consistent Segmented Execution for Long-Context LLMs](https://arxiv.org/html/2605.11744v1) | 2026-05-13T08:00:00+08:00 | Based on this insight, we propose a training-inference consistent segment-level generation framework, in which training and inference follow the same segment-level forward execution semantics.；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`INFER-KV-CACHE` → [Segmented Execution 必须在训练与推理共享同一语义](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [When Reasoning Traces Become Performative: Step-Level Evidence that Chain-of-Thought Is an Imperfect Oversight Channel](https://arxiv.org/html/2605.11746v1) | 2026-05-13T08:00:00+08:00 | Chain-of-thought (CoT) traces are increasingly used both to improve language model capability and to audit model behavior, implicitly assuming that the visible trace remains synchronized with the computation that determines the answer.；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`PLATFORM-EVALUATION-SYSTEM` → [Evaluation Identity 必须包含 Harness 与 Environment](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [DreamAvoid: Critical-Phase Test-Time Dreaming to Avoid Failures in VLA Policies](https://arxiv.org/html/2605.11750v1) | 2026-05-13T08:00:00+08:00 | critical-phase trigger、action proposals 与 short-horizon dream evaluator 形成 test-time VLA failure-avoidance gate，dream 只拥有候选排序权。；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`MULTIMODAL-EMBODIED-VLA` → [Reason–Imagine–Act 把内部 Rollout 变成 Proposal，而非执行权限](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Behavioral Integrity Verification for AI Agent Skills](https://arxiv.org/html/2605.11770v1) | 2026-05-13T08:00:00+08:00 | Agent skills extend LLM agents with privileged third-party capabilities such as filesystem access, credentials, network calls, and shell execution.；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：正文已承载，`AGENT-PLATFORM` → [Skill Lifecycle 需要 Admission 与 Runtime 两个 Gate](../../../../books/part-07-agent/84-agent-platform.md) |
| [Five Attacks on x402 Agentic Payment Protocol](https://arxiv.org/html/2605.11781v1) | 2026-05-13T08:00:00+08:00 | In this paper, we formally analyze x402 and empirically show that it is vulnerable in both design and implementation.；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`PLATFORM-SECURITY` → [Canonical Action 与 Effect-time Authorization](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [ROMER: Expert Replacement and Router Calibration for Robust MoE LLMs on Analog Compute-in-Memory Systems](https://arxiv.org/html/2605.11800v1) | 2026-05-13T08:00:00+08:00 | analog CIM noise 会同时破坏 expert load balance 与 clean-trained router，部署校准必须联合 expert replacement 和 router logits。；3 + 3 + 2 = 8 | 深入完成 | 整合：已写入待终审，`INFER-TENSORRT-LLM` → [MoE 的 Calibration Identity 必须覆盖 Expert Activation Distribution](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Learning Action Manifold with Multi-view Latent Priors for Robotic Manipulation](https://arxiv.org/html/2605.11832v1) | 2026-05-13T08:00:00+08:00 | multi-view geometry prior、occlusion gate 与 action manifold expert 改变 VLA 的几何状态和动作表示。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：正文已承载，`MULTIMODAL-EMBODIED-VLA` → [坐标系归一化是 Representation 到 Action Schema 的桥](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Gradient Clipping Beyond Vector Norms: A Spectral Approach for Matrix-Valued Parameters](https://arxiv.org/html/2605.11838v1) | 2026-05-13T08:00:00+08:00 | Motivated by this phenomenon, we propose spectral clipping, which stabilizes training by clamping singular values that exceed a threshold while preserving the singular directions.；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`TRAIN-PRETRAINING` → [Gradient Clipping 的正确边界与顺序](../../../../books/part-04-training-system/28-pretraining.md) |
| [Probabilistic Calibration Is a Trainable Capability in Language Models](https://arxiv.org/html/2605.11845v1) | 2026-05-13T08:00:00+08:00 | We study whether this capability can be improved directly through fine-tuning.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`PLATFORM-EVALUATION-SYSTEM` → [Calibration Slice 必须包含 Language × Model Scale × Estimator Contract](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [UniVLR: Unifying Text and Vision in Visual Latent Reasoning for Multimodal LLMs](https://arxiv.org/html/2605.11856v1) | 2026-05-13T08:00:00+08:00 | UniVLR 将文字 CoT 与辅助图像写入统一 visual canvas，再压缩为连续 latent reasoning state。；2 + 1 + 2 = 5 | 深入完成 | 整合：已写入待终审，`MULTIMODAL-REPRESENTATION` → [理解与生成也不必被迫共享全部参数](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Beyond Parameter Aggregation: Semantic Consensus for Federated Fine-Tuning of LLMs](https://arxiv.org/html/2605.11857v1) | 2026-05-13T08:00:00+08:00 | We present a theoretical analysis and empirical results demonstrating that this approach can match strong federated fine-tuning baselines while substantially reducing communication by orders of magnitude (e.g., analytically by a factor of $1006$ for Llama3.1-405B), as well as reductions in runtime and energy consumption.；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`TRAIN-DISTRIBUTED-TRAINING` → [跨 Model Family 的 Federated 协作不能继续聚合 Parameters](../../../../books/part-04-training-system/36-distributed-training.md) |
| [IPI-proxy: An Intercepting Proxy for Red-Teaming Web-Browsing AI Agents Against Indirect Prompt Injection](https://arxiv.org/html/2605.11868v1) | 2026-05-13T08:00:00+08:00 | We present IPI-proxy, an open-source toolkit for red-teaming web-browsing agents against indirect prompt injection (IPI).；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`PLATFORM-SECURITY` → [从资产与信任边界开始](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [LOFT: Low-Rank Orthogonal Fine-Tuning via Task-Aware Support Selection](https://arxiv.org/html/2605.11872v1) | 2026-05-13T08:00:00+08:00 | orthogonal PEFT 往往把 adaptation support 与 support 内 transformation 混在同一参数化；LOFT 将两者分开并让 downstream gradient 选择 support。；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入待终审，`TRAIN-LORA` → [Rank 与 target modules 决定更新空间](../../../../books/part-04-training-system/30-lora.md) |
| [On-Policy Self-Evolution via Failure Trajectories for Agentic Safety Alignment](https://arxiv.org/html/2605.11882v1) | 2026-05-13T08:00:00+08:00 | on-policy failure trajectory repair 将 Agent safety 从静态数据训练改为当前 policy 失败、修复、验证和回放的闭环。；3 + 2 + 2 = 7 | 深入完成 | 整合：已写入待终审，`PLATFORM-SECURITY` → [安全数据闭环还可由当前 policy 生成 adversarial candidates](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Proteus: A Self-Evolving Red Team for Agent Skill Ecosystems](https://arxiv.org/html/2605.11891v1) | 2026-05-13T08:00:00+08:00 | We frame this risk as \emph{adaptive leakage} -- whether a budgeted attacker can iteratively revise a skill until it passes audit and produces verified runtime harm -- and present \ours{}, a grey-box self-evolving red-team framework for measuring it.；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`PLATFORM-SECURITY` → [Skill Poisoning 的真值是 Side Effect，而不是是否被调用](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [When Simulation Lies: A Sim-to-Real Benchmark and Domain-Randomized RL Recipe for Tool-Use Agents](https://arxiv.org/html/2605.11928v1) | 2026-05-13T08:00:00+08:00 | We study these failures as a sim-to-real gap in the tool-use partially observable Markov decision process (POMDP), where deployment noise enters through the observation, action space, reward-relevant metadata, or transition dynamics.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`AGENT-TOOL-CALLING` → [Observation 也不可信](../../../../books/part-07-agent/78-tool-calling.md) |
| [From Reaction to Anticipation: Proactive Failure Recovery through Agentic Task Graph for Robotic Manipulation](https://arxiv.org/html/2605.11951v1) | 2026-05-13T08:00:00+08:00 | Inspired by the human capability to anticipate and proactively plan for potential failures, we introduce AgentChord, an agentic system that models a manipulation task as a directed task graph.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`AGENT-WORKFLOW` → [Durable Execution 与 Replay](../../../../books/part-07-agent/81-workflow.md) |
| [The Illusion of Power Capping in LLM Decode: A Phase-Aware Energy Characterisation Across Attention Architectures](https://arxiv.org/html/2605.11999v1) | 2026-05-13T08:00:00+08:00 | We show the appearance is illusory for the phase that dominates production serving: autoregressive decode.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`PLATFORM-COST` → [Generation Energy 不是 Token 数的线性函数](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [CR^2: Cost-Aware Risk-Controlled Routing for Wireless Device-Edge LLM Inference](https://arxiv.org/html/2605.12001v1) | 2026-05-13T08:00:00+08:00 | In this paper, we formulate mobile edge LLM routing as a deployment-constrained, cost-aware decision problem, and propose CR^2, a two-stage device-edge routing framework.；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：正文已承载，`INFER-SCHEDULING` → [目标函数不止吞吐](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [L2P: Unlocking Latent Potential for Pixel Generation](https://arxiv.org/html/2605.12013v1) | 2026-05-13T08:00:00+08:00 | L2P 用 latent diffusion 的合成图像训练 pixel-space generator，在 inference 移除 VAE，改变 representation/training boundary。；2 + 1 + 2 = 5 | 深入完成 | 整合：已写入待终审，`MULTIMODAL-GENERATIVE-PARADIGMS` → [Output Decoder 是独立的版本化 Generation Artifact](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [SAGE: Scalable Automated Robustness Augmentation for LLM Knowledge Evaluation](https://arxiv.org/html/2605.12022v1) | 2026-05-13T08:00:00+08:00 | SAGE 将 robustness variant generation 与 rubric verification 组成版本化 evaluation artifact pipeline。；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入待终审，`PLATFORM-EVALUATION-SYSTEM` → [Benchmark 生成器也会塑造被评估的任务人口](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SkillGraph: Skill-Augmented Reinforcement Learning for Agents via Evolving Skill Graphs](https://arxiv.org/html/2605.12039v1) | 2026-05-13T08:00:00+08:00 | isolated skill entries 只按语义相似度检索，无法表达前置关系，也无法治理 merge/split/delete；SkillGraph 把 procedural memory 变成 typed evolving graph。；3 + 2 + 2 = 7 | 深入完成 | 整合：已写入待终审，`AGENT-MEMORY` → [Procedural Memory 的压缩单位应是可展开的 Contract Graph](../../../../books/part-07-agent/77-memory.md) |
| [OmniRefine: Alignment-Aware Cooperative Compression for Efficient Omnimodal Large Language Models](https://arxiv.org/html/2605.12056v1) | 2026-05-13T08:00:00+08:00 | 固定/native 压缩单元会切断 audio-video correspondence；OmniRefine 先按跨模态相似度重划 chunk，再在 chunk 内联合分配 audio/video token。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：正文已承载，`MULTIMODAL-REPRESENTATION` → [固定预算要先分配信息责任，再选择具体 Token](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [SAGE: A Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory](https://arxiv.org/html/2605.12061v1) | 2026-05-13T08:00:00+08:00 | self-evolving graph memory 把 writer、reader 与反馈分权，记忆图成为可修订状态而非静态 retrieval middleware。；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：正文已承载，`AGENT-MEMORY` → [Derived Graph 更新必须沿 Evidence Dependency 传播](../../../../books/part-07-agent/77-memory.md) |
| [Property-Level Reconstructability of Agent Decisions: An Anchor-Level Pilot Across Vendor SDK Adapter Regimes](https://arxiv.org/html/2605.12078v1) | 2026-05-13T08:00:00+08:00 | Agentic AI failures need post-hoc reconstruction: what the agent did, on whose authority, against which policy, and from what reasoning.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`PLATFORM-TRACE` → [Span 的最小语义](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [Intermediate Artifacts as First-Class Citizens: A Data Model for Durable Intermediate Artifacts in Agentic Systems](https://arxiv.org/html/2605.12087v1) | 2026-05-13T08:00:00+08:00 | We argue that such systems should preserve durable, inspectable intermediate artifacts: typed, structured, addressable, versioned, dependency-aware, authoritative, and consumable by downstream computation.；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`AGENT-PLATFORM` → [Agent Runtime State Machine](../../../../books/part-07-agent/84-agent-platform.md) |
| [Autonomy and Agency in Agentic AI: Architectural Tactics for Regulated Contexts](https://arxiv.org/html/2605.12105v1) | 2026-05-13T08:00:00+08:00 | agency 与 autonomy 是耦合的部署维度；checkpoints、escalation、tool fencing 和 write staging 调节 effect authority。；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`AGENT-PLATFORM` → [长任务的人类边界应前移到目标与结构性 Commit](../../../../books/part-07-agent/84-agent-platform.md) |
| [AB-Sparse: Sparse Attention with Adaptive Block Size for Accurate and Efficient Long-Context Inference](https://arxiv.org/html/2605.12110v1) | 2026-05-13T08:00:00+08:00 | block-sparse attention 的固定 block size 隐含 head 同质性；adaptive per-head block 与 kernel/layout 必须联合设计。；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`MODEL-LONG-CONTEXT` → [Conditional Attention 的路由粒度必须匹配执行粒度](../../../../books/part-02-model/22-long-context.md) |
| [When Policy Entropy Constraint Fails: Preserving Diversity in Flow-based RLHF via Perceptual Entropy](https://arxiv.org/html/2605.12112v1) | 2026-05-13T08:00:00+08:00 | flow-based RLHF 中固定 policy entropy 不能反映视觉多样性坍缩，perceptual entropy 因而成为新的控制变量。；3 + 1 + 3 = 7 | 深入完成 | 整合：已写入待终审，`TRAIN-RLHF` → [反馈预算必须绑定样本粒度与可观测不确定性](../../../../books/part-04-training-system/31-rlhf.md) |
| [To Whom Do Language Models Align? Measuring Principal Hierarchies Under High-Stakes Competing Demands](https://arxiv.org/html/2605.12120v1) | 2026-05-13T08:00:00+08:00 | 模型在 advisory prompt 中维护专业规范，不代表在实际 drafting/action framing 中仍遵从；principal hierarchy 必须作为 domain × task framing × stakeholder 的行为合同测量。；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`PLATFORM-EVALUATION-SYSTEM` → [评估对象有四个层次](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Disentangled Sparse Representations for Concept-Separated Diffusion Unlearning](https://arxiv.org/html/2605.12122v1) | 2026-05-13T08:00:00+08:00 | 普通 sparse reconstruction SAE 让多个概念共享 feature，压制目标概念时会连带损伤非目标内容；concept-aware clustering 把删除边界移到表示 support。；2 + 1 + 2 = 5 | 深入完成 | 整合：已写入待终审，`PLATFORM-SECURITY` → [Unlearning 必须分开参数擦除与推理拒答](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [It's Not the Size: Harness Design Determines Operational Stability in Small Language Models](https://arxiv.org/html/2605.12129v1) | 2026-05-13T08:00:00+08:00 | This paper experimentally analyzes how the level of harness engineering affects the operational performance of small language models (SLMs, 2-3B parameters).；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`AGENT-WORKFLOW` → [Deterministic Spine，Agentic Nodes](../../../../books/part-07-agent/81-workflow.md) |
| [Rollout Cards: A Reproducibility Standard for Agent Research](https://arxiv.org/html/2605.12131v1) | 2026-05-13T08:00:00+08:00 | We introduce rollout cards: publication bundles that preserve the rollout record and declare the views, reporting rules, and drops manifests behind reported scores.；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`PLATFORM-EVALUATION-SYSTEM` → [第一个不变量：评估声明必须绑定完整对象](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Premover: Fast Vision-Language-Action Control by Acting Before Instructions Are Complete](https://arxiv.org/html/2605.12160v1) | 2026-05-13T08:00:00+08:00 | We introduce Premover, a lightweight module that converts this idle window into useful precomputation.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`MULTIMODAL-EMBODIED-VLA` → [Latency 与 control frequency](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Lower bounds for one-layer transformers that compute parity](https://arxiv.org/html/2605.12171v1) | 2026-05-13T08:00:00+08:00 | ‘一层 attention 足以全局交互’不等于它能以固定 heads 和简单 post-process 表达全局 parity；复杂度必须同时计 heads 与后处理函数度数。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`MODEL-SELF-ATTENTION` → [Self Attention 获得了什么](../../../../books/part-02-model/14-self-attention.md) |
| [Do Enterprise Systems Need Learned World Models? The Importance of Context to Infer Dynamics](https://arxiv.org/html/2605.12178v1) | 2026-05-13T08:00:00+08:00 | enterprise agent 通过读取 live configuration 恢复环境动态，改变 learned world model 与 runtime discovery 的 state-owner 分工。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`MULTIMODAL-WORLD-MODELS` → [World Model 不必保存全部 Observation，但必须覆盖下游 Query Closure](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [SyncDPO: Enhancing Temporal Synchronization in Video-Audio Joint Generation via Preference Learning](https://arxiv.org/html/2605.12179v1) | 2026-05-13T08:00:00+08:00 | SyncDPO 用规则化时间扰动在线构造 preference negatives，并以 curriculum 调节 video-audio 对齐难度。；2 + 1 + 2 = 5 | 深入完成 | 整合：已写入待终审，`TRAIN-DPO` → [Preference Pair 选择是实验设计，不只是数据量选择](../../../../books/part-04-training-system/34-dpo.md) |
| [SOAR: Scale Optimization for Accurate Reconstruction in NVFP4 Quantization](https://arxiv.org/html/2605.12245v1) | 2026-05-13T08:00:00+08:00 | To address these issues, we propose Scale Optimization for Accurate Reconstruction (SOAR), a novel post-training quantization framework that improves the accuracy of NVFP4 quantization.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`INFER-TENSORRT-LLM` → [量化为什么不自动带来加速](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [How Useful Is Cross-Domain Generalization for Training LLM Monitors?](https://arxiv.org/html/2605.12265v1) | 2026-05-13T08:00:00+08:00 | We study whether training on multiple classification tasks, each with its own prompt, improves performance on new domains with new classification prompts.；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`PLATFORM-MONITORING` → [小 Monitor 需要专门训练其检测边界](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [Executable Agentic Memory for GUI Agent](https://arxiv.org/html/2605.12294v1) | 2026-05-13T08:00:00+08:00 | GUI agent 每屏重新解释并自由生成动作，会在长任务中反复支付 token 和决策误差；EAM 将复用 routine 编译为可搜索 Knowledge Graph。；3 + 2 + 2 = 7 | 深入完成 | 整合：已写入待终审，`AGENT-MEMORY` → [Procedural Memory 的压缩单位应是可展开的 Contract Graph](../../../../books/part-07-agent/77-memory.md) |
| [Grid Games: The Power of Multiple Grids for Quantizing Large Language Models](https://arxiv.org/html/2605.12327v1) | 2026-05-13T08:00:00+08:00 | microscaled FP4 每组固定一张 grid 会浪费分布适配空间；多 grid 将每组格式选择编码进 scale metadata。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`INFER-TENSORRT-LLM` → [Block Scale 也是可搜索的执行状态](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [$δ$-mem: Efficient Online Memory for Large Language Models](https://arxiv.org/html/2605.12357v1) | 2026-05-13T08:00:00+08:00 | δ-mem 用固定大小 delta-rule associative state 在线修正 frozen attention，明确模型内 memory 的状态/容量边界。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`MODEL-LONG-CONTEXT` → [路线六：让模型在 Test Time 更新内部记忆](../../../../books/part-02-model/22-long-context.md) |
| [Attacks and Mitigations for Distributed Governance of Agentic AI under Byzantine Adversaries](https://arxiv.org/html/2605.12364v1) | 2026-05-13T08:00:00+08:00 | We then present three types of solutions for securing the Provider that offer different trade-offs between security and performance.；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`AGENT-MULTI-AGENT` → [Governance Provider 也必须进入 Byzantine Threat Model](../../../../books/part-07-agent/82-multi-agent.md) |
| [Classifier Context Rot: Monitor Performance Degrades with Context Length](https://arxiv.org/html/2605.12366v1) | 2026-05-13T08:00:00+08:00 | We show that when used as classifiers, current frontier models fail to notice dangerous actions more often in longer transcripts.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`PLATFORM-MONITORING` → [长轨迹 Monitor 需要可回到原始证据的有界状态](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [Trust the Batch, On- or Off-Policy: Adaptive Policy Optimization for RL Post-Training](https://arxiv.org/html/2605.12380v1) | 2026-05-13T08:00:00+08:00 | 固定 clipping/off-policy 超参把 trust-region 与 behavior mismatch 预先混在一起，task、scale 或 rollout execution 改变就需重调；batch ratio distribution 可作为当前 mismatch state。；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`TRAIN-GRPO` → [Asynchronous RL 必须把 Policy Staleness 写进 Advantage](../../../../books/part-04-training-system/33-grpo.md) |
| [Scalable Token-Level Hallucination Detection in Large Language Models](https://arxiv.org/html/2605.12384v1) | 2026-05-13T08:00:00+08:00 | To address these limitations, we propose TokenHD, a holistic pipeline for training token-level hallucination detectors.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`PLATFORM-MONITORING` → [Model-internal Sensor 必须从 Inference Hot Path 解耦](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [NCCLZ: Compression-Enabled GPU Collectives with Decoupled Quantization and Entropy Coding](https://arxiv.org/html/2605.12396v1) | 2026-05-13T08:00:00+08:00 | Experiments on scientific datasets, training gradients, and synthetic workloads show up to 9.65x speedup over NCCL and up to 3.34x improvement over prior compression-assisted collective libraries.；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`TRAIN-DISTRIBUTED-TRAINING` → [通信压缩必须把编解码写进 Critical Path](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Aligning Flow Map Policies with Optimal Q-Guidance](https://arxiv.org/html/2605.12416v1) | 2026-05-13T08:00:00+08:00 | Flow Map 的任意步跳转与 Q-guided trust-region search 改变 action generation 的 latency、proposal 和 control contract。；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入待终审，`MULTIMODAL-EMBODIED-VLA` → [Hierarchical Generative Planner 要把 Subgoal 与低层轨迹分权](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Geometric Factual Recall in Transformers](https://arxiv.org/html/2605.12426v1) | 2026-05-13T08:00:00+08:00 | 把 MLP 权重直接视为事实 key-value memory 会导出事实数线性参数需求；几何表征允许 embedding 叠加关系，而小 MLP 只做 relation-conditioned selector。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`MODEL-FFN` → [MLP 是不是“知识库”](../../../../books/part-02-model/16-feed-forward-mlp.md) |
| [ORCE: Order-Aware Alignment of Verbalized Confidence in Large Language Models](https://arxiv.org/html/2605.12446v1) | 2026-05-13T08:00:00+08:00 | decoupled confidence generation 与 order-aware reward 改变校准状态和证据边界；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入并通过独立写后复核，`PLATFORM-EVALUATION-SYSTEM` → [Verbalized Confidence 解耦与按序校准](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Multi-Stream LLMs: Unblocking Language Models with Parallel Streams of Thoughts, Inputs and Outputs](https://arxiv.org/html/2605.12460v1) | 2026-05-13T08:00:00+08:00 | multi-stream instruction tuning 将 thought/input/output 拆成并行因果 streams，使单流消息格式从模型不变量降为接口选择。；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入待终审，`MODEL-DECODER-ONLY` → [Next-token 接口不要求内部状态只有一个粒度](../../../../books/part-02-model/18-decoder-only.md) |
| [Search Your Block Floating Point Scales!](https://arxiv.org/html/2605.12464v1) | 2026-05-13T08:00:00+08:00 | ScaleSearch 把 BFP/NVFP4 block scale 从 max heuristic 改为可搜索的执行/误差选择。；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入待终审，`INFER-TENSORRT-LLM` → [量化为什么不自动带来加速](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Solve the Loop: Attractor Models for Language and Reasoning](https://arxiv.org/html/2605.12466v1) | 2026-05-13T08:00:00+08:00 | 固定-depth looped Transformer 训练不稳且部署成本固定；Attractor Model 将反复 refinement 改为 fixed-point solver，并用 implicit differentiation 避免训练 memory 随 effective depth 增长。；3 + 2 + 2 = 7 | 深入完成 | 整合：已写入待终审，`MODEL-TRANSFORMER-LAYER` → [Recurrence 可以只占据 Decoder 的局部层段](../../../../books/part-02-model/17-transformer-layer.md) |
| [KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference](https://arxiv.org/html/2605.12471v1) | 2026-05-13T08:00:00+08:00 | We introduce KV-Fold, a simple, training-free long-context inference protocol that treats the key-value (KV) cache as the accumulator in a left fold over sequence chunks.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`INFER-KV-CACHE` → [Cache Object 从 Token KV 扩展到可组合 Transition](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/html/2605.12474v1) | 2026-05-13T08:00:00+08:00 | We study reward hacking in rubric-based RL, where a policy is optimized against a training verifier but evaluated against a cross-family panel of three frontier judges, reducing dependence on any single evaluator.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`TRAIN-RLHF` → [Reward hacking 与 Goodhart's Law](../../../../books/part-04-training-system/31-rlhf.md) |
| [OmniNFT: Modality-wise Omni Diffusion Reinforcement for Joint Audio-Video Generation](https://arxiv.org/html/2605.12480v1) | 2026-05-13T08:00:00+08:00 | joint audio-video diffusion 的单一 global advantage 会混合不一致目标、跨 modality gradient 与稀疏同步区域；OmniNFT 将 credit 按 modality/layer/region 分配。；3 + 2 + 2 = 7 | 深入完成 | 整合：已写入待终审，`TRAIN-RLHF` → [从二元偏好到分布条件化的连续 Reward](../../../../books/part-04-training-system/31-rlhf.md) |
| [ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents](https://arxiv.org/html/2605.12481v1) | 2026-05-13T08:00:00+08:00 | GUI 原子动作与高层 tool call 共存时，agent 不知道何时切换，且缺少 interleaved trajectories；ToolCUA 将 path choice 作为独立训练对象。；3 + 3 + 2 = 8 | 深入完成 | 整合：已写入待终审，`AGENT-WORKFLOW` → [Logical Plan 与 Physical Schedule 必须分别验收](../../../../books/part-07-agent/81-workflow.md) |
| [Pion: A Spectrum-Preserving Optimizer via Orthogonal Equivalence Transformation](https://arxiv.org/html/2605.12492v1) | 2026-05-13T08:00:00+08:00 | Adam/Muon 的 additive update 会同时改变方向与 singular spectrum；Pion 用左右 orthogonal transformations 将谱固定，只优化权重几何。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入待终审，`TRAIN-PRETRAINING` → [Optimizer Update 要尊重参数块的对称性](../../../../books/part-04-training-system/28-pretraining.md) |
| [LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues](https://arxiv.org/html/2605.12493v1) | 2026-05-13T08:00:00+08:00 | To address this gap, we introduce LongMemEval-V2 (LME-V2), a benchmark for evaluating whether memory systems can help agents acquire the experience needed to become knowledgeable colleagues in customized environments.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：正文已承载，`AGENT-MEMORY` → [评估 Memory](../../../../books/part-07-agent/77-memory.md) |
| [AlphaGRPO: Unlocking Self-Reflective Multimodal Generation in UMMs via Decompositional Verifiable Reward](https://arxiv.org/html/2605.12495v1) | 2026-05-13T08:00:00+08:00 | AlphaGRPO 将统一多模态生成 reward 分解为离散 reasoning 与连续视觉 trajectory 的原子可验证问题。；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入待终审，`TRAIN-GRPO` → [Verifiable Reward 不等于每个样本都可学习](../../../../books/part-04-training-system/33-grpo.md) |
| [From Web to Pixels: Bringing Agentic Search into Visual Perception](https://arxiv.org/html/2605.12497v1) | 2026-05-13T08:00:00+08:00 | Pixel-Searcher 把 web evidence acquisition、实体身份解析与 box/mask grounding 串成可追踪的 search-to-pixel workflow。；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入待终审，`AGENT-RAG` → [多模态 Evidence 还要检查模态间的覆盖与支配关系](../../../../books/part-07-agent/76-rag.md) |
| [SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture](https://arxiv.org/html/2605.12500v1) | 2026-05-13T08:00:00+08:00 | SenseNova-U1 用 pixels/words 共享 token/backbone 与轻量 patch encoder/decoder 构成 native understanding-generation interface。；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：正文已承载，`MULTIMODAL-REPRESENTATION` → [理解与生成也不必被迫共享全部参数（正文段落）](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |

| [Rethinking Supervision Granularity: Segment-Level Learning for LLM-Based Theorem Proving](https://arxiv.org/html/2605.11905v1) | 2026-05-13T08:00:00+08:00 | proof supervision 从 tactic/whole-proof 两端改为 open-goal coherent segment，并复用到 rollout；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入并通过独立写后复核，`TRAIN-DATA` → [监督粒度应跟随可验证状态边界](../../../../books/part-04-training-system/27-data.md) |
| [Learn to Think: Improving Multimodal Reasoning through Vision-Aware Self-Improvement Training](https://arxiv.org/html/2605.11931v1) | 2026-05-13T08:00:00+08:00 | partial-correct prefix reuse 与 visual-attention sensor 组成多模态自改进数据回路；2 + 2 + 2 = 6 | 深入完成 | 整合：已写入并通过独立写后复核，`TRAIN-SFT` → [复用正确局部并独立验证视觉依赖](../../../../books/part-04-training-system/29-sft.md) |
| [Uncertainty Quantification for LLM-based Code Generation](https://arxiv.org/html/2605.12201v1) | 2026-05-13T08:00:00+08:00 | partial-program set、multiple testing 与 selective execution 形成多解 risk contract；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入并通过独立写后复核，`PLATFORM-EVALUATION-SYSTEM` → [Prediction Set 必须适配结构化多解输出](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [EVOCHAMBER: Test-Time Co-evolution of Multi-Agent System at Individual, Team, and Population Scales](https://arxiv.org/html/2605.11136v1) | 2026-05-13T08:00:00+08:00 | Multi-Agent 的 test-time learning 不能简化为 N 个单 Agent memory 更新：individual context、team composition/collaboration structure 与 population knowledge flow 是三个不同状态 owner。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入并通过独立写后复核，`AGENT-MULTI-AGENT` → [Participation Graph 与 Step Orchestration 是联合状态](../../../../books/part-07-agent/82-multi-agent.md) |
| [The Bicameral Model: Bidirectional Hidden-State Coupling Between Parallel Language Models](https://arxiv.org/html/2605.11167v1) | 2026-05-13T08:00:00+08:00 | 两个 frozen LM 可在每个 generation step 通过 trainable hidden-state interface 双向通信；这改变的不是消息格式，而是并发 agent 的同步、causal schedule 与 tool-state ownership。；3 + 2 + 2 = 7 | 深入完成 | 整合：已写入并通过独立写后复核，`AGENT-MULTI-AGENT` → [Latent Communication 只能压缩 Payload，不能隐藏 Identity](../../../../books/part-07-agent/82-multi-agent.md) |
| [OLIVIA: Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents](https://arxiv.org/html/2605.11169v1) | 2026-05-13T08:00:00+08:00 | 在 frozen ReAct reasoner 与 tool execution 之间加入 deployment-time contextual bandit，使 action selection 能由 action-level feedback 在线更新，而不重训 reasoning model。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入并通过独立写后复核，`AGENT-TOOL-CALLING` → [执行后行为只能更新下一次 Intent Gate](../../../../books/part-07-agent/78-tool-calling.md) |
| [PIVOT: Bridging Planning and Execution in LLM Agents via Trajectory Refinement](https://arxiv.org/html/2605.11225v1) | 2026-05-13T08:00:00+08:00 | 把完整 trajectory 视为可版本化、可验证的优化状态：执行产生 discrepancy，再用 structured textual gradient 定位并替换 suffix，只有验证后不退化才提交。；3 + 2 + 2 = 7 | 深入完成 | 整合：已写入并通过独立写后复核，`AGENT-PLANNING` → [Replanning 的触发条件](../../../../books/part-07-agent/79-planning.md) |
| [BadSKP: Backdoor Attacks on Knowledge Graph-Enhanced LLMs with Soft Prompts](https://arxiv.org/html/2605.11996v1) | 2026-05-13T08:00:00+08:00 | KG-derived soft prompt 是独立于可见文本的 graph-conditioned channel；攻击上游 KG representation 可在不改用户文本时改变模型行为，因此 graph→projector→prompt 必须成为供应链信任边界。；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入并通过独立写后复核，`PLATFORM-SECURITY` → [Embedding 也是可执行数据供应链的一部分](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [MEME: Multi-entity &amp; Evolving Memory Evaluation](https://arxiv.org/html/2605.12477v1) | 2026-05-13T08:00:00+08:00 | 长期 memory 不能只测静态 recall；多实体状态随时间变化时，Deletion、Cascade 与 Absence 分别测试过期事实、依赖传播和无证据拒答。；3 + 3 + 3 = 9 | 深入完成 | 整合：已写入并通过独立写后复核，`PLATFORM-EVALUATION-SYSTEM` → [动态知识系统需要关系型回归，而不只是静态答案分数](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [$ξ$-DPO: Direct Preference Optimization via Ratio Reward Margin](https://arxiv.org/html/2605.10981v1) | 2026-05-13T08:00:00+08:00 | SimPO 的 beta/gamma 同时耦合过滤强度、数据 gap 与目标 margin；ratio margin 使目标有界且可解释。；2 + 1 + 2 = 5 | 深入完成 | 整合：已写入并通过独立写后复核，`TRAIN-DPO` → [Preference Scale 与 Optimization Scale 不应共用一个旋钮](../../../../books/part-04-training-system/34-dpo.md) |
| [Uniform Scaling Limits in AdamW-Trained Transformers](https://arxiv.org/html/2605.11059v1) | 2026-05-13T08:00:00+08:00 | 给出受限 attention-only/finite-time 条件下 forward-backward joint scaling limit，明确理论可迁移边界。；1 + 2 + 2 = 5 | 标准完成 | 已有覆盖：`TRAIN-PRETRAINING` → [Optimizer 不是与参数化无关的旋钮](../../../../books/part-04-training-system/28-pretraining.md)；独立复核通过 |
| [Muon is Not That Special: Random or Inverted Spectra Work Just as Well](https://arxiv.org/html/2605.11181v1) | 2026-05-13T08:00:00+08:00 | exact-v1 反驳“精确 LMO/全局几何是 Muon 收益必要原因”，把解释转向 alignment、descent potential 与 step-size matching。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入并通过独立写后复核，`TRAIN-PRETRAINING` → [Whitening 的收益取决于 Gradient Spectrum 所在 Regime](../../../../books/part-04-training-system/28-pretraining.md) |
| [Internalizing Curriculum Judgment for LLM Reinforcement Fine-Tuning](https://arxiv.org/html/2605.11235v1) | 2026-05-13T08:00:00+08:00 | current policy 通过近期 variance evidence 学习 curriculum proposal，但 external verifier 仍拥有 outcome truth。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入并通过独立写后复核，`TRAIN-GRPO` → [Group Size 改变什么](../../../../books/part-04-training-system/33-grpo.md) |
| [ReAD: Reinforcement-Guided Capability Distillation for Large Language Models](https://arxiv.org/html/2605.11290v1) | 2026-05-13T08:00:00+08:00 | 固定 token budget 下按 capability state、saturation 与 cross-capability spillover 动态重分配 teacher supervision。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入并通过独立写后复核，`TRAIN-SFT` → [从平均拟合转向覆盖尚未学会的序列](../../../../books/part-04-training-system/29-sft.md) |
| [Couple to Control: Joint Initial Noise Design in Diffusion Models](https://arxiv.org/html/2605.11311v1) | 2026-05-13T08:00:00+08:00 | 保持单样本 Gaussian marginal 不变，用 batch joint coupling 控制 gallery diversity。；3 + 2 + 3 = 8 | 深入完成 | 整合：已写入并通过独立写后复核，`MULTIMODAL-GENERATIVE-PARADIGMS` → [Continuous 与 Discrete Flow 的等价是有条件的](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |

## 4. 证据与知识整合

### [QuIDE: Mastering the Quantized Intelligence Trade-off via Active Optimization](https://arxiv.org/html/2605.10959v1)

**准入：** quantization decisions need workload-specific accuracy, compression and realized latency measurements, but collapsing them into one scalar intelligence index hides Pareto preferences and cannot be a universal execution objective

<!-- review:SF-2026-ARXIV-2605-10959:start -->
#### QuIDE: Mastering the Quantized Intelligence Trade-off via Active Optimization

问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。约束变化与机制：quantization decisions need workload-specific accuracy, compression and realized latency measurements, but collapsing them into one scalar intelligence index hides Pareto preferences and cannot be a universal execution objective。Method：`https://arxiv.org/html/2605.10959v1 §3 QuIDE Metric and Active Optimization`。

Evaluation：`https://arxiv.org/html/2605.10959v1 §4 Experiments`。Counterevidence/limits：`https://arxiv.org/html/2605.10959v1 §5 Limitations; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO`。Artifact：`https://arxiv.org/html/2605.10959v1 artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。

<!-- claim:SF-2026-ARXIV-2605-10959:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:SF-2026-ARXIV-2605-10959:end -->
<!-- review:SF-2026-ARXIV-2605-10959:end -->

**Books 对读：** `INFER-TENSORRT-LLM` → `books/part-05-inference-system/49-tensorrt-llm.md` 的“量化为什么不自动带来加速”已承载 workload-specific accuracy、compression 与 realized latency 必须共同验收，且单一 scalar 不能替代 Pareto 选择。判定：**No Change — Existing Coverage**。
### [Context-Gated Associative Retrieval: From Theory to Transformers](https://arxiv.org/html/2605.10970v1)

**准入：** 把 context-dependent gating 纳入 associative retrieval 的写入与读取规则，改变 attention/memory 的条件更新机制。

<!-- review:SF-2026-ARXIV-2605-10970:start -->
#### Context-Gated Associative Retrieval: From Theory to Transformers

问题、旧路径与约束变化：把 context-dependent gating 纳入 associative retrieval 的写入与读取规则，改变 attention/memory 的条件更新机制。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§3 Method and §4 Theory/connection to transformers。canonical owner=`MODEL-SELF-ATTENTION`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§4 empirical/theoretical connection。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§5 Discussion；无独立 Limitations，结论限于论文假设与受测 retrieval setting。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-10970:start -->exact-v1 支持：把 context-dependent gating 纳入 associative retrieval 的写入与读取规则，改变 attention/memory 的条件更新机制。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-10970:end -->

Books Decision=`No Change — Existing Coverage`；作者只形成命题比较与 root serial queue，不直接修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-10970:end -->

**Books 对读：** `MODEL-SELF-ATTENTION` → `books/part-02-model/14-self-attention.md` 的“从固定写入规则到目标导出的递归更新”。`books/part-02-model/14-self-attention.md` 的“从固定写入规则到目标导出的递归更新”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：把 context-dependent gating 纳入 associative retrieval 的写入与读取规则，改变 attention/memory 的条件更新机制。 判定：**No Change — Existing Coverage**。

### [Steering Without Breaking: Mechanistically Informed Interventions for Discrete Diffusion Language Models](https://arxiv.org/html/2605.10971v1)

**准入：** attribute-specific commit schedule 让离散 diffusion 的 steering 时点成为逐属性控制状态，而不是统一 timestep。

<!-- review:SF-2026-ARXIV-2605-10971:start -->
#### Steering Without Breaking: Mechanistically Informed Interventions for Discrete Diffusion Language Models

问题、旧路径与约束变化：attribute-specific commit schedule 让离散 diffusion 的 steering 时点成为逐属性控制状态，而不是统一 timestep。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§3 Method and §4 attribute-specific scheduling。canonical owner=`MULTIMODAL-GENERATIVE-PARADIGMS`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§5 Experiments。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§6 Conclusion 与 Appendix F 的 latency/trade-off；无独立 Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-10971:start -->exact-v1 支持：attribute-specific commit schedule 让离散 diffusion 的 steering 时点成为逐属性控制状态，而不是统一 timestep。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-10971:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-10971:end -->

**Books 对读：** `MULTIMODAL-GENERATIVE-PARADIGMS` → `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的“Commitment Policy 可以从未来稳定轨迹学习”。`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的“Commitment Policy 可以从未来稳定轨迹学习”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：attribute-specific commit schedule 让离散 diffusion 的 steering 时点成为逐属性控制状态，而不是统一 timestep。 判定：**Integrate — Applied; independent post-write review pending**。

### [Rotation-Preserving Supervised Fine-Tuning](https://arxiv.org/html/2605.10973v1)

**准入：** rotation-preserving SFT 以敏感 pretrained directions 为约束，重写 adaptation 与 forgetting 的可观测权衡。

<!-- review:SF-2026-ARXIV-2605-10973:start -->
#### Rotation-Preserving Supervised Fine-Tuning

问题、旧路径与约束变化：rotation-preserving SFT 以敏感 pretrained directions 为约束，重写 adaptation 与 forgetting 的可观测权衡。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§3 Theory and §4 Method。canonical owner=`TRAIN-SFT`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§5 Experiments。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§6 Conclusion 与 Appendices C–E；无独立 Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-10973:start -->exact-v1 支持：rotation-preserving SFT 以敏感 pretrained directions 为约束，重写 adaptation 与 forgetting 的可观测权衡。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-10973:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-10973:end -->

**Books 对读：** `TRAIN-SFT` → `books/part-04-training-system/29-sft.md` 的“Trainable Subspace 也是 Continual SFT 的评估变量”。`books/part-04-training-system/29-sft.md` 的“Trainable Subspace 也是 Continual SFT 的评估变量”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：rotation-preserving SFT 以敏感 pretrained directions 为约束，重写 adaptation 与 forgetting 的可观测权衡。 判定：**Integrate — Applied; independent post-write review pending**。

### [Vertex-Softmax: Tight Transformer Verification via Exact Softmax Optimization](https://arxiv.org/html/2605.10974v1)

**准入：** `Vertex-Softmax: Tight Transformer Verification via Exact Softmax Optimization` 通过“Certified verification of transformer attention requires bounding the softmax function over interval constraints on the pre-softmax scores.”改变 platform evaluation system 的可观察机制或决策边界；exact-v1 的证明范围限于“We further prove a formal optimality result showing that Vertex-Softmax is the tightest sound bound obtainable from score intervals alone, characterizing precisely what additional structure (score correlations, score-value coupling) is needed for further improvement.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO

<!-- review:SF-2026-ARXIV-2605-10974:start -->
#### Vertex-Softmax: Tight Transformer Verification via Exact Softmax Optimization

问题与演进：`Vertex-Softmax: Tight Transformer Verification via Exact Softmax Optimization` 通过“Certified verification of transformer attention requires bounding the softmax function over interval constraints on the pre-softmax scores.”改变 platform evaluation system 的可观察机制或决策边界；exact-v1 的证明范围限于“We further prove a formal optimality result showing that Vertex-Softmax is the tightest sound bound obtainable from score intervals alone, characterizing precisely what additional structure (score correlations, score-value coupling) is needed for further improvement.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.10974v1 §3 exact score-box softmax; §4 Vertex-CROWN — mechanism: Certified verification of transformer attention requires bounding the softmax function over interval constraints on the pre-softmax scores. Existing verifiers relax softmax ndependently of the downstream objective, leaving avoidable slack. We prove that the exact optimum of this score-box problem is attained at a vertex of the…`。

Evaluation：`https://arxiv.org/html/2605.10974v1 §5 certified-verification experiments — disclosed scope: We further prove a formal optimality result showing that Vertex-Softmax is the tightest sound bound obtainable from score intervals alone, characterizing precisely what additional structure (score correlations, score-value coupling) is needed for further improvement.`。

Non-proof / fallback：`https://arxiv.org/html/2605.10974v1 §6 limitations; score-box independence and surrounding verifier slack; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.10974v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-10974:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-10974:end -->
<!-- review:SF-2026-ARXIV-2605-10974:end -->

**Books 对读：** 原锚点“从目标到证据，而不是从指标到目标”只提供宽泛 evaluation 原则，没有承载 score-box 上 tight sound softmax bound、interval-only 最优性边界，以及进一步收紧需要 score correlation 或 score-value coupling 的结论。判定：**Integrate — Root Writeback Applied**。

### [LEAP: Unlocking dLLM Parallelism via Lookahead Early-Convergence Token Detection](https://arxiv.org/html/2605.10980v1)

**准入：** diffusion LM parallel decode 应检测 early-converged token，而不是把 high confidence 当作唯一安全 commit 条件

<!-- review:SF-2026-ARXIV-2605-10980:start -->
#### LEAP: Unlocking dLLM Parallelism via Lookahead Early-Convergence Token Detection

问题与演进：diffusion LM parallel decode 应检测 early-converged token，而不是把 high confidence 当作唯一安全 commit 条件。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.10980v1 §3 LEAP — mechanism: In response, we introduce LEAP (Lookahead Early-Convergence Token Detection for Accelerated Parallel Decoding).`。

Evaluation：`https://arxiv.org/html/2605.10980v1 §4 Experiments — disclosed scope: Diffusion Language Models (dLLMs) have garnered significant attention for their potential in highly parallel processing. The parallel capabilities of existing dLLMs stem from the assumption of conditional independence at high confidence levels, which ensures negligible discrepancy between the marginal and joint distributions. However, the stringent confidence…`。

Non-proof / fallback：`https://arxiv.org/html/2605.10980v1 §5 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.10980v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-10980:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-10980:end -->
<!-- review:SF-2026-ARXIV-2605-10980:end -->

**Books 对读：** `MULTIMODAL-GENERATIVE-PARADIGMS` → `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的“Early convergence 与 high confidence 不是同一个 Commit 证据”。books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md 的‘Early convergence 与 high confidence 不是同一个 Commit 证据’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：diffusion LM parallel decode 应检测 early-converged token，而不是把 high confidence 当作唯一安全 commit 条件 判定：**Integrate — Already present in current Books**。

### [AESOP: Adversarial Execution-path Selection to Overload Deep Learning Pipelines](https://arxiv.org/html/2605.10987v1)

**准入：** 动态 ML pipeline 的 availability attack surface 由 execution-path fan-out 与 downstream workload volume 共同决定，单模型 perturbation 预算不足以描述风险

<!-- review:SF-2026-ARXIV-2605-10987:start -->
#### AESOP: Adversarial Execution-path Selection to Overload Deep Learning Pipelines

问题与演进：动态 ML pipeline 的 availability attack surface 由 execution-path fan-out 与 downstream workload volume 共同决定，单模型 perturbation 预算不足以描述风险。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.10987v1 §IV Threat Model and AESOP — mechanism: We show that this structure creates an efficiency-attack surface that existing methods targeting single models cannot exploit: on identical inputs and budgets, path-aware targeting inflates FLOPs by $2,407\times$ while the strongest single-model baseline achieves $117\times$ -- a $20\times$ gap attributable entirely to where the attack is…`。

Evaluation：`https://arxiv.org/html/2605.10987v1 §VI Evaluation — disclosed scope: Modern machine learning deployments increasingly compose specialized models into dynamic inference pipelines, where upstream components produce intermediate predictions that determine the workload and inputs of downstream components. The cost of processing an input is therefore not determined by any single model, but by two coupled factors:…`。

Non-proof / fallback：`https://arxiv.org/html/2605.10987v1 §VII-C Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.10987v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-10987:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-10987:end -->
<!-- review:SF-2026-ARXIV-2605-10987:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“Availability 攻击从单模型开销扩展到动态路径”。books/part-06-ai-infrastructure/72-security.md 的‘Availability 攻击从单模型开销扩展到动态路径’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：动态 ML pipeline 的 availability attack surface 由 execution-path fan-out 与 downstream workload volume 共同决定，单模型 perturbation 预算不足以描述风险 判定：**Integrate — Already present in current Books**。

### [Skill Drift Is Contract Violation: Proactive Maintenance for LLM Agent Skill Libraries](https://arxiv.org/html/2605.10990v1)

**准入：** skill drift 应以 role-bearing environment contract violation 检测，而不是对版本字符串或任意值变化报警

<!-- review:SF-2026-ARXIV-2605-10990:start -->
#### Skill Drift Is Contract Violation: Proactive Maintenance for LLM Agent Skill Libraries

问题与演进：skill drift 应以 role-bearing environment contract violation 检测，而不是对版本字符串或任意值变化报警。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.10990v1 §3 Contract Extraction and Validation — mechanism: We formulate skill drift as contract violation and introduce \sgname{}, which extracts executable environment contracts from skill documents and validates only those role-bearing assumptions against known or live conditions.`。

Evaluation：`https://arxiv.org/html/2605.10990v1 §4 Evaluation — disclosed scope: LLM agents increasingly rely on reusable skill libraries, but these skills silently decay as the external services, packages, APIs, and configurations they reference evolve. Existing monitors detect such changes at the wrong granularity: they observe values, not the role those values play in a skill. A…`。

Non-proof / fallback：`https://arxiv.org/html/2605.10990v1 Appendix C Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.10990v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-10990:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-10990:end -->
<!-- review:SF-2026-ARXIV-2605-10990:end -->

**Books 对读：** `AGENT-PLATFORM` → `books/part-07-agent/84-agent-platform.md` 的“Skill Drift 应检测角色契约，而不是任意变化”。books/part-07-agent/84-agent-platform.md 的‘Skill Drift 应检测角色契约，而不是任意变化’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：skill drift 应以 role-bearing environment contract violation 检测，而不是对版本字符串或任意值变化报警 判定：**Integrate — Already present in current Books**。

### [Test-Time Personalization: A Diagnostic Framework and Probabilistic Fix for Scaling Failures](https://arxiv.org/html/2605.10991v1)

**准入：** Best-of-N personalization 的收益取决于 reward-model 的 user/query-level calibration，候选数本身不是可兑现的 scaling law。

<!-- review:SF-2026-ARXIV-2605-10991:start -->
#### Test-Time Personalization: A Diagnostic Framework and Probabilistic Fix for Scaling Failures

问题、旧路径与约束变化：Best-of-N personalization 的收益取决于 reward-model 的 user/query-level calibration，候选数本身不是可兑现的 scaling law。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§2 preliminaries and §3–§5 diagnostic/scaling law。canonical owner=`INFER-SCHEDULING`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§6 Experiments。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§8 Discussion/Conclusion 与 Appendices B/D；无独立 Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-10991:start -->exact-v1 支持：Best-of-N personalization 的收益取决于 reward-model 的 user/query-level calibration，候选数本身不是可兑现的 scaling law。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-10991:end -->

Books Decision=`No Change — Existing Coverage`；作者只形成命题比较与 root serial queue，不直接修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-10991:end -->

**Books 对读：** `INFER-SCHEDULING` → `books/part-05-inference-system/56-inference-scheduling.md` 的“当前 Confidence 不等于继续计算的 Residual Value”。`books/part-05-inference-system/56-inference-scheduling.md` 的“当前 Confidence 不等于继续计算的 Residual Value”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：Best-of-N personalization 的收益取决于 reward-model 的 user/query-level calibration，候选数本身不是可兑现的 scaling law。 判定：**No Change — Existing Coverage**。

### [ECHO: Continuous Hierarchical Memory for Vision-Language-Action Models](https://arxiv.org/html/2605.10993v1)

**准入：** VLA 长任务记忆需要层次化 semantic tree、top-down retrieval 与 background consolidation，而不只是线性历史 buffer

<!-- review:SF-2026-ARXIV-2605-10993:start -->
#### ECHO: Continuous Hierarchical Memory for Vision-Language-Action Models

问题与演进：VLA 长任务记忆需要层次化 semantic tree、top-down retrieval 与 background consolidation，而不只是线性历史 buffer。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.10993v1 §3 ECHO — mechanism: Inspired by the hierarchical organization of human experience, we propose ECHO (Experience Consolidation and Hierarchical Organization), a novel memory framework operating within a Continuous Hierarchical Space.`。

Evaluation：`https://arxiv.org/html/2605.10993v1 §4 Experiments — disclosed scope: Evaluations on LIBERO and preliminary real-world experiments demonstrate the effectiveness of our approach, notably achieving a 12.8% absolute improvement in execution success rate over the $π_0$ baseline on LIBERO-Long, while improving compositional generalization on cross-suite unseen long-horizon tasks.`。

Non-proof / fallback：`https://arxiv.org/html/2605.10993v1 Appendix G Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.10993v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-10993:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-10993:end -->
<!-- review:SF-2026-ARXIV-2605-10993:end -->

**Books 对读：** `MULTIMODAL-EMBODIED-VLA` → `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的“Policy 内部的 Latent Memory 是 Episode State，不是 Agent Memory”。books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md 的‘Policy 内部的 Latent Memory 是 Episode State，不是 Agent Memory’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：VLA 长任务记忆需要层次化 semantic tree、top-down retrieval 与 background consolidation，而不只是线性历史 buffer 判定：**No Change — Existing Coverage**。

### [Few-Shot Truly Benign DPO Attack for Jailbreaking LLMs](https://arxiv.org/html/2605.10998v1)

**准入：** benign-looking DPO data 能在分布外压低 refusal，因此 preference-data admission 必须把 safety redistribution 当成发布风险。

<!-- review:SF-2026-ARXIV-2605-10998:start -->
#### Few-Shot Truly Benign DPO Attack for Jailbreaking LLMs

问题、旧路径与约束变化：benign-looking DPO data 能在分布外压低 refusal，因此 preference-data admission 必须把 safety redistribution 当成发布风险。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§2 Threat model and §4 attack。canonical owner=`PLATFORM-SECURITY`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§5 Experiments and §6 Analysis。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§7 Discussion and Appendix G Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-10998:start -->exact-v1 支持：benign-looking DPO data 能在分布外压低 refusal，因此 preference-data admission 必须把 safety redistribution 当成发布风险。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-10998:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-10998:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“Capability Access Control 可以前移到训练状态”。`books/part-06-ai-infrastructure/72-security.md` 的“Capability Access Control 可以前移到训练状态”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：benign-looking DPO data 能在分布外压低 refusal，因此 preference-data admission 必须把 safety redistribution 当成发布风险。 判定：**Integrate — Applied; independent post-write review pending**。

### [SkillGen: Verified Inference-Time Agent Skill Synthesis](https://arxiv.org/html/2605.10999v1)

**准入：** inference-time skill synthesis 必须比较同一实例有/无 skill 的 repairs 与 regressions，生成 artifact 只是 proposal 而非 admission

<!-- review:SF-2026-ARXIV-2605-10999:start -->
#### SkillGen: Verified Inference-Time Agent Skill Synthesis

问题与演进：inference-time skill synthesis 必须比较同一实例有/无 skill 的 repairs 与 regressions，生成 artifact 只是 proposal 而非 admission。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.10999v1 §3 SkillGen — mechanism: We introduce SkillGen, a multi-agent framework that synthesizes a single auditable skill from trajectories generated by a base agent.`。

Evaluation：`https://arxiv.org/html/2605.10999v1 §4 Evaluation — disclosed scope: Skills are a promising way to improve LLM agent capabilities without retraining, while keeping the added procedure reusable and controllable. However, high-quality skills are still largely written by hand. We introduce SkillGen, a multi-agent framework that synthesizes a single auditable skill from trajectories generated by a…`。

Non-proof / fallback：`https://arxiv.org/html/2605.10999v1 §5 Conclusion; no dedicated limitations section — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.10999v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-10999:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-10999:end -->
<!-- review:SF-2026-ARXIV-2605-10999:end -->

**Books 对读：** `AGENT-PLATFORM` → `books/part-07-agent/84-agent-platform.md` 的“从 Trajectory 到 Skill 是一次受治理的 Compilation”。books/part-07-agent/84-agent-platform.md 的‘从 Trajectory 到 Skill 是一次受治理的 Compilation’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：inference-time skill synthesis 必须比较同一实例有/无 skill 的 repairs 与 regressions，生成 artifact 只是 proposal 而非 admission 判定：**No Change — Existing Coverage**。

### [MT-JailBench: A Modular Benchmark for Understanding Multi-Turn Jailbreak Attacks](https://arxiv.org/html/2605.11002v1)

**准入：** 多轮 jailbreak benchmark 必须冻结 turn/retry/interaction/strategy/judge budget，并把 strategy、prompt generation、refinement 与 flow control 拆成可重组模块

<!-- review:SF-2026-ARXIV-2605-11002:start -->
#### MT-JailBench: A Modular Benchmark for Understanding Multi-Turn Jailbreak Attacks

问题与演进：多轮 jailbreak benchmark 必须冻结 turn/retry/interaction/strategy/judge budget，并把 strategy、prompt generation、refinement 与 flow control 拆成可重组模块。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.11002v1 §3 MT-JailBench Modular Framework — mechanism: We introduce MT-JailBench, a modular evaluation framework for benchmarking multi-turn jailbreaks under fixed conditions.`。

Evaluation：`https://arxiv.org/html/2605.11002v1 §4 Experiments and Component Ablations — disclosed scope: Recent methods demonstrate this risk, but they are usually evaluated as black-box pipelines with different budgets, judges, retry rules, and strategy generation procedures.`。

Non-proof / fallback：`https://arxiv.org/html/2605.11002v1 §5 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.11002v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-11002:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-11002:end -->
<!-- review:SF-2026-ARXIV-2605-11002:end -->

**Books 对读：** `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md` 的“Evidence Chain 与在线干预”。books/part-06-ai-infrastructure/66-evaluation-system.md 的‘Evidence Chain 与在线干预’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：多轮 jailbreak benchmark 必须冻结 turn/retry/interaction/strategy/judge budget，并把 strategy、prompt generation、refinement 与 flow control 拆成可重组模块 判定：**Integrate — Already present in current Books**。

### [The Authorization-Execution Gap Is a Major Safety and Security Problem in Open-World Agents](https://arxiv.org/html/2605.11003v1)

**准入：** This position paper argues that the Authorization-Execution Gap (AEG) is a major safety and security problem in open-world agents.

<!-- review:SF-THE-AUTHORIZATION-EXECUTION-GAP-IS-A-MAJOR-SAFETY-AND-SECURITY-PROBLEM-I:start -->
#### The Authorization-Execution Gap Is a Major Safety and Security Problem in Open-World Agents

问题与机制：This position paper argues that the Authorization-Execution Gap (AEG) is a major safety and security problem in open-world agents.。状态 owner=`AGENT-TOOL-CALLING`；机制改变的是该 owner 下的条件化 state/data/control 或 evaluation contract，而不是把论文名称当作长期结论。
Method locator：`arXiv:2605.11003v1 — §2 authorization-execution gap taxonomy — mechanism: This position paper argues that the Authorization-Execution Gap (AEG) is a major safety and security problem in open-world agents.`；evaluation locator：`arXiv:2605.11003v1 — §Evaluation / Experiments — position-paper case synthesis and proposed process evidence — disclosed evaluation scope only`；counterevidence/limitations：`arXiv:2605.11003v1 — §Limitations / Counterevidence — position-paper boundary: no implemented enforcement or comparative evaluation — non-proof boundary retained`；artifact：`arXiv:2605.11003v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-THE-AUTHORIZATION-EXECUTION-GAP-IS-A-MAJOR-SAFETY-AND-SECURITY-PROBLEM-I:start -->证据只支持 exact-v1 披露的模型、数据、硬件、精度、长度、batch、并发、SLO 与 evaluator；未披露字段均为 Not Disclosed，作者 benchmark 不外推为通用结论。<!-- claim:SF-THE-AUTHORIZATION-EXECUTION-GAP-IS-A-MAJOR-SAFETY-AND-SECURITY-PROBLEM-I:end -->
旧方案在固定 workload、较低规模/风险或无需新增状态 owner 时仍成立；新机制获得更强控制或可观测性，同时引入分类器/控制器误差、额外状态、迁移成本或新的攻击面，需由 owner chapter 保留 fallback 与 coexistence。
<!-- review:SF-THE-AUTHORIZATION-EXECUTION-GAP-IS-A-MAJOR-SAFETY-AND-SECURITY-PROBLEM-I:end -->

**Books 对读：** `AGENT-TOOL-CALLING` → `books/part-07-agent/78-tool-calling.md` 的“模型输出只是 Proposal”。books/part-07-agent/78-tool-calling.md 的‘模型输出只是 Proposal’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：This position paper argues that the Authorization-Execution Gap (AEG) is a major safety and security problem in open-world agents. 判定：**No Change — Existing Coverage**。

### [DisagMoE: Computation-Communication overlapped MoE Training via Disaggregated AF-Pipe Parallelism](https://arxiv.org/html/2605.11005v1)

**准入：** We present DisagMoE, a disaggregated MoE training system that jointly optimizes model placement and scheduling for maximal efficiency.

<!-- review:SF-DISAGMOE-COMPUTATION-COMMUNICATION-OVERLAPPED-MOE-TRAINING-VIA-DISAGGREG:start -->
#### DisagMoE: Computation-Communication overlapped MoE Training via Disaggregated AF-Pipe Parallelism

问题与机制：We present DisagMoE, a disaggregated MoE training system that jointly optimizes model placement and scheduling for maximal efficiency.。状态 owner=`TRAIN-PIPELINE-PARALLEL`；机制改变的是该 owner 下的条件化 state/data/control 或 evaluation contract，而不是把论文名称当作长期结论。
Method locator：`arXiv:2605.11005v1 — §3 disaggregated attention/FFN placement and AF-Pipe — mechanism: We present DisagMoE, a disaggregated MoE training system that jointly optimizes model placement and scheduling for maximal efficiency.`；evaluation locator：`arXiv:2605.11005v1 — §4 16-node H800 evaluation — disclosed evaluation scope only`；counterevidence/limitations：`arXiv:2605.11005v1 — §Limitations / Counterevidence — limitations: topology, MoE family, balance model and failure recovery — non-proof boundary retained`；artifact：`arXiv:2605.11005v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-DISAGMOE-COMPUTATION-COMMUNICATION-OVERLAPPED-MOE-TRAINING-VIA-DISAGGREG:start -->证据只支持 exact-v1 披露的模型、数据、硬件、精度、长度、batch、并发、SLO 与 evaluator；未披露字段均为 Not Disclosed，作者 benchmark 不外推为通用结论。<!-- claim:SF-DISAGMOE-COMPUTATION-COMMUNICATION-OVERLAPPED-MOE-TRAINING-VIA-DISAGGREG:end -->
旧方案在固定 workload、较低规模/风险或无需新增状态 owner 时仍成立；新机制获得更强控制或可观测性，同时引入分类器/控制器误差、额外状态、迁移成本或新的攻击面，需由 owner chapter 保留 fallback 与 coexistence。
<!-- review:SF-DISAGMOE-COMPUTATION-COMMUNICATION-OVERLAPPED-MOE-TRAINING-VIA-DISAGGREG:end -->

**Books 对读：** `TRAIN-PIPELINE-PARALLEL` → `books/part-04-training-system/38-pipeline-parallel.md` 的“异步 Pipeline：去掉 Bubble 会把成本移到参数版本”。books/part-04-training-system/38-pipeline-parallel.md 的‘异步 Pipeline：去掉 Bubble 会把成本移到参数版本’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We present DisagMoE, a disaggregated MoE training system that jointly optimizes model placement and scheduling for maximal efficiency. 判定：**No Change — Existing Coverage**。

### [LoopUS: Recasting Pretrained LLMs into Looped Latent Refinement Models](https://arxiv.org/html/2605.11011v1)

**准入：** latent recurrent refinement 可在不增加参数深度时增加执行深度，但收敛与停止策略成为新的运行状态。

<!-- review:SF-2026-ARXIV-2605-11011:start -->
#### LoopUS: Recasting Pretrained LLMs into Looped Latent Refinement Models

问题、旧路径与约束变化：latent recurrent refinement 可在不增加参数深度时增加执行深度，但收敛与停止策略成为新的运行状态。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§3 Method。canonical owner=`MODEL-TRANSFORMER-LAYER`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§4 Empirical evaluation。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：Appendix F Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11011:start -->exact-v1 支持：latent recurrent refinement 可在不增加参数深度时增加执行深度，但收敛与停止策略成为新的运行状态。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11011:end -->

Books Decision=`No Change — Existing Coverage`；作者只形成命题比较与 root serial queue，不直接修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11011:end -->

**Books 对读：** `MODEL-TRANSFORMER-LAYER` → `books/part-02-model/17-transformer-layer.md` 的“Parameter Depth 与 Execution Depth 可以分离”。`books/part-02-model/17-transformer-layer.md` 的“Parameter Depth 与 Execution Depth 可以分离”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：latent recurrent refinement 可在不增加参数深度时增加执行深度，但收敛与停止策略成为新的运行状态。 判定：**No Change — Existing Coverage**。

### [AgentShield: Deception-based Compromise Detection for Tool-using LLM Agents](https://arxiv.org/html/2605.11026v1)

**准入：** Defenses against indirect prompt injection (IPI) in tool-using LLM agents share two structural weaknesses.

<!-- review:SF-AGENTSHIELD-DECEPTION-BASED-COMPROMISE-DETECTION-FOR-TOOL-USING-LLM-AGEN:start -->
#### AgentShield: Deception-based Compromise Detection for Tool-using LLM Agents

问题与机制：Defenses against indirect prompt injection (IPI) in tool-using LLM agents share two structural weaknesses.。状态 owner=`PLATFORM-SECURITY`；机制改变的是该 owner 下的条件化 state/data/control 或 evaluation contract，而不是把论文名称当作长期结论。
Method locator：`arXiv:2605.11026v1 — §3 fake-tool/credential/parameter traps and classifier — mechanism: Defenses against indirect prompt injection (IPI) in tool-using LLM agents share two structural weaknesses.`；evaluation locator：`arXiv:2605.11026v1 — §4 cross-lingual/adaptive-attack evaluation — disclosed evaluation scope only`；counterevidence/limitations：`arXiv:2605.11026v1 — §Limitations / Counterevidence — limitations: low base attack success, trap discoverability and normal-use coverage — non-proof boundary retained`；artifact：`arXiv:2605.11026v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-AGENTSHIELD-DECEPTION-BASED-COMPROMISE-DETECTION-FOR-TOOL-USING-LLM-AGEN:start -->证据只支持 exact-v1 披露的模型、数据、硬件、精度、长度、batch、并发、SLO 与 evaluator；未披露字段均为 Not Disclosed，作者 benchmark 不外推为通用结论。<!-- claim:SF-AGENTSHIELD-DECEPTION-BASED-COMPROMISE-DETECTION-FOR-TOOL-USING-LLM-AGEN:end -->
旧方案在固定 workload、较低规模/风险或无需新增状态 owner 时仍成立；新机制获得更强控制或可观测性，同时引入分类器/控制器误差、额外状态、迁移成本或新的攻击面，需由 owner chapter 保留 fallback 与 coexistence。
<!-- review:SF-AGENTSHIELD-DECEPTION-BASED-COMPROMISE-DETECTION-FOR-TOOL-USING-LLM-AGEN:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“从资产与信任边界开始”。books/part-06-ai-infrastructure/72-security.md 的‘从资产与信任边界开始’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：Defenses against indirect prompt injection (IPI) in tool-using LLM agents share two structural weaknesses. 判定：**No Change — Existing Coverage**。

### [FragBench: Cross-Session Attacks Hidden in Benign-Looking Fragments](https://arxiv.org/html/2605.11029v1)

**准入：** We build FragBench, a benchmark drawn from 24 real-world cyber-incident campaigns, which keeps the full attack trail: the multi-fragment kill chain, the per-fragment safety-judge verdicts, sandboxed execution traces, and a matched set of benign cover sessions.

<!-- review:SF-FRAGBENCH-CROSS-SESSION-ATTACKS-HIDDEN-IN-BENIGN-LOOKING-FRAGMENTS:start -->
#### FragBench: Cross-Session Attacks Hidden in Benign-Looking Fragments

问题与机制：We build FragBench, a benchmark drawn from 24 real-world cyber-incident campaigns, which keeps the full attack trail: the multi-fragment kill chain, the per-fragment safety-judge verdicts, sandboxed execution traces, and a matched set of benign cover sessions.。状态 owner=`PLATFORM-SECURITY`；机制改变的是该 owner 下的条件化 state/data/control 或 evaluation contract，而不是把论文名称当作长期结论。
Method locator：`arXiv:2605.11029v1 — §3 fragmented campaign graph; §4 generator; §5 detector — mechanism: We build FragBench, a benchmark drawn from 24 real-world cyber-incident campaigns, which keeps the full attack trail: the multi-fragment kill chain, the per-fragment safety-judge verdicts, sandboxed execution traces, and a matched set of benign cover sessions.`；evaluation locator：`arXiv:2605.11029v1 — §6 sandbox execution and held-out detection — disclosed evaluation scope only`；counterevidence/limitations：`arXiv:2605.11029v1 — §6.3 synthetic-benign and gated-prompt limitations — non-proof boundary retained`；artifact：`arXiv:2605.11029v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-FRAGBENCH-CROSS-SESSION-ATTACKS-HIDDEN-IN-BENIGN-LOOKING-FRAGMENTS:start -->证据只支持 exact-v1 披露的模型、数据、硬件、精度、长度、batch、并发、SLO 与 evaluator；未披露字段均为 Not Disclosed，作者 benchmark 不外推为通用结论。<!-- claim:SF-FRAGBENCH-CROSS-SESSION-ATTACKS-HIDDEN-IN-BENIGN-LOOKING-FRAGMENTS:end -->
旧方案在固定 workload、较低规模/风险或无需新增状态 owner 时仍成立；新机制获得更强控制或可观测性，同时引入分类器/控制器误差、额外状态、迁移成本或新的攻击面，需由 owner chapter 保留 fallback 与 coexistence。
<!-- review:SF-FRAGBENCH-CROSS-SESSION-ATTACKS-HIDDEN-IN-BENIGN-LOOKING-FRAGMENTS:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“跨会话分解会绕过 Prompt-local Guard”。正文同时要求跨会话 dormant payload 在每次读取/执行前重新 admission，并把 Safety Evaluation 单位定义为 Run、绑定 Tool Trace 与 deterministic predicate；这直接覆盖完整 fragment chain、benign cover session 与 sandbox trace 的证据单位。 新证据增量：We build FragBench, a benchmark drawn from 24 real-world cyber-incident campaigns, which keeps the full attack trail: the multi-fragment kill chain, the per-fragment safety-judge verdicts, sandboxed execution traces, and a matched set of benign cover sessions. 判定：**No Change — Existing Coverage**。

### [Portable Agent Memory: A Protocol for Cryptographically-Verified Memory Transfer Across Heterogeneous AI Agents](https://arxiv.org/html/2605.11032v1)

**准入：** We present Portable Agent Memory, an open protocol and reference implementation for transferring persistent memory state across heterogeneous AI agents.

<!-- review:SF-PORTABLE-AGENT-MEMORY-A-PROTOCOL-FOR-CRYPTOGRAPHICALLY-VERIFIED-MEMORY-T:start -->
#### Portable Agent Memory: A Protocol for Cryptographically-Verified Memory Transfer Across Heterogeneous AI Agents

问题与机制：We present Portable Agent Memory, an open protocol and reference implementation for transferring persistent memory state across heterogeneous AI agents.。状态 owner=`AGENT-MEMORY`；机制改变的是该 owner 下的条件化 state/data/control 或 evaluation contract，而不是把论文名称当作长期结论。
Method locator：`arXiv:2605.11032v1 — §3 memory schema/Merkle-DAG/capability access/rehydration — mechanism: We present Portable Agent Memory, an open protocol and reference implementation for transferring persistent memory state across heterogeneous AI agents.`；evaluation locator：`arXiv:2605.11032v1 — §4 implementation; §5 evaluation — disclosed evaluation scope only`；counterevidence/limitations：`arXiv:2605.11032v1 — §6.1 limitations: ranking, extractive summary and N=50 scale — non-proof boundary retained`；artifact：`arXiv:2605.11032v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-PORTABLE-AGENT-MEMORY-A-PROTOCOL-FOR-CRYPTOGRAPHICALLY-VERIFIED-MEMORY-T:start -->证据只支持 exact-v1 披露的模型、数据、硬件、精度、长度、batch、并发、SLO 与 evaluator；未披露字段均为 Not Disclosed，作者 benchmark 不外推为通用结论。<!-- claim:SF-PORTABLE-AGENT-MEMORY-A-PROTOCOL-FOR-CRYPTOGRAPHICALLY-VERIFIED-MEMORY-T:end -->
旧方案在固定 workload、较低规模/风险或无需新增状态 owner 时仍成立；新机制获得更强控制或可观测性，同时引入分类器/控制器误差、额外状态、迁移成本或新的攻击面，需由 owner chapter 保留 fallback 与 coexistence。
<!-- review:SF-PORTABLE-AGENT-MEMORY-A-PROTOCOL-FOR-CRYPTOGRAPHICALLY-VERIFIED-MEMORY-T:end -->

**Books 对读：** `AGENT-MEMORY` → `books/part-07-agent/77-memory.md` 的“Memory Write 是高风险决策”。books/part-07-agent/77-memory.md 的‘Memory Write 是高风险决策’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We present Portable Agent Memory, an open protocol and reference implementation for transferring persistent memory state across heterogeneous AI agents. 判定：**No Change — Existing Coverage**。

### [Sequential Behavioral Watermarking for LLM Agents](https://arxiv.org/html/2605.11036v1)

**准入：** sequential behavioral watermark 把 Agent 多步行为与挑战序列绑定，身份判断从单次文本迁移到有状态轨迹。

<!-- review:SF-2026-ARXIV-2605-11036:start -->
#### Sequential Behavioral Watermarking for LLM Agents

问题、旧路径与约束变化：sequential behavioral watermark 把 Agent 多步行为与挑战序列绑定，身份判断从单次文本迁移到有状态轨迹。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§4 Method。canonical owner=`PLATFORM-SECURITY`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§5 Experiments。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：Appendix A Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11036:start -->exact-v1 支持：sequential behavioral watermark 把 Agent 多步行为与挑战序列绑定，身份判断从单次文本迁移到有状态轨迹。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11036:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-11036:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“Behavioral Contract 把 Invariant、Drift 与 Recovery 变成运行期状态”。`books/part-06-ai-infrastructure/72-security.md` 的“Behavioral Contract 把 Invariant、Drift 与 Recovery 变成运行期状态”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：sequential behavioral watermark 把 Agent 多步行为与挑战序列绑定，身份判断从单次文本迁移到有状态轨迹。 判定：**Integrate — Applied; independent post-write review pending**。

### [The Granularity Mismatch in Agent Security: Argument-Level Provenance Solves Enforcement and Isolates the LLM Reasoning Bottleneck](https://arxiv.org/html/2605.11039v1)

**准入：** We present \textsc{PACT} (\emph{Provenance-Aware Capability Contracts}), a runtime monitor that assigns semantic roles to tool arguments, tracks value provenance across replanning steps, and checks whether each argument's origin satisfies its role-specific trust contract.

<!-- review:SF-2026-ARXIV-2605-11039:start -->
#### The Granularity Mismatch in Agent Security: Argument-Level Provenance Solves Enforcement and Isolates the LLM Reasoning Bottleneck

Review provenance 由本节边界正文与 Completion Receipt 共同绑定；owner=`PLATFORM-SECURITY`。
Method / identity：arXiv:2605.11039v1 §3 Pact: argument-level contracts, provenance, runtime checking and formal properties — We present \textsc{PACT} (\emph{Provenance-Aware Capability Contracts}), a runtime monitor that assigns semantic roles to tool arguments, tracks value provenance across replanning steps, and checks whether each argument's origin satisfies its role-specific trust contract.。
Evaluation：arXiv:2605.11039v1 §4 Experiments (§4.1–§4.4), including mechanism ablations and stress boundaries。
Counterevidence / limitations：arXiv:2605.11039v1 §3.1 Threat Model and Scope; §4.4 Practicality, Stress Tests and Boundaries。
Artifact：Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body。

<!-- claim:SF-2026-ARXIV-2605-11039:start -->The exact-v1 body supports the mechanism under §4 Experiments (§4.1–§4.4), including mechanism ablations and stress boundaries. Counterevidence/scope was checked at §3.1 Threat Model and Scope; §4.4 Practicality, Stress Tests and Boundaries. It does not prove that “The Granularity Mismatch in Agent Security: Argument-Level Provenance Solves Enforcement and Isolates the LLM Reasoning Bottleneck” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.<!-- claim:SF-2026-ARXIV-2605-11039:end -->

Disposition=`No Change — Existing Coverage`；该结论来自独立 exact-v1 与 current owner+adjacent comparison，不由 validator 代签。
<!-- review:SF-2026-ARXIV-2605-11039:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“Canonical Action 与 Effect-time Authorization”。books/part-06-ai-infrastructure/72-security.md 的‘Canonical Action 与 Effect-time Authorization’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We present \textsc{PACT} (\emph{Provenance-Aware Capability Contracts}), a runtime monitor that assigns semantic roles to tool arguments, tracks value provenance across replanning steps, and checks whether each argument's origin satisfies its role-specific trust contract. 判定：**No Change — Existing Coverage**。

### [On Problems of Implicit Context Compression for Software Engineering Agents](https://arxiv.org/html/2605.11051v1)

**准入：** implicit context compression 在 single-shot 可成立却在 multi-step Agent 失败，给出压缩适用性的负面边界。

<!-- review:SF-2026-ARXIV-2605-11051:start -->
#### On Problems of Implicit Context Compression for Software Engineering Agents

问题、旧路径与约束变化：implicit context compression 在 single-shot 可成立却在 multi-step Agent 失败，给出压缩适用性的负面边界。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§2 Method。canonical owner=`AGENT-CONTEXT`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§3 Experiments。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§4 Discussion and §5 Conclusion；无独立 Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11051:start -->exact-v1 支持：implicit context compression 在 single-shot 可成立却在 multi-step Agent 失败，给出压缩适用性的负面边界。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11051:end -->

Books Decision=`No Change — Existing Coverage`；作者只形成命题比较与 root serial queue，不直接修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11051:end -->

**Books 对读：** `AGENT-CONTEXT` → `books/part-07-agent/75-context.md` 的“Context Compression 必须保留执行状态，而不只是语义”。`books/part-07-agent/75-context.md` 的“Context Compression 必须保留执行状态，而不只是语义”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：implicit context compression 在 single-shot 可成立却在 multi-step Agent 失败，给出压缩适用性的负面边界。 判定：**No Change — Existing Coverage**。

### [HiDream-O1-Image: A Natively Unified Image Generative Foundation Model with Pixel-level Unified Transformer](https://arxiv.org/html/2605.11061v1)

**准入：** 统一 pixel-space 生成把理解与生成的表示、训练数据和 decoder 责任放入同一 native multimodal contract。

<!-- review:SF-2026-ARXIV-2605-11061:start -->
#### HiDream-O1-Image: A Natively Unified Image Generative Foundation Model with Pixel-level Unified Transformer

问题、旧路径与约束变化：统一 pixel-space 生成把理解与生成的表示、训练数据和 decoder 责任放入同一 native multimodal contract。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§2 Data, §3 Model, §4 Training and §5 Distillation。canonical owner=`MULTIMODAL-REPRESENTATION`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§6–§8 Evaluation。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§9 Conclusion；无独立 Limitations，跨模型与生产条件不得外推。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11061:start -->exact-v1 支持：统一 pixel-space 生成把理解与生成的表示、训练数据和 decoder 责任放入同一 native multimodal contract。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11061:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-11061:end -->

**Books 对读：** `MULTIMODAL-REPRESENTATION` → `books/part-03-multimodal-world-models/23-multimodal-representation.md` 的“阶段四：native multimodal representation”。`books/part-03-multimodal-world-models/23-multimodal-representation.md` 的“阶段四：native multimodal representation”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：统一 pixel-space 生成把理解与生成的表示、训练数据和 decoder 责任放入同一 native multimodal contract。 判定：**Integrate — Applied; independent post-write review pending**。

### [Enabling Performant and Flexible Model-Internal Observability for LLM Inference](https://arxiv.org/html/2605.11093v1)

**准入：** We present DMI-Lib, a high-speed deep model inspector that treats internal observability as a first-class systems primitive, decoupling it from the inference hot path via an asynchronous observability substrate built from Ring^2, a GPU-CPU memory abstraction for capturing and staging tensors, and a policy-controlled…

<!-- review:SF-2026-ARXIV-2605-11093:start -->
#### Enabling Performant and Flexible Model-Internal Observability for LLM Inference

Review provenance 由本节边界正文与 Completion Receipt 共同绑定；owner=`PLATFORM-MONITORING`。
Method / identity：arXiv:2605.11093v1 §3 Challenges; §4 DMI-Lib design (HookPoint, Ring2, exporter, policies and distributed operation); §5 Implementation — We present DMI-Lib, a high-speed deep model inspector that treats internal observability as a first-class systems primitive, decoupling it from the inference hot path via an asynchronous observability substrate built from Ring^2, a GPU-CPU memory abstraction for capturing and staging tensors, and a policy-controlled…。
Evaluation：arXiv:2605.11093v1 §6 Evaluation; §7 Use Cases。
Counterevidence / limitations：arXiv:2605.11093v1 No dedicated limitations section; model/runtime integrations and probes disclosed in §6–§7 bound overhead and coverage。
Artifact：Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body。

<!-- claim:SF-2026-ARXIV-2605-11093:start -->The exact-v1 body supports the mechanism under §6 Evaluation; §7 Use Cases. Counterevidence/scope was checked at No dedicated limitations section; model/runtime integrations and probes disclosed in §6–§7 bound overhead and coverage. It does not prove that “Enabling Performant and Flexible Model-Internal Observability for LLM Inference” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.<!-- claim:SF-2026-ARXIV-2605-11093:end -->

Disposition=`Integrate`；该结论来自独立 exact-v1 与 current owner+adjacent comparison，不由 validator 代签。
<!-- review:SF-2026-ARXIV-2605-11093:end -->

**Books 对读：** `PLATFORM-MONITORING` → `books/part-06-ai-infrastructure/67-monitoring.md` 的“Model-internal Sensor 必须从 Inference Hot Path 解耦”。books/part-06-ai-infrastructure/67-monitoring.md 的‘Model-internal Sensor 必须从 Inference Hot Path 解耦’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We present DMI-Lib, a high-speed deep model inspector that treats internal observability as a first-class systems primitive, decoupling it from the inference hot path via an asynchronous observability substrate built from Ring^2, a GPU-CPU memory abstraction for capturing and staging tensors, and a policy-controlled… 判定：**Integrate — Already present in current Books**。

### [SEVO: Semantic-Enhanced Virtual Observation for Robust VLA Manipulation via Active Illumination and Data-Centric Collection](https://arxiv.org/html/2605.11114v1)

**准入：** VLA 的 observation design 与 data diversity 共同决定 action policy 可见状态，更多数据不能替代观测接口。

<!-- review:SF-2026-ARXIV-2605-11114:start -->
#### SEVO: Semantic-Enhanced Virtual Observation for Robust VLA Manipulation via Active Illumination and Data-Centric Collection

问题、旧路径与约束变化：VLA 的 observation design 与 data diversity 共同决定 action policy 可见状态，更多数据不能替代观测接口。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§IV Method and §V Data。canonical owner=`MULTIMODAL-EMBODIED-VLA`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§VI Experiments。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§VII Discussion and Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11114:start -->exact-v1 支持：VLA 的 observation design 与 data diversity 共同决定 action policy 可见状态，更多数据不能替代观测接口。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11114:end -->

Books Decision=`No Change — Existing Coverage`；作者只形成命题比较与 root serial queue，不直接修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11114:end -->

**Books 对读：** `MULTIMODAL-EMBODIED-VLA` → `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的“State ownership 与 freshness”。`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的“State ownership 与 freshness”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：VLA 的 observation design 与 data diversity 共同决定 action policy 可见状态，更多数据不能替代观测接口。 判定：**No Change — Existing Coverage**。

### [Sampling More, Getting Less: Calibration is the Diversity Bottleneck in LLMs](https://arxiv.org/html/2605.11128v1)

**准入：** order 与 shape miscalibration 会把局部 token 选择误差复合为 sequence-level diversity collapse，需联合验收局部与整体分布。

<!-- review:SF-2026-ARXIV-2605-11128:start -->
#### Sampling More, Getting Less: Calibration is the Diversity Bottleneck in LLMs

问题、旧路径与约束变化：order 与 shape miscalibration 会把局部 token 选择误差复合为 sequence-level diversity collapse，需联合验收局部与整体分布。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§4 order mechanism and §5 shape mechanism。canonical owner=`MODEL-SAMPLING`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：Appendices B/C/G/H/I evaluations and ablations。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：Appendix J Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11128:start -->exact-v1 支持：order 与 shape miscalibration 会把局部 token 选择误差复合为 sequence-level diversity collapse，需联合验收局部与整体分布。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11128:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-11128:end -->

**Books 对读：** `MODEL-SAMPLING` → `books/part-02-model/20-sampling.md` 的“Sampling 为什么会影响长程行为”。`books/part-02-model/20-sampling.md` 的“Sampling 为什么会影响长程行为”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：order 与 shape miscalibration 会把局部 token 选择误差复合为 sequence-level diversity collapse，需联合验收局部与整体分布。 判定：**Integrate — Applied; independent post-write review pending**。

### [CATS: Cascaded Adaptive Tree Speculation for Memory-Limited LLM Inference Acceleration](https://arxiv.org/html/2605.11186v1)

**准入：** memory-constrained speculative inference 必须联合选择 draft/verify 长度与状态驻留，不能只最大化 acceptance。

<!-- review:SF-2026-ARXIV-2605-11186:start -->
#### CATS: Cascaded Adaptive Tree Speculation for Memory-Limited LLM Inference Acceleration

问题、旧路径与约束变化：memory-constrained speculative inference 必须联合选择 draft/verify 长度与状态驻留，不能只最大化 acceptance。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§4 Methodology。canonical owner=`INFER-SPECULATIVE-DECODING`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§5 Experiments。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§6 Conclusion and Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11186:start -->exact-v1 支持：memory-constrained speculative inference 必须联合选择 draft/verify 长度与状态驻留，不能只最大化 acceptance。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11186:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-11186:end -->

**Books 对读：** `INFER-SPECULATIVE-DECODING` → `books/part-05-inference-system/48-speculative-decoding.md` 的“Verify Length 不是孤立的固定超参数”。`books/part-05-inference-system/48-speculative-decoding.md` 的“Verify Length 不是孤立的固定超参数”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：memory-constrained speculative inference 必须联合选择 draft/verify 长度与状态驻留，不能只最大化 acceptance。 判定：**Integrate — Applied; independent post-write review pending**。

### [How Does Differential Privacy Affect Social Bias in LLMs? A Systematic Evaluation](https://arxiv.org/html/2605.11195v1)

**准入：** DP 对 logit-level 与 output-level social bias 的影响不一致，说明 privacy claim 与 fairness claim 必须按行为层级分开验收。

<!-- review:SF-2026-ARXIV-2605-11195:start -->
#### How Does Differential Privacy Affect Social Bias in LLMs? A Systematic Evaluation

**问题与旧基线。** DP 对 logit-level 与 output-level social bias 的影响不一致，说明 privacy claim 与 fairness claim 必须按行为层级分开验收。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3 Motivation and Evaluation Framework；§4 Experimental Setup。同一 DP model 在四种 evaluation surface 上产生不同 bias 变化，memorization reduction 不拥有 fairness truth。

**Evaluation contract。** §5；sentence scoring、completion、classification 和 QA 四类范式。V3=2+2+2=6；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** §7 Limitations；单一 pretrained LLM/DP setting 与选定 bias metrics。

**Trade-off / failure / fallback。** 多范式评估增加数据和解释成本；指标冲突时不得聚合成单一安全结论，应保留分层结果和发布限制。

<!-- claim:SF-2026-ARXIV-2605-11195:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11195:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11195:end -->

**Books 对读：** `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md` 的“评估对象有四个层次”。正文约第 424 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：DP 对 logit-level 与 output-level social bias 的影响不一致，说明 privacy claim 与 fairness claim 必须按行为层级分开验收。 判定：**Integrate — Applied; independent post-write review pending**。

### [Variational Linear Attention: Stable Associative Memory for Long-Context Transformers](https://arxiv.org/html/2605.11196v1)

**准入：** variational linear attention 把 associative memory 更新变成受正则化的在线状态，稳定性来自写入规则而非线性复杂度口号。

<!-- review:SF-2026-ARXIV-2605-11196:start -->
#### Variational Linear Attention: Stable Associative Memory for Long-Context Transformers

问题、旧路径与约束变化：variational linear attention 把 associative memory 更新变成受正则化的在线状态，稳定性来自写入规则而非线性复杂度口号。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§3 Method and §4 Theory。canonical owner=`MODEL-LONG-CONTEXT`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§5–§7 Experiments/analysis。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§8 Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11196:start -->exact-v1 支持：variational linear attention 把 associative memory 更新变成受正则化的在线状态，稳定性来自写入规则而非线性复杂度口号。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11196:end -->

Books Decision=`No Change — Existing Coverage`；作者只形成命题比较与 root serial queue，不直接修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11196:end -->

**Books 对读：** `MODEL-LONG-CONTEXT` → `books/part-02-model/22-long-context.md` 的“路线六：让模型在 Test Time 更新内部记忆”。`books/part-02-model/22-long-context.md` 的“路线六：让模型在 Test Time 更新内部记忆”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：variational linear attention 把 associative memory 更新变成受正则化的在线状态，稳定性来自写入规则而非线性复杂度口号。 判定：**No Change — Existing Coverage**。

### [Continuous Discovery of Vulnerabilities in LLM Serving Systems with Fuzzing](https://arxiv.org/html/2605.11202v1)

**准入：** We present GRIEF, a greybox fuzzer for LLM inference engines that treats timed multi-request traces as first-class inputs, uses lightweight oracles to detect crashes, hangs, performance pathologies, and silent output corruption, and applies controlled replay with log-probability checks to confirm reproducible serving-layer failures.

<!-- review:SF-2026-ARXIV-2605-11202:start -->
#### Continuous Discovery of Vulnerabilities in LLM Serving Systems with Fuzzing

Review provenance 由本节边界正文与 Completion Receipt 共同绑定；owner=`INFER-REQUEST-LIFECYCLE`。
Method / identity：arXiv:2605.11202v1 §2 representative failures; §3 GRIEF fuzzing design, trace mutation and confirmation oracle — We present GRIEF, a greybox fuzzer for LLM inference engines that treats timed multi-request traces as first-class inputs, uses lightweight oracles to detect crashes, hangs, performance pathologies, and silent output corruption, and applies controlled replay with log-probability checks to confirm reproducible serving-layer failures.。
Evaluation：arXiv:2605.11202v1 §4 Evaluation, including KV-cache state-corruption impact。
Counterevidence / limitations：Not Disclosed — exact-v1 body was reviewed, but no stable numbered Limitations/Counterevidence fragment was exposed; reviewer boundary: arXiv:2605.11202v1 No dedicated limitations section; tested serving stacks, mutation grammar and confirmation oracle bound discovery completeness。
Artifact：Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body。

<!-- claim:SF-2026-ARXIV-2605-11202:start -->The exact-v1 body supports the mechanism under §4 Evaluation, including KV-cache state-corruption impact. Counterevidence/scope was checked at No dedicated limitations section; tested serving stacks, mutation grammar and confirmation oracle bound discovery completeness. It does not prove that “Continuous Discovery of Vulnerabilities in LLM Serving Systems with Fuzzing” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.<!-- claim:SF-2026-ARXIV-2605-11202:end -->

Disposition=`No Change — Existing Coverage`；该结论来自独立 exact-v1 与 current owner+adjacent comparison，不由 validator 代签。
<!-- review:SF-2026-ARXIV-2605-11202:end -->

**Books 对读：** `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md` 的“Runtime and Service Evaluation”。timed multi-request trace 应成为 inference-engine fuzzing workload artifact；crash/hang/performance 之外还要以 controlled replay 与 log-prob oracle 捕获 silent corruption。 新证据增量：We present GRIEF, a greybox fuzzer for LLM inference engines that treats timed multi-request traces as first-class inputs, uses lightweight oracles to detect crashes, hangs, performance pathologies, and silent output corruption, and applies controlled replay with log-probability checks to confirm reproducible serving-layer failures. 判定：**Integrate — Applied; independent post-write review pending**。

### [The Scaling Law of Evaluation Failure: Why Simple Averaging Collapses Under Data Sparsity and Item Difficulty Gaps, and How Item Response Theory Recovers Ground Truth Across Domains](https://arxiv.org/html/2605.11205v1)

**准入：** Through controlled simulation experiments across four domains -- NLP (GLUE), clinical drug trials, autonomous vehicle safety, and cybersecurity -- we show that Spearman rank correlation $ρ$ between simple-average rankings and ground-truth rankings degrades from $ρ= 1.000$ at 100% coverage to $ρ= 0.809$ at 67%…

<!-- review:SF-2026-ARXIV-2605-11205:start -->
#### The Scaling Law of Evaluation Failure: Why Simple Averaging Collapses Under Data Sparsity and Item Difficulty Gaps, and How Item Response Theory Recovers Ground Truth Across Domains

Review provenance 由本节边界正文与 Completion Receipt 共同绑定；owner=`PLATFORM-EVALUATION-SYSTEM`。
Method / identity：arXiv:2605.11205v1 §3 Methodology: simple averaging and 2PL item-response model — Through controlled simulation experiments across four domains -- NLP (GLUE), clinical drug trials, autonomous vehicle safety, and cybersecurity -- we show that Spearman rank correlation $ρ$ between simple-average rankings and ground-truth rankings degrades from $ρ= 1.000$ at 100% coverage to $ρ= 0.809$ at 67%…。
Evaluation：arXiv:2605.11205v1 §4 Experimental Design across four domains; §5 Results。
Counterevidence / limitations：Not Disclosed — exact-v1 body was reviewed, but no stable numbered Limitations/Counterevidence fragment was exposed; reviewer boundary: arXiv:2605.11205v1 No dedicated limitations section; synthetic sparsity/difficulty regimes and four disclosed domains bound the scaling-law claim。
Artifact：Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body。

<!-- claim:SF-2026-ARXIV-2605-11205:start -->The exact-v1 body supports the mechanism under §4 Experimental Design across four domains; §5 Results. Counterevidence/scope was checked at No dedicated limitations section; synthetic sparsity/difficulty regimes and four disclosed domains bound the scaling-law claim. It does not prove that “The Scaling Law of Evaluation Failure: Why Simple Averaging Collapses Under Data Sparsity and Item Difficulty Gaps, and How Item Response Theory Recovers Ground Truth Across Domains” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.<!-- claim:SF-2026-ARXIV-2605-11205:end -->

Disposition=`No Change — Existing Coverage`；该结论来自独立 exact-v1 与 current owner+adjacent comparison，不由 validator 代签。
<!-- review:SF-2026-ARXIV-2605-11205:end -->

**Books 对读：** `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md` 的“平均值、切片与不确定性”。books/part-06-ai-infrastructure/66-evaluation-system.md 的‘平均值、切片与不确定性’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：Through controlled simulation experiments across four domains -- NLP (GLUE), clinical drug trials, autonomous vehicle safety, and cybersecurity -- we show that Spearman rank correlation $ρ$ between simple-average rankings and ground-truth rankings degrades from $ρ= 1.000$ at 100% coverage to $ρ= 0.809$ at 67%… 判定：**No Change — Existing Coverage**。

### [Measuring Five-Nines Reliability: Sample-Efficient LLM Evaluation in Saturated Benchmarks](https://arxiv.org/html/2605.11209v1)

**准入：** Leveraging this observation, we propose to learn a sampling distribution concentrated on failure-prone inputs via the cross-entropy method (CEM).

<!-- review:SF-2026-ARXIV-2605-11209:start -->
#### Measuring Five-Nines Reliability: Sample-Efficient LLM Evaluation in Saturated Benchmarks

Review provenance 由本节边界正文与 Completion Receipt 共同绑定；owner=`PLATFORM-EVALUATION-SYSTEM`。
Method / identity：arXiv:2605.11209v1 §3 problem/setup; §4 systematic failure concentration; §5 CEM failure-prone sampling — Leveraging this observation, we propose to learn a sampling distribution concentrated on failure-prone inputs via the cross-entropy method (CEM).。
Evaluation：arXiv:2605.11209v1 §6 inference-efficiency experiments。
Counterevidence / limitations：Not Disclosed — exact-v1 body was reviewed, but no stable numbered Limitations/Counterevidence fragment was exposed; reviewer boundary: arXiv:2605.11209v1 Limitations discussion; saturated benchmarks, selected models and failure parameterization bound rare-event estimates。
Artifact：Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body。

<!-- claim:SF-2026-ARXIV-2605-11209:start -->The exact-v1 body supports the mechanism under §6 inference-efficiency experiments. Counterevidence/scope was checked at Limitations discussion; saturated benchmarks, selected models and failure parameterization bound rare-event estimates. It does not prove that “Measuring Five-Nines Reliability: Sample-Efficient LLM Evaluation in Saturated Benchmarks” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.<!-- claim:SF-2026-ARXIV-2605-11209:end -->

Disposition=`No Change — Existing Coverage`；该结论来自独立 exact-v1 与 current owner+adjacent comparison，不由 validator 代签。
<!-- review:SF-2026-ARXIV-2605-11209:end -->

**Books 对读：** `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md` 的“Agent Regression Testing 需要分配 Evidence Budget”。CEM 学习的 failure-prone sampling distribution 是 rare-failure evidence allocator，不是真实 failure rate owner；必须保留 unbiased audit、importance accounting 与 fallback。 新证据增量：Leveraging this observation, we propose to learn a sampling distribution concentrated on failure-prone inputs via the cross-entropy method (CEM). 判定：**Integrate — Applied; independent post-write review pending**。

### [Enforcing Constraints in Generative Sampling via Adaptive Correction Scheduling](https://arxiv.org/html/2605.11214v1)

**准入：** adaptive correction scheduling 根据当前生成状态分配修正步骤，把统一迭代数改为有边界的控制策略。

<!-- review:SF-2026-ARXIV-2605-11214:start -->
#### Enforcing Constraints in Generative Sampling via Adaptive Correction Scheduling

问题、旧路径与约束变化：adaptive correction scheduling 根据当前生成状态分配修正步骤，把统一迭代数改为有边界的控制策略。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§3 Method。canonical owner=`MULTIMODAL-GENERATIVE-PARADIGMS`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§4 Experiments。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§5 Discussion and Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11214:start -->exact-v1 支持：adaptive correction scheduling 根据当前生成状态分配修正步骤，把统一迭代数改为有边界的控制策略。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11214:end -->

Books Decision=`No Change — Existing Coverage`；作者只形成命题比较与 root serial queue，不直接修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11214:end -->

**Books 对读：** `MULTIMODAL-GENERATIVE-PARADIGMS` → `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的“Refinement 位置也可以成为条件计算状态”。`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的“Refinement 位置也可以成为条件计算状态”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：adaptive correction scheduling 根据当前生成状态分配修正步骤，把统一迭代数改为有边界的控制策略。 判定：**No Change — Existing Coverage**。

### [Leveraging RAG for Training-Free Alignment of LLMs](https://arxiv.org/html/2605.11217v1)

**准入：** RAG-Pref 将 preferred/dispreferred retrieval 在推理时变成 alignment actuator，改变 offline weight alignment 与 online refusal guardrail 的分工。

<!-- review:SF-2026-ARXIV-2605-11217:start -->
#### Leveraging RAG for Training-Free Alignment of LLMs

**问题与旧基线。** RAG-Pref 将 preferred/dispreferred retrieval 在推理时变成 alignment actuator，改变 offline weight alignment 与 online refusal guardrail 的分工。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3 Offline and Online Preference Alignment；§3.1 RAG-Pref；§3.2 Contrastive Information。检索器返回正负偏好示例，生成器在当前 query 上消费对比信息；retrieval 只拥有 conditioning proposal，output policy 仍拥有放行权。

**Evaluation contract。** §5、§5.1 与 Appendices C/F/G；五个开放模型、agentic refusal 与一般偏好任务。V3=2+2+2=6；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** §6 讨论范围；无独立 Limitations；作者平均提升不构成未测攻击或生产安全保证。

**Trade-off / failure / fallback。** 省去再训练但增加检索质量、污染、上下文成本与 online drift；检索证据不足时回退离线 alignment、静态 policy 与显式拒答 gate。

<!-- claim:SF-2026-ARXIV-2605-11217:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11217:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11217:end -->

**Books 对读：** `TRAIN-RLHF` → `books/part-04-training-system/31-rlhf.md` 的“从持久权重更新到条件化 Activation Intervention”。正文约第 353 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：RAG-Pref 将 preferred/dispreferred retrieval 在推理时变成 alignment actuator，改变 offline weight alignment 与 online refusal guardrail 的分工。 判定：**Integrate — Applied; independent post-write review pending**。

### [Comment and Control: Hijacking Agentic Workflows via Context-Grounded Evolution](https://arxiv.org/html/2605.11229v1)

**准入：** In this paper, we design the first detection and exploitation framework, called JAW, to hijack agentic workflows hosted on automation platforms via a novel approach called Context-Grounded Evolution.

<!-- review:SF-2026-ARXIV-2605-11229:start -->
#### Comment and Control: Hijacking Agentic Workflows via Context-Grounded Evolution

问题与机制：In this paper, we design the first detection and exploitation framework, called JAW, to hijack agentic workflows hosted on automation platforms via a novel approach called Context-Grounded Evolution.。机制 owner=`PLATFORM-SECURITY`。
Method / identity：arXiv:2605.11229v1 — §2 threat model; §3 path-sensitive workflow analysis and prompt-provenance taint tracking。
Evaluation：arXiv:2605.11229v1 — §5 Evaluation, including §5.1–§5.4。
Counterevidence / limitations：arXiv:2605.11229v1 — §6 Discussion; modeled workflow languages, events and attack sources bound completeness; Appendix A contains artifacts。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-2026-ARXIV-2605-11229:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `PLATFORM-SECURITY` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-2026-ARXIV-2605-11229:end -->

Books Decision=`No Change — Existing Coverage`。当前 Books 已有 binding，不重复追加。
<!-- review:SF-2026-ARXIV-2605-11229:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“局部合理动作会累积成有害轨迹”。books/part-06-ai-infrastructure/72-security.md 的‘局部合理动作会累积成有害轨迹’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：In this paper, we design the first detection and exploitation framework, called JAW, to hijack agentic workflows hosted on automation platforms via a novel approach called Context-Grounded Evolution. 判定：**No Change — Existing Coverage**。

### [Sieve: Dynamic Expert-Aware PIM Acceleration for Evolving Mixture-of-Experts Models](https://arxiv.org/html/2605.11277v1)

**准入：** MoE expert 热度双峰化使静态 PIM placement 失效，Sieve 依据演化的 token-to-expert 分布动态分配执行位置。

<!-- review:SF-2026-ARXIV-2605-11277:start -->
#### Sieve: Dynamic Expert-Aware PIM Acceleration for Evolving Mixture-of-Experts Models

问题、旧路径与约束变化：MoE expert 热度双峰化使静态 PIM placement 失效，Sieve 依据演化的 token-to-expert 分布动态分配执行位置。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§3 Problem and §4–§6 system/scheduler。canonical owner=`INFER-TENSORRT-LLM`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§7 Evaluation。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§9 Conclusion；无独立 Limitations，结论限于受测 PIM/MoE/trace。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11277:start -->exact-v1 支持：MoE expert 热度双峰化使静态 PIM placement 失效，Sieve 依据演化的 token-to-expert 分布动态分配执行位置。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11277:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-11277:end -->

**Books 对读：** `INFER-TENSORRT-LLM` → `books/part-05-inference-system/49-tensorrt-llm.md` 的“MoE Dispatch 应平衡时间，而不是固定代理量”。`books/part-05-inference-system/49-tensorrt-llm.md` 的“MoE Dispatch 应平衡时间，而不是固定代理量”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：MoE expert 热度双峰化使静态 PIM placement 失效，Sieve 依据演化的 token-to-expert 分布动态分配执行位置。 判定：**Integrate — Applied; independent post-write review pending**。

### [LatentRouter: Can We Choose the Right Multimodal Model Before Seeing Its Answer?](https://arxiv.org/html/2605.11301v1)

**准入：** multimodal routing 被表述为 answer 前的 counterfactual utility prediction，使路由器拥有选择 proposal 而非质量真值。

<!-- review:SF-2026-ARXIV-2605-11301:start -->
#### LatentRouter: Can We Choose the Right Multimodal Model Before Seeing Its Answer?

问题、旧路径与约束变化：multimodal routing 被表述为 answer 前的 counterfactual utility prediction，使路由器拥有选择 proposal 而非质量真值。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§2 Method。canonical owner=`INFER-SCHEDULING`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§3–§4 Experiments。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：Appendix E Limitation。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11301:start -->exact-v1 支持：multimodal routing 被表述为 answer 前的 counterfactual utility prediction，使路由器拥有选择 proposal 而非质量真值。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11301:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-11301:end -->

**Books 对读：** `INFER-SCHEDULING` → `books/part-05-inference-system/56-inference-scheduling.md` 的“Calibration 是在线 Routing State”。`books/part-05-inference-system/56-inference-scheduling.md` 的“Calibration 是在线 Routing State”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：multimodal routing 被表述为 answer 前的 counterfactual utility prediction，使路由器拥有选择 proposal 而非质量真值。 判定：**Integrate — Applied; independent post-write review pending**。

### [SOMA: Efficient Multi-turn LLM Serving via Small Language Model](https://arxiv.org/html/2605.11317v1)

**准入：** We propose a framework that exploits the early turns of a session to estimate a local response manifold and then adapt a smaller surrogate model to this local region for the remainder of the conversation.

<!-- review:SF-2026-ARXIV-2605-11317:start -->
#### SOMA: Efficient Multi-turn LLM Serving via Small Language Model

问题与机制：We propose a framework that exploits the early turns of a session to estimate a local response manifold and then adapt a smaller surrogate model to this local region for the remainder of the conversation.。机制 owner=`INFER-REQUEST-LIFECYCLE`。
Method / identity：arXiv:2605.11317v1 — §2 token-turn patterns and local manifold; §3 soft-prompt initialization, tuning, switching and rollback; §4 theory。
Evaluation：arXiv:2605.11317v1 — §5 Empirical Studies, including §5.1 Experimental Results; Appendix F contains further experiments。
Counterevidence / limitations：arXiv:2605.11317v1 — Appendix I Limitations: dialogue distributions, surrogate/target models and rollback policy bound the result。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-2026-ARXIV-2605-11317:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `INFER-REQUEST-LIFECYCLE` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-2026-ARXIV-2605-11317:end -->

Books Decision=`Integrate — Root Writeback Applied`。现有正文没有该机制的真实 binding；author 未修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11317:end -->

**Books 对读：** “请求状态机”只说明普通 request/session lifecycle，未承载由早期 turns 估计 local response manifold、适配小 surrogate、后续切换与回退的机制。判定：**Integrate — Root Writeback Applied**。

### [Rethinking Evaluation for LLM Hallucination Detection: A Desiderata, A New RAG-based Benchmark, New Insights](https://arxiv.org/html/2605.11330v1)

**准入：** hallucination detection benchmark 需要冻结 label noise、RAG context 与长上下文切片，单一 aggregate 不足以签发 detector 结论。

<!-- review:SF-2026-ARXIV-2605-11330:start -->
#### Rethinking Evaluation for LLM Hallucination Detection: A Desiderata, A New RAG-based Benchmark, New Insights

问题、旧路径与约束变化：hallucination detection benchmark 需要冻结 label noise、RAG context 与长上下文切片，单一 aggregate 不足以签发 detector 结论。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§2 Desiderata, §3 gaps and §4 benchmark。canonical owner=`PLATFORM-EVALUATION-SYSTEM`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§5 Experiments。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§7 Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11330:start -->exact-v1 支持：hallucination detection benchmark 需要冻结 label noise、RAG context 与长上下文切片，单一 aggregate 不足以签发 detector 结论。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11330:end -->

Books Decision=`No Change — Existing Coverage`；作者只形成命题比较与 root serial queue，不直接修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11330:end -->

**Books 对读：** `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md` 的“幻觉指标改善前，先排除 decoding 与输出分布的等价替代解释”。`books/part-06-ai-infrastructure/66-evaluation-system.md` 的“幻觉指标改善前，先排除 decoding 与输出分布的等价替代解释”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：hallucination detection benchmark 需要冻结 label noise、RAG context 与长上下文切片，单一 aggregate 不足以签发 detector 结论。 判定：**No Change — Existing Coverage**。

### [VERDI: Single-Call Confidence Estimation for Verification-Based LLM Judges via Decomposed Inference](https://arxiv.org/html/2605.11334v1)

**准入：** VERDI 从 judge 已生成的结构化 reasoning 分解一次调用的 confidence，但该值仍是可校准 sensor，不是 verdict authority。

<!-- review:SF-2026-ARXIV-2605-11334:start -->
#### VERDI: Single-Call Confidence Estimation for Verification-Based LLM Judges via Decomposed Inference

问题、旧路径与约束变化：VERDI 从 judge 已生成的结构化 reasoning 分解一次调用的 confidence，但该值仍是可校准 sensor，不是 verdict authority。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§3 Method。canonical owner=`PLATFORM-EVALUATION-SYSTEM`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§4–§5 Experiments。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§6 Discussion and §7 Conclusion；无独立 Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11334:start -->exact-v1 支持：VERDI 从 judge 已生成的结构化 reasoning 分解一次调用的 confidence，但该值仍是可校准 sensor，不是 verdict authority。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11334:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-11334:end -->

**Books 对读：** `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md` 的“Confidence 要在 Belief、Action 与 Outcome 三层校准”。`books/part-06-ai-infrastructure/66-evaluation-system.md` 的“Confidence 要在 Belief、Action 与 Outcome 三层校准”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：VERDI 从 judge 已生成的结构化 reasoning 分解一次调用的 confidence，但该值仍是可校准 sensor，不是 verdict authority。 判定：**Integrate — Applied; independent post-write review pending**。

### [ChunkFlow: Communication-Aware Chunked Prefetching for Layerwise Offloading in Distributed Diffusion Transformer Inference](https://arxiv.org/html/2605.11335v1)

**准入：** Building on this model, we design ChunkFlow, a communication-aware, chunk-granular offloading runtime that adaptively yields to collective communication and smoothly trades GPU memory for prefetch volume.

<!-- review:SF-2026-ARXIV-2605-11335:start -->
#### ChunkFlow: Communication-Aware Chunked Prefetching for Layerwise Offloading in Distributed Diffusion Transformer Inference

问题与机制：Building on this model, we design ChunkFlow, a communication-aware, chunk-granular offloading runtime that adaptively yields to collective communication and smoothly trades GPU memory for prefetch volume.。机制 owner=`INFER-GPU-MEMORY`。
Method / identity：arXiv:2605.11335v1 — §2 DiT/offloading motivation; §3 analytical overlap model and communication-aware chunked prefetching。
Evaluation：arXiv:2605.11335v1 — §4 Evaluation, including §4.1–§4.5。
Counterevidence / limitations：arXiv:2605.11335v1 — no dedicated Limitations section; PCIe topology, DiT workloads and offload regime bound the result; Appendix D only discusses applicability to LLM inference。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-2026-ARXIV-2605-11335:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `INFER-GPU-MEMORY` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-2026-ARXIV-2605-11335:end -->

Books Decision=`No Change — Existing Coverage`。当前 Books 已有 binding，不重复追加。
<!-- review:SF-2026-ARXIV-2605-11335:end -->

**Books 对读：** `INFER-GPU-MEMORY` → `books/part-05-inference-system/54-gpu-memory.md` 的“扩展层级”。books/part-05-inference-system/54-gpu-memory.md 的‘扩展层级’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：Building on this model, we design ChunkFlow, a communication-aware, chunk-granular offloading runtime that adaptively yields to collective communication and smoothly trades GPU memory for prefetch volume. 判定：**No Change — Existing Coverage**。

### [Options, Not Clicks: Lattice Refinement for Consent-Driven MCP Authorization](https://arxiv.org/html/2605.11360v1)

**准入：** In this work, we present Conleash, a client-side middleware that enforces boundary-scoped authorization by utilizing a risk lattice to auto-permit safe calls within known boundaries while escalating risks, a policy engine for user-defined invariants, and a refinement loop that converts user decisions into reusable…

<!-- review:SF-2026-ARXIV-2605-11360:start -->
#### Options, Not Clicks: Lattice Refinement for Consent-Driven MCP Authorization

问题与机制：In this work, we present Conleash, a client-side middleware that enforces boundary-scoped authorization by utilizing a risk lattice to auto-permit safe calls within known boundaries while escalating risks, a policy engine for user-defined invariants, and a refinement loop that converts user decisions into reusable…。机制 owner=`AGENT-MCP`。
Method / identity：arXiv:2605.11360v1 — §3 Motivation; §5 policy/risk lattice; §6 ConLeash boundary checking and refinement。
Evaluation：arXiv:2605.11360v1 — §8 Evaluation, including §8.1–§8.3。
Counterevidence / limitations：arXiv:2605.11360v1 — §9 Discussion contains limitations; policy language, risk lattice and disclosed MCP actions bound completeness。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-2026-ARXIV-2605-11360:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `AGENT-MCP` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-2026-ARXIV-2605-11360:end -->

Books Decision=`No Change — Existing Coverage`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-2026-ARXIV-2605-11360:end -->

**Books 对读：** `AGENT-MCP` → `books/part-07-agent/83-mcp.md` 的“MCP 不等于 Tool Authorization”。books/part-07-agent/83-mcp.md 的‘MCP 不等于 Tool Authorization’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：In this work, we present Conleash, a client-side middleware that enforces boundary-scoped authorization by utilizing a risk lattice to auto-permit safe calls within known boundaries while escalating risks, a policy engine for user-defined invariants, and a refinement loop that converts user decisions into reusable… 判定：**No Change — Existing Coverage**。

### [The tractability landscape of diffusion alignment: regularization, rewards, and computational primitives](https://arxiv.org/html/2605.11361v1)

**准入：** diffusion alignment 的可实现性取决于 KL/Wasserstein 目标与可用 sampling primitive，而不是抽象 reward 存在性。

<!-- review:SF-2026-ARXIV-2605-11361:start -->
#### The tractability landscape of diffusion alignment: regularization, rewards, and computational primitives

问题、旧路径与约束变化：diffusion alignment 的可实现性取决于 KL/Wasserstein 目标与可用 sampling primitive，而不是抽象 reward 存在性。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§2 Preliminaries, §3 KL alignment and §4 Wasserstein alignment。canonical owner=`MULTIMODAL-GENERATIVE-PARADIGMS`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：theorem/proof evaluations in §3–§4。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§5 Conclusion；理论工作，无独立 Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11361:start -->exact-v1 支持：diffusion alignment 的可实现性取决于 KL/Wasserstein 目标与可用 sampling primitive，而不是抽象 reward 存在性。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11361:end -->

Books Decision=`No Change — Existing Coverage`；作者只形成命题比较与 root serial queue，不直接修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11361:end -->

**Books 对读：** `MULTIMODAL-GENERATIVE-PARADIGMS` → `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的“Distributional Distance 可以成为受限训练目标”。`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的“Distributional Distance 可以成为受限训练目标”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：diffusion alignment 的可实现性取决于 KL/Wasserstein 目标与可用 sampling primitive，而不是抽象 reward 存在性。 判定：**No Change — Existing Coverage**。

### [LLM-X: A Scalable Negotiation-Oriented Exchange for Communication Among Personal LLM Agents](https://arxiv.org/html/2605.11376v1)

**准入：** We propose a personal-LLM exchange (LLM-X), a scalable negotiation-oriented environment that enables direct, structured communication across populations of personal agents (LLMs), each representing an individual user.

<!-- review:SF-LLM-X-A-SCALABLE-NEGOTIATION-ORIENTED-EXCHANGE-FOR-COMMUNICATION-AMONG-P:start -->
#### LLM-X: A Scalable Negotiation-Oriented Exchange for Communication Among Personal LLM Agents

问题与机制：We propose a personal-LLM exchange (LLM-X), a scalable negotiation-oriented environment that enables direct, structured communication across populations of personal agents (LLMs), each representing an individual user.。机制 owner=`AGENT-MULTI-AGENT`。
Method / identity：arXiv:2605.11376v1 — §3 System Overview: The LLM Exchange; §3.1 Architecture; §3.4 Message Model and Protocol。
Evaluation：arXiv:2605.11376v1 — §4 Environment and Scaling Experiments; §5 Results, including §5.4 Extended Load Experiments。
Counterevidence / limitations：arXiv:2605.11376v1 — §6 Discussion, especially §6.1–§6.4; no dedicated Limitations section, so prototype scale, policy assumptions and open-network failure scope remain boundaries。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-LLM-X-A-SCALABLE-NEGOTIATION-ORIENTED-EXCHANGE-FOR-COMMUNICATION-AMONG-P:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `AGENT-MULTI-AGENT` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-LLM-X-A-SCALABLE-NEGOTIATION-ORIENTED-EXCHANGE-FOR-COMMUNICATION-AMONG-P:end -->

Books Decision=`No Change — Existing Coverage`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-LLM-X-A-SCALABLE-NEGOTIATION-ORIENTED-EXCHANGE-FOR-COMMUNICATION-AMONG-P:end -->

**Books 对读：** `AGENT-MULTI-AGENT` → `books/part-07-agent/82-multi-agent.md` 的“Coordination State 必须有显式 Owner 与 Commit Transition”。population-scale personal-agent exchange 需要把 directory/routing、user identity、negotiation state 与 agreement commit 分权；结构化 message 不自动获得代表用户承诺的 authority。 新证据增量：We propose a personal-LLM exchange (LLM-X), a scalable negotiation-oriented environment that enables direct, structured communication across populations of personal agents (LLMs), each representing an individual user. 判定：**Integrate — Applied; independent post-write review pending**。

### [Kairos: A Scalable Serving System for Physical AI](https://arxiv.org/html/2605.11381v1)

**准入：** To fill this gap, we design Kairos, the first multi-robot serving system that makes the generate-execute loop a first-class citizen, with active involvement in the execution phase.

<!-- review:SF-KAIROS-A-SCALABLE-SERVING-SYSTEM-FOR-PHYSICAL-AI:start -->
#### Kairos: A Scalable Serving System for Physical AI

问题与机制：To fill this gap, we design Kairos, the first multi-robot serving system that makes the generate-execute loop a first-class citizen, with active involvement in the execution phase.。机制 owner=`INFER-SCHEDULING`。
全文定位：`arXiv:2605.11381v1 HTML — §3 adaptive execution-horizon controller; §4 execution-aware scheduling`；evaluation=`arXiv:2605.11381v1 — §5 six-model/five-simulator and real-robot evaluation`；limitations/counterevidence=`arXiv:2605.11381v1 — §6 limitations: confidence calibration, simulator and control-frequency scope`。
<!-- claim:SF-KAIROS-A-SCALABLE-SERVING-SYSTEM-FOR-PHYSICAL-AI:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-KAIROS-A-SCALABLE-SERVING-SYSTEM-FOR-PHYSICAL-AI:end -->
Books Decision=`Integrate`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-KAIROS-A-SCALABLE-SERVING-SYSTEM-FOR-PHYSICAL-AI:end -->

**Books 对读：** `INFER-SCHEDULING` → `books/part-05-inference-system/56-inference-scheduling.md` 的“Physical AI 把 Execution Horizon 变成调度状态”。books/part-05-inference-system/56-inference-scheduling.md 的‘Physical AI 把 Execution Horizon 变成调度状态’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：To fill this gap, we design Kairos, the first multi-robot serving system that makes the generate-execute loop a first-class citizen, with active involvement in the execution phase. 判定：**Integrate — Already present in current Books**。

### [Behavioral Mode Discovery for Fine-tuning Multimodal Generative Policies](https://arxiv.org/html/2605.11387v1)

**准入：** RL 微调生成式 policy 时，成功率优化会压缩原有多模态行为；轨迹级 mode discovery 与互信息奖励改变了 diversity state 的训练责任。

<!-- review:SF-2026-ARXIV-2605-11387:start -->
#### Behavioral Mode Discovery for Fine-tuning Multimodal Generative Policies

**问题与旧基线。** RL 微调生成式 policy 时，成功率优化会压缩原有多模态行为；轨迹级 mode discovery 与互信息奖励改变了 diversity state 的训练责任。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §4 Method：从离线 trajectories 发现离散 latent modes，并最大化 trajectory 与 mode 的互信息。 mode inference 只提供 diversity proposal，任务 reward 仍拥有 success 方向；MI regularizer 在同一 policy update 中保护已发现行为支路。

**Evaluation contract。** §5 Experiments：2D mixture、ManiSkill/D3IL、ANYmal 与 Franka Kitchen；固定种子、N=1024 episodes，结果按三次运行报告。 V3=7（3+2+2）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** Appendix A：mode 数与正则需调节，推断器会随 policy distribution 漂移；仅发现 task-level 离散模式，异构数据扩展仍未解决。

**Trade-off / failure / fallback。** 保留多样性会与单一 reward optimum 竞争；mode inference 漂移、mode alias 与过度分裂会把奖励写错轨迹。 mode 证据不稳或单一路径已满足部署目标时，回退常规 RL fine-tuning、显式 entropy/KL 约束及独立行为覆盖评估。

**Artifact。** Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-11387:start -->exact-v1 支持：只支持披露机器人任务、policy、数据量与 evaluator；不证明真实机器人安全、任意 mode 完备性或跨 embodiment 收益。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-11387:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-11387:end -->

**Books 对读：** `TRAIN-RLHF` → `books/part-04-training-system/31-rlhf.md` 的“Reverse KL 会把“找到高奖励”收缩成单一路径”。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：RL 微调生成式 policy 时，成功率优化会压缩原有多模态行为；轨迹级 mode discovery 与互信息奖励改变了 diversity state 的训练责任。 判定：**Integrate — Applied; independent post-write review pending**。

### [Deep Reasoning in General Purpose Agents via Structured Meta-Cognition](https://arxiv.org/html/2605.11388v1)

**准入：** DOLORES 用可执行 decomposition language 和受控 reasoning threads 改变通用 Agent 的计划、执行与 goal revision 控制流。

<!-- review:SF-2026-ARXIV-2605-11388:start -->
#### Deep Reasoning in General Purpose Agents via Structured Meta-Cognition

**问题与旧基线。** DOLORES 用可执行 decomposition language 和受控 reasoning threads 改变通用 Agent 的计划、执行与 goal revision 控制流。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3 Formal Language；§4 DOLORES Architecture and Implementation。形式化分解产生带依赖的子问题，reasoning threads 分别执行后再由控制器合并；模型生成的分解仍是 proposal。

**Evaluation contract。** §5；四个 reasoning benchmarks、三个模型设置与受控 decomposition。V3=2+2+2=6；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** Appendix A Limitations：分解编写、token 成本和 domain/task 覆盖受限。

**Trade-off / failure / fallback。** 结构化状态提高可审计性但增加分解错误、同步与 token 成本；简单短任务继续适合单轨推理。

<!-- claim:SF-2026-ARXIV-2605-11388:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11388:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11388:end -->

**Books 对读：** `AGENT-PLANNING` → `books/part-07-agent/79-planning.md` 的“从目标到状态图”。正文约第 42 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：DOLORES 用可执行 decomposition language 和受控 reasoning threads 改变通用 Agent 的计划、执行与 goal revision 控制流。 判定：**Integrate — Applied; independent post-write review pending**。

### [fg-expo: Frontier-guided exploration-prioritized policy optimization via adaptive kl and gaussian curriculum](https://arxiv.org/html/2605.11403v1)

**准入：** adaptive KL 与基于逐题历史通过率的 Gaussian curriculum 改变 GRPO/RLVR 的探索控制变量。

<!-- review:SF-2026-ARXIV-2605-11403:start -->
#### fg-expo: Frontier-guided exploration-prioritized policy optimization via adaptive kl and gaussian curriculum

**问题与旧基线。** adaptive KL 与基于逐题历史通过率的 Gaussian curriculum 改变 GRPO/RLVR 的探索控制变量。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3.3 Adaptive KL；§3.4 Gaussian Curriculum Sampling；§3.5 Algorithm；§3.6 Implementation。batch accuracy 调整 KL，逐题 EMA pass-rate 在中等难度处获得较高采样权；两者共享当前 policy 的能力观测。

**Evaluation contract。** §4.1–§4.4；DAPO-17K、两个模型和六个数学 benchmark。V3=2+2+2=6；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** §5 与附录；无独立 Limitations；只支持受测数学 RLVR 设置。

**Trade-off / failure / fallback。** 提高学习信号利用率但会放大能力估计滞后与任务迁移偏差；正文已明确版本化 task utility 同时驱动样本调度和 per-task KL，并给出固定 mixture/floor fallback。

<!-- claim:SF-2026-ARXIV-2605-11403:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11403:end -->

Books Decision=`No Change — Existing Coverage`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11403:end -->

**Books 对读：** `TRAIN-GRPO` → `books/part-04-training-system/33-grpo.md` 的“多任务 RL 的 curriculum/KL controller（正文段落）”。正文约第 1558 行已逐命题覆盖该机制、代价与 fallback；Review notes 不参与覆盖判断。 新证据增量：adaptive KL 与基于逐题历史通过率的 Gaussian curriculum 改变 GRPO/RLVR 的探索控制变量。 判定：**No Change — Existing Coverage**。

### [Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry](https://arxiv.org/html/2605.11418v1)

**准入：** While this design enables scalable, on-demand capability expansion, it also introduces a semantic supply-chain risk in which natural-language metadata and instructions can affect which skills are admitted, surfaced, selected, and loaded.

<!-- review:SF-UNDER-THE-HOOD-OF-SKILL-MD-SEMANTIC-SUPPLY-CHAIN-ATTACKS-ON-AI-AGENT-SKI:start -->
#### Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry

问题与机制：While this design enables scalable, on-demand capability expansion, it also introduces a semantic supply-chain risk in which natural-language metadata and instructions can affect which skills are admitted, surfaced, selected, and loaded.。机制 owner=`AGENT-PLATFORM`。
全文定位：`arXiv:2605.11418v1 HTML — §3 SKILL.md semantic dependency-confusion attack; §4 attack construction`；evaluation=`arXiv:2605.11418v1 — §5 multi-agent/toolchain evaluation`；limitations/counterevidence=`arXiv:2605.11418v1 — §6 limitations: repository, model and attacker-access scope`。
<!-- claim:SF-UNDER-THE-HOOD-OF-SKILL-MD-SEMANTIC-SUPPLY-CHAIN-ATTACKS-ON-AI-AGENT-SKI:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-UNDER-THE-HOOD-OF-SKILL-MD-SEMANTIC-SUPPLY-CHAIN-ATTACKS-ON-AI-AGENT-SKI:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-UNDER-THE-HOOD-OF-SKILL-MD-SEMANTIC-SUPPLY-CHAIN-ATTACKS-ON-AI-AGENT-SKI:end -->

**Books 对读：** `AGENT-PLATFORM` → `books/part-07-agent/84-agent-platform.md` 的“被审计的 Skill 必须与实际执行 Artifact 同一”。正文要求 reviewed bundle immutable identity、依赖/policy admission、执行同 digest 和 runtime receipt，并在 Skill Lifecycle 以 Admission 与 Runtime 两个 Gate 分权；这直接覆盖 semantic metadata/instruction supply-chain。 新证据增量：While this design enables scalable, on-demand capability expansion, it also introduces a semantic supply-chain risk in which natural-language metadata and instructions can affect which skills are admitted, surfaced, selected, and loaded. 判定：**No Change — Existing Coverage**。

### [A Mechanistic Investigation of Supervised Fine Tuning](https://arxiv.org/html/2605.11426v1)

**准入：** SFT 前后整体 activation 高相似仍可掩盖 sparse latent 的 task/layer-specific 漂移，因此表面保持不能证明内部能力未重排。

<!-- review:SF-2026-ARXIV-2605-11426:start -->
#### A Mechanistic Investigation of Supervised Fine Tuning

问题、旧路径与约束变化：SFT 前后整体 activation 高相似仍可掩盖 sparse latent 的 task/layer-specific 漂移，因此表面保持不能证明内部能力未重排。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§3 Methodology。canonical owner=`TRAIN-SFT`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§4 Findings。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：Conclusion and Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11426:start -->exact-v1 支持：SFT 前后整体 activation 高相似仍可掩盖 sparse latent 的 task/layer-specific 漂移，因此表面保持不能证明内部能力未重排。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11426:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-11426:end -->

**Books 对读：** `TRAIN-SFT` → `books/part-04-training-system/29-sft.md` 的“Evaluation 应分开能力与行为”。`books/part-04-training-system/29-sft.md` 的“Evaluation 应分开能力与行为”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：SFT 前后整体 activation 高相似仍可掩盖 sparse latent 的 task/layer-specific 漂移，因此表面保持不能证明内部能力未重排。 判定：**Integrate — Applied; independent post-write review pending**。

### [Agent-BRACE: Decoupling Beliefs from Actions in Long-Horizon Tasks via Verbalized State Uncertainty](https://arxiv.org/html/2605.11436v1)

**准入：** Therefore, we introduce Agent-BRACE: Agent Belief state Representation via Abstraction and Confidence Estimation, a method that decouples an LLM agent into a belief state model and a policy model, jointly optimized via reinforcement learning.

<!-- review:SF-AGENT-BRACE-DECOUPLING-BELIEFS-FROM-ACTIONS-IN-LONG-HORIZON-TASKS-VIA-VE:start -->
#### Agent-BRACE: Decoupling Beliefs from Actions in Long-Horizon Tasks via Verbalized State Uncertainty

问题与机制：Therefore, we introduce Agent-BRACE: Agent Belief state Representation via Abstraction and Confidence Estimation, a method that decouples an LLM agent into a belief state model and a policy model, jointly optimized via reinforcement learning.。机制 owner=`AGENT-MEMORY`。
Method / identity：arXiv:2605.11436v1 — §2 Methodology: Agent-BRACE; §2.2 belief-state/policy decomposition; §2.5 reward design。
Evaluation：arXiv:2605.11436v1 — §3 Experimental Setup and Results; Appendix H statistical reliability。
Counterevidence / limitations：arXiv:2605.11436v1 — no dedicated Limitations section; §6 Conclusion and Appendices C/F/H/I bound the result to ordinal confidence, disclosed environments/models and the reported RL setup。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-AGENT-BRACE-DECOUPLING-BELIEFS-FROM-ACTIONS-IN-LONG-HORIZON-TASKS-VIA-VE:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `AGENT-MEMORY` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-AGENT-BRACE-DECOUPLING-BELIEFS-FROM-ACTIONS-IN-LONG-HORIZON-TASKS-VIA-VE:end -->

Books Decision=`No Change — Existing Coverage`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-AGENT-BRACE-DECOUPLING-BELIEFS-FROM-ACTIONS-IN-LONG-HORIZON-TASKS-VIA-VE:end -->

**Books 对读：** `AGENT-MEMORY` → `books/part-07-agent/77-memory.md` 的“Belief State：先保存竞争假设，再决定事实”。books/part-07-agent/77-memory.md 的‘Belief State：先保存竞争假设，再决定事实’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：Therefore, we introduce Agent-BRACE: Agent Belief state Representation via Abstraction and Confidence Estimation, a method that decouples an LLM agent into a belief state model and a policy model, jointly optimized via reinforcement learning. 判定：**No Change — Existing Coverage**。

### [Can a Single Message Paralyze the AI Infrastructure? The Rise of AbO-DDoS Attacks through Targeted Mobius Injection](https://arxiv.org/html/2605.11442v1)

**准入：** To mitigate Mobius Injection, we propose a proactive defense mechanism using Agent Component Energy (ACE) Analysis, which detects malicious recursive triggers by measuring anomalous energy in the agent's component graph.

<!-- review:SF-CAN-A-SINGLE-MESSAGE-PARALYZE-THE-AI-INFRASTRUCTURE-THE-RISE-OF-ABO-DDOS:start -->
#### Can a Single Message Paralyze the AI Infrastructure? The Rise of AbO-DDoS Attacks through Targeted Mobius Injection

问题与机制：To mitigate Mobius Injection, we propose a proactive defense mechanism using Agent Component Energy (ACE) Analysis, which detects malicious recursive triggers by measuring anomalous energy in the agent's component graph.。机制 owner=`PLATFORM-SECURITY`。
全文定位：`arXiv:2605.11442v1 HTML — §3 Möbius indirect-injection loop; §4 AbO-DDoS control path`；evaluation=`arXiv:2605.11442v1 — §5 three claw agents, three coding agents and twelve LLMs`；limitations/counterevidence=`arXiv:2605.11442v1 — §6 limitations: harness, tool and adaptive-defense boundary`。
<!-- claim:SF-CAN-A-SINGLE-MESSAGE-PARALYZE-THE-AI-INFRASTRUCTURE-THE-RISE-OF-ABO-DDOS:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-CAN-A-SINGLE-MESSAGE-PARALYZE-THE-AI-INFRASTRUCTURE-THE-RISE-OF-ABO-DDOS:end -->
Books Decision=`Integrate`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-CAN-A-SINGLE-MESSAGE-PARALYZE-THE-AI-INFRASTRUCTURE-THE-RISE-OF-ABO-DDOS:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“Exactness 保持不变时，加速路径仍可能被定向击穿”。books/part-06-ai-infrastructure/72-security.md 的‘Exactness 保持不变时，加速路径仍可能被定向击穿’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：To mitigate Mobius Injection, we propose a proactive defense mechanism using Agent Component Energy (ACE) Analysis, which detects malicious recursive triggers by measuring anomalous energy in the agent's component graph. 判定：**Integrate — Already present in current Books**。

### [FibQuant: Universal Vector Quantization for Random-Access KV-Cache Compression](https://arxiv.org/html/2605.11478v1)

**准入：** We introduce \textsc{FibQuant}, a universal fixed-rate vector quantizer that keeps the same normalize--rotate--store interface while replacing scalar tables by a shared radial--angular codebook matched to this canonical source.

<!-- review:SF-FIBQUANT-UNIVERSAL-VECTOR-QUANTIZATION-FOR-RANDOM-ACCESS-KV-CACHE-COMPRE:start -->
#### FibQuant: Universal Vector Quantization for Random-Access KV-Cache Compression

问题与机制：We introduce \textsc{FibQuant}, a universal fixed-rate vector quantizer that keeps the same normalize--rotate--store interface while replacing scalar tables by a shared radial--angular codebook matched to this canonical source.。机制 owner=`INFER-KV-CACHE`。
全文定位：`arXiv:2605.11478v1 HTML — §3 FibQuant fixed-rate random-access code layout`；evaluation=`arXiv:2605.11478v1 — §4 KV-cache quality/throughput evaluation`；limitations/counterevidence=`arXiv:2605.11478v1 — §5 limitations: model, sequence length, hardware and quantization scope`。
<!-- claim:SF-FIBQUANT-UNIVERSAL-VECTOR-QUANTIZATION-FOR-RANDOM-ACCESS-KV-CACHE-COMPRE:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-FIBQUANT-UNIVERSAL-VECTOR-QUANTIZATION-FOR-RANDOM-ACCESS-KV-CACHE-COMPRE:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-FIBQUANT-UNIVERSAL-VECTOR-QUANTIZATION-FOR-RANDOM-ACCESS-KV-CACHE-COMPRE:end -->

**Books 对读：** `INFER-KV-CACHE` → `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 的“Quantization Objective 应对齐 Attention Distortion”。books/part-05-inference-system/45-why-kv-cache-speeds-up.md 的‘Quantization Objective 应对齐 Attention Distortion’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We introduce \textsc{FibQuant}, a universal fixed-rate vector quantizer that keeps the same normalize--rotate--store interface while replacing scalar tables by a shared radial--angular codebook matched to this canonical source. 判定：**No Change — Existing Coverage**。

### [Digital Identity for Agentic Systems: Toward a Portable Authorization Standard for Autonomous Agents](https://arxiv.org/html/2605.11487v1)

**准入：** Enterprise AI is shifting from copilots to autonomous agents capable of executing workflows, negotiating outcomes, and making decisions with limited human oversight.

<!-- review:SF-DIGITAL-IDENTITY-FOR-AGENTIC-SYSTEMS-TOWARD-A-PORTABLE-AUTHORIZATION-STA:start -->
#### Digital Identity for Agentic Systems: Toward a Portable Authorization Standard for Autonomous Agents

问题与机制：Enterprise AI is shifting from copilots to autonomous agents capable of executing workflows, negotiating outcomes, and making decisions with limited human oversight.。机制 owner=`PLATFORM-SECURITY`。
全文定位：`arXiv:2605.11487v1 HTML — §3 portable agent identity and authorization envelope`；evaluation=`arXiv:2605.11487v1 — §4 protocol examples and security analysis`；limitations/counterevidence=`arXiv:2605.11487v1 — §5 limitations: deployment and interoperability evidence`。
<!-- claim:SF-DIGITAL-IDENTITY-FOR-AGENTIC-SYSTEMS-TOWARD-A-PORTABLE-AUTHORIZATION-STA:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-DIGITAL-IDENTITY-FOR-AGENTIC-SYSTEMS-TOWARD-A-PORTABLE-AUTHORIZATION-STA:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-DIGITAL-IDENTITY-FOR-AGENTIC-SYSTEMS-TOWARD-A-PORTABLE-AUTHORIZATION-STA:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“从资产与信任边界开始”。books/part-06-ai-infrastructure/72-security.md 的‘从资产与信任边界开始’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：Enterprise AI is shifting from copilots to autonomous agents capable of executing workflows, negotiating outcomes, and making decisions with limited human oversight. 判定：**No Change — Existing Coverage**。

### [Understanding and Preventing Entropy Collapse in RLVR with On-Policy Entropy Flow Optimization](https://arxiv.org/html/2605.11491v1)

**准入：** RLVR entropy collapse 可分解为 token-level entropy-increasing/decreasing update flow 不平衡，控制器需要在严格 on-policy 边界内调节。

<!-- review:SF-2026-ARXIV-2605-11491:start -->
#### Understanding and Preventing Entropy Collapse in RLVR with On-Policy Entropy Flow Optimization

问题、旧路径与约束变化：RLVR entropy collapse 可分解为 token-level entropy-increasing/decreasing update flow 不平衡，控制器需要在严格 on-policy 边界内调节。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§3–§5 mechanism and method。canonical owner=`TRAIN-GRPO`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§6 Experiments。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：Limitations after Conclusion。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11491:start -->exact-v1 支持：RLVR entropy collapse 可分解为 token-level entropy-increasing/decreasing update flow 不平衡，控制器需要在严格 on-policy 边界内调节。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11491:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-11491:end -->

**Books 对读：** `TRAIN-GRPO` → `books/part-04-training-system/33-grpo.md` 的“Verifiable Reward 不等于每个样本都可学习”。`books/part-04-training-system/33-grpo.md` 的“Verifiable Reward 不等于每个样本都可学习”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：RLVR entropy collapse 可分解为 token-level entropy-increasing/decreasing update flow 不平衡，控制器需要在严格 on-policy 边界内调节。 判定：**Integrate — Applied; independent post-write review pending**。

### [STRIDE: Training-Free Diversity Guidance via PCA-Directed Feature Perturbation in Single-Step Diffusion Models](https://arxiv.org/html/2605.11494v1)

**准入：** 单步/少步 diffusion 失去多步 trajectory 中可注入随机性的接口；PCA 定向 feature perturbation 把 diversity control 移入 student 的内部表示几何。

<!-- review:SF-2026-ARXIV-2605-11494:start -->
#### STRIDE: Training-Free Diversity Guidance via PCA-Directed Feature Perturbation in Single-Step Diffusion Models

**问题与旧基线。** 单步/少步 diffusion 失去多步 trajectory 中可注入随机性的接口；PCA 定向 feature perturbation 把 diversity control 移入 student 的内部表示几何。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §3 Method：在中间 Transformer activation 的主成分方向投影 spatially coherent pink noise；单次 forward、无需训练或在线优化。 activation geometry 拥有可扰动方向，generation model 仍拥有输出；扰动器只改变 proposal diversity，不拥有 fidelity 真值。

**Evaluation contract。** §4 Experiments：FLUX.1-schnell 12B 一步与 SD3.5 Large Turbo 8.1B 四步；COCO、DrawBench、PartiPrompts、GenEval，以相似度、CLIP/HPS 等受限指标比较。 V3=5（2+1+2）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；仅两个 few-step 模型与所选层/主成分/扰动强度。离线 PCA、额外统计和强扰动的语义退化没有形成生产 SLO 结论。

**Trade-off / failure / fallback。** 增加 PCA 校准、存储与层选择成本；feature distribution 漂移或过强扰动会破坏 alignment。 几何失配时关闭 perturbation，回退原 student、multi-step sampler 或外部 best-of-N，并用独立质量 gate 验收。

**Artifact。** Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-11494:start -->exact-v1 支持：只证明作者模型/数据/指标下的 diversity–fidelity Pareto；不证明一般 diffusion manifold、端到端 latency 或用户偏好。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-11494:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-11494:end -->

**Books 对读：** `MULTIMODAL-GENERATIVE-PARADIGMS` → `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的“Few-step Distillation 要在 Student 实际访问的状态上验收”。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：单步/少步 diffusion 失去多步 trajectory 中可注入随机性的接口；PCA 定向 feature perturbation 把 diversity control 移入 student 的内部表示几何。 判定：**Integrate — Applied; independent post-write review pending**。

### [The Evaluation Differential: When Frontier AI Models Recognise They Are Being Tested](https://arxiv.org/html/2605.11496v1)

**准入：** We introduce the Evaluation Differential (ED), a conditional divergence in a target behavioural property between recognised-evaluation and deployment-continuous contexts, define a normalised effect-size form (nED) for cross-property comparison, and prove that marginal evaluation scores cannot identify ED.

<!-- review:SF-THE-EVALUATION-DIFFERENTIAL-WHEN-FRONTIER-AI-MODELS-RECOGNISE-THEY-ARE-B:start -->
#### The Evaluation Differential: When Frontier AI Models Recognise They Are Being Tested

问题与机制：We introduce the Evaluation Differential (ED), a conditional divergence in a target behavioural property between recognised-evaluation and deployment-continuous contexts, define a normalised effect-size form (nED) for cross-property comparison, and prove that marginal evaluation scores cannot identify ED.。机制 owner=`PLATFORM-EVALUATION-SYSTEM`。
全文定位：`arXiv:2605.11496v1 HTML — §3 Evaluation Differential and TRACE estimator`；evaluation=`arXiv:2605.11496v1 — §4 cross-task evaluation and ablations`；limitations/counterevidence=`arXiv:2605.11496v1 — §5 limitations: evaluator, perturbation and domain-shift scope`。
<!-- claim:SF-THE-EVALUATION-DIFFERENTIAL-WHEN-FRONTIER-AI-MODELS-RECOGNISE-THEY-ARE-B:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-THE-EVALUATION-DIFFERENTIAL-WHEN-FRONTIER-AI-MODELS-RECOGNISE-THEY-ARE-B:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-THE-EVALUATION-DIFFERENTIAL-WHEN-FRONTIER-AI-MODELS-RECOGNISE-THEY-ARE-B:end -->

**Books 对读：** `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md` 的“从目标到证据，而不是从指标到目标”。recognised-evaluation 与 deployment-continuous context 的 behavioral differential 必须成为显式 evaluation state；marginal benchmark score 不能识别该 differential。 新证据增量：We introduce the Evaluation Differential (ED), a conditional divergence in a target behavioural property between recognised-evaluation and deployment-continuous contexts, define a normalised effect-size form (nED) for cross-property comparison, and prove that marginal evaluation scores cannot identify ED. 判定：**Integrate — Applied; independent post-write review pending**。

### [FlowSteer: Prompt-Only Workflow Steering Exposes Planning-Time Vulnerabilities in Multi-Agent LLM Systems](https://arxiv.org/html/2605.11514v1)

**准入：** We study this risk through social influence probing workflows to identify high-impact subtasks and malicious-signal propagation.

<!-- review:SF-FLOWSTEER-PROMPT-ONLY-WORKFLOW-STEERING-EXPOSES-PLANNING-TIME-VULNERABIL:start -->
#### FlowSteer: Prompt-Only Workflow Steering Exposes Planning-Time Vulnerabilities in Multi-Agent LLM Systems

问题与机制：We study this risk through social influence probing workflows to identify high-impact subtasks and malicious-signal propagation.。机制 owner=`PLATFORM-SECURITY`。
全文定位：`arXiv:2605.11514v1 HTML — §3 FlowSteer runtime information-flow policy`；evaluation=`arXiv:2605.11514v1 — §4 enforcement path and evaluation`；limitations/counterevidence=`arXiv:2605.11514v1 — §5 limitations: policy completeness and tool-boundary coverage`。
<!-- claim:SF-FLOWSTEER-PROMPT-ONLY-WORKFLOW-STEERING-EXPOSES-PLANNING-TIME-VULNERABIL:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-FLOWSTEER-PROMPT-ONLY-WORKFLOW-STEERING-EXPOSES-PLANNING-TIME-VULNERABIL:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-FLOWSTEER-PROMPT-ONLY-WORKFLOW-STEERING-EXPOSES-PLANNING-TIME-VULNERABIL:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“从资产与信任边界开始”。books/part-06-ai-infrastructure/72-security.md 的‘从资产与信任边界开始’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We study this risk through social influence probing workflows to identify high-impact subtasks and malicious-signal propagation. 判定：**No Change — Existing Coverage**。

### [NAVIS: Concurrent Search and Update with Low Position-Seeking Overhead in On-SSD Graph-Based Vector Search](https://arxiv.org/html/2605.11523v1)

**准入：** We present NAVIS, an on-SSD GVS system that drives down position-seeking overhead through (i) a layout-supported selective vector read that breaks the packed-page coupling without losing its locality benefits, (ii) a dynamic lightweight entrance graph update mechanism that reuses traversal information already produced by concurrent updates, and (iii) an entrance graph-aware edgelist cache that…

<!-- review:SF-NAVIS-CONCURRENT-SEARCH-AND-UPDATE-WITH-LOW-POSITION-SEEKING-OVERHEAD-IN:start -->
#### NAVIS: Concurrent Search and Update with Low Position-Seeking Overhead in On-SSD Graph-Based Vector Search

问题与机制：We present NAVIS, an on-SSD GVS system that drives down position-seeking overhead through (i) a layout-supported selective vector read that breaks the packed-page coupling without losing its locality benefits, (ii) a dynamic lightweight entrance graph update mechanism that reuses traversal information already produced by concurrent updates, and (iii) an entrance graph-aware edgelist cache that…。机制 owner=`AGENT-RAG`。
Method / identity：arXiv:2605.11523v1 — §4 NAVIS overview; §5 selective vector reads; §6 dynamic entrance graph; §7 entrance-graph-aware cache; §8 implementation。
Evaluation：arXiv:2605.11523v1 — §9 Evaluation, including §9.1 Experimental Setup。
Counterevidence / limitations：arXiv:2605.11523v1 — §11 Discussion; SSD/layout/workload scope and concurrent consistency responsibilities bound the result。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-NAVIS-CONCURRENT-SEARCH-AND-UPDATE-WITH-LOW-POSITION-SEEKING-OVERHEAD-IN:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `AGENT-RAG` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-NAVIS-CONCURRENT-SEARCH-AND-UPDATE-WITH-LOW-POSITION-SEEKING-OVERHEAD-IN:end -->

Books Decision=`Integrate`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-NAVIS-CONCURRENT-SEARCH-AND-UPDATE-WITH-LOW-POSITION-SEEKING-OVERHEAD-IN:end -->

**Books 对读：** `AGENT-RAG` → `books/part-07-agent/76-rag.md` 的“Concurrent Update 让 SSD Index 同时拥有 Search 与 Maintenance State”。books/part-07-agent/76-rag.md 的‘Concurrent Update 让 SSD Index 同时拥有 Search 与 Maintenance State’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We present NAVIS, an on-SSD GVS system that drives down position-seeking overhead through (i) a layout-supported selective vector read that breaks the packed-page coupling without losing its locality benefits, (ii) a dynamic lightweight entrance graph update mechanism that reuses traversal information already produced by concurrent updates, and (iii) an entrance graph-aware edgelist cache that… 判定：**Integrate — Already present in current Books**。

### [PRISM: : Planning and Reasoning with Intent in Simulated Embodied Environments](https://arxiv.org/html/2605.11534v1)

**准入：** PRISM 把 embodied-agent 单一 success rate 拆成 perception、intent reasoning 与 long-horizon coordination 的可替换诊断 probe。

<!-- review:SF-2026-ARXIV-2605-11534:start -->
#### PRISM: : Planning and Reasoning with Intent in Simulated Embodied Environments

**问题与旧基线。** PRISM 把 embodied-agent 单一 success rate 拆成 perception、intent reasoning 与 long-horizon coordination 的可替换诊断 probe。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3 Benchmark Construction；§4 Agent-agnostic Protocol and Diagnostic Probes。统一 action API 固定环境，capability tiers 和可替换 probes 分离 failure owner；probe 只是诊断，不等于因果证明。

**Evaluation contract。** §5；300 tasks、五个 apartment、七个 LLM 与模块替换消融。V3=2+2+2=6；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** Appendix J：模拟住宅、任务/对象覆盖与 responsible release 限制。

**Trade-off / failure / fallback。** 获得可定位失败但增加 oracle/probe 假设和 simulator gap；开放世界结果须回退 end-to-end outcome 与真实环境验证。

<!-- claim:SF-2026-ARXIV-2605-11534:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11534:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11534:end -->

**Books 对读：** `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md` 的“Agent and Outcome Evaluation”。正文约第 438 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：PRISM 把 embodied-agent 单一 success rate 拆成 perception、intent reasoning 与 long-horizon coordination 的可替换诊断 probe。 判定：**Integrate — Applied; independent post-write review pending**。

### [Fast MoE Inference via Predictive Prefetching and Expert Replication](https://arxiv.org/html/2605.11537v1)

**准入：** To address these challenges, we propose a dynamic expert replication strategy that predicts which experts are likely to be overloaded and replicates them for upcoming batches of tokens.

<!-- review:SF-FAST-MOE-INFERENCE-VIA-PREDICTIVE-PREFETCHING-AND-EXPERT-REPLICATION:start -->
#### Fast MoE Inference via Predictive Prefetching and Expert Replication

问题与机制：To address these challenges, we propose a dynamic expert replication strategy that predicts which experts are likely to be overloaded and replicates them for upcoming batches of tokens.。机制 owner=`INFER-TENSORRT-LLM`。
全文定位：`arXiv:2605.11537v1 HTML — §3 Methodology; §3.1 inference thread; §3.2 hash-building thread; §3.3 SRU and capacity cap`；evaluation=`arXiv:2605.11537v1 — §4 Experiments under the disclosed MoE models, hardware and traffic`；limitations/counterevidence=`arXiv:2605.11537v1 — §6 Conclusion; no independent Limitations section and front matter contains placeholder publication metadata`。
<!-- claim:SF-FAST-MOE-INFERENCE-VIA-PREDICTIVE-PREFETCHING-AND-EXPERT-REPLICATION:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-FAST-MOE-INFERENCE-VIA-PREDICTIVE-PREFETCHING-AND-EXPERT-REPLICATION:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-FAST-MOE-INFERENCE-VIA-PREDICTIVE-PREFETCHING-AND-EXPERT-REPLICATION:end -->

**Books 对读：** `INFER-TENSORRT-LLM` → `books/part-05-inference-system/49-tensorrt-llm.md` 的“Expert Placement 必须跟随热度演化”。正文的 expert placement/热度演化段已明确 predictive placement 只拥有 proposal、router 仍权威，并覆盖 replica、prefetch、迁移成本与静态 fallback；旧量化锚点作废。 新证据增量：future-token overload prediction 驱动 expert replication/prefetch，并带来 replica lifecycle、placement、显存和通信取舍。 判定：**No Change — Existing Coverage**。

### [Taming Extreme Tokens: Covariance-Aware GRPO with Gaussian-Kernel Advantage Reweighting](https://arxiv.org/html/2605.11538v1)

**准入：** covariance-aware token reweighting 改变 GRPO 中 extreme token 的更新权重与训练稳定性。

<!-- review:SF-2026-ARXIV-2605-11538:start -->
#### Taming Extreme Tokens: Covariance-Aware GRPO with Gaussian-Kernel Advantage Reweighting

**问题与旧基线。** covariance-aware token reweighting 改变 GRPO 中 extreme token 的更新权重与训练稳定性。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §2.2 Motivation；§2.3 Covariance-aware Advantage Reweighting。方法估计 token probability 与 advantage 的协方差，并以 Gaussian kernel 降低 extreme token update 的影响。

**Evaluation contract。** §3；1.5B/7B 模型与数学 reasoning 设置。V3=2+1+2=5；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** Limitations 明确只覆盖至 7B 和数学任务。

**Trade-off / failure / fallback。** 减少少数极端更新但引入 kernel/scale 超参并可能压低真正关键 token；分布稳定时保留原 GRPO，异常时回退 clipping/gradient diagnostics。

<!-- claim:SF-2026-ARXIV-2605-11538:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11538:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11538:end -->

**Books 对读：** `TRAIN-GRPO` → `books/part-04-training-system/33-grpo.md` 的“Group-relative Gradient 不是独立样本均值”。正文约第 290 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：covariance-aware token reweighting 改变 GRPO 中 extreme token 的更新权重与训练稳定性。 判定：**Integrate — Applied; independent post-write review pending**。

### [Sharpen Your Flow: Sharpness-Aware Sampling for Flow Matching](https://arxiv.org/html/2605.11547v1)

**准入：** sharpness-aware sampler 把 flow generation 的 timestep 预算改为由离线局部敏感度校准的非均匀调度。

<!-- review:SF-2026-ARXIV-2605-11547:start -->
#### Sharpen Your Flow: Sharpness-Aware Sampling for Flow Matching

**问题与旧基线。** sharpness-aware sampler 把 flow generation 的 timestep 预算改为由离线局部敏感度校准的非均匀调度。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3 Offline Calibration and Online Sampling；§4 Numerical/Variational/Statistical Principles。离线有限差分估计 velocity-field sharpness，按分位数构造 timestep grid，线上仍用普通 Euler。

**Evaluation contract。** §5 与 Appendices D/E；固定 NFE、synthetic trajectories 与 FLUX 设置。V3=2+1+2=5；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；结论限于作者 sampler、模型与指标，NFE 不等于端到端延迟。

**Trade-off / failure / fallback。** 额外 calibration 换同 NFE 下的误差重分配，但存在 profile drift 与 workload dependence；正文已要求 sensitivity profile、trajectory displacement、quality tolerance 和 global error budget。

<!-- claim:SF-2026-ARXIV-2605-11547:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11547:end -->

Books Decision=`No Change — Existing Coverage`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11547:end -->

**Books 对读：** `MULTIMODAL-GENERATIVE-PARADIGMS` → `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的“Diffusion trajectory 的 sensitivity calibration profile（正文段落）”。正文约第 474 行已逐命题覆盖该机制、代价与 fallback；Review notes 不参与覆盖判断。 新证据增量：sharpness-aware sampler 把 flow generation 的 timestep 预算改为由离线局部敏感度校准的非均匀调度。 判定：**No Change — Existing Coverage**。

### [The DAWN of World-Action Interactive Models](https://arxiv.org/html/2605.11550v1)

**准入：** Experiments show that DAWN achieves strong planning performance and favorable safety-related results across multiple autonomous driving benchmarks.

<!-- review:SF-THE-DAWN-OF-WORLD-ACTION-INTERACTIVE-MODELS:start -->
#### The DAWN of World-Action Interactive Models

问题与机制：Experiments show that DAWN achieves strong planning performance and favorable safety-related results across multiple autonomous driving benchmarks.。机制 owner=`MULTIMODAL-WORLD-MODELS`。
全文定位：`arXiv:2605.11550v1 HTML — §3 action-conditioned world-state model; §4 DAWN update loop`；evaluation=`arXiv:2605.11550v1 — §5 interactive-generation evaluation`；limitations/counterevidence=`arXiv:2605.11550v1 — §6 Limitations; HTML front matter exact date line `August 24, 2026` conflicts with arXiv v1 metadata`。
<!-- claim:SF-THE-DAWN-OF-WORLD-ACTION-INTERACTIVE-MODELS:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-THE-DAWN-OF-WORLD-ACTION-INTERACTIVE-MODELS:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-THE-DAWN-OF-WORLD-ACTION-INTERACTIVE-MODELS:end -->

**Books 对读：** `MULTIMODAL-WORLD-MODELS` → `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 的“Action-conditioned transition”。books/part-03-multimodal-world-models/25-multimodal-world-models.md 的‘Action-conditioned transition’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：Experiments show that DAWN achieves strong planning performance and favorable safety-related results across multiple autonomous driving benchmarks. 判定：**No Change — Existing Coverage**。

### [Hindsight Hint Distillation: Scaffolded Reasoning for SWE Agents from CoT-free Answers](https://arxiv.org/html/2605.11556v1)

**准入：** Hindsight Hint Distillation 从当前 Agent 失败 rollout 生成针对性 hint，再蒸馏成功轨迹，改变 agentic SFT 的数据生成闭环。

<!-- review:SF-2026-ARXIV-2605-11556:start -->
#### Hindsight Hint Distillation: Scaffolded Reasoning for SWE Agents from CoT-free Answers

**问题与旧基线。** Hindsight Hint Distillation 从当前 Agent 失败 rollout 生成针对性 hint，再蒸馏成功轨迹，改变 agentic SFT 的数据生成闭环。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3、§3.1–§3.3 Hindsight Hint Distillation。失败轨迹定位阻塞点，teacher 生成 hint scaffold，policy 完成 rollout 后自蒸馏；hint 不进入部署接口。

**Evaluation contract。** §4；SWE-bench Verified/Multilingual、OpenHands、基线与消融。V3=3+2+3=8；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；结论绑定 coding agent、judge/hint generator 与受测模型。

**Trade-off / failure / fallback。** 降低人工 CoT 成本但可能蒸馏错误归因、judge bias 和 scaffold shortcut；hint 质量不足时保留人工 demonstrations/verified tests。

<!-- claim:SF-2026-ARXIV-2605-11556:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11556:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11556:end -->

**Books 对读：** `TRAIN-SFT` → `books/part-04-training-system/29-sft.md` 的“Rollout-conditioned Distillation 应按证据归因，而不是整段照抄”。正文约第 200 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：Hindsight Hint Distillation 从当前 Agent 失败 rollout 生成针对性 hint，再蒸馏成功轨迹，改变 agentic SFT 的数据生成闭环。 判定：**Integrate — Applied; independent post-write review pending**。

### [When Looking Is Not Enough: Visual Attention Structure Reveals Hallucination in MLLMs](https://arxiv.org/html/2605.11559v1)

**准入：** attention-spectrum sensor 将多模态幻觉检测与 decoding correction 绑定到可观测的视觉注意力结构。

<!-- review:SF-2026-ARXIV-2605-11559:start -->
#### When Looking Is Not Enough: Visual Attention Structure Reveals Hallucination in MLLMs

**问题与旧基线。** attention-spectrum sensor 将多模态幻觉检测与 decoding correction 绑定到可观测的视觉注意力结构。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3.2–§3.3 Empirical Sensor；§4.1–§4.5 LaSCD。Laplacian attention energy 选择视觉证据较强的层，再用层间对比 logits 修正生成；sensor 不拥有事实真值。

**Evaluation contract。** §5；多种 MLLM 与视觉问答/幻觉 benchmark。V3=2+2+2=6；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** §6 与 Appendix C：依赖 grid visual token，未覆盖 reasoning-intensive task 或更大模型。

**Trade-off / failure / fallback。** 增加层选择、校准与额外 forward 成本，attention 相关性可能失效；信号不稳时回退 provenance-grounded evidence 与保守 abstention。

<!-- claim:SF-2026-ARXIV-2605-11559:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11559:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11559:end -->

**Books 对读：** `MULTIMODAL-REPRESENTATION` → `books/part-03-multimodal-world-models/23-multimodal-representation.md` 的“任务贡献与当前可靠性不能共用一个 Gate”。正文约第 296 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：attention-spectrum sensor 将多模态幻觉检测与 decoding correction 绑定到可观测的视觉注意力结构。 判定：**Integrate — Applied; independent post-write review pending**。

### [RIO: Flexible Real-Time Robot I/O for Cross-Embodiment Robot Learning](https://arxiv.org/html/2605.11564v1)

**准入：** Despite recent efforts to collect multi-task, multi-embodiment datasets, to design recipes for training Vision-Language-Action models (VLAs), and to showcase these models on different robot platforms, generalist cross-embodiment robot capabilities remains a largely elusive ideal.

<!-- review:SF-RIO-FLEXIBLE-REAL-TIME-ROBOT-I-O-FOR-CROSS-EMBODIMENT-ROBOT-LEARNING:start -->
#### RIO: Flexible Real-Time Robot I/O for Cross-Embodiment Robot Learning

问题与机制：Despite recent efforts to collect multi-task, multi-embodiment datasets, to design recipes for training Vision-Language-Action models (VLAs), and to showcase these models on different robot platforms, generalist cross-embodiment robot capabilities remains a largely elusive ideal.。机制 owner=`MULTIMODAL-EMBODIED-VLA`。
Method / identity：arXiv:2605.11564v1 — §III RIO design, nodes, middleware, stations and policy-inference interfaces。
Evaluation：arXiv:2605.11564v1 — §IV Evaluation across disclosed robot morphologies and hardware platforms。
Counterevidence / limitations：arXiv:2605.11564v1 — §V Limitations and Future Directions: single-embodiment fine-tuning, unresolved cross-embodiment generalization and dynamic-task gaps。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-RIO-FLEXIBLE-REAL-TIME-ROBOT-I-O-FOR-CROSS-EMBODIMENT-ROBOT-LEARNING:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `MULTIMODAL-EMBODIED-VLA` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-RIO-FLEXIBLE-REAL-TIME-ROBOT-I-O-FOR-CROSS-EMBODIMENT-ROBOT-LEARNING:end -->

Books Decision=`No Change — Existing Coverage`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-RIO-FLEXIBLE-REAL-TIME-ROBOT-I-O-FOR-CROSS-EMBODIMENT-ROBOT-LEARNING:end -->

**Books 对读：** `MULTIMODAL-EMBODIED-VLA` → `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的“State ownership 与 freshness”。books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md 的‘State ownership 与 freshness’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：Despite recent efforts to collect multi-task, multi-embodiment datasets, to design recipes for training Vision-Language-Action models (VLAs), and to showcase these models on different robot platforms, generalist cross-embodiment robot capabilities remains a largely elusive ideal. 判定：**No Change — Existing Coverage**。

### [OUI as a Structural Observable: Towards an Activation-Centric View of Neural Network Training](https://arxiv.org/html/2605.11570v1)

**准入：** loss/accuracy 只能从训练外部看到结果，无法及早定位层内结构是否进入坏区间；OUI 把 activation pattern 作为 label-free early observable。

<!-- review:SF-2026-ARXIV-2605-11570:start -->
#### OUI as a Structural Observable: Towards an Activation-Centric View of Neural Network Training

**问题与旧基线。** loss/accuracy 只能从训练外部看到结果，无法及早定位层内结构是否进入坏区间；OUI 把 activation pattern 作为 label-free early observable。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §2–§4 汇总 OUI 在 supervised weight decay、PPO learning-rate regime 与 layer-wise weight-decay control 中的定义和使用。 activation statistic 是早期 sensor，只能提出 schedule/regularization 调整；optimizer controller 与 held-out evidence 保留 commit authority。

**Evaluation contract。** 论文是跨既有实验的结构性综合：覆盖 supervised、PPO actor–critic 和 online control，但没有新增统一 benchmark 或因果消融。 V3=6（2+2+2）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** 这是 activation-centric position/synthesis evidence；不同网络、activation 与 scale 的可迁移阈值未建立，OUI 与最终泛化的因果关系未证明。

**Trade-off / failure / fallback。** 可提早预警，但增加逐层统计和校准；activation 稳定可能是假稳态，sensor 还可能被 architecture change 破坏。 OUI 未校准时继续以 loss、gradient、held-out 与 checkpoint recovery 联合判断，先 shadow 观察再允许控制器动作。

**Artifact。** Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-11570:start -->exact-v1 支持：支持‘activation 可作为补充训练状态’的假设，不支持单一 OUI 阈值、普适 early stopping 或自动调参最优性。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-11570:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-11570:end -->

**Books 对读：** `TRAIN-PRETRAINING` → `books/part-04-training-system/28-pretraining.md` 的“训练稳定性是多层系统问题”。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：loss/accuracy 只能从训练外部看到结果，无法及早定位层内结构是否进入坏区间；OUI 把 activation pattern 作为 label-free early observable。 判定：**Integrate — Applied; independent post-write review pending**。

### [BitLM: Unlocking Multi-Token Language Generation with Bitwise Continuous Diffusion](https://arxiv.org/html/2605.11577v1)

**准入：** We propose BitLM, a language model that represents each token as a fixed-length binary code and employs a lightweight diffusion head to denoise multiple tokens in parallel within each block.

<!-- review:SF-BITLM-UNLOCKING-MULTI-TOKEN-LANGUAGE-GENERATION-WITH-BITWISE-CONTINUOUS-:start -->
#### BitLM: Unlocking Multi-Token Language Generation with Bitwise Continuous Diffusion

问题与机制：We propose BitLM, a language model that represents each token as a fixed-length binary code and employs a lightweight diffusion head to denoise multiple tokens in parallel within each block.。机制 owner=`MULTIMODAL-GENERATIVE-PARADIGMS`。
全文定位：`arXiv:2605.11577v1 HTML — §3 BitLM block-causal binary diffusion objective`；evaluation=`arXiv:2605.11577v1 — §4 text-generation experiments and ablations`；limitations/counterevidence=`arXiv:2605.11577v1 — §5 limitations: model scale, sampler and latency contract`。
<!-- claim:SF-BITLM-UNLOCKING-MULTI-TOKEN-LANGUAGE-GENERATION-WITH-BITWISE-CONTINUOUS-:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-BITLM-UNLOCKING-MULTI-TOKEN-LANGUAGE-GENERATION-WITH-BITWISE-CONTINUOUS-:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-BITLM-UNLOCKING-MULTI-TOKEN-LANGUAGE-GENERATION-WITH-BITWISE-CONTINUOUS-:end -->

**Books 对读：** `MULTIMODAL-GENERATIVE-PARADIGMS` → `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的“Editable tokens 与 commit boundary”。books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md 的‘Editable tokens 与 commit boundary’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We propose BitLM, a language model that represents each token as a fixed-length binary code and employs a lightweight diffusion head to denoise multiple tokens in parallel within each block. 判定：**No Change — Existing Coverage**。

### [Ada-MK: Adaptive MegaKernel Optimization via Automated DAG-based Search for LLM Inference](https://arxiv.org/html/2605.11581v1)

**准入：** However, existing MegaKernel implementations face a fundamental tension between portability and efficiency on resource-constrained GPUs such as NVIDIA Ada: hand-tuned solutions are tightly coupled to specific architectures and lack portability, while auto-compiled approaches introduce runtime dynamic scheduling whose branch penalties are unacceptable…

<!-- review:SF-ADA-MK-ADAPTIVE-MEGAKERNEL-OPTIMIZATION-VIA-AUTOMATED-DAG-BASED-SEARCH-F:start -->
#### Ada-MK: Adaptive MegaKernel Optimization via Automated DAG-based Search for LLM Inference

问题与机制：However, existing MegaKernel implementations face a fundamental tension between portability and efficiency on resource-constrained GPUs such as NVIDIA Ada: hand-tuned solutions are tightly coupled to specific architectures and lack portability, while auto-compiled approaches introduce runtime dynamic scheduling whose branch penalties are unacceptable…。机制 owner=`INFER-TENSORRT-LLM`。
全文定位：`arXiv:2605.11581v1 HTML — §3 Ada-MK compile-time DAG search and MegaKernel construction`；evaluation=`arXiv:2605.11581v1 — §4 kernel/runtime evaluation`；limitations/counterevidence=`arXiv:2605.11581v1 — §5 limitations: operator set, accelerator and search-cost scope`。
<!-- claim:SF-ADA-MK-ADAPTIVE-MEGAKERNEL-OPTIMIZATION-VIA-AUTOMATED-DAG-BASED-SEARCH-F:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-ADA-MK-ADAPTIVE-MEGAKERNEL-OPTIMIZATION-VIA-AUTOMATED-DAG-BASED-SEARCH-F:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-ADA-MK-ADAPTIVE-MEGAKERNEL-OPTIMIZATION-VIA-AUTOMATED-DAG-BASED-SEARCH-F:end -->

**Books 对读：** `INFER-TENSORRT-LLM` → `books/part-05-inference-system/49-tensorrt-llm.md` 的“从逐 Kernel Launch 到 Persistent Executor”。现有段说明 persistent executor 和 typed plan，却未形成‘固定配置时将 DAG 决策提前、动态配置时保留 runtime path’这一 portability–latency 分支。 新证据增量：固定 deployment configuration 允许把 MegaKernel DAG 的 dynamic scheduling 从 runtime branch 上提到 compile-time search，同时以 shared-memory constraint/K-splitting适配 Ada GPU。 判定：**Integrate — Applied; independent post-write review pending**。

### [SoK: Unlearnability and Unlearning for Model Dememorization](https://arxiv.org/html/2605.11592v1)

**准入：** unlearnability 与 unlearning 共享 shallow dememorization 风险且会相互干扰，单阶段遗忘分数不能证明 knowledge withholding。

<!-- review:SF-2026-ARXIV-2605-11592:start -->
#### SoK: Unlearnability and Unlearning for Model Dememorization

问题、旧路径与约束变化：unlearnability 与 unlearning 共享 shallow dememorization 风险且会相互干扰，单阶段遗忘分数不能证明 knowledge withholding。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§3–§5 taxonomy/mechanisms。canonical owner=`PLATFORM-SECURITY`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§6 Experiments and §7 guarantees。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§8 Conclusion；无独立 Limitations，SoK/实验范围不构成通用删除证明。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11592:start -->exact-v1 支持：unlearnability 与 unlearning 共享 shallow dememorization 风险且会相互干扰，单阶段遗忘分数不能证明 knowledge withholding。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11592:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-11592:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“Unlearning 必须分开参数擦除与推理拒答”。`books/part-06-ai-infrastructure/72-security.md` 的“Unlearning 必须分开参数擦除与推理拒答”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：unlearnability 与 unlearning 共享 shallow dememorization 风险且会相互干扰，单阶段遗忘分数不能证明 knowledge withholding。 判定：**Integrate — Applied; independent post-write review pending**。

### [GAR: Carbon-Aware Routing for LLM Inference via Constrained Optimization](https://arxiv.org/html/2605.11603v1)

**准入：** To address this gap, we introduce Green-Aware Routing (GAR), a constrained multi-objective optimization framework that minimizes per-request CO2 emissions subject to explicit accuracy floors and p95-latency service-level objectives (SLOs).

<!-- review:SF-GAR-CARBON-AWARE-ROUTING-FOR-LLM-INFERENCE-VIA-CONSTRAINED-OPTIMIZATION:start -->
#### GAR: Carbon-Aware Routing for LLM Inference via Constrained Optimization

问题与机制：To address this gap, we introduce Green-Aware Routing (GAR), a constrained multi-objective optimization framework that minimizes per-request CO2 emissions subject to explicit accuracy floors and p95-latency service-level objectives (SLOs).。机制 owner=`INFER-SCHEDULING`。
全文定位：`arXiv:2605.11603v1 HTML — §3 GAR constrained carbon-aware routing`；evaluation=`arXiv:2605.11603v1 — §4 energy/latency evaluation`；limitations/counterevidence=`arXiv:2605.11603v1 — §5 limitations: grid signal, model mix and SLO assumptions`。
<!-- claim:SF-GAR-CARBON-AWARE-ROUTING-FOR-LLM-INFERENCE-VIA-CONSTRAINED-OPTIMIZATION:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-GAR-CARBON-AWARE-ROUTING-FOR-LLM-INFERENCE-VIA-CONSTRAINED-OPTIMIZATION:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-GAR-CARBON-AWARE-ROUTING-FOR-LLM-INFERENCE-VIA-CONSTRAINED-OPTIMIZATION:end -->

**Books 对读：** `INFER-SCHEDULING` → `books/part-05-inference-system/56-inference-scheduling.md` 的“目标函数不止吞吐”。books/part-05-inference-system/56-inference-scheduling.md 的‘目标函数不止吞吐’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：To address this gap, we introduce Green-Aware Routing (GAR), a constrained multi-objective optimization framework that minimizes per-request CO2 emissions subject to explicit accuracy floors and p95-latency service-level objectives (SLOs). 判定：**No Change — Existing Coverage**。

### [Keep What Audio Cannot Say: Context-Preserving Token Pruning for Omni-LLMs](https://arxiv.org/html/2605.11605v1)

**准入：** audio-explainability-aware pruning 将 Omni-LLM 的 visual token 保留规则从单模态重要性改为跨模态冗余条件。

<!-- review:SF-2026-ARXIV-2605-11605:start -->
#### Keep What Audio Cannot Say: Context-Preserving Token Pruning for Omni-LLMs

**问题与旧基线。** audio-explainability-aware pruning 将 Omni-LLM 的 visual token 保留规则从单模态重要性改为跨模态冗余条件。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §2.2 Audio-guided Token Selection；§2.3 Depth-score Temporal Merging。audio predictor 标识可由声音解释的视觉内容，只移除跨模态冗余 token；depth score 再合并时间片段。

**Evaluation contract。** §3；六个 audio-visual benchmark、效率实验及简单 online variant。V3=2+2+2=6；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** Appendix D.2 Limitations；结论依赖音频预测器、受测模型与视频结构。

**Trade-off / failure / fallback。** 节省 token/compute 但会误删音频未能表达的空间细节，且 predictor drift 会改变状态；不确定时保留完整 visual state 或提高预算。

<!-- claim:SF-2026-ARXIV-2605-11605:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11605:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11605:end -->

**Books 对读：** `MULTIMODAL-REPRESENTATION` → `books/part-03-multimodal-world-models/23-multimodal-representation.md` 的“固定预算要先分配信息责任，再选择具体 Token”。正文约第 254 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：audio-explainability-aware pruning 将 Omni-LLM 的 visual token 保留规则从单模态重要性改为跨模态冗余条件。 判定：**Integrate — Applied; independent post-write review pending**。

### [PRISM: A Geometric Risk Bound that Decomposes Drift into Scale, Shape, and Head](https://arxiv.org/html/2605.11608v1)

**准入：** PRISM 将 post-training model drift 分解为 scale、shape 与 output-head 三轴，并把诊断轴映射到不同修复选择。

<!-- review:SF-2026-ARXIV-2605-11608:start -->
#### PRISM: A Geometric Risk Bound that Decomposes Drift into Scale, Shape, and Head

**问题与旧基线。** PRISM 将 post-training model drift 分解为 scale、shape 与 output-head 三轴，并把诊断轴映射到不同修复选择。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3 Unified Risk Bound；§3.3 Three Diagnostic Axes；§3.5 Shape Regularization。几何 risk-gap upper bound 保存 target/variant/head identity，三轴分别诊断 scale、shape 与 head divergence。

**Evaluation contract。** §4–§5；两类模型、五个 benchmark、quantization/LoRA/GGUF variants。V3=2+2+3=7；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** §6 Discussion；bound/calibration、near-isometry、模型与 variant 范围限制，未提供生产风险保证。

**Trade-off / failure / fallback。** 提供可操作诊断但依赖表示访问、对齐和校准假设；假设不成立时回退 task-level held-out evaluation。

<!-- claim:SF-2026-ARXIV-2605-11608:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11608:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11608:end -->

**Books 对读：** `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md` 的“第一个不变量：评估声明必须绑定完整对象”。正文约第 153 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：PRISM 将 post-training model drift 分解为 scale、shape 与 output-head 三轴，并把诊断轴映射到不同修复选择。 判定：**Integrate — Applied; independent post-write review pending**。

### [Nice Fold or Hero Call: Learning Budget-Efficient Thinking for Adaptive Reasoning](https://arxiv.org/html/2605.11625v1)

**准入：** reasoning budget 应按 solvability 的预期回报而非 perceived difficulty 分配，并显式允许 solve/fold/hero-call。

<!-- review:SF-2026-ARXIV-2605-11625:start -->
#### Nice Fold or Hero Call: Learning Budget-Efficient Thinking for Adaptive Reasoning

问题、旧路径与约束变化：reasoning budget 应按 solvability 的预期回报而非 perceived difficulty 分配，并显式允许 solve/fold/hero-call。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§3 Method。canonical owner=`INFER-SCHEDULING`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§4 Experiments。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：Appendix G Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11625:start -->exact-v1 支持：reasoning budget 应按 solvability 的预期回报而非 perceived difficulty 分配，并显式允许 solve/fold/hero-call。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11625:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-11625:end -->

**Books 对读：** `INFER-SCHEDULING` → `books/part-05-inference-system/56-inference-scheduling.md` 的“Reasoning Budget 必须进入调度与评估身份”。`books/part-05-inference-system/56-inference-scheduling.md` 的“Reasoning Budget 必须进入调度与评估身份”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：reasoning budget 应按 solvability 的预期回报而非 perceived difficulty 分配，并显式允许 solve/fold/hero-call。 判定：**Integrate — Applied; independent post-write review pending**。

### [Safety Context Injection: Inference-Time Safety Alignment via Static Filtering and Agentic Analysis](https://arxiv.org/html/2605.11664v1)

**准入：** inference safety 将 assessment 与 generation 分离，并在 static filter 与 agentic analyzer 之间交换 latency、context coverage 与攻击面。

<!-- review:SF-2026-ARXIV-2605-11664:start -->
#### Safety Context Injection: Inference-Time Safety Alignment via Static Filtering and Agentic Analysis

问题、旧路径与约束变化：inference safety 将 assessment 与 generation 分离，并在 static filter 与 agentic analyzer 之间交换 latency、context coverage 与攻击面。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§4 Methodology。canonical owner=`PLATFORM-SECURITY`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§5 Experiments。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§6 Conclusion；无独立 Limitations，黑盒模型与受测攻击集限定结论。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11664:start -->exact-v1 支持：inference safety 将 assessment 与 generation 分离，并在 static filter 与 agentic analyzer 之间交换 latency、context coverage 与攻击面。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11664:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-11664:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“Pre-guard 可以前移，但最终 Authority 不能前移给 Draft Model”。`books/part-06-ai-infrastructure/72-security.md` 的“Pre-guard 可以前移，但最终 Authority 不能前移给 Draft Model”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：inference safety 将 assessment 与 generation 分离，并在 static filter 与 agentic analyzer 之间交换 latency、context coverage 与攻击面。 判定：**Integrate — Applied; independent post-write review pending**。

### [Evolutionary Task Discovery: Advancing Reasoning Frontiers via Skill Composition and Complexity Scaling](https://arxiv.org/html/2605.11666v1)

**准入：** 无结构 mutation 会导致合成 reasoning task 同质化；EvoTD 以 skill × complexity 双轴、crossover/mutation 和 policy-relative ZPD 组织 curriculum。

<!-- review:SF-2026-ARXIV-2605-11666:start -->
#### Evolutionary Task Discovery: Advancing Reasoning Frontiers via Skill Composition and Complexity Scaling

**问题与旧基线。** 无结构 mutation 会导致合成 reasoning task 同质化；EvoTD 以 skill × complexity 双轴、crossover/mutation 和 policy-relative ZPD 组织 curriculum。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §2 Method：dual-axis manifold、Crossover、Parametric Mutation 与动态 Zone of Proximal Development filter。 生成器提出 skill composition，current policy 的通过状态约束 learnable region，数据 control plane 决定入库。

**Evaluation contract。** §3 Experiments：跨作者披露的模型架构、pretraining regime 与 scale；代码入口为 https://github.com/liqinye/EvoTD。 V3=6（2+2+2）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；skill ontology、complexity parameter、verifier 与 ZPD estimator 都绑定受测 reasoning setting。

**Trade-off / failure / fallback。** 扩大覆盖会引入 ontology 偏差、合成污染、难度估计滞后和 verifier overfit。 结构化算子不可靠时保留固定 mixture、真实数据 floor、人工/独立 verifier 与 failure-replay curriculum。

**Artifact。** https://github.com/liqinye/EvoTD；未确认与 exact-v1 绑定的 immutable commit。

<!-- claim:SF-2026-ARXIV-2605-11666:start -->exact-v1 支持：现有正文已明确内容/能力/环境 coverage、组合算子和 policy-relative sweet spot；exact-v1 不再产生新的 owner 或命题。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-11666:end -->

Books Decision=`No Change — Existing Coverage`；作者未修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11666:end -->

**Books 对读：** `TRAIN-DATA` → `books/part-04-training-system/27-data.md` 的“从样本数量到 Coverage Contract：Curriculum 必须同时管理内容、能力与环境”。现有正文已语义承载该机制、边界和 fallback。 新证据增量：无结构 mutation 会导致合成 reasoning task 同质化；EvoTD 以 skill × complexity 双轴、crossover/mutation 和 policy-relative ZPD 组织 curriculum。 判定：**No Change — Existing Coverage**。

### [OOM-Free Alpamayo via CPU-GPU Memory Swapping for Vision-Language-Action Models](https://arxiv.org/html/2605.11678v1)

**准入：** We present a framework, which enables memory-efficient VLA inference on VRAM-constrained GPUs through system-level optimization alone, without model modification.

<!-- review:SF-OOM-FREE-ALPAMAYO-VIA-CPU-GPU-MEMORY-SWAPPING-FOR-VISION-LANGUAGE-ACTION:start -->
#### OOM-Free Alpamayo via CPU-GPU Memory Swapping for Vision-Language-Action Models

问题与机制：We present a framework, which enables memory-efficient VLA inference on VRAM-constrained GPUs through system-level optimization alone, without model modification.。机制 owner=`INFER-GPU-MEMORY`。
全文定位：`arXiv:2605.11678v1 HTML — §3 CPU-GPU demand-layered VLA execution`；evaluation=`arXiv:2605.11678v1 — §4 latency/memory evaluation`；limitations/counterevidence=`arXiv:2605.11678v1 — §5 limitations: platform, policy model and transfer overhead`。
<!-- claim:SF-OOM-FREE-ALPAMAYO-VIA-CPU-GPU-MEMORY-SWAPPING-FOR-VISION-LANGUAGE-ACTION:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-OOM-FREE-ALPAMAYO-VIA-CPU-GPU-MEMORY-SWAPPING-FOR-VISION-LANGUAGE-ACTION:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-OOM-FREE-ALPAMAYO-VIA-CPU-GPU-MEMORY-SWAPPING-FOR-VISION-LANGUAGE-ACTION:end -->

**Books 对读：** `INFER-GPU-MEMORY` → `books/part-05-inference-system/54-gpu-memory.md` 的“扩展层级”。books/part-05-inference-system/54-gpu-memory.md 的‘扩展层级’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We present a framework, which enables memory-efficient VLA inference on VRAM-constrained GPUs through system-level optimization alone, without model modification. 判定：**No Change — Existing Coverage**。

### [Robust LLM Unlearning Against Relearning Attacks: The Minor Components in Representations Matter](https://arxiv.org/html/2605.11685v1)

**准入：** unlearning 只修改 dominant representation components 容易被 relearning 逆转，minor components 也必须进入删除与攻击验收。

<!-- review:SF-2026-ARXIV-2605-11685:start -->
#### Robust LLM Unlearning Against Relearning Attacks: The Minor Components in Representations Matter

问题、旧路径与约束变化：unlearning 只修改 dominant representation components 容易被 relearning 逆转，minor components 也必须进入删除与攻击验收。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§3 Mechanism and §4 Method。canonical owner=`PLATFORM-SECURITY`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§5 Experiments。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：Appendix A Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11685:start -->exact-v1 支持：unlearning 只修改 dominant representation components 容易被 relearning 逆转，minor components 也必须进入删除与攻击验收。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11685:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-11685:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“Unlearning 必须分开参数擦除与推理拒答”。`books/part-06-ai-infrastructure/72-security.md` 的“Unlearning 必须分开参数擦除与推理拒答”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：unlearning 只修改 dominant representation components 容易被 relearning 逆转，minor components 也必须进入删除与攻击验收。 判定：**Integrate — Applied; independent post-write review pending**。

### [GRAFT: Graph-Tokenized LLMs for Tool Planning](https://arxiv.org/html/2605.11706v1)

**准入：** 把 tool graph 作为检索/序列化 prompt 只能做语义 matching，早期选错后会进入非法 graph state；GRAFT 将节点与有向依赖编码进模型表示。

<!-- review:SF-2026-ARXIV-2605-11706:start -->
#### GRAFT: Graph-Tokenized LLMs for Tool Planning

**问题与旧基线。** 把 tool graph 作为检索/序列化 prompt 只能做语义 matching，早期选错后会进入非法 graph state；GRAFT 将节点与有向依赖编码进模型表示。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §3 Method：tool node special tokens、directed-dependency training 与 on-policy tool-context distillation。 graph token 表示计划约束，on-policy samples 暴露自身漂移；模型只提出 plan，workflow/runtime 仍验证依赖与执行 commit。

**Evaluation contract。** §4 Experiments：exact sequence matching 与 dependency legality；范围为作者 tool-planning benchmarks/models。 V3=7（3+2+2）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；图变化、未见 tool、真实执行错误和环境 side effect 均未被 benchmark 完整覆盖。

**Trade-off / failure / fallback。** 减少 prompt graph 搬运却增加 tokenizer/model coupling、graph versioning 与 retraining；错误内化会更难被观察。 动态图或置信不足时回退外部 typed DAG、constraint checker、stepwise replan 与执行前 legality gate。

**Artifact。** Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-11706:start -->exact-v1 支持：只支持所测静态 tool graph 与 legality/equality 指标；不证明真实工具成功、权限安全或动态图一致性。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-11706:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-11706:end -->

**Books 对读：** `AGENT-PLANNING` → `books/part-07-agent/79-planning.md` 的“从目标到状态图”。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：把 tool graph 作为检索/序列化 prompt 只能做语义 matching，早期选错后会进入非法 graph state；GRAFT 将节点与有向依赖编码进模型表示。 判定：**Integrate — Applied; independent post-write review pending**。

### [Toward Stable Value Alignment: Introducing Independent Modules for Consistent Value Guidance](https://arxiv.org/html/2605.11712v1)

**准入：** 独立 value module 与 bridge token 将 alignment steering 从修改 backbone 权重改为可刷新的外部 value state。

<!-- review:SF-2026-ARXIV-2605-11712:start -->
#### Toward Stable Value Alignment: Introducing Independent Modules for Consistent Value Guidance

**问题与旧基线。** 独立 value module 与 bridge token 将 alignment steering 从修改 backbone 权重改为可刷新的外部 value state。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3 Independent Value Policy、SVGT and Bridge Tokens。冻结 backbone 的 hidden state 送入独立 value module，bridge token 将方向注入生成并可动态刷新。

**Evaluation contract。** §4；四个 backbones、公开 safety data 和三次随机种子。V3=2+2+2=6；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** Appendix E：约 50% latency、单维 value 与文化偏差等限制。

**Trade-off / failure / fallback。** 可独立升级 value policy，但增加约 50% latency、表示耦合和价值压缩风险；低风险场景可保留离线 alignment，异常时撤销 bridge intervention。

<!-- claim:SF-2026-ARXIV-2605-11712:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11712:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11712:end -->

**Books 对读：** `TRAIN-RLHF` → `books/part-04-training-system/31-rlhf.md` 的“从持久权重更新到条件化 Activation Intervention”。正文约第 353 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：独立 value module 与 bridge token 将 alignment steering 从修改 backbone 权重改为可刷新的外部 value state。 判定：**Integrate — Applied; independent post-write review pending**。

### [SafeSteer: A Decoding-level Defense Mechanism for Multimodal Large Language Models](https://arxiv.org/html/2605.11716v1)

**准入：** decoding-level probe 将 MLLM safety 从生成后过滤前移到候选 token hidden-state 的在线筛选。

<!-- review:SF-2026-ARXIV-2605-11716:start -->
#### SafeSteer: A Decoding-level Defense Mechanism for Multimodal Large Language Models

**问题与旧基线。** decoding-level probe 将 MLLM safety 从生成后过滤前移到候选 token hidden-state 的在线筛选。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §4 Decoding Probe and Modal Semantic Vector。logistic probe 检查 top-k candidate hidden states，不安全时重采样；跨模态 safety vector 是 sensor，gateway policy 保留 commit authority。

**Evaluation contract。** §5；三个 safety datasets 与多种 attack/utility 设置。V3=2+2+2=6；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** Limitations：text safety transfer 可能降低 robustness；gradual correction 与 top-k 受限。

**Trade-off / failure / fallback。** 提前拦截换 probe drift、top-k 漏检和语义干预副作用；探针置信不足时回退确定性 policy、输出后审计或人工 gate。

<!-- claim:SF-2026-ARXIV-2605-11716:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11716:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11716:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“Learned Security Sensor 与 Reference Monitor 必须分层”。正文约第 597 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：decoding-level probe 将 MLLM safety 从生成后过滤前移到候选 token hidden-state 的在线筛选。 判定：**Integrate — Applied; independent post-write review pending**。

### [EPIC: Efficient Predicate-Guided Inference-Time Control for Compositional Text-to-Image Generation](https://arxiv.org/html/2605.11722v1)

**准入：** 一次生成无法可靠满足多对象、计数、属性与关系；EPIC 将 prompt 固化为 typed visual program，并以 predicate failure 路由 edit 或 resample。

<!-- review:SF-2026-ARXIV-2605-11722:start -->
#### EPIC: Efficient Predicate-Guided Inference-Time Control for Compositional Text-to-Image Generation

**问题与旧基线。** 一次生成无法可靠满足多对象、计数、属性与关系；EPIC 将 prompt 固化为 typed visual program，并以 predicate failure 路由 edit 或 resample。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §3 Method：一次解析得到固定 object variables/predicates，逐图验证；local failure 定向编辑，global failure 重采样，含 acceptance 与 fallback。 visual program 拥有待满足 contract，verifier 只产出 predicate evidence，controller 选择下一 action，最终 acceptance 仍需独立 gate。

**Evaluation contract。** §4 及 Appendix C/D：GenEval2 主实验和预算扫掠，另有 DrawBench/GenEval 审计；比较 generator/editor 执行、MLLM calls/tokens。 V3=7（3+2+2）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** §5 与 Appendix E：visual program 与 verifier 可能错，分解条件不完备；效果依赖具体 generator/editor/verifier 与最大预算。

**Trade-off / failure / fallback。** 可定位局部失败但增加 parse/verifier/编辑成本；错误 program 会稳定地优化错误目标，循环还可能耗尽预算。 verifier 不确定时回退 single-pass 或 best-of-N，保留原 prompt、人工检查和最大 retry/cost budget。

**Artifact。** Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-11722:start -->exact-v1 支持：只证明披露模型、predicate 集和 benchmark 的 alignment/cost；不证明开放世界视觉事实、任意 prompt 可分解或 verifier 正确。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-11722:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-11722:end -->

**Books 对读：** `MULTIMODAL-GENERATIVE-PARADIGMS` → `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的“从一次生成到 Plan → Generate → Validate → Retry”。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：一次生成无法可靠满足多对象、计数、属性与关系；EPIC 将 prompt 固化为 typed visual program，并以 predicate failure 路由 edit 或 resample。 判定：**Integrate — Applied; independent post-write review pending**。

### [Allegory of the Cave: Measurement-Grounded Vision-Language Learning](https://arxiv.org/html/2605.11727v1)

**准入：** measurement-domain input 把 ISP 前原始传感证据、camera conditioning 与 exposure supervision 纳入 VLM representation identity。

<!-- review:SF-2026-ARXIV-2605-11727:start -->
#### Allegory of the Cave: Measurement-Grounded Vision-Language Learning

**问题与旧基线。** measurement-domain input 把 ISP 前原始传感证据、camera conditioning 与 exposure supervision 纳入 VLM representation identity。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3 Measurement-grounded Vision-Language Learning；§4 PRISM-VL。模型在显示域之外读取 measurement-domain signal，并携带 camera/exposure 条件，使感知状态保留采集过程。

**Evaluation contract。** §5；多种 VLM comparison 与 measurement-domain tasks。V3=2+2+2=6；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；相机、任务、数据和受测模型限制结论。

**Trade-off / failure / fallback。** 保留原始证据提高可校准性但增加传感器接口、数据与模型复杂度；原始信号缺失时回退标准 ISP 表示并降低结论强度。

<!-- claim:SF-2026-ARXIV-2605-11727:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11727:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11727:end -->

**Books 对读：** `MULTIMODAL-REPRESENTATION` → `books/part-03-multimodal-world-models/23-multimodal-representation.md` 的“时间、空间与 provenance 必须进入状态”。正文约第 342 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：measurement-domain input 把 ISP 前原始传感证据、camera conditioning 与 exposure supervision 纳入 VLM representation identity。 判定：**Integrate — Applied; independent post-write review pending**。

### [Persona-Conditioned Adversarial Prompting: Multi-Identity Red-Teaming for Adversarial Discovery and Mitigation](https://arxiv.org/html/2605.11730v1)

**准入：** persona-conditioned adversarial search 连接 attack discovery、带 metadata 的 defense dataset 与 adapter fine-tuning。

<!-- review:SF-2026-ARXIV-2605-11730:start -->
#### Persona-Conditioned Adversarial Prompting: Multi-Identity Red-Teaming for Adversarial Discovery and Mitigation

**问题与旧基线。** persona-conditioned adversarial search 连接 attack discovery、带 metadata 的 defense dataset 与 adapter fine-tuning。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3 TAP Background；§4 Method；§6 Dataset Generation and Mitigation。并行 persona/strategy 搜索生成 attack candidates，metadata 与 guard/evaluator 形成筛选后再进入 defense tuning。

**Evaluation contract。** §5 与 Appendix B/C；GPT-OSS 120B、自动 evaluator、adapter fine-tuning。V3=2+2+2=6；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** §8 Limitations：persona/strategy、自动评分、目标模型与 transfer 范围受限。

**Trade-off / failure / fallback。** 扩大多样性但可能 self-confirm、放大 evaluator blind spot；正文已要求 generator、guard、policy taxonomy、人工切片和 deployment gate 分离保存。

<!-- claim:SF-2026-ARXIV-2605-11730:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11730:end -->

Books Decision=`No Change — Existing Coverage`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11730:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“安全数据闭环还可由当前 policy 生成 adversarial candidates（正文段落）”。正文约第 419 行已逐命题覆盖该机制、代价与 fallback；Review notes 不参与覆盖判断。 新证据增量：persona-conditioned adversarial search 连接 attack discovery、带 metadata 的 defense dataset 与 adapter fine-tuning。 判定：**No Change — Existing Coverage**。

### [Position: LLM Inference Should Be Evaluated as Energy-to-Token Production](https://arxiv.org/html/2605.11733v1)

**准入：** quality/SLO-conditioned energy-to-token contract 把 compute、delivered power、cooling、PUE 与 utilization 放进同一产能上界。

<!-- review:SF-2026-ARXIV-2605-11733:start -->
#### Position: LLM Inference Should Be Evaluated as Energy-to-Token Production

问题、旧路径与约束变化：quality/SLO-conditioned energy-to-token contract 把 compute、delivered power、cooling、PUE 与 utilization 放进同一产能上界。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§2 token production function, §3 power constraint and §4 system optimizations。canonical owner=`PLATFORM-COST`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：position-paper examples and alternatives in §6。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：Appendix A Scope and Limitations；价格仅作方向性动机。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11733:start -->exact-v1 支持：quality/SLO-conditioned energy-to-token contract 把 compute、delivered power、cooling、PUE 与 utilization 放进同一产能上界。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11733:end -->

Books Decision=`No Change — Existing Coverage`；作者只形成命题比较与 root serial queue，不直接修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11733:end -->

**Books 对读：** `PLATFORM-COST` → `books/part-06-ai-infrastructure/70-cost.md` 的“Installed Power 不是可部署 AI Capacity”。`books/part-06-ai-infrastructure/70-cost.md` 的“Installed Power 不是可部署 AI Capacity”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：quality/SLO-conditioned energy-to-token contract 把 compute、delivered power、cooling、PUE 与 utilization 放进同一产能上界。 判定：**No Change — Existing Coverage**。

### [Training-Inference Consistent Segmented Execution for Long-Context LLMs](https://arxiv.org/html/2605.11744v1)

**准入：** Based on this insight, we propose a training-inference consistent segment-level generation framework, in which training and inference follow the same segment-level forward execution semantics.

<!-- review:SF-TRAINING-INFERENCE-CONSISTENT-SEGMENTED-EXECUTION-FOR-LONG-CONTEXT-LLMS:start -->
#### Training-Inference Consistent Segmented Execution for Long-Context LLMs

问题与机制：Based on this insight, we propose a training-inference consistent segment-level generation framework, in which training and inference follow the same segment-level forward execution semantics.。机制 owner=`INFER-KV-CACHE`。
全文定位：`arXiv:2605.11744v1 HTML — §3 segmented training/inference-consistent long-context state`；evaluation=`arXiv:2605.11744v1 — §4 long-context quality/runtime evaluation`；limitations/counterevidence=`arXiv:2605.11744v1 — §5 limitations: segment policy, model and cache scope`。
<!-- claim:SF-TRAINING-INFERENCE-CONSISTENT-SEGMENTED-EXECUTION-FOR-LONG-CONTEXT-LLMS:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-TRAINING-INFERENCE-CONSISTENT-SEGMENTED-EXECUTION-FOR-LONG-CONTEXT-LLMS:end -->
Books Decision=`Integrate`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-TRAINING-INFERENCE-CONSISTENT-SEGMENTED-EXECUTION-FOR-LONG-CONTEXT-LLMS:end -->

**Books 对读：** `INFER-KV-CACHE` → `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 的“Segmented Execution 必须在训练与推理共享同一语义”。books/part-05-inference-system/45-why-kv-cache-speeds-up.md 的‘Segmented Execution 必须在训练与推理共享同一语义’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：Based on this insight, we propose a training-inference consistent segment-level generation framework, in which training and inference follow the same segment-level forward execution semantics. 判定：**Integrate — Already present in current Books**。

### [When Reasoning Traces Become Performative: Step-Level Evidence that Chain-of-Thought Is an Imperfect Oversight Channel](https://arxiv.org/html/2605.11746v1)

**准入：** Chain-of-thought (CoT) traces are increasingly used both to improve language model capability and to audit model behavior, implicitly assuming that the visible trace remains synchronized with the computation that determines the answer.

<!-- review:SF-WHEN-REASONING-TRACES-BECOME-PERFORMATIVE-STEP-LEVEL-EVIDENCE-THAT-CHAIN:start -->
#### When Reasoning Traces Become Performative: Step-Level Evidence that Chain-of-Thought Is an Imperfect Oversight Channel

问题与机制：Chain-of-thought (CoT) traces are increasingly used both to improve language model capability and to audit model behavior, implicitly assuming that the visible trace remains synchronized with the computation that determines the answer.。机制 owner=`PLATFORM-EVALUATION-SYSTEM`。
全文定位：`arXiv:2605.11746v1 HTML — §3 imperfect-oversight channel for chain-of-thought`；evaluation=`arXiv:2605.11746v1 — §4 monitor/evaluator experiments`；limitations/counterevidence=`arXiv:2605.11746v1 — §5 limitations: observability, evaluator and hidden-reasoning boundary`。
<!-- claim:SF-WHEN-REASONING-TRACES-BECOME-PERFORMATIVE-STEP-LEVEL-EVIDENCE-THAT-CHAIN:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-WHEN-REASONING-TRACES-BECOME-PERFORMATIVE-STEP-LEVEL-EVIDENCE-THAT-CHAIN:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-WHEN-REASONING-TRACES-BECOME-PERFORMATIVE-STEP-LEVEL-EVIDENCE-THAT-CHAIN:end -->

**Books 对读：** `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md` 的“Evaluation Identity 必须包含 Harness 与 Environment”。visible CoT 与 answer-determining computation 可能不同步；oversight contract 必须区分 trace readability、causal use 与 final behavior，而不能把可见文字当内部计算真值。 新证据增量：Chain-of-thought (CoT) traces are increasingly used both to improve language model capability and to audit model behavior, implicitly assuming that the visible trace remains synchronized with the computation that determines the answer. 判定：**Integrate — Applied; independent post-write review pending**。

### [DreamAvoid: Critical-Phase Test-Time Dreaming to Avoid Failures in VLA Policies](https://arxiv.org/html/2605.11750v1)

**准入：** critical-phase trigger、action proposals 与 short-horizon dream evaluator 形成 test-time VLA failure-avoidance gate，dream 只拥有候选排序权。

<!-- review:SF-2026-ARXIV-2605-11750:start -->
#### DreamAvoid: Critical-Phase Test-Time Dreaming to Avoid Failures in VLA Policies

问题、旧路径与约束变化：critical-phase trigger、action proposals 与 short-horizon dream evaluator 形成 test-time VLA failure-avoidance gate，dream 只拥有候选排序权。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§3 pilot and §4 Method。canonical owner=`MULTIMODAL-EMBODIED-VLA`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§5 real-world and §6 simulation。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§7 and Appendix F Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11750:start -->exact-v1 支持：critical-phase trigger、action proposals 与 short-horizon dream evaluator 形成 test-time VLA failure-avoidance gate，dream 只拥有候选排序权。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11750:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-11750:end -->

**Books 对读：** `MULTIMODAL-EMBODIED-VLA` → `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的“Reason–Imagine–Act 把内部 Rollout 变成 Proposal，而非执行权限”。`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的“Reason–Imagine–Act 把内部 Rollout 变成 Proposal，而非执行权限”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：critical-phase trigger、action proposals 与 short-horizon dream evaluator 形成 test-time VLA failure-avoidance gate，dream 只拥有候选排序权。 判定：**Integrate — Applied; independent post-write review pending**。

### [Behavioral Integrity Verification for AI Agent Skills](https://arxiv.org/html/2605.11770v1)

**准入：** Agent skills extend LLM agents with privileged third-party capabilities such as filesystem access, credentials, network calls, and shell execution.

<!-- review:SF-BEHAVIORAL-INTEGRITY-VERIFICATION-FOR-AI-AGENT-SKILLS:start -->
#### Behavioral Integrity Verification for AI Agent Skills

问题与机制：Agent skills extend LLM agents with privileged third-party capabilities such as filesystem access, credentials, network calls, and shell execution.。机制 owner=`AGENT-PLATFORM`。
全文定位：`arXiv:2605.11770v1 HTML — §3 behavioral-integrity verification for skills`；evaluation=`arXiv:2605.11770v1 — §4 tampering/compatibility evaluation`；limitations/counterevidence=`arXiv:2605.11770v1 — §5 limitations: behavioral oracle and environment coverage`。
<!-- claim:SF-BEHAVIORAL-INTEGRITY-VERIFICATION-FOR-AI-AGENT-SKILLS:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-BEHAVIORAL-INTEGRITY-VERIFICATION-FOR-AI-AGENT-SKILLS:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-BEHAVIORAL-INTEGRITY-VERIFICATION-FOR-AI-AGENT-SKILLS:end -->

**Books 对读：** `AGENT-PLATFORM` → `books/part-07-agent/84-agent-platform.md` 的“Skill Lifecycle 需要 Admission 与 Runtime 两个 Gate”。正文同时要求被审计 Skill 与实际执行 artifact 同一，并在运行前检查 principal、参数、环境、版本、副作用预算和 postcondition；这直接覆盖 privileged skill behavioral integrity。 新证据增量：Agent skills extend LLM agents with privileged third-party capabilities such as filesystem access, credentials, network calls, and shell execution. 判定：**No Change — Existing Coverage**。

### [Five Attacks on x402 Agentic Payment Protocol](https://arxiv.org/html/2605.11781v1)

**准入：** In this paper, we formally analyze x402 and empirically show that it is vulnerable in both design and implementation.

<!-- review:SF-FIVE-ATTACKS-ON-X402-AGENTIC-PAYMENT-PROTOCOL:start -->
#### Five Attacks on x402 Agentic Payment Protocol

问题与机制：In this paper, we formally analyze x402 and empirically show that it is vulnerable in both design and implementation.。机制 owner=`PLATFORM-SECURITY`。
Method / identity：arXiv:2605.11781v1 — §2 x402 models/protocol and threat model; §3 five authorization, binding, replay and web-layer attacks。
Evaluation：arXiv:2605.11781v1 — §4 Evaluation, including local chain, Base Sepolia, live endpoints and cross-implementation audit。
Counterevidence / limitations：arXiv:2605.11781v1 — §6.1 Security–Latency Tradeoff; §6.2 Threats to Validity; §6.5 Limitations and Future Work。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-FIVE-ATTACKS-ON-X402-AGENTIC-PAYMENT-PROTOCOL:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `PLATFORM-SECURITY` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-FIVE-ATTACKS-ON-X402-AGENTIC-PAYMENT-PROTOCOL:end -->

Books Decision=`Integrate`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-FIVE-ATTACKS-ON-X402-AGENTIC-PAYMENT-PROTOCOL:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“Canonical Action 与 Effect-time Authorization”。books/part-06-ai-infrastructure/72-security.md 的‘Canonical Action 与 Effect-time Authorization’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：In this paper, we formally analyze x402 and empirically show that it is vulnerable in both design and implementation. 判定：**Integrate — Already present in current Books**。

### [ROMER: Expert Replacement and Router Calibration for Robust MoE LLMs on Analog Compute-in-Memory Systems](https://arxiv.org/html/2605.11800v1)

**准入：** analog CIM noise 会同时破坏 expert load balance 与 clean-trained router，部署校准必须联合 expert replacement 和 router logits。

<!-- review:SF-2026-ARXIV-2605-11800:start -->
#### ROMER: Expert Replacement and Router Calibration for Robust MoE LLMs on Analog Compute-in-Memory Systems

问题、旧路径与约束变化：analog CIM noise 会同时破坏 expert load balance 与 clean-trained router，部署校准必须联合 expert replacement 和 router logits。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§2 Preliminary and §3 Methodology。canonical owner=`INFER-TENSORRT-LLM`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§4 Experiments。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§5 Conclusion；无独立 Limitations，real-chip-calibrated noise 不等于所有 CIM。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-11800:start -->exact-v1 支持：analog CIM noise 会同时破坏 expert load balance 与 clean-trained router，部署校准必须联合 expert replacement 和 router logits。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-11800:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-11800:end -->

**Books 对读：** `INFER-TENSORRT-LLM` → `books/part-05-inference-system/49-tensorrt-llm.md` 的“MoE 的 Calibration Identity 必须覆盖 Expert Activation Distribution”。`books/part-05-inference-system/49-tensorrt-llm.md` 的“MoE 的 Calibration Identity 必须覆盖 Expert Activation Distribution”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：analog CIM noise 会同时破坏 expert load balance 与 clean-trained router，部署校准必须联合 expert replacement 和 router logits。 判定：**Integrate — Applied; independent post-write review pending**。

### [Learning Action Manifold with Multi-view Latent Priors for Robotic Manipulation](https://arxiv.org/html/2605.11832v1)

**准入：** multi-view geometry prior、occlusion gate 与 action manifold expert 改变 VLA 的几何状态和动作表示。

<!-- review:SF-2026-ARXIV-2605-11832:start -->
#### Learning Action Manifold with Multi-view Latent Priors for Robotic Manipulation

**问题与旧基线。** multi-view geometry prior、occlusion gate 与 action manifold expert 改变 VLA 的几何状态和动作表示。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3 and Appendices B/C：Geometry Module、Gated Transformer and Action Manifold。单目与合成多视图建立几何 prior，occlusion gate 过滤不可靠证据，action manifold 将 state 映射到可执行方向。

**Evaluation contract。** §4；simulation benchmarks 与 real-robot evaluation。V3=2+2+2=6；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** §4H Limitations；受传感、场景、机器人与 action schema 限制。

**Trade-off / failure / fallback。** 几何显式化换 calibration、额外视图与模型复杂度；正文已明确坐标归一化、uncertainty、传统 estimator fallback 以及 action schema/controller 分权。

<!-- claim:SF-2026-ARXIV-2605-11832:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11832:end -->

Books Decision=`No Change — Existing Coverage`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11832:end -->

**Books 对读：** `MULTIMODAL-EMBODIED-VLA` → `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的“坐标系归一化是 Representation 到 Action Schema 的桥”。正文约第 29 行已逐命题覆盖该机制、代价与 fallback；Review notes 不参与覆盖判断。 新证据增量：multi-view geometry prior、occlusion gate 与 action manifold expert 改变 VLA 的几何状态和动作表示。 判定：**No Change — Existing Coverage**。

### [Gradient Clipping Beyond Vector Norms: A Spectral Approach for Matrix-Valued Parameters](https://arxiv.org/html/2605.11838v1)

**准入：** Motivated by this phenomenon, we propose spectral clipping, which stabilizes training by clamping singular values that exceed a threshold while preserving the singular directions.

<!-- review:SF-GRADIENT-CLIPPING-BEYOND-VECTOR-NORMS-A-SPECTRAL-APPROACH-FOR-MATRIX-VAL:start -->
#### Gradient Clipping Beyond Vector Norms: A Spectral Approach for Matrix-Valued Parameters

问题与机制：Motivated by this phenomenon, we propose spectral clipping, which stabilizes training by clamping singular values that exceed a threshold while preserving the singular directions.。机制 owner=`TRAIN-PRETRAINING`。
Method / identity：arXiv:2605.11838v1 — §3 spectral clipping; §4 convergence analysis; §5 randomized truncated-SVD implementation。
Evaluation：arXiv:2605.11838v1 — §6 Numerical Experiments, including §6.2 Shakespeare LLM and §6.3 GPT-2/FineWeb。
Counterevidence / limitations：arXiv:2605.11838v1 — no dedicated Limitations section; clipping bias, truncated-SVD approximation, heavy-tail/low-rank assumptions and evaluated task scale bound the result。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-GRADIENT-CLIPPING-BEYOND-VECTOR-NORMS-A-SPECTRAL-APPROACH-FOR-MATRIX-VAL:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `TRAIN-PRETRAINING` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-GRADIENT-CLIPPING-BEYOND-VECTOR-NORMS-A-SPECTRAL-APPROACH-FOR-MATRIX-VAL:end -->

Books Decision=`Integrate`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-GRADIENT-CLIPPING-BEYOND-VECTOR-NORMS-A-SPECTRAL-APPROACH-FOR-MATRIX-VAL:end -->

**Books 对读：** `TRAIN-PRETRAINING` → `books/part-04-training-system/28-pretraining.md` 的“Gradient Clipping 的正确边界与顺序”。books/part-04-training-system/28-pretraining.md 的‘Gradient Clipping 的正确边界与顺序’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：Motivated by this phenomenon, we propose spectral clipping, which stabilizes training by clamping singular values that exceed a threshold while preserving the singular directions. 判定：**Integrate — Already present in current Books**。

### [Probabilistic Calibration Is a Trainable Capability in Language Models](https://arxiv.org/html/2605.11845v1)

**准入：** We study whether this capability can be improved directly through fine-tuning.

<!-- review:SF-PROBABILISTIC-CALIBRATION-IS-A-TRAINABLE-CAPABILITY-IN-LANGUAGE-MODELS:start -->
#### Probabilistic Calibration Is a Trainable Capability in Language Models

问题与机制：We study whether this capability can be improved directly through fine-tuning.。机制 owner=`PLATFORM-EVALUATION-SYSTEM`。
Method / identity：arXiv:2605.11845v1 — §3 hard-target and soft-target calibration fine-tuning objectives。
Evaluation：arXiv:2605.11845v1 — §4 Experimental Setup and §5 Main Results。
Counterevidence / limitations：arXiv:2605.11845v1 — §6 Discussion and Limitations: synthetic distribution transfer, model/task coverage and downstream capability effects。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-PROBABILISTIC-CALIBRATION-IS-A-TRAINABLE-CAPABILITY-IN-LANGUAGE-MODELS:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `PLATFORM-EVALUATION-SYSTEM` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-PROBABILISTIC-CALIBRATION-IS-A-TRAINABLE-CAPABILITY-IN-LANGUAGE-MODELS:end -->

Books Decision=`No Change — Existing Coverage`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-PROBABILISTIC-CALIBRATION-IS-A-TRAINABLE-CAPABILITY-IN-LANGUAGE-MODELS:end -->

**Books 对读：** `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md` 的“Calibration Slice 必须包含 Language × Model Scale × Estimator Contract”。books/part-06-ai-infrastructure/66-evaluation-system.md 的‘Calibration Slice 必须包含 Language × Model Scale × Estimator Contract’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We study whether this capability can be improved directly through fine-tuning. 判定：**No Change — Existing Coverage**。

### [UniVLR: Unifying Text and Vision in Visual Latent Reasoning for Multimodal LLMs](https://arxiv.org/html/2605.11856v1)

**准入：** UniVLR 将文字 CoT 与辅助图像写入统一 visual canvas，再压缩为连续 latent reasoning state。

<!-- review:SF-2026-ARXIV-2605-11856:start -->
#### UniVLR: Unifying Text and Vision in Visual Latent Reasoning for Multimodal LLMs

**问题与旧基线。** UniVLR 将文字 CoT 与辅助图像写入统一 visual canvas，再压缩为连续 latent reasoning state。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §2 Unified Canvas、Latent Alignment and Continuous Autoregression。文本推理和中间图像先渲染为 canvas，编码为紧凑 latent token，最终答案仍通过 text path 输出。

**Evaluation contract。** §3；多个 VLM reasoning benchmarks 与消融。V3=2+1+2=5；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** §5：依赖 OCR/layout、可检查性较低、固定 token budget，仍需要外部工具。

**Trade-off / failure / fallback。** 跨模态中间状态更统一但降低可解释性并引入 OCR/layout bottleneck；复杂事实任务应保留文本证据与外部工具 fallback。

<!-- claim:SF-2026-ARXIV-2605-11856:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11856:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11856:end -->

**Books 对读：** `MULTIMODAL-REPRESENTATION` → `books/part-03-multimodal-world-models/23-multimodal-representation.md` 的“理解与生成也不必被迫共享全部参数”。正文约第 218 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：UniVLR 将文字 CoT 与辅助图像写入统一 visual canvas，再压缩为连续 latent reasoning state。 判定：**Integrate — Applied; independent post-write review pending**。

### [Beyond Parameter Aggregation: Semantic Consensus for Federated Fine-Tuning of LLMs](https://arxiv.org/html/2605.11857v1)

**准入：** We present a theoretical analysis and empirical results demonstrating that this approach can match strong federated fine-tuning baselines while substantially reducing communication by orders of magnitude (e.g., analytically by a factor of $1006$ for Llama3.1-405B), as well as reductions in runtime and energy consumption.

<!-- review:SF-BEYOND-PARAMETER-AGGREGATION-SEMANTIC-CONSENSUS-FOR-FEDERATED-FINE-TUNIN:start -->
#### Beyond Parameter Aggregation: Semantic Consensus for Federated Fine-Tuning of LLMs

问题与机制：We present a theoretical analysis and empirical results demonstrating that this approach can match strong federated fine-tuning baselines while substantially reducing communication by orders of magnitude (e.g., analytically by a factor of $1006$ for Llama3.1-405B), as well as reductions in runtime and energy consumption.。机制 owner=`TRAIN-DISTRIBUTED-TRAINING`。
Method / identity：arXiv:2605.11857v1 — §3 Method: behavior-level federated semantic consensus and communication analysis。
Evaluation：arXiv:2605.11857v1 — §5 Empirical Evaluation; Appendix C–E experiment setup and additional results。
Counterevidence / limitations：arXiv:2605.11857v1 — §6 Discussion and Conclusion; no dedicated Limitations section, so public-prompt coverage, pseudo-label error and output privacy leakage remain open boundaries。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-BEYOND-PARAMETER-AGGREGATION-SEMANTIC-CONSENSUS-FOR-FEDERATED-FINE-TUNIN:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `TRAIN-DISTRIBUTED-TRAINING` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-BEYOND-PARAMETER-AGGREGATION-SEMANTIC-CONSENSUS-FOR-FEDERATED-FINE-TUNIN:end -->

Books Decision=`Integrate`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-BEYOND-PARAMETER-AGGREGATION-SEMANTIC-CONSENSUS-FOR-FEDERATED-FINE-TUNIN:end -->

**Books 对读：** `TRAIN-DISTRIBUTED-TRAINING` → `books/part-04-training-system/36-distributed-training.md` 的“跨 Model Family 的 Federated 协作不能继续聚合 Parameters”。books/part-04-training-system/36-distributed-training.md 的‘跨 Model Family 的 Federated 协作不能继续聚合 Parameters’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We present a theoretical analysis and empirical results demonstrating that this approach can match strong federated fine-tuning baselines while substantially reducing communication by orders of magnitude (e.g., analytically by a factor of $1006$ for Llama3.1-405B), as well as reductions in runtime and energy consumption. 判定：**Integrate — Already present in current Books**。

### [IPI-proxy: An Intercepting Proxy for Red-Teaming Web-Browsing AI Agents Against Indirect Prompt Injection](https://arxiv.org/html/2605.11868v1)

**准入：** We present IPI-proxy, an open-source toolkit for red-teaming web-browsing agents against indirect prompt injection (IPI).

<!-- review:SF-IPI-PROXY-AN-INTERCEPTING-PROXY-FOR-RED-TEAMING-WEB-BROWSING-AI-AGENTS-A:start -->
#### IPI-proxy: An Intercepting Proxy for Red-Teaming Web-Browsing AI Agents Against Indirect Prompt Injection

问题与机制：We present IPI-proxy, an open-source toolkit for red-teaming web-browsing agents against indirect prompt injection (IPI).。机制 owner=`PLATFORM-SECURITY`。
全文定位：`arXiv:2605.11868v1 HTML — §3 IPI-proxy mediation boundary`；evaluation=`arXiv:2605.11868v1 — §4 indirect-prompt-injection evaluation`；limitations/counterevidence=`arXiv:2605.11868v1 — §5 limitations: classifier, tool and adaptive-attack scope`。
<!-- claim:SF-IPI-PROXY-AN-INTERCEPTING-PROXY-FOR-RED-TEAMING-WEB-BROWSING-AI-AGENTS-A:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-IPI-PROXY-AN-INTERCEPTING-PROXY-FOR-RED-TEAMING-WEB-BROWSING-AI-AGENTS-A:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-IPI-PROXY-AN-INTERCEPTING-PROXY-FOR-RED-TEAMING-WEB-BROWSING-AI-AGENTS-A:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“从资产与信任边界开始”。books/part-06-ai-infrastructure/72-security.md 的‘从资产与信任边界开始’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We present IPI-proxy, an open-source toolkit for red-teaming web-browsing agents against indirect prompt injection (IPI). 判定：**No Change — Existing Coverage**。

### [LOFT: Low-Rank Orthogonal Fine-Tuning via Task-Aware Support Selection](https://arxiv.org/html/2605.11872v1)

**准入：** orthogonal PEFT 往往把 adaptation support 与 support 内 transformation 混在同一参数化；LOFT 将两者分开并让 downstream gradient 选择 support。

<!-- review:SF-2026-ARXIV-2605-11872:start -->
#### LOFT: Low-Rank Orthogonal Fine-Tuning via Task-Aware Support Selection

**问题与旧基线。** orthogonal PEFT 往往把 adaptation support 与 support 内 transformation 混在同一参数化；LOFT 将两者分开并让 downstream gradient 选择 support。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §2 Method/Theory：low-rank multiplicative subspace rotation，统一 coordinate/butterfly/Householder/principal variants，并给出 first-order support analysis。 support selector 决定可更新子空间，orthogonal transform 只在其内改变方向；任务 loss/held-out gate 仍拥有选择真值。

**Evaluation contract。** §3 Experiments：language understanding、vision transfer、math reasoning、multilingual OOD；在匹配参数、显存与 compute 下比较。 V3=6（2+2+2）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；first-order criterion、任务梯度估计和所测 backbone/预算决定外推边界。

**Trade-off / failure / fallback。** task-aware support 提高预算利用率，却增加梯度估计、子空间更新与 optimizer coupling，错误 support 会冻结所需方向。 信号弱或任务多变时回退固定 principal/coordinate support、普通 LoRA 或 full tuning，并按行为而非矩阵距离验收。

**Artifact。** Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-11872:start -->exact-v1 支持：只支持 matched-budget 的受测任务；不证明 orthogonality 自动防遗忘、跨模型最优 support 或部署成本优势。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-11872:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-11872:end -->

**Books 对读：** `TRAIN-LORA` → `books/part-04-training-system/30-lora.md` 的“Rank 与 target modules 决定更新空间”。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：orthogonal PEFT 往往把 adaptation support 与 support 内 transformation 混在同一参数化；LOFT 将两者分开并让 downstream gradient 选择 support。 判定：**Integrate — Applied; independent post-write review pending**。

### [On-Policy Self-Evolution via Failure Trajectories for Agentic Safety Alignment](https://arxiv.org/html/2605.11882v1)

**准入：** on-policy failure trajectory repair 将 Agent safety 从静态数据训练改为当前 policy 失败、修复、验证和回放的闭环。

<!-- review:SF-2026-ARXIV-2605-11882:start -->
#### On-Policy Self-Evolution via Failure Trajectories for Agentic Safety Alignment

**问题与旧基线。** on-policy failure trajectory repair 将 Agent safety 从静态数据训练改为当前 policy 失败、修复、验证和回放的闭环。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3 Failure Trajectory Evolution。当前 policy 生成失败，same-policy 产出 repair，独立 verifier 评分，Pareto replay 再进入 SFT/PFPO。

**Evaluation contract。** §4；严格 dev/test split、三个随机种子和 AgentDojo/AgentHarm/ATBench。V3=3+2+2=7；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** Appendix K：依赖 verifier、policy-generated repair 与有限 benchmark，未覆盖真实长时域。

**Trade-off / failure / fallback。** 提高当前 failure frontier 覆盖但可能 self-confirm、污染 replay 并过拟合 verifier；保留独立 holdout、人工安全 gate 和静态基线。

<!-- claim:SF-2026-ARXIV-2605-11882:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-11882:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11882:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“安全数据闭环还可由当前 policy 生成 adversarial candidates”。正文约第 419 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：on-policy failure trajectory repair 将 Agent safety 从静态数据训练改为当前 policy 失败、修复、验证和回放的闭环。 判定：**Integrate — Applied; independent post-write review pending**。

### [Proteus: A Self-Evolving Red Team for Agent Skill Ecosystems](https://arxiv.org/html/2605.11891v1)

**准入：** We frame this risk as \emph{adaptive leakage} -- whether a budgeted attacker can iteratively revise a skill until it passes audit and produces verified runtime harm -- and present \ours{}, a grey-box self-evolving red-team framework for measuring it.

<!-- review:SF-PROTEUS-A-SELF-EVOLVING-RED-TEAM-FOR-AGENT-SKILL-ECOSYSTEMS:start -->
#### Proteus: A Self-Evolving Red Team for Agent Skill Ecosystems

问题与机制：We frame this risk as \emph{adaptive leakage} -- whether a budgeted attacker can iteratively revise a skill until it passes audit and produces verified runtime harm -- and present \ours{}, a grey-box self-evolving red-team framework for measuring it.。机制 owner=`PLATFORM-SECURITY`。
Method / identity：arXiv:2605.11891v1 — §4 Method: five-axis attack space, audit-sandbox-oracle feedback loop, and path/surface expansion。
Evaluation：arXiv:2605.11891v1 — §5 Experiments and §5.1 Experimental Setup; Appendix A additional results。
Counterevidence / limitations：arXiv:2605.11891v1 — Appendix C.1 Limitations: feedback access, rule oracle and evaluated target/auditor settings。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-PROTEUS-A-SELF-EVOLVING-RED-TEAM-FOR-AGENT-SKILL-ECOSYSTEMS:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `PLATFORM-SECURITY` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-PROTEUS-A-SELF-EVOLVING-RED-TEAM-FOR-AGENT-SKILL-ECOSYSTEMS:end -->

Books Decision=`Integrate`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-PROTEUS-A-SELF-EVOLVING-RED-TEAM-FOR-AGENT-SKILL-ECOSYSTEMS:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“Skill Poisoning 的真值是 Side Effect，而不是是否被调用”。books/part-06-ai-infrastructure/72-security.md 的‘Skill Poisoning 的真值是 Side Effect，而不是是否被调用’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We frame this risk as \emph{adaptive leakage} -- whether a budgeted attacker can iteratively revise a skill until it passes audit and produces verified runtime harm -- and present \ours{}, a grey-box self-evolving red-team framework for measuring it. 判定：**Integrate — Already present in current Books**。

### [When Simulation Lies: A Sim-to-Real Benchmark and Domain-Randomized RL Recipe for Tool-Use Agents](https://arxiv.org/html/2605.11928v1)

**准入：** We study these failures as a sim-to-real gap in the tool-use partially observable Markov decision process (POMDP), where deployment noise enters through the observation, action space, reward-relevant metadata, or transition dynamics.

<!-- review:SF-WHEN-SIMULATION-LIES-A-SIM-TO-REAL-BENCHMARK-AND-DOMAIN-RANDOMIZED-RL-RE:start -->
#### When Simulation Lies: A Sim-to-Real Benchmark and Domain-Randomized RL Recipe for Tool-Use Agents

问题与机制：We study these failures as a sim-to-real gap in the tool-use partially observable Markov decision process (POMDP), where deployment noise enters through the observation, action space, reward-relevant metadata, or transition dynamics.。机制 owner=`AGENT-TOOL-CALLING`。
Method / identity：arXiv:2605.11928v1 — §3 sim-to-real perturbation model and §4 benchmark/domain-randomized RL construction。
Evaluation：arXiv:2605.11928v1 — §6 Experiments, including §6.2 main results and §6.5 live evaluation platform。
Counterevidence / limitations：arXiv:2605.11928v1 — §7 Limitations and Future Work: encoded perturbations, benchmark/tool registries and transfer to live APIs。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-WHEN-SIMULATION-LIES-A-SIM-TO-REAL-BENCHMARK-AND-DOMAIN-RANDOMIZED-RL-RE:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `AGENT-TOOL-CALLING` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-WHEN-SIMULATION-LIES-A-SIM-TO-REAL-BENCHMARK-AND-DOMAIN-RANDOMIZED-RL-RE:end -->

Books Decision=`No Change — Existing Coverage`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-WHEN-SIMULATION-LIES-A-SIM-TO-REAL-BENCHMARK-AND-DOMAIN-RANDOMIZED-RL-RE:end -->

**Books 对读：** `AGENT-TOOL-CALLING` → `books/part-07-agent/78-tool-calling.md` 的“Observation 也不可信”。books/part-07-agent/78-tool-calling.md 的‘Observation 也不可信’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We study these failures as a sim-to-real gap in the tool-use partially observable Markov decision process (POMDP), where deployment noise enters through the observation, action space, reward-relevant metadata, or transition dynamics. 判定：**No Change — Existing Coverage**。

### [From Reaction to Anticipation: Proactive Failure Recovery through Agentic Task Graph for Robotic Manipulation](https://arxiv.org/html/2605.11951v1)

**准入：** Inspired by the human capability to anticipate and proactively plan for potential failures, we introduce AgentChord, an agentic system that models a manipulation task as a directed task graph.

<!-- review:SF-FROM-REACTION-TO-ANTICIPATION-PROACTIVE-FAILURE-RECOVERY-THROUGH-AGENTIC:start -->
#### From Reaction to Anticipation: Proactive Failure Recovery through Agentic Task Graph for Robotic Manipulation

问题与机制：Inspired by the human capability to anticipate and proactively plan for potential failures, we introduce AgentChord, an agentic system that models a manipulation task as a directed task graph.。机制 owner=`AGENT-WORKFLOW`。
全文定位：`arXiv:2605.11951v1 HTML — §3 proactive recovery graph and action ownership`；evaluation=`arXiv:2605.11951v1 — §4 embodied-agent recovery evaluation`；limitations/counterevidence=`arXiv:2605.11951v1 — §5 limitations: simulator, detector and recovery-policy scope`。
<!-- claim:SF-FROM-REACTION-TO-ANTICIPATION-PROACTIVE-FAILURE-RECOVERY-THROUGH-AGENTIC:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-FROM-REACTION-TO-ANTICIPATION-PROACTIVE-FAILURE-RECOVERY-THROUGH-AGENTIC:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-FROM-REACTION-TO-ANTICIPATION-PROACTIVE-FAILURE-RECOVERY-THROUGH-AGENTIC:end -->

**Books 对读：** `AGENT-WORKFLOW` → `books/part-07-agent/81-workflow.md` 的“Durable Execution 与 Replay”。books/part-07-agent/81-workflow.md 的‘Durable Execution 与 Replay’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：Inspired by the human capability to anticipate and proactively plan for potential failures, we introduce AgentChord, an agentic system that models a manipulation task as a directed task graph. 判定：**No Change — Existing Coverage**。

### [The Illusion of Power Capping in LLM Decode: A Phase-Aware Energy Characterisation Across Attention Architectures](https://arxiv.org/html/2605.11999v1)

**准入：** We show the appearance is illusory for the phase that dominates production serving: autoregressive decode.

<!-- review:SF-THE-ILLUSION-OF-POWER-CAPPING-IN-LLM-DECODE-A-PHASE-AWARE-ENERGY-CHARACT:start -->
#### The Illusion of Power Capping in LLM Decode: A Phase-Aware Energy Characterisation Across Attention Architectures

问题与机制：We show the appearance is illusory for the phase that dominates production serving: autoregressive decode.。机制 owner=`PLATFORM-COST`。
全文定位：`arXiv:2605.11999v1 HTML — §3 decode power-cap/clock-lock diagnosis`；evaluation=`arXiv:2605.11999v1 — §4 power/performance evaluation`；limitations/counterevidence=`arXiv:2605.11999v1 — §5 limitations: accelerator, model and power-governor scope`。
<!-- claim:SF-THE-ILLUSION-OF-POWER-CAPPING-IN-LLM-DECODE-A-PHASE-AWARE-ENERGY-CHARACT:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-THE-ILLUSION-OF-POWER-CAPPING-IN-LLM-DECODE-A-PHASE-AWARE-ENERGY-CHARACT:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-THE-ILLUSION-OF-POWER-CAPPING-IN-LLM-DECODE-A-PHASE-AWARE-ENERGY-CHARACT:end -->

**Books 对读：** `PLATFORM-COST` → `books/part-06-ai-infrastructure/70-cost.md` 的“Generation Energy 不是 Token 数的线性函数”。books/part-06-ai-infrastructure/70-cost.md 的‘Generation Energy 不是 Token 数的线性函数’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We show the appearance is illusory for the phase that dominates production serving: autoregressive decode. 判定：**No Change — Existing Coverage**。

### [CR^2: Cost-Aware Risk-Controlled Routing for Wireless Device-Edge LLM Inference](https://arxiv.org/html/2605.12001v1)

**准入：** In this paper, we formulate mobile edge LLM routing as a deployment-constrained, cost-aware decision problem, and propose CR^2, a two-stage device-edge routing framework.

<!-- review:SF-CR-2-COST-AWARE-RISK-CONTROLLED-ROUTING-FOR-WIRELESS-DEVICE-EDGE-LLM-INF:start -->
#### CR^2: Cost-Aware Risk-Controlled Routing for Wireless Device-Edge LLM Inference

问题与机制：In this paper, we formulate mobile edge LLM routing as a deployment-constrained, cost-aware decision problem, and propose CR^2, a two-stage device-edge routing framework.。机制 owner=`INFER-SCHEDULING`。
Method / identity：arXiv:2605.12001v1 — §IV System Model and deployment/information structure; §V formulation; §VI two-stage CR2 method。
Evaluation：arXiv:2605.12001v1 — §VII Experiments and §VII-A Experimental Setup。
Counterevidence / limitations：arXiv:2605.12001v1 — no dedicated Limitations section; §VIII Conclusion plus disclosed channel, model, edge topology and estimator assumptions bound the claim。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-CR-2-COST-AWARE-RISK-CONTROLLED-ROUTING-FOR-WIRELESS-DEVICE-EDGE-LLM-INF:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `INFER-SCHEDULING` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-CR-2-COST-AWARE-RISK-CONTROLLED-ROUTING-FOR-WIRELESS-DEVICE-EDGE-LLM-INF:end -->

Books Decision=`No Change — Existing Coverage`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-CR-2-COST-AWARE-RISK-CONTROLLED-ROUTING-FOR-WIRELESS-DEVICE-EDGE-LLM-INF:end -->

**Books 对读：** `INFER-SCHEDULING` → `books/part-05-inference-system/56-inference-scheduling.md` 的“目标函数不止吞吐”。books/part-05-inference-system/56-inference-scheduling.md 的‘目标函数不止吞吐’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：In this paper, we formulate mobile edge LLM routing as a deployment-constrained, cost-aware decision problem, and propose CR^2, a two-stage device-edge routing framework. 判定：**No Change — Existing Coverage**。

### [L2P: Unlocking Latent Potential for Pixel Generation](https://arxiv.org/html/2605.12013v1)

**准入：** L2P 用 latent diffusion 的合成图像训练 pixel-space generator，在 inference 移除 VAE，改变 representation/training boundary。

<!-- review:SF-2026-ARXIV-2605-12013:start -->
#### L2P: Unlocking Latent Potential for Pixel Generation

**问题与旧基线。** L2P 用 latent diffusion 的合成图像训练 pixel-space generator，在 inference 移除 VAE，改变 representation/training boundary。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3.2–§3.4 L2P Transfer and 4K Extension。teacher 在 latent path 生成训练图像，student 直接在 pixel space 学习；VAE 只存在于数据生成而不在部署路径。

**Evaluation contract。** §4；1024/4K generation 与受测 latent teacher。V3=2+1+2=5；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** Appendix D：synthetic source upper bound，省略 task-specific loss 等。

**Trade-off / failure / fallback。** 减少部署 decoder 依赖但继承 teacher bias 并增加离线合成成本；数据不足或高频细节失败时保留 latent/VAE 路径。

<!-- claim:SF-2026-ARXIV-2605-12013:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-12013:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-12013:end -->

**Books 对读：** `MULTIMODAL-GENERATIVE-PARADIGMS` → `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的“Output Decoder 是独立的版本化 Generation Artifact”。正文约第 396 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：L2P 用 latent diffusion 的合成图像训练 pixel-space generator，在 inference 移除 VAE，改变 representation/training boundary。 判定：**Integrate — Applied; independent post-write review pending**。

### [SAGE: Scalable Automated Robustness Augmentation for LLM Knowledge Evaluation](https://arxiv.org/html/2605.12022v1)

**准入：** SAGE 将 robustness variant generation 与 rubric verification 组成版本化 evaluation artifact pipeline。

<!-- review:SF-2026-ARXIV-2605-12022:start -->
#### SAGE: Scalable Automated Robustness Augmentation for LLM Knowledge Evaluation

**问题与旧基线。** SAGE 将 robustness variant generation 与 rubric verification 组成版本化 evaluation artifact pipeline。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3.2 VariantQual；§3.3 VariantGen。小模型生成 variants，rubric verifier 负责质量筛选，最终 suite 才进入评估；generator 不拥有有效性真值。

**Evaluation contract。** §4；MCQ robustness、生成器/verifier 和多模型对比。V3=2+2+2=6；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** Appendix E：只覆盖 MCQ、预定义 variant 类型并依赖 verifier。

**Trade-off / failure / fallback。** 扩大覆盖换 verifier bias、模板化和成本；低置信 variant 应隔离、人工抽检并保留原 benchmark baseline。

<!-- claim:SF-2026-ARXIV-2605-12022:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-12022:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-12022:end -->

**Books 对读：** `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md` 的“Benchmark 生成器也会塑造被评估的任务人口”。正文约第 806 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：SAGE 将 robustness variant generation 与 rubric verification 组成版本化 evaluation artifact pipeline。 判定：**Integrate — Applied; independent post-write review pending**。

### [SkillGraph: Skill-Augmented Reinforcement Learning for Agents via Evolving Skill Graphs](https://arxiv.org/html/2605.12039v1)

**准入：** isolated skill entries 只按语义相似度检索，无法表达前置关系，也无法治理 merge/split/delete；SkillGraph 把 procedural memory 变成 typed evolving graph。

<!-- review:SF-2026-ARXIV-2605-12039:start -->
#### SkillGraph: Skill-Augmented Reinforcement Learning for Agents via Evolving Skill Graphs

**问题与旧基线。** isolated skill entries 只按语义相似度检索，无法表达前置关系，也无法治理 merge/split/delete；SkillGraph 把 procedural memory 变成 typed evolving graph。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §3 Method：skill nodes 与 prerequisite/enhancement/co-occurrence edges；检索 ordered subgraph，并由 trajectories/RL feedback 更新图和 policy。 skill graph 拥有候选依赖，trajectory evidence 提出 mutation；memory controller 管理版本/合并，workflow 仍拥有执行顺序与 commit。

**Evaluation contract。** §4 Experiments：ALFWorld、WebShop 与七个 search-augmented QA tasks，对比 memory-augmented RL baselines。 V3=7（3+2+2）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；edge induction、删除标准、并发更新、版本回滚与跨环境 transfer 没有生产证据。

**Trade-off / failure / fallback。** 组合性换来图漂移、循环依赖、错误合并和检索成本；RL feedback 还会把当前 policy 偏差固化进 memory。 图证据不足时回退孤立 versioned skills、人工依赖、只读 graph snapshot 和执行时 constraint validation。

**Artifact。** Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-12039:start -->exact-v1 支持：只支持所测环境与 evaluator；不证明技能关系是真因果、跨 agent 可移植或在线图更新一致。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-12039:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-12039:end -->

**Books 对读：** `AGENT-MEMORY` → `books/part-07-agent/77-memory.md` 的“Procedural Memory 的压缩单位应是可展开的 Contract Graph”。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：isolated skill entries 只按语义相似度检索，无法表达前置关系，也无法治理 merge/split/delete；SkillGraph 把 procedural memory 变成 typed evolving graph。 判定：**Integrate — Applied; independent post-write review pending**。

### [OmniRefine: Alignment-Aware Cooperative Compression for Efficient Omnimodal Large Language Models](https://arxiv.org/html/2605.12056v1)

**准入：** 固定/native 压缩单元会切断 audio-video correspondence；OmniRefine 先按跨模态相似度重划 chunk，再在 chunk 内联合分配 audio/video token。

<!-- review:SF-2026-ARXIV-2605-12056:start -->
#### OmniRefine: Alignment-Aware Cooperative Compression for Efficient Omnimodal Large Language Models

**问题与旧基线。** 固定/native 压缩单元会切断 audio-video correspondence；OmniRefine 先按跨模态相似度重划 chunk，再在 chunk 内联合分配 audio/video token。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §3 Method：CPCR 以 frame-audio similarity 和 dynamic programming 重划边界，MACC 在对齐单元内消冗余并保留关键证据。 alignment unit 拥有候选压缩边界，modality budget 分配保留证据角色；downstream task/evaluator 仍决定可接受损失。

**Evaluation contract。** §4 与 Appendix C：多 audio-video benchmarks、Qwen2.5-Omni 3B/7B，硬件/latency profiling、multi-turn KV simulation 与 constant-budget audit。 V3=6（2+2+2）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** Appendix D：跨模态相似度与压缩阈值依赖模型；动态规划和多模态证据误判会带来额外成本。代码/接口承诺发布但 exact immutable commit 未披露。

**Trade-off / failure / fallback。** 降低 token/FLOPs 但可能误删互补细节、错误对齐 chunk，并增加 preprocessing 与 KV identity 复杂度。 不确定时提高 retention、保留完整 modality state，或回退单模态/固定 chunk baseline并做逐任务降级。

**Artifact。** Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-12056:start -->exact-v1 支持：现有正文已覆盖 fixed-budget 信息责任、方向性、timestamp/chunk boundary 和跨模态互补；本证据不改变 canonical 结论。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-12056:end -->

Books Decision=`No Change — Existing Coverage`；作者未修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-12056:end -->

**Books 对读：** `MULTIMODAL-REPRESENTATION` → `books/part-03-multimodal-world-models/23-multimodal-representation.md` 的“固定预算要先分配信息责任，再选择具体 Token”。现有正文已语义承载该机制、边界和 fallback。 新证据增量：固定/native 压缩单元会切断 audio-video correspondence；OmniRefine 先按跨模态相似度重划 chunk，再在 chunk 内联合分配 audio/video token。 判定：**No Change — Existing Coverage**。

### [SAGE: A Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory](https://arxiv.org/html/2605.12061v1)

**准入：** self-evolving graph memory 把 writer、reader 与反馈分权，记忆图成为可修订状态而非静态 retrieval middleware。

<!-- review:SF-2026-ARXIV-2605-12061:start -->
#### SAGE: A Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory

问题、旧路径与约束变化：self-evolving graph memory 把 writer、reader 与反馈分权，记忆图成为可修订状态而非静态 retrieval middleware。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§3 Preliminary and §4 Method。canonical owner=`AGENT-MEMORY`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§5 Experiments。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§6 Conclusion；无独立 Limitations，结论限于受测 graph reader/writer loop。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-12061:start -->exact-v1 支持：self-evolving graph memory 把 writer、reader 与反馈分权，记忆图成为可修订状态而非静态 retrieval middleware。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-12061:end -->

Books Decision=`No Change — Existing Coverage`；作者只形成命题比较与 root serial queue，不直接修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-12061:end -->

**Books 对读：** `AGENT-MEMORY` → `books/part-07-agent/77-memory.md` 的“Derived Graph 更新必须沿 Evidence Dependency 传播”。`books/part-07-agent/77-memory.md` 的“Derived Graph 更新必须沿 Evidence Dependency 传播”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：self-evolving graph memory 把 writer、reader 与反馈分权，记忆图成为可修订状态而非静态 retrieval middleware。 判定：**No Change — Existing Coverage**。

### [Property-Level Reconstructability of Agent Decisions: An Anchor-Level Pilot Across Vendor SDK Adapter Regimes](https://arxiv.org/html/2605.12078v1)

**准入：** Agentic AI failures need post-hoc reconstruction: what the agent did, on whose authority, against which policy, and from what reasoning.

<!-- review:SF-PROPERTY-LEVEL-RECONSTRUCTABILITY-OF-AGENT-DECISIONS-AN-ANCHOR-LEVEL-PIL:start -->
#### Property-Level Reconstructability of Agent Decisions: An Anchor-Level Pilot Across Vendor SDK Adapter Regimes

问题与机制：Agentic AI failures need post-hoc reconstruction: what the agent did, on whose authority, against which policy, and from what reasoning.。机制 owner=`PLATFORM-TRACE`。
Method / identity：arXiv:2605.12078v1 — exact-v1 PDF §3 uniform Decision Trace Reconstructor protocol; §4 pinned worked-example anchors and reproducibility package。
Evaluation：arXiv:2605.12078v1 — exact-v1 PDF §5 per-property/per-regime diagnostic matrix。
Counterevidence / limitations：arXiv:2605.12078v1 — exact-v1 PDF §6 discussion and enumerated limitations: single annotator, one worked-example anchor per cell, no production traces or statistical interchangeability claim。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-PROPERTY-LEVEL-RECONSTRUCTABILITY-OF-AGENT-DECISIONS-AN-ANCHOR-LEVEL-PIL:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `PLATFORM-TRACE` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-PROPERTY-LEVEL-RECONSTRUCTABILITY-OF-AGENT-DECISIONS-AN-ANCHOR-LEVEL-PIL:end -->

Books Decision=`No Change — Existing Coverage`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-PROPERTY-LEVEL-RECONSTRUCTABILITY-OF-AGENT-DECISIONS-AN-ANCHOR-LEVEL-PIL:end -->

**Books 对读：** `PLATFORM-TRACE` → `books/part-06-ai-infrastructure/69-trace.md` 的“Span 的最小语义”。books/part-06-ai-infrastructure/69-trace.md 的‘Span 的最小语义’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：Agentic AI failures need post-hoc reconstruction: what the agent did, on whose authority, against which policy, and from what reasoning. 判定：**No Change — Existing Coverage**。

### [Intermediate Artifacts as First-Class Citizens: A Data Model for Durable Intermediate Artifacts in Agentic Systems](https://arxiv.org/html/2605.12087v1)

**准入：** We argue that such systems should preserve durable, inspectable intermediate artifacts: typed, structured, addressable, versioned, dependency-aware, authoritative, and consumable by downstream computation.

<!-- review:SF-INTERMEDIATE-ARTIFACTS-AS-FIRST-CLASS-CITIZENS-A-DATA-MODEL-FOR-DURABLE-:start -->
#### Intermediate Artifacts as First-Class Citizens: A Data Model for Durable Intermediate Artifacts in Agentic Systems

问题与机制：We argue that such systems should preserve durable, inspectable intermediate artifacts: typed, structured, addressable, versioned, dependency-aware, authoritative, and consumable by downstream computation.。机制 owner=`AGENT-PLATFORM`。
Method / identity：arXiv:2605.12087v1 — §5 Artifact-Centric Data Model; §6 update semantics; §7 reference architecture。
Evaluation：arXiv:2605.12087v1 — §8 Evaluation Implications and worked benchmark-style example。
Counterevidence / limitations：arXiv:2605.12087v1 — §9 Discussion and §10 Limitations: conceptual model, limited implementations and unresolved interoperability/adoption costs。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-INTERMEDIATE-ARTIFACTS-AS-FIRST-CLASS-CITIZENS-A-DATA-MODEL-FOR-DURABLE-:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `AGENT-PLATFORM` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-INTERMEDIATE-ARTIFACTS-AS-FIRST-CLASS-CITIZENS-A-DATA-MODEL-FOR-DURABLE-:end -->

Books Decision=`No Change — Existing Coverage`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-INTERMEDIATE-ARTIFACTS-AS-FIRST-CLASS-CITIZENS-A-DATA-MODEL-FOR-DURABLE-:end -->

**Books 对读：** `AGENT-PLATFORM` → `books/part-07-agent/84-agent-platform.md` 的“Agent Runtime State Machine”。intermediate artifact 必须是 typed、versioned、addressable、dependency-aware 的 durable state，并明确 authoritative producer 与 downstream consumers。 新证据增量：We argue that such systems should preserve durable, inspectable intermediate artifacts: typed, structured, addressable, versioned, dependency-aware, authoritative, and consumable by downstream computation. 判定：**Integrate — Applied; independent post-write review pending**。

### [Autonomy and Agency in Agentic AI: Architectural Tactics for Regulated Contexts](https://arxiv.org/html/2605.12105v1)

**准入：** agency 与 autonomy 是耦合的部署维度；checkpoints、escalation、tool fencing 和 write staging 调节 effect authority。

<!-- review:SF-2026-ARXIV-2605-12105:start -->
#### Autonomy and Agency in Agentic AI: Architectural Tactics for Regulated Contexts

问题、旧路径与约束变化：agency 与 autonomy 是耦合的部署维度；checkpoints、escalation、tool fencing 和 write staging 调节 effect authority。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§III design dimensions and §IV tactics。canonical owner=`AGENT-PLATFORM`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§V worked examples。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§VI Beyond and §VII Conclusion；无独立 Limitations，案例不构成合规认证。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-12105:start -->exact-v1 支持：agency 与 autonomy 是耦合的部署维度；checkpoints、escalation、tool fencing 和 write staging 调节 effect authority。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-12105:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-12105:end -->

**Books 对读：** `AGENT-PLATFORM` → `books/part-07-agent/84-agent-platform.md` 的“长任务的人类边界应前移到目标与结构性 Commit”。`books/part-07-agent/84-agent-platform.md` 的“长任务的人类边界应前移到目标与结构性 Commit”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：agency 与 autonomy 是耦合的部署维度；checkpoints、escalation、tool fencing 和 write staging 调节 effect authority。 判定：**Integrate — Applied; independent post-write review pending**。

### [AB-Sparse: Sparse Attention with Adaptive Block Size for Accurate and Efficient Long-Context Inference](https://arxiv.org/html/2605.12110v1)

**准入：** block-sparse attention 的固定 block size 隐含 head 同质性；adaptive per-head block 与 kernel/layout 必须联合设计。

<!-- review:SF-2026-ARXIV-2605-12110:start -->
#### AB-Sparse: Sparse Attention with Adaptive Block Size for Accurate and Efficient Long-Context Inference

问题、旧路径与约束变化：block-sparse attention 的固定 block size 隐含 head 同质性；adaptive per-head block 与 kernel/layout 必须联合设计。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§2 Background and §3 Design。canonical owner=`MODEL-LONG-CONTEXT`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§4 Evaluation。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§5 Conclusion；无独立 Limitations，headline 受模型、kernel 与硬件约束。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-12110:start -->exact-v1 支持：block-sparse attention 的固定 block size 隐含 head 同质性；adaptive per-head block 与 kernel/layout 必须联合设计。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-12110:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-12110:end -->

**Books 对读：** `MODEL-LONG-CONTEXT` → `books/part-02-model/22-long-context.md` 的“Conditional Attention 的路由粒度必须匹配执行粒度”。`books/part-02-model/22-long-context.md` 的“Conditional Attention 的路由粒度必须匹配执行粒度”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：block-sparse attention 的固定 block size 隐含 head 同质性；adaptive per-head block 与 kernel/layout 必须联合设计。 判定：**Integrate — Applied; independent post-write review pending**。

### [When Policy Entropy Constraint Fails: Preserving Diversity in Flow-based RLHF via Perceptual Entropy](https://arxiv.org/html/2605.12112v1)

**准入：** flow-based RLHF 中固定 policy entropy 不能反映视觉多样性坍缩，perceptual entropy 因而成为新的控制变量。

<!-- review:SF-2026-ARXIV-2605-12112:start -->
#### When Policy Entropy Constraint Fails: Preserving Diversity in Flow-based RLHF via Perceptual Entropy

**问题与旧基线。** flow-based RLHF 中固定 policy entropy 不能反映视觉多样性坍缩，perceptual entropy 因而成为新的控制变量。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3 Diagnosis of Constant Policy Entropy；§4 Perceptual Entropy and GRPO。固定 noise schedule 使 policy entropy 近似常量，而 perceptual diversity 可坍缩；方法估计 perceptual entropy 并加约束。

**Evaluation contract。** §5；FLUX.dev、SD3.5-Medium 与披露 reward settings。V3=3+1+3=7；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；只覆盖两个 flow text-to-image model 和受测 rewards。

**Trade-off / failure / fallback。** 更贴近输出变化但依赖感知 encoder/metric，可能奖励表面差异；metric 漂移时回退人工/多指标评估和保守 KL。

<!-- claim:SF-2026-ARXIV-2605-12112:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-12112:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-12112:end -->

**Books 对读：** `TRAIN-RLHF` → `books/part-04-training-system/31-rlhf.md` 的“反馈预算必须绑定样本粒度与可观测不确定性”。正文约第 409 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：flow-based RLHF 中固定 policy entropy 不能反映视觉多样性坍缩，perceptual entropy 因而成为新的控制变量。 判定：**Integrate — Applied; independent post-write review pending**。

### [To Whom Do Language Models Align? Measuring Principal Hierarchies Under High-Stakes Competing Demands](https://arxiv.org/html/2605.12120v1)

**准入：** 模型在 advisory prompt 中维护专业规范，不代表在实际 drafting/action framing 中仍遵从；principal hierarchy 必须作为 domain × task framing × stakeholder 的行为合同测量。

<!-- review:SF-2026-ARXIV-2605-12120:start -->
#### To Whom Do Language Models Align? Measuring Principal Hierarchies Under High-Stakes Competing Demands

**问题与旧基线。** 模型在 advisory prompt 中维护专业规范，不代表在实际 drafting/action framing 中仍遵从；principal hierarchy 必须作为 domain × task framing × stakeholder 的行为合同测量。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §2 Method：构造 user、institutional authority 与 professional norm 冲突场景，并分别测 advisory 与 task execution。 scenario contract 拥有冲突角色与规范，model output 只是行为证据；release gate 必须按 framing/domain/model slice 保留层级结果。

**Evaluation contract。** §3 Results：法律/医疗 7,136 scenarios、10 个 frontier models；分析 omission、reasoning-visible-but-output-suppressed 等 failure。 V3=9（3+3+3）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** 明确 Limitations：两个高风险领域、合成场景、选定模型/时间点；reasoning trace 不能被视为真实内部因果解释。

**Trade-off / failure / fallback。** 更贴近部署冲突，却增加专业规范定义、专家标注和时变模型成本；平均聚合会掩盖局部 authority inversion。 证据不足时回退明确 policy hierarchy、工具/权限 gate、人工复核和 domain-specific abstention，不让模型自报意图替代行为测试。

**Artifact。** Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-12120:start -->exact-v1 支持：只支持所测法律/医疗场景和模型；不证明真实事故率、内部动机、全部职业规范或未来模型稳定性。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-12120:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-12120:end -->

**Books 对读：** `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md` 的“评估对象有四个层次”。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：模型在 advisory prompt 中维护专业规范，不代表在实际 drafting/action framing 中仍遵从；principal hierarchy 必须作为 domain × task framing × stakeholder 的行为合同测量。 判定：**Integrate — Applied; independent post-write review pending**。

### [Disentangled Sparse Representations for Concept-Separated Diffusion Unlearning](https://arxiv.org/html/2605.12122v1)

**准入：** 普通 sparse reconstruction SAE 让多个概念共享 feature，压制目标概念时会连带损伤非目标内容；concept-aware clustering 把删除边界移到表示 support。

<!-- review:SF-2026-ARXIV-2605-12122:start -->
#### Disentangled Sparse Representations for Concept-Separated Diffusion Unlearning

**问题与旧基线。** 普通 sparse reconstruction SAE 让多个概念共享 feature，压制目标概念时会连带损伤非目标内容；concept-aware clustering 把删除边界移到表示 support。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §3 Method：concept-aware contrastive objective 组织 concept-specific clusters，并以 GeLU encoder 增强分离表达。 cluster assignment 只提出被抑制 feature support；unlearning controller 与行为/evidence gate 仍拥有删除 commit 与验收权。

**Evaluation contract。** §4 Experiments：UnlearnCanvas，重点为 joint style-object unlearning 与 collateral interference。 V3=5（2+1+2）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；只覆盖 diffusion latent、所选概念/benchmark 与 SAE architecture，不证明参数级删除或法律合规。

**Trade-off / failure / fallback。** 更精准抑制换来 cluster leakage、概念重叠、表示漂移和新训练成本；错误分离仍会产生 collateral damage。 分离证据不强时回退模型版本隔离、prompt/output guardrail、重新训练或更宽行为评估，并保留原 artifact。

**Artifact。** Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-12122:start -->exact-v1 支持：只证明作者 benchmark 中的行为抑制/保真指标；不证明知识已从权重移除、跨 prompt 不可恢复或合规删除完成。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-12122:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-12122:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“Unlearning 必须分开参数擦除与推理拒答”。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：普通 sparse reconstruction SAE 让多个概念共享 feature，压制目标概念时会连带损伤非目标内容；concept-aware clustering 把删除边界移到表示 support。 判定：**Integrate — Applied; independent post-write review pending**。

### [It's Not the Size: Harness Design Determines Operational Stability in Small Language Models](https://arxiv.org/html/2605.12129v1)

**准入：** This paper experimentally analyzes how the level of harness engineering affects the operational performance of small language models (SLMs, 2-3B parameters).

<!-- review:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA:start -->
#### It's Not the Size: Harness Design Determines Operational Stability in Small Language Models

问题与机制：This paper experimentally analyzes how the level of harness engineering affects the operational performance of small language models (SLMs, 2-3B parameters).。机制 owner=`AGENT-WORKFLOW`。
Method / identity：arXiv:2605.12129v1 — exact-v1 PDF §3 Methodology, including harness conditions, ablations and task design。
Evaluation：arXiv:2605.12129v1 — exact-v1 PDF §4–§6 results, cross-model comparison and ablation study。
Counterevidence / limitations：arXiv:2605.12129v1 — exact-v1 PDF §7.4 design limitation and §7.5 Limitations: 24 tasks, one run, non-uniform timeout, single scorer, 2–3x overhead, environment mismatch and external rate limits。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `AGENT-WORKFLOW` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA:end -->

Books Decision=`No Change — Existing Coverage`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-IT-S-NOT-THE-SIZE-HARNESS-DESIGN-DETERMINES-OPERATIONAL-STABILITY-IN-SMA:end -->

**Books 对读：** `AGENT-WORKFLOW` → `books/part-07-agent/81-workflow.md` 的“Deterministic Spine，Agentic Nodes”。books/part-07-agent/81-workflow.md 的‘Deterministic Spine，Agentic Nodes’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：This paper experimentally analyzes how the level of harness engineering affects the operational performance of small language models (SLMs, 2-3B parameters). 判定：**No Change — Existing Coverage**。

### [Rollout Cards: A Reproducibility Standard for Agent Research](https://arxiv.org/html/2605.12131v1)

**准入：** We introduce rollout cards: publication bundles that preserve the rollout record and declare the views, reporting rules, and drops manifests behind reported scores.

<!-- review:SF-ROLLOUT-CARDS-A-REPRODUCIBILITY-STANDARD-FOR-AGENT-RESEARCH:start -->
#### Rollout Cards: A Reproducibility Standard for Agent Research

问题与机制：We introduce rollout cards: publication bundles that preserve the rollout record and declare the views, reporting rules, and drops manifests behind reported scores.。机制 owner=`PLATFORM-EVALUATION-SYSTEM`。
全文定位：`arXiv:2605.12131v1 HTML — §3 Rollout Card evidence schema`；evaluation=`arXiv:2605.12131v1 — §4 multi-run evaluation examples`；limitations/counterevidence=`arXiv:2605.12131v1 — §5 limitations: disclosure quality and evaluator comparability`。
<!-- claim:SF-ROLLOUT-CARDS-A-REPRODUCIBILITY-STANDARD-FOR-AGENT-RESEARCH:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-ROLLOUT-CARDS-A-REPRODUCIBILITY-STANDARD-FOR-AGENT-RESEARCH:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-ROLLOUT-CARDS-A-REPRODUCIBILITY-STANDARD-FOR-AGENT-RESEARCH:end -->

**Books 对读：** `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md` 的“第一个不变量：评估声明必须绑定完整对象”。Agent evaluation 的 publication bundle 应同时保存 rollout record、声明的 views/reporting rules 与 dropped-runs manifest，使报告分数可追溯到同一证据对象。 新证据增量：We introduce rollout cards: publication bundles that preserve the rollout record and declare the views, reporting rules, and drops manifests behind reported scores. 判定：**Integrate — Applied; independent post-write review pending**。

### [Premover: Fast Vision-Language-Action Control by Acting Before Instructions Are Complete](https://arxiv.org/html/2605.12160v1)

**准入：** We introduce Premover, a lightweight module that converts this idle window into useful precomputation.

<!-- review:SF-PREMOVER-FAST-VISION-LANGUAGE-ACTION-CONTROL-BY-ACTING-BEFORE-INSTRUCTIO:start -->
#### Premover: Fast Vision-Language-Action Control by Acting Before Instructions Are Complete

问题与机制：We introduce Premover, a lightweight module that converts this idle window into useful precomputation.。机制 owner=`MULTIMODAL-EMBODIED-VLA`。
Method / identity：arXiv:2605.12160v1 — §3 Method: anticipatory instruction encoder, prefix predictor and commitment gate。
Evaluation：arXiv:2605.12160v1 — §4 Experiments, including §4.1 setup, metrics and streaming protocol。
Counterevidence / limitations：arXiv:2605.12160v1 — §5 Limitations and Future Work: instruction distribution, prediction error, embodiment and safety scope。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-PREMOVER-FAST-VISION-LANGUAGE-ACTION-CONTROL-BY-ACTING-BEFORE-INSTRUCTIO:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `MULTIMODAL-EMBODIED-VLA` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-PREMOVER-FAST-VISION-LANGUAGE-ACTION-CONTROL-BY-ACTING-BEFORE-INSTRUCTIO:end -->

Books Decision=`No Change — Existing Coverage`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-PREMOVER-FAST-VISION-LANGUAGE-ACTION-CONTROL-BY-ACTING-BEFORE-INSTRUCTIO:end -->

**Books 对读：** `MULTIMODAL-EMBODIED-VLA` → `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的“Latency 与 control frequency”。books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md 的‘Latency 与 control frequency’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We introduce Premover, a lightweight module that converts this idle window into useful precomputation. 判定：**No Change — Existing Coverage**。

### [Lower bounds for one-layer transformers that compute parity](https://arxiv.org/html/2605.12171v1)

**准入：** ‘一层 attention 足以全局交互’不等于它能以固定 heads 和简单 post-process 表达全局 parity；复杂度必须同时计 heads 与后处理函数度数。

<!-- review:SF-2026-ARXIV-2605-12171:start -->
#### Lower bounds for one-layer transformers that compute parity

**问题与旧基线。** ‘一层 attention 足以全局交互’不等于它能以固定 heads 和简单 post-process 表达全局 parity；复杂度必须同时计 heads 与后处理函数度数。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §3 Theorem：rational post-processing 下，heads × rational degree 必须随输入长度线性增长才能 sign-represent parity；§4 通过 rational approximation 扩到 ReLU post-processing 的 margin-dependent bound。 attention heads 提供交互通道，post-process 提供非线性选择；任何一侧容量不足都不能由‘全局可见’自动补偿。

**Evaluation contract。** 理论论文，无 empirical benchmark；evaluation contract 是 theorem assumptions、sign representation 与 margin。 V3=8（3+2+3）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** 不覆盖多层网络、训练可达性、近似任务、实际 precision 或自然语言分布；下界只在所述函数类和 margin 假设内成立。

**Trade-off / failure / fallback。** 增加 heads/degree 可以绕开下界，但增加参数、计算与优化难度；理论 capacity 也不保证可训练。 需要 parity-like interaction 时使用更多层、显式 recurrence/algorithmic state 或更强后处理；普通局部任务保留单层基线。

**Artifact。** Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-12171:start -->exact-v1 支持：证明的是一层模型的必要增长率，不是 Transformer 普遍失败、真实 LLM 能力上限或具体硬件成本。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-12171:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-12171:end -->

**Books 对读：** `MODEL-SELF-ATTENTION` → `books/part-02-model/14-self-attention.md` 的“Self Attention 获得了什么”。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：‘一层 attention 足以全局交互’不等于它能以固定 heads 和简单 post-process 表达全局 parity；复杂度必须同时计 heads 与后处理函数度数。 判定：**Integrate — Applied; independent post-write review pending**。

### [Do Enterprise Systems Need Learned World Models? The Importance of Context to Infer Dynamics](https://arxiv.org/html/2605.12178v1)

**准入：** enterprise agent 通过读取 live configuration 恢复环境动态，改变 learned world model 与 runtime discovery 的 state-owner 分工。

<!-- review:SF-2026-ARXIV-2605-12178:start -->
#### Do Enterprise Systems Need Learned World Models? The Importance of Context to Infer Dynamics

**问题与旧基线。** enterprise agent 通过读取 live configuration 恢复环境动态，改变 learned world model 与 runtime discovery 的 state-owner 分工。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3 Enterprise Dynamics；§4 Gym；§5 Prompted/Learned/Discovery Approaches。prompted rules、learned dynamics 与 runtime discovery 是三条分支；deployment shift 下 live config 才拥有当前环境状态真值。

**Evaluation contract。** §6；单一 enterprise platform、多个任务和模型。V3=3+2+3=8；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** §9 与 Appendix A：依赖可读规则、tool use、单平台、Tier 1/2 任务及少量模型。

**Trade-off / failure / fallback。** discovery 提高 freshness 但增加工具延迟、权限和解析故障；配置不可读时回退版本化 simulator/learned prior，并保持 state uncertainty。

<!-- claim:SF-2026-ARXIV-2605-12178:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-12178:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-12178:end -->

**Books 对读：** `MULTIMODAL-WORLD-MODELS` → `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 的“World Model 不必保存全部 Observation，但必须覆盖下游 Query Closure”。正文约第 419 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：enterprise agent 通过读取 live configuration 恢复环境动态，改变 learned world model 与 runtime discovery 的 state-owner 分工。 判定：**Integrate — Applied; independent post-write review pending**。

### [SyncDPO: Enhancing Temporal Synchronization in Video-Audio Joint Generation via Preference Learning](https://arxiv.org/html/2605.12179v1)

**准入：** SyncDPO 用规则化时间扰动在线构造 preference negatives，并以 curriculum 调节 video-audio 对齐难度。

<!-- review:SF-2026-ARXIV-2605-12179:start -->
#### SyncDPO: Enhancing Temporal Synchronization in Video-Audio Joint Generation via Preference Learning

**问题与旧基线。** SyncDPO 用规则化时间扰动在线构造 preference negatives，并以 curriculum 调节 video-audio 对齐难度。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3.2 Negative Construction；§3.3 Curriculum Learning。对原样本施加 coarse-to-fine temporal distortion 构造 rejected pair，避免昂贵采样排序并逐步提高难度。

**Evaluation contract。** §4 与 Appendices A/B；四类 benchmark、客观/主观 evaluation。V3=2+1+2=5；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** Appendix C Limitations：规则负例、数据/模型与时序 metric 范围受限。

**Trade-off / failure / fallback。** 降低 pair 构建成本但可能学习扰动模板而非真实同步；真实负例或人工偏好仍是必要 fallback。

<!-- claim:SF-2026-ARXIV-2605-12179:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-12179:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-12179:end -->

**Books 对读：** `TRAIN-DPO` → `books/part-04-training-system/34-dpo.md` 的“Preference Pair 选择是实验设计，不只是数据量选择”。正文约第 244 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：SyncDPO 用规则化时间扰动在线构造 preference negatives，并以 curriculum 调节 video-audio 对齐难度。 判定：**Integrate — Applied; independent post-write review pending**。

### [SOAR: Scale Optimization for Accurate Reconstruction in NVFP4 Quantization](https://arxiv.org/html/2605.12245v1)

**准入：** To address these issues, we propose Scale Optimization for Accurate Reconstruction (SOAR), a novel post-training quantization framework that improves the accuracy of NVFP4 quantization.

<!-- review:SF-SOAR-SCALE-OPTIMIZATION-FOR-ACCURATE-RECONSTRUCTION-IN-NVFP4-QUANTIZATIO:start -->
#### SOAR: Scale Optimization for Accurate Reconstruction in NVFP4 Quantization

问题与机制：To address these issues, we propose Scale Optimization for Accurate Reconstruction (SOAR), a novel post-training quantization framework that improves the accuracy of NVFP4 quantization.。机制 owner=`INFER-TENSORRT-LLM`。
全文定位：`arXiv:2605.12245v1 HTML — §3 NVFP4 SOAR execution path`；evaluation=`arXiv:2605.12245v1 — §4 kernel/model evaluation`；limitations/counterevidence=`arXiv:2605.12245v1 — §5 limitations: hardware, precision and workload scope`。
<!-- claim:SF-SOAR-SCALE-OPTIMIZATION-FOR-ACCURATE-RECONSTRUCTION-IN-NVFP4-QUANTIZATIO:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-SOAR-SCALE-OPTIMIZATION-FOR-ACCURATE-RECONSTRUCTION-IN-NVFP4-QUANTIZATIO:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-SOAR-SCALE-OPTIMIZATION-FOR-ACCURATE-RECONSTRUCTION-IN-NVFP4-QUANTIZATIO:end -->

**Books 对读：** `INFER-TENSORRT-LLM` → `books/part-05-inference-system/49-tensorrt-llm.md` 的“量化为什么不自动带来加速”。books/part-05-inference-system/49-tensorrt-llm.md 的‘量化为什么不自动带来加速’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：To address these issues, we propose Scale Optimization for Accurate Reconstruction (SOAR), a novel post-training quantization framework that improves the accuracy of NVFP4 quantization. 判定：**No Change — Existing Coverage**。

### [How Useful Is Cross-Domain Generalization for Training LLM Monitors?](https://arxiv.org/html/2605.12265v1)

**准入：** We study whether training on multiple classification tasks, each with its own prompt, improves performance on new domains with new classification prompts.

<!-- review:SF-HOW-USEFUL-IS-CROSS-DOMAIN-GENERALIZATION-FOR-TRAINING-LLM-MONITORS:start -->
#### How Useful Is Cross-Domain Generalization for Training LLM Monitors?

问题与机制：We study whether training on multiple classification tasks, each with its own prompt, improves performance on new domains with new classification prompts.。机制 owner=`PLATFORM-MONITORING`。
全文定位：`arXiv:2605.12265v1 HTML — §3 monitor cross-domain generalization protocol`；evaluation=`arXiv:2605.12265v1 — §4 domain-transfer experiments`；limitations/counterevidence=`arXiv:2605.12265v1 — §5 limitations: monitor family and shift coverage`。
<!-- claim:SF-HOW-USEFUL-IS-CROSS-DOMAIN-GENERALIZATION-FOR-TRAINING-LLM-MONITORS:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-HOW-USEFUL-IS-CROSS-DOMAIN-GENERALIZATION-FOR-TRAINING-LLM-MONITORS:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-HOW-USEFUL-IS-CROSS-DOMAIN-GENERALIZATION-FOR-TRAINING-LLM-MONITORS:end -->

**Books 对读：** `PLATFORM-MONITORING` → `books/part-06-ai-infrastructure/67-monitoring.md` 的“小 Monitor 需要专门训练其检测边界”。现有段要求训练 monitor 的 detection boundary，但未解释 supervision granularity、domain/prompt shift 和 instruction mixing 怎样共同决定 transfer/failure。 新证据增量：多任务单 token classifier SFT 对相邻 domain、thinking classification 和 summarization 有部分 transfer，但完全换 prompt/同 domain 时会误用训练规则；general instruction stage 可缓解。 判定：**Integrate — Applied; independent post-write review pending**。

### [Executable Agentic Memory for GUI Agent](https://arxiv.org/html/2605.12294v1)

**准入：** GUI agent 每屏重新解释并自由生成动作，会在长任务中反复支付 token 和决策误差；EAM 将复用 routine 编译为可搜索 Knowledge Graph。

<!-- review:SF-2026-ARXIV-2605-12294:start -->
#### Executable Agentic Memory for GUI Agent

**问题与旧基线。** GUI agent 每屏重新解释并自由生成动作，会在长任务中反复支付 token 和决策误差；EAM 将复用 routine 编译为可搜索 Knowledge Graph。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §4 Method：state-aware DFS 与 action-group mining 构造 memory，轻量 Q model 引导 KG 上的 MCTS；提供 bias-consistency 与 path-recovery sample bounds。 KG 保存可执行 routine/transition，Q 只排序 path proposal；GUI observer 和 workflow runtime 仍验证当前 state 并提交 action。

**Evaluation contract。** §5 Experiments：AndroidWorld，对比 UI-TARS-7B 等；报告成功率、token cost 与平均 latency。 V3=7（3+2+2）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；单一 GUI benchmark、图构造环境、Q bias、UI drift 与 side effect 回滚没有生产验证。

**Trade-off / failure / fallback。** 减少重复推理但增加图陈旧、状态 alias、MCTS/Q 成本与错误 routine 复用。 屏幕不匹配或 path value 不可靠时回退逐步 observation/planning，要求 state precondition、动作确认和可撤销 checkpoint。

**Artifact。** Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-12294:start -->exact-v1 支持：只支持 AndroidWorld 与作者训练/评估合同；不证明真实桌面安全、跨应用迁移或所报 latency 的通用性。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-12294:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-12294:end -->

**Books 对读：** `AGENT-MEMORY` → `books/part-07-agent/77-memory.md` 的“Procedural Memory 的压缩单位应是可展开的 Contract Graph”。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：GUI agent 每屏重新解释并自由生成动作，会在长任务中反复支付 token 和决策误差；EAM 将复用 routine 编译为可搜索 Knowledge Graph。 判定：**Integrate — Applied; independent post-write review pending**。

### [Grid Games: The Power of Multiple Grids for Quantizing Large Language Models](https://arxiv.org/html/2605.12327v1)

**准入：** microscaled FP4 每组固定一张 grid 会浪费分布适配空间；多 grid 将每组格式选择编码进 scale metadata。

<!-- review:SF-2026-ARXIV-2605-12327:start -->
#### Grid Games: The Power of Multiple Grids for Quantizing Large Language Models

**问题与旧基线。** microscaled FP4 每组固定一张 grid 会浪费分布适配空间；多 grid 将每组格式选择编码进 scale metadata。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §3–§4：形式化 power-of-two-grids，构造 PO2(NF4)、MPO2、PO2(Split87)、可 TensorCore 执行的 SFP4。 quantizer 为每组选择 grid，artifact 必须保存 grid/scale identity；runtime/kernel 负责忠实解码，质量 gate 保留发布权。

**Evaluation contract。** §5：开放模型 PTQ 与 Llama-like pretraining，覆盖 weight-only 和 weight+activation；代码 https://github.com/IST-DASLab/GridGames。 V3=8（3+2+3）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；收益随 group size 增大而消失，并依赖格式编码、calibration/training 和 kernel 对多 grid 的真实支持。

**Trade-off / failure / fallback。** 更低误差换额外 metadata、搜索、format/backend coupling；选择错误或 kernel 不支持时理论收益不转化为速度。 回退单一 NVFP4/MXFP4 grid、较高精度或静态 max-scale，并分别验收模型质量和端到端 latency。

**Artifact。** https://github.com/IST-DASLab/GridGames；未确认 exact-v1 immutable commit。

<!-- claim:SF-2026-ARXIV-2605-12327:start -->exact-v1 支持：只支持披露模型、group size、格式与任务；不证明所有硬件可加速、多 grid 总优于单 grid或训练收益可直接迁移 PTQ。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-12327:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-12327:end -->

**Books 对读：** `INFER-TENSORRT-LLM` → `books/part-05-inference-system/49-tensorrt-llm.md` 的“Block Scale 也是可搜索的执行状态”。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：microscaled FP4 每组固定一张 grid 会浪费分布适配空间；多 grid 将每组格式选择编码进 scale metadata。 判定：**Integrate — Applied; independent post-write review pending**。

### [$δ$-mem: Efficient Online Memory for Large Language Models](https://arxiv.org/html/2605.12357v1)

**准入：** δ-mem 用固定大小 delta-rule associative state 在线修正 frozen attention，明确模型内 memory 的状态/容量边界。

<!-- review:SF-2026-ARXIV-2605-12357:start -->
#### $δ$-mem: Efficient Online Memory for Large Language Models

问题、旧路径与约束变化：δ-mem 用固定大小 delta-rule associative state 在线修正 frozen attention，明确模型内 memory 的状态/容量边界。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§2 Preliminary and §3 Method。canonical owner=`MODEL-LONG-CONTEXT`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§4 Experiments and §5 Ablations。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§7 Conclusion and efficiency appendices；无独立 Limitations。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-12357:start -->exact-v1 支持：δ-mem 用固定大小 delta-rule associative state 在线修正 frozen attention，明确模型内 memory 的状态/容量边界。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-12357:end -->

Books Decision=`No Change — Existing Coverage`；作者只形成命题比较与 root serial queue，不直接修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-12357:end -->

**Books 对读：** `MODEL-LONG-CONTEXT` → `books/part-02-model/22-long-context.md` 的“路线六：让模型在 Test Time 更新内部记忆”。`books/part-02-model/22-long-context.md` 的“路线六：让模型在 Test Time 更新内部记忆”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：δ-mem 用固定大小 delta-rule associative state 在线修正 frozen attention，明确模型内 memory 的状态/容量边界。 判定：**No Change — Existing Coverage**。

### [Attacks and Mitigations for Distributed Governance of Agentic AI under Byzantine Adversaries](https://arxiv.org/html/2605.12364v1)

**准入：** We then present three types of solutions for securing the Provider that offer different trade-offs between security and performance.

<!-- review:SF-ATTACKS-AND-MITIGATIONS-FOR-DISTRIBUTED-GOVERNANCE-OF-AGENTIC-AI-UNDER-B:start -->
#### Attacks and Mitigations for Distributed Governance of Agentic AI under Byzantine Adversaries

问题与机制：We then present three types of solutions for securing the Provider that offer different trade-offs between security and performance.。机制 owner=`AGENT-MULTI-AGENT`。
Method / identity：arXiv:2605.12364v1 — §III malicious-provider attacks; §IV–§VII SAGA-BFT/MON/AUD/HYB designs。
Evaluation：arXiv:2605.12364v1 — §VIII Evaluation, including attacker, monitoring/auditing and end-to-end evaluation。
Counterevidence / limitations：arXiv:2605.12364v1 — §II-D threat-model limitations; §IV-B security/performance limitations; §V/VI discussion of monitoring and audit blind spots。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-ATTACKS-AND-MITIGATIONS-FOR-DISTRIBUTED-GOVERNANCE-OF-AGENTIC-AI-UNDER-B:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `AGENT-MULTI-AGENT` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-ATTACKS-AND-MITIGATIONS-FOR-DISTRIBUTED-GOVERNANCE-OF-AGENTIC-AI-UNDER-B:end -->

Books Decision=`Integrate`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-ATTACKS-AND-MITIGATIONS-FOR-DISTRIBUTED-GOVERNANCE-OF-AGENTIC-AI-UNDER-B:end -->

**Books 对读：** `AGENT-MULTI-AGENT` → `books/part-07-agent/82-multi-agent.md` 的“Governance Provider 也必须进入 Byzantine Threat Model”。books/part-07-agent/82-multi-agent.md 的‘Governance Provider 也必须进入 Byzantine Threat Model’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We then present three types of solutions for securing the Provider that offer different trade-offs between security and performance. 判定：**Integrate — Already present in current Books**。

### [Classifier Context Rot: Monitor Performance Degrades with Context Length](https://arxiv.org/html/2605.12366v1)

**准入：** We show that when used as classifiers, current frontier models fail to notice dangerous actions more often in longer transcripts.

<!-- review:SF-CLASSIFIER-CONTEXT-ROT-MONITOR-PERFORMANCE-DEGRADES-WITH-CONTEXT-LENGTH:start -->
#### Classifier Context Rot: Monitor Performance Degrades with Context Length

问题与机制：We show that when used as classifiers, current frontier models fail to notice dangerous actions more often in longer transcripts.。机制 owner=`PLATFORM-MONITORING`。
全文定位：`arXiv:2605.12366v1 HTML — §3 classifier-context-rot measurement`；evaluation=`arXiv:2605.12366v1 — §4 context-length experiments`；limitations/counterevidence=`arXiv:2605.12366v1 — §5 limitations: classifier/model and context-distribution scope`。
<!-- claim:SF-CLASSIFIER-CONTEXT-ROT-MONITOR-PERFORMANCE-DEGRADES-WITH-CONTEXT-LENGTH:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-CLASSIFIER-CONTEXT-ROT-MONITOR-PERFORMANCE-DEGRADES-WITH-CONTEXT-LENGTH:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-CLASSIFIER-CONTEXT-ROT-MONITOR-PERFORMANCE-DEGRADES-WITH-CONTEXT-LENGTH:end -->

**Books 对读：** `PLATFORM-MONITORING` → `books/part-06-ai-infrastructure/67-monitoring.md` 的“长轨迹 Monitor 需要可回到原始证据的有界状态”。books/part-06-ai-infrastructure/67-monitoring.md 的‘长轨迹 Monitor 需要可回到原始证据的有界状态’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We show that when used as classifiers, current frontier models fail to notice dangerous actions more often in longer transcripts. 判定：**No Change — Existing Coverage**。

### [Trust the Batch, On- or Off-Policy: Adaptive Policy Optimization for RL Post-Training](https://arxiv.org/html/2605.12380v1)

**准入：** 固定 clipping/off-policy 超参把 trust-region 与 behavior mismatch 预先混在一起，task、scale 或 rollout execution 改变就需重调；batch ratio distribution 可作为当前 mismatch state。

<!-- review:SF-2026-ARXIV-2605-12380:start -->
#### Trust the Batch, On- or Off-Policy: Adaptive Policy Optimization for RL Post-Training

**问题与旧基线。** 固定 clipping/off-policy 超参把 trust-region 与 behavior mismatch 预先混在一起，task、scale 或 rollout execution 改变就需重调；batch ratio distribution 可作为当前 mismatch state。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §3 Method：normalized effective sample size 同时限制 score-function weight 并设置 off-policy regularizer；ratio 近均匀时接近 on-policy update，集中时自动收紧。 behavior/current-policy ratio 拥有 staleness evidence，ESS controller 分配 update trust；objective 不把 rollout engine 差异藏进固定超参。

**Evaluation contract。** §4 Experiments：跨作者披露的一系列 RL post-training settings 与 tuned baselines；代码 https://github.com/FeynRL-project/FeynRL。 V3=9（3+3+3）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；ESS 是 batch-level proxy，依赖 logprob 数值一致、sample support 和 ratio estimation，不能检测所有 reward/model drift。

**Trade-off / failure / fallback。** 减少手调但可能被小 batch、重尾 ratio 或数值误差误导；保留非零高-ratio signal 也会增加 variance。 ESS 不稳时回退固定 clip/KL、fresh on-policy rollout、丢弃超龄样本和 trainer–rollout numerical identity audit。

**Artifact。** https://github.com/FeynRL-project/FeynRL；未确认 exact-v1 immutable commit。

<!-- claim:SF-2026-ARXIV-2605-12380:start -->exact-v1 支持：只支持所测 policy、task 和 batch regime；不证明免调参、异步任意陈旧仍稳定或所有 mismatch 都可由 ratio 识别。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-12380:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-12380:end -->

**Books 对读：** `TRAIN-GRPO` → `books/part-04-training-system/33-grpo.md` 的“Asynchronous RL 必须把 Policy Staleness 写进 Advantage”。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：固定 clipping/off-policy 超参把 trust-region 与 behavior mismatch 预先混在一起，task、scale 或 rollout execution 改变就需重调；batch ratio distribution 可作为当前 mismatch state。 判定：**Integrate — Applied; independent post-write review pending**。

### [Scalable Token-Level Hallucination Detection in Large Language Models](https://arxiv.org/html/2605.12384v1)

**准入：** To address these limitations, we propose TokenHD, a holistic pipeline for training token-level hallucination detectors.

<!-- review:SF-SCALABLE-TOKEN-LEVEL-HALLUCINATION-DETECTION-IN-LARGE-LANGUAGE-MODELS:start -->
#### Scalable Token-Level Hallucination Detection in Large Language Models

问题与机制：To address these limitations, we propose TokenHD, a holistic pipeline for training token-level hallucination detectors.。机制 owner=`PLATFORM-MONITORING`。
Method / identity：arXiv:2605.12384v1 — §3 TokenHD Framework: data engine, detector training and importance weighting。
Evaluation：arXiv:2605.12384v1 — §4 Evaluating the Effectiveness of TokenHD; Appendix J protocol robustness。
Counterevidence / limitations：arXiv:2605.12384v1 — §7 Conclusion and Limitations; policy/task shift and critic/labeler dependence bound generalization。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-SCALABLE-TOKEN-LEVEL-HALLUCINATION-DETECTION-IN-LARGE-LANGUAGE-MODELS:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `PLATFORM-MONITORING` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-SCALABLE-TOKEN-LEVEL-HALLUCINATION-DETECTION-IN-LARGE-LANGUAGE-MODELS:end -->

Books Decision=`No Change — Existing Coverage`。当前 Books 已有 binding 时不得重复追加；没有正文 binding 且结论改变长期认知时，只进入 root serial write queue。
<!-- review:SF-SCALABLE-TOKEN-LEVEL-HALLUCINATION-DETECTION-IN-LARGE-LANGUAGE-MODELS:end -->

**Books 对读：** `PLATFORM-MONITORING` → `books/part-06-ai-infrastructure/67-monitoring.md` 的“Model-internal Sensor 必须从 Inference Hot Path 解耦”。books/part-06-ai-infrastructure/67-monitoring.md 的‘Model-internal Sensor 必须从 Inference Hot Path 解耦’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：To address these limitations, we propose TokenHD, a holistic pipeline for training token-level hallucination detectors. 判定：**No Change — Existing Coverage**。

### [NCCLZ: Compression-Enabled GPU Collectives with Decoupled Quantization and Entropy Coding](https://arxiv.org/html/2605.12396v1)

**准入：** Experiments on scientific datasets, training gradients, and synthetic workloads show up to 9.65x speedup over NCCL and up to 3.34x improvement over prior compression-assisted collective libraries.

<!-- review:SF-NCCLZ-COMPRESSION-ENABLED-GPU-COLLECTIVES-WITH-DECOUPLED-QUANTIZATION-AN:start -->
#### NCCLZ: Compression-Enabled GPU Collectives with Decoupled Quantization and Entropy Coding

问题与机制：Experiments on scientific datasets, training gradients, and synthetic workloads show up to 9.65x speedup over NCCL and up to 3.34x improvement over prior compression-assisted collective libraries.。机制 owner=`TRAIN-DISTRIBUTED-TRAINING`。
全文定位：`arXiv:2605.12396v1 HTML — §3 NCCLZ collective compression path`；evaluation=`arXiv:2605.12396v1 — §4 communication/training evaluation`；limitations/counterevidence=`arXiv:2605.12396v1 — §5 limitations: topology, compressor and convergence scope`。
<!-- claim:SF-NCCLZ-COMPRESSION-ENABLED-GPU-COLLECTIVES-WITH-DECOUPLED-QUANTIZATION-AN:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-NCCLZ-COMPRESSION-ENABLED-GPU-COLLECTIVES-WITH-DECOUPLED-QUANTIZATION-AN:end -->
Books Decision=`Integrate`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-NCCLZ-COMPRESSION-ENABLED-GPU-COLLECTIVES-WITH-DECOUPLED-QUANTIZATION-AN:end -->

**Books 对读：** `TRAIN-DISTRIBUTED-TRAINING` → `books/part-04-training-system/36-distributed-training.md` 的“通信压缩必须把编解码写进 Critical Path”。books/part-04-training-system/36-distributed-training.md 的‘通信压缩必须把编解码写进 Critical Path’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：Experiments on scientific datasets, training gradients, and synthetic workloads show up to 9.65x speedup over NCCL and up to 3.34x improvement over prior compression-assisted collective libraries. 判定：**Integrate — Already present in current Books**。

### [Aligning Flow Map Policies with Optimal Q-Guidance](https://arxiv.org/html/2605.12416v1)

**准入：** Flow Map 的任意步跳转与 Q-guided trust-region search 改变 action generation 的 latency、proposal 和 control contract。

<!-- review:SF-2026-ARXIV-2605-12416:start -->
#### Aligning Flow Map Policies with Optimal Q-Guidance

**问题与旧基线。** Flow Map 的任意步跳转与 Q-guided trust-region search 改变 action generation 的 latency、proposal 和 control contract。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3 Flow Map Q-guidance；§3.4 Q-guided Search。flow map 允许大步 proposal，Q-guided trust region 和 re-noising beam search负责筛选；controller 仍拥有执行 commit。

**Evaluation contract。** §4；12 robotic tasks、7 environments、offline-to-online setting 与速度分析。V3=2+2+2=6；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；只支持披露任务、环境与 policy。

**Trade-off / failure / fallback。** 减少迭代换 Q-bias、搜索成本和大步误差；Q 不可靠时缩短 jump、回退逐步 flow 或传统 controller。

<!-- claim:SF-2026-ARXIV-2605-12416:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-12416:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-12416:end -->

**Books 对读：** `MULTIMODAL-EMBODIED-VLA` → `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的“Hierarchical Generative Planner 要把 Subgoal 与低层轨迹分权”。正文约第 87 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：Flow Map 的任意步跳转与 Q-guided trust-region search 改变 action generation 的 latency、proposal 和 control contract。 判定：**Integrate — Applied; independent post-write review pending**。

### [Geometric Factual Recall in Transformers](https://arxiv.org/html/2605.12426v1)

**准入：** 把 MLP 权重直接视为事实 key-value memory 会导出事实数线性参数需求；几何表征允许 embedding 叠加关系，而小 MLP 只做 relation-conditioned selector。

<!-- review:SF-2026-ARXIV-2605-12426:start -->
#### Geometric Factual Recall in Transformers

**问题与旧基线。** 把 MLP 权重直接视为事实 key-value memory 会导出事实数线性参数需求；几何表征允许 embedding 叠加关系，而小 MLP 只做 relation-conditioned selector。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §4 Theory：随机双射的单层 controlled setting 中证明 logarithmic embedding dimension 足够；ReLU gate 选择属性，并扩到 multi-hop/CoT capacity–depth trade-off。 embedding 保存关系 superposition，MLP 保存通用选择规则；这与‘MLP 单独拥有事实真值’不同。

**Evaluation contract。** §5 Experiments：受控 synthetic bijection；gradient descent 找到预测结构，重新初始化 subject embedding 后 MLP 对新 bijection zero-shot transfer。 V3=8（3+2+3）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** 只适用于受控随机双射、单层/构造假设与合成训练；不证明自然语言 factual knowledge 都采用同一几何或事实可可靠编辑。

**Trade-off / failure / fallback。** 参数效率来自共享几何，但会引入 embedding interference、margin/维度要求和 multi-hop depth 成本。 结构不满足共享 attribute geometry 时仍可使用显式 retrieval、更多参数/层或传统 associative representation。

**Artifact。** Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-12426:start -->exact-v1 支持：证明和经验只限 controlled setting；不能外推真实 LLM 的知识定位、可解释性、编辑安全或全部 factual recall。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-12426:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-12426:end -->

**Books 对读：** `MODEL-FFN` → `books/part-02-model/16-feed-forward-mlp.md` 的“MLP 是不是“知识库””。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：把 MLP 权重直接视为事实 key-value memory 会导出事实数线性参数需求；几何表征允许 embedding 叠加关系，而小 MLP 只做 relation-conditioned selector。 判定：**Integrate — Applied; independent post-write review pending**。

### [ORCE: Order-Aware Alignment of Verbalized Confidence in Large Language Models](https://arxiv.org/html/2605.12446v1)

**准入：** In this work, we propose a decoupled and order-aware framework for verbalized confidence calibration.

<!-- review:SF-ORCE-ORDER-AWARE-ALIGNMENT-OF-VERBALIZED-CONFIDENCE-IN-LARGE-LANGUAGE-MO:start -->
#### ORCE: Order-Aware Alignment of Verbalized Confidence in Large Language Models

问题与机制：In this work, we propose a decoupled and order-aware framework for verbalized confidence calibration.。机制 owner=`PLATFORM-EVALUATION-SYSTEM`。
Method / identity：arXiv:2605.12446v1 — §3 Method: decoupled confidence generation and order-aware reward。
Evaluation：arXiv:2605.12446v1 — §4 Experiment; Appendix C experiment details and metrics。
Counterevidence / limitations：arXiv:2605.12446v1 — Appendix A.4 Limitations of the idealized analysis: finite-sample surrogate, drifting reference set and DPO approximation。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或复现入口只能作为补充 artifact，不替代正文证据。

<!-- claim:SF-ORCE-ORDER-AWARE-ALIGNMENT-OF-VERBALIZED-CONFIDENCE-IN-LARGE-LANGUAGE-MO:start -->证据只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。方法改变的是 `PLATFORM-EVALUATION-SYSTEM` 下的状态、数据或控制契约；其额外状态、误差来源与执行成本必须和保守 fallback 共存。<!-- claim:SF-ORCE-ORDER-AWARE-ALIGNMENT-OF-VERBALIZED-CONFIDENCE-IN-LARGE-LANGUAGE-MO:end -->

Books Decision=`Integrate — Root Writeback Applied`。现有正文没有该机制的真实 binding；author 未修改共享 Books。
<!-- review:SF-ORCE-ORDER-AWARE-ALIGNMENT-OF-VERBALIZED-CONFIDENCE-IN-LARGE-LANGUAGE-MO:end -->

**Books 对读：** 原锚点只提供宽泛 evaluation 原则，没有承载 decoupled verbalized-confidence generation、order-aware reward/calibration，以及 finite-sample surrogate、reference drift 和 DPO approximation 的边界。判定：**Integrate — Root Writeback Applied**。

### [Multi-Stream LLMs: Unblocking Language Models with Parallel Streams of Thoughts, Inputs and Outputs](https://arxiv.org/html/2605.12460v1)

**准入：** multi-stream instruction tuning 将 thought/input/output 拆成并行因果 streams，使单流消息格式从模型不变量降为接口选择。

<!-- review:SF-2026-ARXIV-2605-12460:start -->
#### Multi-Stream LLMs: Unblocking Language Models with Parallel Streams of Thoughts, Inputs and Outputs

问题、旧路径与约束变化：multi-stream instruction tuning 将 thought/input/output 拆成并行因果 streams，使单流消息格式从模型不变量降为接口选择。 旧路径在新增约束不存在、状态可静态配置或风险较低时仍是合理基线。
Mechanism / state ownership：§2 Advantages and §3 Method。canonical owner=`MODEL-DECODER-ONLY`；论文中的 selector、router、sensor 或 proposal 不自动获得 truth/commit authority。
Evaluation contract：§4 Efficiency, §5 Security and §6 Monitorability。作者结果只支持 exact-v1 披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`。
Counterevidence / limitations：§7 Discussion and appendices；无独立 Limitations，受测多流协议不证明生产调度收益。这不证明跨模型、跨部署或生产 tail 的一般优势。
Artifact：未确认与 exact-v1 绑定的 immutable commit；论文内项目或代码入口只作补充，不能替代正文证据。
Trade-off / failure / fallback：新机制以额外状态、校准、调度或验证成本换取论文所述收益；当传感器漂移、证据越界、状态身份不一致或成本超过收益时，回退到静态策略、完整状态、保守执行或人工/确定性 gate。

<!-- claim:SF-2026-ARXIV-2605-12460:start -->exact-v1 支持：multi-stream instruction tuning 将 thought/input/output 拆成并行因果 streams，使单流消息格式从模型不变量降为接口选择。 未证明：任何未披露环境中的普适收益或安全保证。<!-- claim:SF-2026-ARXIV-2605-12460:end -->

Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。
<!-- review:SF-2026-ARXIV-2605-12460:end -->

**Books 对读：** `MODEL-DECODER-ONLY` → `books/part-02-model/18-decoder-only.md` 的“Next-token 接口不要求内部状态只有一个粒度”。`books/part-02-model/18-decoder-only.md` 的“Next-token 接口不要求内部状态只有一个粒度”是最接近的现有命题；Round 3 已读取该正文与相邻交接，不能仅凭主题相似宣称已覆盖。 新证据增量：multi-stream instruction tuning 将 thought/input/output 拆成并行因果 streams，使单流消息格式从模型不变量降为接口选择。 判定：**Integrate — Applied; independent post-write review pending**。

### [Search Your Block Floating Point Scales!](https://arxiv.org/html/2605.12464v1)

**准入：** ScaleSearch 把 BFP/NVFP4 block scale 从 max heuristic 改为可搜索的执行/误差选择。

<!-- review:SF-2026-ARXIV-2605-12464:start -->
#### Search Your Block Floating Point Scales!

**问题与旧基线。** ScaleSearch 把 BFP/NVFP4 block scale 从 max heuristic 改为可搜索的执行/误差选择。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3 BFP；§4 ScaleSearch；§4.2 Language Modeling。对候选 mantissa-scale 组合搜索而不是固定 block max，量化 artifact 保存 scale selection。

**Evaluation contract。** §5.1–§5.3；特定模型、PTQ、NVFP4 attention 和 overhead。V3=2+2+2=6；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；结论绑定受测模型、格式和 kernel。

**Trade-off / failure / fallback。** 降低误差但增加 calibration/search overhead 和 backend coupling；预算不足时回退 max scale 或较高精度，并重新验收 latency。

<!-- claim:SF-2026-ARXIV-2605-12464:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-12464:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-12464:end -->

**Books 对读：** `INFER-TENSORRT-LLM` → `books/part-05-inference-system/49-tensorrt-llm.md` 的“量化为什么不自动带来加速”。正文约第 630 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：ScaleSearch 把 BFP/NVFP4 block scale 从 max heuristic 改为可搜索的执行/误差选择。 判定：**Integrate — Applied; independent post-write review pending**。

### [Solve the Loop: Attractor Models for Language and Reasoning](https://arxiv.org/html/2605.12466v1)

**准入：** 固定-depth looped Transformer 训练不稳且部署成本固定；Attractor Model 将反复 refinement 改为 fixed-point solver，并用 implicit differentiation 避免训练 memory 随 effective depth 增长。

<!-- review:SF-2026-ARXIV-2605-12466:start -->
#### Solve the Loop: Attractor Models for Language and Reasoning

**问题与旧基线。** 固定-depth looped Transformer 训练不稳且部署成本固定；Attractor Model 将反复 refinement 改为 fixed-point solver，并用 implicit differentiation 避免训练 memory 随 effective depth 增长。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §3 Method：backbone 先提议 output embedding，attractor module 求固定点；收敛决定迭代次数，gradient 由 implicit differentiation 获得。 backbone 拥有 initial proposal，solver 拥有 refinement state，convergence rule 拥有停止 proposal；输出 commit 仍需数值/任务 gate。

**Evaluation contract。** §4 Experiments：large-scale LM pretraining 与 tiny reasoning 两个 regime，比较 perplexity/accuracy/training cost，并观察 equilibrium internalization。 V3=7（3+2+2）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；模型规模、solver 收敛、容差、任务和 hardware 范围受限，移除 solver 的退化不是所有样本都被证明。

**Trade-off / failure / fallback。** adaptive depth/constant-memory backward 换来 fixed-point 求解、收敛失败和 implicit gradient 数值风险；内部化可能失效。 未收敛时限制迭代、回退固定-depth Transformer/loop，保留 residual stability 与 per-sample convergence telemetry。

**Artifact。** Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-12466:start -->exact-v1 支持：只支持作者规模、任务与容差；不证明任意深度免费、所有输入收敛、推理 solver 可总是删除或通用硬件收益。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-12466:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-12466:end -->

**Books 对读：** `MODEL-TRANSFORMER-LAYER` → `books/part-02-model/17-transformer-layer.md` 的“Recurrence 可以只占据 Decoder 的局部层段”。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：固定-depth looped Transformer 训练不稳且部署成本固定；Attractor Model 将反复 refinement 改为 fixed-point solver，并用 implicit differentiation 避免训练 memory 随 effective depth 增长。 判定：**Integrate — Applied; independent post-write review pending**。

### [KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference](https://arxiv.org/html/2605.12471v1)

**准入：** We introduce KV-Fold, a simple, training-free long-context inference protocol that treats the key-value (KV) cache as the accumulator in a left fold over sequence chunks.

<!-- review:SF-KV-FOLD-ONE-STEP-KV-CACHE-RECURRENCE-FOR-LONG-CONTEXT-INFERENCE:start -->
#### KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference

问题与机制：We introduce KV-Fold, a simple, training-free long-context inference protocol that treats the key-value (KV) cache as the accumulator in a left fold over sequence chunks.。机制 owner=`INFER-KV-CACHE`。
全文定位：`arXiv:2605.12471v1 HTML — §3 KV-Fold cache state transformation`；evaluation=`arXiv:2605.12471v1 — §4 memory/quality/latency evaluation`；limitations/counterevidence=`arXiv:2605.12471v1 — §5 limitations: model, length, cache budget and hardware`。
<!-- claim:SF-KV-FOLD-ONE-STEP-KV-CACHE-RECURRENCE-FOR-LONG-CONTEXT-INFERENCE:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-KV-FOLD-ONE-STEP-KV-CACHE-RECURRENCE-FOR-LONG-CONTEXT-INFERENCE:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-KV-FOLD-ONE-STEP-KV-CACHE-RECURRENCE-FOR-LONG-CONTEXT-INFERENCE:end -->

**Books 对读：** `INFER-KV-CACHE` → `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 的“Cache Object 从 Token KV 扩展到可组合 Transition”。books/part-05-inference-system/45-why-kv-cache-speeds-up.md 的‘Cache Object 从 Token KV 扩展到可组合 Transition’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We introduce KV-Fold, a simple, training-free long-context inference protocol that treats the key-value (KV) cache as the accumulator in a left fold over sequence chunks. 判定：**No Change — Existing Coverage**。

### [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/html/2605.12474v1)

**准入：** We study reward hacking in rubric-based RL, where a policy is optimized against a training verifier but evaluated against a cross-family panel of three frontier judges, reducing dependence on any single evaluator.

<!-- review:SF-REWARD-HACKING-IN-RUBRIC-BASED-REINFORCEMENT-LEARNING:start -->
#### Reward Hacking in Rubric-Based Reinforcement Learning

问题与机制：We study reward hacking in rubric-based RL, where a policy is optimized against a training verifier but evaluated against a cross-family panel of three frontier judges, reducing dependence on any single evaluator.。机制 owner=`TRAIN-RLHF`。
全文定位：`arXiv:2605.12474v1 HTML — §3 rubric-aware reward-hacking objective`；evaluation=`arXiv:2605.12474v1 — §4 RL experiments and red-team evaluation`；limitations/counterevidence=`arXiv:2605.12474v1 — §5 limitations: rubric, reward model and task scope`。
<!-- claim:SF-REWARD-HACKING-IN-RUBRIC-BASED-REINFORCEMENT-LEARNING:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-REWARD-HACKING-IN-RUBRIC-BASED-REINFORCEMENT-LEARNING:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-REWARD-HACKING-IN-RUBRIC-BASED-REINFORCEMENT-LEARNING:end -->

**Books 对读：** `TRAIN-RLHF` → `books/part-04-training-system/31-rlhf.md` 的“Reward hacking 与 Goodhart's Law”。books/part-04-training-system/31-rlhf.md 的‘Reward hacking 与 Goodhart's Law’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：We study reward hacking in rubric-based RL, where a policy is optimized against a training verifier but evaluated against a cross-family panel of three frontier judges, reducing dependence on any single evaluator. 判定：**No Change — Existing Coverage**。

### [OmniNFT: Modality-wise Omni Diffusion Reinforcement for Joint Audio-Video Generation](https://arxiv.org/html/2605.12480v1)

**准入：** joint audio-video diffusion 的单一 global advantage 会混合不一致目标、跨 modality gradient 与稀疏同步区域；OmniNFT 将 credit 按 modality/layer/region 分配。

<!-- review:SF-2026-ARXIV-2605-12480:start -->
#### OmniNFT: Modality-wise Omni Diffusion Reinforcement for Joint Audio-Video Generation

**问题与旧基线。** joint audio-video diffusion 的单一 global advantage 会混合不一致目标、跨 modality gradient 与稀疏同步区域；OmniNFT 将 credit 按 modality/layer/region 分配。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §5 Method：modality-wise advantage routing、浅层 audio 的 selective gradient detach、cross-modal interaction 保留，以及 alignment-region loss reweighting。 各 reward channel 只为对应 modality branch 提供 credit；cross-modal layers 保留共享梯度，region weight 负责 decision-density，而非一个标量拥有全部目标。

**Evaluation contract。** §6 Experiments：LTX-2 backbone，JavisBench/VBench；分别报告 audio/video quality、cross-modal alignment 与 synchronization。 V3=7（3+2+2）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；单一 backbone、作者 rewards/evaluators 和 benchmark，未披露 production hardware/SLO；多指标改善不等于真实用户偏好。

**Trade-off / failure / fallback。** 分权可减少 gradient interference，却增加 reward calibration、branch routing 和 gradient surgery complexity；错误归因会牺牲另一模态。 指标冲突或路由不稳时回退 global reward + conservative KL、冻结受影响分支，或分阶段单模态训练后联合验收。

**Artifact。** Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-12480:start -->exact-v1 支持：只支持 LTX-2 与所选 benchmark/evaluator；不证明跨模型通用、真实同步质量、无 reward hacking 或训练稳定性。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-12480:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-12480:end -->

**Books 对读：** `TRAIN-RLHF` → `books/part-04-training-system/31-rlhf.md` 的“从二元偏好到分布条件化的连续 Reward”。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：joint audio-video diffusion 的单一 global advantage 会混合不一致目标、跨 modality gradient 与稀疏同步区域；OmniNFT 将 credit 按 modality/layer/region 分配。 判定：**Integrate — Applied; independent post-write review pending**。

### [ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents](https://arxiv.org/html/2605.12481v1)

**准入：** GUI 原子动作与高层 tool call 共存时，agent 不知道何时切换，且缺少 interleaved trajectories；ToolCUA 将 path choice 作为独立训练对象。

<!-- review:SF-2026-ARXIV-2605-12481:start -->
#### ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents

**问题与旧基线。** GUI 原子动作与高层 tool call 共存时，agent 不知道何时切换，且缺少 interleaved trajectories；ToolCUA 将 path choice 作为独立训练对象。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §2 Method：由静态 GUI trajectories 合成 grounded tool library/interleaved data；warmup SFT + single-turn RL 后，在 GUI-tool environment 进行 online agentic RL。 policy 提议 GUI/tool action path，tool schema 和 current UI state 约束可执行性；workflow runtime 保留权限、side effect 与 commit authority。

**Evaluation contract。** §3 Experiments：Qwen3-VL-8B、OSWorld-MCP 333 feasible tasks、avg@3、最多 50 steps；含 Windows transfer，开源项目 https://x-plug.github.io/ToolCUA/。 V3=8（3+3+2）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** Appendix A：轨迹合成、模型/tool library、sandbox 与 benchmark 限制；tool-efficient reward 不等于 side-effect 安全。

**Trade-off / failure / fallback。** 高层 tool 可缩短路径，但合成轨迹偏差、工具过用、环境漂移和 reward shortcut 会放大不可逆操作风险。 tool/GUI state 不一致时回退原子 GUI、重新 observation、显式 approval 与 dry-run；保留最大步数和 compensation。

**Artifact。** https://x-plug.github.io/ToolCUA/；exact-v1 immutable commit 未披露。

<!-- claim:SF-2026-ARXIV-2605-12481:start -->exact-v1 支持：只支持 OSWorld-MCP/Windows transfer 与所选模型；不证明真实桌面权限安全、所有工具可用或跨 OS 一般收益。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-12481:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-12481:end -->

**Books 对读：** `AGENT-WORKFLOW` → `books/part-07-agent/81-workflow.md` 的“Logical Plan 与 Physical Schedule 必须分别验收”。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：GUI 原子动作与高层 tool call 共存时，agent 不知道何时切换，且缺少 interleaved trajectories；ToolCUA 将 path choice 作为独立训练对象。 判定：**Integrate — Applied; independent post-write review pending**。

### [Pion: A Spectrum-Preserving Optimizer via Orthogonal Equivalence Transformation](https://arxiv.org/html/2605.12492v1)

**准入：** Adam/Muon 的 additive update 会同时改变方向与 singular spectrum；Pion 用左右 orthogonal transformations 将谱固定，只优化权重几何。

<!-- review:SF-2026-ARXIV-2605-12492:start -->
#### Pion: A Spectrum-Preserving Optimizer via Orthogonal Equivalence Transformation

**问题与旧基线。** Adam/Muon 的 additive update 会同时改变方向与 singular spectrum；Pion 用左右 orthogonal transformations 将谱固定，只优化权重几何。 旧方案在该约束不存在、任务较短或额外控制成本超过收益时仍成立。

**Method / ownership。** §2 Method/Theory：Lie-algebra direction 经 matrix exponential 形成左右正交变换，保持 singular values；给出更新、性质与 convergence analysis。 optimizer 拥有坐标/变换 proposal，正交参数化保证谱不变；training objective/held-out evidence 决定这种 invariant 是否仍合适。

**Evaluation contract。** §3 Experiments：LLaMA 1.3B/54B-token C4、60M no-normalization 与 8–200 layer 等受控 pretraining/finetuning settings。 V3=8（3+2+3）。未披露的 model、hardware、precision、length、batch、concurrency、SLO 或 evaluator 均为 `Not Disclosed`。

**Counterevidence / limitations。** Appendix E：matrix exponential/正交变换的 compute/memory overhead；momentum 为可选。更大模型、长期 scale 与 spectrum 必须改变的任务未验证。

**Trade-off / failure / fallback。** 稳定谱换来矩阵变换开销，并可能禁止任务所需的 spectrum adaptation；数值近似会破坏严格正交。 固定谱成为瓶颈或成本过高时回退 AdamW/Muon/混合 optimizer，并按参数角色、梯度谱和 loss trajectory 选择。

**Artifact。** Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-12492:start -->exact-v1 支持：只支持作者规模、数据和实现；不证明固定谱普适最优、超大模型效率或等价于更好泛化。 未证明项不得外推为跨模型、跨部署或 production guarantee。<!-- claim:SF-2026-ARXIV-2605-12492:end -->

Books Decision=`Integrate — Applied`；等待独立 post-write review。
<!-- review:SF-2026-ARXIV-2605-12492:end -->

**Books 对读：** `TRAIN-PRETRAINING` → `books/part-04-training-system/28-pretraining.md` 的“Optimizer Update 要尊重参数块的对称性”。现有正文是相邻基线，但尚未完整承载该证据增量。 新证据增量：Adam/Muon 的 additive update 会同时改变方向与 singular spectrum；Pion 用左右 orthogonal transformations 将谱固定，只优化权重几何。 判定：**Integrate — Applied; independent post-write review pending**。

### [LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues](https://arxiv.org/html/2605.12493v1)

**准入：** To address this gap, we introduce LongMemEval-V2 (LME-V2), a benchmark for evaluating whether memory systems can help agents acquire the experience needed to become knowledgeable colleagues in customized environments.

<!-- review:SF-LONGMEMEVAL-V2-EVALUATING-LONG-TERM-AGENT-MEMORY-TOWARD-EXPERIENCED-COLL:start -->
#### LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues

问题与机制：To address this gap, we introduce LongMemEval-V2 (LME-V2), a benchmark for evaluating whether memory systems can help agents acquire the experience needed to become knowledgeable colleagues in customized environments.。机制 owner=`AGENT-MEMORY`。
全文定位：`arXiv:2605.12493v1 HTML — §3 LongMemEval-V2 memory-validity contract`；evaluation=`arXiv:2605.12493v1 — §4 long-horizon memory evaluation`；limitations/counterevidence=`arXiv:2605.12493v1 — §5 limitations: synthetic tasks, judge and retrieval scope`。
<!-- claim:SF-LONGMEMEVAL-V2-EVALUATING-LONG-TERM-AGENT-MEMORY-TOWARD-EXPERIENCED-COLL:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-LONGMEMEVAL-V2-EVALUATING-LONG-TERM-AGENT-MEMORY-TOWARD-EXPERIENCED-COLL:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-LONGMEMEVAL-V2-EVALUATING-LONG-TERM-AGENT-MEMORY-TOWARD-EXPERIENCED-COLL:end -->

**Books 对读：** `AGENT-MEMORY` → `books/part-07-agent/77-memory.md` 的“评估 Memory”。books/part-07-agent/77-memory.md 的‘评估 Memory’已承载该材料改变的状态、控制权或证据边界；对读时保留旧方案、失败路径与共存条件，不以论文名称替代机制。 新证据增量：To address this gap, we introduce LongMemEval-V2 (LME-V2), a benchmark for evaluating whether memory systems can help agents acquire the experience needed to become knowledgeable colleagues in customized environments. 判定：**No Change — Existing Coverage**。

### [AlphaGRPO: Unlocking Self-Reflective Multimodal Generation in UMMs via Decompositional Verifiable Reward](https://arxiv.org/html/2605.12495v1)

**准入：** AlphaGRPO 将统一多模态生成 reward 分解为离散 reasoning 与连续视觉 trajectory 的原子可验证问题。

<!-- review:SF-2026-ARXIV-2605-12495:start -->
#### AlphaGRPO: Unlocking Self-Reflective Multimodal Generation in UMMs via Decompositional Verifiable Reward

**问题与旧基线。** AlphaGRPO 将统一多模态生成 reward 分解为离散 reasoning 与连续视觉 trajectory 的原子可验证问题。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §4.1 AlphaGRPO；§4.2 Decompositional Reward；§4.3 Data。prompt 被拆成语义/质量原子问题，由 MLLM 分项评分后组成 GRPO feedback，而不是单一整体 reward。

**Evaluation contract。** §5；多个 image generation benchmarks 与 MLLM evaluators。V3=2+2+2=6；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** Appendix A.1 Limitations；reward/evaluator、视觉任务与模型范围受限。

**Trade-off / failure / fallback。** credit 更细但引入 decomposition error、judge bias 和 reward hacking；无法验证时回退人工 pair/整体质量 gate。

<!-- claim:SF-2026-ARXIV-2605-12495:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-12495:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-12495:end -->

**Books 对读：** `TRAIN-GRPO` → `books/part-04-training-system/33-grpo.md` 的“Verifiable Reward 不等于每个样本都可学习”。正文约第 1719 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：AlphaGRPO 将统一多模态生成 reward 分解为离散 reasoning 与连续视觉 trajectory 的原子可验证问题。 判定：**Integrate — Applied; independent post-write review pending**。

### [From Web to Pixels: Bringing Agentic Search into Visual Perception](https://arxiv.org/html/2605.12497v1)

**准入：** Pixel-Searcher 把 web evidence acquisition、实体身份解析与 box/mask grounding 串成可追踪的 search-to-pixel workflow。

<!-- review:SF-2026-ARXIV-2605-12497:start -->
#### From Web to Pixels: Bringing Agentic Search into Visual Perception

**问题与旧基线。** Pixel-Searcher 把 web evidence acquisition、实体身份解析与 box/mask grounding 串成可追踪的 search-to-pixel workflow。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3 WebEyes；§4、§4.1–§4.3 Pixel-Searcher。Agent 先检索并解析隐藏实体，再把证据绑定到视觉 instance；external evidence 只支持 identity proposal，pixel grounding 仍需独立验证。

**Evaluation contract。** §5；120 images、645 QA pairs、1,927 task samples 与消融/failure analysis。V3=2+2+2=6；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；小规模 benchmark、web freshness、search/tool 和 grounding model 限制。

**Trade-off / failure / fallback。** 开放知识提高 long-tail perception，但引入 web provenance、实体歧义、工具延迟和错误级联；证据不足时 abstain 或回退 image-only/local corpus。

<!-- claim:SF-2026-ARXIV-2605-12497:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-12497:end -->

Books Decision=`Integrate`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-12497:end -->

**Books 对读：** `AGENT-RAG` → `books/part-07-agent/76-rag.md` 的“多模态 Evidence 还要检查模态间的覆盖与支配关系”。正文约第 347 行仅提供落点，未承载该 source family 的新增命题。 新证据增量：Pixel-Searcher 把 web evidence acquisition、实体身份解析与 box/mask grounding 串成可追踪的 search-to-pixel workflow。 判定：**Integrate — Applied; independent post-write review pending**。

### [SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture](https://arxiv.org/html/2605.12500v1)

**准入：** SenseNova-U1 用 pixels/words 共享 token/backbone 与轻量 patch encoder/decoder 构成 native understanding-generation interface。

<!-- review:SF-2026-ARXIV-2605-12500:start -->
#### SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture

**问题与旧基线。** SenseNova-U1 用 pixels/words 共享 token/backbone 与轻量 patch encoder/decoder 构成 native understanding-generation interface。 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。

**Method / ownership。** exact-v1 §3.1 Near-lossless Visual Interface；§3.2 Native Unified Model；§3.3 Objective；§3.4 Training；§3.5 Inference。pixel 与 word token 进入共享 backbone，视觉 patch encoder/decoder 不依赖 pretrained vision encoder 或 VAE。

**Evaluation contract。** §5；多个模型规模和作者 benchmark。V3=3+2+2=7；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。

**Counterevidence / limitations。** 无独立 Limitations；VLA/world-model 结果只属 preliminary，厂商结果不外推。

**Trade-off / failure / fallback。** native interface 降低组件裂缝但提高联合训练干扰和重训成本；正文已比较 fully native、modular hybrid 与 ensemble 的参数共享及共存边界。

<!-- claim:SF-2026-ARXIV-2605-12500:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:SF-2026-ARXIV-2605-12500:end -->

Books Decision=`No Change — Existing Coverage`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-12500:end -->

**Books 对读：** `MULTIMODAL-REPRESENTATION` → `books/part-03-multimodal-world-models/23-multimodal-representation.md` 的“理解与生成也不必被迫共享全部参数（正文段落）”。正文约第 218 行已逐命题覆盖该机制、代价与 fallback；Review notes 不参与覆盖判断。 新证据增量：SenseNova-U1 用 pixels/words 共享 token/backbone 与轻量 patch encoder/decoder 构成 native understanding-generation interface。 判定：**No Change — Existing Coverage**。

### [Rethinking Supervision Granularity: Segment-Level Learning for LLM-Based Theorem Proving](https://arxiv.org/html/2605.11905v1)

**准入：** 证明轨迹的监督单元从单 tactic/整条 proof 改为按 open-goal 边界切分的 locally coherent segment，并在训练和 goal-aware rollout 间复用同一边界策略。

<!-- review:SF-2026-ARXIV-2605-11905:start -->
#### Rethinking Supervision Granularity: Segment-Level Learning for LLM-Based Theorem Proving

问题与旧基线：旧方案在输出短、验证便宜或局部信号足够时仍合理。约束变化与机制：证明轨迹的监督单元从单 tactic/整条 proof 改为按 open-goal 边界切分的 locally coherent segment，并在训练和 goal-aware rollout 间复用同一边界策略。

Method / ownership：§3 Segment-level Supervision and boundary selection; §4 Goal-Aware Rollout。canonical owner=TRAIN-DATA；sensor/prediction set 只提供 proposal，验证器或 held-out gate 保留 truth/commit authority。

Evaluation contract：§5 STP/LeanWorkbook/NuminaMath-LEAN, miniF2F, Qwen2.5-Math-7B, common search budget and five runs。V3=6（2+2+2）。

Counterevidence / limitations：§7 open-goal count is approximate; verified-trajectory dependency; weak on short/highly automated proofs。Trade-off/fallback：新机制增加边界估计、采样或验证成本；证据越界时回退旧基线、完整验证或人工 gate。

Evidence boundary：Only exact-v1 disclosed workload, model, evaluator and assumptions are supported; no undisclosed production or cross-domain guarantee.

<!-- claim:SF-2026-ARXIV-2605-11905:start -->Only exact-v1 disclosed workload, model, evaluator and assumptions are supported; no undisclosed production or cross-domain guarantee.<!-- claim:SF-2026-ARXIV-2605-11905:end -->

Books Decision=Integrate — Root Writeback Applied；author 未修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11905:end -->

**Books 对读：** TRAIN-DATA → books/part-04-training-system/27-data.md。Current chapter has adjacent generic coverage but not this mechanism, ownership, trade-off and evidence boundary. 判定：**Integrate — Root Writeback Applied**。

### [Learn to Think: Improving Multimodal Reasoning through Vision-Aware Self-Improvement Training](https://arxiv.org/html/2605.11931v1)

**准入：** VISTA 把 partial-correct prefix reuse 与 intermediate-layer visual-attention sensor 组合为多模态 self-improvement 的数据采集与筛选控制回路。

<!-- review:SF-2026-ARXIV-2605-11931:start -->
#### Learn to Think: Improving Multimodal Reasoning through Vision-Aware Self-Improvement Training

问题与旧基线：旧方案在输出短、验证便宜或局部信号足够时仍合理。约束变化与机制：VISTA 把 partial-correct prefix reuse 与 intermediate-layer visual-attention sensor 组合为多模态 self-improvement 的数据采集与筛选控制回路。

Method / ownership：§3.2 Prefix Resampling; §3.3 Vision-Aware Attention Score。canonical owner=TRAIN-SFT；sensor/prediction set 只提供 proposal，验证器或 held-out gate 保留 truth/commit authority。

Evaluation contract：§4 multiple 2B-8B MLLMs, five benchmarks, SFT/DPO/GRPO, 8xA800 80GB, max output 2048。V3=6（2+2+2）。

Counterevidence / limitations：§5 prefix reuse can reduce diversity; only 2B-8B tested。Trade-off/fallback：新机制增加边界估计、采样或验证成本；证据越界时回退旧基线、完整验证或人工 gate。

Evidence boundary：Only exact-v1 disclosed workload, model, evaluator and assumptions are supported; no undisclosed production or cross-domain guarantee.

<!-- claim:SF-2026-ARXIV-2605-11931:start -->Only exact-v1 disclosed workload, model, evaluator and assumptions are supported; no undisclosed production or cross-domain guarantee.<!-- claim:SF-2026-ARXIV-2605-11931:end -->

Books Decision=Integrate — Root Writeback Applied；author 未修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-11931:end -->

**Books 对读：** TRAIN-SFT → books/part-04-training-system/29-sft.md。Current chapter has adjacent generic coverage but not this mechanism, ownership, trade-off and evidence boundary. 判定：**Integrate — Root Writeback Applied**。

### [Uncertainty Quantification for LLM-based Code Generation](https://arxiv.org/html/2605.12201v1)

**准入：** RisCoSet 将单标签 prediction set 扩展到多有效输出的 partial-program structured set，并用 multiple hypothesis testing 与 selective execution 给出显式 risk contract。

<!-- review:SF-2026-ARXIV-2605-12201:start -->
#### Uncertainty Quantification for LLM-based Code Generation

问题与旧基线：旧方案在输出短、验证便宜或局部信号足够时仍合理。约束变化与机制：RisCoSet 将单标签 prediction set 扩展到多有效输出的 partial-program structured set，并用 multiple hypothesis testing 与 selective execution 给出显式 risk contract。

Method / ownership：§3 Risk-Controlling Prediction Sets; §4 selective execution。canonical owner=PLATFORM-EVALUATION-SYSTEM；sensor/prediction set 只提供 proposal，验证器或 held-out gate 保留 truth/commit authority。

Evaluation contract：§5 HumanEval/MBPP/APPS, three 32B-70B models, 100 splits, sampling and H800/CUDA disclosed。V3=8（3+2+3）。

Counterevidence / limitations：Calibration executes tests; selective execution trades bounded label error for fewer executions。Trade-off/fallback：新机制增加边界估计、采样或验证成本；证据越界时回退旧基线、完整验证或人工 gate。

Evidence boundary：Only exact-v1 disclosed workload, model, evaluator and assumptions are supported; no undisclosed production or cross-domain guarantee.

<!-- claim:SF-2026-ARXIV-2605-12201:start -->Only exact-v1 disclosed workload, model, evaluator and assumptions are supported; no undisclosed production or cross-domain guarantee.<!-- claim:SF-2026-ARXIV-2605-12201:end -->

Books Decision=Integrate — Root Writeback Applied；author 未修改共享 Books。
<!-- review:SF-2026-ARXIV-2605-12201:end -->

**Books 对读：** PLATFORM-EVALUATION-SYSTEM → books/part-06-ai-infrastructure/66-evaluation-system.md。Current chapter has adjacent generic coverage but not this mechanism, ownership, trade-off and evidence boundary. 判定：**Integrate — Root Writeback Applied**。

### [EVOCHAMBER: Test-Time Co-evolution of Multi-Agent System at Individual, Team, and Population Scales](https://arxiv.org/html/2605.11136v1)

**准入：** Multi-Agent 的 test-time learning 不能简化为 N 个单 Agent memory 更新：individual context、team composition/collaboration structure 与 population knowledge flow 是三个不同状态 owner。

<!-- review:SF-2026-ARXIV-2605-11136:start -->
#### EVOCHAMBER: Test-Time Co-evolution of Multi-Agent System at Individual, Team, and Population Scales

问题、旧基线与准入：Multi-Agent 的 test-time learning 不能简化为 N 个单 Agent memory 更新：individual context、team composition/collaboration structure 与 population knowledge flow 是三个不同状态 owner。 旧基线在新增状态、规模或风险约束不存在时仍合理。
Method / state ownership：§3.1–§3.5：CODREAM 在 team failure/disagreement 后做非对称经验路由；team operators 在线选择成员与协作结构；population lifecycle 执行 fork、merge、prune 与 seed。 canonical owner=`AGENT-MULTI-AGENT`；proposal/sensor 不自动取得 truth 或 commit authority。
Evaluation contract：§4.1–§4.4：competition math、code 与 multi-domain reasoning 三条任务流；Qwen3-8B 在单 H100，另用 GPT-4.1-mini；报告 accuracy/pass@1/F1 与分层 ablation。 V3=3+2+3=8。
Counterevidence / limitations：Appendix A：只覆盖两个 model family；推理成本约为 single-agent 的 3.6 倍；lifecycle threshold 固定；更长流、credit attribution 和开放 population 未验证。
Artifact：https://github.com/Mercury7353/EvoChamber；未确认与 exact-v1 绑定的 immutable commit。
Trade-off / failure：更强跨 agent 学习换来额外推理、credit attribution、population churn、错误 transfer 与 specialization collapse。
Fallback / coexistence：短任务、固定团队或 lifecycle evidence 不足时，保留静态 team、局部 memory 和人工/确定性成员管理。

<!-- claim:SF-2026-ARXIV-2605-11136:start -->exact-v1 只支持上述披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。<!-- claim:SF-2026-ARXIV-2605-11136:end -->

Books Decision=`Integrate — Root Writeback Applied`；root 已写入共享 Books，等待独立写后复核。
<!-- review:SF-2026-ARXIV-2605-11136:end -->

**Books 对读：** `AGENT-MULTI-AGENT` → `books/part-07-agent/82-multi-agent.md` 的“Participation Graph 与 Step Orchestration 是联合状态”。Ch82 已把 participation graph、message identity 与 orchestration state 分开，但未承载 individual/team/population 三层联合演化、非对称知识转移和 population lifecycle 的状态边界。 新证据增量：把 multi-agent test-time adaptation 从各 agent 的私有 memory 扩展为三层 versioned state；specialization 依赖非对称 transfer，而 fork/merge/prune/seed 必须由 population controller 提交。 判定：**Integrate — Root Writeback Applied；待独立写后复核**。

### [The Bicameral Model: Bidirectional Hidden-State Coupling Between Parallel Language Models](https://arxiv.org/html/2605.11167v1)

**准入：** 两个 frozen LM 可在每个 generation step 通过 trainable hidden-state interface 双向通信；这改变的不是消息格式，而是并发 agent 的同步、causal schedule 与 tool-state ownership。

<!-- review:SF-2026-ARXIV-2605-11167:start -->
#### The Bicameral Model: Bidirectional Hidden-State Coupling Between Parallel Language Models

问题、旧基线与准入：两个 frozen LM 可在每个 generation step 通过 trainable hidden-state interface 双向通信；这改变的不是消息格式，而是并发 agent 的同步、causal schedule 与 tool-state ownership。 旧基线在新增状态、规模或风险约束不存在时仍合理。
Method / state ownership：§2.1–§2.4：两个 LM lockstep generation；neural interface 双向变换 hidden state，以 learned suppression gate 注入 residual，并对 tool output 维持因果放置。§3 只训练 interface。 canonical owner=`AGENT-MULTI-AGENT`；proposal/sensor 不自动取得 truth 或 commit authority。
Evaluation contract：§4：calculator 与 Z3 两个 tool-use domain，比较独立模型、文本交流和 learned interface；§5 分析 gate 与 communication pattern。 V3=3+2+2=7。
Counterevidence / limitations：§5.4：双模型推理成本可能近似翻倍；GSM8K 在狭小 capability gap 下由 49.6 降至约 40；训练需要 task-specific causal placement annotation。
Artifact：Not Disclosed：未找到与 exact-v1 绑定的公开 repository 或 immutable commit。
Trade-off / failure：降低文本通信开销但增加双模型 compute、同步阻塞、hidden-state coupling、不可解释通信和负迁移。
Fallback / coexistence：能力互补或因果标注不足时，回退显式 typed message/handoff、异步协作或单模型 tool loop。

<!-- claim:SF-2026-ARXIV-2605-11167:start -->exact-v1 只支持上述披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。<!-- claim:SF-2026-ARXIV-2605-11167:end -->

Books Decision=`Integrate — Root Writeback Applied`；root 已写入共享 Books，等待独立写后复核。
<!-- review:SF-2026-ARXIV-2605-11167:end -->

**Books 对读：** `AGENT-MULTI-AGENT` → `books/part-07-agent/82-multi-agent.md` 的“Latent Communication 只能压缩 Payload，不能隐藏 Identity”。Ch82 已要求 latent handoff 保留 identity、version 和 commitment boundary，但未覆盖两个模型逐 token lockstep、双向 hidden-state coupling、suppression gate 与 tool causality 的联合 contract。 新证据增量：latent channel 成为同步通信 plane：interface 只拥有 payload transform/gate，两个 frozen LM 各自拥有生成 state，tool runtime 仍拥有 effect commit；causal schedule 必须显式版本化。 判定：**Integrate — Root Writeback Applied；待独立写后复核**。

### [OLIVIA: Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents](https://arxiv.org/html/2605.11169v1)

**准入：** 在 frozen ReAct reasoner 与 tool execution 之间加入 deployment-time contextual bandit，使 action selection 能由 action-level feedback 在线更新，而不重训 reasoning model。

<!-- review:SF-2026-ARXIV-2605-11169:start -->
#### OLIVIA: Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents

问题、旧基线与准入：在 frozen ReAct reasoner 与 tool execution 之间加入 deployment-time contextual bandit，使 action selection 能由 action-level feedback 在线更新，而不重训 reasoning model。 旧基线在新增状态、规模或风险约束不存在时仍合理。
Method / state ownership：§4–§5：reasoner hidden state 作为 context；每个 action 保存线性 bandit sufficient statistics；UCB 同时估计 expected reward 与 uncertainty，以 rank-one update 吸收在线反馈。 canonical owner=`AGENT-TOOL-CALLING`；proposal/sensor 不自动取得 truth 或 commit authority。
Evaluation contract：§6：ToolBench、TaskBench、TaskBench-MM 与 BFCL；Qwen3-4B 和 Mistral-7B fixed；以 reference completion 转换的 tool-multiset F1 比较 fixed selection 与 OLIVIA。 V3=3+2+3=8。
Counterevidence / limitations：无独立 Limitations。tool-multiset F1 不证明 effect success、permission safety 或生产 tail；开放 action space、non-stationary/adversarial feedback 和 unsafe exploration 未覆盖。
Artifact：Not Disclosed：未确认公开代码或与 exact-v1 绑定的 immutable artifact。
Trade-off / failure：适应环境变化但引入冷启动、unsafe exploration、reward poisoning、per-action state 膨胀和 non-stationary regret。
Fallback / coexistence：高风险 action、反馈不可归因或 action space 快速变化时，回退 frozen policy、allowlist、offline evaluation 和显式审批。

<!-- claim:SF-2026-ARXIV-2605-11169:start -->exact-v1 只支持上述披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。<!-- claim:SF-2026-ARXIV-2605-11169:end -->

Books Decision=`Integrate — Root Writeback Applied`；root 已写入共享 Books，等待独立写后复核。
<!-- review:SF-2026-ARXIV-2605-11169:end -->

**Books 对读：** `AGENT-TOOL-CALLING` → `books/part-07-agent/78-tool-calling.md` 的“执行后行为只能更新下一次 Intent Gate”。Ch78 已规定执行结果只能更新下一次 intent proposal，authorizer/effect runtime 保留 commit authority；但未承载 frozen reasoner 之后的 per-action online statistics、UCB exploration 和 deployment-time decision-layer state。 新证据增量：把 tool proposal policy 拆成可在线学习的 bandit state；feedback 更新 selector 而非 retrospective authorization，UCB uncertainty 只决定探索优先级，不能越过 permission/effect gate。 判定：**Integrate — Root Writeback Applied；待独立写后复核**。

### [PIVOT: Bridging Planning and Execution in LLM Agents via Trajectory Refinement](https://arxiv.org/html/2605.11225v1)

**准入：** 把完整 trajectory 视为可版本化、可验证的优化状态：执行产生 discrepancy，再用 structured textual gradient 定位并替换 suffix，只有验证后不退化才提交。

<!-- review:SF-2026-ARXIV-2605-11225:start -->
#### PIVOT: Bridging Planning and Execution in LLM Agents via Trajectory Refinement

问题、旧基线与准入：把完整 trajectory 视为可版本化、可验证的优化状态：执行产生 discrepancy，再用 structured textual gradient 定位并替换 suffix，只有验证后不退化才提交。 旧基线在新增状态、规模或风险约束不存在时仍合理。
Method / state ownership：§3：PLAN→INSPECT→EVOLVE→VERIFY；inspection 从 execution trace 生成 backward discrepancy/textual gradient，evolution 做 localized trajectory repair，acceptance 保持 incumbent 的 monotonicity。 canonical owner=`AGENT-PLANNING`；proposal/sensor 不自动取得 truth 或 commit authority。
Evaluation contract：§4：DeepPlanning 与 GAIA；每个 domain 120 tasks；报告 composite/case metrics、token proxy、迭代收益和 component ablation。 V3=3+2+2=7。
Counterevidence / limitations：工具能力限制上界；GAIA basic toolkit 会使部分 refinement 退化为 retry；未直接测量 latency，token 只是 proxy；human-in-the-loop 上界不是 autonomous result。
Artifact：Not Disclosed：未确认与 exact-v1 绑定的公开代码或 immutable commit。
Trade-off / failure：可定位失败并保留已验证 prefix，但增加执行、inspection、版本比较与 verifier 成本；错误 textual gradient 会稳定优化错误方向。
Fallback / coexistence：工具弱、验证不可靠或迭代预算耗尽时，回退从 checkpoint 全局 replan、保守 retry 或人工接管。

<!-- claim:SF-2026-ARXIV-2605-11225:start -->exact-v1 只支持上述披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。<!-- claim:SF-2026-ARXIV-2605-11225:end -->

Books Decision=`Integrate — Root Writeback Applied`；root 已写入共享 Books，等待独立写后复核。
<!-- review:SF-2026-ARXIV-2605-11225:end -->

**Books 对读：** `AGENT-PLANNING` → `books/part-07-agent/79-planning.md` 的“Replanning 的触发条件”。Ch79 已有 observation-triggered replan、局部 replan 后的全约束复核和 completion evidence，但未把 accepted trajectory 作为 incumbent state，也未定义 backward discrepancy、suffix replacement 与 monotonic acceptance。 新证据增量：replanning 从重新生成变成带版本与接受准则的 trajectory optimization：executor 提供观测，inspector 提出 discrepancy，evolver 只修改局部 suffix，verifier 独占 commit。 判定：**Integrate — Root Writeback Applied；待独立写后复核**。

### [BadSKP: Backdoor Attacks on Knowledge Graph-Enhanced LLMs with Soft Prompts](https://arxiv.org/html/2605.11996v1)

**准入：** KG-derived soft prompt 是独立于可见文本的 graph-conditioned channel；攻击上游 KG representation 可在不改用户文本时改变模型行为，因此 graph→projector→prompt 必须成为供应链信任边界。

<!-- review:SF-2026-ARXIV-2605-11996:start -->
#### BadSKP: Backdoor Attacks on Knowledge Graph-Enhanced LLMs with Soft Prompts

问题、旧基线与准入：KG-derived soft prompt 是独立于可见文本的 graph-conditioned channel；攻击上游 KG representation 可在不改用户文本时改变模型行为，因此 graph→projector→prompt 必须成为供应链信任边界。 旧基线在新增状态、规模或风险约束不存在时仍合理。
Method / state ownership：§III–§V：定义可修改上游 KG 的 attacker；用 semantic anchoring 维持表面任务相似，再分阶段优化 graph-level representation 与 soft-prompt effect。 canonical owner=`PLATFORM-SECURITY`；proposal/sensor 不自动取得 truth 或 commit authority。
Evaluation contract：§VI：两类 KG-enhanced soft-prompt system、四个 dataset 与多种 backbone/attack/defense setting；报告 attack success、clean utility 与 defense response。 V3=3+3+3=9。
Counterevidence / limitations：无独立 Limitations。结论依赖攻击者可接触上游 KG、两个系统族及所测 dataset/backbone；不证明生产 prevalence 或 semantic-anchor detector 能普遍防御。
Artifact：Not Disclosed：未确认与 exact-v1 绑定的公开 repository/commit。
Trade-off / failure：图知识提升条件化能力却引入不可见 payload、projector drift、poisoned relation propagation 和检测器被规避。
Fallback / coexistence：provenance 缺失、graph drift 或 detector 不确定时，禁用 soft channel，回退 signed snapshot、文本化可审计 evidence 或隔离模型版本。

<!-- claim:SF-2026-ARXIV-2605-11996:start -->exact-v1 只支持上述披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。<!-- claim:SF-2026-ARXIV-2605-11996:end -->

Books Decision=`Integrate — Root Writeback Applied`；root 已写入共享 Books，等待独立写后复核。
<!-- review:SF-2026-ARXIV-2605-11996:end -->

**Books 对读：** `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md` 的“Embedding 也是可执行数据供应链的一部分”。Ch72 已将 embedding、prompt 和 model artifact 纳入供应链，并要求 provenance/identity，但未明确 KG-derived continuous soft prompt 作为旁路 conditioning channel，也未覆盖 graph-space semantic anchoring attack。 新证据增量：安全 identity 必须绑定 KG snapshot、graph encoder/projector 与 model revision；soft prompt 只是 untrusted conditioning payload，semantic anchor 只能作 sensor，policy/effect gate 保留 authority。 判定：**Integrate — Root Writeback Applied；待独立写后复核**。

### [MEME: Multi-entity &amp; Evolving Memory Evaluation](https://arxiv.org/html/2605.12477v1)

**准入：** 长期 memory 不能只测静态 recall；多实体状态随时间变化时，Deletion、Cascade 与 Absence 分别测试过期事实、依赖传播和无证据拒答。

<!-- review:SF-2026-ARXIV-2605-12477:start -->
#### MEME: Multi-entity &amp; Evolving Memory Evaluation

问题、旧基线与准入：长期 memory 不能只测静态 recall；多实体状态随时间变化时，Deletion、Cascade 与 Absence 分别测试过期事实、依赖传播和无证据拒答。 旧基线在新增状态、规模或风险约束不存在时仍合理。
Method / state ownership：§3.1 定义 Deletion、Cascade、Absence 三类任务；§3.2 用有时间顺序的多实体 KG 生成 episode/dialog，并保留依赖关系与 expected state。 canonical owner=`PLATFORM-EVALUATION-SYSTEM`；proposal/sensor 不自动取得 truth 或 commit authority。
Evaluation contract：§4：六个 memory system、三类 paradigm、100 episodes 与约 35k tokens；分别报告 retrieval/final-answer 及 intervention sweep，以区分 stage failure。 V3=3+3+3=9。
Counterevidence / limitations：§6：只有两个 handcrafted KG、LLM-generated dialogue、100 episodes、约 35K tokens；多项 ablation 只用小子集且仅英语。
Artifact：https://seokwonjung-jay.github.io/meme-eval/；项目页提供 code/data，但未确认与 exact-v1 绑定的 immutable commit。
Trade-off / failure：更能暴露关系错误，却增加 KG/episode 构造、时间真值、干预实验与 evaluator 成本；合成对话可能把生成器偏差写入基准。
Fallback / coexistence：领域关系或时间真值不可验证时，保留静态 recall 基线但降级声明，并用人工审计/append-only provenance 验收关键变化。

<!-- claim:SF-2026-ARXIV-2605-12477:start -->exact-v1 只支持上述披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨模型、跨部署或生产 tail 的一般优势。<!-- claim:SF-2026-ARXIV-2605-12477:end -->

Books Decision=`Integrate — Root Writeback Applied`；root 已写入共享 Books，等待独立写后复核。
<!-- review:SF-2026-ARXIV-2605-12477:end -->

**Books 对读：** `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md` 的“动态知识系统需要关系型回归，而不只是静态答案分数”。Ch66 已指出删除不是沉默、动态关系需回归，并区分 evidence 与 answer；但未形成 multi-entity evolving memory 的 Deletion/Cascade/Absence 三轴合同及 stage-diagnostic intervention。 新证据增量：评估对象从单条 memory hit 扩展为 versioned entity-relation state；retriever、memory updater 和 answerer 分阶段验收，Cascade/Absence 让依赖传播与无证据拒答成为独立 release gate。 判定：**Integrate — Root Writeback Applied；待独立写后复核**。

### [$ξ$-DPO: Direct Preference Optimization via Ratio Reward Margin](https://arxiv.org/html/2605.10981v1)

**准入与评分：** SimPO 的 `beta` 既缩放 preference logit，又通过 sigmoid saturation 隐式过滤 high-gap samples；`gamma` 的实际意义随数据集 reward-gap 结构改变。论文把目标改写为到有界 ratio reward margin `xi` 的距离，因此需要重新判断 reference-free preference optimization 的调参语义。V3=`2+1+2=5`；由于结论拟进入 Books，围绕采用命题完成深入审阅。

**机制与证据：** §3.1–§3.2 分析 `beta/gamma`，§4.1–§4.2 给出 logit transform、ratio gap、LeakyReLU 与基于初始 gap quantile 的 `xi` 选择；§5.1–§5.3 覆盖四个 preference datasets 及作者所测 Mistral-7B-Instruct、Llama3-8B-Instruct、Gemma2-9B-Instruct。Appendix A 明示训练后期 target-policy log probability 下降的原因未知，dynamic `xi` 尚未解决。代码入口存在，但 exact-v1 未绑定 immutable commit，也未复现。未披露 hardware、precision、batch、concurrency 与 production SLO。

**Books 对读：** `TRAIN-DPO` 的现有正文已经拆分 preference scale 与 optimization scale。最终单项复核确认正文正确承载 `beta` 的 sample-filtering、`gamma` 的 dataset-gap dependence、ratio reward 对 `beta` 的取消，以及单一 bounded `xi` 对耦合 margin 调节的取代；initial quantile state、LeakyReLU、trade-off、failure 与 DPO/SimPO fallback 也均保留。证据边界已完整列出 exact-v1 §5.1 的三种模型。判定：**Integrate — Root Writeback Applied；独立写后复核通过**。

### [Uniform Scaling Limits in AdamW-Trained Transformers](https://arxiv.org/html/2605.11059v1)

**准入与评分：** exact-v1 在特定 attention-only、初始化与 AdamW 假设下证明 hidden state 与 backpropagated variables 共同趋于 forward-backward ODE，rate 为 `O(L^-1 + L^-1/3 H^-1/2)`；V3=`1+2+2=5`，标准审阅。

**证据边界：** §3.1–§3.4、Lemma 6 与 Theorem 7 给出定理；这是理论工作，没有经验 benchmark。§4 明确 causal mask、完整 Transformer、global training time 与更强 uniform rate 均未解决，故不能外推现实 decoder 或 schedule transfer。

**Books 对读：** `TRAIN-PRETRAINING` 已明确深度/宽度参数化须同时稳定 forward 与 update scale，且数学 scaling limit 不能独自签发现实训练配置；weight decay 的全局结构作用也已有正文。新证据加强但不改变该命题。判定：**No Change — Existing Coverage；独立复核通过**。

### [Muon is Not That Special: Random or Inverted Spectra Work Just as Well](https://arxiv.org/html/2605.11181v1)

**纠错准入与评分：** 该工作直接挑战 Muon 依靠精确 LMO 或理想全局几何获得收益的叙述，按合同强制深入审阅。V3=`3+2+3=8`。

**机制与证据：** §2.1–§2.3 的 Freon 覆盖 Schatten quasi-norm，Kaon 将 singular values 替换为随机噪声仍在所测 GPT-2 setup 匹配 Muon；§3.1–§3.3 将局部进展分解为 batch-gradient alignment、directional descent potential 与 step-size tuning。经验只覆盖 NanoGPT/GPT-2，严格分析限 random-feature model；其他模型、modality 与 nonquadratic loss 未证明，论文也未提供与 exact-v1 绑定的 immutable artifact。

**Books 对读：** `TRAIN-PRETRAINING` 已写 matrix-aware update 与 spectrum/noise regime，但仍可能让读者把收益归因于“保留二维几何”。新正文已修正为：精确 spectrum shape 不是所测收益的必要条件，谱压制、局部对齐、下降潜力和合适步长需分开验证；这不构成部署 Kaon 或淘汰 AdamW/Muon 的证据。判定：**Integrate — Root Writeback Applied；独立写后复核通过**。

### [Internalizing Curriculum Judgment for LLM Reinforcement Fine-Tuning](https://arxiv.org/html/2605.11235v1)

**准入与评分：** METIS 把 curriculum judgment 从外部 heuristic/model 内化到当前 policy：根据 recent prompt–variance examples 预测 informativeness、选择 Top-B，并把 self-judgment reward 与 task reward 联合优化。V3=`3+2+3=8`，深入审阅。

**证据与边界：** §5.1–§5.3 只支持作者 math、code 与 function-calling workloads；“最高 67% wall-clock reduction”和约 3.9% per-step overhead 不外推。§5.3 / Appendix B.4 显示去掉 ICL evidence 后 parse failure 从 0.3% 升至 87.6%，说明 self-judgment 并非内生真值。exact-v1 仅承诺将来发布 code/datasets。

**Books 对读：** `TRAIN-GRPO` 已把 reward variance 定位为 curriculum proposal sensor，并要求 verifier 保留 outcome authority与 random coverage fallback；本次补入同一 policy 通过 ICL evidence 学习该 sensor 的条件分支。判定：**Integrate — Root Writeback Applied；独立写后复核通过**；sensor drift 时回退 static/external curriculum。

### [ReAD: Reinforcement-Guided Capability Distillation for Large Language Models](https://arxiv.org/html/2605.11290v1)

**准入与评分：** fixed token budget 下 capability 之间会 transfer、spillover 和 saturation；ReAD 用 task requirement、student probe、remaining budget 与 recent allocation 构造 state，再由 uncertainty-aware contextual bandit 分配 targeted teacher supervision。V3=`3+2+3=8`，深入审阅。

**证据与边界：** §5–§6 覆盖作者 Llama 与 Qwen teacher/student、20M/150M token budgets、八类 capability、held-out evaluation 与三 seeds。Appendix H 明确 task-requirement model、probe calibration、capability taxonomy、safety/privacy inheritance 与 off-target changes 的限制。代码仓库未绑定 immutable exact-v1 commit，未复现。

**Books 对读：** `TRAIN-SFT` 已讨论 distillation 的 teacher boundary、student occupancy 与动态难度，本次补入 capability-level budget state 和 cross-capability spillover。判定：**Integrate — Root Writeback Applied；独立写后复核通过**；状态估计不稳时保留 static mixture、均匀探索或 staged distillation。

### [Couple to Control: Joint Initial Noise Design in Diffusion Models](https://arxiv.org/html/2605.11311v1)

**准入与评分：** 独立 Gaussian seed 只规定每个样本的 marginal，不规定一次 gallery 的 joint distribution。论文保持每个 noise marginal 为 `N(0,I)`，用 repulsive coupling 改变跨样本 dependence。V3=`3+2+3=8`，深入审阅。

**证据与边界：** §5 使用 2,000 个 COCO prompts、SD1.5/SDXL/SD3、每 prompt 三图及 L2/MSS/Vendi、CLIP、PickScore，并测试 fixed-object background generation。证据只覆盖作者 gallery size、models、metrics 与 Gaussian/subspace coupling；foreground fidelity、其他 sampler、hardware、precision、concurrency 与 production SLO 未闭合，也没有可核验的 immutable artifact。

**Books 对读：** `MULTIMODAL-GENERATIVE-PARADIGMS` 已把 source/coupling/schedule 作为 generation artifact，本次补入“固定 marginal、改变 batch joint contract”的 gallery 分支。判定：**Integrate — Root Writeback Applied；独立写后复核通过**；单图、复现与 failure isolation 优先时继续使用 independent seeds。

## 5. 缺口与下一步

外部终态保留项：`SRC-OPENAI`、`SRC-QWEN`、`SRC-MOONSHOT` 与 `SRC-XIAOMI-MIMO` 的历史入口缺少稳定日级发现页或分页停止点；这些隔离项不用于正面证据、Books 或无遗漏断言。定点重开条件：对应机构提供可复查的官方历史归档、事件时刻或覆盖本窗的稳定索引时，只重开该来源在本窗的覆盖判断，不重跑已冻结的 arXiv 分母与其他来源。

- 分母已冻结为 163 retained + 484 closure + 191 isolation = 838；不存在未审查的 retained candidate。
- 163 项均完成相应深度 Evidence Review、Stable Node owner 与逐命题 Books comparison。
- Round 7 新增 6 项 root 写回已由新的 fresh non-author reviewer 逐项通过：binding 唯一、位于 `## Review notes` 前，并完整承载 mechanism、state/control owner、证据边界、trade-off、failure 与 fallback；不得重复追加。
- Round 8 已完成这 6 项的定点重开：`2605.11059` 的 `No Change — Existing Coverage` 对读通过；5 项写回的 binding 均唯一且位于 `## Review notes` 前，`2605.11181`、`2605.11235`、`2605.11290`、`2605.11311` 通过独立写后复核。
- `2605.10981` 的方法与 evidence-boundary 定点修复均已由未参与写入的 fresh non-author reviewer 核验通过；对应 repair queue 已关闭，没有剩余 Gate。

## 6. 复核

结论：通过

六项 false negative 的题摘贡献复判、exact-v1 Evidence Review、V3 score、Stable owner 与逐命题 Books comparison 已完成。`2605.11059` 的 No Change 与五项 Books 写回全部通过独立复核；`2605.10981` 的核心方法和模型证据范围均与 exact-v1 一致。冻结分母、88 项 root writeback 和所有独立 Gate 已闭合，没有剩余可执行工作。Round 7 已通过的 83 项未重复写入。

作者返修者：`bounded-author:may13-round8-six-20260915`
复核者：`fresh-nonauthor:may13-round8-postwrite-20260915`；最终单项复核：`fresh-nonauthor:may13-round8-10981-final-20260915`
### 活跃证据文件

- v3-active-ledger.json
- v3-active-evidence.json
- v3-books-comparison.json
- v3-root-writeback-queue.json
- v3-author-semantic-audit.json
- v3-round5-root-books-synthesis-repair-queue.json
- V3_ROUND5_ROOT_BOOKS_SYNTHESIS_REPAIR_QUEUE_20260915.md
- V3_ROUND5_AUTHOR_BOUNDED_REPAIR_20260915.md
- V3_FRESH_NONAUTHOR_FINAL_REVIEW_20260915.md
- V3_BOUNDED_SIX_AUTHOR_REPAIR_20260915.md
- V3_ROUND7_BOUNDED_AUTHOR_REPAIR_20260915.md
- V3_ROUND7_ROOT_BOOKS_SYNTHESIS_QUEUE_20260915.md
- V3_ROUND7_FRESH_NONAUTHOR_POSTWRITE_REVIEW_20260915.md
- V3_ROUND8_BOUNDED_AUTHOR_REPAIR_20260915.md
- V3_ROUND8_ROOT_BOOKS_SYNTHESIS_QUEUE_20260915.md
- V3_ROUND8_FRESH_NONAUTHOR_POSTWRITE_REVIEW_20260915.md
- V3_ROUND8_ROOT_SEMANTIC_REPAIR_QUEUE_20260915.md
- ROOT_ROUND8_BOOKS_REPAIR_2605_10981_20260915.md
- V3_ROUND8_FRESH_NONAUTHOR_REVIEW_AFTER_10981_REPAIR_20260915.md
- V3_ROUND8_ROOT_EVIDENCE_BOUNDARY_REPAIR_QUEUE_20260915.md
- V3_ROUND8_FRESH_NONAUTHOR_FINAL_REVIEW_AFTER_10981_EVIDENCE_REPAIR_20260915.md
- v3-independent-semantic-audit.json

**Review Provenance ID:** daily-20260513-v3-round8-10981-final-complete-20260915
