# 2603.08797 — DAG 质量预算与 GPU 分割联合配置

root 实际读取 [JigsawServe exact-v1](https://arxiv.org/html/2603.08797v1) §3.1–3.3/Eq1–14、§4设置、§5/5.1与§7；未核全图像、代码或复现。完整题摘/current 无撤回复用 SUP_EXACT_BATCH4.json。arxiv.content/findable registered Mar11UTC01:58:10 与本日官方公告下界同 BJT03-11夹证；HCDS2026正式日程为未来Mar23，投稿/通知日不是全文首公开，不另推此前 workshop 正文。

Score 2+2+2=6，具体质量非等价 portfolio 差额深入。Owner PLATFORM-GPU-SCHEDULER/Ch63；实际189–210固定shape→语义等价portfolio完整段及共享/MIG边界，Ch62/64入口已读。当前分工不能直接承载不同精度的variant和DAG全路径延迟/质量联合约束；不是重写LLM调度或新增owner。

每task注册variant、DAG、端到端latency/相对最高精度quality；离线profile(task/variant/batch/MIG/MPS)的p95和throughput，runtime更新，MILP选择variant和slice、MIG bin-packing部署。同slice至多4个MPSworker。路径sum(2×local p95)是排队近似，不是联合尾分位证明；PAS将异质task accuracy相乘，作者明确heuristic，不是校准后的端到端正确率。fanout用此前5时间点估计，也不能签硬SLO。

实际4×H100SXM80GB/96CPU/1007GiB/Ubuntu22.04/CUDA12.4/torch2.6/Python3.10，三个depth1–3图像/检测/字幕/TTS组合，非自回归LLM fleet。COCO/Bellevue与Twitter五分钟均值trace缩放至最优系统容量；每个时间点短稳态试验不是连续重分割全过程。11.3×属120GPU analytical，不当4GPU实测。平均43.3%slices/.6%miss只限其协议；drop计miss，但低负载预测误差仍可抬miss。Depth1任务预算无收益、部分配置等同A+S，是共存边界。

离线profile7–12小时，MILP2–20秒，MIG重分割停服务；额外GPU无中断切换是前作/未来部署可能，不是本实现已验。precision、完整输入输出长度/每模型batch/concurrency明细未统一披露；不签LLM端到端tail或真实体验保证。§7实际体验、非DAG、多GPU模型、通信/memory瓶颈与理想packing仍未来。

## 逐字 PRE，待独核

在 Ch63 语义等价 portfolio 完整段后、DRA 前插入单段：

> Compound inference 还可能把模型质量纳入配置选择：不同 task 的 variant 并不语义等价，只有 workload owner 明确允许质量退让，资源 optimizer 才能沿 DAG 路径联合分配 latency、variant 与 MIG/MPS 配置。此时“选更多小 slice”必须与整条路径的输出质量一起验收，而不是把每个 task 的局部最优相加。[有限 GPU 对照](https://arxiv.org/html/2603.08797v1)用局部 p95 和 task-accuracy 乘积作预算代理；异质指标的乘积不是校准后的端到端正确率，局部尾延迟之和也不证明联合尾 SLO。离线 profiling、求解、共享干扰和停机重分割均有成本，逐时间点稳态试验不代表连续线上迁移，也不授自回归 LLM 或多 GPU collective 的性能。质量不可组合、需求预测失配或重配置不能 drain 时，应保留固定 variant/shape、独立端到端评价与更保守的资源预留；scheduler 只执行已批准的配置，不自行取得质量降级权限。<!-- source-family:SF-2026-ARXIV-2603-08797 -->

mar12_independent_continue 非作者实际必要 Source/date、owner与逐字 PRE 通过；root 窄写 Ch63 portfolio 完整段后单段及本人末注，该 reviewer 实际顺读完整邻接、新段和本人末注并回对精确原证与 PRE，POST 通过。原块保留，窄锁释放；未授 DAY。
