# AI Infra 面试：逐周 Checklist

本文件是 [`16-week-plan.md`](./16-week-plan.md) 的执行记录。每次只推进一周，验收证据可供 Review 后，才能勾选当周完成状态。

## 每周固定要求

- [ ] 记录本周计划时间和实际投入时间。
- [ ] 完成 4 道精选 Coding 题和 1 次限时练习。
- [ ] 分别完成 1 次中文和英文技术讲解。
- [ ] 完成 1 次 System Design 或项目深挖练习。
- [ ] 将代码、配置、原始测量结果和结论放在一起。
- [ ] 记录错误、未解决问题和下一项修正行动。
- [ ] 使用官方文档或 primary source 核验版本敏感结论。
- [ ] 不记录缺少 workload 和环境条件的性能数字。

## 第1周：岗位与能力基线

- [x] 收集 AI Platform、LLM Serving 和 Distributed Training 三类岗位的 30 个代表性 JD（见 [第1天 JD 样本](./week-01/day-01-jd-collection.md)）。
- [ ] 将要求分类为共同底座、岗位专项、Senior 信号或 Staff 信号。
- [ ] 按面试影响和证据缺口，整理十大能力差距。
- [ ] 盘点本地 GPU、driver、CUDA、container、Kubernetes 和 profiling 能力。
- [ ] 完成 1 次 Coding 基线 Mock 和 1 次 AI System Design 基线 Mock。
- [ ] 在 Mock 前不突击复习，如实记录基线分数和失败主题。
- [ ] **第1周完成：**岗位矩阵和基线证据已 Review。

## 第2周：GPU 与 CUDA 基础

- [ ] Review GPU execution、memory hierarchy、transfer path 和 Roofline。
- [ ] 在每张可用 GPU 上运行 device inventory 和显存带宽测试。
- [ ] 对比至少两种访存或数据传输模式。
- [ ] Profile 测试过程，区分 launch、compute、memory 和 transfer 时间。
- [ ] 用中英文解释为什么仅看 GPU utilization 不足以判断性能。
- [ ] **第2周完成：**benchmark 可以复现，瓶颈判断有 profiler 证据。

## 第3周：模型机制与 Runtime State

- [ ] 重新推导 Attention、causal mask、MHA/GQA/MQA 和 KV shape。
- [ ] 实现模型权重、KV bytes 和 context capacity 计算器。
- [ ] 为不同 layer、head、precision 和 sequence 配置添加测试。
- [ ] 解释 MoE 总容量、active parameters 和 All-to-All 成本。
- [ ] 解释 accepted context length 为什么不等于 effective context utilization。
- [ ] **第3周完成：**不看笔记也能重新推导公式和 shape。

## 第4周：Communication 与 NCCL

- [ ] 分开 Review collective semantic、algorithm 和 transport。
- [ ] Benchmark AllReduce 和至少一种其他 collective。
- [ ] 扫描不同 message size 和参与 GPU 数量。
- [ ] 计算 effective bandwidth 和 scaling efficiency。
- [ ] 解释 ring/tree 的 trade-off 与 topology sensitivity。
- [ ] **第4周完成：**通信建议明确说明 tensor shape、topology 和 latency/bandwidth 区间。

## 第5周：Distributed Training 策略

- [ ] 运行小型 DDP 训练任务，并核验 global batch 计算。
- [ ] 增加一种 state sharding 或 model parallel 实验。
- [ ] 测量显存、step time、通信和 scaling efficiency。
- [ ] 按各自切分的状态比较 DP、TP、PP、ZeRO、CP 和 EP。
- [ ] 完成一次 Training Cluster System Design。
- [ ] **第5周完成：**并行策略来自书面预算，而不是框架偏好。

## 第6周：训练恢复与 Runtime

- [ ] 保存并恢复 model、optimizer、scheduler、RNG 和 data cursor state。
- [ ] 在声明的容差内比较恢复训练和不中断训练的轨迹。
- [ ] 注入一次 worker 或 process failure。
- [ ] 记录故障检测、恢复、replay 和一致性行为。
- [ ] 撰写一份训练事故深挖材料。
- [ ] **第6周完成：**恢复语义和未提供的保证均已明确。

## 第7周：Inference 基线

- [ ] 使用 vLLM 或 SGLang 部署一个模型。
- [ ] 构建或采用可复现的 workload generator。
- [ ] 测量 TTFT、TPOT、request throughput、token throughput 和 goodput。
- [ ] 扫描 prompt length、output length 和 concurrency。
- [ ] 解释 Prefill、Decode、admission、streaming 和 completion state。
- [ ] **第7周完成：**基线报告包含分布和 percentile，而不只有平均值。

## 第8周：Inference 优化

- [ ] 在至少两种 workload mix 下测量 batching policy 的影响。
- [ ] 构造可控的 KV capacity 压力并观察 admission/eviction。
- [ ] 评估一种 speculative、prefix reuse 或 cache offload 机制。
- [ ] 区分 scheduling、memory 和 serial execution 优化。
- [ ] 记录一种会损害其他指标或 workload 的优化。
- [ ] **第8周完成：**每项优化都有收益、边界和新增技术债。

## 第9周：Serving Runtime 内部机制

- [ ] 追踪一个请求经过 API、scheduler、KV manager、worker 和 stream 的过程。
- [ ] 定位对应源码模块与 Runtime State transition。
- [ ] Profile 一个代表性请求或 batch。
- [ ] 完成第一次 AI Systems 技术 Mock。
- [ ] 完成一次 10 分钟英文 Runtime 讲解。
- [ ] **第9周完成：**Engine 解释不局限于 PagedAttention 或单个 scheduler 特性。

## 第10周：分布式与解耦推理

- [ ] 建模 aggregated 和 PD-disaggregated 架构的资源需求。
- [ ] 实现双进程或单机 PD 模拟。
- [ ] 测量或计算 KV transfer volume 和 break-even condition。
- [ ] 比较 routing、placement、transfer、recovery 和 autoscaling 影响。
- [ ] 标注所有仍需多节点验证的结论。
- [ ] **第10周完成：**部署建议绑定 workload 和 SLO。

## 第11周：AI Platform Control Plane

- [ ] 连接 model identity、Evaluation evidence、deployment revision 和 Runtime configuration。
- [ ] 通过 KServe 或同类声明式 control path 完成部署。
- [ ] 配置 Gateway routing、canary 和 rollback。
- [ ] 追踪 desired state 从 API 到 Serving worker 的路径。
- [ ] 完成一次 AI Platform System Design。
- [ ] **第11周完成：**Control plane、data path 和 artifact ownership 相互独立。

## 第12周：GPU Scheduling 与 Multi-tenancy

- [ ] 定义 queue、quota、priority、fairness、locality 和 gang requirements。
- [ ] 使用 Go 实现一个有实际意义的 scheduler policy 或 controller。
- [ ] 在资源争用条件下测试确定性行为。
- [ ] 测试 starvation、preemption、partial allocation 和 recovery 场景。
- [ ] 通过 event、log 或 metric 暴露策略决策。
- [ ] **第12周完成：**策略正确性可以测试并观测。

## 第13周：证据与生产治理

- [ ] 定义发布 SLO 和 Evaluation gate。
- [ ] 针对一个请求或故障关联 metrics、logs 和 traces。
- [ ] 根据实测 workload 数据构建容量和成本模型。
- [ ] 完成 tenancy 与 security threat model。
- [ ] 定义 canary、rollback 和 evidence retention policy。
- [ ] **第13周完成：**一个发布决策可以端到端追溯。

## 第14周：Capstone 集成

- [ ] 从干净环境跑通完整的 Training-to-Serving 路径。
- [ ] 执行 load test 并保留原始结果。
- [ ] 注入至少一种 compute、process 或 control plane failure。
- [ ] 修复并重新测量一个真实瓶颈。
- [ ] 完成 RFC、ADR、architecture diagram、benchmark 和 incident report。
- [ ] 邀请不了解实现细节的 Reviewer 复现或挑战结论。
- [ ] **第14周完成：**Capstone 可以被独立 Review。

## 第15周：面试压力测试

- [ ] 完成 1 次限时 Coding Mock。
- [ ] 完成 1 次 AI 深度与源码路径 Mock。
- [ ] 完成 1 次定量 System Design Mock。
- [ ] 完成 1 次全英文 Behavioral / Project Mock。
- [ ] 按根因聚类所有失败，而不是逐题修补。
- [ ] 重新测试影响最大的两个薄弱点。
- [ ] **第15周完成：**重复失败主题已经关闭或明确接受。

## 第16周：Portfolio 与投递门禁

- [ ] 从干净环境复现 Capstone setup、测试和 benchmark。
- [ ] 完成中文和英文简历。
- [ ] 完成 8 个双语 Senior-to-Staff 故事。
- [ ] 完成 12 份 System Design 和精选问题库。
- [ ] 根据代码、证据或明确标注的生产结果核验每项简历结论。
- [ ] 按匹配度、价值和面试风险排列目标公司与岗位。
- [ ] 完成最终 Coding、System Design、AI 深度和英文 Mock。
- [ ] **第16周完成：**主计划中的全部就绪标准均已通过。

## 最终统计

- [ ] 完成 64 道精选 Coding 题。
- [ ] 完成 16 次限时 Coding 练习。
- [ ] 完成 12 份 AI System Design。
- [ ] 完成 8 个双语 Senior-to-Staff 故事。
- [ ] 完成 8 次 Mock Interview，其中至少 4 次全英文。
- [ ] 四类 Labs 均可独立运行。
- [ ] 一个端到端 Capstone 可复现且有证据支持。
- [ ] 正式投递材料已经就绪。
