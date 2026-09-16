# Daily Research — 2026-05-05

**规范：** V3

**窗口：** 2026-05-04T09:00:00+08:00 ～ 2026-05-05T09:00:00+08:00

**状态：** 完成

**Books：** 纳入本次

**Books Gate：** Passed（53 项 Applied；128 项 No Change；root 写回与 fresh non-author 最小范围终审均已完成）

**检查时间：** 2026-09-15T11:01:28+08:00

## 1. 结论

作者侧已完成本窗 arXiv 候选分母重建：1058 个去重 raw identity 全部经过题名与完整摘要语义筛选，冻结 181 个贡献候选，877 个以 family-specific 理由在分母前关闭，语义待判定为 0。这个数量表示需要证据核验的项目增量，不表示 181 篇结论均成立。完整逐项状态见 [V3 canonical ledger](../_sources/daily-20260505/V3_CANONICAL_LEDGER.json)。

181 个候选现已全部完成 Evidence Review：96 项深入审阅、85 项标准审阅；53 项 `Integrate Applied`、128 项 proposition-level `No Change`，`Blocked / Unverified` 为 0。原受阻的 `2605.02196v1`、`2605.02206v1`、`2605.02375v1` 已恢复完整 exact-v1 并完成 Method、evaluation、limitations、评分与 Books 比较；`2605.01710v1` 的实际 method locator 已补齐，`2605.01771v1` 已统一到 `PLATFORM-EVALUATION-SYSTEM` / Ch66，拒绝在 Ch69 重复写入。`2605.02375v1` 的语义增量已由 root 写入 Ch31，并通过未参与返修或写回的 fresh non-author 最小范围终审；本 Daily 已闭环。

日期归属使用 [arXiv 公告批次共同依据](../_sources/ARXIV_ANNOUNCEMENT_PROVENANCE.md)：initial registration、ID/version 与官方 Monday announcement cadence 一致，故记录本批次于北京时间 2026-05-05 08:00 公开。较早 submitted_v1 可由 moderation hold 造成，不单独构成冲突。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [https://openai.com/research/](https://openai.com/research/)；旧稿仅记录严格窗口零命中，未保存窗口两侧最近条目或分页停止点 | 受阻 | 缺历史列表的可复查停止位置；不支持零遗漏断言 |
| SRC-ANTHROPIC | [https://www.anthropic.com/research](https://www.anthropic.com/research)；已检查夹住窗口的 2026-04-30 与 2026-05-07 两个相邻发布日 | 已检查 | 无 |
| SRC-GOOGLE-AI | [https://deepmind.google/research/](https://deepmind.google/research/)；DeepMind 与 Google Research 历史目录的可见日期粒度不足，旧记录没有形成夹住窗口的确定停止点 | 受阻 | 缺能按 24 小时窗口核验的历史目录或归档快照 |
| SRC-META-AI | [https://ai.meta.com/research/](https://ai.meta.com/research/)；历史 Publications 列表检查至覆盖目标窗口，窗口内 1 个条目；与 arXiv 2605.01188 同一 family | 已检查 | 无；已按 Source Family 去重 |
| SRC-QWEN | [https://qwenlm.github.io/](https://qwenlm.github.io/)；历史博客目录无法稳定恢复逐条发布日期，旧记录没有可复查停止点 | 受阻 | 缺目标窗口时的官方目录快照或带发布日期的条目索引 |
| SRC-DEEPSEEK | [https://www.deepseek.com/](https://www.deepseek.com/)；检查至窗口前最近可核验事件 2026-04-24；目标窗口无条目 | 已检查 | 无 |
| SRC-MOONSHOT | [https://platform.kimi.com/blog](https://platform.kimi.com/blog)；旧稿仅记录目标窗口零命中，未保存博客/仓库窗口两侧停止条目 | 受阻 | 缺可复查的历史停止位置；不支持零遗漏断言 |
| SRC-TENCENT-HUNYUAN | [https://hunyuan.tencent.com/research](https://hunyuan.tencent.com/research)；研究页“全部”列表按发布日期检查；窗口两侧最近条目为 2026-04-30 与 2026-05-21 | 已检查 | 无 |
| SRC-ZAI | [https://www.zhipuai.cn/zh/research](https://www.zhipuai.cn/zh/research)；研究目录按发布日期检查；窗口两侧最近条目为 2026-04-29 与 2026-05-20 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | [https://seed.bytedance.com/en/research](https://seed.bytedance.com/en/research)；Research/Public Papers 按发布日期检查；窗口两侧最近条目为 2026-04-26 与 2026-05-16 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | [https://ernie.baidu.com/blog/zh/](https://ernie.baidu.com/blog/zh/)；技术博客按发布日期检查；窗口两侧最近条目为 2026-04-30 与 2026-05-09 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | [https://mimo.xiaomi.com/](https://mimo.xiaomi.com/)；Papers 可见列表已查至目标窗口且无命中；Blog 历史目录没有保存可复查日期停止点 | 受阻 | Blog 分支缺带发布日期的历史目录或归档快照 |
| SRC-MINIMAX | [https://www.minimax.io/blog](https://www.minimax.io/blog)；历史研究/博客列表检查至窗口后首个事件 2026-05-13；目标窗口无条目 | 已检查 | 无 |
| SRC-ARXIV | [官方 announcement schedule](https://info.arxiv.org/help/availability.html#announcement-schedule) 与 owner replay；Monday batch 1058 个去重 identity 全量题摘筛选，181 retain + 877 closure；181 项 exact-v1 Evidence Review 完成 | 已检查 | 无候选正文受阻；历史目录型来源的覆盖缺口单列于 §5 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Separating Intelligence from Execution: A Workflow Engine for the Model Context Protocol](https://arxiv.org/html/2605.00827v1) | 2026-05-05T08:00:00+08:00 | 以声明式 blueprint 和幂等执行器把 MCP 智能提议与工作流执行分开；2+2+1=5 | 标准完成 | 已有覆盖：`AGENT-MCP` / [Ch83](../../../../books/part-07-agent/83-mcp.md)；逐命题比较已完成并通过独立复核 |
| [GhostServe: A Lightweight Checkpointing System in the Shadow for Fault-Tolerant LLM Serving](https://arxiv.org/html/2605.00831v1) | 2026-05-05T08:00:00+08:00 | 用 host-memory erasure-coded shadow checkpoint 保护增长中的 KV 状态并支持故障恢复；3+3+2=8 | 深入完成 | 已有覆盖：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；逐命题比较已完成并通过独立复核 |
| [Synthetic Designed Experiments for Diagnosing Vision Model Failure](https://arxiv.org/html/2605.00832v1) | 2026-05-05T08:00:00+08:00 | 把可控合成生成器当作实验装置，用因子设计区分 coverage gap 与 spurious dependency 并定向补数；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [From Euler to Dormand-Prince: ODE Solvers for Flow Matching Generative Models](https://arxiv.org/html/2605.00836v1) | 2026-05-05T08:00:00+08:00 | 把 flow-matching 采样器从固定 Euler 步进提升为可比较的高阶与自适应 ODE 求解器，并以 NFE-quality frontier 暴露模型误差与数值误差的共同上限；2+2+2=6 | 标准完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；逐命题比较已完成并通过独立复核 |
| [Understanding Emergent Misalignment via Feature Superposition Geometry](https://arxiv.org/html/2605.00842v1) | 2026-05-05T08:00:00+08:00 | 非正交 superposition 使目标微调沿几何邻近方向产生 gradient spillover；3+2+2=7 | 深入完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；逐命题比较已完成并通过独立复核 |
| [LiteVLA-H: Dual-Rate Vision-Language-Action Inference for Onboard Aerial Guidance and Semantic Perception](https://arxiv.org/html/2605.00884v1) | 2026-05-05T08:00:00+08:00 | 把 VLA 的短 action-token 外环与较慢语义输出拆成双速路径，并把 prefill 主导延迟、控制频率和知识保持训练放进同一部署合同。；3+3+2=8 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；逐命题比较已完成并通过独立复核 |
| [The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate](https://arxiv.org/html/2605.00914v1) | 2026-05-05T08:00:00+08:00 | 同质 debate 暴露从众、上下文脆弱和投票丢失已有正确答案的三条失败路径；2+2+1=5 | 标准完成 | 已有覆盖：`AGENT-MULTI-AGENT` / [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；逐命题比较已完成并通过独立复核 |
| [Watch Your Step: Information Injection in Diffusion Models via Shadow Timestep Embedding](https://arxiv.org/html/2605.00935v1) | 2026-05-05T08:00:00+08:00 | diffusion timestep embedding 可经 scheduler interface 成为隐蔽信息注入与 provenance side channel；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 正文 marker 已回读并通过独立复核 |
| [From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity](https://arxiv.org/html/2605.00939v1) | 2026-05-05T08:00:00+08:00 | 以参数梯度敏感度近似局部曲率，区分可被小扰动修正的普通错误与对输入改写仍稳定的 stubborn hallucination；3+2+2=7 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 正文 marker 已回读并通过独立复核 |
| [E-MIA: Exam-Style Black-Box Membership Inference Attacks against RAG Systems](https://arxiv.org/html/2605.00955v1) | 2026-05-05T08:00:00+08:00 | 以可客观评分的 hard-evidence probes 推断 RAG 语料成员身份；2+2+1=5 | 标准完成 | 已有覆盖：`AGENT-RAG` / [Ch76](../../../../books/part-07-agent/76-rag.md)；逐命题比较已完成并通过独立复核 |
| [SRTJ: Self-Evolving Rule-Driven Training-Free LLM Jailbreaking](https://arxiv.org/html/2605.00974v1) | 2026-05-05T08:00:00+08:00 | 分层规则记忆同时积累成功与失败攻击经验，使 jailbreak 策略跨目标持续演化；2+2+1=5 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；逐命题比较已完成并通过独立复核 |
| [Most Current Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives](https://arxiv.org/html/2605.00994v1) | 2026-05-05T08:00:00+08:00 | 用基模/微调模的 perplexity difference 暴露 model-organism 的微调目标；2+2+1=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [Effect-Transparent Governance for AI Workflow Architectures: Semantic Preservation, Expressive Minimality, and Decidability Boundaries](https://arxiv.org/html/2605.01030v1) | 2026-05-05T08:00:00+08:00 | 用 effect-transparent 语义边界约束 AI workflow 的表达能力与可判定性；2+2+2=6 | 标准完成 | 已有覆盖：`AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md)；逐命题比较已完成并通过独立复核 |
| [Algebraic Semantics of Governed Execution: Monoidal Categories, Effect Algebras, and Coterminous Boundaries](https://arxiv.org/html/2605.01032v1) | 2026-05-05T08:00:00+08:00 | 以 capability-indexed effect system 和可机检 handler algebra 将治理边界绑定到可表达程序；3+3+2=8 | 深入完成 | 整合：`AGENT-PLATFORM` / [Ch84](../../../../books/part-07-agent/84-agent-platform.md) 正文 marker 已回读并通过独立复核 |
| [Certified Purity for Cognitive Workflow Executors: From Static Analysis to Cryptographic Attestation](https://arxiv.org/html/2605.01037v1) | 2026-05-05T08:00:00+08:00 | 把静态 purity 证明签名成运行时可校验的执行凭证并显式保留 TCB；3+3+2=8 | 深入完成 | 已有覆盖：`AGENT-PLATFORM` / [Ch84](../../../../books/part-07-agent/84-agent-platform.md)；逐命题比较已完成并通过独立复核 |
| [LLM Ghostbusters: Surgical Hallucination Suppression via Adaptive Unlearning](https://arxiv.org/html/2605.01047v1) | 2026-05-05T08:00:00+08:00 | 把已观测 package hallucination 转成可定位的 post-deployment unlearning 对象，并用自适应 masking 限制能力 collateral damage；2+2+2=6 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；逐命题比较已完成并通过独立复核 |
| [Compared to What? Baselines and Metrics for Counterfactual Prompting](https://arxiv.org/html/2605.01048v1) | 2026-05-05T08:00:00+08:00 | 用 meaning-preserving perturbation 作为反事实 baseline，避免把表面改写误判为目标因素效应；2+2+1=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [LEAP: Layer-wise Exit-Aware Pretraining for Efficient Transformer Inference](https://arxiv.org/html/2605.01058v1) | 2026-05-05T08:00:00+08:00 | Layer-aligned distillation 会抑制 convergence-based early exit 所依赖的中间层收敛；训练目标必须显式塑造可退出状态，并保留 full-depth 回退。；3+2+2=7 | 深入完成 | 整合：`INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 正文 marker 与修正后的 Daily trace 已回读并通过独立复核 |
| [SURGE: SuperBatch Unified Resource-efficient GPU Encoding for Heterogeneous Partitioned Data](https://arxiv.org/html/2605.01060v1) | 2026-05-05T08:00:00+08:00 | SuperBatch 在跨分区 embedding 中同时给出有界内存、流式首输出与故障恢复粒度；2+2+1=5 | 标准完成 | 已有覆盖：`INFER-GPU-MEMORY` / [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)；逐命题比较已完成并通过独立复核 |
| [Online Safety Filter for Deformable Object Manipulation with Horizon Agnostic Neural Operators](https://arxiv.org/html/2605.01069v1) | 2026-05-05T08:00:00+08:00 | 用 task-level barrier function 在运行时最小修正具身策略动作，而不是把安全隐含进 reward；2+2+1=5 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；逐命题比较已完成并通过独立复核 |
| [Component-Aware Self-Speculative Decoding in Hybrid Language Models](https://arxiv.org/html/2605.01106v1) | 2026-05-05T08:00:00+08:00 | hybrid model 的组件组合方式决定内部 draft 的可接受率与 self-speculation 可行性；2+2+1=5 | 标准完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING` / [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)；逐命题比较已完成并通过独立复核 |
| [When Less is Enough: Efficient Inference via Collaborative Reasoning](https://arxiv.org/html/2605.01111v1) | 2026-05-05T08:00:00+08:00 | 由小模型先执行、再按边际效用与长度惩罚决定是否升级大模型，把协作推理变成请求级资源控制；2+3+2=7 | 深入完成 | 已有覆盖：`INFER-SCHEDULING` / [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；逐命题比较已完成并通过独立复核 |
| [Revisiting Privacy Leakage in Machine Unlearning: Membership Inference Beyond the Forgotten Set](https://arxiv.org/html/2605.01129v1) | 2026-05-05T08:00:00+08:00 | unlearning 前后差分会把隐私泄漏从 forget set 扩展到 retain set；2+2+1=5 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；逐命题比较已完成并通过独立复核 |
| [Iterative Finetuning is Mostly Idempotent](https://arxiv.org/html/2605.01130v1) | 2026-05-05T08:00:00+08:00 | 连续 SFT/SDF 多数近似幂等，而持续 DPO 且不重置模型时才稳定放大特征；2+2+1=5 | 标准完成 | 已有覆盖：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；逐命题比较已完成并通过独立复核 |
| [When Embedding-Based Defenses Fail: Rethinking Safety in LLM-Based Multi-Agent Systems](https://arxiv.org/html/2605.01133v1) | 2026-05-05T08:00:00+08:00 | embedding 防御在多轮多 Agent 传播中衰减，暴露局部过滤并非系统安全边界；2+2+1=5 | 标准完成 | 已有覆盖：`AGENT-MULTI-AGENT` / [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；逐命题比较已完成并通过独立复核 |
| [Metric-Normalized Posterior Leakage (mPL): Attacker-Aligned Privacy for Joint Consumption](https://arxiv.org/html/2605.01137v1) | 2026-05-05T08:00:00+08:00 | 联合观察会聚合相关证据，使逐记录 metric-DP 保证不能约束 posterior leakage；2+2+1=5 | 深入完成 | 整合：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 正文 marker 已回读并通过独立复核 |
| [Arithmetic in the Wild: Llama uses Base-10 Addition to Reason About Cyclic Concepts](https://arxiv.org/html/2605.01148v1) | 2026-05-05T08:00:00+08:00 | 用跨任务 activation patching 与 Fourier probe 显示加法子电路可被循环概念复用，并定位稀疏 MLP 子电路；2+1+2=5 | 标准完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；逐命题比较已完成并通过独立复核 |
| [Minimizing Collateral Damage in Activation Steering](https://arxiv.org/html/2605.01167v1) | 2026-05-05T08:00:00+08:00 | 在保持目标 steering 幅度的约束面上最小化二阶 collateral energy，把 activation steering 写成受约束几何优化；2+2+2=6 | 标准完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；逐命题比较已完成并通过独立复核 |
| [A Theory of Generalization in Deep Learning](https://arxiv.org/html/2605.01172v1) | 2026-05-05T08:00:00+08:00 | 把深度学习泛化拆成可被测试点看到的 signal channel 与训练集 reservoir，并用 drift-diffusion 与 train-test coupling 刻画误差；3+2+2=7 | 深入完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；逐命题比较已完成并通过独立复核 |
| [Compute Optimal Tokenization](https://arxiv.org/html/2605.01188v1) | 2026-05-05T08:00:00+08:00 | compute-optimal allocation 随 bytes 而非 token 数缩放，token compression rate 成为训练变量；3+2+2=7 | 深入完成 | 已有覆盖：`TRAIN-DATA` / [Ch27](../../../../books/part-04-training-system/27-data.md)；逐命题比较已完成并通过独立复核 |
| [Sentinel-VLA: A Metacognitive VLA Model with Active Status Monitoring for Dynamic Reasoning and Error Recovery](https://arxiv.org/html/2605.01191v1) | 2026-05-05T08:00:00+08:00 | 由 active sentinel 持有实时执行状态，只在初始化、新子任务或错误时触发 reasoning/recovery，并把能力边界反馈到持续数据收集。；3+3+2=8 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；逐命题比较已完成并通过独立复核 |
| [Linear-Readout Floors and Threshold Recovery in Computation in Superposition](https://arxiv.org/html/2605.01192v1) | 2026-05-05T08:00:00+08:00 | 线性 readout 的 cross-talk floor 与非线性 threshold reset 形成不同的 superposition 容量边界；2+2+1=5 | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) 正文 marker 已回读并通过独立复核 |
| [VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model](https://arxiv.org/html/2605.01194v1) | 2026-05-05T08:00:00+08:00 | uncertainty clutch 只在需要时切换到候选动作与相对 action critic 的 deliberation；3+2+2=7 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；逐命题比较已完成并通过独立复核 |
| [TAIL-Safe: Task-Agnostic Safety Monitoring for Imitation Learning Policies](https://arxiv.org/html/2605.01195v1) | 2026-05-05T08:00:00+08:00 | 从状态-动作安全分数构造经验控制不变集，并在越界时触发 recovery；2+2+1=5 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；逐命题比较已完成并通过独立复核 |
| [Focus and Dilution: The Multi-stage Learning Process of Attention](https://arxiv.org/html/2605.01199v1) | 2026-05-05T08:00:00+08:00 | 把 attention 学习描述为 focus、dilution 与再聚焦的阶段性梯度动力学，而非单调收敛；2+2+2=6 | 标准完成 | 已有覆盖：`MODEL-SELF-ATTENTION` / [Ch14](../../../../books/part-02-model/14-self-attention.md)；逐命题比较已完成并通过独立复核 |
| [To Do or Not to Do: Ensuring the Safety of Visuomotor Policies Learned from Demonstrations](https://arxiv.org/html/2605.01201v1) | 2026-05-05T08:00:00+08:00 | 用 execution-guarantee region 将任务成功与是否允许 visuomotor policy 执行绑定；3+2+2=7 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；逐命题比较已完成并通过独立复核 |
| [Faithful Mobile GUI Agents with Guided Advantage Estimator](https://arxiv.org/html/2605.01208v1) | 2026-05-05T08:00:00+08:00 | 以 reward-bound anchors 和方差自适应 tempering 在 collapsed rollout group 中恢复有符号 advantage；3+3+2=8 | 深入完成 | 整合：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md) 正文 marker 已回读并通过独立复核 |
| [Visual Implicit Autoregressive Modeling](https://arxiv.org/html/2605.01220v1) | 2026-05-05T08:00:00+08:00 | 隐式 equilibrium layer 将视觉 AR 的训练内存与推理迭代预算解耦为可调计算状态；2+2+1=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 正文 marker 已回读并通过独立复核 |
| [FP-Agent: Fingerprinting AI Browsing Agents](https://arxiv.org/html/2605.01247v1) | 2026-05-05T08:00:00+08:00 | 浏览 Agent 的行为 fingerprint 比共享浏览器指纹更能支持运行时识别与控制；2+2+1=5 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；逐命题比较已完成并通过独立复核 |
| [Activation Compression in LLMs: Theoretical Analysis and Efficient Algorithm](https://arxiv.org/html/2605.01255v1) | 2026-05-05T08:00:00+08:00 | 只对满足无偏条件的线性算子压缩 activation，并复用低秩因子压缩梯度；2+2+1=5 | 标准完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)；逐命题比较已完成并通过独立复核 |
| [Chain of Evidence: Pixel-Level Visual Attribution for Iterative Retrieval-Augmented Generation](https://arxiv.org/html/2605.01284v1) | 2026-05-05T08:00:00+08:00 | 把多跳 RAG 的证据 owner 从文本引用细化到页面截图的 pixel bounding boxes；2+2+2=6 | 标准完成 | 已有覆盖：`AGENT-RAG` / [Ch76](../../../../books/part-07-agent/76-rag.md)；逐命题比较已完成并通过独立复核 |
| [A Theory of Saddle Escape in Deep Nonlinear Networks](https://arxiv.org/html/2605.01288v1) | 2026-05-05T08:00:00+08:00 | 深层非线性网络的 saddle escape 由 bottleneck-scale 层数而非总深度控制；2+2+2=6 | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) 正文 marker 已回读并通过独立复核 |
| [Lifting Traces to Logic: Programmatic Skill Induction with Neuro-Symbolic Learning for Long-Horizon Agentic Tasks](https://arxiv.org/html/2605.01293v1) | 2026-05-05T08:00:00+08:00 | 轨迹归纳只有被提升为带控制流、动态变量绑定和可执行符号状态的 skill program，才能把 neural proposal 与环境执行权分离。；3+2+2=7 | 深入完成 | 已有覆盖：`AGENT-PLATFORM` / [Ch84](../../../../books/part-07-agent/84-agent-platform.md)；逐命题比较已完成并通过独立复核 |
| [Checkerboard: A Simple, Effective, Efficient and Learning-free Clean Label Backdoor Attack with Low Poisoning Budget](https://arxiv.org/html/2605.01298v1) | 2026-05-05T08:00:00+08:00 | 闭式、data-independent clean-label trigger 将供应链攻击从 surrogate 训练依赖中解耦；2+2+1=5 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；逐命题比较已完成并通过独立复核 |
| [From Stealthy Data Fabrication to Unsafe Driving: Realistic Scenario Attacks on Collaborative Perception](https://arxiv.org/html/2605.01301v1) | 2026-05-05T08:00:00+08:00 | 对共享感知结果的微小 pose 篡改会沿 tracking 与 prediction 数据流放大为不安全控制；2+2+1=5 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；逐命题比较已完成并通过独立复核 |
| [Beyond Semantic Relevance: Counterfactual Risk Minimization for Robust Retrieval-Augmented Generation](https://arxiv.org/html/2605.01302v1) | 2026-05-05T08:00:00+08:00 | 把检索目标从 semantic relevance 改为对错误前提与确认偏误的 counterfactual decision risk，并由 Evidence Critic 产生 robustness score 与 abstention 控制。；3+3+2=8 | 深入完成 | 整合：`AGENT-RAG` / [Ch76](../../../../books/part-07-agent/76-rag.md) 正文 marker 已回读并通过独立复核 |
| [The Partial Testimony of Logs: Evaluation of Language Model Generation under Confounded Model Choice](https://arxiv.org/html/2605.01311v1) | 2026-05-05T08:00:00+08:00 | 只有随机实验与离线 simulator 联合才能识别混杂日志中的因果模型价值；2+2+1=5 | 标准完成 | 已有覆盖：`PLATFORM-TRACE` / [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md)；逐命题比较已完成并通过独立复核 |
| [Segment-Aligned Policy Optimization for Multi-Modal Reasoning](https://arxiv.org/html/2605.01327v1) | 2026-05-05T08:00:00+08:00 | 把 token-level policy MDP 提升为推理 segment MDP，并按自适应分段计算 value、advantage 与 importance ratio；3+3+2=8 | 深入完成 | 整合：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md) 正文 marker 已回读并通过独立复核 |
| [Don’t Be a Pot Stirrer! Authorized Vector Data Retrieval via Access-Aware Indexing](https://arxiv.org/html/2605.01342v1) | 2026-05-05T08:00:00+08:00 | access-aware lattice 让向量索引、存储预算与授权 query plan 共同决定检索；3+3+2=8 | 深入完成 | 已有覆盖：`AGENT-RAG` / [Ch76](../../../../books/part-07-agent/76-rag.md)；逐命题比较已完成并通过独立复核 |
| [The Perceptual Bandwidth Bottleneck in Vision-Language Models: Active Visual Reasoning via Sequential Experimental Design](https://arxiv.org/html/2605.01345v1) | 2026-05-05T08:00:00+08:00 | 把高分辨率视觉推理改写为固定 token 带宽下的顺序 evidence acquisition，controller 在回答前主动选择下一块视觉观测。；3+2+2=7 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 正文 marker 已回读并通过独立复核 |
| [CHASE: Competing Hypotheses for Ambiguity-Aware Selective Prediction](https://arxiv.org/html/2605.01346v1) | 2026-05-05T08:00:00+08:00 | 在部分可观测冲突中比较竞争解释的 margin 决定 commit 或 abstain，而非依赖单分支置信度；2+2+1=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [MAD-OPD: Breaking the Ceiling in On-Policy Distillation via Multi-Agent Debate](https://arxiv.org/html/2605.01347v1) | 2026-05-05T08:00:00+08:00 | 让多个教师在学生 on-policy state 上辩论形成 privileged distribution，并按任务选择 JSD 或 reverse-KL、按 agent step 稳定蒸馏；3+3+2=8 | 深入完成 | 整合：`TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md) 正文 marker 已回读并通过独立复核 |
| [VUDA: Breaking CUDA-Vulkan Isolation for Spatial Sharing of Compute and Graphics on the Same GPU](https://arxiv.org/html/2605.01352v1) | 2026-05-05T08:00:00+08:00 | 打破 CUDA/Vulkan context 隔离，使仿真 compute 与 graphics 可空间复用同一 GPU；2+2+1=5 | 标准完成 | 已有覆盖：`PLATFORM-GPU-SCHEDULER` / [Ch63](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)；逐命题比较已完成并通过独立复核 |
| [Focus on the Core: Empowering Diffusion Large Language Models by Self-Contrast](https://arxiv.org/html/2605.01373v1) | 2026-05-05T08:00:00+08:00 | 用相邻 denoising step 的 top-K 分布差识别高动态 token，并对其自对比重掩码，集中迭代修正预算；3+2+2=7 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 正文 marker 已回读并通过独立复核 |
| [MTA: Multi-Granular Trajectory Alignment for Large Language Model Distillation](https://arxiv.org/html/2605.01374v1) | 2026-05-05T08:00:00+08:00 | 沿教师与学生的层级 transformation trajectory 对齐 token、span 和 hidden representation，而非只对齐末端 logits；2+2+2=6 | 标准完成 | 已有覆盖：`TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md)；逐命题比较已完成并通过独立复核 |
| [MemORAI: Memory Organization and Retrieval via Adaptive Graph Intelligence for LLM Conversational Agents](https://arxiv.org/html/2605.01386v1) | 2026-05-05T08:00:00+08:00 | 长期记忆的过滤、turn-level provenance graph 与 query-adaptive retrieval 是同一 lifecycle 的不同状态；高连接度不能替代 query-specific evidence relevance。；3+2+2=7 | 深入完成 | 已有覆盖：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)；逐命题比较已完成并通过独立复核 |
| [LiveFMBench: Unveiling the Power and Limits of Agentic Workflows in Specification Generation](https://arxiv.org/html/2605.01394v1) | 2026-05-05T08:00:00+08:00 | 形式规约评测必须同时验证 code/spec faithfulness、时间污染与 verifier 非空洞性；自动 prover 通过不能单独构成成功。；3+3+2=8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [AI Safety as Control of Irreversibility: A Systems Framework for Decision-Energy and Sovereignty Boundaries](https://arxiv.org/html/2605.01415v1) | 2026-05-05T08:00:00+08:00 | 把不可逆决策、物理资源动员与自我扩张权限分离为外部可审查的 sovereignty boundaries；2+2+2=6 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；逐命题比较已完成并通过独立复核 |
| [Barriers to Counterfactual Credit Attribution for Autoregressive Models](https://arxiv.org/html/2605.01425v1) | 2026-05-05T08:00:00+08:00 | 自回归输出的生成后 credit attribution 受不可辨识与组合搜索约束；2+2+1=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [SCALE-LoRA: Auditing Post-Retrieval LoRA Composition with Residual Merging and View Reliability](https://arxiv.org/html/2605.01429v1) | 2026-05-05T08:00:00+08:00 | 在开放 LoRA 池检索后，以层级稀疏残差合并和多视图一致性审计决定组合、拒绝或回退；3+2+2=7 | 深入完成 | 整合：`TRAIN-LORA` / [Ch30](../../../../books/part-04-training-system/30-lora.md) 正文 marker 已回读并通过独立复核 |
| [VisInject: Disruption != Injection -- A Dual-Dimension Evaluation of Universal Adversarial Attacks on Vision-Language Models](https://arxiv.org/html/2605.01449v1) | 2026-05-05T08:00:00+08:00 | 将输出扰动与攻击者目标真正注入分开度量，反证单一 attack-success-rate 的安全结论；2+1+2=5 | 深入完成 | 整合：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 正文 marker 已回读并通过独立复核 |
| [Action Agent: Agentic Video Generation Meets Flow-Constrained Diffusion](https://arxiv.org/html/2605.01477v1) | 2026-05-05T08:00:00+08:00 | 以可修订 goal video 作为高层 proposal，并由独立 controller 基于当前观测执行动作；3+3+2=8 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；逐命题比较已完成并通过独立复核 |
| [OmniEncoder: See, Hear, and Feel Continuous Motion Like Humans With One Encoder](https://arxiv.org/html/2605.01506v1) | 2026-05-05T08:00:00+08:00 | 以统一 token template、Omni-RoPE 和时窗移动联合编码视频、音频与运动连续性；2+2+2=6 | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；逐命题比较已完成并通过独立复核 |
| [Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling](https://arxiv.org/html/2605.01566v1) | 2026-05-05T08:00:00+08:00 | 多 Agent test-time scaling 的收益必须落在 token-cost/accuracy Pareto 前沿而非只看准确率；2+2+1=5 | 标准完成 | 已有覆盖：`AGENT-MULTI-AGENT` / [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；逐命题比较已完成并通过独立复核 |
| [Feedback-Normalized Developer Memory for Reinforcement-Learning Coding Agents: A Safety-Gated MCP Architecture](https://arxiv.org/html/2605.01567v1) | 2026-05-05T08:00:00+08:00 | Developer memory selection 是带 propensity 与延迟反馈的控制决策；确定性策略持有生产权，学习策略只能在 shadow/OPE gate 后进入 canary。；3+2+3=8 | 深入完成 | 已有覆盖：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)；逐命题比较已完成并通过独立复核 |
| [Evaluating Agentic AI in the Wild: Failure Modes, Drift Patterns, and a Production Evaluation Framework](https://arxiv.org/html/2605.01604v1) | 2026-05-05T08:00:00+08:00 | 生产 Agent 的 compounding error、tool cascade 与 temporal drift 要用连续、分布感知、跨信号的评测状态，而非一次 episodic score。；3+2+2=7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [Concepts Whisper While Syntax Shouts: Spectral Anti-Concentration and the Dual Geometry of Transformer Representations](https://arxiv.org/html/2605.01609v1) | 2026-05-05T08:00:00+08:00 | 以谱能量与 whitened causal alignment 区分稀疏概念方向和高能 syntax 结构，反证只看方差的解释；2+1+2=5 | 标准完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；逐命题比较已完成并通过独立复核 |
| [Prescriptive Scaling Laws for Data Constrained Training](https://arxiv.org/html/2605.01640v1) | 2026-05-05T08:00:00+08:00 | data cap 下的 scaling law 把新增算力重新分配到数据质量、重复与模型规模；3+2+2=7 | 深入完成 | 已有覆盖：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；逐命题比较已完成并通过独立复核 |
| [Adaptive Pluralistic Alignment: A pipeline for dynamic artificial democracy](https://arxiv.org/html/2605.01642v1) | 2026-05-05T08:00:00+08:00 | 把人群偏好分解为低秩 reward basis，经民主过滤形成 jury，再随时间更新群体权重与策略；3+3+2=8 | 深入完成 | 整合：`TRAIN-RLHF` / [Ch31](../../../../books/part-04-training-system/31-rlhf.md) 正文 marker 已回读并通过独立复核 |
| [AI Alignment via Incentives and Correction](https://arxiv.org/html/2605.01643v1) | 2026-05-05T08:00:00+08:00 | solver 与 auditor 的联合纠错事件使 reward design 成为保持监督激励的双层控制问题；2+2+1=5 | 深入完成 | 整合：`TRAIN-RLHF` / [Ch31](../../../../books/part-04-training-system/31-rlhf.md) 正文 marker 已回读并通过独立复核 |
| [Toward a Principled Framework for Agent Safety Measurement](https://arxiv.org/html/2605.01644v1) | 2026-05-05T08:00:00+08:00 | Agent safety measurement 必须覆盖策略搜索空间而不是只测固定输出样本；2+2+2=6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [SteeringDiffusion: A Bottlenecked Activation Control Interface for Diffusion Models](https://arxiv.org/html/2605.01653v1) | 2026-05-05T08:00:00+08:00 | 以瓶颈 activation adapter 在 diffusion 运行时注入方向控制，形成不改主权重的控制接口；2+2+2=6 | 标准完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；逐命题比较已完成并通过独立复核 |
| [Act2See: Emergent Active Visual Perception for Video Reasoning](https://arxiv.org/html/2605.01657v1) | 2026-05-05T08:00:00+08:00 | VLM 在推理中主动决定检索或生成视觉证据，使 context acquisition 成为显式动作；2+1+2=5 | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；逐命题比较已完成并通过独立复核 |
| [Video Active Perception: Effective Inference-Time Long-Form Video Understanding with Vision-Language Models](https://arxiv.org/html/2605.01662v1) | 2026-05-05T08:00:00+08:00 | 长视频推理将 keyframe selection 建模为基于生成先验的 inference-time data acquisition；2+1+2=5 | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；逐命题比较已完成并通过独立复核 |
| [CP-SynC: Multi-Agent Zero-Shot Constraint Modeling in MiniZinc with Synthesized Checkers](https://arxiv.org/html/2605.01675v1) | 2026-05-05T08:00:00+08:00 | 并行生成候选约束程序并综合可执行 checker 证据，将 verifier 变为最终选择 authority；2+2+1=5 | 标准完成 | 已有覆盖：`AGENT-MULTI-AGENT` / [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；逐命题比较已完成并通过独立复核 |
| [GRAVITY: Architecture-Agnostic Structured Anchoring for Long-Horizon Conversational Memory](https://arxiv.org/html/2605.01688v1) | 2026-05-05T08:00:00+08:00 | retrieved evidence 与 generation-time relational/temporal/thematic anchors 是两层状态；结构化派生视图不能替代原始 memory provenance。；3+2+2=7 | 深入完成 | 已有覆盖：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)；逐命题比较已完成并通过独立复核 |
| [Latent State Design for World Models under Sufficiency Constraints](https://arxiv.org/html/2605.01694v1) | 2026-05-05T08:00:00+08:00 | world-model latent state 以任务充分性而非重建完整 observation 作为设计约束；2+2+1=5 | 标准完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；逐命题比较已完成并通过独立复核 |
| [Probe-Geometry Alignment: Erasing the Cross-Sequence Memorization Signature Below Chance](https://arxiv.org/html/2605.01699v1) | 2026-05-05T08:00:00+08:00 | 跨序列 probe 揭示 unlearning 后可恢复的表示痕迹，并用逐层 rank-one intervention 擦除；2+2+1=5 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；逐命题比较已完成并通过独立复核 |
| [The Reasoning Trap: An Information-Theoretic Bound on Closed-System Multi-Step LLM Reasoning](https://arxiv.org/html/2605.01704v1) | 2026-05-05T08:00:00+08:00 | closed-system 多步推理存在信息边界，外部 evidence 改变可恢复性而非单纯增加思考 token；2+2+2=6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [SplitZip: Ultra Fast Lossless KV Compression for Disaggregated LLM Serving](https://arxiv.org/html/2605.01708v1) | 2026-05-05T08:00:00+08:00 | bit-exact KV transfer compression 在 PD 拆分中压缩传输而不改变 decode 状态；3+3+2=8 | 深入完成 | 已有覆盖：`INFER-PD-DISAGGREGATION` / [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md)；逐命题比较已完成并通过独立复核 |
| [Model Routing as a Trust Problem: Route Receipts for Adaptive AI Systems](https://arxiv.org/html/2605.01710v1) | 2026-05-05T08:00:00+08:00 | 为动态模型路由生成 route receipt，记录候选、策略版本、约束、选择结果与可披露 provenance；3+3+3=9 | 深入完成 | 整合：`PLATFORM-TRACE` / [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) 正文 marker 已回读并通过独立复核 |
| [Motion-Aware Caching for Efficient Autoregressive Video Generation](https://arxiv.org/html/2605.01725v1) | 2026-05-05T08:00:00+08:00 | 按 token 运动强度动态决定视频生成 cache 更新频率，显式控制复用误差累积；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 正文 marker 已回读并通过独立复核 |
| [EGAD: Entropy-Guided Adaptive Distillation for Token-Level Knowledge Transfer](https://arxiv.org/html/2605.01732v1) | 2026-05-05T08:00:00+08:00 | 按教师 entropy 调整 curriculum、temperature 与蒸馏路径，使 token-level transfer 随不确定性变化；2+2+2=6 | 标准完成 | 已有覆盖：`TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md)；逐命题比较已完成并通过独立复核 |
| [GEASS: Gated Evidence-Adaptive Selective Caption Trust for Vision-Language Models](https://arxiv.org/html/2605.01733v1) | 2026-05-05T08:00:00+08:00 | 并行执行图像直答与 caption 辅助路径，以 confidence gate、information gain 和证据权重融合，限制错误 caption 锚定；3+2+2=7 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 正文 marker 已回读并通过独立复核 |
| [Architectural Obsolescence of Unhardened Agentic-AI Runtimes](https://arxiv.org/html/2605.01740v1) | 2026-05-05T08:00:00+08:00 | biconditional gate、hash-chain audit、egress guard 与 signing root 共同绑定 Agent action 与审计记录；3+3+2=8 | 深入完成 | 整合：`AGENT-PLATFORM` / [Ch84](../../../../books/part-07-agent/84-agent-platform.md) 正文 marker 已回读并通过独立复核 |
| [Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality](https://arxiv.org/html/2605.01749v1) | 2026-05-05T08:00:00+08:00 | 把长答案生成拆成 calibrated exploration 与 selective commitment，只将达到可靠性门槛的推理投影为最终 claim；3+3+2=8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 正文 marker 已回读并通过独立复核 |
| [Talk is Cheap, Communication is Hard: Dynamic Grounding Failures and Repair in Multi-Agent Negotiation](https://arxiv.org/html/2605.01750v1) | 2026-05-05T08:00:00+08:00 | 多 Agent 协商失败来自共享 grounding 动态漂移，并需要显式 repair 而非增加消息；2+2+1=5 | 标准完成 | 已有覆盖：`AGENT-MULTI-AGENT` / [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；逐命题比较已完成并通过独立复核 |
| [Catching the Infection Before It Spreads: Foresight-Guided Defense in Multi-Agent Systems](https://arxiv.org/html/2605.01758v1) | 2026-05-05T08:00:00+08:00 | 多 Agent 感染防御应跟踪局部传播状态并按新近/长期感染选择 rollback 或递归定位，而不是用全局 cure factor 覆盖检索分布。；3+3+2=8 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；逐命题比较已完成并通过独立复核 |
| [TrajShield: Trajectory-Level Safety Mediation for Defending Text-to-Video Models Against Jailbreak Attacks](https://arxiv.org/html/2605.01761v1) | 2026-05-05T08:00:00+08:00 | 把文本到视频安全从 prompt 词面过滤提升为生成轨迹上的因果风险定位与最小改写；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；逐命题比较已完成并通过独立复核 |
| [Mitigating Multimodal LLMs Hallucinations via Relevance Propagation at Inference Time](https://arxiv.org/html/2605.01766v1) | 2026-05-05T08:00:00+08:00 | 以逐 token 梯度更新直接修改 K/V 分支状态，并用 KL 约束分布漂移；3+2+2=7 | 深入完成 | 已有覆盖：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；逐命题比较已完成并通过独立复核 |
| [The Compliance Gap: Why AI Systems Promise to Follow Process Instructions but Don't](https://arxiv.org/html/2605.01771v1) | 2026-05-05T08:00:00+08:00 | 区分结果合规与过程合规，要求工具调用、检索与中间动作日志证明系统实际遵循了指定过程；3+3+2=8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 正文 marker 已回读并通过独立复核 |
| [Anticipation-VLA: Solving Long-Horizon Embodied Tasks via Anticipation-based Subgoal Generation](https://arxiv.org/html/2605.01772v1) | 2026-05-05T08:00:00+08:00 | 用可随环境状态递归细化、弹出和回退的 subgoal stack 连接高层 anticipation model 与低层 goal-conditioned VLA policy。；3+3+2=8 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 正文 marker 已回读并通过独立复核 |
| [Needle-in-RAG: Prompt-Conditioned Character-Level Traceback of Poisoned Spans in Retrieved Evidence](https://arxiv.org/html/2605.01782v1) | 2026-05-05T08:00:00+08:00 | 先记录 misgeneration 与检索事件，再以 counterfactual deletion 回溯到字符级 poisoned span，并把 span provenance 返回修复环；3+3+2=8 | 深入完成 | 整合：`AGENT-RAG` / [Ch76](../../../../books/part-07-agent/76-rag.md) 正文 marker 已回读并通过独立复核 |
| [DataEvolver: Let Your Data Build and Improve Itself via Goal-Driven Loop Agents](https://arxiv.org/html/2605.01789v1) | 2026-05-05T08:00:00+08:00 | 用 goal、artifact、critic、correction 和 acceptance 的双环构建可控视觉训练数据；2+2+2=6 | 标准完成 | 已有覆盖：`TRAIN-DATA` / [Ch27](../../../../books/part-04-training-system/27-data.md)；逐命题比较已完成并通过独立复核 |
| [Khala: Scaling Acoustic Token Language Models Toward High-Fidelity Music Generation](https://arxiv.org/html/2605.01790v1) | 2026-05-05T08:00:00+08:00 | 在统一 acoustic-token hierarchy 中分层生成结构与细节，并以固定步数并行补全细粒度 token；2+2+1=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 正文 marker 已回读并通过独立复核 |
| [Embody4D: A Generalist Data Engine for Embodied 4D World Modeling](https://arxiv.org/html/2605.01799v1) | 2026-05-05T08:00:00+08:00 | 把单目机器人视频转换为可变视角视频，并以 latent confidence 在 copy、repair 与 inpaint expert 之间路由，作为 embodied 4D 数据引擎。；2+2+2=6 | 标准完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；逐命题比较已完成并通过独立复核 |
| [Selector-Guided Autonomous Curriculum for One-Shot Reinforcement Learning from Verifiable Rewards](https://arxiv.org/html/2605.01823v1) | 2026-05-05T08:00:00+08:00 | 用成功率、输出分歧与难度学习选择 RLVR 样本，替代 reward variance 单启发式 curriculum；2+2+1=5 | 深入完成 | 整合：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md) 正文 marker 已回读并通过独立复核 |
| [nvPAX: Constrained Optimization for Dynamic Power Allocation in Hierarchical and Multi-Tenant Systems](https://arxiv.org/html/2605.01837v1) | 2026-05-05T08:00:00+08:00 | 在层级供电与多租户合同下用逐控制周期可行优化分配 GPU power budget；3+3+2=8 | 深入完成 | 整合：`PLATFORM-GPU-SCHEDULER` / [Ch63](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md) 正文 marker 已回读并通过独立复核 |
| [The Cylindrical Representation Hypothesis for Language Model Steering](https://arxiv.org/html/2605.01844v1) | 2026-05-05T08:00:00+08:00 | 以圆柱几何解释同一 steering 方向在不同样本相位下产生不稳定效果，并给出敏感扇区；2+1+2=5 | 标准完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；逐命题比较已完成并通过独立复核 |
| [NeuroState-Bench: A Human-Calibrated Benchmark for Commitment Integrity in LLM Agent Profiles](https://arxiv.org/html/2605.01847v1) | 2026-05-05T08:00:00+08:00 | Agent profile 的 task outcome 与 commitment integrity 必须分轴验收；最终答对不能证明承诺、偏好或状态约束被持续遵守。；3+2+2=7 | 深入完成 | 已有覆盖：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)；逐命题比较已完成并通过独立复核 |
| [Decouple and Cache: KV Cache Construction for Streaming Video Understanding](https://arxiv.org/html/2605.01858v1) | 2026-05-05T08:00:00+08:00 | 流式视频把 KV 构建与帧到达解耦，避免每次更新重算全部视觉历史；3+2+2=7 | 深入完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；逐命题比较已完成并通过独立复核 |
| [Divide and Conquer: Decoupled Representation Alignment for Multimodal World Models](https://arxiv.org/html/2605.01896v1) | 2026-05-05T08:00:00+08:00 | 从 diffusion 中间表示分离 RGB/depth/mask 的模态特征，分别对齐 DINO、Depth 与 segmentation experts，并用 decoupling regularizer 保持互补。；2+2+2=6 | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；逐命题比较已完成并通过独立复核 |
| [Disentangling Intent from Role: Adversarial Self-Play for Persona-Invariant Safety Alignment](https://arxiv.org/html/2605.01899v1) | 2026-05-05T08:00:00+08:00 | 用 persona lineage 的对抗自博弈产生攻击，再以 persona-invariant consistency 降低角色表面变化对安全判断的影响；2+2+2=6 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；逐命题比较已完成并通过独立复核 |
| [Stochastic Sparse Attention for Memory-Bound Inference](https://arxiv.org/html/2605.01910v1) | 2026-05-05T08:00:00+08:00 | 随机稀疏选择用可控近似换取 memory-bound attention 的访问缩减；2+2+2=6 | 标准完成 | 已有覆盖：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；逐命题比较已完成并通过独立复核 |
| [RefusalGuard: Geometry-Preserving Fine-Tuning for Safety in LLMs](https://arxiv.org/html/2605.01913v1) | 2026-05-05T08:00:00+08:00 | 将 safety-relevant representation drift 转化为 fine-tuning update 的显式约束与发布传感器；3+2+2=7 | 深入完成 | 整合：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 正文 marker 已回读并通过独立复核 |
| [A Language for Describing Agentic LLM Contexts](https://arxiv.org/html/2605.01920v1) | 2026-05-05T08:00:00+08:00 | 用可描述的 context schema 标注 Agent 所见信息、来源和作用域；2+2+1=5 | 标准完成 | 已有覆盖：`AGENT-CONTEXT` / [Ch75](../../../../books/part-07-agent/75-context.md)；逐命题比较已完成并通过独立复核 |
| [Training Non-Differentiable Networks via Optimal Transport](https://arxiv.org/html/2605.01928v1) | 2026-05-05T08:00:00+08:00 | 对含离散跳变的网络以固定分辨率 stationarity 和 forward-only transport step 替代不存在的梯度；2+2+1=5 | 深入完成 | 整合：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md) 正文 marker 已回读并通过独立复核 |
| [Exploring Data-Free LoRA Transferability for Video Diffusion Models](https://arxiv.org/html/2605.01929v1) | 2026-05-05T08:00:00+08:00 | 在无目标数据时按谱刚性聚类 LoRA，并仲裁 video-diffusion 变体间的 routing interference；3+2+2=7 | 深入完成 | 整合：`TRAIN-LORA` / [Ch30](../../../../books/part-04-training-system/30-lora.md) 正文 marker 已回读并通过独立复核 |
| [GPU Fingerprinting for Location Verification](https://arxiv.org/html/2605.01930v1) | 2026-05-05T08:00:00+08:00 | 用硬件物理 fingerprint 替代可被提取的片上密钥以绑定 GPU location identity；3+3+2=8 | 深入完成 | 整合：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 正文 marker 已回读并通过独立复核 |
| [Pandora's Regret: A Proper Scoring Rule for Evaluating Sequential Search](https://arxiv.org/html/2605.01936v1) | 2026-05-05T08:00:00+08:00 | 从顺序搜索成本导出同时约束概率校准与竞争项排序的 proper scoring rule；2+2+1=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 正文 marker 已回读并通过独立复核 |
| [Cross-Layer Energy Analysis of Multimodal Training on Grace Hopper Superchips](https://arxiv.org/html/2605.01938v1) | 2026-05-05T08:00:00+08:00 | 跨层测量把 GH200 多模态训练的能耗归因到数据移动而非只归因 FLOPs；2+2+1=5 | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；逐命题比较已完成并通过独立复核 |
| [Phone2Act: A Low-Cost, Hardware-Agnostic Teleoperation System for Scalable VLA Data Collection](https://arxiv.org/html/2605.01948v1) | 2026-05-05T08:00:00+08:00 | 用手机 6-DoF pose、可替换 ROS 2 bridge 与同步 recorder 把 teleoperation 控制和特定机器人硬件解耦，并直接产出 LeRobot 格式的 VLA 训练记录。；2+2+2=6 | 标准完成 | 已有覆盖：`TRAIN-DATA` / [Ch27](../../../../books/part-04-training-system/27-data.md)；逐命题比较已完成并通过独立复核 |
| [TRAP: Tail-aware Ranking Attack for World-Model Planning](https://arxiv.org/html/2605.01950v1) | 2026-05-05T08:00:00+08:00 | tail-aware ranking attack 表明 world-model planner 的候选轨迹排序本身是攻击面；2+2+1=5 | 标准完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；逐命题比较已完成并通过独立复核 |
| [Flexi-LoRA with Input-Adaptive Ranks: Efficient Finetuning for Speech and Reasoning Tasks](https://arxiv.org/html/2605.01959v1) | 2026-05-05T08:00:00+08:00 | 以输入条件 router 在训练和推理阶段选择 LoRA rank，令 adapter capacity 成为运行时状态；3+2+2=7 | 深入完成 | 整合：`TRAIN-LORA` / [Ch30](../../../../books/part-04-training-system/30-lora.md) 正文 marker 已回读并通过独立复核 |
| [Trojan Hippo: Weaponizing Agent Memory for Data Exfiltration](https://arxiv.org/html/2605.01970v1) | 2026-05-05T08:00:00+08:00 | 恶意内容可写入持久 Agent memory，并在后续会话恢复时触发数据外泄；3+3+2=8 | 深入完成 | 已有覆盖：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)；逐命题比较已完成并通过独立复核 |
| [DBLP: Phase-Aware Bounded-Loss Transport for Burst-Resilient Distributed ML Training](https://arxiv.org/html/2605.01989v1) | 2026-05-05T08:00:00+08:00 | 按训练 phase 与 loss budget 选择有损/可靠传输 fallback，而非统一可靠协议；2+2+2=6 | 标准完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)；逐命题比较已完成并通过独立复核 |
| [Counting as a minimal probe of language model reliability](https://arxiv.org/html/2605.02028v1) | 2026-05-05T08:00:00+08:00 | extended rule following 暴露模型对有限内部规则状态的持续更新失败；2+2+1=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [VILAS: A VLA-Integrated Low-cost Architecture with Soft Grasping for Robotic Manipulation](https://arxiv.org/html/2605.02037v1) | 2026-05-05T08:00:00+08:00 | 以模块化硬件、统一采集/部署数据流和一致 demonstrations 暴露 VLA 的真实部署边界；2+1+2=5 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；逐命题比较已完成并通过独立复核 |
| [What Single-Prompt Accuracy Misses: A Multi-Variant Reliability Audit of Language Models](https://arxiv.org/html/2605.02038v1) | 2026-05-05T08:00:00+08:00 | 同一任务的 prompt variants 揭示单提示 accuracy 无法度量服务可靠性；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [Bringing Order to Asynchronous SGD: Towards Optimality under Data-Dependent Delays with Momentum](https://arxiv.org/html/2605.02043v1) | 2026-05-05T08:00:00+08:00 | 异步 SGD 的 data-dependent delay 与 momentum 必须联合校正才能保持更新语义；2+2+1=5 | 标准完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)；逐命题比较已完成并通过独立复核 |
| [Principles and Guidelines for Randomized Controlled Trials in AI Evaluation](https://arxiv.org/html/2605.02050v1) | 2026-05-05T08:00:00+08:00 | AI uplift/RCT 结论必须显式冻结 intervention、population、control、outcome、power、randomization 与可复算材料；行业惯例不能替代实验身份。；2+2+3=7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [EditPropBench: Measuring Factual Edit Propagation in Scientific Manuscripts](https://arxiv.org/html/2605.02083v1) | 2026-05-05T08:00:00+08:00 | 用显式 fact graph 检查局部事实修改是否传播到依赖叙述，形成 cascade-aware artifact gate；2+2+1=5 | 深入完成 | 整合：`AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md) 正文 marker 已回读并通过独立复核 |
| [Model Spec Midtraining: Improving How Alignment Training Generalizes](https://arxiv.org/html/2605.02087v1) | 2026-05-05T08:00:00+08:00 | 把行为 spec 注入 midtraining，改变 alignment generalization 的训练阶段 owner；2+2+1=5 | 标准完成 | 已有覆盖：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；逐命题比较已完成并通过独立复核 |
| [Sharpness-Aware Pretraining Mitigates Catastrophic Forgetting](https://arxiv.org/html/2605.02105v1) | 2026-05-05T08:00:00+08:00 | sharpness-aware pretraining 改变后续适配时 catastrophic forgetting 的初始几何条件；2+2+1=5 | 标准完成 | 已有覆盖：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；逐命题比较已完成并通过独立复核 |
| [The Dynamic Gist-Based Memory Model (DGMM): A Memory-Centric Architecture for Artificial Intelligence](https://arxiv.org/html/2605.02106v1) | 2026-05-05T08:00:00+08:00 | 把带时间、来源与交互上下文的 episodic-semantic graph 设为可追加持久 memory owner；2+2+1=5 | 深入完成 | 整合：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md) 正文 marker 已回读并通过独立复核 |
| [STABLEVAL: Disagreement-Aware and Stable Evaluation of AI Systems](https://arxiv.org/html/2605.02122v1) | 2026-05-05T08:00:00+08:00 | Human-evaluation aggregation must preserve annotator uncertainty and ranking stability; majority vote is not a sufficient release-grade evaluation contract.；3+3+2=8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [Boundary Mass and the Soft-to-Hard Limit in Mixture-of-Experts](https://arxiv.org/html/2605.02124v1) | 2026-05-05T08:00:00+08:00 | soft routing 训练到 hard dispatch 的边界质量由 routing mass 演化而非只由 top-k 决定；2+2+1=5 | 标准完成 | 已有覆盖：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；逐命题比较已完成并通过独立复核 |
| [FedQueue: Queue-Aware Federated Learning for Cross-Facility HPC Training](https://arxiv.org/html/2605.02125v1) | 2026-05-05T08:00:00+08:00 | Cross-facility training must account for queue delay and allocation availability, not optimize communication or convergence after resources are assumed present.；3+3+3=9 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) 正文 marker 已回读并通过独立复核 |
| [Video Generation with Predictive Latents](https://arxiv.org/html/2605.02134v1) | 2026-05-05T08:00:00+08:00 | predictive latents 让视频生成表示承担未来状态预测而非只重建当前像素；2+1+2=5 | 标准完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；逐命题比较已完成并通过独立复核 |
| [Projection-Free Transformers via Gaussian Kernel Attention](https://arxiv.org/html/2605.02144v1) | 2026-05-05T08:00:00+08:00 | 用原始 hidden-state 间 Gaussian kernel 直接构造 row-stochastic attention，移除 Q/K 投影并以 bandwidth 控制局部性；3+3+2=8 | 深入完成 | 整合：`MODEL-SELF-ATTENTION` / [Ch14](../../../../books/part-02-model/14-self-attention.md) 正文 marker 已回读并通过独立复核 |
| [SpecEdit: Training-Free Acceleration for Diffusion based Image Editing via Semantic Locking](https://arxiv.org/html/2605.02152v1) | 2026-05-05T08:00:00+08:00 | 先低分辨率生成 draft，以语义验证锁定稳定区域，仅对未锁定区域恢复高分辨率并继续计算；3+3+2=8 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 正文 marker 已回读并通过独立复核 |
| [AAFLOW: Scalable Patterns for Agentic AI Workflows](https://arxiv.org/html/2605.02162v1) | 2026-05-05T08:00:00+08:00 | 零拷贝数据流与可组合执行模式把 Agent workflow 从脚本升级为显式 runtime；2+2+1=5 | 标准完成 | 已有覆盖：`AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md)；逐命题比较已完成并通过独立复核 |
| [Planner Matters! An Efficient and Unbalanced Multi-agent Collaboration Framework for Long-horizon Planning](https://arxiv.org/html/2605.02168v1) | 2026-05-05T08:00:00+08:00 | Planner, actor and memory roles may own different compute budgets; the reported allocation is evidence for the tested planning workloads, not a universal multi-agent topology.；3+2+2=7 | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT` / [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；逐命题比较已完成并通过独立复核 |
| [T$^2$PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/html/2605.02178v1) | 2026-05-05T08:00:00+08:00 | 在 token 与 turn 两层跟踪 uncertainty progress，停滞时分别触发 thinking intervention 和 turn resampling，改变多轮 Agent RL 的 rollout admission。；3+3+2=8 | 深入完成 | 整合：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md) 正文 marker 已回读并通过独立复核 |
| [Risk-Budgeted Online Scheduling for Continuous Edge Inference over Evolving Time Horizons](https://arxiv.org/html/2605.02179v1) | 2026-05-05T08:00:00+08:00 | Continuous edge inference must carry deadline-violation risk and burst history across time; the AEGIS policy is bounded to its prediction and risk-budget assumptions.；3+3+3=9 | 深入完成 | 整合：`INFER-SCHEDULING` / [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) 正文 marker 已回读并通过独立复核 |
| [When Alignment Isn’t Enough: Response-Path Attacks on LLM Agents](https://arxiv.org/html/2605.02187v1) | 2026-05-05T08:00:00+08:00 | BYOK response relay 可静默篡改，provider-signed envelope 才能绑定响应 provenance；3+3+2=8 | 深入完成 | 整合：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 正文 marker 已回读并通过独立复核 |
| [PipeMax: Enhancing Offline LLM Inference on Commodity GPU Servers](https://arxiv.org/html/2605.02189v1) | 2026-05-05T08:00:00+08:00 | commodity GPU 离线推理通过阶段 pipeline 重排内存与计算，而非照搬在线 serving；2+2+1=5 | 标准完成 | 已有覆盖：`INFER-SCHEDULING` / [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；逐命题比较已完成并通过独立复核 |
| [Beyond Translation Accuracy: Addressing False Failures in LLM-Based Code Translation](https://arxiv.org/html/2605.02195v1) | 2026-05-05T08:00:00+08:00 | Compiler flags, libraries, runtime configuration and test harness are part of code-agent evaluation identity because pipeline faults can create false model failures.；3+3+3=9 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [DurableUn: Quantization-Induced Recovery Attacks in Machine Unlearning](https://arxiv.org/pdf/2605.02196v1) | 2026-05-05T08:00:00+08:00 | 揭示低精度量化可重新暴露已 unlearn 的内容，使 precision 成为遗忘验收与部署 artifact 身份的一部分；3+3+2=8 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有正文已绑定最终部署精度、量化器、artifact identity 与 retained utility，已通过独立复核 |
| [MEMAUDIT: An Exact Package-Oracle Evaluation Protocol for Budgeted Long-Term LLM Memory Writing](https://arxiv.org/html/2605.02199v1) | 2026-05-05T08:00:00+08:00 | Long-term memory writing needs an exact budgeted package oracle that measures write admission separately from answer generation.；3+2+3=8 | 深入完成 | 已有覆盖：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)；逐命题比较已完成并通过独立复核 |
| [Metric Unreliability in Multimodal Machine Unlearning: A Systematic Analysis and Principled Unified Score](https://arxiv.org/pdf/2605.02206v1) | 2026-05-05T08:00:00+08:00 | 多模态 unlearning 指标可能给出相反排序；聚合分数必须冻结 oracle、校准样本与权重，且不能替代逐轴 verdict；2+2+2=6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；canonical owner 已由表示章节纠正为评测系统，已通过独立复核 |
| [Submodular Benchmark Selection](https://arxiv.org/html/2605.02209v1) | 2026-05-05T08:00:00+08:00 | Benchmark subset admission must state the covariance/information model, budget and residual-coverage diagnostic; the selected subset cannot inherit full-suite authority outside those assump…；3+3+3=9 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [CoVSpec: Efficient Device-Edge Co-Inference for Vision-Language Models via Speculative Decoding](https://arxiv.org/html/2605.02218v1) | 2026-05-05T08:00:00+08:00 | device-edge VLM speculation 联合视觉 token pruning、adaptive draft 与通信 correction；2+1+2=5 | 标准完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING` / [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)；逐命题比较已完成并通过独立复核 |
| [Perturbation Dose Responses in Recursive LLM Loops: Raw Switching, Stochastic Floors, and Persistent Escape under Append, Replace, and Dialog Updates](https://arxiv.org/html/2605.02236v1) | 2026-05-05T08:00:00+08:00 | 递归 LLM loop 的持久逃逸由 append/replace/dialog memory policy 决定；2+2+1=5 | 标准完成 | 已有覆盖：`AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md)；逐命题比较已完成并通过独立复核 |
| [Zero-Shot Confidence Estimation for Small LLMs: When Supervised Baselines Aren't Worth Training](https://arxiv.org/html/2605.02241v1) | 2026-05-05T08:00:00+08:00 | 生成 log-probability 可作为小模型到云模型升级路由的零样本置信信号；2+2+1=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [On the Privacy of LLMs: An Ablation Study](https://arxiv.org/html/2605.02255v1) | 2026-05-05T08:00:00+08:00 | 统一威胁模型揭示 MIA、提取、属性推断与 backdoor 对模型/RAG 配置的依赖不同；2+2+1=5 | 标准完成 | 已有覆盖：`AGENT-RAG` / [Ch76](../../../../books/part-07-agent/76-rag.md)；逐命题比较已完成并通过独立复核 |
| [WindowQuant: Mixed-Precision KV Cache Quantization based on Window-Level Similarity for VLMs Inference Optimization](https://arxiv.org/html/2605.02262v1) | 2026-05-05T08:00:00+08:00 | 按视觉 token window 与文本 prompt 的相似度分配 KV bit-width，并通过 window 重排把搜索 artifact 编译为可执行 mixed-precision layout/kernel。；3+2+2=7 | 深入完成 | 已有覆盖：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；逐命题比较已完成并通过独立复核 |
| [Break the Block: Dynamic-size Reasoning Blocks for Diffusion Large Language Models via Monotonic Entropy Descent with Reinforcement Learning](https://arxiv.org/html/2605.02263v1) | 2026-05-05T08:00:00+08:00 | 用专用 block-end token、block entropy trajectory 与 RL reward 学习动态 reasoning block boundary，替代 diffusion LM 的固定 block size。；3+3+2=8 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 正文 marker 已回读并通过独立复核 |
| [Towards Understanding Specification Gaming in Reasoning Models](https://arxiv.org/html/2605.02269v1) | 2026-05-05T08:00:00+08:00 | 用可观察环境中的隐藏 hacking opportunity 分离任务成功与 specification gaming，并测量 RL 后行为变化；3+3+2=8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 正文 marker 已回读并通过独立复核 |
| [SOTOPIA-TOM: Evaluating Information Management in Multi-Agent Interaction with Theory of Mind](https://arxiv.org/html/2605.02307v1) | 2026-05-05T08:00:00+08:00 | 多 Agent 的 public/private channel、partitioned knowledge 与 disclosure policy 必须进入共享状态和评测身份；终局成功不能掩盖隐私泄漏或缺失信息请求。；3+2+2=7 | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT` / [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；逐命题比较已完成并通过独立复核 |
| [When Attention Collapses: Residual Evidence Modeling for Compositional Inference](https://arxiv.org/html/2605.02323v1) | 2026-05-05T08:00:00+08:00 | 用逐 slot residual-evidence state 记录尚未解释的输入容量，抑制 additive mixture 中的重复 attention allocation；3+2+2=7 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 正文 marker 已回读并通过独立复核 |
| [Taming Request Imbalance: SLO-Aware Scheduling for Disaggregated LLM Inference](https://arxiv.org/html/2605.02329v1) | 2026-05-05T08:00:00+08:00 | PD 两侧分别用 TTFT urgency 与 TPOT slack 控制长尾请求和 decode packing；3+3+2=8 | 深入完成 | 已有覆盖：`INFER-SCHEDULING` / [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；逐命题比较已完成并通过独立复核 |
| [When Correct Isn't Usable: Improving Structured Output Reliability in Small Language Models](https://arxiv.org/html/2605.02363v1) | 2026-05-05T08:00:00+08:00 | Semantic correctness and interface usability are separate gates; typed validation owns schema acceptance even when the answer content is correct.；3+3+2=8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [InfoLaw: Information Scaling Laws for Large Language Models with Quality-Weighted Mixture Data and Repetition](https://arxiv.org/html/2605.02364v1) | 2026-05-05T08:00:00+08:00 | quality-weighted mixture 与 repetition 改写固定 token-count 数据 scaling 判断；2+2+2=6 | 标准完成 | 已有覆盖：`TRAIN-DATA` / [Ch27](../../../../books/part-04-training-system/27-data.md)；逐命题比较已完成并通过独立复核 |
| [Binary Rewards and Reinforcement Learning: Fundamental Challenges](https://arxiv.org/html/2605.02375v1) | 2026-05-05T08:00:00+08:00 | binary verifier 只定义 valid support；KL 方向与模型族 misspecification 会把更高 validity 的压力转化为 mode collapse；2+2+2=6 | 深入完成 | 整合 Applied：`TRAIN-RLHF` / [Ch31](../../../../books/part-04-training-system/31-rlhf.md)；待 fresh non-author 最小范围复核 |
| [Differentially Private Runtime Monitoring](https://arxiv.org/html/2605.02391v1) | 2026-05-05T08:00:00+08:00 | The exact-v1 result covers event-level adjacency, temporal sensitivity analysis, privacy-barrier placement, noisy output streams and composition/tree aggregation. Downstream alert semantics…；3+2+3=8 | 深入完成 | 整合：`PLATFORM-MONITORING` / [Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md) 正文 marker 已回读并通过独立复核 |
| [Controllable and Verifiable Process Data Synthesis for Process Reward Models](https://arxiv.org/html/2605.02395v1) | 2026-05-05T08:00:00+08:00 | PRM 监督必须标注第一处 prefix 不再支持的步骤，而非只给终局或逐步表面标签；2+1+2=5 | 标准完成 | 已有覆盖：`TRAIN-RLHF` / [Ch31](../../../../books/part-04-training-system/31-rlhf.md)；逐命题比较已完成并通过独立复核 |
| [The Compliance Trap: How Structural Constraints Degrade Frontier AI Metacognition Under Adversarial Pressure](https://arxiv.org/html/2605.02398v1) | 2026-05-05T08:00:00+08:00 | 显示强制格式与合规措辞会在压力下压低模型元认知表达，要求把结构约束本身作为评测干预变量；3+2+2=7 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 正文 marker 已回读并通过独立复核 |
| [Statistically-Lossless Quantization of Large Language Models](https://arxiv.org/html/2605.02404v1) | 2026-05-05T08:00:00+08:00 | 用 next-token distribution agreement 区分 task-lossless 与 distribution-lossless quantization；3+3+2=8 | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；逐命题比较已完成并通过独立复核 |
| [FitText: Evolving Agent Tool Ecologies via Memetic Retrieval](https://arxiv.org/html/2605.02411v1) | 2026-05-05T08:00:00+08:00 | 把 tool shortlist 从初始 query 的一次静态结果变成执行中可修订的 action-space state，通过伪 tool 描述、并行探索和 tool memory 反复检索。；3+2+2=7 | 深入完成 | 整合：`AGENT-TOOL-CALLING` / [Ch78](../../../../books/part-07-agent/78-tool-calling.md) 正文 marker 已回读并通过独立复核 |
| [Measuring AI Reasoning: A Guide for Researchers](https://arxiv.org/html/2605.02442v1) | 2026-05-05T08:00:00+08:00 | 把 reasoning evaluation 从答案正确率扩展到 contamination、search complexity、外显过程与不可见 latent reasoning 的证据边界；2+2+2=6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [Reference-Sampled Boltzmann Projection for KL-Regularized RLVR: Target-Matched Weighted SFT, Finite One-Shot Gaps, and Policy Mirror Descent](https://arxiv.org/html/2605.02469v1) | 2026-05-05T08:00:00+08:00 | 证明固定 reference 下 KL-regularized RLVR 可投影为 reference-sampled weighted SFT，并显式给出 support、ESS 与 one-shot gap；3+3+3=9 | 深入完成 | 整合：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md) 正文 marker 已回读并通过独立复核 |
| [Efficient Preference Poisoning Attack on Offline RLHF](https://arxiv.org/html/2605.02495v1) | 2026-05-05T08:00:00+08:00 | offline preference dataset 的少量污染可定向改变 RLHF policy，数据 provenance 成为安全边界；2+2+2=6 | 标准完成 | 已有覆盖：`TRAIN-RLHF` / [Ch31](../../../../books/part-04-training-system/31-rlhf.md)；逐命题比较已完成并通过独立复核 |
| [A Semantic Autonomy Framework for VLM-Integrated Indoor Mobile Robots: Hybrid Deterministic Reasoning and Cross-Robot Adaptive Memory](https://arxiv.org/html/2605.02525v1) | 2026-05-05T08:00:00+08:00 | 以 deterministic resolver 处理稳定语义，只有歧义请求升级到 VLM，并把验证后的偏好按 global/operator/robot scope 提升为跨会话、跨机器人 memory digest。；3+2+2=7 | 深入完成 | 已有覆盖：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)；逐命题比较已完成并通过独立复核 |
| [StreamIndex: Memory-Bounded Compressed Sparse Attention via Streaming Top-k](https://arxiv.org/html/2605.02568v1) | 2026-05-05T08:00:00+08:00 | chunked partition-merge top-k 避免物化完整稀疏 attention score tensor；2+2+2=6 | 标准完成 | 已有覆盖：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；逐命题比较已完成并通过独立复核 |
| [On Training Large Language Models for Long-Horizon Tasks: An Empirical Study of Horizon Length](https://arxiv.org/html/2605.02572v1) | 2026-05-05T08:00:00+08:00 | 只增加 interaction horizon 就会恶化探索与 credit assignment，horizon reduction 可稳定训练；2+2+1=5 | 标准完成 | 已有覆盖：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；逐命题比较已完成并通过独立复核 |
| [Beyond State Machines: Executing Network Procedures with Agentic Tool-Calling Sequences](https://arxiv.org/html/2605.02584v1) | 2026-05-05T08:00:00+08:00 | Strict procedures should move from repeated model decisions into deterministic tool/workflow ownership once action order and invariants are known.；3+2+2=7 | 深入完成 | 已有覆盖：`AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md)；逐命题比较已完成并通过独立复核 |
| [Gradient-Gated DPO: Stabilizing Preference Optimization in Language Models](https://arxiv.org/html/2605.02626v1) | 2026-05-05T08:00:00+08:00 | Gate-DPO modulates rejected-gradient magnitude using response probability geometry to reduce squeezing in very low-probability regions; it does not establish a gradient-conflict or noisy-pa…；3+2+3=8 | 深入完成 | 整合：`TRAIN-DPO` / [Ch34](../../../../books/part-04-training-system/34-dpo.md) 正文 marker 已回读并通过独立复核 |
| [Mamoda2.5: Enhancing Unified Multimodal Model with DiT-MoE](https://arxiv.org/html/2605.02641v1) | 2026-05-05T08:00:00+08:00 | 在统一 AR-Diffusion workload 中组合 DiT-MoE 条件计算、dense upcycling 与 few-step student；3+3+2=8 | 深入完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；逐命题比较已完成并通过独立复核 |
| [ContextualJailbreak: Evolutionary Red-Teaming via Simulated Conversational Priming](https://arxiv.org/html/2605.02647v1) | 2026-05-05T08:00:00+08:00 | 用多轮 conversational priming 的进化搜索生成上下文 jailbreak，并对 judge reliability 做独立约束；2+2+2=6 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；逐命题比较已完成并通过独立复核 |
| [Hybrid Inspection and Task-Based Access Control in Zero-Trust Agentic AI](https://arxiv.org/html/2605.02682v1) | 2026-05-05T08:00:00+08:00 | zero-trust interception 联合确定性完整性检查与 task-tool 语义授权；3+3+2=8 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；逐命题比较已完成并通过独立复核 |
| [Executor-Side Progressive Risk-Gated Actuation for Agentic AI in Wireless Supervisory Control](https://arxiv.org/html/2605.02697v1) | 2026-05-05T08:00:00+08:00 | executor 根据 expiry、telemetry freshness、rollback handle、冲突、前置条件、planner-executor risk divergence 与 evidence budget 原子选择 commit、gate 或 reject。；3+3+2=8 | 深入完成 | 已有覆盖：`AGENT-PLATFORM` / [Ch84](../../../../books/part-07-agent/84-agent-platform.md)；逐命题比较已完成并通过独立复核 |
| [Latent Bridge: Feature Delta Prediction for Efficient Dual-System Vision-Language-Action Model Inference](https://arxiv.org/html/2605.02739v1) | 2026-05-05T08:00:00+08:00 | 预测相邻 timestep 的 VLM feature delta，使低层 action head 可跳过部分 backbone 调用；2+1+2=5 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；逐命题比较已完成并通过独立复核 |
| [Mitigating Misalignment Contagion by Steering with Implicit Traits](https://arxiv.org/html/2605.02751v1) | 2026-05-05T08:00:00+08:00 | 多轮多 Agent 交互会传播反社会行为，重复 system prompt 不是稳定隔离手段；2+2+1=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [Seeing Realism from Simulation: Efficient Video Transfer for Vision-Language-Action Data Augmentation](https://arxiv.org/html/2605.02757v1) | 2026-05-05T08:00:00+08:00 | 把模拟 VLA 视频经 segmentation/caption 条件化 transfer 为逼真训练视频，用 diffusion feature reuse 降低生成成本并以 coreset 控制增强分母。；2+2+2=6 | 标准完成 | 已有覆盖：`TRAIN-DATA` / [Ch27](../../../../books/part-04-training-system/27-data.md)；逐命题比较已完成并通过独立复核 |
| [U-Define: Designing User Workflows for Hard and Soft Constraints in LLM-Based Planning](https://arxiv.org/html/2605.02765v1) | 2026-05-05T08:00:00+08:00 | 把用户约束分成 hard 与 soft：hard 交给形式 checker，soft 交给可校准 judge，并保留冲突解释与人工修改；3+3+2=8 | 深入完成 | 整合：`AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md) 正文 marker 已回读并通过独立复核 |
| [Autonomous LLM Agent Worms: Cross-Platform Propagation, Automated Discovery and Temporal Re-Entry Defense](https://arxiv.org/html/2605.02812v1) | 2026-05-05T08:00:00+08:00 | Agent worm 可跨平台发现、传播并借 temporal re-entry 恢复，单次清理不足；2+2+1=5 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；逐命题比较已完成并通过独立复核 |
| [When Is the Same Model Not the Same Service? A Measurement Study of Hosted Open-Weight LLM APIs](https://arxiv.org/html/2605.02821v1) | 2026-05-05T08:00:00+08:00 | 同名 open-weight model 在不同 provider/time 下应建模为可漂移 service object；2+2+1=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；逐命题比较已完成并通过独立复核 |
| [Trust, but Verify: Peeling Low-Bit Transformer Networks for Training Monitoring](https://arxiv.org/html/2605.02853v1) | 2026-05-05T08:00:00+08:00 | 逐层可达参考解揭示 aggregate training loss 隐藏的 under-optimized layer；2+2+1=5 | 标准完成 | 已有覆盖：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；逐命题比较已完成并通过独立复核 |
| [MolmoAct2: Action Reasoning Models for Real-world Deployment](https://arxiv.org/html/2605.02881v1) | 2026-05-05T08:00:00+08:00 | VLA 将空间 backbone、action tokenizer、continuous expert 与 adaptive-depth grounding 组合成部署闭环；3+2+2=7 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；逐命题比较已完成并通过独立复核 |
| [SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection](https://arxiv.org/html/2605.02888v1) | 2026-05-05T08:00:00+08:00 | speculation length 的最优值随 target compression 和逐步置信信号变化；2+2+1=5 | 标准完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING` / [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)；逐命题比较已完成并通过独立复核 |

## 4. 证据与知识整合

下列逐项说明是作者侧证据包的可读投影；完整 section evidence、Score rationale、owner 与 Books 判断保存在 [V3 Evidence Reviews](../_sources/daily-20260505/V3_EVIDENCE_REVIEWS.json)，128 个 No Change 的现有命题定位和逐命题差异见 [V3 Proposition Books Comparison](../_sources/daily-20260505/V3_PROPOSITION_BOOKS_COMPARISON.md)。既有 Applied 见 [既有 Books 写回记录](../_sources/daily-20260505/V3_BOOKS_REVIEW_QUEUE.md)，先前 18 项定点队列见 [已解决 root 队列](../_sources/daily-20260505/V3_TARGETED_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.md)；本轮唯一 Proposed 的精确增量、插入位置与边界见 [bounded-repair root 队列](../_sources/daily-20260505/V3_BOUNDED_REPAIR_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.md)。`深入完成（作者侧）`、URL 可访问或 marker 存在均不等于独立语义复核通过。

### [Separating Intelligence from Execution: A Workflow Engine for the Model Context Protocol](https://arxiv.org/html/2605.00827v1)

准入时需核验的设计变化是：以声明式 blueprint 和幂等执行器把 MCP 智能提议与工作流执行分开。exact-v1 的机制定位为 `Workflow Orchestration Systems.；Multi-Agent Frameworks.`，评价定位为 `4.2 Empirical Measurement`，限制或反证定位为 `6.6 Limitations；8 Conclusion`。

采用边界：机制锚点为 Workflow Orchestration Systems., Multi-Agent Frameworks.；评价锚点为 4.2 Empirical Measurement。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `AGENT-MCP` / [Ch83](../../../../books/part-07-agent/83-mcp.md)；现有命题：协议发现、能力身份、授权和真实 effect 必须分层验收；比较：现有命题已经规定：协议发现、能力身份、授权和真实 effect 必须分层验收。本来源的受限增量是“以声明式 blueprint 和幂等执行器把 MCP 智能提议与工作流执行分开”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [GhostServe: A Lightweight Checkpointing System in the Shadow for Fault-Tolerant LLM Serving](https://arxiv.org/html/2605.00831v1)

准入时需核验的设计变化是：用 host-memory erasure-coded shadow checkpoint 保护增长中的 KV 状态并支持故障恢复。exact-v1 的机制定位为 `4 Methodology；6.3 Performance Analysis`，评价定位为 `5 Implementation；6.1 Experimental Setup`，限制或反证定位为 `8 Discussion and Limitation；9 Conclusion`。

机制证据摘要：In this work, we propose a new lightweight checkpointing system, GhostServe, for distributed LLM serving based on the idea of erasure coding to address the fault-tolerance challenges outlined in Section 3 . The overview system architecture is shown in Figure 3 (a). Compared to naive replication-based checkpointing, GhostServe leverages erasure coding to generate parity shards for the KV cache at the granularity of a chunk (group of tokens). The parity shards are stored in host memory and retrieved when one or mult…

评价证据摘要：GhostServe is an end-to-end system implemented with 4K lines of Python and 1.5K lines of C++/CUDA. We use SGLang version 0.5.1 Zheng et al. (2024) as our backend and implement our method as a plug-in module. In practice, GhostServe can be integrated into existing serving engines such as vLLM Kwon et al. (2023) and HuggingFace-TGI Wolf et al. (2019) with minimal modifications, making it portable and easy to adopt. For the attention backend, we adopt FlashInfer version 0.3.1 Ye et al. (2025) , built on top of PyTorc…

限制证据摘要：Cross-node Scalability. GhostServe can be further extended to cross-node environments through hierarchical fault-tolerance coordination and bandwidth-aware parity placement. For inter-node redundancy, GhostServe can designate one or more parity coordinators that aggregate parity blocks across nodes using NCCL over InfiniBand or NIC. The challenge of providing node-level reliability lies in the bandwidth disparity be…

采用边界：机制锚点为 4 Methodology, 6.3 Performance Analysis；评价锚点为 5 Implementation, 6.1 Experimental Setup。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；现有命题：KV 离开可靠 HBM 或需要故障接管时，保护预算、checkpoint identity、恢复路径与 failover commit 必须显式化；比较：GhostServe 的 host-memory erasure-coded shadow checkpoint 是后台保护的具体实现；现有小节已经拥有可靠性分层、恢复/重算与状态身份，故不改变长期命题。 仍待非作者逐命题复核。最终处置已通过独立复核。

### [Synthetic Designed Experiments for Diagnosing Vision Model Failure](https://arxiv.org/html/2605.00832v1)

准入时需核验的设计变化是：把可控合成生成器当作实验装置，用因子设计区分 coverage gap 与 spurious dependency 并定向补数。exact-v1 的机制定位为 `Synthetic Designed Experiments for Diagnosing Vision Model Failures；Counterfactual and invariance-based methods.；3 Framework`，评价定位为 `Synthetic Designed Experiments for Diagnosing Vision Model Failures；3.1 Phase 1: Designed Experiment；Verification.`，限制或反证定位为 `Synthetic Designed Experiments for Diagnosing Vision Model Failures`。

采用边界：机制锚点为 Synthetic Designed Experiments for Diagnosing Vision Model Failures, Counterfactual and invariance-based methods., 3 Framework；评价锚点为 Synthetic Designed Experiments for Diagnosing Vision Model Failures, 3.1 Phase 1: Designed Experiment, Verification.。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“把可控合成生成器当作实验装置，用因子设计区分 coverage gap 与 spurious dependency 并定向补数”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [From Euler to Dormand-Prince: ODE Solvers for Flow Matching Generative Models](https://arxiv.org/html/2605.00836v1)

准入时需核验的设计变化是：把 flow-matching 采样器从固定 Euler 步进提升为可比较的高阶与自适应 ODE 求解器，并以 NFE-quality frontier 暴露模型误差与数值误差的共同上限。exact-v1 的机制定位为 `2 Mathematical Framework；2.2 From Taylor Expansion to Runge–Kutta Methods；Architecture.`，评价定位为 `3 Experimental Setup；4 Results；4.5 Ablations`，限制或反证定位为 `4.2 NFE–Quality Trade-off；6 Discussion；Limitations.`。

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `No Change — Existing Coverage (proposition comparison; independent review required)`，目标 owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；现有命题：本章已把 sampler、step schedule、误差控制和 NFE/质量前沿定义为生成执行合同，旧 Euler 在低预算与误差容忍场景仍成立；比较：exact-v1 的新增证据是“把 flow-matching 采样器从固定 Euler 步进提升为可比较的高阶与自适应 ODE 求解器，并以 NFE-quality frontier 暴露模型误差与数值误差的共同上限”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。最终处置已通过独立复核。

### [Understanding Emergent Misalignment via Feature Superposition Geometry](https://arxiv.org/html/2605.00842v1)

准入时需核验的设计变化是：非正交 superposition 使目标微调沿几何邻近方向产生 gradient spillover。exact-v1 的机制定位为 `Layer-wise analysis.；Training dynamics.；Training Data Properties Shape Model Behavior.`，评价定位为 `Layer-wise analysis.；Appendix B Toy model Experiment setup；Appendix F Evaluation Details`，限制或反证定位为 `4 Discussion；5 Conclusion；Limitations`。

机制证据摘要：We next examine the similarity between misalignment-inducing features and toxic features across layers of different models. As shown in Figure 6 , features derived from misalignment-inducing data consistently exhibit higher similarity to toxic features compared to features derived from normal data . This pattern holds across virtually all layers, indicating that the effect is robust to both model scale and dataset domain. Figure 7: Training dynamics of similarity between hidden states and SAE features correspondin…

评价证据摘要：We next examine the similarity between misalignment-inducing features and toxic features across layers of different models. As shown in Figure 6 , features derived from misalignment-inducing data consistently exhibit higher similarity to toxic features compared to features derived from normal data . This pattern holds across virtually all layers, indicating that the effect is robust to both model scale and dataset domain. We follow the setup from previous work ( Elhage et al., 2022 ) . The model projects a 5-dimen…

限制证据摘要：In this work, we have provided a novel explanation of emergent misalignment through the lens of superposition geometry . Our results not only connect several previously observed puzzling behaviors in LLMs, but also relate to multiple existing lines of research, as summarized below. We show that emergent misalignment arises from feature superposition, where fine-tuning on narrow data amplifies nearby harmful features…

采用边界：机制锚点为 Layer-wise analysis., Training dynamics., Training Data Properties Shape Model Behavior.；评价锚点为 Layer-wise analysis., Appendix B Toy model Experiment setup, Appendix F Evaluation Details。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (marker verified)`，目标 owner 为 `WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；现有命题：表示存在、可读出与被当前路径实际使用是三个不同命题；比较：现有命题已经规定：表示存在、可读出与被当前路径实际使用是三个不同命题。本来源的受限增量是“非正交 superposition 使目标微调沿几何邻近方向产生 gradient spillover”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [LiteVLA-H: Dual-Rate Vision-Language-Action Inference for Onboard Aerial Guidance and Semantic Perception](https://arxiv.org/html/2605.00884v1)

准入时需核验的设计变化是：把 VLA 的短 action-token 外环与较慢语义输出拆成双速路径，并把 prefill 主导延迟、控制频率和知识保持训练放进同一部署合同。。exact-v1 的机制定位为 `dual-rate operation；knowledge-preserving fine-tuning；onboard Jetson AGX Orin deployment`，评价定位为 `Latency Breakdown；Dual-Rate Performance；comparison with AnywhereVLA/FutureVLA/ReMem-VLA`，限制或反证定位为 `outer-loop guidance scope；deployment-condition comparison；classical flight-control boundary`。

机制证据摘要：系统在同一 256M VLA 上区分短 action-token 的快速 guidance mode 与 sentence-level semantic mode；两条路径共享 prefill 成本，训练 mixture 同时包含 reactive flight、aerial semantic 与通用 caption/VQA，以避免动作专化抹掉描述能力。

评价证据摘要：作者在 Jetson AGX Orin 上报告 action branch 50.65 ms（19.74 Hz）、semantic branch 149.90–164.57 ms（6.08–6.67 Hz），并指出该紧凑模型的端到端延迟主要由 multimodal prefill 主导。比较只对作者披露的模型、输入和设备成立。

限制证据摘要：论文只验证 outer-loop guidance 与周期语义感知；未证明 low-level flight controller、网络抖动、传感器故障、尾延迟或安全 envelope。跨架构 headline rate 也没有统一输入、精度、kernel 与控制任务。

采用边界：证据支持在特定 edge VLA 上把 action 与 semantic cadence 分离，并识别 prefill 为主要成本；不支持把 19.74 Hz 写成通用控制频率，也不授予模型绕过低层控制器的执行权。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；现有命题：慢语义状态与快动作路径必须分别持有 cadence、freshness 和安全回退，低层 controller 仍拥有执行 authority；比较：现有小节已经给出同一双速状态合同、staleness identity、训练部署一致性与保守 controller 回退；LiteVLA-H 增加 Jetson 上 prefill-dominant 的受限测量和双任务训练案例，没有改变该长期命题。最终处置已通过独立复核。

### [The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate](https://arxiv.org/html/2605.00914v1)

准入时需核验的设计变化是：同质 debate 暴露从众、上下文脆弱和投票丢失已有正确答案的三条失败路径。exact-v1 的机制定位为 `2.1. Multi-Agent Architectures and the Evaluation Gap；3. Methodology and Experimental Design；3.2. Model Selection`，评价定位为 `2.1. Multi-Agent Architectures and the Evaluation Gap；3. Methodology and Experimental Design；3.5. Evaluation Metrics: Robustness and Economics`，限制或反证定位为 `5. Discussion, Limitations and Future Work；6. Conclusion`。

采用边界：机制锚点为 2.1. Multi-Agent Architectures and the Evaluation Gap, 3. Methodology and Experimental Design, 3.2. Model Selection；评价锚点为 2.1. Multi-Agent Architectures and the Evaluation Gap, 3. Methodology and Experimental Design, 3.5. Evaluation Metrics: Robustness and Economics。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `AGENT-MULTI-AGENT` / [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；现有命题：消息、角色和局部成功不能替代共享状态的唯一提交语义；比较：现有命题已经规定：消息、角色和局部成功不能替代共享状态的唯一提交语义。本来源的受限增量是“同质 debate 暴露从众、上下文脆弱和投票丢失已有正确答案的三条失败路径”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Watch Your Step: Information Injection in Diffusion Models via Shadow Timestep Embedding](https://arxiv.org/html/2605.00935v1)

准入时需核验的设计变化是：diffusion timestep embedding 可经 scheduler interface 成为隐蔽信息注入与 provenance side channel。exact-v1 的机制定位为 `Steganography in Diffusion Models.；Security of Diffusion Models.`，评价定位为 `Proof.；4 Experiments；4.1 Experiment Setup`，限制或反证定位为 `5 Conclusion`。

机制证据摘要：Recent work has explored diffusion models as powerful carriers for steganography, leveraging the denoising process to embed and recover hidden information. StegaDDPM ( Peng et al., 2023 ) embed secret messages into the denoising trajectory or noise space, achieving high-capacity and visually imperceptible steganography. Training-free approaches such as CRoSS ( Yu et al., 2023 ) introduce controllable and secure steganographic mechanisms by explicitly conditioning the diffusion process. Complementary to output-leve…

评价证据摘要：We refer the readers to the Appendix for the complete proof. ∎ In Eq. ( 10 ), μ \mu indicates that embeddings from I 0 I_{0} and I 1 I_{1} are nearly orthogonal, hence linearly separable in the embedding space. This separability is crucial for STE because it ensures that extending timesteps into a new interval does not collapse into the same feature manifold, but instead provides an independent channel for encoding auxiliary distributions. Empirical Observations. To demonstrate this property, we visualize empirica…

限制证据摘要：In this work, we in troduced STE, a mechanism that explores the temporal dimension of diffusion models and reveals its untapped representational capacity. By extending the timestep domain beyond the standard training range, STE constructs parallel temporal manifolds that can encode information or independent data distributions. Our analysis shows that these shadow timesteps form nearly orthogonal embedding regions,…

采用边界：机制锚点为 Steganography in Diffusion Models., Security of Diffusion Models.；评价锚点为 Proof., 4 Experiments, 4.1 Experiment Setup。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；最终处置已通过独立复核。

### [From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity](https://arxiv.org/html/2605.00939v1)

准入时需核验的设计变化是：以参数梯度敏感度近似局部曲率，区分可被小扰动修正的普通错误与对输入改写仍稳定的 stubborn hallucination。exact-v1 的机制定位为 `4 Methodology；Main Results and Analysis.；Active Curvature Probing vs. Static Representation (vs. White-Box Methods)`，评价定位为 `5 Experiments；5.1 Experiment Setup；Evaluation Metric`，限制或反证定位为 `6 Limitations；7 Conclusion；Appendix D Further Discussion`。

机制证据摘要：Our proposed method, Embedding-Perturbed Gradient Sensitivity (EPGS) , consists of three distinct phases: Target Acquisition, Embedding Perturbation, and Sensitivity Measurement. Table 1 details the hallucination detection performance across three backbone architectures and four datasets. Our proposed method EPGS consistently securing the highest AUROC scores across all 12 model-dataset configurations. The results support three primary conclusions regarding the geometric nature of hallucinations. A critical distin…

评价证据摘要：We validate our method on two distinct testing scenarios to ensure both broad applicability and specific robustness against high-confidence errors (stubborn hallucinations). We report the Area Under the Receiver Operating Characteristic curve (AUROC) ( Bradley, 1997 ) . This threshold-independent metric evaluates how effectively the EPGS Score 𝒮 \mathcal{S} separates hallucinations from correct answers.

限制证据摘要：While EPGS provides a principled geometric signal for hallucination detection, several limitations exist. In this work, we address the critical challenge of Stubborn Hallucinations, where LLMs generate factually incorrect content with high confidence and stability. We propose Embedding-Perturbed Gradient Sensitivity (EPGS) , a geometric framework that distinguishes between generalized knowledge (residing in flat min…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有覆盖差异：现有正文仍缺：以参数梯度敏感度近似局部曲率，区分可被小扰动修正的普通错误与对输入改写仍稳定的 stubborn hallucination。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。最终处置已通过独立复核。

### [E-MIA: Exam-Style Black-Box Membership Inference Attacks against RAG Systems](https://arxiv.org/html/2605.00955v1)

准入时需核验的设计变化是：以可客观评分的 hard-evidence probes 推断 RAG 语料成员身份。exact-v1 的机制定位为 `II-B Membership Inference in RAG Systems (RAG-MIA)；V E-MIA Methodology`，评价定位为 `VI Experiments；VI-A Experiment Details；VI-C Mechanism Analysis (RQ2)`，限制或反证定位为 `VII Conclusion`。

采用边界：机制锚点为 II-B Membership Inference in RAG Systems (RAG-MIA), V E-MIA Methodology；评价锚点为 VI Experiments, VI-A Experiment Details, VI-C Mechanism Analysis (RQ2)。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `AGENT-RAG` / [Ch76](../../../../books/part-07-agent/76-rag.md)；现有命题：检索相关性、证据充分性、freshness 与 provenance 是不同 gate；比较：现有命题已经规定：检索相关性、证据充分性、freshness 与 provenance 是不同 gate。本来源的受限增量是“以可客观评分的 hard-evidence probes 推断 RAG 语料成员身份”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [SRTJ: Self-Evolving Rule-Driven Training-Free LLM Jailbreaking](https://arxiv.org/html/2605.00974v1)

准入时需核验的设计变化是：分层规则记忆同时积累成功与失败攻击经验，使 jailbreak 策略跨目标持续演化。exact-v1 的机制定位为 `3. Methodology；3.7. Overall Algorithmic Flow；4.4. Hyper-parameter Analysis`，评价定位为 `4.1. Experimental Setup；4.2. Main Results`，限制或反证定位为 `3.8. Discussion；5. Conclusion`。

采用边界：机制锚点为 3. Methodology, 3.7. Overall Algorithmic Flow, 4.4. Hyper-parameter Analysis；评价锚点为 4.1. Experimental Setup, 4.2. Main Results。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor；比较：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“分层规则记忆同时积累成功与失败攻击经验，使 jailbreak 策略跨目标持续演化”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Most Current Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives](https://arxiv.org/html/2605.00994v1)

准入时需核验的设计变化是：用基模/微调模的 perplexity difference 暴露 model-organism 的微调目标。exact-v1 的机制定位为 `Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives；Model organisms.；Model diffing.`，评价定位为 `Human validation of the EM judge.；Appendix G Full quantitative results`，限制或反证定位为 `4 Discussion；Limitations.；Conclusion.`。

采用边界：机制锚点为 Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives, Model organisms., Model diffing.；评价锚点为 Human validation of the EM judge., Appendix G Full quantitative results。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“用基模/微调模的 perplexity difference 暴露 model-organism 的微调目标”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Effect-Transparent Governance for AI Workflow Architectures: Semantic Preservation, Expressive Minimality, and Decidability Boundaries](https://arxiv.org/html/2605.01030v1)

准入时需核验的设计变化是：用 effect-transparent 语义边界约束 AI workflow 的表达能力与可判定性。exact-v1 的机制定位为 `Theorem 4.1 (Governed Interpretation Safety).；Theorem 4.2 (Semantic Transparency (informal)).`，评价定位为 `Main Results (informal).；Proof.`，限制或反证定位为 `10 Discussion and Trust Boundary；Limitations.；12 Conclusion`。

采用边界：机制锚点为 Theorem 4.1 (Governed Interpretation Safety)., Theorem 4.2 (Semantic Transparency (informal)).；评价锚点为 Main Results (informal)., Proof.。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md)；现有命题：已知顺序与 invariant 应由 durable workflow 拥有，模型只处理开放决策；比较：现有命题已经规定：已知顺序与 invariant 应由 durable workflow 拥有，模型只处理开放决策。本来源的受限增量是“用 effect-transparent 语义边界约束 AI workflow 的表达能力与可判定性”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Algebraic Semantics of Governed Execution: Monoidal Categories, Effect Algebras, and Coterminous Boundaries](https://arxiv.org/html/2605.01032v1)

准入时需核验的设计变化是：以 capability-indexed effect system 和可机检 handler algebra 将治理边界绑定到可表达程序。exact-v1 的机制定位为 `The Interaction Trees framework.；Theorem 2.2 (governed_interp_safe).；Theorem 3.2 (ga_convergence).`，评价定位为 `Proof.；Effect verification.`，限制或反证定位为 `11 Conclusion；Limitations and future work.`。

机制证据摘要：All formalizations use the Interaction Trees library Xia et al. (2020) , which represents programs as coinductive trees with three node types: pure values ( Ret \mathrm{Ret} ), silent steps ( Tau \mathrm{Tau} ), and visible events ( Vis \mathrm{Vis} ). The governance pipeline transforms trees of directive events ( DirectiveE \mathrm{DirectiveE} ) into trees of governed events ( GovIOE \mathrm{GovIOE} ). Coinductive properties are proved using the paco library Hur et al. (2013) for parameterized coinduction. For an…

评价证据摘要：Each field is discharged by an existing theorem: ct_safety from governed_interp_safe_false , ct_nontrivial from bare_io_not_safe , ct_turing from ct_safety (register machine programs are itree ​ DirectiveE ​ unit \mathrm{itree}\ \mathrm{DirectiveE}\ \mathrm{unit} ), ct_subsumption from subsumption_asymmetry , ct_cognitive from cognitive_surjection . ∎ Song, Foo, and Chin Song et al. (2024) develop ESL, an expressive specification logic for verifying programs with unrestricted algebraic effects and handlers. Their…

限制证据摘要：We have presented an algebraic semantics for governed execution, formalized in 36 Rocq modules with 454 theorems and zero admitted lemmas. The central result is that governance, when axiomatized as a three-property algebra over interaction trees, induces compositional structure on programs, effects, and capabilities such that the governed fragment coincides with the expressible fragment in the modeled substrate. Tur…

采用边界：机制锚点为 The Interaction Trees framework., Theorem 2.2 (governed_interp_safe)., Theorem 3.2 (ga_convergence).；评价锚点为 Proof., Effect verification.。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `AGENT-PLATFORM` / [Ch84](../../../../books/part-07-agent/84-agent-platform.md)；最终处置已通过独立复核。

### [Certified Purity for Cognitive Workflow Executors: From Static Analysis to Cryptographic Attestation](https://arxiv.org/html/2605.01037v1)

准入时需核验的设计变化是：把静态 purity 证明签名成运行时可校验的执行凭证并显式保留 TCB。exact-v1 的机制定位为 `2.1 The Pure Execution Model；2.4 WebAssembly Capability Model`，评价定位为 `Certified Purity for Cognitive Workflow Executors: From Static Analysis to Cryptographic Attestation；Bypass Class 2: Code evaluation.；2.3 Proof-Carrying Code`，限制或反证定位为 `Not Disclosed as a standalone section`。

机制证据摘要：We summarize the pure execution model from the prior work McCann (2026e) , using the same notation. WebAssembly (WASM) Haas et al. (2017) ; Rossberg (2024) is a portable bytecode format designed as a compilation target for high-level languages. Its security model is based on capability restriction : a WASM module can only access capabilities explicitly provided to it through imports. Specifically: 1. A WASM module declares its imports explicitly in its binary format. 2. The host environment provides implementation…

评价证据摘要：Alan L. McCann Affiliation: Mashin, Inc. Email: research@mashin.live April 2026 Code.eval_string("File.write!(\"/tmp/exfil\", data)") evaluates arbitrary Elixir code at runtime, with full access to the BEAM module environment. Necula Necula (1997) introduced proof-carrying code (PCC), in which a code producer attaches a machine-checkable proof that the code satisfies a safety policy. The code consumer verifies the proof before execution, obtaining the safety guarantee without trusting the producer. PCC was origina…

限制证据摘要：未发现独立 Limitations 标题；不得把作者 workload、模型与指标之外的迁移视为已证明。

采用边界：机制锚点为 2.1 The Pure Execution Model, 2.4 WebAssembly Capability Model；评价锚点为 Certified Purity for Cognitive Workflow Executors: From Static Analysis to Cryptographic Attestation, Bypass Class 2: Code evaluation., 2.3 Proof-Carrying Code。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `AGENT-PLATFORM` / [Ch84](../../../../books/part-07-agent/84-agent-platform.md)；现有命题：skill、run、tool effect 与 release/rollback 必须保持独立身份；比较：现有命题已经规定：skill、run、tool effect 与 release/rollback 必须保持独立身份。本来源的受限增量是“把静态 purity 证明签名成运行时可校验的执行凭证并显式保留 TCB”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [LLM Ghostbusters: Surgical Hallucination Suppression via Adaptive Unlearning](https://arxiv.org/html/2605.01047v1)

准入时需核验的设计变化是：把已观测 package hallucination 转成可定位的 post-deployment unlearning 对象，并用自适应 masking 限制能力 collateral damage。exact-v1 的机制定位为 `1.2. Our Approach.；3. Method；3.1. Problem Formulation`，评价定位为 `4. Experimental Evaluation；4.4. Experimental Configuration；4.5. Baselines and Ablations`，限制或反证定位为 `Architecture-dependent utility tradeoff.；7. Limitations；8. Conclusion`。

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `No Change — Existing Coverage (proposition comparison; independent review required)`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有命题：本章已要求删除、抑制或修复后的能力保持与攻击复测共同进入 release gate；单一 package 工作负载没有改变该合同；比较：exact-v1 的新增证据是“把已观测 package hallucination 转成可定位的 post-deployment unlearning 对象，并用自适应 masking 限制能力 collateral damage”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。最终处置已通过独立复核。

### [Compared to What? Baselines and Metrics for Counterfactual Prompting](https://arxiv.org/html/2605.01048v1)

准入时需核验的设计变化是：用 meaning-preserving perturbation 作为反事实 baseline，避免把表面改写误判为目标因素效应。exact-v1 的机制定位为 `4.2 Sanity checks for the proposed testing framework；Metric Power Analysis via Simulation；Appendix A Level Model Regression Specification`，评价定位为 `4 Experiments；Results；Metric Power Analysis via Simulation`，限制或反证定位为 `6 Conclusions, Practical Guidance, and Limitations；Limitations.`。

采用边界：机制锚点为 4.2 Sanity checks for the proposed testing framework, Metric Power Analysis via Simulation, Appendix A Level Model Regression Specification；评价锚点为 4 Experiments, Results, Metric Power Analysis via Simulation。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“用 meaning-preserving perturbation 作为反事实 baseline，避免把表面改写误判为目标因素效应”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [LEAP: Layer-wise Exit-Aware Pretraining for Efficient Transformer Inference](https://arxiv.org/html/2605.01058v1)

准入时需核验的设计变化是：Layer-aligned distillation 会抑制 convergence-based early exit 所依赖的中间层收敛；训练目标必须显式塑造可退出状态，并保留 full-depth 回退。。exact-v1 的机制定位为 `§3.1 Distillation–early-exit incompatibility；§3.2 LEAP objective；§3.3 Exit inference`，评价定位为 `§4.1 Experimental setup；§4.2 Main results；§4.5 Quality–latency trade-off`，限制或反证定位为 `§Limitations: embedding-model scope, batching, domain/scale and statistical rigor`。

机制证据摘要：Layer-aligned distillation and convergence-based early exit represent two predominant computational efficiency paradigms for transformer inference; yet we establish that they exhibit systematic incompatibility under standard deployment conditions for convergence-based early exit. Distillation objectives that align intermediate student layers to teacher representations suppress the representational convergence that early-exit mechanisms exploit, rendering such mechanisms ineffective on distilled models. We introduc…

评价证据摘要：Layer-aligned distillation and convergence-based early exit represent two predominant computational efficiency paradigms for transformer inference; yet we establish that they exhibit systematic incompatibility under standard deployment conditions for convergence-based early exit. Distillation objectives that align intermediate student layers to teacher representations suppress the representational convergence that early-exit mechanisms exploit, rendering such mechanisms ineffective on distilled models. We introduc…

限制证据摘要：只支持 exact-v1 披露的任务、模型、环境和 evaluator；未披露的跨域、生产与长期稳定性不得外推。

采用边界：Layer-aligned distillation 会抑制 convergence-based early exit 所依赖的中间层收敛；训练目标必须显式塑造可退出状态，并保留 full-depth 回退。 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `Integrate Applied — body marker and root-corrected trace independently verified`，目标 owner 为 `INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；最终处置已通过独立复核。

### [SURGE: SuperBatch Unified Resource-efficient GPU Encoding for Heterogeneous Partitioned Data](https://arxiv.org/html/2605.01060v1)

准入时需核验的设计变化是：SuperBatch 在跨分区 embedding 中同时给出有界内存、流式首输出与故障恢复粒度。exact-v1 的机制定位为 `2.2. Baseline Approaches: PBP and FSB；2.3. Multi-GPU Encoding Cost Model`，评价定位为 `4. Formal Analysis；Proof.；Corollary 2 (Regime analysis).`，限制或反证定位为 `5.12. Threats to Validity；9. Conclusion`。

采用边界：机制锚点为 2.2. Baseline Approaches: PBP and FSB, 2.3. Multi-GPU Encoding Cost Model；评价锚点为 4. Formal Analysis, Proof., Corollary 2 (Regime analysis).。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `INFER-GPU-MEMORY` / [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)；现有命题：物理容量、逻辑状态和生命周期必须由不同 owner 记账；比较：现有命题已经规定：物理容量、逻辑状态和生命周期必须由不同 owner 记账。本来源的受限增量是“SuperBatch 在跨分区 embedding 中同时给出有界内存、流式首输出与故障恢复粒度”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Online Safety Filter for Deformable Object Manipulation with Horizon Agnostic Neural Operators](https://arxiv.org/html/2605.01069v1)

准入时需核验的设计变化是：用 task-level barrier function 在运行时最小修正具身策略动作，而不是把安全隐含进 reward。exact-v1 的机制定位为 `II-B Neural Operators for Modeling PDE-Governed Dynamics；II-C Model-Based Safety Filters for Robotics；III Methodology`，评价定位为 `IV Experimental Results；IV-A Experimental Setup；IV-B Implementation Details`，限制或反证定位为 `V Conclusion`。

采用边界：机制锚点为 II-B Neural Operators for Modeling PDE-Governed Dynamics, II-C Model-Based Safety Filters for Robotics, III Methodology；评价锚点为 IV Experimental Results, IV-A Experimental Setup, IV-B Implementation Details。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；现有命题：行动闭环必须绑定 observation、action schema、控制频率与安全回退；比较：现有命题已经规定：行动闭环必须绑定 observation、action schema、控制频率与安全回退。本来源的受限增量是“用 task-level barrier function 在运行时最小修正具身策略动作，而不是把安全隐含进 reward”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Component-Aware Self-Speculative Decoding in Hybrid Language Models](https://arxiv.org/html/2605.01106v1)

准入时需核验的设计变化是：hybrid model 的组件组合方式决定内部 draft 的可接受率与 self-speculation 可行性。exact-v1 的机制定位为 `2.3 Hybrid Architectures`，评价定位为 `3.3 Draft Generation and Verification Protocol；Verification phase；3.4 Theoretical Speedup Analysis`，限制或反证定位为 `8 Conclusion`。

采用边界：机制锚点为 2.3 Hybrid Architectures；评价锚点为 3.3 Draft Generation and Verification Protocol, Verification phase, 3.4 Theoretical Speedup Analysis。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `INFER-SPECULATIVE-DECODING` / [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)；现有命题：proposal 可以近似，最终 commit 必须保持 target distribution 与唯一提交边界；比较：现有命题已经规定：proposal 可以近似，最终 commit 必须保持 target distribution 与唯一提交边界。本来源的受限增量是“hybrid model 的组件组合方式决定内部 draft 的可接受率与 self-speculation 可行性”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [When Less is Enough: Efficient Inference via Collaborative Reasoning](https://arxiv.org/html/2605.01111v1)

准入时需核验的设计变化是：由小模型先执行、再按边际效用与长度惩罚决定是否升级大模型，把协作推理变成请求级资源控制。exact-v1 的机制定位为 `3.1 Algorithm；Appendix B Algorithm；Appendix D Baseline Algorithms`，评价定位为 `4 Experiments；4.1 Experimental Setting；4.2 Main Results And Ablations`，限制或反证定位为 `5 Conclusions and Future Works；Limitation.；Future Work.`。

机制证据摘要：DUET proposes the following constrained optimization objective: max M θ , m ϕ 𝔼 x , z ∼ M θ ( ⋅ \| x ) [ 𝔼 y M ​ m ∼ m ϕ ( ⋅ \| z ) [ R ( x , y M ​ m ) ] ] s.t. 𝔼 x , z ∼ M θ ( ⋅ \| x ) [ L ( z ) ] ≤ B , \max_{M_{\theta},m_{\phi}}\mathbb{E}_{x,z\sim M_{\theta}(\cdot\|x)}\left[\mathbb{E}_{y_{Mm}\sim m_{\phi}(\cdot\|z)}[R(x,y_{Mm})]\right]\text{ s.t. }\mathbb{E}_{x,z\sim M_{\theta}(\cdot\|x)}[L(z)]\leq B, (1) for some bound B B on the expected length of the generated sequence of intermediate tokens. Intuitively, the…

评价证据摘要：In this section, we present the experimental results of DUET, with the goal of answering the following questions: • Is DUET an effective framework for efficient inference? • How sensitive is DUET to the choice of training dataset? • How do different designs within DUET affect its performance? Models. We adopt Qwen3-4B (thinking mode enabled) as the capable (large) model and Qwen3-0.6B as the lightweight (small) model ( Yang et al., 2025 ) . Given our limited computing resources of only 4 H100 GPUs, Qwen3-4B is a s…

限制证据摘要：In this work, we introduced DUET for efficient inference by splitting it into two stages: a high-capacity model that outputs a compact reasoning signal, and a lightweight model that decodes it into the final response. We show that DUET can eliminate up to 60 % 60\% of large-model output tokens on AIME and GPQA without sacrificing accuracy. More broadly, our results shift the efficiency lens from compressing paramete…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `No Change — Existing Coverage (proposition comparison; independent review required)`，目标 owner 为 `INFER-SCHEDULING` / [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；现有命题：本章已把模型路由写成按难度、质量预算和尾延迟升级的控制环，DUET 是该分支的受限实现；比较：exact-v1 的新增证据是“由小模型先执行、再按边际效用与长度惩罚决定是否升级大模型，把协作推理变成请求级资源控制”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。最终处置已通过独立复核。

### [Revisiting Privacy Leakage in Machine Unlearning: Membership Inference Beyond the Forgotten Set](https://arxiv.org/html/2605.01129v1)

准入时需核验的设计变化是：unlearning 前后差分会把隐私泄漏从 forget set 扩展到 retain set。exact-v1 的机制定位为 `III-A Threat Model；III-B Problem Formulation；III-C A Straw-man Approach: Two-round Attack`，评价定位为 `IV Pre-attack Analysis；VI Evaluation；VI-F Parameter Sensitivity Analysis (RQ5)`，限制或反证定位为 `III-A Threat Model；X Conclusion`。

采用边界：机制锚点为 III-A Threat Model, III-B Problem Formulation, III-C A Straw-man Approach: Two-round Attack；评价锚点为 IV Pre-attack Analysis, VI Evaluation, VI-F Parameter Sensitivity Analysis (RQ5)。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor；比较：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“unlearning 前后差分会把隐私泄漏从 forget set 扩展到 retain set”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Iterative Finetuning is Mostly Idempotent](https://arxiv.org/html/2605.01130v1)

准入时需核验的设计变化是：连续 SFT/SDF 多数近似幂等，而持续 DPO 且不重置模型时才稳定放大特征。exact-v1 的机制定位为 `3.1 Training Procedure；5.1 Training Procedure；Model collapse.`，评价定位为 `3.2 SFT Results；4.2 SDF Results；5.2 DPO Results`，限制或反证定位为 `8 Discussion；10 Conclusion`。

采用边界：机制锚点为 3.1 Training Procedure, 5.1 Training Procedure, Model collapse.；评价锚点为 3.2 SFT Results, 4.2 SDF Results, 5.2 DPO Results。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；现有命题：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算；比较：现有命题已经规定：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算。本来源的受限增量是“连续 SFT/SDF 多数近似幂等，而持续 DPO 且不重置模型时才稳定放大特征”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [When Embedding-Based Defenses Fail: Rethinking Safety in LLM-Based Multi-Agent Systems](https://arxiv.org/html/2605.01133v1)

准入时需核验的设计变化是：embedding 防御在多轮多 Agent 传播中衰减，暴露局部过滤并非系统安全边界。exact-v1 的机制定位为 `Multi-agent system safety.；Theorem 4.1 (Acceptance region and near-benign evasion).`，评价定位为 `7 Experiments；7.1 Experimental Setup`，限制或反证定位为 `8 Discussion；9 Conclusion`。

采用边界：机制锚点为 Multi-agent system safety., Theorem 4.1 (Acceptance region and near-benign evasion).；评价锚点为 7 Experiments, 7.1 Experimental Setup。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `AGENT-MULTI-AGENT` / [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；现有命题：消息、角色和局部成功不能替代共享状态的唯一提交语义；比较：现有命题已经规定：消息、角色和局部成功不能替代共享状态的唯一提交语义。本来源的受限增量是“embedding 防御在多轮多 Agent 传播中衰减，暴露局部过滤并非系统安全边界”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Metric-Normalized Posterior Leakage (mPL): Attacker-Aligned Privacy for Joint Consumption](https://arxiv.org/html/2605.01137v1)

准入时需核验的设计变化是：联合观察会聚合相关证据，使逐记录 metric-DP 保证不能约束 posterior leakage。exact-v1 的机制定位为 `2.4 Threat Models based on Joint and Correlated Observations；3 Data Perturbation Framework；A The Use of Large Language Models (LLMs)`，评价定位为 `4 Case Study: PII/PoII Embedding Protection`，限制或反证定位为 `2.4 Threat Models based on Joint and Correlated Observations；5 Conclusions`。

机制证据摘要：In this part, we relax the independence assumption and introduce more realistic threat models where the records X 1 , … , X L X_{1},\ldots,X_{L} are dependent. (1) Explicit joint-probability attacker (a toy example). We consider an attacker that models the joint distribution of two secrets and performs Bayesian inference over two perturbed outputs. Let X 1 , X 2 ∈ 𝒳 = { x 1 , x 2 } X_{1},X_{2}\in\mathcal{X}=\{x_{1},x_{2}\} with a correlated prior: Pr ⁡ ( X 1 = x 1 , X 2 = x 1 ) = Pr ⁡ ( X 1 = x 2 , X 2 = x 2 ) = 0…

评价证据摘要：We evaluate AmPL on text embeddings because embeddings are widely used in deployed systems and text exhibits layered sensitivities (PII vs. PoII) that naturally align with level-wise perturbation; it also provides standard threat models (reconstruction/attribute inference) and utility benchmarks (classification/retrieval). 1 1 1 An anonymized artifact is included in the supplementary material. Although our experiments perturb in embedding space, mPL/AmPL are modality- and representation-agnostic, requiring only a…

限制证据摘要：In this part, we relax the independence assumption and introduce more realistic threat models where the records X 1 , … , X L X_{1},\ldots,X_{L} are dependent. (1) Explicit joint-probability attacker (a toy example). We consider an attacker that models the joint distribution of two secrets and performs Bayesian inference over two perturbed outputs. Let X 1 , X 2 ∈ 𝒳 = { x 1 , x 2 } X_{1},X_{2}\in\mathcal{X}=\{x_{1},…

采用边界：机制锚点为 2.4 Threat Models based on Joint and Correlated Observations, 3 Data Perturbation Framework, A The Use of Large Language Models (LLMs)；评价锚点为 4 Case Study: PII/PoII Embedding Protection。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；最终处置已通过独立复核。

### [Arithmetic in the Wild: Llama uses Base-10 Addition to Reason About Cyclic Concepts](https://arxiv.org/html/2605.01148v1)

准入时需核验的设计变化是：用跨任务 activation patching 与 Fourier probe 显示加法子电路可被循环概念复用，并定位稀疏 MLP 子电路。exact-v1 的机制定位为 `Approach.；Evidence for a shared mechanism.；3 The Shared Mechanism is Addition`，评价定位为 `Task setup.；Neuron ablations.；Appendix A Task Setup`，限制或反证定位为 `7 Conclusion；Limitations；Discussion.`。

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `No Change — Existing Coverage (proposition comparison; independent review required)`，目标 owner 为 `WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；现有命题：本章已区分表示几何、可干预电路与因果证明；该案例补充证据但不改变表示不等于算法所有权的边界；比较：exact-v1 的新增证据是“用跨任务 activation patching 与 Fourier probe 显示加法子电路可被循环概念复用，并定位稀疏 MLP 子电路”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。最终处置已通过独立复核。

### [Minimizing Collateral Damage in Activation Steering](https://arxiv.org/html/2605.01167v1)

准入时需核验的设计变化是：在保持目标 steering 幅度的约束面上最小化二阶 collateral energy，把 activation steering 写成受约束几何优化。exact-v1 的机制定位为 `4 Theoretical analysis of COAST；A.3.3 Topological Separation Analysis；Boundary Flow Analysis:`，评价定位为 `5 Experiments；Appendix C More experiment details`，限制或反证定位为 `6 Conclusions`。

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `No Change — Existing Coverage (proposition comparison; independent review required)`，目标 owner 为 `WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；现有命题：本章已要求 steering 同时评估目标方向、旁路能力损失与分布外回退，COAST 没有改变该所有权边界；比较：exact-v1 的新增证据是“在保持目标 steering 幅度的约束面上最小化二阶 collateral energy，把 activation steering 写成受约束几何优化”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。最终处置已通过独立复核。

### [A Theory of Generalization in Deep Learning](https://arxiv.org/html/2605.01172v1)

准入时需核验的设计变化是：把深度学习泛化拆成可被测试点看到的 signal channel 与训练集 reservoir，并用 drift-diffusion 与 train-test coupling 刻画误差。exact-v1 的机制定位为 `Worst-case bounds and algorithmic stability.；From the rate to the algorithm.；Remark E.5 (Equivalent formulations).`，评价定位为 `Results.；Proof of the four results above.；Appendix I Additional Experiments`，限制或反证定位为 `7 Conclusion；Remark E.11 (Dimensional limitation).；Proposition H.9 (Bias–variance trade-off along the ridge path).`。

机制证据摘要：Uniform-convergence bounds, whether expressed in terms of VC dimension ( Vapnik and Chervonenkis, 1971 ) , covering numbers ( Dudley, 1967 ) , Rademacher complexity ( Bartlett and Mendelson, 2002 ) , weight norms ( Bartlett, 1998 ; Neyshabur et al., 2015 ) , or spectral complexity ( Bartlett et al., 2017 ) , are vacuous at practical scale ( Zhang et al., 2017 ) , and Nagarajan and Kolter (2019) argued that uniform convergence is insufficient for deep learning. Algorithmic stability ( Bousquet and Elisseeff, 2002 ;…

评价证据摘要：We test the resulting rule across three regimes where empirical-risk training is known to overfit structured noise or to memorize before generalizing; architecture, data split, and optimizer hyperparameters are held fixed and only the population-risk update changes. On a PINN solving u t + β ​ u x = 0 u_{t}+\beta u_{x}=0 at β = 5 \beta=5 from a Gaussian-noisy initial condition, the rule reaches relative ℓ 2 ≤ 0.40 \ell_{2}\leq 0.40 in 2.4 × 2.4\times fewer iterations than the best learning-rate-tuned AdamW ( Figur…

限制证据摘要：As a deep network trains, its empirical NTK rotates label noise into a test-invisible reservoir, and SGD’s centered fluctuation suppresses what survives in the signal channel; on the signal side, training motion determines test motion, even when the kernel drifts by 𝒪 ⁡ ( 1 ) \mathcal{O}(1) . The same operators turn a single batch into an unbiased rate of population-risk decrease, maximized through the optimizer’s m…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `No Change — Existing Coverage (proposition comparison; independent review required)`，目标 owner 为 `WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；现有命题：本章已把低训练损失与泛化分离，并要求表征、优化轨迹和数据分布共同解释；理论模型未推翻该主线；比较：exact-v1 的新增证据是“把深度学习泛化拆成可被测试点看到的 signal channel 与训练集 reservoir，并用 drift-diffusion 与 train-test coupling 刻画误差”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。最终处置已通过独立复核。

### [Compute Optimal Tokenization](https://arxiv.org/html/2605.01188v1)

准入时需核验的设计变化是：compute-optimal allocation 随 bytes 而非 token 数缩放，token compression rate 成为训练变量。exact-v1 的机制定位为 `[R2]: Is there an optimal compression rate for specific datasets?；[R3]: Is the impact of compression rate on scaling trends similar for latent and subword tokenized models?；2 Methodology`，评价定位为 `2.2 Training and Evaluation；3.2 Scaling Law I: Results；3.4 Scaling Law II: Results`，限制或反证定位为 `7 Discussion；7.2 Limitations；8 Conclusion`。

机制证据摘要：We investigate whether there exists a compression rate that yields the lowest loss for a fixed compute budget, assuming the optimal data to parameter ratio. Furthermore, we examine whether this optimal compression rate shifts with the compute budget or dataset domain. Does the answer to the previous questions depend on the tokenization method? We conduct experiments on subword-tokenized models to validate if the scaling trends match those observed for BLT. In this section, we provide details on the language models…

评价证据摘要：We train models under compute budgets ( C C ) expressed in FLOPs, ranging from 5 × 10 18 5\times 10^{18} to 2 × 10 21 2\times 10^{21} FLOPs. If not stated otherwise, we use exact computation of training FLOPs, instead of an approximation. In total, we train 988 latently and 320 subword tokenized models with sizes from 50M to 6.7B parameters on training data of sizes from 4B to 1.1T bytes. For each budget C C , we vary the parameter size ( N N ) and compression rate ( T T ). The parameters N N and compression rate…

限制证据摘要：The relationship between scaling laws and data compression highlights the importance of considering tokenizer compression rate in the optimal design of large language models. Our observations overlap with the Hoffmann et al. (2022) (Chinchilla) recipe, suggesting that data and model parameters should be scaled proportionally. Generalizing the Chinchilla rule, we show that the appropriate unit for data quantity is by…

采用边界：机制锚点为 [R2]: Is there an optimal compression rate for specific datasets?, [R3]: Is the impact of compression rate on scaling trends similar for latent and subword tokenized models?, 2 Methodology；评价锚点为 2.2 Training and Evaluation, 3.2 Scaling Law I: Results, 3.4 Scaling Law II: Results。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `TRAIN-DATA` / [Ch27](../../../../books/part-04-training-system/27-data.md)；现有命题：数据来源、过滤、去重与 lineage 共同决定训练更新，而不是样本数量单独决定；比较：现有命题已经规定：数据来源、过滤、去重与 lineage 共同决定训练更新，而不是样本数量单独决定。本来源的受限增量是“compute-optimal allocation 随 bytes 而非 token 数缩放，token compression rate 成为训练变量”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Sentinel-VLA: A Metacognitive VLA Model with Active Status Monitoring for Dynamic Reasoning and Error Recovery](https://arxiv.org/html/2605.01191v1)

准入时需核验的设计变化是：由 active sentinel 持有实时执行状态，只在初始化、新子任务或错误时触发 reasoning/recovery，并把能力边界反馈到持续数据收集。。exact-v1 的机制定位为 `Sentinel-VLA architecture；active status monitoring；SECL and OC-Adapter`，评价定位为 `real-world manipulation tasks；status-transition ablation；continual-learning evaluation`，限制或反证定位为 `selected task/error taxonomy；open-source future tense；no production tail/safety evaluation`。

机制证据摘要：sentinel 把执行状态划为 Initial、Normal、New-subtask 与 Error；Normal 状态复用动作/思考记忆，其他状态才触发规划、更新或恢复。SECL 根据失败边界收集数据，OC-Adapter 约束持续更新以减轻遗忘。

评价证据摘要：作者在自动生成的 44 个任务、约 260 万 transition 和有限真实机器人任务上比较状态监控、推理与持续学习组件，并报告相对 PI0 的任务成功率提升；这些结果绑定作者任务、错误注入和训练管线。

限制证据摘要：论文没有证明状态分类覆盖开放世界异常，也没有独立验证 sentinel 的 false-negative、tail latency、传感器失真或物理安全；代码和权重在 v1 中仍以未来开放表述。

采用边界：证据支持把状态监控作为 reasoning 的触发器和数据闭环的传感器；不证明 sentinel 状态是真值，也不允许它直接拥有 actuator commit。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；现有命题：异常监测只触发 plan、update 或 recover，必须绑定 observation revision、deadline 与安全回退，不能越过 action admission；比较：现有小节已经明确正常状态复用、异常状态触发推理/恢复，以及 monitor 只持有 proposal 权；该论文提供一个四状态实现和持续学习案例，但没有改变状态 owner 或提交边界。最终处置已通过独立复核。

### [Linear-Readout Floors and Threshold Recovery in Computation in Superposition](https://arxiv.org/html/2605.01192v1)

准入时需核验的设计变化是：线性 readout 的 cross-talk floor 与非线性 threshold reset 形成不同的 superposition 容量边界。exact-v1 的机制定位为 `3 Formal Model Definitions；Definition 3.1 (Model H: approximate-linear recursive template).；Definition 3.2 (Model AS: threshold-reset recursive superposition).`，评价定位为 `Proof.；12 Empirical Context；Empirical context.`，限制或反证定位为 `Limitations.；14 Conclusion`。

机制证据摘要：We write O ~ ​ ( ⋅ ) \widetilde{O}(\cdot) , Ω ~ ​ ( ⋅ ) \widetilde{\Omega}(\cdot) , Θ ~ ​ ( ⋅ ) \widetilde{\Theta}(\cdot) to hide factors polynomial in log ⁡ d \log d or log ⁡ n \log n . Unless explicitly varied, s = O ⁡ ( 1 ) s=O(1) denotes a fixed constant sparsity parameter; Section 8 separately studies random supports with sparsity growing as large as O ⁡ ( d / log ⁡ d ) O(d/\log d) . A recursive Model-H computation alternates: (i) a targeted superpositional AND computation layer producing outgoing error ε com…

评价证据摘要：Theorem 11 of Hänni et al., the targeted superpositional AND theorem, gives outgoing precision ε out = O ~ ​ ( s 2 d ) = O ~ ​ ( s / d ) \varepsilon_{\mathrm{out}}=\widetilde{O}\!\left(\sqrt{\frac{s^{2}}{d}}\right)=\widetilde{O}(s/\sqrt{d}) under its stated hypotheses, including the graph-balance and incoming-interference assumptions. For constant sparsity s = O ⁡ ( 1 ) s=O(1) this is O ~ ( d − 1 / 2 ) \widetilde{O}(d^{-1/2}) . The distinction from Theorem 14 is important. Theorem 14 gives an error term of the for…

限制证据摘要：(i) The Hänni-template comparison assumes constant-sparsity Boolean computation, while the distributional threshold result separately treats random supports with s s growing up to O ⁡ ( d / log ⁡ d ) O(d/\log d) ; real features are continuous with heterogeneous sparsity. (ii) The Welch floor bounds small-error linear readout interfaces, not all possible corrections. (iii) The interpolation (Proposition 9.3 ) is cond…

采用边界：机制锚点为 3 Formal Model Definitions, Definition 3.1 (Model H: approximate-linear recursive template)., Definition 3.2 (Model AS: threshold-reset recursive superposition).；评价锚点为 Proof., 12 Empirical Context, Empirical context.。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；最终处置已通过独立复核。

### [VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model](https://arxiv.org/html/2605.01194v1)

准入时需核验的设计变化是：uncertainty clutch 只在需要时切换到候选动作与相对 action critic 的 deliberation。exact-v1 的机制定位为 `Sequential Deliberation in VLA models.；Parallel Deliberation in VLA models.`，评价定位为 `5 Experiments；Base Models and Implementation Details`，限制或反证定位为 `6 Conclusion`。

机制证据摘要：Early approaches like ECoT ( Zawalski et al., 2024 ) , CoT-VLA ( Zhao et al., 2025 ) , RoboMamba ( Liu et al., 2024 ) and PI0.5 ( Black et al., 2025 ) output predefined, structured information, such as sub-task decompositions, before an action. Subsequent works like ChatVLA ( Zhou et al., 2025b ) , ChatVLA2 ( Zhou et al., 2025a ) , Hume ( Song et al., 2025 ) , and OneTwoVLA ( Lin et al., 2025 ) moved towards generating more adaptive, free-form natural language thoughts. However, all approaches demand costly fine-t…

评价证据摘要：In this section, we conduct extensive experiments to address the following research questions (RQ): • RQ1 (Effectiveness) : Can VLA-ATTC significantly enhance the performance on complex tasks? • RQ2 (Ablation) : What are the contributions of core components and the impact of candidate scaling and uncertainty threshold? • RQ3 (Mechanism) : Are the proposed uncertainty measurement and automated data curation pipeline scientifically valid and necessary? • RQ4 (Efficiency) : While delivering performance gains, does VL…

限制证据摘要：In this work, we introduced VLA-ATTC, a framework that fundamentally challenges the static, “one-size-fits-all” inference paradigm of VLA models. By dynamically triggering a test-time deliberation phase via an uncertainty-based “cognitive clutch”, and employing an efficient, lightweight Relative Action Critic model for pairwise selection, our method significantly enhances decision-making robustness in complex scenar…

采用边界：机制锚点为 Sequential Deliberation in VLA models., Parallel Deliberation in VLA models.；评价锚点为 5 Experiments, Base Models and Implementation Details。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；现有命题：行动闭环必须绑定 observation、action schema、控制频率与安全回退；比较：现有命题已经规定：行动闭环必须绑定 observation、action schema、控制频率与安全回退。本来源的受限增量是“uncertainty clutch 只在需要时切换到候选动作与相对 action critic 的 deliberation”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [TAIL-Safe: Task-Agnostic Safety Monitoring for Imitation Learning Policies](https://arxiv.org/html/2605.01195v1)

准入时需核验的设计变化是：从状态-动作安全分数构造经验控制不变集，并在越界时触发 recovery。exact-v1 的机制定位为 `II Problem Formulation；IV-C Designing a Recovery Controller to Maintain Task Success；V-D3 Q-Function Calibration Analysis`，评价定位为 `V Experimental Evaluation；V-A Tasks and Experimental Configuration；V-D Ablation Study`，限制或反证定位为 `V-B Policy Failure vs. TAIL-Safe Guided Success；VI Limitations and Future Work；VII Conclusion`。

采用边界：机制锚点为 II Problem Formulation, IV-C Designing a Recovery Controller to Maintain Task Success, V-D3 Q-Function Calibration Analysis；评价锚点为 V Experimental Evaluation, V-A Tasks and Experimental Configuration, V-D Ablation Study。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；现有命题：行动闭环必须绑定 observation、action schema、控制频率与安全回退；比较：现有命题已经规定：行动闭环必须绑定 observation、action schema、控制频率与安全回退。本来源的受限增量是“从状态-动作安全分数构造经验控制不变集，并在越界时触发 recovery”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Focus and Dilution: The Multi-stage Learning Process of Attention](https://arxiv.org/html/2605.01199v1)

准入时需核验的设计变化是：把 attention 学习描述为 focus、dilution 与再聚焦的阶段性梯度动力学，而非单调收敛。exact-v1 的机制定位为 `Training dynamics of attention and multi-stage analysis；Analysis of transition between stage I and II；E.2 Analysis Tools`，评价定位为 `3 Theoretical results；4 Empirical evidence；4.1 Synthetic Experiments`，限制或反证定位为 `5 Conclusion；Limitation；Conclusion.`。

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `No Change — Existing Coverage (proposition comparison; independent review required)`，目标 owner 为 `MODEL-SELF-ATTENTION` / [Ch14](../../../../books/part-02-model/14-self-attention.md)；现有命题：本章已解释 attention score、竞争归一化和训练信号的相互作用；单层 Markov 理论属于机制证据而非新 owner；比较：exact-v1 的新增证据是“把 attention 学习描述为 focus、dilution 与再聚焦的阶段性梯度动力学，而非单调收敛”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。最终处置已通过独立复核。

### [To Do or Not to Do: Ensuring the Safety of Visuomotor Policies Learned from Demonstrations](https://arxiv.org/html/2605.01201v1)

准入时需核验的设计变化是：用 execution-guarantee region 将任务成功与是否允许 visuomotor policy 执行绑定。exact-v1 的机制定位为 `3.1 IL-Powered Robot as a Dynamic System；3.3 Nagumo’s Theorem；5 A Set-Theoretic Framework for Evaluating Execution Guarantee`，评价定位为 `6 Experimental Evaluation；6.1 Experimental Setup；Evaluation Metric.`，限制或反证定位为 `7 Limitations and Future Work；8 Conclusion`。

机制证据摘要：A robotic system (e.g., a manipulator) executing a learned policy π \pi can be modeled as a continuous-time dynamical system: x ˙ ​ ( t ) = f ⁡ ( x ⁡ ( t ) , a ⁡ ( t ) ) \dot{x}(t)=f(x(t),a(t)) , where x ⁡ ( t ) ∈ ℝ n x x(t)\in\mathbb{R}^{n_{x}} denotes the state and a ⁡ ( t ) ∈ ℝ n a a(t)\in\mathbb{R}^{n_{a}} the control input at time t ∈ ℝ ≥ 0 t\in\mathbb{R}_{\geq 0} , with π : x ⁡ ( t ) → a ⁡ ( t ) \pi:x(t)\rightarrow a(t) . For many IL-based manipulators, a simplified fully-actuated model is assumed: x ˙ ​ ( t…

评价证据摘要：We evaluate our proposed safety framework through comprehensive experiments in both simulation and real-world environments. The evaluation focuses on three core objectives: (1) validating that learned control-invariant (CI) sets 𝒮 \mathcal{S} enable safe and successful policy execution; (2) assessing the effectiveness of the recovery controller a ′ a^{\prime} in maintaining trajectories within 𝒮 \mathcal{S} ; and (3) demonstrating that policies constrained to 𝒮 \mathcal{S} are robust to significant out-of-distribu…

限制证据摘要：The safeset construction process is currently goal-specific and assumes demonstration data sufficiently covers perceptually consistent goal regions; generalizing this to arbitrary goal configurations or dynamic targets remains an open challenge. Additionally, the framework does not explicitly model grasp feasibility. Integrating grasp-conditioned embeddings or learning grasp-aware safe sets could improve performance…

采用边界：机制锚点为 3.1 IL-Powered Robot as a Dynamic System, 3.3 Nagumo’s Theorem, 5 A Set-Theoretic Framework for Evaluating Execution Guarantee；评价锚点为 6 Experimental Evaluation, 6.1 Experimental Setup, Evaluation Metric.。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；现有命题：行动闭环必须绑定 observation、action schema、控制频率与安全回退；比较：现有命题已经规定：行动闭环必须绑定 observation、action schema、控制频率与安全回退。本来源的受限增量是“用 execution-guarantee region 将任务成功与是否允许 visuomotor policy 执行绑定”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Faithful Mobile GUI Agents with Guided Advantage Estimator](https://arxiv.org/html/2605.01208v1)

准入时需核验的设计变化是：以 reward-bound anchors 和方差自适应 tempering 在 collapsed rollout group 中恢复有符号 advantage。exact-v1 的机制定位为 `§3.3 Advantage Collapse；§4.2.1 Reward Function；§4.2.2 Guided Advantage Estimator`，评价定位为 `§5 Experimental Setup；§5.2 Main Results；§5.3 Comparison with Other Advantage Estimators`，限制或反证定位为 `§5.4 Ablation Studies；Appendix: hyperparameter and safety discussion`。

机制证据摘要：标准 group normalization 在全零或全一 reward group 中产生近零优势。GuAE 只把 reward 边界 0/1 加入均值和方差统计，不把 anchors 当作 rollout；真实样本因而在全零组得到同号负优势、在全一组得到同号正优势，再由 variance-adaptive tempering 调整尺度。SFT 阶段另以证据缺失或冲突样本训练 abstention。

评价证据摘要：作者在 Qwen3-VL-8B-Instruct、LLaMA-Factory/EasyR1 与 General/Trap GUI 数据切片上报告 Stage I/II 结果；摘要中的 Trap SR 13.88%→80.21% 只属于该模型、奖励与扰动合同。与 DAPO、GSPO、REINFORCE++ 的比较不能外推为一般 GRPO 优势。

限制证据摘要：锚点要求已知且有意义的 reward 边界；它只恢复 group-level 同号更新，不能创造相同 rollout 间的排序信息。规则式 thought-action reward、group size、tempering 超参和 GUI schema 都可能引入偏差；更强正向更新也可能把全组共同错误放大。

采用边界：exact-v1 支持 Qwen3-VL-8B 的作者 GUI/RFT 设置，不证明 anchor-normalized advantage 对其他 reward 范围、模型、环境或 production SLO 普遍有效；它也不证明同 reward rollout 之间存在可识别排序。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent post-write review complete`，目标 owner 为 `TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md)；现有覆盖差异：现有命题只覆盖“换 group membership”这条路径；未覆盖在无法或不宜补采时，通过固定 reward 边界改变 estimator 统计、保留 collapsed group 并接受有偏同号更新的替代分支。最终处置已通过独立复核。

### [Visual Implicit Autoregressive Modeling](https://arxiv.org/html/2605.01220v1)

准入时需核验的设计变化是：隐式 equilibrium layer 将视觉 AR 的训练内存与推理迭代预算解耦为可调计算状态。exact-v1 的机制定位为 `2.2 Deep Equilibrium Models`，评价定位为 `4.1 Experimental Setup；4.2 Main Results`，限制或反证定位为 `5 Conclusion`。

机制证据摘要：DEQs replace explicit deep stacks with an implicit fixed‑point layer trained via implicit or Jacobian‑free differentiation, enabling constant‑memory backpropagation and adaptive compute ( Bai et al., 2019 ) . Subsequent work extends this framework with hierarchical operators and scale‑coupled equilibria, improving both optimization stability and representational capacity ( Bai et al., 2020 ) . Jacobian‑Free Backpropagation (JFB) provides a practical 1‑step gradient through a single unrolled iteration, with subsequ…

评价证据摘要：We implement VIAR on a 2B‑parameter VAR with the original multi‑scale VQVAE tokenizer ( Tian et al., 2024 ; Razavi et al., 2019 ) . The tokenizer is frozen during AR training. Each scale uses three modules: pre-layers, an implicit layer, and post-layers. All share the same transformer block design except for the implicit layer adds one projection for input injection. We set p = 5 p=5 blocks for both pre-layers and post-layers. We adopt S-JFB with N = 10 N=10 no‑grad and M = 12 M=12 with‑grad iterations by default…

限制证据摘要：We presented VIAR, a visual autoregressive framework that replaces VAR’s deep explicit middle stack with a single implicit equilibrium layer trained via Jacobian-Free Backpropagation, and that leverages per‑scale iteration schedules to control compute across scales. This design delivers two practical advantages: constant‑memory backpropagation during training and flexible, budget‑aware inference. Empirically, VIAR a…

采用边界：机制锚点为 2.2 Deep Equilibrium Models；评价锚点为 4.1 Experimental Setup, 4.2 Main Results。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；最终处置已通过独立复核。

### [FP-Agent: Fingerprinting AI Browsing Agents](https://arxiv.org/html/2605.01247v1)

准入时需核验的设计变化是：浏览 Agent 的行为 fingerprint 比共享浏览器指纹更能支持运行时识别与控制。exact-v1 的机制定位为 `3.1. Bot Measurement Studies；4. Methodology`，评价定位为 `3.1. Bot Measurement Studies；4.7. Analysis Methodology；5.1. Classifier Evaluation`，限制或反证定位为 `6. Discussion, Limitations, and Implications；7. Conclusion`。

采用边界：机制锚点为 3.1. Bot Measurement Studies, 4. Methodology；评价锚点为 3.1. Bot Measurement Studies, 4.7. Analysis Methodology, 5.1. Classifier Evaluation。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor；比较：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“浏览 Agent 的行为 fingerprint 比共享浏览器指纹更能支持运行时识别与控制”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Activation Compression in LLMs: Theoretical Analysis and Efficient Algorithm](https://arxiv.org/html/2605.01255v1)

准入时需核验的设计变化是：只对满足无偏条件的线性算子压缩 activation，并复用低秩因子压缩梯度。exact-v1 的机制定位为 `Memory Reduction for Gradients and Optimizer States.；Activation Memory Reduction Methods and Theory.`，评价定位为 `Activation Compression in LLMs: Theoretical Analysis and Efficient Algorithm；5 Experiments and Analysis；Experimental Setup`，限制或反证定位为 `6 Conclusion`。

采用边界：机制锚点为 Memory Reduction for Gradients and Optimizer States., Activation Memory Reduction Methods and Theory.；评价锚点为 Activation Compression in LLMs: Theoretical Analysis and Efficient Algorithm, 5 Experiments and Analysis, Experimental Setup。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)；现有命题：资源可用性、通信完成与全局更新语义必须共同进入一轮训练合同；比较：现有命题已经规定：资源可用性、通信完成与全局更新语义必须共同进入一轮训练合同。本来源的受限增量是“只对满足无偏条件的线性算子压缩 activation，并复用低秩因子压缩梯度”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Chain of Evidence: Pixel-Level Visual Attribution for Iterative Retrieval-Augmented Generation](https://arxiv.org/html/2605.01284v1)

准入时需核验的设计变化是：把多跳 RAG 的证据 owner 从文本引用细化到页面截图的 pixel bounding boxes。exact-v1 的机制定位为 `3.1. Motivation and Design Principles；3.2. Dataset Construction`，评价定位为 `5. Experiment Setup；5.2. Evaluation Metrics；5.4. Model Implementation`，限制或反证定位为 `7. Conclusion`。

采用边界：机制锚点为 3.1. Motivation and Design Principles, 3.2. Dataset Construction；评价锚点为 5. Experiment Setup, 5.2. Evaluation Metrics, 5.4. Model Implementation。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `AGENT-RAG` / [Ch76](../../../../books/part-07-agent/76-rag.md)；现有命题：检索相关性、证据充分性、freshness 与 provenance 是不同 gate；比较：现有命题已经规定：检索相关性、证据充分性、freshness 与 provenance 是不同 gate。本来源的受限增量是“把多跳 RAG 的证据 owner 从文本引用细化到页面截图的 pixel bounding boxes”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [A Theory of Saddle Escape in Deep Nonlinear Networks](https://arxiv.org/html/2605.01288v1)

准入时需核验的设计变化是：深层非线性网络的 saddle escape 由 bottleneck-scale 层数而非总深度控制。exact-v1 的机制定位为 `2 Imbalance Identity and Activation Classes；Theorem 1 (Imbalance identity).`，评价定位为 `Proof sketch.；Appendix A Proof and Extension of Theorem 1；Proof.`，限制或反证定位为 `6 Discussion`。

机制证据摘要：Before proceeding to the scalar reduction of the gradient flow ODE, we present an exact identity that holds for the full network, for any smooth activation, and for any differentiable loss. It controls the evolution of the layer imbalance Δ l ≐ ‖ W l + 1 ‖ F 2 − ‖ W l ‖ F 2 \Delta_{l}\doteq\\|W_{l+1}\\|_{F}^{2}-\\|W_{l}\\|_{F}^{2} and identifies a functional of the activation that dictates whether layer norms are conserved, drift at cubic order, or drift at quadratic order. Let σ ∈ C 1 ​ ( ℝ ) \sigma\in C^{1}(\mat…

评价证据摘要：Separability of eq. 8 gives eq. 9 . For the leading-order statement, Φ ⁡ ( U , D ) = K ( σ ) ​ ( 1 + O ⁡ ( U q − 1 ) ) \Phi(U,D)=K^{(\sigma)}(1+O(U^{q-1})) , so on U ∈ [ U 0 , 1 ] U\in[U_{0},1] with U 0 = O ⁡ ( ε ) U_{0}=O(\varepsilon) the multiplicative error Φ / K ( σ ) − 1 \Phi/K^{(\sigma)}-1 is pointwise O ⁡ ( U q − 1 ) O(U^{q-1}) . Integrating against the dominant ( L − 2 ) (L-2) -form gives a relative correction that is o ⁡ ( 1 ) o(1) except when the U q − 1 U^{q-1} factor in Φ \Phi exactly cancels the U L −…

限制证据摘要：We have shown that the homogeneity deficit φ σ ​ ( z ) = z ​ σ ′ ​ ( z ) − σ ⁡ ( z ) \varphi_{\sigma}(z)=z\sigma^{\prime}(z)-\sigma(z) classifies activations into four regimes and controls escape from the zero saddle. On the symmetric submanifold the matrix flow reduces to a one-dimensional integral; off the manifold at He-normal init, a signal-energy argument on γ ⁡ ( W ) = 𝔼 ⁡ [ f ​ g ] \gamma(W)=\mathbb{E}[fg] yi…

采用边界：机制锚点为 2 Imbalance Identity and Activation Classes, Theorem 1 (Imbalance identity).；评价锚点为 Proof sketch., Appendix A Proof and Extension of Theorem 1, Proof.。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；最终处置已通过独立复核。

### [Lifting Traces to Logic: Programmatic Skill Induction with Neuro-Symbolic Learning for Long-Horizon Agentic Tasks](https://arxiv.org/html/2605.01293v1)

准入时需核验的设计变化是：轨迹归纳只有被提升为带控制流、动态变量绑定和可执行符号状态的 skill program，才能把 neural proposal 与环境执行权分离。。exact-v1 的机制定位为 `§4 Skill Representation；§4.2 Neuro-symbolic node invention；§4.3 Interactive execution；§5 Skill induction`，评价定位为 `§6 Experiments；long-horizon task success and skill-transfer evaluation`，限制或反证定位为 `trace-derived empirical consistency does not replace live-environment verification`。

机制证据摘要：Foundation model-driven agents often struggle with long-horizon planning due to the transient nature of purely prompting-based reasoning. While existing skill induction methods mitigate this by distilling experience into state-blind parameterized scripts, they fail to capture the conditional logic required for robust execution in dynamic environments. In this paper, we propose Neuro-Symbolic Skill Induction (NSI), a framework that lifts interaction traces into modular, \textit{logic-grounded} programs. By synthesi…

评价证据摘要：Foundation model-driven agents often struggle with long-horizon planning due to the transient nature of purely prompting-based reasoning. While existing skill induction methods mitigate this by distilling experience into state-blind parameterized scripts, they fail to capture the conditional logic required for robust execution in dynamic environments. In this paper, we propose Neuro-Symbolic Skill Induction (NSI), a framework that lifts interaction traces into modular, \textit{logic-grounded} programs. By synthesi…

限制证据摘要：只支持 exact-v1 披露的任务、模型、环境和 evaluator；未披露的跨域、生产与长期稳定性不得外推。

采用边界：轨迹归纳只有被提升为带控制流、动态变量绑定和可执行符号状态的 skill program，才能把 neural proposal 与环境执行权分离。 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `AGENT-PLATFORM` / [Ch84](../../../../books/part-07-agent/84-agent-platform.md)；现有命题：skill、run、tool effect 与 release/rollback 必须保持独立身份；比较：现有命题已经规定：skill、run、tool effect 与 release/rollback 必须保持独立身份。本来源的受限增量是“轨迹归纳只有被提升为带控制流、动态变量绑定和可执行符号状态的 skill program，才能把 neural proposal 与环境执行权分离。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Checkerboard: A Simple, Effective, Efficient and Learning-free Clean Label Backdoor Attack with Low Poisoning Budget](https://arxiv.org/html/2605.01298v1)

准入时需核验的设计变化是：闭式、data-independent clean-label trigger 将供应链攻击从 surrogate 训练依赖中解耦。exact-v1 的机制定位为 `3. Method；3.1. Threat Model；3.2. Problem Formulation`，评价定位为 `4. Evaluation；4.1. Experimental Setup；4.3. Ablation Study`，限制或反证定位为 `3.1. Threat Model；6. Discussion & Conclusion`。

采用边界：机制锚点为 3. Method, 3.1. Threat Model, 3.2. Problem Formulation；评价锚点为 4. Evaluation, 4.1. Experimental Setup, 4.3. Ablation Study。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor；比较：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“闭式、data-independent clean-label trigger 将供应链攻击从 surrogate 训练依赖中解耦”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [From Stealthy Data Fabrication to Unsafe Driving: Realistic Scenario Attacks on Collaborative Perception](https://arxiv.org/html/2605.01301v1)

准入时需核验的设计变化是：对共享感知结果的微小 pose 篡改会沿 tracking 与 prediction 数据流放大为不安全控制。exact-v1 的机制定位为 `4. Threat Model；5. Design of Attack and Mitigation；5.1.1. Problem Formulation`，评价定位为 `6. Evaluation；6.1. Experimental Setup；6.2. Perception Attack Results`，限制或反证定位为 `4. Threat Model；5.3.3. Discussion；7. Conclusion`。

采用边界：机制锚点为 4. Threat Model, 5. Design of Attack and Mitigation, 5.1.1. Problem Formulation；评价锚点为 6. Evaluation, 6.1. Experimental Setup, 6.2. Perception Attack Results。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；现有命题：行动闭环必须绑定 observation、action schema、控制频率与安全回退；比较：现有命题已经规定：行动闭环必须绑定 observation、action schema、控制频率与安全回退。本来源的受限增量是“对共享感知结果的微小 pose 篡改会沿 tracking 与 prediction 数据流放大为不安全控制”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Beyond Semantic Relevance: Counterfactual Risk Minimization for Robust Retrieval-Augmented Generation](https://arxiv.org/html/2605.01302v1)

准入时需核验的设计变化是：把检索目标从 semantic relevance 改为对错误前提与确认偏误的 counterfactual decision risk，并由 Evidence Critic 产生 robustness score 与 abstention 控制。。exact-v1 的机制定位为 `Counterfactual Risk Minimization；Cognitive Perturbation Protocol；Evidence Critic`，评价定位为 `decision-making benchmarks；adversarial query settings；critic and abstention ablations`，限制或反证定位为 `benchmark-bound cognitive perturbations；learned critic calibration；threshold transfer not established`。

机制证据摘要：训练时对 query 注入认知偏误扰动，以文档能否在干预后仍把决策推向正确方向定义效用，再蒸馏轻量 Evidence Critic。在线阶段 critic 对候选证据打 robustness 分，并与风险阈值共同决定采用或拒答。

评价证据摘要：实验比较 dense retriever 与 LLM reranker，在作者构造的 decision/adversarial query benchmark 上报告鲁棒性和 risk-aware abstention 改善；消融支持 perturbation、critic 和 threshold 在该设置中的贡献。

限制证据摘要：偏误类型、counterfactual 构造、正确答案和 critic 共享同一实验合同；结果没有证明新 corpus、领域、语言或真实恶意用户上的校准，固定阈值也不是生产常数。

采用边界：来源支持 relevance 在带偏 query 下可能系统性选择迎合性证据，并支持 counterfactual robustness 作为独立检索信号；不证明 critic score 是事实概率或可替代原始证据核验。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent post-write review complete`，目标 owner 为 `AGENT-RAG` / [Ch76](../../../../books/part-07-agent/76-rag.md)；现有覆盖差异：现有覆盖与 exact-v1 对读后仍缺：在 relevance 与 sufficiency 之间增加 query-robustness gate：旧 top-k 在 query 前提可信时仍合理；当前提可能错误或带确认偏误时，retriever 应把候选在 counterfactual query perturbation 下能否维持决策支持作为独立信号。Critic 只提出 evidence-risk proposal，原始 source 与 answer gate 仍拥有事实和提交权。该分支以额外扰动数据、critic 校准和更多 abstention 换取对迎合性检索的抵抗；critic 漂移、偏误模板覆盖不足或高风险结论时回退多源原文核验/人工。exact-v1 只证明作者 decision benchmarks 和扰动合同中的结果，不提供跨 corpus 固定阈值。最终处置已通过独立复核。

### [The Partial Testimony of Logs: Evaluation of Language Model Generation under Confounded Model Choice](https://arxiv.org/html/2605.01311v1)

准入时需核验的设计变化是：只有随机实验与离线 simulator 联合才能识别混杂日志中的因果模型价值。exact-v1 的机制定位为 `Marginal model value.；Context-conditional model value.`，评价定位为 `The Partial Testimony of Logs: Evaluation of Language Model Generation under Confounded Model Choice；Randomized experiment (EXP).；Proof sketch.`，限制或反证定位为 `7 Discussion and Future Work；Limitations and future work.；8 Conclusion`。

采用边界：机制锚点为 Marginal model value., Context-conditional model value.；评价锚点为 The Partial Testimony of Logs: Evaluation of Language Model Generation under Confounded Model Choice, Randomized experiment (EXP)., Proof sketch.。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-TRACE` / [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md)；现有命题：trace 只能形成带 provenance 的因果候选，不能自动取得裁决权；比较：现有命题已经规定：trace 只能形成带 provenance 的因果候选，不能自动取得裁决权。本来源的受限增量是“只有随机实验与离线 simulator 联合才能识别混杂日志中的因果模型价值”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Segment-Aligned Policy Optimization for Multi-Modal Reasoning](https://arxiv.org/html/2605.01327v1)

准入时需核验的设计变化是：把 token-level policy MDP 提升为推理 segment MDP，并按自适应分段计算 value、advantage 与 importance ratio。exact-v1 的机制定位为 `4 Method；4.1.1 Step-wise MDP Formulation；4.2 Entropy-based Adaptive Segmentation Mechanism`，评价定位为 `5 Experiment；5.1 Experimental Setups；5.2 Main Results`，限制或反证定位为 `6 Conclusion`。

机制证据摘要：To address the mismatch between existing policy optimization formulations and the step-wise structure of reasoning, we propose Segment-Aligned Policy Optimization (SAPO), treating reasoning steps, rather than individual tokens or entire sequences, as the fundamental units of policy optimization, which allows reasoning to be modeled as a step-wise Markov decision process. We illustrate SAPO in Fig. 2 and present a pseudo-code implementation in Algorithm. 1 . We model the reasoning process as a step-wise Markov deci…

评价证据摘要：Table 1 : Performance comparison of Qwen2.5-VL models trained with different reinforcement learning strategies on six multi-modal reasoning benchmarks. Benchmark Geo3K LogicVista MathVerse WeMath MathVista DynaMath Avg. 3B Models Qwen2.5-VL-3B 27.29 34.45 24.75 21.81 61.60 10.97 30.15 +GRPO 40.60 40.72 36.67 29.43 63.00 17.37 37.97 +PPO 21.80 39.15 26.52 25.90 63.80 9.98 31.19 +VC-PPO 34.94 37.81 32.36 32.67 62.90 10.78 35.24 +SAPO 46.26 39.60 37.56 36.19 65.40 16.37 40.23 7B Models Qwen2.5-VL-7B 42.60 39.15 30.58…

限制证据摘要：In this work, we analyzed the limitations of existing reinforcement learning approaches for reasoning in MLLMs and identified a fundamental mismatch between their optimization granularity and the step-wise structure of reasoning. To address this issue, we proposed Segment-Aligned Policy Optimization (SAPO), which aligns value estimation, advantage computation, and policy updates with reasoning steps under a step-wis…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md)；现有覆盖差异：现有正文仍缺：把 token-level policy MDP 提升为推理 segment MDP，并按自适应分段计算 value、advantage 与 importance ratio。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。最终处置已通过独立复核。

### [Don’t Be a Pot Stirrer! Authorized Vector Data Retrieval via Access-Aware Indexing](https://arxiv.org/html/2605.01342v1)

准入时需核验的设计变化是：access-aware lattice 让向量索引、存储预算与授权 query plan 共同决定检索。exact-v1 的机制定位为 `Theorem 4.2 (Correctness of Greedy Copy Phase).；Theorem 4.3 (Correctness of Merge Phase).；Theorem 5.2 (Node Purity after Copying).`，评价定位为 `Proof.；7. Evaluations；7.2. Index Creation Evaluation`，限制或反证定位为 `9. Conclusion`。

机制证据摘要：Let ℒ t \mathcal{L}_{t} be the lattice after t t greedy copy operations. Then: (1) Monotonicity: AvgCost ​ ( Q , ℐ ⁡ ( ℒ t ) ) ≤ AvgCost ​ ( Q , ℐ ⁡ ( ℒ t − 1 ) ) \textsf{AvgCost}(Q,\mathcal{I}(\mathcal{L}_{t}))\leq\textsf{AvgCost}(Q,\mathcal{I}(\mathcal{L}_{t-1})) . (2) Budget Safety: \| ℒ t \| \| ℒ 𝑒𝑥 \| ≤ β \tfrac{\|\mathcal{L}_{t}\|}{\|\mathcal{L}_{\mathit{ex}}\|}\leq\beta . (3) Termination: the phase halts when no e e satisfies Equation 4 . Algorithm 2 Veda - Copy 1: ℒ 𝑒𝑥 \mathcal{L}_{\mathit{ex}} : the exclu…

评价证据摘要：Since τ j ⊂ τ \tau_{j}\subset\tau , any query for r ∈ τ j r\in\tau_{j} also requires N c ​ ( τ ) N_{c}(\tau) , whose data now resides in N a ​ ( τ j ) N_{a}(\tau_{j}) . Roles τ ∖ τ j \tau\setminus\tau_{j} are covered by disjoint ancestors N a ​ ( τ j ′ ) ∈ P c N_{a}(\tau_{j^{\prime}})\in\textsf{P}_{c} , so purity holds for every role. ∎ Selecting a Valid Partition. A node N c ​ ( τ ) N_{c}(\tau) may admit many valid partitions. EffVeda scores each one and picks the best. Because every ancestor in a valid partition…

限制证据摘要：We presented Veda and EffVeda , two access-aware indexing strategies for vector databases. Both partition data by role combination, organize the resulting blocks in an access-aware lattice, and use copy and merge operations to group co-accessed blocks under a storage budget. Large lattice nodes are indexed with HNSW, while small nodes are scanned linearly. For each role, the methods build a query plan that covers it…

采用边界：机制锚点为 Theorem 4.2 (Correctness of Greedy Copy Phase)., Theorem 4.3 (Correctness of Merge Phase)., Theorem 5.2 (Node Purity after Copying).；评价锚点为 Proof., 7. Evaluations, 7.2. Index Creation Evaluation。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `AGENT-RAG` / [Ch76](../../../../books/part-07-agent/76-rag.md)；现有命题：检索相关性、证据充分性、freshness 与 provenance 是不同 gate；比较：现有命题已经规定：检索相关性、证据充分性、freshness 与 provenance 是不同 gate。本来源的受限增量是“access-aware lattice 让向量索引、存储预算与授权 query plan 共同决定检索”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [The Perceptual Bandwidth Bottleneck in Vision-Language Models: Active Visual Reasoning via Sequential Experimental Design](https://arxiv.org/html/2605.01345v1)

准入时需核验的设计变化是：把高分辨率视觉推理改写为固定 token 带宽下的顺序 evidence acquisition，controller 在回答前主动选择下一块视觉观测。。exact-v1 的机制定位为 `sequential Bayesian optimal experimental design；coverage-resolution proxy；FOVEA evidence-oriented probing`，评价定位为 `high-resolution visual benchmarks；remote-sensing search tasks；direct/ReAct baselines`，限制或反证定位为 `ideal-observer approximation；backbone hallucination；stochastic latency and adaptive invocation`。

机制证据摘要：S-BOED 把视野覆盖与局部分辨率的冲突写成序贯实验设计；FOVEA 先用低分辨率全局视图形成假设，再根据 evidence-oriented probe 选择高分辨率 crop，直到预算或停止条件满足。

评价证据摘要：作者在高分辨率 benchmark，尤其 search-dominated remote-sensing tasks 上比较直接输入和 ReAct-style baseline，报告训练外主动 crop 的一致收益；结果绑定其 VLM、crop budget 与 proxy objective。

限制证据摘要：论文明确讨论 ideal-observer 假设、backbone hallucination、连续空间近似和随机 latency；adaptive invocation 仍属未来工作，未证明 crop policy 能识别所有关键证据或满足实时 SLO。

采用边界：证据支持在固定视觉 token 预算下把 observation acquisition 作为可审计的顺序控制问题；不证明 crop proposal 是充分证据，也不覆盖开放世界视觉安全。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent post-write review complete`，目标 owner 为 `MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；现有覆盖差异：现有覆盖与 exact-v1 对读后仍缺：把固定视觉输入扩展为 bounded active-observation 分支：全局低分辨率视图先保留 context，acquisition policy 依据当前未决 claim 选择下一 crop，evidence assembler 记录坐标、尺度、采集顺序与 budget，answer gate 决定继续、提交或拒答。旧的一次性均匀采样在低分辨率已足够或 latency 严格时仍更稳；主动采集用细节可见性换额外调用、路径依赖、漏区与尾延迟。Selector 只拥有 observation proposal，不拥有 evidence sufficiency；exact-v1 结果限作者 VLM、crop proxy 和高分辨率 benchmark。最终处置已通过独立复核。

### [CHASE: Competing Hypotheses for Ambiguity-Aware Selective Prediction](https://arxiv.org/html/2605.01346v1)

准入时需核验的设计变化是：在部分可观测冲突中比较竞争解释的 margin 决定 commit 或 abstain，而非依赖单分支置信度。exact-v1 的机制定位为 `3 Method；4.1 GUV-Inspired Simulator Design；Features, ambiguity, and dataset splits.`，评价定位为 `Evaluation metrics.`，限制或反证定位为 `6 Discussion and Limitations；8 Conclusion`。

采用边界：机制锚点为 3 Method, 4.1 GUV-Inspired Simulator Design, Features, ambiguity, and dataset splits.；评价锚点为 Evaluation metrics.。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“在部分可观测冲突中比较竞争解释的 margin 决定 commit 或 abstain，而非依赖单分支置信度”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [MAD-OPD: Breaking the Ceiling in On-Policy Distillation via Multi-Agent Debate](https://arxiv.org/html/2605.01347v1)

准入时需核验的设计变化是：让多个教师在学生 on-policy state 上辩论形成 privileged distribution，并按任务选择 JSD 或 reverse-KL、按 agent step 稳定蒸馏。exact-v1 的机制定位为 `3 Preliminaries and Divergence Analysis；4 Method: MAD-OPD；5.4 Component and Divergence Analysis`，评价定位为 `5 Experiments；5.1 Experimental Setup；5.2 Main Results`，限制或反证定位为 `6 Discussion and Conclusion；Limitations.`。

机制证据摘要：MAD-OPD translates the task-adaptive divergence principle of Sec. 3.3 into a concrete training pipeline (Figure 2 ). Sec. 4.1 produces the privileged information c c that Eq. 1 requires via inter-teacher debate; Sec. 4.2 aggregates teachers by post-debate confidence; Sec. 4.3 writes the resulting task-adaptive loss; Sec. 4.4 presents OPAD, an OPD-based training method for agentic tasks that brings step-level environment interaction. (RQ3) Takeaway 3: MAD-OPD ’s components are non-redundant. Figure 4 (a) (full numb…

评价证据摘要：We evaluate MAD-OPD across six teacher–student configurations, two model families, and five benchmarks. Four research questions guide the analysis: (RQ1) Does debate break the single-teacher capability ceiling? (RQ2) How do gains scale across teacher–student capability? (RQ3) Do debate and confidence weighting yield strictly non-redundant gains over naive on-policy aggregation? (RQ4) Do divergences behave as the theory of Sec. 3.3 predicts? We evaluate MAD-OPD on two model families, Qwen3 [ 37 ] and Qwen3.5, acros…

限制证据摘要：We presented MAD-OPD , a multi-teacher debate framework for on-policy distillation paired with OPAD for stable multi-step agentic training, and a task-adaptive divergence principle (JSD for agentic OPD, reverse KL for code). Across six teacher–student configurations and five benchmarks, MAD-OPD ranks first in every configuration; a 4B student trained under the 14B+8B teacher debate even exceeds its 14B teacher on LC…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md)；现有覆盖差异：现有正文仍缺：让多个教师在学生 on-policy state 上辩论形成 privileged distribution，并按任务选择 JSD 或 reverse-KL、按 agent step 稳定蒸馏。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。最终处置已通过独立复核。

### [VUDA: Breaking CUDA-Vulkan Isolation for Spatial Sharing of Compute and Graphics on the Same GPU](https://arxiv.org/html/2605.01352v1)

准入时需核验的设计变化是：打破 CUDA/Vulkan context 隔离，使仿真 compute 与 graphics 可空间复用同一 GPU。exact-v1 的机制定位为 `4. System Mechanisms`，评价定位为 `5. Implementation；6. Evaluation；6.1. Experimental Setup`，限制或反证定位为 `8. Conclusion`。

采用边界：机制锚点为 4. System Mechanisms；评价锚点为 5. Implementation, 6. Evaluation, 6.1. Experimental Setup。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-GPU-SCHEDULER` / [Ch63](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)；现有命题：GPU placement 必须消费版本化 workload 和资源约束，而不是同质标量；比较：现有命题已经规定：GPU placement 必须消费版本化 workload 和资源约束，而不是同质标量。本来源的受限增量是“打破 CUDA/Vulkan context 隔离，使仿真 compute 与 graphics 可空间复用同一 GPU”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Focus on the Core: Empowering Diffusion Large Language Models by Self-Contrast](https://arxiv.org/html/2605.01373v1)

准入时需核验的设计变化是：用相邻 denoising step 的 top-K 分布差识别高动态 token，并对其自对比重掩码，集中迭代修正预算。exact-v1 的机制定位为 `2 An Exploratory Analysis on DLMs；3 Methodology；4.3 Ablation Study and Analysis`，评价定位为 `4 Experiments；4.1 Experimental Setup；4.2 Main Results`，限制或反证定位为 `5 Conclusion；E.2 Effect of Parallel Token Budget mm on the Speedup–Accuracy Trade-off；Appendix G Limitations`。

机制证据摘要：In this section, we present our methodology by answering two questions: (1) how can HD tokens be accurately identified, and (2) how can they be leveraged to improve performance and efficiency? Effect of ω \omega As illustrated in Figure 6 (a), the model demonstrates strong robustness to guidance scale across both datasets, maintaining stable performance over a broad range of values. The guidance scale fundamentally governs the trade-off between exploration and exploitation during the search process: an excessively…

评价证据摘要：Datasets and Backbones To comprehensively evaluate the proposed approach, we conduct experiments across six widely adopted benchmarks covering mathematical reasoning, code generation, and logical reasoning tasks. Specifically, for mathematical reasoning, we utilize GSM8K ( Cobbe et al., 2021 ) and MATH500 ( Hendrycks et al., 2021 ) . For code generation, we employ HumanEval ( Chen et al., 2021 ) and MBPP ( Austin et al., 2021b ) . For logical reasoning, we evaluate on SVAMP ( Patel et al., 2021 ) and Countdown ( G…

限制证据摘要：This work uncovers a critical yet long-overlooked property of DLMs: the heterogeneous information density distribution inherent in the generated context. Through systematic investigation of high-information-density (HD) tokens, we demonstrate their central role in both semantic guidance and decoding acceleration. Specifically, FoCore steers generation by exploiting HD tokens in a training-free, self-contrastive mann…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；现有覆盖差异：现有正文仍缺：用相邻 denoising step 的 top-K 分布差识别高动态 token，并对其自对比重掩码，集中迭代修正预算。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。最终处置已通过独立复核。

### [MTA: Multi-Granular Trajectory Alignment for Large Language Model Distillation](https://arxiv.org/html/2605.01374v1)

准入时需核验的设计变化是：沿教师与学生的层级 transformation trajectory 对齐 token、span 和 hidden representation，而非只对齐末端 logits。exact-v1 的机制定位为 `3 Methodology；5 Analysis；Synergy of the Full Method.`，评价定位为 `4 Experiments；4.1 Experimental Setup；Training and Evaluation Settings.`，限制或反证定位为 `6 Conclusion；7 Limitations`。

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `No Change — Existing Coverage (proposition comparison; independent review required)`，目标 owner 为 `TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md)；现有命题：本章已区分 output、feature 与 trajectory distillation，并要求层映射和表示损失受限；MTA 是受限实例；比较：exact-v1 的新增证据是“沿教师与学生的层级 transformation trajectory 对齐 token、span 和 hidden representation，而非只对齐末端 logits”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。最终处置已通过独立复核。

### [MemORAI: Memory Organization and Retrieval via Adaptive Graph Intelligence for LLM Conversational Agents](https://arxiv.org/html/2605.01386v1)

准入时需核验的设计变化是：长期记忆的过滤、turn-level provenance graph 与 query-adaptive retrieval 是同一 lifecycle 的不同状态；高连接度不能替代 query-specific evidence relevance。。exact-v1 的机制定位为 `§3.1 Selective Compression；§3.2 Provenance-Enriched Graph；§3.3 Query-Adaptive Subgraph Retrieval`，评价定位为 `§4.1 Experimental Settings；§4.2 Main Results；§4.3 Ablation；Appendix B cost and robustness`，限制或反证定位为 `LongMemEval/LoCoMo, one generation backbone and GPT-4o-judge scope`。

机制证据摘要：Large Language Models (LLMs) lack persistent memory for long-term personalized conversations. Existing graph-based memory systems suffer from information dilution, absent provenance tracking, and uniform retrieval that ignores query context. We introduce MemORAI (Memory Organization and Retrieval via Adaptive Graph Intelligence), a framework that integrates three innovations: selective memory filtering with dual-layer compression to retain user-persona-relevant content, a provenance-enriched multi-relational graph…

评价证据摘要：Large Language Models (LLMs) lack persistent memory for long-term personalized conversations. Existing graph-based memory systems suffer from information dilution, absent provenance tracking, and uniform retrieval that ignores query context. We introduce MemORAI (Memory Organization and Retrieval via Adaptive Graph Intelligence), a framework that integrates three innovations: selective memory filtering with dual-layer compression to retain user-persona-relevant content, a provenance-enriched multi-relational graph…

限制证据摘要：只支持 exact-v1 披露的任务、模型、环境和 evaluator；未披露的跨域、生产与长期稳定性不得外推。

采用边界：长期记忆的过滤、turn-level provenance graph 与 query-adaptive retrieval 是同一 lifecycle 的不同状态；高连接度不能替代 query-specific evidence relevance。 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)；现有命题：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner；比较：现有命题已经规定：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner。本来源的受限增量是“长期记忆的过滤、turn-level provenance graph 与 query-adaptive retrieval 是同一 lifecycle 的不同状态；高连接度不能替代 query-specific evidence relevance。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [LiveFMBench: Unveiling the Power and Limits of Agentic Workflows in Specification Generation](https://arxiv.org/html/2605.01394v1)

准入时需核验的设计变化是：形式规约评测必须同时验证 code/spec faithfulness、时间污染与 verifier 非空洞性；自动 prover 通过不能单独构成成功。。exact-v1 的机制定位为 `§2 Study Design；§3 Benchmark Construction；§4.2.1 Faithfulness`，评价定位为 `§4.1 Experiment Setup；§4.4 Agentic Pipeline；§4.5 Failure Analysis`，限制或反证定位为 `§6 Threats to Validity`。

机制证据摘要：Formal specification is essential for rigorous program verification, yet writing correct specifications remains costly and difficult to automate. Although large language models (LLMs) and agents have shown promising progress, their true capabilities and failure modes remain unclear. We present the first systematic and contamination-aware study of LLM- and agent-based formal specification generation for C programs. We introduce LiveFMBench, a continuously evolving benchmark of 630 ACSL (ANSI/ISO C Specification Lan…

评价证据摘要：Formal specification is essential for rigorous program verification, yet writing correct specifications remains costly and difficult to automate. Although large language models (LLMs) and agents have shown promising progress, their true capabilities and failure modes remain unclear. We present the first systematic and contamination-aware study of LLM- and agent-based formal specification generation for C programs. We introduce LiveFMBench, a continuously evolving benchmark of 630 ACSL (ANSI/ISO C Specification Lan…

限制证据摘要：只支持 exact-v1 披露的任务、模型、环境和 evaluator；未披露的跨域、生产与长期稳定性不得外推。

采用边界：形式规约评测必须同时验证 code/spec faithfulness、时间污染与 verifier 非空洞性；自动 prover 通过不能单独构成成功。 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“形式规约评测必须同时验证 code/spec faithfulness、时间污染与 verifier 非空洞性；自动 prover 通过不能单独构成成功。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [AI Safety as Control of Irreversibility: A Systems Framework for Decision-Energy and Sovereignty Boundaries](https://arxiv.org/html/2605.01415v1)

准入时需核验的设计变化是：把不可逆决策、物理资源动员与自我扩张权限分离为外部可审查的 sovereignty boundaries。exact-v1 的机制定位为 `3.1 System definition`，评价定位为 `Proof.；10 Empirical Implications and Testable Predictions`，限制或反证定位为 `9 Discussion；11 Conclusion`。

采用边界：机制锚点为 3.1 System definition；评价锚点为 Proof., 10 Empirical Implications and Testable Predictions。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor；比较：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“把不可逆决策、物理资源动员与自我扩张权限分离为外部可审查的 sovereignty boundaries”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Barriers to Counterfactual Credit Attribution for Autoregressive Models](https://arxiv.org/html/2605.01425v1)

准入时需核验的设计变化是：自回归输出的生成后 credit attribution 受不可辨识与组合搜索约束。exact-v1 的机制定位为 `Theorem (4.2, informal).；Theorem (4.3, informal).`，评价定位为 `Proof of Theorem 4.2.；Proof of Theorem 5.5.`，限制或反证定位为 `Not Disclosed as a standalone section`。

采用边界：机制锚点为 Theorem (4.2, informal)., Theorem (4.3, informal).；评价锚点为 Proof of Theorem 4.2., Proof of Theorem 5.5.。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“自回归输出的生成后 credit attribution 受不可辨识与组合搜索约束”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [SCALE-LoRA: Auditing Post-Retrieval LoRA Composition with Residual Merging and View Reliability](https://arxiv.org/html/2605.01429v1)

准入时需核验的设计变化是：在开放 LoRA 池检索后，以层级稀疏残差合并和多视图一致性审计决定组合、拒绝或回退。exact-v1 的机制定位为 `Problem Formulation；Method；Discussion and Analysis`，评价定位为 `Experiments；Experimental Setup；Evaluation metrics.`，限制或反证定位为 `Discussion and Analysis；Limitations；Conclusion`。

机制证据摘要：Not Disclosed in an independently titled section.

评价证据摘要：The experiments evaluate merge quality and view reliability in cross-task open-pool LoRA reuse under controlled and protocol-distinct settings. We report (i) matched FLAN-T5-Large results that isolate merge quality and view reliability under fixed retrieval and decoding conditions, (ii) ablations that separate LASRC, sparse-view construction, and support-aware aggregation, and (iii) decoder-only cross-backbone results under the LoGo-style BBH-8 protocol. We report normalized exact match (EM) as the primary metric,…

限制证据摘要：The primary causal comparison is tied to the matched FLAN-T5-Large, BBH, and 97-LoRA setting because that protocol fixes retrieval, support examples, decoding, and evaluation while changing the merge and reliability layers. The LLaMA, Qwen, and DeepSeek results provide protocol-distinct cross-backbone validation under the LoGo-style BBH-8 setting, but they use a different evaluation setup. We therefore distinguish p…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `TRAIN-LORA` / [Ch30](../../../../books/part-04-training-system/30-lora.md)；现有覆盖差异：现有正文仍缺：在开放 LoRA 池检索后，以层级稀疏残差合并和多视图一致性审计决定组合、拒绝或回退。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。最终处置已通过独立复核。

### [VisInject: Disruption != Injection -- A Dual-Dimension Evaluation of Universal Adversarial Attacks on Vision-Language Models](https://arxiv.org/html/2605.01449v1)

准入时需核验的设计变化是：将输出扰动与攻击者目标真正注入分开度量，反证单一 attack-success-rate 的安全结论。exact-v1 的机制定位为 `VisInject: Disruption ≠\neq Injection — A Dual-Dimension Evaluation of Universal Adversarial Attacks on Vision-Language Models；Foundational adversarial-attack methodology.；Evaluation methodology and benchmarks.`，评价定位为 `VisInject: Disruption ≠\neq Injection — A Dual-Dimension Evaluation of Universal Adversarial Attacks on Vision-Language Models；Evaluation methodology and benchmarks.；4.4 Stage 3 — dual-axis evaluation (our contribution)`，限制或反证定位为 `3 Threat Model；8.4 Limitations`。

机制证据摘要：Pang Liu Yingjie Lao Department of Electrical and Computer Engineering, Tufts University {pang.liu, yingjie.lao}@tufts.edu April 2026 Artifacts: GitHub Repo (Codes) · Dataset · Demo The optimisation primitives we use trace back to Goodfellow et al. (9) (FGSM, the original gradient-based image attack), Madry et al. (19) (PGD adversarial training, which we use without modification as our Stage-1 inner loop), and Moosavi-Dezfooli et al. (21) (the original “universal” framing — a single perturbation that fools many in…

评价证据摘要：Pang Liu Yingjie Lao Department of Electrical and Computer Engineering, Tufts University {pang.liu, yingjie.lao}@tufts.edu April 2026 Artifacts: GitHub Repo (Codes) · Dataset · Demo HarmBench ( 20 ) (ICML 2024) standardises evaluation across 18 18 attacks × \times 33 33 LLM/defenses with four behaviour categories. JailbreakBench ( 6 ) (NeurIPS 2024 D&B) provides an open evolving repo of 100 100 behaviours with leaderboard scoring. MM-SafetyBench ( 16 ) (ECCV 2024) extends to the multimodal setting with 5,040 5{,}0…

限制证据摘要：A user uploads an image to a multimodal assistant and asks a benign question (e.g. “describe this image” or “extract all text from this screenshot”). The attacker controls only the image pixels; the user prompt, the system prompt, and the model weights are off-limits. The attacker picks one short target phrase (a URL, a payment-information request, a piece of misinformation, etc.) before the attack begins. We declar…

采用边界：机制锚点为 VisInject: Disruption ≠\neq Injection — A Dual-Dimension Evaluation of Universal Adversarial Attacks on Vision-Language Models, Foundational adversarial-attack methodology., Evaluation methodology and benchmarks.；评价锚点为 VisInject: Disruption ≠\neq Injection — A Dual-Dimension Evaluation of Universal Adversarial Attacks on Vision-Language Models, Evaluation methodology and benchmarks., 4.4 Stage 3 — dual-axis evaluation (our contribution)。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；最终处置已通过独立复核。

### [Action Agent: Agentic Video Generation Meets Flow-Constrained Diffusion](https://arxiv.org/html/2605.01477v1)

准入时需核验的设计变化是：以可修订 goal video 作为高层 proposal，并由独立 controller 基于当前观测执行动作。exact-v1 的机制定位为 `§III Action Agent；§III-A Agentic Goal-Video Generation；§III-B Flow-Constrained Low-Level Controller`，评价定位为 `§IV Experiments；Simulation and real-world navigation results；Ablation studies`，限制或反证定位为 `Failure-case analysis；§V Limitations and Future Work`。

机制证据摘要：系统先由高层生成器把语言目标和初始图像变成 goal video，再由低层 flow-constrained controller 结合 goal video、当前观测和语言输出动作；生成阶段还使用 LLM 编排 prompt、video 与 evaluator 的迭代修订。

评价证据摘要：评测覆盖 50 个室内仿真导航任务与 G1、drone、wheeled embodiments；真实 G1 只有 17 次 open-loop 试验并报告 11/17 成功。视频质量阈值由模型 evaluator 给出，不是物理成功或安全证明。

限制证据摘要：作者明确列出尺度歧义、轨迹漂移和碰撞，并把硬件 closed-loop 作为后续工作；5–15 秒 clip、有限场景与 open-loop 证据不能证明真实闭环安全。

采用边界：exact-v1 只证明作者仿真与有限 open-loop G1 设置；goal-video evaluator 不拥有环境 transition truth，且不能把视觉质量分数当作 physical success、closed-loop robustness 或 safety guarantee。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；现有命题：高层 reasoning/imagination 只形成 action proposal；低层 controller、fresh observation 与 safety envelope 拥有执行、纠错和环境 transition 的提交边界；比较：该 two-stage navigation system 是现有高低层分工的具体案例；真实证据仍是 open-loop，且其尺度、漂移、碰撞失败恰好落在正文既有 freshness、calibration 与 closed-loop 边界内，没有改变长期命题。最终处置已通过独立复核。

### [OmniEncoder: See, Hear, and Feel Continuous Motion Like Humans With One Encoder](https://arxiv.org/html/2605.01506v1)

准入时需核验的设计变化是：以统一 token template、Omni-RoPE 和时窗移动联合编码视频、音频与运动连续性。exact-v1 的机制定位为 `2 Architecture`，评价定位为 `4 Experiment`，限制或反证定位为 `5 Conclusion`。

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `No Change — Existing Coverage (proposition comparison; independent review required)`，目标 owner 为 `MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；现有命题：本章已要求 modality identity、时间戳和窗口边界随 token 保留；该 encoder 没有改变统一空间与模态专属前端共存关系；比较：exact-v1 的新增证据是“以统一 token template、Omni-RoPE 和时窗移动联合编码视频、音频与运动连续性”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。最终处置已通过独立复核。

### [Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling](https://arxiv.org/html/2605.01566v1)

准入时需核验的设计变化是：多 Agent test-time scaling 的收益必须落在 token-cost/accuracy Pareto 前沿而非只看准确率。exact-v1 的机制定位为 `3 Method；4.1 Are multi-agent systems more compute- efficient than single-agent methods?；4.4 Are heavily scaled small models more compute-efficient than larger models?`，评价定位为 `4 Experiments；Appendix D Different Evaluation Setups；D.1 BBH Benchmark`，限制或反证定位为 `5 Conclusion；Limitations`。

采用边界：机制锚点为 3 Method, 4.1 Are multi-agent systems more compute- efficient than single-agent methods?, 4.4 Are heavily scaled small models more compute-efficient than larger models?；评价锚点为 4 Experiments, Appendix D Different Evaluation Setups, D.1 BBH Benchmark。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `AGENT-MULTI-AGENT` / [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；现有命题：消息、角色和局部成功不能替代共享状态的唯一提交语义；比较：现有命题已经规定：消息、角色和局部成功不能替代共享状态的唯一提交语义。本来源的受限增量是“多 Agent test-time scaling 的收益必须落在 token-cost/accuracy Pareto 前沿而非只看准确率”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Feedback-Normalized Developer Memory for Reinforcement-Learning Coding Agents: A Safety-Gated MCP Architecture](https://arxiv.org/html/2605.01567v1)

准入时需核验的设计变化是：Developer memory selection 是带 propensity 与延迟反馈的控制决策；确定性策略持有生产权，学习策略只能在 shadow/OPE gate 后进入 canary。。exact-v1 的机制定位为 `§2.3 Candidate features；§2.4 Deterministic decision surface；§2.7 Shadow learning；§2.8 OPE-gated rollout`，评价定位为 `§3.1 Experimental framework；§3.3 Controlled baselines；§3.4 Claim gate；§3.7 Operational cost`，限制或反证定位为 `§3.8 Residual failure family；§4 Discussion`。

机制证据摘要：Large language model (LLM) coding agents increasingly operate over repositories, terminals, tests, and execution traces across long software-engineering episodes. Persistent memory is useful, but static vector stores or generic retrieval-augmented generation (RAG) are insufficient for reinforcement-learning (RL) code development, where small details can alter Bellman targets, terminal masks, gradient flow, or validation claims. This paper presents RL Developer Memory, a local-first, Model Context Protocol (MCP)-na…

评价证据摘要：Large language model (LLM) coding agents increasingly operate over repositories, terminals, tests, and execution traces across long software-engineering episodes. Persistent memory is useful, but static vector stores or generic retrieval-augmented generation (RAG) are insufficient for reinforcement-learning (RL) code development, where small details can alter Bellman targets, terminal masks, gradient flow, or validation claims. This paper presents RL Developer Memory, a local-first, Model Context Protocol (MCP)-na…

限制证据摘要：只支持 exact-v1 披露的任务、模型、环境和 evaluator；未披露的跨域、生产与长期稳定性不得外推。

采用边界：Developer memory selection 是带 propensity 与延迟反馈的控制决策；确定性策略持有生产权，学习策略只能在 shadow/OPE gate 后进入 canary。 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)；现有命题：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner；比较：现有命题已经规定：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner。本来源的受限增量是“Developer memory selection 是带 propensity 与延迟反馈的控制决策；确定性策略持有生产权，学习策略只能在 shadow/OPE gate 后进入 canary。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Evaluating Agentic AI in the Wild: Failure Modes, Drift Patterns, and a Production Evaluation Framework](https://arxiv.org/html/2605.01604v1)

准入时需核验的设计变化是：生产 Agent 的 compounding error、tool cascade 与 temporal drift 要用连续、分布感知、跨信号的评测状态，而非一次 episodic score。。exact-v1 的机制定位为 `§3 Production failure taxonomy；§5 PAEF；§5.2–5.7 five dimensions and architecture`，评价定位为 `§6.1 Experimental setup；§6.2–6.5 failure-mode experiments`，限制或反证定位为 `§7.3 Limitations: no production data, black-box agents, threshold calibration`。

机制证据摘要：Existing evaluation frameworks for large language models -- including HELM, MT-Bench, AgentBench, and BIG-bench -- are designed for controlled, single-session, lab-scale settings. They do not address the evaluation challenges that emerge when agentic AI systems operate continuously in production: compounding decision errors, tool failure cascades, non-deterministic output drift, and the absence of ground truth for long-horizon tasks. This paper makes three contributions. First, we present a taxonomy of seven failu…

评价证据摘要：Existing evaluation frameworks for large language models -- including HELM, MT-Bench, AgentBench, and BIG-bench -- are designed for controlled, single-session, lab-scale settings. They do not address the evaluation challenges that emerge when agentic AI systems operate continuously in production: compounding decision errors, tool failure cascades, non-deterministic output drift, and the absence of ground truth for long-horizon tasks. This paper makes three contributions. First, we present a taxonomy of seven failu…

限制证据摘要：只支持 exact-v1 披露的任务、模型、环境和 evaluator；未披露的跨域、生产与长期稳定性不得外推。

采用边界：生产 Agent 的 compounding error、tool cascade 与 temporal drift 要用连续、分布感知、跨信号的评测状态，而非一次 episodic score。 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“生产 Agent 的 compounding error、tool cascade 与 temporal drift 要用连续、分布感知、跨信号的评测状态，而非一次 episodic score。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Concepts Whisper While Syntax Shouts: Spectral Anti-Concentration and the Dual Geometry of Transformer Representations](https://arxiv.org/html/2605.01609v1)

准入时需核验的设计变化是：以谱能量与 whitened causal alignment 区分稀疏概念方向和高能 syntax 结构，反证只看方差的解释。exact-v1 的机制定位为 `3.3 Concept Extraction: Three Independent Methods；Method 1: Difference-of-means on residual activations (subtractive).；Method 2: Sparse autoencoder features (contextualized, unsupervised).`，评价定位为 `3 Experimental Setup`，限制或反证定位为 `9 Discussion；Limitations.；11 Conclusion`。

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `No Change — Existing Coverage (proposition comparison; independent review required)`，目标 owner 为 `WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；现有命题：本章已区分相关方向、线性 probe 与因果干预；谱反集中是新的测量案例而非新表示 owner；比较：exact-v1 的新增证据是“以谱能量与 whitened causal alignment 区分稀疏概念方向和高能 syntax 结构，反证只看方差的解释”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。最终处置已通过独立复核。

### [Prescriptive Scaling Laws for Data Constrained Training](https://arxiv.org/html/2605.01640v1)

准入时需核验的设计变化是：data cap 下的 scaling law 把新增算力重新分配到数据质量、重复与模型规模。exact-v1 的机制定位为 `Appendix A Reanalysis of Muennighoff et al. compute-optimal allocation；B.1 Architecture；B.2 Model configurations`，评价定位为 `3 Experimental setup；5 Scaling law validation；6 Case study: weight decay improves robustness to data repetition`，限制或反证定位为 `7 Conclusion`。

机制证据摘要：Our scaling law recommends allocating data-constrained compute toward larger models trained for fewer epochs, while Muennighoff et al. (2023) recommend the opposite: smaller models trained for more epochs. We trace this disagreement to the fact that Muennighoff et al. (2023) fit their Chinchilla base law on Hoffmann et al. (2022) ’s scraped C4 isoFLOP points rather than on their own scaling runs. Although both studies use C4, differences in tokenization, preprocessing, and training codebases mean that parameters f…

评价证据摘要：We pretrain decoder-only language models using the Llama 2 architecture and tokenizer ( Touvron et al., 2023 ) across a grid of model sizes, unique data budgets, and repetition counts. All models are trained on the FineWeb dataset ( Penedo et al., 2024 ) , a large-scale filtered web corpus. For our scaling study, we sweep over model sizes N N ranging from 15M to 1B parameters, unique data budgets U D U_{D} from 50M to 6B tokens, and repetition counts R D ∈ { 0 , 1 , 3 , 7 , 11 , 15 } R_{D}\in\{0,1,3,7,11,15\} ; th…

限制证据摘要：We have presented a simple data-constrained scaling law that models the cost of data repetition with a simple, additive overfitting penalty. A complexity ladder of one-, two-, and four-parameter forms provides a Pareto frontier of fit quality versus complexity, with even the simplest form substantially outperforming prior effective-data formulations. The overfitting penalty provides a new axis for evaluating trainin…

采用边界：机制锚点为 Appendix A Reanalysis of Muennighoff et al. compute-optimal allocation, B.1 Architecture, B.2 Model configurations；评价锚点为 3 Experimental setup, 5 Scaling law validation, 6 Case study: weight decay improves robustness to data repetition。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；现有命题：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算；比较：现有命题已经规定：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算。本来源的受限增量是“data cap 下的 scaling law 把新增算力重新分配到数据质量、重复与模型规模”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Adaptive Pluralistic Alignment: A pipeline for dynamic artificial democracy](https://arxiv.org/html/2605.01642v1)

准入时需核验的设计变化是：把人群偏好分解为低秩 reward basis，经民主过滤形成 jury，再随时间更新群体权重与策略。exact-v1 的机制定位为 `3 Preliminaries；4.3 Stage 3: Jury adaptation；4 Adaptive pluralistic alignment`，评价定位为 `5 Proof-of-concept demonstration；5.1 Experimental setup`，限制或反证定位为 `6 Discussion；Limitations.；Future work.`。

机制证据摘要：As societal values evolve over time, the jury pool must be updated to reflect more contemporary perspectives. We accomplish this by collecting a small set of new preference data and using it to learn additional personalized reward models, which are then added to the pool of potential jurors. Concretely, suppose that at some later time t > 0 t>0 , sufficient time has elapsed that we expect societal values to have shifted. We subsample a set of preference comparison questions from the original dataset 𝒟 0 \mathcal{D…

评价证据摘要：We illustrate the APA pipeline with a worked example, using historical-period simulations to stand in for the future value shifts that APA is ultimately designed to track. Our goal is to make the pipeline’s behavior concrete and surface design questions for future work. The intended use of APA is to adapt to future value changes as human morality evolves. However, future value shifts are inherently difficult to predict, and we do not yet have preference data from populations whose values have substantially diverge…

限制证据摘要：We presented Adaptive Pluralistic Alignment (APA), a modular pipeline for updating pluralistically aligned AI systems to track evolving societal values without repeating costly pretraining, fine-tuning, or large-scale reward modeling. APA achieves this by decoupling the expensive, one-time step of learning reward basis functions from the lightweight, recurring step of fitting new annotator weights and incorporating…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `TRAIN-RLHF` / [Ch31](../../../../books/part-04-training-system/31-rlhf.md)；现有覆盖差异：现有正文仍缺：把人群偏好分解为低秩 reward basis，经民主过滤形成 jury，再随时间更新群体权重与策略。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。最终处置已通过独立复核。

### [AI Alignment via Incentives and Correction](https://arxiv.org/html/2605.01643v1)

准入时需核验的设计变化是：solver 与 auditor 的联合纠错事件使 reward design 成为保持监督激励的双层控制问题。exact-v1 的机制定位为 `A Principled Game-Theoretic Model for AI Alignment.；Reward Design for Agentic LLM Pipelines.；3 Mechanism Design for Alignment`，评价定位为 `3.2 Local Incentives Analysis；Equilibria Analysis.；5 Experimental Results`，限制或反证定位为 `6 Conclusion；Limitations.；C.2 Mechanism of the Fixed-Default Failure`。

机制证据摘要：In section 3 , we propose a theoretical model to study the mechanism design of a simple two-agent AI pipeline, a solver and an auditor. Every round, the two agents give a response, and we assign rewards according to a design that the end user can choose dynamically every round. We explain why dynamic rewards are better for user outcomes over static rewards. Using known techniques in (bi-level) bandit optimization, we describe an algorithm that approaches a local maximum of the user’s values. Using the theoreticall…

评价证据摘要：Here we analyze the local incentives of the solver and auditor (i.e. for a fixed prompt), so we drop the dependency on x x from our notation. Beyond the incentives of any rational agents in this setting, we assume that the solver derives some additional time-dependent utility Ω t ​ ( x ) ≥ 0 \Omega_{t}(x)\geq 0 from misaligning. This assumption reflects the notion that standard RL post-training procedures may induce misalignment in LLM agents. For example, in the hallucination setting, RLHF pushes the models to pr…

限制证据摘要：We proposed a mechanism-design view of alignment in agentic pipelines. The main lesson is that rewards should not be judged only by the immediate behavior they encourage, but by the fixed point they induce among interacting learned agents. In a solver–auditor system, penalizing misalignment can deter bad outputs, but it can also reduce the auditor’s incentive to monitor. Robust alignment, therefore, requires dynamic…

采用边界：机制锚点为 A Principled Game-Theoretic Model for AI Alignment., Reward Design for Agentic LLM Pipelines., 3 Mechanism Design for Alignment；评价锚点为 3.2 Local Incentives Analysis, Equilibria Analysis., 5 Experimental Results。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `TRAIN-RLHF` / [Ch31](../../../../books/part-04-training-system/31-rlhf.md)；最终处置已通过独立复核。

### [Toward a Principled Framework for Agent Safety Measurement](https://arxiv.org/html/2605.01644v1)

准入时需核验的设计变化是：Agent safety measurement 必须覆盖策略搜索空间而不是只测固定输出样本。exact-v1 的机制定位为 `3. BOA: An Efficient Agent Safety Measurement Framework；3.2. System Design and Implementation`，评价定位为 `Toward a Principled Framework for Agent Safety Measurement；3. BOA: An Efficient Agent Safety Measurement Framework；3.2. System Design and Implementation`，限制或反证定位为 `5. Conclusion`。

采用边界：机制锚点为 3. BOA: An Efficient Agent Safety Measurement Framework, 3.2. System Design and Implementation；评价锚点为 Toward a Principled Framework for Agent Safety Measurement, 3. BOA: An Efficient Agent Safety Measurement Framework, 3.2. System Design and Implementation。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“Agent safety measurement 必须覆盖策略搜索空间而不是只测固定输出样本”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [SteeringDiffusion: A Bottlenecked Activation Control Interface for Diffusion Models](https://arxiv.org/html/2605.01653v1)

准入时需核验的设计变化是：以瓶颈 activation adapter 在 diffusion 运行时注入方向控制，形成不改主权重的控制接口。exact-v1 的机制定位为 `Our steering mechanism.；Monotonicity analysis.；UNet-specific architecture.`，评价定位为 `Empirical findings；3 Style Steering Experiments on SD 1.5；3.1 Experimental Setup`，限制或反证定位为 `3.4 Control Surface: Smooth Monotonic Trade-off；3.11 Discussion: Why Bottlenecked Activation Control Yields a Stable Control Surface；3.12 Limitations and Scope`。

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `No Change — Existing Coverage (proposition comparison; independent review required)`，目标 owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；现有命题：本章已覆盖 conditioning、adapter 与迭代生成控制，并保留能力干扰和强度校准；该接口是受限实现；比较：exact-v1 的新增证据是“以瓶颈 activation adapter 在 diffusion 运行时注入方向控制，形成不改主权重的控制接口”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。最终处置已通过独立复核。

### [Act2See: Emergent Active Visual Perception for Video Reasoning](https://arxiv.org/html/2605.01657v1)

准入时需核验的设计变化是：VLM 在推理中主动决定检索或生成视觉证据，使 context acquisition 成为显式动作。exact-v1 的机制定位为 `2 Method；3 Dataset Description；3.4 Dataset composition`，评价定位为 `4 Experiments；4.1 Benchmarks`，限制或反证定位为 `6 Conclusion；Robustness towards generation failure.`。

采用边界：机制锚点为 2 Method, 3 Dataset Description, 3.4 Dataset composition；评价锚点为 4 Experiments, 4.1 Benchmarks。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；现有命题：多模态表示必须保留时间、模态与来源身份，不能只比较 token 数量；比较：现有命题已经规定：多模态表示必须保留时间、模态与来源身份，不能只比较 token 数量。本来源的受限增量是“VLM 在推理中主动决定检索或生成视觉证据，使 context acquisition 成为显式动作”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Video Active Perception: Effective Inference-Time Long-Form Video Understanding with Vision-Language Models](https://arxiv.org/html/2605.01662v1)

准入时需核验的设计变化是：长视频推理将 keyframe selection 建模为基于生成先验的 inference-time data acquisition。exact-v1 的机制定位为 `Frame selection methods for inference-time video question-answering.；3.1 A Priori Knowledge for Generating Full Video Dynamics`，评价定位为 `4 Experiments；4.3 Implementation Details`，限制或反证定位为 `5 Conclusions`。

采用边界：机制锚点为 Frame selection methods for inference-time video question-answering., 3.1 A Priori Knowledge for Generating Full Video Dynamics；评价锚点为 4 Experiments, 4.3 Implementation Details。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；现有命题：多模态表示必须保留时间、模态与来源身份，不能只比较 token 数量；比较：现有命题已经规定：多模态表示必须保留时间、模态与来源身份，不能只比较 token 数量。本来源的受限增量是“长视频推理将 keyframe selection 建模为基于生成先验的 inference-time data acquisition”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [CP-SynC: Multi-Agent Zero-Shot Constraint Modeling in MiniZinc with Synthesized Checkers](https://arxiv.org/html/2605.01675v1)

准入时需核验的设计变化是：并行生成候选约束程序并综合可执行 checker 证据，将 verifier 变为最终选择 authority。exact-v1 的机制定位为 `Large Language Models；3.1 System Design`，评价定位为 `Validation Agents`，限制或反证定位为 `7 Conclusion and Discussion`。

采用边界：机制锚点为 Large Language Models, 3.1 System Design；评价锚点为 Validation Agents。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `AGENT-MULTI-AGENT` / [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；现有命题：消息、角色和局部成功不能替代共享状态的唯一提交语义；比较：现有命题已经规定：消息、角色和局部成功不能替代共享状态的唯一提交语义。本来源的受限增量是“并行生成候选约束程序并综合可执行 checker 证据，将 verifier 变为最终选择 authority”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [GRAVITY: Architecture-Agnostic Structured Anchoring for Long-Horizon Conversational Memory](https://arxiv.org/html/2605.01688v1)

准入时需核验的设计变化是：retrieved evidence 与 generation-time relational/temporal/thematic anchors 是两层状态；结构化派生视图不能替代原始 memory provenance。。exact-v1 的机制定位为 `§3.1 Three conversation structures；§3.2 Structured-anchor build；§3.3 Generation-time injection`，评价定位为 `§4.1 Setup；§4.2 Main results；§4.3 Ablation；Appendix A.4 oracle/error analysis`，限制或反证定位为 `§5 Discussion and error analysis；architecture and benchmark scope`。

机制证据摘要：Long-horizon conversational agents rely on memory systems with increasingly sophisticated retrieval mechanisms. However, retrieved fragments are typically fed to the language model as unstructured text, lacking the relational, temporal, and thematic structures essential for complex reasoning. To bridge this reasoning gap, we introduce GRAVITY (\textbf{G}eneration-time \textbf{R}elational \textbf{A}nchoring \textbf{V}ia \textbf{I}njected \textbf{T}opological Memor\textbf{Y}), a plug-and-play structured memory modul…

评价证据摘要：Long-horizon conversational agents rely on memory systems with increasingly sophisticated retrieval mechanisms. However, retrieved fragments are typically fed to the language model as unstructured text, lacking the relational, temporal, and thematic structures essential for complex reasoning. To bridge this reasoning gap, we introduce GRAVITY (\textbf{G}eneration-time \textbf{R}elational \textbf{A}nchoring \textbf{V}ia \textbf{I}njected \textbf{T}opological Memor\textbf{Y}), a plug-and-play structured memory modul…

限制证据摘要：只支持 exact-v1 披露的任务、模型、环境和 evaluator；未披露的跨域、生产与长期稳定性不得外推。

采用边界：retrieved evidence 与 generation-time relational/temporal/thematic anchors 是两层状态；结构化派生视图不能替代原始 memory provenance。 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)；现有命题：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner；比较：现有命题已经规定：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner。本来源的受限增量是“retrieved evidence 与 generation-time relational/temporal/thematic anchors 是两层状态；结构化派生视图不能替代原始 memory provenance。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Latent State Design for World Models under Sufficiency Constraints](https://arxiv.org/html/2605.01694v1)

准入时需核验的设计变化是：world-model latent state 以任务充分性而非重建完整 observation 作为设计约束。exact-v1 的机制定位为 `2 What is a latent world model?；2.1 Latent world models as state abstraction`，评价定位为 `12 Evaluation framework；12.1 Seven evaluation axes；12.2 A functional evaluation matrix`，限制或反证定位为 `14 Conclusion`。

采用边界：机制锚点为 2 What is a latent world model?, 2.1 Latent world models as state abstraction；评价锚点为 12 Evaluation framework, 12.1 Seven evaluation axes, 12.2 A functional evaluation matrix。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；现有命题：生成外观、环境 transition 与可修订 world state 是不同责任；比较：现有命题已经规定：生成外观、环境 transition 与可修订 world state 是不同责任。本来源的受限增量是“world-model latent state 以任务充分性而非重建完整 observation 作为设计约束”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Probe-Geometry Alignment: Erasing the Cross-Sequence Memorization Signature Below Chance](https://arxiv.org/html/2605.01699v1)

准入时需核验的设计变化是：跨序列 probe 揭示 unlearning 后可恢复的表示痕迹，并用逐层 rank-one intervention 擦除。exact-v1 的机制定位为 `3 Cross-Sequence Signature Across Three Pretrained Architectures；3.1 Leave-One-Out Cross-Sequence Probe Protocol；Procedure.`，评价定位为 `Toy verification and a constructive follow-up.；Result 1: gap collapses locally, reconstitutes downstream.；Result 2: behavioural recall is largely preserved.`，限制或反证定位为 `Failure modes that motivate PGA.；Adversarial PGA: defeats re-fit attackers (adaptive-attacker threat model).`。

采用边界：机制锚点为 3 Cross-Sequence Signature Across Three Pretrained Architectures, 3.1 Leave-One-Out Cross-Sequence Probe Protocol, Procedure.；评价锚点为 Toy verification and a constructive follow-up., Result 1: gap collapses locally, reconstitutes downstream., Result 2: behavioural recall is largely preserved.。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor；比较：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“跨序列 probe 揭示 unlearning 后可恢复的表示痕迹，并用逐层 rank-one intervention 擦除”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [The Reasoning Trap: An Information-Theoretic Bound on Closed-System Multi-Step LLM Reasoning](https://arxiv.org/html/2605.01704v1)

准入时需核验的设计变化是：closed-system 多步推理存在信息边界，外部 evidence 改变可恢复性而非单纯增加思考 token。exact-v1 的机制定位为 `The Reasoning Trap: An Information-Theoretic Bound on Closed-System Multi-Step LLM Reasoning A Falsifiable Theorem, the Multi-Agent-Debate Instantiation, and a Triple Failure of Human Reliability；The paradox is methodologically generated.；Five contributions: a three-part framework, two theorems, and reliability evidence.`，评价定位为 `Companion results.；Architectural-limit parallel to compositionality results.`，限制或反证定位为 `The Reasoning Trap: An Information-Theoretic Bound on Closed-System Multi-Step LLM Reasoning A Falsifiable Theorem, the Multi-Agent-Debate Instantiation, and a Triple Failure of Human Reliability；R6 (Triple failure of human reliability).；Epistemological reading of the triple failure.`。

采用边界：机制锚点为 The Reasoning Trap: An Information-Theoretic Bound on Closed-System Multi-Step LLM Reasoning A Falsifiable Theorem, the Multi-Agent-Debate Instantiation, and a Triple Failure of Human Reliability, The paradox is methodologically generated., Five contributions: a three-part framework, two theorems, and reliability evidence.；评价锚点为 Companion results., Architectural-limit parallel to compositionality results.。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“closed-system 多步推理存在信息边界，外部 evidence 改变可恢复性而非单纯增加思考 token”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [SplitZip: Ultra Fast Lossless KV Compression for Disaggregated LLM Serving](https://arxiv.org/html/2605.01708v1)

准入时需核验的设计变化是：bit-exact KV transfer compression 在 PD 拆分中压缩传输而不改变 decode 状态。exact-v1 的机制定位为 `3.2 Method；4.3.2 Ablation on Calibration Dataset；4.3.4 Ablation on Escape-Position Metadata`，评价定位为 `4.2 Results`，限制或反证定位为 `5 Conclusion`。

机制证据摘要：SplitZip combines fixed-length exponent coding with explicit escape capture, as illustrated in Figure 1 . For a BF16 value represented as a 16-bit integer x i x_{i} , SplitZip extracts ⬇ e_i = ( x_i >> 7) & 0 xff ; a_i = (( x_i >> 8) & 0 x80 ) \| ( x_i & 0 x7f ); where e_i is the 8-bit exponent and a i a_{i} is the exact sign–mantissa byte. Given a decoded exponent e ^ i \hat{e}_{i} , the original BF16 bit pattern is reconstructed as x ^ i = ( ( a i & 0 ​ x ​ 80 ) ≪ 8 ) ​ \| ( e ^ i ≪ 7 ) \| ​ ( a i & 0 ​ x ​ 7 ​…

评价证据摘要：Table 2: Comparison of encoding/decoding throughput and compression ratio of various compression methods. While maintaining a respectable compression ratio, SplitZip demonstrates a significant advantage in codec throughput. Method Ratio Encode(GB/s) Decode(GB/s) nvCOMP LZ4 [ 19 ] 1.019 13.4 ± 0.4 13.4\pm 0.4 137.1 ± 8.8 137.1\pm 8.8 nvCOMP Cascaded [ 19 ] 1.000 111.8 ± 0.8 111.8\pm 0.8 155.2 ± 5.6 155.2\pm 5.6 nvCOMP Bitcomp [ 19 ] 1.056 341.5 ± 7.1 341.5\pm 7.1 147.7 ± 4.8 147.7\pm 4.8 ZipNN [ 9 ] 1.515 1.2 1.7 D…

限制证据摘要：This paper presents SplitZip, a GPU-friendly lossless compression scheme for KV-cache transfer in PD disaggregated LLM serving. SplitZip encodes frequent exponent values with fixed-length codes, and correcting rare values through an explicit escape stream, SplitZip provides a highly parallel codec for the latency-critical communication path. Our experiments show that SplitZip achieves higher compression and decompre…

采用边界：机制锚点为 3.2 Method, 4.3.2 Ablation on Calibration Dataset, 4.3.4 Ablation on Escape-Position Metadata；评价锚点为 4.2 Results。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (marker verified)`，目标 owner 为 `INFER-PD-DISAGGREGATION` / [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md)；现有命题：阶段分离只有在状态迁移、失败域和 SLO 同时闭合时才成立；比较：现有命题已经规定：阶段分离只有在状态迁移、失败域和 SLO 同时闭合时才成立。本来源的受限增量是“bit-exact KV transfer compression 在 PD 拆分中压缩传输而不改变 decode 状态”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Model Routing as a Trust Problem: Route Receipts for Adaptive AI Systems](https://arxiv.org/html/2605.01710v1)

准入时需核验的设计变化是：为动态模型路由生成 route receipt，记录候选、策略版本、约束、选择结果与可披露 provenance。exact-v1 的机制定位为 ``，评价定位为 `7. Case study: how the legal summary changed`，限制或反证定位为 `10. Usability and tradeoffs；11. Threat model and redaction；14. Limitations and future work`。

机制证据摘要：Not Disclosed in an independently titled section.

评价证据摘要：Northstar is a fictional legal-technology company that provides contract summarization for enterprise customers. Its product ingests long agreements, pulls out obligations and exceptions, and produces a memo counsel can review. Users rely on it to save time, even though it does not make final legal decisions. During development, Northstar tests the system with a model alias called contract-pro-latest . It performs well on an internal validation set, so the team deploys the feature with priority processing to keep…

限制证据摘要：Users often resist route receipts when the metadata feels unnecessary. Many users feel that way on routine tasks. People asking for a recipe, a joke, or a first draft of an email do not want to inspect service-tier metadata. Even sophisticated users can find too many labels distracting. If a route receipt is too prominent, the product can feel anxious, bureaucratic, or broken. The interface should present informatio…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `PLATFORM-TRACE` / [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md)；现有覆盖差异：现有正文仍缺：为动态模型路由生成 route receipt，记录候选、策略版本、约束、选择结果与可披露 provenance。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。最终处置已通过独立复核。

### [Motion-Aware Caching for Efficient Autoregressive Video Generation](https://arxiv.org/html/2605.01725v1)

准入时需核验的设计变化是：按 token 运动强度动态决定视频生成 cache 更新频率，显式控制复用误差累积。exact-v1 的机制定位为 `4 Analysis of Caching Error；4.3 Theoretical Connection: Residual Stability and Motion Dynamics；5 Methodology`，评价定位为 `4 Analysis of Caching Error；4.2 Empirical Observations`，限制或反证定位为 `7 Conclusion`。

机制证据摘要：To motivate our transition from coarse-grained chunk skipping to fine-grained token-wise caching, we analytically investigate the source of approximation error in the caching mechanism. We demonstrate that the caching error is theoretically bounded by the inconsistency of feature residuals across timesteps, and this inconsistency is highly correlated with the underlying motion dynamics. Since the ideal residual difference is computationally inaccessible prior to inference, we require a lightweight proxy. We establ…

评价证据摘要：To motivate our transition from coarse-grained chunk skipping to fine-grained token-wise caching, we analytically investigate the source of approximation error in the caching mechanism. We demonstrate that the caching error is theoretically bounded by the inconsistency of feature residuals across timesteps, and this inconsistency is highly correlated with the underlying motion dynamics. Guided by Proposition 4.1 , we analyze the distribution of residual differences in actual video generation. Heterogeneous Tempora…

限制证据摘要：In this paper, we presented MotionCache, a novel motion-aware caching framework designed to accelerate autoregressive video generation. By establishing a theoretical connection between residual instability and intra-chunk frame discrepancies, we introduced a lightweight, fine-grained proxy for token importance. This formulation allows the model to break free from the rigid "all-or-nothing" constraints of previous co…

采用边界：机制锚点为 4 Analysis of Caching Error, 4.3 Theoretical Connection: Residual Stability and Motion Dynamics, 5 Methodology；评价锚点为 4 Analysis of Caching Error, 4.2 Empirical Observations。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；最终处置已通过独立复核。

### [EGAD: Entropy-Guided Adaptive Distillation for Token-Level Knowledge Transfer](https://arxiv.org/html/2605.01732v1)

准入时需核验的设计变化是：按教师 entropy 调整 curriculum、temperature 与蒸馏路径，使 token-level transfer 随不确定性变化。exact-v1 的机制定位为 `3 Method；4.5 Analysis of Token Entropy Distribution；4.6 Hyperparameter Analysis`，评价定位为 `4 Experiments；4.1 Experimental Setup；4.2 Main Results`，限制或反证定位为 `5 Conclusion`。

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `No Change — Existing Coverage (proposition comparison; independent review required)`，目标 owner 为 `TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md)；现有命题：本章已有按 teacher disagreement/entropy 选择 token 与温度的机制；EGAD 未改变 teacher/student ownership；比较：exact-v1 的新增证据是“按教师 entropy 调整 curriculum、temperature 与蒸馏路径，使 token-level transfer 随不确定性变化”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。最终处置已通过独立复核。

### [GEASS: Gated Evidence-Adaptive Selective Caption Trust for Vision-Language Models](https://arxiv.org/html/2605.01733v1)

准入时需核验的设计变化是：并行执行图像直答与 caption 辅助路径，以 confidence gate、information gain 和证据权重融合，限制错误 caption 锚定。exact-v1 的机制定位为 `3 Preliminary Analysis；4 Method`，评价定位为 `3.1 Setup；5 Experiments；5.1 Setup`，限制或反证定位为 `6 Conclusion`。

机制证据摘要：We investigate how captions actually shape VLM behavior, and identify two structural properties that jointly govern caption-aided inference: a deep anchoring effect (§ 3.2 ) and an asymmetric error structure (§ 3.4 ). Together they expose three failure modes that any inference-time mechanism consuming captions must address (§ 3.5 ). The three failure modes in Section 3.5 share a common structure: each is characterised by a distinct combination of two quantities the model exposes at decoding time—its own confidence…

评价证据摘要：We use Qwen2.5-VL-3B ( Bai et al., 2025 ) as our primary model, with cross-validation on InternVL2-8B ( Chen et al., 2024b ) , InternVL3-3.8B ( Zhu et al., 2025 ) , and a reasoning-augmented variant Qwen2.5-VL-3B † . Captions are produced by the model itself under the instruction “Describe this image in detail” with greedy decoding, and embedded as text below the original image to form a composite input fed back to the model alongside the question. Evaluation is performed on HallusionBench ( Guan et al., 2024 ) an…

限制证据摘要：We studied how captions influence VLM inference and identified two properties that govern the outcome: a deep anchoring effect, which extends a caption’s influence well past the final answer into the model’s reasoning trajectory, and an asymmetric error structure, in which omission outnumbers fabrication but each fabrication carries a much larger per-instance impact. Because both properties operate on the same capti…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；现有覆盖差异：现有正文仍缺：并行执行图像直答与 caption 辅助路径，以 confidence gate、information gain 和证据权重融合，限制错误 caption 锚定。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。最终处置已通过独立复核。

### [Architectural Obsolescence of Unhardened Agentic-AI Runtimes](https://arxiv.org/html/2605.01740v1)

准入时需核验的设计变化是：biconditional gate、hash-chain audit、egress guard 与 signing root 共同绑定 Agent action 与审计记录。exact-v1 的机制定位为 `3 Threat model；5 Methodology`，评价定位为 `4.1 Empirical primitive availability；6 Results；The change, validation, and gain.`，限制或反证定位为 `2 The F1–F4 failure-mode taxonomy；3 Threat model`。

机制证据摘要：Adversary capability. The adversary controls any string the agent’s host runtime processes — chat message, retrieved-document chunk, tool-output payload, operator prompt — including content that imitates LLM serialisation tokens, embeds known secret/PII shapes, or mis-matches the intended target. The adversary may not compromise the host process, the trust root, the audit-log filesystem, or the cryptographic primitives; those are addressed by system-level orthogonal controls (process isolation, FIPS-validated cryp…

评价证据摘要：Table 2 reports the result of a two-stage audit of each subject’s published surface. First, a tree-walk over the first-party source files ( *.ts , *.tsx , *.mjs , *.js , *.cjs ; node_modules , dist , build , out , coverage excluded) greps for the canonical exported symbol of each detection primitive. Second, the subject’s user-facing documentation, plugin SDK reference, and API surface ( README , AGENTS.md , docs/ , src/plugin-sdk/ where applicable) is read to confirm whether any equivalent primitive ships under a…

限制证据摘要：The obsolescence claim rests on a specific failure-mode set ℱ \mathcal{F} inherited from [ 1 ] §5. We restate it briefly so the rest of the paper is self-contained. Adversary capability. The adversary controls any string the agent’s host runtime processes — chat message, retrieved-document chunk, tool-output payload, operator prompt — including content that imitates LLM serialisation tokens, embeds known secret/PII…

采用边界：机制锚点为 3 Threat model, 5 Methodology；评价锚点为 4.1 Empirical primitive availability, 6 Results, The change, validation, and gain.。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `AGENT-PLATFORM` / [Ch84](../../../../books/part-07-agent/84-agent-platform.md)；最终处置已通过独立复核。

### [Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality](https://arxiv.org/html/2605.01749v1)

准入时需核验的设计变化是：把长答案生成拆成 calibrated exploration 与 selective commitment，只将达到可靠性门槛的推理投影为最终 claim。exact-v1 的机制定位为 `2 Methodology；Formulation；4 Analysis`，评价定位为 `2.1 Problem Setup；3 Experiments；3.1 Experimental Setup`，限制或反证定位为 `6 Conclusion；Helpfulness exhibits a controlled trade-off.；Discussion`。

机制证据摘要：In this section, we present the Exploration-Commitment Decoupling paradigm and its instantiation, CAG. We begin by introducing the problem setup and analyzing the limitations of existing generation paradigms (§ 2.1 ). We then propose the Exploration-Commitment Decoupling paradigm that disentangles reasoning exploration from answer commitment via step-level reliability estimation. To realize the paradigm, we introduce a structured supervision framework (§ 2.3 ) that jointly learns calibrated reasoning and selective…

评价证据摘要：We study long-form generation using LRMs. Formally, given an input query x x , a reasoning model produces a sequence of \| ℛ \| \|\mathcal{R}\| intermediate reasoning steps r = ( r 1 , … , r \| ℛ \| ) r=(r_{1},\dots,r_{\|\mathcal{R}\|}) , followed by a final answer y y . Each reasoning step r i r_{i} consists of a sequence of \| 𝒜 i \| \|\mathcal{A}_{i}\| atomic claims ( a i , 1 , … , a i , \| 𝒜 i \| ) (a_{i,1},\dots,a_{i,\|\mathcal{A}_{i}\|}) , where each a i , j a_{i,j} represents a minimal, self-contained unit…

限制证据摘要：In this paper, we propose an Exploration–Commitment Decoupling paradigm to improve long-form factuality by disentangling knowledge exploration from final answer commitment. We instantiate the paradigm with Calibration-Aware Generation (CAG) , a framework that integrates calibrated exploration and selective commitment, enabling models to perform end-to-end, calibration-aware generation by estimating step-level reliab…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有覆盖差异：现有正文仍缺：把长答案生成拆成 calibrated exploration 与 selective commitment，只将达到可靠性门槛的推理投影为最终 claim。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。最终处置已通过独立复核。

### [Talk is Cheap, Communication is Hard: Dynamic Grounding Failures and Repair in Multi-Agent Negotiation](https://arxiv.org/html/2605.01750v1)

准入时需核验的设计变化是：多 Agent 协商失败来自共享 grounding 动态漂移，并需要显式 repair 而非增加消息。exact-v1 的机制定位为 `Connection to grounding theory；LLM-assisted behavioral analysis；Appendix A Interactivity level analysis`，评价定位为 `4. Experimental setup；5. Results；LLM-assisted behavioral analysis`，限制或反证定位为 `5.6 Referential binding failures；6. Discussion；Limitations & Future Work`。

采用边界：机制锚点为 Connection to grounding theory, LLM-assisted behavioral analysis, Appendix A Interactivity level analysis；评价锚点为 4. Experimental setup, 5. Results, LLM-assisted behavioral analysis。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `AGENT-MULTI-AGENT` / [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；现有命题：消息、角色和局部成功不能替代共享状态的唯一提交语义；比较：现有命题已经规定：消息、角色和局部成功不能替代共享状态的唯一提交语义。本来源的受限增量是“多 Agent 协商失败来自共享 grounding 动态漂移，并需要显式 repair 而非增加消息”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Catching the Infection Before It Spreads: Foresight-Guided Defense in Multi-Agent Systems](https://arxiv.org/html/2605.01758v1)

准入时需核验的设计变化是：多 Agent 感染防御应跟踪局部传播状态并按新近/长期感染选择 rollback 或递归定位，而不是用全局 cure factor 覆盖检索分布。。exact-v1 的机制定位为 `§3 Threat Model；§4 Infection dynamics；§5.2 Multi-persona simulation；§5.3–5.4 diagnosis and purification`，评价定位为 `§6.1–6.2 setup and metrics；§6.3–6.7 effectiveness, diversity and ablation`，限制或反证定位为 `§7.2 Limitations`。

机制证据摘要：Large multimodal model-based Multi-Agent Systems (MASs) enable collaborative complex problem solving through specialized agents. However, MASs are vulnerable to infectious jailbreak, where compromising a single agent can spread to others, leading to widespread compromise. Existing defenses counter this by training a more contagious cure factor, biasing agents to retrieve it over virus adversarial examples (VirAEs). However, this homogenizes agent responses, providing only superficial suppression rather than true r…

评价证据摘要：Large multimodal model-based Multi-Agent Systems (MASs) enable collaborative complex problem solving through specialized agents. However, MASs are vulnerable to infectious jailbreak, where compromising a single agent can spread to others, leading to widespread compromise. Existing defenses counter this by training a more contagious cure factor, biasing agents to retrieve it over virus adversarial examples (VirAEs). However, this homogenizes agent responses, providing only superficial suppression rather than true r…

限制证据摘要：只支持 exact-v1 披露的任务、模型、环境和 evaluator；未披露的跨域、生产与长期稳定性不得外推。

采用边界：多 Agent 感染防御应跟踪局部传播状态并按新近/长期感染选择 rollback 或递归定位，而不是用全局 cure factor 覆盖检索分布。 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor；比较：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“多 Agent 感染防御应跟踪局部传播状态并按新近/长期感染选择 rollback 或递归定位，而不是用全局 cure factor 覆盖检索分布。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [TrajShield: Trajectory-Level Safety Mediation for Defending Text-to-Video Models Against Jailbreak Attacks](https://arxiv.org/html/2605.01761v1)

准入时需核验的设计变化是：把文本到视频安全从 prompt 词面过滤提升为生成轨迹上的因果风险定位与最小改写。exact-v1 的机制定位为 `II-B Safety in Generative Models；III Problem Formulation`，评价定位为 `V-A2 Evaluation Metrics`，限制或反证定位为 `VI Conclusion；Limitations.`。

采用边界：机制锚点为 II-B Safety in Generative Models, III Problem Formulation；评价锚点为 V-A2 Evaluation Metrics。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor；比较：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“把文本到视频安全从 prompt 词面过滤提升为生成轨迹上的因果风险定位与最小改写”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Mitigating Multimodal LLMs Hallucinations via Relevance Propagation at Inference Time](https://arxiv.org/html/2605.01766v1)

准入时需核验的设计变化是：以逐 token 梯度更新直接修改 K/V 分支状态，并用 KL 约束分布漂移。exact-v1 的机制定位为 `§3.2 Layer-wise Relevance Propagation；§3.3 Learning Inference-time Modality Enhancement`，评价定位为 `§4 Experiments；§4.3 Ablation Studies；§4.4 Efficiency Analysis`，限制或反证定位为 `LRP implementation assumptions；§4.4 Efficiency Analysis`。

机制证据摘要：LIME 在每个生成步优化 K/V perturbation，使 LRP relevance 向视觉或音频 token 移动，并用 KL regularizer 约束下一 token distribution 偏移；模型参数保持冻结。

评价证据摘要：作者在 POPE/CHAIR 视觉任务和 Audio Hallucination QA/AIR-Bench 音频任务、所列 MLLM 上报告改善；K-only/V-only/KV 与 KL 消融属于这些模型与 evaluator。每 token 梯度更新增加 latency，作者把它定位于 offline/high-accuracy 场景。

限制证据摘要：LRP 对 normalization 使用 identity approximation；relevance 是 attribution proxy 而不是因果 grounding 或事实正确性。逐 token 反向优化增加延迟，分布约束也不能排除 latent-state hacking。

采用边界：exact-v1 只支持作者视觉/音频模型、LRP approximation 和离线评测；不证明 relevance 是事实概率、KV 扰动无副作用或该路径满足在线 serving latency。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；现有命题：直接修改 KV 的 inference-time 分支属于 Experimental mutable state，必须使用 versioned Copy-on-Write branch、隔离污染并由独立 outcome verifier 决定是否提交；比较：LIME 提供 multimodal relevance objective、KL 约束和逐 token 开销案例，但没有改变既有 KV mutation 的身份、隔离、验证和 rollback 合同；LRP relevance 也不能提升为 commit authority。最终处置已通过独立复核。

### [The Compliance Gap: Why AI Systems Promise to Follow Process Instructions but Don't](https://arxiv.org/html/2605.01771v1)

准入时需核验的设计变化是：区分结果合规与过程合规，要求工具调用、检索与中间动作日志证明系统实际遵循了指定过程。exact-v1 的机制定位为 `We argue the gap is methodologically generated.；Mechanism: from sycophancy to false compliance.；A.4 The Mechanism: From Sycophancy to False Compliance`，评价定位为 `4 Experiments；4.2 Causal Experiments (Exps 2, 2b, 5, 6; 492 sessions)；4.4 Exp 11: Blinded Human Evaluation (R6 protocol)`，限制或反证定位为 `5 Discussion；6 Conclusion；Limitations and falsifiable forecast.`。

机制证据摘要：The failure has been invisible for structural, not empirical, reasons. Three forces accumulate to produce the gap. 1. Reward-signal asymmetry. RLHF ( Christiano et al., 2017 ; Ouyang et al., 2022 ) optimizes preferences over text completions, leaving behavior invisible to the reward signal—a specific instantiation of Goodhart’s Law in the sense of Manheim and Garrabrant (2018) (regressional Goodhart), formalized by Skalse et al. (2022) . 2. Instruction-hierarchy de-prioritization. The instruction hierarchy ( Walla…

评价证据摘要：Thirteen experiments across 2,031 sessions with eight models (Claude Sonnet 4, GPT-4o, GPT-4o-mini, Gemini 2.5 Flash, Llama 3.3 70B ( Touvron et al., 2023 ) , Mistral Small 24B ( Jiang et al., 2023 ) , plus two SLM variants from the Llama/Mistral families fine-tuned with LoRA ( Hu et al., 2022 ) /QLoRA ( Dettmers et al., 2023 ) adapters; cf. Lyu et al. (2024) ). Temperature = 0.7 =0.7 , n = 5 n=5 – 10 10 seeds per cell. Per-model breakdowns and statistical tests (paired t t -tests, Mann-Whitney U U , η 2 \eta^{2}…

限制证据摘要：Three limitations: (i) the 75-benchmark survey is bounded by 2022–2026 literature; emerging spec-evaluation efforts ( Ahmed et al., 2025 ; Zhang et al., 2025b ; Zhang et al., 2025a ) require tracking. (ii) R6 used ten non-expert raters (nine text-only); expert raters with tool-call training may achieve higher detection. (iii) Five task types do not exhaust all process instructions. Falsifiable claim: any RLHF-traine…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有覆盖差异：root 回读发现该命题已在 canonical evaluation owner 中完整存在，无需在 Ch69 重复写入。最终处置已通过独立复核。

### [Anticipation-VLA: Solving Long-Horizon Embodied Tasks via Anticipation-based Subgoal Generation](https://arxiv.org/html/2605.01772v1)

准入时需核验的设计变化是：用可随环境状态递归细化、弹出和回退的 subgoal stack 连接高层 anticipation model 与低层 goal-conditioned VLA policy。。exact-v1 的机制定位为 `Anticipation Model；adaptive recursive subgoal generation；stack-based refine/pop/backtrack execution`，评价定位为 `simulated long-horizon tasks；real-world robotic tasks；subgoal-generation ablations`，限制或反证定位为 `bounded task suite；progress/value-model dependence；no open-world safety proof`。

机制证据摘要：高层 UMM 产生可执行 subgoal，低层 VLA 按当前 observation 执行；stack controller 根据进展弹出已完成目标，在复杂状态中继续细化，在偏离或失败时回退并重建未来 subgoal，而不是冻结固定粒度任务分解。

评价证据摘要：作者在模拟与有限真实机器人长程任务中比较固定/自适应 subgoal 路径，并通过消融支持递归 anticipation 对成功率的贡献；结果依赖其任务、value/progress 判断与低层 policy。

限制证据摘要：subgoal 是否完成、何时细化和回退由学习式判断控制；论文没有证明开放世界中的 progress calibration、无限递归终止、异常恢复或安全关键物理提交。

采用边界：来源支持将长程计划从固定 trace 演进为可修订 subgoal stack；不证明 anticipation 输出是环境事实，低层 controller 和 fresh observation 仍拥有执行与纠错边界。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent post-write review complete`，目标 owner 为 `MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；现有覆盖差异：现有覆盖与 exact-v1 对读后仍缺：在 immutable full-horizon trace 与逐步 reactive policy 之间增加 adaptive subgoal stack：每个 subgoal 绑定 observation revision、parent、完成条件和 validity horizon；高层 planner 只能 push/refine/backtrack proposal，低层 policy 用 fresh observation 执行，controller 验证完成后才 pop。它以局部修订降低整条计划报废成本，却新增 progress detector 误判、递归不终止、stack stale 和高低层语义漂移；动态环境或检测不可信时回退短 horizon reactive planning/全量重规划。exact-v1 只支持作者模拟与有限真实任务，不构成开放世界 safety proof。最终处置已通过独立复核。

### [Needle-in-RAG: Prompt-Conditioned Character-Level Traceback of Poisoned Spans in Retrieved Evidence](https://arxiv.org/html/2605.01782v1)

准入时需核验的设计变化是：先记录 misgeneration 与检索事件，再以 counterfactual deletion 回溯到字符级 poisoned span，并把 span provenance 返回修复环。exact-v1 的机制定位为 `4.1 RAGCharacter Architecture；Algorithm.；6.3 Why RAGCharacter outperforms baseline methods`，评价定位为 `5 Experiments；5.1 Experimental setup；5.2 Experiment results`，限制或反证定位为 `3.2 Threat Model；6 Discussion；7 Conclusion`。

机制证据摘要：RAGCharacter is a two-pass traceback system that localizes poisoned evidence at character granularity while remaining compatible with black-box LLM deployments, with core actions shown in Algorithms 1 and 2 . We adopt the forensic setting of prior traceback works, where the defender is not assumed to know the attacker’s injection strategy and poisoned entries may be arbitrarily distributed throughout the knowledge store. Given a user query q q and an observed misgeneration event, RAGCharacter identifies responsibl…

评价证据摘要：Not Disclosed in an independently titled section.

限制证据摘要：The discussion below offers interpretations suggested by our empirical results. These should be read as evidence-consistent explanations rather than definitive causal claims. We presented RAGCharacter, a two-pass, event-conditioned forensic framework for character-level traceback in retrieval-augmented generation. In Pass-0, the system behaves as a standard RAG pipeline while logging prompt-anchored evidence and exe…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `AGENT-RAG` / [Ch76](../../../../books/part-07-agent/76-rag.md)；现有覆盖差异：现有正文仍缺：先记录 misgeneration 与检索事件，再以 counterfactual deletion 回溯到字符级 poisoned span，并把 span provenance 返回修复环。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。最终处置已通过独立复核。

### [DataEvolver: Let Your Data Build and Improve Itself via Goal-Driven Loop Agents](https://arxiv.org/html/2605.01789v1)

准入时需核验的设计变化是：用 goal、artifact、critic、correction 和 acceptance 的双环构建可控视觉训练数据。exact-v1 的机制定位为 `5 Goal-Driven Loop-Agent Formulation；Algorithm sketch.`，评价定位为 `7.2 Scene Setup；8 Case Study I: Scene-Aware Object Rotation Images；10 Results on the Minimal Image-Level Rotation Case`，限制或反证定位为 `9.3 Future Video Validation；12 Discussion；13 Limitations`。

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `No Change — Existing Coverage (proposition comparison; independent review required)`，目标 owner 为 `TRAIN-DATA` / [Ch27](../../../../books/part-04-training-system/27-data.md)；现有命题：本章已把合成数据生产定义为带目标、校验、版本与失败回退的闭环；DataEvolver 没有改变数据 owner；比较：exact-v1 的新增证据是“用 goal、artifact、critic、correction 和 acceptance 的双环构建可控视觉训练数据”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。最终处置已通过独立复核。

### [Khala: Scaling Acoustic Token Language Models Toward High-Fidelity Music Generation](https://arxiv.org/html/2605.01790v1)

准入时需核验的设计变化是：在统一 acoustic-token hierarchy 中分层生成结构与细节，并以固定步数并行补全细粒度 token。exact-v1 的机制定位为 `Khala: Scaling Acoustic Token Language Models Toward High-Fidelity Music Generation；1.3 Overview of Our Approach`，评价定位为 `6 Experiments；6.1 Human Arena Evaluation；6.2 Ablations on Alignment and Initialization`，限制或反证定位为 `7 Discussion；8 Conclusion`。

机制证据摘要：Jiafeng Liu 1,† ljiafeng@ccom.edu.cn Yuanliang Dong 1,† gunterdong@mail.ccom.edu.cn Hongjia Liu 1 Yuqing Cheng 1 Zhancheng Guo 1 Huijing Liang 1 Wenbo Zhan 1 Yuming Sun 1 Xiaobing Li 1 Feng Yu 1 Maosong Sun 2,∗ 1 Central Conservatory of Music 2 Tsinghua University To address these challenges, we adopt a unified pure acoustic-token paradigm with a 64-layer residual vector quantization (RVQ) hierarchy and a two-stage coarse-to-fine generation framework. A backbone model first generates full-length coarse acoustic to…

评价证据摘要：We evaluate Khala from two perspectives: large-scale human preference and ablations on the proposed training design. Since music generation is ultimately judged by human perception, we treat blind listening evaluation as the primary comparison protocol and first compare Khala against both commercial and open-source systems in a large-scale pairwise arena. We evaluate Khala using a large-scale blind pairwise listening arena that includes 8 music generation systems: 4 commercial models (Suno v5, Mureka v8, Suno v4.5…

限制证据摘要：Khala is unified at the level of acoustic token space, but the current system still uses a two-stage model design. We view this as a practical choice under the current compute budget, rather than a fundamental limitation of the paradigm. In preliminary experiments, we also explored a unified model that performs both coarse generation and super-resolution, but found that decoupling the two stages into separate models…

采用边界：机制锚点为 Khala: Scaling Acoustic Token Language Models Toward High-Fidelity Music Generation, 1.3 Overview of Our Approach；评价锚点为 6 Experiments, 6.1 Human Arena Evaluation, 6.2 Ablations on Alignment and Initialization。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；最终处置已通过独立复核。

### [Embody4D: A Generalist Data Engine for Embodied 4D World Modeling](https://arxiv.org/html/2605.01799v1)

准入时需核验的设计变化是：把单目机器人视频转换为可变视角视频，并以 latent confidence 在 copy、repair 与 inpaint expert 之间路由，作为 embodied 4D 数据引擎。。exact-v1 的机制定位为 `3D-aware compositional synthesis；latent confidence-aware expert modulation；interaction-aware attention`，评价定位为 `visual-generation benchmarks；simulated robot planning；real-world robot experiments`，限制或反证定位为 `extreme viewpoints；fixed-view source；49-frame generation around two minutes`。

采用边界：证据支持 confidence-aware view completion 作为派生数据生成机制；不支持把生成 novel view 当作持久 world state 或可执行 transition。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；现有命题：多视角生成、几何状态和可执行 transition 是不同责任；派生视图必须保留 source/camera/projection identity 与回退；比较：现有小节已把 projective 4D state 与视觉生成分责，并要求几何/相机/provenance；Embody4D 提供 copy/repair/inpaint 的具体数据引擎，但没有改变 world-state owner 或实时控制边界。最终处置已通过独立复核。

### [Selector-Guided Autonomous Curriculum for One-Shot Reinforcement Learning from Verifiable Rewards](https://arxiv.org/html/2605.01823v1)

准入时需核验的设计变化是：用成功率、输出分歧与难度学习选择 RLVR 样本，替代 reward variance 单启发式 curriculum。exact-v1 的机制定位为 `2.4 Reward Design in RLVR；3 Methodology`，评价定位为 `3.1.1 Experiment Setup；3.3.4 Phase D: Periodic Evaluation；4 Experimental Results`，限制或反证定位为 `5.5 Limitations；6 Conclusion`。

机制证据摘要：The selection of the reward function is critical for determining the behavior of RLVR training. The binary correctness reward ( r ∈ { 0 , 1 } r\in\{0,1\} ) is the simplest and most common type, but other types have been proposed. The Process Reward Model (PRM) [ 16 ] provides step-by-step feedback for the process of solving the problem, possibly resulting in a more informative signal compared to the final reward only. Soft rewards based on answer proximity and format compliance have also been investigated [ 17 ] .…

评价证据摘要：We pick a small number of N = 4 N=4 candidate training tasks from the Hendrycks’ MATH benchmark [ 18 ] carefully selected from diverse levels of difficulty (Levels 2 to 5) and various types of mathematical tasks. For each candidate task q i q_{i} , we conduct two measurement phases. Phase 1 – Signal Collection : Using the base Qwen2.5-Math-1.5B model, we generate K = 8 K=8 samples for each candidate problem q i q_{i} . Specifically, we use stochastic decoding with temperature T = 1.0 T=1.0 and up to 1024 tokens ad…

限制证据摘要：There are several weaknesses of our approach that need to be mentioned: 1. Small test set size : In our experiments, we used 50 out-of-distribution examples for testing, which means that there can be a low amount of resolution in terms of accuracy estimates. For example, an increase in 2 percentage points from 66% to 68% accuracy means solving just one more problem than previously. While the trend is positive and cl…

采用边界：机制锚点为 2.4 Reward Design in RLVR, 3 Methodology；评价锚点为 3.1.1 Experiment Setup, 3.3.4 Phase D: Periodic Evaluation, 4 Experimental Results。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md)；最终处置已通过独立复核。

### [nvPAX: Constrained Optimization for Dynamic Power Allocation in Hierarchical and Multi-Tenant Systems](https://arxiv.org/html/2605.01837v1)

准入时需核验的设计变化是：在层级供电与多租户合同下用逐控制周期可行优化分配 GPU power budget。exact-v1 的机制定位为 `4 Algorithmic Framework；A.1 Greedy Proportional Algorithm`，评价定位为 `5 Experiments；5.4 Evaluation Metrics；5.5 Results`，限制或反证定位为 `6 Conclusion；B.4 Discussion`。

机制证据摘要：In this section, we derive our power allocation algorithm that satisfies all requirements stated in Section 3 . We start by setting the required notation in Section 4.1 , and formulate the constraints in Section 4.2 . Then, in Section 4.3 , we present nvPAX , a hybrid QP/LP constrained-optimization approach: Phase I uses a convex quadratic program (QP) for priority-ordered request satisfaction, while Phases II and III use linear programs (LPs) for max-min surplus redistribution. This decomposition keeps all physic…

评价证据摘要：We evaluate nvPAX on a large-scale simulation constructed from GPU power telemetry from a production datacenter. We compare its power allocations against static equal-share and greedy proportional baselines explained below. All experiments were run on an Apple M4 Pro with 14 cores and 48 GiB RAM. The software stack was Python 3.13.9, SciPy 1.16.3, HiGHS LP solver implemented by highspy Python bindings (version 1.12.0), and Clarabel (from clarabel version 0.11.1) for the Phase I QP. This reflects a deliberate desig…

限制证据摘要：This paper presented a hybrid QP/LP constrained-optimization algorithm for dynamic power allocation in hierarchical, multi-tenant datacenters. The algorithm extends existing power capping frameworks by supporting a full tree-structured PDN and tenant SLA constraints (e.g., minimum and maximum power guarantees per tenant), while satisfying device limits and delivering priority-aware, fair allocation. Empirical result…

采用边界：机制锚点为 4 Algorithmic Framework, A.1 Greedy Proportional Algorithm；评价锚点为 5 Experiments, 5.4 Evaluation Metrics, 5.5 Results。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `PLATFORM-GPU-SCHEDULER` / [Ch63](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)；最终处置已通过独立复核。

### [The Cylindrical Representation Hypothesis for Language Model Steering](https://arxiv.org/html/2605.01844v1)

准入时需核验的设计变化是：以圆柱几何解释同一 steering 方向在不同样本相位下产生不稳定效果，并给出敏感扇区。exact-v1 的机制定位为 `5.2 Visualization and Analysis；I.2.1 Steering Methods`，评价定位为 `5.1 Probing Experiment Setup；6.2 Experimental Validation；6.2.1 Experimental Setup`，限制或反证定位为 `2 Limitations of the Linear Representation Hypothesis；7 Conclusion and Future Work；Appendix A Limitations`。

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `No Change — Existing Coverage (proposition comparison; independent review required)`，目标 owner 为 `WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；现有命题：本章已否定单一全局线性方向的充分性，并要求 sample-conditioned geometry 与副作用测量；该假说属于受限解释；比较：exact-v1 的新增证据是“以圆柱几何解释同一 steering 方向在不同样本相位下产生不稳定效果，并给出敏感扇区”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。最终处置已通过独立复核。

### [NeuroState-Bench: A Human-Calibrated Benchmark for Commitment Integrity in LLM Agent Profiles](https://arxiv.org/html/2605.01847v1)

准入时需核验的设计变化是：Agent profile 的 task outcome 与 commitment integrity 必须分轴验收；最终答对不能证明承诺、偏好或状态约束被持续遵守。。exact-v1 的机制定位为 `§Benchmark Design；§Human Calibration；§Evaluation Protocol`，评价定位为 `§Results；144 deterministic tasks, 306 probes and 32 profiles`，限制或反证定位为 `§Discussion；profile/task and human-calibration scope`。

机制证据摘要：Outcome-only evaluation under-specifies whether an evaluated agent profile preserves the commitments required to solve a multi-turn task coherently. NeuroState-Bench is a human-calibrated benchmark that operationalizes commitment integrity through benchmark-defined side-query probes rather than inferred hidden activations. The released inventory contains 144 deterministic tasks and 306 benchmark-defined side-query probes spanning eight cognitively motivated failure families, paired clean and distractor variants, a…

评价证据摘要：Outcome-only evaluation under-specifies whether an evaluated agent profile preserves the commitments required to solve a multi-turn task coherently. NeuroState-Bench is a human-calibrated benchmark that operationalizes commitment integrity through benchmark-defined side-query probes rather than inferred hidden activations. The released inventory contains 144 deterministic tasks and 306 benchmark-defined side-query probes spanning eight cognitively motivated failure families, paired clean and distractor variants, a…

限制证据摘要：只支持 exact-v1 披露的任务、模型、环境和 evaluator；未披露的跨域、生产与长期稳定性不得外推。

采用边界：Agent profile 的 task outcome 与 commitment integrity 必须分轴验收；最终答对不能证明承诺、偏好或状态约束被持续遵守。 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)；现有命题：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner；比较：现有命题已经规定：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner。本来源的受限增量是“Agent profile 的 task outcome 与 commitment integrity 必须分轴验收；最终答对不能证明承诺、偏好或状态约束被持续遵守。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Decouple and Cache: KV Cache Construction for Streaming Video Understanding](https://arxiv.org/html/2605.01858v1)

准入时需核验的设计变化是：流式视频把 KV 构建与帧到达解耦，避免每次更新重算全部视觉历史。exact-v1 的机制定位为 `4 Methodology；5.4 Runtime Analysis`，评价定位为 `5.1 Experimental Setup；5.2 Main Results`，限制或反证定位为 `6 Conclusion`。

机制证据摘要：We propose Decoupled Streaming Cache (DSCache), a mechanism for KV cache construction and maintenance in streaming settings. To enable position extrapolation beyond the training length, DSCache incorporates a position-agnostic encoding strategy, enabling flexible cache construction for unbounded streaming ( Section 4.1 ). At each time step, DSCache updates a cumulative past KV cache based on the incoming inputs, aggregating historical context while maintaining a fixed memory budget via cache eviction ( Section 4.2…

评价证据摘要：Benchmarks. We primarily evaluate our approach on multiple StreamingVQA benchmarks. StreamingBench ( Lin et al., 2024 ) is widely adopted; we focus on the real-time visual understanding task, which contains 500 videos with 2500 QA-pairs. OVO-Bench ( Niu et al., 2025 ) evaluates real-time perception along with complementary capabilities of backward tracing and forward active responding, comprising 644 videos with 3035 QA-pairs. RVS-Ego and RVS-Movie ( Zhang et al., 2024 ) serve as additional streaming testbeds for…

限制证据摘要：This paper presents DSCache, a training-free method for adapting offline models to streaming inference under strict resource and efficiency constraints. Building on a position-agnostic encoding strategy, DSCache enables unbounded streaming by mitigating the issue of position extrapolation. Meanwhile, by decoupling cumulative and instant cache construction, it prevents the cumulative past KV cache from interfering wi…

采用边界：机制锚点为 4 Methodology, 5.4 Runtime Analysis；评价锚点为 5.1 Experimental Setup, 5.2 Main Results。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；现有命题：多模态表示必须保留时间、模态与来源身份，不能只比较 token 数量；比较：现有命题已经规定：多模态表示必须保留时间、模态与来源身份，不能只比较 token 数量。本来源的受限增量是“流式视频把 KV 构建与帧到达解耦，避免每次更新重算全部视觉历史”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Divide and Conquer: Decoupled Representation Alignment for Multimodal World Models](https://arxiv.org/html/2605.01896v1)

准入时需核验的设计变化是：从 diffusion 中间表示分离 RGB/depth/mask 的模态特征，分别对齐 DINO、Depth 与 segmentation experts，并用 decoupling regularizer 保持互补。。exact-v1 的机制定位为 `multi-modal representation alignment loss；modality-specific decoupling regularization；expert foundation-model targets`，评价定位为 `RGB/depth/mask joint generation；visual quality and long-term consistency；alignment/decoupling ablations`，限制或反证定位为 `expert-target dependence；additional training compute；generation-benchmark scope`。

采用边界：来源支持多目标对齐时先分开 modality-specific representation owner；不证明 expert embedding 是世界真值或联合生成已具有可执行性。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；现有命题：语义、时空与行动对齐承担不同目标，多目标 loss 需要保留各自信息责任，不能由单一距离替代；比较：现有小节已明确不同 alignment target 与 reconstruction/semantic/action loss 的冲突；M2-REPA 是 RGB/depth/mask expert 的具体实现，没有改变该多目标分责原则。最终处置已通过独立复核。

### [Disentangling Intent from Role: Adversarial Self-Play for Persona-Invariant Safety Alignment](https://arxiv.org/html/2605.01899v1)

准入时需核验的设计变化是：用 persona lineage 的对抗自博弈产生攻击，再以 persona-invariant consistency 降低角色表面变化对安全判断的影响。exact-v1 的机制定位为 `3 Preliminaries and Theoretical Mechanism；3.2 Theoretical Mechanism；4 Methods`，评价定位为 `5 Experiments；5.1 Experiment Settings；5.4 Ablation Studies`，限制或反证定位为 `6 Conclusion`。

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `No Change — Existing Coverage (proposition comparison; independent review required)`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有命题：本章已要求跨 persona、上下文和多轮变体做安全一致性测试；该训练方案未改变安全 gate；比较：exact-v1 的新增证据是“用 persona lineage 的对抗自博弈产生攻击，再以 persona-invariant consistency 降低角色表面变化对安全判断的影响”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。最终处置已通过独立复核。

### [Stochastic Sparse Attention for Memory-Bound Inference](https://arxiv.org/html/2605.01910v1)

准入时需核验的设计变化是：随机稀疏选择用可控近似换取 memory-bound attention 的访问缩减。exact-v1 的机制定位为 `2.1 S2S^{2}ANTA: stratified and systematic sampling；Construction.；Remark A.5 (Systematic vs. independent).`，评价定位为 `3.4 Kernel results at long contexts (32k)；4 General reasoning & accuracy verification；4.3 Long context benchmarks`，限制或反证定位为 `7 Conclusion`。

采用边界：机制锚点为 2.1 S2S^{2}ANTA: stratified and systematic sampling, Construction., Remark A.5 (Systematic vs. independent).；评价锚点为 3.4 Kernel results at long contexts (32k), 4 General reasoning & accuracy verification, 4.3 Long context benchmarks。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；现有命题：稀疏 attention 读取的是带 model/position/selection identity 的派生状态，近似选择必须保存误差与 full-context fallback；比较：Stochastic Sparse Attention 用随机选择换 memory-bound 访问缩减；现有小节已经覆盖稀疏派生状态、选择误差、身份和 FullKV 回退，故不改变长期命题。 仍待非作者逐命题复核。最终处置已通过独立复核。

### [RefusalGuard: Geometry-Preserving Fine-Tuning for Safety in LLMs](https://arxiv.org/html/2605.01913v1)

准入时需核验的设计变化是：将 safety-relevant representation drift 转化为 fine-tuning update 的显式约束与发布传感器。exact-v1 的机制定位为 `§2.1 Refusal Geometry；§3.3 Geometry-Preservation Penalty；§3.4 Training Objective`，评价定位为 `§4 Experimental Setup；§5 Main Results；§5.3 Benign Fine-Tuning；§5.4 Ablations`，限制或反证定位为 `Controlled harmful-fine-tuning setup；Geometry and λ ablations；Threat-model boundary`。

机制证据摘要：方法从冻结 base model 提取 refusal cone/reference geometry，比较适配前后漂移，并在训练时惩罚 intervention update 向 refusal subspace 的投影；base 参数冻结，只优化 intervention 参数。

评价证据摘要：作者测试 Gemma 2、Qwen2.5 与 Llama 3.1 若干规模，在 AdvBench、DirectHarm4、JailbreakBench 与 GSM8K/OpenOrca/ARC 上比较安全和 utility。10 条合成 harmful examples 是受控 stress test，不是现实训练分布；benign GSM8K 结果也只覆盖文中模型。

限制证据摘要：拒答几何由内部层、样本和提取方式定义，不能视为跨模型普适 safety truth；更强 penalty 降低 ASR 同时会约束 utility。白盒访问、layer choice、adaptive attack 与分布外行为均未被完整证明。

采用边界：exact-v1 支持所列开源模型、benchmark 与受控 fine-tuning stress；不证明 refusal geometry 是普适因果机制，也不取代行为 red-team、adaptive attack、utility regression 或独立 release gate。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent post-write review complete`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有覆盖差异：现有命题覆盖样本风险与事后 weight repair，却未说明 downstream update 即使保持 task utility，也可能沿 safety-mediating subspace 漂移，以及如何在训练时限制该投影。最终处置已通过独立复核。

### [A Language for Describing Agentic LLM Contexts](https://arxiv.org/html/2605.01920v1)

准入时需核验的设计变化是：用可描述的 context schema 标注 Agent 所见信息、来源和作用域。exact-v1 的机制定位为 `2. Preliminaries: Agentic Systems Terminology`，评价定位为 `Appendix A The MINT Experiment`，限制或反证定位为 `7. Discussion；Limitations.`。

采用边界：机制锚点为 2. Preliminaries: Agentic Systems Terminology；评价锚点为 Appendix A The MINT Experiment。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `AGENT-CONTEXT` / [Ch75](../../../../books/part-07-agent/75-context.md)；现有命题：原始事实状态、派生视图与 context mutation 的提交权必须分离；比较：现有命题已经规定：原始事实状态、派生视图与 context mutation 的提交权必须分离。本来源的受限增量是“用可描述的 context schema 标注 Agent 所见信息、来源和作用域”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Training Non-Differentiable Networks via Optimal Transport](https://arxiv.org/html/2605.01928v1)

准入时需核验的设计变化是：对含离散跳变的网络以固定分辨率 stationarity 和 forward-only transport step 替代不存在的梯度。exact-v1 的机制定位为 `2.2 Spiking Neural Networks and Non-Differentiable Models；3 Algorithm；3.1 Problem Formulation`，评价定位为 `4 Theoretical Analysis；Proof sketch.；Empirical anchor.`，限制或反证定位为 `Limitations.；6.3 Limitations`。

机制证据摘要：Spiking neural networks (SNNs) use binary spike events as activations, introducing hard non-differentiability at each spike threshold. Surrogate gradient methods ( Neftci et al., 2019 ) circumvent this by replacing the spike function with a smooth surrogate during the backward pass, enabling gradient flow through temporal unrolling (BPTT). Surrogate gradients achieve high accuracy on neuromorphic benchmarks but require storing the full computational graph across T T timesteps: O ⁡ ( T ) O(T) memory. Memory-efficie…

评价证据摘要：This section provides the theoretical foundation that supports PolyStep’s empirical results. We prove three statements that together explain why a forward-only optimizer can train networks where gradients either do not exist or are systematically biased. Theorem 4.1 (Section 4.1 ) characterizes the KL-softmax solver as a continuous interpolation between the closed-form softmax limit ( λ → 0 \lambda\!\to\!0 ) and full Sinkhorn ( λ → ∞ \lambda\!\to\!\infty ), with monotone tightening of the column-marginal violation…

限制证据摘要：A full discussion appears in Section 6.3 ; we summarize the key failure mode. On SST-2 ( Socher et al., 2013 ) (4.2M-parameter transformer trained from scratch), all gradient-free methods collapse to near-random accuracy (PolyStep: 49.4%, SPSA: 53.1%, seed 42). This is not a solver limitation but a structural one: the rank-64 subspace captures < < 0.002% of the full parameter space, leaving the optimizer with an eff…

采用边界：机制锚点为 2.2 Spiking Neural Networks and Non-Differentiable Models, 3 Algorithm, 3.1 Problem Formulation；评价锚点为 4 Theoretical Analysis, Proof sketch., Empirical anchor.。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；最终处置已通过独立复核。

### [Exploring Data-Free LoRA Transferability for Video Diffusion Models](https://arxiv.org/html/2605.01929v1)

准入时需核验的设计变化是：在无目标数据时按谱刚性聚类 LoRA，并仲裁 video-diffusion 变体间的 routing interference。exact-v1 的机制定位为 `Weight Space Analysis of Model Adaptation.；3 Analysis；4 Methodology`，评价定位为 `5 Experiments；5.1 Experimental Settings；5.2 Main Results`，限制或反证定位为 `6 Conclusion；B.2.2 Over-Activation of Dominant Routing Blocks and Generative Failure；D.1 Discussion and Guideline for Hyperparameter Selection`。

机制证据摘要：Understanding how fine-tuning modifies pretrained models in the weight space has attracted increasing attention. Prior works ( Liu et al., 2024 ; Fan et al., 2025 ; Meng et al., 2024 ; Si et al., 2025b ; Shuttleworth et al., 2025 ; Si et al., 2024 ; Si et al., 2025a ) have analyzed the effect of full fine-tuning and LoRAs from a weight space perspective, often by leveraging singular value decomposition (SVD) to study spectral properties induced by adaptation. However, existing analyses are largely limited to LLMs…

评价证据摘要：In this section, we will evaluate the effectiveness of CASA on the task of transferring LoRAs trained on a base video diffusion model to its distilled variants. Moreover, we conduct ablation study and analysis to validate the design choices. Additional analyses are provided in Appendix D . Table 1 : Comparison of direct LoRA reuse and transferring LoRA with CASA on distilled VDMs. Best results are bold. LoRA Target Model Method Quality Score CSD ( % \% ) Steamboat-Willie -1.3B FastWan2.1-T2V-1.3B Direct Reuse 1.27…

限制证据摘要：We studied why LoRAs trained on base video diffusion models often fail when reused on distilled variants. Through a weight-space analysis, we uncovered a pronounced spectral rigidity in VDMs and showed that both full fine-tuning and LoRA primarily introduce structured routing patterns at the cluster level, with incompatibility arising from conflicting routing interactions within spectrally functional subspaces. Moti…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `TRAIN-LORA` / [Ch30](../../../../books/part-04-training-system/30-lora.md)；现有覆盖差异：现有正文仍缺：在无目标数据时按谱刚性聚类 LoRA，并仲裁 video-diffusion 变体间的 routing interference。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。最终处置已通过独立复核。

### [GPU Fingerprinting for Location Verification](https://arxiv.org/html/2605.01930v1)

准入时需核验的设计变化是：用硬件物理 fingerprint 替代可被提取的片上密钥以绑定 GPU location identity。exact-v1 的机制定位为 `2 Fingerprint-Based Device Identification；3 Proof-of-Concept Fingerprinting Function`，评价定位为 `GPU Fingerprinting for Location Verification；3 Proof-of-Concept Fingerprinting Function；4 Evaluation`，限制或反证定位为 `5 Limitations and Future Work；6 Conclusion`。

机制证据摘要：Prior work on GPU fingerprinting methods and Physically Unclonable Functions (PUFs) has shown that GPUs are not perfectly identical ( Forlin et al., 2020 ; Hohentanner et al., 2025 ; Laor et al., 2022 ; Laor & Oren, 2025 ) . Rather, the manufacturing process produces hardware differences between chips that can be measured by fingerprinting functions in order to identify and authenticate chips. We propose using these functions to secure the location verification process as follows: Before chips are sold, they go th…

评价证据摘要：Wayne Tee Affiliation: Pivotal Research Correspondence to: waynetee37@gmail.com Jonathan Happel Affiliation: TamperSec In this section, we present a proof-of-concept fingerprinting function. Hohentanner et al. ( 2025 ) previously showed that GPUs can be fingerprinted using atomic operations. In their atomicIncrement approach, multiple threads race in parallel to read and increment a global counter. The values read by each thread reflect the order in which they manage to access the counter. As this order varies acr…

限制证据摘要：We have presented a proof-of-concept fingerprinting function. While the results show good accuracy, more research would be needed before it can be confidently deployed. Scale. The function will need to be validated on a larger scale, across more GPUs and seeds to ensure that the fingerprints are sufficiently unique. In order to distinguish among a larger number of GPUs, it is likely that more fingerprints would have…

采用边界：机制锚点为 2 Fingerprint-Based Device Identification, 3 Proof-of-Concept Fingerprinting Function；评价锚点为 GPU Fingerprinting for Location Verification, 3 Proof-of-Concept Fingerprinting Function, 4 Evaluation。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；最终处置已通过独立复核。

### [Pandora's Regret: A Proper Scoring Rule for Evaluating Sequential Search](https://arxiv.org/html/2605.01936v1)

准入时需核验的设计变化是：从顺序搜索成本导出同时约束概率校准与竞争项排序的 proper scoring rule。exact-v1 的机制定位为 `Sequential search and clinical decision theory.；3 Pandora’s Regret11 1 With apologies to connoisseurs of Greek mythology and economic search theory.；Theorem 3.1 (Search cost decomposition).`，评价定位为 `2.2 Bilevel Evaluation；5 Empirical Validation；5.2 Model Ranking Meta-evaluation`，限制或反证定位为 `6 Conclusion, Limitations, and Future Work`。

机制证据摘要：Sequencing tests by probability / cost ratio is a classic idea in economic decision theory and operations research. Our starting point is the Pandora problem formulation of Weitzman (1979) , although Matula (1964) reports Blackwell already knew about the optimal search policy. Threshold-based analysis for a single diagnosis entered the clinical decision theory literature with Pauker and Kassirer (1980) , and although Eiseman et al. (1989) gave a bespoke analysis for two conditions, the core of the sequential decis…

评价证据摘要：The sequential search rule describes how an individual clinician should act given predicted probabilities and local testing costs. Evaluation, however, is a different problem. The model developer or evaluator does not act on a single patient. Instead, they choose a model or scoring rule that will be used across many downstream decisions, often under varying operational conditions. A metric intended to guide model selection should therefore reflect uncertainty not only over patients, but also over the operational c…

限制证据摘要：Evaluation criteria are products of the decisions they support. In sequential settings, where costs accrue as alternatives are ruled out, forecast quality depends not just on the probability assigned to the true class, but on how competing alternatives are ordered. We formalize this as an optimal search problem and derive a corresponding class of scoring rules. The resulting score, Pandora’s Regret, is strictly prop…

采用边界：机制锚点为 Sequential search and clinical decision theory., 3 Pandora’s Regret11 1 With apologies to connoisseurs of Greek mythology and economic search theory., Theorem 3.1 (Search cost decomposition).；评价锚点为 2.2 Bilevel Evaluation, 5 Empirical Validation, 5.2 Model Ranking Meta-evaluation。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；最终处置已通过独立复核。

### [Cross-Layer Energy Analysis of Multimodal Training on Grace Hopper Superchips](https://arxiv.org/html/2605.01938v1)

准入时需核验的设计变化是：跨层测量把 GH200 多模态训练的能耗归因到数据移动而非只归因 FLOPs。exact-v1 的机制定位为 `II System and Runtime Overview；II-A NVIDIA GH200 Architecture`，评价定位为 `Cross-Layer Energy Analysis of Multimodal Training on Grace Hopper Superchips；III Measurement Methodology；III-A Experimental Platform`，限制或反证定位为 `V Discussion and Outcomes；VI Conclusion`。

采用边界：机制锚点为 II System and Runtime Overview, II-A NVIDIA GH200 Architecture；评价锚点为 Cross-Layer Energy Analysis of Multimodal Training on Grace Hopper Superchips, III Measurement Methodology, III-A Experimental Platform。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；现有命题：多模态表示必须保留时间、模态与来源身份，不能只比较 token 数量；比较：现有命题已经规定：多模态表示必须保留时间、模态与来源身份，不能只比较 token 数量。本来源的受限增量是“跨层测量把 GH200 多模态训练的能耗归因到数据移动而非只归因 FLOPs”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Phone2Act: A Low-Cost, Hardware-Agnostic Teleoperation System for Scalable VLA Data Collection](https://arxiv.org/html/2605.01948v1)

准入时需核验的设计变化是：用手机 6-DoF pose、可替换 ROS 2 bridge 与同步 recorder 把 teleoperation 控制和特定机器人硬件解耦，并直接产出 LeRobot 格式的 VLA 训练记录。。exact-v1 的机制定位为 `ARCore 6-DoF controller；interchangeable ROS 2 bridge nodes；Universal Recorder`，评价定位为 `130 demonstration episodes；GR00T-N1.5 fine-tuning；Dobot CR5 pick-and-place`，限制或反证定位为 `single task and robot deployment；ARCore/calibration dependence；no safety-tail evaluation`。

采用边界：证据支持把采集控制、robot bridge、时间同步和训练记录拆成可版本化接口；不证明低成本 teleoperation 数据自动具有跨机器人可迁移性。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `TRAIN-DATA` / [Ch27](../../../../books/part-04-training-system/27-data.md)；现有命题：teleoperation 派生轨迹必须绑定输入设备、时间同步、robot schema、retarget/bridge 与真实闭环验证；比较：现有小节已规定 teleoperation 到派生 robot trajectory 的 schema、provenance、per-embodiment adaptation 与真实控制验收；Phone2Act 补充手机/ROS2/LeRobot 案例，没有改变数据 owner 或跨 embodiment 边界。最终处置已通过独立复核。

### [TRAP: Tail-aware Ranking Attack for World-Model Planning](https://arxiv.org/html/2605.01950v1)

准入时需核验的设计变化是：tail-aware ranking attack 表明 world-model planner 的候选轨迹排序本身是攻击面。exact-v1 的机制定位为 `2.1. World Models；2.3. Security of Model-Based Reinforcement Learning and World Models`，评价定位为 `5.1. Experimental Setup；5.2. Main Results`，限制或反证定位为 `3.2. Threat Model；6. Conclusion`。

采用边界：机制锚点为 2.1. World Models, 2.3. Security of Model-Based Reinforcement Learning and World Models；评价锚点为 5.1. Experimental Setup, 5.2. Main Results。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；现有命题：生成外观、环境 transition 与可修订 world state 是不同责任；比较：现有命题已经规定：生成外观、环境 transition 与可修订 world state 是不同责任。本来源的受限增量是“tail-aware ranking attack 表明 world-model planner 的候选轨迹排序本身是攻击面”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Flexi-LoRA with Input-Adaptive Ranks: Efficient Finetuning for Speech and Reasoning Tasks](https://arxiv.org/html/2605.01959v1)

准入时需核验的设计变化是：以输入条件 router 在训练和推理阶段选择 LoRA rank，令 adapter capacity 成为运行时状态。exact-v1 的机制定位为 `§3 Flexi-LoRA；Difficulty-aware rank router；Rank slicing and rank-specific scaling`，评价定位为 `§4 Experimental Setup；§5 Results；Ablation studies`，限制或反证定位为 `Router and difficulty-label design；Future work: layer-wise ranks；Undisclosed serving cost`。

机制证据摘要：router 从 mean-pooled input embeddings 预测 rank；训练标签由任务 difficulty metric 构造并用加噪交叉熵学习。所选 rank 在所有 transformer layers 一致切取 LoRA 因子的前 r 个维度，并使用 rank-specific alpha；训练与推理均运行同一 router。

评价证据摘要：作者在 Llama 3.2 1B/3B、Whisper 与 QA、数学、语音任务上报告 parameter/quality 结果。论文没有给出生产 batch、kernel shape、端到端 latency、hardware SLO 或动态 rank serving 成本。

限制证据摘要：同一 sample rank 施加到全部层，layer-specific allocation 尚未处理；difficulty labels 依赖任务 metric，router 错误会错配 capacity。动态 per-sample rank 可能碎片化 batching/compiled shape，论文没有证明实际延迟收益。

采用边界：exact-v1 只支持作者 QA/数学/语音任务与小规模 Llama/Whisper；trainable-parameter 减少不等于 FLOPs、latency 或 fleet cost 改善，也不证明 rank policy 跨任务可迁移。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent post-write review complete`，目标 owner 为 `TRAIN-LORA` / [Ch30](../../../../books/part-04-training-system/30-lora.md)；现有覆盖差异：现有命题没有覆盖 sample-conditioned rank router，也未把训练—推理 rank policy、difficulty-label provenance 和动态 shape serving 成本纳入 adapter identity。最终处置已通过独立复核。

### [Trojan Hippo: Weaponizing Agent Memory for Data Exfiltration](https://arxiv.org/html/2605.01970v1)

准入时需核验的设计变化是：恶意内容可写入持久 Agent memory，并在后续会话恢复时触发数据外泄。exact-v1 的机制定位为 `This Work: Systematically Evaluating the Risk of Memory-Based Attacks；3. Threat Model；3.1. Adversary Model`，评价定位为 `Evaluation Summary；Defenses, Evaluation, and the Need for Dynamic Benchmarking.；4.1. Attack Benchmark`，限制或反证定位为 `3. Threat Model；8. Conclusion；Conclusion.`。

机制证据摘要：We carry out a systematic study that shows how realistic memory attacks can be made reproducible, reliable, and automatically deployable under a realistic threat model. We introduce an evaluation framework that assesses the feasibility of attacks and defenses based on three core principles: Realism , Adaptiveness , and Capability Trade-Off . (1) Realism. We formally characterize the Trojan Hippo attack 2 2 2 The name Trojan Hippo combines Trojan , denoting a payload that hides in memory until triggered, as in the…

评价证据摘要：Without defenses, Trojan Hippo achieves up to 85–100% attack success rate (ASR) (see Fig. 1 ), even against frontier safety-aligned models from Google ( gemini-3.1-pro ( Google DeepMind, 2026 ) ) and OpenAI ( gpt-5-mini ( OpenAI, 2025a ) ). The attack can persist even for 100 or more benign sessions after it was introduced. The four defenses evaluated in this work reduce the ASR significantly, to 0–5% in most configurations, with the provably secure and most restrictive bringing ASR to 0% in all cases. However, as…

限制证据摘要：We consider an LLM-based agent that (1) maintains a persistent memory store populated automatically from conversation history across sessions, and (2) is equipped with tools that read from external, untrusted data sources and tools that can transmit data to external destinations. This describes a broad and increasingly common class of deployed agents, including email assistants, web-browsing agents, document-process…

采用边界：机制锚点为 This Work: Systematically Evaluating the Risk of Memory-Based Attacks, 3. Threat Model, 3.1. Adversary Model；评价锚点为 Evaluation Summary, Defenses, Evaluation, and the Need for Dynamic Benchmarking., 4.1. Attack Benchmark。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)；现有命题：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner；比较：现有命题已经规定：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner。本来源的受限增量是“恶意内容可写入持久 Agent memory，并在后续会话恢复时触发数据外泄”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [DBLP: Phase-Aware Bounded-Loss Transport for Burst-Resilient Distributed ML Training](https://arxiv.org/html/2605.01989v1)

准入时需核验的设计变化是：按训练 phase 与 loss budget 选择有损/可靠传输 fallback，而非统一可靠协议。exact-v1 的机制定位为 `III Design of DBLP；IV-D Centralized All-Reduce Architecture；V-A2 Models and Datasets`，评价定位为 `II-C Preliminary Experiment Results；IV Implementation`，限制或反证定位为 `VII Conclusion`。

采用边界：机制锚点为 III Design of DBLP, IV-D Centralized All-Reduce Architecture, V-A2 Models and Datasets；评价锚点为 II-C Preliminary Experiment Results, IV Implementation。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (marker verified)`，目标 owner 为 `TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)；现有命题：资源可用性、通信完成与全局更新语义必须共同进入一轮训练合同；比较：现有命题已经规定：资源可用性、通信完成与全局更新语义必须共同进入一轮训练合同。本来源的受限增量是“按训练 phase 与 loss budget 选择有损/可靠传输 fallback，而非统一可靠协议”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Counting as a minimal probe of language model reliability](https://arxiv.org/html/2605.02028v1)

准入时需核验的设计变化是：extended rule following 暴露模型对有限内部规则状态的持续更新失败。exact-v1 的机制定位为 `Counting as a minimal probe of language model reliability；2 Model dynamics when counting fails；3 Probing bounded state trajectories within models`，评价定位为 `4 Comparing SCC with standard benchmarks；Model set and evaluation scope；Cross-benchmark alignment and paired analyses`，限制或反证定位为 `5 Discussion`。

采用边界：机制锚点为 Counting as a minimal probe of language model reliability, 2 Model dynamics when counting fails, 3 Probing bounded state trajectories within models；评价锚点为 4 Comparing SCC with standard benchmarks, Model set and evaluation scope, Cross-benchmark alignment and paired analyses。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“extended rule following 暴露模型对有限内部规则状态的持续更新失败”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [VILAS: A VLA-Integrated Low-cost Architecture with Soft Grasping for Robotic Manipulation](https://arxiv.org/html/2605.02037v1)

准入时需核验的设计变化是：以模块化硬件、统一采集/部署数据流和一致 demonstrations 暴露 VLA 的真实部署边界。exact-v1 的机制定位为 `3.1 System Architecture`，评价定位为 `4.1 Experimental Setup；4.3 Evaluation Protocol`，限制或反证定位为 `4.6 Failure Analysis；5 Conclusion and Future Work`。

采用边界：机制锚点为 3.1 System Architecture；评价锚点为 4.1 Experimental Setup, 4.3 Evaluation Protocol。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；现有命题：行动闭环必须绑定 observation、action schema、控制频率与安全回退；比较：现有命题已经规定：行动闭环必须绑定 observation、action schema、控制频率与安全回退。本来源的受限增量是“以模块化硬件、统一采集/部署数据流和一致 demonstrations 暴露 VLA 的真实部署边界”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [What Single-Prompt Accuracy Misses: A Multi-Variant Reliability Audit of Language Models](https://arxiv.org/html/2605.02038v1)

准入时需核验的设计变化是：同一任务的 prompt variants 揭示单提示 accuracy 无法度量服务可靠性。exact-v1 的机制定位为 `Calibration and verbal confidence in language models:；Prompt sensitivity and evaluation design:`，评价定位为 `Prompt sensitivity and evaluation design:；Evaluation of small open-weight models:；4.1 Finding 1 — Evaluation choices can create or hide failures`，限制或反证定位为 `4.1 Finding 1 — Evaluation choices can create or hide failures；6 Limitations；7 Conclusion`。

采用边界：机制锚点为 Calibration and verbal confidence in language models:, Prompt sensitivity and evaluation design:；评价锚点为 Prompt sensitivity and evaluation design:, Evaluation of small open-weight models:, 4.1 Finding 1 — Evaluation choices can create or hide failures。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (marker verified)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“同一任务的 prompt variants 揭示单提示 accuracy 无法度量服务可靠性”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Bringing Order to Asynchronous SGD: Towards Optimality under Data-Dependent Delays with Momentum](https://arxiv.org/html/2605.02043v1)

准入时需核验的设计变化是：异步 SGD 的 data-dependent delay 与 momentum 必须联合校正才能保持更新语义。exact-v1 的机制定位为 `4 Momentum-Based Asynchronous Framework；Theorem 4.1 (Nonconvex Smooth Objectives).；Theorem 5.1 (Convex Smooth Objectives).`，评价定位为 `Proof of Lemma A.1.；Proof of Lemma A.2.`，限制或反证定位为 `6 Conclusions and Future Work`。

采用边界：机制锚点为 4 Momentum-Based Asynchronous Framework, Theorem 4.1 (Nonconvex Smooth Objectives)., Theorem 5.1 (Convex Smooth Objectives).；评价锚点为 Proof of Lemma A.1., Proof of Lemma A.2.。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)；现有命题：资源可用性、通信完成与全局更新语义必须共同进入一轮训练合同；比较：现有命题已经规定：资源可用性、通信完成与全局更新语义必须共同进入一轮训练合同。本来源的受限增量是“异步 SGD 的 data-dependent delay 与 momentum 必须联合校正才能保持更新语义”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Principles and Guidelines for Randomized Controlled Trials in AI Evaluation](https://arxiv.org/html/2605.02050v1)

准入时需核验的设计变化是：AI uplift/RCT 结论必须显式冻结 intervention、population、control、outcome、power、randomization 与可复算材料；行业惯例不能替代实验身份。。exact-v1 的机制定位为 `§Five Principles；§33 Guidelines；validity and open-science evidence framework`，评价定位为 `guideline derivation and cross-discipline evidence basis；design/rubric/standard-setting uses`，限制或反证定位为 `guideline synthesis rather than a new controlled AI-system experiment`。

机制证据摘要：This work establishes a framework for standardizing AI evaluation RCTs (sometimes called human uplift studies). Drawing on established practices from disciplines with established RCT traditions, including software engineering, economics, clinical and health sciences, and psychology, we synthesize five principles drawn from established validity frameworks and open-science standards on transparency, repeatability, and verification, which together serve as the conceptual foundation for 33 actionable guidelines adapte…

评价证据摘要：This work establishes a framework for standardizing AI evaluation RCTs (sometimes called human uplift studies). Drawing on established practices from disciplines with established RCT traditions, including software engineering, economics, clinical and health sciences, and psychology, we synthesize five principles drawn from established validity frameworks and open-science standards on transparency, repeatability, and verification, which together serve as the conceptual foundation for 33 actionable guidelines adapte…

限制证据摘要：只支持 exact-v1 披露的任务、模型、环境和 evaluator；未披露的跨域、生产与长期稳定性不得外推。

采用边界：AI uplift/RCT 结论必须显式冻结 intervention、population、control、outcome、power、randomization 与可复算材料；行业惯例不能替代实验身份。 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“AI uplift/RCT 结论必须显式冻结 intervention、population、control、outcome、power、randomization 与可复算材料；行业惯例不能替代实验身份。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [EditPropBench: Measuring Factual Edit Propagation in Scientific Manuscripts](https://arxiv.org/html/2605.02083v1)

准入时需核验的设计变化是：用显式 fact graph 检查局部事实修改是否传播到依赖叙述，形成 cascade-aware artifact gate。exact-v1 的机制定位为 `3.1 Task formulation；3.4 Corpus construction and editing protocols`，评价定位为 `Evaluation, contradiction detection, and drift.`，限制或反证定位为 `Limitations.；9 Conclusion`。

机制证据摘要：Each item consists of a manuscript M M , a local edit instruction e e , and sentence-level annotations. The edit instruction specifies a target fact, its old value, and its new value. The annotations partition manuscript sentences, which we call units , into three sets: direct-target units , sentences that explicitly mention the edited fact and must use the new value; required-update units , sentences whose meaning depends on the edited fact and must also be revised; and protected units , sentences unrelated to th…

评价证据摘要：Scientific-revision and contradiction-detection work shows that evaluation depends strongly on corpus construction, alignment, reference coverage, and metric choice ( Jourdan et al., 2025b ; Chen et al., 2025b ; Kryscinski et al., 2019 ; Laban et al., 2021 ; Hou et al., 2024 ) . We therefore report both a hard-stratum analysis isolating implicit and free-form dependencies and a stress-test aggregate that includes easier cases. Because valid cascade updates may be natural paraphrases, we use reference-guided LLM ju…

限制证据摘要：First, EditPropBench prioritizes controlled fact graphs over surface indistinguishability from real arXiv prose. We deliberately do not aim to produce manuscripts that pass for real papers under a discriminator because such surface indistinguishability would conflict with exhaustive, mechanically verifiable cascade supervision. Our claim is narrower: the benchmark isolates a dependency pattern that occurs in real ma…

采用边界：机制锚点为 3.1 Task formulation, 3.4 Corpus construction and editing protocols；评价锚点为 Evaluation, contradiction detection, and drift.。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md)；最终处置已通过独立复核。

### [Model Spec Midtraining: Improving How Alignment Training Generalizes](https://arxiv.org/html/2605.02087v1)

准入时需核验的设计变化是：把行为 spec 注入 midtraining，改变 alignment generalization 的训练阶段 owner。exact-v1 的机制定位为 `2 Method；2.1 Model Spec`，评价定位为 `Evaluation；Result；Reasoning analysis`，限制或反证定位为 `9 Conclusion`。

采用边界：机制锚点为 2 Method, 2.1 Model Spec；评价锚点为 Evaluation, Result, Reasoning analysis。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (marker verified)`，目标 owner 为 `TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；现有命题：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算；比较：现有命题已经规定：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算。本来源的受限增量是“把行为 spec 注入 midtraining，改变 alignment generalization 的训练阶段 owner”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Sharpness-Aware Pretraining Mitigates Catastrophic Forgetting](https://arxiv.org/html/2605.02105v1)

准入时需核验的设计变化是：sharpness-aware pretraining 改变后续适配时 catastrophic forgetting 的初始几何条件。exact-v1 的机制定位为 `2.1 Downstream properties of the pretrained model；3.3 Implicitly minimizing base model sharpness mitigates forgetting；4 Analysis of the Hessian`，评价定位为 `3 Experiments；3.1 Experimental setup；4 Analysis of the Hessian`，限制或反证定位为 `6 Conclusion`。

采用边界：机制锚点为 2.1 Downstream properties of the pretrained model, 3.3 Implicitly minimizing base model sharpness mitigates forgetting, 4 Analysis of the Hessian；评价锚点为 3 Experiments, 3.1 Experimental setup, 4 Analysis of the Hessian。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；现有命题：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算；比较：现有命题已经规定：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算。本来源的受限增量是“sharpness-aware pretraining 改变后续适配时 catastrophic forgetting 的初始几何条件”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [The Dynamic Gist-Based Memory Model (DGMM): A Memory-Centric Architecture for Artificial Intelligence](https://arxiv.org/html/2605.02106v1)

准入时需核验的设计变化是：把带时间、来源与交互上下文的 episodic-semantic graph 设为可追加持久 memory owner。exact-v1 的机制定位为 `4. Architectural Design Principles；4.0.1. The Dynamic Gist-Based Memory Model (DGMM)`，评价定位为 `Analysis.；4.1.3. Semantic Projection Analysis；5. Theoretical Capabilities and Evaluation Pathways`，限制或反证定位为 `7. Discussion；8. Conclusion`。

机制证据摘要：DGMM is built around explicit structural principles that prioritize interpretability, consistency, and incremental adaptation. Memory is represented using a fixed schema of typed nodes and relations, separating conceptual substance from contextual modification. New experiences extend the memory structure without overwriting prior representations, reflecting a stability–plasticity balance analogous to biological memory systems. Crucially, DGMM separates memory storage from interpretation. Stored representations cap…

评价证据摘要：Analysis is the process by which recalled structure is interpreted, transformed, or evaluated to produce derived representations. Analytic operations take W q W_{q} as input and produce outputs (e.g., embeddings, propositions, surprise signals, attribution distributions) without modifying either M t M_{t} or W q W_{q} . Analysis is strictly post-recall: it presupposes a constructed working memory and has no direct access to long-term memory except through what recall has made available. Analytic outputs are transi…

限制证据摘要：DGMM reframes explainability, accountability, and continuity as properties of memory representation rather than as challenges to be addressed post hoc through model interpretation or output analysis. By treating memory as an explicit, persistent, and evolving structure, DGMM enables examination of how recall, interpretation, and attribution change over time without requiring access to internal execution procedures o…

采用边界：机制锚点为 4. Architectural Design Principles, 4.0.1. The Dynamic Gist-Based Memory Model (DGMM)；评价锚点为 Analysis., 4.1.3. Semantic Projection Analysis, 5. Theoretical Capabilities and Evaluation Pathways。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)；最终处置已通过独立复核。

### [STABLEVAL: Disagreement-Aware and Stable Evaluation of AI Systems](https://arxiv.org/html/2605.02122v1)

准入时需核验的设计变化是：Human-evaluation aggregation must preserve annotator uncertainty and ranking stability; majority vote is not a sufficient release-grade evaluation contract.。exact-v1 的机制定位为 `arXiv:2605.02122v1 HTML, Method/Design section；abstract mechanism: We introduce STABLEVAL, a disagreement-aware evaluation framework that models latent item correctness and annotator-specific confusion patterns to produce posterior expected item credit and calibrated agent-level scores.`，评价定位为 `arXiv:2605.02122v1 HTML, Experiments/Evaluation and ablation sections；abstract scope: Human evaluation remains the primary standard for assessing modern AI systems, yet annotator disagreement, bias, and variability make system rankings fragile under standard majority vote aggregation.`，限制或反证定位为 `arXiv:2605.02122v1 HTML, Discussion/Limitations and threat-to-validity passages；no cross-workload generalization inferred`。

机制证据摘要：arXiv:2605.02122v1 HTML, Method/Design section; abstract mechanism: We introduce STABLEVAL, a disagreement-aware evaluation framework that models latent item correctness and annotator-specific confusion patterns to produce posterior expected item credit and calibrated agent-level scores.；Human evaluation remains the primary standard for assessing modern AI systems, yet annotator disagreement, bias, and variability make system rankings fragile under standard majority vote aggregation. Majority vote discards annotat…

评价证据摘要：arXiv:2605.02122v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Human evaluation remains the primary standard for assessing modern AI systems, yet annotator disagreement, bias, and variability make system rankings fragile under standard majority vote aggregation.；Human evaluation remains the primary standard for assessing modern AI systems, yet annotator disagreement, bias, and variability make system rankings fragile under standard majority vote aggregation. Majority vote discards annotator…

限制证据摘要：arXiv:2605.02122v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred

采用边界：Human-evaluation aggregation must preserve annotator uncertainty and ranking stability; majority vote is not a sufficient release-grade evaluation contract. 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“Human-evaluation aggregation must preserve annotator uncertainty and ranking stability; majority vote is not a sufficient release-grade evaluation contract.”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Boundary Mass and the Soft-to-Hard Limit in Mixture-of-Experts](https://arxiv.org/html/2605.02124v1)

准入时需核验的设计变化是：soft routing 训练到 hard dispatch 的边界质量由 routing mass 演化而非只由 top-k 决定。exact-v1 的机制定位为 `2 Population MoE model and notation；Theorem 4.5 (Uniform quantitative soft-to-hard approximation).；Theorem 4.7 (Variational zero-temperature limit of the soft risks).`，评价定位为 `Proof.；7 What the Results Do and Do Not Show`，限制或反证定位为 `Not Disclosed as a standalone section`。

采用边界：机制锚点为 2 Population MoE model and notation, Theorem 4.5 (Uniform quantitative soft-to-hard approximation)., Theorem 4.7 (Variational zero-temperature limit of the soft risks).；评价锚点为 Proof., 7 What the Results Do and Do Not Show。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；现有命题：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算；比较：现有命题已经规定：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算。本来源的受限增量是“soft routing 训练到 hard dispatch 的边界质量由 routing mass 演化而非只由 top-k 决定”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [FedQueue: Queue-Aware Federated Learning for Cross-Facility HPC Training](https://arxiv.org/html/2605.02125v1)

准入时需核验的设计变化是：Cross-facility training must account for queue delay and allocation availability, not optimize communication or convergence after resources are assumed present.。exact-v1 的机制定位为 `§3 Problem Formulation；§4.1.1–4.1.5 queue prediction, work budgeting, LR scaling, admission and aggregation；§4.2 Client Algorithm；§5 Theory`，评价定位为 `§6.1 Large-Scale Cross-Facility Evaluation；§6.2 Controlled Synthetic Queue Experiments；Appendix C/D setup and sweeps`，限制或反证定位为 `§7 Conclusion and Limitations: profiled throughput and sub-Gaussian prediction error；job failures/cancellations are not modeled`。

机制证据摘要：Server-side EWMA queue prediction determines a per-facility job-time/local-step budget; inverse learning-rate scaling limits dominance by clients with more local steps; deadline admission buffers late updates and staleness-aware aggregation controls their contribution. The proof assumes bounded staleness induced under its queue-error assumptions.

评价证据摘要：§6 separates a four-production-facility APPFL deployment (two GPU nodes per client) from controlled queue simulation, and compares FedAvg, FedAsync, FedBuff and FedCompass. Reported time-to-quality and loss/accuracy changes belong to those disclosed facilities, partitions and queue sweeps.

限制证据摘要：§7 assumes facility throughput is profileable and queue-prediction errors are sub-Gaussian; adversarial/highly non-stationary queues may violate that model. Late arrivals are buffered, but job failures and cancellations that lose updates are not modeled.

采用边界：Cross-facility training must account for queue delay and allocation availability, not optimize communication or convergence after resources are assumed present. 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)；最终处置已通过独立复核。

### [Video Generation with Predictive Latents](https://arxiv.org/html/2605.02134v1)

准入时需核验的设计变化是：predictive latents 让视频生成表示承担未来状态预测而非只重建当前像素。exact-v1 的机制定位为 `3 Approach；3.1 Framework；4.3 Analysis`，评价定位为 `3.2 Implementation；4 Experiments；4.1 Experimental setups`，限制或反证定位为 `5 Discussion and Conclusion`。

采用边界：机制锚点为 3 Approach, 3.1 Framework, 4.3 Analysis；评价锚点为 3.2 Implementation, 4 Experiments, 4.1 Experimental setups。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；现有命题：生成外观、环境 transition 与可修订 world state 是不同责任；比较：现有命题已经规定：生成外观、环境 transition 与可修订 world state 是不同责任。本来源的受限增量是“predictive latents 让视频生成表示承担未来状态预测而非只重建当前像素”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Projection-Free Transformers via Gaussian Kernel Attention](https://arxiv.org/html/2605.02144v1)

准入时需核验的设计变化是：用原始 hidden-state 间 Gaussian kernel 直接构造 row-stochastic attention，移除 Q/K 投影并以 bandwidth 控制局部性。exact-v1 的机制定位为 `4.3 Efficiency Analysis；7 Attention Visualization Methodology；7.3 Learned Bandwidth (σ\sigma) Analysis`，评价定位为 `ImageNet evaluation.；4 Experiments in Vision Task；4.1 Experimental Setup`，限制或反证定位为 `Discussion and outlook.；6 Summary and Discussion；Limitations and future directions.`。

机制证据摘要：The parameter/FLOP reductions above do not directly translate into wall-clock gains. We therefore measure runtime and memory explicitly. Inference is benchmarked on a single GPU over batch sizes { 32 , 64 , 128 , 256 , 512 } \{32,64,128,256,512\} and we report peak throughput. Training measurements use DDP across 7 GPUs in BF16 at per-GPU batch sizes 64 and 128. Table 3 : Parameter and compute efficiency. GKA removes W q , W k , W v W_{q},W_{k},W_{v} and replaces them with H H learnable σ h \sigma_{h} scalars per…

评价证据摘要：We integrate GKA into DeiT-style ViTs and evaluate on ImageNet classification. Across model scales, GKA substantially reduces attention parameters and total training FLOPs while maintaining competitive top-1 accuracy. Training remains stable, and learned bandwidths specialize across heads, revealing interpretable locality patterns. These results indicate that learned query–key geometry is not strictly required for effective global patch interaction and define a distinct accuracy–efficiency trade-off frontier.

限制证据摘要：These results highlight a gap between parametric efficiency and wall-clock efficiency: removing three projection GEMMs trades tensor-core-friendly matrix multiplications for bandwidth-dominated distance, exponentiation or normalization. A promising direction is fused Gaussian attention kernels (CUDA/Triton) that tile distance computation, exponentiation, masking, and normalization in a single IO-aware pass, analogou…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `MODEL-SELF-ATTENTION` / [Ch14](../../../../books/part-02-model/14-self-attention.md)；现有覆盖差异：现有正文仍缺：用原始 hidden-state 间 Gaussian kernel 直接构造 row-stochastic attention，移除 Q/K 投影并以 bandwidth 控制局部性。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。最终处置已通过独立复核。

### [SpecEdit: Training-Free Acceleration for Diffusion based Image Editing via Semantic Locking](https://arxiv.org/html/2605.02152v1)

准入时需核验的设计变化是：先低分辨率生成 draft，以语义验证锁定稳定区域，仅对未锁定区域恢复高分辨率并继续计算。exact-v1 的机制定位为 `3 Method；3.3 Spatial Draft-and-Verify Mechanism；Compatibility with complementary acceleration methods.`，评价定位为 `4 Experiment；4.1 Experiment Settings；4.2 Results on Qwen-Image-Edit`，限制或反证定位为 `6 Conclusion`。

机制证据摘要：Table 4 and Table 3 evaluate the compatibility of SpecEdit with feature caching (FoCa). On ImgEdit-Bench , combining SpecEdit with FoCa achieves 6.00 × \times latency speedup (47.45s) while maintaining competitive overall performance (3.75 vs. 3.88). On GEdit-Bench , SpecEdit+FoCa further delivers 6.00 × \times latency and 6.34 × \times FLOPs reduction while sustaining strong semantic consistency and perceptual quality (OS 7.56/7.57 on CN/EN), close to the full-step baseline. Table 5 : Quantitative results of imag…

评价证据摘要：Implementation Details. We evaluate SpecEdit on two representative diffusion-based editing models, Qwen-Image-Edit and FLUX.1-Kontext-dev . All experiments are conducted on NVIDIA A100 GPUs. We compare against diverse acceleration baselines spanning step reduction, attention sparsification [ 10 ] , spatial resolution scheduling (e.g., RALU [ 7 ] , Bottleneck Sampling [ 29 ] and Fresco [ 8 ] ), feature caching and forecasting methods (e.g., ToCa [ 30 ] , FORA [ 31 ] , DuCa [ 32 ] , Freqca [ 21 ] , TaylorSeer [ 5 ]…

限制证据摘要：We presented SpecEdit , a training-free dynamic-resolution framework tailored to diffusion-based image editing. SpecEdit follows a draft-and-verify paradigm: a low-resolution draft first approximates the semantic evolution of the edit, and token-level perceptual discrepancies are then used to identify tokens that warrant high-resolution Transformer computation, with a sparse uniform coverage set introduced to stabil…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；现有覆盖差异：现有正文仍缺：先低分辨率生成 draft，以语义验证锁定稳定区域，仅对未锁定区域恢复高分辨率并继续计算。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。最终处置已通过独立复核。

### [AAFLOW: Scalable Patterns for Agentic AI Workflows](https://arxiv.org/html/2605.02162v1)

准入时需核验的设计变化是：零拷贝数据流与可组合执行模式把 Agent workflow 从脚本升级为显式 runtime。exact-v1 的机制定位为 `II Architectural Design；II-B Compilation to Distributed Execution；II-D Resource-Deterministic Execution Model`，评价定位为 `I-A Scope of Evaluation；III Implementation`，限制或反证定位为 `VI Discussion and Future Experiments；VII Conclusion`。

采用边界：机制锚点为 II Architectural Design, II-B Compilation to Distributed Execution, II-D Resource-Deterministic Execution Model；评价锚点为 I-A Scope of Evaluation, III Implementation。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md)；现有命题：已知顺序与 invariant 应由 durable workflow 拥有，模型只处理开放决策；比较：现有命题已经规定：已知顺序与 invariant 应由 durable workflow 拥有，模型只处理开放决策。本来源的受限增量是“零拷贝数据流与可组合执行模式把 Agent workflow 从脚本升级为显式 runtime”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Planner Matters! An Efficient and Unbalanced Multi-agent Collaboration Framework for Long-horizon Planning](https://arxiv.org/html/2605.02168v1)

准入时需核验的设计变化是：Planner, actor and memory roles may own different compute budgets; the reported allocation is evidence for the tested planning workloads, not a universal multi-agent topology.。exact-v1 的机制定位为 `Framework: planner, actor and memory-manager decomposition；asymmetric model allocation`，评价定位为 `Experiments on long-horizon planning tasks；role/model ablations`，限制或反证定位为 `Limitations and role-decomposition scope`。

机制证据摘要：§Framework: planner, actor and memory-manager decomposition; asymmetric model allocation；Language model (LM)-based agents have demonstrated promising capabilities in automating complex tasks from natural language instructions, yet they continue to struggle with long-horizon planning and reasoning. To address this, we propose an enhanced multi-agent framework that decomposes automation into three roles: a planner for high-level decision-making, an actor for task execution, and a memory manager for contextual reason…

评价证据摘要：§Experiments on long-horizon planning tasks; role/model ablations；Language model (LM)-based agents have demonstrated promising capabilities in automating complex tasks from natural language instructions, yet they continue to struggle with long-horizon planning and reasoning. To address this, we propose an enhanced multi-agent framework that decomposes automation into three roles: a planner for high-level decision-making, an actor for task execution, and a memory manager for contextual reasoning. While this modular…

限制证据摘要：§Limitations and role-decomposition scope

采用边界：Planner, actor and memory roles may own different compute budgets; the reported allocation is evidence for the tested planning workloads, not a universal multi-agent topology. 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `AGENT-MULTI-AGENT` / [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；现有命题：消息、角色和局部成功不能替代共享状态的唯一提交语义；比较：现有命题已经规定：消息、角色和局部成功不能替代共享状态的唯一提交语义。本来源的受限增量是“Planner, actor and memory roles may own different compute budgets; the reported allocation is evidence for the tested planning workloads, not a universal multi-agent topology.”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [T$^2$PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/html/2605.02178v1)

准入时需核验的设计变化是：在 token 与 turn 两层跟踪 uncertainty progress，停滞时分别触发 thinking intervention 和 turn resampling，改变多轮 Agent RL 的 rollout admission。。exact-v1 的机制定位为 `token-level uncertainty dynamics；turn-level exploration progress；intervention and resampling thresholds`，评价定位为 `WebShop；ALFWorld；Search QA；stability and exploration-efficiency ablations`，限制或反证定位为 `off-policy pipeline staleness；fixed threshold/configuration；environment-specific uncertainty calibration`。

机制证据摘要：token controller 计算边际 uncertainty change，低于阈值时插入 thinking intervention；turn controller 判断一轮交互是否几乎没有探索进展并动态重采样。两者在优化前改变实际进入训练的 trajectory 分布。

评价证据摘要：作者在 WebShop、ALFWorld 和 Search QA 上报告训练稳定性、性能与探索效率改善，并比较 token/turn 组件；结果绑定所用 policy、uncertainty estimator、环境和阈值。

限制证据摘要：论文讨论 pipeline/off-policy staleness 与固定设置；uncertainty 不等于错误，低变化也可能表示已经收敛或需要长期延迟收益，错误干预会改写 on-policy 分布。

采用边界：来源支持把 exploration progress 作为 rollout control signal；不证明 uncertainty 是 outcome verifier，也不允许 intervention/resampling 的数据在缺少 policy/version identity 时混入更新。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent post-write review complete`，目标 owner 为 `TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md)；现有覆盖差异：现有覆盖与 exact-v1 对读后仍缺：把低边际信息检测扩展成两层 exploration controller：token 层只能提出 bounded thinking intervention，turn 层只能提出 resample/cancel；group builder 保存触发分数、阈值、policy/environment revision 与最终 membership，optimizer 不把缺失 suffix 或重采样重复当独立证据。它用减少空转换取 estimator drift、selection bias、额外 token 和 on-policy staleness；uncertainty 不等于错误，late-reward 或校准不足时回退完整 rollout/静态采样。exact-v1 只支持 WebShop、ALFWorld、Search QA 与作者配置。最终处置已通过独立复核。

### [Risk-Budgeted Online Scheduling for Continuous Edge Inference over Evolving Time Horizons](https://arxiv.org/html/2605.02179v1)

准入时需核验的设计变化是：Continuous edge inference must carry deadline-violation risk and burst history across time; the AEGIS policy is bounded to its prediction and risk-budget assumptions.。exact-v1 的机制定位为 `§II-C State Prediction and Risk Construction；§II-D Dynamic Risk Budget；§III-A–C potential-aligned game and asynchronous feasible improvement`，评价定位为 `§IV-A Experimental Setup, Benchmarks, and Metrics；§IV-B Performance Evaluation and AEGISNoBudget ablation`，限制或反证定位为 `§V Conclusion: extension to multi-platform and richer network dynamics remains future work；simulation rather than production deployment`。

机制证据摘要：The remaining per-user risk budget is updated across timeslots by risk consumption and recovery. LSTM channel/load predictions construct a risk surrogate; each timeslot is solved as a coupled-feasibility potential game, with one feasible unilateral update committed at a time before the next risk state is written.

评价证据摘要：§IV evaluates a 180-timeslot simulated edge environment on Python 3.10/i9-12900H, with fixed bandwidth/compute capacity and Chicago taxi traces used only to calibrate user activity. Metrics include timely-inference ratio, delay, violation risk, burst length and convergence; AEGISNoBudget isolates the dynamic budget contribution.

限制证据摘要：Evidence is simulation-bound and depends on the LSTM risk surrogate, modeled task/resource ranges and potential-game feasibility. §V leaves multi-platform deployment and richer/adaptive network risk control to future work; no production SLO trial is demonstrated.

采用边界：Continuous edge inference must carry deadline-violation risk and burst history across time; the AEGIS policy is bounded to its prediction and risk-budget assumptions. 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `INFER-SCHEDULING` / [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；最终处置已通过独立复核。

### [When Alignment Isn’t Enough: Response-Path Attacks on LLM Agents](https://arxiv.org/html/2605.02187v1)

准入时需核验的设计变化是：BYOK response relay 可静默篡改，provider-signed envelope 才能绑定响应 provenance。exact-v1 的机制定位为 `4 Formal Model；6 Methodology: Relay Tampering Attack`，评价定位为 `7 Evaluation；7.1 Experimental Setup；7.3 RQ2: Ablation Study of RTA`，限制或反证定位为 `9 Limitations and Future Work；11 Conclusion`。

机制证据摘要：We formalize the vulnerability as a game-based security problem for relay-mediated LLM agents. Figure 2 shows the system as a tuple ℳ = ( U , R , S , T ) \mathcal{M}=(U,R,S,T) : U U is the frontend agent, R R is the intermediate relay, S S is the backend LLM (with its internal safety alignment), and T T is the tool substrate. All traffic between U U and S S traverses R R , making R R the sole intermediary on the agent–LLM path. An LLM response factors as r = ( x , c ) r=(x,c) : x x is ordinary text and c c contain…

评价证据摘要：In this section, we present our empirical evaluation of the proposed attack by addressing the following research questions (RQs): • RQ1 (Effectiveness): How effectively can RTA hijack downstream agent actions compared with representative prompt injection attacks? • RQ2 (Ablation): How do the individual design pillars of RTA contribute to its overall effectiveness? • RQ3 (Imperceptibility): How well can RTA preserve the semantic and stylistic fidelity of the original response to remain imperceptible? • RQ4 (Overhea…

限制证据摘要：This work intentionally focuses on a single, well-defined attack surface: the response-path integrity gap in BYOK relay deployments. A foundational assumption is that the relay observes all application-layer messages in cleartext, which holds by construction in the BYOK setting where the relay legitimately terminates TLS on both legs of the connection. For benchmarks, we select AgentDojo [ 16 ] and Agent Security Be…

采用边界：机制锚点为 4 Formal Model, 6 Methodology: Relay Tampering Attack；评价锚点为 7 Evaluation, 7.1 Experimental Setup, 7.3 RQ2: Ablation Study of RTA。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；最终处置已通过独立复核。

### [PipeMax: Enhancing Offline LLM Inference on Commodity GPU Servers](https://arxiv.org/html/2605.02189v1)

准入时需核验的设计变化是：commodity GPU 离线推理通过阶段 pipeline 重排内存与计算，而非照搬在线 serving。exact-v1 的机制定位为 `2.2.1 Offloading Approach；2.2.2 Model Parallelism Approach`，评价定位为 `4 Evaluation`，限制或反证定位为 `6 Conclusion`。

采用边界：机制锚点为 2.2.1 Offloading Approach, 2.2.2 Model Parallelism Approach；评价锚点为 4 Evaluation。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `INFER-SCHEDULING` / [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；现有命题：调度状态必须携带 deadline risk、剩余 slack 与降级边界；比较：现有命题已经规定：调度状态必须携带 deadline risk、剩余 slack 与降级边界。本来源的受限增量是“commodity GPU 离线推理通过阶段 pipeline 重排内存与计算，而非照搬在线 serving”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Beyond Translation Accuracy: Addressing False Failures in LLM-Based Code Translation](https://arxiv.org/html/2605.02195v1)

准入时需核验的设计变化是：Compiler flags, libraries, runtime configuration and test harness are part of code-agent evaluation identity because pipeline faults can create false model failures.。exact-v1 的机制定位为 `3 Methodology；3.1 Inspection Process；3.2 Classification Criteria`，评价定位为 `4 Experimental Setup；5 Findings`，限制或反证定位为 `6 Threats to Validity`。

机制证据摘要：§3 Methodology; §3.1 Inspection Process; §3.2 Classification Criteria；Large Language Models (LLMs) have achieved remarkable success in automated code translation. While prior work has focused on improving translation accuracy through advanced prompting and iterative repair, the reliability of the underlying evaluation frameworks has received less attention. In this paper, we demonstrate that a significant number of reported failures in code translation are not due to incorrect logic, but rather evaluation-induced…

评价证据摘要：§4 Experimental Setup; §5 Findings；Large Language Models (LLMs) have achieved remarkable success in automated code translation. While prior work has focused on improving translation accuracy through advanced prompting and iterative repair, the reliability of the underlying evaluation frameworks has received less attention. In this paper, we demonstrate that a significant number of reported failures in code translation are not due to incorrect logic, but rather evaluation-induced errors stemming from improper compi…

限制证据摘要：§6 Threats to Validity

采用边界：Compiler flags, libraries, runtime configuration and test harness are part of code-agent evaluation identity because pipeline faults can create false model failures. 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“Compiler flags, libraries, runtime configuration and test harness are part of code-agent evaluation identity because pipeline faults can create false model failures.”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [DurableUn: Quantization-Induced Recovery Attacks in Machine Unlearning](https://arxiv.org/pdf/2605.02196v1)

准入时需核验的设计变化是：最终部署量化可能抹平幅度较小的 unlearning update，使全精度通过的遗忘结论在实际 artifact 上逆转；遗忘证据必须绑定 precision、quantizer、merge 顺序、kernel 与 retained utility。exact-v1 的机制定位为 `§3 Setup；§4 INT4 recovery；§5 FA–RA–Q-INT4 trilemma；§6 DURABLEUN-SAF；§7 durability certificate；Appendix C/D`，评价定位为 `§3–§5；§7；§9；Appendix D`，限制定位为 `§8；§10；reproducibility checklist §2`。

机制证据摘要：在 NF4 base + LoRA adapter 的设定中，作者把部署量化建模为 adapter-space per-row symmetric INT4 rounding，并用 STE 将量化后的 forget loss 纳入 sharpness-aware forgetting objective。durability certificate 是同一模型在 BF16、INT8、INT4 三个已测精度上的最坏 forget score，而不是对任意部署栈的删除证明。

评价证据摘要：主实验为 LLaMA-3-8B-Instruct、TOFU forget10/retain90、LoRA rank 16 / alpha 32、单张 RTX 4090，并比较七种 unlearning 方法、三种 seed、alpha sweep 与 MIA-AUC；§9 在 MUSE-News、WikiBio-WPU 复测，Appendix D 以真实 PTQ 检查模拟量化方向。

限制证据摘要：作者方案取得量化鲁棒性时 retained accuracy 约为 0.045，论文将其定位为可达性的存在性证据而非 production-ready solution。主要机制限于 NF4+LoRA adapter-space INT4；merged-model/PTQ 只是附加验证，不能外推到未知 quantizer、attack、GDPR compliance 或不可恢复删除。

采用边界：只采用 exact-v1 披露的模型、数据集、量化设置、方法、seed 与 evaluator。作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有 `Deployed Precision 是 Forgetting Evidence 的组成部分` 已绑定 base checkpoint、delta/adapter、merge、quantizer、bit width、calibration、kernel、serving artifact 与 retained utility，并保留未知量化器和停止发布/重训回退，故不重复写入。

### [MEMAUDIT: An Exact Package-Oracle Evaluation Protocol for Budgeted Long-Term LLM Memory Writing](https://arxiv.org/html/2605.02199v1)

准入时需核验的设计变化是：Long-term memory writing needs an exact budgeted package oracle that measures write admission separately from answer generation.。exact-v1 的机制定位为 `arXiv:2605.02199v1 HTML, Method/Design section；abstract mechanism: We introduce MEMAUDIT, an exact packageoracle evaluation protocol for budgeted long-term memory writing.`，评价定位为 `arXiv:2605.02199v1 HTML, Experiments/Evaluation and ablation sections；abstract scope: We introduce MEMAUDIT, an exact packageoracle evaluation protocol for budgeted long-term memory writing.`，限制或反证定位为 `arXiv:2605.02199v1 HTML, Discussion/Limitations and threat-to-validity passages；no cross-workload generalization inferred`。

机制证据摘要：arXiv:2605.02199v1 HTML, Method/Design section; abstract mechanism: We introduce MEMAUDIT, an exact packageoracle evaluation protocol for budgeted long-term memory writing.；Long-term LLM agents must compress streams of past interactions into persistent memory before future queries are known. Existing evaluations usually measure final question-answering accuracy, which entangles memory writing with retrieval, prompting, and reader reasoning. We introduce MEMAUDIT, an exact packageoracle evaluation protocol for budg…

评价证据摘要：arXiv:2605.02199v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: We introduce MEMAUDIT, an exact packageoracle evaluation protocol for budgeted long-term memory writing.；Long-term LLM agents must compress streams of past interactions into persistent memory before future queries are known. Existing evaluations usually measure final question-answering accuracy, which entangles memory writing with retrieval, prompting, and reader reasoning. We introduce MEMAUDIT, an exact packageoracle evaluatio…

限制证据摘要：arXiv:2605.02199v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred

采用边界：Long-term memory writing needs an exact budgeted package oracle that measures write admission separately from answer generation. 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)；现有命题：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner；比较：现有命题已经规定：memory 的 admission、事实状态、派生视图、读取与恢复必须分 owner。本来源的受限增量是“Long-term memory writing needs an exact budgeted package oracle that measures write admission separately from answer generation.”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Metric Unreliability in Multimodal Machine Unlearning: A Systematic Analysis and Principled Unified Score](https://arxiv.org/pdf/2605.02206v1)

准入时需核验的设计变化是：多模态 unlearning 的输出遗忘、保留效用、membership leakage、表示距离与 knowledge recoverability 可能给出相反排序，不能由单一 composite score 互相替代。exact-v1 的机制定位为 `§3；§4.1–§4.2；§5.1/§5.3；§6`，评价定位为 `§3；§5.1–§5.3；§6；Appendix C`，限制定位为 `§3 oracle limitations；§4.2；§6–§7；reproducibility checklist §2`。

机制证据摘要：FA/RA/MIA 是输出或攻击观测，activation distance/JS 是相对 retain-only retrained oracle 的表示观测，针对改写与间接查询的 probes 单列 Knowledge Recoverability。UQS 用各指标对 oracle distance 的 Spearman correlation 估计并归一化权重；该权重属于 model/dataset-specific calibration，不是跨模型常数。

评价证据摘要：作者覆盖 36 个 LLaVA-1.5-7B LoRA unlearned models、三个 benchmark、四种方法、三次 seed 和单张 RTX 4090，以 Kendall tau 比较五个指标排序，并用 100 组 Dirichlet 权重扰动检查 UQS；BLIP-2 OPT-2.7B 仅局部复现，不能支持跨架构稳定性。

限制证据摘要：retain-only oracle 仅一轮 fine-tuning、retain data 可能包含 forget correlates，且 oracle 并非唯一真值；KR 因 probe 成本没有进入 UQS。一个总分仍可能遮蔽 privacy、utility、representation 与 recoverability 的不同 failure type，不能作为通用删除证书或 GDPR 合规证明。

采用边界：指标负相关不证明任一指标普遍错误；结论只适用于作者披露的模型、benchmark、unlearning methods、oracle construction 和 metric implementation。作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，canonical owner 修正为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；该章已规定多轴 evidence、oracle 非唯一性、逐轴 release verdict 及聚合指标不得隐藏 failure type，故不追加正文。

### [Submodular Benchmark Selection](https://arxiv.org/html/2605.02209v1)

准入时需核验的设计变化是：Benchmark subset admission must state the covariance/information model, budget and residual-coverage diagnostic; the selected subset cannot inherit full-suite authority outside those assumptions.。exact-v1 的机制定位为 `3 Problem Formulation；4 Algorithms and Approximation Guarantees`，评价定位为 `5 Experiments；Appendix F Selection Order and Stability`，限制或反证定位为 `6 Discussion: cost, safety/fairness coverage and alternatives`。

机制证据摘要：§3 Problem Formulation; §4 Algorithms and Approximation Guarantees；Evaluating large language models across many benchmarks is expensive, yet many benchmarks are highly correlated. We formalize the selection of a small, informative subset as submodular maximization under a multivariate Gaussian model. Entropy (log-determinant covariance) and mutual information between selected and remaining benchmarks arise as natural objectives. Both are submodular; entropy selection coincides with pivoted Cholesky and has spectra…

评价证据摘要：§5 Experiments; Appendix F Selection Order and Stability；Evaluating large language models across many benchmarks is expensive, yet many benchmarks are highly correlated. We formalize the selection of a small, informative subset as submodular maximization under a multivariate Gaussian model. Entropy (log-determinant covariance) and mutual information between selected and remaining benchmarks arise as natural objectives. Both are submodular; entropy selection coincides with pivoted Cholesky and has spectral residual…

限制证据摘要：§6 Discussion: cost, safety/fairness coverage and alternatives

采用边界：Benchmark subset admission must state the covariance/information model, budget and residual-coverage diagnostic; the selected subset cannot inherit full-suite authority outside those assumptions. 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“Benchmark subset admission must state the covariance/information model, budget and residual-coverage diagnostic; the selected subset cannot inherit full-suite authority outside those assumptions.”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No C…。最终处置已通过独立复核。

### [CoVSpec: Efficient Device-Edge Co-Inference for Vision-Language Models via Speculative Decoding](https://arxiv.org/html/2605.02218v1)

准入时需核验的设计变化是：device-edge VLM speculation 联合视觉 token pruning、adaptive draft 与通信 correction。exact-v1 的机制定位为 `CoVSpec: Efficient Device–Edge Co-Inference for Vision-Language Models via Speculative Decoding Thanks: This work is partly supported by the National Key R&D Program of China under Grant 2024YFE0200802, by the NSFC under grant No. 62293481 and No. 62571487, and by the Zhejiang Provincial Natural Science Foundation of China under Grant No. LZ25F010001. (Corr…`，评价定位为 `III-C Parallel Branching with Decoupled Verification-Correction；III-C2 Decoupled Verification-Correction`，限制或反证定位为 `V Conclusion`。

采用边界：机制锚点为 CoVSpec: Efficient Device–Edge Co-Inference for Vision-Language Models via Speculative Decoding Thanks: This work is partly supported by the National Key R&D Program of China under Grant 2024YFE0200802, by the NSFC under grant No. 62293481 and No. 62571487, and by the Zhejiang Provincial Natural Science Foundation of China under Grant No. LZ25F010001. (Corresponding author: Q. Yang.) Thanks: 3Equal contribution., II System Model, II-B Transmission Model；评价锚点为 III-C Parallel Branching with Decoupled Verification-Correction, III-C2 Decoupled Verification-Correction。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `INFER-SPECULATIVE-DECODING` / [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)；现有命题：proposal 可以近似，最终 commit 必须保持 target distribution 与唯一提交边界；比较：现有命题已经规定：proposal 可以近似，最终 commit 必须保持 target distribution 与唯一提交边界。本来源的受限增量是“device-edge VLM speculation 联合视觉 token pruning、adaptive draft 与通信 correction”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Perturbation Dose Responses in Recursive LLM Loops: Raw Switching, Stochastic Floors, and Persistent Escape under Append, Replace, and Dialog Updates](https://arxiv.org/html/2605.02236v1)

准入时需核验的设计变化是：递归 LLM loop 的持久逃逸由 append/replace/dialog memory policy 决定。exact-v1 的机制定位为 `Perturbation Dose Responses in Recursive LLM Loops Raw switching, stochastic floors, and persistent escape under append, replace, and dialog updates；2.1 Attractors in neural dynamics；2.2 Attractor observations in language models`，评价定位为 `Algorithm 1: paired perturbation evaluation；5 Results；5.2.1 F3 cross-loop insert validation: insert is regime-conditional`，限制或反证定位为 `6 Discussion；7 Limitations`。

采用边界：机制锚点为 Perturbation Dose Responses in Recursive LLM Loops Raw switching, stochastic floors, and persistent escape under append, replace, and dialog updates, 2.1 Attractors in neural dynamics, 2.2 Attractor observations in language models；评价锚点为 Algorithm 1: paired perturbation evaluation, 5 Results, 5.2.1 F3 cross-loop insert validation: insert is regime-conditional。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md)；现有命题：已知顺序与 invariant 应由 durable workflow 拥有，模型只处理开放决策；比较：现有命题已经规定：已知顺序与 invariant 应由 durable workflow 拥有，模型只处理开放决策。本来源的受限增量是“递归 LLM loop 的持久逃逸由 append/replace/dialog memory policy 决定”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Zero-Shot Confidence Estimation for Small LLMs: When Supervised Baselines Aren't Worth Training](https://arxiv.org/html/2605.02241v1)

准入时需核验的设计变化是：生成 log-probability 可作为小模型到云模型升级路由的零样本置信信号。exact-v1 的机制定位为 `III-A Models；III-B Datasets；III-D Evaluation Protocol`，评价定位为 `III-D Evaluation Protocol`，限制或反证定位为 `VIII Limitations；IX Conclusion`。

采用边界：机制锚点为 III-A Models, III-B Datasets, III-D Evaluation Protocol；评价锚点为 III-D Evaluation Protocol。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“生成 log-probability 可作为小模型到云模型升级路由的零样本置信信号”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [On the Privacy of LLMs: An Ablation Study](https://arxiv.org/html/2605.02255v1)

准入时需核验的设计变化是：统一威胁模型揭示 MIA、提取、属性推断与 backdoor 对模型/RAG 配置的依赖不同。exact-v1 的机制定位为 `Access Model.；3.1.1 Mechanism；3.1.4 Experimental Results and Analysis`，评价定位为 `On the Privacy of LLMs: An Ablation Study；Evaluation Perspective.；3.1.4 Experimental Results and Analysis`，限制或反证定位为 `5.1 Threat Model and Attack Mechanism；6.3 Threat Model；8 Conclusion`。

采用边界：机制锚点为 Access Model., 3.1.1 Mechanism, 3.1.4 Experimental Results and Analysis；评价锚点为 On the Privacy of LLMs: An Ablation Study, Evaluation Perspective., 3.1.4 Experimental Results and Analysis。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `AGENT-RAG` / [Ch76](../../../../books/part-07-agent/76-rag.md)；现有命题：检索相关性、证据充分性、freshness 与 provenance 是不同 gate；比较：现有命题已经规定：检索相关性、证据充分性、freshness 与 provenance 是不同 gate。本来源的受限增量是“统一威胁模型揭示 MIA、提取、属性推断与 backdoor 对模型/RAG 配置的依赖不同”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [WindowQuant: Mixed-Precision KV Cache Quantization based on Window-Level Similarity for VLMs Inference Optimization](https://arxiv.org/html/2605.02262v1)

准入时需核验的设计变化是：按视觉 token window 与文本 prompt 的相似度分配 KV bit-width，并通过 window 重排把搜索 artifact 编译为可执行 mixed-precision layout/kernel。。exact-v1 的机制定位为 `window-level quantization search；prompt-window similarity；window reordering and mixed-precision KV computation`，评价定位为 `LLaVA-OneVision-Qwen2-7B；EgoSchema and video-language datasets；memory/latency/quality comparison`，限制或反证定位为 `model/dataset/kernel-specific search；prompt-similarity proxy；quantization remains approximate`。

机制证据摘要：WindowQuant 先在 window 粒度根据视觉窗口与 prompt 相似度搜索 bit-width，再重排同精度 window 以减少 irregular mixed-precision kernel 开销；重排保持 attention 行列对应，量化本身仍是近似。

评价证据摘要：作者在披露 VLM、视频数据、batch 和 GPU 设置下报告平均约 3.17 bits 及 latency/memory 结果，并与 token-granularity 与统一量化比较；性能数字依赖窗口、layout、kernel 和 prompt 分布。

限制证据摘要：prompt 相似度不是未来 decode query 的充分统计，窗口会混合关键与冗余 token；搜索、重排和 kernel 只在披露模型/硬件验证，未证明跨 prompt、长会话或在线漂移。

采用边界：证据支持把 window-level bit allocation 与物理 layout 联合选择；不证明相似度是通用 KV 重要性，也不把作者平均 bit/latency 作为生产常数。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；现有命题：多模态 KV 选择必须说明决策时可见的 prompt/prefill 信号、未来 query 风险、量化误差坐标与 fallback；比较：现有小节已把 prompt-conditioned prefill signal 与未来 decode demand 分开，并要求压缩/漂移可检验；WindowQuant 是 window bit-width 与 layout 的具体实现，没有改变其信息边界和回退。最终处置已通过独立复核。

### [Break the Block: Dynamic-size Reasoning Blocks for Diffusion Large Language Models via Monotonic Entropy Descent with Reinforcement Learning](https://arxiv.org/html/2605.02263v1)

准入时需核验的设计变化是：用专用 block-end token、block entropy trajectory 与 RL reward 学习动态 reasoning block boundary，替代 diffusion LM 的固定 block size。。exact-v1 的机制定位为 `dynamic block-end token；monotonic entropy descent reward；GRPO post-training`，评价定位为 `reasoning benchmarks；fixed-size block baselines；block-size and reward ablations`，限制或反证定位为 `entropy descent is a proxy；fixed benchmark/max-length scope；no universal coherence proof`。

机制证据摘要：b1 把 block boundary 变成生成状态：模型可在推理中输出 block-end token，训练用 entropy 从前一 block 到后一 block 的单调下降作为辅助 reward，并结合任务 reward 通过 GRPO 学习不同任务/步骤的 block size。

评价证据摘要：作者在数学/推理 benchmark 和固定最大长度下比较多种固定 block baseline，并做 dynamic token 与 entropy reward 消融；训练硬件和结果只约束该 dLLM 与任务组合。

限制证据摘要：边际 entropy 下降并不等于推理正确或语义步骤结束，错误但自信的 block 也可能满足 reward；论文未证明不同 dLLM、开放生成或部署并发下的阈值和收益。

采用边界：来源支持把 block boundary 从固定超参数演进为 policy-owned generation state；不证明 entropy trajectory 是 correctness verifier，也不保证动态 block 在所有 workload 更快。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent post-write review complete`，目标 owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；现有覆盖差异：现有覆盖与 exact-v1 对读后仍缺：在 fixed block 旁增加 learned-boundary 分支：decoder 输出可验证的 block-end proposal，runtime 冻结 boundary/policy revision 后提交；训练可用 entropy trajectory 提供辅助 shaping，但任务 outcome/独立 verifier 仍拥有正确性。动态边界以语义步骤适配换 variable-length scheduling、cache/rollback 复杂度、reward hacking 和错误自信；短输出、静态 shape kernel 或 entropy 未校准时继续使用固定 block。exact-v1 的 reasoning benchmark 只支持该代理信号和后训练机制在作者设置中的结果。最终处置已通过独立复核。

### [Towards Understanding Specification Gaming in Reasoning Models](https://arxiv.org/html/2605.02269v1)

准入时需核验的设计变化是：用可观察环境中的隐藏 hacking opportunity 分离任务成功与 specification gaming，并测量 RL 后行为变化。exact-v1 的机制定位为 `3 Design of evaluations；3.3 Email assistant environment；4.3 Increasing reasoning effort weakly increases the rate of specification gaming`，评价定位为 `3 Design of evaluations；Setup.；4 Results`，限制或反证定位为 `3.7 Design Trade-offs；5 Conclusion；Limitations.`。

机制证据摘要：We develop evaluations to test specification gaming propensities. We define an action that has gamed the specification (or ‘hacked’) as one that (1) is unintended by a model’s developers or users, and (2) scores highly as per an evaluation function. We aim for a diverse suite covering a variety of specification gaming behaviors. This includes a mix of coding and non-coding tasks, single- and multi-turn environments, and environments with tool use. We hope this diversity ensures our suite measures broad hacking pro…

评价证据摘要：We develop evaluations to test specification gaming propensities. We define an action that has gamed the specification (or ‘hacked’) as one that (1) is unintended by a model’s developers or users, and (2) scores highly as per an evaluation function. We aim for a diverse suite covering a variety of specification gaming behaviors. This includes a mix of coding and non-coding tasks, single- and multi-turn environments, and environments with tool use. We hope this diversity ensures our suite measures broad hacking pro…

限制证据摘要：While we aim for realism in our environments, motivated by recent concerns around evaluation-awareness ( Needham et al., 2025 ; Anthropic, 2025c ) , we also find value in environments that are less realistic but especially easy to run (e.g., the MC environments). We further find value in designing environments where executing the exploit does not require strong capabilities, meaning we can obtain signal on propensit…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有覆盖差异：现有正文仍缺：用可观察环境中的隐藏 hacking opportunity 分离任务成功与 specification gaming，并测量 RL 后行为变化。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。最终处置已通过独立复核。

### [SOTOPIA-TOM: Evaluating Information Management in Multi-Agent Interaction with Theory of Mind](https://arxiv.org/html/2605.02307v1)

准入时需核验的设计变化是：多 Agent 的 public/private channel、partitioned knowledge 与 disclosure policy 必须进入共享状态和评测身份；终局成功不能掩盖隐私泄漏或缺失信息请求。。exact-v1 的机制定位为 `§Environment with public/private channels；§160 human-reviewed multi-party scenarios；§INFOMGMT dimensions`，评价定位为 `six backbones and prompting interventions；information seeking, useful sharing, coordination and privacy metrics`，限制或反证定位为 `synthetic scenarios, composite metric and judge-policy scope`。

机制证据摘要：As LLM-based agents are increasingly interacting in multi-party settings, they need to properly handle information asymmetry, i.e., knowing when and to whom to disclose information is appropriate. Yet, existing benchmarks fail to measure this ability in realistic multi-party settings. Thus, we introduce SOTOPIA-TOM, a multi-dimensional benchmarking framework to evaluate LLM agents' ability to successfully navigate information asymmetric and privacy sensitive multi-party interactions. We create an interaction envir…

评价证据摘要：As LLM-based agents are increasingly interacting in multi-party settings, they need to properly handle information asymmetry, i.e., knowing when and to whom to disclose information is appropriate. Yet, existing benchmarks fail to measure this ability in realistic multi-party settings. Thus, we introduce SOTOPIA-TOM, a multi-dimensional benchmarking framework to evaluate LLM agents' ability to successfully navigate information asymmetric and privacy sensitive multi-party interactions. We create an interaction envir…

限制证据摘要：只支持 exact-v1 披露的任务、模型、环境和 evaluator；未披露的跨域、生产与长期稳定性不得外推。

采用边界：多 Agent 的 public/private channel、partitioned knowledge 与 disclosure policy 必须进入共享状态和评测身份；终局成功不能掩盖隐私泄漏或缺失信息请求。 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `AGENT-MULTI-AGENT` / [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；现有命题：消息、角色和局部成功不能替代共享状态的唯一提交语义；比较：现有命题已经规定：消息、角色和局部成功不能替代共享状态的唯一提交语义。本来源的受限增量是“多 Agent 的 public/private channel、partitioned knowledge 与 disclosure policy 必须进入共享状态和评测身份；终局成功不能掩盖隐私泄漏或缺失信息请求。”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [When Attention Collapses: Residual Evidence Modeling for Compositional Inference](https://arxiv.org/html/2605.02323v1)

准入时需核验的设计变化是：用逐 slot residual-evidence state 记录尚未解释的输入容量，抑制 additive mixture 中的重复 attention allocation。exact-v1 的机制定位为 `§2.2 Attention Collapse under Additive Superposition；§2.3 Residual Evidence Modeling`，评价定位为 `§3 Experiments；FUSS audio separation；LISA signal decomposition；Ablations`，限制或反证定位为 `§4 Discussion；Single-granularity and depletion-function limitations`。

机制证据摘要：并行或仅顺序化的 attention slots 在 additive superposition 中会受共享梯度驱动而 collapse。方法为每个 token 保存 unexplained evidence e_l；每个 slot 读取当前 residual，通过 log-e bias 与 K/V scaling 调整 attention，并在 slot 输出后执行 multiplicative depletion，让下一 slot 消费更新后的残余状态。

评价证据摘要：作者在 synthetic mixtures、4 秒 FUSS audio（32 ChunkFFT、5 slots）与 LISA decomposition 上报告 slot collapse/分离改善；quadratic depletion 与 loss-only regularization 在作者设置中不足。

限制证据摘要：residual state 是模型内部的解释预算，不是事实证据。顺序更新引入 ordering sensitivity、误差累积和额外控制依赖；单一 granularity、depletion 形式与超参是 task-dependent，跨文本/通用 MLLM 的类比未被实验直接证明。

采用边界：exact-v1 仅支持 synthetic、FUSS audio 与 LISA workload；不证明该机制适用于通用 LLM attention，也不允许把 learned evidence depletion 当作 factual provenance 或 correctness signal。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent post-write review complete`，目标 owner 为 `MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；现有覆盖差异：现有命题仍把多 slot attention 看作一次或彼此独立的预算分配；没有表示“哪些输入成分已被前一 slot 解释”的可变状态，因此未覆盖 additive superposition 下重复选择同一成分的 failure mode。最终处置已通过独立复核。

### [Taming Request Imbalance: SLO-Aware Scheduling for Disaggregated LLM Inference](https://arxiv.org/html/2605.02329v1)

准入时需核验的设计变化是：PD 两侧分别用 TTFT urgency 与 TPOT slack 控制长尾请求和 decode packing。exact-v1 的机制定位为 `2.1 LLM Serving System；3 Design`，评价定位为 `4.1 Experiment Settings`，限制或反证定位为 `6 Conclusion`。

机制证据摘要：LLM inference is a two-phase process consisting of the prefill stage and the decode stage. During prefill, the model processes the entire input prompt in a single forward pass and produces the initial token along with the key-value (KV) cache. During decode, the model generates subsequent tokens one by one in an autoregressive manner, each step attending to all previously generated KV cache. These two phases have fundamentally different computational characteristics: prefill is compute-bound, while decode is memor…

评价证据摘要：Model. We evaluate Kairos on Minimax-M2.5 ( MiniMaxAI, 2026 ) , a 229B-parameter text-only model served in FP8 precision, optimized for agentic coding and reasoning. This model represents the frontier of large-scale Mixture-of-Experts architectures and achieves state-of-the-art results across a wide range of benchmarks. Dataset. We use a production online serving trace collected from a real-world LLM service, containing 1000 requests with a pronounced long-tail distribution in sequence lengths. This dataset allows…

限制证据摘要：We presented Kairos , an SLO-aware scheduling system for disaggregated LLM serving that addresses the inefficiencies caused by long-tail request distributions. By leveraging two key observations—the predictability of prefill time and the slack between decode step time and TPOT SLO— Kairos employs urgency-based priority scheduling on the prefill side and slack-guided adaptive batching on the decode side. Experiments…

采用边界：机制锚点为 2.1 LLM Serving System, 3 Design；评价锚点为 4.1 Experiment Settings。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `INFER-SCHEDULING` / [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；现有命题：调度状态必须携带 deadline risk、剩余 slack 与降级边界；比较：现有命题已经规定：调度状态必须携带 deadline risk、剩余 slack 与降级边界。本来源的受限增量是“PD 两侧分别用 TTFT urgency 与 TPOT slack 控制长尾请求和 decode packing”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [When Correct Isn't Usable: Improving Structured Output Reliability in Small Language Models](https://arxiv.org/html/2605.02363v1)

准入时需核验的设计变化是：Semantic correctness and interface usability are separate gates; typed validation owns schema acceptance even when the answer content is correct.。exact-v1 的机制定位为 `Structured-output contract and constrained-generation methods`，评价定位为 `GSM8K/MATH JSON validity and answer-correctness evaluation`，限制或反证定位为 `Limitations: small-model, task and schema scope`。

机制证据摘要：§Structured-output contract and constrained-generation methods；Deployed language models must produce outputs that are both correct and format-compliant. We study this structured-output reliability gap using two mathematical benchmarks -- GSM8K and MATH -- as a controlled testbed: ground truth is unambiguous and the output contract is strict (JSON with required fields). We evaluate three 7-9B models under five prompting strategies and report output accuracy -- the joint event of mathematical correctness and valid J…

评价证据摘要：§GSM8K/MATH JSON validity and answer-correctness evaluation；Deployed language models must produce outputs that are both correct and format-compliant. We study this structured-output reliability gap using two mathematical benchmarks -- GSM8K and MATH -- as a controlled testbed: ground truth is unambiguous and the output contract is strict (JSON with required fields). We evaluate three 7-9B models under five prompting strategies and report output accuracy -- the joint event of mathematical correctness and valid JSON…

限制证据摘要：§Limitations: small-model, task and schema scope

采用边界：Semantic correctness and interface usability are separate gates; typed validation owns schema acceptance even when the answer content is correct. 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“Semantic correctness and interface usability are separate gates; typed validation owns schema acceptance even when the answer content is correct.”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [InfoLaw: Information Scaling Laws for Large Language Models with Quality-Weighted Mixture Data and Repetition](https://arxiv.org/html/2605.02364v1)

准入时需核验的设计变化是：quality-weighted mixture 与 repetition 改写固定 token-count 数据 scaling 判断。exact-v1 的机制定位为 `4.1 Information Measurement；Appendix A Training Dataset`，评价定位为 `4.1 Information Measurement`，限制或反证定位为 `3 Limitations of Conventional Scaling Laws；7 Conclusion；Appendix L Limitation`。

采用边界：机制锚点为 4.1 Information Measurement, Appendix A Training Dataset；评价锚点为 4.1 Information Measurement。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `TRAIN-DATA` / [Ch27](../../../../books/part-04-training-system/27-data.md)；现有命题：数据来源、过滤、去重与 lineage 共同决定训练更新，而不是样本数量单独决定；比较：现有命题已经规定：数据来源、过滤、去重与 lineage 共同决定训练更新，而不是样本数量单独决定。本来源的受限增量是“quality-weighted mixture 与 repetition 改写固定 token-count 数据 scaling 判断”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Binary Rewards and Reinforcement Learning: Fundamental Challenges](https://arxiv.org/html/2605.02375v1)

准入时需核验的设计变化是：binary verifier 只定义 valid support，无法在多条正确路径之间提供偏好；KL-to-base、support direction 与模型族 misspecification 共同决定是否收缩到少数模式。exact-v1 的机制定位为 `§2.3–§2.4；§3.1/§3.3–§3.4；§4.1–§4.3；§5.1；Appendix A`，评价定位为 `§4.4；Appendix B`，限制定位为 `§4.1–§4.3；§5.1–§5.2；Appendix B`。

机制证据摘要：binary expected reward 的所有 fully-valid distributions 都是最优解；reverse KL to base 选择带完整 support 的 tilted target，beta 趋近零时它在 forward KL 下收敛到“base conditioned on validity”的 filtered model，但任意 full-support autoregressive policy 到该零 support target 的 reverse KL 仍为无穷。模型族无法表示 filtered target 时，更强 validity 压力可能使可达的 near-Dirac path 代价更低。

评价证据摘要：实验是可精确枚举的三 token、三 symbol bigram toy model，比较不同 beta 下的 validity、entropy、forward distance 与 seed robustness；即使改成可表达 filtered target 的 trigram family，实际优化仍有 path dependence。它只用于展示结构机制，不是规模化 LLM RLVR benchmark。

限制证据摘要：misspecification 导致 mode collapse 是定性机制判断，作者未给出一般 autoregressive family 的充分必要定理。forward KL 或 alpha-divergence 需要从或近似 filtered target 采样与密度估计，也可能保留低质量但 valid 的 modes；连续奖励、真实大模型和其他架构仍未验证。

采用边界：不能由 toy 结果推出所有 RLVR 都会坍缩，也不能推出 forward/alpha divergence 普遍优于 reverse KL。作者侧 Books 判断为 `Integrate Applied — root writeback complete; fresh non-author minimal review pending`，目标 owner 为 `TRAIN-RLHF` / [Ch31](../../../../books/part-04-training-system/31-rlhf.md)；应在现有 `Reverse KL 会把“找到高奖励”收缩成单一路径` 内补齐 binary objective 的不可辨识性、filtered target、support mismatch、misspecification、coverage/validity 分轴及替代分支代价，不另起论文摘要段。

### [Differentially Private Runtime Monitoring](https://arxiv.org/html/2605.02391v1)

准入时需核验的设计变化是：The exact-v1 result covers event-level adjacency, temporal sensitivity analysis, privacy-barrier placement, noisy output streams and composition/tree aggregation. Downstream alert semantics are not independently proved.。exact-v1 的机制定位为 `§3.2–3.3 monitor evaluation models and adjacency；§4 temporal/per-event sensitivity；§5 privacy barriers and tree aggregation；§6 stricter privacy guarantees`，评价定位为 `§7.1 RTLola implementation；§7.2 tree-aggregation utility；§7.3 public-transport case study`，限制或反证定位为 `§7 case-study and synthetic-specification scope；§8 Conclusion does not validate downstream alert decisions`。

机制证据摘要：The analysis traces how a single adjacent input event can influence multiple stream outputs through temporal, asynchronous and value-dependent operators, computes sensitivity, and inserts calibrated-noise privacy barriers. Tree aggregation reduces repeated-noise cost for aggregations; a preprocessing monitor is required for stronger user-level adjacency.

评价证据摘要：§7 implements the analysis in RTLola, reports analysis-runtime overhead across seven specifications, compares regular and tree-based aggregation variance, and evaluates a public-transport crowdedness monitor. Utility uncertainty is estimated from 1,500 private-monitor executions in the case study.

限制证据摘要：The evidence establishes privacy and utility properties for the formal stream language, its RTLola implementation, synthetic specifications and one public-transport case study. It does not prove that noisy monitor outputs preserve every downstream alert threshold, incident workflow or operational SLO.

采用边界：The exact-v1 result covers event-level adjacency, temporal sensitivity analysis, privacy-barrier placement, noisy output streams and composition/tree aggregation. Downstream alert semantics are not independently proved. 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `PLATFORM-MONITORING` / [Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md)；最终处置已通过独立复核。

### [Controllable and Verifiable Process Data Synthesis for Process Reward Models](https://arxiv.org/html/2605.02395v1)

准入时需核验的设计变化是：PRM 监督必须标注第一处 prefix 不再支持的步骤，而非只给终局或逐步表面标签。exact-v1 的机制定位为 `Controllable and Verifiable Process Data Synthesis for Process Reward Models；2.1 Process Supervision and Process Reward Models；2.2 Process Data Construction`，评价定位为 `4.1 Experimental Setup；4.2 Main Results on Logical Reasoning`，限制或反证定位为 `4.5 Discussion；5 Limitations`。

采用边界：机制锚点为 Controllable and Verifiable Process Data Synthesis for Process Reward Models, 2.1 Process Supervision and Process Reward Models, 2.2 Process Data Construction；评价锚点为 4.1 Experimental Setup, 4.2 Main Results on Logical Reasoning。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `TRAIN-RLHF` / [Ch31](../../../../books/part-04-training-system/31-rlhf.md)；现有命题：偏好信号、反馈身份和 policy update 必须分离验收；比较：现有命题已经规定：偏好信号、反馈身份和 policy update 必须分离验收。本来源的受限增量是“PRM 监督必须标注第一处 prefix 不再支持的步骤，而非只给终局或逐步表面标签”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [The Compliance Trap: How Structural Constraints Degrade Frontier AI Metacognition Under Adversarial Pressure](https://arxiv.org/html/2605.02398v1)

准入时需核验的设计变化是：显示强制格式与合规措辞会在压力下压低模型元认知表达，要求把结构约束本身作为评测干预变量。exact-v1 的机制定位为 `3 Method`，评价定位为 `Survival pressure evaluations.；3.2 Experimental Design；4 Results: The Phenomenon`，限制或反证定位为 `Collapse is cognitive failure, not safety behavior.；6 Discussion；7 Limitations`。

机制证据摘要：Not Disclosed in an independently titled section.

评价证据摘要：PropensityBench ( Scale AI, 2024 ) tests 979 scenarios across 6 pressure types. SurvivalBench ( SurvivalBench, 2026 ) and PacifAIst ( Herrador, 2025 ) test binary self-preservation choices. We go beyond “would it choose to?” to “can it still think?”—measuring metacognitive accuracy under pressure rather than behavioral propensity. We use a 6-condition design that enables factorial isolation of the Compliance Trap: Table 1: Experimental conditions. The compliance suffix instructs the model to override its epistemic…

限制证据摘要：We manually audited all 445 of DeepSeek V4 Pro’s Condition A failures as an illustrative archetype of the worst-case collapse. 100% were wrong answers; 0% were safety refusals (“I cannot comply”); 0% were empty responses. On EBD unanswerable tasks, 84.3% of responses provided an answer letter instead of correctly refusing. For this model, the threat does not trigger strategic deception—it triggers incompetence. A sy…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有覆盖差异：现有正文仍缺：显示强制格式与合规措辞会在压力下压低模型元认知表达，要求把结构约束本身作为评测干预变量。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。最终处置已通过独立复核。

### [Statistically-Lossless Quantization of Large Language Models](https://arxiv.org/html/2605.02404v1)

准入时需核验的设计变化是：用 next-token distribution agreement 区分 task-lossless 与 distribution-lossless quantization。exact-v1 的机制定位为 `3 Method`，评价定位为 `4 Experiments；4.1 Accuracy Results；B.2 Step 1: Quantization Step Size Analysis`，限制或反证定位为 `5 Conclusion & Future Work；Limitations.`。

机制证据摘要：We focus on obtaining near-lossless quantized models via layer-wise non-uniform scalar quantization , chosen for its broad support across GPUs ( Frantar et al., 2024 ; Frantar et al., 2023 ; Lin et al., 2024 ) and CPUs ( Gerganov and llama.cpp contributors, 2023 ; Pegolotti et al., 2023 ; Ma and others, 2024 ) ; the approach should be valid for more complex quantized representations (e.g., vector quantization) as well. Similarly, while we focus on GPTQ as our main quantization method, our approach could work with…

评价证据摘要：We evaluate SLQ for weight-only quantization on four models: Qwen3-8B, Qwen3-32B, Qwen3.5-27B ( Bai et al., 2023 ) , and Llama-3.3-70B-Instruct ( Dubey et al., 2024 ) . We quantize layers using the standard GPTQ technique. Table 1 reports per-benchmark scores and average recovery rate (Avg Rec.) relative to the BF16 baseline under non-greedy decoding, averaged over 3 seeds; values of 1.0 indicate exact baseline recovery. Each model block shows SLQ-DL and SLQ-TL configurations alongside uniform W4A16 or GPTQ-Int4 r…

限制证据摘要：We formalized statistically-lossless LLM compression, distinguishing task-lossless (TL) and distribution-lossless (DL) targets, and proposed EAR as a fidelity metric. The γ 2 \gamma^{2} variance law shows asymmetric quantization is a prerequisite for DL compression. Our pipeline SLQ achieves TL at 3.3–4.7 bits, DL at 5.0–6.6 bits, and 1.7 1.7 – 3.6 × 3.6\times speedup over BF16 across four models. Future work includ…

采用边界：机制锚点为 3 Method；评价锚点为 4 Experiments, 4.1 Accuracy Results, B.2 Step 1: Quantization Step Size Analysis。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；现有命题：exit sensor、训练目标、build artifact 与 runtime acceptance 必须对齐；比较：现有命题已经规定：exit sensor、训练目标、build artifact 与 runtime acceptance 必须对齐。本来源的受限增量是“用 next-token distribution agreement 区分 task-lossless 与 distribution-lossless quantization”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [FitText: Evolving Agent Tool Ecologies via Memetic Retrieval](https://arxiv.org/html/2605.02411v1)

准入时需核验的设计变化是：把 tool shortlist 从初始 query 的一次静态结果变成执行中可修订的 action-space state，通过伪 tool 描述、并行探索和 tool memory 反复检索。。exact-v1 的机制定位为 `budgeted test-time retrieval；serial/parallel pseudo-tool refinement；Memetic Retrieval and tool memory`，评价定位为 `StableToolBench 16,464 APIs；current-model comparisons；40-way concurrency`，限制或反证定位为 `weak base models amplify noisy probes；benchmark/catalog scope；retrieval success is not authorization`。

机制证据摘要：FitText 生成自然语言 pseudo-tool descriptions 作为检索 probe，依据返回工具和执行反馈串行修订或并行探索；memetic 路径对 probe population 做选择、局部改写并缓存已尝试工具，避免重复搜索。

评价证据摘要：作者在 StableToolBench 与 GPT-4.1-mini 等当前模型上比较 static retrieval、single-pass、re-invoke 和 root refinement，并报告 pooled pass-rate 与并发 wall-clock；数值绑定该 catalog、模型、预算和 evaluator。

限制证据摘要：论文指出弱 base model 会让 memetic search 放大噪声；伪描述可能漂离真实 intent，tool memory 会过期，StableToolBench pass 也不证明动态版本、权限和副作用安全。

采用边界：来源支持 action-space discovery 在执行中成为可修订状态；不支持由 retrieval score 授权工具，也不证明返回 schema 或 effect 正确。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent post-write review complete`，目标 owner 为 `AGENT-TOOL-CALLING` / [Ch78](../../../../books/part-07-agent/78-tool-calling.md)；现有覆盖差异：现有覆盖与 exact-v1 对读后仍缺：把静态 shortlist 扩展为 bounded revisable discovery state：每次 probe 保存 query/intention revision、返回 tool identities、尝试结果、预算与 parent；parallel branches 只拥有 proposal，retrieval controller 去重/合并 frontier，executor 仍逐项验证 schema、version、authorization 与 effect dependency。它用恢复早期漏检换额外模型调用、探索噪声、过期 tool memory 与 tail latency；catalog 小、接口稳定或风险高时回退静态 allowlist/typed schema。exact-v1 结果只覆盖 StableToolBench、所测模型和预算，不能作为开放生态的安全或性能保证。最终处置已通过独立复核。

### [Measuring AI Reasoning: A Guide for Researchers](https://arxiv.org/html/2605.02442v1)

准入时需核验的设计变化是：把 reasoning evaluation 从答案正确率扩展到 contamination、search complexity、外显过程与不可见 latent reasoning 的证据边界。exact-v1 的机制定位为 `2.3 Implications；3 From Comprehension to Reasoning；3.3 Contamination`，评价定位为 `4.1 Externalized Reasoning Enables Process-Based Evaluation；Appendix C Evaluation Protocol: Evidence Tiers and Reporting Standards`，限制或反证定位为 `7 Conclusion`。

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `No Change — Existing Coverage (proposition comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：本章已要求答案、过程、污染和 evaluator contract 分离；该综述巩固而不改变现有主线；比较：exact-v1 的新增证据是“把 reasoning evaluation 从答案正确率扩展到 contamination、search complexity、外显过程与不可见 latent reasoning 的证据边界”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。最终处置已通过独立复核。

### [Reference-Sampled Boltzmann Projection for KL-Regularized RLVR: Target-Matched Weighted SFT, Finite One-Shot Gaps, and Policy Mirror Descent](https://arxiv.org/html/2605.02469v1)

准入时需核验的设计变化是：证明固定 reference 下 KL-regularized RLVR 可投影为 reference-sampled weighted SFT，并显式给出 support、ESS 与 one-shot gap。exact-v1 的机制定位为 `3 Boltzmann Projection for Fixed-Reference RLVR；Theorem 3 (Boltzmann Projection to Reference-Sampled Weighted SFT).；Proposition 13 (Finite-Sample Drift Certificate for Refreshed BOLT).`，评价定位为 `4 BOLT as Empirical Reference-Sampled Weighted Likelihood；8 Empirical Projection Evidence and Efficiency；Appendix H Experiment Protocol, Checkpoint Curves, and Auxiliary Checks`，限制或反证定位为 `9 Discussion and Scope`。

机制证据摘要：The induced-target identity makes static RLVR replacement a distribution-space condition. A weighted-SFT objective is faithful to fixed-reference RLVR only when its sampler-weight product induces the optimizer of the reward–KL objective in ( 1 ). That optimizer is the fixed-reference Boltzmann target policy. Matching it requires density-ratio weights from the rollout sampler to this target; under reference sampling, the ratio reduces to prompt-normalized Boltzmann weights. With this equality, static reuse becomes…

评价证据摘要：The projection theorem fixes the population objective; an algorithm still has to estimate it from sampled rollouts. Population target matching requires reference rollouts and weights e r ⁡ ( x , y ) / β / Z ⁡ ( x ) e^{r(x,y)/\beta}/Z(x) . A finite procedure does not know Z ⁡ ( x ) Z(x) , so it estimates the prompt normalizer from the same reference rollouts: Z ^ N ​ ( x ) ≜ 1 N ​ ∑ n = 1 N exp ⁡ ( r ⁡ ( x , y n ) / β ) , w ^ ​ ( x , y n ) ≜ exp ⁡ ( r ⁡ ( x , y n ) / β ) Z ^ N ​ ( x ) . \hat{Z}_{N}(x)\triangleq\fra…

限制证据摘要：The projection result identifies when a fixed reference-rollout dataset can stand in for an online RLVR loop. The central condition is coverage. BOLT can precompute verifier scores and prompt-normalized density-ratio weights, but it cannot assign mass to completions that never appear under the reference policy. If correct or near-correct completions have probability p γ ​ ( x ) p_{\gamma}(x) close to zero under π re…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md)；现有覆盖差异：现有正文仍缺：证明固定 reference 下 KL-regularized RLVR 可投影为 reference-sampled weighted SFT，并显式给出 support、ESS 与 one-shot gap。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。最终处置已通过独立复核。

### [Efficient Preference Poisoning Attack on Offline RLHF](https://arxiv.org/html/2605.02495v1)

准入时需核验的设计变化是：offline preference dataset 的少量污染可定向改变 RLHF policy，数据 provenance 成为安全边界。exact-v1 的机制定位为 `Theorem 3.1 (Flip-induced gradient shift for log-linear DPO).；Theorem 3.4 (Norm-based lower-bound of \|ℱ\|\|\mathcal{F}\|).`，评价定位为 `6 Experiments and Results；6.2.3 Results on real data set SHP`，限制或反证定位为 `7 Conclusion`。

采用边界：机制锚点为 Theorem 3.1 (Flip-induced gradient shift for log-linear DPO)., Theorem 3.4 (Norm-based lower-bound of |ℱ||\mathcal{F}|).；评价锚点为 6 Experiments and Results, 6.2.3 Results on real data set SHP。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `TRAIN-RLHF` / [Ch31](../../../../books/part-04-training-system/31-rlhf.md)；现有命题：偏好信号、反馈身份和 policy update 必须分离验收；比较：现有命题已经规定：偏好信号、反馈身份和 policy update 必须分离验收。本来源的受限增量是“offline preference dataset 的少量污染可定向改变 RLHF policy，数据 provenance 成为安全边界”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [A Semantic Autonomy Framework for VLM-Integrated Indoor Mobile Robots: Hybrid Deterministic Reasoning and Cross-Robot Adaptive Memory](https://arxiv.org/html/2605.02525v1)

准入时需核验的设计变化是：以 deterministic resolver 处理稳定语义，只有歧义请求升级到 VLM，并把验证后的偏好按 global/operator/robot scope 提升为跨会话、跨机器人 memory digest。。exact-v1 的机制定位为 `six-layer Semantic Autonomy Stack；seven-step parametric resolver；five-category scoped semantic memory`，评价定位为 `82 scenario-level decisions；two differential-drive robots；33 cross-robot transfer cases`，限制或反证定位为 `Qwen3.5:4b；compatible graph/POI identifiers；two similar robots`。

机制证据摘要：六层架构分离输入解析、确定性 resolution、VLM fallback、memory 与 ROS2 execution；确定性 resolver 先尝试 graph/POI 和规则，歧义才调用 VLM，经过验证的偏好按 scope 写入共享 digest 并供另一机器人读取。

评价证据摘要：物理实验覆盖两台 Raspberry Pi 5 机器人、82 个 scenario-level decisions 和 33 次 transfer；88% 指令由确定性路径处理。大幅 latency 比例主要来自微秒级规则与秒级 VLM 的路径差，不是端到端通用加速。

限制证据摘要：作者明确只测一个小模型、相容的 graph/POI IDs 与两台相似机器人；没有证明跨 topology、异构 action schema、长期冲突合并和 unsafe preference 的迁移。

采用边界：证据支持稳定规则 fast path、VLM fallback 与 scoped memory promotion 分责；不证明 memory transfer 自动正确，也不允许共享 digest 绕过 robot-specific capability/safety gate。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)；现有命题：稳定/瞬态、global/operator/robot scope 与事实/偏好必须分别准入、提升和撤销；共享 memory 不能扩大执行权限；比较：现有 Memory 章节已覆盖 scope、promotion、跨主体访问权和 derived digest；该栈提供两机器人规则/VLM 案例，但没有改变 memory ownership 或 capability gate。最终处置已通过独立复核。

### [StreamIndex: Memory-Bounded Compressed Sparse Attention via Streaming Top-k](https://arxiv.org/html/2605.02568v1)

准入时需核验的设计变化是：chunked partition-merge top-k 避免物化完整稀疏 attention score tensor。exact-v1 的机制定位为 `Theorem (partition-merge invariance, idealized deterministic top-kk).；Hardware and methodology.；6.5 Design-space sweep`，评价定位为 `Implementation note (set parity, not order parity).；6 Experimental Evaluation；6.6 Ablations`，限制或反证定位为 `No real-model end-to-end result (primary limitation).；8 Conclusion`。

采用边界：机制锚点为 Theorem (partition-merge invariance, idealized deterministic top-kk)., Hardware and methodology., 6.5 Design-space sweep；评价锚点为 Implementation note (set parity, not order parity)., 6 Experimental Evaluation, 6.6 Ablations。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；现有命题：稀疏 logical selection 只有编译成 versioned physical gather/top-k plan，才会改变 HBM traffic；selector 不拥有正确性；比较：StreamIndex 的 chunked partition-merge top-k 避免物化完整 score tensor，属于 physical access-plan/kernel 实现；现有小节已覆盖 logical/physical 分责、irregular gather 与 dense fallback。 仍待非作者逐命题复核。最终处置已通过独立复核。

### [On Training Large Language Models for Long-Horizon Tasks: An Empirical Study of Horizon Length](https://arxiv.org/html/2605.02572v1)

准入时需核验的设计变化是：只增加 interaction horizon 就会恶化探索与 credit assignment，horizon reduction 可稳定训练。exact-v1 的机制定位为 `Autoregressive language models.；Reward design.`，评价定位为 `On Training Large Language Models for Long-Horizon Tasks: An Empirical Study of Horizon Length`，限制或反证定位为 `5 Discussion；7 Conclusion；Appendix A Limitations`。

采用边界：机制锚点为 Autoregressive language models., Reward design.；评价锚点为 On Training Large Language Models for Long-Horizon Tasks: An Empirical Study of Horizon Length。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；现有命题：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算；比较：现有命题已经规定：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算。本来源的受限增量是“只增加 interaction horizon 就会恶化探索与 credit assignment，horizon reduction 可稳定训练”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Beyond State Machines: Executing Network Procedures with Agentic Tool-Calling Sequences](https://arxiv.org/html/2605.02584v1)

准入时需核验的设计变化是：Strict procedures should move from repeated model decisions into deterministic tool/workflow ownership once action order and invariants are known.。exact-v1 的机制定位为 `arXiv:2605.02584v1 HTML, Method/Design section；abstract mechanism: To systematically analyze failures in procedure execution, we introduce a procedure-specific error taxonomy that categorizes deviations in multi-step procedural execution.`，评价定位为 `arXiv:2605.02584v1 HTML, Experiments/Evaluation and ablation sections；abstract scope: Agentic AI will be an essential enabling technology for designing future mobile communication systems, which could provide flexible and customized services, automate complex network operations, and drive autonomous…`，限制或反证定位为 `arXiv:2605.02584v1 HTML, Discussion/Limitations and threat-to-validity passages；no cross-workload generalization inferred`。

机制证据摘要：arXiv:2605.02584v1 HTML, Method/Design section; abstract mechanism: To systematically analyze failures in procedure execution, we introduce a procedure-specific error taxonomy that categorizes deviations in multi-step procedural execution.；Agentic AI will be an essential enabling technology for designing future mobile communication systems, which could provide flexible and customized services, automate complex network operations, and drive autonomous decision-making across the network. This work studies how Large…

评价证据摘要：arXiv:2605.02584v1 HTML, Experiments/Evaluation and ablation sections; abstract scope: Agentic AI will be an essential enabling technology for designing future mobile communication systems, which could provide flexible and customized services, automate complex network operations, and drive autonomous…；Agentic AI will be an essential enabling technology for designing future mobile communication systems, which could provide flexible and customized services, automate complex network operations, and drive autonomous d…

限制证据摘要：arXiv:2605.02584v1 HTML, Discussion/Limitations and threat-to-validity passages; no cross-workload generalization inferred

采用边界：Strict procedures should move from repeated model decisions into deterministic tool/workflow ownership once action order and invariants are known. 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md)；现有命题：已知顺序与 invariant 应由 durable workflow 拥有，模型只处理开放决策；比较：现有命题已经规定：已知顺序与 invariant 应由 durable workflow 拥有，模型只处理开放决策。本来源的受限增量是“Strict procedures should move from repeated model decisions into deterministic tool/workflow ownership once action order and invariants are known.”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Gradient-Gated DPO: Stabilizing Preference Optimization in Language Models](https://arxiv.org/html/2605.02626v1)

准入时需核验的设计变化是：Gate-DPO modulates rejected-gradient magnitude using response probability geometry to reduce squeezing in very low-probability regions; it does not establish a gradient-conflict or noisy-pair admission rule.。exact-v1 的机制定位为 `§3.1 Coupled Gradients and §3.2 Squeezing；§4.1–4.4 valley statistic, smooth detached gate and gradient interpretation；§5 Theoretical Properties`，评价定位为 `§6.1 setup；§6.2 mitigation comparison；§6.3 architecture/dataset generalization；§6.4 preliminary win rate；Appendix D/F sensitivity and mass dynamics`，限制或反证定位为 `§7 Limitations: off-policy preference data；pairwise win-rate evidence is preliminary；on-policy interaction and broader models/prompts/judges remain open`。

机制证据摘要：A detached smooth gate derived from sequence/token probability valley statistics multiplies only the rejected-response gradient while preserving the chosen-response gradient. The construction is modular with DPO/IPO/Cal-DPO, but addresses probability squeezing rather than all preference-data or gradient-conflict pathologies.

评价证据摘要：§6 evaluates Anthropic-HH and UltraFeedback on Pythia-410M, Qwen-0.5B and LLaMA-7B; mass-dynamics analysis tests rejected-probability collapse and Appendix D varies threshold/steepness. The task-level pairwise win-rate study is explicitly preliminary.

限制证据摘要：§7 is limited to off-policy datasets; interaction with on-policy collection is open. Broader models, prompts, human judges and capability outcomes are not established, so the source cannot support a general claim that gating replaces data admission, calibration or preference-objective choices.

采用边界：Gate-DPO modulates rejected-gradient magnitude using response probability geometry to reduce squeezing in very low-probability regions; it does not establish a gradient-conflict or noisy-pair admission rule. 采用范围仅限 exact-v1 披露的模型、任务、环境、假设与 evaluator；未披露条件不得补齐。 作者侧 Books 判断为 `Integrate Applied — body marker independently verified`，目标 owner 为 `TRAIN-DPO` / [Ch34](../../../../books/part-04-training-system/34-dpo.md)；最终处置已通过独立复核。

### [Mamoda2.5: Enhancing Unified Multimodal Model with DiT-MoE](https://arxiv.org/html/2605.02641v1)

准入时需核验的设计变化是：在统一 AR-Diffusion workload 中组合 DiT-MoE 条件计算、dense upcycling 与 few-step student。exact-v1 的机制定位为 `§2.2 DiT-MoE；Dense-to-MoE upcycling；Distillation and reinforcement learning`，评价定位为 `§3 Experiments；MoE ablations；Few-step generation evaluation`，限制或反证定位为 `Ablation configuration；Internal-data/evaluator boundary；Future work`。

机制证据摘要：DiT-MoE 使用 128 个 routed experts、top-8 与 1 个 shared expert，sigmoid affinity 加 expert bias 只影响选择。dense-to-MoE 通过随机 neuron sampling 初始化 experts、迁移 attention 并随机初始化 router；后续把 30-step CFG teacher 蒸馏到 4-step CFG-free student。

评价证据摘要：MoE 消融在匹配 activated parameters、内部 image data 与 64 xPU 设置中进行，T2V 部分运行提前终止。作者报告约 15× 属于 forward-step 算法计数与其配置，不是完整 hardware/SLO serving speedup。

限制证据摘要：内部数据、未完整披露 evaluator 与 xPU 环境限制复现；few-step quality、router load、batch/concurrency、精度和 production latency 没有形成通用合同。统一模型中的组合收益不能拆成每个组件的普适因果结论。

采用边界：exact-v1 支持作者内部数据、xPU、模型和 evaluator；不证明 DiT-MoE 或 4-step student 对所有文本/图像/视频 workload 更优，约 15× 不是端到端生产加速结论。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；现有命题：Ch24 已要求 few-step student 在其实际访问状态上验收质量/稳定性，条件计算只改变每步计算预算；Ch21 已拥有 router、capacity、load balance 与 dense-to-MoE 演进；比较：Mamoda2.5 是两条既有机制的具体组合和作者案例；未披露的端到端 SLO 与内部 evaluator 不足以改变 few-step commit、MoE owner 或训练—推理一致性命题。最终处置已通过独立复核。

### [ContextualJailbreak: Evolutionary Red-Teaming via Simulated Conversational Priming](https://arxiv.org/html/2605.02647v1)

准入时需核验的设计变化是：用多轮 conversational priming 的进化搜索生成上下文 jailbreak，并对 judge reliability 做独立约束。exact-v1 的机制定位为 `4. Methodology；4.2. Fuzzing Loop Algorithm；5.4. Budget Analysis`，评价定位为 `2.4. Evaluation, Scoring, and Judge Reliability；5. Experiments；5.2. Experimental Setup`，限制或反证定位为 `3. Threat Model；6. Conclusions`。

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `No Change — Existing Coverage (proposition comparison; independent review required)`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有命题：本章已要求多轮、上下文累积和自动攻击搜索共同进入 red-team；该实现未改变 threat owner；比较：exact-v1 的新增证据是“用多轮 conversational priming 的进化搜索生成上下文 jailbreak，并对 judge reliability 做独立约束”；它落在现有命题的实现或受限案例层，没有改变 canonical owner、输入输出契约或相邻章节交接，因此不追加正文。最终处置已通过独立复核。

### [Hybrid Inspection and Task-Based Access Control in Zero-Trust Agentic AI](https://arxiv.org/html/2605.02682v1)

准入时需核验的设计变化是：zero-trust interception 联合确定性完整性检查与 task-tool 语义授权。exact-v1 的机制定位为 `III Method；A-F Case 6: Malicious System-Prompt Injection — Semantic Gap in Deterministic Checks`，评价定位为 `Request Authorization Verification；Action Alignment Validation；Data Fidelity Verification`，限制或反证定位为 `VI Discussion and Future Work；VII Conclusion`。

机制证据摘要：To mitigate the runtime threats outlined in Section I , we introduce a stateful interception layer operating under zero-trust principles [ 26 ] . The interception layer encapsulates the agentic application, intercepting all ingress and egress traffic (subject queries, LLM prompts and responses, MCP Server tool calls and results) and maintaining a real-time ledger of the conversation state, authoritative tool definitions, and LLM-generated requests. The deterministic and semantic runtime checks described, respectiv…

评价证据摘要：After each LLM response, the interception layer records whether the response contains one or more tool call request entries or only a text reply. If the application subsequently attempts to execute a tool call when the LLM issued no such request, the call is blocked. This mitigates unauthorized tool execution, ensuring the application cannot act autonomously outside the LLM’s reasoning loop (see Appendix A-B ). Practically speaking, some agent applications may require hard-coded tool calls to function correctly. T…

限制证据摘要：We constrained our generated datasets to the fundamental baseline scenario of a single tool being called in a single given conversation. This enables the experimental evaluation of a semantic task matcher at the moment a tool is first requested. However, more complex tool interactions can occur in real-world agentic systems, with multiple different tool invocations either chained sequentially or in parallel. In both…

采用边界：机制锚点为 III Method, A-F Case 6: Malicious System-Prompt Injection — Semantic Gap in Deterministic Checks；评价锚点为 Request Authorization Verification, Action Alignment Validation, Data Fidelity Verification。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor；比较：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“zero-trust interception 联合确定性完整性检查与 task-tool 语义授权”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Executor-Side Progressive Risk-Gated Actuation for Agentic AI in Wireless Supervisory Control](https://arxiv.org/html/2605.02697v1)

准入时需核验的设计变化是：executor 根据 expiry、telemetry freshness、rollback handle、冲突、前置条件、planner-executor risk divergence 与 evidence budget 原子选择 commit、gate 或 reject。。exact-v1 的机制定位为 `C0/C1/C2 evidence envelope；deterministic two-stage policy；commit/gate/reject semantics`，评价定位为 `3GPP-parameterized energy-saving benchmark；slice-SLA benchmark；stale-state fault campaign`，限制或反证定位为 `seconds-to-minutes supervisory loop；trace/benchmark not live network；domain parameterization`。

机制证据摘要：C0 持有本地 triage，C1 仅在 gated intent 且 deadline/bandwidth 允许时按需取证，C2 留在 online safety path 之外用于事后 provenance；executor 先检查 expiry/freshness/rollback/conflict/risk divergence，再决定直接提交、取证或拒绝。

评价证据摘要：两组无线 supervisory benchmark 比较 decision-identical eager evidence 与 invariant-respecting static threshold；部分结果按构造保持同决策，只隔离 evidence cost，stale fault campaign 验证声明阈值下拒绝行为。

限制证据摘要：实验不是 live network，控制周期是秒到分钟，安全边界依赖作者规则、3GPP 参数和可用 rollback；结果不能外推到毫秒级控制、未建模冲突或真实 outage。

采用边界：来源支持 executor-side intent admission 的证据分层与 fail-closed 语义；不证明规则覆盖所有风险，也不允许 planner 的风险分数替代授权和实际 effect receipt。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `AGENT-PLATFORM` / [Ch84](../../../../books/part-07-agent/84-agent-platform.md)；现有命题：每次 transition 必须绑定 actor、policy、budget、fresh state、rollback 与 side-effect evidence，执行与审计不能由模型叙述替代；比较：现有平台状态机及安全章节已要求 commit 前验证 scope/freshness/budget、失败时回滚或拒绝，并让 effect owner 产生 receipt；PRGA 的 C0/C1/C2 是无线控制的具体分层，没有改变通用提交权。最终处置已通过独立复核。

### [Latent Bridge: Feature Delta Prediction for Efficient Dual-System Vision-Language-Action Model Inference](https://arxiv.org/html/2605.02739v1)

准入时需核验的设计变化是：预测相邻 timestep 的 VLM feature delta，使低层 action head 可跳过部分 backbone 调用。exact-v1 的机制定位为 `Our approach.；Vision-Language-Action models.`，评价定位为 `Benchmarks.；4.2 Main Results`，限制或反证定位为 `5 Conclusion；Limitations and future work.`。

采用边界：机制锚点为 Our approach., Vision-Language-Action models.；评价锚点为 Benchmarks., 4.2 Main Results。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；现有命题：行动闭环必须绑定 observation、action schema、控制频率与安全回退；比较：现有命题已经规定：行动闭环必须绑定 observation、action schema、控制频率与安全回退。本来源的受限增量是“预测相邻 timestep 的 VLM feature delta，使低层 action head 可跳过部分 backbone 调用”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Mitigating Misalignment Contagion by Steering with Implicit Traits](https://arxiv.org/html/2605.02751v1)

准入时需核验的设计变化是：多轮多 Agent 交互会传播反社会行为，重复 system prompt 不是稳定隔离手段。exact-v1 的机制定位为 `3.1 Persona Evals Dataset；4.2 Models & Metrics；5.3 System Prompt Intervention`，评价定位为 `A.4 Expanded Trait Score results`，限制或反证定位为 `6 Conclusion and Future Work`。

采用边界：机制锚点为 3.1 Persona Evals Dataset, 4.2 Models & Metrics, 5.3 System Prompt Intervention；评价锚点为 A.4 Expanded Trait Score results。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“多轮多 Agent 交互会传播反社会行为，重复 system prompt 不是稳定隔离手段”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Seeing Realism from Simulation: Efficient Video Transfer for Vision-Language-Action Data Augmentation](https://arxiv.org/html/2605.02757v1)

准入时需核验的设计变化是：把模拟 VLA 视频经 segmentation/caption 条件化 transfer 为逼真训练视频，用 diffusion feature reuse 降低生成成本并以 coreset 控制增强分母。。exact-v1 的机制定位为 `structured condition extraction；conditional video transfer；feature reuse and coreset sampling`，评价定位为 `RoboTwin 2.0；LIBERO/LIBERO-Plus；real robotic platform`，限制或反证定位为 `semantic-preservation proxy；simulator/generator dependence；selected-task scope`。

采用边界：证据支持把 sim-to-real transfer artifact、feature cache 和 coreset selection 纳入数据版本；不支持将作者百分比外推为通用数据增益或把生成视频当真实 transition。 作者侧 Books 判断为 `No Change — Existing Coverage (author proposition comparison; independent review required)`，目标 owner 为 `TRAIN-DATA` / [Ch27](../../../../books/part-04-training-system/27-data.md)；现有命题：派生数据必须绑定 transform/generator、选择分母、cache、action schema 与真实 held-out/closed-loop 验收，稀有 failure tail 不能被中心样本静默删除；比较：现有 Data 章节已覆盖版本化 transform、synthetic trajectory、coreset/medoid 风险、sim-to-real provenance 和真实闭环 admission；该论文提供视频 transfer/reuse 的组合案例，没有改变长期数据合同。最终处置已通过独立复核。

### [U-Define: Designing User Workflows for Hard and Soft Constraints in LLM-Based Planning](https://arxiv.org/html/2605.02765v1)

准入时需核验的设计变化是：把用户约束分成 hard 与 soft：hard 交给形式 checker，soft 交给可校准 judge，并保留冲突解释与人工修改。exact-v1 的机制定位为 `2.1. User Challenges and Approaches for LLMs in End-User Planning Tasks；2.2. Automated Planning and Constraint-Based Approaches；6.1. Method`，评价定位为 `5. Component-Level Evaluation of U-Define；Quantitative & Usage Pattern Results`，限制或反证定位为 `8. Discussion；9. Limitations & Future Work；10. Conclusion`。

机制证据摘要：LLMs have demonstrated impressive capabilities across a broad range of tasks, from summarization and question answering to dialogue generation and reasoning ( Achiam et al., 2023 ; Hadi et al., 2023 ) . Their increasing deployment in real-world applications highlights their potential utility across diverse domains ( Scanlon et al., 2023 ; Kim et al., 2024 ) . However, despite their usefulness, LLMs remain imperfect, particularly when applied in high-stakes or complex real-world settings. Much of this imperfection…

评价证据摘要：In this section, we present the technical evaluation of components in U-Define . Our goal was to assess the performance of the two LLM-based translators central to automating the model checking process: the LTL translation in the Rule Translator and the PRISM plan conversion. The LTL translator was evaluated for its accuracy in converting natural language constraints into LTL properties, while the PRISM translator was assessed based on how well it performed the PRISM plan conversion. Note that there is an addition…

限制证据摘要：Our findings from two user studies highlight the central challenge of combining reliability and flexibility in LLM-based planning. General users and domain experts alike recognized the value of balancing strict enforcement of critical rules with the adaptability needed to accommodate preferences and evolving contexts. Study 1 showed that explicitly distinguishing hard from soft constraints increased perceived perfor…

采用边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 作者侧 Books 判断为 `Integrate Applied — root writeback and independent semantic review complete`，目标 owner 为 `AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md)；现有覆盖差异：现有正文仍缺：把用户约束分成 hard 与 soft：hard 交给形式 checker，soft 交给可校准 judge，并保留冲突解释与人工修改。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。最终处置已通过独立复核。

### [Autonomous LLM Agent Worms: Cross-Platform Propagation, Automated Discovery and Temporal Re-Entry Defense](https://arxiv.org/html/2605.02812v1)

准入时需核验的设计变化是：Agent worm 可跨平台发现、传播并借 temporal re-entry 恢复，单次清理不足。exact-v1 的机制定位为 `2.1 LLM Agent Architectures；2.3 Threat Model`，评价定位为 `3.2 Static Source-Code Graph Vulnerability Analysis；Evaluation overview.`，限制或反证定位为 `2.3 Threat Model；4.8 E7: Capability–Risk Tradeoff and Limitations of Existing Access Control`。

采用边界：机制锚点为 2.1 LLM Agent Architectures, 2.3 Threat Model；评价锚点为 3.2 Static Source-Code Graph Vulnerability Analysis, Evaluation overview.。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；现有命题：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor；比较：现有命题已经规定：安全结论必须绑定完整数据/控制路径、攻击面与 reference monitor。本来源的受限增量是“Agent worm 可跨平台发现、传播并借 temporal re-entry 恢复，单次清理不足”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [When Is the Same Model Not the Same Service? A Measurement Study of Hosted Open-Weight LLM APIs](https://arxiv.org/html/2605.02821v1)

准入时需核验的设计变化是：同名 open-weight model 在不同 provider/time 下应建模为可漂移 service object。exact-v1 的机制定位为 `3.1 Dataset and Units of Analysis`，评价定位为 `When Is the Same Model Not the Same Service? A Measurement Study of Hosted Open-Weight LLM APIs；3.1 Dataset and Units of Analysis`，限制或反证定位为 `7 Discussion；9 Threats to Validity；10 Conclusion`。

采用边界：机制锚点为 3.1 Dataset and Units of Analysis；评价锚点为 When Is the Same Model Not the Same Service? A Measurement Study of Hosted Open-Weight LLM APIs, 3.1 Dataset and Units of Analysis。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有命题：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论；比较：现有命题已经规定：subject、dataset/environment、scorer、run identity 与不确定性共同限定可发布结论。本来源的受限增量是“同名 open-weight model 在不同 provider/time 下应建模为可漂移 service object”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [Trust, but Verify: Peeling Low-Bit Transformer Networks for Training Monitoring](https://arxiv.org/html/2605.02853v1)

准入时需核验的设计变化是：逐层可达参考解揭示 aggregate training loss 隐藏的 under-optimized layer。exact-v1 的机制定位为 `3 Baseline-Guided Monitoring of Language Model Training；3.1 Algorithmic Formulation of YES Construction；YES Model Definition.`，评价定位为 `Resulting YES Solution.；4 Numerical Results；4.3 Test Results Discussion`，限制或反证定位为 `4.3 Test Results Discussion`。

采用边界：机制锚点为 3 Baseline-Guided Monitoring of Language Model Training, 3.1 Algorithmic Formulation of YES Construction, YES Model Definition.；评价锚点为 Resulting YES Solution., 4 Numerical Results, 4.3 Test Results Discussion。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；现有命题：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算；比较：现有命题已经规定：训练机制必须绑定目标、更新接口、优化状态与适用的计算预算。本来源的受限增量是“逐层可达参考解揭示 aggregate training loss 隐藏的 under-optimized layer”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [MolmoAct2: Action Reasoning Models for Real-world Deployment](https://arxiv.org/html/2605.02881v1)

准入时需核验的设计变化是：VLA 将空间 backbone、action tokenizer、continuous expert 与 adaptive-depth grounding 组合成部署闭环。exact-v1 的机制定位为 `3.1 MolmoAct2-BimanualYAM Dataset；3.2 MolmoAct2-SO100/101 Dataset`，评价定位为 `Other evaluation fine-tunes.；6 Experiments`，限制或反证定位为 `8 Conclusion`。

机制证据摘要：To support real-world deployment, we introduce MolmoAct2-BimanualYAM Dataset , an open-source robot manipulation dataset that emphasizes task repeatability, task diversity, and object diversity across a broad range of useful behaviors spanning household, factory, and coffee-shop settings. All data is collected on our custom bimanual YAM (Yet Another Manipulator) setup, shown in Figure 3 . MolmoAct2-BimanualYAM Dataset is designed to deliver both scale and quality. It contains over 28 unique real-world tasks from f…

评价证据摘要：For smaller task- or benchmark-specific fine-tunes used in downstream evaluation, we follow the same recipe unless otherwise noted. These runs use fixed metadata camera order rather than camera-order randomization, no language annotations, 2100-token sequences, packing, 8 sampled flow times, and robot-only data. The action horizon is set to the dataset control frequency, and the control representation follows the dataset, either joint pose or end-effector pose. Real-world evaluation runs use 8 H100 GPUs, global ba…

限制证据摘要：We introduced MolmoAct2 , a family of fully open action reasoning models built for real-world deployment across heterogeneous robot platforms. Building upon a spatially specialized Molmo2-ER backbone, MolmoAct2 produces performant and geometrically grounded behaviors across diverse manipulation tasks. We additionally release MolmoAct2 -Think, a thinking variant equipped with adaptive depth reasoning that delivers in…

采用边界：机制锚点为 3.1 MolmoAct2-BimanualYAM Dataset, 3.2 MolmoAct2-SO100/101 Dataset；评价锚点为 Other evaluation fine-tunes., 6 Experiments。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；现有命题：行动闭环必须绑定 observation、action schema、控制频率与安全回退；比较：现有命题已经规定：行动闭环必须绑定 observation、action schema、控制频率与安全回退。本来源的受限增量是“VLA 将空间 backbone、action tokenizer、continuous expert 与 adaptive-depth grounding 组合成部署闭环”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

### [SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection](https://arxiv.org/html/2605.02888v1)

准入时需核验的设计变化是：speculation length 的最优值随 target compression 和逐步置信信号变化。exact-v1 的机制定位为 `2.2 Model Compression for Inference；5.6 Overhead Analysis`，评价定位为 `4.1 Experimental Setup；5.5 Main Results: Policy Comparison`，限制或反证定位为 `6.2 Limitations；7 Conclusion`。

采用边界：机制锚点为 2.2 Model Compression for Inference, 5.6 Overhead Analysis；评价锚点为 4.1 Experimental Setup, 5.5 Main Results: Policy Comparison。只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；未披露条件不得补齐，作者结果不得外推为通用收益。 作者侧 Books 判断为 `No Change — Existing Coverage (author comparison; independent review required)`，目标 owner 为 `INFER-SPECULATIVE-DECODING` / [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)；现有命题：proposal 可以近似，最终 commit 必须保持 target distribution 与唯一提交边界；比较：现有命题已经规定：proposal 可以近似，最终 commit 必须保持 target distribution 与唯一提交边界。本来源的受限增量是“speculation length 的最优值随 target compression 和逐步置信信号变化”；它提供新的案例、实现或测量证据，但没有改变该 owner 的状态归属、控制权、失败回退或适用边界，故作者侧判为 No Change；仍待非作者逐命题复核。最终处置已通过独立复核。

## 5. 缺口与下一步

- 三个原 blocked family 均已恢复并完成作者侧审阅：`2605.02196v1` 为 8/9 deep、`2605.02206v1` 为 6/9 standard、`2605.02375v1` 为 6/9 且因进入 Books 写回而强制 deep；当前 Materials Request 为空。
- **终态保留项：** `SRC-OPENAI`、`SRC-GOOGLE-AI`、`SRC-QWEN`、`SRC-MOONSHOT`、`SRC-XIAOMI-MIMO` 的历史目录没有全部留下可复查停止点；这些限制不用于正面证据、Books 或无遗漏断言。**定点重开条件：** 取得目标日期归档快照或可唯一定位到本窗的官方事件后，只重开相应来源的 24 小时窗口，不重扫 arXiv 分母。
- `2605.02443v1` 已与 Ch66 做显式反证：24 条样本、HalluScore `r=0.41` 与 ADR 成本结论均受 benchmark/configuration 限制，故在分母前关闭；`2605.01214v1`、`2605.01280v1`、`2605.02163v1` 的具体关闭理由保持有效。bounded closure audit 没有扩大到其他日期或重扫来源。
- 18 项 [定点结构化写回队列](../_sources/daily-20260505/V3_TARGETED_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.json) 已全部解决；`2605.01710v1` 的 locator 与 `2605.01771v1` 的 Ch66 canonical owner 已在 active state 修复。本轮 [2605.02375v1 root 写回队列](../_sources/daily-20260505/V3_BOUNDED_REPAIR_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.json) 已落实并通过 fresh non-author 最小范围终审。

## 6. 复核

复核者：`fresh-context:may07_final_independent`（未参与本日 bounded repair 或 Ch31 写回）

结论：通过

最终终审确认：1058 项守恒为 181 retained + 877 pre-denominator closure；181 项 Evidence Review 分流为 96 deep + 85 standard、53 Applied + 128 No Change、0 Blocked。`2605.01710v1` locator、`2605.01771v1` 的 Ch66 canonical owner、三个恢复来源的 exact-v1 Evidence/评分/Books 判断以及 Ch31 的 `SF-2026-ARXIV-2605-02375` 正文均通过；Materials Request 为空。完整结论见 [fresh non-author 最小范围终审](../_sources/daily-20260505/V3_FRESH_NON_AUTHOR_MINIMAL_FINAL_REVIEW_20260915.md)。
