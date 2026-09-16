# 2026-05-29 Fresh Non-Author Final Review

- Reviewer role: fresh non-author；未参与 05-29 author rebuild 与 TaskMem Books writeback。
- Review result: **FAIL — bounded owner/corpus repair required**。
- Reviewed at: 2026-09-16T17:30:00+08:00。

## Adversarial finding

当前报告把 823 个 arXiv identity 全部移出 confirmed raw，并称缺少逐项官方 announcement membership。这个判断与项目自己的权威日期依据及已保存 owner receipt 冲突：

- `papers/2026/05/_sources/ARXIV_ANNOUNCEMENT_PROVENANCE.md` 明确允许 exact-v1 identity、initial DataCite registration 与官方 announcement cadence 一致时恢复 owner；后续 revision OAI datestamp 不单独制造日期缺口。
- `papers/2026/05/_sources/arxiv-owner-replay-20260903/20260529/arxiv-owner-receipt.json` 已保存 823 个身份，其中 623 个是 `official_arxiv_oai_direct`，200 个是 initial-registration recovery，`semantic_review_pending_count=0`。
- 配套 canonical ledger 已冻结 `823 = 115 retained + 708 pre-denominator closure + 0 withdrawn`，115 个候选都有已完成的 exact-v1 review 与 Books disposition。

因此当前正文的 `1 = 1 + 0 + 0` 只覆盖 TaskMem 官方事件，不是该日完整已确认 corpus 的守恒式；`source-coverage-v3.json`、`screening-outcomes-v3.json`、Evidence、Books comparison 与正文都不能作为 final projection。

## TaskMem writeback check

TaskMem 本身通过：

- Seed `ArticleMeta.PublishDate=1779984000000` 可确定 `2026-05-29T00:00:00+08:00` owner；exact-v1 为 `arXiv:2605.31075v1`，检查时无 withdrawn 标记。
- `3 + 2 + 3 = 8` 与 `AGENT-MEMORY` owner 合理：它改变 memory-write policy 与 task-distribution adapter 的控制边界，而不是只报告单任务精度。
- Ch77 的 paired marker 位于机制正文、早于 `Review notes`。正文保留 base-quality writer → task-conditioned adapter、recent-task proxy、durable commit authority 分离、drift/forgetting 代价和 general-policy/raw-evidence fallback；没有把作者 benchmark 外推为生产可靠性。

TaskMem 的通过不能抵消 arXiv corpus 缺失。

## Exact bounded repair

只重建 05-29 当前 V3 投影，不扩来源或日期：

1. 以已保存 owner receipt/canonical ledger 恢复 823 个 arXiv identity、115 retained、708 closure、0 withdrawn；与 TaskMem 官方 Source Family 做跨源去重后重算总守恒。
2. 将 115 个既有 exact-v1 review 与 Books disposition 投影到当前 Evidence/Books JSON；保留 TaskMem 的独立官方 owner 与已应用 binding。
3. 若 Rosalind/DeepMind date-only 项仍无法跨 09:00 边界定 owner，只能作为终态隔离项，不进入 raw 算术、正面证据、Books 或无遗漏断言。
4. 重跑 validator、JSON、集合算术、identity uniqueness、Books marker 与 scoped diff-check；随后由另一位未参与 repair 的 fresh non-author reviewer 终审。

在上述 repair 完成前，README 必须保持 `进行中`。
