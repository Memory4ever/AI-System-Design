# 2604.22167v1 — Ch66 窄 Books 决策请求

状态：作者提案；**未获 root 写前采用或共享 Ch66 写锁，未计 Integrate**。依据为[官方 exact-v1 HTML §3–4、§6.1–6.2、§9](https://arxiv.org/html/2604.22167v1)、[八项非作者 Existing 审计](V3_EXISTING_INDEPENDENT_AUDIT.md)及当前 [Ch66 Rare Failure Evaluation](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

现文在固定输入 `c` 的随机输出轨迹上，把 proposal 命中率与目标 `Q_risk(c)` 分开，要求逐 token 重权、支持、ESS 与 audit floor；它没有把输入改写分布本身作为另一个分母。原文 §6.1–6.2 对 309 个 StrongREJECT 原问题各做 25 个非对抗改写，观察到语义近邻的 `Q_risk(c)` 可大幅变化，并从给定 query 分布的单输入风险估计推到 n 个输入中最大 `Q_risk(c)` 超过阈值的机会。这是评估身份和采样预算的双层压力，不是多跑同一 prompt 的替代。

建议唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM` Ch66，放在现有 Rare Failure Evaluation 的固定输入重要性重权段后、下一节 Principal Hierarchy 前。可采用的最窄正文：

> 固定输入下把输出尾险估准，仍不能推断一组用户改写或新输入上的风险。稀有失败评估应把输入家族/改写来源与目标解码、harm judge、每输入尾险估计分别版本化：先在每个 `c` 上诊断 proposal 支持、权重尾部和 ESS，再在明确的 `D_query` 与 n、阈值 `τ` 下报告跨输入的风险分布或最大值事件。输入覆盖不足时，不能用更深的单 prompt 重采样补这个缺口；保留独立的 query-family holdout、原模型 audit floor 与 Unknown/发布限制。代价是改写构造、逐输入估计和外部 judge 成本；固定模板且输入变化受控时，原固定输入估计仍是合理局部分支。

边界必须同段或紧邻保留：§6.2 的 30/70 只是同一 309-base-query、7,725 改写池的随机拆分，不是未见 base query 或真实部署 `D_query`；原法需可访问模型权重以构建 unsafe proposal 且 LLM judge 可错。不得采用一般线上发生率/保证、论文效率 headline 或“逐篇部署安全证明”。若 root 认为 Ch66 其它实际位置已具体承载这两个分母，请指出可对照的段落，按 Existing 关闭；不能只因全章谈过输入分布就否定增量。
