# R54三具名发现差额：首次题摘/notice/联合日期与拟贡献（2026-10-25）

范围仅2606.03458/02963/03344；R54具体抽样差额，不扩NAV/Methods。此前25家族24I/E1与机构有限stop有效，不第三。下列均为作者拟准入，未独核/未正式评分/未新增正式候选；完整exact-v1题摘已实际读，尚未读必要全文或比较actual Books。原公告/发号规则依本日先前有效组合标准复用，不重开旧65。

## 2606.03458v1 KVarN

原页：https://arxiv.org/abs/2606.03458v1；完整原HTML `SUP_ABS_2606.03458v1_R54_20261025.html`。当前notice轻核原HTML `SUP_ABS_2606.03458_CURRENT_R54_20261025.html`，两次请求均exit0。

Title: KVarN: Variance-Normalized KV-Cache Quantization Mitigates Error Accumulation in Reasoning Tasks

Abstract: Test-time scaling is a powerful approach to obtain better reasoning in large language models, but it becomes memory-bottlenecked during long-horizon decoding, as the KV-cache grows. KV-cache quantization can help improve this, but current methods are evaluated under prefill-like settings and errors behave differently under autoregressive decoding. We show that in the latter regime, quantization errors accumulate across timesteps, driven primarily by incorrect token scales. We introduce KVarN, a calibration-free KV-cache quantizer that applies a Hadamard rotation followed by a dual-scaling variance normalization across both axes of the K and V matrices. We find that this combination fixes outlying token-scale errors and substantially reduces error accumulation over existing baselines. KVarN establishes a new state-of-theart for KV-cache quantization on generative benchmarks, including MATH500, AIME24 and HumanEval, at 2-bit precision. A vLLM implementation of the KVarN method is available at this https URL

Submission history From: Philippe Bich [ view email ] [v1] Tue, 2 Jun 2026 10:34:56 UTC (372 KB)

日证：同精确DOI `10.48550/arxiv.2606.03458` 原NAV `SUP_NAV_TITLE_SYS_P2_20261024.json`，client=`arxiv.content`、state=`findable`，v1 Submitted=2026-06-02T10:34:56Z，registered=2026-06-03T02:52:53Z。提交均处Mon14–Tue14 EDT段，最早Tue20 EDT公告=Jun03 08BJT；上界Jun03 10:52:53BJT。整个可能公告区间Jun03 08:00至10:52:53均同Jun03，非registered作为实际公开clock，不证明全球更早渠道或历史逐字。

轻notice：v1/current均只v1，无comments；未见withdrawn/erratum/correction/admin条。摘要里的incorrect token scales是研究失效对象，不是勘误notice。

拟贡献：原有prefill式KV量化评价不能代表真实自回归长推理误差累积 → 原文将token-scale错误作为直接失效对象，Hadamard之后对K/V双轴variance normalization → 需要核验静态量化误差小是否足以支持decode质量、以及dual scaling相较单rotation/单scale的增量。具体失效机制与修正潜在明确，拟P；不是因2bit/SOTA或有vLLM代码准入。

采用/必要边界：后续必要仅AR-vs-prefill误差链、双轴归一与可比旋转/量化对照及长生成反侧/总费用；摘要不能证明token-scale唯一因果、所有长度/模型无损、实机净吞吐或代码已核。

## 2606.02963v1 KForge

原页：https://arxiv.org/abs/2606.02963v1；完整原HTML `SUP_ABS_2606.02963v1_R54_20261025.html`。当前notice轻核原HTML `SUP_ABS_2606.02963_CURRENT_R54_20261025.html`，两次请求均exit0。

Title: KForge: LLM-Driven Cross-Platform Kernel Generation for AI Accelerators

Abstract: Production inference increasingly targets a heterogeneous mix of accelerators. Agentic pipelines interleave reasoning, tool calls, and multi-agent coordination, each with distinct compute and memory profiles. For optimal efficiency, each stage should run on the accelerator best suited to it. This creates a systems challenge: each pipeline now requires high-performance kernels across a growing set of hardware backends and programming models. Writing these kernels by hand is time-consuming, demands deep low-level expertise, and does not scale as kernel complexity grows. Recently, Large Language Models (LLMs) have been leveraged for automatic kernel generation, but challenges in low-level code generation and cross-backend generalization persist. We present KForge, a cross-platform framework built around an iterative refinement loop driven by two collaborating LLM-based agents: a generation agent that produces and progressively refines kernels using compilation and correctness feedback, and a performance-analysis agent that interprets profiling data, from programmatic APIs to GUI-based tools, and emits recommendations that steer the next round of synthesis. The loop alternates between functional passes, which drive a candidate to correctness, and optimization passes, which close the performance gap to hand-tuned baselines. We evaluate KForge on two backends with very different baseline reference availability. On NVIDIA B200, KForge achieves a 2.12$\%$ improvement in end-to-end throughput compared to TensorRT-LLM on the gpt-oss-20b inference speed benchmark. On Intel Arc B580, KForge generates Triton kernels achieving a 5.13$\times$ geometric mean speedup over the faster of PyTorch eager and this http URL on 37 GEMM + tail-ops workloads from KernelBench Level 2, primarily via operator fusion and mixed-precision execution.

Submission history From: Taras Sereda [ view email ] [v1] Mon, 1 Jun 2026 23:48:55 UTC (368 KB)

日证：同精确DOI `10.48550/arxiv.2606.02963` 原NAV `SUP_NAV_AGENT_P4_20261024.json（TITLE_SYS P3重复同identity）`，client=`arxiv.content`、state=`findable`，v1 Submitted=2026-06-01T23:48:55Z，registered=2026-06-03T02:10:29Z。提交均处Mon14–Tue14 EDT段，最早Tue20 EDT公告=Jun03 08BJT；上界Jun03 10:10:29BJT。整个可能公告区间Jun03 08:00至10:10:29均同Jun03，非registered作为实际公开clock，不证明全球更早渠道或历史逐字。

轻notice：v1/current均只v1，comments为Accepted at ISCA2026 Workshop MLArchSys；未见withdrawn/erratum/correction/admin条。

拟贡献：异构后端手写kernel不伸缩、单次LLM代码生成不保正确与性能 → 原文分开compilation/correctness驱动functional passes和原生profile（API/GUI）驱动optimization passes，由性能分析agent给生成agent可执行下一轮建议 → 需要核验跨后端时功能门与性能反馈接口如何分责及其实际增量。拟P限该反馈分流/跨后端条件；不是因为两个agent组合或2.12%/5.13倍本身。若必要证据只重复通用迭代且无新增条件，应据实际证据改判，不因投入费时排除。

采用/必要边界：必要只functional/optimization转移、profile消费/正确性资格、两个后端不同参考可用性与mixedprecision/fusion替代解释、对照/预算/关键失败；B200 e2e与B580 operator geomean不可相加/直接比较，不授相同质量预算、LLM自治可靠或双agent不可替代。

## 2606.03344v1 RogueMerge

原页：https://arxiv.org/abs/2606.03344v1；完整原HTML `SUP_ABS_2606.03344v1_R54_20261025.html`。当前notice轻核原HTML `SUP_ABS_2606.03344_CURRENT_R54_20261025.html`，两次请求均exit0。

Title: RogueMerge: Robust and Unified Attacks against LLM Model Merging

Abstract: Model merging composes specialized capabilities into a single LLM by aggregating task vectors sourced from unverified public platforms, exposing a critical supply-chain attack surface: Because any malicious behavior can be encoded into a task vector, and merging grants third-party vectors direct write access to model weights, an attacker-provided task vector can enable or amplify diverse downstream threats. Prior work studies only backdoor attacks against model merging for classifiers using static arithmetic heuristics, which fail to effectively handle diverse attacks on generative LLMs for three reasons. (i) LLMs rely on autoregressive decoding, where the minor parameter drift introduced by merging compounds across tokens and rapidly degrades the attack. (ii) Attackers have no knowledge of the victim's merging configurations, causing a static attack vector optimized in isolation to be easily diluted or destroyed. (iii) Practical threat induction must generalize to attack prompts unseen during optimization, which static vectors cannot adequately encode. We present RogueMerge, the first principled, unified framework that addresses all three challenges. To handle autoregressive generation, we replace static arithmetic with a joint optimization that explicitly enforces attack success after merging. To handle unknown merging settings, we formulate attack injection as a stochastic min-max problem and solve it via meta-learning-style simulation. To generalize across heterogeneous attack prompts, we employ distributionally robust optimization and derive a tractable first-order Taylor approximation at LLM scale, with a provable error bound. Across four threats, six merging algorithms, and over 170 merged LLMs, RogueMerge consistently outperforms existing attacks. It also remains stable across diverse merging settings and resists standard defenses.

Submission history From: Jinghuai Zhang [ view email ] [v1] Tue, 2 Jun 2026 08:54:37 UTC (3,343 KB)

日证：同精确DOI `10.48550/arxiv.2606.03344` 原NAV `SUP_NAV_TITLE_MODEL_P1_20261024.json（含v2漂移，只作日期身份）`，client=`arxiv.content`、state=`findable`，v1 Submitted=2026-06-02T08:54:37Z，registered=2026-06-03T02:48:54Z。提交均处Mon14–Tue14 EDT段，最早Tue20 EDT公告=Jun03 08BJT；上界Jun03 10:48:54BJT。整个可能公告区间Jun03 08:00至10:48:54均同Jun03，非registered作为实际公开clock，不证明全球更早渠道或历史逐字。

轻notice：当前v2 submitted Oct12，comments为To appear in IEEE S&P2027；v1无comments。v1/current未见withdrawn/erratum/correction/admin撤回条；摘要差别已可见但不能据版本号推重要修订，本文只v1。

拟贡献：merge将未验证task-vector写入model weights，孤立静态攻击可能在AR解码/未知merge配置下被稀释 → 原文在合并后目标上联合优化，并以stochastic minmax模拟未知配置、DRO覆盖prompt异质性 → 需要重审权重合并不是中性组合、单vector/单配置审计能否覆盖最终合并后行为。具体安全与优化机制拟P，不能因为已知backdoor主题或已有security owner关闭。

采用/必要边界：只采用v1；必要核威胁模型、实际joint/minmax/DRO目标与一阶近似假设/反侧，以及merge配置/任务/预算评价。摘要provable bound未核不采用；170模型/四威胁不授普遍鲁棒或标准防线无效。v2标题相同但措辞meta-gradient等已漂移，不混后稿。

## 交接

三项首次完整AB/notice/联合日期及具体拟贡献现在ready，立即交同日独立reader首次校准；不等Methods，也未将三条全定为必要Source队列或正式打分。R54机构新原件/普通排除5样本有效复用；本三准入后再逐篇最小必要层。旧LibraR30/DriftR32真实POST尾语已行政修正，无历史标识21阶段段已明确R42历史，不改技术正文。报告仍进行中/日级未通过，不宣称普通未办0。

