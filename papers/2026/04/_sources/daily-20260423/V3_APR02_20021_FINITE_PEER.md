# 2604.20021v1 有界非作者复核

范围：只核 [官方 exact-v1](https://arxiv.org/html/2604.20021v1) §2、§5.2–5.3、§6 与本日 [作者证据记录](./V3_EVIDENCE_REVIEW.md)的准入/证明/成本裁决，并对读当前 Ch62 Gateway 和 Ch70 Cost 的相关长期命题。日期只复用本日 `V3_ROOT_OAI_DATE_BOUNDARY` 的官方 OAI/公告槽组合记录；`submitted`、OAI 或 DOI 均不单独证明首次公开。未复现实验、未核整日来源或 Gate，不改作者正式日报/Books。

## 必要原文与准入

§2 将查询置于连续 embedding 空间，用 ε-net/Voronoi 动态离散；命中旧回答的代价以与 query 距离单调的有界 `φ(d)` 表示，向模型请求才观察到成本。§5.2 在部分反馈下以 KRR 共享附近成本信息，按 lower-confidence cost 和低频切换控制 cache。这是从有限离散 key/cost 扩展到连续到达、可观测性与切换成本的实际系统机制，不能按普通相似度缓存或标题映射前关闭。作者拟 `Design Delta 2 + System Reach 2 + Durability 1 = 5`、标准审阅准入成立；中心保证出现精确反证信号，按合同定点深入而非机械提分。

## 中心保证隔离

§5.3 Assumption 2 约束高概率到达区域的有效中心数 `m_eff` 为常数，Theorem 5.1 显示的上界另含 `k·m_max·loglog T` 切换项。Lemma 5.3 把 `m_max` 定为整个紧查询空间在 ε 半径的最大覆盖数，上界 `(D√d_e/ε)^d_e`；作者同节又承认 ε 按 `T^{-1/2}` 缩小时，最坏情况 `m_max` 可为 `O(T^{d_e/2})`。现有显示假设没有将该项压回 `O(√T)`，因此从展示的式子不能直接得其不加条件的 `~O(√T)` 句。可能需要额外的 `m_max` 增长约束或更紧的只计有效中心切换证明；此处是**证明桥缺口的独立推论**，并非声称已证实整个算法发散、或作者承认错误。

§6 用 50 个合成 prompt，另将 Natural Questions 与 TriviaQA 各 2500 条组成流；384 维 sentence-transformer embedding，LLM 成本由 GPT-2 tokenizer 长度 min-max 归一化代替。在线最终平均 regret 及 runtime 只对应这些 cost/mismatch proxy；没有输出正确性、真实模型服务成本、硬件/精度/并发、cache 跨租户授权或生产 SLO 证据。`mismatch φ(d)` 也不是事实等价/安全接受规则。相对离散/贪心 baseline 的局部收益保留为经验观察，不用作实际节费百分比。

## 实际 owner 与终态建议

Ch62 Gateway 当前有 tenant/model/API 身份、预算与 admission 权限；Ch70 Cost 区分 token/缓存命中代理、硬件与 SLO 实测。本文动态中心+KRR+切换的局部设计值得本日报保留，但不能把其代理相似度接成 Gateway 的答案提交权，亦不能把模拟 regret 接成 Cost 的真实费率/时延保证。当前**5 分，证据深入纠错，`Disputed / no Books` 的有界处置 PASS**；不建议正面修改稳定章节。若作者补定理条件/勘误、真实 serving 成本与答案有效性验收，可定点重开。该裁决不代表 04/23 日级 Gate、日期逐篇精确时刻或全部相关工作覆盖。
