# 2026-04-27：22228 旧正文有限非作者写后复核

审阅者 apr02；仅审 [2604.22228v1](https://arxiv.org/html/2604.22228v1) 必要 §4–5/评价范围与 [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md)“单一路径 P2P 到可重放的多路径传输”实际正文及相邻交接，不复现实验、不签日级 Gate。

正文约 259–267 行的机制判断成立：把 GPU P2P payload 分片经 NVLink 与 host/PCIe 多路径传输，与 CUDA Graph 固化重复 copy/synchronization 的 host orchestration 收益分开；completion、buffer lifetime、capture 条件和旧路径回退均保留。官方 exact-v1 §5 在两台各四 GPU 的 Beluga/Narval 平台做 OMB 和 Jacobi；小消息、双向 host path、window/graph overhead 是真实反例，不支撑任意拓扑、collective 或端到端训练普遍加速。上下文从 contention-aware overlap 进入单条 P2P 多路径、再到 MoE All-to-Allv 的不同粒度，逻辑衔接适当。

但来源绑定标记有一处待修，故**暂不签完整 actual-body PASS**：`semantic-body-binding:SF-2026-ARXIV-2604-22228:start` 在约 263 行，`:end` 在约 271 行，越过本家族两段正文，包入后续 [2604.00317v1](https://arxiv.org/abs/2604.00317v1) NIMBLE 的 All-to-Allv 两段及其独立 source-family marker。这会把其他家族的机制误算作 22228 正文。只需在 Ch36 获得共享文件锁后把 22228 的 `:end` 移到它第二段之后、NIMBLE 段之前，不改机制论证；修后再做定点边界核。该缺口不否定 22228 论文机制及原段事实，但不能沿旧 V2.1 采用标签直接过当前写后 Gate。
