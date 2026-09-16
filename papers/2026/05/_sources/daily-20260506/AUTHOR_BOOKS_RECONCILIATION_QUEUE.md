# 2026-05-06 作者侧 Books 对账与写回队列

本文件保存最终 Books 对账结果。12 项原有实体已回读，10 项新写回已由 root 落实并通过独立 post-write 审计。

- 已存在并复核：12
- 新写回并复核：10
- 撤回闭合：1（2605.03562；Books 无正向 marker/特有结论）

## SF-2026-ARXIV-2605-02909

- Primary: `arXiv:2605.02909v1`
- Owner: `TRAIN-GRPO`
- Status: Integrate — applied and post-write audited
- Exact delta: verifier系统性false positive的pattern而非总错误率决定RLVR平台/崩塌，直接修正奖励可靠性假设。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.02909)

## SF-2026-ARXIV-2605-02946

- Primary: `arXiv:2605.02946v1`
- Owner: `PLATFORM-SECURITY`
- Status: Integrate — already present and rechecked
- Exact delta: MoE输入suffix优化直接操纵refusal/harmful expert routing，并有跨兄弟模型迁移，揭示输出层之外的架构安全攻击面。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.02946)

## SF-2026-ARXIV-2605-02960

- Primary: `arXiv:2605.02960v1`
- Owner: `INFER-PREFILL`
- Status: Integrate — already present and rechecked
- Exact delta: prefill-only长计算窗口允许expert weights AllGather替代activation AllToAll，且依赖饱和阈值/负载路由，改变MoE部署选择。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.02960)

## SF-2026-ARXIV-2605-03159

- Primary: `arXiv:2605.03159v1`
- Owner: `AGENT-WORKFLOW`
- Status: Integrate — applied and post-write audited
- Exact delta: passing traces are compiled into necessary-state and order constraints for nondeterministic workflow acceptance
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03159)

## SF-2026-ARXIV-2605-03188

- Primary: `arXiv:2605.03188v1`
- Owner: `PLATFORM-SECURITY`
- Status: Integrate — applied and post-write audited
- Exact delta: derived-value独立加噪可放大root distinguishability，root-once sanitization用postprocessing共享跨turn预算；改变Agent数据发布图的隐私会计。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03188)

## SF-2026-ARXIV-2605-03190

- Primary: `arXiv:2605.03190v1`
- Owner: `INFER-TENSORRT-LLM`
- Status: Integrate — already present and rechecked
- Exact delta: 异步GPU以资源隔离virtual core和dependency micro-op解耦kernel编排，直接改变memory/compute重叠与动态输入执行。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03190)

## SF-2026-ARXIV-2605-03252

- Primary: `arXiv:2605.03252v1`
- Owner: `TRAIN-LORA`
- Status: Integrate — applied and post-write audited
- Exact delta: zero-init MoE LoRA导致router/expert置换对称deadlock，用disjoint singular subspaces让初始router梯度非退化，具体改写初始化选择。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03252)

## SF-2026-ARXIV-2605-03309

- Primary: `arXiv:2605.03309v1`
- Owner: `PLATFORM-SECURITY`
- Status: Integrate — already present and rechecked
- Exact delta: registry identity+publisher/registry dual signature+namespace pinning规定artifact来源验证，AI package供应链有具体协议分支，须核验非实证/普遍性claim。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03309)

## SF-2026-ARXIV-2605-03314

- Primary: `arXiv:2605.03314v1`
- Owner: `AGENT-CONTEXT`
- Status: Integrate — already present and rechecked
- Exact delta: 离线entailment对齐训练交错披露策略，改变准确率/内容时序tradeoff；训练checker不是runtime gate，已按exact-v1纠正。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03314)

## SF-2026-ARXIV-2605-03317

- Primary: `arXiv:2605.03317v1`
- Owner: `MULTIMODAL-GENERATIVE-PARADIGMS`
- Status: Integrate — applied and post-write audited
- Exact delta: useful diffusion representation granularity changes with SNR/timestep, making a static alignment target mismatched
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03317)

## SF-2026-ARXIV-2605-03327

- Primary: `arXiv:2605.03327v1`
- Owner: `TRAIN-GRPO`
- Status: Integrate — already present and rechecked
- Exact delta: bounded Hellinger和entropy-gated token权重重分配sequence advantage，直接改变critic-free RL信用分配；不能把entropy称真实epistemic truth。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03327)

## SF-2026-ARXIV-2605-03351

- Primary: `arXiv:2605.03351v1`
- Owner: `INFER-KV-CACHE`
- Status: Integrate — applied and post-write audited
- Exact delta: same-video followup KV复用与fresh-video vision skip分开，并用paired drift与stage-share ceiling避免speedup相乘，直接改变视频cache验收。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03351)

## SF-2026-ARXIV-2605-03425

- Primary: `arXiv:2605.03425v1`
- Owner: `TRAIN-PRETRAINING`
- Status: Integrate — already present and rechecked
- Exact delta: DP noise先加入privatized gradient再filter，AdamW二阶矩须扣filtered-noise贡献而非未过滤variance；已核验顺序、校准及直接限制。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03425)

## SF-2026-ARXIV-2605-03596

- Primary: `arXiv:2605.03596v1`
- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Status: Integrate — already present and rechecked
- Exact delta: WorkspaceBench 把跨文件依赖、目录图状态与结果 rubric 纳入 agent 评估，明确暴露单工具/单文件基准不能覆盖的工作区成功条件。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03596)

## SF-2026-ARXIV-2605-03625

- Primary: `arXiv:2605.03625v1`
- Owner: `AGENT-PLANNING`
- Status: Integrate — applied and post-write audited
- Exact delta: graph search creates plan supervision while runtime search remains a separate optional owner
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03625)

## SF-2026-ARXIV-2605-03644

- Primary: `arXiv:2605.03644v1`
- Owner: `INFER-KV-CACHE`
- Status: Integrate — already present and rechecked
- Exact delta: 按 probe entropy 自适应选择 many-shot 数，并重编码位置以复用可重排 KV；直接改变 ICL 推理预算与缓存语义契约。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03644)

## SF-2026-ARXIV-2605-03667

- Primary: `arXiv:2605.03667v1`
- Owner: `TRAIN-PRETRAINING`
- Status: Integrate — already present and rechecked
- Exact delta: 低秩训练中对 squared-ReLU activation 施加硬件 2:4 稀疏，连接激活内存与实际加速路径；需限定特定 FFN/模型尺度而非一般必要条件。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03667)

## SF-2026-ARXIV-2605-03677

- Primary: `arXiv:2605.03677v1`
- Owner: `TRAIN-RLHF`
- Status: Integrate — already present and rechecked
- Exact delta: 把 OPD 拆成 student-state 探索与 teacher token guidance 的 outcome 顺序一致性，提出校准；直接改变蒸馏反馈可靠性的机制边界。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03677)

## SF-2026-ARXIV-2605-03724

- Primary: `arXiv:2605.03724v1`
- Owner: `TRAIN-LORA`
- Status: Integrate — applied and post-write audited
- Exact delta: 区分平方损失 NTK 的充分 rank 阈值、交叉熵 PL 条件与二分类 bias 饱和，给出 rank-one 适用/不适用边界；不是普遍 LoRA rank=1 主张。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03724)

## SF-2026-ARXIV-2605-03812

- Primary: `arXiv:2605.03812v1`
- Owner: `PLATFORM-SECURITY`
- Status: Integrate — applied and post-write audited
- Exact delta: GPU Rowhammer 对 page table 的跨进程/CPU 权限影响直接挑战 GPU 多租户与 IOMMU 隔离假设；安全准入，仅研究防护边界与验证条件。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03812)

## SF-2026-ARXIV-2605-03884

- Primary: `arXiv:2605.03884v1`
- Owner: `AGENT-MULTI-AGENT`
- Status: Integrate — already present and rechecked
- Exact delta: 以量化 KV CacheCard 携带跨 agent latent context 并注入 cache，改变 handoff 表示、校验和重 prefill 代价；存档摘要明显修订，必须回到 exact-v1 限定原始证据。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03884)

## SF-2026-ARXIV-2605-03945

- Primary: `arXiv:2605.03945v1`
- Owner: `PLATFORM-SECURITY`
- Status: Integrate — applied and post-write audited
- Exact delta: CorrDP 按敏感/非敏感特征相关性放宽隐私定义并选择梯度噪声；直接涉及 DP utility 改善究竟来自算法还是保证变弱的安全边界。
- Evidence: [author exact-v1 review](AUTHOR_EVIDENCE_COMPLETION.md#2605.03945)

## Withdrawal reversal

- `SF-2026-ARXIV-2605-03562`: 从正向候选、评分和采用链移除；官方 arXiv exact-v1 页面提示 newer version 已被作者撤回。当前 Books 已无该 ID、Source Family、HeadQ 名称或特有 side-code 结论；root 只需在 post-write review 复算这一不变量，不得误删由其他来源支持的通用 attention-distortion 原则。
