# 2026-04-30 Books 写前最小采用包：26052 / 26180（作者提案，未获锁）

仅供 root 非作者 `exact-v1 → Ch66 actual owner` 裁决；共享 Ch66 尚有其它日期 writer，本文件不授权、不修改 Books，也不把未冻结的候选计为已整合。

## 2604.26052v1 Prompt→Response Risk

- 必要来源：[官方 exact-v1 §3–4](https://arxiv.org/html/2604.26052v1)。人类对每条 prompt 与对应 response **独立**标同一四类别、四级风险，再看成对方向变化、条件 persistence/de-escalation 和 response relevance。它测输入本来多危险以及输出是否增减风险，不是单看输出 harmful rate。
- [Ch66 risk-tier/refusal 段](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)已要求 matched framing、benign/borderline/dual-use、partial compliance、judge identity；但没有同一输入—输出两端**独立标记后保留方向性 transition 分母**。若采用，唯一 owner 为这段的 EvalSpec，而不是训练安全能力或 Ch72 effect gate。
- 拟窄正文：`输出风险不能脱离输入风险解释：同一输出等级可能是把原本高危请求降级后的残余，也可能是从无害请求引入的新危害。评价时应在同一 prompt–response pair 上分别冻结输入与输出的风险类别/严重度标签，再按输入切片报告 persistence、de-escalation 和升级，并把响应是否相关单列；只报输出 harmful rate 或总拒答率会抹掉风险变化的方向。`
- 紧接边界：`输入风险标签是评估注释，不是用户真实意图。作者 §3 的 per-category drift-up 分母是“响应同类有害”条件下回看 prompt 无害的比例，不能倒写成给定无害 prompt 后响应有害的前瞻概率；后者须从原始配对表重算。原数据仅 1,250 条单轮英文，GPT-5.1 与 GPT-4 prompt 不配对，不能由两模型百分比推出因果安全差；新增双端人工标注及歧义调解也有成本。`
- 决定点：若 Ch66 当前其它段已经具体保存 paired input/output 风险 transition，应判 Existing；不能因为已有 risk-tier 字样就机械认为方向分母已覆盖。

## 2604.26180v1 Evergreen

- 必要来源：[官方 exact-v1 §2–6](https://arxiv.org/html/2604.26180v1)。表格上的 semantic aggregate claim 先按 existential/universal/cardinal/proportional/ordinal/nested 类型编译 `filter/map/aggregate/rank/check`，昂贵语义 predicate 留给 LLM，量词和分组交查询引擎；existential 找 witness 即停，universal 找 counterexample 即停，count/proportion 可由剩余 tuple 上界停。采样 confidence sequence 与确定性决定证据须分开。
- [Ch66 claim graph/provenance 段](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)已有 typed claim→supporting artifact/source region→verifier outcome；但未明确**关系聚合 claim 的量词类型决定执行计划、停止条件与最小 tuple lineage**。Ch75/76 只提供 query 与检索，不拥有最终 claim 的真值；建议插在 typed claim graph 之后、已有发布与 lineage 代价之前。
- 拟窄正文：`Claim graph 进一步遇到关系表的 aggregate 声明时，验证单位不能仍是一个文本片段。存在断言只需一条满足条件的 tuple 作 witness，全称断言一条反例便足以否定；计数、比例、排序和嵌套断言则需保留 filter、分组与比较规则，并可在未读 tuple 的上下界已无法翻转结果时提前结束。EvalSpec 应将量词类型编译为查询/停止规则，语义 predicate 可以由模型提议，但最终裁决须回到可重算的 tuple lineage 和查询版本。`
- 紧接边界：`这种编译要支付 schema 绑定、语义谓词调用与 lineage 保存成本；抽样置信序列只给条件性统计判断，不能冒充完整关系证明。作者只在 Yelp 三个子集共 16 条人工检查 claim 上验证编译，参考真值是强 LLM 多数票；其中一个 grounded universal claim 被假反例误判，故不能宣称任何聚合 claim 都已被形式化验证。关系数据不足、开放世界证据缺失或 verifier 无法校准时，应维持 Unknown 与人工/外部判定。`
- 决定点：若当前 Ch66 已把量词类型直接连接到关系查询终止和 tuple lineage，判 Existing；否则只在此处纳入，勿把查询执行细节重复写入 Ch75/76。
