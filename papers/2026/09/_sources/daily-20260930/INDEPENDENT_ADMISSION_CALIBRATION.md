# 2026-09-30 独立准入校准

- 复核者：`sep30_independent`，非报告作者。
- 窗口：`2026-09-29T09:00:00+08:00` ～ `2026-09-30T09:00:00+08:00`；检查时间：`2026-09-30T13:53:22+08:00`。
- 本轮只复核指定 11 项拟入选、4 项代表性排除的准入/日期；不恢复其他日期，不写 Books 或报告，不比较新旧 revision，不扩成全类题摘队列。
- 已重读 AGENTS、Research/Report 当前合同、Sources 使用说明/每日组/arXiv 路由、统一 Prompt、ROADMAP 和相关 checkpoint。工作树运行前已存在大量修改；本文件为唯一写入。

## 日期与撤回检查

[官方 cs.DC new](https://arxiv.org/list/cs.DC/new) 与 [官方 cs.CL new](https://arxiv.org/list/cs.CL/new) 均显示 `Wednesday, 30 September 2026`。前者新提交 15 项、总条目 36；后者新提交 145 项、总条目 326。这里只用指定身份的所在条目校准日期，没有将上述列表转化为逐项关闭队列。

[官方 availability](https://info.arxiv.org/help/availability.html) 明确提交与公开不同：材料随公告公开，周二公告为 Eastern US 20:00。当前批次的常规公告时刻据此推定为 `2026-09-29T20:00:00-04:00` 即 `2026-09-30T08:00:00+08:00`。这是官方列表批次 + 常规日程的推定，不是观测到正文上传的精确秒时；迟于提交日的公开不能用提交字段否决。没有发现本批延迟公告信号，但也不宣称独立观测了 08:00 的实际切换。

11 项当前官方 abs 都取得并读完题摘与 history，显示仅 v1，未显示撤回/删除/纠错公告。`2609.35796` 的精确 abs、v1、export 和 context 入口均不能恢复，改读官方当前 cs.CL 列表中的完整题摘；它的范围排除已明确，不声称核实了不可达 abs 的标记/版本史，也不因此建立无关正文请求。

**arXiv 首次公告不自动等于全球 first-public。** 定点原始来源核验发现：

1. **MoK 2609.36070：不能按首次公开纳入本日。** [Cursor 作者官方正文](https://cursor.com/blog/mixture-of-kittens) 标明 `Aug 4, 2026`，同一作者团队的 28 分钟机制正文已公开 push/pull 按算子选择、重组重叠、消除 CPU-GPU 同步以及 2.37×/1.41×结果，并链接公开实现。其 arXiv 迟到首收录不改变该家族上述主张的早期公开；本轮没有发现具体新增机制事件，不能以新 ID 重新评分。若作者主张本日论文有额外增量，须先指出与已公开正文不同的具体命题，再决定是否形成重要事件，不能默认为新贡献。
2. **Alignment Forecasting 2609.35805：不能把 9/30 当全球首公开。** [四作者联合署名原文](https://www.lesswrong.com/posts/f7r9QCmjoYFG9ReyF/alignment-forecasting-predicting-misalignment-from-training) 实际页日期为 `25th Sep 2026`，详细解释同一任务、benchmark、预测 scaffold、过滤实验和开放行为评估未能建立收益的反证，直接链接作者 `Full paper`。作者正文链接 [john-chen.cc/alignment_forecasting](https://www.john-chen.cc/alignment_forecasting/) 本轮不可达；这不允许把已取得的更早正文忽略。精确全球最早全文时刻仍未建立，但已经足够否定本日首次公开说法。作者日期未给时区，不伪造北京时间精确归属日。
3. **Environment Steering 2609.35807：日期需保留，不先确认为本日首次公开。** [作者公告](https://www.linkedin.com/posts/prajwal-raghunath_emnlp-llmagents-agentsafety-activity-7503276359490748416-sQMr) 明确称此前在 VLDB NOVAS 2026 展示，[官方 workshop](https://www.novasworkshop.org/) 日期为 `August 31, 2026`。这构成早期公开线索，但展示本身不证明本文精确正文曾公开。仅定点检查 [官方 OpenReview group](https://openreview.net/group?id=VLDB.org/2026/Workshop/NOVAS)（未恢复本文精确记录）及作者出版页（本文列 In Review 2026、未提供独立正文日期）。未恢复更早正文，须与“确证旧 first-public”区分：报告先作日期保留项，不用于当窗正面证据/Books；重开条件为本文已出现的官方 conference/作者原文及可核公开日期，而不是泛扫会议历史。

其余 8 项没有在本輪官方精确事件页看到更早公开正文线索，官方新公告归属成立；这不是声称穷尽全网并证明没有更早来源。

## 11 项具体准入与评分建议

评分严格针对本材料新增、拟由证据支持的命题；不把跨几个章节、成熟原则或主题相关性算成 System Reach/Durability。下表是摘要层的审阅投入建议，不是证据完成或 Books 决定。6 分需要标准审阅；若实际发现与 Books 冲突、设计反证、安全约束变化或长期知识缺口，应按合同深入受影响内容并说明触发，不能为配合 Books 更新量把所有条目自动升到 7 分。

| 材料（精确 v1） | 原始提交时间 UTC（不是公告） | 具体准入链与最小采用边界 | 建议 |
| --- | --- | --- | --- |
| [2609.36070 MoK](https://arxiv.org/abs/2609.36070v1) | 2026-09-28 18:22:34 | scale-out 通信优化迁移到 scale-up 会失效 → 按算子通信方向/重叠粒度及设备端 ring buffer 消除同步 → NVL72 MoE 层设计应重选；贡献本身清楚，但上文已明确更早正文公开 | 本日不评分，旧事件路由；不恢复 8 月 |
| [2609.36899 CadenceRL](https://arxiv.org/abs/2609.36899v1) | 2026-09-29 07:23:48 | 长轨迹尾部与大 batch 吞吐相冲突，异构硬件使逐移动估计循环依赖 → pacing/concentration 结构性重塑 + late-bound KV preparation → 异构 rollout 不只做静态路由或单一吞吐调度 | 2+2+2=6；标准，重点核 staleness/转移成本和异构对照 |
| [2609.36938 Janus](https://arxiv.org/abs/2609.36938v1) | 2026-09-29 07:50:41 | 稀疏选 KV 依赖中间值使 SSD reads 上关键路径 → 提前运行原模型 selector 预测并在 attention 前补 miss，配合读写整理 → 区分近似 prefetch 与保持输出的 attention 完成约束 | 2+2+2=6；标准，核预测时序、miss barrier 与 I/O 端到端代价 |
| [2609.36954 Purlin](https://arxiv.org/abs/2609.36954v1) | 2026-09-29 07:57:27 | collective 语义/编排/datapath 耦合妨碍硬件适配 → layout+copy/reduce 语义、共享 SNAC 与 hardware Atom 分层 → 更换移动原语时可复用 coordination，但正确性需核而不止引用解耦术语 | 2+2+2=6；标准，核 SNAC 协调不变量与 online overload 边界 |
| [2609.36959 Cobalt](https://arxiv.org/abs/2609.36959v1) | 2026-09-29 07:59:10 | 逐 expert 负载统计忽略同 token co-activation 可共享通信 → 周期跨节点合置、逐 step 节点内平衡与通信感知 task assignment → EP placement 应同时优化 token 复制目的节点与负载 | 2+2+2=6；标准，核迁移/规划开销、co-activation 漂移与对照 |
| [2609.37062 vSkipper](https://arxiv.org/abs/2609.37062v1) | 2026-09-29 09:01:41 | 少执行层不必更快，FlexiDepth 常规 loop 为负面反证 → token 按 skip 决定重组且只在盈利时路由，保留 graph/batch/KV engine 契约 → 将算法 FLOPs 减少与服务延迟改善分开 | 3+2+2=7；深入，负面结果及 quality loss 归属需保留 |
| [2609.37532 DScale](https://arxiv.org/abs/2609.37532v1) | 2026-09-29 13:17:43 | 并发验证 padding、候选拒绝与动态边界破坏 fixed graph → path tiles、scored-prefix verification budget 与 fixed-address boundary propagation → 限制 verification 工作而非统一裁短 drafter；不能据摘要声称分布保持已证明 | 2+2+2=6；标准，核 acceptance/质量与 predictor 跨域限制 |
| [2609.37626 SPLASH](https://arxiv.org/abs/2609.37626v1) | 2026-09-29 14:02:29 | launch-fixed attention layout 无法适应同批轨迹增长 → weight/KV ownership 解耦、后台迁移与 batch-boundary handoff，加 DOP → 不必 drain/restart 才能换 attention parallelism，但仅在相应 attention/head 结构成立 | 3+2+2=7；深入，核低切换开销分母、状态交接正确性与结构边界 |
| [2609.35794 Sieve/Sage](https://arxiv.org/abs/2609.35794v1) | 2026-09-17 04:59:56 | 单模型统一处理 retrieval failure 混淆无证据和干扰证据 → 显式区分两态并先轻量筛 distraction 再生成/拒答 → 拒答 pipeline 不能只用答案是否存在判定输入风险 | 2+2+2=6；标准，核 label/噪声构造与 end-to-end latency；提交17日不等于17日公开 |
| [2609.35805 Alignment Forecasting](https://arxiv.org/abs/2609.35805v1) | 2026-09-19 07:23:51 | post-hoc audit 才知 SFT 风险 → dataset push signal+base rate+model prior 做 pretraining forecast，MCQ正效与开放行为不明构成采用边界 → 不能把预测概率当部署行为保证；贡献清楚，首次正文已在窗外 | 本日不评分，旧 first-public 路由；不恢复9/25 |
| [2609.35807 Environment Steering](https://arxiv.org/abs/2609.35807v1) | 2026-09-19 20:13:58 | prompt/judge 防御依赖模型且阻断不能恢复 → runtime record-level dataflow declarative policy + violation-specific retry feedback → enforcement 与 model recovery 分离；0%仅已测攻击集 | 日期保留；有效落窗后建议 2+2+2=6，因安全执行约束变化深入受影响命题 |

不作整段全文验收：准入理由清楚但中心证明、实验归因和 Books 差异都还须作者审阅，再交独立证据复核。本轮没有以收益数字大小替代机制准入，也没有因局部/负面证据排除。

## 4 项代表性排除

| 项目 | 独立判断 |
| --- | --- |
| 2609.35796 韩语 invoice OCR | 官方列表完整题摘只建立 deep-learning OCR + image preprocessing 在领域发票上的 F1/时间表现，没有相关 foundation-model/system 机制增量；范围排除成立。列表还标 ATC 2023，但未为不影响排除的日期追索全文。abs 不可达须如实标注。 |
| [2609.35804 prompt perturbation](https://arxiv.org/abs/2609.35804) | 不是因局部/负面结果排除：题摘中的扰动可减轻而非增加 bias/hallucination，原则上可以构成反证。实际排除依据是旧 first-public：[出版方](https://link.springer.com/chapter/10.1007/978-981-96-6588-4_25) 明示 `First Online: 24 June 2025`，而 ICONIP 2024 是会议届次，不宜写成“2024 已发表”精确事实。 |
| [2609.37069 WQ-GADMM](https://arxiv.org/abs/2609.37069) | 题摘确有 window/group activation、量化、bounded staleness 与 KKT residual bound；不得泛称“无机制”。但它为一般异构 edge 分布式优化，MNIST/CIFAR 的 simulated wall-clock，没有建立针对 foundation-model 训练/通信的直接新增边界；只靠 ADMM/量化可联想到 Ch36 不足准入。排除成立。 |
| [2609.37913 Byzantine broadcast](https://arxiv.org/abs/2609.37913) | 完整题摘确有常数 metadata/四阶段 broadcast 协议及 resilience bound；本项目范围排除不是否定理论贡献，而是没有直接支撑大模型/Agent execution 主线的特定机制，不用平台章节作类比兜底。 |

## 有界查漏线索与停点

官方定点 `find` 返回相邻条目时看见 [2609.36522 ParaAnya](https://arxiv.org/abs/2609.36522) 的 PinT 重叠 timestep output caching，及 [2609.35808 MATE](https://arxiv.org/abs/2609.35808) 的 post-retrieval action normalization/任务条件 memory adaptation。它们不是因为能映射 owner 而拟入选：前者新增重叠迭代缓存命中/更新规则的可复用边界，后者以 normalization 消融挑战“检索相关和历史成功足以执行”的判断，至少值得作者定点核。已通知作者；本轮未为此全类扫描或扩大自主候选分母。

**当前停点：** 11项准入/日期校准完成（8当窗待证据、2明确早期正文、1日期保留）；4项代表性排除抽检完成（1精确abs不可达，以官方完整题摘替代）；等待作者给全候选报告与证据/Books处置，继续独立复核。此笔记不能被引用为整个Daily Gate通过。

## 8 项定点方法 / 评价 / Books 缺口复核

按作者后续请求，以下只复核 8 项当窗候选，未重置候选分母或评分。原文均为当前精确 v1；Cobalt / DScale 的网页工具 HTML/PDF 缓存未命中，后以官方精确 HTML HTTP 200 正文流读取指定章节（早次响应超时截断，后次指定主文段完整取得）。没有以缓存错误推断原文不存在，没有比较 revisions，没有实验复现或代码全审。

Books 对照是复核时现有正文，不是仅检查 source marker。以下是采用建议，仍须检查作者实际落书之后的推理链和相邻衔接。

### CadenceRL — TRAIN-DISTRIBUTED-TRAINING / Ch36

- **确有增量与位置：** [v1 §4.1–4.4、§5](https://arxiv.org/html/2609.36899v1)：以 resident-set / pending-set 改变单一 rollout pool 的长短工作组成，不只是扩缩 trainer/rollout GPU；depart 与 destination 分离，按 policy-version 保存 pending，兼容集群可做预备 KV fan-in，不兼容迁移重新 Prefill。
- **评价限制：** §6.1–6.4 / Figs10–18：trainer 故意留余量；同构大模型有吞吐与 tail 的取舍。Pacing 不用硬件标签，但 concentration 用硬件 affinity rank，不宜写“全流程无硬件配置”。Credit 控入途样本数，不硬限单轨迹年龄；30 iteration reward 曲线不是任意 staleness 的收敛证明。
- **现有覆盖 / 缺口：** Ch36 已覆盖 async staleness、resource-role reallocation、serverless actor KV 与恢复；还未解释“暂停长轨迹反而更早完成”的 resident composition 和双阶段机制。建议只增加此条件分支，把版本兼容 / re-prefill 与迁移代价保留；不要在 Ch56 复制 RL training-version 合同。Ch36 `rollout readiness / version / sampling` 邻段可承载。

### Janus — INFER-KV-CACHE / Ch45

- **确有增量与位置：** [v1 §4.2–4.4](https://arxiv.org/html/2609.36938v1)：早层 hidden state 输入目标层自己的 indexer；预测可近似，目标 selector 后的缺失集合必须读齐再 Attention。无同步 local top-k/N 仅用于 prefetch，不改变 native sparse selector；读整理、CPU 写整理和写限速共同服务 append-Prefill。
- **评价限制：** §5.1–5.3：单台8×H200，3 traces；主机虽有1TB DRAM，对照可用量限16GB，LMCache SSD-only。最高孤立 TTFT 优势不是 decode acceleration；在线只测到达率0.005，且排队缩小优势。写过慢会积压，过快干扰读；“无CPU”不能涵盖 CPU-assisted packing。
- **现有覆盖 / 缺口：** Ch45 已有物理 access plan、tier residency / fault、近似 sparse proposal、diffusion group prefetch 和 SSD selective recompute；缺的是 **native sparse Attention 的 exact selection barrier 与预测式物理预取分离**。建议把这一条 correctness-preserving residency 分支接到 offload / demand paging，而非把 selector 预测当新的 Attention approximation，Ch48 不拥有此 KV prefetch 提交边界。

### Purlin — TRAIN-DISTRIBUTED-TRAINING / Ch36，kernel 实现仅 handoff Ch49

- **确有增量与位置：** [v1 §3.1–3.3 / Algorithms1–2、§4.1–4.2](https://arxiv.org/html/2609.36954v1)：layout / copy-reduce 语义、SNAC coordination 与 Atom datapath 分层，兼容中间 layout 才能 composition；chunk ready 与 consumed ACK 分离，后者控制 staging reuse。确定 rank-order reduce 与 opt-in switch reduce 不具有相同保证。
- **评价限制：** §5、AppA/C：主要为单节点 NVIDIA GPU；AppA rooted collectives 是扩展方案，不是全部已实现。延迟 packet path 加倍流量。C4 的1GiB ReduceScatterV 部分平台反输；AIME 的30题非种子采样不能证明普遍 bitwise 等价。
- **现有覆盖 / 缺口：** Ch36 已完整讲 one-sided registration、ordering、data-ready/storage-free/ACK 与 tile-ready，所以仅再写“release/acquire”会是 No Change。实际缺口是把 **collective 语义及协调复用从硬件移动 / reduction primitive 中分离，且受 layout composition 与 numerical policy 限制**。建议 Ch36 一处补该抽象，Ch49 只接硬件 pipeline / codegen legality，不复制完整 SNAC。

### Cobalt — TRAIN-DISTRIBUTED-TRAINING / Ch36

- **确有增量与位置：** [v1 §3.1–3.4 / Eqs1–3、Algorithm1](https://arxiv.org/html/2609.36959v1)：保留 router top-k，周期 EMA co-activation / workload 全局合置，逐步节点内重平衡，再按 token 的 remote-node cover 选执行节点与副本。Global surrogate 最大化 pair co-activation，不是已知当前 batch 的完整最优通信问题。
- **评价限制：** §4.1–4.2 / Table1：16/32 B200，截层模型，50步计时包含 layout 调整；token traffic 不含 FSDP / layout-update 流量。每10步全球更新暂停训练；副本加大还需 gradient sync。任务分配复杂度 O(T·2^(N−1))，均匀采样只是期望均衡，不逐 token 强制负载界，不能外推大 EP-node 数。
- **现有覆盖 / 缺口：** Ch36 已有 expert identity、combine、权重/optimizer authority、reactive spill 和主动 replica placement，但缺“同 token 多 expert 共用跨节点传输”的目标。建议在 replica 分支补 **per-expert 负载 → co-activation / destination-node union + capacity 的联合优化**；沿用既有 gradient / optimizer / epoch 合同，不把 replica 迁移写成零成本或 router 改造。

### vSkipper — INFER-SGLANG / Ch51

- **确有增量与位置：** [v1 §3.1–3.4](https://arxiv.org/html/2609.37062v1)：device row tape 使层内 cohort 在同一 captured graph 中变化；跳层仍以本层投影写本层 KV，route-dependent map 每轮重建；dense / routed 盈利判定独立于 skip policy，decode 至多一次 dense→routed promotion。
- **评价限制：** §4.1–4.4 / Tables2–6：主性能是强制同输出长度 matched-work，与自然停止不能混。服务未增“可分辨”的额外质量损失，不等于 checkpoint 无损；BBH checkpoint 本身掉分。CoQA / Qwen3-4B 吞吐无 resolved gain，always-route 可变慢；少重复机制消融不能称充分统计证明。
- **现有覆盖 / 缺口：** Ch44 已有 decode physical metadata / graph buckets，Ch51 已有 prefix identity、piecewise graph 和阶段 state orchestration；缺 interior skip 的 **per-layer KV / current cohort maps / graph-compatible execution**。建议主 owner 在 Ch51，因为它是引擎能力而非 ordinary dense Decode 定义。盈利 threshold 只作为有硬件/模型条件的机制，不把 A100 resident-token 常数推广成通用阈值。

### DScale — INFER-SPECULATIVE-DECODING / Ch48

- **确有增量与位置：** [v1 §III-B–D / Algorithms1–2 / Eqs8、13–16](https://arxiv.org/html/2609.37532v1)：保留全长 drafter，验证侧共享8N容量，predictor prefix scores 分配非等长预算，固定地址 workspace 传递 token / position / KV / acceptance 同一边界。主文给出独立接受随机数的 stopping 及原 target verifier，完整分布推导在 supplement§3；本复核未代替其数学审阅。
- **评价限制：** §IV-A–D：主实验 A100-40GB TP1 temperature0、4任务、closed-loop8–32；不同系统 backend / drafter版本不同。Draft-training-free 不等于无训练，112K predictor 按target–drafter监督一次。Retention 对照同时扩大平均窗口及重分配，不能归因为纯分配；分量累计消融也不等于全部交互归因。
- **现有覆盖 / 缺口：** Ch48 已有 verify depth 的 opportunity-cost、shared batch budget、survival prediction、KV transaction 和 lossless 多重边界。仅讲“动态验证预算”重复。具体缺口是 **ragged verification 限容量但保留 full draft，fixed address/shape 下改变边界而不破坏 acceptance/KV commit**。建议邻接已有 Verify Length 小节补工程承载；Ch49 只 handoff tiled kernel realization，不把 budget / target-law ownership 搬走。

### SPLASH — INFER-SCHEDULING / Ch56

- **确有增量与位置：** [v1 §3–4.2](https://arxiv.org/html/2609.37626v1)：DOP 分离 projection weight 与 KV ownership；切换按 manifest 差集转移，上一层计算覆盖下一层所需迁移，静态 snapshot / batch boundary 后所有 ranks 共同 handoff。完整 causal/indexer/position/recurrent 状态及 transient HBM 可行性不可省略。
- **评价限制：** §5.2–5.5：DOP并非普遍最佳，128K B1/B4输CP；MQA/GQA受head / layout条件约束。12方向切换的<0.51%分母是256K、B16的目标 ready-layout **Prefill step**，不是普通decode。部分切入TP成本可测，但目标内存不可行，实际scheduler拒绝；转移不能任意峰值超配。
- **现有覆盖 / 缺口：** Ch56 已有动态 request / search / model-slice budget与phase boundary，Ch36已有并行原语；尚无 attention TP/DP/CP/DOP 的 **state-compatible live-layout controller**。建议 Ch56 一处采用稳态+暂态memory、切换成本、hysteresis与共同提交合同，基础并行定义沿用Ch36；不让系统controller获得模型/位置兼容性判定之外的语义权限。

### Sieve / Sage — AGENT-RAG / Ch76

- **确有增量与位置：** [v1 §3.1–3.2 / Eq1、§6](https://arxiv.org/html/2609.35794v1)：检索集合有答案仍可属 distracted；轻量 gate 先辨干扰，再让 generator 判断缺证据或生成。不同拒答原因可路由 filtering / re-retrieval，不等于 classifier 已证明真值。
- **评价限制：** §4.1、§5.2、Limitations、AppC1：标签利用 reference answer / NLI，是离线构造；主噪声模拟，expert域仍需<200标签，非zero-shot。更保守会同时降低 coverage/selective accuracy；无vLLM/quant的raw推理耗时不是生产并发吞吐。不能把不同max baseline的56.6/69.4 pp合并。
- **现有覆盖 / 缺口：** Ch76 RAG hallucination 段已拥有 prior / certainty、counterfactual groundedness、缺证据abstain与claim entailment，但未实现 **distraction vs missing evidence 的生成前gate及不同补救action**。建议保持 evidence authority owner在Ch76，把 gate 当可校准proposal；不能声称“去掉一篇文档”就证明剩余证据充分，强风险继续claim验证/人工升级。

**阶段结论：** 8 项方法均有具体现有正文缺口；主文证据支持有条件采用，不支持去除上述代价、负面项或泛化边界。保持原准入/评分建议不变。尚未见完整 Daily 或作者实际 Books 新diff，故未作 report completeness / Evidence Gate 最终验收。后续按作者请求定点核 STEPQuant、evalstats、localmixNoPE 三项拟采用命题，不延伸旧日期。

## 作者新增 3 项拟采用命题的独立证据前审

本节是作者点名命题的有界复核，不是另启类目筛选。完整官方题摘、当前状态及指定正文已读；三项精确 abs 均显示只有 v1，无撤回声明。STEPQuant / NoPE 提交为09-29 17:59:40 /17:47:41 UTC，evalstats为09-20 16:49:41 UTC；提交时间仍不单独证明全球首公开，作者维持原来源覆盖/first-public责任。

### STEPQuant — Ch54 Recurrent State 量化反馈邻段

**判断：拟命题有证据支持，须保留 conditional / approximation 修饰。** [v1 §2.2、§3.1–3.2、§4.1–4.4、AppF.1/H](https://arxiv.org/html/2609.38169v1) 给出 `E_t=A_t E_(t-1)+ε_t`，但限定相同输入和 gates；当前 readout 使用本步浮点更新态，先于本步 quantized storage，故 readout error 取上一误差经本步 transition。不能写成量化改变生成 tokens 后仍成立的完整 trajectory law。Gate lifetime 近似未完整建模时变 key-dependent transition；时间目标是 lifetime-weighted reconstruction distortion，空间 fitting 再用 row-impact，不能把二者描述为已证最优的一条乘积目标。AppF.1 要求 packed writeback 在下次 recurrent read 前完成，codes/scales/pivots需共同计容量；AppH明确仅两种GDN/KDA模型、固定负载，4bit仍有质量/长度代价。

**具体缺口：** Ch54:672现有正文只说明递归反馈与precision identity。补传播算子、readout时序及 lifetime / readout 两种敏感度，构成可验收增量；无需重复静态weight/KV量化通论。延后writeback不是free overlap，checkpoint/layout/calibration artifact与request-slot reuse仍要兼容。拟采用前审通过；等待实际正文检查。

### evalstats — Ch66 Judge Ranking 后的统计推断合同

**判断：拟命题有证据支持，不等于任意样本下已校准。** [v1 §4–6、AppB.1、§9.6](https://arxiv.org/html/2609.35815v1) 区分人类-judge agreement与下游CI/test；MCAR随机选人工subset是纠偏前提。Judge score和human label须保留同item配对及跨condition设计，不应用便利标注支撑全面有效性。估计λ本身有抽样方差，权重收缩也付power代价。小N的bootstrap-CI警告不能写成禁止所有resampling：作者恰用bootstrap评估λ稳定性。Toolkit PPI当前单factor、≥50judge items、≥15human labels且不能组合multi-run，multi-run CI与unpaired pairwise CI未验证；模拟成立不能升级成所有judge/metric有限样本保证。

**具体缺口：** Ch66:219–248已有局部soft ranking、conformal residual、人类anchor与异质性，未说明高agreement不保证hypothesis-test校准。建议独立短段把原item/human/judge lineage、设计前提、lambda uncertainty和小样本推断选择交给Evaluation owner；不要把PPI称成conformal ranking interval的替代或“人工真值已恢复”。拟采用前审通过；等待实际正文检查。

### localmixNoPE — Ch13 Causal mask / implicit position 邻段

**判断：拟命题有证据支持，需同步修正旧绝对句。** [v1 §III–VI、§VII、AppA–C/E](https://arxiv.org/html/2609.38109v1) 将SWA的有限局部混合解释为lag cross-moment，KDA为简化指数混合扩展；理论依赖mean-profile、stationary / norm-concentration等近似。Global QK readout的近远logit gap取决于矩阵lag contrast与`WQᵀWK`正alignment，cosine仅一slice；独立零均值Q/K初始化的期望readout为零，不自动继承残差recency。训练后的MLP不由init理论保证保序。120M/350M、8192训练长/4096lag有限实证不是无限长保证，§VII仍未建立bias与length-generalizability的定量关系。

**具体缺口：** Ch13:196现有mask段只说可见性与显式PE不同。增加conditional implicit recency分支可澄清“没有显式PE≠没有position signal”；但Ch13开篇:33仍写“Transformer…必须显式重新引入位置”，仅后补段会冲突，须将其限定为plain permutation-equivariant attention或传统设计。不要覆盖RoPE/ALiBi的可控位置机制和failure boundary。拟采用前审通过；等待实际正文检查。

**当前停点更新：** 8项证据 / owner正文前审 + 新增3项拟命题前审完成，已通知作者具体限制与必须修饰。未改Report / Books；未验收完整候选集合、外源覆盖、精确first-public denominator或实际写后语义。继续等待作者完整日报与当前任务Books增量后做非作者写后复核。

## 后续授权：8 项 Books 最小实施及复核身份边界

作者随后明确授予 Ch36 / Ch45 / Ch48 / Ch51 / Ch56 / Ch76 的唯一写 ownership；实施前已重读 Books 上下文、目标邻段及相邻章。以下为本代理按该授权实施的正文增量，不是对自己写入的独立验收。前述准入与定点原文审阅仍保留原阶段状态；此刻本代理对这 8 项成为 Books 写入作者，须由其他非作者完成实际写后语义复核。

| 来源 | 正文插入位置 | 新增论证边界 |
| --- | --- | --- |
| Purlin 2609.36954 | Ch36:329–333，一侧内存通信后 | 布局 / 协调 / 硬件分层，ready / consumer ACK / storage reuse，确定性与有限原语及硬件边界 |
| Cobalt 2609.36959 | Ch36:680–684，MoonEP replica 分支后 | token 共激活的 remote-node union 目标，历史 surrogate、布局停顿与保留 router / authoritative-state 合同 |
| CadenceRL 2609.36899 | Ch36:1360–1364，rollout / update pool 身份段后 | 驻留长尾、tight-fit / tail pool 与晚绑定迁移，in-flight credit 不替代 policy age，负载与迁移代价 |
| Janus 2609.36938 | Ch45:322–326，KV demand paging 后 | 跨层预测只作预取，target selector / 补读 / visibility barrier 保持精确，SSD 写读与有限负载边界 |
| DScale 2609.37532 | Ch48:243–247，Verify Length 观察后 | 完整草稿与共享 verification budget 分离，固定图的 ragged 元数据、target acceptance / KV commit，预测器与评价边界 |
| vSkipper 2609.37062 | Ch51:238–242，piecewise graph 状态 ownership 后 | RUN / ProjectOnly 行带、每层 KV 仍须投影、当前 route 元数据，dense promotion / prefix identity 与条件化收益 |
| SPLASH 2609.37626 | Ch56:373–377，exclusive batch phase switch 后 | projection / KV ownership 解耦、manifest 差集与全 ranks handoff，稳态及暂态容量、切换成本与 hysteresis |
| Sieve / Sage 2609.35794 | Ch76:777–781，缺证据 abstain 后 | distraction 与 missing 的生成前 gate、状态相关补救，classifier 不是真值、coverage / selective accuracy 与噪声边界 |

每项仅新增一个带 `semantic-body-binding:SF-2026-ARXIV-2609-…` 起止标记的正文块，每块两段；未删除或改写旧机制、未添加章末论文清单、未引入宣传性提速数字。未写 Ch13 / Ch54 / Ch66、Report 或共享索引，未 stage / commit / push。格式与绑定一致性检查只证明机械一致性，不证明独立证据验收。完成后暂停本批写入，等待作者非作者写后复核；本代理仍可复核作者写入的另外 3 项及完整 Daily。

### 作者 Ch13 / Ch54 / Ch66 实际写后独立复核

按上一节 3 项独立前审条件，重新读取实际正文及上下文，结果均通过，无当前修复要求：Ch13:33 已同步解除“必须显式 PE”的绝对说法，:199–209 保留局部混合、矩阵 lag moment / QK 读取、mean-profile 近似、有限模型与非无限外推；Ch54:253–256 明确相同输入/gates、当前 readout 先于新 writeback、时间与空间敏感度不等于统一最优乘积、packed metadata ready / 容量、gate-only 近似及有限 GDN/KDA；Ch66:237–244 区分 agreement 与推断校准，保留随机人工同 item 配对、抽样/目标设计、权重不确定性与 power、小样本 bootstrap 的有界警告。上述文件本代理未写，是对其他作者实际写入的独立语义审阅；不等于完整 Daily 或后续额外来源已验收。

### 追加授权的 WUSH / SEED 实施及停止写入

作者随后授予 Ch45 WUSH 与 Ch48 SEED 的必要最小实施。已定点阅读 complement / evidence notes、现有完整相关论证，并自行核 [WUSH exact-v1 §4.2–4.5、§5、AppD.2–D.3](https://arxiv.org/html/2609.38121v1) 与 [SEED exact-v1 §4.1–4.3、§5、AppA](https://arxiv.org/html/2609.36590v1)。两项新增仍为各两段，不重写已覆盖通论：

- WUSH `SF-2026-ARXIV-2609-38121`：Ch45:1031–1035，在 transform / bit-allocation artifact 后补 K/query 与 V/output 的 consumer surrogate 差异、post-normalization/RoPE placement 及在线代价；保留 QuEST 假设与实际 affine quantizer 区别、local L2 不等下游、校准身份和长上下文退步。
- SEED `SF-2026-ARXIV-2609-36590`：Ch48:502–506，在 MTP / full-target contract 后补 verifier-refresh deep KV、薄末两层读取 raw embedding 的同模型路径；保留标准 self-attention 而非新增 cross-attention 模块、联合训练后 target identity、provisional/accepted-prefix boundary 和有限任务/模型评价。

本代理现为以上合计 10 项 Books 正文增量作者，不能充当其独立写后验收人；主作者已接手非作者验收。`git diff --check` 通过，未复现实验。自此停止所有上述 Books 文件写入，释放 Ch45 / Ch48 给主作者后续协调；后续只读复核作者新增及完整 Report，并可更新本 notes 的审阅结果。

## 正式 Daily 的最终非作者复核

复核对象：[2026-09-30 Daily](../../30/README.md)，报告初次交付仍为“进行中”，检查时间字段为 `2026-09-30T15:36:00+08:00`。本代理不是 Report 作者。本轮只读正式报告、当日实际证据/写后记录与映射；复用前述准入及精确版本审阅，不扩扫描，不重读无关附件，不改 Report / Books。

**计数、映射与证据对应通过：** §3 实际 42 行、42 个唯一 v1 家族；§4 实际 42 个唯一证据小节，与表格无缺项/多项。37 整合 + 3 已有覆盖 + 2 仅报告、21 个实际整合章节一致；42 Stable Node / 路径均与 ROADMAP 对应，37 家族采用标记在目标正文主 `## Review notes` 前。后者只是机械存在性检查，不替代写后语义。3 已有覆盖（self-correction / hidden-date / ER-JEPA）分别给出实际正文论点；2 仅报告（MultiTalk / SYNTH 新对照）说明不改变长期机制。ER-JEPA 重开来自独立 matched-budget 反证，修正早期误关，没有把阶段 40/41 当最终分母。

**来源、日期与范围表述通过：** 14 每日来源按清单顺序自包含实际入口/分页或停止位置；Google 首15、Moonshot 10/42、Seed 1/13 页、Baidu 1/2 页、API 首80/187 等范围没有被包装成全站或全列表审阅。CL145新标题与DC24新/交叉标题不相加成唯一家族，submitted 查询仅发现、不定归属。已独立确认核心官方列表仍为 Wed30Sep，CL145new/326total、DC15new/36total；官方日程支持 Tue20EDT→Wed08BJT 推定，报告明确非实际秒级观测或全球首发证明。MoK / Alignment 更早正文排除与 Environment 展示线索日期保留区分正确；没有恢复其他日期。

**终态外部边界通过：** G1–G8 不计候选、不评分、不采用 Books、不支持覆盖通过或“无遗漏”；逐项说明缺什么、当前为何不能采用、可接受替代与定点重开。它们不是普通待审冒充外部受阻。本复核确认报告忠实限定了已执行范围和外部缺口，不声称独立证明未恢复目录里绝无材料。八项仍是终态外部保留，不能被引用成本身 Coverage / Evidence 通过。

**证据 / Books 复核权限通过：** 复用 [root 对其他作者27项实际写后记录](./ROOT_EVIDENCE_NOTES.md)、[另一个非作者的限定实际写后记录](./INDEPENDENT_COMPLEMENT_REVIEW.md) 与 [Detectability / AnswerPool 实际写后记录](./INDEPENDENT_EVIDENCE_CHECK.md)，加上本笔记对 root 三项的实际写后核，覆盖37整合项。本代理自己10项仅采用 root 非写入者验收，不自签其独立通过。逐项摘要保留理论假设、质量/反证、配置身份与未复现/非生产保证；没有用所有 source marker 的存在性自证完整语义。

**机械检查通过：** 本代理实际运行 `python3 scripts/validate_research.py --report papers/2026/09/30/README.md`，V3 一份通过；报告全部本地引用存在，报告/本 notes 的 `git diff --check` 通过。校验只证明接口一致性，非源事实证明。

**当前结论：正式报告内容与记录分工的独立语义复核通过；未发现新增研究、Books 或来源范围待办。** 已通知 Report 作者将 §5 普通待办及 §6“待复核/待机器校验”改为上述真实执行结果，再核最终状态登记。报告安全终态并不认证八项外部缺口，且不证明全网首公开穷尽、实验复现或生产性能。本代理只写本 notes；未 stage / commit / push。
