# 2026-06-09 第二轮全表独立审计

审计日期：2026-09-11（Asia/Shanghai）

## 结论

第二位非作者复核者对 1,235 个 raw identities 与第一轮冻结的 115 个 Candidate 重新检查准入边界。最终冻结：

- Candidate：112；
- pre-denominator Close：1,123；
- Books disposition：112 `No Change — Existing Coverage`、0 `Integrate`、0 `Weekly Only`；
- exact-v1 blocker、普通 Pending、Books 正文缺口：均为 0。

第二轮与第一轮在 112 项上结论一致，并额外识别三个 false positive：

1. `2606.07909` MemToolAgent：把 extraction、environment/user feedback critique 与 similarity retrieval 组合为单一实现，只有局部 benchmark 增益，没有新的持久状态、控制权或验收合同。
2. `2606.08702` ConMem：memory-card graph、retrieval 与冲突协调重述既有 graph-memory pattern，收益归因不足以形成新的长期系统边界。
3. `2606.08300` QueryGraph：LLM 生成依赖图后用确定性 DFS 执行，是 typed plan / graph execution 的薄封装；题摘和正文未披露改变现有边界的协议、规模条件或反例。

三项均保留在原始 screening provenance 中，并以 family-specific reason 关闭；不再出现在 Daily Candidate table、Evidence Review 或 Books Decision 中。第一轮提出的其余 13 项 owner correction 全部确认。第二轮没有发现新的 false negative、Books 增量或需要用户补充的材料。

## Gate

`1,235 = 112 + 1,123` 算术闭合；112 个 Candidate identity 唯一，disposition 唯一。该审计覆盖候选准入、owner、Books existing-coverage 边界和反向误入检查；最终 Markdown、链接、validator 与整月一致性由 root 统一验收。
