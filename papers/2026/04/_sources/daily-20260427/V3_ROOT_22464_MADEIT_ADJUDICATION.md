# 04/27 MADE-IT：泛化关闭理由的定点独立裁决

复核者：root；日报作者：apr01。只裁 `2604.22464v1` 的贡献准入、必要原文与 Ch30 写前采用，不替代本日 158 项题摘审计或整日 Gate。

[官方 exact-v1](https://arxiv.org/html/2604.22464v1) §2.2–3.2 的问题不只是视觉分类准确率：连续任务模型到达时，不受控地每任务增加 expert 会线性膨胀；训练显式 gate 又需要持续任务数据。§3.1 对同一基座的模块权重增量作截断 SVD，用输入/输出主子空间投影重叠提出合并或创建；§3.2 用当前中间特征对 expert 输入子空间的投影匹配选起点，再按共同 task-origin 依赖限制跨层路径。它确实提供了“没有额外 task data 训练 router 时，谁提出 expert 复用与输入时选择”的替代合同，不是泛化的局部视觉 recipe。

[Ch30 当前相邻论证](../../../../../books/part-04-training-system/30-lora.md)已有 expert evolution 与版本化 task-prototype sparse selector，却未明确这种无额外路由训练的数据约束及权重子空间、输入特征与跨层身份的三段责任。原有 task-prototype 分支仍在可获取校准数据时成立。本文证据限于 CLIP-ViT B/32、B/16、L/14 的连续 8/14/20-task 图像分类模型流，报告 ACC/BWT；不能推生成式 MoE、真实 serving latency、任意任务语义或持续漂移。作者的“data-free/training-free”只适用于额外 router，不是任务模型、SVD、合并或推理选择零成本；子空间相似度也不是功能等价证明。

裁决：撤销旧泛化前关闭，恢复为 **Design Delta 2 + System Reach 1 + Durability 2 = 5，标准候选**。具体 Ch30 知识缺口触发必要 Books Decision：以旧 task-prototype 条件→新无额外路由数据约束→子空间演化/输入投影/路径一致性→验证代价与旧方案共存写入正文。root 已完成写前 source→owner 并实际修改 Ch30；还须由非书稿作者对真实文字及相邻交接写后核，未通过前不得在 04/27 计为已完成整合。日期仅依作者已有官方公告/ID/OAI 与相邻批次的联合范围，不在此文件独立签署本日 08–09 时段。
