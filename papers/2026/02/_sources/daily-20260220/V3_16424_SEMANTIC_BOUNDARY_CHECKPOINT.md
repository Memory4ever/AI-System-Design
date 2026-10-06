# 02/20 单篇 checkpoint：Verifiable Semantics 的采用边界

**检查时间：** 2026-10-05T16:56:20+08:00
**范围：** 仅 `2602.16424v1`；供当前作者复用，正式当日状态未更改。
**执行者：** `historical_checkpoint`；最终单篇处置待 root 独立回核，不授整日 Gate。

## 1. 恢复依据与实际阅读

本日默认窗口为 2026-02-19T09:00:00+08:00 ～ 2026-02-20T09:00:00+08:00。本轮不重新发现、扩候选或重核日期，沿用[第十八包停点](V3_EVIDENCE_EIGHTEENTH.md)的本篇身份、准入与已读 core：完整摘要、认证算法尾、Theorem 1、Definition 5 / Proposition 1、漂移/再认证/再协商及模拟。其中心疑问仍有效；不以方法已读授正面 Evidence。

本轮新增实际阅读是[保存的 exact-v1 原源](V3_REVIEW_2602.16424v1.html) §5.3 `S5.SS3`、§6.1 `S6.SS1`，并读具体 owner 的正文及连接层交接。精确定位沿用本日抽取方式：`V3_extract_html.py < V3_REVIEW_2602.16424v1.html | awk 'NF' | nl -ba`；§5.3 为 198–213，§6.1 为 218–224。没有重读完整附件、比较 v2、读统计论文或代码，也未复现实验。

轻量核验[官方 v1 事件页](https://arxiv.org/abs/2602.16424v1)：标题、作者和 v1 身份一致；页面显示 v1 提交字段 `Wed, 18 Feb 2026 12:55:58 UTC`、另有 3 月 v2，不把提交时刻当首公开时刻，也不借 v2 回填本窗。当前可见页无撤回/纠错告示；未遍历完整版本史。

## 2. 实际 LLM 协议支持什么

[原文 §5.3](https://arxiv.org/html/2602.16424v1#S5.SS3)，抽取 200–213：作者在 toy content moderation 中使用同一个 Qwen2.5-3B-Instruct 的两个 LoRA adapters；各以 150 例、不同 label distributions 人为诱导 divergent policies。词汇只有六项（harmful、misleading、sensitive、spam、benign、escalate）；300 场景分 120 audit / 180 held-out，但实际 core-guarding 只测试 50 held-out events，阈值为 τ=0.06。

两项通过认证：benign 的作者 contradiction 为 0%，sensitive 为 2%。Table 2 报告 unguarded 六词 disagreement 5.3%，core-guarded 两词 2.6%；这是作者局部协议的描述性结果。它支持共享事件审计能够筛出一个更小的经验一致词汇，并在该 toy 设置下观察到较低 disagreement；不是不同基础模型、开放协作任务、所有 180 held-out 场景或安全关键部署的证明。§5.3 未给这两个百分比的原始 numerator/denominator、重复运行/不确定性，也未披露训练硬件、precision 或端到端审计/限制词汇成本；不把它们补造为已核事实，不将 51% 相对下降作为普遍收益。

实际取舍是表达覆盖由六词缩为两词；对受限词项的一致性改善并未测定被排除语义需求的任务损失。不能由删除不一致词项的局部结果，授予任意后续决策规则相同结论或 truth / authorization 保证。

## 3. 直接反侧与中心隔离

[原文 §6.1](https://arxiv.org/html/2602.16424v1#S6.SS1)，抽取 221–224，直接承认：认证粒度是单词项而非 composition/context-dependent meaning；“high”和“risk”分别通过不证明“high-risk”一致，适用性依赖事件采样覆盖有关 context。协议目前是 pairwise，未解决多 Agent 的 transitivity/scaling；renegotiation 只是 sketch / entrenchment heuristic。协议还假定 certification verdict 忠实反映 dispositions；作者关于当前架构难以多步欺骗的讨论不是本轮已验证的 adversarial guarantee。

因此补读没有消除第十八包已记录的中心问题：

- Definition 5 / Proposition 1（已读 core 抽取 143–151）从只使用 certified core 推出决策相同，但仅相同词项值不足以约束两个不同 decision rules。作为本轮逻辑反例，同一 core term 的值完全一致时，一方输出该值、另一方输出其取反，两者都只咨询 core，却总作相反决定；这不是作者实验结果，也不替作者改写定理。多词项联合使用还需要明确的联合失败/组合条件，原 v1 采用链未给足。
- Theorem 1（已读 core 抽取 140–142）把 Wilson interval 用于所称 finite-sample 保证；旧停点与 root 原源核查已指出其 coverage / bound-probability 表述问题。本轮不引入外部统计证明，也不把经验 Wilson threshold 重新包装成 exact 保证。

**建议本篇中心处置：争议 → 暂缓，作为本窗终态保留项隔离；窄方法与 toy 观察仅报告。** 保留准入和全部有效旧证据，不改判整篇无贡献，也不把安全名称或 term agreement 当 world truth。该隔离不能支持正面 Evidence / Books 或 Coverage 零遗漏；本轮没有必要继续展开无关附件。

精确重开条件仅为作者提供针对上述桥接的修正证明/明确条件：决策规则及实际执行约束如何共享、对多词项/组合失败如何界定，以及统计 coverage 的正确命题和适用假设。回到 v1 Theorem 1、Definition 5 / Proposition 1 及相关修正说明核对，不自动比较全部旧新版。若未来要采用局部 LLM 收益，另需能解释 Table 2 原始计数/评价单位与 core-guard 的执行规则；这不阻塞当前的安全暂缓建议。

## 4. 实际 owner 与最小处置

`ROADMAP.md` 的唯一 owner 为 **`AGENT-MULTI-AGENT` / Ch82**：[Multi-Agent](../../../../../books/part-07-agent/82-multi-agent.md)。增量问题是两个 Agent 如何建立可消费的共同语义及限定 consequent decisions，不是 MCP/A2A 的 transport、对象或生命周期规范。

已实际比较的正文位置：Ch82 352–362（显式 state owner / commit；状态机不证明语义误解被消除）、565–596（inconsistent world models、consensus without evidence、malicious peer 与失败分账）、630–642（内部共识/外部 truth 分离）、669–680（局部答案组合前需核联合状态，最终 decision owner 仍决定消费）。这些承载一般的语义/共识不等于状态与真值边界，但**不等同于已经覆盖本篇统计词汇认证机制**，不能仅凭主题相似授“已有覆盖”。

连接层交接核对 [Ch83](../../../../../books/part-07-agent/83-mcp.md) 241–259：其只拥有连接与对象映射，委派与证据回到 Ch82，真实批准/提交不由远端状态授予。故无需新 Structural Candidate，也不将本篇移入 Ch83。

最小处置为保留本单篇 checkpoint 给当前 02/20 作者；中心保证不入 Books，本轮无正文写回。只有修正证据可支撑该独特认证链时，才由实际 owner 进一步判断窄整合；不把一般已覆盖原则冒充本篇完整采纳。

## 5. 权限与验收边界

root 当前活跃 agent 树未见 02/20 作者，但这不是跨聊天 ownership 排他证明。本轮只新增本文件；没有解除或改动任何其他线程锁，没有覆盖旧停点或日级状态。运行前 README、Ch82/83 及原源均已有他人修改，全部保留。

实际审阅级别为**中心命题的深入定点审阅**（有效 core 复用＋LLM 协议/直接限制＋actual owner 比较），不是全文/代码复现，亦非已授正面 Evidence Gate。README、Books、LEARNING_STATE、共享索引与汇总计数均未改；不 stage、commit、push。该单项建议仍由 root 独立回核，02/20 整日报告保持原状态。

root 后续实际核验原源抽取 100–225 及以上 owner 正文，单篇独立复核通过；只接受本单篇隔离建议，不授整日 Gate 或变更月度完成数。
