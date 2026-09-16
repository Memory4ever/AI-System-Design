# Daily Research — 2026-05-04

**规范：** V3

**窗口：** 2026-05-03T09:00:00+08:00 ～ 2026-05-04T09:00:00+08:00

**状态：** 完成

**阶段：** Coverage、Evidence 与 Books 已闭环；独立复核通过

**Books：** 纳入本次

**检查时间：** 2026-09-14T17:40:00+08:00

## 1. 结论

本窗真实覆盖十四个每日来源。arXiv 周日夜公告批次由后续 owner-replay 还原出 387 个去重 identity；本次没有沿用旧 37 项分母，而是逐项重读 title+abstract 并按当前“大模型或 AI Infrastructure 的长期机制/状态/控制/证据合同”门槛重筛。四项旧候选降级、六项漏检恢复，最终冻结 **39 个候选、348 个候选前关闭、0 个撤回**，retain rate 为 10.1%。

39 项均已达到分数对应的 exact-v1 审阅深度；33 项复用的证据只来自不可变的同一 v1，身份、版本与 claim 未变化，六项恢复材料重新读取了 Method、关键 evaluation 与 limitation。旧报告中已有 7 项 Books 写回和 1 项结构候选仍可追踪；恢复的六项中两项已被当前 Books 主线完整覆盖，四项已按唯一 owner 写入正文。作者完成 Coverage、筛选、Evidence 与 Books 对读后，非作者重新检查了分母迁移、恢复/降级项、exact-v1 结论边界和四处 Books 正文，未发现需要重开的可执行工作。

## 2. 来源覆盖

本轮只检查每日来源；Weekly 来源没有被重复扫描。“已检查”只覆盖列出的入口、窗口和停止点，不代表机构内部绝无未公开研究。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)公开目录；检查本窗及相邻带日期条目，前序可核实研究发布早于窗口 | 已检查 | 限公开目录；无日期页面不作日级归属 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)；相邻公开条目位于窗口外 | 已检查 | 限公开目录 |
| SRC-GOOGLE-AI | [Google DeepMind](https://deepmind.google/research/)与[Google Research Publications](https://research.google/pubs/)；有界检查窗口与相邻日期 | 已检查 | 部分记录只给月份，不能据此作日级全站无遗漏断言 |
| SRC-META-AI | [Meta AI Research](https://ai.meta.com/research/)公开结果页；检查 2026 年 5 月可见日期与分页停止点 | 已检查 | 动态渲染和分页只支持可见目录结论 |
| SRC-QWEN | [Qwen 官方博客](https://qwenlm.github.io/blog/)与公开研究入口；窗口内未定位发布 | 已检查 | 只覆盖公开目录 |
| SRC-DEEPSEEK | [DeepSeek 官网](https://www.deepseek.com/)与官方公开研究入口 | 受阻 | 缺可分页历史日级研究目录；不用于“全站为零”断言，出现官方日级索引时定点重开 |
| SRC-MOONSHOT | [Kimi Platform Blog](https://platform.kimi.com/blog)与 MoonshotAI 公开入口；目录未见本窗条目 | 已检查 | 不以普通 commit 扩充候选 |
| SRC-TENCENT-HUNYUAN | [Hunyuan Research“全部”列表](https://hunyuan.tencent.com/research)；相邻可核实条目为 04-30 与 05-21 | 已检查 | 页面客户端渲染；只用可见列表卡住窗口 |
| SRC-ZAI | [智谱 Research](https://www.zhipuai.cn/zh/research)；相邻可核实条目为 04-29 与 05-20 | 已检查 | 限官方研究目录 |
| SRC-BYTEDANCE-SEED | [Seed Research](https://seed.bytedance.com/en/research)与[Publications](https://seed.bytedance.com/en/public_papers)；检查窗口与相邻日期 | 已检查 | AI for Science 暂缓，不把无日级时间卡片归入本窗 |
| SRC-BAIDU-ERNIE | [ERNIE 技术博客](https://ernie.baidu.com/blog/zh/)；相邻可核实条目为 04-30 与 05-09 | 已检查 | 限官方目录 |
| SRC-XIAOMI-MIMO | [MiMo Paper / Blog](https://mimo.xiaomi.com/)；窗口内没有带日期 Paper | 已检查 | Blog 卡片缺稳定日级时间，不用于事件归属 |
| SRC-MINIMAX | [MiniMax Research / Blog](https://www.minimax.io/blog)与 News 列表；相邻公开条目位于窗口外 | 已检查 | Agent Tech Blog 缺稳定日级时间 |
| SRC-ARXIV | [owner receipt](../_sources/arxiv-owner-replay-20260903/20260504/arxiv-owner-receipt.json)；387 个去重 identity 的 title+abstract 均复核，exact-v1 按候选深度审阅 | 已检查 | DOI created 是 owner-day proxy，不是精确 09:00 时刻；本批由周日夜公告归入本窗 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Being-H0.7: A Latent World-Action Model from Egocentric Videos](https://arxiv.org/html/2605.00078v1) | 2026-05-04T08:00:00+08:00 | 把未来观测作为训练期 privileged supervision，对齐可部署 prior latent，而不是把 pixel rollout 放进控制关键路径。；**3 + 2 + 3 = 8** | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) / `MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Alignment Contracts for Agentic Security Systems](https://arxiv.org/html/2605.00081v1) | 2026-05-04T08:00:00+08:00 | Agent security 不能只判断 intent 或输出文本；可执行 effect 必须在独立 mediation boundary 由 typed contract、authorization 和 audit 拦截，且模型层与执行层各自保留可观测责任。；**3 + 3 + 3 = 9** | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents](https://arxiv.org/html/2605.00136v1) | 2026-05-04T08:00:00+08:00 | Tool-use accuracy 必须拆开协议格式成本、selection/argument error、transport/runtime failure 与真实工具收益；更多工具或更长 schema 会征收 context 和 routing tax，不能把失败都归因于模型不会调用。；**2 + 3 + 3 = 8** | 深入完成 | 已有覆盖：`AGENT-TOOL-CALLING`，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Wasserstein Distributionally Robust Regret Optimization for Reinforcement Learning from Human Feedback](https://arxiv.org/html/2605.00155v1) | 2026-05-04T08:00:00+08:00 | Preference optimization can treat annotator/reward uncertainty as a distributional ambiguity set and optimize worst-case regret, but robustness radius and reference policy become new control assumptions rather than removing reward misspecification.；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：`TRAIN-RLHF`，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Consistent Diffusion Language Models](https://arxiv.org/html/2605.00161v1) | 2026-05-04T08:00:00+08:00 | Consistent diffusion language modeling narrows train/inference inconsistency by coupling conditional denoising states; it trades token-sequential commitment for iterative correction and does not erase sampling-step, cache or rollback costs.；**2 + 2 + 3 = 7** | 深入完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [RouteProfile: Graph-Based Profiling for Cold-Start LLM Routing](https://arxiv.org/html/2605.00180v1) | 2026-05-04T08:00:00+08:00 | Model routing 的 cold start 不是缺少一个静态 leaderboard，而是缺少 workload-conditioned profile；图结构从已知模型迁移观测可降低探索成本，但 profile staleness、uncertainty 和 online fallback 必须进入 admission/routing contract。；**3 + 3 + 3 = 9** | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [State Stream Transformer (SST) V2: Parallel Training of Nonlinear Recurrence for Latent Space Reasoning](https://arxiv.org/html/2605.00206v1) | 2026-05-04T08:00:00+08:00 | Nonlinear recurrent latent state can be trained with a parallel surrogate and executed recurrently, shifting the bottleneck from explicit token history toward state-transition stability and train/decode equivalence.；**2 + 2 + 3 = 7** | 深入完成 | 已有覆盖：`MODEL-DECODER-ONLY`，[Ch18](../../../../books/part-02-model/18-decoder-only.md) |
| [Attention Is Where You Attack](https://arxiv.org/html/2605.00236v1) | 2026-05-04T08:00:00+08:00 | Safety head 的存在或 ablation 不是稳健性证明；攻击可通过重新分配 attention routing 让下游残差流接收错误信号。；**3 + 2 + 2 = 7** | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Rethinking Network Topologies for Cost-Effective Mixture-of-Experts LLM Serving](https://arxiv.org/html/2605.00254v1) | 2026-05-04T08:00:00+08:00 | MoE serving topology 必须把 expert placement、token skew、all-to-all bytes、network tiers 与 replica cost 联合建模；更便宜的 topology 会把平均带宽收益换成 hotspot、reconfiguration 和 failure-domain 压力。；**3 + 3 + 3 = 9** | 深入完成 | 整合：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Jailbroken Frontier Models Retain Their Capabilities](https://arxiv.org/html/2605.00267v1) | 2026-05-04T08:00:00+08:00 | Jailbreak 后保留通用能力意味着 safety case 不能依赖能力退化；风险控制必须落在 action authority、sandbox、monitoring 与 outcome evidence，而不是假设越狱模型不可完成复杂任务。；**3 + 3 + 3 = 9** | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [How Language Models Process Out-of-Distribution Inputs: A Two-Pathway Framework](https://arxiv.org/html/2605.00269v1) | 2026-05-04T08:00:00+08:00 | 白盒 OOD score 必须先排除 sequence-length confound；content embedding 与跨层 processing trajectory 是互补证据，而不是一个可通吃的置信度。；**3 + 3 + 2 = 8** | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Token Arena: A Continuous Benchmark Unifying Energy and Cognition in AI Inference](https://arxiv.org/html/2605.00300v1) | 2026-05-04T08:00:00+08:00 | Inference benchmark 的原子对象可以是 endpoint/model configuration，而不是模型名称；能耗、质量、延迟与请求策略必须在连续、版本化 contract 中共同记录，且偏好结论不能脱离 evaluator 与 workload。；**3 + 3 + 3 = 9** | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Semia: Auditing Agent Skills via Constraint-Guided Representation Synthesis](https://arxiv.org/html/2605.00314v1) | 2026-05-04T08:00:00+08:00 | Agent skill 审计需要把自然语言/代码能力合成为可查询的约束表示，再在调用前检查 source→sink、permission 与 effect；静态分析提高可解释性，却受表示不完备、动态行为与环境依赖限制。；**3 + 3 + 3 = 9** | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Prompt-Induced Score Variance in Zero-Shot Binary Vision-Language Safety Classification](https://arxiv.org/html/2605.00326v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：A deployable safety score must be tested across semantically equivalent prompts; one first-token probability is not a stable confidence contract. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 2 + 3 = 8** | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Making Every Verified Token Count: Adaptive Verification for MoE Speculative Decoding](https://arxiv.org/html/2605.00342v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：MoE speculative verification is scheduled by accepted-token utility against the union-of-experts verification cost. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 3 + 3 = 9** | 深入完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING`，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Block-wise Codeword Embedding for Reliable Multi-bit Text Watermarking](https://arxiv.org/html/2605.00348v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：Multi-bit watermark extraction and provenance detection are different contracts; designated-codeword verification makes false-positive control explicit. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 2 + 3 = 8** | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [MemRouter: Memory-as-Embedding Routing for Long-Term Conversational Agents](https://arxiv.org/html/2605.00356v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：Memory write admission becomes an independently trained, measurable control plane rather than generation-time narration. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 2 + 3 = 8** | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [From Backward Spreading to Forward Replay: Revisiting Target Construction in LLM Parameter Editing](https://arxiv.org/html/2605.00358v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：Supports cross-layer target compatibility for locate-then-edit methods under the evaluated model/edit regimes; does not establish safe sequential editing, provenance, rollback, or production knowledge-lifecycle correctness. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 2 + 3 = 8** | 深入完成 | 结构候选：待季度结构复核 |
| [Uniform-Correct Policy Optimization: Breaking RLVR's Indifference to Diversity](https://arxiv.org/html/2605.00365v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：RLVR objectives can be indifferent among correct modes; a conditional uniformity term makes diversity an explicit optimization contract. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 2 + 3 = 8** | 深入完成 | 已有覆盖：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Agent Capsules: Quality-Gated Granularity Control for Multi-Agent LLM Pipelines](https://arxiv.org/html/2605.00410v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：Agent dispatch granularity is a runtime decision gated by measured workload quality, not a static pipeline property. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 3 + 3 = 9** | 深入完成 | 已有覆盖：`AGENT-PLATFORM`，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies](https://arxiv.org/html/2605.00416v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：Deployment, intervention capture, offline-to-online value learning and redeployment form a versioned embodied-learning loop. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 3 + 3 = 9** | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [BWLA: Breaking the Barrier of W1AX Post-Training Quantization for LLMs](https://arxiv.org/html/2605.00422v1) | 2026-05-04T08:00:00+08:00 | W1AX PTQ 不能只改 weight codebook；weight geometry、activation tail、低秩 residual 与目标 kernel format 必须作为同一部署计划验收。；**3 + 2 + 2 = 7** | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Skills as Verifiable Artifacts: A Trust Schema and a Biconditional Correctness Criterion for Human-in-the-Loop Agent Runtimes](https://arxiv.org/html/2605.00424v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：Agent skills are untrusted executable artifacts whose verification level must gate capabilities and human approval. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 3 + 3 = 9** | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/html/2605.00425v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：Multi-turn agentic RL can use response-level entropy dynamics as an intrinsic credit and exploration-control signal without a separate process reward model. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 2 + 2 = 7** | 深入完成 | 已有覆盖：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Thinking in Text and Images: Interleaved Vision–Language Reasoning Traces for Long-Horizon Robot Manipulation](https://arxiv.org/html/2605.00438v1) | 2026-05-04T08:00:00+08:00 | 长程 VLA 可把 text subgoal 与 visual keyframe 组成可缓存的 semantic-geometric proposal，但必须绑定现场观测、失效检测与 replanning。；**3 + 2 + 3 = 8** | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [CleanBase: Detecting Malicious Documents in RAG Knowledge Databases](https://arxiv.org/html/2605.00460v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：RAG ingestion needs document-level security evidence; similarity-clique detection is one bounded sensor rather than a trust proof. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**2 + 2 + 2 = 6** | 标准完成 | 已有覆盖：`AGENT-RAG`，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [SAGA: Workflow-Atomic Scheduling for AI Agent Inference on GPU Clusters](https://arxiv.org/html/2605.00528v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：Agent workflow, not isolated request, becomes the scheduling/fairness/cache-lifetime unit. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 3 + 3 = 9** | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [AGoQ: Activation and Gradient Quantization for Memory-Efficient Distributed Training of LLMs](https://arxiv.org/html/2605.00539v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：Activation bit width and gradient communication precision become layer/stage-aware training-runtime policies. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 3 + 2 = 8** | 深入完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Sim-FA: A GPGPU Simulator Framework for Fine-Grained Asynchronous Pipeline Analysis](https://arxiv.org/html/2605.00555v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：GPU performance evidence for asynchronous attention pipelines must model TMA, barriers, warp specialization and cache traffic rather than rely on a coarse roofline alone. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 3 + 3 = 9** | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Jailbreaking Vision-Language Models Through the Visual Modality](https://arxiv.org/html/2605.00583v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：Safety post-training and threat models must treat the visual channel as an active intent-bearing attack surface rather than assume text-domain alignment composes across modalities. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 3 + 3 = 9** | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [LLM-Emu: Native Runtime Emulation of LLM Inference via Profile-Driven Sampling](https://arxiv.org/html/2605.00616v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：A serving emulator preserves the real HTTP, scheduler, KV and output paths while replacing only GPU execution with profiled samples. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 3 + 3 = 9** | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Affordance Agent Harness: Verification-Gated Skill Orchestration](https://arxiv.org/html/2605.00663v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：Skill orchestration needs verifier-owned admission and failure recovery; perceptual affordance confidence cannot directly authorize action. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 2 + 3 = 8** | 深入完成 | 已有覆盖：`AGENT-PLATFORM`，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Beyond Benchmarks: MathArena as an Evaluation Platform for Mathematics with LLMs](https://arxiv.org/html/2605.00674v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：Evaluation for fast-moving capabilities needs continuously refreshed, contamination-resistant tasks with versioned scoring rather than a static benchmark snapshot. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 2 + 3 = 8** | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Eliminating Hidden Serialization in Multi-Node Megakernel Communication](https://arxiv.org/html/2605.00686v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：Fine-grained MoE overlap fails across nodes when per-transfer fences serialize the NIC; signaling and ordering ownership must be separated. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 3 + 3 = 9** | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Learning How and What to Memorize: Cognition-Inspired Two-Stage Optimization for Evolving Memory](https://arxiv.org/html/2605.00702v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：Long-term memory needs separately optimized write/update behavior and answer-time use; static hand-written memory update rules are not a durable policy. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 2 + 2 = 7** | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling](https://arxiv.org/html/2605.00737v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：Tool invocation is an admission decision whose benefit, latency and failure cost must be estimated; availability alone does not justify a call. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 3 + 3 = 9** | 深入完成 | 整合：`AGENT-TOOL-CALLING`，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Characterizing the Expressivity of Local Attention in Transformers](https://arxiv.org/html/2605.00768v1) | 2026-05-04T08:00:00+08:00 | Local attention 不只是 global attention 的便宜近似；在固定精度/深度与有限位置谓词下，两者提供互补的 temporal operators。；**3 + 2 + 2 = 7** | 深入完成 | 整合：`MODEL-LONG-CONTEXT`，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Make Your LVLM KV Cache More Lightweight](https://arxiv.org/html/2605.00789v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：Vision-token KV compression is prompt-conditioned and must preserve modality/token/position identity; the mechanism is a bounded implementation case. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**2 + 3 + 2 = 7** | 深入完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [RunAgent: Interpreting Natural-Language Plans with Constraint-Guided Execution](https://arxiv.org/html/2605.00798v1) | 2026-05-04T08:00:00+08:00 | 长期可保留结论是：Natural-language plans need an executable intermediate representation with step constraints, rubrics and recovery transitions. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；**3 + 3 + 2 = 8** | 深入完成 | 已有覆盖：`AGENT-WORKFLOW`，[Ch81](../../../../books/part-07-agent/81-workflow.md) |

### 分母重筛与关闭

- `2605.00066` 只比较 NAVSIM/Bench2Drive 的自动驾驶 open/closed-loop 相关性，未形成可迁移的通用 evaluation owner；候选前关闭。
- `2605.00226` 是战略游戏中 observation/belief/action 的任务诊断，未改变 Agent planning 的持久状态或执行责任；候选前关闭。
- `2605.00324` 是 learning-to-rank feature rollout，不属于当前大模型/AI Infrastructure 主线；候选前关闭。
- `2605.00803` 属于已暂缓的 AI for Science；不以 coding-agent 外壳提升为本项目候选。

反向漏检审计恢复 `2605.00078`、`2605.00236`、`2605.00269`、`2605.00422`、`2605.00438`、`2605.00768` 六项。`2605.00320` VitaLLM 与 `2604.27396v1` 是同一机制/稿件 family 的重复身份，本窗不重复评分。其余 348 个 identity 的具体关闭理由保留在 owner receipt；撤回数为 0。

## 4. 证据与知识整合

旧候选的 Method/Evaluation/limitation locators 来自同一 immutable exact-v1，并与当前 Books 正文重新对读；完整结构化记录继续保存在 [review packet](../_sources/daily-20260504/review-packet.json) 与旧报告证据快照中。以下每项保留采用边界和最终 Books 处置，不把摘要相似度当作证据。

### [Being-H0.7: A Latent World-Action Model from Egocentric Videos](https://arxiv.org/html/2605.00078v1)

exact-v1 §3.1–3.3 将 learnable latent queries 放在感知与动作之间；训练期 posterior branch 用未来观测 embedding 替换查询，逐层对齐 prior/posterior hidden state，并用 norm/rank regularization 防止 latent collapse，部署时移除 posterior。§4 覆盖六个模拟 benchmark、三类机器人与十二项实机任务；作者的 3–4 ms/step 数字只绑定其 UAC 栈。该证据证明 future-aware latent 可作为 action proposal 的受限分支，不证明 latent 是完整 causal world state，也不替代 controller、fresh observation 或 safety monitor。Ch25/Ch26 已明确 pixel→task-relevant latent、training-only future teacher、cache freshness 与 controller authority，故 No Change。 Score V3：3/2/3 = **8**；最终处置：已有覆盖（`MULTIMODAL-WORLD-MODELS / MULTIMODAL-EMBODIED-VLA`）。

### [Alignment Contracts for Agentic Security Systems](https://arxiv.org/html/2605.00081v1)

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2-6 threat assumptions, contract language, dual-layer observability and enforcement`。
- **Mechanism / ownership:** Agent security 不能只判断 intent 或输出文本；可执行 effect 必须在独立 mediation boundary 由 typed contract、authorization 和 audit 拦截，且模型层与执行层各自保留可观测责任。
- **Evaluation contract:** `§7 examples and policy-composition analysis`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§8 impossibility/scope boundary; disclosed framework is not proof of all semantic safety`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `PLATFORM-SECURITY`；Score V3 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。

### [Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents](https://arxiv.org/html/2605.00136v1)

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-4 decomposition of tool protocol, selection and execution costs`。
- **Mechanism / ownership:** Tool-use accuracy 必须拆开协议格式成本、selection/argument error、transport/runtime failure 与真实工具收益；更多工具或更长 schema 会征收 context 和 routing tax，不能把失败都归因于模型不会调用。
- **Evaluation contract:** `§5 controlled tool-use diagnosis across models/tasks`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6/discussion task and framework scope; no universal tax constant`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Explanatory Analogy` → `AGENT-TOOL-CALLING`；Score V3 `2/3/3` = **8/9**。
- **Books decision:** `No Change — Existing Coverage`。

### [Wasserstein Distributionally Robust Regret Optimization for Reinforcement Learning from Human Feedback](https://arxiv.org/html/2605.00155v1)

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-5 Wasserstein ambiguity set and robust regret objective`。
- **Mechanism / ownership:** Preference optimization can treat annotator/reward uncertainty as a distributional ambiguity set and optimize worst-case regret, but robustness radius and reference policy become new control assumptions rather than removing reward misspecification.
- **Evaluation contract:** `§6 experiments and ablations on specified preference datasets/models`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated limitations section; author experiments do not establish universal robustness radius`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Principle Reuse` → `TRAIN-RLHF`；Score V3 `2/2/2` = **6/9**。
- **Books decision:** `No Change — Existing Coverage`。

### [Consistent Diffusion Language Models](https://arxiv.org/html/2605.00161v1)

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2-3 consistency objective and diffusion language-model mechanism`。
- **Mechanism / ownership:** Consistent diffusion language modeling narrows train/inference inconsistency by coupling conditional denoising states; it trades token-sequential commitment for iterative correction and does not erase sampling-step, cache or rollback costs.
- **Evaluation contract:** `§4-5 language-model evaluations and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6 Conclusion — exact-v1 has no dedicated limitations section; workloads do not prove replacement of autoregressive generation`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Alternative Branch` → `MULTIMODAL-GENERATIVE-PARADIGMS`；Score V3 `2/2/3` = **7/9**。
- **Books decision:** `No Change — Existing Coverage`。

### [RouteProfile: Graph-Based Profiling for Cold-Start LLM Routing](https://arxiv.org/html/2605.00180v1)

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 graph profile construction and cold-start transfer`。
- **Mechanism / ownership:** Model routing 的 cold start 不是缺少一个静态 leaderboard，而是缺少 workload-conditioned profile；图结构从已知模型迁移观测可降低探索成本，但 profile staleness、uncertainty 和 online fallback 必须进入 admission/routing contract。
- **Evaluation contract:** `§4-5 new-model routing experiments, baselines and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6 Conclusion — exact-v1 has no dedicated limitations section; tested model/task graph and offline traces bound the conclusion`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `INFER-SCHEDULING`；Score V3 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。

### [State Stream Transformer (SST) V2: Parallel Training of Nonlinear Recurrence for Latent Space Reasoning](https://arxiv.org/html/2605.00206v1)

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2-4 nonlinear recurrence and parallel-training construction`。
- **Mechanism / ownership:** Nonlinear recurrent latent state can be trained with a parallel surrogate and executed recurrently, shifting the bottleneck from explicit token history toward state-transition stability and train/decode equivalence.
- **Evaluation contract:** `§5 model/task evaluations and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6 limitations on scale, recurrence stability and broader workloads`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Alternative Branch` → `MODEL-DECODER-ONLY`；Score V3 `2/2/3` = **7/9**。
- **Books decision:** `No Change — Existing Coverage`。

### [Attention Is Where You Attack](https://arxiv.org/html/2605.00236v1)

exact-v1 §4–§6 用 Gumbel-softmax 在选定 head 上优化非语义 token，并比较“移除 head”与“重定向 attention”。受测 LLaMA-3-8B、Mistral-7B、Gemma-2-9B 的差异支持 routing concentration 是攻击面，但 §7 明确只有三种 7–9B 架构、同一 200 条 HarmBench 既用于 head calibration 又参与评估，且需要 white-box 与逐模型优化。因此它改变的是威胁模型和 defense evaluation：不能把 head magnitude/存在性当作安全证据；不证明闭源 API 或更大模型具有相同 ASR。该机制边界已写入 Ch72 的攻击面与防御评估主线。 Score V3：3/2/2 = **7**；最终处置：整合（`PLATFORM-SECURITY`）。

### [Rethinking Network Topologies for Cost-Effective Mixture-of-Experts LLM Serving](https://arxiv.org/html/2605.00254v1)

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-5 topology/cost model, placement and routing mechanisms`。
- **Mechanism / ownership:** MoE serving topology 必须把 expert placement、token skew、all-to-all bytes、network tiers 与 replica cost 联合建模；更便宜的 topology 会把平均带宽收益换成 hotspot、reconfiguration 和 failure-domain 压力。
- **Evaluation contract:** `§6 serving scenarios and topology comparisons`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§7 Conclusion — exact-v1 has no dedicated limitations section; scenario assumptions and cost model are not universal production measurements`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `INFER-SCHEDULING`；Score V3 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。

### [Jailbroken Frontier Models Retain Their Capabilities](https://arxiv.org/html/2605.00267v1)

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-4 jailbreak construction and capability-preservation protocol`。
- **Mechanism / ownership:** Jailbreak 后保留通用能力意味着 safety case 不能依赖能力退化；风险控制必须落在 action authority、sandbox、monitoring 与 outcome evidence，而不是假设越狱模型不可完成复杂任务。
- **Evaluation contract:** `§5 general and agentic task evaluations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6 limitations: selected frontier models, attacks and tasks; no deployment prevalence claim`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Explanatory Analogy` → `PLATFORM-SECURITY`；Score V3 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。

### [How Language Models Process Out-of-Distribution Inputs: A Two-Pathway Framework](https://arxiv.org/html/2605.00269v1)

exact-v1 §3 先显示 CED、RAUQ、WildGuard score 和 attention entropy 与长度高度相关，并在 length-matched protocol 下接近随机；随后比较 embedding k-NN 与 27 个跨层 trajectory features，在语义 OOD 与 jailbreak 类结构异常上出现互补 crossover。Appendix 的 PCA 对照仍落后于 hand-crafted trajectory。§4/Limitations 把结论限制在六个 360M–7B 模型、六类任务与每类 200 样本，部分任务信号很弱，跨模型 causal replication 也不完整。该 length-matched deconfounding 要求已写入 Ch66 的 OOD evaluation contract。 Score V3：3/3/2 = **8**；最终处置：整合（`PLATFORM-EVALUATION-SYSTEM`）。

### [Token Arena: A Continuous Benchmark Unifying Energy and Cognition in AI Inference](https://arxiv.org/html/2605.00300v1)

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 endpoint-centric continuous benchmark and measurement protocol`。
- **Mechanism / ownership:** Inference benchmark 的原子对象可以是 endpoint/model configuration，而不是模型名称；能耗、质量、延迟与请求策略必须在连续、版本化 contract 中共同记录，且偏好结论不能脱离 evaluator 与 workload。
- **Evaluation contract:** `§4-5 preference/cognition/energy evaluations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6 discussion and limitations on provider drift, observability and evaluator scope`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `PLATFORM-EVALUATION-SYSTEM`；Score V3 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。

### [Semia: Auditing Agent Skills via Constraint-Guided Representation Synthesis](https://arxiv.org/html/2605.00314v1)

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-5 representation synthesis, Datalog constraints and audit pipeline`。
- **Mechanism / ownership:** Agent skill 审计需要把自然语言/代码能力合成为可查询的约束表示，再在调用前检查 source→sink、permission 与 effect；静态分析提高可解释性，却受表示不完备、动态行为与环境依赖限制。
- **Evaluation contract:** `§6 evaluation over skill corpus, attack cases and hardware setup`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§7 Conclusion — exact-v1 has no dedicated limitations section; static abstraction cannot prove dynamic runtime safety`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Layering / Dependency` → `PLATFORM-SECURITY`；Score V3 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。

### [Prompt-Induced Score Variance in Zero-Shot Binary Vision-Language Safety Classification](https://arxiv.org/html/2605.00326v1)

问题与旧路径：A deployable safety score must be tested across semantically equivalent prompts; one first-token probability is not a stable confidence contract. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§3–4 cross-prompt quantities and mean-ensemble method；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§§5–6 locked 15-prompt protocol across 7 models and 2 datasets; Appendix C/F。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§7 discussion and explicit non-implications; ranking/calibration boundary。Artifact：Appendix E.6 names code and analysis artifacts; immutable commit not established。

### [Making Every Verified Token Count: Adaptive Verification for MoE Speculative Decoding](https://arxiv.org/html/2605.00342v1)

问题与旧路径：MoE speculative verification is scheduled by accepted-token utility against the union-of-experts verification cost. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§2.2–3.3 cost model, accepted-length estimate, tree truncation and SGLang integration；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§4 and Appendix B experiments/ablation。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§3.2.3 profiling boundary and §4 workload contract; no dedicated limitations heading。Artifact：implementation described in SGLang; immutable commit not disclosed。

### [Block-wise Codeword Embedding for Reliable Multi-bit Text Watermarking](https://arxiv.org/html/2605.00348v1)

问题与旧路径：Multi-bit watermark extraction and provenance detection are different contracts; designated-codeword verification makes false-positive control explicit. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§3–4 designated-codeword verification, block embedding and FPR/FNR bounds；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§5 plus Appendix D attacks, ablations and detection metrics。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§3.3 adaptive-shift limitation and attack/model scope。Artifact：implementation details disclosed; immutable repository revision not established。

### [MemRouter: Memory-as-Embedding Routing for Long-Term Conversational Agents](https://arxiv.org/html/2605.00356v1)

问题与旧路径：Memory write admission becomes an independently trained, measurable control plane rather than generation-time narration. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§3–4 write-side router and matched harness；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§5 LoCoMo evaluation and factorial analysis。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：limitations/discussion and matched-QA-backbone boundary。Artifact：code/artifact revision not disclosed。

### [From Backward Spreading to Forward Replay: Revisiting Target Construction in LLM Parameter Editing](https://arxiv.org/html/2605.00358v1)

问题与旧路径：exact-v1 §§4–5 证明 backward spreading 把 final-layer residual 线性分配到早层时隐含 Jacobian eigenvector/正定条件；forward replay 改由首个编辑层的 anchor 沿真实 downstream dynamics 生成兼容 target。该机制把 parameter edit 从局部优化技巧提升为跨层 state-transition 与 compatibility contract；现有知识树没有稳定的 model-edit lifecycle owner，进入 Structural Candidate。 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §4.1 Theoretical grounding; §5 Our method; Appendix A.3–A.4；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§6 Experiments; §6.2 Results; Appendix A.8。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§7 Conclusion and Limitations; first-order/Jacobian and LTE scope。Artifact：§1 code link; immutable event-time commit not pinned。

### [Uniform-Correct Policy Optimization: Breaking RLVR's Indifference to Diversity](https://arxiv.org/html/2605.00365v1)

问题与旧路径：RLVR objectives can be indifferent among correct modes; a conditional uniformity term makes diversity an explicit optimization contract. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§2–4 collapse analysis, optimality criteria and UCPO objective；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§5 and appendices across 3 models/5 math benchmarks。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：discussion/limitations; correct-set observability and math-only scope。Artifact：paper-linked GitHub; event-time commit not pinned。

### [Agent Capsules: Quality-Gated Granularity Control for Multi-Agent LLM Pipelines](https://arxiv.org/html/2605.00410v1)

问题与旧路径：Agent dispatch granularity is a runtime decision gated by measured workload quality, not a static pipeline property. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§4–9 programming model, mode ladder and quality controller；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§§10–12 four topologies and LangGraph/DSPy comparisons。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§13 limitations and §7.4 negative result。Artifact：GitHub v1.0-arxiv tag linked by exact-v1。

### [Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies](https://arxiv.org/html/2605.00416v1)

问题与旧路径：Deployment, intervention capture, offline-to-online value learning and redeployment form a versioned embodied-learning loop. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 method sections for DIVL/QAM and fleet data loop；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：real-robot evaluation: 16 robots, 8 tasks。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：limitations/appendices; one fleet and flow-policy scope。Artifact：project artifact linked; immutable event-time commit not established。

### [BWLA: Breaking the Barrier of W1AX Post-Training Quantization for LLMs](https://arxiv.org/html/2605.00422v1)

exact-v1 §3 以 Orthogonal–Kronecker Transformation 同时把 weight 变成适合二值码本的双峰结构并抑制 activation tail，再用 rank-constrained Proximal SVD Projection 修正 residual；§4 的模型族、困惑度、任务与 kernel 结果只支持作者 workload。§5 明确 W1A4 仍不稳定、线性 orthogonal transform 有表达边界，且只覆盖标准 integer format。Ch49 已从 weight-only→weight-and-activation、outlier/calibration、transform+format joint plan、kernel acceptance 与高精度 fallback 建立完整链，因此本项作为 W1A6 受限实例，不重复写入。 Score V3：3/2/2 = **7**；最终处置：已有覆盖（`INFER-TENSORRT-LLM`）。

### [Skills as Verifiable Artifacts: A Trust Schema and a Biconditional Correctness Criterion for Human-in-the-Loop Agent Runtimes](https://arxiv.org/html/2605.00424v1)

问题与旧路径：Agent skills are untrusted executable artifacts whose verification level must gate capabilities and human approval. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 trust schema, biconditional criterion and runtime profile；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：adversarial-ensemble exercise/reference runtime。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：threat model and verification-level boundary。Artifact：reference implementation linked; immutable revision not established。

### [AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/html/2605.00425v1)

问题与旧路径：Multi-turn agentic RL can use response-level entropy dynamics as an intrinsic credit and exploration-control signal without a separate process reward model. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§3–4 response-level entropy geometry and adaptive modulation；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§5 ALFWorld, WebShop and SWE-bench-Verified across 1.5B–32B models。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§6 compute cost and Appendix D base-RL/implementation boundary。Artifact：algorithm and prompts disclosed; immutable code revision not established。

### [Thinking in Text and Images: Interleaved Vision–Language Reasoning Traces for Long-Horizon Robot Manipulation](https://arxiv.org/html/2605.00438v1)

exact-v1 §3 生成全程交错 text/keyframe trace，缓存后由 closed-loop action decoder 同时读取 live observation、instruction 与 trace；§4 的 trace ablation 支持两种模态互补。§5 明确证据只来自模拟 manipulation，假定生成 trace 时 workspace 静态且充分可见；完整 trace 约有 10 秒前置延迟，scene change、遮挡或其他 agent 介入会产生 stale plan。故 trace 只能拥有 proposal/memory 权，controller 与 observation 仍拥有提交和事实。全局 multimodal trace 的版本、失效和重规划已写入 Ch26。 Score V3：3/2/3 = **8**；最终处置：整合（`MULTIMODAL-EMBODIED-VLA`）。

### [CleanBase: Detecting Malicious Documents in RAG Knowledge Databases](https://arxiv.org/html/2605.00460v1)

问题与旧路径：RAG ingestion needs document-level security evidence; similarity-clique detection is one bounded sensor rather than a trust proof. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§3–4 similarity graph, threshold and clique detector；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§5 experiments and theoretical FP/FN bounds。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：limitations/adaptive-attacker and embedding-distribution boundary。Artifact：GitHub linked in v1; immutable commit not pinned。

### [SAGA: Workflow-Atomic Scheduling for AI Agent Inference on GPU Clusters](https://arxiv.org/html/2605.00528v1)

问题与旧路径：Agent workflow, not isolated request, becomes the scheduling/fairness/cache-lifetime unit. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§3–8 AEG, cache, batching, AFS and implementation；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§9 64-A100 evaluation and ablations。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§1.5 explicit limitations and §9.8 trade-offs。Artifact：vLLM-based implementation; immutable event-time patch not disclosed。

### [AGoQ: Activation and Gradient Quantization for Memory-Efficient Distributed Training of LLMs](https://arxiv.org/html/2605.00539v1)

问题与旧路径：Activation bit width and gradient communication precision become layer/stage-aware training-runtime policies. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 method sections: layer/stage activation policy and 8-bit gradient All-Reduce；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：experiments on 8B–32B LLaMA up to 64 GPUs。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：ablation/discussion; architecture, precision and cluster boundary。Artifact：implementation availability noted; event-time commit not pinned。

### [Sim-FA: A GPGPU Simulator Framework for Fine-Grained Asynchronous Pipeline Analysis](https://arxiv.org/html/2605.00555v1)

问题与旧路径：GPU performance evidence for asynchronous attention pipelines must model TMA, barriers, warp specialization and cache traffic rather than rely on a coarse roofline alone. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§3–5 traffic model, event-driven TMA simulation and FA3 trace translation；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§§5–6 H800 end-to-end and analytical-model validation。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§4.1 abstraction scope and §7 simulator/model comparison boundary。Artifact：instrumented FA3/simulator described; immutable artifact revision not established。

### [Jailbreaking Vision-Language Models Through the Visual Modality](https://arxiv.org/html/2605.00583v1)

问题与旧路径：Safety post-training and threat models must treat the visual channel as an active intent-bearing attack surface rather than assume text-domain alignment composes across modalities. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §3 four visual attack constructions and shared protocol；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§4 six frontier VLM evaluation with judge aggregation。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§5 discussion, limitations and mitigations; threat-model and judge boundary。Artifact：paper-linked GitHub; immutable event-time commit not pinned。

### [LLM-Emu: Native Runtime Emulation of LLM Inference via Profile-Driven Sampling](https://arxiv.org/html/2605.00616v1)

问题与旧路径：A serving emulator preserves the real HTTP, scheduler, KV and output paths while replacing only GPU execution with profiled samples. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§2–4 vLLM-native emulation and profile sampler；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§5 two GPU/four-model/arrival-process evaluation。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§6 limitations; TTFT and profile portability boundary。Artifact：vLLM modification described; immutable commit not disclosed。

### [Affordance Agent Harness: Verification-Gated Skill Orchestration](https://arxiv.org/html/2605.00663v1)

问题与旧路径：Skill orchestration needs verifier-owned admission and failure recovery; perceptual affordance confidence cannot directly authorize action. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 harness architecture, verifier gate and skill orchestration sections；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：affordance/skill execution experiments and failure analysis。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：open-world perception, verifier and embodiment boundary。Artifact：harness artifact described; immutable revision not established。

### [Beyond Benchmarks: MathArena as an Evaluation Platform for Mathematics with LLMs](https://arxiv.org/html/2605.00674v1)

问题与旧路径：Evaluation for fast-moving capabilities needs continuously refreshed, contamination-resistant tasks with versioned scoring rather than a static benchmark snapshot. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 platform/task lifecycle and continuously refreshed evaluation design；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：competition/problem-set evaluations and model comparisons。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：mathematics-only, organizer and contamination boundary。Artifact：platform is public; event-time dataset revision not pinned。

### [Eliminating Hidden Serialization in Multi-Node Megakernel Communication](https://arxiv.org/html/2605.00686v1)

问题与旧路径：Fine-grained MoE overlap fails across nodes when per-transfer fences serialize the NIC; signaling and ordering ownership must be separated. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 §§3–5 root cause, decoupled signaling, NIC ordering and implementation；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：§6 multi-platform/backend/model evaluation and ablation。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：§8 discussion; transport, topology and compute/communication regime boundary。Artifact：Triton-distributed case described; event-time patch not pinned。

### [Learning How and What to Memorize: Cognition-Inspired Two-Stage Optimization for Evolving Memory](https://arxiv.org/html/2605.00702v1)

问题与旧路径：Long-term memory needs separately optimized write/update behavior and answer-time use; static hand-written memory update rules are not a durable policy. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 two-stage optimization for memory extraction/update and use；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：long-horizon personalization evaluations and ablations。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：preference-memory task, judge and model-family boundary。Artifact：artifact revision not disclosed。

### [To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling](https://arxiv.org/html/2605.00737v1)

问题与旧路径：Tool invocation is an admission decision whose benefit, latency and failure cost must be estimated; availability alone does not justify a call. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 tool-call utility model, assessment protocol and optimization framework；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：multi-model/tool-use evaluations and cost-quality ablations。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：toolset, task and evaluator boundary。Artifact：framework artifact revision not disclosed。

### [Characterizing the Expressivity of Local Attention in Transformers](https://arxiv.org/html/2605.00768v1)

exact-v1 §3–§5 在 formal-language recognizer 框架中证明 local-only 与 global-only 对应不同 temporal-logic fragment，hybrid 覆盖更丰富的类别；formal-language 与自然语言实验只作一致性证据。边界同样重要：用多层 1-local 可以换 expressivity，但增加最多与窗口相关的深度；足够强的位置编码可缩小理论差距，论文的固定精度、识别器假设也不是任意 LLM 能力定理。该互补表达力解释已写入 Ch22，而没有外推成性能通则。 Score V3：3/2/2 = **7**；最终处置：整合（`MODEL-LONG-CONTEXT`）。

### [Make Your LVLM KV Cache More Lightweight](https://arxiv.org/html/2605.00789v1)

问题与旧路径：Vision-token KV compression is prompt-conditioned and must preserve modality/token/position identity; the mechanism is a bounded implementation case. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 method sections: prompt-guided message passing and progressive vision-token compression；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：eight LVLMs/eight public benchmarks。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：ablation/limitations; visual-task and selected-token boundary。Artifact：artifact revision not disclosed。

### [RunAgent: Interpreting Natural-Language Plans with Constraint-Guided Execution](https://arxiv.org/html/2605.00798v1)

问题与旧路径：Natural-language plans need an executable intermediate representation with step constraints, rubrics and recovery transitions. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 system/method sections: agentic language, constraints, rubrics and correction；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：Natural-plan and SciBench evaluation。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：limitations/discussion; plan quality and evaluator boundary。Artifact：platform artifact revision not disclosed。


### 本次 Books 汇总

- 已存在且无需重复写入：恢复项 `2605.00078` 的 training-only future latent / deploy-time prior 边界已由 Ch25–26 承载；`2605.00422` 的 weight+activation quantization、outlier/calibration、transform+format+kernel acceptance 已由 Ch49 承载。
- 已写入唯一 owner：`2605.00236` → Ch72 `PLATFORM-SECURITY`；`2605.00269` → Ch66 `PLATFORM-EVALUATION-SYSTEM`；`2605.00438` → Ch26 `MULTIMODAL-EMBODIED-VLA`；`2605.00768` → Ch22 `MODEL-LONG-CONTEXT`。它们分别补齐 attention routing threat、OOD length deconfounding、multimodal trace staleness、global/local expressivity complementarity。
- 旧报告已落实的 Books marker 没有因本次报告迁移被覆盖或删除；被降级的旧候选不再作为本窗采用证据，相关既有正文的独立适用性由其 owner/其他证据维持，本任务不做破坏性删除。

## 5. 缺口与下一步

本窗没有尚可执行的扫描、审阅或 Books 写回。独立复核已检查十四源边界、`387 = 39 + 348 + 0` 守恒、六项恢复证据、四项降级理由以及四处 Books 实际正文。

**终态保留项：** DeepSeek 历史公开入口缺可分页日级研究目录；该限制不支持正面证据、Books 或无遗漏断言。**定点重开条件：** 若官方出现可唯一定位到本窗的日级索引或 primary event，仅重开该来源与对应 Source Family。当前没有需要用户提供的 exact-version 论文正文；所有 arXiv 候选的 v1 HTML 可访问，页面未显示撤回标记。

## 6. 复核

复核者：`/root`（非作者 fresh-context 复核）

结论：通过

独立复核重新核对了固定窗口、十四个 Daily 来源、387 个 identity 的题摘贡献重筛与 Source Family 去重。四项旧候选降级理由均符合当前长期贡献门槛；六项恢复材料的 exact-v1 身份、机制、evaluation 和限制与正文结论相称。`2605.00236`、`2605.00269`、`2605.00438`、`2605.00768` 的 Books 增量已分别写入唯一 owner，marker 成对，位于机制正文而非 Review notes，并保留 workload、证据边界、trade-off、fallback 与旧方案适用条件。其余恢复项已有具体正文覆盖，没有强行追加。未发现撤回候选、重复 family、未处理 Books 决定或可执行待办；机器校验只作为格式证据，不替代本次语义复核。未修改月索引、Weekly 或 Learning State。
