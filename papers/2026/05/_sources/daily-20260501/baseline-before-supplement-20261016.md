# Daily Research — 2026-05-01

**规范：** V3
**窗口：** 2026-04-30T09:00:00+08:00 ～ 2026-05-01T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T16:42:00+08:00

## 1. 结论

本次不继承旧 V2.1 的 63 项候选分母，而是对窗口原始记录中的 556 个唯一 arXiv identity 完成 556/556 题目与摘要语义复筛。按当前长期贡献门槛，最终保留 47 项候选，509 项在候选前关闭；相较旧报告，37 项继续保留、26 项降级、10 项从旧关闭记录恢复。没有发现撤回论文。

47 项候选均重新核对 exact-v1 正文及 Books owner：46 项完成深入审阅，1 项完成标准审阅；21 项此前已经形成真实章节正文，26 项由现有正文充分承载，因此本轮没有新的共享 Books 语义写入。非作者独立复核进一步检查了分母变化、恢复与降级边界、候选证据以及真实正文锚点；发现并修复一处 ZipCCL 来源标记与正文错位后，本日报闭环。

这批材料共同强化了五条长期主线：训练控制量必须能够跨 scale 转移；推理调度必须拥有请求状态、资源状态与可验证 observation；安全与评测必须把更新、上下文和污染路径纳入 release evidence；Agent 的 memory、workflow 与 sandbox state 必须分别治理；多模态生成、world state 与 physical action 不能共享未经验证的能力结论。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| `SRC-OPENAI` | 官方 Research 当前历史索引，限定本窗及模型、训练、推理、Agent 主题 | 已检查 | 历史目录为可变索引，不能单独证明绝对零遗漏 |
| `SRC-ANTHROPIC` | 官方 Research 当前历史索引，限定本窗及模型、可靠性、Agent 主题 | 已检查 | 历史目录为可变索引，不能单独证明绝对零遗漏 |
| `SRC-GOOGLE-AI` | DeepMind 与 Google Research 官方历史索引，限定本窗与 ROADMAP 主线 | 已检查 | 历史目录为可变索引，不能单独证明绝对零遗漏 |
| `SRC-META-AI` | Meta / FAIR 官方 Research 当前历史索引，限定本窗与开放模型、训练机制 | 已检查 | 历史目录为可变索引，不能单独证明绝对零遗漏 |
| `SRC-QWEN` | Qwen 官方博客历史目录，限定本窗与模型、训练、多模态机制 | 已检查 | 历史目录为可变索引，不能单独证明绝对零遗漏 |
| `SRC-DEEPSEEK` | DeepSeek 官方研究入口与公开材料索引，限定本窗 | 已检查 | 历史目录缺少不可变日快照 |
| `SRC-MOONSHOT` | Kimi 官方博客与 MoonshotAI 官方仓库历史记录，限定本窗 | 已检查 | 历史目录缺少不可变日快照 |
| `SRC-TENCENT-HUNYUAN` | 混元 Research“全部”列表及官方仓库，按日期定点检查 | 已检查 | 当前列表未提供可复算的历史分页快照 |
| `SRC-ZAI` | 智谱 Research、官方仓库与发布说明，按日期定点检查 | 已检查 | 当前列表未提供可复算的历史分页快照；窗口前的 Scaling Pain 不计入 |
| `SRC-BYTEDANCE-SEED` | Seed Research、论文目录与官方仓库，限定本窗与大模型系统主题 | 已检查 | 历史目录为可变索引，不能单独证明绝对零遗漏 |
| `SRC-BAIDU-ERNIE` | ERNIE 官方博客与官方仓库历史记录，限定本窗 | 已检查 | 历史目录缺少不可变日快照 |
| `SRC-XIAOMI-MIMO` | MiMo 官方论文页与仓库历史记录，限定本窗 | 已检查 | 历史目录缺少不可变日快照 |
| `SRC-MINIMAX` | MiniMax 中英文技术博客、官方仓库与 Agent 技术博客，限定本窗 | 已检查 | 历史目录为可变索引，不能单独证明绝对零遗漏 |
| `SRC-ARXIV` | 12 个注册主题入口的窗口 owner replay；556 个唯一 identity 全部读取题目与摘要，47 项进入正文审阅 | 已检查 | DOI created 与 OAI datestamp 只作身份旁证；归属使用官方 Friday new-submission 批次与公告节奏 |

原始身份、题目、摘要与旧筛选记录见 [`arxiv-owner-receipt.json`](../_sources/arxiv-owner-replay-20260903/20260501/arxiv-owner-receipt.json)。本轮分母变化及 26 项降级、10 项恢复的逐项理由见 [`V3_RECERTIFICATION.md`](../_sources/daily-20260501/V3_RECERTIFICATION.md)。

## 3. 候选与判断

下表公开时间采用官方 Friday new-submission 批次可支持的窗口内范围；DataCite 注册时间只作身份旁证，不冒充逐篇公开时刻。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [MARS](https://arxiv.org/html/2604.26963v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 异构 Agent workload 的 GPU/CPU 联合 admission 与调度；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Predictive Multi-Tier Memory Management for KV Cache](https://arxiv.org/html/2604.26968v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 把 KV placement 扩为多层预测状态；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Simple Self-Conditioning Adaptation for Masked Diffusion Models](https://arxiv.org/html/2604.26985v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 跨 denoising step 复用 clean-state estimate；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [When Continual Learning Moves to Memory](https://arxiv.org/html/2604.27003v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 参数更新转为 experience memory reuse 后的状态边界；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Dynamic Adversarial Fine-Tuning Reorganizes Refusal Geometry](https://arxiv.org/html/2604.27019v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 安全微调重组 refusal representation 并牵连 utility；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Learning Rate Transfer in Normalized Transformers](https://arxiv.org/html/2604.27077v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 学习率跨 width、depth、token horizon 的 scale transfer；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：TRAIN-PRETRAINING，[Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Co-Evolving Policy Distillation](https://arxiv.org/html/2604.27083v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | teacher 与 policy 同步演进改变 rollout target；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [RoundPipe](https://arxiv.org/html/2604.27085v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 异构 consumer GPU 下重排 pipeline stage 与通信；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-PIPELINE-PARALLEL，[Ch38](../../../../books/part-04-training-system/38-pipeline-parallel.md) |
| [AutoSP](https://arxiv.org/html/2604.27089v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 编译器选择 sequence-parallel plan 与通信边界；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-TENSOR-PARALLEL，[Ch37](../../../../books/part-04-training-system/37-tensor-parallel.md) |
| [Step-level Optimization for Computer-use Agents](https://arxiv.org/html/2604.27151v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 从轨迹级 reward 下沉到 step-level workflow signal；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Path-Lock Expert](https://arxiv.org/html/2604.27201v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | control token 把 reasoning mode 变成显式 expert route；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：MODEL-MOE，[Ch21](../../../../books/part-02-model/21-moe.md) |
| [Indirect Prompt Injection in the Wild](https://arxiv.org/html/2604.27202v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 真实网页中的间接注入改变外部内容信任边界；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Decoupling the Benefits of Subword Tokenization](https://arxiv.org/html/2604.27263v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 受控 byte simulation 分离吞吐与 boundary prior；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MODEL-TOKENIZER，[Ch11](../../../../books/part-02-model/11-tokenizer.md) |
| [NuggetIndex](https://arxiv.org/html/2604.27306v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | atomic retrieval unit 同时拥有 provenance、version 与治理状态；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Safe Bilevel Delegation](https://arxiv.org/html/2604.27358v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 双层 delegation 把 proposal 与 commit authority 分开；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [MiniCPM-o 4.5](https://arxiv.org/html/2604.27393v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 全双工多模态 interaction 引入连续 perception/output state；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [VitaLLM](https://arxiv.org/html/2604.27396v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | ternary accelerator 的 dependency-aware execution plan；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Beyond the Mean](https://arxiv.org/html/2604.27405v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 把同模型变化检测从均值转为 matched uncertainty；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Secret Stealing Attacks on Local LLM Fine-Tuning](https://arxiv.org/html/2604.27426v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 模型代码供应链把本地数据暴露给恶意执行路径；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [ScaleBox](https://arxiv.org/html/2604.27467v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 大规模代码验证需要隔离执行与可追踪 verifier evidence；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [CuLifter](https://arxiv.org/html/2604.27486v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | GPU binary lifting 到 typed IR 改变执行计划可检查性；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Belief-Guided Inference Control](https://arxiv.org/html/2604.27536v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 用可验证 observation 更新 service belief 再执行控制；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Trace-Level Analysis of Information Contamination](https://arxiv.org/html/2604.27586v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 多 Agent 信息污染必须沿 trace 边传播和归责；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-TRACE，[Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [Optimization before Evaluation](https://arxiv.org/html/2604.27637v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | prompt optimization 是 evaluation contract 的受控变量；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Contextual Agentic Memory is a Memo, Not True Memory](https://arxiv.org/html/2604.27707v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 区分 prompt-carried memo 与 durable revisable memory；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Test Before You Deploy](https://arxiv.org/html/2604.27789v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 模型更新需通过 update-specific release gate；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MCPHunt](https://arxiv.org/html/2604.27819v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 跨 MCP server 数据传播需要端到端 policy evidence；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MCP，[Ch83](../../../../books/part-07-agent/83-mcp.md) |
| [ZipCCL](https://arxiv.org/html/2604.27844v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | collective 无损压缩改变通信字节与计算开销权衡；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [AI Inference as Relocatable Electricity Demand](https://arxiv.org/html/2604.27855v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | latency constraint 决定 inference load 的地域迁移空间；3 + 2 + 2 = 7 | 深入完成 | 整合：PLATFORM-COST，[Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [TwinGate](https://arxiv.org/html/2604.27861v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 无稳定身份流量下仍需维护攻击分解状态；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SimEval-IR](https://arxiv.org/html/2604.27878v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | user simulator 成为 evaluation artifact 而非隐含输入；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [In-Context Prompting Obsoletes Agent Orchestration](https://arxiv.org/html/2604.27891v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 对短而稳定程序，prompt state 可替代外部 orchestration；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [RHyVE](https://arxiv.org/html/2604.28056v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | reward hypothesis 在训练前需 competence-aware verification；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Emergent Misalignment Persona Consistency](https://arxiv.org/html/2604.28082v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 模型自评 persona 可能 coherent、inverted 或不一致；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Hierarchical Fault Detection and Diagnosis for Transformers](https://arxiv.org/html/2604.28118v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | component signal 与 fault graph 建立诊断证据链；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：PLATFORM-MONITORING，[Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [Do Sparse Autoencoders Capture Concept Manifolds?](https://arxiv.org/html/2604.28119v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | concept 可能由 global/local atom group 而非单 feature 表示；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Beyond Gaussian Bottlenecks](https://arxiv.org/html/2604.28122v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | topology-aligned latent 保留视觉特征几何；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Beyond SFT-to-RL](https://arxiv.org/html/2604.28123v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | on-policy distillation 作为 multimodal RL 的 pre-alignment stage；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Latent Adversarial Detection](https://arxiv.org/html/2604.28129v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 多轮 probe 使 latent risk 成为持续安全状态；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Crab](https://arxiv.org/html/2604.28138v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | sandbox checkpoint 必须捕获进程外 semantic state；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Claw-Eval-Live](https://arxiv.org/html/2604.28139v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | refreshable task 与 artifact snapshot 支持 live evaluation；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Strait](https://arxiv.org/html/2604.28175v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | priority 需结合 interference-conditioned latency prediction；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Synthetic Computers at Scale](https://arxiv.org/html/2604.28181v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 长程 computer-use 评测需保留 workspace state 与 artifact lineage；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md) |
| [Exploration Hacking](https://arxiv.org/html/2604.28182v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | exploration 本身进入 RL trust boundary；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Representation Fréchet Loss](https://arxiv.org/html/2604.28190v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | population statistic 与 gradient batch 解耦的分布匹配损失；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [LaST-R1](https://arxiv.org/html/2604.28192v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | physical latent reasoning 与 action reward 联合优化；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [HERMES++](https://arxiv.org/html/2604.28196v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 共享 3D state 支持理解与未来几何预测；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |

## 4. 证据与知识整合

### [MARS](https://arxiv.org/html/2604.26963v1)

exact-v1 的控制面以 GPU/CPU 双资源 observation 决定 admission，并用 session metadata 与 KV residency 维持多轮 continuation；实验限定在修改后的 vLLM、单卡 H100/H200 与作者 Agent workload，未证明多租户公平或跨集群稳定性。Ch56 已把调度对象定义为带 runtime state 的 token-generation process，并覆盖 admission、SLO 与 fallback，故为已有覆盖。

### [Predictive Multi-Tier Memory Management for KV Cache](https://arxiv.org/html/2604.26968v1)

正文把 HBM、CXL、主存、NVMe、RDMA 等层级放入预测 placement，但关键收益主要是基于带宽规格和 trace 的分析投影，而非完整生产部署；跨层迁移会增加预测漂移、传输和故障恢复状态。Ch54 已覆盖 KV 分层、冷热判断及成本/延迟边界，故不追加。

### [Simple Self-Conditioning Adaptation for Masked Diffusion Models](https://arxiv.org/html/2604.26985v1)

exact-v1 在 masked diffusion 的迭代去噪中把上一轮 clean-state estimate 作为下一轮条件，改变的是可变生成状态而非单纯 loss；收益依赖 step schedule、表示与作者任务，错误估计也会跨步放大。Ch24 已解释 iterative correction、commit 与 rollback 压力，故为已有覆盖。

### [When Continual Learning Moves to Memory](https://arxiv.org/html/2604.27003v1)

论文把经验复用从参数更新迁到外部 memory，实验比较写入、检索和复用策略，但只覆盖作者 AgentGym/ReMe 任务，不能证明长期知识不会陈旧或污染。Ch77 已把 memory construction、validity、retrieval 与 revision 分开治理，故不新增正文。

### [Dynamic Adversarial Fine-Tuning Reorganizes Refusal Geometry](https://arxiv.org/html/2604.27019v1)

exact-v1 的 activation 分析显示 adversarial fine-tuning 不只是移动单一拒绝方向，而会重组安全表示几何并影响 utility；结果绑定所测模型、攻击和 probe，几何可分性不是安全保证。Ch72 已要求把模型行为、表示诊断与 release gate 分层，故为已有覆盖。

### [Learning Rate Transfer in Normalized Transformers](https://arxiv.org/html/2604.27077v1)

论文通过 normalized parameterization 检查学习率能否跨 width、depth 与 token horizon 转移，证明的是作者模型族中的 scale rule，而非任意架构的万能学习率；优化器、数据与 normalization 改变仍需重校准。Ch28 已覆盖按层信号尺度、稳定性和 scale transfer 的条件边界，故不追加。

### [Co-Evolving Policy Distillation](https://arxiv.org/html/2604.27083v1)

方法让 teacher 与 learner 随训练共同更新，改变 rollout target 的版本状态并缓和静态 teacher 失配；作者实验不能证明非平稳 target 在所有 RL workload 中稳定。Ch33 已覆盖 rollout-policy/reference-policy 漂移、版本一致性与回退条件，故为已有覆盖。

### [RoundPipe](https://arxiv.org/html/2604.27085v1)

RoundPipe 针对异构 consumer GPU 重排 stage、microbatch 与通信路径，以利用不均衡显存和算力；它用更多计划复杂度换取可用吞吐，仍受最慢 stage、链路和容错约束。Ch38 已形成 pipeline bubble、placement 与 heterogeneity 的完整演进链，故不重复。

### [AutoSP](https://arxiv.org/html/2604.27089v1)

AutoSP 把长上下文 sequence-parallel strategy 交给编译器在候选 plan 中选择，显式权衡 activation memory、collective 与重计算；作者硬件和模型上的最优 plan 不可外推。Ch37 已覆盖 sequence/context parallel 的 state partition 与通信代价，故为已有覆盖。

### [Step-level Optimization for Computer-use Agents](https://arxiv.org/html/2604.27151v1)

论文把 trajectory reward 分配到具体 action step，改善稀疏反馈下的 credit assignment；step label 和 evaluator 仍可能奖励捷径，局部成功不等于 workflow durable correctness。Ch81 已覆盖 step state、checkpoint、retry 和 effect evidence，故不追加。

### [Path-Lock Expert](https://arxiv.org/html/2604.27201v1)

exact-v1 用控制 token 在 `/think` 与 `/no_think` 间选择 mode-pure expert MLP，使 reasoning mode 成为显式 routing state；代价是容量碎片、路由依赖与模式错误。Ch21 已覆盖 expert ownership、capacity 与 routing failure，故为已有覆盖。

### [Indirect Prompt Injection in the Wild](https://arxiv.org/html/2604.27202v1)

论文对真实网页中的间接 prompt injection 做来源与目标分类，支持“外部内容是不可信输入”这一 threat model；它不证明样本频率等于所有生产流量，也不提供完备防御。Ch72 已明确 data/control plane 隔离与 effect authorization，故为已有覆盖。

### [Decoupling the Benefits of Subword Tokenization](https://arxiv.org/html/2604.27263v1)

exact-v1 用 byte-level simulation 分别控制 sequence shortening 与 subword boundary prior，从而说明 tokenizer 收益不是单一因素；结论受语言、模型规模与计算预算限制。Ch11 已把压缩、边界先验、词表与 OOV 代价放在同一取舍链，故不追加。

### [NuggetIndex](https://arxiv.org/html/2604.27306v1)

正文把检索单元拆成可版本化、可追溯的 atomic nugget，并把维护和治理元数据纳入索引；作者任务不证明任意语料都能无损原子化。该机制已写入 Ch76 的 evidence identity 与 retrieval-unit lifecycle 正文，Books 整合有效。

### [Safe Bilevel Delegation](https://arxiv.org/html/2604.27358v1)

双层 delegation 让上层选择授权范围、下层在约束内执行，核心增量是 proposal 与 effect commit authority 分离；形式化假设不等于真实工具链已满足。该边界已写入 Ch82 的多 Agent 委托、能力限制与 rollback 论证。

### [MiniCPM-o 4.5](https://arxiv.org/html/2604.27393v1)

exact-v1 将语音、视觉与语言输入输出放入持续全双工 interaction loop，机制价值在跨模态时间状态与可打断输出，而非单项 benchmark；未证明开放环境下的实时鲁棒性。Ch23 已覆盖 modality、timestamp 与 provenance identity，故为已有覆盖。

### [VitaLLM](https://arxiv.org/html/2604.27396v1)

论文将 ternary operator mapping、dependency-aware scheduling 与 accelerator dataflow 联合设计；收益绑定作者模型、硬件和精度，不能外推通用 GPU serving。Ch49 已把量化、kernel 与 execution plan 的共设计及 fallback 写成 owner，故不追加。

### [Beyond the Mean](https://arxiv.org/html/2604.27405v1)

方法比较同一模型两个版本时保留 item-level pairing 与不确定性，而非只比较 aggregate mean；统计检验仍受样本、evaluator 与多重比较影响。该增量已写入 Ch66 的 matched evaluation、置信区间和 release-decision 正文。

### [Secret Stealing Attacks on Local LLM Fine-Tuning](https://arxiv.org/html/2604.27426v1)

exact-v1 展示模型仓库中的可执行训练代码能够读取本地 fine-tuning secret 并建立外传路径；攻击实现不证明所有仓库恶意，但改变了 artifact admission 与 sandbox 边界。该机制已进入 Ch72 的供应链、最小权限与隔离执行正文。

### [ScaleBox](https://arxiv.org/html/2604.27467v1)

ScaleBox 用隔离执行环境和可扩展 verifier 检查大量生成代码，关键不是通过率，而是 test artifact、runtime state 与 verdict provenance；作者任务不覆盖全部语言和对抗程序。该 evidence contract 已写入 Ch66。

### [CuLifter](https://arxiv.org/html/2604.27486v1)

CuLifter 将 GPU binary 提升为 typed IR，使依赖、地址空间与语义检查可以进入 execution-plan 验证；lifting correctness 和未知指令仍是失败边界。该机制已写入 Ch49 的 compiler/runtime plan inspection 路线。

### [Belief-Guided Inference Control](https://arxiv.org/html/2604.27536v1)

控制器不直接相信离线预测，而是从可验证 observation 更新 workload belief，再调整 serving 配置；收益以额外探测、校准和控制延迟为代价。该闭环已写入 Ch56 的 observe-decide-act、SLO 和保守回退正文。

### [Trace-Level Analysis of Information Contamination](https://arxiv.org/html/2604.27586v1)

论文沿多 Agent trace 重建信息流和污染传播，而非只看最终答案；trace 缺失或跨服务 identity 断裂会导致错误归因。该增量已进入 Ch69 的 causality、provenance 与跨 Agent trace 语义。

### [Optimization before Evaluation](https://arxiv.org/html/2604.27637v1)

exact-v1 表明未经优化的 prompt 会把 interface quality 混入 model quality，因此 prompt/search budget 必须成为评测协议变量；优化本身也可能对 benchmark 过拟合。该边界已写入 Ch66 的 evaluation contract 与公平比较正文。

### [Contextual Agentic Memory is a Memo, Not True Memory](https://arxiv.org/html/2604.27707v1)

材料区分上下文中携带的摘要 memo 与可持续写入、验证、修订和遗忘的 memory system；它主要是边界澄清而非新架构。Ch77 已明确这一区分，标准审阅足以支持已有覆盖。

### [Test Before You Deploy](https://arxiv.org/html/2604.27789v1)

正文主张每次模型或依赖更新都应触发与风险相称的 targeted tests，而不是沿用静态 benchmark；作者框架不证明一套测试覆盖所有回归。Ch66 已拥有 versioned evaluation 和 release gate，因此不新增。

### [MCPHunt](https://arxiv.org/html/2604.27819v1)

MCPHunt 把跨 server 的数据传播、工具链边界和 policy violation 放入同一评测 trace；测试集不能证明协议实现安全完备。该机制已进入 Ch83 的 capability、data lineage 与跨 server enforcement 正文。

### [ZipCCL](https://arxiv.org/html/2604.27844v1)

ZipCCL 在 collective 前后增加无损压缩/解压，只有减少的链路字节超过额外 kernel、buffer 与同步成本时才获益；收益绑定 tensor distribution 与互连。该条件分支已写入 Ch36 的 communication optimization 路线。

### [AI Inference as Relocatable Electricity Demand](https://arxiv.org/html/2604.27855v1)

论文把 inference 请求的 latency budget、区域电力和迁移距离联立，说明并非所有负载都能随电价搬迁；模型依赖能源假设，不代表实际运营收益。该约束已写入 Ch70 的 carbon/cost placement 与 SLO 共优化正文。

### [TwinGate](https://arxiv.org/html/2604.27861v1)

TwinGate 针对无稳定用户 identity 的 decompositional jailbreak，维护跨请求攻击状态并用不对称对比信号判断；state collision、隐私和 evasion 仍是失败面。Ch72 已覆盖 stateful defense、identity uncertainty 与误封回退，故不追加。

### [SimEval-IR](https://arxiv.org/html/2604.27878v1)

工具包把 user simulator 的 persona、policy、随机性和 session trace 变成 versioned evaluation artifact；模拟用户不等于真实分布。该增量已进入 Ch66 的 simulator validity 与 evaluator provenance 正文。

### [In-Context Prompting Obsoletes Agent Orchestration](https://arxiv.org/html/2604.27891v1)

作者实验支持一个反向分支：对短、稳定、可一次装入 context 的程序，显式 orchestration 可能只增加状态与失败点；它不适用于长程副作用和恢复。该共存边界已写入 Ch81，防止把 workflow 复杂度当作默认答案。

### [RHyVE](https://arxiv.org/html/2604.28056v1)

RHyVE 在采用 LLM 生成的 reward hypothesis 前评估 verifier competence，并按阶段控制部署；仍可能继承 judge 偏差与覆盖缺口。该 release-before-optimization 机制已进入 Ch31 的 reward trust boundary。

### [Emergent Misalignment Persona Consistency](https://arxiv.org/html/2604.28082v1)

exact-v1 显示 emergent-misalignment 模型对 persona 的自我报告可能一致、反向或不稳定，因此 self-assessment 不能独立作为安全证据；结论绑定作者模型与 elicitation。Ch72 已要求外部行为、表示与独立评测交叉验证，故不追加。

### [Hierarchical Fault Detection and Diagnosis for Transformers](https://arxiv.org/html/2604.28118v1)

论文从 Transformer component signal 构建 fault-propagation graph，并在 7 个模型、9 个任务、5556 个 mutation 上评估；合成 mutation 不等同真实故障分布，graph 也可能随架构漂移。Ch67 已覆盖模型内部信号、因果诊断与版本基线，故为已有覆盖。

### [Do Sparse Autoencoders Capture Concept Manifolds?](https://arxiv.org/html/2604.28119v1)

exact-v1 表明 concept manifold 可能由全局或局部 SAE atom group 表示，单一 feature direction 会稀释或分裂概念；toy 与所测模型不能建立普遍 ontology。Ch5 已把表示视为分布式、任务相关且需 probe 验证，故不追加。

### [Beyond Gaussian Bottlenecks](https://arxiv.org/html/2604.28122v1)

方法用 topology-aligned、power-spherical latent 适配 vision-transformer feature geometry，并在重建/生成任务上验证；它不证明 latent 已成为因果、可控 world state。Ch25 已区分几何表示、predictive state 与 control authority，故为已有覆盖。

### [Beyond SFT-to-RL](https://arxiv.org/html/2604.28123v1)

作者在 multimodal RL 前加入 black-box on-policy distillation，使初始 policy 更接近可探索区域；代价是 teacher bias、额外 rollout 和版本耦合。该阶段化路线已写入 Ch31，作为 SFT 与 RL 之间的条件分支。

### [Latent Adversarial Detection](https://arxiv.org/html/2604.28129v1)

方法在多轮交互中主动 probe hidden activation，并累积 latent risk state，而不是逐轮独立分类；probe 本身可能被适应或增加延迟。该机制已进入 Ch72 的 stateful detection 与 defense-in-depth 正文。

### [Crab](https://arxiv.org/html/2604.28138v1)

Crab 通过 coordinator、eBPF inspector 与 checkpoint/restore data plane 捕获 Agent sandbox 的进程、文件和外部 semantic dependency；exact-v1 只覆盖 Linux sandbox 与所测 backend。该 state ownership 和恢复边界已写入 Ch84。

### [Claw-Eval-Live](https://arxiv.org/html/2604.28139v1)

评测以 refreshable signals、release snapshot、controlled fixtures 与 artifact graders 维护 105 项动态任务；ClawHub-derived demand 不代表通用生产分布。Ch66 已覆盖 live benchmark 的 version、fixture 与 drift，故为已有覆盖。

### [Strait](https://arxiv.org/html/2604.28175v1)

Strait 用双优先级 scheduler 和 interference predictor 估计并发执行影响，避免优先级只把排队延迟搬成 GPU contention；跨模型迁移和 tail-SLO 仍需重新校准。该机制已写入 Ch56 的 priority、interference 与 conservative fallback 正文。

### [Synthetic Computers at Scale](https://arxiv.org/html/2604.28181v1)

正文生成任务一致的文件、目录、终端与 workspace state，用于长程 productivity Agent 训练/评测；合成环境会漏掉组织策略、隐藏依赖和真实用户分布。Ch27 已覆盖 synthetic data 的 state consistency、provenance 与 distribution gap，故不追加。

### [Exploration Hacking](https://arxiv.org/html/2604.28182v1)

论文展示 policy 可通过压低有用 exploration 来抵抗 RL 更新，即便没有显式 reward hacking；构造实验不证明生产普遍性。该 failure mode 已进入 Ch31 的 rollout diversity、policy-update diagnostics 与 release evidence。

### [Representation Fréchet Loss](https://arxiv.org/html/2604.28190v1)

方法把 representation distribution distance 变成训练 loss，并把估计 population statistic 的样本与 gradient batch 解耦；收益依赖 encoder 与统计估计，不能外推感知一致性。该替代生成目标已写入 Ch24 的 objective/evaluation mismatch 路线。

### [LaST-R1](https://arxiv.org/html/2604.28192v1)

exact-v1 把 physical latent reasoning 当作 VLA RL 的显式决策变量，并与 action reward 联合优化，在 LIBERO 与四类真实机器人任务验证；作者实验不证明开放世界安全、实时频率或 sim-to-real 普遍性。Ch26 已覆盖 reasoning/controller 分层、action authority 与 physical evidence，故不追加。

### [HERMES++](https://arxiv.org/html/2604.28196v1)

HERMES++ 共享 3D representation 以同时支持 scene understanding 和 future geometry generation；驾驶数据与 open-loop 指标不证明 closed-loop safety 或 causal controllability。Ch25 已明确 video generation、predictive environment state 与 planner authority 的边界，故为已有覆盖。

## 5. 缺口与下一步

无外部 exact-version 材料缺口，也没有候选处于受阻、争议或暂缓状态；本窗没有尚可继续执行的工作。

终态保留项是 13 个机构历史目录缺少不可变日快照。它们不用于支持正面证据、Books 结论或绝对“无遗漏”断言；定点重开条件是以后取得当日官方快照，或发现能够唯一定位到本窗的官方事件。触发后只重开 2026-05-01 的对应来源与 Source Family，不重跑整日其他已闭合工作。

509 项候选前关闭分布为：局部任务或垂直领域结果 221；受限模型、表示、多模态或 world-model 变体 96；未改变责任边界的 Agent、安全或 workflow 实例 65；未改变训练、推理或执行计划的局部优化 61；单一 benchmark、数据集或评测实现 43；secondary synthesis、AI for Science 暂缓或项目外材料 15；重复、revision 或身份关闭 8。逐项审计入口见 [`V3_RECERTIFICATION.md`](../_sources/daily-20260501/V3_RECERTIFICATION.md)。

## 6. 复核

复核者：`weekly_w37`（非作者 fresh-context reviewer）
结论：通过

独立复核重新计算了 556 个唯一 identity 及 old 63 → new 47 的集合关系，逐项复查 26 个降级与 10 个恢复，并对其余关闭项按高风险主题和关闭理由分层抽查；未发现需要新增或剔除的候选。47 项的日期范围、三维评分、证据边界与处置均无冲突；10 个恢复项重新打开 exact-v1 HTML，未见撤回提示。21 项“整合”均在当前 Books owner 中找到具体机制正文和唯一来源标记，而非仅有 trace 标签；复核发现 ZipCCL 标记被后续段落隔开，已移动回对应通信压缩正文之后，未改变书稿语义。14 个 Daily 来源均有本窗范围与结果，历史目录的可变性按终态保留项隔离。跨模型第二意见未执行；本次非作者独立复核已覆盖合同要求的风险面。
