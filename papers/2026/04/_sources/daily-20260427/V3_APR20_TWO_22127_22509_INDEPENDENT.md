# 04/27 两项 source→实际 owner 有界非作者复核

复核者：apr20_resume；作者：apr01。仅核 `2604.22127v1`、`2604.22509v1` 的决定性官方方法/评价/反证与 Ch30/Ch63 现有正文相邻命题。本文件不签 04/27 首公开日期、十四来源、候选分母、整日 Gate；未修改正式日报或 Books，写前通过也不等于写后通过。

## 2604.22127v1 — Where Should LoRA Go?

**有限 source→Ch30 采用 PASS，限窄条件分支。**[官方 exact-v1](https://arxiv.org/html/2604.22127v1) §3.1–3.3 确实对串行 Qwen3.5-0.8B（18 GDN/6 softmax）与并行 Falcon-H1-0.5B（Mamba2/attention 同块）按组件构造 target modules，固定 `rank=16`；Table 1 trainable 参数预算**不相等**，所以 §4 Table 3 的方向差不能称同参因果识别。GSM8K 域里 Qwen `gdn_only .148` 对 base `.297`，Falcon `ssm_only .469` 对 base `.383`，但 Falcon `attention_only .555` 更好；Qwen `softmax_plus_mlp .148` 也显示“多放一组”并非单调获益。§4.6 paired bootstrap 只覆盖 UltraChat 有逐实例配对的比较，Falcon attention-vs-all GSM8K CI `[-1.2,+12.9]` 跨零，ssm-vs-attention 各 CI 也跨零；§7 单训练 seed、两 sub-1B family、固定 rank、有限域/任务与 PEFT 方法。

实际 [Ch30](../../../../../books/part-04-training-system/30-lora.md) §「Adapter Placement 也在控制知识获得与泛化边界」已承载 early/middle/late 层位、acquisition/transfer、安全回归和 full-stack 回退，下一节「初始梯度只能提出 Adapter Placement」已承载 proposal sensor 非因果真值；但这两处没有把 **recurrent/attention 组件类型与串/并行数据流拓扑**列为 target-module identity 的独立选择变量。故作者拟于原 placement 主线增加机制条件，而不是增论文摘要或声称拓扑唯一原因，是真实最窄知识增量。写入必须把同 budget、held-out 质量/迁移、执行成本当**未来验收要求**，不可伪称论文已经完成同预算控制或多 seed 证明；小模型不是硬拒，受限外推必须明说。2+2+2=6 / Deep 因真 gap 成立。

## 2604.22509v1 — LaissezCloud

**有限 source→Ch63 采用 PASS，限 public-cloud 跨信任域持续合约。**[官方 exact-v1](https://arxiv.org/html/2604.22509v1) §2.3/§4.1–4.5 确实从 launch-time on-demand/spot 推进到运行中可争议的单实例 ownership：tenant 用自身 phase/SLO/迁移成本形成 bid、retention limit 或 relinquish；operator 的 InfraMaps 将私有 power/cooling/maintenance/topology 约束投射成 floor price、reclaim pressure 与 volatility 控制；中心 match/transaction 仍有唯一资源 owner。它不是把价格变成授权、真实效用或全局公平证明。§5.1 的 Azure LLM serving trace + Dynamo Planner、Sailor 分布式训练、batch analytics 是 trace/profile-driven 模拟；`8–23%` 是该受限同租户 autoscaler/预算下 performance-retention 退化改进，不是生产云直接 A/B 或端到端通用收益；§5.5 高重配置开销可退回 FCFS 近似，§7 明示非 strategy-proof/privacy guarantee，紧急物理约束仍需 operator 强制迁移/限电。

实际 [Ch63](../../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md) 核心和 §「Gang、Queue 与 Fairness」已经规定 topology/gang feasibility、quota 借用、reclaim/checkpoint/KV/SLO、operator policy 与 fixed quota 回退；章末 reclaimable sharing 再规定 entitlement deficit、lease、interference。尚无租户私有 utility 与运营方私有物理约束经**窄价格接口持续重议既有 allocation**而不泄露各自内部状态的控制面分权。故作者提出在 quota/reclaim 邻接处写条件分支有实际 gap，2+2+2=6 / Deep 因真 gap 成立。写入要保 tenant proposal vs operator 仲裁/硬安全、价格波动与非价格回退，不把模拟数字写成生产 SLO 保证。

两项均仅 source→owner 写前 PASS；仍需 root 协调共享章锁、作者真实正文整合、不同非作者的 actual write-after 核验，才能计 Books `Integrate`。本有限审阅未执行 04/27 日级独立 Gate。
