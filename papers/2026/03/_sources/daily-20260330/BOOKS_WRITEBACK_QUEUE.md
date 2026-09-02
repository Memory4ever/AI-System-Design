# Books Writeback Queue — 2026-03-30

**Status:** Pending root serial writeback and fresh-context prewrite audit. 本文件不证明 Books 已修改。

| Source Family | Exact Source | Stable Node | Target | Adjacent | Existing Proposition | Proposed Durable Mechanism | Evidence Boundary | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-26498 | arXiv:2603.26498v1 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md | books/part-05-inference-system/55-pd-disaggregation.md; books/part-06-ai-infrastructure/57-what-is-ai-platform.md | 本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。** | TCM-Serve 建立 modality-aware resource abstraction，并在 preprocessing、encoding、prefill/decode 间按异质需求排序与并发，显式拥有阶段资源状态。 | 只支持 arXiv:2603.26498v1 §3.1–§3.7 System Design 的机制与 §4.1–§4.4 的公开 workload；§4.4 Discussion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 | applied_postwrite_verified |
