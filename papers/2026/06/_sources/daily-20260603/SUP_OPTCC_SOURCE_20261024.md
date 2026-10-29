# Jun03 OptCC：必要证据与原 owner 差额

只补Jun02北京时间自然日；root为本记录准备者，尚未由非准备者独核，不预计候选Source通过或Books整合。当前AGENTS、研究/来源Daily与恢复/Report合同、统一Prompt、ROADMAP及Books上下文已读。与其他日期不共用研究上下文；原候选归属与有效证据不搬移。

## 身份、日期与准入

[当前官方abs](https://arxiv.org/abs/2606.01680)本轮已实际读title/完整AB/history，唯一v1，所见无撤回、删除或勘误说明；不是全历史无纠错保证。[精确v1](https://arxiv.org/html/2606.01680v1)。原题摘/history及DataCite字段保留在[既存extra原件](SUP_MODEL_OFFICIAL_EXTRA_AB_20261023.json)：v1 Jun01 04:40:41 UTC；精确DOI `10.48550/arxiv.2606.01680`，client=`arxiv.content`、state=`findable`、registered=`2026-06-02T04:21:23.000Z`。按适用公告/发号规则最早Jun02 00Z，与登记最晚界的完整可能区间均属Jun02北京时间；不是把提交或登记改名实际公开时间，尚待独立组合复算。

准入命题：健康同带宽Ring在少数NIC降速但rank仍存活时把全collective拖慢 → 将健康rank局部归约与慢rank必须参与的合并/回送拆开，再按chunk依赖流水 → 重新考虑退化网络下的数据流，而非只减小总流量或绕过慢rank。拟分2+2+2=6：机制/条件差额、跨rank与通信runtime边界、稳定的退化代价；不把作者首个理论下界或未审全证明计入贡献分数。为补已有Books具体机制而深入必要域，不以工作量改分。

## 实际必要审阅与边界

实际读§2/3问题与模型、§4.1四stage完整控制/数据流、§4.2流水与pattern/端口约束、§4.3两成本式、§4.4实现概述、§5完整评价与直接反侧、§6局限；AppendixA仅读下界陈述，没有审完B/C/D/E全证明、代码或复现。不采用完整information-theoretic最优证明、任意多straggler拓扑或多GPU扩展保证。

单straggler仍须贡献其向量且接收最终结果。健康p−1 ranks先在fast ring对自身贡献做reduce-scatter；各section的partial发给慢rank，慢rank合入自身贡献并回送全局section sum；健康ring再allgather。这四stage不允许丢弃慢rank，runtime仍拥有相同reduce结果与完成barrier。不同section/segment可以交错，让慢NIC传输与健康ring处理重叠，但必须保partial readiness、读写依赖和每端口方向单flow等约束；不同链路不自动意味着任意endpoint通信可无争用并发。另一种stage排列不是本次正文必须再讲的第二套recipe。

模型以p≥3、带宽主导、同类NIC及给定降速因子为条件，忽略每消息固定latency/kernel launch；finite chunks仍有启动/排空、同步、profiling与排序费用。rank失效、运行中移动故障、过期估计、异质拓扑不由该静态模型认证；浮点重排保持数学归约语义不自动保证bitwise相同。多GPU共享NIC扩展另有NVLink至少(g−1)倍NIC等条件，不将其外推到任意fabric。

§5是SimAI/NS3确定性模拟，配置为每server八A100、八ConnectX-6 200Gbps HDR NIC的**模型**，不是实机训练集群实验。fault-free NCCL仅健康参照，ICCL/退化NCCL与R2CCL为受限故障对照；固定通信开销估计也加入模拟时间，不与纯带宽下界混同。p16～256里较大规模P2P同步开销仍会上升。摘要2–6%不覆盖所有正文情形：两个straggler的直接反例有约8.5%额外开销，不能写普遍2–6%。没有重复模拟/统计区间或实机训练step、convergence、端到端LLM throughput/SLO验证；不转述为已获生产收益。采用段不借用任何硬件性能数字。

## 实际 owner 与最小 PRE

唯一owner `TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md)。原章已有同family alias `SF-OPTCC-ASYMMETRIC-ALLREDUCE`，旧trace记DailyJun02不搬移；当前Jun02正式候选表无本篇，不由旧Booktrace推当前Report已处理。root实际读原两段、前NCCLbpf完整组与后Overlap两完整段，Ch35/37职责沿ROADMAP核对；当前正文已有bandwidth-state planner/collective语义分责与通用代价，缺健康局部partial→慢rank合并回送→健康allgather的具体流，以及模拟而非实机的边界。

建议复用同一alias、同一owner，仅在原两个完整正文段之间插一段，不另建论文节，不拆旧marker、不改旧归属。若独核具体认为无新增必要，允许具体已有覆盖；不能只按主题相同替代实际比较。

上锚完整段：
> 正常 Ring/Tree 假设参与链路的带宽差异有限；少数链路降速但未断开时，沿用健康拓扑最容易恢复，却会让整次 AllReduce 被最慢阶段拖住。此时调度器可以把当前链路 bandwidth state、participant ordering、chunk assignment 与 collective lower bound 一起纳入计划，在不改变 reduction 结果与 step barrier 的前提下重排数据流。Network monitor 提供测量，planner 只提出 schedule，communication runtime 仍拥有 collective semantics、completion 与故障判定。

拟新增完整段：
> 重排不能简单跳过慢rank，因为它仍拥有必须归约的数据，也必须取得最终结果。一条带宽主导的条件分支先让健康ranks在快速ring上reduce-scatter自身贡献，再将各section的partial交给慢rank合入其本地贡献并回送，最后由健康ring完成allgather；不同segment按readiness流水，使慢NIC传输与健康ring处理重叠，而不是让每次健康通信都等待慢链路。[OptCC的四阶段设计](https://arxiv.org/html/2606.01680v1#S4)仍须遵守端口方向、数据依赖及完整归约/完成边界，浮点重排也不自动保持bitwise结果。更多chunks、同步与启动/排空都有成本；作者评价为SimAI配置模拟，不是实机训练或SLO验证，多个straggler的正文结果也不支持统一照抄摘要的额外开销区间。固定消息延迟、动态故障或带宽估计失配时，须重验净step收益，保留原collective及作业层恢复，不由模型下界批准任意拓扑的最优或生产提速。

下锚完整段：
> 这条分支用探测、重排和更复杂的 failure handling 换取 degraded-but-live 条件下的完成时间；带宽估计过期、链路状态震荡或额外同步开销可能使它反而更慢。理论 lower bound 只约束给定故障模型与拓扑，不能证明未知网络上的全局最优，也不能把慢链路当成健康链路。状态不可信、故障超出模型或集群稳定时，应回退经过验证的普通 Ring/Tree/hierarchical collective，必要时由作业层重启或缩容。现有证据只覆盖论文披露的链路退化模型与实验环境。

本人H2 Review note只记录必要域、模拟边界、原alias/旧trace不搬移和实际审阅状态。尚未授实际写入、未独核Source/PRE/POST，不预整合或DAY。
