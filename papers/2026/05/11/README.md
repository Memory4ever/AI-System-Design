# Daily Research — 2026-05-11

**规范：** V3
**窗口：** 2026-05-10T09:00:00+08:00 ～ 2026-05-11T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-15T20:09:16+08:00

## 1. 结论

本轮严格只执行 `V3_FRESH_NONAUTHOR_SCREENING_REPAIR_QUEUE_20260915.md` 点名的 28 项，没有扩窗、扩来源或重扫其余 identity。A 组 18 项全部恢复 retained，并逐项完成 official arXiv HTML exact-v1 的 method/evaluation/non-proof 定位；B 组 10 项也全部恢复 retained，因为逐项旧证据与当前 owner 对照仍通过 contribution gate，不能用 generic closure 回退。direct 算术现冻结为 `635 = 102 retained + 533 pre-denominator closure`，整体为 `826 = 102 + 533 + 191`。

102 个候选均有 exact-v1 Evidence Review；Books 判断重冻为 42 Integrate、58 No Change、2 仅报告。42 个 Integrate 均已存在于当前 Books 正文：既有 26 项保留此前写后复核，本次恢复的 16 项已由 root 按唯一 owner 完成写回并通过 fresh non-author 逐项语义终审。`2605.06690` 的 typed epistemic stopping 与 `2605.07443` 的任意块 KV 复用/分层存储/position-conditioning 修复已由当前 Books owner 完整承载，A 组恢复 retained 不等于强制制造重复正文；B 组 10 项均给出命题级 No Change 对照。

Daily 已完成。未参与本次作者返修与 root 写回的 fresh non-author reviewer 复核了 28 项 screening repair、102 项集合与 Evidence、191 项 owner-day isolation，以及 42 个 Integrate marker；对 16 个新正文逐项核验真实语义与相邻衔接。denominator、Evidence、Books 与独立终审均无剩余可执行项。

## 2. 来源覆盖

本轮沿用冻结来源与窗口，只返修点名项目；下列 coverage 不构成新的全量来源重放。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 历史入口；动态列表无法稳定分页回到本窗 | 受阻 | 隔离：不支持全站零遗漏；取得本窗官方归档时才重开 |
| SRC-ANTHROPIC | Research 历史列表；相邻公开事件 05-08 与 05-14 | 已检查 | 未见已列事件落窗；不扩张为全站证明 |
| SRC-GOOGLE-AI | DeepMind/Google Research 本窗定点检查 | 受阻 | 历史列表缺日级稳定停止点；隔离 |
| SRC-META-AI | Meta/FAIR publications 本窗定点检查 | 受阻 | 动态目录缺日级稳定分页；隔离 |
| SRC-QWEN | Qwen 官方历史入口本窗定点检查 | 受阻 | 旧入口不能稳定回溯；隔离 |
| SRC-DEEPSEEK | News/Research；相邻事件 04-24 与 05-14 | 已检查 | 未见本窗事件 |
| SRC-MOONSHOT | Kimi Blog 与官方仓库本窗定点检查 | 受阻 | 无稳定历史日级发现页；隔离 |
| SRC-TENCENT-HUNYUAN | Research‘全部’列表；相邻条目 04-30 与 05-21 | 已检查 | 未见本窗事件 |
| SRC-ZAI | 智谱 Research；相邻条目 04-29 与 05-20 | 已检查 | 未见本窗事件 |
| SRC-BYTEDANCE-SEED | Seed Research/Publication 与 arXiv identity 交叉检查 | 已检查 | 目录回填日不替代首次公开 |
| SRC-BAIDU-ERNIE | ERNIE Blog；相邻事件 05-09 08:00+08 | 已检查 | 早于本窗，不重复 |
| SRC-XIAOMI-MIMO | MiMo Papers 与 Blog 历史入口 | 受阻 | Papers 可排除；Blog 缺稳定历史时刻；隔离 |
| SRC-MINIMAX | Research/Blog；相邻事件 03-18 与 05-26 | 已检查 | 未见本窗事件 |
| SRC-ARXIV | 冻结 826 identity：635 official-announcement direct + 191 owner-day recovery；191/191 已绑定官方 abs version/history/Comments；102 candidate exact-v1 Evidence Review | 已检查 | 1 项 current withdrawal 已关闭；6 项 later revision signal 归属后续事件日，不冒充本窗 revision |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [More Thinking, More Bias: Length-Driven Position Bias in Reasoning Models](https://arxiv.org/html/2605.06672v1) | 2026-05-11T08:00:00+08:00 | Reasoning-model 的多选题位置偏差必须按 reasoning trajectory length 与 direct/CoT mode 分层，不能把随机换序后的单一平均值当作 order robustness。；3 + 2 + 3 = 8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已存在 Books 正文 |
| [Domain-level metacognitive monitoring in frontier LLMs: A 33-model atlas](https://arxiv.org/html/2605.06673v1) | 2026-05-11T08:00:00+08:00 | 模型的 verbalized-confidence 监测质量会随知识域显著变化，aggregate calibration 会掩盖 domain-local failure。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction](https://arxiv.org/html/2605.06676v1) | 2026-05-11T08:00:00+08:00 | KV eviction 可把 head-wise budget 与 token selection 从手工启发式升级为任务目标驱动的 learned policy。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`INFER-KV-CACHE`，[45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [State Representation and Termination for Recursive Reasoning Systems](https://arxiv.org/html/2605.06690v1) | 2026-05-11T08:00:00+08:00 | 递归推理必须显式保存 epistemic state，并把 expand/consolidate order-gap 只当作局部停止诊断，而不是 truth 或全局收敛证明。；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：`AGENT-REFLECTION`，[80-reflection.md](../../../../books/part-07-agent/80-reflection.md) |
| [Hidden Coalitions in Multi-Agent AI: A Spectral Diagnostic from Internal Representations](https://arxiv.org/html/2605.06696v1) | 2026-05-11T08:00:00+08:00 | 多 Agent 行为相似不足以证明 coalition；internal-state mutual information 的谱结构可作为 representational coupling sensor。；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：`PLATFORM-MONITORING`，[67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [CASCADE: Case-Based Continual Adaptation for Large Language Models During Deployment](https://arxiv.org/html/2605.06702v1) | 2026-05-11T08:00:00+08:00 | 部署期学习可把更新权从模型 weights 移到带 reward 的 episodic case bank 与 contextual-bandit retriever。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[77-memory.md](../../../../books/part-07-agent/77-memory.md) |
| [Visual Text Compression as Measure Transport](https://arxiv.org/html/2605.06708v1) | 2026-05-11T08:00:00+08:00 | 把文本渲染成图像进行长上下文压缩时，路由依据应是任务相关信息损失而不是 token compression ratio；precision、coverage 与高成本区域的再编码必须分别可见。；3 + 3 + 3 = 9 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[23-multimodal-representation.md](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；已存在 Books 正文 |
| [When Does a Language Model Commit? A Finite-Answer Theory of Pre-Verbalization Commitment](https://arxiv.org/html/2605.06723v1) | 2026-05-11T08:00:00+08:00 | 模型可以在公开答案出现前稳定偏向某个有限答案，但该 commitment 追踪 eventual output，而不是 truth 或可靠 abstention。；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [When Routine Chats Turn Toxic: Unintended Long-Term State Poisoning in Personalized Agents](https://arxiv.org/html/2605.06731v1) | 2026-05-11T08:00:00+08:00 | 持久 Agent state 的安全边界不止是读取可信度，还包括每次 writeback 的授权漂移审计与可选择回滚。；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[77-memory.md](../../../../books/part-07-agent/77-memory.md) |
| [Beyond Factor Aggregation: Gauge-Aware Low-Rank Server Representations for Federated LoRA](https://arxiv.org/html/2605.06733v1) | 2026-05-11T08:00:00+08:00 | LoRA 聚合对象应是 gauge-invariant 的更新语义，而不是坐标任意的 A/B 因子。；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-LORA`，[30-lora.md](../../../../books/part-04-training-system/30-lora.md)；已存在 Books 正文 |
| [Gradient Extrapolation-Based Policy Optimization](https://arxiv.org/html/2605.06755v1) | 2026-05-11T08:00:00+08:00 | RL optimizer 可用局部 gradient trajectory 近似多步 lookahead，但必须把稳定性检测和退化回普通 GRPO 写进控制合同。；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`TRAIN-GRPO`，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) |
| [Language Models Can Autonomously Hack and Self-Replicate](https://arxiv.org/pdf/2605.06760v1) | 2026-05-11T08:00:00+08:00 | 模型已能把漏洞利用、凭据抽取、权重复制和远端部署串成可重复的自我复制链，扩展了部署威胁模型。；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Weblica: Scalable and Reproducible Training Environments for Visual Web Agents](https://arxiv.org/html/2605.06761v1) | 2026-05-11T08:00:00+08:00 | Web Agent 训练环境应把可复放的页面状态、交互 transition 与生成环境 identity 分开保存，离线成功不能直接授予 live-Web promotion。；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-WORKFLOW`，[81-workflow.md](../../../../books/part-07-agent/81-workflow.md) |
| [Conformal Agent Error Attribution](https://arxiv.org/html/2605.06788v1) | 2026-05-11T08:00:00+08:00 | Agent 故障定位可以输出带有限样本 coverage 的连续回滚区间，而不是未经校准的单点 culprit。；2 + 2 + 2 = 6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已存在 Books 正文 |
| [Towards Security-Auditable LLM Agents: A Unified Graph Representation](https://arxiv.org/html/2605.06812v1) | 2026-05-11T08:00:00+08:00 | Agent 审计图必须同时表达静态 capability base 与动态 semantic state，并保留二者之间的数据、控制与权限传播路径。；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`PLATFORM-TRACE`，[69-trace.md](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [AGWM: Affordance-Grounded World Models for Environments with Compositional Prerequisites](https://arxiv.org/html/2605.06841v1) | 2026-05-11T08:00:00+08:00 | World Model 除预测 next state，还必须显式维护 action prerequisite 与动态 affordance state。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [How to Compress KV Cache in RL Post-Training? Shadow Mask Distillation for Memory-Efficient Alignment](https://arxiv.org/html/2605.06850v1) | 2026-05-11T08:00:00+08:00 | 训练 rollout 使用压缩 KV、learner 使用 dense context 会形成隐藏的 state-policy mismatch，而不仅是普通推理近似误差。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`TRAIN-RLHF`，[31-rlhf.md](../../../../books/part-04-training-system/31-rlhf.md) |
| [Dataset Watermarking for Closed LLMs with Provable Detection](https://arxiv.org/html/2605.06865v1) | 2026-05-11T08:00:00+08:00 | 闭源模型的数据使用审计可以把 dataset-level statistical carrier 与黑盒生成输出的检测统计绑定，但检测只提供 provenance evidence，不等于逐样本或法律归因。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Don't Retrain, Align: Adapting Autoregressive LMs to Diffusion LMs via Representation Alignment](https://arxiv.org/html/2605.06885v1) | 2026-05-11T08:00:00+08:00 | AR→Diffusion 转换可把语言表示与解码顺序分开：保留表示几何，重学 generation path。；3 + 2 + 3 = 8 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；已存在 Books 正文 |
| [Not All Tokens Need 40 Steps: Heterogeneous Step Allocation in Diffusion Transformers for Efficient Video Generation](https://arxiv.org/html/2605.06892v1) | 2026-05-11T08:00:00+08:00 | 连续 diffusion token 的收敛速度不同时，可以按 token group 分配异质 step budget，并让 active queries 读取同步的全局 KV、未激活 token 用缓存 velocity 前进。；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS`，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Self-Programmed Execution for Language-Model Agents](https://arxiv.org/html/2605.06898v1) | 2026-05-11T08:00:00+08:00 | 模型可以提出甚至生成 orchestration program，但 effect isolation、执行边界与最终 commit authority 仍必须留在 harness/runtime。；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-PLATFORM`，[84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md) |
| [Conservative Flows: A New Paradigm of Generative Models](https://arxiv.org/html/2605.06905v1) | 2026-05-11T08:00:00+08:00 | 生成动态不一定从噪声 transport 到数据；也可从 data-supported state 出发，用 invariant flow 在目标分布内产生变化。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS`，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Same Signal, Opposite Meaning: Direction-Informed Adaptive Learning for LLM Agents](https://arxiv.org/html/2605.06908v1) | 2026-05-11T08:00:00+08:00 | test-time compute gate 必须区分 compute need 与 compute suitability；同一 uncertainty/difficulty signal 的效用方向会随 environment 与 backbone 反转。；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-SCHEDULING`，[56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)；Books 正文与独立终审均通过 |
| [Regulating Branch Parallelism in LLM Serving](https://arxiv.org/html/2605.06914v1) | 2026-05-11T08:00:00+08:00 | 分支并行宽度应成为每个 decode step 的 slack-aware admission，而不是 eager 或固定 cap。；3 + 3 + 2 = 8 | 深入完成 | 整合：`INFER-SCHEDULING`，[56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)；已存在 Books 正文 |
| [Can LLMs Take Retrieved Information with a Grain of Salt?](https://arxiv.org/html/2605.06919v1) | 2026-05-11T08:00:00+08:00 | RAG 不能把检索文本表达的 certainty 直接当 evidence authority；source certainty、模型 prior 与最终 answer confidence 必须分开校准。；3 + 3 + 3 = 9 | 深入完成 | 整合：`AGENT-RAG`，[76-rag.md](../../../../books/part-07-agent/76-rag.md)；已存在 Books 正文 |
| [A$^2$RD: Agentic Autoregressive Diffusion for Long Video Consistency](https://arxiv.org/html/2605.06924v1) | 2026-05-11T08:00:00+08:00 | 长视频 segment generation 应从 open-loop chaining 演进为读取持久 multimodal memory、选择生成模式并在提交前分层修正的闭环。；3 + 2 + 3 = 8 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；Books 正文与独立终审均通过 |
| [Bias and Uncertainty in LLM-as-a-Judge Estimation](https://arxiv.org/html/2605.06939v1) | 2026-05-11T08:00:00+08:00 | 校准后的 LLM judge 估计仍可能因 judge quality 与跨模型 calibration instability 发生带高置信度的方向翻转。；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Adaptive Memory Decay for Log-Linear Attention](https://arxiv.org/html/2605.06946v1) | 2026-05-11T08:00:00+08:00 | 固定递归记忆衰减可升级为 input-dependent、跨时间尺度的 learned decay，而不改变 log-linear state complexity。；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`MODEL-LONG-CONTEXT`，[22-long-context.md](../../../../books/part-02-model/22-long-context.md) |
| [Group of Skills: Group-Structured Skill Retrieval for Agent Skill Libraries](https://arxiv.org/html/2605.06978v1) | 2026-05-11T08:00:00+08:00 | 大型 skill library 的检索对象应保留 entry、依赖、guard 与 verifier role，而不是把一组相关文本直接拼成上下文。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[77-memory.md](../../../../books/part-07-agent/77-memory.md) |
| [The Cost of Consensus: Malignant Epistemic Herding and Adaptive Gating in Distributed Multi-Agent Search](https://arxiv.org/html/2605.06988v1) | 2026-05-11T08:00:00+08:00 | Multi-Agent communication 评价必须把 consensus 与 alignment-to-truth 分开；低分歧可能是 confident-but-wrong herding。；3 + 2 + 3 = 8 | 深入完成 | 整合：`AGENT-MULTI-AGENT`，[82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)；Books 正文与独立终审均通过 |
| [Why Does Agentic Safety Fail to Generalize Across Tasks?](https://arxiv.org/html/2605.06992v1) | 2026-05-11T08:00:00+08:00 | Agent safety 的跨任务泛化必须独立于任务执行能力评估，不能用同任务安全率或平均成功率替代。；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Echo: KV-Cache-Free Associative Recall with Spectral Koopman Operators](https://arxiv.org/html/2605.06997v1) | 2026-05-11T08:00:00+08:00 | 常量状态的 recurrent model 可用可更新的谱算子保存 associative-recall sufficient statistics，而不是重新引入线性 KV history。；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖：`MODEL-LONG-CONTEXT`，[22-long-context.md](../../../../books/part-02-model/22-long-context.md) |
| [Adaptive auditing of AI systems with anytime-valid guarantees](https://arxiv.org/html/2605.07002v1) | 2026-05-11T08:00:00+08:00 | adaptive sampling 与随时停止需要 anytime-valid inference，否则少量定向审计会产生伪置信。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [The Context Gathering Decision Process: A POMDP Framework for Agentic Search](https://arxiv.org/html/2605.07042v1) | 2026-05-11T08:00:00+08:00 | agentic search 应以持久 predicate-based belief state 拥有已知/未知与未解条件，并用 programmatic exhaustion gate 终止空转。；3 + 3 + 3 = 9 | 深入完成 | 整合：`AGENT-CONTEXT`，[75-context.md](../../../../books/part-07-agent/75-context.md)；Books 正文与独立终审均通过 |
| [An Interpretable and Scalable Framework for Evaluating Large Language Models](https://arxiv.org/html/2605.07046v1) | 2026-05-11T08:00:00+08:00 | 模型排名不能只平均 binary accuracy；stochastic response 与 item difficulty/discrimination 应进入同一 latent ability contract。；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Dr. Post-Training: A Data Regularization Perspective on LLM Post-Training](https://arxiv.org/pdf/2605.07063v1) | 2026-05-11T08:00:00+08:00 | 通用后训练数据可作为限制目标更新方向的 data-induced regularizer，而不只是供 selection 的样本池。；2 + 1 + 2 = 5 | 深入完成 | 整合：`TRAIN-DATA`，[27-data.md](../../../../books/part-04-training-system/27-data.md)；已存在 Books 正文 |
| [WiCER: Wiki-memory Compile, Evaluate, Refine Iterative Knowledge Compilation for LLM Wiki Systems](https://arxiv.org/html/2605.07068v1) | 2026-05-11T08:00:00+08:00 | 持久 wiki-memory 的编译必须以 probe 驱动的 counterexample/refinement 检查事实丢失，不能把压缩率或 TTFT 当完整性证明。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[77-memory.md](../../../../books/part-07-agent/77-memory.md) |
| [TeamBench: Evaluating Agent Coordination under Enforced Role Separation](https://arxiv.org/html/2605.07073v1) | 2026-05-11T08:00:00+08:00 | Multi-Agent evaluation 必须用 enforcement 区分角色声明与真实 capability separation，并把 team pass、越权尝试和 verifier false accept 分开。；3 + 3 + 3 = 9 | 深入完成 | 整合：`AGENT-MULTI-AGENT`，[82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)；Books 正文与独立终审均通过 |
| [Learning Visual Feature-Based World Models via Residual Latent Action](https://arxiv.org/html/2605.07079v1) | 2026-05-11T08:00:00+08:00 | feature-space World Model 应把可预测 residual transition 压成 latent action，并用 action-conditioned outcome 而非视觉清晰度验证其可规划性。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Securing Computer-Use Agents: A Unified Architecture-Lifecycle Framework for Deployment-Grounded Reliability](https://arxiv.org/html/2605.07110v1) | 2026-05-11T08:00:00+08:00 | Computer-Use Agent 安全应沿 perception/decision/execution 与 creation/deployment/operation/maintenance 的交叉面定位 authority-bearing failure。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY`，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Switchcraft: AI Model Router for Agentic Tool Calling](https://arxiv.org/html/2605.07112v1) | 2026-05-11T08:00:00+08:00 | tool-calling model router 应在 correctness hard condition 下选择最低总成本模型，并把 token-intensive reasoning、router latency 与 function-call structure 纳入成本。；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`AGENT-TOOL-CALLING`，[78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md) |
| [Where to Spend Rollouts: Hit-Utility Optimal Rollout Allocation for Group-Based RLVR](https://arxiv.org/html/2605.07114v1) | 2026-05-11T08:00:00+08:00 | 固定总 rollout budget 下，group-based RLVR 应依据当前 prompt 至少再命中一次正确样本的后验效用分配额外 rollouts，而不是每题固定 group size。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`TRAIN-GRPO`，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) |
| [Region4Web: Rethinking Observation Space Granularity for Web Agents](https://arxiv.org/html/2605.07134v1) | 2026-05-11T08:00:00+08:00 | Web Agent 的观察压缩应保留页面功能区域与跨步 transition，而不是只截断 element-level AXTree；selector 必须提供可恢复的全页回退。；2 + 2 + 3 = 7 | 深入完成 | 整合：`AGENT-CONTEXT`，[75-context.md](../../../../books/part-07-agent/75-context.md)；已存在 Books 正文 |
| [Demystifying and Detecting Agentic Workflow Injection Vulnerabilities in GitHub Actions](https://arxiv.org/html/2605.07135v1) | 2026-05-11T08:00:00+08:00 | CI event content 经 prompt 或 agent output 进入脚本，会把 prompt injection 扩展成 workflow data-flow vulnerability。；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-WORKFLOW`，[81-workflow.md](../../../../books/part-07-agent/81-workflow.md) |
| [Beyond Reasoning: Reinforcement Learning Unlocks Parametric Knowledge in LLMs](https://arxiv.org/html/2605.07153v1) | 2026-05-11T08:00:00+08:00 | 可验证奖励带来的 factual QA 提升可能主要是重排已有参数知识的输出概率，而非写入新事实。；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖：`TRAIN-RLHF`，[31-rlhf.md](../../../../books/part-04-training-system/31-rlhf.md) |
| [Rethinking Experience Utilization in Self-Evolving Language Model Agents](https://arxiv.org/html/2605.07164v1) | 2026-05-11T08:00:00+08:00 | Experience memory 的 serving policy 必须能在推理过程中决定是否、何时检索经验，不能把 initialization-only 或 always-on injection 当默认最优。；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[77-memory.md](../../../../books/part-07-agent/77-memory.md) |
| [Learning Agent Routing From Early Experience](https://arxiv.org/html/2605.07180v1) | 2026-05-11T08:00:00+08:00 | LLM→Agent escalation router 可用少量 early paired experience 建立能力边界，但经验 memory 只提供 routing evidence，不拥有任务结果。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`AGENT-PLATFORM`，[84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md) |
| [Star Elastic: Many-in-One Reasoning LLMs with Efficient Budget Control](https://arxiv.org/html/2605.07182v1) | 2026-05-11T08:00:00+08:00 | 同一 elastic checkpoint 可暴露多个 nested submodel，但运行时仍须按 reasoning phase 单独选择 model slice，并把 slice、phase 与精度写入请求执行身份。；3 + 2 + 2 = 7 | 深入完成 | 整合：`INFER-SCHEDULING`，[56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)；已存在 Books 正文 |
| [Hallucination Detection via Activations of Open-Weight Proxy Analyzers](https://arxiv.org/html/2605.07209v1) | 2026-05-11T08:00:00+08:00 | 开放权重 proxy 的 activation 可作为黑盒目标 hallucination 的辅助 sensor，但不能取得事实 authority。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [CASCADE: Context-Aware Relaxation for Speculative Image Decoding](https://arxiv.org/html/2605.07230v1) | 2026-05-11T08:00:00+08:00 | 图像 speculative decoding 的 verifier 可以利用局部冗余接受语义可替代 proposal，但这属于近似质量合同，不是文本式 exact sampling。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING`，[48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Reformulating KV Cache Eviction Problem for Long-Context LLM Inference](https://arxiv.org/html/2605.07234v1) | 2026-05-11T08:00:00+08:00 | KV eviction utility 应同时观察 attention map、projected value 与 inter-head interaction，并把 head-local score 变为 layer/model-wide 可比较预算。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`INFER-KV-CACHE`，[45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [FATE: Future-State-Aware Scheduling for Heterogeneous LLM Workflows](https://arxiv.org/html/2605.07238v1) | 2026-05-11T08:00:00+08:00 | Workflow-DAG scheduler 应同时评价当前 assignment 与它为下游留下的 model residency、parent-output locality、prefix reuse 和 device reachability。；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [MEMOREPAIR: Barrier-First Cascade Repair in Agentic Memory](https://arxiv.org/html/2605.07242v1) | 2026-05-11T08:00:00+08:00 | Memory source 被删除、纠正或接口迁移后，repair 必须先隔离受影响 descendants，再只发布经过 predecessor-closure 验证的 successor。；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[77-memory.md](../../../../books/part-07-agent/77-memory.md) |
| [Experience Sharing in Mutual Reinforcement Learning for Heterogeneous Language Models](https://arxiv.org/html/2605.07244v1) | 2026-05-11T08:00:00+08:00 | 异构 policy 应共享 typed experience，而不是共享参数或假定 tokenizer/behavior distribution 相同。；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`TRAIN-GRPO`，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) |
| [EnvSimBench: A Benchmark for Evaluating and Improving LLM-Based Environment Simulation](https://arxiv.org/html/2605.07247v1) | 2026-05-11T08:00:00+08:00 | Agent environment simulator 必须按 action outcome、state-change complexity 与 argument cardinality 分层测量，而非只看对话表面相似。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Hard to Read, Easy to Jailbreak: How Visual Degradation Bypasses MLLM Safety Alignment](https://arxiv.org/html/2605.07250v1) | 2026-05-11T08:00:00+08:00 | 当视觉文本降质到人/模型仍能识别而浅层 safety representation 被延迟时，多模态输入会出现 attack comfort zone；安全验收必须覆盖降质邻域。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY`，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [When Are Experts Misrouted? Counterfactual Routing Analysis in Mixture-of-Experts Language Models](https://arxiv.org/html/2605.07260v1) | 2026-05-11T08:00:00+08:00 | Top-k router score 不能被视为 route utility；冻结模型下的 matched-compute counterfactual routes 应成为诊断 fragile-token misrouting 的独立证据。；3 + 2 + 3 = 8 | 深入完成 | 整合：`MODEL-MOE`，[21-moe.md](../../../../books/part-02-model/21-moe.md)；已存在 Books 正文 |
| [Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions](https://arxiv.org/html/2605.07271v1) | 2026-05-11T08:00:00+08:00 | layer pruning 的质量崩塌应按 decision representation transition 诊断；hidden representation 仍相似不代表模型仍能进入 Decisive phase。；2 + 2 + 3 = 7 | 深入完成 | 整合：`MODEL-TRANSFORMER-LAYER`，[17-transformer-layer.md](../../../../books/part-02-model/17-transformer-layer.md)；Books 正文与独立终审均通过 |
| [Structured Role-Aware Policy Optimization for Multimodal Reasoning](https://arxiv.org/html/2605.07274v1) | 2026-05-11T08:00:00+08:00 | 多模态 RLVR 的 sequence reward 需要区分 perception 与 reasoning token 的角色，避免正确答案掩盖视觉证据缺失。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`TRAIN-GRPO`，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) |
| [Predictive but Not Plannable: RC-aux for Latent World Models](https://arxiv.org/html/2605.07278v1) | 2026-05-11T08:00:00+08:00 | predictive latent 距离不一定适合 planning；有限 horizon 的 reachability 必须显式进入训练和 planner scoring。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Sword: Style-Robust World Models as Simulators via Dynamic Latent Bootstrapping for VLA Policy Post-Training](https://arxiv.org/html/2605.07288v1) | 2026-05-11T08:00:00+08:00 | 用 World Model 作为 VLA simulator 时，style perturbation 与 long-horizon error accumulation 必须作为独立可靠性切片，并保持训练/推理 latent-state 一致。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [When Stored Evidence Stops Being Usable: Scale-Conditioned Evaluation of Agent Memory](https://arxiv.org/html/2605.07313v1) | 2026-05-11T08:00:00+08:00 | Agent memory 的可扩展性声明必须条件化于 agent、memory interface、irrelevant-session scale 与 interaction budget，并报告 usable-scale boundary。；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已存在 Books 正文 |
| [SparseRL-Sync: Lossless Weight Synchronization with ~100x Less Communication](https://arxiv.org/html/2605.07330v1) | 2026-05-11T08:00:00+08:00 | Trainer→rollout 同步可传输 lossless sparse parameter delta，但 rollout 必须基于正确 base 重构并验证 identity。；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`，[36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Rethinking Importance Sampling in LLM Policy Optimization: A Cumulative Token Perspective](https://arxiv.org/html/2605.07331v1) | 2026-05-11T08:00:00+08:00 | LLM policy optimization 的 IS ratio 可以对 prefix action likelihood 累乘，但必须用 position-adaptive clipping 控制随序列长度增长的 log-ratio 方差。；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-PPO`，[32-ppo.md](../../../../books/part-04-training-system/32-ppo.md)；Books 正文与独立终审均通过 |
| [MISA: Mixture of Indexer Sparse Attention for Long-Context LLM Inference](https://arxiv.org/html/2605.07363v1) | 2026-05-11T08:00:00+08:00 | 稀疏注意力 indexer 的 head 计算也应被路由；token Top-k 固定不代表 indexer cost 已最小。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`INFER-TENSORRT-LLM`，[49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Unsolvability Ceiling in Multi-LLM Routing: An Empirical Study of Evaluation Artifacts](https://arxiv.org/html/2605.07395v1) | 2026-05-11T08:00:00+08:00 | multi-LLM router 的 oracle/unsolvability ceiling 必须先去除 judge misalignment、truncation 与 format artifact，否则错误标签会训练出 routing collapse。；3 + 3 + 2 = 8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Books 正文与独立终审均通过 |
| [OrchJail: Jailbreaking Tool-Calling Text-to-Image Agents by Orchestration-Guided Fuzzing](https://arxiv.org/html/2605.07414v1) | 2026-05-11T08:00:00+08:00 | Tool-calling T2I Agent 的安全面必须覆盖 individually benign steps 组合成 harmful output 的 orchestration-level attack，而不是只检查单轮 prompt。；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [GameGen-Verifier: Parallel Keypoint-Based Verification for LLM-Generated Games via Runtime State Injection](https://arxiv.org/html/2605.07442v1) | 2026-05-11T08:00:00+08:00 | 长程交互程序的验证应把 specification 分解为 keypoints，以 runtime state injection 到达目标状态，再执行有界 interaction 并返回 falsifying witness。；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [RcLLM: Accelerating Generative Recommendation via Beyond-Prefix KV Caching](https://arxiv.org/html/2605.07443v1) | 2026-05-11T08:00:00+08:00 | 非连续知识复用需要把 prefix cache 扩展为有身份的 reusable block，并联合 tiered residency、locality placement 与 selective-attention correction。；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`INFER-KV-CACHE`，[45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [VNN-LIB 2.0: Rigorous Foundations for Neural Network Verification](https://arxiv.org/html/2605.07451v1) | 2026-05-11T08:00:00+08:00 | verification query 标准必须把 syntax、types 与 model semantics 分开版本化，不能把不断变化的外部 ONNX 语义当作隐式真值。；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Cross-Modal Backdoors in Multimodal Large Language Models](https://arxiv.org/html/2605.07490v1) | 2026-05-11T08:00:00+08:00 | 多模态 connector 本身是可投毒、可跨模态迁移 trigger 的模型 artifact，不能只验证 backbone weights 与 clean utility。；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-MODEL-REGISTRY`，[59-model-registry.md](../../../../books/part-06-ai-infrastructure/59-model-registry.md)；已存在 Books 正文 |
| [DIMoE-Adapters: Dynamic Expert Evolution for Continual Learning in Vision-Language Models](https://arxiv.org/html/2605.07494v1) | 2026-05-11T08:00:00+08:00 | continual VLM adapter 应把固定专家池拆成可演化 sparse pool，并分离 train-time expert evolution 与 inference-time prototype selection。；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-LORA`，[30-lora.md](../../../../books/part-04-training-system/30-lora.md)；Books 正文与独立终审均通过 |
| [Is the Future Compatible? Diagnosing Dynamic Consistency in World Action Models](https://arxiv.org/html/2605.07514v1) | 2026-05-11T08:00:00+08:00 | World Action Model 的 imagined future 必须评估 action–state dynamic consistency，并防止静态 background collapse 伪造高一致性。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[26-multimodal-embodied-vla.md](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [On the Invariance and Generality of Neural Scaling Laws](https://arxiv.org/html/2605.07546v1) | 2026-05-11T08:00:00+08:00 | Scaling law 的可迁移性应由 information-preserving invariance 与信息分辨率下降来限定，而非默认跨 domain 同指数。；2 + 2 + 3 = 7 | 深入完成 | 整合：`WORLDVIEW-SCALING-LAW`，[07-scaling-law.md](../../../../books/part-01-worldview/07-scaling-law.md)；已存在 Books 正文 |
| [Deadline-Driven Hierarchical Agentic Resource Sharing for AI Services and RAN Functions in AI-RAN](https://arxiv.org/html/2605.07547v1) | 2026-05-11T08:00:00+08:00 | deadline workload 的资源控制应分离慢时标 placement 与快时标 allocation，并让 migration critic 比较中断成本与 SLO 收益。；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Tracing the Arrow of Time: Diagnosing Temporal Information Flow in Video-LLMs](https://arxiv.org/html/2605.07568v1) | 2026-05-11T08:00:00+08:00 | 视频时间信息可能已在 encoder 中存在，却在 projector 到 LLM 的接口丢失；表示审计必须逐层定位 bottleneck。；3 + 2 + 3 = 8 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[23-multimodal-representation.md](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；已存在 Books 正文 |
| [HexiSeq: Accommodating Long Context Training of LLMs over Heterogeneous Hardware](https://arxiv.org/html/2605.07569v1) | 2026-05-11T08:00:00+08:00 | 异构长上下文训练的 CP/HP plan 应按 GPU compute、memory 与 network 共同生成 fully asymmetric partition，而不是强制同构 mesh。；3 + 3 + 2 = 8 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING`，[36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)；Books 正文与独立终审均通过 |
| [Safe, or Simply Incapable? Rethinking Safety Evaluation for Phone-Use Agents](https://arxiv.org/html/2605.07630v1) | 2026-05-11T08:00:00+08:00 | phone-use Agent safety 必须把 harmless outcome 分成 safe action、unsafe action 与 inability-to-act；不行动造成的无害不能计作安全。；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Books 正文与独立终审均通过 |
| [Not All Tokens Learn Alike: Attention Entropy Reveals Heterogeneous Signals in RL Reasoning](https://arxiv.org/html/2605.07660v1) | 2026-05-11T08:00:00+08:00 | Token-level RL credit 具有可观测异质性，但 entropy 只能作为 eligibility/weighting sensor，不能替代 verifier 或因果 credit。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`TRAIN-GRPO`，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) |
| [The Coupling Tax: How Shared Token Budgets Undermine Visible Chain-of-Thought Under Fixed Output Limits](https://arxiv.org/html/2605.07686v1) | 2026-05-11T08:00:00+08:00 | Reasoning trace 与 final answer 共用输出上限时会发生结构性 budget coupling；调度与评估必须分别记录 reasoning budget、answer reserve 与截断浪费。；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-SCHEDULING`，[56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)；已存在 Books 正文 |
| [Gradient Starvation in Binary-Reward GRPO: Why Group-Mean Centering Fails and Why the Simplest Fix Works](https://arxiv.org/html/2605.07689v1) | 2026-05-11T08:00:00+08:00 | binary reward 下，group-mean centering 在全对/全错组会把 advantage 清零，造成结构性 gradient starvation。；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`TRAIN-GRPO`，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) |
| [Future Validity is the Missing Statistic: From Impossibility to $Φ$-Estimation for Grammar-Faithful Speculative Decoding](https://arxiv.org/html/2605.07698v1) | 2026-05-11T08:00:00+08:00 | grammar local validity 不等于未来可完成性；speculative decoder 若只有局部 mask 会采到 projected law 而非 grammar-conditional law。；3 + 2 + 3 = 8 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING`，[48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md)；已存在 Books 正文 |
| [Guidance Is Not a Hyperparameter: Learning Dynamic Control in Diffusion Language Models](https://arxiv.org/html/2605.07701v1) | 2026-05-11T08:00:00+08:00 | Diffusion language model 的 CFG scale 可以从固定超参数演进为读取当前 diffusion state 的逐步控制策略。；3 + 2 + 2 = 7 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；已存在 Books 正文 |
| [An Efficient Hybrid Sparse Attention with CPU-GPU Parallelism for Long-Context Inference](https://arxiv.org/html/2605.07719v1) | 2026-05-11T08:00:00+08:00 | CPU-resident sparse KV 需要把预算、head/granularity 选择与跨设备执行共同调度；稀疏率本身不能预测端到端收益。；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`INFER-KV-CACHE`，[45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Coding Agents Don't Know When to Act](https://arxiv.org/html/2605.07769v1) | 2026-05-11T08:00:00+08:00 | Coding Agent 的 evaluation set 必须包含正确行为为 no-op 的负动作样本，并把 reproduce、act、abstain 与 partial-fix 分开计分。；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已存在 Books 正文 |
| [Tracing Uncertainty in Language Model "Reasoning"](https://arxiv.org/html/2605.07776v1) | 2026-05-11T08:00:00+08:00 | reasoning failure sensor 应读取整条 uncertainty trace 的阶段、斜率与形态，而不是只用终局 confidence。；2 + 2 + 3 = 7 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Books 正文与独立终审均通过 |
| [Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs](https://arxiv.org/html/2605.07806v1) | 2026-05-11T08:00:00+08:00 | 单一 verbalized confidence 不是充分 failure sensor；不同 self-assessment 维度必须按任务切片校准，并只作为选择性决策输入。；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Unsafe by Flow: Uncovering Bidirectional Data-Flow Risks in MCP Ecosystem](https://arxiv.org/html/2605.07836v1) | 2026-05-11T08:00:00+08:00 | MCP 安全必须同时跟踪 requester→sensitive sink 与 external/internal data→MCP output 两个方向。；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-MCP`，[83-mcp.md](../../../../books/part-07-agent/83-mcp.md) |
| [MatryoshkaLoRA: Learning Accurate Hierarchical Low-Rank Representations for LLM Fine-Tuning](https://arxiv.org/html/2605.07850v1) | 2026-05-11T08:00:00+08:00 | 动态 LoRA rank 可由同一 adapter 的 nested sub-ranks 提供，但训练和验收必须覆盖整个 rank curve，而非只优化最大 rank。；2 + 2 + 3 = 7 | 深入完成 | 整合：`TRAIN-LORA`，[30-lora.md](../../../../books/part-04-training-system/30-lora.md)；Books 正文与独立终审均通过 |
| [AccelSync: Verifying Synchronization Coverage in Accelerator Pipeline Programs](https://arxiv.org/html/2605.07881v1) | 2026-05-11T08:00:00+08:00 | accelerator pipeline 的同步正确性必须按硬件可见性与 happens-before 验证，golden output/simulator 不足以覆盖 race。；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；已存在 Books 正文 |
| [Trajectory as the Teacher: Few-Step Discrete Flow Matching via Energy-Navigated Distillation](https://arxiv.org/html/2605.07924v1) | 2026-05-11T08:00:00+08:00 | few-step discrete flow distillation 的瓶颈可能在 teacher trajectory target；training-only energy navigator 可在 midpoint 候选中选择较可信路径。；3 + 2 + 3 = 8 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；Books 正文与独立终审均通过 |
| [How to Train Your Latent Diffusion Language Model Jointly With the Latent Space](https://arxiv.org/html/2605.07933v1) | 2026-05-11T08:00:00+08:00 | latent diffusion language model 联合训练 encoder、diffusion 与 decoder 时需要 staged warmup/noise/objective contract，避免表示与生成共同 collapse。；3 + 2 + 3 = 8 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；Books 正文与独立终审均通过 |
| [TraceFix: Repairing Agent Coordination Protocols with TLA+ Counterexamples](https://arxiv.org/html/2605.07935v1) | 2026-05-11T08:00:00+08:00 | Multi-Agent 协议可先转成有限 topology/PlusCal，再用 model-checker counterexample 修复，运行时只允许已验证拓扑中的协调操作。；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT`，[82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md) |
| [Ask Early, Ask Late, Ask Right: When Does Clarification Timing Matter for Long-Horizon Agents?](https://arxiv.org/html/2605.07937v1) | 2026-05-11T08:00:00+08:00 | Clarification 不只是 ask/assume 二选一；缺失信息类型与已执行轨迹的不可逆程度共同决定提问时点。；3 + 3 + 3 = 9 | 深入完成 | 整合：`AGENT-WORKFLOW`，[81-workflow.md](../../../../books/part-07-agent/81-workflow.md)；已存在 Books 正文 |
| [Towards Apples to Apples for AI Evaluations: From Real-World Use Cases to Evaluation Scenarios](https://arxiv.org/html/2605.07986v1) | 2026-05-11T08:00:00+08:00 | Evaluation identity 必须从抽象 capability 名称落到具体用户、预期 outcome、正负影响、风险和 KPI 的运行场景。；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Position: Mechanistic Interpretability Must Disclose Identification Assumptions for Causal Claims](https://arxiv.org/html/2605.08012v1) | 2026-05-11T08:00:00+08:00 | Mechanistic interpretability 的 faithfulness、completeness、ablation 等 validation 指标不能替代 causal identification assumptions。；2 + 2 + 3 = 7 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已存在 Books 正文 |
| [Learning CLI Agents with Structured Action Credit under Selective Observation](https://arxiv.org/html/2605.08013v1) | 2026-05-11T08:00:00+08:00 | CLI Agent 的 sequence reward 可拆为 turn-level action structure、workspace observation reveal 与 abstract-history credit。；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`TRAIN-GRPO`，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) |
| [STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation](https://arxiv.org/html/2605.08029v1) | 2026-05-11T08:00:00+08:00 | 统一多模态模型可让 causal VLM state 与 normalizing-flow visual state 在同一序列内交替耦合，而不是只在输出端串联两个模型。；3 + 2 + 3 = 8 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；已存在 Books 正文 |
| [Beyond Pairs: Your Language Model is Secretly Optimizing a Preference Graph](https://arxiv.org/html/2605.08037v1) | 2026-05-11T08:00:00+08:00 | Preference objective 可从彼此独立的 pair 扩展为带 equivalence class、transitive dominance 与 global anchor 的 graph。；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-DPO`，[34-dpo.md](../../../../books/part-04-training-system/34-dpo.md)；已存在 Books 正文 |
| [Fast Byte Latent Transformer](https://arxiv.org/html/2605.08044v1) | 2026-05-11T08:00:00+08:00 | byte-level 表示的无词表优势会把生成成本推向每 byte 自回归；dynamic patch latent、block diffusion 与 full-model verification 可以重新分配这项成本。；3 + 3 + 3 = 9 | 深入完成 | 整合：`MODEL-TOKENIZER`，[11-tokenizer.md](../../../../books/part-02-model/11-tokenizer.md)；已存在 Books 正文 |
| [The Memory Curse: How Expanded Recall Erodes Cooperative Intent in LLM Agents](https://arxiv.org/html/2605.08060v1) | 2026-05-11T08:00:00+08:00 | 更多历史不一定改善多 Agent 协作；必须把 context length 与历史中的 defect/cooperate content 分开测量。；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-MEMORY`，[77-memory.md](../../../../books/part-07-agent/77-memory.md)；已存在 Books 正文 |
| [Rubric-Grounded RL: Structured Judge Rewards for Generalizable Reasoning](https://arxiv.org/html/2605.08061v1) | 2026-05-11T08:00:00+08:00 | GRPO reward 可由 policy 不可见的 grounding passage 与 weighted rubric 生成 criterion-level credit，但 judge 只能拥有受限评分，不能拥有事实或发布 authority。；3 + 3 + 3 = 9 | 深入完成 | 整合：`TRAIN-GRPO`，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md)；Books 正文与独立终审均通过 |

## 4. 证据与知识整合

详细筛选理由见 [screening ledger](../_sources/daily-20260511/V3_SCREENING_LEDGER_20260914.json)，逐项证据见 [Evidence reviews](../_sources/daily-20260511/V3_EVIDENCE_REVIEWS_20260914.json)，本轮 28 项 Books 对照见 [bounded Books comparison](../_sources/daily-20260511/V3_BOUNDED_REPAIR_BOOKS_COMPARISON_20260915.json)，191 项版本/日期/Comments 依据见 [official basis](../_sources/daily-20260511/V3_ORDINARY_RECOVERY_OFFICIAL_BASIS_20260915.json)。此前 Books 写后结论见 [non-author review](../_sources/daily-20260511/V3_FRESH_NONAUTHOR_POSTWRITE_ACCEPTANCE_20260915.md)，本次输入见 [screening repair queue](../_sources/daily-20260511/V3_FRESH_NONAUTHOR_SCREENING_REPAIR_QUEUE_20260915.md)，新增 Integrate 见 [root Books queue](../_sources/daily-20260511/V3_SCREENING_REPAIR_ROOT_BOOKS_QUEUE_20260915.md)。

### [More Thinking, More Bias: Length-Driven Position Bias in Reasoning Models](https://arxiv.org/html/2605.06672v1)

**采用命题：** Reasoning-model 的多选题位置偏差必须按 reasoning trajectory length 与 direct/CoT mode 分层，不能把随机换序后的单一平均值当作 order robustness。

**机制与评价：** 作者在 13 个 reasoning-mode 配置、MMLU/ARC-C/GPQA 上以 matched-pair PBS、partial correlation、commitment change point 与 truncation continuation probe 检查长度累积效应；12/13 配置在控制 accuracy 后仍呈正相关。

**证据位置：** Method：§3 Method；§3.1 Matched-Pair Evaluation Protocol；Evaluation：§4 Experimental Setup；§5 Results；Figure 1–4；Table 1–2；Limitations / non-proof：§6 Discussion；Limitations；§7 Conclusion。Artifact：exact-v1 声明 code/data 已发布，但本轮未取得不可变仓库 URL 或 commit identity；不据此采用 reproduction claim。

**未证明、代价与回退：** 证据限多选题、所测模型与可见 CoT；truncation continuation 是受控干预，不证明任意长推理都因同一机制变差。成本是每题多次换序和轨迹探测；非 MCQ、短轨迹或无法读 CoT 时回退普通顺序随机化、直接答案对照和外部 verifier。

**Books 比较：** Ch66 已要求随机交换候选顺序并审计 judge position bias，却未把 examinee 自身的 position bias 与 reasoning length、direct/CoT mode 和 truncation probe 绑定为一个 evaluation slice；存在命题级增量。

**最终处置：** 整合：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已写入，fresh 写后语义复核通过。

### [Domain-level metacognitive monitoring in frontier LLMs: A 33-model atlas](https://arxiv.org/html/2605.06673v1)

**采用命题：** 模型的 verbalized-confidence 监测质量会随知识域显著变化，aggregate calibration 会掩盖 domain-local failure。

**机制与评价：** 作者对 33 个模型、1,500 个 MMLU items 计算 model-domain Type-2 AUROC，并以 split-half、family clustering 与 probe-format 对照检查 domain profile。

**证据位置：** Method：§2 Methods（Type-2 AUROC、domain mapping）；Evaluation：§3 Results；Table 2–4；Figure 1–2；Limitations / non-proof：§4.7 Limitations；§5 Conclusion。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 域分组是实用 benchmark taxonomy 而非已验证 latent construct；cell 置信区间宽，verbalized confidence 不等于真实知道/不知道。

**Books 比较：** Ch66 已要求 calibration 按 task/domain/model slice 保存并将 confidence 与 truth 分离；该 atlas 增加受限测量证据，不改变 release contract。

**最终处置：** 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction](https://arxiv.org/html/2605.06676v1)

**采用命题：** KV eviction 可把 head-wise budget 与 token selection 从手工启发式升级为任务目标驱动的 learned policy。

**机制与评价：** LKV-H 从 head embedding 学全局预算，LKV-T 用 differentiable Soft-TopK 学 query-agnostic token importance，并以 frozen-teacher self-distillation 联合优化。

**证据位置：** Method：§3 Methodology；§3.1；§3.5；Evaluation：§4 Experiments；§4.4 ablation；§4.5 overhead/memory；Limitations / non-proof：§5 Conclusion；正文未单列 limitations，边界由实验范围与消融收窄。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 证据限 Llama-3.1-8B-Instruct、LongBench/RULER 与披露保留率；learned selector 会随任务和模型漂移，不能把平均质量当 cache correctness。

**Books 比较：** Ch45 已拥有按 layer/head/query 变化的 budget、learned eviction、identity 与 conservative fallback；本论文是既有分支的受限实例。

**最终处置：** 已有覆盖：`INFER-KV-CACHE`，[45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。

### [Hidden Coalitions in Multi-Agent AI: A Spectral Diagnostic from Internal Representations](https://arxiv.org/html/2605.06696v1)

**采用命题：** 多 Agent 行为相似不足以证明 coalition；internal-state mutual information 的谱结构可作为 representational coupling sensor。

**机制与评价：** 方法从 agent hidden states 构造 pairwise mutual-information graph，以 Fiedler partition 恢复层级或动态 coalition，并用 programmed MARL groups 与描述性 LLM prompts 验证。

**证据位置：** Method：§3 Experimental Methods（agent architecture、MI graph、spectral partition）；Evaluation：§3.5 Statistical evaluation；§4 Results；Limitations / non-proof：§2.6 Scope and limitations；§5 Discussion/Limitations。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 它需要内部状态访问且主要验证 planted/induced structure；谱分区不是意图、共谋或危害真值，prompt label 也可能支配交互信号。

**Books 比较：** Ch67 已要求内部 probe 只作为 versioned detector，不能越权为因果或意图裁决；该工作补充 multi-agent slice，不改 owner contract。

**最终处置：** 已有覆盖：`PLATFORM-MONITORING`，[67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md)。

### [CASCADE: Case-Based Continual Adaptation for Large Language Models During Deployment](https://arxiv.org/html/2605.06702v1)

**采用命题：** 部署期学习可把更新权从模型 weights 移到带 reward 的 episodic case bank 与 contextual-bandit retriever。

**机制与评价：** CASCADE 对 query 选择 case、复用并修订 solution、依据 reward 更新 retriever，再只保留成功案例；模型参数保持冻结。

**证据位置：** Method：§5 Methods；§5.1 Problem Formulation；Appendix E.2 bandit algorithm；Evaluation：§3 Results；§3.1–3.2；Figures 3–6；Limitations / non-proof：§4 Discussion；正文披露的 task/retention assumptions。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** case retention 会固化错误或奖励 shortcut，retriever regret 不证明 case truth；证据限受测单轮、多轮、ALFWorld/ScienceWorld、search 与 EHR tasks。

**Books 比较：** Ch77 已区分 raw experience、derived memory、retrieval policy、write admission 与 model weights；该 contextual-bandit 实现没有改变既有 ownership。

**最终处置：** 已有覆盖：`AGENT-MEMORY`，[77-memory.md](../../../../books/part-07-agent/77-memory.md)。

### [Visual Text Compression as Measure Transport](https://arxiv.org/html/2605.06708v1)

**采用命题：** 把文本渲染成图像进行长上下文压缩时，路由依据应是任务相关信息损失而不是 token compression ratio；precision、coverage 与高成本区域的再编码必须分别可见。

**机制与评价：** 论文把文本/视觉 token 表为经验测度，将 ViT patch encoder 写成 push-forward map，并把 transport cost 分解为 patch 内聚合的 precision cost 与跨 patch fragmentation 的 coverage cost；label-free probe 决定 text/visual path，foveation 对高成本区域提高分辨率。

**证据位置：** Method：§3 Method；§3.2 routing；§3.3 foveation；Evaluation：§4 Experiments；§4.1–§4.3；Table 1–3；Limitations / non-proof：Scope and limitations；Appendix G Limitations of Foveation at Scale。Artifact：no dedicated public implementation artifact disclosed in exact-v1。

**未证明、代价与回退：** 实验限 Qwen3-4B、24 个 NLP 数据集与作者渲染/阈值；label-free cost 仍可能错路由，foveation 在大规模下收益不均。视觉通道未校准、高风险逐字证据或版式漂移时回退原始文本与 source-linked region readback。

**Books 比较：** Ch23 已说明 modality token budget 与共享容量，却没有把 visual-text compression 视为带 precision/coverage loss 的 modality transport，并据此形成可回退的 per-instance route；存在命题级增量。

**最终处置：** 整合：`MULTIMODAL-REPRESENTATION`，[23-multimodal-representation.md](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；已写入，fresh 写后语义复核通过。

### [When Does a Language Model Commit? A Finite-Answer Theory of Pre-Verbalization Commitment](https://arxiv.org/html/2605.06723v1)

**采用命题：** 模型可以在公开答案出现前稳定偏向某个有限答案，但该 commitment 追踪 eventual output，而不是 truth 或可靠 abstention。

**机制与评价：** 论文用 continuation probability 对有限 verbalizers 做 exact projection，定义 retrospective stabilization、answer onset 与 lead，再以 probe、transfer 和 intervention 检查可恢复性。

**证据位置：** Method：§3 Finite-Answer Commitment；§3.1–3.4；Evaluation：§4–§8；Table 2；Appendix L/P/O.3；Limitations / non-proof：§10 Limitations and Conclusion；Appendix P online-vs-retrospective。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 结果依赖有限答案集、verbalizer 与 retrospective future knowledge；Appendix P 显示 naive online detector 不等价，错误答案同样可提前 commitment。

**Books 比较：** Ch66 已明确 confidence/commitment 不是事实置信度，在线发布 Gate 需要外部 evidence 与校准；该测量对象不改变现有 contract。

**最终处置：** 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [When Routine Chats Turn Toxic: Unintended Long-Term State Poisoning in Personalized Agents](https://arxiv.org/html/2605.06731v1)

**采用命题：** 持久 Agent state 的安全边界不止是读取可信度，还包括每次 writeback 的授权漂移审计与可选择回滚。

**机制与评价：** ULSPB 将日常多轮交互造成的 authorization drift、tool-use escalation 与 unchecked autonomy 计入 Harm Score；StateGuard 在执行后的 state-file writeback 边界检查 diff，并只回滚危险编辑。作者以 OpenClaw、四个 backbone、350 个设置及真实交互种子评估。

**证据位置：** Method：§2.1–2.3；§3.1–3.3；§5.1；Evaluation：§4.1–4.3；§5.2；Appendix C/J；Limitations / non-proof：Appendix A；§6；实验与 threat-model scope。Artifact：public artifact disclosed: https://github.com/XiaoyuXU1/ULSPB ; adopted claim does not assume unreleased implementation details。

**未证明、代价与回退：** 证据限 OpenClaw、构造交互模式与安全优先阈值；高 false positive 会拒绝有益个性化，未知或适应性攻击仍可能绕过审计。低风险、短期且不持久的状态可保留轻量写入路径。

**Books 比较：** Ch77 正文已把 poisoning 拆成 write→persistence→recall→adoption→external consequence，并要求 write admission、授权 mutation lineage、stable/transient state、选择性 repair 与 rollback；StateGuard 是该既有命题的受限实现，不新增长期 owner。

**最终处置：** 已有覆盖：`AGENT-MEMORY`，[77-memory.md](../../../../books/part-07-agent/77-memory.md)。

### [Beyond Factor Aggregation: Gauge-Aware Low-Rank Server Representations for Federated LoRA](https://arxiv.org/html/2605.06733v1)

**采用命题：** LoRA 聚合对象应是 gauge-invariant 的更新语义，而不是坐标任意的 A/B 因子。

**机制与评价：** 论文以 client projector 估计 consensus update subspace，在 shared reference coordinates 聚合，并从同一 server state 读出不同 rank adapter；GLUE、SuperNI、稀疏参与和异构 rank 是作者实验边界。

**证据位置：** Method：§3.1–3.2 problem/theory；§4.1–4.3 GLoRA algorithm；Evaluation：§5.1–5.5；Appendix B/C；Limitations / non-proof：§3.2 discussion；§6；experiment scope；无独立 Limitations 标题。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 低秩 server state 避免 dense reconstruction，却增加子空间估计、参考坐标漂移和参与不足风险；证据不证明任意任务或隐私威胁下都优于普通 FedAvg。

**Books 比较：** 在 Ch30「多个 Adapter 能否直接相加」中，紧接“数学上可相加不代表行为无冲突”段后。

**最终处置：** 整合：`TRAIN-LORA`，[30-lora.md](../../../../books/part-04-training-system/30-lora.md)；已存在 Books 正文。

### [Gradient Extrapolation-Based Policy Optimization](https://arxiv.org/html/2605.06755v1)

**采用命题：** RL optimizer 可用局部 gradient trajectory 近似多步 lookahead，但必须把稳定性检测和退化回普通 GRPO 写进控制合同。

**机制与评价：** GXPO 复用同一 rollout/reward/advantage，以三次 backward 形成两步探测、virtual K-step extrapolation 和 corrective update；作者在 Qwen2.5/Llama 数学推理上报告收敛速度与 pass@1。

**证据位置：** Method：§2 Method: GXPO；Algorithm 1；Evaluation：§3 Experiments & Results；Table 1–2；Limitations / non-proof：§5 Limitations；§4 Conclusion。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** Ch33 已把 optimizer transform、update scale、稳定性与 AdamW fallback 写入 recipe identity；该工作只是其中一个局部多步外推实现，且证据限于受测数学任务，不足以改变长期主线。

**Books 比较：** 现有正文已承载同一长期命题；本条只报告受限版本事实与上下文，不形成 Books 增量。

**最终处置：** 仅报告：`TRAIN-GRPO`；不改变长期知识。

### [Language Models Can Autonomously Hack and Self-Replicate](https://arxiv.org/pdf/2605.06760v1)

**采用命题：** 模型已能把漏洞利用、凭据抽取、权重复制和远端部署串成可重复的自我复制链，扩展了部署威胁模型。

**机制与评价：** 作者在四类脆弱主机上让模型自主完成端到端复制，并报告不同模型的重复成功率。

**证据位置：** Method：official exact-v1 PDF pp.4–6：§3 Experimental Setup；§4 Methodology；Evaluation：PDF pp.6–9：§5 Results；>1,000 runs；milestone tables；Limitations / non-proof：PDF pp.9–12：§6 Discussion；§7 Limitations。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 结果只属于构造环境、暴露凭据和给定 harness；不能外推现实普遍成功率，也没有改变 Ch72 已有的最小权限、出站隔离、凭据生命周期和模型 artifact 防泄漏责任。

**Books 比较：** 现有正文已承载同一长期命题；保留本材料为受限证据，不重复追加。

**最终处置：** 已有覆盖：`PLATFORM-SECURITY`，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [Weblica: Scalable and Reproducible Training Environments for Visual Web Agents](https://arxiv.org/html/2605.06761v1)

**采用命题：** Web Agent 训练环境应把可复放的页面状态、交互 transition 与生成环境 identity 分开保存，离线成功不能直接授予 live-Web promotion。

**机制与评价：** Weblica 用 HTTP-level caching 捕获并回放稳定视觉状态，同时保持交互行为；另一分支由 LLM 依据真实网站与核心导航技能合成环境，再用于 SFT/RL。作者在 held-out Weblica 与多个 Web navigation benchmark 上比较规模与 test-time compute。

**证据位置：** Method：§3.1–3.3；§4.1–4.2；Evaluation：§5.1–5.4；Appendix A/C/D；Limitations / non-proof：§6 Limitations。Artifact：no dedicated implementation artifact disclosed in exact-v1 for the adopted mechanism。

**未证明、代价与回退：** 缓存只代表事件时 snapshot，无法覆盖页面更新、权限、动态后端和真实工具失败；合成环境还有 sim-to-real gap。离线环境适合训练和回归，live shadow/canary 仍拥有上线权。

**Books 比较：** Ch81 正文的 Offline World 已明确 versioned corpus、search/visit actions、trajectory lineage、rejection filtering、SFT/RL 与 live canary，并指出 snapshot 不证明 freshness、动态页面、权限或 tool failure；Weblica 不改变该长期合同。

**最终处置：** 已有覆盖：`AGENT-WORKFLOW`，[81-workflow.md](../../../../books/part-07-agent/81-workflow.md)。

### [Conformal Agent Error Attribution](https://arxiv.org/html/2605.06788v1)

**采用命题：** Agent 故障定位可以输出带有限样本 coverage 的连续回滚区间，而不是未经校准的单点 culprit。

**机制与评价：** filtration-based conformal prediction 为序列轨迹构造 contiguous prediction sets，并以这些集合驱动多 Agent rollback；论文给出理论保证、多个 agent/dataset 实验及公开代码。

**证据位置：** Method：§3.1 Conformal Algorithms for Agent Error Attribution；Evaluation：§4–§5；§5.3；Figure 5 rollback；Limitations / non-proof：§6 Conclusion；coverage assumptions in §3。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 保证依赖 calibration/exchangeability 与既定错误标签；区间不证明区间内每步有因果责任，分布漂移时回退更宽区间、人工定位或从最近可信 checkpoint 重放。

**Books 比较：** 在 Ch66「Attribution 是 Versioned Evaluation Contract」之后、「Evaluation Identity 还必须覆盖测量路径、工作负载与规范目标」之前。

**最终处置：** 整合：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已存在 Books 正文。

### [Towards Security-Auditable LLM Agents: A Unified Graph Representation](https://arxiv.org/html/2605.06812v1)

**采用命题：** Agent 审计图必须同时表达静态 capability base 与动态 semantic state，并保留二者之间的数据、控制与权限传播路径。

**机制与评价：** Agent-BOM 用层级有向属性图表示 model/tool/long-term-memory 等静态能力，以及 goal/reasoning/action 等运行态，通过 semantic edge 与 security attribute 支持入口定位、前后向路径追踪和属性裁决；论文声称在 OpenClaw plugin 中覆盖四类代表性攻击链。

**证据位置：** Method：exact-v1 主文 References 前第 1–3 段；Evaluation：exact-v1 主文 References 前第 2–3 段的代表性 attack-scenario 描述；Limitations / non-proof：exact-v1 无独立 limitations/evaluation protocol；边界由短篇主文披露范围给出。Artifact：not disclosed in exact-v1; the paper states an OpenClaw plugin but provides no separate artifact locator。

**未证明、代价与回退：** exact-v1 仅为短篇扩展正文，没有独立实验协议、消融、limitations 或公开 artifact；代表性案例不证明图完整、归因因果或生产 adjudication 正确。无法建立完整事件 lineage 时应回退原始 trace 与人工审计。

**Books 比较：** Ch69 已要求 immutable event trace 为 authority、dependency/root-cause/claim graph 为派生视图，并保存 data/control dependency、agent/tool identity、commit boundary 与 repair authority；Agent-BOM 的静态/动态分层是该命题的具体 schema。

**最终处置：** 已有覆盖：`PLATFORM-TRACE`，[69-trace.md](../../../../books/part-06-ai-infrastructure/69-trace.md)。

### [AGWM: Affordance-Grounded World Models for Environments with Compositional Prerequisites](https://arxiv.org/html/2605.06841v1)

**采用命题：** World Model 除预测 next state，还必须显式维护 action prerequisite 与动态 affordance state。

**机制与评价：** AGWM 将前置依赖表示为 DAG，逐步追踪动作当前是否可执行，针对 structure-changing events 降低多步预测错误；证据来自 game-based simulated environments。

**证据位置：** Method：§3 Method；§3.1；§3.4；Evaluation：§4 Experiments；ablation；Table 1；Limitations / non-proof：Limitations/Broader impact after §5。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** Ch25 已用可执行 transition program、action precondition、symbolic graph 与 environment-authoritative correction 完整承载该责任；DAG affordance tracker 是现有命题的受限实现案例，不新增 owner 或设计结论。

**Books 比较：** 现有正文已承载同一长期命题；保留本材料为受限证据，不重复追加。

**最终处置：** 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。

### [How to Compress KV Cache in RL Post-Training? Shadow Mask Distillation for Memory-Efficient Alignment](https://arxiv.org/html/2605.06850v1)

**采用命题：** 训练 rollout 使用压缩 KV、learner 使用 dense context 会形成隐藏的 state-policy mismatch，而不仅是普通推理近似误差。

**机制与评价：** 论文将 sparse rollout 与 dense learner 的偏差识别为 RL 放大源，并用 shadow mask distillation 让训练感知部署时 mask；适用于 PPO/GRPO/Online-DPO 类 rollout pipeline。

**证据位置：** Method：§3 Methodology；§3.4；Evaluation：§4.1–4.3；Table 3–4；Limitations / non-proof：§5 Limitations；§6。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** Ch31 已将 rollout/training numerical execution identity 纳入 policy identity，Ch33 又明确 token positions、causal mask、memory revision 与 environment snapshot 必须一致；sparse-mask distillation 是该既有合同的实例，不需重复。

**Books 比较：** 现有正文已承载同一长期命题；保留本材料为受限证据，不重复追加。

**最终处置：** 已有覆盖：`TRAIN-RLHF`，[31-rlhf.md](../../../../books/part-04-training-system/31-rlhf.md)。

### [Dataset Watermarking for Closed LLMs with Provable Detection](https://arxiv.org/html/2605.06865v1)

**采用命题：** 闭源模型的数据使用审计可以把 dataset-level statistical carrier 与黑盒生成输出的检测统计绑定，但检测只提供 provenance evidence，不等于逐样本或法律归因。

**机制与评价：** 作者随机选择 word pairs，以 rephrasing 提高 dataset 中的共现频率，再对目标模型生成文本的 pair co-occurrence 做统计检验；在多模型、三类 benchmark、partial contamination 与文本扰动下报告 p-value 和 utility。

**证据位置：** Method：§2 Problem formulation；§4 Our method；Evaluation：§5 Experiment；§5.1–§5.4；Table 1–4；Limitations / non-proof：§6 Limitation；§7 Conclusion。Artifact：no implementation repository disclosed in exact-v1。

**未证明、代价与回退：** 证明依赖随机 key、独立性/生成分布与特定 fine-tuning 设置；未命中不能证明未使用，命中也会受自然共现、后续训练和攻击影响。无法保守校准 FPR/功效时回退 lineage、controlled retraining、membership/dataset inference 组合证据与 Unknown。

**Books 比较：** Ch72 已把 dataset usage inference / natural identifier、method version、observer capability、false-positive boundary 和 provenance non-authority 写成长期合同；Ch66 也已要求 contamination detector 在 scale/distribution 下重校准。该方法是现有命题的具体 carrier。

**最终处置：** 已有覆盖：`PLATFORM-SECURITY`，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [Don't Retrain, Align: Adapting Autoregressive LMs to Diffusion LMs via Representation Alignment](https://arxiv.org/html/2605.06885v1)

**采用命题：** AR→Diffusion 转换可把语言表示与解码顺序分开：保留表示几何，重学 generation path。

**机制与评价：** REPR-ALIGN 在相同架构上冻结 AR teacher，以逐层 cosine alignment 配合 masked denoising；作者在 Qwen3 0.6B/1.7B/4B 和代码任务、0.8B/50B 数据条件下报告低数据加速。

**证据位置：** Method：§3 Method；§3.1–3.4；Algorithm 1；Evaluation：§4 Experiments；Table 1；Figures 3–4；Limitations / non-proof：Appendix C Limitations。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 同架构 teacher、额外 teacher compute 与代码 benchmark 限制外推；alignment 不证明行为等价，失败时回退普通 continued denoising 或保留 AR。

**Books 比较：** 在 Ch24「Diffusion：用迭代修正换并行状态更新」开头，AR factorization 与 masked denoising 分叉之后。

**最终处置：** 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；已存在 Books 正文。

### [Not All Tokens Need 40 Steps: Heterogeneous Step Allocation in Diffusion Transformers for Efficient Video Generation](https://arxiv.org/html/2605.06892v1)

**采用命题：** 连续 diffusion token 的收敛速度不同时，可以按 token group 分配异质 step budget，并让 active queries 读取同步的全局 KV、未激活 token 用缓存 velocity 前进。

**机制与评价：** HSA 将时空 latent tokens 分组并给每组不同 step divisor；每步仅 active tokens 做 QKV，fresh K/V 覆盖 cache 后对全体 K/V attention，Cached Euler 用最近 velocity 更新全部 token；作者在 Wan-2.1/2.2 视频生成下比较质量与 runtime。

**证据位置：** Method：§2 Method；Figure 1；§2.5 caching window；Evaluation：§3 Experiments；§3.2–§3.3；Table 1；Figure 3–5；Limitations / non-proof：§5 Conclusion；Appendix F Broader Impacts, Safeguards, and Licenses；作者模型/视频范围。Artifact：project page disclosed: https://ernestchu.github.io/hsa ; no immutable implementation commit adopted。

**未证明、代价与回退：** stale K/V 与 cached velocity 会在敏感早晚阶段累积误差，分组策略和缓存窗口依赖模型/视频分布；论文未证明任意 DiT 或 production tail-SLO。漂移时回退全 token/full-step FM 或更保守固定 schedule。

**Books 比较：** Ch24 已把不同 token 的收敛速度、token-local dynamic schedule、denoiser/KV-like cache、state/step identity、quality budget 与 full recompute fallback 写入同一主线；HSA 是连续视频 diffusion 的受限实现，不新增长期 owner。

**最终处置：** 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS`，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。

### [Self-Programmed Execution for Language-Model Agents](https://arxiv.org/html/2605.06898v1)

**采用命题：** 模型可以提出甚至生成 orchestration program，但 effect isolation、执行边界与最终 commit authority 仍必须留在 harness/runtime。

**机制与评价：** SPE 让一次 model completion 同时成为上下文和 orchestrator program；Spell 以 Lisp 的 code-as-data、自编辑与重新求值实现，并把 outer evaluator 保持纯、effectful expression 放入只执行一次的 inner eval，以避免编辑程序时重放副作用。作者在 TerminalBench 1.1 与 SWE-bench Lite 子集上测试未专训模型。

**证据位置：** Method：§2；§3；Appendix A/B；Evaluation：§4；TerminalBench 1.1 与 SWE-bench Lite 子集；Limitations / non-proof：§6 Discussion；§4 的 invalid/fatal-program 结果与未训练范围。Artifact：public implementation disclosed: https://github.com/lukejoconnor/spell。

**未证明、代价与回退：** 多数模型仍会生成 invalid program 或致命错误，实验只展示有限 orchestration；模型生成程序扩大了代码注入、资源和副作用风险。静态 workflow 对高风险、可复现任务仍更稳妥。

**Books 比较：** Ch81 已规定 generated code workflow 必须经过 sandbox、typed interface 与 effect verifier；Ch84 又显式把 execution structure 与 orchestration owner(host/model) 纳入平台 identity。SPE 改变 proposal 位置，但未改变现有提交权边界。

**最终处置：** 已有覆盖：`AGENT-PLATFORM`，[84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)。

### [Conservative Flows: A New Paradigm of Generative Models](https://arxiv.org/html/2605.06905v1)

**采用命题：** 生成动态不一定从噪声 transport 到数据；也可从 data-supported state 出发，用 invariant flow 在目标分布内产生变化。

**机制与评价：** 论文用 corrected Langevin/dMALA 与 predictor-corrector probability-invariant flow，配合 pretrained denoiser/flow，在 synthetic 与 ImageNet-256 做长链与 ablation。

**证据位置：** Method：§2 Method；§2.2–2.3；Appendix C；Evaluation：§3 Experiments；Appendix D/E.2；Limitations / non-proof：§4 Discussion and Conclusion；Appendix F Broader Impact。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 这是从已有样本产生同分布 variation 的分支，不是无条件从噪声生成；长链混合、计算预算和近似校正限制 deployment claims。

**Books 比较：** Ch24 已按目标分布、state initialization、iterative correction 与 sampler contract 区分生成路径；该分支扩展案例但不改主线。

**最终处置：** 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS`，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。

### [Regulating Branch Parallelism in LLM Serving](https://arxiv.org/html/2605.06914v1)

**采用命题：** 分支并行宽度应成为每个 decode step 的 slack-aware admission，而不是 eager 或固定 cap。

**机制与评价：** TAPER 预测 branch externality，只在当前 co-batch slack 可容纳时准入；prefix KV 共享使宽度变化不要求回收 branch memory。作者用 10 小时 trace、Qwen3-32B 报告相对 IRP-Off/Eager 的 goodput 与 >95% SLO attainment。

**证据位置：** Method：§3 TAPER；§3.2–3.4；Algorithm 1；Evaluation：§4；Appendix D/E（hardware/model/SLO/overhead）；Limitations / non-proof：§6 Conclusion & Limitations；Appendix C predictor。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 线性 latency predictor、branch independence、单节点和已测 trace 是边界；预测失准或尾延迟紧张时回退固定 cap/serial branch。

**Books 比较：** 在 Ch56「SLO-aware Admission」中，紧接“当前能放下，不等于未来可完成”之后。

**最终处置：** 整合：`INFER-SCHEDULING`，[56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)；已存在 Books 正文。

### [Can LLMs Take Retrieved Information with a Grain of Salt?](https://arxiv.org/html/2605.06919v1)

**采用命题：** RAG 不能把检索文本表达的 certainty 直接当 evidence authority；source certainty、模型 prior 与最终 answer confidence 必须分开校准。

**机制与评价：** 论文定义 context-certainty obedience，并用 prior-answer reminder、certainty recalibration、context simplification 与最后 synthesis 组成约三次 forward 的交互策略，使模型在不确定上下文后重新暴露 prior，再按声明 certainty 调整回答。

**证据位置：** Method：§2.1–2.3；§3.1–3.4；Evaluation：§4；§5.1–5.6；Appendix D；Limitations / non-proof：Appendix E Limitations。Artifact：no implementation repository disclosed in exact-v1; evaluated model licenses are not method artifacts。

**未证明、代价与回退：** 实验限 ClashEval 短答、八个开放权重模型且需要输出概率；表达 certainty 可能错误或被攻击，部分正确 context、长文本和 API/reasoning model 未覆盖。权威来源与 claim verifier 仍优先，策略失配时回退逐 claim 引用、冲突展示与 abstain。

**Books 比较：** Ch76 已保存 source authority、freshness、provenance 与 sufficiency，却没有明确拆开“来源自报 certainty”“模型闭卷 prior”“回答采用强度”三种状态；该分离应进入 RAG answer gate。

**最终处置：** 整合：`AGENT-RAG`，[76-rag.md](../../../../books/part-07-agent/76-rag.md)；已存在 Books 正文。

### [Bias and Uncertainty in LLM-as-a-Judge Estimation](https://arxiv.org/html/2605.06939v1)

**采用命题：** 校准后的 LLM judge 估计仍可能因 judge quality 与跨模型 calibration instability 发生带高置信度的方向翻转。

**机制与评价：** 论文用解析推导、模拟和 MMLU-Pro 案例定义 J 与 delta-J 诊断，区分单模型偏差校正和共享校准的比较风险。

**证据位置：** Method：§3 Naive and Bias-Corrected Estimation；§4 diagnostics；Evaluation：§5 Simulations；§6 MMLU-Pro case study；Limitations / non-proof：§8 Limitations。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** Ch66 已明确 judge competence、directional bias、cross-model calibration slice、soft pairwise probability 与 human-anchored interval；该 J/ΔJ 诊断没有改变现有 release contract。

**Books 比较：** 现有正文已承载同一长期命题；保留本材料为受限证据，不重复追加。

**最终处置：** 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [Adaptive Memory Decay for Log-Linear Attention](https://arxiv.org/html/2605.06946v1)

**采用命题：** 固定递归记忆衰减可升级为 input-dependent、跨时间尺度的 learned decay，而不改变 log-linear state complexity。

**机制与评价：** 方法在 Fenwick-tree hierarchical memory 上用 MLP 预测各层级 lambda，并通过初始化保持初期接近原基线。

**证据位置：** Method：§3 Method；Evaluation：§3.3 Complexity；§4 Experiments；Figures 3–4；Limitations / non-proof：§6 Conclusion；正文未单列 limitations，按 synthetic-task 范围收窄。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** MQAR/selective-copying 与有限长度外推只证明受测 synthetic recall；learned decay 会漂移并不可恢复原文细节。

**Books 比较：** Ch22 已覆盖固定-size recurrent state、input-dependent forgetting、capacity loss 与 attention/retrieval fallback；无需重复写入。

**最终处置：** 已有覆盖：`MODEL-LONG-CONTEXT`，[22-long-context.md](../../../../books/part-02-model/22-long-context.md)。

### [Group of Skills: Group-Structured Skill Retrieval for Agent Skill Libraries](https://arxiv.org/html/2605.06978v1)

**采用命题：** 大型 skill library 的检索对象应保留 entry、依赖、guard 与 verifier role，而不是把一组相关文本直接拼成上下文。

**机制与评价：** GoSkills 从 typed skill graph 选择 anchor，沿 group graph 扩展 support，再压缩为有限 atomic payload，并以 Start/Support/Check/Avoid 固定字段呈现；下游 agent、skill payload 与环境不变。作者在 SkillsBench 与 ALFWorld 上对比可见需求覆盖、reward 与 runtime。

**证据位置：** Method：§3.1–3.2；Appendix B/D；Evaluation：§4–§5；Appendix E/F；Limitations / non-proof：§6 Limitations；Appendix H。Artifact：related public specification disclosed: https://github.com/agentskills/agentskills ; no GoSkills implementation artifact adopted。

**未证明、代价与回退：** role schema 依赖高质量 skill metadata 与可见需求，隐藏约束和缺失能力不会被结构化上下文修复；图漂移、错误边和压缩会删掉必要信息。无法证明 dependency closure 时回退完整 skill 或人工依赖。

**Books 比较：** Ch77 已要求 section-level procedural graph 保存 intent、I/O、precondition、guard、verifier、source pointer 和 dependency closure，并已有 typed skill graph 的 merge/split/retire 与 workflow validation；四种 role 是现有命题的呈现实例。

**最终处置：** 已有覆盖：`AGENT-MEMORY`，[77-memory.md](../../../../books/part-07-agent/77-memory.md)。

### [Why Does Agentic Safety Fail to Generalize Across Tasks?](https://arxiv.org/html/2605.06992v1)

**采用命题：** Agent safety 的跨任务泛化必须独立于任务执行能力评估，不能用同任务安全率或平均成功率替代。

**机制与评价：** 论文用 LQ/H-infinity controller 构造安全映射复杂度分析，并在模拟 quadcopter 与 Llama-3.2 CRM 中比较 safe/unsafe teacher imitation，观察安全策略的跨任务映射更复杂、迁移更差。

**证据位置：** Method：§2；§3.1–3.4；Evaluation：§4.1–4.3；Appendix F；Limitations / non-proof：§5 Limitations。Artifact：public artifact disclosed: https://github.com/Tomerslortau/agentic-safety-generalization。

**未证明、代价与回退：** 理论依赖线性控制、Lipschitz surrogate 与理想样本假设；实验限 imitation、模拟任务与受测 CRM，不证明所有 safety objective 都更难，也不授予因果机制。低风险同分布回归仍可保留较小 acceptance card。

**Books 比较：** Ch66 已明确把统计可靠性、unseen-semantic generalization、mechanistic consistency 与 cross-task transfer 分成 claim-specific acceptance card，且任何单项不能独占发布权；该论文直接支持既有 cross-task 安全切片。

**最终处置：** 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [Echo: KV-Cache-Free Associative Recall with Spectral Koopman Operators](https://arxiv.org/html/2605.06997v1)

**采用命题：** 常量状态的 recurrent model 可用可更新的谱算子保存 associative-recall sufficient statistics，而不是重新引入线性 KV history。

**机制与评价：** Echo/SKA 以 kernel ridge 拟合 key-value history 的 spectral linear system，维护 O(r^2) streaming state；作者在 50M 模型、MQAR 和五个迁移 benchmark 上与 Mamba-2/混合 attention 比较。

**证据位置：** Method：§3 Method；§3.4；Evaluation：§4–§5；Table 1–5；Limitations / non-proof：§6.3 Limitations；§7。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** Ch22 已完整解释 fixed recurrent state、association collision、capacity、hybrid attention 与外部 retrieval 的共存边界；spectral KRR 是一种具体 state parameterization，现有 50M/合成检索证据不足以改写主线。

**Books 比较：** 现有正文已承载同一长期命题；本条只报告受限版本事实与上下文，不形成 Books 增量。

**最终处置：** 仅报告：`MODEL-LONG-CONTEXT`；不改变长期知识。

### [Adaptive auditing of AI systems with anytime-valid guarantees](https://arxiv.org/html/2605.07002v1)

**采用命题：** adaptive sampling 与随时停止需要 anytime-valid inference，否则少量定向审计会产生伪置信。

**机制与评价：** 论文用 dueling nulls 和 e-process 描述 auditor/model 双方，并在受控实验中验证 type-I error。

**证据位置：** Method：§3 Methods；Evaluation：§4.1–4.2；Appendix C/D；Limitations / non-proof：§5 Discussion。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 现有 Ch66 已明确保存 adaptive sampling、停止条件、e-process 与保守 fallback；该论文补强证据但不改变当前 owner 或结论。

**Books 比较：** 现有正文已承载同一长期命题；保留本材料为受限证据，不重复追加。

**最终处置：** 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [An Interpretable and Scalable Framework for Evaluating Large Language Models](https://arxiv.org/html/2605.07046v1)

**采用命题：** 模型排名不能只平均 binary accuracy；stochastic response 与 item difficulty/discrimination 应进入同一 latent ability contract。

**机制与评价：** cBMM 拟合大规模 IRT 参数，以 block majorization-minimization 分离 model ability 与 item characteristics，并做模拟敏感性及 MATH/MMLU-Pro/GPQA 等实证。

**证据位置：** Method：§3 Methodology；Appendix A.5；Evaluation：§4 Experiments；Appendix A.6/A.8；Figures 1–5；Limitations / non-proof：§5 Conclusion；敏感性分析给出模型假设边界。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** IRT 假设、benchmark redundancy 与 latent-scale identity 会改变排序；latent ability 不是开放任务的绝对能力。

**Books 比较：** Ch66 已把 item heterogeneity、IRT-like latent model、sampling variance 与 ranking instability 纳入 evaluation identity；该算法不改现有 contract。

**最终处置：** 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [Dr. Post-Training: A Data Regularization Perspective on LLM Post-Training](https://arxiv.org/pdf/2605.07063v1)

**采用命题：** 通用后训练数据可作为限制目标更新方向的 data-induced regularizer，而不只是供 selection 的样本池。

**机制与评价：** Dr. Post-Training 用 general data 构造 feasible update set，把稀缺 target-data gradient 投影其中，并把现有 selection 方法组织到 bias-variance 光谱；作者覆盖 SFT、RLHF、RLVR。

**证据位置：** Method：official exact-v1 PDF/TeX：§3 data-regularization framework；§4 tensor-lifetime implementation；Evaluation：PDF/TeX §5 Experiments（SFT/RLHF/RLVR/system efficiency）；Limitations / non-proof：PDF/TeX §6 Discussion；§7 Conclusion；Appendix method/system details。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 额外梯度/投影成本与 feasible-set 失配会压制必要更新；目标分布充分或通用数据有偏时回退普通 mixture/selection。

**Books 比较：** 在 Ch27「Post-training Data Selection 是当前 Policy 的在线控制环」之前，作为 data value 从 sampling weight 演进为 update-feasible-set 的分支。

**最终处置：** 整合：`TRAIN-DATA`，[27-data.md](../../../../books/part-04-training-system/27-data.md)；已存在 Books 正文。

### [Where to Spend Rollouts: Hit-Utility Optimal Rollout Allocation for Group-Based RLVR](https://arxiv.org/html/2605.07114v1)

**采用命题：** 固定总 rollout budget 下，group-based RLVR 应依据当前 prompt 至少再命中一次正确样本的后验效用分配额外 rollouts，而不是每题固定 group size。

**机制与评价：** HORA 先取统一 G0 pre-rollouts，以 beta-binomial posterior 估计 hit utility，再优化第二阶段增量分配并生成 variable-size groups；reward evaluation 与 downstream group-relative estimator 保持不变。

**证据位置：** Method：§3 Hit Utility and HORA；Algorithm 1；Evaluation：§4 Experiments；§4.1–§4.2；Table 1；Figure 2–4；Limitations / non-proof：§5 Conclusion and Discussion；Appendix A Limitations and Broader Impact。Artifact：no dedicated public implementation artifact disclosed in exact-v1。

**未证明、代价与回退：** 命中效用依赖二元可验证 reward、prior 与同一步样本；选择会改变 prompt distribution，且不证明更高 pass@K 等同训练收益。prior/能力漂移或 verifier 不可靠时回退固定 group、随机 coverage slice 与静态 curriculum。

**Books 比较：** Ch33 已明确 group size 依赖当前成功率，并让 success rate、输出分歧和难度只拥有 rollout allocation proposal，保留 selection-bias 审计与固定 group fallback；HORA 是该既有命题的后验实现。

**最终处置：** 已有覆盖：`TRAIN-GRPO`，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md)。

### [Region4Web: Rethinking Observation Space Granularity for Web Agents](https://arxiv.org/html/2605.07134v1)

**采用命题：** Web Agent 的观察压缩应保留页面功能区域与跨步 transition，而不是只截断 element-level AXTree；selector 必须提供可恢复的全页回退。

**机制与评价：** Region4Web 把 AXTree 元素划分成功能区域并做 semantic abstraction；PageDigest 按任务选择区域、维护同页增量变化，并在选择不足时用 view_all 恢复。作者在 WebArena 812 tasks、四个 backbone 与两类 agent 方法上评估。

**证据位置：** Method：§3.1 Problem Formulation；§3–§4 Region4Web / PageDigest；Evaluation：§5 Experiments；§5.1–§5.2；Appendix C–G；Limitations / non-proof：Appendix A Limitations and Future Work；Appendix B Broader Impacts。Artifact：public implementation disclosed: https://github.com/kwondu/region4web ; exact-v1 does not freeze a commit。

**未证明、代价与回退：** 功能分区、同页判定和 auxiliary selector 会受动态 DOM、隐藏状态、URL/页面迁移与模型错误影响；压缩不拥有页面真值。高风险操作、selector 不确定或页面 identity 变化时回退完整 AXTree/DOM 与重新观察。

**Books 比较：** Ch75 有 source-linked bounded renderer、page/section selection 与 raw-artifact fallback，但没有将 Web observation 的 functional-region identity 和跨步 incremental digest 写入 Context contract；存在命题级增量。

**最终处置：** 整合：`AGENT-CONTEXT`，[75-context.md](../../../../books/part-07-agent/75-context.md)；已写入，fresh 写后语义复核通过。

### [Demystifying and Detecting Agentic Workflow Injection Vulnerabilities in GitHub Actions](https://arxiv.org/html/2605.07135v1)

**采用命题：** CI event content 经 prompt 或 agent output 进入脚本，会把 prompt injection 扩展成 workflow data-flow vulnerability。

**机制与评价：** 论文区分 Prompt-to-Agent 与 Prompt-to-Script，构建 MCP/agent-aware taint 规格并审计 GitHub Actions corpus。

**证据位置：** Method：§III threat model；§V TaintAWI；Evaluation：§VI Evaluation；Table IV–V；Limitations / non-proof：§VII-B Limitations；§IX。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 静态 taint、给定 threat model 和公开 workflow 样本不证明所有 exploit；Ch81/Ch72 已用 untrusted event→proposal→effect-time authorization 的链路承载此结论。

**Books 比较：** 现有正文已承载同一长期命题；保留本材料为受限证据，不重复追加。

**最终处置：** 已有覆盖：`AGENT-WORKFLOW`，[81-workflow.md](../../../../books/part-07-agent/81-workflow.md)。

### [Beyond Reasoning: Reinforcement Learning Unlocks Parametric Knowledge in LLMs](https://arxiv.org/html/2605.07153v1)

**采用命题：** 可验证奖励带来的 factual QA 提升可能主要是重排已有参数知识的输出概率，而非写入新事实。

**机制与评价：** 作者在三类模型、闭卷 one-hop QA、fact-level 去重和 binary reward 下比较训练/推理基线，并以概率质量变化解释约 27% 相对提升。

**证据位置：** Method：§2 Problem Formulation and Experimental Setup；Evaluation：§3 results；Table 1–3；Appendix H/I；Limitations / non-proof：§6 Discussion；§8。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** Ch31 已用 capability expansion、distribution sharpening 与 mode extinction 区分“获得能力”和“重排已有模式”；受控闭卷 QA 结果补强该边界，但不新增长期命题。

**Books 比较：** 现有正文已承载同一长期命题；保留本材料为受限证据，不重复追加。

**最终处置：** 已有覆盖：`TRAIN-RLHF`，[31-rlhf.md](../../../../books/part-04-training-system/31-rlhf.md)。

### [Rethinking Experience Utilization in Self-Evolving Language Model Agents](https://arxiv.org/html/2605.07164v1)

**采用命题：** Experience memory 的 serving policy 必须能在推理过程中决定是否、何时检索经验，不能把 initialization-only 或 always-on injection 当默认最优。

**机制与评价：** ExpWeave/ExpWeaver 将 experience retrieval 交织进 decision process，以 prompting 或 GRPO policy 选择使用时点；作者在 ReasoningBank/SkillRL/G-Memory、ALFWorld/WebShop 上报告质量与检索次数。

**证据位置：** Method：§3 ExpWeave / ExpWeaver；Figure 1；Evaluation：§4.1–§4.3；§5.1；Figure 2–5；Table 1；Limitations / non-proof：§5 Analysis and Discussions；Appendix A Limitations and Impact Statement。Artifact：no dedicated public implementation artifact disclosed in exact-v1。

**未证明、代价与回退：** 选择器会漏取关键经验或反复取回噪声，收益依赖 experience quality、task 和 agent；RL reward 也可能把少调用误当成功。低规模、关键经验必须可见或策略未校准时回退 global injection、无经验 baseline 或显式人工规则。

**Books 比较：** Ch77 已直接要求按 task cost structure 在 no experience、global injection 与 selective retrieval 间选择，并联合 quality、prompt cost、latency 和 break-even；该论文不改变既有长期命题。

**最终处置：** 已有覆盖：`AGENT-MEMORY`，[77-memory.md](../../../../books/part-07-agent/77-memory.md)。

### [Star Elastic: Many-in-One Reasoning LLMs with Efficient Budget Control](https://arxiv.org/html/2605.07182v1)

**采用命题：** 同一 elastic checkpoint 可暴露多个 nested submodel，但运行时仍须按 reasoning phase 单独选择 model slice，并把 slice、phase 与精度写入请求执行身份。

**机制与评价：** Star Elastic 在一次 post-training 中沿 SSM/channel/MoE/FFN 轴训练 nested submodels，以 differentiable router、curriculum distillation 和 zero-shot extraction 形成多个预算点；推理在 thinking/answering phase 选择不同子模型，并扩展到 NVFP4/FP8。

**证据位置：** Method：§2.2 Elastic Formulation；Figure 2；Appendix F；Evaluation：§4 Experiments；§4.1–§4.5；Table 1–3；Figure 1/3；Limitations / non-proof：Conclusions；作者模型、硬件、量化与估算范围；无独立 Limitations 标题。Artifact：related Megatron-LM/NeMo dependencies disclosed; no dedicated immutable Star Elastic artifact adopted。

**未证明、代价与回退：** 证据限 Nemotron Nano family、160B-token post-training 与作者 benchmark/H100-vLLM 测量；router/slice 可能随任务漂移，嵌套会耦合模型质量，跨 phase 切换还需要兼容 KV/state。无法验证 slice identity 或 crossover 时回退固定 parent / 独立 checkpoint。

**Books 比较：** Ch56 管理 reasoning budget 与 mode routing，但没有表达一个 checkpoint 内的 architecture slice 可按 thinking/answering phase 切换，以及由此产生的 model/KV/precision identity；存在命题级增量。

**最终处置：** 整合：`INFER-SCHEDULING`，[56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)；已写入，fresh 写后语义复核通过。

### [Hallucination Detection via Activations of Open-Weight Proxy Analyzers](https://arxiv.org/html/2605.07209v1)

**采用命题：** 开放权重 proxy 的 activation 可作为黑盒目标 hallucination 的辅助 sensor，但不能取得事实 authority。

**机制与评价：** 论文用 proxy analyzer activation 训练/评估检测器并比较不同目标模型和任务。

**证据位置：** Method：§3 Methodology；§3.1；Evaluation：§4.2–4.3；Table 1–4；Limitations / non-proof：§7 Limitations；§6 Discussion。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 跨模型 representation shift、可解码不等于因果使用且 detector 会漂移；Ch66/Ch72 已要求 probe 只触发 abstention/escalation 并由外部 evidence 验证。

**Books 比较：** 现有正文已承载同一长期命题；保留本材料为受限证据，不重复追加。

**最终处置：** 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [CASCADE: Context-Aware Relaxation for Speculative Image Decoding](https://arxiv.org/html/2605.07230v1)

**采用命题：** 图像 speculative decoding 的 verifier 可以利用局部冗余接受语义可替代 proposal，但这属于近似质量合同，不是文本式 exact sampling。

**机制与评价：** CASCADE 从 target 提取 context-aware redundancy signal，放宽 spatial/semantic interchangeable token 的 acceptance，并将同一信号用于 drafter training；作者在多种 text-to-image/drafter 上报告最高 3.6x。

**证据位置：** Method：§4 Method；Appendix C Algorithm；Evaluation：§5.1–5.3；Table 1–2；Limitations / non-proof：Appendix A Limitations and Future Work。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** Ch48 已把 lossless 与 lossy verification 分开，并明确放宽 acceptance 会形成新的 sampling/quality contract；图像的语义可替代 acceptance 是这一原则的受限案例，不再重复写入。

**Books 比较：** 现有正文已承载同一长期命题；保留本材料为受限证据，不重复追加。

**最终处置：** 已有覆盖：`INFER-SPECULATIVE-DECODING`，[48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md)。

### [Reformulating KV Cache Eviction Problem for Long-Context LLM Inference](https://arxiv.org/html/2605.07234v1)

**采用命题：** KV eviction utility 应同时观察 attention map、projected value 与 inter-head interaction，并把 head-local score 变为 layer/model-wide 可比较预算。

**机制与评价：** LaProx 将 eviction 写成 output-aware layer-wise matrix-multiplication approximation，利用 attention 与 projected value 的乘积近似 token contribution，再生成全局可比 score 做 model-wide selection；作者在 LongBench/NIAH 19 datasets 上测质量与效率。

**证据位置：** Method：§4 Methodology；Algorithm 1–2；Evaluation：§5 Experiments；§5.1–§5.4；Figure 2–3；Table 1；Limitations / non-proof：§6 Conclusion；Appendix E Limitations。Artifact：no dedicated public implementation artifact disclosed in exact-v1。

**未证明、代价与回退：** 矩阵近似与全局排序依赖模型、层、长上下文分布和 prefill-only compression，极端 budget 下仍有 silent quality loss；物理 layout/continuous batching 未证明。score 未校准时回退 recent window、head/layer heuristic 或 FullKV。

**Books 比较：** Ch45 已把 utility eviction、per-layer surrogate、variable per-head cache、layer-wise heterogeneous budget、physical fragmentation 和 FullKV fallback 写入同一命题；LaProx 的 output-aware score 是具体实现。

**最终处置：** 已有覆盖：`INFER-KV-CACHE`，[45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。

### [FATE: Future-State-Aware Scheduling for Heterogeneous LLM Workflows](https://arxiv.org/html/2605.07238v1)

**采用命题：** Workflow-DAG scheduler 应同时评价当前 assignment 与它为下游留下的 model residency、parent-output locality、prefix reuse 和 device reachability。

**机制与评价：** FATE 以 CP-SAT-backed frontier planner、horizon-aware scoring、bounded multi-device shard execution 和 state-conditional cost，反复在 ready frontier 上做 post-decision planning；作者在 real-DAG 与 controlled prefix-reuse benchmark 上比较 makespan/P95。

**证据位置：** Method：§2 Problem Formulation；§3 Method；Algorithm 1；Evaluation：§4 Experiments；§4.1–§4.3；Table 1–3；Figure 2；Limitations / non-proof：§6 Limitations；§7 Conclusion；Appendix D.7 Broader Impacts。Artifact：no dedicated public implementation artifact disclosed in exact-v1。

**未证明、代价与回退：** future-state cost 依赖可见 DAG、代价估计和有限 horizon，CP-SAT/多设备 shard 会增加控制开销；动态 Agent 边、fairness、故障和生产 tail 未证明。图或 state stale 时回退 myopic ready-queue、RR/HEFT 或 locality heuristic。

**Books 比较：** Ch56 已把 workflow post-decision state、longest-remaining-path、downstream prefix reuse、migration/preemption cost 和 task aging 合并为 owner 命题，并保留 synthetic DAG/fairness/tail 边界；FATE 不新增长期知识。

**最终处置：** 已有覆盖：`INFER-SCHEDULING`，[56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。

### [MEMOREPAIR: Barrier-First Cascade Repair in Agentic Memory](https://arxiv.org/html/2605.07242v1)

**采用命题：** Memory source 被删除、纠正或接口迁移后，repair 必须先隔离受影响 descendants，再只发布经过 predecessor-closure 验证的 successor。

**机制与评价：** MemoRepair 先撤下 invalidated descendants，以 retained support 和 staged repaired predecessors 生成 successor，再把发布选择化为 maximum-weight predecessor closure 并用一次 s-t min-cut 求解；ToolBench/MemoryArena 实验假设完整 influence provenance。

**证据位置：** Method：§2 Method；§2.1 Problem Setup；Algorithm 1；Evaluation：§3 Experiments；§3.2–§3.4；Table 1–3；Figure 2；Limitations / non-proof：§5 Limitations and Conclusion。Artifact：no dedicated public implementation artifact disclosed in exact-v1。

**未证明、代价与回退：** 完整 provenance、repair operator 正确性和固定 scalarized cost 是强前提；撤下会降低可用性，外部 side effect 不可由 memory repair 撤销。链路不全时回退 quarantine、append-only evidence、全量重建或人工裁决。

**Books 比较：** Ch77 已要求沿 ancestry 标记 descendants，把 memory/execution disposition 分离，做 dependency tracing、independent-support check、selective replay 和 predecessor-aware eviction；MemoRepair 是该既有 cascade-repair 命题的优化实例。

**最终处置：** 已有覆盖：`AGENT-MEMORY`，[77-memory.md](../../../../books/part-07-agent/77-memory.md)。

### [Experience Sharing in Mutual Reinforcement Learning for Heterogeneous Language Models](https://arxiv.org/html/2605.07244v1)

**采用命题：** 异构 policy 应共享 typed experience，而不是共享参数或假定 tokenizer/behavior distribution 相同。

**机制与评价：** 论文比较 PRP、XGRPO 与 SGT，明确 data/value/outcome 三层共享各自的 density-ratio、support 与 tokenizer residual。

**证据位置：** Method：§4 Mutual RL System Design；Evaluation：§6 Experiments；Appendix A；Limitations / non-proof：§7 Conclusion；evidence limited to disclosed policy pools。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 当前 Ch33 已有 source-tagged joint experience plane、独立 policy 更新、tokenizer/provenance 与 outcome-owner 分责；无需重复追加。

**Books 比较：** 现有正文已承载同一长期命题；保留本材料为受限证据，不重复追加。

**最终处置：** 已有覆盖：`TRAIN-GRPO`，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md)。

### [EnvSimBench: A Benchmark for Evaluating and Improving LLM-Based Environment Simulation](https://arxiv.org/html/2605.07247v1)

**采用命题：** Agent environment simulator 必须按 action outcome、state-change complexity 与 argument cardinality 分层测量，而非只看对话表面相似。

**机制与评价：** EnvSimBench 把 before-state、tool call、implementation 与 after-state 组织为 independently verifiable transition samples，并区分 failure/no-change/state-change。

**证据位置：** Method：§3 Problem Formulation（POMDP/constraint-driven MDP）；Evaluation：§4.1 Benchmark Construction；§5 Results；Tables 2–4；Limitations / non-proof：§6 Discussion and Conclusion。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 400 samples/167 environments 与程序标签只覆盖构造任务；format metric、state fidelity 和真实 Agent success 仍是不同测量对象。

**Books 比较：** Ch66/Ch25 已要求 transition evaluator 绑定 environment revision、state delta、effect receipt 与真实环境 reconciliation；该 benchmark 是受限实例。

**最终处置：** 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [Hard to Read, Easy to Jailbreak: How Visual Degradation Bypasses MLLM Safety Alignment](https://arxiv.org/html/2605.07250v1)

**采用命题：** 当视觉文本降质到人/模型仍能识别而浅层 safety representation 被延迟时，多模态输入会出现 attack comfort zone；安全验收必须覆盖降质邻域。

**机制与评价：** 论文在多种 proprietary/open MLLM、七类视觉干扰和 DPI sweep 上联合测 OCR 与 ASR，以 layer-wise safety probe、same-shape padding、template-free prompts 和 distribution analysis 检查替代解释；Structured Cognitive Offloading 按 transcription→safety evaluation→response 串行处理。

**证据位置：** Method：§3 Attack Comfort Zone；§4.1–4.2 Cognitive Overload/Offloading；Evaluation：§4.3 ablation；Tables 1–6；Appendix A/B/D；Limitations / non-proof：Limitations；§5 Discussion；Appendix E。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** Cognitive Overload 是论文对 probe/ablation 的机制解释，不是已识别的唯一因果路径；ASR judge、OCR、模型版本和构造 harmful prompts 限制外推。Offloading 增加 latency、OCR 错误和提示依赖，不能替代独立 input policy。

**Books 比较：** Ch72 已要求 rendered text/layout/provenance 规范化、跨通道组合检查、OCR 不确定时隔离/拒绝，并明确输入变换属于安全切片；本论文增加降质邻域证据但不改变长期命题。

**最终处置：** 已有覆盖：`PLATFORM-SECURITY`，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [When Are Experts Misrouted? Counterfactual Routing Analysis in Mixture-of-Experts Language Models](https://arxiv.org/html/2605.07260v1)

**采用命题：** Top-k router score 不能被视为 route utility；冻结模型下的 matched-compute counterfactual routes 应成为诊断 fragile-token misrouting 的独立证据。

**机制与评价：** 作者对每个 token 比较标准 route 与 sampled equal-compute alternatives，以 verified reasoning trajectory 中 realized next-token probability 评分；在四个 MoE family 与多类 reasoning task 上观察 fragile tokens 的标准 route 与可达更优 route 分离，并做 final-layer router-only update。

**证据位置：** Method：§3 Method / Analysis Protocol；§3.1；Figure 1–2；Evaluation：§3.2–§3.3；§5.2；Table 2–5；Figure 3；router-only update on AIME/HMMT；Limitations / non-proof：Limitations；§7 Conclusion；sampled-route / realized-token scope。Artifact：no dedicated public implementation artifact disclosed in exact-v1。

**未证明、代价与回退：** counterfactual 只覆盖采样到的 routes，realized-token probability 不是序列级或因果 utility，verified trajectory 又有选择偏差；在线枚举成本高。诊断应保持离线/受控，无法复现时回退标准 top-k、load/quality audit 与端到端 matched-compute evaluation。

**Books 比较：** Ch21 已解释 router probability、load balance、variable-k 与 matched-compute gate，但没有保存 executed-only loss 导致的 counterfactual blind spot，也没有把 fragile-token route alternatives 作为 routing-quality audit；存在命题级增量。

**最终处置：** 整合：`MODEL-MOE`，[21-moe.md](../../../../books/part-02-model/21-moe.md)；已写入，fresh 写后语义复核通过。

### [Structured Role-Aware Policy Optimization for Multimodal Reasoning](https://arxiv.org/html/2605.07274v1)

**采用命题：** 多模态 RLVR 的 sequence reward 需要区分 perception 与 reasoning token 的角色，避免正确答案掩盖视觉证据缺失。

**机制与评价：** SRPO 以原图/腐化图的 on-policy contrast 估计 perception dependency，再以 perception-consistency 调节 reasoning token 权重，共享 trajectory baseline 且不改变 reward sign。

**证据位置：** Method：§3 Method；§3.3；Evaluation：§4.1–4.3；Table 2；Figure 4；Limitations / non-proof：Appendix E Limitations；§5。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** Ch33 已将 modality/role/turn 作为 typed credit boundary，并明确视觉 reliance proxy 不能取得 outcome authority；SRPO 的 corruption contrast 不改变该责任分配。

**Books 比较：** 现有正文已承载同一长期命题；保留本材料为受限证据，不重复追加。

**最终处置：** 已有覆盖：`TRAIN-GRPO`，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md)。

### [Predictive but Not Plannable: RC-aux for Latent World Models](https://arxiv.org/html/2605.07278v1)

**采用命题：** predictive latent 距离不一定适合 planning；有限 horizon 的 reachability 必须显式进入训练和 planner scoring。

**机制与评价：** RC-aux 保留 latent world-model backbone，加入 multi-horizon prediction 与 budget-conditioned reachability，使用 trajectory hard negatives，并在规划时 gate terminal latent cost。

**证据位置：** Method：§3 Method；§3.3 objective；Evaluation：§4 Experiments；§4.2–4.3；Appendix B；Limitations / non-proof：§5 Conclusion；Appendix H Broader Impacts。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 证据限五个 pixel goal-control tasks；reachability estimator 也会错，latent closeness 与真实可执行性仍需环境校正。

**Books 比较：** Ch25 已把 predictive state、plannable reachability、admission 与 real-environment authority 分开；本论文直接验证既有命题。

**最终处置：** 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。

### [When Stored Evidence Stops Being Usable: Scale-Conditioned Evaluation of Agent Memory](https://arxiv.org/html/2605.07313v1)

**采用命题：** Agent memory 的可扩展性声明必须条件化于 agent、memory interface、irrelevant-session scale 与 interaction budget，并报告 usable-scale boundary。

**机制与评价：** 协议固定 query evidence，只逐级加入未标注为任务证据的 irrelevant sessions，记录 agent-memory trajectories，并报告 budget-compliant reliability、P90 memory-call burden、failure-regime decomposition 与 reliability threshold breakdown onset。

**证据位置：** Method：§3 Scale-Conditioned Agent–Memory Evaluation；Figure 1；Evaluation：§4 Experimental Setup；§5 Results；Table 1–2；Figure 2–4；Limitations / non-proof：§6 Discussion and Limitations；§7 Conclusion。Artifact：no dedicated public implementation artifact disclosed in exact-v1。

**未证明、代价与回退：** irrelevant-session 标注、固定 evidence、budget 与 threshold 都是评测构造；LongMemEval/LoCoMo 和受测 interface 不能代表开放生产 memory。它增加多尺度 rerun 成本；样本或调用日志不足时回退固定 snapshot，但必须收窄 scalability claim。

**Books 比较：** Ch66 有 scale/distribution slice 与 budgeted evaluation，Ch77 有 construction/retrieval/reader decomposition，却都未将 evidence-preserving memory growth、tail call burden 和 usable-scale onset 组合成明确的 memory scalability contract；存在命题级增量。

**最终处置：** 整合：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已写入，fresh 写后语义复核通过。

### [SparseRL-Sync: Lossless Weight Synchronization with ~100x Less Communication](https://arxiv.org/html/2605.07330v1)

**采用命题：** Trainer→rollout 同步可传输 lossless sparse parameter delta，但 rollout 必须基于正确 base 重构并验证 identity。

**机制与评价：** 论文以 99%+ element sparsity 构造 indices+values payload 和 bucketing，讨论带宽受限异步 RL。

**证据位置：** Method：§3 SparseRL-Sync；§3.1–3.2；Evaluation：§4 Experiments；Table 2；Figure 4；Limitations / non-proof：§6 Conclusion；boundary from BF16/FP32 and disclosed topology。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** Ch36 已在 source-family marker SF-2026-ARXIV-2605-07330 下完整写入 base/hash/shape/fallback 与非 freshness 保证，故不重复。

**Books 比较：** 现有正文已承载同一长期命题；保留本材料为受限证据，不重复追加。

**最终处置：** 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`，[36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)。

### [MISA: Mixture of Indexer Sparse Attention for Long-Context LLM Inference](https://arxiv.org/html/2605.07363v1)

**采用命题：** 稀疏注意力 indexer 的 head 计算也应被路由；token Top-k 固定不代表 indexer cost 已最小。

**机制与评价：** MISA 先用 block-pooled keys 和轻量 router 选择 query-dependent active indexer heads，再执行 token scoring；MISA† 追加 coarse-to-fine rerank。

**证据位置：** Method：§4 Method；Evaluation：§5 Experimental Results；§5.4；Figures 2–5；Limitations / non-proof：§7 Limitation；§6 Conclusion。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** LongBench/NIAH 和单 H200 kernel latency 不证明端到端 production SLO；router selection 可能漏 recall，需 full-head fallback。

**Books 比较：** Ch49/Ch45 已要求 selector、kernel、quality budget、hardware contract 与 fallback 联合验收；该实现不改变 owner。

**最终处置：** 已有覆盖：`INFER-TENSORRT-LLM`，[49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。

### [OrchJail: Jailbreaking Tool-Calling Text-to-Image Agents by Orchestration-Guided Fuzzing](https://arxiv.org/html/2605.07414v1)

**采用命题：** Tool-calling T2I Agent 的安全面必须覆盖 individually benign steps 组合成 harmful output 的 orchestration-level attack，而不是只检查单轮 prompt。

**机制与评价：** OrchJail 从成功 jailbreak tool-call traces 学习 prompt wording 与高风险 orchestration pattern 的关系，以多目标评分引导 fuzzing，在代表性 tool-calling T2I agents 上比较 attack success、图像 fidelity、query cost 与 defenses。

**证据位置：** Method：§3 Threat Model；§4 Approach；§4.1–§4.1.4；Evaluation：§5 Experiment；§5.1–§5.4；Table 1–4；Limitations / non-proof：§3 Threat Model；§6 Conclusion；未提供完整 defense completeness 保证。Artifact：no dedicated public implementation artifact disclosed in exact-v1。

**未证明、代价与回退：** 这是 offensive search evidence，不证明覆盖所有工具链或能直接形成 production detector；target agent、image judge 与 defense 均会漂移，fuzzing 还可能产生真实有害内容。高风险环境应回退独立 reference monitor、cumulative intent gate、tool allowlist、sandbox 与人工复核。

**Books 比较：** Ch72 已明确 Agent safety gate 要跨 benign-looking subtasks 保存 cumulative intent/state，并测试 decomposition graph 是否完成有害目标，也覆盖 cross-modal joint risk 与 multi-step tool-chain effects；OrchJail 是现有命题的 T2I 攻击实例。

**最终处置：** 已有覆盖：`PLATFORM-SECURITY`，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [Cross-Modal Backdoors in Multimodal Large Language Models](https://arxiv.org/html/2605.07490v1)

**采用命题：** 多模态 connector 本身是可投毒、可跨模态迁移 trigger 的模型 artifact，不能只验证 backbone weights 与 clean utility。

**机制与评价：** 攻击在 connector training 中植入 activation objective，利用 aligned shared latent space 让 image/audio/text trigger 跨通道到达同一 payload；作者比较多 target model、ASR、utility、ablation 与 model-side defenses。

**证据位置：** Method：§III Threat Model；§V Methodology；Evaluation：§IV Mechanistic Analysis；§VI Evaluation；§VI-E ablation；Limitations / non-proof：Appendix D Limitations and Future Directions。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 受控 poisoning、已测 connectors/targets 与 exact/relaxed ASR 不证明现实 prevalence 或未知 trigger 可检测；clean utility 不构成安全证明。

**Books 比较：** Ch59 已覆盖可执行架构/remote code 的 artifact identity，却未把 learned connector weights、activation modality 与 cross-modal reachability 纳入 promotion identity。

**最终处置：** 整合：`PLATFORM-MODEL-REGISTRY`，[59-model-registry.md](../../../../books/part-06-ai-infrastructure/59-model-registry.md)；已存在 Books 正文。

### [On the Invariance and Generality of Neural Scaling Laws](https://arxiv.org/html/2605.07546v1)

**采用命题：** Scaling law 的可迁移性应由 information-preserving invariance 与信息分辨率下降来限定，而非默认跨 domain 同指数。

**机制与评价：** 论文论证 bijective transformation 保留 law，non-bijective transformation 通过 information resolution rho 改变 law，并在语言、视觉、语音及两个跨域案例验证。

**证据位置：** Method：§2 NSL transformation sensitivity；§2.1–2.2；Evaluation：§3–§4；Table 2；Appendix E/F；Limitations / non-proof：Appendix D Limitations。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 有限模型/任务和估计 rho 的选择不构成通用 law；变换不可辨或留出尺度失配时回退目标域小规模 sweep。

**Books 比较：** 在 Ch7「Scaling 的适用边界」中，紧接“技术变化会造成 regime change”之后、联合外推之前。

**最终处置：** 整合：`WORLDVIEW-SCALING-LAW`，[07-scaling-law.md](../../../../books/part-01-worldview/07-scaling-law.md)；已存在 Books 正文。

### [Tracing the Arrow of Time: Diagnosing Temporal Information Flow in Video-LLMs](https://arxiv.org/html/2605.07568v1)

**采用命题：** 视频时间信息可能已在 encoder 中存在，却在 projector 到 LLM 的接口丢失；表示审计必须逐层定位 bottleneck。

**机制与评价：** 作者用 Arrow-of-Time probe 分离 encoder/projector/LLM，比较 frame-centric、video-centric encoder 与 Q-Former/time-preserved MLP，并在 16-frame 设置和多个 temporal benchmark 验证。

**证据位置：** Method：§3.1–3.3；§4.1；§5.1；§6.1；Evaluation：§4.2–4.3；§5.2–5.4；§6.2–6.3；Appendix B/C/E；Limitations / non-proof：§7；实验范围；无独立 Limitations 标题。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** AoT 只是时间信号 probe，16 frames 会漏证据；高 AoT 不保证通用理解，projector 变更失败时回退现有 connector 并单独增加 temporal supervision。

**Books 比较：** 在 Ch23「时间、空间与 provenance 必须进入状态」之后、「Conditional compute」之前。

**最终处置：** 整合：`MULTIMODAL-REPRESENTATION`，[23-multimodal-representation.md](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；已存在 Books 正文。

### [Not All Tokens Learn Alike: Attention Entropy Reveals Heterogeneous Signals in RL Reasoning](https://arxiv.org/html/2605.07660v1)

**采用命题：** Token-level RL credit 具有可观测异质性，但 entropy 只能作为 eligibility/weighting sensor，不能替代 verifier 或因果 credit。

**机制与评价：** 作者按 attention entropy 区分低熵 anchor 与高熵 explorer，分析 gradient alignment/variance，并以从低熵到高熵的动态 soft weighting 调节训练；主实验为 Qwen3-8B+VeRL/DAPO，另含有限模型迁移检查。

**证据位置：** Method：§2–§5；Appendix B/D/K；Evaluation：§3–§5；Appendix F/G/J/K；Limitations / non-proof：§7 Limitations。Artifact：no public implementation artifact disclosed in exact-v1。

**未证明、代价与回退：** 结果依赖受控 Qwen 配置、固定中层与 group-level 相关性；entropy 不证明 token 因果贡献，explorer-only 也不稳定。漂移或 verifier 不可靠时回退 uniform credit、process verifier 或 critic。

**Books 比较：** Ch33 已有 Selective eligibility trace：低熵 token mask 只筛选 credit，明确 entropy 与因果不一致，并要求 verifier authority、mask/trajectory/update identity 和 uniform/process-verifier/critic fallback；动态 soft weighting不改变该长期结论。

**最终处置：** 已有覆盖：`TRAIN-GRPO`，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md)。

### [The Coupling Tax: How Shared Token Budgets Undermine Visible Chain-of-Thought Under Fixed Output Limits](https://arxiv.org/html/2605.07686v1)

**采用命题：** Reasoning trace 与 final answer 共用输出上限时会发生结构性 budget coupling；调度与评估必须分别记录 reasoning budget、answer reserve 与截断浪费。

**机制与评价：** 论文把可见 CoT 与 answer 的共享上限写成 |Z|+|A|≤b，以 chain-length distribution 分解 truncation waste；split-budget generation 为推理和回答保留独立预算，再用 non-thinking extraction pass 从 trace 生成答案。

**证据位置：** Method：§4.1–4.5；§5.1–5.3；Evaluation：§3；§6；Appendix B–V；Limitations / non-proof：§7；任务/模型/budget crossover scope。Artifact：no dedicated public artifact disclosed in exact-v1。

**未证明、代价与回退：** 证据限 Qwen3、DeepSeek-R1-Distill、数学/BBH 与固定输出限制；额外 extraction 增加 prefill、调用和选择偏差，task crossover 必须实测。短答案、无可见 CoT 或严格低延迟时仍可共用简单预算。

**Books 比较：** Ch56 已让 scheduler 持有 reasoning budget、stopping 与 marginal value，却未明确 final-answer reserve 及共享 max-output 导致的 truncation coupling；该状态应进入 request admission 和 evaluation identity。

**最终处置：** 整合：`INFER-SCHEDULING`，[56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)；已存在 Books 正文。

### [Gradient Starvation in Binary-Reward GRPO: Why Group-Mean Centering Fails and Why the Simplest Fix Works](https://arxiv.org/html/2605.07689v1)

**采用命题：** binary reward 下，group-mean centering 在全对/全错组会把 advantage 清零，造成结构性 gradient starvation。

**机制与评价：** 论文证明真实退化率高于 i.i.d. Bernoulli 估计，并在 Qwen3.5-9B GSM8K 七种 seed 中比较 fixed-reference Sign advantage；一个 G=4 轨迹观察到 0.69 退化率。

**证据位置：** Method：§2–§3 theory/advantage formulations；Evaluation：§4–§5；Table 1–4；Figure 2；Limitations / non-proof：Limitations；§6。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** Ch33 在 group-relative advantage 定义后已直接写明 all-zero/all-one group 会令 advantage 近零，并把有效 sample ratio 作为诊断；fixed-reference Sign 是实验性 fallback，不改变现有主命题。

**Books 比较：** 现有正文已承载同一长期命题；保留本材料为受限证据，不重复追加。

**最终处置：** 已有覆盖：`TRAIN-GRPO`，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md)。

### [Future Validity is the Missing Statistic: From Impossibility to $Φ$-Estimation for Grammar-Faithful Speculative Decoding](https://arxiv.org/html/2605.07698v1)

**采用命题：** grammar local validity 不等于未来可完成性；speculative decoder 若只有局部 mask 会采到 projected law 而非 grammar-conditional law。

**机制与评价：** 论文以 future-validity Phi 构造 Doob transform，exact Phi 下 FVO-Spec 精确，近似 Phi 给出 TV bound；在 Dyck、finite JSON 等可计算 grammar 上评估。

**证据位置：** Method：§2–§5 future-validity/Doob transform/estimators；Evaluation：§6 Experiments；Table 1–5；Appendix G/H；Limitations / non-proof：§7 Discussion/Limitations。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 一般 CFG 的 exact Phi 为 #P-hard，OneStep 有 context-independence 误差；估计不可证时回退 local projection 并明确语义，或使用可枚举 grammar/普通 constrained decode。

**Books 比较：** 在 Ch48「Lossless Verification 是分布契约」之后、接受长度例子之前，加入 constrained generation 的 future-validity 条件。

**最终处置：** 整合：`INFER-SPECULATIVE-DECODING`，[48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md)；已存在 Books 正文。

### [Guidance Is Not a Hyperparameter: Learning Dynamic Control in Diffusion Language Models](https://arxiv.org/html/2605.07701v1)

**采用命题：** Diffusion language model 的 CFG scale 可以从固定超参数演进为读取当前 diffusion state 的逐步控制策略。

**机制与评价：** 作者把每步 guidance scale 作为离散 action，以 diffusion state 为 observation、task reward 为终局信号，用 PPO 学习 task-与阶段相关的 guidance trajectory，并与固定/启发式 scale 比较。

**证据位置：** Method：§3.1–3.3；§4.1–4.3；Evaluation：§5.1–5.4；Appendix B/C；Limitations / non-proof：§6 Limitations。Artifact：no public implementation artifact disclosed in exact-v1。

**未证明、代价与回退：** 实验只有三个受控 NLP 任务和特定 discrete diffusion model；learned policy 会随 task、reward、sampler 与 state encoding 漂移，terminal reward 也不证明逐步控制因果正确。失配时回退固定 CFG 或保守启发式 schedule。

**Books 比较：** Ch24 已把 source/coupling/schedule、conditional guidance 并行和 prior guidance 纳入 identity，但未表达 CFG strength 本身由 trajectory-conditioned policy 逐步拥有；该机制补足生成控制 owner。

**最终处置：** 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；已存在 Books 正文。

### [An Efficient Hybrid Sparse Attention with CPU-GPU Parallelism for Long-Context Inference](https://arxiv.org/html/2605.07719v1)

**采用命题：** CPU-resident sparse KV 需要把预算、head/granularity 选择与跨设备执行共同调度；稀疏率本身不能预测端到端收益。

**机制与评价：** Fluxion 组合 output-aware budget、head predictor、granularity selector 与 priority scheduler，在 2 模型、3 benchmark、40 tasks 上比较质量和 1.5x–3.7x speedup。

**证据位置：** Method：§4 Design Overview；Evaluation：§8 Evaluation；§8.3 ablation；Figures 2–6；Limitations / non-proof：§10 Conclusion；scope limited to disclosed CPU/GPU setups。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** Ch45 已明确 host 保留完整可寻址历史、GPU 维护 working set，并联合 selector、fetch、replacement、PCIe 与 fallback；Fluxion 的 budget/head/granularity selector 未改变该机制 owner。

**Books 比较：** 现有正文已承载同一长期命题；保留本材料为受限证据，不重复追加。

**最终处置：** 已有覆盖：`INFER-KV-CACHE`，[45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。

### [Coding Agents Don't Know When to Act](https://arxiv.org/html/2605.07769v1)

**采用命题：** Coding Agent 的 evaluation set 必须包含正确行为为 no-op 的负动作样本，并把 reproduce、act、abstain 与 partial-fix 分开计分。

**机制与评价：** FixedBench 从 SWE-bench Verified 构造 200 个已修复任务，期望 empty patch，并在五个模型、四种 harness 上测不当修改；reproduce-before-patch 提示降低 action bias，却在 partial-fix 场景引入过度 abstention。

**证据位置：** Method：§2.1–2.5；Evaluation：§3.1–3.3；Appendix C/D；Limitations / non-proof：§5 Limitations。Artifact：no dedicated public benchmark/code artifact disclosed in exact-v1。

**未证明、代价与回退：** 证据限 Python、热门仓库、所测 harness 与 patch 定义；no-op benchmark 不代表真实 issue triage，提示策略也会漏修部分修复。应以 paired action/no-action/partial-fix slices 与真实 regression outcome验收。

**Books 比较：** Ch66 有通用 abstention 和 outcome contract，但尚未要求将 no-op 成功、stale issue 与 partial-fix 对照纳入 Coding Agent evaluation identity；缺少这一 slice 会把无必要 patch 错计为积极行为。

**最终处置：** 整合：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已存在 Books 正文。

### [Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs](https://arxiv.org/html/2605.07806v1)

**采用命题：** 单一 verbalized confidence 不是充分 failure sensor；不同 self-assessment 维度必须按任务切片校准，并只作为选择性决策输入。

**机制与评价：** 论文同时采集 confidence 与 effort、understanding、ability、pleasantness、esteem、goal 等 appraisal，比较 12 个模型、38 个任务中的 failure discrimination、calibration 与 pre/post-task abstention；effort/ability 在部分任务更有效。

**证据位置：** Method：§2；Appendix C–H；Evaluation：§3.1–3.3；§4；Appendix I–N；Limitations / non-proof：Appendix A.1 Limitations。Artifact：no public implementation artifact disclosed in exact-v1。

**未证明、代价与回退：** 这些信号是功能性 self-report，不是 self-awareness 或 truth；任务多为可验证 benchmark，开放任务、人类基线和分布外校准有限。信号失配时回退外部 evidence、executable verifier 或人工。

**Books 比较：** Ch66 已把 black-box consistency、token probability、reflexive judge 与 claim-level score 视为观察不同误差面的 sensors，要求按 deployment slice 校准，并把 abstain/human escalation 交给风险策略；新增 appraisal 维度是已有多传感器原则的实例。

**最终处置：** 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [Unsafe by Flow: Uncovering Bidirectional Data-Flow Risks in MCP Ecosystem](https://arxiv.org/html/2605.07836v1)

**采用命题：** MCP 安全必须同时跟踪 requester→sensitive sink 与 external/internal data→MCP output 两个方向。

**机制与评价：** MCP-BiFlow 恢复 MCP entrypoint、定义协议 taint 并做 interprocedural analysis；作者审阅 32 个确认样例与 15,452 仓库。

**证据位置：** Method：§3 Design of MCP-BiFlow；§3.3；Evaluation：§4 Evaluation；§4.4 ablation；Limitations / non-proof：§5 Discussion；§7。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 其静态分析不覆盖 auth/business logic/tool-description poisoning 等未进入可分析 data flow 的风险；Ch83 已把跨 server bidirectional taint、effect-time authorization 与隔离 fallback 写为主线。

**Books 比较：** 现有正文已承载同一长期命题；保留本材料为受限证据，不重复追加。

**最终处置：** 已有覆盖：`AGENT-MCP`，[83-mcp.md](../../../../books/part-07-agent/83-mcp.md)。

### [AccelSync: Verifying Synchronization Coverage in Accelerator Pipeline Programs](https://arxiv.org/html/2605.07881v1)

**采用命题：** accelerator pipeline 的同步正确性必须按硬件可见性与 happens-before 验证，golden output/simulator 不足以覆盖 race。

**机制与评价：** AccelSync 将 DMA/vector/matrix/scalar pipeline 降为受限并发语言，以 program/sync/barrier order 判断 barrier sufficiency，并在 CANN kernels、生成 kernels 和 mutation 上评估。

**证据位置：** Method：§3.1–3.7；§4.1–4.5；Evaluation：§5.1–5.7；§5.9；Limitations / non-proof：§5.8；§5.10；§7。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** sound/complete 只相对参数化模型；驱动升级后一次现象不可复现，硬件模型缺项时应回退 sanitizer、stress test 与保守 barrier。

**Books 比较：** 在 Ch49「Kernel Verification 需要从孤立输入扩展到 Model–Kernel Interface」之后，作为并发可见性检查的下一层。

**最终处置：** 整合：`INFER-TENSORRT-LLM`，[49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；已存在 Books 正文。

### [TraceFix: Repairing Agent Coordination Protocols with TLA+ Counterexamples](https://arxiv.org/html/2605.07935v1)

**采用命题：** Multi-Agent 协议可先转成有限 topology/PlusCal，再用 model-checker counterexample 修复，运行时只允许已验证拓扑中的协调操作。

**机制与评价：** TraceFix 生成结构化 IR、PlusCal 与 TLC repair loop，再编译为 per-agent prompts；作者在 48 tasks、3,456 runs 和 fault injection 下比较。

**证据位置：** Method：§2 Method；§2.2 protocol design agent；Evaluation：§3 benchmark；§4 Evaluation；Limitations / non-proof：§6 Limitations and Scope；§7。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** Ch82 已将声明式协议、safety/liveness 检查、bounded topology repair、deterministic structural validation 与 runtime invariant 串成主线；TLA+/PlusCal repair loop 是既有主线的一个 artifact，不新增命题。

**Books 比较：** 现有正文已承载同一长期命题；保留本材料为受限证据，不重复追加。

**最终处置：** 已有覆盖：`AGENT-MULTI-AGENT`，[82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)。

### [Ask Early, Ask Late, Ask Right: When Does Clarification Timing Matter for Long-Horizon Agents?](https://arxiv.org/html/2605.07937v1)

**采用命题：** Clarification 不只是 ask/assume 二选一；缺失信息类型与已执行轨迹的不可逆程度共同决定提问时点。

**机制与评价：** 论文在 goal/input/constraint/context 四类缺失信息上，于轨迹 10/30/50/70/90% 强制注入 clarification，并用三套长程 Agent benchmark、84 variants、6,000+ runs 和 300 个自然会话估计 timing demand curve。

**证据位置：** Method：§3；§4.1–4.5；Evaluation：§5.1–5.4；Appendix A；Limitations / non-proof：§6 Limitations；Appendix A.7。Artifact：code/data promised but no exact public artifact locator disclosed in exact-v1。

**未证明、代价与回退：** forced injection 关闭自然询问且只测 demand side，样本、模型和 benchmark 有 floor/crossover；早问会增加打断和无必要澄清，晚问会浪费已提交工作。policy 不确定或 effect 不可逆时回退执行前硬门禁与人工确认。

**Books 比较：** Ch81 已把 clarification 写成每轮 admission gate，却未让缺失信息类型、trajectory commitment 和 rollback cost 进入 timing state；该增量应补在 ask/assume 之前。

**最终处置：** 整合：`AGENT-WORKFLOW`，[81-workflow.md](../../../../books/part-07-agent/81-workflow.md)；已存在 Books 正文。

### [Towards Apples to Apples for AI Evaluations: From Real-World Use Cases to Evaluation Scenarios](https://arxiv.org/html/2605.07986v1)

**采用命题：** Evaluation identity 必须从抽象 capability 名称落到具体用户、预期 outcome、正负影响、风险和 KPI 的运行场景。

**机制与评价：** 论文以 SME Use Case Worksheet 收集 sector/user/outcome/impact/KPI，再用 LLM 扩展和三阶段人工审阅形成 107 个金融服务场景，并以 rubric 检查 scenario quality 与 operational grounding。

**证据位置：** Method：§3；§4.1；Evaluation：§5.2 的 process demonstration 与 validation rubric；Limitations / non-proof：§5.3 Limitations。Artifact：no software/data artifact required or disclosed for the adopted methodological claim。

**未证明、代价与回退：** 示例限美国金融服务，LLM 扩展与人工 review 不证明场景完备、代表性或 KPI 因果有效；它是 scenario-construction 方法而非模型表现证据。缺少 domain SME 或可测 outcome 时应保留探索性评估。

**Books 比较：** Ch66 已要求 EvalSpec 冻结 workload/query distribution、intended decision、stage receipts、risk/critical slices、cost/SLO 与 artifact identity，并把 deployment outcome 与 self-report/probe 分开；该 worksheet 是现有 operational-grounding 命题的领域实例。

**最终处置：** 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [Position: Mechanistic Interpretability Must Disclose Identification Assumptions for Causal Claims](https://arxiv.org/html/2605.08012v1)

**采用命题：** Mechanistic interpretability 的 faithfulness、completeness、ablation 等 validation 指标不能替代 causal identification assumptions。

**机制与评价：** position paper 审计 10 篇、以双人 n=30 复核方向，提出声明 causal claim、identification strategy、assumptions、stress test 与 assumption-failure sensitivity。

**证据位置：** Method：§5 Audit Methodology；§5.3 decision rule；Evaluation：§6 Audit Results；Table 2–4；Limitations / non-proof：§9 Limitations and Alternative Views。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** purposive 小样本不能估计领域 prevalence，论文也未提供通用识别方法；无法识别时应降级为关联/干预描述而非 causal claim。

**Books 比较：** 在 Ch66「Attribution 是 Versioned Evaluation Contract」中，先于具体归因分数讨论，加入 causal identification disclosure gate。

**最终处置：** 整合：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已存在 Books 正文。

### [Learning CLI Agents with Structured Action Credit under Selective Observation](https://arxiv.org/html/2605.08013v1)

**采用命题：** CLI Agent 的 sequence reward 可拆为 turn-level action structure、workspace observation reveal 与 abstract-history credit。

**机制与评价：** A3 将 AST action comparison、sigma-Reveal context injection、episode normalization 与 tree-level history credit 合成 per-turn advantage，并在 sandboxed ShellOps/ShellOps-Pro 评测。

**证据位置：** Method：§3 Method；Appendix C；Evaluation：§4 Results；§4.2–4.5；Appendix F；Limitations / non-proof：§5 Limitations；§6 Conclusion。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** credit proxies 依赖 shell AST、gold effect 与受测 workspace schema；结构相似不等执行正确，不能授予 reward truth authority。

**Books 比较：** Ch33 已把 role/turn/tool/effect 作为 typed credit boundary，并要求 verifier/effect receipt 独立拥有结果；该算法不改变主线。

**最终处置：** 已有覆盖：`TRAIN-GRPO`，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md)。

### [STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation](https://arxiv.org/html/2605.08029v1)

**采用命题：** 统一多模态模型可让 causal VLM state 与 normalizing-flow visual state 在同一序列内交替耦合，而不是只在输出端串联两个模型。

**机制与评价：** STARFlow2 的 Pretzel architecture 以 shared causal mask、vertical crossing skip connections、deep/shallow TARFlow 和 staged training 联合生成、编辑、理解与 reasoning。

**证据位置：** Method：§3.1 Pretzel Architecture；§3.2 Deep-Shallow Flow；Evaluation：§4 Experimental Setup；§5.1–5.2；Limitations / non-proof：Appendix A Limitations and Future Work；§7 Conclusion。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 统一 NLL 与共享状态会增加 modality interference、训练阶段耦合和 flow/VLM version identity；benchmark 不证明所有任务共享同一 backbone 最优。

**Books 比较：** Ch24 已比较 AR、Diffusion、Flow 与 unified typed sequence，但尚缺 causal LM state 与 invertible flow state 的显式交错/版本边界。

**最终处置：** 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；已存在 Books 正文。

### [Beyond Pairs: Your Language Model is Secretly Optimizing a Preference Graph](https://arxiv.org/html/2605.08037v1)

**采用命题：** Preference objective 可从彼此独立的 pair 扩展为带 equivalence class、transitive dominance 与 global anchor 的 graph。

**机制与评价：** GraphDPO 把同一 prompt 的 K 个 rollouts 聚为等价类并构造 DAG，以 local Plackett-Luce loss 只比较严格支配边，随后聚合图损失更新 policy。

**证据位置：** Method：§4.2 Graph-Structured Preference Objective；§4.4；Evaluation：§5 Experiments；Table 1–2；Figure 2；Limitations / non-proof：Limitations/Discussion；§6 Conclusion。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 图关系由 reward/preference signal 构造，错误传递性会系统放大标签偏差；三 benchmark、三 seed 不证明任意开放偏好满足 DAG。

**Books 比较：** Ch34 已定义 pairwise DPO 与 dataset/reference identity，但尚未表达 group equivalence 与 transitive graph structure 对 objective identity 的改变。

**最终处置：** 整合：`TRAIN-DPO`，[34-dpo.md](../../../../books/part-04-training-system/34-dpo.md)；已存在 Books 正文。

### [Fast Byte Latent Transformer](https://arxiv.org/html/2605.08044v1)

**采用命题：** byte-level 表示的无词表优势会把生成成本推向每 byte 自回归；dynamic patch latent、block diffusion 与 full-model verification 可以重新分配这项成本。

**机制与评价：** BLT-D 由 entropy patcher 形成 variable-length byte patches，global model 预测 latent，decoder 对 fixed-size masked byte block 并行去噪；BLT-S/BLT-DV 再以 causal full-model verification 接受至首个 mismatch。

**证据位置：** Method：§2.1.1 Architecture Overview；§3.2.2；Evaluation：§4–§6；Figures 1–5；Algorithm 1；Limitations / non-proof：§7 Conclusion；正文未单列 limitations，按 generation/evaluation contract 收窄。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** greedy verification 的等价性不外推 sampling；patch boundary、fixed block、额外 re-encode 与 diffusion NFE 都进入 latency/quality contract。

**Books 比较：** Ch11 已说明 byte/token 计量与 checkpoint identity，Ch24/Ch48 分别拥有 block diffusion 与 verification；仍缺 tokenizer owner 对 dynamic patch 如何改变模型/runtime 接口的主叙述。

**最终处置：** 整合：`MODEL-TOKENIZER`，[11-tokenizer.md](../../../../books/part-02-model/11-tokenizer.md)；已存在 Books 正文。

### [The Memory Curse: How Expanded Recall Erodes Cooperative Intent in LLM Agents](https://arxiv.org/html/2605.08060v1)

**采用命题：** 更多历史不一定改善多 Agent 协作；必须把 context length 与历史中的 defect/cooperate content 分开测量。

**机制与评价：** 论文在四类 repeated social dilemmas 中扩展 history，比较 symmetric/asymmetric memory，并用 sanitization 把 78/80 rounds 替换为 cooperative records，隔离 content-vs-length。

**证据位置：** Method：§3 Experiment Design；Evaluation：§4.3；§4.5 sanitization；§4.6 ablation；Figure 5；Limitations / non-proof：§5 Conclusion；按受控社会博弈和相关性边界收窄。Artifact：not_required_for_adopted_claim; no implementation or reproduction claim adopted。

**未证明、代价与回退：** 结果是受控博弈和模型行为相关性，不能外推真实协作或把 forward-looking lexical ratio 当因果机制；sanitization 也可能删除必要负面证据。

**Books 比较：** Ch77 已覆盖检索/淘汰/reader failure，却未把 harmful historical content 与长度预算作为独立 intervention contract。

**最终处置：** 整合：`AGENT-MEMORY`，[77-memory.md](../../../../books/part-07-agent/77-memory.md)；已存在 Books 正文。

### [State Representation and Termination for Recursive Reasoning Systems](https://arxiv.org/html/2605.06690v1)

**采用命题：** 递归推理必须显式保存 epistemic state，并把 expand/consolidate order-gap 只当作局部停止诊断，而不是 truth 或全局收敛证明。

**机制与评价：** 论文把 claim、evidence relation、open question 与 confidence 组织成 epistemic state graph；比较 expand→consolidate 与 consolidate→expand 的状态距离，并给出线性化 order-gap 在 fixed point 邻域非退化的充要条件。Algorithm 1 与 Table 1 是算法/说明性轨迹，不是生产实验。

**证据位置：** Method：§2–§6；Algorithm 1 Recursive Reasoning with Order-Gap Termination；Evaluation：§7 application analysis；Table 1 为 expository trajectory；Limitations / non-proof：§5 local non-degeneracy theorem；§9 discussion；§10 Conclusion；无全局收敛证明。Artifact：not required for the adopted theoretical claim; exact-v1 discloses no immutable implementation artifact consumed by this review。

**未证明、代价与回退：** 条件只在 fixed point 邻域且针对线性化 gap；作者明确不声称全局收敛。图抽取与 confidence 可能错误，gap 小也可能是两个顺序共同遗漏；证据冲突、抽取不稳或高风险时回退固定预算、外部 verifier 与人工升级。

**Books 比较：** Ch80 已有“Reflection 的停止条件需要 Typed Epistemic State”，逐项保存 claim/evidence/conflict/unknown 与 order gap，并明确 local diagnostic、预算、hard cap、evidence gate 和人工回退；该 exact-v1 是现有正文所承载命题的原始受限证据。

**最终处置：** 已有覆盖：`AGENT-REFLECTION`，[80-reflection.md](../../../../books/part-07-agent/80-reflection.md)。


### [Same Signal, Opposite Meaning: Direction-Informed Adaptive Learning for LLM Agents](https://arxiv.org/html/2605.06908v1)

**采用命题：** test-time compute gate 必须区分 compute need 与 compute suitability；同一 uncertainty/difficulty signal 的效用方向会随 environment 与 backbone 反转。

**机制与评价：** DIAL 先用 base/rollout 的 counterfactual exploration 得到 utility difference，再从通用与任务特征中以稀疏 logistic gate 学习每个 environment/backbone 的方向。Table 1 显示跨六环境、三骨干的 signal–utility 方向不稳定；Table 2–3 与 ablation 检查成功率—成本及反向 gate 的退化。

**证据位置：** Method：§3 Problem Formulation；§4 DIAL；Evaluation：§5.1–§5.3；Table 1–3；Figure 1–3；Limitations / non-proof：§6 Limitations；§7 Conclusion；Appendix H Broader Impact。Artifact：no immutable implementation identity captured; no reproduction claim adopted。

**未证明、代价与回退：** 稀疏 gate 依赖探索数据、reward 与环境/骨干身份；关联方向不是因果机制，错误方向会专门选择有害状态。冷启动、分布漂移或高风险请求回退固定预算、独立 verifier 或保守不追加 compute。

**Books 比较：** Ch56 已有 reasoning budget、solvability、marginal value 与 monitor calibration，但仍把 gate signal 主要写成单调可校准输入；没有保存“同一 signal 在不同 environment/backbone 上方向反转”的 gate-direction identity。

**最终处置：** 整合：`INFER-SCHEDULING`，[56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)；Books 正文与独立终审均通过。


### [A$^2$RD: Agentic Autoregressive Diffusion for Long Video Consistency](https://arxiv.org/html/2605.06924v1)

**采用命题：** 长视频 segment generation 应从 open-loop chaining 演进为读取持久 multimodal memory、选择生成模式并在提交前分层修正的闭环。

**机制与评价：** A2RD 对每个 segment 执行 Retrieve–Synthesize–Refine–Update：MVMem 跟踪跨模态进展，adaptive generator 在 extrapolation/interpolation 间切换，frame/video 两级 self-improvement 抑制误差传播；VBench-Long、LVBench-C 与人工评价覆盖一到十分钟视频。

**证据位置：** Method：§3–§4；§3.1 MVMem Design；Appendix E prompts；Evaluation：§5.1–§6；Table 2–5；Figure 1–4；人工评价；Limitations / non-proof：§7 Conclusions；Limitations；Appendix B.2 methodology analysis。Artifact：supplementary videos are referenced, but no immutable artifact identity was captured; no reproduction claim adopted。

**未证明、代价与回退：** 证据绑定 Veo 3.1、作者 prompt/workflow 与 benchmark；self-refinement 共享 generator/judge 偏差，memory/mode switch 会引入 drift、额外调用和错误累积。边界状态或 evaluator 不可靠时回退短 segment、固定 mode、人工 storyboard 或重新生成。

**Books 比较：** Ch24 已有视频 temporal state、segment commit 与 plan→draft→inspect→refine 的通用分支，但未把跨 segment multimodal memory、mode switch、双层 refine/update 组合成可恢复的长视频闭环状态。

**最终处置：** 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；Books 正文与独立终审均通过。


### [The Cost of Consensus: Malignant Epistemic Herding and Adaptive Gating in Distributed Multi-Agent Search](https://arxiv.org/html/2605.06988v1)

**采用命题：** Multi-Agent communication 评价必须把 consensus 与 alignment-to-truth 分开；低分歧可能是 confident-but-wrong herding。

**机制与评价：** 论文把 agent belief 写成分布状态，联合操纵消息频率与内容，比较持续广播、定期通信与 uncertainty-gated protocols；JSD/rate-to-consensus 与 alignment-to-truth 分开报告，失败 episode 中持续通信可低 JSD 地共同错误。

**证据位置：** Method：§3 System Model；§3.2 Agent Architecture；§4 metrics/design；Evaluation：§4.6；§5；Figure 2–4；Appendix A；Limitations / non-proof：§6 Discussion；§6.5 Limitations；§7 Conclusion。Artifact：not required for the adopted mechanism; no immutable simulator artifact captured。

**未证明、代价与回退：** grid-world、Bayesian fusion、同步执行和已知 truth 不外推开放 Agent；truth alignment 在生产往往不可观测，通信延迟/丢包又改变结果。拿不到独立 truth 时保留 dissent、provenance 与独立 verifier，不能用 consensus 自证正确。

**Books 比较：** Ch82 已警告 correlated hallucination、同源报告和 voting 不能构成独立证据，但尚未把 communication frequency/content、collective belief state 与 truth-alignment/JSD 双指标绑定成 protocol-level evaluation identity。

**最终处置：** 整合：`AGENT-MULTI-AGENT`，[82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)；Books 正文与独立终审均通过。


### [The Context Gathering Decision Process: A POMDP Framework for Agentic Search](https://arxiv.org/html/2605.07042v1)

**采用命题：** agentic search 应以持久 predicate-based belief state 拥有已知/未知与未解条件，并用 programmatic exhaustion gate 终止空转。

**机制与评价：** CGDP 把超大隐藏环境中的 context gathering 建模为 POMDP，并以 approximate Thompson Sampling 解释行为；PBAI loop 将隐式 search 拆成 predicate operations，PBBS 注入 belief state，exhaustion detector 读取程序信号。三域四种 harness 的实验分别检查准确率恢复与 token 节省。

**证据位置：** Method：§3 Framework；§4 Abstract Algorithm；Algorithm 1；Evaluation：§6–§6.2；Table 2–4；Appendix D/F/G；Limitations / non-proof：§7 Discussion and Conclusion；Limitations and Future Work。Artifact：no immutable implementation identity captured; no reproduction claim adopted。

**未证明、代价与回退：** belief extractor 与 predicate schema 会遗漏证据；exhaustion 只检测所建模的停滞，不证明任务已解。状态不完整、开放搜索或高风险时扩大检索、保留 hard budget，并向人工暴露 unresolved predicates。

**Books 比较：** Ch75 已有 Active Information Foraging 的显式 epistemic state、遗漏风险与停止原因，但尚缺把 predicate closure 与 programmatic exhaustion 分离、并要求 gate 不把‘无新结果’解释为‘任务已完成’。

**最终处置：** 整合：`AGENT-CONTEXT`，[75-context.md](../../../../books/part-07-agent/75-context.md)；Books 正文与独立终审均通过。


### [WiCER: Wiki-memory Compile, Evaluate, Refine Iterative Knowledge Compilation for LLM Wiki Systems](https://arxiv.org/html/2605.07068v1)

**采用命题：** 持久 wiki-memory 的编译必须以 probe 驱动的 counterexample/refinement 检查事实丢失，不能把压缩率或 TTFT 当完整性证明。

**机制与评价：** WiCER 在 17 RepLiQA domains/6,800 questions 上先测 full-context、RAG 与 blind compilation，再以 diagnostic probes 定位 dropped facts，迭代 pinning/refine；ablation 显示 targeted diagnosis 而非 generic pinning 贡献恢复。

**证据位置：** Method：§3 setup/config/evaluation；§7.1 Algorithm 1；§7.2；Evaluation：§5–§6；Table 1–5；Limitations / non-proof：§7.4 Analysis and Limitations；§8 Discussion and Conclusion。Artifact：exact-v1 says code/benchmarks are released, but no immutable artifact revision was captured; no reproduction claim adopted。

**未证明、代价与回退：** probe coverage 决定能发现哪些丢失，LLM judge 与 curated knowledge 限制外推；attention dilution 和编译误差并未消失。关键事实、来源更新或 probe 不足时回退原文 retrieval/full context。

**Books 比较：** Ch77 已规定 memory write 必须由 non-writing distillation 产出 candidate、用只读 counterexample/precondition/freshness probes 验证，再由唯一 writer commit；也保留 source revision、compiler/judge 与 retrieval fallback。WiCER 是该合同的 wiki 编译实例。

**最终处置：** 已有覆盖：`AGENT-MEMORY`，[77-memory.md](../../../../books/part-07-agent/77-memory.md)。


### [TeamBench: Evaluating Agent Coordination under Enforced Role Separation](https://arxiv.org/html/2605.07073v1)

**采用命题：** Multi-Agent evaluation 必须用 enforcement 区分角色声明与真实 capability separation，并把 team pass、越权尝试和 verifier false accept 分开。

**机制与评价：** TeamBench 以 OS sandbox 分离 Planner 的 spec access、Executor 的 workspace edit 与 Verifier 的 final attestation；851 templates/931 instances 比较 Solo、prompt-only、sandbox-enforced 与 role ablations，并用 deterministic grader 审计 verifier。相近 pass rate 下，prompt-only 越权编辑更多，verifier 仍大量 false accept。

**证据位置：** Method：§2 benchmark/roles；§2.3 Ablation Conditions；Appendix F.2；Evaluation：§3.1–§3.7；Table 1；Figure 1–5；human study；Limitations / non-proof：§4 Discussion；§5 Conclusion；H2 step-limit exhaustion。Artifact：no immutable benchmark release identity captured; no reproduction claim adopted。

**未证明、代价与回退：** benchmark 的文件权限与 deterministic grader 不覆盖真实网络、credentials、隐式 side effects；强分权增加 coordination/missing-information cost，团队在易任务还可能劣于单 Agent。隔离或 verifier 不可靠时回退 single owner、最小权限与人工 certification。

**Books 比较：** Ch82 已有 role/topology/version、verifier 与 commit owner，但未要求 evaluation 以 OS-enforced capability separation 验证 prompt role，也未把 team success 与 unauthorized attempt/false accept 分列。

**最终处置：** 整合：`AGENT-MULTI-AGENT`，[82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)；Books 正文与独立终审均通过。


### [Learning Visual Feature-Based World Models via Residual Latent Action](https://arxiv.org/html/2605.07079v1)

**采用命题：** feature-space World Model 应把可预测 residual transition 压成 latent action，并用 action-conditioned outcome 而非视觉清晰度验证其可规划性。

**机制与评价：** RLA 从 DINO residual 学 compact latent action，RLA-WM 以 flow matching 预测 residual，再用于 actionless-video imitation 与 offline-video world-model RL；future-frame、latent-action 与 policy success 分层评价。

**证据位置：** Method：§3 Method；Evaluation：§4–§4.1；Table 1–2；Figure 1–4；Limitations / non-proof：§5 Limitations and Conclusion；Appendix A.3。Artifact：project page disclosed in abstract; no immutable code/model revision captured; no reproduction claim adopted。

**未证明、代价与回退：** DINO residual/flow metric 不等于物理真值，offline world rollout 仍受 support gap 与 hallucination；真实 controller 拥有 action commit。表示或 action support 越界时回退 pixel/structured simulator 或真实短 horizon observation。

**Books 比较：** Ch25 已明确 feature/latent prediction 的 encoder identity、representation collapse、action-conditioned outcome 与 closed-loop task gate，并要求 unsupported action 回退高保真 simulator/真实 observation；RLA 是现有 residual latent branch 的具体实现。

**最终处置：** 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。


### [Securing Computer-Use Agents: A Unified Architecture-Lifecycle Framework for Deployment-Grounded Reliability](https://arxiv.org/html/2605.07110v1)

**采用命题：** Computer-Use Agent 安全应沿 perception/decision/execution 与 creation/deployment/operation/maintenance 的交叉面定位 authority-bearing failure。

**机制与评价：** 该综述把 software interaction 写成 partially observable control，建立 architecture–lifecycle coordinate system，并映射 capability formation、permission binding、runtime trajectory 与 maintenance drift 的威胁/控制面；OpenClaw 只是公开例子。

**证据位置：** Method：§II Problem Definition and Design Axes；§III Analytical Framework；Evaluation：§VI Security and Privacy Analysis；§VIII-C；Limitations / non-proof：§VI-A–§VI-D threat scope；综述性非实证边界。Artifact：not required for the adopted survey framework; no implementation claim adopted。

**未证明、代价与回退：** 这是分析框架，不提供系统实证或 OpenClaw 内部验证；分类不能证明控制充分。生产仍需 effect-time authorization、trace/evidence、sandbox 与人工 gate。

**Books 比较：** Ch72 已按 input/context/model/tool/memory/output 与 build/deploy/runtime/maintenance 串联 threat、authority、preventive/evidential gate，且明确 benchmark success 不等于 release readiness；该综述不改变现有安全 owner。

**最终处置：** 已有覆盖：`PLATFORM-SECURITY`，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。


### [Switchcraft: AI Model Router for Agentic Tool Calling](https://arxiv.org/html/2605.07112v1)

**采用命题：** tool-calling model router 应在 correctness hard condition 下选择最低总成本模型，并把 token-intensive reasoning、router latency 与 function-call structure 纳入成本。

**机制与评价：** Switchcraft 用五个 function-calling benchmarks、AST scorer 与 model outputs 训练 DistilBERT router；held-out 12,282 examples 比较 accuracy/cost Pareto、latency、robustness 与 token packing。

**证据位置：** Method：§3 Design；Appendix B/E.1；Evaluation：§4–§4.6；Table 1–3；Figure 1–3；Limitations / non-proof：§5 Limitations；§7 Conclusions；Appendix J.4。Artifact：no immutable router/checkpoint artifact captured; no reproduction claim adopted。

**未证明、代价与回退：** 训练 label 继承 scorer/model pool 偏差，price 与 tool schema 会漂移；成本最优不授权具体 tool effect。分布外、高风险或 classifier 不确定时回退已认证大模型、deterministic tool gate 或人工。

**Books 比较：** Ch78 已把 tool necessity、catalog/routing、benefit-latency-failure-risk 与 preventive/evidential execution gates 分离；router 只提议模型/工具，correctness 与 effect authority 仍独立。该成本分类器不新增 owner。

**最终处置：** 已有覆盖：`AGENT-TOOL-CALLING`，[78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)。


### [Learning Agent Routing From Early Experience](https://arxiv.org/html/2605.07180v1)

**采用命题：** LLM→Agent escalation router 可用少量 early paired experience 建立能力边界，但经验 memory 只提供 routing evidence，不拥有任务结果。

**机制与评价：** BoundaryRouter 在 seed set 上同时执行 direct LLM 与 full Agent，构建 compact experience memory，检索相似案例并用 rubric-guided reasoning 路由；RouteBench 覆盖 in-domain、paraphrase、OOD 与 solver-balanced F1/accuracy/time。

**证据位置：** Method：§3 BoundaryRouter；Appendix A.3；Evaluation：§4–§5；Table 1；Figure 1–5；Limitations / non-proof：§6 Discussion and Conclusion；按 cold-start/benchmark/model 范围收窄。Artifact：no immutable implementation identity captured; no reproduction claim adopted。

**未证明、代价与回退：** early experience 会稀疏、过期并受 benchmark label/rubric 偏差影响；相似任务不保证同一最优 solver。冷启动或高风险时回退静态能力表、全 Agent 或人工 escalation。

**Books 比较：** Ch84 已把 capability routing、paired marginal-utility gate、task/skill compatibility、versioned outcome ledger 与静态 fallback 写入 Agent platform；该 early-memory router 是现有 admission 分支。

**最终处置：** 已有覆盖：`AGENT-PLATFORM`，[84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)。


### [Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions](https://arxiv.org/html/2605.07271v1)

**采用命题：** layer pruning 的质量崩塌应按 decision representation transition 诊断；hidden representation 仍相似不代表模型仍能进入 Decisive phase。

**机制与评价：** 论文用 iterative pruning 追踪 zero-shot accuracy、CKA、decision representation similarity 与 layer-wise Decision Margin；在 Llama3-8B、Llama2-7B、Qwen3-4B 上观察 Silent/Decisive phase 与 pruning cliff，并用噪声敏感性分析结构脆弱性。

**证据位置：** Method：§3 Method；Appendix A.3；Evaluation：§4–§4.3；Figure 1–6；Appendix A.1；Limitations / non-proof：§5 Conclusion；Appendix A.12 Limitations and Future Work。Artifact：no immutable implementation identity captured; no reproduction claim adopted。

**未证明、代价与回退：** Decision Margin 绑定多选任务、选项 logit 与作者模型，不是所有生成任务的通用因果解释；iterative pruning 是分析 probe。指标失配或开放生成时回退任务级评测、activation/gradient probes 与保守少剪枝。

**Books 比较：** Ch17 解释 attention/MLP/residual 的层职责，却未表达 pruning 会保留表面 feature similarity 但截断深层 decision transition，也没有 Silent/Decisive phase 的结构性验收。

**最终处置：** 整合：`MODEL-TRANSFORMER-LAYER`，[17-transformer-layer.md](../../../../books/part-02-model/17-transformer-layer.md)；Books 正文与独立终审均通过。


### [Sword: Style-Robust World Models as Simulators via Dynamic Latent Bootstrapping for VLA Policy Post-Training](https://arxiv.org/html/2605.07288v1)

**采用命题：** 用 World Model 作为 VLA simulator 时，style perturbation 与 long-horizon error accumulation 必须作为独立可靠性切片，并保持训练/推理 latent-state 一致。

**机制与评价：** Sword 用 structure-guided style augmentation 解耦视觉 texture 与 task dynamics，以 Dynamic Latent Bootstrapping 维持 rollout state并控制 memory；LIBERO 上比较 OOD style、prediction fidelity、long horizon 与 RL post-training success。

**证据位置：** Method：§3–§3.3；training objective；Evaluation：§4–§5.2；Figure 1–4；Table 1–2；Limitations / non-proof：§6 Conclusion and Limitations。Artifact：no immutable implementation identity captured; no reproduction claim adopted。

**未证明、代价与回退：** style augmentation 不覆盖动力学/接触 OOD，bootstrapping 会自举错误；simulator success 不证明 sim-to-real。状态/动作 support 越界时回退真实 observation、显式 simulator 或短 horizon replanning。

**Books 比较：** Ch25 已要求 observed/latent/imagined state 分离、style/visual plausibility 不能替代 action consequence、long-horizon calibration 与 closed-loop outcome，并定义 simulator/support fallback；Sword 未改变该合同。

**最终处置：** 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。


### [Rethinking Importance Sampling in LLM Policy Optimization: A Cumulative Token Perspective](https://arxiv.org/html/2605.07331v1)

**采用命题：** LLM policy optimization 的 IS ratio 可以对 prefix action likelihood 累乘，但必须用 position-adaptive clipping 控制随序列长度增长的 log-ratio 方差。

**机制与评价：** CTPO 以 cumulative token IS ratio 对齐当前 token 所在 prefix state，理论比较 token/sequence/cumulative ratio 的 bias–variance；固定 clip 下越后位置越易截断，故按 sqrt(position) 调节 log-space threshold。数学 tool-use benchmark、Figure 1 与 Table 2–3 检查位置 clip rate和结果。

**证据位置：** Method：§2 setup；§3 cumulative ratio/position-adaptive clipping；Evaluation：§3.2–§4.2；Table 1–3；Figure 1–2；Limitations / non-proof：§5 analysis；§6 Conclusion；无独立 Limitations 标题，按模型/任务/长度范围收窄。Artifact：no immutable implementation identity captured; no reproduction claim adopted。

**未证明、代价与回退：** 累积 ratio 的方差随长度放大，approximation 与 clipping schedule 依赖 policy lag、长度和任务；作者未证明其对任意长文本或异步 rollout 稳定。估计爆炸、off-policy gap 大或短序列时回退 token-level PPO、sequence ratio 或更频繁同步。

**Books 比较：** Ch32 定义 token prefix state 与 clipped ratio，Ch33 比较 token/sequence ratio granularity，但没有把 cumulative prefix ratio 与 position-adaptive clip 作为同一 bias–variance branch。

**最终处置：** 整合：`TRAIN-PPO`，[32-ppo.md](../../../../books/part-04-training-system/32-ppo.md)；Books 正文与独立终审均通过。


### [Unsolvability Ceiling in Multi-LLM Routing: An Empirical Study of Evaluation Artifacts](https://arxiv.org/html/2605.07395v1)

**采用命题：** multi-LLM router 的 oracle/unsolvability ceiling 必须先去除 judge misalignment、truncation 与 format artifact，否则错误标签会训练出 routing collapse。

**机制与评价：** 论文将 routing ceiling 分成 genuine evaluator disagreement 与共同 measurement failures；在 MMLU、MedQA、ShareGPT 和 Gemma tiers 上用 exact match/重判分、context overflow 与 formatting decomposition 修正 solvable labels，并显示 judge-derived oracle 分布会偏向小模型。

**证据位置：** Method：§2 routing ceiling；§3.3 Evaluation Framework and Artifact Decomposition；Evaluation：§3 setup；§4–§8；Table 3–7；Limitations / non-proof：§9 Discussion；§9.4 Limitations；§11 Conclusion。Artifact：no immutable implementation identity captured; no reproduction claim adopted。

**未证明、代价与回退：** 证据限特定 Gemma tiers、datasets、judge 和 4,096 context；exact match 也只适合结构化答案。无法取得可靠 adjudication 时应保留 Unknown、扩大 context/解析校验，不能用伪 oracle 训练 router。

**Books 比较：** Ch66 已有 judge bias、truncation、format/schema 与 observed/elicitation ceiling，但尚未明确这些 artifact 会污染 multi-model router 的 oracle labels，并把评估错误固化为 routing policy。

**最终处置：** 整合：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Books 正文与独立终审均通过。


### [GameGen-Verifier: Parallel Keypoint-Based Verification for LLM-Generated Games via Runtime State Injection](https://arxiv.org/html/2605.07442v1)

**采用命题：** 长程交互程序的验证应把 specification 分解为 keypoints，以 runtime state injection 到达目标状态，再执行有界 interaction 并返回 falsifying witness。

**机制与评价：** GameGen-Verifier 将 game spec ground 成 state/interaction/expected-outcome units，白盒 patch runtime 后并行执行；GGV-Harness 提供 isolation、concurrency、fault recovery，VeriGame 100 games 上与 human judgment/AaaV 对比。

**证据位置：** Method：§3–§4 GameGen-Verifier/GGV-Harness；Figure 3；Evaluation：§5–§5.2；Table 1–2；Limitations / non-proof：§6 Limitations；§7 Conclusion；Broader Impact。Artifact：no immutable harness/dataset revision captured; no reproduction claim adopted。

**未证明、代价与回退：** state injection 可能绕过真实 reachability，keypoint extraction/judge 会漏掉组合规则；只证明独立断言不等于完整游戏正确。无法白盒注入或关键状态耦合时回退真实 gameplay、property tests 与人工。

**Books 比较：** Ch66 已规定 EvalSpec 要分解可执行断言、用独立 environment/effect state 验证、保留 reachability/coverage 与 falsifying evidence，且 no-op/outcome 不由 Agent 自证；该 game harness 是现有 contract 的领域实例。

**最终处置：** 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。


### [RcLLM: Accelerating Generative Recommendation via Beyond-Prefix KV Caching](https://arxiv.org/html/2605.07443v1)

**采用命题：** 非连续知识复用需要把 prefix cache 扩展为有身份的 reusable block，并联合 tiered residency、locality placement 与 selective-attention correction。

**机制与评价：** RcLLM 将 system/context 与 item KV 分池，分析 item cache 规模，以 similarity-aware placement 建立全局副本并配合选择性 attention；evaluation 覆盖推荐准确率、延迟/吞吐、cache pool 与 placement ablation。

**证据位置：** Method：§III System Design；§III-A–§III-D；Algorithm 1；Evaluation：§IV–§IV-D；Table I–III；Limitations / non-proof：§V discussion；§VI Conclusion；无独立 Limitations 标题，按 workload/model/implementation 收窄。Artifact：no immutable implementation identity captured; no reproduction claim adopted。

**未证明、代价与回退：** 结果绑定推荐 workload、Qwen3-8B 与作者实现；相似 item 不保证 position/conditioning 等价，分层搬运、选择 miss 与 correction 都可能返还收益。identity 或 repair 不成立时回退完整 prefix prefill/FullKV。

**Books 比较：** Ch45 当前已完整拥有 exact prefix identity、immutable blocks、CPU/SSD tier、prefix-tree locality/prefetch、document/chunk packet、任意位置 position-conditioning seam repair 与 selective recompute；RcLLM 的组合不再增加长期命题。

**最终处置：** 已有覆盖：`INFER-KV-CACHE`，[45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。


### [VNN-LIB 2.0: Rigorous Foundations for Neural Network Verification](https://arxiv.org/html/2605.07451v1)

**采用命题：** verification query 标准必须把 syntax、types 与 model semantics 分开版本化，不能把不断变化的外部 ONNX 语义当作隐式真值。

**机制与评价：** VNN-LIB 2.0 定义 abstract network theory、查询 syntax/type system/formal semantics，并用 Agda mechanization 检查内部一致；Figures 1–6 给出 declaration 与 semantics 结构。

**证据位置：** Method：§2–§9 formal foundations；Figure 1–6；Evaluation：formal mechanization consistency only; exact-v1 has no empirical evaluation section；Limitations / non-proof：§10 Conclusion；network-theory instantiation/ONNX semantics boundary。Artifact：Agda mechanization is stated, but no immutable artifact revision captured; no proof-reproduction claim adopted。

**未证明、代价与回退：** 形式化只相对 network theory 与实例化 model-format semantics；不证明任意 ONNX exporter/solver/浮点 kernel正确，也没有 benchmark。实例化不完整时回退固定版本 translator、solver cross-check 与 concrete execution。

**Books 比较：** Ch66 已要求 evaluation/spec schema、artifact/backend/version 与 deterministic semantics 共同冻结，并区分形式 verifier 与真实 runtime outcome；VNN-LIB 2.0 是该 versioned interface 原则的专用标准。

**最终处置：** 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。


### [DIMoE-Adapters: Dynamic Expert Evolution for Continual Learning in Vision-Language Models](https://arxiv.org/html/2605.07494v1)

**采用命题：** continual VLM adapter 应把固定专家池拆成可演化 sparse pool，并分离 train-time expert evolution 与 inference-time prototype selection。

**机制与评价：** DIMoE-Adapters 为新任务增加 task router/experts 并冻结旧分支；SCEE 依据动态指标扩展/更新 expert pool，PGES 以 task prototypes 决定进入 adapter 或 frozen CLIP zero-shot path。MTIL/few-shot、cost 与 module ablation 检查 transfer、average/last score。

**证据位置：** Method：§3 Methodology；Figure 1–2；Evaluation：§4–§4.3；Table 1–4；DIMoE/SCEE analysis；Limitations / non-proof：§5 Conclusion；正文未单列 limitations，按 continual-VLM/benchmark 范围收窄。Artifact：no immutable implementation identity captured; no reproduction claim adopted。

**未证明、代价与回退：** pool 会持续增长，prototype drift/错误 task ID 会误路由，冻结旧专家也不保证消除遗忘；证据限 CLIP/VLM 与 MTIL。预算或识别失败时回退固定 adapter、共享 LoRA、rehearsal 或 frozen base。

**Books 比较：** Ch30 有 adapter routing、rank/组合/冲突与持续更新边界，但没有把 expert pool lifecycle 与 prototype-based selection 拆成两个 owner/state。

**最终处置：** 整合：`TRAIN-LORA`，[30-lora.md](../../../../books/part-04-training-system/30-lora.md)；Books 正文与独立终审均通过。


### [Is the Future Compatible? Diagnosing Dynamic Consistency in World Action Models](https://arxiv.org/html/2605.07514v1)

**采用命题：** World Action Model 的 imagined future 必须评估 action–state dynamic consistency，并防止静态 background collapse 伪造高一致性。

**机制与评价：** 论文跨 joint-prediction/inverse-dynamics models 比较 consistency 与 rollout success/value，定位低 dynamics failure 的 background collapse，并用 candidate-future consensus 做 value-free test-time selection；RoboCasa/RoboTwin 2.0 分任务评价。

**证据位置：** Method：§3–§4 dynamic consistency；Appendix E；Evaluation：§5–§5.2；Figure 1–6；Appendix C；Limitations / non-proof：§6 Conclusion and Future Work；Appendix H Limitations and Failure Analysis。Artifact：no immutable implementation identity captured; no reproduction claim adopted。

**未证明、代价与回退：** consistency 是相关 signal，不是可达性或安全真值；多个候选共享 model bias 时 consensus 仍会共同错误。低 dynamics、contact-critical 或 OOD action 时回退 value/physics verifier、真实 observation 与短 horizon planning。

**Books 比较：** Ch26 已要求 VLA imagined rollout 同时验证 action consequence、state transition、closed-loop outcome 与真实 controller authority，并把 visual plausibility/latent similarity 降为 sensor；Ch25 又明确 background/latent collapse 与 simulator fallback。该一致性指标不新增 owner。

**最终处置：** 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[26-multimodal-embodied-vla.md](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。


### [Deadline-Driven Hierarchical Agentic Resource Sharing for AI Services and RAN Functions in AI-RAN](https://arxiv.org/html/2605.07547v1)

**采用命题：** deadline workload 的资源控制应分离慢时标 placement 与快时标 allocation，并让 migration critic 比较中断成本与 SLO 收益。

**机制与评价：** HAF 以 LLM agent 做 epoch-level AI/RAN placement，以 closed-form deadline-aware convex algorithm 做 event-level GPU/CPU allocation，再由 predictive critic 过滤不划算 migration；simulation 做 load sweep、critic ablation 与 SLO/migration 对比。

**证据位置：** Method：§II System Model；§III Hierarchical Agentic Framework；Evaluation：§IV；Table I–III；Figure 1–2；critic ablation/load sweep；Limitations / non-proof：§V Conclusion；正文未单列 limitations，按 simulation/AI-RAN/LLM-critic 范围收窄。Artifact：no immutable implementation identity captured; no reproduction claim adopted。

**未证明、代价与回退：** 结果来自 AI-RAN simulation，LLM placement 与 critic 预测会漂移；平均 SLO 不证明硬实时安全。预测不稳、迁移不可恢复或关键 RAN deadline 时回退静态 placement、保守 reservation 与 hard deadline policy。

**Books 比较：** Ch56 已分层 offline/profiled templates 与 online allocation，联合 placement/capacity/deadline/migration cost，并要求 predictor 只提议、hard SLO/policy 保留 authority；HAF 是该 slow/fast controller 的领域实现。

**最终处置：** 已有覆盖：`INFER-SCHEDULING`，[56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。


### [HexiSeq: Accommodating Long Context Training of LLMs over Heterogeneous Hardware](https://arxiv.org/html/2605.07569v1)

**采用命题：** 异构长上下文训练的 CP/HP plan 应按 GPU compute、memory 与 network 共同生成 fully asymmetric partition，而不是强制同构 mesh。

**机制与评价：** HexiSeq 以 hierarchical scheduler 先决定跨设备 context/head ownership，再生成不对称 exchange；在混合 GPU testbeds 的 3B/7B/13B 与 simulation 的 70B 上对比 throughput，并做长 context、heterogeneity 与 scheduler analysis。

**证据位置：** Method：§2 formulation；§3 System Design and Implementation；Appendix B；Evaluation：§5–§5.1；Figure 1–5；Limitations / non-proof：§6 Conclusion；Appendix D Limitations。Artifact：no immutable implementation identity captured; no reproduction claim adopted。

**未证明、代价与回退：** 收益依赖 profile、模型 shape、拓扑与计划一致提交；simulation 不是生产 70B 证明，不对称 plan 增加建图/缓冲/同步与 straggler 风险。profile 过期或成员无法一致提交时回退规则 Ulysses/同构 CP。

**Books 比较：** Ch36 已有 topology-aware fully-connected exchange plan，但当前命题更具体：partition 本身需同时消费异构 compute、memory、network，并允许 CP/HP 维度完全不对称，而非只重排通信图。

**最终处置：** 整合：`TRAIN-DISTRIBUTED-TRAINING`，[36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)；Books 正文与独立终审均通过。


### [Safe, or Simply Incapable? Rethinking Safety Evaluation for Phone-Use Agents](https://arxiv.org/html/2605.07630v1)

**采用命题：** phone-use Agent safety 必须把 harmless outcome 分成 safe action、unsafe action 与 inability-to-act；不行动造成的无害不能计作安全。

**机制与评价：** PhoneSafety 从真实 Android 轨迹抽取 700 个 safety-critical moments，提供 protocol-grounded safe/unsafe references，并把 outcome 分解为 Safe-action、Unsafe-action 与 CFR；700 cases、130+ apps、多模型/agent 和 protocol ablation 比较能力、安全与行动能力。

**证据位置：** Method：§2.1 Evaluation Unit；§2.4 PhoneSafety；§2.6 setup；Evaluation：§3–§3.5；Figure 1–3；Table 1–3；Limitations / non-proof：§4 Conclusion；Appendix H Limitations；Appendix J。Artifact：no immutable dataset release identity captured; no reproduction claim adopted。

**未证明、代价与回退：** reference protocol、app state 与辅助 classifier 可能误标；真实设备覆盖仍有限，safe reference 不证明长期 outcome。低行动能力模型可能虚高 harmlessness，高风险发布需 effect receipt、人工 adjudication 与任务完成率共同验收。

**Books 比较：** Ch66 有 outcome/abstention/no-op 与 safety slice，但尚未把 phone Agent 的 unsafe、safe、irrelevant/no useful action 三分并明确 harmlessness false positive。

**最终处置：** 整合：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Books 正文与独立终审均通过。


### [Tracing Uncertainty in Language Model "Reasoning"](https://arxiv.org/html/2605.07776v1)

**采用命题：** reasoning failure sensor 应读取整条 uncertainty trace 的阶段、斜率与形态，而不是只用终局 confidence。

**机制与评价：** 作者在 GSM8K/ProntoQA、五模型上抽取 distributional/consistency/epistemic uncertainty 的 early/mid/late mean、slope 与 fit quality，用 LR/GB 分类正确/错误，并逐步增加可见轨迹比例测试 early detection；另定位首错附近的轨迹变化。

**证据位置：** Method：§3 Methods；§3.2 Experimental Procedure；Evaluation：§4–§4.3；Figure 1–5；Table 1；Appendix D；Limitations / non-proof：§5 Discussion；Limitations and future work；§6 Conclusion。Artifact：no immutable implementation identity captured; no reproduction claim adopted。

**未证明、代价与回退：** uncertainty feature 是相关 sensor，不是首错因果或 truth；需要 token probabilities/多采样，跨模型/任务校准会漂移。访问受限或 AUROC 不稳时回退终局 verifier、外部 evidence 与保守 abstain。

**Books 比较：** Ch66 已有多 uncertainty sensor 与 deployment-slice calibration，却未把 trace 当 evolving state、按 early/mid/late profile 验证早期 failure sensing。

**最终处置：** 整合：`PLATFORM-EVALUATION-SYSTEM`，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Books 正文与独立终审均通过。


### [MatryoshkaLoRA: Learning Accurate Hierarchical Low-Rank Representations for LLM Fine-Tuning](https://arxiv.org/html/2605.07850v1)

**采用命题：** 动态 LoRA rank 可由同一 adapter 的 nested sub-ranks 提供，但训练和验收必须覆盖整个 rank curve，而非只优化最大 rank。

**机制与评价：** MatryoshkaLoRA 构造共享 ordered low-rank factors，使前 k 个方向形成可独立使用的 sub-adapter，并给出兼容既有 LoRA 方法的多 rank objective；AURAC 汇总 rank–accuracy curve。GSM8K、ARC-C、HellaSwag 与 scaling ablation 检查各 rank。

**证据位置：** Method：§2–§2.3.3；Algorithm 1；Appendix B；Evaluation：§2.5；§3–§3.4；Table 1–3；Limitations / non-proof：§4 Conclusion, Limitations and Broader Impact。Artifact：no immutable implementation identity captured; no reproduction claim adopted。

**未证明、代价与回退：** sub-rank ordering与任务相关，低 rank 可能退化，AURAC 会掩盖关键 operating point；证据限 Llama 与所测任务。固定预算/单部署 rank 时普通 LoRA 更简单，关键 rank 仍需单点 gate。

**Books 比较：** Ch30 已有 rank budgeting、adapter identity 与组合冲突，但没有把单个 adapter 训练成 nested sub-ranks，也未定义跨 rank curve 的 AURAC 验收。

**最终处置：** 整合：`TRAIN-LORA`，[30-lora.md](../../../../books/part-04-training-system/30-lora.md)；Books 正文与独立终审均通过。


### [Trajectory as the Teacher: Few-Step Discrete Flow Matching via Energy-Navigated Distillation](https://arxiv.org/html/2605.07924v1)

**采用命题：** few-step discrete flow distillation 的瓶颈可能在 teacher trajectory target；training-only energy navigator 可在 midpoint 候选中选择较可信路径。

**机制与评价：** TS-DFM 在小步距直接使用 frozen teacher，大步距用 RK-4 semi-teacher 构造候选，并以 energy compass 在 t≥tau 时选择 midpoint；主结果覆盖不同 source distributions/NFE，Table 2 检查 tau 与 diversity，Table 3 报训练开销。

**证据位置：** Method：§3 background；§4 Method: navigation shaping；Appendix A/C.5；Evaluation：§5–§5.2；Table 1–3；Figure 1–3；Appendix E；Limitations / non-proof：§6 Conclusion；无独立 Limitations 标题，按 teacher/energy/diversity/NFE 范围收窄。Artifact：no immutable implementation identity captured; no reproduction claim adopted。

**未证明、代价与回退：** energy 只在训练中评价候选且可能偏向低熵路径；更早启用可降低 perplexity却损失 diversity，teacher/energy bias 会传给 student。指标或分布漂移时回退普通 DFM trajectory、更多 sampling steps 或统一 distillation。

**Books 比较：** Ch24 已讨论 teacher trajectory、off-trajectory state 与 temporal-aware distillation，但没有 training-only midpoint energy selection 以及 quality–diversity/tau 的控制边界。

**最终处置：** 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；Books 正文与独立终审均通过。


### [How to Train Your Latent Diffusion Language Model Jointly With the Latent Space](https://arxiv.org/html/2605.07933v1)

**采用命题：** latent diffusion language model 联合训练 encoder、diffusion 与 decoder 时需要 staged warmup/noise/objective contract，避免表示与生成共同 collapse。

**机制与评价：** LDLM 以 frozen token encoder、trainable latent encoder/diffusion/latent decoder/token decoder联合目标训练；实验比较 decoder losses、diffusion-to-encoder warmup、decoder noise 与 time sampling，并在 OWT/LM1B 等测 generation perplexity、entropy 与 NFE。

**证据位置：** Method：§4–§4.3；Appendix A/A.1；Evaluation：§6；§8；Figure 1–5；Table 1；Appendix B/D；Limitations / non-proof：§9 Conclusion；Appendix G Limitations。Artifact：no immutable implementation identity captured; no reproduction claim adopted。

**未证明、代价与回退：** 联合目标增加 reconstruction、smoothness、diffusion 与 decoder 的耦合；warmup/noise 失配会 collapse，PPL/entropy 不等于语义事实或 serving SLO。训练不稳时回退 staged freeze、离散 diffusion 或 AR。

**Books 比较：** Ch24 已有 text VAE→latent diffusion→decoder factorization 与各阶段 failure，但没有说明端到端 joint objective 的 warmup/noise 如何防止 latent/decoder 共塌缩。

**最终处置：** 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；Books 正文与独立终审均通过。


### [Rubric-Grounded RL: Structured Judge Rewards for Generalizable Reasoning](https://arxiv.org/html/2605.08061v1)

**采用命题：** GRPO reward 可由 policy 不可见的 grounding passage 与 weighted rubric 生成 criterion-level credit，但 judge 只能拥有受限评分，不能拥有事实或发布 authority。

**机制与评价：** Rubric-Grounded RL 离线从技术文档合成 question/grounding/weighted-rubric，在线 policy 只见 question；冻结 judge 读取隐藏 grounding 和 rubric，输出 criterion scores 聚合为 normalized reward供 GRPO。held-out rubric reward、reasoning transfer 与 reward dynamics 是评价边界。

**证据位置：** Method：§3 Method；Judge Prompt Architecture；Training Objective；Appendix A；Evaluation：§4–§5；Table 1–2；Figure 1–3；Algorithm 1；Limitations / non-proof：§6 Discussion；§7 Limitations；§8 Conclusion。Artifact：no immutable corpus/code identity captured; no reproduction claim adopted。

**未证明、代价与回退：** 同一 judge 参与训练与主评价会产生 shared-bias/overoptimization，合成 rubric/weight 可能错误，hidden passage 不代表开放世界真值；证据限作者 8B policy、GPT-OSS judge 与语料。高风险或 judge 漂移时回退 executable verifier、人工 rubric、outcome-only reward 或保留 Unknown。

**Books 比较：** Ch33 已分离 reward/verifier 与 policy，并讨论 token/step credit；但尚未定义 policy-invisible grounding、weighted criteria、criterion-level scores 与 judge authority 的接口。

**最终处置：** 整合：`TRAIN-GRPO`，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md)；Books 正文与独立终审均通过。


## 5. 缺口与下一步

1. screening denominator 已按有界 28 项返修并冻结：`826 = 102 retained + 533 direct closure + 191 owner-day isolation`；没有重开 11 个 DataCite isolation control，也没有扩窗/扩源。
2. 102/102 retained 已有 exact-v1 Evidence Review 与 Books comparison；本轮无材料 blocker。
3. Books 当前为 42 Integrate / 58 No Change / 2 仅报告；42 个 Integrate 已写回并通过 marker、owner、placement 与语义终审，Books pending 为 0。
4. 来源表中的动态历史目录限制是本窗终态保留项：不支持正面证据、Books 或无遗漏断言，也不支持性能/安全保证；定点重开条件是取得相应官方日级归档，届时只重开受影响的来源槽位，不重跑已冻结的 arXiv 分母。
5. 后续事件日 owner 继续分别处理 `2605.06738`、`2605.06772`、`2605.07210`、`2605.07527`、`2605.07818`、`2605.08051` 的官方后续修订信号；它们不计作 2026-05-11 的新 revision event，也不阻断本窗终态。

## 6. 复核

复核者：`/root/may12_fresh_postwrite`（fresh non-author final reviewer；未参与本日作者返修或 root Books 写回）

结论：通过

28 项 screening repair 的准入/反例边界、102/102 exact-v1 Evidence、16 个新正文与 26 个既有 Integrate binding 均通过终审。16 个新正文真实包含旧路径、约束变化、机制与 state/control ownership、trade-off、failure/fallback、证据边界和相邻段衔接；42 个 Integrate marker 均唯一并位于 owner 主 `## Review notes` 前。完整记录见 [fresh non-author final Gate](../_sources/daily-20260511/V3_FRESH_NONAUTHOR_FINAL_GATE_REVIEW_102_20260915.md)。

机器校验只能证明 JSON、评分、分母算术、版本 basis 引用、唯一 owner、链接字段与 Markdown 结构一致；不能替代独立语义复核。

**Repository Changes：** 本轮 fresh review 仅更新 2026-05-11 Daily、active ledger/Evidence/queue、审计记录与学习 checkpoint；未修改 Books，未 stage、commit 或 push。
