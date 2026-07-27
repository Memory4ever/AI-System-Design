# AI Research Weekly — 2025-W20

> Coverage Window: 2025-05-12～2025-05-18
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 2 项长期证据：AlphaEvolve、Sufficient Context for RAG。记录聚焦约束、机制、证据边界与演进关系，不收集一般新闻。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 归档；搜索收录日与后续修订不替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery 与去重；论文机制回到正文。Crossref 仅做 Weekly metadata 交叉检查。
- 历史回填不补造 Daily；Accessed 统一为 2026-07-31。
- benchmark 缺少模型、硬件、长度、batch/concurrency、precision/quantization 与 SLO 时不做通用结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：AlphaEvolve（2025-05-14）。
- 保留：Sufficient Context for RAG 的 Google Research follow-up（2025-05-14）；论文 v1 实际首次公开于 2024-11-09。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| AlphaEvolve | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；优先 refine Workflow/Evaluation |
| Sufficient Context for RAG | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；补全 RAG 的 abstention/control loop |

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

## Evidence Level

- 官方 Blog / Release 只证明公开事实；未公开实现保持未知。
- arXiv v1 默认 Status: Experimental；作者实验不等于独立复现。
- 跨来源连接是本项目推断，以 Evolution Relationship 标记。

## Cross-Week Deduplication

- 同一技术后续 revision 与工程集成回链首次公开周。
- 新版本不覆盖旧方案；年度索引记录 old constraint → new mechanism → new failure mode。

## Knowledge Tree Position

- AlphaEvolve → 第 62、74～78、80 章（Direct Evolution）
- Sufficient Context for RAG → 第 62、71、72、76 章（Direct Evolution）

## Recommended Action

- AlphaEvolve：Must Read；优先 refine Workflow/Evaluation
- Sufficient Context for RAG：Must Read；补全 RAG 的 abstention/control loop

## Event-Date Daily Decision

历史回填不创建 Daily；事件与证据边界直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略旧内容重发、二手转述、缺条件 benchmark 与纯可用性更新。
- discovery 排名和引用量不替代 novelty、reliability 或 longevity。

## Repository Changes

- 新增 papers/2025/weekly/2025-W20/README.md。
- 更新 books/part-06-agent/72-rag.md。
- 更新 books/part-06-agent/77-workflow.md。

## Open Questions

- evaluator gaming、search-level overfitting 与现实部署复核仍是 evaluator-driven search 的核心风险。
- sufficiency classifier 的跨域 calibration、额外 latency 与错误 abstention 仍需线上证据。

## Sources

- AlphaEvolve — https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/（First Public: 2025-05-14；Accessed: 2026-07-31）
- AlphaEvolve white paper — https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/AlphaEvolve.pdf（First Public: 2025-05-14；Accessed: 2026-07-31）
- Sufficient Context paper — https://arxiv.org/abs/2411.06037（First Public: 2024-11-09；v3: 2025-04-23；Accessed: 2026-07-31）
- Sufficient Context Google Research follow-up — https://research.google/blog/deeper-insights-into-retrieval-augmented-generation-the-role-of-sufficient-context/（Published: 2025-05-14；Accessed: 2026-07-31）
