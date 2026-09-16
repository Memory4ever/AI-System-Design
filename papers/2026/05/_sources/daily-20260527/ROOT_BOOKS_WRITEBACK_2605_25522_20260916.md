# 2026-05-27 Root Books Writeback — 2605.25522

- Source Family: `SF-2026-ARXIV-2605-25522`
- Owner: `AGENT-RAG`
- Target: `books/part-07-agent/76-rag.md`
- Anchor: `多向量检索的数据面要避免搬运高精度向量`
- Result: paired semantic-body binding 已写入主 `## Review notes` 之前。

正文承载 PIM graph-ANNS 的联合数据面约束：compact index、跨 PU traversal、host dispatch、异步 mini-batch、rerank/transfer，以及同 recall 下的 overfetch、QPS、energy 与 tail-latency 验收。证据边界保留作者披露的三套 billion-scale 数据与 dual-Xeon/A100/UPMEM 环境；multi-node 与新一代 PIM 的模拟/投影未被外推。

机械检查只确认 marker、位置、JSON 与 Markdown 一致性；最终语义 Gate 仍由未参与本次修复或写回的 fresh non-author reviewer 决定。
