# arXiv:2609.23048v1：压缩 VLA 离线通过后的闭环失效

状态：精确 v1 HTML 的方法、受控干预和局限已定点阅读；非作者独立复核判为 **候选前关闭**。论文的高质量单案例证明其数据包在该模拟任务中可恢复策略，却未改变 Ch26 已有的压缩 VLA 闭环验收合同；不评分、不列日报候选、不修改 Books。不能用此笔记宣称整日报完成。

- 身份：[Anatomy of a Closed-Loop Collapse: A Causal Case Study of a Compressed VLA Policy](https://arxiv.org/abs/2609.23048)，[v1 HTML](https://arxiv.org/html/2609.23048v1)。官方 09-22 New 公告批次按时刻表推定 arXiv 首次公开在 09-23 08:00 北京；v1 文件 09-19 字段不是公告时间。当前 abs 为 v1、未见撤回；不推断其他作者渠道不存在更早公开。
- 问题与旧方案：用 held-out offline gripper/direction metric 和 distillation loss 验收压缩 policy 可低成本筛选；但闭环中 action 改变下一个 observation，离线稳定不能推出执行成功。这个 offline–closed-loop gap 本身不是本文新发现，作者明说研究的是一个发生中的受控解剖案例。
- 实验合同：§III 将 Octo-Base-1.5 12 层蒸馏为 8 层 student，在 Open X-Embodiment 混合数据训练 300k step；参数保留 86%，平均推理 135.4→124.9 ms 仅约 1.08×。离线 teacher ratio 为 0.996/1.000。SimplerEnv/ManiSkill2 中模拟 WidowX pick-and-place，72 configurations 是 3 seeds×24 episode IDs；teacher 40/72，student 0/72。阶段性 outcome 记录 moved/grasp/sustained hold/target，不把四个诊断 episode 的 z 残差当所有场景因果证明。
- 受控干预：§IV–VI 依次测试继续训练、更多同任务离线数据、命令级 z offset、z clamp，均未恢复最终完成。最小配对控制从同一 checkpoint 继续训练相同步数、batch、seed、optimizer/loss，把一半 OXE 流量替换为执行环境中的成功 teacher rollouts；held-out 18/36 对 teacher 17/36，对照 0-rollout 分支仍为 0。这个设计支持 **替换数据包作为整体的充分性**，不识别其内 active component；deployment-state coverage、success-only filtering、teacher-consistent labels 与视觉域同时变化，作者 §VII 明确承认。
- 证明边界与 trade-off：单一模型家族、单一任务、单一 simulator，未验证真实机器人；teacher competency 还限制可做的廉价对照任务。闭环 stage probe 与行动 trace 增加运行、instrumentation、checkpoint/环境身份管理成本，但避免把离线误差均值当 release gate。不能把作者观察的 z 残差升格为普遍 VLA failure mode，也不能宣称一半 teacher rollout 是通用修复剂。
- Books 比较与关闭理由：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 第 806–812 行已写压缩容忍度应由闭环 action deviation 判断，第 896 行明确离线 action accuracy 不替代闭环；本文证明的是单一模拟任务中的受限实例，没有新增可迁移的机制或改变现有设计/评价合同。因而在候选前以 `No new project contribution` 关闭，而不是先选中再用 `No Change` 装饰。
