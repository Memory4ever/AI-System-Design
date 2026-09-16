# 2026-05-07 V3 第四次 Fresh-context 非作者终审

**复核者：** `fresh-context:may07_fourth_final_reviewer:2026-09-15`

**角色边界：** 本复核者未参与 05-07 第三次作者返修或 root Books 写回；本轮不修改 Books。

**结论：** **PASS — Daily Complete / Gates Passed**

## 1. 账目与终态

- 原始身份守恒：`548 = 160 retained + 387 pre-denominator closure + 1 withdrawn`。
- Evidence：`156 source_review_complete + 4 disputed + 0 pending`；160 项均绑定 exact-v1，且没有 retained-candidate access blocker。
- Books：`63 Integrate + 76 No Change + 17 Daily Only + 4 Disputed`；63 项 Integrate 与 active comparison 完全一致。
- 160 项 Score V2 的三项均为 `0..3`，Total 均等于三项之和；160 个 owner 均可由 `ROADMAP.md` 解析。
- 四项 disputed 均已隔离为不支持 Books 的安全终态，并保留精确重开条件；当前没有需要用户补充的 primary material。

## 2. 第三次限定返修复核

### 2.1 Exact-v1 locator

逐篇重新打开官方 exact-v1 HTML，并对照真实目录、Method、Evaluation 与 Limitations：

| arXiv | Method | Evaluation | Limitations |
| --- | --- | --- | --- |
| `2605.04346` | §3.1–§3.6 | §4.1–§4.3；Appendix A | §4.3；§5；Appendix A.1–A.4 |
| `2605.04413` | §3；Theorems 1–3；§4 | §5.1–§5.2；Appendix C–E | Appendix A.4–A.6；Appendix F |
| `2605.04470` | §3.1–§3.4 | §4.1–§4.5；Appendix B–D | §5；Appendix A.5、B、D |
| `2605.04525` | §4.1–§4.2.3 | §5.1–§5.3；Appendix B–C | §6；§5.1.3；Appendix B–C |
| `2605.04647` | §4.1–§4.5；§5 | §6.1–§6.5 | §7 |
| `2605.04980` | §4；§5 | §5.1–§5.4；Appendix A.2–A.4；Appendix B | §7 |
| `2605.05172` | §III-A–III-C；Appendix A | §IV；Appendix B–D | §V；Appendix C |

上述 locator 与 active packet、evidence manifest 及 Daily 的描述一致，没有再发现不存在或越界的章节范围。

### 2.2 Source Family alias

对 23 个指定 canonical family 逐项比较 active ledger、packet 与 comparison；三处 alias 数组完全一致，且每项均包含旧 Books marker 与 `arxiv:<id>v1`。`2605.04450` 原有 canonical/alias 映射保持可解析，没有重复正文。

### 2.3 Books comparison 与正文 marker

- active comparison 恰含 63 项，集合与 packet 的 63 项 Integrate 一致；prior-only 29 项已移除，active-only 29 项已恢复。
- `2605.08215`、`2605.08234` 只保留在 cross-day exclusion 元数据中，未进入本日 active evidence 或 comparison。
- 63 个 Books marker 均唯一落在记录的 owner 文件，marker 计数与 comparison 一致，Stable Node/路径可由 `ROADMAP.md` 唯一解析，且全部位于 `## Review notes` 之前。
- 本轮只验证现存正文与采用命题、owner、位置和证据边界，不对 Books 作任何编辑。

## 3. Withdrawal 与独立假阴性挑战

`2605.04356v1` 的官方 arXiv 页面明确标示 withdrawn；active ledger 只保留一条 `withdrawn_excluded / Rejected — Withdrawn` 身份，packet、evidence、comparison 与候选表均无其 selected 记录。

在前轮已经检查的关闭样本之外，本轮另取 18 个高风险关闭项，覆盖 LLM/多模态、World Model、Agent、安全、训练、推理通信、生成范式与评价：

```text
2605.04057 2605.04128 2605.04172 2605.04185 2605.04410 2605.04412
2605.04559 2605.04842 2605.04870 2605.04899 2605.04973 2605.05000
2605.05020 2605.05031 2605.05092 2605.05123 2605.05151 2605.05197
```

逐项复读完整标题、摘要、现有关闭理由及前轮定点结论，没有发现新的高置信度 false negative。较容易误收的 JoyAI-Image、Driver-WM、Agentic Vulnerability Reasoning 与 VTAgent 均提供局部架构或任务证据，但题摘没有形成足以改变现有主线设计判断的长期机制、边界或反证；因此保持 pre-denominator closure。该结论只覆盖上述分层样本，不冒充对 387 项重新全文审阅。

## 4. 校验结果

- `scripts/validate_research.py --report papers/2026/05/07/README.md`：通过。
- 5 个 active JSON：语法通过；分母、Evidence、Books、Score、identity 集合与 cross-day/withdrawn 强断言通过。
- 7 组 locator、23 组 alias、63 个 Books marker/owner/Review-notes 顺序：通过。
- Daily 本地 Markdown 链接：通过。
- 范围内 unstaged/cached `git diff --check`：通过。

机器校验不替代上述语义复核。当前没有未处理的可执行工作；四项争议和两个跨日隔离项均不支持正向证据或 Books，并有定点重开条件。故 2026-05-07 可标记为 **完成**。
