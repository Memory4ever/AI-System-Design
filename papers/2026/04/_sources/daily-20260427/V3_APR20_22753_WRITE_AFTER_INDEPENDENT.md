# 2604.22753v1 → Ch28 有界非作者写后核

- 审阅人：apr20_resume；作者：apr01。范围仅为 [官方 exact-v1 HTML](https://arxiv.org/html/2604.22753v1) §3–5/Appendix E、[Ch28](../../../../../books/part-04-training-system/28-pretraining.md) 当前 `Scaling-law Pilot 也是有预算的实验调度` 及前后相邻段、章末 `SF-2026-ARXIV-2604-22753` Review note；未读全附件、未复现实验、未签 04/27 日级 Gate。
- 原文必要命题：§3 的有限未观测候选池、异质 `c(x)`、有预算的逐次观测与高成本目标区；§4.1–4.4 以多 basin 局部高斯近似，将目标区预测不确定性拆成 basin 内/间两项，按 `S(x) = [ΔV_intra(x)+ΔV_inter(x)] / c(x)^α` 排序、执行后重拟合。§5 的 8 tasks/65 instances/有限候选池与代理成本支持受限预算—外推对照，而非真实 frontier 训练规划保证。Appendix E 明言 mixture 近似、一步 acquisition、有限 law family/候选池、简化成本 proxy。官方 v1 的近邻表还存在一些任务/预算上 V-opt 优于作者方法，因此不写成逐点占优。
- 当前 Ch28 有真实正文而非仅 marker：先承认固定 grid 在便宜/近域时合理，再写 versioned experiment state、proposal 与训练结果/holdout 的权责、后验与成本 proxy 限制和 grid fallback；其前是数据受限 scaling，其后是训练 probe 诊断，段落边界清楚。`semantic-body-binding` 的 start/end 只包这两段，章末 Review note 明确 Experimental 和外推限制。
- **裁决：需一处最窄修正后 PASS，当前不计写后通过。** 正文“每一步选择最能减少目标区外推不确定性的下一项实验”遗漏该论文中心的 `c(x)^α` 成本归一；仅在段首说 run 成本不同、段尾说成本 proxy，不足以让选择准则与官方 v1 完全一致。建议改为“每一步按目标区外推不确定性的预期下降量与候选成本惩罚的比值，选择下一项可负担实验”，或等价表述，并保留现有 one-step/mixture/cost-proxy/holdout/fallback 边界。这里是文义校准，不要求引入公式、数值或整节重写。
- 本核未改 Ch28、04/27 Report 或共享 Books；待作者最窄改文后须对真实句子再作写后确认。`Status: Experimental` 不等于该日 Integrate Gate。
