# Daily Research — 2026-06-12

**规范：** V3  
**窗口：** 2026-06-11T09:00:00+08:00 ～ 2026-06-12T09:00:00+08:00  
**状态：** 完成
**Books：** 纳入本次  
**检查时间：** 2026-09-11T12:45:00+08:00

## 1. 结论

对本目录 bounded canonical raw bucket 的全部 561 个 identity 已完成 title + complete abstract 准入审计；fresh-context 独立复核将 3 个误收项改为分母前关闭，最终冻结 63 个 Candidate、498 个 family-specific audited Close，满足 `561 raw = 63 Candidate + 498 audited Close`，ordinary pending=0。候选 exact-v1 Evidence Review 与 Books 比较也已独立复核：9 项确有正文增量并已写入 Books，53 项由现有章节覆盖，1 项仅报告。9 条正文均位于首个顶层 `Review notes` 前，具备机制、owner、收益、trade-off、failure、fallback 与证据边界；13 条 trace 日期修正已复验，剩余执行队列为 0。日期 owner 不由 submitted/v1 timestamp、identifier sequence、DataCite created 或 normal cutoff 推导；official historical listing receipt 到位前不执行跨日迁移，该保留限制不阻塞本日报闭环。

当前合同评分已由非作者重新校准，不以已经深读或已经写入 Books 倒推高分。63 项现在分布为 `5 分 × 1、6 分 × 53、8 分 × 9`；既有 exact-v1 深审仍可复用，最低审阅等级按新分数表述。逐项旧分、新分和三维依据见 [current score recalibration](../_sources/daily-20260612/CURRENT_SCORE_RECALIBRATION_20260914.json)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260612/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ANTHROPIC | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260612/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-GOOGLE-AI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260612/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-META-AI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260612/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-QWEN | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260612/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-DEEPSEEK | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260612/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-MOONSHOT | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260612/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260612/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ZAI | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260612/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260612/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260612/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260612/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-MINIMAX | 按当前合同回溯官方入口、窗口内条目与重复身份；详见 [source recert](../_sources/daily-20260612/CURRENT_SOURCE_RECERT_20260914.md) | 已检查 | 无 |
| SRC-ARXIV | [official listing owner audit](../_sources/daily-20260612/official-arxiv-announcement-owner-audit-v3.json) 记录 bounded raw bucket 561 项并撤回 schedule-derived migration；逐项 exact-v1 title + complete abstract；候选核对 exact-v1 HTML/PDF 的方法、评价与 limitations/non-proof | 已检查 | historical listing receipt 待补；未据此迁移 |

全量判定见 [`v3-reverse-admission-audit-20260910.json`](../_sources/daily-20260612/v3-reverse-admission-audit-20260910.json) 与 [`denominator-full-semantic-audit-v1.tsv`](../_sources/daily-20260612/denominator-full-semantic-audit-v1.tsv)。关闭理由绑定各自 exact-v1 题目与完整摘要中的问题/方法证据，不按关键词、学科标签、ROADMAP 映射或共享模板关闭；owner audit 明确保留 historical listing proof 缺口，不把 DataCite registration、submitted time 或正常 cutoff 推算当公开时刻。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Which Models Are Our Models Built On? Auditing Invisible Dependencies in Modern LLMs](https://arxiv.org/html/2606.12385v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We introduce ModSleuth, an agentic system that recursively reconstructs LLM dependency graphs from public artifacts with source-grounded evidence.”，该机制在 TRAIN-DATA 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文锚点：Data lineage 是训练可复现性的前提 |
| [Muse Spark Safety & Preparedness Report](https://arxiv.org/html/2606.12429v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Muse Spark Safety & Preparedness Report》关闭或降池；完整摘要显示“In this report, we first present evaluations for catastrophic risk domains under Meta's Advanced AI Scaling Framework, along with the evidence that informed our launch decision.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [ToolSense: A Diagnostic Framework for Auditing Parametric Tool Knowledge in LLMs](https://arxiv.org/html/2606.12451v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《ToolSense: A Diagnostic Framework for Auditing Parametric Tool Knowledge in LLMs》关闭或降池；完整摘要显示“We introduce \textbf{ToolSense}, an open-source LLM-powered diagnostic framework that takes any tool catalog as input and automatically generates three benchmarks: a Realistic Retrieval Benchmark (RRB) with queries at three ambiguity tiers, an MCQ probing benchmark, and a QA probing benchmark.”。该增量直接改变 AGENT-TOOL-CALLING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；正文锚点：Tool Contract |
| [Influence Factors on RAG Poisoning](https://arxiv.org/html/2606.12469v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“However, this reliance on retrieved content introduces vulnerabilities to poisoning attacks, in which adversarial documents can manipulate both the retrieval process and the generated outputs.”，该机制在 AGENT-RAG 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；正文锚点：RAG 安全必须覆盖完整状态生命周期 |
| [SAIGuard: Communication-State Simulation for Proactive Defense of LLM Multi-Agent Systems](https://arxiv.org/html/2606.12474v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《SAIGuard: Communication-State Simulation for Proactive Defense of LLM Multi-Agent Systems》关闭或降池；完整摘要显示“To address this, we propose a proactive defense framework for MAS security, namely a Simulation-aware Interception Guard (SAIGuard).”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文写入与独立 post-write audit 已完成 |
| [ReCal: Reward Calibration for RL-based LLM Routing](https://arxiv.org/html/2606.12479v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《ReCal: Reward Calibration for RL-based LLM Routing》关闭或降池；完整摘要显示“To address these issues, we propose \textbf{ReCal}, a \textbf{\underline{Re}}ward \textbf{\underline{Cal}}ibration framework for RL-based LLM routing.”。该增量直接改变 INFER-SCHEDULING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点：Model Routing 与 Test-time Scaling 必须结算同一个 Budget |
| [DynamicPTQ: Mitigating Activation Quantization Collapse via Residual-Stream Dynamics](https://arxiv.org/html/2606.12487v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“To characterize this behavior, we introduce Jump Ratio and Historical Feature SNR.”，该机制在 INFER-TENSORRT-LLM 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；正文锚点：量化为什么不自动带来加速 |
| [ITME: Inference Tiered Memory Expansion with Disaggregated CXL-Hybrid Memories](https://arxiv.org/html/2606.12556v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“In this paper, we propose ITME (Inference Tiered Memory Expansion), which leverages a CXL-hybrid memory to present a massive, TB-scale byte-addressable remote memory expansion.”，该机制在 INFER-GPU-MEMORY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-GPU-MEMORY，[owner](../../../../books/part-05-inference-system/54-gpu-memory.md)；正文锚点：Weights 与 KV 的联合 HBM 预算：可提交的运行时精度页 |
| [Arbor: Tree Search as a Cognition Layer for Autonomous Agents](https://arxiv.org/html/2606.12563v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Arbor: Tree Search as a Cognition Layer for Autonomous Agents》关闭或降池；完整摘要显示“Prior autonomous optimization systems operate on isolated targets with stateless evaluation.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；正文锚点：State Machine 是基本模型 |
| [Beyond Attack Success Rate: Examining Trigger Leakage in Vision-Language Agentic Systems](https://arxiv.org/html/2606.12586v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Beyond Attack Success Rate: Examining Trigger Leakage in Vision-Language Agentic Systems》关闭或降池；完整摘要显示“In this work, we formalize the failure of trigger precision as "trigger leakage": inputs that are visually or semantically close to the intended trigger and therefore inadvertently activate the attacker-specified behavior.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文写入与独立 post-write audit 已完成 |
| [Strategic Decision Support for AI Agents](https://arxiv.org/html/2606.12587v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Strategic Decision Support for AI Agents》关闭或降池；完整摘要显示“We propose a framework for strategic decision support for AI agents through an optimization problem that minimizes support usage subject to controlling a counterfactual missed-support error: the probability that the agent acts alone on instances where support would have materially improved its output.”。该增量直接改变 AGENT-PLANNING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-PLANNING，[owner](../../../../books/part-07-agent/79-planning.md)；正文锚点：先校准不确定性，再决定行动、询问或探索 |
| [Keep Policy Gradient in Charge: Sibling-Guided Credit Distillation for Long-Horizon Tool-Use Agents](https://arxiv.org/html/2606.12634v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Keep Policy Gradient in Charge: Sibling-Guided Credit Distillation for Long-Horizon Tool-Use Agents》关闭或降池；完整摘要显示“We introduce Sibling-Guided Credit Distillation (SGCD), which uses distillation for bounded credit weighting rather than as a competing actor loss.”。该增量直接改变 TRAIN-GRPO 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；正文锚点：从一个终局标量到 Typed Credit：Reward 必须匹配决策边界 |
| [Eidola: Modeling Multi-GPU Network Communication Traffic in Distributed AI Workloads](https://arxiv.org/html/2606.12638v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Eidola: Modeling Multi-GPU Network Communication Traffic in Distributed AI Workloads》关闭或降池；完整摘要显示“In this work, we introduce Eidola, a scalable extension to the gem5 simulation framework that enables detailed modeling of inter-GPU communication traffic.”。该增量直接改变 TRAIN-DISTRIBUTED-TRAINING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[owner](../../../../books/part-04-training-system/36-distributed-training.md)；正文锚点：从静态通信配置到受验证的 Collective Policy |
| [Evoflux: Inference-Time Evolution of Executable Tool Workflows for Compact Agents](https://arxiv.org/html/2606.12674v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Evoflux: Inference-Time Evolution of Executable Tool Workflows for Compact Agents》关闭或降池；完整摘要显示“We introduce Evoflux, an inference-time evolutionary search method that treats compact tool use as the repair of executable tool workflows.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；正文锚点：Release 与 Optimization 必须共享 Workflow Identity |
| [M*: A Modular, Extensible, Serving System for Multimodal Models](https://arxiv.org/html/2606.12688v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“Here we present M*, a universal serving system for efficient serving of composite AI models.”，该机制在 INFER-KSERVE-TOPOLOGY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-KSERVE-TOPOLOGY，[owner](../../../../books/part-05-inference-system/53-kserve-llm.md)；正文锚点：组件与 Ownership |
| [SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems](https://arxiv.org/html/2606.12703v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present Signed Memory with Smoothed Retrieval (SMSR), the first defence with a certified robustness bound for this setting.”，该机制在 PLATFORM-SECURITY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Smarter Saboteurs, Better Fixers: Scaling & Security in Linear Multi-Agent Workflows](https://arxiv.org/html/2606.12709v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Smarter Saboteurs, Better Fixers: Scaling & Security in Linear Multi-Agent Workflows》关闭或降池；完整摘要显示“Attackers may leverage prompt-injection or jailbreaking to sabotage individual agents within MAS workflows, but the interaction between model scaling and system-level resilience remains poorly understood.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [PI-Hunter: Automated Red-Teaming for Exposing and Localizing Prompt Injections](https://arxiv.org/html/2606.12737v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We propose PI-Hunter, an automated agentic auditing framework for proactive vulnerability exposure in LLM agents.”，该机制在 PLATFORM-SECURITY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Prefill Awareness in Large Language Models](https://arxiv.org/html/2606.12747v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Prefill Awareness in Large Language Models》关闭或降池；完整摘要显示“If AI models can recognize and act on the fact their prior assistant messages have been inserted or edited, the effectiveness and validity of these methods could be compromised.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文写入与独立 post-write audit 已完成 |
| [Detecting Functional Memorization in Code Language Models](https://arxiv.org/html/2606.12764v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Detecting Functional Memorization in Code Language Models》关闭或降池；完整摘要显示“We formalize this through a counterfactual framework, comparing target models (exposed to specific code) against reference models (not exposed) and requiring functional equivalence only for the target.”。该增量直接改变 TRAIN-DATA 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文写入与独立 post-write audit 已完成 |
| [Rigel: Reverse-Engineering the Metal 4.1 Tensor Compute Path on the Apple M4 Max GPU](https://arxiv.org/html/2606.12765v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present Rigel, an empirical characterization of this path on a single Apple M4 Max (a pre-neural-accelerator generation).”，该机制在 INFER-TENSORRT-LLM 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；正文锚点：量化为什么不自动带来加速 |
| [ProPlay: Procedural World Models for Self-Evolving LLM Agents](https://arxiv.org/html/2606.12780v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《ProPlay: Procedural World Models for Self-Evolving LLM Agents》关闭或降池；完整摘要显示“We introduce ProPlay, a procedural world model that supports procedure-level preplay, where agents can rehearse future procedural paths using the learned world knowledge.”。该增量直接改变 AGENT-PLANNING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-PLANNING，[owner](../../../../books/part-07-agent/79-planning.md)；正文锚点：从目标到状态图 |
| [The Containment Gap: How Deployed Agentic AI Frameworks Fail Public-Facing Safety Requirements](https://arxiv.org/pdf/2606.12797v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We ask whether the frameworks used to build these systems provide architectural-level structural safety guarantees.”，该机制在 PLATFORM-SECURITY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [LoHoSearch: Benchmarking Long-Horizon Search Agents Beyond the Human Difficulty Ceiling](https://arxiv.org/html/2606.12837v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《LoHoSearch: Benchmarking Long-Horizon Search Agents Beyond the Human Difficulty Ceiling》关闭或降池；完整摘要显示“To address this, we introduce LoHoSearch (Long-Horizon Search Agents), a challenging benchmark comprising 544 human-verified questions across 11 domains.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [HarnessBridge: Learnable Bidirectional Controller for LLM Agent Harness](https://arxiv.org/html/2606.12882v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；完整摘要确认其研究 learnable bidirectional harness projection，属于 LLM Agent runtime 范围，因此保留 Candidate。 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；现有 state-machine、compiler/executor 与 learned transition 合同已经覆盖该局部实现。 |
| [SENTINEL: Failure-Driven Reinforcement Learning for Training Tool-Using Language Model Agents](https://arxiv.org/html/2606.12908v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《SENTINEL: Failure-Driven Reinforcement Learning for Training Tool-Using Language Model Agents》关闭或降池；完整摘要显示“We propose SENTINEL, a failure-driven reinforcement learning framework that turns the Solver's rollout failures into targeted training tasks.”。该增量直接改变 TRAIN-DATA 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文锚点：Data lineage 是训练可复现性的前提 |
| [MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems](https://arxiv.org/html/2606.12918v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems》关闭或降池；完整摘要显示“We propose MAStrike, a closed-loop framework for collusive red-teaming in hierarchical MAS.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文写入与独立 post-write audit 已完成 |
| [MARS: Margin-Adversarial Risk-controlled Stopping for Parallel LLM Test-time Scaling](https://arxiv.org/html/2606.12935v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《MARS: Margin-Adversarial Risk-controlled Stopping for Parallel LLM Test-time Scaling》关闭或降池；完整摘要显示“Based on this observation, we introduce MARS, a margin-adversarial stopping rule that estimates which active traces are likely to change their answers and stops once the leader remains safe under a conservative bound on future vote movement.”。该增量直接改变 INFER-SCHEDULING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文写入与独立 post-write audit 已完成 |
| [Multi-Turn Reasoning When Context Arrives in Pieces: Scalable Sharding and Memory-Augmented RL](https://arxiv.org/html/2606.12941v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Multi-Turn Reasoning When Context Arrives in Pieces: Scalable Sharding and Memory-Augmented RL》关闭或降池；完整摘要显示“To make such training scalable, we introduce a low-cost sharding pipeline that converts single-turn QA datasets into multi-turn fragmented-information episodes, eliminating the need for hours of manual annotation.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory](https://arxiv.org/html/2606.12945v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory》关闭或降池；完整摘要显示“We propose a multi-factor memory value function V(m)=\sum_i w_i f_i(m) over seven interpretable factors (emotional intensity, goal relevance, value alignment, self/user relevance, task utility, reliability, and usage history) drawn from cognitive psychology, whose weights are learned from a downstream objective by a gradient-free optimiser, and whose single scalar uniformly controls encoding depth, forget risk, and retrieval rank.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-Based Multi-Agent Systems](https://arxiv.org/pdf/2606.12950v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present Maestro, a workload-aware scheduling system designed for LLM-MAS serving under strict GPU budgets.”，该机制在 INFER-SCHEDULING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点：Model Routing 与 Test-time Scaling 必须结算同一个 Budget |
| [ScaleAcross: Designing Multi-Data-Center Infrastructure for Geo-Distributed AI Training](https://arxiv.org/html/2606.12963v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《ScaleAcross: Designing Multi-Data-Center Infrastructure for Geo-Distributed AI Training》关闭或降池；完整摘要显示“Such deployments introduce system-level challenges arising from synchronization-intensive communication, cross-site data exchange, and wide-area latency constraints.”。该增量直接改变 TRAIN-DISTRIBUTED-TRAINING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[owner](../../../../books/part-04-training-system/36-distributed-training.md)；正文锚点：跨地域电力约束会把全局同步改成层级且有陈旧度的聚合 |
| [Trajectory-Level Redirection Attacks on Vision-Language-Action Models](https://arxiv.org/pdf/2606.12978v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“To find such prompts, we introduce an on-policy prompt search method that uses rollouts to discover perturbations whose closed-loop behavior tracks a target task while satisfying the command-preserving constraints.”，该机制在 MULTIMODAL-EMBODIED-VLA 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；正文锚点：Training-only Foresight 不是 Persistent World State |
| [The Illusion of Multi-Agent Advantage](https://arxiv.org/pdf/2606.13003v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“To isolate these failures from limitations inherent to task structure, we introduce a diagnostic synthetic dataset tailored for MAS featuring explicit task decomposition, context separation and parallelization potential.”，该机制在 AGENT-MULTI-AGENT 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；正文锚点：Message 不是 State |
| [EA-WM: Event-Aware World Models with Task-Specification Grounding for Long-Horizon Manipulation](https://arxiv.org/pdf/2606.13053v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We introduce EA-WM, an event-aware world-model framework that augments frozen visual-feature dynamics with task-specification-grounded event prediction and verification.”，该机制在 MULTIMODAL-WORLD-MODELS 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 Identity correction：raw inventory 题名《EV-WM: Event-Verified World Models for Long-Horizon Robotic Manipulation》不是 v1 authority；官方 exact-v1 题名为《EA-WM: Event-Aware World Models with Task-Specification Grounding for Long-Horizon Manipulation》，Evidence 只按 v1 复验。 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；正文锚点：从平均预测误差到分层的 Rollout Admission |
| [The Emergence of Autonomous Penetration Capabilities in Large Language Model-Powered AI Systems](https://arxiv.org/html/2606.13079v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《The Emergence of Autonomous Penetration Capabilities in Large Language Model-Powered AI Systems》关闭或降池；完整摘要显示“Within this broader red-line scenario, autonomous penetration represents a core enabling capability and subtask: the ability of LLM-powered AI systems to independently conduct adversarial operations against a target server without human intervention, identify and exploit vulnerabilities, and obtain unauthorized access or control.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [Scale Buys Interpolation, Structure Buys a Horizon: Certified Predictability for Equivariant World Models](https://arxiv.org/pdf/2606.13092v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“A world model's average error says nothing about whether a particular prediction can be trusted, or for how long.”，该机制在 MULTIMODAL-WORLD-MODELS 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 Identity correction：raw inventory 题名《Certified World Models: Predictability Across Configuration, Horizon, and Resolution》不是 v1 authority；官方 exact-v1 题名为《Scale Buys Interpolation, Structure Buys a Horizon: Certified Predictability for Equivariant World Models》，Evidence 只按 v1 复验。 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；正文锚点：从平均预测误差到分层的 Rollout Admission |
| [G-Long: Graph-Enhanced Memory Management for Efficient Long-Term Dialogue Agents](https://arxiv.org/html/2606.13115v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《G-Long: Graph-Enhanced Memory Management for Efficient Long-Term Dialogue Agents》关闭或降池；完整摘要显示“To address these limitations, we propose G-Long, a graph-enhanced framework that utilizes a fine-tuned small Language Model (sLM) for structured triplet extraction and associative retrieval, significantly reducing operational costs.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [EvoBrowseComp: Benchmarking Search Agents on Evolving Knowledge](https://arxiv.org/html/2606.13120v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《EvoBrowseComp: Benchmarking Search Agents on Evolving Knowledge》关闭或降池；完整摘要显示“In this paper, we introduce EvoBrowseComp, an evolving benchmark of 400 English and 400 Chinese contamination-free complex questions synthesized via live-web traversal.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [MiniPIC: Flexible Position-Independent Caching in <100LOC](https://arxiv.org/html/2606.13126v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《MiniPIC: Flexible Position-Independent Caching in <100LOC》关闭或降池；完整摘要显示“We present Minimalistic PIC (MiniPIC): a minimal, flexible and fast vLLM design built from two ingredients: positional-encoding-free KV cache and user-controlled cache-reuse primitives.”。该增量直接改变 INFER-KV-CACHE 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：INFER-KV-CACHE，[owner](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；正文锚点：任意 Chunk 复用必须先修复 Position 与 Conditioning Seam |
| [Iterative Visual Thinking and the Self-Correction Mirage in VLM Grounding](https://arxiv.org/html/2606.13156v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Iterative Visual Thinking and the Self-Correction Mirage in VLM Grounding》关闭或降池；完整摘要显示“A natural way to bring this to spatial grounding is visual self-correction: the model predicts a bounding box, sees it rendered on the image, and refines it over several steps.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents](https://arxiv.org/pdf/2606.13174v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We introduce Test-time Rule Acquisition and Compiled Enforcement (TRACE), a drop-in skill-layer pipeline for coding-agent runtimes that mines user corrections, rewrites them as atomic rules, and compiles them into runtime checks that must pass before an agent completes future tasks.”，该机制在 AGENT-WORKFLOW 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；正文锚点：State Machine 是基本模型 |
| [MemRefine: LLM-Guided Compression for Long-Term Agent Memory](https://arxiv.org/html/2606.13177v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《MemRefine: LLM-Guided Compression for Long-Term Agent Memory》关闭或降池；完整摘要显示“However, as interactions accumulate, the memory store grows without bound and fills with redundant entries that inflate storage cost and degrade retrieval by crowding out the most useful evidence.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |
| [LLM-as-an-Investigator: Evidence-First Reasoning for Robust Interactive Problem Diagnosis](https://arxiv.org/html/2606.13220v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《LLM-as-an-Investigator: Evidence-First Reasoning for Robust Interactive Problem Diagnosis》关闭或降池；完整摘要显示“However, when users provide incomplete descriptions or plausible but unverified explanations, LLMs may prematurely align with these assumptions and propose solutions before collecting sufficient evidence.”。该增量直接改变 AGENT-PLANNING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-PLANNING，[owner](../../../../books/part-07-agent/79-planning.md)；正文锚点：从目标到状态图 |
| [From Uncertain Judgments to Calibrated Rankings: Conformal Elo Estimation for LLM Evaluation](https://arxiv.org/html/2606.13221v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《From Uncertain Judgments to Calibrated Rankings: Conformal Elo Estimation for LLM Evaluation》关闭或降池；完整摘要显示“LLM-as-a-judge offers a cheaper alternative, but judge scores carry systematic errors - such as position bias, self-preference, or intransitivity - that can strongly miscalibrate the resulting rankings.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文写入与独立 post-write audit 已完成 |
| [SkillCAT: Contrastive, Assessment-Augmented and Topology-AwareSkill Self-Evolution for LLM Agents](https://arxiv.org/html/2606.13317v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《SkillCAT: Contrastive, Assessment-Augmented and Topology-AwareSkill Self-Evolution for LLM Agents》关闭或降池；完整摘要显示“We propose SkillCAT, a framework that decomposes this process into three stages. (1) Contrastive Causal Extraction (CCE) samples multiple trajectories per task and contrasts same-task success/failure pairs to find the evidence that explains outcome differences. (2) Assessment-Augmented Evolution (AAE) replays each candidate patch on source-task clones, retains only those that do not damage task outcomes, and then merges the retained patches hierarchically. (3) Topology-Aware Task Execution (TTE) compiles the evolved skills into routable sub-skill topologies, so that inference loads only task-relevant capability nodes.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；正文锚点：Trial Evidence 不能直接提交为 Workflow Revision |
| [Can I Buy Your KV Cache?](https://arxiv.org/html/2606.13361v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 1 + 2 = 5；原筛选把《Can I Buy Your KV Cache?》关闭或降池；完整摘要显示“Every agent re-runs prefill, the most compute-intensive step a large model takes, over identical text, only to rebuild a key-value (KV) cache identical to the one the agent before it just built.”。该增量直接改变 INFER-PREFILL 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 仅报告：INFER-PREFILL；exact-v1 尚不足以授权长期 Books 正文变化 |
| [Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents](https://arxiv.org/html/2606.13385v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents》关闭或降池；完整摘要显示“To capture these properties, we introduce StakeBench, a stakeholder-centric benchmark that systematically categorizes and attributes harm in real-world web agent systems for online shopping.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [MiniMax Sparse Attention](https://arxiv.org/pdf/2606.13392v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We introduce MiniMax Sparse Attention (MSA), a blockwise sparse attention built upon Grouped Query Attention (GQA).”，该机制在 MODEL-LONG-CONTEXT 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：MODEL-LONG-CONTEXT，[owner](../../../../books/part-02-model/22-long-context.md)；正文锚点：方案究竟移动了哪个瓶颈 |
| [Accelerating Speculative Diffusions via Block Verification](https://arxiv.org/pdf/2606.13426v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“In this work, we introduce a novel scheme that efficiently implements the original speculative sampling mechanism for diffusion models.”，该机制在 MULTIMODAL-GENERATIVE-PARADIGMS 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；正文锚点：Draft、Verify 与 Correct 不是同一件事 |
| [CQC-RAG: Robust Retrieval-Augmented Generation via Cross-Query Consistency](https://arxiv.org/html/2606.13438v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《CQC-RAG: Robust Retrieval-Augmented Generation via Cross-Query Consistency》关闭或降池；完整摘要显示“To address these limitations, we propose a Cross-Query Consistency Hypothesis: correct answers tend to maintain high confidence across semantically equivalent but syntactically diverse queries, whereas noise-induced hallucinations exhibit unstable confidence under such query variations.”。该增量直接改变 AGENT-RAG 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；正文锚点：Online Retrieval Pipeline |
| [Toward Instructions-as-Code: Understanding the Impact of Instruction Files on Agentic Pull Requests](https://arxiv.org/pdf/2606.13449v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“For better agent efficiency, developers create instruction files that guide the AI-agents, including how to navigate the project, locate the right components, run tests, respect best practices, and more.”，该机制在 AGENT-PROMPT 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-PROMPT，[owner](../../../../books/part-07-agent/74-prompt.md)；正文锚点：Prompt 生命周期 |
| [Budget-Constrained Step-Level Diffusion Caching](https://arxiv.org/pdf/2606.13496v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“In this work, we propose BudCache, which inverts this formulation: rather than letting per-step error thresholds dictate the runtime cost, we fix the compute budget in advance and search for the cache policy that best preserves the final output.”，该机制在 MULTIMODAL-GENERATIVE-PARADIGMS 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；正文锚点：Draft、Verify 与 Correct 不是同一件事 |
| [GF-DiT: Scheduling Parallelism for Diffusion Transformer Serving](https://arxiv.org/pdf/2606.13501v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We present GF-DiT, a policy-programmable runtime for elastic DiT serving that dynamically adapts the parallelism of running requests according to workload demands and service objectives.”，该机制在 INFER-SCHEDULING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点：迭代生成与流式会话需要显式 Progress State |
| [Multiagent Protocols with Aggregated Confidence Signals](https://arxiv.org/html/2606.13591v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《Multiagent Protocols with Aggregated Confidence Signals》关闭或降池；完整摘要显示“We introduce three protocols that produce a final answer along with a single aggregated confidence by first transforming raw confidence signals to make them comparable across models, then combining them via soft voting or a probability fusion we call Bayesian fusion.”。该增量直接改变 AGENT-MULTI-AGENT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；正文锚点：Message 不是 State |
| [See What I See, Know What I Think: Dense Latent Communication Across Heterogeneous Agents](https://arxiv.org/html/2606.13594v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《See What I See, Know What I Think: Dense Latent Communication Across Heterogeneous Agents》关闭或降池；完整摘要显示“Motivated by this, we propose dense alignment for heterogeneous KV-cache communication via a lightweight cross-model cache transformation and two-phase training: reconstruction followed by generation.”。该增量直接改变 AGENT-MULTI-AGENT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；正文写入与独立 post-write audit 已完成 |
| [Reward Modeling for Multi-Agent Orchestration](https://arxiv.org/html/2606.13598v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；完整摘要确认其研究 multi-agent orchestration reward modeling，属于 LLM multi-agent 范围，因此保留 Candidate。 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；现有 dynamic topology、credit、critical-path reward 与 role obligation 已覆盖该局部训练配方。 |
| [AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and Reproducibility](https://arxiv.org/pdf/2606.13608v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“Most benchmarks rely on fixed, LLM-centric harnesses that require heavy integration, create test-production mismatch, and limit fair comparison across diverse agent designs.”，该机制在 PLATFORM-EVALUATION-SYSTEM 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [One Polluted Page Is Enough: Evaluating Web Content Pollution in LLM Recommenders](https://arxiv.org/pdf/2606.13610v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；原筛选把《One Polluted Page Is Enough: Evaluating Web Content Pollution in LLM Recommenders》关闭或降池；完整摘要显示“We introduce FORGE (Fake Online Recommendations in Generative Environments), which locally rewrites real products in a frozen set of retrieved web pages into fake ones and measures how often the LLM recommends the fake product, across 225 real products in 15 categories and 5 consumer scenarios.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：从资产与信任边界开始 |
| [Valid Inference with Synthetic Data via Task Exchangeability](https://arxiv.org/html/2606.13629v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 3 + 2 + 3 = 8；原筛选把《Valid Inference with Synthetic Data via Task Exchangeability》关闭或降池；完整摘要显示“In this work, we propose statistical principles for using synthetic data in scientific research with provable validity guarantees.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文写入与独立 post-write audit 已完成 |
| [Recursive Agent Harnesses](https://arxiv.org/pdf/2606.13643v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We name and study the pattern between these two lines of work, where the recursive unit is a full agent harness with filesystem tools, code execution, and planning rather than a model call with no tools.”，该机制在 AGENT-WORKFLOW 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；正文锚点：State Machine 是基本模型 |
| [HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents](https://arxiv.org/pdf/2606.13663v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“We introduce \textbf{HyperTool}, a unified executable MCP-style tool interface that changes the model-visible unit of tool execution.”，该机制在 AGENT-TOOL-CALLING 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；正文锚点：Tool Contract |
| [EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments](https://arxiv.org/pdf/2606.13681v1) | 2026-06-12T08:00:00+08:00 ～ 2026-06-12T09:00:00+08:00 | 2 + 2 + 2 = 6；旧候选不继承旧 Complete/Books 标签；本轮以完整摘要重新确认“To address this gap, we introduce EvoArena, a benchmark suite that models environment changes as sequences of progressive updates across terminal, software, and social domains.”，该机制在 AGENT-MEMORY 下形成可定位的长期设计、执行或评价边界，因此保留 Candidate；独立终审已完成。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；正文锚点：Consolidation 与 Forgetting |

## 4. 证据与知识整合

### [Which Models Are Our Models Built On? Auditing Invisible Dependencies in Modern LLMs](https://arxiv.org/html/2606.12385v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：模型卡不足以表达递归 training dependencies；provenance 应以 artifact identity 和 operation-centered edges 递归解析生成、过滤、judge 与 selection 关系。

**State / data / control owner。** `TRAIN-DATA` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12385v1 §4 Evaluation; §5 Findings` 支持 `Public-artifact dependency reconstruction across target LLMs`；模型 `Agentic ModSleuth plus audited model artifacts`；硬件 `Not Disclosed — document analysis workload`；精度 `Not applicable`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12385v1 §3 Design of ModSleuth`；counterevidence locator：`arXiv:2606.12385v1 Appendix A verification; Appendix D disclosure gaps`。

**Trade-off / failure / coexistence / evolution。** 递归发现提高 lineage 但受公开文档缺失和 entity resolution 错误限制；它是 audit evidence，不是完整 SBOM guarantee。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12385:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12385v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12385:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/27-data.md`，Review notes 前正文锚点 `Data lineage 是训练可复现性的前提` 已承载长期命题；source 仅作受限证据。

### [Muse Spark Safety & Preparedness Report](https://arxiv.org/html/2606.12429v1)

**问题与机制。** 原筛选把《Muse Spark Safety & Preparedness Report》关闭或降池；完整摘要显示“In this report, we first present evaluations for catastrophic risk domains under Meta's Advanced AI Scaling Framework, along with the evidence that informed our launch decision.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`5.1 Evaluation Methodology`；可采用的最小机制命题是：In this report, we first present evaluations for catastrophic risk domains under Meta's Advanced AI Scaling Framework, along with the evidence that informed our launch decision.

**Evaluation proof。** `1.3 Evaluation Setup; 4.1 Primary Behavior Evaluation; 5 Content Safety Evaluations`；exact-v1 披露：In this report, we first present evaluations for catastrophic risk domains under Meta's Advanced AI Scaling Framework, along with the evidence that informed our launch decision.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；We therefore release Muse Spark as the underlying model of Meta AI. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [ToolSense: A Diagnostic Framework for Auditing Parametric Tool Knowledge in LLMs](https://arxiv.org/html/2606.12451v1)

**问题与机制。** 原筛选把《ToolSense: A Diagnostic Framework for Auditing Parametric Tool Knowledge in LLMs》关闭或降池；完整摘要显示“We introduce \textbf{ToolSense}, an open-source LLM-powered diagnostic framework that takes any tool catalog as input and automatically generates three benchmarks: a Realistic Retrieval Benchmark (RRB) with queries at three ambiguity tiers, an MCQ probing benchmark, and a QA probing benchmark.”。该增量直接改变 AGENT-TOOL-CALLING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 The ToolSense Framework; 5.5 Cross-Architecture Validation; Appendix H Cross-Architecture Probing Results`；可采用的最小机制命题是：We introduce \textbf{ToolSense}, an open-source LLM-powered diagnostic framework that takes any tool catalog as input and automatically generates three benchmarks: a Realistic Retrieval Benchmark (RRB) with queries at three ambiguity tiers, an MCQ probing benchmark, and a QA probing benchmark.

**Evaluation proof。** `3.3 Free-form Evaluation and Internalization Score; 4 Experimental Setup; 5 Results`；exact-v1 披露：Yet these benchmarks use verbose, fully-specified queries, and their evaluation applies constrained decoding that restricts outputs to valid token paths, neither reveals whether the model actually understands its tools.

**Limitations / non-proof。** `Limitations`；We open-source the ToolSense framework and the ToolBench diagnostic benchmarks at https://github.com/SAP/toolsense. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-TOOL-CALLING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/78-tool-calling.md`，Review notes 前正文锚点 `Tool Contract` 已承载长期命题；source 仅作受限证据。

### [Influence Factors on RAG Poisoning](https://arxiv.org/html/2606.12469v1)

<!-- claim:SF-2026-ARXIV-2606-12469:start -->
`Influence Factors on RAG Poisoning` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.12469v1`：Retrieval-Augmented Generation (RAG) systems enhance large language models by grounding responses in retrieved documents from external knowledge sources at inference time.

机制与 owner：Treat RAG poisoning as an interaction among retriever, top-k, chunking, database composition and generator, using a factorial design instead of a single attack rate. 状态/数据/控制 owner 固定为 `AGENT-RAG`；Method 锚点是 `§3 Methodology`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Results and Discussion` 只证明 `432-factorial grid over aligned 100-question HotpotQA/MS-MARCO subsets, retriever, top-k, chunking and database composition` 上、`llama-4-scout-17b-16e-instruct; openai-gpt-oss-120b` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：The 432 configurations use two curated 100-question subsets and two generators; factor effects are evidence for that grid, not universal retriever ordering. 反证/外推边界在 `§5 Conclusions`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。
<!-- claim:SF-2026-ARXIV-2606-12469:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/76-rag.md`，Review notes 前正文锚点 `RAG 安全必须覆盖完整状态生命周期` 已承载长期命题；source 仅作受限证据。

### [SAIGuard: Communication-State Simulation for Proactive Defense of LLM Multi-Agent Systems](https://arxiv.org/html/2606.12474v1)

**问题与机制。** 原筛选把《SAIGuard: Communication-State Simulation for Proactive Defense of LLM Multi-Agent Systems》关闭或降池；完整摘要显示“To address this, we propose a proactive defense framework for MAS security, namely a Simulation-aware Interception Guard (SAIGuard).”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methodology`；可采用的最小机制命题是：To address this, we propose a proactive defense framework for MAS security, namely a Simulation-aware Interception Guard (SAIGuard).

**Evaluation proof。** `4 Experiment; 4.1 Experiment Setup; Appendix C Detailed Experiment Setups`；exact-v1 披露：Experiments across diverse topologies and attack scenarios show that SAIGuard reduces attack success rates while maintaining MAS utility, outperforming reactive defenses.

**Limitations / non-proof。** `Limitations`；Experiments across diverse topologies and attack scenarios show that SAIGuard reduces attack success rates while maintaining MAS utility, outperforming reactive defenses. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `Multi-Agent 防御要在消息传播前模拟状态偏移` 已完成写入并通过独立 post-write audit。

### [ReCal: Reward Calibration for RL-based LLM Routing](https://arxiv.org/html/2606.12479v1)

**问题与机制。** 原筛选把《ReCal: Reward Calibration for RL-based LLM Routing》关闭或降池；完整摘要显示“To address these issues, we propose \textbf{ReCal}, a \textbf{\underline{Re}}ward \textbf{\underline{Cal}}ibration framework for RL-based LLM routing.”。该增量直接改变 INFER-SCHEDULING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`4 The Proposed Framework: ReCal`；可采用的最小机制命题是：To address these issues, we propose \textbf{ReCal}, a \textbf{\underline{Re}}ward \textbf{\underline{Cal}}ibration framework for RL-based LLM routing.

**Evaluation proof。** `5 Experiments; 5.1 Experimental Setup; 5.2 Main Results`；exact-v1 披露：Experiments on seven datasets demonstrate that ReCal consistently improves routing performance, and training stability over baselines.

**Limitations / non-proof。** `Limitations`；Code is available at https://anonymous.4open.science/r/ReCal. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `INFER-SCHEDULING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/56-inference-scheduling.md`，Review notes 前正文锚点 `Model Routing 与 Test-time Scaling 必须结算同一个 Budget` 已承载长期命题；source 仅作受限证据。

### [DynamicPTQ: Mitigating Activation Quantization Collapse via Residual-Stream Dynamics](https://arxiv.org/html/2606.12487v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：4-bit activation/KV PTQ 需要观察 residual stream 的 phase-wise jump，并对关键相位采用 mixed precision，而非只做静态 rotation smoothing。

**State / data / control owner。** `INFER-TENSORRT-LLM` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12487v1 §4 Experiments; §4.9 efficiency` 支持 `Perplexity, zero-shot QA, reasoning and efficiency across dense/MoE LLMs`；模型 `Multiple dense and MoE PTQ backbones`；硬件 `Disclosed in §4.2; exact accelerator remains paper-bound`；精度 `W4A4/KV4 with phase-aware higher precision`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12487v1 §3 Method; §3.3 policy`；counterevidence locator：`arXiv:2606.12487v1 §7 Discussion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** mixed precision 减少 collapse 却削弱全 4-bit memory/throughput 收益；新 backbone 需重新 calibration。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12487:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12487v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12487:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/49-tensorrt-llm.md`，Review notes 前正文锚点 `量化为什么不自动带来加速` 已承载长期命题；source 仅作受限证据。

### [ITME: Inference Tiered Memory Expansion with Disaggregated CXL-Hybrid Memories](https://arxiv.org/html/2606.12556v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：长 context state 可跨 GPU/host/CXL-hybrid/NVMe 构成 byte-addressable tier，并利用 model-weight/prefix access 可预测性做 multi-tier DMA prefetch。

**State / data / control owner。** `INFER-GPU-MEMORY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12556v1 §5 methodology; §6 evaluation` 支持 `Weight and KV offload across GPU, host, CXL and NVMe-oF tiers`；模型 `LLM inference configurations disclosed in §5.1`；硬件 `SK hynix CMM, PCIe Gen5 NVMe SSDs and FPGA prototype`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12556v1 §3 CXL-Hybrid Architecture; §4 ITME`；counterevidence locator：`arXiv:2606.12556v1 §8 Conclusion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** 扩容降低 HBM pressure，却增加预取错误、fabric contention 和硬件成本；不可预测 KV access 仍需普通 paging。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12556:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12556v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12556:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/54-gpu-memory.md`，Review notes 前正文锚点 `Weights 与 KV 的联合 HBM 预算：可提交的运行时精度页` 已承载长期命题；source 仅作受限证据。

### [Arbor: Tree Search as a Cognition Layer for Autonomous Agents](https://arxiv.org/html/2606.12563v1)

**问题与机制。** 原筛选把《Arbor: Tree Search as a Cognition Layer for Autonomous Agents》关闭或降池；完整摘要显示“Prior autonomous optimization systems operate on isolated targets with stateless evaluation.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methodology; 3.1 Problem Formulation; 3.3 Multi-Agent Architecture`；可采用的最小机制命题是：Prior autonomous optimization systems operate on isolated targets with stateless evaluation.

**Evaluation proof。** `4 Experiments; 4.2 Main Results`；exact-v1 披露：Prior autonomous optimization systems operate on isolated targets with stateless evaluation.

**Limitations / non-proof。** `5 Limitations; 6 Discussion and Future Work`；Arbor generalizes to multiple generations of hardware platform, and run-to-run variance is within 2 percentage points demonstrating that the method is hardware-agnostic and reproducible. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-WORKFLOW` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/81-workflow.md`，Review notes 前正文锚点 `State Machine 是基本模型` 已承载长期命题；source 仅作受限证据。

### [Beyond Attack Success Rate: Examining Trigger Leakage in Vision-Language Agentic Systems](https://arxiv.org/html/2606.12586v1)

**问题与机制。** 原筛选把《Beyond Attack Success Rate: Examining Trigger Leakage in Vision-Language Agentic Systems》关闭或降池；完整摘要显示“In this work, we formalize the failure of trigger precision as "trigger leakage": inputs that are visually or semantically close to the intended trigger and therefore inadvertently activate the attacker-specified behavior.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`§2 Threat Model; §3.2 Trigger Leakage; §§4.1–4.3 controlled probe and boundary supervision`；可采用的最小机制命题是：In this work, we formalize the failure of trigger precision as "trigger leakage": inputs that are visually or semantically close to the intended trigger and therefore inadvertently activate the attacker-specified behavior.

**Evaluation proof。** `§5 Agentic Workflow Evaluation`；exact-v1 披露：Current evaluations on such backdoors focus on clean accuracy and attack success rate (ASR), metrics that capture whether a trigger works, but not whether an attack is actually "precise" -- i.e. whether it triggers hidden behaviors only when intended.

**Limitations / non-proof。** `未定位独立 limitations；边界由 §2 attacker capability 与 §5 workload 推得`；Current evaluations on such backdoors focus on clean accuracy and attack success rate (ASR), metrics that capture whether a trigger works, but not whether an attack is actually "precise" -- i.e. whether it triggers hidden behaviors only when intended. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `Backdoor Evaluation 必须测 Trigger 邻域` 已完成写入并通过独立 post-write audit。

### [Strategic Decision Support for AI Agents](https://arxiv.org/html/2606.12587v1)

**问题与机制。** 原筛选把《Strategic Decision Support for AI Agents》关闭或降池；完整摘要显示“We propose a framework for strategic decision support for AI agents through an optimization problem that minimizes support usage subject to controlling a counterfactual missed-support error: the probability that the agent acts alone on instances where support would have materially improved its output.”。该增量直接改变 AGENT-PLANNING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：We propose a framework for strategic decision support for AI agents through an optimization problem that minimizes support usage subject to controlling a counterfactual missed-support error: the probability that the agent acts alone on instances where support would have materially improved its output.

**Evaluation proof。** `5 Experiments; Appendix B Additional Experimental Results`；exact-v1 披露：At the population level, we show that the optimal policy is a threshold rule on the value of support.

**Limitations / non-proof。** `6 Limitations and Future Work`；Experiments across these settings show that our method reliably controls the target error while substantially reducing support usage in practice. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-PLANNING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/79-planning.md`，Review notes 前正文锚点 `先校准不确定性，再决定行动、询问或探索` 已承载长期命题；source 仅作受限证据。

### [Keep Policy Gradient in Charge: Sibling-Guided Credit Distillation for Long-Horizon Tool-Use Agents](https://arxiv.org/html/2606.12634v1)

**问题与机制。** 原筛选把《Keep Policy Gradient in Charge: Sibling-Guided Credit Distillation for Long-Horizon Tool-Use Agents》关闭或降池；完整摘要显示“We introduce Sibling-Guided Credit Distillation (SGCD), which uses distillation for bounded credit weighting rather than as a competing actor loss.”。该增量直接改变 TRAIN-GRPO 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：We introduce Sibling-Guided Credit Distillation (SGCD), which uses distillation for bounded credit weighting rather than as a competing actor loss.

**Evaluation proof。** `5 Experiments; 5.2 Main results`；exact-v1 披露：Direct self-distillation can supply a denser signal, but in our experiments it can also destroy tool use by rehearsing teacher behavior without identifying which actions the verifier rewards.

**Limitations / non-proof。** `Limitations`；Dynamic sampling produces mixed successful and failed sibling rollouts; an external LLM summarizes their contrast into a training-only credit reference; and detached teacher/student divergence reshapes GRPO token advantages. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-GRPO` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/33-grpo.md`，Review notes 前正文锚点 `从一个终局标量到 Typed Credit：Reward 必须匹配决策边界` 已承载长期命题；source 仅作受限证据。

### [Eidola: Modeling Multi-GPU Network Communication Traffic in Distributed AI Workloads](https://arxiv.org/html/2606.12638v1)

**问题与机制。** 原筛选把《Eidola: Modeling Multi-GPU Network Communication Traffic in Distributed AI Workloads》关闭或降池；完整摘要显示“In this work, we introduce Eidola, a scalable extension to the gem5 simulation framework that enables detailed modeling of inter-GPU communication traffic.”。该增量直接改变 TRAIN-DISTRIBUTED-TRAINING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：In this work, we introduce Eidola, a scalable extension to the gem5 simulation framework that enables detailed modeling of inter-GPU communication traffic.

**Evaluation proof。** `4. Results; 5. Case Study: SyncMon; 5.4. Case Study Summary`；exact-v1 披露：Our results show that Eidola provides a flexible and scalable platform for studying inter-GPU communication and supports architectural exploration in modern distributed GPU systems.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Our results show that Eidola provides a flexible and scalable platform for studying inter-GPU communication and supports architectural exploration in modern distributed GPU systems. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-DISTRIBUTED-TRAINING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/36-distributed-training.md`，Review notes 前正文锚点 `从静态通信配置到受验证的 Collective Policy` 已承载长期命题；source 仅作受限证据。

### [Evoflux: Inference-Time Evolution of Executable Tool Workflows for Compact Agents](https://arxiv.org/html/2606.12674v1)

**问题与机制。** 原筛选把《Evoflux: Inference-Time Evolution of Executable Tool Workflows for Compact Agents》关闭或降池；完整摘要显示“We introduce Evoflux, an inference-time evolutionary search method that treats compact tool use as the repair of executable tool workflows.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method; A.4 Heuristic fallback method`；可采用的最小机制命题是：We introduce Evoflux, an inference-time evolutionary search method that treats compact tool use as the repair of executable tool workflows.

**Evaluation proof。** `4 Results and Analysis`；exact-v1 披露：These results show that execution-grounded search is more reliable under scarce teacher-trace budgets.

**Limitations / non-proof。** `Limitations`；These results show that execution-grounded search is more reliable under scarce teacher-trace budgets. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-WORKFLOW` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/81-workflow.md`，Review notes 前正文锚点 `Release 与 Optimization 必须共享 Workflow Identity` 已承载长期命题；source 仅作受限证据。

### [M*: A Modular, Extensible, Serving System for Multimodal Models](https://arxiv.org/html/2606.12688v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：复合多模态模型的 serving contract 应从固定 stage DAG 演进为 model graph + named walks，显式支持 seq/parallel/loop/dynamic-loop/stream 与 component placement。

**State / data / control owner。** `INFER-KSERVE-TOPOLOGY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12688v1 §4 Evaluation; Appendix I reproducibility` 支持 `BAGEL, Qwen3-Omni, Orpheus and V-JEPA2 composite workloads`；模型 `BAGEL-7B, Qwen3-Omni-30B-A3B, Orpheus-3B, V-JEPA2`；硬件 `Single 4×H100 node or 8×H200 node`；精度 `Model-specific; not normalized as one precision`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12688v1 §3 Walk Graph; §§3.1–3.3`；counterevidence locator：`arXiv:2606.12688v1 Appendix H Limitations`。

**Trade-off / failure / coexistence / evolution。** 通用 graph runtime 减少 glue code，却把 state machine、placement、tensor transport 与 per-component batch 变成新控制面；专用引擎仍可能更简单。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12688:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12688v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12688:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/53-kserve-llm.md`，Review notes 前正文锚点 `组件与 Ownership` 已承载长期命题；source 仅作受限证据。

### [SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems](https://arxiv.org/html/2606.12703v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Persistent memory poisoning 的 certified boundary 必须在 write-time 做 cryptographic provenance，并在 query-time 对 authenticated adversary 做 randomized ablation 与 verdict aggregation。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12703v1 §VII Evaluation` 支持 `15 enterprise scenarios; 3,150 repeated plus 450 production-scale trials`；模型 `Persistent RAG-agent configurations; second-agent generality check`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12703v1 §III threat model; §§IV–VI impossibility/SMSR/certificate`；counterevidence locator：`arXiv:2606.12703v1 §VIII Discussion; provenance-key and smoothing assumptions`。

**Trade-off / failure / coexistence / evolution。** HMAC 阻止 unsigned injection 不处理合法凭据滥用；smoothing 增加多次 retrieval/inference 成本且证书依赖 threat bound。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12703:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12703v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12703:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Smarter Saboteurs, Better Fixers: Scaling & Security in Linear Multi-Agent Workflows](https://arxiv.org/html/2606.12709v1)

**问题与机制。** 原筛选把《Smarter Saboteurs, Better Fixers: Scaling & Security in Linear Multi-Agent Workflows》关闭或降池；完整摘要显示“Attackers may leverage prompt-injection or jailbreaking to sabotage individual agents within MAS workflows, but the interaction between model scaling and system-level resilience remains poorly understood.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methodology`；可采用的最小机制命题是：Attackers may leverage prompt-injection or jailbreaking to sabotage individual agents within MAS workflows, but the interaction between model scaling and system-level resilience remains poorly understood.

**Evaluation proof。** `3.2 Four Experimental Configurations; 3.4 Models, Benchmark, and Evaluation; 4 Results`；exact-v1 披露：Our experiments across scales of two open-weight model families on the HumanEval benchmark reveal a compliance-correction symmetry: larger models are far more likely to faithfully execute malicious instructions, with the control-to-malicious performance drop reaching 53.7pp at 27B in uncorrected pipelines.

**Limitations / non-proof。** `5.1 Limitations and Future Work`；However, appending a lightweight terminal Fixer stage collapses this to 0.6pp and restores statistical parity with control-level performance, demonstrating that strictly linear collaboration structures can be viable and resilient to adversaries at this scale, and suggesting that the brittleness previously attributed to linear topology may stem from a lack of correction. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [PI-Hunter: Automated Red-Teaming for Exposing and Localizing Prompt Injections](https://arxiv.org/html/2606.12737v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Prompt-injection red team 应从 attack-success search 扩为 source-aware test construction、feedback evolution、verification 与 localization，输出可修复 attack surface。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12737v1 §4 Experiments; Appendices B–D` 支持 `Multiple agent benchmarks, architectures, attacks and defenses`；模型 `Agent and evaluator models disclosed in §4.1`；硬件 `Not Disclosed — hosted model hardware`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12737v1 §3 PI-Hunter; §§3.1–3.3`；counterevidence locator：`arXiv:2606.12737v1 §4.4 ablations; §5 Conclusion; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** 更广 exposure 不等于防御；搜索受 mutation/evaluator repertoire 约束，held-out attacks 与 runtime enforcement 仍必要。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12737:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12737v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12737:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Prefill Awareness in Large Language Models](https://arxiv.org/html/2606.12747v1)

**问题与机制。** 原筛选把《Prefill Awareness in Large Language Models》关闭或降池；完整摘要显示“If AI models can recognize and act on the fact their prior assistant messages have been inserted or edited, the effectiveness and validity of these methods could be compromised.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`§3 Measuring Prefill Awareness; §4 Prefill Awareness in Agentic Settings`；可采用的最小机制命题是：If AI models can recognize and act on the fact their prior assistant messages have been inserted or edited, the effectiveness and validity of these methods could be compromised.

**Evaluation proof。** `§§3.2–3.3; §§4.1–4.3; Appendices A–C`；exact-v1 披露：Safety-relevant studies of language models, including alignment and jailbreaking evaluations and AI control protocols, often rely on prefilling model outputs.

**Limitations / non-proof。** `§5.1 Limitations; Appendix B.4 Formatting Artifacts`；We recommend that model developers track this capability in frontier systems. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Prefill 是 Harness 输入，不是模型自然历史` 已完成写入并通过独立 post-write audit。

### [Detecting Functional Memorization in Code Language Models](https://arxiv.org/html/2606.12764v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Code training-data audit 必须检测 functional equivalence，而不能只依赖文本 overlap；应以 exposed target 对未 exposed reference 做 counterfactual execution comparison。

**State / data / control owner。** `TRAIN-DATA` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12764v1 §4 Results; Appendices A–C/E` 支持 `Python function-signature continuations with execution-based and LLM-judge functional comparison`；模型 `OLMo-3-32B midtrained target versus pretrained reference`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12764v1 §3 Counterfactual functional memorization`；counterevidence locator：`arXiv:2606.12764v1 §4 result scope; no dedicated limitations section`。

**Trade-off / failure / coexistence / evolution。** execution 更接近语义但覆盖有限输入；LLM judge 是受 operating point 约束的 proxy，不能替代 license/provenance evidence。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12764:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12764v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12764:end -->

**V3 Books Decision。** `Integrate` → `books/part-04-training-system/27-data.md`，Review notes 前正文锚点 `Code Memorization 要验证功能，而不只验证文本` 已完成写入并通过独立 post-write audit。

### [Rigel: Reverse-Engineering the Metal 4.1 Tensor Compute Path on the Apple M4 Max GPU](https://arxiv.org/html/2606.12765v1)

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Low-precision backend contract 必须通过 checksum/provenance microbench 分离 interface support、真正加速、accumulator width、execution rail 与 fragment layout。

**State / data / control owner。** `INFER-TENSORRT-LLM` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.12765v1 §§4–8 measurements and fused-kernel result` 支持 `Metal 4.1 matmul2d microbenchmarks and fused GEMM+bias+GELU`；模型 `Metal Performance Primitives tensor path`；硬件 `Single Apple M4 Max GPU`；精度 `fp8 E4M3, fp16, accumulator ≥fp32 evidence`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.12765v1 §3 Methodology; §§4–8 characterization`；counterevidence locator：`arXiv:2606.12765v1 §10 Discussion and limitations`。

**Trade-off / failure / coexistence / evolution。** 单芯片逆向结果不能外推其他 Apple generations；fp8 在该硬件省 footprint 而非提高吞吐。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-12765:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12765v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-12765:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/49-tensorrt-llm.md`，Review notes 前正文锚点 `量化为什么不自动带来加速` 已承载长期命题；source 仅作受限证据。

### [ProPlay: Procedural World Models for Self-Evolving LLM Agents](https://arxiv.org/html/2606.12780v1)

**问题与机制。** 原筛选把《ProPlay: Procedural World Models for Self-Evolving LLM Agents》关闭或降池；完整摘要显示“We introduce ProPlay, a procedural world model that supports procedure-level preplay, where agents can rehearse future procedural paths using the learned world knowledge.”。该增量直接改变 AGENT-PLANNING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methodology`；可采用的最小机制命题是：We introduce ProPlay, a procedural world model that supports procedure-level preplay, where agents can rehearse future procedural paths using the learned world knowledge.

**Evaluation proof。** `4 Experiments; 4.1 Experimental Setting; 4.2 Results`；exact-v1 披露：Experiments on public benchmarks show that ProPlay consistently improves environment understanding and self-evolution capability over strong baselines.

**Limitations / non-proof。** `4.4 Discussion; Limitations`；Self-evolving agents are expected to improve through interaction without external supervision, but this remains difficult in partially observable environments where agents must explore actively, learn from limited feedback, and decide when to trust prior experience. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-PLANNING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/79-planning.md`，Review notes 前正文锚点 `从目标到状态图` 已承载长期命题；source 仅作受限证据。

### [The Containment Gap: How Deployed Agentic AI Frameworks Fail Public-Facing Safety Requirements](https://arxiv.org/pdf/2606.12797v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：containment 必须在 perception/reasoning/execution/memory 边界分别绑定 validated write、policy gate 与 runtime monitor，而不能从 framework availability 推断 secure-by-default。

**State / data / control owner。** `PLATFORM-SECURITY` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.12797v1 §2.3 Six Containment Principles; §3 Audit Methodology`；evaluation locator 为 `arXiv:2606.12797v1 §§4–5 Compliance Matrix and Experimental Validation`；counterevidence locator 为 `arXiv:2606.12797v1 §3 point-in-time audit limitation; §5.5 Limitations of Lightweight Containment`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 三框架点时审计与合成 welfare agent 只证明结构缺口可被触发；regex validator 不是通用安全证明，framework 版本漂移需要重审。

<!-- claim:SF-2026-ARXIV-2606-12797:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12797v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-12797:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [LoHoSearch: Benchmarking Long-Horizon Search Agents Beyond the Human Difficulty Ceiling](https://arxiv.org/html/2606.12837v1)

**问题与机制。** 原筛选把《LoHoSearch: Benchmarking Long-Horizon Search Agents Beyond the Human Difficulty Ceiling》关闭或降池；完整摘要显示“To address this, we introduce LoHoSearch (Long-Horizon Search Agents), a challenging benchmark comprising 544 human-verified questions across 11 domains.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：To address this, we introduce LoHoSearch (Long-Horizon Search Agents), a challenging benchmark comprising 544 human-verified questions across 11 domains.

**Evaluation proof。** `3 Experiments; 3.1 Experimental Settings; 3.2 Main Results`；exact-v1 披露：Our evaluation demonstrates that even the strongest model achieves only 34.74% accuracy, and existing context management strategies (best +6.8%) yield far smaller gains than on prior benchmarks.

**Limitations / non-proof。** `Limitations`；Our evaluation demonstrates that even the strongest model achieves only 34.74% accuracy, and existing context management strategies (best +6.8%) yield far smaller gains than on prior benchmarks. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [HarnessBridge: Learnable Bidirectional Controller for LLM Agent Harness](https://arxiv.org/html/2606.12882v1)

**问题与机制。** 原筛选把《HarnessBridge: Learnable Bidirectional Controller for LLM Agent Harness》关闭或降池；完整摘要显示“We introduce HarnessBridge, a lightweight learnable harness controller that parameterizes the agent--environment interface as a bidirectional projection.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method`；可采用的最小机制命题是：We introduce HarnessBridge, a lightweight learnable harness controller that parameterizes the agent--environment interface as a bidirectional projection.

**Evaluation proof。** `4 Experiments; 4.1 Experiment Setup; 4.2 Main Results`；exact-v1 披露：On Terminal-Bench~2.0 and SWE-bench Verified, HarnessBridge matches or surpasses strong specialized harnesses while substantially reducing token usage and trajectory length, and generalizes from smaller generators to larger commercial models.

**Limitations / non-proof。** `Appendix E Limitation`；Large language models are increasingly deployed as agents for long-horizon tasks, yet their performance is shaped not only by model capability and environment design, but also by the harness that mediates agent--environment interaction. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-WORKFLOW` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/81-workflow.md`。其 bidirectional projection 是既有 harness state machine、compiler/executor 与 learned transition 合同的一种局部实现，不形成新的长期 owner、handoff 或 release contract。

### [SENTINEL: Failure-Driven Reinforcement Learning for Training Tool-Using Language Model Agents](https://arxiv.org/html/2606.12908v1)

**问题与机制。** 原筛选把《SENTINEL: Failure-Driven Reinforcement Learning for Training Tool-Using Language Model Agents》关闭或降池；完整摘要显示“We propose SENTINEL, a failure-driven reinforcement learning framework that turns the Solver's rollout failures into targeted training tasks.”。该增量直接改变 TRAIN-DATA 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method; 3.1 Problem Formulation; 3.2 Framework Overview`；可采用的最小机制命题是：We propose SENTINEL, a failure-driven reinforcement learning framework that turns the Solver's rollout failures into targeted training tasks.

**Evaluation proof。** `4 Experiments; 4.1 Experimental Setup; 4.2 Main Results`；exact-v1 披露：These results demonstrate that model failures provide an effective and scalable source of targeted training signal for improving tool-using language model agents.

**Limitations / non-proof。** `Limitations`；These results demonstrate that model failures provide an effective and scalable source of targeted training signal for improving tool-using language model agents. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-DATA` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/27-data.md`，Review notes 前正文锚点 `Data lineage 是训练可复现性的前提` 已承载长期命题；source 仅作受限证据。

### [MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems](https://arxiv.org/html/2606.12918v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：多 Agent red-team 要把 agent marginal safety contribution、coalition selection 与 role-aware collusive perturbation纳入同一 closed loop。

**State / data / control owner。** `PLATFORM-SECURITY` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.12918v1 §§3–4 Shapley-guided coalition attribution and MAStrike`；evaluation locator 为 `arXiv:2606.12918v1 §5 experiments across hierarchical MAS environments`；counterevidence locator 为 `arXiv:2606.12918v1 §6 discussion/limitations and benchmark threat-model scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** Shapley 估计与因果诊断增加 calls 且依赖任务分布；合成 coalition 攻击不提供生产发生率，也不覆盖未知 topology。

<!-- claim:SF-2026-ARXIV-2606-12918:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12918v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-12918:end -->

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `Collusive Red-team 要从节点扩展到 Coalition` 已完成写入并通过独立 post-write audit。

### [MARS: Margin-Adversarial Risk-controlled Stopping for Parallel LLM Test-time Scaling](https://arxiv.org/html/2606.12935v1)

**问题与机制。** 原筛选把《MARS: Margin-Adversarial Risk-controlled Stopping for Parallel LLM Test-time Scaling》关闭或降池；完整摘要显示“Based on this observation, we introduce MARS, a margin-adversarial stopping rule that estimates which active traces are likely to change their answers and stops once the leader remains safe under a conservative bound on future vote movement.”。该增量直接改变 INFER-SCHEDULING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`§2 Margin-Adversarial Risk-controlled Stopping; Appendix B derivation`；可采用的最小机制命题是：Based on this observation, we introduce MARS, a margin-adversarial stopping rule that estimates which active traces are likely to change their answers and stops once the leader remains safe under a conservative bound on future vote movement.

**Evaluation proof。** `§3 Experiments; Appendix E Full experimental results`；exact-v1 披露：Across three reasoning models and three competition-math benchmarks, MARS saves 25-47% of self-consistency tokens and 14-29% on top of DeepConf Online, a strong confidence-weighted baseline that already filters and truncates weak traces, while matching the accuracy of the corresponding full-budget baselines.

**Limitations / non-proof。** `Appendix F Limitations & Broader impacts`；Across three reasoning models and three competition-math benchmarks, MARS saves 25-47% of self-consistency tokens and 14-29% on top of DeepConf Online, a strong confidence-weighted baseline that already filters and truncates weak traces, while matching the accuracy of the corresponding full-budget baselines. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `INFER-SCHEDULING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-05-inference-system/56-inference-scheduling.md`，Review notes 前正文锚点 `Parallel Voting 的提前停止必须覆盖未完成 Trace 的最坏移动` 已完成写入并通过独立 post-write audit。

### [Multi-Turn Reasoning When Context Arrives in Pieces: Scalable Sharding and Memory-Augmented RL](https://arxiv.org/html/2606.12941v1)

**问题与机制。** 原筛选把《Multi-Turn Reasoning When Context Arrives in Pieces: Scalable Sharding and Memory-Augmented RL》关闭或降池；完整摘要显示“To make such training scalable, we introduce a low-cost sharding pipeline that converts single-turn QA datasets into multi-turn fragmented-information episodes, eliminating the need for hours of manual annotation.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methodology`；可采用的最小机制命题是：To make such training scalable, we introduce a low-cost sharding pipeline that converts single-turn QA datasets into multi-turn fragmented-information episodes, eliminating the need for hours of manual annotation.

**Evaluation proof。** `4 Experimental Setup; 5 Results`；exact-v1 披露：We show that this Lost in Conversation degradation can be substantially mitigated by training models to maintain a compact rolling memory instead of attending to a growing history.

**Limitations / non-proof。** `Limitations`；Training only on sharded GSM8K, our memory-augmented policy significantly improves multi-turn accuracy and generalises zero-shot to harder math and out-of-domain long-context QA. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MEMORY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory](https://arxiv.org/html/2606.12945v1)

**问题与机制。** 原筛选把《Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory》关闭或降池；完整摘要显示“We propose a multi-factor memory value function V(m)=\sum_i w_i f_i(m) over seven interpretable factors (emotional intensity, goal relevance, value alignment, self/user relevance, task utility, reliability, and usage history) drawn from cognitive psychology, whose weights are learned from a downstream objective by a gradient-free optimiser, and whose single scalar uniformly controls encoding depth, forget risk, and retrieval rank.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`Method`；可采用的最小机制命题是：We propose a multi-factor memory value function V(m)=\sum_i w_i f_i(m) over seven interpretable factors (emotional intensity, goal relevance, value alignment, self/user relevance, task utility, reliability, and usage history) drawn from cognitive psychology, whose weights are learned from a downstream objective by a gradient-free optimiser, and whose single scalar uniformly controls encoding depth, forget risk, and retrieval rank.

**Evaluation proof。** `Experiments`；exact-v1 披露：We make a methodological point: on LongMemEval, scoring goal relevance against the held-out evaluation question saturates gold-evidence retention at \approx 0.98 -- this measures retrieval, not forgetting.

**Limitations / non-proof。** `Discussion; Limitations`；The substrate is open-source; all experiments run on a single CPU with no API calls. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MEMORY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-Based Multi-Agent Systems](https://arxiv.org/pdf/2606.12950v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：LLM-MAS serving scheduler 必须持有 workflow/stage identity、output-length与memory预测、分层weight cache/elastic memory、跨集群routing及全局workflow priority。

**State / data / control owner。** `INFER-SCHEDULING` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.12950v1 §§3–4 Maestro design and hierarchical scheduling`；evaluation locator 为 `arXiv:2606.12950v1 §§5–6 prototype and trace-driven evaluation`；counterevidence locator 为 `arXiv:2606.12950v1 No dedicated limitations section — evaluation scope and prediction/cold-start boundaries are stated in §§5–6`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 预测误差、模型 churn 与跨集群网络会破坏局部最优；单集群或静态 model set 下简单队列/固定部署仍更可验证。

<!-- claim:SF-2026-ARXIV-2606-12950:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12950v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-12950:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/56-inference-scheduling.md`，Review notes 前正文锚点 `Model Routing 与 Test-time Scaling 必须结算同一个 Budget` 已承载长期命题；source 仅作受限证据。

### [ScaleAcross: Designing Multi-Data-Center Infrastructure for Geo-Distributed AI Training](https://arxiv.org/html/2606.12963v1)

**问题与机制。** 原筛选把《ScaleAcross: Designing Multi-Data-Center Infrastructure for Geo-Distributed AI Training》关闭或降池；完整摘要显示“Such deployments introduce system-level challenges arising from synchronization-intensive communication, cross-site data exchange, and wide-area latency constraints.”。该增量直接改变 TRAIN-DISTRIBUTED-TRAINING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`2.2 Scalability Limitations of Legacy VLAN Architectures; 6.4 Emulation and Evaluation Frameworks`；可采用的最小机制命题是：Such deployments introduce system-level challenges arising from synchronization-intensive communication, cross-site data exchange, and wide-area latency constraints.

**Evaluation proof。** `5 Experiments; 6.4 Emulation and Evaluation Frameworks`；exact-v1 披露：Results provide insights into traffic distribution, resilience, and infrastructure behavior in geo-distributed AI environments, highlighting the potential of reproducible multi-data-center infrastructure frameworks for scalable distributed AI training.

**Limitations / non-proof。** `2.2 Scalability Limitations of Legacy VLAN Architectures`；Results provide insights into traffic distribution, resilience, and infrastructure behavior in geo-distributed AI environments, highlighting the potential of reproducible multi-data-center infrastructure frameworks for scalable distributed AI training. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `TRAIN-DISTRIBUTED-TRAINING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-04-training-system/36-distributed-training.md`，Review notes 前正文锚点 `跨地域电力约束会把全局同步改成层级且有陈旧度的聚合` 已承载长期命题；source 仅作受限证据。

### [Trajectory-Level Redirection Attacks on Vision-Language-Action Models](https://arxiv.org/pdf/2606.12978v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：VLA 安全测试必须把 prompt 视为跨闭环复用的 trajectory control input，并以最终物理 outcome 而非单步 action/文本相似度判定 redirection。

**State / data / control owner。** `MULTIMODAL-EMBODIED-VLA` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.12978v1 §§3–4 command-preserving trajectory-redirection threat model and search`；evaluation locator 为 `arXiv:2606.12978v1 §5 simulation and hardware experiments`；counterevidence locator 为 `arXiv:2606.12978v1 §6 limitations and fixed-policy/environment threat-model boundary`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** on-policy search成本高且依赖可 rollout 环境；有限任务与硬件结果不证明任意 VLA 可攻击，也不取代 action/runtime safety envelope。

<!-- claim:SF-2026-ARXIV-2606-12978:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.12978v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-12978:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`，Review notes 前正文锚点 `Training-only Foresight 不是 Persistent World State` 已承载长期命题；source 仅作受限证据。

### [The Illusion of Multi-Agent Advantage](https://arxiv.org/pdf/2606.13003v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：MAS 评价应固定计算预算并显式检查 task decomposition/context separation/parallelism；增加 agents 或自动生成复杂 topology 不构成优势。

**State / data / control owner。** `AGENT-MULTI-AGENT` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13003v1 §§2–3 comparison protocol and diagnostic task structure`；evaluation locator 为 `arXiv:2606.13003v1 §4 SAS/MAS cost-normalized evaluation and deconstruction`；counterevidence locator 为 `arXiv:2606.13003v1 §5 limitations and benchmark/task-family scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 现有 Ch82 已拥有 task coupling、coordinator headroom、agent-count non-monotonicity 与 single-agent fallback；该论文仅作为受限证据，不重复追加。

<!-- claim:SF-2026-ARXIV-2606-13003:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13003v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13003:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/82-multi-agent.md`，Review notes 前正文锚点 `Message 不是 State` 已承载长期命题；source 仅作受限证据。

### 分母前关闭（保留审计轨迹）：AI Peer Review Presentation-only Revisions

独立复核结论：该 family 的对象是 AI for Science 中的论文评审操纵；当前范围明确暂缓该阶段，以下作者侧审阅轨迹不计入 Candidate 或 Books。

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：AI reviewer release gate 必须加入 evidence-invariant presentation counterfactual，防止固定方法/结果仅靠 framing 改写评分。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13044v1 §§3–4 adversarial-repackaging threat model and attack`；evaluation locator 为 `arXiv:2606.13044v1 §5 three-reviewer evaluation and strategy ablations`；counterevidence locator 为 `arXiv:2606.13044v1 §6 limitations and reviewer/paper-sample scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** presentation counterfactual 会增加评测成本且可能把正常清晰度改善误判为攻击；75.1% 是特定 reviewer/sample 结果，不是通用常数。

<!-- claim:SF-2026-ARXIV-2606-13044:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13044v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13044:end -->

**V3 Books Decision。** `Pre-denominator Close — Not applicable`；保留审计轨迹但不计入 Candidate、Books 分布或 root 写入队列。

### [EA-WM: Event-Aware World Models with Task-Specification Grounding for Long-Horizon Manipulation](https://arxiv.org/pdf/2606.13053v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：world-model planning 的 imagined future 必须解码为 task-grounded event/predicate state，再用progress/semantic/physical/uncertainty verifier决定 action proposal 是否可执行。

**State / data / control owner。** `MULTIMODAL-WORLD-MODELS` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13053v1 §§3–4 EA-WM event-aware model and task-specification grounding`；evaluation locator 为 `arXiv:2606.13053v1 §5 navigation/manipulation evaluations`；counterevidence locator 为 `arXiv:2606.13053v1 §6 limitations and task/predicate coverage`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** predicate schema 增加标注、decoder 与 calibration 成本；有限 manipulation/navigation 任务不证明开放世界 predicate 完整或物理可靠。

<!-- claim:SF-2026-ARXIV-2606-13053:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13053v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13053:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-03-multimodal-world-models/25-multimodal-world-models.md`，Review notes 前正文锚点 `从平均预测误差到分层的 Rollout Admission` 已承载长期命题；source 仅作受限证据。

### [The Emergence of Autonomous Penetration Capabilities in Large Language Model-Powered AI Systems](https://arxiv.org/html/2606.13079v1)

**问题与机制。** 原筛选把《The Emergence of Autonomous Penetration Capabilities in Large Language Model-Powered AI Systems》关闭或降池；完整摘要显示“Within this broader red-line scenario, autonomous penetration represents a core enabling capability and subtask: the ability of LLM-powered AI systems to independently conduct adversarial operations against a target server without human intervention, identify and exploit vulnerabilities, and obtain unauthorized access or control.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methods`；可采用的最小机制命题是：Within this broader red-line scenario, autonomous penetration represents a core enabling capability and subtask: the ability of LLM-powered AI systems to independently conduct adversarial operations against a target server without human intervention, identify and exploit vulnerabilities, and obtain unauthorized access or control.

**Evaluation proof。** `2.3 Evaluation targets; 3.3 Details of the experimental setups; 4 Results`；exact-v1 披露：However, existing evaluations often employ opaque methodologies, rely on unrealistic or overly simplified penetration-testing scenarios, or provide LLMs with excessive prior knowledge and task-specific guidance, and cannot accurately capture the extent to which modern AI systems can autonomously perform this core capability within broader high-impact cyberattack scenarios.

**Limitations / non-proof。** `2.2 Related works and limitations; 5 Discussion`；To address these limitations, we construct a new autonomous penetration evaluation framework consisting of two components: target servers and agent scaffolding. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [Scale Buys Interpolation, Structure Buys a Horizon: Certified Predictability for Equivariant World Models](https://arxiv.org/pdf/2606.13092v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：world-model rollout 的可信边界应由 configuration/horizon/resolution certificate 与自我 abstention 表达，不能由平均预测误差替代。

**State / data / control owner。** `MULTIMODAL-WORLD-MODELS` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13092v1 §§2–4 equivariance, orbit-transfer and Lyapunov certificates`；evaluation locator 为 `arXiv:2606.13092v1 §5 synthetic/learned/public-model evaluations`；counterevidence locator 为 `arXiv:2606.13092v1 No dedicated limitations section — certificate assumptions, held-out divergence cross-check and abstention boundary in §§2–5`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** exact/approximate equivariance与局部 Jacobian assumptions 限制证书；失配时必须 abstain/re-observe，不能把 candidate horizon 当安全保证。

<!-- claim:SF-2026-ARXIV-2606-13092:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13092v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13092:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-03-multimodal-world-models/25-multimodal-world-models.md`，Review notes 前正文锚点 `从平均预测误差到分层的 Rollout Admission` 已承载长期命题；source 仅作受限证据。

### [G-Long: Graph-Enhanced Memory Management for Efficient Long-Term Dialogue Agents](https://arxiv.org/html/2606.13115v1)

**问题与机制。** 原筛选把《G-Long: Graph-Enhanced Memory Management for Efficient Long-Term Dialogue Agents》关闭或降池；完整摘要显示“To address these limitations, we propose G-Long, a graph-enhanced framework that utilizes a fine-tuned small Language Model (sLM) for structured triplet extraction and associative retrieval, significantly reducing operational costs.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methodology; 3.1 Framework Overview; 4.5 Systematic Comparison on Diverse Memory Architectures`；可采用的最小机制命题是：To address these limitations, we propose G-Long, a graph-enhanced framework that utilizes a fine-tuned small Language Model (sLM) for structured triplet extraction and associative retrieval, significantly reducing operational costs.

**Evaluation proof。** `4 Experiments; 4.1 Experimental Setup; 4.2 Main Results on Response Generation`；exact-v1 披露：Extensive experiments across diverse benchmarks demonstrate that G-Long achieves state-of-the-art performance in both response generation and memory retrieval, yielding performance gains of up to 9.8% in response quality on MSC and 40.8% in retrieval recall on LME, while significantly minimizing computational overhead.

**Limitations / non-proof。** `Limitations`；While Large Language Models (LLMs) have advanced open-domain dialogue systems, maintaining long-term consistency remains a challenge due to inherent limitations in long-context reasoning and the inefficiency of processing extensive raw text. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MEMORY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [EvoBrowseComp: Benchmarking Search Agents on Evolving Knowledge](https://arxiv.org/html/2606.13120v1)

**问题与机制。** 原筛选把《EvoBrowseComp: Benchmarking Search Agents on Evolving Knowledge》关闭或降池；完整摘要显示“In this paper, we introduce EvoBrowseComp, an evolving benchmark of 400 English and 400 Chinese contamination-free complex questions synthesized via live-web traversal.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：In this paper, we introduce EvoBrowseComp, an evolving benchmark of 400 English and 400 Chinese contamination-free complex questions synthesized via live-web traversal.

**Evaluation proof。** `2.4 Evaluation Protocol; 3 Experiments; 3.1 Experimental Setup`；exact-v1 披露：Search Agents -- large language models augmented with search tools -- have intensified the need for future-proof evaluation benchmarks.

**Limitations / non-proof。** `Limitations`；It establishes a scalable paradigm for auto-updatable, high-difficulty benchmarking that keeps pace with both evolving world knowledge and advancing agent capabilities. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [MiniPIC: Flexible Position-Independent Caching in <100LOC](https://arxiv.org/html/2606.13126v1)

**问题与机制。** 原筛选把《MiniPIC: Flexible Position-Independent Caching in <100LOC》关闭或降池；完整摘要显示“We present Minimalistic PIC (MiniPIC): a minimal, flexible and fast vLLM design built from two ingredients: positional-encoding-free KV cache and user-controlled cache-reuse primitives.”。该增量直接改变 INFER-KV-CACHE 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methods`；可采用的最小机制命题是：We present Minimalistic PIC (MiniPIC): a minimal, flexible and fast vLLM design built from two ingredients: positional-encoding-free KV cache and user-controlled cache-reuse primitives.

**Evaluation proof。** `4 Experiments`；exact-v1 披露：On 2WikiMultihopQA, MiniPIC with interleaved scheduling improves prefill throughput by 49% over baseline vLLM, reduces cached-span time-to-first-token by up to two orders of magnitude, preserves the linear prefill scaling of uncached spans, and incurs only 5.7% worst-case overhead.

**Limitations / non-proof。** `5 Discussion and Related Work`；On 2WikiMultihopQA, MiniPIC with interleaved scheduling improves prefill throughput by 49% over baseline vLLM, reduces cached-span time-to-first-token by up to two orders of magnitude, preserves the linear prefill scaling of uncached spans, and incurs only 5.7% worst-case overhead. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `INFER-KV-CACHE` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`，Review notes 前正文锚点 `任意 Chunk 复用必须先修复 Position 与 Conditioning Seam` 已承载长期命题；source 仅作受限证据。

### [Iterative Visual Thinking and the Self-Correction Mirage in VLM Grounding](https://arxiv.org/html/2606.13156v1)

**问题与机制。** 原筛选把《Iterative Visual Thinking and the Self-Correction Mirage in VLM Grounding》关闭或降池；完整摘要显示“A natural way to bring this to spatial grounding is visual self-correction: the model predicts a bounding box, sees it rendered on the image, and refines it over several steps.”。该增量直接改变 PLATFORM-EVALUATION-SYSTEM 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method`；可采用的最小机制命题是：A natural way to bring this to spatial grounding is visual self-correction: the model predicts a bounding box, sees it rendered on the image, and refines it over several steps.

**Evaluation proof。** `4 Experiments; 4.2 Main Results; 4.4 Qualitative Results`；exact-v1 披露：We show this gain is a measurement mirage.

**Limitations / non-proof。** `4.5 Limitations`；Self-verification confidence correlates only weakly with correctness (r about 0.22), and a counterfactual overlay shows the loop reacts to the presence of a rendered box rather than its correctness. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-EVALUATION-SYSTEM` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents](https://arxiv.org/pdf/2606.13174v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：用户 correction 只有被编译为 atomic rule 与 pre-completion runtime check 才能跨 session 成为 enforcement；memory lookup 仍只是 preference evidence。

**State / data / control owner。** `AGENT-WORKFLOW` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13174v1 §§3–4 TRACE rule acquisition and compiled enforcement`；evaluation locator 为 `arXiv:2606.13174v1 §5 ClawArena/MemoryArena-derived evaluation`；counterevidence locator 为 `arXiv:2606.13174v1 §6 limitations and simulated-user/task-distribution scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 自动抽取可能误编译或过度约束，需 version/supersession/disable；模拟用户结果不证明真实用户长期满意度。

<!-- claim:SF-2026-ARXIV-2606-13174:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13174v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13174:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/81-workflow.md`，Review notes 前正文锚点 `State Machine 是基本模型` 已承载长期命题；source 仅作受限证据。

### [MemRefine: LLM-Guided Compression for Long-Term Agent Memory](https://arxiv.org/html/2606.13177v1)

**问题与机制。** 原筛选把《MemRefine: LLM-Guided Compression for Long-Term Agent Memory》关闭或降池；完整摘要显示“However, as interactions accumulate, the memory store grows without bound and fills with redundant entries that inflate storage cost and degrade retrieval by crowding out the most useful evidence.”。该增量直接改变 AGENT-MEMORY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Method; 3.1 Problem Formulation`；可采用的最小机制命题是：However, as interactions accumulate, the memory store grows without bound and fills with redundant entries that inflate storage cost and degrade retrieval by crowding out the most useful evidence.

**Evaluation proof。** `4 Experimental Setup; 5 Experimental Results and Analysis; Appendix F Category-wise LoCoMo Results`；exact-v1 披露：Across multiple memory frameworks and long-term conversation benchmarks, MemRefine consistently meets target budgets while preserving downstream performance and outperforming rule-based baselines under tight budgets.

**Limitations / non-proof。** `Limitations`；To this end, we then propose MemRefine, an LLM-guided framework that, since surface similarity poorly reflects factual value, uses similarity only to propose candidate pairs and defers delete, merge, and preserve decisions to an LLM judge based on factual content, iterating until the budget is met. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MEMORY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### [LLM-as-an-Investigator: Evidence-First Reasoning for Robust Interactive Problem Diagnosis](https://arxiv.org/html/2606.13220v1)

**问题与机制。** 原筛选把《LLM-as-an-Investigator: Evidence-First Reasoning for Robust Interactive Problem Diagnosis》关闭或降池；完整摘要显示“However, when users provide incomplete descriptions or plausible but unverified explanations, LLMs may prematurely align with these assumptions and propose solutions before collecting sufficient evidence.”。该增量直接改变 AGENT-PLANNING 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`4 Methodology`；可采用的最小机制命题是：However, when users provide incomplete descriptions or plausible but unverified explanations, LLMs may prematurely align with these assumptions and propose solutions before collecting sufficient evidence.

**Evaluation proof。** `3 Case study; 5 Experimental Results; 5.2 Evaluation Pipeline and Experimental Settings`；exact-v1 披露：We use a three-agent evaluation pipeline in which a Problem-Solution Extractor Agent converts solved threads into structured cases, a Ground-Truth Evaluator Agent simulates the user while hiding the known solution, and the tested assistant attempts to recover the solution through dialogue.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；The results show that the proposed approach identifies the problem more accurately than direct prompting and reasoning-only baselines, while its evidence-first protocol helps reduce user-induced conversational bias. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-PLANNING` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/79-planning.md`，Review notes 前正文锚点 `从目标到状态图` 已承载长期命题；source 仅作受限证据。

### [From Uncertain Judgments to Calibrated Rankings: Conformal Elo Estimation for LLM Evaluation](https://arxiv.org/html/2606.13221v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：LLM-judge ranking 需要先把 per-battle score difference校准为 win probability，再对 judge-human Elo residual做 split-conformal interval。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13221v1 §§3–4 probabilistic Bradley-Terry and conformal Elo`；evaluation locator 为 `arXiv:2606.13221v1 §5 LMArena held-out-model evaluation`；counterevidence locator 为 `arXiv:2606.13221v1 No dedicated limitations section — marginal-coverage/exchangeability and judge-distribution boundaries in §§3–5`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** conformal interval只给交换性条件下边际 coverage，不消除 position/self-preference/intransitivity，也不替代关键 release 的 human audit。

<!-- claim:SF-2026-ARXIV-2606-13221:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13221v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13221:end -->

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Judge Ranking 要同时校准局部比较与全局区间` 已完成写入并通过独立 post-write audit。

### 分母前关闭（保留审计轨迹）：Agentic AI Adoption and Software Architecture

独立复核结论：该 family 测量 AI coding adoption 后的软件架构结果，不改变大模型或 LLM Infra 的 state/data/control ownership、运行机制或 evaluation/release contract，以下作者侧审阅轨迹不计入 Candidate 或 Books。

**问题与机制。** 原筛选把《Mining Architectural Quality Under Agentic AI Adoption: A Causal Study of Java Repositories》关闭或降池；完整摘要显示“Yet causal evidence on their effect on software architecture is scarce.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`5.2 A Methodological Lesson for Density-Normalized Mining Outcomes`；可采用的最小机制命题是：Yet causal evidence on their effect on software architecture is scarce.

**Evaluation proof。** `4 Results`；exact-v1 披露：The complete replication package, including the curated 151-repository monthly panel, is publicly available.

**Limitations / non-proof。** `5 Discussion; 6 Threats to Validity`；The complete replication package, including the curated 151-repository monthly panel, is publicly available. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-WORKFLOW` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Pre-denominator Close — Not applicable`；保留审计轨迹但不计入 Candidate、Books 分布或 root 写入队列。

### [SkillCAT: Contrastive, Assessment-Augmented and Topology-AwareSkill Self-Evolution for LLM Agents](https://arxiv.org/html/2606.13317v1)

**问题与机制。** 原筛选把《SkillCAT: Contrastive, Assessment-Augmented and Topology-AwareSkill Self-Evolution for LLM Agents》关闭或降池；完整摘要显示“We propose SkillCAT, a framework that decomposes this process into three stages. (1) Contrastive Causal Extraction (CCE) samples multiple trajectories per task and contrasts same-task success/failure pairs to find the evidence that explains outcome differences. (2) Assessment-Augmented Evolution (AAE) replays each candidate patch on source-task clones, retains only those that do not damage task outcomes, and then merges the retained patches hierarchically. (3) Topology-Aware Task Execution (TTE) compiles the evolved skills into routable sub-skill topologies, so that inference loads only task-relevant capability nodes.”。该增量直接改变 AGENT-WORKFLOW 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`Method; Problem Formulation`；可采用的最小机制命题是：We propose SkillCAT, a framework that decomposes this process into three stages. (1) Contrastive Causal Extraction (CCE) samples multiple trajectories per task and contrasts same-task success/failure pairs to find the evidence that explains outcome differences. (2) Assessment-Augmented Evolution (AAE) replays each candidate patch on source-task clones, retains only those that do not damage task outcomes, and then merges the retained patches hierarchically. (3) Topology-Aware Task Execution (TTE) compiles the evolved skills into routable sub-skill topologies, so that inference loads only task-relevant capability nodes.

**Evaluation proof。** `Experiments; Experimental Setup; Main Results`；exact-v1 披露：We evaluate SkillCAT on widely-used agent benchmarks, including SpreadsheetBench, WikiTableQuestions, and DocVQA, and further assess cross-model and out-of-distribution generalization.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；We propose SkillCAT, a framework that decomposes this process into three stages. (1) Contrastive Causal Extraction (CCE) samples multiple trajectories per task and contrasts same-task success/failure pairs to find the evidence that explains outcome differences. (2) Assessment-Augmented Evolution (AAE) replays each candidate patch on source-task clones, retains only those that do not damage task outcomes, and then merges the retained patches hierarchically. (3) Topology-Aware Task Execution (TTE) compiles the evolved skills into routable sub-skill topologies, so that inference loads only task-relevant capability nodes. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-WORKFLOW` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/81-workflow.md`，Review notes 前正文锚点 `Trial Evidence 不能直接提交为 Workflow Revision` 已承载长期命题；source 仅作受限证据。

### [Can I Buy Your KV Cache?](https://arxiv.org/html/2606.13361v1)

**问题与机制。** 原筛选把《Can I Buy Your KV Cache?》关闭或降池；完整摘要显示“Every agent re-runs prefill, the most compute-intensive step a large model takes, over identical text, only to rebuild a key-value (KV) cache identical to the one the agent before it just built.”。该增量直接改变 INFER-PREFILL 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`4 Method`；可采用的最小机制命题是：Every agent re-runs prefill, the most compute-intensive step a large model takes, over identical text, only to rebuild a key-value (KV) cache identical to the one the agent before it just built.

**Evaluation proof。** `6 Experiments`；exact-v1 披露：We frame the resulting agent-native prefill CDN and leave lossless KV compression and a cross-party payment layer as the open problems.

**Limitations / non-proof。** `7 Discussion: a prefill CDN for the agent economy; 8 Limitations`；Every agent re-runs prefill, the most compute-intensive step a large model takes, over identical text, only to rebuild a key-value (KV) cache identical to the one the agent before it just built. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `INFER-PREFILL` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Only report`；该 exact-v1 仅支持受限案例，尚不足以改变长期 Books 机制链，不创建正文或 trace 采用链。

### [Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents](https://arxiv.org/html/2606.13385v1)

**问题与机制。** 原筛选把《Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents》关闭或降池；完整摘要显示“To capture these properties, we introduce StakeBench, a stakeholder-centric benchmark that systematically categorizes and attributes harm in real-world web agent systems for online shopping.”。该增量直接改变 PLATFORM-SECURITY 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`exact-v1 central method section`；可采用的最小机制命题是：To capture these properties, we introduce StakeBench, a stakeholder-centric benchmark that systematically categorizes and attributes harm in real-world web agent systems for online shopping.

**Evaluation proof。** `3.3 Evaluation Metrics; 4.2 Main Results; Appendix F Automated Evaluation Protocol and Annotation Guidelines`；exact-v1 披露：Evaluating four deployable agent-backbone configurations across 3,168 attacked runs, we find substantial and heterogeneous vulnerabilities: no attack objective is reliably resisted by current LLM-based web agents, and outcomes span four qualitatively distinct modes.

**Limitations / non-proof。** `B.4 Attacker Limitations; Appendix I Limitations and Future Directions`；These patterns are missed by conventional attack-centric, single-metric evaluation, underscoring the need for stakeholder-aware assessment of LLM-based agents in real-world deployments. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `PLATFORM-SECURITY` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [MiniMax Sparse Attention](https://arxiv.org/pdf/2606.13392v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：blockwise sparse attention 要把 per-GQA-group index branch、exact selected-block attention 与 GPU-efficient Top-k/KV-outer execution共同设计。

**State / data / control owner。** `MODEL-LONG-CONTEXT` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13392v1 §§3–4 MiniMax Sparse Attention architecture and kernels`；evaluation locator 为 `arXiv:2606.13392v1 §5 long-context/model evaluation`；counterevidence locator 为 `arXiv:2606.13392v1 §6 limitations and disclosed model/hardware scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** Ch22 已有 MSA 机制、GQA group selection 与受限实验边界，并含 exact family citation；不重复追加。

<!-- claim:SF-2026-ARXIV-2606-13392:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13392v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13392:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-02-model/22-long-context.md`，Review notes 前正文锚点 `方案究竟移动了哪个瓶颈` 已承载长期命题；source 仅作受限证据。

### [Accelerating Speculative Diffusions via Block Verification](https://arxiv.org/pdf/2606.13426v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：diffusion model 的 speculative block proposal 必须由 target-model block verifier统一 commit/rollback，才能把并行候选与 exact output distribution 分开。

**State / data / control owner。** `MULTIMODAL-GENERATIVE-PARADIGMS` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13426v1 §§3–4 speculative diffusion block proposal and verification`；evaluation locator 为 `arXiv:2606.13426v1 §5 image-generation evaluation`；counterevidence locator 为 `arXiv:2606.13426v1 §6 limitations and model/sampler/hardware scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 大 block 提升并行度却放大 rejection与临时 state；有限 DiT/sampler 结果不证明任意 diffusion workload 加速。

<!-- claim:SF-2026-ARXIV-2606-13426:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13426v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13426:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`，Review notes 前正文锚点 `Draft、Verify 与 Correct 不是同一件事` 已承载长期命题；source 仅作受限证据。

### [CQC-RAG: Robust Retrieval-Augmented Generation via Cross-Query Consistency](https://arxiv.org/html/2606.13438v1)

**问题与机制。** 原筛选把《CQC-RAG: Robust Retrieval-Augmented Generation via Cross-Query Consistency》关闭或降池；完整摘要显示“To address these limitations, we propose a Cross-Query Consistency Hypothesis: correct answers tend to maintain high confidence across semantically equivalent but syntactically diverse queries, whereas noise-induced hallucinations exhibit unstable confidence under such query variations.”。该增量直接改变 AGENT-RAG 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3. Methodology`；可采用的最小机制命题是：To address these limitations, we propose a Cross-Query Consistency Hypothesis: correct answers tend to maintain high confidence across semantically equivalent but syntactically diverse queries, whereas noise-induced hallucinations exhibit unstable confidence under such query variations.

**Evaluation proof。** `2.2. Discriminative Answer Evaluation; 4. Experiments; 4.1. Datasets and Evaluation Metrics`；exact-v1 披露：Semantically equivalent queries with different syntactic forms may lead to different retrieval results, while irrelevant or misleading documents can further induce hallucinated answers.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Existing multi-path reasoning methods improve robustness by sampling multiple candidate answers and applying voting- or confidence-based selection, but they still face two limitations: diversity is often injected through uncontrollable decoding randomness, and answer evaluation is usually confined to a single query-induced evidence view. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-RAG` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/76-rag.md`，Review notes 前正文锚点 `Online Retrieval Pipeline` 已承载长期命题；source 仅作受限证据。

### [Toward Instructions-as-Code: Understanding the Impact of Instruction Files on Agentic Pull Requests](https://arxiv.org/pdf/2606.13449v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：repository instruction 文件是可执行 control surface；评价必须区分规则存在、被读取、进入 context、被遵守与最终 outcome。

**State / data / control owner。** `AGENT-PROMPT` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13449v1 §§3–4 instructions-as-code taxonomy and instrumentation`；evaluation locator 为 `arXiv:2606.13449v1 §5 repository/coding-agent experiments`；counterevidence locator 为 `arXiv:2606.13449v1 §6 limitations and harness/model/repository scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 更强 instruction 提高一致性也会固化陈旧约束、扩大 context与冲突；观察到 compliance 不证明 effect correctness。

<!-- claim:SF-2026-ARXIV-2606-13449:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13449v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13449:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/74-prompt.md`，Review notes 前正文锚点 `Prompt 生命周期` 已承载长期命题；source 仅作受限证据。

### [Budget-Constrained Step-Level Diffusion Caching](https://arxiv.org/pdf/2606.13496v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：diffusion serving cache 应把 denoising step、state identity 与误差预算绑定，在 step-level reuse 与 recompute 间动态选择。

**State / data / control owner。** `MULTIMODAL-GENERATIVE-PARADIGMS` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13496v1 §§3–4 step-level diffusion caching mechanism`；evaluation locator 为 `arXiv:2606.13496v1 §5 quality/latency evaluation`；counterevidence locator 为 `arXiv:2606.13496v1 §6 limitations and model/workload calibration scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** cache hit以漂移和额外 metadata换算力；阈值绑定模型、prompt与scheduler，分布漂移时必须回退完整 denoising。

<!-- claim:SF-2026-ARXIV-2606-13496:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13496v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13496:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`，Review notes 前正文锚点 `Draft、Verify 与 Correct 不是同一件事` 已承载长期命题；source 仅作受限证据。

### [GF-DiT: Scheduling Parallelism for Diffusion Transformer Serving](https://arxiv.org/pdf/2606.13501v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：Diffusion Transformer serving 应联合管理 request phase、denoising-step work、cache locality 与 batch admission，而非套用自回归 token scheduler。

**State / data / control owner。** `INFER-SCHEDULING` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13501v1 §§3–4 GF-DiT serving design and scheduler`；evaluation locator 为 `arXiv:2606.13501v1 §5 prototype evaluation`；counterevidence locator 为 `arXiv:2606.13501v1 §6 limitations and disclosed DiT/hardware workload`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** phase-aware batching降低空洞但增加 prediction/state migration；作者 workload 的吞吐/延迟不构成生产 SLO。

<!-- claim:SF-2026-ARXIV-2606-13501:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13501v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13501:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-05-inference-system/56-inference-scheduling.md`，Review notes 前正文锚点 `迭代生成与流式会话需要显式 Progress State` 已承载长期命题；source 仅作受限证据。

### [Multiagent Protocols with Aggregated Confidence Signals](https://arxiv.org/html/2606.13591v1)

**问题与机制。** 原筛选把《Multiagent Protocols with Aggregated Confidence Signals》关闭或降池；完整摘要显示“We introduce three protocols that produce a final answer along with a single aggregated confidence by first transforming raw confidence signals to make them comparable across models, then combining them via soft voting or a probability fusion we call Bayesian fusion.”。该增量直接改变 AGENT-MULTI-AGENT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methods; 3.3 Confidence Calibration Methods`；可采用的最小机制命题是：We introduce three protocols that produce a final answer along with a single aggregated confidence by first transforming raw confidence signals to make them comparable across models, then combining them via soft voting or a probability fusion we call Bayesian fusion.

**Evaluation proof。** `4 Experimental Setup; 4.1 Evaluation; 5 Results`；exact-v1 披露：Analyzing two estimators, sequence probability and self-report, alongside parametric and non-parametric calibrators, we find that calibration improves F1 for both estimators while AUARC is less reliant on it.

**Limitations / non-proof。** `7 Limitations`；We evaluate six homogeneous and heterogeneous debating pairs per benchmark, across five benchmarks and four task types, spanning a range of model capabilities and sizes. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MULTI-AGENT` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/82-multi-agent.md`，Review notes 前正文锚点 `Message 不是 State` 已承载长期命题；source 仅作受限证据。

### [See What I See, Know What I Think: Dense Latent Communication Across Heterogeneous Agents](https://arxiv.org/html/2606.13594v1)

**问题与机制。** 原筛选把《See What I See, Know What I Think: Dense Latent Communication Across Heterogeneous Agents》关闭或降池；完整摘要显示“Motivated by this, we propose dense alignment for heterogeneous KV-cache communication via a lightweight cross-model cache transformation and two-phase training: reconstruction followed by generation.”。该增量直接改变 AGENT-MULTI-AGENT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`4.2 Architecture Design: Heterogeneous Dense Cache Alignment`；可采用的最小机制命题是：Motivated by this, we propose dense alignment for heterogeneous KV-cache communication via a lightweight cross-model cache transformation and two-phase training: reconstruction followed by generation.

**Evaluation proof。** `5 Experiments; 5.1 Context-aware Results; 5.2 Context-unaware Results`；exact-v1 披露：Across all six directions of {Qwen3-4B, 8B, 14B} and six in-domain and out-of-domain benchmarks, our method outperforms prior heterogeneous baselines, matches or exceeds text communication in context-aware settings at roughly 2 to 3 times lower compute, and remains effective in context-unaware transfer where prior methods collapse.

**Limitations / non-proof。** `未定位独立 limitations；边界由 exact-v1 披露 workload 推得`；Across all six directions of {Qwen3-4B, 8B, 14B} and six in-domain and out-of-domain benchmarks, our method outperforms prior heterogeneous baselines, matches or exceeds text communication in context-aware settings at roughly 2 to 3 times lower compute, and remains effective in context-unaware transfer where prior methods collapse. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MULTI-AGENT` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `Integrate` → `books/part-07-agent/82-multi-agent.md`，Review notes 前正文锚点 `Latent Communication 只能压缩 Payload，不能隐藏 Identity` 已完成写入并通过独立 post-write audit。

### [Reward Modeling for Multi-Agent Orchestration](https://arxiv.org/html/2606.13598v1)

**问题与机制。** 原筛选把《Reward Modeling for Multi-Agent Orchestration》关闭或降池；完整摘要显示“We propose Orchestration Reward Modeling (OrchRM), a self-supervised framework for evaluating orchestration quality without human annotations.”。该增量直接改变 AGENT-MULTI-AGENT 下的机制/证据边界，因此恢复 Candidate；不以标题关键词或章节映射准入。 Method：`3 Methodology`；可采用的最小机制命题是：We propose Orchestration Reward Modeling (OrchRM), a self-supervised framework for evaluating orchestration quality without human annotations.

**Evaluation proof。** `4 Experiments; 4.1 Experimental Setup`；exact-v1 披露：Code will be available at https://github.com/Wang-ML-Lab/OrchRM.

**Limitations / non-proof。** `Appendix A Limitations and Broader Impact`；Multi-Agent Systems (MAS) built on Large Language Models (LLMs) require effective orchestration to coordinate specialized agents, yet training such orchestrators is hindered by limited supervision and high computational cost. 只支持 exact-v1 披露的模型、数据、硬件、预算与 evaluator；未披露字段不外推为生产 SLO 或通用保证。

**Owner 与演进。** `AGENT-MULTI-AGENT` 持有 state/data/control 与最终 commit；旧路径在论文前提不成立、校准漂移、artifact/identity 不兼容或收益未覆盖控制成本时继续共存。

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/82-multi-agent.md`。其 self-supervised intermediate-artifact reward model 是既有 dynamic topology、typed credit、critical-path reward 与 role obligation 的局部训练配方，不形成新的长期机制链。

### [AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and Reproducibility](https://arxiv.org/pdf/2606.13608v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：Agent benchmark 应把 task/environment/evaluator protocol做成可部署 assessment contract，并保存run identity、submission与verdict lineage。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13608v1 §§3–4 AgentBeats protocol and platform`；evaluation locator 为 `arXiv:2606.13608v1 §5 benchmark deployment/case-study evaluation`；counterevidence locator 为 `arXiv:2606.13608v1 §6 limitations and supported environment/protocol scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 平台统一降低接线成本却扩大 evaluator/control-plane TCB；可运行 benchmark 不证明 judge、任务或环境代表真实生产。

<!-- claim:SF-2026-ARXIV-2606-13608:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13608v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13608:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Evaluation Identity 必须包含 Harness 与 Environment` 已承载长期命题；source 仅作受限证据。

### [One Polluted Page Is Enough: Evaluating Web Content Pollution in LLM Recommenders](https://arxiv.org/pdf/2606.13610v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：web-connected Agent 的安全评测必须冻结污染时间线与 attacker publishing budget，测量 retriever/index/reader 怎样把公开内容变成控制输入。

**State / data / control owner。** `PLATFORM-SECURITY` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13610v1 §§3–4 content-pollution threat model and benchmark`；evaluation locator 为 `arXiv:2606.13610v1 §5 retrieval/agent attack evaluation`；counterevidence locator 为 `arXiv:2606.13610v1 §6 limitations and web-corpus/model cutoff scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 污染 benchmark会随搜索索引与网页变化而漂移；有限页面与模型不能给真实攻击发生率，source trust/authorization仍需独立控制。

<!-- claim:SF-2026-ARXIV-2606-13610:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13610v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13610:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-06-ai-infrastructure/72-security.md`，Review notes 前正文锚点 `从资产与信任边界开始` 已承载长期命题；source 仅作受限证据。

### [Valid Inference with Synthetic Data via Task Exchangeability](https://arxiv.org/html/2606.13629v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：synthetic-data inference 必须把 generator、selection/filter与downstream sample视为同一随机过程，并检验 task-level exchangeability 后才报告置信区间。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13629v1 §§2–4 task-exchangeability framework and estimators`；evaluation locator 为 `arXiv:2606.13629v1 §5 synthetic-data experiments`；counterevidence locator 为 `arXiv:2606.13629v1 §6 limitations and exchangeability/model-generator assumptions`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 有效区间依赖 exchangeability/independence 近似；generator drift、adaptive filtering与leakage会破坏 coverage，点估计不能替代。

<!-- claim:SF-2026-ARXIV-2606-13629:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13629v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13629:end -->

**V3 Books Decision。** `Integrate` → `books/part-06-ai-infrastructure/66-evaluation-system.md`，Review notes 前正文锚点 `Synthetic Evidence 只有在 Task Exchangeability 成立时才能进入推断` 已完成写入并通过独立 post-write audit。

### [Recursive Agent Harnesses](https://arxiv.org/pdf/2606.13643v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：recursive harness improvement 必须把 harness revision当受控 artifact，以相邻 revision、fixed evaluator与rollback做局部搜索。

**State / data / control owner。** `AGENT-WORKFLOW` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13643v1 §§3–4 recursive harness search and revision protocol`；evaluation locator 为 `arXiv:2606.13643v1 §5 controlled task evaluation`；counterevidence locator 为 `arXiv:2606.13643v1 §6 limitations and evaluator/harness-search scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** Ch81 已有 recursive harness self-improvement、durable workflow与terminal verifier；不复制论文特定 search recipe。

<!-- claim:SF-2026-ARXIV-2606-13643:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13643v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13643:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/81-workflow.md`，Review notes 前正文锚点 `State Machine 是基本模型` 已承载长期命题；source 仅作受限证据。

### 分母前关闭（保留审计轨迹）：Autonomous Scientific Discovery Environment Engineering

独立复核结论：该 family 的对象是 autonomous scientific discovery；AI for Science 当前明确暂缓，且其 proposal-validation-promotion 结构已是通用 workflow 合同，以下作者侧审阅轨迹不计入 Candidate 或 Books。

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：Agent 自改进需要把 candidate skill/workflow artifact、evaluator result与promotion gate分离，失败 proposal不得直接覆盖运行时。

**State / data / control owner。** `AGENT-WORKFLOW` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13662v1 §§3–4 EurekAgent self-improvement loop`；evaluation locator 为 `arXiv:2606.13662v1 §5 benchmark evaluation`；counterevidence locator 为 `arXiv:2606.13662v1 §6 limitations and task/evaluator scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** Ch81/80 已有 proposal→validation→promotion与self-improvement边界；论文结果保留 Daily evidence，不形成第二 owner。

<!-- claim:SF-2026-ARXIV-2606-13662:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13662v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13662:end -->

**V3 Books Decision。** `Pre-denominator Close — Not applicable`；保留审计轨迹但不计入 Candidate、Books 分布或 root 写入队列。

### [HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents](https://arxiv.org/pdf/2606.13663v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：tool granularity 是 interface design变量：平台应在细粒度 primitive与复合 tool之间联合评估planning burden、权限面、失败定位与复用。

**State / data / control owner。** `AGENT-TOOL-CALLING` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13663v1 §§3–4 HyperTool decomposition/composition method`；evaluation locator 为 `arXiv:2606.13663v1 §5 tool-use experiments`；counterevidence locator 为 `arXiv:2606.13663v1 §6 limitations and benchmark/tool-library scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 粗粒度减少 calls 却扩大authority/隐藏 side effects；细粒度可审计但增加 planning 与 latency，不存在通用最优粒度。

<!-- claim:SF-2026-ARXIV-2606-13663:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13663v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13663:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/78-tool-calling.md`，Review notes 前正文锚点 `Tool Contract` 已承载长期命题；source 仅作受限证据。

### [EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments](https://arxiv.org/pdf/2606.13681v1)

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：evolving environment 的 memory 不应只保存最新摘要，而应保存 patch/update history，让状态变化、evidence capture 与 chain-level recovery可评测。

**State / data / control owner。** `AGENT-MEMORY` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.13681v1 §§3–4 EvoArena and patch-based EvoMem`；evaluation locator 为 `arXiv:2606.13681v1 §5 terminal/software/social-preference evaluations`；counterevidence locator 为 `arXiv:2606.13681v1 §6 limitations and domain/model/task-chain scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** patch history提高可追踪性却增加 context/compaction冲突；小幅平均收益不证明所有长期任务优于快照/事件日志。

<!-- claim:SF-2026-ARXIV-2606-13681:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.13681v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-13681:end -->

**V3 Books Decision。** `No Change — Existing Coverage` → `books/part-07-agent/77-memory.md`，Review notes 前正文锚点 `Consolidation 与 Forgetting` 已承载长期命题；source 仅作受限证据。

### Books / semantic audit

`Integrate=9`，`No Change — Existing Coverage=53`，`Only report=1`，另有 3 项经独立准入复核改为分母前关闭。作者侧 proposal 与独立 Gate 的最终覆盖清单见 [`v3-independent-candidate-books-gate-20260911.json`](../_sources/daily-20260612/v3-independent-candidate-books-gate-20260911.json)；独立写后结果见 [`v3-independent-post-write-audit-20260911.json`](../_sources/daily-20260612/v3-independent-post-write-audit-20260911.json)。`books_removal_queue=0`，13 条 trace 日期修正均已完成并复验，remaining queue=`0`。

## 5. 缺口与下一步

终态保留项：official historical arXiv listing/announcement receipt 尚未取得；定点重开条件：未来取得可改变公开日期 owner 的官方 listing evidence；该缺口不用于正面证据、Books 或无遗漏断言。

1. 9 条 Books body writeback 与 13 条 trace 日期修正均已完成；正文 marker、章节位置、长期机制链和报告映射已由非写作者独立复验，执行队列为 0。
2. official historical arXiv listing/announcement receipt 仍是保留的来源边界；在其到位前不执行跨日迁移，也不把该外部证明缺口伪装成当前日期的执行 pending。
3. 若未来取得相反的 official listing evidence，只重开受影响的日期 owner reconciliation，不推翻本次冻结的 Candidate denominator。

### Repository Changes

- 更新 2026-06-12 Daily 与 `_sources/daily-20260612` 下的 V3 Gate、proposal、reconciliation 和独立写后审计 artifact。
- 复验并最小重排 `27-data.md`、`56-inference-scheduling.md`、`66-evaluation-system.md`、`72-security.md`；`82-multi-agent.md` 的现有落点无需重排。
- 未修改 Candidate denominator、`docs/LEARNING_STATE.md`、其他日期或月级 audit。

## 6. 复核

当前来源再认证复核者：\`june_11_20_recert\`（独立于原报告作者）。当前合同来源再认证补齐十三个官方 Daily 源；未发现需恢复的独立候选，原 Candidate/Evidence/Books 结论保持不变。

复核者：Candidate/Books Gate `/root/june_11_12_independent_gate`；独立 post-write audit `/root/june_11_12_postwrite`
结论：通过

- 3 项误收已关闭；9 条 Books 正文与 13 条 trace correction 已逐条复验。独立审计发现并修复了案例先于通用基线的章节顺序问题，并将 synthetic-data inference 的 owner 校正为 `PLATFORM-EVALUATION-SYSTEM`；未改变 Candidate denominator 或长期结论。
- 机器校验：`validate_research.py`、`check_report_v3.validate`、JSON/算术/URL 与身份去重、marker 唯一性、Review notes 边界和 `git diff --check` 均通过。机器结果不替代上述语义复核。
