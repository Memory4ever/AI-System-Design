# 2604.24820v1 Salca：单篇有界证据与作者侧处置

仅处理 2026-04-29 V3 本窗的这一具名家族。官方 [exact-v1 HTML](https://arxiv.org/html/2604.24820v1) 与[版本页](https://arxiv.org/abs/2604.24820v1)；本日首公开归属仍依检查点所述公告、相邻 ID、DOI 代理的**联合批次链**，不以 v1 submitted 字段独证。未做跨版本史、全部附件或芯片复现。

## 准入、机制与 owner

§3.1–3.2、§4 的具体新设计压力是：长上下文 decode 即使选少量 KV，也必须付出全长 relevance 预扫、Top-K threshold 与不规则 HBM gather；仅减少 attention 算量可能让选择器和数据供给反居 critical path。作者在 prefill 从 Key 按绝对值汇总选稳定 heavy channels，decode 以 2-bit asymmetric Key/3-bit symmetric Query 估计分数，8-bit 分桶的 histogram threshold 只给**近似** Top-K，阈值桶 ties 会增加保留数；随后取原 K/V 算选中项上的精确 attention。硬件分级流水、score/index 缓冲、HBM 布局/冲突消减与实际带宽模型同一计划。这里“精确 attention”仅是**选中 KV 条目内**计算，不是完整 Context 的 dense attention 等价；heavy-channel、maxpool、阈值和稀疏预算均可能影响质量。

作者侧先拟 `Design Delta 2 + System Reach 2 + Durability 2 = 6` Standard。长期 owner 最可能是 Ch49 稀疏 Attention 的 selection→gather/kernel lowering；Ch45 保留 KV 物理 identity/有损 access plan，Ch54 保留 HBM 容量预算。现有 Ch49:720–727 已有 previous-step proposal＋验证的 **exact Top-K** 路线，1736 段有 index/selection/gather 融合原则，但尚未明确“近似 threshold 控制选择器/带宽代价，和 exact refinement 互为条件方案”及 ASIC 有效带宽约束。是否有足够稳定、非重复的最窄 Books 缺口待非作者 source→actual-owner 审查，当前不写共享章、不计 Integrate。小规模定制 ASIC 工作点并不因局部 hardware 方法自动排除，反之也不因 headline 倍率自动升为训练/Serving 全路径规则。

## 决定性实证与反证

- §5.1 Table3 使用 LongChat-v1.5-7B-32k、Vicuna-v1.5-7B-16k、ChatGLM3-6B-32k 的 LongBench；对 Loki 与本法在 1/4、3/8、1/2 特征稀疏中报告最优，Top-1024 平均保留 9.4%，不同模型的 maxpool 有/无也经选择。均值 Salca vs Full 分别 `35.15 vs 35.46`、`29.73 vs 30.52`、`50.35 vs 50.40`，不能说零质量损失或同一固定配置全模型成立；Vicuna 相对 Full 明显回退。作者 §4.4 设计点又取约 5.8% 最低保留，不等于 Table3 全部任务在该点质量通过。
- §5.2 的设计是 RTL+VCS **仿真周期**、TSMC 28nm 标准单元 **综合**估面积/核心功耗、Alveo U280 测相同访问模式的 HBM 功耗；A100 的 attention decode latency 用 `cuda.synchronize`，功耗用 NVML。Salca 1%/2% loss 对 dense GPU_D 的 2.81×/3.82× 和 51.11×/74.19× energy 是这一混合硬件协议的估计/对照，不是流片实测、同工艺 GPU 对比、全模型推理时延或生产请求 P95。作者的 ASIC_D 因单片 HBM2 512 GB/s 甚至低于 A100 五片 HBM2E 的 2 TB/s，说明代际/带宽基线不同。
- §5.3 Table6 的“至少 3.5× 超已有 accelerator”不是把 SOFA/FACT/Sanger/DOTA 在相同长上下文硬件上实跑。论文明确把短上下文吞吐按 query parallelism **公式折算**、假设 sufficient data supply，以乘法模型换算 HBM 功耗并添加 buffer 面积；作者也说直接验证 data-supply 对 LCS throughput 的影响不可行。其比较可作为设计模型候选，不能充当同一实验协议的实测排位。
- §3.2 的 histogram 约 `O(n+256)`，在固定 8-bit buckets 可写作线性；ties 的平均 0.19% 膨胀基于分数近似均匀分桶的经验，不是 adversarial/worst-case Top-K 容量保证。执行接近固定稀疏预算的前提是分数桶分布、maxpool、Key heavy channel 稳定与预扫能被后续 saved KV 读取摊销；失效时应回退 exact selector 或 dense attention，并用目标模型/上下文长度/硬件上的同质量端到端指标验收。

## 状态

与旧 V2.1 `3+2+3=8`、`Complete`、No Change 的结论分开。本项仍属于已审 106 篇中的 69 个**潜在线索**之一；上述为作者侧必要范围，尚无正式候选冻结、非作者 source→owner 核或日级 Gate。原文可作为受限算法—硬件协同案例，不证明另一芯片、更新 GPU 或并发 Serving 的一般优越。
