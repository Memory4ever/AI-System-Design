# Daily Research — 2026-08-31

**规范：** V3
**窗口：** 2026-08-30T09:00:00+08:00 ～ 2026-08-31T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T19:57:33+08:00

## 1. 结论

本窗重新按 14 个每日来源检查，arXiv 以官方 `new` 公告而非作者提交时间归属；2026-08-31 08:00 的公告批次包含 457 个去重身份。完整巡检标题，对含义不明确或可能改变大模型/大模型 Infra 长期判断的条目阅读完整摘要后，独立复筛最终保留 37 个材料家族；入选精确版本未见 withdrawn 标记。研究机构入口与官方仓库没有发现另一个满足准入门槛、且首次公开时间落入本窗的独立家族。

最重要的变化不是某个单点 benchmark，而是四组系统边界被进一步收窄：近似推理必须保留 exact verifier 或明确质量合同；安全、隐私与路由评测必须把可观察状态、攻击预算和下游栈写入 evaluation identity；模型压缩、MoE 与长上下文的优化都必须回到真实 data movement、request energy 和 deployment artifact；Agent 的可信执行还要把 policy、telemetry、effect 与 recoverable state 放在模型之外。独立复筛纠正了原稿的过早关闭：最终保留 37 项而非 16 项，均已完成与评分相称的证据审阅和 Books 对读。18 项长期增量已经写入对应 owner，19 项由现有章节实质承载；写后独立复核确认新增正文的机制边界与相邻衔接成立。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/Index 与相邻公开记录按事件日期检查；本窗无新机制正文 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 与 Alignment Science 日期列表检查至窗口末 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind Blog/Publications 与 Google Research publication 入口按日期检查 | 已检查 | 无 |
| SRC-META-AI | 官方 Research/Results 日期列表检查至窗口末 | 已检查 | 无 |
| SRC-QWEN | 官方文章、模型与论文列表按首次公开日期检查，并与 arXiv 家族去重 | 已检查 | 无 |
| SRC-DEEPSEEK | 官网研究入口和官方仓库发布面按日期检查 | 已检查 | 无 |
| SRC-MOONSHOT | Kimi Blog、Research 与官方仓库事件按首次公开日期检查 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Research“全部”列表与官方仓库逐项检查至 Aug28 后的窗口水位 | 已检查 | 无 |
| SRC-ZAI | Research、发布说明与官方仓库按日期检查 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Research、Blog 与论文目录按日期检查，并与 arXiv 去重 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 官方技术博客与仓库发布入口按日期检查 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 官方论文、博客与仓库按日期检查 | 已检查 | 无 |
| SRC-MINIMAX | Research/Blog 与官方仓库按日期检查 | 已检查 | 无 |
| SRC-ARXIV | 2026-08-31 官方 `new` 公告批次；457 个去重身份完成全标题巡检，含糊/高信号项完整题摘筛选；独立复筛将候选从 16 项校正为 37 项 | 已检查 | 无 |

本窗没有触发需要额外扫描的按需来源。

## 3. 候选与判断

下表公开时间表示材料进入本窗的官方 `new` 公告时段，不是作者提交时间。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Accelerating LLM Inference via Vector Index Based Output Embeddings](https://arxiv.org/html/2608.27460v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 将小 batch 的全词表输出投影改写为近似 MIPS，并显式暴露 index recall、batch crossover 与完整分布语义；2 + 2 + 3 = 7 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Grounded Checklist Partial Credit for Agent Skill Trajectories](https://arxiv.org/html/2608.27487v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 用 human-owned rule、log-grounded checklist、abstention 与官方 verifier 分离过程证据和最终成功；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ROPE: Routed Origin Policy Enforcement](https://arxiv.org/html/2608.27496v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 将跨 Agent 消息的 origin 与 delegation policy 绑定到 effect-time enforcement；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Quantization-Triggered Backdoors](https://arxiv.org/html/2608.27512v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 证明高精度 checkpoint 的安全通过不能继承到 many-to-one rounding 后的部署 artifact；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [DAMP: Decay-Aware Mixed-Precision Recurrent-State Quantization](https://arxiv.org/html/2608.27513v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 将 write-once KV 量化与反复读写、误差反馈的 recurrent-state 量化分开，并以 error energy × decay persistence 选择精度；2 + 2 + 3 = 7 | 深入完成 | 整合：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Trajectory-Level Speculative Decoding for Diffusion Language Models](https://arxiv.org/html/2608.27514v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 将 speculative proposal/verification 从左到右 token 推进改写为 denoising trajectory；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Code as Worlds](https://arxiv.org/html/2608.27549v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 把物理世界假设表示为可执行、可渲染、可反驳的程序，并通过 propose—execute—verify—revise 闭环恢复动态；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [LongGuard](https://arxiv.org/html/2608.27580v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 区分 context 截断与危险证据比例稀释，改变长上下文 guardrail 的 evaluation slices；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [If Agents Were Angels, No Governance Would Be Necessary](https://arxiv.org/html/2608.27646v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 在可信 Tool 边界对 operation/resource、query 与 response 分层执行 owner ceiling，Agent policy 只能收窄不能扩大；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Memorization Is Not Extraction](https://arxiv.org/html/2608.27782v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 形式化分离单条记录影响与自适应秘密提取，修正隐私指标替代关系；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [CEDAR: Automata as Verifiable Interfaces for Language-Guided Embodied Action](https://arxiv.org/html/2608.27797v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 把自然语言的持续约束编译为可组合、可复用、可由反例修正的 trace automata，而非每步重新提示；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [ContextLeak](https://arxiv.org/html/2608.27800v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 揭示恶意 Tool metadata 可诱导 Agent 把 prompt、history 与 tool list 主动写进调用参数，补出 implementation exfiltration 之前的缺失边界；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [CURA: Certified Runtime Alarms for Computer-Use Agents](https://arxiv.org/html/2608.27808v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 用 harness telemetry 的 sequential test 与显式 false-alarm budget 替代 Agent 自报成功/失败；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-MONITORING，[Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [TerraceMoE](https://arxiv.org/html/2608.27874v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 用两跳 collective 成本模型说明 MoE 层次化拓扑只有越过 breakeven 才值得启用；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Request and Token Energy Costs](https://arxiv.org/html/2608.28044v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 分离每请求固定成本与每 token 边际能耗，避免 token-normalized 指标掩盖总能耗上升；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-COST，[Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [Speculative Probing](https://arxiv.org/html/2608.28099v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 复用 MTP/draft hidden states 产生低边际成本风险信号，但不转移安全 commit 权；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-MONITORING，[Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [Cross-Session Decomposition Attacks](https://arxiv.org/html/2608.27945v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 证明 prompt-local 安全检查看不到跨会话分散、在外部重组的隐含目标，要求按 intent 邻域恢复跨会话风险状态；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Not to Break, but to Attest](https://arxiv.org/html/2608.27954v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 用 adversarial probe 放大批准模型与部署模型的 logit drift，再以零知识证明形成不暴露权重的 artifact attestation；2 + 3 + 3 = 8 | 深入完成 | 整合：PLATFORM-MODEL-REGISTRY，[Ch59](../../../../books/part-06-ai-infrastructure/59-model-registry.md) |
| [AERA: Adaptive Evidence Residual Allocation](https://arxiv.org/html/2608.27964v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 将“当前看起来多自信”与“额外计算是否仍有恢复价值”分开，处理 reasoning correctness 的非单调轨迹；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Parser States Already Know](https://arxiv.org/html/2608.28276v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 让结构化生成的 parser transition 成为 KV retention policy 的输入；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [VICT: Verifier-Instrumented Credit Tracing](https://arxiv.org/html/2608.28128v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 让 verifier 输出可执行/evidence atoms 与依赖边，将 terminal correctness 守恒地追溯到行动而非凭 hindsight 猜因果；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [HARTS](https://arxiv.org/html/2608.28158v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 为 hybrid-attention 的任意 rollout tree 联合规划 prefix compression、microbatch/DP/slot 与可微 state handoff，避免共享前缀重复训练；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Stay Within Your Bounds](https://arxiv.org/html/2608.28229v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 证明 prefix-feasible 不等于有限 token budget 内可接受，以 PDA reachability 与 distance-to-acceptance 提供 sound completion；3 + 2 + 3 = 8 | 深入完成 | 整合：MODEL-SAMPLING，[Ch20](../../../../books/part-02-model/20-sampling.md) |
| [A Probabilistic Interpretation of KV Cache Eviction](https://arxiv.org/html/2608.28293v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 将 heuristic eviction 解释为有偏估计器，并暴露 eviction 后 decode correction 这一此前缺失的状态责任；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Layered LLM Defenses as an Ensemble](https://arxiv.org/html/2608.28327v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 实测 defense layers 的正相关共同失效，推翻“多层防御残余风险自然相乘”的独立性假设；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [EvoUndo](https://arxiv.org/html/2608.28363v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 将 Agent self-modification 的可恢复性拆为 verification、exact state grounding、witness semantics 与 recovery-language expressivity；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [When Linguistic and Internal Confidence Diverge](https://arxiv.org/html/2608.28382v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 分离 verbal/internal association、magnitude agreement 与 correctness calibration，表明更分散的自报分数仍不是已校准概率；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Program Learning via Symbolic Backpropagation](https://arxiv.org/html/2608.28421v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 将可验证 reasoning 外置为确定性/神经 primitive 组成的程序，并用 loss-guided search 修订；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Sliding-Window Attention Beats Linear Attention](https://arxiv.org/html/2608.28444v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 以受限反例收窄训练后线性 Attention 替换固定窗口 Attention 的适用范围；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Fidelity Is Not Enough](https://arxiv.org/html/2608.28439v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 显示最终值正确仍可能来自未读来源的猜测，要求 dispatch-level trace 与 fidelity/result evaluator 分离；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-TRACE，[Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [COVER: Coalition-Based Evaluation for Model Routing](https://arxiv.org/html/2608.28475v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 要求路由比较固定公开信息、下游栈与合法候选族，避免把局部排名外推为通用策略；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Recognition Without Enforcement](https://arxiv.org/html/2608.28502v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 显示模型能识别伪造 authority 仍可能执行，要求外部 reference monitor 拥有 enforcement；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Communication-Efficient MoE Layer Reconfiguration](https://arxiv.org/abs/2608.28511v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 以路由层集中、dense/token-mixing 层补偿降低训练通信，形成新的架构—runtime 联合分支；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：MODEL-MOE / TRAIN-DISTRIBUTED-TRAINING，[Ch21](../../../../books/part-02-model/21-moe.md)、[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [ContextPilot](https://arxiv.org/html/2608.28476v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 用 planning/memory/offload actions 与 branch-relative action credit 训练主动 Context 管理，但最终 effect 仍由 runtime 提交；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [Offline-Verifiable Accountability for Cross-Organization Agent Messaging](https://arxiv.org/html/2608.28542v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 将 sender、delegation、append-only continuity、witness checkpoint 与 receiver receipt 组成离线可验 evidence bundle；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Logos: An Agent Harness on a Cross-Process Bus](https://arxiv.org/html/2608.28553v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 将 capability 隔离为进程，以 append-only transcript 承载跨步状态并在 tool-call 四个边界验证无重复 effect 的恢复；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-WORKFLOW / AGENT-PLATFORM，[Ch81](../../../../books/part-07-agent/81-workflow.md)、[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [A Formal Limitation on Learning Human Language from Text](https://arxiv.org/html/2608.28560v1) | 2026-08-31T08:00:00+08:00 ～ 2026-08-31T09:00:00+08:00 | 给出文本形式无法恢复缺失外部变量的信息论边界，明确 Context/Tool/abstention 的责任；3 + 2 + 3 = 8 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |

## 4. 证据与知识整合

### [Accelerating LLM Inference via Vector Index Based Output Embeddings](https://arxiv.org/html/2608.27460v1)

exact-v1 将全词表输出投影改写为近似最大内积搜索：HNSW 召回少量候选 token，再交给原有 logit processor。作者主要在 CPU FP32、batch 1、Gemma/Llama/Qwen 小模型上报告结果，Top-K 召回和 LLM-judge 质量不能证明保持完整 softmax 分布；batch 增大后连续 GEMM 会重新取得复用优势。Ch49 已将近似索引、模型 revision、质量校准和 batch crossover 写成 execution-plan 分支，而非通用替代。

### [ROPE: Routed Origin Policy Enforcement](https://arxiv.org/html/2608.27496v1)

论文要求消息 origin 与 delegation scope 在路由和执行时保持可验证，防止 Agent 通过转述把不可信内容升级为 authority。它仍无法处理消息本身已含有害意图、被 policy 明确准入的恶意字段或受委托敏感参数。Ch72 已以 authenticated principal、单调收窄 delegation 与 effect-time authorization 承载该边界，因此无需重复写入。

### [Quantization-Triggered Backdoors](https://arxiv.org/html/2608.27512v1)

作者构造的翻译后门只在量化后的 artifact 触发，并可跨若干 quantizer 转移；平均 BLEU 不能替代 targeted behavior test。证据不能推出所有量化都会制造后门，却足以推翻“FP16 安全通过可自动继承到部署格式”的假设。Ch72 已要求按实际 model × quantizer × bit width × calibration × kernel 重新执行安全 release gate。

### [Trajectory-Level Speculative Decoding for Diffusion Language Models](https://arxiv.org/html/2608.27514v1)

Diffusion LM 的状态不是已提交前缀加下一个 token，而是 mask、位置选择与逐轮修订组成的 denoising trajectory；proposal 与 verifier 必须在这条轨迹上定义 acceptance 和 rollback。作者结果绑定受测 diffusion models、序列长度和硬件，不能外推为所有并行生成的 exact speedup。Ch24 已有 proposal—verification—commit 的 mutable-state 主线，本材料属于现有覆盖。

### [LongGuard](https://arxiv.org/html/2608.27580v1)

0.25k～32k 的 SafetyNIAH 与 15 个 guardrail 显示：即使危险片段仍在可见窗口，benign context 增长也可能通过比例稀释降低 unsafe recall；这不同于截断。合成数据与训练外缓解不证明生产发生率。Ch72 已把长度、危险占比、位置、重复方式与语言拆为独立 evaluation slices，并保留分块扫描的误报和 TTFT 代价。

### [Memorization Is Not Extraction](https://arxiv.org/html/2608.27782v1)

exact-v1 在特定定义下给出 memorization 与 adaptive extraction 不互相控制的紧界和分离构造，并以 48 个 planted secrets 作有限实验。它不提供任意真实语料的泄漏率，却足以说明平均 counterfactual influence、membership test 和有限攻击成功率不能互相替代。Ch72 已把邻接关系、先验可猜测性、查询预算与攻击接口纳入隐私结论。

### [TerraceMoE](https://arxiv.org/html/2608.27874v1)

论文把两层拓扑的第二次 collective、到达算子和链路比率写入成本模型；参考 16×8 ranks 下的 breakeven 因融合和软件开销而变化，且作者测得的平台并未真正处于层次化最优区间。它证明“拓扑存在”不足以授权两跳执行，而不是证明一种 collective 普遍更快。Ch36 已以 payload、participant set、拓扑和 critical path 决定 collective plan。

### [Request and Token Energy Costs](https://arxiv.org/html/2608.28044v1)

请求能耗包含固定 prefill/setup 与边际 decode 两部分；输出变长时每 token 数字可能下降，同时单请求总能耗仍上升。作者测量只覆盖披露硬件、模型和请求分布，不能生成跨部署常数。Ch70 已要求以 request、token、SLO 与质量共同解释成本，故保持已有覆盖。

### [Speculative Probing](https://arxiv.org/html/2608.28099v1)

若 runtime 已训练 MTP/draft head，可复用其 hidden states 驱动轻量风险 probe，使 speculative work 同时产生 token proposal 与监控信号。收益依赖 draft 训练、层选择和模型 revision，probe 仍不是授权者。Ch67 已将它写成可回退的 sensor 分支：没有可靠 draft head 或分布漂移时改用独立 guard/evaluator。

### [Parser States Already Know](https://arxiv.org/html/2608.28276v1)

结构化生成中的 parser state 能区分未来仍需的 schema/history，并据此选择 KV 保留动作；作者使用离线 calibration 和粗粒度 layer/action groups，未证明任意 grammar 或 workload 都能获得同样收益。Ch45 已把 parser/role-conditioned retention、policy identity 与未校准时回退普通 eviction 连成现有主线。

### [Program Learning via Symbolic Backpropagation](https://arxiv.org/html/2608.28421v1)

论文把 reasoning 外置为确定性与神经 primitives 组成的可执行程序，再用 backward/loss-guided search 修订结构。LiveCodeBench、Tau2Bench 等结果只能支持披露任务中的可行性，不证明开放环境的搜索收敛、工具正确或副作用安全。Ch81 已让 durable workflow 拥有显式 state、verifier、checkpoint 和 effect boundary，因此无需按论文名新增正文。

### [Sliding-Window Attention Beats Linear Attention](https://arxiv.org/html/2608.28444v1)

作者在特定 post-training 替换、模型和长上下文任务上发现 sliding-window+sinks 优于若干 linear attention 分支，并报告 2～10× 的受限任务差异。它没有比较从头训练的 hybrid/linear architecture，也不覆盖任意 token budget。Ch22 已保留 dense、windowed、recurrent 与 hybrid 的条件分支；该反例收窄线性替换的适用范围，不需要再追加另一份技术列表。

### [COVER: Coalition-Based Evaluation for Model Routing](https://arxiv.org/html/2608.28475v1)

COVER 固定 public information boundary、下游 stack 与合法 team family 后枚举 coalition，并报告相对该栈的 routing regret。它不能证明某个 router 在不同模型集、成本函数或 evaluator 上普遍最优。Ch66 已要求将 candidate set、information visibility、downstream workflow 与 measurement contract 一起版本化，故判已有覆盖。

### [Recognition Without Enforcement](https://arxiv.org/html/2608.28502v1)

受测模型可以识别伪造 authority，却仍在部分配置中执行，说明 recognition signal 与 enforcement ownership 不同。平均 attack execution 较低但高度集中且依赖配置，不能推出统一内部 trust representation。Ch72 已将模型判断限制为 sensor/proposal，外部 reference monitor 才拥有 effect commit。

### [Communication-Efficient MoE Layer Reconfiguration](https://arxiv.org/abs/2608.28511v1)

论文将 routed expert layers 集中到较少位置，并插入 dense/token-mixing 层补偿，尝试以架构重排减少频繁通信；2B～31.5B 的 matched-parameter 训练支持作者 operating point，31.5B 的 GPU-hour 降幅不能外推到其他拓扑、kernel 或质量目标。Ch21 已说明 MoE 容量与路由层位置的模型代价，Ch36 已拥有 collective critical path，现有两章共同承载该架构—runtime 分支。

### [A Formal Limitation on Learning Human Language from Text](https://arxiv.org/html/2608.28560v1)

论文从信息论上说明只观察文本形式时，若意义依赖未进入输入的外部变量，任何文本学习器都无法唯一恢复它；人工语言、中文零代词和颜色指称实验只覆盖不超过 14B 的模型。它不证明具体回答必然不可知，也不让任意检索结果自动成为真值。Ch5 已把缺失变量的责任交给 Context、可追溯检索、工具 observation、用户确认或 abstention，并保留纯文本任务的简单基线。

### [Grounded Checklist Partial Credit for Agent Skill Trajectories](https://arxiv.org/html/2608.27487v1)

GCPC 先由人定义可复用规则，再由模型按 task instruction 与 official verifier 实例化 checklist；judge 只使用 execution log，证据不足时 abstain，最后由脚本合并官方结果。在 4,455 条 SkillsBench trajectory 及两组迁移数据上，它能看到 pass@1 未改变时的局部进退；但 checklist 实例化与 judge 仍可能共偏，AUC 也只证明区分度。Ch66 已要求过程、最终状态、证据缺失和 evaluator identity 分离，因此判已有覆盖。

### [DAMP: Decay-Aware Mixed-Precision Recurrent-State Quantization](https://arxiv.org/html/2608.27513v1)

反复 quantize—read—update—write 的 recurrent matrix 会把一次 rounding residual 继续传入后续状态，不能照搬静态 weight 或 write-once KV 的量化假设。DAMP 用离线校准的 reconstruction-error energy 与 decay persistence 选高精度 channel，并把固定分区打包进 fused update；Qwen3.6-35B 与 Kimi-Linear-48B 的六项任务支持 9.9-bit operating point。它仅覆盖两种架构、SGLang 与披露硬件，4-bit 仍未恢复 FP32；Ch54 需要补入 persistent recurrent state 的 precision–residency identity 与校准失效回退。

### [Code as Worlds](https://arxiv.org/html/2608.27549v1)

论文把 object state、physical parameters、dynamics 与 rendering 写成 executable world hypothesis，再由 Agent 在 observation 上 propose、execute、render、verify、revise。QuantiPhy 等结果只支持这套表示可形成受限物理监督，不能证明代码等于真实因果模型，也不能跨 simulator/renderer 自动迁移。Ch25 已从 observation generation 推进到 controllable transition、simulator 与可反驳 world state，故无需重复写入。

### [If Agents Were Angels, No Governance Would Be Necessary](https://arxiv.org/html/2608.27646v1)

OBPE 在模型外授权 typed operation/resource，先收窄 query，再过滤 row/field 或 mask response；data owner 给出 ceiling，Agent policy 只能收窄，并给出 order-independence 与 non-widening 的条件。3,621 次 Jira/ServiceNow mock trials 显示 trace failure 下降但 fulfillment 也下降；reconstruction、row-count oracle、writes、durable approval 与 history policy 未闭合。Ch72 已由 reference monitor、schema-owned policy、effect-time authorization 和 response shaping 承载这条责任边界。

### [CEDAR: Automata as Verifiable Interfaces for Language-Guided Embodied Action](https://arxiv.org/html/2608.27797v1)

自由生成程序难以让持续约束复用、组合或由失败 trace 修复；CEDAR 将 skill 与 specification 表示为 event-trace 上的 deterministic finite automata，通过 intersection 把新约束纳入 controller，并用 counterexample 更新语义判断。Minecraft 对照只证明所测 API/约束下优于 program-generating baseline，正则语言也不能表达所有连续物理与长程约束。Ch26 需要补入“语言约束 → 可验证状态机 → low-level action”这一受限编译分支及表达力回退。

### [ContextLeak](https://arxiv.org/html/2608.27800v1)

论文补足了工具窃取链中常被忽略的一段：恶意 Tool 的 name/description 不只诱导被选择，还可诱导 Agent 把 user prompt、history 与 tool list 作为调用参数主动交出。攻击使用 shadow contexts 上的 RL 生成 metadata；受测 detector 对语义自然的描述漏报很高，但实验主要是首次单次工具调用，尚未覆盖完整 trajectory。Ch72 应把 argument construction 也纳入 data-loss boundary：registry 扫描、tool implementation 审计和出站网络控制都不能替代参数级敏感数据策略。

### [CURA: Certified Runtime Alarms for Computer-Use Agents](https://arxiv.org/html/2608.27808v1)

CURA 从只读 harness telemetry 构造 sequential CUSUM test，以 success trajectories 校准 false-alarm budget，并把 alarm 交给外部 overseer；它不依赖 Agent 的 verbal self-report。在 361 个 OSWorld tasks 中能提前发现部分失败，但证书只约束误报，不约束漏报；换 planner 后阈值漂移，belief-level、quiet 与对抗规避失败不可见。Ch67 应加入“self-report → external telemetry sensor → budgeted alarm → escalation”的演进和按 runtime regime 重校准要求。

### [Cross-Session Decomposition Attacks](https://arxiv.org/html/2608.27945v1)

单会话 guard 看不到攻击者把允许的子问题分散到独立交互、再在外部重组为禁止目标。论文给出的 conditional transfer bound 只说明 reference distribution 已含分散支撑时，较低 excess loss 会收紧部署风险与 reference risk 的差距；600-intent 结果固定了 decomposer/composer，但模型族仍有训练和对齐混杂。Ch72 应把 safety state 的 identity 从单 prompt/history 扩到跨会话 latent intent neighborhood，同时保留隐私、误关联与 retention 代价。

### [Not to Break, but to Attest](https://arxiv.org/html/2608.27954v1)

论文不要求公开权重，而是构造 token/embedding/stress probes 放大 approved model 与 deployed model 的 logit drift，再用 Groth16 证明 probe evaluation。多架构、tampering scenario 与 1～50 probes 支持受限可行性，但 adversarial probes 只能覆盖被搜索到的差异，接口与 tokenizer 变化也会改变 attestation identity。Ch59 应补入“artifact digest → behavior-sensitive probe set → privacy-preserving proof”的可选发布分支，并明确它不是完整模型等价证明。

### [AERA: Adaptive Evidence Residual Allocation](https://arxiv.org/html/2608.27964v1)

AERA 不用当前 confidence 直接推断停止，而从 answer distribution、temporal change、re-solving、semantic 与 compute 特征预测下一段计算是否仍可能恢复更好答案；future correctness 只作离线标签。GSM8K/GPQA 的有限结果支持 checkpoint correctness 可非单调和按题分配预算，但不证明跨模型、开放任务或实时 SLO 的校准。Ch56 应把 current evidence 与 residual value-of-compute 分成两份状态，并保留固定预算/独立 verifier fallback。

### [VICT: Verifier-Instrumented Credit Tracing](https://arxiv.org/html/2608.28128v1)

VICT 让 verifier 输出可执行或 evidence atoms 及依赖有效的 proof edges，再把通过的 terminal reward 追溯到最早产生证据的 action；无法证明依赖时 abstain，避免用语言相关性伪造 causal credit。ALFWorld/WebShop 只能支持特定 verifier 与环境中的可行性。Ch33 已区分 terminal gate、可观测 action credit、sign conservation 与 verifier bias，因此判已有覆盖。

### [HARTS](https://arxiv.org/html/2608.28158v1)

Hybrid-attention rollout tree 不能只按 full-attention prefix cache 复用：chunkwise recurrent state 需要在分支边界恢复并保持可微 handoff。HARTS 联合规划 compact-token work、microbatch、DP replica 与 slot，最小化所定义 packed model 下的 sequential linear-attention calls，并保留 activation recomputation 与 no-drop top-k MoE multiplicity。4.81～4.87× 是 SWE-bench-derived workload 与披露并行配置的 author result，不证明任意 rollout tree；Ch36 应补入 tree topology、state handoff、semantic multiplicity 与 replay bound 的共同 execution identity。

### [Stay Within Your Bounds](https://arxiv.org/html/2608.28229v1)

局部 grammar mask 只保证当前 prefix 仍可扩展；tokenizer–grammar mismatch 与有限 horizon 下，合法 prefix 仍可能来不及到 accepting state。论文用 bounded PDA summaries、reachability 和 distance-to-acceptance 做 pruning/reranking，保证返回项被 grammar 接受；近似搜索不保证最高概率或语义正确，预处理与 beam 成本也依赖 grammar。Ch20 应将 prefix feasibility 与 finite-budget acceptance 分开，并保留 parser failure、budget exhaustion 和 unconstrained fallback。

### [A Probabilistic Interpretation of KV Cache Eviction](https://arxiv.org/html/2608.28293v1)

论文把 KV eviction 形式化为 expectation estimation，指出常见 heuristic 可视为 zero-variance biased estimator，并给出 sampling 与 decode-time correction 分支；同时证明一般问题计算困难。实验只说明所测任务和 compression budget 下更稳健，不能把 corrected estimate 写成 exact attention，也未证明 paged runtime 的端到端吞吐。Ch45 应补入 eviction bias 与 correction state，解释质量、采样成本和物理页回收之间的边界。

### [Layered LLM Defenses as an Ensemble](https://arxiv.org/html/2608.28327v1)

多层 defense 只有在失败近似独立时才会让 residual risk 相乘；论文在一套七层 stack 中测得 15 对均为正相关，且共同难度解释大部分相关性，stack 的 false refusal 还会累积。单一 adaptive adversary 和一套 stack 不能推出所有产品的相关系数，却足以否定“层数越多就自动乘法增强”。Ch72 应要求以联合攻击集实测 failure correlation、coverage、cost 与 refusal，而不是合并各组件独立分数。

### [EvoUndo](https://arxiv.org/html/2608.28363v1)

Agent 自修改 prompt/tool/middleware 后，当前 state 上成功的 inverse 未必能在另一 counterfactual state 恢复。EvoUndo 将失败拆成 recovery-language expressivity 与 exact state-address grounding，并由独立 verifier 检查 witness；600 项任务的干预显示两者都可能是瓶颈，但部分交互效应随 backbone 改变。Ch84 应补入 mutation admission、witnessed inverse、counterfactual recovery test 与不可表达时拒绝 self-evolution 的 contract。

### [When Linguistic and Internal Confidence Diverge](https://arxiv.org/html/2608.28382v1)

论文把 verbal/internal association、数值接近与相对 correctness 的 calibration 分开；30 个开源模型、10 个任务显示 instruction tuning 与 prompt 可抬高自报分数，却不保证 instance-level 对齐或校准。logit/semantic entropy 也不是真值，实验主要是 classification 和两个 generation tasks。Ch66 已明确 verbal confidence 只是未校准 sensor，必须与外部 evidence 和 held-out calibration 分离，故不再追加。

### [Fidelity Is Not Enough](https://arxiv.org/html/2608.28439v1)

受测 extraction stack 有一次在未打开 datasheet 时仍给出正确值；最终 fidelity 因而无法证明真实使用了来源。dispatch trace 能暴露 tool omission，规则在 207 次 clean run 无误报并按构造捕获 50 个 planted faults，但对“调用工具后仍错误”的检测力未测，物理 oracle 也只覆盖 37 个 claims 中 2 个。Ch69 已要求 trace 证明控制流和工具调用，Ch66 负责 result correctness，两者不能互相替代。

### [ContextPilot](https://arxiv.org/html/2608.28476v1)

ContextPilot 把 search/delete/summarize 扩到 planning、long-term memory 与 soft offload，并用 context/entropy variation 选择 branch sampling，再对经过同一 editing action 的分支估计局部 advantage。长 Context QA 与 deep-search 结果只支持所测模型和工具集，entropy 不是未来价值真值，错误压缩仍会不可逆丢证据。Ch75 已拥有 working-set proposal、source snapshot、runtime commit 与 fallback，Ch33 已拥有 branch-relative credit，故判已有覆盖。

### [Offline-Verifiable Accountability for Cross-Organization Agent Messaging](https://arxiv.org/html/2608.28542v1)

论文把 sender authentication、log commitment、witness checkpoint、append-only continuity、delegation evidence 与可选 receiver receipt 打包，让离线 verifier 只接受 policy 要求的证据。原型的 300 个 workflow 与 corrupted-bundle tests 证明实现域内的拒绝行为，不证明真实 delivery、receipt、组织身份或跨平台 consensus。Ch82/72 已将消息内容、授权、receipt 与不可变 evidence 分层，故不重复增加正文。

### [Logos: An Agent Harness on a Cross-Process Bus](https://arxiv.org/html/2608.28553v1)

Logos 将 capability 变成独立进程，router 只持 routing table，append-only transcript 承载 session truth；在 tool-call 四个故障边界重启后从已提交位置恢复，避免重复 effect。80 次 session 与有限并发 stress 不能证明网络分区、持久存储故障或不可逆外部副作用的 exactly-once，理论还依赖组件独立和 faithful carrier。Ch81/84 已拥有 transcript replay、effect ledger、idempotency、process isolation 与 recovery boundary，因此判已有覆盖。

## 5. 缺口与下一步

无

## 6. 复核

复核者：fresh-context independent reviewer（非报告作者）
结论：通过

复核重读 457 条全标题与全部 high-signal/含糊题摘，确认原有 16 项无误收、exact-v1 均可访问且未见 withdrawn；将 21 个此前过早关闭的家族恢复为候选。原有 6 项 Books 写回的机制命题、证据边界和 Stable Node owner 与正文一致，其中 2608.27460 的 Design Delta 从 3 校正为 2。新增 12 项长期增量也已逐项写入对应 owner；复核确认 source-family marker 唯一，正文位置处于所属机制链与小结之前，且保留了 workload、证据范围、代价、失败边界或回退条件。37 项均已有最终 disposition，报告、Evidence、Books Decision 与写后正文闭环。
