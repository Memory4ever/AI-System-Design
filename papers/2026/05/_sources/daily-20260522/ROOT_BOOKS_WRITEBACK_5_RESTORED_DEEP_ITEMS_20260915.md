# 2026-05-22 Root Books Writeback — Five Restored Deep Items

- Writer: root（serialized Books owner）
- Status: Applied；等待 fresh non-author post-write semantic review
- Queue: `BOOKS_WRITEBACK_QUEUE_V3.json`

## Applied bindings

| Source Family | Stable owner | Target | Result |
| --- | --- | --- | --- |
| `SF-2026-ARXIV-2605-22223` | `MODEL-DECODER-ONLY` | `books/part-02-model/18-decoder-only.md` | 写入架构条件下的 reachable-output support 上界、Evaluation owner 与 direct-test fallback |
| `SF-2026-ARXIV-2605-22596` | `MULTIMODAL-EMBODIED-VLA` | `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` | 写入 factorized diffusion policy 的独立性假设、score/controller 权限与 trajectory-tube 边界 |
| `SF-2026-ARXIV-2605-22705` | `MODEL-TOKENIZER` | `books/part-02-model/11-tokenizer.md` | 写入 split-tree inference 与 vocabulary 联合身份、全局选择成本及兼容回退 |
| `SF-2026-ARXIV-2605-22765` | `MULTIMODAL-GENERATIVE-PARADIGMS` | `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` | 写入 discrete-diffusion 的 marginal/parameterization/loss/sampler 联合身份与近似边界 |
| `SF-2026-ARXIV-2605-22821` | `MODEL-TOKENIZER` | `books/part-02-model/11-tokenizer.md` | 写入 convex relaxation 的 objective-specific certificate 与独立行为 Gate |

## Root checks

- 每个 Source Family 均使用唯一的 paired `semantic-body-binding` marker。
- 写回嵌入既有机制演进链；未创建论文列表式正文。
- 保留旧方案适用条件、约束变化、收益、代价、failure mode 与 fallback。
- `git diff --check` 对四个目标章节通过。
- 本收据不构成最终 Gate；独立复核须重新检查证据边界、章节 owner 与正文语义。
