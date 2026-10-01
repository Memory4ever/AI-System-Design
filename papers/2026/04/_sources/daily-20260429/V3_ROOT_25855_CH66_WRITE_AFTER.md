# 2604.25855v1 SIEVES：Ch66 实际写后独立复核

复核者：root，非书稿写入者。此项只验收该 Source Family 的实际正文，不代替 04/29 整日报 Gate。

- 来源：重新核对[官方 exact-v1 HTML](https://arxiv.org/html/2604.25855v1) §3.2、§4.1–4.3、Tables 2–3、Appendix 0.A；作者侧逐项证据见 [限定审阅](./V3_SIEVES_25855_BOUNDED_REVIEW.md)。reasoner 的 zoom-in crop 是可见轨迹；selector 的 correctness、localization、coherence 目标并不都是同一种真值，后两项依赖框/伪标签。`C@r` 在目标测试真值上回选阈值，不能成为未来流量的风险保证。
- 实际 owner：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。书稿在内部 hidden-state probe 及不可得时的回退之后，新增可见视觉轨迹分支；后文继续讨论跨模型 probe 与其它风险传感器。顺读前后段没有把 crop 机制误写成模型内部可访问能力，也没有把定位、证据—答案连贯性合并为正确率。
- 采用边界：正文把这个分支限制在能暴露可靠 crop 轨迹的黑盒视觉 reasoner，并写明框标注、伪标签、额外推理与跨 reasoner 协议成本；保留原图/多样本/人工回退。第二段明确独立部署切片校准与同集回选 `coverage at risk` 的区别。未采用单一权重、三 head 的普遍必要性、论文倍率或生产风险保证。
- 检查结果：实际正文、相邻段落与章末 Review note 一致；无超出原文的系统保证。该 Source Family 的 Books 写后 Gate **通过**。首公开日期、其他候选、全来源和整日 Gate 均仍未完成，不能据此把 04/29 标为 Complete。
