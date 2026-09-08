# Daily Research — 2026-08-04

**规范：** V3
**窗口：** 2026-08-03T09:00:00+08:00 ～ 2026-08-04T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T18:30:00+08:00

## 1. 结论

本窗恰逢 arXiv 8 月首个大批次：官方公告索引包含 1,275 个跨分类身份。该数字没有变成候选分母；经逐项题摘语义筛选与独立 false-negative 复核，候选分母由 9 项纠正为 20 项，新增项集中在 Agent memory、KV 证据、缓存安全、异构 Kernel、调度、Diffusion refinement 与 Evaluation。20 项 v1 HTML 均可访问、未见 withdrawal，已按分数完成深入审阅。

其中 AFlex、LiveMem 与受控 orchestration 比较的长期机制已经存在于 Books；其余 17 项形成正文整合。报告不把发现列表规模当作项目贡献规模。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/) 按本窗与相邻日期检查，无符合范围的新机制正文 | 已检查 | 无 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 相邻研究日期为 Jul28 与 Aug10 | 已检查 | 无 |
| SRC-GOOGLE-AI | [DeepMind Publications](https://deepmind.google/research/publications/) 相邻日期为 Jul28 与 Aug05 | 已检查 | 无 |
| SRC-META-AI | [Research](https://ai.meta.com/research/) Aug04 上架的 WaiT 对应更早的 arXiv 首次公开家族；不按二次上架重复计分 | 已检查 | 无 |
| SRC-QWEN | [Qwen](https://qwenlm.github.io/) 按日期检查，本窗无相关正文 | 已检查 | 无 |
| SRC-DEEPSEEK | [Research](https://www.deepseek.com/) 与公开更新按日期检查，本窗无新机制正文 | 已检查 | 无 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog) 与 [GitHub](https://github.com/MoonshotAI) 按发布时间检查，本窗无相关研究事件 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | [Research“全部”列表](https://hunyuan.tencent.com/research) 中 Jul21 后下一条为 Aug11 | 已检查 | 无 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) 中 Jun16 后下一条为 Aug14 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research) 与论文目录按日期检查，下一相关条目为 Aug05 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | [技术博客](https://ernie.baidu.com/blog/zh/) 按日期检查，最近记录早于本窗 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | [MiMo](https://mimo.xiaomi.com/) 论文与博客按日期检查，本窗无条目 | 已检查 | 无 |
| SRC-MINIMAX | [Research / Blog](https://www.minimax.io/blog) 相邻研究记录不落窗 | 已检查 | 无 |
| SRC-ARXIV | Tuesday 08:00 北京时间公告；1,275 个宽身份只作发现索引，逐项题摘语义筛选与独立漏项复核后保留 20 项并重开当前 v1 原文 | 已检查 | 无 |

本窗未触发额外按需来源。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Memory Reward Inflation](https://arxiv.org/html/2608.00017v1) | 2026-08-04T08:00:00+08:00 | 揭示由同一模型自评 memory 的错误会沿检索、采信与再写回形成正反馈；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Request-Level Energy Attribution](https://arxiv.org/html/2608.00026v1) | 2026-08-04T08:00:00+08:00 | 证明 batched execution 下 token 比例不是请求边际能耗的可靠归因，并建立可校准的 Shapley reference；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-COST [Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [Action Chunk Scheduling](https://arxiv.org/html/2608.00337v1) | 2026-08-04T08:00:00+08:00 | 把远程 VLA batching 从同质 request queue 改写为受 robot action-consumption rate 约束的闭环调度；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [The Gate, Not the Cache](https://arxiv.org/html/2608.00391v1) | 2026-08-04T08:00:00+08:00 | 以受控交叉实验表明 VLA token skipping 的闭环可靠性由 gate provenance 而非 reuse/delete 机制本身决定；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Diagnose Before You Compress](https://arxiv.org/html/2608.00423v1) | 2026-08-04T08:00:00+08:00 | 让 trace reduction 保留各组件的独立 bottleneck witness，避免用预测标签循环证明 serving 诊断；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Practical Online KV Cache Compaction](https://arxiv.org/html/2608.00902v1) | 2026-08-04T08:00:00+08:00 | 揭示 Agent KV 压缩的决定变量是 proxy-query 可用时机，立即压缩与延迟压缩具有不同信息边界；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [When Does LLM Orchestration Pay Off?](https://arxiv.org/html/2608.00685v1) | 2026-08-04T08:00:00+08:00 | 在相同优化预算下比较单模型与 orchestration，要求把质量增益与额外调用成本共同归因；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Celty](https://arxiv.org/html/2608.01536v1) | 2026-08-04T08:00:00+08:00 | 将权重与激活双重稀疏的格式、解码和共享累加放入同一 GPU Kernel contract；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [V-Mem](https://arxiv.org/html/2608.01543v1) | 2026-08-04T08:00:00+08:00 | 让 memory retrieval 先判断证据模态，再执行跨模态检索与锚定；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Does Accuracy Equal Evidence?](https://arxiv.org/html/2608.01631v1) | 2026-08-04T08:00:00+08:00 | 区分压缩后答案正确、推理链受支持和对被删状态的反事实依赖；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [PrefixPlace](https://arxiv.org/html/2608.01655v1) | 2026-08-04T08:00:00+08:00 | 联合 prefix 计算、传输、复制与显存占用决定跨副本放置；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Preserving Admission Responsibility](https://arxiv.org/html/2608.01657v1) | 2026-08-04T08:00:00+08:00 | 将共享 prefix cache 的 eviction 外部性归因到产生新 KV block 的 tenant，并让责任跨请求持续；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-MULTI-TENANT [Ch71](../../../../books/part-06-ai-infrastructure/71-multi-tenant.md) |
| [LaCache](https://arxiv.org/html/2608.01718v1) | 2026-08-04T08:00:00+08:00 | 用 query 与响应前缀双重语义检查降低共享 semantic cache 的碰撞提交风险；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [REFLEX](https://arxiv.org/html/2608.01784v1) | 2026-08-04T08:00:00+08:00 | 按 Diffusion refinement 位置与收敛状态分配专家计算，而非沿用固定 token budget；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [AFlex](https://arxiv.org/html/2608.01891v1) | 2026-08-04T08:00:00+08:00 | 将 Attention/FFN 分解后的资源配置与频率控制联合起来，暴露 SLO、pipeline bubble 和能源的跨层取舍；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-PD-DISAGGREGATION [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [TELLER](https://arxiv.org/html/2608.01975v1) | 2026-08-04T08:00:00+08:00 | 把 request、host、CUDA、Kernel 与通信事件串成可检验的跨层因果切片；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-TRACE [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [Resource-Fair Scheduling](https://arxiv.org/html/2608.02244v1) | 2026-08-04T08:00:00+08:00 | 形式化长 KV request 对同 batch 短请求施加的 max-driven 成本外部性，并给出 throughput-fairness 分支；2 + 2 + 3 = 7 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [ParEvalLayer](https://arxiv.org/html/2608.02444v1) | 2026-08-04T08:00:00+08:00 | 将部分评测的继续、停止、淘汰和保留写成显式决策状态，避免观察后改规则；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [LiveMem](https://arxiv.org/html/2608.02515v1) | 2026-08-04T08:00:00+08:00 | 将长期推理状态的生命周期从 active context/KV window 中分离，定义 context turnover 下的 state continuity；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [WorldExam](https://arxiv.org/html/2608.02603v1) | 2026-08-04T08:00:00+08:00 | 把 world model 评测拆为外观、可控性、空间一致性和反应性，而非单一视频质量；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

## 4. 证据与知识整合

### [Memory Reward Inflation](https://arxiv.org/html/2608.00017v1)

正文把自评 memory 的错误沿“检索—信任—再写回”循环放大，与一次性回答误差分开，并以独立纠错器打断回路。实验只覆盖作者的 BIRD 代理环境，不证明任意 judge 都能校准。Ch77 应把 memory quality signal 与 memory write authority 分离：同一生成器的高分只能作候选证据，不能单独授权持久化或提升 provenance。

### [Request-Level Energy Attribution](https://arxiv.org/html/2608.00026v1)

§3 定义 batch energy 与 attribution target，§4 以重放 request subsets 计算 exact Shapley reference，再用低成本请求特征校准在线估计；实验覆盖三类 GPU 与 static/continuous batching。它支持“能耗是共享执行的边际成本，不等于 token 占比”，但不证明 Shapley 是唯一业务公平定义。拟在 Ch70 请求级成本段加入离线 ground truth、在线 estimator、误差预算与 chargeback policy 的分层。

### [Action Chunk Scheduling](https://arxiv.org/html/2608.00337v1)

§3 将 robot policy serving 建模为 MDP 并让 scheduler 读取 action chunk consumption；§4 同时含仿真和真实机器人 fleet。最高 18% throughput 只属于披露负载，不能外推到任意网络/控制频率。拟在 Ch56 VLA scheduling handoff 中加入：deadline 来自每台机器人剩余 action buffer，不是普通 token queue age；同质 fleet 仍可使用简单 batching，异质 consumption 才需要 state-aware scheduling。

### [The Gate, Not the Cache](https://arxiv.org/html/2608.00391v1)

§3 将 reuse/delete 与 self-harvested/clean gate 交叉，发现两种 skipping 都会在污染 gate 下累积失败；§4 以 actuation slack 执行无跳过 dense refresh，§5 在两个 policy、多个 suite 与实机上复核。该结论不证明 dense refresh 对所有控制环都免费。拟在 Ch26 stale-action/state 段加入：gate 本身必须绑定产生它的 dense observation revision，动作执行窗口可隐藏 refresh latency，但不能放松 controller veto。

### [Diagnose Before You Compress](https://arxiv.org/html/2608.00423v1)

§4 分为 candidate nomination、coverage-priority sequence 和 target-system truth verification，强制每个 scheduler/prefill/decode/KV 组件至少保留两个直接 witness；§5 与 16 种政策比较。其 F1/AUC 不证明缩减集合覆盖未测 production workload。拟在 Ch66 workload reduction 后加入：代表性分布不能代替 failure/bottleneck coverage；label 必须来自被测 target 的直接 measurement，不能由待评估预测器生成。

### [Practical Online KV Cache Compaction](https://arxiv.org/html/2608.00902v1)

§3 区分 static 与 online compaction，§4 对 boundary、repeat-prefill 和 delayed future-query proxy 做消融；立即压缩常伤害 Agent 任务，延迟获得真实 future queries 后恢复部分效果。80% 压缩结果受模型、BrowseComp-Plus/WideSearch 与预算约束。拟在 Ch45 在线 KV 分支补入：compaction decision 的信息时点是 contract；未知 future query 时优先保留、延迟或使用可恢复 tier，而不是把离线 oracle 结果当在线能力。

### [When Does LLM Orchestration Pay Off?](https://arxiv.org/html/2608.00685v1)

正文固定模型与优化预算，对单模型和编排方案比较 model-specific accuracy 与额外调用成本；结论随任务、基础模型和预算变化。它不证明 orchestration 普遍优于单次调用。Ch66 已要求 evaluation identity 同时冻结 workflow、模型、harness、预算与成本，故保持已有覆盖。

### [Celty](https://arxiv.org/html/2608.01536v1)

论文把双稀疏 SpMspV 的压缩格式、共享累加与 SIMT 解码共同设计；证据来自作者 Kernel 与模拟/微基准，不证明生产端到端收益。Ch49 应把 sparsity metadata、operand-sharing domain 与 decoder layout 纳入 execution-plan identity；规则矩阵或稀疏度不足时，dense Kernel 仍是更稳定回退。

### [V-Mem](https://arxiv.org/html/2608.01543v1)

方法先预测当前问题需要哪种证据模态，再在该模态检索并用跨模态 anchor 校验，而非把文本相似度当统一 relevance。作者评测不证明路由器在开放域可靠。Ch77 应把 modality route 视作可撤销检索计划，原始证据仍保留 provenance；路由低置信时回退多模态并行检索。

### [Does Accuracy Equal Evidence?](https://arxiv.org/html/2608.01631v1)

实验在固定 trace 上分别测最终答案、chain support 与对被删 KV 的 perturbation faithfulness，说明答案偶然正确不能证明压缩保留了证据。该结论限被测模型与任务。Ch45 的 lossy admission 应同时要求任务质量与证据保持；高风险请求仍需 full-KV replay 或不压缩。

### [PrefixPlace](https://arxiv.org/html/2608.01655v1)

论文把 prefix-compute、首次复制、传输和显存驻留共同放入 epoch planner，并保留 local-copy/recompute 分支。作者 trace 不证明任意集群的最优放置。Ch56 应让 prefix identity、replica residency 与 transfer time 进入调度状态；复用弱或拓扑漂移时回退局部计算。

### [Preserving Admission Responsibility](https://arxiv.org/html/2608.01657v1)

§II 定义 admission-responsibility gap，§III 以 metered new blocks、persistent debt、promotion gate 和 debt-directed eviction 保留责任。vLLM 实验支持 one-touch pollution 下隔离改善，但不证明 debt policy 对所有租户目标公平。拟在 Ch71 cache isolation 段加入：replacement value 回答“留谁”，admission debt 回答“谁承担回收”；idle capacity 仍可 work-conserving 共享，责任不能随请求结束消失。

### [LaCache](https://arxiv.org/html/2608.01718v1)

方法先用 query 找候选，再以新生成的前若干 token 与缓存 response 做二次语义匹配，降低相似问题、不同约束导致的错误复用。它仍依赖 embedding、阈值和威胁模型。Ch72 应把 semantic hit 视作 proposal 而非 truth：高风险响应需要 provenance、tenant/policy identity 与验证，失败回退真实推理。

### [REFLEX](https://arxiv.org/html/2608.01784v1)

正文保持 router 结构不变，却按 block-relative refinement position 与收敛 frontier 动态分配 expert budget。作者 workload 只支持该 Diffusion-MoE 分支。Ch24 应说明：并行 refinement 中 token 的计算价值随 step 变化；自适应预算换来调度与训练复杂度，短轨迹或校准不足时固定预算仍合理。

### [AFlex](https://arxiv.org/html/2608.01891v1)

§III 显示 Attention/FFN 的 energy-optimal frequency 随 phase/workload 改变，§IV 联合 global provisioning、local DVFS 与 interleaved pipeline；A800/Qwen3/Mixtral 作者实验只支持该 operating point。Ch55 已纳入“operator specialization 只有在通信、bubble、控制稳定性共同核算后才成立”，无需重复。

### [TELLER](https://arxiv.org/html/2608.01975v1)

系统以 NVTX、CUPTI 与日志关联 request、host、CUDA、Kernel 和 communication，构造 call-chain tree 与 causal slice，再用受限搜索定位性能根因。证据只覆盖作者环境。Ch69 应把 correlation 与 causality 分开：trace context 建立候选依赖，干预或重放才支持根因；缺层或时钟漂移时只能报告相关性。

### [Resource-Fair Scheduling](https://arxiv.org/html/2608.02244v1)

§2 将 batch step 的 max KV footprint 外部性形式化，§3 给出 ISJL 及竞争界；数值实验不是生产 trace。拟在 Ch56 fairness 段补入：token-metered revenue 与 max-driven GPU cost 并不天然对齐，co-batching 应约束 active-context 差距；FCFS 在简单公平诉求下仍合理，LJF/ISJL 用灵活性换成本一致性。

### [ParEvalLayer](https://arxiv.org/html/2608.02444v1)

论文把 partial evaluation 的继续、提前停止、淘汰与保留定义为预注册四状态规则，避免观察中途按结果改阈值。它不能证明所有任务都可安全早停。Ch66 应要求停止规则、最小证据量与失败成本进入评测合同；不满足可分层假设时回退完整评测。

### [LiveMem](https://arxiv.org/html/2608.02515v1)

§2 明确定义 context turnover 下 memory state continuity，§3 用 recurrent memory state、side attention 和 memory-oriented post-training 使历史状态在原 token/KV 释放后仍可用；实验只支持作者模型与评测。Ch22 已区分 bounded active context、persistent state、重建与失效边界，保留现有正文。

### [WorldExam](https://arxiv.org/html/2608.02603v1)

评测将外观质量、action controllability、空间一致性与交互反应性分开，避免把视频观感外推为可规划环境。1,474 个案例与 20 个模型只证明该 suite 的区分能力，不证明 causal correctness。Ch66 应把 world-model evaluation 绑定 action schema、状态可达性与 closed-loop reactivity；自由视频生成分数不能替代环境契约。

## 5. 缺口与下一步

无

本窗没有可执行未决或外部材料请求。20 项候选均完成证据判断与 Books 决定。

## 6. 复核

复核者：独立复核智能体（2026-09-07）
结论：通过

复核纠正 11 项 false negative。以 1,275 个 official-announcement identity 为分母逐题摘重筛；20 项均复核 exact-v1、withdrawal、评分、证据边界与 owner。3 项已有覆盖真实，17 项长期机制均位于 canonical owner 的正文区。
