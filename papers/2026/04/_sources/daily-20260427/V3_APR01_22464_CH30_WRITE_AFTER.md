# 2604.22464v1 MADE-IT：Ch30 非作者写后核验

结论：**PASS，限本篇实际正文；不是 2026-04-27 日级 Gate。** 书稿由 root 写入，本文核验者 apr01 未参与该两段写作。

- 来源身份：[官方 exact-v1 HTML](https://arxiv.org/html/2604.22464v1) 题名 *Towards Adaptive Continual Model Merging via Manifold-Aware Expert Evolution*，本轮实读 §3.1.1–3.1.3、§3.2.1–3.2.2 与 §4.1–4.5/Table 1–2；[root 写前裁决](V3_ROOT_22464_MADEIT_ADJUDICATION.md)另存。§3.1 把同基座任务模型的模块权重增量作 truncated SVD，以输入/输出子空间投影亲和与适应阈值提出合并或新建；§3.2 用当前中间特征对 expert 输入子空间的匹配选路，由共同任务来源/依赖图约束跨模块路径。这是三项不同责任，不是单个路由分数。
- 实际落点：[TRAIN-LORA Ch30](../../../../../books/part-04-training-system/30-lora.md) 的 Continual VLM expert evolution/task-prototype 段之后、Adaptation Support 段之前，`SF-2026-ARXIV-2604-22464` 两段及章末 Review note。前文任务样本可校准的 learned selector 与本篇无额外 router 训练的输入投影分支构成条件切换；后文回到适配 support 的训练责任，没有把参数几何当功能真值。
- 负边界匹配：正文明确亲和/投影只为 proposal，不能证明标签、安全语义或任务真值；rank、阈值、每层候选扫描与错误路径剪枝均有成本/回退。§4 的证据是 CLIP-ViT B/32、B/16、L/14 在 8/14/20 个连续图像分类任务上的 ACC/BWT，非生成式 MoE、真实在线延迟或生产长期漂移。论文的 data-free/training-free 限额外路由器及合并阶段，不抹去任务模型已有适配、SVD/合并与推理开销。书稿未采用表中胜率作普遍收益。
- 归属日期只作有据组合推断：本家族 receipt 的 v1 Updated `2026-04-27T00:35:19Z`、OAI `2026-04-27`、DOI initial created `2026-04-27T01:38:05Z`，与邻接 ID 批次及官方 Sunday 20 ET 公告/赋号规则合看，支持本窗 08～09 北京时间；`Submitted=2026-04-24T11:35:53Z` 和其它任一元数据均非逐篇 first-public 日志。

据此可把本篇列为 `2+1+2=5`、因真实 Ch30 知识缺口作深入审阅 override、Books **Integrate**，并计入单篇非作者写后通过；不能据此标整日报 Complete。实验未复现。
