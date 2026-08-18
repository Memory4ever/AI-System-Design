# AI Research Weekly — 2025-W27

> Coverage Window: 2025-06-30～2025-07-06
> Research Mode: Retrospective Primary-Source Backfill
> Re-audited: 2026-08-24
> Audit Status: Candidate Evidence Gate Conditional Pass — 36/37 Retained Source-complete; 1 Event-version Full-text Blocked
> Historical Books Gate: Closed

## Executive Summary

旧档案只保留GLM-4.1V-Thinking。本轮重新核对相邻周后，把W28中first-public date实际为2025-07-06的RAT、GradOT、S³与DP-Fusion回拨到W27，形成41个scored owner：19项25～30分、18项20～24分、4项低分。36/37 retained families完成source-complete review；MARVIS的identity、日期、current repository与后续revision可核，但事件时`2507.01544v1`全文仍不可取得，按`Unverified / Blocked`处理而不是普通Pending。3项官方RFC/roadmap已完成事件时issue阅读，最终限定为`Weekly Only — Design Intent / Mechanism Not Shipped`。Review Pending为0，4/4低分闭合，Disputed为0。Historical Books Gate保持关闭。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release或arXiv v1归档；later revision只作同family核验，不倒灌event-time facts。
- arXiv 06-30、07-01～04与Hugging Face已重放；07-05无新arXiv batch。相邻周审计确认07-06存在4项此前误归W28的v1 owner，已回拨本周。fixed-organization清单完成事件页/官方release/RFC的best-effort replay；Google Scholar/OpenAlex/DBLP/Crossref无法取得可证明穷尽性的immutable export，因此Archive/Discovery Recall保持Open，不能宣称年度无遗漏。
- 历史回填不创建Daily；所有性能数字必须绑定model、hardware、precision、length、batch/concurrency与SLO，未披露写`Not Disclosed`。
- vLLM `v0.9.2` official release为2025-07-07，归W28；W26 spillback不在W27重复评分。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI与Hugging Face Blog。

- official/model owner包括GLM-4.1V-Thinking与Kwai Keye-VL report；只有公开行为、没有内部机制的内容不反推training/runtime。

## 2. 论文与学术来源

按arXiv → Google Scholar → OpenAlex → DBLP扫描，回到v1正文核验；Crossref只做metadata交叉检查。

- 当前41个owner覆盖multimodal representation/generation、reasoning post-training、evaluation、Agent workflow、privacy与distributed training；MARVIS仍待事件时v1全文。3个工程proposal已完成event-time issue审计，后续code/release只作为同family演进节点，不再记普通Pending。

## 3. AI Infra 与工程项目

按PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime与OpenXLA扫描。

- 本轮未把W28的vLLM `v0.9.2`提前计入；vLLM/SGLang本周RFC与roadmap均回到官方issue核验。其他固定工程项目未发现可建立本周owner identity的新release/RFC；这是一轮best-effort negative scan，不等于immutable archive export。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| SPIRAL | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete |
| Calligrapher | 3 | 2 | 2 | 5 | 3 | 3 | 18/30 | Low-score closure |
| VMoBA | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| Thinking with Images for Multimodal Reasoning | 3 | 3 | 3 | 4 | 4 | 4 | 21/30 | Full Source Review Complete — Survey Evidence |
| JAM-Flow | 4 | 3 | 3 | 5 | 4 | 4 | 23/30 | Full Source Review Complete — Experimental |
| μ²Tokenizer | 4 | 3 | 3 | 5 | 4 | 4 | 23/30 | Full Source Review Complete — Experimental |
| GLM-4.1V-9B-Thinking | 4 | 3 | 3 | 4 | 4 | 3 | 21/30 | Full Source Review Complete — Experimental Model Case |
| Does Math Reasoning Improve General LLM Capabilities? | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| SciArena | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| ARIG | 4 | 3 | 4 | 5 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental |
| Thinking Beyond Tokens | 2 | 2 | 2 | 4 | 3 | 3 | 16/30 | Low-score closure |
| Mixture of Reasonings | 3 | 3 | 3 | 4 | 4 | 3 | 20/30 | Full Source Review Complete — Experimental |
| FreNBRDF | 3 | 2 | 2 | 5 | 2 | 3 | 17/30 | Low-score closure |
| ZeCO | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete |
| Kwai Keye-VL Technical Report | 4 | 4 | 3 | 5 | 4 | 3 | 23/30 | Full Source Review Complete |
| LongAnimation | 4 | 3 | 3 | 5 | 4 | 4 | 23/30 | Full Source Review Complete — Experimental |
| VLA Models: An Action Tokenization Perspective | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Full Source Review Complete — Survey Evidence |
| Locality-aware Parallel Decoding | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Full Source Review Complete |
| MARVIS | 3 | 3 | 3 | 4 | 4 | 3 | 20/30 | Unverified / Blocked — Event-version Full Text |
| Depth Anything at Any Condition | 4 | 3 | 4 | 5 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental |
| FreeMorph | 3 | 2 | 3 | 5 | 3 | 3 | 19/30 | Low-score closure |
| IntFold | 4 | 3 | 3 | 4 | 3 | 4 | 21/30 | Full Source Review Complete — Experimental |
| Skywork-Reward-V2 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| Energy-Based Transformers | 5 | 5 | 4 | 5 | 5 | 5 | 29/30 | Full Source Review Complete — Experimental |
| AsyncFlow | 5 | 5 | 5 | 5 | 5 | 5 | 30/30 | Full Source Review Complete |
| WebSailor | 5 | 5 | 5 | 5 | 5 | 5 | 30/30 | Full Source Review Complete |
| Decoupled Planning and Execution | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| Fast and Simplex | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| Can LLMs Identify Critical Limitations? | 3 | 3 | 4 | 5 | 5 | 4 | 24/30 | Full Source Review Complete |
| Self-Correction Bench | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete |
| Answer Matching Outperforms Multiple Choice | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Full Source Review Complete |
| LangScene-X | 4 | 3 | 3 | 5 | 4 | 3 | 22/30 | Full Source Review Complete — Experimental |
| Heeding the Inner Voice | 4 | 3 | 4 | 5 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental |
| Bourbaki | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete |
| vLLM CompilationConfig / CLI -O RFC #20283 | 3 | 4 | 4 | 5 | 5 | 4 | 25/30 | Source Review Complete — Design Intent / Not Shipped |
| vLLM Q3 2025 Roadmap #20336 | 2 | 4 | 4 | 5 | 5 | 3 | 23/30 | Source Review Complete — Official Plan / Not Shipped |
| SGLang Q3 2025 Development Roadmap #7736 | 2 | 4 | 4 | 5 | 5 | 3 | 23/30 | Source Review Complete — Official Plan / Not Shipped |
| RAT / Recurrent Attention Transformer | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| GradOT | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| Controllable diffusion LM / S³ | 4 | 3 | 3 | 5 | 4 | 3 | 22/30 | Full Source Review Complete — Experimental |
| DP-Fusion | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |

账目：41 scored owners = 19 high + 18 medium + 4 low；37项达到20+，其中36项source-complete（含3项Version/Plan Fact）、1项event-version Full-text Blocked；Review Pending 0；4项低分闭合；Disputed 0。

### Deep Analysis 1 — GLM-4.1V-Thinking

- First Public: 2025-07-01
- Status: Official open model / technical report
- Primary Source: https://github.com/zai-org/GLM-V
- Evolution Relationship: Layering / Dependency

#### Why

多模态 reasoning 的系统成本来自视觉编码、长上下文、RL rollout 和工具环境的共同作用。

#### Principle and Mechanism

项目公开模型、报告与 reasoning/tool-use 支持；benchmark 仍是作者评测。

#### Trade-off and Evidence Boundary

开放权重改善复现与部署，但视觉 token、KV state 和多轮环境会使 activated parameter 不能代表端到端成本。

#### Connection and Evolution

知识树位置：第 23～25、29、62、74 章。Worth Watching；等待与后续 GLM-4.5 形成稳定链。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

## Full Source Review

### SPIRAL

- **Primary / coverage / owner:** `2506.24119` v1 2025-06-30（current v3 2026-03-02）及official code；27/30；`TRAIN-GRPO`，handoff `AGENT-MULTI-AGENT`。全文覆盖method/equations、actor-learner、evaluation/ablation/statistics、appendices与limitations。
- **Problem / mechanism / ownership:** curated RLVR和fixed opponents易验证，但static curriculum会过拟合。SPIRAL让一个shared policy在terminal-reward zero-sum games中扮演双方，以per-game/per-role EMA baseline形成RAE advantage；environment拥有transition/reward，actors拥有trajectory，learner拥有role-conditioned baseline，checkpoint必须绑定opponent/policy identity。
- **Evaluation boundary:** Qwen3-4B/8B、Octothinker/Llama variants，8个reasoning benchmarks与OOD games，8×H100约25h/run；precision/global batch/concurrency/SLO未披露。证据支持该setup产生transfer signal并避免observed thinking collapse，不证明self-play替代curated RLVR或扩展到open-world。
- **Trade-off / coexistence / disposition:** non-stationarity、collusion、game bias、reward hacking与version state；verifier清晰时fixed dataset仍有更强因果性。Books Frozen；future disposition倾向`No Change — Already Covered`。

### VMoBA

- **Primary / coverage / owner:** `2506.23858` v1-only 2025-06-30及official code；26/30；`MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `MODEL-SELF-ATTENTION`。全文覆盖method、implementation、tables/ablations、appendix pretraining与limitations。
- **Problem / mechanism / ownership:** long/high-resolution video DiT使full attention平方成本主导，而generic 1-D block破坏spatiotemporal structure。VMoBA以recurrent 1D→2D→3D partitions、head-level global scores与cumulative threshold选择可变blocks；attention layer拥有partition/score/threshold state。
- **Evaluation boundary:** Wan2.1-1.3B、Koala-36M、VBench，55K/56K train和33K/76K inference token cases；GPU、precision、batch/concurrency/SLO未披露。作者结果支持长序列效率，但13K可能更慢，training-free full selection还出现vibration。
- **Trade-off / coexistence / disposition:** threshold calibration、dynamic-shape kernel inefficiency、temporal vibration与metric mismatch；短/fixed-shape或strict similarity仍可full attention/local top-k。Books Frozen；future `Refine — Existing Argument`。

### Does Math Reasoning Improve General LLM Capabilities?

- **Primary / coverage / owner:** `2507.00432` v1 2025-07-01（v2 2025-10-20仅lineage）；26/30；`TRAIN-SFT`，handoff `TRAIN-GRPO`。全文覆盖controlled setup、representation/token analyses、cross-domain experiments、appendices与结论。
- **Problem / mechanism / ownership:** math榜单提升可能只是窄化适配。论文以同一Qwen3-14B base/math examples比较teacher-CoT SFT与ground-truth reward RL，再用跨域任务、PCA latent drift与token distribution诊断；base、data/trajectory、reward和evaluation harness分别拥有不同证据角色。
- **Evaluation boundary:** 受控branch及20+ open reasoning models支持SFT常伴一般能力下降而RL分支跨域更稳；不证明RL普遍优于SFT、PCA drift导致能力损失或开放模型横截面具有因果性。hardware/precision/length/batch/concurrency/SLO未披露。
- **Trade-off / coexistence / disposition:** SFT稳定却可能distributional overwrite；RL需verifier/rollout且有reward hacking/高方差。格式学习、cold start与不可验证任务仍适合SFT。Books Frozen；future `Refine — Existing Argument`。

### SciArena

- **Primary / coverage / owner:** `2507.01001` v1 2025-07-01（v2 2026-01-22不回灌）；26/30；`PLATFORM-EVALUATION-SYSTEM`。v1全文38页，覆盖platform pipeline、ranking、data QA、SciArena-Eval及appendices。
- **Problem / mechanism / ownership:** literature-grounded scientific tasks没有唯一可执行答案。平台以moderation→retrieval→blinded pair generation→researcher vote→Bradley–Terry/Elo+bootstrap构成evidence pipeline；index snapshot、model output、vote event、annotator cohort和derived score必须分开拥有。
- **Evaluation boundary:** v1截止2025-06-30为23 models、13,204 votes、102 trusted researchers；best cited automated judge与human pair agreement 65.1%。证明可形成可审计preference ledger与uncertainty ranking，不证明leaderboard是全局scientific ability或automated judge可替代人类。
- **Trade-off / coexistence / disposition:** cohort/index/presentation drift、pair exposure不均和judge bias；exact-match/programmatic verifier在有标准答案时仍优先。Books Frozen；future `Refine — Existing Argument`或章节级`No Change`。

### AsyncFlow

- **Primary / coverage / owner:** `2507.01663` v1-only 2025-07-02；30/30；`TRAIN-GRPO`，runtime handoff `TRAIN-DISTRIBUTED-TRAINING`。全文覆盖architecture、TransferQueue、producer-consumer async、weight transfer、resource planner、evaluation/ablation与limitations。
- **Problem / mechanism / ownership:** synchronous task-separated RL在phase不均和variable rollout下放大idle。TransferQueue分离metadata controller与2D payload storage，以atomic publish/global index串起rollout→reward→trainer→delayed weight activation；trajectory必须带policy lineage/staleness，planner、queue、trainer与weight transport各自拥有状态。
- **Evaluation boundary:** PyTorch2.5.1/CANN8.1/vLLM-Ascend、Qwen2.5-7B/32B、GRPO、32～1024 Ascend NPUs；作者mean 1.59×、max 2.03× throughput。证明该stack可减少idle，不证明sync/async最终收敛等价、GPU可迁移或one-step delay普遍安全。
- **Trade-off / coexistence / disposition:** backpressure、duplicate/lost consumption、metadata hotspot、stale-policy bias、activation race与partial failure；小集群、strict on-policy和可复现优先时barrier/colocation仍合理。Books Frozen；future `Refine — Existing Argument`。

### ZeCO

- **Primary / coverage / owner:** `2507.01004` v1 2025-07-01、v2 2025-07-02；29/30；`TRAIN-TENSOR-PARALLEL`，handoff `TRAIN-DISTRIBUTED-TRAINING`与`MODEL-LONG-CONTEXT`。全文覆盖GLA递归/块形式、LASP1/2、ZeCO/All-Scan算法与证明、forward/backward、实验和appendix。
- **Problem / mechanism / ownership:** linear attention降低长序列compute后，跨sequence-rank recurrent boundary state会让P2P串行或AllGather重复通信。ZeCO把state沿维度切段，用receive-scan-send只传下游所需初始state，并与local diagonal attention重叠；rank拥有local state，ordered collective拥有boundary dependency，runtime拥有segment/readiness。
- **Evaluation boundary:** 1B GLA、8～256×H100 80GB、每rank 8K～32K、总长至8M；作者报告collective/operator/model throughput增益。precision/global batch/network topology/contention/SLO未披露。不证明“zero overhead”、softmax attention可用、任意topology或convergence equivalence。
- **Trade-off / coexistence / disposition:** custom collective、segment tuning、stream ordering、partial-send/deadlock与reverse backward；小规模、成熟library/fault semantics优先或non-compatible state仍适合AllGather/P2P。Books Frozen；future `Refine — Existing Argument`。

### Energy-Based Transformers

- **Primary / coverage / owner:** `2507.02092` v1-only 2025-07-02；29/30；`MODEL-TRANSFORMER-LAYER`，handoff `MODEL-SAMPLING`与`MULTIMODAL-GENERATIVE-PARADIGMS`。全文覆盖energy objective/optimization、text/video/image experiments、scaling axes、thinking algorithms、failure cases、implementation和limitations。
- **Problem / mechanism / ownership:** one-pass next-token/frame prediction不能按candidate迭代修正。EBT让Transformer输出context+candidate的scalar energy，以candidate gradient descent或BoN minimum-energy selection消费更多inference compute；checkpoint拥有energy function，request/inner loop拥有mutable candidate与step/NFE budget，energy score不拥有truth。
- **Evaluation boundary:** ≤800M text models、SSV2 video与COCO image setup，含depth/width/data/batch/FLOPs、NFE/BoN/step ablations；hardware、precision、wall-clock、concurrency/SLO未披露。证明受限recipes中存在跨模态experimental branch，不证明energy是校准概率、foundation-scale趋势或equal-forward等于equal-cost。
- **Trade-off / coexistence / disposition:** gradient memory、inner-loop latency、stop calibration、local minima、energy miscalibration与DoS budget；低延迟/大batch/硬SLO或需external truth verifier时standard AR+verifier仍优先。`Emerging / Experimental`。

### WebSailor

- **Primary / coverage / owner:** `2507.02592` v1-only 2025-07-03及Qwen-Agent artifact；30/30；`AGENT-WORKFLOW`，handoff `AGENT-PLANNING`、`AGENT-TOOL-CALLING`与`PLATFORM-EVALUATION-SYSTEM`。全文覆盖SailorFog-QA、trajectory reconstruction、RFT、DUPO/RL、benchmarks、ablations、limitations与appendix。
- **Problem / mechanism / ownership:** open-web高不确定长轨迹任务缺复杂训练分布。pipeline从rare entity构图并obfuscate生成QA，过滤正确trajectory后重建compact reasoning，先RFT植入ReAct skeleton再以DUPO/RL探索；dataset builder、tool runtime、trajectory store、trainer、format validator和answer judge各有独立owner。
- **Evaluation boundary:** Qwen2.5 3B～72B、BrowseComp/GAIA/Xbench，search top10、最多30 tool calls、group8、trajectory<32K、RL仅50 steps；hardware/precision/concurrency/SLO未披露。证明作者harness中复杂合成+RFT+RL优于baselines，不证明super-human、LLM judge正确、动态web可复现或组件单独因果。
- **Trade-off / coexistence / disposition:** artifact shortcuts、teacher/reconstructor bias、latency/cost、stale evidence、looping与judge hacking；短/可枚举路径、严格权限或高质量demonstrations仍适合fixed workflow/RFT。Books Frozen；future `Refine — Existing Argument`。

### Skywork-Reward-V2

- **Primary / coverage / owner:** `2507.01352` v1 2025-07-02、v2 2025-07-03（v3 later）；26/30；`TRAIN-RLHF`，handoff `TRAIN-DPO`与`PLATFORM-EVALUATION-SYSTEM`。v1全文覆盖preference audit、two-stage curation、human/LLM protocols、BT RMs、seven-suite eval、ablations、limitations与training details。
- **Problem / mechanism / ownership:** 单一RewardBench饱和且public pairs narrow/noisy。pipeline从raw pool提取task/attributes/guideline，以human gold和LLM silver训BT RM，再按error/low-confidence+attribute retrieval做active curation，最终以consistency filtering扩到26M；raw provenance、human cohort、AI proposal、selector、dataset lineage各自有owner，RM confidence不是真值。
- **Evaluation boundary:** 8个0.6B～8B RMs、16K max tokens，final 64×H800、global batch10,240，七类RM suites及downstream/BoN。证明作者setup中curation quality有贡献且single-score会overfit；不证明26M代表总体human preference、confidence已校准或benchmark SOTA等于safe deployment。
- **Trade-off / coexistence / disposition:** human cost/cohort bias、shared AI bias、active-loop hard-example overfocus、filter/flip lineage；关键risk slices仍应human-only/executable labels。Books Frozen；future `Refine — Existing Argument`。

### Locality-aware Parallel Decoding

- **Primary / coverage / owner:** `2507.01957` v1 2025-07-02（v2 later）及official repo；27/30；`MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `MULTIMODAL-REPRESENTATION`与`INFER-KV-CACHE`。v1全文覆盖mask/order algorithm、ImageNet evaluation、editing、ablations、training appendix与schedule code。
- **Problem / mechanism / ownership:** flat-token raster AR每步只commit一patch而memory-bound。LPD把committed image-token context与position queries分离，同组queries可互相attention但不写KV；预计算2D-locality variable groups，sample后atomic commit。checkpoint拥有mask/query semantics，schedule是versioned artifact，KV只拥有committed tokens。
- **Evaluation boundary:** LlamaGen codebook、337M/752M/1.4B，ImageNet256/512；latency/throughput为single A100 BF16，batch1/64。作者报告256→20、1024→48 steps及≥3.4×；不证明text/video通用、same FID等于semantic lossless或fleet/SLO可外推。
- **Trade-off / coexistence / disposition:** 每step更多compute、special-mask/kernel complexity、correlated group error、early wrong commit与schedule/KV identity；raster AR在strict causal、small image或compatibility优先时仍合理。Books Frozen；future `Refine — Existing Argument`。

### GLM-4.1V-9B-Thinking

- **Candidate / Week / Score:** GLM-4.1V-9B-Thinking / 2025-W27 / 21/30。
- **Source Family ID:** `GLM-V-2507.01006`。
- **Source Type:** arXiv technical report、official model repository/weights。
- **First-public Date / Revision History:** arXiv v1 于 2025-07-01 公开；当前 HTML 已由后续 revision 合并 GLM-4.5V/4.6V，故本周判断只使用 v1 与 4.1V 明确归属的材料，不把后续模型能力倒灌为 4.1V 事实。
- **Direct Primary Sources:** arXiv:2507.01006 v1/PDF/HTML；`zai-org/GLM-V` 中 GLM-4.1V-9B-Thinking 的 model card、config 与使用说明。
- **Related Primary Sources:** GLM-4-9B-0414 base model、AIMv2 vision encoder；后续 GLM-4.5V 仅用于标注 revision/evolution。
- **Access and Verification Status:** Verified for paper-described mechanism and released artifacts；完整训练数据、reward model、RL code、cluster topology 与 production runtime Not Disclosed。
- **Full-read Coverage:** 已阅读 metadata/revision boundary、Introduction、architecture、pre-training data/recipe、SFT data/recipe、RL data/reward/RLCS/infra、42 项 evaluation setting、cross-domain ablation、limitations/conclusion，以及与 GUI、grounding、coding protocol 相关 appendix。
- **Original Problem:** 多模态模型若只在短答案或单领域任务上训练，难以把视觉感知、长链推理、GUI action、grounding 与长文档理解放进同一反馈学习过程。
- **Why the Previous Design Was Reasonable:** 大规模 image-text pretraining 加 SFT 能稳定建立视觉语义对齐；固定数据分布、短 CoT 与单域 RL 在任务窄、reward 稳定时更易控制。
- **Changed Constraint:** 多领域样本难度与模型能力不同且随训练变化；固定混合比例会让已学会样本继续消耗 rollout，过难样本又缺少有效 reward signal。
- **Mechanism:** 4.1V 采用 AIMv2-Huge vision encoder、MLP projector 与 GLM-4-9B-0414 decoder；SFT 只保留 long-CoT thinking data。RLCS 以各 domain/sample 的近期 reward success 估计难度，动态扩展可学习样本，并将 rule-based 与 model-based reward 按领域组合。
- **State Ownership:** data pipeline 拥有 domain/sample metadata；rollout/evaluator 拥有 response 与 reward；curriculum controller 拥有难度统计和 sampling distribution；trainer 只消费选中样本与 advantage，不能由 model 自己宣称任务已掌握。
- **Control Flow / Data Flow:** image/video/document → visual tokenization/projector → long-CoT SFT → multi-domain rollout → domain-specific verification/reward → curriculum statistic update → next sampling distribution → policy update。
- **Implementation Details:** image-text corpus 超过 10B pairs，使用 heuristic/CLIP threshold 与 recaptioning；video temporal downsampling 使用 3D convolution；RL sequence/load 在 data-parallel ranks 间平衡，并把 samples packing 到 32K，作者报告 repacking 约减半 forward/backward time。
- **Evaluation Setup:** 42 个公开 benchmark；推理由 vLLM/SGLang 执行，最大输出 8,192 tokens；单图上限约 6,144 visual tokens，视频约 48,000；不同 benchmark 使用各自 prompt/parser，另有 domain-combination ablation。
- **Baselines / Ablations / Sensitivity:** 与同尺寸 open/closed VLM 比较；报告 pretrain→SFT→RL stage 增益及 single-domain/mixed-domain RL 对比。没有公开 reward-model calibration、curriculum 阈值全量 sensitivity、独立复现或相同 harness 下的所有闭源 baseline。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 9B decoder、32K packing、visual/output token limits 披露；训练 GPU 型号/数量、precision、global batch、online concurrency 与 serving SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在作者 pipeline 与 42-benchmark harness 下，动态 curriculum 能在多个 domain 同时产生正向训练信号，且 RL 不只改善 final-answer STEM；它还展示多模态 RL 的 sampling controller 是系统组件，而非单一 loss 公式。
- **What It Does Not Prove:** 不证明 long CoT 总优于 short/no CoT，不证明 mixed-domain RL 对 grounding/GUI 都有效，也不证明榜单差异来自 RLCS 而非 data、base model、prompt 或 evaluator。
- **Limitations / Threats to Validity:** outcome reward 可能强化错误过程；model reward 可被 exploit；训练配置敏感；视觉 clutter、occlusion、复杂空间关系仍弱；混域实验未改善部分 grounding/GUI；当前 HTML 混入后续模型，必须维持版本隔离。
- **Trade-offs / New Failure Modes:** dynamic sampling 减少无效 rollout，却新增 curriculum state、跨 domain reward calibration、滞后统计与 feedback-loop bias；long CoT 增加 token cost、truncation 与 plausible-but-wrong reasoning。
- **Where the Previous Design Still Applies:** 感知任务简单、答案短、rule verifier 缺失或 reward 不可比较时，pretraining+SFT、固定采样或单域 RL 仍更可控；non-thinking mode 也仍适合 latency-sensitive workload。
- **Evolution Relationship:** `Direct Evolution`：multimodal pretraining/SFT → domain-specific reasoning RL → curriculum-controlled multi-domain RL；不是“RL 替代视觉 pretraining”。
- **ROADMAP Node:** canonical owner `MULTIMODAL-REPRESENTATION` / Current Ch23 / Legacy N/A；adjacent `MODEL-LONG-CONTEXT` Ch22、`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24；handoff `TRAIN-GRPO` Ch33与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已targeted阅读Ch22～24、Ch33与Ch66的owner边界；multimodal representation、curriculum/reward与evaluation harness各自保留独立状态所有权。
- **Existing Coverage:** Ch23已覆盖modality/representation identity，Ch33覆盖curriculum、staleness与reward边界，Ch66覆盖harness contract；本report仍是单一experimental model case。
- **Integration Decision:** `Weekly Only — Experimental Model Case`。
- **Changed Files or Rejection Reason:** 不改 Books；单一 VLM report 未形成超出现有 multimodal/training/evaluation contract 的稳定机制。
- **Open Questions:** v1 与后续 revision 的精确差异、RL cluster/precision/global batch、reward calibration、dynamic sampling sensitivity 与独立复现。

### HiRA / Decoupled Planning and Execution

- **Primary / date / owner:** `2507.02652` v1 2025-07-03及code artifact，25/30；`AGENT-PLANNING`，handoff `AGENT-TOOL-CALLING`、`AGENT-REFLECTION`、`AGENT-WORKFLOW`与`AGENT-MULTI-AGENT`。事件时v1 PDF已全文审计，2025-10 v2仅作后续revision。
- **Problem / mechanism / ownership:** monolithic search agent把战略分解、tool selection、execution和evidence synthesis混在同一chain。HiRA以Meta Planner→Adaptive Coordinator→domain executors三层分离；planner拥有global task graph与final synthesis，coordinator拥有routing、distilled handoff和memory/resource registry，executors拥有local tool trajectory，environment拥有search/code/multimodal outputs。
- **Evaluation boundary:** QwQ/Qwen2.5 family、128K context、最多10 subtasks、Bing top-10与restricted Python；GAIA subset、WebWalkerQA、HLE、SimpleQA由Qwen2.5-72B judge，并含transfer/memory/tool ablations。hardware、precision、batch、concurrency、cost/SLO未披露；结果不证明hierarchy普遍优于single-agent，也不证明judge independence或production recovery。
- **Trade-off / coexistence / disposition:** 专门化换来额外calls、routing latency、lossy distillation、stale memory、provenance corruption、partial failure和重复side effects。few-tool/low-latency任务仍适合monolithic ReAct。Books Frozen；future `Refine — Existing Argument`。

### Fast and Simplex / 2-Simplicial Attention

- **Primary / date / owner:** `2507.02754` v1-only 2025-07-03，27/30；`MODEL-SELF-ATTENTION`，handoffexecution与distributed-training owners。全文覆盖trilinear formulation/proof、Triton forward/backward、scaling fit、ablations与appendices。
- **Problem / mechanism / ownership:** dot-product attention只表达pairwise interaction；直接higher-order attention是O(n³)。论文以Q/K/K′ trilinear score和V∘V′ value表示三元interaction，再以sliding windows把复杂度限制到O(n w1 w2)，每四层插入一个2-simplicial layer；layer拥有projections/2-D online-softmax state，Triton kernel拥有tiled normalization和gradient accumulation。
- **Evaluation boundary:** 1B-active/57B-total至3.5B-active/176B-total MoE，比较标准Transformer并在GSM8K、MMLU、MMLU-Pro、MBPP拟合token-efficiency；作者报告larger scales改善，但hardware、precision、batch、training tokens与matched wall-clock/energy未完整披露，不能外推universal exponent或long-context优势。
- **Trade-off / coexistence / disposition:** richer interaction换K′/V′ state、2-D normalization、kernel specialization、window tuning、数值和portability风险；短序列、全局pairwise充分或缺优化kernel时dot-product仍合理。Books Frozen；`Emerging / Experimental`。

### Self-Correction Bench

- **Primary / date / owner:** `2507.02778` v1 2025-07-03，25/30；`AGENT-REFLECTION`，handoff `PLATFORM-EVALUATION-SYSTEM`、`TRAIN-SFT`与`TRAIN-GRPO`。后续v2/v3的扩展机制与结果不倒灌本周。
- **Problem / mechanism / ownership:** “不能纠错”混合了缺知识与未激活critic两种失败。benchmark把同一错误prefix分别放在assistant/internal与user/external role，比较role-conditioned continuation，再插入`Wait`等correction marker做因果干预；harness拥有error identity、role、budget与truth，model只拥有continuation，evaluator拥有correctness label。
- **Evaluation boundary:** SCLI5、GSM8K-SC、PRM800K-SC，14个open models、官方chat templates、temperature 0和有限token budget；作者用Gemini matcher并抽样人工复核，报告多数模型存在internal/external blind spot且marker明显改变结果。它证明role attribution会gate correction，不证明self-awareness、faithful CoT、first-error prevention或production safety。
- **Trade-off / coexistence / disposition:** test-time correction增加token/latency、false revision、marker imitation、prompt sensitivity与backtracking；hard SLO或已有external verifier的任务仍可one-pass/外部验证。Books Frozen；future `Refine — Existing Argument`。

### Answer Matching Outperforms Multiple Choice

- **Primary / date / owner:** `2507.02856` v1-only 2025-07-03及released annotations/code，27/30；`PLATFORM-EVALUATION-SYSTEM`，handoff `PLATFORM-OBSERVABILITY`、`PLATFORM-SECURITY`与`AGENT-REFLECTION`。全文覆盖formal task taxonomy、shortcut experiments、human study、ranking/cost与limitations/appendices。
- **Problem / mechanism / ownership:** MCQ便宜客观却只测discrimination并允许choices-only shortcuts；free-form generation更接近部署但人工评分昂贵。answer matching让candidate只看question并生成response，再让matcher在question、response与reference条件下判断semantic/functional equivalence；dataset拥有reference/valid-answer contract，candidate拥有response，matcher拥有binary label，harness拥有prompt/version/temperature。
- **Evaluation boundary:** 论文在MATH的rule-verifiable数据与人工标注的MMLU-Pro/GPQA-Diamond上比较MCQ、MCQ verify、reference-free judge和多种matchers；零温matcher、candidate generation budget与筛选规则已披露，hardware、precision、batch、concurrency和latency SLO未披露。结果支持filtered unique-answer任务上matching更贴近human/rule verification，不证明所有生成任务可被binary matching或matcher对adversarial optimization稳健。
- **Trade-off / coexistence / disposition:** 增加matcher call和reference curation，仍有false acceptance、prompt injection、version drift与reference wording overfit；deployment本身是discrimination时MCQ仍合理，可执行oracle存在时应优先。Books Frozen；future `Refine — Existing Argument`。

### Bourbaki

- **Primary / date / owner:** `2507.02726` v1-only 2025-07-03，25/30；`AGENT-PLANNING`，handoff `AGENT-TOOL-CALLING`、`AGENT-REFLECTION`、`AGENT-WORKFLOW`与`PLATFORM-EVALUATION-SYSTEM`。全文覆盖self-generated goal-conditioned MDP、Lean/Pantograph implementation、MCTS、evaluation与limitations。
- **Problem / mechanism / ownership:** theorem proving具有长时、稀疏terminal reward；fixed-goal tree假设subgoals已知。Bourbaki允许action创建新goal，以ordered goal stack表示中间conjectures，MCTS用policy生成tactic/subgoal并由Lean verifier决定push/pop与commit；Lean/Pantograph拥有authoritative proof state和validity，search tree拥有goal stack、visit/value，policy只提议。
- **Evaluation boundary:** Pantograph 0.3.2、Lean/mathlib 4.20.1、vLLM、DeepSeek-Prover-v2-7B+Kimina-7B ensemble，N=10、K=512；PutnamBench上以executable Lean correctness比较whole-proof/tree baselines。它证明该setup下verified intermediate goals可提高solved count/sample efficiency，不证明wall-clock/compute优势、general theorem-proving superiority或heuristic completion始终sound；hardware、precision、batch、concurrency/SLO未披露。
- **Trade-off / coexistence / disposition:** denser signal换更多verifier calls、search memory、branch explosion、duplicate states、goal-order bias与reward hacking；短proof/强policy仍适合whole-proof sampling，预定义subgoal时fixed tree更简单。Books Frozen；future `Refine — Existing Argument`。

### Thinking with Images for Multimodal Reasoning

- **Primary / date / owner:** `2506.23918` v1 2025-06-30（v2/v3为同周revision）及living bibliography，21/30；`MULTIMODAL-REPRESENTATION`，handoff generation、world-model、embodied、Agent tool/planning与evaluation owners。全文覆盖taxonomy、implementation routes、benchmarks、applications、cost/safety与appendix。
- **Problem / mechanism / ownership:** static one-shot visual encoding加text-only CoT会丢失空间/细节状态，无法反复检查、操作或模拟。survey区分external visual-tool exploration、programmatic canvas manipulation和intrinsic visual imagination；controller拥有goal/tool selection，visual workspace拥有artifact version/coordinates，perception/generator负责transform，verifier/environment才拥有validity。
- **Evidence boundary:** 这是source map与taxonomy，不是新的controlled experiment；benchmark tables不能支持统一性能结论，也不证明三个stage单向演进、imagined image faithful或visual state普遍优于text。hardware/model/precision/length/batch/concurrency/SLO不适用或未披露。
- **Trade-off / coexistence / disposition:** mutable visual state增加token/compute、dense error propagation、artifact drift与provenance loss；immutable evidence和one-pass perception足够时static image仍合理。`No Change — Already Covered / Weekly Survey Evidence`；Books Frozen。

### JAM-Flow

- **Primary / date / owner:** `2506.23552` v1 2025-06-30及project page，23/30；`MULTIMODAL-GENERATIVE-PARADIGMS`，handoff representation/timestamp、embodied、execution、security/evaluation owners。2026 v2仅作later revision。
- **Problem / mechanism / ownership:** cascaded TTS→head animation可复用、易调试，但audio和motion独立生成会损失相互conditioning与sync。JAM-Flow以Motion-DiT和F5-TTS初始化的Audio-DiT做conditional flow matching，通过selective partial joint attention、audio-length-scaled RoPE、local temporal mask与condition dropping实现双向耦合；两个DiT保留modality-specific latent，joint blocks拥有cross-modal exchange。
- **Evaluation boundary:** CelebV-Dub training，HDTF/LibriSpeech-PC/CelebV-Dub tests，WER、SIM、FID/FVD、LSE与26人user study；4×RTX 6000 Ada约1天、32 NFE、单A6000生成20秒样本约45秒，但baselines非hardware matched。证据支持作者setup的sync-quality折中，不证明real-time、一般视听生成或matched-compute superiority。
- **Trade-off / coexistence / disposition:** joint co-adaptation换training instability、modality interference、metric fragility、length/style failure与deepfake风险；独立升级、单模态质量或严格latency优先时cascade仍合理。Books Frozen；`No Change — Already Covered`或bounded case。

### μ²Tokenizer

- **Primary / date / owner:** `2507.00316` v1 2025-06-30（v2同周revision），23/30；`MULTIMODAL-REPRESENTATION`，handoff `TRAIN-DPO`与`PLATFORM-EVALUATION-SYSTEM`。全文覆盖method、implementation、evaluation和ablations。
- **Problem / mechanism / ownership:** 3-D CT fixed pooling或hard top-k虽便宜有界，却会丢边界、阻断dropped-token gradient并忽略question relevance。μ²Tokenizer把ViT3D tokens经过relative-position attention、differentiable global soft top-k、[1,2,4] multi-scale pooling和question-conditioned aggregation再交给LLM；vision encoder拥有dense volume tokens，tokenizer拥有compression weights，question提供selection context，GREEN harness拥有preference labels。
- **Evaluation boundary:** AMOS-MM、CT-Rate、AbdomenAtlas，1B Llama-3.2+M3D-CLIP ViT3D，bf16/DeepSpeed、4×A40 48GB、k=1024、8×32×256×256 input；比较LaMed/CT-CHAT/RadFM/RadGPT并做RPE/DTS/DMTP与SFT/DPO ablations。它支持作者数据和metric下的compression/alignment增益，不证明clinical safety、general tokenizer superiority或DPO因果独立于GREEN reward。
- **Trade-off / coexistence / disposition:** differentiability/detail换更多attention/memory、soft selection blur、reward bias和synthetic-data coupling；tight compute或需要明确sparse identity时hard top-k/fixed pooling仍合理。Books Frozen；`Experimental / No Change — Already Covered`。

### ARIG

- **Primary / date / owner:** `2507.00472` v1-only 2025-07-01及project page，24/30；`MULTIMODAL-GENERATIVE-PARADIGMS`，handoff representation/timestamp、embodied与inference state scheduling。全文覆盖method、data、metrics、ablations与limitations。
- **Problem / mechanism / ownership:** clipwise或speaker/listener-switched generation便于batch和复用，却依赖future signal并产生transition discontinuity；VQ motion又会丢面部细节。ARIG使用framewise AR、cached short summaries与long-range context，显式VAD conversation-state unit，并以15-step diffusion生成每帧continuous 262-D motion；cache拥有compressed history，CSU拥有speaking/listening/interruption state，sampler拥有next-motion distribution。
- **Evaluation boundary:** >200h MultiDialog/ViCo/RealTalk，RealTalk/ViCo/HDTF及多种motion/sync/image metrics和user study；25fps input、作者报告31fps generation，但hardware、precision、batch和p99 deadline未披露。结果支持其组件和continuous framewise state，不证明end-to-end conversational latency、general avatar generation或matched-hardware superiority。
- **Trade-off / coexistence / disposition:** continuity/detail换AR error accumulation、cache invalidation、VAD misclassification、diffusion deadline jitter与renderer coupling；offline或strict deterministic budget下clipwise/VQ仍合理。Books Frozen；`Experimental / No Change — Existing Hybrid-State Contract`。

### Mixture of Reasonings

- **Primary / date / owner:** `2507.00606` v1 2025-07-01（v2同周），20/30；`TRAIN-SFT`，handoff `AGENT-PLANNING`与`PLATFORM-EVALUATION-SYSTEM`。事件时短论文全文已读。
- **Problem / mechanism / ownership:** task-specific CoT prompt透明且免训练，但对small model很脆弱。closed teacher生成50～500个strategy templates，每个sample选5个、再由teacher选择template和生成trace，evaluator只保留正确结果，最终作为Qwen2.5-7B SFT data；curator/teacher拥有template pool与selection，evaluator拥有acceptance，student weights只内化行为，论文没有runtime router证据。
- **Evaluation boundary:** HotpotQA、StrategyQA、MMLU、BigTom与Creative Writing，样本规模小，多数约50/task；报告总体有限改善但per-task nonmonotonic。hardware、precision、training size、seed、significance与contamination未披露，不能证明strategy autonomy、broad generalization或reasoning faithfulness。
- **Trade-off / coexistence / disposition:** inference prompt简化换offline teacher cost、closed-model bias、leakage和opaque internalization；需要可审计/可快速修改策略或数据少时runtime prompting仍合理。Books Frozen；`No Change — Already Covered / Weekly Experimental`。

### Kwai Keye-VL Technical Report

- **Primary / date / owner:** `2507.01949` v1-only 2025-07-02及official repo/model family，23/30；`MULTIMODAL-REPRESENTATION`，handoff generation/world-model、SFT/GRPO和distributed-training owners。全文覆盖architecture、data/training、post-training、infra、evaluation、decontamination与limitations。
- **Problem / mechanism / ownership:** fixed-resolution frozen ViT+projector稳定易复用，但难保留native-resolution detail、video temporal order与多种reasoning mode。Keye-VL以resolution interpolation+2D RoPE+NaViT packing适配SigLIP ViT，MLP接Qwen3-8B，3D RoPE统一text/image/video且映射时间；四阶段pretraining后做SFT、MPO、mix-mode GRPO。preprocess拥有patch/frame/time identity，checkpoint+data cursor拥有recovery，reward/controller只提供provisional mode/reward。
- **Evaluation boundary:** >600B multimodal tokens、image/video token caps、DP+SP+ZeRO、FLOP-aware balancing与32K packing披露；public benchmarks和internal 150+150 open-ended QA有stage/position ablations，但hardware、precision、global batch、concurrency/SLO未披露且component effects confounded。结果不证明auto-think是calibrated confidence或training infra更快。
- **Trade-off / coexistence / disposition:** native resolution增加sequence/KV/imbalance，absolute-time position耦合sampling identity，multi-mode增加routing与reward error；bounded image/strict-cost时fixed encoder和non-thinking path仍合理。Books Frozen；`No Change — Already Covered / Bounded Case`。

### LongAnimation

- **Primary / date / owner:** `2507.01945` v1 2025-07-02及project/code link，23/30；`MULTIMODAL-GENERATIVE-PARADIGMS`，handoff representation identity、world state与KV-cache owner。W28 v2是same-family revision。
- **Problem / mechanism / ownership:** local overlap可维持相邻连续性却在300～1000帧丢global identity，last-frame AR还会累积噪声。frozen CogVideoX+SketchDiT使用Dynamic Global-Local Memory：动态分段压缩history、保留中层KV并让当前condition跨注意global/local memory；CCR约束reference/generated KV，late denoising做overlap-latent fusion。history KV是compressed evidence，不拥有semantic truth。
- **Evaluation boundary:** Sakuga-42M筛至约80K长clips，1024×576、6×A100，三个training stage；short/long subsets、FID/FVD/PSNR/LPIPS/SSIM及local/global/CCR/fusion ablations。结果支持该anime colorization contract，不证明general long-video、real-time、semantic identity或matched-compute 5× length；precision、batch、SLO和memory overhead未披露。
- **Trade-off / coexistence / disposition:** global memory减少drift却增加第二模型、cache growth/version、summary loss与recovery问题；短clip、tight memory或稳定reference时local-only/fixed-reference仍合理。Books Frozen；`Emerging / Experimental`。

### VLA Models: An Action Tokenization Perspective

- **Primary / date / owner:** `2507.01925` v1-only 2025-07-02，24/30；`MULTIMODAL-EMBODIED-VLA`，handoff world-model、Agent planning/workflow owners。70页survey全文覆盖八类token、data/training/inference/hardware/safety与outlook。
- **Problem / mechanism / ownership:** VLA比较混乱，因为“action token”可能指raw control、language plan、code、affordance、trajectory、goal state、latent或reasoning。survey把module定义为最大differentiable subnetwork或non-differentiable functional unit，强调hierarchical combinations；每个module拥有provisional representation，low-level controller拥有executable conversion，environment拥有outcome truth，safety layer拥有veto。
- **Evidence boundary:** 没有新experiment、baseline、ablation或统一hardware contract；它提供vocabulary与source map，不证明taxonomy完备、任一token普遍优越或层级化必然成为主流。underlying claims仍需回到primary source。
- **Trade-off / coexistence / disposition:** language/code可解释却弱grounding，trajectory/affordance可控却依赖perception/controller，latent压缩却不透明，raw action减少handoff却放大embodiment/data coupling。各分支按任务共存。`No Change — Already Covered / Survey Evidence`；Books Frozen。

### Depth Anything at Any Condition

- **Primary / date / owner:** `2507.01634` v1-only 2025-07-02及official project/code，24/30；`MULTIMODAL-REPRESENTATION`，handoff embodied、pretraining与evaluation owners。全文覆盖method/formulas、implementation、all evaluation suites、component/training/perturbation/freeze/loss-weight ablations与appendix。
- **Problem / mechanism / ownership:** clean-image foundation depth能广泛zero-shot，但在low light/weather/sensor corruption下失效；直接用corrupted pseudo-label不可靠。frozen DepthAnythingV2 teacher与student接收weak/original和strong perturbations，以affine-invariant consistency、KD safeguard和Spatial Distance Relation训练；augmentation policy拥有corruption prior，teacher拥有reference prediction，student拥有robust prediction，ground truth才拥有outcome。
- **Evaluation boundary:** 540K unlabeled images、ViT-S+DPT、4×RTX3090、518²、batch16、20 epochs；DA-2K corruption、NuScenes/RobotCar night、DrivingStereo weather、KITTI-C及normal datasets，含perturbation、SDR、freeze、loss与lambda sensitivity。结果支持该model/corruption contract，不证明arbitrary open-world robustness、metric geometry、robotics safety或production latency；SDR的O((HW)^2)成本未核算。
- **Trade-off / coexistence / disposition:** targeted invariance可能抹掉物理有效变化，frozen encoder保留generalization却限制适配，teacher error被蒸馏，SDR昂贵且可能学coordinate prior。clean/general或有verified labels的stable domain仍适合原foundation/full finetune。Books Frozen；`Emerging / Experimental`。

### IntFold

- **Primary / date / owner:** `2507.02025` v1 2025-07-02（v2同周）及official source/server，21/30；`TRAIN-PRETRAINING`，handoff data、LoRA、evaluation与kernel execution owners。全文覆盖architecture/data/MSA/templates、Triton kernel、consensus ranking、adapters、evaluation、stability与appendix/limitations。
- **Problem / mechanism / ownership:** general biomolecular predictor难接受pocket/epitope/rare-conformation constraints，也难以低成本specialize；diffusion decoys和Pairformer pair-bias又带来selection与memory压力。IntFold在general trunk上叠加per-layer LoRA/constraint embedder和post-hoc affinity blocks，以25次预测的all-pairs DockQ consensus选结构；FlashAttentionPairBias按tile从HBM到SRAM广播而不物化完整bias。base、adapter/constraint、decoy seed、selector evidence、checkpoint/data cursor与precision policy各自拥有状态。
- **Evaluation boundary:** FoldBench、PoseBusters、CDK2、guided folding、affinity与post-2024 subsets，含adapter/constraint、random-vs-consensus、normalization和stability comparisons；AF3因license未在同harness rerun。hardware、accelerator count、batch、concurrency/SLO未披露，IntFold+同时改变多项recipe且无component isolation。证据不支持一般优于AF3、consensus等于truth或training阈值可迁移到LLM。
- **Trade-off / coexistence / disposition:** controllability增加adapter/version/constraint risk；consensus带来25×generation和O(K²) compare；skip-and-recover改变sample distribution，FP32 diffusion增加cost，on-demand kernel增加specialization。无可靠domain data/constraint或budget小仍适合general model/learned confidence。Books Frozen；future `Refine — Existing Argument`。

### Can LLMs Identify Critical Limitations?

- **Primary / date / owner:** `2507.02694` v1-only 2025-07-03，24/30；`PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-RAG`与`AGENT-MULTI-AGENT`。全文覆盖LimitGen-Syn受控扰动、LimitGen-Human人工论文评论、Semantic Scholar retrieval、multi-agent review、judge protocol、实验与limitations。
- **Problem / mechanism / ownership:** 语言模型常能生成数量很多但不关键的批评，而“关键限制”依赖问题、claim、evidence与实验边界的联合判断。论文以受控注入和真实review分别评估limitation detection，并比较直接生成、retrieval augmentation与multi-agent review；文献库拥有evidence identity，retriever拥有coverage/ranking，critic生成候选，judge/human rubric拥有acceptance，评论数量不等于证据质量。
- **Evaluation boundary:** 作者实验支持当前模型识别关键限制仍落后人类、增加评论数量不会自动改善criticality，retrieval收益依赖文献覆盖与相关性；不证明LLM judge是ground truth、multi-agent普遍优于单Agent，或该数据能覆盖部署中的全部failure mode。hardware、precision、batch、concurrency与SLO未披露。
- **Trade-off / coexistence / disposition:** retrieval增加可追溯性也引入index freshness、false-negative与citation mismatch；multi-agent增加perspective也增加communication tax、shared blind spot与judge coupling。已知领域、稳定rubric和人工专家仍是高风险release gate的必要分支。Books Frozen；future `Refine — Existing Argument`。

### LangScene-X

- **Primary / date / owner:** `2507.02813` v1-only 2025-07-03及official project/repo，22/30；`MULTIMODAL-REPRESENTATION`，handoff生成范式与world-model owners。全文覆盖TriMap/LQC公式、surface reconstruction、implementation、baselines、metrics、ablations、结论与artifact；repo中的generalizable LQC/improved TriMap仍为TODO。
- **Problem / mechanism / ownership:** dense calibrated views与per-scene NeRF/3DGS在观测充分时证据清楚，却难服务仅两视图的unseen scene。LangScene-X以CogVideoX progressive training生成RGB/normal/semantic TriMap，以K=2048、D=3的LQC压缩CLIP feature，再经DUSt3R初始化和分阶段3DGS优化；capture/calibration、diffusion latent/seed、mapper revision、codebook与surface state均需独立版本化，生成状态不能冒充观测事实。
- **Evaluation boundary:** 8×A800 80GB、720×480×49 frames，LERF-OVS与ScanNet小规模scene、2D localization/segmentation和局部ablation支持该受限pipeline可行；不证明生成的未观测区域具有3D/物理真实性、D=3/K=2048普适、端到端更快省内存或可安全用于robot action。precision、inference steps、latency/concurrency/SLO未披露，pseudo labels可能共享blind spot。
- **Trade-off / coexistence / disposition:** sparse capture与跨scene复用换来hallucinated unseen state；统一generator可能让多模态共同出错；离散codebook带来collision、quantization与version drift。accuracy/provenance优先且dense views可得时，per-scene reconstruction和continuous feature仍更合理。Books Frozen；`No Change — Already Covered / Experimental Case`。

### Heeding the Inner Voice

- **Primary / date / owner:** `2507.02321` v1-only 2025-07-03及official code，24/30；`MULTIMODAL-GENERATIVE-PARADIGMS`，handoffrepresentation与world-model owners。全文覆盖preliminaries、method/equations、implementation、results、alignment/reward-step ablations、appendix、limitations与artifact；事件硬件按v1的8×H100约6小时锁定，current repo的8×A100只作later artifact evidence。
- **Problem / mechanism / ownership:** standard diffusion objective不直接保证spatial control一致；late final-image reward可靠但覆盖不到结构形成的early trajectory，机械扩到early noisy x0又产生domain shift。方法以timestep-conditioned probe从UNet intermediate features恢复edge/depth，在全trajectory施加alignment loss，同时保留diffusion loss和bounded late reward。输入control是authoritative target，intermediate feature与probe estimate只是step-local provisional state，final verifier不能被internal probe取代。
- **Evaluation boundary:** SD1.5 ControlNet、512²、batch256、2.56M synthetic samples/task、5k evaluation samples、HED/LineArt/depth及四批独立samples支持该contract下改善control/quality operating point；不证明probe等于calibrated world state、适用于所有control/backbone或production workload。precision、interconnect、inference latency/concurrency/SLO未披露，synthetic/control-extractor可能形成correlated blind spot。
- **Trade-off / coexistence / disposition:** trajectory-wide feedback换来probe capacity/version、loss weighting、训练成本与feedback correlation；错误probe会把偏差压入内部表示。final extractor可靠、算力受限或control主要在late refinement时，late reward/standard ControlNet仍合理。Books Frozen；future `Refine — Existing Argument`。

### RAT / Recurrent Attention Transformer

- **Candidate / identity / event:** RAT / 2025-W27 / 27/30；Source Family `ARXIV-2507.04416`，arXiv v1 2025-07-06，official repository同族。W28只是发现位置，不拥有评分；later revision不得改变本周event-time归属。
- **Access / coverage / owner:** v1正文与artifact已覆盖recurrence、associative scan、training/prefill/generation实现、evaluation、chunk-size/decay ablations、limitations；owner `MODEL-LONG-CONTEXT`，handoff `MODEL-SELF-ATTENTION`、`MODEL-KV-CACHE`与`INFER-DECODE`。
- **Problem / previous design / changed constraint:** full attention对任意历史token直接寻址，质量强且实现成熟；长序列使attention compute与KV state随T增长。constant-state recurrent model更省状态，却可能丢失可寻址细节。RAT尝试在两端之间建立由chunk大小控制的连续谱。
- **Mechanism / state / control-data flow:** 输入按chunk处理；chunk内维护EMA式mutable recurrent state，chunk完成后原子提交一个K/V summary。当前chunk保持细粒度causal state，query同时读取已提交summaries与当前chunk。model artifact拥有recurrence/decay/chunk contract，runtime拥有summary cache identity和commit boundary，不能把summary误当原始token KV。
- **Implementation / evaluation contract:** 200M与1.3B模型、H100以及作者长序列任务比较full attention与recurrent baselines；hardware/model/length按论文表格成立，production batch/concurrency、TP/CP、p99 SLO Not Disclosed。结果支持作者setup中cache/compute/quality frontier，不证明7B+、instruction parity、分布式故障恢复或任意long-context workload。
- **Trade-off / failure / coexistence / disposition:** chunk增大保留更多局部信息却提高state/compute；chunk变小增加有损压缩、boundary与RoPE sensitivity。full attention在短上下文或精确回看优先时仍合理，constant-state recurrent在极端state预算下仍合理。`Emerging / Experimental`；Books Frozen。

### GradOT

- **Candidate / identity / event:** GradOT / 2025-W27 / 26/30；Source Family `ARXIV-2507.04455`，sole v1 2025-07-06。W28发现记录需去重，不形成第二owner。
- **Access / coverage / owner:** v1全文覆盖Taylor/Hessian推导、Dynamic Rank Decomposition、Selective Channel Pruning、8-task evaluation、compression cost、lambda/support-data/ratio sensitivity、approximation error与limitations；无author artifact。owner `TRAIN-LORA`，handoff `PLATFORM-MULTI-TENANT`与`PLATFORM-SECURITY`。
- **Problem / previous design / changed constraint:** offsite tuning需要把可调模型送到private-data owner。发送full model最直接但扩大权重与数据共址风险；LayerDrop/CRaSh式emulator便宜，却未显式保存full-model gradient behavior；distillation/ScaleOT更贵。约束转为“较小emulator训练出的adapter回插full model仍有效”。
- **Mechanism / state / control-data flow:** `GCS=||H_iδ_i||_1-λ(∂ℓ/∂w_i⊙δ_i)`为MHA SVD components与MLP paired channels评分。model owner用support data构建emulator；data owner只在emulator上训练首末adapter；returned adapter再挂回original middle block。emulator、support-data版本和adapter/base identity必须共同追踪，adapter不拥有privacy证明。
- **Implementation / evaluation contract:** OPT-1.3B/6.7B、LLaMA-7B/13B、8个QA任务、约60/70% emulator、single A100 80GB。证据支持作者任务中较低构建成本下的plugin utility，不证明formal privacy、model-extraction resistance、70B/MoE或真实组织trust boundary。
- **Trade-off / failure / coexistence / disposition:** Taylor/Fisher近似、component independence、support mismatch和lambda/ratio都可能使回插失效；较弱emulator仍可能泄漏模型信息。full fine-tuning/普通LoRA在单一trust domain仍更简单，正式privacy仍需DP/TEE/access control。`Emerging / Experimental`；Books Frozen。

### Controllable diffusion LM / S³

- **Candidate / identity / event:** Controllable diffusion LM / S³ / 2025-W27 / 22/30；Source Family `ARXIV-2507.04504`，v1 2025-07-06；later v2仅为revision evidence。
- **Access / coverage / owner:** v1全文覆盖AR与masked-diffusion formulation、schema scaffolding、semantic `null`、WikiBio evaluation、structure/content/hallucination metrics与8/16/32-step sensitivity；event-time code/data未发布且正文无独立Limitations section。owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `PLATFORM-EVALUATION-SYSTEM`。
- **Problem / previous design / changed constraint:** left-to-right AR配合grammar能稳定syntax，但早期value错误难回修；自由masked diffusion可全局修正，却必须同时解决output length与结构合法性。结构化生成的新约束是固定schema与可变事实值同时存在。
- **Mechanism / state / control-data flow:** S³预填immutable bracket/field-name tokens，只让value slots保持mask，并允许证据不足的slot生成语义`null`。schema owner拥有field/max-slot contract，denoiser拥有多步mutable values，parser/verifier才拥有最终syntax/semantic acceptance；模型自己的`null`不是外部置信度证明。
- **Implementation / evaluation contract:** 单一LLaDA/WikiBio/RTX4090合同下比较structure、content与hallucination指标，并扫8/16/32 denoising steps。结果支持scaffold改善作者结构指标、semantic null缓解固定slot overgeneration；不证明优于AR grammar/function calling、普遍JSON validity、事实正确或生产latency/SLO。
- **Trade-off / failure / coexistence / disposition:** schema/max slots、null/value collision与多步compute形成新债务，mandatory-slot仍可能hallucinate。hard grammar+AR在低延迟、严格parser contract时仍合理；S³是global refinement的Alternative Branch。`Emerging / Experimental`；Books Frozen。

### DP-Fusion

- **Candidate / identity / event:** DP-Fusion / 2025-W27 / 27/30；Source Family `ARXIV-2507.04531`，v1 2025-07-06；later revisions/artifact只作forward evidence。
- **Access / coverage / owner:** v1全文覆盖group-level RDP threat model、mixture/monotonicity/bisection、transcript composition theorem、TAB-ECHR evaluation、attacks、Appendix proofs/tables/prompts/Wilson intervals与limitations。owner `PLATFORM-SECURITY`，handoff `PLATFORM-MULTI-TENANT`与`INFER-DECODE`。
- **Problem / previous design / changed constraint:** 输入redaction简单、便宜且可审计，但会丢utility；对整个文档统一DP噪声又忽略不同PII group的边界。目标转为在生成时对每个敏感group分别控制泄漏，同时保留public context。
- **Mechanism / state / control-data flow:** 每个output step计算public distribution与各private-group distribution，用bisection求满足对称Rényi-divergence预算的最大`λ_i`，再平均group mixtures采样。NER/oracle拥有group identity与budget，decoder维护prefix、`λ_i`和累计budget；保证针对add/remove one group并假设groups independent，不覆盖跨group语义关联。
- **Implementation / evaluation contract:** Qwen2.5-7B FP16、single A100、100个TAB-ECHR documents、最多8 groups、`T≤900`，并含LOSS/Min-K attacks。证据支持perfect-annotation/open-model合同下的conditional group-level bound与utility/privacy frontier；不证明whole-document DP、imperfect NER、correlated PII、closed API或production SLO。
- **Trade-off / failure / coexistence / disposition:** 每token需要`m+1`次forward，budget随length composition；漏标token会逃逸，过度分组会伤utility。redaction、TEE、access control仍分别解决不同边界。`Emerging / Experimental`；Books Frozen。

### vLLM CompilationConfig / CLI `-O` RFC #20283

- **Candidate / identity / event:** official GitHub RFC issue `vllm-project/vllm#20283`，opened 2025-06-30，25/30；Source Family `VLLM-RFC-20283`。issue与讨论已读，后续PR/release是同族implementation nodes，不回写成事件时已交付事实。
- **Problem / mechanism / ownership:** 既有`CompilationConfig`同时服务用户CLI和compiler内部，V1又存在hard-coded defaults，导致optimization level、compile mode、CUDA graph和startup cost控制含混。RFC提议把mode与`-O0..O3` optimization intent拆开，并集中default resolution；config owner应产生resolved execution-plan identity，runtime/compiler才拥有graph/cache state。
- **Evidence / boundary / trade-off:** primary issue证明设计动机、proposed levels、sunset选项和out-of-scope，不证明所有proposal在W27已合并、性能随O等级单调、兼容矩阵或生产SLO。简化UX会引入preset semantic drift、startup/steady-state取舍、hidden fallback和config migration风险；fine-grained flags仍适合调试与特殊模型。
- **Owner / disposition:** `INFER-TENSORRT-LLM` execution-plan owner，handoff `INFER-VLLM`与observability。`Weekly Only — Design Intent / Mechanism Not Shipped`；Historical Books Gate关闭。

### vLLM Q3 2025 Roadmap #20336

- **Candidate / identity / event:** official GitHub roadmap issue `vllm-project/vllm#20336`，opened 2025-07-01，23/30；Source Family `VLLM-ROADMAP-2025Q3-20336`。issue body与event-time discussion已读，later checked boxes/linked PRs只作演进节点。
- **Problem / mechanism / ownership:** roadmap把V1 parity、scheduler、speculation、multimodal input、startup、reproducible performance、MoE scale-out、P/D、autoscaling与SLO observability列为Q3压力图。它证明maintainer intent与模块耦合被显式识别，但roadmap不是一个统一mechanism，也不证明任务完成、兼容性、性能或故障恢复。
- **Trade-off / boundary:** broad roadmap有助于依赖治理，却会把不同成熟度、owner与时间尺度压到同一清单；checked state可随后变化。每个机制仍必须回到具体RFC/PR/release/code与evaluation contract。`Weekly Only — Official Plan / Mechanism Not Disclosed`；Books Frozen。

### SGLang Q3 2025 Development Roadmap #7736

- **Candidate / identity / event:** official GitHub roadmap issue `sgl-project/sglang#7736`，opened 2025-07-03，23/30；Source Family `SGLANG-ROADMAP-2025Q3-7736`。event-time body与later completion state分离读取。
- **Problem / mechanism / ownership:** issue把advanced-feature compatibility、overlap scheduler、piecewise CUDA graph、mem_cache_v2、speculation、HiCache、parallelism/P-D、quantization、RL integration与Multi-LoRA列为共同可靠性压力。它证明项目认识到feature×feature compatibility而非单feature速度是系统约束；不证明15/17后来完成的项目在W27已存在，也不提供统一benchmark或SLO。
- **Trade-off / boundary:** roadmap作为协调账本能显式依赖，却不能替代component ownership、state identity、rollback与versioned test matrix；later closure也可能隐藏部分实现边界。`Weekly Only — Official Plan / Mechanism Not Shipped`；Books Frozen。

### Unverified / Blocked ledger（1 retained family）

- **P1 Full Text — MARVIS `2507.01544`:** arXiv identity与v1 date 2025-07-02可核；current repository公开embedding→dimensionality reduction/visualization→VLM classification pipeline、supported encoders与可运行benchmark入口，later OpenReview/current revision也可访问。但`2507.01544v1` PDF/TeX/TXT在本环境无法取得，later manuscript与current repository不能证明事件时Method、实验表、ablation、limitations和artifact状态。可接受材料为事件时v1 PDF/HTML/TXT或作者提供的hash-identical archive，建议文件名`2507.01544v1-marvis.pdf`。材料补回后需完成公式/algorithm、visualization choices、all datasets/baselines、model/prompt/hardware、ablation/sensitivity、privacy claim和limitations审计。按用户允许的blocked-skip继续，但该family不计source-complete、不得进入Books。

### Low-score source/date/rejection closure

- **Calligrapher（18/30，`2506.24123`，v1 2025-06-30）：** typography customization有任务价值，但对通用AI System state/runtime contract影响有限。`Rejected — Narrow Application Mechanism`。
- **Thinking Beyond Tokens（16/30，`2507.00951`，v1 2025-07-01）：** broad synthesis/survey没有隔离的新机制或可审计系统实验。`Rejected — Survey / No Isolated Mechanism`。
- **FreNBRDF（17/30，`2507.00476`，v1 2025-07-01）：** neural BRDF是domain-specific representation，不改变通用multimodal/training/runtime contract。`Rejected — Domain-Specific Representation`。
- **FreeMorph（19/30，`2507.01953`，v1 2025-07-02）：** training-free image morphing的10×～50×只绑定作者baselines/setup。`Rejected — Task-Specific Training-Free Editing`。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / technical report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系是本项目推断，已显式标注。

## Cross-Week Deduplication

- Ovis-U1、MoCa、Ella、MARBLE、RExBench、ThinkSound、RoboScape、VOCABTRIM、CRISP-SAM2、HalluSegBench、Radial Attention、DiffuCoder、Automated LLM Speedrunning等按arXiv v1回拨W26；Aha Moment Revisited与BlenderFusion回拨W25。
- vLLM `v0.9.2` official release为2025-07-07，归W28；later revisions留在同一Source Family，不重复评分。
- RAT `2507.04416`、GradOT `2507.04455`、S³ `2507.04504`与DP-Fusion `2507.04531`的v1 date均为2025-07-06，已从W28回拨W27；W28须删除对应评分owner，只保留spillback说明。
- GLM-V current HTML混入4.5V/4.6V，W27 packet严格锁定4.1V v1事实；后续模型只作evolution evidence。

## Knowledge Tree Position

- 已完成owner覆盖`TRAIN-GRPO`、`TRAIN-TENSOR-PARALLEL`、`TRAIN-SFT`、`MODEL-TRANSFORMER-LAYER`、`MULTIMODAL-REPRESENTATION`、`MULTIMODAL-GENERATIVE-PARADIGMS`、`PLATFORM-EVALUATION-SYSTEM`与`AGENT-WORKFLOW`。
- MARVIS的owner只作导航，取得事件时v1全文并完成相邻章节审计前不能形成final机制disposition。3个proposal已限定为Weekly-only plan/design facts，不把later shipping倒灌到W27。

## Recommended Action

- MARVIS按精确材料清单等待事件时v1正文；按blocked-skip规则不阻塞forward cursor。3个proposal保持Weekly-only，后续实现只在真实release week形成implementation node。
- 当前状态是`41 scored owners；36/37 retained source-complete；Review Pending 0；1 Full-text Blocked`。W27 Candidate Evidence Gate在blocked-skip下Conditional Pass；Archive/Discovery Recall与Historical Books Gate仍Open/Closed，不能表述为年度归档完成。
- Historical Books Gate关闭，本轮不修改Books。

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

`Frozen — Historical Books Gate Closed`。已完成packet中的future disposition仅是provisional owner judgment；不能在W27 Evidence Gate和年度Archive/Discovery Gate通过前写入Books。


## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。

## Repository Changes

- 在已有重放基础上回拨4个误归W28的07-06 owner，将W27更新为41项六维评分、36份source-complete review、1份精确Full-text Blocked清单与4份低分闭合。
- 本文件只修改W27；年度索引、Learning State以及W28的4项重复owner需由串行总账owner同步。本阶段未修改Books。

## Open Questions

- MARVIS的`2507.01544v1`原始正文能否补回，并验证论文的privacy措辞、all-dataset baselines与ablation？
- Google Scholar/OpenAlex/DBLP/Crossref若能取得immutable export，是否会发现当前best-effort replay未召回的新W27 owner？
- AsyncFlow、ZeCO、EBT和WebSailor能否获得独立复现、same-budget对照和failure-recovery证据？

## Sources

- SPIRAL — https://arxiv.org/abs/2506.24119
- Calligrapher — https://arxiv.org/abs/2506.24123
- VMoBA — https://arxiv.org/abs/2506.23858
- Thinking with Images — https://arxiv.org/abs/2506.23918
- JAM-Flow — https://arxiv.org/abs/2506.23552
- μ²Tokenizer — https://arxiv.org/abs/2507.00316
- GLM-4.1V-9B-Thinking — https://arxiv.org/abs/2507.01006
- GLM-V repository — https://github.com/zai-org/GLM-V
- Does Math Reasoning Improve General LLM Capabilities? — https://arxiv.org/abs/2507.00432
- SciArena — https://arxiv.org/abs/2507.01001
- ARIG — https://arxiv.org/abs/2507.00472
- Thinking Beyond Tokens — https://arxiv.org/abs/2507.00951
- Mixture of Reasonings — https://arxiv.org/abs/2507.00606
- FreNBRDF — https://arxiv.org/abs/2507.00476
- ZeCO — https://arxiv.org/abs/2507.01004
- Kwai Keye-VL Technical Report — https://arxiv.org/abs/2507.01949
- LongAnimation — https://arxiv.org/abs/2507.01945
- VLA Models: An Action Tokenization Perspective — https://arxiv.org/abs/2507.01925
- Locality-aware Parallel Decoding — https://arxiv.org/abs/2507.01957
- MARVIS — https://arxiv.org/abs/2507.01544
- MARVIS repository — https://github.com/penfever/marvis
- Depth Anything at Any Condition — https://arxiv.org/abs/2507.01634
- FreeMorph — https://arxiv.org/abs/2507.01953
- IntFold — https://arxiv.org/abs/2507.02025
- Skywork-Reward-V2 — https://arxiv.org/abs/2507.01352
- Energy-Based Transformers — https://arxiv.org/abs/2507.02092
- AsyncFlow — https://arxiv.org/abs/2507.01663
- WebSailor — https://arxiv.org/abs/2507.02592
- Decoupled Planning and Execution — https://arxiv.org/abs/2507.02652
- Fast and Simplex — https://arxiv.org/abs/2507.02754
- Can LLMs Identify Critical Limitations? — https://arxiv.org/abs/2507.02694
- Self-Correction Bench — https://arxiv.org/abs/2507.02778
- Answer Matching Outperforms Multiple Choice — https://arxiv.org/abs/2507.02856
- LangScene-X — https://arxiv.org/abs/2507.02813
- vLLM CompilationConfig / CLI -O RFC #20283 — https://github.com/vllm-project/vllm/issues/20283
- vLLM Q3 2025 Roadmap #20336 — https://github.com/vllm-project/vllm/issues/20336
- SGLang Q3 2025 Development Roadmap #7736 — https://github.com/sgl-project/sglang/issues/7736
- Heeding the Inner Voice — https://arxiv.org/abs/2507.02321
- Bourbaki — https://arxiv.org/abs/2507.02726
- RAT / Recurrent Attention Transformer — https://arxiv.org/abs/2507.04416
- GradOT — https://arxiv.org/abs/2507.04455
- Controllable diffusion LM / S³ — https://arxiv.org/abs/2507.04504
- DP-Fusion — https://arxiv.org/abs/2507.04531
