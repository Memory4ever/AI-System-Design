# RPS26498 actual POST重复修复PRE

Root实际POST定位旧同family正文（当前879–883）。作者已实际完整读868–893邻接；不是Source失效或重新准入，只恢复受影响Books组织。保持sole Ch56，未再写。拟撤回本次Admission后新78/80两段（还原预测margin→CALVO原交接），把既有RPS两段最小合并为以下三段，保留原FCFS合理条件/多模态HOL/顺序语义/严格arrival-order与离线或单模态共存、pipeline正确性/profile drift和全费用。本文末注仍只primary/证据/未核边界，不重复产生另一family注。

即使所有请求共享同一 MLLM，输入模态也会让 Prefill 前的 preprocessing、encoding 时间和显存需求相差数个数量级。FCFS 在纯文本服务时间相近时公平且简单；视频等重请求进入同一队列后却会同时占住 compute、encoder state 和 KV capacity，形成 head-of-line blocking。但资源等级不能由模态标签代替：长文本可能比短视频更重，同一图像在不同 encoder 与语言 backbone 上的费用也不同。一条单节点分支为 model–modality 建立隔离 profile，以预计 prefill latency 与 KV footprint 联合形成 resource classes，分类器、预处理与 engine 版本共同决定这一调度接口。<!-- source-family:SF-2026-ARXIV-2603-26498 -->

各资源队列内部保持 FCFS，再以动态优先级让轻量交互请求越过重请求；等待时间进入有上界的 aging 项，却不构成任意过载下重请求不可饥饿的证明。Class 只是一种 scheduling hint，不得改变 modality pipeline 或 request correctness；profile drift、误分类、aging 参数与多队列 starvation 都必须可观测。它用交互 TTFT 换取顺序语义和大请求尾延迟，离线吞吐、单一模态或严格 arrival-order 场景仍适合 FCFS/chunked prefill。<!-- source-family:SF-2026-ARXIV-2603-26498 -->

[RPS-Serve 的 vLLM 0.8.4、单 A100 对照](https://arxiv.org/html/2603.26498v1)中，直接按模态分级会误伤部分大请求；按资源分级能改善所测混合流的轻请求响应，却仍让较重请求承担延迟，在小 KV 预算下尤其明显。其 SLO 按无竞争 E2E 时间的倍数定义，不是固定生产期限；§3.1–3.7 的设计与 §4.1–4.4 的有限 request mix、memory pressure 不证明任意模态比例或生产负载同样改善。隔离 profiling、模型校准、重排/抢占与全部完成请求都计费；分布漂移、重请求公平性或总 goodput 不合格时，保留统一队列、保守 admission/EDF、rate limit 或物理隔离，不由轻请求 TTFT 批准全人口服务保证。<!-- source-family:SF-2026-ARXIV-2603-26498 -->
