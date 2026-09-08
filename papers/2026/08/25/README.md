# Daily Research — 2026-08-25

**规范：** V3
**窗口：** 2026-08-24T09:00:00+08:00 ～ 2026-08-25T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T18:05:00+08:00

## 1. 结论

按 arXiv 官方首次公告批次冻结 1,022 个唯一身份，逐篇完成标题与完整摘要语义筛选，最终保留 64 个能改变大模型系统长期机制、状态边界或评价合同的候选；其余材料以具体的题摘语义理由在候选分母之前关闭。旧 `submitted` 日期只描述版本元数据，不覆盖官方首次公开归属；因此 5 月提交、8 月 25 日才进入官方新公告批次的 KVBoost 仍属于本窗。厂商来源没有独立于这些 arXiv 家族的新材料。

本窗呈现五条长期变化：KV 状态从连续前缀复用扩展到带身份与修复合同的任意 chunk、可恢复分层、混合精度驻留与可压缩性判据；训练优化把 evidence、credit transport、optimizer state 与 update geometry 分开；编译与服务从局部启发式走向全局 layout、阶段感知 placement、near-memory co-design 与动态 power/SLO 控制；Agent 状态从自由文本升级为 typed context、boundary-aware skill、effect-time policy 与持久 event log；evaluation 则必须显式治理 harness、可控性混杂、置信度与证据状态。64 项均已回到精确版本 primary source 核对机制、评价、限制和 withdrawal 状态，并完成 Books 对读。独立回放恢复了 19 个此前被错误关闭或静默遗失的候选，同时将 7 个重复整合建议收敛为已有覆盖；必要的 Books 机制已写入 canonical owner 并通过写后复核。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 列表检查到 8 月 24 日窗口边界，无独立技术正文 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 列表检查到窗口边界，无独立技术正文 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind 与 Google Research 日期列表检查到窗口边界，并与 arXiv 身份去重 | 已检查 | 无 |
| SRC-META-AI | 官方 Research/Results 检查到窗口边界，并与 arXiv 身份去重 | 已检查 | 无 |
| SRC-QWEN | 官方论文与模型列表检查到窗口边界，并与 arXiv 身份去重 | 已检查 | 无 |
| SRC-DEEPSEEK | 官网研究入口与官方仓库检查到窗口边界 | 已检查 | 无 |
| SRC-MOONSHOT | Kimi Blog 与 MoonshotAI 仓库检查到窗口边界 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Research/官方仓库与当窗 arXiv 身份核对，无额外家族 | 已检查 | 无 |
| SRC-ZAI | Research、发布说明与仓库检查到窗口边界 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Research 与论文目录检查到窗口边界，并与 arXiv 去重 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 官方技术博客与 ERNIE 仓库检查到窗口边界 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | MiMo 论文/博客与仓库检查到窗口边界 | 已检查 | 无 |
| SRC-MINIMAX | 中英文 Research/Blog 与仓库检查到窗口边界 | 已检查 | 无 |
| SRC-ARXIV | 官方首次公告批次冻结 1,022 个唯一身份；跨分类去重后逐篇读标题与完整摘要，保留 64 项；其余逐项作 pre-denominator closure；旧 submitted/revision 字段只用于身份核对 | 已检查 | 无 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs](https://arxiv.org/abs/2608.22704) | 2026-08-25T08:00:00+08:00 | 从永久驱逐演进为 GPU/CPU 分层可召回 KV 状态；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 的可恢复分层 KV |
| [The Compaction Cliff in Long-Running AI Agent Memory](https://arxiv.org/abs/2608.22752) | 2026-08-25T08:00:00+08:00 | 统一摘要会系统性损害 exact safety state，要求按知识类型绑定保留策略；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) 的 typed retention 与 raw-evidence fallback |
| [TailSieve: Partial-Rollout-Guided Tail Routing for LLM Rollouts](https://arxiv.org/abs/2608.22788) | 2026-08-25T08:00:00+08:00 | 把 RL rollout 调度目标从单请求延迟改为 group makespan 与长尾分配；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) 的 partial rollout、straggler 与 trajectory lifecycle |
| [AgentFlow: A Flow-Centric Policy Language and Framework for Securing LLM Agent Systems](https://arxiv.org/abs/2608.22868) | 2026-08-25T08:00:00+08:00 | 以 labeled flow、capability 与 stateful taint 管理跨工具数据路径；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 的 trajectory-level flow control 与 reference monitor |
| [The Mask Is Not the Model: Auditing Prefix Invariance in Attention, State-Space, and Hybrid Sequence Models](https://arxiv.org/abs/2608.22876) | 2026-08-25T08:00:00+08:00 | 把 causal mask 声明提升为可观测 prefix-invariance correctness invariant；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MODEL-TRANSFORMER-LAYER，[Ch17](../../../../books/part-02-model/17-transformer-layer.md) 的因果数据流检查 |
| [When Can Agents Safely Checkpoint, Fork, Restore, and Merge?](https://arxiv.org/abs/2608.22928) | 2026-08-25T08:00:00+08:00 | 执行编辑不能撤销已授权或已发送副作用，要求身份、幂等与合并合同；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) 的 checkpoint/replay/commit 边界 |
| [The Laws of Context Allocation](https://arxiv.org/abs/2608.23252) | 2026-08-25T08:00:00+08:00 | 区分 evidence availability 与 utilization，并联合决定检索、停止和上下文预算；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) 的 relevance、sufficiency 与 stopping policy |
| [InjecMEM: Memory Injection Attack on LLM Agent Memory Systems](https://arxiv.org/abs/2608.23471) | 2026-08-25T08:00:00+08:00 | 单次交互可污染未来可召回记忆，暴露 write/retrieval/provenance 权限边界；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) 的记忆写入、来源与修复隔离 |
| [The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams](https://arxiv.org/abs/2608.23541) | 2026-08-25T08:00:00+08:00 | 通信内容和时机会降低独立 proposal diversity，不能把 Agent 数量等同收益；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) 的 communication tax、independence 与 verifier |
| [Best Practice Critic Optimization](https://arxiv.org/abs/2608.23566) | 2026-08-25T08:00:00+08:00 | 将 critic instability 拆成可控制的 target、range、normalization 与 clipping 选择；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：TRAIN-PPO，[Ch32](../../../../books/part-04-training-system/32-ppo.md) 的 critic failure 与 PPO/GRPO 条件分支 |
| [KVBoost: Chunk-Level Key-Value Cache Reuse with Deviation-Guided Recomputation](https://arxiv.org/abs/2608.21362) | 2026-08-25T08:00:00+08:00 | 将前缀缓存扩展为位置/内容双身份的任意 chunk 复用，并以强制修复约束近似命中；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；在 prefix reuse 后加入 identity、seam repair 与 approximate-hit commit 边界 |
| [There Is No Neutral Harness](https://arxiv.org/abs/2608.21382) | 2026-08-25T08:00:00+08:00 | item-level fragility 证明模型排序可能主要由 scoring harness 的脆弱题目承载；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；在 evaluation identity 后加入 item-level fragility gate |
| [Let Credit Follow Computation](https://arxiv.org/abs/2608.21501) | 2026-08-25T08:00:00+08:00 | 将成功证据、credit transport 和 policy update geometry 拆成独立对象；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-PPO，[Ch32](../../../../books/part-04-training-system/32-ppo.md)；在 GAE 后加入 computation-conditioned transport 的条件分支 |
| [Tensor Seeks Layout](https://arxiv.org/abs/2608.21555) | 2026-08-25T08:00:00+08:00 | 将跨算子 layout 选择形式化为全局优化，并区分搜索误差与 cost-model 误差；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；加入 global layout plan 与 cost-model validation 边界 |
| [SAEM: Stage-Aware Expert Management](https://arxiv.org/abs/2608.21614) | 2026-08-25T08:00:00+08:00 | 用 reasoning-stage coherence 改写 MoE expert residency、repacking 与 CPU fallback；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) 的“Reasoning Stage 可以成为 MoE Residency Hint” |
| [PowerSlider](https://arxiv.org/abs/2608.21719) | 2026-08-25T08:00:00+08:00 | 把动态功率上限变成 prefill/think/answer 各阶段的 SLO 与功率分配问题；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；加入 power envelope、phase asymmetry 与 fail-safe |
| [Reinforcement Learning on Benign Facts Amplifies Leakage of Memorized Private Data](https://arxiv.org/abs/2608.21727) | 2026-08-25T08:00:00+08:00 | benign RLVR 也可能提高既有 PII 的可提取性，打破“训练数据无隐私即安全”的假设；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；在 memorization 风险后加入 post-training accessibility shift |
| [Evaluation Awareness in Language Models](https://arxiv.org/abs/2608.21766) | 2026-08-25T08:00:00+08:00 | 区分 evaluation-context representation、verbalization 与 causal control，限制 benchmark 外推；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；加入 evaluation-awareness slice 与 deployment validity 边界 |
| [Counterfactual Quotient Models](https://arxiv.org/abs/2608.22092) | 2026-08-25T08:00:00+08:00 | 只学习 action 改变的 future 差异，剥离与动作无关的共同动态；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 的 counterfactual/action-conditioned sufficiency |
| [What actually runs: a measurement study of language model placement and decode speed on the Apple Neural Engine](https://arxiv.org/abs/2608.22110) | 2026-08-25T08:00:00+08:00 | 证明 accelerator placement 由 graph expression 与 encoding 决定，并以 memory-controller 计数核验真实执行；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；加入 intended plan 与 measured placement 的双证据合同 |
| [RAG Collapse](https://arxiv.org/abs/2608.22118) | 2026-08-25T08:00:00+08:00 | 自生成文档被再次检索会形成 provenance feedback 和 citation self-bias；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md)；在 provenance lifecycle 后加入 self-authored feedback isolation |
| [Model of Models: When Does Emitting a Specialist Beat Attending, Adapting, or Tuning?](https://arxiv.org/abs/2608.21386v1) | 2026-08-25T08:00:00+08:00 | 匹配预算下比较 zero-shot、ICL、test-time adaptation 与 emitted specialist，给出任务条件化机制的 operating regime；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-LORA，[Ch30](../../../../books/part-04-training-system/30-lora.md)；在 adapter lifecycle 后加入 amortized specialist emission 分支 |
| [Selective Cross-View Consistency for World Action Models](https://arxiv.org/abs/2608.21402v1) | 2026-08-25T08:00:00+08:00 | 区分 view-invariant state 与 view-covariant observation，避免一致性约束抹去控制所需视角信息；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 的 state/observation identity 与 action-conditioned transition |
| [Retrieval Needs Multivectors: An Exponential Separation](https://arxiv.org/abs/2608.21494v1) | 2026-08-25T08:00:00+08:00 | 给出单向量检索与多向量交互检索的表达能力分离，修正“更大 embedding 足以替代 token-level matching”的假设；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md)；在 retrieval representation 选择处加入表达力与索引成本分支 |
| [The geometry of AI validation](https://arxiv.org/abs/2608.21496v1) | 2026-08-25T08:00:00+08:00 | 形式化 iid best-of-N 搜索可被有限验证集可靠认证的几何边界；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 adaptive search、holdout exhaustion 与 selection bias |
| [SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation](https://arxiv.org/abs/2608.21500v1) | 2026-08-25T08:00:00+08:00 | 用攻击者 on-policy trajectory 蒸馏 token-level defensive signal，暴露静态拒答训练面对自适应攻击的分布缺口；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 的 adaptive red-team、policy signal 与外部 authorization |
| [Beyond Sparse Weights: When Is Attention Compressible?](https://arxiv.org/abs/2608.21541v1) | 2026-08-25T08:00:00+08:00 | 证明稀疏 attention weight 不足以推出可安全删除 KV，并以 omitted-value statistic 约束近似误差；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；在 eviction score 前加入 value-aware compressibility condition |
| [Evidence-State Reliability Under Controlled Degradation](https://arxiv.org/abs/2608.21559v1) | 2026-08-25T08:00:00+08:00 | 受控降级下 parser validity 与证据状态可靠性分离，说明格式正确不能作为 pipeline correctness 代理；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的分层 fault injection 与 evidence-state contract |
| [Reading the Room: Implicit Confusion Encoding in Recurrent World Model States](https://arxiv.org/abs/2608.21582v1) | 2026-08-25T08:00:00+08:00 | recurrent latent state 可编码 agent confusion，但 probe 可读性与跨任务因果可控性并不等价；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 的 latent-state observability/controllability 边界 |
| [Measuring Activation Control in Large Language Models](https://arxiv.org/abs/2608.21664v1) | 2026-08-25T08:00:00+08:00 | 将 activation monitor 的可预测性与 intervention controllability 分开，防止可线性解码被误写成可可靠控制；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 probe/intervention 因果证据边界 |
| [Context as an Environment](https://arxiv.org/abs/2608.21690v1) | 2026-08-25T08:00:00+08:00 | 以 append-only event log、typed namespace 与 reader projection 重构长程 Agent context ownership；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) 的 typed event、projection 与 compaction boundary |
| [Prompt-Based Abstention Fails Under Misleading Context](https://arxiv.org/abs/2608.22228v1) | 2026-08-25T08:00:00+08:00 | 证明缺证据时的口头 abstention 不保证面对误导证据仍拒答，需冲突检测与外部 evidence gate；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) 的 evidence sufficiency、contradiction 与 abstention |
| [Beyond Dense Adam States](https://arxiv.org/abs/2608.22322v1) | 2026-08-25T08:00:00+08:00 | 将 optimizer-state 量化与 update semantics 绑定，避免只按存储压缩率评估训练正确性；2 + 3 + 2 = 7 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)；在 state sharding 后补 optimizer precision contract |
| [Noise Floor Audit for Agent Benchmarks](https://arxiv.org/abs/2608.22331v1) | 2026-08-25T08:00:00+08:00 | 将微小榜单差异与 harness/run variance 的 noise floor 对照，限制无重复测量的排名结论；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 repeated-run variance 与 practical significance |
| [When Not to Imitate: Boundary-Aware Skill Memory](https://arxiv.org/abs/2608.22339v1) | 2026-08-25T08:00:00+08:00 | 为 skill imitation 增加 applicability boundary，避免成功轨迹在不同 tool/state contract 下被错误复用；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) 的经验准入、适用条件与回滚 |
| [Where World Models Break: Natural-Input Failure Discovery](https://arxiv.org/abs/2608.22421v1) | 2026-08-25T08:00:00+08:00 | 从合成扰动扩展到自然输入搜索，发现视觉质量指标覆盖不到的动态失败簇；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 的 failure discovery 与 intervention-based evaluation |
| [Claim-Level Confidence Calibration for Reliable Decision Making with Large Language Models](https://arxiv.org/abs/2608.22483v1) | 2026-08-25T08:00:00+08:00 | 将整体答案置信度拆成 atomic claim 校准与决策聚合，避免长回答置信度的无条件连乘；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 claim-evidence graph 与 decision aggregation |
| [Understanding the Synchronization Tax in GPU Scale-Up Domains](https://arxiv.org/abs/2608.22503v1) | 2026-08-25T08:00:00+08:00 | 将 scale-up 域扩大后的 barrier waiting 与 collective imbalance 分解为可测同步税；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-TENSOR-PARALLEL，[Ch37](../../../../books/part-04-training-system/37-tensor-parallel.md)；在通信模型后加入 synchronization-tail accounting |
| [NOVA](https://arxiv.org/abs/2608.22613v1) | 2026-08-25T08:00:00+08:00 | 面向 Attention–SSM–MoE 混合负载联合设计 near-memory 数据路径与算子 placement；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；在 global plan 中加入 heterogeneous near-memory branch |
| [CAI-DLLM](https://arxiv.org/abs/2608.22646v1) | 2026-08-25T08:00:00+08:00 | 以收敛状态而非固定迭代数控制 diffusion LM 推理，改变 latency/quality stopping contract；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 的 iterative correction 与 adaptive stopping |
| [Think Only When Needed](https://arxiv.org/abs/2608.23224v1) | 2026-08-25T08:00:00+08:00 | 将 VLA 慢路径推理变为可撤销的 prompt-authority controller，保留实时 base policy；3 + 3 + 2 = 8 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；在 fast/slow controller handoff 中加入 prompt authority |
| [Credal Large Language Models for Semantic Commitment under Uncertainty](https://arxiv.org/abs/2608.23244v1) | 2026-08-25T08:00:00+08:00 | 用 adapter ensemble 的 credal set 区分 token uncertainty 与 semantic commitment，支持 selective prediction；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的受限 uncertainty sensor 与 selective prediction 边界 |
| [Sigmoid Attention as a Better Substrate for Learned KV Cache Eviction](https://arxiv.org/abs/2608.23296v1) | 2026-08-25T08:00:00+08:00 | attention normalization 会改变 learned soft gate 映射到物理 KV 删除的稳定性；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；在 learned eviction 中加入 normalization-dependent calibration |
| [Adversarial Entropy Inflation Against Gumbel-Based Inference Verification](https://arxiv.org/abs/2608.23375v1) | 2026-08-25T08:00:00+08:00 | 攻击可抬高 entropy 破坏基于 Gumbel sampling 的推理验证假设，要求独立 correctness owner；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 adaptive evaluation 与 adversarial uncertainty |
| [When “Do Not” Is Not Deny](https://arxiv.org/abs/2608.23550v1) | 2026-08-25T08:00:00+08:00 | 经验对照显示自然语言禁止规则不能替代 built-in capability control；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 的 prompt policy 与 capability enforcement owner 边界 |
| [CacheRouter: A Dual-Path Tool Routing Architecture with Cache-Preserving Main-Model Isolation for Long-Tail Tool Discovery](https://arxiv.org/abs/2608.22708v1) | 2026-08-25T08:00:00+08:00 | 将稳定主模型前缀与长尾工具发现拆成双路径，换取额外 router 与执行信任边界；2 + 2 + 2 = 6 | 标准完成 | 仅报告：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md)；原型与价格假设不足以改变通用工具生命周期 |
| [CatchBench: When Can an Agent Failure Be Caught?](https://arxiv.org/abs/2608.22808v1) | 2026-08-25T08:00:00+08:00 | 将审计能力绑定 PRE/LIVE/POST 三种可见状态，并公开不可判定比较；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 observation boundary、label provenance 与 unresolved result |
| [What Process Evaluation of Coding Agents Actually Measures: Action, Task, and Step Are Three Different Levels](https://arxiv.org/abs/2608.22960v1) | 2026-08-25T08:00:00+08:00 | 分离 action prediction、task uncertainty 与 step causal attribution，揭示 full-trace judge 的 collider bias；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的评价单位、干预与因果归因边界 |
| [Pointing-VLA: Typed Spatial Grounding Interfaces for Vision-Language-Action Manipulation](https://arxiv.org/abs/2608.23138v1) | 2026-08-25T08:00:00+08:00 | 以 typed point/heatmap/trajectory readout 替代文本坐标，缩短 VLA 到控制器的接口；2 + 2 + 2 = 6 | 标准完成 | 仅报告：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；受限机器人与任务证据不足以改写通用控制架构 |
| [Is Next-Chunk Reasoning RL Really Better than SFT? Revisiting Training Strategies under no-CoT Data](https://arxiv.org/abs/2608.23256v1) | 2026-08-25T08:00:00+08:00 | 受控比较表明 next-chunk RL 的收益可能来自数据暴露而非 RL 本身；2 + 2 + 2 = 6 | 标准完成 | 仅报告：TRAIN-SFT，[Ch29](../../../../books/part-04-training-system/29-sft.md)；保留为特定 no-CoT 数据条件下的替代分支 |
| [SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository Stack Migration?](https://arxiv.org/abs/2608.23564v1) | 2026-08-25T08:00:00+08:00 | 将 migration completeness、behavioral correctness 与独立 targeted tests 分成连续 Gate；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的过程证据、终态正确性与隐藏反例分层 |
| [ReWorld: An Interactive World Model with Long-Horizon Memory](https://arxiv.org/abs/2608.23565v1) | 2026-08-25T08:00:00+08:00 | 以短期控制窗口、全局 heads 与 pose-indexed landmark bank 分离实时控制和长期回访；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 的局部动态、持久世界状态与动作一致性评价 |
| [Forgotten in Weights, Recovered by Tools: Agentic Tool Unlearning for LLM Agents](https://arxiv.org/abs/2608.21544v1) | 2026-08-25T08:00:00+08:00 | 揭示参数遗忘后仍可经工具恢复目标，要求同时治理权重 recall 与 tool trajectory；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；在 unlearning 后加入 tool-mediated recovery 验收 |
| [Benchmarking Composable Compression Techniques in Mixture-of-Experts LLMs](https://arxiv.org/abs/2608.21693v1) | 2026-08-25T08:00:00+08:00 | 证明 expert pruning、weight quantization 与 KV compression 的组合效果不能由单项结果推算；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；加入 composed transformation 的联合评价合同 |
| [LLM4LLM: Bridging Kernel Benchmarks and Real Deployment via Closed-Loop Agentic Optimization](https://arxiv.org/abs/2608.21836v1) | 2026-08-25T08:00:00+08:00 | 将孤立 kernel benchmark 提升为真实 inference workload 内的 phase-aware patch 验收；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 的 deployment-aware kernel acceptance；旧 08-23 trace 已修正为 08-25 |
| [MemGuard: Persisting Verifier Signals for LLM-Agent Memory Governance](https://arxiv.org/abs/2608.21867v1) | 2026-08-25T08:00:00+08:00 | 将 verifier 信号持久化为 memory admission、conflict resolution、summarization 与 archival 元数据；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) 的 verifier-backed lifecycle；旧 08-23 trace 已修正为 08-25 |
| [MCP-Universe RL: A Framework for Training MCP Tool-Use Agents via Reinforcement Learning](https://arxiv.org/abs/2608.22167v1) | 2026-08-25T08:00:00+08:00 | 将 tool environment 生命周期与 tool-stalled rollout pipeline 纳入 RL 系统 owner；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md)；加入环境隔离、回收与 I/O stall overlap |
| [ClawProBench: Trace-Aware Evaluation of AI Agents with Runtime Coverage and Frozen Workplace-Style Holdouts](https://arxiv.org/abs/2608.22510v1) | 2026-08-25T08:00:00+08:00 | 将被测对象定义为 model-plus-runtime，并以 frozen holdout、trace 与 safety gate 分离一次成功和稳定能力；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 runtime-native evaluation；旧 08-24 trace 已修正为 08-25 |
| [NeuroPrefetcher: Storage-Aware Sparse LLM Inference via Delta Prefetching](https://arxiv.org/abs/2608.22643v1) | 2026-08-25T08:00:00+08:00 | 在模型长期大于内存时，以跨 token 稀疏活动局部性驱动 NVMe delta row prefetch；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)；加入 storage-backed weight residency 与 prediction-miss fallback |
| [Risk-Aware Reranking for Agentic Tool Retrieval](https://arxiv.org/abs/2608.22751v1) | 2026-08-25T08:00:00+08:00 | 将 query relevance 与 tool exposure risk 分离并显式调节安全/效用 operating point；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) 与 PLATFORM-SECURITY Ch72 的 discovery、exposure 与 authorization 分层 |
| [FOVEA: Focused On-Demand Visual Evidence Adaptation for Cache-Friendly Multimodal Speculative Decoding](https://arxiv.org/abs/2608.22883v1) | 2026-08-25T08:00:00+08:00 | 以可复用视觉 memory 和 draft-state 条件检索替代固定视觉 budget，改变多模态 speculation 的 proposal state；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)；加入视觉证据预算、cache identity 与 target verification 边界 |
| [Buried in Textual Debt: Context Pruning with Visual Evidence Preservation for MLLM Agents](https://arxiv.org/abs/2608.22963v1) | 2026-08-25T08:00:00+08:00 | 用 goal-conditioned summary 与 KL replay 判断可删除 reasoning text，同时保护视觉证据；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) 的 typed/goal-conditioned pruning 与 raw-evidence fallback |
| [A Physical Response-and-Memory Model for Muon Optimization](https://arxiv.org/abs/2608.22994v1) | 2026-08-25T08:00:00+08:00 | 以响应介质与多时间尺度 memory 解释 Muon momentum，并提出 Bi-Maxwell 分支；2 + 2 + 2 = 6 | 标准完成 | 仅报告：TRAIN-PRETRAINING，[Ch28](../../../../books/part-04-training-system/28-pretraining.md)；受限 benchmark 不足以形成通用 optimizer 结论 |
| [Chimera: Efficient Multi-Vector Retrieval via GPU-CPU Co-Processing](https://arxiv.org/abs/2608.23553v1) | 2026-08-25T08:00:00+08:00 | 将低精度候选生成驻留 GPU、高精度数据驻留 CPU，并重叠异构 scoring 以避免向 GPU 搬运全向量；3 + 3 + 2 = 8 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md)；加入 multi-vector retrieval 的 heterogeneous data plane 与 recall/latency contract |

## 4. 证据与知识整合

### [WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs](https://arxiv.org/abs/2608.22704)

当前修订版仍支持核心结论：long-form speech 的 prefill attention 排名不能可靠代表 decode-time usefulness；少量 anchor heads 充当在线 observer，CPU complement 保存被驱逐 chunk 以便后续召回。作者结果限两个 3B speech backbones、LibriSpeech-Long 与其 CPU–GPU 路径，不能外推为所有模型在相同 retention 下无损。收益是将 eviction 变为可恢复状态，代价是 host capacity、迁移调度与 observer 误判；Ch45 已完整承载。

### [The Compaction Cliff in Long-Running AI Agent Memory](https://arxiv.org/abs/2608.22752)

论文显示 episodic log 与 safety rule 若使用同一压缩策略，递归 compaction 会优先损害需要 exact wording 的控制状态。TypeCompact、TypeDecompose 与 TypeRetrieve 的受限实验支持按类型选择压缩、复制或 pinning；不证明作者比例跨模型、语言或私有 policy 成立。Ch75 已把 safety rule、authorization、schema 与一般历史分型，并要求 raw evidence fallback。

### [TailSieve: Partial-Rollout-Guided Tail Routing for LLM Rollouts](https://arxiv.org/abs/2608.22788)

该研究优化的是 rollout step 的 group makespan：用 partial history 识别长尾组，再联合决定隔离数量和 replica split。五个 Qwen 配置及单台八卡实验只支持给定 rollout/runtime 的收益，ragged verification、预测误差和 CUDA graph overhead 仍是边界。Ch33 已把 partial rollout 视为可恢复 trajectory state，并保留同步小规模路径。

### [AgentFlow: A Flow-Centric Policy Language and Framework for Securing LLM Agent Systems](https://arxiv.org/abs/2608.22868)

AgentFlow 用带标签运行时边、path rule、task-scoped capability 和 stateful taint 表达敏感数据允许流向，并由 reference monitor 执行。它只约束 policy-visible flow；overtaint、未建模 side effect、policy completeness 与 covert channel 未被消除。Ch72 已将模型/judge 与 authorization owner 分离，并覆盖跨步骤 cumulative effect，故无需再次追加框架名。

### [The Mask Is Not the Model: Auditing Prefix Invariance in Attention, State-Space, and Hybrid Sequence Models](https://arxiv.org/abs/2608.22876)

论文形式化 prefix invariance，并通过两次 forward pass 给出逐层定位分数，说明正确 causal mask 并不能覆盖 scan、aggregation 或 normalization 中的未来泄漏。受控 fault injection 支持 audit 的局部有效性，不证明同类缺陷的普遍发生率。Ch17 已把因果性写成跨算子数据流属性，而非 attention-mask 配置声明。

### [When Can Agents Safely Checkpoint, Fork, Restore, and Merge?](https://arxiv.org/abs/2608.22928)

形式模型强调 execution edit 只能改变未来分支，不能撤销已批准权限或已发送 tool request；错误 restore/merge 会重复动作、丢依赖结果或合并冲突状态。exact checker 与证明只覆盖其有限语义，现实异步副作用仍需 idempotency、compensation 与 reconciliation。Ch81 已明确 event-log replay、外部状态共同恢复和最终 commit authority。

### [The Laws of Context Allocation](https://arxiv.org/abs/2608.23252)

工作以 leave-one-out probe 区分“证据可见”与“生成确实使用”，再把检索、上下文预算与停止放入闭环调度。结果绑定给定 generative-search 任务与模型，probe 仍是 attribution estimator，不等同因果真值。Ch76 已用 relevance、sufficiency、cost 与 stopping 的联合 policy 表达同一长期机制。

### [InjecMEM: Memory Injection Attack on LLM Agent Memory Systems](https://arxiv.org/abs/2608.23471)

攻击通过 topical anchor 和 adversarial command 让一次输入成为以后相关 query 可召回的持久状态。实验覆盖多个 memory system/backbone，但真实长期用户流、rewrite-heavy memory 与独立防御未建立。它证明 memory write 是安全入口，不证明所有实现同样脆弱；Ch77 已把 write、retrieval、provenance、ACL 与 repair 分开。

### [The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams](https://arxiv.org/abs/2608.23541)

在匹配预算的 11 个 verifier-scored tasks 中，完整方案共享会让不同模型一轮内趋同，独立 proposal 保留 diversity；critique 只在 violated rule 可识别和修复时有用。证据不支持“所有通信有害”，而支持先定义通信目的、时机与 verifier。Ch82 已沿这条演进组织多 Agent 设计。

### [Best Practice Critic Optimization](https://arxiv.org/abs/2608.23566)

BPCO 将常见 critic instability 拆为 value range、target、normalization、response-length weighting、input 与 clipping 的组合，并通过 1.5B sanity test、40.3K math data 和 30B-A3B MoE 对照展示 single-rollout critic 的条件可行性。它不证明 critic 跨 reward、environment 与规模普遍稳定。Ch32 已保留 PPO 在 credit fidelity 优先时的成立条件，以及相对 GRPO 的方差、计算和过拟合 trade-off。

### [KVBoost: Chunk-Level Key-Value Cache Reuse with Deviation-Guided Recomputation](https://arxiv.org/abs/2608.21362)

论文把 exact prefix identity 与 position-independent content identity 分开：前者可直接复用，后者必须以 seam/deviation probe 选择性重算后才能提交。Qwen2.5-3B、1,000 个 bug-localization 样本与单 RTX 4060 的结果只证明该实现域，不支持“任意 RoPE 模型生产就绪”或普遍无质量损失。Ch45 已有 prefix/cache identity 主干，但缺 arbitrary-position reuse 的强制修复边界，建议在该处吸收。

### [There Is No Neutral Harness](https://arxiv.org/abs/2608.21382)

作者固定题目、权重与 greedy decoding，只改变 26 种同样可辩护的 prompt/option/scoring 配置，并在 12 个模型、3,679 个题目上把排序差异定位到 item level。它证明受测榜单的 gap 大量由 config-fragile items 承载，不证明所有 benchmark 都失效。Ch66 已拥有 harness identity，新增价值是发布排序前必须报告 per-item fragility 与 stable-item ranking。

### [Let Credit Follow Computation](https://arxiv.org/abs/2608.21501)

该工作将 evidence、transport operator 与 update geometry 解耦，让 detached attention statistic 参数化 causal credit kernel，并以 transport-aligned critic 消费 actor hidden/routing state。五个 Qwen3-4B seeds 与有限 Llama/Qwen 设置支持 interaction 效果，但 attention concentration 不等同因果责任，也未覆盖开放环境。建议作为 Ch32 中 fixed GAE 与 group broadcast 之间的条件分支，而非 PPO 的普遍替代。

### [Tensor Seeks Layout](https://arxiv.org/abs/2608.21555)

论文把 operator execution 与 tensor conversion 的总成本写成 dataflow-graph 全局优化，证明一般问题困难、bounded treewidth 可精确求解，并用 MaxSAT 逼近一般实例。最重要的系统结论是：solver 已优化声明目标仍落后时，差距暴露的是 cost model 而非搜索。证据绑定作者生产编译器和披露 workload；建议 Ch49 将 layout identity、global plan、profile revision 与 cost-model validation 串成一条链。

### [SAEM: Stage-Aware Expert Management](https://arxiv.org/abs/2608.21614)

SAEM 利用 chain-of-thought 相邻阶段的 expert activation coherence，联合 stage detection、expert cache、token repacking 与 CPU in-situ execution。作者吞吐仅绑定数学/科学 reasoning、受限显存和校准分布，且匹配 calibration 时收益更高，说明 stage predictor drift 是关键 failure。建议在 Ch54 加入 stage-aware residency；稳定短请求或激活不可预测时仍回到 token-local cache/offload。

### [PowerSlider](https://arxiv.org/abs/2608.21719)

材料把移动 power cap 分配到 compute-bound prefill、KV-constrained thinking 和 memory-bound answer decode，并以 Flex SLO、在线优化及 power-gating fail-safe闭环。SGLang 与生产 trace 结果不能外推不同 GPU、grid 或 SLO，但足以说明 energy average 不能替代 instantaneous power authority。建议 Ch56 新增 phase-aware power scheduling，并保留静态 cap/priority shedding 为可预测回退。

### [Reinforcement Learning on Benign Facts Amplifies Leakage of Memorized Private Data](https://arxiv.org/abs/2608.21727)

实验先确认 instruct 模型已记忆但较少输出 PII，再只用不含 PII 的事实做 RLVR，观察 targeted 与 free-recall extraction 上升。它证明 post-training 能改变既有记忆的可访问性，不证明所有 RLVR 都产生同幅度泄漏，也不说明 reasoning 或 refusal 指标足以发现该风险。建议 Ch72 把 privacy gate 从“训练数据是否含 PII”扩展为 pre/post-training extraction audit。

### [Evaluation Awareness in Language Models](https://arxiv.org/abs/2608.21766)

六个开源模型中 evaluation/deployment prompt 可由 residual-stream probe 区分，但内部表示、输出 verbalization 与 steering effect 并不一致；Olmo checkpoints 还显示该表示在 base 阶段已存在、后训练改变其稳定性和可控性。probe AUROC 不等于模型“知道自己在被测”的完整因果证明。建议 Ch66 将三类 signal 分开，并把 deployment-like slice 纳入外推 Gate。

### [Counterfactual Quotient Models](https://arxiv.org/abs/2608.22092)

方法把不同 action future 中共同变化的成分取商，只保留 action-dependent effects，并在同步 counterfactual rollout 条件下给出 decision sufficiency 与 regret 性质。理论依赖 reward family 和 counterfactual access，物理环境实验只是初步证据。Ch25 已明确 action-conditioned、counterfactual 与 control sufficiency 的责任边界，因此无需重复正文。

### [What actually runs: a measurement study of language model placement and decode speed on the Apple Neural Engine](https://arxiv.org/abs/2608.22110)

研究以等价 graph-expression sweep、匹配训练 artifact 和 ANE memory-controller 计数交叉核验 placement，说明编译器意图与真实设备执行可能不同，encoding 还会改变 residency 和 decode byte budget。结果只覆盖作者 CoreML/ANE 与小模型，不可外推 CUDA 或大模型。建议 Ch49 在 execution-plan validation 中加入 hardware-counter authority 与 byte-stream accounting。

### [RAG Collapse](https://arxiv.org/abs/2608.22118)

三类 simulation、三个模型家族和 1,019 个信息请求显示系统会偏好引用自己生成的材料，进而在反复检索中降低 response diversity；控制 reference quality 后 self-bias 仍存在。它不证明真实 Web 的固定 collapse 概率，也未覆盖独立 provenance admission。建议 Ch76 把 author/model provenance 写入 retrieval identity，对 self-authored evidence 限额、隔离或引入独立来源。

### [Model of Models: When Does Emitting a Specialist Beat Attending, Adapting, or Tuning?](https://arxiv.org/abs/2608.21386v1)

exact-v1 在 matched budget 下比较 zero-shot、ICL、gradient adaptation 与直接生成 LoRA specialist：低维、可跨样本复用的 adaptation 更适合 emission，高维或长序列 specialist 则被生成误差压垮。它证明的是一种受任务维度、复用次数和生成成本约束的分支，不证明 emitted weights 普遍替代训练；Ch30 已加入这条 operating-regime 分界。

### [Selective Cross-View Consistency for World Action Models](https://arxiv.org/abs/2608.21402v1)

方法只约束跨视角不应变化的 latent state，并允许 observation block 随 camera 变换；对 covariant 输出强行一致反而损害 held-out viewpoint control。证据绑定作者的 viewpoint split 与任务，不证明一般 3D invariance；Ch25 已有 state/observation 与 action-conditioned 边界。

### [Retrieval Needs Multivectors: An Exponential Separation](https://arxiv.org/abs/2608.21494v1)

理论构造给出单向量相似度与 token-level multi-vector matching 的指数表达差距。它支持“representation choice 是检索能力约束”，不直接证明某个 late-interaction index 在真实语料更快或更准；Ch76 已把表达收益与索引、存储和 rerank 成本并列。

### [The geometry of AI validation](https://arxiv.org/abs/2608.21496v1)

exact-v1 给出 iid best-of-N search 在有限验证集上的可认证边界，说明反复选择会耗尽 holdout 的独立性。结论依赖其搜索与分布假设，不能直接量化开放式研发的真实过拟合率；Ch66 已有 adaptive selection 与 holdout exhaustion。

### [SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation](https://arxiv.org/abs/2608.21500v1)

方法从当前 policy 遭遇的自适应攻击轨迹蒸馏 token-level defensive behavior，并在作者攻击集上优于静态数据训练。它没有消除未见攻击、policy drift 或 tool effect 风险；Ch72 已要求 learned defense 与外部 capability/authorization 共存。

### [Beyond Sparse Weights: When Is Attention Compressible?](https://arxiv.org/abs/2608.21541v1)

论文指出小 attention weight 仍可乘上大 value 形成不可忽略贡献，并以 omitted-value statistic 约束丢弃误差。该结论直接修正只看 attention mass 的 eviction heuristic；Ch45 已加入 value-aware compressibility condition，并保留 workload/model/quality calibration。

### [Evidence-State Reliability Under Controlled Degradation](https://arxiv.org/abs/2608.21559v1)

受控改变中间 evidence 时，pipeline 仍可产生 parser-valid 输出而结论状态已失真。实验支持把 syntax、evidence state 与 final verdict 分层检查，不证明其故障率可外推生产；Ch66 已用分层 fault injection 与独立 evidence-state oracle 承载该边界。

### [Reading the Room: Implicit Confusion Encoding in Recurrent World Model States](https://arxiv.org/abs/2608.21582v1)

probe 与 causal edit 显示 recurrent world-model state 可编码部分 confusion signal，但跨任务迁移和稳定可控性有限。可读表示只是 sensor，不自动成为 planning authority；Ch25 已有这一边界。

### [Measuring Activation Control in Large Language Models](https://arxiv.org/abs/2608.21664v1)

作者将可线性预测、可干预改变与目标行为改变拆成 matched tests，暴露只报告 probe accuracy 的混杂。结果依赖选定层、方向与行为任务；Ch66 已将 monitor、actuator 与 behavior outcome 分离，不支持普遍可控性。

### [Context as an Environment](https://arxiv.org/abs/2608.21690v1)

该设计把长程上下文变为 append-only events、typed persistent namespace 与按读者生成的 projection。它以更清楚的 revision/replay 换额外存储、schema 与 projection failure；短任务和低风险会话仍可使用直接 prompt assembly。Ch75 已承载这一长期状态分支。

### [Prompt-Based Abstention Fails Under Misleading Context](https://arxiv.org/abs/2608.22228v1)

配对实验显示 prompt 可使缺证据时拒答，却会在提供错误但流畅证据时恢复自信回答。结论只覆盖受测小模型/RAG 设置，但足以证明 abstention 需要 contradiction/evidence gate；Ch76 已有相同主干。

### [Beyond Dense Adam States](https://arxiv.org/abs/2608.22322v1)

log-space optimizer-state quantization 以 update error 和训练 loss 而非压缩率独立验收，并揭示 state distribution/scale 的适用边界。证据不支持所有 optimizer 或低比特格式；Ch36 已把 optimizer state 纳入分布式 memory/precision contract。

### [Noise Floor Audit for Agent Benchmarks](https://arxiv.org/abs/2608.22331v1)

论文把模型差异与重复运行、judge 和 harness 引入的方差对照，部分小幅排序落入 noise floor。它不否定所有 Agent benchmark；长期结论是 Ch66 已有的 repeated-run uncertainty 与 practical significance。

### [When Not to Imitate: Boundary-Aware Skill Memory](https://arxiv.org/abs/2608.22339v1)

方法把 successful trace 与适用的 tool/state boundary 一同存入 skill memory，仅在前置条件匹配时复用。作者任务不能证明开放环境的 boundary detector 可靠；Ch77 已把 applicability predicate 纳入 experience-to-skill promotion、检索与回滚。

### [Where World Models Break: Natural-Input Failure Discovery](https://arxiv.org/abs/2608.22421v1)

自然输入搜索发现了常规生成质量指标和合成扰动未覆盖的动态失败簇。发现器自身可能偏向可搜索区域，不能给出总体故障率；Ch25 已将 failure discovery 与 causal/control evaluation 分开。

### [Claim-Level Confidence Calibration for Reliable Decision Making with Large Language Models](https://arxiv.org/abs/2608.22483v1)

工作将长答案拆成 atomic claims 后分别校准，再按决策目标聚合，避免把非独立 claim 概率机械连乘。它不赋予模型事实真值，且校准只在匹配分布内成立；Ch66 已承载 claim graph 到 decision confidence 的合同。

### [Understanding the Synchronization Tax in GPU Scale-Up Domains](https://arxiv.org/abs/2608.22503v1)

论文把计算、collective service 与 barrier waiting 分开，显示扩大 scale-up domain 会因 tail imbalance 放大同步税。收益数字受拓扑、collective、模型和 batch 约束；长期机制是 parallel degree 的收益必须扣除同步尾部，Ch37 已加入这一显式 accounting。

### [NOVA](https://arxiv.org/abs/2608.22613v1)

作者针对 Attention、SSM 与 MoE 的不同 data movement 设计 near-memory execution/placement。其评估是披露架构与模拟域，不证明生产芯片优势；Ch49 已只吸收异构算子全局 plan 与回退边界。

### [CAI-DLLM](https://arxiv.org/abs/2608.22646v1)

方法根据中间状态的 convergence signal 动态停止 diffusion LM 迭代，用额外判定误差换 latency。作者结果不提供跨模型统一阈值；Ch24 已有 iterative correction、adaptive stopping 与 quality rollback。

### [Think Only When Needed](https://arxiv.org/abs/2608.23224v1)

VLA controller 只在不确定阶段切入慢推理，并恢复 canonical compact prompt，避免 prompt form 漂移拖慢实时 loop。它不证明所有机器人 policy 可安全由语言不确定性触发；Ch26 已吸收 fast/slow prompt authority 与 fail-safe handoff。

### [Credal Large Language Models for Semantic Commitment under Uncertainty](https://arxiv.org/abs/2608.23244v1)

adapter ensemble 构造 uncertainty set，区分 token probability 与 semantic commitment，并用于 selective prediction。结果受 ensemble diversity 和 calibration distribution 限制，不能作为通用 truth confidence；Ch66 已将其定位为受限 uncertainty sensor。

### [Sigmoid Attention as a Better Substrate for Learned KV Cache Eviction](https://arxiv.org/abs/2608.23296v1)

作者表明 softmax 的相对归一化会让 soft importance 与 hard deletion 之间相互耦合，sigmoid attention 在其训练/推理设置中更容易校准 learned eviction。它不证明架构迁移对现有 checkpoint 免费；Ch45 已记录 normalization 与 eviction policy 的联合 identity。

### [Adversarial Entropy Inflation Against Gumbel-Based Inference Verification](https://arxiv.org/abs/2608.23375v1)

攻击者可主动放大 entropy，使依赖 sampling stability 的 verifier 失去原有保证。理论与实验只覆盖相应 threat model；Ch66 已要求 uncertainty proxy 不能拥有最终 correctness authority。

### [When “Do Not” Is Not Deny](https://arxiv.org/abs/2608.23550v1)

matched cases 显示 CLAUDE.md 等自然语言禁止条款与 built-in control 的实际阻断率显著不同。结果受产品版本和任务集限制，但支持稳定原则：prompt 是行为建议，capability gate 才拥有 deny authority；Ch72 已明确该 enforcement-owner 边界。

### [CacheRouter: A Dual-Path Tool Routing Architecture with Cache-Preserving Main-Model Isolation for Long-Tail Tool Discovery](https://arxiv.org/abs/2608.22708v1)

该原型把主模型固定 core-tool 前缀与长尾 router 通道分离，以维持 prompt-cache identity。55 个功能查询与一段 30-turn 对话只能证明特定实现可行，且成本结论绑定厂商缓存计价；新增 router 还引入发现错误、权限和结果归因边界，因此仅作为 Ch78 的受限案例保留。

### [CatchBench: When Can an Agent Failure Be Caught?](https://arxiv.org/abs/2608.22808v1)

CatchBench 将可审计证据分为运行前配置、进行中 trace prefix 与完成后 trace，且不同状态使用不同任务合同，不强行生成统一榜单。72 个 entrants 与 1,162 runs 同时暴露 corpus shortcut 和无法排序的对照；它证明 audit ceiling 受记录状态限制，Ch66 已有对应 observation/label-provenance 边界。

### [What Process Evaluation of Coding Agents Actually Measures: Action, Task, and Step Are Three Different Levels](https://arxiv.org/abs/2608.22960v1)

作者用 prefix-conditioned replay 与受控 judge-information 干预分离 action prediction、task uncertainty 和 step attribution，并在 499 个 episode 中观察到 full-trace collider bias。样本只覆盖 12 个仓库，不能外推所有 coding agent；其长期结论已由 Ch66 的评价单位、干预证据和因果归因合同承载。

### [Pointing-VLA: Typed Spatial Grounding Interfaces for Vision-Language-Action Manipulation](https://arxiv.org/abs/2608.23138v1)

Pointing-VLA 用点、热图和轨迹 heads 直接输出 typed spatial state，避免以自回归文本序列承载几何接口。Bridge/WidowX 与有限真实抓放只支持这类接口在受测控制栈中的收益，不能证明可跨 embodiment 泛化；故仅作为 Ch26 的受限 implementation branch。

### [Is Next-Chunk Reasoning RL Really Better than SFT? Revisiting Training Strategies under no-CoT Data](https://arxiv.org/abs/2608.23256v1)

受控实验用 Mixed SFT 对照 next-chunk reasoning RL，显示先前增益可能来自更有效的数据暴露，并报告大幅训练算力差异。结论绑定 no-CoT 数学推理数据与后续 RLVR，不足以否定其他 RL objective；只保留为 Ch29 的条件化替代证据。

### [SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository Stack Migration?](https://arxiv.org/abs/2608.23564v1)

三阶段 protocol 先确认迁移确实发生，再验证固定行为，最后由独立 agents 生成隐藏差异测试，从而阻止“复制旧实现让测试通过”的 shortcut。20 个任务和 520 runs 只证明受测 stack-migration workload；Ch66 已拥有 process-completeness、behavioral correctness 与 adversarial verification 的分层 Gate。

### [ReWorld: An Interactive World Model with Long-Horizon Memory](https://arxiv.org/abs/2608.23565v1)

ReWorld 以局部 attention heads 维持实时控制、少量 global heads 与 pose-indexed landmark bank 维持长期回访，并用 action-following、recall、video quality 三轴评价。固定 12-chunk cache 的结果绑定作者数据引擎与 rollout；它支持 Ch25 已有的局部 dynamics、持久状态和 action-conditioned evidence 分工。

### [Forgotten in Weights, Recovered by Tools: Agentic Tool Unlearning for LLM Agents](https://arxiv.org/abs/2608.21544v1)

ATU 先压低参数直接 recall，再在模拟 tool environment 中对寻回目标的 trajectory 与最终泄漏施加 RL 惩罚，揭示“权重忘记”不是 Agent 端到端遗忘。RWKU/MUSE 与模拟工具不证明真实开放环境不会旁路恢复；Ch72 已加入 tool-mediated recovery 的 unlearning release gate。

### [Benchmarking Composable Compression Techniques in Mixture-of-Experts LLMs](https://arxiv.org/abs/2608.21693v1)

MoEXBench 在 10 个 30B～235B MoE 上组合 expert pruning、weight quantization 与 KV precision，显示组合质量和运行收益不能从单项比例相加。commodity hardware、公开模型和给定 workload 限制外推；Ch66 已要求对 composed transformations 冻结模型、压缩链、硬件和 slice，而非只报告平均压缩率。

### [LLM4LLM: Bridging Kernel Benchmarks and Real Deployment via Closed-Loop Agentic Optimization](https://arxiv.org/abs/2608.21836v1)

系统从真实 inference script 提取 phase-aware 优化任务，并只接受通过 in-model validation 的 patch，直接暴露 standalone kernel benchmark 与部署行为的差距。A100/H100 上 10 个 workload 的结果不足以证明通用 speedup；Ch49 已将 kernel 候选、真实 execution plan 与部署验收分开，归属 trace 应回拨本日。

### [MemGuard: Persisting Verifier Signals for LLM-Agent Memory Governance](https://arxiv.org/abs/2608.21867v1)

MemGuard 把 reward、confidence、label 和 uncertainty 持久附着到 memory record，并在 admission、retrieval、conflict resolution、summarization 与 archival 中复用。四类 benchmark、四个 backbone 与五个 seeds 支持其生命周期机制，不证明 verifier 在开放分布可靠；Ch77 已吸收 persistent verifier metadata，归属 trace 应回拨本日。

### [MCP-Universe RL: A Framework for Training MCP Tool-Use Agents via Reinforcement Learning](https://arxiv.org/abs/2608.22167v1)

框架把 MCP environment 的 provisioning、isolation、recycling 与 tool-stalled trajectory pipeline 独立于 RL backend，并通过并发 overlap 提高 GPU 利用。三类任务与两种 backend 只证明框架可组合；Ch33 已加入 environment identity、I/O wait、rollout staleness 和回收失败的运行合同。

### [ClawProBench: Trace-Aware Evaluation of AI Agents with Runtime Coverage and Frozen Workplace-Style Holdouts](https://arxiv.org/abs/2608.22510v1)

ClawProBench 把 subject identity 定为 model-plus-runtime，保留 execution trace，并分离 live profile、frozen holdout、safety-gated score 和 strict repeated pass。OpenClaw 单一 runtime 不代表所有 Agent；Ch66 已以 runtime-native identity 与 trace evidence 承载该结论，归属 trace 应回拨本日。

### [NeuroPrefetcher: Storage-Aware Sparse LLM Inference via Delta Prefetching](https://arxiv.org/abs/2608.22643v1)

当模型始终大于可用内存时，NeuroPrefetcher 预测下游 MLP sparse activity，只从 NVMe 读取相对 resident buffer 新出现的 weight rows。真实 unified-memory edge hardware 支持 storage-aware delta prefetch，但 82～85% locality 和 7.9～12.0 倍收益绑定模型、稀疏方案与设备；Ch54 已保留 prediction miss、I/O deadline 和 dense fallback。

### [Risk-Aware Reranking for Agentic Tool Retrieval](https://arxiv.org/abs/2608.22751v1)

方法在冻结 first-stage retriever 后分别估计 query relevance 与 tool exposure risk，并通过显式参数与规则过滤给出不同 operating point。6,108 个标注工具只证明其风险 taxonomy 下的候选暴露变化，不能替代执行权限；Ch78/Ch72 已分别拥有 discovery 与 effect authorization。

### [FOVEA: Focused On-Demand Visual Evidence Adaptation for Cache-Friendly Multimodal Speculative Decoding](https://arxiv.org/abs/2608.22883v1)

FOVEA 建立可复用 visual memory，按 draft hidden state 动态选取有界证据并通过 residual correction 影响 proposal，而不把视觉 token 插回 AR context。最多 2.13 倍只适用于受测 VLM 与 benchmark；Ch48 已将 visual-memory identity、selection budget、draft acceptance 和 target verification 连接起来。

### [Buried in Textual Debt: Context Pruning with Visual Evidence Preservation for MLLM Agents](https://arxiv.org/abs/2608.22963v1)

SPARE 用 task-state summary 作为诊断上下文，通过原上下文/summary-conditioned replay 的 KL 差异判断 reasoning segment 是否可删，并保留视觉证据。删减率绑定受测多模态工具任务，且 summary 会成为新的错误源；Ch75 已有 goal-conditioned projection、不可恢复删除和 raw-evidence fallback。

### [A Physical Response-and-Memory Model for Muon Optimization](https://arxiv.org/abs/2608.22994v1)

论文将 Muon 的 semi-orthogonal update 解释为给定输出侧安全预算的耗散响应，并用多时间尺度 memory 推导 Bi-Maxwell optimizer。证据主要来自公开 optimizer benchmark 与 8 条 probe trajectory，物理类比并未证明普适动力学；故仅作为 Ch28 的 experimental optimizer case，不改写通用更新规则。

### [Chimera: Efficient Multi-Vector Retrieval via GPU-CPU Co-Processing](https://arxiv.org/abs/2608.23553v1)

Chimera 将低精度压缩码常驻 GPU 做候选生成和过滤，将高精度数据留在 CPU，并通过协同 scoring 避免查询时搬运全向量。最高 59.5 倍 QPS 绑定作者数据集、recall 点和硬件；Ch76 已加入 multi-vector retrieval 的 heterogeneous data plane，并保留 recall/latency/host-memory 共存边界。

## 5. 缺口与下一步

无

1,022 个唯一身份已经按完整题目与摘要完成语义准入，最终分母为 64；64/64 均已完成 exact-v1 HTML/PDF、机制、评价、限制与 withdrawal 核验，当前页面未见 withdrawn 标记。最终处置为：34 项已有覆盖，26 项完成 Books 整合，4 项仅报告。其余身份以范围外、单领域应用、局部指标改进或重复现有长期命题等具体理由在分母前关闭。

此前漏失的 19 项已经全部恢复到候选表与 Source Review；其中 LLM4LLM、MemGuard、ClawProBench 的 owner 归属已按官方首次公告回拨本日。没有待补材料、待审证据或待写 Books 条目。

## 6. 复核

复核者：fresh-context 独立智能体
结论：通过

独立回放确认窗口为 `2026-08-24 09:00～2026-08-25 09:00`（Asia/Shanghai），1,022 个 arXiv 唯一身份按 official-announcement owner 归属本日；64 个候选均属于该批次，表格与 64 个 Source Review 一一对应，V2 加总和审阅路由一致。64/64 的 exact-v1 HTML 或 PDF 可访问，未见 withdrawn 标记。

false-negative 复核恢复了 19 项；false-positive 复核将 7 个重复写作建议降为已有覆盖，没有把论文名称新颖误当成知识增量。26 个 `Integrate` 均在正确 canonical owner 的机制正文中形成可定位的 Why/Mechanism/Trade-off/Evidence boundary；其中 Chimera 最初被错误绑定到 evidence-realization 段，已纠正为 Ch76 的 GPU/CPU 异构 multi-vector retrieval data plane，并与 AtlasNav 的 persistent navigation 分离。4 个仅报告案例均保留了不能进入长期正文的明确边界。

本日报的来源、候选分母、证据、Books 写回与写后语义审计均已闭合。
