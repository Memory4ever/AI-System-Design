# 2026-05-26 Root Marker-only Repair

**Status:** Applied；等待不同 fresh non-author 最终复核。

Root 按 `root-books-writeback-queue-v3.json` 为 7 个已经存在且通过作者侧语义复核的正文块补齐精确 `source-family` marker：`2605.24322`、`2605.24366`、`2605.24545`、`2605.24549`、`2605.24696`、`2605.24718`、`2605.24737`。本轮没有新增或重复正文机制，也没有改变 Books disposition。

校验结果：16/16 paired semantic markers 和 16/16 source-family markers 全局唯一；结束 marker 与 source marker 均位于目标章节首个主 `## Review notes` 前；V3 validator、JSON、queue arithmetic 与 scoped `git diff --check` 通过。机械校验不替代不同 reviewer 的最终语义 Gate。
