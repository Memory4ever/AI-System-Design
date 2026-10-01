# `2609.24090v1` — 增量 Workflow 的结果复用与提交边界

- 身份与日期：[arXiv 版本页](https://arxiv.org/abs/2609.24090)、[精确 v1 全文](https://arxiv.org/html/2609.24090v1)，访问 2026-09-23；官方 09-22 New 公告落入本窗，09-21 投稿标记不单独证明首发。
- 问题与旧方案：上游输入一变就重算整个 suffix 是易审计的正确性基线；长时任务中某些字段变化不影响已有结果，盲目重算浪费工具调用。
- 机制与所有权：task fact contract 把输入字段/输出字段/等价条件绑定，字段级依赖 mask 与保守的不变域决定哪些结果可续用；变化超出域则最小重算，等价屏障阻止无意义下游传播。执行 Runtime 拥有 dependency/version read certificate，最终有副作用的提交仍必须在最新版本上检查，模型只提出可复用候选。
- 评价边界：三个工业/企业/LLM 工具模拟场景给出作者的组件调用和延迟收益；不证明跨进程事务、网络分区、未知依赖或不可逆外部 side effect 的一致性。保守不变域误设可能错用陈旧结果，未知依赖应回退 suffix 重算。
- Books Decision：`AGENT-WORKFLOW` Ch81 已明确“已知依赖缩小重算、未知依赖扩大失效”和最终 commit 重新核对 revision journal/read certificate，同时保留跨进程与不可逆副作用非证明。本文的字段 mask 和不变域是该原则的实现案例，未改变章节结论，故 `No Change — Existing Coverage`。V2 评分 2 + 1 + 2 = 5/9；独立审阅通过。
