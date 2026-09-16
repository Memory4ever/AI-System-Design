# 2026-05-22 Root Books Writeback — Three Active Deep Items

- Writer: root（serialized Books owner）
- Status: Applied；等待 fresh non-author post-write semantic review
- Queue: `BOOKS_WRITEBACK_QUEUE_V3.json`

| Source Family | Stable owner | Target | Applied proposition |
| --- | --- | --- | --- |
| `SF-2026-ARXIV-2605-21865` | `PLATFORM-GATEWAY` | `books/part-06-ai-infrastructure/62-gateway.md` | 只有 order 对 client contract 无语义且端到端保序时，key permutation 才能作为受限 trace watermark；提取不证明完整性或授权 |
| `SF-2026-ARXIV-2605-21958` | `AGENT-WORKFLOW` | `books/part-07-agent/81-workflow.md` | causal diagnosis 与 patch prescription 分权，同一 frozen snapshot 比较 patch loci 并端到端 replay |
| `SF-2026-ARXIV-2605-22237` | `INFER-TENSORRT-LLM` | `books/part-05-inference-system/49-tensorrt-llm.md` | FHE activation replacement 以 decision regime 标识；exact certificate 仅限 positive-margin calibration decisions |

## Root checks

- 三个 Source Family 均使用唯一 paired `semantic-body-binding` marker，并位于主 `Review notes` 前。
- 正文保留旧方案、约束变化、owner、证据边界、trade-off 与 failure fallback。
- 本收据不构成最终 Gate；独立复核需挑战 adopted proposition 与 exact-v1 evidence 的对应关系。
