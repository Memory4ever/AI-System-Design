# Daily Research — 2026-05-27

**规范：** V3

**窗口：** 2026-05-26T09:00:00+08:00 ～ 2026-05-27T09:00:00+08:00

**状态：** 完成

**Books：** 纳入本次

**检查时间：** 2026-09-16T13:56:31+08:00

## 1. 结论

旧 V2.1 的 `633 raw / 64 retained`、DataCite-created owner、评分、Evidence、Books disposition 与 `Complete` 均不继承。05-27 的 arXiv first-public owner 是 2026-05-26 20:00 ET（北京时间 05-27 08:00）的 official announcement batch；全类别连续区间为 `2605.24798..2605.26116`，注册类别投影为 691。MiniMax 技术页的 JSON-LD `datePublished=2026-05-27T00:00:00Z` 另增 1 个独立机构 identity，因此总分母冻结为 **692 = 94 retained + 598 pre-denominator closure + 0 withdrawn**。旧 633 个 arXiv identity 与本集合交集为 0，全部落在下一公告区间。

94 项均完成 exact-v1/官方技术页深入审阅，Evidence 为 **94 deep + 0 standard + 0 blocked**，评分分布为 `22 score7 + 62 score8 + 10 score9`。本轮逐项清除了摘要背景句式采用命题，并把 48 个旧 No Change 全量重审；MiniMax 事件复用当前唯一 Ch29 binding。Fresh 反例挑战恢复 `2605.26099`，并在 closure 中追加恢复 `2605.26089` 与 `2605.26097`；Books 投影现为 **61 Applied + 33 No Change + 0 pending Integrate**。三项均已由 root 串行写入 canonical owner；`2605.25333` 为现有覆盖。Fresh non-author 已完成路径、语义绑定、账目与状态终审，本日报闭环。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | official Research index/RSS; adjacent explicit research date 05-20, no window technical event | 已检查 | no positive no-hit claim beyond dated index |
| SRC-ANTHROPIC | official Research index; nearest explicit research date 05-22 | 已检查 | date-only pages are not promoted without a time inside this window |
| SRC-GOOGLE-AI | DeepMind Research/Publications; adjacent explicit dates 05-20 and 05-28 | 已检查 | year-only cards do not prove site-wide no-hit |
| SRC-META-AI | official Publications entry | 受阻 | empty/internal-error behavior; not used for a positive no-hit |
| SRC-QWEN | official article index; adjacent explicit dates 05-20 and 05-29 | 已检查 | none |
| SRC-DEEPSEEK | official Research/News; adjacent explicit dates 04-24 and 06-24 | 已检查 | none |
| SRC-MOONSHOT | official Kimi Platform Blog; research/release/RFC slice only | 已检查 | no window event found on the dated index |
| SRC-TENCENT-HUNYUAN | official Research publicList and linked primary artifacts | 已检查 | visible dated records outside window |
| SRC-ZAI | official Research/release index; adjacent explicit dates 05-20 and 06-16 | 已检查 | none |
| SRC-BYTEDANCE-SEED | official Research/Public Papers; adjacent explicit dates 05-16 and 05-29 | 已检查 | none |
| SRC-BAIDU-ERNIE | official technical Blog; latest explicit pre-window date 05-09 | 已检查 | none |
| SRC-XIAOMI-MIMO | official dated paper/blog cards | 受阻 | undated cards cannot support a day-level no-hit |
| SRC-MINIMAX | official Research/Blog JSON-LD datePublished=2026-05-27T00:00:00Z (05-27 08:00 BJT) | 已检查 | 1 technical research event retained; URL slug/human-readable date not used as owner |
| SRC-ARXIV | official 05-26 20:00 ET announcement; contiguous sequence projected to registered categories | 已检查 | 691 arXiv raw = 93 retained + 598 closure |

完整 owner 证据见 [`official-owner-batch-evidence-v3.json`](../_sources/daily-20260527/official-owner-batch-evidence-v3.json)，14-source 记录见 [`source-coverage-v3.json`](../_sources/daily-20260527/source-coverage-v3.json)，692 条逐项题摘/机构页判定与 family-specific closure 见 [`screening-outcomes-v3.json`](../_sources/daily-20260527/screening-outcomes-v3.json)。Meta 与 MiMo 的入口限制被隔离，不用于正面 no-hit；普通 commit/PR 未扩入 denominator。MiniMax 页在旧 05-26 报告中的 `00:30 BJT` owner 没有 JSON-LD 支持，不能重复计数；该跨日报告元数据由其 owner 另行纠正。Fresh 终审在冻结分母内又重开 `2605.26089` 与 `2605.26097`，没有扩窗或扩源。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [2605.24817 RouteScan: A Non-Intrusive Approach to Auditing MoE LLMs Safety via Expert Routing Telemetry](https://arxiv.org/html/2605.24817v1) | 2026-05-27T08:00:00+08:00 | Inspired by this observation, we propose RouteScan, a non-intrusive auditing framework for detecting harmful behaviors through such routing-induced GPU telemetry.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md)：PLATFORM-MONITORING |
| [2605.24818 Spiking the training data to correct for test set contamination](https://arxiv.org/html/2605.24818v1) | 2026-05-27T08:00:00+08:00 | 在已知比例主动注入 benchmark 样本并拟合 contamination-response curve，把污染校正从事后猜测变成带干预记录的 evaluation protocol。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.24823 Agent Manufacturing: Foundation-Model Agents as First-Class Industrial Entities](https://arxiv.org/html/2605.24823v1) | 2026-05-27T08:00:00+08:00 | 把 Agent Manufacturing 操作化为由 foundation-model agents 承担开放目标解释、长程规划、工具/机器调用及人机协商的生产协调机制，并与封闭协议空间中的传统 multi-agent manufacturing 区分。；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/84-agent-platform.md)：AGENT-PLATFORM |
| [2605.24832 Optimus: Elastic Decoding for Efficient Diffusion LLM Serving](https://arxiv.org/html/2605.24832v1) | 2026-05-27T08:00:00+08:00 | We present Optimus, a serving system that enables elastic decoding for diffusion LLMs by dynamically adapting decoding granularity to runtime load.；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)：INFER-TENSORRT-LLM |
| [2605.24870 Trajectory-Consistent Calibration for Cache-Accelerated Diffusion Models](https://arxiv.org/html/2605.24870v1) | 2026-05-27T08:00:00+08:00 | 把 diffusion cache 的误差从单点 representation mismatch 扩展为会被先前校准继续改写的 trajectory state，并沿 corrected history 逐步拟合 site-local calibration prior。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)：MULTIMODAL-GENERATIVE-PARADIGMS |
| [2605.24879 Efficient DP-SGD for LLMs with Randomized Clipping](https://arxiv.org/html/2605.24879v1) | 2026-05-27T08:00:00+08:00 | 用 Hutchinson/Hutch++ 随机 trace estimation 近似 per-sample gradient norm，把 DP clipping 的显存复杂度从显式 T×T 或 d×d 中间量改为受投影维度控制的 estimator，并为随机 clipping 单独建立 privacy accountant。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.24883 Inverting the Shield: Systematically Generating Safety Tests from Policy Specifications](https://arxiv.org/html/2605.24883v1) | 2026-05-27T08:00:00+08:00 | 把自然语言 safety policy 编译为形式化谓词和语义图，再从未覆盖路径生成可追踪测试，使 policy revision、test identity 与 coverage evidence 成为同一评估对象。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.24892 X-Foresight: A Joint Vision-Action Causal Forecasting Network via Predictive World Modeling](https://arxiv.org/html/2605.24892v1) | 2026-05-27T08:00:00+08:00 | 把低熵相邻帧预测改成跨语义时间块的自回归 future-state 预测：块内保留稠密瞬时动态、块间保留稀疏长程因果，并把 action/latent prediction 与多视角 renderer 分责。；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：MULTIMODAL-WORLD-MODELS |
| [2605.24914 MVR-cache: Optimizing Semantic Caching via Multi-Vector Retrieval and Learned Prompt Segmentation](https://arxiv.org/html/2605.24914v1) | 2026-05-27T08:00:00+08:00 | 以可学习 prompt segmentation 生成多向量表示，再用 MaxSim 做细粒度匹配；训练目标直接约束在 correctness 前提下增加 cache hit，并以强化学习求解不可微组合优化。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)：INFER-KV-CACHE |
| [2605.24922 MuJoCoUni:Persistent Batched Runtime Primitives for MuJoCo](https://arxiv.org/html/2605.24922v1) | 2026-05-27T08:00:00+08:00 | 把 stateless rollout 调用提升为 executor-owned persistent environment pool，使 per-environment model/data、reset、step 与 Jacobian state 在 batched robot-learning loop 中保持可寻址。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：MULTIMODAL-EMBODIED-VLA |
| [2605.24930 H$^{2}$MT: Semantic Hierarchy-Aware Hierarchical Memory Transformer](https://arxiv.org/html/2605.24930v1) | 2026-05-27T08:00:00+08:00 | 先把长文档组织成语义树，再用层级 memory tokens 与 query-aware routing 在粗摘要和细粒度节点间分配注意力预算。；2+2+3=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-02-model/22-long-context.md)：MODEL-LONG-CONTEXT |
| [2605.24941 Memory-Induced Tool-Drift in LLM Agents](https://arxiv.org/html/2605.24941v1) | 2026-05-27T08:00:00+08:00 | 长期记忆中的成本、耐心或风险偏好即使与当前任务无关，也会通过隐式 steering 与关键词注意力重分配改变 tool arguments；相关性提示和 memory filter 只能缓解，不能消除这种 memory-induced tool drift。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/78-tool-calling.md)：AGENT-TOOL-CALLING |
| [2605.24973 MinerU-Popo: Universal Post-Processing Model for Structured Document Parsing](https://arxiv.org/html/2605.24973v1) | 2026-05-27T08:00:00+08:00 | 在 page OCR 之后增加 document-level state owner，跨页合并段落/表格并同步 chunk 与结构索引，使 ingestion 输出可被 RAG 以同一 document revision 消费。；2+2+3=7 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/76-rag.md)：AGENT-RAG |
| [2605.25002 MemMark: State-Evolution Attribution Watermarking for Agent Long-Term Memory Systems](https://arxiv.org/html/2605.25002v1) | 2026-05-27T08:00:00+08:00 | We propose MemMark, a state-evolution attribution watermark that embeds an owner-controlled signal into latent memory-write decisions.；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/77-memory.md)：AGENT-MEMORY |
| [2605.25052 Faithfulness Metrics Don't Measure Faithfulness: A Meta-Evaluation with Ground Truth](https://arxiv.org/html/2605.25052v1) | 2026-05-27T08:00:00+08:00 | 先构造能暴露真实中间计算的任务并生成 step/CoT 级 ground-truth faithfulness label，再审计现有指标；多数指标接近随机、对长 CoT 退化且跨设置不迁移，因此自动分数不能未经有效性验收就充当 faithfulness 证据。；3+3+3=9 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.25073 Security in the Fine-Tuning Lifecycle of Large Language Models: Threats, Defenses,Evaluation, and Future Directions](https://arxiv.org/html/2605.25073v1) | 2026-05-27T08:00:00+08:00 | 把 fine-tuning attack surface 按 pre-tuning input/supply chain、during-tuning optimizer/update 与 post-tuning adapter/artifact 三个 intervention phase 组织，并用同一基座和协议检查跨 phase 防御组合。；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.25077 WorldCraft: From Camera Navigation to Object Manipulation in Interactive Video World Models](https://arxiv.org/html/2605.25077v1) | 2026-05-27T08:00:00+08:00 | 用 camera-invariant Normalized World Trajectory 分离对象运动与相机位移，以 Spatial-Pathway LoRA 注入对象控制，并用 trajectory-anchored persistent state 在对象离屏后保留更新位置。；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：MULTIMODAL-WORLD-MODELS |
| [2605.25085 Polynomial Context-Truncation Sensitivity in Autoregressive Language Models: Sequential Wyner-Ziv Bounds for KV Cache Compression](https://arxiv.org/html/2605.25085v1) | 2026-05-27T08:00:00+08:00 | We study the rate-distortion limits of online KV cache compression in autoregressive language models, formulating it as sequential Wyner-Ziv source coding on the filtration induced by the model, with the next-step query as decoder side information.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)：INFER-KV-CACHE |
| [2605.25092 AgentIR: A Workload-Adaptive Cascade Retrieval Substrate for Long-Term Conversational Memory](https://arxiv.org/html/2605.25092v1) | 2026-05-27T08:00:00+08:00 | 以 BM25 top-k margin 驱动无需重训的 cascade，逐 query 决定是否运行 dense channel/何种 fusion，并用 time-partitioned index 把增长中的长期记忆检索成本与 corpus size 解耦。；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/77-memory.md)：AGENT-MEMORY |
| [2605.25133 Trust but Verify: Prover-Verifier Deliberation for Selective LLM Prediction](https://arxiv.org/html/2605.25133v1) | 2026-05-27T08:00:00+08:00 | We introduce prover-verifier deliberation (PVD), an inference-time protocol grounded in interactive proof theory, as a mechanism for selective prediction: the protocol produces both an answer and a structured confidence verdict, allowing a system to report high-confidence answers while abstaining on uncertain cases.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.25160 SimuWoB: Simulating Real-World Mobile Apps for Fast and Faithful GUI Agent Benchmarking](https://arxiv.org/html/2605.25160v1) | 2026-05-27T08:00:00+08:00 | 由 coding agent 合成可执行 mobile-app simulator，再独立生成 task 与 state validator，把 GUI agent benchmark 的 environment 和 outcome evidence 版本化。；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.25188 DarkForest: Less Talk, Higher Accuracy for Multi-Agent LLMs](https://arxiv.org/html/2605.25188v1) | 2026-05-27T08:00:00+08:00 | 先保持 agents 独立生成，再把响应解析为候选簇，以 reliability、confidence、parse quality、support pattern 与独立性修正形成 belief distribution；coordinator 只接收 policy 允许的结构化证据而非原始推理串。；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/82-multi-agent.md)：AGENT-MULTI-AGENT |
| [2605.25189 Directional Alignment Mitigates Reward Hacking in Reinforcement Learning for Language Models](https://arxiv.org/html/2605.25189v1) | 2026-05-27T08:00:00+08:00 | We study this failure mode through the geometry of reinforcement learning updates in language models and argue that hacking emerges when optimization drifts away from a stable low-dimensional learning trajectory.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/31-rlhf.md)：TRAIN-RLHF |
| [2605.25233 Meta-Agent: From Task Descriptions to Verified Multi-Agent Systems](https://arxiv.org/html/2605.25233v1) | 2026-05-27T08:00:00+08:00 | 把自然语言任务编译为带显式 I/O contract 与 verifier 的 agent DAG；construction-time gate 定点重生失败 artifact，execution-time gate 再以 local/upstream/structural attribution 选择 retry、局部重放或重分解。；3+3+3=9 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/81-workflow.md)：AGENT-WORKFLOW |
| [2605.25240 JudgmentBench: Comparing Rubric and Preference Evaluation for Quality Assessment](https://arxiv.org/html/2605.25240v1) | 2026-05-27T08:00:00+08:00 | 把 rubric score 与 pairwise preference 作为不同 measurement operators，在同一受控质量阶梯上比较各自一致性与区分力，而不是默认二者可互换。；2+2+3=7 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.25244 Inference Time Optimization with Confidence Dynamics](https://arxiv.org/html/2605.25244v1) | 2026-05-27T08:00:00+08:00 | 正确 reasoning trajectory 的 confidence 往往沿程上升、错误轨迹则停滞或下降；CDG voting 把这种轨迹增益作为 answer-selection sensor，但它仍需与模型、任务和采样合同共同校准。；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-02-model/20-sampling.md)：MODEL-SAMPLING |
| [2605.25247 Kavier: Exploring Performance, Sustainability, and Efficiency of LLM Ecosystems under Inference through Cache-Aware Discrete-Event Simulation](https://arxiv.org/html/2605.25247v1) | 2026-05-27T08:00:00+08:00 | 先建立 LLM inference ecosystem 的 reference architecture，再用 cache-aware discrete-event simulator 联合表示 KV/prefix cache、性能、成本与可持续性，并以真实 traces 校准后用于比较配置。；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md)：INFER-SCHEDULING |
| [2605.25252 Quantifying Empirical Compute-Supervision Tradeoffs in RLVR](https://arxiv.org/html/2605.25252v1) | 2026-05-27T08:00:00+08:00 | 在受控 false-positive/false-negative verifier noise 与 rollout 数量下，额外 compute 呈锐减回报且不能消除监督差距；false negative 的损害更快，说明 verifier quality 与训练 compute 不能互换。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/31-rlhf.md)：TRAIN-RLHF |
| [2605.25272 AI Cartography: Mapping the Latent Landscape of AI Benchmark Ecosystems](https://arxiv.org/html/2605.25272v1) | 2026-05-27T08:00:00+08:00 | 用 latent measurement model 分解 benchmark 共同因子与 task-specific variance，使 release evidence 能区分能力构念、数据生态和 leaderboard 聚合造成的相关性。；2+2+3=7 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.25284 Knowing but Not Showing: LLMs Recognize Ambiguity but Rarely Ask Clarifying Questions](https://arxiv.org/html/2605.25284v1) | 2026-05-27T08:00:00+08:00 | 模型在显式判断时常能识别歧义，却在普通 QA 中仍直接作答；检索上下文提高 answerability 的同时进一步降低澄清概率，因此 ambiguity recognition 与 ask/answer 行为必须分开评估。；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/79-planning.md)：AGENT-PLANNING |
| [2605.25292 DECICE: AI-Driven Scheduling and Digital Twin Integration for the Cloud-HPC-Edge Compute Continuum](https://arxiv.org/html/2605.25292v1) | 2026-05-27T08:00:00+08:00 | 让 scheduler 消费由 Digital Twin 维护的 node power/carbon/anomaly state，并把 heterogeneous workflow 先转成正式 dependency/resource model，再输出 Kubernetes/Slurm placement。；2+2+3=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)：PLATFORM-GPU-SCHEDULER |
| [2605.25298 Beyond Thread States: Diagnosing Performance Degradation with eBPF and Thread Dynamics](https://arxiv.org/html/2605.25298v1) | 2026-05-27T08:00:00+08:00 | 从 thread-state 时间占比继续下钻到带 backing-resource identity 的 futex/pipe/socket/VFS/block-I/O dependency graph，并从 request entry thread 反向追踪 contention propagation。；2+2+3=7 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md)：PLATFORM-MONITORING |
| [2605.25313 UWM-JEPA: Predictive World Models That Imagine in Belief Space](https://arxiv.org/html/2605.25313v1) | 2026-05-27T08:00:00+08:00 | 用 joint system-environment density-matrix latent 与 unitary predictor 在 blind rollout 中保持表示的不确定性谱；同时证明 action sensitivity 依赖 counterfactual target，而不能由 teacher-forced context capacity 推出。；3+3+3=9 | 深入完成 | 已有覆盖 [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：MULTIMODAL-WORLD-MODELS |
| [2605.25333 Teaching Video Generators to Remember: Eliciting Dynamic Memory for Out-of-Sight State Evolution](https://arxiv.org/html/2605.25333v1) | 2026-05-27T08:00:00+08:00 | 流式视频 KV cache 只有在条目保留原始时间/相机 identity，且训练显式暴露局部观测失效到历史可靠锚点的非局部恢复边时，才会从容量缓冲演进为动态状态记忆；仅扩大 cache 不会自动学会选择可靠历史。；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：MULTIMODAL-WORLD-MODELS |
| [2605.25338 CausalFlow: Causal Attribution and Counterfactual Repair for LLM Agent Failures](https://arxiv.org/html/2605.25338v1) | 2026-05-27T08:00:00+08:00 | We introduce CausalFlow, an interventional framework that converts failed agent traces into minimal counterfactual repairs and reusable supervision.；2+2+3=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/84-agent-platform.md)：AGENT-PLATFORM |
| [2605.25375 Bandwidth-Aware and Cost-Efficient Pipeline Parallel Scheduling in Geo-Distributed LLM Training](https://arxiv.org/html/2605.25375v1) | 2026-05-27T08:00:00+08:00 | 以动态 job priority、bandwidth-aware cross-region pathfinder 与按电价分配 GPU 的 allocator 联合控制 geo-distributed pipeline training，避免 HoL blocking 并把 JCT、链路约束和电力成本纳入同一计划。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/38-pipeline-parallel.md)：TRAIN-PIPELINE-PARALLEL |
| [2605.25376 KYA: A Framework-Agnostic Trust Layer for Autonomous Systems with Verifiable Provenance and Hierarchical Policy Composition](https://arxiv.org/html/2605.25376v1) | 2026-05-27T08:00:00+08:00 | KYA (Know Your Agents) is an open-source, framework-agnostic trust and governance layer for autonomous systems, composed of five primitives: (1) a four-gate inbound apply pipeline; (2) an only-tighten composition algebra over a three-channel multi-tenant hierarchy; (3) KYP (Know Your Principal), a schema-level unification of trust scoring across human users, AI agents, and service accounts; (4) auditable interaction-multiplier amplification over an AIVSS-shaped additive baseline; and (5) two-axis delegation attribution: a static premium for risky delegates and a runtime debit for actual delegate misbehavior in multi-agent fan-out.；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.25379 StateRAG: Typed State Contracts for Complex Retrieval-Augmented Generation](https://arxiv.org/html/2605.25379v1) | 2026-05-27T08:00:00+08:00 | We introduce StateRAG, which represents retrieval control as a typed state external to the final reader.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/76-rag.md)：AGENT-RAG |
| [2605.25389 Evo-Attacker: Memory-Augmented Reinforcement Learning for Long-Horizon Tool Attacks on LLM-MAS](https://arxiv.org/html/2605.25389v1) | 2026-05-27T08:00:00+08:00 | 把长程 tool attack 建模为带动态 attack memory 的强化学习过程，并用 Attack-Flow GRPO 从 terminal outcome 向中间干预分配 credit；它暴露的是 tool-output trust surface，不授权把攻击策略当通用能力。；2+2+3=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.25421 HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol](https://arxiv.org/html/2605.25421v1) | 2026-05-27T08:00:00+08:00 | 用 latent channel 承载高带宽认知状态、用短文本承载关键可解释信号，并通过单 agent hybrid generation 与多 agent interactive co-training 学习多轮双向混合通信。；2+2+3=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/82-multi-agent.md)：AGENT-MULTI-AGENT |
| [2605.25422 A Token/KV-Cache Communication Media Selection and Resource Allocation Strategy for Multi-Agent Collaboration](https://arxiv.org/html/2605.25422v1) | 2026-05-27T08:00:00+08:00 | 把 token/KV-cache communication medium 与 wireless bandwidth allocation 联合优化；没有一种 medium 在所有 compute/channel regime 都占优，media identity 与资源状态必须共同进入 E2E latency 决策。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/82-multi-agent.md)：AGENT-MULTI-AGENT |
| [2605.25424 SeqRoute: Global Budget-Aware Sequential LLM Routing via Offline Reinforcement Learning](https://arxiv.org/html/2605.25424v1) | 2026-05-27T08:00:00+08:00 | We introduce SeqRoute, a framework that formulates multi-turn routing as a finite-horizon Markov Decision Process and solves it via offline reinforcement learning.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md)：INFER-SCHEDULING |
| [2605.25430 CODESKILL: Learning Self-Evolving Skills for Coding Agents](https://arxiv.org/html/2605.25430v1) | 2026-05-27T08:00:00+08:00 | 把 trajectory→skill extraction、evolution 与 compaction 从固定 prompt 提升为带 verifier reward 的可学习 lifecycle policy。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/84-agent-platform.md)：AGENT-PLATFORM |
| [2605.25451 BigMac: Breaking the Pareto Frontier of Compute and Memory in Multimodal LLM Training](https://arxiv.org/html/2605.25451v1) | 2026-05-27T08:00:00+08:00 | 把 multimodal encoder 与 generator 以 dependency-safe nested pipeline 嵌入 LLM pipeline，使二者 activation memory 为 O(1)，同时避免用降低计算利用率来换显存。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/38-pipeline-parallel.md)：TRAIN-PIPELINE-PARALLEL |
| [2605.25475 IndexMem: Learned KV-Cache Eviction with Latent Memory for Long-Context LLM Inference](https://arxiv.org/html/2605.25475v1) | 2026-05-27T08:00:00+08:00 | 用 learnable indexer 预测 KV importance，同时把被逐出的 token 压入在线更新的 latent memory 并提供 residual readout，从而把 bounded KV residency 与不可逆遗忘分开。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)：INFER-KV-CACHE |
| [2605.25492 SafetyRepro: Configuration-Conditional Rank Instability on Alignment Benchmarks](https://arxiv.org/html/2605.25492v1) | 2026-05-27T08:00:00+08:00 | Pairwise model comparisons drawn from foundation-model benchmarks ("A is safer than B") are read as quantitative verdicts but hinge on harness choices benchmark papers under-specify.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.25507 Credit Assignment with Resets in Language Model Reasoning](https://arxiv.org/html/2605.25507v1) | 2026-05-27T08:00:00+08:00 | 从整条 trajectory 共用 outcome reward 演进到 intermediate-state reset 与 counterfactual suffix 的局部 credit assignment。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/32-ppo.md)：TRAIN-PPO |
| [2605.25521 CS-PQ: Cache-Friendly SIMD Product Quantization for Large-Scale ANNS Index Construction](https://arxiv.org/html/2605.25521v1) | 2026-05-27T08:00:00+08:00 | 沿 PQ centroids 而非 subvector dimension 做 SIMD vectorization，并重排 pipeline 提升 cache locality、消除冗余计算，使 CPU index construction 的数据移动与计算粒度共同受控。；2+2+3=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/76-rag.md)：AGENT-RAG |
| [2605.25522 Co-Designing Graph-based Approximate Nearest Neighbor Search at Billion Scale for Processing-in-Memory](https://arxiv.org/html/2605.25522v1) | 2026-05-27T08:00:00+08:00 | 十亿级 graph ANNS 迁移到 PIM 不能只下沉距离计算：index footprint、跨 PU graph traversal、host coordination 与弱算力必须联合 co-design；compact index 和异步 mini-batch pipeline 会把瓶颈转移到 host rerank/transfer，并形成overfetch–recall–throughput 的显式边界。；3+3+2=8 | 深入完成 | 整合：root 已写入，fresh 写后终审通过 [章节](../../../../books/part-07-agent/76-rag.md)：AGENT-RAG |
| [2605.25535 Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-horizon Agents](https://arxiv.org/html/2605.25535v1) | 2026-05-27T08:00:00+08:00 | 以 session-level storage gate 学习 user-specific retention policy，选择性跳过短暂会话；理想个性化可改善有限预算下的保留，但准确 gating 仍是未解决边界。；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/77-memory.md)：AGENT-MEMORY |
| [2605.25537 Action-Prior Denoising for Smooth Real-Time Chunking](https://arxiv.org/html/2605.25537v1) | 2026-05-27T08:00:00+08:00 | Soft RTC 用部分去噪的 overlap state 与上一 action chunk 构造 action prior，让已提交前缀保持固定、后续 overlap 仍可编辑，从而在不引入昂贵部署 guidance 时降低动作跳变。；2+2+3=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：MULTIMODAL-EMBODIED-VLA |
| [2605.25547 TapSampling: Inference-Time Sampling with a Task-Progress-Understanding Verifier for Robotic Manipulation](https://arxiv.org/html/2605.25547v1) | 2026-05-27T08:00:00+08:00 | Action-VAE 从 policy proposal 周围生成多个低维 latent action candidates，再以 task-progress outcome predictor 选择动作；verifier 只拥有候选排序权，不能替代 controller commit。；2+2+3=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：MULTIMODAL-EMBODIED-VLA |
| [2605.25550 DisagFusion: Asynchronous Pipeline Parallelism and Elastic Scheduling for Disaggregated Diffusion Serving](https://arxiv.org/html/2605.25550v1) | 2026-05-27T08:00:00+08:00 | 以异步 pipeline 重叠 diffusion stages 的计算与 handoff，并结合轻量性能预测和 runtime feedback 动态重配各 stage instance ratio，以吸收 workload shift 与 stage imbalance。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-05-inference-system/55-pd-disaggregation.md)：INFER-PD-DISAGGREGATION |
| [2605.25621 StreamOV: Streaming Omni-Video Understanding via Evidence-Guided Memory and Response Triggering](https://arxiv.org/html/2605.25621v1) | 2026-05-27T08:00:00+08:00 | 用 multimodal evidence-guided long/short-term memory 在固定预算内压缩流式音视频历史，再由 hidden-state trigger 决定何时主动响应，避免把 silence token 或外部 router 当作唯一时机 owner。；2+2+3=7 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)：MULTIMODAL-REPRESENTATION |
| [2605.25624 CUA-Gym: Scaling Verifiable Training Environments and Tasks for Computer-Use Agents](https://arxiv.org/html/2605.25624v1) | 2026-05-27T08:00:00+08:00 | 由 Generator 构造 initial/golden environment state、独立 Discriminator 编写 reward function、orchestrator 迭代执行并以多数票和 rollout 终检，使 task、environment 与 deterministic reward 成为同一可验证 tuple。；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/84-agent-platform.md)：AGENT-PLATFORM |
| [2605.25632 Insuring Every Action: An Authority Frontier Framework for Runtime Actuarial Control of Autonomous AI Agents](https://arxiv.org/html/2605.25632v1) | 2026-05-27T08:00:00+08:00 | We propose the Actuarial Action Interface (AAI), a deterministic runtime contract that prices each such action against a contractually fixed safe default under a time-consistent risk mapping, and gates execution against a per-boundary reserve capital budget.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/78-tool-calling.md)：AGENT-TOOL-CALLING |
| [2605.25641 Iterate Until Retrieved: Factual Nugget Optimization for Discoverable Continual Corrections in Agentic RAG](https://arxiv.org/html/2605.25641v1) | 2026-05-27T08:00:00+08:00 | 把 factual correction 写成带来源的 nugget，并让生产 RAG 充当 test harness：对触发 query 与 paraphrases 反复 probe、读取失败 trace、修订直到可发现；事实正确性与检索可发现性仍是两个 Gate。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/76-rag.md)：AGENT-RAG |
| [2605.25653 When Agents Control Robots: A Zero Trust Policy Model for Agentic Cyber-Physical Systems](https://arxiv.org/html/2605.25653v1) | 2026-05-27T08:00:00+08:00 | 以 25 个 typed primitives 和 Physical Impact Tier 组成 actuation-boundary zero-trust policy；模型只提议机器人参数，policy 在真实物理 effect 前执行确定性约束。；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.25655 Bandwidth-Aware LLM Inference on Heterogeneous Many-Core Supercomputers](https://arxiv.org/html/2605.25655v1) | 2026-05-27T08:00:00+08:00 | 把 VLIW-SIMD operator、density-driven graph fusion 与 Prefill-Buffer-Decode bounded-buffer pipeline 组合为硬件感知执行计划，使数据 locality、通信层级和 hybrid parallelism 共同受控。；2+2+3=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md)：INFER-SCHEDULING |
| [2605.25673 Referential Security as a New Paradigm for AI Evaluations](https://arxiv.org/html/2605.25673v1) | 2026-05-27T08:00:00+08:00 | To resolve this, we propose referential security as a new paradigm for AI evaluation.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.25674 Stochastic Estimation of the Layer-wise Hessian Trace for Monitoring Neural-network Training](https://arxiv.org/html/2605.25674v1) | 2026-05-27T08:00:00+08:00 | 以一次全参数 Hessian-vector product 配合 Hutchinson probes 无偏估计每层 Hessian trace；weight sharing 必须先装配 layer Hessian 再二次求导，并用临界 probe 数平衡随机投影与 mini-batch 方差。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md)：PLATFORM-MONITORING |
| [2605.25682 Profiling-Driven Adaptive Distributed Transformer Inference on Embedded Edge Deployment](https://arxiv.org/html/2605.25682v1) | 2026-05-27T08:00:00+08:00 | 实机 profiling 表明 embedded distributed inference 的瓶颈还包括 CPU-GPU staging；运行时应依据离线 profile 在 local 与 compressed distributed execution 间选择，而不是默认全 tensor exchange。；2+2+3=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md)：INFER-SCHEDULING |
| [2605.25698 How Should LLMs Consume High-Quality Data? Optimal Data Scheduling via Quality-Aware Functional Scaling Laws](https://arxiv.org/html/2605.25698v1) | 2026-05-27T08:00:00+08:00 | Motivated by the theoretical structure, we propose Drop-Stable-Rampup for LLM midtraining: drop the batch size at the quality transition, keep it low to accumulate signal, then ramp up to suppress noise.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/27-data.md)：TRAIN-DATA |
| [2605.25707 AgentHijack: Benchmarking Computer Use Agent Robustness to Common Environment Corruptions](https://arxiv.org/html/2605.25707v1) | 2026-05-27T08:00:00+08:00 | 用九类可配置的非对抗环境 corruption 分阶段压力测试 computer-use agents，并以 action generator 加独立 onlooker 做 grounding、行为摘要与环境复核；轻微扰动也会造成显著执行退化。；2+2+3=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.25716 An Efficient and Privacy-Preserving Architecture for Cross-Institutional Collaborative RAG](https://arxiv.org/html/2605.25716v1) | 2026-05-27T08:00:00+08:00 | 以 numerically stable feature scrambling 与 token permutation 构造 Scrambled Distributed Attention，把 attention execution 与明文数据位置解耦；该协议仍须对 inversion、collusion 与数值误差单独验收。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.25745 Selective Latent Thinking: Adaptive Compression of LLM Reasoning Chains](https://arxiv.org/html/2605.25745v1) | 2026-05-27T08:00:00+08:00 | 按 confidence gate 在 explicit CoT 与 latent span 之间动态切换，使压缩成为可回退的 runtime commit 决策。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-02-model/18-decoder-only.md)：MODEL-DECODER-ONLY |
| [2605.25746 Multi-Agent Coordination Adaptation via Structure-Guided Orchestration](https://arxiv.org/html/2605.25746v1) | 2026-05-27T08:00:00+08:00 | 把 agent participation graph 与 step-level orchestration作为联合可适配状态，而非固定拓扑或隐式通信。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/82-multi-agent.md)：AGENT-MULTI-AGENT |
| [2605.25798 DiSC: Resolution-Scalable Acceleration of Diffusion Models by Exploiting Sparsity and Cached Token Reuse with Hash-based Distribution](https://arxiv.org/html/2605.25798v1) | 2026-05-27T08:00:00+08:00 | 以跨 diffusion step 的 Cached Token Reuse 和复用 attention sparsity mask 的 Softmax Thresholding 形成混合 dense/sparse workload，再用 hash-based bank distribution 在同一 accelerator 数据流中承载稀疏执行。；2+2+3=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)：INFER-TENSORRT-LLM |
| [2605.25815 Behind EvoMap: Characterizing a Self-Evolving Agent-to-Agent Collaboration Network](https://arxiv.org/html/2605.25815v1) | 2026-05-27T08:00:00+08:00 | 证明开放 A2A asset economy 若把 publication、自报 metadata 与本地日志当 authority，会产生不可审计的 reuse/quality failure。；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/84-agent-platform.md)：AGENT-PLATFORM |
| [2605.25819 On Reliability of Efficient Membership Inference Vulnerability Evaluation](https://arxiv.org/html/2605.25819v1) | 2026-05-27T08:00:00+08:00 | 把低-FPR membership-inference audit 的 sample identity、aggregation threshold 与 finite-population bias纳入 measurement contract。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.25820 Visual-Redundancy-Controlled Parallel Decoding for Diffusion-Based Multimodal Large Language Models](https://arxiv.org/html/2605.25820v1) | 2026-05-27T08:00:00+08:00 | 用 Visual Redundancy Index 衡量同一步并行提交 tokens 的视觉 grounding 重叠，再让 VRCD 优先提交视觉互补位置；attention overlap 只是 selection sensor，不是语义正确性证明。；2+2+3=7 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)：MULTIMODAL-GENERATIVE-PARADIGMS |
| [2605.25831 Clarify, Abstain or Answer? Strategising in Conversation with Belief-Augmented Generation](https://arxiv.org/html/2605.25831v1) | 2026-05-27T08:00:00+08:00 | We propose Belief-Augmented Generation (BAG): grounding LLMs in their own belief state via the prompt and letting them reason over these K samples to decide on a conversational strategy: answer, clarify, or abstain.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/80-reflection.md)：AGENT-REFLECTION |
| [2605.25854 From Accounting to Coordination: A Virtual Water-Aware Electricity-Computation-Water Nexus Framework for Data Center Dispatch](https://arxiv.org/html/2605.25854v1) | 2026-05-27T08:00:00+08:00 | 把 data-center workload placement 的 cost 从静态水耗统计改为与电网 dispatch 联动的可执行控制目标。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/70-cost.md)：PLATFORM-COST |
| [2605.25869 Mitigating Provenance-Role Collapse in Long-Term Agents via Typed Memory Representation](https://arxiv.org/html/2605.25869v1) | 2026-05-27T08:00:00+08:00 | To resolve this cognitive vulnerability at the architectural level, we propose MemIR, a typed Memory Intermediate Representation that operationalizes source monitoring as a structural constraint.；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/77-memory.md)：AGENT-MEMORY |
| [2605.25874 WBench: A Comprehensive Multi-turn Benchmark for Interactive Video World Model Evaluation](https://arxiv.org/html/2605.25874v1) | 2026-05-27T08:00:00+08:00 | 以 video quality、setting/interaction adherence、consistency 与 physics compliance 五轴组成 multi-turn world-model benchmark，并统一 text、6-DoF pose 与 discrete action 接口、用人评校准自动子指标。；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：MULTIMODAL-WORLD-MODELS |
| [2605.25889 Capability and Robustness Cannot Both Be Free: An Information-Theoretic Bound for Vision-Language-Action Models](https://arxiv.org/html/2605.25889v1) | 2026-05-27T08:00:00+08:00 | 将 VLA robustness 从单项防御分数提升为 capability、encoder channel 与 attack budget 共同约束的 evaluation boundary。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：MULTIMODAL-EMBODIED-VLA |
| [2605.25893 $D^2$-Monitor: Dynamic Safety Monitoring for Diffusion LLMs via Hesitation-Aware Routing](https://arxiv.org/html/2605.25893v1) | 2026-05-27T08:00:00+08:00 | 把 diffusion trajectory 中 hidden state 反复贴近 probe decision boundary 的次数定义为 safety hesitation，以此预测轻量 probe failure 并只在阈值越界时路由重 probe。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.25966 Mapping the Schedule x Bit-Width Boundary in Sub-100M Quantisation-Aware Training](https://arxiv.org/html/2605.25966v1) | 2026-05-27T08:00:00+08:00 | factorial evidence 否定 FP16/INT8/INT6 需要不同 warmdown 的假设，却发现 INT4 在约 50M 参数以上出现明确 schedule boundary；bit-width、model size 与 schedule 必须共同组成训练 identity。；2+2+3=7 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/28-pretraining.md)：TRAIN-PRETRAINING |
| [2605.25971 Anticipate and Learn: Unleashing Idle-Time Compute in Proactive Agents](https://arxiv.org/html/2605.25971v1) | 2026-05-27T08:00:00+08:00 | 让 agent 在空闲期主动读取 memory、预取 evidence，并把过期/错误 anticipation 作为可取消 speculative state。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/84-agent-platform.md)：AGENT-PLATFORM |
| [2605.25988 What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA](https://arxiv.org/html/2605.25988v1) | 2026-05-27T08:00:00+08:00 | 训练期 checker 的输出分布而非 held-out accuracy 决定是否提供可学习梯度：neutral-heavy log-prob scoring 会 signal collapse，过强 checker 又会诱发短答案、避检索与语言坍缩的 reward hacking。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-07-agent/76-rag.md)：AGENT-RAG |
| [2605.25997 Deployment-complete benchmarking](https://arxiv.org/html/2605.25997v1) | 2026-05-27T08:00:00+08:00 | 把 benchmark score 是否足以决定 deployment action 形式化为 evidence-fiber completeness 与补证成本。；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.26029 CausaLab: A Scalable Environment for Interactive Causal Discovery Toward AI Scientists](https://arxiv.org/html/2605.26029v1) | 2026-05-27T08:00:00+08:00 | 在可干预 synthetic SCM laboratory 中把 held-out prediction 与 recovered graph/equations 的机制忠实度分开计分；高预测准确率可与低结构恢复并存，premature stopping 需要 consistency verification。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.26037 Peak-Then-Collapse and the Four Interface Channels of Knowledge-Graph Tool Use](https://arxiv.org/html/2605.26037v1) | 2026-05-27T08:00:00+08:00 | 揭示 outcome-only RLVR 在低信息 tool feedback 下会 peak-then-collapse，reward densification 只能迁移 failure 而不能补足接口信息。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/33-grpo.md)：TRAIN-GRPO |
| [2605.26045 Confidence and Calibration of Activation Oracles for Reliable Interpretation of Language Model Internals](https://arxiv.org/html/2605.26045v1) | 2026-05-27T08:00:00+08:00 | 把 activation-oracle 文本解释从无置信度输出改为按 answer-space 可枚举性选择的校准 measurement operator。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.26046 When Gradients Collide: Failure Modes of Multi-Objective Prompt Optimization for LLM Judges](https://arxiv.org/html/2605.26046v1) | 2026-05-27T08:00:00+08:00 | multi-objective textual-gradient optimization 存在两个可分 failure：联合反馈会稀释 optimization-time task focus，合并单目标优化后的 instructions 又会产生 inference-time interference。；2+2+3=7 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.26047 Retrying vs Resampling in AI Control](https://arxiv.org/html/2605.26047v1) | 2026-05-27T08:00:00+08:00 | 区分会泄露 monitor rationale 的 retry control 与不暴露反馈的 resampling，并把 sample aggregation/audit budget 纳入安全契约。；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/72-security.md)：PLATFORM-SECURITY |
| [2605.26079 Automated Benchmark Auditing for AI Agents and Large Language Models](https://arxiv.org/html/2605.26079v1) | 2026-05-27T08:00:00+08:00 | 以 agentic audit 重放 task specification、environment dependency 与 grader logic；发现的问题经专家/上游修复验证后会改变分数和模型排序，因此 benchmark task 本身必须先通过 admission。；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：PLATFORM-EVALUATION-SYSTEM |
| [2605.26089 Channel-wise Vector Quantization](https://arxiv.org/html/2605.26089v1) | 2026-05-27T08:00:00+08:00 | 视觉离散表示的 quantization axis 也是 representation contract：patch vector 改为 global channel map 后，token identity、序列长度与 AR ordering 一起变化；3+2+3=8 | 深入完成 | 整合：root 已写入，fresh 写后语义验收通过 [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)：MULTIMODAL-REPRESENTATION |
| [2605.26097 Forgetting in Language Models: Capacity, Optimization, and Self-Generated Replay](https://arxiv.org/html/2605.26097v1) | 2026-05-27T08:00:00+08:00 | retention signal、剩余容量与优化速度共同决定 continual SFT 的遗忘边界；自生成 replay 不能越过容量下界；3+2+3=8 | 深入完成 | 整合：root 已写入，fresh 写后语义验收通过 [章节](../../../../books/part-04-training-system/29-sft.md)：TRAIN-SFT |
| [2605.26099 Language Models Need Sleep](https://arxiv.org/html/2605.26099v1) | 2026-05-27T08:00:00+08:00 | 周期性 offline recurrence 在清空 KV 前把 recent context 整理进 persistent fast weights，并用可调 sleep passes 把深层推理计算从 wake-time decode 移到有界离线阶段；runtime 因而必须共同拥有 sleep trigger、fast-state version、KV clear/commit 与失败回退。；3+2+3=8 | 深入完成 | 整合：[章节](../../../../books/part-02-model/22-long-context.md)：MODEL-LONG-CONTEXT（root 已写入；binding 与证据/推论边界通过 fresh 写后语义验收） |
| [2605.26110 Prism: A Plug-in Reproducible Infrastructure for Scalable Multimodal Continual Instruction Tuning](https://arxiv.org/html/2605.26110v1) | 2026-05-27T08:00:00+08:00 | 以 plugin registration 将 continual-tuning algorithm state 与 MLLM backbone/runtime 解耦，使新策略无需改写底座即可在同一 scalable pipeline 中复现和公平比较。；2+2+3=7 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-06-ai-infrastructure/60-training-operator.md)：PLATFORM-TRAINING-OPERATOR |
| [2605.26112 From Model Scaling to System Scaling: Scaling the Harness in Agentic AI](https://arxiv.org/html/2605.26112v1) | 2026-05-27T08:00:00+08:00 | 把 context governance、memory、skill routing、orchestration、verification 与 governance 组成可版本化 agent harness，并把 harness-level trajectory、memory hygiene、communication fidelity 与 safe evolution 纳入评价对象。；2+2+3=7 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/84-agent-platform.md)：AGENT-PLATFORM |
| [2605.26114 MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research](https://arxiv.org/html/2605.26114v1) | 2026-05-27T08:00:00+08:00 | 把完整 mobile environment state 表示为可配置、fork 和比较的 structured JSON，并以同一 deterministic state judge 同时提供 evaluation verdict 与 dense RL reward，从而支持高并发可验证 rollout。；3+2+3=8 | 深入完成 | 已有覆盖 [章节](../../../../books/part-07-agent/84-agent-platform.md)：AGENT-PLATFORM |
| [minimax:sparse-token-forgetting Why Can't the MiniMax LLM Say "Ma Jiaqi"? Internal Investigation of Sparse Token Forgetting](https://www.minimax.io/blog/sparse-token-forgetting) | 2026-05-27T08:00:00+08:00 | SFT 不只监控 task/domain coverage，还要监控 token-as-target coverage 与 pretrain→SFT `lm_head` drift；全词表重复数据可保底但可能浪费容量或损害会话能力，Korean 反例说明失败时需回退数据清洗、targeted synthesis、受控 replay 或 CPT。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在 [章节](../../../../books/part-04-training-system/29-sft.md)：TRAIN-SFT |

## 4. 证据与知识整合

### [2605.24817 RouteScan: A Non-Intrusive Approach to Auditing MoE LLMs Safety via Expert Routing Telemetry](https://arxiv.org/html/2605.24817v1)

- **采用命题：** Inspired by this observation, we propose RouteScan, a non-intrusive auditing framework for detecting harmful behaviors through such routing-induced GPU telemetry.
- **方法定位：** §5 Method: request-level telemetry, hybrid scoring and calibrated detector
- **评价定位：** §6 Evaluation, including §6.3–§6.5 transfer and privacy-boundary tests
- **限制/反证：** §8 Discussion; §10 Ethical Concern; no dedicated Limitations section
- **证据边界：** RouteScan: A Non-Intrusive Approach to Auditing MoE LLMs Safety via Expert Routing Telemetry 的 exact-v1 只支持该文披露机制：Inspired by this observation, we propose RouteScan, a non-intrusive auditing framework for detecting harmful behaviors through such routing-induced GPU telemetry. 其未证明边界由 `§8 Discussion; §10 Ethical Concern; no dedicated Limitations section` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **Books：** `Applied`；owner 为 `PLATFORM-MONITORING` / [`books/part-06-ai-infrastructure/67-monitoring.md`](../../../../books/part-06-ai-infrastructure/67-monitoring.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.24818 Spiking the training data to correct for test set contamination](https://arxiv.org/html/2605.24818v1)

- **采用命题：** 在已知比例主动注入 benchmark 样本并拟合 contamination-response curve，把污染校正从事后猜测变成带干预记录的 evaluation protocol。
- **方法定位：** §3 Simulating contamination; §3.1 Estimators and predictors; §3.2 Data generation
- **评价定位：** §4 Benchmarking predictors; §5 Practical considerations; Appendix B Experimental details
- **限制/反证：** §5 Practical considerations; §6 Discussion: controlled Hubble-8B/test-set setting, training-data access and counterfactual-model assumptions
- **证据边界：** 只证明论文披露的 Hubble-8B、五类 benchmark 与模拟污染设置；需要训练数据写权限和未污染 counterfactual 假设，不能外推成任意闭源模型的通用校正器。
- **Books：** `Applied`；owner 为 `PLATFORM-EVALUATION-SYSTEM` / [`books/part-06-ai-infrastructure/66-evaluation-system.md`](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.24823 Agent Manufacturing: Foundation-Model Agents as First-Class Industrial Entities](https://arxiv.org/html/2605.24823v1)

- **采用命题：** 把 Agent Manufacturing 操作化为由 foundation-model agents 承担开放目标解释、长程规划、工具/机器调用及人机协商的生产协调机制，并与封闭协议空间中的传统 multi-agent manufacturing 区分。
- **方法定位：** §3 Definition and Decomposition of Industrial Cognition; §4 thin versus thick autonomy
- **评价定位：** §5 The Factory as a Cognitive Ecosystem: A Worked Example
- **限制/反证：** §8 Research Agenda; §9 Conclusion; position paper and near-future composite, not deployed-system validation
- **证据边界：** Agent Manufacturing: Foundation-Model Agents as First-Class Industrial Entities 的 exact-v1 只支持该文披露机制：Manufacturing has passed through four widely recognized paradigms - mechanization, electrification, programmable automation, and Smart Manufacturing - each defined by the kind of work it shifted from humans to machines. 其未证明边界由 `§8 Research Agenda; §9 Conclusion; position paper and near-future composite, not deployed-system validation` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **当前正文承载：** `Agent 改变了平台的控制对象` — 模型服务的主要对象是 request 与 token-generation state。Agent 增加： ```text goal plan and workflow state context assembly memory read/write tool/action intents external side effects delegation human approvals long-running events ``` 请求完成不再等于任务完成。一个 Agent run 可能持续数分钟、数天，被暂停、等待用户、跨多个模型与工具后再恢复。 长期 delegation 还会使 credential 生命周期超过一次模型请求。Heartbeat-bound hierarchical credential 把 child credential 的有效性绑定到 parent 周期性 liveness proof，使父任务失联后授权自动衰减；它用持续签名、时钟与 层级恢复复杂度换更短的悬挂权限窗口。heartbeat delay、partition 或 parent compromise 仍会造成误撤销或错误续期， 作者协议与评测不证明所有身份系统安全；高风险 effect 应保留短期 token、中央 revoke 与人工审批 fallback。 Policy-as-code 运行时可以在 proposal、tool admission、effect execution 与 state commit 等关键阶段执行 intervention， 避免只在 prompt 或最终答案处做一次过滤。每个 policy decision 必须绑定 agent/run、输入、规则 revision、effect 与 receipt；模型和工具都不能自行跳过。更细粒度 enforcement 增加延迟、策略冲突和 availability 风险，demo 结果也不 证明开放环境安全。policy engine 不可用或规则冲突时，应 fail closed、降级到只读能力或转人工，而不是继续执行。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：把 Agent Manufacturing 操作化为由 foundation-model agents 承担开放目标解释、长程规划、工具/机器调用及人机协商的生产协调机制，并与封闭协议空间中的传统 multi-agent manufacturing 区分。
- **Books：** `No Change — Existing Coverage`；owner 为 `AGENT-PLATFORM` / [`books/part-07-agent/84-agent-platform.md`](../../../../books/part-07-agent/84-agent-platform.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.24832 Optimus: Elastic Decoding for Efficient Diffusion LLM Serving](https://arxiv.org/html/2605.24832v1)

- **采用命题：** We present Optimus, a serving system that enables elastic decoding for diffusion LLMs by dynamically adapting decoding granularity to runtime load.
- **方法定位：** §4 Streaming Chunked Decoding; §5 Saturation-aware Elastic Scheduling
- **评价定位：** §7 Evaluation, especially §7.3–§7.7 throughput, serving and ablation results
- **限制/反证：** §9 Conclusion; no dedicated Limitations section; evidence is bounded to evaluated DLLMs, A100 and disclosed loads
- **证据边界：** Optimus: Elastic Decoding for Efficient Diffusion LLM Serving 的 exact-v1 只支持该文披露机制：We present Optimus, a serving system that enables elastic decoding for diffusion LLMs by dynamically adapting decoding granularity to runtime load. 其未证明边界由 `§9 Conclusion; no dedicated Limitations section; evidence is bounded to evaluated DLLMs, A100 and disclosed loads` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **Books：** `Applied`；owner 为 `INFER-TENSORRT-LLM` / [`books/part-05-inference-system/49-tensorrt-llm.md`](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.24870 Trajectory-Consistent Calibration for Cache-Accelerated Diffusion Models](https://arxiv.org/html/2605.24870v1)

- **采用命题：** 把 diffusion cache 的误差从单点 representation mismatch 扩展为会被先前校准继续改写的 trajectory state，并沿 corrected history 逐步拟合 site-local calibration prior。
- **方法定位：** §2 Problem Formulation; §3.1 Local Statistical Calibration; §3.2 Trajectory-Consistent Prior Estimation
- **评价定位：** §4.1–§4.3 PixArt-alpha/DiT-XL/2 experiments and ablations; Appendix B.1–B.8 latency, prompt-count and compute details
- **限制/反证：** Appendix C Limitations and Broader Impact; offline priors, selected sites/windows, representative-prompt and tested-model boundary
- **证据边界：** 只验证 PixArt-alpha、DiT-XL/2、FORA/ToCa/L2C 与披露的离线 prior、采样步数和 H800 路径；prior 漂移、未测 cache policy、在线并发与分布外 prompt 不受该结果保证，失配时应回退 base cache 或 full computation。
- **Books：** `Applied`；owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS` / [`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.24879 Efficient DP-SGD for LLMs with Randomized Clipping](https://arxiv.org/html/2605.24879v1)

- **采用命题：** 用 Hutchinson/Hutch++ 随机 trace estimation 近似 per-sample gradient norm，把 DP clipping 的显存复杂度从显式 T×T 或 d×d 中间量改为受投影维度控制的 estimator，并为随机 clipping 单独建立 privacy accountant。
- **方法定位：** §4 Proposed Method; §5 Privacy Analysis and Accounting; Appendix B.9 randomized-clipping accountant
- **评价定位：** §6 Experiments; §6.1 Memory, Compute and Latency Gains; Appendix D hyperparameters
- **限制/反证：** §7 Conclusion and experiment scope: Llama-3.2-1B, sequence length 4096, selected full/LoRA fine-tuning tasks and randomized norm-estimation assumptions
- **证据边界：** 形式保证依赖论文的随机 clipping mechanism 与 accountant 被原样实现；实验只覆盖 Llama-3.2-1B、固定 4096 长度和三类任务，未证明大模型、分布式 microbatch、任意 epsilon 或任意投影维度下同时保持 utility 与成本优势。
- **Books：** `Applied`；owner 为 `PLATFORM-SECURITY` / [`books/part-06-ai-infrastructure/72-security.md`](../../../../books/part-06-ai-infrastructure/72-security.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.24883 Inverting the Shield: Systematically Generating Safety Tests from Policy Specifications](https://arxiv.org/html/2605.24883v1)

- **采用命题：** 把自然语言 safety policy 编译为形式化谓词和语义图，再从未覆盖路径生成可追踪测试，使 policy revision、test identity 与 coverage evidence 成为同一评估对象。
- **方法定位：** §3 Methodology: policy-to-FOL translation, semantic policy graph and graph-guided query instantiation
- **评价定位：** §4 Evaluation: policy coverage and attack efficacy
- **限制/反证：** § Limitations: policy-quality dependency, static single-turn scope, no multi-turn or agent-state coverage
- **证据边界：** 垃圾输入 policy 会直接产生错误测试；exact-v1 只覆盖静态单轮交互，未证明多轮 Agent state、生产 policy 漂移或自动生成测试的完备性。
- **Books：** `Applied`；owner 为 `PLATFORM-EVALUATION-SYSTEM` / [`books/part-06-ai-infrastructure/66-evaluation-system.md`](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.24892 X-Foresight: A Joint Vision-Action Causal Forecasting Network via Predictive World Modeling](https://arxiv.org/html/2605.24892v1)

- **采用命题：** 把低熵相邻帧预测改成跨语义时间块的自回归 future-state 预测：块内保留稠密瞬时动态、块间保留稀疏长程因果，并把 action/latent prediction 与多视角 renderer 分责。
- **方法定位：** §3.1 Large Drive Model, especially §3.1.3 chunk-wise prediction/CLEF/TIS; §3.2 Vision Renderer; §3.3 training and interleaved inference pipeline
- **评价定位：** §4.1 Large Drive Model and §4.2 Vision Renderer, including horizon/CL-CLEF-TIS ablations and production-scale comparison
- **限制/反证：** §5 Conclusion/future directions; private driving-data distribution, learned renderer and offline/closed-loop evaluation boundary; no dedicated limitations section
- **证据边界：** 证据绑定作者私有驾驶数据、4 Hz 七相机 rollout、learned renderer 与披露的闭环设置；视觉一致性和 planning gain 不证明真实道路安全、因果识别或跨 embodiment 泛化。Ch25 已有 transition-token/reasoner/renderer 分责和多时间尺度状态边界，故不重复写入。
- **当前正文承载：** `从单尺度预测到 Abstraction × Timescale Hierarchy` — 单一 latent、单一帧率的 predictor 在 horizon 短、场景变化均匀时最直接；所有状态在同一表示里更新，也减少跨层 drift。长时视频的约束不同：低频语义变化决定道路拓扑与主体意图，高频视觉变化承担纹理、局部运动和短时一致性。让一个 state 同时保存两种时间尺度，会把计算浪费在重复细节上，或为了压缩而丢失慢变量。 一种演进是让较慢的 abstract predictor 拥有长期语义 trajectory，再由较快的 detail predictor 在其条件下恢复 pixel-aligned dynamics。这里是两个正交轴：abstraction 决定保留什么，timescale 决定何时更新。representation-rich pretraining 可以先提高状态可辨识性，rollout-oriented fine-tuning 再减少自回归误差；二者不能用同一个 loss 结论替代。 分层会引入 interface mismatch、两层 objective 冲突和错误下传：慢层一旦选错语义轨迹，快层只能生成更逼真的错误未来。单尺度 predictor 在短 horizon、数据少或跨层对齐成本高时仍成立。现有驾驶视频实验支持 hierarchy/forcing 的受限机制，却没有证明 action-conditioned control sufficiency、真实道路 causal accuracy 或规划收益。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：把低熵相邻帧预测改成跨语义时间块的自回归 future-state 预测：块内保留稠密瞬时动态、块间保留稀疏长程因果，并把 action/latent prediction 与多视角 renderer 分责。
- **Books：** `No Change — Existing Coverage`；owner 为 `MULTIMODAL-WORLD-MODELS` / [`books/part-03-multimodal-world-models/25-multimodal-world-models.md`](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.24914 MVR-cache: Optimizing Semantic Caching via Multi-Vector Retrieval and Learned Prompt Segmentation](https://arxiv.org/html/2605.24914v1)

- **采用命题：** 以可学习 prompt segmentation 生成多向量表示，再用 MaxSim 做细粒度匹配；训练目标直接约束在 correctness 前提下增加 cache hit，并以强化学习求解不可微组合优化。
- **方法定位：** §3 MVR-cache multi-vector retrieval and prompt segmentation
- **评价定位：** §5 semantic-cache evaluation
- **限制/反证：** §6 limitations and workload/encoder boundary
- **证据边界：** MVR-cache: Optimizing Semantic Caching via Multi-Vector Retrieval and Learned Prompt Segmentation 的 exact-v1 只支持该文披露机制：To reduce LLM costs and latency, semantic caching systems must accurately identify when a new prompt matches a cached one. 其未证明边界由 `§6 limitations and workload/encoder boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **Books：** `Applied`；owner 为 `INFER-KV-CACHE` / [`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。Fresh non-author post-write semantic review passed; the paired binding remains before the first main H2 Review notes.

### [2605.24922 MuJoCoUni:Persistent Batched Runtime Primitives for MuJoCo](https://arxiv.org/html/2605.24922v1)

- **采用命题：** 把 stateless rollout 调用提升为 executor-owned persistent environment pool，使 per-environment model/data、reset、step 与 Jacobian state 在 batched robot-learning loop 中保持可寻址。
- **方法定位：** §3 System Design and API; §3.1 Design boundary; §3.2 Persistent pool ownership; §3.3 Runtime primitives; §3.4 Reset-time randomization
- **评价定位：** §4 Validation and Benchmarks: parity, rollout throughput, reset and Jacobian measurements
- **限制/反证：** §6 Discussion; §6.1 Runtime boundary and trade-offs; §6.3 Reproducibility
- **证据边界：** 证据绑定 MuJoCo 与论文测试硬件/任务；persistent pool 增加生命周期、隔离和复现责任，未证明真实机器人、分布式故障或硬实时控制语义。
- **Books：** `Applied`；owner 为 `MULTIMODAL-EMBODIED-VLA` / [`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.24930 H$^{2}$MT: Semantic Hierarchy-Aware Hierarchical Memory Transformer](https://arxiv.org/html/2605.24930v1)

- **采用命题：** 先把长文档组织成语义树，再用层级 memory tokens 与 query-aware routing 在粗摘要和细粒度节点间分配注意力预算。
- **方法定位：** §3 Methodology; §3.1 Semantic tree construction; §3.2 Memory-token construction; §3.3 Hierarchical inference; §3.4 Objectives
- **评价定位：** §4 Experiments: LongBench/structured-document quality, TTFT and memory
- **限制/反证：** §5 Conclusion and discussion: hierarchy dependency, heuristic-tree error propagation, rare-evidence attenuation and routing-prune risk
- **证据边界：** 收益依赖可恢复的文档层级；错误树和过度压缩会丢失稀有证据。当前 Ch22 已拥有 query-aware hierarchical selection、coarse summary 与 dense fallback，因此不重复写入。
- **当前正文承载：** `Selector 可以进入 Forward，但必须显式承担语义责任` — Teacher-distilled index branch 把 dense Attention 留作语义 owner，便于校准和迁移；另一条并存分支让 selector 直接进入 Attention forward。对每个远程 chunk，不再只用 mean/max pooled key 给出一个被 hard top-k 丢弃的分数，而是学习近似 chunk LogSumExp mass 的 summary，并先在 chunks 间分配 mass、再在 chunk 内对 tokens 归一化。由于 chunk score 参与最终 attention output，next-token LM loss 可以直接训练 selector。 这不会把近似 selector 变成 exact full attention。Landmark/query calibration、HoPE/position rule、chunk size、top-k、local window 与 sparse kernel 必须随 checkpoint 版本化；漏选 chunk 仍是不可恢复的信息损失。 将相邻 queries 的候选 chunks 合并加载可以提高 Tensor Core 利用率，却会引入 union overfetch。短 Context、 严格回读、无法 continued training 或缺少匹配 kernel 时，dense attention 或 teacher-owned selector 仍更合理。 这条分支当前只在作者披露的 345M、1.4B、OLMo3-7B、指定训练 recipe 与单 H800 batch-1 inference contract 下得到验证，不构成通用长度或性能保证。 Selector 的监督还会决定它究竟模仿“Attention 看过哪里”，还是学习“有限预算下什么对任务有用”。用 dense-attention ranking 作 teacher 容易迁移且便于校准；把连续 gate 注入 attention logits，则可让最终 LM loss 直接训练选择器，避免相似度与 task utility 错位。后者获得端到端 credit，却把 selector miss 直接带入模型语义，并新增 pooled summary、稀疏 kernel 和 continued-training 依赖。预算宽松或 exactness 优先时，teacher-owned selector 与 dense fallback 仍应保留。 三条路线解决的问题并不相同：hybrid linear/softmax 保留两种记忆偏好，NSA 联合设计训练 稀疏与硬件访问，DSA 强调既有模型的 staged migration。最终应比较
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：先把长文档组织成语义树，再用层级 memory tokens 与 query-aware routing 在粗摘要和细粒度节点间分配注意力预算。
- **Books：** `No Change — Existing Coverage`；owner 为 `MODEL-LONG-CONTEXT` / [`books/part-02-model/22-long-context.md`](../../../../books/part-02-model/22-long-context.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.24941 Memory-Induced Tool-Drift in LLM Agents](https://arxiv.org/html/2605.24941v1)

- **采用命题：** 长期记忆中的成本、耐心或风险偏好即使与当前任务无关，也会通过隐式 steering 与关键词注意力重分配改变 tool arguments；相关性提示和 memory filter 只能缓解，不能消除这种 memory-induced tool drift。
- **方法定位：** PDF §3 memory-induced tool-drift mechanism
- **评价定位：** PDF §4 agent/tool evaluation
- **限制/反证：** PDF §5 limitations and memory/task boundary
- **证据边界：** Memory-Induced Tool-Drift in LLM Agents 的 exact-v1 只支持该文披露机制：We study a previously unexamined failure of this combination: when personality-driven biases stored in memory (cost-consciousness, impatience, risk tolerance, etc.) silently affect tool calls in contexts where they are not applicable. 其未证明边界由 `PDF §5 limitations and memory/task boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **Books：** `Applied`；owner 为 `AGENT-TOOL-CALLING` / [`books/part-07-agent/78-tool-calling.md`](../../../../books/part-07-agent/78-tool-calling.md)。Fresh non-author post-write semantic review passed; the paired binding remains before the first main H2 Review notes.

### [2605.24973 MinerU-Popo: Universal Post-Processing Model for Structured Document Parsing](https://arxiv.org/html/2605.24973v1)

- **采用命题：** 在 page OCR 之后增加 document-level state owner，跨页合并段落/表格并同步 chunk 与结构索引，使 ingestion 输出可被 RAG 以同一 document revision 消费。
- **方法定位：** §3 Problem formulation; §4.1 Task-oriented data engine; §4.2 Dynamic chunking and synchronization; §4.3 Document enrichment
- **评价定位：** §5 Experiments: five OCR backends and downstream RAG/QA
- **限制/反证：** §5 evaluation scope and §6 conclusion: OCR/model/workload boundary; cross-page summaries can suppress fine-grained evidence
- **证据边界：** 作者结果绑定披露的 OCR/VLM、H200 与文档集合；跨页修复可能合并错误或隐藏细粒度 locator，不能替代原页、region provenance 与独立 evidence check。
- **Books：** `Applied`；owner 为 `AGENT-RAG` / [`books/part-07-agent/76-rag.md`](../../../../books/part-07-agent/76-rag.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25002 MemMark: State-Evolution Attribution Watermarking for Agent Long-Term Memory Systems](https://arxiv.org/html/2605.25002v1)

- **采用命题：** We propose MemMark, a state-evolution attribution watermark that embeds an owner-controlled signal into latent memory-write decisions.
- **方法定位：** §3 Problem Formulation; §4 MemMark, including distribution-preserving watermark and cryptographic audit trace
- **评价定位：** §5 Experiments, RQ1–RQ5
- **限制/反证：** §7 Limitations; Appendix G memory-lifecycle attacks and backend diagnostics
- **证据边界：** MemMark: State-Evolution Attribution Watermarking for Agent Long-Term Memory Systems 的 exact-v1 只支持该文披露机制：We propose MemMark, a state-evolution attribution watermark that embeds an owner-controlled signal into latent memory-write decisions. 其未证明边界由 `§7 Limitations; Appendix G memory-lifecycle attacks and backend diagnostics` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **Books：** `Applied`；owner 为 `AGENT-MEMORY` / [`books/part-07-agent/77-memory.md`](../../../../books/part-07-agent/77-memory.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25052 Faithfulness Metrics Don't Measure Faithfulness: A Meta-Evaluation with Ground Truth](https://arxiv.org/html/2605.25052v1)

- **采用命题：** 先构造能暴露真实中间计算的任务并生成 step/CoT 级 ground-truth faithfulness label，再审计现有指标；多数指标接近随机、对长 CoT 退化且跨设置不迁移，因此自动分数不能未经有效性验收就充当 faithfulness 证据。
- **方法定位：** §2 faithfulness definitions; §3 ground-truth elicitation; §4 BonaFide labeling pipeline
- **评价定位：** §5 Experiments and §5.2 Results
- **限制/反证：** §5.3 Discussion — Limitations; task/model and metric-cost boundary
- **证据边界：** Faithfulness Metrics Don't Measure Faithfulness: A Meta-Evaluation with Ground Truth 的 exact-v1 只支持该文披露机制：Building on this methodology, we present BonaFide, a benchmark of 3,066 labeled CoTs across 13 tasks and 10 models, and use it to conduct the first systematic evaluation of prominent faithfulness metrics. 其未证明边界由 `§5.3 Discussion — Limitations; task/model and metric-cost boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **当前正文承载：** `Scorer 不是绝对真相` — 不同任务需要不同证据源： | Scorer | 优势 | 主要失败方式 | | --- | --- | --- | | Exact rule / schema | 快、确定、可重复 | 只能测可形式化条件 | | Executable verifier | 接近真实结果，如 tests、compiler、simulator | verifier 可能不完整或被绕过 | | Reference-based metric | 易于批量比较 | 多个正确答案时可能误罚 | | Human judgment | 能理解语境与业务风险 | 贵、慢、有分歧和疲劳 | | Model judge | 可扩展、可生成理由 | position、style、self-preference 与共享盲点 | | Production outcome | 最贴近真实价值 | 反馈延迟、混杂因素与实验风险 | LLM-as-a-Judge 可以降低开放式任务的评估成本，但 judge 也必须被评估。至少需要： - 固定 judge model、prompt、sampling 和 rubric； - 用人工或可执行 verifier 校准关键 slices； - 随机交换候选顺序以检查 position bias； - 把 judge disagreement 和理由作为 evidence，而不是只保留平均分； - 防止被评估输出向 judge 注入指令； - 避免 candidate 与 judge 同源时把 correlated preference 当成独立证据。 “让更强模型打分”是一种 measurement design，不是 ground truth 的替代。 当 verifier 还负责挑选纠错训练数据，这个限制会进入反馈回路：只重训被拒绝的答案，会让“答错但被放过” 的样本缺少直接纠错信号；再用同一 verifier 画质量曲线，便可能把未检出的错误当成质量稳定。应在接受与 拒绝两类样本中保留独立审计，分别测错误放行和替代答案的错误，不能只盯升级率下降。 [廉价验证级联的研究](https://arxiv.org/html/2609.01345v1) 测到了这种盲区，但真实训练未实现持续改善； 其渐近错误下限依赖简化模型与合成实验，不能写成所有自训练系统的定律。独立审计增加成本，开放任务也未必 存在廉价真值；此时应披露可判断范围，而不是让内部仪表盘自行证明可靠性。 多模态生成还提供一条低训练成本分支：冻结一个 image-conditioned reader，用目标 prompt 在生成图像条件下的 log-likelihood 作为 **read-back reward sensor**。它测量的是“该 evaluator 能否从图像恢复提示语义”，不是人类 偏好、
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：先构造能暴露真实中间计算的任务并生成 step/CoT 级 ground-truth faithfulness label，再审计现有指标；多数指标接近随机、对长 CoT 退化且跨设置不迁移，因此自动分数不能未经有效性验收就充当 faithfulness 证据。
- **Books：** `No Change — Existing Coverage`；owner 为 `PLATFORM-EVALUATION-SYSTEM` / [`books/part-06-ai-infrastructure/66-evaluation-system.md`](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25073 Security in the Fine-Tuning Lifecycle of Large Language Models: Threats, Defenses,Evaluation, and Future Directions](https://arxiv.org/html/2605.25073v1)

- **采用命题：** 把 fine-tuning attack surface 按 pre-tuning input/supply chain、during-tuning optimizer/update 与 post-tuning adapter/artifact 三个 intervention phase 组织，并用同一基座和协议检查跨 phase 防御组合。
- **方法定位：** §2 Evaluation Substrate and Threat Model; §3–§5 pre/during/post-tuning lifecycle taxonomy; §6 unified cross-phase evaluation
- **评价定位：** §6.2–§6.6 shared models/tasks, reproduced attacks and cross-phase defense combinations
- **限制/反证：** §7 Discussion and §8 Future Directions; reproduced small-model/task configurations, method-compatibility substitutions and lifecycle-survey boundary
- **证据边界：** survey taxonomy 与复现实验只能支持披露的 Llama/Qwen 1B–4B、SST-2/AGNews/agent subsets 和选定 attack-defense pairs；不能证明未复现方法、生产 adapter registry 或 RLHF/DPO 路径已被覆盖。Ch72 已拥有 data→update→artifact→runtime 的安全与 release contract，故不重复写入。
- **当前正文承载：** `生命周期威胁` — ```text Data poisoning, leakage, license/provenance failure Training untrusted code, secret exposure, compromised dependency Artifact overwrite, substitution, unsafe deserialization, model theft Serving auth bypass, DoS, side channel, data exfiltration LLM/Agent prompt injection, insecure output handling, excessive agency ``` 单一 WAF 无法覆盖这条链。每次从一层向下一层传递，都需要验证 identity、integrity 和 authorization。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：把 fine-tuning attack surface 按 pre-tuning input/supply chain、during-tuning optimizer/update 与 post-tuning adapter/artifact 三个 intervention phase 组织，并用同一基座和协议检查跨 phase 防御组合。
- **Books：** `No Change — Existing Coverage`；owner 为 `PLATFORM-SECURITY` / [`books/part-06-ai-infrastructure/72-security.md`](../../../../books/part-06-ai-infrastructure/72-security.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25077 WorldCraft: From Camera Navigation to Object Manipulation in Interactive Video World Models](https://arxiv.org/html/2605.25077v1)

- **采用命题：** 用 camera-invariant Normalized World Trajectory 分离对象运动与相机位移，以 Spatial-Pathway LoRA 注入对象控制，并用 trajectory-anchored persistent state 在对象离屏后保留更新位置。
- **方法定位：** §3 Method: NWT, Spatial-Pathway LoRA and Trajectory-Anchored State Persistence
- **评价定位：** §4 Experiments, including camera/object control and state-persistence ablations
- **限制/反证：** Appendix D Limitations; pixel-world and trajectory-action boundary
- **证据边界：** WorldCraft: From Camera Navigation to Object Manipulation in Interactive Video World Models 的 exact-v1 只支持该文披露机制：We present WorldCraft, a framework that expands interactive video world models from camera navigation to object-level trajectory actions. 其未证明边界由 `Appendix D Limitations; pixel-world and trajectory-action boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **Books：** `Applied`；owner 为 `MULTIMODAL-WORLD-MODELS` / [`books/part-03-multimodal-world-models/25-multimodal-world-models.md`](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。Fresh non-author post-write semantic review passed; the paired binding remains before the first main H2 Review notes.

### [2605.25085 Polynomial Context-Truncation Sensitivity in Autoregressive Language Models: Sequential Wyner-Ziv Bounds for KV Cache Compression](https://arxiv.org/html/2605.25085v1)

- **采用命题：** We study the rate-distortion limits of online KV cache compression in autoregressive language models, formulating it as sequential Wyner-Ziv source coding on the filtration induced by the model, with the next-step query as decoder side information.
- **方法定位：** §3 formulation; §4 Main Theoretical Results on sequential Wyner–Ziv and suffix-only policies
- **评价定位：** §5 Empirical Validation; §6 Connections to Deployed Compression Schemes
- **限制/反证：** §7 Limitations, including architecture, rate-convergence and heavy-hitter boundaries
- **证据边界：** Polynomial Context-Truncation Sensitivity in Autoregressive Language Models: Sequential Wyner-Ziv Bounds for KV Cache Compression 的 exact-v1 只支持该文披露机制：We study the rate-distortion limits of online KV cache compression in autoregressive language models, formulating it as sequential Wyner-Ziv source coding on the filtration induced by the model, with the next-step query as decoder side information. 其未证明边界由 `§7 Limitations, including architecture, rate-convergence and heavy-hitter boundaries` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **Books：** `Applied`；owner 为 `INFER-KV-CACHE` / [`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25092 AgentIR: A Workload-Adaptive Cascade Retrieval Substrate for Long-Term Conversational Memory](https://arxiv.org/html/2605.25092v1)

- **采用命题：** 以 BM25 top-k margin 驱动无需重训的 cascade，逐 query 决定是否运行 dense channel/何种 fusion，并用 time-partitioned index 把增长中的长期记忆检索成本与 corpus size 解耦。
- **方法定位：** §3 System Design; §4 Optimizations; §5.9 Agent Memory Benchmark cascade router
- **评价定位：** §5 Evaluation, especially §5.9 LongMemEval and LoCoMo
- **限制/反证：** §6 Threats to validity and limitations; Appendix N Threats to Validity
- **证据边界：** AgentIR: A Workload-Adaptive Cascade Retrieval Substrate for Long-Term Conversational Memory 的 exact-v1 只支持该文披露机制：Long-term conversational memory is a retrieval workload classical IR was not built for: the index grows during the query stream, query types shift intra-session, and the latency budget per retrieval is sub-10 ms. 其未证明边界由 `§6 Threats to validity and limitations; Appendix N Threats to Validity` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **Books：** `Applied`；owner 为 `AGENT-MEMORY` / [`books/part-07-agent/77-memory.md`](../../../../books/part-07-agent/77-memory.md)。Fresh non-author post-write semantic review passed; the paired binding remains before the first main H2 Review notes.

### [2605.25133 Trust but Verify: Prover-Verifier Deliberation for Selective LLM Prediction](https://arxiv.org/html/2605.25133v1)

- **采用命题：** We introduce prover-verifier deliberation (PVD), an inference-time protocol grounded in interactive proof theory, as a mechanism for selective prediction: the protocol produces both an answer and a structured confidence verdict, allowing a system to report high-confidence answers while abstaining on uncertain cases.
- **方法定位：** §3 Prover-Verifier Deliberation protocol and algorithm
- **评价定位：** §4 Experiments; §5 Results on coverage-precision operating points
- **限制/反证：** §7 Limitations; verifier effective-region and no-formal-guarantee boundary
- **证据边界：** Trust but Verify: Prover-Verifier Deliberation for Selective LLM Prediction 的 exact-v1 只支持该文披露机制：We introduce prover-verifier deliberation (PVD), an inference-time protocol grounded in interactive proof theory, as a mechanism for selective prediction: the protocol produces both an answer and a structured confidence verdict, allowing a system to report high-confidence answers while abstaining on uncertain cases. 其未证明边界由 `§7 Limitations; verifier effective-region and no-formal-guarantee boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **当前正文承载：** `Confidence 最终服务于 Risk–Coverage Decision` — 系统不需要所有回答都达到 `100%`；它需要在错误和拒答之间做显式决策。若错误回答代价为 `C_wrong`，拒答/ 转人工代价为 `C_abstain`，回答的简化期望损失为： ```text Loss(answer)  = (1 - q_answer) * C_wrong Loss(abstain) = C_abstain ``` 只有当： ```text q_answer > 1 - C_abstain / C_wrong ``` 才值得直接回答。高风险场景提高 threshold，并把 critical claims 交给 executable verifier / expert；低风险探索可接受 较低 threshold。若要求整篇 critical claims 的 family-wise error 不超过 `delta`，union bound 给出保守预算： ```text P(any critical claim wrong) <= sum_i (1 - q_i) ``` 它会推动系统减少不必要 claims，而不是无限堆砌“有 90% 把握”的细节。Conformal prediction 可以在 calibration distribution 与 exchangeability 等假设下，为候选集合或 component 提供 coverage guarantee；distribution shift、错误 acceptability function 或 correlated adaptive sampling 仍会破坏解释，不能写成开放世界 truth guarantee。 最终可靠路径是： ```text answer draft → atomic claims + criticality / dependency graph → authoritative retrieval and source-family dedup → support / contradict / insufficient evidence → semantic / model / verifier uncertainty → claim and conclusion calibration → answer / omit detail / retrieve more / ask / abstain / escalate ``` 这条链把“模型感觉自己知道”降级为一个 feature，把 evidence 与 verifier 提升为独立 authority，再由风险政策决定 coverage。真正要优化的不是让 confidence 数字看起来更高，而是在相同 coverage 下减少 false answers，或在相同 risk 下回答更多问
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：We introduce prover-verifier deliberation (PVD), an inference-time protocol grounded in interactive proof theory, as a mechanism for selective prediction: the protocol produces both an answer and a structured confidence verdict, allowing a system to report high-confidence answers while abstaining on uncertain cases.
- **Books：** `No Change — Existing Coverage`；owner 为 `PLATFORM-EVALUATION-SYSTEM` / [`books/part-06-ai-infrastructure/66-evaluation-system.md`](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25160 SimuWoB: Simulating Real-World Mobile Apps for Fast and Faithful GUI Agent Benchmarking](https://arxiv.org/html/2605.25160v1)

- **采用命题：** 由 coding agent 合成可执行 mobile-app simulator，再独立生成 task 与 state validator，把 GUI agent benchmark 的 environment 和 outcome evidence 版本化。
- **方法定位：** §3 SimuWoB; §3.1 Environment generation; §3.2 Task and validator generation
- **评价定位：** §4 Experiments: app fidelity, task feasibility and GUI-agent evaluation
- **限制/反证：** §5 Limitations: visual-only interface, single-app tasks, no accessibility tree or cross-app workflow
- **证据边界：** 只覆盖视觉单应用 simulator；不等于真实 backend、跨应用状态或 accessibility-tree 行为。当前 Ch66/Ch81 已明确 environment generation、task constraint、validator 与 durable marker 分责，故不重复写入。
- **当前正文承载：** `Benchmark 生成器也会塑造被评估的任务人口` — 真实轨迹或仓库任务提供自然分布，却昂贵、含噪且难以冻结；合成任务可控制覆盖和重放，却会把 generator、 filter、tool rule 与 scorer 的偏好写进 benchmark。生成式 benchmark 不应只保存最终题目，还要保存： ```text source population and sampling frame → generator / transformation recipe → filter model and rejection reasons → no-tool / trivial-solution checks → verifier and answerability contract → accepted task population and excluded slices ``` Filter 提高可评分性时，也可能系统性删除长答案、弱工具可解或难以被 judge 解析的任务；post-hoc 单标签 failure taxonomy 则是诊断视图，不是因果 root cause。真实、手工策划与合成 benchmark 应共存，并用交叉执行、 人工抽查和版本化 population report 揭示各自盲区。AgentVista、ISO-Bench 与 SWE-rebench V2 分别提供了 Agent 任务生成、优化 patch 与可执行环境的受限证据，不能把其排行榜外推为开放部署能力。 跨语言派生 benchmark 还应被视为 semantics-preserving compilation，而不是普通字符串翻译。Compiler 必须保留 task invariant、label/choice identity、format/parser contract、language-specific invalid cases，并记录 source item 到 target item 的 transformation lineage。自动翻译扩大覆盖，却会改变难度、歧义、tokenization 和知识前提； 人工复核提高可信度但仍不能证明与源语言等价。原始 benchmark 在长期对比中继续成立，派生版本只能在逐项 validation、contamination 检查和独立 native review 后形成新 distribution。Recovered in Translation 为这条 pipeline 提供了受限证据，不支持跨语言分数直接互换。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：由 coding agent 合成可执行 mobile-app simulator，再独立生成 task 与 state validator，把 GUI agent benchmark 的 environment 和 outcome evidence 版本化。
- **Books：** `No Change — Existing Coverage`；owner 为 `PLATFORM-EVALUATION-SYSTEM` / [`books/part-06-ai-infrastructure/66-evaluation-system.md`](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25188 DarkForest: Less Talk, Higher Accuracy for Multi-Agent LLMs](https://arxiv.org/html/2605.25188v1)

- **采用命题：** 先保持 agents 独立生成，再把响应解析为候选簇，以 reliability、confidence、parse quality、support pattern 与独立性修正形成 belief distribution；coordinator 只接收 policy 允许的结构化证据而非原始推理串。
- **方法定位：** §3 DarkForest Design: calibrated belief, controlled disclosure and guardrail
- **评价定位：** §4 Evaluation; Appendix D ablations
- **限制/反证：** §6 Conclusion; no dedicated Limitations section; benchmark/model and coordinator boundary
- **证据边界：** DarkForest: Less Talk, Higher Accuracy for Multi-Agent LLMs 的 exact-v1 只支持该文披露机制：Multi-agent LLM systems improve reasoning by combining outputs from multiple agents, but interaction-heavy methods can introduce error propagation and high communication overhead. 其未证明边界由 `§6 Conclusion; no dedicated Limitations section; benchmark/model and coordinator boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **当前正文承载：** `扩展 Agent 数量之前，先测量 Coordination Tax` — Multi-Agent 的技术演进并不是从单 Agent 线性增加副本，而是： ```text single reasoning locus → independent parallel exploration → centralized verification → decentralized communication → task-dependent hybrid topology ``` 每一步解决不同边界。Independent 让可分解搜索并行，却缺少跨结果纠错；centralized verification 截断部分错误传播，但形成 bottleneck；peer communication 提供更多局部信息， 也会分裂全局 Context 并拉长 critical path。旧方案没有被后者否定：顺序约束强、工具密集或 单 Agent baseline 已较高时，统一 Context 往往比协调更重要。 一项覆盖六类交互 benchmark、五种 topology 和三个模型家族的 2026 研究，在固定工具、 prompt 与总 reasoning-token budget 下观察到强烈的 domain dependence：某些可分解任务受益， 顺序规划则显著退化；更密集通信在一定点后主要增加冗余。它支持本章的设计假设，但阈值、 回归系数和具体幅度只属于该实验配置，不能当作通用 scaling law。 因此架构选择应先测： ```text decomposability independence of evidence tool / environment coupling single-agent baseline headroom communication turns and bytes error absorption / amplification success per token and critical path ``` 关系属于 `Direct Evolution`：把“多 Agent 可能有用”的定性判断推进为可测量的 task-topology matching，同时保留单 Agent、deterministic verifier 和 workflow 作为长期 有效的较小系统。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：先保持 agents 独立生成，再把响应解析为候选簇，以 reliability、confidence、parse quality、support pattern 与独立性修正形成 belief distribution；coordinator 只接收 policy 允许的结构化证据而非原始推理串。
- **Books：** `No Change — Existing Coverage`；owner 为 `AGENT-MULTI-AGENT` / [`books/part-07-agent/82-multi-agent.md`](../../../../books/part-07-agent/82-multi-agent.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25189 Directional Alignment Mitigates Reward Hacking in Reinforcement Learning for Language Models](https://arxiv.org/html/2605.25189v1)

- **采用命题：** We study this failure mode through the geometry of reinforcement learning updates in language models and argue that hacking emerges when optimization drifts away from a stable low-dimensional learning trajectory.
- **方法定位：** §3–§5 dominant update directions, directional shift and trusted-direction method
- **评价定位：** §6 Experimental Setting; §7 Results
- **限制/反证：** Appendix A.1 Future Work; manuscript explicitly identifies itself as a preliminary study
- **证据边界：** Directional Alignment Mitigates Reward Hacking in Reinforcement Learning for Language Models 的 exact-v1 只支持该文披露机制：We study this failure mode through the geometry of reinforcement learning updates in language models and argue that hacking emerges when optimization drifts away from a stable low-dimensional learning trajectory. 其未证明边界由 `Appendix A.1 Future Work; manuscript explicitly identifies itself as a preliminary study` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **Books：** `Applied`；owner 为 `TRAIN-RLHF` / [`books/part-04-training-system/31-rlhf.md`](../../../../books/part-04-training-system/31-rlhf.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25233 Meta-Agent: From Task Descriptions to Verified Multi-Agent Systems](https://arxiv.org/html/2605.25233v1)

- **采用命题：** 把自然语言任务编译为带显式 I/O contract 与 verifier 的 agent DAG；construction-time gate 定点重生失败 artifact，execution-time gate 再以 local/upstream/structural attribution 选择 retry、局部重放或重分解。
- **方法定位：** §3 Method, especially §3.2 verification loop and error attribution
- **评价定位：** §4 Experiments and ablation study
- **限制/反证：** §4.5 Discussions; §5 Conclusion; no dedicated Limitations section
- **证据边界：** Meta-Agent: From Task Descriptions to Verified Multi-Agent Systems 的 exact-v1 只支持该文披露机制：We present Meta-Agent, a two-phase framework that automatically constructs and executes specialized multi-agent systems from natural-language task descriptions. 其未证明边界由 `§4.5 Discussions; §5 Conclusion; no dedicated Limitations section` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **当前正文承载：** `从一次性脚本到平台拥有的可编辑 DAG` — 自由代码生成适合探索新算子与一次性任务，因为它不要求平台预先拥有完整 operator catalog；但当结果需要被复用、可视化、协作编辑与恢复时，script 不再是足够的状态载体。更稳健的演进是让平台拥有带版本的 canonical DAG，Agent 只提交 typed mutation，backend 在 commit 前验证 schema、引用与无环性，executor 再用 run evidence 验证语义结果，visual editor 与 chat 只呈现同一 graph identity。 这条路线用 operator 生态约束换取可编辑性、审计与恢复；未知算子和短期探索仍可保留脚本分支。Skills 只是可更新的派生操作指南，既不拥有 DAG，也不能绕过平台验证。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：把自然语言任务编译为带显式 I/O contract 与 verifier 的 agent DAG；construction-time gate 定点重生失败 artifact，execution-time gate 再以 local/upstream/structural attribution 选择 retry、局部重放或重分解。
- **Books：** `No Change — Existing Coverage`；owner 为 `AGENT-WORKFLOW` / [`books/part-07-agent/81-workflow.md`](../../../../books/part-07-agent/81-workflow.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25240 JudgmentBench: Comparing Rubric and Preference Evaluation for Quality Assessment](https://arxiv.org/html/2605.25240v1)

- **采用命题：** 把 rubric score 与 pairwise preference 作为不同 measurement operators，在同一受控质量阶梯上比较各自一致性与区分力，而不是默认二者可互换。
- **方法定位：** §3.1 Dataset; §3.2 Constructed quality levels; §3.3 Rubric and pairwise-preference expert annotation
- **评价定位：** §4 Empirical comparison of rubric scoring and comparative judgment
- **限制/反证：** Appendix A.1 Limitations: legal-domain scope, prompt-induced quality confounds, style cues and mixed-trade-off cases
- **证据边界：** 证据主要来自法律文本和 prompt 构造的质量层级，质量与表达风格可能共变；不能据此规定所有 evaluator 都应采用同一判断形式。
- **Books：** `Applied`；owner 为 `PLATFORM-EVALUATION-SYSTEM` / [`books/part-06-ai-infrastructure/66-evaluation-system.md`](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25244 Inference Time Optimization with Confidence Dynamics](https://arxiv.org/html/2605.25244v1)

- **采用命题：** 正确 reasoning trajectory 的 confidence 往往沿程上升、错误轨迹则停滞或下降；CDG voting 把这种轨迹增益作为 answer-selection sensor，但它仍需与模型、任务和采样合同共同校准。
- **方法定位：** §3 Confidence Trajectories and Confidence Dynamic Gain voting
- **评价定位：** §5 Empirical Results and §5.3–§5.4 ablations/score analysis
- **限制/反证：** §6 Conclusion; Appendix A.2 simplified-training-model assumption; no dedicated Limitations section
- **证据边界：** Inference Time Optimization with Confidence Dynamics 的 exact-v1 只支持该文披露机制：In this paper, we investigate the dynamics of confidence along reasoning trajectories and for first time reveal a surprising and unique pattern: correct answer traces tend to exhibit confidence improvement over time (positive confidence gain), while incorrect traces show attenuated or declining confidence as reasoning proceeds. 其未证明边界由 `§6 Conclusion; Appendix A.2 simplified-training-model assumption; no dedicated Limitations section` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **当前正文承载：** `Selector 也要先证明“正确性信号可读”` — Majority vote 不只是一个便宜 baseline，它隐含“正确答案比任一错误答案更常出现”。困难问题可能进入相反的 modal-wrong regime：samples 的错误高度相关，增加 `N` 只会让错误 mode 的票数更稳定。Hidden-state selector 提供另一条分支——不根据答案出现次数，而从候选的内部表示读取一个 correctness ranking signal。 但 probe accuracy 很容易被 question identity 泄漏。若同一 question 的多个 candidates 被随机拆到 train/test， selector 可以学会“这是一道总体很难/很容易的题”，却仍无法在该题内部区分对错。真正与 selection decision 对齐的 measurement 应是： ```text group split by question → rank correct candidates above incorrect candidates within each question → compute leakage-free decodability on held-out questions → compare expected selector gain against voting / verifier cost ``` 只有当这条 within-question signal 在目标 model、layer、task、sampling policy 和 difficulty slice 上稳定可读，才启用 hidden-state selection；否则保留 majority、output-space score、独立 verifier 或 abstain。这个 gate 测的是 selector competence，不是候选本身的 truth probability，也不能授予最终 acceptance authority。 CASE 的作者实验为这条机制提供了受限证据：answer-token hidden state 的线性 readout 在部分 model/task 上可预测 selection 相对 voting 的收益，而在 signal 近 chance 的设置中不应启用；普通 random split 会显著高估 probe。论文 主要覆盖 multiple-choice、最终 answer token 与可取得 hidden state 的模型，阈值又依赖 difficulty distribution， 因此正文不保留固定 AUC、任务增益或“更大模型必然更可解码”的结论。 这形成一条条件演进，而不是单向替代： ```text majorit
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：正确 reasoning trajectory 的 confidence 往往沿程上升、错误轨迹则停滞或下降；CDG voting 把这种轨迹增益作为 answer-selection sensor，但它仍需与模型、任务和采样合同共同校准。
- **Books：** `No Change — Existing Coverage`；owner 为 `MODEL-SAMPLING` / [`books/part-02-model/20-sampling.md`](../../../../books/part-02-model/20-sampling.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25247 Kavier: Exploring Performance, Sustainability, and Efficiency of LLM Ecosystems under Inference through Cache-Aware Discrete-Event Simulation](https://arxiv.org/html/2605.25247v1)

- **采用命题：** 先建立 LLM inference ecosystem 的 reference architecture，再用 cache-aware discrete-event simulator 联合表示 KV/prefix cache、性能、成本与可持续性，并以真实 traces 校准后用于比较配置。
- **方法定位：** §4 Design of Kavier and cache-aware simulation modules
- **评价定位：** §6 Trace-Based Experiments with Kavier
- **限制/反证：** §6.7 Discussion; §7.2 Future Work; bachelor-thesis prototype and simulator-calibration boundary
- **证据边界：** Kavier: Exploring Performance, Sustainability, and Efficiency of LLM Ecosystems under Inference through Cache-Aware Discrete-Event Simulation 的 exact-v1 只支持该文披露机制：To improve the design and operation of LLM ecosystems, we envision simulators and simulation-based digital twins becoming primary decision-making tools. 其未证明边界由 `§6.7 Discussion; §7.2 Future Work; bachelor-thesis prototype and simulator-calibration boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **当前正文承载：** `Task-DAG Simulator 只能校准 Capacity Plan，不能承诺线上 SLO` — 单 query 的 TTFT/TPOT 无法表达多模型 Agent 的 tool wait、并行分支和下游 join。容量规划应把 task DAG、per-node model、 token shape、dependency、tool-time distribution 与资源拓扑冻结为 workload identity，再用 trace-driven simulation 比较 routing/placement 计划；最终 owner 是端到端 task completion 与 deadline，单节点指标只是子阶段证据。 仿真扩大了可比较配置，却会受 trace representativeness、相关到达、tool tail 与模型版本漂移影响。计划必须用线上 shadow/canary 校准，并在误差超界时回退保守 capacity、aging/FIFO 或实测 routing；作者 simulator 的有限任务和集群结果 不是生产容量保证。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：先建立 LLM inference ecosystem 的 reference architecture，再用 cache-aware discrete-event simulator 联合表示 KV/prefix cache、性能、成本与可持续性，并以真实 traces 校准后用于比较配置。
- **Books：** `No Change — Existing Coverage`；owner 为 `INFER-SCHEDULING` / [`books/part-05-inference-system/56-inference-scheduling.md`](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25252 Quantifying Empirical Compute-Supervision Tradeoffs in RLVR](https://arxiv.org/html/2605.25252v1)

- **采用命题：** 在受控 false-positive/false-negative verifier noise 与 rollout 数量下，额外 compute 呈锐减回报且不能消除监督差距；false negative 的损害更快，说明 verifier quality 与训练 compute 不能互换。
- **方法定位：** §3 Methodology: controlled false-positive/false-negative verifier noise and rollout scaling
- **评价定位：** §4 Results on compute-supervision tradeoffs
- **限制/反证：** §5 Conclusion; narrow Qwen2.5/GSM8K/GRPO setting and no dedicated Limitations section
- **证据边界：** Quantifying Empirical Compute-Supervision Tradeoffs in RLVR 的 exact-v1 只支持该文披露机制：Reinforcement learning with verifiable rewards (RLVR) has become a standard paradigm for post-training language models, but in practice, verifiers are rarely perfect. 其未证明边界由 `§5 Conclusion; narrow Qwen2.5/GSM8K/GRPO setting and no dedicated Limitations section` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **Books：** `Applied`；owner 为 `TRAIN-RLHF` / [`books/part-04-training-system/31-rlhf.md`](../../../../books/part-04-training-system/31-rlhf.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25272 AI Cartography: Mapping the Latent Landscape of AI Benchmark Ecosystems](https://arxiv.org/html/2605.25272v1)

- **采用命题：** 用 latent measurement model 分解 benchmark 共同因子与 task-specific variance，使 release evidence 能区分能力构念、数据生态和 leaderboard 聚合造成的相关性。
- **方法定位：** §2 Variance decomposition, confirmatory factor analysis, bifactor model and mixed-effects latent regression; §3 Experiment and data
- **评价定位：** §4 Results across six benchmark ecosystems
- **限制/反证：** § Limitations: one snapshot/six benchmarks, observational design, noisy metadata, non-representative sample and temporal instability
- **证据边界：** 只是一轮六 benchmark 的观察性快照；latent factor 不是能力本体，也不证明因果。模型、数据与提交策略变化后必须重新拟合而不能复用旧 factor。
- **Books：** `Applied`；owner 为 `PLATFORM-EVALUATION-SYSTEM` / [`books/part-06-ai-infrastructure/66-evaluation-system.md`](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25284 Knowing but Not Showing: LLMs Recognize Ambiguity but Rarely Ask Clarifying Questions](https://arxiv.org/html/2605.25284v1)

- **采用命题：** 模型在显式判断时常能识别歧义，却在普通 QA 中仍直接作答；检索上下文提高 answerability 的同时进一步降低澄清概率，因此 ambiguity recognition 与 ask/answer 行为必须分开评估。
- **方法定位：** §3 ambiguity-recognition and clarification protocol
- **评价定位：** §4 evaluation
- **限制/反证：** §5 limitations and prompt/model boundary
- **证据边界：** Knowing but Not Showing: LLMs Recognize Ambiguity but Rarely Ask Clarifying Questions 的 exact-v1 只支持该文披露机制：To study these abilities, we evaluate models on ambiguous, unambiguous, and disambiguated questions in three settings: standard question answering, explicit ambiguity judgment, and behavioral analysis, where a judge model classifies responses as direct answers, refusals, or clarifying questions. 其未证明边界由 `§5 limitations and prompt/model boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **当前正文承载：** `先校准不确定性，再决定行动、询问或探索` — 成本感知 planning 的关键并不是让模型输出一个置信度，而是把 prior、可获得 observation、action cost 与错误后果绑定到同一 decision contract： ```text calibrated prior over task state + expected information gain of ask / explore + action, delay and failure cost → act / ask / gather evidence / defer → update belief from an observed outcome ``` 合成环境中拟合的 prior 不能直接当作生产概率；cost 也不只是 token 数，还可能包括用户中断、工具价格、延迟与不可逆副作用。因此 expected utility policy 必须受 hard safety override、预算上限和低置信 fallback 约束，并按 deployment slice 重新校准。固定 rule 在样本少、概率失准或风险极高时继续合理；Calibrate-Then-Act 只为受控低维任务中的 uncertainty/cost-conditioned exploration 提供实验性证据，不证明现实 Agent 已获得全局最优行动策略。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：模型在显式判断时常能识别歧义，却在普通 QA 中仍直接作答；检索上下文提高 answerability 的同时进一步降低澄清概率，因此 ambiguity recognition 与 ask/answer 行为必须分开评估。
- **Books：** `No Change — Existing Coverage`；owner 为 `AGENT-PLANNING` / [`books/part-07-agent/79-planning.md`](../../../../books/part-07-agent/79-planning.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25292 DECICE: AI-Driven Scheduling and Digital Twin Integration for the Cloud-HPC-Edge Compute Continuum](https://arxiv.org/html/2605.25292v1)

- **采用命题：** 让 scheduler 消费由 Digital Twin 维护的 node power/carbon/anomaly state，并把 heterogeneous workflow 先转成正式 dependency/resource model，再输出 Kubernetes/Slurm placement。
- **方法定位：** §II Work Package Structure and Contributions: IAIS data flow, formal workflow mapping, Kubernetes/Slurm control manager and Digital Twin state
- **评价定位：** §III Evaluation Results: 10–5000 job/node scalability and solver/heuristic workflow comparison
- **限制/反证：** §IV Conclusion and project-report scope; component-level evaluation, heterogeneous project artifacts and no controlled end-to-end production SLO comparison
- **证据边界：** 论文是 DECICE 项目架构与组件结果汇总；5000×5000 scalability、solver runtime 和 production-like use cases 不是同一 end-to-end SLO 实验，也未证明 RNN/RL 优于所有启发式。Ch63–65 已覆盖 state-aware placement、carbon/energy signal、workflow dependency 与 Slurm/Kubernetes 边界，故不重复写入。
- **当前正文承载：** `Power Budget 是分层资源契约` — 只给每张 GPU 设置独立 power cap，在单租户、固定供电域中容易实施；机架、集群与租户同时受不同 上限约束后，局部调节可能让上层预算不可行。调度器需要在每个控制周期求一个满足层级 capacity、 租户 entitlement 与设备边界的可行分配，再把 setpoint 交给节点执行；budget owner 拥有约束， optimizer 只拥有分配 proposal，硬件 telemetry 反馈下一周期。该路径用求解与控制延迟换可组合预算， 并会引入测量漂移、不可行输入与震荡；规模小或预算独立时，静态 cap 仍更可靠。作者模拟/实验支持 其算法范围，不证明任意 GPU fleet 的功耗—性能关系或生产稳定性。 把 GPU 数量当唯一容量会遗漏供电链的四个不同 owner：设计 provisioning 决定理论上限，rack validation 证明安装边界，operational cap 留出可靠性余量，runtime scheduler 才能消费瞬时 swing。调度器应依据可用功率而非铭牌功率 admission，并保留测量延迟与降级策略；收益是提高基础设施利用率，代价是 telemetry、控制稳定性和故障域耦合。功率波动不可测或业务不能容忍 throttle 时，静态保守 cap 仍更合理。单个大规模集群的测量不能外推为所有硬件和冷却拓扑。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：让 scheduler 消费由 Digital Twin 维护的 node power/carbon/anomaly state，并把 heterogeneous workflow 先转成正式 dependency/resource model，再输出 Kubernetes/Slurm placement。
- **Books：** `No Change — Existing Coverage`；owner 为 `PLATFORM-GPU-SCHEDULER` / [`books/part-06-ai-infrastructure/63-gpu-scheduler.md`](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25298 Beyond Thread States: Diagnosing Performance Degradation with eBPF and Thread Dynamics](https://arxiv.org/html/2605.25298v1)

- **采用命题：** 从 thread-state 时间占比继续下钻到带 backing-resource identity 的 futex/pipe/socket/VFS/block-I/O dependency graph，并从 request entry thread 反向追踪 contention propagation。
- **方法定位：** §III Design; §IV-A eBPF metric collection; §IV-C Selective Thread Tracking and Algorithm 1
- **评价定位：** §V–§VI six data-intensive applications and CPU/disk/lock/external-service contention; Artifact Description/Evaluation
- **限制/反证：** §IV-C optimistic entry-point propagation assumption; §V single x86/Linux 6.8.12 host and six-application workload boundary
- **证据边界：** 选择性算法假设 degradation 能传播到可识别 entry thread；证据绑定单机 x86/Linux 6.8.12、六类应用与人工注入 contention，不能证明跨 kernel、GPU collective、容器隔离或无 socket entry 的训练作业同样可诊断。
- **Books：** `Applied`；owner 为 `PLATFORM-MONITORING` / [`books/part-06-ai-infrastructure/67-monitoring.md`](../../../../books/part-06-ai-infrastructure/67-monitoring.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25313 UWM-JEPA: Predictive World Models That Imagine in Belief Space](https://arxiv.org/html/2605.25313v1)

- **采用命题：** 用 joint system-environment density-matrix latent 与 unitary predictor 在 blind rollout 中保持表示的不确定性谱；同时证明 action sensitivity 依赖 counterfactual target，而不能由 teacher-forced context capacity 推出。
- **方法定位：** §3 UWM-JEPA belief-space dynamics
- **评价定位：** §4 world-model evaluation
- **限制/反证：** §5 limitations and environment/action boundary
- **证据边界：** UWM-JEPA: Predictive World Models That Imagine in Belief Space 的 exact-v1 只支持该文披露机制：We introduce the Unitary World Model JEPA (UWM-JEPA), a JEPA world model with a density-matrix latent on a joint system-environment space and a learned unitary predictor. 其未证明边界由 `§5 limitations and environment/action boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。
- **当前正文承载：** `Latent Geometry 不等于 Planning Cost` — Latent space 的距离也不天然等于规划代价。若只用 Euclidean proximity，两个视觉上接近但动力学不可达的状态可能被错误排序；一条条件分支可从离线轨迹的先后关系学习 directed temporal distance，并让 rollout consistency 对齐 plan horizon。Representation owner 生成候选 progress cost，planner 只在 locked evaluation 与真实 transition refresh 通过后消费它，不能把时间共现直接当可达性真值。 这种方法利用弱顺序监督换更贴近控制的表示，却依赖轨迹覆盖、负例构造和 horizon；contact-rich、跨轨迹捷径或反向不可达会制造错误 cost。证据不足时保留几何 cost、显式 simulator 或短 horizon replanning。现有实验支持作者任务中 directed head、negative 与 consistency term 的受控贡献，不证明所有环境都应弃用 Euclidean geometry。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：用 joint system-environment density-matrix latent 与 unitary predictor 在 blind rollout 中保持表示的不确定性谱；同时证明 action sensitivity 依赖 counterfactual target，而不能由 teacher-forced context capacity 推出。
- **Books：** `No Change — Existing Coverage`；owner 为 `MULTIMODAL-WORLD-MODELS` / [`books/part-03-multimodal-world-models/25-multimodal-world-models.md`](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25333 Teaching Video Generators to Remember: Eliciting Dynamic Memory for Out-of-Sight State Evolution](https://arxiv.org/html/2605.25333v1)

- **采用命题：** 流式视频 KV cache 只有在条目保留原始时间/相机 identity，且训练显式暴露局部观测失效到历史可靠锚点的非局部恢复边时，才会从容量缓冲演进为动态状态记忆；仅扩大 cache 不会自动学会选择可靠历史。
- **方法定位：** §3.2 PM-RoPE; §3.3 Dynamic Memory with Streaming KV Cache; §3.4 Training Scheme for Dynamic Memory
- **评价定位：** §4.1–§4.4 STEVO-Bench/VBench, component ablations and KV-importance diagnostics
- **限制/反证：** §5 Conclusion and Limitation: bounded interruption types; camera/depth quality and pose-error boundary
- **证据边界：** exact-v1 证明的是作者 video diffusion backbone、camera/depth pipeline、STEVO-Bench/VBench 与受控 interruption 下的非局部历史检索机制；它不解决全部物理推理，camera/depth/pose error 会污染监督，也不证明生成 cache 是环境事实、开放世界状态或安全控制 authority。失败时回退显式 state memory、短窗口重算或新 observation 校正。
- **当前正文承载：** `Memory 架构为何从静态 cache 演进` — 短视频可缓存最近 frames 或 KV；视角反复切换、物体离开画面再返回时，单一短窗口会遗忘状态。正文已把 recent-frame cache → view-indexed/static-dynamic memory → transition-aware persistent belief 写成演进，并明确 cache placement 不能替代 world-state semantics。
- **差异判断：** ReMind 提供 original-position/camera-aware KV addressing、node-drop/noisy-memory/reference-cache curriculum 与受限 recovery evidence，但没有改变正文既有的 dynamic-memory owner、观测校正、stale-state 与 fallback 判断。
- **Books：** `No Change — Existing Coverage`；owner 为 `MULTIMODAL-WORLD-MODELS` / [`books/part-03-multimodal-world-models/25-multimodal-world-models.md`](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。Main-body heading/excerpt before the first H2 Review notes already carries the durable proposition; exact difference is recorded.

### [2605.25338 CausalFlow: Causal Attribution and Counterfactual Repair for LLM Agent Failures](https://arxiv.org/html/2605.25338v1)

- **采用命题：** We introduce CausalFlow, an interventional framework that converts failed agent traces into minimal counterfactual repairs and reusable supervision.
- **方法定位：** §3 Problem Setup; §4.1–§4.3 causal attribution, counterfactual repair and multi-agent validation
- **评价定位：** §5–§6 intervention protocol, repair performance, minimality and ablations
- **限制/反证：** §7 Discussion; Appendix A.10 Runtime Analysis; Appendix B Future Work
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `Harness、Protocol 与 Credit 都是 Platform-owned Artifact` — 生成代码若只是最终文本，reviewer 无法知道哪些 invariant 在演化中持续成立。Protocol-driven 分支把允许的 state transition、test/evidence obligation 与 release rule 版本化，代码只是其一个 materialization。平台拥有 protocol 和 receipt，Agent 只能提议 mutation。它以更强可审计性换取协议维护和不完备规格；探索性原型仍可先 code-first，但进入 持久系统前必须补齐可执行 contract。 同一模型在不同 file view、tool schema、feedback loop 和 completion proof 下会形成不同工程能力，因此 harness 不是 外围脚本，而是 versioned runtime substrate。Run identity 要绑定 observation policy、action adapter、environment、 feedback 与 done verifier；模型升级和 harness 升级必须分开归因。更强 harness 会扩大权限和隐性状态，失败时应回退 最小工具集与可执行测试。案例只证明 system-level contribution，不能把模型能力与 harness 能力互换命名。 系统级 reward 无法直接说明哪个 Agent、prompt 或 tool policy 应更新。对同一 query 比较多个 joint configuration， 可生成 contrastive per-component credit proposal；但 attribution owner 必须保存配置差异和共同环境，训练或发布 Gate 再决定是否消费。收益是减少盲目整体搜索，代价是组合 rollout 成本、interaction confounding 与错误归因。强耦合任务 或样本不足时，保留 system-level ablation 和人工 owner review。 Agent Platform 同时面对多个时间尺度： | 调度层 | 对象 | | --- | --- | | Inference runtime | token、batch、KV | | GPU/cluster | Pod、gang、device | | Agent runtime | ready steps、tools、approvals、deadlines | | Workflow/platform | runs、tenants、budgets、priorities | Agent waiting 不应占用模型/GPU。Runtime 可在 event 到来时重新组装 Context
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：We introduce CausalFlow, an interventional framework that converts failed agent traces into minimal counterfactual repairs and reusable supervision.
- **Books：** `No Change — Existing Coverage`；owner 为 `AGENT-PLATFORM` / [`books/part-07-agent/84-agent-platform.md`](../../../../books/part-07-agent/84-agent-platform.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25375 Bandwidth-Aware and Cost-Efficient Pipeline Parallel Scheduling in Geo-Distributed LLM Training](https://arxiv.org/html/2605.25375v1)

- **采用命题：** 以动态 job priority、bandwidth-aware cross-region pathfinder 与按电价分配 GPU 的 allocator 联合控制 geo-distributed pipeline training，避免 HoL blocking 并把 JCT、链路约束和电力成本纳入同一计划。
- **方法定位：** §III problem definition; §III-B dynamic priority, bandwidth pathfinder and cost allocator
- **评价定位：** §IV-A–§IV-E geo-cluster setup, bandwidth/GPU/workload sensitivity and ablation
- **限制/反证：** §II-A prior limitations; §V conclusion; evidence is simulator/trace-bound
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `TRAIN-PIPELINE-PARALLEL` / [`books/part-04-training-system/38-pipeline-parallel.md`](../../../../books/part-04-training-system/38-pipeline-parallel.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25376 KYA: A Framework-Agnostic Trust Layer for Autonomous Systems with Verifiable Provenance and Hierarchical Policy Composition](https://arxiv.org/html/2605.25376v1)

- **采用命题：** KYA (Know Your Agents) is an open-source, framework-agnostic trust and governance layer for autonomous systems, composed of five primitives: (1) a four-gate inbound apply pipeline; (2) an only-tighten composition algebra over a three-channel multi-tenant hierarchy; (3) KYP (Know Your Principal), a schema-level unification of trust scoring across human users, AI agents, and service accounts; (4) auditable interaction-multiplier amplification over an AIVSS-shaped additive baseline; and (5) two-axis delegation attribution: a static premium for risky delegates and a runtime debit for actual delegate misbehavior in multi-agent fan-out.
- **方法定位：** §2 threat model; §3 three-layer runtime gates; §5 dynamic rogue signals; §6 evidence chain
- **评价定位：** §4.4 worked fleets; §8–§10 evaluation, red-team and performance sections
- **限制/反证：** §4.5 calibration and limitations; §11 limitations and threat-model boundary
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `Agent 授权必须沿 Delegation Chain 单调收窄` — 授权不仅约束 `use`，还应分别约束 `read` 与 `transmit`。某 principal 可以读取资料，不代表可以把内容放进模型 Context；允许在本地推理，也不代表可以发送给外部 provider 或下游 Tool。每条数据边因此绑定用途、目标与可见字段，拒绝发生在 materialization 之前。分权会降低便利性与 cache reuse，却阻止“已经能看见”被错误升级为任意传播权。<!-- semantic-body-binding:SF-2026-ARXIV-2608-20658 --> 当调用经过第三方 provider、重试和恢复路径时，authorization 还要一直延续到最终 delivery fence：请求 revision、目标 endpoint、幂等键、允许的 side effect 与完成 receipt 必须一致。只在最初 proposal 检查一次，会让 failover 或 retry 把动作提交到不同主体或重复执行。严格 fence 增加拒绝与协调成本；不可证明当前 effect 状态时应转人工 reconciliation。<!-- semantic-body-binding:SF-2026-ARXIV-2608-21159 --> 静态 RBAC 假定 principal 长期存在、动作集合预先可知；Agent 会临时创建子任务并继续委派。每次 delegation 应携带上游 principal、允许的 effect vocabulary、预算与 session state，后续能力只能收窄，不能因组合多个局部权限而重新获得更大 authority。外部 enforcement point 在 effect 前做 composition check，并在事后留下可验证审计链。 该机制依赖 policy 完整性和可靠 identity，会增加 critical-path latency；fail-closed 还会把控制面故障转成拒绝服务。低风险、只读或单步骤任务仍可使用较简单的 capability token，但 prompt 中的“允许”永远不能替代外置授权。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：KYA (Know Your Agents) is an open-source, framework-agnostic trust and governance layer for autonomous systems, composed of five primitives: (1) a four-gate inbound apply pipeline; (2) an only-tighten composition algebra over a three-channel multi-tenant hierarchy; (3) KYP (Know Your Principal), a schema-level unification of trust scoring across human users, AI agents, and service accounts; (4) auditable interaction-multiplier amplification over an AIVSS-shaped additive baseline; and (5) two-axis delegation attribution: a static premium for risky delegates and a runtime debit for actual delegate misbehavior in multi-agent fan-out.
- **Books：** `No Change — Existing Coverage`；owner 为 `PLATFORM-SECURITY` / [`books/part-06-ai-infrastructure/72-security.md`](../../../../books/part-06-ai-infrastructure/72-security.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25379 StateRAG: Typed State Contracts for Complex Retrieval-Augmented Generation](https://arxiv.org/html/2605.25379v1)

- **采用命题：** We introduce StateRAG, which represents retrieval control as a typed state external to the final reader.
- **方法定位：** §1.2 structured retrieval state; §3 tree memory, adaptive routing, MARS/SMP and access control
- **评价定位：** §4 datasets, main results, component ablation and verifier-guided recovery
- **限制/反证：** §5 Limitations; Appendix A.4 efficiency accounting; Appendix F.3 failure modes
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `AGENT-RAG` / [`books/part-07-agent/76-rag.md`](../../../../books/part-07-agent/76-rag.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25389 Evo-Attacker: Memory-Augmented Reinforcement Learning for Long-Horizon Tool Attacks on LLM-MAS](https://arxiv.org/html/2605.25389v1)

- **采用命题：** 把长程 tool attack 建模为带动态 attack memory 的强化学习过程，并用 Attack-Flow GRPO 从 terminal outcome 向中间干预分配 credit；它暴露的是 tool-output trust surface，不授权把攻击策略当通用能力。
- **方法定位：** §2 threat model; §3.1–§3.3 attack memory, memory-augmented attack and Attack-Flow GRPO
- **评价定位：** §4 main, ablation, stealth and cross-model experiments
- **限制/反证：** §6 Conclusion; Appendix C framework/dataset/training scope
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `外部化 Attack/Defense Memory 需要 Provenance Gate` — 持续安全若只依赖重新训练权重，更新慢且难以审计。把 attack patterns、defense rules 和反例保存在可检查的外部结构中，可让红队发现快速进入防护 loop；但检索和更新策略必须版本化，模型只能提出、不能自动批准长期防御。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13411 --> 长期运行 Agent 还会从消息、memory、自写 skill 和 scheduler 接收跨时刻输入；一次 prompt injection 可作为 sleeper channel 留存并在未来触发，因此写入时就要进行 provenance、权限和有效期检查。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13471 --> 外部记忆会积累污染与过期规则。来源不明、规则冲突或命中分布漂移时，应隔离条目、回退稳定 policy bundle，并要求人工批准。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：把长程 tool attack 建模为带动态 attack memory 的强化学习过程，并用 Attack-Flow GRPO 从 terminal outcome 向中间干预分配 credit；它暴露的是 tool-output trust surface，不授权把攻击策略当通用能力。
- **Books：** `No Change — Existing Coverage`；owner 为 `PLATFORM-SECURITY` / [`books/part-06-ai-infrastructure/72-security.md`](../../../../books/part-06-ai-infrastructure/72-security.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25421 HyLaT: Efficient Multi-Agent Communication via Hybrid Latent-Text Protocol](https://arxiv.org/html/2605.25421v1)

- **采用命题：** 用 latent channel 承载高带宽认知状态、用短文本承载关键可解释信号，并通过单 agent hybrid generation 与多 agent interactive co-training 学习多轮双向混合通信。
- **方法定位：** §2.2–§2.4 dual-channel protocol, cross-channel alignment and interactive co-training
- **评价定位：** §3–§4 task/metric setup, ablation, compatibility, robustness and scale analysis
- **限制/反证：** §6 Conclusion; Appendix B model-family/scale boundary
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `Latent Communication 只能压缩 Payload，不能隐藏 Identity` — 文本消息可审计但 token/latency 成本高；共享模型族可传 latent cache 以复用中间表示，但通信 owner 仍须记录发送者、模型 revision、shape、生命周期与 fallback text。收益是减小通信，代价是版本耦合、不可解释和跨模型失配；审计或异构优先时回退显式消息。<!-- source-family:SF-2026-ARXIV-2605-22863 --> exact-v1 §3–4 与 Appendix C 支持其 latent-cache 机制，§5 不证明跨模型互操作或语义等价。 异构 Agent 之间即使都使用 KV，也不能把 sender cache 当作 receiver state。跨模型通信必须经过有版本的 cache transform；identity 至少绑定 sender/receiver model、tokenizer、layer/layout、可见输入和 transform-training revision。Transform 只生成 derived state，receiver 仍拥有最终 reasoning 与 action；context-unaware transfer 需要携带更密的 contextual state，不能假设接收者已看到相同 prompt。 这种对齐减少文本重编码，却增加训练、模型升级耦合、不可解释错误和 cache 形状兼容成本。跨模型校准失败、身份不符或审计要求可读时，应回退文本消息。作者只验证 Qwen3 三种规模的六个方向和有限 benchmark，不证明跨架构、跨 tokenizer 或生产网络下普遍优于文本。 显式文本 handoff 在异构、审计优先时仍是可解释基线；两个模型若在每个 generation step 通过可训练 interface 双向交换 hidden state，通信 plane 就从异步消息变成 lockstep causal state。Interface 只拥有 payload transform 与 suppression gate，两个 frozen LM 分别拥有自己的生成状态，tool runtime 仍拥有 effect commit；哪一步看到哪段 tool output、何时注入 residual，必须随 causal schedule 一起版本化。 这种 latent coupling 降低文本序列化开销，却可能近似翻倍模型 compute，并新增同步阻塞、不可解释通信、负迁移与 task-specific causal annotation。能力互补不清、因果放置无法证明或审计要求可读时，应回退显式 typed message、异步协作或单模型 tool loop。exact-v1 只支持作者的 ca
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：用 latent channel 承载高带宽认知状态、用短文本承载关键可解释信号，并通过单 agent hybrid generation 与多 agent interactive co-training 学习多轮双向混合通信。
- **Books：** `No Change — Existing Coverage`；owner 为 `AGENT-MULTI-AGENT` / [`books/part-07-agent/82-multi-agent.md`](../../../../books/part-07-agent/82-multi-agent.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25422 A Token/KV-Cache Communication Media Selection and Resource Allocation Strategy for Multi-Agent Collaboration](https://arxiv.org/html/2605.25422v1)

- **采用命题：** 把 token/KV-cache communication medium 与 wireless bandwidth allocation 联合优化；没有一种 medium 在所有 compute/channel regime 都占优，media identity 与资源状态必须共同进入 E2E latency 决策。
- **方法定位：** §3 system model; §4 token/KV latency; §5.1–§5.2 constrained mode and bandwidth optimization
- **评价定位：** §5.3 numerical validation and multi-round mode switching
- **限制/反证：** §6 Conclusion and Future Work; wireless/model assumptions bound generality
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `AGENT-MULTI-AGENT` / [`books/part-07-agent/82-multi-agent.md`](../../../../books/part-07-agent/82-multi-agent.md)。Fresh non-author post-write semantic review passed; the paired binding remains before the first main H2 Review notes.

### [2605.25424 SeqRoute: Global Budget-Aware Sequential LLM Routing via Offline Reinforcement Learning](https://arxiv.org/html/2605.25424v1)

- **采用命题：** We introduce SeqRoute, a framework that formulates multi-turn routing as a finite-horizon Markov Decision Process and solves it via offline reinforcement learning.
- **方法定位：** §3 session-budget MDP; §4.1–§4.3 HBR, CQL and deployment lambda-sweep
- **评价定位：** §5 cost-safety frontier, delayed-gratification and ablation experiments
- **限制/反证：** §6 Conclusion; offline reward proxy, single model pair and fixed-cost assumptions
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `INFER-SCHEDULING` / [`books/part-05-inference-system/56-inference-scheduling.md`](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25430 CODESKILL: Learning Self-Evolving Skills for Coding Agents](https://arxiv.org/html/2605.25430v1)

- **采用命题：** 把 trajectory→skill extraction、evolution 与 compaction 从固定 prompt 提升为带 verifier reward 的可学习 lifecycle policy。
- **方法定位：** §3.1 Skill extraction; §3.2 learnable skill-bank maintenance; §3.3 RL objective
- **评价定位：** §4 EnvBench, SWE-Bench Verified and Terminal-Bench 2; iterative-bank ablations
- **限制/反证：** §5/Appendix: frozen downstream agent, benchmark and verifier-reward boundary
- **证据边界：** 只支持 CODESKILL: Learning Self-Evolving Skills for Coding Agents exact-v1 披露的方法与 evaluation envelope；未测试的模型、硬件、并发、tail-SLO、攻击分布和生产泛化均未证明。
- **Books：** `Applied`；owner 为 `AGENT-PLATFORM` / [`books/part-07-agent/84-agent-platform.md`](../../../../books/part-07-agent/84-agent-platform.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25451 BigMac: Breaking the Pareto Frontier of Compute and Memory in Multimodal LLM Training](https://arxiv.org/html/2605.25451v1)

- **采用命题：** 把 multimodal encoder 与 generator 以 dependency-safe nested pipeline 嵌入 LLM pipeline，使二者 activation memory 为 O(1)，同时避免用降低计算利用率来换显存。
- **方法定位：** Project artifact: dependency-safe nested pipeline; global operator-table schedule; scheduler/executor separation; PP-transparent interface; schedule-aware profiler/simulator
- **评价定位：** Project artifact: Qwen3-30B-A3B + 1.3B ViT; second workload adds 20B MMDiT; 8K sequence; comparison with Optimus/Megatron-DistTrain
- **限制/反证：** No explicit Limitations section; hardware, precision, topology, concurrency and tail-SLO are Not Disclosed on the accessible artifact
- **证据边界：** Author-hosted artifact verifies the disclosed BigMac mechanism and workloads, but not the inaccessible paper body or a universal compute-memory Pareto advantage.
- **Books：** `Applied`；owner 为 `TRAIN-PIPELINE-PARALLEL` / [`books/part-04-training-system/38-pipeline-parallel.md`](../../../../books/part-04-training-system/38-pipeline-parallel.md)。Fresh non-author post-write semantic review passed; the paired binding remains before the first main H2 Review notes.

### [2605.25475 IndexMem: Learned KV-Cache Eviction with Latent Memory for Long-Context LLM Inference](https://arxiv.org/html/2605.25475v1)

- **采用命题：** 用 learnable indexer 预测 KV importance，同时把被逐出的 token 压入在线更新的 latent memory 并提供 residual readout，从而把 bounded KV residency 与不可逆遗忘分开。
- **方法定位：** §3.1 learned token indexer; §3.2 latent fast/slow-weight memory
- **评价定位：** §4 RULER, NIAH, LongBench, compression and ablation
- **限制/反证：** §6 Conclusion & Limitation; Appendix A limited budgets, models and frozen backbone
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `INFER-KV-CACHE` / [`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。Fresh non-author post-write semantic review passed; the paired binding remains before the first main H2 Review notes.

### [2605.25492 SafetyRepro: Configuration-Conditional Rank Instability on Alignment Benchmarks](https://arxiv.org/html/2605.25492v1)

- **采用命题：** Pairwise model comparisons drawn from foundation-model benchmarks ("A is safer than B") are read as quantitative verdicts but hinge on harness choices benchmark papers under-specify.
- **方法定位：** §3 configuration grid; §4 SDI/CFR/rank-concordance/variance metrics
- **评价定位：** §5 configuration-conditional reversals and cross-package analysis
- **限制/反证：** §6 Threats to Validity: narrow model/benchmark/envelope and qualitative variance attribution
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `PLATFORM-EVALUATION-SYSTEM` / [`books/part-06-ai-infrastructure/66-evaluation-system.md`](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25507 Credit Assignment with Resets in Language Model Reasoning](https://arxiv.org/html/2605.25507v1)

- **采用命题：** 从整条 trajectory 共用 outcome reward 演进到 intermediate-state reset 与 counterfactual suffix 的局部 credit assignment。
- **方法定位：** §3 Conservative Policy Iteration with reset credit; §4 RRPO and SRPO
- **评价定位：** §5–§6 reasoning benchmarks, GRPO/RRPO/SRPO comparison and reset ablations
- **限制/反证：** §7 Limitations: self-localized error and verifiable-reward reasoning scope
- **证据边界：** 只支持 Credit Assignment with Resets in Language Model Reasoning exact-v1 披露的方法与 evaluation envelope；未测试的模型、硬件、并发、tail-SLO、攻击分布和生产泛化均未证明。
- **Books：** `Applied`；owner 为 `TRAIN-PPO` / [`books/part-04-training-system/32-ppo.md`](../../../../books/part-04-training-system/32-ppo.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25521 CS-PQ: Cache-Friendly SIMD Product Quantization for Large-Scale ANNS Index Construction](https://arxiv.org/html/2605.25521v1)

- **采用命题：** 沿 PQ centroids 而非 subvector dimension 做 SIMD vectorization，并重排 pipeline 提升 cache locality、消除冗余计算，使 CPU index construction 的数据移动与计算粒度共同受控。
- **方法定位：** §3 motivation; §4 centroid-parallel SIMD, cache organization and ranking-preserving reformulation
- **评价定位：** §5 setup, end-to-end, microbenchmark, ablation and microarchitecture evidence
- **限制/反证：** §7 Conclusion; evaluated CPU/PQ construction boundary
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `多向量检索的数据面要避免搬运高精度向量` — 多向量匹配需要细粒度表示，却容易让 CPU 驻留的高精度向量在每次查询时跨总线搬到 GPU，计算加速最终被数据移动抵消。异构执行可以让 GPU 常驻低精度 codes 做 candidate generation 与过滤，再由 CPU 上的高精度数据完成 refinement，并重叠两侧计算。它以额外副本、量化误差和一致性管理换取低延迟；验收必须在相同 recall 下报告 host/device memory、传输量、QPS 与尾延迟，不能只比较 kernel 时间。 混合 text/graph RAG 不应只拼接两路结果。Graph-to-text 通道可用已访问节点为文本证据投票降噪；text-to-graph 通道则把 search history 中被 beam pruning 的 orphan nodes 保存为带 provenance 的 deferred search state，并在文本线索支持时重开。该机制用历史状态与双向校验换 recall/precision，代价是 stale graph、错误 resurrection 与额外融合控制；identity/provenance 不完整时回退独立 text/graph 检索与显式 rerank。 作者仅报告多个 multi-hop benchmark 的相对结果，摘要未披露完整模型、硬件、并发或生产 freshness 条件；不证明通用最优融合。 PLATFORM-SECURITY 只接收 poisoning/authorization handoff；RAG 章节拥有检索状态与证据 admission。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：沿 PQ centroids 而非 subvector dimension 做 SIMD vectorization，并重排 pipeline 提升 cache locality、消除冗余计算，使 CPU index construction 的数据移动与计算粒度共同受控。
- **Books：** `No Change — Existing Coverage`；owner 为 `AGENT-RAG` / [`books/part-07-agent/76-rag.md`](../../../../books/part-07-agent/76-rag.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25522 Co-Designing Graph-based Approximate Nearest Neighbor Search at Billion Scale for Processing-in-Memory](https://arxiv.org/html/2605.25522v1)

- **采用命题：** 十亿级 graph ANNS 迁移到 PIM 不能只下沉距离计算：index footprint、跨 PU graph traversal、host coordination 与弱算力必须联合 co-design；compact index 和异步 mini-batch pipeline 会把瓶颈转移到 host rerank/transfer，并形成overfetch–recall–throughput 的显式边界。
- **方法定位：** §II-C co-design challenges; §IV-A compact index; §IV-B asynchronous pipeline; §IV-C multiplication-free kernel
- **评价定位：** §V-A–§V-E: three billion-scale datasets, CPU/GPU/PIM baselines, ablations and scalability
- **限制/反证：** No dedicated Limitations section; §V-D shows host rerank/transfer domination and overfetch trade-off; §V-E scale-out/emerging-PIM results include simulation/projection beyond the measured UPMEM system
- **证据边界：** exact-v1 的端到端证据绑定三套 billion-scale datasets、披露的 dual-Xeon/A100/UPMEM 配置和 recall@10；host rerank 已成为主要瓶颈，multi-node/emerging-PIM 部分含模拟或投影，不能外推到任意 index、硬件、并发或生产尾延迟。容量、互联或 recall contract 不满足时应回退 CPU/GPU 或既有 ANN 数据面。
- **Books：** `Applied`；owner 为 `AGENT-RAG` / [`books/part-07-agent/76-rag.md`](../../../../books/part-07-agent/76-rag.md)。Root 已在主 `## Review notes` 前写入唯一 paired semantic-body binding；fresh non-author 已终审语义与位置。

### [2605.25535 Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-horizon Agents](https://arxiv.org/html/2605.25535v1)

- **采用命题：** 以 session-level storage gate 学习 user-specific retention policy，选择性跳过短暂会话；理想个性化可改善有限预算下的保留，但准确 gating 仍是未解决边界。
- **方法定位：** §3–§4 static/dynamic PerMem-Bench; §7.1 session-level personalized storage gating
- **评价定位：** §5 meta-evaluation; §6 protocol; §7.2 memory-system results
- **限制/反证：** §8 Conclusion; appendix construction/judge/checkpoint-sampling boundaries
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `个性化更新与事实可靠性是两套策略` — 用户在行动前澄清需求，与在看到结果后修正偏好，写入语义并不相同。前者缩小当前 action 的歧义，后者可能使旧 preference 失效。Memory service 因此不能把所有 feedback 合并成一段 persona，而应保存： ```text feedback source and consent + preference scope / subject + valid time and expiry + action or outcome that triggered it + supersedes / conflicts-with relation ``` 参数化个性化也必须分离“用户事实”与“如何使用事实”。如果每位用户都持有一整份 LoRA，身份内容、推理能力与 base-model drift 会混在同一不可寻址对象中，撤销和迁移都很困难。一种更清楚的边界是把用户内容写入局部、hash-addressed rows，共享 adapter 只承载通用 reasoning；memory service 持有 row identity、consent、版本与删除，模型只在明确用户作用域中读取。 这种表示减少 per-user adapter 成本并允许组合，但新增 hash collision、row growth、base migration 和删除证明问题，也不能保证任意事实都能忠实写入参数。需要来源追踪、频繁更正或强删除证明时，external memory 仍是主路径；parametric row 只承担低延迟、受限的派生状态。 文档级 parametric memory 也不必压进一个 monolithic adapter。可以把每份文档编译成带 semantic type 与 provenance key 的 micro-LoRA atom，由 query router 只选择候选 atoms、composer 形成 query-specific adapter，冻结 base model 再执行。Atom identity 必须绑定 source revision、compiler、base-model revision 与组合顺序；router 只拥有选择 proposal，memory service 保留来源、撤销和冲突处理。 细粒度组合减少整文档重训和无关参数干扰，却新增 router miss、atom conflict、组合非交换性与 base migration。来源需要逐句引用、文档频繁更新或组合校验失败时，应回退原文 retrieval/完整 context；有限 QA 结果不能证明参数原子忠实保存全部文档事实。 自动 merge 可以减少下一次询问，却会引入 stale preference、过度个性化
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：以 session-level storage gate 学习 user-specific retention policy，选择性跳过短暂会话；理想个性化可改善有限预算下的保留，但准确 gating 仍是未解决边界。
- **Books：** `No Change — Existing Coverage`；owner 为 `AGENT-MEMORY` / [`books/part-07-agent/77-memory.md`](../../../../books/part-07-agent/77-memory.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25537 Action-Prior Denoising for Smooth Real-Time Chunking](https://arxiv.org/html/2605.25537v1)

- **采用命题：** Soft RTC 用部分去噪的 overlap state 与上一 action chunk 构造 action prior，让已提交前缀保持固定、后续 overlap 仍可编辑，从而在不引入昂贵部署 guidance 时降低动作跳变。
- **方法定位：** §III problem; §IV-A action-prior denoising; §IV-B inference blending
- **评价定位：** §V–§VI Kinetix setup, real-robot pilot and delay/window sweeps
- **限制/反证：** §VII Discussion; small real-robot pilot and policy/workload scope
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `Action Chunk 是控制闭环的时间契约` — 逐步 action 每次都读取最新 observation，适合高扰动环境，但推理频率和通信成本高；更长 action chunk 能摊薄模型调用，却把一次感知误差锁进更长 open-loop interval。Chunk horizon 因而不能是孤立超参，它必须与 observation watermark、controller correction budget、安全中断点和 model revision 一起版本化，低层 controller 拥有逐步执行与紧急停止权，高层 VLA 只提交 provisional trajectory。 更长 chunk 获得吞吐和动作连贯性，代价是 stale perception、误差累积与中断延迟；环境变化快、接触操作精细时应缩短 chunk 或回退逐步控制。arXiv:2605.22493v1 的方法和实验只支持作者任务、policy 与控制设置，不证明固定最优 horizon 可跨机器人、传感器和安全 envelope 迁移。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：Soft RTC 用部分去噪的 overlap state 与上一 action chunk 构造 action prior，让已提交前缀保持固定、后续 overlap 仍可编辑，从而在不引入昂贵部署 guidance 时降低动作跳变。
- **Books：** `No Change — Existing Coverage`；owner 为 `MULTIMODAL-EMBODIED-VLA` / [`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25547 TapSampling: Inference-Time Sampling with a Task-Progress-Understanding Verifier for Robotic Manipulation](https://arxiv.org/html/2605.25547v1)

- **采用命题：** Action-VAE 从 policy proposal 周围生成多个低维 latent action candidates，再以 task-progress outcome predictor 选择动作；verifier 只拥有候选排序权，不能替代 controller commit。
- **方法定位：** §3.2 posterior action sampling; §3.3 task-progress verification
- **评价定位：** §4 simulation, real-world and sample/latent ablations
- **限制/反证：** Appendix I linear-progress assumption and base-policy capacity boundary
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `Critical-phase Dreaming 只获得候选排序权` — 每步都运行 world-model rollout 会超过实时控制预算，完全 reactive policy 又可能在关键转折前看不到失败。受限方案先由 trigger 判断 critical phase，再生成少量 action proposals，用 short-horizon dream evaluator 排序，最后把候选交给 runtime assurance；dream state 不拥有物理 commit 权，真实 observation 仍会覆盖想象。 按关键阶段调用减少平均开销，却新增 trigger 漏检、world-model 偏差和 evaluator 自我确认；错误 dream 可能把安全动作排除。高频、不可逆或模型失配时，应回退 reactive controller、硬约束和 human override。`arXiv:2605.11750v1` 的 §3–§7 与 Appendix F 只支持作者仿真和真实机器人设置，不证明开放环境安全或长期 rollout 忠实。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：Action-VAE 从 policy proposal 周围生成多个低维 latent action candidates，再以 task-progress outcome predictor 选择动作；verifier 只拥有候选排序权，不能替代 controller commit。
- **Books：** `No Change — Existing Coverage`；owner 为 `MULTIMODAL-EMBODIED-VLA` / [`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25550 DisagFusion: Asynchronous Pipeline Parallelism and Elastic Scheduling for Disaggregated Diffusion Serving](https://arxiv.org/html/2605.25550v1)

- **采用命题：** 以异步 pipeline 重叠 diffusion stages 的计算与 handoff，并结合轻量性能预测和 runtime feedback 动态重配各 stage instance ratio，以吸收 workload shift 与 stage imbalance。
- **方法定位：** §2 workload/stage imbalance; §3 async pipeline and hybrid instance scheduler; §4 implementation
- **评价定位：** §5 quality, latency, scale, robustness, elasticity and utilization
- **限制/反证：** §7 Conclusion; diffusion-stage topology and disclosed hardware/workload boundary
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `INFER-PD-DISAGGREGATION` / [`books/part-05-inference-system/55-pd-disaggregation.md`](../../../../books/part-05-inference-system/55-pd-disaggregation.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25621 StreamOV: Streaming Omni-Video Understanding via Evidence-Guided Memory and Response Triggering](https://arxiv.org/html/2605.25621v1)

- **采用命题：** 用 multimodal evidence-guided long/short-term memory 在固定预算内压缩流式音视频历史，再由 hidden-state trigger 决定何时主动响应，避免把 silence token 或外部 router 当作唯一时机 owner。
- **方法定位：** §4.1 evidence construction; §4.2 long/short memory update; §4.3 response trigger
- **评价定位：** §3 SOVBench and §5 audio-visual/visual-only/ablation evaluation
- **限制/反证：** Appendix J trigger failures; Appendix K limitations and future work
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `MULTIMODAL-REPRESENTATION` / [`books/part-03-multimodal-world-models/23-multimodal-representation.md`](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。Fresh non-author post-write semantic review passed; the paired binding remains before the first main H2 Review notes.

### [2605.25624 CUA-Gym: Scaling Verifiable Training Environments and Tasks for Computer-Use Agents](https://arxiv.org/html/2605.25624v1)

- **采用命题：** 由 Generator 构造 initial/golden environment state、独立 Discriminator 编写 reward function、orchestrator 迭代执行并以多数票和 rollout 终检，使 task、environment 与 deterministic reward 成为同一可验证 tuple。
- **方法定位：** §2.1 adversarial task/reward co-generation; §2.2 environment scaling
- **评价定位：** §3–§4 training results, data/environment scaling and emergent multi-action calls
- **限制/反证：** §6 Limitations; synthetic task and environment-fidelity boundary
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `Model 与 data-generating harness 是共同演进的配对 artifact` — Agent 能力不仅由 weights 决定，也由生成任务、环境状态、tool feedback 和评分证据的 harness 塑造。只优化模型会过拟合旧 harness，只升级 harness 又会让既有 checkpoint 失去可比性。平台应把 model revision 与 harness revision 成对注册，交替优化时保留 cross-product regression：新模型跑旧/新 harness，旧模型也跑新 harness。 联合演进扩大探索空间，却增加版本组合和 benchmark overfitting。有限实验不证明某种 co-evolution schedule 最优；生产 release 仍需冻结独立 holdout/environment，无法解释回归时回退上一对已验证 artifact。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：由 Generator 构造 initial/golden environment state、独立 Discriminator 编写 reward function、orchestrator 迭代执行并以多数票和 rollout 终检，使 task、environment 与 deterministic reward 成为同一可验证 tuple。
- **Books：** `No Change — Existing Coverage`；owner 为 `AGENT-PLATFORM` / [`books/part-07-agent/84-agent-platform.md`](../../../../books/part-07-agent/84-agent-platform.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25632 Insuring Every Action: An Authority Frontier Framework for Runtime Actuarial Control of Autonomous AI Agents](https://arxiv.org/html/2605.25632v1)

- **采用命题：** We propose the Actuarial Action Interface (AAI), a deterministic runtime contract that prices each such action against a contractually fixed safe default under a time-consistent risk mapping, and gates execution against a per-boundary reserve capital budget.
- **方法定位：** §3 action taxonomy and quote-bind-commit; §4 authority frontier and capital metrics
- **评价定位：** §5–§7 simulation, calibration and runtime-control experiments
- **限制/反证：** §8 Limitations; actuarial assumptions and empirical deployment boundary
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `AGENT-TOOL-CALLING` / [`books/part-07-agent/78-tool-calling.md`](../../../../books/part-07-agent/78-tool-calling.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25641 Iterate Until Retrieved: Factual Nugget Optimization for Discoverable Continual Corrections in Agentic RAG](https://arxiv.org/html/2605.25641v1)

- **采用命题：** 把 factual correction 写成带来源的 nugget，并让生产 RAG 充当 test harness：对触发 query 与 paraphrases 反复 probe、读取失败 trace、修订直到可发现；事实正确性与检索可发现性仍是两个 Gate。
- **方法定位：** §3 production correction setting; §4 factual-nugget variants and iterative optimization
- **评价定位：** §5–§6 held-out, transfer, negative-control and answer-level results
- **限制/反证：** §7 Conclusion: one retrieval architecture, English-only and LLM dependence
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `AGENT-RAG` / [`books/part-07-agent/76-rag.md`](../../../../books/part-07-agent/76-rag.md)。Fresh non-author post-write semantic review passed; the paired binding remains before the first main H2 Review notes.

### [2605.25653 When Agents Control Robots: A Zero Trust Policy Model for Agentic Cyber-Physical Systems](https://arxiv.org/html/2605.25653v1)

- **采用命题：** 以 25 个 typed primitives 和 Physical Impact Tier 组成 actuation-boundary zero-trust policy；模型只提议机器人参数，policy 在真实物理 effect 前执行确定性约束。
- **方法定位：** §3 threat/system model; §4 typed zero-trust enforcement and physical-impact tiers
- **评价定位：** §5 deployed instantiation, 60 traces and coverage analysis
- **限制/反证：** §6 Conclusion; small system/model/trace envelope
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `Cyber-physical Safety 要验证持续的 Process Effect` — 获得访问、发出写操作甚至设备接受命令，都不等于物理攻击或保护已经成立。评价链应继续追踪 action 是否改变 actuator、变化是否穿过控制回路、过程变量是否持续越界，以及安全联锁是否生效。把早期代理指标当 outcome 会高估攻击与防御能力；代价是需要 simulator、hardware-in-the-loop 或受控实体验证。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：以 25 个 typed primitives 和 Physical Impact Tier 组成 actuation-boundary zero-trust policy；模型只提议机器人参数，policy 在真实物理 effect 前执行确定性约束。
- **Books：** `No Change — Existing Coverage`；owner 为 `PLATFORM-SECURITY` / [`books/part-06-ai-infrastructure/72-security.md`](../../../../books/part-06-ai-infrastructure/72-security.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25655 Bandwidth-Aware LLM Inference on Heterogeneous Many-Core Supercomputers](https://arxiv.org/html/2605.25655v1)

- **采用命题：** 把 VLIW-SIMD operator、density-driven graph fusion 与 Prefill-Buffer-Decode bounded-buffer pipeline 组合为硬件感知执行计划，使数据 locality、通信层级和 hybrid parallelism 共同受控。
- **方法定位：** §III-A framework; §III-B operators; §III-C graph schedule; §III-D adaptive parallelism
- **评价定位：** §IV throughput, ablation and operator scaling experiments
- **限制/反证：** §V Conclusion; MT-3000-specific architecture and bandwidth boundary
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `低带宽拓扑要联合预算 Hops、Bytes 与 Steps` — 单数据中心、高带宽互联中，固定 pipeline placement 与局部通信优化通常足够，稳定拓扑也让故障和 tail latency 更容易解释。GPU 分散在低带宽、跨地域节点后，只看空闲显存或单跳带宽会失真：少放一个 transformer block 可能增加每个 decode step 的跨节点 hops；为了减少 hops 而 offload KV，又会引入 host-memory traffic；lossless compression 改变每跳 bytes，speculative decoding 则可能改变完成同样输出所需的串行 decode steps。 因此 placement planner 应在同一 GPU-memory constraint 下联合选择 block consolidation、KV residency/offload、pipeline hops、micro-batch overlap、lossless communication representation 与 speculative-work budget。Planner 只提出 versioned plan；cache owner 确认 KV location，communicator 确认 payload/epoch，runtime 才在 plan boundary commit，autoscaler仍负责未来 capacity。第 48 章仍拥有 draft、verify、acceptance 与 committed-token correctness；本章只把已定义的 speculative work 纳入低带宽全局计划，不能把这些 authority 合并成一个吞吐分数。 联合优化可以在低带宽环境减少通信暴露，却把 host CPU memory、压缩/解压、dynamic-program cost、拓扑漂移和故障恢复带进 serving contract。高带宽同构集群、KV offload 反而更慢、压缩收益不足或 topology/SLO 无法准确建模时，固定 placement 与普通 pipeline 仍更可验证。论文结果只绑定其 internet-scale testbed、模型和公开配置，不证明通用去中心化服务优势。 去中心化 prefix cache 进一步改变了调度状态的可靠性要求。集中目录能提供较新的全局视图，却会增加协调延迟和单点压力；节点只维护本地 radix tree 并周期性交换摘要，则能让路由控制面随 peer 数量扩展。这里的关键不是强行让所有副本同步，而是把弱一致性的失败语义限定为“可能错过一次 cache hit”，不能让陈旧目录影响 token correctness。Scheduler 因而可以把 cache
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：把 VLIW-SIMD operator、density-driven graph fusion 与 Prefill-Buffer-Decode bounded-buffer pipeline 组合为硬件感知执行计划，使数据 locality、通信层级和 hybrid parallelism 共同受控。
- **Books：** `No Change — Existing Coverage`；owner 为 `INFER-SCHEDULING` / [`books/part-05-inference-system/56-inference-scheduling.md`](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25673 Referential Security as a New Paradigm for AI Evaluations](https://arxiv.org/html/2605.25673v1)

- **采用命题：** To resolve this, we propose referential security as a new paradigm for AI evaluation.
- **方法定位：** §3 referential stability; §4 threat model; §5 workflows; §8 attestation/fingerprinting architectures
- **评价定位：** §7 provider identifier survey and workflow analysis
- **限制/反证：** §9 Conclusions; proposal-level evidence without broad deployed evaluation
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `PLATFORM-SECURITY` / [`books/part-06-ai-infrastructure/72-security.md`](../../../../books/part-06-ai-infrastructure/72-security.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25674 Stochastic Estimation of the Layer-wise Hessian Trace for Monitoring Neural-network Training](https://arxiv.org/html/2605.25674v1)

- **采用命题：** 以一次全参数 Hessian-vector product 配合 Hutchinson probes 无偏估计每层 Hessian trace；weight sharing 必须先装配 layer Hessian 再二次求导，并用临界 probe 数平衡随机投影与 mini-batch 方差。
- **方法定位：** §2 layer-wise target; §3 unbiased estimator; §4 variance analysis
- **评价定位：** §5 memorisation-regime setup, decision rule and empirical validation
- **限制/反证：** §6 Discussion and limitations; modest model/monitoring setting
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `PLATFORM-MONITORING` / [`books/part-06-ai-infrastructure/67-monitoring.md`](../../../../books/part-06-ai-infrastructure/67-monitoring.md)。Fresh non-author post-write semantic review passed; the paired binding remains before the first main H2 Review notes.

### [2605.25682 Profiling-Driven Adaptive Distributed Transformer Inference on Embedded Edge Deployment](https://arxiv.org/html/2605.25682v1)

- **采用命题：** 实机 profiling 表明 embedded distributed inference 的瓶颈还包括 CPU-GPU staging；运行时应依据离线 profile 在 local 与 compressed distributed execution 间选择，而不是默认全 tensor exchange。
- **方法定位：** §3 segment communication, staging bottleneck and adaptive inference
- **评价定位：** §4 prototype; §5 latency, energy, qualitative and instrumentation results
- **限制/反证：** §6 Conclusion; Jetson/Wi-Fi prototype and qualitative-output boundary
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `从逐配置压测到校准后的配置搜索` — Routing、placement 与 autoscaling 之前还有一个更慢的决策层：在给定 model、hardware、runtime、 parallelism、KV budget、workload 和 SLO 下，哪些配置值得部署。逐项启动服务并压测最接近真实 silicon， 在配置空间较小时仍是最可信的方案；但框架开关、并行度、chunk size、batch 和 PD 拓扑组合增长后， 穷举的加载与测量成本会变成瓶颈。 更可扩展的路线不是取消 benchmark，而是把它变成校准与验证环节：先测量 versioned primitive/operator database，再用 iteration model 组合 GEMM、attention、communication 与 memory cost；根据 workload descriptor、topology 和 SLO 生成候选，筛选 Pareto frontier，最后只对高价值配置做 silicon validation。 ```text manual exhaustive benchmark -> calibrated primitive database -> iteration- and queue-aware prediction -> SLO-constrained candidate / Pareto search -> version-compatible launch contract -> targeted silicon validation and rollback ``` Prefill/Decode 分池时，配置器还必须分别估计两侧 service rate，把 KV transfer 修正纳入 TTFT，并以 较慢一侧做 rate matching。它说明 PD 不是固定拓扑选择，而是受 arrival、ISL/OSL、TTFT/TPOT 与 transfer contract 约束的双队列配平。 模型的可靠性取决于 calibration identity。数据库至少要绑定 GPU/driver、runtime/kernel revision、 model/precision、shape range、parallel mapping、workload distribution 与 SLO；任何一项漂移都可能令 推荐失效。Prediction uncertainty、outlier policy、freshness detector、fallback 和 rollback 因而也是 配置系统的一部分。未校准硬件、新 kernel、强 tail-SLO 或 queueing regime 改变时，直接压测仍不可替代。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：实机 profiling 表明 embedded distributed inference 的瓶颈还包括 CPU-GPU staging；运行时应依据离线 profile 在 local 与 compressed distributed execution 间选择，而不是默认全 tensor exchange。
- **Books：** `No Change — Existing Coverage`；owner 为 `INFER-SCHEDULING` / [`books/part-05-inference-system/56-inference-scheduling.md`](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25698 How Should LLMs Consume High-Quality Data? Optimal Data Scheduling via Quality-Aware Functional Scaling Laws](https://arxiv.org/html/2605.25698v1)

- **采用命题：** Motivated by the theoretical structure, we propose Drop-Stable-Rampup for LLM midtraining: drop the batch size at the quality transition, keep it low to accumulate signal, then ramp up to suppress noise.
- **方法定位：** §3 quality-aware functional scaling law; §4 optimal schedule; §5.1 Drop-Stable-Rampup
- **评价定位：** §5.2–§5.4 batch drop, phase ratio and schedule comparison
- **限制/反证：** §6 scope: theoretical simplification, multi-task heterogeneity, scale dependence and overhead
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `TRAIN-DATA` / [`books/part-04-training-system/27-data.md`](../../../../books/part-04-training-system/27-data.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25707 AgentHijack: Benchmarking Computer Use Agent Robustness to Common Environment Corruptions](https://arxiv.org/html/2605.25707v1)

- **采用命题：** 用九类可配置的非对抗环境 corruption 分阶段压力测试 computer-use agents，并以 action generator 加独立 onlooker 做 grounding、行为摘要与环境复核；轻微扰动也会造成显著执行退化。
- **方法定位：** §3 corruption benchmark; §4 robustness method
- **评价定位：** §5 setup, main results and ablation; Appendix E case studies
- **限制/反证：** §6 Conclusion; OSWorld corruption/model envelope
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `Tool Robustness 要按 Failure Stage 注入` — 干净 E2E 成功率只能告诉系统是否完成任务，不能定位 tool failure 在 selection、schema grounding、argument binding、output interpretation 还是 runtime effect 阶段发生。更可行动的评测应按阶段注入 interface、intent、observation 与 runtime perturbation，并用 typed trace 追踪 cascade；不同故障组合不能假定简单相加。 stage-aligned injection 需要维护 gold fields、故障模型和 scorer，本身也可能偏离真实 incident 分布。干净回归仍是必要基线，只有诊断或发布决策需要时才承担额外成本；未覆盖故障必须保留为 evidence limitation。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：用九类可配置的非对抗环境 corruption 分阶段压力测试 computer-use agents，并以 action generator 加独立 onlooker 做 grounding、行为摘要与环境复核；轻微扰动也会造成显著执行退化。
- **Books：** `No Change — Existing Coverage`；owner 为 `PLATFORM-EVALUATION-SYSTEM` / [`books/part-06-ai-infrastructure/66-evaluation-system.md`](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25716 An Efficient and Privacy-Preserving Architecture for Cross-Institutional Collaborative RAG](https://arxiv.org/html/2605.25716v1)

- **采用命题：** 以 numerically stable feature scrambling 与 token permutation 构造 Scrambled Distributed Attention，把 attention execution 与明文数据位置解耦；该协议仍须对 inversion、collusion 与数值误差单独验收。
- **方法定位：** §3 threat model; §4 scrambled distributed attention; §5 role-aware collaborative RAG
- **评价定位：** §6 privacy analysis; §7 latency, network, utility and quantization evaluation
- **限制/反证：** §8 Discussion; honest-but-curious assumptions and disclosed network/topology boundary
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `PLATFORM-SECURITY` / [`books/part-06-ai-infrastructure/72-security.md`](../../../../books/part-06-ai-infrastructure/72-security.md)。Fresh non-author post-write semantic review passed; the paired binding remains before the first main H2 Review notes.

### [2605.25745 Selective Latent Thinking: Adaptive Compression of LLM Reasoning Chains](https://arxiv.org/html/2605.25745v1)

- **采用命题：** 按 confidence gate 在 explicit CoT 与 latent span 之间动态切换，使压缩成为可回退的 runtime commit 决策。
- **方法定位：** §3 span anticipation, confidence gate, latent encoding and three-stage training
- **评价定位：** §4 four math benchmarks; compression/accuracy/latency and gating ablations
- **限制/反证：** §5 Limitations: math/model/calibration scope and latent-span error propagation
- **证据边界：** 只支持 Selective Latent Thinking: Adaptive Compression of LLM Reasoning Chains exact-v1 披露的方法与 evaluation envelope；未测试的模型、硬件、并发、tail-SLO、攻击分布和生产泛化均未证明。
- **Books：** `Applied`；owner 为 `MODEL-DECODER-ONLY` / [`books/part-02-model/18-decoder-only.md`](../../../../books/part-02-model/18-decoder-only.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25746 Multi-Agent Coordination Adaptation via Structure-Guided Orchestration](https://arxiv.org/html/2605.25746v1)

- **采用命题：** 把 agent participation graph 与 step-level orchestration作为联合可适配状态，而非固定拓扑或隐式通信。
- **方法定位：** §3 joint structure/orchestration posterior; §4 task-budget structural prior and policy orchestration
- **评价定位：** §5 benchmark/token-budget comparisons and interaction ablations
- **限制/反证：** §6 Limitations: tested tasks/models/budgets and centralized training assumptions
- **证据边界：** 只支持 Multi-Agent Coordination Adaptation via Structure-Guided Orchestration exact-v1 披露的方法与 evaluation envelope；未测试的模型、硬件、并发、tail-SLO、攻击分布和生产泛化均未证明。
- **Books：** `Applied`；owner 为 `AGENT-MULTI-AGENT` / [`books/part-07-agent/82-multi-agent.md`](../../../../books/part-07-agent/82-multi-agent.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25798 DiSC: Resolution-Scalable Acceleration of Diffusion Models by Exploiting Sparsity and Cached Token Reuse with Hash-based Distribution](https://arxiv.org/html/2605.25798v1)

- **采用命题：** 以跨 diffusion step 的 Cached Token Reuse 和复用 attention sparsity mask 的 Softmax Thresholding 形成混合 dense/sparse workload，再用 hash-based bank distribution 在同一 accelerator 数据流中承载稀疏执行。
- **方法定位：** §III cached-token reuse and softmax-threshold mask reuse; §IV hash-distributed hardware
- **评价定位：** §V methodology, performance, area/power and high-resolution comparison
- **限制/反证：** §VII Conclusion; specialized architecture and diffusion-workload simulation boundary
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `Token-level 预算不能由三个独立近似器分别消费` — activation sparsity、structured pruning 与 low precision 分别优化时最容易实现，但三者都在消耗同一 token 的质量 余量：attention 少看哪些位置、MLP 跳过哪些结构、剩余计算采用何种精度会相互改变误差。三个局部 controller 即使 各自满足阈值，也可能叠加成不可接受的输出漂移。 联合路径把 token/context state、目标 SLO 与可校准 quality budget 交给一个 proposal policy，同时选择 attention sparsity、structured width/pruning 与 precision；compiler/runtime 只接受硬件支持、metadata 成本可控且通过 reference check 的 plan。policy 拥有候选，不拥有正确性；verifier 和 dense/full-precision fallback 仍拥有 admission。 联合控制能把算力投入更敏感 token，却新增组合 action space、online decision overhead、calibration drift 与难以隔离 的误差来源。训练分布外输入、预算传感器失准、硬件不支持动态 plan 或 tail latency 受 controller 本身支配时，应 回退独立的静态 sparsity/quantization artifact，必要时执行 dense full precision。论文结果只支持其模型、accelerator 与 policy action space，不能把作者质量—算力曲线外推为生产常数。[受限证据：arXiv:2605.10875v1]
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：以跨 diffusion step 的 Cached Token Reuse 和复用 attention sparsity mask 的 Softmax Thresholding 形成混合 dense/sparse workload，再用 hash-based bank distribution 在同一 accelerator 数据流中承载稀疏执行。
- **Books：** `No Change — Existing Coverage`；owner 为 `INFER-TENSORRT-LLM` / [`books/part-05-inference-system/49-tensorrt-llm.md`](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25815 Behind EvoMap: Characterizing a Self-Evolving Agent-to-Agent Collaboration Network](https://arxiv.org/html/2605.25815v1)

- **采用命题：** 证明开放 A2A asset economy 若把 publication、自报 metadata 与本地日志当 authority，会产生不可审计的 reuse/quality failure。
- **方法定位：** §3 EvoMap dataset/protocol reconstruction; §4 reuse, credit, GDI and validation analysis
- **评价定位：** §5–§7 1.5M assets/128K agents empirical audit and manipulation checks
- **限制/反证：** §8 limitations: 47-day observational snapshot, one ecosystem and self-reported fields
- **证据边界：** 只支持 Behind EvoMap: Characterizing a Self-Evolving Agent-to-Agent Collaboration Network exact-v1 披露的方法与 evaluation envelope；未测试的模型、硬件、并发、tail-SLO、攻击分布和生产泛化均未证明。
- **Books：** `Applied`；owner 为 `AGENT-PLATFORM` / [`books/part-07-agent/84-agent-platform.md`](../../../../books/part-07-agent/84-agent-platform.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25819 On Reliability of Efficient Membership Inference Vulnerability Evaluation](https://arxiv.org/html/2605.25819v1)

- **采用命题：** 把低-FPR membership-inference audit 的 sample identity、aggregation threshold 与 finite-population bias纳入 measurement contract。
- **方法定位：** §3 per-sample vulnerability; §4 calibrated aggregation; §5 finite-population correction
- **评价定位：** §6 efficient LiRA experiments and analytical simulation
- **限制/反证：** §7/Appendix: Gaussian post-processing, finite shadow-model and dataset scope
- **证据边界：** 只支持 On Reliability of Efficient Membership Inference Vulnerability Evaluation exact-v1 披露的方法与 evaluation envelope；未测试的模型、硬件、并发、tail-SLO、攻击分布和生产泛化均未证明。
- **Books：** `Applied`；owner 为 `PLATFORM-EVALUATION-SYSTEM` / [`books/part-06-ai-infrastructure/66-evaluation-system.md`](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25820 Visual-Redundancy-Controlled Parallel Decoding for Diffusion-Based Multimodal Large Language Models](https://arxiv.org/html/2605.25820v1)

- **采用命题：** 用 Visual Redundancy Index 衡量同一步并行提交 tokens 的视觉 grounding 重叠，再让 VRCD 优先提交视觉互补位置；attention overlap 只是 selection sensor，不是语义正确性证明。
- **方法定位：** §3.2 visual redundancy; §3.3 redundancy-controlled parallel decoding
- **评价定位：** §4 model/benchmark comparison, certainty analysis and ablation
- **限制/反证：** Appendix A.3 limitations; backbone and multimodal-task scope
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS` / [`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。Fresh non-author post-write semantic review passed; the paired binding remains before the first main H2 Review notes.

### [2605.25831 Clarify, Abstain or Answer? Strategising in Conversation with Belief-Augmented Generation](https://arxiv.org/html/2605.25831v1)

- **采用命题：** We propose Belief-Augmented Generation (BAG): grounding LLMs in their own belief state via the prompt and letting them reason over these K samples to decide on a conversational strategy: answer, clarify, or abstain.
- **方法定位：** §3.1 belief-state construction; §3.2 clarify/abstain/answer strategy
- **评价定位：** §4–§7 interaction simulation, accuracy, clarification and faithfulness
- **限制/反证：** §9 Limitations; simulated-user/judge and dataset ambiguity boundary
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `AGENT-REFLECTION` / [`books/part-07-agent/80-reflection.md`](../../../../books/part-07-agent/80-reflection.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25854 From Accounting to Coordination: A Virtual Water-Aware Electricity-Computation-Water Nexus Framework for Data Center Dispatch](https://arxiv.org/html/2605.25854v1)

- **采用命题：** 把 data-center workload placement 的 cost 从静态水耗统计改为与电网 dispatch 联动的可执行控制目标。
- **方法定位：** §3 differentiable ECW dispatch layer; §4 fixed-point virtual-water coordination
- **评价定位：** §5 IEEE 30/118-bus dispatch and consistency experiments
- **限制/反证：** §6 limitations: simulated grid, water-attribution model and no production DC trace
- **证据边界：** 只支持 From Accounting to Coordination: A Virtual Water-Aware Electricity-Computation-Water Nexus Framework for Data Center Dispatch exact-v1 披露的方法与 evaluation envelope；未测试的模型、硬件、并发、tail-SLO、攻击分布和生产泛化均未证明。
- **Books：** `Applied`；owner 为 `PLATFORM-COST` / [`books/part-06-ai-infrastructure/70-cost.md`](../../../../books/part-06-ai-infrastructure/70-cost.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25869 Mitigating Provenance-Role Collapse in Long-Term Agents via Typed Memory Representation](https://arxiv.org/html/2605.25869v1)

- **采用命题：** To resolve this cognitive vulnerability at the architectural level, we propose MemIR, a typed Memory Intermediate Representation that operationalizes source monitoring as a structural constraint.
- **方法定位：** §3.1 typed memory atoms; §3.2 multi-route projection; §3.3 provenance-scoped use
- **评价定位：** §4 main results, ablation, backbone and hyperparameter analysis
- **限制/反证：** §5 Conclusion; benchmark/prompt and long-term deployment boundary
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `AGENT-MEMORY` / [`books/part-07-agent/77-memory.md`](../../../../books/part-07-agent/77-memory.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25874 WBench: A Comprehensive Multi-turn Benchmark for Interactive Video World Model Evaluation](https://arxiv.org/html/2605.25874v1)

- **采用命题：** 以 video quality、setting/interaction adherence、consistency 与 physics compliance 五轴组成 multi-turn world-model benchmark，并统一 text、6-DoF pose 与 discrete action 接口、用人评校准自动子指标。
- **方法定位：** §3 multi-turn dataset; §4 world-model evaluation suite
- **评价定位：** §5 protocol, per-dimension, cross-dimension and human-alignment results
- **限制/反证：** §6 Conclusion; Appendix B web-model access and configuration boundary
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `视觉逼真与三维一致性是两份不同证据` — 逐帧视觉质量可以筛掉明显伪影，却不能证明相机运动、遮挡关系、物体尺度和场景几何在 rollout 中自洽。面向 planning 的 World Model 需要把 perceptual realism 与 geometric consistency 分开测，并绑定 camera/scene state： ```text initial observation + camera/action contract → generated rollout → perceptual quality evidence + multi-view / temporal geometry evidence → planning-relevant acceptance ``` 几何约束能减少“看起来合理但无法作为环境状态”的视频，却增加标定、深度/位姿估计和 evaluator 偏差；二维生成任务、固定视角或不消费三维状态的 workload 仍可只用感知质量基线。即使几何一致，也不证明 transition 具有因果可控性，更不能替代 action-conditioned policy evaluation。 确定性或近确定性环境中，固定初态与 action 后比较一次 predicted transition 可以是充分而便宜的 baseline；但很多物理过程 在相同条件下存在多个合法 outcome。此时“生成了一条合理轨迹”只证明 support 中可能有一个样本，无法证明模型给各结果 分配了正确概率。更严格的合同需要固定初态和 action，独立重复采样，再把 rollout 映射为可审计 outcome： ```text same initial observation + same action contract → repeated independent rollouts → integrity-valid outcome extraction → empirical outcome distribution → compare with reference distribution ``` 它把 world model 从 plausible video generator 进一步约束为 stochastic transition sampler。代价是更高采样成本、outcome 离散化误差、reference distribution 构造成本和 seed/runtime identity；有限样本下没有观察到某个 rare outcome，也不证明 它的概率为零。单次 deterministic transition test 在近确定性场景、smoke test 或预算很低时仍合理；只有环境固有随机性会 影响 planning/risk 时，di
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：以 video quality、setting/interaction adherence、consistency 与 physics compliance 五轴组成 multi-turn world-model benchmark，并统一 text、6-DoF pose 与 discrete action 接口、用人评校准自动子指标。
- **Books：** `No Change — Existing Coverage`；owner 为 `MULTIMODAL-WORLD-MODELS` / [`books/part-03-multimodal-world-models/25-multimodal-world-models.md`](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.25889 Capability and Robustness Cannot Both Be Free: An Information-Theoretic Bound for Vision-Language-Action Models](https://arxiv.org/html/2605.25889v1)

- **采用命题：** 将 VLA robustness 从单项防御分数提升为 capability、encoder channel 与 attack budget 共同约束的 evaluation boundary。
- **方法定位：** §3 information-theoretic capability/robustness bound; §4 encoder-specific corollary
- **评价定位：** §5 Gaussian/OpenVLA/LIBERO/PGD and cross-architecture diagnostics
- **限制/反证：** §6 limitations: loose pixel bound, estimated mutual information and tested attacks
- **证据边界：** 只支持 Capability and Robustness Cannot Both Be Free: An Information-Theoretic Bound for Vision-Language-Action Models exact-v1 披露的方法与 evaluation envelope；未测试的模型、硬件、并发、tail-SLO、攻击分布和生产泛化均未证明。
- **Books：** `Applied`；owner 为 `MULTIMODAL-EMBODIED-VLA` / [`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25893 $D^2$-Monitor: Dynamic Safety Monitoring for Diffusion LLMs via Hesitation-Aware Routing](https://arxiv.org/html/2605.25893v1)

- **采用命题：** 把 diffusion trajectory 中 hidden state 反复贴近 probe decision boundary 的次数定义为 safety hesitation，以此预测轻量 probe failure 并只在阈值越界时路由重 probe。
- **方法定位：** §3 hesitation signals; §4 cascade monitor and probe routing
- **评价定位：** §5 datasets/models, efficiency-effectiveness, robustness and ablation
- **限制/反证：** Appendix A Limitation; evaluated diffusion models/remasking strategies only
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `PLATFORM-SECURITY` / [`books/part-06-ai-infrastructure/72-security.md`](../../../../books/part-06-ai-infrastructure/72-security.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25966 Mapping the Schedule x Bit-Width Boundary in Sub-100M Quantisation-Aware Training](https://arxiv.org/html/2605.25966v1)

- **采用命题：** factorial evidence 否定 FP16/INT8/INT6 需要不同 warmdown 的假设，却发现 INT4 在约 50M 参数以上出现明确 schedule boundary；bit-width、model size 与 schedule 必须共同组成训练 identity。
- **方法定位：** §3 QAT implementation, LR schedule and factorial/ablation grid
- **评价定位：** §4–§5 compute/statistical protocol and schedule×bit-width results
- **限制/反证：** §6.8 Limitations; sub-100M and tested optimizer/data regime
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `TRAIN-PRETRAINING` / [`books/part-04-training-system/28-pretraining.md`](../../../../books/part-04-training-system/28-pretraining.md)。Fresh non-author post-write semantic review passed; the paired binding remains before the first main H2 Review notes.

### [2605.25971 Anticipate and Learn: Unleashing Idle-Time Compute in Proactive Agents](https://arxiv.org/html/2605.25971v1)

- **采用命题：** 让 agent 在空闲期主动读取 memory、预取 evidence，并把过期/错误 anticipation 作为可取消 speculative state。
- **方法定位：** §3 proactive need prediction; §4 idle-time evidence acquisition and persistent-memory loop
- **评价定位：** §5 ProActEval/MemBench, turn/effort/hallucination and ablation results
- **限制/反证：** §6 limitations: predictable-need scenarios, privacy/cost and stale anticipation
- **证据边界：** 只支持 Anticipate and Learn: Unleashing Idle-Time Compute in Proactive Agents exact-v1 披露的方法与 evaluation envelope；未测试的模型、硬件、并发、tail-SLO、攻击分布和生产泛化均未证明。
- **Books：** `Applied`；owner 为 `AGENT-PLATFORM` / [`books/part-07-agent/84-agent-platform.md`](../../../../books/part-07-agent/84-agent-platform.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25988 What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA](https://arxiv.org/html/2605.25988v1)

- **采用命题：** 训练期 checker 的输出分布而非 held-out accuracy 决定是否提供可学习梯度：neutral-heavy log-prob scoring 会 signal collapse，过强 checker 又会诱发短答案、避检索与语言坍缩的 reward hacking。
- **方法定位：** §3 checker backends and reward; §5 signal collapse; §6 reward-hacking cascade
- **评价定位：** §4 main/cross-model results and appendices 9–16
- **限制/反证：** §8 listed limitations: evaluation independence, seeds, test size, domain and incomplete cascade resolution
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `AGENT-RAG` / [`books/part-07-agent/76-rag.md`](../../../../books/part-07-agent/76-rag.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.25997 Deployment-complete benchmarking](https://arxiv.org/html/2605.25997v1)

- **采用命题：** 把 benchmark score 是否足以决定 deployment action 形式化为 evidence-fiber completeness 与补证成本。
- **方法定位：** §2 evidence fibers and action completeness; §3 completion curves; §4 certify-then-acquire
- **评价定位：** §5 controlled channels and Tox21/Matbench/JARVIS audits
- **限制/反证：** §6 limitations: finite response spaces, selected public datasets and action model
- **证据边界：** 只支持 Deployment-complete benchmarking exact-v1 披露的方法与 evaluation envelope；未测试的模型、硬件、并发、tail-SLO、攻击分布和生产泛化均未证明。
- **Books：** `Applied`；owner 为 `PLATFORM-EVALUATION-SYSTEM` / [`books/part-06-ai-infrastructure/66-evaluation-system.md`](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.26029 CausaLab: A Scalable Environment for Interactive Causal Discovery Toward AI Scientists](https://arxiv.org/html/2605.26029v1)

- **采用命题：** 在可干预 synthetic SCM laboratory 中把 held-out prediction 与 recovered graph/equations 的机制忠实度分开计分；高预测准确率可与低结构恢复并存，premature stopping 需要 consistency verification。
- **方法定位：** §3 interactive SCM environment; §4 parsable causal-trajectory DSL
- **评价定位：** §5 mechanism recovery, interventions, scale and verification results
- **限制/反证：** §8 Limitations; synthetic SCM and benchmark-agent scope
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `PLATFORM-EVALUATION-SYSTEM` / [`books/part-06-ai-infrastructure/66-evaluation-system.md`](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Fresh non-author post-write semantic review passed; the paired binding remains before the first main H2 Review notes.

### [2605.26037 Peak-Then-Collapse and the Four Interface Channels of Knowledge-Graph Tool Use](https://arxiv.org/html/2605.26037v1)

- **采用命题：** 揭示 outcome-only RLVR 在低信息 tool feedback 下会 peak-then-collapse，reward densification 只能迁移 failure 而不能补足接口信息。
- **方法定位：** §2 KG tool interface and RLVR setup; §3 four feedback channels; §4 reward variants
- **评价定位：** §5 four-seed peak-collapse, oracle relation ablation and self-distillation
- **限制/反证：** §6 limitations: Freebase/CWQ/Qwen2.5-7B and interface-specific failure
- **证据边界：** 只支持 Peak-Then-Collapse and the Four Interface Channels of Knowledge-Graph Tool Use exact-v1 披露的方法与 evaluation envelope；未测试的模型、硬件、并发、tail-SLO、攻击分布和生产泛化均未证明。
- **Books：** `Applied`；owner 为 `TRAIN-GRPO` / [`books/part-04-training-system/33-grpo.md`](../../../../books/part-04-training-system/33-grpo.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.26045 Confidence and Calibration of Activation Oracles for Reliable Interpretation of Language Model Internals](https://arxiv.org/html/2605.26045v1)

- **采用命题：** 把 activation-oracle 文本解释从无置信度输出改为按 answer-space 可枚举性选择的校准 measurement operator。
- **方法定位：** §3 five confidence operators for activation oracles; §4 calibration protocol
- **评价定位：** §5 four Qwen/Gemma oracles, 6K samples/operator and label/no-label comparisons
- **限制/反证：** §6 limitations: secret-word task, enumerability and no general interpretability guarantee
- **证据边界：** 只支持 Confidence and Calibration of Activation Oracles for Reliable Interpretation of Language Model Internals exact-v1 披露的方法与 evaluation envelope；未测试的模型、硬件、并发、tail-SLO、攻击分布和生产泛化均未证明。
- **Books：** `Applied`；owner 为 `PLATFORM-EVALUATION-SYSTEM` / [`books/part-06-ai-infrastructure/66-evaluation-system.md`](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.26046 When Gradients Collide: Failure Modes of Multi-Objective Prompt Optimization for LLM Judges](https://arxiv.org/html/2605.26046v1)

- **采用命题：** multi-objective textual-gradient optimization 存在两个可分 failure：联合反馈会稀释 optimization-time task focus，合并单目标优化后的 instructions 又会产生 inference-time interference。
- **方法定位：** §3 decomposition grid; §5 gradient-specificity and instruction-interference analysis
- **评价定位：** §4 results and appendices B–F trajectory/task diagnostics
- **限制/反证：** §6–§7 conclusion/future work; two datasets and textual-gradient optimizer scope
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **Books：** `Applied`；owner 为 `PLATFORM-EVALUATION-SYSTEM` / [`books/part-06-ai-infrastructure/66-evaluation-system.md`](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Fresh non-author post-write semantic review passed; the paired binding remains before the first main H2 Review notes.

### [2605.26047 Retrying vs Resampling in AI Control](https://arxiv.org/html/2605.26047v1)

- **采用命题：** 区分会泄露 monitor rationale 的 retry control 与不暴露反馈的 resampling，并把 sample aggregation/audit budget 纳入安全契约。
- **方法定位：** §2 control setting/metrics; §3 retrying; §4 resampling and audit aggregation
- **评价定位：** §5–§6 BashArena safety/usefulness, budget and selective-resampling experiments
- **限制/反证：** §7 limitations: one coding arena, model/monitor pair and adaptive adversary
- **证据边界：** 只支持 Retrying vs Resampling in AI Control exact-v1 披露的方法与 evaluation envelope；未测试的模型、硬件、并发、tail-SLO、攻击分布和生产泛化均未证明。
- **Books：** `Applied`；owner 为 `PLATFORM-SECURITY` / [`books/part-06-ai-infrastructure/72-security.md`](../../../../books/part-06-ai-infrastructure/72-security.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

### [2605.26079 Automated Benchmark Auditing for AI Agents and Large Language Models](https://arxiv.org/html/2605.26079v1)

- **采用命题：** 以 agentic audit 重放 task specification、environment dependency 与 grader logic；发现的问题经专家/上游修复验证后会改变分数和模型排序，因此 benchmark task 本身必须先通过 admission。
- **方法定位：** §2 evidence-collector/auditor; §3 benchmark-quality audit protocol
- **评价定位：** §4 fix/manual validation and §5 trajectory audit analysis
- **限制/反证：** §7 Conclusion; automated auditor false-positive/coverage and sampled-benchmark boundary
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `先验证 Benchmark 的 Reference Artifact，再比较 Agent` — 可执行 benchmark 仍可能因为 reference patch、依赖、机器镜像或 scorer 不稳定而产生伪排名。一个 candidate 失败，不一定说明 Agent 能力不足；也可能是 reference artifact 在另一台机器、冷缓存或重新构建后本身不再通过。 因此 benchmark admission 应先独立于被测 Agent 重放 reference： ```text immutable task + environment revision → rebuild and replay reference artifact across machine / round → verify deterministic and semantic outcomes → estimate infrastructure and scorer variance → only then score candidates and aggregate rankings ``` Reference replay 通过也不能证明 task 代表真实 workload，只能关闭“ground truth 自身不可复现”这一类故障。 当分数靠近 release threshold 时，还要报告 task-weight、failure penalty、timeout 与聚合方式的 sensitivity，而不是 把一个 leaderboard total 当成自然常数。固定单机环境在快速回归中仍合理；跨机器 replay 只在 benchmark 要承担 跨系统比较或发布决策时值得支付成本。Performance-Optimization Benchmark Reliability 的作者研究支持这种 reference-first 审计，但不证明其任务集覆盖生产优化分布。 Reference 可以稳定重放，仍不意味着它准确表达了请求。代码检索尤其容易暴露这个差别：query 只要求处理正整数， 测试却额外要求非正数返回某个值，那么删除这个额外分支的程序可能在声明输入域内完全正确，却被测试判错。 因此 evaluator 要分别固定自然语言任务、允许的输入域、reference 与 test oracle；oracle 拥有可执行判定， 不自动拥有扩充需求的权力。发现域不一致时，应补明任务合同、修正测试，或将结果限定为“符合这个 oracle”， 不能直接提升为“语义正确”。这比只验证 reference 能运行更昂贵，却能避免把生成测试的偏差当成模型失败。 还要检查多个指标是否真的提供独立证据。若冻结的检索语料为每个 query 只安排一个可通过测试的 canonical snippet， 且不存在其他通过项，那么“top-k 中至少一项执行通过”恰好等于
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：以 agentic audit 重放 task specification、environment dependency 与 grader logic；发现的问题经专家/上游修复验证后会改变分数和模型排序，因此 benchmark task 本身必须先通过 admission。
- **Books：** `No Change — Existing Coverage`；owner 为 `PLATFORM-EVALUATION-SYSTEM` / [`books/part-06-ai-infrastructure/66-evaluation-system.md`](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.26089 Channel-wise Vector Quantization](https://arxiv.org/html/2605.26089v1)

- **为什么进入 denominator：** 它改变视觉 token 的基本量化轴，使 representation identity、序列 factorization 与生成顺序成为同一个系统合同，而非单一任务精度增量。
- **方法定位：** §3.1 Channel-wise Vector Quantization；§3.2 Channel-wise Autoregressive Generation；Appendix B nested channel dropout。
- **评价定位：** §4.1–§4.3 reconstruction/generation、matched VQ comparisons、codebook/dropout ablations；Appendices C–E。
- **限制/反证：** §5 与 Appendix D 只给 image 设置；channel 没有天然顺序，variable resolution 依赖额外 resampling，视频和统一理解仍未证明。
- **证据边界与回退：** exact-v1 只支持作者披露数据、模型和 matched token-budget；不能宣称 channel token 普遍优于 patch token。ordering、resampler 或 generation quality 回归时回退 patch/grid VQ、普通 1D tokenizer 或独立生成路径。
- **Books：** `Applied`；owner=`MULTIMODAL-REPRESENTATION` / Ch23；root 已写入 paired binding，fresh non-author 验收通过。

### [2605.26097 Forgetting in Language Models: Capacity, Optimization, and Self-Generated Replay](https://arxiv.org/html/2605.26097v1)

- **为什么进入 denominator：** 它把 continual SFT 的 retention signal、剩余容量与 learning-rate/step compute 放进同一可证伪设计边界，修正“只要降低 LR 或加 replay 就能防遗忘”的过度简化。
- **方法定位：** §2 self-generated replay/KL；§3 capacity saturation；§4 LR/compute trade-off；§5 instruction-tuned case。
- **评价定位：** Figures 2–9 的 controlled mixtures、容量/LR sweeps 与 Llama-3.2-1B-Instruct/Verilog slice。
- **限制/反证：** §7 明确多数实验 ≤46M、主要为一个新任务，只有 Figure 9 达 1B；capacity 只由 proxy 间接测量。
- **证据边界与回退：** exact-v1 不证明 BOS samples 覆盖真实 pretraining distribution，也不覆盖多任务、frontier scale 或生产安全回归。retain slices、replay distribution 或容量 proxy 失效时，回退真实 replay、低 LR/早停、adapter/扩容或停止更新。
- **Books：** `Applied`；owner=`TRAIN-SFT` / Ch29；root 已写入 paired binding，fresh non-author 验收通过。

### [2605.26099 Language Models Need Sleep](https://arxiv.org/html/2605.26099v1)

- **采用命题：** 周期性 offline recurrence 在清空 KV 前把 recent context 整理进 persistent fast weights，并用可调 sleep passes 把深层推理计算从 wake-time decode 移到有界离线阶段；runtime 因而必须共同拥有 sleep trigger、fast-state version、KV clear/commit 与失败回退。
- **方法定位：** §5 LLM Sleep: Offline Recursive Memory Consolidation。
- **评价定位：** §6.1–§6.5 cellular automata、Depo、GSM-Infinite、sliding-window eviction 与 training-throughput experiments。
- **限制/反证：** §7 Discussion and Limitations；受控任务、hybrid attention/SSM architecture 与额外 offline compute boundary。
- **证据边界：** exact-v1 只证明作者 hybrid architecture 与披露任务/schedule 下的受限收益；不证明任意长上下文无损压缩、frontier serving、多租户隔离、迁移、恢复或生产 tail-SLO。
- **差异判断：** Ch22 已拥有 fast-weight mutable-state identity、reset/checkpoint 与 KV/recurrent/RAG 分工，但未承载在 KV clear 前执行多轮 offline recurrence、以 gate 原子提交 fast state并把计算移到 sleep budget 的控制分支。
- **Books：** `Applied`；owner 为 `MODEL-LONG-CONTEXT` / [`books/part-02-model/22-long-context.md`](../../../../books/part-02-model/22-long-context.md)。正文 paired binding 已写入；exact-v1 机制与系统设计推论保持明确分离，start marker 位于完整采用段落之前，fresh non-author 终审通过。

### [2605.26110 Prism: A Plug-in Reproducible Infrastructure for Scalable Multimodal Continual Instruction Tuning](https://arxiv.org/html/2605.26110v1)

- **采用命题：** 以 plugin registration 将 continual-tuning algorithm state 与 MLLM backbone/runtime 解耦，使新策略无需改写底座即可在同一 scalable pipeline 中复现和公平比较。
- **方法定位：** §3 backbone/plugin boundary, registration API and scalable training integration
- **评价定位：** §4 reproducibility/continual-tuning method comparisons
- **限制/反证：** §5 limitations: research codebase, supported backbones and no production fault study
- **证据边界：** 只支持 Prism: A Plug-in Reproducible Infrastructure for Scalable Multimodal Continual Instruction Tuning exact-v1 披露的方法与 evaluation envelope；未测试的模型、硬件、并发、tail-SLO、攻击分布和生产泛化均未证明。
- **Books：** `Applied`；owner 为 `PLATFORM-TRAINING-OPERATOR` / [`books/part-06-ai-infrastructure/60-training-operator.md`](../../../../books/part-06-ai-infrastructure/60-training-operator.md)。Fresh non-author post-write semantic review passed; the paired binding remains before the first main H2 Review notes.

### [2605.26112 From Model Scaling to System Scaling: Scaling the Harness in Agentic AI](https://arxiv.org/html/2605.26112v1)

- **采用命题：** 把 context governance、memory、skill routing、orchestration、verification 与 governance 组成可版本化 agent harness，并把 harness-level trajectory、memory hygiene、communication fidelity 与 safe evolution 纳入评价对象。
- **方法定位：** §3 harness infrastructure and temporal layers; §4 context/memory/skill bottlenecks
- **评价定位：** §5 process/longitudinal evaluation and safe evolution argument
- **限制/反证：** §6 alternative views and limitations; position/framework paper without controlled deployment study
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `本章要回答的问题` — 一个 Agent demo 变成平台后，需要管理哪些新对象和控制闭环？Agent Platform 与 Part VI AI Platform 是两套系统吗？如何评估一个长期执行、调用工具并产生副作用的 Agent？ 本章的核心判断是：**Agent Platform 是 AI Platform 对有状态行动循环的扩展。它统一 Agent definition、run、context、memory、tools、workflow、evaluation 与 policy，但复用 Part VI 的 identity、resource、evidence、cost、tenancy、security 和 recovery substrate。** 本章先确定可部署 definition、run 与可复用能力资产的身份，再把它们放入 control、execution 与 evidence 三个 平面，随后讨论 scheduling、policy、evaluation、release 与 feedback。顺序很重要：没有冻结对象身份，后面的 资源归因、权限判断和演化证据都无法比较。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：把 context governance、memory、skill routing、orchestration、verification 与 governance 组成可版本化 agent harness，并把 harness-level trajectory、memory hygiene、communication fidelity 与 safe evolution 纳入评价对象。
- **Books：** `No Change — Existing Coverage`；owner 为 `AGENT-PLATFORM` / [`books/part-07-agent/84-agent-platform.md`](../../../../books/part-07-agent/84-agent-platform.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [2605.26114 MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research](https://arxiv.org/html/2605.26114v1)

- **采用命题：** 把完整 mobile environment state 表示为可配置、fork 和比较的 structured JSON，并以同一 deterministic state judge 同时提供 evaluation verdict 与 dense RL reward，从而支持高并发可验证 rollout。
- **方法定位：** §3.1 layered state model; §3.2 programmable/serializable state and verifiable outcomes
- **评价定位：** §4 protocol; §5 benchmark, sim-to-real, judge error and efficiency
- **限制/反证：** §6 listed visual/backend/app/legal/misuse limitations
- **证据边界：** Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.
- **当前正文承载：** `Model 与 data-generating harness 是共同演进的配对 artifact` — Agent 能力不仅由 weights 决定，也由生成任务、环境状态、tool feedback 和评分证据的 harness 塑造。只优化模型会过拟合旧 harness，只升级 harness 又会让既有 checkpoint 失去可比性。平台应把 model revision 与 harness revision 成对注册，交替优化时保留 cross-product regression：新模型跑旧/新 harness，旧模型也跑新 harness。 联合演进扩大探索空间，却增加版本组合和 benchmark overfitting。有限实验不证明某种 co-evolution schedule 最优；生产 release 仍需冻结独立 holdout/environment，无法解释回归时回退上一对已验证 artifact。
- **差异判断：** 该正文已经承担稳定机制；本 exact-v1 只补充受限实现/反证：把完整 mobile environment state 表示为可配置、fork 和比较的 structured JSON，并以同一 deterministic state judge 同时提供 evaluation verdict 与 dense RL reward，从而支持高并发可验证 rollout。
- **Books：** `No Change — Existing Coverage`；owner 为 `AGENT-PLATFORM` / [`books/part-07-agent/84-agent-platform.md`](../../../../books/part-07-agent/84-agent-platform.md)。Main-body heading/excerpt before the first H2 Review notes carries the durable proposition; exact difference is recorded.

### [minimax:sparse-token-forgetting Why Can't the MiniMax LLM Say "Ma Jiaqi"? Internal Investigation of Sparse Token Forgetting](https://www.minimax.io/blog/sparse-token-forgetting)

- **采用命题：** SFT 不只监控 task/domain coverage，还要监控 token-as-target coverage 与 pretrain→SFT `lm_head` drift；全词表重复数据可保底但可能浪费容量或损害会话能力，Korean 反例说明失败时需回退数据清洗、targeted synthesis、受控 replay 或 CPT。
- **方法定位：** Hypothesis 1–2; Exploring Intermediate Metrics
- **评价定位：** Validation & Repair Experiments
- **限制/反证：** Korean non-fix and Other Directions Worth Exploring
- **证据边界：** 只支持 MiniMax 披露的 M2-series pretrain→SFT 对比、token/language slices、全词表重复数据配方与对应实验；未披露训练 artifact 和跨模型复现，且 Korean 非修复反例阻止把全词表补数外推为通用方案。
- **Books：** `Applied`；owner 为 `TRAIN-SFT` / [`books/part-04-training-system/29-sft.md`](../../../../books/part-04-training-system/29-sft.md)。Fresh non-author post-write semantic review passed; the marker remains globally unique and before the first main H2 Review notes.

## 5. 缺口与下一步

Evidence 无 access blocker。fresh closure challenge 在冻结 692 owner corpus 内追加恢复 `2605.26089` 与 `2605.26097`，没有扩日期或来源；两项 exact-v1 与 root Books 写回均已完成，root queue 当前为 0 pending。此前 `2605.26099` 的 Ch22 paired marker 已覆盖完整命题，并明确区分论文支持与项目对 atomic commit/recovery 的系统推导，本轮复核通过。Meta 与 MiMo 的来源级限制作为本窗终态保留项隔离：不用于正面证据、Books 或无遗漏断言；定点重开条件是对应官方入口恢复并提供本窗口可核验的事件清单或技术正文。

## 6. 复核

复核者：fresh non-author；未参与此前 denominator/Evidence rebuild、root Books 写回或路径修复。

结论：通过

- **核验范围：** 仅确认 `2605.26089` adjacent path 已修正为真实的 `17-transformer-layer.md`，并复核 `2605.26089`、`2605.26097`、`2605.26099` 既有写后语义结果、canonical 账目、queue、markers 与 validator；未扩源或重审全文。
- **当前账目：** `692=94 retained+598 closure`；`94 deep`；`61 Applied + 33 No Change + 0 pending Integrate`；root queue=`0 pending`。
- **验收结果：** 三项目标 owner/adjacent path 均存在，paired marker 各一组且位于首个主 `## Review notes` 之前；canonical pending-review 状态已同步为通过。
- **收据：** [`FRESH_NONAUTHOR_V3_FINAL_PASS_20260916_R3.md`](../_sources/daily-20260527/FRESH_NONAUTHOR_V3_FINAL_PASS_20260916_R3.md)。
