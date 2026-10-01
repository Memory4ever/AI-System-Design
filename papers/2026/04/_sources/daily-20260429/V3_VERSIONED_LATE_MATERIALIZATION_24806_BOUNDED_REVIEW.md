# 2604.24806v1 Versioned Late Materialization：作者侧窄深入与保证边界

本项是已读旧 60 题摘中的原有潜在线索，**不增加** `106=69 潜在+37 具名前闭` 工作集合，也不是冻结候选或日 Gate。官方必要源：[exact-v1 HTML](https://arxiv.org/html/2604.24806v1) §2.1–2.3、§3.1–3.3、§4.1–4.3、§5 Tables 1–2；[v1 身份页](https://arxiv.org/abs/2604.24806v1)。HTML 页眉 `27 Apr 2026` 是版本身份，首公开仍须与本日 checkpoint 的官方公告批次、相邻 ID、DOI 代理联合链核，不把 submitted 独证当时间。

## 范围与可保留的设计差异

这是推荐模型的训练数据基础设施，而非 LLM 成绩论文；准入并非因为它能映射 `TRAIN-DATA`。其具体贡献问题是：若每个训练行都预物化长用户历史来维持在线—离线一致性，多 tenant 的不同序列长度需求使写放大和读放大先于 GPU 训练成为瓶颈。作者提出只在推理时保存近期可变历史和旧历史的 `start_ts/end_ts/length`、可选 checksum，训练时对归一化历史作有界读取并重建；只读 tier 按 user/feature_group/时间 stripe 使短历史 tenant 不必读取最长历史。这里改变的是 **snapshot correctness 与 data movement 的共同选择**，不是一般“数据库 late materialization 很快”。训练侧再以独立 DPP、预取、rebatching、相邻样本合并和同分片 hash 把远端读尽量隐藏在 GPU 工作后面；这些只在该负载与存储布局下验收。

§5 Table 1 实测三个共用 union dataset 的模型 tenant。共享 primary write bandwidth 下降 `46.2%`；但 Model A 的 primary read `−70.3%` 同时新增 immutable lookup `+62.7%`（各相对旧 primary read），per-batch load latency **增加 `9.7%`**，不能把 70.3% 当净总 I/O 节约或说每个 job 都更快。Model B/C 分别借短序列 projection 把 batch latency 降 `26.4%/36.2%`；作者以不同 host-resource read throughput 论证 lookup 资源更低，但没有从这张表得到跨平台统一成本常数。§5.2 的同长度 256–4K NE 与 Fat Row 近似，是本负载下重建未明显损伤预测的证据；更长序列的 NE/线上 A/B 同时改变序列长度及 model-side ULTRA-HSTU/VISTA 效率栈，不能归因这套数据协议独自提升模型能力，也不能外推 LLM 长上下文。

## 中央精确重建保证的必要反例（只隔离印刷主张）

§3.1 的证明前提写“历史 append-only、temporal order、immutable，events never retroactively modified or deleted”；§3.3 据此称同一时间边界的 range scan 在推理和训练阶段给**相同结果**。但 §4.1.2 又说每日 compaction 从 source-of-truth 重建整个 lookback window，§4.3 明说该重建会把被删除账户/内容的历史事件从旧历史中 scrub，并回填 SideInfo schema。构造最小反例：在请求时刻 `T_req`，已可见事件 `e` 的 event timestamp 小于记录的 `end_ts`，模型消费了 `e`；请求后、训练前有删除/历史回填，下一日 compaction 对同一时间范围的旧 stripe 去掉 `e`（或插入带旧 event timestamp 的迟到 `e'`）。训练时仅用保存的时间边界、长度和**可选** checksum 再扫描，不能自动重建请求时的字节内容；长度相同的替换甚至不被长度检查发现，checksum 不符也只检测、不给旧版本恢复路径。该反例只针对印刷的无条件 O2O **exact reconstruction** 保证；可能存在未披露的 pinned generation、事务化 read snapshot、删除后样本失效/重算或只针对不可变子集的保障，不能由本文直接断言真实生产发生了泄漏/错误。隐私删除也可能有意使过去训练样本失效，须与“精确复现旧推理输入”分成不同政策。

另一必要条件是 §3.1 的 `timestamp≤t` 只排除事件时刻晚于请求的记录：若请求后才到达、但带旧 event timestamp 的迟到事件后来进入 immutable tier，单靠 event-time predicate 也无法辨“当时已可见”与“后来回填”。重开这一保证的最小材料是 immutable snapshot/generation ID 的读取与保存、compaction 与删除/回填的版本可见性语义、checksum mismatch 的 reject/replay 路径，以及 streaming 与 batch 的独立一致性对照；不要求全系统重现，也不把坏例外泛化成所有晚物化无效。

## Owner、分数与处置提案

`ROADMAP.md` 的 `TRAIN-DATA` → [Ch27](../../../../../books/part-04-training-system/27-data.md) 已要求不可变 manifest、correction/withdrawal/supersession 传播到 derivatives/checkpoint lineage，且章末旧 `2604.24806` Review note 仅以受限口径记“event-time bounded scan、length/checksum invariant”，并未在正文采纳 unqualified O2O 保证。故作者侧拟 `Design Delta 3 + System Reach 2 + Durability 3 = 8/9`、`Deep`，`Disputed / Books 暂缓` **只针对上述精确重建保证**；系统给出的近/远历史 bifurcation、按 tenant projection 和受限成本数据仍是有效证据。请非作者核官方原句、这个反例是否被 §3–4 其它必要条件化解、以及 Ch27 的最小真实 owner gap；在此之前不把旧 V2.1 Review note 当写后 Gate，不改共享 Books 或正式日报，也不预签日期/来源/日级通过。
