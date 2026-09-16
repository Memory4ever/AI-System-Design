# Daily Research — 2026-07-15

**规范：** V3
**窗口：** 2026-07-14T09:00:00+08:00 ～ 2026-07-15T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T17:30:00+08:00

## 1. 结论

本窗旧报告从 482 个 arXiv 去重身份保留 55 项；按当前贡献门槛重新完成逐条题摘筛选并经独立 false-negative 复核后，候选冻结为 14 项，41 项转为有具体理由的分母前关闭。被关闭材料主要是垂直应用、局部 Agent/VLA 变体、单 benchmark 评测或只共享系统术语的工作；入选 exact v1 未见 withdrawn。

长期价值集中在四条执行链：长上下文压缩不能只报平均质量，必须显式定义 query visibility、state estimator 和 kernel；diffusion、MoE speculative 与异构 edge execution 都需要联合规划逻辑工作和物理执行；多租户 RAG 成本与 RL 训练必须把资源/评价合同纳入系统身份；Agent/VLA 还必须把可验证 claim、异步 action/observation、failure attribution 与 evaluator 的省略风险变成显式状态。重新核验发现 `2607.12875` 实际是知识驱动、多 Agent 生成推理引擎的 MetaInfer，而非 model/framework/kernel 联合搜索；错误的 Ch49 写回已清理，9 项新增机制保留，5 项沿用既有正文，待非作者重新复核后闭合。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-ANTHROPIC | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-GOOGLE-AI | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-META-AI | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-QWEN | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-DEEPSEEK | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-MOONSHOT | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-TENCENT-HUNYUAN | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-ZAI | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-BYTEDANCE-SEED | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-BAIDU-ERNIE | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-XIAOMI-MIMO | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-MINIMAX | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-ARXIV | 官方新公告；482 个去重身份完成标题巡检与含糊/高信号完整摘要筛选，独立复核后 14 项入选 | 已检查 | 无 |

代表性关闭包括 time-series anomaly、病理/营养应用、VLA 局部策略、只比较 judge 或 rubric 的单 benchmark 和 N:M sparse ViT；它们不改变本书的大模型系统设计合同。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Semidirect Fourier Delta Attention](https://arxiv.org/html/2607.11897v1) | 2026-07-15T08:00:00+08:00 ～ 2026-07-15T09:00:00+08:00 | 将 phase-controlled delta memory 与可实现的 chunk-WY kernel 共同定义；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [How Query Visibility Changes KV-Cache Compression Rankings](https://arxiv.org/html/2607.11942v1) | 2026-07-15T08:00:00+08:00 ～ 2026-07-15T09:00:00+08:00 | 证明 query-aware 与 query-blind 方法不能在同一“压缩率”下直接排名；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [LiteTopK](https://arxiv.org/html/2607.11976v1) | 2026-07-15T08:00:00+08:00 ～ 2026-07-15T09:00:00+08:00 | 把 sparse attention 的 indexer 与 TopK 融合为一个 data-movement kernel；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [FlashDiff](https://arxiv.org/html/2607.12121v1) | 2026-07-15T08:00:00+08:00 ～ 2026-07-15T09:00:00+08:00 | 以区域依赖和 stale-KV 误差界规划 diffusion serving 执行；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Cost-Governed RAG](https://arxiv.org/html/2607.12188v1) | 2026-07-15T08:00:00+08:00 ～ 2026-07-15T09:00:00+08:00 | 跨 retrieval 与 generation 归集 tenant/request 成本；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-COST，[Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [Ring-Zero](https://arxiv.org/html/2607.12395v1) | 2026-07-15T08:00:00+08:00 ～ 2026-07-15T09:00:00+08:00 | 将超大规模 zero-RL 的生成、reward 与更新组织为 ring pipeline；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [A JoLT for the KV Cache](https://arxiv.org/html/2607.12550v1) | 2026-07-15T08:00:00+08:00 ～ 2026-07-15T09:00:00+08:00 | 联合分配 Tucker rank 与 rotated residual，而非对每层统一压缩；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [EG-VAR](https://arxiv.org/html/2607.12650v1) | 2026-07-15T08:00:00+08:00 ～ 2026-07-15T09:00:00+08:00 | 把工具返回的经验事实与 Lean kernel 的形式证明组合成 typed claim；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Jetson-PI](https://arxiv.org/html/2607.12659v1) | 2026-07-15T08:00:00+08:00 ～ 2026-07-15T09:00:00+08:00 | 让异步 VLA 的未来状态显式条件于推理期间已提交的动作；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Less Experts, Faster Decoding](https://arxiv.org/html/2607.12696v1) | 2026-07-15T08:00:00+08:00 ～ 2026-07-15T09:00:00+08:00 | 将 draft acceptance 与目标模型 expert activation cost 联合优化；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Oat: Tracing Agentic Failure from the Flow of Success](https://arxiv.org/html/2607.12747v1) | 2026-07-15T08:00:00+08:00 ～ 2026-07-15T09:00:00+08:00 | 只用成功轨迹学习连续时间正常流，再以偏离定位失败步骤；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-TRACE，[Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [HeteroMosaic](https://arxiv.org/html/2607.12839v1) | 2026-07-15T08:00:00+08:00 ～ 2026-07-15T09:00:00+08:00 | 在异构 edge backend 间进行 dependency-preserving microbatch placement；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [MetaInfer: A Knowledge Only LLM Inference Engine Generator SKILL Toolbox](https://arxiv.org/html/2607.12875v1) | 2026-07-15T08:00:00+08:00 ～ 2026-07-15T09:00:00+08:00 | 用 contract knowledge base、多 Agent 分责和 staged test gates 从知识而非现成框架代码生成推理引擎；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Win by Silence](https://arxiv.org/html/2607.12986v1) | 2026-07-15T08:00:00+08:00 ～ 2026-07-15T09:00:00+08:00 | 揭示 plan evaluator 对删除与省略并不单调，并以 typed-state coverage gate 约束分数发布；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

## 4. 证据与知识整合

### [Semidirect Fourier Delta Attention](https://arxiv.org/html/2607.11897v1)
**拟采用命题。** 长上下文状态机制只有同时给出可表达的 phase/delta algebra 与可实现的 chunk-WY scan/kernel，才构成系统方案。**定位：** Method Appendix D.2、G.3；Evaluation Appendix E/E.3；Limitations §10。论文支持构造与 kernel microbenchmark，不证明端到端 LLM 质量、训练稳定性或不同硬件收益。代价是 tied state 假设、kernel 专用化与数值误差；表达或 kernel 条件不成立时回退 full attention/已验证线性 attention。Ch22 应补此 handoff。

### [How Query Visibility Changes KV-Cache Compression Rankings](https://arxiv.org/html/2607.11942v1)
**拟采用命题。** KV 压缩排名必须绑定 selector 在决策时能否看到 query；query-aware 与 query-blind 不是同一 access contract。**定位：** Method §3.1/§3.3；Evaluation §3.3、Appendix B；Limitations §7～§8。matched-budget 对照支持单一可见性变量能逆转作者 benchmark 排名，不证明其他 workload、budget 或 kernel 上相同排序。代价是 query-aware 在线计算与缓存访问；SLO 不允许时回退 query-blind/static 策略。Ch45 已承载 estimator information、budget 与 workload identity。

### [LiteTopK](https://arxiv.org/html/2607.11976v1)
**拟采用命题。** sparse attention 的 indexer 与 TopK 应联合成 data-movement kernel，避免完整 score/index 中间量落地。**定位：** Method §3.2；Evaluation §4/§4.2；Limitations §5。作者实验支持受测维度、稀疏度与 GPU 下减少 materialization，不证明端到端模型质量或任意设备收益。代价是 fused kernel 的形状/稀疏度绑定与维护成本；阈值不足时回退标准 TopK/dense kernel。Ch49 应增加 kernel 选择门槛。

### [FlashDiff](https://arxiv.org/html/2607.12121v1)
**拟采用命题。** diffusion serving 可按区域依赖与活跃度跳过局部重算，但 stale KV 必须受显式误差 guard 约束。**定位：** Method §4、§6.1；Evaluation Appendix A/A.6 与作者 image/video/audio workload；Limitations §8。结果支持作者 pipeline 的区域执行收益与二阶 stale-KV 分析，不证明其他架构或质量指标。代价是依赖跟踪、区域调度和误差累积；guard 越界时回退 full-region/full-step recompute。Ch49 应承载该 execution-plan 分支。

### [Cost-Governed RAG](https://arxiv.org/html/2607.12188v1)
**拟采用命题。** 多租户 RAG 成本身份必须沿 request/tenant 穿过 index、retrieval、rerank 与 generation，共享索引成本需要可解释分摊。**定位：** Method §3、§4.5；Evaluation §4/§4.1；Limitations §7 与 §5。原型支持受测架构的跨阶段 attribution，不证明任意云账单、缓存命中或共享基础设施分摊准确。代价是细粒度 telemetry、归属争议与测量开销；无法唯一归因时保留 shared pool/区间估算而非伪精确 chargeback。Ch70 应补该合同。

### [Ring-Zero](https://arxiv.org/html/2607.12395v1)
**拟采用命题。** 超大规模 zero-RL 需要把 rollout、reward/judge 与 update 组织为可追踪 ring pipeline，规模不能替代 evaluator contract。**定位：** Method §3、§5.5；Evaluation §2、Appendix B；Limitations §5、§8。作者结果支持其模型/任务下的扩展行为，不证明“参数规模即 reasoning”或 judge-based CoT 的事实有效性。代价是 pipeline staleness、judge 成本和 failure propagation；评价不稳时回退更小同步环、可执行 verifier 与人工 slice。Ch31 已承载，无需追加。

### [A JoLT for the KV Cache](https://arxiv.org/html/2607.12550v1)
**拟采用命题。** KV 压缩应联合分配 per-layer Tucker rank 与 rotated residual，而不是统一压缩率；逻辑误差预算必须映射到可回收物理页。**定位：** Method §4；Evaluation §6、Appendix G；Limitations §9。作者实验/消融支持联合 allocation 在受测模型中改善质量-容量曲线，不证明在线 estimator、并发 decode 或其他模型的稳定收益。代价是误差估计、metadata 与专用 kernel；预算失配时回退更高 rank/residual 或完整 KV。Ch45 应补该边界。

### [EG-VAR](https://arxiv.org/html/2607.12650v1)
exact v1 将 tool attestation、逐来源 semantic lift 与 Lean kernel 分权，只有 kernel 可铸造 `Verified`，其余路径必须 `Abstain`。**定位：** Method/Failure Appendix I；Evaluation Appendix E/E.3；Limitations Appendix M/M.1。TableBench 只支持作者表格、工具与形式化映射；未证明 semantic lift 正确、来源未污染或开放域命题等同用户意图。代价是 formalization、lineage 与 abstention；无法建立可信 lift 时回退带引用的经验回答而非伪 Verified。Ch78 应把 observation、statement、proof receipt 与 publication 连成证据门。

### [Jetson-PI](https://arxiv.org/html/2607.12659v1)
**拟采用命题。** 异步 VLA 的未来 observation 必须条件于推理期间已经 committed 的 action，并记录其实际生效时间；大模型只在置信条件触发。**定位：** Method §4.3、Appendix A；Evaluation §5/§5.1；Limitations Appendix B、§6。作者机器人实验支持其 Jetson Orin/Thor、RTX 4090 设置，不证明任意 embodiment 的 15 Hz 可靠控制或安全性。代价是 buffer/graph 状态、future-correction 误差与置信漂移；越界时回退低层 controller、减速/停机或同步 inference。Ch26 已承载，不重复写入。

### [Less Experts, Faster Decoding](https://arxiv.org/html/2607.12696v1)
**拟采用命题。** MoE speculative drafter 的目标不是只提高 acceptance，而是最小化 target verification 中新增 expert activation 与通信；高 acceptance 也可能更慢。**定位：** Method §4、Appendix F；Evaluation Appendix B/B.3；Limitations §6。作者模型与 oracle analysis 支持 expert-set overlap 会改变收益，不证明不同 routing、batch 或集群同样成立。代价是在线 predictor、expert-profile drift 和调度复杂度；收益为负时回退普通 drafter、固定候选或自回归。Ch48 应联合 accounting acceptance、FLOPs、overlap 与 communication。

### [Oat: Tracing Agentic Failure from the Flow of Success](https://arxiv.org/html/2607.12747v1)
exact v1 从成功轨迹拟合连续时间正常流，再按失败轨迹偏离排序步骤并用 conformal threshold 控制检测率。**定位：** Method §4、Appendix F；Evaluation §5、Appendix G；Limitations Appendix A、E。作者 benchmark 支持 localization，不证明因果；结果依赖表征、成功样本覆盖、轨迹长度与 failure annotation。代价是 reference-flow drift、阈值校准与误报；候选必须经 replay/intervention，覆盖不足时回退结构化人工 trace。Ch69 应承载该证据升级链。

### [HeteroMosaic](https://arxiv.org/html/2607.12839v1)
**拟采用命题。** 异构 edge inference 的 microbatch placement 必须保留 dependency，同时联合 compute、memory 与 transfer，而非只选最快 device。**定位：** Method §3.1、§6.5；Evaluation §6/§6.1；Limitations §7～§8。作者结果绑定 AMD edge platform，不证明其他加速器、模型或动态 workload。代价是 profile、切分与同步；收益不确定时回退单设备或静态 phase plan。Ch49 已有该 owner 与 state-transfer commit 边界。

### [MetaInfer: A Knowledge Only LLM Inference Engine Generator SKILL Toolbox](https://arxiv.org/html/2607.12875v1)
**拟采用命题。** 当通用推理框架的抽象层与跨模型/硬件维护成本过高时，可以把 model specification、tensor/interface contract、weight/parallel rules、platform constraints 与已验证 failure/fix 组织成 Contract Knowledge Base；实现 Agent、specification reviewer 与 verifier 分权，每一 construction stage 只由固定 test contract 决定能否前进。**定位：** Method §3.1～§3.3 与 Appendix A（generation workflow、zero-reference contract、coverage detection、independent knowledge evolution 和多 Agent 角色）；Evaluation §4.1～§4.4 与 Appendices B～C（Qwen3-8B、K100、Apple M5 和 Qwen3.6-27B/Z200 的受限 construction/runtime evidence）；Limitations §5.3。论文没有提出 model/framework/kernel 的 costed adaptation graph 或联合搜索。作者结果证明这套生成闭环能在披露目标上产生可运行 artifact，并显示缺少 reference code 会增加时间、Agent、tool call 与 token 成本；不证明生成代码语义完备、在未公开平台上自动泛化、达到全局性能最优或免除人工/环境依赖。代价是 CKB coverage/version、外部信息质量、生成与测试成本，以及局部经验过拟合；知识覆盖不足、test contract 不充分或 revalidation 失败时，应停止 promotion，回退 reference implementation 或人工开发。Ch81 已用“spec/test/optimizer 分责、分层 verifier 与 reference fallback”完整承载，因此改为已有覆盖，不再让 Ch49 承担错误机制。

### [Win by Silence](https://arxiv.org/html/2607.12986v1)
exact v1 在冻结的 26 条 route cohort 上逐步删除 plan 内容，观察 rubric 分数可能因省略而上升；typed-state gate 仅在 required deltas 全覆盖时发布分数。**定位：** Method §2.3；Evaluation §4；Limitations §9～§10。结果绑定作者 plan/scorer，不证明任意 plan 的唯一完整 inventory。代价是维护 typed inventory、模型化 typing 错误和额外 gate；inventory 不可信时回退人工 completeness review，不发布总分。Ch66 应分离 deletion perturbation、coverage state 与 score-release authority。

## 5. 缺口与下一步

无

无材料请求。9 项新增机制均已写入正文：`2607.11897` 位于 Ch22“固定大小 State 与逐 Token KV 之间还有稀疏 Item Cache”；`2607.11976` 与 `2607.12121` 位于 Ch49“Execution Plan 必须联合逻辑稀疏、Tensor Lifetime 与硬件数据流”；`2607.12188` 位于 Ch70“RAG 成本必须沿 Request 与 Tenant 穿过整条 Pipeline”；`2607.12550` 位于 Ch45“压缩、漂移与驱逐都需要可检验的误差预算”；`2607.12650` 位于 Ch78“Tool Evidence 与 Formal Proof 必须在 Typed Claim 上汇合”；`2607.12696` 位于 Ch48“Draft 结构必须同时优化 Coverage 与 Verification Waste”；`2607.12747` 位于 Ch69“Failure Attribution 必须从阶段定位升级到可证伪的因果候选”；`2607.12986` 位于 Ch66“删除扰动能揭示 Evaluator 的省略偏好”。`2607.12875` 的错误 Ch49 写回已清理，正确机制由 Ch81 的 contract/test/optimizer 分责与 verifier ladder 既有正文覆盖；Jetson-PI 与其余 3 项既有覆盖保持不变。

## 6. 复核

复核者：root（非作者独立语义复核）

结论：通过

非作者逐项复核确认：`2607.12875` 已恢复 MetaInfer 的官方题名与“Contract Knowledge Base、多 Agent 分责、分阶段测试 Gate”机制，评分、`AGENT-WORKFLOW` owner 与 Existing Coverage 判断一致；Ch49 中错误的联合搜索机制和 source-family 绑定已删除。其余 9 项整合与 4 项既有覆盖保持原证据边界，候选分母仍为 14，机械校验与语义 Gate 均闭合。
