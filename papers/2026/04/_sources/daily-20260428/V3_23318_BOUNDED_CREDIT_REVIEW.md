# 2604.23318v1：Hidden-state span credit 的有界贡献复核

本页只处理 04/28 工作池中的一个既有开放身份，不把工作池变成候选分母。固定窗口为北京时间 `[2026-04-27 09:00, 2026-04-28 09:00)`；v1 提交于 04/25T14:11:23Z，不能将该字段当首次公开。既存官方 receipt 记录 v1 `Updated=2026-04-28T00:32:47Z`、当前 OAI datestamp `2026-04-28`，两者与公告槽/连续 ID 相容但各自不证明逐篇首发。正式落窗、评分和 Books Decision 待独立 Gate。

## 决定贡献的原文与实际 owner

[官方 exact-v1](https://arxiv.org/html/2604.23318v1) §2 在同题八条 rollout 中只保留正误混合的题，截断前缀后分别估计 16 次续答成功率与最近 100 token 隐藏态分布的 Wasserstein 距离；诊断排除含最终答案的 span，但仍是模型自身表征与后续成功的相关性，而非逐步真值。§3.2–3.3/Algorithm 1 以正确/错误 outcome 分组，对每个 span 取到反方任意 span 的最小 Sinkhorn 近似距离，再以重叠 span 的最大值形成 token 权重，乘原 GRPO rollout advantage；没有反方组时回退原更新。它保留正负 advantage 的方向，却改变 token 与 rollout 的梯度总量，不能称守恒的 credit 分解。

§4 的分离只在预/后分叉同分布与不同分布、隐藏态有界、有限样本集中且 population gap 大于噪声等条件下成立；定理讲的是分布距离排序，不是隐藏态已经识别错误 token 的因果位置。§5.4.2 的 per-rollout normalization 消融虽仍胜 GRPO，默认全组归一还携带额外 cross-rollout magnitude 效果；两者不能混称纯 token-credit 效果。§5.2–5.3 采用各 seed 多 checkpoint 的**best-observed** 五数学/五代码 benchmark 平均分，PRM 对照只在数学任务；§6 报三配置训练时间比 GRPO 增约 15.5%、10.4%、7.4%，不是没有额外计算，也不是同总训练预算下的普遍 PRM 优势。

[Ch33 Sequence Reward 怎样作用到 Tokens](../../../../../books/part-04-training-system/33-grpo.md) 当前已写 outcome 广播、可解析字段 credit、首错边界监督、entropy/token proxy 与环境/验证者权责。它尚未承载“**在只有 outcome 标签、同题正误混合的条件下，以 policy 自身 hidden-state span 的跨组分布差异作局部 credit proposal**”这一传感器分支；它与字段 verifier 或外部 PRM 的证据 owner 不同，也不能取代它们。若非作者确认此分支改变本章长期选择，可在 Sequence Reward 广播与显式过程信号之间窄加条件分支，并就近写正误混合要求、Sinkhorn/跨 rollout 成本、相关性非因果与 outcome verifier 的最终权威；短回答或无正误混合仍回退原 GRPO。Ch66 只负责 outcome/verifier 校准，不重复成为训练 credit owner。

作者侧结论：贡献线索成立，**待非作者 source→实际 owner 及日期核后**决定是否进入正式候选/评分；当前不申请 Ch33 写锁、不预记 Integrate。旧 receipt 的 `deep_complete/No Change` 不能替代当前合同的 exact-v1→实际正文对读。
