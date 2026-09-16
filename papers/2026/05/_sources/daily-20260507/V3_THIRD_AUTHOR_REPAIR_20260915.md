# 2026-05-07 V3 第三次作者限定返修

**身份：** bounded repair author，不具备最终 Gate 签署权

**范围：** 仅处理第三次非作者终审列出的 locator、alias、Books comparison 与对应证据状态

**状态：** **Ongoing — 作者返修完成，等待新的非作者限定复核**

## 1. 不变账目

- 分母：`548 = 160 retained + 387 pre-denominator closure + 1 withdrawn`。
- Evidence：`156 complete + 4 disputed + 0 pending`。
- Books disposition：`63 Integrate + 76 No Change + 17 Daily Only + 4 Disputed`。
- `2605.04356` 继续只保留 withdrawn identity 与排除理由，不进入候选、评分或 Books。
- 本次未修改任何 Books 正文，也未改变 63 项既有 Integration 的语义命题。

## 2. Exact-v1 locator 返修

7 篇论文的官方 exact-v1 HTML 均已重新打开，并以页面真实目录校正 active packet 与 Daily：

| arXiv | Method | Evaluation | Limitations |
| --- | --- | --- | --- |
| `2605.04346` | §3.1–§3.6 | §4.1–§4.3；Appendix A | §4.3；§5；Appendix A.1–A.4 |
| `2605.04413` | §3；Theorems 1–3；§4 | §5.1–§5.2；Appendix C–E | Appendix A.4–A.6；Appendix F |
| `2605.04470` | §3.1–§3.4 | §4.1–§4.5；Appendix B–D | §5；Appendix A.5、B、D |
| `2605.04525` | §4.1–§4.2.3 | §5.1–§5.3；Appendix B–C | §6；§5.1.3；Appendix B–C |
| `2605.04647` | §4.1–§4.5；§5 | §6.1–§6.5 | §7 |
| `2605.04980` | §4；§5 | §5.1–§5.4；Appendix A.2–A.4；Appendix B | §7 |
| `2605.05172` | §III-A–III-C；Appendix A | §IV；Appendix B–D | §V；Appendix C |

采用命题和 evidence description 不需要改写；原问题是不存在或过宽的章节范围，尤其 `2605.05172` 必须使用正文实际采用的罗马编号。

## 3. Source Family alias 返修

以下 23 个 active canonical family 已在 active ledger、active packet 和新 comparison 中登记旧 Books marker 与 `arxiv:<id>v1` alias：

```text
2605.04418  2605.04431  2605.04446  2605.04468  2605.04477
2605.04478  2605.04496  2605.04563  2605.04572  2605.04624
2605.04665  2605.04678  2605.04709  2605.04719  2605.04811
2605.04913  2605.04960  2605.04984  2605.04992  2605.05007
2605.05049  2605.05090  2605.05112
```

`2605.04450` 与 `2605.04711` 原有 canonical/alias 映射保持不变。alias 只恢复身份回溯，不重复写 Books 正文。

## 4. Books comparison 重建

`books-current-content-comparison.json` 已由 active 160-item packet 重新生成：

- 项目数：63，且全部为 active `Integrate`。
- 与旧快照重合 34 项；active-only 29 项已经恢复；prior-only 29 项已经移除。
- 跨日 `2605.08215`、`2605.08234` 已明确排除，未误归 05-07。
- 每项均记录 canonical family、alias、Stable Node、实际 Books 路径、采用命题与真实 marker。
- 63 项集合与 active packet 的 63 项 `整合` 一一对应；marker 均能解析到唯一 owner Books 文件。

active evidence manifest 同步按 160 个 retained item 重建，记录 exact-v1 URL、Method/Evaluation/Limitations locator、review status 与 Source Family identity；旧 manifest 中 17 个非本日 active identity（含两个跨日 family）不再作为本日 evidence item。

## 5. 变更范围与下一步

本次变更仅涉及：

- `papers/2026/05/07/README.md`
- `screening-ledger-v3-author-repair.json`
- `exact-v1-review-packet-v3-author-repair.json`
- `books-current-content-comparison.json`
- `evidence-provenance-manifest.json`
- `coverage-receipt.json`
- 本 checkpoint

作者侧可判定一致性检查确认：160 个 active identity、63 个 Integration、23 组新增 alias、7 组 locator 与两个跨日排除相互一致。最终 Gate 仍需新的非作者只复核上述受影响范围；在该复核完成前，Daily 必须保持 `进行中`，不得标记 `Complete / Gates Passed`。

## 6. 作者侧校验结果

- `scripts/validate_research.py --report papers/2026/05/07/README.md`：通过。
- 范围内 `git diff --check`：通过。
- JSON 与 Books marker 强断言：通过；63 项 Integration 集合完全相等，23 组 alias 在 ledger/packet/comparison 完全一致，7 组 locator 与 Daily 完全一致。
- 工作树检查：未 stage、commit、push；仓库中已有大量其他日期和 Books 修改，本轮未覆盖或回滚。

这些结果只证明作者侧格式与可判定一致性，不替代新的非作者语义复核。
