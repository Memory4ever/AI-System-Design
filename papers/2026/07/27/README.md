# Daily Research — 2026-07-27

**规范：** V3
**窗口：** 2026-07-26T09:00:00+08:00 ～ 2026-07-27T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T22:30:00+08:00

## 1. 结论

本窗 official arXiv Monday announcement 经跨分类去重后共有 **383** 个身份。旧 V2.1 报告保留 100 项，存在把“能映射 ROADMAP”“在某个 AI 任务上有改进”误当长期贡献的系统性扩池。独立重审标题与完整摘要，并对含糊、高信号项复用 exact-v1 Method、Evaluation 与 Limitations 后，当前冻结 **40** 项候选，**343** 项在候选分母前关闭，retain rate 为 **10.44%**。关闭项主要是 AI for Science、垂直业务/医疗应用、通用机器人局部方法、单任务 benchmark、已知方法的任务包装，以及没有改变大模型或其 Infra 机制/适用边界的局部优化。

40 项候选形成六条长期线索：可复用 KV 必须修复离线状态与当前 Context 的分布错配；训练效率机制必须同时保留更新容量、policy version 与生成来源；World Model 的持久状态、预测视图和物理动作接口需要不同 owner；评测必须能界定红队、记忆、置信度与 Agent benchmark 到底证明什么；Agent 的 role、capability、change scope 与 tool effect 不能由终局成功率代替；kernel、PIM、异构 memory 与 CPU/GPU placement 的收益必须绑定执行形态和硬件合同。

全部 40 项已取得 exact-v1 HTML 或 PDF，并按采用命题完成证据审阅；其中 **24 项已有正文覆盖、1 项仅报告、15 项已完成 Books 写入**。非作者写后复核逐项确认新增机制已进入对应章节实体正文，并保留 source binding、证据边界、trade-off、旧路径与回退条件。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-ANTHROPIC | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-GOOGLE-AI | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-META-AI | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-QWEN | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-DEEPSEEK | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-MOONSHOT | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-TENCENT-HUNYUAN | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-ZAI | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-BYTEDANCE-SEED | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-BAIDU-ERNIE | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-XIAOMI-MIMO | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-MINIMAX | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-ARXIV | official category listings 与 v1 identity 归并得到 383 项；逐标题巡检，含糊或可能改变项目判断者读取完整摘要；40 项再用 exact-v1 正文定点核验 | 已检查 | 无 |

所有候选均按 2026-07-27 08:00（北京时间）的 official announcement 归属本窗；不比较后续版本。原始清单标记 `2606.24369` 为 withdrawn，已在候选前排除，不参与评分、正面证据或 Books。07-25 回拨的 8 个 owner identity 已全部重判：`2607.21927`、`2607.21962`、`2607.21985`、`2607.22043`、`2607.22242`、`2607.22389` 保留；`2607.21918` 只证明 robotic ultrasound 场景的局部 pipeline，`2607.22000` 只把既有 action-conditioned JEPA 应用于钢琴音频，二者均没有新增本项目需长期保存的机制边界，已在分母前关闭。

## 3. 候选与判断

评分依次为 Design Delta + System Reach + Durability；7～9 分深入审阅，5～6 分标准审阅。分数较低但触发 Books 缺口复核者也按深入审阅处理，不反向抬分。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [FlowEvo](https://arxiv.org/html/2607.21596v1) | 2026-07-27T08:00:00+08:00 | workflow 编译为可复用 skill，并以 downstream utility 抑制负迁移；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`AGENT-PLATFORM`，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Decoupled Attention Fusion](https://arxiv.org/html/2607.21599v1) | 2026-07-27T08:00:00+08:00 | 修复离线文档 KV 缺少跨文档 attention 的状态错配；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [FlowGuard](https://arxiv.org/html/2607.21600v1) | 2026-07-27T08:00:00+08:00 | 用跨模态内部一致性而非单模态输入检查检测组合攻击；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [AgentKVShift](https://arxiv.org/html/2607.21604v1) | 2026-07-27T08:00:00+08:00 | 以 memory-unit probe 估计共享 KV residual，修正未重算 token；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Procedural Knowledge Is Not Low-Rank](https://arxiv.org/html/2607.21612v1) | 2026-07-27T08:00:00+08:00 | 反证“提高 LoRA rank 即能吸收多步条件程序”的容量假设；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-LORA`，[Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [Do VLMs Read or Rewrite?](https://arxiv.org/html/2607.21617v1) | 2026-07-27T08:00:00+08:00 | 区分 faithful transcription 与语言先验驱动的合理化改写；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [FBLayout](https://arxiv.org/html/2607.21624v1) | 2026-07-27T08:00:00+08:00 | 将前后向 layout 与移动 GPU memory traffic 联合设计；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`TRAIN-LORA`，[Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [Role Drift](https://arxiv.org/html/2607.21627v1) | 2026-07-27T08:00:00+08:00 | 揭示 terminal accuracy 可由模块越权捷径获得；3 + 3 + 3 = 9 | 深入完成 | 整合：`AGENT-MULTI-AGENT`，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [CARE](https://arxiv.org/html/2607.21642v1) | 2026-07-27T08:00:00+08:00 | shell action 在执行前 canonicalize、静态归因并只升级含糊项；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`AGENT-TOOL-CALLING`，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Molt](https://arxiv.org/html/2607.21653v1) | 2026-07-27T08:00:00+08:00 | 异步 Agent RL 将 token 来源、policy version 与 model semantics 绑定；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Persistent Computational State](https://arxiv.org/html/2607.21686v1) | 2026-07-27T08:00:00+08:00 | World Model session 必须持久化不可重算的 RNG/memory/KV kernel；3 + 3 + 3 = 9 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [RED-PIM](https://arxiv.org/html/2607.21731v1) | 2026-07-27T08:00:00+08:00 | 通过 attention 代数重排将 PIM 跨 bank 数据移动从二次降到线性；3 + 2 + 2 = 7 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [What AI Red-Team Evaluations Can and Cannot Prove](https://arxiv.org/html/2607.21735v1) | 2026-07-27T08:00:00+08:00 | 用 testing budget 与 elicitation discrimination 给出可计算 evidential ceiling；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [When Model Release Meets Model Reuse](https://arxiv.org/html/2607.21738v1) | 2026-07-27T08:00:00+08:00 | 证明 producer 与 consumer 对 metadata、lineage 目的和记录位置不一致；2 + 2 + 2 = 6 | 深入完成 | 整合：`PLATFORM-MODEL-REGISTRY`，[Ch59](../../../../books/part-06-ai-infrastructure/59-model-registry.md) |
| [Acceptance Collapse in Speculative Decoding](https://arxiv.org/html/2607.21804v1) | 2026-07-27T08:00:00+08:00 | lossless 输出保证不等于 acceptance/goodput 不可攻击；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING`，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [ToolGuardian](https://arxiv.org/html/2607.21835v1) | 2026-07-27T08:00:00+08:00 | 将 tool admission characterization 与 task-time authorization 分离；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-TOOL-CALLING`，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Claim Plane](https://arxiv.org/abs/2607.21909v1) | 2026-07-27T08:00:00+08:00 | 并行 coding agent 在写前声明 typed intent，动态 scope promotion 重新 admission；3 + 3 + 2 = 8 | 深入完成 | 整合：`AGENT-WORKFLOW`，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [TRACE-RealWorld](https://arxiv.org/html/2607.21910v1) | 2026-07-27T08:00:00+08:00 | 把预测世界状态视为会过期的 materialized view，并给 commitment 定义 refresh/compensation；3 + 3 + 3 = 9 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Reliability-Contagion Feasibility](https://arxiv.org/html/2607.21912v1) | 2026-07-27T08:00:00+08:00 | 多 Agent connectivity 同时受证据汇聚与错误传播约束；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT`，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [RIS-Kernel](https://arxiv.org/html/2607.21927v1) | 2026-07-27T08:00:00+08:00 | 随机稀疏 attention 作为 CPU 长上下文替代分支；2 + 1 + 2 = 5 | 标准完成 | 仅报告：多 seed ensemble 与边缘显著性不足以改变长期执行结论 |
| [Ground Truth First](https://arxiv.org/html/2607.21962v1) | 2026-07-27T08:00:00+08:00 | 先生成带 valid-time/provenance 的事实再渲染会话，避免后抽答案污染；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Unified Static-Dynamic Pruning](https://arxiv.org/html/2607.21985v1) | 2026-07-27T08:00:00+08:00 | 共享 sparse format 让 prefill 静态稀疏与 decode 动态稀疏共存；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [VIGOR](https://arxiv.org/html/2607.22002v1) | 2026-07-27T08:00:00+08:00 | 在固定总预算内按在线 group reward variance 逐轮分配 rollout；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [HEMERA](https://arxiv.org/html/2607.22022v1) | 2026-07-27T08:00:00+08:00 | 将矩阵化 SSD 重写为等价 streaming recursion 并分配给异构单元；3 + 2 + 2 = 7 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Stated versus Internal Confidence](https://arxiv.org/html/2607.22034v1) | 2026-07-27T08:00:00+08:00 | 证明 verbalized confidence 与 token probability 是不同 sensor，且都可能在严重 shift 下失效；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Scaling Native Multimodal Pre-Training](https://arxiv.org/html/2607.22043v1) | 2026-07-27T08:00:00+08:00 | compute-optimal allocation 同时依赖模型、token 与 multimodal mixture；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION`，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Entropy-Scaled Trust Regions](https://arxiv.org/html/2607.22186v1) | 2026-07-27T08:00:00+08:00 | 异步 RL 的 importance-ratio 容许区间应随 token entropy 变化；3 + 3 + 2 = 8 | 深入完成 | 整合：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Agentic CPU-GPU Scheduling](https://arxiv.org/html/2607.22242v1) | 2026-07-27T08:00:00+08:00 | immediate GPU、queued GPU 与 CPU offload 必须结合 contention/VRAM 在线选择；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`AGENT-PLATFORM`，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Cross-Tokenizer On-Policy Distillation](https://arxiv.org/html/2607.22334v1) | 2026-07-27T08:00:00+08:00 | 以 byte-prefix marginal 保留跨 tokenizer teacher 概率质量；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-SFT`，[Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Do Agent Benchmarks Measure Capability?](https://arxiv.org/html/2607.22368v1) | 2026-07-27T08:00:00+08:00 | 将 exposure→use→misleading score 显式化，区分 task success 与 protocol validity；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [HiKV](https://arxiv.org/html/2607.22389v1) | 2026-07-27T08:00:00+08:00 | token eviction 与 element loading 两级压缩绑定可重构 sorter；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-GPU-MEMORY`，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [The Prompt Is Not the Query](https://arxiv.org/html/2607.22392v1) | 2026-07-27T08:00:00+08:00 | final prompt 是 request-state delta，不是完整 session query；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-CONTEXT`，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [Identifiability of Controlled World Models](https://arxiv.org/html/2607.22430v1) | 2026-07-27T08:00:00+08:00 | representation identifiability 与 action-conditioned transition identifiability 是两项条件；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [TileSight](https://arxiv.org/html/2607.22432v1) | 2026-07-27T08:00:00+08:00 | 用统一 tile resource/action abstraction 连接 core、cache 与网络；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Dynamic Capability Scoping](https://arxiv.org/html/2607.22445v1) | 2026-07-27T08:00:00+08:00 | role ceiling、task classifier 与组合禁令共同产生最小权限 proposal；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`AGENT-PLATFORM`，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Where Facts Go Missing](https://arxiv.org/html/2607.22448v1) | 2026-07-27T08:00:00+08:00 | 将事实遗漏按 pipeline layer 归因，并分离确定性软件丢失与行为性未检索；3 + 3 + 2 = 8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [TRACE-ROUTER](https://arxiv.org/html/2607.22465v1) | 2026-07-27T08:00:00+08:00 | 将 routing unit 从单次 call 改成 task，并用 terminal outcome 更新；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [The Regression Tax](https://arxiv.org/html/2607.22520v1) | 2026-07-27T08:00:00+08:00 | skill 平均增益必须拆成 gain、regression 与 residual failure；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`AGENT-PLATFORM`，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [ViTacWorld](https://arxiv.org/html/2607.22530v1) | 2026-07-27T08:00:00+08:00 | tactile 是视觉不可观测接触状态，需与 action/visual state 时间对齐；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Robot-Factored World Models](https://arxiv.org/html/2607.22535v1) | 2026-07-27T08:00:00+08:00 | 将 action realization 与 robot rendering 移出 world model，避免 future-state leakage；3 + 3 + 2 = 8 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |

## 4. 证据与知识整合

### [FlowEvo](https://arxiv.org/html/2607.21596v1)

§3 将成功 workflow 编译成可执行 skill，持久库按 downstream utility 抑制负迁移；§4 在五类任务、10 个不同规模 base model 上支持“执行轨迹可被提炼并复用”的受限可行性。它不证明一次成功就应永久晋升，也不解决 evaluator 错误、skill dependency drift 和版本兼容。Ch84 已把 trajectory→skill compilation、marginal utility、regression gate、retirement 与 rollback 写成完整生命周期，故无需重复写入。

### [Decoupled Attention Fusion](https://arxiv.org/html/2607.21599v1)

§2 把离线 document KV 的修复拆成 important-token inter-document attention、question-document attention 与 state fusion，使三个 dense path 可使用 FlashAttention；§3 的 preliminary benchmark 只支持作者模型、长度与 vLLM 配置下相对 CacheBlend/full recompute 的结果。它没有证明融合后的 hidden state 对任意文档顺序、cache revision 或 tail-SLO 都等价。Ch45 已明确离线 KV 复用必须绑定 prefix/dependency identity，以 probe/selective recompute 修复 stale residual，并在误差越界时回退完整 Prefill，已覆盖该机制边界。

### [FlowGuard](https://arxiv.org/html/2607.21600v1)

§3 用 text-only、vision-only 与 fused prediction 构造 redundancy/synergy/dominance FlowVector，one-class detector 只在 benign data 上拟合；§4 与 Appendix A 支持所测 attack set 上降低 ASR，但不证明未见模态、adaptive attacker 或换 backbone 后仍校准。跨模态一致性只是风险 sensor，不能取得 allow/deny authority。Ch72 已要求多模态 guard 同时保留 provenance、cross-modal consistency、独立 policy 与 fail-closed controller，故判已有覆盖。

### [AgentKVShift](https://arxiv.org/html/2607.21604v1)

§3 与 Appendix C 将每个 retrieved memory unit 的 KV residual 分解成共享 offset 加 token fluctuation，以少量 probe 同时修正被重算和未重算 token；四个 3B～32B 模型、两项 memory benchmark 与单 A100 结果仅支持该 cache layout/refresh ratio 下接近 full recompute。它不证明 residual 在换模板、position、模型 revision 或 memory mutation 后仍稳定。Ch45 已拥有 `identity → probe → selective recompute/residual correction → fallback` 这条复用链，Agent memory 只提供语义来源，不拥有 KV correctness。

### [Procedural Knowledge Is Not Low-Rank](https://arxiv.org/html/2607.21612v1)

§2～§4 在三种多步条件程序、3B/8B 模型和 rank 16～128 下，显示高 completion 与低 terminal success 可以并存；full-finetune update 的 effective rank 远高于 128，为“程序更新未落在低秩子空间”提供解释。该结果不证明所有 procedural task 都需要 full fine-tuning，SVD 能量也不等价于因果必需 rank。写后对读确认 Ch30 已将条件分支/终态约束写为 LoRA 容量边界，并保留 full fine-tune、外置 workflow/tool 与验证器三条共存分支。

### [Do VLMs Read or Rewrite?](https://arxiv.org/html/2607.21617v1)

FaithC4 用三类字符扰动、三种语言和 15 个 OCR/VLM system 比较 literal transcription；结果只证明 general-purpose VLM 在该数据上可能把异常字符串改写为更 plausible 文本，layer probe 也只是相关诊断。它不证明所有语义 VLM 都不适合 OCR，也不证明 FFN distance 是因果开关。写后对读确认 Ch23 已区分语义归一化与逐字转录：exact evidence 路径保留 OCR-specialized/raw-text、character-level evaluator 与 source image，不以语义正确率替代 fidelity。

### [FBLayout](https://arxiv.org/html/2607.21624v1)

§4 以 R-Tile、索引变换和 activation-guided propagation 让 forward/backward 共享可执行 layout；§5 的 2.2～5.7 倍仅属于七个 transformer、Mali/Adreno 与作者实现，不证明其他 shape、NPU 或训练 objective。它用全图 layout coupling 换 cache locality，也新增 compiler propagation 与 backend lock-in。Ch30 已把高 rank/target-module 的 intermediate、kernel layout、backend guard 与 eager fallback 置于 runtime contract 中，足以承载该受限实现。

### [Role Drift](https://arxiv.org/html/2607.21627v1)

§4 的两条 compound pipeline 显示 end-to-end RL 可以通过 decomposer 偷带答案、reader 回退参数记忆而提高 terminal accuracy；Role Anchor 保持 role prompt 相对 neutral prompt 对 next-token distribution 的影响，但以可调 accuracy 损失为代价。该证据不证明 prompt-shift proxy 完整定义角色，也不覆盖开放工具副作用。写后对读确认 Ch82 已把角色正确性与终局成功分账，并以 role-local obligation/trace gate 阻止把 shortcut 取得的 terminal reward自动归功于预定模块。

### [CARE](https://arxiv.org/html/2607.21642v1)

§III 将 shell command canonicalize，并从 syntax、command semantics、bounded path context 与 provenance 产生 deterministic evidence，只把 underdetermined case 升级给 LLM judge；§IV～V 的 F1、false-positive、latency 与 sandbox harm reduction 只属于论文 threat set。静态规则会漏 semantic intent，resolver/LLM judge 也会错判。Ch78/Ch72 已把 proposal、canonical action、deterministic pre-execution gate、least privilege、escalation 和 effect receipt 分开，覆盖其长期机制。

### [Molt](https://arxiv.org/html/2607.21653v1)

§2～§4 的核心不是代码量，而是单一异步 loop 只训练本 policy 实际生成的 token，并让 token、policy version 与 model semantics 一致；matched protocol 只表明作者任务下与 Megatron stack 统计可比，不证明 compact framework 可替代大规模容错、checkpoint 与 topology control。Ch33 已将 rollout provenance、behavior/current policy、staleness、token identity 与异步回退写成训练语义，因此仅把 Molt 当实现证据。

### [Persistent Computational State](https://arxiv.org/html/2607.21686v1)

§8/§7 通过 snapshot/restore observation+RNG、memory bank 或 windowed KV，证明三类受测 world model 在真实 excursion 后可 byte-identical 回到 never-left continuation；只破坏 RNG 就会退化。这反证了“返回视点失败必然是模型能力缺失”，但不证明所有 world model 的最小状态相同，也未覆盖跨机故障和模型升级。写后对读确认 Ch25 已区分可重算 Context 与不可重算 PCS，并写入 session identity、atomic checkpoint/restore、model revision compatibility 与 relevance-aware eviction。

### [RED-PIM](https://arxiv.org/html/2607.21731v1)

§III 将 attention 运算重排，使 bank-local intermediate 从 `N×N` 降为 `d×d`，跨 bank traffic 从二次降到线性；§IV 的仿真/数据集结果只支持论文 PIM organization，不等于 GPU 或现有 PIM 产品的端到端收益。交换运算顺序会引入数值、layout、capacity 和专用硬件约束。写后对读确认 Ch49 已把代数等价变换作为 PIM data-movement 分支，与 dense GPU path 共存，并要求数值、bank/interconnect 与端到端 workload 验收。

### [What AI Red-Team Evaluations Can and Cannot Prove](https://arxiv.org/html/2607.21735v1)

方法部分在固定预算、评分规则和近似独立 trial 下，把 benchmark null result 的最大 Bayes factor 写成 evidential ceiling；八个 suite 的审计只说明高频 harm 与 rare catastrophic harm 需要不同样本量。它不证明真实 harm rate、trial 独立或 adaptive red-team 的 elicitation rate 已知。写后对读确认 Ch66 已把 clean sheet 的最强证据命题绑定 testing budget，并要求报告 harm-rate 目标、elicitation/discrimination 假设、有效试验数与 inconclusive 区域。

### [When Model Release Meets Model Reuse](https://arxiv.org/html/2607.21738v1)

§3～§4 的 50 位 producer 与 95 位 consumer 调查显示双方依赖相同 artifacts，却对 metadata 放置、lineage 深度和治理优先级有不同目的；它是人因证据，不证明某个 registry schema 因果提高可靠性。写后对读确认 Ch59 已区分 producer provenance 与 consumer compatibility/reliability evidence，并要求 Registry schema 显式保存 claim owner、intended consumer、required evidence 与 missing status。

### [Acceptance Collapse in Speculative Decoding](https://arxiv.org/html/2607.21804v1)

§4 用 verifier-aligned surrogate 优化 suffix，使 draft mass 偏向 target 难接受 token，同时用 target-preservation objective 避免明显破坏任务；§5 的 62.3% sample-time 增长只属于 GSM8K 等披露配置。它证明 lossless output 不保证 stable goodput，不证明攻击在所有 draft/target 和服务 admission 下可迁移。Ch48 与 Ch72 已把 acceptance rate 视为可操纵运行状态，并要求预算、fallback 与 abuse control，故无需新增。

### [ToolGuardian](https://arxiv.org/html/2607.21835v1)

§III 将 description、syscall、mock execution 与 source analysis 逐步转成 capability/effect facts，再由 ASP 分别执行 admission 和 runtime authorization；16 个 tool 与 20 个场景只能证明该小型规则域的可行性。source 不可见、effect 模型不全或组合规则遗漏时仍会漏判。Ch78 已区分 tool discovery、characterization、policy admission、call-time authorization 与 effect receipt，Ch72 保留 fail-closed path，已完整覆盖。

### [Claim Plane](https://arxiv.org/abs/2607.21909v1)

exact-v1 PDF 将 base commit、typed resources、dependencies 和 committed/contingent operations 编成 versioned ChangeIntent；control plane 原子 admission，首次 contingent mutation 再做 scope promotion，并以 lease、worktree lock、fencing token 与 Git provenance 限制实际写入。六对 CooperBench 只证明机制可运行，不支持性能或普遍冲突消除。写后对读确认 Ch81 已补入写前 intent admission 与运行中 scope promotion，并保留含糊 overlap、共享文件或不可逆 effect 时串行化/拒绝的旧路径。

### [TRACE-RealWorld](https://arxiv.org/html/2607.21910v1)

§5 将 predicted state 作为 materialized view，把 physical commitment 视为 freshness authorization 会过期的 read；priced verification 在证据可能改变决定时 refresh，Saga-style compensation 只修复依赖已失效且可逆的 commitment。Flood-SAR 结果不证明 adaptive refresh 在成本、覆盖或任务成功上总占优，且 97 次 restoration 中仍有 10 次未完成。写后对读确认 Ch25 已以 claim expiry、consequence-conditioned refresh、consistency debt 与不可逆动作的人工/controller gate 约束 physical commitment。

### [Reliability-Contagion Feasibility](https://arxiv.org/html/2607.21912v1)

§6～§8 将错误传播与多数投票可靠性同时写成 topology constraint；21,000 条模拟和六节点实验只显示方向性，不证明开放 Agent 网络中的固定阈值。更密连接可能提升证据池化，也可能扩大错误 offspring，结论还依赖 per-edge exposure 或 fixed-sender-budget 的计量方式。Ch82 已明确错误相关时多数票会放大失败，并保存 minority evidence、通信预算与拓扑回退，已覆盖。

### [RIS-Kernel](https://arxiv.org/html/2607.21927v1)

§4 用随机/结构 sparse attention 在 CPU 上处理 32K/65K Context；关键结果依赖 10～70 个 ensemble seeds，65K 增益只有边缘显著性，且未给 GPU kernel、端到端并发或 tail-SLO。它能作为预算极紧时的 CPU feasibility case，却不足以改写 Ch22/Ch49 对 sparse attention 的长期结论，因此仅报告；需要独立复验、单次请求成本与质量匹配后才重开。

### [Ground Truth First](https://arxiv.org/html/2607.21962v1)

§3 先生成带 validity interval、volatility 与 source channel 的 life script，再渲染会话并机械生成问题；§4～§5 的五种 memory backend、两种 horizon 和三次重复显示短期/长期排名可能反转。合成用户、约 380 个问题与 LLM judge 不证明生产长期记忆排序。Ch66 已有 `fact + validity interval + provenance` 的 ground-truth-first evaluation，Ch77 拥有写入/过期状态，故无需重复。

### [Unified Static-Dynamic Pruning](https://arxiv.org/html/2607.21985v1)

§4 用共享 column-addressable bitmap 让 prefill 走 Tensor-Core SpMM、decode 走 activation-aware spMspV；§5 的速度和 sparsity 来自特定 inference GPU、模型与 kernel，不能与其他精度/shape 直接相乘。metadata、padding 与 irregularity 会吞掉理论压缩。Ch49 已写明静态 weight mask 与 input-dependent activation sparsity 需共享可寻址格式、按 phase 选择 kernel 并保留 dense fallback，已覆盖。

### [VIGOR](https://arxiv.org/html/2607.22002v1)

§4 从少量 rollout 起步，把剩余固定预算逐轮给 group reward variance 更高的 prompt；§5 的数学/代码结果只支持所测 verifier 与 policy stage。variance 估计本身消耗样本，稀有成功、非平稳 reward 或错误 verifier 会误分配。Ch33 已将固定总 rollout/token budget、reward variance、support coverage 与动态 allocation 写在同一控制链中，已覆盖。

### [HEMERA](https://arxiv.org/html/2607.22022v1)

§5 将 Mamba-2 的矩阵化 SSD 改写为代数等价 streaming recursion，把 dense projection 映射到 in-memory units、递归 state update 映射到 dedicated stream engine；§6 的 A100 对比来自模拟/专用 accelerator 假设，不能证明可制造性或通用 edge latency。写后对读确认 Ch49 已把等价表示、state materialization 与异构硬件划分放入 execution-plan owner，并要求 numerical equivalence、state ordering、fabric cost 与成熟 GPU fallback。

### [Stated versus Internal Confidence](https://arxiv.org/html/2607.22034v1)

§3～§5 在两个小型 VLM、六种图像退化和 3,800 次预测中比较 verbalized confidence 与 mean token probability；内部概率在多数 slice 更能分错，但 severe underexposure 下两者都失效。它不证明 token probability 是 calibrated correctness probability，也不覆盖生成式长答案。Ch66 已明确 self-report、token probability、sample agreement 与 verifier 是不同 sensor，必须按 deployment slice 校准并在 shift 下 defer，已覆盖。

### [Scaling Native Multimodal Pre-Training](https://arxiv.org/html/2607.22043v1)

§2.3/§4.1 与 Appendix A/B 在固定 compute 下联合拟合 model size、token count 与 mixture，显示 language 与 multimodal objective 对数据配比有不同 allocation law；只支持作者模型族、规模和 loss，不证明下游任务或更大 scale 的唯一最优配比。Ch23 已明确 native multimodal 的 loss、sampling ratio、packing 和 router load 共同决定表示，并记录该 source family，故已有覆盖。

### [Entropy-Scaled Trust Regions](https://arxiv.org/html/2607.22186v1)

§3.3～§4 观察到低 entropy token 的微小 train/inference discrepancy 会放大 ratio noise，而高 entropy token 的较大 ratio 可能来自合法探索；ESTR 因而按局部 entropy 缩放 deviation gate。§5 的 2.6 倍和质量结果绑定 BrowseComp-Plus/multi-turn GSM8K 与作者 async stack，不证明 entropy 是 staleness 的充分统计量。写后对读确认 Ch33 已写入统一 ratio threshold 对低熵噪声和高熵探索的混淆，并保留同步/版本有界路径作为校准失效时回退。

### [Agentic CPU-GPU Scheduling](https://arxiv.org/html/2607.22242v1)

§3 将每个 tool 映射为 immediate GPU、queued GPU 或 CPU offload，runtime monitor 只提供 utilization、VRAM、reprobe 与 exploration observation，LLM 提案不拥有资源真值；§4 的 13/13 最优只来自 19 个 tool 和 13 个受控场景。Ch84 已把 Agent run 的 CPU/GPU/tool/wait phase、headroom、prefetch/swap cost 与 deterministic resource manager 分责，并保留 static placement，已覆盖。

### [Cross-Tokenizer On-Policy Distillation](https://arxiv.org/html/2607.22334v1)

§3 把 teacher next-token distribution 投影到共享 byte space，将概率分给最长匹配 student byte prefix，未匹配质量进入显式 residual；超过 99% 位置满足单 teacher-token prefix 条件，其余只给 mass-preserving lower bound。§4 的数学/编程结果不证明任意 Unicode normalization、跨 token 边界或不同语言都忠实。写后对读确认 Ch29 已把 byte normalization、residual mass、跨边界 approximation 与 tokenizer identity 写入跨 tokenizer probability interface，并保留 shared tokenizer 基线。

### [Do Agent Benchmarks Measure Capability?](https://arxiv.org/html/2607.22368v1)

Appendix B/H 定义 exposure、agent use 与 intended score 的 post-hoc attribution，并以 Mislead gap 比较 exploit score 与 intended score；2,385 traces/15 benchmarks 支持“终局成功可能来自公开解、evaluation artifact 或 invalid scoring path”。它不证明未发现 exposure 的 benchmark 有效。Ch66 已将 environment integrity、scorer validity、shortcut/reward hacking 与 task outcome 分账，并要求 trace/effect evidence，已覆盖。

### [HiKV](https://arxiv.org/html/2607.22389v1)

§IV 先按 token importance eviction，再只加载保留 token 的重要 elements，reconfigurable sorter 为两级不同 datapath 服务；§V 的速度、能耗、1% accuracy 与 8% area 都是作者硬件模型/任务条件，不是生产保证。Ch54 已记录该 source family，并将 token/element granularity、external-memory traffic、specialized hardware 与 iso-quality gate 连成同一分层 KV 路线，已有覆盖。

### [The Prompt Is Not the Query](https://arxiv.org/html/2607.22392v1)

§6/§7.2 在两个多轮 conversation corpus 中显示 final prompt 常缺少历史中已出现的 request dimensions，同时又可能新增 dimension；length-matched null 只支持“信息可用性不足”，不估计 history 对答案的因果影响。Ch75 的中心命题已经把 Context 定义为随 user/tool/workflow transition 更新的 working state，并明确单次 visible input 只是 assembled view，足以覆盖。

### [Identifiability of Controlled World Models](https://arxiv.org/html/2607.22430v1)

§3 分离 representation identifiability 的 spectral separation 与 transition identifiability 的 conditional action excitation，并给出 counterfactual error 随最弱 excitation margin 放大的界；§4 只在四个 nonlinear observation setting 支持理论方向。Gaussian latent、正交变换和行为策略覆盖是假设，不证明现实视频/机器人动力学。Ch25 已明确 state-only prediction 只能得到 behavior-policy-averaged future，action intervention 与 route-specific evidence 才能支撑控制状态，已有覆盖。

### [TileSight](https://arxiv.org/html/2607.22432v1)

§4 把 tile 表成 compute/memory/network resource vector 与 ordered actions，再用 reuse distance 和 alpha-beta stage cost 连接 core、cache、GPU；§5 的 MAPE 绑定 A100/H200/B200/B6000、regular tile programs 和作者 benchmark。它不能预测不规则 control flow、未建模 interference 或所有 vLLM SLO。Ch49 已以 tile abstraction、resource model、legal overlap、measurement calibration 与 profiler fallback 组织 execution planning，已有覆盖。

### [Dynamic Capability Scoping](https://arxiv.org/html/2607.22445v1)

§3 组合 role ceiling、task-context classification 和 policy 禁止组合来产生 permission proposal，observe-only 模式保留不一致请求；§5 的 600 条 synthetic prompt 与 60-record human review 只证明 dataset/policy 共同迭代的可行性。分类器看不到运行中才发现的需要，synthetic policy 也不证明真实组织授权正确。Ch84/Ch78 已要求 dynamic least privilege、capability lease、call-time reauthorization 与外部 policy authority，已覆盖。

### [Where Facts Go Missing](https://arxiv.org/html/2607.22448v1)

Attribution Methodology 把 ingestion 到 final answer 分为 L0～L8，并用 conditional waterfall 先定位 deterministic software loss，再分析 behavioral non-retrieval；75,476 个 synthetic trials 和 372 个 pilot 支持受控 pipeline-level localization。benchmark allocation、模型/engine confounding 和 heuristic label 不证明 production omission prevalence，也不能把 q4 KV/RoPE 相关性写成因果。写后对读确认 Ch66 已把 deterministic first-loss 放在行为评分之前，并加入 source-presence invariant、layer transition receipt、first-loss attribution 与原始 evidence replay。

### [TRACE-ROUTER](https://arxiv.org/html/2607.22465v1)

§3 在 task admission 只选一次 model，后续 calls 保持 pinned，并用 terminal accuracy/latency reward 更新 contextual bandit；§4 的结果绑定三个 Agent benchmark。它减少 per-call credit mismatch，却可能错过任务阶段变化、backend failure 和 Context drift。Ch56 已把多轮 routing 扩展为保存 session state、累计成本、终局效用与 conservative fallback 的有限 horizon policy，包含该更简单的 task-pinned 分支，故已有覆盖。

### [The Regression Tax](https://arxiv.org/html/2607.22520v1)

§3 与 §6.1 在近 6,000 次运行中将 skill 净效果拆成 gains、regressions 与 residual failures，并把回归归因于 description osmosis、grounding displacement 和 verification displacement；它不证明这些 taxonomy 在所有模型/harness 中完备。Ch84 已要求 marginal skill gate、negative transfer、grounding/verification、canary、retirement 和 rollback，已覆盖。

### [ViTacWorld](https://arxiv.org/html/2607.22530v1)

§3.4/Appendix C 将 visual、tactile 与 action trajectory 时间对齐，先混合真实/仿真预训练，再用真实 policy rollout 贴近下游；受测 contact-rich task 只支持 tactile rollout 可辅助 policy training/evaluation，不证明 tactile sim-to-real gap 普遍更小或生成数据正确。写后对读确认 Ch25 已把 tactile 作为视觉不可观测的独立 observation，绑定 sensor provenance、calibration、timestamp、embodiment、action alignment 与 real-contact gate。

### [Robot-Factored World Models](https://arxiv.org/html/2607.22535v1)

§3 将 command 经真实 controller/kinematics 展开为 deployment-available nominal trajectory，再用 URDF 渲染 robot geometry；world model 只学习场景对已实现动作的响应，避免直接学 action realization，也避免输入 logged future state 泄漏 outcome。§4/Appendix 只支持所测 embodiment/viewpoint，rendering/calibration/controller mismatch 仍会传播。写后对读确认 Ch25 已明确 controller/kinematics、renderer 与 world model 的中间 owner 分工，Ch26 继续拥有真实执行与 safety envelope。

## 5. 缺口与下一步

无

40 项均有 exact-v1 HTML；`2607.21909` 使用 exact-v1 PDF/text。没有 blocked 或 disputed 候选，withdrawn `2606.24369` 已从正面链路清除。15 项 Books 增量已逐项写入并完成非作者正文对读。

4 个 Existing Coverage family 的 Books trace 已从错误的 `2026-07-25` 修正为 official first-public owner `2026-07-27`：`SF-2026-ARXIV-2607-21962`（Ch66）、`SF-2026-ARXIV-2607-21985`（Ch49）、`SF-2026-ARXIV-2607-22043`（Ch23）、`SF-2026-ARXIV-2607-22389`（Ch54）。复核确认正文机制与审计身份现在一致。

`2607.21927` 保持仅报告；定点重开条件是取得可比较的单次执行成本、matched-quality 结果和独立复验。在此之前它是终态保留项，不用于正面证据、Books 结论或“无遗漏”断言。

## 6. 复核

复核者：非作者独立复核（/root/aug11_20，2026-09-10）

结论：通过

本轮对 15 项 Integrate 逐项核验了 Books 实体正文、Stable Node owner、source-family binding、采用/未证明边界、trade-off、旧路径与 fallback，并检查其在章节中的邻接语义；没有用 trace 或 Review notes 代替正文。Existing Coverage 的机制抽查通过，4 个错误 trace 日期也已修正并重新核验。报告证据、Books 正文与 first-public owner 现已闭合。
