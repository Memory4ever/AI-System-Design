# 2025-05-01 Source Packet

- Window: `[2025-04-30T09:00:00+08:00, 2025-05-01T09:00:00+08:00)`
- Raw identities: `853`
- Registered routes: `339`（`217` Core full-semantic + `122` routed categories；其中 `107` keyword-triggered）
- Retained Source Families: `19`
- Pre-denominator closures: `834`
- Coverage snapshot: `../arxiv-20250501.xml`
- Screening evidence: `screening-ledger.json`
- Summary: `screening-summary.json`
- Report builder: `generate-report.py`
- Books writeback receipt / audit queue: `books-writeback-queue.md`

`SHA256SUMS.txt` 只列本报告实际使用的 frozen evidence：一个 Atom snapshot，以及 19 个候选对应的 20 个 exact-v1 HTML/PDF 文件。`arxiv-2505.10571v1.html` 是筛选期的未引用下载，不属于本报告 Reviewed Evidence，也不进入 manifest。

首次冻结为 15 个候选。fresh-context false-negative audit 找到 `2504.21680`、`2505.10570`、`2504.21752` 与 `2505.00749` 四项，完成 exact-v1 Review 后重新冻结为 19；ledger 保留修正前后的语义原因。
