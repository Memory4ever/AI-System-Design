# 04/27 root 写入的非作者有限写后核验

核验者 apr01（不是下列正文的写入者）。本轮只对 6 项新写入与 3 项定点修正的官方 exact-v1 必要方法/评价、实际书稿正文、相邻交接和 source-family 边界做有限检查；未复现实验，也未复核 14 来源、完整候选分母或整日 Gate。下列 PASS 只对所列实际正文有效。

| 家族与主来源 | 实际正文与邻接 | 有界裁决 |
| --- | --- | --- |
| [2604.22291v1](https://arxiv.org/html/2604.22291v1) Train in Vain，§2–5、Table 2–3、Limitations | [Ch27](../../../../../books/part-04-training-system/27-data.md)“代码可运行不等于它适合训练代码模型”在旧代码语料过滤后、Synthetic Data 前。 | **PASS。** 功能保持与 next-token 监督效用分账是真增量；dead-branch 同模板 `.38` 对 poisoned `.20` 只作为 Java/CodeLLM 微调受限反证。正文未写攻击步骤或把污染当数据权利通用方案，canary/lineage 为工程准入判断而非作者证明的完备防御。 |
| [2604.22127v1](https://arxiv.org/html/2604.22127v1) hybrid LoRA，§3–4/7 | [Ch30](../../../../../books/part-04-training-system/30-lora.md) placement 层位主线之后、初始梯度 proposal 之前。 | **PASS。** target module 的组件类型与串/并行挂载身份超出原层位选择；同 rank 不同参数/成本、两 sub-1B 家族、单 seed、部分 CI 跨零和 full-stack 回退均在正文，没有把 attention-only 写成普适最优。 |
| [2604.22509v1](https://arxiv.org/html/2604.22509v1) LaissezCloud，§2.3/4–5/7 | [Ch63](../../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md) quota/fairness 后、GPU sharing 前。 | **PASS。** 租户私有效用 proposal 与运营方物理仲裁分权、软价格与硬安全共存、迁移/重配置成本和固定 quota 回退均准确；8–23% 明确限定 trace/profile 模拟，不称云上生产 SLO 或 incentive/privacy 保证。 |
| [2604.22167v1](https://arxiv.org/html/2604.22167v1) Tail Risks，§3–4/6.1–6.2 | [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 原固定 prompt importance-sampling 尾险后。 | **PASS。** 固定 `c` 输出风险与 `D_query` 输入家族分母分开；同一 309 base questions 的 25 改写在同一池内随机 30/70，不当作 unseen base question 或部署发生率。逐输入 proposal/weight/judge 成本、Unknown/fixed-template 旧路正确。 |
| [2604.22438v1](https://arxiv.org/html/2604.22438v1) SSG，§4–5 | [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 多 bit CDF 水印之后。 | **PASS。** 单 bit keyed 分组等词数不等概率质量的低熵失效不同于现有多 bit 容量论点；正文清楚分开全词表理论与 top-k 实现、排序开销、反向质量切片和来源证明边界。 |
| [2604.22550v1](https://arxiv.org/html/2604.22550v1) ArmSSL，§III–VI | [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) extraction/watermark 归属接口段。 | **PASS。** embedding 与下游 confidence API 的 probe 身份、OOD 密簇可反向移除均承载；黑盒验证非作者首创，主对照冻结 encoder、有限负例与自适应移除反证清楚。没有把统计水印当法律权属或任意 FT 保证。 |
| [2604.22228v1](https://arxiv.org/html/2604.22228v1) multipath/Graph，§4–5 | [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md) P2P 两段被专属 start/end 绑定，end 位于后续 NIMBLE 之前。 | **修后 PASS。** payload 分路与 host launch replay 两个收益分账、双向 host path/小消息反例与四 GPU OMB 范围正确；source marker 不再越界包入另一篇 collective。 |
| [2604.22312v1](https://arxiv.org/html/2604.22312v1) GVR Top-K，§4.1–4.2/6 | [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md) Exact Top-K 段专属 start/end。 | **修后 PASS。** 现在正确写成在 `K≤f(T)≤C` 时正常 Verify 后 refine 至恰好 K；不能满足容量条件才 fallback，不再把正常 refine 说成验证失败。Blackwell/SMEM/时序相关限制保留。 |
| [2604.22753v1](https://arxiv.org/html/2604.22753v1) scaling pilot，§3–5/Alg.1 | [Ch28](../../../../../books/part-04-training-system/28-pretraining.md) pilot 段专属 start/end。 | **修后 PASS。** 当前正文已经写入成本折减选择而非绝对降幅最大；对应源式为 `(ΔV_intra+ΔV_inter)/c(x)^α`。候选可负担、后验/holdout、固定网格回退及非任意大模型外推齐备。 |

本次书稿正文明显与原主张同向，但 PASS 不等于来源窗口完整、候选冻结、实现复现或 04/27 日级验收。报告中可将这 9 项的各自“待写后”状态改为真实非作者通过；其余普通项和来源限制必须另审。
