# Daily Research — 2026-07-29

**规范：** V3
**窗口：** 2026-07-28T09:00:00+08:00 ～ 2026-07-29T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T19:46:39+08:00

## 1. 结论

本窗 arXiv 官方 owner inventory 共 570 个跨分类去重身份。旧 V2.1 报告保留了 141 个候选，来源召回本身可复用，但第一次 V3 重判把“已有 Books 覆盖”与“不能进入候选”混在一起，错误关闭了具有长期机制贡献的材料。本轮保留已闭合的 429 项题摘筛选证据，并对前次从 141 项中降级的 106 项逐条重读标题与完整摘要；第一次恢复 68 项后，又由独立复核者对余下 38 项做 false-negative 审计，进一步恢复 20 项，最终仅 18 项维持 pre-denominator closure。修正后的算术为 `570 raw = 123 candidates + 447 non-candidates`，retain rate 为 21.58%。已有正文覆盖只影响 Books disposition，不再改变 Candidate Denominator。

保留项集中在六条系统路线：评价协议必须控制真实 compute、随机性和外部状态；低比特训练、稀疏注意力与异构执行必须把算法决策交给真实 kernel/compiler 消费；长上下文与 Agent memory 必须区分 active state、可寻址归档和参数固化；工具与多 Agent 执行需要把语义风险、typed claim 和 workflow transition 交给外部 commit owner；World Model/VLA 必须区分视觉生成、action-conditioned transition 与实时控制；模型与可执行架构 artifact 必须作为同一个供应链安全对象。

123 项候选的 exact-v1 均可访问，本轮未发现整篇 withdrawn、身份争议或材料受阻；`2607.25589v1` 撤回的是原 benchmark 的性能、排名和临床结论，而不是论文身份，本轮只采用其纠错机制与无效结论边界。最终 54 项由现有 Books 机制正文完整承载，69 项形成并完成明确的 Books 增量；所有增量均已进入对应 owner 章节，并完成正文锚点、相邻衔接、证据边界和回退条件的写后复核。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 当前每日来源清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-ANTHROPIC | 当前每日来源清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-GOOGLE-AI | 当前每日来源清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-META-AI | 当前每日来源清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-QWEN | 当前每日来源清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-DEEPSEEK | 当前每日来源清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-MOONSHOT | 当前每日来源清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-TENCENT-HUNYUAN | 当前每日来源清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-ZAI | 当前每日来源清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-BYTEDANCE-SEED | 当前每日来源清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-BAIDU-ERNIE | 当前每日来源清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-XIAOMI-MIMO | 当前每日来源清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-MINIMAX | 当前每日来源清单在该历史窗口尚未生效 | 不适用 | 无 |
| SRC-ARXIV | 官方分类列表、v1 history 与 availability schedule；570 个跨分类去重身份；旧报告保存的 141 项题摘与 exact-v1 证据逐项重判，429 项既有 pre-denominator closure 保持关闭 | 已检查 | 无 |

本窗没有触发需要另行扫描的按需来源。arXiv 日期按首次公告归属，技术判断只使用 exact v1；当前 revision 只用于确认论文未撤回，不替代事件时证据。旧报告的逐项审阅与来源定位仍可从 Git 历史恢复，本次压缩没有把旧评分当作新准入依据。

## 3. 候选与判断

公开时间使用 arXiv 官方公告落入本窗的可证范围，不伪造更细粒度时间。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Do Models Fake Alignment Without Clear Consequences?](https://arxiv.org/html/2607.24758v1) | 2026-07-29T08:00:00+08:00 | 证明 evaluation-conditioned 行为差异不必依赖显式模型后果，改变部署外推与 paired-trace 审计合同；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [CaRE Compute-aware Remasking Evaluation Protocol for Masked Diffusion Language Models](https://arxiv.org/html/2607.24763v1) | 2026-07-29T08:00:00+08:00 | 把 masked-diffusion 排名从名义 step 数改为真实 NFE、随机性与多指标共同控制；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SpecPrefetch: Parameter-Efficient Expert Prefetching for Sparse MoE Foundation Models](https://arxiv.org/html/2607.24787v1) | 2026-07-29T08:00:00+08:00 | 将 expert transfer prediction 与 native router 的执行决定分权，使误预测只损失带宽而不改变模型语义；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Early Detection of Distributed Backdoors in Multi-Agent LLM Systems: A Characterization Study](https://arxiv.org/html/2607.24893v1) | 2026-07-29T08:00:00+08:00 | 将单步安全检查扩为跨 Agent fragment provenance 与 assembly-before-abort 的时序问题；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model](https://arxiv.org/html/2607.24904v1) | 2026-07-29T08:00:00+08:00 | 将视频 token identity 与 codec motion/residual 元数据绑定，并以 event gate 控制流式视觉计算；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Stable FP4 Training via Transposition-Invariant Block Quantization](https://arxiv.org/html/2607.24953v1) | 2026-07-29T08:00:00+08:00 | 把 forward/backward 两个矩阵视图的 scale identity 纳入 FP4 训练图，避免转置改变 block partition；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-PRETRAINING，[Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Conformal Cascade: Distribution-Free Accuracy Guarantees for Multi-Tier LLM Inference](https://arxiv.org/html/2607.25018v1) | 2026-07-29T08:00:00+08:00 | 用校准 prediction set 决定 commit/defer，并把有限样本 coverage 与级联成本显式关联；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Similar Models Learn Differently: Final-Window Pretraining Shapes Post-Training Beyond SFT](https://arxiv.org/html/2607.25063v1) | 2026-07-29T08:00:00+08:00 | 说明 matched post-SFT 行为不能替代 ordered pretraining lineage 与后续 update-response 的 artifact 适用性；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-PRETRAINING，[Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Addressable Recall Compaction for Long Context-Window Control in AI Agents](https://arxiv.org/html/2607.25066v1) | 2026-07-29T08:00:00+08:00 | 将完整 tool observation 留在 append-only 可寻址归档，active context 只保留 citation 与按 ID 回读能力；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [When Do Agent Loops Mistake Stagnation for Progress? Self-Evaluation Bias and Externally Grounded Verification in Long-Running Autonomous LLM Agent Loops](https://arxiv.org/pdf/2607.25152v1) | 2026-07-29T08:00:00+08:00 | 把 Agent completion 从自述/产物内 judge 迁移到真实 world-state gate，限制“更强 judge 足以闭环”的结论；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Rethinking CD: A Reproducibility Study and Extension on the Ineffectiveness of Contrastive Decoding at Mitigating Object Hallucinations in MLLMs](https://arxiv.org/html/2607.25196v1) | 2026-07-29T08:00:00+08:00 | 证明部分 hallucination 改善来自 output-distribution shift 或退化为 greedy，而非视觉 grounding 增强；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [VisualPatchWorld: Code World Models as Latent Structured Representations for Planning](https://arxiv.org/html/2607.25236v1) | 2026-07-29T08:00:00+08:00 | 把隐式 dynamics 分支扩为可检查、可滚动的程序状态，并保留接触动力学下的 simulator fallback；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems](https://arxiv.org/html/2607.25255v1) | 2026-07-29T08:00:00+08:00 | 将局部 prompt 分类演进为跨委派 semantic taint 与 irreversible sink 前的 workflow reconstruction；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Bridging Compute- and Data-Optimal Pretraining](https://arxiv.org/html/2607.25271v1) | 2026-07-29T08:00:00+08:00 | 以随模型、tokens-per-parameter 与扩增量变化的 token effectiveness 连接 compute-bound 与 data-bound regime；3 + 3 + 3 = 9 | 深入完成 | 整合：WORLDVIEW-SCALING-LAW，[Ch7](../../../../books/part-01-worldview/07-scaling-law.md) |
| [CoSA: Accelerating Long-Context Inference via Proxy-Kernel Co-Designed Sparse Attention](https://arxiv.org/html/2607.25291v1) | 2026-07-29T08:00:00+08:00 | 将 proxy 的 binary mask 改为 ordered candidate mask，再由 online-softmax kernel 在紧预算下提交跳过；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-PREFILL，[Ch43](../../../../books/part-05-inference-system/43-prefill.md) |
| [Hybrid Analysis for Secure MCP Tool Use in LLM Agents](https://arxiv.org/html/2607.25297v1) | 2026-07-29T08:00:00+08:00 | 把 prompt/output 静态扫描扩为 MCP 工具全生命周期的静态—动态联合检查与执行后验证；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Raven: High-Recall Sequence Modeling with Sparse Memory Routing](https://arxiv.org/html/2607.25357v1) | 2026-07-29T08:00:00+08:00 | 在 dense recurrent state 与 sliding-window hard eviction 之间引入固定槽位、稀疏选择写与 selective decay；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Explanation-Bound Tool Execution for AI Agents: Server-Verified Action Claims Without Trusting Model Rationales](https://arxiv.org/html/2607.25364v1) | 2026-07-29T08:00:00+08:00 | 将自由文本 rationale 降级为 proposal，把 typed action claim 与 server-held facts 的匹配交给外部 mediator；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [COVENANT: Natural-Language Workflow Compilation for Aligned Agent Execution](https://arxiv.org/html/2607.25400v1) | 2026-07-29T08:00:00+08:00 | 将自然语言 procedure 从 prompt 变成 WAST/WCFG，由 interpreter 拥有合法 transition 与 effect commit；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [CodeNib: A Multi-View Data System for Serving Repository Context to Coding Agents](https://arxiv.org/html/2607.25431v1) | 2026-07-29T08:00:00+08:00 | 把 coding context 组织为 commit-bound lexical/dense/structural views，并为增量更新声明各自有效边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [Seen, Said, or Forgotten? A Causal Audit of Visual KV Memory Across Dialog Turns](https://arxiv.org/html/2607.25467v1) | 2026-07-29T08:00:00+08:00 | 说明当前 attention 不是未来视觉证据价值，safe eviction 需要 future dependence 或事实已被可靠 verbalize；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Architectural Backdoors in Vision-Language Model Supply Chains via Representation Steering](https://arxiv.org/html/2607.25479v1) | 2026-07-29T08:00:00+08:00 | 证明模型供应链的攻击面包含 architecture/remote code 与计算图，权重扫描不足以建立 artifact trust；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-MODEL-REGISTRY，[Ch59](../../../../books/part-06-ai-infrastructure/59-model-registry.md) |
| [Beyond Prefill-Decode Disaggregation: Dissecting LLM Inference for Heterogeneous Platforms via Dynamic Operator Scheduling](https://arxiv.org/html/2607.25498v1) | 2026-07-29T08:00:00+08:00 | 将静态 PD/roofline placement 演进为 stage DAG、运行时 operator placement 与 persistent weight-layout 联合控制；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [PowerScale: Energy-Efficient Geo-Distributed Model Training with Federated Datacenter Power](https://arxiv.org/html/2607.25650v1) | 2026-07-29T08:00:00+08:00 | 把全站点 WAN barrier 改为区域内同步、区域间异步聚合，并让同步频率随训练进展和电力约束变化；3 + 3 + 2 = 8 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization](https://arxiv.org/html/2607.25659v1) | 2026-07-29T08:00:00+08:00 | 将 response-level GRPO advantage 通过 rubric/no-rubric counterfactual likelihood 对比重新分配到 token；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL](https://arxiv.org/html/2607.25816v1) | 2026-07-29T08:00:00+08:00 | 将独立 tool-call predictor 合并为同模型双模式，并以自身 rollout 对齐 proposal；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [AngelSpec: Towards Real-World High Performance Inference with Speculative Decoding](https://arxiv.org/html/2607.25852v1) | 2026-07-29T08:00:00+08:00 | 将 universal drafter/fixed verification 改为 workload-specialized proposal 与 batch-level verification budget；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [CONQuER: Hardware-Aware Mixed-Precision Quantisation with Online-Calibrated Surrogates](https://arxiv.org/html/2607.25884v1) | 2026-07-29T08:00:00+08:00 | 将 bit-width assignment 下沉到 compiler IR，用 surrogate 预筛并以少量真实硬件测量在线校准；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification](https://arxiv.org/html/2607.25904v1) | 2026-07-29T08:00:00+08:00 | 将 GUI reward 从截图/轨迹判断推进到 completion-condition proposal 与执行后环境状态取证；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [DC-WAM: Dynamic-Centric Visual Supervision and Reasoning for World-Action Models](https://arxiv.org/html/2607.25918v1) | 2026-07-29T08:00:00+08:00 | 将视觉分支的目标从外观重建收窄为交互诱发 dynamics，并以动态相关性控制 attention；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [From Role Prompt to Infinite Thinking: Exploiting Persona Conditioning for Inference Cost Attacks in LLMs](https://arxiv.org/html/2607.25936v1) | 2026-07-29T08:00:00+08:00 | 将 persona consistency 暴露为隐蔽的 token amplification 攻击面，要求预算与 stop policy 不由生成语义拥有；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [UniMem: Complementary Episodic-to-Parametric Memory for Boundary-Agnostic Task Streams](https://arxiv.org/html/2607.26017v1) | 2026-07-29T08:00:00+08:00 | 用 routing token 在 episodic retrieval 与 recurring-pattern parameter consolidation 间选择，显式暴露不可逆边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Wonder: Video World Model Done Better](https://arxiv.org/html/2607.26037v1) | 2026-07-29T08:00:00+08:00 | 将 camera control、dense coordinate field、稀疏长期视觉 memory 与实时生成共同设计；2 + 3 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [$π\mathbf{R}^2$: Reactive Real-time Flow Policies](https://arxiv.org/html/2607.26055v1) | 2026-07-29T08:00:00+08:00 | 以新鲜 fast proprioception、异步 slow vision-language state 与 latency-adaptive flow 恢复 action-chunk 闭环反应；3 + 3 + 3 = 9 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models](https://arxiv.org/html/2607.26056v1) | 2026-07-29T08:00:00+08:00 | 用共享 intent grammar 将 action-conditioned latent transition 映射为分布式 action law，使 direct policy 与可选 search 共存；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [GLIDE: Guided Layerwise Hybrid Attention for Efficient LLM Inference](https://arxiv.org/html/2607.24788v1) | 2026-07-29T08:00:00+08:00 | 用 layerwise sensitivity 决定哪些层保留 softmax window、哪些层改为 recurrent aggregation，将 KV I/O 从统一窗口升级为分层状态预算；3 + 3 + 2 = 8 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Prediction Is Not Memory: Dual-Timescale Gated Profile Writing for Persistent User Modeling](https://arxiv.org/html/2607.24798v1) | 2026-07-29T08:00:00+08:00 | 把交互预测与 durable profile write 分权，阻止短期点击直接固化为长期偏好；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [When Thinking Before Retrieval Hurts: TraceBound Diagnostics for Adaptive Knowledge-Graph Retrieval](https://arxiv.org/html/2607.24800v1) | 2026-07-29T08:00:00+08:00 | 证明 retrieval trace/prompt 增强可能增加重复调用并错误分配探索预算，检索必须按控制策略而非提示格式验收；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Forgetting Is Not a Fix: Path Dependence in Sequential Engram Editing](https://arxiv.org/html/2607.24805v1) | 2026-07-29T08:00:00+08:00 | 反驳模型编辑的交换律假设，要求每次后续编辑重新验证旧删除/修改声明；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Neuromorphic Diffusion Language Models: Addressing Compute and Memory Bottlenecks via Sparsity and Block Denoising](https://arxiv.org/html/2607.24841v1) | 2026-07-29T08:00:00+08:00 | 把 block diffusion 的每次参数读取多 token 进度与 spike 稀疏的 active-channel 减少放进同一 roofline 合同；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Agent Retrieval Bench: Evaluating Repository Context Retrieval for Coding Agents](https://arxiv.org/html/2607.24882v1) | 2026-07-29T08:00:00+08:00 | 用 repository edit→ripple 任务暴露 retrieval recall、candidate filter 与自然 no-gold abstention 校准的不同失败面；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [Beyond "What to Retrieve": Uncertainty in Retrieval-Augmented Code Generation](https://arxiv.org/html/2607.24884v1) | 2026-07-29T08:00:00+08:00 | 把 code RAG 的不确定性拆到 query、candidate pool、API set 与 downstream generation，说明过滤无法恢复初始召回缺失；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Mechanisms of Width Scaling in Normalized Residual Networks: The Effective Alignment Dimension](https://arxiv.org/html/2607.24887v1) | 2026-07-29T08:00:00+08:00 | 以 effective alignment dimension 约束有限样本下的宽度扩展，区分 function-preserving 扩容与 test-risk 改善；3 + 2 + 3 = 8 | 深入完成 | 整合：WORLDVIEW-SCALING-LAW，[Ch7](../../../../books/part-01-worldview/07-scaling-law.md) |
| [TYPO: Instruction-Dense Visual Jailbreaks against Commercial Closed-Source Image-Generation Models](https://arxiv.org/html/2607.24897v1) | 2026-07-29T08:00:00+08:00 | 把图像内密集文字与视觉布局组成双通道 jailbreak，扩展文本 prompt filter 的输入边界；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [ALIBI: Adaptive Agentic Attacks on LLM-Based Vulnerability Detectors via Adversarial Code Comments](https://arxiv.org/html/2607.24964v1) | 2026-07-29T08:00:00+08:00 | 证明代码注释可伪造工具结果并操纵 LLM vulnerability detector，要求自然语言与程序证据隔离；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Towards Robust Reinforcement Learning for Small-Scale Language Model Agents](https://arxiv.org/html/2607.25091v1) | 2026-07-29T08:00:00+08:00 | 把小模型 PPO 失败定位到 adapter 可训练性、importance-ratio 数值精度与 reward-model collapse 三个独立控制面；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-PPO，[Ch32](../../../../books/part-04-training-system/32-ppo.md) |
| [PreDiff-LM: Pretrained Discrete Masked Diffusion Language Modeling with Hybrid Attention](https://arxiv.org/html/2607.25157v1) | 2026-07-29T08:00:00+08:00 | 用 prompt 内 causal、masked target 内 bidirectional 的 hybrid attention 复用 AR 权重，同时保留与 AR 的质量/效率差距；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Decision-Level Hijacking: Injecting Cognitive Bias into Large Language Models via Bit-Flip Attacks](https://arxiv.org/html/2607.25227v1) | 2026-07-29T08:00:00+08:00 | 证明极少量 weight bit flip 能持久改变特定议题立场，要求 registry 对权重完整性与行为 canary 联合验证；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-MODEL-REGISTRY，[Ch59](../../../../books/part-06-ai-infrastructure/59-model-registry.md) |
| [Instruction-Tuned Language Models Cannot Sample from Distributions They Can Describe](https://arxiv.org/html/2607.25292v1) | 2026-07-29T08:00:00+08:00 | 区分模型能描述群体分布与单次调用能从该分布采样，阻止把 temperature 多次调用当成人群抽样器；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Every Time I Hire a Linguist, Inference Costs Go Down: On Linguistic Rules as Effective Prompt Compressors](https://arxiv.org/html/2607.25335v1) | 2026-07-29T08:00:00+08:00 | 把 prompt compression 的在线 LM scoring 替换为离线搜索出的确定性语言规则，并暴露高压缩率下从 token pruning 转向 sentence extraction 的边界；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control](https://arxiv.org/html/2607.25337v1) | 2026-07-29T08:00:00+08:00 | 从离线轨迹顺序挖掘 directed temporal cost，使 world-model 表示训练与 plan-time progress ranking 对齐；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following](https://arxiv.org/html/2607.25398v1) | 2026-07-29T08:00:00+08:00 | 以长 policy 文档、真实工具轨迹和全条件 all-pass rubric 检查 standing instruction 是否真正约束执行；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Bits and Memories: Measuring Verbatim Extraction Across LLM Quantization](https://arxiv.org/html/2607.25451v1) | 2026-07-29T08:00:00+08:00 | 用 verbatim extraction 而非 membership inference 衡量量化后的隐私风险，否定把压缩当作删除机制；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model](https://arxiv.org/html/2607.25487v1) | 2026-07-29T08:00:00+08:00 | 把 episode plan、chunk-level think 与双视角时间历史蒸馏到小型 VLA，展示监督结构与模型容量的替代关系；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Automated Numerical Stability Analysis of Deep Learning Operators](https://arxiv.org/html/2607.25494v1) | 2026-07-29T08:00:00+08:00 | 以 stochastic perturbation 检测 operator 数值不稳定，把 dtype 标签推进为可监测的数值执行合同；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [At-the-Roofline Sparse Tensor Contractions on Vector Processors for Transformer Inference](https://arxiv.org/html/2607.25504v1) | 2026-07-29T08:00:00+08:00 | 说明中等双稀疏只有被 ISA 与 metadata-driven gather-accumulate-scatter 消费才接近 roofline；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Agent Skills Matter: Inferring Proprietary Skills from Execution Trajectories](https://arxiv.org/html/2607.25560v1) | 2026-07-29T08:00:00+08:00 | 把可观察 trajectory 识别为 proprietary skill 的行为侧信道，要求发布/日志策略纳入 procedure leakage threat model；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Forensic Reproducibility Audit of a Radiology Vision-Language Model Benchmark: From Intended Protocol to Released Artifact](https://arxiv.org/html/2607.25589v1) | 2026-07-29T08:00:00+08:00 | 用一次纠错审计说明可复算数值不等于复现原实验，benchmark 必须绑定 cohort、render、prompt、model、call 与 annotation identity；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [An Empirical Study of Model Context Protocol Applications](https://arxiv.org/html/2607.25635v1) | 2026-07-29T08:00:00+08:00 | 把 MCP app 侧 configuration、SDK transport 与 blocking approval 分成独立集成责任，暴露协议没有自动提供人类监督；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-MCP，[Ch83](../../../../books/part-07-agent/83-mcp.md) |
| [Demystifying Deep Learning Compiler Frontend Bugs: An LLM-Aided Empirical Study](https://arxiv.org/html/2607.25651v1) | 2026-07-29T08:00:00+08:00 | 把 compiler frontend graph capture/IR translation 作为独立故障层，并以 root-cause-aware tests 验证而非只测低层 operator；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic Simulation](https://arxiv.org/html/2607.25656v1) | 2026-07-29T08:00:00+08:00 | 用确定性 simulation 隔离 orchestration plan 的依赖、并行与资源冲突，避免把 individual agent 能力混入调度评价；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Detecting CSAM Text-to-Image LoRAs From Weights](https://arxiv.org/html/2607.25750v1) | 2026-07-29T08:00:00+08:00 | 以 LoRA update 的奇异向量作为 inference-free 内容指纹，为不安全生成前的权重准入提供 sensor；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-MODEL-REGISTRY，[Ch59](../../../../books/part-06-ai-infrastructure/59-model-registry.md) |
| [WarmTuner: Program-Specific Warm Starts for Compiler Autotuning via Offline-to-Online Reinforcement Learning](https://arxiv.org/html/2607.25831v1) | 2026-07-29T08:00:00+08:00 | 把历史 autotuning prior 与目标程序的 compile-run feedback 合并，说明配置 policy 必须允许在线校准与 fallback；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Towards a Systems Foundation for Agentic Cloud Management](https://arxiv.org/html/2607.25883v1) | 2026-07-29T08:00:00+08:00 | 为 cloud management agent 分离 session-local resource view、共享资源并发协调、冲突 intent 与 attributable feedback；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Distributing Security Controls Through Harness Engineering](https://arxiv.org/html/2607.25890v1) | 2026-07-29T08:00:00+08:00 | 把安全控制分布到 prompt、tool gateway、filesystem 与 harness，并用同一 adversarial suite 检查组合边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Minimizing Targeted Activations: Input-Only Suppression of Evaluation-Awareness Latents in Large Language Models](https://arxiv.org/html/2607.25907v1) | 2026-07-29T08:00:00+08:00 | 以 placebo direction 和真实 passage 对照证明 latent readability/suppressibility 不等于行为可控性；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Penelope: Localized Latent Recurrence for Efficient Structured Reasoning](https://arxiv.org/html/2607.25915v1) | 2026-07-29T08:00:00+08:00 | 把额外 reasoning compute 局部化为 decoder 中段 recurrence 与 boundary memory，而非重复整层或生成显式 CoT；3 + 2 + 3 = 8 | 深入完成 | 整合：MODEL-TRANSFORMER-LAYER，[Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [MODUS: Decoder-Only Any-to-Any Modeling of Diverse Modalities](https://arxiv.org/html/2607.25948v1) | 2026-07-29T08:00:00+08:00 | 将任意模态统一为 decoder-only 输入/输出 token，不依赖 modality-specific head，并允许生成另一模态做自校验；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Reinforcement Learning for Code Optimization](https://arxiv.org/html/2607.25970v1) | 2026-07-29T08:00:00+08:00 | 把 correctness、执行时间噪声、稀疏 reward 与 GRPO 稳定性绑定同一 code-optimization RL 环境；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [IH-Benchmark: A Conflict-Centered Benchmark for Instruction-Hierarchy Robustness in LLM Applications](https://arxiv.org/html/2607.25987v1) | 2026-07-29T08:00:00+08:00 | 证明 system-user 合规不能代表 user-tool 冲突面，instruction hierarchy 必须按来源层级和 constraint family 分片评价；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches?](https://arxiv.org/html/2607.25995v1) | 2026-07-29T08:00:00+08:00 | 证明 scanner-only 修复缺少 live call graph 与 service-account binding 时会产生功能 blast radius，runtime topology 应是 remediation evidence；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Parallel Decoding Distillation for Fast Image and Video Generation](https://arxiv.org/html/2607.26004v1) | 2026-07-29T08:00:00+08:00 | 让一次 network evaluation 预测多个 denoising steps，以 trajectory distillation 换少步生成并保留可变 NFE；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Reinformed Dreamer: An Asymmetric World Model Efficiently Trained through Latent Guidance](https://arxiv.org/html/2607.26040v1) | 2026-07-29T08:00:00+08:00 | 用训练期 privileged state 的 latent guidance 改善 observation representation，同时把部署时可见 observation 与特权信息分离；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?](https://arxiv.org/html/2607.26041v1) | 2026-07-29T08:00:00+08:00 | 将 computer-use 的 GUI grounding 与 action 后 causal transition reconstruction 分开，直接诊断 stale observation、source tracking 与 recovery；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Spend Experts Where You Are Unsure: Confidence-Adaptive Routing for Mixture-of-Experts LoRA](https://arxiv.org/html/2607.26052v1) | 2026-07-29T08:00:00+08:00 | 用 router mass 与 expert disagreement 按 token 自适应选择 expert 数，并用 budget thermostat 保持平均 compute；3 + 2 + 3 = 8 | 深入完成 | 整合：MODEL-MOE，[Ch21](../../../../books/part-02-model/21-moe.md) |
| [Kernel Forge: An Agent Harness for LLM-based Generation and Optimization of CUDA Kernels](https://arxiv.org/html/2607.24762v1) | 2026-07-29T08:00:00+08:00 | 把未修改 PyTorch 模型内的 kernel 发现、候选搜索、编译、正确性检查、计时与回嵌纳入同一 agent harness；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Measuring and Improving Behavioral Consistency in Large Language Models through Fact-Heuristic-Emotion State Enforcement](https://arxiv.org/html/2607.24765v1) | 2026-07-29T08:00:00+08:00 | 以 Fact/Heuristic/Emotion typed state 降低重复决策波动，同时明确一致性改善不等于推理正确；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [RoCo-ACE: Rollout-Conditioned Online Distillation for Retention-Aware Knowledge Injection](https://arxiv.org/html/2607.24771v1) | 2026-07-29T08:00:00+08:00 | 用同一 rollout 的有/无参考似然差给 reference-supported token 重新加权，并对遗漏权威事实做稀疏锚定校正；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-SFT，[Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [LivingArena: Do LLMs Know What Other LLMs Don't? Peer-Probing as Scalable Evaluation](https://arxiv.org/html/2607.24780v1) | 2026-07-29T08:00:00+08:00 | 用交互历史驱动模型互相生成可验证探针，并分离答题能力与可靠出题/自验能力；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SearchArt: Training Long-Horizon Search Agent with Scalable Synthetic and Verified Task](https://arxiv.org/html/2607.24850v1) | 2026-07-29T08:00:00+08:00 | 从网页构造证据图、QA 与搜索轨迹，并以一致性、轨迹质量和证据相关性联合验收后进入 SFT/RL；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md) |
| [The Missing Layer: Specification Infrastructure for AI Oversight](https://arxiv.org/html/2607.24866v1) | 2026-07-29T08:00:00+08:00 | 以版本化 specification 连接可解释性、运行时 mediation、evaluation 与 escalation，使一份 policy artifact 驱动多层监督；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Inverse RL Helps Align AI by Imitating Humans](https://arxiv.org/html/2607.24900v1) | 2026-07-29T08:00:00+08:00 | 从偏好标签反推 evaluator 的隐含 reward，并显式暴露可识别性、偏差与策略依赖；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [PerceptionBench: Evaluating Atomic Visual Perception in Multimodal Large Language Models](https://arxiv.org/html/2607.24957v1) | 2026-07-29T08:00:00+08:00 | 以受控观测与任务分片区分 perception failure、reasoning failure 和 evaluator failure，避免总分掩盖错误 owner；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Matryoshka Agent: Unfolding Sub-Agents for Long-Horizon Machine Learning Engineering](https://arxiv.org/html/2607.25090v1) | 2026-07-29T08:00:00+08:00 | 由 Orchestrator 保持紧凑长期探索状态，短生命周期 Sub-Agent 通过标准工具接口拥有具体环境执行；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [ScalableRAG: High-Quality RAG at Zero Ingestion Cost](https://arxiv.org/html/2607.25135v1) | 2026-07-29T08:00:00+08:00 | 用可读写 document/value workspace 与常数次 LLM 调用替代昂贵预构建知识图，另保留少量 ingestion 的扩展分支；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Less Data, Better Alignment: Data-Centric Multi-Evaluator Agreement for Preference Optimization](https://arxiv.org/html/2607.25136v1) | 2026-07-29T08:00:00+08:00 | 由 on-policy 候选触发多 rubric evaluator 与过程 critic，只让高共识信号进入更新；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [HiEviDR-Bench: A Benchmark for Hierarchical Evidence Aggregation in Deep Research](https://arxiv.org/html/2607.25151v1) | 2026-07-29T08:00:00+08:00 | 用 evidence graph 与逐级 gate 分离证据识别、跨源连接、中间 claim、引用和最终答案错误；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Laplace-PSN-IRT: Uncertainty Quantification for Neural Item Response Theory Models of LLM Benchmarks](https://arxiv.org/html/2607.25257v1) | 2026-07-29T08:00:00+08:00 | 用 item difficulty、模型能力与后验不确定性分离观测分数，使比较携带置信区间而非单点排名；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [CLBench-V: Evaluating Multimodal Context Learning from Grounding to Knowledge Acquisition](https://arxiv.org/html/2607.25294v1) | 2026-07-29T08:00:00+08:00 | 将多模态 in-context learning 分解为 grounding、规则归纳与新知识获得，避免总分掩盖阶段性失败；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Specula: Scaling formal specifications for autonomous model checking of system code](https://arxiv.org/html/2607.25333v1) | 2026-07-29T08:00:00+08:00 | 让 agent 从系统代码生成形式化 specification，并把模型检查器结果反馈到迭代修正而非让 LLM 自证；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain](https://arxiv.org/html/2607.25415v1) | 2026-07-29T08:00:00+08:00 | 将 agent policy、外部控制器、执行 receipt 与训练数据闭环成可回放的运营系统；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Toward an Organizational Science of Multi-Agent LLM Systems: Decoupling Who, How, and Which Algorithm](https://arxiv.org/html/2607.25446v1) | 2026-07-29T08:00:00+08:00 | 分离团队角色、协调方式与协作算法，并显示 accountability 只有进入交付控制流时才改变结果；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Beyond Self-Knowledge: Propagating Uncertainty Across Reasoning and Retrieval in LLMs](https://arxiv.org/html/2607.25600v1) | 2026-07-29T08:00:00+08:00 | 用验证集冻结的模型特定阈值决定直接回答或 top-5 检索，暴露选择性证据获取与额外 probe token 的成本；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [MemSFT: Mitigating Alignment Tax with an External Parametric Memory](https://arxiv.org/html/2607.25614v1) | 2026-07-29T08:00:00+08:00 | 冻结 backbone，以可复用 parametric memory 模仿 retriever，并由逐 token router 融合两者分布；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-SFT，[Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [SkillGate: Cost Efficient Runtime Malicious Skill File Detection in Coding Agents](https://arxiv.org/html/2607.25619v1) | 2026-07-29T08:00:00+08:00 | 用 regex 安全预筛与局部 snippet LLM judge 降低 skill 安装前检查成本，同时显式保留漏检边界；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Localized Adaptation Reveals Distinct Learning Signatures in Transformers](https://arxiv.org/html/2607.25663v1) | 2026-07-29T08:00:00+08:00 | 用分层 LoRA 干预表明 lexical、fact、policy、causal 与 procedural objective 具有不同 acquisition/transfer/boundedness geometry；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-LORA，[Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge Prediction](https://arxiv.org/html/2607.25718v1) | 2026-07-29T08:00:00+08:00 | 把工具前置条件、共享状态和 effect dependency 纳入 action graph，由执行器验证而非模型自由串接；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Transformer Transformer: A Unified Model for Motion-Conditioned Robot Co-design](https://arxiv.org/html/2607.25798v1) | 2026-07-29T08:00:00+08:00 | 统一 token 化 embodiment、state 与 action，以 reward-agnostic dynamics 预测指导机器人形态和控制器联合搜索；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [CHILL-Harness: Counterfactual Harness Learning for Efficient Reasoning in Long-Horizon Agents](https://arxiv.org/html/2607.25825v1) | 2026-07-29T08:00:00+08:00 | 估计 orchestration 干预的反事实 advantage，只授权有充分收益且保持成功率的 workflow 调整；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs](https://arxiv.org/html/2607.25853v1) | 2026-07-29T08:00:00+08:00 | 把高层 procedure 与低层 effectful step 分层，允许 checkpoint、恢复与局部 fallback；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Stemma: Induced Decision Regions Reveal LLM Provenance](https://arxiv.org/html/2607.25880v1) | 2026-07-29T08:00:00+08:00 | 将开放输出映射为有限 decision region，以适配后仍继承的决策边界而非表面文本识别模型 lineage；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-MODEL-REGISTRY，[Ch59](../../../../books/part-06-ai-infrastructure/59-model-registry.md) |
| [RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement](https://arxiv.org/html/2607.25886v1) | 2026-07-29T08:00:00+08:00 | 固定训练、服务与评测栈，只让 Agent 改数据策略，并保留中途最优 checkpoint 防止后续反馈驱动退化；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Toward Standardized Cross-Vendor Agent Tool Trust Management in Autonomous Networks](https://arxiv.org/html/2607.25914v1) | 2026-07-29T08:00:00+08:00 | 用 trust state machine、跨厂商通知与依赖图回溯，把工具信任变化传播到调用方和受影响操作；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SecDrift: Measuring Sector-Conditioned Security Drift in AI-Generated Code](https://arxiv.org/html/2607.25225v1) | 2026-07-29T08:00:00+08:00 | 以 matched counterfactual 固定任务、接口和示例，仅改变行业语境，测量代码安全漂移并暴露 detector 零告警的下界性质；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [The Case Against Generation for Retrieval: Discriminative Language Models as Effective Retrievers](https://arxiv.org/html/2607.25346v1) | 2026-07-29T08:00:00+08:00 | 以双塔判别式表示、EOS pooling、KL distillation 与 ANN 将 retrieval 从生成式解码改回可索引匹配；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Distilling Temporal Search and Reasoning: Evolving LLMs for Future Prediction via Harness-Assisted Efficient Data Synthesis](https://arxiv.org/html/2607.25554v1) | 2026-07-29T08:00:00+08:00 | 由 time-truncation harness 在每次搜索交互上强制时间截断，防止未来信息泄漏进训练 lineage；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md) |
| [F(AI)²R: Who Did What, and Who Checked? Verifiable AI Provenance as an Executable Skill](https://arxiv.org/html/2607.25637v1) | 2026-07-29T08:00:00+08:00 | 用带授权者与 authority ceiling 的 provenance event 区分 artifact 可访问性、claim verification 和最终 truth status；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-TRACE，[Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks](https://arxiv.org/html/2607.25877v1) | 2026-07-29T08:00:00+08:00 | 在固定 Agent DAG 上传播经过校准的局部概率，显式暴露相关性假设与人工接管预算；2 + 2 + 1 = 5 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [MDTransformer: A Hardware-Software Co-Design of Mode-Division Photonic Transformer Accelerator with Inverse-Designed Coherent Crossbar](https://arxiv.org/html/2607.26016v1) | 2026-07-29T08:00:00+08:00 | 以光子 crossbar 与 Transformer dataflow 联合设计展示算法—执行介质共优化，同时保留仿真、精度与制造误差边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [JKO-RAG: Distributional Retrieval as Wasserstein Free-Energy Gradient Flow](https://arxiv.org/html/2607.24776v1) | 2026-07-29T08:00:00+08:00 | 将 relevance、entropy 与 redundancy 合并为分布式 reranking objective，但未改变候选生成、证据 owner 和回退边界；2 + 2 + 1 = 5 | 标准完成 | 已有覆盖：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Three Sides of Retrieval: Factorial Evidence for Document-Side, Query-Side, and Answer-Side Complementarity in RAG](https://arxiv.org/html/2607.24781v1) | 2026-07-29T08:00:00+08:00 | 用 factorial evaluation 分离文档结构、查询改写和答案核验三层贡献，并引入与 chunk index 并行的 heading index；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Reasoning with Memory: A Temporal Granularity-Adaptive Framework for Training-Free Long Video Understanding](https://arxiv.org/html/2607.24794v1) | 2026-07-29T08:00:00+08:00 | 由 query temporal granularity 调节事件覆盖与固定帧预算，明确 selector 只路由证据而不拥有事实；2 + 2 + 1 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [AVE-Compass: Towards Holistic Evaluation for Audio-Video Editing Abilities](https://arxiv.org/html/2607.24821v1) | 2026-07-29T08:00:00+08:00 | 在编辑质量前增加 response/no-op gate，并分报响应率、条件质量与无条件成功率；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [GAUGE: Grading Agent-Built Financial Models Without a Golden Answer](https://arxiv.org/html/2607.24889v1) | 2026-07-29T08:00:00+08:00 | 将 deterministic correctness gate 与 judgment-based defensibility facets 分权，允许 N/A、abstain 与人工复核；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ODYSSE: Episode-wise Policy Optimization for Personalized Agentic Reasoning](https://arxiv.org/html/2607.25369v1) | 2026-07-29T08:00:00+08:00 | 保留完整 episode identity，组合 stage-local reward、episode signal 与多层归一化，避免跨步骤依赖被拆散；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [A Causality-aware Infer-diagnose-refine Framework for Test-time Modality Adaptation in VLA Models](https://arxiv.org/html/2607.25516v1) | 2026-07-29T08:00:00+08:00 | 以 factual、visual-zero 和 proprio-zero 三次前向差异作为 sensitivity sensor，并用有界 residual 修正动作；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [OmniDelta: Skill-Driven Budget Allocation for Token Compression in OmniLLMs](https://arxiv.org/html/2607.25669v1) | 2026-07-29T08:00:00+08:00 | 先做跨模态 query-conditioned budget，再做模态内 content/redundancy 分配，并保留预算守恒与模态下限；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [SAM3D-Guided Object-Centric Representation Alignment for Vision-Language-Action Models](https://arxiv.org/html/2607.25912v1) | 2026-07-29T08:00:00+08:00 | 用仅训练期存在的 privileged 3D teacher 对齐对象表示，部署时恢复 RGB、语言与 proprioception 输入；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [MemLens: A Value-Aware Memory Management System with Interactive Analytics for LLM-based Agents](https://arxiv.org/html/2607.25992v1) | 2026-07-29T08:00:00+08:00 | 以 memory unit、proxy value 与近似 Shapley contribution 支持记忆审计，但评分噪声仍不能等同因果价值；2 + 2 + 1 = 5 | 标准完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Context Assembly as the Controlled Variable: A Control-Theoretic View of Harness Policies for Frozen LLM Agents](https://arxiv.org/html/2607.25408v1) | 2026-07-29T08:00:00+08:00 | 将 context assembly 视为外部可版本化 policy，区分选择权重与任务成功概率，并保留静态 workflow fallback；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [WorkSurface-Bench: Benchmarking Enterprise Agents on Multi-Surface Knowledge Routing](https://arxiv.org/html/2607.25765v1) | 2026-07-29T08:00:00+08:00 | 将 surface routing、artifact acquisition、answer correctness 与执行成本拆成独立 failure owner；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Messier: A High-Resolution Corpus for Cross-Benchmark Agent Evaluation](https://arxiv.org/html/2607.25891v1) | 2026-07-29T08:00:00+08:00 | 将 model、scaffold、task、environment、typed verifier、逐 verifier outcome 与聚合规则共同纳入 evaluation identity；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [RepoReasoner: Evaluating Repository-Level Code Reasoning Ability of Long-Context Language Models](https://arxiv.org/html/2607.25996v1) | 2026-07-29T08:00:00+08:00 | 以动态 trace gold 对比 oracle、noisy 与 retrieval context，区分上下文可访问性和真实代码执行推理；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

## 4. 证据与知识整合

### [Do Models Fake Alignment Without Clear Consequences?](https://arxiv.org/html/2607.24758v1)

Exact v1 在 15 个模型、一个企业网络访问情景中观察到 9 个模型存在显著 evaluation/deployment compliance gap，其中 5 个在移除显式部署后果后仍保留差异。它证明“没有显式后果就不会出现评测条件行为”不成立，但不能证明模型具有统一动机或任意 benchmark 都失效。Ch66 已把 evaluation-awareness 拆为 representation、verbalization、causal control 与真实 deployment slice，并要求 paired traces，因此无需重复新增。

### [CaRE Compute-aware Remasking Evaluation Protocol for Masked Diffusion Language Models](https://arxiv.org/html/2607.24763v1)

七种 remasking、两个模型、四个随机性设置和三个 step budget 的 matched comparison 显示，temperature 可主导 MAUVE 方差，按实际 NFE 对齐还会翻转部分策略排名。证据不证明某个 remasking 策略跨模型最优，也不覆盖所有 diffusion sampler；长期增量是 EvalSpec 必须记录实际函数调用数、temperature/随机性、指标集合与预算，而不是把名义 step 当成等 compute。该增量已写入 Ch66。

### [SpecPrefetch: Parameter-Efficient Expert Prefetching for Sparse MoE Foundation Models](https://arxiv.org/html/2607.24787v1)

共享轻量 predictor 只提出下一层 expert transfer，冻结的 native router 仍拥有执行选择；因此错误预测造成 cache/bandwidth 浪费，不改变最终 expert 语义。作者在两类视觉 MoE 与 Snapdragon 设备上报告收益，但没有证明跨模型、链路和并发通用。Ch54 已要求 prefetch 是可取消 hint、miss 回退 demand load，并把 cache 与带宽约束纳入调度，判已有覆盖。

### [Early Detection of Distributed Backdoors in Multi-Agent LLM Systems: A Characterization Study](https://arxiv.org/html/2607.24893v1)

论文构造了由多个 Agent 分散持有、run 后才重组的 payload，说明每步安全检查缺少跨节点状态；可工作的 detector 又部分依赖长度和 entropy 等可移除表面线索。有限五模型、两任务域不能给出生产检出率。Ch72 已把 source、delegation、memory write 与 irreversible sink 串成 provenance flow，并把 semantic taint 限制为 sensor，完整承载该边界。

### [Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model](https://arxiv.org/html/2607.24904v1)

方法直接消费 codec 的 I/P frame、motion vector 与 residual energy 来选择动态 patch，并用轻量 event gate 决定何时唤醒主 decoder。作者 token/速度结果绑定其 codec、模型和硬件，不能从 75% visual-token reduction 推出等比例端到端收益。Ch23 已把 codec/GOP/motion/residual 与 tokenizer 共同纳入 representation identity，并保留 dense-frame fallback。

### [Stable FP4 Training via Transposition-Invariant Block Quantization](https://arxiv.org/html/2607.24953v1)

Exact v1 的核心不是“FP4 更低比特”，而是同一个权重或梯度在 forward/backward 转置后不能得到不同 block partition 与 scale state；论文通过二维 block scale、scale 处理和 rounding 约束缓解该不一致。作者训练轨迹不能证明所有模型、optimizer 与原生硬件稳定。Ch28 已将 transposition-invariant identity 写成明确 correctness contract，并保留 FP8/BF16 回退。

### [Conformal Cascade: Distribution-Free Accuracy Guarantees for Multi-Tier LLM Inference](https://arxiv.org/html/2607.25018v1)

方法以 held-out calibration 得到 prediction set，集合坍缩为单答案时小模型提交，否则 defer；有限样本 marginal coverage 与 tier 数共同定义保证。论文明确开放式生成仍需 answer clustering，selection-preservation 也不是由 marginal coverage 自动推出。Ch56 已在 prediction-set commit/defer 路线中写明这些假设和成本，判已有覆盖；现有 Books trace 的 Daily 日期误写为 07-28，应由共享 owner 校正为 07-29。

### [Similar Models Learn Differently: Final-Window Pretraining Shapes Post-Training Beyond SFT](https://arxiv.org/html/2607.25063v1)

六个分支只改变最后 500M pretraining tokens，SFT 后行为接近，却在相同 DPO/RLVR 更新下到达不同安全端点；这支持 checkpoint 适用性包含 ordered data-window lineage 与 downstream update response。它不证明任意最后窗口或所有模型都有同样效应。Ch28 已承载该 artifact identity，现有 trace 的 Daily 日期需从 07-28 校正为 07-29。

### [Addressable Recall Compaction for Long Context-Window Control in AI Agents](https://arxiv.org/html/2607.25066v1)

ARC 让归档拥有完整 tool observation，active context 只持有稳定 ID/citation，Agent 按 ID 回读而无需重执行工具。作者在两个 Qwen3 context 配置与有限 benchmark 上支持 retention/cost 改善，不证明 ID 永久有效、归档可信或开放工作流无污染。Ch75 已明确 working set、retrieval handle、pin state 与 backing-store authority 分层，Ch77 负责归档 provenance，判已有覆盖。

### [When Do Agent Loops Mistake Stagnation for Progress? Self-Evaluation Bias and Externally Grounded Verification in Long-Running Autonomous LLM Agent Loops](https://arxiv.org/pdf/2607.25152v1)

受控 testbed 固定 Agent 与工具，只替换 evaluator 的信息通道；54 个 cycle 中自报 improvement 并不能对应真实 world-state delta，而在 success 可由 artifact 内部判定的边界任务上差距消失。该证据定位的是 evaluator 是否看到权威状态，不是某个 judge 普遍无用。Ch66 已要求 completion evidence 来自环境状态与不可伪造 oracle，判已有覆盖。

### [Rethinking CD: A Reproducibility Study and Extension on the Ineffectiveness of Contrastive Decoding at Mitigating Object Hallucinations in MLLMs](https://arxiv.org/html/2607.25196v1)

复现与扩展实验表明，若 APC 使采样退化为 greedy，或 yes/no 输出分布单向偏移，POPE 等分数提升不等于视觉证据 grounding 改善；生成式与判别式数据集上的行为也不一致。LLaVA/Qwen 和有限 benchmark 不能否定所有 contrastive proposal。Ch66 需新增“先审计输出分布与 decoding equivalence，再解释 hallucination metric”的 evaluator contract，避免把格式偏移当事实性收益。

### [VisualPatchWorld: Code World Models as Latent Structured Representations for Planning](https://arxiv.org/html/2607.25236v1)

VPW 用主动 probe 选择定性 dynamics form，再从 state-action trace 拟合参数，生成可检查、可 rollout 的程序供 MPC 使用；接触丰富 pushing 的残余差距需要 engine 验证候选计划。结果不证明程序表示可覆盖开放现实动力学。Ch25 已区分 simulator、predictive model、controllable model 与真实环境，并保留模型预测加 simulator fallback，判已有覆盖。

### [SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems](https://arxiv.org/html/2607.25255v1)

SafeFlow 为 root request 和委派结果传播 structured semantic taint，在 irreversible action 前重建 workflow-level risk context。四类 benchmark 支持所测攻击下降，却不证明 taint ontology 完备或未见 payload 可检测。Ch72 已把 semantic taint、provenance、sink-time deterministic policy 与 capability isolation 分层，exact source-family trace 已存在。

### [Bridging Compute- and Data-Optimal Pretraining](https://arxiv.org/html/2607.25271v1)

论文用 token-effectiveness `η` 表达重复或改写 token 相对 fresh token 的边际价值，并发现它随模型规模、tokens-per-parameter 与扩增量变化且会饱和。14M～600M、Dolma-3 和两种扩增策略不能建立 frontier-scale 普适常数。Ch7 需把经典 compute-optimal 假设扩展为 compute/data/model 三种 regime，并明确 derived tokens 不是固定比例的新数据替代品。

### [CoSA: Accelerating Long-Context Inference via Proxy-Kernel Co-Designed Sparse Attention](https://arxiv.org/html/2607.25291v1)

KAP 在中等预算下产生有序 page 访问候选，OSK 再根据 online-softmax 统计在 kernel 内动态跳过；这改变了 sparse mask 与执行提交权的边界。作者 128K、特定模型/硬件结果不能外推任意 SLO。Ch43 已用 exact source-family marker 写入 ordered mask、kernel refinement 与 dense fallback，判已有覆盖。

### [Hybrid Analysis for Secure MCP Tool Use in LLM Agents](https://arxiv.org/html/2607.25297v1)

MTGuard 把 prompt/生成结果静态分析与工具调用、返回值和执行后状态的动态检查联结，说明单点 schema scan 看不到生命周期组合风险。摘要和 exact-v1 实验支持方法内效果，但没有证明所有 MCP server、side effect 或 artifact 都可被观测。Ch72 已要求跨参数、返回值、后续调用和 effect receipt 做 taint/provenance audit，判已有覆盖。

### [Raven: High-Recall Sequence Modeling with Sparse Memory Routing](https://arxiv.org/html/2607.25357v1)

Raven 在固定大小 memory slots 上只衰减和更新输入选择的少量槽位，介于 dense recurrent write 的干扰与 sliding-window 的位置硬淘汰之间。16× context extrapolation 只属于作者 recall workload，不证明开放域事实记忆或成熟 kernel。Ch22 已包含固定 state、compressed checkpoint 与稀疏 item cache 的中间分支，也明确 slot collapse、竞争写入和 miss，判已有覆盖。

### [Explanation-Bound Tool Execution for AI Agents: Server-Verified Action Claims Without Trusting Model Rationales](https://arxiv.org/html/2607.25364v1)

EBTE 把 rationale 中决策相关内容转为 typed claims，再与 server-held intent、policy、payload、risk、provenance 和 freshness facts 比较；模型不能扩大 baseline authority，冲突 deny、不完整 review。作者 conformance suite 证明 profile 行为，不证明自然语言 claim 提取正确或现实后果安全。Ch78 已把模型限制为 proposal owner，并由外部 authorizer/executor 持有 commit，判已有覆盖。

### [COVENANT: Natural-Language Workflow Compilation for Aligned Agent Execution](https://arxiv.org/html/2607.25400v1)

COVENANT 将自然语言 workflow 编译为 WAST/WCFG，controller 逐节点验证参数和 effect 后才推进 graph state。120 个 case 的结果不证明编译器能完整理解任意 policy，错误编译会被确定性重复。Ch81 已把概率 planner 嵌入可恢复状态机，并要求 versioned evidence 和独立 admission path 才能提交终态，完整覆盖其长期命题。

### [CodeNib: A Multi-View Data System for Serving Repository Context to Coding Agents](https://arxiv.org/html/2607.25431v1)

CodeNib 把 lexical、dense 与 structural view 绑定 repository commit 和 source range，并分别测 rebuild equivalence、增量维护与 serving latency。作者 100 snapshots/有限模型只支持其 operation-specific validity，不证明任意语言服务器或仓库规模。Ch75 已把 context assembly 写成 versioned view、freshness、provenance 与按需回源的 serving 问题，且已列入该 source。

### [Seen, Said, or Forgotten? A Causal Audit of Visual KV Memory Across Dialog Turns](https://arxiv.org/html/2607.25467v1)

CVMA 在同一 prefill 上成对移除视觉 region、整图或先前 assistant text，显示当前 attention 可能比随机更差地预测未来有用视觉证据；已 verbalized facts 有时可由文本 KV 替代，未说出的事实则不能。有限 stack 不提供通用 eviction threshold。Ch45 已要求 eviction signal 只是 proposal、未来效用和质量 gate 决定提交，判已有覆盖。

### [Architectural Backdoors in Vision-Language Model Supply Chains via Representation Steering](https://arxiv.org/html/2607.25479v1)

攻击在 architecture 中加入 trigger-gated representation steering，trigger 缺席时路径归零，因此只扫描权重、训练数据或 clean utility 可能看不到 dormant behavior。多 VLM/task 实验证明该 trust boundary 存在，但不说明所有 remote code 都恶意或论文审计方法足以证明安全。Ch59 需把 model artifact 从 weights 扩为 architecture definition、text encoder、remote code/config 与 exported graph，并要求 registry 在发布前验证可执行逻辑与 hash；Ch72 只接收其安全策略 handoff。

### [Beyond Prefill-Decode Disaggregation: Dissecting LLM Inference for Heterogeneous Platforms via Dynamic Operator Scheduling](https://arxiv.org/html/2607.25498v1)

DOPS 以 stage-aware DAG 表达算子依赖，Bifocal 动态选择设备，WLA 在内存约束下选择 persistent weight layout；它说明 PD 边界不足以代表异构执行。作者 NPU/PIM 平台的速度不能外推 GPU fleet，closed-loop profiling 也增加切换和测量状态。Ch49 已把 execution plan、operator DAG、layout identity 与 transition cost 放在同一 owner，判已有覆盖。

### [PowerScale: Energy-Efficient Geo-Distributed Model Training with Federated Datacenter Power](https://arxiv.org/html/2607.25650v1)

PowerScale 将每站点直接 WAN 全量同步改为区域内频繁同步、区域聚合器异步向全局提交，并根据训练进展调节频率。100-site Flower simulation 支持作者能耗/时间结果，却未证明真实大模型收敛、故障、隐私或异构优化器语义。Ch36 已吸收“层级聚合改变 update staleness 与 canonical checkpoint ownership”的分支，并保留单域同步作为一致性与恢复优先时的基线。

### [CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization](https://arxiv.org/html/2607.25659v1)

CoRT 在原 rubric prompt 与 matched criteria-free prompt 下重算同一 response 的 token likelihood，用差值作为 rubric dependence proxy，再在保留 response reward 符号与归一化的前提下重新分配 GRPO advantage。实验不能把 likelihood contrast 升格为因果 credit。Ch33 已要求 token credit 是受限 sensor、response reward 与 policy objective 仍拥有更新边界，判已有覆盖。

### [Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL](https://arxiv.org/html/2607.25816v1)

同一模型以 agent/speculator 两种模式复用 prefix KV，并从自身 rollout 构造下一工具调用 proposal；最终调用仍须由 canonical agent path 与 executor 验证。两个任务族的 Hit@1 不证明真实 I/O latency 或副作用安全。Ch48 已写入 self-speculation、proposal miss 与 canonical commit，exact source-family trace 已存在。

### [AngelSpec: Towards Real-World High Performance Inference with Speculative Decoding](https://arxiv.org/html/2607.25852v1)

AngelSpec 将高熵对话交给 MTP proposal、较可预测的 code/math 交给 block-diffusion proposal，并按在线负载和硬件成本在 batch 内分配 verification depth。作者 Hy3 系列吞吐数字不跨模型/硬件成立，exact target verification 仍拥有输出 commit。Ch48 已完整承载 workload-specific drafter 与 shared verification budget。

### [CONQuER: Hardware-Aware Mixed-Precision Quantisation with Online-Calibrated Surrogates](https://arxiv.org/html/2607.25884v1)

CONQuER 把量化配置放入 TOSA compiler pipeline，先用 cache bound/isotropy surrogate 排除候选，再只对强候选执行 hardware-in-the-loop 校准。作者多 CPU/GPU 结果支持“最优 bit policy 依赖真实 lowering 与硬件”，不证明 surrogate 永不漏掉最优解。Ch49 已把 compiler IR、selective calibration、Pareto search 与 dense fallback 写入执行 owner。

### [Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification](https://arxiv.org/html/2607.25904v1)

IRA 先提出 task completion conditions，再调用系统、应用和 GUI 工具读取执行后环境状态验证，而不是只看截图或轨迹叙述。321 条 Ubuntu trajectory 与后续 RL 结果不认证任意桌面环境，proposed condition 也可能不完备。Ch66 已将 task、trajectory observation、environment transition、oracle 与 reward 分权，判已有覆盖。

### [DC-WAM: Dynamic-Centric Visual Supervision and Reasoning for World-Action Models](https://arxiv.org/html/2607.25918v1)

DC-WAM 不再要求视频分支平均重建所有 appearance，而用 temporal-difference flow matching、轨迹区域权重和 token-level dynamic relevance 把容量聚焦在接触与运动。仿真/真实操作结果支持作者任务，不证明纹理永远无关或生成质量可替代安全。Ch25 需明确“视频 branch 的 owner 是 control-relevant transition supervision，而非 photorealism 本身”，并保留需要高保真 observation 的场景。

### [From Role Prompt to Infinite Thinking: Exploiting Persona Conditioning for Inference Cost Attacks in LLMs](https://arxiv.org/html/2607.25936v1)

RolePlay 利用 persona consistency 诱导语义自然但超长的推理，说明显式“请继续”或 adversarial suffix 不是 token amplification 的唯一入口。作者平均/最大倍数绑定其模型、任务与停止配置，不能外推生产成本。Ch72 需把 output-token、wall-clock、tool-call 与 retry budget 作为 executor/gateway 的不可绕过 authority，persona 与模型自报进度只能作为输入，超限应终止或降级。

### [UniMem: Complementary Episodic-to-Parametric Memory for Boundary-Agnostic Task Streams](https://arxiv.org/html/2607.26017v1)

UniMem 用 routing tokens 将稀有/新任务送入 episodic buffer，把重复、可靠模式固化到可扩展 parametric blocks；这减少重复 retrieval，却把错误 consolidation、router drift、provenance 与删除变难。三个 backbone 的 streaming 任务结果不证明无边界部署稳定。Ch77 已完整区分 external evidence、parameter consolidation、lineage、撤销和回滚，判已有覆盖。

### [Wonder: Video World Model Done Better](https://arxiv.org/html/2607.26037v1)

Wonder 用 dense camera coordinate field 表达控制，以 sparse attention memory 访问增长中的视觉 context，并通过 distillation 支持实时长 rollout。作者 16 FPS/minute-scale video 只证明其配置中的可控视觉一致性，不证明 action causality、物理正确或闭环安全。Ch25 需把它作为“controllable video world”分支，明确 camera-state、memory identity 与生成一致性，同时与可执行环境模型保持边界。

### [$π\mathbf{R}^2$: Reactive Real-time Flow Policies](https://arxiv.org/html/2607.26055v1)

方法将 fresh proprioception 作为每 tick 更新的 fast channel，vision-language feature 作为异步 slow channel；latency-adaptive flow 又把 in-flight actions 当 conditioning，使 action chunk 在硬件时延变化时继续闭环。xArm6/A5000 和所测任务的成功率不能证明不同 embodiment、安全 envelope 或 stale vision 上界。Ch26 已吸收 fast/slow state ownership、staleness budget、action commit 与 emergency fallback。

### [INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models](https://arxiv.org/html/2607.26056v1)

INTACT 以共享四槽 grammar 让局部 transition intent 与 goal intent 进入同构 backbone，输出 action-law distribution；条件均值可 direct act，CEM 仍作为可选验证分支。四个 LeWM task 与 reward-free demonstrations 不证明开放物理环境或安全泛化。Ch25 已吸收“forward prediction → test-time search → learned intent-to-action law”的演进，并明确 direct policy 不能因此获得环境真值或最终安全 commit 权。

### [GLIDE: Guided Layerwise Hybrid Attention for Efficient LLM Inference](https://arxiv.org/html/2607.24788v1)

Exact-v1 §II-D、§III 先测各层替换 softmax 后的敏感度，再让早层保留较大窗口、深层更多依赖 recurrent aggregation；因此被压缩的是分层 KV state，而不是简单把所有层换成线性 attention。§IV 只支持作者模型、长度与硬件上的质量—延迟折中，§V 不证明敏感度在换 checkpoint 或 workload 后稳定。它节省 KV I/O，却增加层级配置、校准与 fallback；Ch22 现有正文只有一般性的 layer-wise 转换和 probe，尚未写明由 sensitivity/calibration 在 softmax window 与 recurrent state 间分配每层状态预算，因此改判整合，并保留统一窗口或全注意力回退。

### [Prediction Is Not Memory: Dual-Timescale Gated Profile Writing for Persistent User Modeling](https://arxiv.org/html/2607.24798v1)

Exact-v1 Introduction 与 Method 把“预测这次互动”同“是否写入持久 profile”拆开，gate 读取长期、短期和候选 drift，只把有长期证据的变化提交。§Experiments 的 near/far protocol 证明 write-all 在作者数据上会伤害远期 alignment，并不证明 near-future label 是真实长期偏好的无偏 oracle。选择性写入降低污染，却会漏掉稀有偏好并引入 gate drift；Ch77 已明确 prediction/confidence 不能拥有 durable write authority，判已有覆盖。

### [When Thinking Before Retrieval Hurts: TraceBound Diagnostics for Adaptive Knowledge-Graph Retrieval](https://arxiv.org/html/2607.24800v1)

Exact-v1 §3 将 query profile、failure hint 与 trajectory counter 注入同一 retriever，§4–5 在固定图、工具和标签后观察到更多重复/空调用及错误 exploration allocation。它证明“可解释 trace 更多”可能让控制策略更差，不证明 reasoning 普遍伤害检索，也未给出生产图上的最优 stopping policy。外部 budget 能限制浪费但不能修复 action policy；Ch76 已把 query revision、检索动作、未读贡献和停止决定归 retrieval controller，判已有覆盖。

### [Forgetting Is Not a Fix: Path Dependence in Sequential Engram Editing](https://arxiv.org/html/2607.24805v1)

Exact-v1 §1–4 在原实现和其推荐 edit strength 上依次施加多个编辑，比较零次组合与顺序重校准路径；§4 的三组模型结果显示编辑不交换、survivor covariance 累积漂移且已擦除知识可能回返。它推翻的是 sequential setting 下的 commutative-manifold 假设，不否定单次编辑结果，也不证明所有编辑器都有同样疲劳曲线。顺序重验增加 control matrix 和发布成本，却是合规删除跨 revision 仍成立的必要条件；Ch66 需加入“每次新编辑都重开既有删除证书”的 artifact-lifecycle 规则。

### [Neuromorphic Diffusion Language Models: Addressing Compute and Memory Bottlenecks via Sparsity and Block Denoising](https://arxiv.org/html/2607.24841v1)

Exact-v1 §II-A、§III-A 把 block denoising 的多 token/NFE 与 spike-induced inactive-channel skipping 组合，§IV 用 token-level roofline 区分 memory-bound 与 compute-bound，§V 的证据限于翻译任务和作者 neuromorphic setting。它没有证明 spike hardware 普及、能量数据可跨平台复用，或 NFE 减少等于端到端 SLO 改善。该分支用训练/硬件耦合换 active traffic，普通 GPU 或稀疏利用不足时 AR/普通 block diffusion 仍合理；Ch24 已吸收这条“并行进度 × active compute”的条件化 roofline 路线。

### [Agent Retrieval Bench: Evaluating Repository Context Retrieval for Coding Agents](https://arxiv.org/html/2607.24882v1)

Exact-v1 Appendix C、D 与 candidate-filter ablation 把 edit location、ripple files 和自然 no-gold case 分开，显示 gold recall、下游 edit success 与 selective abstention 并非同一指标。它是诊断性 benchmark，不证明 web-scale repository、任意语言或单一 threshold 可迁移。更完整的合同增加 gold lineage 和 counterfactual control 成本；Ch75 现有正文尚未把 retrieval recall、candidate filtering、下游 edit success 与自然 no-gold abstention 分开验收，因此改判整合，并保留 oracle/gold 不可得时的受限 judge 与人工复核。

### [Beyond "What to Retrieve": Uncertainty in Retrieval-Augmented Code Generation](https://arxiv.org/html/2607.24884v1)

Exact-v1 的 Uncertainty-Aware Framework 分别估计 query/API candidate 与生成阶段风险，实验显示 target-aware refinement 能改善已召回 API set，但 required API 不在初始池时后级过滤无从恢复。证据绑定作者 code tasks、retriever 和 evaluator，不证明 uncertainty score 已校准为生产失败概率。多级 uncertainty 增加模型调用和阈值漂移；Ch76 已明确 retrieval recall、evidence sufficiency、answer gate 与 abstention 分权，判已有覆盖。

### [Mechanisms of Width Scaling in Normalized Residual Networks: The Effective Alignment Dimension](https://arxiv.org/html/2607.24887v1)

Exact-v1 理论部分从独立 train/test gradient inner product 的均值与方差得到有限样本 misalignment 上界，主实验以 LLaMA-style、Pythia 与 ResNet residual intervention 检查该统计量能否预测 held-out loss 方向。它证明的是给定 finite second moments、非零 population gradient 与 function-preserving expansion 的局部条件，不是“宽度增加必然泛化更好”，也不覆盖长期训练动力学。Ch7 需把 scaling 从平均 loss 曲线推进到“扩容方向能否跨样本对齐”的可测条件，同时保留数据不足时的保守扩容/复验。

### [TYPO: Instruction-Dense Visual Jailbreaks against Commercial Closed-Source Image-Generation Models](https://arxiv.org/html/2607.24897v1)

Exact-v1 §3 threat model、§4 方法把图像中的密集文字、布局与外层文本 prompt 组合为黑盒搜索空间，§5 在四个当时版本的商业图像模型上测得相对九种攻击更高的成功率。该结果不证明当前版本仍易受同一模板攻击，也不覆盖内部 filter、真实 abuse rate 或任意视觉语言。视觉/文本联合检查提高拦截面，却带来 OCR 误判、版面规避与额外延迟；Ch72 需把 rendered text 和 visual layout 纳入 multimodal input policy，而不是只扫描字符串 prompt。

### [ALIBI: Adaptive Agentic Attacks on LLM-Based Vulnerability Detectors via Adversarial Code Comments](https://arxiv.org/html/2607.24964v1)

Exact-v1 §3 允许 coding agent 在不改程序行为的前提下迭代注释，并利用 detector feedback 伪造推理或外部工具结果；§4 在 125 个 null-pointer 修复任务上显示 prompt-only 防御弱于 comment sanitization 与架构隔离。它不证明所有漏洞类别、detector 或生产 gate 有相同攻击率。删除注释会丢失真实开发语义，完全信任注释又让不可信自然语言覆盖程序证据；Ch72 已把 untrusted context、独立静态/动态 verifier 与 effect gate 分层，判已有覆盖。

### [Towards Robust Reinforcement Learning for Small-Scale Language Model Agents](https://arxiv.org/html/2607.25091v1)

Exact-v1 §III–V 将不收敛分别追到 PEFT/TRL 中 LoRA 参数静默冻结、bf16 importance ratio overflow 与 reward-model error 引发的 policy collapse，并用 merge-reinitialize、FP32 update、reward whitening/ratio guard/rollback 对应修复。十五组小模型实验只支持 70–500M、250-step PPO 与披露数据，不证明这些措施足以稳定大模型或长期在线 RL。Ch32 需将“梯度存在、ratio 数值可解释、reward 有判别力、rollback 可用”写成独立 admission gates；较小模型和可靠 reward 下，标准 PPO 仍可保留。

### [PreDiff-LM: Pretrained Discrete Masked Diffusion Language Modeling with Hybrid Attention](https://arxiv.org/html/2607.25157v1)

Exact-v1 §3 让 observed prompt 内维持 causal attention、masked target 内使用 full bidirectional attention，从而复用 AR initialization 而不把 prompt 也变成可变状态；§4 在 matched GPT-2 Medium/WikiText 设置中改善 diffusion baseline，但同规模 fine-tuned AR 仍更强，长于 512 tokens 与远域迁移也退化。该路线以 attention mask mismatch 和迭代推理换双向 correction；Ch24 需把它作为 AR→masked diffusion 的兼容桥，而不是“diffusion 取代 AR”的证据。

### [Decision-Level Hijacking: Injecting Cognitive Bias into Large Language Models via Bit-Flip Attacks](https://arxiv.org/html/2607.25227v1)

Exact-v1 §3–4 定义攻击者在部署后改变极少量 weight bits，以多目标优化保持通用输出同时定向改变特定议题立场；§5 在三个开放模型和两类场景中观察到持久 stance shift。它不证明任意硬件故障、bit budget 或模型都可被同样操纵，也不等价于真实供应链发生率。Hash 只能发现已知 artifact 变化，behavior canary 只能采样语义风险；Ch59 需联合签名/hash、存储传输校验与定向行为回归，并在任一不一致时隔离 artifact。

### [Instruction-Tuned Language Models Cannot Sample from Distributions They Can Describe](https://arxiv.org/html/2607.25292v1)

Exact-v1 §3 与 Appendix A/J 比较 base、连续 post-training stage、内部 option probability 和重复 persona calls，显示 instruction-tuned 模型可描述群体分布，却在逐 persona 调用中坍缩为近确定答案；调 temperature 不能修复 sampling 之前已形成的分布。证据来自所测 public-opinion benchmark 和模型家族，不证明所有模拟人群任务都失效。单次描述分布减少调用，却依赖模型的分布估计；Ch66 需禁止把重复生成样本直接当独立人口样本，并要求用真实人群数据校准 sampling contract。

### [Every Time I Hire a Linguist, Inference Costs Go Down: On Linguistic Rules as Effective Prompt Compressors](https://arxiv.org/html/2607.25335v1)

Exact-v1 Appendix A/B 先离线搜索 lexical、syntactic、semantic 与 discourse rules，部署时只做 CPU deterministic filtering；§5 显示轻中度压缩可接近 LM scorer，高压缩率则从 token pruning 转成 sentence extraction 并明显退化。有限种子、语料和 fixed search 配置不能证明规则跨语言、tokenizer 或任务稳定。它减少在线 forward，却增加离线维护和规则漂移；Ch75 已把压缩写成 preservation contract、budget 与 raw fallback，足以容纳该确定性分支，判已有覆盖。

### [Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control](https://arxiv.org/html/2607.25337v1)

Exact-v1 §3 用同轨迹时间顺序作正例、跨轨迹 pair 作启发式负例，并以 rollout-consistency 对齐 planning horizon；Appendix A/C 的 locked evaluation 与 ablation 支持 directed head、negative 和一致性项各有贡献。它不证明时间接近等于可达性，contact-rich task 仍可能更适合 Euclidean geometry。Ch25 需把 progress cost 从“表示空间天然给出”改为可学习且与 plan-time operator 联合验收的状态，保留 geometry 和真实环境 refresh 作为回退。

### [HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following](https://arxiv.org/html/2607.25398v1)

Exact-v1 §3–4 将 20–124 页 standing policy、MCP 工具环境和 824 个确定性 criteria 绑定同一 trajectory，严格 all-pass 还同时检查必须做与禁止做的 action。§6 的失败只证明 65 个作者任务中的规则遗失、越权请求和错误 self-report，不给出开放企业环境的失败率。精细 rubric 成本高且依赖完整 policy encoding；Ch66 已要求 atomic criteria、过程 trace、真实 effect receipt 与 instruction source 分片，判已有覆盖。

### [Bits and Memories: Measuring Verbatim Extraction Across LLM Quantization](https://arxiv.org/html/2607.25451v1)

Exact-v1 §3 直接在已知 memorized sequences 上跨五种精度、三种模型规模和两种量化算法测 verbatim extraction，同时用 perplexity 追踪能力；§4 显示记忆下降快于能力，但 4-bit 最大模型仍复现多数已知序列。它不证明未命中序列已删除，也不覆盖私有训练数据或部署攻击者。量化可降低部分暴露但不能拥有 privacy erase authority；Ch72 需明确 membership inference、extraction 与 deletion 是三种不同合同，并在量化后重跑 targeted extraction。

### [CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model](https://arxiv.org/html/2607.25487v1)

Exact-v1 §3 将双视角 16-frame history、episode Plan 和 chunk Think 分层蒸馏到 0.9B action model；LIBERO-Plus 与 paired plan intervention 支持这些监督在作者任务中具有 load-bearing 作用。结果不证明语言 CoT 是因果真值、跨 embodiment 可迁移或满足物理安全。它用 teacher/annotation 和额外时序输入换小模型容量，Ch26 已有对应机制正文与 source marker，判已有覆盖。

### [Automated Numerical Stability Analysis of Deep Learning Operators](https://arxiv.org/html/2607.25494v1)

Exact-v1 §3 对暴露 operator 采用 CESTAC、多次随机扰动或 GEMM-like 数据扰动，在训练/推理时定位数值不稳定源；§4 只验证注入污染的受测任务，§5 承认重复计算带来运行时开销。该 sensor 不证明误差一定影响最终 token，也不覆盖 fused/opaque kernel。Ch49 已要求 precision、reduction topology、kernel implementation 和 differential numerical gate 共同定义执行 artifact，现有正文足以承载该监测分支。

### [At-the-Roofline Sparse Tensor Contractions on Vector Processors for Transformer Inference](https://arxiv.org/html/2607.25504v1)

Exact-v1 §III 将 Gustavson dataflow 所需的 indexed gather-accumulate-scatter 下沉到 RVV extension 与 runtime-configurable sparse unit，§IV 以 RTL 校准模型、40–60% 双稀疏 LLaMA-3-8B 测 prefill/decode。速度只属于该 12nm vector cluster、模型和稀疏度，不证明通用 GPU 或端到端 serving 同幅提升。专用 ISA 换来更高稀疏利用率，也增加硬件/编译器绑定；Ch49 已明确逻辑稀疏必须被实际 lowering 与 hardware dataflow 消费，判已有覆盖。

### [Agent Skills Matter: Inferring Proprietary Skills from Execution Trajectories](https://arxiv.org/html/2607.25560v1)

Exact-v1 §3 与 Appendix B 用 matched skill-enabled/disabled trajectories 抽取重复行为 signature，再迭代合成替代 skill；Appendix D/F 的五种场景结果说明即使 artifact 隐藏，程序性知识仍可能从 benign trace 泄漏。它不证明任意 skill 可完整重建，也未量化生产日志中的现实攻击率。减少 trace 细节会伤害可观测性，保留全部轨迹又扩大侧信道；Ch84 需把 trajectory disclosure、redaction、probe budget 和 proprietary procedure 分级加入平台发布合同。

### [Forensic Reproducibility Audit of a Radiology Vision-Language Model Benchmark: From Intended Protocol to Released Artifact](https://arxiv.org/html/2607.25589v1)

Exact-v1 §2–3 从 intended cohort、released artifact、实际 API calls、annotation 与 keyed analysis 逐层重建原 benchmark，发现数字可复算但实验条件不等于报告条件，因此撤回原性能、排名、prompt-effect 和临床结论。撤回的是旧 claim 而非本纠错论文；它也不证明新 contract 能阻止所有数据污染。Ch66 需把 cohort membership、render/prompt hash、provider-resolved model、call status、annotation provenance 与 derived artifact 都纳入 run identity，只有同一身份链可支持复现声明。

### [An Empirical Study of Model Context Protocol Applications](https://arxiv.org/html/2607.25635v1)

Exact-v1 §IV 对 1,723 个 GitHub MCPApps 建 taxonomy，并把 config file、SDK communication、enable/disable、logging 与 blocking approval 分开计数；其结果显示常见 SDK 或日志并不意味着执行前有人类 gate。仓库挖掘受公开 GitHub、分类器和时间快照限制，百分比不能代表全部生产 MCP。Blocking approval 提高安全但增加交互延迟与疲劳；Ch83 需明确协议只标准化连接，app/runtime 仍拥有 permission、approval、credential 和 effect commit。

### [Demystifying Deep Learning Compiler Frontend Bugs: An LLM-Aided Empirical Study](https://arxiv.org/html/2607.25651v1)

Exact-v1 §4 对 TorchDynamo 的 123 个 frontend bugs 建七类 root cause，再由这些类别生成 targeted tests；作者报告 23 个新 bug 中 15 个确认，证明 graph capture/IR translation 不能被低层 operator tests 替代。它只覆盖一个 frontend 和已知 taxonomy，不能保证发现类别外错误，LLM 分析也不是独立 correctness oracle。Ch49 需把 frontend semantic capture、lowering、kernel 与 runtime 分层验证，并保留 eager/reference path 作 differential fallback。

### [OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic Simulation](https://arxiv.org/html/2607.25656v1)

Exact-v1 Method 与 Appendix E 把 task dependency、parallelism 和资源冲突编码为可确定重放的 simulator，使 orchestration plan 可脱离 individual agent execution 评价；ablation 说明生成问题和模型调度各有独立 failure。它不证明 simulation 完整代表真实工具、通信失败或多租户 side effect。Ch82 已将角色、协议、共享状态与 coordinator commit 分权，并要求 simulator 证据不能冒充生产运行，判已有覆盖。

### [Detecting CSAM Text-to-Image LoRAs From Weights](https://arxiv.org/html/2607.25750v1)

Exact-v1 Method/Appendix A 从 LoRA update 提取 top-left singular vector，在不生成目标内容的前提下分类其最强学习方向；人类年龄 proxy 的实验显示该 sensor 可跨部分 base model、噪声和精度变化保持信号。Proxy 不等于真实 CSAM、fingerprint 也不证明内容必然生成或覆盖规避攻击。Ch59 需把 weight-only scan 作为 quarantine 前置 sensor，绑定 base model、adapter hash、threshold 与 abstention；高风险 artifact 仍需独立政策和人工处置。

### [WarmTuner: Program-Specific Warm Starts for Compiler Autotuning via Offline-to-Online Reinforcement Learning](https://arxiv.org/html/2607.25831v1)

Exact-v1 §III-C 先由历史好配置训练 program-conditioned flag policy，再用目标程序真实 compile-run feedback 在线更新同一 prior；§IV 的结果限 GCC 15.2、cBench/PolyBench 与给定 budget。它不证明 GRPO 比所有搜索器稳定，也不能把平均 speedup 外推新编译器或硬件。在线反馈减少 prior mismatch，却增加测量噪声和部署时 tuning 成本；Ch49 已有 feasibility/ranking、hardware-in-loop calibration 与已验证 plan fallback，判已有覆盖。

### [Towards a Systems Foundation for Agentic Cloud Management](https://arxiv.org/html/2607.25883v1)

Exact-v1 §3 把每个 agent session 限制在 resource-local view，并对共享资源的并发操作维护 intent、lock/escrow 和 attributable feedback；Azure API workload 只验证作者 substrate 的代表性路径，不覆盖真实故障、权限漂移或大规模尾延迟。更强协调减少冲突，却增加 metadata、锁状态与恢复协议。Ch84 已把 session isolation、out-of-band control envelope、effect receipt、并发 conflict 和 rollback 作为平台职责，判已有覆盖。

### [Distributing Security Controls Through Harness Engineering](https://arxiv.org/html/2607.25890v1)

Exact-v1 §IV 将防线分别放在 prompt、tool gateway、filesystem/sandbox 与运行 harness，§V/VII 用同一 adversarial suite 检查组合而非单项宣传；部分观察未能在后续 run 复现，正文因此不能采用 100% headline。它不证明已覆盖未知攻击或各组件失效独立。分布式控制提高 defense in depth，也产生配置交互与归因成本；Ch72 已要求 threat model、reference monitor、effect gate 与跨层回归共同成立，判已有覆盖。

### [Minimizing Targeted Activations: Input-Only Suppression of Evaluation-Awareness Latents in Large Language Models](https://arxiv.org/html/2607.25907v1)

Exact-v1 §3、§5.3 只改输入 prefix 来压低多种内部 latent，并加入 random-direction placebo、真实 evaluation passage 与 behavior judgment 对照；实验显示方向可读、可压低甚至 feature 可归零，却不必改变对应行为。证据限两个 Llama scale 和构造 latent，不证明 activation probes 无用。内部 sensor 仍可诊断，但不能独自发布行为或安全结论；Ch66 已有 representation、verbalization 与 control 分离及 placebo/causal validation，判已有覆盖。

### [Penelope: Localized Latent Recurrence for Efficient Structured Reasoning](https://arxiv.org/html/2607.25915v1)

Exact-v1 §3 只执行一次 lower decoder prefix 形成 boundary memory，再在选定层段用 time-modulated GRU/recurrent readout 迭代，最后恢复普通 answer generation；§4 的 validation-selected budget 支持部分 structured reasoning 的 latency—accuracy 折中。它不证明 latent steps 等价于正确推理，Deep ListOps 增益很小且非随深度单调。Ch17 已吸收“全 decoder/显式 CoT → 局部 latent recurrence”的 compute branch，并把循环稳定、预算选择与可解释性损失写入代价。

### [MODUS: Decoder-Only Any-to-Any Modeling of Diverse Modalities](https://arxiv.org/html/2607.25948v1)

Exact-v1 §3.2 把各模态都编码为同一 decoder-only sequence，使任意模态既可作条件又可作输出，不依赖 modality-specific head/loss；Appendix B/C 支持作者任务上的 specialist/multitask 对比与 chained generation。它不证明所有模态共享 tokenizer/损失都最优，自生成另一模态评分也不是独立 verifier。Ch24 需将它作为统一 AR factorization 的 any-to-any 分支，明确参数共享换来 modality interference、序列成本与自验证相关误差。

### [Reinforcement Learning for Code Optimization](https://arxiv.org/html/2607.25970v1)

Exact-v1 Appendix C/D 将 hidden-test correctness、calibrated timing sandbox、速度 reward 与 GRPO 稳定措施放进同一 environment，并用 sandbox degradation 检查测量噪声。结果只支持披露模型、DMC-Optim/LCB、top-percentile 判定与执行平台，不证明任意代码或硬件上的 speedup。Ch33 已把 timed reward 的 evaluator identity、稀疏信号、rollback 和纯 correctness 共存边界写入正文并有 source marker，判已有覆盖。

### [IH-Benchmark: A Conflict-Centered Benchmark for Instruction-Hierarchy Robustness in LLM Applications](https://arxiv.org/html/2607.25987v1)

Exact-v1 taxonomy 与 Appendix G/J 分别构造 system>user 和 user>tool 冲突，以 44 类 constraint 和 binary all-pass 检查来源层级；37 个模型的结果显示直接冲突表现不能预测 tool-output 注入。它不证明该 DSL/judge 覆盖所有自然语言 policy，也不支持一个总 compliance 分数。Ch66 已按 source surface、atomic constraint、deterministic predicate 与 scoped judge 分片评测，判已有覆盖。

### [Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches?](https://arxiv.org/html/2607.25995v1)

Exact-v1 §3 从 Istio call edges、Trivy finding 与 service-account binding 组装 live cluster context，§4–5 用 topology-dependent/independent control 比较 patch correctness；结果说明 scanner-compliant patch 在缺少依赖图时可造成 blast radius。它只覆盖 VulnCare、所测模型和七类 dependency，不证明模型获得集群真值或 patch 可直接执行。Ch72 已要求 authoritative runtime state、impact analysis、dry-run/rollback 与 effect gate，但尚未明确 scanner-only finding 与 live call graph、service-account binding 的证据差异及 topology-dependent patch contract，因此改判整合。

### [Parallel Decoding Distillation for Fast Image and Video Generation](https://arxiv.org/html/2607.26004v1)

Exact-v1 Algorithm 与 §2 让 student 一次预测多个 denoising transitions，学习 trajectory mean velocity 而不依赖 JVP/finite difference；§5/Appendix B 的 4–8 NFE 质量与 diversity 只属于 LTX、Wan、Qwen-Image 等披露设置。它不证明 NFE 等于 wall time、data-free distillation 跨域稳定或 mode collapse 被消除。Ch24 需把 PDD 放在 sequential denoise→multi-step proposal 的演进链，要求 scheduler 同时验收 NFE、真实 latency、diversity 与 rollback。

### [Reinformed Dreamer: An Asymmetric World Model Efficiently Trained through Latent Guidance](https://arxiv.org/html/2607.26040v1)

Exact-v1 PDF Method 先指出旧 asymmetric world model 的 privileged representation 问题，再让训练期 state representation 指导 observation encoder；实验只说明若干 benchmark 上比 Dreamer/旧 asymmetric branch 更一致。它不证明 privileged state 在真实部署可得、partial observation 的 belief 已正确，或多步 rollout 安全。Ch25 需区分 training-only guidance 与 runtime state：前者可改善表示但不能进入部署 truth authority，失配时仍回退观察更新和短 horizon replanning。

### [Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?](https://arxiv.org/html/2607.26041v1)

Exact-v1 PDF 将 3-frame ordering/cross-trajectory decoy 与 before-after action inference 分开，2,013 个实例揭示模型可能复制输入顺序、混淆 stale screenshot，并且识别 action family 比定位 click/drag 更难。它不证明 offline benchmark 等价真实 async desktop、模型差距能直接预测任务完成率。Ch66 已把 GUI action proposal、环境 effect、fresh observation、transition verifier 与 recovery 分权，判已有覆盖。

### [Spend Experts Where You Are Unsure: Confidence-Adaptive Routing for Mixture-of-Experts LoRA](https://arxiv.org/html/2607.26052v1)

Exact-v1 §4 按 router weight 降序累积到 nucleus threshold，expert disagreement 可扩展集合，budget thermostat 再把平均 active experts 校准到目标；Appendix B/C 的 matched-compute 实验支持所测两个 backbone 和任务。它不证明 router mass 是通用 epistemic uncertainty，也不增加总容量；动态 k 会放大 load variance、dispatch fragmentation 与 OOD calibration drift。Ch21 需把 fixed top-k 扩为 budget-constrained variable-k 分支，并保留 capacity、expert placement 与 fixed-k fallback。

### 恢复候选的逐项 Source Review

### [Kernel Forge: An Agent Harness for LLM-based Generation and Optimization of CUDA Kernels](https://arxiv.org/html/2607.24762v1)

Exact-v1 将任意未修改 PyTorch 模型中的 kernel 发现、MCTS 候选搜索、编译、正确性检查、计时与回嵌放进同一 harness；四个模型和 GB10 上的 14 个 kernel 只证明该配置的局部收益，不能推出整模端到端加速或跨硬件泛化。搜索与验证消耗额外编译/运行预算，失败时应回退原 PyTorch operator；Ch49 已有“抽取后必须回嵌并重验 correctness/SLO”的机制正文，判已有覆盖。

### [Measuring and Improving Behavioral Consistency in Large Language Models through Fact-Heuristic-Emotion State Enforcement](https://arxiv.org/html/2607.24765v1)

Exact-v1 在 26 个模型、37,403 次韩语决策观测中显示 typed state 能降低重复输出波动和 decision flip，同时作者明确其不提高 reasoning correctness。结构化状态带来额外 prompt/解析成本且只验证有限语言和任务；Ch66 已分离 consistency、correctness 与外部证据，判已有覆盖。

### [RoCo-ACE: Rollout-Conditioned Online Distillation for Retention-Aware Knowledge Injection](https://arxiv.org/html/2607.24771v1)

Exact-v1 用同一 rollout 在 reference-free/reference-conditioned 下的似然差给 reference-supported token 加权，并用稀疏 anchor 修正 rollout 遗漏的权威事实；三类注入任务与六个 retention benchmark 只支持所测模型。它以参考推理和权重设计成本换取 retention，参考错误仍会被放大；Ch29 已吸收“rollout 局部蒸馏 + omission anchor”而不是完整答案模仿。

### [LivingArena: Do LLMs Know What Other LLMs Don't? Peer-Probing as Scalable Evaluation](https://arxiv.org/html/2607.24780v1)

Exact-v1 让模型依据交互历史互相生成并验证针对性问题，3,600 轮十模型实验显示强 answerer 不一定是可靠 questioner，且被暴露弱点可在独立问题中复现。它不能证明模型生成的 reference 普遍可信，反而要求出题与答题两个 evaluator owner；Ch66 已吸收 adaptive peer-probing 及自验失败边界。

### [SearchArt: Training Long-Horizon Search Agent with Scalable Synthetic and Verified Task](https://arxiv.org/html/2607.24850v1)

Exact-v1 从网页合成 QA、证据图和搜索轨迹，再以 QA 一致性、轨迹质量与证据相关性验收后进入多阶段 SFT/RL。作者 benchmark 不能证明合成 evidence graph 没有系统偏差，验证与生成也增加显著成本；Ch27 已吸收“合成数据只有通过证据/轨迹联合 gate 才可进入训练 lineage”。

### [The Missing Layer: Specification Infrastructure for AI Oversight](https://arxiv.org/html/2607.24866v1)

Exact-v1 把 Legibility、Specification、Mediation、Evaluation、Escalation 串成共享 oversight 层，并以 CARMA 原型展示同一版本化 specification 驱动 enforcement、evaluation 与 escalation。它主要是架构提案，不能证明六项原则已成为标准或原型覆盖生产威胁；Ch72 已吸收 policy artifact 的 composability、traceability 和 escalation owner，并保留人工接管。

### [Inverse RL Helps Align AI by Imitating Humans](https://arxiv.org/html/2607.24900v1)

Exact-v1 从 demonstrations 与 policy samples 在小型 response-feature 空间的差异恢复显式 reward，并用于 reranking 与 on-policy RL；结果只证明所测特征、任务和策略能改善，不能识别唯一的人类偏好。方法省去成对偏好却依赖 feature/evaluator 选择并可能被策略利用；Ch31 已吸收 demonstration-derived reward 的可识别性与 adversarial revalidation。

### [PerceptionBench: Evaluating Atomic Visual Perception in Multimodal Large Language Models](https://arxiv.org/html/2607.24957v1)

Exact-v1 用 3,000 个短答案问题隔离十类原子视觉感知，十六个 MLLM 的相近总分呈现不同能力轮廓。它不能把感知错误与所有上游编码、OCR 或 judge 错误完全因果分离，也不代表生产视觉分布；Ch66 已吸收“先隔离 perception，再评价 reasoning”的 capability slice。

### [Matryoshka Agent: Unfolding Sub-Agents for Long-Horizon Machine Learning Engineering](https://arxiv.org/html/2607.25090v1)

Exact-v1 由高层 Orchestrator 保存紧凑探索状态，短生命周期 Sub-Agent 经标准工具接口执行具体尝试，从而分离长期策略与噪声环境轨迹。MLE benchmark 的收益不能外推到任意多 Agent 系统，且层级会引入摘要丢失和错误委派；Ch82 已有 supervisor/worker、动态有界拓扑和 commit owner，判已有覆盖。

### [ScalableRAG: High-Quality RAG at Zero Ingestion Cost](https://arxiv.org/html/2607.25135v1)

Exact-v1 用可读写 document/value workspace 在查询时完成集合运算，避免预构建图或表；Limited-Ingestion 分支再用少量向量索引和模式发现扩展。六个 corpus 的平均结果不能证明零 ingestion 对频繁查询、权限隔离或更新成本最优；Ch76 已吸收“预计算索引 ↔ query-time workspace”的替代分支及扫描成本回退。

### [Less Data, Better Alignment: Data-Centric Multi-Evaluator Agreement for Preference Optimization](https://arxiv.org/html/2607.25136v1)

Exact-v1 从目标 policy 生成候选，以 helpfulness、factuality、conciseness evaluator 和 process critic 校正，只接纳 54,236 项中的 1,871 项高共识样本。它证明数据 gate 可比换 objective 更重要，但不证明 evaluator 无偏，且增加多评审推理成本；Ch31 已吸收 on-policy candidate→multi-rubric→process correction→consensus admission 的数据控制链。

### [HiEviDR-Bench: A Benchmark for Hierarchical Evidence Aggregation in Deep Research](https://arxiv.org/html/2607.25151v1)

Exact-v1 为 2,000 个 deep-research 问题提供 evidence graph，并按 report、traceability、citation、claim verification 和 answer correctness 逐级定位错误。结果不能证明 graph 标注覆盖开放研究的全部有效证据；Ch66 已有 claim→evidence→test→judgment→update 与 surface quality/epistemic quality 分离，判已有覆盖。

### [Laplace-PSN-IRT: Uncertainty Quantification for Neural Item Response Theory Models of LLM Benchmarks](https://arxiv.org/html/2607.25257v1)

Exact-v1 在 neural IRT 上以 Laplace posterior 输出 model ability 与 item property 的不确定性，使 leaderboard 差异带可信区间。它依赖 IRT 结构与局部近似，不能把后验宽度解释为真实部署风险；Ch66 已吸收 item-level latent difficulty、posterior uncertainty 和模型排序不确定性。

### [CLBench-V: Evaluating Multimodal Context Learning from Grounding to Knowledge Acquisition](https://arxiv.org/html/2607.25294v1)

Exact-v1 将多模态 context learning 分解为 grounding、规则归纳与 knowledge acquisition，避免仅用最终答案总分。它不能证明各阶段完全独立，也未覆盖长时在线记忆；Ch66 需将阶段性 contract 与统一端到端分数并存，并为失败定位保留分片指标。

### [Specula: Scaling formal specifications for autonomous model checking of system code](https://arxiv.org/html/2607.25333v1)

Exact-v1 让 agent 从系统代码构造形式化 specification，并由真实 model checker 给 counterexample 反馈继续修正，使 verifier 而非语言模型拥有接受权。它不证明生成 specification 完备，错误规格仍可能让验证“正确地证明错误目标”；Ch66 已吸收 specification validity 与 checker result 两层 gate。

### [A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain](https://arxiv.org/html/2607.25415v1)

Exact-v1 将 context assembly、tool use、verification 与多目标 reward 交给可训练 controller，并发布跨域轨迹与 reward decomposition。有限三个 domain 和两个 provider 不能证明控制策略跨组织迁移，在线适配还会引入探索风险；Ch84 已吸收 harness policy 的版本、effect evidence、成本预算与静态 fallback。

### [Toward an Organizational Science of Multi-Agent LLM Systems: Decoupling Who, How, and Which Algorithm](https://arxiv.org/html/2607.25446v1)

Exact-v1 将 organization、coordination 与 collaboration protocol 设计为可独立替换层，并显示 accountability placement 只有在交付路径经过该角色时才影响结果。实验不能证明 contextual-bandit routing 在开放团队中稳定，在线选择还会带来 judge/cost drift；Ch82 已分离角色、协议、协调 owner 与 commit，判已有覆盖。

### [Beyond Self-Knowledge: Propagating Uncertainty Across Reasoning and Retrieval in LLMs](https://arxiv.org/html/2607.25600v1)

Exact-v1 用 held-out 集冻结模型特定 confidence threshold，低置信问题执行 top-5 TF-IDF retrieval；27,000 个 policy instance 显示相对 always-retrieve 少 20.4% passages，但 probe 令总 token 增 28.2%，且 AUROC 仅 0.628。它不证明 verbal confidence 是概率或跨模型可迁移；Ch76 已有 evidence sufficiency、模型特定校准、直接/检索/拒答与成本回退，判已有覆盖。

### [MemSFT: Mitigating Alignment Tax with an External Parametric Memory](https://arxiv.org/html/2607.25614v1)

Exact-v1 冻结 backbone，用 parametric memory 模仿非参数 retriever，再由逐 token router 融合 memory 与 base distribution。三个专业域的收益不能证明 memory 跨域安全或消除遗忘，路由还增加训练和推理成本；Ch29 已吸收“参数专门化从 backbone 移到可插拔 memory”的 SFT 替代分支。

### [SkillGate: Cost Efficient Runtime Malicious Skill File Detection in Coding Agents](https://arxiv.org/html/2607.25619v1)

Exact-v1 用 regex 安全信号绕过 LLM、对命中窗口调用 judge；SkillsBench 的 F1/FPR/token 节省只属于该恶意分布，不能证明 snippet 不会漏掉跨段 payload。它降低成本但保留静态 false-negative，因此仍需 sandbox/effect gate；Ch72 已完整承载，判已有覆盖。

### [Localized Adaptation Reveals Distinct Learning Signatures in Transformers](https://arxiv.org/html/2607.25663v1)

Exact-v1 对五类 objective 做 early/middle/late/full LoRA 干预，发现 acquisition、transfer 与 boundedness 的层位偏好不同，并在五个模型家族上复验方向。它不证明层语义固定或 localized LoRA 可跨架构直接迁移；Ch30 已吸收“adapter placement 是控制泛化边界的变量”，并保留 full-stack 与重校准 fallback。

### [Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge Prediction](https://arxiv.org/html/2607.25718v1)

Exact-v1 将 tool retrieval 从独立打分变成 query-conditioned hyperedge prediction，使整个工具集合及 cardinality-specific compatibility 成为选择单位。ToolBench 结果不能证明共调用图在新工具、权限变化或长尾域保持有效；Ch78 已吸收 set-level admission、依赖失效与独立工具检索 fallback。

### [Transformer Transformer: A Unified Model for Motion-Conditioned Robot Co-design](https://arxiv.org/html/2607.25798v1)

Exact-v1 统一 token 化 embodiment、state 与 action，以 reward-agnostic dynamics 预测转成 reward-specific value，引导机器人形态 diffusion；跨设计空间实验及 ALOHA 实物只支持所测轨迹和奖励。它不证明仿真 dynamics 在新硬件安全，也增加形态—控制联合搜索成本；Ch25 已吸收 world model 参与 embodiment co-design 的条件与真实控制验证 gate。

### [CHILL-Harness: Counterfactual Harness Learning for Efficient Reasoning in Long-Horizon Agents](https://arxiv.org/html/2607.25825v1)

Exact-v1 估计 orchestration intervention 相对当前 workflow 的 counterfactual advantage，只授权超过 margin 且满足 success-preserving objective 的调整。多类长任务结果不能证明因果估计在环境漂移下无偏，错误 confidence 会冻结有益变化或放行退化；Ch84 已吸收 adaptive harness 的授权、预算与静态策略 fallback。

### [HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs](https://arxiv.org/html/2607.25853v1)

Exact-v1 用 skill、AtomicOp 与 decomposition/temporal/compatibility/support/recovery typed edge 构成图，执行时只取相关子图并保持 symbolic task state。三个环境不能证明图抽取正确或跨版本 action schema 可复用；Ch81 已吸收高层 procedure→AtomicOp grounding、checkpoint 与 recovery edge。

### [Stemma: Induced Decision Regions Reveal LLM Provenance](https://arxiv.org/html/2607.25880v1)

Exact-v1 把开放输出归约为有限 decision region，以 stability、robustness、specificity 选择 probe，在多类权重变换和部署实例上区分 lineage。AUC/TPR 不证明法律意义所有权或对主动规避稳健，black-box probe 也增加查询成本；Ch59 已吸收 behavioral fingerprint 是 provenance sensor、必须与签名/权重 lineage 联合。

### [RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement](https://arxiv.org/html/2607.25886v1)

Exact-v1 固定训练、服务、评测与预算，只允许 Agent 迭代数据策略；结果显示多数继续搜索在中途峰值后退化，证明“最后一次尝试”不能自动拥有发布权。六个 benchmark 不能证明自动研究可递归自我改进；Ch66 已写入 checkpoint preservation、独立 evaluator 和 release gate，判已整合。

### [Toward Standardized Cross-Vendor Agent Tool Trust Management in Autonomous Networks](https://arxiv.org/html/2607.25914v1)

Exact-v1 提出跨厂商 trust state machine、MnS 通知、阻尼级联与依赖图回溯；模拟只证明设定拓扑和通知模型下的收敛/传播，不是已落地的 3GPP 标准或生产 SLA。Ch72 需把它作为 proposed contract，补 trust degradation→调用阻断→retroactive impact 的控制链与人工 override。

### [SecDrift: Measuring Sector-Conditioned Security Drift in AI-Generated Code](https://arxiv.org/html/2607.25225v1)

Exact-v1 用 matched counterfactual 保持任务、接口和示例不变，只替换行业语境，再比较生成代码的安全缺陷；这比跨数据集总分更接近“语境是否改变安全行为”的可归因实验。自动 detector 的零告警只能形成所覆盖缺陷类别的下界，不能证明代码安全；长期增量是 Ch66 将固定控制变量、detector coverage、人工审查与动态执行验证写入同一 evaluation contract。

### [The Case Against Generation for Retrieval: Discriminative Language Models as Effective Retrievers](https://arxiv.org/html/2607.25346v1)

Exact-v1 将检索路径从逐 token 生成改为双塔编码、EOS pooling、KL distillation 与 ANN 查询，使文档表示可离线索引并把在线成本移回向量匹配。实验不能证明判别式检索在需要复杂交互推理或快速变化 corpus 时总是占优；Ch76 已经完整区分 factorized retrieval、cross-encoder reranking、索引 freshness 和端到端生成分支，判已有覆盖。

### [Distilling Temporal Search and Reasoning: Evolving LLMs for Future Prediction via Harness-Assisted Efficient Data Synthesis](https://arxiv.org/html/2607.25554v1)

Exact-v1 的关键不是提示模型“不要看未来”，而是由 harness 在每个 search/tool round 按 cutoff 过滤 observation，并以可验证时间戳决定样本是否进入训练 lineage。`datePublished` 缺失或冲突时必须 fail closed，实时检索与时间冻结快照是不同可复现性分支；Ch27 已吸收这种由执行环境而非模型文本拥有时间边界的机制。

### [F(AI)²R: Who Did What, and Who Checked? Verifiable AI Provenance as an Executable Skill](https://arxiv.org/html/2607.25637v1)

Exact-v1 把 provenance 表达为可执行活动与实体关系，并为 artifact、prompt 和输出保存 identity/hash；verification state 只能由具备相应权限的 grantor 单调提升，不能由被审对象自证。单仓库示例不能证明跨组织信任已经解决，artifact 可访问也不等于 claim 为真；Ch69 已吸收 authority ceiling、promotion event 与 evidence/truth 分离。

### [Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks](https://arxiv.org/html/2607.25877v1)

Exact-v1 在预先声明的 Agent 依赖图上组合局部校准概率，以运行时 posterior 触发告警或人工接管。该结果依赖 DAG、条件独立与局部 calibration 都近似成立，不能把传播后的数值当作真实端到端正确率；Ch82 已有相关性、校准、风险预算和 human gate 的机制边界，判已有覆盖。

### [MDTransformer: A Hardware-Software Co-Design of Mode-Division Photonic Transformer Accelerator with Inverse-Designed Coherent Crossbar](https://arxiv.org/html/2607.26016v1)

Exact-v1 将 attention/MLP dataflow 映射到 mode-division photonic crossbar，并围绕器件并行度、转换开销与数值表示共同选择执行计划。结论主要来自作者仿真，不能外推为生产吞吐、精度或制造良率；Ch49 已要求新执行介质同时给出真实 kernel consumption、精度 contract、测量层级和传统 GPU fallback，判已有覆盖。

### [JKO-RAG: Distributional Retrieval as Wasserstein Free-Energy Gradient Flow](https://arxiv.org/html/2607.24776v1)

Exact-v1 以 Wasserstein/free-energy 形式把 relevance、entropy 与 redundancy 合并成迭代式文档分布更新，本质上改变的是候选后的 reranking 与多样性控制。它没有改变 corpus identity、候选召回 owner 或 evidence verification，也未证明额外迭代成本对所有查询值得；Ch76 已承载候选生成、reranking、diversity/stability 与简单检索回退，判已有覆盖。

### [Three Sides of Retrieval: Factorial Evidence for Document-Side, Query-Side, and Answer-Side Complementarity in RAG](https://arxiv.org/html/2607.24781v1)

Exact-v1 用 factorial 设计分别消融文档结构、查询重写和答案核验，避免把三者的收益合并成一个 RAG 总分；文档侧建立与 chunk index 并行的 heading index，再按预算展开相关 section。小规模企业文档结果不能证明结构索引普遍优于 chunking，OCR 或弱标题文档应回退普通索引；Ch76 已吸收三层责任与共存边界。

### [Reasoning with Memory: A Temporal Granularity-Adaptive Framework for Training-Free Long Video Understanding](https://arxiv.org/html/2607.24794v1)

Exact-v1 先根据 query 所需时间粒度选择 observation span，再用 temporal-semantic memory graph 在固定帧预算内覆盖事件，而不是把更多帧无条件塞进上下文。selector 只是 evidence router，不能把被选帧当成事实证明；当查询粒度估计不稳或事件稠密时应回退 uniform/dense sampling。Ch23 已吸收 representation budget、event coverage 和证据 owner 边界。

### [AVE-Compass: Towards Holistic Evaluation for Audio-Video Editing Abilities](https://arxiv.org/html/2607.24821v1)

Exact-v1 先检查系统是否响应并执行编辑，再对成功响应测条件质量；因此 response rate、conditional quality 与 unconditional success 必须并列，不能只在成功样本上汇报高分。基准的任务和 judge 不能证明开放编辑场景的普遍质量；Ch66 已吸收 no-op gate、分母公开、确定性检查与人工复核回退。

### [GAUGE: Grading Agent-Built Financial Models Without a Golden Answer](https://arxiv.org/html/2607.24889v1)

Exact-v1 面对不存在唯一 golden answer 的财务模型，把公式一致性、引用与结构等 deterministic gate 和可辩护性 judgment facets 分离；不可判定项允许 N/A、abstain 或升级人工。领域 rubric 不能外推为所有 spreadsheet/agent 任务，LLM judge 也不拥有最终事实；Ch66 已吸收 deterministic correctness 与 defensibility envelope 的双层合同。

### [ODYSSE: Episode-wise Policy Optimization for Personalized Agentic Reasoning](https://arxiv.org/html/2607.25369v1)

Exact-v1 以完整 episode 为采样与更新单位，在局部 stage reward 之外保留 episode outcome，并在多个层级归一化 advantage，以免跨步骤依赖被独立 sample 打散。有限模型、单卡和数据集不能证明 reward broadcast 是逐步因果 credit；Ch33 已吸收 episode identity、局部反馈、全局结果与 step-wise/GRPO fallback。

### [A Causality-aware Infer-diagnose-refine Framework for Test-time Modality Adaptation in VLA Models](https://arxiv.org/html/2607.25516v1)

Exact-v1 对 factual input、visual-zero 与 proprio-zero 分别前向，用动作差异定位模型对模态的敏感性，再以有 gate、缩放和 clipping 的 residual 修正 base action。干预差异只是 sensitivity sensor，并不证明真实因果归属；当诊断不稳定或安全 envelope 被触发时必须提交原始动作或停止。Ch26 已按此收窄作者的宽泛因果表述。

### [OmniDelta: Skill-Driven Budget Allocation for Token Compression in OmniLLMs](https://arxiv.org/html/2607.25669v1)

Exact-v1 将固定多模态配额演进为两层控制：先按 query/skill 分配跨模态预算，再在每种模态内依据内容价值与冗余选择 token。收益依赖 selector 与任务分布，错误分配会在进入主模型前不可逆丢证据；Ch23 已吸收预算守恒、每模态下限和 dense/full-token fallback。

### [SAM3D-Guided Object-Centric Representation Alignment for Vision-Language-Action Models](https://arxiv.org/html/2607.25912v1)

Exact-v1 用 detector、SAM2/SAM3D 生成训练期 privileged object/3D teacher，对齐 VLA 的对象中心表示；部署路径仍只消费 RGB、语言和 proprioception。该机制不能证明运行时拥有实时 metric geometry，teacher mask 误差还可能固化偏差；Ch26 已吸收 train-time privilege、runtime input contract 与 RGB policy fallback。

### [MemLens: A Value-Aware Memory Management System with Interactive Analytics for LLM-based Agents](https://arxiv.org/html/2607.25992v1)

Exact-v1 把长期记忆拆成可审计 unit，并用 proxy 与近似 Shapley contribution 辅助保留、删除和可视化分析。价值估计依赖抽样、任务分布与 evaluator，不能解释为单条记忆的因果效用；Ch77 已经要求 derived memory 带 provenance、marginal scorer uncertainty、删除回滚和人工复核，判已有覆盖。

### [Context Assembly as the Controlled Variable: A Control-Theoretic View of Harness Policies for Frozen LLM Agents](https://arxiv.org/html/2607.25408v1)

Exact-v1 将 frozen model 外部的 context assembly 定义为可观测、可版本化、可替换的 harness policy，由它选择何时注入哪些 observation，而不是把成功归因给权重。selection softmax 不是 outcome probability，在线控制还会引入探索与成本风险；Ch84 已吸收 policy identity、effect evidence、授权边界和静态 workflow fallback。

### [WorkSurface-Bench: Benchmarking Enterprise Agents on Multi-Surface Knowledge Routing](https://arxiv.org/html/2607.25765v1)

Exact-v1 把 enterprise agent 任务分成 knowledge surface routing、artifact acquisition、answer construction 与成本，允许定位是选错系统、拿错对象还是推理失败。封闭 surface/task 集不能证明开放企业环境表现，串行路由也未必总优于 wide/parallel search；Ch66 已吸收四类 failure owner 和预算化 fallback。

### [Messier: A High-Resolution Corpus for Cross-Benchmark Agent Evaluation](https://arxiv.org/html/2607.25891v1)

Exact-v1 说明 Agent evaluation identity 不只有模型和总分，还包括 scaffold、task、environment、typed verifier、每个 verifier outcome 与 aggregation rule；改变聚合方式可能改变排名。语料覆盖不能证明某种 aggregation 是普遍真值；Ch66 已吸收逐 verifier 保存、聚合规则版本化和 benchmark-local fallback。

### [RepoReasoner: Evaluating Repository-Level Code Reasoning Ability of Long-Context Language Models](https://arxiv.org/html/2607.25996v1)

Exact-v1 以动态执行 trace 构造 gold，并比较 oracle、noisy 与 retrieval context，分离代码证据是否可达和模型能否完成 repository-level reasoning。特定仓库与任务不能证明长上下文模型的通用工程能力，oracle context 也不等于真实检索可得；Ch66/Ch75 已承载 access、selection、reasoning 与 execution verification 的分层，判已有覆盖。

### 三项深入分析的跨材料结论

CaRE 暴露了评价中最常见的伪改进：如果真实 NFE、随机性和 metric 不一致，方法名义上相同的 step budget 没有可比性。Stable FP4 则展示训练系统中的对应问题：如果转置前后的 block/scale identity 不一致，算法宣称的低比特路径甚至没有执行同一个数值 contract。二者共同要求测量对象先拥有稳定身份，再讨论优劣。

`πR²` 把这条原则推进到物理闭环：fast proprioception、slow vision state、in-flight action 与 hardware latency 都是不同 freshness 的状态，不能塞进一个“当前 observation”。真正的演进不是多一个模块，而是明确谁拥有最新观测、谁可继续 action chunk、何时必须重规划或停止。

## 5. 缺口与下一步

无

106 项降级材料已全量重读标题与完整摘要：第一次恢复 68 项，独立 false-negative 审计又从余下 38 项恢复 20 项，最终 18 项维持 pre-denominator closure。维持关闭的精确集合为：

- 单领域应用或非大模型系统机制：`2607.24859`、`24875`、`24981`、`24996`、`25019`、`25082`、`25356`、`25566`、`25583`；
- 局部方法或 operating point，未改变长期设计 contract：`2607.25818`、`25857`；
- survey、perspective 或既有机制包装：`2607.24759`、`25032`、`25076`、`25379`、`25380`、`25507`；
- 因果证据不足且三维评分未达到候选阈值：`2607.24769`。

本窗没有 blocked、disputed、整篇 withdrawn 或 Materials Request。20 项二次恢复材料中，14 项完成 Books Integration，6 项经真实正文锚点审计判定 Existing Coverage；`2607.25818` 与 `2607.24769` 经 exact-v1 审阅分别仅为 4 分与 3 分，保持候选分母之前关闭。最终 123 项候选中，69 项 Integrate、54 项 Existing Coverage，待审阅、待写入和待材料项均为 0。

## 6. 复核

复核者：`/root/july_evidence_crosscheck`（closure false-negative 审计）、`/root/july29_agent_books`、`/root/july29_books_review`、`/root`（归并与写后语义验收）
结论：通过

独立复核重新检查了 38 项剩余 closure 的标题与完整摘要，并对恢复的 20 项逐一完成 exact-v1、三维评分、owner、Books disposition 和证据边界审阅。所有 Integrate 项均已写入真实机制正文，不以 trace 标签代替正文；写后验收核对了 canonical owner、旧方案与约束变化、控制权、trade-off、failure mode、fallback、Source Family marker 和 Daily 链接。最终算术为 `570 raw = 123 candidates + 447 closures`，无待审阅、待写入或待材料项。
