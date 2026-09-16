# 2026-05-17 V3 Owner Reconciliation

## 结论

旧版 `screening-ledger-independent-final.json` 的 279 个 identity 以 `submitted_v1_utc` 和抓取/注册时间构造 05-17 窗口，违反当前合同“先按官方首次公开或公告事件确定 owner，再做贡献筛选”的顺序。它们不能构成 2026-05-17 的 Candidate Denominator。

## 279 项逐项调和结果

利用已有后续 replay / recovery 记录的逐 identity `arxiv_id` 对齐结果为：

| 后续 replay / recovery 记录 | identity 数 | 旧候选数 | 旧分母前关闭数 |
| --- | ---: | ---: | ---: |
| 2026-05-19 | 252 | 28 | 224 |
| 2026-05-20 | 11 | 1 | 10 |
| 2026-05-21 | 3 | 0 | 3 |
| 2026-05-25 | 1 | 1 | 0 |
| 2026-05-26 | 1 | 1 | 0 |
| 2026-05-29 | 6 | 0 | 6 |
| 2026-06-02 | 1 | 0 | 1 |
| 2026-06-12 | 4 | 0 | 4 |
| **合计** | **279** | **31** | **248** |

其中 05-19～05-29 的 274 项可在 `arxiv-owner-replay-20260903/<date>/arxiv-owner-receipt.json` 逐项找到；`2606.00053` 出现在 06-02 DataCite boundary-created 记录，`2606.12435`～`2606.12438` 出现在 06-12 provisional raw bucket，且该 audit 明确记录 official listing receipt 未捕获。因此本表只证明 279/279 均不属于 05-17；后 5 项的恢复桶不是已确认的官方首次公开日，其精确 owner 由对应六月报告负责。这里也不覆盖更早的机构首次公开：`2605.17164` Charon 的 Source Family 已由 05-16 ByteDance Seed 官方事件拥有。

## 旧 31 候选

31/31 的 exact-v1 证据文件继续保留，但全部从 05-17 移出。其 arXiv 事件分布为 05-19 的 28 项、05-20 的 1 项、05-25 的 1 项、05-26 的 1 项。现有 exact-v1 packet 没有正向 withdrawn 标记；由于它们不是本窗事件，当前报告不据此声明这些 family 的现时撤回状态，撤回检查由真实 owner 日的 V3 认证负责。

## False-positive / False-negative 边界

- **False positive：** 旧 31 个候选全部是 05-17 owner-day false positive；旧 248 个 closure 也不是本窗已筛选 identity。旧评分和 Books 决定不进入本日报。
- **False negative：** 对每日机构来源做反向检查时发现 GIM 的 Meta 目录记录，但官方详情页日期为 05-18，arXiv v1 时刻为 2026-05-18T17:09:50Z；因此它是窗外/日期冲突线索，不是 05-17 的漏收候选。
- **Withdrawn：** 05-17 官方 arXiv announcement identity 为 0，所以本窗 withdrawn=0。旧 279 项的撤回状态不由 05-17 继承或宣称。

## 后续约束

真实 owner 日可以在 identity、exact version 与采用命题未变化时复用旧证据，但必须用 V3 准入、评分、Books 对读和非作者终审重新认证。05-17 不产生 Books 写回。
