# 2604.20105v1 EnergAIzer：有限非作者 Source→Owner 复核

- 复核者：apr02（不是 04/23 报告作者）；范围只含本家族必要方法、评价反例、Ch70 实际命题与相邻交接。未复现实验，也未审核 04/23 日期或全部来源。
- 原始材料：[arXiv exact-v1](https://arxiv.org/html/2604.20105v1) §III-B、§IV-A～C、§V、§VI-A/C/D/E；04/23 [作者审阅](./V3_EVIDENCE_REVIEW.md) 的 `2604.20105v1` 小节与此源在决定性机制上相符。页眉 04/22 不是首次公开证明，归属仍交日期 Gate。
- 实际 owner：[Ch70 成本](../../../../../books/part-06-ai-infrastructure/70-cost.md) 的资源时间/实际能耗分账、GPU Power Budget、默认频率参考曲线与“分析模型只作 what-if，发布仍须实测”段；Ch49 是 kernel 优化参数的上游，Ch56 是实际请求 SLO 的下游，不应另建论文收纳段。

## 裁决

`Design Delta 2 + System Reach 2 + Durability 2 = 6`、贡献准入与深入审阅方向通过。Ch70 现有参考曲线方案仍需新 workload 的默认频率观测；本文的可保留窄差异是：设计阶段尚不能运行目标 GPU 时，按 tile、swizzle、pipeline 推导 L2/DRAM 流量及 busy/lazy SM 活动，离线校准相位时延与模块功率系数，再将顺序 kernel 的预测合成为目标架构/频率的功率 *proposal*。同 latency 的两个 GEMM 微基准功率相差 96W，说明不能只用 FLOPs、总 bytes 或延迟替代此活动层；这是受控实例，不是生产请求普遍差距。现 Ch70 没有这一“结构化活动预测→真实仪表验收”的交接，故 `No Change — Existing Coverage` 不足，建议在 GPU Power Budget/Minos 参考曲线邻段加入两段窄机制与测量回退；不把作者估计器或误差数字当通用控制律。

必要边界：§IV-B/C 的 correction 与 `C` 均用 A100/A10 离线实测拟合，operator shape→kernel 参数还需离线决策树，故不是完全免 profiling；§VI-C 的 H100 6.7% 与 L40S 12.7% 是作者配置，L40S/GDDR6 已违反跨代相近每 bit/MAC 能效假设。§VI-E 排除并发/重叠 kernel、通信 kernel 与不规则稀疏；顺序单 GPU 预测不能签分布式推理总功率、多租户尾延迟或完整服务能耗。测量完整时原始 device/host 计量继续是成本与发布 authority，模型只能帮助排候选点；目标 GPU 能效、kernel layout 或并发超出校准时回退 target profiling/保守功率预算。未见当窗日期的独立公告证明，本复核不预记 Books 实写或整日 Complete。
