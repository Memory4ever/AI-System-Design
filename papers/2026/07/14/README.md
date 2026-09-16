# Daily Research — 2026-07-14

**规范：** V3
**窗口：** 2026-07-13T09:00:00+08:00 ～ 2026-07-14T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T17:00:00+08:00

## 1. 结论

本窗旧报告从 965 个 arXiv 去重身份保留 103 项；重新按长期大模型/Infra 贡献逐项题摘复筛并经独立 false-negative 回看后，候选收紧为 14 项。被移出的 89 项主要是 Agent/VLA 产品变体、垂直应用、AI for Science、仅局部 benchmark 或把系统名词当作贡献的工作；它们改为分母前关闭。入选 exact v1 均可访问且未见 withdrawn。

14 项共同揭示一条系统演进：优化器或 learned policy 只能提出计划，SLO guard、parser、monitor 和 security boundary 必须拥有最终 commit；内存受限 MoE、KV eviction、speculative tree、diffusion tensor lifetime、可迁移世界状态与 selective SSM 则把物理 residency、逻辑状态和可验证输出放进同一 execution contract。MemDecay 与 AAFLOW+ 沿用既有正文，其余 12 项已经写入对应 owner，并完成非作者逐项语义复核。

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
| SRC-ARXIV | 官方新公告；965 个去重身份完成标题巡检与含糊/高信号完整摘要筛选，并经独立 false-negative 回看恢复 4 项，14 项入选 | 已检查 | 无 |

代表性关闭项包括 Agent benchmark/产品变体、医学与金融应用、AI scientist、局部多模态 safety 和仅改善单数据集的方案；不为它们保留候选或零分行。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [MawForge](https://arxiv.org/html/2607.09686v1) | 2026-07-14T08:00:00+08:00 ～ 2026-07-14T09:00:00+08:00 | 按需 materialize 本地 MoE expert，在容量与载入抖动之间建立 residency contract；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Remembering Distinct Items, Not Tokens](https://arxiv.org/html/2607.09889v1) | 2026-07-14T08:00:00+08:00 ～ 2026-07-14T09:00:00+08:00 | 在 recurrent state 与 Attention 间增加按 distinct item 分配的稀疏 cache；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Trusted Floors Under Untrusted Learners](https://arxiv.org/html/2607.09992v1) | 2026-07-14T08:00:00+08:00 ～ 2026-07-14T09:00:00+08:00 | 用 verified guard 为 learned serving policy 提供最小 SLO floor；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [FlashTrie](https://arxiv.org/html/2607.10044v1) | 2026-07-14T08:00:00+08:00 ～ 2026-07-14T09:00:00+08:00 | 把 trie-constrained beam search 的 parser state 和候选扩展搬到 GPU；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-DECODE，[Ch44](../../../../books/part-05-inference-system/44-decode.md) |
| [Stateful Worlds, Stateless Elasticity](https://arxiv.org/html/2607.10389v1) | 2026-07-14T08:00:00+08:00 ～ 2026-07-14T09:00:00+08:00 | 将不可在交互时限内重建的 world-model state 变成带 exactness、deadline、bandwidth 与 atomic commit 的可迁移对象；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-DYNAMO，[Ch52](../../../../books/part-05-inference-system/52-dynamo.md) |
| [MemDecay](https://arxiv.org/html/2607.10582v1) | 2026-07-14T08:00:00+08:00 ～ 2026-07-14T09:00:00+08:00 | 按 Agent 语义 region 的生命周期执行 KV eviction；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Progressive Tree Drafting](https://arxiv.org/html/2607.10661v1) | 2026-07-14T08:00:00+08:00 ～ 2026-07-14T09:00:00+08:00 | 用渐进树展开平衡 speculative coverage 与 verification waste；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [WSqD](https://arxiv.org/html/2607.10959v1) | 2026-07-14T08:00:00+08:00 ～ 2026-07-14T09:00:00+08:00 | 用 horizon-free schedule 减少训练终点先验对 LR 的耦合；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-PRETRAINING，[Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [AAFLOW+](https://arxiv.org/html/2607.10987v1) | 2026-07-14T08:00:00+08:00 ～ 2026-07-14T09:00:00+08:00 | 将 workflow data edge 与 KV-state edge 分离，并显式定义兼容、fork、transfer、resume 与 eviction；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-DYNAMO，[Ch52](../../../../books/part-05-inference-system/52-dynamo.md) |
| [Rethinking MCP Security](https://arxiv.org/html/2607.11086v1) | 2026-07-14T08:00:00+08:00 ～ 2026-07-14T09:00:00+08:00 | 以运行中 MCP server corpus 检查 scanner coverage 与误报，而非只审 spec；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MCP，[Ch83](../../../../books/part-07-agent/83-mcp.md) |
| [Xema](https://arxiv.org/html/2607.11136v1) | 2026-07-14T08:00:00+08:00 ～ 2026-07-14T09:00:00+08:00 | 由 template-static tensor lifetime 联合规划 diffusion serving 的 memory mitigation、layout、parallelism、concurrency 与 SLO；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Calibrated e-CUSUM Decoding](https://arxiv.org/html/2607.11317v1) | 2026-07-14T08:00:00+08:00 ～ 2026-07-14T09:00:00+08:00 | 指出 token log-prob 不是量化 reasoning degeneration 的可靠 monitor observable；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-DECODE，[Ch44](../../../../books/part-05-inference-system/44-decode.md) |
| [HCRMap](https://arxiv.org/html/2607.11586v1) | 2026-07-14T08:00:00+08:00 ～ 2026-07-14T09:00:00+08:00 | 用访问压力与 3.5D 拓扑共同决定 hot expert residency；3 + 3 + 3 = 9 | 深入完成 | 整合：MODEL-MOE，[Ch21](../../../../books/part-02-model/21-moe.md) |
| [An Exact Instrument for State Usage in Selective State-Space Models](https://arxiv.org/html/2607.11796v1) | 2026-07-14T08:00:00+08:00 ～ 2026-07-14T09:00:00+08:00 | 用 exact per-mode output decomposition 区分静态 state pruning 与输入驱动的 mode migration；3 + 2 + 3 = 8 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) |

## 4. 证据与知识整合

### [MawForge](https://arxiv.org/html/2607.09686v1)
**拟采用命题。** 内存受限设备不必让全部 MoE expert 常驻；runtime 可保留公共 tensor，只按路由预测把 expert materialize 到有容量水位的 cache。**定位：** Method §4/§4.1；Evaluation §5～§6；Limitations §11、§7。作者测试支持其设备与 trace 下的可运行性，不证明任意本地硬件、路由漂移或并发下仍平稳。代价是载入 latency、预测 miss、cache thrash 与统一内存压力；miss 或水位越界时回退预热/静态 placement 或较小模型。Ch56 的增量是把 prediction error、watermark 与 eviction fallback 写进 residency controller。

### [Remembering Distinct Items, Not Tokens](https://arxiv.org/html/2607.09889v1)
**拟采用命题。** 固定 recurrent state 与逐 token KV 之间可增加按“新颖 item”分配 slot 的稀疏 cache，使容量随 distinct identity 而非序列长度增长。**定位：** Method §2、§3.1；Evaluation §3；Limitations §4。受控 associative recall 与四类序列支持该中间分支，不证明真实大模型语料、跨请求身份或开放域长期记忆。代价是 novelty threshold、identity collision 与 slot 增长；识别不稳时回退固定 recurrent state、静态 eviction 或完整 attention。Ch22 应保留为 alternative branch。

### [Trusted Floors Under Untrusted Learners](https://arxiv.org/html/2607.09992v1)
**拟采用命题。** learned serving policy 只能 propose，verified guard 必须在已声明 operating envelope 内决定 admissible action，并在越界时把控制权交给基线 scheduler。**定位：** Method §2～§3；Evaluation/operating-envelope anchors in §2；Limitations §5～§6。论文支持静态 screen 能维持被形式化的 floor，不证明未建模状态、统计尾部或 guard 外的 SLO。代价是保守拒绝、效用损失与规则维护；状态不在证明域时 fail closed 到已验证 scheduler。Ch56 应明确 commit owner 与 fallback。

### [FlashTrie](https://arxiv.org/html/2607.10044v1)
**拟采用命题。** constrained decoding 的 parser/trie state 是 runtime state；把 traversal、candidate expansion 与 beam compaction 搬到 GPU 可减少 CPU 往返，但 acceptance correctness 仍由约束状态拥有。**定位：** Method Appendix B；Evaluation Appendix J～K（NQ/GENRE 与大 trie）；Limitations §5/Discussion。结果不证明任意 grammar、动态约束或不同 GPU。代价是 device-resident parser state、显存和不规则 traversal；不支持的 grammar 或状态溢出时回退 CPU trie/reference decoder。Ch44 应补齐该边界。

### [Stateful Worlds, Stateless Elasticity](https://arxiv.org/html/2607.10389v1)
WorldMove 把 session-owned world state 作为不可分、带 fingerprint 的迁移对象：只有 transfer、verification 与 commit 都落在 readout horizon 内，且 fabric bandwidth 覆盖完整 state 与 dirty rate 时才允许迁移。**定位：** Method Appendix G、§5；Evaluation §6、§3；Limitations §8。作者分别验证 serving loop 与 mover，48 次两家 provider 内迁移 bit-identical；未构建二者同 fabric 的完整组合，跨 GPU architecture 也不保证 bit-exact。代价是带宽、停顿、校验与 dirty-state 追赶；准入失败即拒绝迁移并回退 prewarm/static placement，可重算状态仍优先 replay。Ch52 应承载 verification plane 与 fail-closed commit。

### [MemDecay](https://arxiv.org/html/2607.10582v1)
**拟采用命题。** Agent turn/region 的语义生命周期可作为 KV retention hint，但不能取得 logical context truth 的所有权。**定位：** Method §3；Evaluation §4；Limitations §5。作者 agent trace 支持受测任务中的容量收益，不证明跨 runtime、错误 region label 或对抗性重激活下的可靠性。代价是标签 metadata、误分类与关键历史被逐出；不确定或 miss 时回退完整/高优先 KV、通用 recency 或从源上下文重算。Ch45 已完整承载。

### [Progressive Tree Drafting](https://arxiv.org/html/2607.10661v1)
**拟采用命题。** speculative tree 应按观察到的 acceptance 分布逐层扩张，而不是一次生成固定树；target verification 仍拥有 commit authority。**定位：** Method §3、Appendix D；Evaluation Appendix C、G；Limitations §5。作者 overhead/quality 对照支持受测分布的 breakeven，不证明跨模型、负载或 batch 仍优。代价是树构建、分支浪费与 verifier pressure；预测收益不足时回退线性 draft、固定深度或自回归。Ch48 应补入 expansion/verification budget。

### [WSqD](https://arxiv.org/html/2607.10959v1)
**拟采用命题。** 训练终点未知时，LR schedule 不应依赖精确 horizon；shifted inverse-square-root 的稳定段与显式 cooldown 可把继续训练和停机决策解耦。**定位：** Method §1.1 与 Appendix C.3；Evaluation Appendix A、C；Limitations §5。理论与较小 LLaMA 实验支持该受限分支，不证明大规模最优性或普适超参。代价是 schedule sensitivity、cooldown 时机和继续训练状态；已知 horizon 时仍可用 cosine/WSD，异常时由 checkpoint 回退。Ch28 应加入该共存路线。

### [AAFLOW+](https://arxiv.org/html/2607.10987v1)
exact v1 以 `model/config + KV blocks + position + lineage + placement/owner` 定义 KV-state object，并将普通 data dependency 与 state edge 分开。**定位：** Method Appendix A/A.1；Evaluation Appendix F/F.1；Limitations §8～§9。fork、transfer、resume、restricted merge 与 eviction 只有 compatibility predicate 成立才提交，否则回退文本 replay/recompute；prototype 不证明任意 backend 的 zero-copy 或 safe merge。代价是 metadata、兼容检查与网络转移。Ch52 已有实体正文承载这些 policy，故只作为 exact-v1 证据。

### [Rethinking MCP Security](https://arxiv.org/html/2607.11086v1)
**拟采用命题。** MCP 安全不能只审 spec 或静态 scanner 输出；server artifact/version、capability surface、runtime behavior 与 scanner identity 必须进入同一 corpus contract。**定位：** Method §4、§2.1；Evaluation §5.2、Appendix B；Limitations §6/§6.2。实际 server 快照揭示 scanner coverage/false-positive 差异，不证明未来生态或 runtime exploitability。代价是动态执行成本与攻击面；无法沙箱运行时回退静态扫描、版本 pin 与人工复核。Ch83 应补齐证据层级。

### [Xema](https://arxiv.org/html/2607.11136v1)
Xema 先按模型、分辨率、帧数与 denoising steps 离线推导 tensor lifetime trace，只在显存压力区间启用 activation offload、chunking/fusion，并用 static layout 复用不重叠地址；planner 再联合选 memory control、parallelism 与 concurrency。**定位：** Method §4、§8；Evaluation §7.2、§9；Limitations §11。收益绑定 template-static diffusion 与作者 image/video stack，不证明动态 graph 或其他 GPU 最优。代价是离线 tracing、plan identity 与 shape drift；不匹配时回退通用 allocator 与保守配置。Ch49 应写成 `trace → pressure interval → bounded mitigation → layout → runtime check`。

### [Calibrated e-CUSUM Decoding](https://arxiv.org/html/2607.11317v1)
**拟采用命题。** 量化后 token log-prob 可能与 reasoning degeneration 脱钩，monitor 必须使用经校准的 drift observable，并把 alarm 与恢复动作分权。**定位：** Method §3；Evaluation §5～§6；Limitations §6.2、§7。数学分析否定旧中心化统计的可用性，pilot 只支持 e-CUSUM 作为候选 sensor，不证明质量恢复，且限单模型/数据/seed。代价是误报、延迟与重算；报警后回退高精度/完整 decode，由独立 owner 决定。Ch44 应明确此界线。

### [HCRMap](https://arxiv.org/html/2607.11586v1)
**拟采用命题。** MoE expert residency 必须同时考虑访问压力和 chiplet/interposer topology，而不只按 router 热度排序。**定位：** Method §6、§4；Evaluation §7/§7.1；Limitations §8。作者比较支持其 3.5D topology 下的映射收益，不证明其他 accelerator、模型或迁移成本。代价是副本容量、拓扑绑定与动态迁移；profile 漂移时回退静态 mapping 或通用 runtime scheduler。Ch21 负责原则，Ch56 负责实际 placement/迁移。

### [An Exact Instrument for State Usage in Selective State-Space Models](https://arxiv.org/html/2607.11796v1)
论文利用 diagonal selective SSM 构造 exact per-mode output decomposition 和任意 subset 的离线 pruning error，并用 frozen-signal counterfactual 定位 input-dependent write map。**定位：** Method §3；Evaluation §4；Limitations §5。两遍 oracle 读取完整首遍能量，只证明 headroom，不是 deployed saving；Mamba-2 仅 pre-norm 分解成立，低成本 estimator 只恢复少量收益。代价是首遍观测、mask identity 与额外执行；无法可靠预测时回退完整 state 或静态保守 mask。Ch22 应把静态 pruning 与 input-conditioned selection 分成两支。

## 5. 缺口与下一步

无

无材料请求。12 项新增机制均已写入正文：`2607.09686` 与 `2607.09992` 位于 Ch56“Expert Residency Controller 只能优化 Placement，不能重写 Router”；`2607.09889` 与 `2607.11796` 位于 Ch22“固定大小 State 与逐 Token KV 之间还有稀疏 Item Cache”；`2607.10044` 与 `2607.11317` 位于 Ch44“结构约束与退化监测都必须拥有显式 Runtime State”；`2607.10389` 位于 Ch52“Stateful Elasticity 必须迁移可验证的 Environment State”；`2607.10661` 位于 Ch48“Draft 结构必须同时优化 Coverage 与 Verification Waste”；`2607.10959` 位于 Ch28“不知道训练终点时，Schedule 不能依赖准确 Horizon”；`2607.11086` 位于 Ch83“Server Security 需要 Runtime Corpus Audit，不只需要 Spec Scanner”；`2607.11136` 位于 Ch49“Execution Plan 必须联合逻辑稀疏、Tensor Lifetime 与硬件数据流”；`2607.11586` 位于 Ch21“Router 连续性必须与 Expert Residency 共同设计”。MemDecay 与 AAFLOW+ 的既有正文覆盖保持不变。

## 6. 复核

复核者：`/root/aug01_10`（Books 写后非作者独立复核；准入复核沿用 `/root/aug21_31`）

结论：通过

14 项的日期、withdrawn 状态、owner 与 exact-v1 边界沿用已通过的准入复核。本轮逐项检查了 12 个新增 family 的机制正文，而不是只找 source marker：Ch56 保留 Router 与 residency/SLO authority 分离，Ch22 把 recurrent state、item cache 与 input-conditioned mode 组织为共存分支，Ch44 保存 CPU reference 和高精度回退，Ch52 将迁移建模为有 identity、lease 与原子接管的 state transaction，Ch48 保留 target commit authority，Ch28 说明 horizon-free 的适用条件，Ch83 分离静态 scanner 与 runtime corpus audit，Ch49 绑定 tensor lifetime、误差 guard 和 full recompute，Ch21 保留 topology-aware placement 的 runtime owner。所有段落均说明代价、未证明边界或旧路径，且与前后文衔接；MemDecay 与 AAFLOW+ 也确有实体正文承载。机器校验另行通过，因此本日报闭环。
