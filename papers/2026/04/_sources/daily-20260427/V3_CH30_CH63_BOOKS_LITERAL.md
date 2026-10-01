# 22127/22509：两项已获有限 source→owner PASS 的待写正文

这是作者供 root 协调共享章的最窄写前材料，不是 Books 实写、非作者写后或整日 Gate。[独立 source→actual owner 审阅](V3_APR20_TWO_22127_22509_INDEPENDENT.md)已核必要 exact-v1；两项仍须 root 确认文件锁与实际写后复核。

## 2604.22127v1 → TRAIN-LORA Ch30

**位置：**[Ch30](../../../../../books/part-04-training-system/30-lora.md)“Adapter Placement 也在控制知识获得与泛化边界”现有 early/middle/late 层位论证之后、“初始梯度只能提出 Adapter Placement”之前。现文把**层位**作为变量，还未把 hybrid block 的 recurrent/attention 组件类型及其串/并行数据流拓扑纳入 target-module identity。

> 对 hybrid language model，层位相同不代表可更新通路相同：串行 GDN→softmax 与并行 SSM+attention 的 recurrent/attention 组件承担不同前向路径，LoRA 的 target modules 应把组件类型和拓扑列为独立选择变量。可以先冻结 rank、确认 adapter 确实挂到预定模块，再分别测 recurrent-only、attention-only 与组合分支的 acquisition、跨任务迁移及原能力回归；不能因为某组件参数更多，就预判把更新放在那里更有效。<!-- source-family:SF-2026-ARXIV-2604-22127 -->
>
> 这种 placement 扩展会增加候选训练、模块发现与验证、adapter artifact 版本以及部署路径成本。Qwen3.5-0.8B 与 Falcon-H1-0.5B 在受限任务上的方向不同，提示拓扑可能改变有效选择，却没有在同等 trainable-parameter 预算、多 seed 和更大模型上隔离拓扑为唯一原因；部分比较的置信区间还跨零。故同预算/同执行成本与 held-out 迁移只是下一轮验收要求，不是该研究已完成的证明。收益不稳或接口不支持精确组件挂载时，回退已校准的全层/普通 attention LoRA 或 full fine-tuning，而不是把单模型 attention-only 排名写成跨架构定律。

**证据：**[官方 exact-v1](https://arxiv.org/html/2604.22127v1) §3.1–3.3/Table 1、§4.2–4.6/Table 3、§7；[独立核](V3_APR20_TWO_22127_22509_INDEPENDENT.md)指出同 rank 不同参数量、GSM8K Falcon `ssm_only .469` 虽高于 base `.383` 仍低于 `attention_only .555`，且部分 paired CI 跨零。上文的“同预算验收”是本书工程判断，不称论文已做。

## 2604.22509v1 → PLATFORM-GPU-SCHEDULER Ch63

**位置：**[Ch63](../../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)“Gang、Queue 与 Fairness”中 quota 借用/抢占成本之后、“GPU Sharing 的语义不同”之前；与后文 lease/reclaim 同属持续 allocation 决策，而非第56章 token scheduler。

> 静态 quota 与借用规则易于解释，却难把租户私有的当期 phase/SLO/迁移代价和运营方私有的供电、冷却、维护、拓扑压力同时写进可共享的输入。一个有条件的持续重议接口允许 tenant 提交对现有 allocation 的保留或放弃 proposal，operator 把物理约束投射为价格/回收压力并保有最终 match、transaction 和紧急硬约束仲裁权。价格在这里只传递受限资源压力，不授予 tenant 对设备的永久所有权，也不证明报价是真实效用或分配全局公平。<!-- source-family:SF-2026-ARXIV-2604-22509 -->
>
> 每轮重议会支付 profile、控制面通信、波动和 checkpoint/migration 成本，还可能使长作业难以预测。受限 trace/profile 模拟涵盖 LLM serving、分布式训练和 batch analytics，但 8–23% 是该租户 autoscaler/预算设置下的对照，不是生产云 A/B 或 request-tail SLO；高 reconfiguration cost 时原文也退近 FCFS。报价不可信、功率/故障必须立即处置或迁移不可承受时，仍由 operator 的硬安全、quota、lease 与保守 reclaim 路径裁决，不能用软价格越权。

**证据：**[官方 exact-v1](https://arxiv.org/html/2604.22509v1) §2.3、§4.1–4.5、§5.1/5.5、§7；[独立核](V3_APR20_TWO_22127_22509_INDEPENDENT.md)已对读 Ch63 现有 gang/quota/reclaim 与 simulation 限制。模型中价格接口的工程 admission 条件属本书推断，原文未证明 strategy-proofness 或隐私保证。
