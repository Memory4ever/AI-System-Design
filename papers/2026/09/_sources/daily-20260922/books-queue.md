# 2026-09-22 Books Queue

## 已落实

| Source Family | Owner | 实际写回 |
| --- | --- | --- |
| `SF-2026-ARXIV-2609-20830` | `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 | 增加 mutable-canvas cursor-action AR 分支，说明串行 action、KV identity、rollback 与 append-only fallback |
| `SF-2026-ARXIV-2609-21058` | `INFER-TENSORRT-LLM` / Ch49 | 增加真实 workload addressable fraction、端到端上界、scale-invariant correctness 与 complete-write admission |
| `SF-2026-ARXIV-2609-21079` | `INFER-SCHEDULING` / Ch56 | 增加异构多阶段全局 routing 的分层 observation、latency model、admission、漂移与保守 fallback |

三项均已置于 owner 章节的机制主线内，并带唯一 Source Family marker；没有写入未披露 benchmark 条件。

## 仍需裁决

- Qwen Code v0.24.3 经官方 release 与 Ch84/Ch72 已有论点对读后候选前关闭，不再进入评分或 Books Gate。剩余 65 个 arXiv 暂列候选仍需最终 Books disposition；其中 43 项尚需完成证据审阅或 fallback recovery。以上候选分母仍待原始 arXiv 来源清单重建。
- `2609.21081`、`2609.21172`、`2609.21187`、`2609.21284`、`2609.21858`、`2609.22056` 等可能由现有正文覆盖，但必须给出真实论点锚点。
- `2609.21573`、`2609.21908`、`2609.22005` 等可能提供新 failure mode；只有证据与邻接对读成立后才写入。
- `2609.12748v2` 已核原始正文的因果解释撤回；Ch84 既有论点不把 request/exposure 当作实际传播或 outcome，仍需官方 replacement 日与独立语义复核后给最终 Books disposition。

队列清空、报告同步和 fresh non-author writeback review 之前，Books Gate 与 Daily Gate 均保持打开。
