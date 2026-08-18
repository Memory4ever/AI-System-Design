# AI Research Weekly — 2025-W20

> Coverage Window: 2025-05-12～2025-05-18
> Research Mode: Retrospective Primary-Source Backfill
> Re-audited: 2026-08-24
> Audit Status: Candidate Evidence Gate Passed — 81/81 Scored Owners Reconciled
> Historical Books Gate: Closed

## Executive Summary

旧档案只保留AlphaEvolve与Sufficient Context，明显欠召回。两轮完整重放后已闭合80个唯一评分owner；W21最终日期复核又确认BARREL（arXiv:2505.13529）v1为2025-05-18，因此W20的canonical分母增至81。本轮已完成BARREL事件版本全文、六维评分与年度账本回拨，并重新复算81个owner；Candidate Evidence Gate通过，年度Archive/Discovery Gate仍保持打开。

WorldPM 已通过 event-time v1/v2 全文与官方 repository 恢复。SageAttention3 的论文机制可核，但论文所称 code availability 与官方 repository 的 2025-09-27 release timeline 冲突，因此只把 artifact 日期保留为明确 dispute，不撤回其可读机制证据。SweRank等前置 family 与 Transformers 4.52 等后续事件均按 first-public date 路由，不重复计分。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 归档；搜索收录日与后续修订不替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery 与去重；论文机制回到正文。Crossref 仅做 Weekly metadata 交叉检查。
- 历史回填不补造 Daily；本轮来源Accessed为2026-08-22～2026-08-24。
- benchmark 缺少模型、硬件、长度、batch/concurrency、precision/quantization 与 SLO 时不做通用结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留AlphaEvolve、OpenAI Codex cloud preview及本周官方/工程owner。Sufficient Context论文v1实际首发于2024-11-09，本周Google follow-up只是related evidence node。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 当前owner以arXiv v1和event-time paper为主；64个retained packet全部闭合。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 保留KServe v0.15.1、NVLink Fusion版本/设计事实；Qwen3/MiMo report作为W18 revision evidence，不重复计分。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| AlphaEvolve | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| Sufficient Context for RAG | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete — 2025 follow-up node |
| DeepSeek-V3 Hardware Co-design | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Full Source Review Complete |
| BLIP3-o | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete |
| OpenAI Codex cloud preview | 3 | 5 | 5 | 5 | 5 | 2 | 25/30 | Full Source Review Complete — Product Fact |
| Parallel Scaling Law / ParScale | 5 | 5 | 4 | 5 | 4 | 3 | 26/30 | Full Source Review Complete |
| WorldPM | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — recovered |
| MiniMax-Speech | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete |
| MLE-Dojo | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete |
| OpenThinkIMG | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Full Source Review Complete |
| EnerVerse-AC | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete |
| GuardReasoner-VL | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete |
| Visual Planning | 5 | 4 | 3 | 5 | 4 | 4 | 25/30 | Full Source Review Complete |
| MMLongBench | 4 | 5 | 4 | 5 | 4 | 3 | 25/30 | Full Source Review Complete |
| KServe v0.15.1 | 2 | 5 | 5 | 5 | 5 | 1 | 23/30 | Full Source Review Complete — Version Fact |
| EWMBench | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Full Source Review Complete |
| Group Think | 5 | 4 | 3 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| MuToR | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| IKEA adaptive search | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review Complete |
| Learning from Peers | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | Full Source Review Complete |
| DanceGRPO | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Source Review Complete |
| Continual-pretraining Learning Dynamics | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| Overflow Prevention for Recurrent Long Context | 4 | 4 | 3 | 4 | 4 | 3 | 22/30 | Full Source Review Complete |
| ARC Text-to-Audio | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Source Review Complete |
| AM-Thinking-v1 | 2 | 3 | 4 | 4 | 4 | 3 | 20/30 | Full Source Review Complete — Model Recipe Fact |
| Aya Vision | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete |
| MulDimIF | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Full Source Review Complete |
| NavDP | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Source Review Complete |
| TRAIL | 3 | 4 | 4 | 4 | 5 | 3 | 23/30 | Full Source Review Complete |
| Tests as Prompt / WebApp1K | 3 | 3 | 4 | 3 | 4 | 3 | 20/30 | Full Source Review Complete |
| System Prompt Optimization with Meta-Learning | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review Complete |
| CoT Encyclopedia | 4 | 3 | 3 | 4 | 4 | 4 | 22/30 | Full Source Review Complete |
| J1 Judge RL | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review Complete |
| WavReward | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Full Source Review Complete |
| Omni-R1 Audio | 3 | 3 | 3 | 4 | 4 | 3 | 20/30 | Full Source Review Complete |
| Beyond Aha! | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete |
| End-to-End Vision Tokenizer Tuning | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Source Review Complete |
| SuperCoder | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Source Review Complete |
| Follow the Path | 3 | 3 | 3 | 4 | 4 | 3 | 20/30 | Full Source Review Complete |
| MatTools | 3 | 4 | 5 | 4 | 4 | 3 | 23/30 | Full Source Review Complete |
| Symbiotic Watermarking | 4 | 4 | 3 | 4 | 4 | 3 | 22/30 | Full Source Review Complete |
| MPS-Prover | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure |
| GIE-Bench | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure |
| VCRBench | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure |
| SageAttention3 | 5 | 5 | 5 | 5 | 4 | 3 | 27/30 | Full Source Review Complete — artifact date disputed |
| UCGM | 5 | 4 | 4 | 5 | 4 | 4 | 26/30 | Full Source Review Complete |
| H3DP | 5 | 4 | 4 | 5 | 4 | 3 | 25/30 | Full Source Review Complete |
| R2R2R | 5 | 5 | 5 | 5 | 4 | 3 | 27/30 | Full Source Review Complete |
| TokenAdapt | 5 | 4 | 4 | 5 | 4 | 4 | 26/30 | Full Source Review Complete |
| Continuous VAR | 5 | 4 | 4 | 5 | 4 | 4 | 26/30 | Full Source Review Complete |
| Deep Fusion | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete |
| UniSkill | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete |
| PointArena | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete |
| Memorization-Compression Cycles | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | Full Source Review Complete |
| Step1X-3D | 4 | 3 | 4 | 5 | 3 | 3 | 22/30 | Full Source Review Complete |
| MathCoder | 4 | 3 | 4 | 4 | 4 | 3 | 22/30 | Full Source Review Complete |
| Depth Any Prior | 4 | 3 | 4 | 5 | 3 | 3 | 22/30 | Full Source Review Complete |
| RAG hyperparameter sensitivity | 3 | 4 | 4 | 4 | 4 | 2 | 21/30 | Full Source Review Complete — limited study |
| Behind the Scenes of Maya | 3 | 3 | 4 | 4 | 3 | 3 | 20/30 | Full Source Review Complete — threshold |
| HealthBench | 4 | 5 | 5 | 5 | 5 | 2 | 26/30 | Full Source Review Complete |
| OMol25 | 4 | 5 | 5 | 5 | 4 | 2 | 25/30 | Full Source Review Complete |
| UMA | 5 | 5 | 5 | 5 | 4 | 2 | 26/30 | Full Source Review Complete |
| NVIDIA NVLink Fusion | 3 | 5 | 4 | 5 | 4 | 2 | 23/30 | Full Source Review Complete — partially disclosed fact |
| Time-R1 | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — W21 spillback |
| Orthogonal Residual Updates | 5 | 4 | 4 | 5 | 4 | 3 | 25/30 | Full Source Review Complete — W21 spillback |
| Synthetic Data RL | 4 | 4 | 5 | 5 | 4 | 3 | 25/30 | Full Source Review Complete — W21 spillback |
| BARREL | 4 | 3 | 4 | 4 | 4 | 4 | 23/30 | Full Source Review Complete — W21 spillback；numeric/reward-order evidence dispute preserved |
| LightLab | 3 | 3 | 3 | 5 | 2 | 3 | 19/30 | Low-score closure — narrow generation case |
| Style SVG | 3 | 2 | 3 | 5 | 2 | 3 | 18/30 | Low-score closure — narrow application |
| Agent taxonomy | 2 | 3 | 3 | 4 | 3 | 2 | 17/30 | Low-score closure — survey/taxonomy |
| ReSurgSAM2 | 3 | 2 | 3 | 4 | 2 | 3 | 17/30 | Low-score closure — narrow segmentation |
| 3D-Fixup | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Low-score closure — limited reusable mechanism |
| QuXAI | 3 | 2 | 2 | 4 | 1 | 3 | 15/30 | Low-score closure — weak project relevance |
| AdaptCLIP | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Low-score closure — incremental adaptation |
| MetaUAS | 3 | 3 | 3 | 4 | 2 | 3 | 18/30 | Low-score closure — narrow anomaly branch |
| OneNIP | 3 | 3 | 3 | 4 | 2 | 3 | 18/30 | Low-score closure — narrow imaging pipeline |
| AnoGen | 3 | 3 | 3 | 4 | 2 | 3 | 18/30 | Low-score closure — narrow anomaly generation |
| SkillFormer | 3 | 3 | 3 | 4 | 2 | 3 | 18/30 | Low-score closure — insufficient system principle |
| ViMRHP | 2 | 2 | 3 | 4 | 3 | 3 | 17/30 | Low-score closure — weak transfer |
| VISTAR | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure — incremental benchmark |
| Meta brain-language study | 3 | 3 | 3 | 5 | 2 | 3 | 19/30 | Low-score closure — scientific explanation |

账目：81 rows；25 high、39 medium、17 low；64/64 retained Full Source Reviews complete；17/17低分闭合；Pending 0、Blocked 0；SageAttention3 artifact-date dispute 1；BARREL numeric/reward-order evidence dispute 1。

### Deep Analysis 1 — AlphaEvolve

- First Public: 2025-05-14
- Status: Google DeepMind official research system
- Primary Source: https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/
- Evolution Relationship: Direct Evolution

#### Why

算法发现若只依赖一次生成，很难兼顾探索广度与结果可靠性；可执行 evaluator 能把搜索闭环变成可积累的优化过程。

#### Principle and Mechanism

AlphaEvolve 以模型 ensemble 生成程序候选，用自动 evaluator 评分，再通过 evolutionary loop 选择、变异和迭代。

#### Trade-off and Evidence Boundary

可执行 objective 提供强反馈，但系统只优化被编码的指标；evaluator 漏洞、测试不完整、算力成本和现实部署验证成为新 failure modes。

#### Connection and Evolution

知识树位置：第 62、74～78、80 章。Must Read；优先 refine Workflow/Evaluation。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 2 — Sufficient Context for RAG

- First Public: 2024-11-09（论文 v1）；2025-05-14 为 Google Research follow-up
- Status: ICLR 2025 paper + Google Research official follow-up
- Primary Source: https://research.google/blog/deeper-insights-into-retrieval-augmented-generation-the-role-of-sufficient-context/
- Evolution Relationship: Direct Evolution

#### Why

retrieval relevance 不能回答“证据是否足够支持答案”；相关但不充分的上下文反而会提高模型错误作答的信心。

#### Principle and Mechanism

研究定义 sufficient context，训练/提示 autorater 对 query-context pair 分类，并将该信号与 model confidence 结合做 selective generation。

#### Trade-off and Evidence Boundary

增加 sufficiency gate 可改善 accuracy-coverage 权衡，却引入另一个可能误判的模型、额外 latency 和阈值治理；论文结果绑定特定数据集与模型。

#### Connection and Evolution

知识树位置：第 62、71、72、76 章。Must Read；补全 RAG 的 abstention/control loop。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### AlphaEvolve

- **Candidate / Week / Score:** AlphaEvolve / 2025-W20 / 25/30。
- **Source Family ID:** `deepmind-alphaevolve-evaluator-search`。
- **Source Type:** Google DeepMind official research announcement、44 页 white paper、公开数学结果 Colab；系统代码未开源。
- **First-public Date / Revision History:** announcement 与 white paper 2025-05-14；未发现版本化 revision history，后续产品计划不反投影。
- **Direct Primary Sources:** DeepMind blog；AlphaEvolve white paper；alphaevolve_results mathematical-results artifact。
- **Related Primary Sources:** FunSearch 作为直接前序；Google内部 Borg scheduler、TPU circuit、Pallas/FlashAttention优化案例只按 white paper 的受限披露处理。
- **Access and Verification Status:** Verified；white paper 的系统设计、任务 specification、prompt sampling、generation、evaluation、database、distributed pipeline、全部案例、ablation、related work、discussion与 appendices 已读。私有代码/生产配置不可核验。
- **Full-read Coverage:** metadata；FunSearch演进；完整 controller loop；evaluation cascade/multi-score；MAP-Elites/island database；async pipeline；matrix/math、cluster scheduling、kernel/circuit/attention cases；三随机种子ablation；限制和数学 artifact。
- **Original Problem:** 单次或重复独立 LLM sampling 缺少可积累的外部反馈与 lineage，很难在巨大程序空间持续改进，并且生成正确性不能由语言流畅度保证。
- **Why the Previous Design Was Reasonable:** 人工算法设计、固定search operators或单函数FunSearch更易审查、限定搜索空间并控制 evaluator成本；对不可自动验证任务，人仍是必要 evaluator。
- **Changed Constraint:** frontier coding models可修改数百行/多函数代码，而大量数学与系统优化问题可提供机器可执行 evaluator；昂贵但并行的 evaluation使较少高质量samples成为可能。
- **Mechanism:** 人定义 initial program、EVOLVE blocks、evaluation function和metrics；prompt sampler从program database抽取parent/inspirations与反馈；Gemini 2.0 Flash/Pro ensemble产生diff；evaluator cascade先廉价过滤再昂贵验证；带scores/outputs/lineage的program回写database，以MAP-Elites/island式selection平衡探索与利用。
- **State Ownership:** program database拥有候选、lineage、metrics与失败历史；controller拥有budget和queue；evaluator拥有“可接受”判据；LLM只提出diff。部署authority仍归工程师、verifier与发布系统。
- **Control Flow / Data Flow:** sample(parent,inspirations) → build prompt → LLM diff → apply/compile → evaluator cascade并行执行 → attach metrics/artifacts → database selection → next generation。asyncio controller、LLM samplers与evaluation nodes并发，目标是budget内吞吐而非单候选latency。
- **Implementation Details:** 支持全文件/多语言、multiobjective、meta-prompt evolution、LLM-generated auxiliary feedback、不同抽象层（直接对象/constructor/search algorithm）和每候选可到约100 compute-hours的并行evaluation。完整infrastructure、retry/idempotency/security sandbox为 `Not Disclosed`。
- **Evaluation Setup:** 数学上超过50个open problems；矩阵乘法与kissing-number等；Google系统案例含Borg scheduling simulator/unseen workload test/全fleet观测、matrix kernel、TPU circuit formal/工程验证和attention kernel。不同案例 evaluator与部署门槛不同，不能汇总为单一score。
- **Baselines / Ablations / Sensitivity:** 对matrix tensor decomposition与kissing number，用三随机种子比较full method、no evolution、no context、small LLM only、no full-file evolution、no meta-prompt evolution，按compute budget画curve；也与FunSearch能力范围对比。没有跨所有任务的uniform baseline或 evaluator-corruption sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** generation models为Gemini 2.0 Flash+Pro；某些evaluation可并行使用accelerators并耗费小时/约100 compute-hours。GPU/TPU SKU、precision、prompt length、global concurrency、总search budget和服务SLO未统一披露。
- **What the Evidence Actually Proves:** 在可程序化且可自动评分的问题上，带lineage/evolution/evaluator的外部workflow比论文给出的独立sampling ablations更能持续发现高分候选；部分结果经过数学证明或生产前/后独立验证。
- **What It Does Not Prove:** 不证明LLM自我修改权重、任意科学问题可自动验证、evaluator无漏洞、search结果自动可部署、通用Agent自治或所有案例相对人类/传统optimizer的成本优势。
- **Limitations / Threats to Validity:** 主要实现私有；任务由团队选择；各案例budget不完整；自动evaluator适用性是硬门槛；模拟器/测试分布可能过拟合；部分辅助score来自LLM；生产案例需人工/现有verification stack。
- **Trade-offs / New Failure Modes:** 强反馈提高可验证性，却把系统风险转移到objective misspecification、evaluator gaming、search-level overfitting、duplicate/lineage膨胀、异步stale selection、sandbox escape、昂贵并行compute与部署authority混淆。
- **Where the Previous Design Still Applies:** 不可自动评分、真实实验成本高、搜索空间可用传统optimizer覆盖、代码变更需强可解释性或高风险生产系统时，human-designed algorithm、deterministic search和manual review仍合理。
- **Evolution Relationship:** 对FunSearch为 `Direct Evolution`（单函数/单目标/百万samples → 全文件/多目标/丰富反馈/更少samples）；对Agent Workflow为 `Principle Reuse`，不是通用workflow替代品。
- **ROADMAP Node:** Ch62、Ch74–78、Ch80；Ch77为主owner，Ch62拥有 EvalSpec/evidence contract。
- **Target and Adjacent Chapters Read:** Ch61–63、Ch73–78、Ch80已读。
- 本周候选已完成最终 Books disposition；实际章节修改或拒绝理由见各候选的 `Changed Files or Rejection Reason`。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch77，沉淀 evaluator-driven artifact search。
- **Changed Files or Rejection Reason:** 已复核 `books/part-06-agent/77-workflow.md`。
- **Open Questions:** private scheduler/database schema、failure recovery、sandbox、evaluator versioning、search budget accounting、stale asynchronous selection以及production promotion policy未完整公开。

### Sufficient Context: A New Lens on RAG Systems

- **Candidate / Week / Score:** Sufficient Context source family / 2025-W20 / 25/30；2025事件是official follow-up，不是论文首次公开。
- **Source Family ID:** `google-sufficient-context-rag-2411.06037`。
- **Source Type:** ICLR 2025论文、arXiv v1–v3、Google Research 2025-05-14 follow-up与作者 prompts/artifact。
- **First-public Date / Revision History:** arXiv v1 2024-11-09、v2 2024-12-07、v3 2025-04-23；Google Research blog 2025-05-14。本周归档的是follow-up，年度索引必须保留原始first-public。
- **Direct Primary Sources:** arXiv 2411.06037 v3 PDF（25页）、ICLR paper、Google Research blog。
- **Related Primary Sources:** 作者GitHub prompts；Vertex AI re-ranker是官方工程关联，但不能据此断言实现了论文完整selective-generation pipeline。
- **Access and Verification Status:** Verified；论文Introduction/Related Work、definition/autorater、datasets/model analysis、selective generation、fine-tuning、limitations、完整appendix/prompts与训练设置已读。
- **Full-read Coverage:** metadata/revisions；sufficiency定义与AIS/entailment差异；115例人工集和autoraters；FreshQA/Musique/HotPotQA；五个model families；LLMEval；confidence+sufficiency logistic gate；LoRA experiment；limitations/appendix。
- **Original Problem:** relevance或gold-document标签不能区分“检索结果谈论同一主题”与“证据足以构造答案”，因此RAG错误无法归因于retrieval insufficiency还是generator misuse。
- **Why the Previous Design Was Reasonable:** relevance/reranking可在大corpus中高效提高recall/precision；严格“insufficient即拒答”会丢掉模型借助参数知识正确回答的样本，故旧pipeline并非错误。
- **Changed Constraint:** RAG生产系统需要可控accuracy–coverage与abstention，而不是只优化top-k relevance或最终accuracy；多跳、冲突、时效问题使“含答案字符串”不足。
- **Mechanism:** 不使用ground-truth answer，仅对(query, context)判断是否存在context支持的plausible answer；以Gemini 1.5 Pro 1-shot autorater做分析、FLAMe 24B做较便宜online signal；把binary sufficiency与model self-rated P(True)/P(Correct)输入logistic regression预测hallucination，再按threshold abstain。
- **State Ownership:** retriever/packer拥有context set；sufficiency rater产生派生signal；generation model产生answer/confidence；policy layer拥有threshold、coverage目标与abstention决定。任何rater都不是ground truth owner。
- **Control Flow / Data Flow:** retrieve/pack（截断至6K实验context）→ sufficiency rater（FLAMe按1600-token chunks，任一chunk sufficient即正）+ self-rated confidence → logistic score → threshold → answer或abstain；可扩展为re-query但论文未实现完整iterative loop。
- **Implementation Details:** 115个gold-labeled query-context pairs上Gemini 1.5 Pro 1-shot autorater报告93% accuracy；selective gate做100次random hyperparameter search。LoRA Mistral-7B-Instruct-v0.3用2,000 examples、rank4/alpha8、2 epochs、batch16、LR1e-5，训练不稳定且不同checkpoint差异大。
- **Evaluation Setup:** FreshQA True Premise 452例；Musique-Ans与HotPotQA dev各500例；contexts测试2K/6K/10K后主实验用6K。Models为gpt-4o-2024-08-06、gemini-1.5-pro-0514、claude-3-5-sonnet-20240620、gemma-2-27b-it、Mistral-7B-Instruct-v0.3。
- **Baselines / Ablations / Sensitivity:** closed-book vs vanilla RAG；sufficient/insufficient slices；confidence-only vs confidence+sufficiency；Gemini/FLAMe/TRUE-NLI/contains-GT autoraters；random/insufficient-context `idk` fine-tuning mixes；context length sensitivity。Gemma onMusique无sufficiency增益，证明机制并非普适。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** models/length/LoRA batch如上；hardware、API concurrency、precision、rater latency/cost与production SLO `Not Disclosed`。因此2–10%只绑定论文datasets/coverage regions。
- **What the Evidence Actually Proves:** relevance、sufficiency与faithfulness是不同failure dimensions；在论文特定QA/model/rater条件下，sufficiency可作为confidence之外的selective-generation signal，并在部分coverage区间提高answered-query accuracy。
- **What It Does Not Prove:** 不证明binary rater是真值、所有RAG任务收益2–10%、insufficient context必须拒答、reranker等于sufficiency gate、summarization/multimodal/enterprise corpus可直接迁移，或能消除hallucination。
- **Limitations / Threats to Validity:**只研究QA；retrieval方法对sufficiency的因果未系统比较；autorater和LLMEval均可能错；115例校准集小；API models可漂移；FLAMe chunk-any-positive规则可能漏跨chunk组合/产生假阳性；阈值与distribution shift相关。
- **Trade-offs / New Failure Modes:** 增加rater和confidence调用带来latency/cost、threshold治理、false-sufficient与false-abstain；更高selective accuracy以coverage下降为代价；过度依赖sufficiency会错过参数知识或部分context有帮助的答案。
- **Where the Previous Design Still Applies:** relevance retrieval/reranking仍负责candidate generation；高coverage/低风险任务可少abstain；确定知识库可用entailment/规则；小模型若本身accuracy太低，sufficiency signal可能无增益。
- **Evolution Relationship:** 对relevance-only RAG是 `Direct Evolution`（candidate relevance → evidence sufficiency → selective policy）；与faithfulness checker是 `Layering / Dependency`，二者不可互换。
- **ROADMAP Node:** Ch62、Ch71、Ch72、Ch76；Ch72为主owner，Ch62拥有rater/evaluation identity。
- **Target and Adjacent Chapters Read:** Ch61–63、Ch71–73、Ch75–77已读。
- **Existing Coverage:** Ch72已有relevance/sufficiency/faithfulness三层、re-query/abstain control loop、rater calibration/latency/false-sufficient与benchmark边界；其中iterative re-query是本项目工程推断，已与论文本身机制区分。需Books Gate确认措辞。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch72，区分 relevance、sufficiency 与 faithfulness。
- **Changed Files or Rejection Reason:** 已复核 `books/part-06-agent/72-rag.md`；论文未实现的 iterative retrieval 不倒灌正文。
- **Open Questions:** cross-domain calibration、online rater cost/latency、multi-document跨chunk sufficiency、retrieval loop效果、false-abstain业务成本与multimodal extension。

### DeepSeek-V3 hardware co-design

- **Primary / date / owner:** `2505.09343`，v1 2025-05-14，28/30；`INFER-TENSORRT-LLM` Ch49，handoff `MODEL-MOE` / `TRAIN-DISTRIBUTED-TRAINING`。
- **Problem / mechanism / ownership:** 2,048×H800训练把模型容量、低精度算力、跨节点带宽与尾延迟耦合。MLA压缩推理状态，细粒度MoE改变activation/communication比例，FP8改变数值与kernel contract，多平面网络分流collectives；control plane必须把模型拓扑、precision与network path作为同一execution plan。
- **Evidence boundary:** 作者system report证明该模型/硬件合同中的可行性与bottlenecks，不证明MLA/MoE/FP8对任意模型、GPU、网络或SLO均占优。
- **Trade-off / coexistence / disposition:** 新增precision verification、routing load、专用通信layout与软硬件耦合；较小规模或可移植性优先仍可dense+BF16。Books Pending — `Refine — Existing Argument`。

### BLIP3-o

- **Primary / date / owner:** `2505.09568`，v1 2025-05-14，27/30；`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24，handoff Ch23。
- **Problem / mechanism / ownership:** 理解与生成专模易分别优化，但统一交互要求共享语义状态。BLIP3-o先训练image understanding再训练generation，以diffusion transformer预测CLIP feature而非只在VAE latent上生成；共享主干输出进入迭代feature correction，再由decoder还原图像。
- **Evidence boundary:** 多理解/生成benchmark和开放artifact支持顺序训练减少部分能力干扰及CLIP-feature diffusion可行；不证明统一模型普遍优于两个专模，也不消除data/decoder依赖。
- **Trade-off / coexistence / disposition:** 统一接口换来目标竞争、更多训练阶段与迭代生成成本；隔离和SLO不同的服务仍适合专模。Books Pending — `Integrate — New Mechanism Candidate`。

### OpenAI Codex cloud preview

- **Primary / date / owner:** OpenAI official launch 2025-05-16，25/30；`AGENT-PLATFORM` Ch84，handoff Ch81。
- **Problem / mechanism / ownership:** IDE同步补全适合短反馈，长任务需要异步、隔离、并行与审计。平台为每个任务构建独立cloud sandbox，装载repository/environment instructions，Agent读写并运行tests/linters，最终返回diff与logs；workspace和execution state按任务隔离。
- **Evidence boundary:** 官方发布只证明产品行为和task lifecycle，不披露模型训练/规划机制，亦不能从演示外推安全性与成功率。
- **Trade-off / coexistence / disposition:** 获得并行与execution evidence，代价是environment rebuild、secret/network permission、stale checkout、merge conflict和反馈延迟；微小修改仍适合本地同步工具。Books Pending — `Refine Existing Argument / Version Fact Boundary`。

### Parallel Scaling Law / ParScale

- **Primary / date / owner:** `2505.10475`，v1 2025-05-15，26/30；`MODEL-TRANSFORMER-LAYER` Ch17，handoff Ch49。
- **Problem / mechanism / ownership:** parameter scaling增加memory，test-time token scaling增加serial latency。ParScale对同一input施加P个可学习、多样transformation，复用共享参数并行forward，再动态聚合P路output；新增的是parallel activation/aggregation state，而非P份weights。
- **Evidence boundary:** 作者pretraining与scaling-law fit支持其合同中的memory/latency trade-off；不证明`O(log P)`等效在所有规模/任务成立，也未消除FLOPs、并行hardware与aggregation cost。
- **Trade-off / coexistence / disposition:** 增加activation、同步和聚合复杂度；并行资源不足时传统scaling仍合理。`Emerging / Experimental`。

### MiniMax-Speech

- **Primary / date / owner:** `2505.07916`，v1 2025-05-12，25/30；`MULTIMODAL-REPRESENTATION` Ch23，handoff Ch24。
- **Problem / mechanism / ownership:** zero-shot TTS常依赖reference transcript或不可分离speaker embedding。learnable speaker encoder直接从audio抽取timbre state，AR Transformer生成声学序列，Flow-VAE改善重建；timbre representation还能被LoRA、text-to-voice或专业克隆路径使用。
- **Evidence boundary:** 32 languages、WER、speaker similarity、主观评测与TTS Arena只支持作者model中的质量；不证明跨语言公平、consent/privacy安全或production real-time，硬件/batch/SLO未充分披露。
- **Trade-off / coexistence / disposition:** 可复用timbre也形成可复制身份状态，带来provenance与滥用风险；有转写监督的TTS在发音可控与审计优先时仍适用。Books Pending — `Refine Existing Argument`。

### MLE-Dojo

- **Primary / date / owner:** `2505.07782`，v1 2025-05-12，28/30；`PLATFORM-EVALUATION-SYSTEM` Ch66，handoff Ch81。
- **Problem / mechanism / ownership:** 静态QA或single-attempt benchmark无法测ML engineering Agent的试验—失败—修正循环。MLE-Dojo基于200+ Kaggle challenges构造Gym-style executable environment；Agent action修改data/code/hyperparameters，environment执行并返回score/error，trajectory可用于SFT/RL与复现。
- **Evidence boundary:** 8个frontier LLM的轨迹支持迭代反馈改善结果且长程纠错仍弱；不等同真实组织中的permission、cost、implicit requirement或production correctness。
- **Trade-off / coexistence / disposition:** executable verifier提高证据强度，但受environment封装、leakage、compute与reward gaming影响；静态benchmark仍适合便宜回归。Books Pending — `Integrate New Mechanism Candidate`。

### OpenThinkIMG / V-ToolRL

- **Primary / date / owner:** `2505.08617`，v1 2025-05-13，25/30；`AGENT-TOOL-CALLING` Ch78，handoff Ch23。
- **Problem / mechanism / ownership:** 静态SFT能模仿tool calls，却不能根据中间image/tool result动态选下一action。统一vision-tool interface和trajectory先初始化policy，再以真实tool interaction的task-success feedback做V-ToolRL；Agent state在multimodal context、proposal、tool output与下一决策间循环。
- **Evidence boundary:** Qwen2-VL-2B chart reasoning只证明单域work-in-progress相对baselines改善；不证明通用视觉Agent、tool safety或recovery。
- **Trade-off / coexistence / disposition:** 自适应调用换来execution cost、sparse reward、tool nondeterminism与policy exploitation；稳定窄任务仍适合SFT。Books Pending — `Integrate New Mechanism Candidate`。

### EnerVerse-AC

- **Primary / date / owner:** `2505.09723`，v1 2025-05-14，25/30；`MULTIMODAL-WORLD-MODELS` Ch25，handoff Ch26。
- **Problem / mechanism / ownership:** 真实robot与高保真simulator可靠但昂贵，普通text-to-video又不保证action consistency。EnerVerse-AC以多级action conditioning与ray-map encoding把动作和多视角几何写入future observation generation；current observation+proposed action→world-model rollout→synthetic next observation/trajectory→policy test/data augmentation。
- **Evidence boundary:** 作者manipulation数据支持可控多视角未来与受限数据/评估用途；不证明rollout可替代物理世界、长期误差不累积或sim-to-real安全。
- **Trade-off / coexistence / disposition:** 降sampling成本但引入model bias、causal shortcut与evaluator/model共错；真实robot/simulator仍是physical release gate。Books Pending — `Integrate New Mechanism Candidate`。

### GuardReasoner-VL

- **Primary / date / owner:** `2505.11049`，v1 2025-05-16，25/30；`PLATFORM-SECURITY` Ch72，handoff Ch66。
- **Problem / mechanism / ownership:** one-pass multimodal classifier快，但复杂图文policy interpretation需要reasoning；无约束CoT又拉高cost。123K samples/631K steps先SFT，rejection sampling与safety-aware concatenation扩样，再以dynamic clipping和length-aware reward联合accuracy、format与token cost做online RL。
- **Evidence boundary:** 作者benchmark平均F1 improvement只支持其data/model/strategy；不证明CoT faithful、对新policy/attack稳定，也不能替代operating point与成本评估。
- **Trade-off / coexistence / disposition:** 可审查推理换来latency、reward gaming与解释泄漏；低风险高吞吐仍可calibrated classifier，复杂边界再升级reasoning guard。Books Pending — `Refine Existing Argument`。

### Visual Planning

- **Primary / date / owner:** `2505.11409`，v1 2025-05-16，25/30；`AGENT-PLANNING` Ch79，handoff Ch23/24。
- **Problem / mechanism / ownership:** text CoT把空间状态序列化会丢邻接与布局。Visual Planning把image sequence作为intermediate plan state，VPRL/GRPO以environment success训练vision model；observation image→visual waypoint/state→next visual state，文本不再是唯一规划媒介。
- **Evidence boundary:** FrozenLake/Maze/MiniBehavior只证明visual intermediate state是可行supplementary channel；不证明无文本规划普适或真实环境可执行，后续revision不得倒灌。
- **Trade-off / coexistence / disposition:** 保留空间结构却增加image generation cost、verification与error accumulation；离散规则任务仍宜symbolic/text plan。`Emerging / Experimental`。

### MMLongBench

- **Primary / date / owner:** `2505.10610`，v1 2025-05-15，25/30；`PLATFORM-EVALUATION-SYSTEM` Ch66，handoff Ch22。
- **Problem / mechanism / ownership:** 单needle或短图文benchmark不能区分长窗口声明、cross-modal retrieval与multi-image reasoning。13,331 examples覆盖五类任务，以cross-modal tokenization标准化到8K–128K，对46个LCVLM统一测试；evaluation owner必须同时记录length、image composition、task family与judge。
- **Evidence boundary:** 证明单任务是总体能力的弱proxy且当时models仍脆弱；不证明真实latency/cost，也不能把不同proprietary tokenizer的token数完全等同。
- **Trade-off / coexistence / disposition:** 覆盖广但昂贵且judge/tokenization有bias；窄regression仍适合CI。Books Pending — `Refine Existing Argument`。

### KServe v0.15.1

- **Primary / date / owner:** official GitHub release `v0.15.1`，W20 event，23/30；`PLATFORM-KSERVE` Ch61，handoff Ch53。
- **Problem / mechanism / ownership:** v0.15.0功能基线之后，production adoption需要patch修复compatibility/correctness，而非再次引入架构。controller/runtime/manifest在同minor family更新，desired-state/reconciliation contract不变；具体行为必须逐条绑定release notes/PR。
- **Evidence boundary:** tag只证明版本事实与change set，不证明新机制或对任意cluster无regression。
- **Trade-off / coexistence / disposition:** 仍需CRD/version compatibility、canary和rollback；稳定cluster可风险评估后暂缓。`Weekly Only — Version Fact`。

### EWMBench

- **Primary / date / owner:** `2505.09694`，v1 2025-05-14、v2 05-18，23/30；`PLATFORM-EVALUATION-SYSTEM` Ch66，handoff Ch25。
- **Problem / mechanism / ownership:** FID/视觉逼真度不能判断embodied rollout是否保持scene、action和semantic consistency。EWMBench把evidence拆为scene consistency、motion correctness与semantic alignment，toolkit对world-model outputs生成多维证据。
- **Evidence boundary:** 比较视频/世界模型支持“感知质量不蕴含action-grounded correctness”；不证明三维指标覆盖physical safety、long causal chain或closed-loop policy。
- **Trade-off / coexistence / disposition:** 诊断增强但metrics仍可被gaming，aggregation会隐藏弱项；必须与simulator/real rollout联合。Books Pending — `Integrate New Mechanism Candidate`。

### Group Think

- **Primary / date / owner:** `2505.11107`，v1 2025-05-16，24/30；`AGENT-MULTI-AGENT` Ch82，handoff Ch56。
- **Problem / mechanism / ownership:** turn-based multi-agent可互审但串行增加latency，独立CoT又重复探索。Group Think让同一LLM并发维护多个thinker trajectories，各自generation state隔离，但可见peers的partial tokens并在token granularity改向/接力。
- **Evidence boundary:** open-source LLM/local GPU实验支持其小batch实现复用idle compute；不证明token sharing对所有模型/任务稳健，correlated error、fairness与memory contention未闭合。
- **Trade-off / coexistence / disposition:** 降轮次等待却增加同步、shared-state identity与干扰；通信稀疏任务仍适合turn-based，确定任务更适合单路径。`Emerging / Experimental`。

### MuToR — Multi-Token Prediction Needs Registers

- **Primary / date / owner:** `2505.10518`，v1 2025-05-15，24/30；`TRAIN-PRETRAINING` Ch28，handoff Ch29/48。
- **Problem / mechanism / ownership:** multi-token heads增强pretraining signal但架构改动和objective mismatch难迁移。MuToR在input中交错少量learnable register tokens，每个register预测不同future target，主干与next-token objective保持兼容；register是训练时显式future-prediction state。
- **Evidence boundary:** language/vision pretraining、SFT、PEFT支持轻量迁移；不证明future-token supervision必然改善downstream或能直接转为serving speedup。
- **Trade-off / coexistence / disposition:** 增加sequence positions、loss coupling与compute；标准next-token仍是稳定baseline，speculative runtime仍需独立verifier。Books Pending — `Refine Existing Argument`。

### IKEA adaptive search agent

- **Primary / date / owner:** `2505.07596`，v1 2025-05-12，24/30；`AGENT-RAG` Ch76，handoff Ch66。
- **Problem / mechanism / ownership:** always-retrieve增加冗余、冲突evidence与latency，never-retrieve又越过知识边界。该工作以knowledge-boundary-aware data/reward用RL联合优化correctness、少检索与必要时检索；internal reasoning先作sufficiency proposal，不足才search，evidence回流后answer。
- **Evidence boundary:** 多knowledge tasks支持作者setup下降低retrieval frequency并改善指标；不证明模型真正“知道自己不知道”、OOD calibration、source trust或conflict resolution。
- **Trade-off / coexistence / disposition:** 误判会漏检，reward可能把confidence proxy学成shortcut；高风险仍应强制verification，稳定低风险可直接回答。Books Pending — `Integrate New Mechanism Candidate`。

### Learning from Peers / LeaP

- **Primary / date / owner:** `2505.07787`，v1 2025-05-12，23/30；`AGENT-REFLECTION` Ch80，handoff Ch82。
- **Problem / mechanism / ownership:** 单reasoning path被错误prefix支配后难恢复，末尾self-consistency太晚。LeaP让多paths周期总结intermediate state，经routing共享给peers，其他path在生成中吸收；LeaP-T通过finetuning学习summarization/reflection。
- **Evidence boundary:** AIME/AIMO/GPQA与指定models支持及时peer signal缓解Prefix Dominance Trap；不证明大模型、开放域或tool tasks同样，比较受sample budget/parallel compute影响。
- **Trade-off / coexistence / disposition:** 增加tokens、routing、error propagation与homogenization；单路径headroom足且预算敏感时仍优先。Books Pending — `Refine Existing Argument`。

### DanceGRPO

- **Primary / date / owner:** `2505.07818`，v1 2025-05-12，23/30；`TRAIN-GRPO` Ch33，handoff Ch24。
- **Problem / mechanism / ownership:** DDPO/DPOK在多prompt视觉生成中不稳，单reward又不覆盖aesthetics/alignment/motion。DanceGRPO把group-relative advantage用于diffusion/rectified-flow sample groups，以五类reward model提供相对信号。
- **Evidence boundary:** 三任务、四foundation models支持作者配置下的稳定性与改善；不证明reward代表human preference，也不把8月后revisions倒灌W20。
- **Trade-off / coexistence / disposition:** 省critic但sampling昂贵，仍有reward hacking、group bias与credit assignment；小数据/明确pairwise preference仍可DPO类方法。Books Pending — `Refine Existing Argument`。

### Learning Dynamics in Continual Pre-Training

- **Primary / date / owner:** `2505.07796`，v1 2025-05-12，24/30；`TRAIN-PRETRAINING` Ch28，handoff Ch27。
- **Problem / mechanism / ownership:** CPT常凭经验选peak LR、steps与replay，domain loss下降可能伴随general forgetting。该工作把loss transition分为distribution shift与LR annealing，拟合跨step/LR schedule的scaling law；control plane据domain/general validation选择LR、steps与replay。
- **Evidence boundary:** 多datasets/hyperparameters支持经验律在测试范围内预测loss；不证明loss等价downstream capability，也不保证跨model、optimizer、污染或drift外推。
- **Trade-off / coexistence / disposition:** 依赖early measurements、稳定分布和comparable validation；小规模或强drift仍需online sweep/early stop。Books Pending — `Integrate New Mechanism Candidate`。

### Overflow Prevention for Recurrent Long Context（OPRM）

- **Primary / date / score / owner:** `2505.07793`，v1 2025-05-12，22/30；`MODEL-LONG-CONTEXT`。作者代码：`assafbk/OPRM`。
- **Problem / mechanism / ownership:** fixed-size recurrent state 在线性成本下合理，但信息密度超过 capacity 后会 overflow。OPRM把 context 切 chunk，以 prefix+chunk+query 并行 speculative prefill，经 IDK filter 后按 first-token entropy/query likelihood 选择一个 hidden state 继续 decode；chunk states 只是候选，selector 拥有 commit，未选信息被丢弃。
- **Evaluation boundary:** Falcon3-Mamba、Falcon-Mamba、RecurrentGemma、RWKV6，LongBench/v2/InfiniteBench及 selector analyses 证明很多任务可由相关单 chunk 改善；不证明跨 chunk reasoning 完整，也不证明 entropy 是事实置信度或150K等于有效记忆。
- **Trade-off / coexistence:** 重复 prefix compute、selection error、跨 chunk evidence loss；信息确可压入 recurrent state 时原方案仍更简单。Books Pending；不打开 Historical Books Gate。

### ARC Text-to-Audio

- **Primary / date / score / owner:** `2505.08175`，v1 2025-05-13，23/30；`MULTIMODAL-GENERATIVE-PARADIGMS`。
- **Problem / mechanism / ownership:** multi-step diffusion/flow 保质量但 latency 高；teacher-trajectory distillation 又复杂。Adversarial Relativistic-Contrastive post-training以 relativistic adversarial objective 加 contrastive discriminator 压缩 Stable Audio Open sampling；generator拥有 sample trajectory，discriminator/reward 提供相对质量与 prompt signal。
- **Evaluation boundary:** 论文把12s、44.1kHz stereo的H100约75ms和mobile约7s绑定其模型与实现；不证明所有长度、设备、并发、感知质量或real-time SLO。新增 adversarial instability、mode artifact 与 hardware-specific kernel 依赖；离线质量优先仍可使用多步 sampler。
- **Disposition:** Books Pending — Experimental mechanism case。

### AM-Thinking-v1

- **Primary / date / score / owner:** `2505.08311`，paper v1 2025-05-13；model card记录05-10 release，20/30；`TRAIN-GRPO`。
- **Problem / mechanism / ownership:** 671B MoE reasoning部署成本高；该 family 以 Qwen2.5-32B base 经 SFT 与 dual-stage RL 发布中型 reasoning checkpoint。publisher拥有 dataset/reward/checkpoint lineage，推理模型只拥有 output state。
- **Evidence boundary:** AIME、LiveCodeBench等为作者 benchmark；只证明artifact与公开recipe事实，不证明私有训练细节完整、leaderboard公平或安全成熟，且作者明确 red-team 不足。
- **Disposition:** `Weekly Only — Model Recipe Fact`；不把产品能力反推为通用机制。

### Aya Vision technical paper

- **Primary / date / score / owner:** `2505.08751`，paper v1 2025-05-13；official family release 2025-03-04，24/30；`MULTIMODAL-REPRESENTATION`。
- **Problem / mechanism / ownership:** vision encoder接入后直接 multimodal tune 容易破坏 text/multilingual ability。方案联合 synthetic multilingual multimodal annotation 与 cross-modal model merging，在保留 text weights 的同时注入 vision branch；language/vision checkpoints是 merge inputs，merged artifact必须独立验证两类能力。
- **Evaluation boundary:** 8B/32B、23 languages、AyaVisionBench/mWildVision支持该 setup 下的 trade-off 改善；不证明 judge 绝对质量或所有低资源语言覆盖。新增 synthetic/translation bias 与 merge interference；单语或 vision-only 仍可普通 finetune。
- **Chronology:** W20只记录 technical-paper revision，不覆盖W10附近official family owner。Books Pending。

### MulDimIF

- **Primary / date / score / owner:** `2505.07591`，v1 2025-05-12，23/30；`PLATFORM-EVALUATION-SYSTEM`。
- **Problem / mechanism / ownership:** 窄 templated benchmark 不能区分 constraint pattern、category、difficulty与conflict。MulDimIF构造三类pattern×四类constraint×四级difficulty，经 expansion、conflict detection、rewrite生成 code-verifiable tests，并复用为RL data；spec拥有constraints，code verifier拥有pass/fail，model answer不自证。
- **Evaluation boundary:** event-time v1为1,200 tests、19 models/7 families；current repository扩展不得倒灌。证明维度化可以诊断约束失败，不证明自动生成无 leakage、validator 不可 gaming 或 attention analysis 是唯一因果。
- **Trade-off / coexistence:** template/validator gaming；语义性任务仍需 human/independent judge。Books Pending。

### NavDP

- **Primary / date / score / owner:** `2505.08712`，v1 2025-05-13，23/30；`MULTIMODAL-EMBODIED-VLA`。
- **Problem / mechanism / ownership:** map/localization与real demos可靠但昂贵且 embodiment-specific；simulation-only policy有domain gap。shared transformer编码local observations，diffusion policy生成候选trajectory，critic选择；simulation privileged global info只生成高质 demos/negatives，不进入deployment observation。policy拥有proposal，critic拥有selection，controller/environment拥有commit与truth。
- **Evaluation boundary:** 363.2km/1244 scenes、约2500 trajectories/GPU/day、三类robot与real tests支持论文平台的zero-shot transfer；Gaussian-splat real-to-sim仍是preliminary，不证明任意sensor、calibration、terrain或safety envelope。
- **Trade-off / coexistence:** critic misranking、diffusion latency、sim bias；结构化环境中 mapping-based navigation仍更可审计。Books Pending。

### TRAIL

- **Primary / date / score / owner:** `2505.08638`，v1 2025-05-13，23/30；`PLATFORM-TRACE`。
- **Problem / mechanism / ownership:** final success rate或manual review无法定位tool、reasoning、multi-agent超长异构trace中的failure。TRAIL建立error taxonomy并标注148条single/multi-agent SWE/open-world traces；trace spans/events保留位置和category，judge输出类型+位置，human annotation仍是reference owner。
- **Evaluation boundary:** 148 traces、800+ errors，best model joint localization约11%；证明当时long-context LLM难做trace debugging，不证明taxonomy穷尽、human labels无歧义或自动judge可替代operator。
- **Trade-off / coexistence:** annotation成本与trace privacy；结构化确定性错误仍适合rules。Books Pending。

### Tests as Prompt / WebApp1K

- **Primary / date / score / owner:** `2505.09027`，v1 2025-05-13，20/30；`PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-TOOL-CALLING`。
- **Problem / mechanism / ownership:** NL spec+hidden tests不能测model是否能从executable contract理解application behavior。WebApp1K用1,000个web-app challenges/20 domains，以tests同时作为prompt与verifier；model生成implementation，sandbox/test runner拥有pass/fail truth，error taxonomy区分context/instruction/API failure。
- **Evaluation boundary:** 19 frontier models、TDD与language prompt、context/multi-feature complexity证明test-first setting暴露instruction loss；不证明tests完整表达需求、React代表general SE或passing即安全。
- **Trade-off / coexistence:** test overfit与framework drift；非功能需求仍需要NL spec与人工验收。Books Pending。

### System Prompt Optimization with Meta-Learning（MetaSPO）

- **Primary / date / score / owner:** `2505.09666`，v1 2025-05-14，24/30；`AGENT-PROMPT`。
- **Problem / mechanism / ownership:** per-query user-prompt optimization不可复用；system prompt需跨任务稳定又与task-specific prompt协同。MetaSPO用 bilevel/meta-learning outer loop跨datasets优化system prompt，inner loop迭代user prompts；system prompt是shared policy state，user prompt是task adaptation state，evaluator提供两层objective。
- **Evaluation boundary:** 14 unseen datasets/5 domains及generic/CoT/genetic baselines支持特定task distribution上的transfer；不证明自然语言prompt具有连续优化保证、跨model/vendor稳定或security policy不可绕过。
- **Trade-off / coexistence:** meta-overfit、API drift、evaluation calls；少量固定任务仍可手写prompt。Books Pending。

### CoT Encyclopedia

- **Primary / date / score / owner:** `2505.10185`，v1 2025-05-15，22/30；`AGENT-REFLECTION`。
- **Problem / mechanism / ownership:** 预定义reasoning taxonomy受human intuition限制。该工作从generated CoTs抽取criteria，embedding/clustering为categories，再生成contrastive rubrics，并用strategy prediction/steering选择轨迹；trace corpus拥有observed state，cluster/rubric是derived state，controller而非taxonomy拥有最终选择。
- **Evaluation boundary:** interpretability/comprehensiveness、strategy prediction/steering只证明derived taxonomy在所测tasks有用；不证明CoT忠实反映内部机制、clusters跨model稳定或steering因果纯净。
- **Trade-off / coexistence:** judge/embedding bias与taxonomy drift；明确已知策略仍可规则化。Books Pending。

### J1 — RL-trained LLM-as-a-Judge

- **Primary / date / score / owner:** `2505.10320`，v1 2025-05-15，24/30；`PLATFORM-EVALUATION-SYSTEM`。
- **Problem / mechanism / ownership:** prompted/distilled judge易有position bias，subjective prompt又缺直接verifiable reward。J1把可验证与synthetic non-verifiable preference转为reward，以GRPO训练judge生成thought+verdict，并用swapped-order consistency抑制position bias；reference pair拥有label，judge只产生derived evidence，release gate不归judge。
- **Evaluation boundary:** 8B/32B/70B、22K synthetic pairs、多个judge benchmarks及reward/seed/thought-length ablations支持论文distribution上的改善；不证明synthetic preference代表人类、多judge独立或CoT faithful。
- **Trade-off / coexistence:** judge reward hacking与self-generated reference bias；高风险评测仍需规则、人工或独立证据。Books Pending。

### WavReward

- **Primary / date / score / owner:** `2505.09558`，v1 2025-05-14，22/30；`PLATFORM-EVALUATION-SYSTEM`。
- **Problem / mechanism / ownership:** text judge忽略prosody、emotion与acoustic instruction。WavReward以audio-LM evaluator覆盖理解/生成及多种acoustic attributes，并以reasoning、nonlinear reward和multi-sample feedback训练；audio artifact是input，reward model产生多维score，人类/benchmark仍为calibration owner。
- **Evaluation boundary:** in/out-domain objective和subjective A/B及component ablations证明该data/model上的spoken evaluation改善；不证明headline跨语言、codec、noise泛化，或judge可作为ground truth。
- **Trade-off / coexistence:** 重audio inference与correlated bias；内容型低成本检查仍可ASR+规则。Books Pending。

### Omni-R1 Audio

- **Primary / date / score / owner:** `2505.09439`，v1 2025-05-14，20/30；`TRAIN-GRPO`，handoff `MULTIMODAL-REPRESENTATION`。
- **Problem / mechanism / ownership:** audio QA finetuning通常假设必须有audio-labelled data，但错误可能主要来自text reasoning。作者在Qwen2.5-Omni上以GRPO比较with-audio、without-audio和text-only data；audio encoder提供perceptual state，language policy提供reasoning state，verifier只奖励final answer。
- **Evaluation boundary:** MMAU sounds/music/speech/mixes、AVQA及text-only ablations支持部分增益来自text reasoning；不证明audio不重要、所有audio tasks相同或perception error已解决。
- **Trade-off / coexistence:** final reward可能掩盖modality shortcut；细粒度听觉仍需要acoustic-specific data。Books Pending。

### Beyond “Aha!”

- **Primary / date / score / owner:** `2505.10554`，v1 2025-05-15，24/30；`TRAIN-GRPO`。
- **Problem / mechanism / ownership:** outcome RL可偶发self-correction，却不能稳定训练deduction、induction、abduction等meta-ability。该工作生成self-verifiable tasks分别训练这些ability，再parameter-space merge并做domain RL；individual checkpoints拥有ability state，merge recipe组合，verifier reward驱动domain policy。
- **Evaluation boundary:** math/code/science及individual/merge/domain-RL ablations支持该recipe在论文benchmarks改善；不证明taxonomy完备、merge无interference或“Aha”机制被解释。
- **Trade-off / coexistence:** 多checkpoint、merge conflict与synthetic shortcut；强verifier domain仍可只用outcome RL。Books Pending。

### End-to-End Vision Tokenizer Tuning（ETT）

- **Primary / date / score / owner:** `2505.10562`，v1 2025-05-15，23/30；`MULTIMODAL-REPRESENTATION`。
- **Problem / mechanism / ownership:** frozen VQ tokenizer按reconstruction优化，容易丢OCR/semantic detail，且下游LLM梯度不能穿过discrete index。ETT用codebook embeddings经MLP接LLM，使tokenizer/projector/LLM端到端反传，并以caption CE加VQ reconstruction loss约束semantic与fidelity；随后冻结tokenizer做Chat/Gen post-training。
- **Evaluation boundary:** GQA/TextVQA/POPE/MME等understanding、generation/reconstruction和loss ablation支持选定256²/data/model上的2–6%改善；不证明高分辨率、视频、所有codebook或joint training都稳定。
- **Trade-off / coexistence:** coupled optimization、artifact incompatibility与catastrophic drift；模块复用与稳定接口场景仍适合frozen tokenizer。Books Pending。

### SuperCoder — assembly superoptimization

- **Primary / date / score / owner:** `2505.11480`，v1 2025-05-16，23/30；`AGENT-TOOL-CALLING`，handoff `INFER-TENSORRT-LLM`。
- **Problem / mechanism / ownership:** compiler rule/search保证语义但易停在局部策略；LLM可提proposal，却必须同时满足bit-level correctness和真实speed。该工作以8,072 assembly programs构造executable benchmark，RL reward结合tests与speedup；model proposal→compile/run tests→benchmark→reward/update，sandbox拥有machine state，tests拥有semantic gate，timer拥有performance evidence。
- **Evaluation boundary:** 23 LLMs、Qwen2.5-Coder-7B baseline/finetuned支持特定ISA/compiler/hardware corpus上的superoptimization；不证明跨CPU/flags、timing稳定或passing tests等于全语义等价。
- **Trade-off / coexistence:** unsafe code、benchmark noise和overfit；compiler优化仍是可信默认baseline。Books Pending。

### Follow the Path / fs1

- **Primary / date / score / owner:** `2505.11140`，v1 2025-05-16，20/30；`AGENT-RAG`。
- **Problem / mechanism / ownership:** 从LRM蒸馏CoT会复制parametric hallucination；knowledge-intensive reasoning需要grounded trajectory。该工作以knowledge-graph paths条件化large reasoner生成3.9K grounded traces，再fine-tune 8个instruction models；KG path是provenance input，teacher产生trajectory，student学习，answer evaluator只判结果。
- **Evaluation boundary:** 6个open-domain QA、23.9K questions及size/hop analyses支持KG-covered tasks上的增益；不证明trace每一步事实、KG coverage完整或开放web同样有效。
- **Trade-off / coexistence:** KG staleness/coverage与teacher contamination；动态事实仍需要live RAG。Books Pending。

### MatTools

- **Primary / date / score / owner:** `2505.10852`，v1 2025-05-16，23/30；`PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-TOOL-CALLING`。
- **Problem / mechanism / ownership:** materials QA不证明model能正确调用physics packages。MatTools以69,225 package/docs QA加49 real tasks/138 subtasks构造tool-use benchmark；LLM生成Python，sandbox运行pymatgen等tool，evaluator验证artifact/result。tool version与environment拥有runtime truth，model不自证。
- **Evaluation boundary:** generalist/specialist模型在该suite上的差异支持executable evaluation价值；不证明物理结果科学有效、49 tasks覆盖材料研究或safe execution充分。
- **Trade-off / coexistence:** dependency/version/license与domain verifier成本；高风险科学流程仍需要专家脚本与人工复核。Books Pending。

### Symbiotic Watermarking / SymMark

- **Primary / date / score / owner:** `2505.09924`，v1 2025-05-15，22/30；`PLATFORM-SECURITY`。
- **Problem / mechanism / ownership:** logits-based与sampling-based watermark在detectability、robustness、quality/security间各有边界。SymMark以serial/parallel/hybrid组合两类watermark，hybrid按token entropy选择logit transform、按semantic entropy选择sampling watermark；secret/key与detector state由provenance system拥有，generator只产生marked sequence。
- **Evaluation boundary:** 多datasets/models/attacks证明论文setting能改善多目标trade-off；不证明cryptographic security、未知paraphrase鲁棒或不影响alignment，且W23另有alignment反证family。
- **Trade-off / coexistence:** 双信号干涉、threshold治理和sampling drift；单watermark在窄threat model仍更简单。Books Pending。

### WorldPM — recovered preference-pretraining packet

- **Primary / date / score / owner:** `2505.10527` v1 2025-05-15、v2 2025-05-18 与 `QwenLM/WorldPM` official repository；25/30；`TRAIN-RLHF`，handoff `TRAIN-GRPO`/`PLATFORM-EVALUATION-SYSTEM`。
- **Problem / mechanism / ownership:** 小规模人工偏好对可控但覆盖不足；WorldPM 从 StackExchange/Reddit/Quora 的 reply-vote gap 建 pair，选用约15M pairs/约30B tokens，以 Bradley–Terry loss 预训练 Qwen2.5 1.5B～72B scalar reward head。builder 拥有 pair/provenance/filter，trainer 拥有 model/optimizer，inference 只输出未校准 scalar score。
- **Evaluation contract:** 7组20个subtasks、BoN-256 与后续 HelpSteer2/UltraFeedback/RLHFlow adaptation；context 2048、1 epoch、batch 10K、1536 steps、Adam、LR 3e-6，并含 batch/LR ablation。硬件、precision、production concurrency/SLO 未披露。
- **Proof boundary / trade-off:** 支持作者合同中的 reward initialization 与若干 objective/adversarial task 改善，不证明 votes 等于 truth、universal preference、calibration 或 safe policy；平台偏差、污染、length/markdown shortcut、reward hacking 与 judge coupling 是新 failure modes。`Review Pending` 已关闭。

### SageAttention3 — FP4 attention with disputed artifact date

- **Primary / date / score / owner:** `2505.11594` v1 2025-05-16；27/30；`INFER-TENSORRT-LLM`，handoff `TRAIN-DISTRIBUTED-TRAINING`。
- **Mechanism / ownership:** NVFP4 1×16 microscaling QK/PV、Q/K smoothing、two-level P scale 与 fused softmax/quant producer warp；SageBwd 将 7 个 backward matmul 中 6 个降为 INT8，量化 scale 与 accumulation boundary 成为 execution-plan state。
- **Evaluation contract:** RTX 5090 inference、RTX 4090 training，覆盖 Qwen/Llama/CogVideo/Hunyuan/Mochi/Flux/SD3.5；headline kernel TOPS/相对 FA2、xFormers 只在作者所列 shape 与 comparison contract 内成立，未提供 portability、fleet concurrency 或 SLO。
- **Dispute / trade-off:** paper 声称 code available，但 official repository 将 SageAttention3 release 记为 2025-09-27；机制证据保留，artifact 不倒写 W20。新代价是 format/hardware coupling、quant error、shape cliffs 与 backward economics。

### UCGM

- **Primary / date / score / owner:** `2505.07447`，v1 2025-05-12，26/30；`MULTIMODAL-GENERATIVE-PARADIGMS`。
- **Mechanism:** consistency ratio 统一 diffusion、flow 与 few-step generation，UCGM-S 通过 x/z parameterization 与 extrapolation 改变采样控制流。
- **Evidence boundary:** CIFAR/ImageNet、多个 architecture 与 FID-50K 支持作者图像合同；不证明 text/video 或未披露 hardware/SLO 下的通用收益。数值稳定、distillation/solver coupling 是代价。

### H3DP

- **Primary / date / score / owner:** `2505.07819`，v1 2025-05-12，25/30；`MULTIMODAL-EMBODIED-VLA`。
- **Mechanism:** depth-aware observation state、multi-scale residual quantization 与 coarse-to-fine diffusion policy 把感知到控制的状态分层。
- **Evidence boundary:** 44 sim+4 real tasks、3 seeds、20 episodes、200 epochs 与 top-5 checkpoint selection；不证明未见 embodiment、contact-rich calibration 或真实长期闭环。旧的 single-scale policy 在状态简单时仍更可控。

### R2R2R

- **Primary / date / score / owner:** `2505.09601`，v1 2025-05-14，27/30；`TRAIN-DATA`，handoff `MULTIMODAL-EMBODIED-VLA`。
- **Mechanism / flow:** scan/demo → 3DGS/GARField/mesh → differentiable render/DINO 6DoF → Slerp/grasp/IK → IsaacLab，显式保存 geometry、trajectory 与 simulator lineage。
- **Evaluation boundary:** RTX4090 data throughput、GH200 policy training、1050 YuMi trials与TOST只证明给定 rigid/quasi-static pipeline；dynamics、collision 与 sim-to-real uncertainty 未闭合。代价是复杂 artifact/version chain。

### TokenAdapt

- **Primary / date / score / owner:** `2505.09738`，v1 2025-05-14，26/30；`MODEL-TOKENIZER`。
- **Mechanism:** local decomposition、global kNN、blend/fallback 与 supertokens 把 vocabulary adaptation 从一次静态替换变成受控 mapping pipeline。
- **Evidence boundary:** Llama/Qwen 3B、81K/128K vocabulary 及 multilingual/code/math perplexity；不证明下游 task、hardware 或 serving compatibility。新风险是 token identity、embedding drift 与 artifact incompatibility。

### Continuous VAR

- **Primary / date / score / owner:** `2505.07812`，v1 2025-05-12，26/30；`MULTIMODAL-GENERATIVE-PARADIGMS`。
- **Mechanism:** strictly proper energy score 与 continuous candidates 避免 fixed-VQ 的离散 bottleneck，改变 next-scale training target。
- **Evidence boundary:** ImageNet 上 GIVT/MAR/VAR 对比与 LR/collapse sensitivity；不证明非图像、生产 latency 或跨 tokenizer 泛化。fixed VQ 在接口稳定/缓存复用重要时仍合理。

### Deep Fusion

- **Primary / date / score / owner:** `2505.10046`，v1 2025-05-15，24/30；`MULTIMODAL-GENERATIVE-PARADIGMS`。
- **Mechanism:** frozen LLM 与 trainable DiT 通过 attention fusion 分离语言 prior 与 generation state。
- **Evidence boundary:** controlled GenEval 支持所选模型/数据上的 layering branch，不证明所有 unified architecture 或端到端 joint training 应被替代；跨模块 alignment 与双模型成本是 trade-off。

### UniSkill

- **Primary / date / score / owner:** `2505.08787`，v1 2025-05-13，24/30；`MULTIMODAL-EMBODIED-VLA`。
- **Mechanism:** inverse-skill dynamics、image-edit forward model 与 skill-conditioned diffusion 把 cross-embodiment transfer拆成可追踪 skill state。
- **Evidence boundary:** 约100 demos、3 prompts、20 rollouts；不证明 viewpoint/contact/open-loop/schema shift 下稳定。直接 per-robot imitation 在少量固定 embodiment 时仍更简单。

### PointArena

- **Primary / date / score / owner:** `2505.09990`，v1 2025-05-15，24/30；`PLATFORM-EVALUATION-SYSTEM`，handoff Ch26。
- **Mechanism:** PointBench、PointBattle 与 PointAct 把 3D model evaluation 分离为 fixed tasks、pairwise human preference 与 action-facing capability。
- **Evidence boundary:** 约1000 benchmark items、4500+ votes；不证明 rater/platform 无偏或覆盖 physical safety。新增治理成本是 rater identity、versioned prompt 与 action verifier。

### Memorization-Compression Cycles

- **Primary / date / score / owner:** `2505.08727`，v1 2025-05-13，23/30；`TRAIN-PRETRAINING`。
- **Mechanism:** entropy constraint、information bottleneck、gradient alignment 与 GAPT switch 将 memorization/compression 作为 training dynamics state，而非“sleep”类比。
- **Evidence boundary:** GPT-2/FineWeb-scale 小设置；不证明 LLM-scale 普适或产生 human-like consolidation。新增阈值与 phase-switch failure；标准 continual pretraining 仍是默认基线。

### Step1X-3D

- **Primary / date / score / owner:** `2505.07747`，v1 2025-05-12，22/30；`MULTIMODAL-GENERATIVE-PARADIGMS`。
- **Mechanism:** geometry VAE-DiT/TSDF/residual quantization 与 cross-view texture diffusion/LoRA 形成 geometry→texture 两阶段 artifact contract。
- **Evidence boundary:** >5M collected/~2M curated 与110-person study；proprietary curation、跨阶段 error propagation 和未披露 production cost 限制外推。

### MathCoder

- **Primary / date / score / owner:** `2505.10557`，v1 2025-05-15，22/30；`TRAIN-DATA`，handoff Ch23/66。
- **Mechanism:** FigCodifier、ImgCode8.6M 与 MM-MathInstruct3M 把 figure→code→instruction lineage 用于 visual math data construction。
- **Evidence boundary:** 六类 metrics 与作者 benchmark 支持 synthetic data workflow，不证明 judge 独立、污染已排除或 compute 可泛化。artifact provenance 与 verifier coupling 是核心代价。

### Depth Any Prior

- **Primary / date / score / owner:** `2505.10565`，v1 2025-05-15，22/30；`MULTIMODAL-REPRESENTATION`。
- **Mechanism:** incomplete metric prior + complete relative MDE，通过 kNN scale/shift、distance weighting 与 conditioning 恢复 depth state。
- **Evidence boundary:** 七个 datasets 支持所列 depth contract，不证明 arbitrary-domain calibration 或安全控制闭环。单一 relative-depth model 在无 metric prior 时仍适用。

### RAG Hyperparameter Sensitivity

- **Primary / date / score / owner:** `2505.08445`，v1 2025-05-13，21/30；`AGENT-RAG`。
- **Mechanism:** 分离 Chroma/FAISS、chunk、rerank、temperature 等 control knobs，显示 retrieval 与 generation parameter 不是一个统一 owner。
- **Evidence boundary:** 13%/5×结论只属于作者设置；未覆盖 freshness、security、production concurrency/SLO。它是 sensitivity case，不是通用最优配置。

### Behind the Scenes of Maya

- **Primary / date / score / owner:** `2505.08910`，v1 2025-05-13，20/30；`TRAIN-DATA`。
- **Mechanism:** LLaVA-like multilingual data/recipe 的受限实现证据，展示 language coverage 与 modality tuning 的耦合。
- **Evidence boundary:** corpus/model较窄，不能形成新的通用 architecture 结论；只在 threshold 保留，作为 data recipe case。

### HealthBench

- **Primary / date / score / owner:** OpenAI official 2025-05-12 + `2505.08775` 2025-05-13，26/30；`PLATFORM-EVALUATION-SYSTEM`。
- **Mechanism:** 5000 conversations、262 physicians/60 countries、48,562 criteria 与 GPT-4.1 grader，把 scenario、rubric、grader 与 canary/version 分开管理。
- **Evidence boundary:** Consensus/Hard 与 physician meta-eval 支持 benchmark contract，不证明 clinical safety、autonomy 或 grader 即 ground truth。rubric drift、domain coverage 与 grader correlation 是新 failure modes。

### OMol25

- **Primary / date / score / owner:** `2505.08762`，v1 2025-05-13，25/30；`TRAIN-DATA`。
- **Mechanism:** ORCA 6.0.1、ωB97M-V/def2-TZVPD pipeline 生成 >100M calculations/~83M systems，data identity必须绑定 method/basis/geometry/version。
- **Evidence boundary:** later 140M count 不倒写事件时版本；<=350 atoms、约6B core-hours与 chemistry coverage/license bias 限制外推。证明数据系统规模，不证明 universal molecular accuracy。

### UMA

- **Primary / date / score / owner:** Meta official 2025-05-14；26/30；`MODEL-MOE`，handoff `TRAIN-DATA`。
- **Mechanism:** 约1.4B total/~50M active Mixture Linear Experts/equivariant GNN，在约500M 3D structures/>30B atoms上学习 conditional capacity。
- **Evidence boundary:** later `2506.23971` 是后续 node；官方事件证明 workload-specific sparse atomic model，不证明 universal chemistry 或所有 hardware efficiency。router specialization 与 data imbalance 是代价。

### NVIDIA NVLink Fusion

- **Primary / date / score / owner:** NVIDIA official 2025-05-18，23/30；`INFER-TENSORRT-LLM` execution/hardware co-design owner。
- **Mechanism:** custom XPU/CPU 通过 NVLink/NVLink-C2C/switch ecosystem 与 NVIDIA GPU 形成 scale-up domain，并与 Spectrum-X scale-out 分层。
- **Evidence boundary:** 无可复现实验、完整 coherency/ordering、topology control、failure recovery、fairness、power 或 SLO；只保留 `Version Fact / Mechanism Partially Disclosed`，不得推断统一 memory semantics。

### Time-R1

- **Primary / date / score / owner:** `2505.13508`，v1 2025-05-16，24/30；`TRAIN-GRPO`，从W21回拨。
- **Mechanism:** comprehension→prediction→inference curriculum，以 accuracy/format/length/repetition rewards 训练 temporal reasoning policy。
- **Evidence boundary:** Qwen2.5-3B、TimeBench >200K NYT items/10 years；不证明 scale/external distribution 或 disclosed compute 下普适。reward shortcut 与 temporal contamination 是风险。

### Orthogonal Residual Updates

- **Primary / date / score / owner:** `2505.11881`，v1 2025-05-17，25/30；`MODEL-TRANSFORMER-LAYER`，从W21回拨。
- **Mechanism:** `f_perp = f - <x,f>/(||x||²+eps)x` 将 residual update 与 current state 局部正交，并使用 early-orthogonal/later-linear switch。
- **Evaluation boundary:** ViT/ResNet、CIFAR/Tiny/ImageNet、batch1024/4096、300 epochs与显式 overhead；没有 LLM evidence。额外 projection cost 与 stage switch 是代价，标准 residual 在大规模 sequence model 中仍是默认。

### Synthetic Data RL

- **Primary / date / score / owner:** `2505.17063`，v1 2025-05-18，25/30；`TRAIN-GRPO`，handoff `TRAIN-DATA`，从W21回拨。
- **Mechanism:** task+retrieved documents → QA → pattern/difficulty estimate → adaptive generation → pass-rate filter → GRPO，生成器、retriever、verifier 与 policy 各自拥有不同 state。
- **Evaluation boundary:** Qwen2.5-7B、GSM/MATH/GPQA/MedQA/LogiQA/CQA/CFA、5×A100/约110h average；不证明 multimodal/multi-turn/14B/production。verifier bias、curriculum feedback loop 与 synthetic collapse 是新 failure modes。

### BARREL — Boundary-Aware Reasoning for Factual and Reliable LRMs

- **Candidate / Week / Score:** BARREL / 2025-W20 / 23/30（`4/3/4/4/4/4`）。
- **Source Family ID / Source Type:** `ARXIV-2505.13529-BARREL`；arXiv research paper，事件版本为v1。
- **Event Date / Revision History:** v1 first-public 2025-05-18；v2 2026-02-25属于同一family的后续修订，不能把新增baseline、模型或文字修正倒写成W20证据。
- **Direct / Related Primary Sources:** `https://arxiv.org/pdf/2505.13529v1`为本次机制与实验结论的唯一事件版本正文；当前arXiv metadata只用于确认revision history。
- **Access and Full-read Coverage:** Verified。已阅读metadata、Introduction/Related Work、knowledge labeling、evidence-grounded trajectory construction、SFT、GRPO reward、TriviaQA/SciQ/NQ-Open evaluation、baselines、主要表格、limitations与appendices；未把v2扩展实验回投v1。
- **Original Problem / Previous Design:** 在answer-maximization benchmark中总是给出答案、继续延长reasoning曾是合理策略；但当题目超出模型知识边界时，它会把候选猜测写成确定结论，long reasoning还可能放大second-thought与unsupported answer。
- **Changed Constraint / Principle:** 系统目标从“尽量答对”变为“在已知问题上答对、在未知问题上可靠拒答”。这要求把answer correctness与abstention policy分开评估，不能把token probability直接当成知识边界。
- **Mechanism / State Ownership:** 对每个问题运行`K`个prompt、每个prompt采样`L`次；任一采样命中gold则标作known，否则标作unknown。known样本构造证据锚定、比较候选并确认答案的轨迹；unknown样本构造探索后明确承认不确定的轨迹。SFT学习两类行为，GRPO再用规则reward区分正确回答、谨慎拒答与错误回答。dataset builder拥有known/unknown标签与轨迹；policy只生成reasoning/answer；rule verifier拥有reward，不能被模型自报confidence替代。
- **Control / Data Flow and Implementation:** question → repeated sampled answers → gold-match labeling → class-conditional reasoning-trace synthesis → SFT checkpoint → group rollout → rule reward → GRPO update → answer/refusal。该流程把知识边界变成training-time derived label，而不是模型内部可校准的epistemic state。
- **Evaluation Contract:** v1在TriviaQA、SciQ、NQ-Open各取1000题，共3000题；使用DeepSeek-R1-Distill-Llama-8B与Qwen-7B，比较ICL、ICL-IDK与Distill等baseline。硬件、训练precision、完整batch/concurrency与production SLO为`Not Disclosed`。
- **Baselines / Ablations / Sensitivity / Overhead:** 论文比较always-answer、prompted abstention与训练方案，并分析reliability/accuracy；但没有充分覆盖`K×L`误标敏感性、跨域calibration、长期distribution shift、独立复现或production latency。重复采样、轨迹生成与GRPO引入显著额外训练/teacher/verifier成本。
- **What the Evidence Proves:** 在该模型、三组QA数据与作者harness下，显式训练“正确回答或谨慎拒答”可改善accuracy–reliability取舍；它支持把abstention作为受治理的output policy。
- **What It Does Not Prove / Dispute:** 它不证明“没有一次采样答对”就等于模型不知道，也不提供可直接解释为真实概率的calibrated confidence。v1 abstract给出的61.48与主表61.58存在数值不一致；reward公式的OCR/符号顺序与“错误应比拒答受更重惩罚”的文字意图也不够一致，因此不采用精确headline或不经核验的reward ordering。
- **Trade-offs / Failure Modes:** 收益是减少高风险瞎猜；代价是false abstention、sampling miss导致unknown误标、偶然命中导致known误标、teacher/evaluator bias、reward gaming与coverage下降。对高覆盖、低风险、答案可即时验证的known workload，直接回答仍可能更合适。
- **Evolution / Owner / Adjacent Chapters:** `Direct Evolution`：always answer → confidence/prompt abstention → evidence-grounded boundary training → rule-constrained preference/RL。canonical owner为`TRAIN-GRPO`，handoff到`PLATFORM-EVALUATION-SYSTEM`与RAG/evidence章节；已核对Ch31～33与Ch66的reward/evaluation边界。
- **Integration Decision / Open Questions:** `Books Frozen — Historical Gate Closed`。待年度Gate后判断是否只作为Ch33受限训练案例；仍需独立校准实验回答derived known/unknown label如何映射到可部署的coverage、risk与human escalation policy。

## Evidence Level

- 官方 Blog / Release 只证明公开事实；未公开实现保持未知。
- arXiv v1 默认 Status: Experimental；作者实验不等于独立复现。
- 跨来源连接是本项目推断，以 Evolution Relationship 标记。

## Review Pending and Low-score Closure Ledger

- Ordinary `Review Pending = 0`。WorldPM已通过v1/v2全文与official repository闭合，不再请求外部材料。
- MPS-Prover、GIE-Bench、VCRBench及新增14项低分候选全部完成来源、first-public date、六维评分与拒绝边界核验；它们作为窄域应用、增量benchmark、taxonomy或scientific explanation保留在Weekly，不进入长期机制候选。
- SageAttention3不是blocked：正文、方法与实验可审计；只有event-time code availability与official repository release timeline冲突，状态为`Disputed — Artifact Date`。

Candidate Evidence Gate：`Passed`。81个owner中64/64个20+候选均有event-version Full Source Review，17/17低分完成identity/date/score/rejection闭合，Pending 0、Blocked 0。SageAttention3的artifact-date冲突与BARREL的v1数字/reward-order冲突均保留为显式`Disputed`字段，不把可读机制整体撤回。年度Archive/Discovery Gate与Historical Books Gate保持关闭。

## Cross-Week Deduplication

- Qwen3 technical report（2505.09388）与MiMo report（2505.07608）是W18 family的revision evidence，不重复评分。
- Seed1.5-VL、Skywork-VL Reward、AttentionInfluence、INTELLECT-2、DynamicRAG、UMoE、UniVLA、Unilogit、REFINE-AF、InstanceGen和Toxicity in LLaVA按v1日期回拨W19。
- SweRank（2505.07849）v1首发于2025-05-07，canonical owner回拨W19；W20不重复计分。
- SageAttention3、Time-R1、Orthogonal Residual Updates、Synthetic Data RL与BARREL按v1 2025-05-16～18从W21回拨W20；W21不重复评分。
- Transformers 4.52.0/4.52.1 forward至W21；NVIDIA NVLink Fusion的05-18 official event归W20并作为部分披露的version/design fact评分。
- MetaSPO/System Prompt Optimization aliases collapse为一个family；ETT别名同样只保留一个owner row。

## Knowledge Tree Position

- Owner覆盖Part II～VII：Model Scaling/Long Context，Multimodal Representation/Generation/World/Embodied，Training Data/Pretraining/GRPO/Distributed，Inference Execution，Platform Serving/Evaluation/Security，以及Agent Prompt/RAG/Tool/Planning/Reflection/Workflow/Multi-Agent/Platform。
- 章节映射只表示审计owner；Historical Books Gate关闭，不表示这些family已写入Books。

## Recommended Action

- 保持SageAttention3 artifact-date dispute，不把2025-09-27 repository release倒写成W20 event-time artifact。
- BARREL已按事件版本回拨并完成六维评分、全文packet与年度账本；后续只在出现新的primary evidence时重新开启本周Candidate Gate。

## Event-Date Daily Decision

历史回填不创建 Daily；事件与证据边界直接保留在本 Weekly。

## Books Integration Decision

`Books Frozen — Historical Gate Closed`。旧“Books Gate已完成”声明已撤销。本轮只恢复Weekly证据，不修改Books；64个strict packet的disposition均为provisional。


## Ignored Noise

- 忽略旧内容重发、二手转述、缺条件 benchmark 与纯可用性更新。
- discovery 排名和引用量不替代 novelty、reliability 或 longevity。

## Repository Changes

- 将44项lower-bound重建为81个已闭合score rows；BARREL作为第五个W21→W20 spillback完成评分、全文证据与账本写回。
- 本轮不修改Books、ROADMAP或DECISIONS。

## Open Questions

- SageAttention3 paper所称event-time code availability是否存在可验证的May 2025 tag/commit，还是只能保留September repository release？
- cross-index与固定组织历史导出若恢复，是否会增加05-12～05-18 owner；新增证据必须显式重新开启周Gate。

## Sources

- AlphaEvolve — https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/（First Public: 2025-05-14；Accessed: 2026-07-31）
- AlphaEvolve white paper — https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/AlphaEvolve.pdf（First Public: 2025-05-14；Accessed: 2026-07-31）
- Sufficient Context paper — https://arxiv.org/abs/2411.06037（First Public: 2024-11-09；v3: 2025-04-23；Accessed: 2026-07-31）
- Sufficient Context Google Research follow-up — https://research.google/blog/deeper-insights-into-retrieval-augmented-generation-the-role-of-sufficient-context/（Published: 2025-05-14；Accessed: 2026-07-31）
- DeepSeek-V3 Hardware Co-design — https://arxiv.org/abs/2505.09343（v1: 2025-05-14；Accessed: 2026-08-22）
- BLIP3-o — https://arxiv.org/abs/2505.09568（v1: 2025-05-14；Accessed: 2026-08-22）
- OpenAI Codex cloud preview — https://openai.com/index/introducing-codex/（First Public: 2025-05-16；Accessed: 2026-08-22）
- Parallel Scaling Law / ParScale — https://arxiv.org/abs/2505.10475（v1: 2025-05-15；Accessed: 2026-08-22）
- MiniMax-Speech — https://arxiv.org/abs/2505.07916（v1: 2025-05-12；Accessed: 2026-08-22）
- MLE-Dojo — https://arxiv.org/abs/2505.07782（v1: 2025-05-12；Accessed: 2026-08-22）
- OpenThinkIMG — https://arxiv.org/abs/2505.08617（v1: 2025-05-13；Accessed: 2026-08-22）
- EnerVerse-AC — https://arxiv.org/abs/2505.09723（v1: 2025-05-14；Accessed: 2026-08-22）
- GuardReasoner-VL — https://arxiv.org/abs/2505.11049（v1: 2025-05-16；Accessed: 2026-08-22）
- Visual Planning — https://arxiv.org/abs/2505.11409（v1: 2025-05-16；Accessed: 2026-08-22）
- MMLongBench — https://arxiv.org/abs/2505.10610（v1: 2025-05-15；Accessed: 2026-08-22）
- KServe v0.15.1 — https://github.com/kserve/kserve/releases/tag/v0.15.1（First Public: 2025-05-15；Accessed: 2026-08-22）
- EWMBench — https://arxiv.org/abs/2505.09694（v1: 2025-05-14；Accessed: 2026-08-22）
- Group Think — https://arxiv.org/abs/2505.11107（v1: 2025-05-16；Accessed: 2026-08-22）
- MuToR — https://arxiv.org/abs/2505.10518（v1: 2025-05-15；Accessed: 2026-08-22）
- IKEA adaptive search — https://arxiv.org/abs/2505.07596（v1: 2025-05-12；Accessed: 2026-08-22）
- Learning from Peers — https://arxiv.org/abs/2505.07787（v1: 2025-05-12；Accessed: 2026-08-22）
- DanceGRPO — https://arxiv.org/abs/2505.07818（v1: 2025-05-12；Accessed: 2026-08-22）
- Continual-pretraining Learning Dynamics — https://arxiv.org/abs/2505.07796（v1: 2025-05-12；Accessed: 2026-08-22）
- Overflow Prevention for Recurrent Long Context — https://arxiv.org/html/2505.07793（v1: 2025-05-12；Accessed: 2026-08-22）
- ARC Text-to-Audio — https://arxiv.org/html/2505.08175（v1: 2025-05-13；Accessed: 2026-08-22）
- AM-Thinking-v1 — https://arxiv.org/html/2505.08311（v1: 2025-05-13；Accessed: 2026-08-22）
- Aya Vision technical paper — https://arxiv.org/html/2505.08751（v1: 2025-05-13；Accessed: 2026-08-22）
- MulDimIF — https://arxiv.org/html/2505.07591（v1: 2025-05-12；Accessed: 2026-08-22）
- NavDP — https://arxiv.org/html/2505.08712（v1: 2025-05-13；Accessed: 2026-08-22）
- TRAIL — https://arxiv.org/html/2505.08638（v1: 2025-05-13；Accessed: 2026-08-22）
- Tests as Prompt / WebApp1K — https://arxiv.org/html/2505.09027（v1: 2025-05-13；Accessed: 2026-08-22）
- System Prompt Optimization with Meta-Learning — https://arxiv.org/html/2505.09666（v1: 2025-05-14；Accessed: 2026-08-22）
- CoT Encyclopedia — https://arxiv.org/html/2505.10185（v1: 2025-05-15；Accessed: 2026-08-22）
- J1 Judge RL — https://arxiv.org/html/2505.10320（v1: 2025-05-15；Accessed: 2026-08-22）
- WavReward — https://arxiv.org/html/2505.09558（v1: 2025-05-14；Accessed: 2026-08-22）
- Omni-R1 Audio — https://arxiv.org/html/2505.09439（v1: 2025-05-14；Accessed: 2026-08-22）
- Beyond “Aha!” — https://arxiv.org/html/2505.10554（v1: 2025-05-15；Accessed: 2026-08-22）
- End-to-End Vision Tokenizer Tuning — https://arxiv.org/html/2505.10562（v1: 2025-05-15；Accessed: 2026-08-22）
- SuperCoder — https://arxiv.org/html/2505.11480（v1: 2025-05-16；Accessed: 2026-08-22）
- Follow the Path / fs1 — https://arxiv.org/html/2505.11140（v1: 2025-05-16；Accessed: 2026-08-22）
- MatTools — https://arxiv.org/html/2505.10852（v1: 2025-05-16；Accessed: 2026-08-22）
- Symbiotic Watermarking — https://arxiv.org/html/2505.09924（v1: 2025-05-15；Accessed: 2026-08-22）
- WorldPM — https://arxiv.org/abs/2505.10527；https://github.com/QwenLM/WorldPM（v1: 2025-05-15；Accessed: 2026-08-24）
- SageAttention3 — https://arxiv.org/abs/2505.11594；https://github.com/thu-ml/SageAttention（v1: 2025-05-16；Accessed: 2026-08-24）
- UCGM — https://arxiv.org/abs/2505.07447（v1: 2025-05-12；Accessed: 2026-08-24）
- H3DP — https://arxiv.org/abs/2505.07819（v1: 2025-05-12；Accessed: 2026-08-24）
- R2R2R — https://arxiv.org/abs/2505.09601（v1: 2025-05-14；Accessed: 2026-08-24）
- TokenAdapt — https://arxiv.org/abs/2505.09738（v1: 2025-05-14；Accessed: 2026-08-24）
- Continuous VAR — https://arxiv.org/abs/2505.07812（v1: 2025-05-12；Accessed: 2026-08-24）
- Deep Fusion — https://arxiv.org/abs/2505.10046（v1: 2025-05-15；Accessed: 2026-08-24）
- UniSkill — https://arxiv.org/abs/2505.08787（v1: 2025-05-13；Accessed: 2026-08-24）
- PointArena — https://arxiv.org/abs/2505.09990（v1: 2025-05-15；Accessed: 2026-08-24）
- Memorization-Compression Cycles — https://arxiv.org/abs/2505.08727（v1: 2025-05-13；Accessed: 2026-08-24）
- Step1X-3D — https://arxiv.org/abs/2505.07747（v1: 2025-05-12；Accessed: 2026-08-24）
- MathCoder — https://arxiv.org/abs/2505.10557（v1: 2025-05-15；Accessed: 2026-08-24）
- Depth Any Prior — https://arxiv.org/abs/2505.10565（v1: 2025-05-15；Accessed: 2026-08-24）
- RAG hyperparameter sensitivity — https://arxiv.org/abs/2505.08445（v1: 2025-05-13；Accessed: 2026-08-24）
- Behind the Scenes of Maya — https://arxiv.org/abs/2505.08910（v1: 2025-05-13；Accessed: 2026-08-24）
- HealthBench — https://openai.com/index/healthbench/；https://arxiv.org/abs/2505.08775（Event: 2025-05-12；Accessed: 2026-08-24）
- OMol25 — https://arxiv.org/abs/2505.08762（v1: 2025-05-13；Accessed: 2026-08-24）
- UMA — https://ai.meta.com/blog/meta-fair-science-new-open-source-releases/（Event: 2025-05-14；Accessed: 2026-08-24）
- NVIDIA NVLink Fusion — https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Unveils-NVLink-Fusion-for-Industry-to-Build-Semi-Custom-AI-Infrastructure-With-NVIDIA-Partner-Ecosystem/default.aspx（Event: 2025-05-18；Accessed: 2026-08-24）
- Time-R1 — https://arxiv.org/abs/2505.13508（v1: 2025-05-16；Accessed: 2026-08-24）
- Orthogonal Residual Updates — https://arxiv.org/abs/2505.11881（v1: 2025-05-17；Accessed: 2026-08-24）
- Synthetic Data RL — https://arxiv.org/abs/2505.17063（v1: 2025-05-18；Accessed: 2026-08-24）
- BARREL — https://arxiv.org/pdf/2505.13529v1（v1: 2025-05-18；Accessed: 2026-08-24）
- Low-score identities — https://arxiv.org/abs/2505.09608；https://arxiv.org/abs/2505.10558；https://arxiv.org/abs/2505.10468；https://arxiv.org/abs/2505.08581；https://arxiv.org/abs/2505.10566；https://arxiv.org/abs/2505.10167；https://arxiv.org/abs/2505.09926；https://arxiv.org/abs/2505.09265；https://arxiv.org/abs/2505.09264；https://arxiv.org/abs/2505.09263；https://arxiv.org/abs/2505.08665；https://arxiv.org/abs/2505.07416；https://arxiv.org/abs/2505.08084（Accessed: 2026-08-24）
