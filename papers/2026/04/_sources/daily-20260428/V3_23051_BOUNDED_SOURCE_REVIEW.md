# 2604.23051v1 对话时间作用域：有界证据与 Ch66 owner 对读

固定窗口 `[2026-04-27 09:00, 2026-04-28 09:00) +08:00`。继[作者侧贡献对读](./V3_23051_NECESSARY_CONTRIBUTION.md)，重开[官方 exact-v1](https://arxiv.org/html/2604.23051v1) §3.1–3.4、§4.1、§5 Tables 3–4、§8，顺读 [Ch66 Longitudinal State](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的事实有效期、as-of 查询及 memory write/read/answer 分账。此页仅完成必要 source→owner 提案：日期尚待非作者本窗确认，不入正式分母/评分/Books，不修改 Ch66（当前另有共享锁）。

论文的 1,469,628 条链以 Wikidata 有效期事实和模板合成，首轮显式设时间锚，后轮可隐式继承、显式覆盖或跨实体沿用。同题的 **Gold Context** 把前轮 assistant 答案替换成正确答案，**Self-Conditioned** 使用模型自己前轮答案，**Questions Only** 移除历史。这三个分母不等同于 Ch66 的 memory store `full-history/no-memory`：即便 store 的事实和 as-of 时间正确，模型仍可能把对话中已定的时间作用域错绑到后续问题。真正可补的评价对象是 `fact-validity × conversation-scope transition × answer`，让 carryover/override/cross-entity 与自生成历史错误传播分别计账，而不是再写一个“长期记忆会漂移”段。

§5 Table 3 在受测模型显示 Gold Context 的 chain accuracy 远低于 final-turn accuracy，Self-Conditioned 的 chain accuracy 更低；正确终轮不代表全链作用域正确。Table 4 按链长列终轮准确度，但不同长度的题组并不保证同难度，因此长度曲线不可直接作同一链的因果退化估计。`Drift` 只在历史/2025 当前值可区分时测“错答匹配当前值”，不是内部检索机制真值；论文的“larger model/current prior 导致 drift”是观察性解释，不可由模型横向差直接归因。§8 限于实体中心 Wikidata、英文固定模板和版本化当前值，不代表自由叙事/真实生产 Agent；Gold 历史是 oracle，不是线上可得状态。

若本窗日期和贡献准入获非作者确认，可暂拟 `Design 2 + System 1 + Duration 2 = 5`、因 Ch66 的真实评价分母缺口按 Books-gap 路由深入必要审阅。拟在 Ch66 当前 Longitudinal State 的 fact ledger/as-of query 后窄加：同一事实库下再控制 conversation scope 的继承、覆盖及跨实体转移，Gold/Self/Questions 三条件分开报告 turn/chain/final 和有效期内的 present-match drift；同时写明模板/当前 snapshot、oracle 与额外三条件调用成本，保留现有 write/read audit 和无历史基线。Ch77 只交接时间事实/记忆写入，不成为这篇的主 owner。日期、root 写前裁决及 Ch66 锁前，本项 Books Decision 仍为 `待裁决`。
