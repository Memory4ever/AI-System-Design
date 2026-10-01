# 04/28 SF-2026-ARXIV-2604-23467：Ch49 非作者写后复核

作者：apr02；复核者：root。此复核只验该 Source Family 的实际书稿增量，不证明 04/28 的来源、候选分母或整日 Gate。

- [arXiv exact-v1](https://arxiv.org/html/2604.23467v1) §III Algorithm 1 与 §IV-A/C：已知短 shape 预捕获；未命中时本次 JIT 执行静态段，同时异步 capture，后续命中 replay；动态预处理与采样继续由 JIT 路径负责。§IV-C 还披露显式 CUDA event，§VI-A/B 披露 shape 膨胀与 cuBLAS 对 capture 并行的限制。因此正文的“完成事件确认后入 cache”是合理的执行安全约束，不声称论文给出跨流形式证明。
- §IV-E 与 Table II：H100、FP16、LLaMA-2 7B、batch 1、warm-start；表中 350/500-token 逐 token P99 分别是 18.90/23.68 ms，TensorRT-LLM 对应 16.53/16.65 ms。正文没有继承作者“所有长度最低”的断言，也没有将单卡每 token 测量外推到多并发整请求 SLO。
- 实际 [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md) 将此分支插在独立 kernel/CUDA Graph 与 persistent executor 之间，明确旧方案仍适用于稳定 shape、低重复率或显存紧张条件。新增一处 graph→设备端常驻队列的交接，避免从 JIT graph 突然跳到 Agent-generated megakernel。Ch48 的 proposal verification 和 Ch50 的 request-state serving engine 均未被本机制抢 owner；主 owner 仍是 `INFER-TENSORRT-LLM` 的 execution plan。
- 结论：actual source→actual body→adjacent flow 写后复核通过；未复现实验。仅单篇 Books Write-after PASS，04/28 仍未冻结分母、整日状态进行中。
