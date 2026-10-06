# 11/14 Sparse circuits 有限证据与 owner 差额 ready

作者 Planck。沿用 [root 首批独立校准](FIRST_INDEPENDENT_REVIEW.md) 的日期与准入，不重复申请同一层校准。本包申请有限命题的 Evidence / owner 独立核验；不是 Books 写后复核，实际 Books 写入为0。

## 原源、日期与采用边界

[官方 Blog](https://openai.com/index/understanding-neural-networks-through-sparse-circuits/) 的实际核心存于 [raw-web-07](raw-web-07.json)，采用 L45–72 所披露的训练设计与局部评价。官方 [RSS raw](raw-openai-rss.xml) 原值 `Thu, 13 Nov 2025 10:00:00 GMT` 对应 BJT 2025-11-13 18:00，落在本窗；root 已核此事件权限。直接 HTML 请求403不作为文章元数据。

当前链接的 [2511.13653v1](https://arxiv.org/abs/2511.13653v1) 是 Nov17 提交的后续原件，身份见 [raw-web-08](raw-web-08.json)。不把该稿倒填为 Nov13 原技术稿。当前采用的是发布方 Blog 中明示的有限命题，未认证博客此后完全未变，也未认证实现或复现实验。

## 方法、评价与反侧

官方 L45–52 将事后分析 dense 网络与训练时迫使大量权重为零区分；这是连接稀疏约束，不是稀疏 activation 分解。L55–63 用手工算法任务和剪枝后任务能否维持来评价 circuit；quote 例子的充分性与删除边失效只针对该任务和干预。L57 的固定规模取舍与扩规模移动前沿是作者局部观察，不是等算力结论。L65、69–72 保留复杂任务解释不全、小模型、训练成本与部署效率限制，不能外推 frontier 可解释性或安全保证。

采用命题：**可解释性可以作为训练表示形成阶段的一条受约束设计轴，而不只作为训练后诊断；它与容量及训练/部署成本共同取舍。** 不采用唯一算法、通用能力提升、稀疏加速或完整安全解释。具体稀疏优化算法、全任务剪枝阈值、matched FLOPs 与误差条均 Not Disclosed 于所用 Blog；本包不依赖这些数值主张。评分沿用 **2+1+2=5**，标准审阅的范围限定于以上命题。

## 实际 owner 对读与建议位置

已实际重读项目 context、学习方法、写作指南、ROADMAP 及 Ch4/5/6 交接。唯一 owner 为 `WORLDVIEW-REPRESENTATION`，[Ch5](../../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。本次对读重点为现有“分布式表示与 Superposition”前两段、“从可读出到机制”证据阶梯，以及工程验证中 basis invariance / sufficiency / necessity 两段；这些是当前 owner 比较，不是本日日期证据。

现有覆盖：容量共享与干扰/解释难度；probe、patching、sparse decomposition 只是局部证据；充分性不等唯一实现。故不建议复制这些成熟原则。具体差额：现有 sparse decomposition 是分析已形成的表示，未在所读段落解释**训练时限制权重连接**这一替代分支及其成本位置。

建议 root 如认可独立证据与长期差额，在 Superposition 第二段之后、现有后训练几何耦合分支之前，融入一个短段：先保留 dense 容量共享的合理性，再引入将连接约束前移的另一目标；紧邻写明能力/解释性局部前沿、稀疏训练成本和简单任务解释不能外推完整模型。不新增章节，不写论文摘要，不因名称缺位要求整合。

作者建议为**整合候选（未落实）**，可独立改判为仅报告或具体已有覆盖。本 lane 无共享 Books ownership；root 协调实际写入及非写入者 POST 后才能在正式报告记整合。可选 Nov13 原技术稿缺失不阻断 Blog 所支持的有限命题；只有采用上述未披露算法/定量细节时才精确重开原稿。

## 请独立核验

1. L45–72 能否支持采用命题，是否仍有超出 Blog 的推断；不要将后续稿件充当历史原件。
2. Ch5 的真实覆盖是否已足够，或训练时连接约束及成本位置是否确有短段差额。
3. 如整合，确认邻接位置与限定语，再由 root 协调共享 Books 写入和非写入者 POST；本包未授任何 Books 完成。
