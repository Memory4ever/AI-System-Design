# 2026-05-05 bounded repair：root Books 写回队列

**状态：** 1 项已由 root 写入并通过 fresh non-author 最小范围终审；作者未修改 Books，且未自行签发最终 Gate。

## `SF-2026-ARXIV-2605-02375` → `TRAIN-RLHF` / Ch31

- 来源：`arXiv:2605.02375v1`；[exact-v1 HTML](https://arxiv.org/html/2605.02375v1)；[exact-v1 PDF](https://arxiv.org/pdf/2605.02375v1)。
- 精确位置：在 `Reverse KL 会把“找到高奖励”收缩成单一路径` 小节内，位于现有 `SF-2026-ARXIV-2605-19461` 证据边界之后、`Reward hacking 与 Goodhart's Law` 之前；先重排现有论证，不新增论文摘要式小节。
- 现有缺口：正文已经要求 reward 与 response-distribution coverage 分轴，却没有解释 binary reward 的 fully-valid optimum degeneracy、filtered target 的来源、reverse-KL support mismatch 及 misspecification 如何把低 `beta` 压力转成 mode collapse。
- 应写增量：binary verifier 只定义 valid support，base/reference 决定 valid outputs 间的相对概率；KL-to-base 隐式选择 filtered target。该 target 在 forward KL 中可由 tilted distribution 逼近，但 full-support policy 对其 reverse KL 为无穷；模型族无法表示目标时，提高 validity 的压力可能选择更易达到的近 Dirac valid path。
- 状态与控制权：verifier 只拥有 valid/invalid；base/reference 拥有相对概率先验；optimizer 只在可表示 family 内更新；Evaluation 同时观察 validity、entropy/coverage、KL direction、model family 与 optimizer path。
- Trade-off / fallback：forward KL 或 alpha-divergence 增加采样与密度估计成本，也可能保留低质量 valid modes；单一可验证答案、目标分布不可估计或预算有限时，reverse-KL baseline 仍合理。coverage 明显下降时再启用替代分支，并保留独立 verifier、diversity slice 和 base/reference 对照。
- 证据边界：§2～§5 与 Appendix A 支持形式链路；§4.4 / Appendix B 只有 toy n-gram 实验，不证明所有真实 LLM RLVR 都坍缩或替代 divergence 普遍更优。

机器可读字段见 [JSON queue](./V3_BOUNDED_REPAIR_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.json)。
