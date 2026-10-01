# 2604.23467v1：动态图形捕获的必要证据与 Ch49 比较（作者侧）

本文件只处理一条已读完整题摘的贡献线索，不冻结 04/28 候选分母、首公开日或 Books 决定。材料身份为官方 [Hybrid JIT–CUDA Graph Optimization for Low-Latency Large Language Model Inference v1](https://arxiv.org/html/2604.23467v1)，以该 v1 的 §III–VI 为依据；页头 `25 Apr 2026` 是 submitted/稿件标示，不当 04/28 首公开时刻。历史 receipt 的 v1 Updated `2026-04-28T00:42:45Z` 早于本窗截止，但 DOI created `03:24:25Z` 在截止后；日期只能继续按官方公告槽、连续 ID、OAI 与例外组合核。

## 决定性机制与真实差异

§III Algorithm 1 / §IV-A 不是仅把 CUDA Graph 与 JIT 两个成熟词并列：启动时为序列长度 1–50 预捕获，运行中按长度命中 graph 时 replay，miss 时用 JIT 执行静态段并在另一 stream 异步 capture，完成后放入 rolling graph buffer、淘汰低使用项；动态预处理/采样留在 JIT。CUDA event 协调两 stream，cuBLAS capture 仍会部分串行。这个分支改变了 shape 变化时 graph cache miss 的责任：不是只有事前全预捕获、padding 或回退逐 kernel，而是可以让运行中 capture 更新缓存，代价是 miss 的首次成本、capture workspace、cache eviction 与双栈调试。

实际 [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md) 第 77 行及 1473–1497 行已明确 graph 只适合重复结构、shape proliferation、静态 capacity/padding 与 graph-cache miss；未具体承载 **miss 请求以 JIT 执行、后续同 shape 改为 graph replay** 的生命周期条件。若独立采用通过，主 owner 是 `INFER-TENSORRT-LLM`，只在 graph 与动态执行路径的邻段补这一窄条件；固定 shape/预捕获及独立 launch 仍应共存，不可写成完整 TensorRT–LLM 替代。

## 关键反证、分母与非证明项

- §IV-E / §V 是 LLaMA-2 7B、H100 94GB、FP16、PyTorch 2.3/CUDA 12.4、batch1、prompt 10–500、warm-start caching 的 1000 次运行；不含多租户、长 prefill、并发/队列、质量对照或服务 SLO。Table I TTFT 最短 10-token 为 13.36ms（TensorRT–LLM 16ms），500-token 为 17.79ms（TensorRT–LLM 88ms）；不同系统的端到端实现/预热和路径并非全部只差 capture 机制。
- §V-B Table II 的 P99 *per-token* 在短 generation 明显占优，但 350-token 时作者路径 18.90ms **高于** TensorRT–LLM 16.53ms，500-token 时 23.68ms **高于** 16.65ms；因此摘要/正文“最低尾延迟覆盖所有受测长度”及平均 20.2% 降低不能当无条件结论。它也不是 request-level P99。
- §V-C 报关闭异步 regeneration 后 TTFT +17.5%、dynamic JIT 改 Python 后 per-token +28%，可支持两个组件在受测配置下都有作用；未披露跨更高并发的控制实验。§VI-A/B 明确每个未覆盖长度仍需首次 capture、不同 shape 占显存，cuBLAS 可限制并行；不把 asynchronous 字面当 capture 与 compute 必可完全重叠。

作者侧贡献判断：确有与当前 Ch49 不同的运行时 graph-cache 更新条件，建议贡献准入并做非作者源→owner 校准；设计/范围/稳定性暂估 `2+1+2=5`。若确认长期知识缺口，按合同提升到深入审阅而**不改分数**；未通过独立校准、日期与写前 Gate 前不写共享 Books，也不在正式表计已 Integrate。
