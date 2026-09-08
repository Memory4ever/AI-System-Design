# Daily Research — 2026-08-13

**规范：** V3
**窗口：** 2026-08-12T09:00:00+08:00 ～ 2026-08-13T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T22:40:00+08:00

## 1. 结论

本窗 14 个 Daily 来源均已检查。arXiv 官方公告批次跨分类去重后共有 500 个身份；独立复核重新从批次首项逐题阅读标题，对边界项和高信号项继续阅读完整摘要，并在 AI for Science、纯领域应用、局部 benchmark 和仅参数改进进入候选分母前关闭后，冻结 29 个候选。候选率为 5.8%，不是把全部 AI 论文当作项目候选。

29 项均已核对 exact-v1、withdrawn 状态并完成 Source Review，其中 3 项进入本报告的展开式 Deep Analysis。独立复核恢复了作者初筛漏掉的 8 项，并将仅以新场景复述现有原则的多项 Books 提案降级为已有覆盖；最终 9 项长期机制增量已写入对应正文，1 项此前已有本 Source Family 的落盘证据，其余 19 项由现有命题覆盖。写后语义、owner 与相邻衔接复核通过，日报闭合。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 归档按日期检查 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 日期列表出现 8 月 13 日 Multiagent 文章，但页面未暴露可唯一归窗的时刻 | 受阻 | 见 §6 |
| SRC-GOOGLE-AI | DeepMind / Google Research 发布目录按日期检查 | 已检查 | 无 |
| SRC-META-AI | FAIR publication 列表按日期检查 | 已检查 | 无 |
| SRC-QWEN | 官方文章目录按日期检查 | 已检查 | 无 |
| SRC-DEEPSEEK | 官网研究与更新目录按日期检查 | 已检查 | 无 |
| SRC-MOONSHOT | 官方 Blog 与仓库发布入口按日期检查 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Research“全部”目录；ELR 首次公开时间冲突继续隔离 | 受阻 | 见 §6 |
| SRC-ZAI | Research 日期目录按日期检查 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Research、Blog、Publications 按日期检查 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 技术博客与仓库发布入口按日期检查 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | Paper / Blog 与官方仓库按日期检查 | 已检查 | 无 |
| SRC-MINIMAX | Research / Blog 按日期检查 | 已检查 | 无 |
| SRC-ARXIV | 官方新公告 500 个唯一身份；独立全标题语义复核，边界/高信号项读完整摘要，保留 29 项；候选 v1 可访问且未 withdrawn | 已检查 | 无 |

没有触发按需来源。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Detecting a Route Flip](https://arxiv.org/html/2608.11212v1) | 2026-08-13T08:00:00+08:00 | 将 MoE 量化损伤拆成 compute error 与 routing mediator；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Cutting AI Datacenter Energy with Reinforcement Learning](https://arxiv.org/html/2608.11226v1) | 2026-08-13T08:00:00+08:00 | 以实测功率遥测判断训练控制器的 actuator authority；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-COST`，[Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [LinearKV](https://arxiv.org/html/2608.11231v1) | 2026-08-13T08:00:00+08:00 | hybrid LLM 的 position-independent cache 由单 recurrent state 初始化；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [InfraBench](https://arxiv.org/html/2608.11234v1) | 2026-08-13T08:00:00+08:00 | 以 durable state、distributed invariants 与 side effects 评价基础设施 Agent；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [CORA-Diff](https://arxiv.org/html/2608.11235v1) | 2026-08-13T08:00:00+08:00 | 用 confidence 与 persistence gate 只重算未决 diffusion token；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Lost in Compaction](https://arxiv.org/html/2608.11242v1) | 2026-08-13T08:00:00+08:00 | 识别 compaction 静默丢弃 session constraints 的系统风险；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-CONTEXT`，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [Agent Safety Should Be a Runtime Contract](https://arxiv.org/html/2608.11274v1) | 2026-08-13T08:00:00+08:00 | preventive gate 与 action evidence chain 共同约束副作用；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-TOOL-CALLING`，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Lifecycle-Optimal Tokenization](https://arxiv.org/html/2608.11361v1) | 2026-08-13T08:00:00+08:00 | 将 tokenizer 选择从训练压缩率扩为训练与部署总成本；3 + 2 + 3 = 8 | 深入完成 | 整合：`MODEL-TOKENIZER`，[Ch11](../../../../books/part-02-model/11-tokenizer.md) |
| [PAIR](https://arxiv.org/html/2608.11368v1) | 2026-08-13T08:00:00+08:00 | 以成对比较为统计单元重分配 GRPO rollout token；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [ForeWAM](https://arxiv.org/html/2608.11605v1) | 2026-08-13T08:00:00+08:00 | 用 Future-KV 暴露 latent dynamics 而不解码未来视频；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Transactional Continuity Kernel](https://arxiv.org/html/2608.11632v1) | 2026-08-13T08:00:00+08:00 | 以 predecessor、authority、freshness 和 effect uniqueness 原子激活 branch head；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-WORKFLOW`，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [The Sleeping Agent](https://arxiv.org/html/2608.11775v1) | 2026-08-13T08:00:00+08:00 | 证明 gist compression 会选择性丢失 temporal expressions；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：`AGENT-CONTEXT`，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [Total Recall at What Cost?](https://arxiv.org/html/2608.11879v1) | 2026-08-13T08:00:00+08:00 | memory 成本由内部行为而非对话长度单独决定；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-COST`，[Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [Agent Skills Can Be Harmful](https://arxiv.org/html/2608.11888v1) | 2026-08-13T08:00:00+08:00 | paired run 将功能失败和成本回归归因到具体 skill；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-PLATFORM`，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [RealisticTritonBench](https://arxiv.org/html/2608.12004v1) | 2026-08-13T08:00:00+08:00 | 真实 PR kernel 任务回到原框架验 correctness 与性能；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Kernel-Managed Expert Cache](https://arxiv.org/html/2608.12103v1) | 2026-08-13T08:00:00+08:00 | 比较 OS page cache 与 user-space expert residency 并暴露 reclaim 方法偏差；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`INFER-GPU-MEMORY`，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [The Ingestion Tax](https://arxiv.org/html/2608.12114v1) | 2026-08-13T08:00:00+08:00 | 将模型装载从拷贝路径改为 file-backed GPU-readable pages；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-GPU-MEMORY`，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Ready Cohorts](https://arxiv.org/html/2608.12123v1) | 2026-08-13T08:00:00+08:00 | deadline-feasible cohort 与 device-resident decision 决定 GPU control 是否值得；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [RoutePack](https://arxiv.org/html/2608.12146v1) | 2026-08-13T08:00:00+08:00 | 用 rollout 路由回放联合规划 expert placement 与 sample packing；3 + 3 + 3 = 9 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [The Information Abundance Paradox](https://arxiv.org/html/2608.12218v1) | 2026-08-13T08:00:00+08:00 | 长上下文训练会把学习压力从参数内化移向上下文依赖；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-PRETRAINING`，[Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Convergent Detour Hijacking](https://arxiv.org/html/2608.12273v1) | 2026-08-13T08:00:00+08:00 | 恶意 skill 可在返回正确终点前制造隐蔽资源 detour；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-PLATFORM`，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [MaSRead](https://arxiv.org/html/2608.11218v1) | 2026-08-13T08:00:00+08:00 | 将 replicated latent store 的 convergence、routing、addressing 与 composition 拆成不同义务；3 + 3 + 3 = 9 | 深入完成 | 整合：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Deployment Decision Reliability](https://arxiv.org/html/2608.11323v1) | 2026-08-13T08:00:00+08:00 | 用 agent×task 方差和 held-out reliability 判断长时评测能否支持部署决策；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [The Devil Is in the Interface](https://arxiv.org/html/2608.11386v1) | 2026-08-13T08:00:00+08:00 | 控制底层能力不变后，工具组织方式仍改变探索、步骤数与行为一致性；3 + 3 + 3 = 9 | 深入完成 | 整合：`AGENT-TOOL-CALLING`，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [When Agents Talk](https://arxiv.org/html/2608.11436v1) | 2026-08-13T08:00:00+08:00 | 共享记忆让 honeytoken 指纹可累积学习，传感器不能替代私有 reference monitor；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [A Full-Stack Characterization of High-Bandwidth Flash](https://arxiv.org/html/2608.11668v1) | 2026-08-13T08:00:00+08:00 | 区分 HBF 容量、带宽、page latency 与 KV/weight dataflow 的瓶颈；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-GPU-MEMORY`，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Towards Understanding On-Policy Distillation](https://arxiv.org/html/2608.11829v1) | 2026-08-13T08:00:00+08:00 | 用 avg@K 与 pass@K 区分采样效率提升和能力边界扩张；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [LazyTrain](https://arxiv.org/html/2608.11919v1) | 2026-08-13T08:00:00+08:00 | 联合优化 checkpoint、activation placement、重算与 CPU/GPU/NVMe overlap；3 + 3 + 3 = 9 | 深入完成 | 整合：`TRAIN-DEEPSPEED`，[Ch41](../../../../books/part-04-training-system/41-deepspeed.md) |
| [Who Thinks Best Depends on How Long You Let Them](https://arxiv.org/html/2608.12150v1) | 2026-08-13T08:00:00+08:00 | 证明 token budget 可改变单项结果和模型排序，预算是 evaluation protocol 的一部分；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

## 4. 证据与知识整合

### [Detecting a Route Flip](https://arxiv.org/html/2608.11212v1)

**旧约束。** MoE 量化常把质量回归统称为数值误差，因此工程上自然会优先保护 gate 或扩大个别张量精度。问题是 gate 的输出只决定路由，真正的损害还取决于被替换 expert 的计算差异；一次 route flip 可能无害，也可能放大误差。

**机制。** 作者以四组因果运行把损伤拆成 compute path 与 routing mediator：量化运行、冻结原路由、只替换路由以及参考运行。route margin 能提示是否容易翻转，却不能给出翻转的有害方向。设计含义是量化计划必须把 router、expert placement 与执行误差作为同一状态链观测，而不是只读 gate confidence。

**证据边界与 trade-off。** 证据覆盖 OLMoE 与跨模型实验，并包含 4-bit KV、BF16 gate 的受控组合；真实 int4 kernel 证据较弱，不能推出“任何 MoE 量化都必须保护全部 router”。更细的因果诊断增加 profiling 成本，却能避免把容量浪费在无害 flip 上。该边界已写入 Ch49 的 execution-plan contract，不改变 Ch21 的架构定义。

### [RoutePack](https://arxiv.org/html/2608.12146v1)

**旧约束。** RL rollout 已经产生真实 token-to-expert 路由，但训练系统通常仍分别决定样本 packing 与 expert placement；两套局部优化都合理，却可能让相同 step 的 attention padding 与 all-to-all 同时恶化。

**机制。** RoutePack 重放 rollout 路由，在 sealed planning window 内联合选择逐层 expert placement 和 attention/expert-aware sample packing。关键不是预测一个平均热度，而是保持 logical routing 在 forward/backward 期间的状态一致性，避免 planner 决策与执行时 ownership 漂移。

**证据边界与 trade-off。** 论文覆盖两个 Ling 模型、GSM8K 和单一 64×8 GRPO 配置；planner 开销未被完整计入端到端收益，也未证明 PP/CP、多节点和分布变化下仍成立。收益来自复用已有 rollout state，代价是更强的 step sealing、元数据与回放一致性。joint placement/packing branch 已写入 Ch36，Ch37 只承接通信后果。

### [The Information Abundance Paradox](https://arxiv.org/html/2608.12218v1)

**旧约束。** 增加训练上下文通常被视作“给模型更多证据”，但 pretraining objective 只要求降低下一 token 损失；当答案可直接从上下文读取时，模型未必需要把规律写进参数。

**机制。** 作者比较不同 context 条件，观察梯度贡献从 FFN 路径向 attention 路径移动，并用干预验证长上下文下的上下文依赖增强。它揭示了 data packaging 与 objective 的耦合：信息更多不等于 parametric knowledge 更强，训练系统需要区分 context-use 与 weight-internalization 的目标。

**证据边界与 trade-off。** 实验规模最高约 750M，不能直接外推到前沿 LLM 或所有数据混合。更短、打散或遮蔽的上下文可能增加内化压力，却牺牲长程建模与训练吞吐。该分支已写入 Ch28 的 objective/data coupling，并保留规模外推边界。

### [Cutting AI Datacenter Energy with Reinforcement Learning](https://arxiv.org/html/2608.11226v1)

在 7B、14B、72B GRPO 运行中结合功率遥测，显示 group-size 等 actuator 会在不同 sharding 下失去控制权。它支持“先证明 actuator authority，再闭合节能控制环”，但不证明跨集群节能比例。该原则已写入 Ch70，并 handoff 至训练 runtime。

### [LinearKV](https://arxiv.org/html/2608.11231v1)

v1 将 full-attention KV concatenation 与 linear layer state initialization 分开；代数上精确合并多个 state 不保证质量，单 state initializer 更稳。Ch45 已区分 token-indexed KV、fixed recurrent state、initializer/merge/reset 与失败回退，已有覆盖。

### [InfraBench](https://arxiv.org/html/2608.11234v1)

executor 与 evaluator 分开检查短期目标、持久状态、分布式不变量、副作用和清理；重复运行暴露一次 pass 隐藏的不稳定。Ch66 已要求 final-state、durability、risk 与重复运行分账，已有覆盖。

### [CORA-Diff](https://arxiv.org/html/2608.11235v1)

confidence+persistence gate 只继续更新未决位置并允许 block 提前终止，不改变 backbone/logit。结论限匹配的 Learn2PD/LLaDA/Dream 设置；Ch24 已把 mutable set、confidence/persistence gate、cache invalidation 与 fallback 串成同一 correction contract，已有覆盖。

### [Lost in Compaction](https://arxiv.org/html/2608.11242v1)

三类长上下文中，普通摘要会把持续有效约束当旧文本压缩；side channel 改善保留。Ch75 已将 constraint state 与语义摘要分离，并要求 version、scope、expiry 与执行前重验，已有覆盖。

### [Agent Safety Should Be a Runtime Contract](https://arxiv.org/html/2608.11274v1)

position paper 将 sandbox/permission 等 preventive control 与 test/log/diff/citation 等 evidential control 并置；不能把文献计数当因果证据。Ch78 已把 proposal、evidence gate 与 effect-time authority 分层，已有覆盖。

### [Lifecycle-Optimal Tokenization](https://arxiv.org/html/2608.11361v1)

总成本函数同时计训练成本与部署量、batch 相关推理成本；A10G/A100、1.3～2.3B、英语 FineWeb 结果不代表 7B+ 或多语种。Ch11 已将词表选择写为 lifecycle workload function。

### [PAIR](https://arxiv.org/html/2608.11368v1)

以 comparison pair 为统计单元，用 inclusion probability 修正 token allocation；无裁剪、无标准化、单步 estimator 才具设计无偏性。真实 GRPO 的 clipping、standardization 与多 epoch 会使实现成为近似；适用边界已写入 Ch33。

### [ForeWAM](https://arxiv.org/html/2608.11605v1)

Future-KV 由 frozen latent-action teacher 监督，用一次 Video DiT prefill 条件化 action denoising，部署不生成未来视频。Ch26 已区分 latent predictive state 与实时 controller，已有覆盖。

### [Transactional Continuity Kernel](https://arxiv.org/html/2608.11632v1)

只有 Commit 原子推进 authoritative branch head，并在提交时重验 ownership、pre-state、freshness 与 effect uniqueness。Ch81 已承载相同 transaction contract，已有覆盖。

### [The Sleeping Agent](https://arxiv.org/html/2608.11775v1)

matched compaction 把 temporal question 退化定位到日期/时间表达丢失，范围限 LoCoMo 十段对话。Ch75 已区分 facts、temporal order、constraints 与 execution frontier，已有覆盖。

### [Total Recall at What Cost?](https://arxiv.org/html/2608.11879v1)

同 backbone 与对话长度下，memory consolidation/retrieval 行为决定真实 token/call 成本，break-even 在模型间显著变化。Ch70 已按 archive write、derived view、summary、retrieval 与 rebuild 分解 memory amplification，已有覆盖。

### [Agent Skills Can Be Harmful](https://arxiv.org/html/2608.11888v1)

paired no-skill/skill 运行显示相关 skill 也可能把过重流程变成强制步骤。Ch84 已有 admission、cost-aware selection 与 no-skill baseline，已有覆盖。

### [RealisticTritonBench](https://arxiv.org/html/2608.12004v1)

任务来自真实 framework PR，kernel 必须回到原项目验证，避免孤立 shape 与宽松 tolerance 被利用。Ch66 已要求 buggy/candidate/reference state 与原仓库 validation path 同时可重放，已有覆盖。

### [Kernel-Managed Expert Cache](https://arxiv.org/html/2608.12103v1)

完整 expert-pool trace 比较 page-cache recency 与 static oracle，并揭示不同 reclaim 方法会污染设备流量。Ch54 已有 reclaim methodology 与 page-cache hit path，已有覆盖。

### [The Ingestion Tax](https://arxiv.org/html/2608.12114v1)

file-backed 权重以 mapped GPU-readable pages 与 DLPack 零拷贝缩短加载路径，同时要求 page alignment、resident cache 和正确的 activation ordering。证据集中 Apple、AMD APU、GH200 与低 batch decode，不覆盖 PCIe/batched prefill；该 Source Family 已在 Ch54 的加载路径正文中落盘。

### [Ready Cohorts](https://arxiv.org/html/2608.12123v1)

先证明 deadline-feasible cohort 上界，再判断 decision state 是否真正在 device；host decision 未移除时固定 device graph 反而更慢。Ch56 已用 ready work、deadline、device-resident decision 与 fallback 描述同一调度门，已有覆盖。

### [Convergent Detour Hijacking](https://arxiv.org/html/2608.12273v1)

skill description 控制 selection、body 控制 planning，攻击可绕一段受限 detour 后仍返回正确结果，终态 correctness 因此隐藏资源放大。Ch84 已要求 skill admission、paired no-skill baseline、运行时 path/cost budget 与撤回，已有覆盖；证据仍只覆盖一个平台与 mock backend。

### [MaSRead](https://arxiv.org/html/2608.11218v1)

论文把 query-blind KV fragment 作为 grow-only replicated store，以 content hash 保证身份与收敛，再用 opaque lexical tags 路由、hard attention mask 隔离读取。其关键增量是：存储收敛不等于可寻址，routing、addressing、recovery 与 final composition 必须分别验收。证据覆盖四类 store、自然语言多跳、两种模型家族；但 lexical connectivity 断裂时会确定性漏读，且最终回答仍受 frozen reader 限制。Ch77 已增加 latent memory 的 addressing contract，物理 KV 布局仍交给 Ch45。

### [Deployment Decision Reliability](https://arxiv.org/html/2608.11323v1)

论文用多种方差估计器拆分 agent、task 及交互效应，显示某些长时 benchmark 的总体榜单可靠性不能代表 hard slice 或 held-out family。Ch66 已要求 repeated runs、hierarchical sampling、item/rater/repeat variance 与 deployment slice，不需要因该受限三套 benchmark 再增加新机制；其具体比率不能外推为通用常数。

### [The Devil Is in the Interface](https://arxiv.org/html/2608.11386v1)

在底层信息和动作能力近似不变时，六种 tool architecture 仍改变 coding agent 的探索范围、重复运行一致性、步骤数和 token 使用。它把 tool schema 从“能力声明”推进为 behavior-shaping interface：平台需把命名、粒度、状态返回与组合方式纳入版本和评测，而不能只比较工具集合。证据来自 3 个 actor、11,700 条仓库任务轨迹，不证明同一排序迁移到 GUI、机器人或生产权限边界；机制已写入 Ch78。

### [When Agents Talk](https://arxiv.org/html/2608.11436v1)

论文证明共享记忆会把多个弱 honeytoken 指纹累积成可学习信号，因此“对可信 Agent 无害”的识别规则也可能被共享攻击者复用。Ch72 已把 shared-memory influence graph、private reference monitor、最小反馈与 effect-time authorization 分层，已有覆盖；honeytoken 仍只是指定 policy violation 的 sensor，不是攻击覆盖证明。

### [A Full-Stack Characterization of High-Bandwidth Flash](https://arxiv.org/html/2608.11668v1)

论文分解 HBF 的 page latency、plane parallelism、host/device path 与 KV/weight dataflow，避免把容量扩展直接写成 serving 加速。Ch54 已建立 persistent near-memory hierarchy、prefetch、resident state、SLO 与模拟/实机证据边界，已有覆盖；所测平台不能外推为所有 flash 或并发形态。

### [Towards Understanding On-Policy Distillation](https://arxiv.org/html/2608.11829v1)

作者在相同 sampling budget 下同时观察 avg@K 与 pass@K，发现 OPD 可提高小预算命中率，却不必扩张大预算下的可解问题集合。Ch33 已区分 policy mass relocation、sampling efficiency 与 capability boundary，并要求报告 budget-conditioned 指标，已有覆盖；该结论仅适用于所测 OPD 变体与 reasoning benchmark。

### [LazyTrain](https://arxiv.org/html/2608.11919v1)

固定 checkpoint/offload 规则在单 GPU 层流训练中简单可复现，但会让 PCIe、host memory 和 NVMe transfer 暴露在 critical path。LazyTrain 将 checkpoint selection、activation placement、recomputation 与通信 overlap 联合求解，再由 runtime 执行冻结策略。证据仅覆盖披露的 H800/RTX 3090、3B～27B 与对应 accuracy contract；MILP 求解、8-bit optimizer 和 fast clipping 引入 plan drift 与质量复验成本。该机制已接入 Ch41 的 offload working-set 主线，而非放入 Ch40 的多维并行 runtime。

### [Who Thinks Best Depends on How Long You Let Them](https://arxiv.org/html/2608.12150v1)

论文在固定任务上改变最大生成 token，观察到非单调 item 和跨 budget 模型排序反转。Ch66 已把 token/tool/attempt budget、truncation、abstention 与 operating curve 作为 evaluation identity，已有覆盖；四模型三 benchmark 的反转率不能作为跨域常数。

## 5. 缺口与下一步

- **终态保留项：** [Anthropic Multiagent Systems](https://www.anthropic.com/research/multiagent-systems) 只显示 2026-08-13，Hunyuan ELR 的展示日期与机器时间冲突；两者均缺可唯一归窗的带时区 creator-primary 时间。它们不用于正面证据、Books 或无遗漏断言。**定点重开条件：** 取得可解释首次公开时刻的官方记录后，只重开日期归属与受影响候选。
- 9 个 Books 增量已写入对应机制正文；2608.12114 此前已有唯一 Source Family marker，没有重复写入。

## 6. 复核

复核者：`/root/aug09_16`
结论：通过

独立复核从 500 项官方公告身份首项开始重放题摘语义筛选，恢复 8 个 false negative，并确认 29/29 exact-v1 可访问、未见 withdrawn 标记、§3/§4 一一对应。对 Books 的 fresh-context 比较把 10 个原提案降级为已有覆盖；9 个真正增量已逐项核对 source-family marker、正文位置、owner、证据边界与相邻衔接，其中 LazyTrain 从 Ch40 修正到更匹配 offload working-set 的 Ch41。日期不确定的 Anthropic/Hunyuan 材料作为终态保留项隔离，不用于正面证据、Books 或无遗漏断言；取得带时区 creator-primary 时间记录时只定点重开归属。
