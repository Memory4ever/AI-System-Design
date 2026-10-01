# 2604.22753v1 → Ch28：非作者实际写后核

本次仅核[官方 exact-v1](https://arxiv.org/html/2604.22753v1) §3–5 与 Appendix E 的必要目标/成本/限制、`books/part-04-training-system/28-pretraining.md` 中“Scaling-law Pilot 也是有预算的实验调度”的实际正文和上下游交接；未复现实验，未审 04/27 的日期/来源/其他家族，不代替整日 Gate。

**主链通过，一句待修，暂不签最终 PASS。** 正文把原先固定 grid 的透明基线保留，并增加候选 run 成本、当前多峰拟合状态、昂贵目标区不确定性的顺序选择；实验 proposal 与真实训练结果、拟合、holdout 的责任没有偷换。与 v1 §3 的有限候选池和异质成本、§4.1–4.4 的 target-region `V_intra + V_inter`/cost acquisition、每轮观测后重估总体相符。作者所谓少量预算效果受其任务、law family、近似 basin posterior 与 cost proxy 限制；正文明确不推出任意 frontier run 的可靠最优规划，也保留后验不可信时的 grid 回退。前接 data-saturation scaling，后接训练 probe 诊断，两侧没有让一个 pilot 分数接管模型质量验收。

同伴定点指出 Ch28 第二句“每一步选择最能减少目标区外推不确定性的下一项实验”单独读会变成纯预期不确定性下降最大化，而论文 §4.2/Algorithm 1 明确用 `(ΔV_intra+ΔV_inter)/c(x)^α` 排序，并须为可负担的剩余候选。建议只将该句改成“每一步在可负担候选中，按目标区预期不确定性下降相对于运行成本惩罚的得分选择下一项实验”。共享 Ch28 由 owner 获锁后修，本文不代改；修后需再实际读一句并签终态。

`semantic-body-binding:SF-2026-ARXIV-2604-22753` 精确包住本项机制段，不吞相邻主题。正文的 versioned experiment state / scheduler 是本书的工程责任表达，不误称作者已部署该平台。此审阅仅限该单篇 source→actual-body；是否归 04/27、日报其他准入和独立日 Gate 仍另验。
