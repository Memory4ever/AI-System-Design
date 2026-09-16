# 2026-06-02 V3 恢复阻塞与共享写入队列

## 分母证据冲突

- 可读 canonical raw packet：1,449 identities。
- 可读 semantic checkpoint：51 prior candidates + 1,398 closure proposals；其中历史状态字段已由本次 110/1,339 重审结果取代。
- 可读 owner receipt：51 candidate identities，18 个由 DataCite 确认本 owner，33 个需要迁移后重建。
- 旧报告顶部另称 736 raw identities、旧 52 收紧为 28；对应 `identity-provenance-v2-strict.json`、`candidate-denominator-audit-v3-fresh.json`、`screening-ledger-v3-fresh.tsv`、`evidence-audit-v3-fresh.json`、`evidence-books-comparison-v3-fresh.json`、`post-write-fresh-audit-v4.json` 均为 0 字节。

不得以 28 这个总数反推候选身份。当前已从 1,449-row packet 冻结 110 Candidate / 1,339 Close：旧 51 项为 44/7，旧 1,398 closure 为 66/1,332；逐项结果见 `V3_SCREENING_LEDGER.md`。

本轮 false-negative 抽检证实旧共享理由不可靠，因此已全量重审 1,398 项并恢复 66 项。`SENSE`、`ART`、`BudgetDraft`、`PrivacyPeek`、`Bit-Exact AI Inference Verification`、`PR2`、`When Safe Skills Collide` 和 `TAPS` 的完整摘要能指出明确系统合同；`BitsMoE`、`CAST` 等仅有局部模型/训练增量者仍关闭。当前不再有待重审的 closure family。

## Books 共享写入队列（已闭合）

旧报告标记 17 项 `Integrate`；当前准入保留 16 项，`SF-ORDER-AGNOSTIC-CHAIN-RULE` 撤回并删除整条采用链。三条错误 Daily 日期均已修正为 `2026-06-02`。16 个存续项已逐项执行 trace-to-body：14 项完成正文绑定，`SF-ADAPTIVE-AUTO-HARNESS` 与 `SF-GHOST-TOOL-ISSUE-PRIVACY` 经当前正文重读改判 Existing。

本轮从旧 closure 恢复的 20 个 proposal 也已全部由对应 owner 消费：19 项完成正文绑定，`SF-MEMPRO-EVOLVABLE-PROGRAM` 经当前 Memory 正文重读改判 Existing。另有 `SF-SKILLHARM-LIFECYCLE` 在旧前沿复判中由 proposal 改判 Existing，命题锚点为“Harness Backdoor 把单次写入变成跨 Run 控制状态”。

最终共享队列为 0，exact-v1 access blocker 为 0；全部新增正文与 Existing 锚点已经由非作者按正文而非 trace 完成 post-write review。完整清单与验收结果见 `POST_WRITE_AUDIT_SCOPE_V3.md`。
