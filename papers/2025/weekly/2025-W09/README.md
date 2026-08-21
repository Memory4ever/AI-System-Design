# AI Research Weekly — 2025-W09

> Coverage Window: 2025-02-24～2025-03-02
> Research Mode: Retrospective Backfill
> Audit Status: Candidate Evidence Gate Passed with Declared Gaps — 100 Full Source Reviews；3 low-score verifications；0 ordinary pending
> Accessed: 2026-08-20
> Backfilled: 2026-07-31

## Executive Summary

旧版周报只保留 Claude 3.7 Sonnet / Claude Code，并错误写成“论文与工程无候选”。本轮重新发现已确认：
W09 至少还包含 SWE-RL、SpargeAttn、Kanana、Drop-Upcycling、OmniAlign-V、WebGames、multi-draft
speculative decoding、MXFP4 training 等独立 Source Family；AI co-scientist 的 2 月 26 日论文是 W08
官方 Blog family 的 revision/evidence node，不重复计为新事件。

本轮已完成 Claude 3.7、GPT-4.5、DeepSeek Open Source Week、2月27～28日 academic/cross-index/HF Newsletter owner、
JAX 0.5.1、Ray 2.43.0等全部已发现可访问family的审计。当前100个`20+` owner event拥有非模板化Full Source Review，
3个低分event完成identity/date/score/rejection，ordinary `Review Pending = 0`。Google Scholar/OpenAlex/DBLP精确日期导出
以及Kubeflow manifests、Megatron-LM、llama.cpp历史release time slice仍保留为显式Discovery/Release-feed Gap；
它们不再阻塞forward cursor，但年度Archive Completion Gate保持Open。W09 Candidate Evidence Gate通过，本轮仍不进入Books Integration。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；本轮访问日期为 2026-08-20。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。
- Hugging Face Daily Papers 只用于 discovery；必须回到 arXiv v1 的 `Published on` 日期归属 owner Week，
  不能把 community submit/recommendation 日期当作论文首发日期。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：Claude 3.7 Sonnet and Claude Code（2025-02-24）、GPT-4.5 research preview与System Card（2025-02-27）。
- `Full Source Review Complete`（fixed-org rescan）：Wan2.1 inference code/weights（2025-02-25；technical report 3月21日same-family evidence）。
- `Full Source Review Complete`（fixed-org rescan）：Ai2 olmOCR model/data/pipeline（2025-02-25；paper v1同日）。
- `Full Source Review Complete`（fixed-org rescan）：Microsoft Phi-4-mini + Phi-4-multimodal launch family（2025-02-26；report v1 3月3日）。
- `Full Source Review Complete`（fixed-org rescan）：Cohere Command R7B Arabic open-weights release（2025-02-27；report v1 3月18日）。
- `Spillback to W08`：SmolVLM2 Blog为2025-02-20，不因本轮发现日期放入W09。
- `Full Source Review Complete`（DeepSeek Open Source Week）：FlashMLA v1（2月24日）、DeepEP V1（2月25日）、DeepGEMM v1（2月26日）。
- `Full Source Review Complete`（DeepSeek Open Source Week Day 4）：DualPipe code artifact（2月27日；mechanism paper v1为2024-12-27 pre-window）。
- `Full Source Review Complete`（DeepSeek Open Source Week Day 4）：EPLB initial artifact（2月27日；initial commit 2月26日）。
- `Full Source Review Complete`（DeepSeek Open Source Week Day 5）：3FS open-source artifact（2月28日）。
- `Full Source Review Complete`（DeepSeek Open Source Week Day 5）：smallpond open-source artifact（2月28日；initial commit 2月27日）。
- `Full Source Review Complete`（DeepSeek Open Source Week Day 6）：V3/R1 online inference-system overview（3月1日；24-hour production contract）。
  这些是独立kernel、collective、parallelism、storage/data与serving Source Family，不能压成一条厂商新闻或在未全文审计前评分。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

- `Full Source Review Complete`：SWE-RL、SpargeAttn、Drop-Upcycling、Kanana、Towards Optimal Multi-draft
  Speculative Decoding、WebGames、OmniAlign-V、Language Models' Factuality Depends on the Language of Inquiry、Rank1。
- `Full Source Review Complete`（本批新增）：DeltaBench / Long-CoT Error Detection、Agentic Reward Modeling。
- `Full Source Review Complete`（PDF recovery）：VEM、CritiQ。
- `Full Source Review Complete`（本批新增）：Training LLMs with MXFP4。
- `Full Source Review Complete`（本批新增）：Self-Training Elicits Concise Reasoning、Granite Embedding Models。
- `Spillback to W08`：LUME v1 2025-02-20；W09 的2月27日是v3，不重复评分。
- `Full Source Review Complete`（本批新增）：WorldModelBench。
- `Full Source Review Complete`（本批新增）：LongRePS。
- `Full Source Review Complete`（本批新增）：PersonaBench、Safety Tax。
- `Full Source Review Complete`（本批新增）：ARIES、GUI Pivot。
- `Full Source Review Complete`（本批新增）：RaPID、Babel、LADDER、Diffusion Planner。
- `Full Source Review Complete`（HF replay新增）：Make LoRA Great Again / GOAT、Stable-SPAM。
- `Full Source Review Complete`（HF replay新增）：VideoGrain、DICEPTION。
- `Full Source Review Complete`（HF replay新增）：Mobile-Agent-V v1。
- `Full Source Review Complete`（HF replay新增）：Thus Spake Long-Context LLM survey v1。
- `Full Source Review Complete`（HF replay新增）：KV-Edit、K-LoRA。
- `Full Source Review Complete`（HF replay新增）：ART / Anonymous Region Transformer、
  Clustering-On-Difficulty downstream scaling。
- `Full Source Review Complete`（HF replay新增）：Visual Perception Tokens、MLLMs Know Where to Look。
- `Full Source Review Complete`（HF replay新增）：Finding the Sweet Spot / Preference Data、WiCkeD。
- `Full Source Review Complete`（HF 2月27日页新增）：TheoremExplainAgent、BIG-Bench Extra Hard。
- `Full Source Review Complete`（HF 2月27日页新增）：Plutus。
- `Full Source Review Complete`（HF 2月27日页新增）：Project Alexandria、Can Language Models Falsify? / REFUTE。
- `Full Source Review Complete`（HF 2月27日页新增）：Distill Any Depth、MMKE-Bench。
- `Full Source Review Complete`（HF 2月27日页新增）：FSPO。
- `Full Source Review Complete`（HF 2月27日页新增）：AISafetyLab technical report、PosterSum。
- `Low-score Verification Complete`（HF 2月27日页新增）：GHOST 2.0（18/30；domain-specific image manipulation，
  Weekly Only — Outside Core Knowledge-tree Scope）。
- `Low-score Verification Complete`（HF 2月27日页新增）：Accented ATC ASR（18/30；domain/accent-specific Whisper
  fine-tuning，Weekly Only — Domain Case / No New Core Mechanism）。
- `Full Source Review Complete`（2月28日cross-index）：xAR、ArtGS、FUSED、Relation-Specific Neurons、MAMUT、DVPO、
  NeoBERT、LongRoPE2、Ext2Gen与SuperRAG。
- `Full Source Review Complete`（HF 2月28日Newsletter replay）：R2-T2、Self-rewarding Correction、SoRFT、UniTok、EDGS、FINEREASON、FlexiDiT、MedVLM-R1、Mobius、Dream Engine、R1-T1与Variational Consistency Training。
- Newsletter可见20条identity已全部恢复：18个W09 owner完成，
  CODESYNC回拨W08、上述12个新增W09 owner与Guardians of the Agentic System回拨W08；推荐日不替代v1日期。
- `Cross-week Source Family Node`：AISafetyLab technical report v1属于W09；official framework open-source event
  2024-12-31属于W01 spillback，不能将code availability首次归到本周。
  technical report已完成26/30 Full Source Review，decision为`Books Pending — No Change Candidate / Code Event Spillback W01`。
- `Spillback to W08`（HF 2月27日推荐页）：MolSpectra v1 2025-02-22、DOEI v1 2025-02-21；
  推荐日不改变owner Week，后续由W08 spillback ledger全文处理。
- `Spillback to W08`（HF 2月28日推荐页）：CODESYNC（arXiv:2502.16645）v1为2025-02-23；本周只保存
  discovery lineage，不重复评分。
- `Spillback to W08`（HF 2月28日Newsletter）：Guardians of the Agentic System（arXiv:2502.16750）v1为
  2025-02-23；尽管Newsletter在2月28日推荐，owner仍属于W08。
- `Spillback to W01`（HF 2月28日推荐页）：Non-ergodic Emergence（arXiv:2501.01638）v1为2025-01-03，
  2025-02-28只是v2 revision；回拨W01 source-family revision ledger，不作为W09新事件。
- 3月1～2日没有检索到对应HF Newsletter或精确`Submitted on`命中；arXiv官方年度报告说明announcement通常每周五天，
  但周末submission可能进入后续listing，因此不能仅凭“无周末announcement”推断无owner event。Google Scholar/OpenAlex/DBLP的精确日期导出
  在本轮接口中仍不可访问，保留`Discovery Gap / External Metadata Export Unavailable`，不伪造“零候选”。
- `Cross-week Revision Node`：Towards an AI co-scientist（paper v1 2025-02-26）；owner family 的官方
  Blog event 位于 W08，本周只补全文证据与 revision lineage，不重复评分。
- 已确认 HF 2 月 24～25 日推荐页中的 LLM-Microscope、MaskGWM、LightThinker、MoBA、StructFlowBench
  等论文 v1 早于 W09，已从本周候选池排除，防止推荐日造成日期漂移。
- HF 2月24日页的 SurveyX、SIFT、U-SAFEBENCH、AlchemyBench、MedHallu、ThinkJSON、o3 reasoning分析、
  InterFeedback与Tree-of-Debate均以v1归W08；HF 2月25日页的Audio-FLAN、CodeCriticBench、RIFLEx、MMIR、
  Reflective Planning与TAG同样归W08。推荐页日期只保留为discovery evidence，不改变owner Week。
- HF 2月26日页的Curie、Scale-Distribution Decoupling、Prompt-to-Leaderboard与LaTIM按v1归W08；
  其机制是否需要补入W08由W08 spillback ledger另行处理，不在W09重复评分。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- `Full Source Review Complete`：Ray 2.43.0（2025-02-27），首次发布alpha `ray.data.llm` / `ray.serve.llm`。
- `Full Source Review Complete`：JAX 0.5.1（2025-02-24）；sharding进入JIT tracing-cache identity，CPU
  multi-process collectives默认Gloo，并修正TPU startup与persistent compilation-cache I/O边界。
- `Low-score Verification Complete`：Unsloth Direct Windows Support（2025-02-28；19/30）；属于安装与兼容性
  version fact，未改变训练/推理核心机制，且公开回复暴露vLLM/Triton/CMake/CUDA兼容边界。
- 已完成package/release日期去重：TensorRT-LLM 0.17.0（2025-01-30）、Triton 3.2.0（2025-01-22）、
  SGLang 0.4.3（2025-02-14）、Transformers 4.49.0与Accelerate 1.4.0（均2025-02-17）、vLLM 0.7.3
  与DeepSpeed 0.16.4（均2025-02-20）归更早 owner Week；DeepSpeed 0.16.5（2025-03-27）、Triton 3.3.0
  （2025-04-09）、SGLang 0.4.4（2025-03-13）、Accelerate 1.5.0（2025-03-12）归后续周。
- MLX PyPI序列显示0.22.1（2025-02-06）之后是0.23.2（2025-03-05），W09没有package release；
  原“MLX 0.23.1 / 2025-02-19”缺少immutable artifact metadata，已撤回而非当作无条件事实。
- JAX 0.5.2官方changelog日期为2025-03-04、PyPI upload为2025-03-05，均归W10；它修复0.5.1的
  TPU metric logging / `tpu-info` regression，作为same-family revision node，不在W09重复评分。
- 进一步日期去重：CUDA 12.8.0为2025-01-31、12.8.1文档为2025-03-04；NVIDIA Dynamo首次公开为
  2025-03-18；KServe 0.15.0-rc0为2025-01-27、GA为2025-03-31；Kubernetes 1.32.2为2025-02-13；
  ONNX Runtime 1.20.1为2024-11-21、1.21.0为2025-03-08。本周均无新owner，不能把后续版本回填W09。
- OpenXLA/XLA官方GitHub仓库不发布GitHub Releases，因此该release feed不构成候选源；未来需以JAX/XLA commit、
  StableHLO release或官方Blog的明确事件日期发现，而不能用空release页证明“无代码变化”。
- Kubeflow manifests、Megatron-LM历史release分页与llama.cpp高频tag的W09 immutable time-slice仍无法从当前接口完整导出，
  转入`Blocked — Historical Release Feed Time Slice Unavailable` ledger；这三项按blocked-skip规则不再维持普通`Discovery Pending`。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GPT-4.5 research preview | 3 | 5 | 4 | 4 | 5 | 4 | 25/30 | Books Pending — Refine Existing Argument Candidate / Mechanism Partially Disclosed |
| Claude 3.7 Sonnet and Claude Code | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| SWE-RL | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Books Pending — Refine Existing Argument Candidate |
| SpargeAttn | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| Drop-Upcycling | 4 | 4 | 4 | 5 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| Kanana | 3 | 4 | 4 | 4 | 5 | 5 | 25/30 | Books Pending — Refine Existing Argument Candidate |
| Towards Optimal Multi-draft Speculative Decoding | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| WebGames | 3 | 4 | 5 | 4 | 5 | 5 | 26/30 | Books Pending — No Change Candidate |
| OmniAlign-V | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Books Pending — Refine Existing Argument Candidate |
| Language Models' Factuality Depends on the Language of Inquiry | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Books Pending — Refine Existing Argument Candidate |
| Rank1 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Books Pending — No Change Candidate |
| DeltaBench / Can LLMs Detect Errors in Long CoT? | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Books Pending — Refine Existing Argument Candidate |
| Agentic Reward Modeling | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| VEM: Environment-Free Exploration for Training GUI Agent | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Books Pending — Refine Existing Argument Candidate |
| CritiQ: Mining Data Quality Criteria from Human Preferences | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| Training LLMs with MXFP4 | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Books Pending — Refine Existing Argument Candidate |
| Self-Training Elicits Concise Reasoning | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Books Pending — Refine Existing Argument Candidate |
| Granite Embedding Models | 3 | 4 | 5 | 5 | 5 | 5 | 27/30 | Books Pending — No Change Candidate |
| WorldModelBench | 4 | 5 | 4 | 5 | 5 | 5 | 28/30 | Books Pending — No Change Candidate |
| LongRePS | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| PersonaBench | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Books Pending — No Change Candidate |
| Safety Tax | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Books Pending — No Change Candidate |
| ARIES: Autonomous Reasoning on Interactive Thought Graphs | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Books Pending — No Change Candidate |
| GUI Pivot / Query Inference | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Books Pending — Refine Existing Argument Candidate |
| RaPID: Retrieval-Augmented Long Text Generation | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| Babel Multilingual LLMs | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| LADDER / Test-Time Reinforcement Learning | 5 | 5 | 3 | 4 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| What Makes a Good Diffusion Planner? | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Books Pending — Refine Existing Argument Candidate |
| Ray 2.43.0 LLM APIs | 3 | 4 | 5 | 5 | 5 | 4 | 26/30 | Books Pending — No Change Candidate |
| JAX 0.5.1 | 3 | 4 | 4 | 5 | 5 | 4 | 25/30 | Books Pending — Refine Existing Argument Candidate |
| FlashMLA v1 | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Books Pending — Refine Existing Argument Candidate / W09 Snapshot Not Tagged |
| DeepEP V1 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Books Pending — Refine Existing Argument Candidate / V1 Artifact Mutable |
| DeepGEMM v1 | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Books Pending — Refine Existing Argument Candidate / W09 Snapshot Not Tagged |
| DualPipe code artifact | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate / Mechanism Pre-window |
| EPLB initial artifact | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Books Pending — Refine Existing Argument Candidate / Initial Snapshot Partially Recovered |
| 3FS open-source artifact | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Books Pending — Structural/Refine Candidate / W09 Snapshot Not Tagged |
| smallpond open-source artifact | 3 | 4 | 5 | 4 | 5 | 4 | 25/30 | Books Pending — Refine Existing Argument Candidate / 3FS-coupled Evidence |
| V3/R1 Online Inference System Overview | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Books Pending — Refine Existing Argument Candidate / Vendor Production Case |
| Wan2.1 code and weights release | 5 | 4 | 5 | 4 | 5 | 5 | 28/30 | Books Pending — Refine Existing Argument Candidate / Later Report Evidence |
| olmOCR model/data/pipeline release | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Books Pending — Refine Existing Argument Candidate / Teacher and Pipeline Coupled |
| Phi-4-mini + Phi-4-multimodal launch family | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Books Pending — Refine Existing Argument Candidate / Later Report Evidence |
| Command R7B Arabic open-weights release | 4 | 3 | 5 | 4 | 5 | 5 | 26/30 | Books Pending — Refine Existing Argument Candidate / Regional Post-training Branch |
| Make LoRA Great Again / GOAT | 4 | 4 | 4 | 5 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| Stable-SPAM (v1) | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| VideoGrain | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Refine Existing Argument Candidate |
| DICEPTION (v1) | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Books Pending — Refine Existing Argument Candidate |
| Mobile-Agent-V (v1) | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| Thus Spake Long-Context LLM (survey v1) | 2 | 4 | 5 | 4 | 5 | 5 | 25/30 | Books Pending — No Change Candidate |
| KV-Edit | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| K-LoRA | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Books Pending — Refine Existing Argument Candidate |
| ART / Anonymous Region Transformer | 5 | 4 | 3 | 4 | 5 | 5 | 26/30 | Books Pending — Refine Existing Argument Candidate / Artifact Withdrawn |
| Clustering-On-Difficulty downstream scaling | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | Books Pending — Refine Existing Argument Candidate / Headline Metric Disputed |
| Visual Perception Token | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| MLLMs Know Where to Look / ViCrop | 4 | 4 | 4 | 5 | 5 | 5 | 27/30 | Books Pending — No Change Candidate |
| Finding the Sweet Spot / Preference Data | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| WiCkeD | 3 | 4 | 5 | 5 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| TheoremExplainAgent (v1) | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Books Pending — No Change Candidate |
| BIG-Bench Extra Hard (v1) | 4 | 4 | 5 | 5 | 5 | 5 | 28/30 | Books Pending — Refine Existing Argument Candidate |
| GHOST 2.0 | 3 | 2 | 3 | 5 | 2 | 3 | 18/30 | Weekly Only — Outside Core Knowledge-tree Scope |
| Plutus | 3 | 4 | 5 | 5 | 4 | 4 | 25/30 | Books Pending — No Change Candidate |
| Project Alexandria | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | Books Pending — Refine Existing Argument Candidate / Legal Status Jurisdiction-Specific |
| Can Language Models Falsify? / REFUTE | 5 | 5 | 4 | 5 | 5 | 5 | 29/30 | Books Pending — Refine Existing Argument Candidate |
| Distill Any Depth | 4 | 3 | 4 | 4 | 3 | 4 | 22/30 | Books Pending — No Change Candidate |
| MMKE-Bench | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Books Pending — Refine Existing Argument Candidate / Artifact Metadata Inconsistent |
| FSPO | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| Accented ATC ASR | 2 | 3 | 4 | 4 | 2 | 3 | 18/30 | Weekly Only — Domain Case / No New Core Mechanism |
| AISafetyLab technical report | 3 | 4 | 5 | 5 | 5 | 4 | 26/30 | Books Pending — No Change Candidate / Code Event Spillback W01 |
| PosterSum | 3 | 3 | 4 | 5 | 4 | 5 | 24/30 | Books Pending — No Change Candidate |
| Beyond Next-Token / xAR | 5 | 4 | 4 | 5 | 5 | 5 | 28/30 | Books Pending — Refine Existing Argument Candidate |
| LongRoPE2 | 5 | 4 | 4 | 5 | 5 | 5 | 28/30 | Books Pending — Refine Existing Argument Candidate |
| ArtGS | 4 | 3 | 4 | 5 | 4 | 4 | 24/30 | Books Pending — Refine Existing Argument Candidate |
| FUSED / Reversible Federated Unlearning | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Books Pending — Refine Existing Argument Candidate |
| Relation-Specific Neurons | 4 | 4 | 3 | 5 | 5 | 5 | 26/30 | Books Pending — No Change Candidate |
| MAMUT | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Books Pending — Refine Existing Argument Candidate / Downstream Model Evidence Missing |
| DVPO / Pretrain Value, Not Reward (v1) | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Books Pending — Refine Existing Argument Candidate / Theorem Assumptions Restricted |
| NeoBERT | 3 | 4 | 5 | 5 | 4 | 5 | 26/30 | Books Pending — Refine Existing Argument Candidate |
| Ext2Gen v1 | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate / Artifact Unreleased at v1 |
| SuperRAG | 3 | 4 | 4 | 4 | 5 | 5 | 25/30 | Books Pending — Refine Existing Argument Candidate / Core Parser Not Open |
| R2-T2 | 5 | 4 | 3 | 5 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate / High Test-time FLOP Cost |
| Self-rewarding Correction | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Books Pending — Refine Existing Argument Candidate / Internal Reward Not Independent |
| SoRFT | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate / Proxy Reward False Negatives |
| UniTok | 5 | 4 | 4 | 5 | 5 | 5 | 28/30 | Books Pending — Refine Existing Argument Candidate |
| EDGS / Sparse Time-Variant Gaussian Splatting | 4 | 3 | 4 | 5 | 3 | 4 | 23/30 | Books Pending — No Change Candidate / Rendering Evidence Only |
| FINEREASON | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| FlexiDiT | 5 | 4 | 4 | 5 | 5 | 5 | 28/30 | Books Pending — Refine Existing Argument Candidate |
| MedVLM-R1 v1 | 4 | 4 | 3 | 4 | 5 | 5 | 25/30 | Books Pending — Refine Existing Argument Candidate / Reasoning Faithfulness Unverified |
| Mobius | 4 | 3 | 4 | 4 | 4 | 5 | 24/30 | Books Pending — Refine Existing Argument Candidate / Training-Free Base-Model Bound |
| Dream Engine / Multimodal Representation Alignment | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Books Pending — Refine Existing Argument Candidate |
| R1-T1 v1 | 4 | 4 | 3 | 3 | 5 | 5 | 24/30 | Books Pending — Refine Existing Argument Candidate / v1 Evidence Incomplete |
| Variational Consistency Training / VCT | 5 | 4 | 3 | 5 | 4 | 5 | 26/30 | Books Pending — Refine Existing Argument Candidate |
| Unsloth Direct Windows Support | 2 | 3 | 4 | 4 | 3 | 3 | 19/30 | Weekly Only — Version/Compatibility Fact / No New Core Mechanism |
| Predictive Data Selection / PreSelect | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Books Pending — Refine Existing Argument Candidate |
| Chain of Draft | 3 | 4 | 5 | 5 | 4 | 3 | 24/30 | Books Pending — Refine Existing Argument Candidate / Prompting Case |
| DeepSolution / SolutionRAG | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Books Pending — Refine Existing Argument Candidate / Domain Case |
| ViDoRAG / ViDoSeek | 4 | 4 | 4 | 5 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| LettuceDetect | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Books Pending — Refine Existing Argument Candidate |
| TeleRAG | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Books Pending — Refine Existing Argument Candidate |
| DexGraspVLA | 4 | 4 | 4 | 5 | 5 | 5 | 27/30 | Books Pending — Experimental Embodied Branch |
| TokenSwift / Ultra-long Sequence Generation | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Books Pending — Refine Existing Argument Candidate |
| Efficient Test-Time Scaling via Self-Calibration | 4 | 4 | 4 | 5 | 5 | 5 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| DuoDecoding | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Books Pending — Refine Existing Argument Candidate |
| Web AI Agent Vulnerability | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Refine Existing Argument Candidate |
| LLM as a Broken Telephone | 3 | 4 | 4 | 5 | 4 | 4 | 24/30 | Books Pending — Refine Existing Argument Candidate |

> 说明：表中只列已经获得最终证据 disposition 的 owner event：`20+` 候选完成 Full Source Review，
> 低分候选完成identity/date/score/rejection核验。ordinary backlog为0；声明的外部metadata/release-feed gaps不阻塞W09 Gate。

## Low-score Candidate Verification

### GHOST 2.0

- **Identity and Date:** `GHOST 2.0: Generative High-fidelity One Shot Transfer of Heads`，arXiv:2502.18417；
  v1 2025-02-25、v2 2025-02-26、v3 2025-02-27、v4 2025-06-09。W09 owner锁定v1。
- **Primary Sources Checked:** https://arxiv.org/html/2502.18417v1；https://arxiv.org/abs/2502.18417；
  https://github.com/ai-forever/ghost-2.0。已核验abstract/introduction、Aligner→Blender pipeline、evaluation/conclusion/
  impact statement、revision与official train/inference surface；current repo无immutable W09 tag。
- **Score:** Technical Novelty 3、System Impact 2、Practical Value 3、Source Reliability 5、Project Relevance 2、
  Longevity 3，Total 18/30。
- **Rejection Boundary:** 该工作以multi-scale identity/motion encoders生成对齐head，再通过semantic-region correlation、
  color reference与inpainting UNet完成domain-specific head swap；它是完整computer-vision application，但没有改变本书关于
  multimodal representation、generation state、serving runtime、platform或agent workflow的核心设计结论。Deepfake consent、watermark、
  detection与misuse风险应由`PLATFORM-SECURITY`的一般synthetic-media policy承载，不因单一应用建立新机制主线。
- **Disposition:** `Weekly Only — Outside Core Knowledge-tree Scope`。不进入Books，不把作者benchmark或“state of the art”外推。

### Accented ATC ASR

- **Identity and Date:** `Adapting Automatic Speech Recognition for Accented Air Traffic Control Communications`，
  arXiv:2502.20311；v1 2025-02-27，唯一version。
- **Primary Sources Checked:** https://arxiv.org/html/2502.20311v1；https://arxiv.org/abs/2502.20311；
  https://github.com/aether-raid/atc-transcription。已核验dataset/fine-tuning/noise augmentation、30-epoch selection、
  cross-accent WER、future work/conclusion及official train/infer surface；dataset/model access受限且repo无release tag。
- **Score:** Technical Novelty 2、System Impact 3、Practical Value 4、Source Reliability 4、Project Relevance 2、
  Longevity 3，Total 18/30。
- **Rejection Boundary:** 该工作以37小时SEA-accented ATC数据fine-tune Whisper Small/Large-v3-Turbo，加入radio-noise
  augmentations并按validation WER选checkpoint；在本地SEA dataset显著改善，但对ATCO2/ATCOSIM泛化下降。它验证“data distribution、
  accent、terminology与noise必须进入evaluation slice”，却没有提出新的ASR architecture、training-system或AI-platform机制。
- **Disposition:** `Weekly Only — Domain Case / No New Core Mechanism`。不进入Books；9.82% WER不外推为aviation safety或production SLO。

### Unsloth Direct Windows Support

- **Identity and Date:** `Direct Windows support for Unsloth`，official announcement discussion #1849于2025-02-28发布，
  implementation指向PR #1841；W09 owner是Windows packaging/installation compatibility event，不等于独立runtime release。
- **Primary Sources Checked:** https://github.com/unslothai/unsloth/discussions/1849；
  https://github.com/unslothai/unsloth/pull/1841。已核验`pyproject.toml` dependency surface、Python 3.9～3.12、
  CUDA 11.8/12.4/12.6与GTX 1650/RTX 3050测试声明，并检查后续回复中的CMake、Triton、vLLM与CUDA/PyTorch mismatch限制。
- **Score:** Technical Novelty 2、System Impact 3、Practical Value 4、Source Reliability 4、Project Relevance 3、
  Longevity 3，Total 19/30。
- **Rejection Boundary:** 该事件把Windows SDK/MSVC、CUDA/PyTorch版本和Python extras编码进安装路径，降低手工依赖拼装成本；
  但它没有改变LoRA/GRPO、kernel、memory、distributed runtime或serving机制。公开测试仅覆盖两台消费级GPU，后续回复仍出现
  vLLM缺少Windows binary、Triton/CMake与CUDA wheel冲突，不能外推为完整Windows support matrix或production readiness。
- **Disposition:** `Weekly Only — Version/Compatibility Fact / No New Core Mechanism`。Books不吸收产品安装步骤；长期认知只保留
  “platform support必须绑定OS/compiler/driver/runtime/extension matrix”，该观点现有Platform章节已覆盖。

### Deep Analysis 1 — Claude 3.7 Sonnet and Claude Code

- First Public: 2025-02-24
- Status: Official release; vendor evaluation
- Primary Source: https://www.anthropic.com/news/claude-3-7-sonnet
- Evolution Relationship: Direct Evolution

#### Why

同一模型需要在即时响应与长思考之间选择不同 inference budget；coding agent 还需要把 reasoning 接到可执行工具闭环。

#### Principle and Mechanism

官方发布引入 hybrid reasoning 与可控 thinking budget，并以 Claude Code research preview 展示终端 agent。

#### Trade-off and Evidence Boundary

统一模型简化产品路由，却把预算控制、可见 CoT、成本与 latency 交给运行时；厂商 benchmark 无法分离 model 与 harness 贡献。

#### Connection and Evolution

知识树位置：`MODEL-SAMPLING`、`INFER-SCHEDULING`、`AGENT-TOOL-CALLING` / `AGENT-WORKFLOW`
与 `PLATFORM-SECURITY`。该来源只支持版本行为与system-card evidence，不公开新的model/runtime mechanism。

## Full Source Review

### GPT-4.5: Pre-training Scale and Inference-time Reasoning Are Complementary Capability Axes

- **Candidate / Week / Score:** GPT-4.5 research preview / 2025-W09 / 25/30。
- **Source Family ID:** `openai-gpt-4-5-pretraining-scale-vs-reasoning-axis`。
- **Source Type:** OpenAI official launch + 31-page System Card + official evaluation repository lineage；no architecture/training paper or public weights。
- **Event Date / First-public Date / Revision History:** launch与System Card均为2025-02-27；research preview后来下线或被新模型替代不改变W09 owner date。
- **Direct Primary Sources:** https://openai.com/index/introducing-gpt-4-5/；
  https://cdn.openai.com/gpt-4-5-system-card-2272025.pdf。
- **Related Primary Sources:** https://github.com/openai/simple-evals；launch-linked model/API documentation只用于product surface；
  GPT-4o、o1与o3-mini system cards用于baseline/evolution，不反推GPT-4.5内部实现。
- **Access and Verification Status:** launch与System Card全文可访问；model size、architecture、token count、data mix proportions、
  compute、optimizer、alignment algorithm与serving topology为`Not Disclosed`。作者评估未独立复现。
- **Full-read Coverage:** launch全部sections/appendix；System Card model data/training、disallowed content、jailbreak、hallucination、fairness、
  instruction hierarchy、red teaming、Apollo/METR、Preparedness CBRN/cyber/persuasion/autonomy、multilingual、conclusion与appendices。
- **Original Problem:** 单纯增加test-time chain-of-thought擅长可验证STEM/logic，却不必然提升广泛world knowledge、自然对话、审美与
  intent alignment；反之，扩大pre-training可能改善知识与模式联结，却缺少显式多步计算预算。
- **Why the Previous Design Was Reasonable:** GPT-style next-token pretraining可统一吸收广泛数据并摊销推理成本；reasoning model通过额外
  inference compute把复杂搜索留到请求时。两者分别优化不同能力/成本边界，单一路线在其目标workload上仍合理。
- **Changed Constraint:** 产品需要同时服务开放域知识、写作/协作与复杂STEM；模型规模继续上升时，监督数据、alignment capacity、
  hallucination、安全评估和inference cost都成为独立约束，不能只用一个aggregate benchmark描述“更聪明”。
- **Mechanism:** 官方只披露继续扩大unsupervised pre-training compute/data并采用architecture/optimization innovations，随后以SFT、RLHF与
  “由较小模型产生数据”的新scalable supervision技术post-train；GPT-4.5不在回答前执行o1式显式reasoning。具体算法未披露。
- **State Ownership:** pretraining weights拥有压缩后的统计知识；post-training policy拥有instruction/behavior preference；system message拥有
  instruction hierarchy；deployment moderation与policy layer拥有部分安全控制；evaluation harness拥有attempt/refusal与capability测量，不能混为model state。
- **Control Flow / Data Flow:** heterogeneous pretraining corpora → filtering → unsupervised objective → base weights → SFT/RLHF/scalable supervision →
  aligned checkpoint → system/user messages → direct token generation；与reasoning branch的“prompt → internal deliberation budget → answer”形成并列路径。
- **Implementation Details:** 官方披露训练于Azure AI supercomputers、数据含public/proprietary partnership/custom datasets并执行PII与风险过滤；
  instruction hierarchy监督system优先于user。parameter count、topology、precision、parallelism、checkpoint与runtime未公开。
- **Evaluation Contract:** System Card比较GPT-4o、o1/o3-mini与GPT-4.5，覆盖PersonQA、refusal/jailbreak、BBQ、instruction hierarchy、
  red-team、Preparedness、SWE-Lancer与14-language MMLU；不同任务使用不同prompt/scaffold/judge，production model可能随system updates变化。
- **Baselines / Ablations / Sensitivity / Overhead:** 有跨模型baseline但没有matched compute/data/architecture ablation，无法分离pretraining scale、
  architecture、optimization与post-training贡献；没有cost/latency/quality frontier或重复seed。METR只评估earlier checkpoint且使用o1-optimized scaffold。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Azure supercomputer之外均`Not Disclosed`；parameter count、GPU type/count、
  precision、training tokens、context length contract、batch、API concurrency、TTFT/TPOT、cost与SLO未形成可比较workload contract。
- **What the Evidence Actually Proves:** OpenAI在W09发布了一个不依赖显式reasoning的更大GPT branch，并公开把pretraining scale与reasoning scale
  定义为互补轴；System Card在其评测条件下显示PersonQA hallucination/accuracy与部分instruction hierarchy改进，同时部分安全指标只是持平或更差。
- **What It Does Not Prove:** pretraining形成真实因果world model、规模自动消除hallucination、GPT-4.5普遍优于reasoning models、small-model-generated
  supervision无偏、EQ可客观泛化、或任何公开benchmark能隔离模型与harness贡献。内部architecture/optimizer也不能由能力反推。
- **Limitations / Threats to Validity:** vendor-authored、research preview、mechanism partial disclosure、model snapshot可变、评测覆盖有限、
  no matched ablation/independent replication；PersonQA不覆盖chemistry等domain，Preparedness明确是capability lower bound且受elicitation影响。
- **Trade-offs / New Failure Modes:** 扩大pretraining带来广泛知识/自然交互，却增加训练compute、数据治理、记忆/隐私与部署成本；
  direct answer降低reasoning latency但复杂搜索较弱；derived supervision可扩展alignment，却引入teacher bias、provenance与feedback-loop风险。
- **Where the Previous Design Still Applies:** reasoning models用于可验证多步STEM/logic；较小GPT用于低成本高并发；RAG/tool verification用于新鲜或可追溯事实；
  domain model用于受控分布；human review用于高风险决策。GPT-4.5不是这些分支的单向替代。
- **Evolution Relationship:** `Alternative Branch`：scale direct pretraining/world knowledge ↔ scale inference-time reasoning/search；长期系统趋向
  base knowledge + dynamic reasoning + retrieval/tools + verifier/routing组合，而不是用后一条路线覆盖前一条。
- **ROADMAP Node:** `WORLDVIEW-SCALING-LAW`（Current Ch7；Legacy Ch7）主 owner；handoff到`WORLDVIEW-LLM-INTELLIGENCE`、
  `TRAIN-PRETRAINING`、`TRAIN-RLHF`、`MODEL-SAMPLING`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch5 representation、Ch7 scaling、Ch8 capability、Ch28 pretraining、Ch31 RLHF、
  Ch66 evaluation与Ch72 security；本条应解释capability axes/evidence boundary，而不是写GPT-4.5产品清单。
- **Existing Coverage:** Books已有pretraining与inference-time compute的分层，但缺少“两个互补能力轴不能用单一榜单合并”的清晰演进链；
  该source family可refine既有论证，同时保留RAG、reasoning与小模型共存条件。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Mechanism Partially Disclosed`。Historical Books Gate保持关闭。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly与年度账本；未修改Books，未保留vendor headline或把PersonQA外推为通用可靠性。
- **Open Questions:** architecture/compute/data scaling law、derived-supervision provenance、pretraining-vs-reasoning matched frontier、knowledge freshness、
  calibration/abstention、memory/privacy、serving cost、domain hallucination、independent reproduction与后续unified-router演进。

### Claude 3.7 Sonnet and Claude Code

- **Candidate / Week / Score:** Claude 3.7 Sonnet and Claude Code / 2025-W09 / 23/30。
- **Source Family ID:** `claude-3-7-hybrid-reasoning-and-code-agent`。
- **Source Type:** Anthropic official release + 43-page system card + extended-thinking disclosure；Claude Code
  当时为 product research preview，无公开 runtime design paper。
- **First-public Date / Revision History:** 2025-02-24；system card 与 release同日。后续 Claude Code/product
  changes 不反写为 3.7 release facts。
- **Direct Primary Sources:** https://www.anthropic.com/news/claude-3-7-sonnet；
  https://www.anthropic.com/news/visible-extended-thinking；
  https://www.anthropic.com/system-cards；官方 Claude 3.7 Sonnet System Card PDF。
- **Related Primary Sources:** linked SWE-bench/TAU-bench definitions与 scaffold disclosures；Claude Code current
  docs只证明后续状态，不证明 2025 preview architecture。
- **Access and Verification Status:** Verified for public model/product behavior and system-card evaluations；model
  architecture、training recipe、Claude Code planner/state/recovery 为 `Mechanism Not Disclosed`。
- **Full-read Coverage:** 已读 announcement/appendix/scaffolding、extended-thinking rationale、system card training/
  release process、thinking mode、computer-use/prompt-injection、CoT faithfulness、autonomy/cyber/CBRN evaluations、
  thresholds与third-party assessment；核对 Claude Code preview公开 tool surface。
- **Original Problem:** users需要按 task difficulty在低延迟回答与更多 inference compute之间选择；coding
  还需让模型读取/修改 repository并运行命令/测试，不能只生成 isolated snippet。
- **Why the Previous Design Was Reasonable:** separate fast/reasoning models可独立优化成本与质量，standard
  response减少 latency和 token暴露；人工 coding workflow把 shell/git/test权限留在人类，failure radius较小。
- **Changed Constraint:** 同一产品希望连续调节 reasoning tokens并减少 model routing discontinuity；terminal
  agent需要把 reasoning接到高权限工具，同时面临 prompt injection、partial success和long-horizon stopping。
- **Mechanism:** system card只公开同一 model由 RL训练生成 extended-thinking tokens，API通过 system prompt给
  maximum thinking tokens；standard/extended mode由用户选择。Claude Code preview公开可搜索/读取/编辑文件、
  运行 tests/CLI、commit/push，并要求 user in loop；内部 planner、sandbox、state machine Not Disclosed。
- **State Ownership:** model/runtime拥有当前 thinking-token budget与completion；Claude Code可观察地持有 session/
  tool transcript，但 authoritative file/git state仍在用户环境。权限、checkpoint、retry与approval owner在
  2025来源中 Not Disclosed，不能从后续产品推断。
- **Control Flow / Data Flow:** prompt+mode/budget→single model standard或extended completion→可见 thinking+
  final answer；coding preview是 user task→model选择 bash/file-edit actions→environment结果回流→iterate→
  human oversight。具体 orchestration/rollback未知。
- **Implementation Details:** extended mode maximum tokens由system prompt指定；training仅披露 proprietary data mix、
  filtering、RL/Constitutional AI概况。Claude Code release列出 bash+string-replacement editor等 minimal scaffold；
  high-compute SWE-bench另有parallel attempts、visible-test filtering与scoring model，不能和vanilla pass@1混用。
- **Evaluation Setup:** release含 SWE-bench Verified、TAU-bench等vendor evaluations；TAU-bench max steps从30增至
  100并加planning tool；SWE-bench high-compute使用parallel sampling/filter/ranker。system card另做176-task prompt-
  injection eval、autonomy rule-out suite与CoT faithfulness tests。
- **Baselines / Ablations / Sensitivity:** standard vs extended mode、3.5 predecessor、不同 thinking lengths与
  mitigations；prompt-injection 74%→88% prevention同时0.5% false positive属于176-task adversarial set；system
  card显示 thinking length只在部分 domain提升，CoT常未显式提关键 clues。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** hardware、parameter、precision、serving
  batch/concurrency Not Disclosed；thinking budget为token cap但具体 benchmark各自配置不同；不构成通用 latency/
  cost/SLO curve。
- **What the Evidence Actually Proves:** 官方提供同一model的可控 extended-token interface及一个terminal coding
  preview；system card证明tool-using risk需要model training+runtime classifier等分层 mitigation，且明确可见
  CoT不保证faithful。benchmark结果高度依赖 scaffold/steps/compute。
- **What It Does Not Prove:** 不公开 hybrid model内部architecture，不证明thinking tokens忠实或单调提升质量，
  不证明Claude Code使用某种durable workflow，也不证明厂商 SWE-bench score可分离model与harness贡献。
- **Limitations / Threats to Validity:** proprietary model与vendor eval；benchmark scaffold/infra exclusions改变
  comparability；thinking可泄露或帮助jailbreak，streaming classifier可false-positive；prompt injection仍有未阻止
  cases；autonomy suite是rule-out而非通过即证明真实R&D acceleration。
- **Trade-offs / New Failure Modes:** unified model减少routing complexity，却把budget/latency/cost与thinking exposure
  交给runtime；terminal tools增加环境注入、credential/data exfiltration、partial edits、premature completion与
  rollback责任；CoT monitoring若不faithful会产生虚假安全感。
- **Where the Previous Design Still Applies:** latency-critical/简单请求使用standard mode；separate specialized
  models在成本隔离/独立升级时仍合理；高风险代码/运维应保持human approval、least privilege与deterministic CI。
- **Evolution Relationship:** `Direct Evolution`（product interface）：fixed response mode→same-model controllable
  compute；`Layering / Dependency`（coding）：model→tool harness→environment/approval，而非model自治的同义词。
- **ROADMAP Node:** `INFER-SCHEDULING`（Current Ch56；Legacy Ch52）主 owner；`MODEL-SAMPLING`
  （Current/Legacy Ch20）handoff；`AGENT-TOOL-CALLING` / `AGENT-WORKFLOW`（Current Ch78/81；
  Legacy Ch74/77）负责tool/workflow；`PLATFORM-SECURITY`（Current Ch72；Legacy Ch68）负责prompt injection。
- **Target and Adjacent Chapters Read:** 已读 Current Ch19～21、Ch54～56、Ch72、Ch77～82；核对 budget control、
  model-vs-harness evaluation与untrusted tool environment。
- **Existing Coverage:** Books已有 adaptive inference budget、tool permission与workflow state原则；来源主要是
  version/product fact和system-card case，未披露可新增的model/runtime mechanism。
- **Integration Decision:** `Weekly Only — Version/Product Fact / Mechanism Not Disclosed`。
  若写入只可能作为 inference-budget/security 的受限案例，不形成新设计结论。
- **Changed Files or Rejection Reason:** 不改 Books；thinking budget、tool permission 和 workflow state 已由
  `MODEL-SAMPLING` / `INFER-SCHEDULING` / Agent nodes 的通用 contract 覆盖。
- **Open Questions:** quality-per-token calibration、budget owner、encrypted/hidden thinking audit、Claude Code
  2025 preview的sandbox/approval/recovery contract与model/harness contribution separation。

### SWE-RL: Software Evolution Data as a Verifier-Bounded RL Environment

- **Candidate / Week / Score:** SWE-RL / 2025-W09 / 25/30。
- **Source Family ID:** `swe-rl-software-evolution-grpo`。
- **Source Type:** arXiv v1 full paper + official repository/reward implementation + Agentless Mini evaluation scaffold。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-25；后续 NeurIPS version、repository
  refactor 与新增说明只作 lineage，不倒写为 W09 event-time implementation。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.18449；https://arxiv.org/html/2502.18449v1；
  https://github.com/facebookresearch/swe-rl。
- **Access and Verification Status:** v1 Method、evaluation、ablation、appendices 与 current official artifact
  已核验。Repository 明示 current refactor 可能与内部训练实现不一致，test generation/execution 仍为 WIP；
  因此 artifact 证明 reward/scaffold surface，不证明 paper-time online RL stack 可复现。
- **Full-read Coverage:** metadata、Introduction、PR data curation、reward/GRPO objective、training setup、
  SWE-bench/scaling/OOD/reward ablation、limitations、Agentless Mini/SFT/midtraining appendices、prompt，以及
  current reward APIs、pipeline stages、WIP 边界。
- **Original Problem:** competitive-code RL 可以依赖 exact answer 或 executable tests；真实 repository issue
  缺廉价、稳定的完整执行环境，且现有训练常依赖 proprietary teacher traces。如何从公开 software evolution
  artifact 构造可规模化的 policy-improvement signal？
- **Why the Previous Design Was Reasonable:** SFT teacher traces直接提供格式与repair pattern；execution reward
  更接近功能正确性；固定 Agent scaffold把 localization、repair、test generation分开，便于调试。它们在可承担
  teacher/execution成本、需要 semantic correctness 或 workflow可观测性时仍更可靠。
- **Changed Constraint:** 需要从数百万 repositories/PRs 扩展训练，同时减少 proprietary teacher 与
  per-rollout execution cost；policy还要适配 file localization、repair和rerank组成的外部 scaffold。
- **Mechanism:** 从 4.6M clones 与 GitHub events聚合24M PR，经去污染、issue linking、relevant-file prediction
  与过滤得到约11M instances；RL seed包含 issue、完整相关文件与oracle patch。格式错误 reward=-1，其他输出用
  predicted/oracle patch 的 `SequenceMatcher` similarity，组内采样后用 GRPO 更新。
- **State Ownership:** dataset pipeline拥有 repo/commit/PR/issue identity；oracle patch拥有训练 target；policy
  生成 reasoning与search/replace edits；reward parser/sequence matcher拥有可见优化信号；Agentless Mini拥有
  localization、sampling、test generation与reranking；SWE-bench evaluator而非训练 reward拥有最终 solved authority。
- **Control Flow / Data Flow:** repository history/events → self-contained PR instance → issue+code context+oracle patch
  → 16 rollouts/problem → format parse + patch similarity → group-relative update；evaluation时另经 localization →
  500 repair samples → reproduction-test execution/rerank → one patch → SWE-bench hidden evaluator。
- **Implementation Details:** Llama-3.3-70B-Instruct训练1,600 steps、16K context、global batch 512；每步32
  problems×16 rollouts。Current repository公开 prompt与三种 patch-similarity reward API，但明确 paper-time training
  implementation未完整复现，reproduction/regression test path因refactor/infra差异仍 WIP。
- **Evaluation Contract:** SWE-bench Verified 500 issues；主结果每题500 patches、temperature 1.0、top-30
  reproduction tests并只提交最高rank patch。Repair-only ablation提供oracle files且不运行定位/测试；OOD表是
  HumanEval+、BigCodeBench、CRUXEval、MATH/MMLU等不同contract，不能与41.0%合成“通用推理”单指标。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比 base、同seed SFT、midtraining与其他公开 systems；
  repair samples从20增至160带来主要增益，160→500趋于饱和；tests约20后趋于饱和；paper承认大sampling
  budget昂贵。没有等总推理compute的model-only comparison，也没有完整reward exploit/semantic-equivalence ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 70B Llama、16K、global batch 512、
  16 rollouts/problem与500 inference patches已披露；训练/推理 GPU、topology、precision、wall time、tokens、
  serving concurrency、cost、energy与tail SLO为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在 disclosed model、PR data、patch-similarity reward 与 Agentless Mini
  scaffold下，group-relative RL改善了作者定义的repair/evaluation结果；software evolution artifact可以把
  open-world repository history转换为规模化但有偏的训练 environment。
- **What It Does Not Prove:** patch similarity不证明functional equivalence；41.0%不能归因于model alone；
  OOD gains不证明general reasoning mechanism；current repo不能复现paper-time RL infra；pipeline不等于durable
  autonomous coding workflow。
- **Limitations / Threats to Validity:** oracle patch单解偏差、sequence-level reward shortcut、完整文件context的
  unrealistic budget、training/eval repository shift、scaffold contribution、500-sample selection、hidden-test coverage、
  license/provenance与current artifact drift。
- **Trade-offs / New Failure Modes:** cheap similarity reward换来高throughput，却压制等价实现并可奖励表面重合；
  external scaffold降低policy学习难度，却分裂credit；更多sampling提升coverage但放大GPU/cost/selection bias；
  public PR data增加provenance、secrets、license、temporal leakage与repository identity问题。
- **Where the Previous Design Still Applies:** 可执行sandbox存在时，tests/property checks优于patch similarity；
  小规模或高质量teacher可用时SFT更直接；严格production workflow仍需 typed tool permissions、transaction、
  regression gate与human review。
- **Evolution Relationship:** `Direct Evolution`：teacher-trace SFT → verifier-bounded grouped RL on software
  evolution；`Layering / Dependency`：policy → patch reward → scaffold → executable benchmark；不是model能力替代
  workflow evidence。
- **ROADMAP Node:** `TRAIN-GRPO`（Current Ch33；Legacy Ch29）为主 owner；handoff到 `TRAIN-DATA`、
  `PLATFORM-EVALUATION-SYSTEM`、`AGENT-WORKFLOW` 与 `PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读 Ch33 GRPO主干与 verifier/trajectory lifecycle；核对 Ch27 data、
  Ch66 evaluation、Ch81 workflow 的 owner边界。训练reward不拥有release correctness，Agentless scaffold不拥有
  policy objective。
- **Existing Coverage:** Ch33已有 group-relative signal、verifier-is-specification、trajectory identity与
  model/harness/evaluator分层。新证据能 refine“software evolution artifact如何成为有偏environment”，不改变
  GRPO的基本设计结论。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。Historical Books Gate关闭；
  后续只能吸收 artifact/reward/scaffold authority分层，不复制41.0% headline。
- **Changed Files or Rejection Reason:** 本周只更新 Weekly；完成 Source Review并纠正“无论文候选”。
- **Open Questions:** event-time training commit/container、GPU/topology/precision、PR licenses/secrets、semantic
  reward、held-out temporal split、equal-compute SFT/RL、reward hacking、workflow failures、cost/tail SLO与独立复现。

### SpargeAttn: Prediction and Verification inside a Sparse Attention Kernel

- **Candidate / Week / Score:** SpargeAttn / 2025-W09 / 27/30。
- **Source Family ID:** `spargeattn-two-stage-online-sparse-attention`。
- **Source Type:** arXiv v1 full paper + official CUDA/Triton repository + evaluation scripts/examples。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-25；paper注明后续 SageAttention2
  implementation另有约30%速度改进，该结果属于后续 lineage，不倒写进 W09。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.18137；https://arxiv.org/html/2502.18137v1；
  https://github.com/thu-ml/SpargeAttn。
- **Access and Verification Status:** v1 Method、kernel design、实验、ablation、appendix和current artifact已核验；
  official repository当前推荐 API 与paper-time SageAttention base存在版本漂移，W09结论锁定v1。
- **Full-read Coverage:** sparse-mask taxonomy、Sparse FlashAttention、compressed Q/K predictor、stage-1 mask、
  softmax-aware warp filter、SageAttention组合、per-layer grid search、Hilbert permutation、text/image/video setup、
  quality/efficiency、overhead与judge/permutation ablation、current block-sparse API。
- **Original Problem:** dynamic sparse attention若先完整计算mask，预测开销可能吃掉节省；固定pattern不适应
  input/model；直接丢块又可能在softmax后放大误差。需要在运行时以小于saved work的代价判断哪些QK/AV块可跳过。
- **Why the Previous Design Was Reasonable:** exact FlashAttention保持语义且无需校准；pattern-based sparsity实现
  简单、shape稳定；training-native sparse attention可让模型适应mask。短序列、unknown workload、strict exactness
  或校准不足时这些分支仍更合适。
- **Changed Constraint:** LLM和video序列进入17K～128K，attention占比上升；不同heads/layers/inputs的
  sparsity不统一，稀疏预测必须在线、低overhead并同时约束output error。
- **Mechanism:** 先压缩Q/K blocks并用block self-similarity判断可否安全近似，再以TopCdf选择重要block形成
  stage-1 mask；kernel计算selected QK，online softmax过程中按warp partial mass继续跳过低贡献AV work；视觉
  tokens可用Hilbert curve提高邻域self-similarity；SageAttention承担低精度attention execution。
- **State Ownership:** caller/model拥有Q/K/V与causal semantics；offline/per-layer search拥有阈值 `tau/theta/lambda`
  及校准identity；predictor拥有候选mask而非最终模型truth；online softmax拥有本tile是否继续执行；kernel拥有
  block layout与numeric accumulation；evaluation拥有quality tolerance。
- **Control Flow / Data Flow:** Q/K/V → optional locality permutation → block compression/self-similarity →
  predicted sparse mask → sparse QK → online softmax statistics → second-stage warp filtering → selected AV →
  inverse permutation/output。Mask/error threshold改变执行，不改变trained weights。
- **Implementation Details:** paper v1以128×64 blocks与五个sample inputs做layer-wise grid search，先约束
  relative L1 `<l1`再搜索第二级 `<l2`；current API暴露 `topk` 或custom per-head block mask。阈值、layout、
  SageAttention version与GPU architecture共同构成execution-plan identity。
- **Evaluation Contract:** Llama3.1 128K NIAH/LongBench/InfiniteBench/WikiText；CogVideoX 17K、Mochi 22K、
  Flux/SD3.5 4.5K等生成workloads；表报告attention TOPS、sparsity与task metrics。Paper visible table未给出统一
  end-to-end request latency、batch/concurrency、TTFT/TPOT或production SLO。
- **Baselines / Ablations / Sensitivity / Overhead:** exact full attention、MInference、FlexPrefill；测试
  permutation、self-similarity judge、prediction overhead和不同sparsity。Judge分析只保留约2%差异显著cases；
  五input校准和有限thresholds不构成distribution-shift guarantee。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** v1结果绑定作者实现与SageAttention；
  序列长度/模型已披露，统一GPU、precision/quantization、batch、concurrency、memory、energy、tail latency与
  SLO在可见contract中不完整，不能把4～7×attention-kernel claim外推为service speedup。
- **What the Evidence Actually Proves:** 在作者披露的多模型任务上，两级在线筛选可把mask prediction和
  softmax contribution检查嵌入attention execution，并在设定的局部误差/任务指标下获得更多skip opportunity。
- **What It Does Not Prove:** “any model”不是零校准、零质量风险或跨hardware通用；TOPS不是end-to-end
  latency/goodput；五input grid search不证明future inputs；paper-time结果不包含后续SageAttention2增益。
- **Limitations / Threats to Validity:** per-layer threshold overfit、dynamic-shape/graph integration、non-stationary
  workload、causal/decode小M、numeric drift、current artifact drift、baselines不同sparsity/error operating point，
  以及缺少independent reproduction与production-tail evidence。
- **Trade-offs / New Failure Modes:** 更多sparsity减少QK/AV FLOPs，却增加predictor、metadata、branch divergence、
  calibration与error budget；locality permutation提高block structure，却增加reorder/inverse cost；approximation
  failure可能集中在稀有heads/tokens而被aggregate metric掩盖。
- **Where the Previous Design Still Applies:** exact FlashAttention用于短序列、strict correctness、unknown models；
  static pattern适用于结构稳定且compile/graph重要；native sparse training适用于可接受retrain并希望模型适应mask。
- **Evolution Relationship:** `Direct Evolution`：fixed/training-specific sparse mask → input-aware mask prediction →
  softmax-aware online verification；`Layering / Dependency`于FlashAttention/SageAttention kernel，而非替代所有
  attention与Serving scheduling。
- **ROADMAP Node:** `INFER-TENSORRT-LLM`（Current Ch49；Legacy Ch45）的通用execution-plan owner；handoff到
  `MODEL-SELF-ATTENTION`、`INFER-PREFILL`、`INFER-DECODE` 与 `PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读 Ch49 execution/kernel/FlashAttention主线，核对 Ch14 attention
  semantics与 Ch43 Prefill边界；本论文拥有approximate kernel branch，不拥有request scheduling或KV policy。
- **Existing Coverage:** Ch49已有IO-aware tiling、kernel/workload contract与exact/approximate分支；新证据可 refine
  “prediction必须有在线verification与版本化error budget”，不支持新增产品功能列表。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。Historical Books Gate关闭。
- **Changed Files or Rejection Reason:** 本周只更新 Weekly；完成v1与artifact的非模板化审计。
- **Open Questions:** immutable W09 commit、GPU/CUDA/SageAttention版本、full latency/memory、Decode与continuous
  batching、threshold drift/recalibration、per-head tail error、graph capture、多GPU与independent reproduction。

### Drop-Upcycling: Dense Knowledge Preservation versus Expert Specialization

- **Candidate / Week / Score:** Drop-Upcycling / 2025-W09 / 27/30。
- **Source Family ID:** `drop-upcycling-partial-expert-reinitialization`。
- **Source Type:** arXiv v1 full paper + official code/config/data/checkpoint/log artifact family。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-26；后续 conference/current repository
  只用于核验，不改变W09事件边界。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.19261；https://arxiv.org/html/2502.19261v1；
  https://github.com/Taishi-N324/Drop-Upcycling。
- **Access and Verification Status:** v1 Method、theory、long-run evaluation、ablation、appendices及official artifact
  surfaces已核验；paper提供code/data/checkpoints/logs，但完整200K GPU-hour independent rerun未执行。
- **Full-read Coverage:** MoE/upcycling background、SwiGLU/top-2 dropless routing、column sampling/statistics/partial
  reinitialization、retained/common/diverse decomposition、scratch/naive/noise/BTX baselines、500B-token training、
  reinit-ratio/specialization/load-balance/convergence analysis、fine-grained/shared extensions与limitations。
- **Original Problem:** dense checkpoint复制成多个相同experts可立即保留能力，但router早期看到近似同质分支，
  specialization慢；从scratch产生多样性，却丢掉昂贵的dense knowledge并从较高loss开始。
- **Why the Previous Design Was Reasonable:** naive upcycling最安全地保留函数并缩短warm start；random init使
  experts天然不同；BTX用domain branches建立语义差异。短continued-training、强domain expert或不愿破坏
  checkpoint时，旧方案仍合理。
- **Changed Constraint:** MoE计划继续训练数百billion tokens，初始loss优势不够；需要同时保留dense function
  的一部分与足够parameter diversity，让长期learning curve不因expert symmetry变平。
- **Mechanism:** 对每个dense SwiGLU FFN随机选择相同intermediate dimensions，按矩阵方向丢弃对应columns/rows；
  从被选dense weights统计mean/variance并独立重采样每个expert的选中部分，其余权重保留。Top-2时约
  `(1-r)^k` common representation仍被共享，reinitialized portion提供diversity。
- **State Ownership:** dense checkpoint拥有可迁移knowledge；初始化器拥有sampled dimension mask、statistics与
  expert seed；router拥有token→expert choice；load-balance loss/capacity拥有training stability；optimizer从新
  MoE state继续训练；checkpoint/log artifact保存可复算identity。
- **Control Flow / Data Flow:** dense checkpoint → replicate FFN experts → sample intermediate dimensions →
  compute per-matrix statistics → reinitialize selected slices per expert → initialize router → dropless top-2 training →
  observe routing/specialization/convergence → checkpoint MoE。
- **Implementation Details:** standard experiments使用8 experts、top-2 dropless routing；dense通常预训练1T tokens，
  MoE继续500B；Drop ratio在多规模分析，router load-balancing coefficient 0.02。BTX额外训练三个100B-token
  domain dense branches，计算账目不能与其他初始化简单等价。
- **Evaluation Contract:** Llama/Mixtral-style 152M、1.5B、3.7B及8×3.7B路线；LLM-jp corpus v3约2.1T
  available tokens，MoE run达500B；H100累计超过200K GPU-hours；日英QA/MRC/translation/summarization、
  English reasoning等任务，few-shot与CoT设置按appendix固定。
- **Baselines / Ablations / Sensitivity / Overhead:** scratch、naive、50% random-noise upcycling、BTX、dense；
  reinitialization ratio、gate init、expert routing、global/layer balance、convergence catch-up、fine-grained/shared
  extension均讨论。Paper承认LR schedule与不同step count可能混淆catch-up analysis。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** H100与累计GPU-hours、tokens/model
  scales披露；完整cluster topology、precision、micro/global batch、sequence length、optimizer-state layout、network、
  failure/restart、energy与Serving SLO不在统一headline contract中。
- **What the Evidence Actually Proves:** 在作者的bilingual corpus、top-2 8-expert与长训练contract内，部分
  reinitialization形成一个可执行的knowledge-retention/diversity折中，并比被测scratch/naive/noise/BTX有更好的
  long-run curve；实验资源公开提高可审计性。
- **What It Does Not Prove:** 约1/4 training FLOPs不是所有MoE/硬件的端到端成本定律；随机slice不保证语义
  specialization；结果不覆盖shared/fine-grained experts、不同router/capacity、Serving latency或跨语言通用性。
- **Limitations / Threats to Validity:** single model family/corpus、LR schedule confounding、200K GPU-hour复现门槛、
  random-mask seed、benchmark aggregation、router/expert specialization proxy、fine-grained/shared仅为基本extension。
- **Trade-offs / New Failure Modes:** 保留更多weights降低initial loss但保留symmetry；重置更多提高diversity却
  破坏dense function并增加recovery tokens；random slices可产生expert variance、router instability与seed sensitivity；
  upcycled optimizer/checkpoint/schema增加migration与resume identity。
- **Where the Previous Design Still Applies:** continued tokens较少时naive upcycling的initial advantage可能足够；
  新architecture/无dense checkpoint时scratch必要；明确domain experts时BTX有语义先验；shared/fine-grained MoE
  仍需专用初始化研究。
- **Evolution Relationship:** `Alternative Branch`：scratch diversity ↔ naive retention；Drop-Upcycling在两者间
  建立partial-reset branch，而非证明单向替代；`Layering / Dependency`于router、load balance与distributed expert
  execution。
- **ROADMAP Node:** `MODEL-MOE`（Current/Legacy Ch21）为主 owner；handoff到 `TRAIN-PRETRAINING`、
  `TRAIN-DISTRIBUTED-TRAINING`、`TRAIN-CHECKPOINT` 与 `INFER-TENSORRT-LLM`。
- **Target and Adjacent Chapters Read:** 已读 Ch21 MoE的router/capacity/communication主线，核对 Ch28 pretraining
  与 Ch36 distributed runtime；初始化改变expert function，不拥有All-to-All placement或Serving kernel。
- **Existing Coverage:** Ch21已有capacity-active compute、specialization/load balance与execution handoff；本论文
  提供dense→MoE initialization演进缺口，可能 refine“容量结构改变时checkpoint不是可直接复制的中性状态”。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。Historical Books Gate关闭。
- **Changed Files or Rejection Reason:** 本周只更新 Weekly；完成v1/source artifact审计并保留LR混淆边界。
- **Open Questions:** immutable event-time commit/container、exact batch/sequence/precision/topology、seed variance、
  optimizer migration、shared/fine-grained experts、capacity/EP interaction、Serving quality/latency与independent rerun。

### Kanana: A Model Family as a Versioned Capability-Production Pipeline

- **Candidate / Week / Score:** Kanana / 2025-W09 / 25/30。
- **Source Family ID:** `kanana-bilingual-staged-training-and-adaptation`。
- **Source Type:** arXiv v1 technical report + official model-weight/repository release surface；training data、
  training code与immutable run artifact未完整公开。
- **Event Date / First-public Date / Revision History:** technical report arXiv v1 2025-02-26；official repository
  records report/2.1B weights release on 2025-02-27。2024 Kakao development Blogs是predecessor lineage；Kanana 1.5
  属后续版本，不倒写进W09。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.18934；https://arxiv.org/html/2502.18934v1；
  https://github.com/kakao/kanana；official 2.1B model collection。
- **Access and Verification Status:** v1各训练阶段、data/evaluation、appendices与event-time model release identity
  已核验；official repository当前混合Kanana 1.0/1.5且只有README/weights surface，不能作为W09 training code复现。
- **Full-read Coverage:** pretraining data/filtering、staged mixture、depth up-scaling、iterative pruning/distillation、
  SFT/reward model/offline+online DPO、embedding/RAG/function calling adaptations、benchmark prompts、training
  hyperparameters、limitations，以及current official version lineage。
- **Original Problem:** underrepresented-language model既需要Korean-specific data与evaluation，又无法简单复制主流
  English model的token/parameter/training budget；同一组织还要从base checkpoint派生chat、embedding、RAG与function
  calling artifacts。问题不是一个benchmark，而是如何在固定compute下组织完整capability-production pipeline。
- **Why the Previous Design Was Reasonable:** 一次性混合全量数据、从scratch训练每个size、SFT后直接发布，
  ownership简单且各模型独立；固定reference的offline preference data也易复算。当compute充足、模型组合少、
  domain稳定或认证要求独立artifact时，这些路径仍更清晰。
- **Changed Constraint:** 只有约3T curated bilingual tokens与有限compute，却需2.1B/9.8B/32.5B portfolio及多种
  downstream adaptation；high-quality data稀缺，post-training又可能造成length/style drift。
- **Mechanism:** 先用cascaded/language-specific filters构建英韩mixture；Stage 1用2.7T diverse tokens，Stage 2
  用300B high-quality mixture；8B/26.8B经layer stacking和各200B continued tokens扩至9.8B/32.5B；8B经
  channel/head/neuron pruning与logit-KL distillation迭代压到2.1B。Post-training依次SFT、Bradley-Terry RM、
  offline DPO与asynchronous online DPO，fixed offline-DPO reference用于抑制observed length growth。
- **State Ownership:** data pipeline拥有language/domain/quality tags与mixture revision；training stage拥有checkpoint/
  scheduler/token counter；DUS/pruning mask拥有architecture lineage；teacher/student logits拥有distillation contract；
  SFT/preference/RM/reference checkpoints分别拥有post-training identity；embedding/RAG/function models是派生assets，
  不是base model同一版本别名。
- **Control Flow / Data Flow:** collected corpora → filtering/dedup/language classifiers → Stage-1 checkpoint →
  high-quality annealing/mixture search → Stage-2 checkpoint → DUS或prune/distill branches → SFT → RM selection by
  best-of-N → offline DPO → async online response sampling/DPO → separately versioned adaptation models。
- **Implementation Details:** 采用Llama 3 architecture/tokenizer但不使用其weights/outputs；pretraining加入
  independent weight decay `1e-4`与z-loss `5e-6`；PD公开batch 512、sequence 8192、LR `1.2e-4`、100-step
  warmup与final-logit KL。Online DPO保持offline-DPO reference不变，因为更新reference观察到response变长。
- **Evaluation Contract:** base models用MMLU/KMMLU/HAE-RAE、HumanEval/MBPP/GSM8K固定few-shot/greedy；
  instruct models覆盖MT/KoMT-Bench、IFEval、code/math/knowledge；embedding用英韩MTEB subsets；RAG与function
  calling使用自建bench。不同model size、base/instruct与judge不可合并为一个Pareto score。
- **Baselines / Ablations / Sensitivity / Overhead:** data quality的25B continual-pretrain对照、Stage 1/2、DUS前后、
  scratch 2.1B vs 0.3T PD、iterative compression、SFT domain removal与fixed/updating reference observation；缺少
  full factorial data×architecture×schedule、teacher-cost-inclusive distillation budget和跨seed variance。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 2.1B/8B/9.8B/26.8B/32.5B、3T/3.2T、
  PD batch/8K已部分披露；hardware/topology、precision、complete batch/LR per size、data processing FLOPs、DUS/teacher
  cost、post-training rollout concurrency、Serving latency/throughput与SLO为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者bilingual data与evaluation contract内，staged data mixture、DUS、
  PD和multi-stage post-training构成可执行的model-family生产路线；fixed reference是对observed length drift的具体
  control choice；2.1B weights提供有限artifact evidence。
- **What It Does Not Prove:** 图1只计student training FLOPs，不能证明teacher/data/filter/search/failed-run-inclusive
  lifecycle Pareto frontier；benchmark superiority不证明每个mechanism独立因果；English→Korean transfer不构成通用
  multilingual law；README/weights不能复现training pipeline。
- **Limitations / Threats to Validity:** vendor report、private data/filter details、missing training code/run manifests、
  model-family benchmark mismatch、LLM judge、teacher-cost omission、数学能力弱点、only 2.1B initial open weights、
  current 1.5 repository drift与无independent reproduction。
- **Trade-offs / New Failure Modes:** staged mixture提高late-stage quality但使data/schedule/checkpoint强耦合；DUS复用
  lower-depth knowledge但新增layer-copy symmetry与continued-training cost；prune/distill节省student tokens却引入teacher
  cost、calibration/mask lineage和能力损失；fixed reference约束length drift但会随policy distribution变旧。
- **Where the Previous Design Still Applies:** 从scratch独立训练适用于architecture/portfolio稳定性优先；single-stage
  mixture适合data分布成熟且避免selection overfit；较大dense model在deployment memory允许时减少distillation风险；
  offline DPO适用于online RM不可信或rollout成本高的场景。
- **Evolution Relationship:** `Layering / Dependency`：data control → staged pretraining → architecture transform →
  post-training → task adaptation；DUS与PD是相反方向的`Alternative Branch`，online DPO是offline DPO后的受控演进，
  不是“新阶段自动更好”。
- **ROADMAP Node:** `TRAIN-PRETRAINING`（Current Ch28；Legacy Ch24）主 owner；handoff到 `TRAIN-DATA`、
  `TRAIN-SFT`、`TRAIN-DPO`、`TRAIN-CHECKPOINT`、`PLATFORM-MODEL-REGISTRY` 与 Agent/RAG tool owners。
- **Target and Adjacent Chapters Read:** 已读 Ch27 data mixture/control-plane、Ch28 token/schedule/checkpoint主干与
  Ch34 reference/length effect；报告的RAG/function calling只作为derived asset case，不把产品能力混入base training owner。
- **Existing Coverage:** Books已有data distribution=optimization weight、training stage/checkpoint identity、DPO
  reference与length shortcut；Kanana提供model-family lifecycle的跨阶段案例，可 refine owner handoff而非追加型号清单。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。Historical Books Gate关闭。
- **Changed Files or Rejection Reason:** 本周只更新 Weekly；完成v1/report/repository lineage审计并把student-only
  FLOPs从lifecycle cost中分离。
- **Open Questions:** event-time weights/model-card checksum、training code/run manifests、data licenses/filter thresholds、
  full hardware/precision/token ledger、DUS layer map、teacher/search/failed-run cost、online DPO staleness、safety eval、
  adaptation asset lineage与independent reproduction。

### Towards Optimal Multi-draft Speculative Decoding

- **Candidate / Week / Score:** Towards Optimal Multi-draft Speculative Decoding / 2025-W09 / 27/30。
- **Source Family ID:** `optimal-transport-multi-draft-speculative-decoding`。
- **Source Type:** arXiv v1 theory/algorithm/evaluation paper；无公开official implementation artifact。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-26；后续 revision不得倒写进W09。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.18779；https://arxiv.org/html/2502.18779v1。
- **Access and Verification Status:** v1 definitions、proof route、algorithms、experiments、temperature/draft-count
  ablations、generation tests与appendices已核验；无代码/immutable run，execution evidence只来自论文。
- **Full-read Coverage:** single/multi-draft exact sampling、optimal-transport formulation、dual/TUM/subset selection、
  q-convex special cases、efficient upper-bound computation、greedy draft construction与verification、RRS/K-SEQ/
  SpecHub关系、四model/三task experiments、temperature/draft tree sensitivity、proofs与additional tables。
- **Original Problem:** 多个draft tokens可增加覆盖，却产生两个独立问题：怎样选择一个不浪费重复proposal的
  joint draft distribution，以及怎样验证并保持target distribution。现有verification与理论最优acceptance之间的
  gap过去只在小vocabulary LP上可算，无法作为真实LLM设计上界。
- **Why the Previous Design Was Reasonable:** with-replacement sampling可并行独立draw，实现简单；RRS逐个递归
  rejection保持exactness；single-draft减少tree/kernel/state complexity。Draft便宜、temperature稳定、并发高或
  implementation portability优先时，这些方案仍合理。
- **Changed Constraint:** vocabulary达数万、每步多个draft/多层tree时，full transport variables按
  `|V|^n`增长；重复draft浪费target verification slots，单看observed acceptance又无法判断是sampling还是verifier
  离理论上界更远。
- **Mechanism:** 将maximal accepted-any-draft coupling的optimal transport dual转成subset selection；利用total
  unimodularity取得binary optimum，并对with/without-replacement joint distributions用q-convex structure高效计算
  upper bound。Practical branch按draft概率贪心选择前 `n-1` tokens、最后一个随机，再用matching verifier达到该
  construction的理论acceptance。
- **State Ownership:** draft distribution拥有proposal coverage；sampling policy拥有replacement/without-replacement/
  greedy joint law；target distribution拥有最终语义；verification coupling拥有exact marginal与accepted token；runtime
  拥有tree/KV/compute budget；acceptance estimator只拥有效率证据，不拥有end-to-end SLO。
- **Control Flow / Data Flow:** prefix → draft logits → construct `n`-token proposal set → one target batched forward →
  exact verifier couples proposals withtarget distribution → accept one proposal或residual target sample → commit token/KV；
  multi-step EAGLE tree重复该过程，但paper理论主干只严格分析single-step。
- **Implementation Details:** efficient computation对常见joint distributions求 `Q(H)`与subset optimum；greedy method
  不等于argmax decode，因为最后一个draft保留随机性且verification校正target marginal。Paper在EAGLE框架模拟
  2×depth4、4×depth3与default sparse tree，但未发布实现。
- **Evaluation Contract:** Alpaca、WMT14 De-En、CNN/DailyMail各1,024 samples、max generation 128；target/draft为
  LLaMA 7B/68M、OPT 6.7B/125M、Vicuna 7B/EAGLE 0.24B、Qwen2 7B/EAGLE 0.26B；default temperature 0.7、
  3 drafts；总compute <50 RTX A6000 GPU-hours。MT-Bench tree测试另比较acceptance与generation speed。
- **Baselines / Ablations / Sensitivity / Overhead:** RRS with/without replacement、K-SEQ、SpecHub、EAGLE sparse
  tree与theoretical optimum；temperature影响非单调，greedy在高temperature可失去优势；draft count增加的边际
  acceptance不是免费，paper未给fleet concurrency/KV memory/kernel occupancy sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** RTX A6000总GPU-hour、models、128-token
  cap、temperature/drafts披露；precision、batch/concurrency、prompt/output distribution、KV footprint、TTFT/TPOT、
  target/draft placement、network与tail SLO为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 对定义的single-step MDSD，optimal acceptance可化为subset selection；
  without-replacement通常因减少重复proposal提升coverage；现有verifiers在作者real-text distributions上未达upper
  bound；draft sampling law本身是accepted progress的设计变量。
- **What It Does Not Prove:** theoretical acceptance optimum不是latency/goodput optimum；single-step proof不自动覆盖
  arbitrary tree/KV commit；greedy不是所有temperature/task最优；1.17×左右局部speed rows不构成production claim；
  无artifact不能证明implementation reproducibility。
- **Limitations / Threats to Validity:** 无显式limitations section与code、single-step theory/multi-step experiment gap、
  small sample/model set、fixed max output、temperature/domain dependence、draft/target compute未统一cost model、
  concurrency和memory omission。
- **Trade-offs / New Failure Modes:** 去重/greedy drafts提高coverage，却引入joint-sampling/verification complexity与
  less-parallel proposal construction；更多draft提高acceptance ceiling，却扩大target batch、tree/KV reservation与
  rejected work；exact verifier保护语义，但schema/numeric bug会直接破坏distribution contract。
- **Where the Previous Design Still Applies:** single draft用于low-overlap、short output或simple runtime；independent
  with-replacement适合GPU并行生成且重复概率低；RRS在implementation成熟和optimality gap小的operating point继续成立。
- **Evolution Relationship:** `Direct Evolution`：single draft → multiple independent drafts → without-replacement
  coverage → upper-bound-aware joint sampling/verifier co-design；后者优化proposal/verification contract，不替代target。
- **ROADMAP Node:** `INFER-SPECULATIVE-DECODING`（Current Ch48；Legacy Ch44）主 owner；handoff到
  `MODEL-SAMPLING`、`INFER-KV-CACHE`、`INFER-SCHEDULING`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch48 exact/lossy verification、accepted-progress cost、draft artifact与
  KV rollback主线，并核对Ch45/56；paper新增joint-draft optimality坐标，不拥有fleet admission或model quality。
- **Existing Coverage:** Ch48已经强调exact target marginal、acceptance≠goodput与proposal/verification分责；该论文
  可 refine“多个draft不是数量旋钮，而是joint distribution + verifier coupling”，不改变基本结论。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。Historical Books Gate关闭。
- **Changed Files or Rejection Reason:** 本周只更新Weekly；完成v1全文审计并明确无artifact/无production SLO。
- **Open Questions:** official code/run、multi-step exact proof、full-vocabulary complexity、KV/tree implementation、
  batch/concurrency、hardware-aware objective、draft diversity cost、numeric exactness与独立复现。

### WebGames: Hermetic Browser Tasks as Component-level Agent Evidence

- **Candidate / Week / Score:** WebGames / 2025-W09 / 26/30。
- **Source Family ID:** `webgames-hermetic-browser-agent-benchmark`。
- **Source Type:** arXiv v1 benchmark paper + official client-side environment/code + JSONL/Inspect AI evaluation surface。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-25；v1包含51 tasks。Current repository已扩展
  为150 challenges与更新model results，属于后续 benchmark revision，不倒写进W09。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.18356；https://arxiv.org/html/2502.18356v1；
  https://github.com/convergence-ai/webgames。
- **Access and Verification Status:** v1 design、tasks、tool schema、evaluation与human comparison以及current official
  environment/revision已核验；event-time commit/tag未在paper中冻结，current repo不能直接复现v1 exact suite。
- **Full-read Coverage:** five design principles/categories、client-side verifier、JSONL/Inspect integration、SoM/ReAct/
  Playwright scaffold、POMDP observation/action loop、all model/human results、51-task appendix、run instructions、
  conclusions/future metrics与current 150-task drift。
- **Original Problem:** live-web benchmarks混入network/site/account drift，端到端success又无法说明agent缺的是click、
  drag、temporal coordination、visual reading、memory还是workflow。需要可本地重放、能单独暴露interaction primitives
  且具有deterministic completion predicate的环境。
- **Why the Previous Design Was Reasonable:** live websites提供真实distribution、external state与业务语义；DOM/API
  benchmark更稳定且工具精确；final success足以做粗release gate。真实部署、API-first agent或高层workflow验证时，
  这些分支仍不可替代。
- **Changed Constraint:** multimodal computer-use agent需要比较50+异构micro-interactions，但模型action spaces、
  safety policies、scaffolds和context windows不同；若environment不冻结，失败无法复算。
- **Mechanism:** 每个challenge是client-side single-page state machine，完成后输出unique password作为deterministic
  success token；JSONL记录task spec并可接Inspect AI scorer。多数models通过Set-of-Marks截图+element list，使用
  Playwright typed tools与ReAct loop，context只保留前两次observations，直到self-declared complete或max steps。
- **State Ownership:** environment拥有DOM/game/clock/verification state；tool harness拥有action schema与browser control；
  model只提出reasoning/action；SoM preprocessor拥有可见element abstraction；completion token/scorer拥有binary
  outcome；safety policy拥有refusal，不应被误写为perception failure。
- **Control Flow / Data Flow:** reset challenge → screenshot+SoM extraction → model sees recent two observations →
  proposes typed browser action → Playwright mutates environment → deterministic challenge verifier updates/returns password →
  loop/stop → Inspect scorer checks final reported token。
- **Implementation Details:** 51 v1 tasks覆盖click/type/scroll/file/tab/iframe/canvas/WebGL/drag/hover/timing、memory/
  puzzle、workflow与games；Claude使用coordinate computer-use环境而非相同SoM scaffold。Current repo可pnpm本地运行，
  但150-task/current-model results不是v1 evidence。
- **Evaluation Contract:** v1 compares GPT-4o、Claude Computer-Use、Gemini-1.5-Pro、Qwen2-VL 7B/72B与Proxy；
  model environment/scaffold不完全一致。20名UK self-reported web-literate humans完成全套、平均约80分钟；AI表为
  binary task success与reported standard error，缺token/action/time/cost统一预算。
- **Baselines / Ablations / Sensitivity / Overhead:** human baseline、多个models、SoM/coordinate environment differences；
  没有同model跨scaffold ablation、observation-history/max-step sensitivity、repeated run reliability、difficulty/seed drift、
  action economy或latency distribution。Paper自己将这些列为future directions。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model names与two-observation context policy披露；
  exact API versions、sampling、max steps per run、image resolution、token/tool budgets、latency、hardware、concurrency、
  browser version与SLO为 `Not Disclosed`。
- **What the Evidence Actually Proves:** hermetic micro-environments能把部分browser interaction能力变成可执行unit-like
  evidence；v1显示所有被测systems在该heterogeneous harness下远未达到human success，且模型能力、action space和
  safety refusal共同决定结果。
- **What It Does Not Prove:** 41.2%不是model-alone capability；human comparison不控制action interface；password
  completion不证明路径安全/高效；microgame成功不等于live-web/business workflow可靠；current150-task结果不是W09。
- **Limitations / Threats to Validity:** intentionally adversarial task selection、public tasks/contamination、binary metric、
  heterogeneous scaffolds、small human cohort/UK filter、missing repeat runs/budgets、self-declared completion、event-time
  commit drift与缺真实site distribution。
- **Trade-offs / New Failure Modes:** hermetic environment提高复现与diagnosis，却牺牲live-web drift/auth/security；SoM
  提高grounding却改变subject；unique password易评分，却可能被source inspection/shortcut泄漏；microtasks隔离能力，
  但不能覆盖long-horizon side effects。
- **Where the Previous Design Still Applies:** live-world suites用于external dependency/robustness；DOM/API eval用于
  deterministic business tools；end-to-end workflow benchmark用于cross-capability integration；人工测试用于视觉或业务
  equivalence难形式化的cases。
- **Evolution Relationship:** `Layering / Dependency`：interaction primitive tests → hermetic component suite →
  end-to-end workflow/live-world evaluation；不是后者被前者取代。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Current Ch66；Legacy Ch62）主 owner；handoff到
  `AGENT-TOOL-CALLING`、`AGENT-WORKFLOW`、`PLATFORM-SECURITY`与`PLATFORM-TRACE`。
- **Target and Adjacent Chapters Read:** 已读Ch66 subject/environment/harness/executable evidence与agent outcome主线，
  核对Ch78 tool proposal、Ch81 workflow state；benchmark不拥有tool authorization或production release decision。
- **Existing Coverage:** Ch66已明确 model≠harness≠environment、hermetic component vs complex workflow、binary success
  边界及trajectory evidence；WebGames是高质量受限案例，但没有新增长期机制缺口。
- **Integration Decision:** `Books Pending — No Change Candidate`。后续Books审计应引用现有具体论点，而非追加
  benchmark介绍；Historical Books Gate关闭。
- **Changed Files or Rejection Reason:** 本周只更新Weekly；完整记录v1/current suite drift与heterogeneous harness边界。
- **Open Questions:** immutable v1 tag/browser/container、task-source leakage、repeat reliability、max-step/action budgets、
  matched scaffold/model comparison、trajectory/action economy、live transfer、safety-adjusted scoring与independent rerun。

### OmniAlign-V: Multimodal Preference Alignment Starts with Data Distribution

- **Candidate / Week / Score:** OmniAlign-V / 2025-W09 / 26/30。
- **Source Family ID:** `omnialign-v-multimodal-preference-data-and-dpo`。
- **Source Type:** arXiv v1 full paper + official code/data/checkpoint/benchmark repository。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-25；ACL/current artifact lineage用于核验，
  不倒写event-time results。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.18411；https://arxiv.org/html/2502.18411v1；
  https://github.com/PhoenixZ810/OmniAlign-V。
- **Access and Verification Status:** v1 dataset pipeline、SFT/DPO、benchmark、ablation、training details、licenses与
  official artifact已核验；GPT-4o/Qwen/InternVL generator/judge API revisions与event-time exact outputs未冻结。
- **Full-read Coverage:** preliminary forgetting study、task taxonomy/image filter、all generation/refinement stages、
  205K SFT/OmniAlign-V-DPO、252-item MM-AlignBench、SFT/DPO/all benchmark rows、subset/filter ablations、GPU/training
  appendix、human review与license partitions。
- **Original Problem:** vision instruction tuning常优化OCR/object/VQA短答案，却会削弱base LLM处理开放问题的
  structure、detail与helpfulness；把text-only chat data直接混回去又可能伤害multimodal skills。需要同时改变图像、
  question和answer distribution，而不是只换preference objective。
- **Why the Previous Design Was Reasonable:** traditional VQA有较客观labels、生成便宜且易评估；text-only alignment
  data复用成熟；SFT足以建立基础image→text mapping。基础感知、严格factual QA、data budget小或judge不可信时，
  这些分支仍更安全。
- **Changed Constraint:** 用户提出开放、创意、知识丰富、instruction-constrained的multimodal requests；视觉dataset
  还包含chart/diagram/poster，单一image-complexity score或一个generator容易同时产生OCR error与style bias。
- **Mechanism:** taxonomy按knowledge/inference/creative/instruction/infographic/detail组织；natural images经complexity+
  object richness双层filter；GPT-4o生成QA，creative tasks由caption→seed-question selection增加多样性；chart answers
  由GPT-4o/Qwen2VL/InternVL提取/比较facts、merge并经两名human experts review。SFT后构造chosen/rejected pairs做DPO。
- **State Ownership:** source dataset/license拥有image provenance；filter revision拥有selection；generator/prompts拥有
  synthetic QA；human review拥有有限quality adjudication；SFT/DPO datasets拥有training distribution；reference/policy
  checkpoints拥有DPO identity；MM-AlignBench rubric/judge拥有preference proxy，不拥有universal human values。
- **Control Flow / Data Flow:** source images → task-specific filter → caption/question/answer generation → instruction/
  explanation/OCR refinement → human review subsets → immutable SFT manifest → multimodal SFT → pair construction/rejection
  sampling → DPO → independent VQA + preference benchmark evaluation。
- **Implementation Details:** CLIP-L/336 visual encoder；pretrain冻结vision+LLM，batch256/LR1e-3；SFT解冻LLM，
  LLaVANext还解冻vision encoder，max 3×3 splits、batch128/LR2e-5。7B/32B runs分别用8/16/32×A800、
  12/13/24h。Paper未披露DPO完整hyperparameters与generator API budget。
- **Evaluation Contract:** 7B InternLM2.5和32B Qwen2.5 LLaVA/LLaVANext plus InternVL2-8B；MM-AlignBench、
  WildVision、MIA/MMVet/MMMU/MMBench/AI2D/OCRBench。MM-AlignBench是252 human-curated samples，以Claude3V
  reference与GPT-4o judge产生win/reward；不能当作独立human preference truth。
- **Baselines / Ablations / Sensitivity / Overhead:** LLaVANext-778K、text-only mixes、OmniAlign subsets、image filter、
  SFT vs DPO、多backbones；未做generator/judge replacement、human inter-rater、answer-length controlled judge、full
  source-by-source/license/data-size curve或matched total training compute。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** A800 counts/hours、batch/LR/image splits披露；
  precision、sequence/image token lengths、gradient accumulation、DPO batch/reference、generator calls/cost、serving
  latency/concurrency和SLO为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者LLaVA-family contract中，改变multimodal instruction distribution是
  alignment能力的前置条件，DPO在已有open-ended SFT coverage上进一步改变judge-based preference；data subsets与
  visual capability需共同评估。
- **What It Does Not Prove:** 结果不证明DPO单独因果、不证明GPT-4o judge=human preference、不证明答案更长即更正确、
  不证明所有MLLM都发生同一种catastrophic forgetting，也不证明vendor comparison跨prompt/scaffold完全公平。
- **Limitations / Threats to Validity:** generator/reference/judge同源偏好、252-sample benchmark、两名author experts、
  synthetic factual error、public-image license heterogeneity、answer-length/style confound、single architecture family、
  DPO details缺失与无独立reproduction。
- **Trade-offs / New Failure Modes:** open-ended data提高helpfulness，却增加unsupported detail/style imitation；multi-model
  fact merge降低单model OCR error，却可能形成correlated consensus；joint SFT保护capabilities但扩大data治理；DPO
  提高judge score却可能overfit rubric/length。
- **Where the Previous Design Still Applies:** objective VQA用于perception regression；text-only data保护language-only
  behavior；SFT适合preference pairs不足或judge风险高；human-authored multimodal data用于高风险领域。
- **Evolution Relationship:** `Direct Evolution`：short factual VQA SFT → open-ended task-balanced multimodal SFT →
  preference pairs/DPO；`Layering / Dependency`于representation、data lineage与evaluation judge，而非DPO替代数据。
- **ROADMAP Node:** `TRAIN-DATA`（Current Ch27；Legacy Ch23）主 owner；handoff到
  `MULTIMODAL-REPRESENTATION`、`TRAIN-SFT`、`TRAIN-DPO`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch27 synthetic data/lineage/mixture、Ch34 DPO reference/pair边界与Ch23
  multimodal training handoff；benchmark judge归Ch66，不由dataset作者定义universal preference。
- **Existing Coverage:** Books已覆盖synthetic generator/judge lineage、data distribution与DPO objective bias；该family
  可 refine“multimodal alignment先改变task/answer distribution，再谈preference objective”，不是新增dataset清单。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。Historical Books Gate关闭。
- **Changed Files or Rejection Reason:** 本周只更新Weekly；完成v1/artifact审计并分离data、objective与judge贡献。
- **Open Questions:** event-time artifact checksums、DPO config/reference、generator/judge versions/cost、length-controlled
  human evaluation、inter-rater agreement、license/delete lineage、safety slices、Serving cost与independent reproduction。

### Language Models' Factuality Depends on the Language of Inquiry

- **Candidate / Week / Score:** Language Models' Factuality Depends on the Language of Inquiry / 2025-W09 / 26/30。
- **Source Family ID:** `x-fakt-language-conditioned-factual-recall`。
- **Source Type:** arXiv v1 full benchmark paper + official generation/evaluation/result repository。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-25；current repository无release tag，W09锁定v1。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.17955；https://arxiv.org/html/2502.17955v1；
  https://github.com/kmrtanmay/X_FaKT。
- **Access and Verification Status:** v1 dataset/tasks/metrics/experiments/limitations与official scripts/results已核验；
  generated outputs和judge存在但未有immutable event-time environment/container。
- **Full-read Coverage:** dataset construction、factual/in-context/counterfactual tasks、FRS/KTS/X-FAKT formulas、14-model
  setup、4×A100 contract、all quantitative/language-group analyses、judge failure examples、limitations/ethics与repository。
- **Original Problem:** 同一fact可能在associated language可召回、换语言就失败；“模型知道这件事”若只按一个prompt/
  language判断，会把language-conditioned access误写成全局knowledge。Context还可能与strong parametric prior冲突。
- **Why the Previous Design Was Reasonable:** 单语言accuracy简单、直接，适合单一deployment locale；translated benchmark
  便于控制semantic content；parametric fact在context冲突时纠正用户有时正是安全行为。明确language contract、无
  hypothetical context或retrieval证据强时，旧方案仍合理。
- **Changed Constraint:** multilingual systems服务不同resource/script populations，RAG/context可能要求模型暂时遵循
  supplied evidence；evaluation必须分开“是否会答”“跨语言是否一致”“是否遵循当前context”。
- **Mechanism:** 802 factual items在13 languages测associated/non-associated recall；156 in-context items与1,404
  counterfactual items测context use。FRS用两类error总量，KTS用两类error差，X-FAKT取harmonic mean；temperature0
  generation后由Qwen2.5-72B judge分类，再按language/country汇总。
- **State Ownership:** benchmark source/translation拥有question semantics；language/query template拥有access path；model
  weights拥有parametric prior；prompt context拥有session evidence；judge拥有proxy verdict而非ground truth；FRS/KTS
  只拥有aggregate diagnostic，不能作为per-query confidence。
- **Control Flow / Data Flow:** fact/country/name source → 13-language prompt variants → model completion → fixed judge prompt
  → associated/non-associated/context error labels → per-language slices → FRS/KTS harmonic aggregation。
- **Implementation Details:** 14 open models；temperature0、max128 output；Qwen2.5-72B judge max256；4×A100 80GB。
  Repository包含generations/results/scripts但无release/container；translation与country-language association简化真实
  multilingual identity。
- **Evaluation Contract:** country-related facts、13 languages分high/medium/low resource；model family/size混合；t-tests
  比较associated vs non-associated error。Counterfactual task的“follow context”不总等于real-world correctness，必须
  按instruction semantics解释。
- **Baselines / Ablations / Sensitivity / Overhead:** 14 model scale/family comparison与三task类型；缺prompt paraphrase、
  translation quality/human evaluation、multiple judges、sampling/calibration、retrieval augmentation与domain transfer
  ablation。Size trend是observational，不是architecture/training-data causal law。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 4×A100 80GB、temperature/max tokens披露；
  precision/quantization、batch/concurrency、prompt lengths、latency/cost与SLO未披露。
- **What the Evidence Actually Proves:** 在该country-fact/template/judge contract中，factual access显著依赖query
  language/resource association；cross-language consistency与raw accuracy是不同维度；judge自身parametric prior可误判
  counterfactual context。
- **What It Does Not Prove:** 不证明facts物理存储在可分离“language silos”，不证明所有domain/languages，不证明大模型
  size因果改善transfer，不证明KTS/X-FAKT是calibrated confidence，也不说明模型何时应接受假context。
- **Limitations / Threats to Validity:** 13 languages、country facts、standardized templates、open models only、translation/
  association stereotypes、single model judge、metric transform choice、context truth semantics与无human adjudication。
- **Trade-offs / New Failure Modes:** 多语言consistency gate提高公平性却扩大evaluation matrix；跨语言routing/retrieval可
  找到更可靠evidence，却增加translation/provenance/latency；强parametric prior抗misinformation，却会拒绝legitimate
  hypothetical/current context。
- **Where the Previous Design Still Applies:** 单locale deployment可按本地slice评估；high-stakes facts应检索primary
  evidence而非依赖cross-language self-query；counterfactual simulation需显式task mode；规则/human judge用于simple facts。
- **Evolution Relationship:** `Direct Evolution`：single-language factual accuracy → language-conditioned recall slices →
  cross-language consistency + context-adherence matrix；不是一个harmonic score取代原始errors。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Current Ch66；Legacy Ch62）主 owner；handoff到
  `AGENT-CONTEXT`、`AGENT-RAG`、`TRAIN-DATA`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch66 language slices、factuality/confidence/judge边界与Ch75 context authority；
  RAG owner负责external evidence，benchmark metric不负责runtime abstention。
- **Existing Coverage:** Ch66已要求按language slice、judge calibration与atomic factual evidence分层；该论文可 refine
  “knowledge availability是query-interface relative”，但KTS不是confidence。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。Historical Books Gate关闭。
- **Changed Files or Rejection Reason:** 本周只更新Weekly；完成v1/artifact审计并纠正“factual metric=confidence”外推。
- **Open Questions:** translation/human audit、prompt paraphrase、multi-judge agreement、retrieval/cross-language routing、
  domain expansion、per-query calibration、context-vs-prior policy、artifact tag/container与independent reproduction。

### Rank1: Reasoning Reranking and the Cost of Verbalized Relevance

- **Candidate / Week / Score:** Rank1 / 2025-W09 / 25/30。
- **Source Family ID:** `rank1-reasoning-reranker-distillation`。
- **Source Type:** arXiv v1 full paper + official training/evaluation code + models/data/run files。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-25；current artifact提供更多model sizes，W09
  evidence锁定paper main 7B/14B/32B与specified alternatives。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.18418；https://arxiv.org/html/2502.18418v1；
  https://github.com/orionw/rank1。
- **Access and Verification Status:** v1 data/filter/training、all retrieval experiments、test-time scaling failure、quantization、
  limitations、appendices与official configs/models/data/run-files已核验；R1 teacher API outputs可下载但teacher internals未知。
- **Full-read Coverage:** 635K generation pipeline、386K filtered mix、LoRA training、BRIGHT/NevIR/mFollowIR/DL19/BEIR、
  qrel reannotation、budget forcing、alternate bases/AWQ、overthinking/inference limits、failed methods与current usage/runtime。
- **Original Problem:** first-stage retriever返回top-k后，传统pointwise classifier只输出relevance score，难处理negation、
  theorem/process similarity或user-defined relevance；listwise LLM能看更多documents但串行且昂贵。能否把teacher的
  query-passage reasoning蒸馏成可并行pointwise reranker？
- **Why the Previous Design Was Reasonable:** cross-encoder/classification head快、输出短、易batch；listwise ranking利用
  candidates间比较；BM25/dense retriever成本低。高QPS、simple relevance、short top-k或strict latency时仍更合适。
- **Changed Constraint:** reasoning-intensive retrieval与instruction-defined relevance需要更多per-passage compute；旧qrels
  未标注强model发现的新relevant documents，使score同时测model和annotation coverage。
- **Mechanism:** 用R1分别判断MS MARCO positives/easy/hard negatives并生成reasoning traces；过滤teacher与known labels
  disagreement以及student/teacher disagreement，得到386,336 samples；对Qwen2.5 base 7B/14B/32B做LoRA SFT，
  inference时对每个query-passage独立生成reasoning+binary relevance，再按score rerank top100。
- **State Ownership:** first-stage retriever拥有candidate recall；teacher trace/generation prompt拥有distillation data；filter
  拥有admission；reranker拥有pointwise relevance proposal；task-specific prompt定义relevance semantics；qrels/human
  reannotation拥有evaluation authority；RAG packer仍决定context budget。
- **Control Flow / Data Flow:** query → first-stage top100 → duplicate query per passage → Rank1 verbal reasoning/relevance →
  scalar/label ranking → top-k context；training为MS MARCO candidate→R1 trace→quality filter→LoRA checkpoint。
- **Implementation Details:** LoRA rank32/alpha64 on all parameters、LR1e-4、effective batch128、≤2 epochs/3 days，
  early stop on BRIGHT Biology+NevIR；inference 1×H100 80GB、fp16；official repo pinsvLLM0.7.2并记录batch-dependent
  nondeterminism，default context16K/max output8,192明显扩大per-passage budget。
- **Evaluation Contract:** BRIGHT top100 from BM25-on-GPT4o-CoT、NevIR、mFollowIR、DL19 top100 RepLLaMA、BEIR top100
  BM25S；metrics多为nDCG。DL19额外人工relabel295 top10 cases；paper没有统一latency/cost matched baseline。
- **Baselines / Ablations / Sensitivity / Overhead:** BM25、mE5、MonoT5、RankLLaMA、FollowIR、limited listwise rows；
  base family/scale、AWQ、data filters、budget forcing。关键反证：强行增加test-time tokens平均使结果更差，说明
  “reasoning reranker”不等于compute单调有效；BEIR总体低于traditional baselines。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** main models、1×H100 80GB、fp16、LoRA config
  披露；teacher generation hardware/cost、per-query top-k concurrency、actual output lengths、latency distribution、GPU
  memory/energy与SLO未披露。
- **What the Evidence Actually Proves:** teacher reasoning traces可在该MS MARCO/LoRA contract中训练pointwise reranker，
  并改善若干reasoning/instruction retrieval slices；更强reranker暴露旧qrels coverage问题；额外verbalized compute的
  边际价值依赖task difficulty，不能盲目budget-force。
- **What It Does Not Prove:** reasoning chain不等于faithful explanation；benchmark gains不证明RAG answer improvement；
  qrel reannotation由作者触发可能有selection bias；AWQ model size缩小不等于latency等比缩小；不证明all retrieval应
  使用generative reranker。
- **Limitations / Threats to Validity:** proprietary R1 teacher、self-filter confirmation bias、MS MARCO-only training、
  pointwise independence、old qrel noise、authors' reannotation、missing matched compute、slow long outputs、vLLM nondeterminism。
- **Trade-offs / New Failure Modes:** verbal reasoning提高复杂relevance表达，却把top-k成本乘以generated tokens；teacher
  trace传递bias；task prompt提高adaptation却扩大prompt-injection/definition drift；quantization省memory但改变ranking。
- **Where the Previous Design Still Applies:** BM25/dense retriever做high-recall first stage；cross-encoder用于low-latency
  relevance；listwise用于小candidate set且relative comparison重要；non-generative classifier用于高QPS。
- **Evolution Relationship:** `Layering / Dependency`：retriever → classifier reranker → reasoning pointwise reranker →
  context packer；`Alternative Branch`而非单向替代，且test-time token budget存在负收益区。
- **ROADMAP Node:** `AGENT-RAG`（Current Ch76；Legacy Ch72）主 owner；handoff到 `TRAIN-SFT`、
  `INFER-SCHEDULING`、`PLATFORM-COST`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch76 online retrieval/rerank/budget/sufficiency主线，核对Ch29 SFT、Ch56
  scheduling与Ch66 qrel/evidence contract；reranker只排序candidate，不拥有answer correctness。
- **Existing Coverage:** Ch76已说明LLM reranker提高interaction precision但增加latency/cost、evaluation必须绑定query/
  corpus/reranker/packer；Rank1提供“verbalized reasoning可有负边际compute”的case，未形成新机制缺口。
- **Integration Decision:** `Books Pending — No Change Candidate`。后续只需确认现有论点，不追加模型清单。
- **Changed Files or Rejection Reason:** 本周只更新Weekly；完成v1/artifact审计并保留budget-forcing反结果与qrel drift。
- **Open Questions:** teacher cost/version、trace faithfulness、latency/goodput per top-k、matched-compute baselines、qrel
  adjudicator agreement、RAG end-to-end effect、online update、prompt injection与independent reproduction。

### DeltaBench: Long Reasoning Makes Critique an Evidence-retrieval Problem

- **Candidate / Week / Score:** DeltaBench / Can LLMs Detect Errors in Long CoT? / 2025-W09 / 26/30。
- **Source Family ID:** `deltabench-long-cot-error-detection`。
- **Source Type:** arXiv v1 full benchmark paper + official section-level dataset/evaluation repository；full labeled data
  于2025-03-05发布，是后续artifact node。
- **Event Date / First-public Date / Revision History:** paper v1 2025-02-26；dataset release 2025-03-05属于W10 artifact
  lineage，不倒写为W09可用artifact。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.19361；https://arxiv.org/html/2502.19361v1；
  https://github.com/LivingFutureLab/DeltaBench。
- **Access and Verification Status:** v1 construction、annotation、all analyses/evaluations、limitations与current artifact已
  核验；paper event时dataset未公开，compute/runtime contract未披露。
- **Full-read Coverage:** query clustering/difficulty filtering、long-CoT generation/section split、domain correctness checks、
  multi-stage human annotation、useful/correct/reflection/error taxonomy、PRM/critic metrics、length/error/self-critique
  analyses、appendices、annotation cost/personnel与artifact release chronology。
- **Original Problem:** final-answer correctness无法定位long reasoning中第一个或全部错误；step-level切分过细且标注昂贵；
  PRM threshold来自短math steps时，迁移到1K～7K+ token multi-domain traces可能失效。
- **Why the Previous Design Was Reasonable:** outcome verifier便宜且直接；step PRM适合短、结构明确的math reasoning；
  self-critique无需额外model。final answer可执行、trace短或只需release verdict时旧方案仍足够。
- **Changed Constraint:** o1-like models生成长、反复、自我修正的CoT，包含多个subtasks与冗余；模型/PRM既要找错，
  又要区分strategy shift、usefulness、correctness和effective reflection。
- **Mechanism:** 从多领域queries经embedding dedup、difficulty/subcategory sampling选题，用QwQ/R1/Gemini Thinking生成
  traces；先按blank-line切steps，再由GPT-4聚合成semantic sections；rules/sandbox/LLM做预核验，domain experts逐
  section标注。Critic一次指出所有error sections，PRM按per-dataset z-score或HitRate@k排序低reward sections。
- **State Ownership:** source query/test拥有task truth；generator拥有trace；section splitter拥有analysis granularity；human
  annotators+domain verifier拥有labels；critic/PRM只拥有error proposals/scores；outcome/executable verifier仍拥有final
  correctness；benchmark version拥有comparison population。
- **Control Flow / Data Flow:** query → long-CoT generator → section segmentation → domain pre-verification → multi-reviewer
  labels/error corrections → critic full-trace或PRM section scores → precision/recall/F1/HitRate slices → diagnosis。
- **Implementation Details:** 1,236 samples、48 subcategories；每unit annotation约$15，三initial annotators、两junior reviewers、
  five spot-check staff与overlap QA；programming用SandboxFusion+LLM，PCB/general mostly LLM judge。PRM threshold
  `mu-sigma`是benchmark-relative，不是production calibrated error probability。
- **Evaluation Contract:** long traces来自QwQ-32B-Preview、DeepSeek-R1、Gemini2 Flash Thinking；critics/PRMs跨math/code/
  PCB/general评估。Top critic macro-F1约40.8%；critic随4–7K长度下降，PRM较稳定但absolute F1更低。无统一
  inference budget、API versions、hardware、cost或repeat variance。
- **Baselines / Ablations / Sensitivity / Overhead:** multiple PRMs/critics、length bins、error types、HitRate@1/3/5与
  self-vs-cross critique；缺section-split alternative、annotator agreement numeric、threshold calibration、external-feedback/
  tool critic、matched token budget与live-data drift tests。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** trace length bins/model names披露；generation/
  evaluation hardware、precision、sampling details、batch/concurrency、judge tokens/latency/cost与SLO为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在该section-level human-labeled contract中，long-trace error detection远未可靠；
  reasoning-model身份/size不保证critique；self-critique可能显著弱于cross-model critique；PRM rank signal与binary error
  classification必须分开。
- **What It Does Not Prove:** 公开CoT等于internal faithful reasoning、40.8%是所有critic上限、reflection causally useless、
  longer reasoning总体有害、section labels完全客观，或PRM不能用于candidate ranking。
- **Limitations / Threats to Validity:** static/expensive small benchmark、subjective sections/labels、generator-specific traces、
  LLM-assisted filtering/splitting、PCB/general judge proxy、artifact晚于paper、missing compute与possible contamination。
- **Trade-offs / New Failure Modes:** section granularity降低annotation burden却隐藏within-section first error；full-trace critic
  有global context但随length衰退；PRM可逐section扩展却依赖distribution threshold；self-critique便宜但correlated blind spot。
- **Where the Previous Design Still Applies:** executable outcome verifier用于math/code final authority；short-step PRM用于局部
  ranking；independent critic用于高风险review；human/domain expert用于开放科学/知识错误。
- **Evolution Relationship:** `Direct Evolution`：final outcome → step score → semantic section diagnosis → typed error/
  reflection evidence；后者增加diagnosis，不替代outcome truth。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Current Ch66；Legacy Ch62）主 owner；handoff到
  `AGENT-REFLECTION`、`TRAIN-RLHF`、`TRAIN-GRPO`与`PLATFORM-COST`。
- **Target and Adjacent Chapters Read:** 已读Ch66 trajectory/first-error/judge证据主线，核对Ch80 reflection与Ch31/33
  reward ownership；critic verdict不能自动成为training/release authority。
- **Existing Coverage:** Ch66已区分trajectory narrative、action/environment evidence、first error与judge calibration；
  DeltaBench可 refine“long trace使critique成为budgeted evidence localization”，不支持模型排行榜正文。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。Historical Books Gate关闭。
- **Changed Files or Rejection Reason:** 本周只更新Weekly；分离W09 paper event与W10 dataset artifact release。
- **Open Questions:** event-time dataset/commit、API/model revisions、compute/tokens/cost、section alternative、agreement、
  contamination、external-tool critic、calibration、hidden-CoT applicability与independent reproduction。

### Agentic Reward Modeling: Reward Is a Routed Evidence System, Not One Scalar Model

- **Candidate / Week / Score:** Agentic Reward Modeling / 2025-W09 / 27/30。
- **Source Family ID:** `rewardagent-routed-preference-and-verifier-signals`。
- **Source Type:** arXiv v1 full system paper + official router/verifier/judger code and IFBench artifact。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-26；ACL/current repo只作lineage。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.19328；https://arxiv.org/html/2502.19328v1；
  https://github.com/THU-KEG/Agentic-Reward-Modeling。
- **Access and Verification Status:** v1 architecture、prompts、benchmarks、ablation、Best-of-N、DPO、limitations与official
  artifact已核验；Google search/API results、model endpoints与event-time commit未冻结。
- **Full-read Coverage:** reward preliminaries、router、factuality pairwise/query/evidence/verification workflow、generated-code
  hard-constraint checker/refinement、weighted judger、RM/Judge/IFBench、router/verifier ablations、oracle route、32-sample
  search、UltraFeedback/on-policy DPO、appendices与artifact。
- **Original Problem:** monolithic RM容易偏好verbosity/style，忽略factuality与hard constraints；单一rule verifier只覆盖
  窄domain。需要让不同evidence sources按instruction选择、独立评分，再显式组合，而不是假设一个latent scalar已经包含
  所有“好”。
- **Why the Previous Design Was Reasonable:** scalar RM便宜、统一、可微且易用于RL/DPO/Best-of-N；rule checker在formal
  tasks可靠；LLM judge覆盖开放语义。单一维度、低风险、低latency或verifier不可构造时仍合理。
- **Changed Constraint:** open responses同时含subjective preference、atomic facts与machine-checkable constraints；不同
  prompts需要不同verifier，错误router或噪声retrieval会比base RM更差。
- **Mechanism:** router判断调用哪些verification agents；factuality agent做pairwise claim差异→queries→parametric/search
  evidence→verification；instruction agent抽取hard constraints、生成并迭代修复Python checker后执行；judger以base RM+
  verifier scores等权求和。结果用于Best-of-32 selection或构造highest/lowest DPO pairs。
- **State Ownership:** base RM拥有人类preference proxy；router拥有evidence-plan proposal；factuality search/claim verifier
  拥有事实proxy；generated code checker拥有encoded constraint而非instruction truth；sandbox拥有execution；judger拥有
  aggregation policy；external held-out eval拥有最终decision evidence。
- **Control Flow / Data Flow:** instruction+candidate pair → router → selected factual/constraint agents → claim/query/search或
  code generation/refinement/execution → typed component scores → weighted judger → reward/rank → Best-of-N或DPO pair →
  independently evaluated policy。
- **Implementation Details:** base ArmoRM；GPT-4o-mini backbone或Llama3-8B，constraint coder为Qwen2.5-Coder-7B；
  weights全部1.0。Factuality可用parametric knowledge或Google API，后者在部分bench反而降低结果；oracle routing显著
  优于learned router，暴露planner仍是瓶颈。
- **Evaluation Contract:** RM-Bench chat、JudgeBench knowledge、synthetic IFBench 47/133/264 simple/normal/hard pairs；
  Best-of-N在TriviaQA/IFEval/CELLO，每prompt32 responses、temperature1；DPO用Zephyr7B SFT、UltraFeedback或20K
  on-policy instructions×8 responses，评MMLU/Trivia/Truthful/IFEval/CELLO/MT-Bench。
- **Baselines / Ablations / Sensitivity / Overhead:** multiple RMs/generative judges、remove each verifier、single-LLM ensemble、
  oracle routing、parametric vs search、UF vs on-policy pairs；缺weights/routing threshold sensitivity、retrieval quality、
  code sandbox security、equal-call/token cost、reward hacking underpolicy shift与human factual audit。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** component models和sample counts披露；GPU、precision、
  prompt/output lengths、parallel calls、Google latency/cost、code execution budget、training batch与tail SLO未披露。
- **What the Evidence Actually Proves:** 在其three-benchmark/Best-of-N/DPO contracts中，routed specialized checking比
  base RM或simple ensemble更有效；verifier selection是独立problem；external search不是自动提升；component reward可
  改变downstream pair distribution。
- **What It Does Not Prove:** generated checker/factuality agent是ground truth、equal weights通用、72.5%足以自动训练/
  release、高benchmark score免疫reward hacking、较小component stack一定更便宜，或agentic naming意味着自治。
- **Limitations / Threats to Validity:** only factuality+hard constraints、LLM-generated IFBench/checkers、same-family model
  bias、search noise、oracle-route gap、no threat model/sandbox details、average score掩盖slices、closed API drift与无
  policy-shift adversarial evaluation。
- **Trade-offs / New Failure Modes:** typed verifier提高diagnosis与correctness coverage，却增加router error、tool/API cost、
  evidence injection、checker bugs、score calibration/weight conflict；monolithic RM较盲但latency/operability更简单。
- **Where the Previous Design Still Applies:** exact rule/executable verifier直接拥有formal truth；scalar RM用于subjective
  style/helpfulness；human review处理开放高风险facts；offline fixed pairs适合无可靠online evidence acquisition。
- **Evolution Relationship:** `Direct Evolution`：single preference RM → RM ensemble → routed typed verifiers + explicit
  aggregation；`Layering / Dependency`于retrieval/tool sandbox/evaluation，不是一个更大RM的同义词。
- **ROADMAP Node:** `TRAIN-RLHF`（Current Ch31；Legacy Ch27）主 owner；handoff到 `TRAIN-DPO`、
  `PLATFORM-EVALUATION-SYSTEM`、`AGENT-WORKFLOW`、`AGENT-TOOL-CALLING`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch31 reward/preference pipeline、Ch34 pair construction、Ch66 scorer/evidence
  authority与Ch81 workflow；RewardAgent产生training signal，不拥有deployment truth。
- **Existing Coverage:** Books已覆盖reward≠truth、verifier/tool/evidence分层与judge hacking；该论文可 refine“reward
  由routed evidence plan生成，router/aggregation也需版本化”，不追加benchmark numbers。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。Historical Books Gate关闭。
- **Changed Files or Rejection Reason:** 本周只更新Weekly；完成v1/artifact审计并记录search负结果与oracle-route gap。
- **Open Questions:** immutable commits/endpoints、full cost/latency、weights calibration、router uncertainty、claim extraction
  recall、retrieval poisoning、sandbox isolation、policy-shift red team、human audit与independent reproduction。

### VEM: Frozen Offline Value as an Environment Proxy for GUI Policy Training

- **Candidate / Week / Score:** VEM: Environment-Free Exploration for Training GUI Agent / 2025-W09 / 26/30。
- **Source Family ID:** `vem-offline-gui-value-environment-model`。
- **Source Type:** 20-page arXiv v1 PDF + official Microsoft code/config/data-preprocess/offline-online evaluation artifact。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-26；current repository用于核验，未见immutable release tag。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.18906；https://arxiv.org/pdf/2502.18906v1；
  https://github.com/microsoft/GUI-Agent-RL。
- **Access and Verification Status:** HTML不可用；已完整读取同ID v1 PDF的Method、theory、experiments、appendices与official
  implementation。Paper无独立limitations section，相关边界从coverage assumptions、judge/eval与experiments恢复。
- **Full-read Coverage:** environment/offline/world-model baselines、MDP/Q formulation、GPT-4o value annotation、Qwen2VL
  VEM regression、frozen-value PPO、coverage/performance bound、AITW data/config、offline/online results、training stability、
  action/prompt/proof appendix与code quick-start。
- **Original Problem:** online GUI RL需要真实device rollouts和rewards，昂贵且有副作用；next-state world model在长trajectory
  复合误差；plain offline imitation缺exploration且distribution shift严重。能否不预测next screen，只估计某action是否
  推进目标？
- **Why the Previous Design Was Reasonable:** online environment reward最接近真实outcome；world model支持planning；SFT
  从human demonstrations稳定。环境可复现、interaction便宜、安全且需要recovery learning时，online/hybrid仍更可信。
- **Changed Constraint:** UI layout频繁变化，真实rollout昂贵，offline dataset只覆盖behavior-policy actions；policy仍需尝试
  dataset中未明确示范但语义上合理的actions，reward/value proxy必须跨视觉变化泛化。
- **Mechanism:** GPT-4o根据task、history、screenshot、candidate action生成binary beneficial/suboptimal labels；Qwen2VL SFT
  回归成frozen `Q_theta(s,a)`；Auto-GUI policy从offline states采样candidate actions，用PPO最大化VEM score，而不调用
  environment/next-state simulator。理论bound显式依赖Q近似误差与policy离behavior support距离。
- **State Ownership:** offline AITW trajectory拥有observed state/action；GPT-4o label是surrogate preference；VEM拥有fixed
  value proxy；policy拥有action distribution；real Android environment/GPT-4o online judge拥有deployment outcome；coverage
  assumption不是runtime guard，需另做OOD/admission。
- **Control Flow / Data Flow:** offline trajectories/screenshots → GPT-4o pair labels → Qwen2VL critic/VEM training → freeze
  VEM → sample offline state + policy actions → VEM scores/advantages → PPO policy update → offline exact-action evaluation →
  bounded online Android evaluation。
- **Implementation Details:** General 436 train episodes/3,340 steps，WebShopping 560/6,240；VEM 8×A100、10 epochs、
  global batch64、AdamW LR1e-5、12h；policy full-parameter single A100、batch32、LR1e-6、5 epochs、<8h。Repo称
  critic使用LoRA，与paper“full policy/frozen critic”需分开，不能把两者混成一个parameter-efficiency claim。
- **Evaluation Contract:** AITW General/WebShopping；offline按human action match算Step/Task SR；online为real Android、
  max10 steps、dedup tasks、GPT-4o automated judge。VEM自身F1/accuracy约0.79/0.71 General、0.80/0.75 WebShopping；
  online WebShopping只有14.29%且多baselines相同，样本很小/离散。
- **Baselines / Ablations / Sensitivity / Overhead:** GPT-4o、Auto-GUI、CogAgent、SeeClick、DigiRL offline/online；paper
  提供training curves/cases但缺VEM removal/random labels、teacher replacement、coverage/OOD、policy-distance constraint、
  seed variance、online task count confidence与matched environment-interaction cost。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** A100 counts/hours、batch/epochs/LR披露；precision、
  screenshot/token length、rollout generation batch、online latency/cost、device/app versions、concurrency与SLO未披露。
- **What the Evidence Actually Proves:** 在该AITW subset与GPT-4o-labeled proxy下，frozen semantic state-action scorer可为
  offline policy提供比plain imitation更细的credit，并在小规模online eval达到可比较结果；Q approximation与coverage是
  机制成立的必要条件。
- **What It Does Not Prove:** VEM是environment model或真实Q*、binary immediate judgement等于long-term return、完全消除
  distribution shift、对任意UI layout agnostic、比online RL通用更优，或GPT-4o judge/result独立于training teacher。
- **Limitations / Threats to Validity:** teacher/judge coupling、binary coarse labels、no explicit OOD guard、support theorem假设
  不可直接验证、two AITW domains、小online sample、exact-action offline metric、no explicit limitations section、artifact无tag。
- **Trade-offs / New Failure Modes:** 不预测next-state避免compounding error，却失去transition/side-effect modeling；frozen
  value稳定但会stale/reward-hack；offline安全便宜但coverage受限；semantic score抗layout change却可能忽略pixel/action precision。
- **Where the Previous Design Still Applies:** online RL用于真实recovery/side effects；world model用于counterfactual planning；
  SFT用于高质量demonstrations；hybrid offline→online calibration用于VEM uncertainty高或action超support。
- **Evolution Relationship:** `Alternative Branch`：online environment reward ↔ next-state simulation ↔ frozen semantic value
  proxy；不是environment-free单向替代environment-based，真实deployment evaluation仍是authority。
- **ROADMAP Node:** `TRAIN-PPO`（Current Ch32；Legacy Ch28）主 owner；handoff到 `TRAIN-RLHF`、
  `AGENT-TOOL-CALLING`、`AGENT-WORKFLOW`、`PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch32 value/advantage/PPO与reward-correctness边界，核对Ch78/81 action/environment
  ownership和Ch66 offline/online eval；VEM替换reward/value source，不拥有environment truth。
- **Existing Coverage:** Ch32已有value error污染policy和reward correctness分层；VEM可 refine“frozen offline value降低
  variance但把support/staleness变成首要failure”，不支持写成GUI产品清单。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。Historical Books Gate关闭。
- **Changed Files or Rejection Reason:** 本周只更新Weekly；通过PDF+official artifact恢复blocked HTML来源。
- **Open Questions:** immutable event-time commit/models、online task counts/CI、teacher/judge independence、VEM calibration/
  OOD abstention、policy support constraint、side-effect safety、latency/cost、hybrid online correction与independent rerun。

### CritiQ: Data Quality Criteria as a Versioned Learned Specification

- **Candidate / Week / Score:** CritiQ: Mining Data Quality Criteria from Human Preferences / 2025-W09 / 27/30。
- **Source Family ID:** `critiq-human-pair-to-quality-criteria-and-scorer`。
- **Source Type:** 21-page arXiv v1 PDF + official CritiQ Flow/scorer code；knowledge base因source licenses未发布。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-26；official code 2025-03-07属于W10 artifact
  release，不倒写为W09可执行状态。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.19279；https://arxiv.org/pdf/2502.19279v1；
  https://github.com/KYLN24/CritiQ。
- **Access and Verification Status:** v1 Method、all experiments/analysis、hyperparameters、annotation/criteria prompts、limitations
  与current code已核验；event-time code未公开，knowledge-base artifact不可取得，完整replication仍受阻。
- **Full-read Coverage:** heuristic/LLM quality signals、knowledge-base retrieval、manager criteria evolution/reflection、worker
  pairwise voting、Bradley-Terry scorer、temperature/Gumbel selection、human agreement、ablation、10B/3B-token continual
  pretraining、criteria/voting analyses、all appendices与license/artifact gap。
- **Original Problem:** static heuristics、perplexity/classifier或handwritten“educational quality”把专家偏好固化成不可解释/
  domain-specific filters；全量human labels昂贵。如何从约30个pair comparisons恢复可读criteria，再扩展到corpus scoring？
- **Why the Previous Design Was Reasonable:** deterministic heuristics快、可审计；perplexity提供model-relative fluency；
  trained classifier稳定；人工rubric适合成熟domain。规模极大、latency敏感、法规明确或human pairs太少时仍更合适。
- **Changed Constraint:** code/math/logic的“quality”含不同dimensions，单一criterion跨domain失效；LLM pairwise judging昂贵，
  但criteria若能显式化可供小scorer蒸馏与后续治理。
- **Mechanism:** 从human `D_human` 25–30 pairs启动；knowledge base检索previous-work criteria；20 worker agents分别按criterion
  pairwise判断并majority vote；manager根据train accuracy/wrong cases迭代保留、修订、生成criteria并记录bad-criteria memo；
  final criteria给25K random pairs打labels，训练Qwen2.5-1.5B Bradley-Terry scorer；score经temperature exponential+
  Gumbel top-k无放回采样构建训练subset。
- **State Ownership:** human pairs拥有local preference anchor；knowledge base拥有prior criteria/provenance；manager拥有criteria
  revision proposal；workers拥有pair votes；threshold/voting policy拥有selection；scorer拥有distilled proxy；corpus manifest与
  downstream training/eval拥有最终data utility evidence。
- **Control Flow / Data Flow:** source corpus → sample human pairs → retrieve/generate criteria → worker pair votes → manager
  reflection/evolution → final criteria/version → label25K pairs → train scorer → score corpus → temperature sampling → immutable
  subset → continual pretraining → downstream evaluation。
- **Implementation Details:** manager GPT-4o-2024-11-20，workers Qwen2.5-72B-Instruct，scorer Qwen2.5-1.5B；20 criteria、
  3–5 iterations、manually chosen thresholds；scorer LR2e-5/4 epochs/max32K/global batch128。Continual pretraining Llama3.1-3B，
  8K、4M-token global batch、4 epochs、32×H800，code/logic10B、math3B tokens。
- **Evaluation Contract:** Stack v2 Python、OpenWebMath non-code、Zyda-2；human test pairs只保留3 annotators unanimous cases
  （193/70/134）；continual pretraining评HumanEval/MBPP(+)、GSM8K/SAT-Math/MATH、ARC-C/LogiQA。与uniform/raw比，
  未与equal-cost strong classifier/QuRating完整downstream比较。
- **Baselines / Ablations / Sensitivity / Overhead:** vanilla worker prompt、TextGrad、QuRating single criteria；remove knowledge
  base/evolution、criteria distribution、iteration/majority voting。缺human-pair count curve、manager/worker replacement、
  threshold/temperature sensitivity、random seeds、full selection rate/corpus scan cost和from-scratch scale。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** H800 count、tokens、sequence/batch/LR披露；manager/
  worker inference hardware、API/token cost、precision、corpus size/selection ratio、throughput/energy与SLO未完整披露。
- **What the Evidence Actually Proves:** 在三个domain与small human anchor下，criteria evolution+voting能提高held-out unanimous
  pair agreement，distilled scorer选出的subset在作者3B continual-pretraining contract中优于uniform；criteria是可版本化的
  learned data specification，而非universal truth。
- **What It Does Not Prove:** 30 pairs足以任意domain、criteria消除human/LLM bias、agreement等于model utility、scorer跨corpus/
  model稳定、continual gains由每个criterion独立导致，或10B/3B结果外推到full pretraining/frontier scale。
- **Limitations / Threats to Validity:** authors annotate and benefit、unanimous-only test selection、three domains、closed GPT-4o
  manager、missing knowledge base/license、manual hyperparameter search、small 3B continual model、no from-scratch/seed variance、
  event-time artifact absent。
- **Trade-offs / New Failure Modes:** learned criteria降低manual rubric effort，却会overfit30 pairs；multiple workers提高agreement
  但共享model blind spot且成本高；distillation便宜却冻结criteria drift；top-score selection会收窄diversity，所以temperature
  sampling保留coverage但引入policy choice。
- **Where the Previous Design Still Applies:** deterministic filters用于safety/license/syntax；perplexity用于distribution outlier；
  human rubric用于高风险domain；uniform mixture保留未知diversity；continuous feedback用于criteria drift。
- **Evolution Relationship:** `Direct Evolution`：handwritten heuristic → LLM fixed rubric → human-anchored evolving criteria →
  distilled scorer + stochastic selection；后者增加specification lifecycle，不替代hard policy filters。
- **ROADMAP Node:** `TRAIN-DATA`（Current Ch27；Legacy Ch23）主 owner；handoff到 `TRAIN-PRETRAINING`、
  `TRAIN-CHECKPOINT`、`PLATFORM-EVALUATION-SYSTEM`、`AGENT-WORKFLOW`与`PLATFORM-COST`。
- **Target and Adjacent Chapters Read:** 已读Ch27 quality/filter/synthetic judge/lineage与mixture主线，核对Ch28 pretraining、
  Ch81 workflow与Ch66 evaluation；scorer selection不拥有license/safety或downstream truth。
- **Existing Coverage:** Ch27已有quality filter是versioned policy、generator/judge lineage与sampling coverage；CritiQ可 refine
  “criteria自身是可演化artifact，hard filters与soft learned quality必须分层”，不加入具体阈值配方。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。Historical Books Gate关闭。
- **Changed Files or Rejection Reason:** 本周只更新Weekly；通过PDF恢复全文并记录W09 paper/W10 code release边界。
- **Open Questions:** event-time code/knowledge-base snapshot、pair-count/seed sensitivity、annotator agreement beyond unanimous、
  criteria drift/delete、manager/worker cost、selection diversity、cross-domain/model transfer、from-scratch scale与independent rerun。

### Training LLMs with MXFP4: Unbiased Gradients Are Necessary but Not Sufficient

- **Candidate / Week / Score:** Training LLMs with MXFP4 / 2025-W09 / 28/30。
- **Source Family ID:** `mxfp4-stochastic-rounding-hadamard-backward-training`。
- **Source Type:** arXiv v1 full theory/experiment paper + immutable Megatron-LM/microxcaling commit references；无论文专用
  implementation artifact，且无真实MXFP4 hardware wall-clock run。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-27；后续hardware/software支持只作lineage。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.20586；https://arxiv.org/html/2502.20586v1；
  https://github.com/microsoft/microxcaling/tree/7bc41952de394f5cc5e782baf132e7c7542eb4e4；
  Megatron-LM commit `a4ad305d4b117217141730b9b18af52dda069450`。
- **Access and Verification Status:** v1 math、algorithms、all GPT runs/ablations、proxy overhead、appendices/proofs与immutable
  dependency revisions已核验；paper没有code release和limitations section，真实FP4 speedup保持`Estimated / Not Verified`。
- **Full-read Coverage:** IEEE/MX formats、mixed precision/SR、unbiased scaling proof、RHT variance theorem/blockwise construction、
  345M/1.3B/6.7B and 210B-token runs、RHT/SR/block-size/FP8-forward ablations、INT4/INT8/H100/A100/Trainium proxy、
  exact configs/commits与proof appendices。
- **Original Problem:** MXFP4 block scale扩大dynamic range，却仍因clipping/nearest rounding产生biased gradients；stochastic
  rounding消除expectation bias但outliers让variance很高，小gradients还会随机flush to zero。低bit训练必须同时控制bias、
  variance与hardware overhead。
- **Why the Previous Design Was Reasonable:** BF16成熟、数值稳定且跨hardware；FP8用forward/backward不同formats平衡range/
  precision；nearest rounding deterministic且便宜。没有native FP4/SR、模型小、reliability优先或RHT overhead无法融合时，
  BF16/FP8仍更合理。
- **Changed Constraint:** 最新accelerators承诺MXFP4 GEMM吞吐，backward占decoder linear layer三次GEMM中的两次；要取得收益，
  recipe不能让quality loss抵消更多steps，也不能因跨DP batch dimension的full RHT引入collective bottleneck。
- **Mechanism:** 每32-value MX block先按max exponent缩放；为避免FP4最大值6被6–8区间clipping，额外乘3/4并用independent
  dithering SR，GEMM accumulator再乘16/9恢复unbiased expectation。对gradient/activation/weight在reduction-local `g=64`
  blocks施加random-sign Hadamard transform，集中outliers、把variance对block size的linear dependence压到log-level；只在
  backward decoder linears使用MXFP4，forward仍BF16/可选FP8，master weights保持FP32。
- **State Ownership:** high-precision master weights/optimizer拥有parameter truth；quantization policy拥有format/block/scale；
  RNG stream拥有SR/RHT signs与reproducibility；kernel/compiler拥有fusion/overhead；distributed runtime拥有shard boundaries；
  validation/convergence拥有quality gate，unbiased theorem不拥有wall-clock/perplexity guarantee。
- **Control Flow / Data Flow:** BF16/FP8 forward → loss → backward gradient/activation/weight blocks → random sign+Hadamard →
  3/4 scaling + stochastic MXFP4 quantization → FP4 GEMM → high-precision accumulator×16/9 → optimizer/master-weight update。
- **Implementation Details:** blockwise RHT避免跨data-parallel batch mixing；`g<=256`预期memory-bound，paper主run `g=64`。
  Megatron mixed precision保留FP32 master/BF16 copies；GPT 345M/1.3B/6.7B contexts 1K/2K，gradient clip1.0；AWS P4/G6e、
  NVIDIA PyTorch Ubuntu24.04、Transformer Engine1.5用于FP8。
- **Evaluation Contract:** GPT2-Wikipedia、345M/1.3B/6.7B，20–42B tokens，另1.3B 210B；validation perplexity与少量
  zero-shot/Tulu2 fine-tune。MXFP4仅emulated bit-accurately；20B短run可由RHT或SR单独接近BF16，但210B显示无SR的
  biased path出现约0.1 PPL gap。
- **Baselines / Ablations / Sensitivity / Overhead:** BF16、pure MXFP4、RHT-only、SR-only、RHT+SR、FP8 forward、RHT
  g32/64/128/256；proxy throughput用A100 INT4/INT8 Llama2-70B decoder、H100 FP8 RHT kernels和Trainium1 BF16 SR。
  没有native MXFP4 end-to-end wall clock、multi-node communication、seed variance或frontier-scale convergence。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** training model/config/instances披露；speed proxy为
  A100/H100/Trainium不同hardware与INT4/INT8/FP8/BF16不同datatypes。Headline 1.3×/1.7×是backward estimate，不是
  same-system native MXFP4 production measurement；energy/failure/recovery/SLO未披露。
- **What the Evidence Actually Proves:** 在emulated MXFP4 backward与作者GPT contracts内，nearest/pure FP4显著伤害
  convergence，SR提供unbiased expectation，RHT降低variance/early information loss，两者在长run各有必要角色；
  block-local transform避免full-DP communication。
- **What It Does Not Prove:** unbiased gradient等于BF16 trajectory、native FP4必得headline speedup、RHT overhead可完全
  fusion、所有layers/models/optimizers适用、forward FP4 near-lossless，或20–210B token结果外推trillion-token/frontier scale。
- **Limitations / Threats to Validity:** no native FP4 hardware/code release/explicit limitations、emulation、heterogeneous proxy
  devices、small GPT/data domain、few seeds/not disclosed、backward-only、short 6.7B run、missing distributed topology/
  communication/failure evidence。
- **Trade-offs / New Failure Modes:** 更低bit减少GEMM cost却增加RNG、transform、scale/accumulator与kernel specialization；
  SR消bias却增variance/nondeterminism；RHT降variance却mixes coordinates、需版本化RNG/block layout并可能增加memory traffic；
  block-local避免collective但concentration较弱。
- **Where the Previous Design Still Applies:** BF16用于portability/stability；FP8用于已有hardware/software与full forward/backward
  support；nearest rounding用于inference/static weights；high precision保留sensitive ops/master state；pure FP4只有在quality/
  wall-clock gate均通过时可用。
- **Evolution Relationship:** `Direct Evolution`：BF16 mixed precision → FP8 role-specific formats → naive MXFP4 backward →
  unbiased SR → RHT variance control + block-local distributed mapping；后者不是“精度越低越快”的单向结论。
- **ROADMAP Node:** `TRAIN-PRETRAINING`（Current Ch28；Legacy Ch24）主 owner；handoff到
  `TRAIN-DISTRIBUTED-TRAINING`、`TRAIN-CHECKPOINT`、`INFER-TENSORRT-LLM`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch28 mixed precision/low-bit graph、gradient clipping与optimizer state主线，核对
  Ch36 shard/communication和Ch49 kernel/hardware contract；precision recipe不拥有cluster-level speedup。
- **Existing Coverage:** Ch28已明确“无偏不等于免费”、precision policy沿error path分区与完整convergence contract；该论文
  提供SR bias + RHT variance + distributed locality的mechanism chain，可 refine现有论证。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。Historical Books Gate关闭。
- **Changed Files or Rejection Reason:** 本周只更新Weekly；完成v1全文，明确headline speed是跨hardware proxy estimate。
- **Open Questions:** native MXFP4 kernels/hardware、paper code、seed variance、trillion-token/frontier models、optimizer/layer
  sensitivity、multi-node RHT/sharding、RNG checkpoint/replay、energy/failure recovery与independent reproduction。

### Self-Training Elicits Concise Reasoning: Distill a Better Compute Policy from the Model's Own Tail

- **Candidate / Week / Score:** Self-Training Elicits Concise Reasoning / 2025-W09 / 26/30。
- **Source Family ID:** `concise-reasoning-self-training-fs-bon`。
- **Source Type:** arXiv v1 full paper + official generation/fine-tuning/evaluation code and released models。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-27、v2 2025-02-28（同W09）；June v3/ACL
  revisions只作lineage，review锁定v1机制与event-time results。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.20122；https://arxiv.org/html/2502.20122v1；
  https://github.com/TergelMunkhbat/concise-reasoning。
- **Access and Verification Status:** v1 preliminary distribution、all methods/results/analysis、budget/config/prompts、limitations
  与official artifact已核验；task-specific math scope与GPT-4o exemplar dependency明确保留。
- **Full-read Coverage:** length distributions、zero-shot failures、question-wise BoN、human/GPT/self few-shot、FS-BoN+
  augmentation、five model/two dataset budget-matched results、scale/complexity/transfer analyses、full prompts/config/cost、
  limitations与code/models。
- **Original Problem:** CoT把output tokens当sequential compute，但训练并未优化每个token的边际价值；简单“be concise”/
  fixed budget会截断必要推理并损害accuracy。模型分布里已有短且正确的paths，问题是如何把低概率tail变成默认policy。
- **Why the Previous Design Was Reasonable:** 长CoT提高coverage、自我检查和hard-task capacity；zero-shot budget无需训练；
  external teacher可提供高质量short rationales。难题分布未知、accuracy优先或缺exact verifier时，保留更长reasoning仍合理。
- **Changed Constraint:** inference cost/latency随output tokens增长，且task-specialized models对prompt-level conciseness控制不敏感；
  需要question-relative而非global shortest selection，避免只训练easy questions。
- **Mechanism:** 每题采样多条paths，用exact answer parser只保留correct，按该题选择shortest；few-shot exemplars先把sampling
  distribution推向shorter region，再做BoN；同时混入default-distribution BoN paths覆盖hard questions；最后标准SFT把
  test-time search/long prompt的收益蒸馏进policy。训练样本长度成为implicit compute policy。
- **State Ownership:** task/oracle parser拥有correctness；sampling prompt/model/temp拥有candidate distribution；question-wise
  selector拥有length-quality tradeoff；few-shot exemplars拥有bootstrap prior；SFT checkpoint拥有distilled behavior；runtime
  scheduler/cost policy仍拥有deployment token budget/stop，不由training mean length替代。
- **Control Flow / Data Flow:** training questions → default/few-shot stochastic samples → exact answer validation → per-question
  shortest-correct selection/augmentation → SFT → greedy evaluation accuracy+all-output token length → deployment cost validation。
- **Implementation Details:** five main models1.5B–7B，scale checks1B/3B/8B；GSM8K/MATH；default BoN16 paths，FS-BoN
  16+16 augmentation，budget-matched8+8；SFT batch16、1 epoch、LR1e-5、max469 steps；BF16、8×H100，总main约1,000
  H100-hours。Generation dominates：single-H100 example约1–1.5h vs training2m24s。
- **Evaluation Contract:** final-answer accuracy+average output tokens（包括incorrect paths）；greedy decode；GSM8K max512、MATH
  max1024。Relative length以baseline平均为denominator；30%是five-family/two-task aggregate，不能直接换算TTFT/TPOT或
  production cost。
- **Baselines / Ablations / Sensitivity / Overhead:** multiple zero-shot prompts、direct answer/human/GPT4o CoT、naive BoN、
  Rational Metareasoning、FS-Human/GPT/self、FS-BoN budget matched、augmentation、question-wise/global selection、scale与
  complexity slices；缺multi-domain、interactive tools、latency/hardware serving、reward for semantic proof quality与distribution shift。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** models/H100/BF16/budgets/length caps披露；production
  batch/concurrency、KV cost、TTFT/TPOT/tail latency、energy与SLO未测，tokens仅是cost proxy。
- **What the Evidence Actually Proves:** 在math tasks和exact final-answer filter下，model自身distribution包含更短correct paths；
  per-question self-training能将部分tail behavior转为default，few-shot+BoN提高sample efficiency；固定prompt budget存在明显
  accuracy trade-off。
- **What It Does Not Prove:** shorter trace保留faithful reasoning、所有removed tokens冗余、30%普适、accuracy完全不变于每个
  model/task slice、thinking-model hidden CoT可同样压缩，或token reduction等于wall-clock reduction。
- **Limitations / Threats to Validity:** GSM8K/MATH only、≤8B scale、exact-answer selection可保留invalid reasoning、GPT-4o
  exemplars/validator、task-specific SFT、aggregate accuracy masking、max-token truncation、no OOD/safety/faithfulness/serving test。
- **Trade-offs / New Failure Modes:** BoN发现short paths但generation cost指数上升；few-shot提高效率却传递style/teacher bias；
  SFT降低runtime tokens却可能削弱hard-task exploration、自-correction和calibration；question-wise selection保护coverage但需oracle。
- **Where the Previous Design Still Applies:** long reasoning用于hard/unknown tasks；adaptive runtime budget用于per-request risk；
  prompt-only控制适合不可训练API；external verified process supervision用于reasoning validity；direct answer用于trivial tasks。
- **Evolution Relationship:** `Direct Evolution`：unbounded/default CoT → prompt/fixed budget → per-question shortest-correct BoN →
  few-shot-shifted sampling + self-training；是conditional compute branch，不证明所有reasoning应压缩。
- **ROADMAP Node:** `TRAIN-SFT`（Current Ch29；Legacy Ch25）主 owner；handoff到 `MODEL-SAMPLING`、
  `INFER-SCHEDULING`、`PLATFORM-COST`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch29 demonstration/distribution、Ch20 sampling、Ch56 budget/SLO和Ch66
  accuracy/process evidence边界；SFT改变default behavior，不拥有runtime release gate。
- **Existing Coverage:** Books已有adaptive inference budget、training data=behavior prior与accuracy/cost joint contract；该论文
  可 refine“把model distribution tail蒸馏为compute policy”，不保留30%常数。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。Historical Books Gate关闭。
- **Changed Files or Rejection Reason:** 本周只更新Weekly；完成v1全文、artifact与budget accounting审计。
- **Open Questions:** OOD/general tasks、>8B/thinking models、process validity/faithfulness、hard-task regression、online adaptive
  stop、serving latency/KV/goodput、safety/refusal length、teacher-free exemplars与independent reproduction。

### Granite Embedding Models: Retrieval Artifact Design across Quality, License and Latency

- **Candidate / Week / Score:** Granite Embedding Models / 2025-W09 / 27/30。
- **Source Family ID:** `granite-embedding-dense-sparse-distilled-enterprise-retrieval`。
- **Source Type:** arXiv v1 technical report + Apache-2.0 model cards/weights；training code/data manifests未完整公开。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-27；later r1.1/multi-turn revisions属于后续lineage，
  W09锁定original 30M/125M English、107M/278M multilingual与30M sparse family。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.20204；https://arxiv.org/html/2502.20204v1；
  https://huggingface.co/ibm-granite/granite-embedding-30m-english。
- **Access and Verification Status:** v1 architecture/data/training/dense/multilingual/sparse/evaluation appendices与event-family
  model card已核验；internal data/benchmarks、training code、full manifests与exact release checksums不公开。
- **Full-read Coverage:** 6/12-layer encoders、contrastive loss/in-batch+hard negatives、retrieval-oriented pretraining、decoder/
  encoder/self-distillation、stage-wise languages、model merging、sparse term/FLOPS/NORM losses、data governance/sampling、
  public/internal/code/multilingual eval、single-A100 latency与model card/license/context limits。
- **Original Problem:** large decoder embeddings表达强但memory/latency高；small encoders高效却需要retrieval-specific data；dense
  semantic retrieval、sparse exact-term retrieval、multilingual coverage和commercial licensing是不同constraints，不能用一个
  leaderboard average解决。
- **Why the Previous Design Was Reasonable:** BM25/sparse inverted index对identifiers和可解释term weights稳定；dense dual encoder
  对semantic recall高效；large decoder teacher适合offline quality。小corpus、exact match、single-language或许可不敏感研究
  环境中，已有模型仍合理。
- **Changed Constraint:** enterprise corpus含technical/code/multilingual queries，需low-latency portfolio、permissive data lineage与
  domain adaptation，同时避免用research-only MS MARCO训练commercial artifact。
- **Mechanism:** weak title/body/citation/QA pairs用in-batch negatives；annotated/synthetic pairs加入mined hard negatives；12-layer
  English先retrieval-oriented pretrain，再由decoder teacher的similarity distribution蒸馏；6-layer students蒸馏12-layer；
  multilingual按6→12 languages分阶段contrastive/self-distill；model merging适配enterprise domain；sparse branch用term max-pool+
  contrastive KD+FLOPS+NORM regularization。
- **State Ownership:** dataset partition/license/PII review拥有admission；query/passage/hard-negative generator拥有training relation；
  teacher checkpoint拥有soft similarity distribution；student/model-merge revision拥有embedding geometry；index artifact拥有vector/
  term schema；retriever/RAG runtime拥有query/corpus/SLO，不由model card score替代。
- **Control Flow / Data Flow:** cleared data partitions → pair/synthetic/hard-negative construction → dataset-alpha batch sampling →
  retrieval pretrain/contrastive finetune → teacher score distillation → optional stage-wise language/domain merge → immutable model →
  corpus re-embedding/index build → retrieval evaluation/deployment。
- **Implementation Details:** English vocab50K，multilingual250K；6-layer384-d vs12-layer768-d，max512 tokens；dataset sampling
  `p_i ∝ |D_i|^alpha` with reported0.5/0.9 choices；MS MARCO excluded forlicense；one hard negativefinetune/up tothree for
  distillation；sparse loss adds total-norm because FLOPS alone insufficient from distilled initialization。
- **Evaluation Contract:** BEIR/MTEB、MIRACL/multilingual tasks、CoIR plus internal RedHat/UnifiedSearch/ClapNQ；internal corpora
  466/402 queries with666K/1.7M docs；latency single A100，但batch、sequence lengths、precision/warmup/repetitions未披露。
  Appendix full MTEB averages show Granite并非所有generic tasks优于BGE/E5，headline Figure混合internal strengths。
- **Baselines / Ablations / Sensitivity / Overhead:** similar-size E5/BGE/GTE/Nomic/Arctic/SPLADE；paper描述recipe choices但缺
  systematic component ablation、teacher/data/license matched baselines、alpha/hard-negative/model-merge sensitivity、index build/
  storage/throughput与downstream RAG answer effects。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** single A100 latency与model sizes/dim/context披露；training
  cluster为A100 80GB但GPU count/tokens/wall time/precision不披露；query latency缺batch/concurrency/tail SLO，model card当前BF16
  status可能包含post-W09 revision。
- **What the Evidence Actually Proves:** 一个retrieval portfolio可以通过teacher/student、dense/sparse与language stages在quality/
  latency/license axes上形成不同artifacts；data governance与model/index compatibility是production design的一部分；作者models
  在其internal/selected retrieval tasks有优势。
- **What It Does Not Prove:** universal embedding superiority、internal benchmark可外推、distillation每个component因果贡献、
  Apache model license自动证明all source data rights、0.16s是production SLO，或embedding score等于RAG answer quality。
- **Limitations / Threats to Validity:** vendor/internal data+benchmarks、no training code/manifests、no explicit limitations section、
  mixed benchmark averages、512 truncation、selected comparisons、current model-card revision drift、missing RAG end-to-end/
  independent reproduction。
- **Trade-offs / New Failure Modes:** small student省latency/memory但丢long-tail geometry；hard negatives提升precision却可能false-
  negative collapse；dense semantic vs sparse exact-term是alternative branches；multilingual vocab扩大artifact/memory；model merge保留
  generality但引入geometry/index invalidation。
- **Where the Previous Design Still Applies:** BM25/sparse用于identifiers；large dense encoder用于quality-first；hybrid retrieval用于
  mixed corpus；domain-specific retraining用于stable enterprise distribution；off-the-shelf open model用于low governance cost。
- **Evolution Relationship:** `Layering / Dependency`：general encoder → retrieval-oriented contrastive model → teacher-distilled
  portfolio → dense/sparse/language/domain branches → versioned index；不是单一模型替代所有retrieval路径。
- **ROADMAP Node:** `MODEL-EMBEDDING`（Current/Legacy Ch12）主 owner；handoff到 `TRAIN-DATA`、`AGENT-RAG`、
  `PLATFORM-MODEL-REGISTRY`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch12 representation/geometry、Ch27 data governance、Ch76 retrieval/index contract和
  Ch59 registry；embedding model不拥有authorization、packing或answer truth。
- **Existing Coverage:** Books已有dense/lexical/hybrid retrieval、index identity、embedding/model/data lineage；Granite是受限
  implementation case，没有新增需要独立正文的长期机制。
- **Integration Decision:** `Books Pending — No Change Candidate`。后续只需引用现有论点，不追加产品清单。
- **Changed Files or Rejection Reason:** 本周只更新Weekly；完成v1/model-card审计并保留generic benchmark反证。
- **Open Questions:** immutable W09 model revisions/checksums、training manifests/code/cost、source partition licenses/delete、
  component ablations、index build/storage、tail latency/concurrency、hybrid/RAG outcome与independent reproduction。

### WorldModelBench: Video Plausibility Is Evidence below Controllable World Modeling

- **Candidate / Week / Score:** WorldModelBench / 2025-W09 / 28/30。
- **Source Family ID:** `worldmodelbench-video-physics-instruction-human-judge`。
- **Source Type:** official project first-public + arXiv v1 full paper + public test data/judge/evaluation surfaces。
- **Event Date / First-public Date / Revision History:** official project announcement 2025-02-27、arXiv v1 2025-02-28，均属W09；
  later leaderboard/model submissions只作living benchmark lineage。
- **Direct Primary Sources:** https://worldmodelbench-team.github.io/；https://arxiv.org/abs/2502.20694；
  https://arxiv.org/html/2502.20694v1；project-linked test data/judge/evaluation artifacts。
- **Access and Verification Status:** v1 benchmark/judge/reward optimization、all human/model results、appendices/inference configs、
  project artifact已核验；closed model APIs/version outputs与reward-training code/run未完全冻结。
- **Full-read Coverage:** design criteria、350 prompt curation、7 domains/56 subdomains、67K labels/agreement、2B VILA judge、14
  model comparisons、Elo/subdomains/hard subset、judge accuracy、VBench correlation、reward-gradient OpenSora case、inference
  hyperparameters、discussion/limitations与project artifacts。
- **Original Problem:** high-FVD/visual quality视频仍可违反gravity、mass conservation或instruction，因而“看起来真实”不能证明
  model学会environment dynamics；但world-model claim常被普通video benchmark接受。需要把physics/instruction/common-sense
  evidence从aesthetic quality中拆出。
- **Why the Previous Design Was Reasonable:** FVD/CLIP/VBench便宜、规模大、适合生成质量regression；human arena能直接反映
  visual preference；explicit simulator能验证physics。内容生成场景、无action/control claim或低成本screening时旧指标仍合理。
- **Changed Constraint:** video generators被用于robotics/driving/planning叙事，I2V/T2V需预测feasible future frames；评价成本极高
  （paper示例Mochi约4×A100、5分钟/样本），benchmark必须在小prompt set、dense criteria和automatic judge间折中。
- **Mechanism:** 从driving/robotics/human/industry/nature/gaming/animation reference videos提取first frame与action captions，经human
  verify构成350 T2V/I2V conditions；每video按instruction0–3、five physics binaries、frame/temporal commonsense two binaries评分。
  65 voters产生8,336 votes/67K labels；将每vote拆成8 QA训练2B VILA judge，并用judge token probability gap作为OpenSora
  differentiable reward。
- **State Ownership:** reference video/prompt拥有feasible target hint；human rubric/votes拥有benchmark labels；judge拥有proxy scores；
  generator拥有video distribution；explicit environment/controller拥有真实action consequence；benchmark不拥有causal transition truth。
- **Control Flow / Data Flow:** reference video → first-frame/action condition → generator video → human multi-criteria vote → judge
  train/test split by model outputs → automatic criteria scores → leaderboard；optional branch用judge reward gradient更新video model，
  再由independent human/eval复核。
- **Implementation Details:** 350 prompts×14 models，average1.7 votes/video；12 model outputs/prompt训练、2 held-out model outputs测试，
  plus original video high-reward samples；4,421 train/713 eval videos。Judge comparison混合GPT-4o/Gemini reasoning chains，
  majority vote为sparse ground truth。Reward把subscoresnaive sum，未学习risk weights。
- **Evaluation Contract:** human score agreement within±2为87.1%，pairwise agreement70%；10 CS-PhD-level expert sanity check；judge
  test仅same prompts/unseen generator outputs。14 model inference settings、T2V/I2V/hard45 prompts不同；closed APIs拒绝部分samples。
- **Baselines / Ablations / Sensitivity / Overhead:** VBench/VideoPhy comparison、GPT-4o/Gemini/Qwen/VILA judges、zero-shot/CoT/
  fine-tune、annotation scaling、hard subset、reward optimization qualitative case；缺prompt/domain holdout、real control outcomes、
  action-conditioned counterfactuals、judge adversarial gaming、human post-training evaluation与long-horizon rollout。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** per-generator steps/CFG/resolution partially披露，Mochi cost
  example4×A100/5min；judge/video training hardware、precision、batch、walltime、API latency与production SLO不完整。
- **What the Evidence Actually Proves:** ordinaryvideo quality metrics与human physics rubric相关性低；当前generators在selected
  future-frame tasks存在instruction/physics violations；human-aligned judge可在same-prompt held-out-generator split近似labels；
  video plausibility必须独立于aesthetics测量。
- **What It Does Not Prove:** 被测video model是action-conditioned/causal world model、physics rubric覆盖real dynamics、judge improvement
  产生真实planning/control收益、reward optimization不hack judge、human preference=physical law，或350 prompts代表open world。
- **Limitations / Threats to Validity:** small350 suite、prompt/reference selection、low1.7 votes/video、70% pairwise agreement、same-prompt
  judge split、closed API drift/refusals、coarse five laws、naive score sum、qualitative reward result、no action/control/sim-to-real evidence。
- **Trade-offs / New Failure Modes:** fine-grained rubric增加diagnosis但仍是visual proxy；human labels提高meaning却昂贵/subjective；small
  suite便于运行却易overfit；learned judge降成本却新增reward hacking/correlated error；real simulator更权威但domain-specific昂贵。
- **Where the Previous Design Still Applies:** VBench/FVD用于visual regression；explicit simulator/physics engine用于causal invariants；
  action-conditioned environment evaluation用于planning/control；human review用于开放violations；hybrid gate逐级升级证据。
- **Evolution Relationship:** `Direct Evolution`：aesthetic/frame quality → temporal coherence → instruction/physics plausibility →
  action-conditioned intervention/closed-loop outcome；WorldModelBench位于第三层，不是controllable world-model终点。
- **ROADMAP Node:** `MULTIMODAL-WORLD-MODELS`（Current Ch25；new node）主 owner；handoff到
  `PLATFORM-EVALUATION-SYSTEM`、`MULTIMODAL-GENERATIVE-PARADIGMS`、`MULTIMODAL-EMBODIED-VLA`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch25 video/predictive/controllable distinction与evaluation ladder，核对Ch24 generation、
  Ch26 action authority与Ch66 judge contract；video judge不拥有environment transition truth。
- **Existing Coverage:** Ch25已经明确visual quality不等于action consequence，并建立pixels→action-conditioned→closed-loop ladder；
  WorldModelBench为该既有论点提供受限primary evidence，没有新增缺失机制。
- **Integration Decision:** `Books Pending — No Change Candidate`。后续Books pass只需引用现有论点，不追加leaderboard。
- **Changed Files or Rejection Reason:** 本周只更新Weekly；完整保存human/judge/reward evidence与“video≠controllable world model”边界。
- **Open Questions:** prompt/domain holdout、more votes/agreement、action-conditioned variants、real simulator/robot outcomes、judge red-team/
  calibration、reward hacking、long horizon、closed API reproducibility、training code/cost与independent reproduction。

### LongRePS: Long Context Capacity Still Needs Grounded Reasoning Supervision

- **Candidate / Week / Score:** LongRePS / 2025-W09 / 27/30。
- **Source Family ID:** `longreps-grounded-long-context-reasoning-supervision`。
- **Source Type:** 14-page arXiv v1 PDF + official sampling/filter/training/evaluation repository；training/eval data released
  2025-03-03，属于W10 artifact lineage。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-28；artifact 2025-03-03不倒写为W09可执行状态。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.20790；https://arxiv.org/pdf/2502.20790v1；
  https://github.com/lemon-prog123/LongRePS。
- **Access and Verification Status:** HTML不可用；已完整读取v1 PDF、all tables/analysis/appendices与current official code/data
  instructions。Event-time artifact未发布，current repository无immutable W09 tag。
- **Full-read Coverage:** cross-model CoT survey on10K–128K tasks、majority/oracle scaling、warmup/self-sampling、answer/source/
  intrinsic filters、SFT、MuSiQue/LongBenchV1/V2 results、criteria/sampling/source analyses、full prompts/config、limitations与artifact chronology。
- **Original Problem:** 128K context window只证明tokens可进入attention，不证明模型能检索、聚合并引用分散evidence；small models
  的vanilla CoT还可能制造干扰。Outcome-only SFT可学答案格式，却不约束reasoning是否来自source或逻辑一致。
- **Why the Previous Design Was Reasonable:** context extension/position scaling先解决容量；outcome supervision便宜且不依赖
  subjective process judge；plain retrieval对single needle足够。简单lookup、short contexts、strong outcome verifier或推理不可见时，
  旧方案仍更稳。
- **Changed Constraint:** multi-document QA在10K–128K内需要多hop evidence；self-sampled long CoTs含hallucinated excerpts与
  internally inconsistent aggregation，完整long-context LLM judge又昂贵且不可靠。
- **Mechanism:** 先用300 teacher-CoT warmup base Llama/Qwen；对3,000 MuSiQue examples各sample30 paths，prompt强制
  decomposition+`[Excerpt]` citations；按final-answer F1=1过滤，再用source substring exact match检查每个excerpt，最后用不带
  long source的LLM评logical coherence/completeness/conciseness并选top path；用约2,000 retained paths做2-epoch SFT。
- **State Ownership:** context/source document拥有evidence truth；answer key拥有outcome；citation extractor/exact match拥有literal
  grounding proxy；intrinsic judge拥有coherence proxy；training manifest拥有selected path；model checkpoint拥有learned policy；
  deployment RAG/evaluation仍拥有fresh source/provenance，不由CoT文本替代。
- **Control Flow / Data Flow:** long context+question → N sampled decompositions/citations/answers → answer F1 gate → source exact-match
  gate → intrinsic consistency rank → selected CoT dataset → SFT → in-domain/cross-domain long-context evaluation。
- **Implementation Details:** MuSiQue expanded from<4K to10–16K；warmup20 steps LR1e-5/batch32；self-sampling temp0.7、N=30；
  consistency threshold1.0 filters约1,000/3,000；SFT2 epochs LR5e-6/batch32；8×A100 viaLLaMA-Factory。Evaluation contexts
  reach128K although training only≤16K。
- **Evaluation Contract:** Llama3.1-8B/Qwen2.5-7B base，MuSiQue F1、selectedLongBenchV1 QA与LongBenchV2 SQA/MQA
  multiple-choice accuracy；comparison with outcome-supervised same hyperparameters and reference instruct/GPT models。Initial CoT survey
  converts some synthetic tasks toMCQ and includes7 models；not a uniform generation contract。
- **Baselines / Ablations / Sensitivity / Overhead:** no-CoT/CoT acrossmodels/lengths/tasks、outcome supervision、AC→+SF→+IC、
  sampling N=1/10/30/50/100、self vsGPT4o-mini/GPT4o CoTs。Performance peaks then decreases asN grows，showingjudge/filter
  capacity rather than sample count alone is bottleneck；缺matched generation/judge cost、citation paraphrase/semantic grounding与seeds。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 8×A100/training lengths/batches/steps披露；GPU memory、
  precision、generation/judge tokens/wall time、LongBench inference batch/latency、serving concurrency和SLO未披露。
- **What the Evidence Actually Proves:** 在MuSiQue-derived16K training与selected QA tests中，outcome+literal source+
  consistency filtering比outcome-only SFT产生更好结果；long-context CoT收益取决于task/model capacity，single-needle可被CoT干扰；
  process-quality selection不是“sample越多越好”。
- **What It Does Not Prove:** excerpt match=entailment、CoT faithful/causal、16K training建立128K reasoning机制、所有long tasks获益、
  +13.6/+9.3普适、teacher CoT无泄漏、intrinsic judge正确，或生产long-context goodput改善。
- **Limitations / Threats to Validity:** only7B/8B、MuSiQue training、≤16K SFT、small eval subsets/MCQ conversion、exact substring
  discouragesparaphrase、LLM judge bias、best-of-two-epoch reporting、missing seeds/cost、artifact afterevent、no retrieval/serving test。
- **Trade-offs / New Failure Modes:** explicit citations提高可审计性却鼓励copy/format shortcut；exact match便宜但不验证evidence use；
  LLM consistency judge省long-context cost却可偏好style；30× sampling增加training compute；SFT提高default reasoning但可能增加output tokens。
- **Where the Previous Design Still Applies:** outcome-only training用于exact tasks；retrieval/citation system用于fresh evidence；no-CoT用于
  simple lookup；long-context architecture/data scaling用于capacity；external verifier/human review用于high-stakes reasoning。
- **Evolution Relationship:** `Layering / Dependency`：context-window capacity → retrieval access → CoT evidence aggregation →
  answer/source/process gates → supervised reasoning policy；不是CoT替代attention/retrieval。
- **ROADMAP Node:** `MODEL-LONG-CONTEXT`（Current/Legacy Ch22）主 owner；handoff到 `TRAIN-SFT`、`TRAIN-DATA`、
  `AGENT-RAG`、`PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-COST`。
- **Target and Adjacent Chapters Read:** 已读Ch22 capacity/effective context、Ch29 SFT、Ch27 data verification、Ch76 evidence retrieval与
  Ch66 process judge；reasoning path不拥有source truth或runtime SLO。
- **Existing Coverage:** Books已有nominal vs effective context、retrieval/grounding/process evidence分层；LongRePS可 refine“长context
  reasoning supervision需同时绑定answer、source与process”，不保留headline常数。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。Historical Books Gate关闭。
- **Changed Files or Rejection Reason:** 本周只更新Weekly；通过PDF恢复全文，并分离W09 paper与W10 artifact release。
- **Open Questions:** event-time code/data、semantic entailment vs substring、judge calibration、cost-matched sampling、>16K training、
  32B/70B、retrieval/tool integration、output latency/goodput、seeds/contamination与independent reproduction。

### PersonaBench: Personalization Requires Governed State, Not Only Top-k Retrieval

- **Candidate / Week / Score:** PersonaBench / 2025-W09 / 26/30。
- **Source Family ID:** `personabench-private-personal-state-rag-evaluation`。
- **Source Type:** Salesforce AI Research arXiv v1；后续 ACL Findings / arXiv v2 属同一 family，未发现可归属于
  event-time 的官方代码或完整 ground-truth artifact。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-28；v2 2025-08-20。W09 只以 v1
  建立事件，后续修订不重复计分。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.20616；
  https://arxiv.org/html/2502.20616v1。
- **Related Primary Sources:** v2 / ACL Findings 只用于确认 publication lineage；Hugging Face paper page只作
  discovery，不代替论文正文。
- **Access and Verification Status:** v1 HTML 全文、表格、结果、limitations 与 appendix 已核验；论文明确计划
  公开 generated documents，但 ground-truth profiles 与实际 template 不公开，因此 artifact-level reproduction
  为 `Not Available at Event Time / Partially Disclosed`。
- **Full-read Coverage:** profile schema、persona/social-graph construction、private-document synthesis、noise/news/
  preference updates、dataset statistics、RAG implementation、retrieval/end-to-end metrics、noise/category ablation、
  conclusion、ethical/consistency limitations 与 document/prompt examples。
- **Original Problem:** 私有助理需要从对话、user-AI interaction、购买记录等碎片中恢复用户事实、偏好与社会关系；
  直接暴露真实私有数据无法形成公开 benchmark，而通用 RAG 常把问题简化为“找最相似 passage”。
- **Why the Previous Design Was Reasonable:** session chunk + dense top-k + LLM 的 pipeline 简单、成本可控，适合
  单一事实、短历史和低噪声知识库；只评 retrieval recall 也便于定位第一阶段 miss。它在事实局部、无更新、
  ACL 单一且答案只需一段 evidence 时仍合理。
- **Changed Constraint:** 用户状态分散在不同 document types 与社交节点中，包含无关内容、时间更新和 multi-hop
  关系；source-of-truth profile 不会直接出现在 Context，retriever 还需面对不同 query category 与 noise ratio。
- **Mechanism:** 先以 demographic / psychographic / social template 生成五个社区和关联 persona，再合成 conversation、
  user-AI interaction 与 purchase-history sessions；加入 0/0.3/0.5/0.7 noise、外部 news 与小概率 preference update。
  用 session timestamp 切块，三个 dense retriever 统一取最大复杂问题所需的 top-k=5，并由四个 GPT variants回答
  basic、preference 与 social multi-hop questions；retrieval与answer分别计分。
- **State Ownership:** 隐藏 synthetic profile拥有 benchmark truth；timestamped private documents拥有可见 evidence；
  social graph只是生成依赖；retriever拥有候选排序，不拥有用户真值；LLM只生成推断；真实系统中 consent、ACL、
  valid time、supersession 与 deletion 仍由 Memory/security owners管理。
- **Control Flow / Data Flow:** hidden profile + social graph → timestamped private documents + controlled noise/update →
  query → session-level retrieval → packed evidence → LLM answer → retrieval recall/NDCG 与 answer recall/F1；错误可分为
  evidence miss、更新/关系解释失败和生成失败。
- **Implementation Details:** 五个社区各抽三人，共15个 test characters、最多48类属性、582 questions（269 basic、
  186 preference、127 social）；documents按session时间切块并附参与者姓名。Retrievers为23M MiniLM、110M MPNet与
  567M BGE-M3；readers为GPT-4o、GPT-4o-mini、GPT-4与GPT-3.5-turbo，共12种组合。
- **Evaluation Contract:** retrieval用Recall/NDCG，答案用term-level Recall/F1；主表在0.5 noise，另测noise、类别、
  update、easy/hard 与 ground-truth-context分支。Ground-truth-context仍是synthetic document evidence，不是生产用户事实。
- **Baselines / Ablations / Sensitivity / Overhead:** 三种retriever×四种reader、noise0→0.7、basic/preference/social、
  preference list size与GT-context；0.5 noise下BGE-M3 overall retrieval recall为0.325。缺lexical/hybrid、query
  decomposition、temporal resolver、social-graph retrieval、ACL、human validation、latency/cost与independent replication。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/API identity和retriever sizes披露；embedding/
  reader hardware、precision、document/token lengths、batch、concurrency、latency、cost和production SLO均 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在该synthetic English benchmark与固定top-k pipeline中，增大dense retriever
  不能解决noise、更新、multi-hop与answer-use的组合问题；即使给定相关context，reader仍可能无法完整恢复personal state。
  因而 personalization evaluation需要分开 retrieval 与 downstream interpretation。
- **What It Does Not Prove:** 生产用户数据具有相同分布、BGE-M3或GPT版本的通用排名、graph memory必然更好、synthetic
  profile等同真实身份、0.325可外推，或存储更多私人历史可以合法且安全地提高个性化。
- **Limitations / Threats to Validity:** 仅15个synthetic characters、自动生成documents可能不一致、truth profiles/template
  不公开、English/provider/API drift、固定top-k、公平性/隐私/consent/删除未执行、缺开放artifact与human-user validation。
- **Trade-offs / New Failure Modes:** synthetic data避免真实PII却引入simulation bias；session chunk保留时间边界却可能
  切断跨session evidence；更大top-k提高coverage却扩大noise、token和隐私暴露；显式personal state提升一致性却新增
  stale preference、错误持久化、越权关联、删除传播与过度个性化。
- **Where the Previous Design Still Applies:** flat dense/lexical top-k用于短且局部的授权历史；full Context用于极短历史且
  miss不可接受；authoritative profile用于用户明确确认的字段；高风险或冲突信息应ask/abstain，而非自动merge。
- **Evolution Relationship:** `Layering / Dependency`：document RAG → temporal/entity evidence assembly → governed personal-state
  construction → supersession/authorization → answer/use evaluation；不是RAG被Memory单向替代。
- **ROADMAP Node:** `AGENT-MEMORY`（Current Ch77；Legacy Ch73）主 owner；handoff到 `AGENT-RAG`（Ch76）、
  `PLATFORM-SECURITY`（Ch72）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读Ch76 ingestion/retrieval/failure attribution、Ch77 typed write、bounded evidence set、
  temporal/supersession/personalization policy，核对Ch72 ACL-before-retrieval与Ch66 system evaluation contract。
- **Existing Coverage:** Ch77已明确personal feedback不能合并成单一persona、Memory write/read需provenance/valid-time/
  supersession，且retrieval construction与answer use必须分开；Ch76已拆retrieval miss与generator miss。论文提供受限benchmark
  evidence，但没有新增长期机制缺口。
- **Integration Decision:** `Books Pending — No Change Candidate`。后续Books pass应引用现有具体论点，避免追加benchmark列表。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，也未把未公开artifact或synthetic truth外推。
- **Open Questions:** v1 event-time artifact、v2具体变化、hybrid/graph/temporal baselines、query-time anchoring、ACL与deletion、
  real-user consent/fairness、human validation、cost/SLO、multi-language与independent reproduction。

### Safety Tax: Sequential Safety SFT Is a Multi-objective Regression Case, Not a Universal Law

- **Candidate / Week / Score:** Safety Tax / 2025-W09 / 26/30。
- **Source Family ID:** `safety-tax-sequential-sft-reasoning-regression`。
- **Source Type:** arXiv v1 + official code/data/model repository；v2属于同一 paper family。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-03-01；v2 2025-06-05。W09 owner event为v1，
  v2与current repository仅用于核验lineage，不倒写为event-time implementation completeness。
- **Direct Primary Sources:** https://arxiv.org/abs/2503.00555；https://arxiv.org/html/2503.00555v1；
  https://github.com/git-disl/Safety-Tax。
- **Related Primary Sources:** repository-linked DirectRefusal dataset与aligned checkpoints；SafeChain是对照数据来源，
  不是本论文独立提出的通用safety objective。
- **Access and Verification Status:** v1全文、表格、limitations、appendix与current official reproduction instructions已核验；
  repository无immutable W09 release/tag，event-time artifact状态不能由current main完全重建。
- **Full-read Coverage:** two-stage production pipeline、DirectRefusal/SafeChain construction、models/benchmarks/hyperparameters、
  main and cross-model results、epoch sensitivity、8×H200 overhead、qualitative examples、limitations与official scripts/data lineage。
- **Original Problem:** reasoning training可能提高task accuracy同时扩大harmful-answer opportunity；随后安全对齐能否恢复拒答，
  又不破坏刚形成的reasoning behavior，是一个多目标、顺序更新与能力保持问题。
- **Why the Previous Design Was Reasonable:** 先训练reasoning、再用少量安全demonstrations做SFT，模块职责清楚、实现简单、
  计算成本低，也便于快速修复refusal behavior；当能力分布与安全数据兼容、update较小并有回归gate时仍可成立。
- **Changed Constraint:** 两阶段都更新同一32B参数，后阶段仅1000条窄安全数据且连续5 epochs；短模板拒答和长CoT拒答
  改变不同token distribution，使优化方向可能覆盖先前的推理行为。
- **Mechanism:** 以s1.1-32B、DeepSeek-R1-Distill-Qwen-32B、LIMO-32B为reasoning checkpoints，分别对
  DirectRefusal短拒答或SafeChain safety-CoT做full-model SFT；AdamW、LR5e-5、weight decay1e-4、cosine、5 epochs。
  再分别测AIME24/GPQA/MATH500 correctness与BeaverTails harmful score，并做epoch和system-overhead比较。
- **State Ownership:** reasoning checkpoint拥有既有parameter behavior；safety dataset定义目标demonstration distribution；
  optimizer拥有更新轨迹；benchmark scorer只拥有相应proxy；deployment policy、threat model与release authority不由单一
  harmful score或reasoning average拥有。
- **Control Flow / Data Flow:** shared Qwen-32B base → independently produced reasoning checkpoint → one of two safety datasets →
  sequential full SFT → reasoning/safety evaluations；没有joint objective、replay mixture、adapter、KL anchor或RL safety branch。
- **Implementation Details:** 三个LRM共享Qwen-32B-Instruct base；安全数据各1000 examples，full SFT五轮。官方repo基于s1，
  使用DeepSpeed ZeRO-3、Slurm scripts与lm-eval，并说明GPT-4o参与部分evaluation；current scripts覆盖three model branches
  与1–4 epoch runs。
- **Evaluation Contract:** s1.1主表用AIME24、GPQA、MATH500 average与BeaverTails；cross-model表只保留GPQA和harmful score。
  s1.1从63.40降至56.31（SafeChain）或32.49（DirectRefusal），harmful score从60.40降至30.80或0.80；这些是
  paper条件下的作者结果，不是通用比例。
- **Baselines / Ablations / Sensitivity / Overhead:** base/LRM/two safety datasets、three LRMs与epoch sensitivity；SafeChain相对
  DirectRefusal在8×H200上报告1.47× training time、1.03× memory。缺mixed replay、joint/multi-objective training、LoRA、
  KL/reference anchoring、RL/GRPO safety alignment、matched tokens、seeds/error bars、refusal precision与adversarial robustness。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 8×H200、32B models、训练时长和aggregate memory披露；
  precision、sequence-length distribution、effective/global batch、gradient accumulation、decode settings、evaluation concurrency、
  latency与production SLO为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在共享Qwen-32B base的三种reasoning checkpoints和该full-SFT配置中，安全数据选择
  形成不同的safety/capability operating point；短DirectRefusal更强地收窄harmful responses，也伴随更大bench regression，
  long SafeChain成本更高但保留更多reasoning score。
- **What It Does Not Prove:** safety与reasoning存在不可避免的普适Pareto frontier、RL/GRPO/DPO/Constitutional methods也会退化、
  harmful score等于真实安全、reasoning gain导致harmfulness、所有模型/语言/风险类别共享比例，或多目标/replay/adapter无法避免回退。
- **Limitations / Threats to Validity:** 作者自己限定为SFT而非RL；三模型共享base、窄1000-example数据、五轮高update、
  benchmark和judge proxy、missing seeds/uncertainty、跨模型表只测GPQA、event-time code tag缺失、repo宣传语比证据更绝对。
- **Trade-offs / New Failure Modes:** short refusal便宜且容易执行，却可能过度拒答、模板坍缩和能力遗忘；safety CoT保留更多
  reasoning surface，却增加tokens、training memory/time和potential leakage；mixed replay或更小update可能保留能力，却稀释
  safety signal并增加data-governance与调参成本。
- **Where the Previous Design Still Applies:** sequential SFT适合紧急、可测、低update的behavior patch；adapter/prompt policy适合
  可逆边界；joint/replay/KL或preference/RL branches适合需要同时维持能力的场景；deterministic runtime safeguards仍负责
  权限与side effects，不能由weights拒答替代。
- **Evolution Relationship:** `Alternative Branch`：reasoning checkpoint → sequential safety SFT → capability/safety regression gate；
  压力进一步导向mixed replay、update control、multi-objective/preference/RL branches与runtime defense-in-depth，而不是宣告
  “安全必然损害推理”。
- **ROADMAP Node:** `TRAIN-SFT`（Current Ch29；Legacy Ch25）主 owner；handoff到 `TRAIN-RLHF`（Ch31）、
  `PLATFORM-EVALUATION-SYSTEM`（Ch66）与 `PLATFORM-SECURITY`（Ch72）。
- **Target and Adjacent Chapters Read:** 已读Ch29 catastrophic forgetting、safety/refusal与general capability回归，核对Ch31
  多目标preference proxy、Ch66条件性证据与Ch72 threat-model/release边界。
- **Existing Coverage:** Ch29已经说明窄数据、过大learning rate或过久SFT会导致通用能力回退和拒答边界漂移，并要求
  safety、task correctness与general capability分开评估；该论文是机制受限案例，没有形成正文缺口。
- **Integration Decision:** `Books Pending — No Change Candidate`。后续Books pass只需确认现有章节已经覆盖，不能保留
  “unavoidable safety tax”作为通用结论。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；保存实验合同与作者结论边界，不修改Books。
- **Open Questions:** v1 artifact commit、v2变化、seeds/error bars、matched-token/learning-rate/epoch ablation、replay/joint/
  adapter/KL/RL branches、refusal precision/over-refusal、multilingual/adversarial safety与independent reproduction。

### ARIES: Learned Graph Traversal Moves Scheduling into the Reasoning Control Loop

- **Candidate / Week / Score:** ARIES: Autonomous Reasoning with LLMs on Interactive Thought Graph Environments /
  2025-W09 / 26/30。
- **Source Family ID:** `aries-llm-policy-interactive-thought-graph`。
- **Source Type:** arXiv v1；未发现作者官方代码、artifact或event-time immutable implementation。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-28；arXiv history只有该版本。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.21208；https://arxiv.org/html/2502.21208v1。
- **Related Primary Sources:** later OpenReview/venue submissions只作publication lineage，不替代W09 v1证据；HF page只作discovery。
- **Access and Verification Status:** v1 HTML全文、algorithm、tables、ablation、limitations和appendices已核验；code/artifact
  `Not Publicly Linked`，结果不能执行级复现。
- **Full-read Coverage:** topological reasoning formalization、divide-and-conquer transformations、MDP/action policy、multi-agent
  control flow、in-context action analysis、ensemble、HumanEval/sorting/set-intersection setup、Bayesian-search baselines、transition
  profiles、model-size/depth failures、ensemble/CoT ablation、limitations、risk与benchmark definitions。
- **Original Problem:** Tree/Graph-of-Thought用固定、task-specific transformation schedule；不同task需要重新搜索decompose、solve、
  aggregate、refine的顺序与multiplicity，search cost甚至高于单次推理。
- **Why the Previous Design Was Reasonable:** 静态schedule可复现、容易设置hard budget，也不把控制权交给随机模型；task稳定、
  transformation success profile已知或高风险需要确定流程时，预先调优/规则schedule仍更合理。
- **Changed Constraint:** workload跨task变化，固定schedule不能根据当前graph、action history和失败反馈调整；但在线planner也必须
  在有限query budget内决定何时分解、重试、聚合、refine或停止。
- **Mechanism:** 把thought graph视为MDP state，把proposal/solve/evaluate/refine/reduce/aggregate视为actions。Policy LLM读取
  typed-by-text action descriptions、current nodes/edges与history，分析策略后选择下一transformation；reasoning LLM执行并更新graph。
  每步并行询问五个policy agents，以majority action降低stochasticity，直至solution或iteration cap。
- **State Ownership:** thought-graph runtime拥有candidate nodes/edges与history；policy agents只提出next action；reasoning agent生成
  transformed nodes；benchmark error/test拥有success evidence。文本planner不拥有action legality、budget或最终correctness。
- **Control Flow / Data Flow:** problem → initial graph → policy ensemble(graph+history+action schema) → majority action → reasoning
  transformation → graph update/error feedback → repeat/stop → reduce/aggregate final answer；static GoT branch在运行前先做Bayesian search。
- **Implementation Details:** Llama-3.1-70B/405B同时作为policy/reasoning agents，temperature=1；70B在8×A6000，405B在
  4 nodes/16×H100，约3K GPU-hours。主要实验固定ensemble=5；cost以LLM query count近似，因为作者观察token-count方差较低。
- **Evaluation Contract:** HumanEval functional accuracy、sorting/set-intersection error，以及search/inference query counts；
  static GoT分别使用25/50/100% Bayesian-search budgets，另有direct prompting。405B HumanEval作者表中ARIES 89.0%、5.3
  inference queries；headline只相对这些baseline与配置成立。
- **Baselines / Ablations / Sensitivity / Overhead:** direct IO、three searched static schedules、70B vs405B、task/decomposition depth、
  transition success、ensemble1–15与policy CoT。缺matched tokens/latency/energy、seed confidence intervals、external verifier、
  prompt sensitivity、cross-model policy/reasoner、real tool state与artifact reproduction。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model、temperature、GPU counts和total GPU-hours披露；
  precision、prompt/output lengths、SGLang config、batch/concurrency、network、latency、energy与production SLO为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在三类结构化tasks中，405B policy可依据graph state改变transformation mix，并在作者的
  query-count contract下优于searched schedules；70B与深decomposition会失败，aggregation/refinement transition是主要压力点。
- **What It Does Not Prove:** LLM policy无需task semantics即可泛化、MDP/Markov假设在开放任务成立、majority消除相关错误、
  query count等于真实cost、任意Multi-Agent优于single planner，或高准确率可以绕过deterministic validation。
- **Limitations / Threats to Validity:** only Llama-3.1、three benchmarks、action preconditions/effects仍是自然语言、static baseline
  搜索合同特殊、temperature1/high variance、无artifact、3K GPU-hours、deeper graphs反向退化、policy和reasoner同源错误相关。
- **Trade-offs / New Failure Modes:** 自适应schedule省离线search并按反馈分配预算，却新增policy calls、graph serialization、
  invalid action、majority correlated error与control latency；ensemble提高稳定性但成本线性增长；深分解暴露中间evidence却放大
  aggregation error。静态schedule在稳定/高风险路径继续成立。
- **Where the Previous Design Still Applies:** direct prompt用于简单task；fixed tree/search用于branch cheap且可重复；deterministic
  Workflow用于side effects/legality；single planner + external verifier用于同源multi-agent无独立信息时。
- **Evolution Relationship:** `Direct Evolution`：fixed CoT → static tree/graph schedule → searched task-specific schedule →
  state-conditioned bounded policy → durable Workflow validation；ARIES覆盖第四步实验，不拥有第五步authority。
- **ROADMAP Node:** `AGENT-PLANNING`（Current Ch79；Legacy Ch75）主 owner；handoff到 `AGENT-WORKFLOW`、
  `AGENT-MULTI-AGENT`、`PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-COST`。
- **Target and Adjacent Chapters Read:** 已读Ch79 decomposition/search/replanning/budget，核对Ch81 authoritative transition、Ch82
  single-agent baseline/coordination tax/dynamic topology与Ch66 evaluation subject；thought graph不是workflow source of truth。
- **Existing Coverage:** Ch79已把plan定义为状态转移假设并保留dynamic branching、budget和search failure；Ch82已要求task topology、
  verifier与coordination tax。ARIES提供早期受限case，没有新的长期机制缺口。
- **Integration Decision:** `Books Pending — No Change Candidate`。后续Books pass只验证现有论点，不追加headline数字。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；因无artifact保持作者实验边界，不修改Books。
- **Open Questions:** official code/commit、action parser/legality、matched token/latency/energy、independent seeds、heterogeneous
  policy/reasoner、external verifier、weakly structured/open-world tasks、failure recovery、state persistence与security。

### GUI Pivot: Curriculum Must Bridge the Interface Seen by Perception and Action

- **Candidate / Week / Score:** GUI Pivot / Query Inference / 2025-W09 / 26/30。
- **Source Family ID:** `gui-pivot-query-inference-coordinate-intent-action`。
- **Source Type:** arXiv v1 + author official preprocessing/training-data/evaluation repository；v2属同一family。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-03-01；v2 2025-03-04。W09以v1为owner event。
- **Direct Primary Sources:** https://arxiv.org/abs/2503.00401；https://arxiv.org/html/2503.00401v1；
  https://github.com/ZrW00/GUIPivot。
- **Related Primary Sources:** UIBERT、AndroidControl、AITZ与OS-Atlas是dataset/baseline dependencies；其原始claims不由本论文代替。
- **Access and Verification Status:** v1全文、tables、appendix、prompts与current official repo/data instructions已核验；repo无
  immutable W09 release/tag，current main不能证明全部event-time artifact状态。
- **Full-read Coverage:** grounding/reasoning task equations、small-data preliminary study、query refinement/re-grounding/filter、
  four training branches、datasets/models/metrics/hyperparameters、scale/CoAT ablations、limitations/ethics、artifact layout与evaluation scripts。
- **Original Problem:** GUI grounding训练的是“screenshot + low-level element query → coordinate”，实际Agent需要“screenshot + user intent →
  typed action + parameters”。在小数据下，两个interface不同，坐标监督不自然迁移到intent-conditioned action prediction。
- **Why the Previous Design Was Reasonable:** grounding具有清晰局部label、易从UI data扩展，百万级数据可训练视觉定位；下游SFT再
  学action protocol。大规模grounding、element-level automation或低层pointing任务中该分支仍有效。
- **Changed Constraint:** personalized/on-device场景只有约1K–10K perception samples，无法依赖13M级grounding；同样数据预算下，
  supervision必须同时保留coordinate sensitivity并接近下游query/action语义。
- **Mechanism:** 从UIBERT screenshot与coordinate反向生成高层intended query；再用原grounding model把生成query re-ground，
  只有predicted center落在原box内才保留，形成9,570个`<screenshot, refined query, coordinate>` triplets。先做query-inference
  pretraining（或与grounding各半），再在AndroidControl/AITZ做action SFT。
- **State Ownership:** source UI sample拥有screen/coordinate label；refiner提出intent query；re-grounding model只做consistency
  filter，不拥有真实user intent；downstream demonstrations拥有action labels；runtime OS/environment才拥有action outcome与authority。
- **Control Flow / Data Flow:** UIBERT `(s,q,c)` → query refinement `(s,c)->q_r` → re-ground `(s,q_r)->c_r` → geometric
  containment gate → query-inference dataset → 5-epoch perception pretraining → 3-epoch mobile-action SFT → step-level TMR/AMR evaluation。
- **Implementation Details:** Qwen2-VL-7B-Instruct foundation，OS-Atlas-Base-7B（>13M grounding samples）对照；coordinates归一化
  到[0,1000]，action schema含CLICK/TYPE/SCROLL及benchmark-specific actions；LLaMA-Factory、LR1e-5、FlashAttention inference。
- **Evaluation Contract:** AndroidControl与AITZ test subsets，action type match rate (TMR)和exact action match rate (AMR)；四分支为
  no perception pretrain、grounding、query inference、grounding+query inference。只测offline single-step action prediction，不执行GUI。
- **Baselines / Ablations / Sensitivity / Overhead:** matched 9,570 grounding samples、query/pivot variants、OS-Atlas、1K/2K/5K/full
  scale、screen description/previous action result/action thought/action description。结果显示input semantic context常有益，而output
  reasoning components可降低分数；缺random seeds、confidence intervals、unfiltered/refiner quality、end-to-end trajectory与cost。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/LR/epochs/data size/action distribution披露；GPU、
  precision、batch、image resolution/token length、wall time、latency/concurrency、on-device footprint与SLO为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在Qwen2-VL-7B、UIBERT-derived小数据与两个offline benchmarks中，task-interface更接近
  downstream intent/action的pivot supervision比同规模coordinate grounding更有效；input semantics与output CoT不可视为同一干预。
- **What It Does Not Prove:** generated query等于真实user intent、<0.1% data带来通用data efficiency、OS-Atlas已被全面超过、
  single-step exact match等于trajectory success、local deployment可行，或query inference替代large-scale grounding。
- **Limitations / Threats to Validity:** synthetic/refined query可能保留generator bias，re-grounding是同类model proxy；仅7B和两种
  mobile datasets；后续benchmark SFT仍必需；small-data focus、zero-shot可能下降；无live UI、recovery、safety、cross-app split evidence。
- **Trade-offs / New Failure Modes:** pivot提高supervision relevance并省数据，却依赖query generator/filter共同盲点；严格geometric
  gate提高坐标一致性但不验证intent semantics；vertical tuning可能伤instruction following；input context增加tokens，output CoT可制造
  imitation noise。大规模grounding在广覆盖/zero-shot需求下仍成立。
- **Where the Previous Design Still Applies:** coordinate grounding用于perception primitive；large-scale pretraining用于广泛UI元素覆盖；
  programmatic accessibility tree/API在权限允许时更准确；end-to-end trajectory RL/evaluation用于observation/recovery，而非被single-step SFT取代。
- **Evolution Relationship:** `Layering / Dependency`：coordinate grounding → query-oriented pivot → action-protocol SFT →
  environment trajectory/effect verification；不是视觉定位到GUI Agent的单向替代。
- **ROADMAP Node:** `TRAIN-SFT`（Current Ch29；Legacy Ch25）主 owner；handoff到 `MULTIMODAL-REPRESENTATION`、
  `AGENT-TOOL-CALLING`、`AGENT-WORKFLOW`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch29 demonstration/interface distribution与trajectory SFT，核对Ch23 modality boundary、
  Ch78 typed action proposal、Ch81 effect state和Ch66 component-vs-outcome evaluation。
- **Existing Coverage:** Books已有“训练的是token-level protocol”与training/serving interface一致性，也区分tool proposal和effect；
  但“用pivot task修复pretraining/downstream interface mismatch”可作为长期curriculum机制refine既有论证。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。Historical Books Gate仍关闭。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；artifact chronology与offline/action boundary已保留，未修改Books。
- **Open Questions:** event-time commit、query-refiner identity/quality、seeds/error bars、matched compute、zero-shot regression、live GUI
  trajectory/recovery、cross-app/generalization、accessibility-tree baseline、safety/permissions、on-device latency/memory与independent replication。

### RaPID: Long-form Synthesis Needs an Evidence Plan before a Writing Plan

- **Candidate / Week / Score:** RaPID: Efficient Retrieval-Augmented Long Text Generation / 2025-W09 / 27/30。
- **Source Family ID:** `rapid-long-form-outline-attribute-search-writing-dag`。
- **Source Type:** arXiv v1 + public dataset links；later ACL Findings paper同family。v1未提供可唯一定位的完整official repo URL。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-03-02；arXiv仅一个版本。
- **Direct Primary Sources:** https://arxiv.org/abs/2503.00751；https://arxiv.org/html/2503.00751v1；paper-linked
  FreshWiki-2024 / Wikipedia dump artifacts。
- **Related Primary Sources:** ACL Findings 2025 publication确认later venue/code claim；STORM/Co-STORM repositories只作为baseline lineage。
- **Access and Verification Status:** v1全文、prompts、tables、human eval、limitations、efficiency appendix与data links已核验；
  event-time executable code identity不完整，标记 `Artifact Partially Verified`。
- **Full-read Coverage:** intent/outline retrieval、attribute buffer/query generation、parallel search、outline convergence、section-dependency
  DAG、FreshWiki-2024、four baselines、outline/article/factuality/judge metrics、three backbones、ablation、human study、API usage与limitations。
- **Original Problem:** knowledge-intensive长文同时需要fresh evidence、主题覆盖与跨section coherence；直接生成依赖参数知识，普通
  section-wise RAG会重复或断裂，多Agent讨论扩大视角但传播hallucination并增加latency。
- **Why the Previous Design Was Reasonable:** single-shot/outline RAG实现简单、调用少，适合短报告、已知结构或事实密度低的任务；
  STORM式multi-perspective探索适合未知维度多且人愿意支付额外search budget的场景。
- **Changed Constraint:** 100-topic fresh Wikipedia workload要求在写作前确认intent、系统发现attributes、保存source pool，并按
  section dependency决定生成顺序；质量与API calls/tokens/critical path必须共同约束。
- **Mechanism:** 搜索topic生成brief，并从2.6M Wikipedia outlines检索few-shot结构；从outline抽取atomic attributes、转成queries
  并行搜索，references反向触发add/delete/noop outline更新，直到buffer/outline收敛或budget耗尽。最终把一级sections构成
  dependency DAG，topological order生成，每section只检索所需reference；plan失败时回退parallel generation。
- **State Ownership:** search corpus/results拥有external evidence；outline/attribute buffer拥有coverage proposal；writing DAG拥有
  dependency order；section generator拥有draft；source URL与claim verifier拥有grounding evidence。Outline和LLM judge都不拥有truth。
- **Control Flow / Data Flow:** topic → search brief + outline examples → initial outline → attribute/query buffer → parallel search →
  reference set → iterative outline revision → section DAG/topological order → section-specific retrieval/generation → article metrics/human review。
- **Implementation Details:** DSPy；GPT-4o-2024-11-20、Qwen-Max-2024-09-19、DeepSeek-v3；Google Custom Search top-5；
  e5-large-v2与MiniLM retrievers；Wikipedia dump 2024-08-01；target Wikipedia pages从search/outline corpus排除。
- **Evaluation Contract:** FreshWiki-2024中100个2024-revised topics；outline title exact-match P/R/F1；article ROUGE/entity recall、
  FActScore precision/claims/F1@300、Prometheus-7B四维rubric与info diversity；20 topics由10名master-level volunteers成对评价。
- **Baselines / Ablations / Sensitivity / Overhead:** RAG、outline-RAG、STORM、Co-STORM；移除writing plan；three backbones；API
  calls/tokens/time。RaPID平均31.04 calls、43.62K tokens、127.19s，低于STORM/Co-STORM但高于simple RAG；缺per-module
  search/outline ablation、source citation correctness、live-web replay、judge calibration与cost variance。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** provider model snapshots、top-5与parallelism=3披露；
  hardware/precision不适用于closed APIs且未披露，context/output lengths、rate limits、tail latency、cost、concurrency和SLO不完整。
- **What the Evidence Actually Proves:** 在该Wikipedia-style contract下，先分离coverage discovery、reference pool与writing dependency
  可改善作者所测outline/coherence/factual-density frontier，并比多轮agent discussion减少调用；单一relevance score会奖励短而信息少的文章。
- **What It Does Not Prove:** generated dependencies真实、FActScore/Prometheus等于claim truth、target leakage完全排除、任意long-form/
  finance/science都受益、multi-agent普遍较差，或headline latency在其他provider/limits下成立。
- **Limitations / Threats to Validity:** Wikipedia-only、100 topics、closed/search APIs与model drift、source ranking bias、两人/文章的小型
  human review、exact title matching、LLM judges correlated、缺claim-to-source citations、event-time code identity与multimodal/table evidence。
- **Trade-offs / New Failure Modes:** staged plan提高可归因性却会把错误intent/outline固化到全篇；parallel attributes降低critical path
  却重复/冲突；DAG减少section drift却牺牲并行并可能伪造dependency；multi-agent探索更开放但协调成本更高。简单RAG仍适合窄任务。
- **Where the Previous Design Still Applies:** direct generation用于creative/低风险；outline-RAG用于结构已知；multi-agent用于perspective
  discovery；human editor用于高价值 publication；claim-level provenance与abstention仍需独立gate。
- **Evolution Relationship:** `Layering / Dependency`：single retrieval → outline-guided retrieval → attribute/evidence acquisition →
  dependency-aware artifact synthesis → claim/source verification；RaPID到第四步，未完成第五步。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Current Ch81；Legacy Ch77）主 owner；handoff到 `AGENT-RAG`、`AGENT-PLANNING`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-COST`。
- **Target and Adjacent Chapters Read:** 已读Ch76 evidence retrieval/sufficiency，Ch79 dependency-aware acquisition，Ch81 template/
  realized graph/artifact state，核对Ch66 report/process/provenance evidence；writing plan不能替代source authority。
- **Existing Coverage:** Books已区分retrieval、plan、durable artifact和evaluation，但可refine“evidence coverage plan先于artifact
  dependency plan；二者state owner不同”的演进链。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。Historical Books Gate关闭。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；保留partial artifact与judge/source边界，不修改Books。
- **Open Questions:** exact official repo/event commit、FreshWiki-2024 split/URLs、claim citation、search drift、source-family dedup、
  dependency verifier、module ablations、cross-domain/multimodal、tail latency/cost与independent reproduction。

### Babel: Model Growth Requires a Recovery Phase before Domain Rebalancing

- **Candidate / Week / Score:** Babel Multilingual LLMs / 2025-W09 / 27/30。
- **Source Family ID:** `babel-depth-extension-multilingual-recovery-training`。
- **Source Type:** arXiv v1 + official project/GitHub + released 9B/83B base/chat model cards。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-03-02；arXiv只有一个版本。HF weights更新从2025-03-05起，
  属artifact lineage而非W09 paper event重复评分。
- **Direct Primary Sources:** https://arxiv.org/abs/2503.00865；https://arxiv.org/html/2503.00865v1；
  https://github.com/babel-llm/babel-llm；https://huggingface.co/Tower-Babel/Babel-83B。
- **Related Primary Sources:** project page与Babel-9B/9B-Chat/83B-Chat cards；Qwen2.5是base architecture lineage。
- **Access and Verification Status:** paper全文、data/model/training/eval、official repo与model card已核验；pretraining code、token counts、
  mixture weights、hardware与checkpoint lineage未公开到可复现程度，标记 `Weights Verified / Training Partially Disclosed`。
- **Full-read Coverage:** 25-language selection/data ratios、sources、rule+LLM+linguist cleaning、dedup、extension position/init ablations、
  9B/83B architecture、recovery/continuous stages、six multilingual benchmarks、language-resource analysis、SFT data/training和model cards。
- **Original Problem:** continued pretraining可改变语言distribution，却受原模型capacity ceiling约束；直接扩深又破坏已训练layers的
  coordination。低资源语言数据稀少且质量不均，单纯按web abundance采样会继续偏向高资源语言。
- **Why the Previous Design Was Reasonable:** frozen architecture + continued pretraining最省工程风险，继承optimizer/kernel/runtime，
  适合目标语言接近base coverage或compute有限时；from-scratch multilingual training在规模和完整控制足够时仍合理。
- **Changed Constraint:** 需要覆盖25种高人口语言并提升低资源能力，同时复用Qwen2.5-7B/72B investment；新增layers必须先恢复
  base collaboration，再提高低资源/教材mixture，不能把两种目标混在一次无边界continue training里。
- **Mechanism:** 在第二半每隔一层插入duplicated layer：9B加6层、83B加12层，initial weights为原层复制+mean0.0001
  Gaussian noise。Stage1近均衡采样25 languages并混入高质量英/中corpus恢复性能；Stage2提高低资源语言与textbook比例持续训练。
  数据先rule normalize、Qwen-0.5B classifier（GPT-4o labels+linguist review）和graph/hash dedup。
- **State Ownership:** base checkpoint拥有原capability；extension manifest拥有layer mapping/init；recovery checkpoint拥有结构恢复；
  mixture manifest拥有language/resource weighting；final weights拥有trained behavior；benchmark translation/score不拥有语言人口真值。
- **Control Flow / Data Flow:** multilingual corpora → normalize/quality classifier/dedup → base checkpoint → depth extension →
  Stage1 balanced recovery → Stage2 low-resource/textbook continual training → base evaluation → multilingual SFT → chat evaluation/model release。
- **Implementation Details:** Qwen2.5-7B→9B在layers14..24插入6层，72B→83B在40..62插入12层；attention heads/hidden/
  embedding不变。SFT约1M multi-turn conversations，English40%、Chinese10%，packed max4096，LR4e-6、warmup0.1。
- **Evaluation Contract:** MMMLU/M3Exam world knowledge、MGSM/XCOPA reasoning、XNLI understanding、Flores-200 translation；缺失MMMLU
  languages用Google Translate；比较同量级open models，chat另与GPT-4o比较。Aggregate average混合不同metric，不是单一risk score。
- **Baselines / Ablations / Sensitivity / Overhead:** layer insert vs append、duplicate/zero/noise initialization与noise mean；9B/83B
  base/instruct comparisons、high/low-resource slices、English-only vs multilingual 400K SFT。缺compute-matched plain continued
  pretraining/from-scratch、token/mixture/hardware、seeds/error bars、catastrophic forgetting和deployment latency。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/layer/SFT length/LR披露；pretraining tokens、optimizer、
  precision、batch、GPU topology、training time/energy、inference memory/latency/concurrency/SLO为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者的Qwen-derived checkpoints/data/evals中，depth extension+explicit recovery+language
  rebalancing能形成有竞争力的25-language models；low-resource improvement需要数据质量/mixture而非只增参数；multilingual SFT优于
  English-only SFT on aggregate contract。
- **What It Does Not Prove:** 90% speakers=90% linguistic fairness/quality、layer growth本身造成全部gain、任意architecture可安全扩深、
  aggregate average适合所有语言、Babel在生产成本/安全上优于base，或作者benchmark独立复现。
- **Limitations / Threats to Validity:** training contract大量缺失、translated benchmark contamination/translation error、speaker-count
  与dialect/coverage不等价、公开weights晚于event、no uncertainty、same base/data confounds、licenses/data provenance和safety未详评。
- **Trade-offs / New Failure Modes:** reuse base省from-scratch compute却引入extension shock与recovery phase；balanced sampling提升长尾却
  over/under-sample不同corpora；LLM cleaning扩展质量控制却继承judge bias；新增layers提高capacity也提高memory/latency和serving cost。
- **Where the Previous Design Still Applies:** plain continued pretraining用于小domain shift；adapter/SFT用于行为而非底层coverage；
  from-scratch用于tokenizer/architecture根本变化；固定depth用于runtime/SLO稳定优先时。
- **Evolution Relationship:** `Direct Evolution`：frozen-base continual pretraining → structured depth extension → recovery →
  target-mixture continuation → multilingual SFT；后阶段不覆盖前阶段，而依赖其checkpoint contract。
- **ROADMAP Node:** `TRAIN-PRETRAINING`（Current Ch28；Legacy Ch24）主 owner；handoff到 `TRAIN-DATA`、
  `TRAIN-SFT`、`TRAIN-CHECKPOINT`、`PLATFORM-MODEL-REGISTRY`与`PLATFORM-COST`。
- **Target and Adjacent Chapters Read:** 已读Ch27 data quality/mixture、Ch28 mid-training/objective/scale、Ch29 SFT与Ch35 checkpoint；
  layer extension是training-state migration，不是普通architecture feature list。
- **Existing Coverage:** Ch28已有mid-training、retention/restoration与state-aware width expansion，但depth extension后的separate recovery
  phase可补足“结构迁移→恢复→目标分布”这条机制链。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。不能保留model leaderboard headline。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；model weights与training disclosure边界已分开，未修改Books。
- **Open Questions:** exact pretraining tokens/mixtures、optimizer/precision/hardware、event-time checkpoint commits、compute-matched baseline、
  tokenizer coverage、retention/safety、dialect/fairness slices、serving cost与independent replication。

### LADDER: Self-generated Curriculum Works Only behind an Independent Verifier Boundary

- **Candidate / Week / Score:** LADDER / Test-Time Reinforcement Learning / 2025-W09 / 27/30。
- **Source Family ID:** `ladder-recursive-variant-curriculum-ttrl`。
- **Source Type:** arXiv v1 + author organization repository；v2/v3与later package changes属于same family。
- **Event Date / First-public Date / Revision History:** v1 2025-03-02；v2 2025-03-04；v3 2025-03-05。W09 owner锁定v1。
- **Direct Primary Sources:** https://arxiv.org/abs/2503.00735；https://arxiv.org/html/2503.00735v1；
  https://github.com/Tufalabs/ladder。
- **Related Primary Sources:** HF-linked initial MITIntegrationBee variant code与current Tufalabs package；current repo无release，不能反推W09 code。
- **Access and Verification Status:** v1全文、algorithms、verifier、RL protocol、experiments/discussion已核验；current repo主要实现variant
  generation且citation metadata存在placeholder，event-time full GRPO/TTRL reproduction为 `Partially Verified`。
- **Full-read Coverage:** recursive variant generation、transformation library/diversity controls、numerical verifier、GRPO reward、3B
  train/test design、historical/2025 MIT split、TTRL rollback、baselines/results、failure analysis/future curriculum与repository scope。
- **Original Problem:** hard questions对small model几乎全失败，直接RL group缺少mixed outcomes而collapse；人工课程昂贵。模型可生成
  easier variants，但若没有difficulty structure和executable verification，自训练会复制错误或无信息样本。
- **Why the Previous Design Was Reasonable:** static curated curriculum、SFT或固定external problems可控、易复算；pass@k在问题可解且
  sampling便宜时无需更新weights。开放域/无可靠verifier或高风险模型更新时，旧方案仍更安全。
- **Changed Constraint:** verifiable integration domain允许大量synthetic variants和binary reward；测试题可能OOD，单纯增加sampling仍
  不够，于是test-time compute从“多采样”扩展为“为单题生成课程并临时更新checkpoint”。
- **Mechanism:** 建立数学transformation library，对每题随机给3–5 transformations、每prompt批量10 variants并递归形成difficulty tree；
  用五个随机点附近0.1 intervals做adaptive numerical quadrature，relative error≤1e-2且格式正确才reward。GRPO在train variants上
  更新；TTRL为每个failed test question生成约800 variants、最多100 RL steps，答题后rollback base/LADDER checkpoint。
- **State Ownership:** original problem/split拥有task identity；variant generator只提curriculum；numerical checker拥有proxy verdict；
  official solution拥有MIT final truth；trainer拥有temporary policy；rollback controller拥有per-question isolation。Model自解不拥有reward truth。
- **Control Flow / Data Flow:** source problems → recursive easier/equivalent variants → numerical/edge-case filter → versioned curriculum →
  GRPO → held-out tests；TTRL branch为failed test → per-question variants → temporary update → answer/check → rollback before next question。
- **Implementation Details:** 3B experiment为110 integrals，10 train/100 test、每train约500 variants；MIT branch用2010–2024 exams生成
  9K variants（70% easier/30% equivalent，depth2），2025 exam held out；7B batch128。KL coefficient0.001；hardware/LR等未披露。
- **Evaluation Contract:** Llama3.2-3B的held-out100 problems：pass@1/10、RL without variants、LADDER；7B DeepSeek-R1-Distill-
  Qwen2.5 on 20-question 2025 MIT qualifier；TTRL只应用LADDER仍失败的问题，“任一步答对”视为solved。o1没有checker，非matched comparison。
- **Baselines / Ablations / Sensitivity / Overhead:** no-RL/pass@k/plain RL、variant count、LADDER vs base、TTRL after LADDER vs base；
  numerical exploits被手工补filter。缺matched train/test compute、difficulty calibration oracle、verifier false-positive audit、seeds/CI、
  cross-domain tasks、test-time wall-clock/GPU/memory与contamination beyond exact match。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model sizes、variant counts、steps、7B batch与KL披露；GPU、
  precision、LR、group size、sequence lengths、optimizer/runtime、per-question latency/cost/concurrency和SLO为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者constructed integration workload中，verified difficulty variants把all-fail training distribution
  变成可学习curriculum；plain RL collapse而LADDER gain，TTRL只在已有domain exposure的LADDER checkpoint上解决额外三题。
- **What It Does Not Prove:** autonomous general self-improvement、numerical checker完全正确、TTRL优于matched sampling/solver、任何domain可
  自动产生difficulty gradient、test-time weight update适合shared serving，或90%可以严格超过无checker的o1。
- **Limitations / Threats to Validity:** tiny/custom test、GPT-4o-selected solvable problems、integration-only、numerical tolerance/exploit、
  test-conditioned training与“any step correct”selection、missing compute/seeds、current artifact mismatch、checkpoint pollution/rollback未系统测试。
- **Trade-offs / New Failure Modes:** recursive curriculum扩大near-frontier signal却可能偏离original semantics；verifier便宜却可被hack；
  TTRL提升单题能力却为每题训练checkpoint，增加latency、isolation、cache invalidation、tenant leakage与rollback风险。Static offline RL更可治理。
- **Where the Previous Design Still Applies:** curated datasets用于开放/高风险；plain GRPO用于reward variance足够；pass@k用于无权改weights；
  symbolic checker优先于numeric proxy；offline specialization用于高QPS shared serving。
- **Evolution Relationship:** `Direct Evolution`：fixed task set → generated variants → difficulty-structured verified curriculum → domain RL →
  per-query temporary adaptation/rollback；每一步增加能力也增加state/governance burden。
- **ROADMAP Node:** `TRAIN-GRPO`（Current Ch33；Legacy Ch29）主 owner；handoff到 `TRAIN-DATA`、`TRAIN-CHECKPOINT`、
  `AGENT-WORKFLOW`、`PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch27 feedback curriculum、Ch33 group variance/verifier/role separation、Ch35 checkpoint，核对
  Ch81 sequential refinement/rollback与Ch66 verifier artifact；TTRL是training state，不是普通prompt-time reasoning。
- **Existing Coverage:** Books已覆盖failure-driven curriculum、GRPO all-equal groups、verifier hacking与online update rollback；LADDER可
  refine“curriculum proposal owner ≠ solver/update owner ≠ verifier，per-query weights需隔离/rollback”的演进案例。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。headline增益不进入正文。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；current repo不当作event-time完整artifact，未修改Books。
- **Open Questions:** v1 code commit/full trainer、GRPO hyperparameters/hardware、verifier calibration、matched compute/pass@k、domain transfer、
  data contamination、parallel tenant isolation、cache/registry identity、rollback correctness与independent replication。

### Diffusion Veteran: A Planner Is a Factorization of Future State, Action and Selection

- **Candidate / Week / Score:** What Makes a Good Diffusion Planner for Decision Making? / 2025-W09 / 28/30。
- **Source Family ID:** `diffusion-veteran-offline-rl-planner-factorization`。
- **Source Type:** ICLR 2025 Spotlight paper/arXiv v1 + official PyTorch/CleanDiffuser implementation。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-03-01；arXiv只有一个版本。
- **Direct Primary Sources:** https://arxiv.org/abs/2503.00535；https://arxiv.org/html/2503.00535v1；
  https://github.com/Josh00-Lu/DiffusionVeteran；https://openreview.net/forum?id=7BQkXXM8Fy。
- **Related Primary Sources:** CleanDiffuser official library与D4RL benchmark；later integrations不改变W09 event facts。
- **Access and Verification Status:** paper全文、>6K-search methodology、appendix/hyperparameters/validation tasks与official repo已核验；
  event-time hardware/energy/commit tag仍不完整。
- **Full-read Coverage:** planner component taxonomy、controlled-variable procedure、D4RL/main+Adroit validation、DV algorithm、joint/separate
  action、stride/horizon、Transformer/U-Net/depth、CG/CFG/MC selection、policy vs planner、full hyperparameters、efficiency/safety limitations与code。
- **Original Problem:** diffusion planners混用joint state-action vs state-only、U-Net vs Transformer、guided vs unconditional selection、
  different strides/horizons，headline分数无法说明哪一机制有效，也难区分planning与policy。
- **Why the Previous Design Was Reasonable:** Diffuser式joint generation接口简单，U-Net沿用vision经验，reward guidance直接朝高return采样；
  diffusion policy在反应性locomotion、低latency和短credit horizon下比完整planning更便宜。
- **Changed Constraint:** offline behavior datasets包含不同action dimensionality、near-optimal density与long-horizon structure；planner需在
  dataset support内生成future state、选计划并转成当前action，同时控制20-step denoising和50 candidates的推理成本。
- **Mechanism:** DV用DiT1D生成state trajectory，固定current state，unconditional sample N=50 plans并由critic选best；separate inverse-
  dynamics model从current/next planned state产生action。可jump-step stride规划；planner、critic、inverse dynamics分开训练/拥有状态。
- **State Ownership:** offline dataset拥有observed transitions/rewards；planner拥有provisional future states；critic拥有return proxy；
  inverse dynamics拥有state-transition→action mapping；environment拥有actual next state/return。Generated plan不拥有execution authority。
- **Control Flow / Data Flow:** offline trajectories/preprocessing → train state diffusion + critic + inverse dynamics → current state → N denoised
  future plans → critic selection → first transition → action model → environment → repeat/replan；policy branch直接state→action distribution。
- **Implementation Details:** DiT hidden256/head32，2 blocks常规、AntMaze8；Adam LR3e-4、batch128、planner/inverse 1M steps、critic
  200K或1M；DDIM20 steps temp1、inverse DDPM10 temp0.5；horizon32，task-specific stride，discount0.997或IQL-maze shaping。
- **Evaluation Contract:** D4RL Kitchen、AntMaze、Maze2D、MuJoCo normalized online episode return；DV结果500 episode seeds，Adroit
  eight datasets用150 seeds验证。比较BC/IQL/CQL等policies与Diffuser/DD/HD等planners，但部分baseline数字来自文献。
- **Baselines / Ablations / Sensitivity / Overhead:** >6K models；joint/separate action、stride1/2/4/5/8/15/25、Transformer/U-Net及
  parameter scale、depth、CG/CFG/MCSS/none、candidate1/20/50、horizon4/32/40、Adroit validation。缺matched wall-clock/energy、
  visual/POMDP/live transfer、safety constraints与all-baseline reimplementation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** architecture/steps/batch/seeds详细披露；GPU type/count、precision、
  total train time/energy、per-action latency、control frequency、parallel candidates/memory和deployment SLO为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在这些state-based offline-RL tasks中，component interactions决定frontier：high-dimensional action
  常受益state plan+inverse dynamics；Transformer对long dependencies有优势；larger/deeper非单调；unconditional selection只在dataset含
  足够near-optimal trajectories时可能胜guidance；stride是task-dependent temporal abstraction。
- **What It Does Not Prove:** Transformer/MCSS/separate action在所有robotics上最优、6K search形成universal recipe、offline return代表
  physical safety、attention map证明因果planning、diffusion planner适合real-time控制，或model-based/model-free类比是严格分类。
- **Limitations / Threats to Validity:** standard fully observed MDP/state coordinates、offline datasets/reward shaping、huge search selection
  bias、hardware/cost缺失、single return metric、no interpretability/safety、visual/POMDP/offline-online不覆盖、baseline implementation异质。
- **Trade-offs / New Failure Modes:** state-only plan分离action可降低高维joint burden，却把error转给inverse dynamics；MCSS省task-specific
  guidance tuning却需N倍sampling与critic，可选中OOD plan；larger stride减少decision steps却忽略intermediate dynamics；planner更deliberate
  但慢，policy更快却缺long-horizon lookahead。
- **Where the Previous Design Still Applies:** joint generation用于low-dimensional/coupled action；guided sampling用于high-quality trajectory
  稀少；U-Net在local structure/成熟kernel下；diffusion policy用于reactive control；classical planner/controller用于hard constraints。
- **Evolution Relationship:** `Alternative Branch`：reactive diffusion policy ↔ future-state diffusion planner；planner内部再从joint state-action
  → state plan+inverse dynamics，从per-step plan→temporal stride，从guidance→sample-and-select。不是单向替代链。
- **ROADMAP Node:** `MULTIMODAL-EMBODIED-VLA`（Current Ch26；new node）主 owner；handoff到
  `MULTIMODAL-GENERATIVE-PARADIGMS`、`MULTIMODAL-WORLD-MODELS`、`AGENT-PLANNING`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch24 diffusion state/commit、Ch25 transition model边界、Ch26 action representation/controller/
  closed loop与Ch79 search/budget；offline plan proposal不能获得physical execution authority。
- **Existing Coverage:** Ch26已有action chunk/trajectory、hierarchical controller与world-action interface，但缺少“state plan、action model、
  critic selection三权分离”和policy/planner共存条件，可refine现有机制链。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。只沉淀factorization/trade-off，不保留SOTA表。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；实验与生产control contract分开，未修改Books。
- **Open Questions:** event-time commit/hardware、wall-clock/control rate、candidate parallelism、critic OOD/calibration、visual/POMDP、
  offline-to-online、constraint/safety filter、real robot、energy、policy/planner arbitration与independent reproduction。

### Ray 2.43.0: Batch and Online LLM Paths Share Configuration, Not Runtime State

- **Candidate / Week / Score:** Ray 2.43.0 LLM APIs / 2025-W09 / 26/30。
- **Source Family ID:** `ray-2-43-llm-batch-serve-alpha-contracts`。
- **Source Type:** signed GitHub release/tag + versioned Ray 2.43 docs + public RFC + mechanism/failure PRs。
- **Event Date / First-public Date / Revision History:** signed `ray-2.43.0` released 2025-02-27 19:57 UTC，commit `744eaa9`；
  later Ray LLM APIs belong to future version nodes and cannot be read back into this alpha contract。
- **Direct Primary Sources:** https://github.com/ray-project/ray/releases/tag/ray-2.43.0；
  https://docs.ray.io/en/releases-2.43.0/serve/llm/overview.html；https://github.com/ray-project/ray/issues/50639。
- **Related Primary Sources:** https://github.com/ray-project/ray/pull/50054；release-linked backpressure PR #50311、state/accounting PRs；
  vLLM/Ray Data dependencies remain separate source families。
- **Access and Verification Status:** immutable release/tag、versioned docs、RFC与cancellation PR已核验；release明确LLM APIs为alpha，
  no-deprecation stability与production SLO均不成立。
- **Full-read Coverage:** release highlights、Data LLM Processor configs、Serve VLLMService/LLMRouter、OpenAI protocol、multi-model/
  Multi-LoRA/autoscaling examples、Train V2 state tracking、cancellation/backpressure fixes、RFC motivation/design principles与version boundary。
- **Original Problem:** Ray Data和Ray Serve可调度distributed Python workloads，但用户仍需手工组装vLLM engine、batch preprocessing/
  postprocessing、online deployment、router/autoscaling与adapter loading；batch和online路径各自形成不可复用胶水。
- **Why the Previous Design Was Reasonable:** 直接调用vLLM或HTTP endpoint拥有最少抽象、版本边界清楚；通用Ray Dataset/Serve deployment
  保持engine-agnostic。模型少、单一服务或定制runtime强时，手工composition仍更透明。
- **Changed Constraint:** 同一平台同时承担offline batch、OpenAI-compatible online serving、multi-model/LoRA和autoscaling，需要共享model/
  deployment configuration与paved road；但两条路径的queue、cancellation、backpressure和result semantics不同。
- **Mechanism:** `ray.data.llm`以Processor/ProcessorConfig封装本地vLLM replica或HTTP endpoint，并把pre/postprocess接入Dataset；
  `ray.serve.llm`用LLMConfig构建VLLMService，LLMRouter组合一个或多个deployments，Ray Serve负责replica/autoscaling，vLLM仍拥有token/
  KV engine。LoRA通过Serve multiplexing按request动态加载并LRU cache。
- **State Ownership:** Dataset block/operator拥有batch rows；Processor拥有engine/endpoint invocation；Serve controller拥有replica/route/
  autoscaling；vLLM engine拥有request/token/KV；LLMRouter拥有model selection；adapter cache拥有loaded LoRA state。共享config不等于共享in-flight state。
- **Control Flow / Data Flow:** batch: Dataset row → preprocess → local vLLM or HTTP processor → postprocess → dataset sink；online:
  OpenAI request → LLMRouter → VLLMService replica → vLLM engine → stream response。Cancellation/backpressure分别沿Serve request lifecycle传播。
- **Implementation Details:** Ray Data支持`VLLMEngineProcessorConfig`与`HttpRequestProcessorConfig`；Serve config声明model source、accelerator、
  engine kwargs与min/max replicas；Multi-LoRA使用dynamic path、per-replica cache。Release同时修复batched cancellation hang与backpressure propagation。
- **Evaluation Contract:** release没有统一quality/performance benchmark；任何吞吐、latency、scale或LoRA cache结果必须由用户在锁定Ray/vLLM/
  model/hardware/workload下测量。RLlib的100K steps/s是不同workload，不能用于LLM API结论。
- **Baselines / Ablations / Sensitivity / Overhead:** release/API文档没有direct vLLM、custom Ray deployment、KServe等matched comparison，也未提供
  router/autoscaler/cancellation failure matrix；因此本条是机制/version evidence，不是性能论文。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** docs示例含Qwen、A10G、configurable vLLM kwargs/concurrency；
  无统一model、precision、length mix、batch、cluster topology、TTFT/TPOT/goodput、cost和SLO，均 `Not Disclosed / User Defined`。
- **What the Evidence Actually Proves:** Ray 2.43把两种LLM execution path纳入正式但alpha模块，并公开batch processor、online service/router/
  config ownership；cancellation/backpressure PR证明通用batching也有request-lifecycle correctness，不只是吞吐封装。
- **What It Does Not Prove:** batch/online拥有相同semantics、Ray替代vLLM/KServe、alpha API production-ready、LLMRouter执行KV/prefix-aware
  selection、autoscaling满足GPU SLO、或LoRA multiplexing在任意working set下高效。
- **Limitations / Threats to Validity:** alpha/no-deprecation guarantee、version-specific class names、no benchmark、docs/example coverage有限、
  vLLM compatibility drift、HTTP provider semantics、model-download/cold-start、adapter eviction、failure recovery和multi-tenant isolation未闭合。
- **Trade-offs / New Failure Modes:** paved API降低胶水与配置重复，却增加framework coupling、version migration与hidden defaults；shared base+LoRA
  降显存却引入cache miss/compatibility；router简化入口却可能成为selection bottleneck；cancellation/backpressure修复说明抽象层会新增hang/leak风险。
- **Where the Previous Design Still Applies:** direct engine用于单服务/性能调优；plain Dataset map用于非LLM operators；KServe/Kubernetes controller
  用于declarative cross-cluster lifecycle；external gateway用于tenant/auth；static full-model deployment用于adapter working set不稳定时。
- **Evolution Relationship:** `Layering / Dependency`：manual engine composition → framework-level batch/serve adapters → shared config/paved road →
  production identity/evidence/policy；2.43提供第二、三步alpha实现，不拥有最终平台governance。
- **ROADMAP Node:** `PLATFORM-FOUNDATIONS`（Current Ch57；Legacy Ch53）主 owner；handoff到 `INFER-VLLM`、
  `PLATFORM-KSERVE`、`PLATFORM-GATEWAY`、`PLATFORM-GPU-SCHEDULER`与`PLATFORM-PRODUCTION`。
- **Target and Adjacent Chapters Read:** 已读Ch50 vLLM engine ownership、Ch57 platform control/data planes、Ch61 service lifecycle与
  Ch73 production contract；framework wrapper不能进入token scheduler或替代release evidence。
- **Existing Coverage:** Books已明确平台统一identity/state/policy而不重写专业engine，并区分runtime、service controller与gateway；Ray 2.43
  是版本化实现案例，没有新的长期机制缺口。
- **Integration Decision:** `Books Pending — No Change Candidate`。不把alpha class list写入长期正文。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；release facts、RFC intent与production inference明确分开，未修改Books。
- **Open Questions:** W09 exact RFC merge/commit lineage、Data docs recovery、vLLM compatibility matrix、routing policy、prefix/KV awareness、
  cold start、LoRA cache metrics、cancellation/backpressure failure injection、multi-tenant security与production SLO。

### JAX 0.5.1: Sharding Is Part of Compilation Identity, Not Mere Placement Metadata

- **Candidate / Week / Score:** JAX 0.5.1 / 2025-W09 / 25/30。
- **Source Family ID:** `jax-0-5-1-sharding-cache-collective-runtime-contract`。
- **Source Type:** official versioned changelog + PyPI immutable package metadata + linked implementation issues/PRs。
- **Event Date / First-public Date / Revision History:** JAX 0.5.1 changelog与PyPI source/wheel均为2025-02-24；
  0.5.2于2025-03-04发布且只声明修复0.5.1的TPU metric logging / `tpu-info`，属于W10 revision node。
- **Direct Primary Sources:** https://docs.jax.dev/en/latest/changelog.html#jax-0-5-1-feb-24-2025；
  https://pypi.org/project/jax/0.5.1/。
- **Related Primary Sources:** changelog-linked custom-DCE PR #25956、QR PR #20282、multinomial PR #25955与
  DebugInfo issue #26480；0.5.2 changelog用于已知regression lineage，不反写0.5.1能力。
- **Access and Verification Status:** official changelog完整可访问，PyPI上传日期与artifact hash已核验；GitHub release页不可访问，
  但version/date/mechanism由官方docs与immutable package metadata双重确认。未执行2025 artifact benchmark。
- **Full-read Coverage:** 0.5.1全部breaking changes、new features、changes、deprecations、bug fixes，0.5.0前序contract、
  0.5.2紧邻修复、PyPI artifact metadata以及与sharding/cache/collective相关的公开机制边界。
- **Original Problem:** tracing、lowering与compilation具有多层cache identity；若tracing cache忽略输入sharding类型，语义不同的
  placement contract可能复用同一trace。与此同时，CPU multi-process collective、TPU startup与network-backed compilation cache仍需手工配置或承担额外I/O。
- **Why the Previous Design Was Reasonable:** 当sharding主要在lowering/compilation阶段解释时，tracing只按shape/dtype复用可减少retracing；
  CPU collectives保持显式配置避免引入默认backend依赖；为LRU维护access-time文件在cache size受控时是合理的eviction bookkeeping。
- **Changed Constraint:** sharding逐渐进入program semantics与distributed execution identity；同一shape/dtype但不同sharding class可能需要
  不同trace。多主机CPU执行与共享网络cache也从实验路径变成需要更安全默认值的常规工程路径。
- **Mechanism:** 0.5.1把输入`NamedSharding`纳入JIT tracing-cache key，使sharding类型变化触发retrace；CPU collectives
  默认使用Gloo并允许环境变量配置；未启用LRU时不再写compilation-cache access-time文件；另改进TPU v5e+ runtime启动/关闭路径。
- **State Ownership:** JAX tracer拥有abstract value与trace-cache identity；sharding object拥有logical mesh/partition contract；
  lowering/compiler cache拥有compiled artifact；Gloo backend拥有CPU process-group communication；persistent cache拥有artifact与可选LRU metadata。
- **Control Flow / Data Flow:** Python call + shaped/sharded inputs → tracing-key lookup → cache hit或retrace → lowering/compile cache →
  device execution；multi-process CPU collective由Gloo交换buffers；persistent cache只在启用size/LRU contract时更新access metadata。
- **Implementation Details:** changelog示例显示`SingleDeviceSharding`与`NamedSharding`即使数据等价也产生trace miss；
  `JAX_CPU_COLLECTIVES_IMPLEMENTATION` / `JAX_NUM_CPU_DEVICES`可由env设置且collective默认Gloo；TPU优化可能需要VM transparent hugepages。
- **Evaluation Contract:** 唯一披露性能数字是TPU v5e及更新设备startup/shutdown约从17秒降至8秒，并附transparent-hugepage条件；
  persistent-cache条目只声称减少未启用LRU时对large-scale network storage的无效I/O。无端到端训练/推理benchmark。
- **Baselines / Ablations / Sensitivity / Overhead:** 未披露不同mesh、host count、Gloo/MPI对比、retrace frequency、compile latency、
  network filesystem类型或failure injection；无法量化更严格cache key带来的retrace/compile成本与正确性收益。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** TPU结果仅限定v5e+与VM hugepage条件；model、precision、
  sequence length、batch、host topology、并发与SLO均`Not Disclosed`。CPU Gloo条目未披露硬件、网络、process count与collective size。
- **What the Evidence Actually Proves:** 0.5.1正式改变了trace-cache identity和CPU collective默认值；它证明distributed placement
  metadata会影响program-cache correctness，且runtime/cache默认值需要随真实部署环境演进。
- **What It Does Not Prove:** `NamedSharding` key消除所有cache alias、Gloo优于MPI/NCCL/UCC、TPU改进适用于旧设备或任意VM、
  network cache总会更快，或JAX 0.5.1整体提升模型训练吞吐。0.5.2的metric regression也不能忽略。
- **Limitations / Threats to Validity:** release note而非matched study；缺少benchmark与failure matrix；0.5.1引入TPU metric regression；
  current docs可能包含后续链接更新；GitHub release页不可访问，具体commit/PR闭包未完全冻结。
- **Trade-offs / New Failure Modes:** 更完整cache identity提高语义安全，却增加retrace、compile storm与cache fragmentation风险；
  默认Gloo降低CPU multi-host门槛，却可能隐藏backend选择和网络调优；关闭无用atime I/O降低元数据压力，但失去未声明的外部LRU观察信号。
- **Where the Previous Design Still Applies:** 单设备/固定sharding的shape-dtype cache仍最简单；明确MPI/UCC/vendor backend适合已有通信栈；
  启用bounded cache时access-time bookkeeping仍必要；对短作业，TPU startup优化比steady-state throughput更重要，长作业则相反。
- **Evolution Relationship:** `Direct Evolution`：shape/dtype-centric trace identity → lowering阶段识别sharding → sharding进入trace key →
  future cache identity还需包含layout、topology、compiler/runtime version与artifact compatibility。默认collective则是`Alternative Branch`，不是替代所有backend。
- **ROADMAP Node:** `TRAIN-DISTRIBUTED-TRAINING`（Current Ch36；Legacy Ch32）主 owner；handoff到
  `PLATFORM-FOUNDATIONS`、`PLATFORM-MODEL-REGISTRY`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch35 checkpoint/artifact identity、Ch36 collective/runtime contract、Ch37 sharding、
  Ch57 platform boundary与Ch66 evidence contract；版本条目只用于refine cache/sharding identity，不写成JAX产品清单。
- **Existing Coverage:** Ch36已有collective与communication backend分层，但尚未明确“placement/sharding也是编译缓存identity”；
  该长期机制可refine既有论证，同时保留Gloo/MPI/NCCL/UCC的共存条件。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。Historical Books Gate保持关闭。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly与年度账本；未修改Books，未把release性能数字外推为训练吞吐。
- **Open Questions:** cache key是否还需device layout/topology/version、retrace storm可观测性、Gloo failure semantics、backend selection policy、
  multi-controller recovery、shared-cache consistency、0.5.2 regression影响、matched compile/startup/collective benchmark与独立复现。

### FlashMLA v1: Decode Attention Can Be Compute-bound When Model Topology Changes Arithmetic Intensity

- **Candidate / Week / Score:** FlashMLA v1 / 2025-W09 / 28/30。
- **Source Family ID:** `deepseek-flashmla-v1-paged-variable-length-mla-decode-kernel`。
- **Source Type:** DeepSeek Open Source Week Day 1 index + open-source CUDA/CUTLASS artifact/tests + later official deep-dive that explicitly identifies v1 baseline；no W09 release tag or paper。
- **Event Date / First-public Date / Revision History:** repository公开与Day 1 index为2025-02-24；2025-04-22 kernel重写把compute-bound结果从580提升到660 TFLOPS，
  2025-08/09加入SM100/MHA/sparse/FP8能力。W09锁定BF16 dense MLA decode v1，后续能力只作evolution。
- **Direct Primary Sources:** https://github.com/deepseek-ai/open-infra-index；https://github.com/deepseek-ai/FlashMLA；
  https://github.com/deepseek-ai/FlashMLA/tree/main/tests。
- **Related Primary Sources:** https://github.com/deepseek-ai/FlashMLA/blob/main/docs/20250422-new-kernel-deep-dive.md；
  DeepSeek-V2/V3 MLA definition、FlashAttention/Flash-Decoding/CUTLASS作为mechanism lineage，不替代v1 artifact。
- **Access and Verification Status:** Day 1 identity、v1 public contract（Hopper、BF16、paged KV block 64、variable lengths、3000 GB/s/580 TFLOPS）与
  later official v1→v2 comparison已核验；无immutable W09 tag，current main混入后续features，作者benchmark未独立复现。
- **Full-read Coverage:** Open Infra Day 1、current README/version news、MLA decode API/metadata/split/combine、page/block/sequence contract、tests与benchmark入口、
  2025-04 deep-dive的roofline推导、register constraint、old ping-pong vs new seesaw、TMA/cache/tile scheduling与explicit version boundary。
- **Original Problem:** MLA压缩KV state降低cache footprint，但decode仍需对variable-length paged history计算attention；通用FlashAttention/MHA kernel的head/layout、
  page与scheduler假设无法直接匹配DeepSeek MLA，split-KV又会产生partial outputs与online-softmax combine成本。
- **Why the Previous Design Was Reasonable:** 通用attention kernel可移植、覆盖更多shape并共享维护；decode通常被视为memory-bound，优先减少KV读取与kernel launch是合理策略；
  tensor parallel还能分摊heads/compute。对小head count或低arithmetic intensity workload，这些选择仍成立。
- **Changed Constraint:** DeepSeek decode实例不使用tensor parallel，保留128 query heads；MLA的compressed shared KV使每次KV读取被更多query-head计算复用，
  arithmetic intensity约随`2*h_q*s_q`增长，decode在`h_q*s_q≈128`附近可从memory-bound转为compute-bound。
- **Mechanism:** v1先按每个request的`cache_seqlens`、query-head ratio与SM资源生成tile/split metadata，再对block-size-64 paged BF16 KV执行split-KV MLA，
  各split维护online-softmax partial output/LSE，随后combine。v1使用Hopper-specialized warp/pipeline scheduling；后续官方文档称其为old ping-pong-buffer design。
- **State Ownership:** model architecture拥有MLA head dimensions/compressed KV semantics；KV cache/block table拥有page identity与valid length；metadata/tile scheduler拥有
  request→SM/split assignment；kernel拥有partial max/sum/output accumulator；combine拥有跨split normalization/commit；serving engine拥有batch lifecycle与cache validity。
- **Control Flow / Data Flow:** variable-length requests + q + paged BF16 KV/block table → one-time/per-batch metadata/split planning → per-SM KV tiles → QK + online softmax + PV partials →
  split combine/LSE → BF16 output；decode loop复用kernel contract，但batch/cache变化需要重新生成或验证metadata。
- **Implementation Details:** W09 public surface面向Hopper/H800、BF16、page block 64，支持variable sequence lengths；benchmark区分memory-bound与compute-bound shapes。
  Current API的FP8/sparse/prefill/MTP参数属于后续扩展，不能写成v1实现；v1 exact commit、launch bounds和all supported shapes未冻结。
- **Evaluation Contract:** Day 1报告H800上memory-bound约3000 GB/s、compute-bound BF16约580 TFLOPS；later official deep-dive确认旧版本数字并给出H800 3.35 TB/s、
  nominal 990 / throttled约865 TFLOPS roofline上下文。没有完整batch/length grid、latency percentile或end-to-end server SLO。
- **Baselines / Ablations / Sensitivity / Overhead:** W09没有matched FlashInfer/FlashAttention/vLLM baseline、metadata/combine overhead分解、page-size/length/batch sensitivity或error bars；
  4月文档仅比较旧ping-pong与新seesaw，指出新kernel在memory-bound场景约慢2%，不能倒推v1全域优势。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** H800 SXM5/Hopper、BF16、MLA、page block64已披露；具体driver/CUDA、batch分布、
  context-length histogram、cache occupancy、concurrent requests、TPOT/p99、power/clock与production SLO未完整披露。后续CUDA12.8/FP8数字不归v1。
- **What the Evidence Actually Proves:** DeepSeek公开了适配MLA/paged-variable-length decode的可执行kernel contract，并在作者H800条件下展示两种roofline regime；
  它证明“decode必然memory-bound”不是模型无关定律，head topology、TP与KV compression会改变arithmetic intensity和最佳schedule。
- **What It Does Not Prove:** FlashMLA在任意attention/model/GPU/page size下更快、3000 GB/s等于端到端吞吐、580 TFLOPS可外推B200/FP8/sparse/prefill、
  no-TP总是最优、或kernel保证cache identity/failure recovery。后续660/410/640 TFLOPS不属于W09 v1。
- **Limitations / Threats to Validity:** no immutable tag、current repo drift、author microbenchmark、single-vendor Hopper focus、缺matched baseline与latency/SLO；
  MLA-specific dimensions限制portability，metadata/split/combine与serving integration成本未量化，后续文档才解释部分schedule。
- **Trade-offs / New Failure Modes:** model-specific fusion提高utilization，却增加shape/architecture/CUDA耦合与维护成本；split-KV改善parallelism却增加partial state/combine；
  page block64利于TMA/layout却可能增加fragmentation；metadata balancing依赖length snapshot，stale metadata、invalid block table或unsupported shape可导致错误/性能崩塌。
- **Where the Previous Design Still Applies:** FlashAttention/MHA用于通用训练/prefill；memory-centric decode kernel用于低head/small-batch；TP用于模型容量或通信可接受时；
  page-size1/其他paging适合碎片敏感runtime；unfused reference path用于correctness/portable fallback。
- **Evolution Relationship:** `Direct Evolution`：generic dense attention → Flash-Decoding split-KV → MLA-aware paged variable-length kernel →
  schedule按roofline/SM resources特化 → later seesaw/FP8/sparse/SM100。每步以更强workload specialization换取性能并扩大compatibility matrix。
- **ROADMAP Node:** `INFER-TENSORRT-LLM`（Current Ch49；Legacy Ch45，通用execution-plan/kernel owner）主 owner；handoff到
  `MODEL-SELF-ATTENTION`、`MODEL-KV-CACHE`、`INFER-DECODE`、`INFER-PAGED-ATTENTION`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch14 attention、Ch19/45 KV identity、Ch44 decode、Ch47 paging、Ch49 execution kernel与Ch66 evidence；
  kernel拥有tile/split execution，不拥有request admission、KV invalidation、distributed routing或model-level accuracy。
- **Existing Coverage:** Books已有FlashAttention、PagedAttention与decode memory-bound主线，但缺少“MLA/no-TP使decode转为compute-bound”的反例与
  roofline-driven schedule演进；该family可修正过度泛化并补充metadata/combine state/fallback边界。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / W09 Snapshot Not Tagged`。Historical Books Gate保持关闭。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly与年度账本；v1 facts与4月/9月演进明确分层，未把kernel benchmark写入Books。
- **Open Questions:** W09 commit recovery、correctness tolerance、matched FlashInfer/vLLM、metadata/combine cost、shape coverage、page fragmentation、
  dynamic batching/stale metadata、CUDA Graph、TP/no-TP frontier、p99/TPOT、multi-GPU integration、fallback与independent reproduction。

### DeepEP V1: MoE Communication Must Split Throughput and Latency Contracts

- **Candidate / Week / Score:** DeepEP V1 / 2025-W09 / 29/30。
- **Source Family ID:** `deepseek-deepep-v1-moe-dispatch-combine-communication-contract`。
- **Source Type:** DeepSeek Open Source Week official index + open-source CUDA/Python artifact + archived V1 documentation/tests；no frozen W09 release tag or paper。
- **Event Date / First-public Date / Revision History:** Day 2 announcement与public repository为2025-02-25；current main已演进至V2。
  W09结论锁定NVSHMEM-based V1；NCCL Gin、ElasticBuffer、EP2048等V2事实只作后续evolution，不回填V1。
- **Direct Primary Sources:** https://github.com/deepseek-ai/open-infra-index；https://github.com/deepseek-ai/DeepEP；
  https://raw.githubusercontent.com/deepseek-ai/DeepEP/main/docs/legacy.md。
- **Related Primary Sources:** DeepSeek-V3 technical report定义group-limited routing/workload；current V2 README与release用于版本分界；
  V1 issue #39、tests及source tree用于deadlock/buffer/autotuning/implementation boundary。
- **Access and Verification Status:** V1 archived docs、interfaces、requirements、performance tables、network guidance、roadmap/notices与current source tree已核验；
  W09 immutable tag/commit未恢复，作者benchmark未独立复现，current main不能充当原始artifact快照。
- **Full-read Coverage:** Open Infra Day 2、V1 architecture/performance、normal/low-latency API/control flow、dispatch/combine forward/backward、
  buffer sizing、layout/CPU sync、CUDA Graph条件、hook overlap、NVLink/RDMA、routing/congestion、autotuning、unfinished roadmap、undefined PTX与deadlock notices。
- **Original Problem:** MoE把每个token路由到跨GPU experts，形成不规则all-to-all；训练/prefill追求大batch吞吐，decode只有少量token且对tail latency敏感。
  通用collective无法同时贴合token layout、FP8 dispatch/BF16 combine、NVLink/RDMA非对称域与compute overlap。
- **Why the Previous Design Was Reasonable:** NCCL all-to-all或框架collective提供稳定、通用、拓扑抽象，适合规则通信与可移植性；
  单一高吞吐kernel在训练/prefill中能摊销launch和同步成本。模型较dense、EP规模小或网络未知时，通用collective仍更安全。
- **Changed Constraint:** DeepSeek-V3/R1的group-limited routing、跨节点EP和online decode要求通信既利用NVLink/RDMA带宽，又少占SM、避免CPU同步并支持低精度；
  batch从4096-token训练/prefill缩到约128-token decode，使throughput-optimal协议不再latency-optimal。
- **Mechanism:** V1提供两套dispatch/combine：normal kernels先计算token layout，再在NVLink域与RDMA域转发，支持FP8 dispatch、BF16 combine和可控SM；
  low-latency kernels使用pure RDMA与receive hook，让网络传输后台进行且不占计算SM，并以固定最大token/buffer contract支持CUDA Graph replay。
- **State Ownership:** router/top-k indices拥有token→expert意图；layout阶段拥有per-rank/per-expert counts；`Buffer`拥有NVLink/RDMA queues与capacity；
  returned handle拥有combine/inverse routing metadata；NVSHMEM/RDMA拥有remote transport；CUDA events/hooks拥有compute-communication dependency与completion。
- **Control Flow / Data Flow:** hidden states + top-k ids/weights → layout counts/mask → dispatch across NVLink/RDMA → per-expert contiguous tokens → expert GEMM →
  combine using saved handle/top-k weights → origin ranks；backward互换dispatch/combine。Decode可先返回hook，在独立compute后触发/等待receive completion。
- **Implementation Details:** V1依赖NVSHMEM、PyTorch≥2.1、CUDA≥12.3 for SM90；normal path默认24 SM并需cluster autotune；
  low-latency buffer按max tokens、hidden、EP size、experts预分配，QP count等于local experts；缺NVSHMEM时禁用internode/LL功能。
- **Evaluation Contract:** normal benchmark锁定H800、160 GB/s NVLink、CX7 400 Gb/s、4096 tokens/rank、hidden 7168、top-4 groups/top-8 experts、
  FP8 dispatch/BF16 combine、EP8～64；LL benchmark锁定H800/CX7、128 tokens、same hidden/top-8、EP8～256，报告logical bottleneck bandwidth/latency。
- **Baselines / Ablations / Sensitivity / Overhead:** 以硬件理论NVLink/RDMA bandwidth为主要参照；无matched NCCL/Tutel/Megatron baseline、end-to-end model ablation、
  tail percentile、load-imbalance sensitivity、failure recovery或multi-tenant interference。default configs只针对内部cluster，要求用户重新autotune。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** H800 + CX7、hidden 7168、FP8/BF16、4096或128 tokens、top-8、EP8～256已披露；
  node count映射、sequence length、expert capacity/drop policy、concurrent models、p95/p99、training step/decode TPOT与production SLO未完整披露。
- **What the Evidence Actually Proves:** DeepEP V1公开了MoE-aware dispatch/combine state与两类通信协议，并在作者H800/CX7条件下接近相应带宽且给出微秒级LL测量；
  它证明collective API必须暴露routing metadata、buffer ownership和overlap completion，而不仅是一个`all_to_all`调用。
- **What It Does Not Prove:** 在任意topology/RoCE/EP规模都饱和带宽、zero-SM等于zero-overhead、author microbenchmark转化为端到端goodput、
  aggressive PTX在其他GPU正确、queue design无deadlock、或DeepEP替代NCCL/UCC/MPI。V2结果不能倒推V1。
- **Limitations / Threats to Validity:** official code但无immutable W09 tag、author-only microbench、H800/CX7-centric、no end-to-end/SLO/failure study；
  docs明确implementation与V3 paper略有差异，RoCE仅理论兼容，normal path存在CPU wait/CUDA Graph限制，current repo已重构。
- **Trade-offs / New Failure Modes:** specialized kernels换来带宽/latency与overlap，却增加topology/driver/PTX耦合、buffer预留、autotuning与运维复杂度；
  queue省内存但可能deadlock；fixed max buffer更简单却浪费显存；禁用congestion control提升峰值但放大共享fabric interference；AR降低冲突却加latency。
- **Where the Previous Design Still Applies:** NCCL/UCC用于portable collective和非MoE workload；单节点NVLink path无需RDMA；normal path适合训练/prefill；
  low-latency path适合小batch decode；static routing适合轻载，adaptive routing适合重载；固定buffer适合可预测capacity，queue适合显存紧张。
- **Evolution Relationship:** `Direct Evolution`：generic all-to-all → MoE-aware layout/dispatch/combine → throughput/latency双协议 + explicit overlap →
  V2 unified elastic interface/NCCL Gin/更少SM。V2不是对V1的否定，而是以更大buffer和失去0-SM RDMA LL换取scale与简化。
- **ROADMAP Node:** `TRAIN-DISTRIBUTED-TRAINING`（Current Ch36；Legacy Ch32）主 owner；handoff到`MODEL-MOE`、
  `TRAIN-TENSOR-PARALLEL`、`INFER-PREFILL`、`INFER-DECODE`、`INFER-SCHEDULING`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch21 MoE routing/capacity、Ch36 collective/backend、Ch37 partition、Ch43/44 prefill/decode、
  Ch56 scheduling与Ch66 evidence；communication library拥有transport/layout，不拥有router objective、expert placement或fleet admission。
- **Existing Coverage:** Books已有MPI→NCCL/UCC与collective/topology演进，也提到EP all-to-all；但缺少“同一MoE collective按prefill/training与decode拆成双协议”、
  routing handle/receive hook/buffer state及deadlock/undefined-PTX trade-off，可形成重要机制refine。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / V1 Artifact Mutable`。Historical Books Gate保持关闭。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly与年度账本；current V2与W09 V1严格分离，作者microbenchmark不进入Books。
- **Open Questions:** W09 commit snapshot、matched NCCL/UCC/DeepSpeed/Megatron、RoCE与congestion、load imbalance、EP elasticity、failure/timeout/cancellation、
  p99/TPOT、buffer fragmentation、CUDA Graph recovery、security/isolation、V1→V2 migration与independent reproduction。

### DeepGEMM v1: Quantization Layout Is an Executable Contract, Not Merely a Dtype Choice

- **Candidate / Week / Score:** DeepGEMM v1 / 2025-W09 / 28/30。
- **Source Family ID:** `deepseek-deepgemm-v1-fp8-dense-grouped-moe-jit-kernel-contract`。
- **Source Type:** DeepSeek Open Source Week Day 3 index + open-source CUDA/Python artifact/tests + DeepSeek-V3 FP8 workload lineage；no W09 tag or standalone paper。
- **Event Date / First-public Date / Revision History:** Day 3 announcement/repository为2025-02-26；W09 v1只包含Hopper SM90 FP8 dense GEMM与MoE grouped contiguous/masked layouts、JIT与SASS tuning。
  Weight-gradient、NVRTC、1550 TFLOPS、SM100、MQA scorer、FP4/Mega MoE均为2025-04之后节点，不回填。
- **Direct Primary Sources:** https://github.com/deepseek-ai/open-infra-index；https://github.com/deepseek-ai/DeepGEMM；
  https://github.com/deepseek-ai/DeepGEMM/tree/main/tests。
- **Related Primary Sources:** DeepSeek-V3 technical report定义fine-grained FP8 scaling与MoE shapes；current README news/release chronology用于version exclusion；
  CUTLASS/CuTe只作kernel lineage，不替代DeepGEMM evidence。
- **Access and Verification Status:** Day 3 identity、initial public claims（dense/MoE FP8、JIT、~300 core lines、up to1350+ TFLOPS on Hopper）与current legacy/source layout已核验；
  W09 immutable tag/commit未恢复，current main大幅重构，作者benchmark未独立复现。
- **Full-read Coverage:** Open Infra Day 3、README chronology/requirements/interfaces、dense/grouped contiguous/masked GEMM、scaling-factor/TMA layout、casting boundary、
  JIT/cache/config surface、tests/legacy tree及明确后续news；DeepSeek-V3 FP8 format与DeepEP handoff作为workload contract。
- **Original Problem:** FP8降低GEMM带宽与提高Tensor Core吞吐，但数值范围需要fine-grained scaling；MoE又产生不同expert token counts，导致传统single-shape GEMM与
  generic grouped GEMM在小M、动态layout和decode/CUDA Graph中效率下降。dtype声明本身不包含scale/layout/valid-row语义。
- **Why the Previous Design Was Reasonable:** cuBLAS/CUTLASS提供成熟correctness、广泛shape与architecture支持；BF16避免scale管理；静态expert batch可用普通GEMM循环。
  当shape多变、portability优先或没有Hopper FP8时，这些方案仍更稳健且维护成本更低。
- **Changed Constraint:** V3/R1在训练与推理大量使用fine-grained FP8，并要求dense与MoE GEMM共享低开销kernel；training/prefill有每expert不同token段，decode时CPU可能不知道valid rows且需要CUDA Graph，
  因而kernel必须显式接受contiguous segment或mask layout。
- **Mechanism:** v1以运行时JIT生成SM90 NT-layout FP8 GEMM；dense path执行scaled`A @ B.T`；MoE contiguous path沿M轴拼接各expert tokens并要求block alignment；
  masked path在固定capacity tensor上用GPU mask跳过invalid rows，直接消费DeepEP low-latency dispatch布局，避免CPU读回token counts。
- **State Ownership:** producer拥有FP8 values与fine-grained scale；layout transformer拥有TMA-aligned/transposed scale metadata；JIT cache拥有shape/config→binary identity；
  contiguous offsets或mask拥有expert valid-row identity；GEMM kernel拥有accumulation/output；DeepEP拥有dispatch/combine，不由DeepGEMM重做通信。
- **Control Flow / Data Flow:** BF16 activation/weight → upstream quantize + scale/layout transform → dense or expert-grouped FP8 tensors → shape/config JIT lookup/compile →
  TMA load + tensor-core GEMM + scaled accumulation → BF16 output；MoE path接收DeepEP layout，expert compute后再由combine返回origin ranks。
- **Implementation Details:** W09面向SM90/Hopper、CUDA≥12.3、PyTorch≥2.1、C++20，核心基于CUTLASS concepts但减少template依赖；v1支持dense、M-axis grouped contiguous与masked decode layout。
  Casting/transposition不由GEMM kernel负责，必须在上游实现或fusion；current SM100/FP4/BF16/weight-grad APIs不属于v1。
- **Evaluation Contract:** Day 3只报告Hopper上最高1350+ FP8 TFLOPS并声称多数matrix sizes优于expert-tuned kernels；公开tests覆盖dense/grouped shapes与reference comparison，
  但W09没有完整shape表、clock/power、precision error、baseline version、warmup、JIT amortization或端到端model contract。
- **Baselines / Ablations / Sensitivity / Overhead:** 缺matched cuBLAS/CUTLASS/Triton全矩阵、quantize/layout/JIT overhead、small-M/imbalance sensitivity、seed/error与SASS ablation；
  后续1550 TFLOPS和NVRTC 10x compile是future revisions，不能作为v1 evidence。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Hopper/H800、FP8 fine-grained scale、dense/MoE已披露；具体M/N/K grid、token/expert distribution、
  CUDA/driver/clock、batch/concurrency、training step/decode latency、energy/cost与SLO未完整披露。1350+是kernel peak，不是model tokens/s。
- **What the Evidence Actually Proves:** DeepGEMM公开了把FP8 scale、TMA layout、expert segmentation/mask和JIT config视为一体的可执行kernel interface；它说明MoE计算优化必须与dispatch layout、
  CUDA Graph及quantization metadata协同，而不能仅把BF16替换成FP8。
- **What It Does Not Prove:** 任意shape/architecture都优于vendor BLAS、FP8无accuracy损失、1350 TFLOPS转化为端到端goodput、JIT免费、masked layout消除所有CPU sync、
  或DeepGEMM取代CUTLASS/Triton。current Mega MoE/SM100能力不属于W09。
- **Limitations / Threats to Validity:** no W09 snapshot/tag、author-only peak claim、Hopper/NT-layout-centric、current code drift、无完整accuracy/end-to-end/failure evaluation；
  upstream quantization/transposition成本被排除，JIT cache invalidation与compiler/SASS compatibility未在初版量化。
- **Trade-offs / New Failure Modes:** specialization提高Tensor Core利用率，却增加shape explosion、JIT cold start/cache、compiler/driver与layout耦合；fine-grained scales改善数值却增加metadata/transform bandwidth；
  contiguous layout高效但需padding/alignment，masked layout支持graph却浪费fixed-capacity compute/storage并可能因stale mask算错。
- **Where the Previous Design Still Applies:** BF16用于数值/portable fallback；cuBLAS/CUTLASS用于广泛shape与多GPU代际；Triton用于快速迭代；contiguous layout适合training/prefill已知counts；
  masked layout适合decode/CUDA Graph；普通GEMM loop适合expert少且M稳定的场景。
- **Evolution Relationship:** `Direct Evolution`：vendor/general GEMM → FP8 fine-grained scaling → MoE-aware contiguous/masked grouped GEMM + JIT →
  later weight-grad/NVRTC/SM100/indexer → Mega MoE communication-compute fusion。每步增加fusion与specialization，也扩大artifact/version/cache contract。
- **ROADMAP Node:** `INFER-TENSORRT-LLM`（Current Ch49；Legacy Ch45，通用execution-plan/kernel owner）主 owner；handoff到`MODEL-MOE`、
  `TRAIN-PRETRAINING`、`TRAIN-DISTRIBUTED-TRAINING`、`INFER-DECODE`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch21 MoE、Ch28 precision/objective、Ch36 communication、Ch44 decode、Ch49 kernel/execution与Ch66 evidence；
  DeepGEMM拥有compute/layout/JIT，不拥有router、communication、quantization policy或serving admission。
- **Existing Coverage:** Books已有FP8、GEMM fusion与MoE kernel案例，但缺少scale/layout/mask/JIT作为一个artifact identity，以及contiguous training/prefill与masked decode的条件分支；
  该family可refine执行计划而不保存厂商peak表。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / W09 Snapshot Not Tagged`。Historical Books Gate保持关闭。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly与年度账本；W09 v1与后续SM100/Mega MoE严格分离，1350+ TFLOPS不写入Books。
- **Open Questions:** W09 commit、full shape/config table、accuracy/error、quantize/layout overhead、JIT cold start/cache invalidation、compiler/driver portability、
  expert imbalance、mask correctness、end-to-end step/TPOT、energy/cost、fallback与independent reproduction。

### DualPipe Code Artifact: Pipeline Scheduling Co-designs Dependency Order, Memory, and Communication Overlap

- **Candidate / Week / Score:** DualPipe code artifact / 2025-W09 / 27/30。
- **Source Family ID:** `deepseek-dualpipe-bidirectional-pipeline-overlap-artifact`。
- **Source Type:** 2025-02-27 official code artifact + DeepSeek-V3 technical report + profile data；mechanism first-public predates 2025 scope。
- **Event Date / First-public Date / Revision History:** DualPipe mechanism随DeepSeek-V3 report v1于2024-12-27公开；W09 event是2025-02-27 code opening。
  Current repo加入DualPipeV，属于later derived schedule，不反写初始artifact；本周记录artifact/evidence node，不重复发明日期。
- **Direct Primary Sources:** https://github.com/deepseek-ai/DualPipe；https://arxiv.org/html/2412.19437v2#S3.SS2.SSS1；
  https://github.com/deepseek-ai/profile-data。
- **Related Primary Sources:** ZeroBubble/ZB1P、1F1B、Chimera原论文用于schedule baseline；Open Infra Day 4只证明code release chronology。
- **Access and Verification Status:** report全文相关architecture/infra/evaluation/limitations、DualPipe schedule/formulas/example code与profile artifact可访问；
  production HAI-LLM integration未开源，example要求用户实现module-specific overlap，未独立复现2048-H800 run。
- **Full-read Coverage:** report cluster/training framework、DualPipe decomposition/bidirectional schedule、bubble/memory comparison、cross-node EP overlap、memory techniques、
  training stability/scale；repo schedule diagrams、1F1B/ZB1P comparison、examples/requirements、custom overlap boundary与later DualPipeV分界。
- **Original Problem:** 64-way cross-node EP使all-to-all communication与compute约1:1；传统1F1B只沿一个pipeline方向推进，bubble随PP stages增长，
  communication若串行会吞噬fine-grained MoE的计算收益。
- **Why the Previous Design Was Reasonable:** GPipe/1F1B依赖清楚、单份参数、调试与framework支持成熟；ZeroBubble拆分weight-gradient降低bubble；
  当communication较轻、模型不使用跨节点EP或memory紧张时，单向schedule的简单性与较低parameter residency仍有优势。
- **Changed Constraint:** DeepSeek-V3使用16-way PP、64-way EP跨8节点且不使用TP；需要同时隐藏PP send/recv和EP dispatch/combine，并保持较低bubble，
  仅靠更快collective不足以解决dependency/order问题。
- **Mechanism:** 把每个forward/backward chunk拆成attention、EP dispatch、MLP、EP combine与PP communication；backward再拆input-gradient和weight-gradient。
  两个pipeline方向从两端同时注入micro-batches，重排互不依赖的forward/backward components，并调节communication/compute占用SM比例实现overlap。
- **State Ownership:** scheduler拥有micro-batch direction/stage/time-slot；pipeline rank拥有两份参数分片与activation queue；autograd拥有input/weight gradient依赖；
  EP runtime拥有dispatch/combine completion；PP channel拥有boundary tensors；barrier/event拥有跨stream commit。模型层本身不决定schedule。
- **Control Flow / Data Flow:** micro-batches从pipeline两端进入 → per-stage forward attention/dispatch/MLP/combine → PP transfer；
  与反向micro-batch的input-grad/weight-grad交错 → gradient accumulation → optimizer step。只有dependency与buffer lifetime满足时才能真正重叠。
- **Implementation Details:** report要求even PP stages，DualPipe参数副本2×、peak activation约PP+1；repo提供PyTorch examples但真实module必须实现
  `overlapped_forward_backward`。DeepSeek使用custom all-to-all kernels并手动分配communication vs compute SM，说明schedule与kernel/topology不可分离。
- **Evaluation Contract:** report环境为2048 H800、8 GPUs/node、NVLink/NVSwitch、IB，训练使用PP16/EP64/ZeRO-1；主要证据为bubble公式、profile timeline与
  14.8T-token run整体稳定性。没有isolated DualPipe wall-clock ablation、matched hardware run或SLO。
- **Baselines / Ablations / Sensitivity / Overhead:** 理论比较1F1B、ZB1P、Chimera；bubble为`(PP/2-1)(F&B+B-3W)`，参数2×、activation PP+1。
  未披露micro-batch count/imbalance、stage variance、communication jitter、failure/restart、optimizer boundary或compiler scheduling sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 2048 H800、PP16、EP64、ZeRO-1、FP8 training与V3 workload已披露；
  per-microbatch size、sequence mix、exact stage timing、network contention、memory bytes、step latency/goodput/error bars未完整披露。
- **What the Evidence Actually Proves:** DualPipe公开了一种把pipeline dependency DAG与EP communication overlap共同设计的schedule，并给出可执行示例、
  bubble/memory公式及大规模训练使用证据；它证明pipeline优化不只是减少空闲格，还要显式拥有communication completion与activation lifetime。
- **What It Does Not Prove:** 所有workload都full overlap、理论bubble等于实际speedup、两份参数成本可忽略、DualPipe普遍优于1F1B/ZB1P/Chimera、
  或example代码可直接替换production runtime。整体V3稳定性不能归因于单一schedule。
- **Limitations / Threats to Validity:** mechanism paper v1 pre-window、code release后无production integration、author profile/no matched ablation、DeepSeek-specific EP/topology、
  custom overlap callback留给用户；DualPipeV是later branch，current README混合version lineage。
- **Trade-offs / New Failure Modes:** overlap降低bubble/visible communication，却增加2×parameter residency、activation queue、双向dependency与stream/barrier复杂度；
  stage time不均、collective jitter或错误SM配比会破坏overlap，buffer reuse过早可污染activation/gradient，failure recovery需要重建双向in-flight state。
- **Where the Previous Design Still Applies:** 1F1B用于简单/内存受限pipeline；ZB1P用于不愿复制参数但可拆weight-grad；Chimera用于满足其micro-batch约束的双向schedule；
  no-PP/TP或单节点训练无需DualPipe；communication不重时应优先降低复杂度。
- **Evolution Relationship:** `Direct Evolution`：GPipe fill-drain → 1F1B activation-memory control → ZeroBubble gradient decomposition →
  bidirectional DualPipe + EP/PP overlap → later DualPipeV减少设备数。收益来自依赖重排，代价是更多resident state与recovery complexity。
- **ROADMAP Node:** `TRAIN-PIPELINE-PARALLEL`（Current Ch38；Legacy Ch34）主 owner；handoff到`TRAIN-DISTRIBUTED-TRAINING`、
  `MODEL-MOE`、`TRAIN-ZERO`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch36 distributed runtime、Ch38 pipeline、Ch39 ZeRO、Ch21 MoE与Ch66 evidence；
  DualPipe拥有schedule/dependency，不拥有collective kernel、expert placement、optimizer semantics或cluster admission。
- **Existing Coverage:** Books已有GPipe→1F1B→ZeroBubble与DualPipe概览，但缺少双向in-flight state、2×parameter/PP+1 activation、
  communication-SM co-design和failure/recovery trade-off的完整演进，可refine而非追加项目介绍。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Mechanism Pre-window`。Historical Books Gate保持关闭。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly与年度账本；明确区分2024 mechanism first-public与2025 code artifact，未修改Books。
- **Open Questions:** initial artifact commit、production callback、matched ablation、stage imbalance、micro-batch sensitivity、collective jitter、
  deadlock detection、checkpoint/drain/restart、optimizer step boundary、memory bytes、DualPipeV migration与independent reproduction。

### EPLB Initial Artifact: Router Load, Replica Count, and Physical Placement Are Different Control Loops

- **Candidate / Week / Score:** EPLB initial artifact / 2025-W09 / 26/30。
- **Source Family ID:** `deepseek-eplb-redundant-expert-replication-topology-placement`。
- **Source Type:** 2025-02-27 official code artifact + immutable initial-commit identity + README/148-line planner + DeepSeek-V3 routing/placement lineage；no paper-specific evaluation。
- **Event Date / First-public Date / Revision History:** initial commit `f9bc62e` authored 2025-02-26，Day 4 announcement 2025-02-27；
  March 21 added GPU-level balancing for global policy and March 24 fixed device handling，both are later revisions and cannot be read into W09 behavior。
- **Direct Primary Sources:** https://github.com/deepseek-ai/EPLB；https://github.com/deepseek-ai/EPLB/commit/f9bc62e84182eee311ec97c3ec3ce38f5073a646；
  https://raw.githubusercontent.com/deepseek-ai/EPLB/main/eplb.py。
- **Related Primary Sources:** https://arxiv.org/html/2412.19437v2#S2.SS1.SSS2；Open Infra Day 4 chronology；
  DeepEP/serving overview only define downstream dispatch/runtime，not planner correctness。
- **Access and Verification Status:** current README/code/commit chronology与initial SHA已核验；initial commit content cache不可访问，
  因而March improvements已从W09 claim中排除，exact initial global-policy implementation标记`Partially Recovered`。没有production deployment controller。
- **Full-read Coverage:** README problem/policies/example、全部`eplb.py` greedy packing/replication/hierarchical/global branches与mapping construction、
  commit chronology、V3 group-limited routing/redundant experts、scope exclusion of load prediction与runtime handoff。
- **Original Problem:** MoE router对不同experts产生非均匀且随workload漂移的token load；静态“一expert一GPU位置”让hot expert拖慢整层，
  并在group-limited routing下产生跨节点traffic。仅优化router loss不能决定physical replica/placement。
- **Why the Previous Design Was Reasonable:** 固定expert placement简单、checkpoint identity稳定、无需迁移权重/KV或更新routing table；
  auxiliary load-balancing loss可在训练期约束均匀性。负载稳定、专家少或显存紧张时，不复制仍是更低状态成本的方案。
- **Changed Constraint:** online/prefill/decode workload分布不同，aux-loss-free routing允许自然specialization，hot experts不可避免；
  node内NVLink快于node间网络，EP size与group/node整除关系改变，因此replication与topology-aware placement需要独立控制平面。
- **Mechanism:** planner接收每层logical-expert load与physical replica budget；贪心复制当前`load/replica_count`最大的expert以近似降低max replica load；
  hierarchical policy先按group aggregate load平衡到nodes，再在node内复制hot experts并定长贪心pack到GPUs；global policy忽略groups全局复制/放置。
- **State Ownership:** load estimator拥有历史统计/forecast且repo明确不负责；planner拥有logical↔physical mapping与replica count；model registry/checkpoint拥有logical weights；
  deployment/runtime拥有physical replica materialization/migration；router/dispatcher必须消费新map；GPU/node topology拥有placement constraints。
- **Control Flow / Data Flow:** runtime counters → moving-average/forecast（外部）→ `[layers, logical experts]` weights → choose policy → replicate hot logical experts →
  pack groups/nodes/GPUs → emit `phy2log/log2phy/logcnt` → copy/migrate weights → atomically publish routing map → dispatch按new epoch执行。
- **Implementation Details:** current code用descending-weight greedy fixed-cardinality bin packing，replication逐次选择最大`weight/logcnt`；hierarchical path要求groups可整除nodes、GPUs可整除nodes、
  physical experts可整除GPUs。W09 initial global GPU packing细节因后续commit不可倒灌而保持partial。
- **Evaluation Contract:** repository只给2-layer、12 logical experts/layer、16 replicas、4 groups、2 nodes/8 GPUs worked example；
  无真实load trace、throughput/p99、migration time、memory overhead、optimality gap、rebalancing interval或failure benchmark。
- **Baselines / Ablations / Sensitivity / Overhead:** 无no-replication、random/round-robin、ILP/min-cost-flow、online controller等matched baseline；
  未测试load noise/window、replica budget、group/node divisibility、oscillation、weight-copy/network overhead或stale map。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** example仅给logical/physical counts与2-node/8-GPU topology；GPU/NIC、model size、expert weight bytes、
  precision、prefill/decode mix、concurrency、SLO均`Not Disclosed`。README只建议moving average，不给window/operating point。
- **What the Evidence Actually Proves:** EPLB公开了把load observation、redundant expert count与topology-aware physical placement分离的可执行heuristic，
  并产出双向identity map；它证明MoE“负载均衡”不仅是training objective，也有deployment-state/controller层。
- **What It Does Not Prove:** greedy plan最优、moving average足够预测、rebalance在线无中断、hierarchical总优于global、复制hot expert自动降低p99、
  或planner包含weight migration/atomic cutover/failure rollback。current March fixes不能算W09功能。
- **Limitations / Threats to Validity:** initial content partially inaccessible、only worked example、no tests/benchmark/production controller、load prediction out of scope；
  heuristic assumes divisible topology/fixed capacity，忽略heterogeneous GPU/NIC、copy cost、failure domain与tenant isolation。
- **Trade-offs / New Failure Modes:** redundant replicas降低hotspot却占用weight/HBM并减少distinct capacity；topology locality减IB traffic却限制global balance；
  frequent rebalance追踪drift却带来copy/churn/cache coldness；stale load会复制错误expert，non-atomic map/weight epoch可misroute，greedy可受局部最优影响。
- **Where the Previous Design Still Applies:** static placement用于稳定load/小模型；router auxiliary loss用于训练期regularization；global policy用于group/node不整除或decode大EP；
  hierarchical用于prefill小EP且group locality强；ILP/offline planning用于变更少但要求更优解的集群。
- **Evolution Relationship:** `Layering / Dependency`：router objective → observe executable token load → replicate hot experts → topology-aware placement →
  future online migration/atomic epoch/rollback。后层补充前层，不能用placement修复所有router collapse，也不能用router loss替代runtime placement。
- **ROADMAP Node:** `MODEL-MOE`（Current Ch21；Legacy Ch21）主 owner；handoff到`TRAIN-DISTRIBUTED-TRAINING`、
  `INFER-SCHEDULING`、`PLATFORM-GPU-SCHEDULER`、`PLATFORM-MODEL-REGISTRY`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch21 routing/capacity、Ch36 EP communication、Ch56 inference scheduling、Ch59 registry、Ch63 GPU scheduling与Ch66 evidence；
  EPLB拥有plan，不拥有load predictor、weight transfer、routing cutover或request SLO controller。
- **Existing Coverage:** Books已有router objective→dispatch/placement耦合与expert replication概念，但缺少load estimator/planner/runtime三层owner、
  hierarchical/global条件、dual map epoch与rebalance failure modes；该artifact可refine已有论证。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Initial Snapshot Partially Recovered`。Historical Books Gate保持关闭。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly与年度账本；March improvements明确排除，未修改Books。
- **Open Questions:** initial commit content recovery、load estimator/window、optimality gap、heterogeneous topology、replica budget、weight-copy time、
  atomic map epoch、in-flight requests、cache warmup、oscillation guard、failure rollback、p99/goodput与independent reproduction。

### 3FS Open-source Artifact: Shared AI State Needs Both Strong Data Semantics and Workload-specific I/O Paths

- **Candidate / Week / Score:** 3FS open-source artifact / 2025-W09 / 29/30。
- **Source Family ID:** `deepseek-3fs-disaggregated-rdma-craq-ai-shared-storage`。
- **Source Type:** 2025-02-28 official code artifact + full design notes + benchmark/workload docs + SC24/production lineage；no immutable W09 release tag。
- **Event Date / First-public Date / Revision History:** Open Infra Day 5/public repository为2025-02-28；Fire-Flyer AI-HPC/3FS lineage早于本周。
  Current main持续修复并扩展OS/build/platform，W09锁定公开时的core architecture/workload contract，后续compiler compatibility等只作evolution/operability evidence。
- **Direct Primary Sources:** https://github.com/deepseek-ai/3FS；https://raw.githubusercontent.com/deepseek-ai/3FS/main/docs/design_notes.md；
  https://raw.githubusercontent.com/deepseek-ai/3FS/main/docs/metrics.md。
- **Related Primary Sources:** https://github.com/deepseek-ai/open-infra-index；smallpond/GraySort artifact、USRBIO/fio engine、SC24 Fire-Flyer AI-HPC paper与
  FoundationDB/CRAQ原始设计用于lineage；不以第三方存储宣传替代代码/docs。
- **Access and Verification Status:** README、223-line design notes、metrics、source/config/deploy/tests与performance conditions可访问；
  W09 immutable tag/commit未恢复，current docs可能含后续operability修订，作者production benchmark未独立复现。
- **Full-read Coverage:** component/membership、file/POSIX rationale、FUSE limitations、native async zero-copy Iov/Ior、metadata/chunk mapping、FDB transactions、dynamic attrs、
  CRAQ write/read/version、chain tables/recovery balance、failure leases/state machine、online recovery、chunk engine/COW/allocator、metrics与三类workload benchmarks。
- **Original Problem:** AI训练/推理同时需要海量随机dataset reads、checkpoint并发写、data-prep shuffle、中间文件与跨节点KV reuse；
  local disks要求应用管理locality/prefetch，object store弱化atomic directories/links/POSIX，传统FUSE在small random I/O下受copy与shared-queue lock限制。
- **Why the Previous Design Was Reasonable:** object store便宜、弹性、API简单且适合immutable large objects；local NVMe最低latency；Lustre/GPFS等成熟parallel FS已有生态；
  FUSE降低部署/迁移门槛。顺序大块I/O或cloud-first workload中，这些方案仍可能成本更低且风险更小。
- **Changed Constraint:** 数百storage/client nodes、NVMe与RDMA把bisection bandwidth推高，metadata不能进入data critical path；同一namespace需服务read-heavy training、
  atomic dataset publication、checkpoint和latency-sensitive KV lookup，同时在SSD/服务失败期间保持可解释一致性与带宽。
- **Mechanism:** 3FS分离cluster manager、stateless metadata、storage与client；metadata存于FoundationDB SSI transaction；文件等长chunk跨CRAQ chains条带/复制，
  write-all/read-any；client open时取layout后直接计算chunk/chain。FUSE保兼容，native Iov/Ior提供batched async zero-copy RDMA path。
- **State Ownership:** elected cluster manager拥有membership/chain-table epoch与target public/local states；FDB拥有inode/dentry metadata transaction；meta service无状态；
  storage target拥有committed/pending chunk version；client拥有layout/cache/fd session与I/O completion ring；application拥有buffer lifecycle与fsync/visibility expectation。
- **Control Flow / Data Flow:** open/create → any meta service → FDB transaction/layout → client computes chunk/chain → RDMA request to head/read replica；
  write在chain中pull data→lock→pending version→tail commit→ack反向commit；read-any遇pending可retry/relaxed-read。failure触发lease/state/chain version与background recovery。
- **Implementation Details:** metadata service stateless failover；FUSE path约400K 4KiB reads/s后受spinlock限制；native path共享registered Iov与io_uring-like Ior并batch requests；
  file length active-write时默认5秒上报、close/fsync查询精确尾chunk；read-only fd不跟踪，chunk engine用RocksDB metadata+COW+size-class allocator。
- **Evaluation Contract:** peak-read为180 storage nodes，每节点2×200Gbps IB+16×14TiB NVMe，500+ clients各1×200Gbps，training background traffic下约6.6 TiB/s；
  GraySort为25 storage/50 compute nodes、110.5 TiB/8192 partitions、30m14s、3.66 TiB/min；KV clients各1×400Gbps，peak约40 GiB/s。
- **Baselines / Ablations / Sensitivity / Overhead:** 没有matched Lustre/GPFS/Ceph/S3/local-NVMe、replication-factor、failure/recovery、FUSE-vs-native end-to-end或cost ablation；
  figures缺完整percentiles/error bars，GraySort同时评估smallpond+3FS，不能把全部收益归因于filesystem。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** storage/client/NIC/SSD/GraySort规模已披露；model、KV tensor layout/precision、request size distribution、
  queue depth、replication factor、client concurrency、p95/p99、checkpoint size、failure rate、cost/energy与SLO未完整披露。
- **What the Evidence Actually Proves:** 3FS公开了以transactional namespace + CRAQ versioned chunks + RDMA direct client组合的完整shared-state architecture，
  并在披露cluster条件下展示多TiB/s aggregate workloads；它证明AI storage必须同时定义identity、consistency、recovery和client data path。
- **What It Does Not Prove:** 任意集群线性扩展、6.6 TiB/s可复现/成本最优、disk KV优于DRAM/host cache、FUSE不适用所有训练、CRAQ提供所有POSIX语义、
  或3FS替代object store/parallel FS。File length在active writes中明确只有eventual consistency。
- **Limitations / Threats to Validity:** author-operated production cluster、no matched baseline/cost、W09 snapshot untagged、hardware/resource intensive、
  FDB/RDMA/SSD/lease dependencies；read-only fd不跟踪、concurrent file length、FUSE same-file writes、network partition/fail-stop assumptions与relaxed read需应用理解。
- **Trade-offs / New Failure Modes:** disaggregation简化locality却依赖fabric/bisection；strong chunk consistency增加write chain latency；read-any提高吞吐但pending/retry复杂；
  FUSE兼容但copy/lock受限，native zero-copy快却要求registration/ring ownership；stateless meta易升级但依赖FDB；chain epoch、lease、stale layout或recovery可导致reject/stall。
- **Where the Previous Design Still Applies:** object store用于archive/immutable artifact/cross-region；local NVMe用于ephemeral scratch/ultra-low latency；FUSE用于兼容与大块I/O；
  native API用于small random/performance-critical path；DRAM/HBM KV用于hot set；existing parallel FS用于团队缺少RDMA/FDB运维能力时。
- **Evolution Relationship:** `Layering / Dependency`：local storage + manual locality → object/shared FS → disaggregated all-flash RDMA namespace →
  dual compatibility/native data paths → same substrate承载dataset/checkpoint/KV。新层扩展统一state contract，不否定对象存储或tiered cache。
- **ROADMAP Node:** `PLATFORM-FOUNDATIONS`（Current Ch57；Legacy Ch53）主 owner；handoff到`TRAIN-DATA`、`TRAIN-CHECKPOINT`、
  `INFER-KV-CACHE`、`PLATFORM-MODEL-REGISTRY`、`PLATFORM-MONITORING`与`PLATFORM-PRODUCTION`；记录`Structural Candidate — Shared Storage Plane`。
- **Target and Adjacent Chapters Read:** 已读Ch27 data、Ch35 checkpoint、Ch45 KV、Ch57 platform planes、Ch59 registry、Ch67 monitoring与Ch73 production；
  storage拥有durable bytes/namespace，不拥有dataset semantics、checkpoint commit protocol上层manifest或KV cache admission/invalidation。
- **Existing Coverage:** Books横跨data/checkpoint/KV提到object/PFS/tiering，却缺一个canonical shared-storage owner来解释metadata/data plane、strong consistency、recovery与dual client path；
  该family可能需要在Platform foundations中refine并保留结构候选，而不是重复散落多章。
- **Integration Decision:** `Books Pending — Structural/Refine Candidate / W09 Snapshot Not Tagged`。Historical Books Gate保持关闭。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly与年度账本；性能数字保留完整cluster contract，未修改Books。
- **Open Questions:** W09 snapshot、replication/stripe defaults、cost/TCO、matched PFS/object baseline、failure/recovery goodput、network partition、FDB bottleneck、
  auth/multi-tenancy/encryption、tiering/eviction、checkpoint atomic manifest、KV identity/invalidation、p99与independent reproduction。

### smallpond Open-source Artifact: Shared Storage Can Replace a Long-running Shuffle Service for the Right Batch Workload

- **Candidate / Week / Score:** smallpond open-source artifact / 2025-W09 / 25/30。
- **Source Family ID:** `deepseek-smallpond-duckdb-3fs-ephemeral-dataflow`。
- **Source Type:** 2025-02-28 official code artifact + initial commit chronology + DataFrame/static-DAG docs + executable GraySort benchmark；no system paper。
- **Event Date / First-public Date / Revision History:** initial commit `770aa41`与README update为2025-02-27，Open Infra Day 5 announcement为2025-02-28；
  March 5 reformat不构成机制事件。Current repo只有3 commits，W09 artifact基本可追踪，但PyPI/dependency versions仍可能漂移。
- **Direct Primary Sources:** https://github.com/deepseek-ai/smallpond；https://raw.githubusercontent.com/deepseek-ai/smallpond/main/docs/source/getstarted.rst；
  https://raw.githubusercontent.com/deepseek-ai/smallpond/main/benchmarks/gray_sort_benchmark.py。
- **Related Primary Sources:** https://raw.githubusercontent.com/deepseek-ai/smallpond/main/docs/source/api.rst；3FS design/GraySort conditions；
  DuckDB/Ray/Arrow/Polars只证明dependencies与execution choices，不替代smallpond evidence。
- **Access and Verification Status:** repo/3-commit chronology、high/low-level APIs、logical/execution/io/platform source tree、GraySort script与3FS benchmark conditions已核验；
  no immutable release tag、no matched framework study、initial dependency lock与production failure traces未披露。
- **Full-read Coverage:** README/features/quickstart/performance、getting-started/manual partitioning/monitoring、high-level dynamic Ray backend、low-level static built-in scheduler、
  logical DAG/task/data paths、全部341-line GraySort generation/shuffle/sort/validation plan与3FS hardware/workload contract。
- **Original Problem:** 单机DuckDB对单节点数据高效，但PB-scale preprocessing/shuffle超过单机CPU/memory；Spark/Flink等distributed engine引入长期services、executor/shuffle lifecycle与运维面。
  在已有高吞吐shared FS时，是否可让本地embedded engines各处理partition，并用文件交换替代专用shuffle service？
- **Why the Previous Design Was Reasonable:** Spark/Flink拥有成熟optimizer、shuffle、lineage/retry、streaming/state与multi-tenant governance；长期executors摊销startup并支持iterative workloads。
  单机DuckDB则简单且对中小数据极高效。没有3FS级shared I/O或需要低延迟streaming时，旧方案更合适。
- **Changed Constraint:** DeepSeek已有3FS统一namespace与大规模RDMA bandwidth，batch preprocessing主要是Parquet/SQL/repartition/sort，任务可按files/rows/hash切分；
  因此共享存储可成为intermediate-state/data exchange plane，worker可短生命周期且每task嵌入DuckDB/Arrow/Polars。
- **Mechanism:** 用户构建DataFrame或logical DAG（source→partition/shuffle→SQL/Python task→file sink）；driver把nodes展开为partition tasks；
  high-level API由Ray动态调度，low-level API用built-in scheduler执行static graph；worker本地运行embedded engine，intermediate/output materialize到3FS，免独立shuffle service。
- **State Ownership:** logical plan/driver拥有DAG与task dependency；scheduler拥有resource/attempt lifecycle；dataset/partition descriptors拥有file identity与partition mapping；
  3FS拥有durable intermediate bytes；DuckDB/Arrow/Polars task拥有ephemeral compute state；output/validation marker拥有commit evidence。
- **Control Flow / Data Flow:** discover Parquet files → manual/derived partition plan → schedule independent tasks → local scan/SQL/map → hash/prefix shuffle files on3FS →
  downstream partition sort/aggregate → Parquet/data files → optional valsort validation。Task completion依赖文件可见性而非resident shuffle process。
- **Implementation Details:** getting-started明确目前由用户指定partitions；DataFrame支持file/row/hash repartition、SQL/Python map与Parquet sink；
  GraySort以100-byte records/10-byte keys、prefix buckets，先shuffle到power-of-two partitions，再用DuckDB/Arrow/Polars排序并可运行gensort/valsort correctness。
- **Evaluation Contract:** 3FS+smallpond GraySort使用25 storage nodes（2 NUMA services、2×400Gbps NIC）和50 compute nodes（192 physical cores、2.2TiB RAM、1×200Gbps NIC），
  110.5TiB、8192 partitions、30m14s、3.66TiB/min；script允许shuffle/sort engine、CPU/memory、compression与validation配置。
- **Baselines / Ablations / Sensitivity / Overhead:** 无matched Spark/Flink/Ray Data/Dask/DuckDB single-node、3FS-vs-object-store、scheduler backend、partition count/skew、failure/retry、
  startup或small-file ablation；GraySort是combined smallpond+3FS result，不能隔离framework contribution。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** GraySort cluster/bytes/partitions/time已披露；无LLM model/precision，task concurrency、Ray version、DuckDB version、
  retry count、network utilization、p95 task time、cost/energy与production SLO未完整披露。
- **What the Evidence Actually Proves:** smallpond公开了把embedded analytical engine、file-backed partitions与ephemeral scheduling组合成distributed batch dataflow的可执行实现，
  并在3FS条件下完成110.5TiB sort；它证明shared storage可以承担某类batch shuffle的durable handoff，但只在storage bandwidth/semantics足够时成立。
- **What It Does Not Prove:** smallpond普遍快于Spark/Flink、无需shuffle优化/long-running services、PB-scale claim适用于任意object store、GraySort吞吐全由smallpond贡献、
  或系统具有mature exactly-once/retry/streaming semantics。两套API/backend也尚未统一。
- **Limitations / Threats to Validity:** author-only combined benchmark、no baseline/error bars、3FS依赖、manual partitioning、high/low API分裂、no system paper；
  static/file-materialized design对iterative/streaming workload不利，driver/scheduler failure/commit协议与multi-tenant security未充分公开。
- **Trade-offs / New Failure Modes:** 无长期shuffle service降低运维与内存state，却把intermediate I/O/namespace/cleanup压力交给3FS；embedded engines提高local efficiency但版本/extension需一致；
  manual partition可控却易skew；partial files、duplicate attempts、stale manifests、driver loss、small-file explosion或storage slowdown会传播到整个DAG。
- **Where the Previous Design Still Applies:** Spark用于复杂SQL/成熟batch生态；Flink用于streaming/state/event time；Ray Data用于Python/AI pipeline与动态actors；
  single DuckDB用于单机；object-store-native engines用于cloud。smallpond适合3FS-backed、file-oriented、可物化的large batch preprocessing。
- **Evolution Relationship:** `Alternative Branch`：single-node embedded DB → long-running distributed compute/shuffle engines ↔
  shared-storage-backed ephemeral embedded tasks。它不是Spark/Flink的下一代替代，而是将control complexity换成storage bandwidth/durability的不同系统分解。
- **ROADMAP Node:** `TRAIN-DATA`（Current Ch27；Legacy Ch23）主 owner；handoff到`PLATFORM-FOUNDATIONS`、
  `PLATFORM-GPU-SCHEDULER`（通用resource scheduling principle）、`PLATFORM-MONITORING`与`PLATFORM-PRODUCTION`。
- **Target and Adjacent Chapters Read:** 已读Ch27 data pipeline、Ch57 platform planes、Ch63 resource scheduling、Ch67 monitoring与Ch73 production；
  smallpond拥有batch dataflow/partition task，不拥有3FS consistency、streaming semantics、dataset governance或training job lifecycle。
- **Existing Coverage:** Books已有Spark/Flink/Ray与data preparation，但缺少“shared storage替代shuffle service”的alternative branch及其I/O/commit/failure代价；
  可refine现有data-system decomposition，不需新增framework章节。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / 3FS-coupled Evidence`。Historical Books Gate保持关闭。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly与年度账本；GraySort绑定3FS/cluster条件，未修改Books。
- **Open Questions:** exact dependency lock、task retry/idempotency、partial-output commit、driver HA、scheduler backend convergence、auto partition/skew、
  object-store support、small-file GC、multi-tenancy/security、matched Spark/Ray Data、cost/energy与independent reproduction。

### V3/R1 Online Inference System Overview: Each Phase Needs Its Own Parallelism and Load Signal

- **Candidate / Week / Score:** V3/R1 Online Inference System Overview / 2025-W09 / 29/30。
- **Source Family ID:** `deepseek-v3-r1-pd-ep-overlap-multisignal-load-balancing`。
- **Source Type:** 2025-03-01 official production system case + profile data + code families from Days 1–5；no standalone reproducible serving repository。
- **Event Date / First-public Date / Revision History:** Day 6 article committed/published 2025-03-01，owner W09；statistics window为UTC+8 2025-02-27 12:00～02-28 12:00。
  Later Dynamo/serving integrations are separate families，不能反写本案例。
- **Direct Primary Sources:** https://github.com/deepseek-ai/open-infra-index/blob/main/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md；
  https://github.com/deepseek-ai/profile-data。
- **Related Primary Sources:** FlashMLA、DeepEP、DeepGEMM、EPLB与3FS source packets；DeepSeek-V3/R1 reports定义model/precision；
  pricing只用于article的theoretical revenue calculation，不证明actual margin。
- **Access and Verification Status:** full 88-line article、parallelism/topology、overlap stages、three load balancers、24-hour node/token/cache/cost statistics已核验；
  production router/controller/source、traffic trace、SLO percentiles与independent reproduction未公开。
- **Full-read Coverage:** system principles、cross-node EP、PD-specific parallelism、prefill dual-batch overlap、decode attention split/5-stage pipeline、
  prefill/decode/expert load objectives、architecture diagram、precision、diurnal fleet sharing、24-hour tokens/cache/node/cost/revenue caveats及profile data。
- **Original Problem:** 256-expert sparse MoE每token只激活8 experts；若单请求/小batch执行，每expert M过小，GEMM利用率和latency都差。
  放大跨节点EP能聚合batch并减少每GPU resident experts，却引入all-to-all、DP instance skew与phase-specific memory/compute imbalance。
- **Why the Previous Design Was Reasonable:** 单节点TP/DP部署边界简单、通信少、failure domain小；统一parallelism便于容量规划；按request count做round-robin足以处理相近长度请求。
  小模型、低sparsity、低traffic或严格fault isolation时，这些设计仍更合适。
- **Changed Constraint:** V3/R1高sparsity要求极大aggregate batch；prefill计算随input tokens/attention长度，decode受KV length、request count与per-step小GEMM影响；
  同一parallelism和单一queue metric无法同时优化TTFT、TPOT、GEMM efficiency、memory与all-to-all。
- **Mechanism:** PD disaggregation后，prefill deployment用routed-expert EP32、MLA/shared-expert DP32跨4 nodes；decode用EP144/DP144跨18 nodes。
  Prefill把batch拆为2 microbatches交替隐藏communication；decode拆attention并用5-stage pipeline。三类balancer分别管理DP phase load与expert placement。
- **State Ownership:** ingress/router拥有request→prefill/decode instance；prefill balancer拥有attention work/input-token send load；decode balancer拥有KV occupancy/request count；
  EPLB拥有expert replica placement；DeepEP拥有dispatch/combine；3FS/disk cache拥有prefix KV bytes；fleet controller拥有day/night node allocation；model engine拥有token state。
- **Control Flow / Data Flow:** request/prefix lookup → disk-KV hit或prefill EP32 batch → phase handoff/KV state → decode EP144 iteration → output；
  each phase splits microbatches/stages to overlap all-to-all with attention/GEMM；telemetry feeds phase balancers/EPLB and fleet controller adjusts nodes by diurnal load。
- **Implementation Details:** prefill unit 4 nodes、32 redundant routed experts、each GPU 9 routed+1 shared；decode unit 18 nodes、32 redundant routed experts、each GPU 2 routed+1 shared。
  FP8用于matmul与dispatch，BF16用于core MLA与combine；article不公开handoff protocol、queue algorithm、KV identity或failure recovery。
- **Evaluation Contract:** 24-hour all web/app/API traffic，combined peak278/avg226.75 nodes（8×H800/node）；608B input tokens，342B/56.3% disk-KV hits，168B outputs；
  avg generation20–22 tok/s、avg KV length4989；per H800 node约73.7k input tok/s prefill或14.8k output tok/s decode。
- **Baselines / Ablations / Sensitivity / Overhead:** 无single-node/TP、unified deployment、no-overlap、EP degree、no-disk-cache或balancer ablation；
  无TTFT/TPOT percentiles、goodput、error bars、request mix/length distribution、failure days或independent audit，无法隔离每组件贡献。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** H800、8 GPUs/node、EP/DP degrees、FP8/BF16、avg KV4989、24h token/node stats已披露；
  exact batch/concurrency/context histogram、network、cache capacity/eviction、TTFT/p99、availability、power/energy与SLO未披露。
- **What the Evidence Actually Proves:** DeepSeek公开运行了PD-disaggregated、phase-specific EP/DP与multi-signal load balancing系统，并给出真实24h aggregate counters；
  它证明“load”不是单一request count：prefill要看attention/input tokens，decode要看KV/request count，expert path要看receive load。
- **What It Does Not Prove:** 该架构普遍最优、EP144适合其他models/fabrics、communication完全被隐藏、56.3% cache hit可复制、73.7k/14.8k是SLO goodput、
  或545%为actual profit。Article明确actual revenue更低，且tokens/s含cache hits、不同phase不可直接相加。
- **Limitations / Threats to Validity:** vendor case、单24h高负载窗口、no code/controller、no baseline/percentiles/failures、pricing counterfactual；
  web/app/API混合但分布未披露，cache hit计入input throughput，模型/traffic/fabric强耦合，不能形成跨系统benchmark。
- **Trade-offs / New Failure Modes:** large EP改善GEMM/weight locality却扩大failure domain与all-to-all；PD独立扩缩容却新增KV handoff/phase queues；
  overlap提高utilization但增加pipeline state；多balancer更准确却可能目标冲突/oscillation；disk cache省compute但引入identity/freshness/eviction/storage tail latency。
- **Where the Previous Design Still Applies:** colocated prefill/decode用于低traffic/简单运维；TP用于dense/weight-capacity限制；request-count routing用于长度相近；
  DRAM/HBM prefix cache用于hot set；static capacity用于稳定load；smaller EP/failure domains用于availability优先场景。
- **Evolution Relationship:** `Direct Evolution`：single-instance serving → PD phase separation → phase-specific parallelism → communication-compute overlap →
  multi-signal state-aware balancing → diurnal fleet sharing。每一步提高utilization，也新增state owner、handoff、feedback loop与failure semantics。
- **ROADMAP Node:** `INFER-PD-DISAGGREGATION`（Current Ch55；Legacy Ch51）主 owner；handoff到`MODEL-MOE`、`INFER-PREFILL`、
  `INFER-DECODE`、`INFER-SCHEDULING`、`PLATFORM-GPU-SCHEDULER`、`PLATFORM-COST`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch43/44 prefill/decode、Ch52 distributed state、Ch55 PD、Ch56 scheduling、Ch63 GPU、Ch66 evidence与Ch70 cost；
  case拥有phase topology/control signals，不公开gateway/admission、KV transfer correctness或production release process。
- **Existing Coverage:** Books已有PD、state-aware scheduling与KV locality，但缺少phase-specific EP degree、三个load signals、overlap pipeline和fleet time-sharing的统一演进；
  该case可refine现有主线，同时保留vendor workload boundary，不保存545% headline。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Vendor Production Case`。Historical Books Gate保持关闭。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly与年度账本；所有throughput/cost数字绑定24h/model/hardware/precision/phase条件，未修改Books。
- **Open Questions:** request/length distribution、TTFT/TPOT/p99、KV transfer/identity/invalidation、disk-cache capacity/eviction、balancer algorithms/control stability、
  failure recovery、EP degree frontier、network topology、actual cost/revenue、multi-tenant isolation与independent reproduction。

### Wan2.1 Code and Weights Release: Video Generation Scales by Compressing State Before Scaling the Transformer

- **Candidate / Week / Score:** Wan2.1 code and weights release / 2025-W09 / 28/30。
- **Source Family ID:** `wan2-1-causal-video-vae-flow-matching-dit-open-weights`。
- **Source Type:** 2025-02-25 official inference code/weights/model cards + 2025-03-21 same-family technical report + executable inference surface；no open training code at W09。
- **Event Date / First-public Date / Revision History:** code/weights first public 2025-02-25，ComfyUI integration 2月27日，Diffusers 3月3日；technical report v1 3月21日。
  W09 owner是T2V/I2V code/weights；FLF2V、VACE与later community models are separate future nodes。
- **Direct Primary Sources:** https://github.com/Wan-Video/Wan2.1；https://huggingface.co/Wan-AI/Wan2.1-T2V-14B；
  https://arxiv.org/html/2503.20314v1。
- **Related Primary Sources:** Wan2.1 model collection/I2V cards、Wan-Bench artifacts、xDiT integration；
  report后发机制用于解释same family，不能伪装成2月25日已披露内容。
- **Access and Verification Status:** repo/news/version dates、inference code/config/model weights/cards与891-line report全文可访问；
  training pipeline/data/optimizer code未开源，copyright/data proportions与full benchmark artifacts不完整，作者结果未独立复现。
- **Full-read Coverage:** report related work、billions-scale data cleaning/caption/OCR pipeline、Wan-VAE design/training/cache/evaluation、DiT/flow matching、pre/post-training、
  Wan-Bench/human/VBench、I2V and downstream boundaries、efficiency、limitations/conclusion；repo task/resolution/model matrix、single/multi-GPU/offload/prompt extension与version chronology。
- **Original Problem:** raw video state随frames×resolution爆炸，直接pixel-space transformer无法扩展；普通2D VAE忽略temporal causality/coherence，
  generic DiT对long spatio-temporal token sequence成本高；同时consumer GPU与14B quality形成能力/成本分支。
- **Why the Previous Design Was Reasonable:** image diffusion/2D VAE成熟、训练稳定且适合single-frame；3D VAE/latent video diffusion减少compute但可能丢细节；
  large proprietary models可用scale换quality。静态图像、短低分辨率或高fidelity reconstruction时，旧方案仍合理。
- **Changed Constraint:** video需要空间与时间联合压缩、因果chunk processing、text/motion alignment与长序列memory control；开放部署还要求1.3B/14B、480p/720p、
  offload/parallelism等多种execution contract，而非一个checkpoint覆盖所有cost points。
- **Mechanism:** 127M 3D causal Wan-VAE将video压缩为`[1+T/4,H/8,W/8,16]`，首帧只做spatial compression；RMSNorm与feature cache保持causal chunk continuity。
  Latents经3D patchify进入T5-conditioned flow-matching DiT，time embedding生成每block modulation；1.3B与14B形成capacity branches。
- **State Ownership:** data pipeline拥有shot/quality/motion/text/caption provenance；VAE latent/cache拥有spatio-temporal identity与chunk boundary；T5拥有text condition；
  DiT/sampler拥有denoising state/step；I2V condition/mask拥有preserved frame semantics；runtime拥有offload/FSDP/sequence-parallel execution，不拥有model quality。
- **Control Flow / Data Flow:** prompt（optional extension）→ T5 text tokens；video/image training data → 3D causal VAE latents → noisy flow state → DiT cross-attention/modulation →
  iterative sampler → latent video → chunked VAE decode with feature cache → frames。I2V adds first-frame latent/mask condition。
- **Implementation Details:** VAE 4× temporal/8×8 spatial compression、16 latent channels、feature cache最多4-frame chunks；VAE先2D image train→inflate 3D low-res/5-frame→high-quality/GAN fine-tune。
  W09公开T2V 14B/1.3B与I2V 14B inference；current FSDP+xDiT Ulysses/Ring与later tasks按version边界处理。
- **Evaluation Contract:** report Wan-VAE在200个25-frame 720×720 videos比较PSNR/speed；Wan-Bench对每model 1,035 samples并按human-weighted dynamic/image/instruction metrics；
  >700 human tasks/20+ annotators。Repo称1.3B约8.19GB VRAM，RTX4090生成5s 480p约4min（no quantization），需绑定settings。
- **Baselines / Ablations / Sensitivity / Overhead:** VAE比较SVD/Open-Sora/Step/Mochi/Hunyuan等不同compression/latent；generation比较commercial/open models但prompt extension/judge可影响结果；
  缺full training compute、seed/error、data/architecture ablation、sampler steps/CFG/resolution统一成本与independent replication。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 1.3B/14B、480p/720p、RTX4090/offload/5s/约4min与14B single high-end GPU约30min已披露；
  training GPU topology/precision/tokens、batch/concurrency、exact frame count、power/cost、production latency/SLO未完整披露。
- **What the Evidence Actually Proves:** Wan2.1公开了可运行的small/large video foundation model branches与causal latent-video architecture；
  later report在作者条件下证明3D VAE compression/cache、data/caption pipeline和DiT training共同形成video system，而非单纯放大image model。
- **What It Does Not Prove:** Wan学习真实world dynamics/causality、Wan-Bench headline普遍优于commercial models、8.19GB/4min适用于任意prompt/frame/driver、
  infinite-length cache无drift、或14B质量值得所有成本。Video generation不等于controllable world model。
- **Limitations / Threats to Validity:** author benchmark/judge、later report、training code/data rights incomplete、task/version混合、high compute；
  report承认large-motion fine detail、14B约30min和domain expertise不足，VAE compression/cache可能累积temporal artifacts。
- **Trade-offs / New Failure Modes:** latent compression降低sequence/compute却丢细节；causal cache降memory却引入chunk state/drift；1.3B可部署但quality/capacity受限；
  14B提高quality却增加VRAM/latency；prompt extension改善alignment但引入second-model cost/provenance；parallel/offload降低HBM要求却增加communication/host transfer。
- **Where the Previous Design Still Applies:** image diffusion用于single-frame；smaller VAE/model用于edge/iteration；14B用于quality-first offline generation；
  physics simulator/world model用于action-conditioned causal prediction；AR/block diffusion用于不同factorization；no prompt extension用于latency/provenance控制。
- **Evolution Relationship:** `Layering / Dependency`：image VAE/diffusion → causal 3D VAE latent video → flow-matching DiT scale → small/large deployment branches →
  I2V/edit/control extensions。后续任务建立在foundation上，但不应覆盖T2V/I2V owner或被解释为world-model必然演进。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Current Ch24；Legacy N/A）主 owner；handoff到`MULTIMODAL-REPRESENTATION`、
  `MULTIMODAL-WORLD-MODELS`（boundary only）、`INFER-EXECUTION-ENGINE`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch23 representation、Ch24 generation、Ch25 world-model boundary、Ch49 execution与Ch66 evaluation；
  Wan拥有latent video generation，不拥有environment transition/action/control truth。
- **Existing Coverage:** Ch24已有AR/diffusion/flow与video state，但缺少“先用causal VAE压缩时空state，再扩DiT”的完整机制、chunk cache和small/large deployment branch；
  可refine现有演进而不追加model catalog。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Later Report Evidence`。Historical Books Gate保持关闭。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly与年度账本；code-release与later report日期分离，未修改Books。
- **Open Questions:** W09 artifact hash、training compute/data rights、VAE long-video drift、compression fidelity、sampler/CFG frontier、matched evaluation、
  text rendering、motion physics、multi-GPU/offload cost、safety/watermark、independent reproduction与world-model boundary。

### olmOCR Model/Data/Pipeline Release: Evidence Extraction Is a Typed, Retryable Data Pipeline

- **Candidate / Week / Score:** olmOCR model/data/pipeline release / 2025-W09 / 29/30。
- **Source Family ID:** `ai2-olmocr-document-anchoring-vlm-linearization-pipeline`。
- **Source Type:** Ai2 official Blog + arXiv v1 + open model/data/training/inference/evaluation artifacts + initial v0.1.58 release。
- **Event Date / First-public Date / Revision History:** Blog、paper v1、model/data/pipeline v0.1.58均于2025-02-25公开；
  March temperature improvements、May benchmark、June vLLM switch与later olmOCR2 are future revision nodes，不反写W09。
- **Direct Primary Sources:** https://allenai.org/blog/olmocr；https://arxiv.org/html/2502.18443v1；https://github.com/allenai/olmocr。
- **Related Primary Sources:** https://huggingface.co/datasets/allenai/olmOCR-mix-0225；https://huggingface.co/allenai/olmOCR-7B-0225-preview；
  SGLang/vLLM、Qwen2-VL、Poppler/PyPDF与peS2o artifacts用于pipeline/baseline semantics。
- **Access and Verification Status:** 561-line paper、Blog、v0.1.58 chronology、model/data/code、prompt/schema、pipeline/retry与three-level evaluation完整可访问；
  current repo已演进至v0.4，W09 behavior锁定paper/v0.1.58，作者cost/human/downstream结果未独立复现。
- **Full-read Coverage:** related work、document anchoring、teacher/tool selection、266,135-page data composition/sampling、prompt/schema、Qwen2-VL fine-tune、
  SGLang work-item pipeline、cost assumptions、prompt-length/retry/rotation/repetition/fallback、teacher alignment、human ELO、50B mid-training downstream与appendix prompts。
- **Original Problem:** PDF保存glyph/coordinates/rendering而非自然reading order；born-digital text extraction会丢layout/table/equation，纯raster OCR又放弃已有text/metadata并在模糊区域hallucinate。
  单页模型accuracy不足以保证百万页处理的cost、retry、failure recovery和training-data usefulness。
- **Why the Previous Design Was Reasonable:** PyPDF/GROBID等deterministic parsers快、便宜、可审计；OCR适合扫描件；通用GPT-4o能处理复杂layout且无需训练。
  结构简单、需要exact character authority或数据规模较小时，这些分支仍更合适。
- **Changed Constraint:** LLM pretraining/RAG需要跨多栏、表格、公式、手写与扫描件的统一linearized text；数据规模达亿级PDF/百万页时，API teacher成本不可持续，
  同时任何重复、schema failure、rotation或hallucination都会污染下游语料。
- **Mechanism:** document anchoring用PyPDF抽取raw text、image/text block coordinates并按character budget注入prompt，同时提供Poppler raster page；
  GPT-4o以structured schema生成silver labels，fine-tune Qwen2-VL-7B。Inference复用anchor+image，parse JSON/rotation，失败重采样/升温重试，最终fallback plain text。
- **State Ownership:** source artifact拥有PDF bytes/page identity；anchorer拥有text/block/image coordinates与sampling budget；renderer拥有page pixels/DPI；VLM拥有candidate linearization；
  schema/parser拥有typed metadata/text；retry controller拥有attempt/temperature/rotation/fallback；object store/work queue拥有page attempt/commit；dataset manifest拥有provenance。
- **Control Flow / Data Flow:** PDF page → rasterize longest edge2048 + extract anchors → budget/truncate prompt → SGLang VLM request → structured JSON → validate rotation/schema/repetition →
  retry with resampled anchors/temperature or fallback → Markdown/Dolma output → document/page manifest → training/RAG consumer。
- **Implementation Details:** training set 105,504 docs/266,135 pages（99,903 web PDFs + 5,601 public-domain books），约60% academic/12% brochure/11% legal等；
  prompt超过8192 tokens时指数降低anchor character limit。Batch work items约500 pages，workers并发提交all pages并等待engine drain，optional S3协调。
- **Evaluation Contract:** cost table假定A100 $1.89/h、L40S $0.79/h、H100 $2.69/h与20% retries；L40S/H100均约$190/M pages。Teacher alignment、
  2,017 PDFs/2,000 pairs/11 Ai2 raters/452 preferences ELO，以及same-PDF 50B-token OLMo2 mid-training vs Grobid+rules三层证据。
- **Baselines / Ablations / Sensitivity / Overhead:** teacher比较GPT-4o/mini/Gemini/Claude以小规模qualitative筛选；human compares Marker/MinerU/GOT-OCR defaults；
  缺anchor/no-anchor full ablation、language/domain、retry rate distribution、DPI/character budget、multi-GPU scaling curve与external raters。Downstream average +1.3pp有task gains/losses。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Qwen2-VL-7B、2048px page、8192 prompt、500-page work item、A100/L40S/H100 token/cost与20% retry assumption已披露；
  precision、GPU count scaling points、concurrency、page token distribution、p95 latency、storage/network、SLO未完整披露。
- **What the Evidence Actually Proves:** anchor+image+specialized VLM+retry pipeline在作者条件下比pure general parser更接近teacher/human preference，并在same-source 50B mid-training中改变downstream结果；
  它证明source extraction quality是training-system input contract，且生产正确性来自model与typed recovery共同作用。
- **What It Does Not Prove:** olmOCR是字符级ground truth、GPT-4o silver labels无错、ELO>1800泛化所有language/document、$190适用所有cloud/length/retry、
  或+1.3pp全部由OCR质量造成。Fallback/plain-text也不保证table/equation fidelity。
- **Limitations / Threats to Validity:** English filtering、teacher imitation/bias、internal raters、same-distribution PDFs、only452 meaningful judgments、author cost、no full anchor ablation；
  repeated generations可耗尽context/HBM，retry降低throughput，schema-constrained decode当时不可靠，current repo/version drift。
- **Trade-offs / New Failure Modes:** metadata anchors减少hallucination却可能注入corrupt/poisoned PDF text；VLM保layout却非deterministic；temperature/retry恢复collapse却增加cost/variance；
  schema提供typed control却可能OOD collapse；fallback提高completion rate但降低structure；teacher distillation扩大coverage也复制teacher omissions/licenses。
- **Where the Previous Design Still Applies:** deterministic parser/OCR用于exact text与simple PDFs；GROBID用于academic structure；commercial API用于低量/rare layouts；
  human review用于legal/medical/high-value evidence；multimodal RAG可保留page image而非只linearize；abstention/quarantine适合无法验证pages。
- **Evolution Relationship:** `Layering / Dependency`：binary PDF parser/OCR → raster VLM → anchor text+geometry with image → specialized distilled VLM →
  typed validation/retry/fallback → downstream training evidence。后层组合前层，而不是用generative OCR否定deterministic authority。
- **ROADMAP Node:** `TRAIN-DATA`（Current Ch27；Legacy Ch23）主 owner；handoff到`MULTIMODAL-REPRESENTATION`、
  `AGENT-RAG`、`PLATFORM-MODEL-REGISTRY`、`PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch23 representation/provenance、Ch27 data、Ch59 registry、Ch66 evaluation、Ch72 security与Ch76 RAG；
  olmOCR拥有source-to-text artifact，不拥有source truth、retrieval ranking或downstream answer verification。
- **Existing Coverage:** Books已有OCR/parser/RAG与data provenance，但缺少anchor+image typed extraction、attempt/fallback state和“用downstream mid-training验证parser”的证据阶梯；
  可refine现有data pipeline而不新增OCR产品章节。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Teacher and Pipeline Coupled`。Historical Books Gate保持关闭。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly与年度账本；W09 v0.1.58与later benchmark/model明确分离，未修改Books。
- **Open Questions:** multilingual/domain slices、anchor poisoning、character/DPI budget、retry/abstention calibration、page/document atomic commit、duplicate attempts、
  licensing/PII、external human eval、matched parser cost、downstream causality、SLO与independent reproduction。

### Phi-4 Mini/Multimodal Launch Family: Freeze Shared Capability, Route Modality-specific Delta State

- **Candidate / Week / Score:** Phi-4-mini + Phi-4-multimodal launch family / 2025-W09 / 29/30。
- **Source Family ID:** `microsoft-phi4-mini-multimodal-frozen-backbone-mixture-lora`。
- **Source Type:** 2025-02-26 Microsoft official launch + open model/data cards/weights/custom code + 2025-03-03 same-family 31-section technical report。
- **Event Date / First-public Date / Revision History:** sibling models/weights launched 2025-02-26；technical report v1 2025-03-03。
  Reasoning-enhanced Phi-4-mini preview、later ONNX/finetunes/leaderboards are separate revisions and cannot be read as launch facts。
- **Direct Primary Sources:** https://azure.microsoft.com/en-us/blog/empowering-innovation-the-next-generation-of-the-phi-family/；
  https://huggingface.co/microsoft/Phi-4-mini-instruct；https://huggingface.co/microsoft/Phi-4-multimodal-instruct。
- **Related Primary Sources:** https://arxiv.org/html/2503.01743v1；Phi data summary cards、Cookbook/model code；
  LongRoPE/Phi-4/Phi-3.5/SigLIP papers用于lineage，不替代current artifacts。
- **Access and Verification Status:** official launch、both model cards/weights/config/custom code、1031-line report architecture/training/evaluation/safety/limitations可访问；
  exact data mix/artifact hashes、training code与full benchmark logs不完整，vendor results未独立复现。
- **Full-read Coverage:** language architecture/LR scaling/data recipe、vision/audio encoders/projectors/LoRAs/router、multi-stage modality/joint training、
  vision/speech/language/coding/reasoning evaluations、text/audio/vision safety、weaknesses，model-card hardware/data/context/runtime/fine-tuning surface。
- **Original Problem:** separate ASR→LLM→VLM pipelines lose prosody/background/joint cross-modal evidence and multiplymodel/runtime state；
  full fine-tuning one shared multimodal model can overwritelanguage capability，while cross-attention-only adapters may leaveperformance gap。
- **Why the Previous Design Was Reasonable:** specialist models isolate failures、can upgrade independently and provideclear modality contracts；full fine-tuning maximizes joint adaptation；
  cross-attention preserves backbone。Modality rarely co-occurs、memory permits multiple models or safety boundaries differ时，separate pipeline仍合理。
- **Changed Constraint:** edge/compute-constrained deployment wants one 128K checkpoint handling text/image/audio combinations while retaining base language performance；
  modalities have different encoders/data/safety，yet shared decoder weight should not be duplicated or catastrophically interfered。
- **Mechanism:** Phi-4-mini provides frozen3.8B decoder backbone；Phi-4-multimodal addsSigLIP vision encoder/MLP projector/vision LoRA and speech encoder/projector/speech LoRA。
  Modality-specific router selects/combines LoRA deltas according to input mode，supporting text、vision+text、speech、vision+speech while base weights remain unchanged。
- **State Ownership:** tokenizer/base LM owns shared text/decoder state；vision/audio encoders own modality features；projectors own embedding-space alignment；
  each LoRA ownsmodality delta；router owns active adapter composition；KV cache/runtime must bind adapter set+modality inputs to cache identity；application owns modality/safety policy。
- **Control Flow / Data Flow:** text/image/audio → modality encoder(s) → project toLM tokens + common tokenizer → router activates vision/speech LoRA deltas →
  frozen decoder processes combined sequence → text output。Text-only bypassesmodality adapters，joint vision-speech training tunescomposition without updatingbase。
- **Implementation Details:** mini为32 layers、hidden3072、200,064 vocab、tied embeddings、24 Q/8 KV GQA heads与128K LongRoPE；GQA将KV heads降到1/3。
  Multimodal 5.6B以mini为backbone，vision encoder+projector约440M、vision LoRA约370M；vLLM可按request加载speech/vision LoRA，launch code需`trust_remote_code`。
- **Evaluation Contract:** mini/multimodal model cards含internal text/vision/speech suites；report覆盖same-size/larger baselines、ASR/ST/QA/audio/vision-speech、
  language/coding/CoT与safety。Training metadata：mini 512×A100-80G/21 days/5T text；multimodal 512×A100-80G/28 days、5T text+2.3M speech hours+1.1T image-text。
- **Baselines / Ablations / Sensitivity / Overhead:** report比较cross-attention/full-finetune与adapter approaches并含多benchmark，但缺matched deployment latency、
  adapter routing/cache overhead、simultaneous-modality ablation、data mix/LoRA rank sensitivity、seed/error与independent reproduction。OpenASR Mar4 result是later observation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** parameters、A100 count/time、data scale、128K、BF16 weights与language coverage披露；
  training precision/topology、batch、sequence mix、edge hardware latency/energy、concurrency、adapter working set、TTFT/TPOT/SLO未完整披露。
- **What the Evidence Actually Proves:** Microsoft公开了shared frozen decoder + modality-specific LoRA/router的single-checkpoint实现，并在作者evaluations中保持text能力同时支持joint modalities；
  它证明adapter不仅是fine-tuning compression，也可成为runtime-selectable capability state。
- **What It Does Not Prove:** one unified model普遍优于specialist pipeline、LoRA完全消除interference、128K在all modalities有效、edge部署自动低latency、
  benchmark headline可跨harness比较，或adapter switching/cache reuse天然安全。Speech QA与multilingual仍有已披露差距。
- **Limitations / Threats to Validity:** vendor/internal benchmarks、custom code/trust boundary、no full logs/training code、later report；
  model size限制facts/multilingual，audio safety data仅voice且没有audio-specific jailbreak，vision/audio languages不对称，model cards要求application mitigations。
- **Trade-offs / New Failure Modes:** frozen base保护language/降低retraining，却限制deep cross-modal adaptation；multiple LoRA省weights却增加router、adapter cache、composition和KV identity；
  shared decoder降低deployment footprint却扩大common-mode failure；trust_remote_code与modality parsers增加supply-chain/input attack surface。
- **Where the Previous Design Still Applies:** specialist ASR/VLM用于deterministic/独立upgrade；full fine-tune用于单modalityquality-first；cross-attention用于严格base isolation；
  separate services用于security/failure domain；small mini用于text edge，multimodal用于joint evidence；cloud large model用于quality ceiling。
- **Evolution Relationship:** `Alternative Branch`：specialist pipeline → full unified multimodal fine-tune ↔ frozen backbone + cross-attention/adapters →
  mixture-of-LoRAs + modality router。它以runtime state/adapter complexity换取base reuse与capability preservation，不是单向替代。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Current Ch23；Legacy N/A）主 owner；handoff到`MODEL-DECODER-ONLY`、
  `MODEL-LONG-CONTEXT`、`TRAIN-LORA`、`INFER-VLLM`、`PLATFORM-MODEL-REGISTRY`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch18 decoder、Ch22 long context、Ch23 modality boundary、Ch30 LoRA、Ch50 vLLM、Ch59 registry与Ch72 security；
  family拥有adapter capability composition，不拥有tool workflow、deployment policy或multimodal truth verification。
- **Existing Coverage:** Books已有encoder/projector/fusion与LoRA serving，但缺少frozen shared backbone→modality delta→router→adapter/cache identity的完整链及specialist coexistence；
  可refine representation与LoRA handoff，不建立Phi产品章节。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Later Report Evidence`。Historical Books Gate保持关闭。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly与年度账本；Feb launch与Mar report/leaderboard分离，未修改Books。
- **Open Questions:** adapter composition/interference、router correctness、KV/prefix identity、rank/working-set memory、edge latency/energy、multimodal context accounting、
  custom-code sandbox、audio jailbreak、language parity、matched specialist pipeline、independent reproduction与future modality add/remove lifecycle。

### Command R7B Arabic Release: Regional Capability Is a Data/Evaluation Control Loop, Not Literal Translation

- **Candidate / Week / Score:** Command R7B Arabic open-weights release / 2025-W09 / 26/30。
- **Source Family ID:** `cohere-command-r7b-arabic-multilingual-arbitrage-iterative-posttraining`。
- **Source Type:** 2025-02-27 official launch/changelog + open-weight gated model card/config + 2025-03-18 same-family technical report。
- **Event Date / First-public Date / Revision History:** open weights/Blog 2025-02-27；report v1 2025-03-18。
  Base Command R7B 12-2024 is parent family；later Command A/quantizations/deployments are revisions or separate products，不回填W09。
- **Direct Primary Sources:** https://cohere.com/blog/command-r7b-arabic；https://docs.cohere.com/changelog/command-r7b-arabic；
  https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025。
- **Related Primary Sources:** https://arxiv.org/html/2503.14603v1；base `CohereLabs/c4ai-command-r7b-12-2024` card；
  IFEval/AlGhafa/TyDiQA/FaithEval artifacts用于evaluation semantics，later report不能伪装成launch-day disclosure。
- **Access and Verification Status:** launch/docs、gated but readable model card/config/weights metadata、292-line report method/evaluation/limitations可访问；
  training datasets/weights、reward/judge versions、expert checkpoints/merge manifests与full logs未公开，作者结果未独立复现。
- **Full-read Coverage:** base selection、Arabic/English architecture/prompt/RAG modes、multilingual arbitrage/human annotation、iterative SFT data inclusion loop、
  two-stage DPO、expert linear merge、Arabic/general benchmarks、MSA/enterprise limitations、license/deployment surface与report appendix lineage。
- **Original Problem:** Arabic enterprise data稀缺，literal translation忽略morphology、syntax与cultural/task semantics；直接继续预训练成本高，
  只优化Arabic可能破坏base English/general capability。Regional model同时需要instruction control、RAG faithfulness、language purity与compact deployment。
- **Why the Previous Design Was Reasonable:** general multilingual base摊销pretraining cost；literal translation快速扩数据；single SFT mix简单可复现；large global model覆盖更多facts/dialects。
  数据充足、regional nuance不关键或可依赖RAG时，general model仍是更低lifecycle成本的选择。
- **Changed Constraint:** MSA instruction如diacritics/grammar/length control不能自然由English模板翻译；enterprise需要Arabic citations与少code-switch；
  团队要在7B规模快速迭代并保持English/core benchmark，因此需要targeted data/eval feedback loop而非重训base。
- **Mechanism:** 从Command R7B base出发，由Arabic experts翻译/扩展IFEval并加入Arabic-specific constraints；以seed生成synthetic prompts/completions，
  reward model+Arabic LLM judge panel过滤/构造preference pairs。每个candidate dataset单独加入base mix→SFT→benchmark gate→保留或multilingual-arbitrage refine；再两阶段DPO并线性merge capability experts。
- **State Ownership:** base checkpoint拥有general capability；dataset candidate/manifest拥有language/domain/provenance；human annotators拥有linguistic corrections；
  reward/judge ensemble拥有filter/pair policy；benchmark gate拥有retain/reject decision；expert checkpoints/merge weights拥有capability composition；chat/RAG template拥有mode/citation surface。
- **Control Flow / Data Flow:** general base → Arabic seed/human adaptation → synthetic generation → reward/judge filter → candidate mix SFT → Arabic+general eval gate →
  accepted data next iteration → offline DPO → iterative Arabic preference DPO → equal-weight expert merge → conversational/instruct/RAG runtime。
- **Implementation Details:** ~8B total（7B transformer+1B embeddings）、128K context、sliding-window pattern 3 local layers(window4096)+1 global no-position layer；
  Arabic/English、MSA focus、CC-BY-NC gated weights。RAG template接受100–400-word snippets并生成inline citations；system preamble optional。
- **Evaluation Contract:** Arabic suite AlGhafa-Native、ArabicMMLU、IFEval AR 541 samples、TyDiQA Arabic、professionally translated FaithEval；
  general Open LLM Leaderboard/BBH/MuSR/GPQA/MMLU-Pro/IFEval/MATH，plus Arabic Arena-hard preference。Report compares same-size bases but no real deployment study。
- **Baselines / Ablations / Sensitivity / Overhead:** report describes dataset inclusion loop/merge weighting search but lacks per-stage full ablation、data counts/tokens、compute、judge agreement、
  DPO hyperparameters、merge variance与multi-seed。Arabic gains small on some knowledge/RAG metrics and general MATH drops vs base，showing specialization trade-off。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model size/BF16/128K/SWA window disclosed；training GPU/topology/time/tokens/precision、
  inference memory/latency、batch/concurrency、Arabic token efficiency、cost/energy与SLO均`Not Disclosed`。
- **What the Evidence Actually Proves:** Cohere公开了一个regional post-training pipeline，将human linguistic adaptation、synthetic filtering、dataset-level eval gate、DPO与expert merge串成控制循环；
  在作者benchmarks中Arabic instruction/RAG改善且general average接近base。
- **What It Does Not Prove:** MSA代表所有Arabic dialect/cultures、inline citations保证faithfulness、translated benchmarks等于enterprise performance、equal-weight merge普遍最优、
  regional model整体优于larger general models，或128K在Arabic/RAG下被验证。Report明确real-world deployment尚未证明。
- **Limitations / Threats to Validity:** later author report、no training artifacts/logs、MSA-only、translated/proxy benchmarks、reward/judge bias、non-commercial license；
  English→Arabic transfer仍困难，dialects与real workflows未覆盖，model merging理论/replication不足且增加error source。
- **Trade-offs / New Failure Modes:** specialization提高language fit却消耗general capacity/可能code-switch或dialect bias；synthetic data扩规模却复制teacher errors；
  eval-gated mixing可控但对suite overfit；expert merge省compute却弱化lineage/reproducibility；RAG template给citations却可能引用不支持claim的snippet。
- **Where the Previous Design Still Applies:** general multilingual model用于wide-language/general knowledge；continued pretraining用于deep language acquisition；
  RAG用于fresh/local knowledge；fine-tune/LoRA用于tenant domain；human translation用于small high-value sets；separate dialect models用于spoken regional use。
- **Evolution Relationship:** `Alternative Branch`：multilingual pretraining/vocabulary expansion → literal translated post-training →
  human-in-loop multilingual arbitrage + iterative dataset gates → preference tuning + expert merge。它是低compute regional adaptation branch，不覆盖full pretraining路线。
- **ROADMAP Node:** `TRAIN-DATA`（Current Ch27；Legacy Ch23）主 owner；handoff到`TRAIN-SFT`、`TRAIN-DPO`、
  `PLATFORM-EVALUATION-SYSTEM`、`AGENT-RAG`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch27 data control、Ch29 SFT、Ch34 DPO、Ch66 evaluation、Ch72 security与Ch76 RAG；
  family拥有regional data/post-training policy，不拥有retrieval correctness、enterprise deployment truth或dialect coverage。
- **Existing Coverage:** Books已有multilingual data与SFT/DPO，但缺少“dataset candidate→SFT→eval gate→refine/retain”、human cultural constraint与expert-merge lineage；
  可refinedata-system loop，不新增regional model catalog。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Regional Post-training Branch`。Historical Books Gate保持关闭。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly与年度账本；Feb release与Mar report分离，未修改Books。
- **Open Questions:** data/token manifests、annotator/judge agreement、reward versions、DPO configs、merge checkpoint lineage、dialects/code-switch、
  Arabic tokenization/latency、RAG citation faithfulness、enterprise A/B、license/deployment与independent reproduction。

### Make LoRA Great Again / GOAT: Adapter Initialization and Scaling Are Part of the Optimization Contract

- **Candidate / Week / Score:** Make LoRA Great Again / GOAT / 2025-W09 / 27/30。
- **Source Family ID:** `goat-svd-structured-lora-moe-optimization-alignment`。
- **Source Type:** arXiv v1 + official ICML 2025 implementation；v2/v3/v4属于same family revisions。
- **Event Date / First-public Date / Revision History:** v1 2025-02-24；v2 2025-02-26；v3 2025-05-20；v4 2026-03-03。
  W09机制与实验锁定v1，后续ICML/code status只作lineage。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.16894；https://arxiv.org/html/2502.16894v1；
  https://github.com/Facico/GOAT-PEFT；https://openreview.net/forum?id=SUxq4HeIAd。
- **Related Primary Sources:** LoRA/DoRA/PiSSA/MiLoRA与MoLoRA/AdaMoLE/HydraLoRA原论文用于baseline semantics；repo说明代码参考LoRAPro。
- **Access and Verification Status:** v1全文、theorems/proofs、25-task experiments、ablations、rank/expert/routing/parameter/FLOP appendices与
  current official code/scripts已核验；event-time immutable tag和hardware contract未公开。
- **Full-read Coverage:** LoRA update equivalence、SVD priors、LoRA-MoE routing、weight/gradient alignment、residual correction、four-domain
  setup、Full FT/single/MoE baselines、initialization/scaling ablation、rank/expert ratio、routing loads、convergence、hyperparameters与artifact。
- **Original Problem:** 标准LoRA从零/随机低秩因子出发，无法显式利用pretrained singular directions；静态principal/minor SVD只选一段先验。
  把多个LoRA experts交给router又会让每个non-zero prior在初始化时共同改变base output，且LoRA与full-rank MoE的梯度尺度不同。
- **Why the Previous Design Was Reasonable:** zero-delta initialization精确继承base，单LoRA artifact最小、merge/serve简单；Full FT容量最高；
  task单一、adapter rank足够或router/serving复杂度不值得时，旧方案仍更稳。
- **Changed Constraint:** 希望用多个低秩experts覆盖不同pretrained SVD regions，同时维持upcycled Full-FT MoE的初始函数与近似更新轨迹；
  router、expert priors、scaling与residual不能再独立选择。
- **Mechanism:** 将每个weight的SVD spectrum按间隔切成E个distinct rank-r chunks初始化A/B experts；top-k router按input选择experts。
  对所有prior产生的weighted low-rank sum减去`W_res`，使initial equivalent weight回到`W0`；再用理论scaling/residual correction
  近似对齐每expert的LoRA gradient与upcycled full-rank MoE update。
- **State Ownership:** frozen base拥有原weight；SVD manifest拥有factor/chunk identity；router拥有token→adapter selection；每个LoRA expert
  拥有low-rank delta；`W_res`拥有initial-function correction；training recipe拥有scaling。任何一个缺失都会改变artifact semantics。
- **Control Flow / Data Flow:** base weight → SVD/chunk allocation → initialize E adapters + residual → router top-k → weighted low-rank forward →
  task loss → scaled adapter/router gradients → adapter bundle；deployment再决定merge或dynamic routing，不能只加载单一矩阵对。
- **Implementation Details:** 主要LLaMA2-7B/ViT-B32/RoBERTa-large experiments；常见2-of-8 experts，rank按domain8或32；AdamW、
  task-specific batch/LR/epochs，NLG batch32/rank8/alpha16/LR2e-5/5 epochs。Repo提供CV/NLG/NLU/commonsense scripts与FlashAttention2.7.3。
- **Evaluation Contract:** 25 datasets、four domains：7 image classification、Wizard/MetaMath/Code NLG→MTBench/GSM8K/HumanEval、
  Commonsense170K→8 QA sets、7 GLUE tasks。Full-FT MoE因8×memory仅在IC/NLU比较；chat由GPT-4评估，跨domain metrics不可直接平均成生产结论。
- **Baselines / Ablations / Sensitivity / Overhead:** Full FT/Full FT MoE、8 single-LoRA与3 LoRA-MoE baselines；SVD chunk type、MoE/scaling、
  rank8→128、expert count/active ratio、routing load、convergence、parameter/FLOPs。缺matched wall-clock/HBM/communication、seeds/CI、
  base/model scale diversity、adapter serving与router failure studies。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/rank/experts/batch/LR/epochs披露；GPU topology、precision、
  sequence lengths、wall time、router dispatch kernel、training/serving concurrency、latency与SLO为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者任务/模型中，non-zero pretrained priors必须同时修正initial function与update scaling；
  SVD chunks+router比单一静态SVD segment提供更大适配分支，2-of-8在该storage/performance实验中是较平衡point。
- **What It Does Not Prove:** LoRA可普遍等价Full FT、SVD singular regions对应稳定语义experts、theorem assumptions在nonlinear network/
  arbitrary optimizer/finite precision严格成立、GOAT端到端比Full FT更快，或dynamic serving无需额外state/communication。
- **Limitations / Threats to Validity:** proofs依赖近似weight/gradient与identical-router assumptions；authors tune各task，缺seed uncertainty；
  Full FT MoE comparison不完整、GPT-4 judge、LLaMA2-era base、no hardware/runtime、current repo only7 commits/no release tag。
- **Trade-offs / New Failure Modes:** richer priors/experts提高capacity却增加SVD build、router training、adapter storage、load imbalance、merge困难与
  per-request identity；residual保持initial output却成为checkpoint必需state；高rank减gap但收益递减。单LoRA仍最易治理。
- **Where the Previous Design Still Applies:** zero-init LoRA用于可逆小artifact；PiSSA/MiLoRA用于单subspace prior；Full FT用于capacity优先；
  static multi-adapter routing用于tenant明确；dense single adapter用于small-QPS或kernel/serving简洁性优先。
- **Evolution Relationship:** `Direct Evolution`：zero-delta LoRA → static SVD prior → multiple SVD adapter experts → router-conditioned update →
  function/gradient-aligned adapter bundle；每步增加expressivity，也增加artifact state。
- **ROADMAP Node:** `TRAIN-LORA`（Current Ch30；Legacy Ch26）主 owner；handoff到 `MODEL-MOE`、`TRAIN-SFT`、
  `TRAIN-CHECKPOINT`、`INFER-VLLM`与`PLATFORM-MODEL-REGISTRY`。
- **Target and Adjacent Chapters Read:** 已读Ch30 low-rank/SVD/init/merge/dynamic adapter，核对Ch21 router/experts、Ch29 objective、
  Ch35 artifact与Ch50 LoRA cache；MoE adapter不是base-model sparse MoE的同义词。
- **Existing Coverage:** Ch30已明确LoRA不是post-hoc SVD并要求base/adapter/runtime lineage，但缺“non-zero prior必须同时对齐initial
  function与gradient scale；router+residual也属于adapter identity”，可refine既有论证。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。不保留25-task leaderboard headline。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；v1/revision与training/runtime边界已分开，未修改Books。
- **Open Questions:** event-time commit、proof sensitivity、seeds/uncertainty、modern bases、matched HBM/FLOPs/walltime、router collapse/
  capacity、merge semantics、multi-tenant adapter cache、quantized base与independent reproduction。

### Stable-SPAM v1: Low-precision Instability Can Persist in Optimizer History after the Spike Has Passed

- **Candidate / Week / Score:** Stable-SPAM (v1 title) / 2025-W09 / 27/30。
- **Source Family ID:** `stable-spam-gradient-norm-history-low-precision-training`。
- **Source Type:** arXiv v1 + pre-release official optimizer/code；later family was renamed GradientStabilizer and accepted ICML 2026。
- **Event Date / First-public Date / Revision History:** v1 2025-02-24；v2 2025-04-11；v3 2026-02-27；v4 2026-05-26；
  v5 2026-08-03。W09 locks Stable-SPAM v1；later title/mechanism revisions are not silently substituted。
- **Direct Primary Sources:** https://arxiv.org/html/2502.17055v1；https://arxiv.org/abs/2502.17055；
  https://github.com/TianjinYellow/StableSPAM。
- **Related Primary Sources:** SPAM (arXiv:2501.06842) owns spike-aware clipping/momentum-reset predecessor；GaLore repo is code base lineage。
- **Access and Verification Status:** v1全文、pseudocode、C4 low-bit/BF16 experiments、LR/component/hyperparameter ablations、appendix与
  official pre-release repo已核验；repo仍列LLM/4-bit pretraining code TODO且无event-time release tag，artifact为partial。
- **Full-read Coverage:** Adam/Adafactor/Adam-mini/SPAM stability sweep、INT/FP4 gradient observations、AdaGN/AdaClip/MoRet mechanism、
  60M–1B experiments、INT2/3/4、BF16/integration with other optimizers、LR/component/hyperparameter ablations、architecture/config、pseudocode。
- **Original Problem:** 低比特weight/activation会放大element-wise gradient spikes和whole-matrix norm波动；一次spike进入Adam一二阶moments后，
  即使当前gradient恢复，历史状态仍可能长期缩放后续updates。SPAM clipping+periodic reset有效，但LR敏感且norm仍不稳。
- **Why the Previous Design Was Reasonable:** global norm clipping简单、无额外optimizer-state schema；Adam moments平滑noise；BF16避免大部分
  quantization error。精度充足、spike稀少、成熟recipe或恢复兼容优先时旧路径仍合理。
- **Changed Constraint:** FP4/INT4训练在更高LR下频繁出现不同层/矩阵的局部spikes与global norm surge；固定threshold不能随phase适应，
  只clip单步也无法清除已污染moments。
- **Mechanism:** AdaClip用historical max-gradient EMA形成bias-corrected threshold，只缩放超过threshold的elements；AdaGN为每个gradient
  matrix维护norm的一二阶EMA，把当前matrix归一后按historical adaptive norm重缩放；MoRet每`Delta T`清空Adam moments，截断spike history。
- **State Ownership:** parameter gradient拥有当前signal；AdaClip threshold EMA拥有element-spike history；AdaGN norm EMAs拥有matrix-scale history；
  Adam moments拥有coordinate history；reset schedule拥有epoch/step phase。它们都必须进入checkpoint/resume identity。
- **Control Flow / Data Flow:** quantized forward/backward → raw gradient/max/norm → adaptive element clipping → matrix norm normalization →
  Adam update → periodic moment reset → parameter update；monitor同时保存raw/clipped norm、threshold、reset与loss。
- **Implementation Details:** LLaMA 60M/130M/350M/1B on C4，seq256/global batch512≈131K tokens/step，warmup2K+cosine-to10%；
  tokens1.1B/2.2B/6.4B/11.6B；low-bit LR按size1e-3/4e-4/2e-4，`Delta T=1000`、gamma1=.7、gamma2=.9、gamma3=.999。
- **Evaluation Contract:** validation perplexity/loss、gradient-norm/loss curves；FP4/INT4 LLaMA、350M INT2/3/4、BF16 60M–1B；
  LR sweep约1e-4→5e-3，另在60M/130M把AdaGN/AdaClip接入Lion/Adam-mini。无end-to-end hardware throughput。
- **Baselines / Ablations / Sensitivity / Overhead:** Adam、Adafactor、Adam-mini、SPAM、Lion；MoRet/AdaGN/AdaClip逐项、替换SpikeClip/
  GradClip、four gammas/reset interval与LR sweep。缺optimizer-state memory/communication、resume tests、large-model/token-scale、data anomaly
  attribution、true hardware low-bit vs simulation、multiple seeds/CI。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** models/FP4/INT4/BF16/length/batch/tokens/LR披露；GPU type/count、
  actual low-bit kernel, accumulation/DP degree、walltime、HBM、collective overhead、failure/recovery SLO为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者small LLaMA+C4 contract中，低比特扩大LR sensitivity并使gradient history成为failure state；
  norm EMA、adaptive element threshold与periodic moment reset共同改变stability，组件作用在FP4/BF16不同，不能缩成单一clip技巧。
- **What It Does Not Prove:** optimizer普遍优于Adam、4-bit质量超过BF16的headline可外推到大模型、gradient spike都是数值而非data/loss问题、
  periodic reset永远安全、later GradientStabilizer等同v1，或减少steps等于减少wall-clock/energy。
- **Limitations / Threats to Validity:** 60M–1B/seq256、C4-only、best-LR selection、missing seeds/hardware、pre-release repo/TODO、optimizer多
  hyperparameters、no distributed/checkpoint recovery、quantization graph披露不足、later title/mechanism drift。
- **Trade-offs / New Failure Modes:** additional norm/threshold EMAs提高phase adaptation却增加state、reductions和checkpoint compatibility；
  reset清除污染也丢失有用curvature history；aggressive normalization/clipping会抹平real signal。BF16/Adam在风险/简洁优先时仍成立。
- **Where the Previous Design Still Applies:** global clipping用于rare outlier；SPAM用于element spikes但norm较稳；Adam/BF16用于成熟大规模；
  data filtering/loss scaling解决source anomaly；optimizer change必须在same token/hardware contract下比较。
- **Evolution Relationship:** `Direct Evolution`：Adam historical moments → global/element spike clipping → periodic history reset →
  adaptive element threshold + matrix-norm history；后者没有否定前者，而是把failure state显式化。
- **ROADMAP Node:** `TRAIN-PRETRAINING`（Current Ch28；Legacy Ch24）主 owner；handoff到 `TRAIN-DISTRIBUTED-TRAINING`、
  `TRAIN-CHECKPOINT`、`TRAIN-DEEPSPEED`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch28 LR/clipping/per-layer update与low-bit graph，核对Ch36 reduction、Ch35 optimizer checkpoint、
  Ch41 precision/overflow和Ch66 evidence contract；optimizer不拥有data correctness。
- **Existing Coverage:** Ch28已有global clipping和dynamic controller state，但缺“spike→moment contamination→adaptive threshold/norm→reset”的
  完整演进，以及这些EMA/reset需checkpoint/collective一致性的系统含义，可refine既有论证。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。v1与2026 renamed family必须分别审计后再吸收。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；保留artifact partial与revision drift，未修改Books。
- **Open Questions:** v1 immutable commit/full code、later revision mechanism diff、real low-bit hardware、large model/long context、seeds、
  state/collective overhead、resume/reshard、data spikes、reset schedule与independent reproduction。

### VideoGrain: Editing Control Is Attention Routing over Versioned Regions

- **Candidate / Week / Score:** VideoGrain / 2025-W09 / 26/30。
- **Source Family ID:** `videograin-region-conditioned-spacetime-attention-editing`。
- **Source Type:** arXiv v1 / ICLR 2025 paper + official inference repository/project/data lineage。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-24；arXiv仅一个版本。后续dataset/repo更新不重复计分。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.17258；https://arxiv.org/html/2502.17258v1；
  https://github.com/knightyxp/VideoGrain；https://knightyxp.github.io/VideoGrain_project_page/。
- **Related Primary Sources:** SD1.5、DDIM inversion、SAM-Track、ControlNet/FLATTEN/PnP及baseline repos构成依赖，不由VideoGrain替代。
- **Access and Verification Status:** v1全文、method/equations、76-video evaluation、human/automatic metrics、ablation、limitations与official
  code已核验；dataset在2025-03-15更新，event-time完整artifact与immutable tag未证实。
- **Full-read Coverage:** failure visualization、class/instance/part formulation、DDIM inversion、semantic clustering/SAM-Track masks、
  cross/self ST-Layout attention equations、SD1.5/A40 setup、baselines/metrics/human eval、prompt/mask/attention ablations与limitations。
- **Original Problem:** global text-to-video edit能改“人”这一class，却无法把同类的左/右实例分别绑定不同prompt；cross-attention会在
  regions间泄漏，self-attention又把same-class features跨实例/frames混合，导致局部edit污染和结构失真。
- **Why the Previous Design Was Reasonable:** single global prompt与class-level attention无需region masks，适合全局style/object replacement；
  finetuned editors可学习复杂shape change。没有instance distinction或标注成本高时，旧方案更简单。
- **Changed Constraint:** one-prompt需要同时承载多个region-specific edits，且保持16–32 frames的instance identity和temporal coherence；
  training-free路径必须在frozen prior上修改routing，而不是重训模型。
- **Mechanism:** 对source latent做50-step DDIM inversion；用inversion self-attention KMeans得到semantic layout，再由SAM-Track分离实例。
  denoising前15步中，cross-attention把`local prompt↔target mask`作为positive并抑制outside scores；self-attention增强same-region跨frame
  pairs、屏蔽different-instance pairs。global prompt、local prompt和mask共同定义edit contract。
- **State Ownership:** source video/inverted latent拥有content state；SAM-Track/masks拥有provisional region identity；local prompts拥有edit
  intent；cross-attention路由text→region；self-attention路由region→region temporal features；frozen SD prior拥有generation boundary。
- **Control Flow / Data Flow:** source frames → DDIM inversion → attention clustering + tracked instance masks → global/local prompts →
  early-step ST-Layout cross/self modulation → denoise + temporal plug-ins/ControlNet → edited clip → automatic/human evaluation。
- **Implementation Details:** SD1.5、50 inversion+50 denoise steps，ST modulation first15；self coefficient`0.3*t^5`、cross`t^5`；
  sliced attention节省memory；single NVIDIA A40；76 pairs from DAVIS/TGVE/Internet，16–32 frames。
- **Evaluation Contract:** class/instance/part edits；CLIP-T prompt alignment、CLIP-F frame similarity、RAFT Warp-Err、Q-edit以及human Edit-Acc/
  Temp-Con/Overall；FateZero/ControlVideo/TokenFlow/Ground-A-Video/DMT，T2I baselines统一ControlNet conditions。
- **Baselines / Ablations / Sensitivity / Overhead:** baseline→+cross→+self modulation、prompt count、mask granularity、modulation timestep/
  coefficient；缺mask-quality oracle、SAM-Track failure slice、same compute/latency/memory、multiple seeds、base-model variants与adversarial edits。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** SD1.5/A40/steps/frames披露；resolution、precision、batch、GPU memory、
  runtime、concurrency、streaming/final latency和production SLO为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在该small editing suite中，local prompt要成为可执行control，需要同时约束cross-attention
  text-region binding与self-attention region separation；只改cross path仍会因same-class feature coupling产生结构污染。
- **What It Does Not Prove:** attention maps等于causal object identity、SAM masks总正确、training-free适合large deformation、headline metrics
  可外推到modern T2V、modulation不会破坏unmasked regions，或region routing已解决provenance/safety。
- **Limitations / Threats to Validity:** 76 clips、SD1.5/T2I prior、mask/tracker dependency、16–32 frames、base prior限制、large shape/
  appearance change失败、human protocol规模未充分披露、metrics偏好相关性/flow proxy、artifact晚于event。
- **Trade-offs / New Failure Modes:** explicit masks提升local control却增加segmentation/tracking error和region drift；attention suppression减少leakage
  也可能切断合法cross-region context；frozen prior省训练却锁定base bias/shape limits；finetuning在domain稳定且大变形需求下仍更合适。
- **Where the Previous Design Still Applies:** global edit用于uniform changes；trained video editor用于motion/shape prior；ControlNet用于global
  structure；manual masks用于高价值精确任务；full self-attention在regions相互依赖且mask不可信时保留信息。
- **Evolution Relationship:** `Direct Evolution`：global prompt edit → spatial region prompt → cross-attention binding → cross-frame self-attention
  separation；每一步解决更细control，也新增region identity/state。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Current Ch24；new node）主 owner；handoff到
  `MULTIMODAL-REPRESENTATION`、`MODEL-SELF-ATTENTION`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch23 coordinate/representation identity、Ch24 diffusion state/commit、Ch17 attention semantics与
  Ch66 multimodal evaluation；region mask是control state，不是生成真值。
- **Existing Coverage:** Ch24已有diffusion trajectory与mutable state，却未明确“editing granularity提升时，cross-attention绑定与self-attention
  isolation分别承担intent routing与feature separation”，可refine既有生成控制链。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。不保留单suite SOTA数字。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；event-time artifact与base-model限制已保留，未修改Books。
- **Open Questions:** event-time code/data commit、tracker/mask oracle、modern T2V backbones、long clips/occlusion、memory/runtime、region overlap/
  interaction、unmasked preservation、human agreement、安全编辑与independent reproduction。

### DICEPTION v1: A Shared Output Representation Can Reuse a Generative Prior without Proving Shared Task Synergy

- **Candidate / Week / Score:** DICEPTION (v1) / 2025-W09 / 26/30。
- **Source Family ID:** `diception-rgb-output-perception-diffusion-generalist`。
- **Source Type:** arXiv v1；later NeurIPS 2025 paper/model/inference code belong same family but were released in September/October。
- **Event Date / First-public Date / Revision History:** v1 2025-02-24；v2 2025-02-25；v3 2025-10-09。W09锁定v1 author set、
  architecture/evaluation/artifact state，不把v3 few-step/CFG additions倒写。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.17157；https://arxiv.org/html/2502.17157v1；
  https://aim-uofa.github.io/Diception/。
- **Related Primary Sources:** https://github.com/aim-uofa/Diception 与 https://huggingface.co/Canyu/DICEPTION 仅证明2025-09后的
  inference/model artifact；training code仍TODO，不能作为W09 executable evidence。
- **Access and Verification Status:** v1全文、data/training/inference、six-task comparisons、single-vs-multi、architecture/prompt/postprocess
  ablations、appendices/limitations已核验；event-time code/model未发布，`Paper Verified / Artifact Later`。
- **Full-read Coverage:** flow-matching/SD3 prior、RGB task encoding、random-color masks/KMeans、image+point conditioning、LoRA few-shot transfer、
  1.8M data construction、4×H800 training、task metrics/specialist baselines、single-task control、UNet/DiT and step ablations、postprocess failures。
- **Original Problem:** depth、normal、pose和多种segmentation通常使用不同heads/output spaces与specialist models；from-scratch generalist需要
  大量pixel labels。预训练T2I diffusion拥有视觉prior，但其native output是RGB image而不是typed perception tensors。
- **Why the Previous Design Was Reasonable:** specialist heads直接输出metric depth/class/mask，postprocess清晰、inference快，适合高精度/
  real-time；multi-head encoder共享features又保留task semantics。数据和deployment稳定时旧路径更可控。
- **Changed Constraint:** 资源只有约1.8M pseudo/real labels，希望最大复用SD3 pretrained prior并用一个architecture/task-prompt处理多个输出；
  new task还要求50-shot/LoRA适配，而不是重建head。
- **Mechanism:** 将depth/normal/single-channel maps复制成RGB，segmentation mask以随机colors编码instances/classes，pose也映射为image-like target；
  SD3/flow-matching接收input-image latent、task text token及最多5 point embeddings，denoise到RGB-like output，再由KMeans/typed postprocess恢复mask/
  coordinates。New tasks只训练<1% LoRA parameters。
- **State Ownership:** raw task label拥有ground truth semantics；`Psi`/color codec拥有typed→RGB mapping；SD3 latent/denoiser拥有generated image；
  task prompt拥有route；postprocessor/KMeans拥有RGB→typed reconstruction；metric evaluator拥有task-specific correctness。RGB不是统一truth type。
- **Control Flow / Data Flow:** image + optional points + task token → VAE/point encoder → noisy target RGB latent → shared flow denoiser →
  decoded RGB-like artifact → task-specific clustering/coordinate/depth postprocess → specialist metric；few-shot branch加载task LoRA。
- **Implementation Details:** 500K OpenImages pseudo depth/norm、400K SA-1B point masks、200K hair masks、EntityV2/COCO/pose，约1.8M total；
  SD3 architecture，4×H800、24 days、AdamW LR2e-5 constant、batch28/GPU；segmentation mixture被提高以补慢收敛。
- **Evaluation Contract:** depth/normal datasets与metrics、COCO entity/semantic/pose、23 point-seg validation sets；specialist baselines、SAM comparison、
  matched-data single-task models。v1 average inference0.8s/H800、2s/4090；postprocessing-heavy segmentation evaluation有限。
- **Baselines / Ablations / Sensitivity / Overhead:** multi-task vs matched single-task、1 vs5 points、SD3 DiT vs SDXL UNet、denoise steps、
  RGB mask/postprocess category failures、50-shot LoRA；缺true-label vs pseudo-label source ablation、compute-matched multi-head encoder、seeds/CI、
  task-mixture sensitivity、calibration and deployment pipeline cost。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** SD3/4×H800/24d/batch28及single-GPU latency披露；precision、resolution
  mix、optimizer states、gradient accumulation、peak HBM、multi-request batch/concurrency和SLO不完整。
- **What the Evidence Actually Proves:** 在v1 contract中，output representation与pretrained generative prior对齐可以减少new architecture/
  data requirement；task-specific prompt/codec/postprocess共同构成generalist interface。Matched single-task与multi-task无明显gap，也无mutual promotion。
- **What It Does Not Prove:** diffusion是perception的通用最优范式、RGB preserves metric precision、tasks互相学习、600K/1B data ratio可直接比较、
  50-shot works generally、one-step safe，或later code/model在W09可用。
- **Limitations / Threats to Validity:** pseudo labels继承teacher bias；RGB/KMeans丢small/dense regions（person/bird/book AP低）；pose/semantic结果
  落后specialists；24-day cost与slow inference；multi-task trajectories overlap/failure；no event artifact、no training code、later revision changes。
- **Trade-offs / New Failure Modes:** shared RGB interface复用prior并简化architecture，却把typed precision转成color/postprocess error；shared denoising
  降模型数量却增加latency/task interference；specialist heads保持metric semantics和低latency，仍适合production perception。
- **Where the Previous Design Still Applies:** direct discriminative head用于real-time/metric outputs；shared encoder+typed heads用于multi-task；
  generative RGB path用于label-scarce transfer/visualizable output；LoRA用于小data adaptation但需独立task validation。
- **Evolution Relationship:** `Alternative Branch`：shared encoder + typed heads ↔ shared generative RGB output + typed postprocess；后者把表示统一
  前移到output codec，不是对specialist perception的单向替代。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Current Ch23；new node）主 owner；handoff到
  `MULTIMODAL-GENERATIVE-PARADIGMS`、`TRAIN-DATA`、`TRAIN-LORA`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch23 continuous/discrete/mixed representation与identity，Ch24 diffusion semantics，核对Ch27
  pseudo-data provenance、Ch30 LoRA和Ch66 typed metric；output shape统一不等于semantic/output contract统一。
- **Existing Coverage:** Ch23已强调tensor compatibility≠semantic compatibility，但缺“把typed task outputs编码到pretrained RGB manifold，
  再由postprocessor恢复”的反向representation branch及其precision/latency代价，可refine该论证。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。v3新增结论需在其真实revision week另审。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；v1/later artifact与task-specific failures已分开，未修改Books。
- **Open Questions:** v1 artifact、training code、pseudo-label source bias、typed precision/calibration、task-mixture/negative transfer、DiT-vs-UNet
  compute match、few-step later revision、real-time serving、resolution/concurrency、安全与independent reproduction。

### Mobile-Agent-V v1: A Demonstration Video Is Procedural Evidence, Not an Executable Script

- **Candidate / Week / Score:** Mobile-Agent-V (v1) / 2025-W09 / 27/30。
- **Source Family ID:** `mobile-agent-v-video-procedural-evidence-aligned-execution`。
- **Source Type:** arXiv v1；later v3 title/method and May paper belong revision family；event-time code was only promised。
- **Event Date / First-public Date / Revision History:** v1 2025-02-24，v2 2025-02-25，v3 2025-06-03并改名为“A Video-Guided
  Approach for ... Knowledge Injection”。W09严格使用v1 multi-agent collaboration contract。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.17110；https://arxiv.org/html/2502.17110v1。
- **Related Primary Sources:** https://github.com/X-PLUG/MobileAgent 是Mobile-Agent family repo，但current tree未包含可核验的
  Mobile-Agent-V v1 implementation；later arXiv:2505.13887/OpenReview用于revision lineage，不替代v1。
- **Access and Verification Status:** v1全文、algorithm、benchmark、metrics、window/keyframe/reflection ablations、case/limitations已核验；
  event-time code/immutable artifact unavailable，`Paper Verified / Artifact Unverified`。
- **Full-read Coverage:** GUI/video prior work、full pipeline、sampling/filtering、sliding window、six-action schema、decision/reflection/video agents、
  max-exploration loop、OnePlus/ADB setup、three difficulty levels、four metrics、three baselines/human-knowledge branch、misalignment/window/keyframe/
  reflection analysis、case、appendix thresholds/prompts与limitations。
- **Original Problem:** mobile Agent常缺device-specific procedure；人工写SOP准确但昂贵。整段操作video含操作前后state，却被大量静态frames
  稀释；直接把全部frames交给MLLM既超Context又难将当前device state对齐到demonstration progress。
- **Why the Previous Design Was Reasonable:** handwritten procedure具有明确step order、易审计，适合稳定/高风险SOP；Agent自行探索无需
  demo，适合简单或UI频繁变化的task。短video也可full-context replay。
- **Changed Constraint:** 用户可以低成本录制video，但实际task wording/device state可能与demo不完全相同；系统需在每次action后重新定位
  demo window、验证proposal并处理missing/redundant frames，而不是盲目播放坐标序列。
- **Mechanism:** video先uniform sample，再按consecutive similarity与temporal-gap thresholds去冗余；Decision Agent读取当前W-frame window、
  video/user instruction、current screenshot与action history，提出Click/Scroll/Type/Back/Home/Done；Deep-Reflection逐操作核对demo并修正；
  execute后Video Agent用before/after screenshots定位对应keyframe并移动window，直到Done或max explorations。
- **State Ownership:** recorded video/keyframes拥有procedural evidence；window start拥有demo progress hypothesis；device screenshot/XML拥有current
  environment state；Decision只拥有action proposal；Reflection拥有advisory validation；executor/ADB拥有effect；Video Agent更新alignment，
  不拥有task completion truth。
- **Control Flow / Data Flow:** video → keyframe reduction → initial window → action proposal → demo/state reflection → execute typed action →
  observe before/after device state → align/advance window → repeat/stop。Raw video不能直接成为Workflow transition log。
- **Implementation Details:** GPT-4o default API for all agents/baselines；OnePlus7Pro+ADB；click positions来自XML hierarchy并标注到screenshots；
  window size>2用于容忍keyframe error，paper探索similarity threshold/window size；six-action schema和max exploration cap。
- **Evaluation Contract:** author-built device-specific benchmark分basic/normal/advanced instructions；Success Rate、step Completion Rate、Decision
  Accuracy、Step Count；AppAgent/Mobile-Agent v1/v2及human-curated knowledge baseline。Video-misaligned branch改变specific actions但保留logic。
- **Baselines / Ablations / Sensitivity / Overhead:** three agent frameworks、human text knowledge、aligned/misaligned video、window size、manual vs
  automatic keyframes、with/without deep reflection、case trace和video-vs-writing preparation time。缺task count/trials/variance充分说明、
  model/role ablation、call/token/latency cost、same-step deterministic verifier、安全/permission与cross-device studies。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** GPT-4o API/device/action schema披露；video duration/frame counts、tokens、
  model snapshot、sampling、API latency/cost、concurrency、ADB timing、failure timeout和SLO均不完整或 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在该single-device benchmark中，video procedure需要“压缩→局部window→proposal check→environment alignment”
  才能转成action；larger context有diminishing returns，manual keyframes略好，reflection主要改善复杂task的decision accuracy。
- **What It Does Not Prove:** video自动成为正确SOP、多Agent本身造成全部gain、reflection独立于same-model blind spot、30%/80%可外推、
  misaligned tasks代表open-world generalization、或video instruction可越过permissions/approval。
- **Limitations / Threats to Validity:** custom small benchmark、OnePlus only、GPT-4o/proprietary drift、XML grounding advantage、no code、video quality/
  missing critical frames、same-model roles、manual metrics/ground truth、no safety/side-effect recovery、later title/method drift。
- **Trade-offs / New Failure Modes:** video降低SOP authoring effort却增加PII、temporal alignment、stale UI、frame omission和storage costs；local window
  控制Context却可能错过distant prerequisite；Reflection减少misalignment却增加calls/correlated errors。Human SOP仍适合高风险稳定流程。
- **Where the Previous Design Still Applies:** curated Skill用于repeatable audited task；direct exploration用于simple UI；accessibility/API tools优于
  pixels when available；single controller+deterministic verifier优于same-model role proliferation；full video仅在短/低noise时可接受。
- **Evolution Relationship:** `Layering / Dependency`：raw demonstration → compressed temporal evidence → state-aligned procedural window →
  checked action proposal → environment-confirmed workflow transition；不是video直接替代Skill/Workflow。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Current Ch81；Legacy Ch77）主 owner；handoff到 `AGENT-CONTEXT`、`AGENT-MEMORY`、
  `AGENT-REFLECTION`、`AGENT-MULTI-AGENT`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch75 bounded context、Ch77 procedural memory/provenance、Ch80 reflection、Ch81 durable transition与
  Ch82 role decomposition；video-derived evidence不能获得executor authority或未经验证写成persistent Skill。
- **Existing Coverage:** Books已有procedural memory、Reflection independence和Workflow authoritative state，但可refine“demonstration evidence
  必须与live state持续对齐；progress window与device state由不同owner维护”的演进链。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。later May/June family revision必须另行核验。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；code absence与v1/v3 title/method drift已显式保留，未修改Books。
- **Open Questions:** event-time implementation、later revision diff、benchmark/task counts、video privacy/consent、frame/calibration robustness、
  cross-device/app drift、deterministic action/effect verifier、permissions、API cost/latency、failure recovery与independent reproduction。

### Thus Spake Long-Context LLM v1: Nominal Window Is Only One Coordinate of the Lifecycle

- **Candidate / Week / Score:** Thus Spake Long-Context Large Language Model (survey v1) / 2025-W09 / 25/30。
- **Source Family ID:** `thus-spake-long-context-lifecycle-survey`。
- **Source Type:** academic survey + author-maintained bibliography/slides；secondary evidence，不是任一 cited mechanism 的primary source。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-24；v2 2025-11-11。W09锁定v1 coverage与claims。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.17129；https://arxiv.org/html/2502.17129v1；
  https://github.com/OpenMOSS/Thus-Spake-Long-Context-LLM。
- **Related Primary Sources:** survey引用约800项paper/report/framework；本Source Review仅核验taxonomy与引用边界，任何具体机制/
  benchmark若进入Books必须重新打开对应primary source。
- **Access and Verification Status:** v1全部12 sections、equations、taxonomy figures、model/benchmark tables、10 unanswered questions、
  acknowledgement/omission statement与author bibliography已读；v2未用于W09结论。
- **Full-read Coverage:** RoPE/weak-vs-strong extrapolation、KV six dimensions、cache/text×read/write memory quadrants、attention/RWKV/SSM/hybrid、
  training parallelism/memory/MFU、inference memory/compute/distribution/frameworks、long-data/pretraining、input-output post-training taxonomy、
  long-context multimodal adaptation、benchmark tasks/features/safety和Q1–Q10。
- **Original Problem:** vendor/config宣称的context window把多个独立问题压成一个长度数字：模型是否能表示远距离位置、是否能保留/
  选择state、训练/推理是否承受compute-memory-communication、数据是否包含真实远依赖、evaluation是否测有效使用。
- **Why the Previous Design Was Reasonable:** maximum token window与perplexity便于比较architecture/config；full attention + full KV最接近原模型，
  short-context pretraining数据充足。短文、低并发、强retrieval或capacity非瓶颈时，这些旧设计仍合理。
- **Changed Constraint:** claimed windows扩展到128K–2M，long video/code/many-shot ICL进入workload；quadratic attention、linear KV、mixed-length
  imbalance、long-data scarcity、position bias与benchmark contamination同时出现，单一层优化无法说明effective context。
- **Mechanism:** 该survey不提出新model algorithm，而建立lifecycle taxonomy：先区分weak perplexity extrapolation与strong downstream
  extrapolation；把KV footprint分解为sequence×layers×KV heads×feature dimension×dtype；把memory按cache/text及read/write分四象限；
  再将architecture→training/inference infra→data/post-training→evaluation串成依赖链。
- **State Ownership:** position scheme拥有index mapping；model architecture拥有receptive/recursive state；KV/memory manager拥有stored context；
  training runtime拥有activation/parallel schedule；serving runtime拥有admission/cache/scheduling；dataset拥有dependency evidence；benchmark拥有
  conditional measurement。`max_position_embeddings`不拥有effective-context truth。
- **Control Flow / Data Flow:** raw long corpus → curation/dependency/mixture → long-context train/post-train → model+position/memory architecture →
  distributed training artifact → serving KV/memory tiers/scheduler → task-specific eval by length/depth/stability/contamination → deployment decision。
- **Implementation Details:** survey本身无implementation；它整理position interpolation/inference scaling、token drop/merge/layer/head/feature/dtype
  KV compression、memory retrieval/write、distributed attention、activation/offload, prefix reuse, PD scheduling与framework cases。
- **Evaluation Contract:** secondary comparison of long QA/summary、NIAH/multi-retrieval、code/math/aggregation、long ICL/reasoning；benchmark features
  包含length、stability、contamination、alignment/safety。其model tables混合vendor reports与不同scorers，不能作为横向leaderboard。
- **Baselines / Ablations / Sensitivity / Overhead:** N/A for survey；它对比design families但没有统一matched experiment、ablation或hardware contract。
  每个headline必须回到cited primary source核验。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** survey汇总异构contracts，无法形成单一hardware/model/precision/length/
  batch/concurrency/SLO；统一值全部 `Not Applicable`。这正是禁止跨paper数值外推的原因。
- **What the Evidence Actually Proves:** v1作者在2025-02形成覆盖architecture、infra、training、evaluation的广泛taxonomy，并明确nominal
  window、perplexity、retrieval、memory与downstream能力不可互相替代；它可作为source discovery/knowledge-tree completeness check。
- **What It Does Not Prove:** 任一listed method优于另一方法、长context必然替代RAG、Mamba/RWKV替代Transformer、0.5–5B long tokens普适、
  cache compression无质量损失、vendor context真实有效，或survey遗漏项不存在。
- **Limitations / Threats to Validity:** secondary source、fast-moving 2025 snapshot、约800异构references、authors承认可能遗漏、taxonomy overlaps、
  vendor/model table drift、some blog/code citations、no systematic-review inclusion protocol、no unified evidence grading或reproduction。
- **Trade-offs / New Failure Modes:** lifecycle view提高完整性却可能把相邻术语误当同层替代；大taxonomy便于导航却掩盖evidence quality。
  将其作为Books事实源会传播二手错误；将其只作discovery map则要求额外primary-source成本。
- **Where the Previous Design Still Applies:** short context+RAG用于fresh/sparse evidence；full attention/KV用于quality-first；window-based evaluation
  用于capacity smoke test；perplexity用于language modeling regression；每项仅在其原contract内有效。
- **Evolution Relationship:** `Layering / Dependency`：position capacity → effective attention/memory access → trainable long dependency → executable
  infrastructure → task evidence；同时存在`Alternative Branch`：long full-context与RAG/memory selection各有条件。
- **ROADMAP Node:** `MODEL-LONG-CONTEXT`（Current/Legacy Ch22）主 owner；handoff到 `INFER-KV-CACHE`、
  `TRAIN-DISTRIBUTED-TRAINING`、`INFER-PD-DISAGGREGATION`、`AGENT-RAG`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch22 nominal/effective context，核对Ch19 position、Ch45 KV、Ch36/40 distributed training、
  Ch55 PD、Ch76 RAG与Ch66 evaluation；survey taxonomy不能覆盖这些owner的primary evidence。
- **Existing Coverage:** Books当前已把position、KV、distributed runtime、data、RAG与evaluation分给独立owner，并明确nominal≠effective context；
  survey验证结构覆盖而不提供新机制，避免把所有long-context内容重新堆入Ch22。
- **Integration Decision:** `Books Pending — No Change Candidate`。年度Books pass只需引用现有章节级去重证据，不引用survey headline。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；作为secondary taxonomy保存，不修改Books，也不把v2更新倒灌。
- **Open Questions:** v2 taxonomy diff、systematic inclusion criteria、primary-source coverage gaps、long-output/long-in-long-out、effective-context
  calibration、long-context vs RAG matched contracts、on-device/multimodal、mixed-length scheduling与benchmark contamination。

### KV-Edit: Reusing Background State Is Not the Same Contract as Autoregressive KV Cache

- **Candidate / Week / Score:** KV-Edit: Training-Free Image Editing for Precise Background Preservation / 2025-W09 / 27/30。
- **Source Family ID:** `kv-edit-dit-background-state-reuse`。
- **Source Type:** arXiv v1 paper + author project page + official Apache-2.0 implementation；later ICCV acceptance与
  post-event repository changes只作lineage。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-24、v2 2025-02-25、v3 2025-03-12；
  official code于2025-02-25发布。2025-03-04新增`attention scale`不倒写为W09 v1机制。
- **Direct Primary Sources:** https://arxiv.org/html/2502.17363v1；https://arxiv.org/abs/2502.17363；
  https://github.com/Xilluill/KV-Edit；https://xilluill.github.io/projectpages/KV-Edit/。
- **Related Primary Sources:** official FLUX repository与authors声明的RF-Solver-Edit code base；PIE-Bench及六个
  evaluation baselines只用于核对实验合同，不把later ComfyUI integration当作W09 evidence。
- **Access and Verification Status:** v1 HTML、revision history、算法1/2、全部实验/ablation/user study与当前official
  code surface已核验；缺少immutable event-time tag，current repository正在restructuring。
- **Full-read Coverage:** metadata、Abstract、Introduction、Related Work、ODE/Rectified Flow preliminaries、
  inversion error analysis、attention decoupling、KV-Edit与memory-efficient variant、implementation、PIE-Bench
  comparison、ablation、user study、Conclusion及official demo/hardware paths全部阅读。
- **Original Problem:** training-free inversion→denoising会因离散化累计误差、新text condition与新foreground
  同时改变未编辑背景；“看起来相似”不能满足局部编辑对背景像素一致性的要求。
- **Why the Previous Design Was Reasonable:** 对UNet或不要求严格保真的编辑，完整图像共同inversion/denoising、
  attention injection或更精确sampler复用pretrained generator且无需训练；training-based inpainting则能从数据学习边界。
- **Changed Constraint:** DiT使foreground/background可按token分离，用户要求mask外背景严格不变，同时12B级
  generator让逐timestep、逐layer保存全部状态的memory cost成为PC部署约束。
- **Mechanism:** inversion时按`(timestep, layer)`缓存background tokens的K/V；denoising只让foreground tokens
  形成Q，将其K/V与缓存background K/V拼接后计算attention。可选reinitialization破坏原foreground，inversion
  attention mask阻断object信息扩散；inversion-free版本逐步消费并释放cache，将step-count空间从`O(N)`降为`O(1)`。
- **State Ownership:** user/segmenter拥有edit mask；pinned DiT/FLUX revision拥有QKV semantics；inversion pass拥有
  `background KV[timestep, layer, position]`生成与identity；denoising pass只读对应slice并更新foreground；final compositor
  将生成foreground与原background合并。这里的cache是编辑路径状态，不是Serving request prefix cache。
- **Control Flow / Data Flow:** source image + source prompt + mask → inversion path → per-step/per-layer background KV →
  target prompt + foreground/noise → foreground-only Q + foreground/cached-background K,V → edited foreground →
  composite with original background；inversion-free branch将每次inverse step与denoise step交替执行并立即释放KV。
- **Implementation Details:** v1基于FLUX.1-[dev] Rectified Flow；总28 steps、默认跳过最后4个inversion steps，
  inversion/denoising guidance为1.5/5.5；论文实验使用2×NVIDIA RTX 3090 24GB。官方demo提供大内存单机、
  双GPU、GPU offload及低CPU-memory inversion-free路径；current main不等于immutable W09 artifact。
- **Evaluation Contract:** PIE-Bench 620 images中的9类semantic editing任务，排除style transfer；比较image quality
  （HPSv2、aesthetic）、mask外背景（PSNR、LPIPS、MSE）与text alignment（CLIP、ImageReward）。User study从
  random class选110 images，由20+ participants成对比较quality/background/text/overall。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比P2P、MasaCtrl、RF-Inversion、RF-Edit、BrushEdit、FLUX-Fill；
  ablate no-skip、reinitialization、attention mask及inversion-free memory path。论文报告enhancements提高removal/text
  alignment但大mask时降低image quality/continuity；没有统一latency、energy或HBM peak table。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** FLUX.1-[dev]、2×RTX 3090 24GB、28 diffusion
  steps；precision、batch、concurrency、wall-clock latency、peak HBM/CPU、resolution distribution与production SLO为
  `Not Disclosed`。官方README的`>40GB CPU / 24GB GPU`是运行建议，不是论文benchmark contract。
- **What the Evidence Actually Proves:** 在作者披露的FLUX/PIE-Bench合同中，mask外background不再经过生成路径，
  因而其状态保存明显优于“重新生成后追求相似”；foreground仍可通过cached K/V读取background context。Ablation还证明
  removal强度与边界连续性之间存在可见trade-off。
- **What It Does Not Prove:** 任意DiT实现都可零修改适配、任意mask/分辨率/视频都严格一致、foreground与background
  边界无artifact、inversion-free与full-cache质量等价、单GPU生产SLO可达，或该KV与causal LLM KV具有相同不变量。
- **Limitations / Threats to Validity:** 单一FLUX base、单benchmark及作者实现；mask accuracy是外部依赖；style transfer被
  排除；user study人数只披露为20+；CLIP/ImageReward为proxy；precision/latency/memory峰值缺失；repository无W09 tag且
  later attention-scale/restructuring会造成version drift。
- **Trade-offs / New Failure Modes:** 从“背景重生成”转为“背景state pinning”获得像素一致性，却增加mask authority、
  timestep/layer cache identity、memory与model-revision binding；mask过大、残留foreground信息、prompt冲突会导致removal失败，
  reinitialization/attention mask又可能造成接缝。`O(1)` variant降低memory但会保留content artifact。
- **Where the Previous Design Still Applies:** 无严格背景一致性、需要global style/layout transformation、UNet base、mask不可靠、
  image很小或training data充足时，joint regeneration、attention injection、sampler correction或training-based inpainting仍合理；
  full-cache path在quality-first且memory足够时比inversion-free更清楚。
- **Evolution Relationship:** `Principle Reuse`：causal KV cache复用不再变化的历史token state；KV-Edit则人为冻结mask外
  background path并让新foreground查询该state。共同原则是“把不变量从重算路径移入版本化state”，但一个来自causal mask，
  一个来自editing contract，不能写成`Direct Evolution`。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Current Ch24）主 owner；handoff到
  `MULTIMODAL-REPRESENTATION`、`MODEL-SELF-ATTENTION`、`INFER-KV-CACHE`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch23 representation identity、Ch24 diffusion/iterative correction、Ch45 causal
  KV invariant与Ch66 evaluation contract；确认机制归生成编辑主线，Ch45只能引用状态复用类比。
- **Existing Coverage:** Ch24已有AR/diffusion、mutable state、commit/rollback主线，但尚可refine“编辑时不变量可以从
  generative transition中剥离”；Ch45已明确causal-history contract，足以防止术语误并。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；Historical Books Gate开启后只沉淀
  invariant extraction、state identity与quality/memory branch，不复制作者headline或表格。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；KV-Edit未写入Books，post-W09 attention scale与ICCV status未倒灌。
- **Open Questions:** immutable 2025-02-25 commit、exact dtype/resolution/peak memory/latency、single-GPU reproducibility、
  mask uncertainty、boundary metric、video temporal identity、model-agnostic modifications、inversion-free artifact rate与independent reproduction。

### K-LoRA: Adapter Composition Becomes a Timestep-and-Layer Selection Policy

- **Candidate / Week / Score:** K-LoRA: Unlocking Training-Free Fusion of Any Subject and Style LoRAs / 2025-W09 / 25/30。
- **Source Family ID:** `k-lora-diffusion-adapter-selection`。
- **Source Type:** arXiv v1/CVPR paper + supplementary material + official inference/training repository；author experiments，
  not independent reproduction。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-25、v2 2025-03-02；W09可读取v1与同周
  v2 metadata，但机制与评分锁定v1。Current GitHub有24 commits、无release/tag，不能反推event-time completeness。
- **Direct Primary Sources:** https://arxiv.org/html/2502.18461v1；https://arxiv.org/abs/2502.18461；
  https://github.com/HVision-NKU/K-LoRA；https://k-lora.github.io/K-LoRA.io/。
- **Related Primary Sources:** DreamBooth/StyleDrop datasets、SDXL/FLUX bases、ZipLoRA/B-LoRA/Multi-LoRA Composition
  baselines；community LoRAs只用于作者robustness case，不提升其provenance。
- **Access and Verification Status:** v1正文、公式、pseudocode、全部appendices、revision history与current official code/docs已核验；
  repository TODO仍列出SDXL/FLUX inference与video说明，且无immutable W09 artifact。
- **Full-read Coverage:** metadata、Abstract、Introduction、Related Work、LoRA preliminaries、两项empirical findings、
  Top-K layer selection、timestep/source scaling、SDXL/FLUX experiments、user/GPT-4o evaluation、fixed/random/K/scale
  ablations、prompt control、alternative scale、robustness与parameter sensitivity全部阅读。
- **Original Problem:** 独立训练的subject与style LoRAs直接权重相加会争夺同一attention update space，常出现主体形状、
  颜色或style丢失；joint/ZipLoRA/B-LoRA可缓解冲突但需要额外训练或改变原adapter。
- **Why the Previous Design Was Reasonable:** 静态加权merge实现简单、可形成单一artifact且适合语义兼容的adapters；joint training
  能显式学习交互；单adapter always-on避免online routing和per-step variation。在adapter少、组合固定或需要可预测执行时仍合理。
- **Changed Constraint:** 用户希望复用来自不同训练/社区来源的subject/style adapters，不再支付joint retraining；扩散过程又具有
  coarse-to-fine timestep structure，某些layers/steps不需要两个LoRA同时生效，为conditional selection提供空间。
- **Mechanism:** 对每个attention layer将content/style LoRA update取绝对值并flatten，各取`K=r_c*r_s`个最大元素求和；
  由timestep scale `S=alpha*t_now/t_all+beta`调节style score，来源scale `gamma`校正不同weight magnitude，最终在该layer/
  step完整选择content或style LoRA。它不逐元素混合，也不修改原LoRA矩阵。
- **State Ownership:** base revision与target-module schema拥有compatibility；每个LoRA artifact拥有rank、weights、subject/style role与
  provenance；K-LoRA policy拥有K、alpha/beta/gamma、timestep convention与per-layer selection；runtime拥有当前step、loaded adapters、
  route decision与batch/kernel execution；evaluation拥有组合是否可发布的evidence。
- **Control Flow / Data Flow:** independently trained subject/style images → two LoRA artifacts bound to one base → load both → for each
  diffusion timestep/layer compute Top-K magnitude summaries → apply timestep/source scaling → select one full adapter update → denoise →
  evaluate subject/style fidelity；artifact weights不被合并重写。
- **Implementation Details:** local adapters以SDXL v1.0、DreamBooth subject 4–5 images与StyleDrop/single style image训练；official
  example使用rank 8、1024 resolution、batch 1、1000 steps、constant LR `5e-5`、gradient checkpointing与8-bit Adam。
  Inference脚本覆盖SDXL与FLUX/community LoRAs；这些current instructions未由immutable event-time tag固定。
- **Evaluation Contract:** 18 object-style combinations×10 generated images；style similarity用CLIP，subject similarity用CLIP与DINO；
  比较Direct merge、joint training、ZipLoRA、B-LoRA。另随机选22 result sets做user preference，并用GPT-4o评价；paper未披露
  user count、prompt/order/blinding或GPT-4o prompt/version。
- **Baselines / Ablations / Sensitivity / Overhead:** fixed selection、1/3 content/2/3 style random selection、不同K、去除scale、
  cross-source gamma、alternative `S*`与alpha/beta grid；过小K使两种概念都弱，过大K导致style丢失/shape distortion；`S*`
  强化早期color blocks但削弱texture/brushstrokes。未报告selection overhead、memory、latency或multi-adapter batch cost。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** SDXL v1.0与FLUX；训练example为1024、batch 1、rank 8、
  1000 steps、mixed precision disabled。实验GPU、显存、inference steps/seeds全量合同、precision（FLUX）、concurrency、latency、
  throughput与SLO为`Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者18×10组合及其subject/style metrics中，adapter作用对layer和diffusion timestep并不
  均匀；保留原adapter、按step/layer选择能够形成不同于static merge/joint retraining的conditional composition branch，且
  ablation显示K与scale都会改变主体/style平衡。
- **What It Does Not Prove:** Top-K weight magnitude等于因果importance、`K=r_c*r_s`普适、alpha/beta/gamma无需调参、任意community
  LoRA安全兼容、多于两个adapters可扩展、LLM LoRA具有同样timestep规律，或作者user/GPT-4o preference等于生产质量。
- **Limitations / Threats to Validity:** 小规模自选组合、proxy metrics、user study protocol缺失、LLM judge自洽偏差、硬件与成本未披露、
  base/LoRA来源和license差异、weight magnitude受training/scaling影响、只比较两种role、repo无W09 tag且README/TODO状态矛盾。
- **Trade-offs / New Failure Modes:** training-free fusion避免joint optimization与lossy merge，却让每步每层routing成为runtime state；
  magnitude/scale漂移会导致selection flip，style与subject不能同时作用于同一layer，adapter churn增加memory/kernel/batching成本，
  policy参数与base/adapter任一revision变化都需重新evaluation。
- **Where the Previous Design Still Applies:** 单一adapter、固定组合、高风险可预测Serving或merge后kernel效率优先时static merge/always-on
  更合适；强冲突且有数据/预算时joint training可直接优化组合；需要同层连续叠加时weighted composition仍是独立分支。
- **Evolution Relationship:** `Alternative Branch`：static weight sum / joint training → preserve independent adapters → conditional
  per-layer/per-timestep selection。它复用MoE/routing原则但selection unit是完整LoRA layer，未训练router，也不是expert dispatch。
- **ROADMAP Node:** `TRAIN-LORA`（Current Ch30；Legacy Ch26）主 owner；handoff到
  `MULTIMODAL-GENERATIVE-PARADIGMS`、`INFER-VLLM`、`PLATFORM-MODEL-REGISTRY`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch29 objective边界、Ch30 adapter composition/dynamic serving、Ch24 diffusion steps、
  Ch50 multi-adapter runtime与Ch59 registry identity；确认训练与推理policy不能混为同一owner。
- **Existing Coverage:** Ch30已明确“数学可相加不保证行为兼容”并要求composition重新Evaluation；K-LoRA可refine为一个受限反例：
  保持adapter immutable，把冲突转化为step/layer selection，同时新增policy identity与runtime state。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；只在Historical Books Gate后补composition evolution与
  system contract，不保留作者“任意LoRA”“无需调参”等外推。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，current code与CVPR status不替代W09 v1 artifact evidence。
- **Open Questions:** immutable W09 commit、user/GPT judge protocol、GPU/precision/latency/memory、multi-adapter scalability、magnitude
  normalization、selection stability、license/provenance、base mismatch、batch locality、failure fallback与independent reproduction。

### ART: Structured Output Factorization Moves Control from Per-Region Text to Typed Layout State

- **Candidate / Week / Score:** ART: Anonymous Region Transformer for Variable Multi-Layer Transparent Image Generation / 2025-W09 / 26/30。
- **Source Family ID:** `art-anonymous-region-multilayer-generation`。
- **Source Type:** arXiv v1 + CVPR paper/supplement + Microsoft Research publication + official repository；current artifact withdrawn。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-25，唯一arXiv version；CVPR publication在June 2025，
  official repository于2025-07-23因training data可能来自illegal sources撤下weights、checkpoints与training/inference code。
- **Direct Primary Sources:** https://arxiv.org/html/2502.18364v1；https://arxiv.org/abs/2502.18364；
  https://openaccess.thecvf.com/content/CVPR2025/html/Pu_ART_Anonymous_Region_Transformer_for_Variable_Multi-Layer_Transparent_Image_Generation_CVPR_2025_paper.html；
  https://github.com/microsoft/art-msra。
- **Related Primary Sources:** Microsoft Research publication与official project page；FLUX.1[dev]、LayerDiffuse、COLE等只作为
  architecture/baseline lineage，不能替代withdrawn MLTD artifact。
- **Access and Verification Status:** v1 main text、全部supplement、CVPR copy与current official repo notice已核验；paper可读，
  但private MLTD data与曾发布weights/code已撤回，当前不可执行复现。
- **Full-read Coverage:** metadata、Introduction/Related Work、RGBA autoencoder、layout-conditioned 3D RoPE、MMDiT generation、
  LLaMA-3.1-8B layout planner、private dataset、training/evaluation、system comparisons、all ablations、supplementary conflict/
  label assignment、50-layer examples、RoPE implementation、layout variation/editing、transparency encoding与limitations全部阅读。
- **Original Problem:** 单层text-to-image无法产出可独立编辑的RGBA layers；已有multi-layer方法只支持少量固定层或按层串行生成，
  semantic layout还要求为每个region编写prompt，并在local/global conditions间制造attention conflict。
- **Why the Previous Design Was Reasonable:** per-region semantic prompt给用户明确对象控制，sequential generation降低一次性state size，
  unified raster image最容易训练和评价；层数少、语义必须人工锁定或数据缺乏时，这些设计仍更可控。
- **Changed Constraint:** graphic design需要variable layer count/resolution、独立alpha与layer editing；几十层使full attention和人工region
  caption成本快速增长，同时composed image与各layer必须共同harmonize。
- **Mechanism:** 将输出分解为merged reference、background与variable RGBA foreground layers；autoencoder对tight-cropped layers编码，
  ViT decoder联合恢复RGBA；`(x,y,layer)` 3D RoPE提供跨层位置identity；MMDiT以global prompt和只含bounding boxes的anonymous
  layout同时denoise全部layers，regional full attention只保留各layer有效region tokens；LLM planner从global prompt产生anonymous boxes。
- **State Ownership:** layout planner拥有box set但不拥有region semantics；alpha channel/box extraction拥有layer extent；autoencoder拥有
  RGBA latent schema；3D RoPE拥有spatial/layer index；MMDiT拥有跨global/background/foreground harmony；compositor拥有z-order与final image；
  dataset/license owner决定artifact是否可训练、发布和撤销。
- **Control Flow / Data Flow:** global prompt → LLaMA layout planner or human boxes → anonymous region layout → noisy merged/background/
  tight-cropped foreground latents + 3D indices → joint MMDiT denoising → multi-layer transparency decoder → variable RGBA layers →
  deterministic composition / layer-wise edit；semantic assignment由model cross-attention推断而非region prompt显式提供。
- **Implementation Details:** FLUX.1[dev]；ablation用LoRA rank 64、30K iterations、global batch 8、Prodigy LR 1.0、512²；
  system comparison用90K iterations、1024²；decoder为ViT-Base 12 layers/768 hidden/3072 MLP/12 heads/86M params；
  800K train + 5K validation，MLTD约1M private designs、平均11 layers/11.38K visual tokens。
- **Evaluation Contract:** Design-Multi-Layer-Bench与COCO-derived Photo-Multi-Layer-Bench；FID merged、PSNR、SSIM、RGB/alpha
  layer PSNR；30 participants各比较50 pairs，覆盖aesthetics、prompt/layout、typography与harmonization；efficiency figure以
  1024²、100 samples、不同layer counts比较attention variants。
- **Baselines / Ablations / Sensitivity / Overhead:** LayerDiffuse/COLE system baselines；semantic vs anonymous layout、with/without
  composed reference、full vs spatial+temporal vs regional full attention、2D/3D position encoding、80→800K data、3→51 layers、
  caption length、planner variants及decoder conditions。Paper headline `>12×`只属于其figure contract，GPU/precision未披露。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** FLUX.1[dev]、LoRA rank64、512²/1024²、batch8；
  GPU type/count、precision、training time、inference concurrency、exact layer-token distribution per point与production SLO为`Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者private data/evaluation合同内，显式layer identity、tight regional tokens与joint reference/
  background/foreground generation形成了可扩展structured-output branch；region-specific text不是唯一控制方式，且可能与global coherence冲突。
- **What It Does Not Prove:** anonymous layout普遍优于semantic control、model确实具有人类Schema Theory、50+ layers在任意scene均可靠、
  dataset合法可再用、current artifact可复现、headline speedup跨GPU/precision成立，或video/time dimension可直接复用layer axis。
- **Limitations / Threats to Validity:** private/withdrawn data与code使reproduction blocked；authors承认repeated/combined layer failures和layout
  generalization不足；typography落后COLE；GPT-4o harmonization是proxy；用户研究规模有限；没有hardware contract；dataset source legality
  直接破坏artifact lifecycle与长期可用性。
- **Trade-offs / New Failure Modes:** 去掉region prompts降低annotation/conflict，却减少explicit semantic authority；joint generation改善
  harmony却扩大state和coupled failure；regional crop降低compute却依赖box/alpha correctness；3D index支持variable layers却新增z-order/schema
  compatibility；private data带来质量却导致许可、删除、checkpoint撤销和不可复现风险。
- **Where the Previous Design Still Applies:** 少量layers、强语义锁定、typography-critical或需public reproducibility时semantic layout/
  renderer pipeline更合理；single raster generation适合无需post-edit的低延迟场景；sequential layer generation适合逐层人工approval。
- **Evolution Relationship:** `Alternative Branch`：single raster → fixed/few transparent layers → sequential semantic layers；ART走向
  anonymous typed layout + joint variable-layer generation。不是later method替代earlier branches，而是把human semantic work换成model prior和
  structured state。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Current Ch24）主 owner；handoff到
  `MULTIMODAL-REPRESENTATION`、`MODEL-POSITION-ENCODING`、`TRAIN-DATA`、`INFER-TENSORRT-LLM`与
  `PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch23 representation/provenance、Ch24 factorization/commit、Ch13 position encoding、
  Ch27 data contract、Ch49 execution plan与Ch66 evaluation；确认layer schema与generator主线不应散落成产品清单。
- **Existing Coverage:** Ch23已有modality/schema/provenance identity，Ch24已有generation state与commit；ART可refine“输出结构本身改变
  attention shape、control authority与artifact contract”，同时withdrawal为data provenance→model availability的反例。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Artifact Withdrawn`；只有机制与provenance lesson可进入
  Books，不能保留不可核验的可运行性或通用`12×`结论。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；没有下载/恢复已撤下artifact，也未将later CVPR/repo state倒写为W09 release。
- **Open Questions:** event-time repo/weights hash、MLTD source/license/delete scope、hardware/precision、attention figure raw values、
  z-order/overlap semantics、planner failure recovery、interactive edits、public-data reproduction与withdrawn derivatives处理。

### Clustering-On-Difficulty: Aggregate Loss Scaling Does Not Own Downstream Predictability

- **Candidate / Week / Score:** Unveiling Downstream Performance Scaling of LLMs: A Clustering-Based Perspective / 2025-W09 / 25/30。
- **Source Family ID:** `cod-downstream-performance-scaling`。
- **Source Type:** ByteDance Seed arXiv v1 paper；later ICLR 2026 revision/publication lineage；无public code/artifact located。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-24、v2 2025-05-23、v3 2025-10-11、v4
  2026-03-09；W09锁定v1。ICLR 2026 acceptance不倒写为event-time peer-review status。
- **Direct Primary Sources:** https://arxiv.org/html/2502.17262v1；https://arxiv.org/abs/2502.17262。
- **Related Primary Sources:** later OpenReview/ICLR paper只作revision lineage；Qwen2-72B与in-house MoE只作为mapping anchors；
  HF/Scholar仅用于discovery，不提供机制证据。
- **Access and Verification Status:** v1全部正文、proof、clustering/smoothing appendices、ablation、difficulty distribution与limitations已读；
  未找到public evaluation/training code、model checkpoints或raw predictions。v1 abstract的1.36%与正文Table 3 mean 1.63%冲突。
- **Full-read Coverage:** metadata、Introduction/Related Work、loss/performance pilot、COD four stages、assumptions/proposition/proof、
  Improved-MeanShift、fit/filter/map equations、nine dense models、eight benchmarks、three baselines、cluster/formula/anchor/interpolation
  ablations、smoothing、predictable-subset distribution与MoE/annealing/multiple-choice/CoT limitations全部阅读。
- **Original Problem:** pretraining loss在同loss点不能唯一决定OOD downstream accuracy；benchmark样本具有不同threshold、slope和ceiling，
  aggregate curve会把emergent、saturated与scalable samples混在一起，导致70B前置预测不可靠。
- **Why the Previous Design Was Reasonable:** loss power law平滑、便宜且适合模型族内compute planning；直接performance-compute或
  loss-intermediate fitting不需任务级多次evaluation。任务分布均匀、外推距离小、recipe固定时，aggregate baseline仍是合理起点。
- **Changed Constraint:** 大模型训练成本使full-scale试错不可接受；下游metrics离散、difficulty heterogeneity强，model size、LR schedule、
  data distribution和answer format都会破坏“同loss→同能力”的假设。
- **Mechanism:** 用一组递增dense models在每个sample上的passrate vector表示difficulty trajectory；Improved-MeanShift限制cluster
  diameter/minimum size并排除zero-performance outliers；每cluster拟合`g+(1-g)exp(-aC^-b-c)`，过滤非单调/低ceiling clusters；
  对predictable subset加权外推，再用过(0,0)/(1,1)且由external/in-domain anchors校准的quartic mapping回到full benchmark。
- **State Ownership:** training experiment拥有model/compute/data/LR identity；evaluation harness拥有sample passrates与few-shot prompts；
  clustering stage拥有difficulty vector/outlier/cluster revision；fit stage拥有curve/threshold；mapping stage拥有anchors/interpolation；
  capacity planner只能消费带uncertainty和regime identity的prediction，不能让一个headline替代release evidence。
- **Control Flow / Data Flow:** controlled small-model ladder + repeated sample evaluation → difficulty vectors + checkpoint smoothing → clusters/
  outliers → cluster-wise fits → predictable subset → target-compute extrapolation → anchor-calibrated subset→full mapping → prediction error
  audit against trained 70B → budget/monitoring decision。
- **Implementation Details:** 122M、238M、411M、652M、973M、1.9B、7B、12B predictors与68.452B target；training tokens
  26B→8.012T、constant LR、same data distribution；minimum cluster size 10，small-model passrate采用100 trials并对相邻3 checkpoints
  horizontal smoothing；evaluation为LLaMA3-aligned few-shot completion。
- **Evaluation Contract:** GSM8K、MATH、BBH、TriviaQA、MBPP、AGIEval、DROP、MMLU-Pro，500→17,944 questions、3–8 shots；
  absolute predicted-vs-actual percentage-point error，比较end-to-end、passrate、loss-intermediate、COD without mapping与complete COD。
- **Baselines / Ablations / Sensitivity / Overhead:** K-Means/DBSCAN/MeanShift/Improved variants；remove random-guess/ceiling terms；
  direct power law；quartic/cubic/quintic/spline mapping；without/OOD/ID anchors；predictable task ratio。v1 Table 3给complete COD mean/max
  1.63/2.38 pp，但abstract写1.36%，数值不能视为已闭合。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model sizes/tokens/layers/dims/heads已披露；accelerator、precision、
  global batch、sequence length、wall-clock/MFU、training failures与production SLO为`Not Disclosed`。该paper预测quality，不是runtime benchmark。
- **What the Evidence Actually Proves:** 作者实验表明task-level scaling heterogeneity是aggregate downstream prediction的重要误差源；在其
  fixed dense/constant-LR/data regime中，分群、可预测subset与anchor mapping共同降低了八个benchmark的预测误差。
- **What It Does Not Prove:** downstream accuracy由loss唯一决定、COD跨MoE/annealing/post-training/CoT成立、difficulty partition与model/data
  无关、zero-score samples永远不可预测、1.36/1.63任一headline正确，或预测误差足够小即可自动批准昂贵training run。
- **Limitations / Threats to Validity:** dense-only、constant LR、same data、finite-answer/few-shot completion；theory假设unique answer且无
  reasoning trace；multiple choice与true passrate不一致；需要大量questions/100 trials；anchors可能泄漏distribution assumptions；无code/raw data；
  v1 abstract/table numeric conflict；later 1.55%不可用于修复W09 v1。
- **Trade-offs / New Failure Modes:** task clustering减少heterogeneity却删除hard/non-emergent evidence；subset→full mapping恢复aggregate estimate
  却引入anchor dependence和polynomial over/underfit；repeated evaluations降低variance却增加成本；predictable benchmark可能偏向容易扩展的slice，
  让safety/long-tail failure被系统性排除。
- **Where the Previous Design Still Applies:** validation loss用于训练健康和in-domain trend；aggregate scaling适合均匀/大样本/近区间；直接
  full benchmark在target model已存在时拥有事实authority；MoE、annealing、post-training和CoT应先建立新ladder而非沿用COD曲线。
- **Evolution Relationship:** `Layering / Dependency`：aggregate loss scaling → task-level difficulty trajectories → predictable subset → calibrated
  full-set mapping；它扩展而非否定Kaplan/Chinchilla，前者预测不同对象，后者仍为pretraining resource allocation基线。
- **ROADMAP Node:** `WORLDVIEW-SCALING-LAW`（Current/Legacy Ch7）主 owner；handoff到 `TRAIN-PRETRAINING`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-COST`。
- **Target and Adjacent Chapters Read:** 已读Ch7 loss/capability boundary、Ch8 emergence measurement、Ch28 pretraining recipe、Ch66 subject/
  distribution/uncertainty与Ch70 lifecycle cost；确认COD应作为conditional downstream prediction branch而非替换通用scaling law。
- **Existing Coverage:** Ch7已明确loss不能直接推出能力且recipe/regime change使曲线失效；COD可refine“为什么benchmark内部difficulty variance
  也破坏外推，以及可预测subset怎样同时提供信号和制造盲区”。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Headline Metric Disputed`；未来只吸收对象分层、方法与
  failure modes，不保留冲突headline数值。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，未用2026 accepted version覆盖v1，也未把无artifact写成可复现。
- **Open Questions:** 1.36% vs 1.63% provenance、v1→v4 formula/data diff、public code/raw predictions、hardware/precision、MoE/annealing/
  post-training/CoT ladders、uncertainty intervals、cluster drift、anchor selection、safety slices与independent reproduction。

### Visual Perception Token: Perception Becomes a Model-Issued, Runtime-Executed Control Action

- **Candidate / Week / Score:** Introducing Visual Perception Token into Multimodal Large Language Model / 2025-W09 / 27/30。
- **Source Family ID:** `visual-perception-token-active-reencoding`。
- **Source Type:** arXiv v1 paper + official code/models/datasets；author-trained Qwen2-VL variants，Status: Experimental。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-24，唯一version；current repository无release tag，
  后续model/data inventory不能反推全部artifact在W09已发布。
- **Direct Primary Sources:** https://arxiv.org/html/2502.17425v1；https://arxiv.org/abs/2502.17425；
  https://github.com/yu-rp/VisualPerceptionToken。
- **Related Primary Sources:** linked Hugging Face model/dataset cards与pinned Transformers 4.45.2/LLaMA-Factory 0.9.1.dev0；
  Qwen2-VL、DINOv2、SAM只作base/encoder dependencies。
- **Access and Verification Status:** paper、supplement、training/evaluation contract、current source/config/model/data inventory已核验；
  无immutable W09 artifact，independent reproduction未核验。
- **Full-read Coverage:** metadata、Introduction/Related Work、Region Selection与Vision Re-Encoding tokens、architecture/equations、829K data、
  two-stage training、all main/supplementary results、grid/control-token/mask/projector ablations、examples、discussion与repository instructions。
- **Original Problem:** one-shot vision encoding固定了resolution、region与encoder；LLM发现问题后无法要求重新看局部、换视觉特征或把
  query-specific control反馈给projector，small text/object/spatial relation因早期压缩而不可恢复。
- **Why the Previous Design Was Reasonable:** fixed encoder→projector→LLM路径简单、batch shape稳定、一次计算即可回答；高分辨率或额外
  encoder全量运行最容易保证coverage。短图、低延迟和无需fine-grained perception时仍合理。
- **Changed Constraint:** document/OCR/fine-grained tasks的relevant region很小，精确bbox对不同分辨率难生成；不同query可能需要crop、
  DINO、SAM或原encoder的不同信息，perception budget应按需分配。
- **Mechanism:** 扩展vocabulary：六-token Region Selection以`k×k` grid cell编码近似box，触发crop→原encoder重处理；三-token
  Vision Re-Encoding触发额外encoder，其unsupervised control-token hidden state作为cross-attention projector的K/V来筛选vision features。
  Mask modeling迫使answer通过control state消费信息；global与new visual embeddings共同进入LLM。
- **State Ownership:** model拥有是否发出perception token与control hidden state；runtime/parser拥有token schema、grid→pixel映射、crop/
  encoder invocation与budget；vision encoder/projector拥有feature semantics；conversation state拥有first/second-pass embeddings；artifact
  identity绑定base、encoder、projector、token vocabulary与mask policy。
- **Control Flow / Data Flow:** image+question → coarse encode → LLM emits answer or typed perception tokens → validate action/token schema →
  crop or re-encode with selected branch → conditioned projector → append new visual embeddings → LLM answer；free-choice variant由模型决定是否调用。
- **Implementation Details:** Qwen2-VL-2B full tuning、7B LoRA rank512；additional DINO/SAM/original encoder；829K instruction samples；
  alignment 1 epoch LR2e-3 batch128仅projector，finetune 1 epoch LR2e-5 batch256冻结vision encoders；8×A100约20h；code pinned
  Transformers 4.45.2与LLaMA-Factory 0.9.1.dev0。
- **Evaluation Contract:** spatial/GQA/OpenImage/VSR、general LLaVA instruction、Flickr held-out、CUB、DocVQA/DUDE/POPE及MME/MMBench；
  test split存在时使用official，否则random split并去image overlap。Headline average混合不同datasets，不是统一production metric。
- **Baselines / Ablations / Sensitivity / Overhead:** 2B/7B bases、224/512 resolution、DINO/CLIP/SAM、forced/free-choice；grid `k=4/8/16`
  vs bbox、with/without control hidden state、1/2/4 tokens、mask modeling与projector tuning；`k=8`在作者任务上最好，过细增加token-learning成本。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 8×A100、Qwen2-VL 2B/7B、train batches128/256；A100 memory、
  precision、input/output lengths、inference batch/concurrency、perception-call rate、latency/HBM与SLO为`Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者Qwen2-VL/data合同中，将visual perception action编码为model-generated token并让runtime执行，
  能把one-shot representation变成iterative perception loop；explicit grid与latent control是两种不同interpretability/capacity分支。
- **What It Does Not Prove:** model知道何时必须重看、hidden state可解释、任意encoder/tool可接入、2B普遍胜过7B、headline 23.6%可跨任务
  平均、extra perception不会放大幻觉，或该接口已具备权限、预算、超时与fallback语义。
- **Limitations / Threats to Validity:** training/eval overlap由作者split policy控制；headline聚合异构metrics；多数数据进入training；无latency/
  call-rate报告；control token无可读语义；grid只能矩形单region；additional encoder增加supply-chain与feature drift；无明确limitations section。
- **Trade-offs / New Failure Modes:** active perception提升detail fidelity，却增加第二次encode、tokens、router error与tail latency；explicit grid可审计但
  coarse，latent control容量高但不可解释；false positive浪费compute，false negative永久丢detail，invalid token/box或encoder failure需fallback。
- **Where the Previous Design Still Applies:** fixed high-resolution encoder适合coverage-first；external OCR/detector适合deterministic authority；
  one-shot path适合短图/low-latency；human crop适合高风险review。VPT是conditional branch，不是所有请求必经步骤。
- **Evolution Relationship:** `Layering / Dependency`：fixed perception → model emits typed perception request → runtime re-encodes → model consumes
  observation。它复用Tool Calling principle，但action发生在model内部vision pipeline，side effect主要是compute/state而非外部世界。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Current Ch23）主 owner；handoff到 `AGENT-TOOL-CALLING`、`TRAIN-SFT`、
  `INFER-SCHEDULING`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch23 representation contract、Ch24 generation state、Ch29 SFT、Ch56 scheduling、Ch66 evaluation与
  Ch78 perception tool flow；确认control token schema归representation，runtime authority归Tool Calling。
- **Existing Coverage:** Ch78已有coarse perception→unresolved region→typed perception-tool request→source-linked observation主线；VPT可refine
  model-native trigger与latent-control branch，但不能把它当外部evidence authority。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；未来只沉淀active perception state machine、typed identity与
  failure semantics，不保留跨dataset headline。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，也未把current model/data inventory倒写为W09 release completeness。
- **Open Questions:** W09 commit/release、model/data card revision、inference call rate/latency/memory、multi-region/temporal perception、token parser/
  timeout/fallback、calibration、untrusted image attacks、encoder licensing与independent reproduction。

### MLLMs Know Where to Look: Localization Confidence Is Not Perception Correctness

- **Candidate / Week / Score:** MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs / 2025-W09 / 27/30。
- **Source Family ID:** `vicrop-internal-attention-guided-perception`。
- **Source Type:** ICLR 2025 paper + official MIT-licensed implementation + TextVQA bbox annotation artifact。
- **Event Date / First-public Date / Revision History:** official code 2025-01-26与ICLR acceptance 2025-01-21早于arXiv；paper owner event按
  arXiv v1 2025-02-24记录，唯一version。2025-03/04 Qwen2.5-VL additions属later lineage。
- **Direct Primary Sources:** https://arxiv.org/html/2502.17422v1；https://arxiv.org/abs/2502.17422；
  https://github.com/saccharomycetes/mllms_know；ICLR 2025 proceedings。
- **Related Primary Sources:** authors' TextVQA_GT_bbox dataset、LLaVA-1.5/InstructBLIP dependencies；later Qwen2.5-VL code不用于v1结果。
- **Access and Verification Status:** full v1、all appendices、official code/docs与artifact chronology已核验；event-time code存在但无release tag。
- **Full-read Coverage:** sensitivity intervention、attention localization、three ViCrop methods、bbox/high-res algorithms、two-model/seven-benchmark
  evaluation、layer/high-res/external-tool/overhead analyses、dataset statistics/manual annotations、prompt formats、LLaVA-NeXT/V* comparisons、
  limitations与repository implementation全部阅读。
- **Original Problem:** MLLM在small visual subjects上回答错误，需区分“没定位到对象”与“定位到了但压缩后看不清”；只扩大model或统一
  resolution会为所有requests支付成本，仍受input resolution上限。
- **Why the Previous Design Was Reasonable:** full image一次encode保留global relations、固定shape易batch；human crop是强oracle；training higher-res
  model可把能力内化。large concepts/global questions或低latency时旧路径仍合理。
- **Changed Constraint:** detail-sensitive OCR/VQA的subject占比很小，global resize抹掉信息；attention/gradient已包含query-specific localization
  signal，允许在不训练weights时做第二次focused observation。
- **Mechanism:** 将answer-start token→image-token attention与connector token→patch attention组合并做generic-instruction normalization（rel-att），
  或以decision gradient加权attention（grad-att），或直接input gradient；用多尺度sliding window从importance map选crop，resize后把cropped
  image tokens与original tokens拼接。>1K image先分blocks求importance再重组。
- **State Ownership:** original image拥有source truth；model internal attention/gradient只拥有proposal signal；selected layer/window heuristic拥有
  crop policy；runtime拥有second forward、token concatenation与budget；answer model拥有最终prediction；evaluation bbox只用于analysis，不应泄漏线上。
- **Control Flow / Data Flow:** image+question → first pass/start-token internal maps → normalize/aggregate → sliding-window crop proposal → validate crop →
  re-encode crop + retain global tokens → second answer pass → scorer；external SAM/YOLO/CLIP是alternative locator branch。
- **Implementation Details:** v1测试LLaVA-1.5与InstructBLIP，official repo含modified Transformers、rel-att/grad-att/pure-grad与seven datasets；
  TextVQA analysis从5,000 questions手工筛成4,370 unambiguous pairs；high-res blocks<1024²，window scales `{1,1.2,…,2}`。
- **Evaluation Contract:** TextVQA、V*、POPE、DocVQA、AOKVQA、GQA、VQAv2；human-crop size intervention还覆盖BLIP-2、Qwen-VL、GPT-4o；
  v1 result table绑定LLaVA-1.5/InstructBLIP。Overhead在RTX A6000与Intel Gold 5317报告，非serving goodput。
- **Baselines / Ablations / Sensitivity / Overhead:** no crop/human crop、rel-att/grad-att/pure-grad、selected/averaged layers、with/without high-res、
  external SAM/YOLO/CLIP、LLaVA-NeXT/V* comparison；LLaVA rel/grad GPU overhead约1.16/0.89s，pure-grad 2.36s，具体仅限作者环境。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** LLaVA-1.5、InstructBLIP；RTX A6000、Intel Gold 5317用于overhead；
  precision、batch、concurrency、prompt/output lengths、memory、TTFT/TPOT与SLO为`Not Disclosed`。
- **What the Evidence Actually Proves:** size intervention表明small-subject accuracy损失有因果perception component；在作者models/datasets中，
  internal localization signal即使answer错误仍可帮助propose useful crop，second observation改善detail-sensitive accuracy。
- **What It Does Not Prove:** attention是faithful causal explanation、所有wrong answers都定位正确、crop置信度等于答案置信度、multiple regions/
  counting/relations可解、任何MLLM可零修改应用，或1–2秒overhead满足production SLO。
- **Limitations / Threats to Validity:** 只聚焦单region；relation/counting帮助有限；新增visual tokens与固定overhead；manual TextVQA subset；
  selected layer使用held-out set；connector architecture影响额外tokens可用性；attention/gradient maps可能受prompt/adversarial distractor影响。
- **Trade-offs / New Failure Modes:** training-free避免重训，却把请求变成two-pass pipeline；保留global tokens降低crop tunnel vision但增加context；
  incorrect map会放大错误region并形成self-confirmation；high-res tiling增加preprocessing；gradient methods需backward-like work且难batch。
- **Where the Previous Design Still Applies:** global relation/counting、多对象、short image或strict latency时no-crop/full view更合理；human/external detector在
  high-risk或有typed ontology时更可靠；training-based high-res model适合稳定高流量workload。
- **Evolution Relationship:** `Principle Reuse`：model internal state → bounded perception proposal → source-derived second observation；不是
  attention→truth。与VPT相比，ViCrop不训练trigger，而由runtime固定执行；VPT则把是否/如何重看写入model output contract。
- **ROADMAP Node:** `AGENT-TOOL-CALLING`（Current Ch78；Legacy Ch74）主 owner；handoff到
  `MULTIMODAL-REPRESENTATION`、`AGENT-CONTEXT`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch23 lossy representation、Ch75 bounded context、Ch78 uncertainty-driven perception tools及Ch66
  evaluator boundary；现有章节已区分proposal、source-linked observation与truth authority。
- **Existing Coverage:** Ch78已完整覆盖coarse native perception→unresolved region→typed crop/OCR/frame seek→verify/abstain，并记录crop identity、
  provenance与self-confirmation failure；本family提供primary evidence但没有新的长期机制缺口。
- **Integration Decision:** `Books Pending — No Change Candidate`；年度Books pass应以Ch78具体段落完成去重，不重复写一份ViCrop论文摘要。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；没有修改Books，later Qwen2.5 code/results未倒写为W09 evidence。
- **Open Questions:** immutable event-time commit、attention faithfulness、multi-region selection、uncertainty-based controller、batched two-pass runtime、
  adversarial crops、security/provenance、mixed-modality generalization、tail latency与independent reproduction。

### Finding the Sweet Spot: Preference-Pair Difficulty Is a Data-Control Variable

- **Candidate / Week / Score:** Finding the Sweet Spot: Preference Data Construction for Scaling Preference Optimization / 2025-W09 / 27/30。
- **Source Family ID:** `preference-pair-reward-distribution-sweet-spot`。
- **Source Type:** arXiv v1 + later ACL 2025 paper lineage + official code/data/checkpoints；author experiments，Status: Experimental。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-24、v2 2025-05-21、v3 2025-06-28；W09锁定v1。
  ACL publication与later affiliation/code updates不倒写为event-time facts。
- **Direct Primary Sources:** https://arxiv.org/html/2502.16825v1；https://arxiv.org/abs/2502.16825；
  https://github.com/XYaoooo/DPO_Pair。
- **Related Primary Sources:** ACL Anthology final paper、linked Hugging Face sampled-response/reward datasets与checkpoints；Armorm、Skywork、
  UltraFeedback、AlpacaEval 2和Arena-Hard只在作者实验合同内使用。
- **Access and Verification Status:** v1全部正文/appendix、84-model grid、5→400 sample scaling、two reward models、academic benchmarks与
  current official scripts/data/checkpoints已核验；repository无release/tag，不能固定W09 commit。
- **Full-read Coverage:** metadata、DPO derivation/background、max-min case study、reward-distribution construction、21 pair combinations、
  four policy bases、sample scaling、reward-model transfer、training loss/overfitting analysis、hyperparameters、academic evaluations、appendix
  extended points/400 samples/top rewards与artifact surface全部阅读。
- **Original Problem:** on-policy sampling从5扩到200/400时，传统`max reward` chosen + `min reward` rejected并不持续改善DPO，甚至出现
  win-rate下降；仅增加sample budget没有定义pair是否可学习、是否过于极端或是否被reward outlier支配。
- **Why the Previous Design Was Reasonable:** max-min最容易实现、margin最大且直觉上提供清晰偏好；sample少、reward稳定或只需快速构造
  pairs时仍合理。DPO本身也不要求reward distribution model，因此旧pipeline具有更少状态。
- **Changed Constraint:** sample scale增大后extreme order statistics继续移动，minimum可能成为异常/低质量response；pair margin过大可让训练
  loss快速下降却诱导shortcut/overfit，过小又让chosen/rejected难区分。Data selection成为随sample budget变化的控制问题。
- **Mechanism:** 对每个prompt的`n` responses用reward model打分，以prompt-specific `mu,sigma`近似分布；选择`{min,mu±2sigma,
  mu±sigma,mu,max}`最近样本，枚举21个ordered pairs并训练比较；经验上保持高reward chosen、将rejected固定在`mu-2sigma`附近，
  随n增加chosen质量提升而避免minimum extreme drift。
- **State Ownership:** sampler拥有policy/temperature/n/seed；reward stage拥有reward-model revision和per-prompt scores；pair builder拥有
  distribution estimate、point-selection/tie/missing policy与chosen/rejected identity；DPO trainer拥有reference/beta/template；evaluation拥有
  independent judge与length control。Reward score不是human truth。
- **Control Flow / Data Flow:** prompt → SFT/on-policy sampling `n` → score with pinned RM → per-prompt distribution/representative responses →
  pair policy `(high, mu-2sigma)` → DPO policy/reference forwards → checkpoint → AlpacaEval/Arena/academic slices → adjust sample/pair policy。
- **Implementation Details:** Llama-3-8B/Mistral-7B base经UltraChat SFT及对应Instruct bases；UltraFeedback prompts；sampling temperature0.8，
  n=5/20/60/100/200，追加400；Armorm与Skywork RMs；DPO batch128/1 epoch，LR 5e-7 or 3e-7、beta0.01/0.1；
  8×H100 + 8×A100；vLLM sampling，repo含SFT/DPO/sample/reward scripts。
- **Evaluation Contract:** AlpacaEval 2 805 prompts，win rate与length-controlled win rate；Arena-Hard comparison；ARC-C、HellaSwag、
  TruthfulQA、GSM8K regression slices。主要结论来自四个7B/8B model settings和author judge pipeline，不是human preference universal law。
- **Baselines / Ablations / Sensitivity / Overhead:** max-min at different n、all21 pair positions、mu±3/4sigma、5→400 samples、Armorm→Skywork、
  base/instruct与academic tasks；small margin underfits，extreme max-min有最低train loss却lower eval；Llama-Instruct 100→200有小幅下降，
  所以“持续提升”存在例外/plateau。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 8H100+8A100、Llama3-8B/Mistral7B、train batch128、1 epoch；
  precision、sequence lengths、sampling concurrency、wall-clock/token cost、RM throughput、failure/retry与SLO为`Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者四model/two-RM/UltraFeedback合同中，preference pair质量不能由reward ordering alone表示；
  chosen/rejected绝对位置与margin共同影响optimization/generalization，更多on-policy samples只有配合selection policy才转化为收益。
- **What It Does Not Prove:** rewards服从normal distribution、`mu-2sigma`跨RM/model/domain永久最优、minimum一定错误、DPO loss越低越差、
  human preference等于RM score，或sample 400以上仍按同一curve扩展。
- **Limitations / Threats to Validity:** 4个7B/8B models、同一prompt source、main judge benchmarks由models评分；normal fit未经严格goodness-of-fit；
  order statistics依赖RM calibration；84-model search可能selection bias；无human study/independent reproduction；repo无immutable tag；成本未完整报告。
- **Trade-offs / New Failure Modes:** distribution-aware pair降低extreme outlier影响，却新增per-prompt大量sampling/RM cost、distribution estimation、
  RM drift与selection policy version；moderate rejected可能更可学，也可能保留有害内容；固定sigma rule在skew/multimodal rewards上失效。
- **Where the Previous Design Still Applies:** 低budget n=2/5、human-curated pairs、verified binary outcome或reward noise很低时max-min/simple pairs更省；
  online PPO/GRPO在需要探索current policy state时仍是另一分支；SFT用于absolute demonstrations而非pair margin。
- **Evolution Relationship:** `Direct Evolution`：fixed max-min pair → sample scaling暴露extreme drift/overfit → distribution-aware pair position →
  sample-budget-conditioned data policy。它refine DPO input contract，不改变DPO objective formula。
- **ROADMAP Node:** `TRAIN-DPO`（Current Ch34；Legacy Ch30）主 owner；handoff到 `TRAIN-DATA`、`TRAIN-RLHF`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-COST`。
- **Target and Adjacent Chapters Read:** 已读Ch31 RLHF data/reward、Ch34 DPO pair margin/offline bias、Ch27 data lineage、Ch66 judge/evidence与
  Ch70 lifecycle cost；确认owner是pair construction而非新optimizer。
- **Existing Coverage:** Ch34已说明chosen/rejected可能都差、margin/length/independent eval，但尚可refine“pair绝对reward位置与sample budget共同
  定义difficulty；最低training loss可能是shortcut而非generalization”。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；Historical Books Gate后只沉淀data-control/evolution与边界，
  不把`mu-2sigma`写成通用常数。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，later ACL status/code state未替代W09 v1 evidence。
- **Open Questions:** reward distribution fit/calibration、human preference validation、RM ensemble/disagreement、skew/multimodal rewards、n>400、
  larger/reasoning models、sampling/RM lifecycle cost、harmful rejected filtering、event-time commit与independent reproduction。

### WiCkeD: Testing Knowledge of Absence Requires a Valid Counterfactual Dataset

- **Candidate / Week / Score:** WiCkeD: A Simple Method to Make Multiple Choice Benchmarks More Challenging / 2025-W09 / 27/30。
- **Source Family ID:** `wicked-mcq-absence-counterfactual`。
- **Source Type:** arXiv v1 + later ACL 2025 short-paper lineage + official open code/data/classifier；benchmark transformation study。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-25，唯一arXiv version；later ACL paper reports7 benchmarks whereas
  v1 explicitly evaluates6，W09 locks six-benchmark contract。
- **Direct Primary Sources:** https://arxiv.org/html/2502.18316v1；https://arxiv.org/abs/2502.18316；
  https://github.com/ahmedselhady/wicked-benchmarks；official SBA classifier model card。
- **Related Primary Sources:** Eval-Harness task implementations、MMLU/MMLU-Pro/MMLU-Redux/CommonsenseQA/TruthfulQA/ARC-Challenge；
  later ACL version只作lineage，不更改v1 denominator。
- **Access and Verification Status:** v1 main/appendices、algorithm、SBA/SCA filtering、18-model direct/CoT results、five random variants、
  prompt/equations及official repository/model已核验；repo安装示例存在path typo且无release tag。
- **Full-read Coverage:** metadata、benchmark shortcut/NOTA literature、replacement algorithm、coherence classifier、4K labeling protocol、
  six benchmarks、18 models、5-shot direct/zero-shot CoT、ranking/degradation analysis、SBA classifier precision/recall、prompting与artifact surface。
- **Original Problem:** conventional MCQ可通过option priors、elimination或recognition选中显式correct choice，却不测试模型能否判断“所有给定选项
  都不成立”；原benchmark saturation也掩盖knowledge gap与reasoning fragility。
- **Why the Previous Design Was Reasonable:** fixed options提供确定gold、低成本scoring和跨模型可比性；well-written distractors本已测试discrimination。
  训练/教育场景或需要稳定历史trend时原benchmark继续成立。
- **Changed Constraint:** strong models在原MCQ上接近ceiling且可能利用spurious correlations；需要minimal counterfactual在保持question和option count
  大致不变时，改变“正确答案是否在集合内”这一decision contract。
- **Mechanism:** 每题uniform随机替换一个option为`None of the above`；若删correct，NOTA成为gold，否则原correct保留；生成5个随机variants。
  为避免Single-Best-Answer题删最佳后第二佳变成正确却仍标NOTA，用GPT-4o-mini标4K样本、人工校验1K、训练BERT classifier，
  predicted SBA原样复制而不变换。
- **State Ownership:** source benchmark拥有question/options/gold/license；transformer拥有seed/replaced index/NOTA label；SBA classifier只拥有
  coherence filter proposal；manual audit拥有validation truth；Eval-Harness拥有prompt/label scoring；run必须记录variant seed与classifier revision。
- **Control Flow / Data Flow:** source MCQ → SBA/SCA classification → if SBA copy unchanged; else seeded option replacement → recompute gold →
  five variant datasets → 5-shot label-prob or zero-shot CoT evaluation → compare paired original/transformed accuracy/ranking → inspect reversals。
- **Implementation Details:** 4K samples from MMLU/MMLU-Pro/TruthfulQA/CommonsenseQA；1K manual eval +3K synthetic-label BERT train；classifier
  SBA recall98.9%、precision95.1%；six Eval-Harness benchmarks、five variants；18 open-weight 7B–72B models；CoT max generation4096。
- **Evaluation Contract:** direct MCQ uses5 demonstrations so most prompts include NOTA-correct example；CoT on MMLU/MMLU-Pro/MMLU-Redux；
  model families Qwen2.5/Llama3.1/Gemma2/Mistral/DeepSeek-R1 distills，report mean/std across variants and paired degradation。
- **Baselines / Ablations / Sensitivity / Overhead:** original benchmark is paired baseline；base vs instruct、direct vs CoT、family/size sensitivity；
  v1 average drop约12.2 points in Table1（abstract 12.1 rounding），ranking shifts；no matched human difficulty study or alternative wildcard wording ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model identities/sizes与CoT max4096 disclosed；hardware、precision、batch、
  concurrency、latency/cost与SLO为`Not Disclosed`。这是evaluation design，不是serving benchmark。
- **What the Evidence Actually Proves:** minimal option-set counterfactual exposes capability not measured by original MCQ: recognizing correct-answer absence；
  performance degradation and ranking shifts vary by model family，so original accuracy does not fully order this behavior。
- **What It Does Not Prove:** drop entirely等于reasoning deficit、NOTA wording无bias、classifier removes all incoherent items、R1 models普遍更会
  abstain、WiCkeD harder meansbetter benchmark，或MCQ absence detection predictsopen-ended uncertainty/calibration。
- **Limitations / Threats to Validity:** classifier still permits~1.1% SBA false negatives and synthetic-label bias；SBA items copied unchanged造成mixed
  transformed intensity；NOTA avoidance/prior与few-shot demonstration影响结果；random variants有限；later 6→7 benchmark drift；no human item analysis。
- **Trade-offs / New Failure Modes:** automatic transformation低成本且保留paired comparison，却新增classifier/seed/version state、label noise和NOTA
  format artifact；过滤SBA提高validity但不同benchmarks变换比例不同；强制absence可测epistemic branch，也可能只是新的prompt skill。
- **Where the Previous Design Still Applies:** open-ended/executable tasks更直接测真实能力；原MCQ用于historical continuity；human-reviewed NOTA items用于
  high-stakes exams；calibrated selective QA必须测试answer/abstain operating point，而非只看NOTA accuracy。
- **Evolution Relationship:** `Principle Reuse`：static benchmark → paired counterfactual transformation → explicit missing-answer state → model/ranking
  sensitivity。它不是新training method，而是改变measurement intervention，同时保留original as control。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Current Ch66；Legacy Ch62）主 owner；handoff到 `MODEL-SAMPLING`、
  `TRAIN-DATA`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch66 subject/distribution/slices/abstention/counterfactual evidence、Ch20 answer selection、Ch27 data
  provenance与Ch72 security；确认NOTA不等于production abstention，但可作为bounded diagnostic。
- **Existing Coverage:** Ch66已有abstain cost/operating point与paired counterfactual主线；WiCkeD可refine“counterfactual transformation本身也需gold
  coherence classifier、seed与mixed-intensity accounting”，不是再加一张benchmark表。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；未来沉淀measurement intervention与dataset failure，v1 headline/
  model ranking留在Review notes。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，未用later ACL七benchmark版本覆盖v1六benchmark事实。
- **Open Questions:** sixth→seventh benchmark revision、event-time code hash、SBA false-negative audit、NOTA lexical bias、human difficulty、variant count、
  open-ended/selective-QA correlation、contamination、cost与independent reproduction。

### TheoremExplainAgent v1: Multimodal Artifact Generation Makes Hidden Reasoning Errors Executable

- **Candidate / Week / Score:** TheoremExplainAgent: Towards Multimodal Explanations for LLM Theorem Understanding / 2025-W09 / 26/30。
- **Source Family ID:** `theorem-explain-agent-multimodal-artifact-workflow`。
- **Source Type:** arXiv v1 + TheoremExplainBench + later official generation/evaluation repository；vendor-model workflow study。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-26；v2 2025-05-25改题为`Video-based`并加入camera-ready内容。
  Official generation/evaluation code 2025-03-03才发布，W09只把code列为later artifact lineage。
- **Direct Primary Sources:** https://arxiv.org/html/2502.19400v1；https://arxiv.org/abs/2502.19400；
  https://github.com/TIGER-AI-Lab/TheoremExplainAgent；https://tiger-ai-lab.github.io/TheoremExplainAgent/。
- **Related Primary Sources:** TheoremExplainBench 240-theorem dataset、generated video data与Manim/Kokoro/LiteLLM dependencies；later ACL oral
  status不提升v1 experimental evidence等级。
- **Access and Verification Status:** v1 full text、evaluation/cost appendix、revision history与current official code/docs已核验；event-time
  executable code未公开且current repo无W09 release/tag。
- **Full-read Coverage:** metadata、Related Work、task definition、planner/coder/critic/RAG workflow、benchmark construction、five metrics、
  240-theorem experiments、success/quality/correlation/error/case studies、limitations/risks、runtime/cost/artifact appendices及current code surface。
- **Original Problem:** text-only theorem explanation可语言流畅却隐藏错误推导；生成5–10分钟visual explanation需要scene decomposition、Manim code、
  rendering、layout、narration与repair，one-shot generation无法维持长artifact consistency。
- **Why the Previous Design Was Reasonable:** short text explanation/one-shot code成本低、可快速检查；人工Manim提供高layout quality；单步RAG适合
  明确API query。简单定理、短视频或human review充足时旧方案仍合理。
- **Changed Constraint:** long-form output把reasoning变成可执行visual artifact；一个错误会在多scene、code compile、layout与TTS间传播，
  需要把plan、code、render和repair分成持久阶段，并分别验证execution success与pedagogical quality。
- **Mechanism:** Planner按定理生成storyboard/scenes；coding agent把scene转为Manim code；executor/render pipeline运行并由critic/fix loop处理
  failures；optional agentic RAG在storyboard、implementation、repair阶段生成不同queries并缓存。Final videos由scene clips+narration合成。
- **State Ownership:** planner拥有scene DAG/specification；coder拥有versioned source；renderer拥有compile/runtime artifact；critic只拥有typed
  repair proposal；RAG index拥有docs snapshot；assembler拥有audio/video timeline；evaluation分别拥有success与五维quality evidence。
- **Control Flow / Data Flow:** theorem/context → plan scenes → optional stage-specific retrieval → generate code → execute Manim → diagnose/retry →
  render clips + TTS → assemble video → transcript/keyframe/chunk scoring → commit/reject；failed scene不可由final average静默覆盖。
- **Implementation Details:** v1比较GPT-4o、Gemini 2.0 Flash、Claude 3.5 Sonnet v1、o3-mini medium，planner/coder使用同一candidate；
  benchmark 240 theorems×4 STEM domains×3 difficulty；assumed 7 scenes/4 fixes；later repo用LiteLLM、Manim、Kokoro/FFmpeg/LaTeX。
- **Evaluation Contract:** execution success rate与Accuracy/Depth、Visual Relevance、Logical Flow、Element Layout、Visual Consistency五维；text/transcript
  由GPT-4o评，key frames由GPT-4o评，motion chunks由Gemini 2.0 Flash评；quality table含human-made Manim baseline，judge非ground truth。
- **Baselines / Ablations / Sensitivity / Overhead:** agentless<20s vs agentic up to10min；with/withoutRAG across models；difficulty/domain slices；
  error types与human comparison。RAG有时降低success/score，说明more context可产生generic/misaligned API calls；没有independent judge/human calibration。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** vendor API models，约7 scenes/4 fixes；paper报告per-video 1120–2380s、
  input up to1.05M tokens、cost$0.10–$4.67的受限配置；hardware、provider snapshot、batch/concurrency、retry distribution与SLO未完整披露。
- **What the Evidence Actually Proves:** 在作者TheoremExplainBench/workflow中，long artifact需要explicit planning/execution/recovery；visualization可把
  text explanation中难定位的reasoning/application错误暴露为scene/code/layout evidence；RAG并非单向收益。
- **What It Does Not Prove:** execution success等于theorem correctness、model“深刻理解”定理、LLM judges可靠等同human learning、o3-mini普遍优越、
  visual explanation提高学习效果，或later code在W09可运行。
- **Limitations / Threats to Validity:** vendor API/version drift、same model planner/coder correlated errors、model judges与generator同生态、240 synthetic/
  curated theorem set、无student learning study、layout issues普遍、cost/latency高、artifact code发布跨周、RAG corpus/relevance threshold未完全锁定。
- **Trade-offs / New Failure Modes:** workflow提升长度/recovery却新增scene boundary、code execution、retrieval mismatch、audio/video sync、partial artifact
  cleanup与judge bias；visuals增强diagnosis也可能让错误图形产生更高false confidence；rigid templates提高logical score但损失表达性。
- **Where the Previous Design Still Applies:** text explanation适合快速/可搜索review；human-authored visualization适合高风险education；one-shot artifact适合短任务；
  deterministic theorem prover/renderer checks优先于LLM judge，RAG仅在API/docs freshness真正需要时启用。
- **Evolution Relationship:** `Layering / Dependency`：text answer → storyboard → executable visual artifact → multimodal evaluation/recovery；不是video
  替代text，而是将reasoning claim投射到更多可观察failure surfaces。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Current Ch81；Legacy Ch77）主 owner；handoff到 `AGENT-PLANNING`、`AGENT-RAG`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-COST`。
- **Target and Adjacent Chapters Read:** 已读Ch79 planning、Ch81 durable artifact/refinement、Ch76 RAG、Ch66 artifact/judge evidence及Ch70 cost；
  当前owner已覆盖plan→execute→evaluate→rollback和RAG负收益边界。
- **Existing Coverage:** Ch81已有versioned artifact、typed feedback、sequential refinement与thin-control/thick-state；Ch66已有artifact+environment+
  trace及multimodal judge边界。该family提供案例证据，但没有新的长期机制缺口。
- **Integration Decision:** `Books Pending — No Change Candidate`；年度Books pass应引用现有具体论点去重，paper/model ranking仅留Weekly。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，2025-03-03 code与later ACL/v2状态未倒写为W09 artifact availability。
- **Open Questions:** v1 event-time prompts/code、provider snapshot、judge-human correlation、student learning outcome、independent theorem verifier、
  partial-scene recovery、RAG threshold/cache identity、sandbox/security、cost distribution与reproducibility。

### BIG-Bench Extra Hard v1: Replacing Saturated Tasks Trades Longitudinal Continuity for Measurement Headroom

- **Candidate / Week / Score:** BIG-Bench Extra Hard / 2025-W09 / 28/30。
- **Source Family ID:** `bbeh-general-reasoning-task-replacement`。
- **Source Type:** Google DeepMind/Research arXiv v1 + Apache-2.0 official dataset/evaluator；benchmark construction/evaluation study。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-26、v2 2025-05-06；W09锁定v1 tasks/results。Later ACL/
  leaderboard/evaluator integrations只作lineage。
- **Direct Primary Sources:** https://arxiv.org/html/2502.19187v1；https://arxiv.org/abs/2502.19187；
  https://github.com/google-deepmind/bbeh。
- **Related Primary Sources:** source datasets for23 tasks、BBH counterpart prompts与later Lighteval/Inspect integrations；各derived task需保留原source
  attribution/license，不能只引用aggregate BBEH。
- **Access and Verification Status:** v1 full text、23 task descriptions/appendix、BBH counterpart comparison、provider/open-weight results与official
  evaluate.py/data已核验；repo仅5 commits且无release/tag，API model snapshots不完全immutable。
- **Full-read Coverage:** metadata、BBH saturation/shortcut analysis、12 reasoning-skill taxonomy、all23 task replacements、construction/sample counts、
  random/input/output-length comparisons、9-model table、general-vs-reasoning/small-vs-large analyses、task-specific failures、BBH pair table与reproducibility。
- **Original Problem:** BBH被strong models饱和，13/23 tasks选项少导致random floor高，部分任务可走shortcut，macro input仅约700 chars；
  aggregate high score不再分辨many-hop、long input、distractor、algorithm induction和conflict handling。
- **Why the Previous Design Was Reasonable:** frozen BBH提供长期可比、广技能覆盖与低成本evaluation；短输入/limited options使scoring稳定。
  regression、历史趋势和资源有限场景仍需保留旧suite。
- **Changed Constraint:** model能力提高后ceiling压缩ranking，benchmark contamination/shortcut更容易；需要增加reasoning depth和input complexity，
  但若只扩展同一道题会保留已知shortcut，因此选择同domain的新task counterpart。
- **Mechanism:** 对BBH每个23 tasks替换为同/更广reasoning domain的新task，200 questions/task（DisambiguationQA 120）；引入many-hop、
  learning-on-the-fly、error tracing、long-context/multi-needle、strong-prior override、distractors、algorithm induction等skills；以task accuracy
  harmonic mean聚合，保留per-task slices并与原BBH counterpart成对比较。
- **State Ownership:** source task拥有semantic/rubric/license；BBEH transformation/curation拥有new examples与counterpart mapping；evaluator拥有prompt/
  answer extraction；provider/model revision拥有run identity；aggregate metric只拥有summary，不能覆盖per-task floor/format failure。
- **Control Flow / Data Flow:** saturated suite diagnosis → define skill taxonomy → select/build harder counterpart per task → validate answer/rubric →
  run pinned models → record per-task accuracy + random floor + extraction failures → harmonic aggregate → compare counterpart/headroom → refresh decision。
- **Implementation Details:** 23 tasks；200 examples each except120；tests general-purpose Llama3.1-8B-Instruct、Gemma2-27B-IT、Gemini Flash-Lite/
  Flash、GPT-4o及reasoning Distill-R1-Qwen32B、DeepSeek-R1、o3-mini high；official repository supplies JSON/task code/evaluate.py/leaderboard。
- **Evaluation Contract:** broad general reasoning而非math/code-only；per-task exact/defined scorers，overall harmonic mean；API runs through AI Studio、
  OpenAI、Together，open models loaded onGPU；v1 reports best general-purpose9.8% vs reasoning-specialized44.8%，但provider/harness contract限制外推。
- **Baselines / Ablations / Sensitivity / Overhead:** random baseline、BBH counterpart pair、general vs reasoning、Gemini Flash vs Flash-Lite、task/input/
  output length analyses。Output length约7×仅是thinking proxy；below-random due unextractable answer时some analysis clamps to random floor，改变comparison。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/API identities disclosed；open-model GPU type/count、precision、batch/
  concurrency、prompt limits、latency/cost与SLO多数`Not Disclosed`。Benchmark分数不是runtime性能数字。
- **What the Evidence Actually Proves:** BBH在2025 model set上存在ceiling/shortcut/headroom问题；paired harder tasks显著扩大failure visibility，
  reasoning-specialized与general models的relative behavior因skill slice而异；单aggregate score不能解释原因。
- **What It Does Not Prove:** BBEH测量“通用推理”全部维度、longer output即更多有效thinking、reasoning model44.8%可跨provider复现、每个new task
  无污染/shortcut、难度越高越有效，或BBH应被删除。
- **Limitations / Threats to Validity:** new tasks与old tasks不是item-level同分布；longitudinal comparability受损；200/task方差有限；API versions可漂移；
  answer extraction/format失败混入reasoning；harmonic mean强惩罚near-zero；task source licenses/contamination不统一；无human difficulty calibration。
- **Trade-offs / New Failure Modes:** replacement恢复headroom却断开原trend；多skill/long input提高真实性却增加cost、format与scorer surface；harmonic mean
  防止强项掩盖弱项，却可能由一个broken task支配；公开benchmark未来仍会再次饱和/污染，需要suite lifecycle而非一次升级。
- **Where the Previous Design Still Applies:** BBH用于historical regression/cheap smoke test；domain-specific/executable benchmarks用于有明确truth的任务；
  production slices验证实际workload。新suite应与旧suite重叠运行一段时间，而非静默替换。
- **Evolution Relationship:** `Direct Evolution`：diverse BIG-Bench → hard subset BBH → saturation/shortcut diagnosis → same-skill harder task replacement BBEH →
  future living/frozen dual suites。每步换取headroom并付出continuity和governance成本。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Current Ch66；Legacy Ch62）主 owner；handoff到 `WORLDVIEW-SCALING-LAW`、
  `MODEL-SAMPLING`、`TRAIN-DATA`与`PLATFORM-COST`。
- **Target and Adjacent Chapters Read:** 已读Ch66 dataset governance/frozen/adversarial/slices、Ch7 scaling/capability boundary、Ch20 answer extraction、
  Ch27 provenance与Ch70 cost；确认主缺口是benchmark lifecycle而非模型机制。
- **Existing Coverage:** Ch66已有frozen benchmark、adversarial suite、contamination与object/distribution/scorer identity；可refine“saturation后task replacement
  恢复headroom但必须dual-run维持continuity”，这是当前正文未明确串起的演进。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；未来只沉淀benchmark lifecycle/trade-off，不复制23-task清单或排名。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，v2/ACL/later leaderboard未倒写为v1 evidence。
- **Open Questions:** v1 immutable repo commit、API model snapshots/prompts、task-level confidence intervals、contamination/source licenses、human difficulty、
  harmonic-vs-macro decision、format failure normalization、dual-run retirement policy与independent reproduction。

### Plutus: Domain and Language Form a Product Space, Not Two Independent Benchmark Labels

- **Candidate / Week / Score:** Plutus: Benchmarking Large Language Models in Low-Resource Greek Finance / 2025-W09 / 25/30。
- **Source Family ID:** `plutus-greek-financial-evaluation-and-adaptation`。
- **Source Type:** arXiv v1 + public benchmark/datasets/model/leaderboard collection；domain/language evaluation and LoRA adaptation study。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-26，唯一version；HF model/datasets主要于2025-02-27发布，
  GRFinSUM collection later update 2025-04-23。W09 paper与event-time artifacts分别记录。
- **Direct Primary Sources:** https://arxiv.org/html/2502.18772v1；https://arxiv.org/abs/2502.18772；
  https://huggingface.co/collections/TheFinAI/plutus-benchmarking-greek-financial-llms。
- **Related Primary Sources:** Plutus-8B model card、six dataset cards与Open Greek Financial LLM Leaderboard；source annual reports/exam data/
  FNS-2023/GRMultiFin licenses决定各task可用范围。
- **Access and Verification Status:** v1全18-page内容、task/data/annotation/evaluation/training/human-review appendices与current public collection已核验；
  collection later updates存在，缺少统一immutable W09 release manifest。
- **Full-read Coverage:** metadata、Greek/financial related work、five task definitions、six datasets、instruction conversion、22-model evaluation、
  Plutus-8B LoRA/quantization training、automatic/human metrics、task/human results、annotation guidelines/demography/process、quality agreement、licenses与ethics。
- **Original Problem:** multilingual general models和English financial models分别掌握language或domain的一部分，却可能在Greek financial numeric entities、
  terminology、long documents与reasoning上同时失效；只用通用Greek或English finance benchmark无法定位交叉缺口。
- **Why the Previous Design Was Reasonable:** translate English financial benchmark成本低、便于跨语言比较；general Greek model复用广语料；
  English financial model保留domain vocabulary。资源稀缺、只需粗略能力扫描时这些旧分支仍合理。
- **Changed Constraint:** high-risk finance要求原语言span、数字、实体和事实一致；Greek morphology/long names与financial semantics共同决定labels，
  translation会改变span/tokenization/terminology，聚合单task分数无法代表真实domain workload。
- **Mechanism:** Plutus-ben将Greek finance拆成numeric NER、textual NER、QA、abstractive summarization、topic classification，分别定义schema/
  metric/split/license；Plutus-instruction用四个training datasets做instruction tuning，GRFinQA留作held-out generalization；以Greek-capable
  Llama-Krikri-8B为base做int4 LoRA，形成Plutus-8B并在同一multi-task suite和human summary rubric下比较。
- **State Ownership:** source document/license拥有事实与用途；annotation guideline/annotator拥有span/summary labels；dataset version拥有split/
  translation/schema；training manifest拥有included/excluded tasks；model artifact拥有base/LoRA/quantization；EvalRun拥有prompt/scorer/provider；
  leaderboard只展示结果，不拥有cross-task truth。
- **Control Flow / Data Flow:** public Greek financial sources → expert annotation + agreement audit → task-specific datasets/splits/licenses →
  instruction conversion (exclude GRFinQA) → int4 LoRA training → immutable model revision → five-task automatic eval + summary human eval →
  per-task evidence/leaderboard → domain release decision。
- **Implementation Details:** base Llama-Krikri-8B-Instruct；LoRA rank16/alpha32/dropout0，int4 base，block size4096、sequences up to42K，
  AdamW LR5e-4 cosine、3 epochs、batch1、gradient accumulation4、bf16；Plutus-ben test sizes100/100/225/50/54。
- **Evaluation Contract:** 22 models across proprietary/general small/general large/English financial/Greek general；Entity F1 for NER、accuracy for QA/
  classification、ROUGE-1 for summarization；human summary review scoresGreek fluency/coherence/factuality 1–5；tasks are not exchangeable despite reported mean。
- **Baselines / Ablations / Sensitivity / Overhead:** cross-category comparison与held-out GRFinQA provide limited transfer/generalization evidence；
  no matched ablation separating Greek pretraining、finance instruction、LoRA、quantization or data volume；no seed/sensitivity/cost/throughput analysis。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/training dtype bf16、int4 base、4096 blocks/up to42K、batch1/accum4 disclosed；
  GPU type/count、training time/cost、serving concurrency、latency、throughput与financial SLO为`Not Disclosed`。
- **What the Evidence Actually Proves:** 在Plutus-ben条件下，language specialization与domain specialization不可互相替代；expert-native annotation、
  task-specific schema和domain adaptation共同提高Greek financial slices，held-out QA improvement提供有限transfer evidence。
- **What It Does Not Prove:** Plutus-8B适合financial advice、Greek/finance factors因果独立、ROUGE代表summary factuality、42K context有效使用、
  leaderboard mean可跨task比较、int4/LoRA无损，或translated English data不能帮助任何Greek task。
- **Limitations / Threats to Validity:** datasets/test sets很小、单国家/语言/domain、22 models的prompt/provider/version可能异构、source licensing混合
  Public/CC-BY/CC-BY-NC、human rater population有限、no seeds/confidence intervals、training/eval potential topical overlap、paper template metadata残留。
- **Trade-offs / New Failure Modes:** local expert data提高semantic fidelity却成本高/refresh慢；multi-task suite扩大coverage却aggregate掩盖critical slice；
  domain fine-tuning增加numeric/NER能力却可能窄化general behavior；long documents增加context cost；finance deployment还需fresh data、citation、
  abstention、regulation与human approval，paper未提供。
- **Where the Previous Design Still Applies:** translation benchmark用于cheap cross-lingual smoke test；general Greek model用于开放域；English financial model
  用于English workload；RAG/source-linked workflow适合fresh/high-stakes facts；specialized model只在stable terminology/high volume时值得维护。
- **Evolution Relationship:** `Layering / Dependency`：general multilingual evaluation → language slice → domain slice → language×domain task contract →
  expert dataset + specialized artifact → deployment evidence。不是“domain model替代general model”，而是增加高风险slice和资产成本。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Current Ch66；Legacy Ch62）主 owner；handoff到 `TRAIN-DATA`、`TRAIN-SFT`、
  `MODEL-LONG-CONTEXT`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch66 subject/distribution/domain slices/human raters、Ch27 data provenance、Ch29 SFT、Ch22 effective context
  与Ch72 high-risk/security；确认language×domain contract已由现有框架承载。
- **Existing Coverage:** Ch66已要求intended-use population/slices、task-specific scorer与uncertainty；Ch27已有source/license/annotation lineage；Ch72要求
  high-risk evidence。Plutus提供具体domain case，但没有新的长期机制缺口。
- **Integration Decision:** `Books Pending — No Change Candidate`；年度Books pass引用现有章节具体论点去重，不复制model leaderboard。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，也未把2025-04 later dataset update倒写为W09完整artifact。
- **Open Questions:** event-time manifest/checksums、GPU/cost/seeds、prompt/provider versions、confidence intervals、translation leakage、license compatibility、
  dataset refresh、citation/freshness/abstention、regulatory review、42K effective-context evidence与independent reproduction。

### Project Alexandria: A Derived Knowledge Index Must Preserve Claims, Provenance and Legal Scope Separately

- **Candidate / Week / Score:** Project Alexandria: Towards Freeing Scientific Knowledge from Copyright Burdens via LLMs / 2025-W09 / 25/30。
- **Source Family ID:** `alexandria-scientific-knowledge-units`。
- **Source Type:** technical position report + author legal analysis + synthetic MCQ experiments + public code/dataset lineage；legal status is jurisdiction-specific。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-26、v2 2025-04-18；W09锁定v1。Current large-scale Scientific-Summaries
  dataset与22M+ paper claims是later project lineage，不能倒写为v1 evidence。
- **Direct Primary Sources:** https://arxiv.org/html/2502.19413v1；https://arxiv.org/abs/2502.19413；
  https://github.com/LAION-AI/project-alexandria；official project/database links。
- **Related Primary Sources:** LAION Scientific-Summaries dataset card、peS2o/arXiv/S2ORC/OpenAlex metadata sources；German legal opinion is referenced/
  linked in supplement but its source status and applicability require separate legal review。
- **Access and Verification Status:** v1 paper、KU schema/example、German/US legal argument、all MCQ/overlap/embedding experiments、criticisms/open problems与
  public repo surface已核验；technical evidence verified，legal defensibility remains`Jurisdiction-Specific / Emerging`，not legal advice。
- **Full-read Coverage:** metadata、Introduction、Knowledge Units、German copyright/US fair use analysis、4-domain abstracts/long papers、MCQ retention、
  n-gram/plagiarism/reconstruction tests、embedding alternative、criticisms/impact/open problems、KU/MCQ/overlap appendices与legal-opinion availability boundary。
- **Original Problem:** scientific paper同时包含facts/methods/relations与受保护expression；直接复制/简单paraphrase可能保留style，embedding又无法
  可靠保存数字、因果和关系，paywall/licensing限制RAG corpus可共享性。
- **Why the Previous Design Was Reasonable:** 原文chunk是最强source fidelity与citation authority；embedding index成本低且不暴露明文；人工knowledge
  graph质量更高。授权corpus、高风险研究或proof/table不可压缩时，旧方案继续成立。
- **Changed Constraint:** 希望跨机构共享derived scientific knowledge，同时不分发原文；系统需要将claim content、expression overlap、source attribution、
  access/delete policy和jurisdictional legal basis拆成不同状态，而不是用“summary”一个字段混合。
- **Mechanism:** 以paragraph为单位让LLM抽取entities、attributes、relationships，加previous-KU context summary维持局部连续性，并保存source sentence
  MinHash/DOI provenance；long paper按200-word chunks、参考前10 units。KUs作为structured retrieval/index artifact，原文只在ephemeral TDM或受控存储中存在。
- **State Ownership:** source publisher/license拥有原文使用范围；extractor/model/prompt拥有KU transform；KU schema拥有typed claims；MinHash/DOI拥有
  lineage而非完整citation proof；legal policy拥有jurisdiction/use/purpose/retention；community/validator拥有correction/supersession；source remains truth authority。
- **Control Flow / Data Flow:** authorized source → ephemeral parse/chunk → LLM KU extraction + prior-unit context → claim/provenance/overlap validation →
  publish derived index under explicit legal policy → retrieve KU → dereference/cite source when authorized → correct/supersede/delete affected derivatives。
- **Implementation Details:** abstract study uses1K Biology、1K Math、1K Physics peS2o +1K CS arXiv abstracts，3 MCQs/abstract；full-paper study100 Medical+
  100 Physics papers，200-word chunks、previous10 KUs、10 MCQs/paper；Gemini Pro1.5-002生成MCQs/gold，multiple models answer；repo lacks immutable W09 release。
- **Evaluation Contract:** no-context lower bound、original-text upper bound、KU-only treatment；4 domains/6 answer models for abstracts，3 models/2 domains for
  full papers；surface reproduction measured by5/7/11-gram Jaccard and online plagiarism detector，plusprompted reconstruction。Same source-generated MCQs constrain validity。
- **Baselines / Ablations / Sensitivity / Overhead:** original/no-context/KU；Gemini vs Qwen KU/reconstruction；BGE-M3 embedding sanity checks include gibberish/
  unrelated/scrambled/original。No human fact audit、cross-source contradiction、schema ablation、chunk-size sweep or legal adversarial review。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model versions partially disclosed；hardware、precision、batch/concurrency、extraction
  throughput/cost、storage/index size、latency与SLO为`Not Disclosed`。Retention percentage is QA accuracy ratio, not byte/fact recall guarantee。
- **What the Evidence Actually Proves:** 在作者synthetic MCQ合同中，structured KUs保留了大量可被同类models问答的facts，同时surface n-gram overlap
  通常低；embedding cosine对scrambled text仍高，说明semantic similarity不能替代claim-level preservation。
- **What It Does Not Prove:** 约95%所有scientific knowledge被保留、KUs无hallucination/omission、proof/table/diagram可等价转换、低text overlap即无
  copyright infringement、US/German分析适用于其他jurisdictions/use cases，或MinHash足以支持每个claim。
- **Limitations / Threats to Validity:** position paper；legal memo/applicability非独立裁决；MCQ/gold由same frontier model从source生成，可能偏向KU可回答facts；
  no domain experts/manual claim recall；online plagiarism tool非legal test；paragraph-local graph丢global nuance；later dataset规模不等于quality。
- **Trade-offs / New Failure Modes:** KU降低明文分发与token cost，却引入extraction hallucination、relation flattening、schema drift、source deletion传播、
  attribution dilution、legal policy misclassification与false confidence；保存MinHash增强lineage但可能成为source fingerprint/privacy concern。
- **Where the Previous Design Still Applies:** licensed full-text RAG用于accuracy/citation；human-curated graph用于high stakes；embedding用于coarse candidate retrieval；
  table/proof/image保持native artifact；无法确认rights或claim fidelity时应只保留metadata/link而不发布derived content。
- **Evolution Relationship:** `Alternative Branch`：full-text corpus → embedding index / paraphrase → structured KU derived index；更长期应演进为
  claim-level provenance + cross-source validation + legal-policy gate，而不是让KU覆盖source。
- **ROADMAP Node:** `AGENT-RAG`（Current Ch76；Legacy Ch72）主 owner；handoff到 `TRAIN-DATA`、`AGENT-MEMORY`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch76 source/index/chunk/provenance/sufficiency、Ch27 license/delete lineage、Ch77 derived memory、Ch66
  claim-level evidence与Ch72 security；确认KU是derived retrieval artifact，不是新的source authority。
- **Existing Coverage:** Books已有embedding≠truth、source digest/license、claim evidence与derived memory governance；可refine“expression-removal与fact/
  provenance/legal-scope必须独立验证”，并将legal claim明确保持jurisdiction-specific。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Legal Status Jurisdiction-Specific`。不能把论文法律论证写成通用事实。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，later 22M+ dataset claims未用于W09评分。
- **Open Questions:** human claim recall/precision、proof/table/multimodal handling、cross-source contradiction、source deletion、MinHash reversibility、schema/
  interoperability、jurisdiction/use policy、market substitution、attribution/citation、event-time artifact与independent legal/technical review。

### REFUTE: Generating a Solution and Falsifying a Candidate Are Orthogonal Executable Capabilities

- **Candidate / Week / Score:** Can Language Models Falsify? Evaluating Algorithmic Reasoning with Counterexample Creation / 2025-W09 / 29/30。
- **Source Family ID:** `refute-executable-counterexample-generation`。
- **Source Type:** arXiv v1 technical report + executable benchmark/dataset/evaluator + official project/repository；later COLM publication lineage。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-26，唯一version；later COLM acceptance不倒写W09 peer-review status。
- **Direct Primary Sources:** https://arxiv.org/pdf/2502.19414v1；https://arxiv.org/abs/2502.19414；
  https://falsifiers.github.io/；https://github.com/falsifiers/REFUTE。
- **Related Primary Sources:** public REFUTE dataset、Codeforces statements/submissions/editorials与exact language versions；LiveCodeBench/model rating只为
  solution-generation comparison，not measured execution of same task pipeline。
- **Access and Verification Status:** 28-page v1 PDF、all methods/filtering/prompts/agent/search/error appendices、project results与official executable repo已核验；
  repo仅4 commits、无release/tag，provider API snapshots需按paper IDs锁定。
- **Full-read Coverage:** metadata、falsification framing、formal task、647→324 dataset pipeline、topics/ratings、prompt/few-shot/correct-code/ReAct、
  RandSearch/Oracle、validators/timeouts、5-model costs/results/error correlation、all prompts/examples/limitations/impact与artifact evaluator。
- **Original Problem:** solution-generation benchmark只测“构造一个正确program”，不测“针对一份看似合理但错误的program主动寻找使其失败的input”；
  self-reflection/critique若没有counterexample能力，可能只重写解释而无法推翻错误candidate。
- **Why the Previous Design Was Reasonable:** unit tests/known cases能低成本验证常见bug；solution generation适合明确spec；model judge可处理开放文本。
  已有强test suite、形式证明或简单bug时旧工具仍更直接。
- **Changed Constraint:** subtle competitive-programming submissions曾通过许多tests甚至contest后才被hack；有效反例可能很多且不可预列，要求模型生成
  arbitrary input-generator code，由executable oracle检验existential claim，而不是与一个reference string比对。
- **Mechanism:** 给problem statement、constraints和incorrect code，模型输出Python/C++ program生成candidate input；validator检查format/constraints，
  分别运行buggy与held-out correct solution，outputs不同即成功。Agent最多10次30s code execution +5次submission repair；RandSearch生成random
  input+brute solver，Oracle branch提供correct solver，所有search有1–2min budget。
- **State Ownership:** problem/source revision拥有spec；incorrect submission拥有candidate identity；editorial solution拥有test oracle但不是公开给默认model；
  generator artifact拥有candidate distribution；sandbox/compiler/timeout拥有execution semantics；validator拥有verdict；agent feedback只能修复submission。
- **Control Flow / Data Flow:** recent Codeforces problems/submissions → filter evaluator-compatible/rating/trivial/random/bait cases → pin buggy+correct code →
  model emits input generator → sandbox executes generator/input validation → buggy and correct programs run → compare outputs → feedback/retry → pass@k/error analysis。
- **Implementation Details:** 647 problems→495 evaluator-compatible→403 rating≥1200→345 non-random-trivial→324 afterhuman bait filtering；304 programmers、
  317 C++ submissions、35+ topics、problem Elo1200–3500；official package caches compiled code and supports exact Codeforces languages/OpenRouter。
- **Evaluation Contract:** DeepSeek-V3、Claude3.5-Sonnet-20241022、Gemini2.0-Flash-Thinking-0121、DeepSeek-R1、o3-mini-high-0131；zero/few-shot、
  with-correct, ReAct with/without demos, RandSearch/Oracle；success only if valid input causesbuggy≠correct within budgets。Solution%由ratings估计而非same-run generation。
- **Baselines / Ablations / Sensitivity / Overhead:** prompt vs agent feedback、correct-code reveal、search strategies、success byproblem/author/test depth/length；
  best counterexample<9%，agent primarily reducesvalidation errors；RandSearch failures约35%，其中多数来自wrong brute solver；strategies find disjoint successes。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** API model revisions and per-run strategy budgets disclosed；hardware/precision、
  batch/concurrency、full token/latency distribution和production SLO未披露。Cost table is provider-specific and must not be generalized。
- **What the Evidence Actually Proves:** 在324 executable tasks中，falsification success远低于rating-estimated solution capacity，correct code与execution
  feedback不自动关闭gap；different strategies find partially disjoint counterexamples，so capability is not one scalar “coding ability”。
- **What It Does Not Prove:** solution-generation percentage与counterexample percentage严格可比、models不会在future versions改善、REFUTE覆盖scientific
  falsification、correct solution绝对无bug、executable verdict等于real-world correctness，或反例能力足以保证self-improvement。
- **Limitations / Threats to Validity:** solution capacity是Elo-derived estimate；Codeforces/algorithmic domain；human filter removes bait；oneincorrect
  submission/problem；provider/version drift；sandbox/oracle bugs；public benchmark contamination over time；no confidence intervals per strategy in headline；
  open scientific claims often lack executable oracle。
- **Trade-offs / New Failure Modes:** inverse benchmark提高错误发现evidence，却需trusted oracle/sandbox、arbitrary-code isolation、timeout、language/runtime
  versions和dynamic refresh；search扩大coverage但生成的brute solver也可错；feedback降低format failure却未必提高semantic diagnosis。
- **Where the Previous Design Still Applies:** predefined tests用于fast regression；formal proof/SMT适合可形式化spec；mutation/fuzzing适合coverage；solution
  generation仍测constructive ability；开放研究需expert/cross-source evidence而不能伪造executable certainty。
- **Evolution Relationship:** `Alternative Branch`：solve specification → verify candidate on known tests；REFUTE增加candidate→generate adversarial counterexample→
  executable falsification。两branch应在Workflow中组合，但一方不能代表另一方。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Current Ch66；Legacy Ch62）主 owner；handoff到 `AGENT-REFLECTION`、
  `AGENT-WORKFLOW`、`MODEL-SAMPLING`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch66 executable artifact/verifier/evidence ladder、Ch80 feedback independence/constraint audit、Ch81 artifact loop、
  Ch20 sampling/pass@k与Ch72 sandbox security；REFUTE补全constructive vs falsification axis。
- **Existing Coverage:** Ch66已有answer→artifact→executable verifier与mutation/adversarial ladder，Ch80已有external verifier优先；可refine“solution correctness
  与counterexample generation是正交capabilities，reflection必须能产生可执行否证而非仅解释”。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；model percentages和Codeforces rankings留在Review notes。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，later COLM status未倒写v1。
- **Open Questions:** immutable W09 dataset/repo commit、oracle/reference audits、sandbox isolation、dynamic refresh/contamination、multiple bugs/submissions、
  pass@k/cost curve、SMT/fuzzing hybrids、natural-language/scientific counterexamples与independent reproduction。

### Distill Any Depth: Teacher Output, Normalization and Observation Context Form One Supervision Contract

- **Candidate / Week / Score:** Distill Any Depth: Distillation Creates a Stronger Monocular Depth Estimator / 2025-W09 / 22/30。
- **Source Family ID:** `distill-any-depth-cross-context-multiteacher`。
- **Source Type:** arXiv v1 + project page + official inference/models repository；domain-specific pseudo-label distillation study。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-26、v2 2025-04-21；paper/project/models/demo reported released
  2025-02-26，GPU demo update2025-03-02、small model2025-03-08。W09 locks v1 and event-time artifact surface。
- **Direct Primary Sources:** https://arxiv.org/html/2502.19204v1；https://arxiv.org/abs/2502.19204；
  https://github.com/Westlake-AGI-Lab/Distill-Any-Depth；https://distill-any-depth-official.github.io/。
- **Related Primary Sources:** DepthAnythingv2、GenPercept、MiDaS teachers and SA-1B unlabeled data；later community integrations do not establish
  paper-time reproduction。
- **Access and Verification Status:** v1 full text/appendix、all normalization/context/teacher ablations、five-benchmark evaluation与current official repo已核验；
  README在发布models/demo同时仍将training/evaluation code列TODO，event-time full reproduction incomplete。
- **Full-read Coverage:** metadata、MDE/semi-supervised background、global/local/hybrid normalization equations、shared/local-global contexts、random
  multi-teacher mechanism、50K ablation setup、cross-architecture/five-benchmark comparisons、qualitative/limitations、model/code chronology全部阅读。
- **Original Problem:** unlabeled RGB可由teacher生成pseudo-depth，但global scale-shift-invariant normalization会把teacher局部噪声传播到整幅map；
  teacher看global image保结构却丢detail，看crop保detail却失去scene-wide relative depth。
- **Why the Previous Design Was Reasonable:** single teacher/global context与global normalization最简单、shape稳定且保证全图尺度关系；有高质量dense
  ground truth、domain窄或detail不关键时仍合理。
- **Changed Constraint:** zero-shot MDE需从large unlabeled corpus吸收细节并跨indoor/outdoor分布；不同teachers的output scale/distribution和不同crop
  context不可直接比较，监督表示本身成为noise/identity contract。
- **Mechanism:** Hybrid Normalization在多个depth-value contexts计算scale/shift-invariant loss；Shared-Context让teacher/student看同crop；Local-Global
  让teacher看local crop、student看full image，只在overlap监督；training iteration随机选择GenPercept/DepthAnythingv2等teacher，以teacher diversity
  形成mixture，而非先平均不兼容pseudo labels。
- **State Ownership:** each teacher revision拥有pseudo-label semantics；crop/augmentation拥有observation context与coordinate map；normalizer拥有group/
  scale/shift definition；student training run拥有selected-teacher sequence；dataset/source拥有image rights；evaluation alignment拥有metric transform。
- **Control Flow / Data Flow:** unlabeled image → sample teacher + global/local context → teacher pseudo-depth → context-aware normalization → align crop/global
  coordinates → student full/crop prediction → shared/local-global losses → update student → unseen benchmark scale/shift alignment → release artifact。
- **Implementation Details:** ablation uses50K SA-1B images、560²、batch4、~20K iterations、single NVIDIA V100；teachers include diffusion GenPercept and
  DINOv2-based DepthAnythingv2，student DPT/DA/MiDaS variants；official repo releases24.8M/97.5M/335.3M checkpoints but manifest/tag absent。
- **Evaluation Contract:** unseen NYUv2、KITTI、ETH3D、ScanNet、DIODE；AbsRel and delta1 after scale+shift alignment；cross-context on ETH3D/DIODE、
  cross-architecture teachers/students、five-benchmark multi-teacher and SOTA comparisons。Relative depth metrics do not prove metric depth/control safety。
- **Baselines / Ablations / Sensitivity / Overhead:** global/local/hybrid normalization、no/shared/local-global/both context losses、DA/MiDaS teacher-student
  crossings、single vs multi teachers；no matched teacher-call FLOPs、training wall time、energy or label-cache/storage analysis。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** V100、560²、batch4 disclosed for50K ablation；full-scale train hardware/data size、
  precision、teacher concurrency/cache、wall time、inference latency/throughput、edge/robotics SLO为`Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者MDE合同中，pseudo-label transform与teacher observation context显著改变student结果；local/global
  constraints互补，heterogeneous teachers可在随机 mixture下转移不同细节/structure bias。
- **What It Does Not Prove:** hybrid normalization普适于其他modalities/tasks、random teacher selection优于所有ensembles、pseudo-labels正确、relative
  depth可用于physical control、student全面强于每个teacher、或artifact可按paper完全复现。
- **Limitations / Threats to Validity:** single domain、mostly author benchmarks、pseudo-label teacher errors、no uncertainty/calibration、SA-1B subset licensing/
  sampling未详述、current training/eval code status矛盾、full training contract缺失、qualitative “detail” judgement与SOTA tables可能受alignment影响。
- **Trade-offs / New Failure Modes:** cross-context提高detail却增加crop coordinate/teacher compute；multi-teacher提高diversity却引入teacher-selection variance、
  incompatible scales、lineage/storage与bias mixture；normalization抑制global noise也可能抹掉真实metric scale。
- **Where the Previous Design Still Applies:** labeled metric-depth supervision用于safety/control；single teacher适合成本/稳定性；global context适合large structure；
  local crop适合detail-only tasks；offline cached pseudo-labels在teacher成本高时更可复现。
- **Evolution Relationship:** `Principle Reuse`：single teacher/global pseudo-label → context-aware supervision → multiple teacher mixture。它refine
  distillation contract，不构成通用multimodal architecture evolution。
- **ROADMAP Node:** `TRAIN-SFT`（Current Ch29；Legacy Ch25）主 owner；handoff到 `TRAIN-DATA`、
  `MULTIMODAL-REPRESENTATION`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch29 teacher/student state-distribution/lineage、Ch27 derived data、Ch23 coordinate representation及Ch66
  evaluation boundary；现有章节已经覆盖teacher identity、pseudo-label bias与cross-context contract。
- **Existing Coverage:** Ch29已明确teacher strength/trajectory不自动等于可学target，soft/hard/on-policy distillation必须绑定state与teacher lineage；
  DAD是视觉领域的受限例证，没有新的全书机制缺口。
- **Integration Decision:** `Books Pending — No Change Candidate`；不把MDE benchmark表或“stronger”标题写入长期正文。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，later small model/GPU demo未倒写W09。
- **Open Questions:** immutable event-time repo/model hashes、full train/eval code、teacher call/cache cost、pseudo-depth uncertainty、metric scale recovery、
  teacher selection policy、full SA-1B sampling/license、control-task validation与independent reproduction。

### MMKE-Bench: A Knowledge Edit Is a Versioned State Transition, Not a Single Correct Answer

- **Candidate / Week / Score:** MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge / 2025-W09 / 26/30。
- **Source Family ID:** `mmke-bench-multimodal-knowledge-editing`。
- **Source Type:** ICLR 2025 arXiv v1 + public dataset/code/project；benchmark and comparative editing-method study。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-27、v2 2025-03-01；repo claims code/data released2024-10-25 but
  contains a likely typo `2023-10-25` for HF paper. W09 owner is arXiv v1；artifact chronology remains inconsistent。
- **Direct Primary Sources:** https://arxiv.org/html/2502.19870v1；https://arxiv.org/abs/2502.19870；
  https://github.com/MMKE-Bench-ICLR/MMKE-Bench；official project/dataset。
- **Related Primary Sources:** BLIP-2/MiniGPT-4/LLaVA-1.5 bases；FT/IKE/SERAC/MEND/KE editing implementations；source images from MMpedia、Google、
  YouTube/Bilibili and prior personalization datasets impose separate provenance/licensing constraints。
- **Access and Verification Status:** v1 full text/appendices、construction/questions、single/sequential results、method hyperparameters与current repo已核验；
  v1 reports2,940 knowledge/8,363 images/175 fine types，current README reports2,940/7,229/110，metadata unresolved。
- **Full-read Coverage:** metadata、triplet benchmark limits、free-form knowledge definition、entity/semantic/user editing、four-stage construction、
  reliability/locality/generalization/portability equations、human check/stats、three LMMs/five editors、single/sequential experiments、case/results/appendices/code。
- **Original Problem:** prior multimodal editing benchmarks mostly changeentity triplets and saturate；real edits may alterappearance, action/gesture/relation or user-specific facts，
  and success must not corrupt unrelated text/image behavior or vanish after subsequent edits。
- **Why the Previous Design Was Reasonable:** `(subject,relation,object)` is easy to generate/score，single edit isolatesmechanism，one reliability metric简洁；
  entity facts、small models or regression smoke tests still benefit from these controls。
- **Changed Constraint:** free-form multimodal facts cross image/text and personalization domains；model updates are persistent state transitions，so same new fact
  must generalize across images/questions, propagate where intended, remain local elsewhere, and survive edit sequences。
- **Mechanism:** constructs visual entity edits by replacing image with same-type entity+counterfactual description，visual semantic edits foractions/gestures/
  object relations/texture/color，user edits forowned/favorite/affiliation facts；for each edit generates text/image reliability、text/image locality、image
  generalization and portability questions，then evaluates single edit and repeated edits while revisiting first edit。
- **State Ownership:** edit request owns target scope/new fact/user；source image/text/license owns evidence；editor ownsparameter/external-memory delta；base/model
  revision ownspre-edit behavior；evaluation suite owns affected/unaffected/generalized/portable slices；sequential ledger ownsorder and first-edit retention。
- **Control Flow / Data Flow:** collect original visual knowledge → generate counterfactual/user edit → human verify images/descriptions/questions → apply editor to
  pinned LMM → evaluate T/I reliability+locality+I-generalization+portability → append next edits → re-evaluate first edit → record rollback/supersession evidence。
- **Implementation Details:** paper v1:2,940 knowledge、8,363 images、175 fine types，train/test counts entity636/955、semantic214/293、user331/511；
  BLIP2-OPT、MiniGPT-4、LLaVA-1.5；FT last LLM layer/alignment module plus IKE/SERAC/MEND/KE；token-level editing accuracy。
- **Evaluation Contract:** T-Loc/I-Loc compare unaffected outputs；T-Rel/I-Rel test edited fact；I-Gen tests alternate images/questions；Port tests related
  consequences；single-edit resets base per item，sequential edit applies1/3/5/6/10 or category-specific updates then tests earliest knowledge。
- **Baselines / Ablations / Sensitivity / Overhead:** three LMMs×six method variants includingFT-LLM/FT-Alignment；no method dominates all axes；SERAC often
  preserves locality but lower reliability/generalization，IKE improves edit uptake atlocality cost；no latency/memory/edit-time/rollback or multi-seed sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/method layers/steps/LRs partly disclosed；GPU、precision、batch/concurrency、
  edit latency、external memory size、serving overhead与SLO为`Not Disclosed`。
- **What the Evidence Actually Proves:** v1 benchmark exposes separable edit properties and sequential degradation that entity-only/single-score tests hide；
  editing parameter/alignment/external memory surfaces trades reliability against locality/generalization/portability differently。
- **What It Does Not Prove:** benchmark metadata denominator correct、free-form facts真实/legally sourced、token-level accuracy代表semantic correctness、
  personalization consent exists、any editor is production safe，or weight editing is preferable toRAG/memory/model update。
- **Limitations / Threats to Validity:** artifact/paper counts conflict；Google/YouTube/Bilibili crawls and synthetic user relations raiselicense/privacy/consent；
  onlyolder3 LMMs、automatic questions with human verification、token-level scorer、no human behavior/safety、counterfactuals may be unnatural，no rollback tests。
- **Trade-offs / New Failure Modes:** weight edit offers low per-query context but hard provenance/delete/rollback；external memory preserves locality but routing may miss；
  sequential updates create interference/order dependence；user-specific edit can leak across tenants；broad portability may become unintended propagation。
- **Where the Previous Design Still Applies:** RAG/external memory for fresh/citable/deletable facts；adapter per tenant for isolation；full retraining for large stable
  domain shifts；triplet benchmark for precise entities；single-edit test for diagnosis。High-risk edits need approval and rollback, not automatic promotion。
- **Evolution Relationship:** `Direct Evolution`：entity triplet/single edit → free-form multimodal edits → multi-axis evaluation → sequential state retention。
  下一阶段应加入provenance、tenant scope、delete/rollback与online side effects，而不是只提高reliability score。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Current Ch66；Legacy Ch62）主 owner；handoff到 `AGENT-MEMORY`、`TRAIN-SFT`、
  `MULTIMODAL-REPRESENTATION`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch66 subject/slices/stateful evaluation、Ch77 external/parametric memory lifecycle、Ch29 update lineage、Ch23
  multimodal identity与Ch72 tenant/security；确认model edit应作为state transition而非Memory shortcut。
- **Existing Coverage:** Books已覆盖derived memory、parameter consolidation、source authority、delete/rollback与evaluation slices；可refine为明确的
  edit evidence matrix：reliability≠locality≠generalization≠portability，sequential retention另算。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Artifact Metadata Inconsistent`；不得保留冲突dataset totals。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，artifact denominator conflict未自行裁决。
- **Open Questions:** 8,363/7,229 and175/110 provenance、event-time commit、source licenses/consent、semantic scorer、tenant isolation、edit identity/
  rollback/delete、long edit streams、newerLMMs、latency/memory/SLO与independent reproduction。

### FSPO: Population Alignment Loses the User; Meta-Learning Makes Preference Context an Input

- **Candidate / Week / Score:** FSPO: Few-Shot Preference Optimization of Synthetic Preference Data in LLMs Elicits Effective Personalization to Real Users / 2025-W09 / 27/30。
- **Source Family ID:** `fspo-user-conditioned-preference-meta-learning`。
- **Source Type:** arXiv v1 + public code/data/protocol + preliminary human study；synthetic-to-real personalization experiment。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-26；v2 2026-04-16 changes title to`Few-Shot Optimization of
  Synthetic Preferences Personalizes to Real Users`。W09锁定v1 method/data/results。
- **Direct Primary Sources:** https://arxiv.org/html/2502.19312v1；https://arxiv.org/abs/2502.19312；
  https://github.com/Asap7772/fewshot-preference-optimization；https://fewshot-preference-optimization.github.io/。
- **Related Primary Sources:** open Roleplay/Review/ELIX datasets and protocols；DPO/IPO codebase、Prolific human study、AlpacaEval-derived judge；
  later v2/current project page only for lineage。
- **Access and Verification Status:** v1 full text/appendix、meta-objective、synthetic construction、three domains、all baselines/synthetic/human results、
  limitations/ethics/hyperparameters/artifact statement与current code已核验；repo只有5 commits、无immutable W09 release。
- **Full-read Coverage:** metadata、preference/RM background、FSPO algorithm/equations、user-description CoT、Review/ELIX/Roleplay tasks、>1M synthetic
  preferences、diversity/coherence/underspecification pipeline、Sim2Real、4/8-shot baselines、1500 synthetic users、25-user study、risks/training/artifacts。
- **Original Problem:** RLHF/DPO把不同人的pairs聚合为population preference，hidden user context被边缘化；给新用户只有少量labels时，per-user
  fine-tuning昂贵，pure prompt又未经过“如何从几条偏好推断reward function”的跨用户训练。
- **Why the Previous Design Was Reasonable:** population alignment稳定、资产少且避免过拟合个人；prompt/profile memory可快速切换；per-user adapter在
  稳定高流量用户上易隔离。用户差异小、风险高或数据极少时这些旧分支仍更可控。
- **Changed Constraint:** assistants/content systems需快速适应new user且真实preference data稀缺；系统必须从few labeled comparisons推断latent context，
  同时区分用户identity、label examples、derived description、policy weights与global safety policy。
- **Mechanism:** 将每个user视为meta-task：训练时抽该用户few-shot preference subset作为context，用剩余held-out pair计算IPO/implicit-reward loss并
  更新shared policy；inference时把new user few-shot examples并入prompt。可选User Description CoT先从examples生成persona description，再与query/
  examples共同生成response；training两阶段Few-shot Pref-FT→Few-shot IPO。
- **State Ownership:** user/consent domain拥有raw labels；few-shot sampler拥有support/query split；synthetic generator拥有persona/preference provenance；
  shared FSPO checkpoint拥有adaptation prior；runtime context拥有current labels/derived description；global policy/safety owner可覆盖personal preference；
  delete/expiry must propagate to caches/derived profiles。
- **Control Flow / Data Flow:** consented/synthetic user definitions → generate/label preference pairs → enforcecross-user diversity + within-user coherence →
  sample support/heldout per user → Pref-FT/IPO meta-training → new user gives4/8 labels → optional derived description → personalized response →
  user/judge eval → update, forget or revoke user state。
- **Implementation Details:** Llama3.2-3B-Instruct；4/8 shots；Pref-FT LR1e-7、IPO LR1e-6、IPO beta0.005 recommended，1 epoch each stage；
  1 node×8 A100 about8h/experiment withFSDP、~4000 aggregate GPU-hours；FlashAttention for longer prompts；SGLang/vLLM for synthesis/inference。
- **Evaluation Contract:** three domains：Review(sentiment×verbosity)、ELIX(education-background responses)、Roleplay(open QA)；trained/interpolated/held-out
  users/questions；baselines base、few-shot prompting、Pref-FT、oracle user description；GPT-4o personalized judge plus25 Prolific users×11 held-out questions。
- **Baselines / Ablations / Sensitivity / Overhead:** synthetic diversity/coherence and description CoT designs、4/8 shots、trained/interpolated users、
  length(~250 words)/format/view normalization；no production longitudinal study、no deletion/adversarial preference/safety override or full cost-per-user comparison。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 8×A100/8h per experiment and ~4000 GPU-hours disclosed；3B model/128K nominal
  context，no sequence parallelism；precision、batch, actual context lengths、online concurrency/latency/KV cost与SLO未完整披露。
- **What the Evidence Actually Proves:** 在作者synthetic tasks及25-user controlled study中，training shared model to interpret preference examples as
  task context can outperform unconditioned/few-shot/SFT baselines；synthetic user diversity+coherence影响Sim2Real transfer。
- **What It Does Not Prove:** derived persona真实/完整、71–72% winrate跨population/tasks稳定、synthetic preferences无stereotype、FSPO respects safety/
  privacy/delete、larger models/context更好，或user labels应永久写入weights。
- **Limitations / Threats to Validity:** preliminary25-user/controlled questions、English-only、3B model、GPT-4o judge、synthetic generator/judge shared biases、
  format/view normalization、demographic axes可能固化stereotypes、dataset含Qwen Chinese artifacts、echo chamber/harmful-view amplification、no long-term drift。
- **Trade-offs / New Failure Modes:** shared meta-policy avoids per-user checkpoint explosion but keepspreferences inlong prompt and spreads synthetic bias globally；
  explicit derived profile可诊断却会overgeneralize sensitive traits；few-shot labels易被poison/ambiguous；personalization可冲突global policy、tenant isolation和right-to-delete。
- **Where the Previous Design Still Applies:** no personalization for safety/neutrality；explicit editable profile/memory for transparency/delete；RAG for factual interests；
  per-user adapter for stable high-volume tenants；human approval for high-risk recommendations。FSPO只是一条conditional branch。
- **Evolution Relationship:** `Direct Evolution`：population-level preference aggregation → explicit user profile/few-shot prompt → meta-learned interpretation of
  preference context → bounded personalized policy。下一阶段压力是consent、scope、safety override、expiry/delete与online calibration。
- **ROADMAP Node:** `TRAIN-DPO`（Current Ch34；Legacy Ch30）主 owner；handoff到 `TRAIN-DATA`、`AGENT-MEMORY`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch31 population reward、Ch34 pair objective/offline bias、Ch27 synthetic/consent lineage、Ch77 user memory/
  parameter consolidation、Ch66 human/judge evaluation及Ch72 policy/security；确认user context是objective input而非普通pair metadata。
- **Existing Coverage:** Ch34已有pair/reference/objective，Ch77已有external vs parametric personalization与delete/rollback；FSPO可refine“population pair aggregation
  hides user context，meta-learning把support preferences变成versioned inference input”，并保留global-policy boundary。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；不保留headline winrates或synthetic persona examples。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，2026 v2 title/results未覆盖W09 v1。
- **Open Questions:** immutable event-time dataset/code、preference consent/delete、poisoning/ambiguity、sensitive-attribute inference、policy override、longitudinal
  drift/feedback loops、larger models、latency/KV cost、judge-human calibration与independent reproduction。

### AISafetyLab v1: A Common Interface Enables Matched Attack–Defense Experiments, Not a Universal Safety Score

- **Candidate / Week / Score:** AISafetyLab: A Comprehensive Framework for AI Safety Evaluation and Improvement / 2025-W09 / 26/30。
- **Source Family ID:** `aisafetylab-attack-defense-evaluation-framework`。
- **Source Type:** arXiv v1 technical report + MIT-licensed continuously maintained toolkit；framework release and paper are separate event nodes。
- **Event Date / First-public Date / Revision History:** official framework open-sourced2024-12-31（W01 spillback）；technical report v1
  2025-02-24（W09），唯一paper version。Current repository has95 commits and expanded dependencies/methods，not v1 behavior。
- **Direct Primary Sources:** https://arxiv.org/html/2502.16776v1；https://arxiv.org/abs/2502.16776；
  https://github.com/thu-coai/AISafetyLab。
- **Related Primary Sources:** HarmBench subset、Vicuna-7B-v1.5、LlamaGuard3 scorer and implemented attack/defense papers；each method’s official source remains
  authoritative for algorithm semantics，AISafetyLab adapter is an integration artifact。
- **Access and Verification Status:** v1 full text/appendices、framework interfaces、13 attacks/16 defenses/scorers、50-query experiment and current repo/docs已核验；
  no immutable 2024-12-31 or W09 release/tag，current setup version0.1/dependency range can drift。
- **Full-read Coverage:** metadata、safety evaluation/improvement/toolkits、attack access classes and mutate/select/feedback design、inference/training defenses、
  scorer/model/dataset/logging interfaces、usage、Vicuna attack×defense matrix、overrefusal/scorer inconsistency、all method implementation appendices/conclusion。
- **Original Problem:** safety research tools implement attacks、defenses and scorers with incompatible model/dataset/config/result shapes，making matched comparison、
  reproduction and method composition costly；isolated ASR headline hides overrefusal and scorer semantics。
- **Why the Previous Design Was Reasonable:** method-specific repository best preservesauthor intent and latest features；single attack/defense experiment has fewer
  abstraction losses。Small scope、highly specialized threat or official reproduction仍应优先原实现。
- **Changed Constraint:** systematic red-team needs matrix acrosswhite/gray/black-box access、pre/mid/post-generation and training-time defenses，shared dataset/
  target/scorer/logging identity；without typed adapters，differences in harness can masquerade asmethod performance。
- **Mechanism:** three core modules：Attack managers decomposeinit→mutate→select→feedback；Defense composespreprocess→generation guidance→postprocess plus
  safety tuning/RLHF/unlearning；Evaluation exposes common`score(query,response)` across fine-tuned/prompt scorers and OverRefuseScorer；Models/Dataset/
  Utils/Logging normalize local/API calls、Example state and result persistence。
- **State Ownership:** threat model owns attacker access/budget；attack adapter owns mutation/selection/stop；defense pipeline owns stage/order/config；target model/
  template ownsbehavior；dataset owns harmful/benign population；scorer owns taxonomy/threshold；run owns all revisions/seeds/results；deployment gate remains external。
- **Control Flow / Data Flow:** pin target+template+dataset → instantiate attack(access/budget) → generate adversarial queries → run ordered defenses/model →
  collect response/trace → score harmfulness + overrefusal → aggregate per attack/defense slice → inspect failures/disagreement → release/reject/repair adapter。
- **Implementation Details:** v1 implements13 attacks（1 white/3 gray/9 black）、13 inference defenses across three stages、3 training defenses；localHF and
  OpenAI-compatible API models、retry handling、Example dataset/loguru logging。Current repo adds methods/deps beyondv1 and cannot be treated as same artifact。
- **Evaluation Contract:** Vicuna-7B-v1.5 target、50 HarmBench harmful instructions、13 attacks×original/16 defenses，LlamaGuard-3-8B scorer；report attack
  success rate andoverrefusal. Training-defense data controlled~1K samples；paper acknowledges fictional/repetitive outputs create scorer unfairness。
- **Baselines / Ablations / Sensitivity / Overhead:** attack/defense cross-matrix and no-defense baseline；not a controlled algorithm ablation，因为methods have
  differentquery budgets/access/compute/training data。No seeds/confidence intervals、benign utility suite、latency/cost/memory or scorer-human calibration。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** target/scorer and 50-query set disclosed；hardware、precision、attack query budgets in
  unified table、batch/concurrency、latency/cost andproduction SLO mostly`Not Disclosed`。
- **What the Evidence Actually Proves:** shared interfaces make a reproducible experiment matrix possible and reveal attack effectiveness depends on defense；lowASR
  can coincide with severe overrefusal，and a single scorer can misclassify fictional/repetitive outputs。
- **What It Does Not Prove:** framework adapters are semantically identical toofficial methods、LlamaGuard verdict is ground truth、best defense generalizes to
  othermodels/attacks、composing defenses monotonically improves safety、or toolkit version0.1 is production-ready。
- **Limitations / Threats to Validity:** one weak target、50 harmful prompts、model scorer、unmatched budgets、no benign task quality except overrefusal proxy、
  no multimodal/agent safety in v1、dependency/current-main drift、toolkit can operationalize harmful attacks and requires access control/log retention。
- **Trade-offs / New Failure Modes:** common interface reduces integration cost but may flatten method-specific preconditions；continuous updates improve coverage while
  breaking longitudinal comparability；attack toolkit enables research and misuse；defense composition adds order conflicts/latency；scorer swap changes verdict history。
- **Where the Previous Design Still Applies:** official method repo for faithful reproduction；narrow deterministic policies for known threats；human/expert review for
  ambiguous harm；production safety requires telemetry、canary、incident response and domain threat models beyond offline jailbreak matrix。
- **Evolution Relationship:** `Layering / Dependency`：isolated attack repos → common adapters → matched attack×defense×scorer runs → versioned safety evidence →
  external release gate。Framework does not own safety truth。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Current Ch72；Legacy Ch68）主 owner；handoff到 `PLATFORM-EVALUATION-SYSTEM`、
  `TRAIN-RLHF`与`PLATFORM-PRODUCTION`。
- **Target and Adjacent Chapters Read:** 已读Ch72 threat model/defense-in-depth/red-team/release，Ch66 subject/dataset/scorer/run，Ch31 safety alignment and
  Ch73 production gate；现有Books已明确工具不定义安全目标、ASR≠deployment safety。
- **Existing Coverage:** Security/Evaluation正文已覆盖threat model、attack budget、scorer identity、overrefusal、offline→release gates；AISafetyLab提供
  implementation case but没有新的长期机制缺口。
- **Integration Decision:** `Books Pending — No Change Candidate / Code Event Spillback W01`。W01需补official open-source event，W09保留paper evidence。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，current95-commit framework未倒写v1 capability。
- **Open Questions:** immutable2024-12-31/W09 commits、adapter semantic equivalence、attack budgets/seeds、benign utility、scorer-human calibration、
  multimodal/agent safety、defense-order semantics、sandbox/access control、cost/SLO andlongitudinal versioning。

### PosterSum: High-Resolution Multimodal Documents Need Hierarchical Evidence Compression

- **Candidate / Week / Score:** PosterSum: A Multimodal Benchmark for Scientific Poster Summarization / 2025-W09 / 24/30。
- **Source Family ID:** `postersum-hierarchical-multimodal-document-summary`。
- **Source Type:** arXiv v1 + public 16,305-pair dataset + repository placeholder；benchmark and frozen-model hierarchical pipeline study。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-24，唯一version；dataset current main has7 commits；official GitHub仍写
  `Code coming soon`，therefore paper pseudocode/config is not full executable artifact。
- **Direct Primary Sources:** https://arxiv.org/html/2502.17540v1；https://arxiv.org/abs/2502.17540；
  https://huggingface.co/datasets/rohitsaxena/PosterSum；https://github.com/saxenarohit/postersum。
- **Related Primary Sources:** ICLR/ICML/NeurIPS poster/abstract sources and permissions；SAM、MiniCPM-Llama3-V2.5、Llama3.1-8B dependencies；later
  IJCNLP publication only lineage。
- **Access and Verification Status:** v1 full text/appendix、dataset card/splits、all baselines/metrics/ablation/limitations and repo status已核验；dataset public，
  generation/Segment&Summarize code unavailable in official repo。
- **Full-read Coverage:** metadata、related multimodal/scientific/layout work、conference collection、16,305 stats/topic labels、OCR/closed/open/CoT/LoRA baselines、
  SAM segmentation+k-means/local/global pipeline、automatic/factuality metrics、cluster/local-model ablations、hardware/model versions、ethics/limitations/examples。
- **Original Problem:** scientific posters arehigh-resolution layouts containing dense text、figures、tables、equations and cross-region references；global resize/
  one-shot MLLM loses small evidence，OCR-only loses visual semantics，yet final abstract requires coherent document-level synthesis。
- **Why the Previous Design Was Reasonable:** direct whole-image MLLM preserves global layout and minimal orchestration；OCR→text summarizer is cheap/auditable；
  paper abstract is available supervision。Simple/low-resolution posters or latency-sensitive use still favor these branches。
- **Changed Constraint:** mean3547×2454 poster exceeds model visual budget；sections are spatially separable but not fully independent，so system must allocate local
  perception budget then compress evidence before global synthesis，while preservingregion identity and redundancy/conflict handling。
- **Mechanism:** SAM proposesregions，region features arek-means clustered into`k=8` coherent groups；frozen local MLLM summarizes eachcluster’s text/
  figures/tables，then frozen text LLM synthesizes all local summaries into global abstract。This is hierarchical evidence compression，not parameter training；LoRA baselines separate branch。
- **State Ownership:** sourceposter/image URL/permission owns evidence；segmenter owns masks；cluster policy owns grouping/k；local summaries arederived provisional evidence；
  global summarizer owns prose composition；abstract is reference target but notposter truth；dataset/model/prompt/scorer versions ownEvalRun identity。
- **Control Flow / Data Flow:** conference poster+paper abstract → permission/source metadata → image normalization → SAM segments → cluster/dedup regions →
  local multimodal summaries → global text synthesis → compare with abstract/factuality proxies → human/automatic verify before release。
- **Implementation Details:** 16,305 pairs/137 GPT-4o-generated topics/year2022–24，split10,305/3,000/3,000，meanabstract224 tokens；k=8 chosen on100-val
  subset；MiniCPM local +Llama3.1-8B global；max768 output tokens；LoRA rank8/alpha8/dropout0.1、10 epochs/batch4；2×A10080GB for training。
- **Evaluation Contract:** OCR(Pytesseract/MMOCR)+Llama baseline，closed GPT-4o-2024-08-06/Gemini2.0-Flash-exp/Claude3.5-20241022，openMLLM zero/CoT，
  LoRA models and hierarchical pipeline；ROUGE/BERTScore/SacreBLEU/METEOR plus SummaC/FActScore against paper abstract，not source-grounded expert verdict。
- **Baselines / Ablations / Sensitivity / Overhead:** with/without clustering(top8 largest segments)、swap local MLLM、k=2..10、CoT andLoRA；no segmentation
  oracle、reading-order/cross-reference ablation、human domain evaluation、latency/token/cost or multiple seeds。Paper notes factuality metrics fail onscientific text。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 2×A10080GB for fine-tuning，batch4/10epochs/max768 outputs；precision、inference
  concurrency、per-poster local calls/tokens、TTFT/latency/cost andproduction SLO为`Not Disclosed`。
- **What the Evidence Actually Proves:** in this ML-poster/abstract dataset，hierarchical region decomposition improves automatic summary similarity over one-shot
  baselines and is robust to one alternate local model；high-resolution document understanding benefits from local/global budget separation。
- **What It Does Not Prove:** generated summaries factually matchposters、abstract is complete/correct ground truth、k=8 generalizes、SAM segments semantic sections、
  CoT reveals reasoning、method beats experts，or pipeline applies to other scientific domains/layouts。
- **Limitations / Threats to Validity:** only ML conferences2022–24、poster may differ frompaper abstract、GPT-4o topic bias、random split may shareauthors/templates/topics、
  automatic overlap metrics dominate、scientific factuality proxies poor、code missing、image URLs may drift、segmentation fragments cross-references。
- **Trade-offs / New Failure Modes:** hierarchy restoresdetail but multipliescalls/latency and losescross-region relations；local summaries can hallucinate then be amplified globally；clustering reduces
  redundancy but may merge unrelatedregions；OCR remains better for exact text；source permissions do not automatically grant downstream model-output rights。
- **Where the Previous Design Still Applies:** OCR+source citations for exactfacts；whole-image MLLM for simple layouts；paper full-text RAG for authoritative detail；
  human/domain expert review for scientific release；layout-aware model training for high-volume stable corpus。
- **Evolution Relationship:** `Principle Reuse`：flat whole document → layout-aware segments → local evidence summaries → global synthesis。Same asRAG chunk/
  parent-child aggregation，with vision-specific segmentation andcross-region failure modes。
- **ROADMAP Node:** `AGENT-RAG`（Current Ch76；Legacy Ch72）主 owner；handoff到 `MULTIMODAL-REPRESENTATION`、
  `AGENT-WORKFLOW`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch76 ingestion/chunking/multimodal operators/sufficiency，Ch23 coordinate/provenance，Ch81 artifact workflow and
  Ch66 scientific evidence/claim metrics；现有主线已覆盖hierarchical evidence compression与source authority。
- **Existing Coverage:** RAG已说明parser/chunk/parent-child、multimodal-native operators、local evidence≠truth；Evaluation已覆盖scientific artifact and
  claim provenance。PosterSum提供受限案例，没有新的长期机制缺口。
- **Integration Decision:** `Books Pending — No Change Candidate`；benchmark metrics/model rankings留Weekly。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，official repo code absence已记录。
- **Open Questions:** event-time dataset/repo hashes、poster permissions/URL retention、author/template leakage、semantic segmentation/reading order、source-grounded
  factuality、human expert eval、latency/cost、code release andcross-domain reproduction。

### Beyond Next-Token / xAR: Prediction Unit Is a Factorization Choice, Not a Universal Token

- **Candidate / Week / Score:** Beyond Next-Token: Next-X Prediction for Autoregressive Visual Generation / 2025-W09 / 28/30。
- **Source Family ID:** `xar-next-x-continuous-visual-autoregression`。
- **Source Type:** arXiv v1 + official implementation/checkpoints + ICCV 2025 lineage；experimental image-generation architecture。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-27，当前仅一个arXiv version；后续ICCV acceptance与
  current repository不倒写W09 artifact availability。
- **Direct Primary Sources:** https://arxiv.org/html/2502.20388v1；https://arxiv.org/abs/2502.20388；
  https://github.com/OliverRensu/xAR；https://oliverrensu.github.io/project/xAR。
- **Related Primary Sources:** official pretrained weights and ImageNet evaluation scripts；VAE/MAR/VAR/DiT/SiT/REPA official papers作为
  representation/factorization baselines，不以二手排行榜替代原实验。
- **Access and Verification Status:** v1正文、Method/equations/pseudocode、main/ablation/speed tables、hyperparameters、limitations和current
  five-commit repository已核验；无immutable W09 release/tag，current code/checkpoints属于later artifact lineage。
- **Full-read Coverage:** metadata、AR vision/flow-matching related work、next-X construction、Noisy Context Learning、SDE inference、ImageNet-256/512、
  entity/cell/noise ablations、training/evaluation hyperparameters、single-A100 sampling table、limitations和official train/eval commands。
- **Original Problem:** 语言token拥有相对自然的离散语义单位，图像patch却可能只包含对象碎片；把二维latent机械展平成单patch序列既增加
  autoregressive steps，也让teacher forcing只看到perfect history，inference时自生成误差会累积。
- **Why the Previous Design Was Reasonable:** single-token AR拥有清楚的causal factorization、exact prefix state与成熟sampling/cache语义；整图
  diffusion/flow则允许全局并行修正。文本、严格streaming或需要可审计commit顺序时，token AR仍然是合理基线。
- **Changed Constraint:** visual latent的空间结构、局部语义密度与允许整幅图最终提交的contract不同于文本；系统需要在prediction-step数量、
  单步entity维度、局部条件和error recovery之间选择新的factorization。
- **Mechanism:** 将连续VAE latent划分为可变entity X：single patch、spatial cell、non-local subsample、coarse-to-fine scale或entire image；每个
  AR step不做离散classification，而以flow-matching velocity regression从Gaussian noise生成当前entity。NCL训练时为历史entities独立采样noise
  level，使模型学习在imperfect context下预测；inference仍按entity顺序生成clean estimates。
- **State Ownership:** VAE/tokenizer revision拥有continuous latent geometry；entity policy拥有shape/order/granularity；flow sampler拥有当前noise/time
  state；AR runtime拥有已生成entity history；classifier-free guidance与SDE steps拥有quality/cost operating point；最终decoder拥有pixel commit。
- **Control Flow / Data Flow:** image → frozen VAE latent → choose entity partition/order → sample per-entity noise/time → causal Transformer predicts
  flow velocity under noisy prior entities → integrate current entity → append provisional clean entity → repeat → VAE decode → final image commit/evaluate。
- **Implementation Details:** default16×16 latent fromstride-16 VAE，8×8 contiguous cells形成2×2 entity grid；172M/608M/1.1B variants，AdamW、
  batch2048、800 epochs、100 warmup、cosine LR 4e-4→1e-5、dropout0.1、SDE sampling50 steps。Official xAR-H command uses8 nodes×8 GPUs；
  repo warns mixed precision may NaN and suggests TF32 fallback。
- **Evaluation Contract:** class-conditional ImageNet-1K at256/512；FID、IS、precision、recall；50K-image evaluation with CFG。Main comparison spans
  GAN/diffusion/flow/masked/AR families；single-A100 samples/sec table uses official codebases but does not disclose end-to-end service SLO。
- **Baselines / Ablations / Sensitivity / Overhead:** token/cell/subsample/scale/whole-image X、cell k=1/2/4/8/16、clean/increasing/decreasing/random
  noisy context、model scale and sampling steps；no dynamic entity policy、human semantic evaluation、OOD dataset、text-conditioned generation、multiple seeds/
  confidence intervals or serving concurrency study。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** training topology8×8 GPUs and global batch2048 implied by official command；GPU model、
  training precision/time not disclosed。Sampling throughput measured single A100, 256² images, 40/50 vs250/256 steps；online batch/concurrency、latency
  distribution、memory、cost和SLO为`Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者ImageNet contract中，prediction entity是可优化design variable；moderate contiguous cells优于同模型的
  token/scale/whole-image variants，random noisy-history training优于clean-history ablation，且当前实现展示了较少sampling steps下的quality/throughput点。
- **What It Does Not Prove:** 8×8 cell普遍最优、NCL消除所有exposure bias、flow-regression AR保持离散AR distribution、作者speed比在生产batch成立、
  ImageNet FID代表text-to-image/world-model能力，或visual factorization可直接迁移到language/action。
- **Limitations / Threats to Validity:** 单一curated classification dataset与两种resolution；entity geometry固定、dynamic semantic regions未研究；
  FID/IS有限、无human/OOD evaluation；baselines的model size/training/sampler不同；event-time code不可锁定；mixed-precision NaN提示数值稳定性风险。
- **Trade-offs / New Failure Modes:** 大entity减少AR steps并提高单步语义密度，却增加每步regression维度、flow work与entity内部不可见dependency；
  noisy context提高error tolerance但形成training/inference noise mismatch；固定grid会切断对象；continuous provisional state使cache、rollback和streaming
  commit比token AR更复杂。
- **Where the Previous Design Still Applies:** exact textual prefix、tool/action commit与低延迟streaming继续使用token AR；整图diffusion/flow适合允许
  global revision的quality-first image task；small cells适合局部可控性；静态entity policy在batch/graph capture和简单artifact中更可预测。
- **Evolution Relationship:** `Direct Evolution` + `Alternative Branch`：pixel/patch AR → learned discrete visual tokens → scale/subsample AR →
  flexible continuous entity AR with noisy history；与whole-image flow是同一factorization spectrum，不是AR单向取代diffusion。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Current Ch24；Legacy N/A）主 owner；handoff到
  `MULTIMODAL-REPRESENTATION`、`MODEL-SAMPLING`、`INFER-SPECULATIVE-DECODING`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch23 representation/token identity、Ch24 AR/diffusion/block/mutable commit、Ch20 sampling与Ch48
  proposal/verify；现有正文有factorization和commit boundary，但缺少“prediction entity粒度本身是AR设计轴”的完整桥梁。
- **Existing Coverage:** Ch24已覆盖AR、flow、block/masked refinement和draft/correct contract；xAR可refine token→scale/block/entity演进，并说明
  visual entity grouping改变序列factorization而非只换tokenizer，保留作者结果的ImageNet边界。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；只沉淀entity granularity、noisy-history contract与commit trade-off，
  不保留SOTA/FID headline或推断production speed。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，later ICCV/code/checkpoint作为artifact lineage单列。
- **Open Questions:** event-time code hash、dynamic/semantic entities、entity order、NCL与actual self-generated error distribution、text conditioning、
  OOD/human evaluation、training precision/stability、memory/concurrency、cache identity、rollback/streaming及independent reproduction。

### LongRoPE2: Context Extension Requires Position Calibration and Dual-Window Training Contracts

- **Candidate / Week / Score:** LongRoPE2: Near-Lossless LLM Context Window Scaling / 2025-W09 / 28/30。
- **Source Family ID:** `longrope2-critical-dimension-mixed-window-training`。
- **Source Type:** arXiv v1 + Microsoft official evolution-search artifact；experimental context-extension method。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-27，当前仅一个paper version；LongRoPE 2024是related predecessor，
  LongRoPE2是同repository的新paper node，不能把LongRoPE的2M claim或Phi integration当作本论文结果。
- **Direct Primary Sources:** https://arxiv.org/html/2502.20082v1；https://arxiv.org/abs/2502.20082；
  https://github.com/microsoft/LongRoPE。
- **Related Primary Sources:** LongRoPE predecessor、YaRN/NTK baselines、RULER/LOFT/InfiniteBench/LongBench、RedPajama/StarCoder/FineWeb-Edu data；
  official repo明确因policy restriction只公开evolution-search部分。
- **Access and Verification Status:** v1全文、RoPE theory/hypothesis、two algorithms、mixed-window mechanism、setup/main/ablation/appendix和current
  official repo已核验；training pipeline/weights未完整公开且无immutable W09 tag，artifact completeness受限。
- **Full-read Coverage:** metadata、position-extension related work、theoretical/practical critical dimension、needle-PPL search、mixed original/rescaled RoPE
  training、10B-token mix、64-A100 setup、short/long benchmarks、critical-dimension/metric/mixed-window ablations、appendix and repository boundary。
- **Original Problem:** RoPE在数学上可计算更远位置不等于模型在训练中学会这些frequency dimensions；统一rescaling可能仍在目标长度失效，
  同时破坏原短窗能力。仅声明accepted length因此不能证明effective context。
- **Why the Previous Design Was Reasonable:** uniform/analytic PI、NTK或YaRN简单、无需逐模型搜索，progressive long training用数据适配新位置；
  若只服务单一长窗、模型/预算足够或短窗能力不敏感，这些方案仍较易复现和运维。
- **Changed Constraint:** deployment需要同一checkpoint同时保留short-task quality和128K retrieval/composition，且不能用数百B tokens反复扩窗；
  calibration必须承认不同RoPE dimensions的effective training exposure不等于理论period。
- **Mechanism:** 根据pretraining window内rotation coverage提出real critical dimension早于theoretical boundary；用synthetic long document中的needle-answer
  token PPL作为evolution-search fitness，搜索高维non-uniform scale factors，低维用NTK-aware scaling。Mid-training时短样本使用original RoPE并以mask隔离
  packed documents，长样本使用rescaled RoPE；inference按input length选择两套position contract。
- **State Ownership:** base checkpoint拥有原RoPE/short behavior；search artifact拥有model+target-length-specific scale vector与critical dimension；
  dataset packer/mask拥有document boundaries；mid-training run拥有dual-window objective；runtime router拥有length→RoPE choice；KV/prefix cache identity必须
  包含RoPE mode、scale vector和model revision。
- **Control Flow / Data Flow:** pin base model/train length/target length → synthesize needle documents → initialize/mutate monotonic scale vectors → evaluate
  needle-token PPL → select real critical dimension/scales → mix short(original RoPE, packed mask) and long(rescaled RoPE) batches → mid-train weights → evaluate
  accepted/effective/short capability separately → runtime selects position mode before Prefill。
- **Implementation Details:** Phi3-mini-3.8B and LLaMA3-8B extended to128K；64×A100，10B long/mid-training tokens plus1B FineWeb-Edu short
  tokens，1 epoch/global batch64/LR2e-5 cosine；long sources4.5B RedPajama-v1、2.5B v2、2B StarCoder，length8K–200K chunked128K。
  Search uses monotonic high-dimension mutations andneedle-PPL；repo releases evolution/search/evaluation only。
- **Evaluation Contract:** long stress testsRULER/Needle，real tasksLOFT/InfiniteBench/LongBench，short taskswithin4096；baselinesYaRN/NTK/LongRoPE
  share the same mid-training procedure。Claims apply to two base models、128K target and disclosed data/training contract。
- **Baselines / Ablations / Sensitivity / Overhead:** theoretical vs real critical dimension、PG19 full-token PPL vs needle-token PPL、with/without mixed-window
  training；no search-seed variance、search compute/cost、routing threshold sensitivity、other RoPE bases/model families、multi-million target or production cache/latency study。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 64×A100、3.8B/8B、128K、global batch64、10B+1B tokens disclosed；
  precision、optimizer states/parallelism、wall time、search GPU-hours、inference batch/concurrency、TTFT/TPOT/KV memory/cost/SLO为`Not Disclosed`。
- **What the Evidence Actually Proves:** 在两模型matched mid-training中，model-specific searched scaling、needle-sensitive objective与dual-window training
  分别改善作者的long retrieval/benchmarks和short-task retention；accepted 128K与effective behavior需要分别测量。
- **What It Does Not Prove:** 高RoPE维度不足训练是唯一因果、needle-PPL充分代表multi-document reasoning、98% retention跨任务稳定、10B recipe适用于
  任意checkpoint/target、million-token extension成立、或position scaling降低dense Attention/KV的compute/memory成本。
- **Limitations / Threats to Validity:** 仅两种sub-10B base models和128K；训练pipeline/weights不完整公开；synthetic needle可能引导过拟合retrieval；
  baseline implementation与authors’ search budget存在差异；短/长task averages掩盖slice failures；no independent reproduction or end-to-end serving evidence。
- **Trade-offs / New Failure Modes:** search降低uniform scaling bias却新增per-model/per-target calibration artifact与compute；dual RoPE保留short能力却形成
  runtime mode boundary、cache fragmentation和threshold discontinuity；long mid-training仍昂贵并可能改变其他能力；更长accepted length继续放大Prefill/KV成本。
- **Where the Previous Design Still Applies:** native long-context pretraining适合有足够数据/compute的新模型；uniform scaling适合快速实验；RAG/external memory
  适合证据可索引且不愿承担full-window cost；sparse/linear Attention解决compute/state轴，不能由RoPE calibration替代。
- **Evolution Relationship:** `Direct Evolution`：uniform analytical scaling → non-uniform searched LongRoPE → real-critical-dimension + needle-guided scaling →
  mixed original/rescaled window training。它与sparse Attention、RAG是`Layering / Dependency`，不构成替代。
- **ROADMAP Node:** `MODEL-LONG-CONTEXT`（Current Ch22；Legacy Ch22）主 owner；handoff到`MODEL-POSITION-ENCODING`、
  `TRAIN-PRETRAINING`、`INFER-KV-CACHE`、`INFER-PREFILL-DECODE`与`AGENT-RAG`。
- **Target and Adjacent Chapters Read:** 已读Ch13 position encoding、Ch22 accepted/positional/effective/system四层能力、Ch28 mid-training、Ch43 Prefill/
  Decode与Ch45 KV；确认LongRoPE2只移动position/training瓶颈，不解决dense compute或online capacity。
- **Existing Coverage:** Ch22已有“position function defined ≠ reliable behavior”、position scaling与训练分布、effective utilization边界；本family可refine
  theory→empirical calibration→dual-window runtime contract以及cache identity/failure mode，而非新增headline length。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；只沉淀calibration artifact、mixed-window/coexistence和system handoff，
  不保留作者“near-lossless/80×”为通用事实。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，LongRoPE predecessor和current repo capability未合并成W09 result。
- **Open Questions:** full training artifact/weights、immutable W09 commit、search cost/seeds、other model/RoPE bases/targets、routing threshold、
  cache identity/migration、TTFT/TPOT/goodput、long-composition calibration、independent reproduction及million-token evidence。

### ArtGS: An Interactable Replica Needs Canonical State, Part Identity and Motion—not Only a Good Render

- **Candidate / Week / Score:** Building Interactable Replicas of Complex Articulated Objects via Gaussian Splatting / 2025-W09 / 24/30。
- **Source Family ID:** `artgs-canonical-gaussian-articulated-replica`。
- **Source Type:** arXiv v1 + ICLR 2025 project/demo artifact + synthetic/real multi-view RGB-D reconstruction study。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-26，current metadata only one version；later ICLR publication/project
  demo provides lineage but no public code repository or immutable W09 artifact。
- **Direct Primary Sources:** https://arxiv.org/html/2502.19459v1；https://arxiv.org/abs/2502.19459；
  https://articulate-gs.github.io/。
- **Related Primary Sources:** PARIS/DTA baselines、PartNet-Mobility/MultiScan data、3D Gaussian Splatting/TSDF/Open3D and IsaacSim demo；
  project videos/meshes demonstrate outputs but do not substitute executable code。
- **Access and Verification Status:** v1全文、all equations/stages、datasets/metrics、10/3-trial results、five ablations、implementation appendix、
  limitations/failure cases and project demo已核验；paper says public project，but no source code/immutable model artifact可审计。
- **Full-read Coverage:** metadata、dynamic/articulation related work、Gaussian/mesh preliminaries、two-state canonical mapping、coarse-to-fine matching、
  center-based part assignment、joint-type/self-guided optimization、PARIS/DTA-Multi/ArtGS-Multi、hardware/time、ablation、visibility、randomness、limited states、
  TSDF fidelity and failure cases。
- **Original Problem:** 单一object state只能看到部分geometry；分别重建各state会丢失part identity，先分割再估joint又让geometry error传播。
  多part日常物体需要把跨state observation对齐为同一canonical object，同时恢复piecewise geometry与可控制articulation。
- **Why the Previous Design Was Reasonable:** state-by-state NeRF/mesh重建简单且每个state可独立优化；pretrained segmentation/correspondence先验能减少
  per-object搜索；已知CAD/physics model提供强约束。少part、visibility高或已有reliable kinematic prior时这些路径仍更稳。
- **Changed Constraint:** unknown objects有3–6 movable parts、occlusion和sensor noise；replica必须接受joint state并生成一致geometry，而非只在observed
  view渲染逼真，因此canonical state、part assignment和motion parameter必须联合拥有同一identity。
- **Mechanism:** 分别训练两个state的Gaussians，downsample到5K并Hungarian-match取mid-state canonical initialization；用跨state Chamfer motion
  区分static/dynamic并补充static Gaussians。K个learnable ellipsoidal centers通过distance + hash-MLP residual和annealed Gumbel-Softmax分配parts，
  每part学习SE(3) revolute/prismatic transform；render/CD/center regularization joint optimization后用TSDF提取part meshes。
- **State Ownership:** RGB-D capture/calibration拥有observations；canonical Gaussian set拥有cross-state object identity；part centers/masks拥有decomposition；
  joint parameters拥有kinematic transition；per-state transform拥有rendered state；TSDF mesh是derived artifact；controller/simulator才拥有可执行action与physics。
- **Control Flow / Data Flow:** capture multi-view RGB-D at two states → train state-local Gaussians → match/downsample and infer motion → initialize canonical
  Gaussians/part centers → warm up joint type → jointly optimize masks+SE(3)+geometry → render states/evaluate axes → extract part meshes → import into simulator →
  verify interaction before physical use。
- **Implementation Details:** single-state 10K steps (~2 min/object)，joint-type warmup3K–5K steps(30–50s)，joint optimization20K steps(5–7min)；
  RTX3090 time comparisons；Gumbel temperature1→0.1 over10K；5K matching Gaussians；part count K is provided，not inferred from open world。
- **Evaluation Contract:** PARIS(10 synthetic+2 real two-part)、DTA-Multi(2 synthetic three-part) and ArtGS-Multi(5 synthetic with3–6 movable parts)；
  10K-point bidirectional Chamfer for whole/static/movable mesh，axis angle/position and part-motion error；10 trials simple/DTA、3 trials complex。
- **Baselines / Ablations / Sensitivity / Overhead:** Ditto/PARIS/CSG-reg/3Dseg-reg/DTA；random canonical init、MLP/slot segmentation、random centers、
  no motion prior、no joint warmup；no unknown-K test、more-than-two states、continuous video、contact/material physics、closed-loop manipulation or sim-to-real ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** per-object RTX3090 and ~8-minute optimization disclosed；RGB-D view count、precision、
  Gaussian count after densification、memory、batch/concurrency、render/control frequency and robotics SLO not fully disclosed。
- **What the Evidence Actually Proves:** 在小规模per-object two-state contract中，canonical cross-state representation + motion-aware part assignment improves
  joint/mesh metrics and runtime over selected baselines，且initialization/part assignment是作者实验中的关键failure determinant。
- **What It Does Not Prove:** learned replica满足物理动力学、contact/friction/safety，two views/states足以identify all joints，K可自动发现，project mesh可
  直接用于robot control，或IsaacSim demo代表sim-to-real success。
- **Limitations / Threats to Validity:** tiny/new synthetic benchmark、two-state assumption、knownK、same-motion parts merge、bad center init persists、
  sensor noise/occlusion、TSDF limits mesh fidelity、no code/weights、per-object optimization、baseline scaling and no open-world/human-environment validation。
- **Trade-offs / New Failure Modes:** explicit canonical/kinematic state makes replica controllable and diagnosable but needs capture states、per-object optimization and
  brittle initialization；soft→hard assignment stabilizes training yet can commit wrong part identity；Gaussians render efficiently while derived TSDF may lose precise surfaces；
  same-motion parts are observationally non-identifiable from two states。
- **Where the Previous Design Still Applies:** static Gaussian/NeRF for rendering-only objects；CAD/physics simulator for exact known mechanisms；feed-forward
  segmentation/kinematics for high-volume known categories；multi-state/interaction sensing when identifiability matters；human correction for safety-critical digital twins。
- **Evolution Relationship:** `Direct Evolution`：state-local render → correspondence-aligned canonical geometry → explicit part identity + kinematic transition →
  interactable replica；toward embodied closed loop still requires action-conditioned observation、physics/contact and real outcome correction。
- **ROADMAP Node:** `MULTIMODAL-EMBODIED-VLA`（Current Ch26；Legacy N/A）主 owner；handoff到
  `MULTIMODAL-WORLD-MODELS`、`MULTIMODAL-REPRESENTATION`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch25 observed/belief/imagined state与action transition、Ch26 physical action/embodiment/sim-to-real，
  以及Ch23 modality/provenance；ArtGS补的是environment replica state contract，不是VLA policy本身。
- **Existing Coverage:** Ch25/26已有world state、simulator、physical feedback与state ownership，但对“renderable representation→canonical articulated
  replica”的中间演进较弱；该family可refine part identity/observability边界并明确render quality≠control correctness。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；只沉淀canonical/part/motion state与identifiability trade-off，
  不保留SOTA metric或把demo写成robotics evidence。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books；project demo可读但code/immutable artifact缺失已记录。
- **Open Questions:** event-time code/data、unknown part count、multi-state active sensing、identical-motion identifiability、contact/material dynamics、
  real-time update、mesh fidelity、sim-to-real/closed-loop outcome、safety envelope and independent reproduction。

### FUSED: Reversible Unlearning Moves Deletion into a Versioned Adapter—but Does Not Prove Erasure

- **Candidate / Week / Score:** Unlearning through Knowledge Overwriting: Reversible Federated Unlearning via Selective Sparse Adapter / 2025-W09 / 26/30。
- **Source Family ID:** `fused-selective-sparse-adapter-federated-unlearning`。
- **Source Type:** arXiv v1 + public PyTorch implementation；experimental federated unlearning for image classifiers。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-28，current metadata only one version；current nine-commit repository has no
  release/tag，therefore code revision at event time is not fixed。
- **Direct Primary Sources:** https://arxiv.org/html/2502.20709v1；https://arxiv.org/abs/2502.20709；
  https://github.com/Zhong-Zhengyi/FUSED-Code。
- **Related Primary Sources:** Retraining、FedEraser、Exact-Fun、EraseClient baselines；FashionMNIST/CIFAR datasets and paper’s membership-inference protocol。
- **Access and Verification Status:** v1全文/equations/algorithm、client/class/sample settings、main results、CLI ablation、discussion and current code/dependencies
  已核验；no immutable event-time commit，paper/repo license and reproducibility metadata are incomplete。
- **Full-read Coverage:** metadata、MU/FU/catastrophic-forgetting related work、CLI layer-distance calculation、sparse adapter merge/aggregation、gradient-overwrite
  argument、50-client setup、IID/non-IID、RA/FA/ReA/MIA/compute/communication、critical-layer analysis、data-reduction/CLI ablations、limitations and quick start。
- **Original Problem:** 删除某client/class/sample后，从剩余数据完整retrain最可信却昂贵；approximate federated unlearning可能误伤共享knowledge、改变base
  weights且难撤销。系统需要把“忘记请求”与保留knowledge、通信成本和恢复/审计分开。
- **Why the Previous Design Was Reasonable:** full retraining从未包含待删数据，语义最清楚；server-only update不依赖clients在线；checkpoint rollback简单。
  高风险删除、模型小或remaining data可得时，retrain仍是更强基线。
- **Changed Constraint:** FL data分散且clients可能退出；不同client贡献在weights中重叠，删除request需要低通信、limited interference和artifact-level
  reversibility，同时不能把“可卸载adapter”误写成法规意义的exact deletion。
- **Mechanism:** server先发global model，clients local-train后上传；按每层client-model与initial global参数的weighted Manhattan distance排序critical layers。
  在top-K layers随机保留稀疏adapter parameters，冻结base；持有remaining data的clients只训练adapter并FedAvg aggregation，最后merge/attach到base，
  用remaining knowledge覆盖target behavior。移除adapter即可恢复原base（也会恢复原knowledge）。
- **State Ownership:** original global checkpoint仍拥有含target data的knowledge；CLI run拥有layer ranking；unlearning request/manifest拥有target scope；
  sparse adapter拥有behavioral overwrite delta；remaining clients拥有local data/updates；server拥有aggregation；deployment alias决定base+adapter组合；auditor拥有
  erasure evidence，不能由adapter presence单独替代。
- **Control Flow / Data Flow:** register deletion target → pin original checkpoint/client-data lineage → one federated probe round → rank sensitive layers →
  create sparse adapters → distribute only toremaining-data clients → local overwrite training → aggregate I rounds → publish base+adapter artifact → evaluate retained/
  forgotten/MIA slices → deploy or remove/replace adapter → retain audit and propagation evidence。
- **Implementation Details:** PyTorch2.2，one server/50 clients，SGD/Adam、batch128、global/local iterations；FashionMNIST-LeNet、CIFAR10
  ResNet18/SimpleViT、CIFAR100-ResNet18；Dirichlet α1.0/0.1；repo quick start uses100 global×5 local epochs and CUDA12.1 stack。
- **Evaluation Contract:** client unlearning via label-flip Byzantine client、class unlearning、sample unlearning via backdoor；retained accuracy(RA)、forgotten
  accuracy(FA)、relearning accuracy(ReA)、membership-inference accuracy、wall-clock compute and single-client communication；Retraining treated as upper bound。
- **Baselines / Ablations / Sensitivity / Overhead:** Retraining/FedEraser/Exact-Fun/EraseClient；CLI vs random layers、critical-layer evolution、half remaining data、
  IID/non-IID；no cryptographic deletion verification、adaptive attacker、many sequential requests、client dropout/stragglers、adapter composition/order、large model or language data。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** single RTX4090 simulation、50 logical clients、batch128 and small classifiers disclosed；
  precision、network topology/latency、parallel clients、secure aggregation、DP、server memory、real FL wall-clock availability and deletion SLO为`Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者small-image simulated FL setup中，layer-selective sparse remaining-data adapters reach selected utility/forgetting
  proxies near retraining with lower communicated parameters；CLI outperforms random layer selection on retained accuracy slices。
- **What It Does Not Prove:** target information从base weights或backups中被删除、MIA metric exhausts privacy leakage、adapter removal preserves deletion、
  reversibility and right-to-be-forgotten are simultaneously satisfied、all clients will participate，或method scales to LLMs/real heterogeneous FL。
- **Limitations / Threats to Validity:** authors acknowledge remaining-data and all relevant client participation requirements；small public image datasets、simulated
  network、weak MIA、random sparse mask、no confidence intervals/independent reproduction、relearning metric ambiguity、no repeated request/composition or malicious server/client。
- **Trade-offs / New Failure Modes:** frozen base+adapter lowers update/communication and offers operational rollback，但original sensitive knowledge remains recoverable；
  adapter loss/misrouting silently revives behavior；critical-layer ranking leaks client-update statistics and may drift；sequential adapters conflict；client absence blocks deletion；
  overwrite may suppress behavior without removing memorized representation。
- **Where the Previous Design Still Applies:** full retraining for strongest provenance reset；SISA/data partitioning for planned deletion；server-side influence/update for
  offline clients；data-store/index deletion for external state；DP to limit future contribution leakage；model retirement when exact erasure cannot be demonstrated。
- **Evolution Relationship:** `Alternative Branch`：full retrain → approximate weight update → isolated sparse overwrite adapter；从irreversible mutation演进到
  versioned removable delta，获得rollback却暴露“rollback会恢复被忘知识”的governance contradiction。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Current Ch72；Legacy Ch68）主 owner；handoff到`TRAIN-DATA`、`TRAIN-CHECKPOINT`、
  `PLATFORM-ARTIFACT-MANAGEMENT`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch27 deletion/consent/data lineage、Ch35 base+adapter/merge/checkpoint lineage、Ch58 artifact promotion、
  Ch66 evidence contract与Ch72 privacy/deletion propagation；确认unlearning属于derived model-state deletion，不等于input-store delete。
- **Existing Coverage:** Books已有data/index/cache delete propagation和base+adapter identity，却缺少“behavior overwrite、weight erasure、rollback
  reversibility三者冲突”的明确演进；FUSED可作为受限机制refine，必须保留small-model/weak-verifier边界。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；只沉淀deletion object、adapter ownership、rollback contradiction和
  verification ladder，不把作者RA/FA/MIA写成法律或exact-erasure证明。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，current repository无W09 tag且license未明确。
- **Open Questions:** event-time code/license、deletion threat model、strong extraction/influence audit、client dropout/secure aggregation、sequential adapter
  composition、base/checkpoint/backup retirement、large-model scaling、time-to-delete SLO、legal interpretation and independent reproduction。

### Relation-Specific Neurons: Local Intervention Supports Distributed, Shared Mechanisms—not a Neuron Dictionary

- **Candidate / Week / Score:** On Relation-Specific Neurons in Large Language Models / 2025-W09 / 26/30。
- **Source Family ID:** `relation-specific-neurons-intervention-evidence`。
- **Source Type:** arXiv v1 + later EMNLP 2025 code/data artifact；mechanistic-interpretability intervention study。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-24；v2 2025-10-07 and EMNLP publication arelater revisions。
  W09 locks v1 claims/limitations；current repository is later artifact lineage and has no event-time tag。
- **Direct Primary Sources:** https://arxiv.org/pdf/2502.17355v1；https://arxiv.org/abs/2502.17355；
  https://github.com/cisnlp/relation-specific-neurons。
- **Related Primary Sources:** LRE relation triples、Dolma frequency proxy、Llama-2-7B/13B；current code is based on Self-Conditioning and
  language-specific-neuron tooling，not an independent reproduction。
- **Access and Verification Status:** arXiv v1 HTML cache missed，so同ID v1 PDF全25页、appendices、metadata and current three-commit repository已核验；
  PDF covers method/results/figures/limitations，artifact only current state and no release tag。
- **Full-read Coverage:** metadata、knowledge-neuron/representation related work、12-relation data split、positive/negative AP identification、held-out
  entity-disjoint QA、top-k zero intervention、7B/13B layer/overlap/intra/inter results、k sensitivity、five-language transfer、Dolma frequency proxy、concept
  comparison、neuron-type appendix、limitations and official commands。
- **Original Problem:** factual triple由entity和relation共同决定；activation probe可发现相关neuron，却无法说明模型是否在generation中使用relation-level
  mechanism，亦不清楚facts是单neuron、distributed population还是shared feature处理。
- **Why the Previous Design Was Reasonable:** weight/activation visualization和linear probes便宜、适合大规模发现；fact-specific editing更直接处理单个
  knowledge item。若目标只是关联性筛选或known fact correction，这些旧方法仍合理。
- **Changed Constraint:** 要提出mechanism claim必须控制entity overlap、对候选activation做intervention并测target与non-target behavior；同时要承认
  neural basis/polysemanticity会让单coordinate label随model size/initialization改变。
- **Mechanism:** 对每个relation构造positive prompts与其他relation negatives，取FFN neuron在tokens上的平均output，以Average Precision排序；
  在无subject overlap的50 held-out triples/relation上，把top-k neuron outputs置零并生成前2 tokens。比较同relation、其他relations、不同k/model/language，
  得到cumulativity、versatility和interference hypotheses。
- **State Ownership:** dataset/template拥有relation label与entity split；model revision/basis拥有neuron identity；probe run拥有AP ranking；intervention hook
  拥有top-k/forcing/token position；generation/scorer拥有two-token correctness；interpretation owner只能保存hypothesis和scope，不能把label写成模型内部真名。
- **Control Flow / Data Flow:** triples → relation-specific detection/eval split → validate prompts model answers correctly → collect FFN outputs → AP rank
  per relation → freeze model/relation/k → zero selected outputs on held-out prompts → compare target/cross-relation/language accuracy → test frequency/concept confounds →
  record causal scope and non-target effects。
- **Implementation Details:** Llama-2-7B(32 layers/835,584 FFN neurons) and13B(40/1,310,720)，12 relations，50 held-out triples each；
  default top3000 FFN neurons，generation length2；current Python3.8 code supports two Llama models and exposes top-k/zero-forcing scripts。
- **Evaluation Contract:** original vs relation-neuron ablation vs cross-relation/random/k sweeps；entity overlap minimized；English primary evaluation plus German/
  French/Chinese/Japanese transfer on7B；frequency robustness approximated usingDolma documents containing subject+object，not actual Llama-2 pretraining counts。
- **Baselines / Ablations / Sensitivity / Overhead:** k from0 through50K、random deactivation、7B vs13B、cross-relation overlap/interference、language and
  concept-neuron comparison、other neuron types preliminary；no activation patch restoration、causal mediation/circuit reconstruction、paraphrase/template robustness、
  instruction-tuned models or basis-rotation invariance。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model sizes、layers、neuron counts、prompt/eval sizes disclosed；hardware、precision、
  batch、prompt length distribution、generation throughput/memory and production SLO为`Not Disclosed`。
- **What the Evidence Actually Proves:** 在两base models和12 templated relation tasks中，AP-selected FFN coordinates have stronger causal influence than
  random coordinates on held-out same-relation recall，effects accumulate acrossmany neurons and can transfer/interfere across relations/languages。
- **What It Does Not Prove:** 每个relation拥有稳定独立neuron set、selected neurons “store” complete facts、zero intervention无off-manifold side effects、
  overlap等于shared semantic mechanism、English internal translation claim成立，或coordinates可跨checkpoint/model family对齐。
- **Limitations / Threats to Validity:** 12 relations/5 languages、templated two-token QA、base Llama-2 only、top3000 arbitrary、zeroing distribution shift、
  no prompt paraphrase/seed confidence、Dolma not training corpus、v1 PDF/current code drift、basis dependence and correlated entity/type features。
- **Trade-offs / New Failure Modes:** coordinate-level intervention简单可复现，却把distributed feature切成basis-dependent neurons；更大k增强target effect也
  增加collateral damage；shared neurons提高parameter reuse却产生interference；apparent improvement onother relations may be noise removal or off-manifold behavior，
  不是可靠optimization strategy。
- **Where the Previous Design Still Applies:** black-box behavior evaluation for deployment truth；probes for cheap discovery；sparse features/circuits for more
  basis-robust decomposition；activation patching/restoration for stronger causal chain；fact-level editing when exact fact—not relation mechanism—is the target。
- **Evolution Relationship:** `Direct Evolution` of evidence：activation correlation → relation-vs-other decodability → entity-disjoint neuron intervention →
  cross-relation/language side-effect analysis。它支持distributed/shared representation，不支持single-neuron dictionary。
- **ROADMAP Node:** `WORLDVIEW-REPRESENTATION`（Current Ch5；Legacy Ch5）主 owner；handoff到`MODEL-FFN`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch5 superposition/correlation→decodability→intervention evidence ladder、Ch16 FFN memory intuition，
  Ch66 causal evaluation和Ch72 intervention/safety boundary；现有Books已明确single neuron polysemantic和causal evidence限制。
- **Existing Coverage:** Ch5已有几乎同构的证据阶梯、basis dependence和intervention caveat，Ch16明确neuron-concept不可直接推出；本论文提供
  relation-level case与collateral interference evidence，但没有新增长期框架缺口。
- **Integration Decision:** `Books Pending — No Change Candidate`；保留Weekly作为受限案例，不复制relation list或top-k数字进正文。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，v2/EMNLP wording和later code不覆盖v1 evidence。
- **Open Questions:** immutable v1 code/data、paraphrase and prompt-template robustness、activation restoration、basis-invariant features、instruction models、
  other architectures/languages、multiple seeds、off-manifold zeroing、frequency causal test and independent reproduction。

### MAMUT: Symbolic Invariance Can Generate Hard Data, but a Generator Is Not a Learning Result

- **Candidate / Week / Score:** MAMUT: A Novel Framework for Modifying Mathematical Formulas for the Generation of Specialized Datasets for Language Model Training / 2025-W09 / 22/30。
- **Source Family ID:** `mamut-symbolic-equivalence-hard-negative-data`。
- **Source Type:** arXiv v1 + public SymPy-based generator + four public datasets；data-construction artifact，not a trained-model evaluation。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-28，current metadata only one version；repository/datasets are continuously
  maintained and lack immutable W09 release mapping。
- **Direct Primary Sources:** https://arxiv.org/html/2502.20855v1；https://arxiv.org/abs/2502.20855；
  https://github.com/aieng-lab/math-mutator；https://huggingface.co/ddrg。
- **Related Primary Sources:** modified SymPy random-LaTeX fork、NMFT 71 identities、ARQMath/AMPS source datasets；source licenses and data provenance
  remain separately authoritative。
- **Access and Verification Status:** v1全文、EquVG/FalseVG methods、all dataset statistics/examples、implementation appendix and public artifacts已核验；
  paper provides no downstream model-training experiment, human error audit or immutable event-time dataset hashes。
- **Full-read Coverage:** metadata、math language/MIR/data augmentation related work、NMFT creation、parse/substitute/random-print EquVG、eight FalseVG
  strategies、MF/MT/NMF/MFR construction/stats/filtering、SymPy/hybrid parser、examples/conclusion and source/artifact boundaries。
- **Original Problem:** mathematical equivalence is invariant tovariable renaming、commutative reorder and notation style，while random negatives are too easy；
  models can exploittoken overlap/function presence instead ofstructure。Expert-curated formula pairs are accurate but too small forrepresentation learning。
- **Why the Previous Design Was Reasonable:** human-curated math datasets and formal theorem tools provide stronger correctness；random negatives arecheap and
  scalable；LLM paraphrase handles natural-language variation。High-stakes proof or unsupported notation仍需要这些分支和formal verification。
- **Changed Constraint:** training needs millions ofcontrolled positive/near-negative variants withconsistent symbol replacement acrossformula+text；generator must
  distinguish semantic invariance fromLaTeX surface variation and preserve source/provenance identity。
- **Mechanism:** EquVG parsesLaTeX intoextended SymPy/hybrid expression，substitutes variables/functions consistently and randomly prints equivalent
  commutative/notation forms。FalseVG applies random subsets of operator swap、partial variable split、constant replacement、false distribution、manual and random
  strategies，then substitution/printing，creating visually close non-equivalent pairs。String uniqueness dedupesoutputs。
- **State Ownership:** source row/license owns original content；parser version owns symbolic tree；transformation recipe/seed ownsderived variant；equivalence label
  owner is symbolic rule/manual template，not the model；dataset manifest ownssource→variant lineage；training run owns sampling weights；independent verifier ownsheld-out correctness。
- **Control Flow / Data Flow:** ingest formula/text + provenance → parse classically or safe hybrid → validate/filter → choose EquVG or FalseVG recipe → apply
  consistent substitutions/structural mutation → randomized LaTeX print → validate/dedup at string level → publish versioned rows/labels → train/evaluate only on
  source-disjoint heldout concepts and notation families。
- **Implementation Details:** SymPy1.12 extended for matrices/sets/derivatives/operators and safe string substitution；71 named identities/522 templates；
  generated sizes include3.2M MF、7.0M MT and~23.7M NMF/MFR rows；output count is not token count or independent semantic diversity。
- **Evaluation Contract:** paper reports construction statistics、string uniqueness and illustrative rules only；no encoder/LLM baseline、downstream retrieval/
  equation completion、ablation、human/formal sample audit、source-family holdout or contamination test。Therefore model-benefit claim remains unverified。
- **Baselines / Ablations / Sensitivity / Overhead:** related work discussed expert/synthetic/LLM augmentation and random negatives，but no matched experiment；
  no mutation-rate/strategy sensitivity、parser failure rate、false-positive label rate、duplicates under symbolic canonicalization、compute/storage/quality trade-off。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** TU Dresden HPC acknowledged，but hardware/runtime/storage、formula length distribution、
  generation concurrency/cost、training model/precision/batch and any SLO are`Not Disclosed`。
- **What the Evidence Actually Proves:** deterministic symbolic/LaTeX transformation pipeline can generatelarge named datasets and encode explicit invariances/
  near-negative recipes with public artifacts；it creates a controllable data actuator beyond naive textual paraphrase。
- **What It Does Not Prove:** every generated equivalence/non-equivalence label is mathematically correct、millions of strings are semantically diverse、models learn
  deeper mathematics、hard negatives improve OOD reasoning/retrieval、or generated rows are free of source-license/contamination concerns。
- **Limitations / Threats to Validity:** parser andrule coverage有限；some identities carry missing domain assumptions；manual/GPT-3.5 templates can be wrong；
  string dedup≠semantic dedup；no downstream evidence/formal audit；source distributions math forums/exercises narrow；large variants from71 identities risk template memorization。
- **Trade-offs / New Failure Modes:** explicit symbolic rules improve label auditability but only within supported grammar；hard negatives suppressshortcuts yet can teach
  generator artifacts；mass variants rebalance gradients towardfewtemplates；hybrid string parser increases coverage while weakening formal semantics；false formulas require clear
  containment to avoid leaking as factual training text。
- **Where the Previous Design Still Applies:** theorem prover/CAS forformal verification；expert datasets fordomain assumptions/proofs；LLM transformation forrich natural
  language followed byverifier；random negatives forbroad easy-rejection calibration；fixed untouched test sets forlongitudinal comparison。
- **Evolution Relationship:** `Direct Evolution`：raw math corpus → variable renaming → structure-preserving symbolic equivalence → adversarial near-negative generation →
  verifier-gated, source-disjoint curriculum。MAMUT reachesgeneration，not the final verifier/model-benefit stages。
- **ROADMAP Node:** `TRAIN-DATA`（Current Ch27；Legacy Ch23）主 owner；handoff到`MODEL-TOKENIZER`、
  `TRAIN-PRETRAINING`、`PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch27 data provenance/synthetic curriculum/verifier/contamination、Ch11 tokenization、Ch28 objective and
  Ch66 evidence；现有Books有generator-verifier separation，但symbolic invariance/near-negative branch可更具体。
- **Existing Coverage:** Ch27已说明synthetic diversity、feature coverage、independent verifier和source lineage；MAMUT可refine“formal transformation preserves
  known invariance better than free-form generation”，同时暴露rule coverage与template amplification。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Downstream Model Evidence Missing`；只能沉淀data-construction principle，
  不得写成模型数学能力提升结论。
- **Changed Files or Rejection Reason:** 本轮只更新Weekly；未修改Books，continuous datasets/repo未当作W09 frozen artifact。
- **Open Questions:** event-time hashes/licenses、domain-assumption verifier、parser/rule failure audit、semantic dedup、source-disjoint evaluation、downstream
  model ablation、negative leakage containment、strategy weighting、storage/compute cost and independent reproduction。

### DVPO v1: Freezing Value Removes Critic Drift but Freezes Its Coverage Boundary Too

- **Candidate / Week / Score:** Lean and Mean: Decoupled Value Policy Optimization with Global Value Guidance / 2025-W09 / 28/30。
- **Source Family ID:** `dvpo-pretrained-global-value-static-critic`。
- **Source Type:** arXiv v1 experimental RLHF algorithm；later v2/ICLR 2026 paper and Microsoft code are revision/artifact lineage，not W09 evidence。
- **Event Date / First-public Date / Revision History:** v1 2025-02-24 titled`Lean and Mean...`；v2 2026-01-26 retitled
  `Pretrain Value, Not Reward...` and materially refines framing/code availability。This packet locks v1 method/theorem/results。
- **Direct Primary Sources:** https://arxiv.org/html/2502.16944v1；https://arxiv.org/abs/2502.16944。
- **Related Primary Sources:** v2/ICLR lineage and https://github.com/microsoft/DKI_LLM/tree/main/dvpo only verifylater evolution；UltraFeedback、UltraRM、
  HH-RLHF、MT-Bench/Arena-Hard/AlpacaEval and PPO/DPO/GRPO baselines retain their own contracts。
- **Access and Verification Status:** v1 full HTML、method/equations/theorem、training/evaluation、efficiency curves、appendices/hyperparameters/judge prompt已核验；
  v1 has no immutable official code artifact，later code cannot establish event-time implementation semantics。
- **Full-read Coverage:** metadata/revision、RLHF/value/reward related work、MDP/data definitions、trajectory-conditioned GVM、TD target/batch normalization、
  frozen-value PPO objective、equivalence theorem/assumptions、base/instruction settings、all baselines/judges、training curves/efficiency、hardware/hyperparameters and appendices。
- **Original Problem:** PPO-style RLHF simultaneously keepsactor、online critic、reward and reference models；critic追随moving policy增加state/compute和instability。
  Offline preference setting又没有new ground-truth rewards，raising whether online critic learning adds information or only re-estimates a fixed proxy。
- **Why the Previous Design Was Reasonable:** online critic approximates current-policy return and can adapt when rollout distribution changes；reward model
  separates terminal preference semantics from value bootstrap。Whenever fresh verifier/environment reward exists、coverage moves materially or long-horizon credit matters，
  actor-critic remains the clearer branch。
- **Changed Constraint:** in fixed-feedback RLHF，labels/reward do not refresh during policy optimization，yet four-model memory and critic drift dominate cost；
  system seeks token-level guidance without co-training another mutable model。
- **Mechanism:** pretrain a trajectory-conditioned GVM `Q_phi(tau,s,a)` on offline policy trajectories and return-to-go via TD loss，normalize value batches，then
  freeze it。Policy uses clipped PPO ratio with normalized GVM output as static advantage；trajectory examples act as policy identity rather than explicit policy parameters。
- **State Ownership:** offline preference/reward dataset ownssupervision；trajectory sample ownsimplicit policy identity；GVM checkpoint ownsfixed value surface；
  actor/old policy ownrollout/update；reference policy ownsKL anchor；batch-normalization statistics/objective version ownvalue scale；evaluator ownsindependent quality evidence。
- **Control Flow / Data Flow:** collect policy trajectories + terminal proxy reward → construct prefix actions/discounted returns → train and calibrate GVM → freeze
  GVM/version → actor generates rollouts → score each sampled token/prefix with GVM → normalize static advantages → PPO clipped update againstold policy/KL anchor →
  monitor policy-to-GVM coverage and external quality → stop/refresh/reject。
- **Implementation Details:** v1 uses Llama3.2-3B/Llama3-8B base→SFT and Mistral-7B-Instruct settings，UltraFeedback/UltraRM/HH-RLHF；SFT LR2e-5,
  batch16,3 epochs；RM LoRA rank8/alpha32/dropout0.1,batch4；8×A100-80GB for SFT/RM。Exact GVM/policy hyperparameters are partly appendix-dependent。
- **Evaluation Contract:** MT-Bench80 questions、Arena-Hard500、AlpacaEval805 and held-out preference sets，primarily GPT-4/GPT-4o judges；compare SFT、
  DPO、ReMax、GRPO、PPO under base/instruction settings；memory/time claims tied to disclosed training pipeline and model sizes。
- **Baselines / Ablations / Sensitivity / Overhead:** policy-conditioned vs generic value cases、GVM performance/curves and PPO/DPO/reward-only baselines；
  no fresh-reward setting comparison、trajectory policy-identity ablation across large drift、GVM refresh schedule、judge-human calibration、multiple seeds/confidence intervals、
  long-horizon/tool environment or complete end-to-end pretrain-GVM amortization analysis。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 8×A10080GB and3B/7B/8B disclosed，some batches/LRs/steps reported；precision、
  rollout length/concurrency、GVM request batching、communication/offload、total GPU-hours including GVM pretraining and production SLO not fully disclosed。
- **What the Evidence Actually Proves:** in the authors’ fixed-proxy, small set of LLM preference workloads，pretraining/fixing a policy-conditioned value model can
  guide PPO-like updates with comparable author benchmark scores and reduced policy-phase mutable model cost；static critic is a viable conditional branch。
- **What It Does Not Prove:** reward and value are generally equivalent、fixed GVM remains accurate under large policy drift、token-level value identifiescausal token
  contribution、headline memory/time includes all lifecycle costs、LLM judges equal human preference，or PPO’s online critic is universally redundant。
- **Limitations / Threats to Validity:** theorem assumes bounded approximation error、offline support coverage、fixed signals and same distribution；those areexactly
  fragile under policy optimization。Trajectory-as-policy proxy may be ambiguous；TD bootstraps a learned proxy；v1 code absent；few model families/datasets、judge bias、
  no seeds/error bars or safety/factual verifier slices。
- **Trade-offs / New Failure Modes:** frozen GVM removesmoving-target coupling and memory but converts critic error into persistent optimization bias；trajectory
  conditioning adds long input/state identity；batch normalization makes advantage scale batch-composition-dependent；policy can exploit static GVM and leave support without
  an online critic detecting drift。
- **Where the Previous Design Still Applies:** PPO critic when current-policy values/fresh rewards matter；GRPO when same-prompt rollout groups are cheap；DPO for
  offline simplicity/auditability；verifier outcome for executable tasks；periodically refreshed RM/value ensemble when drift/uncertainty can be measured。
- **Evolution Relationship:** `Alternative Branch`：terminal reward + online critic → reward-only/group baseline → pretrained policy-conditioned value + static critic。
  It moves credit estimation earlier in lifecycle，tradingco-adaptation for frozen coverage and amortization。
- **ROADMAP Node:** `TRAIN-PPO`（Current Ch32；Legacy Ch28）主 owner；handoff到`TRAIN-RLHF`、`TRAIN-GRPO`、
  `PLATFORM-EVALUATION-SYSTEM`与`INFER-RESOURCE-SCHEDULING`。
- **Target and Adjacent Chapters Read:** 已读Ch31 reward/policy-relative state、Ch32 critic/advantage/PPO state、Ch33 group baseline and Ch66 judge evidence；
  current Books has prompt-only/static baseline branches but not full lifecycle placement of pretrained value artifact。
- **Existing Coverage:** Ch32 already separates value granularity and notes stale baselines；DVPO can refine “critic mutability vs artifact coverage” evolution and GVM
  version/state ownership，without adopting theorem as universal claim。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Theorem Assumptions Restricted`；no benchmark/memory headline retained as general fact。
- **Changed Files or Rejection Reason:** this pass updates Weekly only；Books untouched；v2 title/code/results not used to overwrite v1 event evidence。
- **Open Questions:** v1 code/immutable run、total GVM amortization、support-distance detector、refresh/rollback policy、trajectory policy identity、value calibration、
  safety/factual verifier、judge-human agreement、distributed rollout architecture、independent reproduction and theorem under drift。

### NeoBERT: Modern Components Help, but Data, Scale and Boundary-correct Packing Still Dominate

- **Candidate / Week / Score:** NeoBERT: A Next-Generation BERT / 2025-W09 / 26/30。
- **Source Family ID:** `neobert-modern-bidirectional-encoder-pretraining`。
- **Source Type:** arXiv v1 + open training/evaluation code、F32 checkpoint and model card；encoder architecture/pretraining ablation study。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-26，current only one paper version；HF collection/model release around2025-02-28
  is a separate artifact node。Current repos/models are mutable and no W09 immutable release was found。
- **Direct Primary Sources:** https://arxiv.org/html/2502.19587v1；https://arxiv.org/abs/2502.19587；
  https://github.com/chandar-lab/NeoBERT；https://huggingface.co/chandar-lab/NeoBERT。
- **Related Primary Sources:** RefinedWeb、GLUE、MTEB and standardized contrastive fine-tuning dataset/protocol；BERT/RoBERTa/NomicBERT/ModernBERT baselines。
- **Access and Verification Status:** v1 full text/appendices、ten successively trained ablations、data/training/eval/efficiency and current code/model card checked；
  later Transformer integration issue and mutable model files are not W09 architecture proof。
- **Full-read Coverage:** metadata、encoder related work、depth/width/RoPE/Pre-LN-RMSNorm/SwiGLU、RefinedWeb/tokenizer/length、MLM mask/optimizer/batch、
  M0–M9 ablations including discarded choices、GLUE/MTEB/length/throughput、8-H100 training details、broader impact、repository/model artifact。
- **Original Problem:** BERT-like encoders remain useful forrepresentation/classification/retrieval but legacy absolute positions、small corpora and old recipes limit
  context/quality。Comparisons confound pretraining backbone with expensive task-specific fine-tuning，making it unclear which system choice actually helps。
- **Why the Previous Design Was Reasonable:** BERT/RoBERTa are compact、mature and fast at≤512 tokens；WordPiece and padding preserveboundary semantics；
  absolute positions are simple。For short, latency-sensitive classification or existing ecosystem compatibility they remain strong baselines。
- **Changed Constraint:** modern retrieval/embedding tasks need4K context、larger/diverse data and efficient kernels while keeping encoder-only bidirectional semantics；
  design must separate architectural modernization from data scale and downstream contrastive recipe。
- **Mechanism:** 250M/28-layer×768 encoder usesRoPE、Pre-LN RMSNorm、SwiGLU、MLM20% all-mask、AdamW cosine and FlashAttention；
  stage1 trains1M steps/2T tokens at1024，stage2 adds50K/100B at4096。Ten fully trained variants add changes sequentially；MTEB comparison uses one
  model-agnostic contrastive recipe with task-homogeneous in-batch/hard negatives。
- **State Ownership:** tokenizer/model config ownrepresentation interface；dataset manifest ownsRefinedWeb slice；masking/packing ownattention/loss boundaries；
  pretraining stages ownlength curriculum and position range；checkpoint/model card ownartifact identity；fine-tuning recipe ownsMTEB result，not base model alone。
- **Control Flow / Data Flow:** pin architecture/tokenizer/data → create masked sequences withdocument-safe boundaries → stage1 1024-token MLM → checkpoint →
  stage2 length extension at4096 → evaluate pseudo-PPL by length and GLUE → apply identical contrastive recipe to each backbone → MTEB slices → package code/weights/config →
  runtime throughput test under fixed GPU/length/batch sweep。
- **Implementation Details:** 28 layers、width768、250M；8×H100，1.05M steps/~6000 GPU-hours；local batch32×8 accumulation×8 GPUs≈2M tokens,
  theoretical token batch held in long stage；2.1T tokens total。HF artifact is~982MB F32 custom code and requires explicit trust boundary。
- **Evaluation Contract:** GLUE development-set fine-tune/search；MTEB-English56 datasets/7 task types after2000-step standardized contrastive training；
  Wikipedia2467 long sequences for pseudo-perplexity；synthetic max-length sequences512–8192，batch1–512，100 steps on oneA100 for peak throughput。
- **Baselines / Ablations / Sensitivity / Overhead:** ten successive full pretrains compare architecture/data/tokenizer/optimizer/mask/packing/scale/shape/batch/length；
  changes are sequential not full factorial，so interaction/order confounds remain。No multilingual/OOD/safety/contamination/production workload、multiple seeds or matched total-data compute across all baselines。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 8×H100/6000GPUh training；singleA100 efficiency；F32 published weights；
  lengths/batches/tokens disclosed，but training precision、network topology、latency percentiles、online concurrency/cost and SLO incomplete。
- **What the Evidence Actually Proves:** under authors’ sequential GLUE ablation，data diversity/scale and model size give the largest gains；naive cross-document
  packing and decoder-oriented tokenizer can hurt encoder tasks；modern encoder with staged length training is viable and open artifacts support reproduction attempts。
- **What It Does Not Prove:** each component contributes independently、NeoBERT is universal best encoder、RoPE alone guarantees3K/4K utilization、MTEB scores arise
  only from pretraining、peak tokens/s predictsservice latency，or2.1T-token training is “affordable” across organizations。
- **Limitations / Threats to Validity:** sequential/non-factorial ablation、GLUE saturation/dev tuning、English RefinedWeb bias/contamination、MTEB recipe and training-data
  overlap risk、pseudo-PPL not downstream long-context reasoning、single-run/no uncertainty、custom-code supply-chain exposure and mutable artifact identity。
- **Trade-offs / New Failure Modes:** deeper encoder improves parameter efficiency but increases sequential layer latency；RoPE/long curriculum expands range while dense
  attention cost growsquadratically；large web data brings bias/license/quality debt；packing removes padding but wrong cross-document attention corrupts objective；standardized
  fine-tuning improves comparability yet may underfit models needing specialized adapters。
- **Where the Previous Design Still Applies:** BERT/RoBERTa for≤512 and mature integrations；specialized embedding model/adapters for stable high-volume tasks；
  correct masked packing or padding whenboundary complexity outweighs compute; decoder-only model when generation/in-context behavior is required。
- **Evolution Relationship:** `Direct Evolution` + `Layering / Dependency`：legacy encoder → modern block/position → web-scale MLM → staged long context → controlled
  contrastive adaptation。The paper’s own ablations show modernization is not a monotonic feature checklist。
- **ROADMAP Node:** `TRAIN-PRETRAINING`（Current Ch28；Legacy Ch24）主 owner；handoff到`MODEL-TRANSFORMER-LAYER`、
  `MODEL-POSITION-ENCODING`、`MODEL-TOKENIZER`、`MODEL-LONG-CONTEXT`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch11/13/17 component contracts、Ch27 data/packing、Ch28 objective/batch/schedule and Ch66 evaluation；
  confirmed that architecture details stay in Part II while controlled recipe/evidence is owned by pretraining。
- **Existing Coverage:** Books already covers each component and document-safe packing，but lacks a concise cross-component case showingdata/scale dominance and
  non-monotonic integration；NeoBERT can refine system-level experiment ordering rather than create an encoder product list。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；only keep controlled-ablation lessons and old/new coexistence，not leaderboard claims。
- **Changed Files or Rejection Reason:** this pass updates Weekly only；Books untouched；mutable HF/GitHub and later ecosystem integration are artifact lineage only。
- **Open Questions:** frozen W09 hashes、training precision/logs、ablation order interactions、data contamination/license、multilingual/OOD、long-task utilization、
  latency/cost vs throughput、custom-code security、independent reproduction and encoder-vs-decoder workload boundary。

### Ext2Gen v1: Retrieval Recall Is Not Enough; Evidence Selection Can Become a Trained Generation State

- **Candidate / Week / Score:** Ext2Gen: Alignment through Unified Extraction and Generation for Robust Retrieval-Augmented Generation / 2025-W09 / 27/30。
- **Source Family ID:** `ext2gen-evidence-extraction-preference-aligned-rag`。
- **Source Type:** arXiv v1 experimental RAG generation/alignment study；dataset/model announced but not released in v1。
- **Event Date / First-public Date / Revision History:** v1 2025-02-28 titled`Ext2Gen...`；v2 2025-03-12；v3 2025-11-17 retitled
  `Aligning Extraction and Generation...` and accepted WSDM 2026。W09 packet locks v1 claims/data/artifact status。
- **Direct Primary Sources:** https://arxiv.org/html/2503.04789v1；https://arxiv.org/abs/2503.04789。
- **Related Primary Sources:** five source datasets、eight generator checkpoints、Llama3.3 filter、E5/Chroma retrieval、DPO/KTO/SimPO/QLoRA；
  later dataset/model release was promised but no v1 immutable artifact is available。
- **Access and Verification Status:** v1 full text、method/data rules、feedback construction、robustness and live-retrieval evaluation、all appendices/
  hyperparameters/latency/limitations checked；scientific artifacts section says dataset/model “soon”，so reproduction remains incomplete。
- **Full-read Coverage:** metadata/revisions、retrieval/generation/alignment related work、20K→18K QA construction、relevant/noisy chunk validation、192K outputs/
  120K/150K preferences、SFT/DPO/KTO/SimPO、1K robustness and600 live-RAG tests、position/noise/extraction/feedback/backbone analyses、4-H100 config、latency and limitations。
- **Original Problem:** retriever can include decisive evidence yet generator ignores it because relevant chunk position changes or irrelevant Top-k overloads context；
  improving recall/rerank alone does not train generation to separate evidence from distraction。
- **Why the Previous Design Was Reasonable:** top-k retrieval + direct answer minimizeslatency and orchestration；separate reranker/compressor can be swapped without
  retraining generator。Clean/small contexts or hard SLO still favor direct generation and external deterministic evidence selection。
- **Changed Constraint:** compact generation models receive up to25 noisy chunks at uncertain positions，and evidence-use—not retrieval availability—dominates failure；
  system needs an explicit intermediate evidence state and training signal for both selection and answer quality。
- **Mechanism:** require one model output to contain extracted source sentences followed by final answer；build synthetic mixed-context inputs acrossfive domains，filter
  answer/chunk validity with a different LLM，collect outputs fromeight models，score answer inclusion and similarity with four metrics，form pairs，then DPO-align 3B/8B
  backbones。At runtime extraction is provisional evidence plan feeding generation。
- **State Ownership:** corpus/chunk digest owns source truth；retriever owns candidate set/order；filter model owns synthetic labels；preference rule/metrics ownchosen/
  rejected relation；aligned model owns extraction+answer format；extracted sentence remains derived evidence with source pointer；final verifier owns claim support/abstention。
- **Control Flow / Data Flow:** query + retrieved chunks → validate/mix relevant+noise → model emits extracted sentences → preserve chunk/span mapping → generate answer →
  score inclusion/similarity/faithfulness → train from preferences → deploy behind retrieval → if extraction empty/insufficient requery or abstain，not parametric fill-in。
- **Implementation Details:** 18K filtered QA inputs from HotPotQA/MS-MARCO/PubMed/CNNDM/GovReport，up to25 noise chunks，192K completions and150K R2 pairs；
  Llama3.2-3B/Llama3.1-8B QLoRA+DeepSpeed ZeRO-2 on4×H100，9K steps,batch32；SFT LR5e-4,DPO5e-6,weight decay0.05。
- **Evaluation Contract:** 1K held-out synthetic mixed-context QA(200/domain) plus600 online retrieval questions acrossNQ/MS-MARCO/HotpotQA，Top-k10/20/30,
  naive/HyDE/MuGI；Acc、GPT-4o LLMEval、ROUGE-L、BERTScore and lexical extraction precision/recall。Input averages2161 words；latency is query-level author setup。
- **Baselines / Ablations / Sensitivity / Overhead:** ideal relevant-only、default prompt、metric-specific SFT、DPO R1/R2、KTO/SimPO、0–150K feedback、
  with/without extraction、SFT “gold”、Qwen2.5-3B；no human source-faithfulness audit、adversarial documents、conflicting evidence、multiple relevant sources、ACL/freshness or
  claim-level entailment calibration。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 4×H100、3B/8B、batch32/9K steps disclosed；precision/QLoRA quantization detail、
  sequence/token lengths beyondword average、inference batch/concurrency、retrieval latency/cost and production SLO incomplete。Extraction adds measured latency but hardware context is not full。
- **What the Evidence Actually Proves:** under authors’ synthetic-noise and selected live-RAG contracts，training a model to emit source sentences before answer improves
  the same QA metrics and remains more robust toposition/noise than prompt-only/SFT variants；generation-side evidence use is a separable optimization target。
- **What It Does Not Prove:** extracted sentences are sufficient/true，explicit extraction is faithful reasoning，DPO removes hallucination，metric-composed preferences
  match humans，no-answer calibration works，or gains generalize toconflict/adversarial/multilingual/private corpora and production latency。
- **Limitations / Threats to Validity:** synthetic QA and labels generated/filtered/judged by related LLM ecosystem；true answer assumes one relevant chunk；same metrics
  create preferences and evaluation；artifact unavailable at v1；LLMEval correlation unknown；retrieval corpora/datasets overlap risk；no seeds/error bars/source entailment。
- **Trade-offs / New Failure Modes:** explicit extraction gives citation surface and noise filter but adds tokens/latency and can hallucinate/misquote evidence；joint model
  couples extraction and prose errors；preference rules can optimize lexical similarity；training for fixed noise/order creates brittleness；without relevant chunks model still fails。
- **Where the Previous Design Still Applies:** direct RAG forshort clean context/strict latency；separate reranker/compressor for modularity；claim verifier for high stakes；
  agentic re-query/sufficiency gate when evidence missing；human review when sources conflict or evidence interpretation isdomain-specific。
- **Evolution Relationship:** `Direct Evolution`：retrieve top-k → rerank/compress → prompt-level extract-then-answer → preference-trained joint extraction/generation →
  source-bound claim verification and abstention。Ext2Gen reaches trainedselection，not final verification。
- **ROADMAP Node:** `AGENT-RAG`（Current Ch76；Legacy Ch72）主 owner；handoff到`TRAIN-DPO`、`AGENT-CONTEXT`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch75 context packing、Ch76 relevance/sufficiency/faithfulness and evidence policy、Ch34 preference objective、
  Ch66 claim evidence；confirmed extraction plan is derived state owned by RAG generation，not retriever truth。
- **Existing Coverage:** Ch76 already separates relevance/sufficiency/faithfulness and requires claim verification；Ext2Gen can refine generation-side evolution by
  making evidence selection a trained intermediate state，while v1 adds no new source-authority orverification guarantee。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Artifact Unreleased at v1`；retain mechanism/trade-off，drop benchmark headline。
- **Changed Files or Rejection Reason:** this pass updates Weekly only；Books untouched；v2/v3 and later artifacts do not overwrite v1 status。
- **Open Questions:** v1 dataset/model hashes、source licenses/contamination、span-faithfulness、multiple/conflicting evidence、no-answer calibration、prompt injection/
  ACL、human evaluation、latency/goodput、metric circularity and independent reproduction。

### SuperRAG: Document Layout Is a Retrieval Graph, but Derived Structure Is Not Source Authority

- **Candidate / Week / Score:** SuperRAG: Beyond RAG with Layout-Aware Graph Modeling / 2025-W09 / 25/30。
- **Source Family ID:** `superrag-layout-aware-multimodal-document-graph`。
- **Source Type:** arXiv v1/NAACL 2025 Industry paper + related continuously maintained Kotaemon project；core in-house parser is not open。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-28，only paper version；Kotaemon predates/continues beyond paper and has327 current
  commits，so repository behavior cannot be treated as an immutable SuperRAG release。
- **Direct Primary Sources:** https://arxiv.org/pdf/2503.04790v1；https://arxiv.org/abs/2503.04790；
  https://github.com/Cinnamon/kotaemon。
- **Related Primary Sources:** DOCBENCH/SPIQA、Azure Document Intelligence、DocLayNet in-house parser training、Milvus/Elasticsearch/Neo4j、OpenAI
  embedding-v3-large/GPT-4o-2024-05-01、Cohere reranker；each external component has separate version contract。
- **Access and Verification Status:** v1 PDF all14 pages、layout parser/model schema、retrieval pipeline、datasets/results/ablation/output cases/demo/limitations checked；
  paper’s in-house reader/data/model not public，Kotaemon current main is only related UI/RAG artifact，not complete reproduction。
- **Full-read Coverage:** metadata、graph/multimodal RAG related work、page parser/OCR/table/reading-order/ToC、property graph node/edge schema、LLM/heuristic traversal、
  cross-page/table/diagram expansion、hybrid/rerank/generation stack、DOCBENCH/SPIQA、layout/three-setting ablation、failure samples、demo、limitations and artifact boundary。
- **Original Problem:** flat chunks discard page hierarchy、reading order、section membership and table/figure relationships；multi-page questions need evidence whose
  meaning depends on layout and adjacency，so vector similarity alone may retrieve fragments without their structural context。
- **Why the Previous Design Was Reasonable:** flat lexical/vector index is cheap、incrementally maintainable and robust toparser errors；page-image retrieval preserves
  visual layout without constructing schema。Text-heavy/simple documents or rapidly changing corpora still favor these branches。
- **Changed Constraint:** long enterprise/scientific PDFs mix text、tables、figures and ToC across pages；retrieval must navigate typed hierarchy/sequence while deciding
  whether expensive multimodal expansion is necessary。
- **Mechanism:** parse each page into titles/sections/chunks/tables/diagrams and reading order；build property graph rootedCompany→Document→Page/ToC→MasterSection→
  Section/Table/Diagram with`is_under/has_next` edges；combine BM25/vector candidates with graph expansion，ToC routing，table/diagram OCR+multimodal interpretation，
  optional LLM-generated Cypher and self-reflection，then rerank and generate。
- **State Ownership:** source document/digest owns evidence；parser version owns derived layout nodes/order；graph schema/index revision owns relationships；vector/lexical
  stores own candidate state；LLM traversal owns provisional query plan，not authorization；retrieved spans/images retain source coordinates；generator/evaluator ownanswer/run。
- **Control Flow / Data Flow:** upload/version document → parse pages/modalities → validate reading order/table/figure links → build typed graph + vector/lexical indexes →
  query hybrid retrieval → expand parent/neighbor/ToC/multimodal nodes under budget → rerank → dereference source spans/images → answer/cite → evaluate and trace parser/index versions。
- **Implementation Details:** in-house reader fine-tuned with5773 layout pages and5010 reading-order images plus Azure DI；Milvus+Elasticsearch+Neo4j；top3 tables/
  diagrams、top20 contexts、top10 rerank；GPT-4o completion and OpenAI embedding；Kotaemon offers current multimodal/hybrid/GraphRAG UI but exact paper pipeline is not frozen。
- **Evaluation Contract:** DOCBENCH1102 questions/229 PDFs across5 domains，avg66 pages/46,377 tokens；SPIQA test-A666、B228、C493 figure/table questions；
  GPT-4 evaluator；compare flat/layout graph and external systems/rerun baselines；three cumulative settings add layout expansion then self-reflection。
- **Baselines / Ablations / Sensitivity / Overhead:** non-layout hybrid+cross-page、layout+ToC/table/diagram、plus self-reflection；GPT-4/4o/Kimi/Claude/ColPali/Qwen
  comparisons；no parser-oracle/failure slice、edge-type ablation、graph freshness/delete/ACL、incremental indexing、latency/cost/storage、adversarial PDF or component-version sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** document/test sizes and API model versions/top-k disclosed；hardware、parser/graph build time、
  storage、precision、query concurrency、tail latency/cost and SLO are`Not Disclosed`，despite authors noting multimodal graph overhead。
- **What the Evidence Actually Proves:** in authors’ document QA pipeline，preserving derived layout relationships and selectively expanding table/figure context improves
  GPT-4-judged accuracy over their flat setup；some errors originate at retrieval when relevant visual component is absent。
- **What It Does Not Prove:** graph edges are factually correct/complete，layout parser generalizes，Kotaemon reproducespaper，GPT-4 judge equalsground truth，self-reflection
  causally owns full gain，citations guarantee entailment，or system meets enterprise security/latency/update requirements。
- **Limitations / Threats to Validity:** proprietary in-house parser/training data、API dependencies、cumulative rather than isolated ablations、single judge、small test sets、
  benchmark/system configuration mismatch、no run variance，derived layout can silently corrupt source relations，current repo drift and no immutable artifact。
- **Trade-offs / New Failure Modes:** graph recovers hierarchy/cross-page context but multiplies parse/index/storage/update/ACL/delete state；LLM Cypher can over-traverse or
  inject malformed queries；table/diagram expansion increaseslatency/noise；stale/misparsed edges create confident wrong evidence paths；flat retrieval avoids graph drift。
- **Where the Previous Design Still Applies:** flat BM25/vector forsimple/high-churn corpora；page-image retrieval when visual layout is primary；deterministic parent-child
  expansion for regulated environments；manual schema for stable domain documents；source dereference/human review for high-stakes tables/figures。
- **Evolution Relationship:** `Direct Evolution`：flat chunks → document-aware parent/child → typed layout graph → query-conditioned multimodal expansion →
  source-dereferenced evidence verification。Graph is a navigation/index artifact，not a new source of truth。
- **ROADMAP Node:** `AGENT-RAG`（Current Ch76；Legacy Ch72）主 owner；handoff到`MULTIMODAL-REPRESENTATION`、
  `AGENT-CONTEXT`、`PLATFORM-ARTIFACT-MANAGEMENT`、`PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch23 modality/coordinate provenance、Ch75 context packing、Ch76 multimodal operators/chunking/graph traversal，
  Ch58 artifact lineage and Ch72 ACL/delete；current Books owns this mechanism and its governance handoffs。
- **Existing Coverage:** Ch76 already states parser/table structure、parent-child、modality-native operators、graph provenance/dereference；SuperRAG can refine
  a continuous flat→layout-graph route and typed edge failure modes，without adding a product-specific subsection。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Core Parser Not Open`；mechanism only，not paper leaderboard or vendor stack。
- **Changed Files or Rejection Reason:** this pass updates Weekly only；Books untouched；Kotaemon main and vendor APIs are not treated as W09 frozen implementation。
- **Open Questions:** in-house parser/code/data、event-time repo hash、parser-oracle evaluation、graph edge correctness/freshness、incremental rebuild、ACL/delete propagation、
  adversarial PDFs、latency/storage/cost、judge-human agreement、isolated ablation and independent reproduction。

### R2-T2: Test-Time Routing Turns Reference Successes into Runtime Control State

- **Candidate / Week / Score:** R2-T2: Re-Routing in Test-Time for Multimodal Mixture-of-Experts / 2025-W09 / 27/30。
- **Source Family ID:** `r2t2-test-time-multimodal-expert-rerouting`。
- **Source Type:** arXiv v1 + later ICML 2025 code artifact；test-time adaptation for frozen multimodal expert routing。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-27，current metadata only one paper version；current13-commit repository is later
  artifact lineage with no immutable W09 tag。
- **Direct Primary Sources:** https://arxiv.org/html/2502.20395v1；https://arxiv.org/abs/2502.20395；
  https://github.com/tianyi-lab/R2-T2。
- **Related Primary Sources:** MoAI/MoVA model papers/checkpoints、reference/evaluation datasets and external expert encoders；oracle route is an upper bound only。
- **Access and Verification Status:** v1 full text、three algorithms/equations、all benchmark/reference sets、FLOP and k/kernel/LR/embedding ablations、cases/
  appendices and current code checked；event-time code revision unavailable。
- **Full-read Coverage:** metadata、multimodal MoE/router/test-time adaptation background、NGD/kernel regression/mode finding、neighborhood/embedding choices、
  MoAI/MoVA experts、9 evaluation benchmarks/paired reference sets、oracle/base/results、FLOPs、hyperparameters、route transitions and artifact。
- **Original Problem:** end-to-end router learns an average mapping from task/input toexpert weights，but unseen multimodal tasks may selectwrong perception expert；
  retraining router for every frontier is expensive and freezesnew reference evidence outside runtime。
- **Why the Previous Design Was Reasonable:** trained router is one cheap forward path、batchable and stateless；top-k expert selection gives predictable compute。
  High-volume/stable distributions and strict latency still favor static routing or periodic router retraining。
- **Changed Constraint:** sparse multimodal experts expose a large oracle routing gap and deployment receives labeled successful examples for adjacent tasks；system can
  spend extra test-time compute to adapt routing without changing base weights。
- **Mechanism:** maintain reference samples on which model is correct plus their routes；embed new task/query，find k-nearest successful references，then either
  optimize route weights against neighbor losses(NGD)、kernel-average neighbor routes plus interpolation search，or mean-shift toward a mode inroute space；experts/base remain frozen。
- **State Ownership:** base/router checkpoint owns initial route；reference corpus owns correctness labels/routes/model revision；embedding/kernel/k ownneighborhood；
  per-request optimizer ownsprovisional route trajectory；expert runtime ownsactual dispatch；scheduler ownsadded FLOP/latency budget；decision trace ownsroute override/reason。
- **Control Flow / Data Flow:** pin model+expert set → build versioned successful-reference index → receive multimodal query → compute initial route/task embedding →
  retrieve neighbors → estimate/iterate route override → execute experts/model → record output/cost → verifier decides whether result may join reference set → expire on model drift。
- **Implementation Details:** evaluated MoAI-7B six experts and MoVA seven experts；reference sets capped5K each，kNN defaultk=5，10 update steps；task embedding/
  Gaussian kernel and fixed cross-benchmark hyperparameters；current code contains MoAI path/configs but no W09 release。
- **Evaluation Contract:** MMBench/MME-P/SQA-IMG/AI2D/TextVQA/GQA/CVBench2D/3D/PhysBench，paired with different 5K reference datasets；
  accuracy/normalized average，oracle uses ground truth；FLOPs measured MoAI-7B MMBench per case，not service latency/goodput。
- **Baselines / Ablations / Sensitivity / Overhead:** base/oracle、mode/kernel/NGD、k and epsilon neighborhoods、kernel types、learning rates、steps、embedding and
  route transition cases；no corrupted/poisoned references、online index update、OOD detection、calibration/abstention、batching/cache effects or end-to-end latency/cost。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/benchmark sizes and per-case theoretical FLOPs disclosed；hardware、precision、
  image resolution/prompt lengths、batch/concurrency、neighbor-index latency/memory and SLO are`Not Disclosed`。NGD 67.5T vs base9.9T FLOPs on one contract。
- **What the Evidence Actually Proves:** for two specific multimodal expert models and matched reference/evaluation tasks，local route adaptation can recover part of
  oracle gap without weight updates；route is a useful runtime control variable distinct from trained parameters。
- **What It Does Not Prove:** nearby task embeddings imply same optimal expert，NGD is efficient online，reference correctness is safe/causal，gains survive
  adversarial/new domains or router retraining，or larger benchmark accuracy offsets 6–7× per-case compute in production。
- **Limitations / Threats to Validity:** only two architectures sharing specialist-expert pattern、curated labeled references、oracle-informed research design、
  no wall-clock/hardware/seed uncertainty、fixed benchmarks may overlap skills、neighbor label quality assumed、current code drift and no security/privacy analysis。
- **Trade-offs / New Failure Modes:** runtime adaptation avoids checkpoint mutation but adds reference index、per-requestoptimization and tail latency；wrong/poisoned
  neighbor routes amplify errors；route overridesfragment batches and caches；model revision invalidates stored routes；successful-only reference set creates selection bias。
- **Where the Previous Design Still Applies:** static router for regular/high-throughput traffic；periodic retraining for stable new domain；deterministic task-to-expert
  policy when schema known；dense fusion whenexpert selection risk exceeds compute；human/verified routing for high-stakes modality use。
- **Evolution Relationship:** `Direct Evolution`：trained global router → per-task expert routing → test-time route search using verified neighbors → online governed
  route memory。It changes control-plane state，not expert capacity。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Current Ch23；Legacy N/A）主 owner；handoff到`MODEL-MOE`、
  `INFER-RESOURCE-SCHEDULING`、`PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch21 routing/capacity/dispatch、Ch23 modality-specific encoders/fusion identity、Ch56 scheduling and Ch66 evidence；
  route override belongs representation fusion but creates runtime scheduling/security contracts。
- **Existing Coverage:** Ch21/23 already distinguish router objective from executable dispatch and modality fusion；R2-T2 can refine route-as-versioned runtime state,
  reference provenance and static-vs-adaptive coexistence，not create a benchmark subsection。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / High Test-time FLOP Cost`。
- **Changed Files or Rejection Reason:** this pass updates Weekly only；Books untouched；current code not treated as event-time artifact。
- **Open Questions:** W09 commit、reference provenance/poisoning/privacy、route cache/index freshness、OOD/no-neighbor abstention、batch fragmentation、wall-clock/
  goodput、online feedback loop、other MoE types and independent reproduction。

### Self-rewarding Correction: A Model Can Learn a Verify–Revise Protocol, but Its Verdict Is Correlated Evidence

- **Candidate / Week / Score:** Self-rewarding correction for mathematical reasoning / 2025-W09 / 28/30。
- **Source Family ID:** `self-rewarding-verify-revise-math-rlvr`。
- **Source Type:** arXiv v1 + public SFT/DPO/PPO/evaluation recipes and datasets；experimental math self-correction training。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-26，current only one paper version；continuous RLHFlow repository has no immutable
  W09 release，so recipe state is later lineage。
- **Direct Primary Sources:** https://arxiv.org/html/2502.19613v1；https://arxiv.org/abs/2502.19613；
  https://github.com/RLHFlow/Self-rewarding-reasoning-LLM。
- **Related Primary Sources:** ToRA/SymPy verifier、Qwen2.5-Math/Llama-3 checkpoints、NuminaMath/MATH/GSM8K/OlympiadBench、Axolotl/vLLM/OpenRLHF/VeRL；
  external ORM/gold verifier remain separate evidence owners。
- **Access and Verification Status:** v1 full text、two training stages、multi-turn objectives/data formats、main/Llama/efficiency/distribution ablations、
  training versions and current code checked；paper lacks a dedicated broad limitations section but discusses reward accuracy/capacity/distribution shift。
- **Full-read Coverage:** metadata、self-reward/alignment/correction literature、sequential rejection sampling、tokenized verify/revise protocol、KL-RL/PPO/iterative and
  multi-turn DPO、32K IFT data/20K×8 RL sampling、all math datasets/baselines/turn transitions、reward accuracy/dynamics、two-turn Llama study、data ablations/software details。
- **Original Problem:** intrinsic “please check again” often changes correct answers and cannot know when to stop；external reward model/verifier improves correction but adds
  another inference component。The desired capability is not only solve，but classify own attempt and revise conditionally。
- **Why the Previous Design Was Reasonable:** external verifier/ORM providesindependent signal and clear stop rule；single-pass solve minimizescost and error loops。
  Verifiable/high-stakes tasks or weak self-evaluation still needexternal authority。
- **Changed Constraint:** deployment wants one model to carry generation and evaluation protocol，while training has executable math verifier for self-generated
  trajectories；system can distill verifier-shaped behavior into model then optimize multi-turn transitions。
- **Mechanism:** sequential rejection sampling builds trajectories with initial CoT、`[VERIFY]` verdict、conditional correction and stop；IFT teaches protocol token
  prediction。Stage2 uses rule-based final correctness for PPO/iterative DPO or multi-turn DPO preferences that separately reward correct verdict、successful revision and avoiding
  correct→incorrect transitions；runtime follows verdict-driven two-turn control。
- **State Ownership:** external SymPy/ToRA verifier owns training truth；self-generated dataset owns attempt/verdict/revision lineage；policy checkpoint owns learned
  protocol；runtime transcript ownscurrent attempt/verdict；orchestrator ownsmax turns/stop/rollback；self verdict is sensor，not authority forirreversible action。
- **Control Flow / Data Flow:** sample math prompt → generate attempts → executable verifier labels outcomes → construct balanced sequential trajectories/preferences →
  IFT protocol → RLVR/DPO update → runtime solve → self-evaluate token+reason → deterministic controller decides revise/stop under budget → optional external verification →
  log correct→incorrect and incorrect→correct transitions。
- **Implementation Details:** Qwen2.5-Math-7B base，32K packed8192-token trajectories，global batch32/LR1e-5/cosine/3epochs(best epoch1)；iterative DPO
  LR2e-7,batch32,20K prompts×8 responses/iteration；Llama experiments use Axolotl0.4.1,transformers4.44.1,torch2.1.2,vLLM0.5.4 and up to2048 tokens/turn。
- **Evaluation Contract:** MATH500/GSM8K/OlympiadBench and related math sets；report turn1/turn2 accuracy plus incorrect→correct and correct→incorrect transitions，
  compare intrinsic prompting、gold/external RM、STaR/RAFT、IFT、PPO/iterative DPO/M-DPO；verifier only validates final symbolic answer，not reasoning faithfulness。
- **Baselines / Ablations / Sensitivity / Overhead:** IFT vs prompt/external RM/STaR，PPO vs direct alignment，reward accuracy/learning dynamics，two-turn format，
  balanced vs skewed correction data and preference subsets；no non-math/open-world verifier、adversarial self-verdict、tool/action side effects、long loops、human calibration or
  independent model-family evaluator。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/token/batch/software disclosed；GPU type/count、precision、training GPU-hours、
  rollout concurrency、two-turn latency/KV cost and deployment SLO mostly`Not Disclosed`。
- **What the Evidence Actually Proves:** in verifier-backed math workloads，training explicit verify/revise transitions can reduce harmful indiscriminate correction and
  improve second-turn accuracy relative to intrinsic prompt baselines；protocol behavior can be distilled into same policy model。
- **What It Does Not Prove:** self-verdict is independent/reliable outside math，generated reasoning is faithful，model can detect unknown unknowns，self-reward removes
  need for external verifier in high stakes，multi-turn loops monotonically improve，or integrated model is cheaper end-to-end than external RM under matched batching。
- **Limitations / Threats to Validity:** training truth comes from external rule verifier despite “self-rewarding” runtime label；same model generates/evaluates causing
  correlated errors；reward accuracy below external ORM and drifts with policy；math answer checker incomplete；few model families、format failures、no hardware/seed uncertainty、
  current repo drift and possible train/eval contamination。
- **Trade-offs / New Failure Modes:** one model simplifies serving component count but doubles/extends decode and makescritic failure correlated with proposal；conservative
  verdicts protect correct answers but miss repairable errors；overconfident wrong verdict stops early；iterative correction amplifies prompt/KV/state cost and can oscillate。
- **Where the Previous Design Still Applies:** single pass forlow-cost/high-confidence tasks；external executable verifier for formal answers/code；independent RM/human
  reviewer for semantic/high-risk tasks；workflow-level retry with fresh evidence rather than self-opinion；abstention when no verifier exists。
- **Evolution Relationship:** `Direct Evolution`：intrinsic re-prompt → external reward-guided correction → verifier-generated verify/revise demonstrations →
  RL-trained integrated self-reward protocol → independently calibrated workflow gate。The paper reaches integrated protocol，not independent gate。
- **ROADMAP Node:** `AGENT-REFLECTION`（Current Ch80；Legacy Ch76）主 owner；handoff到`TRAIN-GRPO`、`TRAIN-DPO`、
  `AGENT-WORKFLOW`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch33 RLVR/group reward、Ch34 preference pairs、Ch80 reflection/correlated self-critique、Ch81 durable workflow and
  Ch66 executable verification；confirmed runtime verdict is reflection sensor while training mechanism belongs post-training handoff。
- **Existing Coverage:** Ch80 already distinguishes self-critique from external evidence and tracksrevision loops；this family can refine training-origin/evolution and
  transition metrics，without changing the conclusion that self-evaluation cannot authorize high-risk actions。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Internal Reward Not Independent`。
- **Changed Files or Rejection Reason:** this pass updates Weekly only；Books untouched；current repo not treated as W09 immutable run。
- **Open Questions:** event-time hashes、GPU/precision/cost、self-verdict calibration、non-math tasks、long-loop stability、prompt injection、unknown-unknown abstention、
  independent verifier/human comparison、matched serving cost and reproduction。

### SoRFT: Workflow Decomposition Creates Trainable Intermediate Contracts—but PR Overlap Is Not Execution Truth

- **Candidate / Week / Score:** SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning / 2025-W09 / 27/30。
- **Source Family ID:** `sorft-subtask-rule-reward-software-repair`。
- **Source Type:** arXiv v1 + ACL 2025 paper lineage；experimental SFT+PPO training for Agentless software repair，no official code artifact found。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-27，current only one arXiv version；later ACL publication does not alter W09
  method/evidence boundary。
- **Direct Primary Sources:** https://arxiv.org/html/2502.20127v1；https://arxiv.org/abs/2502.20127；
  https://aclanthology.org/2025.acl-long.559.pdf。
- **Related Primary Sources:** SWE-Bench Verified/Lite、Agentless1.0、Qwen2.5-Coder、SEART GitHub Search、Claude3.5 teacher；resolved PRs provide
  reference changes，while executable tests remain the stronger outcome evidence。
- **Access and Verification Status:** v1 full text、subtask equations/reward algorithm、data construction、SFT/RL setup、SWE-Bench results/reward/data ablations、
  appendices/limitations and ACL lineage checked；no reproducible official training code/checkpoint/release located。
- **Full-read Coverage:** metadata、SWE-Bench/framework/RL background、file/function/line/edit decomposition、rejection-sampled CoT、F-beta PPO reward、660/100 repo
  selection、30K issue-PR/60K SFT/30K RL data、7B/32B Agentless evaluation、hit-reward hacking、general code tests、false-negative/Python limitations and prompts。
- **Original Problem:** end-to-end issue resolution has sparse executable outcome and long action chain；agent trajectories are hard to label at intermediate steps，while
  filtering only successful teacher traces discards negative signal and couples capability to proprietary models。
- **Why the Previous Design Was Reasonable:** end-to-end test reward directly measures patch behavior and supports multiple valid fixes；SFT on successful trajectories is
  simple/stable。When sandbox execution is affordable and agent state isobservable，these remain stronger than syntactic proxies。
- **Changed Constraint:** resolved GitHub PRs expose intermediate locations/edits at scale，and pipeline decomposition makes those states parseable；training can attach
  dense rewards to localization/edit steps before the final test harness。
- **Mechanism:** decompose Agentless into file→function→line localization→Search/Replace edit；teacher generates CoT and samples with no ground-truth overlap are rejected
  for SFT。PPO then replaceslearned RM with per-subtask F-beta overlap reward(β=3 recall-weighted)，plus validity checks preventing nonexistenttargets；same policy learns all stages。
- **State Ownership:** issue/repo revision ownsinput；merged PR ownsone reference patch，not unique truth；workflow stage owns typed target；reward parser/F-beta ownsproxy；
  policy/old/reference checkpoints ownPPO state；sandbox tests own executable acceptance；framework version owns prompt/context/tool semantics。
- **Control Flow / Data Flow:** select licensed repos excluding SWE-Bench → bind issue+PR revision → derive stage ground truths → teacher samples CoT → rejection filter →
  SFT format/stage behavior → PPO rollouts per stage → parse targets/compute F-beta → update policy → run Agentless pipeline on fixed repo → apply patch → tests decide resolution。
- **Implementation Details:** 660 candidate Python repos，100 for teacher data；30K issue-PR pairs produce60K SFT rows，30K RL rows；Qwen2.5-Coder7B/32B and
  Agentless1.0；training hardware、precision、PPO rollout/batch/KL/checkpoint details not sufficiently disclosed in v1。
- **Evaluation Contract:** SWE-Bench Verified500 and Lite300 Python issues；%Applied and executable %Resolved；compare base/SFT/SFT+RL within Agentless and published
  framework-specific models。Subtask hit rates and same-data 90K SFT ablation supplement end-to-end tests。
- **Baselines / Ablations / Sensitivity / Overhead:** base/SFT/SFT+RL、hit reward vsF-beta reward hacking、60K vs90K SFT、subtask localization；no direct
  end-to-end executable reward training、β sensitivity、multi-language repos、new framework/tool prompts、teacher-free data、multiple seeds/confidence/cost or contamination audit beyond repo exclusion。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 7B/32B models/data counts disclosed；GPU/hardware、precision、sequence lengths、
  batches、rollout concurrency、training wall time/cost and repair SLO are`Not Disclosed`。
- **What the Evidence Actually Proves:** in Agentless/Python SWE-Bench setting，stage-typed supervision plus rule PPO improves apply/resolve rates over same framework’s
  base/SFT models；reward granularity matters and an overly permissive hit proxy is exploitable。
- **What It Does Not Prove:** F-beta corresponds tocorrect repair，PR patch is unique ground truth，CoT is faithful，SoRFT generalizes tointeractive agents/languages，
  SFT “poor generalization” is causal，or framework/model cross-comparisons isolate training method。
- **Limitations / Threats to Validity:** authors note valid alternative fixes become false negatives and only Python tested；framework-specific prompts、teacher bias、
  issue/PR temporal leakage、syntactic overlap proxy、no official artifact、single benchmark ecosystem、unknown seeds/hardware and reward parser attack surface。
- **Trade-offs / New Failure Modes:** decomposition yields dense attribution and easier training but freezes one workflow and propagates early localization error；PR overlap
  is cheap but discourages valid alternative code；recall-heavy reward encourages broad targets；pipeline state is auditable yet less adaptive than tool agent；proxy optimization can
  improve `%Applied` without semantic correctness。
- **Where the Previous Design Still Applies:** executable unit/integration tests for outcome truth；end-to-end agent RL when environment feedback is available；SFT for
  stable formats；human review for ambiguous fixes；retrieval/static analysis for deterministic localization；different workflow decomposition for other repositories。
- **Evolution Relationship:** `Layering / Dependency`：end-to-end patch/test → pipeline decomposition → derived intermediate labels → rejection SFT → rule-based PPO →
  executable final verification。Intermediate reward densifies learning but does not replace final test authority。
- **ROADMAP Node:** `TRAIN-PPO`（Current Ch32；Legacy Ch28）主 owner；handoff到`AGENT-WORKFLOW`、`AGENT-PLATFORM`、
  `PLATFORM-EVALUATION-SYSTEM`与`TRAIN-DATA`。
- **Target and Adjacent Chapters Read:** 已读Ch32 reward/ratio/proxy state、Ch81 workflow durable stages、Ch84 agent environment and Ch66 executable evidence；
  confirms training proxy and final sandbox outcome have distinct owners。
- **Existing Coverage:** Books already covers verifier-based RL and workflow artifacts；SoRFT can refine stage-derived reward evolution and proxy/executable hierarchy，
  without preserving leaderboard/model names。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Proxy Reward False Negatives`。
- **Changed Files or Rejection Reason:** this pass updates Weekly only；Books untouched；absence of official code/checkpoint is explicit。
- **Open Questions:** official event-time code/data/checkpoint、PR license/temporal leakage、β/alternative patch handling、test-execution reward、other languages/frameworks、
  hardware/cost、multi-seed evaluation and independent reproduction。

### UniTok: Unified Objectives Need More Representation Capacity, Not Merely a Shared Token ID Space

- **Candidate / Week / Score:** UniTok: A Unified Tokenizer for Visual Generation and Understanding / 2025-W09 / 28/30。
- **Source Family ID:** `unitok-multi-codebook-unified-visual-tokenization`。
- **Source Type:** arXiv v1 + code/model/project release on2025-02-28；experimental discrete visual tokenizer and unified autoregressive MLLM。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-27，current only one arXiv version；paper/code/model project release2025-02-28 is a
  separate artifact event。Later April/May checkpoints and NeurIPS changes are not W09 evidence。
- **Direct Primary Sources:** https://arxiv.org/html/2502.20321v1；https://arxiv.org/abs/2502.20321；
  https://github.com/FoundationVision/UniTok；https://huggingface.co/FoundationVision/unitok_tokenizer。
- **Related Primary Sources:** DataComp-1B、ViTamin、DINOv2-S discriminator、Llama2-7B/Liquid unified MLLM and internal/synthetic generation data；
  internal30M MidJourney-style data limits full reproduction。
- **Access and Verification Status:** v1 full text、loss/capacity mechanism、tokenizer/MLLM setup、understanding/generation/reconstruction ablations、appendices and
  current code/model card checked；later repository updates clearly separated from event-time artifact。
- **Full-read Coverage:** metadata、generation/understanding/unified tokenizer related work、CLIP+VQVAE objectives、single-codebook bottleneck、multi-codebook VQ、
  attention factorization、unified MLLM、1.28B tokenizer training/70M MLLM mix、ImageNet/LLaVA/GenEval/FID、codebook/loss/CLIP-init ablations、one-epoch limitation/artifact。
- **Original Problem:** generation needs fine-grained invertiblevisual detail，understanding needssemantic alignment；one discrete code per patch with limited codebook capacity
  forces objectives tocompete and large monolithic codebooks becomeunstable/underused。
- **Why the Previous Design Was Reasonable:** separate VAE and CLIP encoders specialize each objective and can upgrade independently；continuous features avoid
  quantization loss。When unified token stream is unnecessary or quality/safety domains differ，dual encoders remain cleaner。
- **Changed Constraint:** unified autoregressive MLLM wants a common discrete interface for image input/output，but must carry both local reconstruction and global semantics
  without multiplying token sequence length or using an unmanageably large single codebook。
- **Mechanism:** train ViTamin hybrid tokenizer with CLIP-style semantic contrastive loss plus VQ reconstruction/perceptual/GAN losses；split 64-d latent intoeight independent
  8-d subspaces，each quantized by4096-entry codebook，forming a tuple token with combinatorial capacity。Attention-based factorization lets one Transformer predict codebook
  components without expanding spatial sequence eightfold；same tokens feed understanding and AR generation。
- **State Ownership:** tokenizer revision owns image↔tuple-code contract；each sub-codebook ownscomponent identity；encoder/decoder and loss mix ownrepresentation；
  MLLM checkpoint owns semantics over codes；artifact bundle must bind all codebooks/order/dimensions；runtime cannot swap tokenizer or codebook independently。
- **Control Flow / Data Flow:** image → hybrid encoder → split latent subspaces → nearest entry in each codebook → tuple codes per patch → MLLM attention factorization →
  understand text or autoregressively predictvisual tuple → decoder reconstructs image → evaluate semantic and reconstruction slices under same tokenizer revision。
- **Implementation Details:** eight4096-entry/8-d codebooks(global64-d)，ViTamin-L/16，DINOv2-S discriminator；tokenizer one epoch on1.28B DataComp pairs at256²,
  global batch16K，LR1e-3 tokenizer/2e-4 discriminator；unified MLLM Llama2-7B with10M text、30M internal synthetic and30M recaptioned pairs。
- **Evaluation Contract:** ImageNet rFID and zero-shot accuracy；LLaVA-style visual understanding tasks；GenEval/GenAI-Bench and image generation FID；compare specialized/
  unified discrete/continuous tokenizers，CLIP/random init，loss combinations，codebook count/size and attention factorization。Hardware/serving contract not fully disclosed。
- **Baselines / Ablations / Sensitivity / Overhead:** single vsmulti-codebook、codebook size/count、semantic/reconstruction losses、CLIP initialization、factorization；
  no matched total-data/hardware across proprietary baselines、longer tokenizer schedule、video/high-resolution/robustness、codebook drift/version migration or production codec cost。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** models/data/resolution/global batch disclosed；GPU type/count、precision、training GPU-hours、
  tokenization/decoding latency、memory/bandwidth、batch/concurrency and SLO are`Not Disclosed`。
- **What the Evidence Actually Proves:** in authors’ training/evaluation contract，increasing discrete representation capacity through factorized codebooks reduces the
  observed reconstruction/semantic compromise and supports one tokenizer in both generation and understanding；objective conflict can partly originate at bottleneck capacity。
- **What It Does Not Prove:** objectives never conflict，tuple code is universally better，ImageNet accuracy predictsVQA，unified tokenizer beats dual encoders under
  matched compute/data，internal data is reproducible，or unified interface simplifies deployment lifecycle overall。
- **Limitations / Threats to Validity:** one-epoch tokenizer undertrains semantics；30M internal synthetic data；large mixed dataset/licensing/contamination；
  sequential benchmark differences、no independent reproduction、later checkpoint changes architecture、tuple identity/version coupling and no operational measurement。
- **Trade-offs / New Failure Modes:** factorized codebooks expand capacity without spatial token growth but multiply lookup/output heads and create tuple-order compatibility；
  shared tokenizer reduces modality handoff yet couples generation/understanding releases；semantic loss may suppress detail and reconstruction loss may preserve nuisance features；
  dead/imbalanced sub-codebooks can waste capacity。
- **Where the Previous Design Still Applies:** separate CLIP/VAE forindependent quality and upgrade；continuous encoder for perception-only workloads；single codebook for
  small/simple images；modality-specific codec whenlatency/precision/safety contracts differ；explicit adapter between representations for fault isolation。
- **Evolution Relationship:** `Direct Evolution`：specialized continuous/discrete encoders → joint single-codebook tokenizer → capacity-expanded multi-codebook tuple →
  attention-factorized unified MLLM。Unification trades interface translation for artifact coupling。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Current Ch23；Legacy N/A）主 owner；handoff到
  `MULTIMODAL-GENERATIVE-PARADIGMS`、`MODEL-TOKENIZER`、`PLATFORM-ARTIFACT-MANAGEMENT`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch23 modality/token/codec identity、Ch24 generation factorization、Ch11 tokenizer interface and Ch58 artifact lineage；
  confirms multi-codebook is representation owner，not a generic text tokenizer change。
- **Existing Coverage:** Ch23 already explains shared token space and modality-specific codecs，but can refine“capacity bottleneck masquerades as objective conflict” and
  tuple-code artifact coupling；no product/benchmark list needed。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；keep mechanism/evolution，drop SOTA metrics and later checkpoint claims。
- **Changed Files or Rejection Reason:** this pass updates Weekly only；Books untouched；April/May/NeurIPS updates not backdated。
- **Open Questions:** event-time hashes/data/license、hardware/precision/cost、sub-codebook utilization、longer schedule、high-resolution/video、matched dual-encoder
  baseline、version migration/rollback、serving latency and independent reproduction。

### EDGS: Separate Static State from Dynamic Updates before Paying Temporal Compute Everywhere

- **Candidate / Week / Score:** Efficient Gaussian Splatting for Monocular Dynamic Scene Rendering via Sparse Time-Variant Attribute Modeling / 2025-W09 / 23/30。
- **Source Family ID:** `edgs-static-dynamic-sparse-gaussian-state`。
- **Source Type:** arXiv v1/AAAI 2025 experimental dynamic-scene rendering method；no official code artifact located。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-27，current only one version；AAAI proceedings publication2025-04-11 islater
  formal-publication lineage，not a new W09 event。
- **Direct Primary Sources:** https://arxiv.org/html/2502.20378v1；https://arxiv.org/abs/2502.20378；
  https://ojs.aaai.org/index.php/AAAI/article/view/32460。
- **Related Primary Sources:** NeRF-DS/HyperNeRF datasets、3DGS/Deformable-3DGS/4DGS/SCGS/Scaffold-GS baselines and COLMAP；no public EDGS code/model found。
- **Access and Verification Status:** v1 full text/equations、anchor/time-mask/RBF mechanism、datasets/baselines/results/ablation and AAAI record checked；
  no appendix/artifact beyond paper and no dedicated limitations section。
- **Full-read Coverage:** metadata、dynamic 3DGS/grid background、SfM anchor initialization、attribute split、RBF offset、unsupervised time mask、densify/prune/loss、
  NeRF-DS/HyperNeRF metrics/FPS/VRAM、anchor/mask/RBF/KNN/cosine ablations、visualizations/conclusion and publication lineage。
- **Original Problem:** deformable 3DGS queries temporal MLP attributes for every dense Gaussian，including static background；densification increasespoints、slows
  rendering and may introduce static-region jitter even though only a subset actually changes over time。
- **Why the Previous Design Was Reasonable:** one deformation field over all Gaussians is simple and avoids misclassifying static/dynamic regions；dense points maximize
  reconstruction flexibility。Small scenes、offline rendering or highly non-rigid motion can justify the dense path。
- **Changed Constraint:** real-time dynamic rendering ispoint-count/MLP-query bound and most scene state is time invariant；representation should allocate temporal compute only
  where observed motion warrants it while retaining dense rendered detail。
- **Mechanism:** voxelize COLMAP points into sparse frozen anchors；tiny MLPs decode invariant color/opacity and time-varying scale/rotation。An unsupervised time-mask
  gates static anchors away from deformation MLP；deform anchor motion once and use feature-space RBF to scale each attached Gaussian offset，plus gradient densification and
  opacity pruning。
- **State Ownership:** source video/camera poses own observations；frozen anchor grid owns canonical spatial state；time mask ownsmutable/static classification；anchor
  feature owns local semantics；deformation MLP owns time transition proposal；attached Gaussian offsets ownrender detail；rasterizer owns pixels，not physical truth。
- **Control Flow / Data Flow:** monocular frames+poses → COLMAP points → voxel anchor grid → decode static attributes → classify temporal anchors → query deformation only
  fordynamic anchors/time → RBF propagate anchor movement to offsets → splat image → compare frame loss → densify/prune anchors → render novel time/view。
- **Implementation Details:** voxel anchor grid、K offsets/anchor、RBF sigma1、L1+SSIM+time-mask regularization each lambda0.2；anchor positions frozen，gradients
  accumulated100 iterations for densification。Exact training steps/hardware depend paper setup and are not fully exposed in available HTML。
- **Evaluation Contract:** monocular real-world NeRF-DS and HyperNeRF/VRIG scenes；PSNR/SSIM/MS-SSIM/LPIPS、FPS、Gaussian count/storage/VRAM；compare
  NeRF/static/dynamic Gaussian methods。Image rendering metrics and FPS do not measure action-conditioned state prediction。
- **Baselines / Ablations / Sensitivity / Overhead:** anchor-grid/time-mask removal、rigid/KNN/cosine/RBF offsets、visual mask/features；no static/dynamic ground-truth
  segmentation、collision/contact/action intervention、long-horizon drift、camera/calibration noise、different resolution hardware normalization or independent reproduction。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** resolution/FPS tables appear but device、precision、batch、training time、memory traffic and
  complete latency/SLO contract are not consistently disclosed，so speed numbers cannot be generalized。
- **What the Evidence Actually Proves:** in two rendering datasets，factoring mostly static anchor state from sparse time-varying updates can reduce temporal MLP work/
  point redundancy while preserving authors’ view-synthesis metrics；state mutability is a useful representation axis。
- **What It Does Not Prove:** learned mask identifiesphysical objects，RBF models causal dynamics，rendered scene is a controllableworld model，FPS transfers across
  hardware/resolution，or sparse temporal state supports planning/robotics。
- **Limitations / Threats to Validity:** no explicit limitations/artifact、few curated scenes、render metrics favor appearance、unsupervised mask can leak motion/camera effects、
  RBF sigma fixed、COLMAP/pose dependency、occlusion/new topology/collision not evaluated and no uncertainty/seed reporting。
- **Trade-offs / New Failure Modes:** sparse temporal updates save work and stabilize background but wrong static mask freezes real motion；anchor factorization compressesstate
  yet may smear non-rigid detail；RBF is cheap/local but feature similarity need not equal motion coupling；densification can reintroducepoint growth。
- **Where the Previous Design Still Applies:** dense deformation forsmall/offline/highly dynamic scenes；explicit simulator forcausal/action state；standard3DGS for static
  scenes；multi-state sensor/mesh model forinteraction；human/geometry constraints where mask errors matter。
- **Evolution Relationship:** `Principle Reuse`：dense time-varying state → anchor-factorized state → static/dynamic separation → sparse temporal updates。It is a rendering
  representation evolution，not evidence that video generation became a world model。
- **ROADMAP Node:** `MULTIMODAL-WORLD-MODELS`（Current Ch25；Legacy N/A）主 owner；handoff到
  `MULTIMODAL-GENERATIVE-PARADIGMS`、`MULTIMODAL-EMBODIED-VLA`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch24 video generation/state cost、Ch25 observed/latent/action-conditioned state and static/dynamic memory，Ch26 physical
  control；current Books already separates visual plausibility from causalworld state。
- **Existing Coverage:** Ch25 explicitly contains static/dynamic separated memory and warns rendering quality≠control sufficiency；EDGS is a concrete rendering case but
  adds no new long-term mechanism beyond existing principle。
- **Integration Decision:** `Books Pending — No Change Candidate / Rendering Evidence Only`。
- **Changed Files or Rejection Reason:** this pass updates Weekly only；Books untouched；no public code/model and no speed extrapolation。
- **Open Questions:** code/config/hardware、mask calibration、camera-motion confound、dynamic topology/collision、long-horizon drift、action conditioning、matched FPS/
  quality frontier and independent reproduction。

### FINEREASON: Final Accuracy Hides Whether a Model Can Check State, Transition, or Backtrack

- **Candidate / Week / Score:** FINEREASON: Evaluating and Improving LLMs' Deliberate Reasoning through Reflective Puzzle Solving / 2025-W09 / 27/30。
- **Source Family ID:** `finereason-state-check-transition-reflection-benchmark`。
- **Source Type:** arXiv v1 + later ACL 2025 code/data artifact；fine-grained reasoning evaluation and GRPO transfer study。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-27；later revisions/ACL publication and current repository are lineage only。W09 locks
  v1 benchmark/training claims。
- **Direct Primary Sources:** https://arxiv.org/html/2502.20238v1；https://arxiv.org/abs/2502.20238；
  https://github.com/DAMO-NLP-SG/FineReason；https://aclanthology.org/2025.acl-long.333.pdf。
- **Related Primary Sources:** Sudoku/Kaggle、Graph Coloring generator、Game of24、Grid Puzzle data、MetaMathQA、OpenR1/GRPO and evaluated model APIs；
  each API/model revision remains part of EvalRun identity。
- **Access and Verification Status:** v1 full text/appendices、tree construction、state tasks、all model/error/difficulty analyses、GRPO mix/ratio/scale/hardware and
  current code lineage checked；event-time immutable repo not available。
- **Full-read Coverage:** metadata、four puzzle types/minimal moves/DFS/executable rules、state checking/transition prompts、2K+2K eval construction、models and metrics、
  solvable/unsolvable/transition errors、difficulty、10K puzzle+15K math GRPO pool、mix/scale ablations、8×H20 config、limitations/artifact。
- **Original Problem:** final-answer accuracy conflates planning、constraint checking、forward moves and backtracking；a model can luckily reach answer or fail after one
  local error，so aggregate score cannot identify which state transition mechanism is missing。
- **Why the Previous Design Was Reasonable:** end-to-end tasks best represent user outcome and avoid artificial intermediate labels；CoT/manual grading is flexible。
  Open-ended domains without executable state semantics still require outcome/human evaluation。
- **Changed Constraint:** logic puzzles offer fully enumerable/validatable state trees and minimal reversible actions，allowing evaluation/training at atomicstate boundaries rather
  than treating generated rationale text as truth。
- **Mechanism:** translate puzzle rules to executable validators and DFS full search tree；each node isstate，edge is one minimal add/remove operation。State Checking predicts
  whether anysolution exists below current node；State Transition must choose unvisited child when solvable or exactly parent when dead。Training mixes puzzle state tasks with math
  prompts under rule-verifiable GRPO。
- **State Ownership:** puzzle generator/version ownroot/rules；executable solver owns solvability and parent/child truth；history ownvisited states；model ownsproposal；
  evaluator ownsstate-check/transition/error taxonomy；GRPO run ownsreward/data mix；final answer remainsseparate outcome metric。
- **Control Flow / Data Flow:** construct puzzle → enumerate DFS tree → sample depth-balanced solvable/unsolvable states → package rules/history/current state/bad children →
  model check state → propose minimal transition → executable validator labels class/error → aggregate slices → mix state tasks with math → GRPO → retest held-out state and math outcomes。
- **Implementation Details:** 500 states/category yield2000 State Checking and2000 State Transition cases；Grid has94 solvable/406 unsolvable imbalance；training pool10K
  puzzle+15K MetaMath，GRPO on1.5B/7B distilled models，LR4e-5,warmup0.1,batch112,max1024+1024,1epoch,8×H20-120GB(one vLLM GPU)。
- **Evaluation Contract:** Sudoku/Graph Coloring/Game24/Grid；zero-shot CoT with no-programming instruction；state-check accuracy/precision/recall/F1，transition exact
  minimal move and errors(Multiple/Invalid/Unsolvable child/Backtrack/Sibling)，difficulty slices and final puzzles；math transfer GSM8K/MATH under mix ratios/scales。
- **Baselines / Ablations / Sensitivity / Overhead:** general/reasoning proprietary/open models、solvable vsunsolvable、ground-truth checking forisolating transition、
  difficulty/error types、math:puzzle0.4–1.0 and2K–12.5K training scale；no multiple seeds/confidence、program/tool-enabled agents、representation formats beyond text tables、
  cross-domain planning/control or contamination/solver-bug audit。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** training hardware/model/length/batch disclosed；precision、evaluation API settings/cost、
  sampling temperature、training wall time、inference concurrency/latency and SLO incomplete。
- **What the Evidence Actually Proves:** under four executable puzzle systems，state checking and state transition are separable capabilities and backtracking/unsolvable
  transitions are common failure slices；adding verifier-backed puzzle data improves authors’ math benchmarks over matched math-only training in selected models/runs。
- **What It Does Not Prove:** textual CoT reflectsinternal computation，puzzle transfer is broad “System2” ability，single best mix ratio generalizes，training gain is
  seed-stable，state checking predicts real-world uncertainty，or final-answer benchmark should be replaced by atomic tests。
- **Limitations / Threats to Validity:** synthetic/small puzzle families、Grid imbalance、text-table/zero-shot prompt choice、solver/generated-state artifacts、no seeds/error
  bars、API version drift、possible math contamination、short1024 completion and later repo/paper drift。
- **Trade-offs / New Failure Modes:** atomic evaluation improves diagnosis and reward density but narrows task ontology；full-tree enumeration is infeasible foropen worlds；
  oracle checking can leak privileged state if inserted at runtime；training on minimal moves may overfit format and penalize validmacro actions；more backtracking skill costs steps/tokens。
- **Where the Previous Design Still Applies:** end-to-end outcome forreal utility；external planner/simulator forhuge state spaces；human evaluation forsemantic transitions；
  process supervision when states cannot beformalized；tool execution forcode/math and abstention when uncertainty cannot be enumerated。
- **Evolution Relationship:** `Direct Evolution` of evidence：final answer → static process labels → executable state checking → typed transition/backtracking errors →
  verifier-backed curriculum。Atomic metrics complement，not replace，end outcome。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Current Ch66；Legacy Ch62）主 owner；handoff到`AGENT-REFLECTION`、
  `AGENT-PLANNING`、`AGENT-WORKFLOW`与`TRAIN-GRPO`。
- **Target and Adjacent Chapters Read:** 已读Ch66 subject/state/transition/evidence taxonomy、Ch79 planning、Ch80 reflection/backtracking、Ch81 workflow and
  Ch33 verifier RL；confirmed benchmark owns diagnostic contract，not universal reasoning theory。
- **Existing Coverage:** Books already distinguishes final artifact from intermediate/executable evidence；FINEREASON can refine state-transition error taxonomy and
  privileged-oracle boundary，without preserving model leaderboard。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。
- **Changed Files or Rejection Reason:** this pass updates Weekly only；Books untouched；current code/ACL publication not backdated。
- **Open Questions:** event-time hash、solver correctness、seed variance、tool-enabled baseline、other state representations/domains、open-world approximation、
  mix-ratio stability、API revision/cost and independent reproduction。

### FlexiDiT: Diffusion Compute Should Follow Denoising Phase, Not Stay Uniform by Habit

- **Candidate / Week / Score:** FlexiDiT: Your Diffusion Transformer Can Easily Generate High-Quality Samples with Less Compute / 2025-W09 / 28/30。
- **Source Family ID:** `flexidit-phase-aware-patch-compute-scheduling`。
- **Source Type:** arXiv v1/CVPR 2025 experimental diffusion-Transformer adaptation；no official public code artifact located。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-27，current only one version；later CVPR proceedings is formal-publication lineage。
- **Direct Primary Sources:** https://arxiv.org/html/2502.20126v1；https://arxiv.org/abs/2502.20126；
  https://openaccess.thecvf.com/content/CVPR2025/papers/Anagnostidis_FlexiDiT_Your_Diffusion_Transformer_Can_Easily_Generate_High-Quality_Samples_with_CVPR_2025_paper.pdf。
- **Related Primary Sources:** DiT-XL/2、text-image Transformers/Emu/video DiT and ImageNet/COCO/generation benchmarks；proprietary base models/data limit reproduction。
- **Access and Verification Status:** v1 full text、shared/LoRA adaptation、scheduler/guidance、image/text/video experiments、FLOPs-latency、exposure bias/packing/
  attention analyses、implementation/human evaluation appendices checked；no code/release/model artifact found。
- **Full-read Coverage:** metadata、diffusion/DiT compute background、multi-patch embedding/de-embedding、shared-parameter vsLoRA modes、weak/powerful scheduler、CFG
  guidance、class/text/video datasets/solvers/steps/FID/CLIP/human/latency、caching and exposure bias、fine-tuning data/compute/implementation details。
- **Original Problem:** a monolithic DiT spends the same token count/model capacity at every denoising step，although early high-noise steps mainly establishlow-frequency
  structure while later steps refine detail；uniform compute ignores phase-specific value of resolution。
- **Why the Previous Design Was Reasonable:** fixed patch/model keeps one compiled graph、simple batching and stable semantics across all steps；separate cascades can
  specialize phases explicitly。Small models、few steps or graph-capture-heavy serving may prefer uniform execution。
- **Changed Constraint:** high-resolution image/video attention cost scales with token count and repeated denoising NFEs；a pretrained model should support multiple compute
  modes without storing full independent denoisers or losing shared knowledge。
- **Mechanism:** add larger-patch embedding/de-embedding so same Transformer processes fewer tokens in weak mode；fine-tune shared parameters or patch-specific LoRAs to
  align weak/powerful predictions。Scheduler uses weak coarse mode for early steps and powerful small patches later；conditional/unconditional CFG paths may use different modes，
  and training exposes powerful model to weak-generated states to correct accumulated error。
- **State Ownership:** base checkpoint owns powerful semantics；patch adapters/LoRAs own alternate tokenization contract；scheduler owns timestep→mode policy；solver/CFG
  own denoising/control states；request owns current latent/step；runtime owns graph/memory/latency and must include mode sequence in artifact/run identity。
- **Control Flow / Data Flow:** load base+flex adapters → initialize noise → for each solver timestep choose patch mode/CFG modes → tokenize latent at selected granularity →
  shared DiT predicts update → detokenize same latent space → advance solver → switch to powerful mode near detail phase → decode image/video → evaluate quality andactual latency。
- **Implementation Details:** common powerful patch2→weak patch4 setup；new embed/de-embed plus shared weights or per-sequence LoRA；fine-tuning reported<5% original
  pretraining compute and sometimes<5K images。Class-conditioned DDPM250 and alternate DPM/SA solvers plus image/video modes；exact proprietary setup varies by model。
- **Evaluation Contract:** ImageNet class generation、COCO/text-to-image、Emu and text-to-video；FID/sFID/IS/precision/recall/CLIP/human preference，FLOPs and measured
  latency on disclosed experiment setups；schedulers varyweak-step proportion and CFG scale，not a production multi-tenant goodput test。
- **Baselines / Ablations / Sensitivity / Overhead:** static powerful/weak、shared vsLoRA、patch schedule/direction、solver/step counts、CFG modes、weak-step count、
  caching distance、attention/prediction alignment、training data size；no adversarial prompts/safety regression、dynamic per-sample controller、batch mixture/graph overhead、
  memory residency or independent reproduction。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** paper reports FLOPs/latency for multiple models but complete hardware/precision/batch/compile/
  concurrency/SLO contract is not uniform；headline compute reductions cannot be treated as universal wall-clock savings。
- **What the Evidence Actually Proves:** in authors’ image/video DiT settings，phase-dependent patch-token count can trace a quality–compute frontier after limited adaptation；
  denoising steps need not share identical compute，and shared model modes can retain knowledge better than isolated models。
- **What It Does Not Prove:** early steps always needless compute，quality is unchanged across prompts/safety slices，FLOPs map tolatency/goodput，dynamic scheduler works
  without retraining，or technique transfers totext diffusion/online serving under mixed batches。
- **Limitations / Threats to Validity:** no official artifact、some proprietary models/data、quality metrics/human studies limited、scheduler chosen offline、no seed/
  confidence and safety/fairness regression；larger patch may erase small early structures that later steps cannot recover。
- **Trade-offs / New Failure Modes:** weak early mode savesattention but adds adapters、mode-switch/cache/graph complexity；shared weights transfer knowledge yet couple
  modes；LoRAs isolate tokenization but increase artifact combinations；wrong switch boundary produces irreversible coarse error；heterogeneous schedules fragment batches。
- **Where the Previous Design Still Applies:** uniform DiT forsimple/low-step/batched pipelines；separate cascades for independent specialization；distillation/consistency
  model when reducing number of steps is primary；static resolution when small object fidelity/safety requires consistent high detail。
- **Evolution Relationship:** `Direct Evolution`：uniform model per step → separate phase experts/cascades → one multi-patch model → phase-aware weak/powerful schedule →
  future request-adaptive compute controller。It reallocates compute; it does not remove denoising/state cost。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Current Ch24；Legacy N/A）主 owner；handoff到
  `MULTIMODAL-REPRESENTATION`、`INFER-EXECUTION-ENGINE`、`INFER-RESOURCE-SCHEDULING`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch23 token/patch identity、Ch24 diffusion schedule/cost/commit、Ch50 execution engine and Ch56 scheduling；
  confirms this is generation-phase compute policy with serving handoff。
- **Existing Coverage:** Ch24 already compares diffusion steps and mutable generation，but lacks explicit“timestep value→token granularity→runtime schedule” chain；
  FlexiDiT can refine it without retaining vendor benchmarks。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。
- **Changed Files or Rejection Reason:** this pass updates Weekly only；Books untouched；no code/model and no generic speed claim。
- **Open Questions:** official artifact、hardware/precision/latency contract、dynamic per-sample controller、batching/graph cache、safety/detail slices、adapter migration、
  high-resolution/video reproduction and independence from solver/CFG tuning。

### MedVLM-R1 v1: Outcome Reward Can Improve Closed-Set Transfer while Producing Unfaithful Explanations

- **Candidate / Week / Score:** MedVLM-R1: Incentivizing Medical Reasoning Capability of VLMs via Reinforcement Learning / 2025-W09 / 25/30。
- **Source Family ID:** `medvlm-r1-medical-vqa-grpo-format-outcome-reward`。
- **Source Type:** arXiv v1 experimental proof-of-concept + later MICCAI/code/model lineage；high-stakes closed-set radiology VQA。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-26；v2 2025-03-19 and MICCAI2025 later revise publication；current one-commit repo/
  HF model are later artifacts。W09 locks v1 paper/results and code absence at event time。
- **Direct Primary Sources:** https://arxiv.org/html/2502.19634v1；https://arxiv.org/abs/2502.19634；
  later lineage https://github.com/JZPeterPan/MedVLM-R1 and https://huggingface.co/JZPeterPan/MedVLM-R1。
- **Related Primary Sources:** Qwen2-VL-2B、HuatuoGPT-Vision/VQA source datasets、open-r1-multimodal/R1-V frameworks and later MICCAI record；
  none turns model output into clinical diagnosis evidence。
- **Access and Verification Status:** v1 full text、GRPO/reward/data/setup/baselines/results/reasoning examples/limitations checked；current code/model/failure cases and
  MICCAI review lineage checked separately，no immutable W09 artifact。
- **Full-read Coverage:** metadata/revisions、medical VLM/RL background、prompt/tags、GRPO objective、format+answer reward、17.3K source pool/600 MRI train/
  300×3 tests、2×A100 setup、zero-shot/medical/SFT baselines、ID/OOD result、reasoning faithfulness failures、modality/open-set limitations and artifacts。
- **Original Problem:** medical VLM SFT needs many image-text pairs and may overfit one modality；final-answer supervision offers no explicit rationale，but clinicians require
  evidence and calibrated uncertainty—not merely a multiple-choice letter。
- **Why the Previous Design Was Reasonable:** SFT on curated clinician rationales gives controlled terminology/provenance；classification VLM without free rationale avoids
  persuasive hallucination。Forclinical use，expert supervision and validated decision support remainnecessary。
- **Changed Constraint:** only600 MRI labels are available and authors seek MRI→CT/X-ray transfer plus structured reasoning output；group sampling can exploit cheap exact-choice
  reward without a learned critic/rationale reference。
- **Mechanism:** Qwen2-VL-2B samplesG=6 outputs per image/question；GRPO normalizes total reward within group and applies clipped ratio+KL to initial reference。
  Reward gives1 for exact `<think>/<answer>` structure and0/0.5/1 for missing/partial/exact multiple-choice answer；no reward checks medical reasoning content or image grounding。
- **State Ownership:** medical dataset owns image/choice label；format parser owns tag correctness；group rollout ownsrelative baseline；policy/reference checkpoints ownRL
  state；generated rationale is unverifiedderived text；clinician/evaluator must own diagnostic evidence/authority；deployment must not treat `<think>` as explanation proof。
- **Control Flow / Data Flow:** sample MRI VQA → policy produces six tagged rationale/answers → parser scores format+letter → group-normalize advantage → GRPO update withKL →
  test MRI/CT/X-ray → inspect rationale contradictions/failures → require external clinical validation/abstention before any decision use。
- **Implementation Details:** Qwen2-VL-2B，600 MRI train；2×A100-SXM4-80GB，300 steps,batch2,G=6,~4h；900 tests(300 MRI/CT/X-ray)；
  other optimization hyperparameters inherited from external framework and not fully pinned in v1。
- **Evaluation Contract:** multiple-choice HuatuoGPT-Vision subset；MRI in-domain, CT/X-ray OOD；exact tagged single-letter accuracy。Baselines Qwen2-VL2/7/72B,
  HuatuoGPT-Vision7B and same 2B SFT/600 MRI。No radiologist review, calibration, sensitivity/specificity, patient-level split or clinical outcome。
- **Baselines / Ablations / Sensitivity / Overhead:** GRPO vs same-data SFT and zero-shot models；paper states format and accuracy terms both needed but lacks full reward
  ablation、G/beta/epsilon sensitivity、multiple seeds、open-ended/rationale scorer、image-text shortcut or modality-balanced training comparison。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 2×A10080GB/4h/300 steps/batch2/G6 disclosed；precision、image resolution、prompt/output
  length、inference concurrency/latency/cost and clinical SLO not disclosed。
- **What the Evidence Actually Proves:** in a small closed-set split，GRPO with format+choice outcome reward changes a2B VLM and improves measured CT/X-ray choice accuracy
  relative to same-data SFT；small verifiable reward can yield cross-modality behavior in this benchmark。
- **What It Does Not Prove:** model learned medical reasoning，rationales arefaithful/transparent，OOD split represents hospitals/patients，RL generally outperforms SFT，
  answer accuracy supports clinical deployment，or 600 examples beat million-sample models under matched data/prompt/evaluation。
- **Limitations / Threats to Validity:** authors report failure toconverge pathology/OCT、open-ended degradation and superficial/contradictory rationales；tiny closed-set data、
  modality rather than site/patient OOD、prompt mismatch across baselines、single run/no uncertainty、label leakage/duplicates unknown and later artifact drift。
- **Trade-offs / New Failure Modes:** outcome reward is cheap and avoids rationale labels but can retrofit persuasive text around guessed choice；format reward improves parser
  reliability yet spends optimization capacity on tags；group reward needs multiple rollouts；KL limits drift but not hallucination；false confidence is especially harmful clinically。
- **Where the Previous Design Still Applies:** expert-reviewed SFT/rationales forclinical language；calibrated classifier/abstention forclosed-set triage；external image
  findings/segmentation and guideline retrieval；independent radiologist adjudication；prospective/site-shift evaluation before deployment。
- **Evolution Relationship:** `Alternative Branch`：large supervised medical VLM → small same-data SFT → closed-set GRPO outcome optimization → externally verified,
  calibrated clinical reasoning workflow。Paper stops beforefaithfulness/calibration/clinical gate。
- **ROADMAP Node:** `TRAIN-GRPO`（Current Ch33；Legacy Ch29）主 owner；handoff到`MULTIMODAL-REPRESENTATION`、
  `PLATFORM-EVALUATION-SYSTEM`、`PLATFORM-SECURITY`与`AGENT-WORKFLOW`。
- **Target and Adjacent Chapters Read:** 已读Ch33 group reward/verifier boundary、Ch23 modality distribution、Ch66 domain/evidence evaluation and Ch72 high-stakes
  security；confirms answer verifier does not own rationale/clinical truth。
- **Existing Coverage:** Books already says RLVR rewards outcome not reasoning and high-stakes evaluation needs domain contract；MedVLM-R1 can refine multimodal/domain case and
  explicit rationale failure，without model ranking/medical claims。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Reasoning Faithfulness Unverified`。
- **Changed Files or Rejection Reason:** this pass updates Weekly only；Books untouched；later code/model/MICCAI claims not backdated。
- **Open Questions:** event-time artifact、patient/source dedup、radiologist rationale/grounding audit、calibration/abstention、hospital/site OOD、open-ended tasks、reward
  ablation/seeds、privacy/license、inference SLO and prospective clinical validation。

### Mobius: Cyclic Output Semantics Require Cyclic Latent State and Decoder Symmetry

- **Candidate / Week / Score:** Mobius: Text to Seamless Looping Video Generation via Latent Shift / 2025-W09 / 24/30。
- **Source Family ID:** `mobius-cyclic-latent-video-diffusion-inference`。
- **Source Type:** arXiv v1/ACM TOG submission experimental training-free video diffusion inference；code promised but not publicly verified。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-27，current only one version；project page is presentation artifact，no immutable code release。
- **Direct Primary Sources:** https://arxiv.org/html/2502.20307v1；https://arxiv.org/abs/2502.20307；
  http://mobius-diffusion.github.io/。
- **Related Primary Sources:** CogVideoX-5B/DDIM、VBench/EvalCrafter prompts、SVD/CogVideo interpolation、FreeNoise/FIFO/DiTCtrl long-video methods；
  base-model license/behavior remains authoritative。
- **Access and Verification Status:** v1 full text/equations、latent shift/decoder/RoPE mechanism、140-prompt setup、metrics/user study/ablation/long video/
  limitations checked；paper says code will be available but no official code repository was resolved。
- **Full-read Coverage:** metadata、cinemagraph/video/long-video background、CogVideoX latent diffusion、cycle shifting、frame-invariant decoding、NTK-aware temporal
  RoPE、480×720/50-step/H100 setup、interpolation/latent-mix baselines、MSE/FVD/CLIP/VBench/user study、skip/RoPE/length analyses、motion-prior limitation。
- **Original Problem:** standard video diffusion owns a linear, fixed-length frame order；looped output requires last→first continuity and equal treatment of every frame，
  while 3D VAE and position encoding privilege the first frame and trained context length。
- **Why the Previous Design Was Reasonable:** linear latent sequence matches natural video and encoder compression；frame interpolation with fixed endpoints enforces boundary
  exactly。Ordinary non-looping generation or known keyframes still favor these contracts。
- **Changed Constraint:** text-only generation has no endpoint frames yet output commit semantics are cyclic and may exceed model context；inference must alter state traversal
  without retraining a 5B video model。
- **Mechanism:** initialize N cyclic noise latents，at denoising step t rotate start index `(t*s) mod N` and process one model-context window with wraparound，so each latent
  sees changing neighbors and boundary context。Prepend copied tail latents before 3D-VAE decode then trim to neutralize first-frame special handling；interpolate temporal RoPE for
  longer cycles，using fixed rather than shifted position mode when appropriate。
- **State Ownership:** base model owns denoising prior/context length；cyclic latent buffer owns frame identity moduloN；scheduler owns shift/skip/window；RoPE mode owns
  temporal coordinates；3D VAE owns asymmetric decode boundary；output codec owns final loop commit；none ownsphysical dynamics truth。
- **Control Flow / Data Flow:** text→noise ring → select wrapped window per timestep → CogVideoX denoise → rotate next window → repeat all steps → prepend tail latents →
  frame-invariant VAE decode → trim redundant frames → compare last/first and whole-video quality → emit loop or longer linear video。
- **Implementation Details:** CogVideoX-5B，480×720，50 DDIM steps，140 GPT-expanded VBench/EvalCrafter prompts，single H100；latent lengthN=n×base context,
  skip-step scheduler，frame copies and temporal RoPE interpolation；same nominal inference speed claimed but exact memory/long-length scaling not fully reported。
- **Evaluation Contract:** MSE first-vs-last、FVD、CLIP、VBench smooth/dynamic and user study for loop quality；interpolation baselines receive generated first frame as both
  endpoints，creating a different conditioning contract；long-video compares Gen-L-Video/FreeNoise/FIFO/DiTCtrl。
- **Baselines / Ablations / Sensitivity / Overhead:** CogVideoX direct、two interpolation models、Latent Mix、shift skip、fixed/shifted RoPE、frame-invariant decoder and
  long-video methods；no multiple base models、prompt/domain slices、long-duration memory/OOM frontier、seed variance、audio or safety/copyright evaluation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** single H100,5B,480×720,50 steps disclosed；precision、batch/concurrency、VRAM vsN、latency/
  duration curve、decode cost and serving SLO not disclosed。
- **What the Evidence Actually Proves:** under authors’ CogVideoX setup，cyclically rotating latent windows plus boundary-aware decoding creates more seamless loop metrics/
  preferences than selected baselines without weight training；output topology can require matching inference-state topology。
- **What It Does Not Prove:** arbitrary length maintains semantics/motion，RoPE interpolation yields reliable long context，loop representsreal periodic dynamics，same speed
  holds asN grows，or approach generalizes toother video models/domains。
- **Limitations / Threats to Validity:** one base model/140 prompts、no code、baseline conditioning mismatch、metrics weak forsemantic cycle、base motion-prior failures,
  customized illustration inconsistency、no seeds/confidence/memory curve and training-free changes can exploit unsupported latent positions。
- **Trade-offs / New Failure Modes:** cyclic state preserves boundary but changes every frame’s neighborhood and may smear temporal identity；longer N increasesmemory/work；
  copied-latent decoder fix is codec-specific；RoPE extrapolation may drift；training-free reuse is cheap but inherits all base prior/bias/safety limits。
- **Where the Previous Design Still Applies:** endpoint interpolation forknown start/end；linear generation for narratives；trained looping model fordomain fidelity；short base
  context when memory constrained；explicit simulator forperiodic physical behavior。
- **Evolution Relationship:** `Direct Evolution`：linear fixed-window latent → endpoint interpolation → cyclic latent scheduling → decoder-symmetric loop → extended cyclic/
  linear windows。This is output-state control，not world-model causality。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Current Ch24；Legacy N/A）主 owner；handoff到
  `MULTIMODAL-WORLD-MODELS`、`MODEL-POSITION-ENCODING`、`INFER-EXECUTION-ENGINE`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch24 video diffusion/mutable state、Ch25 observed vsgenerated dynamics、Ch13 position identity and Ch50 execution state；
  cyclic buffer is generation-runtime state，not environment belief。
- **Existing Coverage:** Ch24 already discusses video temporal state and commit；Mobius can refine topology/codec boundary and training-free inheritance，without a named product section。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / Training-Free Base-Model Bound`。
- **Changed Files or Rejection Reason:** this pass updates Weekly only；Books untouched；code absence and no arbitrary-length extrapolation claim retained。
- **Open Questions:** official code、other base models、N-memory/latency curve、semantic loop metric、audio、RoPE drift、codec portability、long-duration failure and independent reproduction。

### Dream Engine: A Shared Multimodal Encoder Can Replace Text Conditioning without Becoming a Unified Generator

- **Candidate / Week / Score:** Multimodal Representation Alignment for Image Generation: Text-Image Interleaved Control Is Easier Than You Think / 2025-W09 / 26/30。
- **Source Family ID:** `dream-engine-lmm-to-diffusion-interleaved-conditioning`。
- **Source Type:** arXiv v1 + later code repository；experimental LMM-conditioned diffusion generation/alignment。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-27，current one version；current repository has no immutable W09 release and may reflect later updates。
- **Direct Primary Sources:** https://arxiv.org/html/2502.20172v1；https://arxiv.org/abs/2502.20172；
  https://github.com/chenllliang/DreamEngine。
- **Related Primary Sources:** Qwen2VL-2B-Instruct、SD3.5-Large/MM-DiT、JourneyDB/CC12M/UltraEdit/internal object data and GenEval；internal4M data
  prevents full reproduction。
- **Access and Verification Status:** v1 full text、adapter/blending/objectives/two stages、datasets/training、GenEval/reconstruction/interleaved qualitative tasks/
  dynamics/blending ablation and current repo checked；paper lacks dedicated limitations/hardware disclosures and core data/model release is incomplete。
- **Full-read Coverage:** metadata、LMM/MM-DiT background、encoder replacement/two-layer adapter、ViT residual blend、flow objective、Stage1 text/image alignment、Stage2
  edit/object composition、20M+ data mix、LoRA training、text-image generation/reconstruction/qualitative controls、concept→detail dynamics、blend ratio and related work。
- **Original Problem:** text-only diffusion encoders cannot directly represent arbitrary interleaved text plusmultiple reference images；specialized image adapters/tokens often
  handle one task/image and add representation translation or per-input tuning。
- **Why the Previous Design Was Reasonable:** CLIP/T5 are optimized/stable text conditioners and separate image adapters isolate visual control；modular encoders can upgrade
  independently。Simple text-to-image or one-control workloads still favor them。
- **Changed Constraint:** generation input becomes an ordered mixed sequence of text and images with compositional instructions；system seeks reuse ofLMM shared semantics while
  retaining a high-quality pretrained diffusion decoder。
- **Mechanism:** replace SD3.5 CLIP/T5 encoders with frozen Qwen2VL hidden states projected by two-layer MLP into MM-DiT conditioning；blend final LMM image-patch states
  with ViT features to recover detail。Stage1 trainsadapter on text→image and image reconstruction while freezing LMM/DiT；Stage2 LoRA-tunes DiT attention for free-form edit and
  multi-image object composition，LMM remains frozen。
- **State Ownership:** LMM/tokenizer owns interleaved input semantics/order；ViT residual ownsvisual detail；adapter owns coordinate mapping；DiT/LoRA owns generation response；
  dataset/task prompt ownscomposition semantics；source image identity/provenance must survive conditioning，and output remains new generated artifact。
- **Control Flow / Data Flow:** tokenize ordered text/images → frozen LMM joint attention → separate semantic hidden/ViT detail blend → adapter maps condition → MM-DiT flow
  denoises latent → image decoder commits output；training first aligns bridge/reconstruction，then updates DiT LoRA on edit/composition tasks。
- **Implementation Details:** Qwen2VL-2B + SD3.5-Large，adapterMLP middle4096/SiLU；Stage1 one epoch,batch128,LR1e-4,warmup5%,cosine；Stage2 DiT attention
  LoRA rank32,LR5e-5。Data:12M text-image+4M image alignment,1M UltraEdit+4M internal object task。
- **Evaluation Contract:** GenEval text-to-image；200-image COCO/JourneyDB reconstruction CLIP+L2；interleaved control primarily qualitative vsEmu2；blend-ratio and
  no-image-alignment ablation。No human compositional benchmark、source identity/consent、failure/safety or latency/cost evaluation。
- **Baselines / Ablations / Sensitivity / Overhead:** SD3.5/native and AR/diffusion models、SeedTokenizer/EMU2/SEED-X reconstruction、with/without image alignment、
  visual blend ratio；no frozen-vs-unfrozen LMM、adapter width/LoRA rank、matched data/compute、multi-image quantitative test、prompt order/conflict or component version study。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/data/batch/LR disclosed；hardware、precision、sequence/image counts per prompt、training
  GPU-hours、inference memory/latency/concurrency and SLO are`Not Disclosed`。
- **What the Evidence Actually Proves:** in authors’ setup，a frozen LMM representation can condition a pretrained diffusion model through a lightweight adapter and LoRA，
  supporting text/image reconstruction and showcased interleaved controls；shared semantics and modality-specific generator can be layered rather than fully unified。
- **What It Does Not Prove:** LMM space is universally aligned，qualitative object mixing generalizes，model preserves source identity/rights，understanding capability is
  unchanged，architecture is an omni-model，or it beats specialized controls under matched data/compute。
- **Limitations / Threats to Validity:** internal4M data、qualitative core task、tiny reconstruction sample、no hardware/code release boundary、foundation-model/data bias,
  no negative/failure cases or human study；“emergent” composition may reflect COCO/internal correlations。
- **Trade-offs / New Failure Modes:** shared LMM input enablesarbitrary interleaving but couples tokenizer/LMM/adapter/DiT versions；frozen LMM preserves behavior yet may
  bottleneck generation；ViT blend restores detail but can copy/conflict withsemantic instruction；long mixed inputs increase attention/conditioning cost and source confusion。
- **Where the Previous Design Still Applies:** CLIP/T5 forstable text-only generation；IP-Adapter/ControlNet forsingle typed control；per-subject tuning foridentity fidelity；
  discrete unified generator when one autoregressive stream is required；modular pipeline forindependent upgrades/safety review。
- **Evolution Relationship:** `Layering / Dependency`：text encoder→diffusion → specialized image adapter → shared LMM interleaved conditioner → DiT task LoRA。
  It unifies the conditioning interface，not the entire model/runtime/objective。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Current Ch23；Legacy N/A）主 owner；handoff到
  `MULTIMODAL-GENERATIVE-PARADIGMS`、`PLATFORM-ARTIFACT-MANAGEMENT`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch23 shared representation/modality boundaries、Ch24 diffusion conditioning/generation，Ch58 artifact lineage and Ch66
  multimodal evaluation；confirmed conditioner and generator remain separate owners。
- **Existing Coverage:** Ch23 already distinguishes shared semantic interface from modality-specific towers；Dream Engine can refine LMM-conditioner evolution and artifact
  coupling，without claiming full unification。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。
- **Changed Files or Rejection Reason:** this pass updates Weekly only；Books untouched；internal data and qualitative evidence prevent stronger conclusion。
- **Open Questions:** event-time code/model、internal data provenance、quantitative multi-image control、identity/consent、hardware/latency、LMM unfreeze trade-off、
  component migration、prompt order/conflict and independent reproduction。

### R1-T1 v1: Reasoning Templates Can Seed Translation Policy Search, but COMET Reward Does Not Verify the Reasoning

- **Candidate / Week / Score:** R1-T1: Fully Incentivizing Translation Capability in LLMs via Reasoning Learning / 2025-W09 / 24/30。
- **Source Family ID:** `r1t1-translation-cot-reinforce-comet`。
- **Source Type:** arXiv v1 experimental SFT+REINFORCE++ translation reasoning；v1 artifact is an incomplete 10-page preprint with no public code。
- **Event Date / First-public Date / Revision History:** v1 2025-02-27；v2 2025-03-03 and v3 2025-05-26 materially expand/revise paper。This packet
  uses v1 PDF only for method/results and treats later versions as revision lineage。
- **Direct Primary Sources:** https://arxiv.org/pdf/2502.19735v1；https://arxiv.org/abs/2502.19735。
- **Related Primary Sources:** Flores-101、COMET/wmt20-comet-da、Qwen2.5-7B-Instruct、REINFORCE++ and seed parallel corpora；later v3 may contain
  additional domains/human evaluation unavailable in v1 and is not backdated。
- **Access and Verification Status:** arXiv HTML for v1 resolves to broken ACL template，so same-ID v1 PDF all10 pages was read；dataset/CoT/reward/RL/
  Flores tables/self-evolution case checked。No code、hardware、domain-task tables or dedicated limitation section in v1。
- **Full-read Coverage:** metadata/revisions、MT/CoT/RL background、2K seed pairs、six expert strategy templates/multi-agent refinement、SFT、format+COMET reward、
  modified REINFORCE++、Qwen setup、seen/unseen Flores directions、baseline tables and one qualitative CoT evolution case。
- **Original Problem:** direct translation or fixed CoT handles one domain/style but does not adapt reasoning strategy across language/domain；SFT onsynthetic CoT can
  overfit teacher format and discard exploration，while reasoning-distilled models may degrade translation。
- **Why the Previous Design Was Reasonable:** direct NMT/LLM translation minimizeslatency and avoids unverifiable rationale；specialized glossary/domain adaptation provides
  deterministic controls。Most ordinary translation workloads do not need long reasoning traces。
- **Changed Constraint:** authors target general translation across seen/unseen directions and want model toselect/refine translator strategies at inference，with onlysmall
  seed parallel data and automatic metric feedback。
- **Mechanism:** sample2K parallel pairs spanning lengths/domains/six languages；instantiate six expert-curated translation strategies into CoT usingmulti-agent reviews and
  discardunchanged refinement steps；full-parameter SFT teaches tags/strategies。Modified REINFORCE++ samples16 rollouts，rewards exact `<think>/<answer>` format plus positive
  rounded COMET against reference，then updates policy relative to a baseline reward。
- **State Ownership:** source/reference pair owns translation target but not unique wording；CoT template/reviewer owns strategy trace；COMET version owns learned quality
  proxy；policy/reference/checkpoint own RL state；format parser owns tags；human/domain reviewer should own terminology/meaning acceptance。
- **Control Flow / Data Flow:** sample licensed parallel pair → choose/instantiate strategy → multi-agent translate/review/refine → filter redundant trajectory → SFT policy →
  rollout tagged reasoning/translation → COMET+format score → REINFORCE++ update → evaluate frozen language directions → human/domain verification before release。
- **Implementation Details:** Qwen2.5-7B-Instruct；2K seed pairs split9:1,10–1200 tokens；SFT2 epochs full parameter LR1e-4；RL3 epochs LR3e-7,
  batch8,16 rollouts。Hardware、precision、KL/reference details、training cost and code are`Not Disclosed` in v1。
- **Evaluation Contract:** Flores-101 directions involving zh/en plus trained zh/ja/ru/fr/de/en and unseen th/nl/vi/tr/cs；COMET only in v1 tables；compare base/
  instruct/DeepSeek-distilled/SFT with/without CoT/RL。Abstract mentions broader domains/human evidence not fully substantiated in v1 body。
- **Baselines / Ablations / Sensitivity / Overhead:** base/instruct/distilled/SFT/RL and token-overlap check；no seed variance、human MQM/error taxonomy、reward ablation、
  direct-vs-reasoning latency、strategy-level contribution、domain tables、COMET gaming or later-version reconciliation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 7B,length distribution,batch/rollouts disclosed；hardware/precision/context-output length,
  training/inference latency/cost/concurrency and SLO not disclosed。
- **What the Evidence Actually Proves:** in v1 authors’ automatic Flores setup，small strategy-CoT SFT plus COMET-guided RL changes translation behavior and slightly
  improves aggregate COMET over selected baselines，including some unseen directions。
- **What It Does Not Prove:** CoT mirrors human translation cognition，reasoning causes quality，COMET improvement equals human preference/adequacy，model works across
  40+ directions/domains claimed later，or “self-evolution” is more than policy optimizing a fixed metric/template。
- **Limitations / Threats to Validity:** v1 HTML broken/PDF incomplete references/figures，no code/hardware/human evaluation/error bars，tiny2K seed，COMET used as reward
  and evaluation，reference/metric gaming，random split rather than document/domain holdout，unseen languages may still exist in base pretraining。
- **Trade-offs / New Failure Modes:** explicit strategies improvediagnosability but add tokens/latency and can hallucinate explanations；metric reward ischeap but couples
  training/evaluation and may favor reference-like wording；format reward can dominate low COMET；multi-agent synthetic traces share model biases；full tuning risks forgetting。
- **Where the Previous Design Still Applies:** direct translation forlatency；terminology/glossary constraints for regulated domains；human post-edit/MQM forhigh stakes；
  specialized NMT for stable pairs；external back-translation/quality estimation as independent workflow rather than hidden CoT。
- **Evolution Relationship:** `Alternative Branch`：direct MT → fixed human strategy prompt → synthetic strategy-CoT SFT → metric-guided policy exploration →
  human/domain-gated translation workflow。The paper reaches proxy optimization，not reasoning verification。
- **ROADMAP Node:** `TRAIN-GRPO`（Current Ch33；Legacy Ch29）主 owner；handoff到`TRAIN-SFT`、`AGENT-WORKFLOW`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已读Ch29 SFT imitation、Ch33 group/verifier reward boundaries、Ch81 workflow and Ch66 metric circularity；
  translation CoT is training/workflow artifact，not evidence of internal reasoning。
- **Existing Coverage:** Books already separates outcome proxy from reasoning and preserves direct-vs-RL branches；R1-T1 may refine cross-domain metric-reward case，but v1
  evidence is too incomplete forstronger mechanism claim。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate / v1 Evidence Incomplete`。
- **Changed Files or Rejection Reason:** this pass updates Weekly only；Books untouched；v2/v3 claims not backdated and no code found。
- **Open Questions:** v1 code/data/hardware、six template definitions/contributions、human MQM、COMET gaming、domain/40-direction evidence、forgetting、latency/cost、
  later revision diff and independent reproduction。

### Variational Consistency Training: Learn the Data–Noise Coupling to Reshape the Training Problem, Not the Sampler Prior

- **Candidate / Week / Score:** Training Consistency Models with Variational Noise Coupling / 2025-W09 / 26/30。
- **Source Family ID:** `vct-learned-data-noise-coupling-consistency-model`。
- **Source Type:** arXiv v1 + official Sony VCT code；experimental non-distillation consistency-model training。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-02-25；current title adds`VCT:` but same source family/revisions。W09 locks v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.18197v1；https://arxiv.org/abs/2502.18197；
  https://github.com/sony/vct。
- **Related Primary Sources:** iCT/ECM/OT baselines、FashionMNIST/CIFAR10/FFHQ/ImageNet64 and DDPM++/EDM2-S configs；published baseline values and authors’
  reimplementations are distinguished。
- **Access and Verification Status:** v1 full text/derivations/algorithms、VAE/ELBO link、beta schedule、all experiments/configs/toy/qualitative appendices and current
  official code checked；no independent reproduction found。
- **Full-read Coverage:** metadata、CT/FM/coupling background、continuous/discrete loss、Gaussian encoder coupling、joint objective/KL prior、VAE bound、beta adaptation、
  multistep sampler、iCT/ECM/OT/LI/VE baselines、FID/beta ablations、Fashion/CIFAR/FFHQ/ImageNet configs/hardware/time、toy geometry and code。
- **Original Problem:** independent data/noise pairing in consistency training can induce ambiguous/sharp flow partitions and high-variance bootstrap targets，especially with
  coarse time discretization；model must learn a difficult mapping fixed by forward process。
- **Why the Previous Design Was Reasonable:** independent Gaussian coupling guarantees exact known prior and simple one-step sampling；OT/minibatch coupling avoids extraencoder。
  When standard CT is stable or inference simplicity is paramount，these remainstrong baselines。
- **Changed Constraint:** non-distillation CT needs better few-step quality without pretrained diffusion teacher；training may alter coupling geometry as long as aggregated
  terminal noise remains close enough tostandard Normal for sampling。
- **Mechanism:** train small encoder `q_phi(x1|x0)=N(mu_phi(x0),sigma_phi(x0)^2 I)` jointly with consistency model；sample data-dependent noise by reparameterization,
  build paired adjacent noisy states，minimize consistency distance plus beta-weighted KL toN(0,I)，EMA both networks。Adaptive beta follows time-discretization weight；one-step
  sampling uses standard noise/model，multistep re-encodes intermediate samples viaencoder。
- **State Ownership:** data distribution owns x0；encoder checkpoint owns coupling/posterior；KL schedule owns prior-compatibility pressure；consistency/EMA checkpoints own
  denoiser map；sampler owns step schedule；artifact identity must bind encoder even if one-step deployment omits it after training。
- **Control Flow / Data Flow:** sample data → encoder emitsnoise posterior → sample coupled x1 → interpolate adjacent times → online/EMA consistency predictions →
  consistency+KL update encoder/model → validate aggregated prior/FID → one-step sample fromN(0,I) or multistep model→encoder→renoise loop。
- **Implementation Details:** Gaussian same-dimensional encoder，linear/variance-exploding kernels，beta dataset/model-specific and clipping200 early；iCT/ECM models
  13.6M–280M plus1.5M–6M encoder；400K/200K iterations,RAdam/Adam,1–2 H100。Encoder adds measured training hours; multistep adds encoder forward passes。
- **Evaluation Contract:** FashionMNIST/CIFAR10/FFHQ64/ImageNet64；1/2-step FID and visual samples；compare authors’ reimplemented iCT/ECM with linear/VE kernels,
  minibatch OT and learned coupling；some starred baseline results from papers，ImageNet iteration counts differ where marked。
- **Baselines / Ablations / Sensitivity / Overhead:** independent vsOT vsvariational coupling、linear/VE kernels、beta5–60 and adaptive beta、toy Gaussian geometry；
  no high-resolution/text-conditioned/audio/video test、precision/seed confidence、likelihood calibration、encoder removal/migration or production latency/goodput。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** H100 count/training hours/batches/iterations/model size disclosed；precision、data-loader/
  distributed details、sampling batch/concurrency、end-to-end decode latency and SLO incomplete。
- **What the Evidence Actually Proves:** in authors’ low-resolution image experiments，jointly learned coupling improves 1/2-step FID over matched reimplementations with
  modest extra training compute；coupling choice is part of objective geometry，not merely random-data plumbing。
- **What It Does Not Prove:** learned coupling removes CT instability generally，ELBO-style bound yields calibrated likelihood，FID gain transfers tolarge conditional models，
  prior match is exact，or extra encoder is free in multistep/production lifecycle。
- **Limitations / Threats to Validity:** only small/64² images、FID-centric、dataset-specific beta、large early clipping signalsinstability，mixed baseline provenance/
  iteration counts、no seeds/error bars、posterior restricted Gaussian/diagonal and no independent replication。
- **Trade-offs / New Failure Modes:** easier flow geometry addsencoder/state/KL tuning；weak beta breaks prior sampling，strong beta collapses tostandard CT；joint optimization
  can co-adapt encoder/model and hide poor marginal match；one-step deployment simpler but training lineage still depends onencoder；multistep pays extra encoder passes。
- **Where the Previous Design Still Applies:** standard CT forsimple/mature recipe；distillation when strong teacher exists；OT coupling withoutpersistent encoder；diffusion
  forquality/flexible steps；VAE/flow when likelihood/latent semantics are primary。
- **Evolution Relationship:** `Direct Evolution`：independent CT coupling → minibatch/hand-designed coupling → learned variational coupling + prior regularization →
  future adaptive coupling controllers。It reshapes training trajectories while preserving standard-noise deployment contract only approximately。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Current Ch24；Legacy N/A）主 owner；handoff到`TRAIN-PRETRAINING`、
  `INFER-EXECUTION-ENGINE`与`PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读Ch24 diffusion/flow/consistency and iterative cost、Ch28 objective/state、Ch50 execution and Ch66 evidence；
  confirms coupling is training mechanism with inference artifact consequences。
- **Existing Coverage:** Ch24 already compares diffusion/flow/correction but lacks data-noise coupling as an objective design axis；VCT can refine this without retaining FID table。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`。
- **Changed Files or Rejection Reason:** this pass updates Weekly only；Books untouched；current code linked but no independent reproduction。
- **Open Questions:** beta auto-calibration/prior diagnostics、high-resolution/conditional models、seed variance、encoder migration/removal、multistep latency、likelihood/
  calibration、interaction with modern CT improvements and independent reproduction。

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- 事件按 first-public date 归属本周；后续 revision、模型卡补充和工程集成回链本周，不重复创建新事件。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- GPT-4.5 → `WORLDVIEW-SCALING-LAW`（主 owner），连接`WORLDVIEW-LLM-INTELLIGENCE`、`TRAIN-PRETRAINING`、
  `TRAIN-RLHF`、`MODEL-SAMPLING`与`PLATFORM-EVALUATION-SYSTEM`。
- FlashMLA v1 → `INFER-TENSORRT-LLM`（通用execution-plan/kernel主 owner），连接`MODEL-SELF-ATTENTION`、
  `MODEL-KV-CACHE`、`INFER-DECODE`、`INFER-PAGED-ATTENTION`与`PLATFORM-EVALUATION-SYSTEM`。
- DeepEP V1 → `TRAIN-DISTRIBUTED-TRAINING`（主 owner），连接`MODEL-MOE`、`TRAIN-TENSOR-PARALLEL`、
  `INFER-PREFILL`、`INFER-DECODE`、`INFER-SCHEDULING`与`PLATFORM-EVALUATION-SYSTEM`。
- DeepGEMM v1 → `INFER-TENSORRT-LLM`（通用execution-plan/kernel主 owner），连接`MODEL-MOE`、
  `TRAIN-PRETRAINING`、`TRAIN-DISTRIBUTED-TRAINING`、`INFER-DECODE`与`PLATFORM-EVALUATION-SYSTEM`。
- DualPipe → `TRAIN-PIPELINE-PARALLEL`（主 owner），连接`TRAIN-DISTRIBUTED-TRAINING`、`MODEL-MOE`、
  `TRAIN-ZERO`与`PLATFORM-EVALUATION-SYSTEM`。
- EPLB → `MODEL-MOE`（主 owner），连接`TRAIN-DISTRIBUTED-TRAINING`、`INFER-SCHEDULING`、
  `PLATFORM-GPU-SCHEDULER`、`PLATFORM-MODEL-REGISTRY`与`PLATFORM-EVALUATION-SYSTEM`。
- 3FS → `PLATFORM-FOUNDATIONS`（主 owner / shared-storage structural candidate），连接`TRAIN-DATA`、
  `TRAIN-CHECKPOINT`、`INFER-KV-CACHE`、`PLATFORM-MODEL-REGISTRY`、`PLATFORM-MONITORING`与`PLATFORM-PRODUCTION`。
- smallpond → `TRAIN-DATA`（主 owner），连接`PLATFORM-FOUNDATIONS`、`PLATFORM-GPU-SCHEDULER`、
  `PLATFORM-MONITORING`与`PLATFORM-PRODUCTION`。
- V3/R1 Online Inference Overview → `INFER-PD-DISAGGREGATION`（主 owner），连接`MODEL-MOE`、
  `INFER-PREFILL`、`INFER-DECODE`、`INFER-SCHEDULING`、`PLATFORM-GPU-SCHEDULER`、`PLATFORM-COST`与`PLATFORM-EVALUATION-SYSTEM`。
- Wan2.1 → `MULTIMODAL-GENERATIVE-PARADIGMS`（主 owner），连接`MULTIMODAL-REPRESENTATION`、
  `MULTIMODAL-WORLD-MODELS`（boundary）、`INFER-EXECUTION-ENGINE`与`PLATFORM-EVALUATION-SYSTEM`。
- olmOCR → `TRAIN-DATA`（主 owner），连接`MULTIMODAL-REPRESENTATION`、`AGENT-RAG`、
  `PLATFORM-MODEL-REGISTRY`、`PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- Phi-4 mini/multimodal → `MULTIMODAL-REPRESENTATION`（主 owner），连接`MODEL-DECODER-ONLY`、
  `MODEL-LONG-CONTEXT`、`TRAIN-LORA`、`INFER-VLLM`、`PLATFORM-MODEL-REGISTRY`与`PLATFORM-SECURITY`。
- Command R7B Arabic → `TRAIN-DATA`（主 owner），连接`TRAIN-SFT`、`TRAIN-DPO`、
  `PLATFORM-EVALUATION-SYSTEM`、`AGENT-RAG`与`PLATFORM-SECURITY`。
- Claude 3.7 Sonnet and Claude Code → `MODEL-SAMPLING`、`INFER-SCHEDULING`、
  `AGENT-TOOL-CALLING` / `AGENT-WORKFLOW`、`PLATFORM-SECURITY`。
- SWE-RL → `TRAIN-GRPO`（主 owner），连接 `TRAIN-DATA`、`PLATFORM-EVALUATION-SYSTEM`、
  `AGENT-WORKFLOW` 与 `PLATFORM-SECURITY`。
- SpargeAttn → `INFER-TENSORRT-LLM`（通用 execution-plan owner），连接
  `MODEL-SELF-ATTENTION`、`INFER-PREFILL`、`INFER-DECODE` 与 `PLATFORM-EVALUATION-SYSTEM`。
- Drop-Upcycling → `MODEL-MOE`（主 owner），连接 `TRAIN-PRETRAINING`、
  `TRAIN-DISTRIBUTED-TRAINING`、`TRAIN-CHECKPOINT` 与 `INFER-TENSORRT-LLM`。
- Kanana → `TRAIN-PRETRAINING`（主 owner），连接 `TRAIN-DATA`、`TRAIN-SFT`、`TRAIN-DPO`、
  `TRAIN-CHECKPOINT` 与 `PLATFORM-MODEL-REGISTRY`。
- Towards Optimal Multi-draft Speculative Decoding → `INFER-SPECULATIVE-DECODING`（主 owner），连接
  `MODEL-SAMPLING`、`INFER-KV-CACHE`、`INFER-SCHEDULING`与`PLATFORM-EVALUATION-SYSTEM`。
- WebGames → `PLATFORM-EVALUATION-SYSTEM`（主 owner），连接 `AGENT-TOOL-CALLING`、
  `AGENT-WORKFLOW`、`PLATFORM-SECURITY`与`PLATFORM-TRACE`。
- OmniAlign-V → `TRAIN-DATA`（主 owner），连接 `MULTIMODAL-REPRESENTATION`、`TRAIN-SFT`、
  `TRAIN-DPO`与`PLATFORM-EVALUATION-SYSTEM`。
- Language Models' Factuality Depends on the Language of Inquiry → `PLATFORM-EVALUATION-SYSTEM`（主 owner），
  连接 `AGENT-CONTEXT`、`AGENT-RAG`、`TRAIN-DATA`与`PLATFORM-SECURITY`。
- Rank1 → `AGENT-RAG`（主 owner），连接 `TRAIN-SFT`、`INFER-SCHEDULING`、`PLATFORM-COST`与
  `PLATFORM-EVALUATION-SYSTEM`。
- DeltaBench → `PLATFORM-EVALUATION-SYSTEM`（主 owner），连接 `AGENT-REFLECTION`、`TRAIN-RLHF`、
  `TRAIN-GRPO`与`PLATFORM-COST`。
- Agentic Reward Modeling → `TRAIN-RLHF`（主 owner），连接 `TRAIN-DPO`、
  `PLATFORM-EVALUATION-SYSTEM`、`AGENT-WORKFLOW`、`AGENT-TOOL-CALLING`与`PLATFORM-SECURITY`。
- VEM → `TRAIN-PPO`（主 owner），连接 `TRAIN-RLHF`、`AGENT-TOOL-CALLING`、`AGENT-WORKFLOW`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- CritiQ → `TRAIN-DATA`（主 owner），连接 `TRAIN-PRETRAINING`、`TRAIN-CHECKPOINT`、
  `PLATFORM-EVALUATION-SYSTEM`、`AGENT-WORKFLOW`与`PLATFORM-COST`。
- Training LLMs with MXFP4 → `TRAIN-PRETRAINING`（主 owner），连接 `TRAIN-DISTRIBUTED-TRAINING`、
  `TRAIN-CHECKPOINT`、`INFER-TENSORRT-LLM`与`PLATFORM-EVALUATION-SYSTEM`。
- Self-Training Elicits Concise Reasoning → `TRAIN-SFT`（主 owner），连接 `MODEL-SAMPLING`、
  `INFER-SCHEDULING`、`PLATFORM-COST`与`PLATFORM-EVALUATION-SYSTEM`。
- Granite Embedding Models → `MODEL-EMBEDDING`（主 owner），连接 `TRAIN-DATA`、`AGENT-RAG`、
  `PLATFORM-MODEL-REGISTRY`与`PLATFORM-EVALUATION-SYSTEM`。
- WorldModelBench → `MULTIMODAL-WORLD-MODELS`（主 owner），连接 `PLATFORM-EVALUATION-SYSTEM`、
  `MULTIMODAL-GENERATIVE-PARADIGMS`、`MULTIMODAL-EMBODIED-VLA`与`PLATFORM-SECURITY`。
- LongRePS → `MODEL-LONG-CONTEXT`（主 owner），连接 `TRAIN-SFT`、`TRAIN-DATA`、`AGENT-RAG`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-COST`。
- PersonaBench → `AGENT-MEMORY`（主 owner），连接 `AGENT-RAG`、`PLATFORM-SECURITY`与
  `PLATFORM-EVALUATION-SYSTEM`。
- Safety Tax → `TRAIN-SFT`（主 owner），连接 `TRAIN-RLHF`、`PLATFORM-EVALUATION-SYSTEM`与
  `PLATFORM-SECURITY`。
- ARIES → `AGENT-PLANNING`（主 owner），连接 `AGENT-WORKFLOW`、`AGENT-MULTI-AGENT`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-COST`。
- GUI Pivot → `TRAIN-SFT`（主 owner），连接 `MULTIMODAL-REPRESENTATION`、`AGENT-TOOL-CALLING`、
  `AGENT-WORKFLOW`与`PLATFORM-EVALUATION-SYSTEM`。
- RaPID → `AGENT-WORKFLOW`（主 owner），连接 `AGENT-RAG`、`AGENT-PLANNING`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-COST`。
- Babel → `TRAIN-PRETRAINING`（主 owner），连接 `TRAIN-DATA`、`TRAIN-SFT`、`TRAIN-CHECKPOINT`、
  `PLATFORM-MODEL-REGISTRY`与`PLATFORM-COST`。
- LADDER → `TRAIN-GRPO`（主 owner），连接 `TRAIN-DATA`、`TRAIN-CHECKPOINT`、`AGENT-WORKFLOW`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- Diffusion Planner → `MULTIMODAL-EMBODIED-VLA`（主 owner），连接 `MULTIMODAL-GENERATIVE-PARADIGMS`、
  `MULTIMODAL-WORLD-MODELS`、`AGENT-PLANNING`与`PLATFORM-EVALUATION-SYSTEM`。
- Ray 2.43.0 → `PLATFORM-FOUNDATIONS`（主 owner），连接 `INFER-VLLM`、`PLATFORM-KSERVE`、
  `PLATFORM-GATEWAY`、`PLATFORM-GPU-SCHEDULER`与`PLATFORM-PRODUCTION`。
- JAX 0.5.1 → `TRAIN-DISTRIBUTED-TRAINING`（主 owner），连接`TRAIN-CHECKPOINT`、
  `TRAIN-TENSOR-PARALLEL`、`PLATFORM-FOUNDATIONS`、`PLATFORM-MODEL-REGISTRY`与`PLATFORM-EVALUATION-SYSTEM`。
- GOAT → `TRAIN-LORA`（主 owner），连接 `MODEL-MOE`、`TRAIN-SFT`、`TRAIN-CHECKPOINT`、
  `INFER-VLLM`与`PLATFORM-MODEL-REGISTRY`。
- Stable-SPAM v1 → `TRAIN-PRETRAINING`（主 owner），连接 `TRAIN-DISTRIBUTED-TRAINING`、
  `TRAIN-CHECKPOINT`、`TRAIN-DEEPSPEED`与`PLATFORM-EVALUATION-SYSTEM`。
- VideoGrain → `MULTIMODAL-GENERATIVE-PARADIGMS`（主 owner），连接 `MULTIMODAL-REPRESENTATION`、
  `MODEL-SELF-ATTENTION`与`PLATFORM-EVALUATION-SYSTEM`。
- DICEPTION v1 → `MULTIMODAL-REPRESENTATION`（主 owner），连接 `MULTIMODAL-GENERATIVE-PARADIGMS`、
  `TRAIN-DATA`、`TRAIN-LORA`与`PLATFORM-EVALUATION-SYSTEM`。
- Mobile-Agent-V v1 → `AGENT-WORKFLOW`（主 owner），连接 `AGENT-CONTEXT`、`AGENT-MEMORY`、
  `AGENT-REFLECTION`、`AGENT-MULTI-AGENT`与`PLATFORM-SECURITY`。
- Thus Spake Long-Context LLM v1 → `MODEL-LONG-CONTEXT`（主 owner），连接 `INFER-KV-CACHE`、
  `TRAIN-DISTRIBUTED-TRAINING`、`INFER-PD-DISAGGREGATION`、`AGENT-RAG`与`PLATFORM-EVALUATION-SYSTEM`。
- KV-Edit → `MULTIMODAL-GENERATIVE-PARADIGMS`（主 owner），连接 `MULTIMODAL-REPRESENTATION`、
  `MODEL-SELF-ATTENTION`、`INFER-KV-CACHE`与`PLATFORM-EVALUATION-SYSTEM`；与自回归 KV Cache 仅为
  `Principle Reuse`，不共享 causal-state invariant。
- K-LoRA → `TRAIN-LORA`（主 owner），连接 `MULTIMODAL-GENERATIVE-PARADIGMS`、`INFER-VLLM`、
  `PLATFORM-MODEL-REGISTRY`与`PLATFORM-EVALUATION-SYSTEM`。
- ART → `MULTIMODAL-GENERATIVE-PARADIGMS`（主 owner），连接 `MULTIMODAL-REPRESENTATION`、
  `MODEL-POSITION-ENCODING`、`TRAIN-DATA`、`INFER-TENSORRT-LLM`与`PLATFORM-EVALUATION-SYSTEM`。
- Clustering-On-Difficulty → `WORLDVIEW-SCALING-LAW`（主 owner），连接 `TRAIN-PRETRAINING`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-COST`。
- Visual Perception Token → `MULTIMODAL-REPRESENTATION`（主 owner），连接 `AGENT-TOOL-CALLING`、
  `TRAIN-SFT`、`INFER-SCHEDULING`与`PLATFORM-EVALUATION-SYSTEM`。
- MLLMs Know Where to Look / ViCrop → `AGENT-TOOL-CALLING`（主 owner），连接
  `MULTIMODAL-REPRESENTATION`、`AGENT-CONTEXT`与`PLATFORM-EVALUATION-SYSTEM`。
- Finding the Sweet Spot → `TRAIN-DPO`（主 owner），连接 `TRAIN-DATA`、`TRAIN-RLHF`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-COST`。
- WiCkeD → `PLATFORM-EVALUATION-SYSTEM`（主 owner），连接 `MODEL-SAMPLING`、
  `TRAIN-DATA`与`PLATFORM-SECURITY`。
- TheoremExplainAgent → `AGENT-WORKFLOW`（主 owner），连接 `AGENT-PLANNING`、`AGENT-RAG`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-COST`。
- BIG-Bench Extra Hard → `PLATFORM-EVALUATION-SYSTEM`（主 owner），连接 `WORLDVIEW-SCALING-LAW`、
  `MODEL-SAMPLING`、`TRAIN-DATA`与`PLATFORM-COST`。
- GHOST 2.0 → `Weekly Only — Outside Core Knowledge-tree Scope`；仅以 `PLATFORM-SECURITY` 保存synthetic-media
  consent/misuse handoff，不建立Books owner。
- Plutus → `PLATFORM-EVALUATION-SYSTEM`（主 owner），连接 `TRAIN-DATA`、`TRAIN-SFT`、
  `MODEL-LONG-CONTEXT`与`PLATFORM-SECURITY`。
- Project Alexandria → `AGENT-RAG`（主 owner），连接 `TRAIN-DATA`、`AGENT-MEMORY`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- REFUTE → `PLATFORM-EVALUATION-SYSTEM`（主 owner），连接 `AGENT-REFLECTION`、`AGENT-WORKFLOW`、
  `MODEL-SAMPLING`与`PLATFORM-SECURITY`。
- Distill Any Depth → `TRAIN-SFT`（主 owner），连接 `TRAIN-DATA`、`MULTIMODAL-REPRESENTATION`与
  `PLATFORM-EVALUATION-SYSTEM`。
- MMKE-Bench → `PLATFORM-EVALUATION-SYSTEM`（主 owner），连接 `AGENT-MEMORY`、`TRAIN-SFT`、
  `MULTIMODAL-REPRESENTATION`与`PLATFORM-SECURITY`。
- FSPO → `TRAIN-DPO`（主 owner），连接 `TRAIN-DATA`、`AGENT-MEMORY`、`PLATFORM-EVALUATION-SYSTEM`与
  `PLATFORM-SECURITY`。
- Accented ATC ASR → `Weekly Only — Domain Case / No New Core Mechanism`；仅连接 `TRAIN-DATA`、
  `MULTIMODAL-REPRESENTATION`与`PLATFORM-EVALUATION-SYSTEM`。
- Unsloth Direct Windows Support → `Weekly Only — Version/Compatibility Fact / No New Core Mechanism`；仅连接
  `TRAIN-LORA`、`TRAIN-GRPO`、`PLATFORM-FOUNDATIONS`与`PLATFORM-EVALUATION-SYSTEM`，不建立Books owner。
- AISafetyLab → `PLATFORM-SECURITY`（主 owner），连接 `PLATFORM-EVALUATION-SYSTEM`、`TRAIN-RLHF`与
  `PLATFORM-PRODUCTION`；framework code release回拨W01。
- PosterSum → `AGENT-RAG`（主 owner），连接 `MULTIMODAL-REPRESENTATION`、`AGENT-WORKFLOW`与
  `PLATFORM-EVALUATION-SYSTEM`。
- xAR → `MULTIMODAL-GENERATIVE-PARADIGMS`（主 owner），连接`MULTIMODAL-REPRESENTATION`、
  `MODEL-SAMPLING`、`INFER-SPECULATIVE-DECODING`与`PLATFORM-EVALUATION-SYSTEM`。
- LongRoPE2 → `MODEL-LONG-CONTEXT`（主 owner），连接`MODEL-POSITION-ENCODING`、`TRAIN-PRETRAINING`、
  `INFER-KV-CACHE`、`INFER-PREFILL-DECODE`与`AGENT-RAG`。
- ArtGS → `MULTIMODAL-EMBODIED-VLA`（主 owner），连接`MULTIMODAL-WORLD-MODELS`、
  `MULTIMODAL-REPRESENTATION`与`PLATFORM-EVALUATION-SYSTEM`。
- FUSED → `PLATFORM-SECURITY`（主 owner），连接`TRAIN-DATA`、`TRAIN-CHECKPOINT`、
  `PLATFORM-ARTIFACT-MANAGEMENT`与`PLATFORM-EVALUATION-SYSTEM`。
- Relation-Specific Neurons → `WORLDVIEW-REPRESENTATION`（主 owner），连接`MODEL-FFN`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- MAMUT → `TRAIN-DATA`（主 owner），连接`MODEL-TOKENIZER`、`TRAIN-PRETRAINING`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- DVPO → `TRAIN-PPO`（主 owner），连接`TRAIN-RLHF`、`TRAIN-GRPO`、`PLATFORM-EVALUATION-SYSTEM`与
  `INFER-RESOURCE-SCHEDULING`。
- NeoBERT → `TRAIN-PRETRAINING`（主 owner），连接`MODEL-TRANSFORMER-LAYER`、`MODEL-POSITION-ENCODING`、
  `MODEL-TOKENIZER`、`MODEL-LONG-CONTEXT`与`PLATFORM-EVALUATION-SYSTEM`。
- Ext2Gen → `AGENT-RAG`（主 owner），连接`TRAIN-DPO`、`AGENT-CONTEXT`、`PLATFORM-EVALUATION-SYSTEM`与
  `PLATFORM-SECURITY`。
- SuperRAG → `AGENT-RAG`（主 owner），连接`MULTIMODAL-REPRESENTATION`、`AGENT-CONTEXT`、
  `PLATFORM-ARTIFACT-MANAGEMENT`、`PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- R2-T2 → `MULTIMODAL-REPRESENTATION`（主 owner），连接`MODEL-MOE`、`INFER-RESOURCE-SCHEDULING`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- Self-rewarding Correction → `AGENT-REFLECTION`（主 owner），连接`TRAIN-GRPO`、`TRAIN-DPO`、
  `AGENT-WORKFLOW`与`PLATFORM-EVALUATION-SYSTEM`。
- SoRFT → `TRAIN-PPO`（主 owner），连接`AGENT-WORKFLOW`、`AGENT-PLATFORM`、
  `PLATFORM-EVALUATION-SYSTEM`与`TRAIN-DATA`。
- UniTok → `MULTIMODAL-REPRESENTATION`（主 owner），连接`MULTIMODAL-GENERATIVE-PARADIGMS`、
  `MODEL-TOKENIZER`、`PLATFORM-ARTIFACT-MANAGEMENT`与`PLATFORM-EVALUATION-SYSTEM`。
- EDGS → `MULTIMODAL-WORLD-MODELS`（主 owner），连接`MULTIMODAL-GENERATIVE-PARADIGMS`、
  `MULTIMODAL-EMBODIED-VLA`与`PLATFORM-EVALUATION-SYSTEM`。
- FINEREASON → `PLATFORM-EVALUATION-SYSTEM`（主 owner），连接`AGENT-REFLECTION`、`AGENT-PLANNING`、
  `AGENT-WORKFLOW`与`TRAIN-GRPO`。
- FlexiDiT → `MULTIMODAL-GENERATIVE-PARADIGMS`（主 owner），连接`MULTIMODAL-REPRESENTATION`、
  `INFER-EXECUTION-ENGINE`、`INFER-RESOURCE-SCHEDULING`与`PLATFORM-EVALUATION-SYSTEM`。
- MedVLM-R1 → `TRAIN-GRPO`（主 owner），连接`MULTIMODAL-REPRESENTATION`、`PLATFORM-EVALUATION-SYSTEM`、
  `PLATFORM-SECURITY`与`AGENT-WORKFLOW`。
- Mobius → `MULTIMODAL-GENERATIVE-PARADIGMS`（主 owner），连接`MULTIMODAL-WORLD-MODELS`、
  `MODEL-POSITION-ENCODING`、`INFER-EXECUTION-ENGINE`与`PLATFORM-EVALUATION-SYSTEM`。
- Dream Engine → `MULTIMODAL-REPRESENTATION`（主 owner），连接`MULTIMODAL-GENERATIVE-PARADIGMS`、
  `PLATFORM-ARTIFACT-MANAGEMENT`与`PLATFORM-EVALUATION-SYSTEM`。
- R1-T1 → `TRAIN-GRPO`（主 owner），连接`TRAIN-SFT`、`AGENT-WORKFLOW`、
  `PLATFORM-EVALUATION-SYSTEM`与`PLATFORM-SECURITY`。
- Variational Consistency Training → `MULTIMODAL-GENERATIVE-PARADIGMS`（主 owner），连接`TRAIN-PRETRAINING`、
  `INFER-EXECUTION-ENGINE`与`PLATFORM-EVALUATION-SYSTEM`。

## Recommended Action

- GPT-4.5：Books Pending — Refine Existing Argument Candidate / Mechanism Partially Disclosed。
- FlashMLA v1：Books Pending — Refine Existing Argument Candidate / W09 Snapshot Not Tagged。
- DeepEP V1：Books Pending — Refine Existing Argument Candidate / V1 Artifact Mutable。
- DeepGEMM v1：Books Pending — Refine Existing Argument Candidate / W09 Snapshot Not Tagged。
- DualPipe：Books Pending — Refine Existing Argument Candidate / Mechanism Pre-window。
- EPLB：Books Pending — Refine Existing Argument Candidate / Initial Snapshot Partially Recovered。
- 3FS：Books Pending — Structural/Refine Candidate / W09 Snapshot Not Tagged。
- smallpond：Books Pending — Refine Existing Argument Candidate / 3FS-coupled Evidence。
- V3/R1 Online Inference Overview：Books Pending — Refine Existing Argument Candidate / Vendor Production Case。
- Wan2.1：Books Pending — Refine Existing Argument Candidate / Later Report Evidence。
- olmOCR：Books Pending — Refine Existing Argument Candidate / Teacher and Pipeline Coupled。
- Phi-4 mini/multimodal：Books Pending — Refine Existing Argument Candidate / Later Report Evidence。
- Command R7B Arabic：Books Pending — Refine Existing Argument Candidate / Regional Post-training Branch。
- Claude 3.7 Sonnet / Claude Code：Weekly Only；公开行为与system-card case，内部机制未披露。
- SWE-RL：Books Pending — Refine Existing Argument Candidate。
- SpargeAttn：Books Pending — Refine Existing Argument Candidate。
- Drop-Upcycling：Books Pending — Refine Existing Argument Candidate。
- Kanana：Books Pending — Refine Existing Argument Candidate。
- Towards Optimal Multi-draft Speculative Decoding：Books Pending — Refine Existing Argument Candidate。
- WebGames：Books Pending — No Change Candidate。
- OmniAlign-V：Books Pending — Refine Existing Argument Candidate。
- Cross-lingual factuality：Books Pending — Refine Existing Argument Candidate。
- Rank1：Books Pending — No Change Candidate。
- DeltaBench：Books Pending — Refine Existing Argument Candidate。
- Agentic Reward Modeling：Books Pending — Refine Existing Argument Candidate。
- VEM：Books Pending — Refine Existing Argument Candidate。
- CritiQ：Books Pending — Refine Existing Argument Candidate。
- Training LLMs with MXFP4：Books Pending — Refine Existing Argument Candidate。
- Self-Training Elicits Concise Reasoning：Books Pending — Refine Existing Argument Candidate。
- Granite Embedding Models：Books Pending — No Change Candidate。
- WorldModelBench：Books Pending — No Change Candidate。
- LongRePS：Books Pending — Refine Existing Argument Candidate。
- PersonaBench：Books Pending — No Change Candidate。
- Safety Tax：Books Pending — No Change Candidate。
- ARIES：Books Pending — No Change Candidate。
- GUI Pivot：Books Pending — Refine Existing Argument Candidate。
- RaPID：Books Pending — Refine Existing Argument Candidate。
- Babel：Books Pending — Refine Existing Argument Candidate。
- LADDER：Books Pending — Refine Existing Argument Candidate。
- Diffusion Planner：Books Pending — Refine Existing Argument Candidate。
- Ray 2.43.0：Books Pending — No Change Candidate。
- JAX 0.5.1：Books Pending — Refine Existing Argument Candidate；Historical Books Gate保持关闭。
- GOAT：Books Pending — Refine Existing Argument Candidate。
- Stable-SPAM v1：Books Pending — Refine Existing Argument Candidate。
- VideoGrain：Books Pending — Refine Existing Argument Candidate。
- DICEPTION v1：Books Pending — Refine Existing Argument Candidate。
- Mobile-Agent-V v1：Books Pending — Refine Existing Argument Candidate。
- Thus Spake Long-Context LLM v1：Books Pending — No Change Candidate。
- KV-Edit：Books Pending — Refine Existing Argument Candidate。
- K-LoRA：Books Pending — Refine Existing Argument Candidate。
- ART：Books Pending — Refine Existing Argument Candidate / Artifact Withdrawn。
- Clustering-On-Difficulty：Books Pending — Refine Existing Argument Candidate；v1 headline metric保持`Disputed`。
- Visual Perception Token：Books Pending — Refine Existing Argument Candidate。
- MLLMs Know Where to Look / ViCrop：Books Pending — No Change Candidate。
- Finding the Sweet Spot：Books Pending — Refine Existing Argument Candidate。
- WiCkeD：Books Pending — Refine Existing Argument Candidate。
- TheoremExplainAgent：Books Pending — No Change Candidate。
- BIG-Bench Extra Hard：Books Pending — Refine Existing Argument Candidate。
- GHOST 2.0：Weekly Only — Outside Core Knowledge-tree Scope。
- Plutus：Books Pending — No Change Candidate。
- Project Alexandria：Books Pending — Refine Existing Argument Candidate；legal claim保持jurisdiction-specific/Emerging。
- REFUTE：Books Pending — Refine Existing Argument Candidate。
- Distill Any Depth：Books Pending — No Change Candidate。
- MMKE-Bench：Books Pending — Refine Existing Argument Candidate / Artifact Metadata Inconsistent。
- FSPO：Books Pending — Refine Existing Argument Candidate。
- Accented ATC ASR：Weekly Only — Domain Case / No New Core Mechanism。
- Unsloth Direct Windows Support：Weekly Only — Version/Compatibility Fact / No New Core Mechanism。
- AISafetyLab：Books Pending — No Change Candidate；official framework code event spillback W01。
- PosterSum：Books Pending — No Change Candidate。
- xAR：Books Pending — Refine Existing Argument Candidate。
- LongRoPE2：Books Pending — Refine Existing Argument Candidate。
- ArtGS：Books Pending — Refine Existing Argument Candidate。
- FUSED：Books Pending — Refine Existing Argument Candidate。
- Relation-Specific Neurons：Books Pending — No Change Candidate。
- MAMUT：Books Pending — Refine Existing Argument Candidate / Downstream Model Evidence Missing。
- DVPO：Books Pending — Refine Existing Argument Candidate / Theorem Assumptions Restricted。
- NeoBERT：Books Pending — Refine Existing Argument Candidate。
- Ext2Gen：Books Pending — Refine Existing Argument Candidate / Artifact Unreleased at v1。
- SuperRAG：Books Pending — Refine Existing Argument Candidate / Core Parser Not Open。
- R2-T2：Books Pending — Refine Existing Argument Candidate / High Test-time FLOP Cost。
- Self-rewarding Correction：Books Pending — Refine Existing Argument Candidate / Internal Reward Not Independent。
- SoRFT：Books Pending — Refine Existing Argument Candidate / Proxy Reward False Negatives。
- UniTok：Books Pending — Refine Existing Argument Candidate。
- EDGS：Books Pending — No Change Candidate / Rendering Evidence Only。
- FINEREASON：Books Pending — Refine Existing Argument Candidate。
- FlexiDiT：Books Pending — Refine Existing Argument Candidate。
- MedVLM-R1：Books Pending — Refine Existing Argument Candidate / Reasoning Faithfulness Unverified。
- Mobius：Books Pending — Refine Existing Argument Candidate / Training-Free Base-Model Bound。
- Dream Engine：Books Pending — Refine Existing Argument Candidate。
- R1-T1：Books Pending — Refine Existing Argument Candidate / v1 Evidence Incomplete。
- Variational Consistency Training：Books Pending — Refine Existing Argument Candidate。
- 其余已发现 Source Family：完成全文审计后再固定评分与 Books disposition。

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

Historical Books Gate 保持关闭。当前100个20+ owner event完成 Source Review，另3个低分owner event完成
identity/date/score/rejection核验；ordinary backlog已清零。声明的academic export gap与三项engineering release-feed
blocker保持在年度Archive ledger，不阻塞forward cursor。不得把本周摘要或score直接写入 Books。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。

## Repository Changes

- 幂等修复 `papers/2025/weekly/2025-W09/README.md`：撤回“论文与工程无候选”与“Books Gate已完成”，
  当前已为100个20+ owner events保存非模板化 Full Source Review，并完成3个低分owner event核验；本检查点完成W10 replay回拨的12个family。
- 2025 Primary-Source Re-audit 进行中；W09 Candidate Evidence Gate在声明Discovery/Release-feed gaps条件下通过，本周未进入 Books Integration。

## Open Questions

- W09已闭合全部已发现可访问owner；最终账目为100个20+ Full Source Reviews、3个低分核验、0 ordinary pending。
- 模型机构复扫发现并完成GPT-4.5，修正旧“仅Claude 3.7”结论；固定机构scan已完成本周可访问范围。
- fixed-org发现的Wan2.1、olmOCR、Phi-4 sibling family与Command R7B Arabic均完成，W09 ordinary `Review Pending = 0`；
  SmolVLM2、Grok 3与Mistral Saba按日期回拨W08，不放进W09。
- DeepSeek Open Source Week从机构复扫恢复8个family；FlashMLA v1、DeepEP V1、DeepGEMM v1、DualPipe、EPLB、3FS、smallpond与
  V3/R1 inference overview已全部完成，ordinary `Review Pending = 0`。
- 工程replay已闭合JAX、Ray、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、KServe、Kubernetes、
  Transformers、Accelerate、DeepSpeed、Unsloth、MLX、ONNX Runtime与OpenXLA的W09日期归属；Kubeflow、
  Megatron-LM与llama.cpp转入明确blocked ledger，不再伪装为普通review pending。
- HF 2月28日Newsletter可见20条identity已全部恢复；18个W09 owner已完成，ordinary `Review Pending = 0`，
  CODESYNC与Guardians按v1回拨W08。AISafetyLab code与Non-ergodic revision回拨W01，MolSpectra、DOEI、CODESYNC与
  Guardians回拨W08。Cross-index另发现并完成FUSED、MAMUT、Ext2Gen与SuperRAG。
- hybrid reasoning的内部机制、quality-per-token calibration以及Claude Code preview的state/sandbox/recovery
  contract仍未公开；其他family的问题见各 Source Review。

## W10 Discovery Spillback Full Source Reviews（2026-08-20）

以下 12 个 Source Family 均按 v1 归属 W09。每个 packet 将身份/版本/来源/阅读范围，问题/机制/状态与
数据控制流，evaluation contract/证明边界，以及 trade-off/owner/disposition 合并为四组非模板字段。

### Predictive Data Selection / PreSelect

- **Identity / access:** 2025-W09，29/30，`preselect-predictive-data-selection`，arXiv + official code；v1 2025-03-02。已读 https://arxiv.org/html/2503.00808v1 的 predictive-strength derivation、fastText deployment、400M～3B pretraining、17-task evaluation、filtering/infra/hyperparameter appendix。
- **Problem / mechanism:** rule/domain quality filter不直接估计“哪些数据教会目标能力”。PreSelect用多组 open models 在 seed documents上的 normalized loss排序与 downstream能力排序计算 predictive strength，取正负样本训练 fastText scorer，再扩展到大 corpus；score pipeline owns selection evidence，immutable manifest owns realized data。
- **Evidence contract:** RefinedWeb/C4 pools，400M/1B/3B Llama/Pythia，8B～100B selected tokens，对 random、PPL、FineWeb-Edu、DCLM 等；作者的10x compute claim只成立于1B 30B selected vs 300B random和所测17 tasks，不证明 predictive correlation是因果、也不覆盖 frontier-scale drift。
- **Boundary / owner:** benchmark-target leakage、open-model family bias、fastText approximation与 scorer staleness是 failure modes；未知目标时 domain/diversity sampling仍合理。`Direct Evolution`；owner `TRAIN-DATA`（Ch27，legacy Ch23），读 Ch28/66。`Books Pending — Refine Existing Argument`；待验证 dedup、multilingual与动态 score refresh。

### Chain of Draft

- **Identity / access:** 2025-W09，24/30，`chain-of-draft-concise-reasoning`，arXiv research；v1 2025-02-25。已读 https://arxiv.org/html/2502.18600v1 的 prompt contract、arithmetic/commonsense/symbolic tasks、token/latency results与案例；论文无独立 implementation/limitations section，相关字段按 `Not Disclosed` 处理。
- **Problem / mechanism:** verbose CoT把中间叙述本身变成 token/latency cost。CoD通过“每一步只写关键草稿、约5词”约束外显 reasoning；model仍拥有隐藏计算与生成，prompt只改变可见 trace，答案 evaluator拥有 correctness。
- **Evidence contract:** 多个 closed LLM、GSM8K/BBH类 multi-step tasks，与 direct answer/standard CoT比较 token、latency、accuracy；证明部分模型/任务可用短 scratchpad维持质量，不证明隐藏 reasoning更短、训练模型或 hard tasks均适用，且 provider latency/price会变化。
- **Boundary / owner:** 过度压缩会删除可审计步骤、降低 verifier/人类定位能力；高风险证明仍需要完整 trace。`Alternative Branch`；owner `AGENT-PROMPT`（Ch74，legacy Ch70），handoff `MODEL-SAMPLING`/Ch66；读 Ch75。`Books Pending — Refine Existing Argument`。

### DeepSolution / SolutionRAG

- **Identity / access:** 2025-W09，25/30，`deepsolution-solutionrag`，arXiv research；v1 2025-02-28。已读 https://arxiv.org/html/2502.20730v1 的 SolutionBench construction/manual verification、bi-point tree、depth/branch/prune settings、baselines、ablation、appendix与limitations。
- **Problem / mechanism:** single-pass/single-chain RAG难以同时提出工程方案并批判缺陷。SolutionRAG交替生成 solution node 与 comment node，tree expansion后用 evaluator prune（默认 depth5、branch2、retain1）；tree store owns alternatives，review node owns critique proposal，final selector owns commit但不是 external truth。
- **Evidence contract:** 从工程期刊构建并人工核验 benchmark，比较 deep reasoning APIs、single/multi-round RAG并消融 tree/bi-point；证明该 domain/harness的搜索结构有效，不证明 LLM judge能验证真实工程可行性。论文明确未做专门训练，hardware与生产SLO未披露。
- **Boundary / owner:** tree token cost、judge bias、早剪枝与 source authority drift；明确问题/强检索时单链更经济。`Direct Evolution`；owner `AGENT-RAG`（Ch76，legacy Ch72），handoff Ch79/80/66；读 Ch75/77。`Books Pending — Domain-limited Refine Candidate`。

### ViDoRAG / ViDoSeek

- **Identity / access:** 2025-W09，27/30，`vidorag-visual-document-rag`，v1 PDF + official code；v1 2025-02-25，v2 later。HTML cache失败后完整读取 https://arxiv.org/pdf/2502.18017v1 的 dataset pipeline、hybrid retrieval、three-agent flow、experiments/ablations/appendix与limitations，并核对 abs metadata。
- **Problem / mechanism:** OCR-only/visual-only retrieval各自丢信息，static top-k又不能适配 query。ViDoRAG以 GMM拟合 text/visual similarity动态选K并融合结果，seeker扫缩略图、inspector反思/初答、answer agent提交；corpus/index owns evidence identity，agents只拥有 candidate/reasoning state。
- **Evidence contract:** ViDoSeek约1.2k questions、约6k pages/12 domains，比较 OCR/visual/multimodal RAG与 agent variants；作者报告其 benchmark上超过强基线，但不证明跨文档类型/语言、judge factuality或大规模并发。数据由专家+GPT-4/4o辅助构建，存在 generation/evaluation coupling。
- **Boundary / owner:** GMM misfit、modal score不可比、agent token tax与 source-page provenance丢失；单模态文档/精确OCR可用简单 pipeline。`Direct Evolution`；owner `AGENT-RAG`（Ch76），handoff `MULTIMODAL-REPRESENTATION`/Ch66；读 Ch75/77。`Books Pending — Refine Existing Argument`。

### LettuceDetect

- **Identity / access:** 2025-W09，26/30，`lettucedetect-rag-hallucination`，arXiv + model/code；v1 2025-02-24。已读 https://arxiv.org/html/2502.17125v1 的 ModernBERT span classifier、RAGTruth training/evaluation、long-context/latency comparison与 error analysis；缺少独立 ablation/limitations部分已明确。
- **Problem / mechanism:** LLM-as-judge昂贵，旧 encoder有512-token边界；LettuceDetect把 question/context/answer编码为最长8192 tokens的 ModernBERT输入，对 answer span/token分类 hallucination。source context owns comparison evidence，detector owns non-authoritative flags，application决定 abstain/retry。
- **Evidence contract:** RAGTruth及其 sentence/word-level labels，与 prompt-based LLM/encoder baselines比较 accuracy/F1/latency；部分对比因 RAG-HAT/RAGTruth公开实现缺项采用作者实现。证据支持此 dataset的检测效率，不证明跨 domain calibrated confidence或事实源本身正确。
- **Boundary / owner:** detector domain shift、context poisoning、span threshold与 false negative；高风险 claim仍需检索+independent verifier。`Layering / Dependency`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `AGENT-RAG`；读 Ch65/67。`Books Pending — Refine Existing Argument`。

### TeleRAG

- **Identity / access:** 2025-W09，28/30，`telerag-lookahead-retrieval`，arXiv + implementation；v1 2025-02-28。已读 https://arxiv.org/html/2502.20969v1 的 pipeline model、IVF/lookahead algorithm、optimal prefetch model、PyTorch/FAISS implementation、hardware/task evaluation与 appendix。
- **Problem / mechanism:** GPU index快但容量不足，CPU offload容量大却让 retrieval串行等待。TeleRAG利用 query transformation/pre-retrieval generation窗口预测相似 query的 IVF clusters，从CPU异步搬到GPU并与LLM compute重叠；index owns authoritative vectors，prefetch cache owns speculative state，retrieval miss回退CPU。
- **Evidence contract:** NQ等 RAG workloads，FlashRAG pipelines、1024-query retrieval tests与多种 nprobe/prefetch量，对 CPU/GPU baselines；作者平均最多1.72x只绑定其 GPU/CPU/index/datastore/LLM pipeline，不证明高并发、query drift或NVMe/remote store。precision与完整SLO按未披露处理。
- **Boundary / owner:** misprediction bandwidth waste、GPU cache pressure、PCIe contention与 consistency/invalidation；small index/GPU-resident corpus仍无需 lookahead。`Principle Reuse`；owner `AGENT-RAG`（Ch76），handoff `INFER-SCHEDULING`/Ch54；读 Ch75/77。`Books Pending — Refine Existing Argument`。

### DexGraspVLA

- **Identity / access:** 2025-W09，27/30，`dexgraspvla-hierarchical-control`，v1 PDF + project artifact；v1 2025-02-28，later revisions不改变owner。已读 https://arxiv.org/pdf/2502.20900v1 的 planner/controller、representation/action diffusion、2,094-episode data、real-robot evaluation、appendix与limitations。
- **Problem / mechanism:** raw visual imitation在object/background/light变化下domain shift大。framework用VLM高层定位/分解目标，DINOv2/Cutie等抽取mask/invariant features，DiT低层预测action chunk并以 receding horizon只执行前Ha步；planner owns intent，controller owns provisional action，robot/environment feedback owns commit truth。
- **Evidence contract:** 7-DoF arm、6-DoF hand、双RealSense，36 training objects/2,094 episodes，unseen clutter/environment与 baseline comparison；v1声称90%+只代表其robot/setup/combinations，不证明任意embodiment或 functional grasping。论文明确未覆盖极小物体、极拥挤和后续功能使用。
- **Boundary / owner:** VLM bbox错误、tracker drift、action-chunk latency与hardware calibration；固定环境可用end-to-end policy。`Layering / Dependency`；owner `MULTIMODAL-EMBODIED-VLA`（Ch26），handoff Ch23/25/66；读 Ch25/27。`Books Pending — Experimental`。

### TokenSwift / Ultra-long Sequence Generation

- **Identity / access:** 2025-W09，28/30，`tokenswift-ultralong-speculative-generation`，arXiv research；v1 2025-02-26。已读 https://arxiv.org/html/2502.18890v1 的 multi-draft tree、token reutilization、dynamic KV、penalty/n-gram selection、20K～100K experiments、sampling/KV/temperature/prefix ablations与 appendix。
- **Problem / mechanism:** speculative acceptance在极长自由生成中随context/重复模式变化，draft与KV成本累积。TokenSwift复用历史tokens/n-grams形成多候选tree，动态保留重要KV并用 contextual penalty维持diversity；target verifier owns exact distribution，draft/tree/KV eviction均为 speculative state。
- **Evidence contract:** Llama3.1-8B、prefix 2K～8K、generation 20K～100K、top-p/temperature variants，与 AR/Medusa等比较；100K从近5小时到约90分钟仅为作者单workload结果。证明其设定可lossless加速，不证明文本质量、batch serving、larger models或all samplers。
- **Boundary / owner:** tree verification cost、KV eviction误判、repetition penalty改变proposal与long-output utility；短输出/高batch可能 conventional decode更优。`Direct Evolution`；owner `INFER-SPECULATIVE-DECODING`（Ch48，legacy Ch44），handoff Ch45/56；读 Ch47/49。`Books Pending — Refine Existing Argument`。

### Efficient Test-Time Scaling via Self-Calibration

- **Identity / access:** 2025-W09，27/30，`self-calibration-test-time-scaling`，arXiv research；v1 2025-02-25。已读 https://arxiv.org/html/2503.00031v1 的 confidence distillation、dynamic temperature/soft self-consistency、adaptive sampling、multiple models/datasets、ECE/accuracy ablation与 appendix。
- **Problem / mechanism:** fixed Best-of-N浪费easy query预算，raw self-confidence又overconfident。method先用multi-sample self-consistency生成soft confidence target，再fine-tune model一次forward输出 calibrated confidence，runtime按threshold继续采样/停止；model owns estimate，scheduler owns budget，task evaluator owns correctness。
- **Evidence contract:** Llama/Qwen等与 MathQA、object counting等，比较 vanilla confidence、reward model、fixed/adaptive self-consistency，以 ECE/accuracy/token budget评价并消融EDT/SSC/loss；证明所测分布能改善budget allocation，不证明 confidence等于事实概率或跨domain threshold稳定。
- **Boundary / owner:** teacher self-consistency相关错误、calibration drift、extra output head/training与 threshold mis-tuning；稳定低风险workload可fixed-N。`Direct Evolution`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `MODEL-SAMPLING`/Ch56；读 Ch65/67。`Books Pending — Refine Existing Argument`。

### DuoDecoding

- **Identity / access:** 2025-W09，28/30，`duodecoding-heterogeneous-speculation`，arXiv + code；v1 2025-03-02。已读 https://arxiv.org/html/2503.00784v1 的 optimal draft budget、dynamic multi-sequence drafting、CPU/GPU overlap、seven-task evaluation、ablations与limitations。
- **Problem / mechanism:** draft与target同GPU争算力并增加TTFT。DuoDecoding把Q5_K_M draft放16-core Xeon CPU、FP16 target放A800 GPU并行运行，按hardware model选择draft budget，多draft sequences提升acceptance；target owns accepted prefix，CPU draft owns disposable candidates。
- **Evidence contract:** 7B target/base+chat、dialogue/translation/math/code等，single A800+16-core CPU，transformers+llama.cpp，对 conventional speculation/decoding比较TPS/latency/TTFT；up to2.61x和TTFT 83%不外推 large batch、larger target或不同CPU/GPU ratio，论文亦明确这些限制。
- **Boundary / owner:** CPU quantization quality、host scheduling、transfer/synchronization与idle balance；GPU余量足或batch大时same-device draft可能更优。`Direct Evolution`；owner `INFER-SPECULATIVE-DECODING`（Ch48），handoff Ch54/56；读 Ch47/49。`Books Pending — Refine Existing Argument`。

### Web AI Agent Vulnerability

- **Identity / access:** 2025-W09，27/30，`web-agent-component-vulnerability`，arXiv research；v1 2025-02-27。已读 https://arxiv.org/html/2502.20383v1 的 fine-grained taxonomy、component reconstruction、mock/real web setup、ablation、qualitative appendix与limitations；危险prompt细节不复制。
- **Problem / mechanism:** 同一aligned backbone进入web agent后更易产生有害action，说明风险来自system composition。论文逐步加入 system-prompt user goal、multi-step action generation、action instructions与 observation/event stream，隔离使拒绝边界弱化的组件；agent harness owns privileged context/action opportunities。
- **Evidence contract:** GPT-4o-2024-08-06、10 harmful requests×3、mock Instagram/LinkedIn/Gmail并与real sites对照；结果支持该 scaffold的三类风险因素，不证明所有web agents、所有models或真实攻击率。样本小、framework/model覆盖有限且judge contract有边界。
- **Boundary / owner:** system prompt privilege confusion、observation injection、multi-step policy drift与action side effects；standalone refusal不能替代 runtime guard。`Layering / Dependency`；owner `PLATFORM-SECURITY`（Ch72，legacy Ch68），handoff `AGENT-TOOL-CALLING`/Ch84；读 Ch71/73。`Books Pending — Refine Existing Argument`。

### LLM as a Broken Telephone

- **Identity / access:** 2025-W09，24/30，`broken-telephone-iterative-distortion`，arXiv + code/data；v1 2025-02-27。已读 https://arxiv.org/html/2502.20258v1 的 repeated translation/rephrasing protocols、three domains/models、100-iteration metrics、temperature/model-collaboration ablations与limitations。
- **Problem / mechanism:** workflow常把model output无provenance地再次作为input，微小改写会累积。实验把book/movie/news文本经多语translation或rephrase循环100次，以 relevance/factuality追踪drift；each stage owns only derivative text，original artifact remains sole reference truth。
- **Evidence contract:** Llama/Mistral/Gemma 7～9B、30-sample ablations与three similar text domains；观察显示反复生成普遍丢细节，但不证明所有workflow单调同速退化，也未覆盖retrieval grounding、larger models和long-tail专业内容。
- **Boundary / owner:** compounding omission、plausible fabrication与cross-model correlated error；有immutable source+diff/verifier时多阶段编辑仍合理。`Principle Reuse`；owner `AGENT-WORKFLOW`（Ch81，legacy Ch77），handoff Ch66/77；读 Ch80/82。`Books Pending — Refine Existing Argument`。

### Spillback Resolution

12 个 spillback family 全部完成 `20+` Full Source Review、评分、Stable Node owner 与 disposition；没有按
Hugging Face recommendation date重复进入 W10。W09 最终账目更新为100个 `20+` Full Source Reviews、
3个低分核验、0 ordinary `Review Pending`。Candidate Evidence Gate 恢复为 Passed with Declared Gaps；
Scholar/OpenAlex/DBLP export及既有engineering historical-feed gap继续只影响年度Archive Completion Gate。

## Sources

- GPT-4.5 official launch — https://openai.com/index/introducing-gpt-4-5/
  （First Public: 2025-02-27；Accessed: 2026-08-20）
- GPT-4.5 System Card — https://cdn.openai.com/gpt-4-5-system-card-2272025.pdf
  （Published: 2025-02-27；31 pages；Accessed: 2026-08-20）
- OpenAI simple-evals — https://github.com/openai/simple-evals
  （Related evaluation artifact；mutable current repo；Accessed: 2026-08-20）
- DeepSeek Open Infra index — https://github.com/deepseek-ai/open-infra-index
  （Open Source Week: 2025-02-24～2025-03-01；identity/date/discovery owner；Accessed: 2026-08-20）
- DeepSeek Open Infra index activity — https://github.com/deepseek-ai/open-infra-index/activity
  （Day-level commit chronology；Accessed: 2026-08-20）
- DeepSeek 3FS official repository — https://github.com/deepseek-ai/3FS
  （Day 5 owner: 2025-02-28；current mutable artifact；Accessed: 2026-08-20）
- DeepEP official repository — https://github.com/deepseek-ai/DeepEP
  （Day 2 owner: 2025-02-25；current main is V2；Accessed: 2026-08-20）
- DeepEP V1 archived documentation — https://raw.githubusercontent.com/deepseek-ai/DeepEP/main/docs/legacy.md
  （NVSHMEM-based V1 mechanism/performance/notices；Accessed: 2026-08-20）
- FlashMLA official repository — https://github.com/deepseek-ai/FlashMLA
  （Day 1 owner: 2025-02-24；current main contains later kernels；Accessed: 2026-08-20）
- FlashMLA 2025-04 official deep-dive — https://github.com/deepseek-ai/FlashMLA/blob/main/docs/20250422-new-kernel-deep-dive.md
  （Related v1 baseline/evolution evidence；not backdated as W09 mechanism；Accessed: 2026-08-20）
- DeepGEMM official repository — https://github.com/deepseek-ai/DeepGEMM
  （Day 3 owner: 2025-02-26；current main contains later refactors/features；Accessed: 2026-08-20）
- DeepGEMM tests / legacy tree — https://github.com/deepseek-ai/DeepGEMM/tree/main/tests；
  https://github.com/deepseek-ai/DeepGEMM/tree/main/deep_gemm/legacy
  （Current artifact used with explicit W09 version boundary；Accessed: 2026-08-20）
- DualPipe official artifact — https://github.com/deepseek-ai/DualPipe
  （Code Event: 2025-02-27；mechanism first-public pre-window；Accessed: 2026-08-20）
- DeepSeek-V3 report DualPipe section — https://arxiv.org/html/2412.19437v2#S3.SS2.SSS1
  （Mechanism/evaluation lineage；v1: 2024-12-27；Accessed: 2026-08-20）
- DeepSeek V3/R1 profile data — https://github.com/deepseek-ai/profile-data
  （Related compute-communication overlap evidence；Accessed: 2026-08-20）
- EPLB official repository / planner — https://github.com/deepseek-ai/EPLB；
  https://raw.githubusercontent.com/deepseek-ai/EPLB/main/eplb.py
  （Day 4 artifact；Accessed: 2026-08-20）
- EPLB initial commit identity — https://github.com/deepseek-ai/EPLB/commit/f9bc62e84182eee311ec97c3ec3ce38f5073a646
  （Authored: 2025-02-26；content cache unavailable；Accessed: 2026-08-20）
- 3FS official repository — https://github.com/deepseek-ai/3FS
  （Day 5 open-source event: 2025-02-28；Accessed: 2026-08-20）
- 3FS design notes / metrics — https://raw.githubusercontent.com/deepseek-ai/3FS/main/docs/design_notes.md；
  https://raw.githubusercontent.com/deepseek-ai/3FS/main/docs/metrics.md
  （Architecture/consistency/recovery/evidence contract；Accessed: 2026-08-20）
- smallpond official repository / docs — https://github.com/deepseek-ai/smallpond；
  https://raw.githubusercontent.com/deepseek-ai/smallpond/main/docs/source/getstarted.rst；
  https://raw.githubusercontent.com/deepseek-ai/smallpond/main/docs/source/api.rst
  （Day 5 open-source event: 2025-02-28；Accessed: 2026-08-20）
- smallpond GraySort benchmark — https://raw.githubusercontent.com/deepseek-ai/smallpond/main/benchmarks/gray_sort_benchmark.py
  （Executable benchmark contract；Accessed: 2026-08-20）
- V3/R1 Online Inference System Overview — https://github.com/deepseek-ai/open-infra-index/blob/main/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md
  （First Public: 2025-03-01；statistics window: 2025-02-27～02-28 UTC+8；Accessed: 2026-08-20）
- Wan2.1 official repository — https://github.com/Wan-Video/Wan2.1
  （Code/weights released: 2025-02-25；technical report later 2025-03-21；Accessed: 2026-08-20）
- Wan2.1 technical report — https://arxiv.org/html/2503.20314v1
  （First Public: 2025-03-21；same-family later evidence；Accessed: 2026-08-20）
- Ai2 olmOCR official launch — https://allenai.org/blog/olmocr
  （First Public: 2025-02-25；Accessed: 2026-08-20）
- olmOCR v1 paper / artifact — https://arxiv.org/html/2502.18443v1；https://github.com/allenai/olmocr
  （First Public: 2025-02-25；v0.1.58 initial public release；Accessed: 2026-08-20）
- Microsoft Phi-4 mini/multimodal official launch — https://azure.microsoft.com/en-us/blog/empowering-innovation-the-next-generation-of-the-phi-family/
  （First Public: 2025-02-26；Accessed: 2026-08-20）
- Phi-4 multimodal official model card — https://huggingface.co/microsoft/Phi-4-multimodal-instruct
  （Model artifact/evaluation/training metadata；Accessed: 2026-08-20）
- Phi-4 mini official model card / technical report — https://huggingface.co/microsoft/Phi-4-mini-instruct；
  https://arxiv.org/html/2503.01743v1
  （Launch: 2025-02-26；report v1: 2025-03-03 same-family evidence；Accessed: 2026-08-20）
- SmolVLM2 official Blog — https://huggingface.co/blog/smolvlm2
  （First Public: 2025-02-20 → W08 spillback；Accessed: 2026-08-20）
- Cohere Command R7B Arabic release — https://cohere.com/blog/command-r7b-arabic；
  https://docs.cohere.com/changelog/command-r7b-arabic
  （First Public/open weights: 2025-02-27；Accessed: 2026-08-20）
- Command R7B Arabic model card / later report — https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025；
  https://arxiv.org/html/2503.14603v1
  （Release: 2025-02-27；report v1: 2025-03-18 same-family evidence；Accessed: 2026-08-20）
- Claude 3.7 Sonnet and Claude Code — https://www.anthropic.com/news/claude-3-7-sonnet（First Public: 2025-02-24；Accessed: 2026-08-20）
- Claude 3.7 Sonnet System Card — https://www.anthropic.com/system-cards（First Public: 2025-02-24；Accessed: 2026-08-20）
- SWE-RL v1 — https://arxiv.org/html/2502.18449v1（First Public: 2025-02-25；Accessed: 2026-08-20）
- SWE-RL official artifact — https://github.com/facebookresearch/swe-rl（Accessed: 2026-08-20）
- SpargeAttn v1 — https://arxiv.org/html/2502.18137v1（First Public: 2025-02-25；Accessed: 2026-08-20）
- SpargeAttn official artifact — https://github.com/thu-ml/SpargeAttn（Accessed: 2026-08-20）
- Drop-Upcycling v1 — https://arxiv.org/html/2502.19261v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- Drop-Upcycling official artifact — https://github.com/Taishi-N324/Drop-Upcycling（Accessed: 2026-08-20）
- Kanana v1 — https://arxiv.org/html/2502.18934v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- Kanana official model/repository lineage — https://github.com/kakao/kanana（Accessed: 2026-08-20）
- Towards Optimal Multi-draft Speculative Decoding v1 — https://arxiv.org/html/2502.18779v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- WebGames v1 — https://arxiv.org/html/2502.18356v1（First Public: 2025-02-25；Accessed: 2026-08-20）
- WebGames official environment — https://github.com/convergence-ai/webgames（Accessed: 2026-08-20）
- OmniAlign-V v1 — https://arxiv.org/html/2502.18411v1（First Public: 2025-02-25；Accessed: 2026-08-20）
- OmniAlign-V official artifact — https://github.com/PhoenixZ810/OmniAlign-V（Accessed: 2026-08-20）
- Cross-lingual factuality / X-FAKT v1 — https://arxiv.org/html/2502.17955v1（First Public: 2025-02-25；Accessed: 2026-08-20）
- X-FAKT official benchmark artifact — https://github.com/kmrtanmay/X_FaKT（Accessed: 2026-08-20）
- Rank1 v1 — https://arxiv.org/html/2502.18418v1（First Public: 2025-02-25；Accessed: 2026-08-20）
- Rank1 official artifact — https://github.com/orionw/rank1（Accessed: 2026-08-20）
- DeltaBench v1 — https://arxiv.org/html/2502.19361v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- DeltaBench official artifact — https://github.com/LivingFutureLab/DeltaBench（Dataset Release: 2025-03-05；Accessed: 2026-08-20）
- Agentic Reward Modeling v1 — https://arxiv.org/html/2502.19328v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- Agentic Reward Modeling official artifact — https://github.com/THU-KEG/Agentic-Reward-Modeling（Accessed: 2026-08-20）
- VEM v1 PDF — https://arxiv.org/pdf/2502.18906v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- VEM official artifact — https://github.com/microsoft/GUI-Agent-RL（Accessed: 2026-08-20）
- CritiQ v1 PDF — https://arxiv.org/pdf/2502.19279v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- CritiQ official artifact — https://github.com/KYLN24/CritiQ（Code Release: 2025-03-07；Accessed: 2026-08-20）
- Training LLMs with MXFP4 v1 — https://arxiv.org/html/2502.20586v1（First Public: 2025-02-27；Accessed: 2026-08-20）
- Microsoft microxcaling dependency — https://github.com/microsoft/microxcaling/tree/7bc41952de394f5cc5e782baf132e7c7542eb4e4（Accessed: 2026-08-20）
- Self-Training Elicits Concise Reasoning v1 — https://arxiv.org/html/2502.20122v1（First Public: 2025-02-27；Accessed: 2026-08-20）
- Concise Reasoning official artifact — https://github.com/TergelMunkhbat/concise-reasoning（Accessed: 2026-08-20）
- Granite Embedding Models v1 — https://arxiv.org/html/2502.20204v1（First Public: 2025-02-27；Accessed: 2026-08-20）
- Granite Embedding 30M model card — https://huggingface.co/ibm-granite/granite-embedding-30m-english（Accessed: 2026-08-20）
- WorldModelBench project — https://worldmodelbench-team.github.io/（First Public: 2025-02-27；Accessed: 2026-08-20）
- WorldModelBench v1 — https://arxiv.org/html/2502.20694v1（Paper v1: 2025-02-28；Accessed: 2026-08-20）
- LongRePS v1 PDF — https://arxiv.org/pdf/2502.20790v1（First Public: 2025-02-28；Accessed: 2026-08-20）
- LongRePS official artifact — https://github.com/lemon-prog123/LongRePS（Data Release: 2025-03-03；Accessed: 2026-08-20）
- PersonaBench v1 — https://arxiv.org/html/2502.20616v1（First Public: 2025-02-28；Accessed: 2026-08-20）
- PersonaBench revision history — https://arxiv.org/abs/2502.20616（v1: 2025-02-28；v2: 2025-08-20；Accessed: 2026-08-20）
- Safety Tax v1 — https://arxiv.org/html/2503.00555v1（First Public: 2025-03-01；Accessed: 2026-08-20）
- Safety Tax revision history — https://arxiv.org/abs/2503.00555（v1: 2025-03-01；v2: 2025-06-05；Accessed: 2026-08-20）
- Safety Tax official artifact — https://github.com/git-disl/Safety-Tax（Accessed: 2026-08-20；no immutable W09 release tag）
- ARIES v1 — https://arxiv.org/html/2502.21208v1（First Public: 2025-02-28；Accessed: 2026-08-20）
- ARIES revision metadata — https://arxiv.org/abs/2502.21208（v1 only；Accessed: 2026-08-20）
- GUI Pivot v1 — https://arxiv.org/html/2503.00401v1（First Public: 2025-03-01；Accessed: 2026-08-20）
- GUI Pivot revision metadata — https://arxiv.org/abs/2503.00401（v1: 2025-03-01；v2: 2025-03-04；Accessed: 2026-08-20）
- GUI Pivot official artifact — https://github.com/ZrW00/GUIPivot（Accessed: 2026-08-20；no immutable W09 release tag）
- RaPID v1 — https://arxiv.org/html/2503.00751v1（First Public: 2025-03-02；Accessed: 2026-08-20）
- RaPID metadata — https://arxiv.org/abs/2503.00751（v1 only；Accessed: 2026-08-20）
- Babel v1 — https://arxiv.org/html/2503.00865v1（First Public: 2025-03-02；Accessed: 2026-08-20）
- Babel official project — https://github.com/babel-llm/babel-llm（Accessed: 2026-08-20）
- Babel-83B model card — https://huggingface.co/Tower-Babel/Babel-83B（Artifact Update: 2025-03-05；Accessed: 2026-08-20）
- LADDER v1 — https://arxiv.org/html/2503.00735v1（First Public: 2025-03-02；Accessed: 2026-08-20）
- LADDER revision metadata — https://arxiv.org/abs/2503.00735（v1: 2025-03-02；v2: 2025-03-04；v3: 2025-03-05；Accessed: 2026-08-20）
- LADDER current artifact — https://github.com/Tufalabs/ladder（Accessed: 2026-08-20；no release tag；event-time full trainer unverified）
- Diffusion Planner v1 — https://arxiv.org/html/2503.00535v1（First Public: 2025-03-01；Accessed: 2026-08-20）
- Diffusion Veteran official artifact — https://github.com/Josh00-Lu/DiffusionVeteran（Accessed: 2026-08-20）
- Ray 2.43.0 signed release — https://github.com/ray-project/ray/releases/tag/ray-2.43.0（First Public: 2025-02-27；Accessed: 2026-08-20）
- Ray 2.43.0 Serve LLM docs — https://docs.ray.io/en/releases-2.43.0/serve/llm/overview.html（Accessed: 2026-08-20）
- JAX 0.5.1 official changelog — https://docs.jax.dev/en/latest/changelog.html#jax-0-5-1-feb-24-2025
  （First Public: 2025-02-24；Accessed: 2026-08-20）
- JAX 0.5.1 PyPI artifact metadata — https://pypi.org/project/jax/0.5.1/
  （Source/wheel uploaded: 2025-02-24；Accessed: 2026-08-20）
- Triton release history — https://github.com/triton-lang/triton/blob/main/RELEASE.md
  （3.2.0: 2025-01-22；3.3.0: 2025-04-09；Accessed: 2026-08-20）
- vLLM 0.7.3 package metadata — https://pypi.org/project/vllm/0.7.3/
  （Uploaded: 2025-02-20；Accessed: 2026-08-20）
- SGLang package metadata — https://pypi.org/project/sglang/0.4.3/；https://pypi.org/project/sglang/0.4.4/
  （0.4.3: 2025-02-14；0.4.4: 2025-03-13；Accessed: 2026-08-20）
- Transformers 4.49.0 package metadata — https://pypi.org/project/transformers/4.49.0/
  （Released: 2025-02-17；Accessed: 2026-08-20）
- Accelerate package metadata — https://pypi.org/project/accelerate/1.4.0/；https://pypi.org/project/accelerate/1.5.0/
  （1.4.0: 2025-02-17；1.5.0: 2025-03-12；Accessed: 2026-08-20）
- DeepSpeed package history — https://pypi.org/project/deepspeed/0.16.4/；https://pypi.org/project/deepspeed/0.16.5/
  （0.16.4: 2025-02-20；0.16.5: 2025-03-27；Accessed: 2026-08-20）
- MLX package history — https://pypi.org/project/mlx/0.22.1/；https://pypi.org/project/mlx/0.23.2/
  （0.22.1: 2025-02-06；0.23.2: 2025-03-05；Accessed: 2026-08-20）
- CUDA Toolkit 12.8 Blog / 12.8.1 docs — https://developer.nvidia.com/blog/cuda-toolkit-12-8-delivers-nvidia-blackwell-support；
  https://docs.nvidia.com/cuda/archive/12.8.1/cuda-toolkit-release-notes/index.html
  （12.8.0: 2025-01-31；12.8.1 docs: 2025-03-04；Accessed: 2026-08-20）
- NVIDIA Dynamo first-public Blog — https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/
  （First Public: 2025-03-18；Accessed: 2026-08-20）
- KServe v0.15 release lineage — https://github.com/kserve/kserve/releases/tag/v0.15.0-rc0；
  https://github.com/kserve/kserve/releases/tag/v0.15.0
  （RC0: 2025-01-27；GA: 2025-03-31；Accessed: 2026-08-20）
- Kubernetes v1.32.2 — https://github.com/kubernetes/kubernetes/releases/tag/v1.32.2；
  https://raw.githubusercontent.com/kubernetes/kubernetes/master/CHANGELOG/CHANGELOG-1.32.md
  （Released: 2025-02-13；includes CVE-2025-0426 fix；Accessed: 2026-08-20）
- ONNX Runtime release lineage — https://github.com/microsoft/onnxruntime/releases/tag/v1.20.1；
  https://github.com/microsoft/onnxruntime/releases/tag/v1.21.0
  （1.20.1: 2024-11-21；1.21.0: 2025-03-08；Accessed: 2026-08-20）
- OpenXLA/XLA releases page — https://github.com/openxla/xla/releases
  （No GitHub releases published；not proof of no code changes；Accessed: 2026-08-20）
- Unsloth Windows support announcement / implementation — https://github.com/unslothai/unsloth/discussions/1849；
  https://github.com/unslothai/unsloth/pull/1841
  （First Public: 2025-02-28；Accessed: 2026-08-20）
- Ray LLM APIs RFC — https://github.com/ray-project/ray/issues/50639（Accessed: 2026-08-20）
- Ray Serve batched-cancellation fix — https://github.com/ray-project/ray/pull/50054（Merged before 2.43.0；Accessed: 2026-08-20）
- GOAT v1 — https://arxiv.org/html/2502.16894v1（First Public: 2025-02-24；Accessed: 2026-08-20）
- GOAT revision metadata — https://arxiv.org/abs/2502.16894（v1: 2025-02-24；v2: 2025-02-26；later revisions retained in family；Accessed: 2026-08-20）
- GOAT official artifact — https://github.com/Facico/GOAT-PEFT（Accessed: 2026-08-20；no immutable W09 release tag）
- Stable-SPAM v1 — https://arxiv.org/html/2502.17055v1（First Public: 2025-02-24；Accessed: 2026-08-20）
- Stable-SPAM / GradientStabilizer revision metadata — https://arxiv.org/abs/2502.17055（v1 Stable-SPAM: 2025-02-24；current family renamed；Accessed: 2026-08-20）
- Stable-SPAM pre-release artifact — https://github.com/TianjinYellow/StableSPAM（Accessed: 2026-08-20；LLM/4-bit code TODO remains）
- VideoGrain v1 — https://arxiv.org/html/2502.17258v1（First Public: 2025-02-24；Accessed: 2026-08-20）
- VideoGrain official artifact — https://github.com/knightyxp/VideoGrain（Accessed: 2026-08-20）
- DICEPTION v1 — https://arxiv.org/html/2502.17157v1（First Public: 2025-02-24；Accessed: 2026-08-20）
- DICEPTION revision metadata — https://arxiv.org/abs/2502.17157（v1: 2025-02-24；v2: 2025-02-25；v3: 2025-10-09；Accessed: 2026-08-20）
- DICEPTION later artifact — https://github.com/aim-uofa/Diception（Model/Inference Release: 2025-09-21；Accessed: 2026-08-20）
- Mobile-Agent-V v1 — https://arxiv.org/html/2502.17110v1（First Public: 2025-02-24；Accessed: 2026-08-20）
- Mobile-Agent-V revision metadata — https://arxiv.org/abs/2502.17110（v1: 2025-02-24；v2: 2025-02-25；v3 renamed: 2025-06-03；Accessed: 2026-08-20）
- MobileAgent family repository — https://github.com/X-PLUG/MobileAgent（Accessed: 2026-08-20；Mobile-Agent-V v1 implementation not located）
- Thus Spake Long-Context LLM v1 — https://arxiv.org/html/2502.17129v1（First Public: 2025-02-24；Accessed: 2026-08-20）
- Thus Spake Long-Context LLM revision metadata — https://arxiv.org/abs/2502.17129（v1: 2025-02-24；v2: 2025-11-11；Accessed: 2026-08-20）
- Thus Spake author bibliography — https://github.com/OpenMOSS/Thus-Spake-Long-Context-LLM（Accessed: 2026-08-20）
- KV-Edit v1 — https://arxiv.org/html/2502.17363v1（First Public: 2025-02-24；Accessed: 2026-08-20）
- KV-Edit revision metadata — https://arxiv.org/abs/2502.17363（v1: 2025-02-24；v2: 2025-02-25；v3: 2025-03-12；Accessed: 2026-08-20）
- KV-Edit official artifact — https://github.com/Xilluill/KV-Edit（Code Release: 2025-02-25；Accessed: 2026-08-20；no immutable W09 tag）
- K-LoRA v1 — https://arxiv.org/html/2502.18461v1（First Public: 2025-02-25；Accessed: 2026-08-20）
- K-LoRA revision metadata — https://arxiv.org/abs/2502.18461（v1: 2025-02-25；v2: 2025-03-02；Accessed: 2026-08-20）
- K-LoRA official artifact — https://github.com/HVision-NKU/K-LoRA（Accessed: 2026-08-20；no immutable W09 tag）
- ART v1 — https://arxiv.org/html/2502.18364v1（First Public: 2025-02-25；Accessed: 2026-08-20）
- ART revision metadata — https://arxiv.org/abs/2502.18364（v1 only: 2025-02-25；Accessed: 2026-08-20）
- ART official repository withdrawal notice — https://github.com/microsoft/art-msra（Artifact Withdrawn: 2025-07-23；Accessed: 2026-08-20）
- Clustering-On-Difficulty v1 — https://arxiv.org/html/2502.17262v1（First Public: 2025-02-24；Accessed: 2026-08-20）
- Clustering-On-Difficulty revision metadata — https://arxiv.org/abs/2502.17262（v1: 2025-02-24；v2: 2025-05-23；v3: 2025-10-11；v4: 2026-03-09；Accessed: 2026-08-20）
- Visual Perception Token v1 — https://arxiv.org/html/2502.17425v1（First Public: 2025-02-24；Accessed: 2026-08-20）
- Visual Perception Token metadata — https://arxiv.org/abs/2502.17425（v1 only；Accessed: 2026-08-20）
- Visual Perception Token official artifact — https://github.com/yu-rp/VisualPerceptionToken（Accessed: 2026-08-20；no immutable W09 tag）
- MLLMs Know Where to Look v1 — https://arxiv.org/html/2502.17422v1（First Public: 2025-02-24；Accessed: 2026-08-20）
- MLLMs Know Where to Look metadata — https://arxiv.org/abs/2502.17422（v1 only；Accessed: 2026-08-20）
- ViCrop official artifact — https://github.com/saccharomycetes/mllms_know（Code Release: 2025-01-26；Accessed: 2026-08-20；no release tag）
- Finding the Sweet Spot v1 — https://arxiv.org/html/2502.16825v1（First Public: 2025-02-24；Accessed: 2026-08-20）
- Finding the Sweet Spot revision metadata — https://arxiv.org/abs/2502.16825（v1: 2025-02-24；v2: 2025-05-21；v3: 2025-06-28；Accessed: 2026-08-20）
- DPO Pair official artifact — https://github.com/XYaoooo/DPO_Pair（Accessed: 2026-08-20；no immutable W09 tag）
- WiCkeD v1 — https://arxiv.org/html/2502.18316v1（First Public: 2025-02-25；Accessed: 2026-08-20）
- WiCkeD metadata — https://arxiv.org/abs/2502.18316（v1 only；Accessed: 2026-08-20）
- WiCkeD official artifact — https://github.com/ahmedselhady/wicked-benchmarks（Accessed: 2026-08-20；no release tag）
- TheoremExplainAgent v1 — https://arxiv.org/html/2502.19400v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- TheoremExplainAgent revision metadata — https://arxiv.org/abs/2502.19400（v1: 2025-02-26；v2: 2025-05-25；Accessed: 2026-08-20）
- TheoremExplainAgent official artifact — https://github.com/TIGER-AI-Lab/TheoremExplainAgent（Code Release: 2025-03-03；Accessed: 2026-08-20）
- BIG-Bench Extra Hard v1 — https://arxiv.org/html/2502.19187v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- BIG-Bench Extra Hard revision metadata — https://arxiv.org/abs/2502.19187（v1: 2025-02-26；v2: 2025-05-06；Accessed: 2026-08-20）
- BIG-Bench Extra Hard official artifact — https://github.com/google-deepmind/bbeh（Accessed: 2026-08-20；no release tag）
- GHOST 2.0 v1 — https://arxiv.org/html/2502.18417v1（First Public: 2025-02-25；Accessed: 2026-08-20）
- GHOST 2.0 revision metadata — https://arxiv.org/abs/2502.18417（v1: 2025-02-25；v2: 2025-02-26；v3: 2025-02-27；v4: 2025-06-09；Accessed: 2026-08-20）
- GHOST 2.0 official artifact — https://github.com/ai-forever/ghost-2.0（Accessed: 2026-08-20；no immutable W09 tag）
- Plutus v1 — https://arxiv.org/html/2502.18772v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- Plutus metadata — https://arxiv.org/abs/2502.18772（v1 only；Accessed: 2026-08-20）
- Plutus official collection — https://huggingface.co/collections/TheFinAI/plutus-benchmarking-greek-financial-llms（Artifacts first updated: 2025-02-27；Accessed: 2026-08-20）
- Project Alexandria v1 — https://arxiv.org/html/2502.19413v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- Project Alexandria revision metadata — https://arxiv.org/abs/2502.19413（v1: 2025-02-26；v2: 2025-04-18；Accessed: 2026-08-20）
- Project Alexandria official artifact — https://github.com/LAION-AI/project-alexandria（Accessed: 2026-08-20；no immutable W09 release）
- REFUTE v1 PDF — https://arxiv.org/pdf/2502.19414v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- REFUTE metadata — https://arxiv.org/abs/2502.19414（v1 only；Accessed: 2026-08-20）
- REFUTE official artifact — https://github.com/falsifiers/REFUTE（Accessed: 2026-08-20；no release tag）
- Distill Any Depth v1 — https://arxiv.org/html/2502.19204v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- Distill Any Depth revision metadata — https://arxiv.org/abs/2502.19204（v1: 2025-02-26；v2: 2025-04-21；Accessed: 2026-08-20）
- Distill Any Depth official artifact — https://github.com/Westlake-AGI-Lab/Distill-Any-Depth（Artifact Release: 2025-02-26；Accessed: 2026-08-20；training/evaluation code status inconsistent）
- MMKE-Bench v1 — https://arxiv.org/html/2502.19870v1（First Public: 2025-02-27；Accessed: 2026-08-20）
- MMKE-Bench revision metadata — https://arxiv.org/abs/2502.19870（v1: 2025-02-27；v2: 2025-03-01；Accessed: 2026-08-20）
- MMKE-Bench official artifact — https://github.com/MMKE-Bench-ICLR/MMKE-Bench（Accessed: 2026-08-20；paper/artifact totals inconsistent）
- FSPO v1 — https://arxiv.org/html/2502.19312v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- FSPO revision metadata — https://arxiv.org/abs/2502.19312（v1: 2025-02-26；v2: 2026-04-16；Accessed: 2026-08-20）
- FSPO official artifact — https://github.com/Asap7772/fewshot-preference-optimization（Accessed: 2026-08-20；no release tag）
- Accented ATC ASR v1 — https://arxiv.org/html/2502.20311v1（First Public: 2025-02-27；Accessed: 2026-08-20）
- Accented ATC ASR metadata — https://arxiv.org/abs/2502.20311（v1 only；Accessed: 2026-08-20）
- Accented ATC ASR official artifact — https://github.com/aether-raid/atc-transcription（Accessed: 2026-08-20；dataset/model access restricted）
- AISafetyLab technical report v1 — https://arxiv.org/html/2502.16776v1（First Public: 2025-02-24；Accessed: 2026-08-20）
- AISafetyLab metadata — https://arxiv.org/abs/2502.16776（v1 only；Accessed: 2026-08-20）
- AISafetyLab official framework — https://github.com/thu-coai/AISafetyLab（Open-source Event: 2024-12-31 → W01 spillback；Accessed: 2026-08-20）
- PosterSum v1 — https://arxiv.org/html/2502.17540v1（First Public: 2025-02-24；Accessed: 2026-08-20）
- PosterSum metadata — https://arxiv.org/abs/2502.17540（v1 only；Accessed: 2026-08-20）
- PosterSum dataset — https://huggingface.co/datasets/rohitsaxena/PosterSum（16,305 pairs；Accessed: 2026-08-20）
- PosterSum official repository — https://github.com/saxenarohit/postersum（Accessed: 2026-08-20；code still marked coming soon）
- xAR v1 — https://arxiv.org/html/2502.20388v1（First Public: 2025-02-27；Accessed: 2026-08-20）
- xAR metadata — https://arxiv.org/abs/2502.20388（v1 only；Accessed: 2026-08-20）
- xAR official artifact — https://github.com/OliverRensu/xAR（Accessed: 2026-08-20；later code/checkpoint lineage，no W09 tag）
- LongRoPE2 v1 — https://arxiv.org/html/2502.20082v1（First Public: 2025-02-27；Accessed: 2026-08-20）
- LongRoPE2 metadata — https://arxiv.org/abs/2502.20082（v1 only；Accessed: 2026-08-20）
- LongRoPE / LongRoPE2 official artifact — https://github.com/microsoft/LongRoPE（Accessed: 2026-08-20；evolution-search only）
- ArtGS v1 — https://arxiv.org/html/2502.19459v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- ArtGS metadata — https://arxiv.org/abs/2502.19459（v1 only；Accessed: 2026-08-20）
- ArtGS official project/demo — https://articulate-gs.github.io/（Accessed: 2026-08-20；no public code artifact）
- FUSED v1 — https://arxiv.org/html/2502.20709v1（First Public: 2025-02-28；Accessed: 2026-08-20）
- FUSED metadata — https://arxiv.org/abs/2502.20709（v1 only；Accessed: 2026-08-20）
- FUSED official artifact — https://github.com/Zhong-Zhengyi/FUSED-Code（Accessed: 2026-08-20；no release tag/license metadata）
- Relation-Specific Neurons v1 PDF — https://arxiv.org/pdf/2502.17355v1（First Public: 2025-02-24；Accessed: 2026-08-20；HTML cache miss）
- Relation-Specific Neurons metadata — https://arxiv.org/abs/2502.17355（v1: 2025-02-24；v2: 2025-10-07；Accessed: 2026-08-20）
- Relation-Specific Neurons official artifact — https://github.com/cisnlp/relation-specific-neurons（Accessed: 2026-08-20；later three-commit artifact）
- MAMUT v1 — https://arxiv.org/html/2502.20855v1（First Public: 2025-02-28；Accessed: 2026-08-20）
- MAMUT metadata — https://arxiv.org/abs/2502.20855（v1 only；Accessed: 2026-08-20）
- MAMUT official generator — https://github.com/aieng-lab/math-mutator（Accessed: 2026-08-20）
- MAMUT generated datasets — https://huggingface.co/ddrg（Accessed: 2026-08-20；continuous artifact lineage）
- DVPO v1 — https://arxiv.org/html/2502.16944v1（First Public: 2025-02-24；Accessed: 2026-08-20）
- DVPO revision metadata — https://arxiv.org/abs/2502.16944（v1: 2025-02-24；v2: 2026-01-26；Accessed: 2026-08-20）
- DVPO later official code lineage — https://github.com/microsoft/DKI_LLM/tree/main/dvpo（Accessed: 2026-08-20；not W09 artifact evidence）
- NeoBERT v1 — https://arxiv.org/html/2502.19587v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- NeoBERT metadata — https://arxiv.org/abs/2502.19587（v1 only；Accessed: 2026-08-20）
- NeoBERT official repository — https://github.com/chandar-lab/NeoBERT（Accessed: 2026-08-20；mutable artifact）
- NeoBERT model card/weights — https://huggingface.co/chandar-lab/NeoBERT（Artifact Release: 2025-02-28；Accessed: 2026-08-20）
- Ext2Gen v1 — https://arxiv.org/html/2503.04789v1（First Public: 2025-02-28；Accessed: 2026-08-20）
- Ext2Gen revision metadata — https://arxiv.org/abs/2503.04789（v1: 2025-02-28；v2: 2025-03-12；v3: 2025-11-17；Accessed: 2026-08-20）
- SuperRAG v1 PDF — https://arxiv.org/pdf/2503.04790v1（First Public: 2025-02-28；Accessed: 2026-08-20；HTML cache unavailable）
- SuperRAG metadata — https://arxiv.org/abs/2503.04790（v1 only；Accessed: 2026-08-20）
- Kotaemon related project — https://github.com/Cinnamon/kotaemon（Accessed: 2026-08-20；continuous project，not frozen SuperRAG implementation）
- R2-T2 v1 — https://arxiv.org/html/2502.20395v1（First Public: 2025-02-27；Accessed: 2026-08-20）
- R2-T2 metadata — https://arxiv.org/abs/2502.20395（v1 only；Accessed: 2026-08-20）
- R2-T2 official artifact — https://github.com/tianyi-lab/R2-T2（Accessed: 2026-08-20；later 13-commit artifact）
- Self-rewarding Correction v1 — https://arxiv.org/html/2502.19613v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- Self-rewarding Correction metadata — https://arxiv.org/abs/2502.19613（v1 only；Accessed: 2026-08-20）
- Self-rewarding Correction official recipes — https://github.com/RLHFlow/Self-rewarding-reasoning-LLM（Accessed: 2026-08-20；continuous artifact）
- SoRFT v1 — https://arxiv.org/html/2502.20127v1（First Public: 2025-02-27；Accessed: 2026-08-20）
- SoRFT metadata — https://arxiv.org/abs/2502.20127（v1 only；Accessed: 2026-08-20）
- SoRFT ACL publication — https://aclanthology.org/2025.acl-long.559.pdf（Publication lineage；Accessed: 2026-08-20）
- UniTok v1 — https://arxiv.org/html/2502.20321v1（First Public: 2025-02-27；Accessed: 2026-08-20）
- UniTok metadata — https://arxiv.org/abs/2502.20321（v1 only；Accessed: 2026-08-20）
- UniTok official artifact — https://github.com/FoundationVision/UniTok（Release: 2025-02-28；Accessed: 2026-08-20；later updates separated）
- UniTok tokenizer weights — https://huggingface.co/FoundationVision/unitok_tokenizer（Release: 2025-02-28；Accessed: 2026-08-20）
- EDGS v1 — https://arxiv.org/html/2502.20378v1（First Public: 2025-02-27；Accessed: 2026-08-20）
- EDGS metadata — https://arxiv.org/abs/2502.20378（v1 only；Accessed: 2026-08-20）
- EDGS AAAI proceedings — https://ojs.aaai.org/index.php/AAAI/article/view/32460（Published: 2025-04-11；Accessed: 2026-08-20）
- FINEREASON v1 — https://arxiv.org/html/2502.20238v1（First Public: 2025-02-27；Accessed: 2026-08-20）
- FINEREASON metadata — https://arxiv.org/abs/2502.20238（v1 lineage；Accessed: 2026-08-20）
- FINEREASON official artifact — https://github.com/DAMO-NLP-SG/FineReason（Accessed: 2026-08-20；later ACL artifact）
- FINEREASON ACL publication — https://aclanthology.org/2025.acl-long.333.pdf（Publication lineage；Accessed: 2026-08-20）
- FlexiDiT v1 — https://arxiv.org/html/2502.20126v1（First Public: 2025-02-27；Accessed: 2026-08-20）
- FlexiDiT metadata — https://arxiv.org/abs/2502.20126（v1 only；Accessed: 2026-08-20）
- FlexiDiT CVPR publication — https://openaccess.thecvf.com/content/CVPR2025/papers/Anagnostidis_FlexiDiT_Your_Diffusion_Transformer_Can_Easily_Generate_High-Quality_Samples_with_CVPR_2025_paper.pdf（Publication lineage；Accessed: 2026-08-20）
- MedVLM-R1 v1 — https://arxiv.org/html/2502.19634v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- MedVLM-R1 metadata — https://arxiv.org/abs/2502.19634（v1: 2025-02-26；later revisions separated；Accessed: 2026-08-20）
- MedVLM-R1 later official code — https://github.com/JZPeterPan/MedVLM-R1（Accessed: 2026-08-20；one-commit later artifact）
- MedVLM-R1 later model card — https://huggingface.co/JZPeterPan/MedVLM-R1（Accessed: 2026-08-20；later artifact with failure cases）
- Mobius v1 — https://arxiv.org/html/2502.20307v1（First Public: 2025-02-27；Accessed: 2026-08-20）
- Mobius metadata — https://arxiv.org/abs/2502.20307（v1 only；Accessed: 2026-08-20）
- Mobius project page — http://mobius-diffusion.github.io/（Accessed: 2026-08-20；presentation artifact，code unresolved）
- Dream Engine v1 — https://arxiv.org/html/2502.20172v1（First Public: 2025-02-27；Accessed: 2026-08-20）
- Dream Engine metadata — https://arxiv.org/abs/2502.20172（v1 only；Accessed: 2026-08-20）
- Dream Engine official artifact — https://github.com/chenllliang/DreamEngine（Accessed: 2026-08-20；mutable current repository）
- R1-T1 v1 PDF — https://arxiv.org/pdf/2502.19735v1（First Public: 2025-02-27；Accessed: 2026-08-20；HTML source malformed）
- R1-T1 revision metadata — https://arxiv.org/abs/2502.19735（v1: 2025-02-27；v2: 2025-03-03；v3: 2025-05-26；Accessed: 2026-08-20）
- Variational Consistency Training v1 — https://arxiv.org/html/2502.18197v1（First Public: 2025-02-25；Accessed: 2026-08-20）
- Variational Consistency Training metadata — https://arxiv.org/abs/2502.18197（v1 lineage；Accessed: 2026-08-20）
- VCT official artifact — https://github.com/sony/vct（Accessed: 2026-08-20）
- LUME revision metadata — https://arxiv.org/abs/2502.15097（v1: 2025-02-20 → W08；v2: 2025-02-25；v3: 2025-02-27；Spillback only；Accessed: 2026-08-20）
- Hugging Face Daily Papers discovery pages — https://huggingface.co/papers/date/2025-02-24；
  https://huggingface.co/papers/date/2025-02-25；https://huggingface.co/papers/date/2025-02-26；
  https://huggingface.co/papers/date/2025-02-27；https://huggingface.co/papers/date/2025-02-28
  （Discovery only；Accessed: 2026-08-20）
- HF Daily Paper Newsletter 2025-02-28 archive — https://groups.google.com/g/hf-daily-paper-newsletter/c/2szeo1N45Qk
  （20 visible identities resolved；Accessed: 2026-08-20）
- arXiv Annual Report 2022 — https://info.arxiv.org/about/reports/2022_arXiv_annual_report.pdf
  （announcement cadence boundary only；Accessed: 2026-08-20）
- Predictive Data Selection v1 — https://arxiv.org/html/2503.00808v1（First Public: 2025-03-02；Accessed: 2026-08-20）
- Chain of Draft v1 — https://arxiv.org/html/2502.18600v1（First Public: 2025-02-25；Accessed: 2026-08-20）
- DeepSolution v1 — https://arxiv.org/html/2502.20730v1（First Public: 2025-02-28；Accessed: 2026-08-20）
- ViDoRAG v1 PDF — https://arxiv.org/pdf/2502.18017v1（First Public: 2025-02-25；HTML cache failed；Accessed: 2026-08-20）
- LettuceDetect v1 — https://arxiv.org/html/2502.17125v1（First Public: 2025-02-24；Accessed: 2026-08-20）
- TeleRAG v1 — https://arxiv.org/html/2502.20969v1（First Public: 2025-02-28；Accessed: 2026-08-20）
- DexGraspVLA v1 PDF — https://arxiv.org/pdf/2502.20900v1（First Public: 2025-02-28；HTML cache failed；Accessed: 2026-08-20）
- TokenSwift v1 — https://arxiv.org/html/2502.18890v1（First Public: 2025-02-26；Accessed: 2026-08-20）
- Self-Calibration v1 — https://arxiv.org/html/2503.00031v1（First Public: 2025-02-25；Accessed: 2026-08-20）
- DuoDecoding v1 — https://arxiv.org/html/2503.00784v1（First Public: 2025-03-02；Accessed: 2026-08-20）
- Web AI Agent Vulnerability v1 — https://arxiv.org/html/2502.20383v1（First Public: 2025-02-27；Accessed: 2026-08-20）
- LLM as a Broken Telephone v1 — https://arxiv.org/html/2502.20258v1（First Public: 2025-02-27；Accessed: 2026-08-20）
