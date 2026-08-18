# AI Research Weekly — 2025-W18

> Coverage Window: 2025-04-28～2025-05-04
> Research Mode: Retrospective Backfill
> Audit Status: Candidate Evidence Gate Passed — 43/43 Scored；36/36 Retained Packets；7/7 Low-score Closures；0 Pending / 0 Blocked / 1 Terminal Disputed
> Historical Books Gate: Closed — existing decisions are provisional
> Accessed: 2026-07-31
> Backfilled: 2026-07-31
> Last Re-audited: 2026-08-24

## Executive Summary

旧版只保留Qwen3，无法证明2025-04-28～05-04来源召回或全文阅读已经闭合。本轮最终恢复43个
scored owner identities：36个20+（18个25～30、18个20～24）和7个低分。36/36个retained
candidates均完成非模板化Full Source Review；PIPA 2025-05-02 v1正文已恢复并与05-06 AURA
revision隔离。VideoHallu的正文已读完，但论文所称GRPO与展示的objective/reward contract冲突，
因此作为terminal `Disputed`冻结而非Review Pending。Review Pending=0，Blocked=0，Candidate
Evidence Gate通过；跨索引不可复现导出与VideoHallu event-time artifact仍使年度Archive Gate保持Open。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 归档；搜索收录日与后续修订不替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery 与去重；论文机制回到正文。Crossref 仅做 Weekly metadata 交叉检查。
- 历史回填不补造 Daily；Accessed 统一为 2026-07-31。
- benchmark 缺少模型、硬件、长度、batch/concurrency、precision/quantization 与 SLO 时不做通用结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：GPT-4o sycophancy rollback/postmortem、Qwen3、Phi-4 reasoning、Phi-4 Mini Reasoning、
  DeepSeek-Prover-V2、MiMo-7B、Nova Premier与Llama-Nemotron technical report。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 恢复26个20+学术owner与7个低分闭合。PIPA v1已全文核验；VideoHallu保持terminal Disputed。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- Ray 2.45.0以21/30保留为versioned runtime contract；不把release中的局部性能数字外推为通用结论。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GPT-4o sycophancy rollback and postmortem | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Release-gate incident |
| Qwen3 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Hybrid reasoning runtime contract |
| Phi-4-reasoning | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Compact reasoning recipe |
| Phi-4-Mini-Reasoning | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Staged small-model branch |
| DeepSeek-Prover-V2 | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Executable theorem verification |
| MiMo-7B release | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Later report boundary |
| Amazon Nova Premier | 2 | 3 | 4 | 5 | 3 | 3 | 20/30 | Full Source Review Complete — Version Fact / Mechanism Not Disclosed |
| Llama-Nemotron technical report | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Train/runtime co-design |
| Mem0 | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Full Source Review Complete — Mutable external memory |
| One-shot RLVR | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Full Source Review Complete — Exploration/data boundary |
| The Leaderboard Illusion | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Full Source Review Complete — Submission-lineage bias |
| UniversalRAG | 4 | 3 | 4 | 4 | 4 | 4 | 23/30 | Full Source Review Complete — Conditional retrieval branch |
| ReasonIR | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Reasoning-aware retriever |
| Meta Policy Optimization | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Evolving reward rubric |
| WebThinker | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete — Deep-research workflow |
| Softpick | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Source Review Complete — Rectified attention branch |
| TesserAct | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — 4D world-state branch |
| NORA | 4 | 3 | 4 | 4 | 4 | 3 | 22/30 | Full Source Review Complete — Compact VLA control |
| Mixture of Sparse Attention | 4 | 4 | 3 | 4 | 4 | 3 | 22/30 | Full Source Review Complete — Expert-choice attention |
| Graph-of-Tokens MoE routing | 4 | 3 | 3 | 4 | 4 | 3 | 21/30 | Full Source Review Complete — Context-aware routing |
| Ava agentic video analytics | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Event-graph retrieval |
| Transferable black-box VLM attacks | 5 | 5 | 4 | 4 | 4 | 3 | 25/30 | Full Source Review Complete — Shared-representation threat |
| Self-generated in-context agent examples | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Trajectory-derived memory |
| PIPA interactive planning evaluation | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Source Review Complete — v1 isolated from AURA revision |
| Always Tell Me The Odds | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Source Review Complete — Conditional calibration |
| UQLM uncertainty-quantification suite | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Versioned UQ Toolkit / No Change |
| VideoHallu | 4 | 3 | 4 | 4 | 4 | 3 | 22/30 | Disputed — GRPO label/objective mismatch |
| Towards Safer Pretraining / HarmFormer | 3 | 4 | 4 | 4 | 4 | 3 | 22/30 | Full Source Review Complete — Data-filter contract |
| Ray 2.45.0 | 2 | 4 | 4 | 5 | 4 | 2 | 21/30 | Full Source Review Complete — Versioned runtime contract |
| TD-Eval | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Turn/dialogue evidence |
| Spark scientific idea-generation system | 4 | 3 | 3 | 4 | 4 | 3 | 21/30 | Full Source Review Complete — Retrieval/judge workflow |
| ARTIST / Agentic Reasoning and Tool Integration via RL | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Source Review Complete — Tool-output-masked agentic RL |
| R&B Domain Regrouping and Data Mixture Balancing | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Source Review Complete — Gradient-defined data ownership |
| SWE-smith | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete — Executable training-data factory |
| Who&When Multi-Agent Failure Attribution | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Full Source Review Complete — Trace-level blame evidence |
| Practical Efficiency of Muon for Pretraining | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Source Review Complete — Optimizer/time Pareto branch |
| Taming the Titans survey | 2 | 3 | 3 | 4 | 3 | 4 | 19/30 | Low-score Source/Date/Rejection Verified |
| A Survey on LLM-based Human-Agent Systems | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score Source/Date/Rejection Verified |
| Parameter-Efficient Transformer Embeddings | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Low-score Source/Date/Rejection Verified |
| Controllable Weather Synthesis and Removal | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Low-score Source/Date/Rejection Verified |
| Retrieval-augmented ICL for Multimodal Disease Classification | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Low-score Source/Date/Rejection Verified |
| A Survey on Inference Engines for Large Language Models | 2 | 3 | 4 | 4 | 3 | 3 | 19/30 | Low-score Source/Date/Rejection Verified — Secondary engine matrix |
| Low-Precision Training of Large Language Models | 2 | 3 | 4 | 4 | 3 | 3 | 19/30 | Low-score Source/Date/Rejection Verified — Secondary synthesis |

### Deep Analysis 1 — Qwen3

- First Public: 2025-04-29
- Status: Official open-weight release
- Primary Source: https://qwenlm.github.io/blog/qwen3/
- Evolution Relationship: Direct Evolution

#### Why

用户既需要低延迟即时回答，也需要高预算 reasoning；如果为两种行为维护独立模型，会增加训练、部署与路由成本。

#### Principle and Mechanism

Qwen3 在同一模型中提供 thinking/non-thinking modes，并组合 dense/MoE 尺寸、长上下文与 reasoning post-training。

#### Trade-off and Evidence Boundary

统一模型减少 model fleet 分裂，却把 mode control、prompt format、budget accounting 和 capacity planning 变成 runtime contract；厂商 benchmark 不能证明所有 workload 的 Pareto 优势。

#### Connection and Evolution

知识树位置：第 20～24、29、45、46 章。Must Read；与 Claude 3.7、DeepSeek V3.1 形成 hybrid reasoning 演进链。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### Qwen3

- **Candidate / Week / Score:** Qwen3 / 2025-W18 / 26/30。
- **Source Family ID:** `qwen3-2025-base-hybrid-reasoning`。
- **Source Type:** 官方 release blog、open-weight model cards/repository，以及后续 arXiv technical report。
- **First-public Date / Revision History:** Qwen3 weights/blog 2025-04-29；Technical Report arXiv v1 2025-05-14（属于 W20 的后续 evidence，但与 release 联读）；截至访问日 report 只有 v1。7 月 2507 variants 不反投影到本候选。
- **Direct Primary Sources:** Qwen3 release blog、QwenLM/Qwen3 repository、Qwen/Qwen3-235B-A22B model card。
- **Related Primary Sources:** Qwen3 Technical Report arXiv:2505.09388（35 页）；QwQ-32B和 Qwen2.5作为训练/架构前序。
- **Access and Verification Status:** Verified；release/model card 与 report 的 architecture、pretraining、全部 base/post-training evaluation、four-stage post-training及 references 已读。训练代码、RL stack与完整 artifact未公开。
- **Full-read Coverage:** metadata；architecture tables；data construction与三阶段 pretraining；15个 base benchmarks；long-CoT cold start、reasoning RL、thinking-mode fusion、thinking budget；model cards/chat templates；限制与未披露项。
- **Original Problem:** 独立 chat model 与 reasoning model 形成两个 weight fleet，带来训练、部署、路由、cache和版本治理成本；固定 reasoning depth又无法按任务复杂度控制 latency/cost。
- **Why the Previous Design Was Reasonable:** 独立模型避免 thinking/non-thinking behavior相互干扰，能为各自目标单独调优、容量规划和回归测试；简单请求无需承担长 CoT。
- **Changed Constraint:** 同一产品需要在即时响应与高 test-time compute之间动态切换，同时用 open-weight family覆盖从 0.6B dense 到 235B MoE 的部署规模。
- **Mechanism:** 先做 long-CoT cold start，再以3,995个 query-verifier pairs和 GRPO reasoning RL训练 thinking policy；随后用 thinking data（Stage 2 model rejection sampling）与 curated non-thinking data持续 SFT，通过 `/think`、`/no_think`和空 thinking block统一格式，最后做 general-domain RL。Thinking budget通过 early termination控制最大 reasoning tokens。
- **State Ownership:** model weights承载两种行为；chat template/host选择mode与budget；serving runtime拥有token budget、KV、admission和SLO。模型不拥有业务级budget policy。
- **Control Flow / Data Flow:** request + mode flag/budget → 同一 policy生成 hidden/visible thinking block → 达到终止条件或budget → final answer；训练链为 base → cold-start SFT → verifier reward rollouts/GRPO → mode-fusion SFT → general RL。
- **Implementation Details:** dense采用GQA、SwiGLU、RoPE、pre-RMSNorm，移除QKV bias并加入QK-Norm；MoE为128 experts、每token激活8个、无shared expert，并使用global-batch load-balancing loss。模型context table为32K或128K；release blog早期pretraining叙述32K extension与最终 model card需按具体checkpoint解释。
- **Evaluation Setup:** base model用15个general/reasoning/math/code/multilingual benchmarks，同一 pipeline与few-shot/CoT设置比较Qwen2.5、DeepSeek-V3、Gemma3、Llama3/4等；post-training含AIME、LiveCodeBench、CodeForces、BFCL等作者评测。Report未提供生产latency/cost测量。
- **Baselines / Ablations / Sensitivity:** report比较不同规模和dense/MoE baseline，并给thinking budget随token增加的趋势；没有完整mode-fusion ablation、budget-to-latency曲线、router/load-balance sensitivity或独立复现。AIME单次RL run从70.1到85.1只证明该recipe实例。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model sizes、experts、active params、context与pretraining tokens（约36T）披露；硬件、训练precision、global batch、rollout batch/并发、serving quantization、TTFT/TPOT和SLO为 `Not Disclosed`。作者只说large batch/high rollouts有利。
- **What the Evidence Actually Proves:** 一个open-weight policy可通过显式数据与template把thinking/non-thinking behaviors合并，并暴露推理budget control；在作者benchmark中不同budget表现有系统差异。
- **What It Does Not Prove:** 不证明单模型在所有 workload 都比双模型fleet便宜/更稳、thinking trace忠实、budget与质量单调于所有任务、MoE active params直接等于真实成本，或厂商benchmark可跨scaffold比较。
- **Limitations / Threats to Validity:** vendor-authored evaluation；训练hardware/precision/系统成本缺失；无mode interference与forgetting ablation；benchmark contamination和grader差异；report晚于release两周；后续2507改变checkpoint语义。
- **Trade-offs / New Failure Modes:** 合并fleet减少weight duplication与外部router，却新增mode adherence、prompt/template identity、budget enforcement、thinking token容量、错误早停、mode contamination和同endpoint latency bimodality；MoE另有expert routing/communication与hotspot。
- **Where the Previous Design Still Applies:** 强隔离SLO、独立安全策略、不同hardware/quantization、简单请求占绝大多数或需要可预测latency时，独立chat/reasoning models或host router仍合理。
- **Evolution Relationship:** 对QwQ/独立reasoning model为 `Direct Evolution`；对serving scheduler是 `Layering / Dependency`。它与Claude3.7/后续DeepSeek hybrid reasoning形成同一设计分支，不表示后者覆盖前者。
- **ROADMAP Node:** 主owner `INFER-SCHEDULING` Ch56 / legacy Ch52，training handoff `TRAIN-GRPO` Ch33 / legacy Ch29；`MODEL-SAMPLING` Ch20与`MODEL-MOE` Ch21只承担机制边界。
- **Target and Adjacent Chapters Read:** 已读Ch55～56、Ch20～21与Ch32～34，核对mode/budget、MoE cost与post-training owner。
- **Existing Coverage:** Ch56已有request-level effort/SLO scheduling，Ch33已有cold start→reasoning RL→general能力恢复；Qwen3增加同一policy的mode/template/budget identity案例，但是否改变正文须待Historical Books Gate。
- **Integration Decision:** `Refine — Existing Argument Candidate`；Books Frozen。
- **Changed Files or Rejection Reason:** 本轮不修改Books；不记录型号benchmark，也不把W20 technical report倒写成release时已公开材料。
- **Open Questions:** mode-fusion data比例与干扰、thinking budget训练目标、不同budget下calibration与SLO、MoE expert placement、rollout系统和general RL细节均未公开。

### GPT-4o sycophancy rollback and postmortem

- **Identity / Sources / Coverage:** 28/30，`openai-gpt4o-sycophancy-2025-04`；04-25 update、04-28 rollback、04-29 note与05-02 postmortem联读，覆盖chronology、causal analysis、eval/release process与mitigation。
- **Problem / Previous / Changed:** reward、memory、fresh data与thumbs feedback各自优化有用proxy原本合理；组合后primary reward变弱、agreeableness被放大，而qualitative flag非blocking且没有sycophancy deployment eval。
- **Mechanism / State / Flow:** 这是incident analysis而非新模型算法；dataset/reward mix、eval suite、release gate、monitor与rollback拥有控制状态。candidate→offline eval→A/B→release→monitor→rollback。
- **Evaluation / Evidence Boundary:** 只证明该release/process failure与behavior-specific blocking eval需求；model internals、hardware、precision与完整ablation未披露，不证明memory贡献或某个cure普适。
- **Trade-off / Failure / Previous Design:** aggregate gate便宜但会漏interaction；新增专项gate增加release cost。风险含proxy gaming、qualitative evidence被忽略和rollback latency；单独信号仍可在interaction tests下使用。
- **Owner / Adjacent / Decision / Open:** `PLATFORM-EVALUATION-SYSTEM` Ch66，handoff Ch31/73；已读相邻evidence/release chapters。`Refine — Existing Argument Candidate`，Books Frozen；待interaction ablation、canary threshold与calibration。

### Phi-4-reasoning

- **Identity / Sources / Coverage:** 26/30，`microsoft-phi4-reasoning`；arXiv:2504.21318 v1 04-30，已读SFT/RL recipe、evaluation、appendix与limitations。
- **Problem / Previous / Changed:** compact 14B direct-SFT/chat响应快且简单，但长推理与可验证STEM/code需要更多trajectory capacity。
- **Mechanism / State / Flow:** 1.4M+ teachable prompts含teacher demonstrations做SFT；reasoning-plus再加short outcome-verifiable RL并产生更长答案。weights拥有policy，scaffold/evaluator拥有generation和scoring。
- **Evaluation / Boundary:** 14B/32K、多math/code/science author benchmarks；hardware、precision、batch、concurrency、SLO未披露。不证明general knowledge、trace faithfulness或摆脱teacher/scaffold。
- **Trade-off / Failure / Coexistence:** teacher error、长decode、verifier bias、trace-answer contradiction与truncation；bounded latency仍适合短响应Phi。
- **Owner / Decision:** `TRAIN-SFT` Ch29，handoff Ch33/56；已读相邻post-training/runtime chapters。`Refine — Existing Argument Candidate`，Books Frozen。

### Phi-4-Mini-Reasoning

- **Identity / Sources / Coverage:** 25/30，`microsoft-phi4-mini-reasoning`；arXiv:2504.21233 v1 04-30，四阶段训练、step ablation、evaluation与appendix已读。
- **Problem / Previous / Changed:** 3.8B纯SFT或单阶段RL便宜，却有较少reasoning headroom和更不稳定RL。
- **Mechanism / State / Flow:** distillation mid-training→distillation FT→rollout DPO→RLVR；长度16K→20K→25K，前两阶段batch128/LR1e-5/5 epochs，DPO/RL LR5e-7/1 epoch。
- **Evaluation / Boundary:** AIME24/Math500/GPQA，temp .6、top-p .95、max32K、3 runs；hardware未披露。支持该实例的staged curriculum，不证明每阶段普适必要。
- **Trade-off / Failure / Coexistence:** teacher inheritance、long-output cost、reward overfit；小SFT path仍适合非推理/低SLO任务。
- **Owner / Decision:** `TRAIN-SFT` Ch29，handoff Ch34/33；`Refine — Existing Argument Candidate`，Books Frozen。

### DeepSeek-Prover-V2

- **Identity / Sources / Coverage:** 27/30，`deepseek-prover-v2`；arXiv:2504.21801 v1 04-30、official repo，Method、Lean artifact、training、evaluation与appendix已读。
- **Problem / Previous / Changed:** theorem-level生成简单但reward sparse；自然语言推理不保证Lean可执行正确性。
- **Mechanism / State / Flow:** V3生成NL sketch与Lean subgoals，7B递归解子目标；verified proofs+CoT做cold start，再expert iteration/GRPO。Lean env/verifier拥有correctness，rollout store拥有candidates，policy只proposal。
- **Evaluation:** Lean4.9.0-rc2、MiniF2F Pass@1/32/1024/8192；671B SFT context16384、GRPO 256 prompts/iter×32 proofs、max32768，再distill 7B。
- **Evidence / Failure / Coexistence:** 支持decomposition+executable verifier在巨大sampling budget下成立；不证明cheap/general reasoning。论文观察benchmark bug、vacuous proof与reward hacking；monolithic generation仍适合小定理/低预算。
- **Owner / Decision:** `TRAIN-GRPO` Ch33，handoff Ch66；`Integrate — New Mechanism Candidate`但Books Frozen。

### MiMo-7B release

- **Identity / Sources / Coverage:** 25/30，`xiaomi-mimo-7b`；official weights/repo 04-30；arXiv:2505.07608 v1 05-12是W20 related report，联读但不倒写。
- **Problem / Previous / Changed:** compact open model希望兼顾math/code reasoning；release时完整训练contract未公开。
- **Mechanism / State / Flow:** later report披露25T three-stage pretraining、MTP与约130K math/code prompts RL、difficulty-driven code reward/resampling；这些是后续family evidence，不是04-30 announcement contemporaneous disclosure。
- **Evaluation / Boundary:** 证明04-30 artifact存在和后续report描述recipe；不证明release claims独立可复现或production cost，hardware/precision/SLO不完整。
- **Trade-off / Failure / Coexistence:** later-evidence contamination、verifier/reward bias、MTP compatibility与compact capacity ceiling；普通small model仍适合更低复杂度。
- **Owner / Decision:** `TRAIN-PRETRAINING` Ch28 + Ch33，MTP handoff Ch48；`Emerging / Experimental`，Books Frozen。

### Amazon Nova Premier

- **Identity / Sources / Coverage:** 20/30，`amazon-nova-premier-2025-04`；official AWS announcement 04-30全文核验。
- **Problem / Mechanism Boundary:** release把model定位为complex-task model与distillation teacher；architecture、training、system card、state/control flow与matched evaluation均`Not Disclosed`，不能从产品能力反推。
- **Evidence / Non-evidence:** 只证明GA/version/teacher-distillation positioning，不证明安全机制、通用优势或内部runtime。
- **Trade-off / Coexistence:** teacher可降低student data构建成本，却引入teacher dependency、license与quality transfer风险；自有data/SFT仍适合可控任务。
- **Owner / Adjacent / Decision:** `TRAIN-SFT` Ch29 version-fact handoff；`Weekly Only — Version/Product Fact`，不进入Books。

### Llama-Nemotron technical report

- **Identity / Sources / Coverage:** 28/30，`nvidia-llama-nemotron-2025`；arXiv:2505.00949 v1 05-02；March release是earlier family node。架构搜索、post-training、system implementation、evaluation/ablation/appendix已读。
- **Problem / Previous / Changed:** uniform Transformer与decoupled trainer/generator简化工具，但reasoning quality、throughput、latency、data与RL rollout开始相互约束。
- **Mechanism / State / Flow:** Puzzle block library+MIP按hardware/latency/memory/throughput搜索nonuniform blocks/FFN Fusion；SFT/GRPO。RL在Megatron trainer与vLLM generator间all-gather权重→shared memory→训练offload/release→vLLM wake/generate→release→trainer reload。
- **Evaluation Contract:** Super单H100 TP1 FP8约300K cached tokens，Ultra 8 H100；RL 72×8 H100，train TP8/SP/CP2/PP18/DP2，generation TP8/DP72，BF16+FP32 optimizer/FP8 generation，约140k H100-hours；data scale与LR/curriculum ablation。
- **Evidence / Failure / Coexistence:** 支持该co-designed instance与phase/state ownership；不证明跨hardware最优。风险含search objective过拟合、weight skew、memory phase handoff与成本；uniform architecture仍适合portability。
- **Owner / Decision:** `TRAIN-DISTRIBUTED-TRAINING` Ch36，handoff Ch49/50；`Integrate — New Mechanism Candidate`，Books Frozen。

### Mem0

- **Identity / Sources / Coverage:** 26/30，`mem0-production-memory`；arXiv:2504.19413 v1 04-28，paper+code/project；Method、LOCOMO、latency/token analysis与prompts/algorithm已读。
- **Problem / Previous / Changed:** full context/RAG无外部可变状态、简单可审计，但有限、昂贵、噪声大且session-bound；长期交互要求selective update/delete。
- **Mechanism / State / Flow:** summary+recent window→LLM extraction→similar-memory retrieval→ADD/UPDATE/DELETE/NOOP；Mem0g增加timestamped entity graph与dual retrieval。external DB/graph拥有state，host拥有identity/provenance/erase。
- **Evaluation:** LOCOMO 10 conversations、约600 dialogues/26k tokens each、约200 QA；m=s=10、GPT-4o-mini、dense embedding/Neo4j、judge 10 runs；测p95/token/search latency。
- **Evidence / Failure / Coexistence:** 支持vendor-run contract下selective memory优于tested full-context/RAG；不证明production update correctness。风险含stale/conflict、wrong merge、destructive delete、privacy leak；短/read-only session仍适合context/RAG。
- **Owner / Decision:** `AGENT-MEMORY` Ch77，handoff Ch76；`Integrate — New Mechanism Candidate`，Books Frozen。

### One-shot RLVR

- **Identity / Sources / Coverage:** 25/30，`rlvr-one-example-2504.20571`；arXiv v1 04-29，setup、curves、ablations与appendix已读。
- **Problem / Previous / Changed:** 大verified dataset稳健但昂贵；问题是RL gain究竟来自new knowledge还是exploration/optimization。
- **Mechanism / State / Flow:** 500-step probe按variance排序1,209 DSR examples，选一例复制128 samples，8 responses/prompt，以GRPO/PPO更新；rollout/reward/optimizer拥有训练state。
- **Evaluation / Boundary:** Qwen2.5-Math 1.5B/7B、Llama3.2-3B、R1-distill，math tasks；best-checkpoint、example sensitivity和unstable runs限制外推。作者明确不节省RL compute。
- **Trade-off / Failure / Coexistence:** selection bias、math-only、wrong-label tolerance与high sensitivity；大dataset仍适合coverage/robustness。
- **Owner / Decision:** `TRAIN-GRPO` Ch33；`Emerging / Experimental`，Books Frozen。

### The Leaderboard Illusion

- **Identity / Sources / Coverage:** 27/30，`arena-leaderboard-illusion`；arXiv:2504.20879 v1 04-29，data audit、Bradley-Terry assumptions、simulation与appendix已读。
- **Problem / Previous / Changed:** pairwise arena在unbiased/interconnected comparisons下合理；private variant testing、selective disclosure/retraction改变sampling distribution。
- **Mechanism / State / Flow:** leaderboard需要拥有submission identity、variant lineage、comparison graph与disclosure policy；authors审计Jan–Mar variant/de-anonymization并模拟best-of-N lift。
- **Evidence / Boundary:** 支持selective disclosure破坏unbiased-sampling premise并抬高expected maxima；不证明每个provider有意gaming或给出true capability ranking。
- **Trade-off / Failure / Coexistence:** 强lineage/disclosure增加运营/隐私成本；provider inference、scraping gaps、fragmented graph与position bias仍存在。开放稳定submission仍可用传统BT。
- **Owner / Decision:** `PLATFORM-EVALUATION-SYSTEM` Ch66；`Integrate — New Mechanism Candidate`，Books Frozen。

### UniversalRAG

- **Identity / Sources / Coverage:** 23/30，`universalrag-2504.20734`；v1 04-29，later revisions不倒写；Method/evaluation已读。
- **Problem / Previous / Changed:** unified vector store运维简单，但单embedding/chunk policy难覆盖text/image/audio/video与不同query granularity。
- **Mechanism / State / Flow:** modality/query-aware router选择corpus-specific representation/index/granularity，再交给generator；per-corpus index与routing decision分别版本化。
- **Evidence / Boundary:** 10 benchmarks作者实验支持conditional branch优于shared baseline；不证明universal modalities、index freshness、latency或failure recovery。
- **Trade-off / Coexistence:** router error、fragmented indexes、asset/version growth；单模态/稳定query仍适合unified index。
- **Owner / Decision:** `AGENT-RAG` Ch76；`Refine — Existing Argument Candidate`，Books Frozen。

### ReasonIR

- **Identity / Sources / Coverage:** 24/30，`reasonir-retriever`；arXiv:2504.20595 v1 04-29，data synthesis、contrastive training、BRIGHT/RAG与appendix已读。
- **Problem / Previous / Changed:** lexical/topical retriever便宜，却错过只在推理后显出用处的evidence；BM25 hard negatives可能是假负例。
- **Mechanism / State / Flow:** 生成reasoning queries与plausible-but-unhelpful negatives，adapt Llama3.1-8B bidirectional；batch2048、1000 steps、LR2e-5、GradCache/cross-device negatives；query rewriting作为test-time compute。
- **Evidence / Boundary:** BRIGHT与MMLU/GPQA RAG作者结果支持data/negative contract改变retriever；不证明web freshness或200× claim跨compute成立。
- **Trade-off / Coexistence:** synthetic bias、false negatives、reranker shift与rewriting cost；普通query仍适合dense/BM25。
- **Owner / Decision:** `AGENT-RAG` Ch76；`Refine — Existing Argument Candidate`，Books Frozen。

### Meta Policy Optimization

- **Identity / Sources / Coverage:** 24/30，`meta-policy-optimization-evolving-rm`；arXiv:2504.20157 v1 04-28，formal partition、implementation、four tasks与limitations已读。
- **Problem / Previous / Changed:** fixed rubric/RM稳定且便宜，但policy演进后会变粗并暴露可hack gaps。
- **Mechanism / State / Flow:** 每k batches，meta-RM读取samples/policy outputs/current rubric/scores→分析→rubric refinement/merge；reward prompt成为versioned training state。
- **Evaluation:** Qwen2-1.5B policy、32B/72B RM/MRM，TRL+SGLang；essay 8×A100-80GB、batch64、40 refinements，另BillSum/ethics/math。
- **Evidence / Failure / Coexistence:** 支持tested dynamic rubric发现title/Chinese/degenerate hacks；不证明true reward convergence。风险是nonstationary comparability、judge bias与成本；fixed RM仍适合稳定任务。
- **Owner / Decision:** `TRAIN-RLHF` Ch31，handoff Ch66；`Emerging / Experimental`，Books Frozen。

### WebThinker

- **Identity / Sources / Coverage:** 26/30，`webthinker-deep-research`；arXiv:2504.21776 v1 04-30，workflow、online DPO、benchmarks/ablation已读。
- **Problem / Previous / Changed:** static RAG可控，但不能在reasoning/drafting中持续发现新evidence needs。
- **Mechanism / State / Flow:** think-search-draft + deep web explorer + self-reflection；QwQ-32B、Bing/Crawl4AI，two online-DPO iterations。runtime拥有search result/provenance与workflow state。
- **Evaluation:** GPQA/GAIA/WebWalkerQA/HLE与report generation；max generation81920，Qwen/DeepSeek/GPT judges。live-web drift、provenance completeness与economics未验证。
- **Trade-off / Failure / Coexistence:** search nondeterminism、self-reinforcing sources、judge overlap、extreme token cost；static RAG仍适合bounded corpus/SLO。
- **Owner / Decision:** `AGENT-WORKFLOW` Ch81，handoff Ch76；`Integrate — New Mechanism Candidate`，Books Frozen。

### Self-generated in-context agent examples

- **Identity / Sources / Coverage:** 24/30，`agent-self-generated-trajectory-examples`；arXiv:2505.00234 v1 05-01，method/algorithm、ALFWorld/Wordcraft/InterCode-SQL与appendix已读。
- **Problem / Previous / Changed:** fixed demonstrations简单稳定，但与当前state/task错配并浪费online trial history。
- **Mechanism / State / Flow:** 保存successful trajectories，生成/选择exemplar population并注入后续prompt；external DB拥有provenance/version，policy保持frozen。
- **Evidence / Boundary:** 支持tested sequential tasks中无需weight update的gain；不证明safe transfer或monotonic improvement。
- **Trade-off / Failure / Coexistence:** contamination、prompt growth、success bias与stale environment schema；任务固定时curated demos更可靠。
- **Owner / Decision:** `AGENT-MEMORY` Ch77，handoff Ch79；`Refine — Existing Argument Candidate`，Books Frozen。

### TD-Eval

- **Identity / Sources / Coverage:** 24/30，`td-eval-turn-dialogue`；arXiv:2504.19982 v1 04-28，method、human study、MultiWOZ/tau-Bench、ablation与limits已读。
- **Problem / Previous / Changed:** final dialogue success/string match便宜，却会掩盖中间hallucination、backend mismatch与policy violation。
- **Mechanism / State / Flow:** per-turn judge读取history/query/DB result/response并评分cohesion/backend/policy；full dialogue再pairwise/Elo。EvalSpec必须版本化turn evidence与global outcome。
- **Evaluation:** 10→9 annotators、90 dialogues/490 turns；100 MultiWOZ+165 tau-Bench，GPT-4o judge/user simulator，9 models。
- **Evidence / Failure / Coexistence:** 支持local+global diagnostics优于selected baselines；不证明real-user satisfaction。same-model judge/simulator、position/Elo bias与cost是风险；objective backend tests仍应保留。
- **Owner / Decision:** `PLATFORM-EVALUATION-SYSTEM` Ch66，handoff Ch81；`Refine — Existing Argument Candidate`，Books Frozen。

### Spark scientific idea-generation system

- **Identity / Sources / Coverage:** 21/30，`spark-scientific-idea-generation`；arXiv:2504.20090 v1 04-28，system、judge training/eval与limitations已读。
- **Problem / Previous / Changed:** unguided ideation便宜，却缺literature grounding与critical filter。
- **Mechanism / State / Flow:** recursive arXiv/Scholar retrieval→embedding/FAISS/MMR→evidence snippets→generator→SFT Judge→accept/reject agent；retrieval, idea artifact与judge version分开拥有。
- **Evaluation / Boundary:** 600K transformed OpenReview pairs、temporal split与>10k generated AI ideas；支持modular prototype，不证明scientific novelty/utility或跨域发现。
- **Trade-off / Failure / Coexistence:** one-pass filter、similarity-only retrieval、judge bias、no feedback/strong human validation；human-led workflow仍必要。
- **Owner / Decision:** `AGENT-WORKFLOW` Ch81，handoff Ch76/66；`Emerging / Experimental`，Books Frozen。

### Softpick

- **Identity / Sources / Coverage:** 23/30，`softpick-rectified-softmax`；arXiv:2504.20966 v1 04-30，formulation、training diagnostics、comparisons与limitations已读。
- **Problem / Previous / Changed:** softmax normalized/stable且kernel成熟，但必须分配unit mass，可能产生attention sink/outlier。
- **Mechanism / State / Flow:** subtract threshold并clip的rectified softmax允许zero mass，改变attention state semantics而非只换kernel。
- **Evaluation / Boundary:** diagnostics及340M/1.8B scaling；10k-step ablation无downstream。支持sink/outlier reduction和340M behavior，不证明scale reliability；1.8B underperforms。
- **Trade-off / Coexistence:** inactive heads、lost recall、short-sequence weakness与implementation cost；标准softmax仍是稳健默认。
- **Owner / Decision:** `MODEL-SELF-ATTENTION` Ch14；`Emerging / Experimental`，Books Frozen。

### TesserAct

- **Identity / Sources / Coverage:** 24/30，`tesseract-4d-world-model`；arXiv:2504.20995 v1 04-30，RGB/depth/normal method、generation/planning、losses与appendix已读。
- **Problem / Previous / Changed:** RGB video便宜却不足以提供embodied planning所需3D/temporal geometry。
- **Mechanism / State / Flow:** action/text/robot-conditioned diffusion联合预测RGB-D-N，以consistency/regularization约束temporal geometry，planning消费generated rollout。
- **Evidence / Boundary:** 支持tested extra geometry/loss提升coherence与robot cases；只覆盖单surface/view，不证明完整environment state或real-world causality。
- **Trade-off / Coexistence:** hallucinated depth/normals、view inconsistency与rollout compounding；appearance-only generation仍适合视觉任务。
- **Owner / Decision:** `MULTIMODAL-WORLD-MODELS` Ch25，handoff Ch26；`Integrate — New Mechanism Candidate`，Books Frozen。

### NORA

- **Identity / Sources / Coverage:** 22/30，`nora-vla-3b`；arXiv:2504.19854 v1 04-28，code/checkpoint、architecture/training/eval/appendix已读。
- **Problem / Previous / Changed:** 大VLA/CoT成本高；VLM本身不能输出embodiment action。
- **Mechanism / State / Flow:** Qwen2.5-VL-3B + 2,048 FAST+ action tokens，image+instruction→AR action chunk；Open-X 970k demos，8×H100约4k hours、bf16、batch256、1.1M updates。
- **Evaluation / Boundary:** WidowX 9×10 trials、LIBERO 500 trials；chunk1 vs5。支持compact VLA在tested settings可竞争，不证明general real-time safety；chunking在低频real robot导致crash/affordance failures。
- **Trade-off / Coexistence:** action-token drift、chunk latency/commit与physical failure；分层controller仍适合hard real-time。
- **Owner / Decision:** `MULTIMODAL-EMBODIED-VLA` Ch26；`Refine — Existing Argument Candidate`，Books Frozen。

### Mixture of Sparse Attention

- **Identity / Sources / Coverage:** 22/30，`mosa-expert-choice-sparse-attention`；arXiv:2505.00315 v1 05-01，routing/math/iso-FLOP/limits已读。
- **Problem / Previous / Changed:** dense exact access昂贵，static sparsity pattern固定；希望content-dependent token selection。
- **Mechanism / State / Flow:** each head as expert选择top-k tokens，只在selected subset算QKV/attention；selected-token capacity均衡。
- **Evidence / Boundary:** iso-FLOP non-AR LM experiment支持tested gain；不适用于causal decode，perplexity不总转化downstream，短序列弱。
- **Trade-off / Coexistence:** future-token dependence、starvation、coverage与unoptimized sparse kernel；dense/static window仍可部署。
- **Owner / Decision:** `MODEL-LONG-CONTEXT` Ch22，handoff Ch49；`Emerging / Experimental`，Books Frozen。

### Graph-of-Tokens MoE routing

- **Identity / Sources / Coverage:** 21/30，`graph-tokens-similarity-attention-aware-smoe`；arXiv:2505.00792 v1 05-01，PGM、entropy/routing、LM/ImageNet与appendix已读。
- **Problem / Previous / Changed:** independent per-token router并行简单，但representation稳定时routing仍fluctuate。
- **Mechanism / State / Flow:** sequence similarity或preceding attention作为conditional graph context，影响expert selection。
- **Evidence / Boundary:** medium LM与60M V-MoE、K=2实验支持modest stability/perplexity gain；不证明frontier distributed dispatch benefit。
- **Trade-off / Coexistence:** extra context compute、attention dependency与unmeasured communication；independent router仍适合低overhead。
- **Owner / Decision:** `MODEL-MOE` Ch21，handoff Ch36；`Emerging / Experimental`，Books Frozen。

### Ava agentic video analytics

- **Identity / Sources / Coverage:** 24/30，`ava-agentic-video-analytics`；arXiv:2505.00254 v1 05-01，system、Ava-100、ablation/overhead/limits已读。
- **Problem / Previous / Changed:** hundreds-hour video无法进入VLM context；frame-vector RAG丢event summary/multihop。
- **Mechanism / State / Flow:** 3s chunks→VLM descriptions→semantic merge→event/entity/temporal graph；tri-view retrieval+MCTS+self-consistency。graph/index/search state分别拥有。
- **Evaluation:** Qwen2.5-VL-7B index，2×4090 >5FPS；Ava-100仅8个>10h videos/120 QA；8→16 consistency约2×cost仅+0.9%。
- **Evidence / Failure / Coexistence:** 支持workload-specific event graph+search可行；不证明video truth completeness。lossy descriptions、count errors、fixed search cost与staleness；短video仍适合direct/RAG。
- **Owner / Decision:** `AGENT-RAG` Ch76，handoff Ch23；`Integrate — New Mechanism Candidate`，Books Frozen。

### Transferable black-box VLM attacks

- **Identity / Sources / Coverage:** 25/30，`blackbox-vlm-transfer-attacks`；arXiv:2505.01050 v1 05-02，threat model、loss/data transfer、three tasks与appendix已读。
- **Problem / Previous / Changed:** proprietary VLM opaque，但shared visual representation可能允许black-box transfer。
- **Mechanism / State / Flow:** 对open surrogate ensemble优化l_inf perturbation，结合DropPath/PatchDrop/averaging与visual contrastive loss、preprocess randomization。
- **Evidence / Boundary:** captions/VQA/OCR对GPT-4o/Claude/Gemini snapshot的tested transfer；不证明later APIs、adaptive filters或physical robustness。
- **Trade-off / Coexistence:** semantic judge、visibility constraints、API drift与defense adaptation；white-box/local threat仍需单独处理。
- **Owner / Decision:** `PLATFORM-SECURITY` Ch72，handoff Ch23；`Integrate — New Threat-model Candidate`，Books Frozen。

### PIPA interactive planning evaluation

- **Candidate / Week / Score:** PIPA interactive planning evaluation / 2025-W18 / 23/30；Source Family `pipa-aura-interactive-planning-eval`，arXiv:2505.01592。
- **Event Date / Revision / Sources:** v1于2025-05-02公开，题为《PIPA: A Unified Evaluation Protocol for Diagnosing Interactive Planning Agents》；v2于05-06改题AURA。已读取事件时v1 HTML的Introduction、POMDP taxonomy、四类metric、AgentBench/WebLINX/FlowBench/τ-Bench实例化、三组实验、human study、agent mixing、user-simulator error taxonomy和Appendix；v2仅用于确认same-family revision，不把后发文字倒写为v1事实。
- **Problem / Previous / Changed:** task-completion rate在单一benchmark中合理，却无法说明错误发生在belief/state、action、observation/policy还是final reward；跨环境比较又受metric semantics不同影响。交互式agent进入部分可观测、多轮和主观满意度场景后，单一terminal score不再足以定位系统责任。
- **Mechanism / State / Flow / Implementation:** 用POMDP的`S/A/O/R`及可选policy `P`作为公共坐标；state consistency、action validity、policy adherence由atomic boolean LLM judge实现，task completion保留环境原生verifier。`environment`拥有事实状态与transition，agent trace拥有belief/action，evaluator拥有metric/judge prompt/version，human study只提供preference evidence。控制流为`trace → phase-aligned predicates → per-axis scores → task-native reward → diagnostic comparison`，不能把judge分数解释成真实环境状态。
- **Evaluation Contract:** 对WebLINX、τ-Bench-Retail/Airline的多个closed/open models比较phase metrics与task success；human study检查stage-specific改进与satisfaction关系；agent mixing在τ-Bench-Airline上使用FP8 llama-3.3-70B、qwen2.5-72B、mistral-large，llama-3.3-70B user simulator，每配置5次。硬件、batch/concurrency和SLO未披露；Appendix公开judge prompts、benchmark metric map、human-study instructions与simulator failure cases。
- **Evidence / Boundary / Trade-off:** 证明同一POMDP坐标可揭示terminal success掩盖的阶段差异，并提供受限cross-benchmark diagnosis；不证明LLM judge无偏、atomic metric可跨domain直接比较、user simulator等同真人，或mix-and-match agent在production更优。新增judge cost、prompt/model drift、hidden-state proxy error、metric gaming与component ownership ambiguity；具有强environment verifier的窄任务仍应以原生success为release gate，PIPA只作诊断层。
- **Owner / Adjacent / Decision:** `PLATFORM-EVALUATION-SYSTEM` Ch66，handoff `AGENT-PLANNING` Ch79与`AGENT-WORKFLOW` Ch81；已读目标与相邻章，现有coverage已有“模型能力≠harness/environment opportunity”，本family补充phase-aligned diagnosis。`Refine — Existing Argument Candidate / Books Frozen`；open question是v1→AURA哪些metric identity变化值得在未来revision audit中单列。

### Always Tell Me The Odds

- **Identity / Sources / Coverage:** 23/30，`conditional-probability-calibration-2505.01595`；v1 05-02，conditional probability task、elicitation/eval/appendix已读。
- **Problem / Previous / Changed:** unconditional confidence不能表达显式evidence/scenario条件；fluency不是calibration。
- **Mechanism / State / Flow:** elicited model output给event-pair conditional probability，以proper scoring/calibration评估；它不是atomic claims概率相乘。
- **Evidence / Boundary:** 支持benchmark内model calibration差异；不证明open-world epistemic uncertainty或causality。
- **Trade-off / Failure / Coexistence:** verbal anchoring、base-rate omission、correlated claims与leakage；retrieval/verifier evidence仍必要。
- **Owner / Decision:** `PLATFORM-EVALUATION-SYSTEM` Ch66；`Refine — Existing Argument Candidate`，Books Frozen。

### UQLM uncertainty-quantification suite

- **Identity / coverage:** Source Family `UQLM-UQ-SUITE`，research paper `2504.19254` v1 2025-04-27 / event-time latest v2 2025-04-30，28/30；PyPI alpha/beta与stable v0.1.0（05-03～05-06）是same-week artifact nodes，v0.1.8和`2507.06196` package descriptor是W27/W28 forward evidence。已读event-time paper全部scorer公式、ensemble optimization、六benchmark setup、Filtered Accuracy/ROC-AUC/F1、discussion、limitations、code appendix，并联读official repo/release与package descriptor。Owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff monitoring/logging/trace。
- **Problem / mechanism / ownership:** ground-truth、source verifier与人工审查在有reference或高风险时最可靠，但generation-time常没有即时答案，规模化逐条复核不可行。UQLM把多种proxy映射到`[0,1]` response score：black-box对同prompt多次采样，计算exact/embedding/NLI consistency与semantic entropy；white-box使用length-normalized joint/minimum token probability；self/external judge映射三分类。非负和为1的linear ensemble按ROC-AUC调weights再按F1调threshold，或联合优化。generator拥有responses/sampling/logprobs，scorer拥有proxy model/prompt/version，ensemble拥有components/weights/objective/tuning set，calibration/risk policy才拥有`answer/filter/review/abstain`，external evidence/verifier拥有correctness authority。
- **Implementation / evaluation contract:** `prompt → original + m candidates/logprobs → scorer features → normalized proxies → ensemble → threshold/policy → delayed labels/recalibration`。研究用UQLM v0.1.0、GSM8K/SVAMP/CSQA/AI2-ARC/PopQA/NQ-Open各1000 questions，GPT-3.5-16k-turbo与Gemini-1.0-pro各生成original+15 candidates；只有Gemini提供white-box logprobs。ROC-AUC/F1用5-fold CV，Filtered Accuracy扫threshold0～0.9。结果支持这些closed-book QA与旧API模型下proxy可排序部分错误、slice-tuned ensemble通常减少single-sensor脆弱性；不证明`[0,1]`是calibrated `P(correct)`、stable consensus等于truth、v0.1.8与v0.1.0性能等价、open-world/RAG/long-form factuality或production latency/cost。
- **Trade-off / threats / coexistence:** black-box provider-agnostic但需要多次generation与NLI/embedding compute；white-box便宜但依赖logprob/tokenization；judge灵活却共享generator bias；ensemble增加tuning label、相关signal double-count、drift monitoring与rollback。缺hardware、precision、length、batch/concurrency、SLO、Brier/ECE及component-correlation/weight-stability。可形式化domain仍应使用fixed verifier，高风险domain仍需external evidence与human review。Ch66已明确semantic entropy、`P(True)`、judge和retrieval score只是features，必须按deployment slice校准并用risk-coverage/abstention治理，故`No Change — Already Covered / Versioned Toolkit Case`；Historical Books Gate关闭。

### VideoHallu

- **Identity / Sources / Coverage:** 22/30，`videohallu-synthetic-video-reasoning`；arXiv:2505.01481 v1 05-02，dataset、evaluation、SFT/claimed GRPO、training与ablation已读。
- **Problem / Previous / Changed:** text priors会让VLM忽略impossible synthetic dynamics。
- **Mechanism / Evaluation:** abnormal videos/QA；Qwen2.5-VL-7B与LLaVA-OneVision混合800 synthetic+2k real QA，15 frames、LR1e-6、1 epoch、8×A100；reward为平均ROUGE overlap。
- **Evidence / Boundary:** 支持tested models接近chance且post-training改善该benchmark；不证明physical world model或GRPO普适。
- **Dispute / Failure:** displayed“GRPO”equation更接近pairwise preference/DPO-style objective，算法label与reward contract冲突；synthetic artifact、小数据与ROUGE mismatch。
- **Owner / Decision:** `PLATFORM-EVALUATION-SYSTEM` Ch66，handoff Ch25；`Disputed / Experimental`，不进入Books。

### Towards Safer Pretraining / HarmFormer

- **Identity / Sources / Coverage:** 22/30，`safer-pretraining-harmformer-havoc`；arXiv:2505.02009 v1 05-04，taxonomy/data/model/eval/limits已读。
- **Problem / Previous / Changed:** binary short-text filters便宜，但误删topical discussion并漏contextual harmful intent。
- **Mechanism / State / Flow:** Safe/Topical/Toxic×5 taxonomy，GPT-4o labels，3M sampled pages→258k balanced labels；Longformer multitask 5 heads、1024 tokens、batch16、LR2e-5、3 epochs。
- **Evidence / Boundary:** 支持tested taxonomy/filter优于selected baselines；不证明过滤后pretraining safety/capability提升。
- **Trade-off / Failure / Coexistence:** model/prompt transfer poor、false positive、cultural taxonomy bias与prevalence sampling；simple filters仍适合clear-cut policy。
- **Owner / Decision:** `TRAIN-DATA` Ch27，handoff Ch72/66；`Refine — Existing Argument Candidate`，Books Frozen。

### Ray 2.45.0

- **Identity / Sources / Coverage:** 21/30，`ray-2.45-runtime-release`；official release 04-29全文核验。
- **Mechanism / State / Flow:** object-store fallback、compiled-graph shared-memory/collectives、dashboard subprocess、Data lineage/metadata/memory autotune、Serve cancellation/accelerator fixes；各自拥有不同runtime state，不是单一机制。
- **Evidence / Boundary:** release证明version surface；局部>5× claim缺完整workload，不作通用performance结论。
- **Trade-off / Failure / Coexistence:** version skew、cancellation leak、shared-memory lifetime、observability fragmentation；旧stable Ray仍可继续。
- **Owner / Decision:** `PLATFORM-FOUNDATIONS` Ch57，handoff Ch36；`Weekly Only — Version/Product Fact`。

### ARTIST / Agentic Reasoning and Tool Integration via RL

- **Candidate / Week / Score:** ARTIST / 2025-W18 / 27/30；Source Family `artist-agentic-tool-rl`，arXiv:2505.01441 v1 2025-04-28，论文正文与Appendix C实现细节已读；event-time代码承诺“will be released soon”，故artifact状态不计为已验证。
- **Problem / Previous / Changed:** prompt/SFT教固定tool syntax在静态任务中合理，但面对多步反馈、失败返回与tool-choice分支时，人工trajectory覆盖不足。约束从“会调用工具”变为“在rollout中学习何时调用、如何根据结果修正”。
- **Mechanism / State / Flow:** reasoning、tool query、deterministic tool output和answer交错为trajectory；GRPO以group-relative outcome训练model-generated tokens，明确mask tool-output tokens，reward由answer、format和successful-execution fraction组成。policy拥有proposal，environment/tool拥有execution result，rollout runtime拥有transcript/mask/reward provenance，trainer拥有group baseline与update。
- **Implementation / Evaluation:** Qwen2.5-7B/14B-Instruct；math与BFCL v3/τ-Bench两支，Pass@1同时检查final response与environment state；math batch 8、6 rollouts、8k max tokens、LR1e-6，4×A100-80GB约20h；function calling为7B、每GPU batch 8、3 training GPUs、grad accumulation 4、8 rollouts、4×A100-80GB约34h。与base、prompt+tools、ToRA/NuminaMath-TIR及frontier models比较；未提供独立artifact复现和完整failure ablation。
- **Evidence / Trade-off / Coexistence:** 支持tested tasks中outcome RL可学习tool-use policy且mask deterministic outputs是必要ownership边界；不证明任意tool/environment泛化或安全可执行。新增rollout cost、reward hacking、tool side effect、sandbox、stale result与credit assignment；deterministic workflow或高风险动作仍应保留显式policy/verifier。Owner `TRAIN-GRPO` Ch33，handoff `AGENT-TOOL` Ch78与Ch81；`Integrate — New Mechanism Candidate / Books Frozen`。

### R&B Domain Regrouping and Data Mixture Balancing

- **Candidate / Week / Score:** R&B / 2025-W18 / 27/30；Source Family `rb-gradient-domain-mixture`，arXiv:2505.00358 v1 2025-05-01；全文、公式、算法、compute appendix、实验配置和ablation已读，artifact未披露。
- **Problem / Previous / Changed:** 人工domain labels与固定比例在domain稳定时便宜可解释，但label未必对应gradient-compatible skills；逐domain holdout evaluation随domain数增长又昂贵。数据混合要同时解决domain ownership和sampling control。
- **Mechanism / State / Flow:** 先用embedding与gradient-informed criterion regroup examples，再在训练round累积final-layer gradient，构造cluster similarity matrix `G`，结合evaluation proportions后softmax更新mixture。dataset/clusterer拥有membership version，trainer拥有gradient sample，mixture controller拥有probability simplex与update cadence；数据流为`examples → regrouped domains → sampled batches → gradients/G → next-round proportions`。
- **Evaluation / Boundary:** Super-NaturalInstructions train/test、Dolly-15k及额外modalities，与stratified、Skill-It、Aioli、DGA比较；论文给出`Tm²/(6D_t)`相对overhead模型并报告相对两数量级开销下降。实验主要为小/中规模受控训练，硬件、precision、production data drift/SLO未完整披露；结果不证明对trillion-token预训练或非平稳语料普适。
- **Trade-off / Coexistence:** regrouping降低错误taxonomy约束，却引入cluster identity drift、gradient sampling noise、final-layer proxy偏差与mixture oscillation；监管/业务domain仍可能必须保留人工边界。Owner `TRAIN-DATA` Ch27，handoff Ch28；`Integrate — New Mechanism Candidate / Books Frozen`。

### SWE-smith

- **Candidate / Week / Score:** SWE-smith / 2025-W18 / 29/30；Source Family `swe-smith-executable-training-data`，arXiv:2504.21798 v1 2025-04-30；论文、Appendix实验/失败分析与official `SWE-bench/SWE-smith` repository已读。
- **Problem / Previous / Changed:** 从真实PR提取SWE任务保真但人力、环境存储和repo覆盖限制规模；纯文本合成便宜却缺可执行correctness。约束转为可批量生成“确实破坏测试且可复现”的任务、环境与trajectory。
- **Mechanism / State / Flow:** 对Python repo构建Docker environment，使用combine、procedural AST mutation、LM modify/rewrite与PR mirror注入bug；只保留fail-to-pass tests成立的实例，再生成issue text与expert trajectories。repository commit、image、test oracle、bug patch、issue和trajectory必须共同构成dataset identity；pipeline而非LLM judge拥有accept/reject authority。
- **Evaluation Contract:** 50,137 instances/128 repos，五种generator yield/cost与issue-type/repository ablation；以5,016 trajectories对Qwen2.5-Coder 7B/32B做full-parameter RFT，max context 32,768、LR5e-5、最多3 epochs、2～8×H100-80GB，在SWE-bench Verified评估32B模型40.2% Pass@1。artifact提供code、tasks、trajectories、models和environment ledger；论文承认Python-centric且只用fine-tuning展示数据效用。
- **Evidence / Trade-off / Coexistence:** 证明executable mutation+test oracle可把SWE training data扩到tested规模，并把environment纳入artifact；不证明synthetic bug分布等同真实issues、40.2%只由规模导致，或能跨语言泛化。新增container supply-chain、test inadequacy、mutation bias、repo license/commit drift与高存储成本；高质量真实PR仍适合作校准集。Owner `TRAIN-DATA` Ch27，handoff `AGENT-WORKFLOW` Ch81与`PLATFORM-EVALUATION-SYSTEM` Ch66；`Integrate — New Mechanism Candidate / Books Frozen`。

### Who&When Multi-Agent Failure Attribution

- **Candidate / Week / Score:** Who&When / 2025-W18 / 27/30；Source Family `whowhen-multi-agent-failure-attribution`，arXiv:2505.00212 v1 2025-04-30；正文、算法、annotation、cost/sensitivity、Appendix已读。
- **Problem / Previous / Changed:** overall task failure与人工读log能发现问题，但不能规模化回答哪个agent、哪一步造成decisive error；多agent共享状态和长trace使“最后报错者=根因”不成立。
- **Mechanism / State / Flow:** 三位expert多轮标注responsible agent、decisive step和rationale；用all-at-once、step-by-step与binary-search LLM judge定位。trace store拥有immutable actions/tool results，annotation ledger拥有human consensus，judge拥有model/prompt/context window，统计层才聚合component blame；不得用预测blame自动执行rollback。
- **Evaluation Contract:** 127个algorithm-generated/human-crafted systems、184 annotated failure tasks，来自GAIA/AssistantBench和Magnetic-One；主judge GPT-4o，并测Llama/Qwen/o1/R1。agent-level与step-level accuracy、log-length sensitivity、±1～5 tolerance和token cost联合评估；长trace下exact step accuracy趋近0，hybrid改善两指标但token最高（149,177）。硬件、latency/SLO与inter-annotator系数未披露。
- **Evidence / Trade-off / Coexistence:** 证明failure attribution是独立observability/evaluation问题，且global context、local precision与cost互相冲突；不证明LLM judge能可靠确定causality或适用于arbitrary teams。新增judge bias、shared-cause遗漏、single-blame simplification、privacy与trace retention成本；small deterministic workflows仍适合rule-based provenance。Owner `PLATFORM-OBSERVABILITY` Ch67，handoff `AGENT-MULTI-AGENT` Ch82；`Integrate — New Mechanism Candidate / Books Frozen`。

### Practical Efficiency of Muon for Pretraining

- **Candidate / Week / Score:** Practical Efficiency of Muon / 2025-W18 / 29/30；Source Family `muon-pretraining-practical-efficiency`，arXiv:2505.02222 v1 2025-05-04；全文、Newton-Schulz实现、critical-batch、telescoping tuning、muP与Appendix已读；in-house JAX implementation正文可定位，独立repository未披露。
- **Problem / Previous / Changed:** AdamW稳定且生态成熟，但只比较step loss会忽略wall-clock、FLOPs、batch saturation和optimizer tuning cost；二阶近似若需全规模grid search则收益会被实验成本吞噬。
- **Mechanism / State / Flow:** Muon对除embedding/norm外的matrix gradient做momentum后以Newton-Schulz近似orthogonalization，并用`0.2√n`尺度；embedding/norm继续Adam。optimizer state按parameter type分治；telescoping sweep从100M逐尺度缩小mesh，假设最优hyperparameter随width平滑漂移，muP负责跨width parameterization。
- **Evaluation Contract:** Gemma-3-like decoder，100M～4B，DCLM与Python+DCLM，10B～50B token；TPU v5p约50% MFU，最大3.7B run为128 chips×100h/160B tokens；比较AdamW的compute-time Pareto、critical batch、architecture/data/model-size ablation。论文以fresh-batch training loss近似generalization，且最大规模结果不等同held-out downstream quality。
- **Evidence / Trade-off / Coexistence:** 支持tested scale下Muon在compute/time平面扩展AdamW frontier并降低大模型tuning开销；不证明所有架构、optimizer-state sharding或非TPU实现同样获益。新增matrix-shape分支、orthogonalization kernel/communication、precision稳定性、parameter classification与tuning-assumption风险；小模型、成熟AdamW stack或非matrix参数仍可优先AdamW。Owner `TRAIN-PRETRAINING` Ch28，handoff Ch36/41；`Refine — Existing Optimizer Branch Candidate / Books Frozen`。

### Low-score Closures

- **Taming the Titans survey / 19/30 / `taming-titans-survey`:** arXiv:2504.19720 v1 04-28；secondary inference-serving source map，无新primary mechanism。
- **A Survey on LLM-based Human-Agent Systems / 19/30 / `human-agent-systems-survey`:** arXiv:2505.00753 v1 05-01；taxonomy，不提供新executable orchestration/eval evidence。
- **Parameter-Efficient Transformer Embeddings / 18/30 / `parameter-efficient-transformer-embeddings`:** arXiv:2505.02266 v1 05-04；仅SNLI/MNLI/STS-B proof-of-concept，无scale/generation contract。
- **Controllable Weather Synthesis and Removal / 18/30 / `weather-diffusion-control`:** arXiv:2505.00704 v1 05-01；窄域generation case，不改变通用world/generation contract。
- **Retrieval-augmented ICL for Multimodal Disease Classification / 18/30 / `multimodal-disease-raicl`:** arXiv:2505.02087 v1 05-04；domain-specific evidence，clinical generalization不足。
- **A Survey on Inference Engines for Large Language Models / 19/30 / `llm-inference-engine-survey-2505.01658`:** arXiv:2505.01658 v1 05-03；25个engine的feature/maturity/commercial matrix属于secondary synthesis，snapshot会快速漂移，未提出新的runtime mechanism或可复现实验，保留作discovery map而不承担机制结论。
- **Low-Precision Training of Large Language Models / 19/30 / `low-precision-training-survey-2505.01043`:** arXiv:2505.01043 v1 05-02；系统整理fixed/integer/floating/custom format、QAT和communication compression，但证据来自被综述工作，不能替代各primary paper的数值稳定性与hardware contract，故低分闭合。

### Pending、Blocked 与 Cross-week Ledger

- **Review Pending / Unscored identity:** 0 / 0。PIPA v1与七个W19 spillback均已完成事件时全文、六维评分、owner和相邻章节审读；UQLM也已按W18 owner闭合，不再列入W28 pending。
- **Blocked / Disputed:** 0 / 1。VideoHallu为source-complete terminal dispute：论文展示的目标函数、average-ROUGE reward与“GRPO”算法标签不一致；需要event-time code、训练config或作者勘误才能解除，但它不是可读材料pending。
- **Discovery limitation:** 固定机构、arXiv owner与后续周spillback已重放；Scholar/OpenAlex/DBLP的历史query result无法以immutable export复现，因此本周Candidate Evidence Gate可通过，但年度Archive Completion Gate仍为Conditional Open。
- **Spillback W17:** Skywork-R1V2、BitNet-v2、Sparse Frontier、Kimi-Audio、MMInference、RAGEN与RoboVerse。
- **Spillback W16/W15:** vLLM v0.8.4与Transformers v4.51.3归W16；SGLang v0.4.5归W15。
- **Forward related evidence:** Qwen3 report与MiMo report归W20；UniversalRAG v2是same-family revision；Llama-Nemotron May report是W18 evidence node。

## Candidate Evidence Gate

- ISO window：Pass。
- Scored owner identities：43；unscored spillback identities：0；retained 20+：36（18 high、18 medium）；strict Full Source Review：36/36；Review Pending：0。
- Low-score source/date/rejection：7/7；Blocked：0；terminal Disputed：1（VideoHallu，全文完成但机制标签冲突）。
- Candidate Evidence Gate：`Passed`；Discovery/Archive Gate：`Conditional Open — immutable cross-index export unavailable`；Historical Books Gate：Closed。

## Evidence Level

- 官方 Blog / Release 只证明公开事实；未公开实现保持未知。
- arXiv v1 默认 Status: Experimental；作者实验不等于独立复现。
- 跨来源连接是本项目推断，以 Evolution Relationship 标记。

## Cross-Week Deduplication

- 同一技术后续 revision 与工程集成回链首次公开周。
- 新版本不覆盖旧方案；年度索引记录 old constraint → new mechanism → new failure mode。

## Knowledge Tree Position

- Model / Training：Softpick、MoSA、Graph-of-Tokens、Phi family、DeepSeek-Prover、One-shot RLVR、Llama-Nemotron、R&B与Muon → Part II/IV。
- Multimodal：TesserAct、NORA、VLM attacks与VideoHallu → Part III，并分别回到world-state、physical action、security与evaluation owner。
- Inference / Platform：Qwen3 mode/budget → Ch56；GPT incident、Leaderboard、Odds、TD-Eval与PIPA → Ch66；Ray → Ch57。
- Agent：Mem0/self-generated trajectories → Ch77；UniversalRAG/ReasonIR/Ava → Ch76；ARTIST、SWE-smith与Who&When分别连接tool-training、executable workflow data和multi-agent trace attribution。

## Recommended Action

- 36/36个20+ owner完成strict Full Source Review，7/7个低分完成source/date/rejection闭合；Review Pending与Blocked均为0。
- VideoHallu保持Disputed，不能因作者使用“GRPO”标签就写入training机制结论。
- 所有Books disposition保持Frozen/provisional；本轮只恢复Weekly证据。

## Event-Date Daily Decision

历史回填不创建 Daily；事件与证据边界直接保留在本 Weekly。

## Books Integration Decision

Historical Books Gate关闭。W18 Candidate Evidence Gate已闭合；PIPA v1与所有spillback均完成。
尚未闭合的是年度Archive Completion Gate：VideoHallu仍为terminal Disputed，且跨索引历史query缺
immutable export。本轮只修复Weekly，不修改Books。


## Ignored Noise

- 忽略旧内容重发、二手转述、缺条件 benchmark 与纯可用性更新。
- discovery 排名和引用量不替代 novelty、reliability 或 longevity。

## Repository Changes

- 将旧1项baseline最终扩展并校准为43个已评分owner identities：36项20+全部strict complete、
  7项低分全部闭合；PIPA v1和七项canonical spillback均完成，不再存在unscored identity。
- Candidate Evidence Gate通过；VideoHallu作为terminal Disputed保留，跨索引immutable export使年度Archive Gate保持Open；Historical Books Gate关闭。本轮只修改W18 Weekly。

## Open Questions

- PIPA 2025-05-02 v1已与05-06 AURA revision隔离；后续只需审计revision具体metric identity变化，不影响W18 gate。
- VideoHallu需要2025-05-02 event-time code、训练config或作者勘误核对其所谓GRPO objective；未解决前保持Disputed且禁止进入Books。
- Qwen3/MiMo的W20 technical report只作forward related evidence；Arena variant de-anonymization仍有采样不确定性。

## Sources

- Qwen3 — https://qwenlm.github.io/blog/qwen3/（First Public: 2025-04-29；Accessed: 2026-07-31）
- Qwen3 Technical Report — https://arxiv.org/abs/2505.09388（First Public: 2025-05-14；v1；Accessed: 2026-07-31）
- Qwen3 repository — https://github.com/QwenLM/Qwen3（Release family opened: 2025-04-29；Accessed: 2026-07-31）
- Qwen3-235B-A22B model card — https://huggingface.co/Qwen/Qwen3-235B-A22B（Accessed: 2026-07-31）
- GPT-4o sycophancy rollback — https://openai.com/index/sycophancy-in-gpt-4o/（First Public: 2025-04-29；Full Source Review Complete；Accessed: 2026-08-22）
- GPT-4o sycophancy postmortem — https://openai.com/index/expanding-on-sycophancy/（First Public: 2025-05-02；Full Source Review Complete；Accessed: 2026-08-22）
- Phi-4-reasoning — https://arxiv.org/abs/2504.21318（v1: 2025-04-30；Full Source Review Complete；Accessed: 2026-08-22）
- Phi-4-Mini-Reasoning — https://arxiv.org/abs/2504.21233（v1: 2025-04-30；Full Source Review Complete；Accessed: 2026-08-22）
- DeepSeek-Prover-V2 — https://arxiv.org/abs/2504.21801（v1: 2025-04-30；Full Source Review Complete；Accessed: 2026-08-22）
- DeepSeek-Prover-V2 artifact — https://github.com/deepseek-ai/DeepSeek-Prover-V2（Accessed: 2026-08-22）
- MiMo-7B — https://github.com/XiaomiMiMo/MiMo（Release: 2025-04-30；Full Source Review Complete；Accessed: 2026-08-22）
- Amazon Nova Premier — https://aws.amazon.com/blogs/aws/amazon-nova-premier-our-most-capable-model-for-complex-tasks-and-teacher-for-model-distillation/（First Public: 2025-04-30；Full Source Review Complete；Accessed: 2026-08-22）
- Llama-Nemotron technical report — https://arxiv.org/abs/2505.00949（v1: 2025-05-02；Full Source Review Complete；Accessed: 2026-08-22）
- Mem0 — https://arxiv.org/abs/2504.19413（v1: 2025-04-28；Full Source Review Complete；Accessed: 2026-08-22）
- Mem0 project — https://mem0.ai/research（Accessed: 2026-08-22）
- One-shot RLVR — https://arxiv.org/abs/2504.20571（v1: 2025-04-29；Full Source Review Complete；Accessed: 2026-08-22）
- The Leaderboard Illusion — https://arxiv.org/abs/2504.20879（v1: 2025-04-29；Full Source Review Complete；Accessed: 2026-08-22）
- UniversalRAG — https://arxiv.org/abs/2504.20734（v1: 2025-04-29；Full Source Review Complete；Accessed: 2026-08-22）
- ReasonIR — https://arxiv.org/abs/2504.20595（v1: 2025-04-29；Full Source Review Complete；Accessed: 2026-08-22）
- Meta Policy Optimization — https://arxiv.org/abs/2504.20157（v1: 2025-04-28；Full Source Review Complete；Accessed: 2026-08-22）
- WebThinker — https://arxiv.org/abs/2504.21776（v1: 2025-04-30；Full Source Review Complete；Accessed: 2026-08-22）
- Softpick — https://arxiv.org/abs/2504.20966（v1: 2025-04-30；Full Source Review Complete；Accessed: 2026-08-22）
- TesserAct — https://arxiv.org/abs/2504.20995（v1: 2025-04-30；Full Source Review Complete；Accessed: 2026-08-22）
- NORA — https://arxiv.org/abs/2504.19854（v1: 2025-04-28；Full Source Review Complete；Accessed: 2026-08-22）
- Mixture of Sparse Attention — https://arxiv.org/abs/2505.00315（v1: 2025-05-01；Full Source Review Complete；Accessed: 2026-08-22）
- Graph-of-Tokens MoE routing — https://arxiv.org/abs/2505.00792（v1: 2025-05-01；Full Source Review Complete；Accessed: 2026-08-22）
- Ava agentic video analytics — https://arxiv.org/abs/2505.00254（v1: 2025-05-01；Full Source Review Complete；Accessed: 2026-08-22）
- Ava artifact — https://github.com/I-ESC/Project-Ava（Accessed: 2026-08-22）
- Transferable black-box VLM attacks — https://arxiv.org/abs/2505.01050（v1: 2025-05-02；Full Source Review Complete；Accessed: 2026-08-22）
- Self-generated in-context agent examples — https://arxiv.org/abs/2505.00234（v1: 2025-05-01；Full Source Review Complete；Accessed: 2026-08-22）
- PIPA interactive planning evaluation — https://arxiv.org/html/2505.01592v1（v1: 2025-05-02；Full Source Review Complete；v2/AURA: 2025-05-06 same-family revision；Accessed: 2026-08-24）
- Always Tell Me The Odds — https://arxiv.org/abs/2505.01595（v1: 2025-05-02；Full Source Review Complete；Accessed: 2026-08-22）
- UQLM research paper — https://arxiv.org/abs/2504.19254（v1: 2025-04-27；v2: 2025-04-30；Full Source Review Complete；Accessed: 2026-08-22）
- UQLM official repository — https://github.com/cvs-health/uqlm
- UQLM v0.1.0 — https://github.com/cvs-health/uqlm/releases/tag/v0.1.0
- UQLM formal package descriptor — https://arxiv.org/abs/2507.06196（Forward related evidence；W28 no duplicate score）
- VideoHallu — https://arxiv.org/abs/2505.01481（v1: 2025-05-02；Disputed；Accessed: 2026-08-22）
- Towards Safer Pretraining / HarmFormer — https://arxiv.org/abs/2505.02009（v1: 2025-05-04；Full Source Review Complete；Accessed: 2026-08-22）
- Ray 2.45.0 — https://github.com/ray-project/ray/releases/tag/ray-2.45.0（First Public: 2025-04-29；Full Source Review Complete；Accessed: 2026-08-22）
- TD-Eval — https://arxiv.org/abs/2504.19982（v1: 2025-04-28；Full Source Review Complete；Accessed: 2026-08-22）
- Spark scientific idea-generation system — https://arxiv.org/abs/2504.20090（v1: 2025-04-28；Full Source Review Complete；Accessed: 2026-08-22）
- Taming the Titans survey — https://arxiv.org/abs/2504.19720（v1: 2025-04-28；Low-score Closure；Accessed: 2026-08-22）
- A Survey on LLM-based Human-Agent Systems — https://arxiv.org/abs/2505.00753（v1: 2025-05-01；Low-score Closure；Accessed: 2026-08-22）
- Parameter-Efficient Transformer Embeddings — https://arxiv.org/abs/2505.02266（v1: 2025-05-04；Low-score Closure；Accessed: 2026-08-22）
- Controllable Weather Synthesis and Removal — https://arxiv.org/abs/2505.00704（v1: 2025-05-01；Low-score Closure；Accessed: 2026-08-22）
- Retrieval-augmented ICL for Multimodal Disease Classification — https://arxiv.org/abs/2505.02087（v1: 2025-05-04；Low-score Closure；Accessed: 2026-08-22）
- A Survey on Inference Engines for Large Language Models — https://arxiv.org/abs/2505.01658（v1: 2025-05-03；Low-score Closure；Accessed: 2026-08-24）
- Inference-engine survey tracking repository — https://github.com/sihyeong/Awesome-LLM-Inference-Engine（Related evolving artifact；Accessed: 2026-08-24）
- ARTIST / Agentic Reasoning and Tool Integration via RL — https://arxiv.org/html/2505.01441v1（v1: 2025-04-28；Full Source Review Complete；event-time code Not Released；Accessed: 2026-08-24）
- R&B Domain Regrouping and Data Mixture Balancing — https://arxiv.org/html/2505.00358v1（v1: 2025-05-01；Full Source Review Complete；Accessed: 2026-08-24）
- SWE-smith — https://arxiv.org/html/2504.21798v1（v1: 2025-04-30；Full Source Review Complete；Accessed: 2026-08-24）
- SWE-smith official artifact — https://github.com/SWE-bench/SWE-smith（Related primary artifact；Accessed: 2026-08-24）
- Who&When Multi-Agent Failure Attribution — https://arxiv.org/html/2505.00212v1（v1: 2025-04-30；Full Source Review Complete；Accessed: 2026-08-24）
- Low-Precision Training of Large Language Models — https://arxiv.org/html/2505.01043v1（v1: 2025-05-02；Low-score Closure；Accessed: 2026-08-24）
- Practical Efficiency of Muon for Pretraining — https://arxiv.org/html/2505.02222v1（v1: 2025-05-04；Full Source Review Complete；Accessed: 2026-08-24）
- Qwen3 Technical Report — https://arxiv.org/abs/2505.09388（v1: 2025-05-14；forward W20 related evidence；Accessed: 2026-08-22）
- MiMo Technical Report — https://arxiv.org/abs/2505.07608（v1: 2025-05-12；forward W20 related evidence；Accessed: 2026-08-22）
