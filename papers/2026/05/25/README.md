# Daily Research — 2026-05-25

**规范：** V3

**窗口：** 2026-05-24T09:00:00+08:00 ～ 2026-05-25T09:00:00+08:00

**状态：** 完成

**Books：** 纳入本次

**检查时间：** 2026-09-16T14:11:00+08:00

## 1. 结论

当前冻结 raw identity 仍为 **499 = 402 official-day-owned + 97 owner-day ambiguous terminal isolation**。402 个可正面归属项由 400 条 official OAI direct arXiv membership 与 OpenAI 官方 RSS 的 2 条事件组成；97 条 DataCite-recovered identity 只保留 identity/version 与既有阅读成果，不再进入 Candidate Denominator、Evidence 或 Books。

对 402 个 day-owned identity 的当前贡献投影为 **402 = 225 candidate + 177 family-specific pre-denominator closure + 0 withdrawn**。Evidence 为 **225 = 224 complete + 1 blocked**：106 deep complete、118 standard complete、1 deep blocked；score distribution 为 `{'6': 120, '7': 38, '8': 38, '9': 29}`。唯一 blocked 是 official-day-owned 的 `2605.23857`，材料请求保持精确。

Books 对账为 **225 = 44 Applied + 1 Deferred + 0 Integrate + 166 No Change — Existing Coverage + 8 Report Only + 6 Structural Candidate**。8 个 owner-day ambiguous Applied 依赖已从本 Daily 的正面归属中撤回并写入 quarantine；现有 Books 正文不删除，但 05-25 不再把它们当作 Applied evidence。独立 fresh non-author 已核对 owner-day 分区、候选/Evidence/Books 集合、quarantine、唯一 blocked family、材料请求和当前正文 binding，未发现新的实质缺陷，本日报完成。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方 News/Research RSS；两条 00:00Z 事件完成 event-type 与贡献筛选 | 已检查 | 2 raw，均在候选分母前关闭 |
| SRC-ANTHROPIC | 官方 Research；相邻公开项为 05-22，早于窗口 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind Research/Google Publications；相邻 dated research 为 05-19 与 05-28 | 已检查 | 部分 publications 仅年/venue，不据此支持全站 day-level no-hit |
| SRC-META-AI | 官方 Publications 入口 | 受阻 | 入口返回空/内部错误；不用于支持 no-hit，按外部保留项隔离 |
| SRC-QWEN | 官方 article index；相邻 05-20 与 05-29 | 已检查 | 无 |
| SRC-DEEPSEEK | 官方 News/Research；相邻 04-24 与 06-24 | 已检查 | 无 |
| SRC-MOONSHOT | Kimi Blog；无窗内 dated research/release/RFC | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 官方 publicList；五条可见记录均在窗外 | 已检查 | 无 |
| SRC-ZAI | 官方 Research；相邻 05-20 与 06-16 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 官方 Research/Public Papers；相邻 05-16 与 05-29 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 官方技术 Blog；最近明确 dated 项为 05-09 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 官方 dated papers；相邻 03-13 与 06-29 | 受阻 | undated blog cards 不支持 day-level no-hit，按外部边界隔离 |
| SRC-MINIMAX | 官方 Blog/Agent Tech；相邻 03-18 与 05-26/27 | 已检查 | 无 |
| SRC-ARXIV | 05-25 08:00 BJT official announcement schedule；400 条 OAI direct membership；97 条仅由 DataCite 恢复 identity/version | 受阻 | 497 arXiv identities = 225 retained + 177 closure + 97 owner-day terminal isolation；隔离项不支持正面归属 |

完整 owner 证据见 [`official-owner-batch-evidence-v3.json`](../_sources/daily-20260525/official-owner-batch-evidence-v3.json)，14-source 结构化记录见 [`source-coverage-v3.json`](../_sources/daily-20260525/source-coverage-v3.json)，499 条逐项题摘与非模板理由见 [`screening-outcomes-v3.json`](../_sources/daily-20260525/screening-outcomes-v3.json)。`已检查` 仅指注册入口的有界核验；受阻/无日级时间的入口不支持“无遗漏”。普通 GitHub commit/PR 未扩入 Daily denominator。

## 3. 候选与判断

表中只列 225 个 official-day-owned candidate。97 个 DataCite-recovered identity 及其 title、完整 abstract、既有 exact-v1 工作仍保存在 canonical JSON 中，但属于 Candidate Denominator 外的 terminal isolation，不在本表评分，也不形成当窗 Evidence 或 Books 决定。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [2605.22826 Evaluating Large Language Models in a Complex Hidden Role Game](https://arxiv.org/abs/2605.22826) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：This work investigates the reasoning, persuasion, and deceptive capabilities of LLMs within the social deduction game Secret Hitler.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.22827 Computable Fairness: Boltzmann-Softmax Control for AI Resource Allocation](https://arxiv.org/abs/2605.22827) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose Computable Fair Division (CFD), a framework that reinterprets the Boltzmann-Softmax function not as a selection tool but as a probabilistic resource allocation mechanism, redefining the inverse temperature parameter $β$ as a computable control variable governing the efficiency-fairness balance.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-GPU-SCHEDULER [章节](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md) |
| [2605.22829 LFRAG: Layout-oriented Fine-grained Retrieval-Augmented Generation on Multimodal Document Understanding](https://arxiv.org/abs/2605.22829) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To address these issues, we propose Layout-oriented Fine-grained Retrieval-Augmented Generation (LFRAG), a novel framework that advances multimodal RAG from page-level to block-level retrieval.；3+2+2=7 | 深入完成 | 已有覆盖：AGENT-RAG [章节](../../../../books/part-07-agent/76-rag.md) |
| [2605.22842 The Misattribution Gap: When Memory Poisoning Looks Like Model Failure in Agentic AI Systems](https://arxiv.org/abs/2605.22842) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-MEMORY [章节](../../../../books/part-07-agent/77-memory.md) |
| [2605.22850 ObjectCache: Layerwise Object-Storage Retrieval for KV Cache Reuse](https://arxiv.org/abs/2605.22850) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：INFER-KV-CACHE [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [2605.22855 PrefBench: Evaluating Zero-Shot LLM Agents in Hidden-Preference Personalized Pricing Negotiations](https://arxiv.org/abs/2605.22855) | 2026-05-25T08:00:00+08:00 | fresh non-author 反例恢复；分离 structured-action contract compliance、agreement rate 与 intended outcome；2+2+3=7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.22866 BOHM: Zero-Cost Hierarchical Attribution for Compound AI Systems](https://arxiv.org/abs/2605.22866) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.22868 FusionSense: Tri-Stage Near-Sensor Learning for Runtime-Adaptive Multimodal Edge Intelligence](https://arxiv.org/abs/2605.22868) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+2=7 | 深入完成 | 结构候选 |
| [2605.22869 FuRA: Full-Rank Parameter-Efficient Fine-Tuning with Spectral Preconditioning](https://arxiv.org/abs/2605.22869) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；用 block tensor-train/SVD basis 预条件化低秩更新，使有限 rank 的可用方向不只由 nominal rank 决定。；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-LORA [章节](../../../../books/part-04-training-system/30-lora.md) |
| [2605.22870 The Readout Shortcut: Positional Number Copying Dominates Arithmetic CoT Readout in Small Language Models](https://arxiv.org/abs/2605.22870) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；dense per-step/per-loop loss 只约束 readout 可见方向，模型可能把可解中间状态藏在 readout null space，并在最后一步才形成答案。；3+2+2=7 | 深入完成 | 已有覆盖：MODEL-DECODER-ONLY [章节](../../../../books/part-02-model/18-decoder-only.md) |
| [2605.22871 Approximate Machine Unlearning through Manifold Representation Forgetting Guided by Self Mode Connectivity](https://arxiv.org/abs/2605.22871) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：In this paper, we propose \textbf{ManiF-SMC} (\textbf{Mani}fold \textbf{F}orgetting with \textbf{S}elf \textbf{M}ode \textbf{C}onnectivity), motivated by the observation that a model retrained on the remaining data tends to classify erased samples by their semantic similarity to the retained data.；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md) |
| [2605.22874 NeuroNL2LTL: A Neurosymbolic Framework for Natural Language Translation of Linear Temporal Logic](https://arxiv.org/abs/2605.22874) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We present NeuroNL2LTL, a neurosymbolic architecture unifying learned translation with formal verification.；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING [章节](../../../../books/part-07-agent/78-tool-calling.md) |
| [2605.22875 RMA: an Agentic System for Research-Level Mathematical Problems](https://arxiv.org/abs/2605.22875) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We present $\textbf{Research Math Agents (RMA)}$, an agentic framework for automated reasoning on research-level mathematical problems.；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-PLANNING [章节](../../../../books/part-07-agent/79-planning.md) |
| [2605.22879 Budgeted Dynamic Trace Structures for Token-Efficient Sequential Computation](https://arxiv.org/abs/2605.22879) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；把长执行轨迹表示为带状态过滤的 rooted graph 与 append-only history，在 token/byte budget 下用 summary+suffix compaction、reference-counted observations、delta overlay 与 soft cap 保留可恢复结构。；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：AGENT-CONTEXT [章节](../../../../books/part-07-agent/75-context.md) |
| [2605.22880 How Far Will They Go? Red-Teaming Online Influence with Large Language Models](https://arxiv.org/abs/2605.22880) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We introduce an empirical red-teaming framework for measuring LLM Overton Windows (OWs), defined as the range of political opinions a model can reliably express on controversial topics, and for quantifying how simple natural-language jailbreaks expand that range.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.22883 Energy per Successful Goal: Goal-Level Energy Accounting for Agentic AI Systems](https://arxiv.org/abs/2605.22883) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在：PLATFORM-COST [章节](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [2605.22884 Tensor Cache: Eviction-conditioned Associative Memory for Transformers](https://arxiv.org/abs/2605.22884) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：INFER-KV-CACHE [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [2605.22885 ImProver 2: Iteratively Self-Improving LMs for Neurosymbolic Proof Optimization](https://arxiv.org/abs/2605.22885) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；用 Lean checker、formal-structure scaffold 与 expert-iteration/preference loop 优化已验证证明，同时以结构化 metrics 而非自由文本判断改写质量。；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING [章节](../../../../books/part-07-agent/78-tool-calling.md) |
| [2605.22891 Pointwise Metrics Mislead: An Evaluation Protocol for Multimodal Inverse Problems](https://arxiv.org/abs/2605.22891) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.22896 Agentic-VLA: Efficient Online Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2605.22896) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [2605.22897 From Residuals to Reasons: LLM-Guided Mechanism Inference from Tabular Data](https://arxiv.org/abs/2605.22897) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We introduce Multi-Agent Residual In-Context Learning (MARICL), an agentic framework in which LLM agents analyze where a base-model fails, hypothesize missing structure from high-residual examples provided in context, and produce explicit correction terms refined through multi-turn textual gradient optimization.；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-PLANNING [章节](../../../../books/part-07-agent/79-planning.md) |
| [2605.22898 FIRMA: FIbonacci Ring Model Aggregation for Privacy-preserving Federated Learning](https://arxiv.org/abs/2605.22898) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose FIRMA (\textbf{FI}bonacci \textbf{R}ing \textbf{M}odel \textbf{A}ggregation), a family of three progressively enhanced federated learning protocols: 1) \fibfl\ establishes the foundation: server-free ring aggregation with Fibonacci-weighted neighbour blending and permanently private classification heads.；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING [章节](../../../../books/part-04-training-system/36-distributed-training.md) |
| [2605.22902 Transcoders Trace Visual Grounding and Hallucinations in Vision-Language Models](https://arxiv.org/abs/2605.22902) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：These results show that function-centric circuit decomposition yields interpretable and predictive accounts of multimodal computation in VLMs.；3+2+2=7 | 深入完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2605.22903 Seeing without Looking: Do Vision-Language Benchmarks Really Test Vision?](https://arxiv.org/abs/2605.22903) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；top-1 benchmark accuracy 对视觉 token 删除、遮挡与 entity swap 可能不敏感，必须把保持输入/问题而干预视觉证据的 counterfactual test 纳入 grounding evaluation。；3+2+2=7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.22905 EVE-Agent: Evidence-Verifiable Self-Evolving Agents](https://arxiv.org/abs/2605.22905) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-PLATFORM [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [2605.22907 VideoOdyssey: A Benchmark for Ultra-Long-Context and Omni-Modal Video Understanding](https://arxiv.org/abs/2605.22907) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Driven by this metric, we introduce VideoOdyssey, a benchmark specifically designed for ultra-long-context and omni-modal video understanding.；2+2+2=6 | 标准完成 | 已有覆盖：MODEL-LONG-CONTEXT [章节](../../../../books/part-02-model/22-long-context.md) |
| [2605.22939 Learnability-Informed Fine-Tuning of Diffusion Language Models](https://arxiv.org/abs/2605.22939) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；Diffusion LM 的 SFT 不应在所有 timestep 同等学习所有 token；LIFT 按 token learnability 将易/难 token 分配到不同 mask/context regime。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在：TRAIN-SFT [章节](../../../../books/part-04-training-system/29-sft.md) |
| [2605.22940 Human-Centered Learning Mechanics: A Dynamical Framework for Entropy-Regulated Representation Learning](https://arxiv.org/abs/2605.22940) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose Human-Centered Learning Mechanics (HCLM), a dynamical and information-theoretic framework for open and controlled learning systems.；2+2+2=6 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [章节](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [2605.22963 Graph Alignment Topology as an Inductive Bias for Grounding Detection](https://arxiv.org/abs/2605.22963) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Large Language Models (LLMs) are optimized to produce distributionally plausible continuations rather than to explicitly verify whether generated propositions are entailed by source documents.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.22964 Certification from Examples is Hard for Circuits and Transformers under Minimal Overparametrization](https://arxiv.org/abs/2605.22964) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；有限样例通过不能升级成精确算法证书；对受限 threshold-circuit/log-precision Transformer 类，exact certification 仍可能需要指数证据。；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.22972 A mathematical theory of balancing relational generalization and memorization](https://arxiv.org/abs/2605.22972) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To address this gap, we introduce a novel task, transitive inference with exceptions, that tests for relational generalization and memorization of an exception to the relational rule.；2+2+2=6 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [章节](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [2605.22976 LLM Code Smells: A Taxonomy and Detection Approach](https://arxiv.org/abs/2605.22976) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Our results show that LLM code smells affect 73.5% of the analyzed systems, with a detection precision of 91.3% and a recall of 71.8%.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.22981 Memorization Dynamics of Fill-in-the-Middle Pretraining](https://arxiv.org/abs/2605.22981) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；fill-in-the-middle objective 与重复片段共同改变 memorization surface，必须按 corruption/objective、重复次数和 extraction probe 区分记忆风险。；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md) |
| [2605.22984 Test-Time Training Undermines Safety Guardrails](https://arxiv.org/abs/2605.22984) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.22986 Robots That Know What to Ask: Recovering Misaligned Rewards through Targeted Explanations](https://arxiv.org/abs/2605.22986) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose a framework that detects such underspecified features and actively solicits targeted corrective demonstrations.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [2605.22996 CoMoGen: COntrollable MOtion Dynamics and Interactions with Mask-Guided Video GENeration](https://arxiv.org/abs/2605.22996) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We present CoMoGen, a controllable video generation framework that generates realistic interactive dynamics from a single binary mask sequence conditioned on an input image.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23017 Smoothed Elicitation Complexity for Approximate $Γ$-calibration of Discrete Classification Tasks](https://arxiv.org/abs/2605.23017) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Along the way, we characterize the Lipschitz elicitation complexity of strongly orderable discrete properties by constructing algorithms for designing these Lipschitz properties, which we prove can be post-processed to obtain the original discrete property.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23019 PACE: Two-Timescale Self-Evolution for Small Language Model Agents](https://arxiv.org/abs/2605.23019) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：AGENT-PLATFORM [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [2605.23023 How to Steer Your Multi-Agent System: Human-LLM Collaborative Planning](https://arxiv.org/abs/2605.23023) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；human–LLM co-planning 应把 proposal、critique、selection 与 final commit authority 分开，而不是让对话流畅度代理计划质量。；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-PLANNING [章节](../../../../books/part-07-agent/79-planning.md) |
| [2605.23024 The Deterministic Horizon: Impossibility Results as Design Specifications for Trustworthy AI Systems](https://arxiv.org/abs/2605.23024) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Large language models now write software, draft legal documents, and produce clinical notes, yet fundamental limits, from Turing and Arrow to the No Free Lunch theorems, shape what computation can do.；2+2+2=6 | 标准完成 | 仅报告：MODEL-DECODER-ONLY [章节](../../../../books/part-02-model/18-decoder-only.md) |
| [2605.23028 RADAR: Relative Angular Divergence Across Representations](https://arxiv.org/abs/2605.23028) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose RADAR, a simple, geometrically grounded metric for estimating cross-domain transferability in foundation models.；2+2+2=6 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [章节](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [2605.23032 Brain-LLM Alignment Tracks Training Data, Not Typology](https://arxiv.org/abs/2605.23032) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Brain-LLM alignment is well established in English, yet the brain's language network is neuroanatomically universal across languages.；2+2+2=6 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [章节](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [2605.23033 Uncovering the Latent Potential of Deep Intermediate Representations](https://arxiv.org/abs/2605.23033) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Contrary to the widespread practice of using only the final layer or shallow mixtures, we show that task-relevant information is distributed non-monotonically across layers and cannot be recovered by naïve aggregation.；3+2+2=7 | 深入完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [章节](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [2605.23035 Sparse Autoencoders Map Brain-LLM Alignment onto Cortical Semantic Topography](https://arxiv.org/abs/2605.23035) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Intermediate layers of large language models (LLMs) best predict human brain responses to language, one of the most robust findings in computational neurolinguistics, yet why remains mechanistically unexplained.；2+2+2=6 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [章节](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [2605.23036 Multilingual Steering by Design: Multilingual Sparse Autoencoders and Principled Layer Selection](https://arxiv.org/abs/2605.23036) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：First, we show that training SAEs on multilingual data consistently strengthens cross-lingual representations and yields more reliable, quality-preserving language control across layers and model families.；2+2+2=6 | 标准完成 | 已有覆盖：MODEL-SELF-ATTENTION [章节](../../../../books/part-02-model/14-self-attention.md) |
| [2605.23039 Do Language Models Know What Not to Say? Causal Evidence for Statistical Preemption in LLMs](https://arxiv.org/abs/2605.23039) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We present a computational study that, for the first time, directly dissociates statistical preemption from the competing entrenchment hypothesis in large language models within a single converging design.；2+2+2=6 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [章节](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [2605.23040 Steered Generation via Gradient-Based Optimization on Sparse Query Features](https://arxiv.org/abs/2605.23040) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；从 query-conditioned sparse features 中优化小规模干预方向，可把全局 steering vector 改成输入相关控制，但需要独立因果与任务回归 Gate。；2+2+2=6 | 标准完成 | 结构候选 |
| [2605.23043 HawkesLLM: Semantic Uncertainty Propagation in Agentic Text Simulation](https://arxiv.org/abs/2605.23043) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：This paper studies this problem with HawkesLLM, a framework that separates temporal influence modeling from text generation.；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-MEMORY [章节](../../../../books/part-07-agent/77-memory.md) |
| [2605.23054 Model Collapse as Cultural Evolution](https://arxiv.org/abs/2605.23054) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；recursive synthetic training 的漂移可呈非单调 cultural-attractor dynamics，不能只用单代质量或单一 supplier share 解释 model collapse。；3+2+2=7 | 深入完成 | 已有覆盖：TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md) |
| [2605.23058 A measurement substrate for agentic Kubernetes operations: Methodology and a case study in retrieval-compounding falsification](https://arxiv.org/abs/2605.23058) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23061 Anytime Training with Schedule-Free Spectral Optimization](https://arxiv.org/abs/2605.23061) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；schedule-free matrix optimizer 的 averaging、spectral update 与 weight decay 必须作为同一 state transition 验收，而非把 horizon-free 当作无状态。；2+3+2=7 | 深入完成 | 已有覆盖：TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [2605.23065 Dithering Defense: Adversarial Robustness of Vision Foundation Models via Multi-Level Floyd-Steinberg Dithering](https://arxiv.org/abs/2605.23065) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We study multi-level Floyd-Steinberg error-diffusion dithering as a lightweight, model-agnostic input transformation that disrupts adversarial perturbations while preserving semantic content.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.23067 What Training Data Teaches RL Memory Agents: An Empirical Study of Curriculum Effects in Memory-Augmented QA](https://arxiv.org/abs/2605.23067) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 已有覆盖：TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md) |
| [2605.23069 DFKI-MLT at SemEval-2026 TASK 7: Steering Multilingual Models Towards Cultural Knowledge](https://arxiv.org/abs/2605.23069) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We present the DFKI-MLT system for SemEval-2026 Task 7 on cultural awareness, where we apply activation steering to multilingual LLMs using language vectors extracted from parallel FLORES data.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23070 Flow Mismatching: Unsupervised Anomaly Detection via Velocity Discrepancies in Flow Matching Models](https://arxiv.org/abs/2605.23070) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose Flow Mismatching, an unsupervised anomaly detection method that deliberately avoids reconstruction-based paradigms.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23074 PathCal: State-Aware Reflection-Marker Calibration for Efficient Reasoning](https://arxiv.org/abs/2605.23074) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；把 wait/but/alternatively 等 reflection marker 分型，只在局部不确定、竞争分支证据过强时软调 logits，而非全程固定抑制。；3+2+2=7 | 深入完成 | 整合：当前正文 binding 已存在：INFER-DECODE [章节](../../../../books/part-05-inference-system/44-decode.md) |
| [2605.23078 GEMQ: Global Expert-Level Mixed-Precision Quantization for MoE LLMs](https://arxiv.org/abs/2605.23078) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：INFER-TENSORRT-LLM [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [2605.23081 ThriftAttention: Selective Mixed Precision for Long-Context FP4 Attention](https://arxiv.org/abs/2605.23081) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；保留完整低精度 attention/KV 路径，只为 query-dependent 少量重要 blocks 晋升精度；selector 与 paired-cache identity 必须一致。；3+3+2=8 | 深入完成 | 已有覆盖：INFER-KV-CACHE [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [2605.23087 The Implicit Bias of Depth: From Neural Collapse to Softmax Codes](https://arxiv.org/abs/2605.23087) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We study the deep unconstrained feature model (UFM)-equivalent to a deep linear network with orthogonal inputs-trained without regularization, to isolate how gradient descent and depth alone shape NC.；2+2+2=6 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [章节](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [2605.23089 Dreaming Smoothly and Sample Efficiently with Gradient Penalized Latent Dynamics](https://arxiv.org/abs/2605.23089) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose GPLD, a gradient-penalized latent dynamics regularizer for DreamerV3 that applies a row-wise Jacobian penalty to the posterior latent distribution to encourage locally smooth transition learning.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [2605.23091 Security of LLM-generated Code: A Comparative Analysis](https://arxiv.org/abs/2605.23091) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We empirically evaluate the security of code generated by seven popular LLMs.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.23099 SVR-MAD: A Bayesian-Inspired Framework for Posterior-Guided Multi-Agent Debate](https://arxiv.org/abs/2605.23099) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；把 pre-debate confidence 当 prior、peer challenge outcome 当 posterior-style evidence，增量构造只保留高价值通信的 debate graph。；3+3+2=8 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [2605.23108 Philosophical Dispositions as Behavioral Constraints for AI-Assisted Code Review: An Empirical Study](https://arxiv.org/abs/2605.23108) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We present a system that constrains AI reviewer behavior through philosophical dispositions -- coherent personality lenses grounded in specific epistemological traditions (Pyrrhonist Skepticism, Navya-Ny=aya logic, Diogenes' Cynicism, Confucian relational ethics) that direct attention to structurally different types of issues.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23109 Inductive Deductive Synthesis: Enabling AI to Generate Formally Verified Systems](https://arxiv.org/abs/2605.23109) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；把 LLM synthesis proposal 与 Rocq specification/proof kernel 交替执行，只有独立 checker 能把候选升级为 verified artifact。；3+3+2=8 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING [章节](../../../../books/part-07-agent/78-tool-calling.md) |
| [2605.23113 Inconsistency-aware Multimodal Schrödinger Bridge for Deepfake Localization](https://arxiv.org/abs/2605.23113) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We present IaMSB, an inconsistency-aware multimodal Schrödinger Bridge (SB) that jointly estimates cross-modal consistency and performs interval-level localization.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23116 CoReVAD: A Contextual Reasoning Framework for Training-Free Video Anomaly Detection](https://arxiv.org/abs/2605.23116) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To address these challenges, we propose CoReVAD, a contextual reasoning framework for training-free video anomaly detection that operates with a single frozen VLM.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23141 VisAnalog: A Diagnostic Suite for Visual Concept Transfer on Natural Images](https://arxiv.org/abs/2605.23141) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We introduce VisAnalog, a controlled suite for this setting on natural images.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23147 As X, Do Y: How Persona and Task Combine in Instruction-Tuned LLMs](https://arxiv.org/abs/2605.23147) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；persona 与 task 在局部 residual site 上近似可加，不推出 persona prompt 可被单一 activation 或短 prefix 压缩；功能状态可能跨 token、层与 KV 分布。；3+2+2=7 | 深入完成 | 已有覆盖：MODEL-SELF-ATTENTION [章节](../../../../books/part-02-model/14-self-attention.md) |
| [2605.23156 Any-Dimensional Invariant Universality](https://arxiv.org/abs/2605.23156) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We develop a systematic approach to establish any-dimensional universality, by identifying any-dimensional functions with a unique function taking inputs in a suitable infinite-dimensional limit space containing inputs of all finite sizes as well as their limits.；2+2+2=6 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [章节](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [2605.23157 Same Model, Different Weakness: How Language and Modality Reshape the Jailbreak Attack Surface in Frontier MLLMs](https://arxiv.org/abs/2605.23157) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.23158 What Does the Server See? Understanding Privacy Leakage from Large Language Models in Split Inference](https://arxiv.org/abs/2605.23158) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.23168 PoisonForge: Task-Level Targeted Poisoning Benchmark for Instruction-Tuned LLMs](https://arxiv.org/abs/2605.23168) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 已有覆盖：TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md) |
| [2605.23170 Positional Failures in Long-Context LLMs: A Blind Spot in Reasoning Benchmarks](https://arxiv.org/abs/2605.23170) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23171 Understanding and Improving Noisy Embedding Techniques in Instruction Finetuning](https://arxiv.org/abs/2605.23171) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；用对称 embedding noise 更严格地正则局部曲率，把 instruction tuning 的 noise distribution 作为可版本化训练状态，而不是只记录 noise norm。；2+2+2=6 | 深入完成 | 整合：当前正文 binding 已存在：TRAIN-SFT [章节](../../../../books/part-04-training-system/29-sft.md) |
| [2605.23175 Robust LLM Watermarking with Minimal Semantic Distortion for IP Protection](https://arxiv.org/abs/2605.23175) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；水印身份绑定 provider/user key：generation 用 key-conditioned synonym tournament 保留实体，detector 联合编码 text+key，以 provider-specific verification 替代全局无主 watermark。；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.23178 Composing People Together: Iterative Pose-Image Generation for Multi-Person Interaction Scenes](https://arxiv.org/abs/2605.23178) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Despite recent progress, text-to-image models still struggle to generate semantically diverse and compositionally accurate multi-person interaction scenes, often collapsing to repetitive layouts, stereotypical poses, and poorly grounded interactions.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23179 Redrawing the AI Map: A Theory of Accountability Boundaries in Agentic Ecosystems](https://arxiv.org/abs/2605.23179) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We develop a capability-level theory of accountability-boundary placement in agentic ecosystems.；2+2+2=6 | 标准完成 | 仅报告：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23180 Self-Improving In-Context Learning](https://arxiv.org/abs/2605.23180) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；用单次 forward 得到的 demonstration-output likelihood 构造 bounded self-supervised proxy，再以 zeroth-order optimization 更新固定 few-shot prompt embeddings。；3+2+2=7 | 深入完成 | 整合：当前正文 binding 已存在：AGENT-PROMPT [章节](../../../../books/part-07-agent/74-prompt.md) |
| [2605.23187 IntentionNav: A Benchmark for Intent-Driven Object Navigation from Implicit Human Instruction](https://arxiv.org/abs/2605.23187) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We study this setting as intent-driven object navigation and introduce IntentionNav, a diagnostic benchmark for active object search from implicit human instructions.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23189 Empirical Bayes Conformal Prediction for Vision and Language Models](https://arxiv.org/abs/2605.23189) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；把重复 score 的均值与方差通过 empirical-Bayes r-value 写入 conformal nonconformity，在保持声明 coverage 的同时降低高方差伪候选。；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23190 Hidden Human-Like Nature of Machine-Generated Texts: Theory and Detection Enhancement](https://arxiv.org/abs/2605.23190) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To this end, we first reveal the existence of such hidden human-like spans, and then theoretically analyze their impact on detection.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23196 Prompt Overflow: What the Guardrail Inspects Is Not What the Model Infers](https://arxiv.org/abs/2605.23196) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.23198 Label-Efficient Dataset Pruning via Semi-Supervised Pseudo-Labeling](https://arxiv.org/abs/2605.23198) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose SemiPrune, a label-efficient dataset pruning framework, using only a small randomly labeled subset, that uses semi-supervised learning to generate pseudo-labels for unlabeled data, allowing existing supervised pruning methods that require label information to be seamlessly applied to the resulting pseudo-labeled training pool.；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md) |
| [2605.23200 Adaptive Mass-Segmented KV Compression for Long-Context Reasoning](https://arxiv.org/abs/2605.23200) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 已有覆盖：INFER-KV-CACHE [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [2605.23201 MixFake: Benchmarking and Enhancing Audio Deepfake Detection in Diverse Real-world Mixed Audio](https://arxiv.org/abs/2605.23201) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：In this paper, we first introduce MixFake, a large-scale benchmark dataset designed to simulate diverse acoustic environments with varying SNR levels and mixed authenticity components.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23203 Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We present a formal verification approach that targets robustness against 3D motion perturbations of the capturing camera.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23215 FastKernels: Benchmarking GPU Kernel Generation in Production](https://arxiv.org/abs/2605.23215) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23218 Foundation Protocol: A Coordination Layer for Agentic Society](https://arxiv.org/abs/2605.23218) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [2605.23220 WMAttack: Automated Attack Search for Adversarial Evaluation of World-Model Agents](https://arxiv.org/abs/2605.23220) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [2605.23226 MASQ: Accelerating Masked Diffusion via Stage-Wise Multi-Precision Quantization](https://arxiv.org/abs/2605.23226) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；masked diffusion 按 spatial/semantic importance 与 timestep 分配 MXINT8/4/2，并让 mask manager、non-matrix ops 和 multi-precision engine 共享执行计划。；3+3+2=8 | 深入完成 | 结构候选 |
| [2605.23238 GENSTRAT: Toward a Science of Strategic Reasoning in Large Language Models](https://arxiv.org/abs/2605.23238) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We introduce GENSTRAT, which uses procedurally generated strategic environments to address these challenges.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23244 Convex Optimization for Alignment and Preference Learning on a Single GPU](https://arxiv.org/abs/2605.23244) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；用两层 ReLU convex reformulation 与 CRONOS/ADMM 训练 reference-free preference policy，将 reference forward 与大规模超参搜索换成受限凸表达。；3+2+2=7 | 深入完成 | 整合：当前正文 binding 已存在：TRAIN-DPO [章节](../../../../books/part-04-training-system/34-dpo.md) |
| [2605.23245 SimInsert: Seamless Video Object Insertion via Regional Sparse Attention Fusion](https://arxiv.org/abs/2605.23245) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To bridge this gap, we present \textit{SimInsert}, a training-free paradigm that efficiently decouples the task into intuitive single-frame editing and semantic motion description.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23249 Enhancing Deep Neural Network Reliability with Refinement and Calibration](https://arxiv.org/abs/2605.23249) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To address this limitation, we propose: (1) a novel loss function that explicitly promotes refinement and can be optimized through supervised contrastive learning; and (2) a unified training framework, RefCal, that jointly optimizes calibration, refinement, and accuracy to improve DNN reliability.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23254 CARE: Class-Adaptive Expert Consensus for Reliable Learning with Long-Tailed Noisy Labels](https://arxiv.org/abs/2605.23254) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To address this issue, we propose Class-Adaptive Rectification with Experts (CARE), a parameter-efficient framework that leverages three complementary supervision sources from vision-language models (VLM): observed noisy labels, VLM text embeddings, and visual features.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2605.23257 Turning Adaptation into Assets: Cross-Domain Bridging for Online Vision-Language Navigation](https://arxiv.org/abs/2605.23257) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To overcome these issues, we propose Inter-Domain BridgE with Historical Assets (IDEA), a novel TTA framework that transforms adaptation into the accumulation and composition of assets.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [2605.23258 A Simple Plug-in for Improving Eviction-Based KV Cache Compression](https://arxiv.org/abs/2605.23258) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；2+2+3=7 | 深入完成 | 已有覆盖：INFER-KV-CACHE [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [2605.23259 Multi-Gate Residuals](https://arxiv.org/abs/2605.23259) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；用 multi-stream context、轻量 gating 与 attention pooling 稳定深层 residual activation，在不增加跨设备 attention-residual 通信的条件下提供可训练多路残差状态。；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：MODEL-TRANSFORMER-LAYER [章节](../../../../books/part-02-model/17-transformer-layer.md) |
| [2605.23261 UniSRM: A Unified Speech Reward Model for Reasoning-Based Fine-grained Assessment](https://arxiv.org/abs/2605.23261) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：In this work, we propose UniSRM, a unified speech reward model that can support multi-dimensional, interpretable reward signals with reliable reasoning.；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md) |
| [2605.23270 ChainFlow-VLA: Causal Flow Planning with Vision-Language Models](https://arxiv.org/abs/2605.23270) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To address this, we propose ChainFlow-VLA, which unifies causal generation and global refinement within a unified probabilistic framework.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [2605.23271 EvalVerse: Pipeline-Aware and Expert-Calibrated Benchmarking for Professional Cinematic Video Generation](https://arxiv.org/abs/2605.23271) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To bridge this gap, we introduce EvalVerse, a comprehensive, pipeline-aware, and expert-calibrated evaluation framework.；3+2+2=7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23275 Diffusion Domain Expansion: Learning to Coordinate Pre-trained Diffusion Models](https://arxiv.org/abs/2605.23275) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：In this paper, we propose Diffusion Domain Expansion (DDE), a method that efficiently extends pre-trained diffusion models to generate larger objects and handle more complex conditioning beyond their original capabilities.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23281 DepthAgent: Towards Better Universal Depth Estimation via Sample-wise Expert Selection](https://arxiv.org/abs/2605.23281) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：In this paper, we show that depth experts exhibit strong sample-wise complementarity: model preference is highly correlated with camera geometry, and multi-model fusion brings the largest gains on difficult samples where individual experts are unreliable.；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING [章节](../../../../books/part-07-agent/78-tool-calling.md) |
| [2605.23287 LangFlash: Feed-forward 3D Language Gaussian Splatting from Sparse Unposed Images](https://arxiv.org/abs/2605.23287) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We present LangFlash, a feed-forward framework for 3D Language Gaussian Splatting that reconstructs 3D scenes parameterized by Gaussian primitives enriched with language-aligned semantic features from sparse unposed multi-view images.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23288 Spatio-Temporal Similarity Volume Aggregation for Open-Vocabulary Action Recognition](https://arxiv.org/abs/2605.23288) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose Similarity Volume Aggregation (SimVA), a framework that constructs a dense 4D spatio-temporal similarity volume from patch-level visual-text similarities.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2605.23294 NASiC: 3D NAND-based CAM-Selected Multibit CIM Architecture for Efficient On-Device Mixture-of-Experts LLM Inference](https://arxiv.org/abs/2605.23294) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [2605.23296 Parallel Context Compaction for Long-Horizon LLM Agent Serving](https://arxiv.org/abs/2605.23296) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：AGENT-CONTEXT [章节](../../../../books/part-07-agent/75-context.md) |
| [2605.23297 Ontological Knowledge Blocks: Executable Compliance and Profile-Based Validation for Trustworthy AI Systems](https://arxiv.org/abs/2605.23297) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：This paper introduces Ontological Knowledge Blocks (OKBs), a programmable governance infrastructure that compiles regulatory obligations into machine-checkable constraints over structured evidence graphs.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.23311 DART: Semantic Recoverability for Structured Tool Agents](https://arxiv.org/abs/2605.23311) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING [章节](../../../../books/part-07-agent/78-tool-calling.md) |
| [2605.23315 Convergence Without Understanding: When Language Models Agree on Representations but Disagree on Reasoning](https://arxiv.org/abs/2605.23315) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；跨模型 CKA/transfer probe 的表示收敛可与 generation-stage divergence、低 causal flip rate 同时出现；可解码共享信息不等于共享 reasoning mechanism。；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23330 Security, Privacy, and Ethical Risks in OpenClaw](https://arxiv.org/abs/2605.23330) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：This paper systematically investigates the security, privacy, and ethical risks, as well as the traceability challenges of OpenClaw, a locally executable AI agent system for natural language interaction and real-world task completion.；2+2+2=6 | 标准完成 | 仅报告：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23341 Sparse Compositional Flow Matching by geometric assembly from motion primitives](https://arxiv.org/abs/2605.23341) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Embodied trajectories, such as the executable motion sequences of robotic manipulators, underwater vehicles, and mobile robots, are a fundamental output of embodied AI.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23344 CHASD: Language Increment-Calibrated Contrastive Decoding against Hallucination in LVLMs](https://arxiv.org/abs/2605.23344) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；只在 next-token 低置信时开启负视觉分支，并按当前 attention salient tokens 做局部扰动，使 contrastive hallucination calibration 成为按 token 条件计算。；2+2+2=6 | 深入完成 | 整合：当前正文 binding 已存在：MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2605.23346 Contrastive Distribution Matching for Amortized Sequential Monte Carlo in Discrete Diffusion](https://arxiv.org/abs/2605.23346) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To overcome this limitation, we introduce Contrastive Distribution Matching (CDM), a novel framework that amortizes the cost of SMC inference by learning a parameterized twist function via positive and negative samples.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23351 Prudent-Banker: No Extra Fees for Baseline Safety in Adversarial Bandits With and Without Delays](https://arxiv.org/abs/2605.23351) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We study adversarial multi-armed bandits with and without delayed feedback under a safety-aware goal: achieving minimax-optimal worst-case regret while keeping nearly constant regret relative to a designated "safe" baseline policy.；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md) |
| [2605.23362 Instance-Optimal Estimation with Multiple LLM Judges on a Budget](https://arxiv.org/abs/2605.23362) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23365 Score-Based One-step MeanFlow Policy Optimization](https://arxiv.org/abs/2605.23365) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose Score-Based One-step MeanFlow Policy Optimization (SOM), an actor-critic algorithm that resolves this by constructing the target velocity field directly from the Q-function via score estimation and a probability flow ODE, thereby concentrating probability mass on high-value modes.；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-PPO [章节](../../../../books/part-04-training-system/32-ppo.md) |
| [2605.23372 Curriculum reinforcement learning with measurable task representation learning](https://arxiv.org/abs/2605.23372) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To achieve automatic curriculum generation in complex task, we propose a novel automatic curriculum generation approach based on measurable task representation learning.；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-PPO [章节](../../../../books/part-04-training-system/32-ppo.md) |
| [2605.23373 AffectCodec: Emotion-Preserving Neural Speech Codec with Block-Diagonal Residual FSQ](https://arxiv.org/abs/2605.23373) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose AffectCodec, an emotion-preserving neural speech codec built on Block-Diagonal Residual Finite Scalar Quantization (BD-RFSQ).；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2605.23381 VDE: Training-Free Accelerating Rectified Flow Model via Velocity Decomposition and Estimation](https://arxiv.org/abs/2605.23381) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；把 rectified-flow acceleration 从静态 feature cache 改为对 velocity 的平行/正交分量做 input-adaptive estimation，并以周期 full-forward anchor 限制累计误差。；3+2+2=7 | 深入完成 | 整合：当前正文 binding 已存在：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23382 From Correctness to Preference: A Framework for Personalized Agentic Reinforcement Learning](https://arxiv.org/abs/2605.23382) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；把 generic task reward 与 personalized preference reward 分离，以 user-specific anchor 校准 advantage，并把可复用 skill 组织为 preference-aligned graph memory。；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md) |
| [2605.23384 Metacognition as Reward: Reinforcing LLM Reasoning via Knowledge and Regulation Signals](https://arxiv.org/abs/2605.23384) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；以 metacognitive knowledge 与 regulation 两类 process channel 对 reasoning trajectory 评分，并与终态正确性联合优化。；3+2+2=7 | 深入完成 | 已有覆盖：TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md) |
| [2605.23389 AlignedServe: Orchestrating Prefix-aware Batching to Build a High-throughput and Computing-efficient LLM Serving System](https://arxiv.org/abs/2605.23389) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：INFER-SCHEDULING [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [2605.23398 TPMM-DPO: Trajectory-aware Preference-guided Model Merging for Iterative Direct Preference Optimization](https://arxiv.org/abs/2605.23398) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；把 iterative DPO 的 policy snapshots 视为带 lineage 的优化轨迹，用 preference-guided learned weights 构造 reference，减少单一上一轮 reference 的噪声累积。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在：TRAIN-DPO [章节](../../../../books/part-04-training-system/34-dpo.md) |
| [2605.23410 What Linear Probes Miss: Multi-View Probing for Weight-Space Learning](https://arxiv.org/abs/2605.23410) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To bridge this gap, we introduce MVProbe, a multi-perspective probing framework that synthesizes first-order signals with interaction-aware (Gram-based) views.；2+2+2=6 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [章节](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [2605.23411 Sample-wise Targeted Adversarial Attacks on Test-time Adaptation](https://arxiv.org/abs/2605.23411) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To capture a more realistic threat, we introduce a sample-wise targeted attack.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.23414 When Planning Fails Despite Correct Execution: On Epistemic Calibration for LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2605.23414) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [2605.23420 Naturalistic measure of social norms alignment](https://arxiv.org/abs/2605.23420) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose a framework for measuring social norm alignment in naturalistic, free-form settings through solution matching.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23424 Sparse In-Network Learning via Shortest-Path Backpropagation and Finite-Rate Gating](https://arxiv.org/abs/2605.23424) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：In-network learning (INL) trains distributed neural modules by exchanging latent activations and backpropagated errors over a communication graph.；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [2605.23426 Socially fluent AI decouples conversational signals from source identity in online interaction](https://arxiv.org/abs/2605.23426) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Socially fluent agentic AI can now participate in online interaction in ways that resemble ordinary human conversation, potentially weakening people's ability to infer who is human from conversational signals alone.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23445 DFSAttn: Dynamic Fine-grained Sparse Attention for Efficient Video Generation](https://arxiv.org/abs/2605.23445) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：In this paper, we revisit block sparse attention and derive a theoretical lower bound on attention recall to characterize the key factors governing its effectiveness.；3+2+2=7 | 深入完成 | 已有覆盖：MODEL-SELF-ATTENTION [章节](../../../../books/part-02-model/14-self-attention.md) |
| [2605.23446 Weisfeiler-Leman Is Incomplete on Simple Spectrum Graphs, so Canonicalize Them](https://arxiv.org/abs/2605.23446) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Graphs with a simple spectrum admit cubic-time isomorphism testing, yet we prove that for every natural number $k$, the $k$-Weisfeiler-Leman ($k$-WL) test cannot distinguish all non-isomorphic graphs with a simple spectrum.；2+2+2=6 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [章节](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [2605.23449 Commutator-Induced Uncertainty in VAEs](https://arxiv.org/abs/2605.23449) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We introduce a Lie Group VAE framework that combines geometric and algebraic perspectives on uncertainty while separating discrete generative factors from continuous geometric transformations.；2+2+2=6 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [章节](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [2605.23451 Efficient One-Step Diffusion Restoration Model with Compact Token Compression and Linear Attention](https://arxiv.org/abs/2605.23451) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Motivated by this observation, we revisit Real-ISR from the perspectives of compact latent representation and linear-complexity modeling, and propose SANA-SR, an efficient one-step restoration framework.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23458 One-Forcing: Towards Stable One-Step Autoregressive Video Generation](https://arxiv.org/abs/2605.23458) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；以 DMD objective 加 auxiliary GAN loss 稳定 one-step autoregressive video student，并比较 framewise/chunkwise training。；3+2+2=7 | 深入完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23463 StepAudio 2.5 Technical Report](https://arxiv.org/abs/2605.23463) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；统一 audio backbone 仍需把语义 token、acoustic detail、task-specific RLHF 与 streaming decode state 分责，ASR multi-token prediction 只是受限训练分支。；3+3+2=8 | 深入完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2605.23464 Unextractable Protocol Models: Collaborative Training and Inference without Weight Materialization](https://arxiv.org/abs/2605.23464) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.23467 S$^3$GNN: Efficient Global Mixing and Local Message Passing for Long-Range Graph Learning](https://arxiv.org/abs/2605.23467) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We revisit these conclusions and show that the associated Jacobian sensitivity lower bound is generally difficult to achieve in practice.；2+2+2=6 | 标准完成 | 已有覆盖：MODEL-SELF-ATTENTION [章节](../../../../books/part-02-model/14-self-attention.md) |
| [2605.23472 Rethinking Transfer Learning for Industrial Inspection: DINOv3 vs. ImageNet Pretraining Across RGB and X-ray Tasks](https://arxiv.org/abs/2605.23472) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We evaluate semantic segmentation, instance segmentation, and object detection across four downstream datasets spanning RGB surface-defect inspection and X-ray defect detection.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23476 Non-normal spectral signatures of instability in neural network training dynamics](https://arxiv.org/abs/2605.23476) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；optimizer update matrix 非 normal 时，eigenvalue/spectral-radius 稳定并不控制瞬态放大；应把 eigenvector conditioning/pseudospectral sensitivity 作为诊断而非自动控制权。；3+2+2=7 | 深入完成 | 整合：当前正文 binding 已存在：TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [2605.23477 Semantically Structured Mixture-of-Experts for Compositional Robotic Manipulation](https://arxiv.org/abs/2605.23477) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We introduce Semantically Structured Mixture-of-Experts Diffusion Policy (SMoDP) for compositional robotic manipulation, a framework that grounds expert specialization in semantic task structure.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [2605.23482 Multimodal Distribution Matching for Vision-Language Dataset Distillation](https://arxiv.org/abs/2605.23482) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To address this, we present Multimodal Distribution Matching (MDM), a geometry-aware framework for efficient and generalizable multimodal distillation.；3+2+2=7 | 深入完成 | 整合：当前正文 binding 已存在：TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md) |
| [2605.23493 EDGE-OPD: Internalizing Privileged Context with Evidence Guided On-Policy Distillation](https://arxiv.org/abs/2605.23493) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 已有覆盖：TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md) |
| [2605.23497 Asking For An Old Friend: Diagnosing and Mitigating Temporal Failure Modes in LLM-based Statutory Question Answering](https://arxiv.org/abs/2605.23497) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；RAG 必须把 fact date 与 document validity interval 作为 hard filter，分别防止 post-cutoff staleness 与对历史问题的 recency bias。；2+2+3=7 | 深入完成 | 整合：当前正文 binding 已存在：AGENT-RAG [章节](../../../../books/part-07-agent/76-rag.md) |
| [2605.23508 DrawVideo: Generating Long Video from Storyboard Keyframe Sketches](https://arxiv.org/abs/2605.23508) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose DrawVideo, a sketch-guided, storyboard-driven framework for controllable long-video generation.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23522 Precise: SDE-Consistent Stochastic Sampling for RL Post-Training of Flow-Matching Models](https://arxiv.org/abs/2605.23522) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；flow-model RL 的 stochastic sampler 本身属于 policy identity：exploration SDE schedule 与小步数离散化必须共同保持 denoising consistency。；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23551 Goal-Conditioned Agents that Learn Everything All at Once](https://arxiv.org/abs/2605.23551) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We show that this approach significantly outperforms other methods on goal-conditioned Craftax and is competitive with existing baselines on continuous control environments, while achieving a &gt;250x speed-up compared to all-goals relabelling.；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-PPO [章节](../../../../books/part-04-training-system/32-ppo.md) |
| [2605.23556 Is Dimensionality a Barrier for Retrieval Models?](https://arxiv.org/abs/2605.23556) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；理论给出 sparse relevance matrix 下达到 maximal margin 所需的 embedding dimension 上下界，并说明 sigmoid loss 在 free-embedding experiment 中的 margin 优势。；3+2+3=8 | 深入完成 | 仅报告：MODEL-EMBEDDING [章节](../../../../books/part-02-model/12-embedding.md) |
| [2605.23562 ARMS: Automatic Reward Shaping for Sparse-Reward Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.23562) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose Automatic Reward-shaping in Multi-agent Systems (ARMS), a self-supervised reward shaping framework for MARL that learns dense shaping signals from sparse environmental rewards through trajectory ranking.；3+2+2=7 | 深入完成 | 整合：当前正文 binding 已存在：AGENT-MULTI-AGENT [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [2605.23563 MARS: Magnitude-Aware Rank Statistics](https://arxiv.org/abs/2605.23563) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：In order to address this issue, we propose Magnitude-Aware Rank Statistics (MARS) that incorporates a relative margin coefficient as a weight for the discrete ranks.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23565 Understanding Goal Generalisation in Sequential Reinforcement Learning](https://arxiv.org/abs/2605.23565) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We study over 100 sequential training pipelines, evaluating behaviour across over 250 out-of-distribution environments.；3+2+2=7 | 深入完成 | 整合：当前正文 binding 已存在：TRAIN-PPO [章节](../../../../books/part-04-training-system/32-ppo.md) |
| [2605.23572 HARNESS-LM: A Three-Phase Training Recipe for Harnessing SLMs in Sponsored Search Retrieval](https://arxiv.org/abs/2605.23572) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：In this paper, we present HARNESS-LM (HLM), a three-phase training framework for transferring the capabilities of large-scale retrievers into compact, cost-efficient models.；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [2605.23574 Push Your Agent: Measuring and Enforcing Quantitative Goal Persistence in Long-Horizon LLM Agents](https://arxiv.org/abs/2605.23574) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-WORKFLOW [章节](../../../../books/part-07-agent/81-workflow.md) |
| [2605.23591 Asymmetric Scaling Laws from Sparse Features](https://arxiv.org/abs/2605.23591) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；稀疏 rare coordinates 可让 under/over-parameterized loss 呈不对称 exponent、double descent 与偏向增加数据量的 compute frontier。；3+2+3=8 | 深入完成 | 仅报告：WORLDVIEW-SCALING-LAW [章节](../../../../books/part-01-worldview/07-scaling-law.md) |
| [2605.23598 When Youth Enter the Algorithmic Wild: Discovering and Understanding Potentially Harmful Teen Videos on Douyin and Kwai](https://arxiv.org/abs/2605.23598) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To bridge this gap, we propose PHTV-Scout, the first large-scale, behaviorally grounded measurement framework for Potentially Harmful Teen Videos (PHTVs).；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23602 GlowGS: Generative Semantic Feature Learning for 3D Gaussian Splatting in Nighttime Glow Scenes](https://arxiv.org/abs/2605.23602) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Existing 3DGS methods effectively render high-quality novel views in clear-day scenes.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2605.23603 Preisach Attention: A Hysteretic Model of Sequential Memory](https://arxiv.org/abs/2605.23603) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；以 hysteretic relay operators 替代部分 attention interaction 可获得理论表达力与复杂性结果。；3+2+3=8 | 深入完成 | 仅报告：MODEL-SELF-ATTENTION [章节](../../../../books/part-02-model/14-self-attention.md) |
| [2605.23605 DiLaDiff: Distilled Latent-Augmented Diffusion for Language Modeling](https://arxiv.org/abs/2605.23605) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；为 masked diffusion LM 增加 semantic continuous latent：autoencoder 学表示、latent diffusion 学 prior、consistency model 压到 few-step，再与 discrete decoding 组合。；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23610 EM-Vid: Training-Free Entity-Centric Memory for Efficient and Consistent Multi-Shot Video Generation](https://arxiv.org/abs/2605.23610) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；把多镜头视频 full-frame history 改成 entity-indexed latent-patch bank，并用 budgeted update、entity-only sparse attention 与 noise injection 分离身份持久状态和场景瞬态。；3+3+2=8 | 深入完成 | 整合：当前正文 binding 已存在：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23618 Benchmarking Google Embeddings 2 against Open-Source Models for Multilingual Dense Retrieval and RAG Systems](https://arxiv.org/abs/2605.23618) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Chunking experiments show that all six models saturate at 32-token chunks on our corpus, with semantic chunking providing measurable gains only at 16 tokens.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23623 Adversarial Vulnerability Under Temporal Concept Drift: A Longitudinal Study of Android Malware Detection](https://arxiv.org/abs/2605.23623) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We present a longitudinal, drift-aware evaluation of adversarial robustness across more than a decade of Android applications using static and dynamic feature representations extracted from emulator and real-device executions.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.23628 How Hard is it to Rig a Benchmark? A Social Choice Analysis of Leaderboard Robustness](https://arxiv.org/abs/2605.23628) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23629 DDX-TRACE: A Benchmark for Medical Diagnostic Trajectories in VLMs](https://arxiv.org/abs/2605.23629) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We introduce DDX-TRACE, a physician-adjudicated benchmark for multimodal neuroradiology that evaluates diagnostic trajectories under hidden evidence over 211 challenging cases.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23630 To Overlay or to Customize? Revisiting Architectural Choices in Heterogeneous Systems](https://arxiv.org/abs/2605.23630) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：In this work, we present a systematic study of this trade-off from a deployment-centric perspective, focusing on an autonomous driving scenario.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-PRODUCTION [章节](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md) |
| [2605.23634 DualMem: Bypassing the Objectness Bottleneck for Calibrated Unknown-Stream Filtering in Open-World Object Detection](https://arxiv.org/abs/2605.23634) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We find that the unknown prediction streams of strong OWOD detectors are heavily polluted: on M-OWODB, across PROB, OW-DETR, and HypOW, future-task positive unknowns make up less than 10% of unknown predictions, whereas background false positives account for 46-71%.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2605.23635 Dirichlet-Based Monte Carlo Dropout for Uncertainty Estimation in Neural Networks](https://arxiv.org/abs/2605.23635) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Traditional neural networks provide deterministic predictions without inherent uncertainty estimates.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23640 CachePrune: Privacy-Aware and Fine-Grained KV Cache Sharing for Efficient LLM Inference](https://arxiv.org/abs/2605.23640) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 已有覆盖：INFER-KV-CACHE [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [2605.23641 Kernel-Based ReLU Approximation for Homomorphic Encryption-Compatible Privacy-preserving Deep Learning Models](https://arxiv.org/abs/2605.23641) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：This paper proposes a kernel-based approximation of ReLU, enabling its use within HE-constrained settings and thus contributing a critical step toward supporting privacy-preserving LLMs.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.23643 Less Effort, Shorter Proofs: Reinforcement Learning for Security Protocol Analysis in Tamarin](https://arxiv.org/abs/2605.23643) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：In this paper, we present a reinforcement learning (RL) framework inspired by AlphaZero and AlphaProof that implements a new style of proof search for Tamarin.；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING [章节](../../../../books/part-07-agent/78-tool-calling.md) |
| [2605.23645 Learning Through Noise: Why Subliminal Learning Works and When It Fails](https://arxiv.org/abs/2605.23645) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；蒸馏无关噪声也能传递 teacher signal；关键不是相同初始化，而是 auxiliary/class output head 的兼容性与表示可恢复性。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在：TRAIN-SFT [章节](../../../../books/part-04-training-system/29-sft.md) |
| [2605.23652 One Policy, Infinite NPCs: Persona-Traceable Shared RL Policies for Scalable Game Agents](https://arxiv.org/abs/2605.23652) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We introduce pcsp (Persona Conditioned Shared Policy), a single reinforcement learning policy conditioned on frozen LLM embeddings of free-form persona descriptions.；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [2605.23655 CVSearch: Empowering Multimodal LLMs with Cognitive Visual Search for High-Resolution Image Perception](https://arxiv.org/abs/2605.23655) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To address this dilemma, we introduce CVSearch, a training-free adaptive framework that dynamically schedules search strategies via an Assess-then-Search workflow.；3+2+2=7 | 深入完成 | 已有覆盖：MODEL-SELF-ATTENTION [章节](../../../../books/part-02-model/14-self-attention.md) |
| [2605.23656 Recursive Block-Diagonal Coupling for Resource-Efficient Training of Vision Models](https://arxiv.org/abs/2605.23656) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose an efficient training protocol, RBDC, that builds wide models by coupling in a parameter-free block-diagonal way narrower, independently trained models in a recursive way.；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [2605.23672 RiGS: Rigid-aware 4D Gaussian Splatting from a Single Monocular Video](https://arxiv.org/abs/2605.23672) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：In this work, we present Rigid-aware 4D Gaussian Splatting (RiGS), which simultaneously captures motions across multiple temporal scales.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23673 Relevant Walk Search for Explaining Graph Neural Networks](https://arxiv.org/abs/2605.23673) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Specifically, we propose {\em polynomial-time} algorithms for finding top-$K$ relevant walks, which drastically reduces the computation and thus increases the applicability of GNN-LRP to large-scale problems.；2+2+2=6 | 标准完成 | 已有覆盖：MODEL-SELF-ATTENTION [章节](../../../../books/part-02-model/14-self-attention.md) |
| [2605.23684 Synthetic Sources?: Auditing Generative Search Engine Citations for Evidence of AI-Generated Sources](https://arxiv.org/abs/2605.23684) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：In a step towards identifying whether AI-generated sources are being cited by these engines, this work presents an audit of four generative search engines (ChatGPT, Copilot, Gemini, Perplexity) using a total of 712 real-world human-generated queries spanning domains of public importance: politics, health, and the environment.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23695 Validating Threat Modeling Results with the Help of Vulnerable Test Applications](https://arxiv.org/abs/2605.23695) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：This paper evaluates a complementary, vulnerability-grounded validation approach.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.23699 CRONOS: Benchmarking Counterfactual Physical Consistency in Video Models](https://arxiv.org/abs/2605.23699) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We introduce CRONOS, an intervention-based benchmark designed to evaluate counterfactual physical consistency: whether a model's predictions of physical events respond appropriately to controlled changes in the visual input, such as variations of scene context, viewpoint, object appearance, and object category.；3+2+2=7 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [2605.23702 TubiFM: Unified Item, Carousel, and Search Ranking for Streaming Discovery](https://arxiv.org/abs/2605.23702) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We introduce the user story, a serialized representation that turns a user's cross-surface history - attributes, sessions, watch events with surface and carousel context, and search events - into a single token sequence.；2+2+2=6 | 标准完成 | 已有覆盖：MODEL-DECODER-ONLY [章节](../../../../books/part-02-model/18-decoder-only.md) |
| [2605.23707 Flare: Leveraging Serverless Elasticity to Absorb Microservice Load Spikes](https://arxiv.org/abs/2605.23707) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To address the challenge of unpredictable load spikes, we propose Flare, a hybrid microservice architecture that combines VMs with serverless computing.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-PRODUCTION [章节](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md) |
| [2605.23719 Weierstrass Positional Encoding for Vision Transformers](https://arxiv.org/abs/2605.23719) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；用复平面上的 Weierstrass elliptic function/derivative 编码 2D patch coordinate，使 absolute encoding 可通过 addition formula 派生 relative position，并支持连续分辨率。；2+2+3=7 | 深入完成 | 整合：当前正文 binding 已存在：MODEL-POSITION-ENCODING [章节](../../../../books/part-02-model/13-position-encoding.md) |
| [2605.23721 Is a Document Educational or Just Wikipedia-Style? -- Pitfalls of Classifier-Based Quality Filtering](https://arxiv.org/abs/2605.23721) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；quality classifier 可被表面格式操纵，使内容质量不变时 retention 决策翻转；filter release 应包含 policy-preserving style counterfactual。；3+2+2=7 | 深入完成 | 已有覆盖：TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md) |
| [2605.23723 MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection](https://arxiv.org/abs/2605.23723) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-MEMORY [章节](../../../../books/part-07-agent/77-memory.md) |
| [2605.23726 Optimal Dimension-Free Sampling for Regularized Classification](https://arxiv.org/abs/2605.23726) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We prove optimal sampling bounds achieving $(1\pm\varepsilon)$-relative error for a broad class of Lipschitz continuous classification loss functions under various regularization terms.；2+2+2=6 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [章节](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [2605.23744 Contrast to Detect: Dynamic Graph Contrastive Regularization for Unsupervised Anomaly Detection in Multivariate Time Series](https://arxiv.org/abs/2605.23744) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose ContrastAD, an unsupervised framework that turns structural evolution itself into a learning signal rather than suppressing it.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23747 Revitalizing Dense Material Segmentation: Stabilized Vision Transformers and the Generalization Paradox](https://arxiv.org/abs/2605.23747) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We conduct an exhaustive evaluation of SegFormer and Mask2Former architectures, revealing that standard training paradigms fail on amorphous texture fields due to high-variance gradients.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23751 Approaching I/O-optimality for Approximate Attention](https://arxiv.org/abs/2605.23751) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；在特定 external-memory/I/O model 与 additive approximation error 下构造 attention 算法及 lower bound。；3+2+2=7 | 深入完成 | 仅报告：MODEL-SELF-ATTENTION [章节](../../../../books/part-02-model/14-self-attention.md) |
| [2605.23753 SeedER: Seed-and-Expand Retrieval from Knowledge Graphs](https://arxiv.org/abs/2605.23753) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；用 dense/entity seed 初始化小 core set，再由 RL graph policy 在 budget 内做局部 expansion，将 multi-hop retrieval 写成可复用的局部决策序列。；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-RAG [章节](../../../../books/part-07-agent/76-rag.md) |
| [2605.23762 Direct Dynamic Retargeting for Humanoid Imitation Learning from Videos](https://arxiv.org/abs/2605.23762) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We identify that these intermediate kinematic projections introduce a geometric bias, restricting the search space and yielding suboptimal dynamic behaviors.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [2605.23771 PhotoFlow: Agentic 3D Virtual Photography Missions](https://arxiv.org/abs/2605.23771) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We introduce PhotoFlow, a Director-Reviewer-Reflector agent for closed-loop camera search.；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-PLANNING [章节](../../../../books/part-07-agent/79-planning.md) |
| [2605.23772 Agentic Proving for Program Verification](https://arxiv.org/abs/2605.23772) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；program-verification benchmark 的自然语言题与形式规格可能不等价；必须将 specification normalization、patched versions 与 executable checker 绑定到 Evaluation Identity。；3+2+2=7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23780 Beyond Binary Edits Robust Multimodal Knowledge Editing with Adversarial Subspace Alignment](https://arxiv.org/abs/2605.23780) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；把 multimodal knowledge edit 的 generality 定义为 knowledge-unit 内一致性，用 joint-latent adversarial variants 暴露脆弱区域，再以低秩 subspace 对齐限制 edit 范围。；3+2+2=7 | 深入完成 | 结构候选 |
| [2605.23796 UniSpike: Accelerating Spiking Neural Networks on Neuromorphic Systems via Eliminating Address Redundancy](https://arxiv.org/abs/2605.23796) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：This paper presents UniSpike, a hardware-software co-design that removes address redundancy by aggregating spikes destined for the same core into compact packets.；2+2+2=6 | 标准完成 | 结构候选 |
| [2605.23797 Debiased Negative Mining Improves Out-of-distribution Detection with Pre-trained Vision-Language Models](https://arxiv.org/abs/2605.23797) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To this end, we develop a theoretical framework for correcting the sampling bias of negatives labels by indirectly approximating the distribution of negative labels.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23819 Not Too Generative, Not Too Discriminative: The Human Alignment Sweet Spot](https://arxiv.org/abs/2605.23819) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：A central question in computational vision is whether human-like visual representations are better explained by discriminative or generative learning.；2+2+2=6 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [章节](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [2605.23821 Hierarchical Concept Geometry in Language Models Emerges from Word Co-occurrence](https://arxiv.org/abs/2605.23821) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose a distributional theory of how hypernymy -- the ``is-a'' relation between general and specific concepts -- is encoded geometrically in language representations.；3+2+2=7 | 深入完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [章节](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [2605.23825 It's the humans, not the data: Geopolitical bias in LLMs originates in post-training, amplified by the language of the prompt](https://arxiv.org/abs/2605.23825) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；偏差 attribution 必须把 base 与 chat/post-trained checkpoint 成对比较，并把 prompt language 作为 evaluation slice；不能把 chat 行为静默归因给 pretraining data。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23832 SFG-ROS: A Resource-Aware Framework for Dense Multi-Agent Perception](https://arxiv.org/abs/2605.23832) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To address these bottlenecks, we present SFG-ROS, a resource-aware multi-agent software framework designed for dynamic fleet deployments.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-PRODUCTION [章节](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md) |
| [2605.23833 DORA: Dataflow-Instruction Orchestration Architecture for DNN Acceleration](https://arxiv.org/abs/2605.23833) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；用 dataflow ISA 显式控制 on-chip memory、parallelism、off-chip movement 与 synchronization，再由 MILP/heuristic 两阶段 compiler search 生成执行计划。；3+3+3=9 | 深入完成 | 结构候选 |
| [2605.23845 Learning a Particle Dynamics Model with Real-world Videos](https://arxiv.org/abs/2605.23845) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Specifically, we propose to learn a particle-based dynamics model compatible with a Gaussian splatting framework, which operates on dense particles derived from Gaussians (i.e., particles with scales and rotations) and predicts their position and rotation changes over time.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [2605.23847 Instrumentation for Imitation Learning: Enhancing Training Datasets for Clothes Hanger Insertion](https://arxiv.org/abs/2605.23847) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：In this paper, we present instrumented imitation learning of clothes hanger insertion.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [2605.23856 Point Tracking Improves World Action Models](https://arxiv.org/abs/2605.23856) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [2605.23857 Strong Teacher Not Needed? On Distillation in LLM Pretraining](https://arxiv.org/abs/2605.23857) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；teacher 的 aggregate capability 更强不保证固定 student 在固定 token/compute budget 下学得更多；teacher–student compatibility 与 target difficulty 应成为 distillation selection contract。；3+2+2=7 | 受阻 | 暂缓：TRAIN-SFT [章节](../../../../books/part-04-training-system/29-sft.md) |
| [2605.23859 Natural Yet Challenging to Detect: Robust In-the-Wild TTS through EMA and Dual-Scoring Prompt Selection -- Submission for WildSpoof 2026 TTS Track](https://arxiv.org/abs/2605.23859) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We introduce F5-TTS-DPS, a model built upon the F5-TTS architecture.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.23861 Leveraging Foundation Models for Causal Generative Modeling](https://arxiv.org/abs/2605.23861) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We introduce FM-CGM, a modular framework for end-to-end visual causal reasoning using pretrained foundation models.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23867 Human Decision-Making with Persuasive and Narrative LLM Explanations](https://arxiv.org/abs/2605.23867) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Here we conduct a large-scale human behavioral experiment to evaluate decision-making performance with LLM-generated narrative explanations of varying persuasiveness.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23868 Vision Transformers Need Better Token Interaction](https://arxiv.org/abs/2605.23868) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We revisit this dense degradation phenomenon and argue that it is not fully explained by high-norm artifacts alone.；3+2+2=7 | 深入完成 | 已有覆盖：MODEL-SELF-ATTENTION [章节](../../../../books/part-02-model/14-self-attention.md) |
| [2605.23871 Move on Muon : A Hamiltonian probability gradient flow perspective of Muon optimizer](https://arxiv.org/abs/2605.23871) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；把 regularized Muon 解释为 nuclear-norm Fenchel smoothing 下的 mirror/prox update，momentum 是 dual coordinate，并给出受假设约束的 Hamiltonian dissipation/convergence。；3+2+3=8 | 深入完成 | 已有覆盖：TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [2605.23872 Training-Free Looped Transformers](https://arxiv.org/abs/2605.23872) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；training-free looped Transformer 通过 damped substeps/RK-style refinement 改变有效深度，但必须有收敛、预算与退化 fallback。；3+2+2=7 | 深入完成 | 已有覆盖：MODEL-TRANSFORMER-LAYER [章节](../../../../books/part-02-model/17-transformer-layer.md) |
| [2605.23878 LaMo: Self-Supervised Latent Motion Priors for Physical Realism in Video Generation](https://arxiv.org/abs/2605.23878) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We propose LaMo, which formulates a latent motion prior over frame-to-frame latent changes conditioned on the current latent and prompt.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23879 On the Stability of Spherical Hellinger-Kantorovich Flows and Their Implications for Differential Privacy](https://arxiv.org/abs/2605.23879) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：In this work, we develop a perturbation theory for SHK gradient flows.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.23883 PGT: Procedurally Generated Tasks for improving visual grounding in MLLMs](https://arxiv.org/abs/2605.23883) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：In this work, we propose Procedurally Generated Tasks (PGT), a simple data-driven framework that serves a dual purpose: inducing fine-grained visual understanding and acting as a low-cost diagnostic tool to identify the source of perception failures.；3+2+2=7 | 深入完成 | 整合：当前正文 binding 已存在：TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md) |
| [2605.23885 Multilingual Knowledge Transfer under Data Constraints via Lexical Interventions](https://arxiv.org/abs/2605.23885) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；在高资源预训练语料中按 bilingual vocabulary 替换部分词项，把跨语言 transfer 从额外模型/平行语料改成可版本化 lexical intervention。；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在：TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md) |
| [2605.23887 CHRONOS: Temporally-Aware Multi-Agent Coordination for Evolving Data Marketplaces](https://arxiv.org/abs/2605.23887) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We present CHRONOS, a three-layer architecture providing a unified treatment of these challenges with explicit public and private separation.；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [2605.23888 GenRecon: Bridging Generative Priors for Multi-View 3D Scene Reconstruction](https://arxiv.org/abs/2605.23888) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：We introduce a new approach to high-fidelity 3D scene reconstruction from multi-view RGB images that tightly couples reconstruction with a strong generative 3D prior.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23889 HorizonStream: Long-Horizon Attention for Streaming 3D Reconstruction](https://arxiv.org/abs/2605.23889) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；将 streaming attention 的 influence kernel 分解为 channel-wise long-range decay 与 short-range local geometry，用有界 state 支持多时间尺度证据而避免 sliding-window hard cutoff/attention sink。；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：MODEL-SELF-ATTENTION [章节](../../../../books/part-02-model/14-self-attention.md) |
| [2605.23891 Smart-Insertion-V: Photorealistic Video Insertion via a Closed-Loop Feedback Dual-Stream Framework](https://arxiv.org/abs/2605.23891) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：To overcome this, we propose \textit{\textbf{Smart-Insertion-V}}, an end-to-end \textbf{Dual-Stream} framework that concurrently conducts video insertion and image style transfer.；2+2+2=6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23892 Good Token Hunting: A Hitchhiker's Guide to Token Selection for Visual Geometry Transformers](https://arxiv.org/abs/2605.23892) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；视觉几何 Transformer 的 global attention 可先按 frame diversity 保留覆盖，再按 layer-specific attention entropy 稀疏 token，而不是所有层共享一次 top-k。；3+3+2=8 | 深入完成 | 整合：当前正文 binding 已存在：MODEL-SELF-ATTENTION [章节](../../../../books/part-02-model/14-self-attention.md) |
| [2605.23893 Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models](https://arxiv.org/abs/2605.23893) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 整合：当前正文 binding 已存在：MODEL-MOE [章节](../../../../books/part-02-model/21-moe.md) |
| [2605.23897 ETCHR: Editing To Clarify and Harness Reasoning](https://arxiv.org/abs/2605.23897) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Guided by this analysis, we introduce ETCHR (Editing To Clarify and Harness Reasoning), a question-conditioned, reasoning-aware image editor decoupled from the downstream understanding model and trained with a two-stage recipe targeted at the two gaps: Reasoning Imitation via supervised fine-tuning on edit trajectories, followed by Reasoning Enhancement with VLM-derived rewards for edit correctness and downstream reasoning accuracy.；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING [章节](../../../../books/part-07-agent/78-tool-calling.md) |
| [2605.23898 SPACENUM: Revisiting Spatial Numerical Understanding in VLMs](https://arxiv.org/abs/2605.23898) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；exact-v1 采用命题：Therefore, in this work, we revisit spatial numerical understanding through SpaceNum, a unified framework that captures two complementary settings: numbers as dynamic transitions during spatial exploration, and numbers as static layouts in spatial reasoning.；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.23899 From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills](https://arxiv.org/abs/2605.23899) | 2026-05-25T08:00:00+08:00 | V3 复核沿用 identity/version/命题不变的 exact-v1 证据；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-PLATFORM [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [2605.23901 LLMs as Noisy Channels: A Shannon Perspective on Model Capacity and Scaling Laws](https://arxiv.org/abs/2605.23901) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；把训练噪声、量化或 SFT 扰动拟合为 noisy-channel capacity 可形成诊断性 scaling relation。；3+2+2=7 | 深入完成 | 仅报告：TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [2605.23902 PiD: Fast and High-Resolution Latent Decoding with Pixel Diffusion](https://arxiv.org/abs/2605.23902) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；把 latent-to-pixel reconstruction decoder 改成 conditional pixel diffusion，同时承担 decoding/upscaling；sigma-aware adapter 允许提前终止 latent diffusion，再以 DMD2 压到四步。；3+3+3=9 | 深入完成 | 整合：当前正文 binding 已存在：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.23903 Geo-Align: Video Generation Alignment via Metric Geometry Reward](https://arxiv.org/abs/2605.23903) | 2026-05-25T08:00:00+08:00 | FN challenge 恢复；camera-controlled video RL 用 metric 3D estimator 分离 rotation/translation deviation，并以 real conditioning + synthetic target trajectory 避免 paired video。；3+2+2=7 | 深入完成 | 整合：当前正文 binding 已存在：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |

## 4. 证据与知识整合

225 项逐项版本、评分、method/evaluation/non-proof locator、采用命题与证据边界见 [`evidence-review-v3.json`](../_sources/daily-20260525/evidence-review-v3.json)。可读原始 Source Review 冻结在 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md)，仅对 official-day-owned 且 identity、exact-v1 与采用命题未变的 family 复用；旧日期 owner、分母、Books 状态或 Complete 结论均不继承。2605.22850 的 placeholder locator 已用官方 exact-v1 HTML §3–§6.3 修复，2605.22855 则由 fresh non-author 反例检查从 closure 恢复并完成 exact-v1 review。当前 Books 对读见 [`books-comparison-v3.json`](../_sources/daily-20260525/books-comparison-v3.json)。

### [2605.22826 Evaluating Large Language Models in a Complex Hidden Role Game](https://arxiv.org/abs/2605.22826)

<!-- review:SF-2026-ARXIV-2605-22826:start -->
证据位置：3 Methodology; 4 Results; 2.3 Current Limitations。
<!-- claim:SF-2026-ARXIV-2605-22826:start -->exact-v1 采用命题：This work investigates the reasoning, persuasion, and deceptive capabilities of LLMs within the social deduction game Secret Hitler.<!-- claim:SF-2026-ARXIV-2605-22826:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-22826:end -->

### [2605.22827 Computable Fairness: Boltzmann-Softmax Control for AI Resource Allocation](https://arxiv.org/abs/2605.22827)

<!-- review:SF-2026-ARXIV-2605-22827:start -->
证据位置：official arXiv PDF §2 Methodology; official arXiv PDF §3 Simulation and Results; official arXiv PDF §4.4 Limitations and Future Directions。
<!-- claim:SF-2026-ARXIV-2605-22827:start -->exact-v1 采用命题：We propose Computable Fair Division (CFD), a framework that reinterprets the Boltzmann-Softmax function not as a selection tool but as a probabilistic resource allocation mechanism, redefining the inverse temperature parameter $β$ as a computable control variable governing the efficiency-fairness balance.<!-- claim:SF-2026-ARXIV-2605-22827:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `official arXiv PDF §3 Simulation and Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Filter、Score 与 Bind 分责；Gang、Queue 与 Fairness 必须由显式调度状态拥有。
Books：No Change — Existing Coverage；owner=PLATFORM-GPU-SCHEDULER。
<!-- review:SF-2026-ARXIV-2605-22827:end -->

### [2605.22829 LFRAG: Layout-oriented Fine-grained Retrieval-Augmented Generation on Multimodal Document Understanding](https://arxiv.org/abs/2605.22829)

<!-- review:SF-2026-ARXIV-2605-22829:start -->
证据位置：3 Methodology; 4.2 Experimental Results on LFDocQA; no dedicated limitations section; non-proof boundary taken from disclosed method/evaluation scope。
<!-- claim:SF-2026-ARXIV-2605-22829:start -->exact-v1 采用命题：To address these issues, we propose Layout-oriented Fine-grained Retrieval-Augmented Generation (LFRAG), a novel framework that advances multimodal RAG from page-level to block-level retrieval.<!-- claim:SF-2026-ARXIV-2605-22829:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4.2 Experimental Results on LFDocQA` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§文档结构、查询改写与答案核验必须分层消融；Relevance 不等于 Sufficient Context。
Books：No Change — Existing Coverage；owner=AGENT-RAG。
<!-- review:SF-2026-ARXIV-2605-22829:end -->

### [2605.22842 The Misattribution Gap: When Memory Poisoning Looks Like Model Failure in Agentic AI Systems](https://arxiv.org/abs/2605.22842)

<!-- review:SF-2026-ARXIV-2605-22842:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-22842:start -->We introduce Counterfactual Composition Testing, which identifies the causal entry with 87.5% accuracy and zero false positives, while a forensics baseline fails across all 25 scenarios.<!-- claim:SF-2026-ARXIV-2605-22842:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-22842:end -->

### [2605.22850 ObjectCache: Layerwise Object-Storage Retrieval for KV Cache Reuse](https://arxiv.org/abs/2605.22850)

<!-- review:SF-2026-ARXIV-2605-22850:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-22850` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-22850:start -->ObjectCache: Layerwise Object-Storage Retrieval for KV Cache Reuse 提出的具体变化是：We propose ObjectCache, which co-designs the storage protocol and transfer schedule so that the storage server delivers KV cache data in the order the GPU consumes it, overlapping data transfer with compute across concurrent requests. 摘要中的长期系统挑战为：prefix KV reuse crosses local memory into layerwise object-store retrieval with explicit object identity。它可能改变 `INFER-KV-CACHE` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Under shared bandwidth caps, our scheduler reduces added TTFT by 1.2--1.8x compared with equal bandwidth sharing.”暂不作为最终证据。<!-- claim:SF-2026-ARXIV-2605-22850:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-22850:end -->

### [2605.22855 PrefBench: Evaluating Zero-Shot LLM Agents in Hidden-Preference Personalized Pricing Negotiations](https://arxiv.org/abs/2605.22855)

<!-- review:SF-2026-ARXIV-2605-22855:start -->
证据位置：HTML §§3–5 task formulation、simulator assets、LLM protocol/baselines；HTML §6 Experiments（Table 3 main results、Table 4 prompt/reasoning analyses）；HTML §8 Limitations and Future Work；Appendix D uncertainty/heuristic details。
<!-- claim:SF-2026-ARXIV-2605-22855:start -->Agent evaluation 必须分离 structured-action contract compliance、agreement/completion rate 与 intended business/environment outcome：在作者固定的 7,500-episode stream 中，合法 JSON action 与高于 0.99 的 deal rate 可以同时对应接近 random baseline、远低于 concession heuristic 的 seller profit。<!-- claim:SF-2026-ARXIV-2605-22855:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 PrefBench 的半合成车辆定价 simulator、benchmark-defined hidden buyer model、披露的 zero-shot prompts/providers 与 seller-profit objective；不证明真实谈判收入、一般 Agent 无能，亦未评估 fairness、privacy、welfare。更详细 prompt 在作者 ablation 中提高成交率却降低利润，因此 contract completion 只能作为诊断，不可冒充成功判据；外部有效性或 objective identity 不清时，保留原始 trajectory 与独立 outcome metrics，而不是把 completion 升级为 success。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。Ch66 已通过“HTTP 成功只是质量判断的第一道门”与“从目标到证据，而不是从指标到目标”分离 Contract、Semantic/Policy 和 Outcome；本论文是该既有命题的受限实例，没有改变 owner、state/control responsibility、trade-off、failure 或 fallback。
<!-- review:SF-2026-ARXIV-2605-22855:end -->

### [2605.22866 BOHM: Zero-Cost Hierarchical Attribution for Compound AI Systems](https://arxiv.org/abs/2605.22866)

<!-- review:SF-2026-ARXIV-2605-22866:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-22866` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-22866:start -->We introduce BOHM, which extracts a hierarchical attribution tree directly from the routing weights such systems already maintain: leaf attribution is the path product of root-to-leaf routing weights; level-k attribution is the induced distribution over depth-k nodes.<!-- claim:SF-2026-ARXIV-2605-22866:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-22866:end -->

### [2605.22868 FusionSense: Tri-Stage Near-Sensor Learning for Runtime-Adaptive Multimodal Edge Intelligence](https://arxiv.org/abs/2605.22868)

<!-- review:SF-2026-ARXIV-2605-22868:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-22868` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-22868:start -->We present FusionSense, a fusion-aware intelligent sensing framework for energy-constrained autonomous edge systems.<!-- claim:SF-2026-ARXIV-2605-22868:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-22868:end -->

### [2605.22869 FuRA: Full-Rank Parameter-Efficient Fine-Tuning with Spectral Preconditioning](https://arxiv.org/abs/2605.22869)

<!-- review:SF-2026-ARXIV-2605-22869:start -->
证据位置：PDF §3–§5 FuRA spectral PEFT; PDF §6 Experiments; PDF Appendix E scope and ablations。
<!-- claim:SF-2026-ARXIV-2605-22869:start -->用 block tensor-train/SVD basis 预条件化低秩更新，使有限 rank 的可用方向不只由 nominal rank 决定。<!-- claim:SF-2026-ARXIV-2605-22869:end -->
证据边界、trade-off、failure 与 fallback：收益绑定受测 LLaMA/VLM 任务、SVD basis 与预计算；basis 陈旧或额外分解成本超界时回退普通 LoRA/full tuning。Ch30 已明确 adapter capacity 同时取决于 rank、optimizer transform 与实际更新谱。
Books：No Change — Existing Coverage；owner=TRAIN-LORA。
<!-- review:SF-2026-ARXIV-2605-22869:end -->

### [2605.22870 The Readout Shortcut: Positional Number Copying Dominates Arithmetic CoT Readout in Small Language Models](https://arxiv.org/abs/2605.22870)

<!-- review:SF-2026-ARXIV-2605-22870:start -->
证据位置：PDF §2–§6 Readout Shortcut analyses; PDF arithmetic experiments; PDF §Limitations (p.8)。
<!-- claim:SF-2026-ARXIV-2605-22870:start -->dense per-step/per-loop loss 只约束 readout 可见方向，模型可能把可解中间状态藏在 readout null space，并在最后一步才形成答案。<!-- claim:SF-2026-ARXIV-2605-22870:end -->
证据边界、trade-off、failure 与 fallback：证据限于 1–3B arithmetic、numeric trailing answer 与受测架构；不能外推开放任务。Ch18 已写明 looped LM 的 per-loop cross-entropy 只控制 readout-visible variables，hidden recurrent state 仍可携带信息。
Books：No Change — Existing Coverage；owner=MODEL-DECODER-ONLY。
<!-- review:SF-2026-ARXIV-2605-22870:end -->

### [2605.22871 Approximate Machine Unlearning through Manifold Representation Forgetting Guided by Self Mode Connectivity](https://arxiv.org/abs/2605.22871)

<!-- review:SF-2026-ARXIV-2605-22871:start -->
证据位置：3. Priliminary and Problem Reformulation; 5. Experiments; G.2. Limitations and Additional Evaluation with Fine Tuning。
<!-- claim:SF-2026-ARXIV-2605-22871:start -->exact-v1 采用命题：In this paper, we propose \textbf{ManiF-SMC} (\textbf{Mani}fold \textbf{F}orgetting with \textbf{S}elf \textbf{M}ode \textbf{C}onnectivity), motivated by the observation that a model retrained on the remaining data tends to classify erased samples by their semantic similarity to the retained data.<!-- claim:SF-2026-ARXIV-2605-22871:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5. Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Supervision Granularity 应跟随可验证的状态边界；dataset revision 与 coverage contract 必须可重放。
Books：No Change — Existing Coverage；owner=TRAIN-DATA。
<!-- review:SF-2026-ARXIV-2605-22871:end -->

### [2605.22874 NeuroNL2LTL: A Neurosymbolic Framework for Natural Language Translation of Linear Temporal Logic](https://arxiv.org/abs/2605.22874)

<!-- review:SF-2026-ARXIV-2605-22874:start -->
证据位置：3 The System Architecture; 4.2 Main Results: Translation Accuracy; 6 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-22874:start -->exact-v1 采用命题：We present NeuroNL2LTL, a neurosymbolic architecture unifying learned translation with formal verification.<!-- claim:SF-2026-ARXIV-2605-22874:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4.2 Main Results: Translation Accuracy` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§模型输出只是 Proposal；Tool Contract、side-effect class 与独立 Outcome Contract 拥有 commit。
Books：No Change — Existing Coverage；owner=AGENT-TOOL-CALLING。
<!-- review:SF-2026-ARXIV-2605-22874:end -->

### [2605.22875 RMA: an Agentic System for Research-Level Mathematical Problems](https://arxiv.org/abs/2605.22875)

<!-- review:SF-2026-ARXIV-2605-22875:start -->
证据位置：3 Methodology; Correctness results from mathematicians.; Appendix C Limitations。
<!-- claim:SF-2026-ARXIV-2605-22875:start -->exact-v1 采用命题：We present $\textbf{Research Math Agents (RMA)}$, an agentic framework for automated reasoning on research-level mathematical problems.<!-- claim:SF-2026-ARXIV-2605-22875:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `Correctness results from mathematicians.` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Plan 不是解释文本；从目标到状态图，并以完成证据和 verifier 决定提交。
Books：No Change — Existing Coverage；owner=AGENT-PLANNING。
<!-- review:SF-2026-ARXIV-2605-22875:end -->

### [2605.22879 Budgeted Dynamic Trace Structures for Token-Efficient Sequential Computation](https://arxiv.org/abs/2605.22879)

<!-- review:SF-2026-ARXIV-2605-22879:start -->
证据位置：HTML §§2–4 trace graph/history/budget/compaction data structures; HTML §7 Experiments; §7.2–§7.4 synthetic/tokenizer/forward matrices; HTML §10 Limitations。
<!-- claim:SF-2026-ARXIV-2605-22879:start -->把长执行轨迹表示为带状态过滤的 rooted graph 与 append-only history，在 token/byte budget 下用 summary+suffix compaction、reference-counted observations、delta overlay 与 soft cap 保留可恢复结构。<!-- claim:SF-2026-ARXIV-2605-22879:end -->
证据边界、trade-off、failure 与 fallback：结果来自 synthetic trace、ancillary Rust artifact 与三种公开 tokenizer/forward 目标；近似 token accounting、summary 错误和引用生命周期会破坏恢复语义，超界时保留原始 history 或提高预算。
Books：Applied；owner=AGENT-CONTEXT。
<!-- review:SF-2026-ARXIV-2605-22879:end -->

### [2605.22880 How Far Will They Go? Red-Teaming Online Influence with Large Language Models](https://arxiv.org/abs/2605.22880)

<!-- review:SF-2026-ARXIV-2605-22880:start -->
证据位置：3 Methodology; 4 Results; 5 Discussion。
<!-- claim:SF-2026-ARXIV-2605-22880:start -->exact-v1 采用命题：We introduce an empirical red-teaming framework for measuring LLM Overton Windows (OWs), defined as the range of political opinions a model can reliably express on controversial topics, and for quantifying how simple natural-language jailbreaks expand that range.<!-- claim:SF-2026-ARXIV-2605-22880:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-22880:end -->

### [2605.22883 Energy per Successful Goal: Goal-Level Energy Accounting for Agentic AI Systems](https://arxiv.org/abs/2605.22883)

<!-- review:SF-2026-ARXIV-2605-22883:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-22883` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-22883:start -->Agent 能耗从 per-token/per-request 上移到 per-successful-goal：同一 goal 的模型调用、tool、retry、idle 与失败 run 进入同一 lineage；成功谓词/evaluator 版本决定分母。<!-- claim:SF-2026-ARXIV-2605-22883:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-22883:end -->

### [2605.22884 Tensor Cache: Eviction-conditioned Associative Memory for Transformers](https://arxiv.org/abs/2605.22884)

<!-- review:SF-2026-ARXIV-2605-22884:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-22884` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-22884:start -->sliding-window eviction 不再等于丢弃：exact recent KV 作为 L1，已驱逐 KV 以 outer-product fast-weight matrix 形成固定大小 L2；写入顺序、decay/gate、数值 scan 与 exact-window fallback 成为新 cache identity。<!-- claim:SF-2026-ARXIV-2605-22884:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-22884:end -->

### [2605.22885 ImProver 2: Iteratively Self-Improving LMs for Neurosymbolic Proof Optimization](https://arxiv.org/abs/2605.22885)

<!-- review:SF-2026-ARXIV-2605-22885:start -->
证据位置：HTML §4 ImProver 2; §4.2 neurosymbolic augmentation; §4.3 IRPO; HTML §5 Experiments; §5.2 main results/ablations; HTML §6 Limitations and Future Work。
<!-- claim:SF-2026-ARXIV-2605-22885:start -->用 Lean checker、formal-structure scaffold 与 expert-iteration/preference loop 优化已验证证明，同时以结构化 metrics 而非自由文本判断改写质量。<!-- claim:SF-2026-ARXIV-2605-22885:end -->
证据边界、trade-off、failure 与 fallback：证据限 Lean 4、作者 proof repositories、7B model 与披露 metrics；checker 只证明形式目标，不能证明规范对应现实意图，失败时回退原证明与人工 code review。
Books：No Change — Existing Coverage；owner=AGENT-TOOL-CALLING。
<!-- review:SF-2026-ARXIV-2605-22885:end -->

### [2605.22891 Pointwise Metrics Mislead: An Evaluation Protocol for Multimodal Inverse Problems](https://arxiv.org/abs/2605.22891)

<!-- review:SF-2026-ARXIV-2605-22891:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-22891` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-22891:start -->We show that this assumption fails structurally for inverse problems with multimodal posteriors.<!-- claim:SF-2026-ARXIV-2605-22891:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-22891:end -->

### [2605.22896 Agentic-VLA: Efficient Online Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2605.22896)

<!-- review:SF-2026-ARXIV-2605-22896:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-22896` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-22896:start -->We introduce Agentic-VLA, an agentic training framework that enables VLAs to efficiently adapt online through three key innovations: (1) Adaptive Reward Synthesis, which dynamically generates and adjusts reward functions based on the VLA's current capabilities and task complexity, decomposing complex tasks into learnable sub-goals for curriculum learning; (2) Language-Guided Exploration, where a critic model provides structured guidance for systematic exploration rather than random sampling; and (3) Experience Memory,which stores and retrieves task-relevant policy weights for warm-starting adaptation to similar tasks.<!-- claim:SF-2026-ARXIV-2605-22896:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-22896:end -->

### [2605.22897 From Residuals to Reasons: LLM-Guided Mechanism Inference from Tabular Data](https://arxiv.org/abs/2605.22897)

<!-- review:SF-2026-ARXIV-2605-22897:start -->
证据位置：2 Methods; 4 Experiments; no dedicated limitations section; non-proof boundary taken from disclosed method/evaluation scope。
<!-- claim:SF-2026-ARXIV-2605-22897:start -->exact-v1 采用命题：We introduce Multi-Agent Residual In-Context Learning (MARICL), an agentic framework in which LLM agents analyze where a base-model fails, hypothesize missing structure from high-residual examples provided in context, and produce explicit correction terms refined through multi-turn textual gradient optimization.<!-- claim:SF-2026-ARXIV-2605-22897:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Plan 不是解释文本；从目标到状态图，并以完成证据和 verifier 决定提交。
Books：No Change — Existing Coverage；owner=AGENT-PLANNING。
<!-- review:SF-2026-ARXIV-2605-22897:end -->

### [2605.22898 FIRMA: FIbonacci Ring Model Aggregation for Privacy-preserving Federated Learning](https://arxiv.org/abs/2605.22898)

<!-- review:SF-2026-ARXIV-2605-22898:start -->
证据位置：3.2 Model Architecture; 6.5 FibFL Component Ablation Study; 7. General Discussion and Conclusions。
<!-- claim:SF-2026-ARXIV-2605-22898:start -->exact-v1 采用命题：We propose FIRMA (\textbf{FI}bonacci \textbf{R}ing \textbf{M}odel \textbf{A}ggregation), a family of three progressively enhanced federated learning protocols: 1) \fibfl\ establishes the foundation: server-free ring aggregation with Fibonacci-weighted neighbour blending and permanently private classification heads.<!-- claim:SF-2026-ARXIV-2605-22898:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `6.5 FibFL Component Ablation Study` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§全局 loss/update 语义与 collective throughput 分开；通信优化不能改变训练状态身份。
Books：No Change — Existing Coverage；owner=TRAIN-DISTRIBUTED-TRAINING。
<!-- review:SF-2026-ARXIV-2605-22898:end -->

### [2605.22902 Transcoders Trace Visual Grounding and Hallucinations in Vision-Language Models](https://arxiv.org/abs/2605.22902)

<!-- review:SF-2026-ARXIV-2605-22902:start -->
证据位置：2 Methodology; 2.2 Experimental Setup; 8 Limitations and Scope。
<!-- claim:SF-2026-ARXIV-2605-22902:start -->exact-v1 采用命题：These results show that function-centric circuit decomposition yields interpretable and predictive accounts of multimodal computation in VLMs.<!-- claim:SF-2026-ARXIV-2605-22902:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `2.2 Experimental Setup` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§任务贡献与当前可靠性不能共用一个 Gate；感知、写入、读取与行动使用必须分开验证。
Books：No Change — Existing Coverage；owner=MULTIMODAL-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-22902:end -->

### [2605.22903 Seeing without Looking: Do Vision-Language Benchmarks Really Test Vision?](https://arxiv.org/abs/2605.22903)

<!-- review:SF-2026-ARXIV-2605-22903:start -->
证据位置：HTML §3 Vision is not Needed; HTML §4–§6 intervention experiments; HTML §7 Discussion; §8 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-22903:start -->top-1 benchmark accuracy 对视觉 token 删除、遮挡与 entity swap 可能不敏感，必须把保持输入/问题而干预视觉证据的 counterfactual test 纳入 grounding evaluation。<!-- claim:SF-2026-ARXIV-2605-22903:end -->
证据边界、trade-off、failure 与 fallback：七个开源 VLM、四类 benchmark 与作者干预不证明所有视觉任务失真；实体定位/生成式替换也引入误差。Ch66 已要求同一 Evaluation Identity 下执行证据干预并把 sensor 与 truth authority 分开。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-22903:end -->

### [2605.22905 EVE-Agent: Evidence-Verifiable Self-Evolving Agents](https://arxiv.org/abs/2605.22905)

<!-- review:SF-2026-ARXIV-2605-22905:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-22905` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-22905:start -->We argue that evidence verifiability is a prerequisite for trustworthy self-evolution in search agents: each generated instance should include not only an answer but also a source-grounded span whose contribution to that answer can be measured.<!-- claim:SF-2026-ARXIV-2605-22905:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-22905:end -->

### [2605.22907 VideoOdyssey: A Benchmark for Ultra-Long-Context and Omni-Modal Video Understanding](https://arxiv.org/abs/2605.22907)

<!-- review:SF-2026-ARXIV-2605-22907:start -->
证据位置：Multimodal Large Language Models; 4.2 Main Results and Findings; Appendix I Limitations and broader impacts。
<!-- claim:SF-2026-ARXIV-2605-22907:start -->exact-v1 采用命题：Driven by this metric, we introduce VideoOdyssey, a benchmark specifically designed for ultra-long-context and omni-modal video understanding.<!-- claim:SF-2026-ARXIV-2605-22907:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4.2 Main Results and Findings` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§长上下文容量必须同时声明计算、状态与读取合同，而不能由名义长度推出。
Books：No Change — Existing Coverage；owner=MODEL-LONG-CONTEXT。
<!-- review:SF-2026-ARXIV-2605-22907:end -->

### [2605.22939 Learnability-Informed Fine-Tuning of Diffusion Language Models](https://arxiv.org/abs/2605.22939)

<!-- review:SF-2026-ARXIV-2605-22939:start -->
证据位置：HTML §4 Analysis; §5 Methods — what/when tokens are learned; HTML §6 Experiments; §6.2 results; §6.3 ablations; HTML §7 Conclusion; Appendix B/D compute-matched and implementation scope。
<!-- claim:SF-2026-ARXIV-2605-22939:start -->Diffusion LM 的 SFT 不应在所有 timestep 同等学习所有 token；LIFT 按 token learnability 将易/难 token 分配到不同 mask/context regime。<!-- claim:SF-2026-ARXIV-2605-22939:end -->
证据边界、trade-off、failure 与 fallback：证据限 LLaDA/Dream、六项 reasoning benchmark 与作者 mask/sampling recipe；learnability proxy 失配会形成错误 curriculum，回退 vanilla SFT 或 compute-matched sampling。
Books：Applied；owner=TRAIN-SFT。
<!-- review:SF-2026-ARXIV-2605-22939:end -->

### [2605.22940 Human-Centered Learning Mechanics: A Dynamical Framework for Entropy-Regulated Representation Learning](https://arxiv.org/abs/2605.22940)

<!-- review:SF-2026-ARXIV-2605-22940:start -->
证据位置：3 The Human-Centered Learning Mechanics (HCLM) Framework; Appendix A Proofs of Theoretical Results; 9.8 Limitations of the Current Formulation。
<!-- claim:SF-2026-ARXIV-2605-22940:start -->exact-v1 采用命题：We propose Human-Centered Learning Mechanics (HCLM), a dynamical and information-theoretic framework for open and controlled learning systems.<!-- claim:SF-2026-ARXIV-2605-22940:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `Appendix A Proofs of Theoretical Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从可读出到机制：证据应逐级变强——信息存在、可读与被使用是三个不同命题。
Books：No Change — Existing Coverage；owner=WORLDVIEW-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-22940:end -->

### [2605.22963 Graph Alignment Topology as an Inductive Bias for Grounding Detection](https://arxiv.org/abs/2605.22963)

<!-- review:SF-2026-ARXIV-2605-22963:start -->
证据位置：3 Method; 5 Results; 6 Discussion。
<!-- claim:SF-2026-ARXIV-2605-22963:start -->exact-v1 采用命题：Large Language Models (LLMs) are optimized to produce distributionally plausible continuations rather than to explicitly verify whether generated propositions are entailed by source documents.<!-- claim:SF-2026-ARXIV-2605-22963:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5 Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-22963:end -->

### [2605.22964 Certification from Examples is Hard for Circuits and Transformers under Minimal Overparametrization](https://arxiv.org/abs/2605.22964)

<!-- review:SF-2026-ARXIV-2605-22964:start -->
证据位置：PDF main certification-hardness theorems; PDF trained/constructed addition cases; PDF assumptions and appendices。
<!-- claim:SF-2026-ARXIV-2605-22964:start -->有限样例通过不能升级成精确算法证书；对受限 threshold-circuit/log-precision Transformer 类，exact certification 仍可能需要指数证据。<!-- claim:SF-2026-ARXIV-2605-22964:end -->
证据边界、trade-off、failure 与 fallback：结论依赖形式模型、精度与开销定义，不证明所有神经网络验证都指数困难。Ch66 已区分 tests、translation certificate 与 machine proof，并要求 specification/parser/solver 边界保留。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-22964:end -->

### [2605.22972 A mathematical theory of balancing relational generalization and memorization](https://arxiv.org/abs/2605.22972)

<!-- review:SF-2026-ARXIV-2605-22972:start -->
证据位置：4 Theoretical Results; 4 Theoretical Results; 6 Discussion。
<!-- claim:SF-2026-ARXIV-2605-22972:start -->exact-v1 采用命题：To address this gap, we introduce a novel task, transitive inference with exceptions, that tests for relational generalization and memorization of an exception to the relational rule.<!-- claim:SF-2026-ARXIV-2605-22972:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Theoretical Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从可读出到机制：证据应逐级变强——信息存在、可读与被使用是三个不同命题。
Books：No Change — Existing Coverage；owner=WORLDVIEW-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-22972:end -->

### [2605.22976 LLM Code Smells: A Taxonomy and Detection Approach](https://arxiv.org/abs/2605.22976)

<!-- review:SF-2026-ARXIV-2605-22976:start -->
证据位置：3 General Methodology; 7 Validation Design and Results; 8 Limitations and threats to validity。
<!-- claim:SF-2026-ARXIV-2605-22976:start -->exact-v1 采用命题：Our results show that LLM code smells affect 73.5% of the analyzed systems, with a detection precision of 91.3% and a recall of 71.8%.<!-- claim:SF-2026-ARXIV-2605-22976:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `7 Validation Design and Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-22976:end -->

### [2605.22981 Memorization Dynamics of Fill-in-the-Middle Pretraining](https://arxiv.org/abs/2605.22981)

<!-- review:SF-2026-ARXIV-2605-22981:start -->
证据位置：PDF §3–§4 FIM memorization experiments; PDF §5.1 Limitations; PDF appendices。
<!-- claim:SF-2026-ARXIV-2605-22981:start -->fill-in-the-middle objective 与重复片段共同改变 memorization surface，必须按 corruption/objective、重复次数和 extraction probe 区分记忆风险。<!-- claim:SF-2026-ARXIV-2605-22981:end -->
证据边界、trade-off、failure 与 fallback：仅从头训练的小模型与重复次数不超过 128，attribution 未闭合；Ch27 已要求 corruption policy、dedup/repetition 与 memorization probe 共同版本化。
Books：No Change — Existing Coverage；owner=TRAIN-DATA。
<!-- review:SF-2026-ARXIV-2605-22981:end -->

### [2605.22984 Test-Time Training Undermines Safety Guardrails](https://arxiv.org/abs/2605.22984)

<!-- review:SF-2026-ARXIV-2605-22984:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-22984` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-22984:start -->test-time training 会创建可持续改变后续行为的新 model revision；adaptation loop 只能提出 update，独立 safety gate 必须在更新前后重验收并拥有 commit/rollback，收益是适应性，代价是可累积 guardrail erosion。<!-- claim:SF-2026-ARXIV-2605-22984:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-22984:end -->

### [2605.22986 Robots That Know What to Ask: Recovering Misaligned Rewards through Targeted Explanations](https://arxiv.org/abs/2605.22986)

<!-- review:SF-2026-ARXIV-2605-22986:start -->
证据位置：IV Method; V-B Results; VII Conclusion。
<!-- claim:SF-2026-ARXIV-2605-22986:start -->exact-v1 采用命题：We propose a framework that detects such underspecified features and actively solicits targeted corrective demonstrations.<!-- claim:SF-2026-ARXIV-2605-22986:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `V-B Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§VLA 闭环把 observation revision、action schema、controller authority 与真实 environment transition 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-EMBODIED-VLA。
<!-- review:SF-2026-ARXIV-2605-22986:end -->

### [2605.22996 CoMoGen: COntrollable MOtion Dynamics and Interactions with Mask-Guided Video GENeration](https://arxiv.org/abs/2605.22996)

<!-- review:SF-2026-ARXIV-2605-22996:start -->
证据位置：4 Method; 5 Experiments; 5.4 Discussion on Out-of-distribution Robustness and Efficiency。
<!-- claim:SF-2026-ARXIV-2605-22996:start -->exact-v1 采用命题：We present CoMoGen, a controllable video generation framework that generates realistic interactive dynamics from a single binary mask sequence conditioned on an input image.<!-- claim:SF-2026-ARXIV-2605-22996:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5 Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§并行与少步生成必须声明依赖、轨迹和状态边界；Draft、Verify 与 Correct 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-22996:end -->

### [2605.23017 Smoothed Elicitation Complexity for Approximate $Γ$-calibration of Discrete Classification Tasks](https://arxiv.org/abs/2605.23017)

<!-- review:SF-2026-ARXIV-2605-23017:start -->
证据位置：HTML §3 one-dimensional Lipschitz elicitable properties; HTML §3.1 algorithms; Appendix C applications; HTML Appendix B calibration-metric discussion; theorem assumptions。
<!-- claim:SF-2026-ARXIV-2605-23017:start -->exact-v1 采用命题：Along the way, we characterize the Lipschitz elicitation complexity of strongly orderable discrete properties by constructing algorithms for designing these Lipschitz properties, which we prove can be post-processed to obtain the original discrete property.<!-- claim:SF-2026-ARXIV-2605-23017:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `no standalone evaluation section; exact-v1 stated theorem/method scope reviewed` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23017:end -->

### [2605.23019 PACE: Two-Timescale Self-Evolution for Small Language Model Agents](https://arxiv.org/abs/2605.23019)

<!-- review:SF-2026-ARXIV-2605-23019:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23019` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23019:start -->Agent 自演化应分成 prompt fast path 与 control-logic slow path：前者饱和后才允许后者在 held-out replay 下晋级；双 timescale 降低 blast radius，但引入阶段切换、验证集过拟合和 rollback debt。<!-- claim:SF-2026-ARXIV-2605-23019:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23019:end -->

### [2605.23023 How to Steer Your Multi-Agent System: Human-LLM Collaborative Planning](https://arxiv.org/abs/2605.23023)

<!-- review:SF-2026-ARXIV-2605-23023:start -->
证据位置：PDF §3–§4 co-planning design space; PDF §5–§6 user study and controlled experiments; PDF §7.2 Limitations。
<!-- claim:SF-2026-ARXIV-2605-23023:start -->human–LLM co-planning 应把 proposal、critique、selection 与 final commit authority 分开，而不是让对话流畅度代理计划质量。<!-- claim:SF-2026-ARXIV-2605-23023:end -->
证据边界、trade-off、failure 与 fallback：用户研究与任务集不能证明跨领域最优交互；Ch79 已拥有 proposal/verification/commit、branch budget 与 human gate。高风险动作失败时回退人工计划与显式批准。
Books：No Change — Existing Coverage；owner=AGENT-PLANNING。
<!-- review:SF-2026-ARXIV-2605-23023:end -->

### [2605.23024 The Deterministic Horizon: Impossibility Results as Design Specifications for Trustworthy AI Systems](https://arxiv.org/abs/2605.23024)

<!-- review:SF-2026-ARXIV-2605-23024:start -->
证据位置：official PDF §2.2–§2.3 architecture ceiling and Deterministic Horizon; official PDF §2.3.2 empirical validation across 12 architectures; §2.3.3 fine-tuning test; official PDF thesis-level assumptions and cross-chapter scope; no single universal deployment theorem。
<!-- claim:SF-2026-ARXIV-2605-23024:start -->exact-v1 采用命题：Large language models now write software, draft legal documents, and produce clinical notes, yet fundamental limits, from Turing and Arrow to the No Free Lunch theorems, shape what computation can do.<!-- claim:SF-2026-ARXIV-2605-23024:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `official PDF §2.3.2 empirical validation across 12 architectures; §2.3.3 fine-tuning test` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Next-token 接口不要求内部状态只有一个粒度；输出接口不等于完整内部机制。
Books：Report Only；owner=MODEL-DECODER-ONLY。
<!-- review:SF-2026-ARXIV-2605-23024:end -->

### [2605.23028 RADAR: Relative Angular Divergence Across Representations](https://arxiv.org/abs/2605.23028)

<!-- review:SF-2026-ARXIV-2605-23028:start -->
证据位置：2 Problem Statement; 4 Results; 6 Limitations, Future Work and Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23028:start -->exact-v1 采用命题：We propose RADAR, a simple, geometrically grounded metric for estimating cross-domain transferability in foundation models.<!-- claim:SF-2026-ARXIV-2605-23028:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从可读出到机制：证据应逐级变强——信息存在、可读与被使用是三个不同命题。
Books：No Change — Existing Coverage；owner=WORLDVIEW-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23028:end -->

### [2605.23032 Brain-LLM Alignment Tracks Training Data, Not Typology](https://arxiv.org/abs/2605.23032)

<!-- review:SF-2026-ARXIV-2605-23032:start -->
证据位置：3.5 Statistical Framework; Why the result is non-trivial.; Limitations。
<!-- claim:SF-2026-ARXIV-2605-23032:start -->exact-v1 采用命题：Brain-LLM alignment is well established in English, yet the brain's language network is neuroanatomically universal across languages.<!-- claim:SF-2026-ARXIV-2605-23032:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `Why the result is non-trivial.` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从可读出到机制：证据应逐级变强——信息存在、可读与被使用是三个不同命题。
Books：No Change — Existing Coverage；owner=WORLDVIEW-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23032:end -->

### [2605.23033 Uncovering the Latent Potential of Deep Intermediate Representations](https://arxiv.org/abs/2605.23033)

<!-- review:SF-2026-ARXIV-2605-23033:start -->
证据位置：3 Methodology; 5 Experimental setup; no dedicated limitations section; non-proof boundary taken from disclosed method/evaluation scope。
<!-- claim:SF-2026-ARXIV-2605-23033:start -->exact-v1 采用命题：Contrary to the widespread practice of using only the final layer or shallow mixtures, we show that task-relevant information is distributed non-monotonically across layers and cannot be recovered by naïve aggregation.<!-- claim:SF-2026-ARXIV-2605-23033:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5 Experimental setup` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从可读出到机制：证据应逐级变强——信息存在、可读与被使用是三个不同命题。
Books：No Change — Existing Coverage；owner=WORLDVIEW-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23033:end -->

### [2605.23035 Sparse Autoencoders Map Brain-LLM Alignment onto Cortical Semantic Topography](https://arxiv.org/abs/2605.23035)

<!-- review:SF-2026-ARXIV-2605-23035:start -->
证据位置：3 Methodology; 4 Results; Limitations of the audit.。
<!-- claim:SF-2026-ARXIV-2605-23035:start -->exact-v1 采用命题：Intermediate layers of large language models (LLMs) best predict human brain responses to language, one of the most robust findings in computational neurolinguistics, yet why remains mechanistically unexplained.<!-- claim:SF-2026-ARXIV-2605-23035:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从可读出到机制：证据应逐级变强——信息存在、可读与被使用是三个不同命题。
Books：No Change — Existing Coverage；owner=WORLDVIEW-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23035:end -->

### [2605.23036 Multilingual Steering by Design: Multilingual Sparse Autoencoders and Principled Layer Selection](https://arxiv.org/abs/2605.23036)

<!-- review:SF-2026-ARXIV-2605-23036:start -->
证据位置：SAE-Based Activation and Language Steering.; 5 Results; Limitations。
<!-- claim:SF-2026-ARXIV-2605-23036:start -->exact-v1 采用命题：First, we show that training SAEs on multilingual data consistently strengthens cross-lingual representations and yields more reliable, quality-preserving language control across layers and model families.<!-- claim:SF-2026-ARXIV-2605-23036:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5 Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Sparse Support 与 Value Normalization 是两步决策；selector 必须承担语义责任并保留 dense fallback。
Books：No Change — Existing Coverage；owner=MODEL-SELF-ATTENTION。
<!-- review:SF-2026-ARXIV-2605-23036:end -->

### [2605.23039 Do Language Models Know What Not to Say? Causal Evidence for Statistical Preemption in LLMs](https://arxiv.org/abs/2605.23039)

<!-- review:SF-2026-ARXIV-2605-23039:start -->
证据位置：G.4 Validation Method and Precision; 4.2 Results: Group Differences; no dedicated limitations section; non-proof boundary taken from disclosed method/evaluation scope。
<!-- claim:SF-2026-ARXIV-2605-23039:start -->exact-v1 采用命题：We present a computational study that, for the first time, directly dissociates statistical preemption from the competing entrenchment hypothesis in large language models within a single converging design.<!-- claim:SF-2026-ARXIV-2605-23039:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4.2 Results: Group Differences` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从可读出到机制：证据应逐级变强——信息存在、可读与被使用是三个不同命题。
Books：No Change — Existing Coverage；owner=WORLDVIEW-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23039:end -->

### [2605.23040 Steered Generation via Gradient-Based Optimization on Sparse Query Features](https://arxiv.org/abs/2605.23040)

<!-- review:SF-2026-ARXIV-2605-23040:start -->
证据位置：PDF §2 sparse query-feature steering; PDF experiments and ablations; PDF scope/limitations。
<!-- claim:SF-2026-ARXIV-2605-23040:start -->从 query-conditioned sparse features 中优化小规模干预方向，可把全局 steering vector 改成输入相关控制，但需要独立因果与任务回归 Gate。<!-- claim:SF-2026-ARXIV-2605-23040:end -->
证据边界、trade-off、failure 与 fallback：SAE/model/task 与优化成本限制结论；feature 相关不等于因果，错误 direction 会破坏未测行为。当前 ROADMAP 没有唯一 model-internals intervention owner，先保留结构候选，不强塞 Prompt 或 Evaluation。
Books：Structural Candidate；owner=尚无唯一 owner。
<!-- review:SF-2026-ARXIV-2605-23040:end -->

### [2605.23043 HawkesLLM: Semantic Uncertainty Propagation in Agentic Text Simulation](https://arxiv.org/abs/2605.23043)

<!-- review:SF-2026-ARXIV-2605-23043:start -->
证据位置：3.1 Agentic Text Simulation Framework; 5 Results; 6 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23043:start -->exact-v1 采用命题：This paper studies this problem with HawkesLLM, a framework that separates temporal influence modeling from text generation.<!-- claim:SF-2026-ARXIV-2605-23043:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5 Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Memory Write 是高风险决策；Fact State 与 Retrieval-policy State 必须分离。
Books：No Change — Existing Coverage；owner=AGENT-MEMORY。
<!-- review:SF-2026-ARXIV-2605-23043:end -->

### [2605.23054 Model Collapse as Cultural Evolution](https://arxiv.org/abs/2605.23054)

<!-- review:SF-2026-ARXIV-2605-23054:start -->
证据位置：PDF iterated self-training design; PDF experiments and five predictions; PDF §7 Limitations。
<!-- claim:SF-2026-ARXIV-2605-23054:start -->recursive synthetic training 的漂移可呈非单调 cultural-attractor dynamics，不能只用单代质量或单一 supplier share 解释 model collapse。<!-- claim:SF-2026-ARXIV-2605-23054:end -->
证据边界、trade-off、failure 与 fallback：文化演化只是分析对应而非形式等价，模型/代数有限；Ch27 已要求同时冻结 base checkpoint、supplier mixture、human anchor、generation 与 seed，并避免单变量因果。
Books：No Change — Existing Coverage；owner=TRAIN-DATA。
<!-- review:SF-2026-ARXIV-2605-23054:end -->

### [2605.23058 A measurement substrate for agentic Kubernetes operations: Methodology and a case study in retrieval-compounding falsification](https://arxiv.org/abs/2605.23058)

<!-- review:SF-2026-ARXIV-2605-23058:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23058` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23058:start -->We present agent-breakage, a closed-loop measurement framework that injects faults into a target Kubernetes cluster, observes how an autonomous agent responds, scores the response on four axes against ground truth, and accumulates outcome-labeled (state, action, outcome) tuples.<!-- claim:SF-2026-ARXIV-2605-23058:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23058:end -->

### [2605.23061 Anytime Training with Schedule-Free Spectral Optimization](https://arxiv.org/abs/2605.23061)

<!-- review:SF-2026-ARXIV-2605-23061:start -->
证据位置：PDF §2–§4 SF-NorMuon; PDF language-model experiments; Appendix E; PDF compute/scale omissions。
<!-- claim:SF-2026-ARXIV-2605-23061:start -->schedule-free matrix optimizer 的 averaging、spectral update 与 weight decay 必须作为同一 state transition 验收，而非把 horizon-free 当作无状态。<!-- claim:SF-2026-ARXIV-2605-23061:end -->
证据边界、trade-off、failure 与 fallback：证据只到 125M/772M 与披露 token budgets，最大 8x 运行因计算未完成；Ch28 已覆盖 schedule-free averaging、weight-decay interaction、optimizer-state/checkpoint identity 与 WSD/cosine fallback。
Books：No Change — Existing Coverage；owner=TRAIN-PRETRAINING。
<!-- review:SF-2026-ARXIV-2605-23061:end -->

### [2605.23065 Dithering Defense: Adversarial Robustness of Vision Foundation Models via Multi-Level Floyd-Steinberg Dithering](https://arxiv.org/abs/2605.23065)

<!-- review:SF-2026-ARXIV-2605-23065:start -->
证据位置：5.5 Vision-language model; 5 Results and Discussion; 5 Results and Discussion。
<!-- claim:SF-2026-ARXIV-2605-23065:start -->exact-v1 采用命题：We study multi-level Floyd-Steinberg error-diffusion dithering as a lightweight, model-agnostic input transformation that disrupts adversarial perturbations while preserving semantic content.<!-- claim:SF-2026-ARXIV-2605-23065:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5 Results and Discussion` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从资产与信任边界开始；检测器是 Policy-bound Sensor，不拥有安全判决。
Books：No Change — Existing Coverage；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-23065:end -->

### [2605.23067 What Training Data Teaches RL Memory Agents: An Empirical Study of Curriculum Effects in Memory-Augmented QA](https://arxiv.org/abs/2605.23067)

<!-- review:SF-2026-ARXIV-2605-23067:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23067` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23067:start -->We present a controlled empirical study that holds architecture, RL algorithm, and all hyperparameters fixed and varies only the training curriculum across three conditions: in-domain (LoCoMo), mixed-benchmark (LoCoMo + LongMemEval), and out-of-domain (LongMemEval only).<!-- claim:SF-2026-ARXIV-2605-23067:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23067:end -->

### [2605.23069 DFKI-MLT at SemEval-2026 TASK 7: Steering Multilingual Models Towards Cultural Knowledge](https://arxiv.org/abs/2605.23069)

<!-- review:SF-2026-ARXIV-2605-23069:start -->
证据位置：Track 1: Short Answer Questions (SAQ).; 5 Results and Analysis; 7 Limitations and Future Work。
<!-- claim:SF-2026-ARXIV-2605-23069:start -->exact-v1 采用命题：We present the DFKI-MLT system for SemEval-2026 Task 7 on cultural awareness, where we apply activation steering to multilingual LLMs using language vectors extracted from parallel FLORES data.<!-- claim:SF-2026-ARXIV-2605-23069:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5 Results and Analysis` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23069:end -->

### [2605.23070 Flow Mismatching: Unsupervised Anomaly Detection via Velocity Discrepancies in Flow Matching Models](https://arxiv.org/abs/2605.23070)

<!-- review:SF-2026-ARXIV-2605-23070:start -->
证据位置：3 Flow Mismatching Anomaly Detection Method; Appendix F Qualitative results; no dedicated limitations section; non-proof boundary taken from disclosed method/evaluation scope。
<!-- claim:SF-2026-ARXIV-2605-23070:start -->exact-v1 采用命题：We propose Flow Mismatching, an unsupervised anomaly detection method that deliberately avoids reconstruction-based paradigms.<!-- claim:SF-2026-ARXIV-2605-23070:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `Appendix F Qualitative results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§并行与少步生成必须声明依赖、轨迹和状态边界；Draft、Verify 与 Correct 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23070:end -->

### [2605.23074 PathCal: State-Aware Reflection-Marker Calibration for Efficient Reasoning](https://arxiv.org/abs/2605.23074)

<!-- review:SF-2026-ARXIV-2605-23074:start -->
证据位置：HTML §3 marker interventions; §4 PathCal category/state-aware calibration; HTML §5 Experiments; Appendix E diagnostics; Appendix H cost; HTML §6 Discussion and Conclusion; Appendix H scope。
<!-- claim:SF-2026-ARXIV-2605-23074:start -->把 wait/but/alternatively 等 reflection marker 分型，只在局部不确定、竞争分支证据过强时软调 logits，而非全程固定抑制。<!-- claim:SF-2026-ARXIV-2605-23074:end -->
证据边界、trade-off、failure 与 fallback：训练外控制仍依赖 marker vocabulary、tokenizer 与作者六 benchmark；marker 不是 reasoning truth，过度干预会破坏正确路径，失败时关闭 controller 并回退原 decode。
Books：Applied；owner=INFER-DECODE。
<!-- review:SF-2026-ARXIV-2605-23074:end -->

### [2605.23078 GEMQ: Global Expert-Level Mixed-Precision Quantization for MoE LLMs](https://arxiv.org/abs/2605.23078)

<!-- review:SF-2026-ARXIV-2605-23078:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23078` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23078:start -->MoE quantization 会改变 router 的 expert selection，bit allocation 不能继续逐层独立决定；global expert error budget 与 router recalibration 共同形成 execution-plan revision，内存收益换来全局求解与校准成本。<!-- claim:SF-2026-ARXIV-2605-23078:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23078:end -->

### [2605.23081 ThriftAttention: Selective Mixed Precision for Long-Context FP4 Attention](https://arxiv.org/abs/2605.23081)

<!-- review:SF-2026-ARXIV-2605-23081:start -->
证据位置：PDF ThriftAttention method; PDF experiments; PDF §5 limitations。
<!-- claim:SF-2026-ARXIV-2605-23081:start -->保留完整低精度 attention/KV 路径，只为 query-dependent 少量重要 blocks 晋升精度；selector 与 paired-cache identity 必须一致。<!-- claim:SF-2026-ARXIV-2605-23081:end -->
证据边界、trade-off、failure 与 fallback：作者结果限 consumer Blackwell 与指定模型，5% FP16 headline 不证明 production goodput。Ch45 已逐字承载 selective precision promotion、双路径 kernel/footprint/fallback，并列 ThriftAttention。
Books：No Change — Existing Coverage；owner=INFER-KV-CACHE。
<!-- review:SF-2026-ARXIV-2605-23081:end -->

### [2605.23087 The Implicit Bias of Depth: From Neural Collapse to Softmax Codes](https://arxiv.org/abs/2605.23087)

<!-- review:SF-2026-ARXIV-2605-23087:start -->
证据位置：4.1 The Hadamard Framework; Appendix E Further Numerical Experiments; Limitations:。
<!-- claim:SF-2026-ARXIV-2605-23087:start -->exact-v1 采用命题：We study the deep unconstrained feature model (UFM)-equivalent to a deep linear network with orthogonal inputs-trained without regularization, to isolate how gradient descent and depth alone shape NC.<!-- claim:SF-2026-ARXIV-2605-23087:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `Appendix E Further Numerical Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从可读出到机制：证据应逐级变强——信息存在、可读与被使用是三个不同命题。
Books：No Change — Existing Coverage；owner=WORLDVIEW-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23087:end -->

### [2605.23089 Dreaming Smoothly and Sample Efficiently with Gradient Penalized Latent Dynamics](https://arxiv.org/abs/2605.23089)

<!-- review:SF-2026-ARXIV-2605-23089:start -->
证据位置：Smoothness in reinforcement learning.; Appendix C DMC Proprioceptive Results; 6 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23089:start -->exact-v1 采用命题：We propose GPLD, a gradient-penalized latent dynamics regularizer for DreamerV3 that applies a row-wise Jacobian penalty to the posterior latent distribution to encourage locally smooth transition learning.<!-- claim:SF-2026-ARXIV-2605-23089:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `Appendix C DMC Proprioceptive Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§在谈 State 之前先声明预测 Channel，并把 observation/action truth 与模型假设分开。
Books：No Change — Existing Coverage；owner=MULTIMODAL-WORLD-MODELS。
<!-- review:SF-2026-ARXIV-2605-23089:end -->

### [2605.23091 Security of LLM-generated Code: A Comparative Analysis](https://arxiv.org/abs/2605.23091)

<!-- review:SF-2026-ARXIV-2605-23091:start -->
证据位置：official arXiv PDF §3 Methodology; §3.3 Static Code Analysis; official arXiv PDF §4 Results; official arXiv PDF §3.6 Limitations。
<!-- claim:SF-2026-ARXIV-2605-23091:start -->exact-v1 采用命题：We empirically evaluate the security of code generated by seven popular LLMs.<!-- claim:SF-2026-ARXIV-2605-23091:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `official arXiv PDF §4 Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从资产与信任边界开始；检测器是 Policy-bound Sensor，不拥有安全判决。
Books：No Change — Existing Coverage；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-23091:end -->

### [2605.23099 SVR-MAD: A Bayesian-Inspired Framework for Posterior-Guided Multi-Agent Debate](https://arxiv.org/abs/2605.23099)

<!-- review:SF-2026-ARXIV-2605-23099:start -->
证据位置：HTML §3 prior/posterior signal analysis; §4 SVR-MAD design; HTML §5 Evaluation; Appendix B ablations; HTML Limitations; Ethical considerations。
<!-- claim:SF-2026-ARXIV-2605-23099:start -->把 pre-debate confidence 当 prior、peer challenge outcome 当 posterior-style evidence，增量构造只保留高价值通信的 debate graph。<!-- claim:SF-2026-ARXIV-2605-23099:end -->
证据边界、trade-off、failure 与 fallback：posterior-style score 不是真贝叶斯后验，相关 hallucination 和共享模型盲点仍会稳定误导；预算紧或独立 verifier 可用时回退固定 topology/单 Agent+verification。
Books：No Change — Existing Coverage；owner=AGENT-MULTI-AGENT。
<!-- review:SF-2026-ARXIV-2605-23099:end -->

### [2605.23108 Philosophical Dispositions as Behavioral Constraints for AI-Assisted Code Review: An Empirical Study](https://arxiv.org/abs/2605.23108)

<!-- review:SF-2026-ARXIV-2605-23108:start -->
证据位置：IV-A Methodology; IV-C Results; VII Threats to Validity。
<!-- claim:SF-2026-ARXIV-2605-23108:start -->exact-v1 采用命题：We present a system that constrains AI reviewer behavior through philosophical dispositions -- coherent personality lenses grounded in specific epistemological traditions (Pyrrhonist Skepticism, Navya-Ny=aya logic, Diogenes' Cynicism, Confucian relational ethics) that direct attention to structurally different types of issues.<!-- claim:SF-2026-ARXIV-2605-23108:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `IV-C Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23108:end -->

### [2605.23109 Inductive Deductive Synthesis: Enabling AI to Generate Formally Verified Systems](https://arxiv.org/abs/2605.23109)

<!-- review:SF-2026-ARXIV-2605-23109:start -->
证据位置：PDF §3–§4 IDS synthesis; PDF §5 and Appendix E evaluation; PDF main limitations; Appendix H。
<!-- claim:SF-2026-ARXIV-2605-23109:start -->把 LLM synthesis proposal 与 Rocq specification/proof kernel 交替执行，只有独立 checker 能把候选升级为 verified artifact。<!-- claim:SF-2026-ARXIV-2605-23109:end -->
证据边界、trade-off、failure 与 fallback：依赖形式规格、Rocq 环境与受测 benchmark；proof 不覆盖现实语义映射。Ch78 已规定 tool evidence 与 formal proof 在 typed claim 汇合、失败时 Abstain。
Books：No Change — Existing Coverage；owner=AGENT-TOOL-CALLING。
<!-- review:SF-2026-ARXIV-2605-23109:end -->

### [2605.23113 Inconsistency-aware Multimodal Schrödinger Bridge for Deepfake Localization](https://arxiv.org/abs/2605.23113)

<!-- review:SF-2026-ARXIV-2605-23113:start -->
证据位置：3 Method; 4 Experiments; 5 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23113:start -->exact-v1 采用命题：We present IaMSB, an inconsistency-aware multimodal Schrödinger Bridge (SB) that jointly estimates cross-modal consistency and performs interval-level localization.<!-- claim:SF-2026-ARXIV-2605-23113:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§并行与少步生成必须声明依赖、轨迹和状态边界；Draft、Verify 与 Correct 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23113:end -->

### [2605.23116 CoReVAD: A Contextual Reasoning Framework for Training-Free Video Anomaly Detection](https://arxiv.org/abs/2605.23116)

<!-- review:SF-2026-ARXIV-2605-23116:start -->
证据位置：3 Methodology; 4.5 Qualitative Results; 5 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23116:start -->exact-v1 采用命题：To address these challenges, we propose CoReVAD, a contextual reasoning framework for training-free video anomaly detection that operates with a single frozen VLM.<!-- claim:SF-2026-ARXIV-2605-23116:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4.5 Qualitative Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23116:end -->

### [2605.23141 VisAnalog: A Diagnostic Suite for Visual Concept Transfer on Natural Images](https://arxiv.org/abs/2605.23141)

<!-- review:SF-2026-ARXIV-2605-23141:start -->
证据位置：3 VisAnalog : Task and Construction; 4.1 Main benchmark results; 5 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23141:start -->exact-v1 采用命题：We introduce VisAnalog, a controlled suite for this setting on natural images.<!-- claim:SF-2026-ARXIV-2605-23141:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4.1 Main benchmark results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23141:end -->

### [2605.23147 As X, Do Y: How Persona and Task Combine in Instruction-Tuned LLMs](https://arxiv.org/abs/2605.23147)

<!-- review:SF-2026-ARXIV-2605-23147:start -->
证据位置：HTML §3–§5 persona/task representation analyses; HTML experiments; HTML discussion/limitations。
<!-- claim:SF-2026-ARXIV-2605-23147:start -->persona 与 task 在局部 residual site 上近似可加，不推出 persona prompt 可被单一 activation 或短 prefix 压缩；功能状态可能跨 token、层与 KV 分布。<!-- claim:SF-2026-ARXIV-2605-23147:end -->
证据边界、trade-off、failure 与 fallback：受测 instruction-tuned models/personas 不证明统一线性控制。Ch14 已明确单位置可读不等于单位置控制，task template 可能跨 demo positions、层和 residual 路径共同承载。
Books：No Change — Existing Coverage；owner=MODEL-SELF-ATTENTION。
<!-- review:SF-2026-ARXIV-2605-23147:end -->

### [2605.23156 Any-Dimensional Invariant Universality](https://arxiv.org/abs/2605.23156)

<!-- review:SF-2026-ARXIV-2605-23156:start -->
证据位置：HTML §3 any-dimensional invariant-universality recipe; HTML §4 instantiations over sets, sequences and measures; HTML theorem assumptions and appendices; no finite-data or optimization guarantee。
<!-- claim:SF-2026-ARXIV-2605-23156:start -->exact-v1 采用命题：We develop a systematic approach to establish any-dimensional universality, by identifying any-dimensional functions with a unique function taking inputs in a suitable infinite-dimensional limit space containing inputs of all finite sizes as well as their limits.<!-- claim:SF-2026-ARXIV-2605-23156:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `no standalone evaluation section; exact-v1 stated theorem/method scope reviewed` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从可读出到机制：证据应逐级变强——信息存在、可读与被使用是三个不同命题。
Books：No Change — Existing Coverage；owner=WORLDVIEW-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23156:end -->

### [2605.23157 Same Model, Different Weakness: How Language and Modality Reshape the Jailbreak Attack Surface in Frontier MLLMs](https://arxiv.org/abs/2605.23157)

<!-- review:SF-2026-ARXIV-2605-23157:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23157` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23157:start -->We present the first systematic cross-lingual, multimodal red-teaming study comparing jailbreak vulnerability in US English (en-US) and Mexican Spanish (es-MX) across four frontier MLLMs: Claude Sonnet 4.5, GPT-5, Pixtral Large, and Qwen Omni.<!-- claim:SF-2026-ARXIV-2605-23157:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23157:end -->

### [2605.23158 What Does the Server See? Understanding Privacy Leakage from Large Language Models in Split Inference](https://arxiv.org/abs/2605.23158)

<!-- review:SF-2026-ARXIV-2605-23158:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23158` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23158:start -->To fill this gap, we introduce ActInv, which solves an intermediate activation matching problem to reconstruct the client's input.<!-- claim:SF-2026-ARXIV-2605-23158:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23158:end -->

### [2605.23168 PoisonForge: Task-Level Targeted Poisoning Benchmark for Instruction-Tuned LLMs](https://arxiv.org/abs/2605.23168)

<!-- review:SF-2026-ARXIV-2605-23168:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23168` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23168:start -->We introduce PoisonForge, a benchmark that parameterizes this threat along four dimensions (bias type, poisoning mode, appearance count, and target output length) and evaluates 12 open-weight models (from 2B to 32B parameters) across five families under a primarily 1% poison budget.<!-- claim:SF-2026-ARXIV-2605-23168:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23168:end -->

### [2605.23170 Positional Failures in Long-Context LLMs: A Blind Spot in Reasoning Benchmarks](https://arxiv.org/abs/2605.23170)

<!-- review:SF-2026-ARXIV-2605-23170:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23170` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23170:start -->We propose Context Rot Evaluation (CRE), a controlled framework varying all three factors, and evaluate nine LLMs on GSM8K and ARC-Challenge across two rounds: an initial five-model set and four newer vendor releases.<!-- claim:SF-2026-ARXIV-2605-23170:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23170:end -->

### [2605.23171 Understanding and Improving Noisy Embedding Techniques in Instruction Finetuning](https://arxiv.org/abs/2605.23171)

<!-- review:SF-2026-ARXIV-2605-23171:start -->
证据位置：HTML §3 noise-distribution analysis; §4 SymNoise; HTML §5 Experiments; §5.4–§5.5 results/analysis; HTML §6 Conclusion; Appendix A/B scope and proofs。
<!-- claim:SF-2026-ARXIV-2605-23171:start -->用对称 embedding noise 更严格地正则局部曲率，把 instruction tuning 的 noise distribution 作为可版本化训练状态，而不是只记录 noise norm。<!-- claim:SF-2026-ARXIV-2605-23171:end -->
证据边界、trade-off、failure 与 fallback：证据限 LLaMA-2-7B、披露 instruction sets 与 AlpacaEval/OpenLLM；大幅分数受 evaluator/response length 影响，退化时回退无噪 SFT、NEFTune 或更小 noise。
Books：Applied；owner=TRAIN-SFT。
<!-- review:SF-2026-ARXIV-2605-23171:end -->

### [2605.23175 Robust LLM Watermarking with Minimal Semantic Distortion for IP Protection](https://arxiv.org/abs/2605.23175)

<!-- review:SF-2026-ARXIV-2605-23175:start -->
证据位置：HTML §3 Threat Models; §4 SafeSeal generation/detection/bounds; HTML §5 Experiments; Appendix D attacks/cross-provider/latency; HTML §6 Conclusion and Future Work; Appendix D tested attacks。
<!-- claim:SF-2026-ARXIV-2605-23175:start -->水印身份绑定 provider/user key：generation 用 key-conditioned synonym tournament 保留实体，detector 联合编码 text+key，以 provider-specific verification 替代全局无主 watermark。<!-- claim:SF-2026-ARXIV-2605-23175:end -->
证据边界、trade-off、failure 与 fallback：同义替换仍会造成语义/风格漂移，detector 对改写与跨域分布敏感，key lifecycle/rotation 泄漏未由 benchmark 证明；高风险归属回退签名、日志与人工取证。
Books：Applied；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-23175:end -->

### [2605.23178 Composing People Together: Iterative Pose-Image Generation for Multi-Person Interaction Scenes](https://arxiv.org/abs/2605.23178)

<!-- review:SF-2026-ARXIV-2605-23178:start -->
证据位置：3. Method; 4. Experiments; C.7. Failure Cases and Limitations。
<!-- claim:SF-2026-ARXIV-2605-23178:start -->exact-v1 采用命题：Despite recent progress, text-to-image models still struggle to generate semantically diverse and compositionally accurate multi-person interaction scenes, often collapsing to repetitive layouts, stereotypical poses, and poorly grounded interactions.<!-- claim:SF-2026-ARXIV-2605-23178:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4. Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§并行与少步生成必须声明依赖、轨迹和状态边界；Draft、Verify 与 Correct 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23178:end -->

### [2605.23179 Redrawing the AI Map: A Theory of Accountability Boundaries in Agentic Ecosystems](https://arxiv.org/abs/2605.23179)

<!-- review:SF-2026-ARXIV-2605-23179:start -->
证据位置：HTML §§3–7 boundary-shift theory and propositions; HTML §8 structured theoretical illustrations; HTML §10 Limitations and Future Research。
<!-- claim:SF-2026-ARXIV-2605-23179:start -->exact-v1 采用命题：We develop a capability-level theory of accountability-boundary placement in agentic ecosystems.<!-- claim:SF-2026-ARXIV-2605-23179:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `no standalone evaluation section; exact-v1 stated theorem/method scope reviewed` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：Report Only；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23179:end -->

### [2605.23180 Self-Improving In-Context Learning](https://arxiv.org/abs/2605.23180)

<!-- review:SF-2026-ARXIV-2605-23180:start -->
证据位置：HTML §4 Self-Improving ICL; §4.1 confidence proxy; §4.2 calibration; HTML §5 Experiments; §5.2 correlation; §5.3 ablations; HTML §6 Conclusion — Limitations。
<!-- claim:SF-2026-ARXIV-2605-23180:start -->用单次 forward 得到的 demonstration-output likelihood 构造 bounded self-supervised proxy，再以 zeroth-order optimization 更新固定 few-shot prompt embeddings。<!-- claim:SF-2026-ARXIV-2605-23180:end -->
证据边界、trade-off、failure 与 fallback：proxy 相关不等于 correctness，test-time forward/optimization 增加延迟且连续 embedding 难审计；相关性或 regression gate 失效时回退离散 prompt、固定 demonstrations。
Books：Applied；owner=AGENT-PROMPT。
<!-- review:SF-2026-ARXIV-2605-23180:end -->

### [2605.23187 IntentionNav: A Benchmark for Intent-Driven Object Navigation from Implicit Human Instruction](https://arxiv.org/abs/2605.23187)

<!-- review:SF-2026-ARXIV-2605-23187:start -->
证据位置：4 Evaluation Framework; 5.1 Main results; 6 Conclusions。
<!-- claim:SF-2026-ARXIV-2605-23187:start -->exact-v1 采用命题：We study this setting as intent-driven object navigation and introduce IntentionNav, a diagnostic benchmark for active object search from implicit human instructions.<!-- claim:SF-2026-ARXIV-2605-23187:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5.1 Main results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23187:end -->

### [2605.23189 Empirical Bayes Conformal Prediction for Vision and Language Models](https://arxiv.org/abs/2605.23189)

<!-- review:SF-2026-ARXIV-2605-23189:start -->
证据位置：HTML §3 r-value construction; §3.4 coverage/set-size analysis; HTML §§4–5 vision/VLM/LLM coverage experiments; HTML §7 Conclusion; Appendix B compute; Appendix C assumptions/proofs。
<!-- claim:SF-2026-ARXIV-2605-23189:start -->把重复 score 的均值与方差通过 empirical-Bayes r-value 写入 conformal nonconformity，在保持声明 coverage 的同时降低高方差伪候选。<!-- claim:SF-2026-ARXIV-2605-23189:end -->
证据边界、trade-off、failure 与 fallback：依赖 exchangeability、posterior/parametric assumptions 与重复评分成本；variance 不含信息时退化为普通 CP，分布变化时必须重校准并回退标准 conformal set。
Books：Applied；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23189:end -->

### [2605.23190 Hidden Human-Like Nature of Machine-Generated Texts: Theory and Detection Enhancement](https://arxiv.org/abs/2605.23190)

<!-- review:SF-2026-ARXIV-2605-23190:start -->
证据位置：IV Proposed Method; V Experiments; VI Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23190:start -->exact-v1 采用命题：To this end, we first reveal the existence of such hidden human-like spans, and then theoretically analyze their impact on detection.<!-- claim:SF-2026-ARXIV-2605-23190:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `V Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23190:end -->

### [2605.23196 Prompt Overflow: What the Guardrail Inspects Is Not What the Model Infers](https://arxiv.org/abs/2605.23196)

<!-- review:SF-2026-ARXIV-2605-23196:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23196` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23196:start -->In this paper, we identify a critical blind spot arising from the mismatch between the limited inspection windows of guardrail models and the substantially larger context inference windows of downstream LLMs.<!-- claim:SF-2026-ARXIV-2605-23196:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23196:end -->

### [2605.23198 Label-Efficient Dataset Pruning via Semi-Supervised Pseudo-Labeling](https://arxiv.org/abs/2605.23198)

<!-- review:SF-2026-ARXIV-2605-23198:start -->
证据位置：3 Methodology; Appendix C Additional Ablation Results; 3.2 Limitations of Deep-clustering-based Pseudo-labeling。
<!-- claim:SF-2026-ARXIV-2605-23198:start -->exact-v1 采用命题：We propose SemiPrune, a label-efficient dataset pruning framework, using only a small randomly labeled subset, that uses semi-supervised learning to generate pseudo-labels for unlabeled data, allowing existing supervised pruning methods that require label information to be seamlessly applied to the resulting pseudo-labeled training pool.<!-- claim:SF-2026-ARXIV-2605-23198:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `Appendix C Additional Ablation Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Supervision Granularity 应跟随可验证的状态边界；dataset revision 与 coverage contract 必须可重放。
Books：No Change — Existing Coverage；owner=TRAIN-DATA。
<!-- review:SF-2026-ARXIV-2605-23198:end -->

### [2605.23200 Adaptive Mass-Segmented KV Compression for Long-Context Reasoning](https://arxiv.org/abs/2605.23200)

<!-- review:SF-2026-ARXIV-2605-23200:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23200` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23200:start -->However, we show that their reliance on global Top-k selection triggers Region Wipe-out: the severe eviction of contiguous reasoning blocks that derails logical coherence.<!-- claim:SF-2026-ARXIV-2605-23200:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23200:end -->

### [2605.23201 MixFake: Benchmarking and Enhancing Audio Deepfake Detection in Diverse Real-world Mixed Audio](https://arxiv.org/abs/2605.23201)

<!-- review:SF-2026-ARXIV-2605-23201:start -->
证据位置：III Proposed Methodology; IV Experiments; V Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23201:start -->exact-v1 采用命题：In this paper, we first introduce MixFake, a large-scale benchmark dataset designed to simulate diverse acoustic environments with varying SNR levels and mixed authenticity components.<!-- claim:SF-2026-ARXIV-2605-23201:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `IV Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23201:end -->

### [2605.23203 Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)

<!-- review:SF-2026-ARXIV-2605-23203:start -->
证据位置：3 Method; 17 Extended results; no dedicated limitations section; non-proof boundary taken from disclosed method/evaluation scope。
<!-- claim:SF-2026-ARXIV-2605-23203:start -->exact-v1 采用命题：We present a formal verification approach that targets robustness against 3D motion perturbations of the capturing camera.<!-- claim:SF-2026-ARXIV-2605-23203:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `17 Extended results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23203:end -->

### [2605.23215 FastKernels: Benchmarking GPU Kernel Generation in Production](https://arxiv.org/abs/2605.23215)

<!-- review:SF-2026-ARXIV-2605-23215:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23215` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23215:start -->The resulting reward signals are misleading: agents learn to generate kernels that score well in sandboxes but introduce interface incompatibilities, compilation-stack conflicts, and silent correctness degradation when integrated into real systems.<!-- claim:SF-2026-ARXIV-2605-23215:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23215:end -->

### [2605.23218 Foundation Protocol: A Coordination Layer for Agentic Society](https://arxiv.org/abs/2605.23218)

<!-- review:SF-2026-ARXIV-2605-23218:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23218` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23218:start -->Autonomous agents are moving from tools into a layer of social infrastructure: they browse, purchase, deploy software, manage systems, and increasingly interact with one another.<!-- claim:SF-2026-ARXIV-2605-23218:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23218:end -->

### [2605.23220 WMAttack: Automated Attack Search for Adversarial Evaluation of World-Model Agents](https://arxiv.org/abs/2605.23220)

<!-- review:SF-2026-ARXIV-2605-23220:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23220` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23220:start -->We introduce WMAttack, an automated attack-search framework for adversarial evaluation of world-model agents.<!-- claim:SF-2026-ARXIV-2605-23220:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23220:end -->

### [2605.23226 MASQ: Accelerating Masked Diffusion via Stage-Wise Multi-Precision Quantization](https://arxiv.org/abs/2605.23226)

<!-- review:SF-2026-ARXIV-2605-23226:start -->
证据位置：HTML §§3–4 stage-wise precision algorithm and accelerator architecture; HTML §5 Evaluation; §5.2–§5.4 quality/performance/area-power; HTML §6 Conclusion — A100/Orin/accelerator-model boundary。
<!-- claim:SF-2026-ARXIV-2605-23226:start -->masked diffusion 按 spatial/semantic importance 与 timestep 分配 MXINT8/4/2，并让 mask manager、non-matrix ops 和 multi-precision engine 共享执行计划。<!-- claim:SF-2026-ARXIV-2605-23226:end -->
证据边界、trade-off、failure 与 fallback：speed/energy 结果依赖作者 hardware model、A100/Orin comparisons 与受测 image task；量化误差或 mask drift 时回退较高精度/全图计算。当前 ROADMAP 无生成 accelerator co-design 唯一 owner。
Books：Structural Candidate；owner=尚无唯一 owner。
<!-- review:SF-2026-ARXIV-2605-23226:end -->

### [2605.23238 GENSTRAT: Toward a Science of Strategic Reasoning in Large Language Models](https://arxiv.org/abs/2605.23238)

<!-- review:SF-2026-ARXIV-2605-23238:start -->
证据位置：3 Generalized betting games and GENSTRAT; 6 Overall results; 10 Limitations and discussion。
<!-- claim:SF-2026-ARXIV-2605-23238:start -->exact-v1 采用命题：We introduce GENSTRAT, which uses procedurally generated strategic environments to address these challenges.<!-- claim:SF-2026-ARXIV-2605-23238:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `6 Overall results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23238:end -->

### [2605.23244 Convex Optimization for Alignment and Preference Learning on a Single GPU](https://arxiv.org/abs/2605.23244)

<!-- review:SF-2026-ARXIV-2605-23244:start -->
证据位置：HTML §4 COALA convex preference framework/algorithm/guarantees; HTML §5 Experiments; §6.1–§6.5 quality and compute; HTML §6.6 Expressiveness Tradeoff; §7 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23244:start -->用两层 ReLU convex reformulation 与 CRONOS/ADMM 训练 reference-free preference policy，将 reference forward 与大规模超参搜索换成受限凸表达。<!-- claim:SF-2026-ARXIV-2605-23244:end -->
证据边界、trade-off、failure 与 fallback：凸性属于 reformulated policy class，不等于完整 LLM objective 全局凸；表达力、feature construction 与单 GPU 结果限制外推，失配时回退标准 DPO/ORPO 与 reference logprobs。
Books：Applied；owner=TRAIN-DPO。
<!-- review:SF-2026-ARXIV-2605-23244:end -->

### [2605.23245 SimInsert: Seamless Video Object Insertion via Regional Sparse Attention Fusion](https://arxiv.org/abs/2605.23245)

<!-- review:SF-2026-ARXIV-2605-23245:start -->
证据位置：III Method; IV-B Quantitative Results; V Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23245:start -->exact-v1 采用命题：To bridge this gap, we present \textit{SimInsert}, a training-free paradigm that efficiently decouples the task into intuitive single-frame editing and semantic motion description.<!-- claim:SF-2026-ARXIV-2605-23245:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `IV-B Quantitative Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§并行与少步生成必须声明依赖、轨迹和状态边界；Draft、Verify 与 Correct 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23245:end -->

### [2605.23249 Enhancing Deep Neural Network Reliability with Refinement and Calibration](https://arxiv.org/abs/2605.23249)

<!-- review:SF-2026-ARXIV-2605-23249:start -->
证据位置：3 Proposed methodology; 6 Results; no dedicated limitations section; non-proof boundary taken from disclosed method/evaluation scope。
<!-- claim:SF-2026-ARXIV-2605-23249:start -->exact-v1 采用命题：To address this limitation, we propose: (1) a novel loss function that explicitly promotes refinement and can be optimized through supervised contrastive learning; and (2) a unified training framework, RefCal, that jointly optimizes calibration, refinement, and accuracy to improve DNN reliability.<!-- claim:SF-2026-ARXIV-2605-23249:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `6 Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23249:end -->

### [2605.23254 CARE: Class-Adaptive Expert Consensus for Reliable Learning with Long-Tailed Noisy Labels](https://arxiv.org/abs/2605.23254)

<!-- review:SF-2026-ARXIV-2605-23254:start -->
证据位置：2 Proposed Method; 3.2 Main Comparison Results 2 2 footnotemark: 2; Appendix P Limitation Analysis & Future Work。
<!-- claim:SF-2026-ARXIV-2605-23254:start -->exact-v1 采用命题：To address this issue, we propose Class-Adaptive Rectification with Experts (CARE), a parameter-efficient framework that leverages three complementary supervision sources from vision-language models (VLM): observed noisy labels, VLM text embeddings, and visual features.<!-- claim:SF-2026-ARXIV-2605-23254:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `3.2 Main Comparison Results 2 2 footnotemark: 2` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§任务贡献与当前可靠性不能共用一个 Gate；感知、写入、读取与行动使用必须分开验证。
Books：No Change — Existing Coverage；owner=MULTIMODAL-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23254:end -->

### [2605.23257 Turning Adaptation into Assets: Cross-Domain Bridging for Online Vision-Language Navigation](https://arxiv.org/abs/2605.23257)

<!-- review:SF-2026-ARXIV-2605-23257:start -->
证据位置：4 Methodology; 5.2 Main Results; no dedicated limitations section; non-proof boundary taken from disclosed method/evaluation scope。
<!-- claim:SF-2026-ARXIV-2605-23257:start -->exact-v1 采用命题：To overcome these issues, we propose Inter-Domain BridgE with Historical Assets (IDEA), a novel TTA framework that transforms adaptation into the accumulation and composition of assets.<!-- claim:SF-2026-ARXIV-2605-23257:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5.2 Main Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§VLA 闭环把 observation revision、action schema、controller authority 与真实 environment transition 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-EMBODIED-VLA。
<!-- review:SF-2026-ARXIV-2605-23257:end -->

### [2605.23258 A Simple Plug-in for Improving Eviction-Based KV Cache Compression](https://arxiv.org/abs/2605.23258)

<!-- review:SF-2026-ARXIV-2605-23258:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23258` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23258:start -->We present VECTOR, a plug-and-play augmentation for eviction-based pipelines that introduces three-way token routing: retention, approximation, and eviction.<!-- claim:SF-2026-ARXIV-2605-23258:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23258:end -->

### [2605.23259 Multi-Gate Residuals](https://arxiv.org/abs/2605.23259)

<!-- review:SF-2026-ARXIV-2605-23259:start -->
证据位置：HTML §3 Methodology; §3.1 architecture; §3.2 stability; HTML §4 Experiment and Analysis; §4.4 efficiency; HTML §5 Conclusion and Discussion。
<!-- claim:SF-2026-ARXIV-2605-23259:start -->用 multi-stream context、轻量 gating 与 attention pooling 稳定深层 residual activation，在不增加跨设备 attention-residual 通信的条件下提供可训练多路残差状态。<!-- claim:SF-2026-ARXIV-2605-23259:end -->
证据边界、trade-off、failure 与 fallback：多流状态、gate 初始化、fusion/recompute 增加内存与 kernel 复杂度；证据限作者训练规模，门控坍缩或通信/质量收益不闭合时回退普通 residual/Attention Residual。
Books：Applied；owner=MODEL-TRANSFORMER-LAYER。
<!-- review:SF-2026-ARXIV-2605-23259:end -->

### [2605.23261 UniSRM: A Unified Speech Reward Model for Reasoning-Based Fine-grained Assessment](https://arxiv.org/abs/2605.23261)

<!-- review:SF-2026-ARXIV-2605-23261:start -->
证据位置：4 Method; 5.2 Main Results; Limitations。
<!-- claim:SF-2026-ARXIV-2605-23261:start -->exact-v1 采用命题：In this work, we propose UniSRM, a unified speech reward model that can support multi-dimensional, interpretable reward signals with reliable reasoning.<!-- claim:SF-2026-ARXIV-2605-23261:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5.2 Main Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Reward Model、policy objective 与独立 outcome evidence 分责；PPO 没有解决 Reward correctness。
Books：No Change — Existing Coverage；owner=TRAIN-RLHF。
<!-- review:SF-2026-ARXIV-2605-23261:end -->

### [2605.23270 ChainFlow-VLA: Causal Flow Planning with Vision-Language Models](https://arxiv.org/abs/2605.23270)

<!-- review:SF-2026-ARXIV-2605-23270:start -->
证据位置：3 Preliminaries; 5.2 Main Results; 6 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23270:start -->exact-v1 采用命题：To address this, we propose ChainFlow-VLA, which unifies causal generation and global refinement within a unified probabilistic framework.<!-- claim:SF-2026-ARXIV-2605-23270:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5.2 Main Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§VLA 闭环把 observation revision、action schema、controller authority 与真实 environment transition 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-EMBODIED-VLA。
<!-- review:SF-2026-ARXIV-2605-23270:end -->

### [2605.23271 EvalVerse: Pipeline-Aware and Expert-Calibrated Benchmarking for Professional Cinematic Video Generation](https://arxiv.org/abs/2605.23271)

<!-- review:SF-2026-ARXIV-2605-23271:start -->
证据位置：2.1 Generative Video Foundation Model; 5 Benchmark: Expert Evaluation Results; 7.2.2 Discussion: The Complementary Synergy of CoT and SFT。
<!-- claim:SF-2026-ARXIV-2605-23271:start -->exact-v1 采用命题：To bridge this gap, we introduce EvalVerse, a comprehensive, pipeline-aware, and expert-calibrated evaluation framework.<!-- claim:SF-2026-ARXIV-2605-23271:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5 Benchmark: Expert Evaluation Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23271:end -->

### [2605.23275 Diffusion Domain Expansion: Learning to Coordinate Pre-trained Diffusion Models](https://arxiv.org/abs/2605.23275)

<!-- review:SF-2026-ARXIV-2605-23275:start -->
证据位置：3 Method; 4 Experiments; 5 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23275:start -->exact-v1 采用命题：In this paper, we propose Diffusion Domain Expansion (DDE), a method that efficiently extends pre-trained diffusion models to generate larger objects and handle more complex conditioning beyond their original capabilities.<!-- claim:SF-2026-ARXIV-2605-23275:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§并行与少步生成必须声明依赖、轨迹和状态边界；Draft、Verify 与 Correct 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23275:end -->

### [2605.23281 DepthAgent: Towards Better Universal Depth Estimation via Sample-wise Expert Selection](https://arxiv.org/abs/2605.23281)

<!-- review:SF-2026-ARXIV-2605-23281:start -->
证据位置：3 Method Overview; 4.1 Experimental Results; 5 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23281:start -->exact-v1 采用命题：In this paper, we show that depth experts exhibit strong sample-wise complementarity: model preference is highly correlated with camera geometry, and multi-model fusion brings the largest gains on difficult samples where individual experts are unreliable.<!-- claim:SF-2026-ARXIV-2605-23281:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4.1 Experimental Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§模型输出只是 Proposal；Tool Contract、side-effect class 与独立 Outcome Contract 拥有 commit。
Books：No Change — Existing Coverage；owner=AGENT-TOOL-CALLING。
<!-- review:SF-2026-ARXIV-2605-23281:end -->

### [2605.23287 LangFlash: Feed-forward 3D Language Gaussian Splatting from Sparse Unposed Images](https://arxiv.org/abs/2605.23287)

<!-- review:SF-2026-ARXIV-2605-23287:start -->
证据位置：3 Method; 4 Experiments; 5 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23287:start -->exact-v1 采用命题：We present LangFlash, a feed-forward framework for 3D Language Gaussian Splatting that reconstructs 3D scenes parameterized by Gaussian primitives enriched with language-aligned semantic features from sparse unposed multi-view images.<!-- claim:SF-2026-ARXIV-2605-23287:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§并行与少步生成必须声明依赖、轨迹和状态边界；Draft、Verify 与 Correct 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23287:end -->

### [2605.23288 Spatio-Temporal Similarity Volume Aggregation for Open-Vocabulary Action Recognition](https://arxiv.org/abs/2605.23288)

<!-- review:SF-2026-ARXIV-2605-23288:start -->
证据位置：2 Method; 3.1 Main Results; 5 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23288:start -->exact-v1 采用命题：We propose Similarity Volume Aggregation (SimVA), a framework that constructs a dense 4D spatio-temporal similarity volume from patch-level visual-text similarities.<!-- claim:SF-2026-ARXIV-2605-23288:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `3.1 Main Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§任务贡献与当前可靠性不能共用一个 Gate；感知、写入、读取与行动使用必须分开验证。
Books：No Change — Existing Coverage；owner=MULTIMODAL-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23288:end -->

### [2605.23294 NASiC: 3D NAND-based CAM-Selected Multibit CIM Architecture for Efficient On-Device Mixture-of-Experts LLM Inference](https://arxiv.org/abs/2605.23294)

<!-- review:SF-2026-ARXIV-2605-23294:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23294` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23294:start -->With extensive experimental results, we demonstrate NASiC achieves 4-114.8x improved performance and 3.9-70x improved energy efficiency over state-of-the-art designs, along with high accuracy, showing its great potential for efficient on-device MoE LLM inference.<!-- claim:SF-2026-ARXIV-2605-23294:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23294:end -->

### [2605.23296 Parallel Context Compaction for Long-Horizon LLM Agent Serving](https://arxiv.org/abs/2605.23296)

<!-- review:SF-2026-ARXIV-2605-23296:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23296` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23296:start -->We introduce \textbf{parallel compaction} for long-horizon agentic flows and characterize it against the sequential synchronous baseline across four backbones spanning 8B to 120B parameters, mixing dense and MoE architectures with reasoning and non-reasoning models, on the HotpotQA multi-hop QA and LoCoMo long-context dialogue benchmarks.<!-- claim:SF-2026-ARXIV-2605-23296:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23296:end -->

### [2605.23297 Ontological Knowledge Blocks: Executable Compliance and Profile-Based Validation for Trustworthy AI Systems](https://arxiv.org/abs/2605.23297)

<!-- review:SF-2026-ARXIV-2605-23297:start -->
证据位置：IV Methodology; VII-A Experimental Setup; VIII Discussion。
<!-- claim:SF-2026-ARXIV-2605-23297:start -->exact-v1 采用命题：This paper introduces Ontological Knowledge Blocks (OKBs), a programmable governance infrastructure that compiles regulatory obligations into machine-checkable constraints over structured evidence graphs.<!-- claim:SF-2026-ARXIV-2605-23297:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `VII-A Experimental Setup` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从资产与信任边界开始；检测器是 Policy-bound Sensor，不拥有安全判决。
Books：No Change — Existing Coverage；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-23297:end -->

### [2605.23311 DART: Semantic Recoverability for Structured Tool Agents](https://arxiv.org/abs/2605.23311)

<!-- review:SF-2026-ARXIV-2605-23311:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23311` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23311:start -->We formalize this gap as semantic recoverability and address it in DART, a modular runtime that localizes the failed instance, certifies semantically recoverable boundaries of that instance, aligns checkpoints to those boundaries, and selects an admissible restore point that preserves committed downstream work under dependency and effect constraints-or blocks otherwise.<!-- claim:SF-2026-ARXIV-2605-23311:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23311:end -->

### [2605.23315 Convergence Without Understanding: When Language Models Agree on Representations but Disagree on Reasoning](https://arxiv.org/abs/2605.23315)

<!-- review:SF-2026-ARXIV-2605-23315:start -->
证据位置：HTML §2 Methodology; §2.3 transfer probes and causal ablation; HTML §3 Results; Appendix B robustness checks; HTML §§4–6 Discussion/Conclusion/Limitations。
<!-- claim:SF-2026-ARXIV-2605-23315:start -->跨模型 CKA/transfer probe 的表示收敛可与 generation-stage divergence、低 causal flip rate 同时出现；可解码共享信息不等于共享 reasoning mechanism。<!-- claim:SF-2026-ARXIV-2605-23315:end -->
证据边界、trade-off、failure 与 fallback：16 模型、800 reasoning problems 与所选 ablations 不证明所有模型家族；CKA 与 probe 都受层对齐/任务影响，机制声明失败时降级为描述性 similarity。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23315:end -->

### [2605.23330 Security, Privacy, and Ethical Risks in OpenClaw](https://arxiv.org/abs/2605.23330)

<!-- review:SF-2026-ARXIV-2605-23330:start -->
证据位置：HTML §3 threat model and security risks; HTML §§3.3–6 defense assessment, privacy, ethics, reliability and traceability; HTML §7 Future Works; §8 Conclusion; survey evidence only。
<!-- claim:SF-2026-ARXIV-2605-23330:start -->exact-v1 采用命题：This paper systematically investigates the security, privacy, and ethical risks, as well as the traceability challenges of OpenClaw, a locally executable AI agent system for natural language interaction and real-world task completion.<!-- claim:SF-2026-ARXIV-2605-23330:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `no standalone evaluation section; exact-v1 stated theorem/method scope reviewed` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：Report Only；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23330:end -->

### [2605.23341 Sparse Compositional Flow Matching by geometric assembly from motion primitives](https://arxiv.org/abs/2605.23341)

<!-- review:SF-2026-ARXIV-2605-23341:start -->
证据位置：3 Method; 4 Experiments; 5 Discussion and Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23341:start -->exact-v1 采用命题：Embodied trajectories, such as the executable motion sequences of robotic manipulators, underwater vehicles, and mobile robots, are a fundamental output of embodied AI.<!-- claim:SF-2026-ARXIV-2605-23341:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§并行与少步生成必须声明依赖、轨迹和状态边界；Draft、Verify 与 Correct 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23341:end -->

### [2605.23344 CHASD: Language Increment-Calibrated Contrastive Decoding against Hallucination in LVLMs](https://arxiv.org/abs/2605.23344)

<!-- review:SF-2026-ARXIV-2605-23344:start -->
证据位置：HTML §3 CHASD; §3.2.1 uncertainty gate; §3.2.2 localized perturbation; HTML §4 Experiments; §4.3 ablation; HTML Appendix B Limitations; Appendix C complexity。
<!-- claim:SF-2026-ARXIV-2605-23344:start -->只在 next-token 低置信时开启负视觉分支，并按当前 attention salient tokens 做局部扰动，使 contrastive hallucination calibration 成为按 token 条件计算。<!-- claim:SF-2026-ARXIV-2605-23344:end -->
证据边界、trade-off、failure 与 fallback：confidence/attention 不是视觉 truth，阈值和扰动可删除真实证据；额外 branch 增加延迟，失配时回退原分布、全局视觉核验或外部 grounding checker。
Books：Applied；owner=MULTIMODAL-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23344:end -->

### [2605.23346 Contrastive Distribution Matching for Amortized Sequential Monte Carlo in Discrete Diffusion](https://arxiv.org/abs/2605.23346)

<!-- review:SF-2026-ARXIV-2605-23346:start -->
证据位置：2 Preliminary: Discrete Diffusion; Appendix E Additional Results; 7 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23346:start -->exact-v1 采用命题：To overcome this limitation, we introduce Contrastive Distribution Matching (CDM), a novel framework that amortizes the cost of SMC inference by learning a parameterized twist function via positive and negative samples.<!-- claim:SF-2026-ARXIV-2605-23346:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `Appendix E Additional Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§并行与少步生成必须声明依赖、轨迹和状态边界；Draft、Verify 与 Correct 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23346:end -->

### [2605.23351 Prudent-Banker: No Extra Fees for Baseline Safety in Adversarial Bandits With and Without Delays](https://arxiv.org/abs/2605.23351)

<!-- review:SF-2026-ARXIV-2605-23351:start -->
证据位置：3 The Prudent-Banker Algorithm; 4 Main Results and Analysis; no dedicated limitations section; non-proof boundary taken from disclosed method/evaluation scope。
<!-- claim:SF-2026-ARXIV-2605-23351:start -->exact-v1 采用命题：We study adversarial multi-armed bandits with and without delayed feedback under a safety-aware goal: achieving minimax-optimal worst-case regret while keeping nearly constant regret relative to a designated "safe" baseline policy.<!-- claim:SF-2026-ARXIV-2605-23351:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Main Results and Analysis` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Reward Model、policy objective 与独立 outcome evidence 分责；PPO 没有解决 Reward correctness。
Books：No Change — Existing Coverage；owner=TRAIN-RLHF。
<!-- review:SF-2026-ARXIV-2605-23351:end -->

### [2605.23362 Instance-Optimal Estimation with Multiple LLM Judges on a Budget](https://arxiv.org/abs/2605.23362)

<!-- review:SF-2026-ARXIV-2605-23362:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23362` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23362:start -->We formalize this question as *budgeted heteroskedastic multi-judge estimation*.<!-- claim:SF-2026-ARXIV-2605-23362:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23362:end -->

### [2605.23365 Score-Based One-step MeanFlow Policy Optimization](https://arxiv.org/abs/2605.23365)

<!-- review:SF-2026-ARXIV-2605-23365:start -->
证据位置：Appendix A Algorithm Pseudocode; Appendix B VE-SDE Formulation of SOM and Experimental Results under VE-SDE; Limitations and Future Work.。
<!-- claim:SF-2026-ARXIV-2605-23365:start -->exact-v1 采用命题：We propose Score-Based One-step MeanFlow Policy Optimization (SOM), an actor-critic algorithm that resolves this by constructing the target velocity field directly from the Q-function via score estimation and a probability flow ODE, thereby concentrating probability mass on high-value modes.<!-- claim:SF-2026-ARXIV-2605-23365:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `Appendix B VE-SDE Formulation of SOM and Experimental Results under VE-SDE` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Credit Transport 应服从真实 Computation Graph；PPO 没有解决 Reward correctness。
Books：No Change — Existing Coverage；owner=TRAIN-PPO。
<!-- review:SF-2026-ARXIV-2605-23365:end -->

### [2605.23372 Curriculum reinforcement learning with measurable task representation learning](https://arxiv.org/abs/2605.23372)

<!-- review:SF-2026-ARXIV-2605-23372:start -->
证据位置：3.1 Curriculum Reinforcement Learning; 5.2.2 Results and Analysis; 6 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23372:start -->exact-v1 采用命题：To achieve automatic curriculum generation in complex task, we propose a novel automatic curriculum generation approach based on measurable task representation learning.<!-- claim:SF-2026-ARXIV-2605-23372:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5.2.2 Results and Analysis` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Credit Transport 应服从真实 Computation Graph；PPO 没有解决 Reward correctness。
Books：No Change — Existing Coverage；owner=TRAIN-PPO。
<!-- review:SF-2026-ARXIV-2605-23372:end -->

### [2605.23373 AffectCodec: Emotion-Preserving Neural Speech Codec with Block-Diagonal Residual FSQ](https://arxiv.org/abs/2605.23373)

<!-- review:SF-2026-ARXIV-2605-23373:start -->
证据位置：3.1 Emotion-Acoustic Dual-Path Architecture; 4 Experiments; 5 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23373:start -->exact-v1 采用命题：We propose AffectCodec, an emotion-preserving neural speech codec built on Block-Diagonal Residual Finite Scalar Quantization (BD-RFSQ).<!-- claim:SF-2026-ARXIV-2605-23373:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§任务贡献与当前可靠性不能共用一个 Gate；感知、写入、读取与行动使用必须分开验证。
Books：No Change — Existing Coverage；owner=MULTIMODAL-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23373:end -->

### [2605.23381 VDE: Training-Free Accelerating Rectified Flow Model via Velocity Decomposition and Estimation](https://arxiv.org/abs/2605.23381)

<!-- review:SF-2026-ARXIV-2605-23381:start -->
证据位置：HTML §3 velocity decomposition/temporal dynamics/VDE; HTML §4 Experiments; §4.3 ablations; HTML §5 Conclusion — training-free approximation boundary。
<!-- claim:SF-2026-ARXIV-2605-23381:start -->把 rectified-flow acceleration 从静态 feature cache 改为对 velocity 的平行/正交分量做 input-adaptive estimation，并以周期 full-forward anchor 限制累计误差。<!-- claim:SF-2026-ARXIV-2605-23381:end -->
证据边界、trade-off、failure 与 fallback：temporal predictability 会随 model/task/resolution 漂移，anchor interval 太长会累计误差；质量或 drift gate 失败时回退 full forward 或缩短 anchor interval。
Books：Applied；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23381:end -->

### [2605.23382 From Correctness to Preference: A Framework for Personalized Agentic Reinforcement Learning](https://arxiv.org/abs/2605.23382)

<!-- review:SF-2026-ARXIV-2605-23382:start -->
证据位置：HTML §4 PARPO/reward disentanglement/skill graph memory; HTML §5 Experiments; §5.3–§5.5 ablation/dynamics; HTML §6 Conclusion and Limitations; Appendix C assumptions。
<!-- claim:SF-2026-ARXIV-2605-23382:start -->把 generic task reward 与 personalized preference reward 分离，以 user-specific anchor 校准 advantage，并把可复用 skill 组织为 preference-aligned graph memory。<!-- claim:SF-2026-ARXIV-2605-23382:end -->
证据边界、trade-off、failure 与 fallback：user anchor、reward disentanglement 与 skill retrieval 都可能固化稀疏/错误偏好；证据限 ETAPP/SJAgent，隐私或泛化 gate 失效时回退通用 policy、显式 profile 和人工 preference control。
Books：Applied；owner=TRAIN-RLHF。
<!-- review:SF-2026-ARXIV-2605-23382:end -->

### [2605.23384 Metacognition as Reward: Reinforcing LLM Reasoning via Knowledge and Regulation Signals](https://arxiv.org/abs/2605.23384)

<!-- review:SF-2026-ARXIV-2605-23384:start -->
证据位置：HTML §3 metacognitive rollout/reward/policy optimization; HTML §4 Experiment; §4.3–§4.5 mechanism/generalization/ablation; HTML §5 Conclusion and Limitation。
<!-- claim:SF-2026-ARXIV-2605-23384:start -->以 metacognitive knowledge 与 regulation 两类 process channel 对 reasoning trajectory 评分，并与终态正确性联合优化。<!-- claim:SF-2026-ARXIV-2605-23384:end -->
证据边界、trade-off、failure 与 fallback：自然语言 process scaffold 和 judge 仍可能奖励可读但错误的推理；22 benchmark 不能证明跨任务 truth，失败时回退 executable outcome reward、分项 rubric 与人工抽检。
Books：No Change — Existing Coverage；owner=TRAIN-RLHF。
<!-- review:SF-2026-ARXIV-2605-23384:end -->

### [2605.23389 AlignedServe: Orchestrating Prefix-aware Batching to Build a High-throughput and Computing-efficient LLM Serving System](https://arxiv.org/abs/2605.23389)

<!-- review:SF-2026-ARXIV-2605-23389:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23389` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23389:start -->We propose AlignedServe, an LLM serving framework built around prefix-aware batching.<!-- claim:SF-2026-ARXIV-2605-23389:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23389:end -->

### [2605.23398 TPMM-DPO: Trajectory-aware Preference-guided Model Merging for Iterative Direct Preference Optimization](https://arxiv.org/abs/2605.23398)

<!-- review:SF-2026-ARXIV-2605-23398:start -->
证据位置：HTML §3 trajectory model merging with learnable weights; HTML §5 Experimental Setup; §5.5 results/robustness/iterations; HTML §6 Conclusions。
<!-- claim:SF-2026-ARXIV-2605-23398:start -->把 iterative DPO 的 policy snapshots 视为带 lineage 的优化轨迹，用 preference-guided learned weights 构造 reference，减少单一上一轮 reference 的噪声累积。<!-- claim:SF-2026-ARXIV-2605-23398:end -->
证据边界、trade-off、failure 与 fallback：learned fusion 会引入 snapshot 存储、选择偏差与额外训练，in/out-domain 结果不证明长期稳定；权重或 held-out reward 失真时回退固定 reference、简单平均或停止迭代。
Books：Applied；owner=TRAIN-DPO。
<!-- review:SF-2026-ARXIV-2605-23398:end -->

### [2605.23410 What Linear Probes Miss: Multi-View Probing for Weight-Space Learning](https://arxiv.org/abs/2605.23410)

<!-- review:SF-2026-ARXIV-2605-23410:start -->
证据位置：4 Method; 5.1 Main Results on Model Jungle; 3.3 Limitations of First-Order Probing。
<!-- claim:SF-2026-ARXIV-2605-23410:start -->exact-v1 采用命题：To bridge this gap, we introduce MVProbe, a multi-perspective probing framework that synthesizes first-order signals with interaction-aware (Gram-based) views.<!-- claim:SF-2026-ARXIV-2605-23410:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5.1 Main Results on Model Jungle` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从可读出到机制：证据应逐级变强——信息存在、可读与被使用是三个不同命题。
Books：No Change — Existing Coverage；owner=WORLDVIEW-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23410:end -->

### [2605.23411 Sample-wise Targeted Adversarial Attacks on Test-time Adaptation](https://arxiv.org/abs/2605.23411)

<!-- review:SF-2026-ARXIV-2605-23411:start -->
证据位置：3 Threat Model; 5.2 Main Results; Appendix J Limitation and Future Work。
<!-- claim:SF-2026-ARXIV-2605-23411:start -->exact-v1 采用命题：To capture a more realistic threat, we introduce a sample-wise targeted attack.<!-- claim:SF-2026-ARXIV-2605-23411:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5.2 Main Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从资产与信任边界开始；检测器是 Policy-bound Sensor，不拥有安全判决。
Books：No Change — Existing Coverage；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-23411:end -->

### [2605.23414 When Planning Fails Despite Correct Execution: On Epistemic Calibration for LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2605.23414)

<!-- review:SF-2026-ARXIV-2605-23414:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23414` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23414:start -->To address this, we propose the Epistemic Planning Calibration Agentic Workflow (EPC-AW), which assesses whether plans remain supported under varying information conditions rather than directly verifying feasibility.<!-- claim:SF-2026-ARXIV-2605-23414:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23414:end -->

### [2605.23420 Naturalistic measure of social norms alignment](https://arxiv.org/abs/2605.23420)

<!-- review:SF-2026-ARXIV-2605-23420:start -->
证据位置：3.1 Methodology; 6 Results and Discussion; Limitations。
<!-- claim:SF-2026-ARXIV-2605-23420:start -->exact-v1 采用命题：We propose a framework for measuring social norm alignment in naturalistic, free-form settings through solution matching.<!-- claim:SF-2026-ARXIV-2605-23420:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `6 Results and Discussion` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23420:end -->

### [2605.23424 Sparse In-Network Learning via Shortest-Path Backpropagation and Finite-Rate Gating](https://arxiv.org/abs/2605.23424)

<!-- review:SF-2026-ARXIV-2605-23424:start -->
证据位置：II System Model and Sparse Backpropagation; IV-A Numerical results:; V Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23424:start -->exact-v1 采用命题：In-network learning (INL) trains distributed neural modules by exchanging latent activations and backpropagated errors over a communication graph.<!-- claim:SF-2026-ARXIV-2605-23424:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `IV-A Numerical results:` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§一次 training step 的状态流；optimizer、data transform 与 update geometry 属于同一 run identity。
Books：No Change — Existing Coverage；owner=TRAIN-PRETRAINING。
<!-- review:SF-2026-ARXIV-2605-23424:end -->

### [2605.23426 Socially fluent AI decouples conversational signals from source identity in online interaction](https://arxiv.org/abs/2605.23426)

<!-- review:SF-2026-ARXIV-2605-23426:start -->
证据位置：Results; Results; Discussion。
<!-- claim:SF-2026-ARXIV-2605-23426:start -->exact-v1 采用命题：Socially fluent agentic AI can now participate in online interaction in ways that resemble ordinary human conversation, potentially weakening people's ability to infer who is human from conversational signals alone.<!-- claim:SF-2026-ARXIV-2605-23426:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23426:end -->

### [2605.23445 DFSAttn: Dynamic Fine-grained Sparse Attention for Efficient Video Generation](https://arxiv.org/abs/2605.23445)

<!-- review:SF-2026-ARXIV-2605-23445:start -->
证据位置：5 Method; 6.2 Quality and efficiency results; 7 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23445:start -->exact-v1 采用命题：In this paper, we revisit block sparse attention and derive a theoretical lower bound on attention recall to characterize the key factors governing its effectiveness.<!-- claim:SF-2026-ARXIV-2605-23445:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `6.2 Quality and efficiency results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Sparse Support 与 Value Normalization 是两步决策；selector 必须承担语义责任并保留 dense fallback。
Books：No Change — Existing Coverage；owner=MODEL-SELF-ATTENTION。
<!-- review:SF-2026-ARXIV-2605-23445:end -->

### [2605.23446 Weisfeiler-Leman Is Incomplete on Simple Spectrum Graphs, so Canonicalize Them](https://arxiv.org/abs/2605.23446)

<!-- review:SF-2026-ARXIV-2605-23446:start -->
证据位置：3 Preliminaries; 6 Experiments; no dedicated limitations section; non-proof boundary taken from disclosed method/evaluation scope。
<!-- claim:SF-2026-ARXIV-2605-23446:start -->exact-v1 采用命题：Graphs with a simple spectrum admit cubic-time isomorphism testing, yet we prove that for every natural number $k$, the $k$-Weisfeiler-Leman ($k$-WL) test cannot distinguish all non-isomorphic graphs with a simple spectrum.<!-- claim:SF-2026-ARXIV-2605-23446:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `6 Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从可读出到机制：证据应逐级变强——信息存在、可读与被使用是三个不同命题。
Books：No Change — Existing Coverage；owner=WORLDVIEW-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23446:end -->

### [2605.23449 Commutator-Induced Uncertainty in VAEs](https://arxiv.org/abs/2605.23449)

<!-- review:SF-2026-ARXIV-2605-23449:start -->
证据位置：3 Methodology; 5 Results; 6 Conclusions。
<!-- claim:SF-2026-ARXIV-2605-23449:start -->exact-v1 采用命题：We introduce a Lie Group VAE framework that combines geometric and algebraic perspectives on uncertainty while separating discrete generative factors from continuous geometric transformations.<!-- claim:SF-2026-ARXIV-2605-23449:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5 Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从可读出到机制：证据应逐级变强——信息存在、可读与被使用是三个不同命题。
Books：No Change — Existing Coverage；owner=WORLDVIEW-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23449:end -->

### [2605.23451 Efficient One-Step Diffusion Restoration Model with Compact Token Compression and Linear Attention](https://arxiv.org/abs/2605.23451)

<!-- review:SF-2026-ARXIV-2605-23451:start -->
证据位置：3 Proposed Method; 4 Experimental Results; Appendix D Limitations and Future Work。
<!-- claim:SF-2026-ARXIV-2605-23451:start -->exact-v1 采用命题：Motivated by this observation, we revisit Real-ISR from the perspectives of compact latent representation and linear-complexity modeling, and propose SANA-SR, an efficient one-step restoration framework.<!-- claim:SF-2026-ARXIV-2605-23451:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Experimental Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§并行与少步生成必须声明依赖、轨迹和状态边界；Draft、Verify 与 Correct 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23451:end -->

### [2605.23458 One-Forcing: Towards Stable One-Step Autoregressive Video Generation](https://arxiv.org/abs/2605.23458)

<!-- review:SF-2026-ARXIV-2605-23458:start -->
证据位置：HTML §3 consistency/DMD limitations and One-Forcing objective; HTML §4 Experiments; §4.4–§4.5 human study/ablation; HTML §6 Limitations and Future Work。
<!-- claim:SF-2026-ARXIV-2605-23458:start -->以 DMD objective 加 auxiliary GAN loss 稳定 one-step autoregressive video student，并比较 framewise/chunkwise training。<!-- claim:SF-2026-ARXIV-2605-23458:end -->
证据边界、trade-off、failure 与 fallback：单步 student 仍继承 teacher/DMD/critic bias、blurring 与 mode loss；VBench 和作者 human study 不证明 production latency/一致性，失败时回退多步 sampler。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23458:end -->

### [2605.23463 StepAudio 2.5 Technical Report](https://arxiv.org/abs/2605.23463)

<!-- review:SF-2026-ARXIV-2605-23463:start -->
证据位置：PDF §2 StepAudio 2.5 architecture; PDF §3–§5 evaluations; PDF limitations/evaluator caveats (p.10)。
<!-- claim:SF-2026-ARXIV-2605-23463:start -->统一 audio backbone 仍需把语义 token、acoustic detail、task-specific RLHF 与 streaming decode state 分责，ASR multi-token prediction 只是受限训练分支。<!-- claim:SF-2026-ARXIV-2605-23463:end -->
证据边界、trade-off、failure 与 fallback：厂商报告的模型、数据和 evaluator 不证明生产 streaming/SLO 或任意语种；Ch23 已覆盖 semantic/acoustic codebooks、speaker/turn identity、streaming backpressure 与不对称 audio representation。
Books：No Change — Existing Coverage；owner=MULTIMODAL-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23463:end -->

### [2605.23464 Unextractable Protocol Models: Collaborative Training and Inference without Weight Materialization](https://arxiv.org/abs/2605.23464)

<!-- review:SF-2026-ARXIV-2605-23464:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23464` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23464:start -->We introduce Unextractable Protocol Models (UPMs): a training and inference framework that leverages the sharded model setup to ensure model shards (i.e., subsets) held by participants are incompatible at different time steps.<!-- claim:SF-2026-ARXIV-2605-23464:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23464:end -->

### [2605.23467 S$^3$GNN: Efficient Global Mixing and Local Message Passing for Long-Range Graph Learning](https://arxiv.org/abs/2605.23467)

<!-- review:SF-2026-ARXIV-2605-23467:start -->
证据位置：3 Method; Results and Computational Complexity; no dedicated limitations section; non-proof boundary taken from disclosed method/evaluation scope。
<!-- claim:SF-2026-ARXIV-2605-23467:start -->exact-v1 采用命题：We revisit these conclusions and show that the associated Jacobian sensitivity lower bound is generally difficult to achieve in practice.<!-- claim:SF-2026-ARXIV-2605-23467:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `Results and Computational Complexity` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Sparse Support 与 Value Normalization 是两步决策；selector 必须承担语义责任并保留 dense fallback。
Books：No Change — Existing Coverage；owner=MODEL-SELF-ATTENTION。
<!-- review:SF-2026-ARXIV-2605-23467:end -->

### [2605.23472 Rethinking Transfer Learning for Industrial Inspection: DINOv3 vs. ImageNet Pretraining Across RGB and X-ray Tasks](https://arxiv.org/abs/2605.23472)

<!-- review:SF-2026-ARXIV-2605-23472:start -->
证据位置：3 Methodology; 5 Results and Analysis; 6 Discussions。
<!-- claim:SF-2026-ARXIV-2605-23472:start -->exact-v1 采用命题：We evaluate semantic segmentation, instance segmentation, and object detection across four downstream datasets spanning RGB surface-defect inspection and X-ray defect detection.<!-- claim:SF-2026-ARXIV-2605-23472:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5 Results and Analysis` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23472:end -->

### [2605.23476 Non-normal spectral signatures of instability in neural network training dynamics](https://arxiv.org/abs/2605.23476)

<!-- review:SF-2026-ARXIV-2605-23476:start -->
证据位置：HTML §§II–III non-normal update theory; HTML §IV numerical two-layer experiments; HTML §IV proof-of-concept scope。
<!-- claim:SF-2026-ARXIV-2605-23476:start -->optimizer update matrix 非 normal 时，eigenvalue/spectral-radius 稳定并不控制瞬态放大；应把 eigenvector conditioning/pseudospectral sensitivity 作为诊断而非自动控制权。<!-- claim:SF-2026-ARXIV-2605-23476:end -->
证据边界、trade-off、failure 与 fallback：只支持理论构造和小型 two-layer 数值实验，不能证明大型 Transformer 收敛或墙钟收益；诊断成本高或 basis 不稳时回退 singular-value/update-norm、loss trajectory 与 matched optimizer baseline。
Books：Applied；owner=TRAIN-PRETRAINING。
<!-- review:SF-2026-ARXIV-2605-23476:end -->

### [2605.23477 Semantically Structured Mixture-of-Experts for Compositional Robotic Manipulation](https://arxiv.org/abs/2605.23477)

<!-- review:SF-2026-ARXIV-2605-23477:start -->
证据位置：III Method; IV-E Real-world Results; IV-G Discussion and Limitations。
<!-- claim:SF-2026-ARXIV-2605-23477:start -->exact-v1 采用命题：We introduce Semantically Structured Mixture-of-Experts Diffusion Policy (SMoDP) for compositional robotic manipulation, a framework that grounds expert specialization in semantic task structure.<!-- claim:SF-2026-ARXIV-2605-23477:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `IV-E Real-world Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§VLA 闭环把 observation revision、action schema、controller authority 与真实 environment transition 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-EMBODIED-VLA。
<!-- review:SF-2026-ARXIV-2605-23477:end -->

### [2605.23482 Multimodal Distribution Matching for Vision-Language Dataset Distillation](https://arxiv.org/abs/2605.23482)

<!-- review:SF-2026-ARXIV-2605-23482:start -->
证据位置：3 Proposed Method; S3.7 Full Retrieval Results; no dedicated limitations section; non-proof boundary taken from disclosed method/evaluation scope。
<!-- claim:SF-2026-ARXIV-2605-23482:start -->exact-v1 采用命题：To address this, we present Multimodal Distribution Matching (MDM), a geometry-aware framework for efficient and generalizable multimodal distillation.<!-- claim:SF-2026-ARXIV-2605-23482:end -->
证据边界、trade-off、failure 与 fallback：结果绑定作者的 embedding geometry、数据集、IPC/trajectory baselines 与 expert pool；joint-space 距离可能遗漏细粒度 modality evidence，规模增大还受 expert-training cost 支配。几何失配或 downstream slice 回归时回退原始数据 mixture、单模态校验与可重放 trajectory matching。
Books：Applied；owner=TRAIN-DATA。
<!-- review:SF-2026-ARXIV-2605-23482:end -->

### [2605.23493 EDGE-OPD: Internalizing Privileged Context with Evidence Guided On-Policy Distillation](https://arxiv.org/abs/2605.23493)

<!-- review:SF-2026-ARXIV-2605-23493:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23493` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23493:start -->In this paper, we study this problem in a rare-token/identity setting and propose EviDence GuidEd On-Policy Distillation (EDGE-OPD), a modification of OPSD with two distinct characteristics: a) it uses guided rollouts to inject privileged-context behavior to the student at sampling time, so that the rare target behavior is actually present in the on-policy data, and b) it applies an evidence mask: the student is updated only at token positions where the privileged context supports the sampled token, rather than on every token in the rollout.<!-- claim:SF-2026-ARXIV-2605-23493:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23493:end -->

### [2605.23497 Asking For An Old Friend: Diagnosing and Mitigating Temporal Failure Modes in LLM-based Statutory Question Answering](https://arxiv.org/abs/2605.23497)

<!-- review:SF-2026-ARXIV-2605-23497:start -->
证据位置：HTML §2.4 temporal failure definitions; §4.1 temporally filtered RAG; HTML §§3–5 expert dataset/experiments/discussion; HTML §6 Conclusion and Open Questions。
<!-- claim:SF-2026-ARXIV-2605-23497:start -->RAG 必须把 fact date 与 document validity interval 作为 hard filter，分别防止 post-cutoff staleness 与对历史问题的 recency bias。<!-- claim:SF-2026-ARXIV-2605-23497:end -->
证据边界、trade-off、failure 与 fallback：证据限 312 条德国法 QA、五模型与 LLM judge；版本元数据缺失或法域含糊时不得自动裁决，回退 authoritative archive 与专家审查。
Books：Applied；owner=AGENT-RAG。
<!-- review:SF-2026-ARXIV-2605-23497:end -->

### [2605.23508 DrawVideo: Generating Long Video from Storyboard Keyframe Sketches](https://arxiv.org/abs/2605.23508)

<!-- review:SF-2026-ARXIV-2605-23508:start -->
证据位置：4 Methodology – DrawVideo Framework; 5 Experiments & Results; 6 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23508:start -->exact-v1 采用命题：We propose DrawVideo, a sketch-guided, storyboard-driven framework for controllable long-video generation.<!-- claim:SF-2026-ARXIV-2605-23508:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5 Experiments & Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§并行与少步生成必须声明依赖、轨迹和状态边界；Draft、Verify 与 Correct 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23508:end -->

### [2605.23522 Precise: SDE-Consistent Stochastic Sampling for RL Post-Training of Flow-Matching Models](https://arxiv.org/abs/2605.23522)

<!-- review:SF-2026-ARXIV-2605-23522:start -->
证据位置：HTML §4 sampler method/analysis; §4.3 SDE-consistent transition; HTML §5 Experiments; §5.5 ablations; HTML §4 assumptions/discussion; Appendix A/B approximation/error boundary。
<!-- claim:SF-2026-ARXIV-2605-23522:start -->flow-model RL 的 stochastic sampler 本身属于 policy identity：exploration SDE schedule 与小步数离散化必须共同保持 denoising consistency。<!-- claim:SF-2026-ARXIV-2605-23522:end -->
证据边界、trade-off、failure 与 fallback：冻结 posterior mean 是局部近似，reward/evaluator 与受测 FLUX setting 限制结论；探索过强或误差累计时回退 ODE、较小步长或已有 sampler。
Books：Applied；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23522:end -->

### [2605.23551 Goal-Conditioned Agents that Learn Everything All at Once](https://arxiv.org/abs/2605.23551)

<!-- review:SF-2026-ARXIV-2605-23551:start -->
证据位置：2.1 Goal-Conditioned Reinforcement Learning; 6 Experimental Results; 8 Limitations and Future Work。
<!-- claim:SF-2026-ARXIV-2605-23551:start -->exact-v1 采用命题：We show that this approach significantly outperforms other methods on goal-conditioned Craftax and is competitive with existing baselines on continuous control environments, while achieving a &gt;250x speed-up compared to all-goals relabelling.<!-- claim:SF-2026-ARXIV-2605-23551:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `6 Experimental Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Credit Transport 应服从真实 Computation Graph；PPO 没有解决 Reward correctness。
Books：No Change — Existing Coverage；owner=TRAIN-PPO。
<!-- review:SF-2026-ARXIV-2605-23551:end -->

### [2605.23556 Is Dimensionality a Barrier for Retrieval Models?](https://arxiv.org/abs/2605.23556)

<!-- review:SF-2026-ARXIV-2605-23556:start -->
证据位置：HTML §1.2–§1.4 retrieval margin formulation/results; §§2–4 proofs; HTML Appendix H InfoNCE/sigmoid free-embedding experiment; HTML §5 Limitations, Broader Impact, and LLM Usage。
<!-- claim:SF-2026-ARXIV-2605-23556:start -->理论给出 sparse relevance matrix 下达到 maximal margin 所需的 embedding dimension 上下界，并说明 sigmoid loss 在 free-embedding experiment 中的 margin 优势。<!-- claim:SF-2026-ARXIV-2605-23556:end -->
证据边界、trade-off、failure 与 fallback：结论依赖二值 relevance matrix、unit-norm/max-margin proxy 与 free embeddings，不等价真实 ANN、learned encoders 或端到端 RAG；仅作为表示容量边界报告。
Books：Report Only；owner=MODEL-EMBEDDING。
<!-- review:SF-2026-ARXIV-2605-23556:end -->

### [2605.23562 ARMS: Automatic Reward Shaping for Sparse-Reward Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.23562)

<!-- review:SF-2026-ARXIV-2605-23562:start -->
证据位置：5 Method; 6 Experiments; 7 Conclusion and Future Work。
<!-- claim:SF-2026-ARXIV-2605-23562:start -->exact-v1 采用命题：We propose Automatic Reward-shaping in Multi-agent Systems (ARMS), a self-supervised reward shaping framework for MARL that learns dense shaping signals from sparse environmental rewards through trajectory ranking.<!-- claim:SF-2026-ARXIV-2605-23562:end -->
证据边界、trade-off、failure 与 fallback：理论保证依赖固定对手条件，实验只覆盖部分可观测 multi-agent pathfinding；有限探索与耦合 policy-reward dynamics 会形成 oscillatory reward hacking。检测到循环协调或 best-response 漂移时增加探索、冻结 shaping model，或回退原始 sparse reward。
Books：Applied；owner=AGENT-MULTI-AGENT。
<!-- review:SF-2026-ARXIV-2605-23562:end -->

### [2605.23563 MARS: Magnitude-Aware Rank Statistics](https://arxiv.org/abs/2605.23563)

<!-- review:SF-2026-ARXIV-2605-23563:start -->
证据位置：2.1 The Friedman Test; 4 Experiments and Empirical Analysis; 4.7 Discussion。
<!-- claim:SF-2026-ARXIV-2605-23563:start -->exact-v1 采用命题：In order to address this issue, we propose Magnitude-Aware Rank Statistics (MARS) that incorporates a relative margin coefficient as a weight for the discrete ranks.<!-- claim:SF-2026-ARXIV-2605-23563:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Experiments and Empirical Analysis` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23563:end -->

### [2605.23565 Understanding Goal Generalisation in Sequential Reinforcement Learning](https://arxiv.org/abs/2605.23565)

<!-- review:SF-2026-ARXIV-2605-23565:start -->
证据位置：4.1 Method; 4.2 Results; no dedicated limitations section; non-proof boundary taken from disclosed method/evaluation scope。
<!-- claim:SF-2026-ARXIV-2605-23565:start -->exact-v1 采用命题：We study over 100 sequential training pipelines, evaluating behaviour across over 250 out-of-distribution environments.<!-- claim:SF-2026-ARXIV-2605-23565:end -->
证据边界、trade-off、failure 与 fallback：100 余条训练流水线和 250 余个合成 OOD 环境只支持作者特征化环境；latent policy gradients 是低维预测模型，不是真实 policy 的因果证书。probe 失配或真实任务无可定义 feature basis 时回退直接 OOD rollout、counterfactual retraining 与人工 goal audit。
Books：Applied；owner=TRAIN-PPO。
<!-- review:SF-2026-ARXIV-2605-23565:end -->

### [2605.23572 HARNESS-LM: A Three-Phase Training Recipe for Harnessing SLMs in Sponsored Search Retrieval](https://arxiv.org/abs/2605.23572)

<!-- review:SF-2026-ARXIV-2605-23572:start -->
证据位置：2. HLM: Training Recipe; 3. Experiments & Results; 4. Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23572:start -->exact-v1 采用命题：In this paper, we present HARNESS-LM (HLM), a three-phase training framework for transferring the capabilities of large-scale retrievers into compact, cost-efficient models.<!-- claim:SF-2026-ARXIV-2605-23572:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `3. Experiments & Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§一次 training step 的状态流；optimizer、data transform 与 update geometry 属于同一 run identity。
Books：No Change — Existing Coverage；owner=TRAIN-PRETRAINING。
<!-- review:SF-2026-ARXIV-2605-23572:end -->

### [2605.23574 Push Your Agent: Measuring and Enforcing Quantitative Goal Persistence in Long-Horizon LLM Agents](https://arxiv.org/abs/2605.23574)

<!-- review:SF-2026-ARXIV-2605-23574:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23574` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23574:start -->We study this gap as Quantitative Goal Persistence (QGP): whether an agent keeps working until an external verifier confirms enough distinct valid items.<!-- claim:SF-2026-ARXIV-2605-23574:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23574:end -->

### [2605.23591 Asymmetric Scaling Laws from Sparse Features](https://arxiv.org/abs/2605.23591)

<!-- review:SF-2026-ARXIV-2605-23591:start -->
证据位置：HTML §§2–3 sparse-random-feature model and two-exponent law; §§5–6 compute/GD; HTML §§4/7 experiments with linear/ReLU random features; HTML §8 Conclusion — Limitations; Appendix D/E assumptions。
<!-- claim:SF-2026-ARXIV-2605-23591:start -->稀疏 rare coordinates 可让 under/over-parameterized loss 呈不对称 exponent、double descent 与偏向增加数据量的 compute frontier。<!-- claim:SF-2026-ARXIV-2605-23591:end -->
证据边界、trade-off、failure 与 fallback：这是 random-feature asymptotic model 与 synthetic experiment，不是 LLM empirical scaling law；不据此给 frontier training 配方，仅保留理论反例。
Books：Report Only；owner=WORLDVIEW-SCALING-LAW。
<!-- review:SF-2026-ARXIV-2605-23591:end -->

### [2605.23598 When Youth Enter the Algorithmic Wild: Discovering and Understanding Potentially Harmful Teen Videos on Douyin and Kwai](https://arxiv.org/abs/2605.23598)

<!-- review:SF-2026-ARXIV-2605-23598:start -->
证据位置：C.3 Performance Evaluation of the LoRA-Finetuned Model; C.4 Comparative ICL Experiments with Qwen-VL-MAX; 6 Discussion。
<!-- claim:SF-2026-ARXIV-2605-23598:start -->exact-v1 采用命题：To bridge this gap, we propose PHTV-Scout, the first large-scale, behaviorally grounded measurement framework for Potentially Harmful Teen Videos (PHTVs).<!-- claim:SF-2026-ARXIV-2605-23598:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `C.4 Comparative ICL Experiments with Qwen-VL-MAX` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23598:end -->

### [2605.23602 GlowGS: Generative Semantic Feature Learning for 3D Gaussian Splatting in Nighttime Glow Scenes](https://arxiv.org/abs/2605.23602)

<!-- review:SF-2026-ARXIV-2605-23602:start -->
证据位置：3 Proposed Method: GlowGS; 4 Experiments; 5 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23602:start -->exact-v1 采用命题：Existing 3DGS methods effectively render high-quality novel views in clear-day scenes.<!-- claim:SF-2026-ARXIV-2605-23602:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§任务贡献与当前可靠性不能共用一个 Gate；感知、写入、读取与行动使用必须分开验证。
Books：No Change — Existing Coverage；owner=MULTIMODAL-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23602:end -->

### [2605.23603 Preisach Attention: A Hysteretic Model of Sequential Memory](https://arxiv.org/abs/2605.23603)

<!-- review:SF-2026-ARXIV-2605-23603:start -->
证据位置：HTML §3 Preisach Attention; HTML §4–§7 theory; HTML §10 open questions。
<!-- claim:SF-2026-ARXIV-2605-23603:start -->以 hysteretic relay operators 替代部分 attention interaction 可获得理论表达力与复杂性结果。<!-- claim:SF-2026-ARXIV-2605-23603:end -->
证据边界、trade-off、failure 与 fallback：只在 arbitrary-precision/formal setting 下证明性质，没有训练语言模型或 benchmark；仅报告为理论设计线索，不把 Turing completeness 写成可部署优势。
Books：Report Only；owner=MODEL-SELF-ATTENTION。
<!-- review:SF-2026-ARXIV-2605-23603:end -->

### [2605.23605 DiLaDiff: Distilled Latent-Augmented Diffusion for Language Modeling](https://arxiv.org/abs/2605.23605)

<!-- review:SF-2026-ARXIV-2605-23605:start -->
证据位置：HTML §3 autoencoder/latent diffusion/consistency distillation; HTML §4 Experiments; §4.1–§4.3 latent/hybrid/ablation; HTML §5 Conclusion — Limitations and future work; Appendix D。
<!-- claim:SF-2026-ARXIV-2605-23605:start -->为 masked diffusion LM 增加 semantic continuous latent：autoencoder 学表示、latent diffusion 学 prior、consistency model 压到 few-step，再与 discrete decoding 组合。<!-- claim:SF-2026-ARXIV-2605-23605:end -->
证据边界、trade-off、failure 与 fallback：新增 autoencoder/prior/distillation 三重训练与 latent collapse/decoder error；证据限作者文本模型，likelihood/长文本/服务成本未普遍证明，失败时回退纯 masked diffusion。
Books：Applied；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23605:end -->

### [2605.23610 EM-Vid: Training-Free Entity-Centric Memory for Efficient and Consistent Multi-Shot Video Generation](https://arxiv.org/abs/2605.23610)

<!-- review:SF-2026-ARXIV-2605-23610:start -->
证据位置：HTML §3 entity-indexed latent memory/sparse conditioning/update/noise control; HTML §4 Evaluation; §4.3 results/efficiency; HTML §5 Conclusion & Discussion; Appendix D–H scope。
<!-- claim:SF-2026-ARXIV-2605-23610:start -->把多镜头视频 full-frame history 改成 entity-indexed latent-patch bank，并用 budgeted update、entity-only sparse attention 与 noise injection 分离身份持久状态和场景瞬态。<!-- claim:SF-2026-ARXIV-2605-23610:end -->
证据边界、trade-off、failure 与 fallback：entity extraction/update 错误会污染后续镜头，patch bank 会丢环境关系；证据限作者 scripts/models，失败时回退 keyframe/full-frame conditioning 或整段生成。
Books：Applied；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23610:end -->

### [2605.23618 Benchmarking Google Embeddings 2 against Open-Source Models for Multilingual Dense Retrieval and RAG Systems](https://arxiv.org/abs/2605.23618)

<!-- review:SF-2026-ARXIV-2605-23618:start -->
证据位置：III Methodology; V Experimental Results; VIII Limitations。
<!-- claim:SF-2026-ARXIV-2605-23618:start -->exact-v1 采用命题：Chunking experiments show that all six models saturate at 32-token chunks on our corpus, with semantic chunking providing measurable gains only at 16 tokens.<!-- claim:SF-2026-ARXIV-2605-23618:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `V Experimental Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23618:end -->

### [2605.23623 Adversarial Vulnerability Under Temporal Concept Drift: A Longitudinal Study of Android Malware Detection](https://arxiv.org/abs/2605.23623)

<!-- review:SF-2026-ARXIV-2605-23623:start -->
证据位置：5 Methodology; 6 Results and Discussion; 7 Threats to Validity。
<!-- claim:SF-2026-ARXIV-2605-23623:start -->exact-v1 采用命题：We present a longitudinal, drift-aware evaluation of adversarial robustness across more than a decade of Android applications using static and dynamic feature representations extracted from emulator and real-device executions.<!-- claim:SF-2026-ARXIV-2605-23623:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `6 Results and Discussion` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从资产与信任边界开始；检测器是 Policy-bound Sensor，不拥有安全判决。
Books：No Change — Existing Coverage；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-23623:end -->

### [2605.23628 How Hard is it to Rig a Benchmark? A Social Choice Analysis of Leaderboard Robustness](https://arxiv.org/abs/2605.23628)

<!-- review:SF-2026-ARXIV-2605-23628:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23628` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23628:start -->Leveraging this identification, we show that the benchmark-specific training problem is NP-hard under Borda count and mean win rate.<!-- claim:SF-2026-ARXIV-2605-23628:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23628:end -->

### [2605.23629 DDX-TRACE: A Benchmark for Medical Diagnostic Trajectories in VLMs](https://arxiv.org/abs/2605.23629)

<!-- review:SF-2026-ARXIV-2605-23629:start -->
证据位置：3 Benchmark Construction; 5 Experiments and Results; 6 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23629:start -->exact-v1 采用命题：We introduce DDX-TRACE, a physician-adjudicated benchmark for multimodal neuroradiology that evaluates diagnostic trajectories under hidden evidence over 211 challenging cases.<!-- claim:SF-2026-ARXIV-2605-23629:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5 Experiments and Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23629:end -->

### [2605.23630 To Overlay or to Customize? Revisiting Architectural Choices in Heterogeneous Systems](https://arxiv.org/abs/2605.23630)

<!-- review:SF-2026-ARXIV-2605-23630:start -->
证据位置：6. Case Study for Advanced Overlay Architecture Design; 3. Experiment Setup; 7. Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23630:start -->exact-v1 采用命题：In this work, we present a systematic study of this trade-off from a deployment-centric perspective, focusing on an autonomous driving scenario.<!-- claim:SF-2026-ARXIV-2605-23630:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `3. Experiment Setup` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§生产系统必须把可用性、容量、变更、回滚与真实 outcome receipt 连接起来。
Books：No Change — Existing Coverage；owner=PLATFORM-PRODUCTION。
<!-- review:SF-2026-ARXIV-2605-23630:end -->

### [2605.23634 DualMem: Bypassing the Objectness Bottleneck for Calibrated Unknown-Stream Filtering in Open-World Object Detection](https://arxiv.org/abs/2605.23634)

<!-- review:SF-2026-ARXIV-2605-23634:start -->
证据位置：4 DualMem Method; 5.1 Main Results; 6 Discussion and Limitations。
<!-- claim:SF-2026-ARXIV-2605-23634:start -->exact-v1 采用命题：We find that the unknown prediction streams of strong OWOD detectors are heavily polluted: on M-OWODB, across PROB, OW-DETR, and HypOW, future-task positive unknowns make up less than 10% of unknown predictions, whereas background false positives account for 46-71%.<!-- claim:SF-2026-ARXIV-2605-23634:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5.1 Main Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§任务贡献与当前可靠性不能共用一个 Gate；感知、写入、读取与行动使用必须分开验证。
Books：No Change — Existing Coverage；owner=MULTIMODAL-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23634:end -->

### [2605.23635 Dirichlet-Based Monte Carlo Dropout for Uncertainty Estimation in Neural Networks](https://arxiv.org/abs/2605.23635)

<!-- review:SF-2026-ARXIV-2605-23635:start -->
证据位置：2 Proposed approach; 3 Results; 4 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23635:start -->exact-v1 采用命题：Traditional neural networks provide deterministic predictions without inherent uncertainty estimates.<!-- claim:SF-2026-ARXIV-2605-23635:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `3 Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23635:end -->

### [2605.23640 CachePrune: Privacy-Aware and Fine-Grained KV Cache Sharing for Efficient LLM Inference](https://arxiv.org/abs/2605.23640)

<!-- review:SF-2026-ARXIV-2605-23640:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23640` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23640:start -->Building on this, we present CachePrune, a privacy-aware KV cache sharing mechanism that enables fine-grained reuse of KV entries across requests.<!-- claim:SF-2026-ARXIV-2605-23640:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23640:end -->

### [2605.23641 Kernel-Based ReLU Approximation for Homomorphic Encryption-Compatible Privacy-preserving Deep Learning Models](https://arxiv.org/abs/2605.23641)

<!-- review:SF-2026-ARXIV-2605-23641:start -->
证据位置：4.3. Algorithm & Final Output; 5.4. Results; 5.5. Discussion。
<!-- claim:SF-2026-ARXIV-2605-23641:start -->exact-v1 采用命题：This paper proposes a kernel-based approximation of ReLU, enabling its use within HE-constrained settings and thus contributing a critical step toward supporting privacy-preserving LLMs.<!-- claim:SF-2026-ARXIV-2605-23641:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5.4. Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从资产与信任边界开始；检测器是 Policy-bound Sensor，不拥有安全判决。
Books：No Change — Existing Coverage；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-23641:end -->

### [2605.23643 Less Effort, Shorter Proofs: Reinforcement Learning for Security Protocol Analysis in Tamarin](https://arxiv.org/abs/2605.23643)

<!-- review:SF-2026-ARXIV-2605-23643:start -->
证据位置：HTML §4 reusable Tamarin proof-search API; HTML §5 evaluation across 16 protocol case studies; HTML conclusion and case-study/tool-interface scope。
<!-- claim:SF-2026-ARXIV-2605-23643:start -->exact-v1 采用命题：In this paper, we present a reinforcement learning (RL) framework inspired by AlphaZero and AlphaProof that implements a new style of proof search for Tamarin.<!-- claim:SF-2026-ARXIV-2605-23643:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `no standalone evaluation section; exact-v1 stated theorem/method scope reviewed` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§模型输出只是 Proposal；Tool Contract、side-effect class 与独立 Outcome Contract 拥有 commit。
Books：No Change — Existing Coverage；owner=AGENT-TOOL-CALLING。
<!-- review:SF-2026-ARXIV-2605-23643:end -->

### [2605.23645 Learning Through Noise: Why Subliminal Learning Works and When It Fails](https://arxiv.org/abs/2605.23645)

<!-- review:SF-2026-ARXIV-2605-23645:start -->
证据位置：HTML §3 conditions for subliminal learning; §5 Methods; HTML §4 Results; Appendix B/C controlled experiments; HTML §6 Discussion; Appendix A necessary/failed conditions。
<!-- claim:SF-2026-ARXIV-2605-23645:start -->蒸馏无关噪声也能传递 teacher signal；关键不是相同初始化，而是 auxiliary/class output head 的兼容性与表示可恢复性。<!-- claim:SF-2026-ARXIV-2605-23645:end -->
证据边界、trade-off、failure 与 fallback：理论和实验基于 controlled MNIST/MLP-CNN heads，不证明 LLM 普遍 subliminal transfer；head 不兼容时效应消失，应回退内容审计、verified data 与独立初始化。
Books：Applied；owner=TRAIN-SFT。
<!-- review:SF-2026-ARXIV-2605-23645:end -->

### [2605.23652 One Policy, Infinite NPCs: Persona-Traceable Shared RL Policies for Scalable Game Agents](https://arxiv.org/abs/2605.23652)

<!-- review:SF-2026-ARXIV-2605-23652:start -->
证据位置：Appendix B UE5 System Architecture; V Layer 1 Results: Mechanistic Validation; IX Limitations and Scope。
<!-- claim:SF-2026-ARXIV-2605-23652:start -->exact-v1 采用命题：We introduce pcsp (Persona Conditioned Shared Policy), a single reinforcement learning policy conditioned on frozen LLM embeddings of free-form persona descriptions.<!-- claim:SF-2026-ARXIV-2605-23652:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `V Layer 1 Results: Mechanistic Validation` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Coordination State 必须有显式 Owner 与 Commit Transition；Pairwise coupling 不能外推 group dynamics。
Books：No Change — Existing Coverage；owner=AGENT-MULTI-AGENT。
<!-- review:SF-2026-ARXIV-2605-23652:end -->

### [2605.23655 CVSearch: Empowering Multimodal LLMs with Cognitive Visual Search for High-Resolution Image Perception](https://arxiv.org/abs/2605.23655)

<!-- review:SF-2026-ARXIV-2605-23655:start -->
证据位置：4.1 Method Overview; 5.2 Main Experimental Results; Limitations。
<!-- claim:SF-2026-ARXIV-2605-23655:start -->exact-v1 采用命题：To address this dilemma, we introduce CVSearch, a training-free adaptive framework that dynamically schedules search strategies via an Assess-then-Search workflow.<!-- claim:SF-2026-ARXIV-2605-23655:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5.2 Main Experimental Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Sparse Support 与 Value Normalization 是两步决策；selector 必须承担语义责任并保留 dense fallback。
Books：No Change — Existing Coverage；owner=MODEL-SELF-ATTENTION。
<!-- review:SF-2026-ARXIV-2605-23655:end -->

### [2605.23656 Recursive Block-Diagonal Coupling for Resource-Efficient Training of Vision Models](https://arxiv.org/abs/2605.23656)

<!-- review:SF-2026-ARXIV-2605-23656:start -->
证据位置：3 Method; 4 Results; 5 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23656:start -->exact-v1 采用命题：We propose an efficient training protocol, RBDC, that builds wide models by coupling in a parameter-free block-diagonal way narrower, independently trained models in a recursive way.<!-- claim:SF-2026-ARXIV-2605-23656:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§一次 training step 的状态流；optimizer、data transform 与 update geometry 属于同一 run identity。
Books：No Change — Existing Coverage；owner=TRAIN-PRETRAINING。
<!-- review:SF-2026-ARXIV-2605-23656:end -->

### [2605.23672 RiGS: Rigid-aware 4D Gaussian Splatting from a Single Monocular Video](https://arxiv.org/abs/2605.23672)

<!-- review:SF-2026-ARXIV-2605-23672:start -->
证据位置：3 Method; 11 More Results; 5 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23672:start -->exact-v1 采用命题：In this work, we present Rigid-aware 4D Gaussian Splatting (RiGS), which simultaneously captures motions across multiple temporal scales.<!-- claim:SF-2026-ARXIV-2605-23672:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `11 More Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§并行与少步生成必须声明依赖、轨迹和状态边界；Draft、Verify 与 Correct 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23672:end -->

### [2605.23673 Relevant Walk Search for Explaining Graph Neural Networks](https://arxiv.org/abs/2605.23673)

<!-- review:SF-2026-ARXIV-2605-23673:start -->
证据位置：2.1 Graph Neural Networks; 4 Experiments; Limitations。
<!-- claim:SF-2026-ARXIV-2605-23673:start -->exact-v1 采用命题：Specifically, we propose {\em polynomial-time} algorithms for finding top-$K$ relevant walks, which drastically reduces the computation and thus increases the applicability of GNN-LRP to large-scale problems.<!-- claim:SF-2026-ARXIV-2605-23673:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Sparse Support 与 Value Normalization 是两步决策；selector 必须承担语义责任并保留 dense fallback。
Books：No Change — Existing Coverage；owner=MODEL-SELF-ATTENTION。
<!-- review:SF-2026-ARXIV-2605-23673:end -->

### [2605.23684 Synthetic Sources?: Auditing Generative Search Engine Citations for Evidence of AI-Generated Sources](https://arxiv.org/abs/2605.23684)

<!-- review:SF-2026-ARXIV-2605-23684:start -->
证据位置：Methodology; Results; Limitations。
<!-- claim:SF-2026-ARXIV-2605-23684:start -->exact-v1 采用命题：In a step towards identifying whether AI-generated sources are being cited by these engines, this work presents an audit of four generative search engines (ChatGPT, Copilot, Gemini, Perplexity) using a total of 712 real-world human-generated queries spanning domains of public importance: politics, health, and the environment.<!-- claim:SF-2026-ARXIV-2605-23684:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23684:end -->

### [2605.23695 Validating Threat Modeling Results with the Help of Vulnerable Test Applications](https://arxiv.org/abs/2605.23695)

<!-- review:SF-2026-ARXIV-2605-23695:start -->
证据位置：III Research Design; IV Results; Limitations。
<!-- claim:SF-2026-ARXIV-2605-23695:start -->exact-v1 采用命题：This paper evaluates a complementary, vulnerability-grounded validation approach.<!-- claim:SF-2026-ARXIV-2605-23695:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `IV Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从资产与信任边界开始；检测器是 Policy-bound Sensor，不拥有安全判决。
Books：No Change — Existing Coverage；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-23695:end -->

### [2605.23699 CRONOS: Benchmarking Counterfactual Physical Consistency in Video Models](https://arxiv.org/abs/2605.23699)

<!-- review:SF-2026-ARXIV-2605-23699:start -->
证据位置：3 CRONOS Benchmark; 4 Results; 5 Limitations。
<!-- claim:SF-2026-ARXIV-2605-23699:start -->exact-v1 采用命题：We introduce CRONOS, an intervention-based benchmark designed to evaluate counterfactual physical consistency: whether a model's predictions of physical events respond appropriately to controlled changes in the visual input, such as variations of scene context, viewpoint, object appearance, and object category.<!-- claim:SF-2026-ARXIV-2605-23699:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§在谈 State 之前先声明预测 Channel，并把 observation/action truth 与模型假设分开。
Books：No Change — Existing Coverage；owner=MULTIMODAL-WORLD-MODELS。
<!-- review:SF-2026-ARXIV-2605-23699:end -->

### [2605.23702 TubiFM: Unified Item, Carousel, and Search Ranking for Streaming Discovery](https://arxiv.org/abs/2605.23702)

<!-- review:SF-2026-ARXIV-2605-23702:start -->
证据位置：5. TubiFM Model; 6.3. Results; 9. Limitations。
<!-- claim:SF-2026-ARXIV-2605-23702:start -->exact-v1 采用命题：We introduce the user story, a serialized representation that turns a user's cross-surface history - attributes, sessions, watch events with surface and carousel context, and search events - into a single token sequence.<!-- claim:SF-2026-ARXIV-2605-23702:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `6.3. Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Next-token 接口不要求内部状态只有一个粒度；输出接口不等于完整内部机制。
Books：No Change — Existing Coverage；owner=MODEL-DECODER-ONLY。
<!-- review:SF-2026-ARXIV-2605-23702:end -->

### [2605.23707 Flare: Leveraging Serverless Elasticity to Absorb Microservice Load Spikes](https://arxiv.org/abs/2605.23707)

<!-- review:SF-2026-ARXIV-2605-23707:start -->
证据位置：VI Experimental Methodology; VI Experimental Methodology; IX Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23707:start -->exact-v1 采用命题：To address the challenge of unpredictable load spikes, we propose Flare, a hybrid microservice architecture that combines VMs with serverless computing.<!-- claim:SF-2026-ARXIV-2605-23707:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `VI Experimental Methodology` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§生产系统必须把可用性、容量、变更、回滚与真实 outcome receipt 连接起来。
Books：No Change — Existing Coverage；owner=PLATFORM-PRODUCTION。
<!-- review:SF-2026-ARXIV-2605-23707:end -->

### [2605.23719 Weierstrass Positional Encoding for Vision Transformers](https://arxiv.org/abs/2605.23719)

<!-- review:SF-2026-ARXIV-2605-23719:start -->
证据位置：HTML §II Weierstrass elliptic 2D positional encoding/theory; HTML §III Experiments; §III-E/III-F ablation/sensitivity; HTML Appendix G-L model shortcomings/future directions。
<!-- claim:SF-2026-ARXIV-2605-23719:start -->用复平面上的 Weierstrass elliptic function/derivative 编码 2D patch coordinate，使 absolute encoding 可通过 addition formula 派生 relative position，并支持连续分辨率。<!-- claim:SF-2026-ARXIV-2605-23719:end -->
证据边界、trade-off、failure 与 fallback：lattice computation、数值稳定与几何先验不保证适合所有视觉任务；作者 ViT 实验不证明跨模态通用，极端 aspect/数值误差时回退 2D RoPE/learned table。
Books：Applied；owner=MODEL-POSITION-ENCODING。
<!-- review:SF-2026-ARXIV-2605-23719:end -->

### [2605.23721 Is a Document Educational or Just Wikipedia-Style? -- Pitfalls of Classifier-Based Quality Filtering](https://arxiv.org/abs/2605.23721)

<!-- review:SF-2026-ARXIV-2605-23721:start -->
证据位置：PDF §3 classifier-quality filtering bypass; PDF §4 manual annotation/experiments; PDF §5 conclusion and limitations。
<!-- claim:SF-2026-ARXIV-2605-23721:start -->quality classifier 可被表面格式操纵，使内容质量不变时 retention 决策翻转；filter release 应包含 policy-preserving style counterfactual。<!-- claim:SF-2026-ARXIV-2605-23721:end -->
证据边界、trade-off、failure 与 fallback：只覆盖 FineWeb-Edu classifier 与受测 reformatting；Ch27 已写明模型过滤器继承偏好、教科书风格损失多样性，并要求 retention/distribution shift 联合报告。
Books：No Change — Existing Coverage；owner=TRAIN-DATA。
<!-- review:SF-2026-ARXIV-2605-23721:end -->

### [2605.23723 MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection](https://arxiv.org/abs/2605.23723)

<!-- review:SF-2026-ARXIV-2605-23723:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23723` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23723:start -->We propose \textbf{MemAudit}, a post-hoc causal memory auditing framework for memory-augmented LLM agents.<!-- claim:SF-2026-ARXIV-2605-23723:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23723:end -->

### [2605.23726 Optimal Dimension-Free Sampling for Regularized Classification](https://arxiv.org/abs/2605.23726)

<!-- review:SF-2026-ARXIV-2605-23726:start -->
证据位置：2 Sampling, algorithms, and applications; 3 Our results; no dedicated limitations section; non-proof boundary taken from disclosed method/evaluation scope。
<!-- claim:SF-2026-ARXIV-2605-23726:start -->exact-v1 采用命题：We prove optimal sampling bounds achieving $(1\pm\varepsilon)$-relative error for a broad class of Lipschitz continuous classification loss functions under various regularization terms.<!-- claim:SF-2026-ARXIV-2605-23726:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `3 Our results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从可读出到机制：证据应逐级变强——信息存在、可读与被使用是三个不同命题。
Books：No Change — Existing Coverage；owner=WORLDVIEW-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23726:end -->

### [2605.23744 Contrast to Detect: Dynamic Graph Contrastive Regularization for Unsupervised Anomaly Detection in Multivariate Time Series](https://arxiv.org/abs/2605.23744)

<!-- review:SF-2026-ARXIV-2605-23744:start -->
证据位置：3. Methodology; 4. Experiments; 5. Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23744:start -->exact-v1 采用命题：We propose ContrastAD, an unsupervised framework that turns structural evolution itself into a learning signal rather than suppressing it.<!-- claim:SF-2026-ARXIV-2605-23744:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4. Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23744:end -->

### [2605.23747 Revitalizing Dense Material Segmentation: Stabilized Vision Transformers and the Generalization Paradox](https://arxiv.org/abs/2605.23747)

<!-- review:SF-2026-ARXIV-2605-23747:start -->
证据位置：3 Methodology; 4 Experiments and Results; 6 Conclusion and Limitations。
<!-- claim:SF-2026-ARXIV-2605-23747:start -->exact-v1 采用命题：We conduct an exhaustive evaluation of SegFormer and Mask2Former architectures, revealing that standard training paradigms fail on amorphous texture fields due to high-variance gradients.<!-- claim:SF-2026-ARXIV-2605-23747:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Experiments and Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23747:end -->

### [2605.23751 Approaching I/O-optimality for Approximate Attention](https://arxiv.org/abs/2605.23751)

<!-- review:SF-2026-ARXIV-2605-23751:start -->
证据位置：PDF §2 I/O model; PDF approximate-attention algorithms/lower bounds; PDF theory boundary。
<!-- claim:SF-2026-ARXIV-2605-23751:start -->在特定 external-memory/I/O model 与 additive approximation error 下构造 attention 算法及 lower bound。<!-- claim:SF-2026-ARXIV-2605-23751:end -->
证据边界、trade-off、failure 与 fallback：没有生产 kernel 或端到端模型实验，且不是 exact softmax；仅报告，不从渐近 I/O 界推出 GPU latency。实现前仍以 dense/exact attention 为 fidelity fallback。
Books：Report Only；owner=MODEL-SELF-ATTENTION。
<!-- review:SF-2026-ARXIV-2605-23751:end -->

### [2605.23753 SeedER: Seed-and-Expand Retrieval from Knowledge Graphs](https://arxiv.org/abs/2605.23753)

<!-- review:SF-2026-ARXIV-2605-23753:start -->
证据位置：HTML §§3–4 local seed-and-expand retrieval/learned expansion policy; HTML §5 Experiments; §5.1 ablations; HTML §6 Conclusion; Appendix B theory assumptions。
<!-- claim:SF-2026-ARXIV-2605-23753:start -->用 dense/entity seed 初始化小 core set，再由 RL graph policy 在 budget 内做局部 expansion，将 multi-hop retrieval 写成可复用的局部决策序列。<!-- claim:SF-2026-ARXIV-2605-23753:end -->
证据边界、trade-off、failure 与 fallback：只覆盖 STARK 类知识图、作者训练 policy 与 candidate recall；graph/seed 错误会阻断路径，失败时回退 fixed-depth expansion、dense+graph rerank 与显式 citation。
Books：No Change — Existing Coverage；owner=AGENT-RAG。
<!-- review:SF-2026-ARXIV-2605-23753:end -->

### [2605.23762 Direct Dynamic Retargeting for Humanoid Imitation Learning from Videos](https://arxiv.org/abs/2605.23762)

<!-- review:SF-2026-ARXIV-2605-23762:start -->
证据位置：III Method; IV-D Real World experiments; V Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23762:start -->exact-v1 采用命题：We identify that these intermediate kinematic projections introduce a geometric bias, restricting the search space and yielding suboptimal dynamic behaviors.<!-- claim:SF-2026-ARXIV-2605-23762:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `IV-D Real World experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§VLA 闭环把 observation revision、action schema、controller authority 与真实 environment transition 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-EMBODIED-VLA。
<!-- review:SF-2026-ARXIV-2605-23762:end -->

### [2605.23771 PhotoFlow: Agentic 3D Virtual Photography Missions](https://arxiv.org/abs/2605.23771)

<!-- review:SF-2026-ARXIV-2605-23771:start -->
证据位置：Automated photography and cinematography.; 5 Experiments; 6 Limitations。
<!-- claim:SF-2026-ARXIV-2605-23771:start -->exact-v1 采用命题：We introduce PhotoFlow, a Director-Reviewer-Reflector agent for closed-loop camera search.<!-- claim:SF-2026-ARXIV-2605-23771:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5 Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Plan 不是解释文本；从目标到状态图，并以完成证据和 verifier 决定提交。
Books：No Change — Existing Coverage；owner=AGENT-PLANNING。
<!-- review:SF-2026-ARXIV-2605-23771:end -->

### [2605.23772 Agentic Proving for Program Verification](https://arxiv.org/abs/2605.23772)

<!-- review:SF-2026-ARXIV-2605-23772:start -->
证据位置：PDF §2 methodology; PDF §4 CLEVER experiments; PDF benchmark-isomorphism limitations。
<!-- claim:SF-2026-ARXIV-2605-23772:start -->program-verification benchmark 的自然语言题与形式规格可能不等价；必须将 specification normalization、patched versions 与 executable checker 绑定到 Evaluation Identity。<!-- claim:SF-2026-ARXIV-2605-23772:end -->
证据边界、trade-off、failure 与 fallback：结果绑定 Claude/API 与 CLEVER 版本，ambiguous specs 仍需人工裁决；Ch66 已把 specification、parser、toolchain、tests 与 proof kernel 分层，任何一层通过都不覆盖其余边界。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23772:end -->

### [2605.23780 Beyond Binary Edits Robust Multimodal Knowledge Editing with Adversarial Subspace Alignment](https://arxiv.org/abs/2605.23780)

<!-- review:SF-2026-ARXIV-2605-23780:start -->
证据位置：HTML §4 latent adversarial robustification/rank-constrained subspace/asymmetric gradient; HTML §5 Experiments; §5.2–§5.3 performance/ablation; HTML Appendix E Limitations。
<!-- claim:SF-2026-ARXIV-2605-23780:start -->把 multimodal knowledge edit 的 generality 定义为 knowledge-unit 内一致性，用 joint-latent adversarial variants 暴露脆弱区域，再以低秩 subspace 对齐限制 edit 范围。<!-- claim:SF-2026-ARXIV-2605-23780:end -->
证据边界、trade-off、failure 与 fallback：语义 coherent adversary、knowledge-unit 与 low-rank assumption 都可能错，且 edit locality/controls 需独立验收；当前 ROADMAP 无 model-editing 唯一 owner，先保留 Structural Candidate。
Books：Structural Candidate；owner=尚无唯一 owner。
<!-- review:SF-2026-ARXIV-2605-23780:end -->

### [2605.23796 UniSpike: Accelerating Spiking Neural Networks on Neuromorphic Systems via Eliminating Address Redundancy](https://arxiv.org/abs/2605.23796)

<!-- review:SF-2026-ARXIV-2605-23796:start -->
证据位置：3.3. Implementation: UniSpike Architecture; 4.2. Overall Results; 5. Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23796:start -->exact-v1 采用命题：This paper presents UniSpike, a hardware-software co-design that removes address redundancy by aggregating spikes destined for the same core into compact packets.<!-- claim:SF-2026-ARXIV-2605-23796:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4.2. Overall Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：当前知识树没有唯一 owner，不能把局部结果直接升级为稳定机制。
Books：Structural Candidate；owner=尚无唯一 owner。
<!-- review:SF-2026-ARXIV-2605-23796:end -->

### [2605.23797 Debiased Negative Mining Improves Out-of-distribution Detection with Pre-trained Vision-Language Models](https://arxiv.org/abs/2605.23797)

<!-- review:SF-2026-ARXIV-2605-23797:start -->
证据位置：4 Methodology; 6 Experiments; no dedicated limitations section; non-proof boundary taken from disclosed method/evaluation scope。
<!-- claim:SF-2026-ARXIV-2605-23797:start -->exact-v1 采用命题：To this end, we develop a theoretical framework for correcting the sampling bias of negatives labels by indirectly approximating the distribution of negative labels.<!-- claim:SF-2026-ARXIV-2605-23797:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `6 Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23797:end -->

### [2605.23819 Not Too Generative, Not Too Discriminative: The Human Alignment Sweet Spot](https://arxiv.org/abs/2605.23819)

<!-- review:SF-2026-ARXIV-2605-23819:start -->
证据位置：3 Method; 4 Results; 5 Conclusion & Discussion。
<!-- claim:SF-2026-ARXIV-2605-23819:start -->exact-v1 采用命题：A central question in computational vision is whether human-like visual representations are better explained by discriminative or generative learning.<!-- claim:SF-2026-ARXIV-2605-23819:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从可读出到机制：证据应逐级变强——信息存在、可读与被使用是三个不同命题。
Books：No Change — Existing Coverage；owner=WORLDVIEW-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23819:end -->

### [2605.23821 Hierarchical Concept Geometry in Language Models Emerges from Word Co-occurrence](https://arxiv.org/abs/2605.23821)

<!-- review:SF-2026-ARXIV-2605-23821:start -->
证据位置：HTML §3 hierarchy-aligned spectral theory; HTML §§4–5 empirical tests in word2vec and LLM unembeddings; HTML §6 Limitations。
<!-- claim:SF-2026-ARXIV-2605-23821:start -->exact-v1 采用命题：We propose a distributional theory of how hypernymy -- the ``is-a'' relation between general and specific concepts -- is encoded geometrically in language representations.<!-- claim:SF-2026-ARXIV-2605-23821:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `no standalone evaluation section; exact-v1 stated theorem/method scope reviewed` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从可读出到机制：证据应逐级变强——信息存在、可读与被使用是三个不同命题。
Books：No Change — Existing Coverage；owner=WORLDVIEW-REPRESENTATION。
<!-- review:SF-2026-ARXIV-2605-23821:end -->

### [2605.23825 It's the humans, not the data: Geopolitical bias in LLMs originates in post-training, amplified by the language of the prompt](https://arxiv.org/abs/2605.23825)

<!-- review:SF-2026-ARXIV-2605-23825:start -->
证据位置：HTML Methods — base/chat pairs, scenario bank, multilingual measurement; HTML result sections — post-training/language effects and robustness; HTML Discussion — What this does not settle; Limitations。
<!-- claim:SF-2026-ARXIV-2605-23825:start -->偏差 attribution 必须把 base 与 chat/post-trained checkpoint 成对比较，并把 prompt language 作为 evaluation slice；不能把 chat 行为静默归因给 pretraining data。<!-- claim:SF-2026-ARXIV-2605-23825:end -->
证据边界、trade-off、failure 与 fallback：七模型、28 country pairs、强制选择 probe 与三语言不能识别具体 post-training cause，也可能受 response format 影响；回退开放生成、人工审查与更多 counterfactual controls。
Books：Applied；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23825:end -->

### [2605.23832 SFG-ROS: A Resource-Aware Framework for Dense Multi-Agent Perception](https://arxiv.org/abs/2605.23832)

<!-- review:SF-2026-ARXIV-2605-23832:start -->
证据位置：2.1 Multi-Agent ROS 2 Frameworks; 5 Experimental Evaluation; 6 Conclusion and Future Work。
<!-- claim:SF-2026-ARXIV-2605-23832:start -->exact-v1 采用命题：To address these bottlenecks, we present SFG-ROS, a resource-aware multi-agent software framework designed for dynamic fleet deployments.<!-- claim:SF-2026-ARXIV-2605-23832:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5 Experimental Evaluation` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§生产系统必须把可用性、容量、变更、回滚与真实 outcome receipt 连接起来。
Books：No Change — Existing Coverage；owner=PLATFORM-PRODUCTION。
<!-- review:SF-2026-ARXIV-2605-23832:end -->

### [2605.23833 DORA: Dataflow-Instruction Orchestration Architecture for DNN Acceleration](https://arxiv.org/abs/2605.23833)

<!-- review:SF-2026-ARXIV-2605-23833:start -->
证据位置：HTML §§3–4 DORA ISA/architecture/compiler/DSE; HTML §§5–7 VCK190 case study/end-to-end/generalization; HTML §7 Generality; §8 Conclusion — single-platform evidence boundary。
<!-- claim:SF-2026-ARXIV-2605-23833:start -->用 dataflow ISA 显式控制 on-chip memory、parallelism、off-chip movement 与 synchronization，再由 MILP/heuristic 两阶段 compiler search 生成执行计划。<!-- claim:SF-2026-ARXIV-2605-23833:end -->
证据边界、trade-off、failure 与 fallback：证据限 AMD Versal VCK190、作者 workloads 与模拟/原型，不能推出通用 GPU/ASIC 性能；当前 ROADMAP 无 DNN-accelerator ISA/compiler 唯一 owner，先保留 Structural Candidate。
Books：Structural Candidate；owner=尚无唯一 owner。
<!-- review:SF-2026-ARXIV-2605-23833:end -->

### [2605.23845 Learning a Particle Dynamics Model with Real-world Videos](https://arxiv.org/abs/2605.23845)

<!-- review:SF-2026-ARXIV-2605-23845:start -->
证据位置：3 Method; 5 Experiment; 6 Limitations。
<!-- claim:SF-2026-ARXIV-2605-23845:start -->exact-v1 采用命题：Specifically, we propose to learn a particle-based dynamics model compatible with a Gaussian splatting framework, which operates on dense particles derived from Gaussians (i.e., particles with scales and rotations) and predicts their position and rotation changes over time.<!-- claim:SF-2026-ARXIV-2605-23845:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5 Experiment` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§在谈 State 之前先声明预测 Channel，并把 observation/action truth 与模型假设分开。
Books：No Change — Existing Coverage；owner=MULTIMODAL-WORLD-MODELS。
<!-- review:SF-2026-ARXIV-2605-23845:end -->

### [2605.23847 Instrumentation for Imitation Learning: Enhancing Training Datasets for Clothes Hanger Insertion](https://arxiv.org/abs/2605.23847)

<!-- review:SF-2026-ARXIV-2605-23847:start -->
证据位置：II-C Policy Architecture; III Results; IV Discussion。
<!-- claim:SF-2026-ARXIV-2605-23847:start -->exact-v1 采用命题：In this paper, we present instrumented imitation learning of clothes hanger insertion.<!-- claim:SF-2026-ARXIV-2605-23847:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `III Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§VLA 闭环把 observation revision、action schema、controller authority 与真实 environment transition 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-EMBODIED-VLA。
<!-- review:SF-2026-ARXIV-2605-23847:end -->

### [2605.23856 Point Tracking Improves World Action Models](https://arxiv.org/abs/2605.23856)

<!-- review:SF-2026-ARXIV-2605-23856:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23856` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23856:start -->We propose JOPAT, a JOint Pixel-And-Track World-Action Model that predicts latent visual observations, 2D point tracks with visibility, and actions in a single denoising diffusion transformer.<!-- claim:SF-2026-ARXIV-2605-23856:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23856:end -->

### [2605.23857 Strong Teacher Not Needed? On Distillation in LLM Pretraining](https://arxiv.org/abs/2605.23857)

<!-- review:SF-2026-ARXIV-2605-23857:start -->
证据位置：PDF distillation method; PDF §6 experiments; Appendix G ablations; PDF fixed student/scale boundary。
<!-- claim:SF-2026-ARXIV-2605-23857:start -->teacher 的 aggregate capability 更强不保证固定 student 在固定 token/compute budget 下学得更多；teacher–student compatibility 与 target difficulty 应成为 distillation selection contract。<!-- claim:SF-2026-ARXIV-2605-23857:end -->
证据边界、trade-off、failure 与 fallback：主实验固定约 1.7B student、受测 teachers/tokens 与混合 LM/KD loss，不支持普遍选择弱 teacher；兼容性或 held-out gate 失效时回退 matched stronger teacher、ensemble/mixture 或直接 ground-truth SFT。
Books：Deferred；owner=TRAIN-SFT。
<!-- review:SF-2026-ARXIV-2605-23857:end -->

### [2605.23859 Natural Yet Challenging to Detect: Robust In-the-Wild TTS through EMA and Dual-Scoring Prompt Selection -- Submission for WildSpoof 2026 TTS Track](https://arxiv.org/abs/2605.23859)

<!-- review:SF-2026-ARXIV-2605-23859:start -->
证据位置：2 Methods; 3 Experimental Results; no dedicated limitations section; non-proof boundary taken from disclosed method/evaluation scope。
<!-- claim:SF-2026-ARXIV-2605-23859:start -->exact-v1 采用命题：We introduce F5-TTS-DPS, a model built upon the F5-TTS architecture.<!-- claim:SF-2026-ARXIV-2605-23859:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `3 Experimental Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从资产与信任边界开始；检测器是 Policy-bound Sensor，不拥有安全判决。
Books：No Change — Existing Coverage；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-23859:end -->

### [2605.23861 Leveraging Foundation Models for Causal Generative Modeling](https://arxiv.org/abs/2605.23861)

<!-- review:SF-2026-ARXIV-2605-23861:start -->
证据位置：5. Methodology; 6. Experiments; 7. Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23861:start -->exact-v1 采用命题：We introduce FM-CGM, a modular framework for end-to-end visual causal reasoning using pretrained foundation models.<!-- claim:SF-2026-ARXIV-2605-23861:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `6. Experiments` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§并行与少步生成必须声明依赖、轨迹和状态边界；Draft、Verify 与 Correct 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23861:end -->

### [2605.23867 Human Decision-Making with Persuasive and Narrative LLM Explanations](https://arxiv.org/abs/2605.23867)

<!-- review:SF-2026-ARXIV-2605-23867:start -->
证据位置：2.1 Narrative AI explanations; 3.6 Confirmatory results; 5 Limitations and future work。
<!-- claim:SF-2026-ARXIV-2605-23867:start -->exact-v1 采用命题：Here we conduct a large-scale human behavioral experiment to evaluate decision-making performance with LLM-generated narrative explanations of varying persuasiveness.<!-- claim:SF-2026-ARXIV-2605-23867:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `3.6 Confirmatory results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23867:end -->

### [2605.23868 Vision Transformers Need Better Token Interaction](https://arxiv.org/abs/2605.23868)

<!-- review:SF-2026-ARXIV-2605-23868:start -->
证据位置：3 Method; 4.2 Quantitative Results; 5 Discussion。
<!-- claim:SF-2026-ARXIV-2605-23868:start -->exact-v1 采用命题：We revisit this dense degradation phenomenon and argue that it is not fully explained by high-norm artifacts alone.<!-- claim:SF-2026-ARXIV-2605-23868:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4.2 Quantitative Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Sparse Support 与 Value Normalization 是两步决策；selector 必须承担语义责任并保留 dense fallback。
Books：No Change — Existing Coverage；owner=MODEL-SELF-ATTENTION。
<!-- review:SF-2026-ARXIV-2605-23868:end -->

### [2605.23871 Move on Muon : A Hamiltonian probability gradient flow perspective of Muon optimizer](https://arxiv.org/abs/2605.23871)

<!-- review:SF-2026-ARXIV-2605-23871:start -->
证据位置：HTML §§1–6 regularized Muon mirror/prox and Hamiltonian probability flow; HTML §7 Numerical Experiments; Appendix A.21 synthetic experiments; HTML theorem assumptions A1–A7; §8 Conclusion; subsequential hard-Muon limit。
<!-- claim:SF-2026-ARXIV-2605-23871:start -->把 regularized Muon 解释为 nuclear-norm Fenchel smoothing 下的 mirror/prox update，momentum 是 dual coordinate，并给出受假设约束的 Hamiltonian dissipation/convergence。<!-- claim:SF-2026-ARXIV-2605-23871:end -->
证据边界、trade-off、failure 与 fallback：主要是理论与 synthetic particle experiment；收敛依赖 gradient dominance、bounded momentum、curvature/alignment 等假设，不证明真实 Transformer/MoE wall-clock 或泛化，失配时回退 matched optimizer baseline。
Books：No Change — Existing Coverage；owner=TRAIN-PRETRAINING。
<!-- review:SF-2026-ARXIV-2605-23871:end -->

### [2605.23872 Training-Free Looped Transformers](https://arxiv.org/abs/2605.23872)

<!-- review:SF-2026-ARXIV-2605-23872:start -->
证据位置：PDF §2 damped substeps/Runge–Kutta loop; PDF §3 experiments; PDF fixed-recipe and failure cases。
<!-- claim:SF-2026-ARXIV-2605-23872:start -->training-free looped Transformer 通过 damped substeps/RK-style refinement 改变有效深度，但必须有收敛、预算与退化 fallback。<!-- claim:SF-2026-ARXIV-2605-23872:end -->
证据边界、trade-off、failure 与 fallback：知识型选择题、约 20k H100 hours 与受测 checkpoints 不证明通用收益；Ch17 已覆盖 fixed-loop/fixed-point refinement、收敛失败、迭代上限和固定深度 fallback。
Books：No Change — Existing Coverage；owner=MODEL-TRANSFORMER-LAYER。
<!-- review:SF-2026-ARXIV-2605-23872:end -->

### [2605.23878 LaMo: Self-Supervised Latent Motion Priors for Physical Realism in Video Generation](https://arxiv.org/abs/2605.23878)

<!-- review:SF-2026-ARXIV-2605-23878:start -->
证据位置：3 Method; 4.2 Main Results; 5 Conclusions and Limitations。
<!-- claim:SF-2026-ARXIV-2605-23878:start -->exact-v1 采用命题：We propose LaMo, which formulates a latent motion prior over frame-to-frame latent changes conditioned on the current latent and prompt.<!-- claim:SF-2026-ARXIV-2605-23878:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4.2 Main Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§并行与少步生成必须声明依赖、轨迹和状态边界；Draft、Verify 与 Correct 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23878:end -->

### [2605.23879 On the Stability of Spherical Hellinger-Kantorovich Flows and Their Implications for Differential Privacy](https://arxiv.org/abs/2605.23879)

<!-- review:SF-2026-ARXIV-2605-23879:start -->
证据位置：2 Notation; 4 Main Perturbation based Results; no dedicated limitations section; non-proof boundary taken from disclosed method/evaluation scope。
<!-- claim:SF-2026-ARXIV-2605-23879:start -->exact-v1 采用命题：In this work, we develop a perturbation theory for SHK gradient flows.<!-- claim:SF-2026-ARXIV-2605-23879:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4 Main Perturbation based Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§从资产与信任边界开始；检测器是 Policy-bound Sensor，不拥有安全判决。
Books：No Change — Existing Coverage；owner=PLATFORM-SECURITY。
<!-- review:SF-2026-ARXIV-2605-23879:end -->

### [2605.23883 PGT: Procedurally Generated Tasks for improving visual grounding in MLLMs](https://arxiv.org/abs/2605.23883)

<!-- review:SF-2026-ARXIV-2605-23883:start -->
证据位置：Causes of Finegrained Understanding Limitations in MLLMs.; 4 Results; Causes of Finegrained Understanding Limitations in MLLMs.。
<!-- claim:SF-2026-ARXIV-2605-23883:start -->exact-v1 采用命题：In this work, we propose Procedurally Generated Tasks (PGT), a simple data-driven framework that serves a dual purpose: inducing fine-grained visual understanding and acting as a low-cost diagnostic tool to identify the source of perception failures.<!-- claim:SF-2026-ARXIV-2605-23883:end -->
证据边界、trade-off、failure 与 fallback：收益绑定作者的 geometric overlays、MLLM、instruction-tuning recipe 与 11 个 benchmark；任务饱和、视觉 clutter 与合成 primitive 偏差会削弱迁移，不能证明所有空间错误都来自数据。迁移或通用能力回归时回退原始 mixture、独立 synthetic set 与真实图像人工标注。
Books：Applied；owner=TRAIN-DATA。
<!-- review:SF-2026-ARXIV-2605-23883:end -->

### [2605.23885 Multilingual Knowledge Transfer under Data Constraints via Lexical Interventions](https://arxiv.org/abs/2605.23885)

<!-- review:SF-2026-ARXIV-2605-23885:start -->
证据位置：HTML §3 lexical interventions for cross-lingual transfer; HTML §§4–6 setup/results/ablations; HTML §7 Conclusion; Appendix A tested languages/scales。
<!-- claim:SF-2026-ARXIV-2605-23885:start -->在高资源预训练语料中按 bilingual vocabulary 替换部分词项，把跨语言 transfer 从额外模型/平行语料改成可版本化 lexical intervention。<!-- claim:SF-2026-ARXIV-2605-23885:end -->
证据边界、trade-off、failure 与 fallback：词典歧义、replacement ratio 与 domain mixture 会制造语义噪声，八语言/五规模不证明通用迁移；退化时回退原始语料、可靠平行数据或独立 continued pretraining。
Books：Applied；owner=TRAIN-DATA。
<!-- review:SF-2026-ARXIV-2605-23885:end -->

### [2605.23887 CHRONOS: Temporally-Aware Multi-Agent Coordination for Evolving Data Marketplaces](https://arxiv.org/abs/2605.23887)

<!-- review:SF-2026-ARXIV-2605-23887:start -->
证据位置：4. The CHRONOS Architecture; 7.5. Ablation Study; 9. Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23887:start -->exact-v1 采用命题：We present CHRONOS, a three-layer architecture providing a unified treatment of these challenges with explicit public and private separation.<!-- claim:SF-2026-ARXIV-2605-23887:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `7.5. Ablation Study` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Coordination State 必须有显式 Owner 与 Commit Transition；Pairwise coupling 不能外推 group dynamics。
Books：No Change — Existing Coverage；owner=AGENT-MULTI-AGENT。
<!-- review:SF-2026-ARXIV-2605-23887:end -->

### [2605.23888 GenRecon: Bridging Generative Priors for Multi-View 3D Scene Reconstruction](https://arxiv.org/abs/2605.23888)

<!-- review:SF-2026-ARXIV-2605-23888:start -->
证据位置：3 Method; 4.1 Reconstruction Results; 4.4 Limitations。
<!-- claim:SF-2026-ARXIV-2605-23888:start -->exact-v1 采用命题：We introduce a new approach to high-fidelity 3D scene reconstruction from multi-view RGB images that tightly couples reconstruction with a strong generative 3D prior.<!-- claim:SF-2026-ARXIV-2605-23888:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4.1 Reconstruction Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§并行与少步生成必须声明依赖、轨迹和状态边界；Draft、Verify 与 Correct 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23888:end -->

### [2605.23889 HorizonStream: Long-Horizon Attention for Streaming 3D Reconstruction](https://arxiv.org/abs/2605.23889)

<!-- review:SF-2026-ARXIV-2605-23889:start -->
证据位置：HTML §3 geometric linear/local attention and architecture; HTML §4 Experiments; §4.3–§4.4 trajectory/reconstruction; HTML Appendix A/B attention dilution, boundedness and horizon assumptions。
<!-- claim:SF-2026-ARXIV-2605-23889:start -->将 streaming attention 的 influence kernel 分解为 channel-wise long-range decay 与 short-range local geometry，用有界 state 支持多时间尺度证据而避免 sliding-window hard cutoff/attention sink。<!-- claim:SF-2026-ARXIV-2605-23889:end -->
证据边界、trade-off、failure 与 fallback：结论绑定 3D geometry、48-frame training 与作者数据；decay state 可能遗忘突发证据，metric readout 也不是真值，失配时回退 sliding window/softmax/relocalization。
Books：Applied；owner=MODEL-SELF-ATTENTION。
<!-- review:SF-2026-ARXIV-2605-23889:end -->

### [2605.23891 Smart-Insertion-V: Photorealistic Video Insertion via a Closed-Loop Feedback Dual-Stream Framework](https://arxiv.org/abs/2605.23891)

<!-- review:SF-2026-ARXIV-2605-23891:start -->
证据位置：4 Method; 5.1 Qualitative Results; 6 Limitations。
<!-- claim:SF-2026-ARXIV-2605-23891:start -->exact-v1 采用命题：To overcome this, we propose \textit{\textbf{Smart-Insertion-V}}, an end-to-end \textbf{Dual-Stream} framework that concurrently conducts video insertion and image style transfer.<!-- claim:SF-2026-ARXIV-2605-23891:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `5.1 Qualitative Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§并行与少步生成必须声明依赖、轨迹和状态边界；Draft、Verify 与 Correct 分责。
Books：No Change — Existing Coverage；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23891:end -->

### [2605.23892 Good Token Hunting: A Hitchhiker's Guide to Token Selection for Visual Geometry Transformers](https://arxiv.org/abs/2605.23892)

<!-- review:SF-2026-ARXIV-2605-23892:start -->
证据位置：HTML §3 two-stage inter/intra-frame token selection; HTML §4 Experiments; §4.3 ablation/sensitivity; HTML Appendix G Limitations。
<!-- claim:SF-2026-ARXIV-2605-23892:start -->视觉几何 Transformer 的 global attention 可先按 frame diversity 保留覆盖，再按 layer-specific attention entropy 稀疏 token，而不是所有层共享一次 top-k。<!-- claim:SF-2026-ARXIV-2605-23892:end -->
证据边界、trade-off、failure 与 fallback：diversity/entropy 是任务特定 proxy，选择会删掉细小几何证据；500-image 结果不证明通用视觉 attention，回退 dense attention、提高 budget 或保留关键帧。
Books：Applied；owner=MODEL-SELF-ATTENTION。
<!-- review:SF-2026-ARXIV-2605-23892:end -->

### [2605.23893 Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models](https://arxiv.org/abs/2605.23893)

<!-- review:SF-2026-ARXIV-2605-23893:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23893` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23893:start -->We propose Complete-muE, a framework which targets hyperparameter transfer across dense FFN and any Mixture-of-Experts (MoE) setups in transformer blocks.<!-- claim:SF-2026-ARXIV-2605-23893:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23893:end -->

### [2605.23897 ETCHR: Editing To Clarify and Harness Reasoning](https://arxiv.org/abs/2605.23897)

<!-- review:SF-2026-ARXIV-2605-23897:start -->
证据位置：2 Analysis; 4.1 Main Results; 6 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23897:start -->exact-v1 采用命题：Guided by this analysis, we introduce ETCHR (Editing To Clarify and Harness Reasoning), a question-conditioned, reasoning-aware image editor decoupled from the downstream understanding model and trained with a two-stage recipe targeted at the two gaps: Reasoning Imitation via supervised fine-tuning on edit trajectories, followed by Reasoning Enhancement with VLM-derived rewards for edit correctness and downstream reasoning accuracy.<!-- claim:SF-2026-ARXIV-2605-23897:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `4.1 Main Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§模型输出只是 Proposal；Tool Contract、side-effect class 与独立 Outcome Contract 拥有 commit。
Books：No Change — Existing Coverage；owner=AGENT-TOOL-CALLING。
<!-- review:SF-2026-ARXIV-2605-23897:end -->

### [2605.23898 SPACENUM: Revisiting Spatial Numerical Understanding in VLMs](https://arxiv.org/abs/2605.23898)

<!-- review:SF-2026-ARXIV-2605-23898:start -->
证据位置：2 SpaceNum Data Curation; 3.1 Overall Results; Limitations and future work.。
<!-- claim:SF-2026-ARXIV-2605-23898:start -->exact-v1 采用命题：Therefore, in this work, we revisit spatial numerical understanding through SpaceNum, a unified framework that captures two complementary settings: numbers as dynamic transitions during spatial exploration, and numbers as static layouts in spatial reasoning.<!-- claim:SF-2026-ARXIV-2605-23898:end -->
证据边界、trade-off、failure 与 fallback：证据只覆盖 exact-v1 的 `3.1 Overall Results` 与作者披露的模型、数据、任务和设置；它不证明跨模型、跨分布或生产环境的普遍成立，也不把相关性/局部指标升级为因果。若该条件或测量不成立，回退当前 owner 基线：§Evaluation Identity 必须包含 Harness 与 Environment；评估声明总是相对于分布。
Books：No Change — Existing Coverage；owner=PLATFORM-EVALUATION-SYSTEM。
<!-- review:SF-2026-ARXIV-2605-23898:end -->

### [2605.23899 From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills](https://arxiv.org/abs/2605.23899)

<!-- review:SF-2026-ARXIV-2605-23899:start -->
exact-v1 identity、采用命题与版本未变，复用 [`legacy-v21-report-snapshot.md`](../_sources/daily-20260525/legacy-v21-report-snapshot.md) 中 `SF-2026-ARXIV-2605-23899` 的可读 Source Review 与 locator；V2.1 的 owner-day、分母和 Complete 状态不复用。当前结构化 method/evaluation/non-proof 边界见 `evidence-review-v3.json`。
<!-- claim:SF-2026-ARXIV-2605-23899:start -->However, while extraction methods continue to proliferate, understanding remains limited, with no comprehensive study spanning the full skill lifecycle -- \textbf{experience generation}, \textbf{skill extraction}, and \textbf{skill consumption} -- to ask whether such skills actually work, when they work, and what makes them succeed or fail.<!-- claim:SF-2026-ARXIV-2605-23899:end -->
证据边界：Only the exact-v1 method/evaluation/non-proof boundary in the preserved review is reused; V2.1 date ownership and Complete status are not reused.
<!-- review:SF-2026-ARXIV-2605-23899:end -->

### [2605.23901 LLMs as Noisy Channels: A Shannon Perspective on Model Capacity and Scaling Laws](https://arxiv.org/abs/2605.23901)

<!-- review:SF-2026-ARXIV-2605-23901:start -->
证据位置：PDF §3 noisy-channel scaling theory; PDF §4 Pythia/OLMo2 experiments; PDF selected-noise/fit boundary。
<!-- claim:SF-2026-ARXIV-2605-23901:start -->把训练噪声、量化或 SFT 扰动拟合为 noisy-channel capacity 可形成诊断性 scaling relation。<!-- claim:SF-2026-ARXIV-2605-23901:end -->
证据边界、trade-off、failure 与 fallback：选定 perturbations 和模型上的拟合不是普遍 Shannon law，也没有建立因果控制接口；仅报告为分析假说，训练决策仍回退 matched loss/quality/compute curves。
Books：Report Only；owner=TRAIN-PRETRAINING。
<!-- review:SF-2026-ARXIV-2605-23901:end -->

### [2605.23902 PiD: Fast and High-Resolution Latent Decoding with Pixel Diffusion](https://arxiv.org/abs/2605.23902)

<!-- review:SF-2026-ARXIV-2605-23902:start -->
证据位置：HTML §3 Pixel Diffusion Decoder; §3.4 distillation/early termination; HTML §4 Experiments; §4.3–§4.7 quality/cost/ablation/4K; HTML §4.6 Ablation and Discussion; §5 Conclusion。
<!-- claim:SF-2026-ARXIV-2605-23902:start -->把 latent-to-pixel reconstruction decoder 改成 conditional pixel diffusion，同时承担 decoding/upscaling；sigma-aware adapter 允许提前终止 latent diffusion，再以 DMD2 压到四步。<!-- claim:SF-2026-ARXIV-2605-23902:end -->
证据边界、trade-off、failure 与 fallback：pixel diffusion 引入生成随机性、13GB/指定硬件成本与 distillation bias，可能改变 faithful reconstruction；失真或预算超界时回退 VAE decoder/级联 SR。
Books：Applied；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23902:end -->

### [2605.23903 Geo-Align: Video Generation Alignment via Metric Geometry Reward](https://arxiv.org/abs/2605.23903)

<!-- review:SF-2026-ARXIV-2605-23903:start -->
证据位置：HTML §3 metric-geometry reward/GRPO/data pipeline; HTML §4 Experiments; §4.4–§4.5 results/ablation; HTML Appendix A.1 Limitations。
<!-- claim:SF-2026-ARXIV-2605-23903:start -->camera-controlled video RL 用 metric 3D estimator 分离 rotation/translation deviation，并以 real conditioning + synthetic target trajectory 避免 paired video。<!-- claim:SF-2026-ARXIV-2605-23903:end -->
证据边界、trade-off、failure 与 fallback：3D estimator 是 reward sensor，误差会被 policy 利用；数据和相机任务不证明开放视频 fidelity，失败时回退 SFT、人工 camera labels 或 deterministic geometry checks。
Books：Applied；owner=MULTIMODAL-GENERATIVE-PARADIGMS。
<!-- review:SF-2026-ARXIV-2605-23903:end -->

## 5. 缺口与下一步

1. 97 条 DataCite-recovered identity 已全部进入 owner-day terminal isolation；其 56 个旧 candidate、Evidence 与 Books 投影不再属于本 Daily。精确 identity 清单与 reopen condition 见 [`screening-outcomes-v3.json`](../_sources/daily-20260525/screening-outcomes-v3.json) 和 [`materials-request-v3.json`](../_sources/daily-20260525/materials-request-v3.json)。
2. 八个 ambiguous Applied family（2605.22863、2605.22873、2605.22949、2605.22967、2605.23080、2605.23128、2605.23668、2605.23826）已写为 owner-unresolved quarantine。现有 Books 正文保留，但不再由 05-25 提供正面 provenance；只有恢复 official owner day 或转交另一 verified owner report 后才能重开。
3. 唯一 day-owned blocked candidate 是 2605.23857；其 exact-v1 body 请求继续保留。2605.22834 与 2605.23491 在 owner day 未恢复前不再以 exact-v1 body 缺失阻塞本报告。
4. 本次没有扩来源、重跑 499 条或删除 Books。fresh non-author 已确认 97/402 partition、225 Evidence/Books 投影、8 个 quarantine 与材料清单一致；后续只在材料请求的精确重开条件满足时重开受影响 family。

终态保留项：97 个 owner-day ambiguous identity、`2605.23857` exact-v1 正文，以及 Meta/MiMo 日级入口限制均已隔离，不用于支持正面证据、Books 或无遗漏断言。定点重开条件：取得 97 项的 official arXiv announcement membership 或 verified owner report、取得 `2605.23857` 可重放的 official exact-v1 HTML/PDF 正文，或取得能唯一落入本窗的 Meta/MiMo 官方事件/历史索引；触发后只重开命中的 Source Family 或来源切片。

## 6. 复核

- **作者侧结果：** `499=402+97`；`402=225+177+0`；Evidence `225=224+1`；Books `225=44+1+166+8+6`；8 个 ambiguous Applied 依赖已 quarantine，2605.23128 不再由本 Daily 正面拥有。
- **独立复核：** fresh non-author 未参与本日 author repair 或 Books 写回；先找 owner-day、set projection、quarantine、blocked/materials 与 binding 反例，未发现新的实质缺陷。
- **状态：** `Complete — owner-day bounded repair passed fresh non-author final review`。
- **Receipt：** [`OWNER_DAY_BOUNDED_REPAIR_20260916.md`](../_sources/daily-20260525/OWNER_DAY_BOUNDED_REPAIR_20260916.md)、[`owner-day-bounded-repair-receipt-v3.json`](../_sources/daily-20260525/owner-day-bounded-repair-receipt-v3.json) 与 [`FRESH_NONAUTHOR_OWNER_DAY_FINAL_PASS_20260916.md`](../_sources/daily-20260525/FRESH_NONAUTHOR_OWNER_DAY_FINAL_PASS_20260916.md)。

复核者：`fresh-nonauthor:may25-owner-day-final-20260916`（未参与 05-25 author repair 或 root Books 写回）

结论：通过
