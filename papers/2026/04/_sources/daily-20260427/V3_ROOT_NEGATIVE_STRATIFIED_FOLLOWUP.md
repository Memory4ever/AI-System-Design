# 04/27 旧泛化否定侧：独立分层补核

复核者：root（非 04/27 日报作者），2026-09-28。本次只检验旧“局部模型/优化方法”受影响组里的四种高混淆边界，实际打开各自的官方 exact-v1 完整题摘，并与相应 Books 主线对读。原组 158/158 题摘由日报作者核读、141 前关闭和 17 已选/恢复的账目见[子集记录](V3_GENERIC_LOCAL_METHOD_SUBSET_AUDIT.md)；本文件是独立抽查，不冒称复读 141 篇 Method，也不替代日级来源与全体候选 Gate。

| 抽样 family / 对照 owner | 独立判断与保留边界 |
| --- | --- |
| [2604.22229v1 DROL](https://arxiv.org/abs/2604.22229v1)，训练后更新边界 | 题摘确有动态分配数据 action 到当前 latent 候选、只更新赢家的 BC+critic 路线；这不是“没有状态变化”。但其动作支持与点对点 teacher 冲突在 OGBench/D4RL 的一步离线控制问题上验证，尚无模型语言生成、可验证 RLVR/GRPO group 或本书训练平台设计的必要桥。Ch33 已分 critic、reward authority 与 rollout 状态；不能把 offline action support 自动升级为 LLM 的 on-policy 更新法。维持具名前关闭，不宣称其控制任务结果无效。 |
| [2604.22282v1 STEM](https://arxiv.org/abs/2604.22282v1)，`AGENT-RAG` Ch76 | 题摘给 schema-guided atomic relation decomposition、全局 guidance subgraph 与 Triple-GNN，属于真实 KGQA 多跳检索，不因含“图”而直接收录或排除。Ch76 已有 query-specific evidence subgraph、anchor/frontier、图来源身份及实际 traversal/citation；当前摘要只显示特定 KG schema/模型组合及作者 multi-hop benchmark 增益，未给出会改变这些长期状态 owner、授权、停机或证据提交的独立条件。维持具名前关闭；若 exact-v1 Method 后续证明全局 schema 状态令现有局部图遍历的选择或证据验收失效，再定点重开。 |
| [2604.22560v1 Driving VQA](https://arxiv.org/abs/2604.22560v1)，`MULTIMODAL-EMBODIED-VLA` Ch26 | 两个不同 base VLM 的显式上下文与门控投影分别降低作者的跨阶段 NLI 矛盾；题摘自己限制两者不可作同一训练/模型的直接增益比较，并承认 lexical/structural consistency 退步。Ch26 的不可逆物理动作需要 trajectory、controller、environment feedback 与安全提交，VQA 自洽指标尚不构成这些 contract 的改变。维持驾驶问答应用的具名前关闭，不能将其 NLI 百分比外推为实际驾驶安全。 |
| [2604.22603v1 Chamelio](https://arxiv.org/abs/2604.22603v1)，`PLATFORM`/推理通信边界 | 题摘给共享主机 datapath、bounded eBPF fast path、tenant slow path 和运行周期计量，确实涉及通用多租户系统隔离；但其受测负载是自定义 TCP，而非训练 collective、模型服务 P/D 传输或 AI gateway。项目当前路线不因“通用网络系统可类比”就获得直接贡献，作者 Mreq/s 和尾延迟不作为推理 SLO 证据。维持具名前关闭；只有后续真实 AI workload 接口/反证改变现有选择时重开。 |

四项均非“关键词不匹配”关闭，而是对比原文所研究问题与现章的具体设计判断后没有足够新长期差额。此样本加上先前[安全/评价/Agent 独立审计](V3_SOURCE_NEGATIVE_INDEPENDENT_AUDIT.md)与日报作者的 158 项同理由全题摘核读，说明旧泛化理由已被定点修正：此前漏收的 `22438/22550/22169/22464/22171` 等已回到候选，而上述不同主题的否定仍有具体根据。独立抽样不能证明其它 raw 身份绝无漏项；最终仍须把来源停点、日期例外、46 个工作候选的必要证据/Books 与日级状态一起检查。
