# 04/22 两项有界非作者反向准入裁决

本记录只裁定 `2604.19457v1` 与 `2604.18660v1` 是否应进入贡献候选分母；不是这两项的落窗证明，也不是 04/22 来源、否定侧或整日 Gate。根据官方 exact-v1 与当前 Books 具体 owner 比较，不用题目相关性替代长期增量。

## 2604.19457v1：合成企业 Agent 四轴评测

- Primary：[exact-v1](https://arxiv.org/html/2604.19457v1) §3–4、§6–7、§9。论文把 factual precision、reasoning coherence、compliance reconstruction、calibrated abstention 分开；两个合成 regulated decision 域、有限案例和同系列 judge 支撑其受限比较。不能由此证明四轴在真实企业全部充分，也不能把合成任务排序外推为通用记忆架构优劣。
- 现有 owner：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已区分外部 policy/合规 reference、真实 process/outcome、条件质量与固定分母、commit/abstain 和独立 judge；Agent memory 的事实保存与提交权也已有相邻交接。论文的四个名称使局部应用评测更可操作，但没有改变这些现有责任边界或提供当前书稿缺失的可迁移系统机制。
- **独立处置：具名 pre-denominator closure。** 不继承作者原定的 `5 / Standard / Weekly Only` 作最终评分；这是“已有长期原则下的合成应用实例”，不是因领域名而排斥，也不是材料受阻。保留本记录与原始 evidence；若后续独立真实部署显示现有 EvalSpec 无法表达某条不可替代轴，再重开 owner 判断。

## 2604.18660v1：教育 Tutor 答案泄漏

- Primary：[exact-v1](https://arxiv.org/html/2604.18660v1) §3、§5 与 Appendix D/F。Tutor、Student adversary、leak judge 分开；论文自己报告 in-context 攻击者可能先解出答案，故学生给出正确答案不能直接计为 Tutor 泄漏。受限 fine-tuned attacker、模型和题目改变测得强度，不能把某一 attack success rate 当普遍 tutor 安全率。
- 现有 owner：`PLATFORM-EVALUATION-SYSTEM` Ch66 的实际 trace/response/judge 分母与 [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 的 secret identity、攻击预算和泄漏判定已经要求区分攻击者自身知识、受测系统披露与 judge 事件。本文给出教育任务的有用具体检验，但教育答案保密是该应用的目标，不产生新的平台级 state/data/control owner 或修正书稿结论。
- **独立处置：具名 pre-denominator closure。** 不机械保留原候选评分；不是说泄漏无关 AI System，而是当前具体论文没有超出现有长期安全/评估合同。若后续发现跨任务可复现、并迫使现有泄漏分母改变的机制证据，可重新评估。

两项均不进入 Books，不以 `No Change — Existing Coverage` 冒充已入候选后的完整 Source Review。作者侧应回填 04/22 工作 ledger 与正式报告的计数/理由，并另行完成日期及整日 Gate；本记录不授权将 Daily 标记 Complete。
