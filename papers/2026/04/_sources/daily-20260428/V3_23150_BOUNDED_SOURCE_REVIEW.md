# 2604.23150v1 有界证据审阅与 Ch56 Books 提案（日期未独立过 Gate）

固定窗口 `[2026-04-27 09:00, 2026-04-28 09:00) +08:00`。本页复用[root 对贡献与 owner 的独立校准](./V3_ROOT_TWO_MOE_OWNER_INDEPENDENT.md)，定点重开[官方 exact-v1 正文](https://arxiv.org/html/2604.23150v1) §3.3.3、§4.1–4.2、§5.1–5.3，并对读 [Ch56 的 prefill signature→locality routing 正文](../../../../../books/part-05-inference-system/56-inference-scheduling.md)。[日期组合](./V3_TWO_MOE_DATE_PROPOSAL.md)仍是作者侧本窗有据推断，**尚待非作者日期复核**；故本页不把它计入正式分母、评分表或实际 Books 整合。

## 贡献与机制

Ch56 已有“prefill 观测 expert activation → 请求按 expert locality 路由 → locality band 内再看负载”，且明说每个 decoder 的 expert placement 可用相同统计但不归 routing policy 偷改。这篇的最窄新增责任是 **placement 统计必须条件化在将由该 expert group 服务的 request cluster 上**，不只按全局 expert 热度或一张 pairwise 共激活矩阵放置。原文 §4.1 对历史 *decode* 的 request×expert activation 向量做 L2 归一化与 K-means，把 cluster 映射到 group；§4.2 Eq.5 对映射到 group `d` 的 clusters 求 `U_{d,e}`，先以容量约束安放每个唯一 expert。prefill activation 则是新请求推断类型／成组的信号，不是已知未来 decode 路由的 oracle。主 owner 为 `INFER-SCHEDULING`/Ch56；Ch21 仅模型 router/placement 分权的交接，Ch36 训练 EP 不是本文 decode 调度的 owner。

## 主要受测证据及不成立的跃迁

- §3.3.3 的 prefill/decode 逐层 expert-count 相关性在三受测模型不同（Maverick `.82`、Qwen3 `.68`、DeepSeek-V3 `.55`），不能假定每请求准确预测。§5.1 的 80/20 是**同七个已知数据集**上的 request-type 分类；最高准确度不是未知业务域/线上分布保持证明。
- §4.2 给出可选 redundant-copy 第二阶段，但该节明确 **evaluation 不用 redundant experts**；§5.2 的 EPLB 对照也设零副本。不能把测得收益归因到复制或声称已测副本容量成本。
- §5.2 的 DeepSeek-V3 `DP8TP8→EP64`、500 global batches、Layer 42 中位归一化 all-to-all 数据量为 `.94` 对 linear/EPLB `1.00`；§5.3 的 Maverick 100 batches 有最多约 20% message-size 下降，但 padding-to-max kernel 下仅约 9% communication-time、5.5% layer-time，Qwen3 单代表层约 12%/6%。这是受测层／通信合同，不是端到端 request SLO、任意拓扑吞吐或在线稳定收益。
- §3.3.3 指出仅凭 expert activation 可能推断请求类型；不能沿论文另一处“未记录 prompt 文本即 fully mitigates privacy”升级为隐私保证。实际采用需限定 trace 可见权限、保留期限与重聚类版本。放置刷新、cluster drift、额外 metadata/运维成本及普通全局热度／least-load 的回退都仍成立。

若日期非作者复核确认属于本窗，贡献阈值可暂拟 `Design 2 + System 2 + Duration 2 = 6`；由于 Ch56 有真实条件化 placement 缺口，按 Books gap 触发深入必要审阅，而非因 6 分本身自动深入。拟在 Ch56 现有“Per-decoder expert placement 还可以继续利用同一统计”之后加一处两段以内条件分支：第一段把历史 decode 请求聚类与 `cluster→group→U_{d,e}` 放置状态和 prefill 成组信号分开；第二段要求同时验收 all-to-all **字节、padding 后通信时间、层时间、请求 SLO**，列校准/刷新/副本未测/隐私与普通布局回退。不得替换现有路由主线，也不得把单篇整理成产品列表。日期、root 写前确认及 Ch56 共享锁前，Books Decision 保持 `待裁决`。
