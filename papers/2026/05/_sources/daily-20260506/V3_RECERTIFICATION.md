# 2026-05-06 V3 重新认证

本文件只保存当前 checkpoint。更早的 57/436、63 候选和 27 项写回批次均已被本轮 493 项重放取代，不得继续作为活动分母、评分或 Books Gate。

## 当前事实

- Window：2026-05-05T09:00:00+08:00 ～ 2026-05-06T09:00:00+08:00。
- Raw identities：493。
- Candidate Denominator：137。
- Pre-denominator closure：356。
- exact-v1 evidence：137/137。
- Independent score review：137/137。
- Independent Books proposition review：137/137。
- Books decisions：12 existing entities + 10 root writebacks + 115 Existing Coverage。
- Withdrawal terminal closure：`2605.03562`；不属于候选、评分或正向 Books chain。
- Overall status：Complete；10 项 Books 写回均已落实，post-write fresh-context Gate 通过。

## 活动文件

- `v3-canonical-screening-ledger.json`：唯一活动 identity/denominator ledger。
- `AUTHOR_EVIDENCE_COMPLETION.json` / `.md`：137 项 exact-v1 evidence。
- `NONAUTHOR_SCORE_RECALIBRATION.json`：137 项 before/after 独立重评分。
- `NONAUTHOR_BOOKS_RECONCILIATION.md`：已落实的精确 root Books 队列与 115 项 Existing Coverage 对读。
- `POST_WRITE_FRESH_CONTEXT_AUDIT.md`：10 项新写回、12 项既有实体和 withdrawal 不变量的独立复核。
- `NONAUTHOR_FINAL_GATE.md`：最终独立 Gate。

旧 `screening-ledger-*`、`exact-v1-review-packet.json`、`BOOKS_WRITEBACK_QUEUE.md`、`post-write-semantic-audit.json` 与 marker repair 文件均为 superseded reconstruction artifacts，只能解释历史过程，不能支持当前状态。为防止旧状态复活，`screening-ledger-final.tsv` 中的 `2605.03562` 已改为 withdrawal terminal closure，旧 `build_author_packet.py` 也已设置为 fail-closed；当前重建只能使用 `finalize_author_repair.py` 与活动 V3 账本。
