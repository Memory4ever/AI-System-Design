# Daily Research — 2026-06-11

**规范：** V3  
**窗口：** 2026-06-10T09:00:00+08:00 ～ 2026-06-11T09:00:00+08:00  
**状态：** 完成
**Books：** 纳入本次  
**检查时间：** 2026-10-26T08:24:32+08:00
**原检查时间：** 2026-09-11T12:45:00+08:00
**窗口说明：** 用户明确仅补遗漏，保留旧候选日期、评分、小时窗及有效证据；旧完成声明只描述旧轮，不代替本轮验收。
**补充窗口：** 2026-06-10 ～ 2026-06-10
**冻结候选日期：** [补查前原报告](../_sources/daily-20260611/baseline-before-supplement-20261026.md)

## 1. 结论

本轮新增42个唯一材料家族，全部经过完整题摘的具体贡献准入与合法日期核验；有限来源/主题发现已到停止点，1361宽导航不是审阅队列。新增已安全处置为37项真实Books整合、2项具体已有覆盖、3项中心争议隔离，候选普通必要/Books待办为0；非作者唯一[DAY §101](../_sources/daily-20260611/SUP_REVIEW_20261026.md#101-jun11补查唯一完整日级验收day通过安全终态)已通过，本日报完成安全终态，不授外部保留项Coverage/Evidence通过。旧52家族日期/评分/小时窗和有效层保留，新增不以整合率或数量配额取舍。当前入口/停止见[来源检查](../_sources/daily-20260611/SUP_SOURCE_CHECK_20261026.md)，完整题摘及准入见[校准](../_sources/daily-20260611/SUP_ADMISSION_20261026.md)，必要/唯一稿见[证据](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)，实际独核见[review](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

下列旧轮统计与完成结论仅适用于原小时窗及当时已审事件，不是新增自然日来源检查完成声明：

对本目录 bounded canonical raw bucket 的全部 562 个 identity 已完成 title + complete abstract 准入审计；fresh-context 独立复核将 2 个误收项改为分母前关闭，最终冻结 52 个 Candidate、510 个 family-specific audited Close，满足 `562 raw = 52 Candidate + 510 audited Close`，ordinary pending=0。候选 exact-v1 Evidence Review 与 Books 比较也已独立复核：10 项确有正文增量并已写入 Books，40 项由现有章节覆盖，2 项仅报告。10 条正文均位于首个顶层 `Review notes` 前，具备机制、owner、收益、trade-off、failure、fallback 与证据边界；7 条 trace 日期修正已复验，剩余执行队列为 0。日期 owner 不由 submitted/v1 timestamp、identifier sequence、DataCite created 或 normal cutoff 推导；official historical listing receipt 到位前不执行跨日迁移，该保留限制不阻塞本日报闭环。

当前合同评分已由非作者重新校准，不以已经深读或已经写入 Books 倒推高分。52 项现在分布为 `5 分 × 2、6 分 × 40、8 分 × 10`；既有 exact-v1 深审仍可复用，最低审阅等级按新分数表述。逐项旧分、新分和三维依据见 [current score recalibration](../_sources/daily-20260611/CURRENT_SCORE_RECALIBRATION_20260914.json)。

## 2. 来源覆盖

本表为本轮Jun10自然日实际入口与停止范围；完整原参数、语义排除和恢复边界见[来源记录](../_sources/daily-20260611/SUP_SOURCE_CHECK_20261026.md)。旧[source recert](../_sources/daily-20260611/CURRENT_SOURCE_RECERT_20260914.md)只保其历史有效层，不代替本表。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS单响应1318项，目标邻段两项Jun10原件核心：influence campaign与LSEG adoption；贡献前具体关闭，不展开全年 | 已检查 | 无；不称全网零发布 |
| SRC-ANTHROPIC | Research历史listing/default/2，共24条；Jun12→Jun08越过目标，停第2页 | 已检查 | 无本日具名Research项 |
| SRC-GOOGLE-AI | DeepMind Blog第2页与Research六月单页12项；DiffusionGemma准入，unlearning Blog仅介绍Jan28旧研究 | 受阻 | Publications历史日级完整目录未恢复，不能由Blog代证 |
| SRC-META-AI | 官方Research/Blog与具名Jun10检索；可见Jun29→Apr08，停止当前目录及精确日期线索 | 受阻 | Research历史日级目录未恢复，不授零研究 |
| SRC-QWEN | 官方retrieval type=qwen_ai，中英各40项无分页；Jun01→Jun16越过目标 | 已检查 | 无Jun10条目；未用无参空响应 |
| SRC-DEEPSEEK | 官网与API updates相邻Apr24→Jul31，目标间无具名Jun10项 | 已检查 | 无；只约定官方入口 |
| SRC-MOONSHOT | Platform Blog可见最新2025-11-07；GitHub org单页42repo及精确日期补检已停止 | 受阻 | Blog不足覆盖2026；repo更新时间不证首公开，非全机构零发布 |
| SRC-TENCENT-HUNYUAN | Research中文All官方API页1 size100，total11/list11；Jul06→May21，停止单页 | 已检查 | 无Jun10；中文header与原参数见来源记录 |
| SRC-ZAI | Research日期排序Jun16→May20，越过目标，停止首目录目标邻段 | 已检查 | 无Jun10具名项 |
| SRC-BYTEDANCE-SEED | public_papers第1页1–20/247，Jun11→Jun04→Jun03，停止第1页 | 已检查 | 科学应用仅导航，不扩领域 |
| SRC-BAIDU-ERNIE | 技术Blog最新May09早于目标，停止当前目录 | 已检查 | 无Jun10具名项 |
| SRC-XIAOMI-MIMO | 官方SSR Jun10 long-horizon原件准入；route邻段Jun08→Jun10，ModelRelease Jun02→Sep22另核 | 已检查 | 无；Blog事件不被无模型release抹去 |
| SRC-MINIMAX | 官方Blog目标邻段Jun09→Jun01，停止单目录 | 已检查 | 无Jun10具名项 |
| SRC-ARXIV | DataCite同arxiv.content registered窗：两有限主题单页269/128按ID去重浏览相关题名与完整题摘；宽1361仅导航，官方月列表只作有界线索 | 受阻 | 日公告端点/月列表无日分组，五项合法上下界仍跨日，具名隔离；非全学科召回 |

旧562目录的[历史准入审计](../_sources/daily-20260611/v3-reverse-admission-audit-20260910.json)与[字段表](../_sources/daily-20260611/denominator-full-semantic-audit-v1.tsv)仅保原52去重/证据，不因其存在继续整类逐项审阅。日期规则按当前研究合同：唯一v1日程最早界与同DOI的arxiv.content/findable registered最晚界合法联合；不是submitted/created单字段，也不把registered重命名为实际时刻。整个界均落Jun10才列新增候选，跨日者在§5隔离；不迁移用户要求保留的旧日期。

## 3. 候选与判断

### Jun10自然日新增（42家族，当前进度）

前42行为Jun10自然日新增，日期按本轮原件/合法联合界核到2026-06-10；10747另保更早Jun6口头talk、未得更早正文的限定。后52行为用户要求保留的旧候选，原日期/评分/小时窗与有效证据不变，不因新增重计。新增评分只针对其具体增量，全部已获安全处置。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [MiMo Code Long-Horizon](https://mimo.xiaomi.com/blog/mimo-code-long-horizon) | 2026-06-10 | 提前增量抽取与换窗装配分责，非单writer原子最新；2+2+2=6 | 深入完成 | 整合：AGENT-CONTEXT，[Compaction首段后](../../../../books/part-07-agent/75-context.md) |
| [Piper: A Programmable Distributed Training System](https://arxiv.org/html/2606.11169v1) | 2026-06-10 | 策略指令编译统一计算/通信DAG与每设备执行计划；2+2+2=6 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[手写Plan→planner末段后](../../../../books/part-04-training-system/36-distributed-training.md) |
| [DiffusionGemma](https://developers.googleblog.com/en/diffusiongemma-the-developer-guide/) | 2026-06-10 | 低并发块内并行与高QPS已有batch摊权重的共存边界；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[ParallelProgress首段后](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [The Role of Feedback Alignment in Self-Distillation](https://arxiv.org/html/2606.11173v1) | 2026-06-10 | 批评反馈逐字锚点可强化错token或压低正确token；2+1+2=5 | 深入完成 | 整合：TRAIN-SFT，[ContextDistillation概念末](../../../../books/part-04-training-system/29-sft.md) |
| [Multi-Faceted Interactivity Alignment in Full-Duplex Speech Models](https://arxiv.org/html/2606.11167v1) | 2026-06-10 | 多轴交互reward仍可反退未被judge覆盖的Safety-task维度；2+1+2=5 | 深入完成 | 已有覆盖：TRAIN-RLHF，[Evaluation独立于RewardModel的ensemble盲区段](../../../../books/part-04-training-system/31-rlhf.md) |
| [Optimal Post-Training Quantization Scales and Where to Find Them](https://arxiv.org/html/2606.10890v1) | 2026-06-10 | 有限RTN区间优化与exact-global attainment边界；2+1+3=6 | 争议 | 暂缓：C10负权重ties-up反例；见§4/§5 |
| [ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models](https://arxiv.org/html/2606.11164v1) | 2026-06-10 | prefill静态预算不能代CoT动态需求，数量分配与淘汰分责；2+1+2=5 | 标准完成 | 已有覆盖：INFER-KV-CACHE，[CoT adaptive layer/head与prefill/decode统计段](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Recoverable but Not Stationary:Local Linear Structures in Weights and Activations](https://arxiv.org/html/2606.10929v1) | 2026-06-10 | 单点局部task-plane低rank不等整段恢复固定支集；2+1+3=6 | 深入完成 | 整合：TRAIN-LORA，[TLoRA段后](../../../../books/part-04-training-system/30-lora.md) |
| [When to Align, When to Predict: A Phase Diagram for Multimodal Learning](https://arxiv.org/html/2606.11190v1) | 2026-06-10 | CA/CP对signal与相关nuisance的谱竞争、方向与MSE反侧；2+2+3=7 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[对齐centroid/pair首段后](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [The Arbiter Agent: Continually Monitoring Multi-Agent Conversations to Detect Emergent Misalignment](https://arxiv.org/html/2606.10747v1) | 2026-06-10 | 同neutral人口、无SP/CoT下主动问询+log与被动观察差额；2+2+2=6 | 深入完成 | 整合：AGENT-MULTI-AGENT，[Fleetoversight末/角色正确性前](../../../../books/part-07-agent/82-multi-agent.md) |
| [K-Forcing: Joint Next-K-Token Decoding via Push-Forward Language Modeling](https://arxiv.org/html/2606.10820v1) | 2026-06-10 | iid noise条件的联合k-token映射与递进蒸馏/临时noise状态；2+1+3=6 | 深入完成 | 整合：MODEL-DECODER-ONLY，[conceptclock末/历史生产前](../../../../books/part-02-model/18-decoder-only.md) |
| [A Theory on Flow Matching with Neural Networks](https://arxiv.org/html/2606.10089v1) | 2026-06-10 | 两层ReLU学习到样本W1的采样桥接条件；2+1+3=6 | 争议 | 暂缓：F1半径越界及端点Lip缺口；见§4/§5 |
| [Mean Flow Distillation: Robust and Stable Distillation for Flow Matching Models](https://arxiv.org/html/2606.11155v1) | 2026-06-10 | aux分布场、同起点区间位移guidance与Jacobian近似分账；2+1+3=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[K-DMD段后](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Unifying Local Communications and Local Updates for LLM Pretraining](https://arxiv.org/html/2606.11081v1) | 2026-06-10 | pre/post-local纠偏改变inner/outer/gossip优化与baseline资格；2+2+2=6 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[09970 gossip段后/后验采样前](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Flow-DPPO: Divergence Proximal Policy Optimization for Flow Matching Models](https://arxiv.org/html/2606.11025v1) | 2026-06-10 | 逐步Gaussian exactKL与方向性divergence mask；2+1+2=5 | 深入完成 | 整合：TRAIN-PPO，[owner](../../../../books/part-04-training-system/32-ppo.md)；KLpenalty末Estimator后，实际POST通过 |
| [Beyond Uniform Token-Level Trust Region in LLM Reinforcement Learning](https://arxiv.org/html/2606.10968v1) | 2026-06-10 | 位置阈值和累计prefix偏离共同约束PPO；2+1+3=6 | 深入完成 | 整合：TRAIN-PPO，[owner](../../../../books/part-04-training-system/32-ppo.md)；29999完整marker后/Nstep前，实际POST通过 |
| [Provenance-Grounded Gating and Adaptive Recovery in Synthetic Post-Training Data Curation](https://arxiv.org/html/2606.11127v1) | 2026-06-10 | 来源gate与reward人口分歧、拒例诊断再生与scale主效应；2+1+2=5 | 深入完成 | 整合：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；Synthetic首概念后，实际POST通过 |
| [Exploring the Design Space of Reward Backpropagation for Flow Matching](https://arxiv.org/html/2606.11075v1) | 2026-06-10 | 无grad采样与backward surrogate分轨及有限Jacobian链；2+2+2=6 | 深入完成 | 整合：TRAIN-RLHF，[owner](../../../../books/part-04-training-system/31-rlhf.md)；21654完整binding后，实际POST通过 |
| [Provenance Tracking in AI Compilers through the Lens of Coalgebra](https://arxiv.org/html/2606.10937v1) | 2026-06-10 | 非单射rewrite下observable action/bisimulation的provenance条件；2+2+2=6 | 争议 | 暂缓：F/Fsharp观测与完整R/bisimulation缺口；见§4/§5 |
| [Express Language Modeling](https://arxiv.org/html/2606.10944v1) | 2026-06-10 | 非causal近似到causal的误差/有界memory转换；2+2+3=7 | 深入完成 | 整合：MODEL-SELF-ATTENTION，[改变算子节首概念后](../../../../books/part-02-model/14-self-attention.md) |
| [Attention Amnesia in Hybrid LLMs: When CoT Fine-Tuning Breaks Long-Range Recall, and How to Fix It](https://arxiv.org/html/2606.11052v1) | 2026-06-10 | hybrid CoT-SFT损长程QK路由与局部恢复反证；2+2+2=6 | 深入完成 | 整合：TRAIN-SFT，[11426 activation段后](../../../../books/part-04-training-system/29-sft.md) |
| [Attention-Discounted Adaptive Sampler for Masked Diffusion Language Models](https://arxiv.org/html/2606.10829v1) | 2026-06-10 | 固定reveal数量时set内attention交互改变subset选择；2+1+3=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；AXON04236完整marker后，实际POST通过 |
| [miniReranker: Efficient Multimodal Reranking through Visual Cache Reuse and Interaction Sparsity](https://arxiv.org/html/2606.10759v1) | 2026-06-10 | vision-first前缀复用方向与窄交互带cache资格；2+1+2=5 | 深入完成 | 整合：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；FusionRAG12904完整marker后，实际POST通过 |
| [Dynamic Linear Attention](https://arxiv.org/html/2606.10650v1) | 2026-06-10 | 信息变化决定state边界、相邻合并的有界时间缓存；2+1+2=5 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[owner](../../../../books/part-02-model/22-long-context.md)；MemoryCaching首段后，实际POST通过 |
| [Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design](https://arxiv.org/html/2606.10493v1) | 2026-06-10 | 小EP token复制/本地gate/局部reduce的dispatch取舍；2+2+2=6 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[owner](../../../../books/part-04-training-system/36-distributed-training.md)；ThunderEP40093完整marker后，实际POST通过 |
| [ASTRA-sim 3.0: Next-Level Distributed Machine Learning Simulations via High-Fidelity GPU and Infrastructure Modeling](https://arxiv.org/html/2606.10440v1) | 2026-06-10 | cacheline/GPU控制数据路径与InfraGraph细化模拟；2+2+2=6 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[owner](../../../../books/part-04-training-system/36-distributed-training.md)；alphaBeta概念末/bytes效率前，实际POST通过 |
| [How Does Reasoning Flow? Tracing Attention-Induced Information Flow for Targeted RL in LLMs](https://arxiv.org/html/2606.10646v1) | 2026-06-10 | answer可达attention DAG的局部守恒信用代理；2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；SequenceReward粗糙性说明后，实际POST通过 |
| [What Fits (Into Few Tokens) Doesn't Overfit: Compression and Generalization in ML Research Agents](https://arxiv.org/html/2606.11045v1) | 2026-06-10 | 短策略fresh复现与一bit反馈/诱导overfit的反侧；2+2+3=7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；28798完整marker后，实际POST通过 |
| [Frontier Coding Agents Use Metaprogramming to Adapt to Unfamiliar Programming Languages](https://arxiv.org/html/2606.10933v1) | 2026-06-10 | 禁metaprogramming、代码helper与文字指导及预算效应；2+1+2=5 | 深入完成 | 整合：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；Agentfriendly末/ResourceLowering前，实际POST通过 |
| [Pushing the Limits of LLM Tool Calling via Experiential Knowledge Integration and Activation](https://arxiv.org/html/2606.10875v1) | 2026-06-10 | 实例经验相对抽象意图、宽采样相对深推理的条件；2+1+2=5 | 深入完成 | 整合：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；ToolDiscovery首概念位，实际POST通过 |
| [Janus: A Benchmark for Goal-Conditioned Information Distortion in LLMs](https://arxiv.org/html/2606.10852v1) | 2026-06-10 | 固定事实池中目标驱动的遗漏/强调仍能误导；2+1+3=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；18280输出验收后/26242前，实际POST通过 |
| [MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents](https://arxiv.org/html/2606.10742v1) | 2026-06-10 | 多模态图记忆的召回触发与读取后动作诱导两阶段风险；2+2+2=6 | 深入完成 | 整合：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；poisonchain checkpoint后/Repair前，实际POST通过 |
| [Effective Reinforcement Learning for Agentic Search by Recycling Zero-Variance Queries During Training](https://arxiv.org/html/2606.10709v1) | 2026-06-10 | zero-variance query资格随policy变化、mutable pool重采；2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO，[06375完整admission末/Pareto探测前](../../../../books/part-04-training-system/33-grpo.md) |
| [CLP: Collocation-Length Prediction for Zero-Loss Adaptive Multi-Token Inference](https://arxiv.org/html/2606.10935v1) | 2026-06-10 | 首token属backbone、后续MTP span门与非exact资格；2+1+2=5 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING，[效用仲裁24793 marker后/WISV前](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Continual LLM Upcycling: A Predictor-Gated Bank-Wise Sparsity Training Recipe for Dense-to-Sparse LLMs](https://arxiv.org/html/2606.10722v1) | 2026-06-10 | bank-sparse训练layer-local长程失效与单层修复；2+1+2=5 | 深入完成 | 整合：MODEL-FFN，[00454 marker后/01973前](../../../../books/part-02-model/16-feed-forward-mlp.md) |
| [SSR-Merge: Subspace Signal Routing for Training-Free LoRA Merging in Diffusion Models](https://arxiv.org/html/2606.10617v1) | 2026-06-10 | 低秩信号decorrelation/路由的OLS与统计支持条件；2+1+3=6 | 深入完成 | 整合：TRAIN-LORA，[多个Adapter能否直接相加后/CompositionAdmission前](../../../../books/part-04-training-system/30-lora.md) |
| [Fast and Highly Expressive Policy Learning for Offline Reinforcement Learning via Bootstrapped Flow Q-Learning](https://arxiv.org/html/2606.10613v1) | 2026-06-10 | 短程displacement自举单步action、无需额外teacher的条件；2+1+3=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[少步蒸馏组合一致完整概念段后/提升observables固定矩阵段前](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [SpenseGPT: Practical One-shot Pruning Enabling Sparse and Dense GEMMs for LLM Inference](https://arxiv.org/html/2606.10445v1) | 2026-06-10 | dense与2:4区域分区格式可由现有GEMM消费；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM，[23410 marker后/28947前](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Parallel Causal Associative Fields: Gated Sparse Memory for Long-Context Language Modeling](https://arxiv.org/html/2606.10435v1) | 2026-06-10 | 有界causal successor cache与localLM gate的资源/因果取舍；2+1+3=6 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[远期memorybank末/外部工作集前](../../../../books/part-02-model/22-long-context.md) |
| [RATrain: A Resource-Aware Training Runtime for Large Language Models on Bandwidth-Constrained Heterogeneous Supercomputing Platforms](https://arxiv.org/html/2606.10415v1) | 2026-06-10 | MT3000显式层级内存下1F1B状态生命周期计划；2+2+2=6 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[Piper11169完整段marker后/从Phase串行主标题前](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Reasoning or Memorization? Direction-Aware Diversity Exploration in LLM Reinforcement Learning](https://arxiv.org/html/2606.10346v1) | 2026-06-10 | reasoning/shortcut方向加权gradient多样性奖励的可识别性；2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO，[DQO04784完整marker后/同题正确rollout稀有度分支前](../../../../books/part-04-training-system/33-grpo.md) |
| [UniSVQ: 2-bit Unified Scalar-Vector Quantization](https://arxiv.org/html/2606.10520v1) | 2026-06-10 | integer lattice仿射codeword与VQ/整数kernel兼容边界；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM，[10496 productLUT完整实现限制段后/重复weight在线乘积复用段前](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |

| [PoQ-Judge: A Multi-Architecture Evaluation Framework for Cost-Aware Proof-of-Quality in Decentralized LLM Inference](https://arxiv.org/html/2606.11196v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《PoQ-Judge: A Multi-Architecture Evaluation Framework for Cost-Aware Proof-of-Quality in Decentralized LLM Inference》关闭或降池；完整摘要显示“We present PoQ-Judge, a framework that trains dedicated judge models to score query-output pairs without ground-truth references.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [The Structural Attention Tax: How Retrieval Format Hijacks In-Context Learning Independent of Content](https://arxiv.org/html/2606.11198v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《The Structural Attention Tax: How Retrieval Format Hijacks In-Context Learning Independent of Content》关闭或降池；完整摘要显示“We develop a formal framework decomposing attention scores into semantic and structural components (Eq.”。该增量直接改变 AGENT-RAG 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；正文写入与独立 post-write audit 已完成 |
| [Beyond Compaction: Structured Context Eviction for Long-Horizon Agents](https://arxiv.org/html/2606.11213v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Beyond Compaction: Structured Context Eviction for Long-Horizon Agents》关闭或降池；完整摘要显示“We present Context Window Lifecycle (CWL), a context-management scheme that gives long-horizon LLM agents an effectively unbounded working horizon.”。该增量直接改变 AGENT-CONTEXT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-CONTEXT，[owner](../../../../books/part-07-agent/75-context.md)；正文锚点：Context Compression 必须保留执行状态，而不只是语义 |
| [SPEAR: A System for Post-Quantization Error-Adaptive Recovery Enabling Efficient Low-Bit LLM Serving](https://arxiv.org/html/2606.11244v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《SPEAR: A System for Post-Quantization Error-Adaptive Recovery Enabling Efficient Low-Bit LLM Serving》关闭或降池；完整摘要显示“We present SPEAR, a system for post-quantization error-adaptive recovery that improves low-bit LLM serving.”。该增量直接改变 INFER-TENSORRT-LLM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；正文写入与独立 post-write audit 已完成 |
| [When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines](https://arxiv.org/html/2606.11265v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“Based on this observation, we propose Chunk-aware and Rerank-Consistent Poisoning (CRCP), a poisoning framework that jointly optimizes retrieval relevance, reranker consistency, and chunk-boundary robustness.”，该机制在 AGENT-RAG 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；正文锚点：RAG 安全必须覆盖完整状态生命周期 |
| [Quantifying Subliminal Behavioral Transfer Ratios in Language Model Distillation](https://arxiv.org/html/2606.11270v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“While qualitative evidence supports the existence of this effect, its magnitude has not been systematically characterized.”，该机制在 TRAIN-DATA 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文锚点：Data lineage 是训练可复现性的前提 |
| [FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse](https://arxiv.org/html/2606.11290v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“To this end, we present FlowBank, a three-stage framework for portfolio-based agentic workflow optimization.”，该机制在 AGENT-WORKFLOW 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；正文锚点：State Machine 是基本模型 |
| [Knowing When to Ask: Self-Gated Clarification for Hierarchical Language Agents](https://arxiv.org/html/2606.11349v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“Rather than treating clarification as an external uncertainty trigger, we propose ACTION-RATING, a formulation that places it inside the agent's action space on a shared ordinal scale with navigation, so that asking competes directly with acting at every decision point and help-seeking becomes observable at intermediate states.”，该机制在 AGENT-PLANNING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-PLANNING，[owner](../../../../books/part-07-agent/79-planning.md)；正文锚点：从目标到状态图 |
| [When More Documents Hurt RAG: Mitigating Vector Search Dilution with Domain-Scoped, Model-Agnostic Retrieval](https://arxiv.org/html/2606.11350v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《When More Documents Hurt RAG: Mitigating Vector Search Dilution with Domain-Scoped, Model-Agnostic Retrieval》关闭或降池；完整摘要显示“To address this dilution, we propose MASDR-RAG ( Multi-Agent Scoped Domain Retrieval for RAG) and evaluate it on 200 expert-validated queries across five LLM backbones, six corpora, and two index stacks.”。该增量直接改变 AGENT-RAG 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；正文锚点：Online Retrieval Pipeline |
| [TileFuse: A Fused Mixed-Precision Kernel Library for Efficient Quantized LLM Inference on AMD NPUs](https://arxiv.org/html/2606.11357v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“In this work, we present TileFuse, a close-to-metal mixed-precision kernel library for AMD XDNA2 NPUs that targets GEMM/GEMV-based operators in quantized LLM inference.”，该机制在 INFER-DECODE 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-DECODE，[owner](../../../../books/part-05-inference-system/44-decode.md)；正文锚点：端侧融合必须围绕真实 Tile / Dataflow Contract |
| [When Probing Accuracy Saturates, Fragility Resolves: A Complementary Metric for LLM Pre-Training Analysis](https://arxiv.org/html/2606.11375v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《When Probing Accuracy Saturates, Fragility Resolves: A Complementary Metric for LLM Pre-Training Analysis》关闭或降池；完整摘要显示“We introduce fragility, a complementary per-layer metric defined as the activation-noise level at which probe accuracy collapses.”。该增量直接改变 TRAIN-PRETRAINING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：TRAIN-PRETRAINING，[owner](../../../../books/part-04-training-system/28-pretraining.md)；正文写入与独立 post-write audit 已完成 |
| [Small Experiments, Cheaper Decisions: A Case Study in Staged Promotion for Micro-Pretraining](https://arxiv.org/html/2606.11387v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We study an auditable staged-promotion protocol for a fixed micro-pretraining runner on two heterogeneous host blocks: Windows A100 and Linux L40S.”，该机制在 TRAIN-PRETRAINING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：TRAIN-PRETRAINING，[owner](../../../../books/part-04-training-system/28-pretraining.md)；正文锚点：Scaling-law Pilot 也是有预算的实验调度 |
| [Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models](https://arxiv.org/html/2606.11409v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We propose a compute-aware evaluation framework based on computational pressure, measured in cumulative floating-point operations (FLOPs), as a proxy for adversarial effort.”，该机制在 PLATFORM-EVALUATION-SYSTEM 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [Signed Compression Progress on a Sealed Audit is Goodhart-Resistant](https://arxiv.org/html/2606.11417v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Signed Compression Progress on a Sealed Audit is Goodhart-Resistant》关闭或降池；完整摘要显示“The folk claim is that this reward is "credible" because it is paid only for learning.”。该增量直接改变 TRAIN-RLHF 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：TRAIN-RLHF，[owner](../../../../books/part-04-training-system/31-rlhf.md)；正文写入与独立 post-write audit 已完成 |
| [INFRAMIND: Infrastructure-Aware Multi-Agent Orchestration](https://arxiv.org/html/2606.11440v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《INFRAMIND: Infrastructure-Aware Multi-Agent Orchestration》关闭或降池；完整摘要显示“We introduce INFRAMIND, a framework that makes the entire multi-agent stack infrastructure-aware.”。该增量直接改变 INFER-SCHEDULING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文写入与独立 post-write audit 已完成 |
| [Forecasting Future Behavior as a Learning Task](https://arxiv.org/html/2606.11445v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Forecasting Future Behavior as a Learning Task》关闭或降池；完整摘要显示“We propose an alternative that bypasses the explanation step: treat behavior forecasting as a learnable task and train Behavior Forecasters that operates on a single reasoning trajectory to make the same forecasts one would typically seek from an explanation.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文写入与独立 post-write audit 已完成 |
| [ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajectories](https://arxiv.org/html/2606.11520v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We propose ISE (Intent -> Simulate -> Execute), a three-stage synthesis paradigm that addresses these gaps jointly.”，该机制在 TRAIN-DATA 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文锚点：Data lineage 是训练可复现性的前提 |
| [SkillJuror: Measuring How Agent Skill Organization Changes Runtime Behavior](https://arxiv.org/html/2606.11543v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present SkillJuror, a framework for evaluating Skill writing paradigms through semantically controlled variants, matched multi-trial evaluations, and trajectory evidence while holding task knowledge fixed.”，该机制在 AGENT-REFLECTION 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-REFLECTION，[owner](../../../../books/part-07-agent/80-reflection.md)；正文锚点：Reflection 应输出可执行诊断 |
| [Defense Against Prompt Inversion Attacks: An Information-Theoretic Approach for LLM Collaborative Inference](https://arxiv.org/html/2606.11592v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Defense Against Prompt Inversion Attacks: An Information-Theoretic Approach for LLM Collaborative Inference》关闭或降池；完整摘要显示“We propose an information-theoretic defense framework for prompt inversion in collaborative LLM inference.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Sovereign Assurance Boundary: Certificate-Bound Admission for Agentic Infrastructure](https://arxiv.org/html/2606.11632v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“This paper introduces the Sovereign Assurance Boundary (SAB), a certificate-bound runtime admission layer for autonomous execution authority.”，该机制在 PLATFORM-SECURITY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security](https://arxiv.org/html/2606.11671v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present Runtime Skill Audit (RSA), a dynamic analysis method that audits skills by asking what the skill-mediated agent actually does under targeted runtime conditions.”，该机制在 PLATFORM-SECURITY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents](https://arxiv.org/html/2606.11680v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents》关闭或降池；完整摘要显示“In this work, we present HORMA, a Hierarchical Organize-and-Retrieve Memory Agent that organizes experience into a file-system-like hierarchical structure, where summarized entities are linked to the corresponding raw trajectories, enabling efficient access without losing detailed information.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness](https://arxiv.org/html/2606.11686v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present layer-isolated evaluation: a deployed ordering agent is decomposed into a fixed taxonomy of layers (ontology, intent, routing, decomposition, escalation, safety, memory, and cross-cutting envelope/defense), each exercised by its own assertion slice in a deterministic, no-LLM "pure" mode.”，该机制在 PLATFORM-EVALUATION-SYSTEM 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [Goal-Autopilot: A Verifiable Anti-Fabrication Firewall for Unattended Long-Horizon Agents](https://arxiv.org/html/2606.11688v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present Autopilot, an execution model that makes silent fabricated success structurally impossible rather than merely rarer.”，该机制在 AGENT-WORKFLOW 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；正文锚点：State Machine 是基本模型 |
| [Beyond Per-Token Pricing: A Concurrency-Aware Methodology for LLM Infrastructure Cost Estimation](https://arxiv.org/html/2606.11690v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We propose a measurement methodology that parameterizes the relationship as C_eff = f(H, M, Q, lambda, L), validate it with 42 benchmarks across dense, ultra-sparse MoE, and sparse MoE models, and release vllm-cost-meter, an open-source cost meter that attaches to a live vLLM server and reports real \$/M-tokens against the operator's own traffic.”，该机制在 PLATFORM-COST 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-COST，[owner](../../../../books/part-06-ai-infrastructure/70-cost.md)；正文锚点：Utilization 应由实际负载推出，而不是由计算器假定 |
| [Substrate Asymmetry in User-Side Memory: A Diagnostic Framework](https://arxiv.org/html/2606.11712v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Substrate Asymmetry in User-Side Memory: A Diagnostic Framework》关闭或降池；完整摘要显示“We show this aggregate metric hides opposite-direction failures.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [Making Locality-aware GEMM Compatible with Page-Granularity Placement on Chiplet GPUs](https://arxiv.org/html/2606.11718v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We propose Chiplet-Contiguous Layout, a global memory layout that stores chiplet-local data contiguously.”，该机制在 INFER-GPU-MEMORY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-GPU-MEMORY，[owner](../../../../books/part-05-inference-system/54-gpu-memory.md)；正文锚点：Weights 与 KV 的联合 HBM 预算：可提交的运行时精度页 |
| [External Experience Serving in Production LLM Systems: A Deployment-Oriented Study of Quality-Cost Trade-offs](https://arxiv.org/html/2606.11806v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“It is how different serving strategies trade off quality against online cost under realistic constraints.”，该机制在 AGENT-MEMORY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [Grammar-Constrained Decoding Can Jailbreak LLMs into Generating Malicious Code](https://arxiv.org/html/2606.11817v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Grammar-Constrained Decoding Can Jailbreak LLMs into Generating Malicious Code》关闭或降池；完整摘要显示“To address this vulnerability, we propose CodeShield, a safety alignment approach that robustly preserves safe behavior even under attacker-controlled grammar constraints.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文写入与独立 post-write audit 已完成 |
| [Task-Aware Structured Memory for Dynamic Multi-modal In-Context Learning](https://arxiv.org/html/2606.11853v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Task-Aware Structured Memory for Dynamic Multi-modal In-Context Learning》关闭或降池；完整摘要显示“We introduce TASM (Task-Aware Structured Memory), a training-free framework that addresses these limitations through task-aware, structure-preserving, and dynamically accessible memory construction.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [Harnessing Routing Foresight for Micro-step-level MoE load balancing in RL Post-training](https://arxiv.org/html/2606.11867v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Harnessing Routing Foresight for Micro-step-level MoE load balancing in RL Post-training》关闭或降池；完整摘要显示“We introduce ForeMoE, a micro-step-level load balancing system for MoE RL post-training.”。该增量直接改变 TRAIN-DISTRIBUTED-TRAINING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[owner](../../../../books/part-04-training-system/36-distributed-training.md)；正文锚点：Expert Placement 与 Sample Packing 可以共享 Rollout Routing State |
| [WarpGuard: Protected-Site Control-Flow Integrity for CUDA SASS Binaries](https://arxiv.org/html/2606.11871v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present WarpGuard, to our knowledge the first protected-site CFI system for CUDA device binaries operating on executed SASS.”，该机制在 PLATFORM-SECURITY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Gerrymandering the Warp: Non-Control-Data Attacks on CUDA Collective Decision](https://arxiv.org/html/2606.11878v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“Such decisions depend not only on computed values, but also on which lanes are represented, what evidence they contribute, which lane speaks for the group, and which checked state reaches commit.”，该机制在 PLATFORM-SECURITY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Characterizing Software Aging in GPU-Based LLM Serving Systems](https://arxiv.org/html/2606.11916v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“Traditional aging studies focus on CPU-centric software with relatively regular workloads; LLM serving is different, spanning a Python host and a CUDA device, handling requests whose cost varies by orders of magnitude, and relying on rapidly evolving software stacks.”，该机制在 PLATFORM-MONITORING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-MONITORING，[owner](../../../../books/part-06-ai-infrastructure/67-monitoring.md)；正文锚点：条件化机制分支与共存边界 |
| [Online Shift Detection and Conformal Adaptation for Deployed Safety Classifiers](https://arxiv.org/html/2606.11949v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“Adversarial inputs require $3.3\times$ more reasoning tokens than benign inputs to produce valid safety scores ($T_{50,\text{adv}}{=}154$ vs. $T_{50,\text{benign}}{=}46$ for o3), so low-budget deployments silently starve the monitor on exactly the inputs it must catch.”，该机制在 PLATFORM-MONITORING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-MONITORING，[owner](../../../../books/part-06-ai-infrastructure/67-monitoring.md)；正文锚点：条件化机制分支与共存边界 |
| [Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents](https://arxiv.org/html/2606.11998v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We introduce \emph{bootstrapped monitoring}, a protocol that addresses this by inserting a stronger, intermediate untrusted model with transparent chain-of-thought reasoning into the oversight chain.”，该机制在 PLATFORM-SECURITY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [FORT-Searcher: Synthesizing Shortcut-Resistant Search Tasks for Training Deep Search Agents](https://arxiv.org/html/2606.12087v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《FORT-Searcher: Synthesizing Shortcut-Resistant Search Tasks for Training Deep Search Agents》关闭或降池；完整摘要显示“We formalize this gap with a shortcut-aware difficulty framework and identify four actionable shortcut risks: evidence co-coverage, single-clue selectivity, exposed constants, and prior-knowledge binding.”。该增量直接改变 TRAIN-DATA 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文锚点：Data lineage 是训练可复现性的前提 |
| [The Brain That Goes Quiet: Serving a Large Model's Knowledge at 131 Tokens per Second on an 8 GB Laptop by Removing the Large Model from the Runtime Path](https://arxiv.org/html/2606.12154v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 1 + 2 = 5；原筛选把《The Brain That Goes Quiet: Serving a Large Model's Knowledge at 131 Tokens per Second on an 8 GB Laptop by Removing the Large Model from the Runtime Path》关闭或降池；完整摘要显示“That result solved a placement problem and immediately exposed a different one: even correctly placed, the large model needed roughly four seconds to answer, because it was still being invoked at every query.”。该增量直接改变 INFER-PREFILL 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 仅报告：INFER-PREFILL；exact-v1 尚不足以授权长期 Books 正文变化 |
| [A Controlled Study of Decoding-Time Truthfulness Methods on Instruction-Tuned LLMs](https://arxiv.org/html/2606.12160v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《A Controlled Study of Decoding-Time Truthfulness Methods on Instruction-Tuned LLMs》关闭或降池；完整摘要显示“However, modern instruction-tuned LLMs already achieve substantially higher baselines (61-76%), raising the question of whether these methods remain effective in practice.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [Mind your key: An Empirical Study of LLM API Credential Leakage in iOS Apps](https://arxiv.org/html/2606.12212v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Mind your key: An Empirical Study of LLM API Credential Leakage in iOS Apps》关闭或降池；完整摘要显示“We present the first in-depth empirical study of API key leakage in LLM-integrated apps.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Rule Taxonomy and Evolution in AI IDEs: A Mining and Survey Study](https://arxiv.org/html/2606.12231v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Rule Taxonomy and Evolution in AI IDEs: A Mining and Survey Study》关闭或降池；完整摘要显示“Despite their role in aligning AI behavior with developer intent, the taxonomy, evolution, and practical impact of these rules remain largely unexplored.”。该增量直接改变 AGENT-PROMPT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-PROMPT，[owner](../../../../books/part-07-agent/74-prompt.md)；正文锚点：Prompt 生命周期 |
| [VIA-SD: Verification via Intra-Model Routing for Speculative Decoding](https://arxiv.org/html/2606.12243v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We propose Verification via Intra-Model Routing for Speculative Decoding (VIA-SD), a multi-tier framework using a routed slim-verifier.”，该机制在 INFER-SPECULATIVE-DECODING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[owner](../../../../books/part-05-inference-system/48-speculative-decoding.md)；正文锚点：Correctness owner 没有改变 |
| [A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents](https://arxiv.org/html/2606.12320v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；五平面、stop-anywhere mediation、capability attenuation 与 structured audit 属于范围内架构证据，但对 owner 章节的逐段比较表明这些原则已由 effect-time authorization、delegation-chain attenuation、跨通道 influence graph 与 evidence chain 承载。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；不把参考架构 taxonomy 重写为第二套正文 |
| [PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents](https://arxiv.org/html/2606.12329v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present projectmem, an open-source, local-first memory and judgment layer for AI coding agents. projectmem records development as an append-only, plain-text event log of typed events - issues, attempts, fixes, decisions, and notes - and deterministically projects that log into compact, AI-readable summaries served through the Model Context Protocol (MCP).”，该机制在 AGENT-MEMORY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [OCELOT: Inference-Leakage Budgets for Privacy-Preserving LLM Agents](https://arxiv.org/html/2606.12341v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《OCELOT: Inference-Leakage Budgets for Privacy-Preserving LLM Agents》关闭或降池；完整摘要显示“We recast agent privacy as \emph{posterior-risk control} and present OCELOT, a runtime mediator that budgets how much an adversary's belief about a secret may improve across a trajectory, rather than filtering outputs.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文写入与独立 post-write audit 已完成 |
| [ALIGNBEAM : Inference-Time Alignment Transfer via Cross-Vocabulary Logit Mixing](https://arxiv.org/html/2606.12342v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 1 + 2 = 5；原筛选把《ALIGNBEAM : Inference-Time Alignment Transfer via Cross-Vocabulary Logit Mixing》关闭或降池；完整摘要显示“We present ALIGNBEAM, a training-free method that lifts this restriction by translating anchor logits into the target model's vocabulary token-by-token at each decoding step; a small LLM judge then selects the safest among K candidate continuations.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 仅报告：PLATFORM-SECURITY；exact-v1 尚不足以授权长期 Books 正文变化 |
| [Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks](https://arxiv.org/html/2606.12344v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks》关闭或降池；完整摘要显示“We introduce Claw-SWE-Bench, a multilingual SWE-bench-style benchmark and adapter protocol that makes heterogeneous agent harnesses, or claws, comparable under fair settings including a fixed prompt, runtime budget, workspace contract, patch extraction procedure, and evaluator.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [On Subquadratic Architectures: From Applications to Principles](https://arxiv.org/html/2606.12364v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《On Subquadratic Architectures: From Applications to Principles》关闭或降池；完整摘要显示“To explain xLSTM's advantage, we present a unified formulation and analyze the underlying architectural mechanisms, focusing on state tracking and memory dynamics.”。该增量直接改变 MODEL-LONG-CONTEXT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：MODEL-LONG-CONTEXT，[owner](../../../../books/part-02-model/22-long-context.md)；正文锚点：方案究竟移动了哪个瓶颈 |
| [Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling](https://arxiv.org/html/2606.12370v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“To address this bottleneck, we present Bebop, a systematic study of MTP in LLM post-training, and offer practical recipes to integrate MTP into large-scale RL pipelines.”，该机制在 INFER-SPECULATIVE-DECODING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[owner](../../../../books/part-05-inference-system/48-speculative-decoding.md)；正文锚点：Correctness owner 没有改变 |
| [Verifiable Environments Are LEGO Bricks: Recursive Composition for Reasoning Generalization](https://arxiv.org/html/2606.12373v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Verifiable Environments Are LEGO Bricks: Recursive Composition for Reasoning Generalization》关闭或降池；完整摘要显示“While prior research demonstrates that scaling environment quantity improves RL performance, existing manual or individual construction methods suffer from linear scaling limits, thereby hindering scalable reasoning generalization.”。该增量直接改变 TRAIN-DATA 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文写入与独立 post-write audit 已完成 |
| [APPO: Agentic Procedural Policy Optimization](https://arxiv.org/html/2606.12384v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《APPO: Agentic Procedural Policy Optimization》关闭或降池；完整摘要显示“Motivated by these observations, we propose \textbf{Agentic Procedural Policy Optimization (APPO)}, which shifts branching and credit assignment from coarse interaction units to fine-grained decision points in the sequence.”。该增量直接改变 TRAIN-GRPO 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；正文锚点：从一个终局标量到 Typed Credit：Reward 必须匹配决策边界 |
| [Doc-to-Atom: Learning to Compile and Compose Memory Atoms](https://arxiv.org/html/2606.12400v1) | 2026-06-11T08:00:00+08:00 ～ 2026-06-11T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Doc-to-Atom: Learning to Compile and Compose Memory Atoms》关闭或降池；完整摘要显示“To address these challenges, we propose Doc-to-Atom (Doc2Atom), a compositional parametric memory framework that decomposes each document into semantically typed knowledge atoms.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文写入与独立 post-write audit 已完成 |

## 4. 证据与知识整合

本轮新增证据分批如下；未列出完成证据的新增候选仍是普通待办，不借旧52的完成标签过关。

### [MiMo Code Long-Horizon](https://mimo.xiaomi.com/blog/mimo-code-long-horizon)

已实际整合 AGENT-CONTEXT 的“Compaction首段后”单段；必要、actual owner、唯一稿与实际POST均由非writer通过。只提前抽取与最终装配的预算时机；不授single-writer原子最新、归因隔离或CLI计划已实现。 完整版本/位置/对照与边界见[本轮必要记录 A1](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)，独核见[本轮review](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Piper: A Programmable Distributed Training System](https://arxiv.org/html/2606.11169v1)

已实际整合 TRAIN-DISTRIBUTED-TRAINING 的“手写Plan→planner末段后”单段；必要、actual owner、唯一稿与实际POST均由非writer通过。受限traceable图/布局与通信顺序、reshard及kernel/弱扩展反侧保留，不授任意策略或全局最优。 完整版本/位置/对照与边界见[本轮必要记录 A2](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)，独核见[本轮review](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [DiffusionGemma](https://developers.googleblog.com/en/diffusiongemma-the-developer-guide/)

已实际整合 MULTIMODAL-GENERATIVE-PARADIGMS 的“ParallelProgress首段后”单段；必要、actual owner、唯一稿与实际POST均由非writer通过。高QPS已有batch可减弱块并行收益；不借July current card历史背书或4x通用数字。 完整版本/位置/对照与边界见[本轮必要记录 A3](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)，独核见[本轮review](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [The Role of Feedback Alignment in Self-Distillation](https://arxiv.org/html/2606.11173v1)

已实际整合 TRAIN-SFT 的“ContextDistillation概念末”单段；必要、actual owner、唯一稿与实际POST均由非writer通过。保错误全文复述/无逐字正确锚的双反例、30题反复选checkpoint与全critic费用，induction仅假说。 完整版本/位置/对照与边界见[本轮必要记录 A4](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)，独核见[本轮review](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Multi-Faceted Interactivity Alignment in Full-Duplex Speech Models](https://arxiv.org/html/2606.11167v1)

具体已有覆盖：TRAIN-RLHF 的“Evaluation独立于RewardModel的ensemble盲区段”；不是因同主题而No Change。Fisher后Safety-task与碎片backchannel反退只为局部负面证据；base示例本来不拒答，不写safe→unsafe因果。现正文ensemble盲区/人口独立评价已承载。 完整版本/位置/对照与边界见[本轮必要记录 A5](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)，独核见[本轮review](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Optimal Post-Training Quantization Scales and Where to Find Them](https://arxiv.org/html/2606.10890v1)

中心争议，Books暂缓；不删除6分候选、不将有问题的中心定理写入书稿。修正负w=-1/ties-up例满足C9前提，C10由闭包inf推进attainment不成立；区间二次结构与实测不随之全否。 完整版本/位置/对照与边界见[本轮必要记录 A6](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)，独核见[本轮review](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models](https://arxiv.org/html/2606.11164v1)

具体已有覆盖：INFER-KV-CACHE 的“CoT adaptive layer/head与prefill/decode统计段”；不是因同主题而No Change。现正文CoT adaptive layer/head与prefill/decode区别已承载；clip后归一floor不自证exact硬预算，maxbatch吞吐不签同batch加速。 完整版本/位置/对照与边界见[本轮必要记录 A7](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)，独核见[本轮review](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Recoverable but Not Stationary:Local Linear Structures in Weights and Activations](https://arxiv.org/html/2606.10929v1)

已实际整合 TRAIN-LORA 的“TLoRA段后”单段；必要、actual owner、唯一稿与实际POST均由非writer通过。synthetic旧plane投影弱于full，GPT2 local约束恢复却可接近full；位移投影率不是训练上限，Qwen7B sampling-control反侧保留。 完整版本/位置/对照与边界见[本轮必要记录 A8](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)，独核见[本轮review](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [When to Align, When to Predict: A Phase Diagram for Multimodal Learning](https://arxiv.org/html/2606.11190v1)

已实际整合 MULTIMODAL-REPRESENTATION 的“对齐centroid/pair首段后”单段；必要、actual owner、唯一稿与实际POST均由非writer通过。固定k/spiked与CA双边/CP单边whitening；保overcapacity、r0下界非失败、COCO目标/probe混杂，不采用科学应用。 完整版本/位置/对照与边界见[本轮必要记录 A9](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)，独核见[本轮review](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [The Arbiter Agent: Continually Monitoring Multi-Agent Conversations to Detect Emergent Misalignment](https://arxiv.org/html/2606.10747v1)

已实际整合 AGENT-MULTI-AGENT 的“Fleetoversight末/角色正确性前”单段；必要、actual owner、唯一稿与实际POST均由非writer通过。同neutral Qwen人口的黑箱问询+log差额，不借SP/CoT权限；五对话/强auditor/wordbudget与误报限制保留，Jun6 talk非正文日。 完整版本/位置/对照与边界见[本轮必要记录 A10](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)，独核见[本轮review](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [K-Forcing: Joint Next-K-Token Decoding via Push-Forward Language Modeling](https://arxiv.org/html/2606.10820v1)

已实际整合 MODEL-DECODER-ONLY 的“conceptclock末/历史生产前”单段；必要、actual owner、唯一稿与实际POST均由非writer通过。联合噪声映射不是exact AR law；保2k真实token/noise处理、临时KV、FP16→FP32训练与densemask全费，NFE非全serving费用。 完整版本/位置/对照与边界见[本轮必要记录 A11](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)，独核见[本轮review](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [A Theory on Flow Matching with Neural Networks](https://arxiv.org/html/2606.10089v1)

中心争议，Books暂缓；不删除6分候选、不将有问题的中心定理写入书稿。C1/F1用r=M/(2L)越出diamK，恒100合法例给100≤20矛盾；Ass4不推出Eq1全时间uniform Lipschitz，不采W1桥接，不否认未核独立优化/泛化或全部经验。 完整版本/位置/对照与边界见[本轮必要记录 A12](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)，独核见[本轮review](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Mean Flow Distillation: Robust and Stable Distillation for Flow Matching Models](https://arxiv.org/html/2606.11155v1)

已实际整合 MULTIMODAL-GENERATIVE-PARADIGMS 的“K-DMD段后”单段；必要、actual owner、唯一稿与实际POST均由非writer通过。理想aux/zero/fullsupport充分条件不同于实际停solver Jacobian的guidance；IID方差假设和全ODE/辅助准备费保留，不采普遍1/K或Eq46。 完整版本/位置/对照与边界见[本轮必要记录 A13](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)，独核见[本轮review](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Unifying Local Communications and Local Updates for LLM Pretraining](https://arxiv.org/html/2606.11081v1)

已实际整合 TRAIN-DISTRIBUTED-TRAINING 的“09970 gossip段后/后验采样前”单段；必要、actual owner、唯一稿与实际POST均由非writer通过。pre/postlocal correction与延迟Local-DAdam资格；保logicalworkers、single-run、稀疏质量差、70B模拟与SGD非Adam保证。 完整版本/位置/对照与边界见[本轮必要记录 A14](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)，独核见[本轮review](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Provenance Tracking in AI Compilers through the Lens of Coalgebra](https://arxiv.org/html/2606.10937v1)

6分中心争议/Books暂缓。F已带operator labels却混用value等价；R漏action后继配对，无weak/multistep规则。实现仍每pass维护span map，不授无instrumentation自动正确性；重开需完整关系及实现一致证明。 完整依据见[必要记录A15](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Express Language Modeling](https://arxiv.org/html/2606.10944v1)

实际整合MODEL-SELF-ATTENTION“改变算子节首概念后”，非writer必要/PRE/实际POST通过。仅weighted prefix summary/query-before-update，保norm/value/prob、后续KV、固定s/每题选点与核非全模型限制。 完整依据见[必要记录A16](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Attention Amnesia in Hybrid LLMs: When CoT Fine-Tuning Breaks Long-Range Recall, and How to Fix It](https://arxiv.org/html/2606.11052v1)

实际整合TRAIN-SFT“11426 activation段后”，非writer必要/PRE/实际POST通过。仅同源preQK/post其余混合asset干预，保Jet反退、Hype未回pre、T3口径与数学退步，不采Markov普遍定理。 完整依据见[必要记录A17](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Flow-DPPO: Divergence Proximal Policy Optimization for Flow Matching Models](https://arxiv.org/html/2606.11025v1)

实际整合TRAIN-PPO“KLpenalty末Estimator后”，reader§46唯一实际POST通过。只同state等正covariance Gaussian KL；ratio-sign不是共享参数实际KL方向，保predictive未验证、mask非硬投影与全部费用/反侧。完整依据见[必要记录A18](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Beyond Uniform Token-Level Trust Region in LLM Reinforcement Learning](https://arxiv.org/html/2606.10968v1)

实际整合TRAIN-PPO“29999完整marker后/Nstep前”，reader§47唯一实际POST通过。累计distribution-divergence非累计likelihoodratio，保TopK-TV下界、slack/纠偏例外、完整response额度及验证择优，不授全局hardcap。完整依据见[必要记录A19](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Provenance-Grounded Gating and Adaptive Recovery in Synthetic Post-Training Data Curation](https://arxiv.org/html/2606.11127v1)

实际整合TRAIN-DATA“Synthetic首概念后”，reader§53唯一实际POST通过。原chunk的faithfulness与无source quality分责，改写须重验；不由yield、同源judge或scale签真值。 完整依据见[必要记录A20](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Exploring the Design Space of Reward Backpropagation for Flow Matching](https://arxiv.org/html/2606.11075v1)

实际整合TRAIN-RLHF“21654完整binding后”，reader§54唯一实际POST通过。forward同endpoint不等fullgradient，保O(N)cache、oneJ非范数保证及全部费用。 完整依据见[必要记录A21](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Attention-Discounted Adaptive Sampler for Masked Diffusion Language Models](https://arxiv.org/html/2606.10829v1)

实际整合MULTIMODAL-GENERATIVE-PARADIGMS“AXON04236完整marker后”，reader§55唯一实际POST通过。固定k的directional greedy选择；规则不变非实际count固定，attention非依赖真值。 完整依据见[必要记录A22](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design](https://arxiv.org/html/2606.10493v1)

实际整合TRAIN-DISTRIBUTED-TRAINING“ThunderEP40093完整marker后”，reader§59唯一实际POST通过。只小EP全token复制/局部weightedpartial交换，保驻留/重复gate与单层非SLO边界。 完整依据见[必要记录A23](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [miniReranker: Efficient Multimodal Reranking through Visual Cache Reuse and Interaction Sparsity](https://arxiv.org/html/2606.10759v1)

实际整合AGENT-RAG“FusionRAG12904完整marker后”，reader§60唯一实际POST通过。跨query doc与请求内querycache分责，保显式交互带适配及质量/全cache费用。 完整依据见[必要记录A24](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [ASTRA-sim 3.0: Next-Level Distributed Machine Learning Simulations via High-Fidelity GPU and Infrastructure Modeling](https://arxiv.org/html/2606.10440v1)

实际整合TRAIN-DISTRIBUTED-TRAINING“alphaBeta概念末/bytes效率前”，reader§63唯一实际POST通过。控制/数据cacheline争用可反转get/put，generic模拟/共同graph不等实机或backend校准。 完整依据见[必要记录A25](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [How Does Reasoning Flow? Tracing Attention-Induced Information Flow for Targeted RL in LLMs](https://arxiv.org/html/2606.10646v1)

实际整合TRAIN-GRPO“SequenceReward粗糙性说明后”，reader§64唯一实际POST通过。h>0局部图流守恒只提重权rank，不授因果/步骤真值，保连续权重反退与attention全费。 完整依据见[必要记录A26](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [What Fits (Into Few Tokens) Doesn't Overfit: Compression and Generalization in ML Research Agents](https://arxiv.org/html/2606.11045v1)

实际整合PLATFORM-EVALUATION-SYSTEM“28798完整marker后”，reader§67唯一实际POST通过。短消息只认证reproducer，one-bit保证按预定完整transcript预算；保iid/旁路及Bernoulli范围。 完整依据见[必要记录A27](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Dynamic Linear Attention](https://arxiv.org/html/2606.10650v1)

实际整合MODEL-LONG-CONTEXT“MemoryCaching首段后”，reader§68唯一实际POST通过。动态边界/相邻有损merge共同保存countscore顺序；不授bound为真实优越或无限记忆。 完整依据见[必要记录A28](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Pushing the Limits of LLM Tool Calling via Experiential Knowledge Integration and Activation](https://arxiv.org/html/2606.10875v1)

实际整合AGENT-TOOL-CALLING“ToolDiscovery首概念位”，reader§72唯一实际POST通过。只instance经验与当步候选预算的局部对照，仅选定call执行；保温度/费用/负面切片。 完整依据见[必要记录A29](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Frontier Coding Agents Use Metaprogramming to Adapt to Unfamiliar Programming Languages](https://arxiv.org/html/2606.10933v1)

实际整合AGENT-TOOL-CALLING“Agentfriendly末/ResourceLowering前”，reader§75唯一实际POST通过。hostgenerator/目标source分责，保禁host权限共变、观察token非因果和hidden反馈边界。 完整依据见[必要记录A31](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Janus: A Benchmark for Goal-Conditioned Information Distortion in LLMs](https://arxiv.org/html/2606.10852v1)

实际整合PLATFORM-EVALUATION-SYSTEM“18280输出验收后/26242前”，reader§77唯一实际POST通过。固定fact覆盖不替平衡呈现；保角色/目标约束共变、代理分母/人审与无真实说服证据。 完整依据见[必要记录A30](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents](https://arxiv.org/html/2606.10742v1)

实际整合AGENT-MEMORY“poisonchain checkpoint后/Repair前”，reader§78唯一实际POST通过。直接召回/graph扩展/实际消费闭包分账，不授新authority；保conditional trigger及localhost边界。 完整依据见[必要记录A32](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)与[独核](../_sources/daily-20260611/SUP_REVIEW_20261026.md)。

### [Effective Reinforcement Learning for Agentic Search by Recycling Zero-Variance Queries During Training](https://arxiv.org/html/2606.10709v1)

精确v1必要与直接反侧见[证据A33](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)。零方差还不应被永久写成题目标签：同一题在有限group里全对/全错，是给定policy和采样预算的一次观察，后来能力变化、漂移或仅重采样都可能重新产生差分。[受限query-recycling分支](https://arxiv.org/html/2606.10709v1#S3.SS4)因而将此前没有贡献更新的题保留在activepool，只有真正选入update的signal-bearing题才消费掉；有界过采样负责本轮多看多少，pool资格负责后续还可看谁，不能混作同一预算或在线难度真值。需保存pool/consumed身份、policy、group和实际消费记录，失败与过量未用rollout仍付费；匹配trajectory数不等tokens、工具调用或optimizer exposure相同。较多rescues不独立证明能力增长，固定pool也会逐渐失去信号，局部收益并非各任务单调。判分、人口或净预算失配时，保留原mixed-group补采、随机coverage与普通epoch计划，不由一次全零永久删题，也不由循环重试承诺无限有效学习。

归属（Owner）：`TRAIN-GRPO`；实际写入[对应章节](../../../../books/part-04-training-system/33-grpo.md)的06375完整admission末/Pareto探测前，唯一独立review§82已核完整新增、两侧和本人注，指定位生效释放；未核代码或复现。

### [Continual LLM Upcycling: A Predictor-Gated Bank-Wise Sparsity Training Recipe for Dense-to-Sparse LLMs](https://arxiv.org/html/2606.10722v1)

精确v1必要与直接反侧见[证据A34](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)。稀疏门控的验收还需按层、phase与任务拆开：一个受限bank-wise分支为每层增加低秩predictor，在固定channel bank内只保部分通道，hardforward配softsurrogate继续训练。[局部fallback对照](https://arxiv.org/html/2606.10722v1#S6.SS2)中，短任务和整体长窗均值接近dense，仍可在特定长CWE读出出现cliff；只将一层的prompt末问答后缀换成校准denseactivation，可救回部分CWE，却不修NIAH且伤MMLU，不能把它叫恢复全部记忆或通用长窗补丁。应共同记录predictor、bank/mask、layer、prefill/decode与校准人口，分别验远程检索、局部读出和短任务；GPU若仍先算denseup/gate，activechannel少也不省这两项投影。预测/选择、稀疏布局、额外参数/训练、fallback与双侧回归都计费；读出、质量或真实省算不合时，保留原dense/较轻稀疏和不启局部修补，不由较低loss、平均稀疏率或一个召回恢复点批准能力保持。

归属（Owner）：`MODEL-FFN`；实际写入[对应章节](../../../../books/part-02-model/16-feed-forward-mlp.md)的00454 marker后/01973前，唯一独立review§87已核完整新增、两侧和本人注，指定位生效释放；未核代码或复现。

### [SSR-Merge: Subspace Signal Routing for Training-Free LoRA Merging in Diffusion Models](https://arxiv.org/html/2606.10617v1)

精确v1必要与直接反侧见[证据A35](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)。同基座adapter直接相加若仍相互干扰，可把各down-projection纵向stack、up-projection横向concat，在这份Kr维空间内按各任务校准特征累积Gram与taskblockguide，再求固定线性router并吸收进up-projection。[受限二阶路由分支](https://arxiv.org/html/2606.10617v1#S3)在Gram可逆时可匹配该校准人口的线性output最小二乘，却不由层内MSE最小推出全生成任务无冲突。相关token很多不保证Gram良态、独立有效样本或单prompt/单timestep全域充分，原文逐block伪逆选择等式亦不能一般沿用；需保存任务/层、校准prompt与时间、统计精度、条件数和真实合并资产。流式统计省rawfeature驻留，不免每层平方统计、求解、原LoRA训练和多任务回归，Kr资产未fold时也不同于单r部署。校准支持、数值或质量不合时，保留分离adapter、原相加/可信选择与更多校准，不由training-free或router可fold批准无损、零全费或普遍最优。

归属（Owner）：`TRAIN-LORA`；实际写入[对应章节](../../../../books/part-04-training-system/30-lora.md)的多个Adapter能否直接相加后/CompositionAdmission前，唯一独立review§88已核完整新增、两侧和本人注，指定位生效释放；未核代码或复现。

### [CLP: Collocation-Length Prediction for Zero-Loss Adaptive Multi-Token Inference](https://arxiv.org/html/2606.10935v1)

精确v1必要与直接反侧见[证据A36](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)。即使每轮第一个token仍来自原LM head，也不能据此承诺额外span无损：同一hidden上的MTP可提出后续tokens，再由长度classifier及confidence门决定接纳多少，但未逐个target验证的bonus一旦提交，就改变下一轮prefix。[受限CLP分支](https://arxiv.org/html/2606.10935v1)因此应标为近似spanproposal，而非exact speculative decoding；最大类别概率不是整段正确率，只有退到零bonus的原AR或真正验证吻合的路径才保相应greedy轨迹。Classifier训练/校准人口、head与backbone、阈值和KV更新要共同绑定，少量prompt的TPS/低重复率不替独立任务质量；保守阈值也可能比原AR更慢。全部hidden/label制备、MTP与gate训练、额外参数/logits和质量回归均计费；误差、校准或净收益不合时，保零bonus原AR或已验draft-and-verify，不由native首token、轻classifier或zero-loss名称签发完整生成分布与生产加速。

归属（Owner）：`INFER-SPECULATIVE-DECODING`；实际写入[对应章节](../../../../books/part-05-inference-system/48-speculative-decoding.md)的效用仲裁24793 marker后/WISV前，唯一独立review§83已核完整新增、两侧和本人注，指定位生效释放；未核代码或复现。

### [SpenseGPT: Practical One-shot Pruning Enabling Sparse and Dense GEMMs for LLM Inference](https://arxiv.org/html/2606.10445v1)

精确v1必要与直接反侧见[证据A37](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)。混合稀疏也可沿MLP共享intermediate坐标切成连续dense区与2:4区，让up/gate分别计算输出片段，down对输入片段的结果累加，从而复用现成dense/sparse GEMM而不扩大activation。一个[受限Spense分支](https://arxiv.org/html/2606.10445v1#S3)先选择要保护的索引，再共同置换up/gate行与down列；剪枝前把dense索引放在SparseGPT尚可补偿的后部，和仅在部署时重排是不同决定，相同索引放前仍可严重损质量。未剪枝的置换恒等不替有损分组/重构签字，独立敏感度评分也非组合最优，需保存实际dense数量、2:4组、置换及校准/重构顺序。双GEMM/accumulate、索引与packing、校准剪枝和任务回归均计费；小M可比dense慢，B200/FP8大batch的decode收益不授低并发或全SLO。库/shape、校准支持或质量—费用失配时，保原dense、已验纯2:4或较高dense比例，不由更自由格式或单核稀疏峰值批准无损与通用加速。

归属（Owner）：`INFER-TENSORRT-LLM`；实际写入[对应章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)的23410 marker后/28947前，唯一独立review§91已核完整新增、两侧和本人注，指定位生效释放；未核代码或复现。

### [Parallel Causal Associative Fields: Gated Sparse Memory for Long-Context Language Modeling](https://arxiv.org/html/2606.10435v1)

精确v1必要与直接反侧见[证据A38](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)。保留的也可以是可寻址的“旧context→已观察successor token”记录，而非summary或全部KV：先用causal token hash提出有限候选，再用连续key/query与recency评分形成successor分布，同local parametric LM由受训gate混合，空bucket回原local路径。[PCAF的受限分支](https://arxiv.org/html/2606.10435v1#S3)把address与value resolution分开，却不从hash命中推出语义相似或事实正确；每个预测位置只能读successor已在其prefix出现的记录，整序列teacher forcing也须保这份可见性。每bucket最多K会丢记录，重复/碰撞可损召回，候选数有界不等全部feature、建表或full-AR运行成本恒定。更多K/semantic容量能改善局部PPL却付吞吐，best validation与next-token诊断也不替完整生成质量。路由/保留规则、key/gate、记录位置与snapshot共同保存，建表、驻留、评分和训练回归均计费；碰撞、长程关系或净质量—费用不合时，保留localLM、较大候选、显式历史/原hybrid与外部取证，不由稀疏读取批准无限记忆、无泄漏kernel或通用加速。

归属（Owner）：`MODEL-LONG-CONTEXT`；实际写入[对应章节](../../../../books/part-02-model/22-long-context.md)的远期memorybank末/外部工作集前，唯一独立review§92已核完整新增、两侧和本人注，指定位生效释放；未核代码或复现。

### [Fast and Highly Expressive Policy Learning for Offline Reinforcement Learning via Bootstrapped Flow Q-Learning](https://arxiv.org/html/2606.10613v1)

精确v1必要与直接反侧见[证据A39](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)。组合一致还可以由当前模型自己提供长区间target，而不另训distillation teacher：同一conditioning state下，将两段短flow map的复合作stop-gradient目标，并以已知conditional velocity在小区间锚定，避免只学组合律时连错误的identity map也能自洽。[BFQ的受限分支](https://arxiv.org/html/2606.10613v1#S4)用velocity-like参数化保持零间隔identity与训练信号，但有限间隔、近似优化和critic误差仍不授全局自举收敛、精确分布或一步动作安全；两个loss的随机混合无偏也不是policy gradient无偏。“无独立teacher”仍支付两段policy forward、target/critic、离线数据与调参，批量生成频率不是单请求闭环时延。保存时间域、边界target、state/noise支持、当前与target身份及实际费用，原算法未闭的时间/归一guard不拼执行recipe；退化、Q外推或净质量—费用不合时，保原多步flow、独立teacher/可信监督与control gate，不由自一致性批准无损one-step替换。

归属（Owner）：`MULTIMODAL-GENERATIVE-PARADIGMS`；实际写入[对应章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)的少步蒸馏组合一致完整概念段后/提升observables固定矩阵段前，唯一独立review§97已核完整新增、两侧和本人注，指定位生效释放；未核代码或复现。

### [RATrain: A Resource-Aware Training Runtime for Large Language Models on Bandwidth-Constrained Heterogeneous Supercomputing Platforms](https://arxiv.org/html/2606.10415v1)

精确v1必要与直接反侧见[证据A40](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)。显式DAG之外，stage-local runtime还可在不改1F1B与gradient accumulation的前提下搬移状态生产时机：只保activation checkpoint，在可用forward/idle窗口提前恢复backward所需张量，并在该layer最后一次累积完成后依次同步梯度、更新shard、预取新weight，赶在下一次合法读取前ready。[RATrain的受限实现](https://arxiv.org/html/2606.10415v1#S3)让队列/事件和短生存恢复buffer承担这份合同，不是每microbatch更新，也不靠重排取消数据依赖；窗口、共享memory或传输资源不足时仍须现场恢复/等待。Planner须同时计inflight checkpoints、恢复buffer/workspace、暴露通信与profile误差，预分配复用也不能跨未完成读写复用。所测MT3000内存层级与共用operator backend下的策略对照，不授GPU通用收益、bitwise更新等价或完整收敛；各关闭组件倍率不相乘。Profiling、恢复、weight搬运与完整loss/运行回归均计费，deadline、内存或净吞吐失配时保原backward重算、较保守静态plan与已验runtime，不以更高MAC利用率批准全训练加速。

归属（Owner）：`TRAIN-DISTRIBUTED-TRAINING`；实际写入[对应章节](../../../../books/part-04-training-system/36-distributed-training.md)的Piper11169完整段marker后/从Phase串行主标题前，唯一独立review§98已核完整新增、两侧和本人注，指定位生效释放；未核代码或复现。

### [Reasoning or Memorization? Direction-Aware Diversity Exploration in LLM Reinforcement Learning](https://arxiv.org/html/2606.10346v1)

精确v1必要与直接反侧见[证据A41](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)。多样性也可先声明要鼓励哪一种表示差异：从初始policy的两类对比prompt取得固定hidden方向，用它给token的最终层敏感度proxy加权，并把rollouts分组，只相对指定参考组计算新颖度，再对两组作相反符号的reward shaping。[DiRL的受限分支](https://arxiv.org/html/2606.10346v1#S3)改变的是bonus权重与参考人口，不认证被分为“reasoning”的文本真的推理、另一组只是记忆，或hidden proxy的角度就是全参数更新方向；不同token的Jacobian不能由一个加总向量自动消去。Reference子集的权重与零范数/同分处理须声明，不把余弦平方分数当精确独立信息；错而被标为正组的回答也可能少受惩罚。应绑定对比数据/标签、policy与层位、固定方向、group/权重及verifier，独立检查解法与迁移，不能用同一方向读出的比例上涨自证机制。校准、读出、向量矩阵与全部rollout/训练回归计费；方向漂移、proxy或净质量失配时，保原outcome GRPO、较弱bonus与可信独立评价，不由更多新颖文本批准新推理能力或免费探索。

归属（Owner）：`TRAIN-GRPO`；实际写入[对应章节](../../../../books/part-04-training-system/33-grpo.md)的DQO04784完整marker后/同题正确rollout稀有度分支前，唯一独立review§100已核完整新增、两侧和本人注，指定位生效释放；未核代码或复现。

### [UniSVQ: 2-bit Unified Scalar-Vector Quantization](https://arxiv.org/html/2606.10520v1)

精确v1必要与直接反侧见[证据A42](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)。避免任意向量码本lookup，还可将每个低位word限制为共享仿射整数格：重构是小矩阵A作用于integer codes再加B，于是每block乘法可先对activation做A变换，再消费integer权重，另加共享偏移。[UniSVQ的受限接口](https://arxiv.org/html/2606.10520v1#S3)用较小仿射参数换取这种可交换消费，但限制了表示自由度；变换后的activation仍为浮点，不能把weight-only兼容说成纯INT GEMM、activation/KV同位宽或原生tensor core已验。实际custom fused路径与optimized GEMM集成尚有边界，有限格初始化也不由渐近Gaussian论证获得无损保证。RHT/LDL校准、整数codes、A/B、packing与activation变换/偏移共同定义asset，全部制备与执行回归计费；有限batch1计时慢于另一scalar路径、部分质量弱于VQ也须保留。格式、质量或净费用失配时，保任意VQ配匹配consumer、成熟scalar量化或高精度，不由更小码本metadata批准全模型同质量加速。

归属（Owner）：`INFER-TENSORRT-LLM`；实际写入[对应章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)的10496 productLUT完整实现限制段后/重复weight在线乘积复用段前，唯一独立review§99已核完整新增、两侧和本人注，指定位生效释放；未核代码或复现。

### 原52家族的有效证据（历史范围，不代本轮新项）

### [PoQ-Judge: A Multi-Architecture Evaluation Framework for Cost-Aware Proof-of-Quality in Decentralized LLM Inference](https://arxiv.org/html/2606.11196v1)

**问题与机制。** 原筛选把《PoQ-Judge: A Multi-Architecture Evaluation Framework for Cost-Aware Proof-of-Quality in Decentralized LLM Inference》关闭或降池；完整摘要显示“We present PoQ-Judge, a framework that trains dedicated judge models to score query-output pairs without ground-truth references.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 PoQ-Judge: Reference-Free Evaluation Framework; 3.1 Judge Model Architectures`；可采用的最小机制命题是：We present PoQ-Judge, a framework that trains dedicated judge models to score query-output pairs without ground-truth references.

**Evaluation proof。** `2.2 The Reference-Free Evaluation Gap; 3 PoQ-Judge: Reference-Free Evaluation Framework; 3.5 Cascade Evaluation Protocol`；exact-v1 披露：Decentralized LLM inference networks need lightweight, reference-free quality evaluation for Proof of Quality (PoQ).

**Limitations / non-proof。** `6 Discussion`；We also show that online calibration identifies semantic quality as the dominant dimension and that cascade evaluation reduces cost by 72.7 percent with only modest quality loss. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [The Structural Attention Tax: How Retrieval Format Hijacks In-Context Learning Independent of Content](https://arxiv.org/html/2606.11198v1)

**问题与机制。** 原筛选把《The Structural Attention Tax: How Retrieval Format Hijacks In-Context Learning Independent of Content》关闭或降池；完整摘要显示“We develop a formal framework decomposing attention scores into semantic and structural components (Eq.”。该增量直接改变 AGENT-RAG 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 The Structural Attention Tax Framework; 4 Methodology`；可采用的最小机制命题是：We develop a formal framework decomposing attention scores into semantic and structural components (Eq.

**Evaluation proof。** `4.1 Experimental Design; 5 Results; Appendix A Experimental Setup and Validation`；exact-v1 披露：We derive five structure-aware mitigation strategies from the framework, ranging from zero-cost prompt modifications to training-time regularisation; format flattening (S3) is validated by both accuracy and attention-level evidence from a verbalized-triple control, while structural dispersal (S1) yields mixed results that illuminate the challenges of format-level intervention.

**Limitations / non-proof。** `7 Discussion; 8 Limitations`；We derive five structure-aware mitigation strategies from the framework, ranging from zero-cost prompt modifications to training-time regularisation; format flattening (S3) is validated by both accuracy and attention-level evidence from a verbalized-triple control, while structural dispersal (S1) yields mixed results that illuminate the challenges of format-level intervention. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-RAG` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-07-agent/76-rag.md`，Review notes 前正文锚点 `Retrieval Format 也是输入身份` 已完成写入并通过独立 post-write audit。

### [Beyond Compaction: Structured Context Eviction for Long-Horizon Agents](https://arxiv.org/html/2606.11213v1)

**问题与机制。** 原筛选把《Beyond Compaction: Structured Context Eviction for Long-Horizon Agents》关闭或降池；完整摘要显示“We present Context Window Lifecycle (CWL), a context-management scheme that gives long-horizon LLM agents an effectively unbounded working horizon.”。该增量直接改变 AGENT-CONTEXT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`4 Architecture; 6.2 Evaluation Methodology`；可采用的最小机制命题是：We present Context Window Lifecycle (CWL), a context-management scheme that gives long-horizon LLM agents an effectively unbounded working horizon.

**Evaluation proof。** `6 Empirical Evaluation; 6.2 Evaluation Methodology; 6.3 Results`；exact-v1 披露：We describe the annotation protocol, the episode graph, the eviction policy, and the token-accounting loop, and evaluate CWL on long-horizon agentic benchmarks: a single agent session completing 89 sequential tasks across 80 million tokens with no measurable degradation in task accuracy relative to per-task isolated sessions

**Limitations / non-proof。** `7 Limitations and Open Questions`；Compared to summarization-based compaction, CWL avoids four well-known limitations: unpredictable lossiness, destruction of causal structure, blocking model cost, and compression-induced hallucination. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-CONTEXT` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/75-context.md`，Review notes 前正文锚点 `Context Compression 必须保留执行状态，而不只是语义` 已承载长期命题；source 仅作受限证据。

### [SPEAR: A System for Post-Quantization Error-Adaptive Recovery Enabling Efficient Low-Bit LLM Serving](https://arxiv.org/html/2606.11244v1)

**问题与机制。** 原筛选把《SPEAR: A System for Post-Quantization Error-Adaptive Recovery Enabling Efficient Low-Bit LLM Serving》关闭或降池；完整摘要显示“We present SPEAR, a system for post-quantization error-adaptive recovery that improves low-bit LLM serving.”。该增量直接改变 INFER-TENSORRT-LLM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`2.2 SPEAR Framework; Appendix B Method Configuration`；可采用的最小机制命题是：We present SPEAR, a system for post-quantization error-adaptive recovery that improves low-bit LLM serving.

**Evaluation proof。** `5 Evaluation; 5.2 Algorithmic Quality Recovery Results; 5.3 Deployment System Results`；exact-v1 披露：Across challenging per-channel quantization settings, SPEAR recovers 56-75% of the perplexity gap between W4 and FP16 while adding less than 1% model memory overhead and maintaining latency comparable to a widely used 4-bit serving deployment.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；SPEAR introduces lightweight Error Compensators (ECs) modulated by per-token gates and places them only at the most error-sensitive layers identified through a CKA-guided entropy-aware diagnostic. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `INFER-TENSORRT-LLM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-05-inference-system/49-tensorrt-llm.md`，Review notes 前正文锚点 `Post-quantization Recovery 必须同时通过质量与执行 Gate` 已完成写入并通过独立 post-write audit。

### [When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines](https://arxiv.org/html/2606.11265v1)

<!-- claim:SF-2026-ARXIV-2606-11265:start -->
`When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11265v1`：Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate downstream model outputs through malicious knowledge injection.

机制与 owner：Evaluate corpus poisoning after the real chunking and reranking pipeline, distinguishing retrieval exposure from whether the generator follows a poisoned chunk. 状态/数据/控制 owner 固定为 `AGENT-RAG`；Method 锚点是 `§IV Methodology`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§V Experiment` 只证明 `Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate downstream model outputs through malicious knowledge injection.` 上、`Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Attack success depends on retriever, chunk and generator settings; a failed poison under one pipeline does not certify the corpus or other retrieval depths. 反证/外推边界在 `§III Threat Model and §VI Conclusion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11265:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/76-rag.md`，Review notes 前正文锚点 `RAG 安全必须覆盖完整状态生命周期` 已承载长期命题；source 仅作受限证据。

### [Quantifying Subliminal Behavioral Transfer Ratios in Language Model Distillation](https://arxiv.org/html/2606.11270v1)

<!-- claim:SF-2026-ARXIV-2606-11270:start -->
`Quantifying Subliminal Behavioral Transfer Ratios in Language Model Distillation` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11270v1`：Distillation of a language model intended to transfer benign behavior to a student model may also transfer undesirable characteristics, if they are present in the teacher model, a phenomenon known as subliminal learning.

机制与 owner：Measure subliminal behavior transfer through distillation as a ratio conditioned on teacher behavior and student response rather than treating matching outputs as benign data. 状态/数据/控制 owner 固定为 `TRAIN-DATA`；Method 锚点是 `§3 Methodology`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Experiments and Results` 只证明 `Distillation of a language model intended to transfer benign behavior to a student model may also transfer undesirable characteristics, if they are present in the teacher model, a phenomenon known as subliminal learning.` 上、`Llama-2-7B-Chat and Qwen2.5-7B-Instruct teachers/students; GPT-4.1 evaluator` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Observed transfer ratios are model/task specific and do not identify every causal feature; data lineage and behavioral canaries must coexist with aggregate metrics. 反证/外推边界在 `§5 Analysis and §6 Conclusion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11270:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/27-data.md`，Review notes 前正文锚点 `Data lineage 是训练可复现性的前提` 已承载长期命题；source 仅作受限证据。

### [FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse](https://arxiv.org/html/2606.11290v1)

<!-- claim:SF-2026-ARXIV-2606-11290:start -->
`FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11290v1`：Large Language Model (LLM)-based multi-agent systems are increasingly powerful, but current agentic workflow optimization paradigms make an unsatisfying trade-off.

机制与 owner：Precompute reusable workflow fragments into a bank and choose them per query, separating expensive workflow search from repeated online execution. 状态/数据/控制 owner 固定为 `AGENT-WORKFLOW`；Method 锚点是 `§3 Methodology`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Experiments` 只证明 `Large Language Model (LLM)-based multi-agent systems are increasingly powerful, but current agentic workflow optimization paradigms make an unsatisfying trade-off.` 上、`Qwen3-8B FlowBank optimizer; GPT-4o and Qwen3-8B optimizer baselines` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：A stale bank can reuse the wrong flow and query adaptation still needs validation; unconstrained online search remains the fallback for novel tasks. 反证/外推边界在 `Appendix F.1 Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11290:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/81-workflow.md`，Review notes 前正文锚点 `State Machine 是基本模型` 已承载长期命题；source 仅作受限证据。

### [Knowing When to Ask: Self-Gated Clarification for Hierarchical Language Agents](https://arxiv.org/html/2606.11349v1)

<!-- claim:SF-2026-ARXIV-2606-11349:start -->
`Knowing When to Ask: Self-Gated Clarification for Hierarchical Language Agents` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11349v1`：In hierarchical reasoning, failures often originate at intermediate decision points where the agent commits to a wrong branch without recognizing that it lacks critical information.

机制与 owner：Make clarification a self-gated action competing with navigation on the same ordinal scale so information-seeking becomes an observable policy decision. 状态/数据/控制 owner 固定为 `AGENT-PLANNING`；Method 锚点是 `§3 Framework`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§§4–5 Experiments and Results` 只证明 `In hierarchical reasoning, failures often originate at intermediate decision points where the agent commits to a wrong branch without recognizing that it lacks critical information.` 上、`Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：The measured shift depends on benchmark information gaps and answer-channel quality; asking more questions is not itself evidence of better deployment behavior. 反证/外推边界在 `§6 Discussion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11349:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/79-planning.md`，Review notes 前正文锚点 `从目标到状态图` 已承载长期命题；source 仅作受限证据。

### [When More Documents Hurt RAG: Mitigating Vector Search Dilution with Domain-Scoped, Model-Agnostic Retrieval](https://arxiv.org/html/2606.11350v1)

**问题与机制。** 原筛选把《When More Documents Hurt RAG: Mitigating Vector Search Dilution with Domain-Scoped, Model-Agnostic Retrieval》关闭或降池；完整摘要显示“To address this dilution, we propose MASDR-RAG ( Multi-Agent Scoped Domain Retrieval for RAG) and evaluate it on 200 expert-validated queries across five LLM backbones, six corpora, and two index stacks.”。该增量直接改变 AGENT-RAG 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`4 Architecture: MASDR-RAG and Hybrid-Routed`；可采用的最小机制命题是：To address this dilution, we propose MASDR-RAG ( Multi-Agent Scoped Domain Retrieval for RAG) and evaluate it on 200 expert-validated queries across five LLM backbones, six corpora, and two index stacks.

**Evaluation proof。** `5 Evaluation: Proprietary Stack`；exact-v1 披露：Our results indicate that domain scoping using organizational metadata is the key fix, significantly improving P@10 from 0.77 to 0.86 ($p < 0.05$).

**Limitations / non-proof。** `11 Discussion: Scope vs. Orchestration; Limitations`；To address this dilution, we propose MASDR-RAG ( Multi-Agent Scoped Domain Retrieval for RAG) and evaluate it on 200 expert-validated queries across five LLM backbones, six corpora, and two index stacks. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-RAG` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/76-rag.md`，Review notes 前正文锚点 `Online Retrieval Pipeline` 已承载长期命题；source 仅作受限证据。

### [TileFuse: A Fused Mixed-Precision Kernel Library for Efficient Quantized LLM Inference on AMD NPUs](https://arxiv.org/html/2606.11357v1)

<!-- claim:SF-2026-ARXIV-2606-11357:start -->
`TileFuse: A Fused Mixed-Precision Kernel Library for Efficient Quantized LLM Inference on AMD NPUs` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11357v1`：With the growing demand for on-device LLM inference, edge SoCs increasingly integrate NPUs to improve performance and energy efficiency under tight power and thermal budgets.

机制与 owner：Fuse mixed-precision quantized LLM operators around AMD NPU tile/dataflow constraints instead of composing generic kernels with repeated layout conversion. 状态/数据/控制 owner 固定为 `INFER-DECODE`；Method 锚点是 `§4 TileFuse Overview`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§5 Evaluation` 只证明 `With the growing demand for on-device LLM inference, edge SoCs increasingly integrate NPUs to improve performance and energy efficiency under tight power and thermal budgets.` 上、`Gemma 2B and Qwen2.5 3B end-to-end LLM workloads` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Kernel gains are bound to the evaluated AMD NPU and quantization formats; unsupported shapes and quality effects require fallback kernels and model-level checks. 反证/外推边界在 `§6 Discussion and Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11357:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/44-decode.md`，Review notes 前正文锚点 `端侧融合必须围绕真实 Tile / Dataflow Contract` 已承载长期命题；source 仅作受限证据。

### [When Probing Accuracy Saturates, Fragility Resolves: A Complementary Metric for LLM Pre-Training Analysis](https://arxiv.org/html/2606.11375v1)

<!-- claim:SF-2026-ARXIV-2606-11375:start -->
`When Probing Accuracy Saturates, Fragility Resolves: A Complementary Metric for LLM Pre-Training Analysis` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11375v1`：Standard linear probing declares a property "encoded" when a classifier on hidden states achieves high accuracy.

机制与 owner：Add perturbation fragility after linear-probe accuracy saturates, so pretraining checkpoints with equal separability can still be distinguished by representation stability. 状态/数据/控制 owner 固定为 `TRAIN-PRETRAINING`；Method 锚点是 `§3 Methodology`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Results` 只证明 `Standard linear probing declares a property "encoded" when a classifier on hidden states achieves high accuracy.` 上、`OLMo-2 1B and OLMo-3 7B checkpoints` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Fragility depends on probe, perturbation and layer choice and is not a training objective by itself; downstream evaluation still owns usefulness. 反证/外推边界在 `§5.3 Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11375:end -->

**V3 Books Decision。** `Integrate` → `books/part-04-training-system/28-pretraining.md`，Review notes 前正文锚点 `Probe 饱和后，Fragility 只能补充诊断` 已完成写入并通过独立 post-write audit。

### [Small Experiments, Cheaper Decisions: A Case Study in Staged Promotion for Micro-Pretraining](https://arxiv.org/html/2606.11387v1)

<!-- claim:SF-2026-ARXIV-2606-11387:start -->
`Small Experiments, Cheaper Decisions: A Case Study in Staged Promotion for Micro-Pretraining` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11387v1`：Short pretraining runs can reduce experimental cost, but they can also over-promote configurations that only look strong at tiny budgets.

机制与 owner：Use small controlled pretraining experiments as promotion receipts before expensive runs, with explicit continuation/stop decisions instead of scaling every hypothesis. 状态/数据/控制 owner 固定为 `TRAIN-PRETRAINING`；Method 锚点是 `§4.3–4.4 Promotion Schedule and Frozen Rules`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§5 Results` 只证明 `Short pretraining runs can reduce experimental cost, but they can also over-promote configurations that only look strong at tiny budgets.` 上、`Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Micro-scale rank order can invert at scale and cheap experiments omit distributed effects; staged promotion reduces decision cost but cannot guarantee final-model quality. 反证/外推边界在 `§7 Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11387:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/28-pretraining.md`，Review notes 前正文锚点 `Scaling-law Pilot 也是有预算的实验调度` 已承载长期命题；source 仅作受限证据。

### [Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models](https://arxiv.org/html/2606.11409v1)

<!-- claim:SF-2026-ARXIV-2606-11409:start -->
`Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11409v1`：Adversarial robustness evaluations of large language models (LLMs) typically report attack success rate (ASR) under fixed query budgets, implicitly treating all attacks as equally costly.

机制与 owner：Parameterize adversarial risk by cumulative attack FLOPs and report risk-compute curves, not only success at an equal query count. 状态/数据/控制 owner 固定为 `PLATFORM-EVALUATION-SYSTEM`；Method 锚点是 `§2 Framework`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§3–4 Experimental Setup and Results` 只证明 `Three attack strategies on two jailbreak benchmarks, re-parameterized by cumulative FLOPs` 上、`Ten models across three families and four training/alignment stages` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Risk-compute curves are evaluation objects, not service SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：FLOPs omit hardware, latency and monetary factors and attacker strategies can transfer; it is a comparable pressure proxy, not a production security SLO. 反证/外推边界在 `§7 Future Work & Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11409:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [Signed Compression Progress on a Sealed Audit is Goodhart-Resistant](https://arxiv.org/html/2606.11417v1)

**问题与机制。** 原筛选把《Signed Compression Progress on a Sealed Audit is Goodhart-Resistant》关闭或降池；完整摘要显示“The folk claim is that this reward is "credible" because it is paid only for learning.”。该增量直接改变 TRAIN-RLHF 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`§§3–6 sealed-audit setup, telescoping guarantee and scheduler separation`；可采用的最小机制命题是：The folk claim is that this reward is "credible" because it is paid only for learning.

**Evaluation proof。** `§7 Experiments; §8 Lean 4 mechanization`；exact-v1 披露：Experiments confirm the theory: finite-audit deviation scales as n^{-0.527}; signed progress resists clip-farming, stream leakage, and noisy-TV curiosity; naive reusable audits are exploitable by black-box scalar feedback, while standard release defenses keep the attack below the 2 Delta_n threshold.

**Limitations / non-proof。** `§5 Where the theorem breaks; §10 Limitations`；The folk claim is that this reward is "credible" because it is paid only for learning. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-RLHF` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-04-training-system/31-rlhf.md`，Review notes 前正文锚点 `Learning Progress Reward 必须绑定 Sealed Audit` 已完成写入并通过独立 post-write audit。

### [INFRAMIND: Infrastructure-Aware Multi-Agent Orchestration](https://arxiv.org/html/2606.11440v1)

**问题与机制。** 原筛选把《INFRAMIND: Infrastructure-Aware Multi-Agent Orchestration》关闭或降池；完整摘要显示“We introduce INFRAMIND, a framework that makes the entire multi-agent stack infrastructure-aware.”。该增量直接改变 INFER-SCHEDULING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Problem Formulation; 4 Method`；可采用的最小机制命题是：We introduce INFRAMIND, a framework that makes the entire multi-agent stack infrastructure-aware.

**Evaluation proof。** `5 Experiments; 5.2 Main Results`；exact-v1 披露：Across five benchmarks, INFRAMIND delivers up to +7.6 pp accuracy over the prior baseline at low load with up to 7x lower latency, and sustains up to 99.9% SLO compliance under high load where every baseline drops below 50%.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；However, these methods do not consider the runtime state of the serving infrastructure. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `INFER-SCHEDULING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-05-inference-system/56-inference-scheduling.md`，Review notes 前正文锚点 `Infrastructure-aware Multi-Agent Orchestration 必须消费同一状态` 已完成写入并通过独立 post-write audit。

### [Forecasting Future Behavior as a Learning Task](https://arxiv.org/html/2606.11445v1)

<!-- claim:SF-2026-ARXIV-2606-11445:start -->
`Forecasting Future Behavior as a Learning Task` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11445v1`：Trust in an AI system is often anchored by explanations of how it works, which one then uses to forecast its behavior on new inputs.

机制与 owner：Train a single-pass behavior forecaster directly on reasoning trajectories to predict rerun stability and response changes without pretending the trace is a faithful explanation. 状态/数据/控制 owner 固定为 `PLATFORM-EVALUATION-SYSTEM`；Method 锚点是 `§3 Method`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§§4–5 evaluation and ablation` 只证明 `Trust in an AI system is often anchored by explanations of how it works, which one then uses to forecast its behavior on new inputs.` 上、`OLMo-3-7B-Think and Qwen3.5-2B target LRMs; GPT-5.4 and Claude Opus 4.6 naive readers` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Forecast accuracy is limited to trained behavior questions and model distributions; a forecaster predicts outcomes but does not explain causes or authorize actions. 反证/外推边界在 `§7 Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11445:end -->

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `行为预测是独立 Evaluation Task，不是解释的副产品` 已完成写入并通过独立 post-write audit。

### [ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajectories](https://arxiv.org/html/2606.11520v1)

<!-- claim:SF-2026-ARXIV-2606-11520:start -->
`ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajectories` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11520v1`：Training capable OS agents requires data that simultaneously captures structured user intents, multi-turn task delegation, and grounded tool execution--properties absent from existing datasets.

机制与 owner：Synthesize OS-agent data through structured intent, role-locked multi-turn simulation and execution of every tool call in an isolated live workspace. 状态/数据/控制 owner 固定为 `TRAIN-DATA`；Method 锚点是 `§4 ISE Synthesis Paradigm`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§5 Experiments` 只证明 `Training capable OS agents requires data that simultaneously captures structured user intents, multi-turn task delegation, and grounded tool execution--properties absent from existing datasets.` 上、`Qwen3-8B fine-tuned model; Qwen3-8B, Qwen3-32B, and GPT-4o references` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：A generated intent distribution and one workspace image can miss real-user states; execution grounding proves tool effects in that sandbox, not external safety. 反证/外推边界在 `§6 Limitations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-11520:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/27-data.md`，Review notes 前正文锚点 `Data lineage 是训练可复现性的前提` 已承载长期命题；source 仅作受限证据。

### [SkillJuror: Measuring How Agent Skill Organization Changes Runtime Behavior](https://arxiv.org/html/2606.11543v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Skill 的目录组织本身会改变资源读取与有效采用轨迹；Progressive Disclosure 必须以知识等价变体、trajectory evidence 与 verifier outcome 联合评测。

**State / data / control owner。** `AGENT-REFLECTION` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11543v1 §4 Experiments; §4.1 setup; §§4.2–4.5` 支持 `82 SkillsBench tasks × 3 conditions × 5 trials`；模型 `GPT-5.4 high reasoning`；硬件 `Not Disclosed — hosted runtime hardware is not identified`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11543v1 §3 Method; §§3.2–3.4 controlled variants/runtime evidence`；counterevidence locator：`arXiv:2606.11543v1 §6 Limitations; Appendix E layout sensitivity`。

**Trade-off / failure / coexistence / evolution。** 按需资源降低入口负担但可能产生 fanout tax；精确格式、阈值或长 artifact pipeline 仍适合 flat/local instructions。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11543:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11543v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11543:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/80-reflection.md`，Review notes 前正文锚点 `Reflection 应输出可执行诊断` 已承载长期命题；source 仅作受限证据。

### [Defense Against Prompt Inversion Attacks: An Information-Theoretic Approach for LLM Collaborative Inference](https://arxiv.org/html/2606.11592v1)

**问题与机制。** 原筛选把《Defense Against Prompt Inversion Attacks: An Information-Theoretic Approach for LLM Collaborative Inference》关闭或降池；完整摘要显示“We propose an information-theoretic defense framework for prompt inversion in collaborative LLM inference.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method: Privacy-Preserving Collaborative Inference; 3.2 Privacy Adapter Architecture`；可采用的最小机制命题是：We propose an information-theoretic defense framework for prompt inversion in collaborative LLM inference.

**Evaluation proof。** `6 Experimental Evaluation; 6.1 Experimental Setup; 6.2 Main Results: Privacy-Utility Tradeoff and Bottleneck Ablation`；exact-v1 披露：Extensive experiments across multiple settings demonstrate that our method achieves superior privacy-utility-latency tradeoffs compared to existing defenses (up to 35% reduction in attack success), providing a principled foundation for private and efficient collaborative LLM inference.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Existing defenses rely largely on heuristic perturbations or empirical tuning, offering limited theoretical understanding of privacy leakage and its interaction with utility and latency constraints. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Sovereign Assurance Boundary: Certificate-Bound Admission for Agentic Infrastructure](https://arxiv.org/html/2606.11632v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Agent proposal 必须编译为 typed contract，并绑定 evidence digest、policy/revocation epoch 与 scoped broker identity 后才可成为执行 authority。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11632v1 §7 Evaluation Methodology and Targets; §7.3 setup` 支持 `500 contracts × five trials; 2,500 admissions`；模型 `Go SAB prototype, OPA, PostgreSQL ledger, three-validator SQA`；硬件 `Single-node local workstation; exact CPU/GPU not disclosed`；精度 `Not applicable — control-plane prototype`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11632v1 §§3–5 SAB model, airlock and broker`；counterevidence locator：`arXiv:2606.11632v1 §9 Discussion and Limitations; §9.2`。

**Trade-off / failure / coexistence / evolution。** 证书化增加 admission latency 和 TCB；证据陈旧、policy/validator 漂移或 emergency bypass 会破坏保证，IAM 仍保留。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11632:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11632v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11632:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security](https://arxiv.org/html/2606.11671v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Skill 安全不能只审静态文件；应按 capability profile 构造 targeted runtime context，在 sandbox 中执行并以 trace evidence 标注行为。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11671v1 §5 Evaluation` 支持 `100 OpenClaw skills with static baselines and evolving attacks`；模型 `LLM-assisted profiler/task generator/trace judge; exact models not fully disclosed`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11671v1 §3 Runtime Skill Audit; §4 implementation`；counterevidence locator：`arXiv:2606.11671v1 §7 Limitations`。

**Trade-off / failure / coexistence / evolution。** 动态探测覆盖 context-dependent behavior，却不穷尽 trigger；模型化 task/judge 会漂移，静态扫描仍是廉价第一层。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11671:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11671v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11671:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents](https://arxiv.org/html/2606.11680v1)

**问题与机制。** 原筛选把《Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents》关闭或降池；完整摘要显示“In this work, we present HORMA, a Hierarchical Organize-and-Retrieve Memory Agent that organizes experience into a file-system-like hierarchical structure, where summarized entities are linked to the corresponding raw trajectories, enabling efficient access without losing detailed information.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：In this work, we present HORMA, a Hierarchical Organize-and-Retrieve Memory Agent that organizes experience into a file-system-like hierarchical structure, where summarized entities are linked to the corresponding raw trajectories, enabling efficient access without losing detailed information.

**Evaluation proof。** `5 Experiments; 5.1 Experimental Setup; 5.2 Main Results`；exact-v1 披露：Compared to existing methods, it consistently achieves better efficiency-performance trade-offs and generalizes effectively to unseen tasks.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Compared to existing methods, it consistently achieves better efficiency-performance trade-offs and generalizes effectively to unseen tasks. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MEMORY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness](https://arxiv.org/html/2606.11686v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：生产 Agent 的 deterministic scaffold 应按 ontology/intent/routing/decomposition/escalation/safety/memory 分层，用 no-LLM regression-locked slices 阻止 aggregate pass rate 掩盖局部回归。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11686v1 §4 Evaluation; controlled regression injection` 支持 `238 cases across 23 slices; seven injected regressions; two tenants`；模型 `No-LLM deterministic ordering-agent scaffold`；硬件 `Not Disclosed`；精度 `Not applicable — deterministic harness`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11686v1 §3 Layer-Isolated Evaluation; taxonomy and pure mode`；counterevidence locator：`arXiv:2606.11686v1 §5 Discussion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** 分层 gate 定位快但只覆盖显式 scaffold；端到端 stochastic behavior 与未被 exercise 的 layer 仍需独立评测。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11686:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11686v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11686:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [Goal-Autopilot: A Verifiable Anti-Fabrication Firewall for Unattended Long-Horizon Agents](https://arxiv.org/html/2606.11688v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：长程 Agent 应把 durable FSM、stateless ticks、falsifiable gate 与 terminal hard floor 外置，使未执行/未通过 gate 时最多 honest stall，不能宣告完成。

**State / data / control owner。** `AGENT-WORKFLOW` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11688v1 §6 Empirical evaluation; §6.5 scaled corpus` 支持 `3,150 paired cells; 70 tasks including 50 SWE-bench Lite`；模型 `Three systems × three models; model identities partly withheld`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11688v1 §3 Method; §4 theorem; §5 System`；counterevidence locator：`arXiv:2606.11688v1 §7 Limitations; Appendix A auditor boundary`。

**Trade-off / failure / coexistence / evolution。** hard floor 用 coverage 换 honesty；定理依赖 gate soundness、floor enforcement 与 plan coverage，不能证明任务本身正确。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11688:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11688v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11688:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/81-workflow.md`，Review notes 前正文锚点 `State Machine 是基本模型` 已承载长期命题；source 仅作受限证据。

### [Beyond Per-Token Pricing: A Concurrency-Aware Methodology for LLM Infrastructure Cost Estimation](https://arxiv.org/html/2606.11690v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：LLM 成本必须把 offered load λ 经 Little's Law 映射为 in-flight concurrency 与实际利用率；固定 100% utilization 的每 token 估价会系统性误导低负载自托管。

**State / data / control owner。** `PLATFORM-COST` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11690v1 §4 Experimental Setup; §5 Results` 支持 `42 H100 benchmarks plus 56 A100 cross-hardware runs, 1–10 rps and saturation sweeps`；模型 `Dense, ultra-sparse MoE and sparse MoE models`；硬件 `NVIDIA H100 and A100 80GB PCIe`；精度 `FP16 and FP8 where supported`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11690v1 §3 Concurrency-Aware Cost Framework`；counterevidence locator：`arXiv:2606.11690v1 §6.8 Scope; §6.9 Limitations`。

**Trade-off / failure / coexistence / evolution。** 真实 meter 提高归因但需要 workload replay；burst、prefix cache、I/O shape 与硬件 FP8 支持会改变 crossover。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11690:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11690v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11690:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/70-cost.md`，Review notes 前正文锚点 `Utilization 应由实际负载推出，而不是由计算器假定` 已承载长期命题；source 仅作受限证据。

### [Substrate Asymmetry in User-Side Memory: A Diagnostic Framework](https://arxiv.org/html/2606.11712v1)

**问题与机制。** 原筛选把《Substrate Asymmetry in User-Side Memory: A Diagnostic Framework》关闭或降池；完整摘要显示“We show this aggregate metric hides opposite-direction failures.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`2.2 Memory architectures; 3 Method; Appendix A Appendix A: Method (full detail)`；可采用的最小机制命题是：We show this aggregate metric hides opposite-direction failures.

**Evaluation proof。** `4 Results; Appendix B Appendix B: Results (full per-axis detail)`；exact-v1 披露：We show this aggregate metric hides opposite-direction failures.

**Limitations / non-proof。** `6 Discussion; Appendix D Appendix D: Discussion (full); D.4 Limitations (honest)`；We contribute the diagnostic framework, the diagnosed real-data negative, the alignment-tax replication, and the routing-as-classification finding. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MEMORY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [Making Locality-aware GEMM Compatible with Page-Granularity Placement on Chiplet GPUs](https://arxiv.org/html/2606.11718v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Chiplet GPU 的 GEMM locality 需要让 chiplet-local tiles 在 global address space 连续，使 page-granularity placement 与 CTA affinity 一致。

**State / data / control owner。** `INFER-GPU-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11718v1 §IV Evaluation; §IV-A methodology` 支持 `Qwen3-30B and Llama-3.1-70B inference/training GEMM shapes`；模型 `Qwen3-30B; Llama-3.1-70B`；硬件 `Modeled multi-chiplet GPU; exact product not claimed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11718v1 §III Chiplet-Contiguous Layout`；counterevidence locator：`arXiv:2606.11718v1 §V Conclusion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** 布局变换减少 remote HBM traffic，却要求 runtime/compiler 重排；对非 GEMM、动态 shape 或不同 interleave policy 不构成普遍收益。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11718:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11718v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11718:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/54-gpu-memory.md`，Review notes 前正文锚点 `Weights 与 KV 的联合 HBM 预算：可提交的运行时精度页` 已承载长期命题；source 仅作受限证据。

### [External Experience Serving in Production LLM Systems: A Deployment-Oriented Study of Quality-Cost Trade-offs](https://arxiv.org/html/2606.11806v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：生产 experience serving 要按 task cost structure 在 no experience、global injection 与 selective retrieval 间选择，以 quality、prompt cost、latency 与 break-even 联合决策。

**State / data / control owner。** `AGENT-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11806v1 §4 setup; §5 Results; Appendices E–G` 支持 `Production moderation plus tool-use and GPQA contrast tasks`；模型 `Reasoning/instruct model variants disclosed in Appendix A.4`；硬件 `Not Disclosed — hosted serving hardware not identified`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11806v1 §3 Experience Serving in Production`；counterevidence locator：`arXiv:2606.11806v1 §4.4 claim boundary; Appendix H interpretation scope`。

**Trade-off / failure / coexistence / evolution。** selective retrieval 控制 prompt burden，但 miss/over-trigger 与 selector overhead 会伤害质量；规则少或高度共享时 global compact 仍成立。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11806:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11806v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11806:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [Grammar-Constrained Decoding Can Jailbreak LLMs into Generating Malicious Code](https://arxiv.org/html/2606.11817v1)

**问题与机制。** 原筛选把《Grammar-Constrained Decoding Can Jailbreak LLMs into Generating Malicious Code》关闭或降池；完整摘要显示“To address this vulnerability, we propose CodeShield, a safety alignment approach that robustly preserves safe behavior even under attacker-controlled grammar constraints.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`IV Methodology`；可采用的最小机制命题是：To address this vulnerability, we propose CodeShield, a safety alignment approach that robustly preserves safe behavior even under attacker-controlled grammar constraints.

**Evaluation proof。** `V Experimental Setup; VI Experimental Results`；exact-v1 披露：Our experiments show that simply applying a benign code grammar constraint can effectively jailbreak LLMs.

**Limitations / non-proof。** `VII Discussion; VII-C Threats to Validity`；Such code is semantically harmless, so it does not implement the malicious request, and structurally diverse, so it is difficult to suppress through grammar tightening. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `Decoding Constraint 也是不可信控制输入` 已完成写入并通过独立 post-write audit。

### [Task-Aware Structured Memory for Dynamic Multi-modal In-Context Learning](https://arxiv.org/html/2606.11853v1)

**问题与机制。** 原筛选把《Task-Aware Structured Memory for Dynamic Multi-modal In-Context Learning》关闭或降池；完整摘要显示“We introduce TASM (Task-Aware Structured Memory), a training-free framework that addresses these limitations through task-aware, structure-preserving, and dynamically accessible memory construction.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methodology; 3.1 Preliminaries and Problem Formulation`；可采用的最小机制命题是：We introduce TASM (Task-Aware Structured Memory), a training-free framework that addresses these limitations through task-aware, structure-preserving, and dynamically accessible memory construction.

**Evaluation proof。** `4 Experiments; 4.1 Experimental Setting; 4.2 Experimental Results`；exact-v1 披露：Evaluations confirm TASM maintains high performance under heavy compression, effectively balancing efficiency with adaptability.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Multi-modal large language models (MLLMs) depend on in-context learning (ICL) for rapid task adaptation, but their scalability is severely limited by finite context windows and the growing cost of key-value (KV) caches in long multi-modal sequences. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MEMORY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [Harnessing Routing Foresight for Micro-step-level MoE load balancing in RL Post-training](https://arxiv.org/html/2606.11867v1)

**问题与机制。** 原筛选把《Harnessing Routing Foresight for Micro-step-level MoE load balancing in RL Post-training》关闭或降池；完整摘要显示“We introduce ForeMoE, a micro-step-level load balancing system for MoE RL post-training.”。该增量直接改变 TRAIN-DISTRIBUTED-TRAINING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`2.1. MoE Architecture`；可采用的最小机制命题是：We introduce ForeMoE, a micro-step-level load balancing system for MoE RL post-training.

**Evaluation proof。** `10. Evaluation; 10.1. Experimental Setup; 10.4. Case Study`；exact-v1 披露：Evaluations on 64 GPUs demonstrate that ForeMoE achieves up to a 1.45$\times$ speedup over state-of-the-art RL post-training systems.

**Limitations / non-proof。** `3. Observations and Current Limitations`；Instead of relying on historical statistics, ForeMoE exploits the multi-stage RL pipeline (rollout, recompute, policy update) by using foreseeable routing information from the rollout stage to proactively guide load balancing in the remaining stages. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-DISTRIBUTED-TRAINING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/36-distributed-training.md`，Review notes 前正文锚点 `Expert Placement 与 Sample Packing 可以共享 Rollout Routing State` 已承载长期命题；source 仅作受限证据。

### 分母前关闭（保留审计轨迹）：Agents All the Way Down

独立复核结论：该 family 是单项目方法论与既有 agent building practice 的重新组织，没有提供可独立定位的新 state/control/evaluation contract；以下作者侧审阅轨迹仅用于解释误收原因，不计入 Candidate 或 Books。

**问题与机制。** 原筛选把《Agents All the Way Down; A Methodology for Building Custom AI Agents from Substrate to Production》关闭或降池；完整摘要显示“We present it as a transferable practice, independent of any language or framework.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 PDF；方法链由摘要中的 P1–P5 生命周期定义定位`；可采用的最小机制命题是：We present it as a transferable practice, independent of any language or framework.

**Evaluation proof。** `exact-v1 PDF；生产案例与边界说明`；exact-v1 披露：We present it as a transferable practice, independent of any language or framework.

**Limitations / non-proof。** `exact-v1 PDF；摘要未披露独立 limitations 标题`；We present it as a transferable practice, independent of any language or framework. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-WORKFLOW` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Pre-denominator Close — Not applicable`；保留审计轨迹但不计入 Candidate、Books 分布或 root 写入队列。

### [WarpGuard: Protected-Site Control-Flow Integrity for CUDA SASS Binaries](https://arxiv.org/html/2606.11871v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：CUDA binary security 的 owner 是 executed SASS consumption site；protected-site CFI 必须恢复 site policy、验证 forward/backward transfer 并对 unsupported surface 显式出账。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11871v1 §VI Evaluation; §VII backend cost` 支持 `77 CUDA artifacts; 51,621 sites; 52.2M dynamic checks`；模型 `CUDA SASS binaries`；硬件 `NVIDIA CUDA testbed; exact GPU bound in §VI-A`；精度 `Not applicable — binary instrumentation`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11871v1 §III threat model; §§IV–V design/implementation`；counterevidence locator：`arXiv:2606.11871v1 §VI-H portability boundaries; §VIII Discussion`。

**Trade-off / failure / coexistence / evolution。** SASS-level enforcement覆盖真实执行面但增加 instrumentation/callback cost；未恢复 site 必须 fail closed 或留在 denominator 外。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11871:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11871v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11871:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Gerrymandering the Warp: Non-Control-Data Attacks on CUDA Collective Decision](https://arxiv.org/html/2606.11878v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：GPU collective 的 mask、predicate、source lane、descriptor 与 epoch 是 authority-bearing non-control data；应在 collective 使用前绑定 membership/contribution/role/time。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11878v1 §VI evidence; §VII-D mitigation results` 支持 `CUDA contract-conformance suite across four authority dimensions`；模型 `CUDA collective primitives and CIC wrapper`；硬件 `NVIDIA CUDA testbed; exact GPU in evidence appendix`；精度 `Not applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11878v1 §§III–V participation authority and CSC`；counterevidence locator：`arXiv:2606.11878v1 §VII-E Cost and Limits; §VIII Discussion and Limitations`。

**Trade-off / failure / coexistence / evolution。** CIC 防止 range-valid metadata 扭曲授权，却需保存 reference membership/epoch；普通 CFI 不覆盖此语义面。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11878:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11878v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11878:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Characterizing Software Aging in GPU-Based LLM Serving Systems](https://arxiv.org/html/2606.11916v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：LLM serving release 不能只测分钟级峰值；应在 host/device/client 三面进行长时 aging campaign，并用 autocorrelation-aware statistics 区分 leak、runtime 与 workload regime。

**State / data / control owner。** `PLATFORM-MONITORING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11916v1 §IV Results; §§IV-A–IV-E` 支持 `216-hour campaign; six co-located deployments; Poisson stress`；模型 `Qwen2.5-7B-Instruct on vLLM, Triton-vLLM and PyTorch/HF`；硬件 `One host with 3× NVIDIA L40S`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11916v1 §III Methodology`；counterevidence locator：`arXiv:2606.11916v1 §V Threats to Validity`。

**Trade-off / failure / coexistence / evolution。** 长时 campaign 昂贵且 co-location 可能混入 contention；短基准仍适合 kernel 回归，但不能替代 rejuvenation evidence。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11916:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11916v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11916:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/67-monitoring.md`，Review notes 前正文锚点 `条件化机制分支与共存边界` 已承载长期命题；source 仅作受限证据。

### [Online Shift Detection and Conformal Adaptation for Deployed Safety Classifiers](https://arxiv.org/html/2606.11949v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：deployed safety classifier 需要 reference-window calibration、sequential alarm、multiplicity control 与 alarm-triggered conformal abstention；shift sensor 与安全 authority 分离。

**State / data / control owner。** `PLATFORM-MONITORING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11949v1 §4 setup; §5 Results` 支持 `4 classifiers × 5 shifts × 20 seeds × 2 windows; 800 cells`；模型 `Four deployed safety classifiers`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11949v1 §3 Methods; §§3.1–3.10`；counterevidence locator：`arXiv:2606.11949v1 §6.5 Limitations; §5.4 ground-truth regimes`。

**Trade-off / failure / coexistence / evolution。** 检测可能对 target attack 无信号，density ratio 也会退化；abstention 恢复 coverage 不等于阻止攻击。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11949:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11949v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11949:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/67-monitoring.md`，Review notes 前正文锚点 `条件化机制分支与共存边界` 已承载长期命题；source 仅作受限证据。

### [Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents](https://arxiv.org/html/2606.11998v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：trusted monitor 能力落后时，可用更强 untrusted monitor 评估 action，再让 weaker trusted model 监督其透明推理；control graph 要显式保存 collusion threat model。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.11998v1 §4 Results; Appendix C red/blue teaming` 支持 `Multi-turn BashArena software-engineering tasks`；模型 `Trusted, untrusted-agent and intermediate-monitor model configurations`；硬件 `Not Disclosed — API/runtime hardware not identified`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.11998v1 §3 Methods; §3.1 threat model/protocol`；counterevidence locator：`arXiv:2606.11998v1 §5 Discussion, Transparent CoT assumption and Limitations`。

**Trade-off / failure / coexistence / evolution。** bootstrapping 延长弱 monitor 生命周期，却依赖 transparent CoT；隐藏推理、steganography 或共同盲点会失效。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-11998:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.11998v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-11998:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### 分母前关闭（保留审计轨迹）：Scientific Novelty Assessment

独立复核结论：该 family 的对象是 AI for Science 中的 scientific novelty judgment；当前范围明确暂缓该阶段，以下作者侧审阅轨迹不计入 Candidate 或 Books。

**问题与机制。** 原筛选把《On the Limits of LLM-as-Judge for Scientific Novelty Assessment》关闭或降池；完整摘要显示“We introduce RQ-Bench, a benchmark built from recent arXiv papers.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：We introduce RQ-Bench, a benchmark built from recent arXiv papers.

**Evaluation proof。** `5 Evaluation Setup; 6 Experiments; 6.1 Experimental Setup`；exact-v1 披露：This makes novelty evaluation a central problem.

**Limitations / non-proof。** `6.2 Results and Discussions; Limitations`；These RQs are not the only valid questions for the same background. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Pre-denominator Close — Not applicable`；保留审计轨迹但不计入 Candidate、Books 分布或 root 写入队列。

### [FORT-Searcher: Synthesizing Shortcut-Resistant Search Tasks for Training Deep Search Agents](https://arxiv.org/html/2606.12087v1)

**问题与机制。** 原筛选把《FORT-Searcher: Synthesizing Shortcut-Resistant Search Tasks for Training Deep Search Agents》关闭或降池；完整摘要显示“We formalize this gap with a shortcut-aware difficulty framework and identify four actionable shortcut risks: evidence co-coverage, single-clue selectivity, exposed constants, and prior-knowledge binding.”。该增量直接改变 TRAIN-DATA 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`2 Difficulty Framework; 2.1 Problem Formulation; 3 Methodology`；可采用的最小机制命题是：We formalize this gap with a shortcut-aware difficulty framework and identify four actionable shortcut risks: evidence co-coverage, single-clue selectivity, exposed constants, and prior-knowledge binding.

**Evaluation proof。** `4 Experiment; 4.1 Experimental Setup; 4.2 Main Results`；exact-v1 披露：Experiments show that FORT induces longer pre-answer search and fewer shortcut patterns than existing open-source deep search datasets.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Existing synthesis methods often increase apparent difficulty by enriching graph structures, but structural complexity alone does not guarantee realized search difficulty: the intended search process can collapse through a cheaper identifying route. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-DATA` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/27-data.md`，Review notes 前正文锚点 `Data lineage 是训练可复现性的前提` 已承载长期命题；source 仅作受限证据。

### [The Brain That Goes Quiet: Serving a Large Model's Knowledge at 131 Tokens per Second on an 8 GB Laptop by Removing the Large Model from the Runtime Path](https://arxiv.org/html/2606.12154v1)

**问题与机制。** 原筛选把《The Brain That Goes Quiet: Serving a Large Model's Knowledge at 131 Tokens per Second on an 8 GB Laptop by Removing the Large Model from the Runtime Path》关闭或降池；完整摘要显示“That result solved a placement problem and immediately exposed a different one: even correctly placed, the large model needed roughly four seconds to answer, because it was still being invoked at every query.”。该增量直接改变 INFER-PREFILL 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`4 The Horsehair Architecture`；可采用的最小机制命题是：That result solved a placement problem and immediately exposed a different one: even correctly placed, the large model needed roughly four seconds to answer, because it was still being invoked at every query.

**Evaluation proof。** `5 Experimental Setup; 6 Results`；exact-v1 披露：A 16-case verification gate blocked all ten corrupted entries while admitting all six supported ones.

**Limitations / non-proof。** `8 Limitations`；During an offline phase, the large model reads source documents and writes verified answer entries into a structured knowledge store; at runtime, only a lightweight router, a deterministic renderer, and a 1B-class model are active. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `INFER-PREFILL` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Only report`；该 exact-v1 仅支持受限案例，尚不足以改变长期 Books 机制链，不创建正文或 trace 采用链。

### [A Controlled Study of Decoding-Time Truthfulness Methods on Instruction-Tuned LLMs](https://arxiv.org/html/2606.12160v1)

**问题与机制。** 原筛选把《A Controlled Study of Decoding-Time Truthfulness Methods on Instruction-Tuned LLMs》关闭或降池；完整摘要显示“However, modern instruction-tuned LLMs already achieve substantially higher baselines (61-76%), raising the question of whether these methods remain effective in practice.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Evaluation Framework; 4.5 Deliberative Methods`；可采用的最小机制命题是：However, modern instruction-tuned LLMs already achieve substantially higher baselines (61-76%), raising the question of whether these methods remain effective in practice.

**Evaluation proof。** `3 Evaluation Framework; 4 Experiments; 4.1 Main Results`；exact-v1 披露：We design a six-control evaluation framework -- out-of-distribution training, multi-judge validation, simple decoding baselines, confound controls, bootstrap confidence intervals, and seed variance -- and apply it across 5 models (1B-70B), 3 benchmarks, and 15 methods.

**Limitations / non-proof。** `5 Discussion and Conclusion`；We release a seven-point evaluation checklist and discuss implications for future truthfulness research. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [Mind your key: An Empirical Study of LLM API Credential Leakage in iOS Apps](https://arxiv.org/html/2606.12212v1)

**问题与机制。** 原筛选把《Mind your key: An Empirical Study of LLM API Credential Leakage in iOS Apps》关闭或降池；完整摘要显示“We present the first in-depth empirical study of API key leakage in LLM-integrated apps.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3. Methodology`；可采用的最小机制命题是：We present the first in-depth empirical study of API key leakage in LLM-integrated apps.

**Evaluation proof。** `exact-v1 evaluation/results section`；exact-v1 披露：Our findings show that LLM API key leakage is both prevalent and persistent in the iOS ecosystem, exposing a systemic gap between developer practice and secure integration principles, and suggest that secure LLM integration requires not only developer awareness but also explicit security guidance from providers and platform-level enforcement.

**Limitations / non-proof。** `6. Threats to Validity`；To assess remediation, we re-analyzed the same 282 vulnerable applications three months after responsible disclosure; only 28% had remediated the reported vulnerability, while 72% remained exploitable, with persistent issues stemming from unauthenticated backends and broken JWT implementations. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Rule Taxonomy and Evolution in AI IDEs: A Mining and Survey Study](https://arxiv.org/html/2606.12231v1)

**问题与机制。** 原筛选把《Rule Taxonomy and Evolution in AI IDEs: A Mining and Survey Study》关闭或降池；完整摘要显示“Despite their role in aligning AI behavior with developer intent, the taxonomy, evolution, and practical impact of these rules remain largely unexplored.”。该增量直接改变 AGENT-PROMPT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`4. Research Methodology`；可采用的最小机制命题是：Despite their role in aligning AI behavior with developer intent, the taxonomy, evolution, and practical impact of these rules remain largely unexplored.

**Evaluation proof。** `3.1. Evaluation and Impact of AI IDEs; 5. Study Results; 6.1. Interpretation of Study Results`；exact-v1 披露：Our study provides empirical insights that can help developers optimize prompting strategies and guide tool builders in designing automated conflict-detection and context-management mechanisms for AI IDEs.

**Limitations / non-proof。** `6. Discussion; 7. Threats to Validity`；Our study provides empirical insights that can help developers optimize prompting strategies and guide tool builders in designing automated conflict-detection and context-management mechanisms for AI IDEs. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-PROMPT` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/74-prompt.md`，Review notes 前正文锚点 `Prompt 生命周期` 已承载长期命题；source 仅作受限证据。

### [VIA-SD: Verification via Intra-Model Routing for Speculative Decoding](https://arxiv.org/html/2606.12243v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：把 draft verification 从二元 accept/full-recompute 演进为 direct/slim/full 三层，并用 intra-model routing 选择 verifier 资源。

**State / data / control owner。** `INFER-SPECULATIVE-DECODING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12243v1 §4 Experiments` 支持 `Four tasks across T5/Gemma model families`；模型 `T5 and Gemma families`；硬件 `Disclosed in §4.1; no cross-paper normalization`；精度 `Disclosed in §4.1 where applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12243v1 §3 Methodology; §§3.2–3.5`；counterevidence locator：`arXiv:2606.12243v1 §4.4 additional analysis; §5 Conclusion`。

**Trade-off / failure / coexistence / evolution。** slim verifier 节约 full-model calls 但引入 routing error/threshold；exact rejection contract 与 full verifier fallback 必须保留。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12243:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12243v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12243:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/48-speculative-decoding.md`，Review notes 前正文锚点 `Correctness owner 没有改变` 已承载长期命题；source 仅作受限证据。

### [A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents](https://arxiv.org/html/2606.12320v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：生产 Agent governance 应分 reasoning/network/identity/endpoint/data 五平面，并把 stop-anywhere mediation、capability attenuation、TTL 与 structured audit 组合为 cross-plane control。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12320v1 §9 case studies; §10 validation roadmap` 支持 `Seven canonical workflow threats plus production case studies`；模型 `Reference architecture; not a model benchmark`；硬件 `Not applicable`；精度 `Not applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12320v1 §§3–8 threat model, five planes and composed architecture`；counterevidence locator：`arXiv:2606.12320v1 §11 Limitations and Open Questions`。

**Trade-off / failure / coexistence / evolution。** 多平面提高可中断性与归因，却增加 latency/state consistency/TCB；reference architecture 不证明生产效果。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12320:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12320v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12320:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`。五平面是实现 taxonomy；现有正文已经拥有 delegation/effect-time authorization、capability attenuation、跨通道 influence graph 与 evidence chain，不追加平行架构清单。

### [PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents](https://arxiv.org/html/2606.12329v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Coding-agent memory 可用 append-only typed event log 作 authoritative state，并确定性投影摘要；pre-action gate 只消费既有 failure/fragility evidence。

**State / data / control owner。** `AGENT-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12329v1 §7 Evaluation` 支持 `Two-month self-study, 10 projects, 207 events`；模型 `Local-first projectmem with MCP/CLI`；硬件 `Local developer environment; hardware not disclosed`；精度 `Not applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12329v1 §3 System Design; §§4–6 architecture/implementation`；counterevidence locator：`arXiv:2606.12329v1 §8 Limitations and Future Work`。

**Trade-off / failure / coexistence / evolution。** event sourcing 提供 provenance/rollback，但 self-study 不能证明跨团队收益；错误 judgment 仍需 supersession 与关闭开关。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12329:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12329v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12329:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [OCELOT: Inference-Leakage Budgets for Privacy-Preserving LLM Agents](https://arxiv.org/html/2606.12341v1)

**问题与机制。** 原筛选把《OCELOT: Inference-Leakage Budgets for Privacy-Preserving LLM Agents》关闭或降池；完整摘要显示“We recast agent privacy as \emph{posterior-risk control} and present OCELOT, a runtime mediator that budgets how much an adversary's belief about a secret may improve across a trajectory, rather than filtering outputs.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`III Problem Formulation; IV-A Architecture and Rubrics`；可采用的最小机制命题是：We recast agent privacy as \emph{posterior-risk control} and present OCELOT, a runtime mediator that budgets how much an adversary's belief about a secret may improve across a trajectory, rather than filtering outputs.

**Evaluation proof。** `V Experiments; V-A Experimental Setup; V-B Privacy–Utility Evaluation`；exact-v1 披露：Across diverse agent benchmarks and recent defenses, OCELOT attains significantly lower leakage at higher task utility, resists adaptive injection, jailbreak, cumulative inference, and sink collusion, and adds only modest overhead.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Across diverse agent benchmarks and recent defenses, OCELOT attains significantly lower leakage at higher task utility, resists adaptive injection, jailbreak, cumulative inference, and sink collusion, and adds only modest overhead. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `Agent Privacy 必须对整条 Trajectory 记账` 已完成写入并通过独立 post-write audit。

### [ALIGNBEAM : Inference-Time Alignment Transfer via Cross-Vocabulary Logit Mixing](https://arxiv.org/html/2606.12342v1)

**问题与机制。** 原筛选把《ALIGNBEAM : Inference-Time Alignment Transfer via Cross-Vocabulary Logit Mixing》关闭或降池；完整摘要显示“We present ALIGNBEAM, a training-free method that lifts this restriction by translating anchor logits into the target model's vocabulary token-by-token at each decoding step; a small LLM judge then selects the safest among K candidate continuations.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method; J.5 Qwen2.5-7B-Base: Same-Family Anchor Size and Method Ablation`；可采用的最小机制命题是：We present ALIGNBEAM, a training-free method that lifts this restriction by translating anchor logits into the target model's vocabulary token-by-token at each decoding step; a small LLM judge then selects the safest among K candidate continuations.

**Evaluation proof。** `4 Experiments; 5 Results; 5.1 Headline Results`；exact-v1 披露：Across both cross-vocabulary and same-vocabulary evaluation pairs, ALIGNBEAM substantially raises refusal on adversarial benchmarks while keeping task accuracy and inference overhead within practical bounds.

**Limitations / non-proof。** `Limitations; Appendix L Extended Limitations`；The results show that safety alignment can be transferred between model families at inference time, without touching either model's weights. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Only report`；该 exact-v1 仅支持受限案例，尚不足以改变长期 Books 机制链，不创建正文或 trace 采用链。

### [Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks](https://arxiv.org/html/2606.12344v1)

**问题与机制。** 原筛选把《Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks》关闭或降池；完整摘要显示“We introduce Claw-SWE-Bench, a multilingual SWE-bench-style benchmark and adapter protocol that makes heterogeneous agent harnesses, or claws, comparable under fair settings including a fixed prompt, runtime budget, workspace contract, patch extraction procedure, and evaluator.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：We introduce Claw-SWE-Bench, a multilingual SWE-bench-style benchmark and adapter protocol that makes heterogeneous agent harnesses, or claws, comparable under fair settings including a fixed prompt, runtime budget, workspace contract, patch extraction procedure, and evaluator.

**Evaluation proof。** `3.3 Validation Results and the 80-Instance Scale; 4 Experimental Setup; 5 Results`；exact-v1 披露：Claw-SWE-Bench therefore treats harness and cost accounting as first-class axes of SWE-style coding-agent evaluation, providing both a full benchmark and a low-cost reference set for reproducible comparison.

**Limitations / non-proof。** `7 Conclusion and Discussion`；General-purpose agents such as OpenClaw are increasingly used as autonomous tool users, but their coding ability is difficult to measure under SWE-bench: a generic agent does not by itself satisfy the clean Docker workspace, patch, and prediction contract required for scoring. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [On Subquadratic Architectures: From Applications to Principles](https://arxiv.org/html/2606.12364v1)

**问题与机制。** 原筛选把《On Subquadratic Architectures: From Applications to Principles》关闭或降池；完整摘要显示“To explain xLSTM's advantage, we present a unified formulation and analyze the underlying architectural mechanisms, focusing on state tracking and memory dynamics.”。该增量直接改变 MODEL-LONG-CONTEXT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Analysis of Leading Subquadratic Attention Architectures`；可采用的最小机制命题是：To explain xLSTM's advantage, we present a unified formulation and analyze the underlying architectural mechanisms, focusing on state tracking and memory dynamics.

**Evaluation proof。** `2 Experiments with Complex Dependencies; 4 Experiments on Accumulation and State Tracking; Appendix B Code-focused Language Model Pre-training Results`；exact-v1 披露：We evaluate these models on tasks with complex dependencies: (1) code-model pre-training, (2) distillation of code models from large language models, and (3) pre-training of time-series foundation models.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Overall, our findings indicate that xLSTM's gains on complex tasks stem from robust state tracking and accumulation. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `MODEL-LONG-CONTEXT` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-02-model/22-long-context.md`，Review notes 前正文锚点 `方案究竟移动了哪个瓶颈` 已承载长期命题；source 仅作受限证据。

### [Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling](https://arxiv.org/html/2606.12370v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：RL rollout acceleration 中 MTP acceptance 受 policy entropy 与 draft mismatch 联合约束；rejection sampling 与 TV objective 比 target-only 接受对 policy update 更平滑。

**State / data / control owner。** `INFER-SPECULATIVE-DECODING` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12370v1 §6 Experiments` 支持 `RL math/reasoning workloads and MTP acceptance/throughput sweeps`；模型 `Multiple MTP-enabled LLM scales`；硬件 `Disclosed in experimental appendix`；精度 `Disclosed in experimental appendix`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12370v1 §§3–5 entropy bound, TV loss and adaptation`；counterevidence locator：`arXiv:2606.12370v1 §7.8 top-k instability; §9 Limitations`。

**Trade-off / failure / coexistence / evolution。** 更新 MTP 提升 rollout throughput 却增加训练耦合；top-k TV 不稳，完整 rejection sampling 是 correctness fallback；TRAIN-RLHF 只消费 rollout throughput 与 policy-update handoff。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12370:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12370v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12370:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/48-speculative-decoding.md`，Review notes 前正文锚点 `Correctness owner 没有改变` 已承载长期命题；source 仅作受限证据。

### [Verifiable Environments Are LEGO Bricks: Recursive Composition for Reasoning Generalization](https://arxiv.org/html/2606.12373v1)

**问题与机制。** 原筛选把《Verifiable Environments Are LEGO Bricks: Recursive Composition for Reasoning Generalization》关闭或降池；完整摘要显示“While prior research demonstrates that scaling environment quantity improves RL performance, existing manual or individual construction methods suffer from linear scaling limits, thereby hindering scalable reasoning generalization.”。该增量直接改变 TRAIN-DATA 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method`；可采用的最小机制命题是：While prior research demonstrates that scaling environment quantity improves RL performance, existing manual or individual construction methods suffer from linear scaling limits, thereby hindering scalable reasoning generalization.

**Evaluation proof。** `4 Experiments; 4.1 Experimental Setup; 4.2 Main Results`；exact-v1 披露：Extensive experiments show that RL training on these composite environments consistently enhances reasoning generalization.

**Limitations / non-proof。** `Appendix A Limitations`；Moreover, RACES achieves performance comparable to training on 300 individual environments using only 50 base environments, demonstrating significant efficiency in environment utilization. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-DATA` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-04-training-system/27-data.md`，Review notes 前正文锚点 `可验证环境可以组合，但组合器不拥有正确性` 已完成写入并通过独立 post-write audit。

### [APPO: Agentic Procedural Policy Optimization](https://arxiv.org/html/2606.12384v1)

**问题与机制。** 原筛选把《APPO: Agentic Procedural Policy Optimization》关闭或降池；完整摘要显示“Motivated by these observations, we propose \textbf{Agentic Procedural Policy Optimization (APPO)}, which shifts branching and credit assignment from coarse interaction units to fine-grained decision points in the sequence.”。该增量直接改变 TRAIN-GRPO 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：Motivated by these observations, we propose \textbf{Agentic Procedural Policy Optimization (APPO)}, which shifts branching and credit assignment from coarse interaction units to fine-grained decision points in the sequence.

**Evaluation proof。** `4 Experiments; 4.1 Experiment Setup; 4.2 Main Results`；exact-v1 披露：Experiments on 13 benchmarks show that APPO consistently improves strong agentic RL baselines by nearly 4 points, while keeping efficient tool-calls and maintaining behavior interpretability.

**Limitations / non-proof。** `Appendix G Limitations`；Our pilot analysis shows that influential decision points are broadly distributed throughout the generated sequence rather than concentrated at tool calls, while token entropy alone does not reliably reflect their impact on final outcomes. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-GRPO` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/33-grpo.md`，Review notes 前正文锚点 `从一个终局标量到 Typed Credit：Reward 必须匹配决策边界` 已承载长期命题；source 仅作受限证据。

### [Doc-to-Atom: Learning to Compile and Compose Memory Atoms](https://arxiv.org/html/2606.12400v1)

**问题与机制。** 原筛选把《Doc-to-Atom: Learning to Compile and Compose Memory Atoms》关闭或降池；完整摘要显示“To address these challenges, we propose Doc-to-Atom (Doc2Atom), a compositional parametric memory framework that decomposes each document into semantically typed knowledge atoms.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method; 3.2 Compositional Memory Framework`；可采用的最小机制命题是：To address these challenges, we propose Doc-to-Atom (Doc2Atom), a compositional parametric memory framework that decomposes each document into semantically typed knowledge atoms.

**Evaluation proof。** `4 Experiments; 4.1 Experimental Setup; 4.2 Main Results`；exact-v1 披露：Experiments on six diverse QA benchmarks demonstrate that Doc2Atom outperforms Doc-to-LoRA baselines while reducing the memory cost of document internalization.

**Limitations / non-proof。** `Limitations`；However, producing a single monolithic adapter for all queries leads to irrelevant-query interference, limited compositional recall, and poor scalability to long-document reasoning. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MEMORY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `个性化更新与事实可靠性是两套策略` 已完成写入并通过独立 post-write audit。

### Books / semantic audit

`Integrate=10`，`No Change — Existing Coverage=40`，`Only report=2`，另有 2 项经独立准入复核改为分母前关闭。作者侧 proposal 与独立 Gate 的最终覆盖清单见 [`v3-independent-candidate-books-gate-20260911.json`](../_sources/daily-20260611/v3-independent-candidate-books-gate-20260911.json)；独立写后结果见 [`v3-independent-post-write-audit-20260911.json`](../_sources/daily-20260611/v3-independent-post-write-audit-20260911.json)。`books_removal_queue=0`，7 条 trace 日期修正均已完成并复验，remaining queue=`0`。

## 5. 缺口与下一步

无普通可执行待办；候选必要/Books、行政终存、机器检查和非作者唯一DAY均已完成。以下均是终态保留项，不支持正面证据、Books采用、全网无遗漏或性能/安全保证，材料后来到达只定点重开：

- 来源目录：Google Publications与Meta/FAIR历史Jun10日级目录未恢复；Moonshot Platform Blog可见最后2025-11-07，org 42repo的更新时间不是2026发布证据。实际入口/尝试与停止见[来源记录](../_sources/daily-20260611/SUP_SOURCE_CHECK_20261026.md)。需原机构历史目录/归档或具名正文及公开日期，不能由Blog或搜索无结果推零；本轮约定有限入口已穷尽，不继续全站搜索。
- 日期五项：[2606.10932v1](https://arxiv.org/abs/2606.10932v1)合法界Apr29–Jun10、[2606.09951v1](https://arxiv.org/abs/2606.09951v1)、[2606.09932v1](https://arxiv.org/abs/2606.09932v1)、[2606.09962v1](https://arxiv.org/abs/2606.09962v1)均Jun09–10、[2606.09864v1](https://arxiv.org/abs/2606.09864v1)Jun02–10仍跨BJT日；同DOI原登记与唯一v1上下界见来源记录。未列当窗确定候选、未评分或Books；需官方日公告或更窄且合法的公开正文上界，不截取目标日、不使用created或提交日代公开日，不无限追假想早稿。
- 中心争议：[PiSO10890v1](https://arxiv.org/html/2606.10890v1)C9/C10任意实权重下负w/ties-up未取到全局最小的反例；[10089v1](https://arxiv.org/html/2606.10089v1)C1/F1取球半径未验几何域、F2采样桥需uniform Lipschitz而原线性schedule不满足；[10937v1](https://arxiv.org/html/2606.10937v1)完整R不含需要后继pair、未定义value quotient/weak matching。三项均原6分保留，只中心正面采用H/Books暂缓，不把局部反例外推其余独立结果。原件/反例/重开点见[必要A6/A12/A15](../_sources/daily-20260611/SUP_NECESSARY_20261026.md)及[唯一review§14/25/36](../_sources/daily-20260611/SUP_REVIEW_20261026.md)；需精确修订的假设/证明/反例修补及独立核验后重开，不写通用Books警句。

窗外恢复线索：[Google Jun10 unlearning Blog所指2601.19755v1](https://arxiv.org/abs/2601.19755v1)同DOI登记为Jan28 03:11:01Z，与唯一Jan27v1联合已早于本窗；Blog只介绍同框架，无具名Jun10新增实验/修订。仅留真实Jan28研究线索，未处理其完整研究、不称已审重复、不扩本日报或January。10747已有限核Jun6口头talk、没有更早正文证，当前只采用Jun10 arXiv正文事件，不称全球首传播。

本轮实际写入21个唯一owner文件（逐项位置在§3/§4）：Ch14/16/18/22/23/24、27/29/30/31/32/33/36、48/49/66、75/76/77/78/82。所有37条新增均正文在真实H2 Review notes前，原唯一稿/直接完整两侧/本人注已经非writer实际POST，精确窄位全释放。未改共享State/索引或其他日期；保护并发2025/Jun12及既有staged/unstaged/untracked，不stage/unstage/commit/push。本日行政截断已按本日原HEAD/index同blob恢复旧尾；补查前档案只规范行尾展示空格、旧字段与全部证据不变，最终另逐字核旧52行和完整旧§4。

## 6. 复核

复核者：非writer `jun11_review`，复用root canonical§1–14的实际准入/Source/PRE/POST有效层；§15起余项与唯一DAY由reader负责，root不第三Methods。

结论：通过

唯一完整[DAY §101](../_sources/daily-20260611/SUP_REVIEW_20261026.md#101-jun11补查唯一完整日级验收day通过安全终态)已真实保存，作者仅据既成事实行政同步，不自签或添加第三研究/复核。

实际复核：首批6个完整题摘（4潜候选及10706/10381两具体N），B2–B5每批12个完整题摘，共54项AB校准=39候选+14具体N+10932日期隔离；再加MiMo/Gemma两官方核心和10089单篇题摘/合法日期为42候选。入口、有限主题和停止点按canonical§1/5/9/12/19/20复用；宽1361导航和旧562未全量重审，不把分层抽检称全量验证。全部42拟入选的必要证据/Books判断均已逐项独核，37实际整合、2具体已有覆盖、3中心争议隔离；实际POST见canonical各节，最新末四为§97–100。理论纠错、GPT2 constrained local近Full反侧、baseline人口/全费等具体修正已经落必要与正文，不照录宣传性保证。

旧轮有效审核（仅旧52/原小时窗）：Candidate/Books Gate `/root/june_11_12_independent_gate`、postwrite `/root/june_11_12_postwrite` 与 `june_11_20_recert` 的既成范围复用，完整原声明见[补查前档案](../_sources/daily-20260611/baseline-before-supplement-20261026.md)，不代本轮Coverage或DAY。机器V3、Markdown/191本地引用目标（含最终新增的两处DAY链接）、94候选与同名同URL证据、旧52完整行/whole旧§4保护与报告/本日sources/21owner限定diffcheck均实际通过；格式检查不替上述唯一语义独核。
