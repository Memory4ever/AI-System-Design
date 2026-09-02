# Books Writeback Queue — 2026-03-19

**Status:** Pending root serial writeback and fresh-context prewrite audit. 本文件不证明 Books 已修改。

| Source Family | Exact Source | Stable Node | Target | Adjacent | Existing Proposition | Proposed Durable Mechanism | Evidence Boundary | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-17803 | arXiv:2603.17803v1 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md | books/part-05-inference-system/44-decode.md; books/part-05-inference-system/46-continuous-batching.md | 当 cold tier 从单一 host memory 扩展到多块 SSD，容量不再是主要矛盾，访问并行度和数据布局才是。简单 hash 或 round-robin striping 假设每个 KV block 独立且请求分布均匀；实际检索若经常共同激活一组历史 blocks， 它们落到同一设备就会形成热点。可选分支可以离线学习 co-activation graph，把相关 block 分散到不同设备， 在线再协同 fetch、更新 hot cache： | Swarm 离线学习 KV co-activation，按关联图跨 SSD 放置，并在在线阶段协同检索、更新和缓存。 | 只支持 arXiv:2603.17803v1 §4 Design Overview 的机制与 §8.2 Overall Performance 的公开 workload；§8.4 Sensitivity Analysis 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 | applied_postwrite_verified |
