# AI Research Weekly — 2025-W30

> Coverage Window: 2025-07-21～2025-07-27
> Research Mode: Retrospective Backfill
> Initial Archive Accessed: 2026-07-31
> Discovery Replay and Primary-source Re-audit: 2026-08-24
> Audit Status: Candidate Evidence Gate Conditional Pass — 54/54 Scored Owners, 39/39 Retained Full Source Review, 15/15 Low-score or Blocked Closure, 1 Exact External Material Blocker
> Historical Books Gate: Closed

## Executive Summary

W30 的旧档案只有 Qwen3-Coder、SpecForge 和一项异构 Agent system 论文，不能代表当周研究面。按固定机构、arXiv/学术索引与 AI Infra 顺序重放，并接收 W32 routing 发现的三个 owner spillback 后，本周闭合 **54 个 scored owner**：29 个 25～30 分、10 个 20～24 分、14 个普通低分，以及 1 个因全文无法取得而降级为 19 分的精确 Blocked 项。39 个 20+ 候选均已回到 primary source 阅读 Method、实现、实验、消融或附录与 limitations；15 个低分/阻塞候选均完成身份、v1 日期、分数与拒绝理由闭合。由于 Zebra-CoT v1 全文仍缺，本周 Candidate Evidence Gate 只能 `Conditional Pass`：允许 forward cursor 继续，但不能宣称材料无缺口或 Archive Completion。

长期信号集中在三个系统契约：RL objective 必须与实际采样粒度和 MoE routing state 对齐；Agent/Deep Search evaluation 必须同时测最终答案、检索过程和 attribution；多模态生成正从静态媒体进入可交互、可控制、带持久状态的 world simulation。上述仍是 Weekly evidence，不触发 Historical Books Integration。

## Coverage Window and Limitations

- owner 由官方首次公开日、GitHub release/tag 或 arXiv v1 日期决定；revision 留在同一 Source Family，不重复计分。
- Hugging Face Daily Papers、Scholar、OpenAlex、DBLP、Semantic Scholar 只用于 discovery 与去重；机制结论回到 arXiv 正文、官方报告、代码或 release。
- 历史回填不补造 Daily；Event-date Daily Decision 固定为 Weekly owner。
- 作者 benchmark 只在其模型、数据、硬件、精度、长度、batch、concurrency、SLO 与 evaluator contract 下成立；未披露字段写 `Not Disclosed`。
- Zebra-CoT 的身份与 v1 日期可核验，但本轮 arXiv HTML/PDF 均无法取得，不能保持 20+；已降级并给出精确材料请求。

## Source Coverage

### 1. 模型与研究机构

按 OpenAI、Anthropic、Google/DeepMind、Meta、Microsoft、NVIDIA、Amazon、Apple、Qwen、DeepSeek、Moonshot、ByteDance、Tencent、Baidu、Alibaba、Shanghai AI Laboratory 等固定顺序核验。保留 Qwen3-Coder；TeleChat2/2.5/T1 以 technical report 归档。没有把价格、API alias 或仅有宣传口径的变化计为机制事件。

### 2. 论文与学术来源

按 arXiv 当周 v1、交叉索引与 Source Family 回链重放，覆盖 training objective、multimodal representation/generation、embodied/world model、evaluation、Agent search、formal verification、online MoE 与 heterogeneous Agent systems。所有 20+ owner 均完成非模板化 Full Source Review。

### 3. AI Infra 与工程项目

按 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Hugging Face、DeepSpeed、Megatron-LM、llama.cpp、ONNX Runtime、OpenXLA 顺序核验。保留 SpecForge；Ray Q3 roadmap 仅是 design intent。PyTorch 2.8 等 7 月 30 日事件归 W31。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Qwen3-Coder | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Weekly Only — Mechanism Partially Disclosed |
| GUI-G² | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Emerging / Experimental |
| GR-3 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Emerging / Experimental |
| Being-H0 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Emerging / Experimental |
| STITCH | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Emerging / Experimental |
| Dual-Token Constraints / Archer | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Emerging / Experimental |
| Latent Denoising Tokenizer | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Emerging / Experimental |
| TokensGen | 3 | 4 | 4 | 5 | 5 | 3 | 24/30 | Emerging / Experimental |
| LLM Economist | 3 | 3 | 3 | 5 | 4 | 3 | 21/30 | Emerging / Experimental |
| PhysGym | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Emerging / Experimental |
| SPAR | 3 | 4 | 4 | 5 | 3 | 3 | 22/30 | Emerging / Experimental |
| Does More Inference-Time Compute Really Help Robustness? | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Emerging / Experimental |
| LAPO | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Emerging / Experimental |
| Hierarchical Budget Policy Optimization | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Emerging / Experimental |
| True Multimodal In-Context Learning | 3 | 4 | 4 | 5 | 5 | 3 | 24/30 | Emerging / Experimental |
| Beyond Context Limits / TIMRUN | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Emerging / Experimental |
| Step-Audio 2 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Emerging / Experimental |
| MegaScience | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Emerging / Experimental |
| ThinkAct | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Emerging / Experimental |
| Semi-off-Policy RL / SOPHIA | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Emerging / Experimental |
| Experience is the Best Teacher | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Emerging / Experimental |
| Yume | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Emerging / Experimental |
| Turing Eye Test | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Emerging / Experimental |
| Multi-Domain Reasoning via RL | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Emerging / Experimental |
| RAVine | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Emerging / Experimental |
| Re:Form | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Emerging / Experimental |
| PUSA V1.0 | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Emerging / Experimental |
| Finding Dori | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Emerging / Experimental |
| Group Sequence Policy Optimization | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Emerging / Experimental |
| GLiNER2 | 3 | 4 | 4 | 5 | 4 | 3 | 23/30 | Emerging / Experimental |
| TTS-VAR | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Emerging / Experimental |
| DriftMoE | 3 | 4 | 4 | 5 | 4 | 3 | 23/30 | Emerging / Experimental |
| TeleChat2 / 2.5 / T1 Technical Report | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Weekly Only — Model/Training Report |
| TeEFusion | 3 | 4 | 4 | 5 | 5 | 3 | 24/30 | Emerging / Experimental |
| SpecForge | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Refine — Existing Argument after Books Gate |
| Efficient Agents | 4 | 5 | 5 | 4 | 4 | 4 | 26/30 | Emerging / Experimental — Internal Manuscript Date Conflict Not Used for Owner |
| InstructVLA | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Emerging / Experimental |
| Dens3R | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Emerging / Experimental |
| Efficient and Scalable Agentic AI with Heterogeneous Systems | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Emerging / Experimental |
| SeC | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Narrow evidence |
| Spelke Segments | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Narrow evidence |
| SegDT | 3 | 3 | 3 | 5 | 2 | 2 | 18/30 | Archive Only — Narrow evidence |
| HOComp | 3 | 3 | 3 | 5 | 2 | 2 | 18/30 | Archive Only — Narrow evidence |
| Task-specific Zero-shot QAT | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Narrow evidence |
| CAFT | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Narrow evidence |
| DesignLab | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Domain-specific benchmark |
| Ultra3D | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Narrow evidence |
| Captain Cinema | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Narrow evidence |
| EarthCrafter | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Narrow evidence |
| Agentar-Fin-R1 | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Domain-specific model |
| A New Pair of GloVes | 3 | 3 | 3 | 5 | 2 | 2 | 18/30 | Archive Only — Local model mechanism |
| HLFormer | 3 | 3 | 3 | 5 | 2 | 2 | 18/30 | Archive Only — Narrow architecture |
| Ray Q3 2025 Roadmap | 2 | 3 | 3 | 4 | 2 | 2 | 16/30 | Weekly Only — Design Intent, Not Release |
| Zebra-CoT | 3 | 3 | 3 | 4 | 4 | 2 | 19/30 | Unverified / Blocked — Full Text |

计数复核：54 rows = 29 high（25～30）+ 10 medium（20～24）+ 15 low/blocked（<20）；39 retained rows 均完成 Full Source Review。

## Deep Analysis

### 1. GSPO：从 token-level surrogate 到 sequence-level sampling contract

GRPO 的 token-level importance ratio 在自回归序列上并不等于真实 sequence sampling ratio；响应变长、policy drift 或 MoE routing 重放不一致时，高方差会被 clipping 放大。GSPO 改用序列 likelihood 的几何平均定义 importance ratio，并在 sequence level 完成 clipping、reward 与 optimization，使优化粒度与 group reward 对齐。论文在 Qwen3-30B-A3B、AIME、LiveCodeBench/CodeForces 等作者设置中报告更稳定训练，并说明无需 Routing Replay；它没有证明所有模型、reward 或 off-policy gap 下都优于 PPO/GRPO，也没有公开完整 fleet cost。长期价值是：RL objective、采样单元、routing state 与 infrastructure replay contract 必须共同设计。

### 2. TIMRUN：context 超限不是“扩窗”，而是状态外置与预算控制

长任务把上下文窗口从容量问题变成状态管理问题。TIMRUN 让模型在窗口将满时生成可恢复摘要，并在新窗口继续任务，相当于把 token history 压缩为模型可读 checkpoint。它扩展任务时长，却会丢失 provenance、精确细节和隐含约束，错误还可能跨窗口累积。它与 KV cache 扩容不是同一层：前者改变 information state，后者保存 exact decode state。

### 3. RAVine：Agentic Search 的结果正确性不能替代过程证据

RAVine 构建 dense/BM25 web environment，以 attributable nuggets 和 block-level matching 评估长答案，并增加 tool-use/process metrics。实验暴露最终得分与中间搜索行为并不总一致，也观察到模型绕过检索而依赖内部知识。它证明 evaluation 必须把 answer、evidence、tool trace 分开记录；不证明自动抽取 nuggets 无偏，也不证明离线索引代表开放 Web 的 freshness、权限和 failure model。

## Full Source Review

以下 36 项均核对 v1/官方 first-public、正文方法、实验/附录与 artifact。每项给出原问题、机制/状态、evaluation boundary、trade-off、owner 与 disposition，不把论文名列表当作审计。

### Qwen3-Coder — `QWEN3-CODER-2025-07` — 24/30

官方 2025-07-22 发布披露 480B-total/35B-active MoE、256K native context、execution-driven Code RL、long-horizon Agent RL 与 20,000 环境并行。问题从单次补全变为 repo state、tool feedback 和 delayed credit；environment service 拥有 snapshot/execution/test outcome。作者 benchmark 未给统一 scaffold、samples、hardware 与 leakage audit，不能证明自动 tests 等价真实 specification。Owner `TRAIN-GRPO`，handoff `AGENT-WORKFLOW`；Weekly Only。

### GUI-G² — `ARXIV-2507.15846` — 26/30

v1 2025-07-21。GUI grounding 从单点 reward 演进为 Gaussian target、coverage reward 与自适应方差并接入 GRPO；trainer 拥有 reward geometry，environment 拥有 screenshot/action result。Qwen2.5-VL-7B、8×A100-80GB、bf16、约 100K instances 与 ScreenSpot 支持更平滑 credit，但不能证明动态 UI 和真实副作用泛化。Owner `AGENT-TOOL-CALLING`，handoff `TRAIN-GRPO`；Experimental。

### GR-3 — `ARXIV-2507.15493` — 26/30

v1 2025-07-21。VLA 从单次映射推进到多轮指令、memory-conditioned manipulation 与生成式 trajectory/action modeling；policy 拥有 proposal，controller/environment 保留 physical commit。机器人任务和消融不能替代 safety envelope、calibration drift 与长期运行。Owner `MULTIMODAL-EMBODIED-VLA`；Experimental。

### Being-H0 — `ARXIV-2507.15597` — 26/30

v1 2025-07-21。方法分离 high-level language/vision reasoning 与 low-level whole-body controller，解决 VLM 输出不满足实时动力学的问题；perception、planner、controller 分层拥有状态。作者实验未证明跨 embodiment 或开放环境安全。Owner `MULTIMODAL-EMBODIED-VLA`；Experimental。

### STITCH — `ARXIV-2507.15375` — 25/30

v1 2025-07-21。研究 speech/text 统一表示与跨模态生成，核心取舍是 shared semantic space 与声学时间细节；tokenizer 拥有 modality/timestamp identity。作者任务不证明所有语言、噪声与 streaming SLO 都受益。Owner `MULTIMODAL-REPRESENTATION`；Experimental。

### Dual-Token Constraints / Archer — `ARXIV-2507.15778` — 26/30

v1 2025-07-21。Archer 按 response entropy percentile 区分高低不确定轨迹并施加不同 clipping/KL，修正统一 token policy 的过强/过弱更新。1.5B model、code/math 数据和 DAPO baseline 支持作者设置，不能外推大模型。Owner `TRAIN-GRPO`；Experimental。

### Latent Denoising Tokenizer — `ARXIV-2507.15856` — 25/30

v1 2025-07-21。用 latent denoising 学习视觉 tokenizer，减少离散量化对细节与语义的共同损失；tokenizer 版本决定下游 checkpoint/cache compatibility。重建和生成结果未证明跨模型通用。Owner `MULTIMODAL-REPRESENTATION`；Experimental。

### TokensGen — `ARXIV-2507.15728` — 24/30

v1 2025-07-21。统一 token 序列复用 autoregressive infrastructure，代价是长视觉序列、ordering bias 与 latency；跨尺度生成实验不能与不同 tokenizer/compute 的 diffusion 直接比较。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`；Experimental。

### LLM Economist — `ARXIV-2507.15815` — 21/30

v1 2025-07-21。两层 in-context RL 构造 planner-worker Stackelberg simulation，worker persona/utility 与 planner tax policy 分离，aggregate history 成为共享状态。LLM judge、synthetic persona 和经济假设限制外推。Owner `AGENT-MULTI-AGENT`；Experimental。

### PhysGym — `ARXIV-2507.15550` — 25/30

v1 2025-07-21；31 页 PDF 已读。模型通过受控先验、交互试验和观测恢复物理规律，environment 拥有 dynamics，agent 拥有 hypothesis/action trace。simulator、prompt、budget 与 judge 共同塑造结果，不证明真实科学自治。Owner `PLATFORM-EVALUATION-SYSTEM`；Experimental。

### SPAR — `ARXIV-2507.15245` — 22/30

v1 2025-07-21。五类 Agent 执行 query/reference-chain/judgment/rerank，压缩 198K candidates；SPARBench 仅 50 queries/560 relevant docs，且系统使用不同 search source，F1 差异不能纯归因 multi-agent mechanism。Owner `AGENT-RAG`；Experimental。

### Does More Inference-Time Compute Really Help Robustness? — `ARXIV-2507.15974` — 25/30

v1 2025-07-21。增加 rollout 只有在 proposal diversity 与 verifier reliability 同时成立时才可能提高 robustness；correlated failure 会重复同一错误。受限 benchmark 不能把 pass@k 增长等价可靠性。Owner `PLATFORM-EVALUATION-SYSTEM`，handoff `PLATFORM-SECURITY`；Experimental。

### LAPO — `ARXIV-2507.15758` — 26/30

v1 2025-07-21。把长轨迹 credit 从整条 reward 推进到更细粒度 latent/action-aware optimization，rollout store 与 verifier 必须版本化 trajectory boundary。作者消融未覆盖 verifier error 与大规模异步 lag。Owner `TRAIN-GRPO`；Experimental。

### Hierarchical Budget Policy Optimization — `ARXIV-2507.15844` — 25/30

v1 2025-07-21。高层分配 token/step budget、低层执行推理，使 budget controller 成为 policy state。作者 accuracy-cost 曲线缺 production latency/concurrency SLO，且可能奖励过早停止。Owner `TRAIN-GRPO`，handoff `INFER-SCHEDULING`；Experimental。

### True Multimodal In-Context Learning — `ARXIV-2507.15807` — 24/30

v1 2025-07-21。示例中的 modality、label 与 mapping 都参与更新，强调 exemplar identity、ordering 与 cross-modal binding。诊断任务不能证明开放域 M-ICL 泛化。Owner `MULTIMODAL-REPRESENTATION`；Experimental。

### Beyond Context Limits / TIMRUN — `ARXIV-2507.16784` — 27/30

v1 2025-07-22。observe budget → summarize → new run → restore state 的迭代摘要扩展任务时长，却引入 lossy checkpoint、provenance 丢失与错误累积；不能替代 exact KV state。Owner `AGENT-CONTEXT`，handoff `INFER-GPU-MEMORY`；Experimental。

### Step-Audio 2 — `ARXIV-2507.16632` — 26/30

v1 2025-07-22。报告覆盖 speech tokenizer、统一理解/生成、tool interaction 与 streaming audio，说明时间、speaker 与 codec version 是一等 token identity。训练数据、realtime SLO 与安全边界不完整。Owner `MULTIMODAL-REPRESENTATION`；Experimental。

### MegaScience — `ARXIV-2507.16812` — 27/30

v1 2025-07-22。跨学科 data/evaluation pipeline 把 provenance、difficulty、contamination 和 structured verifier 置于单一 aggregate score 之前。作者结果不证明跨模型或真实研究 workflow 泛化。Owner `TRAIN-DATA`，handoff `PLATFORM-EVALUATION-SYSTEM`；Experimental。

### ThinkAct — `ARXIV-2507.16815` — 26/30

v1 2025-07-22。显式 reasoning/action proposal 与低层 execution 分离，trajectory state、observation refresh 与 physical commit 不同 owner。实验未覆盖 safety、latency jitter 与 distribution shift。Owner `MULTIMODAL-EMBODIED-VLA`；Experimental。

### Semi-off-Policy RL / SOPHIA — `ARXIV-2507.16814` — 25/30

v1 2025-07-22。在高成本 on-policy 与失真 off-policy 之间允许受控 policy lag，并用 correction/selection 管理旧 rollout；收益是 reuse，代价是 importance variance、stale reward 与 version ownership。未覆盖更大异步 fleet。Owner `TRAIN-GRPO`；Experimental。

### Experience is the Best Teacher — `ARXIV-2507.16713` — 26/30

v1 2025-07-22。embodied agent 从成功/失败 trajectory 生成训练 signal，要求 experience provenance、reset policy 与 environment feedback 可追溯。作者仿真/机器人结果可能受失败分布和 intervention 偏差。Owner `MULTIMODAL-EMBODIED-VLA`；Experimental。

### Yume — `ARXIV-2507.17744` — 27/30

v1 2025-07-23。camera-motion quantization、Masked Video Diffusion Transformer、memory module、anti-artifact/time-travel sampling 与 distillation+cache 构成交互 world generation。它仍是视觉 generator，不等于因果可靠 simulator；540P 作者评测不证明物理一致性。Owner `MULTIMODAL-WORLD-MODELS`；Experimental。

### Turing Eye Test — `ARXIV-2507.16863` — 26/30

v1 实际为 2025-07-21。四类 synthetic perception task、15 MLLM、pass@1/32、vision/language SFT 与 ICL 对照把瓶颈定位到视觉编码。版本明确是 preliminary subset，Grad-CAM 不证明普遍机制。Owner `MULTIMODAL-REPRESENTATION`，handoff `PLATFORM-EVALUATION-SYSTEM`；Experimental。

### Multi-Domain Reasoning via RL — `ARXIV-2507.17512` — 27/30

v1 2025-07-23。Qwen2.5-7B、8×A100、veRL、math/code/puzzle 实验显示单域 RL 提升近域却可能损害另一域；response-level reward 不能定位错误 cell。data composition 与 verifier granularity 是共同控制面，不能外推其他模型族。Owner `TRAIN-GRPO`，handoff `TRAIN-DATA`；Experimental。

### RAVine — `ARXIV-2507.16725` — 27/30

v1 2025-07-22。dense/BM25 index、search/fetch、attributable nuggets、block matching 与 process metrics 区分 answer、evidence completeness 与 tool behavior。离线 corpus、自动 nuggets 与 evaluator model 限制开放 Web 外推。Owner `PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-RAG`；Experimental。

### Re:Form — `ARXIV-2507.16331` — 25/30

v1 2025-07-22。Dafny verifier 替代人工 CoT annotation，使 RL 直接消费可执行 correctness；formal kernel 很强，但 specification coverage、compiler version、timeout 与 reward hacking 仍是边界。preliminary Dafny 结果不等价一般软件工程。Owner `TRAIN-GRPO`；Experimental。

### PUSA V1.0 — `ARXIV-2507.16116` — 25/30

v1 2025-07-22。vectorized timestep 允许视频帧处于不同 denoising phase，突破 scalar timestep 的同步约束；新增 timestep-state 与 frame alignment。约 500 美元口径非通用 cost contract，仍有模糊/闪烁。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`；Experimental。

### Finding Dori — `ARXIV-2507.16880` — 25/30

v1 2025-07-22。在 Stable Diffusion v1.4、500 memorized prompts 上用 adversarial text embedding 绕过 pruning，表明“隐藏”不等于“删除”memorization。研究仅覆盖部分层，长期结论是 mitigation 必须做 adaptive attack 与 deletion verification。Owner `PLATFORM-SECURITY`；Experimental。

### Group Sequence Policy Optimization — `ARXIV-2507.18071` — 28/30

v1 2025-07-24。sequence likelihood ratio/clipping 对齐 sequence reward，并分析 token ratio 在长 response 和 MoE routing 下的高方差。Qwen3-30B-A3B 等作者实验支持稳定性和取消 Routing Replay 的可能性，但完整 hardware/cost 与独立复现不足。Owner `TRAIN-GRPO`；Experimental。

### GLiNER2 — `ARXIV-2507.18546` — 23/30

v1 2025-07-24。schema-driven interface 在单 encoder pass 统一 NER、classification、relation，schema 成为输入输出 contract。多任务实验未充分覆盖 schema complexity、长文本、跨域 calibration 与 serving batch。Owner `MODEL-DECODER-ONLY`；Experimental。

### TTS-VAR — `ARXIV-2507.18537` — 25/30

v1 2025-07-24。structure-aware clustering/test-time selection 改进 coarse-to-fine visual AR，避免简单 resampling scale-dependent 失效。GenEval 0.69→0.75 只在作者 evaluator/compute 下成立，position alignment 与 1-D tokenizer 泛化未解。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`；Experimental。

### DriftMoE — `ARXIV-2507.18464` — 23/30

v1 2025-07-24。三层 MLP router 与 Hoeffding-tree experts 在线共训，用 multi-hot correctness mask 取代显式 drift detector。九 streams、10 seeds、Threadripper+2×RTX4090 的 prequential 评测在 class imbalance 上也会崩溃；不能外推 LLM MoE。Owner `MODEL-MOE`；Experimental。

### TeleChat2 / 2.5 / T1 — `ARXIV-2507.18013` — 24/30

v1 2025-07-24。报告披露 10T-token pretraining、long-context annealing、model averaging、SFT/DPO/RL、35B/115B artifacts 与并行可靠性工程；T1 偏长 CoT，2.5 偏速度。未完全披露数据/硬件且为作者评测，作为 lifecycle/version evidence。Owner `TRAIN-PRETRAINING`；Weekly Only。

### TeEFusion — `ARXIV-2507.18192` — 24/30

v1 2025-07-24。线性融合 conditional/unconditional embeddings，将 CFG magnitude 与复杂 sampler teacher 蒸馏进单路 student。SD3/内部模型最高 6× 缺完整 hardware/concurrency/SLO，operational boundary 限制泛化。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`；Experimental。

### SpecForge — `SPECFORGE-2025` — 24/30

官方 2025-07-25。EAGLE-3 draft training、training-time test、online/offline hidden-state production 与 SGLang serving 组成 artifact lifecycle。offline 可低 GPU 但约 12TB states，online 少 disk 却增加 target GPU/failure coupling；MT-Bench 结果缺完整 hardware/concurrency/SLO。Owner `INFER-SPECULATIVE-DECODING`；Books Gate 后才可 Refine。

### Efficient Agents — `ARXIV-2508.02694` — 26/30

arXiv v1 metadata 给出 2025-07-24，按该 first-public owner 归 W30；HTML title page 同时出现“August 11, 2026”，与 v1 metadata 冲突，明确视为 manuscript 内部日期错误，不用于路由或机制证明。旧 Agent 设计倾向叠加更强 backbone、更多 ReAct steps、Best-of-N、复杂 browser 与 memory，因为单任务 capability 是首要约束；当 API/token cost 成为规模瓶颈后，论文以 GAIA、pass@1、token/call cost 和 `cost-of-pass=C/R` 对 backbone、planning interval、tool source、query expansion、memory 与 BoN 做 one-factor-at-a-time 对照，再组合成 Efficient Agents。framework 拥有 plan/tool/memory policy，provider price table 拥有计费版本，evaluation harness 拥有成功判定；GAIA default 为 GPT-4.1、12 steps、plan interval 1、10 searches、BoN 1、simple memory，价格截至 2025-05。作者报告相对 OWL 保留 96.7% performance、单题 cost $0.398→$0.228，但仅单 benchmark、API 价格会漂移、没有 latency/energy/hardware/concurrency/SLO，也无独立 Limitations；不能证明最小组件组合适合所有 workload。简单任务仍应使用小 backbone/少步骤，复杂开放任务可能需要更深 search 和记忆。Owner `PLATFORM-COST`，handoff `AGENT-PLATFORM`、`AGENT-WORKFLOW`；`Emerging / Experimental`。

### InstructVLA — `ARXIV-2507.17520` — 27/30

v1 2025-07-23。旧 VLA 直接在 manipulation data 上 full fine-tune，能学习动作但容易遗忘预训练 VLM 的 OCR、语言和 situated reasoning；新约束是同时保持高层 multimodal understanding、跨 embodiment 指令泛化与低层实时 action generation。InstructVLA 用 MoE LoRA adaptation 和 64 个 latent action queries 将 VLM intention 交给 DINOv2+FiLM、block-causal Transformer/flow-matching action expert，两阶段先训练 action expert（LM+flow loss、约 650M trainable parameters），再做 650K VLA-IT；推理先自回归生成文本至 action query，随后并行 decode queries，并缓存 language response/latent action。VLM 拥有语义意图，action expert 拥有 action trajectory，robot controller/environment 保留 physical commit。SimplerEnv、Google/WidowX、Franka real-world 与 ablation 支持 64-token trade-off、移除 DINOv2 导致作者设置 50% drop、VLA-IT reasoning 提升；但 success rate 受 simulator、annotation、camera/embodiment 与 GPT-4o auxiliary baseline 影响，未证明开放环境 safety、control-frequency jitter 或长期 calibration。直接 atomic instruction/窄域任务下旧 action-only policy 仍更便宜。Owner `MULTIMODAL-EMBODIED-VLA`，handoff `MULTIMODAL-REPRESENTATION`、`TRAIN-LORA`；`Emerging / Experimental`。

### Dens3R — `ARXIV-2507.16290` — 25/30

v1 2025-07-22。旧深度、normal、pointmap 模型分别预测单一几何量，在 camera intrinsics 未知、多 view/多 resolution 场景会产生互不一致的 geometry；Dens3R 用 shared encoder-decoder visual Transformer 和 task heads 统一状态，第一阶段学习 cross-view scale-invariant pointmap，第二阶段加入 surface-normal/one-to-one correspondence 形成 intrinsic-invariant pointmap，再以 512→1024 coarse-to-fine training 与 position-interpolated RoPE 支持高分辨率。backbone 拥有统一 geometric representation，task head 拥有 depth/normal/matching 输出，SfM/downstream pipeline 仍拥有 reconstruction commit。normal、depth、matching、多分辨率 benchmark 和 ablation 支持各组件；shared encoder-decoder 在 512 pair 设置把 memory 4.6GB→4.1GB、parameters 737.591M→624.152M 而 compute 仍为 1.362TFlops。它不证明 metric-scale/pose 在所有传感器成立，thin structures 与 noisy data 仍失败，训练 hardware、latency/concurrency/SLO 也不完整；单任务、已知 intrinsics 或资源受限时专用模型仍合理。Owner `MULTIMODAL-REPRESENTATION`，handoff `MULTIMODAL-WORLD-MODELS`；`Emerging / Experimental`。

### Efficient and Scalable Agentic AI with Heterogeneous Systems — `ARXIV-2507.19635` — 27/30

v1 2025-07-25；26 页 PDF 已读。typed/cyclic Agent graph 配合 compute/memory/bandwidth/cost model、MLIR-like dialect 与 slow/fast planner做异构 placement；workflow IR、profile、placement 与 runtime commit 各有 owner。Llama3 8B/70B、FP16/FP8、多类 accelerator 与 TCO 分析主要是 model/roofline-driven，未公开可执行 compiler/runtime、integer rounding、queue/failure 与 reproduction artifact。Owner `PLATFORM-GPU-SCHEDULER`；Experimental。

## Low-score and Blocked Closure

- **SeC / `2507.15852` / v1 2025-07-21 / 19:** 特定压缩/生成设置，缺跨模型与系统层证据。
- **Spelke Segments / `2507.16038` / v1 2025-07-21 / 19:** 视觉认知诊断有价值，但不改变 representation/runtime contract。
- **SegDT / `2507.15595` / v1 2025-07-21 / 18:** task-specific segmentation，系统影响与 longevity 不足。
- **HOComp / `2507.16813` / v1 2025-07-22 / 18:** human-object composition 范围窄，未形成可复用 mechanism。
- **Task-specific Zero-shot QAT / `2507.16782` / v1 2025-07-22 / 19:** 缺 hardware kernel、latency 与 accuracy contract。
- **CAFT / `2507.16795` / v1 2025-07-22 / 19:** 缺 state ownership、rollback 与跨域 evidence。
- **DesignLab / `2507.17202` / v1 2025-07-23 / 19:** design-domain benchmark，数据/evaluator 过于领域化。
- **Ultra3D / `2507.17745` / v1 2025-07-23 / 19:** 局部 3D generation，未改变 multimodal system 主线。
- **Captain Cinema / `2507.18634` / v1 2025-07-24 / 19:** cinematic application，缺 controllable state 与 production contract。
- **EarthCrafter / `2507.16535` / v1 2025-07-22 / 19:** causal control 和 persistent state 证据不足。
- **Agentar-Fin-R1 / `2507.16802` / v1 2025-07-22 / 19:** 领域数据/benchmark 不支持通用 Agent/RL 结论。
- **A New Pair of GloVes / `2507.18103` / v1 2025-07-24 / 18:** embedding 局部改造，系统 relevance 不足。
- **HLFormer / `2507.17402` / v1 2025-07-23 / 18:** 缺规模、硬件与多 workload 证据。
- **Ray Q3 2025 Roadmap / official issue 2025-07-25 / 16:** design intent，不是 implemented release。
- **Zebra-CoT / `2507.16746` / v1 2025-07-22 / 19:** metadata/abstract 可确认，但 arXiv HTML/PDF 均无法取得；缺 **v1 full text（Method、实验、消融、Appendix、limitations）**。可接受作者项目页全文或 repository 同版 manuscript，建议文件名 `2507.16746v1-zebra-cot.pdf`。补回后重做 mechanism、evaluation contract、score 与 disposition；当前 `Unverified / Blocked — Full Text`。

## Candidate Evidence Gate

- Scored owner rows：54/54。
- High 25～30：29/29 Full Source Review Complete。
- Medium 20～24：10/10 Full Source Review Complete。
- Low/Blocked <20：15/15 source/date/score/rejection or exact-material closure。
- Review Pending：0。
- Unverified / Blocked：1（Zebra-CoT；不阻塞 forward cursor，但阻塞“无材料缺口”声明）。
- Candidate Evidence Gate：`Conditional Pass — 1 Exact External Material Blocker`；允许 forward cursor 继续，但阻塞无缺口声明和 2025 Archive Completion。
- Historical Books Gate：`Closed`。

## Independent Review Checkpoint

- **Date / revision:** 54 个 owner 均按 first-public/v1 重新核对；arXiv retained rows 的 owner 绑定 v1，后来 revision 只更新同一 Source Family 的证据，不创建新评分行。Turing Eye Test 已纠正为 v1 2025-07-21；Efficient Agents 按 arXiv v1 2025-07-24 路由，HTML title-page 的 2026-08-11 冲突日期不作为 owner 证据。
- **Source boundary:** 39 个 retained 中，38 个具有可读取论文/技术报告/官方工程全文；Qwen3-Coder 只有官方发布、model card 与 repository，因内部 RL/scheduler 未披露固定为 `Mechanism Partially Disclosed`。Zebra-CoT 只有 metadata/abstract，已降级而非沿用 20+。
- **Score arithmetic:** 54/54 Total 与六维分数逐行机器复算一致；分层为 29 high、10 medium、15 low/blocked。
- **Review coverage:** 39/39 retained 有候选专属机制、状态或控制流、evaluation boundary、trade-off、coexistence 与 owner/disposition；15/15 low/blocked 有 source/date/score/rejection 或精确材料请求。
- **Dedup:** 14 个 pre-W30 v1 spillback 只列回拨关系，不在本周重复计分；本周 Source Family/primary identifier 无重复 owner。
- **Markdown / Git:** 标题层级、表格、URL、行尾空白与本文件 `git diff --check` 通过；没有 stage、unstage、commit 或 push。

## Cross-Week Deduplication

以下在当周 discovery 页面再次出现但 v1 早于 2025-07-21，均回拨 W29，不在 W30 重复计分：MiroMind-M1、Invisible Leash、WebShaper、NoHumansRequired、Inverse Scaling、Video Thinking Test、MCPEval、Streaming4D、Try Again、Serial Scaling、MUR、nablaNABLA、DMOSpeech2、Promptomatix。revision/project page/code release 留在同一 Source Family history。

## Evidence Level

- **Official / Artifact:** Qwen3-Coder、SpecForge、TeleChat artifacts 与 Ray roadmap；只陈述公开版本和接口。
- **Primary Research / Author Evidence:** 其余 arXiv/technical report；结论绑定作者实验，默认 Experimental。
- **Project Inference:** Source Family、owner、演进关系与 Books disposition 是本项目判断。

## Knowledge Tree Position

- Training：`TRAIN-DATA`、`TRAIN-GRPO`、`TRAIN-DISTRIBUTED-TRAINING`。
- Multimodal：`MULTIMODAL-REPRESENTATION`、`MULTIMODAL-GENERATIVE-PARADIGMS`、`MULTIMODAL-WORLD-MODELS`、`MULTIMODAL-EMBODIED-VLA`。
- Runtime：`INFER-SPECULATIVE-DECODING`、`INFER-GPU-MEMORY`、`INFER-SCHEDULING`。
- Platform：`PLATFORM-EVALUATION-SYSTEM`、`PLATFORM-GPU-SCHEDULER`、`PLATFORM-SECURITY`。
- Agent：`AGENT-CONTEXT`、`AGENT-RAG`、`AGENT-TOOL-CALLING`、`AGENT-WORKFLOW`、`AGENT-MULTI-AGENT`。

## Recommended Action

- 保留 GSPO、TIMRUN、RAVine、Yume、TET、multi-domain RL、PhysGym、Efficient Agents、InstructVLA、Dens3R 与 heterogeneous Agent systems 作为未来 Source-Family Books Gate 的重点 packet。
- SpecForge 只在 Historical Books Gate 开启后 refine 既有 artifact lifecycle，不写项目功能表。
- Zebra-CoT 等待 v1 正文；低分候选保持 Archive Only。

## Event-Date Daily Decision

Historical Backfill 不创建历史 Daily；所有事件日期、证据与 rejection 直接记录在本 Weekly。

## Books Integration Decision

`Frozen — Historical Books Gate Closed`。本周 Candidate Evidence Gate 仅为 Conditional Pass，且 2025 全年 Evidence Gate 尚未通过；Zebra-CoT 外部材料缺口关闭前不得宣称 Archive Completion。本轮不修改 Books、ROADMAP、DECISIONS 或 Learning State。

## Ignored Noise

- 转载、榜单截图、无 primary identifier 聚合、旧论文重发、无条件 benchmark。
- API alias、价格与 roadmap 若未形成已实现机制，只作版本/设计意图事实。
- v1 属前周的论文不重复计分。

## Repository Changes

- W30 从 3 个 lower-bound owner 重建为 54 个 scored owner，其中 3 个由 W32 routing spillback 恢复。
- 39/39 retained 完成 Full Source Review；15/15 low/blocked 完成 closure。
- 仅修改本 Weekly；未修改年度索引、Daily、Books、ROADMAP、DECISIONS 或 Learning State。

## Open Questions

- Zebra-CoT v1 正文补回后是否存在足以恢复 20+ 的机制证据？
- GSPO 在非 MoE、不同 policy lag 与独立 fleet 上的 bias/variance 边界如何？
- attributable nugget 如何在动态 Web、权限和删除/更新下保持 provenance/freshness？
- world generation 如何与 causal controllability、persistent state 和 physical safety 分离评估？

## Sources

以下 primary sources 均于 2026-08-24 重新访问；官方首发日或 arXiv v1 日期列于各项后。

- Qwen3-Coder — https://qwenlm.github.io/blog/qwen3-coder/（2025-07-22）
- GUI-G² — https://arxiv.org/abs/2507.15846（v1 2025-07-21）
- GR-3 — https://arxiv.org/abs/2507.15493（v1 2025-07-21）
- Being-H0 — https://arxiv.org/abs/2507.15597（v1 2025-07-21）
- STITCH — https://arxiv.org/abs/2507.15375（v1 2025-07-21）
- Archer — https://arxiv.org/abs/2507.15778（v1 2025-07-21）
- Latent Denoising Tokenizer — https://arxiv.org/abs/2507.15856（v1 2025-07-21）
- TokensGen — https://arxiv.org/abs/2507.15728（v1 2025-07-21）
- LLM Economist — https://arxiv.org/abs/2507.15815（v1 2025-07-21）
- PhysGym — https://arxiv.org/abs/2507.15550（v1 2025-07-21）
- SPAR — https://arxiv.org/abs/2507.15245（v1 2025-07-21）
- Inference-Time Compute and Robustness — https://arxiv.org/abs/2507.15974（v1 2025-07-21）
- LAPO — https://arxiv.org/abs/2507.15758（v1 2025-07-21）
- HBPO — https://arxiv.org/abs/2507.15844（v1 2025-07-21）
- True Multimodal ICL — https://arxiv.org/abs/2507.15807（v1 2025-07-21）
- TIMRUN — https://arxiv.org/abs/2507.16784（v1 2025-07-22）
- Step-Audio 2 — https://arxiv.org/abs/2507.16632（v1 2025-07-22）
- MegaScience — https://arxiv.org/abs/2507.16812（v1 2025-07-22）
- ThinkAct — https://arxiv.org/abs/2507.16815（v1 2025-07-22）
- SOPHIA — https://arxiv.org/abs/2507.16814（v1 2025-07-22）
- Experience is the Best Teacher — https://arxiv.org/abs/2507.16713（v1 2025-07-22）
- Yume — https://arxiv.org/abs/2507.17744（v1 2025-07-23）
- Turing Eye Test — https://arxiv.org/abs/2507.16863（v1 2025-07-21）
- Multi-Domain Reasoning via RL — https://arxiv.org/abs/2507.17512（v1 2025-07-23）
- RAVine — https://arxiv.org/abs/2507.16725（v1 2025-07-22）
- Re:Form — https://arxiv.org/abs/2507.16331（v1 2025-07-22）
- PUSA V1.0 — https://arxiv.org/abs/2507.16116（v1 2025-07-22）
- Finding Dori — https://arxiv.org/abs/2507.16880（v1 2025-07-22）
- GSPO — https://arxiv.org/abs/2507.18071（v1 2025-07-24）
- GLiNER2 — https://arxiv.org/abs/2507.18546（v1 2025-07-24）
- TTS-VAR — https://arxiv.org/abs/2507.18537（v1 2025-07-24）
- DriftMoE — https://arxiv.org/abs/2507.18464（v1 2025-07-24）
- TeleChat2 / 2.5 / T1 — https://arxiv.org/abs/2507.18013（v1 2025-07-24）
- TeEFusion — https://arxiv.org/abs/2507.18192（v1 2025-07-24）
- SpecForge — https://www.lmsys.org/blog/2025-07-25-spec-forge/（2025-07-25）
- SpecForge repository — https://github.com/sgl-project/SpecForge（release artifact）
- Efficient Agents — https://arxiv.org/abs/2508.02694（v1 metadata 2025-07-24；HTML manuscript date conflict noted）
- InstructVLA — https://arxiv.org/abs/2507.17520（v1 2025-07-23）
- Dens3R — https://arxiv.org/abs/2507.16290（v1 2025-07-22）
- Heterogeneous Agentic AI Systems — https://arxiv.org/abs/2507.19635（v1 2025-07-25）
- SeC — https://arxiv.org/abs/2507.15852（v1 2025-07-21）
- Spelke Segments — https://arxiv.org/abs/2507.16038（v1 2025-07-21）
- SegDT — https://arxiv.org/abs/2507.15595（v1 2025-07-21）
- HOComp — https://arxiv.org/abs/2507.16813（v1 2025-07-22）
- Task-specific Zero-shot QAT — https://arxiv.org/abs/2507.16782（v1 2025-07-22）
- CAFT — https://arxiv.org/abs/2507.16795（v1 2025-07-22）
- DesignLab — https://arxiv.org/abs/2507.17202（v1 2025-07-23）
- Ultra3D — https://arxiv.org/abs/2507.17745（v1 2025-07-23）
- Captain Cinema — https://arxiv.org/abs/2507.18634（v1 2025-07-24）
- EarthCrafter — https://arxiv.org/abs/2507.16535（v1 2025-07-22）
- Agentar-Fin-R1 — https://arxiv.org/abs/2507.16802（v1 2025-07-22）
- A New Pair of GloVes — https://arxiv.org/abs/2507.18103（v1 2025-07-24）
- HLFormer — https://arxiv.org/abs/2507.17402（v1 2025-07-23）
- Ray Q3 2025 Roadmap — https://github.com/ray-project/ray/issues/54883（2025-07-25）
- Zebra-CoT — https://arxiv.org/abs/2507.16746（v1 2025-07-22；full text blocked）
