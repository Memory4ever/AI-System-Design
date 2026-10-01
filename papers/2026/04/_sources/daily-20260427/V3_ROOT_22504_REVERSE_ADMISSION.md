# 04/27 2604.22504v1 非作者反向准入与日期限定

范围：仅裁决该家族能否从泛化前分母关闭恢复为有条件的候选，并对照当前 Books owner；不签发整日首发、来源或日级 Gate。Primary：[arXiv v1 身份/提交历史](https://arxiv.org/abs/2604.22504v1)、[exact-v1 正文](https://arxiv.org/html/2604.22504v1) §2–4 与 Appendix A。访问：2026-09-28。

## 贡献与旧方案

本篇不是“又一种推荐排序指标”。在**受约束物品词表、单一目标物品、二元 reward**的设置下，它把负候选生成方式与实际优化目标连接起来：随机负样本的 pairwise 比较偏向全局 AUC，beam 给出的高分困难负样本把比较密度推向排序头部；作者提出的 windowed partial AUC 和软阈值重加权则试图指定 Top-K 附近。与 Ch33 现有按 prompt 成败统计重新分配 rollout budget 不同，这里改变的是**同一用户内负物品的 proposal 分布及 surrogate objective**，有一个可迁移的“采样分布并非评价中性”的训练判断。因此旧泛化前关闭理由不成立，建议暂恢复 `Design Delta 2 + System Reach 1 + Durability 2 = 5` 的标准审阅候选。

## 不得外推的边界

论文的等价/相关性结论依赖二元 reward、约束 item 映射和特定 pairwise 推导；有限 beam 只是 top-tail 的近似 proposal，不能说一般 GRPO 必然优化 AUC，也不能说任意 hard negative 就精确等价 OPAUC。WPAUC 与 Recall@K 的等价是**单正例**和指定窗口宽度下的特例；多正例仅作受限模拟相关性。作者四个推荐数据集与 Qwen2.5-0.5B 等实验不证明通用推理 RL、任意检索或生产 SLO 收益，硬负例还可能增加计算、覆盖偏差和 false-negative 压力。

## 日期与 Books

身份页记 v1 submitted `2026-04-24 12:31:57 UTC`，这不是公开时间。arXiv 官方 [announcement schedule](https://github.com/arXiv/arxiv-docs/blob/develop/source/help/availability.md) 规定周四 14:00～周五 14:00 美东收稿批次通常在周日 20:00 美东公告，即北京时间周一 08:00；若该稿未被 moderation/defer，推定可落 04/27 的 `[04/26 09:00,04/27 09:00)` 窗口。**仅 schedule+submitted 不能排除个案延迟**；需作者以官方 announcement/list identity 或相邻 ID/记录组合确认，才可冻结 04/27 owner。

Books 暂不写入。`TRAIN-GRPO` Ch33 已将 group membership、prompt sampling/selection bias、重要性和评价合同分开，但没有把此单正例推荐特例直接写成通用定理的理由。作者完成标准 Source Review 后，若发现可脱离该任务而仍改变 Ch33 既有机制结论的证据，再提窄整合；否则 `Weekly/Report Only — bounded recommendation objective`，不是因“有 ROADMAP 节点”就自动进书稿。

作者应先确认日期、完成论文 Method/推导/实验/限制与关联前后章复核，再更新工作分母与正式报告；本裁决不是 04/27 Complete。
