# A²D Source → TRAIN-GRPO PRE 提案

作者 supplement_20260201。本文为写前提案，保留当时“待root独立核查/尚未改书”的层级，不代表当前待办。2+1+2=5，具体owner gap与公式冲突定点深入；精确v1必要证据及反侧见 [补查§3](./supplement-20261008.md#3-a²d必要证据反侧与stop)。Eq3/5 NLL无log及无正例处置不采用。实际Source/PRE、获准窄写、POST与DAY通过结果见[本日最终停点](./supplement-20261008.md#5-精确停点)，不要从拟文预授实际写入。

现有Ch33 L407–413（POPE/PrefixRL）是人工/外部prefix conditioning与suffix reward-update；L992–1027是demo/skill scaffold退火。它们不拥有“学习一个decomposer、以proxy结果训练、conditional extra exploration的正例以无子问题条件辅助更新”的具体职责。拟插入PrefixRL两段之后、reward-variance selector之前；唯一owner TRAIN-GRPO。Ch32保留policy-gradient/critic基础，Ch34离线chosen/rejected不接管此on-the-fly guided-positive支路。

## 拟正文两段

人工或外部成功prefix不是唯一的探索脚手架来源。一个受限分支从同一backbone另训decomposer：它提出子问题，由固定proxy reasoner在原问题与子问题条件下多次尝试，用“至少一解正确”与格式检查的乘积奖励训练分解策略，再把子问题冻结为离线训练注释。这个reward只评价指定proxy与采样预算下的提示效用，不证明每个子问题真实正确。reasoner仍先在原问题上生成普通rollout；仅在成功率低于阈值时增加带子问题的探索，把选出的正确回答用于不包含子问题的辅助学习，普通outcome RL并未取消。关键差异是分开“探索时使用什么条件”与“参数更新希望保留什么依赖”，而不是把分题文本本身当作必须模仿的答案。<!-- source-family:SF-2026-ARXIV-2602-00759 -->

[A²D的受限对照](https://arxiv.org/html/2602.00759v1)支持在所测数学协议中保留正例选择、提示移除与多样prompt，持续在训练和测试注入同一子问题可能形成脚手架依赖；但去提示测试的表现仍须单独验收，部分任务也低于普通GRPO。decomposer训练、proxy多次验证、离线注释与额外guided rollout都是成本，64条普通rollout对照不等于完整训练预算匹配。v1把辅助loss称作NLL而Eq3/5没有写log，附录算法仅引用这些式子，故此处只采用条件采样与更新责任接口，不把原式当可执行目标或无偏policy-gradient保证。提示不可靠、正例稀少、无提示迁移或预算不合适时，保留原prompt RL、可审计的人工prefix与明确SFT，而不以无外部强teacher推导免费自进化。<!-- source-family:SF-2026-ARXIV-2602-00759 -->

若root批准，受本日写入范围限制请root协调实际Books写者及非作者POST；本作者只维护本日README/_sources，不擅自改共享Books。若判断上述机制已有具体覆盖，请指定承载论点，以已有覆盖结束，不为diff写书。
