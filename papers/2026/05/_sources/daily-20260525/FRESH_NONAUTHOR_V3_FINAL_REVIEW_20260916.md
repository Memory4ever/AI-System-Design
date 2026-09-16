# 2026-05-25 fresh non-author V3 final review

- reviewer role: 未参与本日 author recertification 或 root Books writeback。
- verdict: **FAIL / Ongoing**；不签 Complete，不写共享 Books。
- author claim checked: `499 = 82 + 417 + 0`；`82 = 77 deep complete + 4 standard complete + 1 deep blocked`；`17 Applied + 5 Integrate + 53 No Change + 2 Structural + 4 Report Only + 1 Deferred`。
- physical root state: 5 个新 binding 已写入，故物理 Books 状态是 22 个 Applied binding；原 comparison/README 的 `5 Integrate pending root` 已过时，但不能因写回完成而跳过 Evidence 与 semantic Gate。

## 结论

最终 Gate 未通过。closure 中至少 20 项已经由 title + full abstract 证明存在长期机制却被 generic reason 关闭，另有 21 项同理由 bounded reopen；因此 `82 retained / 417 closure` 不是可冻结的语义分割。owner receipt 对 400 项有 official OAI direct 路径，但 97 项的底层 receipt 仍把 DataCite initial-created 写作 owner proxy，当前 batch wrapper 没有保存官方 first/last membership locator，故 497 arXiv denominator 也不能直接宣告最终通过。

Evidence 中 `2605.22850` locator 不可重放，`2605.22873` 与 `2605.22967` 的 limitations section 写错，`2605.23476` locator 不够精确；`2605.22834` 与 `2605.23857` 的核心摘要命题可核，但 independent exact-v1 body replay 受阻。`2605.23491` 的 Deferred terminal isolation 正确：它不支撑正面结论，也没有进入 Books。

5 个新 root binding 的 paired marker 都是全局唯一且位于正文、在 `## Review notes` 前；`22873/22967/23476` 的机制、owner、trade-off、failure/fallback 语义通过，`22834/23857` 保留材料复核条件。17 个旧 Applied 中 `2605.22949` 与 `2605.23893` 的 marker 已被后续段落挤离原命题，需 root 重新成对绑定。53 个 No Change 中 37 个只有 owner headings 或泛化 owner summary，没有可重放 existing proposition locator。

机构源方面，Meta 与 Xiaomi 的边界隔离正确；`zero_omission_claim=false` 正确。其余 day-level no-hit 记录只有文字结论，没有官方 checked URL 与相邻日期条目 URL，需补 receipt，不能靠 prose assertion 完成 Coverage Gate。

精确、严格有界的修复对象见 `FRESH_NONAUTHOR_V3_REPAIR_QUEUE_20260916.md`；结构化审计见 `fresh-nonauthor-final-review-v3.json`。
