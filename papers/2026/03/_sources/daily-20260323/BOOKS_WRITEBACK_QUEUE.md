# Books Writeback Queue — 2026-03-23

**Status:** Pending root serial writeback and fresh-context prewrite audit. 本文件不证明 Books 已修改。

| Source Family | Exact Source | Stable Node | Target | Adjacent | Existing Proposition | Proposed Durable Mechanism | Evidence Boundary | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-19664 | arXiv:2603.19664v1 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md | books/part-05-inference-system/44-decode.md; books/part-05-inference-system/46-continuous-batching.md | 第一条分支按 head 在 shared、residual 与 exact mode 之间做离散路由，适合表达“这个 head 是否需要保真”； 第二条分支按 token 分配 residual rank，适合表达“同一 head 内哪些位置需要更多层间细节”。二者复用相邻层 相关性原则，却不是同一种 selector。attention-logit 或 attention-output reconstruction error 只是当前 prompt 的 保真 proxy，不是未来 causal utility；probe、router、basis、residual precision 与 policy revision 都必须进入 cache identity。 | 论文从 residual stream 重新计算部分层的 K/V，以重算换缓存容量，并按层选择可替代的 KV。 | 只支持 arXiv:2603.19664v1 §3 Method 的机制与 §5.4 Downstream Task Evaluation (RQ2) 的公开 workload；§6 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 | applied_postwrite_verified |
