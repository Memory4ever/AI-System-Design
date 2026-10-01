# 04/28 arXiv 贡献准入：第三批前十项

本批是旧 V2.1 `retained` 队列的第 61–70 个身份 `2604.23711`～`2604.23887`，逐项重读已有 `arxiv-owner-replay-20260903/20260428/arxiv-owner-receipt.json` 的完整标题与摘要。旧 `/9`、Books 决定和缓存版本均不作正式依据。“继续”只表示题摘显示可能改变长期机制/评价合同，尚非冻结候选；须核官方 exact-v1、公告归属、主要反证和当前 owner。此处没有把 ten papers 全送全文。

| ID | 题摘判断 | 具体理由 / 最小后续 |
| --- | --- | --- |
| 2604.23711 | 继续核贡献 | 单/少查询从 Agent 当前上下文记忆抽取隐私与传统训练数据泄漏对象不同，可能改变 memory-to-output 防护边界；但摘要的黑/灰盒混用、仅模型拒绝与检测基线不足以证明架构性突破。需核实际注入权限、secret 可见性、每 query 泄漏分母及 Ch72 既有 effect/output guard。 |
| 2604.23747 | 继续 | 指出 DeepSpeed CPU-offload 梯度累积丢 micro-batch、OpenRLHF mini-batch loss 聚合错权重，使 mixed-policy vs SFT→RL 排名受坏基线污染；这是训练比较的可复现性合同而非单新 optimizer。需核 exact affected versions、补丁与同预算实验，禁止把修复后两个受测模型上的优势写成所有 mixed-policy 皆劣。 |
| 2604.23758 | 前分母关闭 | 超导体发现中原子模型、LLM 语义决策、实验合成具有领域科学价值，但核心证据是材料候选与四个实验合成，不是本阶段大模型或模型 Infra 的状态/控制/评价新合同。AI for Science 当前暂不进入主线，不借“Agentic”字样入选。 |
| 2604.23775 | 前分母关闭 | VLA safety 训练/推理攻防 timing taxonomy 汇集威胁与开放议程；摘要未提供独立攻击机制、控制实验或改变已有机器人 safety/runtime owner 的新实施边界。保留可作为发现线索，不把 survey 当技术结论证据。 |
| 2604.23781 | 继续 | 多日外生环境更新、五个有状态沙箱与执行后 1537 个确定性 checker，使 `weighted progress 75.8` 与 strict Task Success `20.0%` 分母分离；可能补 Ch66 静态 episode 对长期 Agent 的失效边界。需核任务生成/外生更新真实性、checker 覆盖、对五服务之外的限制及现有 outcome-witness 章节。 |
| 2604.23798 | 继续核贡献 | FP32 exact-softmax 的结合 scan 把顺序在线 update 转为对数并行深度、避 Tensor Core，可能对 edge/FP32 的 kernel 路径产生独立分支；但摘要跨 A100/Jetson/BERT/LLaMA offload 的吞吐口径混杂。需核真实数值误差界、并行 work/额外内存与同精度同 shape 基线，若只属受限 kernel microbenchmark 不进 Books。 |
| 2604.23831 | 前分母关闭 | Jetson 上 MobileNetV2 CPU-FP32 vs GPU-TensorRT-FP16 的加载时延与准确率不同维度，显示 timing safety 要单独检查；但模型、precision、runtime 与 execution path 同时变动，不能把 7.2×/周期违约归因于“隔离”单变量。医疗器械法规类比也不改变本项目大模型 Infra 的新机制；不采用监管解释。 |
| 2604.23838 | 继续 | RL pipeline Sub-Stage Graph 将 stage 内/跨 worker 不均衡、长尾 rollout 迁移与异构管线图调度合一，可能改变常规同步/异步 trainer 的资源调度所有权。需核 4–64 H100/A100 的通信、配置、rollout 收敛/质量与 vLLM/verl 基线是否等预算，不从最高 1.85× 推全负载。 |
| 2604.23853 | 继续核贡献 | trace step 成本归因后把蒸馏 skill patch 分成 preserve/prune/repair，观察聚合省成本为零、质量退步都来自 preserve，是“规则类型”而非单技能平均效果的反证；可能补 Ch66/84 skill evaluation 责任。需核 30 held-out 两 seed 与84-task transfer、patch 选择/可复核原始轨迹及现有 typed-skill 章节；不因发布 schema 就默认新机制。 |
| 2604.23887 | 前分母关闭，定点查漏 | 模型自保护策略被 adaptive attacker 攻破而独立应用代码输出过滤 15k 次零泄露，是已有“模型不是权限边界，effect/output gate 应独立”的受限实例。输出规则可否防止工具前已发生的 secret exfiltration 未证；不把零观察泄漏当普遍安全保证。仅定点对读 Ch72 若当前正文遗漏“输出过滤晚于工具 effect”反例再重开。 |

本批为 **3 项继续、3 项继续核贡献、4 项前分母关闭**；六项开放线索并非已冻结候选，也非六项都需全文审读。
