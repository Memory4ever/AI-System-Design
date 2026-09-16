# 2026-05-05 V3 Proposition-level Books Comparison

状态：作者侧对照完成；Proposed 等待 root 写回，全部结果等待 fresh-context 非作者最终复核。

## `SF-2026-ARXIV-2605-00827` — Separating Intelligence from Execution: A Workflow Engine for the Model Context Protocol

- Owner：`AGENT-MCP` / Ch83 / `books/part-07-agent/83-mcp.md`。
- 现有命题：协议发现、能力身份、授权和真实 effect 必须分层验收
- 差异判断：现有命题已经规定：协议发现、能力身份、授权和真实 effect 必须分层验收。本来源的受限增量是“以声明式 blueprint 和幂等执行器把 MCP 智能提议与工作流执行分开”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-00831` — GhostServe: A Lightweight Checkpointing System in the Shadow for Fault-Tolerant LLM Serving

- Owner：`INFER-KV-CACHE` / Ch45 / `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`。
- 现有命题：KV 离开可靠 HBM 或需要故障接管时，保护预算、checkpoint identity、恢复路径与 failover commit 必须显式化。
- 差异判断：GhostServe 的 host-memory erasure-coded shadow checkpoint 是后台保护的具体实现；现有小节已经拥有可靠性分层、恢复/重算与状态身份，故不改变长期命题。 仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-00832` — Synthetic Designed Experiments for Diagnosing Vision Model Failure

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“把可控合成生成器当作实验装置，用因子设计区分 coverage gap 与 spurious dependency 并定向补数”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-00836` — From Euler to Dormand-Prince: ODE Solvers for Flow Matching Generative Models

- Owner：`MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 / `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。
- 现有命题：本章已把 sampler、step schedule、误差控制和 NFE/质量前沿定义为生成执行合同，旧 Euler 在低预算与误差容忍场景仍成立
- 差异判断：exact-v1 的新增证据是“把 flow-matching 采样器从固定 Euler 步进提升为可比较的高阶与自适应 ODE 求解器，并以 NFE-quality frontier 暴露模型误差与数值误差的共同上限”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。
- 处置：`No Change — Existing Coverage (proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-00842` — Understanding Emergent Misalignment via Feature Superposition Geometry

- Owner：`WORLDVIEW-REPRESENTATION` / Ch5 / `books/part-01-worldview/05-what-neural-networks-learn.md`。
- 现有命题：表示存在、可读出与被当前路径实际使用是三个不同命题
- 差异判断：现有命题已经规定：表示存在、可读出与被当前路径实际使用是三个不同命题。本来源的受限增量是“非正交 superposition 使目标微调沿几何邻近方向产生 gradient spillover”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (marker verified)`。

## `SF-2026-ARXIV-2605-00884` — LiteVLA-H: Dual-Rate Vision-Language-Action Inference for Onboard Aerial Guidance and Semantic Perception

- Owner：`MULTIMODAL-EMBODIED-VLA` / Ch26 / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。
- 现有命题：慢语义状态与快动作路径必须分别持有 cadence、freshness 和安全回退，低层 controller 仍拥有执行 authority。
- 差异判断：现有小节已经给出同一双速状态合同、staleness identity、训练部署一致性与保守 controller 回退；LiteVLA-H 增加 Jetson 上 prefill-dominant 的受限测量和双任务训练案例，没有改变该长期命题。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-00914` — The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate

- Owner：`AGENT-MULTI-AGENT` / Ch82 / `books/part-07-agent/82-multi-agent.md`。
- 现有命题：消息、角色和局部成功不能替代共享状态的唯一提交语义
- 差异判断：现有命题已经规定：消息、角色和局部成功不能替代共享状态的唯一提交语义。本来源的受限增量是“同质 debate 暴露从众、上下文脆弱和投票丢失已有正确答案的三条失败路径”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-00935` — Watch Your Step: Information Injection in Diffusion Models via Shadow Timestep Embedding

- Owner：`MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 / `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-2026-ARXIV-2605-00939` — From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：本章已有事实正确性、校准与证据门，但缺少把错误的局部可修正性作为独立诊断信号
- 差异判断：现有正文仍缺：以参数梯度敏感度近似局部曲率，区分可被小扰动修正的普通错误与对输入改写仍稳定的 stubborn hallucination。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-2026-ARXIV-2605-00955` — E-MIA: Exam-Style Black-Box Membership Inference Attacks against RAG Systems

- Owner：`AGENT-RAG` / Ch76 / `books/part-07-agent/76-rag.md`。
- 现有命题：检索相关性、证据充分性、freshness 与 provenance 是不同 gate
- 差异判断：现有命题已经规定：检索相关性、证据充分性、freshness 与 provenance 是不同 gate。本来源的受限增量是“以可客观评分的 hard-evidence probes 推断 RAG 语料成员身份”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-00974` — SRTJ: Self-Evolving Rule-Driven Training-Free LLM Jailbreaking

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor
- 差异判断：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“分层规则记忆同时积累成功与失败攻击经验，使 jailbreak 策略跨目标持续演化”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-00994` — Most Current Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“用基模/微调模的 perplexity difference 暴露 model-organism 的微调目标”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01030` — Effect-Transparent Governance for AI Workflow Architectures: Semantic Preservation, Expressive Minimality, and Decidability Boundaries

- Owner：`AGENT-WORKFLOW` / Ch81 / `books/part-07-agent/81-workflow.md`。
- 现有命题：已知顺序与 invariant 应由 durable workflow 拥有，模型只处理开放决策
- 差异判断：现有命题已经规定：已知顺序与 invariant 应由 durable workflow 拥有，模型只处理开放决策。本来源的受限增量是“用 effect-transparent 语义边界约束 AI workflow 的表达能力与可判定性”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01032` — Algebraic Semantics of Governed Execution: Monoidal Categories, Effect Algebras, and Coterminous Boundaries

- Owner：`AGENT-PLATFORM` / Ch84 / `books/part-07-agent/84-agent-platform.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-2026-ARXIV-2605-01037` — Certified Purity for Cognitive Workflow Executors: From Static Analysis to Cryptographic Attestation

- Owner：`AGENT-PLATFORM` / Ch84 / `books/part-07-agent/84-agent-platform.md`。
- 现有命题：skill、run、tool effect 与 release/rollback 必须保持独立身份
- 差异判断：现有命题已经规定：skill、run、tool effect 与 release/rollback 必须保持独立身份。本来源的受限增量是“把静态 purity 证明签名成运行时可校验的执行凭证并显式保留 TCB”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01047` — LLM Ghostbusters: Surgical Hallucination Suppression via Adaptive Unlearning

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：本章已要求删除、抑制或修复后的能力保持与攻击复测共同进入 release gate；单一 package 工作负载没有改变该合同
- 差异判断：exact-v1 的新增证据是“把已观测 package hallucination 转成可定位的 post-deployment unlearning 对象，并用自适应 masking 限制能力 collateral damage”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。
- 处置：`No Change — Existing Coverage (proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01048` — Compared to What? Baselines and Metrics for Counterfactual Prompting

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“用 meaning-preserving perturbation 作为反事实 baseline，避免把表面改写误判为目标因素效应”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-LEAP-EARLY-EXIT-PRETRAINING-CONTRACT` — LEAP: Layer-wise Exit-Aware Pretraining for Efficient Transformer Inference

- Owner：`INFER-TENSORRT-LLM` / Ch49 / `books/part-05-inference-system/49-tensorrt-llm.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker and root-corrected trace verified; independent review pending`。

## `SF-2026-ARXIV-2605-01060` — SURGE: SuperBatch Unified Resource-efficient GPU Encoding for Heterogeneous Partitioned Data

- Owner：`INFER-GPU-MEMORY` / Ch54 / `books/part-05-inference-system/54-gpu-memory.md`。
- 现有命题：物理容量、逻辑状态和生命周期必须由不同 owner 记账
- 差异判断：现有命题已经规定：物理容量、逻辑状态和生命周期必须由不同 owner 记账。本来源的受限增量是“SuperBatch 在跨分区 embedding 中同时给出有界内存、流式首输出与故障恢复粒度”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01069` — Online Safety Filter for Deformable Object Manipulation with Horizon Agnostic Neural Operators

- Owner：`MULTIMODAL-EMBODIED-VLA` / Ch26 / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。
- 现有命题：行动闭环必须绑定 observation、action schema、控制频率与安全回退
- 差异判断：现有命题已经规定：行动闭环必须绑定 observation、action schema、控制频率与安全回退。本来源的受限增量是“用 task-level barrier function 在运行时最小修正具身策略动作，而不是把安全隐含进 reward”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01106` — Component-Aware Self-Speculative Decoding in Hybrid Language Models

- Owner：`INFER-SPECULATIVE-DECODING` / Ch48 / `books/part-05-inference-system/48-speculative-decoding.md`。
- 现有命题：proposal 可以近似，最终 commit 必须保持 target distribution 与唯一提交边界
- 差异判断：现有命题已经规定：proposal 可以近似，最终 commit 必须保持 target distribution 与唯一提交边界。本来源的受限增量是“hybrid model 的组件组合方式决定内部 draft 的可接受率与 self-speculation 可行性”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01111` — When Less is Enough: Efficient Inference via Collaborative Reasoning

- Owner：`INFER-SCHEDULING` / Ch56 / `books/part-05-inference-system/56-inference-scheduling.md`。
- 现有命题：本章已把模型路由写成按难度、质量预算和尾延迟升级的控制环，DUET 是该分支的受限实现
- 差异判断：exact-v1 的新增证据是“由小模型先执行、再按边际效用与长度惩罚决定是否升级大模型，把协作推理变成请求级资源控制”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。
- 处置：`No Change — Existing Coverage (proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01129` — Revisiting Privacy Leakage in Machine Unlearning: Membership Inference Beyond the Forgotten Set

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor
- 差异判断：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“unlearning 前后差分会把隐私泄漏从 forget set 扩展到 retain set”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01130` — Iterative Finetuning is Mostly Idempotent

- Owner：`TRAIN-PRETRAINING` / Ch28 / `books/part-04-training-system/28-pretraining.md`。
- 现有命题：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算
- 差异判断：现有命题已经规定：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算。本来源的受限增量是“连续 SFT/SDF 多数近似幂等，而持续 DPO 且不重置模型时才稳定放大特征”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01133` — When Embedding-Based Defenses Fail: Rethinking Safety in LLM-Based Multi-Agent Systems

- Owner：`AGENT-MULTI-AGENT` / Ch82 / `books/part-07-agent/82-multi-agent.md`。
- 现有命题：消息、角色和局部成功不能替代共享状态的唯一提交语义
- 差异判断：现有命题已经规定：消息、角色和局部成功不能替代共享状态的唯一提交语义。本来源的受限增量是“embedding 防御在多轮多 Agent 传播中衰减，暴露局部过滤并非系统安全边界”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01137` — Metric-Normalized Posterior Leakage (mPL): Attacker-Aligned Privacy for Joint Consumption

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-2026-ARXIV-2605-01148` — Arithmetic in the Wild: Llama uses Base-10 Addition to Reason About Cyclic Concepts

- Owner：`WORLDVIEW-REPRESENTATION` / Ch5 / `books/part-01-worldview/05-what-neural-networks-learn.md`。
- 现有命题：本章已区分表示几何、可干预电路与因果证明；该案例补充证据但不改变表示不等于算法所有权的边界
- 差异判断：exact-v1 的新增证据是“用跨任务 activation patching 与 Fourier probe 显示加法子电路可被循环概念复用，并定位稀疏 MLP 子电路”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。
- 处置：`No Change — Existing Coverage (proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01167` — Minimizing Collateral Damage in Activation Steering

- Owner：`WORLDVIEW-REPRESENTATION` / Ch5 / `books/part-01-worldview/05-what-neural-networks-learn.md`。
- 现有命题：本章已要求 steering 同时评估目标方向、旁路能力损失与分布外回退，COAST 没有改变该所有权边界
- 差异判断：exact-v1 的新增证据是“在保持目标 steering 幅度的约束面上最小化二阶 collateral energy，把 activation steering 写成受约束几何优化”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。
- 处置：`No Change — Existing Coverage (proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01172` — A Theory of Generalization in Deep Learning

- Owner：`WORLDVIEW-REPRESENTATION` / Ch5 / `books/part-01-worldview/05-what-neural-networks-learn.md`。
- 现有命题：本章已把低训练损失与泛化分离，并要求表征、优化轨迹和数据分布共同解释；理论模型未推翻该主线
- 差异判断：exact-v1 的新增证据是“把深度学习泛化拆成可被测试点看到的 signal channel 与训练集 reservoir，并用 drift-diffusion 与 train-test coupling 刻画误差”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。
- 处置：`No Change — Existing Coverage (proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01188` — Compute Optimal Tokenization

- Owner：`TRAIN-DATA` / Ch27 / `books/part-04-training-system/27-data.md`。
- 现有命题：数据来源、过滤、去重与 lineage 共同决定训练更新，而不是样本数量单独决定
- 差异判断：现有命题已经规定：数据来源、过滤、去重与 lineage 共同决定训练更新，而不是样本数量单独决定。本来源的受限增量是“compute-optimal allocation 随 bytes 而非 token 数缩放，token compression rate 成为训练变量”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01191` — Sentinel-VLA: A Metacognitive VLA Model with Active Status Monitoring for Dynamic Reasoning and Error Recovery

- Owner：`MULTIMODAL-EMBODIED-VLA` / Ch26 / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。
- 现有命题：异常监测只触发 plan、update 或 recover，必须绑定 observation revision、deadline 与安全回退，不能越过 action admission。
- 差异判断：现有小节已经明确正常状态复用、异常状态触发推理/恢复，以及 monitor 只持有 proposal 权；该论文提供一个四状态实现和持续学习案例，但没有改变状态 owner 或提交边界。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01192` — Linear-Readout Floors and Threshold Recovery in Computation in Superposition

- Owner：`WORLDVIEW-REPRESENTATION` / Ch5 / `books/part-01-worldview/05-what-neural-networks-learn.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-2026-ARXIV-2605-01194` — VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model

- Owner：`MULTIMODAL-EMBODIED-VLA` / Ch26 / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。
- 现有命题：行动闭环必须绑定 observation、action schema、控制频率与安全回退
- 差异判断：现有命题已经规定：行动闭环必须绑定 observation、action schema、控制频率与安全回退。本来源的受限增量是“uncertainty clutch 只在需要时切换到候选动作与相对 action critic 的 deliberation”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01195` — TAIL-Safe: Task-Agnostic Safety Monitoring for Imitation Learning Policies

- Owner：`MULTIMODAL-EMBODIED-VLA` / Ch26 / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。
- 现有命题：行动闭环必须绑定 observation、action schema、控制频率与安全回退
- 差异判断：现有命题已经规定：行动闭环必须绑定 observation、action schema、控制频率与安全回退。本来源的受限增量是“从状态-动作安全分数构造经验控制不变集，并在越界时触发 recovery”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01199` — Focus and Dilution: The Multi-stage Learning Process of Attention

- Owner：`MODEL-SELF-ATTENTION` / Ch14 / `books/part-02-model/14-self-attention.md`。
- 现有命题：本章已解释 attention score、竞争归一化和训练信号的相互作用；单层 Markov 理论属于机制证据而非新 owner
- 差异判断：exact-v1 的新增证据是“把 attention 学习描述为 focus、dilution 与再聚焦的阶段性梯度动力学，而非单调收敛”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。
- 处置：`No Change — Existing Coverage (proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01201` — To Do or Not to Do: Ensuring the Safety of Visuomotor Policies Learned from Demonstrations

- Owner：`MULTIMODAL-EMBODIED-VLA` / Ch26 / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。
- 现有命题：行动闭环必须绑定 observation、action schema、控制频率与安全回退
- 差异判断：现有命题已经规定：行动闭环必须绑定 observation、action schema、控制频率与安全回退。本来源的受限增量是“用 execution-guarantee region 将任务成功与是否允许 visuomotor policy 执行绑定”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01208` — Faithful Mobile GUI Agents with Guided Advantage Estimator

- Owner：`TRAIN-GRPO` / Ch33 / `books/part-04-training-system/33-grpo.md`。
- 现有命题：现有正文用 Dynamic Sampling 补采并过滤全对、全错的零优势 group，以 mixed-outcome membership 恢复相对排序。
- 差异判断：现有命题只覆盖“换 group membership”这条路径；未覆盖在无法或不宜补采时，通过固定 reward 边界改变 estimator 统计、保留 collapsed group 并接受有偏同号更新的替代分支。
- 处置：`Integrate Applied — root writeback complete; independent post-write review pending`。

## `SF-2026-ARXIV-2605-01220` — Visual Implicit Autoregressive Modeling

- Owner：`MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 / `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-2026-ARXIV-2605-01247` — FP-Agent: Fingerprinting AI Browsing Agents

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor
- 差异判断：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“浏览 Agent 的行为 fingerprint 比共享浏览器指纹更能支持运行时识别与控制”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01255` — Activation Compression in LLMs: Theoretical Analysis and Efficient Algorithm

- Owner：`TRAIN-DISTRIBUTED-TRAINING` / Ch36 / `books/part-04-training-system/36-distributed-training.md`。
- 现有命题：资源可用性、通信完成与全局更新语义必须共同进入一轮训练合同
- 差异判断：现有命题已经规定：资源可用性、通信完成与全局更新语义必须共同进入一轮训练合同。本来源的受限增量是“只对满足无偏条件的线性算子压缩 activation，并复用低秩因子压缩梯度”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01284` — Chain of Evidence: Pixel-Level Visual Attribution for Iterative Retrieval-Augmented Generation

- Owner：`AGENT-RAG` / Ch76 / `books/part-07-agent/76-rag.md`。
- 现有命题：检索相关性、证据充分性、freshness 与 provenance 是不同 gate
- 差异判断：现有命题已经规定：检索相关性、证据充分性、freshness 与 provenance 是不同 gate。本来源的受限增量是“把多跳 RAG 的证据 owner 从文本引用细化到页面截图的 pixel bounding boxes”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01288` — A Theory of Saddle Escape in Deep Nonlinear Networks

- Owner：`WORLDVIEW-REPRESENTATION` / Ch5 / `books/part-01-worldview/05-what-neural-networks-learn.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-NEURO-SYMBOLIC-TRACE-TO-SKILL-COMPILATION` — Lifting Traces to Logic: Programmatic Skill Induction with Neuro-Symbolic Learning for Long-Horizon Agentic Tasks

- Owner：`AGENT-PLATFORM` / Ch84 / `books/part-07-agent/84-agent-platform.md`。
- 现有命题：skill、run、tool effect 与 release/rollback 必须保持独立身份
- 差异判断：现有命题已经规定：skill、run、tool effect 与 release/rollback 必须保持独立身份。本来源的受限增量是“轨迹归纳只有被提升为带控制流、动态变量绑定和可执行符号状态的 skill program，才能把 neural proposal 与环境执行权分离。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01298` — Checkerboard: A Simple, Effective, Efficient and Learning-free Clean Label Backdoor Attack with Low Poisoning Budget

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor
- 差异判断：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“闭式、data-independent clean-label trigger 将供应链攻击从 surrogate 训练依赖中解耦”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01301` — From Stealthy Data Fabrication to Unsafe Driving: Realistic Scenario Attacks on Collaborative Perception

- Owner：`MULTIMODAL-EMBODIED-VLA` / Ch26 / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。
- 现有命题：行动闭环必须绑定 observation、action schema、控制频率与安全回退
- 差异判断：现有命题已经规定：行动闭环必须绑定 observation、action schema、控制频率与安全回退。本来源的受限增量是“对共享感知结果的微小 pose 篡改会沿 tracking 与 prediction 数据流放大为不安全控制”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01302` — Beyond Semantic Relevance: Counterfactual Risk Minimization for Robust Retrieval-Augmented Generation

- Owner：`AGENT-RAG` / Ch76 / `books/part-07-agent/76-rag.md`。
- 现有命题：本章已拆分 relevance、sufficiency、faithfulness，并校准 escalation/abstention，但没有显式处理 query 自身带错误前提时，相关性会主动放大错误这一机制。
- 差异判断：现有覆盖与 exact-v1 对读后仍缺：在 relevance 与 sufficiency 之间增加 query-robustness gate：旧 top-k 在 query 前提可信时仍合理；当前提可能错误或带确认偏误时，retriever 应把候选在 counterfactual query perturbation 下能否维持决策支持作为独立信号。Critic 只提出 evidence-risk proposal，原始 source 与 answer gate 仍拥有事实和提交权。该分支以额外扰动数据、critic 校准和更多 abstention 换取对迎合性检索的抵抗；critic 漂移、偏误模板覆盖不足或高风险结论时回退多源原文核验/人工。exact-v1 只证明作者 decision benchmarks 和扰动合同中的结果，不提供跨 corpus 固定阈值。
- 处置：`Integrate Applied — root writeback complete; independent post-write review pending`。

## `SF-2026-ARXIV-2605-01311` — The Partial Testimony of Logs: Evaluation of Language Model Generation under Confounded Model Choice

- Owner：`PLATFORM-TRACE` / Ch69 / `books/part-06-ai-infrastructure/69-trace.md`。
- 现有命题：trace 只能形成带 provenance 的因果候选，不能自动取得裁决权
- 差异判断：现有命题已经规定：trace 只能形成带 provenance 的因果候选，不能自动取得裁决权。本来源的受限增量是“只有随机实验与离线 simulator 联合才能识别混杂日志中的因果模型价值”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01327` — Segment-Aligned Policy Optimization for Multi-Modal Reasoning

- Owner：`TRAIN-GRPO` / Ch33 / `books/part-04-training-system/33-grpo.md`。
- 现有命题：本章已有 group 与 token 级 credit assignment，但缺少由语义步骤持有 credit 与截断边界的中间粒度
- 差异判断：现有正文仍缺：把 token-level policy MDP 提升为推理 segment MDP，并按自适应分段计算 value、advantage 与 importance ratio。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-2026-ARXIV-2605-01342` — Don’t Be a Pot Stirrer! Authorized Vector Data Retrieval via Access-Aware Indexing

- Owner：`AGENT-RAG` / Ch76 / `books/part-07-agent/76-rag.md`。
- 现有命题：检索相关性、证据充分性、freshness 与 provenance 是不同 gate
- 差异判断：现有命题已经规定：检索相关性、证据充分性、freshness 与 provenance 是不同 gate。本来源的受限增量是“access-aware lattice 让向量索引、存储预算与授权 query plan 共同决定检索”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01345` — The Perceptual Bandwidth Bottleneck in Vision-Language Models: Active Visual Reasoning via Sequential Experimental Design

- Owner：`MULTIMODAL-REPRESENTATION` / Ch23 / `books/part-03-multimodal-world-models/23-multimodal-representation.md`。
- 现有命题：本章已有 query-conditioned 模态/事件预算和 selector，但默认候选 observation 已经存在，没有说明模型可在推理中请求新的高分辨率局部证据。
- 差异判断：现有覆盖与 exact-v1 对读后仍缺：把固定视觉输入扩展为 bounded active-observation 分支：全局低分辨率视图先保留 context，acquisition policy 依据当前未决 claim 选择下一 crop，evidence assembler 记录坐标、尺度、采集顺序与 budget，answer gate 决定继续、提交或拒答。旧的一次性均匀采样在低分辨率已足够或 latency 严格时仍更稳；主动采集用细节可见性换额外调用、路径依赖、漏区与尾延迟。Selector 只拥有 observation proposal，不拥有 evidence sufficiency；exact-v1 结果限作者 VLM、crop proxy 和高分辨率 benchmark。
- 处置：`Integrate Applied — root writeback complete; independent post-write review pending`。

## `SF-2026-ARXIV-2605-01346` — CHASE: Competing Hypotheses for Ambiguity-Aware Selective Prediction

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“在部分可观测冲突中比较竞争解释的 margin 决定 commit 或 abstain，而非依赖单分支置信度”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01347` — MAD-OPD: Breaking the Ceiling in On-Policy Distillation via Multi-Agent Debate

- Owner：`TRAIN-SFT` / Ch29 / `books/part-04-training-system/29-sft.md`。
- 现有命题：本章已有单教师 on-policy distillation 与 KL 方向选择，但没有教师集体形成 supervision state、confidence ownership 和 agent-step sampling 的分支
- 差异判断：现有正文仍缺：让多个教师在学生 on-policy state 上辩论形成 privileged distribution，并按任务选择 JSD 或 reverse-KL、按 agent step 稳定蒸馏。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-2026-ARXIV-2605-01352` — VUDA: Breaking CUDA-Vulkan Isolation for Spatial Sharing of Compute and Graphics on the Same GPU

- Owner：`PLATFORM-GPU-SCHEDULER` / Ch63 / `books/part-06-ai-infrastructure/63-gpu-scheduler.md`。
- 现有命题：GPU placement 必须消费版本化 workload 和资源约束，而不是同质标量
- 差异判断：现有命题已经规定：GPU placement 必须消费版本化 workload 和资源约束，而不是同质标量。本来源的受限增量是“打破 CUDA/Vulkan context 隔离，使仿真 compute 与 graphics 可空间复用同一 GPU”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01373` — Focus on the Core: Empowering Diffusion Large Language Models by Self-Contrast

- Owner：`MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 / `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。
- 现有命题：本章已有 selective refresh 与可变 commit，但未说明用跨步分布不稳定性决定哪些 token 重新开放
- 差异判断：现有正文仍缺：用相邻 denoising step 的 top-K 分布差识别高动态 token，并对其自对比重掩码，集中迭代修正预算。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-2026-ARXIV-2605-01374` — MTA: Multi-Granular Trajectory Alignment for Large Language Model Distillation

- Owner：`TRAIN-SFT` / Ch29 / `books/part-04-training-system/29-sft.md`。
- 现有命题：本章已区分 output、feature 与 trajectory distillation，并要求层映射和表示损失受限；MTA 是受限实例
- 差异判断：exact-v1 的新增证据是“沿教师与学生的层级 transformation trajectory 对齐 token、span 和 hidden representation，而非只对齐末端 logits”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。
- 处置：`No Change — Existing Coverage (proposition comparison; independent review required)`。

## `SF-MEMORAI-PROVENANCE-AWARE-GRAPH-MEMORY` — MemORAI: Memory Organization and Retrieval via Adaptive Graph Intelligence for LLM Conversational Agents

- Owner：`AGENT-MEMORY` / Ch77 / `books/part-07-agent/77-memory.md`。
- 现有命题：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner
- 差异判断：现有命题已经规定：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner。本来源的受限增量是“长期记忆的过滤、turn-level provenance graph 与 query-adaptive retrieval 是同一 lifecycle 的不同状态；高连接度不能替代 query-specific evidence relevance。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-LIVEFMBENCH-FAITHFULNESS-GATE` — LiveFMBench: Unveiling the Power and Limits of Agentic Workflows in Specification Generation

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“形式规约评测必须同时验证 code/spec faithfulness、时间污染与 verifier 非空洞性；自动 prover 通过不能单独构成成功。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01415` — AI Safety as Control of Irreversibility: A Systems Framework for Decision-Energy and Sovereignty Boundaries

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor
- 差异判断：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“把不可逆决策、物理资源动员与自我扩张权限分离为外部可审查的 sovereignty boundaries”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01425` — Barriers to Counterfactual Credit Attribution for Autoregressive Models

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“自回归输出的生成后 credit attribution 受不可辨识与组合搜索约束”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01429` — SCALE-LoRA: Auditing Post-Retrieval LoRA Composition with Residual Merging and View Reliability

- Owner：`TRAIN-LORA` / Ch30 / `books/part-04-training-system/30-lora.md`。
- 现有命题：本章已有 adapter merge 与冲突风险，但缺少 post-retrieval composition 的可靠性状态和 disagreement gate
- 差异判断：现有正文仍缺：在开放 LoRA 池检索后，以层级稀疏残差合并和多视图一致性审计决定组合、拒绝或回退。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-2026-ARXIV-2605-01449` — VisInject: Disruption != Injection -- A Dual-Dimension Evaluation of Universal Adversarial Attacks on Vision-Language Models

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-2026-ARXIV-2605-01477` — Action Agent: Agentic Video Generation Meets Flow-Constrained Diffusion

- Owner：`MULTIMODAL-EMBODIED-VLA` / Ch26 / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。
- 现有命题：高层 reasoning/imagination 只形成 action proposal；低层 controller、fresh observation 与 safety envelope 拥有执行、纠错和环境 transition 的提交边界。
- 差异判断：该 two-stage navigation system 是现有高低层分工的具体案例；真实证据仍是 open-loop，且其尺度、漂移、碰撞失败恰好落在正文既有 freshness、calibration 与 closed-loop 边界内，没有改变长期命题。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01506` — OmniEncoder: See, Hear, and Feel Continuous Motion Like Humans With One Encoder

- Owner：`MULTIMODAL-REPRESENTATION` / Ch23 / `books/part-03-multimodal-world-models/23-multimodal-representation.md`。
- 现有命题：本章已要求 modality identity、时间戳和窗口边界随 token 保留；该 encoder 没有改变统一空间与模态专属前端共存关系
- 差异判断：exact-v1 的新增证据是“以统一 token template、Omni-RoPE 和时窗移动联合编码视频、音频与运动连续性”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。
- 处置：`No Change — Existing Coverage (proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01566` — Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling

- Owner：`AGENT-MULTI-AGENT` / Ch82 / `books/part-07-agent/82-multi-agent.md`。
- 现有命题：消息、角色和局部成功不能替代共享状态的唯一提交语义
- 差异判断：现有命题已经规定：消息、角色和局部成功不能替代共享状态的唯一提交语义。本来源的受限增量是“多 Agent test-time scaling 的收益必须落在 token-cost/accuracy Pareto 前沿而非只看准确率”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-RL-DEVELOPER-MEMORY-OPE-GATE` — Feedback-Normalized Developer Memory for Reinforcement-Learning Coding Agents: A Safety-Gated MCP Architecture

- Owner：`AGENT-MEMORY` / Ch77 / `books/part-07-agent/77-memory.md`。
- 现有命题：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner
- 差异判断：现有命题已经规定：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner。本来源的受限增量是“Developer memory selection 是带 propensity 与延迟反馈的控制决策；确定性策略持有生产权，学习策略只能在 shadow/OPE gate 后进入 canary。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-PRODUCTION-AGENT-CONTINUOUS-EVALUATION` — Evaluating Agentic AI in the Wild: Failure Modes, Drift Patterns, and a Production Evaluation Framework

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“生产 Agent 的 compounding error、tool cascade 与 temporal drift 要用连续、分布感知、跨信号的评测状态，而非一次 episodic score。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01609` — Concepts Whisper While Syntax Shouts: Spectral Anti-Concentration and the Dual Geometry of Transformer Representations

- Owner：`WORLDVIEW-REPRESENTATION` / Ch5 / `books/part-01-worldview/05-what-neural-networks-learn.md`。
- 现有命题：本章已区分相关方向、线性 probe 与因果干预；谱反集中是新的测量案例而非新表示 owner
- 差异判断：exact-v1 的新增证据是“以谱能量与 whitened causal alignment 区分稀疏概念方向和高能 syntax 结构，反证只看方差的解释”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。
- 处置：`No Change — Existing Coverage (proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01640` — Prescriptive Scaling Laws for Data Constrained Training

- Owner：`TRAIN-PRETRAINING` / Ch28 / `books/part-04-training-system/28-pretraining.md`。
- 现有命题：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算
- 差异判断：现有命题已经规定：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算。本来源的受限增量是“data cap 下的 scaling law 把新增算力重新分配到数据质量、重复与模型规模”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01642` — Adaptive Pluralistic Alignment: A pipeline for dynamic artificial democracy

- Owner：`TRAIN-RLHF` / Ch31 / `books/part-04-training-system/31-rlhf.md`。
- 现有命题：本章已有多目标 reward 与偏好聚合，但缺少 reward basis、jury membership 和时间变化权重的显式状态所有权
- 差异判断：现有正文仍缺：把人群偏好分解为低秩 reward basis，经民主过滤形成 jury，再随时间更新群体权重与策略。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-2026-ARXIV-2605-01643` — AI Alignment via Incentives and Correction

- Owner：`TRAIN-RLHF` / Ch31 / `books/part-04-training-system/31-rlhf.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-2026-ARXIV-2605-01644` — Toward a Principled Framework for Agent Safety Measurement

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“Agent safety measurement 必须覆盖策略搜索空间而不是只测固定输出样本”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01653` — SteeringDiffusion: A Bottlenecked Activation Control Interface for Diffusion Models

- Owner：`MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 / `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。
- 现有命题：本章已覆盖 conditioning、adapter 与迭代生成控制，并保留能力干扰和强度校准；该接口是受限实现
- 差异判断：exact-v1 的新增证据是“以瓶颈 activation adapter 在 diffusion 运行时注入方向控制，形成不改主权重的控制接口”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。
- 处置：`No Change — Existing Coverage (proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01657` — Act2See: Emergent Active Visual Perception for Video Reasoning

- Owner：`MULTIMODAL-REPRESENTATION` / Ch23 / `books/part-03-multimodal-world-models/23-multimodal-representation.md`。
- 现有命题：多模态表示必须保留时间、模态与来源身份，不能只比较 token 数量
- 差异判断：现有命题已经规定：多模态表示必须保留时间、模态与来源身份，不能只比较 token 数量。本来源的受限增量是“VLM 在推理中主动决定检索或生成视觉证据，使 context acquisition 成为显式动作”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01662` — Video Active Perception: Effective Inference-Time Long-Form Video Understanding with Vision-Language Models

- Owner：`MULTIMODAL-REPRESENTATION` / Ch23 / `books/part-03-multimodal-world-models/23-multimodal-representation.md`。
- 现有命题：多模态表示必须保留时间、模态与来源身份，不能只比较 token 数量
- 差异判断：现有命题已经规定：多模态表示必须保留时间、模态与来源身份，不能只比较 token 数量。本来源的受限增量是“长视频推理将 keyframe selection 建模为基于生成先验的 inference-time data acquisition”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01675` — CP-SynC: Multi-Agent Zero-Shot Constraint Modeling in MiniZinc with Synthesized Checkers

- Owner：`AGENT-MULTI-AGENT` / Ch82 / `books/part-07-agent/82-multi-agent.md`。
- 现有命题：消息、角色和局部成功不能替代共享状态的唯一提交语义
- 差异判断：现有命题已经规定：消息、角色和局部成功不能替代共享状态的唯一提交语义。本来源的受限增量是“并行生成候选约束程序并综合可执行 checker 证据，将 verifier 变为最终选择 authority”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-GRAVITY-GENERATION-TIME-STRUCTURED-ANCHORS` — GRAVITY: Architecture-Agnostic Structured Anchoring for Long-Horizon Conversational Memory

- Owner：`AGENT-MEMORY` / Ch77 / `books/part-07-agent/77-memory.md`。
- 现有命题：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner
- 差异判断：现有命题已经规定：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner。本来源的受限增量是“retrieved evidence 与 generation-time relational/temporal/thematic anchors 是两层状态；结构化派生视图不能替代原始 memory provenance。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01694` — Latent State Design for World Models under Sufficiency Constraints

- Owner：`MULTIMODAL-WORLD-MODELS` / Ch25 / `books/part-03-multimodal-world-models/25-multimodal-world-models.md`。
- 现有命题：生成外观、环境 transition 与可修订 world state 是不同责任
- 差异判断：现有命题已经规定：生成外观、环境 transition 与可修订 world state 是不同责任。本来源的受限增量是“world-model latent state 以任务充分性而非重建完整 observation 作为设计约束”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01699` — Probe-Geometry Alignment: Erasing the Cross-Sequence Memorization Signature Below Chance

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor
- 差异判断：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“跨序列 probe 揭示 unlearning 后可恢复的表示痕迹，并用逐层 rank-one intervention 擦除”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01704` — The Reasoning Trap: An Information-Theoretic Bound on Closed-System Multi-Step LLM Reasoning

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“closed-system 多步推理存在信息边界，外部 evidence 改变可恢复性而非单纯增加思考 token”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01708` — SplitZip: Ultra Fast Lossless KV Compression for Disaggregated LLM Serving

- Owner：`INFER-PD-DISAGGREGATION` / Ch55 / `books/part-05-inference-system/55-pd-disaggregation.md`。
- 现有命题：阶段分离只有在状态迁移、失败域和 SLO 同时闭合时才成立
- 差异判断：现有命题已经规定：阶段分离只有在状态迁移、失败域和 SLO 同时闭合时才成立。本来源的受限增量是“bit-exact KV transfer compression 在 PD 拆分中压缩传输而不改变 decode 状态”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (marker verified)`。

## `SF-2026-ARXIV-2605-01710` — Model Routing as a Trust Problem: Route Receipts for Adaptive AI Systems

- Owner：`PLATFORM-TRACE` / Ch69 / `books/part-06-ai-infrastructure/69-trace.md`。
- 现有命题：本章已有请求 trace，但缺少路由决策本身的候选集、策略版本和约束快照，模型名不能重建实际决策
- 差异判断：现有正文仍缺：为动态模型路由生成 route receipt，记录候选、策略版本、约束、选择结果与可披露 provenance。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-2026-ARXIV-2605-01725` — Motion-Aware Caching for Efficient Autoregressive Video Generation

- Owner：`MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 / `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-2026-ARXIV-2605-01732` — EGAD: Entropy-Guided Adaptive Distillation for Token-Level Knowledge Transfer

- Owner：`TRAIN-SFT` / Ch29 / `books/part-04-training-system/29-sft.md`。
- 现有命题：本章已有按 teacher disagreement/entropy 选择 token 与温度的机制；EGAD 未改变 teacher/student ownership
- 差异判断：exact-v1 的新增证据是“按教师 entropy 调整 curriculum、temperature 与蒸馏路径，使 token-level transfer 随不确定性变化”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。
- 处置：`No Change — Existing Coverage (proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01733` — GEASS: Gated Evidence-Adaptive Selective Caption Trust for Vision-Language Models

- Owner：`MULTIMODAL-REPRESENTATION` / Ch23 / `books/part-03-multimodal-world-models/23-multimodal-representation.md`。
- 现有命题：本章已有多模态证据 provenance，但缺少 caption 作为不对称可疑证据的双路径 admission/拒绝控制
- 差异判断：现有正文仍缺：并行执行图像直答与 caption 辅助路径，以 confidence gate、information gain 和证据权重融合，限制错误 caption 锚定。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-2026-ARXIV-2605-01740` — Architectural Obsolescence of Unhardened Agentic-AI Runtimes

- Owner：`AGENT-PLATFORM` / Ch84 / `books/part-07-agent/84-agent-platform.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-2026-ARXIV-2605-01749` — Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：本章已有 claim-level evidence gate，但缺少 exploration state 与 externally committed answer 的训练时分权
- 差异判断：现有正文仍缺：把长答案生成拆成 calibrated exploration 与 selective commitment，只将达到可靠性门槛的推理投影为最终 claim。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-2026-ARXIV-2605-01750` — Talk is Cheap, Communication is Hard: Dynamic Grounding Failures and Repair in Multi-Agent Negotiation

- Owner：`AGENT-MULTI-AGENT` / Ch82 / `books/part-07-agent/82-multi-agent.md`。
- 现有命题：消息、角色和局部成功不能替代共享状态的唯一提交语义
- 差异判断：现有命题已经规定：消息、角色和局部成功不能替代共享状态的唯一提交语义。本来源的受限增量是“多 Agent 协商失败来自共享 grounding 动态漂移，并需要显式 repair 而非增加消息”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-FORESIGHT-LOCALIZED-MULTIAGENT-RECOVERY` — Catching the Infection Before It Spreads: Foresight-Guided Defense in Multi-Agent Systems

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor
- 差异判断：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“多 Agent 感染防御应跟踪局部传播状态并按新近/长期感染选择 rollback 或递归定位，而不是用全局 cure factor 覆盖检索分布。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01761` — TrajShield: Trajectory-Level Safety Mediation for Defending Text-to-Video Models Against Jailbreak Attacks

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor
- 差异判断：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“把文本到视频安全从 prompt 词面过滤提升为生成轨迹上的因果风险定位与最小改写”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01766` — Mitigating Multimodal LLMs Hallucinations via Relevance Propagation at Inference Time

- Owner：`INFER-KV-CACHE` / Ch45 / `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`。
- 现有命题：直接修改 KV 的 inference-time 分支属于 Experimental mutable state，必须使用 versioned Copy-on-Write branch、隔离污染并由独立 outcome verifier 决定是否提交。
- 差异判断：LIME 提供 multimodal relevance objective、KL 约束和逐 token 开销案例，但没有改变既有 KV mutation 的身份、隔离、验证和 rollback 合同；LRP relevance 也不能提升为 commit authority。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01771` — The Compliance Gap: Why AI Systems Promise to Follow Process Instructions but Don't

- Owner：`PLATFORM-TRACE` / Ch69 / `books/part-06-ai-infrastructure/69-trace.md`。
- 现有命题：本章已有 trace/span，但缺少将 process instruction 映射为可观察事件并判定 false compliance 的验收合同
- 差异判断：现有正文仍缺：区分结果合规与过程合规，要求工具调用、检索与中间动作日志证明系统实际遵循了指定过程。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-2026-ARXIV-2605-01772` — Anticipation-VLA: Solving Long-Horizon Embodied Tasks via Anticipation-based Subgoal Generation

- Owner：`MULTIMODAL-EMBODIED-VLA` / Ch26 / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。
- 现有命题：现有小节允许整条 trace 失效后重规划，但缺少局部 subgoal 的递归细化、完成弹出与失败回退状态机。
- 差异判断：现有覆盖与 exact-v1 对读后仍缺：在 immutable full-horizon trace 与逐步 reactive policy 之间增加 adaptive subgoal stack：每个 subgoal 绑定 observation revision、parent、完成条件和 validity horizon；高层 planner 只能 push/refine/backtrack proposal，低层 policy 用 fresh observation 执行，controller 验证完成后才 pop。它以局部修订降低整条计划报废成本，却新增 progress detector 误判、递归不终止、stack stale 和高低层语义漂移；动态环境或检测不可信时回退短 horizon reactive planning/全量重规划。exact-v1 只支持作者模拟与有限真实任务，不构成开放世界 safety proof。
- 处置：`Integrate Applied — root writeback complete; independent post-write review pending`。

## `SF-2026-ARXIV-2605-01782` — Needle-in-RAG: Prompt-Conditioned Character-Level Traceback of Poisoned Spans in Retrieved Evidence

- Owner：`AGENT-RAG` / Ch76 / `books/part-07-agent/76-rag.md`。
- 现有命题：本章已有文档级 provenance 与 poisoning 防御，但缺少黑盒链路中从错误输出反查字符 span 的两阶段取证状态
- 差异判断：现有正文仍缺：先记录 misgeneration 与检索事件，再以 counterfactual deletion 回溯到字符级 poisoned span，并把 span provenance 返回修复环。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-2026-ARXIV-2605-01789` — DataEvolver: Let Your Data Build and Improve Itself via Goal-Driven Loop Agents

- Owner：`TRAIN-DATA` / Ch27 / `books/part-04-training-system/27-data.md`。
- 现有命题：本章已把合成数据生产定义为带目标、校验、版本与失败回退的闭环；DataEvolver 没有改变数据 owner
- 差异判断：exact-v1 的新增证据是“用 goal、artifact、critic、correction 和 acceptance 的双环构建可控视觉训练数据”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。
- 处置：`No Change — Existing Coverage (proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01790` — Khala: Scaling Acoustic Token Language Models Toward High-Fidelity Music Generation

- Owner：`MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 / `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-2026-ARXIV-2605-01799` — Embody4D: A Generalist Data Engine for Embodied 4D World Modeling

- Owner：`MULTIMODAL-WORLD-MODELS` / Ch25 / `books/part-03-multimodal-world-models/25-multimodal-world-models.md`。
- 现有命题：多视角生成、几何状态和可执行 transition 是不同责任；派生视图必须保留 source/camera/projection identity 与回退。
- 差异判断：现有小节已把 projective 4D state 与视觉生成分责，并要求几何/相机/provenance；Embody4D 提供 copy/repair/inpaint 的具体数据引擎，但没有改变 world-state owner 或实时控制边界。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01823` — Selector-Guided Autonomous Curriculum for One-Shot Reinforcement Learning from Verifiable Rewards

- Owner：`TRAIN-GRPO` / Ch33 / `books/part-04-training-system/33-grpo.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-2026-ARXIV-2605-01837` — nvPAX: Constrained Optimization for Dynamic Power Allocation in Hierarchical and Multi-Tenant Systems

- Owner：`PLATFORM-GPU-SCHEDULER` / Ch63 / `books/part-06-ai-infrastructure/63-gpu-scheduler.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-2026-ARXIV-2605-01844` — The Cylindrical Representation Hypothesis for Language Model Steering

- Owner：`WORLDVIEW-REPRESENTATION` / Ch5 / `books/part-01-worldview/05-what-neural-networks-learn.md`。
- 现有命题：本章已否定单一全局线性方向的充分性，并要求 sample-conditioned geometry 与副作用测量；该假说属于受限解释
- 差异判断：exact-v1 的新增证据是“以圆柱几何解释同一 steering 方向在不同样本相位下产生不稳定效果，并给出敏感扇区”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。
- 处置：`No Change — Existing Coverage (proposition comparison; independent review required)`。

## `SF-NEUROSTATE-COMMITMENT-INTEGRITY` — NeuroState-Bench: A Human-Calibrated Benchmark for Commitment Integrity in LLM Agent Profiles

- Owner：`AGENT-MEMORY` / Ch77 / `books/part-07-agent/77-memory.md`。
- 现有命题：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner
- 差异判断：现有命题已经规定：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner。本来源的受限增量是“Agent profile 的 task outcome 与 commitment integrity 必须分轴验收；最终答对不能证明承诺、偏好或状态约束被持续遵守。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01858` — Decouple and Cache: KV Cache Construction for Streaming Video Understanding

- Owner：`MULTIMODAL-REPRESENTATION` / Ch23 / `books/part-03-multimodal-world-models/23-multimodal-representation.md`。
- 现有命题：多模态表示必须保留时间、模态与来源身份，不能只比较 token 数量
- 差异判断：现有命题已经规定：多模态表示必须保留时间、模态与来源身份，不能只比较 token 数量。本来源的受限增量是“流式视频把 KV 构建与帧到达解耦，避免每次更新重算全部视觉历史”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01896` — Divide and Conquer: Decoupled Representation Alignment for Multimodal World Models

- Owner：`MULTIMODAL-REPRESENTATION` / Ch23 / `books/part-03-multimodal-world-models/23-multimodal-representation.md`。
- 现有命题：语义、时空与行动对齐承担不同目标，多目标 loss 需要保留各自信息责任，不能由单一距离替代。
- 差异判断：现有小节已明确不同 alignment target 与 reconstruction/semantic/action loss 的冲突；M2-REPA 是 RGB/depth/mask expert 的具体实现，没有改变该多目标分责原则。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01899` — Disentangling Intent from Role: Adversarial Self-Play for Persona-Invariant Safety Alignment

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：本章已要求跨 persona、上下文和多轮变体做安全一致性测试；该训练方案未改变安全 gate
- 差异判断：exact-v1 的新增证据是“用 persona lineage 的对抗自博弈产生攻击，再以 persona-invariant consistency 降低角色表面变化对安全判断的影响”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。
- 处置：`No Change — Existing Coverage (proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01910` — Stochastic Sparse Attention for Memory-Bound Inference

- Owner：`INFER-KV-CACHE` / Ch45 / `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`。
- 现有命题：稀疏 attention 读取的是带 model/position/selection identity 的派生状态，近似选择必须保存误差与 full-context fallback。
- 差异判断：Stochastic Sparse Attention 用随机选择换 memory-bound 访问缩减；现有小节已经覆盖稀疏派生状态、选择误差、身份和 FullKV 回退，故不改变长期命题。 仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01913` — RefusalGuard: Geometry-Preserving Fine-Tuning for Safety in LLMs

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：现有正文要求以 sample-level dynamics 发现 fine-tuning 安全退化，并将 risk score 保持为传感器；阈值失效时仍执行完整 safety regression。
- 差异判断：现有命题覆盖样本风险与事后 weight repair，却未说明 downstream update 即使保持 task utility，也可能沿 safety-mediating subspace 漂移，以及如何在训练时限制该投影。
- 处置：`Integrate Applied — root writeback complete; independent post-write review pending`。

## `SF-2026-ARXIV-2605-01920` — A Language for Describing Agentic LLM Contexts

- Owner：`AGENT-CONTEXT` / Ch75 / `books/part-07-agent/75-context.md`。
- 现有命题：原始事实状态、派生视图与 context mutation 的提交权必须分离
- 差异判断：现有命题已经规定：原始事实状态、派生视图与 context mutation 的提交权必须分离。本来源的受限增量是“用可描述的 context schema 标注 Agent 所见信息、来源和作用域”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01928` — Training Non-Differentiable Networks via Optimal Transport

- Owner：`TRAIN-PRETRAINING` / Ch28 / `books/part-04-training-system/28-pretraining.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-2026-ARXIV-2605-01929` — Exploring Data-Free LoRA Transferability for Video Diffusion Models

- Owner：`TRAIN-LORA` / Ch30 / `books/part-04-training-system/30-lora.md`。
- 现有命题：本章已有权重空间合并，但缺少跨 backbone/蒸馏变体迁移时的谱兼容性 gate 与无数据回退边界
- 差异判断：现有正文仍缺：在无目标数据时按谱刚性聚类 LoRA，并仲裁 video-diffusion 变体间的 routing interference。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-2026-ARXIV-2605-01930` — GPU Fingerprinting for Location Verification

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-2026-ARXIV-2605-01936` — Pandora's Regret: A Proper Scoring Rule for Evaluating Sequential Search

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-2026-ARXIV-2605-01938` — Cross-Layer Energy Analysis of Multimodal Training on Grace Hopper Superchips

- Owner：`MULTIMODAL-REPRESENTATION` / Ch23 / `books/part-03-multimodal-world-models/23-multimodal-representation.md`。
- 现有命题：多模态表示必须保留时间、模态与来源身份，不能只比较 token 数量
- 差异判断：现有命题已经规定：多模态表示必须保留时间、模态与来源身份，不能只比较 token 数量。本来源的受限增量是“跨层测量把 GH200 多模态训练的能耗归因到数据移动而非只归因 FLOPs”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01948` — Phone2Act: A Low-Cost, Hardware-Agnostic Teleoperation System for Scalable VLA Data Collection

- Owner：`TRAIN-DATA` / Ch27 / `books/part-04-training-system/27-data.md`。
- 现有命题：teleoperation 派生轨迹必须绑定输入设备、时间同步、robot schema、retarget/bridge 与真实闭环验证。
- 差异判断：现有小节已规定 teleoperation 到派生 robot trajectory 的 schema、provenance、per-embodiment adaptation 与真实控制验收；Phone2Act 补充手机/ROS2/LeRobot 案例，没有改变数据 owner 或跨 embodiment 边界。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01950` — TRAP: Tail-aware Ranking Attack for World-Model Planning

- Owner：`MULTIMODAL-WORLD-MODELS` / Ch25 / `books/part-03-multimodal-world-models/25-multimodal-world-models.md`。
- 现有命题：生成外观、环境 transition 与可修订 world state 是不同责任
- 差异判断：现有命题已经规定：生成外观、环境 transition 与可修订 world state 是不同责任。本来源的受限增量是“tail-aware ranking attack 表明 world-model planner 的候选轨迹排序本身是攻击面”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01959` — Flexi-LoRA with Input-Adaptive Ranks: Efficient Finetuning for Speech and Reasoning Tasks

- Owner：`TRAIN-LORA` / Ch30 / `books/part-04-training-system/30-lora.md`。
- 现有命题：现有正文把 rank、target modules、base revision 与预算冻结为 adapter update-space identity，并用 rank sweep 选择静态容量。
- 差异判断：现有命题没有覆盖 sample-conditioned rank router，也未把训练—推理 rank policy、difficulty-label provenance 和动态 shape serving 成本纳入 adapter identity。
- 处置：`Integrate Applied — root writeback complete; independent post-write review pending`。

## `SF-2026-ARXIV-2605-01970` — Trojan Hippo: Weaponizing Agent Memory for Data Exfiltration

- Owner：`AGENT-MEMORY` / Ch77 / `books/part-07-agent/77-memory.md`。
- 现有命题：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner
- 差异判断：现有命题已经规定：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner。本来源的受限增量是“恶意内容可写入持久 Agent memory，并在后续会话恢复时触发数据外泄”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-01989` — DBLP: Phase-Aware Bounded-Loss Transport for Burst-Resilient Distributed ML Training

- Owner：`TRAIN-DISTRIBUTED-TRAINING` / Ch36 / `books/part-04-training-system/36-distributed-training.md`。
- 现有命题：资源可用性、通信完成与全局更新语义必须共同进入一轮训练合同
- 差异判断：现有命题已经规定：资源可用性、通信完成与全局更新语义必须共同进入一轮训练合同。本来源的受限增量是“按训练 phase 与 loss budget 选择有损/可靠传输 fallback，而非统一可靠协议”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (marker verified)`。

## `SF-2026-ARXIV-2605-02028` — Counting as a minimal probe of language model reliability

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“extended rule following 暴露模型对有限内部规则状态的持续更新失败”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02037` — VILAS: A VLA-Integrated Low-cost Architecture with Soft Grasping for Robotic Manipulation

- Owner：`MULTIMODAL-EMBODIED-VLA` / Ch26 / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。
- 现有命题：行动闭环必须绑定 observation、action schema、控制频率与安全回退
- 差异判断：现有命题已经规定：行动闭环必须绑定 observation、action schema、控制频率与安全回退。本来源的受限增量是“以模块化硬件、统一采集/部署数据流和一致 demonstrations 暴露 VLA 的真实部署边界”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02038` — What Single-Prompt Accuracy Misses: A Multi-Variant Reliability Audit of Language Models

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“同一任务的 prompt variants 揭示单提示 accuracy 无法度量服务可靠性”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (marker verified)`。

## `SF-2026-ARXIV-2605-02043` — Bringing Order to Asynchronous SGD: Towards Optimality under Data-Dependent Delays with Momentum

- Owner：`TRAIN-DISTRIBUTED-TRAINING` / Ch36 / `books/part-04-training-system/36-distributed-training.md`。
- 现有命题：资源可用性、通信完成与全局更新语义必须共同进入一轮训练合同
- 差异判断：现有命题已经规定：资源可用性、通信完成与全局更新语义必须共同进入一轮训练合同。本来源的受限增量是“异步 SGD 的 data-dependent delay 与 momentum 必须联合校正才能保持更新语义”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-AI-EVALUATION-RCT-CONTRACT` — Principles and Guidelines for Randomized Controlled Trials in AI Evaluation

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“AI uplift/RCT 结论必须显式冻结 intervention、population、control、outcome、power、randomization 与可复算材料；行业惯例不能替代实验身份。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02083` — EditPropBench: Measuring Factual Edit Propagation in Scientific Manuscripts

- Owner：`AGENT-WORKFLOW` / Ch81 / `books/part-07-agent/81-workflow.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-2026-ARXIV-2605-02087` — Model Spec Midtraining: Improving How Alignment Training Generalizes

- Owner：`TRAIN-PRETRAINING` / Ch28 / `books/part-04-training-system/28-pretraining.md`。
- 现有命题：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算
- 差异判断：现有命题已经规定：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算。本来源的受限增量是“把行为 spec 注入 midtraining，改变 alignment generalization 的训练阶段 owner”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (marker verified)`。

## `SF-2026-ARXIV-2605-02105` — Sharpness-Aware Pretraining Mitigates Catastrophic Forgetting

- Owner：`TRAIN-PRETRAINING` / Ch28 / `books/part-04-training-system/28-pretraining.md`。
- 现有命题：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算
- 差异判断：现有命题已经规定：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算。本来源的受限增量是“sharpness-aware pretraining 改变后续适配时 catastrophic forgetting 的初始几何条件”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02106` — The Dynamic Gist-Based Memory Model (DGMM): A Memory-Centric Architecture for Artificial Intelligence

- Owner：`AGENT-MEMORY` / Ch77 / `books/part-07-agent/77-memory.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent final review pending`。

## `SF-STABLEVAL-DISAGREEMENT-AWARE-RANKING` — STABLEVAL: Disagreement-Aware and Stable Evaluation of AI Systems

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“Human-evaluation aggregation must preserve annotator uncertainty and ranking stability; majority vote is not a sufficient release-grade evaluation contract.”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02124` — Boundary Mass and the Soft-to-Hard Limit in Mixture-of-Experts

- Owner：`TRAIN-PRETRAINING` / Ch28 / `books/part-04-training-system/28-pretraining.md`。
- 现有命题：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算
- 差异判断：现有命题已经规定：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算。本来源的受限增量是“soft routing 训练到 hard dispatch 的边界质量由 routing mass 演化而非只由 top-k 决定”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-FEDQUEUE-CROSS-FACILITY-QUEUE-AWARE-TRAINING` — FedQueue: Queue-Aware Federated Learning for Cross-Facility HPC Training

- Owner：`TRAIN-DISTRIBUTED-TRAINING` / Ch36 / `books/part-04-training-system/36-distributed-training.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent review pending`。

## `SF-2026-ARXIV-2605-02134` — Video Generation with Predictive Latents

- Owner：`MULTIMODAL-WORLD-MODELS` / Ch25 / `books/part-03-multimodal-world-models/25-multimodal-world-models.md`。
- 现有命题：生成外观、环境 transition 与可修订 world state 是不同责任
- 差异判断：现有命题已经规定：生成外观、环境 transition 与可修订 world state 是不同责任。本来源的受限增量是“predictive latents 让视频生成表示承担未来状态预测而非只重建当前像素”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02144` — Projection-Free Transformers via Gaussian Kernel Attention

- Owner：`MODEL-SELF-ATTENTION` / Ch14 / `books/part-02-model/14-self-attention.md`。
- 现有命题：本章把 Q/K 视为可学习寻址坐标，但尚未呈现 projection-free kernel diffusion 作为不同归纳偏置的替代分支
- 差异判断：现有正文仍缺：用原始 hidden-state 间 Gaussian kernel 直接构造 row-stochastic attention，移除 Q/K 投影并以 bandwidth 控制局部性。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-2026-ARXIV-2605-02152` — SpecEdit: Training-Free Acceleration for Diffusion based Image Editing via Semantic Locking

- Owner：`MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 / `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。
- 现有命题：本章已有 token commit/rollback，但缺少跨分辨率 draft、semantic lock 与 selective high-resolution compute 的组合
- 差异判断：现有正文仍缺：先低分辨率生成 draft，以语义验证锁定稳定区域，仅对未锁定区域恢复高分辨率并继续计算。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-2026-ARXIV-2605-02162` — AAFLOW: Scalable Patterns for Agentic AI Workflows

- Owner：`AGENT-WORKFLOW` / Ch81 / `books/part-07-agent/81-workflow.md`。
- 现有命题：已知顺序与 invariant 应由 durable workflow 拥有，模型只处理开放决策
- 差异判断：现有命题已经规定：已知顺序与 invariant 应由 durable workflow 拥有，模型只处理开放决策。本来源的受限增量是“零拷贝数据流与可组合执行模式把 Agent workflow 从脚本升级为显式 runtime”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-UNBALANCED-MULTIAGENT-COMPUTE-OWNERSHIP` — Planner Matters! An Efficient and Unbalanced Multi-agent Collaboration Framework for Long-horizon Planning

- Owner：`AGENT-MULTI-AGENT` / Ch82 / `books/part-07-agent/82-multi-agent.md`。
- 现有命题：消息、角色和局部成功不能替代共享状态的唯一提交语义
- 差异判断：现有命题已经规定：消息、角色和局部成功不能替代共享状态的唯一提交语义。本来源的受限增量是“Planner, actor and memory roles may own different compute budgets; the reported allocation is evidence for the tested planning workloads, not a universal multi-agent topology.”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02178` — T$^2$PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning

- Owner：`TRAIN-GRPO` / Ch33 / `books/part-04-training-system/33-grpo.md`。
- 现有命题：本章已有 prefix 相似度驱动的取消 proposal，但没有把 token-level 思考干预与 turn-level 重采样分成两种不同控制动作。
- 差异判断：现有覆盖与 exact-v1 对读后仍缺：把低边际信息检测扩展成两层 exploration controller：token 层只能提出 bounded thinking intervention，turn 层只能提出 resample/cancel；group builder 保存触发分数、阈值、policy/environment revision 与最终 membership，optimizer 不把缺失 suffix 或重采样重复当独立证据。它用减少空转换取 estimator drift、selection bias、额外 token 和 on-policy staleness；uncertainty 不等于错误，late-reward 或校准不足时回退完整 rollout/静态采样。exact-v1 只支持 WebShop、ALFWorld、Search QA 与作者配置。
- 处置：`Integrate Applied — root writeback complete; independent post-write review pending`。

## `SF-EDGE-CONTINUOUS-INFERENCE-RISK-BUDGET` — Risk-Budgeted Online Scheduling for Continuous Edge Inference over Evolving Time Horizons

- Owner：`INFER-SCHEDULING` / Ch56 / `books/part-05-inference-system/56-inference-scheduling.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent review pending`。

## `SF-RESPONSE-PATH-TAMPERING-PROVIDER-SIGNATURE` — When Alignment Isn’t Enough: Response-Path Attacks on LLM Agents

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent review pending`。

## `SF-2026-ARXIV-2605-02189` — PipeMax: Enhancing Offline LLM Inference on Commodity GPU Servers

- Owner：`INFER-SCHEDULING` / Ch56 / `books/part-05-inference-system/56-inference-scheduling.md`。
- 现有命题：调度状态必须携带 deadline risk、剩余 slack 与降级边界
- 差异判断：现有命题已经规定：调度状态必须携带 deadline risk、剩余 slack 与降级边界。本来源的受限增量是“commodity GPU 离线推理通过阶段 pipeline 重排内存与计算，而非照搬在线 serving”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-CODE-EVAL-PIPELINE-FALSE-FAILURES` — Beyond Translation Accuracy: Addressing False Failures in LLM-Based Code Translation

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“Compiler flags, libraries, runtime configuration and test harness are part of code-agent evaluation identity because pipeline faults can create false model failures.”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02196` — DurableUn: Quantization-Induced Recovery Attacks in Machine Unlearning

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：`Deployed Precision 是 Forgetting Evidence 的组成部分` 已要求把 base checkpoint、unlearning delta/adapter、merge、quantizer、bit width、calibration、kernel 与最终 serving artifact 绑定为证据身份，并与 retained utility 分轴验收。
- 差异判断：exact-v1 的 NF4+LoRA INT4 recovery、FA–RA–Q-INT4 trilemma、STE mitigation 和低 retained accuracy 是现有机制的受限实验；没有改变 owner、未知量化器边界或失败时停止发布/重训的回退。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-MEMAUDIT-EXACT-PACKAGE-ORACLE` — MEMAUDIT: An Exact Package-Oracle Evaluation Protocol for Budgeted Long-Term LLM Memory Writing

- Owner：`AGENT-MEMORY` / Ch77 / `books/part-07-agent/77-memory.md`。
- 现有命题：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner
- 差异判断：现有命题已经规定：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner。本来源的受限增量是“Long-term memory writing needs an exact budgeted package oracle that measures write admission separately from answer generation.”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02206` — Metric Unreliability in Multimodal Machine Unlearning: A Systematic Analysis and Principled Unified Score

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：Evaluation owner 已要求按目标拆分互不替代的证据轴，冻结 scorer/oracle/subject identity，并禁止聚合总分掩盖 failure type；unlearning 还必须区分 suppression、reference distance、recoverability 与 retain utility。
- 差异判断：exact-v1 的五指标排序冲突、retain-only oracle、KR blind spot 与 correlation-weighted UQS 是现有 evaluation contract 的受限案例；UQS 的 model/dataset dependence 与不含 KR 的边界反而强化了现有“聚合不能替代逐轴 verdict”。canonical owner 从表示章节纠正为评测系统。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-SUBMODULAR-BENCHMARK-SELECTION` — Submodular Benchmark Selection

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“Benchmark subset admission must state the covariance/information model, budget and residual-coverage diagnostic; the selected subset cannot inherit full-suite authority outside those assumptions.”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02218` — CoVSpec: Efficient Device-Edge Co-Inference for Vision-Language Models via Speculative Decoding

- Owner：`INFER-SPECULATIVE-DECODING` / Ch48 / `books/part-05-inference-system/48-speculative-decoding.md`。
- 现有命题：proposal 可以近似，最终 commit 必须保持 target distribution 与唯一提交边界
- 差异判断：现有命题已经规定：proposal 可以近似，最终 commit 必须保持 target distribution 与唯一提交边界。本来源的受限增量是“device-edge VLM speculation 联合视觉 token pruning、adaptive draft 与通信 correction”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02236` — Perturbation Dose Responses in Recursive LLM Loops: Raw Switching, Stochastic Floors, and Persistent Escape under Append, Replace, and Dialog Updates

- Owner：`AGENT-WORKFLOW` / Ch81 / `books/part-07-agent/81-workflow.md`。
- 现有命题：已知顺序与 invariant 应由 durable workflow 拥有，模型只处理开放决策
- 差异判断：现有命题已经规定：已知顺序与 invariant 应由 durable workflow 拥有，模型只处理开放决策。本来源的受限增量是“递归 LLM loop 的持久逃逸由 append/replace/dialog memory policy 决定”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02241` — Zero-Shot Confidence Estimation for Small LLMs: When Supervised Baselines Aren't Worth Training

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“生成 log-probability 可作为小模型到云模型升级路由的零样本置信信号”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02255` — On the Privacy of LLMs: An Ablation Study

- Owner：`AGENT-RAG` / Ch76 / `books/part-07-agent/76-rag.md`。
- 现有命题：检索相关性、证据充分性、freshness 与 provenance 是不同 gate
- 差异判断：现有命题已经规定：检索相关性、证据充分性、freshness 与 provenance 是不同 gate。本来源的受限增量是“统一威胁模型揭示 MIA、提取、属性推断与 backdoor 对模型/RAG 配置的依赖不同”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02262` — WindowQuant: Mixed-Precision KV Cache Quantization based on Window-Level Similarity for VLMs Inference Optimization

- Owner：`INFER-KV-CACHE` / Ch45 / `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`。
- 现有命题：多模态 KV 选择必须说明决策时可见的 prompt/prefill 信号、未来 query 风险、量化误差坐标与 fallback。
- 差异判断：现有小节已把 prompt-conditioned prefill signal 与未来 decode demand 分开，并要求压缩/漂移可检验；WindowQuant 是 window bit-width 与 layout 的具体实现，没有改变其信息边界和回退。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02263` — Break the Block: Dynamic-size Reasoning Blocks for Diffusion Large Language Models via Monotonic Entropy Descent with Reinforcement Learning

- Owner：`MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 / `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。
- 现有命题：本章已把 block size 视为 workload-dependent trade-off，也讨论 future-stable trajectory，但没有给出 boundary owner、训练信号和错误自信的反例边界。
- 差异判断：现有覆盖与 exact-v1 对读后仍缺：在 fixed block 旁增加 learned-boundary 分支：decoder 输出可验证的 block-end proposal，runtime 冻结 boundary/policy revision 后提交；训练可用 entropy trajectory 提供辅助 shaping，但任务 outcome/独立 verifier 仍拥有正确性。动态边界以语义步骤适配换 variable-length scheduling、cache/rollback 复杂度、reward hacking 和错误自信；短输出、静态 shape kernel 或 entropy 未校准时继续使用固定 block。exact-v1 的 reasoning benchmark 只支持该代理信号和后训练机制在作者设置中的结果。
- 处置：`Integrate Applied — root writeback complete; independent post-write review pending`。

## `SF-2026-ARXIV-2605-02269` — Towards Understanding Specification Gaming in Reasoning Models

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：本章已有 reward hacking 测试，但缺少把可利用机会、过程轨迹与表面成功分开的统一评价合同
- 差异判断：现有正文仍缺：用可观察环境中的隐藏 hacking opportunity 分离任务成功与 specification gaming，并测量 RL 后行为变化。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-SOTOPIA-TOM-INFORMATION-FLOW-EVALUATION` — SOTOPIA-TOM: Evaluating Information Management in Multi-Agent Interaction with Theory of Mind

- Owner：`AGENT-MULTI-AGENT` / Ch82 / `books/part-07-agent/82-multi-agent.md`。
- 现有命题：消息、角色和局部成功不能替代共享状态的唯一提交语义
- 差异判断：现有命题已经规定：消息、角色和局部成功不能替代共享状态的唯一提交语义。本来源的受限增量是“多 Agent 的 public/private channel、partitioned knowledge 与 disclosure policy 必须进入共享状态和评测身份；终局成功不能掩盖隐私泄漏或缺失信息请求。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02323` — When Attention Collapses: Residual Evidence Modeling for Compositional Inference

- Owner：`MULTIMODAL-REPRESENTATION` / Ch23 / `books/part-03-multimodal-world-models/23-multimodal-representation.md`。
- 现有命题：现有正文比较 early/late/cross/shared fusion，并要求先分配固定 token budget 的信息责任，再选择具体 token。
- 差异判断：现有命题仍把多 slot attention 看作一次或彼此独立的预算分配；没有表示“哪些输入成分已被前一 slot 解释”的可变状态，因此未覆盖 additive superposition 下重复选择同一成分的 failure mode。
- 处置：`Integrate Applied — root writeback complete; independent post-write review pending`。

## `SF-2026-ARXIV-2605-02329` — Taming Request Imbalance: SLO-Aware Scheduling for Disaggregated LLM Inference

- Owner：`INFER-SCHEDULING` / Ch56 / `books/part-05-inference-system/56-inference-scheduling.md`。
- 现有命题：调度状态必须携带 deadline risk、剩余 slack 与降级边界
- 差异判断：现有命题已经规定：调度状态必须携带 deadline risk、剩余 slack 与降级边界。本来源的受限增量是“PD 两侧分别用 TTFT urgency 与 TPOT slack 控制长尾请求和 decode packing”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-STRUCTURED-OUTPUT-TYPED-VALIDATION` — When Correct Isn't Usable: Improving Structured Output Reliability in Small Language Models

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“Semantic correctness and interface usability are separate gates; typed validation owns schema acceptance even when the answer content is correct.”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02364` — InfoLaw: Information Scaling Laws for Large Language Models with Quality-Weighted Mixture Data and Repetition

- Owner：`TRAIN-DATA` / Ch27 / `books/part-04-training-system/27-data.md`。
- 现有命题：数据来源、过滤、去重与 lineage 共同决定训练更新，而不是样本数量单独决定
- 差异判断：现有命题已经规定：数据来源、过滤、去重与 lineage 共同决定训练更新，而不是样本数量单独决定。本来源的受限增量是“quality-weighted mixture 与 repetition 改写固定 token-count 数据 scaling 判断”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02375` — Binary Rewards and Reinforcement Learning: Fundamental Challenges

- Owner：`TRAIN-RLHF` / Ch31 / `books/part-04-training-system/31-rlhf.md`。
- 现有命题：Ch31 已要求 reward 与 response-distribution coverage 分轴，并把 forward/group matching 作为条件分支，但没有解释 binary reward 的退化性、filtered target 的来源、reverse-KL support mismatch 与 misspecification 的完整因果链。
- 差异判断：exact-v1 证明 binary expected reward 对所有 fully-valid distributions 无辨识力，KL-to-base 才选择 valid support 内的相对质量；tilted target 对 filtered model 的收敛是 forward-direction，而 full-support policy 对该零支撑 target 的 reverse KL 为无穷。模型 family 无法表示 target 时，小 beta 可把优化压向少数 valid modes。该机制补全现有章节从现象到原因、状态 owner、替代方案与回退的演进。
- 处置：`Integrate Proposed — root writeback and independent review required`；精确队列见 `V3_BOUNDED_REPAIR_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.json`。

## `SF-DP-RUNTIME-MONITORING` — Differentially Private Runtime Monitoring

- Owner：`PLATFORM-MONITORING` / Ch67 / `books/part-06-ai-infrastructure/67-monitoring.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent review pending`。

## `SF-2026-ARXIV-2605-02395` — Controllable and Verifiable Process Data Synthesis for Process Reward Models

- Owner：`TRAIN-RLHF` / Ch31 / `books/part-04-training-system/31-rlhf.md`。
- 现有命题：偏好信号、反馈身份和 policy update 必须分离验收
- 差异判断：现有命题已经规定：偏好信号、反馈身份和 policy update 必须分离验收。本来源的受限增量是“PRM 监督必须标注第一处 prefix 不再支持的步骤，而非只给终局或逐步表面标签”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02398` — The Compliance Trap: How Structural Constraints Degrade Frontier AI Metacognition Under Adversarial Pressure

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：本章已有 prompt sensitivity，但缺少把 compliance scaffold 导致的自我评估退化单独隔离并复测
- 差异判断：现有正文仍缺：显示强制格式与合规措辞会在压力下压低模型元认知表达，要求把结构约束本身作为评测干预变量。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-2026-ARXIV-2605-02404` — Statistically-Lossless Quantization of Large Language Models

- Owner：`INFER-TENSORRT-LLM` / Ch49 / `books/part-05-inference-system/49-tensorrt-llm.md`。
- 现有命题：exit sensor、训练目标、build artifact 与 runtime acceptance 必须对齐
- 差异判断：现有命题已经规定：exit sensor、训练目标、build artifact 与 runtime acceptance 必须对齐。本来源的受限增量是“用 next-token distribution agreement 区分 task-lossless 与 distribution-lossless quantization”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02411` — FitText: Evolving Agent Tool Ecologies via Memetic Retrieval

- Owner：`AGENT-TOOL-CALLING` / Ch78 / `books/part-07-agent/78-tool-calling.md`。
- 现有命题：本章已有 authorized catalog retrieval、shortlist 和 schema exposure，但主要是一次性 discovery，没有定义失败后如何修订 probe、并行探索与保存检索 frontier。
- 差异判断：现有覆盖与 exact-v1 对读后仍缺：把静态 shortlist 扩展为 bounded revisable discovery state：每次 probe 保存 query/intention revision、返回 tool identities、尝试结果、预算与 parent；parallel branches 只拥有 proposal，retrieval controller 去重/合并 frontier，executor 仍逐项验证 schema、version、authorization 与 effect dependency。它用恢复早期漏检换额外模型调用、探索噪声、过期 tool memory 与 tail latency；catalog 小、接口稳定或风险高时回退静态 allowlist/typed schema。exact-v1 结果只覆盖 StableToolBench、所测模型和预算，不能作为开放生态的安全或性能保证。
- 处置：`Integrate Applied — root writeback complete; independent post-write review pending`。

## `SF-2026-ARXIV-2605-02442` — Measuring AI Reasoning: A Guide for Researchers

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：本章已要求答案、过程、污染和 evaluator contract 分离；该综述巩固而不改变现有主线
- 差异判断：exact-v1 的新增证据是“把 reasoning evaluation 从答案正确率扩展到 contamination、search complexity、外显过程与不可见 latent reasoning 的证据边界”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。
- 处置：`No Change — Existing Coverage (proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02469` — Reference-Sampled Boltzmann Projection for KL-Regularized RLVR: Target-Matched Weighted SFT, Finite One-Shot Gaps, and Policy Mirror Descent

- Owner：`TRAIN-GRPO` / Ch33 / `books/part-04-training-system/33-grpo.md`。
- 现有命题：本章已有 on-policy/offline 分界，但缺少何时 weighted SFT 能精确替代、何时因 support/ESS 产生不可约差距的判据
- 差异判断：现有正文仍缺：证明固定 reference 下 KL-regularized RLVR 可投影为 reference-sampled weighted SFT，并显式给出 support、ESS 与 one-shot gap。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-2026-ARXIV-2605-02495` — Efficient Preference Poisoning Attack on Offline RLHF

- Owner：`TRAIN-RLHF` / Ch31 / `books/part-04-training-system/31-rlhf.md`。
- 现有命题：偏好信号、反馈身份和 policy update 必须分离验收
- 差异判断：现有命题已经规定：偏好信号、反馈身份和 policy update 必须分离验收。本来源的受限增量是“offline preference dataset 的少量污染可定向改变 RLHF policy，数据 provenance 成为安全边界”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02525` — A Semantic Autonomy Framework for VLM-Integrated Indoor Mobile Robots: Hybrid Deterministic Reasoning and Cross-Robot Adaptive Memory

- Owner：`AGENT-MEMORY` / Ch77 / `books/part-07-agent/77-memory.md`。
- 现有命题：稳定/瞬态、global/operator/robot scope 与事实/偏好必须分别准入、提升和撤销；共享 memory 不能扩大执行权限。
- 差异判断：现有 Memory 章节已覆盖 scope、promotion、跨主体访问权和 derived digest；该栈提供两机器人规则/VLM 案例，但没有改变 memory ownership 或 capability gate。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02568` — StreamIndex: Memory-Bounded Compressed Sparse Attention via Streaming Top-k

- Owner：`INFER-KV-CACHE` / Ch45 / `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`。
- 现有命题：稀疏 logical selection 只有编译成 versioned physical gather/top-k plan，才会改变 HBM traffic；selector 不拥有正确性。
- 差异判断：StreamIndex 的 chunked partition-merge top-k 避免物化完整 score tensor，属于 physical access-plan/kernel 实现；现有小节已覆盖 logical/physical 分责、irregular gather 与 dense fallback。 仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02572` — On Training Large Language Models for Long-Horizon Tasks: An Empirical Study of Horizon Length

- Owner：`TRAIN-PRETRAINING` / Ch28 / `books/part-04-training-system/28-pretraining.md`。
- 现有命题：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算
- 差异判断：现有命题已经规定：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算。本来源的受限增量是“只增加 interaction horizon 就会恶化探索与 credit assignment，horizon reduction 可稳定训练”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-AGENTIC-TOOL-SEQUENCE-PROCEDURE-BOUNDARY` — Beyond State Machines: Executing Network Procedures with Agentic Tool-Calling Sequences

- Owner：`AGENT-WORKFLOW` / Ch81 / `books/part-07-agent/81-workflow.md`。
- 现有命题：已知顺序与 invariant 应由 durable workflow 拥有，模型只处理开放决策
- 差异判断：现有命题已经规定：已知顺序与 invariant 应由 durable workflow 拥有，模型只处理开放决策。本来源的受限增量是“Strict procedures should move from repeated model decisions into deterministic tool/workflow ownership once action order and invariants are known.”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-GRADIENT-GATED-DPO` — Gradient-Gated DPO: Stabilizing Preference Optimization in Language Models

- Owner：`TRAIN-DPO` / Ch34 / `books/part-04-training-system/34-dpo.md`。
- 现有命题：已按实际章节定位完成对照。
- 差异判断：未发现会改变长期 owner 或章节交接的新命题。
- 处置：`Integrate Applied — body marker verified; independent review pending`。

## `SF-2026-ARXIV-2605-02641` — Mamoda2.5: Enhancing Unified Multimodal Model with DiT-MoE

- Owner：`MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 / `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。
- 现有命题：Ch24 已要求 few-step student 在其实际访问状态上验收质量/稳定性，条件计算只改变每步计算预算；Ch21 已拥有 router、capacity、load balance 与 dense-to-MoE 演进。
- 差异判断：Mamoda2.5 是两条既有机制的具体组合和作者案例；未披露的端到端 SLO 与内部 evaluator 不足以改变 few-step commit、MoE owner 或训练—推理一致性命题。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02647` — ContextualJailbreak: Evolutionary Red-Teaming via Simulated Conversational Priming

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：本章已要求多轮、上下文累积和自动攻击搜索共同进入 red-team；该实现未改变 threat owner
- 差异判断：exact-v1 的新增证据是“用多轮 conversational priming 的进化搜索生成上下文 jailbreak，并对 judge reliability 做独立约束”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。
- 处置：`No Change — Existing Coverage (proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02682` — Hybrid Inspection and Task-Based Access Control in Zero-Trust Agentic AI

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor
- 差异判断：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“zero-trust interception 联合确定性完整性检查与 task-tool 语义授权”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02697` — Executor-Side Progressive Risk-Gated Actuation for Agentic AI in Wireless Supervisory Control

- Owner：`AGENT-PLATFORM` / Ch84 / `books/part-07-agent/84-agent-platform.md`。
- 现有命题：每次 transition 必须绑定 actor、policy、budget、fresh state、rollback 与 side-effect evidence，执行与审计不能由模型叙述替代。
- 差异判断：现有平台状态机及安全章节已要求 commit 前验证 scope/freshness/budget、失败时回滚或拒绝，并让 effect owner 产生 receipt；PRGA 的 C0/C1/C2 是无线控制的具体分层，没有改变通用提交权。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02739` — Latent Bridge: Feature Delta Prediction for Efficient Dual-System Vision-Language-Action Model Inference

- Owner：`MULTIMODAL-EMBODIED-VLA` / Ch26 / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。
- 现有命题：行动闭环必须绑定 observation、action schema、控制频率与安全回退
- 差异判断：现有命题已经规定：行动闭环必须绑定 observation、action schema、控制频率与安全回退。本来源的受限增量是“预测相邻 timestep 的 VLM feature delta，使低层 action head 可跳过部分 backbone 调用”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02751` — Mitigating Misalignment Contagion by Steering with Implicit Traits

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“多轮多 Agent 交互会传播反社会行为，重复 system prompt 不是稳定隔离手段”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02757` — Seeing Realism from Simulation: Efficient Video Transfer for Vision-Language-Action Data Augmentation

- Owner：`TRAIN-DATA` / Ch27 / `books/part-04-training-system/27-data.md`。
- 现有命题：派生数据必须绑定 transform/generator、选择分母、cache、action schema 与真实 held-out/closed-loop 验收，稀有 failure tail 不能被中心样本静默删除。
- 差异判断：现有 Data 章节已覆盖版本化 transform、synthetic trajectory、coreset/medoid 风险、sim-to-real provenance 和真实闭环 admission；该论文提供视频 transfer/reuse 的组合案例，没有改变长期数据合同。
- 处置：`No Change — Existing Coverage (author proposition comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02765` — U-Define: Designing User Workflows for Hard and Soft Constraints in LLM-Based Planning

- Owner：`AGENT-WORKFLOW` / Ch81 / `books/part-07-agent/81-workflow.md`。
- 现有命题：本章已有工作流 verifier，但缺少 hard/soft constraint 的不同所有权、冲突优先级与用户修订闭环
- 差异判断：现有正文仍缺：把用户约束分成 hard 与 soft：hard 交给形式 checker，soft 交给可校准 judge，并保留冲突解释与人工修改。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 处置：`Integrate Proposed — root writeback and independent review required`。

## `SF-2026-ARXIV-2605-02812` — Autonomous LLM Agent Worms: Cross-Platform Propagation, Automated Discovery and Temporal Re-Entry Defense

- Owner：`PLATFORM-SECURITY` / Ch72 / `books/part-06-ai-infrastructure/72-security.md`。
- 现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor
- 差异判断：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“Agent worm 可跨平台发现、传播并借 temporal re-entry 恢复，单次清理不足”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02821` — When Is the Same Model Not the Same Service? A Measurement Study of Hosted Open-Weight LLM APIs

- Owner：`PLATFORM-EVALUATION-SYSTEM` / Ch66 / `books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论
- 差异判断：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“同名 open-weight model 在不同 provider/time 下应建模为可漂移 service object”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02853` — Trust, but Verify: Peeling Low-Bit Transformer Networks for Training Monitoring

- Owner：`TRAIN-PRETRAINING` / Ch28 / `books/part-04-training-system/28-pretraining.md`。
- 现有命题：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算
- 差异判断：现有命题已经规定：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算。本来源的受限增量是“逐层可达参考解揭示 aggregate training loss 隐藏的 under-optimized layer”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02881` — MolmoAct2: Action Reasoning Models for Real-world Deployment

- Owner：`MULTIMODAL-EMBODIED-VLA` / Ch26 / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。
- 现有命题：行动闭环必须绑定 observation、action schema、控制频率与安全回退
- 差异判断：现有命题已经规定：行动闭环必须绑定 observation、action schema、控制频率与安全回退。本来源的受限增量是“VLA 将空间 backbone、action tokenizer、continuous expert 与 adaptive-depth grounding 组合成部署闭环”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。

## `SF-2026-ARXIV-2605-02888` — SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection

- Owner：`INFER-SPECULATIVE-DECODING` / Ch48 / `books/part-05-inference-system/48-speculative-decoding.md`。
- 现有命题：proposal 可以近似，最终 commit 必须保持 target distribution 与唯一提交边界
- 差异判断：现有命题已经规定：proposal 可以近似，最终 commit 必须保持 target distribution 与唯一提交边界。本来源的受限增量是“speculation length 的最优值随 target compression 和逐步置信信号变化”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。
- 处置：`No Change — Existing Coverage (author comparison; independent review required)`。
