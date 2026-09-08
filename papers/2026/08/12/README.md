# Daily Research — 2026-08-12

**规范：** V3
**窗口：** 2026-08-11T09:00:00+08:00 ～ 2026-08-12T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-08T00:03:21+08:00

## 1. 结论

本窗 14 个每日来源均已检查。arXiv 官方公告批次跨分类去重后有 516 个身份，逐项完成标题语义判断，并对模糊或高信号条目读取完整摘要；独立复核重开高信号题摘范围后，将候选分母由 18 修正为 32 项。候选集中在表示的可干预性、长上下文架构、Agentic RL 与混合 rollout 调度、KV 传输、训练故障定位、量化与 MoE、World Model / VLA、Agent 身份委托及供应链故障。

30 项完成当前 v1 HTML 深入审阅，2 项完成标准审阅，全部检查 withdrawn；7 项已有 Books 覆盖，22 项长期增量已写入对应 owner，3 项因证据不足以形成稳定长期机制而仅保留日报。独立写后审计确认 22 个 marker 唯一、语义绑定和 canonical owner 正确，正文均位于 Review notes 之前；其中 SALT 的表述已收紧为“语言重建约束 action token 的语义对齐”，不把单个 token 外推为天然人类可读动作。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 归档按日期检查 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 日期列表检查；劳动力 retraining 经济研究不改变本项目系统 contract，准入前排除 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind / Google Research 发布目录按日期检查 | 已检查 | 无 |
| SRC-META-AI | FAIR publication 列表按日期检查 | 已检查 | 无 |
| SRC-QWEN | 官方文章目录按日期检查 | 已检查 | 无 |
| SRC-DEEPSEEK | 官网研究与更新目录按日期检查 | 已检查 | 无 |
| SRC-MOONSHOT | 官方 Blog 与公开仓库发布入口按日期检查 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Research“全部”目录；ELR 日期冲突沿用前一日隔离，不重复请求 | 受阻 | 同一去重材料请求见 §5 |
| SRC-ZAI | Research 日期目录按日期检查 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Research、Blog、Publications 按日期检查 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 技术博客与仓库发布入口按日期检查 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | Paper / Blog 与官方仓库按日期检查 | 已检查 | 无 |
| SRC-MINIMAX | Research / Blog 按日期检查 | 已检查 | 无 |
| SRC-ARXIV | 相关分类官方新公告跨分类去重 516 项；逐项题摘筛选并经独立高信号漏项复核，冻结 32 项；候选 v1 均可访问且未 withdrawn | 已检查 | 无 |

没有其他按需来源被触发。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Decodable But Not Detachable](https://arxiv.org/html/2608.10214v1) | 2026-08-12T08:00:00+08:00 | 区分表示可解码与参数子集可因果拆卸，并把模块性绑定到训练数据粒度；3 + 2 + 3 = 8 | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION`，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Similarity Gates Approve Reversals](https://arxiv.org/html/2608.10216v1) | 2026-08-12T08:00:00+08:00 | 用匹配反事实证明余弦相似度不能单独承担语义等价 release gate；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Cracks in the Foundation](https://arxiv.org/html/2608.10296v1) | 2026-08-12T08:00:00+08:00 | 控制变量说明长上下文能力是多项架构选择复合后的系统属性；3 + 2 + 3 = 8 | 深入完成 | 整合：`MODEL-LONG-CONTEXT`，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [MemSpec](https://arxiv.org/html/2608.10362v1) | 2026-08-12T08:00:00+08:00 | 将 draft 选择与可驻留 working set 分离；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING`，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [TideRL](https://arxiv.org/html/2608.10402v1) | 2026-08-12T08:00:00+08:00 | 用 rollout readiness、可恢复状态与弹性 rank 调度改善 agentic RL goodput；3 + 3 + 3 = 9 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Continuous Interaction Diffusion](https://arxiv.org/html/2608.10438v1) | 2026-08-12T08:00:00+08:00 | 提出 denoising 内的异步只读工具通道与 typed thought state；3 + 2 + 2 = 7 | 深入完成 | 仅报告：无实证 performance claim，暂不沉淀为稳定机制 |
| [Dependency-Guided Rollback Repair](https://arxiv.org/html/2608.10502v1) | 2026-08-12T08:00:00+08:00 | 沿 memory→claim→action dependency 失活污染状态并选择性重放；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [MAP-Graph](https://arxiv.org/html/2608.10509v1) | 2026-08-12T08:00:00+08:00 | 把 provenance、permission、path trust 与 action risk 变为共享记忆控制信号；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [ImpactHO](https://arxiv.org/html/2608.10545v1) | 2026-08-12T08:00:00+08:00 | 将多用户部分 KV 传输表述为有最低效用锚点的准入与带宽分配；3 + 3 + 2 = 8 | 深入完成 | 整合：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [MOSAIC](https://arxiv.org/html/2608.10605v1) | 2026-08-12T08:00:00+08:00 | 将 scaling law 与 MFU、通信、内存和并行布局联合求解；3 + 3 + 3 = 9 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Load Hijack](https://arxiv.org/html/2608.10614v1) | 2026-08-12T08:00:00+08:00 | router checkpoint 可被触发成设备级 straggler 调度器；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Decomposition-Induced Context-Memory Conflict](https://arxiv.org/html/2608.10627v1) | 2026-08-12T08:00:00+08:00 | 证明任务分解本身可能把来源事实替换成稳定的参数记忆；3 + 2 + 3 = 8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [REDAgentBench](https://arxiv.org/html/2608.10669v1) | 2026-08-12T08:00:00+08:00 | 用 service receipt 与最终状态区分暴露、执行、观察和裁决；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Enterprise MCP Authorization Gateway](https://arxiv.org/html/2608.10760v1) | 2026-08-12T08:00:00+08:00 | 将 user/service persona、credential ownership 与 OAuth delegation 明确成 MCP policy boundary；3 + 3 + 3 = 9 | 深入完成 | 整合：`AGENT-MCP`，[Ch83](../../../../books/part-07-agent/83-mcp.md) |
| [MoE Proxy Models](https://arxiv.org/html/2608.10823v1) | 2026-08-12T08:00:00+08:00 | 用结构保持的 expert pruning 低成本复现 RL post-training 故障；3 + 2 + 2 = 7 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SCOUT](https://arxiv.org/html/2608.11034v1) | 2026-08-12T08:00:00+08:00 | 用副本等价性、带外观察与原位 replay 定位分布式预训练故障；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-MONITORING`，[Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [Catastrophic Remembering](https://arxiv.org/html/2608.11095v1) | 2026-08-12T08:00:00+08:00 | 指令缺少 rationale 时删除验证成本爆炸，导致 prompt 单向膨胀；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`AGENT-PROMPT`，[Ch74](../../../../books/part-07-agent/74-prompt.md) |
| [Workload-Aware Mixed RL Rollout Scheduling](https://arxiv.org/html/2608.11152v1) | 2026-08-12T08:00:00+08:00 | 将 session admission 视为 KV 容量承诺，以 footprint×residency 管理混合 rollout；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；handoff：Ch36 |
| [The Multilingual Quantization Tax](https://arxiv.org/html/2608.09941v1) | 2026-08-12T08:00:00+08:00 | 证明量化 release gate 必须按语言与 typology 切片，而不能由总体平均替代；3 + 2 + 2 = 7 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [4D-WAM](https://arxiv.org/html/2608.10107v1) | 2026-08-12T08:00:00+08:00 | 用几何 teacher 约束预测视频的深度与时序世界状态；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Procedural Fairness in RLHF](https://arxiv.org/html/2608.10126v1) | 2026-08-12T08:00:00+08:00 | 将偏好聚合的群体身份、过程公平与结果效用分开验收；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`TRAIN-RLHF`，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Reproducing LeWorldModel](https://arxiv.org/html/2608.10145v1) | 2026-08-12T08:00:00+08:00 | 暴露未发布 protocol、配置与 artifact 缺失会改变 world-model 复现实验结论；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ECT](https://arxiv.org/html/2608.10209v1) | 2026-08-12T08:00:00+08:00 | 用小型合成实验探索 episode-level credit transfer；2 + 2 + 2 = 6 | 标准完成 | 仅报告：proof-of-concept 尚未建立可迁移的生产训练机制 |
| [FACT](https://arxiv.org/html/2608.10232v1) | 2026-08-12T08:00:00+08:00 | 将失败动作及其后果作为 action-conditioned world-model 训练信号；3 + 2 + 3 = 8 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [SINKFLEX-RL](https://arxiv.org/html/2608.10357v1) | 2026-08-12T08:00:00+08:00 | 组合已有内存优化模块以降低 agentic RL 峰值显存；2 + 2 + 2 = 6 | 标准完成 | 仅报告：只有单次初步运行且缺少组件消融、吞吐与延迟证据 |
| [UniF-MoE](https://arxiv.org/html/2608.10392v1) | 2026-08-12T08:00:00+08:00 | 先共享公共变换、再路由 residual，重画 shared/specialized capacity 边界；3 + 2 + 3 = 8 | 深入完成 | 整合：`MODEL-MOE`，[Ch21](../../../../books/part-02-model/21-moe.md) |
| [DURA](https://arxiv.org/html/2608.10393v1) | 2026-08-12T08:00:00+08:00 | 以 action-output 与 latent patch 反馈驱动黑盒 VLA 攻击，暴露物理闭环的 query budget；3 + 3 + 2 = 8 | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [A Reward-SNR Floor for RL](https://arxiv.org/html/2608.10441v1) | 2026-08-12T08:00:00+08:00 | 用 matched-moment noise placebo 判断 reward signal 是否高于可学习噪声底；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SALT](https://arxiv.org/html/2608.10484v1) | 2026-08-12T08:00:00+08:00 | 用冻结 VLM 的指令重建约束 action token 表示的语义可读性；3 + 2 + 3 = 8 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Certify or Refuse](https://arxiv.org/html/2608.10893v1) | 2026-08-12T08:00:00+08:00 | 将 shift-aware risk certificate 与拒绝输出绑定；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ReRound](https://arxiv.org/html/2608.11045v1) | 2026-08-12T08:00:00+08:00 | 用离线 diffusion weight reconstruction 引导 rounding，而不改变部署 runtime；3 + 2 + 2 = 7 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [VIScore](https://arxiv.org/html/2608.11174v1) | 2026-08-12T08:00:00+08:00 | 分离 world model 的 veracity、influence 与 sobriety，避免视频质量代替控制价值；3 + 2 + 3 = 8 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |

## 4. 证据与知识整合

### [Decodable But Not Detachable](https://arxiv.org/html/2608.10214v1)

v1 在 1.5B～7B 的三个模型家族、八个领域上统一比较 probe decodability 与参数遮蔽造成的因果损伤。受试模型里，subject-level 表示虽可高精度解码，却没有形成可独立拆卸的局部参数模块；语言与模态这种 token-level 数据边界则出现更明显的对角因果损伤。它支持在 Ch5 补充“可读出不等于可控制、可迁移或可删除”，并把训练数据粒度写成参数模块性的条件，而不是把结果外推到所有模型或规模。

### [Similarity Gates Approve Reversals](https://arxiv.org/html/2608.10216v1)

作者构造词汇重叠匹配的等价/反转对，显示固定 cosine threshold 可以在保持高字面相似度时批准结论反转；受测 production-style drift gate 在 56 个反转样本上均未拦截。drop-in encoder 与 NLI 替换也没有消除测量失配。该小型人工语料不能证明所有 embedding 监控无效，但足以要求 Ch66 将 release gate 的测量对象写清：语义决策不能由单一相似度代理拥有，至少需要 matched counterfactual 与任务结论检查。

### [Cracks in the Foundation](https://arxiv.org/html/2608.10296v1)

v1 在 26 个 7B 模型上固定数据、tokenizer 与 context-extension recipe，分别改变 normalization、GQA、预训练上下文和 sliding-window 配置。结果表明若干短上下文损失难以暴露的小选择会在扩展时复合成显著差异，且早期延长上下文实验具有预测价值。证据只覆盖作者的架构与训练组合；拟在 Ch22 加入“长上下文 readiness 是联合架构属性”，要求在长序列阶段尽早验证，而不能用短上下文 loss 代替。

### [MemSpec](https://arxiv.org/html/2608.10362v1)

v1 将 predictor 给出的 draft effectiveness 与 runtime 的 resident working set 分开，scheduler 先安排可用 draft，避免 edge device 上频繁换模型抵消接受率收益；证据绑定 Jetson Orin Nano。Ch48 已明确 draft proposal 必须与加载成本、resident state 和 end-to-end throughput 联合判断，已有覆盖。

### [TideRL](https://arxiv.org/html/2608.10402v1)

Agentic rollout 会因工具等待、增长上下文和不同 episode 时长停顿，单看 GPU 占用会奖励错误的调度。TideRL 保存可恢复 rollout state，在 decoupled streaming 与 colocated aggregation 间按 readiness 选择，并把 ranks 移给当前可推进的阶段。作者在文本与多模态 workload 上给出端到端结果，但不能外推到未测试的工具和集群。拟在 Ch36 将 rollout readiness 写成资源所有权信号，以 goodput 而非瞬时利用率闭环，并保留 on-policy/staleness 约束。

### [Continuous Interaction Diffusion](https://arxiv.org/html/2608.10438v1)

正文提出 fact/thought/display 三通道、read-only perceptual binding 与 denoising-overlap runtime，并明确首篇没有实证性能主张。它是有价值的 alternative branch，但当前没有结果证明 typed latent state 能保持工具语义、幂等性或安全边界，因此仅在日报保留，不进入 Books。

### [Dependency-Guided Rollback Repair](https://arxiv.org/html/2608.10502v1)

方法从诊断出的 faulty memory 沿 typed dependency graph 传播 invalidation，保留有独立可信支持的分支，再选择性重放；受控 benchmark 支持 recovery/cost trade-off，不证明开放工具环境的 provenance 完整。Ch77 已承载 derived memory rollback 与 authoritative lineage，已有覆盖。

### [MAP-Graph](https://arxiv.org/html/2608.10509v1)

论文先做 hard permission filter，再用 multiplicative path trust 排序，最后按 action risk gate 决定执行；provenance 不再只是事后审计。Ch77 已有相同机制及 synthetic benchmark 边界，已有覆盖。

### [ImpactHO](https://arxiv.org/html/2608.10545v1)

v1 不把 KV offload 当成“能传多少就传多少”，而是先从各用户的质量—传输曲线找到最低效用锚点，再在 admission 后对剩余带宽做加权分配。其 RULER、Qwen3/Llama 与网络仿真实验依赖 Fast KVzip 的 importance signal，并非生产多租户证据。拟在 Ch56 把部分状态迁移写成 utility-bounded admission：若用户无法达到可用锚点应拒绝或降级，而不是公平地分到无效碎片。

### [MOSAIC](https://arxiv.org/html/2608.10605v1)

v1 把 MoE sparsity、loss scaling、MFU、communication、memory 和 parallel layout 放入一个受校准 cluster constraint 的优化，而不是先求 compute-optimal 模型再交给系统补救。拟在 Ch36 的“算法 shape 决定系统可行域”之后补入 cluster-optimal frontier，同时保留 scaling fit 范围外不可外推的限制。

### [Load Hijack](https://arxiv.org/html/2608.10614v1)

攻击只修改 checkpoint router weights，用私有 trigger 将 token 集中到共址 experts，使目标 GPU 成为 straggler；普通输入仍接近干净 routing。拟在 Ch72 的 model artifact supply-chain 段加入 router-as-scheduler threat，要求签名之外还审计触发 routing distribution、per-device load 与 runtime anomaly。

### [Decomposition-Induced Context-Memory Conflict](https://arxiv.org/html/2608.10627v1)

作者显示，把一个本可由上下文回答的任务拆成中间步骤，会让模型在某一步稳定回退到参数记忆，即使原始来源仍在上下文中；SelfCheck 式重复一致性无法发现这种稳定错误。context-aware decoding 能缓解但增加解析成本，且自然样本率与模型尺度仍有限。拟在 Ch66 将 decomposition 本身视为需要验证的 transformation，要求每个中间 claim 保留 source entailment/provenance，而不能把 self-consistency 当成事实置信度。

### [REDAgentBench](https://arxiv.org/html/2608.10669v1)

v1 从显式 safety constraint 生成攻击，在隔离 service sandbox 执行，并用 service receipt/final-state 验证真实 harmful effect；单一 ASR 会混淆可见性与实际执行。拟在 Ch66 的 Agent evaluation 中加入 exposure→execution→observation→adjudication 分层，最终状态拥有裁决权。

### [Enterprise MCP Authorization Gateway](https://arxiv.org/html/2608.10760v1)

论文把 MCP tool access 的两条轴分开：调用者是 end user 还是 non-user service，以及 credential 由谁持有；据此实现 BYOT、gateway-owned token 与 RFC 8693 delegated OAuth 三类 flow。部署覆盖数十个 MCP servers，但为作者自述，没有受控安全实验。拟在 Ch83 补充 gateway 作为 policy enforcement point 的身份委托 contract：persona、credential ownership、delegation scope、审计和 offboarding 必须显式绑定。

### [MoE Proxy Models](https://arxiv.org/html/2608.10823v1)

作者用结构保持、cluster-based expert pruning 保留 backbone 与 routing，以较小代理复现 Ascend 上的 overflow/divergence；这是故障诊断 surrogate，不是训练质量替代物。拟在 Ch66 的 failure reproduction 中加入“保留触发故障的结构因子”验收，并明确 proxy 一致不证明全模型收敛。

### [SCOUT](https://arxiv.org/html/2608.11034v1)

SCOUT 利用数据并行副本在同一步应呈现相近 progress、timing 与 numerical signature 的不变量做 strict-majority 定位；带外 CPU observer 在训练进程 hang 时仍可采集证据，并在原位环境 replay 可疑 collective 或 checkpoint。公开实现适配多个训练栈，但作者实验不能保证覆盖所有网络与 silent corruption。拟在 Ch67 加入“观察路径必须独立于被观察进程”和“副本等价性先定位、原位 replay 再归因”的演进链。

### [Catastrophic Remembering](https://arxiv.org/html/2608.11095v1)

大规模仓库历史说明 agent instruction 追加容易、删除因 rationale 丢失而昂贵；受控 inversion 实验显示保留注释可压缩冗余，但不证明任意 prompt rewrite 等价。Ch74 已把 rationale、稀有 guard、regression 与 canary 纳入 prompt lifecycle，已有覆盖。

### [Workload-Aware Mixed RL Rollout Scheduling](https://arxiv.org/html/2608.11152v1)

不同 rollout class 共用推理池时，prefix-aware routing 只优化复用，无法约束被长会话和工具空档占住的 KV 容量。v1 将 trainer 的目标 mixture/staleness 与 router 的 admission/placement 分责，并用 footprint×residency 估算 block-time；session admission 因而是一项容量承诺。拟由 Ch56 承载 workload quota、驻留时间和 admission，Ch36 只 handoff 训练侧 mixture 与 freshness contract；结果仍限于作者配置。

### [The Multilingual Quantization Tax](https://arxiv.org/html/2608.09941v1)

v1 在 Gemma 4 / Qwen 3.5 的 2B、4B 模型上，用 NF4 比较八种语言的 classification 任务，显示总体均值会掩盖不同语言与 typology 的非对称退化。论文关于 outlier 与跨语言 routing 的解释仍是机制假说，且没有生成、工具调用或生产延迟证据。拟在 Ch49 的量化验收中增加 language/task slice，结论仅限“release contract 必须逐切片验证”，不写成已证明的内部因果机制。

### [4D-WAM](https://arxiv.org/html/2608.10107v1)

方法用冻结几何 teacher 同时约束预测帧的 feature 与 depth，使视频生成不只追求像素相似，还保持驾驶环境的时空结构。证据只覆盖驾驶数据和作者 world-model pipeline，不能证明几何 teacher 对任意 embodiment 有效。Ch25 已把 action-conditioned transition、持久 4D state 与 observation correction 串成同一责任链，判定已有覆盖。

### [Procedural Fairness in RLHF](https://arxiv.org/html/2608.10126v1)

v1 用 971 个比较、60 个模拟 rater 和 20 个 prompts，将偏好聚合结果与“谁被代表、如何聚合”的过程公平分开。受控模拟不能代表真实社会偏好，也不证明某一 aggregation rule 普遍优越。Ch31 已明确偏好不是单一客观标量，并要求群体 identity、aggregation policy 与冲突保留进入 reward provenance，判定已有覆盖。

### [Reproducing LeWorldModel](https://arxiv.org/html/2608.10145v1)

复现实验在 TwoRoom、18.03M frames 和单 seed 上重建原方法，发现未公开 protocol、配置细节和 artifact 选择会显著改变 success。它不能裁决原模型在更多环境中的能力，却直接证明“论文描述可读”不等于可复现 evaluation contract。拟在 Ch66 的 world-model evaluation 中要求 environment revision、data generation、checkpoint、rollout protocol、seed 与成功判据共同版本化；缺任一项时只可声明局部复现。

### [ECT](https://arxiv.org/html/2608.10209v1)

论文在两个小型合成问题上探索 episode-level credit transfer，证明构造在作者 toy setting 中可以运行，但没有真实 LLM/Agent workload、规模行为或与成熟 estimator 的充分比较。它暂时不足以改变训练系统的稳定设计判断，故仅报告，等待更大规模独立复现或明确 failure regime。

### [FACT](https://arxiv.org/html/2608.10232v1)

v1 先执行 action，再用失败后的 observation 训练 action-conditioned world model；teacher-forcing mask 允许未来/value 头看到真实执行动作，使模型学习“错误动作造成什么后果”，而不是把失败轨迹当噪声丢弃。best-of-N 增加采样成本，证据限于仿真与双臂实机任务。拟在 Ch25 的 imagined rollout 主线补入 failure-conditioned transition，并明确执行动作是环境状态更新的权威输入。

### [SINKFLEX-RL](https://arxiv.org/html/2608.10357v1)

正文组合 activation checkpoint、offload 等既有模块，Tau2 retail 只给出初步单次运行和峰值显存；缺少逐组件消融、吞吐、延迟与训练质量的闭环。它能作为实现线索，但尚未形成超出现有训练内存路线的稳定机制，因此仅报告，不以组件拼装产生 Books 增量。

### [UniF-MoE](https://arxiv.org/html/2608.10392v1)

方法先让所有 token 经过共享变换，再只把 residual 路由给 experts；这把“公共能力全部复制到每个 expert”的旧方案改成 shared-first / specialize-after。GLUE 与 DomainBed 结果只支持小规模表示任务，不能外推到大模型训练吞吐或通信。拟在 Ch21 将它作为 shared/specialized capacity 的 alternative branch，保留新增共享瓶颈和 residual routing collapse 风险。

### [DURA](https://arxiv.org/html/2608.10393v1)

v1 只观察 VLA action output，用 diffusion latent patch 迭代提出扰动；在 OpenVLA、π0-FAST、LIBERO 和有限 Franka 实验中，需要每次更新 128～2,048 次 queries。证据说明黑盒 action feedback 也能形成物理攻击面，但不证明开放世界通用性。拟在 Ch72 把 VLA threat model 从视觉输入扩展到 action-output feedback loop，并绑定 query budget、safety controller 与实机 effect receipt。

### [A Reward-SNR Floor for RL](https://arxiv.org/html/2608.10441v1)

论文构造与真实 reward 一阶/二阶矩匹配的 noise placebo：如果 learner 无法稳定优于 placebo，reward signal 尚未越过可学习检测底线。三项公开推荐数据集只支持必要条件诊断，这不是 policy regret bound 或充分成功证明。拟在 Ch66 加入 design-time reward regime gate，先证明 signal 超越匹配噪声，再比较 optimizer 或扩大训练。

### [SALT](https://arxiv.org/html/2608.10484v1)

SALT 用冻结 VLM 从 action token 重建语言指令，迫使 action representation 保留可读的任务语义；证据来自 0.5B 模型、BridgeV2 的 17 个 verbs 与 SimplerEnv，并不证明语言可读性因果带来控制鲁棒性。拟在 Ch26 的 action representation 中加入语义对齐作为 experimental auxiliary objective，同时保留 control-frequency、low-level safety 与真实闭环验收。

### [Certify or Refuse](https://arxiv.org/html/2608.10893v1)

正文在预注册、exact shift 与 bounded-density-ratio 假设下给出 selective-risk certificate；SQuAD 到 NewsQA 的单个示例最终选择拒绝，而非证明更高任务能力。Ch66 已承载 shift-aware coverage/risk、拒绝输出和假设公开的机制，判定已有覆盖；该理论细节作为证据边界，不重复扩写正文。

### [ReRound](https://arxiv.org/html/2608.11045v1)

v1 用离线 diffusion 模型重建权重分布，指导 midpoint rounding，并按谱性质选择适用层；部署后仍是普通量化权重，不改变 runtime。证据只覆盖较小 LLM，训练 diffusion 的离线成本、跨模型迁移和端到端 serving 均未充分评估。拟在 Ch49 将它作为 activation/text calibration 之外的 weight-reconstruction 分支，并要求离线成本、层选择、质量回归与相同 runtime format 一起验收。

### [VIScore](https://arxiv.org/html/2608.11174v1)

VIScore 将 world model 分为 veracity、对 downstream policy 的 influence 与不夸大无效改进的 sobriety，避免生成视频的视觉质量代替控制价值；受测模型/任务的 Spearman 相关达到作者报告水平，但相关性不是因果保证。拟在 Ch25 的 evaluation contract 中分别验收 prediction fidelity、policy sensitivity 与 calibrated abstention，防止单一视频指标成为发布 authority。

## 5. 缺口与下一步

- **终态保留项：** Hunyuan [From LR to ELR](https://hunyuan.tencent.com/research) 与上一日报是同一去重材料请求；当前公开记录不足以确定真实 owner 日，因此不支持正面证据、Books 写回或本窗无遗漏断言。**定点重开条件：** 取得带时区的首次公开记录、事件时网页存档或官方说明；届时只重开真实 owner Daily，不在本日报重复计分。

除该外部日期身份缺口外，本日报候选、证据与 Books 写回均已闭合。

## 6. 复核

复核者：独立 fresh-context reviewer（2026-09-08）

结论：通过

独立复核重开 516 个官方公告身份中的高信号题摘范围，确认原稿存在 14 个 false negative，将候选分母由 18 修正为 32；抽查原 18 项未发现需要移出分母的 false positive。32 项均核对 exact-v1 HTML 与 withdrawn 页面状态；3 项新增材料由现有具体命题承载，9 项形成新的长期机制提案，2 项因证据不足降为仅报告。写后逐项检查 22 个 source-family marker、canonical owner、相邻段落和 Review notes 边界，确认采用命题均已进入机制正文；仅对 SALT 的措辞做语义收紧。Coverage、Candidate、Evidence、Books 与独立复核 Gate 均已闭合。Cross-model skipped: 本轮为父任务分派的非交互独立复核。
