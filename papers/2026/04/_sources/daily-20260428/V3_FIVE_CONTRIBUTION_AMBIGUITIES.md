# 04/28 五项“继续核贡献”的有界消歧（作者侧）

本记录只处理旧 111 身份中已读完整题摘、但仍标为“继续核贡献”的五项。重新核官方 `abs/...v1` 的题名、完整摘要与版本身份；已有 owner 比较只用来指出需要验的具体差异，不沿用 V2.1 分数或 Books 结论。以下“准入”指**贡献准入作者提案**，还须非作者校准、官方公告归属、相应层级的必要证据和 Books 判断；投稿日不是公开日。五项没有新增共享 Books 写入。

| Source Family | 作者侧贡献判断 | 具体增量及必要证据边界 |
| --- | --- | --- |
| [2604.23467v1](https://arxiv.org/abs/2604.23467v1) | 准入待独立校准；Ch49 | 既有 CUDA Graph 静态形状优化在短交互序列的形状变化下需要 JIT 回退；v1 的静态 replay / 动态 JIT 分区与异步捕获、运行中复用构成具体缓存更新分支，值得核验 cache miss 与 shape 覆盖何时优于纯预捕获。证据只有 LLaMA-2 7B、单 GPU、batch=1、prompt 10–500 token；TTFT/P99 不能外推多租户、同精度全链或服务 SLO。 |
| [2604.23577v1](https://arxiv.org/abs/2604.23577v1) | 准入待独立校准；Ch56 | Ch56 已有模型路由的在线成本反馈，但 v1 把升级失败按任务簇收集、定向蒸馏便宜 tier，再回训 router，形成服务失败样本→模型能力边界更新→路由分布更新的闭环；这不只是三个模块并列或另一个 router。需以 §method/8 周约 5k queries/day pilot 的 acceptance、人工评价、同预算 untargeted distillation 和端到端成本分母审阅；58%/p99 的受测结果不成为全流量保证。 |
| [2604.23932v1](https://arxiv.org/abs/2604.23932v1) | 准入待独立校准；Ch36 | 跨 DC LLM 训练中的长 RTT/OTN 与常规 RDMA credit 节奏失配；v1 的分段 long-haul 流控、源/目的 OTN 速率匹配及 pseudo-ACK 形成具体传输控制分支，需要与 Ch36 collective completion 和故障回退分开审阅。只有四页作者稿与模拟结果，最高 20×/buffer −62.7% 不能直接作实际训练吞吐、收敛、WAN 故障恢复或 NIC 部署收益。 |
| [2604.24542v1](https://arxiv.org/abs/2604.24542v1) | 准入待独立校准；Ch67/72 owner 待定 | 当前第三方模型缺 clean reference、trigger 与可改权重时，v1 以每层 hidden-state 差的 shrinkage Mahalanobis 加 200 个 clean 校准例作 runtime health sensor。这是可检验的 artifact 观测条件变化，非“安全监控”主题映射。须把 detector FPR 12–16%、各攻击机会集、模型可见 hidden states 与外部阻断器分开；92–100% DAN、GCG 较弱不证明统一阻断或未知攻击安全保证。 |
| [2604.24579v1](https://arxiv.org/abs/2604.24579v1) | 准入待独立校准；Ch66 | 现有 pass@k/pass^k/RDC 作为各自标量会隐去成功时间分布；v1 从 Agent trace 拟合吸收 DTMC，并以一阶到达分布、区间与 50/50 fit/test 对照把这些指标放回同一 estimand，是具体评价有效性分支。状态聚类、AIC/KS 与 Laplace/Dirichlet 假设仍须查；七个受控框架、KS `p>0.05` 仅未拒绝拟合，不证明链是真实执行机制或可外推线上 Agent。 |

这五项只解决贡献事实是否足以进入证据审阅，不触动既有 70 开放/41 拟前关工作口径；将其中五个“继续核贡献”从**作者侧歧义队列**转入**待独立准入与证据队列**，并不自动增加冻结评分分母。独立审阅如发现与 Ch49/56/36/67/72/66 的具体机制已完全等价，可按合同改判，须保留上述事实和改判原因。
