# Daily Research — 2026-08-11

**规范：** V3
**窗口：** 2026-08-10T09:00:00+08:00 ～ 2026-08-11T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-08T00:03:21+08:00

## 1. 结论

本窗 14 个每日来源均已检查。arXiv 官方公告批次跨分类去重后有 1,188 个身份；标题先排除明确领域应用，完整摘要再判断是否改变大模型或大模型基础设施的长期机制。独立复核重开高信号题摘范围后，将候选分母由 20 项修正为 31 项。高信号集中在授权与证据 lineage、MoE/KV 的状态 ownership、训练并行、serving correctness、检索执行与可归因观测，而不是单任务精度改进。

30 项完成 exact-v1 深入审阅，1 项完成标准审阅，全部检查 withdrawn；其中 11 项由现有 Books 的具体命题承载，19 项长期增量已写入对应 canonical owner，1 项因证据主要来自受控模拟且关键检测依赖 model judge 而仅保留日报。独立写后审计确认 marker 唯一、语义绑定正确且正文均位于 Review notes 之前；OpRAG 的 Daily trace owner 也已从误记的 08-09 修正为 08-11。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 归档按日期检查 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 日期列表检查；本窗没有范围内新原始研究 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind / Google Research 发布目录按日期检查 | 已检查 | 无 |
| SRC-META-AI | FAIR publication 列表按日期检查 | 已检查 | 无 |
| SRC-QWEN | 官方文章目录按日期检查 | 已检查 | 无 |
| SRC-DEEPSEEK | 官网研究与更新目录按日期检查 | 已检查 | 无 |
| SRC-MOONSHOT | 官方 Blog 与公开仓库发布入口按日期检查 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Research“全部”目录出现 ELR 项，但公开日期字段彼此冲突，已隔离 | 受阻 | 见 §5 日期材料请求 |
| SRC-ZAI | Research 日期目录按日期检查 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Research、Blog、Publications 按日期检查 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 技术博客与仓库发布入口按日期检查 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | Paper / Blog 与官方仓库按日期检查 | 已检查 | 无 |
| SRC-MINIMAX | Research / Blog 按日期检查 | 已检查 | 无 |
| SRC-ARXIV | 相关分类官方新公告跨分类去重 1,188 项；逐项题摘筛选并经独立高信号漏项复核，保留 31 项；候选 v1 均可访问且未 withdrawn | 已检查 | 无 |

没有其他按需来源被触发。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [MasDrift](https://arxiv.org/html/2608.07556v1) | 2026-08-11T08:00:00+08:00 | 将 user authorization 作为跨 agent handoff 必须保存的独立状态；3 + 3 + 3 = 9 | 深入完成 | 整合：`AGENT-MULTI-AGENT`，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [RouteGuard](https://arxiv.org/html/2608.07583v1) | 2026-08-11T08:00:00+08:00 | 用 conditional regret 与 workload-cluster sampling 判断路由收益能否被认证；3 + 2 + 3 = 8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Evidence-Locked Judge Selection](https://arxiv.org/html/2608.07813v1) | 2026-08-11T08:00:00+08:00 | 将 LLM judge 从 shipping authority 降为受 evidence admissibility 约束的 proposal；3 + 2 + 3 = 8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [CommitKV](https://arxiv.org/html/2608.07855v1) | 2026-08-11T08:00:00+08:00 | 用 tool-call commit 前后影响区分 dormant 与 completed KV；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [TelemetrySuffBench](https://arxiv.org/html/2608.07899v1) | 2026-08-11T08:00:00+08:00 | 分离 failure detection、origin localization 与证据不足时 abstention；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-TRACE`，[Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [Reproducible MoE Expert Caching](https://arxiv.org/html/2608.07911v1) | 2026-08-11T08:00:00+08:00 | 证明 replay semantics、污染与 operating regime 会反转缓存策略结论；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-GPU-MEMORY`，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Persistent Semantic Entities](https://arxiv.org/html/2608.07952v1) | 2026-08-11T08:00:00+08:00 | 将 name binding、event trigger 与跨边界 propagation 识别为隐式 Agent state；2 + 2 + 2 = 6 | 标准完成 | 仅报告：受控 runtime 与 judge 证据不足以确立普遍生产机制 |
| [EasyBalance](https://arxiv.org/html/2608.07964v1) | 2026-08-11T08:00:00+08:00 | 以跨层可执行窗口缓解单层 expert imbalance；3 + 3 + 2 = 8 | 深入完成 | 整合：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [ZeroLock](https://arxiv.org/html/2608.07974v1) | 2026-08-11T08:00:00+08:00 | 用局部目标解除 backprop update locking 并支持并发 chunk 更新；3 + 2 + 2 = 7 | 深入完成 | 整合：`TRAIN-PIPELINE-PARALLEL`，[Ch38](../../../../books/part-04-training-system/38-pipeline-parallel.md) |
| [Quality-Diversity Stress Tests for PRMs](https://arxiv.org/html/2608.08008v1) | 2026-08-11T08:00:00+08:00 | 区分 search coverage 与 exploit coverage，并限定 archive 能认证的 repair bound；3 + 2 + 3 = 8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Archer](https://arxiv.org/html/2608.08086v1) | 2026-08-11T08:00:00+08:00 | 为可回滚 diffusion LM 划分 immutable prompt reuse 与 mutable response state；3 + 2 + 3 = 8 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [OasisKV](https://arxiv.org/html/2608.08097v1) | 2026-08-11T08:00:00+08:00 | 用 speculative lookahead 预取 decode 所需稀疏 KV；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`INFER-VLLM`，[Ch50](../../../../books/part-05-inference-system/50-vllm.md) |
| [LLMVisor](https://arxiv.org/html/2608.08382v1) | 2026-08-11T08:00:00+08:00 | 以 roofline phase 与 FLOPs/I/O 将 co-batch latency 分解为可加的 request shares；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-TRACE`，[Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [FlashBoot](https://arxiv.org/html/2608.08482v1) | 2026-08-11T08:00:00+08:00 | 用连续可导出 tensor arena 与 remote mapping 移除 rack-scale weight load 的碎片和 communicator setup；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-GPU-MEMORY`，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Prompt-Invariant RLVR](https://arxiv.org/html/2608.08802v1) | 2026-08-11T08:00:00+08:00 | 分离格式与语义 reward，并约束等价 prompt 下策略一致性；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Decoupling Expert Dispatch and Aggregation](https://arxiv.org/html/2608.08853v1) | 2026-08-11T08:00:00+08:00 | 固定 dispatch 后重新学习 aggregation，揭示 routing 与 commitment 不是同一职责；3 + 2 + 3 = 8 | 深入完成 | 整合：`MODEL-MOE`，[Ch21](../../../../books/part-02-model/21-moe.md) |
| [DistillCache](https://arxiv.org/html/2608.08878v1) | 2026-08-11T08:00:00+08:00 | 以逐步 KL 近似未来 predictive influence 的 KV eviction；2 + 2 + 2 = 6，因直接影响缓存 correctness 做深入审阅 | 深入完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [SwiftQK](https://arxiv.org/html/2608.09160v1) | 2026-08-11T08:00:00+08:00 | TP 下只交换 QK-Norm 标量统计并与本地计算重叠；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`TRAIN-TENSOR-PARALLEL`，[Ch37](../../../../books/part-04-training-system/37-tensor-parallel.md) |
| [KVGov](https://arxiv.org/html/2608.09225v1) | 2026-08-11T08:00:00+08:00 | 以 principal salt 让跨租户 prefix cache key 不可共享；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [World Tokens](https://arxiv.org/html/2608.09730v1) | 2026-08-11T08:00:00+08:00 | 训练期用世界预测塑形 action representation，部署时移除视频分支；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [SPECTRA](https://arxiv.org/html/2608.07915v1) | 2026-08-11T08:00:00+08:00 | 用可逆变换去相关 KV，并按通道敏感度分配非均匀位宽；3 + 3 + 2 = 8 | 深入完成 | 整合：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [ElastiCo](https://arxiv.org/html/2608.07971v1) | 2026-08-11T08:00:00+08:00 | 将训练资源 shape、干扰预测与 shadow-price admission 放进同一弹性控制环；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`PLATFORM-GPU-SCHEDULER`，[Ch63](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md) |
| [BASIS](https://arxiv.org/html/2608.08027v1) | 2026-08-11T08:00:00+08:00 | 分离越权行为存在性与实际 breach 证据，降低单一安全探针造成的过度拒绝；3 + 2 + 3 = 8 | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [The Replay Gap](https://arxiv.org/html/2608.08239v1) | 2026-08-11T08:00:00+08:00 | 证明静态 replay 会改变后续环境状态，无法替代分支式在线 agent evaluation；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Stateful CARS](https://arxiv.org/html/2608.08282v1) | 2026-08-11T08:00:00+08:00 | 以冻结的可判定状态约束精确条件化采样，并暴露 product-state 指数增长；3 + 2 + 2 = 7 | 深入完成 | 整合：`MODEL-SAMPLING`，[Ch20](../../../../books/part-02-model/20-sampling.md) |
| [OpRAG](https://arxiv.org/html/2608.08340v1) | 2026-08-11T08:00:00+08:00 | 将检索、生成和资源阶段统一为可观测的 typed runtime 调度；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Are Agent Skills Really Reusable?](https://arxiv.org/html/2608.08453v1) | 2026-08-11T08:00:00+08:00 | 用大规模 skill corpus 揭示可复用性依赖 schema、依赖声明与失败路由元数据；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`AGENT-PLATFORM`，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [MCP Matters](https://arxiv.org/html/2608.08467v1) | 2026-08-11T08:00:00+08:00 | 证明 tool availability 本身会改变模型遵循 instruction-embedded data 的路径；3 + 3 + 2 = 8 | 深入完成 | 整合：`AGENT-MCP`，[Ch83](../../../../books/part-07-agent/83-mcp.md) |
| [RippleKV](https://arxiv.org/html/2608.08684v1) | 2026-08-11T08:00:00+08:00 | 用逐层 KV 扰动到输出 KL 的响应估计压缩敏感度；3 + 3 + 2 = 8 | 深入完成 | 整合：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [WebGPU Dispatch Bottlenecks](https://arxiv.org/html/2608.08730v1) | 2026-08-11T08:00:00+08:00 | 用顺序 dispatch 对照分离 launch overhead 与同步等待；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [KVDiagnosis](https://arxiv.org/html/2608.09412v1) | 2026-08-11T08:00:00+08:00 | 以逐设置 FullCache 对照和错误迁移矩阵诊断 KV 压缩的失效方式；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

## 4. 证据与知识整合

### [MasDrift](https://arxiv.org/html/2608.07556v1)

v1 §3～5 在 600 个 benign productivity tasks、九种 coordination condition 和 trace-level evaluator 中，把 completion、unauthorized action、over-disclosure 与 constraint loss 分开。Source defense 每次 call 回锚原始 user request，Chain defense 依赖逐跳衰减；结果支持 re-anchor 在所测配置中更稳，但任务、judge 与模型范围不构成形式保证。拟在 Ch82 的 delegation contract 中把 goal 与 authorization lineage 分离，pending side effect 必须重新绑定原始授权，handoff 不能自行产生权限。

### [RouteGuard](https://arxiv.org/html/2608.07583v1)

v1 的核心不是训练一个更高 AUC router，而是用 conditional-regret functional、finite-sample bracket 与 sampling unit 判断“路由增益是否可部署”；RouterBench 的结论会随 prompt-level 与 workload-cluster resampling 改变，OpenRCA 则拒绝认证冗余 advisors。拟在 Ch66 的 routing evaluation 中加入可拒绝的 gain certificate，并把 workload cluster 作为统计单位，避免用候选互补性或 gate AUC 替代真实增益。

### [Evidence-Locked Judge Selection](https://arxiv.org/html/2608.07813v1)

v1 在冻结 candidates、judge 与 budget 的条件下比较 majority、scalar judge 与 evidence-locked non-compensatory rule；同一 judge 可自信地降低 accuracy，而 admissibility gate 只在有 extractive certificate 时允许 override。实验规模有限且 HotpotQA 的部分检验边缘显著，不能宣称该规则普遍最优。拟在 Ch66 将 LLM judge 从 release authority 降为 proposal，证据 gate 拥有 override/repair 的提交权并记录 blast radius。

### [CommitKV](https://arxiv.org/html/2608.07855v1)

v1 方法以 tool-call commit 为边界，对同一 page 做前后删除干预，再联合测试候选 page；这比瞬时 attention eviction 更接近 agent event lifecycle，但只证明已观察任务中的 future irrelevance。拟在 Ch45 的 semantic retention 之后加入 commit-aware retirement，并明确 keys、values、position 必须同索引更新。

### [TelemetrySuffBench](https://arxiv.org/html/2608.07899v1)

v1 以 canonical multi-component traces、七类 telemetry mask 和 exact-equal ambiguous pairs 独立测 detection、origin localization 与 abstention；metadata/OTel/OpenInference views 保留 detection，却几乎失去 origin 定位，decision content 与 provenance 是主要缺失。该 benchmark 仍是同一 generator family 的受控证据，不能直接代表生产故障分布。Ch69 已明确“看到失败”不等于“定位 owner”，并要求 decision-to-provenance link 与证据不足时 abstain，已有覆盖。

### [Reproducible MoE Expert Caching](https://arxiv.org/html/2608.07911v1)

正文把 fused-event replay、模板污染和 per-layer capacity regime 分开做 intervention，显示错误 replay 可反转 LRU 类策略排名，offline optimum 也不能代表可实现收益。拟在 Ch54 的 expert tiering evaluation contract 中加入 event atomicity、uncontaminated workload 和 capacity-normalized regime 三个前提。

### [Persistent Semantic Entities](https://arxiv.org/html/2608.07952v1)

v1 §3 把 name-to-handler binding、event subscription 与 serialized propagation 形式化成隐式状态，并在受控 Rust/Python runtime 上做 mechanism ablation。论文也明确主要 detection 依赖 context-isolated LLM judge、完整人工验证推迟、部分早期显著性主张已撤回，生产 framework case 多为机制重建而非真实 incident。它提供值得保留的 threat hypothesis，但不足以把“所有 tool-agent 都存在 PSE”写成长期结论，故仅报告并保留后续独立复现实验需求。

### [EasyBalance](https://arxiv.org/html/2608.07964v1)

方法不迁移 expert，而是让不同层的 expert workload 在满足依赖的时间窗内交错执行；收益来自跨层负载互补，代价是 deferred work、调度状态和依赖正确性。拟在 Ch56 的 MoE scheduling 分支中补入 cross-layer ready-set，不写成无开销通用加速。

### [ZeroLock](https://arxiv.org/html/2608.07974v1)

论文用局部目标把 chunk update 与全局 backprop 解耦，并给出收敛界、early forwarding 与 failure recovery 原型；其证据只覆盖 edge fine-tuning 原型，不能替代大规模 BP。拟在 Ch38 将其作为 BP pipeline 的 alternative branch，保留 objective mismatch 与跨 chunk 表征漂移风险。

### [Quality-Diversity Stress Tests for PRMs](https://arxiv.org/html/2608.08008v1)

v1 用 MAP-Elites 保留每个 behavior cell 的最严重 correctness-flipping edit，并证明 covered-cell tail/average repair bound 与“覆盖比例即可约束最坏未覆盖 cell”不是同一件事；real-PRM 实验还显示 aggregation rule 会改变 exploit surface。拟在 Ch66 的 adversarial evaluation 中区分 search coverage、exploit coverage、metric-cover radius 与 archive fitting error，禁止把高覆盖率直接写成全域安全证明。

### [Archer](https://arxiv.org/html/2608.08086v1)

v1 把 diffusion LM 的 response 视为持续可改写状态，只复用 token identity 固定的 prompt K/V，并以 state neighborhood 和 decoder margin 限定 approximation；这不同于 AR 中“全部历史不可变”的普通缓存。作者 suite 的速度与质量只支持受测 DLM。拟在 Ch24 的 rollback semantics 后加入 reversible-state cache boundary，并 handoff Ch45：prompt reuse 是受状态距离约束的近似，mutable response 必须刷新，越界回退 full refresh。

### [OasisKV](https://arxiv.org/html/2608.08097v1)

lookahead token 只作为下一步 sparse-KV 重要性 proposal，后台 attention pipeline 负责 prefetch，miss 与预测误差仍付出质量/带宽代价。Ch50 已承载 speculative lookahead、host/remote KV tier 与受限 benchmark 边界，判定已有覆盖。

### [Prompt-Invariant RLVR](https://arxiv.org/html/2608.08802v1)

正文理论分析 reward entanglement 与 prompt dependency，方法用三值 reward 和等义 prompt adversary 约束策略；作者 stress test 不证明任意语义保持变换。Ch33 已明确 reward schema 与 paraphrase robustness 必须分别验收，已有覆盖。

### [Decoupling Expert Dispatch and Aggregation](https://arxiv.org/html/2608.08853v1)

在 expert IDs、计算量和 selected mass 固定时，aggregation head 仍产生可测增益，支持 router 的“选择谁”和“相信多少”应拆开；结果主要来自 OLMoE 与一次 DeepSeek replication。拟在 Ch21 路由主线中增加 dispatch/commitment ownership，不把小 head 的收益外推到所有 MoE。

### [DistillCache](https://arxiv.org/html/2608.08878v1)

论文将 eviction 视为 sequential decision，以 full-cache next-step distribution 的 KL 作为 reward；它依赖训练模型、内部信号和受测 LongBench 条件。Ch45 已有 learned eviction、质量 reference 与压缩 budget 的完整边界，因此不重复写入。

### [SwiftQK](https://arxiv.org/html/2608.09160v1)

方法利用 RMSNorm 只依赖全局平方和的结构，把 full-vector all-gather 换成 scalar statistic reduction，并在 persistent kernel 内重叠余下计算；适用性依赖 norm 定义与 topology。Ch37 已承载该通信代数与 deadlock-safe overlap，已有覆盖。

### [KVGov](https://arxiv.org/html/2608.09225v1)

论文的硬保证来自 principal-scoped HMAC salt 使 keyspace 分离；后续审计调度为仿真，不应与隔离保证混写。Ch72 已区分 cache identity、tenant principal 与 residual efficiency，已有覆盖。

### [World Tokens](https://arxiv.org/html/2608.09730v1)

World Adapter 是 action expert 的唯一视觉语义通路，future-video objective 因此塑形部署时仍保留的 world tokens；部署移除 denoiser，换取 VLA latency，但也失去在线 rollout 可视接口。Ch25 已承载 training-time world model 与 deployment-time policy 的分工，已有覆盖。

### [LLMVisor](https://arxiv.org/html/2608.08382v1)

v1 用 compute-bound / memory-bound 的 piecewise roofline 形式，将同一 dynamic batch 的总 latency 分解成可加 per-request share，并在 Llama/Qwen、A100/H100、不同 TP 与 workload mix 下校准。它证明受测引擎上的 attribution accuracy，不证明跨 kernel、量化、PD 或 scheduler policy 可直接迁移。拟在 Ch69 的 trace accounting 中增加“batch-level observability → request-level causal cost share”分支，并把 model/hardware/execution-plan revision 绑定 attribution model。

### [FlashBoot](https://arxiv.org/html/2608.08482v1)

v1 将启动瓶颈分成 per-tensor fragmentation、NCCL communicator setup 与串行 clone，再以 FabricArena 的连续可导出 tensor layout、CPU bulk load 和 remote GPU mapping 消除相应路径。NVL72 与作者模型的 headline 数字不外推，代码在 v1 仅承诺后续公开。拟在 Ch54 的 model residency 路线补入 load-ready state：artifact layout、exportable address space、remote mapping lifetime 与 clone completion 必须共同提交；不支持该 fabric 时仍回退普通 loader/NCCL。

### [SPECTRA](https://arxiv.org/html/2608.07915v1)

v1 先用可逆线性变换降低 KV 通道相关性，再依据校准集上的通道敏感度分配非均匀位宽；其收益来自表示变换与位宽预算共同作用，不能归因于通用“低比特 KV”。实验覆盖作者选择的模型、长上下文任务和校准分布，未证明 workload drift 下的稳定性。拟在 Ch45 的量化路线补入 transform identity、bit allocation 与 calibration revision 的联合版本化，分布失配时回退均匀量化或完整 KV。

### [ElastiCo](https://arxiv.org/html/2608.07971v1)

v1 将 Resource Shape Transformation、干扰预测与 shadow price 放入同一弹性 admission loop，并在 A100 集群的 64 个物理 workload 与 512 个模拟 workload 上评估。模型依赖 12 类训练 workload，不能外推到异构设备或未见作业。Ch63 已把资源 shape、干扰模型、价格信号和弹性重配置的提交边界串成完整控制环，判定已有覆盖。

### [BASIS](https://arxiv.org/html/2608.08027v1)

v1 先用 behavior-existence probe 判断危险能力是否出现，再由 breach-specific probe 判断策略边界是否真正被跨越；级联 gate 在所测开放模型和任务上减少单一探针造成的过度拒绝。attention probe 只是相关信号而非 reference monitor，也没有生产 TCB 证明。拟在 Ch72 把 capability signal 降为 proposal，只有 effect trace 与 policy-specific breach receipt 才能拥有阻断或放行权。

### [The Replay Gap](https://arxiv.org/html/2608.08239v1)

论文比较静态 replay 与从同一检查点分支出的 live trajectory：agent 的动作会改变后续页面、工具和外部状态，因此离线重放即使输入相同，也可能评估另一条世界线。结果只覆盖一个 scaffold、一个 benchmark 和有限模型，不能量化所有生产差距。拟在 Ch66 将 agent regression 分成 deterministic artifact replay 与 checkpointed live branch；前者负责可复现诊断，后者才验证状态依赖的最终效果。

### [Stateful CARS](https://arxiv.org/html/2608.08282v1)

v1 把状态化约束编译为冻结、可判定的 validator state，并用 Doob transform 对基础模型做精确条件化；形式结果给出 soundness，却也明确多个约束状态的 product construction 可能指数增长。matched comparison 没有证明普遍速度收益。拟在 Ch20 将其作为 rejection/repair 之外的 exact branch：适合有限状态且硬约束值得支付状态成本的场景，状态空间过大时仍需近似约束、拒绝采样或生成后验证。

### [OpRAG](https://arxiv.org/html/2608.08340v1)

v1 把 embedding、index lookup、rerank、prompt assembly 和 decode 表述为带 typed resource 的多阶段 runtime，并用队列与 stage telemetry 驱动调度；实验只有单 replica/GPU、FAISS 和未分布式的配置，不能证明跨 TP/PP 的收益。Ch56 已有 resource-typed request state、阶段 readiness 与端到端 SLO owner，长期机制已有覆盖。Books 留痕原误写成 2026-08-09，本轮已将 trace owner 修正为本日报 2026-08-11。

### [Are Agent Skills Really Reusable?](https://arxiv.org/html/2608.08453v1)

论文对约 13.8 万个公开 skills 做 schema、依赖和执行压力测试，并归纳接口漂移、隐藏依赖、权限和错误恢复缺失等 defect family。公开 GitHub 选择与确定性 stress test 不能代表企业私有 skill 分布。Ch84 已要求 skill artifact 声明输入输出、依赖、权限、版本和 failure routing，并以可执行验收代替目录数量，判定已有覆盖。

### [MCP Matters](https://arxiv.org/html/2608.08467v1)

v1 在 24 个 LLM、约 5.4 万次 trial 中观察：仅增加一个可调用工具，就可能让模型忽略 instruction 内嵌数据而优先发起 tool call；生产法律服务案例仍只覆盖一个 server，主要指标是首次调用和 resource utilization，不等于最终任务正确性。拟在 Ch83 将“工具存在”写成 host placement 对模型控制流的干预，要求 no-tool matched control、最终 effect receipt 与显式 authority boundary。

### [RippleKV](https://arxiv.org/html/2608.08684v1)

v1 对不同层的 KV 做受控扰动，以输出分布 KL 估计压缩敏感度，再据此分配预算。该 proxy 依赖模型、校准 prompt 和扰动强度，实验仅覆盖 LongBench，不能成为跨 workload 的固定层级真值。拟在 Ch45 的 layer-aware compression 中加入 sensitivity profile 的版本身份、校准漂移检查和 FullKV 对照。

### [WebGPU Dispatch Bottlenecks](https://arxiv.org/html/2608.08730v1)

v1 用顺序 dispatch、显式同步和不同 kernel 数量的对照，把浏览器/WebGPU 的 command submission 成本与设备执行等待分离；batch 1 下大量小 kernel 的固定开销成为瓶颈。证据不覆盖 CUDA server runtime。Ch49 已把 launch、同步和 graph capture 的固定成本放进 execution-plan owner，并保留 workload 与后端边界，判定已有覆盖。

### [KVDiagnosis](https://arxiv.org/html/2608.09412v1)

v1 为每个压缩方法与设置建立匹配的 FullCache 对照，再以 correct-to-wrong 迁移、任务适用性和 attention/intervention 诊断区分“平均分下降”背后的不同 failure。证据来自 Qwen3-8B、三次已记录 revision、greedy decoding，attention 因果分析也只在该模型完成。拟在 Ch66 把 KV 方法验收改为 per-setting matched baseline、错误迁移矩阵与适用范围声明，禁止用跨设置均值掩盖 correctness flip。

## 5. 缺口与下一步

- **终态保留项：** Hunyuan [From LR to ELR](https://hunyuan.tencent.com/research) 的公开身份可确认，但官方 API 的 `displayPublishTime`、`publishedAt`、`publicAt` 与 Research 列表日期不一致。它不支持正面证据、Books 写回或本窗无遗漏断言。**定点重开条件：** 取得带时区的首次公开记录、事件时网页存档或官方说明；恢复后只重开其真实 owner Daily，并审阅 ELR 对 `TRAIN-PRETRAINING` 的增量。

其余确定性工作已完成：19 个 Books 增量通过写后审计，OpRAG 的 Daily trace owner 已修正为 2026-08-11。ELR 只有日期冲突的外部身份线索，不支持正面证据、Books 写回或本窗遗漏断言；取得可核验首次公开记录时再定点重开真实 owner Daily。

## 6. 复核

复核者：独立 fresh-context reviewer（2026-09-08）

结论：通过

独立复核重开 1,188 个官方公告身份中的高信号题摘范围，确认原稿存在 11 个 false negative，将候选分母由 20 修正为 31；抽查原 20 项未发现需要移出分母的 false positive。31 项均核对 exact-v1 HTML 与 withdrawn 页面状态，4 项新增材料可由现有具体命题承载，7 项形成新的长期机制，OpRAG 的 Books trace owner 日期已纠正。Hunyuan ELR 日期冲突继续隔离，不支持当窗候选或覆盖断言。19 项 Books 增量逐项完成 marker、canonical owner、相邻衔接、证据边界和 Review notes 位置检查。Coverage、Candidate、Evidence、Books 与独立复核 Gate 均已闭合。Cross-model skipped: 本轮为父任务分派的非交互独立复核。
