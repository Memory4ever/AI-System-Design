# 2026-05-07 V3 第三次 Fresh-context 终审

**复核者：** `fresh-context:may07_final_independent:2026-09-15`  
**范围：** 只复核 2026-05-07，不扩展时间窗，不修改 Books  
**结论：** **FAIL — Daily 继续保持进行中**

## 1. 已确认成立的部分

- 活跃 V3 账本守恒：`548 = 160 retained + 387 pre-denominator closure + 1 withdrawn`。
- 160 个 retained identity 与 active exact-v1 packet 的 160 项完全一致；Evidence 为 `156 source_review_complete + 4 disputed + 0 pending`，Books 处置为 `63 整合 + 76 已有覆盖 + 17 仅报告 + 4 争议`。
- `2605.04356` 仅保留 withdrawn identity、状态与排除理由，未进入候选、评分或 Books 正向证据链。
- 160 项 V3 Score 的三项加总均正确，Method / Evaluation / Limitations 字段非空，所有 Stable Node 均可在 `ROADMAP.md` 解析。
- 对 387 个关闭项重新检查标题，并对容易形成系统误判的 LLM、Agent、VLA、World Model、Evaluation、Inference、Training 与 Security 条目定点复读完整摘要。重点复读的 `2605.04264`、`2605.04304`、`2605.04547`、`2605.04607`、`2605.04641`、`2605.04726`、`2605.04759`、`2605.04858`、`2605.04916`、`2605.05126`、`2605.05182` 未形成新的高置信度 false negative：它们分别停留在观点议程、领域任务、局部方法或一般机器人控制，现有关闭理由可成立。
- 63 项 `整合` 的当前章节 marker 均能解析到唯一 Books 文件，owner 与 active ledger 一致，且 marker 均位于 `## Review notes` 之前；没有发现“只在报告中声称整合、Books 正文完全不存在”的项目。
- root 本轮新增的 7 项正文（`2605.04346`、`2605.04413`、`2605.04470`、`2605.04525`、`2605.04647`、`2605.04980`、`2605.05172`）均形成了旧方案/约束变化、机制与状态 owner、收益与代价、failure/fallback、exact-v1 外推边界；正文语义本身通过本轮复核。

上述机器检查只能证明可判定一致性。本轮另行打开了 7 个 exact-v1 HTML 并对照真实目录与正文；因此下面的 locator 问题不是 validator 推断。

## 2. 阻塞 Gate 的问题

### 2.1 七个新增 Source Review 的 exact-v1 locator 均需校正

采用命题与 Books 正文没有发现实质错误，但 active packet / Daily 中的若干章节号或 Appendix 范围并不存在于 exact-v1，不能以错误 locator 支撑证据链：

| arXiv | 当前 locator 问题 | 应按 exact-v1 重定位的范围 |
| --- | --- | --- |
| `2605.04346` | Evaluation 写 `§4.1–§4.4；Appendix A–D`，Limitations 写 `§4.4–§5`；exact-v1 只有 §4.1–4.3 与 Appendix A | Method §3.1–3.6；Evaluation §4.1–4.3、Appendix A；限制由 §4.3、§5 与实验范围定位 |
| `2605.04413` | Limitations 写 `§5.4`，exact-v1 的 §5 只有 §5.1–5.2 | Method §3–4；Evaluation §5.1–5.2、Appendix C–E；Limitations Appendix F，并引用相关反例/假设位置 |
| `2605.04470` | Method 写到不存在的 §3.5，Evaluation 写到不存在的 Appendix E | Method §3.1–3.4；Evaluation §4.1–4.5、Appendix B–D；限制由 §5 与 Appendix B/D 的适用条件定位 |
| `2605.04525` | Method 写 `§4.1–§4.4`、Evaluation 写 `Appendix D–F`、Limitations 写 `Appendix F`；exact-v1 方法止于 §4.2.3，Appendix 只有 A–C | Method §4.1–4.2.3；Evaluation §5.1–5.3、Appendix B–C；限制由 §6 及对应实验/实现范围定位 |
| `2605.04647` | Evaluation 写 `Appendix C–F`，exact-v1 没有这些 Appendix；Method 还遗漏了直接支撑 RL credit 的 §4.5 | Method §4.1–4.5、§5；Evaluation §6.1–6.5；Limitations §7 |
| `2605.04980` | Evaluation 写 `Appendix C–F`，exact-v1 只有 Appendix A–B；`§4–§6` 还混入机制和结论而非精确 evaluation 范围 | Method/representation §4 与 §5；Evaluation §5.1–5.4、Appendix A.2–A.4、Appendix B；Limitations §7 |
| `2605.05172` | 使用阿拉伯 `§3.1–§3.3 / §4 / §5`，而 exact-v1 可见章节为罗马编号 III-A–III-C、IV、V | Method III-A–III-C、Appendix A；Evaluation IV、Appendix B–D；Limitations V、Appendix C |

修复时只改 locator 与受其影响的证据描述，不需要重写已经成立的 Books 段落；校正后需再由非作者抽查源文与采用边界。

### 2.2 23 项 Source Family 缺少显式 alias

下列 active packet 以 `SF-2026-ARXIV-*` 为 family id，但 Books 正文沿用旧标题 marker；`review_gap` 虽能人工读出映射，active ledger/packet 却没有像 `2605.04450` 那样登记 alias，导致 family identity 不能稳定机器回溯：

```text
2605.04418  2605.04431  2605.04446  2605.04468  2605.04477
2605.04478  2605.04496  2605.04563  2605.04572  2605.04624
2605.04665  2605.04678  2605.04709  2605.04719  2605.04811
2605.04913  2605.04960  2605.04984  2605.04992  2605.05007
2605.05049  2605.05090  2605.05112
```

这 23 项不是 Books 正文缺失；它们的旧 marker 与正文均已找到。最小修复是在 active screening ledger、active exact-v1 packet 及重建后的 comparison 中登记同一 canonical family 与旧 marker alias，不重复写 Books 正文。

### 2.3 Books comparison artifact 仍是旧/新混合快照

`books-current-content-comparison.json` 有 63 项，但并非 active packet 的 63 项 `整合`：二者仅重合 34 项，各有 29 项不一致；该文件内部还是 `35 Integrate + 19 No Change + 7 整合 + 1 已有覆盖 + 1 仅报告` 的混合状态，并包含不属于 05-07 active denominator 的 `2605.08215`、`2605.08234`。

最小修复是从 active 160-item packet 重建 comparison：至少覆盖全部 63 项 `整合`，并使每项的 disposition、canonical family、alias、owner、章节路径与实际 marker 一致。若该文件不再承担 active Books comparison，则应明确标记 superseded，并创建唯一的当前 comparison；不能让 README 把它当现行证据。

## 3. 最小返修范围

1. 重新打开上述 7 个 exact-v1 HTML，校正 active packet 与 Daily 中的 Method / Evaluation / Limitations locator；采用命题不变时不重写 Books。
2. 为 23 项旧标题 marker 补 canonical/alias 映射，贯通 active ledger、packet 与 comparison。
3. 从 active packet 重建 `books-current-content-comparison.json`，消除 29/29 集合漂移和跨日条目。
4. 作者修复后，仅对这三类受影响范围做新的非作者复核；未受影响的 153 项 Source Review、其余 40 项 Integrate 正文与已成立的分母检查可以复用。

不需要用户补充 primary material；7 个 exact-v1 HTML 本轮均可直接访问。由于以上问题仍可在仓库内修复，05-07 的状态必须保持 `进行中`，不得写 `Complete / Gates Passed`。
