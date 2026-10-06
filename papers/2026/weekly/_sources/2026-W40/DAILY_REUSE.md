# W40 Daily 复用与身份归并

仅机械归并已完成Daily的身份、日期与有效审阅/Books结果；不重扫日级来源，不将机器归并称语义复核。七份窗口连续覆盖Sep27 09→Oct4 09。10/04已由root非作者复核通过（本次重读终态）。

- papers/2026/09/28/README.md：2026-09-27T09:00:00+08:00 ～ 2026-09-28T09:00:00+08:00；59 行。Daily状态以实际README终态为准。
- papers/2026/09/29/README.md：2026-09-28T09:00:00+08:00 ～ 2026-09-29T09:00:00+08:00；43 行。Daily状态以实际README终态为准。
- papers/2026/09/30/README.md：2026-09-29T09:00:00+08:00 ～ 2026-09-30T09:00:00+08:00；42 行。Daily状态以实际README终态为准。
- papers/2026/10/01/README.md：2026-09-30T09:00:00+08:00 ～ 2026-10-01T09:00:00+08:00；21 行。Daily状态以实际README终态为准。
- papers/2026/10/02/README.md：2026-10-01T09:00:00+08:00 ～ 2026-10-02T09:00:00+08:00；2 行。Daily状态以实际README终态为准。
- papers/2026/10/03/README.md：2026-10-02T09:00:00+08:00 ～ 2026-10-03T09:00:00+08:00；0 行。Daily状态以实际README终态为准。
- papers/2026/10/04/README.md：2026-10-03T09:00:00+08:00 ～ 2026-10-04T09:00:00+08:00；3 行。Daily状态以实际README终态为准。

七日报表170行，arXiv按ID忽略版本，官方项目按规范URL归并；OpenAgentCore两行归并为一个项目家族，其0.0.3/0.0.4与0.0.7/0.0.8/0.0.9为不同发布事件且均保留。结果169唯一家族；未发现论文ID重复。周源8家族无同身份碰撞，合计177（包括CodeJudge中心争议终态保留1，不把它算正面Evidence）。

## arxiv:2609.31600

- Daily：papers/2026/09/28/README.md
- 事件/判断：[New LoRA Skills Should Read but Never Write](https://arxiv.org/abs/2609.31600v1) / 2026-09-28T08:00:00+08:00 / Gauge坐标与单向block权限区分旧参数项与总函数；2+2+2=6 / 深入完成 / 整合：TRAIN-LORA [Ch30](../../../../../books/part-04-training-system/30-lora.md)，Fed gauge后两段；仅有条件composition

## arxiv:2609.31415

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Evaluating the accuracy of KV cache reuse techniques](https://arxiv.org/abs/2609.31415v1) / 2026-09-28T08:00:00+08:00 / Baseline条件评价与warmup角色反事实修正reuse验收；3+2+2=7 / 深入完成 / 整合：INFER-KV-CACHE [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，PatchKV后两段

## arxiv:2609.31560

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Generalization behavior of OPTQ and the role of regularization](https://arxiv.org/abs/2609.31560v1) / 2026-09-28T08:00:00+08:00 / 校准→population泛化的独立概率/正则条件；2+1+3=6 / 深入完成 / 整合：INFER-TENSORRT-LLM [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)，weighted-cover后两段

## arxiv:2609.30738

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Beyond Mean Attention: Diversity-Aware, Layer-Wise Scoring for KV Cache Eviction](https://arxiv.org/abs/2609.30738v1) / 2026-09-28T08:00:00+08:00 / 构建集合的冗余排序与depth profile非普适收益；2+1+2=5 / 深入完成 / 整合：INFER-KV-CACHE [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，TwinKV后两段

## arxiv:2609.31551

- Daily：papers/2026/09/28/README.md
- 事件/判断：[EAServe: Encode-Aware Disaggregated Serving for Multimodal Large Language Models](https://arxiv.org/abs/2609.31551v1) / 2026-09-28T08:00:00+08:00 / Encode批等待/SM共驻与分流联动，但吞吐目标不同于SLO goodput；2+2+2=6 / 深入完成 / 整合：INFER-PD-DISAGGREGATION [Ch55](../../../../../books/part-05-inference-system/55-pd-disaggregation.md)，goodput→KV transfer两段

## arxiv:2609.31395

- Daily：papers/2026/09/28/README.md
- 事件/判断：[ActKV: Efficient LLM Agents through Action-Guided KV Cache Management](https://arxiv.org/abs/2609.31395v1) / 2026-09-28T08:00:00+08:00 / Action访问历史与round末预算/无冲突原位压缩；2+2+2=6 / 深入完成 / 整合：INFER-KV-CACHE [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，LoopGuard后两段

## arxiv:2609.30884

- Daily：papers/2026/09/28/README.md
- 事件/判断：[CacheReforge: Bounded Recovery for Stale KV Caches under Evolving Adapters](https://arxiv.org/abs/2609.30884v1) / 2026-09-28T08:00:00+08:00 / 逐层参数anchor/位移及可执行restart与tail证书分权；2+2+2=6 / 深入完成 / 整合：INFER-KV-CACHE [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，21362 seam后两段

## arxiv:2609.30820

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Quantizing Looped Transformers: Feedback Exposure and Calibration Blindness](https://arxiv.org/abs/2609.30820v1) / 2026-09-28T08:00:00+08:00 / Loop-entry反馈位置与跨step Hessian覆盖是不同精度轴；3+1+2=6 / 深入完成 / 整合：INFER-TENSORRT-LLM [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)，OPTQ→PTQ两段

## arxiv:2609.30950

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Low-Bit Recurrent States in Hybrid Language Models](https://arxiv.org/abs/2609.30950v1) / 2026-09-28T08:00:00+08:00 / 误差存活/readout方向与range共同限制state位宽代理；2+1+2=5 / 深入完成 / 整合：INFER-TENSORRT-LLM [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)，Fractional末两段

## arxiv:2609.31291

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Softmax Reparameterization for Output-Head Quantization](https://arxiv.org/abs/2609.31291v1) / 2026-09-28T08:00:00+08:00 / 公共row shift等价与量化/非线性修正的权限不同；2+1+2=5 / 深入完成 / 整合：INFER-TENSORRT-LLM [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)，Greedy→ExactTopK两段

## arxiv:2609.31250

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Deterministic Regime Switching and Feasibility Inversion in Dynamic Tensor Rematerialization](https://arxiv.org/abs/2609.31250v1) / 2026-09-28T08:00:00+08:00 / 重复eviction与pinned frontier使在线budget可非单调；3+1+2=6 / 深入完成 / 整合：TRAIN-PRETRAINING [Ch28](../../../../../books/part-04-training-system/28-pretraining.md)，activation保存/重算末两段

## arxiv:2609.31093

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Block Sparse Attention with Log-Linear Complexity](https://arxiv.org/abs/2609.31093v1) / 2026-09-28T08:00:00+08:00 / 分层候选routing降低selector扫描但ancestor漏选不由leaf精确修复；2+1+2=5 / 深入完成 / 整合：MODEL-LONG-CONTEXT [Ch22](../../../../../books/part-02-model/22-long-context.md)，MiniMax sparse→selector forward两段

## arxiv:2609.31114

- Daily：papers/2026/09/28/README.md
- 事件/判断：[From Shortcut Learning to Discrete Neural Insertion Sort](https://arxiv.org/abs/2609.31114v1) / 2026-09-28T08:00:00+08:00 / 最终正确与逐步算法执行不同，discrete control仍需全局终止监督；2+1+3=6 / 深入完成 / 整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，25800→训练标准两段

## arxiv:2609.31589

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Common-Mode Collapse and Recovery in Direct Feedback Alignment](https://arxiv.org/abs/2609.31589v1) / 2026-09-28T08:00:00+08:00 / 共享mean teaching低秩驱动与readout/optimizer的非单调collapse；2+1+3=6 / 深入完成 / 整合：TRAIN-PRETRAINING [Ch28](../../../../../books/part-04-training-system/28-pretraining.md)，01563→depth parameterization两段

## arxiv:2609.31564

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Weight Pair Encoding: Inducing a Smaller Grammar in Neural Network Weights](https://arxiv.org/abs/2609.31564v1) / 2026-09-28T08:00:00+08:00 / 训练code-domain重复语法是独立压缩轴，不等kernel或位宽收益；2+1+2=5 / 深入完成 / 整合：INFER-TENSORRT-LLM [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)，PTQ/QAT定义→W4A16两段

## arxiv:2609.31401

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Decodable In-Context State and Model Output Across Training](https://arxiv.org/abs/2609.31401v1) / 2026-09-28T08:00:00+08:00 / logits与argmax分权否证probe对错差直接等于信息丢失；3+1+3=7 / 深入完成 / 整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，独立reader→encoder移植两段

## arxiv:2609.31098

- Daily：papers/2026/09/28/README.md
- 事件/判断：[The Residual Stream's Effective Depth](https://arxiv.org/abs/2609.31098v1) / 2026-09-28T08:00:00+08:00 / 累积state几何需matched参照，不是无用层或pruning许可；3+1+2=6 / 深入完成 / 整合：MODEL-TRANSFORMER-LAYER [Ch17](../../../../../books/part-02-model/17-transformer-layer.md)，分别检验→逐层替换两段

## arxiv:2609.30546

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Convergence guarantees for Muon: New parameter regimes and generalizations](https://arxiv.org/abs/2609.30546v1) / 2026-09-28T08:00:00+08:00 / 有限NS、ideal sign与soft-sign代理的轨迹保证权限分开；2+1+3=6 / 深入完成 / 整合：TRAIN-PRETRAINING [Ch28](../../../../../books/part-04-training-system/28-pretraining.md)，18999→多Optimizer两段

## arxiv:2609.31261

- Daily：papers/2026/09/28/README.md
- 事件/判断：[MoSAR: Mixture of Semantic Attention Regimes for Learning Adaptive and Approximable Attention Geometries](https://arxiv.org/abs/2609.31261v1) / 2026-09-28T08:00:00+08:00 / pair geometry、top1、hard tail及kernel是不同变化；2+1+2=5 / 深入完成 / 整合：MODEL-LONG-CONTEXT [Ch22](../../../../../books/part-02-model/22-long-context.md)，13141→无法重训Target两段

## arxiv:2609.31009

- Daily：papers/2026/09/28/README.md
- 事件/判断：[G$^2$PTQ: Improving LLM Post-Training Quantization with Generalized Gradient Compensation](https://arxiv.org/abs/2609.31009v1) / 2026-09-28T08:00:00+08:00 / partial-quantized block刷新梯度/曲率与估计预算一阶补偿；2+1+2=5 / 深入完成 / 整合：INFER-TENSORRT-LLM [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)，LoopPTQ→PTQ/QAT两段

## arxiv:2609.31458

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Nonparametric In-Context Learning under Growing Geometric Complexity: Minimax Optimality and Local Geometry-Adaptivity of Transformers](https://arxiv.org/abs/2609.31458v1) / 2026-09-28T08:00:00+08:00 / geometry-first comparator与prompt样本/训练任务双预算权限；2+1+3=6 / 深入完成 / 整合：WORLDVIEW-LLM-INTELLIGENCE [Ch8](../../../../../books/part-01-worldview/08-why-llms-show-intelligence.md)，context质量state→Post-training两段

## arxiv:2609.31181

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Where a Model Sends Its Own Repeated Token](https://arxiv.org/abs/2609.31181v1) / 2026-09-28T08:00:00+08:00 / fixedpoint集合cardinality反证与source-paired destination/null/precision floor；3+1+2=6 / 深入完成 / 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，subject身份→adapter例子两段

## arxiv:2609.31342

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Stale-Document Poisoning: When Outdated Retrieval Overrides Correct Model Answers](https://arxiv.org/abs/2609.31342v1) / 2026-09-28T08:00:00+08:00 / metadata存在不等reader遵守有效期，RAG纠正与损坏须双侧评价；3+2+2=7 / 深入完成 / 整合：AGENT-RAG [Ch76](../../../../../books/part-07-agent/76-rag.md)，Temporal旧binding→权威后继两段

## arxiv:2609.31301

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Beyond Approved Actions: Runtime Validation of Persistent Outcomes in Agent Workflows](https://arxiv.org/abs/2609.31301v1) / 2026-09-28T08:00:00+08:00 / effect profile、同candidate equality与backend capability分权；2+2+2=6 / 深入完成 / 整合：AGENT-PLATFORM [Ch84](../../../../../books/part-07-agent/84-agent-platform.md)，LIBOS旧binding→Discovery两段

## arxiv:2609.30935

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Estimating and Orthogonalizing Unknown Pre-training Gradients for Continual Fine-tuning of Large Language Models](https://arxiv.org/abs/2609.30935v1) / 2026-09-28T08:00:00+08:00 / 虚拟更新搜索synthetic保护gradient与有限步/coverage权限分离；2+1+2=5 / 深入完成 / 整合：TRAIN-SFT [Ch29](../../../../../books/part-04-training-system/29-sft.md)，14010→EmbeddingNoise两段

## arxiv:2609.30837

- Daily：papers/2026/09/28/README.md
- 事件/判断：[MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2609.30837v1) / 2026-09-28T08:00:00+08:00 / base-relative专长方向与student教学方向的token级筛选/权重分权；2+1+2=5 / 深入完成 / 整合：TRAIN-SFT [Ch29](../../../../../books/part-04-training-system/29-sft.md)，debate→Self-distillation两段

## arxiv:2609.30864

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Persistent Negatives for Adversarial Black-Box On-Policy Distillation](https://arxiv.org/abs/2609.30864v1) / 2026-09-28T08:00:00+08:00 / 历史完整比较仅训练RM，fresh groups仍唯一进入policy update；2+1+2=5 / 深入完成 / 整合：TRAIN-SFT [Ch29](../../../../../books/part-04-training-system/29-sft.md)，14071→混合Occupancy两段

## arxiv:2609.30652

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Recursive Self-Improvement via On-Policy Distillation for Reasoning](https://arxiv.org/abs/2609.30652v1) / 2026-09-28T08:00:00+08:00 / 特权guidance与无gold改写的独立CE/admission分支；2+1+2=5 / 深入完成 / 整合：TRAIN-SFT [Ch29](../../../../../books/part-04-training-system/29-sft.md)，ContextDistillation成本→carrier两段

## arxiv:2609.30878

- Daily：papers/2026/09/28/README.md
- 事件/判断：[TISD: On-Policy Self-Distillation with Trajectory Intervention](https://arxiv.org/abs/2609.30878v1) / 2026-09-28T08:00:00+08:00 / teacher一次branch提案后由student采新suffix、原反馈监督新状态；2+1+2=5 / 深入完成 / 整合：TRAIN-SFT [Ch29](../../../../../books/part-04-training-system/29-sft.md)，privileged evidence→ContextDistillation两段

## arxiv:2609.31382

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Highlight-Then-Summarize: Learning to Compress Evidence for Long-Context Understanding](https://arxiv.org/abs/2609.31382v1) / 2026-09-28T08:00:00+08:00 / E/S/A分开训练及预算反转限定过程目标；2+1+2=5 / 标准完成 / 仅报告：局部layout/harmonic奖励与参数—质量frontier，无一般aggregation因果或新通用知识缺口

## arxiv:2609.30572

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Entropy Regularization: A Free Correction to Cross-Entropy for Verified Demonstrations](https://arxiv.org/abs/2609.30572v1) / 2026-09-28T08:00:00+08:00 / 演示likelihood、采样分布正确集合与token entropy proxy分权；2+1+3=6 / 深入完成 / 整合：TRAIN-SFT [Ch29](../../../../../books/part-04-training-system/29-sft.md)，masked CE→loss-mask示例两段

## arxiv:2609.31448

- Daily：papers/2026/09/28/README.md
- 事件/判断：[ViSTA: A Simple Bridge Extends Visual Alignment to Clinical Time-Series Understanding in Multimodal LLMs](https://arxiv.org/abs/2609.31448v1) / 2026-09-28T08:00:00+08:00 / 内部变量summary与原visual token残差桥的局部选择；2+1+2=5 / 标准完成 / 仅报告：同参数桥接口/任务frontier，不外推通用信息保留或临床效力

## arxiv:2609.31571

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Strategically Diverse Sampling for Self-Training](https://arxiv.org/abs/2609.31571v1) / 2026-09-28T08:00:00+08:00 / 同题approach预分叉采样与correct过滤/策略覆盖独立；3+1+2=6 / 深入完成 / 整合：TRAIN-DATA [Ch27](../../../../../books/part-04-training-system/27-data.md)，synthetic开头→行为树前两段

## arxiv:2609.31047

- Daily：papers/2026/09/28/README.md
- 事件/判断：[DynBranch: Speculative Subgraph Reuse for Dynamic Agentic LLM Serving](https://arxiv.org/abs/2609.31047v1) / 2026-09-28T08:00:00+08:00 / 未resolve候选的不可见shadow与setup/fill负载准入分开；2+2+2=6 / 深入完成 / 整合：INFER-SCHEDULING [Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md)，Pythia→coldwarmup前两段

## arxiv:2609.31490

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Authority at Commit Time: Reject-and-Rerun Semantics for Governed Agentic Systems](https://arxiv.org/abs/2609.31490v1) / 2026-09-28T08:00:00+08:00 / governing subset与admission/dispatch两时点的权限不同；2+2+2=6 / 深入完成 / 整合：AGENT-PLATFORM [Ch84](../../../../../books/part-07-agent/84-agent-platform.md)，runpin→Feedback两段

## arxiv:2609.30342

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Low-Rank Friction for Memory-Efficient Transformer Pretraining](https://arxiv.org/abs/2609.30342v1) / 2026-09-28T08:00:00+08:00 / 平方momentum形成friction而非平方gradient缩放position；2+1+3=6 / 深入完成 / 整合：TRAIN-PRETRAINING [Ch28](../../../../../books/part-04-training-system/28-pretraining.md)，roleallocation→Embedding两段

## arxiv:2609.31587

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Compact Documentation for Coding Agents: A Benchmark, an Optimizer, and Why It Does Not Transfer](https://arxiv.org/abs/2609.31587v1) / 2026-09-28T08:00:00+08:00 / roundtrip proxy与真实交付、derived handbook与current source分权；3+1+2=6 / 标准完成 / 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)、AGENT-WORKFLOW [Ch81](../../../../../books/part-07-agent/81-workflow.md)；不E整recipe

## arxiv:2609.31563

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Multi-agent Scaling Across Disjunctive and Compensatory Tasks](https://arxiv.org/abs/2609.31563v1) / 2026-09-28T08:00:00+08:00 / conditional-iid与item bias、oracle/plurality/平均的极限不同；3+2+2=7 / 深入完成 / 整合：AGENT-MULTI-AGENT [Ch82](../../../../../books/part-07-agent/82-multi-agent.md)，Peer/Debate→Blackboard两段

## arxiv:2609.31422

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Towards Mitigating Fabricated Consensus: The Active Provenance Gate for Multi-Agent Debate Synthesis](https://arxiv.org/abs/2609.31422v1) / 2026-09-28T08:00:00+08:00 / 闭世界PF句比例/强制共识与实际发布权分开；2+2+2=6 / 标准完成 / 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)、AGENT-WORKFLOW [Ch81](../../../../../books/part-07-agent/81-workflow.md)；不E完整recipe

## arxiv:2609.30813

- Daily：papers/2026/09/28/README.md
- 事件/判断：[A Benchmark and Diagnostic Study of Epistemic Admission in Shared Agent Memory](https://arxiv.org/abs/2609.30813v1) / 2026-09-28T08:00:00+08:00 / lineage/truth分轴、assertion≠citation、写入/暴露/采纳三事件；3+2+2=7 / 深入完成 / 整合：AGENT-MEMORY [Ch77](../../../../../books/part-07-agent/77-memory.md)，SelfStore→LateConstruction两段

## arxiv:2609.30289

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Not All Memories Are Equal: Hierarchical Collaborative Memory for Validity-Aware Retrieval in LLM Agents](https://arxiv.org/abs/2609.30289v1) / 2026-09-28T08:00:00+08:00 / 学习current/history两级维护与soft validity重排，不等valid-only gate；2+1+2=5 / 标准完成 / 仅报告：局部维护/soft-rank recipe，不改变授权、有效期与并发通用合同

## arxiv:2609.30293

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Cartograph: Federated Tool Discovery with Operator-Attested Retrieval for AI Agents](https://arxiv.org/abs/2609.30293v1) / 2026-09-28T08:00:00+08:00 / operator签文本与派生embedding分权、粗server召回决定tool shortlist；2+2+2=6 / 深入完成 / 整合：AGENT-MCP [Ch83](../../../../../books/part-07-agent/83-mcp.md)，ToolDescription→组合Admission两段

## arxiv:2609.30328

- Daily：papers/2026/09/28/README.md
- 事件/判断：[When Is a Multi-Agent Code Judge Actually Grounded? Two Label-Free Measurements, and a Judge That Declines to Guess](https://arxiv.org/abs/2609.30328v1) / 2026-09-28T08:00:00+08:00 / question相同不认证候选证据/verification output不可区分；3+1+3=7 / 争议 / 暂缓：printed无区分力充分性隔离，有限经验gate与coverage保留

## arxiv:2609.31620

- Daily：papers/2026/09/28/README.md
- 事件/判断：[FuseReg: Regularizing Layer Fusion Mitigates the Reconstruction-Generation Gap in Representation Autoencoders](https://arxiv.org/abs/2609.31620v1) / 2026-09-28T08:00:00+08:00 / 随机nonempty layermean及decoder/DiT两个率与目标分开；2+1+2=5 / 深入完成 / 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，RepresentationArtifact→Fusion两段

## arxiv:2609.31349

- Daily：papers/2026/09/28/README.md
- 事件/判断：[DyMD: Preserving Interaction Dynamics through Distribution Matching Distillation in Few-Step Video World Models](https://arxiv.org/abs/2609.31349v1) / 2026-09-28T08:00:00+08:00 / teacher状态支持与critic拟合困难的表示/预算分权；3+1+2=6 / 深入完成 / 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，reward-target→09536前两段

## arxiv:2609.30996

- Daily：papers/2026/09/28/README.md
- 事件/判断：[The Linear Representation Hypothesis for Vision-Language-Action Models](https://arxiv.org/abs/2609.30996v1) / 2026-09-28T08:00:00+08:00 / propagatedQoI线性probe存在与policy自然参数steering条件分开；2+1+3=6 / 深入完成 / 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，Actionchunk→Trajectory前两段

## arxiv:2609.30946

- Daily：papers/2026/09/28/README.md
- 事件/判断：[OneWorld: Learning Consistent Physics Across Actions in World Models](https://arxiv.org/abs/2609.30946v1) / 2026-09-28T08:00:00+08:00 / 共同mechanism posterior支持与个体/共享fit/gap分开；3+1+2=6 / 深入完成 / 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，common-reset→action-recovery两段

## arxiv:2609.30595

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Action Forcing: Training World Models on Unsupervised Video by Recovering Underlying Egomotion Bases](https://arxiv.org/abs/2609.30595v1) / 2026-09-28T08:00:00+08:00 / 数据PCA零点与noop、teacher输出label与generator真实target分权；3+2+2=7 / 深入完成 / 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，inverse20104→GUI两段

## arxiv:2609.31394

- Daily：papers/2026/09/28/README.md
- 事件/判断：[InternW0-$\Delta$: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data](https://arxiv.org/abs/2609.31394v1) / 2026-09-28T08:00:00+08:00 / 部署change表示与两future监督/4D删除分权，mask才授contextKV复用；2+2+2=6 / 深入完成 / 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，PFD→ActionRepresentation两段

## arxiv:2609.31048

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Kintsugi-VLA: Turning Failed Robot Rollouts into Recovery Data through Interventional Recoverability](https://arxiv.org/abs/2609.31048v1) / 2026-09-28T08:00:00+08:00 / expert-relative非单调恢复与observedterminalfrontier/采样预算分权；3+2+2=7 / 深入完成 / 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，OfflineFailure→EvaluationLadder两段

## arxiv:2609.31619

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Learning to Stop without Learning to Stop: Self-Supervised Confidence Training Improves Reasoning Efficiency](https://arxiv.org/abs/2609.31619v1) / 2026-09-28T08:00:00+08:00 / 自监督概率标签改变效率但不同于可靠停止/校准；2+1+2=5 / 标准完成 / 仅报告：限定训练recipe经验，未确立通用stopping机制；任务质量反退保留

## arxiv:2609.31430

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Compress What You See, Not What You Say: Anchored Context Distillation for Latent-Observation Software Engineering Agents](https://arxiv.org/abs/2609.31430v1) / 2026-09-28T08:00:00+08:00 / 双view独立behavior anchor与表示迁移cache成本；2+2+2=6 / 深入完成 / 整合：AGENT-CONTEXT [Ch75](../../../../../books/part-07-agent/75-context.md)，POINTS后两段

## arxiv:2609.31381

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Completed Pairs Hide Capped Failures: A ReVerPi Case Study of Selective Context Projection](https://arxiv.org/abs/2609.31381v1) / 2026-09-28T08:00:00+08:00 / 成对观测机会依赖first-arm完成造成zero positivity与有限识别；3+2+2=7 / 深入完成 / 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，ResponseRate后两段

## arxiv:2609.31214

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Which Influence Are We Estimating? The Role of Counterfactual Specifications in Data Attribution](https://arxiv.org/abs/2609.31214v1) / 2026-09-28T08:00:00+08:00 / 先声明B/P/T估计目标，再用匹配reference检近似误差；3+1+3=7 / 深入完成 / 整合：TRAIN-DATA [Ch27](../../../../../books/part-04-training-system/27-data.md)，SAE attribution后两段

## arxiv:2609.31121

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning](https://arxiv.org/abs/2609.31121v1) / 2026-09-28T08:00:00+08:00 / 完整可读推理也可操纵monitor framing，paraphrase恢复有损；3+2+2=7 / 深入完成 / 整合：PLATFORM-SECURITY [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)，CoT score→runtime前两段

## arxiv:2609.30383

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Stealth Apart, Harm Together: Skill Cascading Attacks on Skill-Based Agent Systems](https://arxiv.org/abs/2609.30383v1) / 2026-09-28T08:00:00+08:00 / 多个declared-capability内变换串联消关键signal，commitment审计不同于concat扫描；3+2+2=7 / 深入完成 / 整合：PLATFORM-SECURITY [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)，Skill描述后两段

## arxiv:2609.30325

- Daily：papers/2026/09/28/README.md
- 事件/判断：[ScopeBench: Do Agents Preserve Engagement Boundaries Under Goal Pressure?](https://arxiv.org/abs/2609.30325v1) / 2026-09-28T08:00:00+08:00 / 无合法路径时机械成功floor与failed-stratum过程judge分权；3+2+2=7 / 深入完成 / 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，adaptive profile后两段

## arxiv:2609.30657

- Daily：papers/2026/09/28/README.md
- 事件/判断：[Prompt Injection Detection for Email Agents Through Attack Chain Modeling](https://arxiv.org/abs/2609.30657v1) / 2026-09-28T08:00:00+08:00 / 阶段预测前提/条件分母与实际receipt及policy operatingpoint分权；2+2+2=6 / 深入完成 / 整合：PLATFORM-SECURITY [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)，Containment末两段

## arxiv:2609.30634

- Daily：papers/2026/09/28/README.md
- 事件/判断：[In-Context Binding Capacity in Language Models](https://arxiv.org/abs/2609.30634v1) / 2026-09-28T08:00:00+08:00 / own-ceiling归一化容量不能代替absolute task requirement与实测可行集；2+1+3=6 / 深入完成 / 整合：MODEL-LONG-CONTEXT [Ch22](../../../../../books/part-02-model/22-long-context.md)，eval slices后两段

## arxiv:2609.35481

- Daily：papers/2026/09/29/README.md
- 事件/判断：[TopoEP 2609.35481v1](https://arxiv.org/abs/2609.35481v1) / 2026-09-29T08:00:00+08:00 / 共享矩阵确定deviceplan与两级topology成本门；2+2+3=7 / 深入完成 / 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md)，MoonEP→Cobalt，两段实际写后root通过

## arxiv:2609.35263

- Daily：papers/2026/09/29/README.md
- 事件/判断：[WavePP 2609.35263v1](https://arxiv.org/abs/2609.35263v1) / 2026-09-29T08:00:00+08:00 / all-stage endpoint租约与suffix backing先commit、延后materialize；2+2+3=7 / 深入完成 / 整合：`INFER-KV-CACHE` [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，05219→retention，两段实际写后root通过

## arxiv:2609.35065

- Daily：papers/2026/09/29/README.md
- 事件/判断：[TempoKV 2609.35065v1](https://arxiv.org/abs/2609.35065v1) / 2026-09-29T08:00:00+08:00 / metadata claim与capacity commitment分开，由TTU/TTR共同触发；2+1+3=6 / 深入完成 / 整合：`INFER-KV-CACHE` [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，prefetch23049→CacheScout，两段实际写后root通过

## arxiv:2609.34645

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Nereus 2609.34645v1](https://arxiv.org/abs/2609.34645v1) / 2026-09-29T08:00:00+08:00 / sealed TP/PP replica与跨stage转移DAG，feasibility与payback分权；2+2+3=7 / 深入完成 / 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md)，22614→token balance，两段实际写后root通过

## arxiv:2609.33762

- Daily：papers/2026/09/29/README.md
- 事件/判断：[EfficientAgent 2609.33762v1](https://arxiv.org/abs/2609.33762v1) / 2026-09-29T08:00:00+08:00 / pool working-set压力下host writefilter与大池恢复写全的反向条件；2+1+3=6 / 深入完成 / 整合：`INFER-KV-CACHE` [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，初Eviction→ContextResidency，实际写后root通过

## arxiv:2609.32283

- Daily：papers/2026/09/29/README.md
- 事件/判断：[AgentReplay 2609.32283v1](https://arxiv.org/abs/2609.32283v1) / 2026-09-29T08:00:00+08:00 / 模型正常forward后、nextstate前固定轨迹，logicalroute/tool等待与runtime自由度分开；2+1+3=6 / 深入完成 / 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，Runtime→AgentOutcome，实际写后root通过

## https://openai.com/index/introducing-dots/

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Introducing dots](https://openai.com/index/introducing-dots/) / 2026-09-29T08:00:00+08:00 / 主动只读发现不继承delegated task执行权限；2+2+2=6 / 深入完成 / 整合：`AGENT-PLATFORM` [Ch84](../../../../../books/part-07-agent/84-agent-platform.md)，Omni→Scheduling，实际写后root通过

## https://openai.com/index/towards-safety-cases-for-frontier-ai-training/

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Towards safety cases for frontier AI training](https://openai.com/index/towards-safety-cases-for-frontier-ai-training/) / 2026-09-29T03:00:00+08:00 / 持续case失效暂停covered runs，派生数据/评分恢复与权重rollback分开；3+2+3=8 / 深入完成 / 整合：`PLATFORM-SECURITY` [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)，SafetyEval首两段，实际写后root通过

## https://openai.com/index/how-we-will-do-better-for-australia/

- Daily：papers/2026/09/29/README.md
- 事件/判断：[How we will do better for Australia](https://openai.com/index/how-we-will-do-better-for-australia/) / 2026-09-29T03:00:00+08:00 / 初步受影响方通知不等待最终调查归因，已知/未知分别提交；3+2+2=7 / 深入完成 / 整合：`PLATFORM-SECURITY` [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)，n-days→匿名，两段实际写后root通过

## arxiv:2609.35630

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Read-Blindness 2609.35630v1](https://arxiv.org/abs/2609.35630v1) / 2026-09-29T08:00:00+08:00 / 读敏感、写增量与累积的不同权限；2+1+3=6 / 深入完成 / 整合：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../../books/part-02-model/17-transformer-layer.md)，两段实际写后root通过

## arxiv:2609.35663

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Entity Copy 2609.35663v1](https://arxiv.org/abs/2609.35663v1) / 2026-09-29T08:00:00+08:00 / context参与准备路由不等于原生context读出提供答案；2+1+3=6 / 深入完成 / 整合：`MODEL-SELF-ATTENTION` [Ch14](../../../../../books/part-02-model/14-self-attention.md)，两段实际写后root通过

## arxiv:2609.35646

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Rubric IRT 2609.35646v1](https://arxiv.org/abs/2609.35646v1) / 2026-09-29T08:00:00+08:00 / 条件latent测量与冻结测量器的criterion信息预算；2+1+3=6 / 深入完成 / 整合：`TRAIN-RLHF` [Ch31](../../../../../books/part-04-training-system/31-rlhf.md)，两段实际写后root通过

## arxiv:2609.34386

- Daily：papers/2026/09/29/README.md
- 事件/判断：[SparseOPD 2609.34386v1](https://arxiv.org/abs/2609.34386v1) / 2026-09-29T08:00:00+08:00 / 全correction观察和有符号稀疏head微分分离；2+1+3=6 / 深入完成 / 整合：`TRAIN-SFT` [Ch29](../../../../../books/part-04-training-system/29-sft.md)，两段实际写后root通过

## arxiv:2609.33923

- Daily：papers/2026/09/29/README.md
- 事件/判断：[ProbeQuant 2609.33923v1](https://arxiv.org/abs/2609.33923v1) / 2026-09-29T08:00:00+08:00 / isolated uncertainty、input secondmoment与downstream目标不同权限；2+1+3=6 / 深入完成 / 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)，实际两段root写后通过

## arxiv:2609.33672

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Reset Is Not Recovery 2609.33672v1](https://arxiv.org/abs/2609.33672v1) / 2026-09-29T08:00:00+08:00 / reset事件不等于effectivecontext恢复，以pairedclean核残余影响；2+1+3=6 / 深入完成 / 整合：`AGENT-CONTEXT` [Ch75](../../../../../books/part-07-agent/75-context.md)，实际两段root写后通过

## arxiv:2609.33634

- Daily：papers/2026/09/29/README.md
- 事件/判断：[LLaDA-Guard 2609.33634v1](https://arxiv.org/abs/2609.33634v1) / 2026-09-29T08:00:00+08:00 / labelconditional重构证据域与verdict权限；2+2+2=6 / 深入完成 / 整合：`PLATFORM-SECURITY` [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)，实际两段root写后通过

## arxiv:2609.33335

- Daily：papers/2026/09/29/README.md
- 事件/判断：[World-Model Post-Training Audit 2609.33335v1](https://arxiv.org/abs/2609.33335v1) / 2026-09-29T08:00:00+08:00 / 正确预测内容与额外优化、selection与coverage归因拆开；3+1+3=7 / 深入完成 / 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，实际两段root写后通过

## arxiv:2609.33642

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Perturbed Documents 2609.33642v1](https://arxiv.org/abs/2609.33642v1) / 2026-09-29T08:00:00+08:00 / 同question/rubric的with/without文档双侧admission门；2+1+3=6 / 深入完成 / 整合：`TRAIN-DATA` [Ch27](../../../../../books/part-04-training-system/27-data.md)，实际两段root写后通过

## arxiv:2609.34738

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Event-Set Completion Distillation 2609.34738v1](https://arxiv.org/abs/2609.34738v1) / 2026-09-29T08:00:00+08:00 / 实际child completion集合总概率不同于单token配给；2+1+3=6 / 深入完成 / 整合：`TRAIN-SFT` [Ch29](../../../../../books/part-04-training-system/29-sft.md)，实际两段root写后通过

## arxiv:2609.34657

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Torch-PIM 2609.34657v1](https://arxiv.org/abs/2609.34657v1) / 2026-09-29T08:00:00+08:00 / Lowering 产生的实际 loop nest 决定放置候选域与 host profile 权限；2+1+2=5 / 深入完成 / 整合：`INFER-TENSORRT-LLM` [Ch49 lowering→dequantization](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过

## arxiv:2609.33184

- Daily：papers/2026/09/29/README.md
- 事件/判断：[SpecStream 2609.33184v1](https://arxiv.org/abs/2609.33184v1) / 2026-09-29T08:00:00+08:00 / 仅迁移已提交历史、多 query 流式验证与 target 优先准入；2+2+3=7 / 深入完成 / 整合：`INFER-SPECULATIVE-DECODING` [Ch48 memory-budget→drafter](../../../../../books/part-05-inference-system/48-speculative-decoding.md)；实际正文与非作者写后通过

## arxiv:2609.35366

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Planarian 2609.35366v1](https://arxiv.org/abs/2609.35366v1) / 2026-09-29T08:00:00+08:00 / 预先可补偿操作与 tool-boundary 联合 capture，不自授远端 fork；2+2+3=7 / 深入完成 / 整合：`AGENT-WORKFLOW` [Ch81 AgentRewind→Waypoint](../../../../../books/part-07-agent/81-workflow.md)；实际正文与非作者写后通过

## arxiv:2609.34727

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Dynamic Flow, Static Graph 2609.34727v1](https://arxiv.org/abs/2609.34727v1) / 2026-09-29T08:00:00+08:00 / 固定图容纳选择性 KV 重算，并按实测调用成本规划 chunks；2+1+3=6 / 深入完成 / 整合：`INFER-TENSORRT-LLM` [Ch49 静态图→基础优化](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过

## arxiv:2609.34612

- Daily：papers/2026/09/29/README.md
- 事件/判断：[SPIMOE: Exploiting Hybrid Sparsity for Reasoning MoE Inference on Heterogeneous PIM Architectures 2609.34612v1](https://arxiv.org/abs/2609.34612v1) / 2026-09-29T08:00:00+08:00 / 联合稀疏/PIM 的质量与资源耦合验证，不把 recipe 升为通用机制；2+1+3=6 / 标准完成 / 仅报告：局部实现/评价不改变现有长期机制，具体理由见下节

## arxiv:2609.34351

- Daily：papers/2026/09/29/README.md
- 事件/判断：[PolyCIM: Improving Data Reuse in Digital CIM Accelerators with Polyhedral-Based Compilation 2609.34351v1](https://arxiv.org/abs/2609.34351v1) / 2026-09-29T08:00:00+08:00 / 非轴向 reuse 先仿射 realignment，再映射有限 CIM/layout；2+1+2=5 / 深入完成 / 整合：`INFER-TENSORRT-LLM` [Ch49 Nautilus→Persistent Executor](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过

## arxiv:2609.34663

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Tool Waiting and Re-arrival in Compile-Time-Static LLM Serving: Cost Mechanisms and Configuration Selection 2609.34663v1](https://arxiv.org/abs/2609.34663v1) / 2026-09-29T08:00:00+08:00 / 静态 bucket 与内生 tool re-arrival 联合决定 padding/驻留成本；2+1+3=6 / 深入完成 / 整合：`INFER-CONTINUOUS-BATCHING` [Ch46 trade-off→工程判断](../../../../../books/part-05-inference-system/46-continuous-batching.md)；实际正文与非作者写后通过

## arxiv:2609.35569

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Beyond Energy: When Sustainability Dimensions Reshape LLM Serving Decisions 2609.35569v1](https://arxiv.org/abs/2609.35569v1) / 2026-09-29T08:00:00+08:00 / 固定部署运营排序与跨部署 embodied crossover 分账；2+1+3=6 / 深入完成 / 整合：`PLATFORM-COST` [Ch70 Unit Economics 生命周期→需求反弹](../../../../../books/part-06-ai-infrastructure/70-cost.md)；实际正文与非作者写后通过

## arxiv:2609.35188

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Beneath the Tokens: A Performance Engineering Study of Multi-Token Prediction in GPU-Accelerated LLM Inference 2609.35188v1](https://arxiv.org/abs/2609.35188v1) / 2026-09-29T08:00:00+08:00 / 每有效 token 的调用摊销与单 kernel 时间不是同一指标；1+1+3=5 / 标准完成 / 仅报告：局部实现/评价不改变现有长期机制，具体理由见下节

## arxiv:2609.34380

- Daily：papers/2026/09/29/README.md
- 事件/判断：[DPS: Dual-Mode Precision LLM Serving with Semi-Unified Memory 2609.34380v1](https://arxiv.org/abs/2609.34380v1) / 2026-09-29T08:00:00+08:00 / persistent weights/residual/KV 非对称共享与 forward 模式提交；2+2+3=7 / 深入完成 / 整合：`INFER-GPU-MEMORY` [Ch54 双模式 Weight 与 KV](../../../../../books/part-05-inference-system/54-gpu-memory.md)；实际正文与非作者写后通过

## arxiv:2609.33889

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Where Activation Sparsity and KV-Cache Sparsity Cross in LLM Decoding 2609.33889v1](https://arxiv.org/abs/2609.33889v1) / 2026-09-29T08:00:00+08:00 / weight-read/KV-read 的 byte 交点还须质量和 kernel 成本校准；2+1+3=6 / 深入完成 / 整合：`INFER-GPU-MEMORY` [Ch54 少读 Weight 与少读 KV 的交点](../../../../../books/part-05-inference-system/54-gpu-memory.md)；实际正文与非作者写后通过

## arxiv:2609.33477

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Just Let Linear States Forget the Distant Past: Prefix Caching via SuffixReplay for Hybrid LLMs 2609.33477v1](https://arxiv.org/abs/2609.33477v1) / 2026-09-29T08:00:00+08:00 / 按 linear group 保存输入锚点，近似 replay 与发布边界分开；2+2+3=7 / 深入完成 / 整合：`INFER-KV-CACHE` [Ch45 Group 输入锚点→Video cache](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；实际正文与非作者写后通过

## arxiv:2609.34785

- Daily：papers/2026/09/29/README.md
- 事件/判断：[BEHAVE: Functional Behavior Modeling Enables Self-Improving Agents for Hardware Design and Verification 2609.34785v1](https://arxiv.org/abs/2609.34785v1) / 2026-09-29T08:00:00+08:00 / 允许 transaction timing 差异但双产物都须独立 hidden gold；2+1+3=6 / 深入完成 / 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66 Transaction oracle→Dense Process](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；实际正文与非作者写后通过

## arxiv:2609.35508

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Argus: Agentic, Reference-Calibrated, Tree-Guided, System-Software-Level Bottleneck Localization 2609.35508v1](https://arxiv.org/abs/2609.35508v1) / 2026-09-29T08:00:00+08:00 / 同 workload reference 与 tree/probe 定位的受限实现验证；1+1+3=5 / 标准完成 / 仅报告：局部实现/评价不改变现有长期机制，具体理由见下节

## arxiv:2609.35587

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Hardware-Aware Features for CUTLASS Kernel Selection 2609.35587v1](https://arxiv.org/abs/2609.35587v1) / 2026-09-29T08:00:00+08:00 / candidate-induced 硬件代理排序、shape-group 留出与执行 coverage；2+1+2=5 / 深入完成 / 整合：`INFER-TENSORRT-LLM` [Ch49 硬件行为代理→Tensor Core层级](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过

## arxiv:2609.35425

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Semantic Prefix Oracles 2609.35425v1](https://arxiv.org/abs/2609.35425v1) / 2026-09-29T08:00:00+08:00 / 语义 prefix 安全剪枝与可完成性是两份合同；2+2+3=7 / 深入完成 / 整合：`INFER-SGLANG` [Ch51 Structured Generation→Adapter readiness](../../../../../books/part-05-inference-system/51-sglang.md)；实际正文与非作者写后通过

## arxiv:2609.35739

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Rubric-Calibrated Preferences 2609.35739v1](https://arxiv.org/abs/2609.35739v1) / 2026-09-29T08:00:00+08:00 / query内BT排序与跨query单位/原点分开校准；2+1+3=6 / 深入完成 / 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66 Judge Ranking→Route/defer](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；实际正文与非作者写后通过

## arxiv:2609.35430

- Daily：papers/2026/09/29/README.md
- 事件/判断：[SpeakGR 2609.35430v1](https://arxiv.org/abs/2609.35430v1) / 2026-09-29T08:00:00+08:00 / 扩SID词表后分开检索正确与原文本条件分布保护；2+1+3=6 / 深入完成 / 整合：`TRAIN-SFT` [Ch29 Occupancy→共享Trace](../../../../../books/part-04-training-system/29-sft.md)；实际正文与非作者写后通过

## arxiv:2609.33517

- Daily：papers/2026/09/29/README.md
- 事件/判断：[TRACE 2609.33517v1](https://arxiv.org/abs/2609.33517v1) / 2026-09-29T08:00:00+08:00 / return epoch 下逐项有效不等整组关键义务覆盖；2+2+3=7 / 深入完成 / 整合：`AGENT-MEMORY` [Ch77 Memory Read Recency→累计披露](../../../../../books/part-07-agent/77-memory.md)；实际正文与非作者写后通过

## arxiv:2609.35439

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Revision, Not Restart: Revisable Visual Plans for Closed-Loop World–Action Models 2609.35439v1](https://arxiv.org/abs/2609.35439v1) / 2026-09-29T08:00:00+08:00 / 保存visual solver路径，用真实feedback修订未执行计划再解动作；2+2+3=7 / 深入完成 / 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26 World-action→Future-to-Action](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；实际正文与非作者写后通过

## arxiv:2609.35652

- Daily：papers/2026/09/29/README.md
- 事件/判断：[MM-ABC: Towards Generalist Mobile Manipulation via Seeing, Coordinating and Imagining 2609.35652v1](https://arxiv.org/abs/2609.35652v1) / 2026-09-29T08:00:00+08:00 / common endpoint loss下clean-head/velocity-head改变noise burden；2+1+3=6 / 深入完成 / 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26 固定点decoder→endpoint initialization](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；实际正文与非作者写后通过

## arxiv:2609.35469

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Rethinking Causal Action Tokenization with Conditional Annealing in Flow Matching 2609.35469v1](https://arxiv.org/abs/2609.35469v1) / 2026-09-29T08:00:00+08:00 / flow阶段绑定code可见性形成ordered increments而非物理因果；2+1+3=6 / 深入完成 / 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26 离散codec→粗planner/refiner](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；实际正文与非作者写后通过

## arxiv:2609.35304

- Daily：papers/2026/09/29/README.md
- 事件/判断：[Signal or Noise? Modality Contribution and Cooperation in Multimodal GraphRAG 2609.35304v1](https://arxiv.org/abs/2609.35304v1) / 2026-09-29T08:00:00+08:00 / supporting-edge subset admission与明确baseline的模态交互诊断；2+1+3=6 / 深入完成 / 整合：`AGENT-RAG` [Ch76 多模态admission→Escalation](../../../../../books/part-07-agent/76-rag.md)；实际正文与非作者写后通过

## arxiv:2609.34496

- Daily：papers/2026/09/29/README.md
- 事件/判断：[MASTraceBench: Diagnosing Collaboration Gains through Proposal Trajectories in LLM-Based Multi-Agent Systems 2609.34496v1](https://arxiv.org/abs/2609.34496v1) / 2026-09-29T08:00:00+08:00 / initial→final proposal→aggregate分三层质量账；2+1+3=6 / 深入完成 / 整合：`AGENT-MULTI-AGENT` [Ch82 Evaluation成本表→条件分支](../../../../../books/part-07-agent/82-multi-agent.md)；实际正文与非作者写后通过

## arxiv:2609.35794

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Sieve and Sage: Efficient Distraction Filtering for Reliable RALM Abstention — 2609.35794v1](https://arxiv.org/html/2609.35794v1) / 2026-09-30T08:00:00+08:00 / 检索缺证据与存在证据却受干扰需要不同补救；生成前gate提供条件性路由。 2+2+2=6 / 深入完成 / 整合：`AGENT-RAG` / [Ch76](../../../../../books/part-07-agent/76-rag.md)

## arxiv:2609.35808

- Daily：papers/2026/09/30/README.md
- 事件/判断：[When Successful Memories Mislead Embodied Agents: Memory Adaption For Task-Conditioned Execution — 2609.35808v1](https://arxiv.org/html/2609.35808v1) / 2026-09-30T08:00:00+08:00 / 成功轨迹的旧动作schema仍能误导；将接口兼容收益与压缩收益分开。 3+1+2=6 / 深入完成 / 整合：`AGENT-MEMORY` / [Ch77](../../../../../books/part-07-agent/77-memory.md)

## arxiv:2609.35815

- Daily：papers/2026/09/30/README.md
- 事件/判断：[How to Run Statistics over LLM Judges and Trust the Results: Calibrated Inference for Small-Sample AI Evaluation with evalstats — 2609.35815v1](https://arxiv.org/html/2609.35815v1) / 2026-09-30T08:00:00+08:00 / 高judge agreement不保证区间/检验校准；人工配对抽样和估计不确定性改变发布判断。 3+2+3=8 / 深入完成 / 整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

## arxiv:2609.35817

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Less Uniform Discrete Diffusion is More Powerful and Scalable — 2609.35817v1](https://arxiv.org/html/2609.35817v1) / 2026-09-30T08:00:00+08:00 / uniform reverse目标的平滑与corruption身份耦合；清洁目标和per-token time改变训练解释。 2+2+2=6 / 深入完成 / 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)

## arxiv:2609.35832

- Daily：papers/2026/09/30/README.md
- 事件/判断：[When Should LLMs Trust Their Own Revisions? A Risk-Aware Study of Intrinsic Self-Correction — 2609.35832v1](https://arxiv.org/pdf/2609.35832v1) / 2026-09-30T08:00:00+08:00 / 修正错误与引入新错必须分账，revision前gate和后验acceptance预算不同。 2+1+2=5 / 标准完成 / 已有覆盖：`AGENT-REFLECTION` / [Ch80](../../../../../books/part-07-agent/80-reflection.md)

## arxiv:2609.35860

- Daily：papers/2026/09/30/README.md
- 事件/判断：[The Detectability Gap: Hidden Heterogeneity in Hallucination Detection Across Language Models — 2609.35860v1](https://arxiv.org/html/2609.35860v1) / 2026-09-30T08:00:00+08:00 / 用同一统计量定义难组再测detectability会自造gap；冻结partition后须换signal检验。 3+1+2=6 / 深入完成 / 整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

## arxiv:2609.36059

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Mnemon: Raw Records, Fast Judgments, Slow Thoughts — 2609.36059v1](https://arxiv.org/html/2609.36059v1) / 2026-09-30T08:00:00+08:00 / raw authority已覆盖；新增判定器替换条件及waves、总判断、lifecycle cost的不同预算。 2+2+3=7 / 深入完成 / 整合：`AGENT-MEMORY` / [Ch77](../../../../../books/part-07-agent/77-memory.md)

## arxiv:2609.36178

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Targeting Pivotal Decisions for Credit Assignment in Agentic Reinforcement Learning — 2609.36178v1](https://arxiv.org/html/2609.36178v1) / 2026-09-30T08:00:00+08:00 / judge选址不等数值credit；恢复两端状态，用固定current policy续跑估局部贡献。 2+2+2=6 / 深入完成 / 整合：`TRAIN-GRPO` / [Ch33](../../../../../books/part-04-training-system/33-grpo.md)

## arxiv:2609.36246

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Learning from Teacher Continuations at Student States — 2609.36246v1](https://arxiv.org/html/2609.36246v1) / 2026-09-30T08:00:00+08:00 / teacher文本continuation免logit接口，但其后续状态及CE监督边界不同于逐token纠错。 2+2+2=6 / 深入完成 / 整合：`TRAIN-SFT` / [Ch29](../../../../../books/part-04-training-system/29-sft.md)

## arxiv:2609.36452

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Reliable Parallel Decoding in Masked Diffusion Language Models — 2609.36452v1](https://arxiv.org/html/2609.36452v1) / 2026-09-30T08:00:00+08:00 / 同pass高confidence不足以joint commit；final-layer稳定性与未解决上游熵约束承诺集合。 2+1+2=5 / 深入完成 / 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)

## arxiv:2609.36522

- Daily：papers/2026/09/30/README.md
- 事件/判断：[ParaAnya: Accelerating Parallel Diffusion Sampling with Plug-and-Play Output Caching — 2609.36522v1](https://arxiv.org/html/2609.36522v1) / 2026-09-30T08:00:00+08:00 / 并行迭代反复访问同timestep可缓存输出，但命中检查及通信可能吃掉NFE收益。 2+2+2=6 / 深入完成 / 整合：`INFER-TENSORRT-LLM` / [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)

## arxiv:2609.36590

- Daily：papers/2026/09/30/README.md
- 事件/判断：[SEED: Self-Speculative Decoding via Implicit Encoder-Decoder — 2609.36590v1](https://arxiv.org/html/2609.36590v1) / 2026-09-30T08:00:00+08:00 / verifier刷新deep KV，再由薄末层读raw embedding起草，形成自推测的另一条件分支。 2+2+2=6 / 深入完成 / 整合：`INFER-SPECULATIVE-DECODING` / [Ch48](../../../../../books/part-05-inference-system/48-speculative-decoding.md)

## arxiv:2609.36654

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Replay the Curvature: Accurate and Scalable NVFP4 Quantization for Large Language Model Inference — 2609.36654v1](https://arxiv.org/html/2609.36654v1) / 2026-09-30T08:00:00+08:00 / 未来列可补偿时当前误差应条件化；scale候选需私有回放真实顺序量化轨迹。 2+2+2=6 / 深入完成 / 整合：`INFER-TENSORRT-LLM` / [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)

## arxiv:2609.36722

- Daily：papers/2026/09/30/README.md
- 事件/判断：[ATTUNER: Recomputation-Free KV Cache Reuse via Query-Side Adaptation — 2609.36722v1](https://arxiv.org/pdf/2609.36722v1) / 2026-09-30T08:00:00+08:00 / 独立artifact KV丢跨artifact条件；冻结cache producer并训练query consumer，不将位置修复当充分条件。 2+2+2=6 / 深入完成 / 整合：`INFER-KV-CACHE` / [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)

## arxiv:2609.36899

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Reshaping Rollout Workloads for Asynchronous RL Post-Training on Heterogeneous Accelerators — 2609.36899v1](https://arxiv.org/html/2609.36899v1) / 2026-09-30T08:00:00+08:00 / 暂停长轨迹可改善resident组成；depart/destination分离改变异构rollout调度。 2+2+2=6 / 深入完成 / 整合：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md)

## arxiv:2609.36903

- Daily：papers/2026/09/30/README.md
- 事件/判断：[MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conversation — 2609.36903v1](https://arxiv.org/html/2609.36903v1) / 2026-09-30T08:00:00+08:00 / 长多方双语评价及固定架构data对照限制由短dyadic效果外推的能力判断。 2+2+2=6 / 标准完成 / 仅报告：`MULTIMODAL-REPRESENTATION` / [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；新增证据不改长期机制，旧机制不重评

## arxiv:2609.36931

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Dating the Model: Hidden Dates in System Prompts Affect LLM Evaluation — 2609.36931v1](https://arxiv.org/html/2609.36931v1) / 2026-09-30T08:00:00+08:00 / system date是确定性输入干预，隐藏默认值可改变比较而非随机采样噪声。 2+1+2=5 / 标准完成 / 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

## arxiv:2609.36938

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Efficient Agentic LLM Serving over SSD-based Sparse KV Storage — 2609.36938v1](https://arxiv.org/html/2609.36938v1) / 2026-09-30T08:00:00+08:00 / 预测层间selector可预取，但target native selector及缺失补读仍决定Attention可见状态。 2+2+2=6 / 深入完成 / 整合：`INFER-KV-CACHE` / [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)

## arxiv:2609.36952

- Daily：papers/2026/09/30/README.md
- 事件/判断：[ER-JEPA: Experience Replay Improves Joint-Embedding Predictive Learning in Language Models — 2609.36952v1](https://arxiv.org/html/2609.36952v1) / 2026-09-30T08:00:00+08:00 / 匹配compute/token/current-batch对照仍显示历史内容作用；初筛关闭理由因此被独立反证。 2+1+2=5 / 标准完成 / 已有覆盖：`TRAIN-SFT` / [Ch29](../../../../../books/part-04-training-system/29-sft.md)

## arxiv:2609.36954

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Purlin: Separating Orchestration from the Datapath of Collectives — 2609.36954v1](https://arxiv.org/html/2609.36954v1) / 2026-09-30T08:00:00+08:00 / layout/copy-reduce语义和coordination可复用，但hardware datapath及数值policy不等价。 2+2+2=6 / 深入完成 / 整合：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md)

## arxiv:2609.36959

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Cobalt: Leveraging Expert Co-activation for Efficient Distributed MoE Training — 2609.36959v1](https://arxiv.org/html/2609.36959v1) / 2026-09-30T08:00:00+08:00 / 单token多expert的destination-node union不同于各expert负载和，改变布局目标。 2+2+2=6 / 深入完成 / 整合：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md)

## arxiv:2609.37044

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Learning from Think-Mode Advantage via On-Policy Distillation — 2609.37044v1](https://arxiv.org/html/2609.37044v1) / 2026-09-30T08:00:00+08:00 / teacher优势与trace对兄弟response的可转移性分离，用group路由权重而非一律强模仿。 2+1+2=5 / 深入完成 / 整合：`TRAIN-SFT` / [Ch29](../../../../../books/part-04-training-system/29-sft.md)

## arxiv:2609.37062

- Daily：papers/2026/09/30/README.md
- 事件/判断：[vSkipper: Translating Dynamic Layer Skipping into LLM Serving Gains — 2609.37062v1](https://arxiv.org/html/2609.37062v1) / 2026-09-30T08:00:00+08:00 / 内部skip仍需本层KV投影和route元数据；policy省层不自动成为引擎收益。 3+2+2=7 / 深入完成 / 整合：`INFER-SGLANG` / [Ch51](../../../../../books/part-05-inference-system/51-sglang.md)

## arxiv:2609.37196

- Daily：papers/2026/09/30/README.md
- 事件/判断：[ToolFence: Fine-Grained Authorization for Secure Tool-Using LLM Agents — 2609.37196v1](https://arxiv.org/html/2609.37196v1) / 2026-09-30T08:00:00+08:00 / capability shape grant与当前具体值provenance分离；缓存授权不能缓存证据真值。 3+2+2=7 / 深入完成 / 整合：`PLATFORM-SECURITY` / [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)

## arxiv:2609.37371

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Compiling Learning Problems into Adaptation Programs for Language Models — 2609.37371v1](https://arxiv.org/html/2609.37371v1) / 2026-09-30T08:00:00+08:00 / episode geometry可摊销选择adaptation program；未知family仍需default与适配成本预算。 2+1+2=5 / 深入完成 / 整合：`TRAIN-LORA` / [Ch30](../../../../../books/part-04-training-system/30-lora.md)

## arxiv:2609.37494

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Your Benchmark Is Not Saturated: Reviving Multiple-Choice Evaluation with Answer Pooling — 2609.37494v1](https://arxiv.org/html/2609.37494v1) / 2026-09-30T08:00:00+08:00 / 共享答案池把单题分类变耦合assignment；chance和干扰控制变化须与原任务分开。 2+1+2=5 / 深入完成 / 整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

## arxiv:2609.37532

- Daily：papers/2026/09/30/README.md
- 事件/判断：[DScale: Scaling Block-Diffusion Speculative Decoding with Adaptive Verification — 2609.37532v1](https://arxiv.org/html/2609.37532v1) / 2026-09-30T08:00:00+08:00 / 保完整草稿而限ragged verification共享预算；图固定地址不意味着commit边界固定。 2+2+2=6 / 深入完成 / 整合：`INFER-SPECULATIVE-DECODING` / [Ch48](../../../../../books/part-05-inference-system/48-speculative-decoding.md)

## arxiv:2609.37533

- Daily：papers/2026/09/30/README.md
- 事件/判断：[E-MoE: Enhanced Mixture-of-Experts for Non-Factorized Diffusion Language Models — 2609.37533v1](https://arxiv.org/html/2609.37533v1) / 2026-09-30T08:00:00+08:00 / 离散router latent可让parallel reverse采样相关；clean/noisy router匹配决定训练推理接口。 2+1+2=5 / 深入完成 / 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)

## arxiv:2609.37624

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Correct, Don't Delete: Mitigating Emergent Misalignment with Corrective Supervision — 2609.37624v1](https://arxiv.org/html/2609.37624v1) / 2026-09-30T08:00:00+08:00 / 删除坏监督移除该输入的训练机会，纠正则尝试供正面目标；两种intervention不可混同。 2+1+2=5 / 深入完成 / 整合：`TRAIN-DATA` / [Ch27](../../../../../books/part-04-training-system/27-data.md)

## arxiv:2609.37626

- Daily：papers/2026/09/30/README.md
- 事件/判断：[SPLASH: Switching Parallel Layouts of Attention with Seamless Handoff for LLM Serving — 2609.37626v1](https://arxiv.org/html/2609.37626v1) / 2026-09-30T08:00:00+08:00 / projection/KV ownership解耦后，live-layout切换需稳态+暂态容量及共同handoff。 3+2+2=7 / 深入完成 / 整合：`INFER-SCHEDULING` / [Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md)

## arxiv:2609.37690

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Honeycomb: Constant-Size Scene Memory Representation for Video World Models — 2609.37690v1](https://arxiv.org/html/2609.37690v1) / 2026-09-30T08:00:00+08:00 / 固定planes在expanding bounds下warp/coarsen；存储恒定不等信息精度恒定。 2+2+3=7 / 深入完成 / 整合：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)

## arxiv:2609.37852

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Delta-Matching: Closing the Final Gap of Native 8-bit Training for LLMs — 2609.37852v1](https://arxiv.org/html/2609.37852v1) / 2026-09-30T08:00:00+08:00 / 量化dP使saved delta失配，重算匹配contraction恢复softmax梯度零行和。 3+2+3=8 / 深入完成 / 整合：`TRAIN-PRETRAINING` / [Ch28](../../../../../books/part-04-training-system/28-pretraining.md)

## arxiv:2609.37879

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Retrieval Capacity of Self-Attention Under Competition — 2609.37879v1](https://arxiv.org/html/2609.37879v1) / 2026-09-30T08:00:00+08:00 / 权重不等独立知识贡献；V方向及delete/renormalize不同干预改变诊断解释。 2+1+3=6 / 深入完成 / 整合：`MODEL-SELF-ATTENTION` / [Ch14](../../../../../books/part-02-model/14-self-attention.md)

## arxiv:2609.37891

- Daily：papers/2026/09/30/README.md
- 事件/判断：[It's All Training: A Fully Synthetic Single-Stage Recipe for LLMs — 2609.37891v1](https://arxiv.org/html/2609.37891v1) / 2026-09-30T08:00:00+08:00 / 旧synthetic pipeline不重算；本窗同600M/data trace ablation和seed外反证限制效率归因。 2+1+2=5 / 标准完成 / 仅报告：`TRAIN-PRETRAINING` / [Ch28](../../../../../books/part-04-training-system/28-pretraining.md)；新增证据不改长期机制，旧机制不重评

## arxiv:2609.37899

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Scaling Zero-Order Pretraining through Model Sharding — 2609.37899v1](https://arxiv.org/html/2609.37899v1) / 2026-09-30T08:00:00+08:00 / 可分目标移除跨expert SPSA噪声，以表征耦合换独立更新，非通用通信分片。 2+2+3=7 / 深入完成 / 整合：`TRAIN-PRETRAINING` / [Ch28](../../../../../books/part-04-training-system/28-pretraining.md)

## arxiv:2609.37930

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Learning What to Remember: Long-horizon Counterfactual Memory Optimization — 2609.37930v1](https://arxiv.org/html/2609.37930v1) / 2026-09-30T08:00:00+08:00 / rewrite总效用含继承收益；相邻状态对同future targets的增量才接近本次write credit。 2+2+3=7 / 深入完成 / 整合：`AGENT-MEMORY` / [Ch77](../../../../../books/part-07-agent/77-memory.md)

## arxiv:2609.38109

- Daily：papers/2026/09/30/README.md
- 事件/判断：[How Local Mixing Encodes Relative Position in Global NoPE Attention — 2609.38109v1](https://arxiv.org/html/2609.38109v1) / 2026-09-30T08:00:00+08:00 / 局部mixing及Q/K对齐能读implicit recency，修正必须显式PE的绝对句。 2+1+3=6 / 深入完成 / 整合：`MODEL-POSITION-ENCODING` / [Ch13](../../../../../books/part-02-model/13-position-encoding.md)

## arxiv:2609.38121

- Daily：papers/2026/09/30/README.md
- 事件/判断：[WUSH-KV: KV Cache Quantization with Data-Adaptive Transforms — 2609.38121v1](https://arxiv.org/html/2609.38121v1) / 2026-09-30T08:00:00+08:00 / K/query与V/output需要不同consumer metric，post-RoPE变换折叠及在线代价不同。 2+2+2=6 / 深入完成 / 整合：`INFER-KV-CACHE` / [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)

## arxiv:2609.38123

- Daily：papers/2026/09/30/README.md
- 事件/判断：[HelixWorld: A Real-time Interactive Audio-Visual World Model — 2609.38123v1](https://arxiv.org/html/2609.38123v1) / 2026-09-30T08:00:00+08:00 / camera/world state联合条件视听，在student自身轨迹纠偏streaming而非只换音轨。 2+2+2=6 / 深入完成 / 整合：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)

## arxiv:2609.38142

- Daily：papers/2026/09/30/README.md
- 事件/判断：[AdviSD: Learning to Advise Frontier LLMs via Targeted Multi-Turn Self-Distillation — 2609.38142v1](https://arxiv.org/html/2609.38142v1) / 2026-09-30T08:00:00+08:00 / advisor对recorded response的预测敏感性可选择监督，但不是executor反事实因果。 2+2+3=7 / 深入完成 / 整合：`TRAIN-GRPO` / [Ch33](../../../../../books/part-04-training-system/33-grpo.md)

## arxiv:2609.38164

- Daily：papers/2026/09/30/README.md
- 事件/判断：[Rho: A Foundation for Efficiently Adaptable VLA Models — 2609.38164v1](https://arxiv.org/html/2609.38164v1) / 2026-09-30T08:00:00+08:00 / embodiment midtraining→任务更新→冻结action generator的latent repair分开适配authority。 2+2+2=6 / 深入完成 / 整合：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)

## arxiv:2609.38169

- Daily：papers/2026/09/30/README.md
- 事件/判断：[STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization — 2609.38169v1](https://arxiv.org/html/2609.38169v1) / 2026-09-30T08:00:00+08:00 / state误差随transition传播；readout时序与temporal/spatial敏感度影响量化生命周期。 2+2+3=7 / 深入完成 / 整合：`INFER-GPU-MEMORY` / [Ch54](../../../../../books/part-05-inference-system/54-gpu-memory.md)

## https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/

- Daily：papers/2026/10/01/README.md
- 事件/判断：[Disrupting a coordinated model distillation campaign](https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/) / 2026-09-30T18:30:00+08:00 / 密文隐藏不等消费授权，跨身份/model-family重放需与release gate分层。3+2+3=8 / 深入完成 / 整合：`PLATFORM-SECURITY` / [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)，实际POST通过

## https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/

- Daily：papers/2026/10/01/README.md
- 事件/判断：[Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) / 2026-10-01T04:00:00+08:00 / 风险监测与训练反馈权限分账，不能优化低monitor score代替安全。3+2+2=7 / 深入完成 / 整合：`PLATFORM-SECURITY` / [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)，仅反馈分工增量，实际POST通过

## arxiv:2609.38201

- Daily：papers/2026/10/01/README.md
- 事件/判断：[TomasuLLM](https://arxiv.org/html/2609.38201v1) / 2026-10-01T08:00:00+08:00 / 真实工具推测执行需要区分operand就绪、当前提交与预测观测的后继有效性。3+2+2=7 / 深入完成 / 整合：`AGENT-WORKFLOW` / [Ch81](../../../../../books/part-07-agent/81-workflow.md)，COW搜索与Live Fork之间，实际POST通过

## arxiv:2609.38205

- Daily：papers/2026/10/01/README.md
- 事件/判断：[The System Prompt Illusion](https://arxiv.org/html/2609.38205v1) / 2026-10-01T08:00:00+08:00 / probe可读、表征几何相似、局部patch因果证据不能互换；设计反证加深。2+1+2=5 / 深入完成 / 已有覆盖：`WORLDVIEW-REPRESENTATION` / [Ch5](../../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，仅readout/局部因果分账

## arxiv:2609.38222

- Daily：papers/2026/10/01/README.md
- 事件/判断：[Conformal Factuality Control for Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/html/2609.38222v1) / 2026-10-01T08:00:00+08:00 / 全回答支持率含空输出，不等于非空回答的条件支持率；verifier标签不是语义真值。2+1+2=5 / 标准完成 / 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，仅分母及oracle权限边界

## arxiv:2609.39334

- Daily：papers/2026/10/01/README.md
- 事件/判断：[SpecScale](https://arxiv.org/html/2609.39334v1) / 2026-10-01T08:00:00+08:00 / 逻辑候选数不等实际forward数，独立draw与PRM排队分别控制；长期机制缺口加深。2+2+2=6 / 深入完成 / 整合：`INFER-CONTINUOUS-BATCHING` / [Ch46](../../../../../books/part-05-inference-system/46-continuous-batching.md)，iteration工作单元后，实际POST通过

## arxiv:2609.38706

- Daily：papers/2026/10/01/README.md
- 事件/判断：[Preserving Provenance in Shared KV Caches](https://arxiv.org/html/2609.38706v1) / 2026-10-01T08:00:00+08:00 / local key正确不保证connector保留计算等价和sharing权限，跨worker/lookup-store身份须一致。3+2+2=7 / 深入完成 / 整合：`INFER-KV-CACHE` / [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，Prefix reuse，实际POST通过

## arxiv:2609.38981

- Daily：papers/2026/10/01/README.md
- 事件/判断：[Vosti](https://arxiv.org/html/2609.38981v1) / 2026-10-01T08:00:00+08:00 / 单kernel确定性不足wholeengine；canonical KV与relational kernel合同须组合。3+2+2=7 / 深入完成 / 整合：`INFER-TENSORRT-LLM` / [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)，数值验收，实际POST通过

## arxiv:2609.39819

- Daily：papers/2026/10/01/README.md
- 事件/判断：[KVTether](https://arxiv.org/html/2609.39819v1) / 2026-10-01T08:00:00+08:00 / message变异须传播prefix版本失效，跨context引用和waiting age分账；长期缺口加深。2+2+2=6 / 深入完成 / 整合：`INFER-KV-CACHE` / [Ch45](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，Agent语义区域后，实际POST通过

## arxiv:2609.39131

- Daily：papers/2026/10/01/README.md
- 事件/判断：[Characterizing High Bandwidth Flash for LLM Serving](https://arxiv.org/html/2609.39131v1) / 2026-10-01T08:00:00+08:00 / flash层容量不免费，write endurance、缓存锁定与admission压力联合规划；长期缺口加深。2+2+2=6 / 深入完成 / 整合：`INFER-GPU-MEMORY` / [Ch54](../../../../../books/part-05-inference-system/54-gpu-memory.md)，扩展层级，实际POST通过

## arxiv:2609.39235

- Daily：papers/2026/10/01/README.md
- 事件/判断：[The Planning Limits of Latent World Models](https://arxiv.org/html/2609.39235v1) / 2026-10-01T08:00:00+08:00 / 精确transition仍会因目标评分短视失败，prediction质量与planning range不同。3+2+2=7 / 深入完成 / 整合：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，Imagined rollout，实际POST通过

## arxiv:2609.38275

- Daily：papers/2026/10/01/README.md
- 事件/判断：[U-Fuzz](https://arxiv.org/html/2609.38275v1) / 2026-10-01T08:00:00+08:00 / 正确memory不保证正确消费，query/state变异、探索与判错需分权；长期缺口加深。2+2+2=6 / 深入完成 / 整合：`AGENT-MEMORY` / [Ch77](../../../../../books/part-07-agent/77-memory.md)，Recall/Use之后，实际POST通过

## arxiv:2609.38648

- Daily：papers/2026/10/01/README.md
- 事件/判断：[StateFork](https://arxiv.org/html/2609.38648v1) / 2026-10-01T08:00:00+08:00 / 文件恢复不等session后续观察等价，逻辑分支与checkpoint物理化分权；恢复合同深入。2+2+2=6 / 深入完成 / 整合：`AGENT-WORKFLOW` / [Ch81](../../../../../books/part-07-agent/81-workflow.md)，联合恢复之后，实际POST通过

## arxiv:2609.39145

- Daily：papers/2026/10/01/README.md
- 事件/判断：[Blackout and Freeze](https://arxiv.org/html/2609.39145v1) / 2026-10-01T08:00:00+08:00 / 缺帧与陈旧帧不同，恢复任务成功不认证物理风险；安全设计反证。3+2+2=7 / 深入完成 / 整合：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，Safety envelope，实际POST通过

## arxiv:2609.39822

- Daily：papers/2026/10/01/README.md
- 事件/判断：[Two-step Flow VLA](https://arxiv.org/html/2609.39822v1) / 2026-10-01T08:00:00+08:00 / 近action区间可另学平均velocity，NFE减少与控制质量必须分账；长期缺口加深。2+2+2=6 / 深入完成 / 整合：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，solver分支，实际POST通过

## arxiv:2609.39816

- Daily：papers/2026/10/01/README.md
- 事件/判断：[Prefix-invariant Fast Matrix Multiplication](https://arxiv.org/html/2609.39816v1) / 2026-10-01T08:00:00+08:00 / batch形状确定性不保证早先token不受未来影响，低精度累加需条件化prefix不变性。3+2+2=7 / 深入完成 / 整合：`INFER-TENSORRT-LLM` / [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)，数值合同，实际POST通过

## arxiv:2609.39350

- Daily：papers/2026/10/01/README.md
- 事件/判断：[HAPMoE](https://arxiv.org/html/2609.39350v1) / 2026-10-01T08:00:00+08:00 / 异构stage不能事后固定同构EP/TPE，需要device-aware联合容量/通信/分区计划；长期缺口加深。2+2+2=6 / 深入完成 / 整合：`TRAIN-PIPELINE-PARALLEL` / [Ch38](../../../../../books/part-04-training-system/38-pipeline-parallel.md)，Stage Balance，实际POST通过

## arxiv:2609.40093

- Daily：papers/2026/10/01/README.md
- 事件/判断：[ThunderEP](https://arxiv.org/html/2609.40093v1) / 2026-10-01T08:00:00+08:00 / host-only通信的relay traffic与依赖链收益不同，prefill DMA不能直接移植captured decode；长期缺口加深。2+2+2=6 / 深入完成 / 整合：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md)，多路径分支，实际POST通过

## arxiv:2609.38465

- Daily：papers/2026/10/01/README.md
- 事件/判断：[Gradient-Conflict Audit](https://arxiv.org/html/2609.38465v1) / 2026-10-01T08:00:00+08:00 / 降冲突proxy不等改善任务，诊断有效性须区分预测/同期、干预/结果与population；设计反证加深。3+1+2=6 / 深入完成 / 整合：`TRAIN-PRETRAINING` / [Ch28](../../../../../books/part-04-training-system/28-pretraining.md)，多模态方差冲突后，实际POST通过

## arxiv:2609.38777

- Daily：papers/2026/10/01/README.md
- 事件/判断：[CW-OPD](https://arxiv.org/html/2609.38777v1) / 2026-10-01T08:00:00+08:00 / 单world端点匹配不约束跨视觉响应，共同logit变化消项仅限transition；长期缺口加深。2+1+2=5 / 深入完成 / 整合：`TRAIN-GRPO` / [Ch33](../../../../../books/part-04-training-system/33-grpo.md)，teacher对照分支，实际POST通过

## arxiv:2609.39120

- Daily：papers/2026/10/01/README.md
- 事件/判断：[S-OPD](https://arxiv.org/html/2609.39120v1) / 2026-10-01T08:00:00+08:00 / teacher只选学生视觉contrast位置，mask敏感与noise稳定是不同辅助目标；长期缺口加深。2+1+2=5 / 深入完成 / 整合：`TRAIN-GRPO` / [Ch33](../../../../../books/part-04-training-system/33-grpo.md)，视觉选择分支，实际POST通过

## https://github.com/minimax-ai/minimax-code

- Daily：papers/2026/10/02/README.md
- 事件/判断：[MiniMax Code v0.6.0](https://github.com/MiniMax-AI/minimax-code/releases/tag/v0.6.0) / 2026-10-01T21:56:17+08:00 / BYOK宽重试需排除安全拒绝，拒绝说明不得污染状态码分类；1 + 1 + 2 = 4 / 深入完成 / 整合：`AGENT-PLATFORM`，[Ch84状态机](../../../../../books/part-07-agent/84-agent-platform.md#agent-runtime-state-machine)

## https://github.com/minimax-ai/openagentcore

- Daily：papers/2026/10/02/README.md
- 事件/判断：[OpenAgentCore v0.0.3（含v0.0.4同窗演进）](https://github.com/MiniMax-AI/OpenAgentCore/releases/tag/v0.0.3) / 2026-10-01T16:30:10+08:00 / 版本化CI Agent放宽工具/环境秘密边界，不能用main合入代替运行隔离；1 + 1 + 1 = 3 / 深入完成 / 仅报告：具体配置事实，无新增防护机制或已测安全结果
- Daily：papers/2026/10/04/README.md
- 事件/判断：[OpenAgentCore v0.0.7–v0.0.9](https://github.com/MiniMax-AI/OpenAgentCore/releases/tag/v0.0.9) / 2026-10-03T12:38:03+08:00 / 将发布入口移至 Web、撤去容器内托管 TLS/Docker socket 与 host Core admin port，并调整 URL/密钥契约；1 + 2 + 1 = 4 / 深入完成 / 仅报告：版本拓扑与操作者责任，不证明生产安全或新授权理论

## https://github.com/deepseek-ai/deepseek-harness

- Daily：papers/2026/10/04/README.md
- 事件/判断：[DeepSeek Harness v0.2.1-alpha.1](https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.2.1-alpha.1) / 2026-10-03T14:42:19+08:00 / 插件子路径元数据、诊断导出与扩展入口的破坏性兼容契约；1 + 1 + 1 = 3 / 深入完成 / 仅报告：alpha 版本迁移事实，不建立长期兼容机制结论

## https://github.com/xiaomimimo/mimo-code

- Daily：papers/2026/10/04/README.md
- 事件/判断：[MiMo-Code：Provider Refresh Without Instance Disposal，PR #2603](https://github.com/XiaomiMiMo/MiMo-Code/pull/2603) / 2026-10-03T19:11:41+08:00 / 保留 Instance 的 provider refresh：idle admission、先准备后统一发布、忙时不排队、closing-owner sampling 拒绝；1 + 1 + 2 = 4 / 深入完成 / 仅报告：局部 SDK/运行时契约及可复用约束的实现例证，不扩大为通用热更新保证

