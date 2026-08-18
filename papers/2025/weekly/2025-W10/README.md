# AI Research Weekly — 2025-W10

> Coverage Window: 2025-03-03～2025-03-09
> Research Mode: Retrospective Backfill
> Audit Status: Candidate Evidence Gate Passed again after seventh W12 recommendation-lag batch — 47 Full Source Reviews；6 low-score verifications；0 ordinary pending
> Historical Books Gate: Closed — Weekly evidence only
> Accessed: 2026-07-31
> Backfilled: 2026-07-31
> Re-audited: 2026-08-20

## Executive Summary

旧版周报只保留 EAGLE-3 与 Mistral OCR。本轮重放固定机构、3 月 3～9 日 academic feed/cross-index 与
工程 release与后续spillback，当前恢复43个真正归属W10的新增`20+` Source Family、6个低分或版本事实，并把Phi-4 report、
LADDER、Babel、Remasking等按first-public date回链W09。46个`20+`候选（含原EAGLE-3与后续DropletVideo spillback）均完成
非模板化 Full Source Review，低分项均完成身份、日期和拒绝理由核验，ordinary `Review Pending = 0`。
Scholar/OpenAlex/DBLP 的历史结果导出与少数工程项目 historical release feed 仍列为 Discovery Gap；因此
W10 Candidate Evidence Gate曾按declared-gap规则通过；前七批spillback均已审计。mechanistic-interpretability adversarial attack v1为2025-03-08，其白盒/refusal-subspace边界已完成Full Source Review，当前Gate再次通过。年度Archive Completion Gate继续Open。本轮只维护
Weekly，Historical Books Gate 关闭。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；原两项访问日期保留 2026-07-31，本轮新增来源访问日期为 2026-08-20。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。
- Hugging Face Daily Papers 仅作 discovery feed；候选身份、v1、方法与实验均回到 arXiv/官方 artifact。
- Google Scholar、OpenAlex、DBLP 的可复算历史 export 尚未取得；这不伪装成零遗漏，而作为年度 Discovery Gap 延续。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：Mistral OCR（2025-03-06，产品事实）。
- Phi-4 Mini/Multimodal technical report（v1 2025-03-03）是 W09 official launch family 的 related evidence，
  不在 W10 重复计分。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 完成 43 个 `20+` Full Source Reviews；核心路线覆盖 speculative decoding、multimodal/post-training、
  data selection、quantization、pipeline memory、uncertainty/evidence、tool/agent runtime 与 world-consistent generation。
- 发现页在 3 月 3～7 日推荐、但 v1 属于 W09 的论文均回拨 W09，不使用推荐日期替代事件日期。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- JAX 0.5.2（2025-03-04）为修复 TPU metrics/`tpu-info` 的 patch release，完成低分核验；没有公开新的长期机制。
- ONNX Runtime v1.21.0（2025-03-08）由W11 fixed-source replay回拨并完成Full Source Review。
- vLLM、SGLang、KServe、Kubeflow、DeepSpeed、Megatron-LM 与 llama.cpp 的历史 release feed 未发现可稳定
  归属且达到门槛的新机制；无法导出的历史 feed 继续列入年度 Discovery Gap，而不是写成“绝对没有事件”。

## Candidate Scoring

评分针对 primary source 在 W10 事件时点的公开证据。论文作者 benchmark 不外推为通用结论；同一 family 的后续
revision/artifact 只用于机制核验，不重复计分。

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| EAGLE-3 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Must Read；与后续 MTP/SpecForge 联合进入第 44 章审计 |
| Mistral OCR | 4 | 3 | 3 | 3 | 3 | 3 | 19/30 | Record Only；未达 Books 门槛 |
| Visual-RFT | 4 | 4 | 4 | 5 | 5 | 5 | 27/30 | Books Pending — Refine multimodal verifiable-reward branch |
| Cognitive Behaviors / Four Habits of STaRs | 4 | 4 | 4 | 5 | 5 | 5 | 27/30 | Books Pending — Refine RL learnability preconditions |
| LLM Apprehension and Uncertainty | 3 | 4 | 4 | 4 | 5 | 5 | 25/30 | Books Pending — Refine calibrated abstention evidence |
| Liger | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Books Pending — Experimental recurrent-conversion branch |
| Large-Scale Data Selection for Instruction Tuning | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Refine data-selection contract |
| SampleMix | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Books Pending — Refine sample-wise mixture branch |
| RSQ | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | Books Pending — Refine calibration-token weighting |
| MultiAgentBench | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Refine topology/evaluator contract |
| MPO / Meta Plan Optimization | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Refine plan/execution separation |
| Mask-DPO | 4 | 4 | 4 | 5 | 5 | 5 | 27/30 | Books Pending — Experimental fine-grained factuality alignment |
| PipeOffload | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Books Pending — Refine PP activation-lifetime branch |
| IVR / Evolutionary Guided Decoding | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Experimental value-guided decoding |
| AppAgentX | 3 | 4 | 4 | 4 | 5 | 5 | 25/30 | Books Pending — Refine derived workflow memory |
| HoT / Highlighted Chain of Thought | 3 | 3 | 4 | 5 | 5 | 4 | 24/30 | Books Pending — Refine evidence UX / over-trust boundary |
| Process-based Self-Rewarding Language Models | 4 | 4 | 4 | 5 | 5 | 5 | 27/30 | Books Pending — Refine process-reward ownership |
| KodCode | 4 | 4 | 5 | 5 | 5 | 3 | 26/30 | Books Pending — Refine executable-data contract |
| Gen3C | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Books Pending — Experimental 3D-conditioned generation branch |
| ToolRet / Retrieval Models Aren't Tool-Savvy | 4 | 4 | 5 | 5 | 5 | 3 | 26/30 | Books Pending — Refine tool-registry retrieval contract |
| START | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Refine tool-in-reasoning trajectory loop |
| STORM | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Refine temporal token compression |
| Audio Flamingo 2 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Refine long-audio representation contract |
| JAX 0.5.2 | 1 | 2 | 3 | 5 | 3 | 3 | 17/30 | Weekly Only — Patch release / no new core mechanism |
| LLMVoX | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Weekly Only — Domain model / insufficient general mechanism |
| EgoLife | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Weekly Only — Application benchmark / no stable runtime mechanism |
| LINGOLY-TOO | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Weekly Only — Evaluation case / scope narrow |
| IFIR | 3 | 3 | 4 | 4 | 3 | 2 | 19/30 | Weekly Only — Domain retrieval benchmark |
| Unified Reward Model | 4 | 4 | 4 | 5 | 5 | 5 | 27/30 | Books Pending — Refine multimodal reward boundary |
| Sketch-of-Thought | 3 | 4 | 5 | 5 | 4 | 4 | 25/30 | Books Pending — Refine adaptive concise-reasoning branch |
| Forgetting Transformer / FoX | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Books Pending — Experimental attention branch |
| R1-Searcher | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Refine search-in-reasoning branch |
| SafeArena | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Refine Agent safety evaluation |
| Learning from Failures / Multi-Attempt RL | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Books Pending — Refine feedback-state branch |
| Linear-MoE | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Books Pending — Experimental architecture/runtime branch |
| WildIFEval | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Books Pending — Refine constraint-level evaluation |
| Long-Output LLM Survey | 2 | 4 | 4 | 4 | 5 | 4 | 23/30 | Books Pending — Refine output-length system contract |
| VisualSimpleQA | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Books Pending — Refine decoupled multimodal factuality evaluation |
| MoE-X / Intrinsically Interpretable MoE | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Experimental intrinsic-interpretability branch |
| Capacity-Aware Inference | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Books Pending — Refine MoE straggler/capacity contract |
| Collapse of Dense Retrievers | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Refine retrieval-bias and evidence-priority contract |
| OTTER | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Experimental VLA perception branch |
| MagicInfinite | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Books Pending — Experimental long-video/portrait generation branch |
| AI4SE Benchmark Review / BenchScout / BenchFrame | 3 | 4 | 5 | 4 | 5 | 4 | 25/30 | Books Pending — Refine benchmark lifecycle and test-coverage contract |
| LaMaTE / LLM as MT Encoder | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Refine encoder-decoder inference branch |
| More Documents, Same Length | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Refine multi-document RAG contract |
| ONNX Runtime v1.21.0 | 4 | 5 | 5 | 5 | 4 | 3 | 26/30 | Books Pending — Refine GenAI pipeline and execution-provider contract |
| Trajectory Distribution Matching / TDM | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Books Pending — Experimental few-step distillation branch |
| ProJudge | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Refine multimodal process-evaluation contract |
| ARMOR v0.1 | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Experimental asymmetric unified-generation branch |
| GoalFlow | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Books Pending — Experimental goal-conditioned embodied-planning branch |
| DropletVideo | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Books Pending — Refine camera/plot state data contract |
| Mechanistic Interpretability Adversarial Attack / SSR | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Books Pending — Refine white-box refusal threat model |

### Deep Analysis 1 — EAGLE-3

- First Public: 2025-03-03
- Status: arXiv v1; Experimental
- Primary Source: https://arxiv.org/abs/2503.01840
- Evolution Relationship: Direct Evolution

#### Why

speculative decoding 的上限由 draft 成本、接受长度和 target verification 成本共同决定；只扩大训练数据无法解除 feature-prediction bottleneck。

#### Principle and Mechanism

EAGLE-3 从 top-layer feature prediction 转向 direct token prediction，并融合多层 target features，以 training-time test 扩展 draft 训练。

#### Trade-off and Evidence Boundary

提高接受率仍需额外 draft state、训练数据和 verification compute；作者最高 speedup 与 SGLang throughput 结果绑定模型、硬件、batch 和实现，不能写成固定倍数。

#### Connection and Evolution

知识树位置：第 40、44、45、47、52 章。Must Read；与后续 MTP/SpecForge 联合进入第 44 章审计。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 2 — Mistral OCR

- First Public: 2025-03-06
- Status: Official model release
- Primary Source: https://mistral.ai/news/mistral-ocr
- Evolution Relationship: Layering / Dependency

#### Why

文档理解的瓶颈常在输入解析与结构保真，而不只在语言模型推理。

#### Principle and Mechanism

官方发布将 PDF/图像转换为带结构的文本表示；缺少足够独立评测与系统细节。

#### Trade-off and Evidence Boundary

专用解析器可压缩多模态输入成本，但 OCR 错误会成为下游不可见的数据质量故障。

#### Connection and Evolution

知识树位置：第 11、23、71 章。Record Only；未达 Books 门槛。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### EAGLE-3

- **Candidate / Week / Score:** EAGLE-3 / 2025-W10 / 26/30。
- **Source Family ID:** `eagle-mtp-specforge-specbundle`；后续与 MTP、SpecForge、SpecBundle 联读。
- **Source Type:** arXiv 作者论文 + official EAGLE repository + SGLang/vLLM integration experiments。
- **First-public Date / Revision History:** v1 2025-03-03；latest visible revision按 arXiv metadata核对；归档按
  v1。HTML生成时间不是first-public date。
- **Direct Primary Sources:** https://arxiv.org/abs/2503.01840；
  https://arxiv.org/html/2503.01840；https://github.com/SafeAILab/EAGLE。
- **Related Primary Sources:** EAGLE/EAGLE-2、HASS、Medusa及speculative sampling理论；SGLang/vLLM只证明
  对应实验版本的integration，不保证current framework behavior。
- **Access and Verification Status:** Verified；paper method/evaluation/appendix与official repo可访问。repository
  后续更新需与论文时点区分。
- **Full-read Coverage:** 已读metadata、Introduction/Related Work、speculative sampling math、EAGLE/EAGLE-2、
  inference pipeline、training-time test/mask、training data/optimizer、all model/task results、ablation、SGLang/
  vLLM experiments、implementation appendix，并核对official repository定位。
- **Original Problem:** speculative decoding收益由draft cost、acceptance length与target verification共同决定；
  EAGLE的top-layer feature regression在多步self-generated input下累积误差，增加draft data也趋于饱和。
- **Why the Previous Design Was Reasonable:** feature-level autoregression复用target top-layer representation和LM
  head，比独立small LM更贴近target distribution；EAGLE-2 dynamic tree按confidence分配draft nodes，避免静态树
  浪费，且strict acceptance保持target distribution。
- **Changed Constraint:** draft训练数据可扩大、reasoning model输出更长，但feature regression loss限制输入/
  representation；training用真实features而inference后续step只能看到draft output，产生train-test mismatch。
- **Mechanism:** 移除feature regression，draft直接预测tokens；记录target low/mid/high layer features并concat+FC
  融合为`g`。第一步使用target `g`+sampled-token embedding，后续缺少未verified target feature时用上一step
  draft output替代；training-time test把predicted outputs回灌并用特殊mask模拟多step inference；继承EAGLE-2
  context-aware dynamic tree与tree verification。
- **State Ownership:** target forward拥有verified KV/features与acceptance probabilities；draft model拥有unverified
  draft hidden/token tree；verification负责authoritative accept/reject与rollback到首个rejection。training pipeline
  拥有teacher-generated response与simulated-step masks。
- **Control Flow / Data Flow:** target prefill/previous verification→capture multi-layer features→draft step生成tree/
  probabilities→target tree-attention并行verify→按speculative-sampling rule sequential accept→rejection处resample并
  丢弃remaining branch→新verified prefix进入下一cycle。
- **Implementation Details:** draft core为one Transformer decoder layer；AdamW β=(0.9,0.95)、gradient clip 0.5、
  LR 5e-5；ShareGPT 68K+UltraChat 464K，reasoning model另用OpenThoughts-114K-math；target生成responses；
  EAGLE-3 tree depth 8、node count与EAGLE-2相同。
- **Evaluation Setup:** Vicuna-13B、Llama-3.1-8B-Instruct、Llama-3.3-70B-Instruct、DeepSeek-R1-Distill-
  Llama-8B；MT-bench/HumanEval/GSM8K/Alpaca/CNN-DM；同一draft weights跨tasks。metrics为actual speedup、
  average acceptance length与n-alpha；strict acceptance故不另评generation quality。
- **Baselines / Ablations / Sensitivity:** vanilla、standard speculative、PLD、Medusa、Lookahead、Hydra、HASS、
  EAGLE/EAGLE-2；ablation在Llama-3.1-8B上分离remove-feature-constraint与fused-features；data scaling；
  SGLang/vLLM batch sweep。缺不同tree budget、draft size和production arrival/SLO联合sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** SGLang v0.4.4单H100、Llama-3.1-8B、
  MT-Bench、chain length3、无tree，batch2～64；batch64 throughput 1.38×。vLLM section正文说RTX3090，table
  caption写A100，存在hardware inconsistency，不能作为确定hardware结论；precision、prompt/output length与SLO
  未完整披露。最高6.5×来自特定model/task、低batch latency，不可泛化。
- **What the Evidence Actually Proves:** strict verification保持sampling distribution；在作者contract中，移除
  feature constraint与多层fusion分别提高acceptance/speedup，且EAGLE-3在某些large batch仍有throughput收益。
  ablation支持两项mechanism贡献，但不隔离所有training-data effects。
- **What It Does Not Prove:** 不证明speculative decoding总能提高throughput，不证明6.5×适用于production，
  不证明multi-layer feature capture无memory/bandwidth机会成本，也不证明EAGLE-3必然优于MTP或future bundle。
- **Limitations / Threats to Validity:** author-trained drafts与benchmark prompts；缺真实arrival、prefix mix、tail
  latency、multi-GPU、quantization；reasoning dataset与task重合可能影响acceptance；vLLM hardware披露矛盾；
  paper无独立limitations section。
- **Trade-offs / New Failure Modes:** acceptance提高但增加draft checkpoint/training、target intermediate-feature
  taps、tree buffers、verification scheduling和per-model compatibility；large batch下spare compute减少，draft可能
  抢占target throughput；错误tree/buffer rollback会破坏lossless contract。
- **Where the Previous Design Still Applies:** memory/feature-tap成本敏感时small independent draft或EAGLE feature
  reuse仍可用；high batch/compute-bound workload可关闭spec decode；static/simple draft适合固定短pattern；vanilla
  decoding是low-complexity reference。
- **Evolution Relationship:** `Direct Evolution`：independent token draft→EAGLE feature draft→EAGLE-2 dynamic tree→
  EAGLE-3 direct-token+multi-layer fusion/training-time test；MTP/bundle是后续分支而非自动替代。
- **ROADMAP Node:** Ch44主 owner；Ch40/43提供decode/verification，Ch45 kernel，Ch47 runtime integration，
  Ch52 workload gate。
- **Target and Adjacent Chapters Read:** 已读 Ch40～47、Ch52，并最终审计 Ch44 演进段、公式、
  lossless boundary和batch crossover。
- **Existing Coverage:** Ch44已有EAGLE-3 provisional内容；Evidence Gate后需补/修hardware inconsistency、data与
  tree configuration、large-batch crossover，并与MTP/SpecForge/SpecBundle完成family-level去重。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch44，与 MTP/SpecForge/SpecBundle 组成 artifact lifecycle。
  最终落书。
- **Changed Files or Rejection Reason:** 已复核 `books/part-04-inference-system/44-speculative-decoding.md` 的 feature fusion、acceptance 与证据边界。
- **Open Questions:** intermediate-feature capture成本、draft/target资源隔离、multi-GPU verification、quantized
  compatibility、SLO-aware enablement，以及MTP-trained targets与external draft如何统一lifecycle。

### Mistral OCR

- **Candidate / Week / Score:** Mistral OCR / 2025-W10 / 19/30。
- **Source Family ID:** `mistral-ocr-document-ingestion`。
- **Source Type:** Mistral official release/lifecycle page + API documentation；无technical report、model card或code。
- **First-public Date / Revision History:** Mistral OCR 2503于2025-03-06发布；2505于2025-05-22更新。访问时
  2503发布页标记deprecated并被新OCR family替代；该后续lifecycle事实不改变2025 first-public归档。
- **Direct Primary Sources:** https://mistral.ai/news/mistral-ocr/；
  https://legal.mistral.ai/ai-governance/models/mistral-ocr；
  https://docs.mistral.ai/studio-api/document-processing/basic_ocr。
- **Related Primary Sources:** official cookbook/example只证明API input/output；发布页引用的internal benchmark
  不存在公开dataset/artifact，不能充当independent evidence。
- **Access and Verification Status:** Verified as `Version Fact / Mechanism Not Disclosed`；architecture、training
  data、weights、kernel、confidence calibration与2503 self-host contract均未公开。
- **Full-read Coverage:** 已读release、lifecycle、capabilities、input/output schema、images/tables/Markdown、pricing/
  deployment claims、internal benchmark tables、throughput claim、API docs及当前deprecation/version caveats。
- **Original Problem:** RAG/agent若直接把PDF当plain text会丢reading order、tables、equations、images与layout；
  ingestion error会在retrieval前形成不可见的信息损失。
- **Why the Previous Design Was Reasonable:** conventional OCR/text extraction便宜、可自托管、deterministic且
  易做page/word confidence；对born-digital/simple-layout文档，parser+OCR pipeline更可观察并可按阶段重试。
- **Changed Constraint:** multimodal/complex documents要求interleaved text-image、table/math/layout preservation，
  并希望输出Markdown/JSON直接进入RAG与tool workflow。
- **Mechanism:** 2503公开行为为image/PDF→ordered interleaved text/images/Markdown，支持document-as-prompt与
  structured output。model architecture、layout encoder、OCR decoder、training与post-processing全部
  `Not Disclosed`；current docs的新block/confidence fields也不能倒推2503已具备。
- **State Ownership:** API返回page-level content/images/metadata；调用方必须拥有source file、page/region identity、
  versioned parser result与downstream chunk lineage。vendor model内部state owner Not Disclosed。
- **Control Flow / Data Flow:** document upload/URL→vendor OCR API→page-ordered Markdown+extracted images→caller
  validation/chunk/index→RAG。若无source-coordinate/provenance保留，下游无法定位或修复OCR error。
- **Implementation Details:** 2503公开价格1000 pages/USD、batch约两倍pages per dollar、selective self-host与
  claimed 2000 pages/min single node，但node hardware、precision、document length/layout mix与tail latency未披露。
- **Evaluation Setup:** vendor internal text-only test set（publication papers+web PDFs）比较Google Document AI、
  Azure OCR、Gemini与GPT-4o；另有language fuzzy-match表。dataset、sample count、scoring script与confidence
  interval未公开，且competitors不抽images。
- **Baselines / Ablations / Sensitivity:** only vendor comparison tables；无architecture ablation、layout/category
  sensitivity、scan quality、page length、cost/error curve或independent replication。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model size/hardware/precision/input limits/
  concurrency/tail SLO Not Disclosed；2000 pages/min与price不是可复现实验contract。
- **What the Evidence Actually Proves:** 2025-03-06官方提供了一个将PDF/image转为structured/interleaved output
  的API，并公开其RAG定位和后续lifecycle；input/output boundary具有系统意义。
- **What It Does Not Prove:** 不证明模型内部document understanding机制、不证明vendor benchmark排序、
  不证明2000 pages/min适用于任意layout，也不证明OCR output语义正确或适合作为无验证ground truth。
- **Limitations / Threats to Validity:** internal/private benchmark与closed model；2503已deprecated，current docs混合
  later-version features；缺confidence/coordinate/provenance的2503 contract；敏感document经vendor API有privacy/
  residency风险。
- **Trade-offs / New Failure Modes:** 统一parser简化ingestion，却产生silent table/math/order errors、image-text
  misalignment、version drift、vendor lock-in、data exfiltration和re-index成本；结构化输出看似可信反而可能掩盖
  OCR uncertainty。
- **Where the Previous Design Still Applies:** born-digital/simple docs继续用native parser；高合规场景用on-prem/
  open OCR；关键表格/公式采用dual parser+human validation；可解释pipeline便于region-level recovery。
- **Evolution Relationship:** `Layering / Dependency`：document parser是RAG之前的数据质量层；不是RAG或
  multimodal reasoning本身的替代。
- **ROADMAP Node:** Ch11主 owner（data quality/lineage）；Ch72只做retrieval handoff，Ch23讨论multimodal input。
- **Target and Adjacent Chapters Read:** 已读Ch10～12、Ch23、Ch71～73；现有章节已覆盖input lineage、chunking
  与retrieval error propagation。
- **Existing Coverage:** 公开来源没有长期内部机制；Books已有“ingestion error precedes retrieval”原则，且2503
  已deprecated，新增vendor case会快速过时。
- **Integration Decision:** `Weekly Only — Version/Product Fact / Mechanism Not Disclosed`。
- **Changed Files or Rejection Reason:** 不改 Books；公开材料不足以支持模型机制或可复现性能结论。
  benchmark不可复现且长期principle已覆盖。
- **Open Questions:** versioned parser contract、region-level confidence/lineage、dual-parser reconciliation、
  sensitive-document residency与re-index migration cost。

### Visual-RFT

- **Identity / access:** 2025-W10，27/30，`visual-rft-verifiable-multimodal-rl`，arXiv research；v1 2025-03-03，后续 revision 不改变 owner。已读 https://arxiv.org/html/2503.01785 的方法、四类任务、reward、训练设置、结果与 appendix；代码为 related artifact。
- **Problem / mechanism:** SFT 在少样本视觉任务中同时模仿正确与偶然模式；Visual-RFT 用 Qwen2-VL rollout、GRPO，以及分类 accuracy 或 detection IoU/confidence/format 的可执行 reward 更新 policy。policy 拥有生成状态，task verifier 拥有 reward truth；数据流为 image/prompt→rollout→parser/verifier→group-relative advantage→update。
- **Evidence contract:** Qwen2-VL 2B/7B，在 fine-grained classification、few-shot/open-vocabulary detection 与 reasoning grounding 上比较 base/SFT/Visual-RFT；论文证明这些任务和 reward 下 RL 可提高样本效率，不证明任意视觉任务、任意 verifier 或自然语言 judge 都可泛化。训练硬件、线上并发与 SLO 未完整披露。
- **Boundary / owner:** verifier blind spot、format gaming、reward-task coupling 与 rollout cost 是新增 failure mode；高质量 SFT 在不可验证任务仍合理。`Direct Evolution`；owner `TRAIN-GRPO`（Ch33，legacy Ch29），handoff `MULTIMODAL-REPRESENTATION`（Ch23）；读相邻 Ch32/34，现有“verifier 决定可学边界”可 refine。`Books Pending — Refine Existing Argument`；问题是跨任务 reward calibration 与错误 verifier 的回滚。

### Cognitive Behaviors / Four Habits of STaRs

- **Identity / access:** 2025-W10，27/30，`cognitive-behaviors-rl-learnability`，arXiv + author code；v1 2025-03-03。已读 https://arxiv.org/html/2503.01307 的 controlled priming、PPO setup、OpenWebMath filtering、behavior analysis、controls 与 appendix。
- **Problem / mechanism:** 相同 RL recipe 下 Qwen2.5-3B 改善而 Llama3.2-3B plateau，说明“更多 RL compute”不是充分条件。论文以 verification、backtracking、subgoal、backward chaining 轨迹 priming 改变初始 policy，再由 PPO 在 Countdown reward 下选择性放大有用行为；policy owns trajectories，environment owns exact answer reward。
- **Evidence contract:** VERL/TinyZero、250 PPO steps、每 prompt 4 trajectories，并含空 CoT 与错误答案但保留行为的 controls；结果支持初始行为分布影响 RL learnability，且仅延长输出不够，不证明四种行为是普适必要条件，也不证明错误 CoT 在开放任务安全。硬件与完整 SLO Not Disclosed。
- **Boundary / owner:** priming 可引入 domain bias、错误 reasoning style 与 reward overfit；具备强初始 policy 时直接 RL 仍合理。`Principle Reuse`；owner `TRAIN-GRPO`（Ch33），handoff `TRAIN-PRETRAINING`（Ch28）；读 Ch28/32/34。`Books Pending — Refine Existing Argument`；待验证跨 domain、不同 optimizer 与 independent verifier 下是否成立。

### LLM Apprehension and Uncertainty

- **Identity / access:** 2025-W10，25/30，`llm-uncertainty-entropy-masj`，arXiv + code；v1 2025-03-03。已读 https://arxiv.org/html/2503.01688 的 MMLU-Pro pipeline、entropy/MASJ definition、four-model evaluation、domain split 与 limitations。
- **Problem / mechanism:** fluency 不等于知道；短 multiple-choice answer 可从 logits 计算 token entropy，而 MASJ 让 Mistral-Large-123B 显式判断题目教育层级与 reasoning steps。tested model owns logits，judge owns derived complexity label，evaluation pipeline owns correctness join。
- **Evidence contract:** Phi-4、Mistral-Small-24B-Instruct、Qwen 1.5B/72B on MMLU-Pro；低 reasoning 子集上 entropy 较能预测错误且随模型规模改善，MASJ 较弱。只证明该短答案 benchmark 的相关性，不证明生成式 atomic claims 的 calibrated probability，也不证明 self-report 是可靠 uncertainty。
- **Boundary / owner:** tokenization、answer length、dataset bias、judge dependence 与 distribution shift 会破坏 calibration；外部 evidence/verifier 仍优先。`Explanatory Analogy`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66，legacy Ch62），handoff `WORLDVIEW-KNOWLEDGE-TREE`；读 Ch65/67。`Books Pending — Refine Existing Argument`；问题是 selective-risk curve、ECE/Brier 与 abstention threshold。

### Liger

- **Identity / access:** 2025-W10，27/30，`liger-transformer-linearization`，arXiv research；v1 2025-03-03。已读 https://arxiv.org/html/2503.01496 的 conversion equations、hybrid attention、training、latency/memory、ablation 与 appendix。
- **Problem / mechanism:** softmax attention 保留全历史但 KV 随长度增长；既有 linearization 依赖新增 feature map/gate 且两阶段 brittle。Liger 复用 pretrained Q/K/V 构造 gate/recurrent state，以 GLA 与 window-64 SWA 混合；recurrent state owns compressed history，SWA owns local exact context，LoRA repairs distribution shift。
- **Evidence contract:** Mistral-7B、Llama3-8B，single A800 80GB，100k cleaned Alpaca samples/约 0.02B tokens、LoRA rank 8、2 epochs；与 SUPRA/Mamba-in-Llama 等比较并消融 gate/feature map/SWA。证明该 conversion recipe 可在所测模型回收多数质量并获得 constant-state branch，不证明长程 exact retrieval、all architectures 或 production latency parity。
- **Boundary / owner:** information compression、conversion training、hybrid merge weight 与 recurrent numerical drift 是新成本；短 context/高精度 retrieval 仍适合 softmax。`Alternative Branch`；owner `MODEL-SELF-ATTENTION`（Ch14），handoff `MODEL-LONG-CONTEXT`/`INFER-KV-CACHE`；读 Ch13/15/22/45。`Books Pending — Experimental`；待验证长 context recall 与 quantized recurrent state。

### Large-Scale Data Selection for Instruction Tuning

- **Identity / access:** 2025-W10，28/30，`rds-large-scale-instruction-selection`，arXiv + author artifact；v1 2025-03-03。已读 https://arxiv.org/html/2503.01807 的 methods、Tülu2/3 experiments、cost analysis、scaling、appendix 与 limitations。
- **Problem / mechanism:** selection score 在小 pool 上有效不代表能在百万级数据、multi-task target 下抵消 scoring cost。RDS/RDS+ 用 query set 与 candidate representation/gradient-like relevance score，按 task round-robin 平衡 selection；dataset pipeline owns scores/version，trainer consumes immutable selected manifest。
- **Evidence contract:** Tülu2/Tülu3 pools、Llama-family base、MMLU/GSM8K/BBH/TydiQA/Codex/SQuAD/AlpacaEval，与 random、quality/influence/retrieval baselines比较并计入 selection FLOPs；证明 RDS+ 在这两个 pool 的部分预算更有效，不证明跨数据域普适，且全池 model pass 成本线性增长。
- **Boundary / owner:** query leakage、task imbalance、selection-model bias、score staleness 与 provenance 丢失是 failure mode；cheap random/stratified sampling 在超大池仍合理。`Direct Evolution`；owner `TRAIN-DATA`（Ch27），handoff Ch28/66；读 Ch28。`Books Pending — Refine Existing Argument`；问题是动态数据、去污染与 selection amortization。

### SampleMix

- **Identity / access:** 2025-W10，27/30，`samplemix-pretraining-mixture`，arXiv research；v1 2025-03-03。已读 https://arxiv.org/html/2503.01506 的 quality/diversity scoring、optimization、token-budget experiments、analysis、appendix 与 limitations。
- **Problem / mechanism:** domain-level mixture 把域内样本视为同质并忽略跨域语义重叠。SampleMix 在 sample 级联合 quality 与 embedding-space diversity，求 sampling weight 并在目标 token budget 下 up/down-sample；data curator owns score/model/version，sampler owns realized mixture manifest。
- **Evidence contract:** 多个公开语料、不同 token budgets 与 downstream/perplexity evaluation，比较 domain-wise/random/quality/diversity branches；作者报告达到平均 baseline 所需 step 更少。证据只适用于所用 proxy、embedding 与规模，不证明 1.9x 是通用收益；hardware、full training SLO Not Disclosed。
- **Boundary / owner:** proxy bias、embedding collapse、重复 upsampling、尾部知识丢失与 score compute 是代价；稳定域和低预算 pipeline 仍可用 domain weights。`Direct Evolution`；owner `TRAIN-DATA`（Ch27），读 Ch28；`Books Pending — Refine Existing Argument`。待验证 mixture drift、dedup interaction 与 per-sample provenance。

### RSQ

- **Identity / access:** 2025-W10，27/30，`rsq-token-important-ptq`，arXiv research；v1 2025-03-03。已读 https://arxiv.org/html/2503.01820 的 GPTQ/QuaRot background、rotate-scale-quantize、importance variants、long-context evaluation、ablations 与 appendix。
- **Problem / mechanism:** layer-wise PTQ 均匀最小化所有 calibration token reconstruction error，可能让大量低价值 token 主导 Hessian。RSQ 先 orthogonal rotation 抑制 weight outlier，再按 First/Last、frequency、activation、similarity 或 attention contribution 加权 token，最后在 GPTQ/LDLQ error compensation 中量化。
- **Evidence contract:** Llama3-8B-Instruct 等，主要 3-bit，WikiText calibration 256×4096 或等 token-budget variants，并评估 perplexity、10 tasks 与 long-context suites，含 bit/data/importance ablation。证明所测 PTQ 中 token-weighted calibration 优于均匀目标，不证明 attention score 等同语义重要性或所有 model/bit/kernel 都受益。
- **Boundary / owner:** importance estimator cost、calibration shift、position bias 与 kernel support 是新增约束；4-bit/宽松内存下简单 PTQ 仍合理。`Direct Evolution`；owner `INFER-TENSORRT-LLM`（Ch49，legacy Ch45），handoff Ch54/66；读 Ch48/50。`Books Pending — Refine Existing Argument`；待验证 end-to-end throughput 与 serving accuracy contract。

### MultiAgentBench

- **Identity / access:** 2025-W10，26/30，`multiagentbench-marble`，arXiv + MARBLE code；v1 2025-03-03。已读 https://arxiv.org/html/2503.01935 的 six environments、star/tree/chain/graph protocols、metrics、human check、ablations、appendix 与 limitations。
- **Problem / mechanism:** final task score 隐藏 communication/coordination failure。MARBLE 用 explicit agent graph、planner/actor roles、event/environment state、milestone KPI 与 LLM/rule evaluators比较 topology；coordination engine owns routing，environment owns executable state，memory/log owns trace。
- **Evidence contract:** research、Minecraft、database、coding、bargaining、Werewolf，多个 closed/open models，消融 iteration 与 agent count；结果表明 topology 优势依场景而变，不能推出 graph 普遍最佳，且 milestone/coordination judge 含 LLM evaluator bias。
- **Boundary / owner:** communication tax、shared-state inconsistency、judge circularity 与 error amplification；single-agent headroom 大或任务不可分时不应扩 agent。`Principle Reuse`；owner `AGENT-MULTI-AGENT`（Ch82，legacy Ch78），handoff Ch81/66；读 Ch81/83。`Books Pending — Refine Existing Argument`；问题是 topology selection、cost-normalized gain 与 deterministic replay。

### MPO / Meta Plan Optimization

- **Identity / access:** 2025-W10，26/30，`mpo-meta-plan-optimization`，arXiv research；v1 2025-03-04。已读 https://arxiv.org/html/2503.02682 的 meta-plan representation、environment exploration、training、SciWorld/ALFWorld/WebShop、ablation 与 limitations。
- **Problem / mechanism:** on-the-fly implicit planning易 hallucinate，per-agent trajectory tuning又难迁移。MPO 训练独立 meta planner输出高层 guidance，由 frozen/varied executor落地，environment return 反向优化 plan；planner owns intent skeleton，executor owns action state，environment owns success evidence。
- **Evidence contract:** GPT-4o、Qwen2.5-7B-Instruct 等在三个 embodied/web environments，对 no-plan、SFT、GPT planner、RFT消融；证明所测 meta plan 可跨 executor/held-out scenario 改善，不证明开放世界长期计划或 safety。hardware、token cost/latency SLO Not Disclosed。
- **Boundary / owner:** plan-execution drift、stale guidance、extra call cost 与 attribution ambiguity；短任务 direct policy 仍合理。`Layering / Dependency`；owner `AGENT-PLANNING`（Ch79），handoff Ch81；读 Ch78/80。`Books Pending — Refine Existing Argument`；待验证 replanning trigger 与 rollback semantics。

### Mask-DPO

- **Identity / access:** 2025-W10，27/30，`mask-dpo-factuality`，arXiv research；v1 2025-03-04。已读 https://arxiv.org/html/2503.02846 的 sentence annotation、masked objective、Llama3.1 setup、FactScore/ANAH evaluation、ablation、appendix 与 limitations。
- **Problem / mechanism:** response-level DPO 会奖励 preferred response 中仍错误的句子，也会惩罚 rejected response 中正确的句子。Mask-DPO 由 ANAH-v2 逐句标注 factuality，在 token loss 中 mask 掉这两类 ambiguous span；annotator owns label，dataset owns aligned mask，policy consumes preference loss。
- **Evidence contract:** Llama3.1-8B-Instruct、ANAH-v2 reward/annotation，比较 vanilla DPO 与 mask ablation，并在 ANAH/FactScore 测试；证明该 annotator/domain 下 fine-grained credit assignment 改善，不证明事实被独立核实。作者明确提示同一模型参与数据构造与 review，存在 reward hacking/circular evaluation；hardware/SLO Not Disclosed。
- **Boundary / owner:** annotation error、span alignment、mask 稀疏化与 reward-model bias；整段 preference 干净时 vanilla DPO 更简单。`Direct Evolution`；owner `TRAIN-DPO`（Ch34，legacy Ch30），handoff Ch66；读 Ch33/35。`Books Pending — Experimental`；待验证 independent evidence verifier 与 calibrated abstention。

### PipeOffload

- **Identity / access:** 2025-W10，28/30，`pipeoffload-activation-lifetime`，arXiv + code；v1 2025-03-03。已读 https://arxiv.org/html/2503.01328 的 PP memory model、selective offload、implementation、hardware evaluation、recompute/offload ablation 与 appendix。
- **Problem / mechanism:** 增加 PP stage 减少每卡 layers，却需要更多 in-flight microbatches 填 bubble，activation memory 不随 stage 数下降。PipeOffload 利用 forward→backward 的长 lifetime 把 chosen activations异步搬到 host，再 prefetch；scheduler owns lifetime/dependency，GPU allocator owns resident tensors，host buffer owns offloaded state。
- **Evidence contract:** 多种 model/stage/microbatch 与 GPU/PCIe configuration，比较 PP/TP、selective/full offload、recompute；作者显示不少配置可隐藏 transfer，且 LayerNorm/GeLU/dropout recompute 可再降约 40% activation、带约 1–2% slowdown。证据绑定其 interconnect/schedule，不证明所有 topology 或 failure recovery。
- **Boundary / owner:** pinned-host pressure、PCIe contention、prefetch miss、OOM migration 与 checkpoint interaction；短 lifetime、高带宽不足时 recompute/更少 microbatch 仍合理。`Direct Evolution`；owner `TRAIN-PIPELINE-PARALLEL`（Ch38，legacy Ch34），handoff Ch36/39；读 Ch37/39。`Books Pending — Refine Existing Argument`；待验证 NUMA 与 fault semantics。

### IVR / Evolutionary Guided Decoding

- **Identity / access:** 2025-W10，26/30，`ivr-value-guided-decoding`，arXiv research；v1 2025-03-04，后续 revision 仅作核验。已读 https://arxiv.org/html/2503.02368 的 value exploration、iterative refinement、blockwise decoding、three task families、ablation、appendix 与 limitations。
- **Problem / mechanism:** fixed reward/value model 在 policy 改变后产生 distribution shift，token-wise guided decoding又有高 latency。IVR 交替采样 policy trajectories、收集偏好/价值数据、迭代更新 value function，再以 blockwise beam search引导 generation；policy owns candidate state，value model owns non-authoritative score，decoder owns commit。
- **Evidence contract:** summarization、multi-turn dialogue、instruction following，比较 ARGS/VAS/FUDGE 与 no-iteration ablation，并分析 trajectories/iterations/transfer；证明其任务内 iterative value refresh 可提高作者 judge/reward，不证明 judge 与人类偏好一致，也不消除 base-policy dependence。training/inference cost 随 iteration/branch 增长。
- **Boundary / owner:** reward hacking、value staleness、beam collapse 与 extra decode cost；stable constrained task 可用 fixed verifier。`Direct Evolution`；owner `MODEL-SAMPLING`（Ch20），handoff `INFER-DECODE`/Ch66；读 Ch19/42/44。`Books Pending — Experimental`；待验证 exactness、online latency 与 independent judge。

### AppAgentX

- **Identity / access:** 2025-W10，25/30，`appagentx-derived-gui-workflow`，arXiv research；v1 2025-03-04。已读 https://arxiv.org/html/2503.02268 的 visual-only pipeline、history chain、operation abstraction、A3 evaluation、perceptor/action ablation 与 cases。
- **Problem / mechanism:** GUI agent 每次从像素重新规划，重复动作浪费 tokens/latency。AppAgentX 记录 execution chain，从成功历史抽象 higher-level action/knowledge，再在后续 task 检索复用；environment owns screen truth，agent memory owns derived procedure，executor validates each action outcome。
- **Evidence contract:** GPT-4o default、Android Agent Arena 201 tasks/20 apps，比较 baseline、不同 screen parser 与 basic/full action space；结果支持 richer action abstraction 降低所测时间但不证明跨 OS、UI drift 或安全敏感操作。backend/API-free 只是实验约束，failure recovery/并发 Not Disclosed。
- **Boundary / owner:** stale procedure、visual aliasing、unsafe macro 与 provenance/supersession；低频或高风险任务仍应逐步规划。`Direct Evolution`；owner `AGENT-MEMORY`（Ch77），handoff Ch78/81；读 Ch76/78。`Books Pending — Refine Existing Argument`；待验证 invalidation、approval 与 rollback。

### HoT / Highlighted Chain of Thought

- **Identity / access:** 2025-W10，24/30，`hot-grounded-highlight-ux`，arXiv + datasets；v1 2025-03-03。已读 https://arxiv.org/html/2503.02003 的 XML grounding prompt、17 tasks、human study、tag/repetition ablations、appendices 与 limitations。
- **Problem / mechanism:** 混合事实/非事实的回答让人难以定位输入证据。HoT 先重写问题并标记 facts，再在 answer 中回链 tag；model owns citation-like spans，UI exposes them，human remains final verifier。它没有引入外部 evidence retrieval，也没有改变 world-truth ownership。
- **Evidence contract:** multiple LLMs/17 reasoning and comprehension tasks、time-limited human verification、question-repeat/tag ablation；显示 highlights 可提高正确答案的识别效率，但错误答案也更易造成 over-trust。故证据反驳“可视化 grounding 自动提高可靠性”，不证明 hallucination 被消除。
- **Boundary / owner:** fabricated tag、selective omission、attention capture 与 automation bias；无证据时普通回答+明确 abstention 更诚实。`Principle Reuse`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `AGENT-CONTEXT`；读 Ch65/67。`Books Pending — Refine Existing Argument`；待验证 evidence authenticity indicator 与 UI risk calibration。

### Process-based Self-Rewarding Language Models

- **Identity / access:** 2025-W10，27/30，`process-self-rewarding`，arXiv research；v1 2025-03-05。已读 https://arxiv.org/html/2503.03746 的 step-wise judge/preference loop、math/instruction experiments、human agreement、appendix 与 limitations。
- **Problem / mechanism:** outcome/self-reward 对长数学轨迹 credit assignment 粗糙，且同一模型迭代可能退化。方法让 policy 逐步生成并逐步 judge，相邻或候选 step 建 preference，再做 step-wise preference optimization；policy/judge 可同源，trajectory store owns process labels。
- **Evidence contract:** mathematical benchmarks与 instruction-following，比较 outcome self-reward、process variant与 external baselines，以 exact accuracy/LLM judge评价；支持细粒度 feedback 在所测 math loop 更稳定，不证明 self-judge 客观，也不隔离 shared-model bias。hardware、precision、online SLO Not Disclosed。
- **Boundary / owner:** judge-policy collusion、错误早期 step 被放大、label cost 与 long-trajectory storage；有可靠 executable outcome 时直接 verifier 更强。`Direct Evolution`；owner `TRAIN-DPO`（Ch34），handoff Ch33/66/80；读 Ch33/35。`Books Pending — Refine Existing Argument`；待验证 independent process verifier 与 rollback。

### KodCode

- **Identity / access:** 2025-W10，26/30，`kodcode-executable-synthetic-data`，arXiv + dataset/code；v1 2025-03-04。已读 https://arxiv.org/html/2503.02951 的 source transformations、question/solution/test generation、self-verification、training、data-selection ablation、appendix 与 limitations。
- **Problem / mechanism:** synthetic coding data 可扩规模，但题目单一、solution 不可执行或 tests 不充分。KodCode 生成 question-solution-test triplet，对困难题增加 attempts，用 execution/self-verification过滤；generator owns proposal，sandbox/test suite owns acceptance evidence，dataset manifest preserves provenance/licence branch。
- **Evidence contract:** multiple subsets/models，fine-tune Qwen2.5-Coder variants并在 HumanEval/MBPP/LiveCodeBench 等比较与 10k data ablation；支持可执行过滤提高所测 code post-training，仍在 LiveCodeBench-Hard 弱，且 unit tests 不证明完整 semantic correctness。hardware/SLO Not Disclosed。
- **Boundary / owner:** weak tests、sandbox escape、generator contamination、license 与 false acceptance；人类 curated hard set 仍必要。`Direct Evolution`；owner `TRAIN-DATA`（Ch27），handoff Ch29/66；读 Ch28。`Books Pending — Refine Existing Argument`；待验证 mutation testing、coverage 与 provenance delete。

### Gen3C

- **Identity / access:** 2025-W10，25/30，`gen3c-world-consistent-video`，arXiv research；v1 2025-03-05。已读 https://arxiv.org/html/2503.03751 的 3D cache/conditioning、autoregressive generation、applications、optimization/inference appendix、fusion/depth ablations 与 limitations。
- **Problem / mechanism:** pure video prior 可生成逼真帧，却在 camera 回看时忘记场景。Gen3C 从输入估计 depth/point cloud，沿目标 camera trajectory render 3D-conditioned context，再由 video diffusion补全；3D cache owns approximate scene state，camera path owns control，generator owns appearance proposal。
- **Evidence contract:** RE10K、driving与 dynamic novel-view tasks，PSNR/SSIM/LPIPS和 qualitative comparison，消融 explicit vs learned fusion及 noisy depth；证明 approximate geometry improves tested view consistency/control，不等同 causal world model，dynamic object motion仍依赖预生成 video。hardware/real-time SLO Not Disclosed。
- **Boundary / owner:** depth error、occlusion holes、state drift 与 static-geometry bias；单次 free-form generation 不需 persistent state。`Layering / Dependency`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `MULTIMODAL-WORLD-MODELS`（Ch25）；读 Ch23/25。`Books Pending — Experimental`；待验证 action-conditioned transition 与 state correction。

### ToolRet / Retrieval Models Aren't Tool-Savvy

- **Identity / access:** 2025-W10，26/30，`toolret-tool-retrieval`，arXiv + dataset/code；v1 2025-03-03。已读 https://arxiv.org/html/2503.01763 的 43k-tool corpus/7.6k tasks、heterogeneous schema、metrics、six model families、instruction-tuning ablation 与 appendix。
- **Problem / mechanism:** tool-use benchmark 常预先给小候选集，掩盖大 registry 的 retrieval failure。ToolRet 把 API descriptions、code functions 与 custom apps 建 corpus，以 query/instruction retriever召回后再交给 LLM；registry owns tool identity/version，retriever owns candidate set，executor owns authoritative invocation result。
- **Evidence contract:** dense/sparse/LLM retrieval baselines，以 recall/completeness@k 等评估；instruction+query tuning优于 query-only，但强通用 retriever在 tool corpus仍低。证明 tool selection是独立 bottleneck，不证明 recall 会等比例转为 task success，也未覆盖 permission/version drift。
- **Boundary / owner:** schema ambiguity、stale embedding、top-k context tax 与 unsafe candidate exposure；小稳定 toolset可直接 enumerate。`Layering / Dependency`；owner `AGENT-TOOL-CALLING`（Ch78），handoff Ch75/83；读 Ch77/79。`Books Pending — Refine Existing Argument`；待验证 registry invalidation、authorization-aware retrieval 与 end-to-end success。

### START

- **Identity / access:** 2025-W10，28/30，`start-tool-integrated-reasoner`，arXiv research；v1 2025-03-06。已读 https://arxiv.org/html/2503.04625 的 Hint-infer、Hint-RFT、trajectory filtering/editing、QwQ training、benchmarks、implementation 与 limitations。
- **Problem / mechanism:** long CoT 遇到计算/模拟时仅靠 parametric reasoning 易 hallucinate。START 在 inference 插入 tool-use hint诱发 code execution，再对带 tool call 的 trajectories评分、过滤、修正并 RFT 到 QwQ-32B-Preview；policy owns reasoning，sandbox owns computation truth，filter owns training admission。
- **Evidence contract:** GPQA、AMC/AIME、LiveCodeBench，对 base与 R1-distill/o1-preview 等比较；证明 code-tool trajectories在所测可执行任务提升，不证明网页/现实工具、unsafe code 或 general factuality。作者数字绑定 model、prompt与 execution harness，hardware/concurrency/SLO Not Disclosed。
- **Boundary / owner:** sandbox security、tool error、hint dependence、trajectory contamination 与 extra latency；简单问题 internal reasoning仍便宜。`Direct Evolution`；owner `AGENT-TOOL-CALLING`（Ch78），handoff Ch79/81/72；读 Ch77/79。`Books Pending — Refine Existing Argument`；待验证 permission、timeout、idempotency 与 provenance。

### STORM

- **Identity / access:** 2025-W10，27/30，`storm-video-token-compression`，arXiv research；v1 2025-03-06。已读 https://arxiv.org/html/2503.04130 的 temporal Mamba projector、spatial pooling、training/evaluation、token/latency ablations、streaming appendix 与 architecture details。
- **Problem / mechanism:** independent frame tokens既缺显式 temporal state又迅速耗尽 context。STORM 在 image encoder 与 LLM 间用 Mamba temporal module融合跨帧信息，再做时空 token reduction；encoder owns frame features，temporal state owns compressed history，LLM consumes bounded tokens。
- **Evidence contract:** multiple video QA/long-video benchmarks、32-frame training与更长 test、token budget/architecture/compression ablations；证明所测 token budget 下 temporal compression优于 naïve pooling且可单 GPU运行，不证明所有事件细节被保留或 streaming state可无损 rollback。hardware latency仅代表披露设置。
- **Boundary / owner:** compression loss、temporal aliasing、state reset与 event-boundary sensitivity；短视频/细粒度取证仍适合更多原始 tokens。`Direct Evolution`；owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `MODEL-LONG-CONTEXT`/Ch45；读 Ch22/24。`Books Pending — Refine Existing Argument`；待验证 adaptive token budget与 provenance。

### Audio Flamingo 2

- **Identity / access:** 2025-W10，26/30，`audio-flamingo-2-long-audio`，arXiv + NVIDIA project artifact；v1 2025-03-06。已读 https://arxiv.org/html/2503.03983 的 CLAP/audio encoder、cross-attention curriculum、AudioSkills/LongAudio data、20+ benchmarks、ablations、computational appendix 与 limitations。
- **Problem / mechanism:** speech-centric or short-clip models缺少长音频事件、音乐与非语音 reasoning。AF2 以 custom CLAP/encoder提取 audio representation，通过 periodic cross-attention接入 LLM，并以 multi-stage curriculum从短 skill扩展长 audio；audio encoder owns sensory tokens，LLM owns response state，dataset/evaluator owns task evidence。
- **Evidence contract:** public audio datasets、synthetic QA与 LongAudioBench，比较多种 audio-language models并消融 RoPE、transformation layers、cross-attention frequency与 LLM size；支持该组合在所测 benchmark增强，不证明 real-time agent hearing、所有语言/噪声或 proprietary model superiority。CLAP retrieval-based metric有已声明限制。
- **Boundary / owner:** long-audio token/latency、synthetic-label bias、temporal localization与 benchmark leakage；ASR→text pipeline在 speech-only tasks仍更可解释。`Layering / Dependency`；owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch24/66；读 Ch22/24。`Books Pending — Refine Existing Argument`；待验证 streaming state、timestamp identity与 correction。

### ONNX Runtime v1.21.0

- **Identity / access:** 2025-W10，26/30，`onnxruntime-1.21.0`；official GitHub release/tag v1.21.0、commit `e0b66ca`，released 2025-03-08。已读release notes的GenAI chat/decoder/MultiLoRA、migration、TensorRT/CUDA/QNN/OpenVINO/CoreML execution-provider、tokenizer/build/runtime changes及linked official migration references。
- **Problem / mechanism:**通用graph runtime若只执行单次tensor graph，用户仍需自行拼接tokenizer、decoder loop、KV/pipeline与provider-specific op assignment。v1.21.0加入chat mode、decoder model pipelines与Java MultiLoRA；EP层允许TensorRT 10.8、op exclusion/default DDS assignment、CUDA DLL preload、QNN shared memory、OpenVINO weight sharing等。model graph/tokenizer/pipeline state属于GenAI layer，EP partition/provider version属于execution-plan identity。
- **Evidence contract:**release明确chat mode存在breaking API migration，Phi long-prompt/top-k output bugs被修复；没有统一model、hardware、precision、length、batch/concurrency、TTFT/TPOT或SLO benchmark。各EP支持只证明compatibility surface，不证明同图在TensorRT/QNN/OpenVINO/CoreML有等价numerics/latency；后续patch行为不能倒灌。
- **Boundary / owner:**unified runtime减少application glue，却把tokenizer schema、provider partition、fallback与DLL/SDK matrix纳入artifact；EP unsupported op会切回其他provider并产生silent performance cliffs。framework-native runtime在dynamic/custom kernels或LLM-specialized scheduling下仍合理。`Direct Evolution`；owner `INFER-EXECUTION`（Ch49），handoff `PLATFORM-MODEL-REGISTRY`（Ch59）与 `PLATFORM-PRODUCTION`（Ch73）；读Ch48/50。`Books Pending — Refine Existing Argument`。

### Low-score and Version-Fact Verification

- **JAX 0.5.2 / 17/30:** official changelog 2025-03-04；patch of 0.5.1 fixing TPU metrics/`tpu-info`。身份与日期 verified；没有新的 execution/communication mechanism，`Weekly Only — Patch Release`，owner handoff `TRAIN-DISTRIBUTED-TRAINING`，不触发 Books。
- **LLMVoX / 19/30:** arXiv 2503.04724，v1 2025-03-06；streaming TTS adapter/domain model。公开实验不足以建立跨模型通用 audio-runtime contract，`Weekly Only — Domain Model`。
- **EgoLife / 19/30:** arXiv 2503.03803，v1 2025-03-05；egocentric assistant dataset/system case。应用组合价值高但无独立稳定 runtime mechanism，`Weekly Only — Application Case`。
- **LINGOLY-TOO / 18/30:** arXiv 2503.02972，v1 2025-03-04；用 linguistic templatisation/orthographic obfuscation分离 memorization/reasoning。属于窄评测案例，`Weekly Only — Evaluation Case`。
- **IFIR / 19/30:** arXiv 2503.04644，v1 2025-03-06；expert-domain IR instruction-following benchmark。没有新的 retrieval ownership/control flow，`Weekly Only — Domain Benchmark`。
- **LLM as a Broken Telephone / 18/30:** arXiv 2502.20258，v1 2025-02-27，实际 owner 为 W09；W10 仅 discovery spillback，不重复计分。观察 iterative generation distortion，但不形成 W10 event。

### Unified Reward Model

- **Identity / access:** 2025-W10，27/30，`unifiedreward-multimodal-preference`，arXiv+code/data；v1 2025-03-07。已读 https://arxiv.org/html/2503.05236v1 的236K preference mixture、pair/point objective、data filtering、DPO branches、reward/DPO evaluations、appendix与limitations。
- **Problem / mechanism:** task-specific reward models不能共享image/video、understanding/generation evidence。UnifiedReward以LLaVA-OneVision-7B联合学习point score与pair ranking，再对N=10 outputs先pair ranking、后point sifting构造chosen/rejected，分别训练VLM/Diffusion DPO；human dataset ownsinitial preference，reward model只拥有derived score。
- **Evidence contract:** VLRewardBench、ShareGPTVideo、GenAI/VideoGen RewardBench及多个understanding/generation benchmarks；DPO涉及LLaVA、SDXL-Turbo、T2V-Turbo。证明作者mixture内multi-task transfer，不证明单一reward跨域校准或self-generated preference无bias；硬件、online SLO未披露。
- **Boundary / owner:** reward circularity、task imbalance、score scale不统一与judge blind spot；专用verifier在高风险任务仍合理。`Principle Reuse`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoffCh23/24/34；读Ch65/67。`Books Pending — Refine Existing Argument`。

### Sketch-of-Thought

- **Identity / access:** 2025-W10，25/30，`sketch-of-thought`，arXiv+code；v1 2025-03-07。已读 https://arxiv.org/html/2503.05179v1 的Conceptual Chaining、Chunked Symbolism、Expert Lexicons、router training、15-dataset multilingual/multimodal evaluation、self-consistency与limitations。
- **Problem / mechanism:** uniform verbose CoT对简单/结构化任务浪费tokens。SoT用lightweight router按task选择三种compressed reasoning language，model生成sketch再answer；router ownsformat proposal，answer evaluator owns correctness。
- **Evidence contract:** Qwen2.5 family与15 reasoning datasets，作者报告平均76% token reduction且accuracy大致保持；数字绑定prompt/model/task，不证明hidden compute减少、free-form auditability或OOD router可靠。
- **Boundary / owner:**压缩会丢verification steps，router misclassification新增failure；复杂证明仍需完整trace。`Alternative Branch`；owner `AGENT-PROMPT`（Ch74），handoffCh20/66；读Ch75。`Books Pending — Refine Existing Argument`。

### Forgetting Transformer / FoX

- **Identity / access:** 2025-W10，28/30，`forgetting-transformer`，arXiv+code；v1 2025-03-03。已读 https://arxiv.org/html/2503.02130v1 的forget-gate derivation、FoX/Pro block、training/throughput、needle tests、short/long context、FlashAttention appendix、scale/seed sensitivity。
- **Problem / mechanism:** softmax attention保留任意past token却没有data-dependent forgetting。FoX在unnormalized attention score上累积input-dependent forget factor，再softmax；state仍是explicit KV而非fixed recurrent state，FlashAttention-compatible kernel实现scan/score融合。
- **Evidence contract:**125M～760M等训练规模、2.7B～16B tokens、language modeling/length extrapolation/needle/short tasks，与Transformer、Mamba2、HGRN2、DeltaNet及sliding-window比较。证明所测scale的selective decay价值，不证明frontier long-context、serving KV减少或all kernels parity。
- **Boundary / owner:**gate saturation、过早遗忘、额外scan/state与初始化敏感；exact retrieval仍适合plain attention。`Alternative Branch`；owner `MODEL-SELF-ATTENTION`（Ch14），handoffCh22/45/49；读Ch13/15。`Books Pending — Experimental`。

### R1-Searcher

- **Identity / access:** 2025-W10，27/30，`r1-searcher-rl`，arXiv+code；v1 2025-03-08。已读 https://arxiv.org/html/2503.05592v1 的two-stage outcome RL、search environment/action format、reward、multi-hop QA evaluation、analysis与appendix。
- **Problem / mechanism:**prompted iterative RAG依赖复杂prompt/strong closed model，SFT容易memorize paths。R1-Searcher先训练正确answer，再开放search action与outcome reward，使policy学习何时/如何检索；retriever ownsdocuments，policy ownsquery/trajectory，exact answer checker ownsreward。
- **Evidence contract:**small open LLM与four multi-hop QA benchmarks，对RAG/prompt/tool baselines；证明其retriever/corpus/answer setting的RL search，不证明source truth、citation entailment或web安全。process quality没有独立reward。
- **Boundary / owner:**outcome reward容忍无效/虚假search、query drift与retrieval cost；simple QA可one-shot RAG。`Direct Evolution`；owner `AGENT-RAG`（Ch76），handoffCh33/78；读Ch75/77。`Books Pending — Refine Existing Argument`。

### SafeArena

- **Identity / access:** 2025-W10，27/30，`safearena-web-agent-misuse`，arXiv+environment；v1 2025-03-06。已读 https://arxiv.org/html/2503.04957v1 的250 safe/250 harmful tasks、four sites、human curation/verification、risk metrics、models/attacks、human/ARIA evaluation、appendix与limitations；不复制危险任务细节。
- **Problem / mechanism:**chat refusal score不能衡量Agent在真实action space的deliberate misuse。SafeArena在可控websites执行paired safe/harmful tasks，以task completion与normalized safety、human/judge共同评价；environment ownsobservable side effects，agent output文本不是唯一证据。
- **Evidence contract:**多种LLM agents、四类websites与task-decomposition/priming tests；证明当时agents经常完成有害任务且chat alignment transfer弱，不证明开放互联网attack rate。500 tasks、site simulation与judge/human sample限制外推。
- **Boundary / owner:**benchmark本身含dual-use内容、evaluator error与environment coverage gap；deployment需permission/approval/policy gate。`Layering / Dependency`；owner `PLATFORM-SECURITY`（Ch72），handoffCh66/78/84；读Ch71/73。`Books Pending — Refine Existing Argument`。

### Learning from Failures / Multi-Attempt RL

- **Identity / access:** 2025-W10，25/30，`multi-attempt-rl-failure-feedback`，arXiv research；v1 2025-03-06。已读 https://arxiv.org/html/2503.04808v1 的multi-attempt MDP/objective、wrong-answer feedback、RL setup、math evaluation与analysis；公开正文较短，hardware/完整limitations为Not Disclosed。
- **Problem / mechanism:**single-attempt outcome RL只区分终局成败，失败轨迹没有修正机会。multi-attempt environment在错误后返回typed failure feedback并保留dialogue state，policy可再次回答；environment ownsanswer truth，trajectory ownsprior failure。
- **Evidence contract:**1.5B model/math benchmark，作者报告two-attempt evaluation 45.6→52.5而single-turn-trained 42.3→43.2；只证明该task/reward规模，不证明内在self-verification或开放任务可泛化。
- **Boundary / owner:**feedback leakage、重复guess、extra rollout与state contamination；cost-sensitive exact task仍可single attempt。`Direct Evolution`；owner `TRAIN-GRPO`（Ch33），handoffCh80/81；读Ch32/34。`Books Pending — Refine Existing Argument`。

### Linear-MoE

- **Identity / access:** 2025-W10，28/30，`linear-moe-system`，arXiv+code；v1 2025-03-08。已读 https://arxiv.org/html/2503.05447v1 的unified LSM model layer、MoE/hybrid architecture、Linear-MoE sequence parallelism、training subsystem、A0.3B-2B/A1B-7B evaluation、implementation与appendix。
- **Problem / mechanism:**MoE降低activated FFN compute却保留quadratic attention；LSM降低sequence complexity却引入state/parallel scan。Linear-MoE组合linear attention/SSM/linear-RNN与sparse experts，并设计适配recurrent state的sequence parallel/parallel training；hybrid layers保留softmax retrieval branch。
- **Evidence contract:**两组小至7B series及training efficiency/benchmark comparison，证明作者system可训练多种LSM-MoE，不证明frontier quality、constant-memory exact retrieval或production fault tolerance；vendor-style“production-level”是作者主张。
- **Boundary / owner:**router imbalance、expert all-to-all、recurrent state partition与hybrid scheduling耦合；短context dense/standard MoE仍成熟。`Layering / Dependency`；owner `MODEL-MOE`（Ch21），handoffCh14/36/37/40；读Ch20/22。`Books Pending — Experimental`。

### WildIFEval

- **Identity / access:** 2025-W10，25/30，`wildifeval-real-constraint-following`，arXiv+dataset/code；v1 2025-03-09。已读 https://arxiv.org/html/2503.06573v1 的LMSYS filtering、constraint extraction/taxonomy、human verification、14-model evaluation、judge validation、correlation与appendix。
- **Problem / mechanism:** synthetic/rule benchmarks不能代表real-user multi-constraint组合。WildIFEval从LMSYS-Chat-1M筛出11,813 tasks，由Llama3.1-70B分解29,874 constraints，按8类逐constraint judge并聚合fraction fulfilled；dataset ownstask/constraint identity，judge score不是ground truth。
- **Evidence contract:**14 models、0.5B～671B、zero-shot；best约0.65，constraint数增加性能下降。human check仅20 responses、judge agreement75%，且length constraint可能应使用deterministic counter；因此不能把LLM judge score外推为通用instruction reliability。
- **Boundary / owner:**decomposition/judge同源bias、soft constraints不可执行、real-user privacy/filtering与macro/micro weighting；rule verifier对format/length仍更强。`Direct Evolution`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoffCh74/84；读Ch65/67。`Books Pending — Refine Existing Argument`。

### Shifting Long-Context Research from Input to Output

- **Identity / access:** 2025-W10，23/30，`long-output-research-survey`，arXiv survey/position paper；v1 2025-03-06。已读 https://arxiv.org/html/2503.04723v1 的demand/paper census、data/benchmark/model survey、Broken-Mirror test、training/inference challenges、alternative views与appendix。
- **Problem / mechanism:**long-context常只报告input capacity，忽略autoregressive output的sequential latency、coherence与evaluation。论文把需求拆为long-output data、length+quality benchmark、model/runtime；100K user-query length demand由Llama3.3-70B预测，2024 conference census为position evidence而非causal experiment。
- **Evidence contract:**survey列出LongWriter/Suri/LongGen/HelloBench等，并展示3K-word logical inconsistency常逃过LLM judge；“4K+ output需求”“102:2 paper ratio”“long output更慢”绑定其sampling/classification与API measurements，不证明所有domains或architectures。
- **Boundary / owner:**synthetic data mismatch、long-form judge blind spot、decode cost与chained-generation error accumulation；短/segmented output仍可通过workflow解决。`Principle Reuse`；owner `MODEL-LONG-CONTEXT`（Ch22），handoffCh44/56/66/81；读Ch21/23。`Books Pending — Refine Existing Argument`。

### VisualSimpleQA

- **Identity / access:** 2025-W10，25/30，`visualsimpleqa-decoupled-factuality`，arXiv v1 + dataset；v1 2025-03-09。已读 https://arxiv.org/html/2503.06492v1 的paired text/multimodal design、difficulty criteria、six-annotator evidence/ROI verification、15-model evaluation、refusal metrics与hard subset analysis。
- **Problem / mechanism:**end-to-end multimodal accuracy无法判断错误来自visual extraction还是linguistic knowledge。每条sample同时包含image-grounded question、把必要visual rationale显式写出的self-contained text-only question与ground truth；text-only score近似language-module ceiling，TQA→MQA relative degradation近似visual-module gap。benchmark ownspaired identity/evidence/ROI，model refusal与answer分别计数。
- **Evidence contract:**VisualSimpleQA-hard按difficulty≥0.7选129项；评测GPT-4o、Claude、Gemini与12个open LVLM，分别报告correct/incorrect/refusal和non-refusal conditional accuracy。结果证明该paired harness能暴露module gap，不证明text-only question与visual perception严格等价，也不能把API model snapshot分数外推当前版本或deployment hallucination rate。
- **Boundary / owner:**ROI、knowledge popularity、question rewrite与judge/annotation可引入construct bias；refusal提高safety却会降低coverage，必须共同报告。end-to-end task benchmark在验证真实workflow时仍必要。`Layering / Dependency`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `MULTIMODAL-REPRESENTATION`（Ch23）；读Ch65/67。`Books Pending — Refine Existing Argument`。

### MoE-X / Intrinsically Interpretable MoE

- **Identity / access:** 2025-W10，27/30，`moex-intrinsic-interpretability`，arXiv v1；v1 2025-03-05。已读 https://arxiv.org/html/2503.07639v1 的wide-sparse equivalence、ReLU experts、sparsity-aware router/complexity、chess/FineWeb experiments、SAE comparison、ablations、auto-interpretability与appendices；hardware未披露。
- **Problem / mechanism:**dense neurons polysemantic，post-hoc SAE需额外artifact且reconstruction不完美。MoE-X把all experts视作一个wide sparse MLP，以ReLU制造intra-expert activation sparsity，再用expert weight statistics预测哪个expert会更sparse，router优先选择这些experts；router ownsexpert selection，activation feature ownsinterpretability target，expert parallel placement仍属于runtime。
- **Evidence contract:**16M Lichess games/character PGN，natural language用FineWeb 10BT、context1024、batch320、100k steps，并比较GPT-2/Switch/SAE；BSP coverage/reconstruction和1000 random features的auto-detection支持所测small/medium models更易解释。它不证明features是causal/monosemantic，不证明frontier-scale、安全行为或sparsity router的distributed latency；没有独立Limitations和hardware contract。
- **Boundary / owner:**interpretability objective可能与quality/load balance冲突，ReLU dead features、router metric gaming、expert collapse和all-to-all skew仍存在；SAE适用于既有frozen dense model。`Alternative Branch`；owner `MODEL-MOE`（Ch21），handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）与 `INFER-EXECUTION`（Ch49）；读Ch20/22。`Books Pending — Experimental`。

### Capacity-Aware Inference

- **Identity / access:** 2025-W10，28/30，`capacity-aware-moe-inference`；arXiv v1 2025-03-07，后续v5/ICLR 2026改名/扩展为Expanded Drop。W10 review锁定 https://arxiv.org/html/2503.05066v1 的Token Drop + Token Reroute、capacity equations、OLMoE/Qwen/DeepSeek/Mixtral evaluation、capacity/reroute ablations与limitations，不把v5机制倒灌。
- **Problem / mechanism:**expert parallel的iteration latency由最重expert而非平均load决定。v1以capacity factor限制每expert assignments；Token Drop按router score删overflow mappings，Token Reroute屏蔽overloaded expert后重算Top-k，把overflow token迭代转给underloaded experts。router score/capacity ownslossy admission policy，runtime ownsplacement与collective synchronization。
- **Evidence contract:**OLMoE/OLMoE-Instruct、Qwen1.5-MoE、DeepSeek-V2-Lite、Mixtral-8×7B等，九项language benchmarks，比较capacity factors、drop metrics、expert drop与reroute rounds；Mixtral case为one expert/GPU，其他可multi-expert/GPU。作者speedup绑定其expert-parallel simulator/implementation、batch/load/model；precision、interconnect、完整GPU型号/concurrency/SLO未统一披露，不能写成通用1.85×。
- **Boundary / owner:**drop直接损失token-expert computation，reroute改变trained routing distribution并增加Top-k rounds；低capacity会损quality，placement/network不均衡也不会被token policy完全消除。dropless routing在quality-first或balanced workload仍合理。`Direct Evolution`；owner `INFER-EXECUTION`（Ch49），handoff `MODEL-MOE`（Ch21）与 `PLATFORM-RESOURCE-SCHEDULING`（Ch65）；读Ch48/50。`Books Pending — Refine Existing Argument`。

### Collapse of Dense Retrievers

- **Identity / access:** 2025-W10，27/30，`dense-retriever-heuristic-bias`，arXiv v1；v1 2025-03-06。已读 https://arxiv.org/html/2503.05037v1 的Re-DocRED conversion、six controlled perturbations、multiple retrievers/statistical tests、bias interaction、GPT-4o RAG poisoning与limitations。
- **Problem / mechanism:**dense similarity可被shortness、early position、literal head mention和repetition捷径支配，使含事实证据的document输给无答案foil。作者从Re-DocRED构造每setting 250 queries，控制evidence sentence及unrelated/head-only sentences，逐项干预length/order/literal overlap，再组合foil。retriever ownsranking score，corpus construction ownscounterfactual pair，RAG generator只能看到selected evidence。
- **Evidence contract:**Contriever/RetroMAE/Dragon/COCO-DR等；bias-composition test中正确evidence preference低于3%，GPT-4o/mini在poison/foil/evidence/no-doc条件下比较。它证明这些retrievers在合成可控Wikipedia relations上会被捷径压倒，不证明所有domains、rerankers或hybrid search同样崩溃；GPT-4o同时生成/回答/评价会引入相关误差，论文明确承认Re-DocRED annotation与LLM-eval限制。
- **Boundary / owner:**counterfactual documents可能不自然，statistical significance不等于production prevalence；简单BM25也有literal bias但更可解释。缓解需要retrieval stress tests、reranker/evidence entailment与immutable source，不是只换embedding。`Direct Evolution`；owner `AGENT-RAG`（Ch76），handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch75/77。`Books Pending — Refine Existing Argument`。

### OTTER

- **Identity / access:** 2025-W10，27/30，`otter-text-aware-vla`，arXiv v1；v1 2025-03-05。已读 https://arxiv.org/html/2503.03734v1 的CLIP patch-token alignment、attention pooling/policy/action chunk、DS-PnP/DS-ALL、DROID pretraining、simulation/physical trials、ablations、scaling与limitations。
- **Problem / mechanism:**把vision/text features独立传入small robotics policy会丢失VLM预训练的cross-modal alignment，在少量demonstrations上难学会“指令对应哪个object”。OTTER用per-token language features与CLIP patches算similarity distribution，聚合text-aware visual tokens，再与language token和proprioception进入4-layer policy，预测未来12 actions；frozen VLM ownssemantic prior，policy ownsembodiment/action state。
- **Evidence contract:**10 pick/place tasks、724 demos；四primitives共1,185 demos，DROID/OXE extension；Franka physical 100 in-distribution +70 unseen trials及LIBERO simulation。对Octo/OpenVLA/direct-feature/fine-tuned-CLIP/no-proprioception等ablation支持text-aware frozen features在此setup提高unseen success；不证明跨morphology、long-horizon manipulation、safety或real-time control，paper明确多指hand等非SE(3) embodiment仍是限制。
- **Boundary / owner:**CLIP可能ground错误object，attention pooling压缩spatial detail，frozen semantics与robot domain shift冲突，action chunk放大早期错误；大量robot data充足时end-to-end VLA仍合理。`Alternative Branch`；owner `MULTIMODAL-EMBODIED-VLA`（Ch26），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `AGENT-WORKFLOW`（Ch81）；读Ch25/27。`Books Pending — Experimental`。

### MagicInfinite

- **Identity / access:** 2025-W10，26/30，`magicinfinite-talking-video`，arXiv v1 + project/product page；v1 2025-03-07。已读 https://arxiv.org/html/2503.05978v1 的3D DiT/audio-text-image flow、two-stage curriculum、face mask/adaptive loss、DMD2+CFG distillation、sliding-window inference、1.85M-data/training setup、benchmark/metrics；paper没有独立Limitations或component ablation section。
- **Problem / mechanism:**global text控制scene/motion，audio只控制小face region，joint fine-tune会让强text prior淹没lip signal；full-attention/multi-step CFG又使长视频昂贵。Stage1学image+text I2V，Stage2在face mask内注入Wav2Vec cross-attention并按face area放大loss；DMD2用real/fake distributions+LoRA把50 NFE压到4，sliding windows overlap-blend，sequence parallel分摊full attention。window boundary与previous overlap ownstemporal state。
- **Evidence contract:**1.85M internal 720×1280/129-frame/25fps clips，base 200×H100、distillation16×H100；100 HDTF+100internal tests及30 portraits/20 audio/20 prompts benchmark。8×H100下10秒540p≈10秒、1分钟540p≈60秒与20×均绑定13B/4-step/USP/internal baseline，不证明single-GPU、arbitrary-duration identity或“without quality loss”；internal data、caption teachers与no ablation限制可复现性。
- **Boundary / owner:**overlap blend会累积identity/motion drift，mask/face detector对遮挡、小脸、多人物敏感，three-model distillation与full attention训练成本高；短talking-head可用specialized 2D/3D avatar方案。`Direct Evolution`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `INFER-EXECUTION`（Ch49）与 `MULTIMODAL-REPRESENTATION`（Ch23）；读Ch23/25。`Books Pending — Experimental`。

### AI4SE Benchmark Review / BenchScout / BenchFrame

- **Identity / access:** 2025-W10，25/30，`ai4se-benchmark-lifecycle`；arXiv v1 2025-03-07，v3 later expands census. W10锁定 https://arxiv.org/html/2503.05860v1 的173-study/204-benchmark review、search/quality criteria、BenchScout clustering/user study、BenchFrame、HumanEvalNext construction、10-model evaluation与threats/appendices，不把v3 247/273 census倒灌。
- **Problem / mechanism:**benchmark数量增长后，研究者倾向沿用热门suite，即使tests、canonical solution、language conversion与contamination已失效。BenchScout把paper contexts embedding+cluster/visualize用于发现；BenchFrame把benchmark需求、data/task/test/peer review/version迭代显式化；HumanEvalNext修canonical solutions、扩大assertions、提高conversion compatibility并独立review。
- **Evidence contract:**v1系统回顾173 studies/204 benchmarks，BenchScout 22-person Likert study；HumanEvalNext把assertions从1325增到2551，10 code models相对HumanEval平均pass@1下降31.22 absolute points。结果证明test suite版本会改变排名，不证明更难必然更valid，也不能把下降直接归因contamination；review search只覆盖2014～2024 English/selected indexes，user study小。
- **Boundary / owner:**benchmark repair引入new spec、test oracle、runtime/version与migration成本；过度hardening可能偏向edge cases或canonical style。旧benchmark仍可用于longitudinal continuity，但必须锁版本并与fresh hidden/executable tests并用。`Direct Evolution`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `PLATFORM-MODEL-REGISTRY`（Ch59）与 `AGENT-WORKFLOW`（Ch81）；读Ch65/67。`Books Pending — Refine Existing Argument`。

### LaMaTE / LLM as MT Encoder

- **Identity / access:** 2025-W10，27/30，`lamate-llm-encoder-mt`，arXiv v1 + ACL artifact/code/data；v1 2025-03-09。已读 https://arxiv.org/html/2503.06594v1 的architecture/adaptor/two-stage training、ComMT construction/quality checks、WMT/multitask evaluation、speed/KV model、depth/adaptor/decoder ablations与limitations。
- **Problem / mechanism:**decoder-only MT每个target step携带large LLM layers/KV，source/target共享causal stack；传统NMT高效却缺少LLM representation。LaMaTE用Llama3-8B只编码source，fusion+MLP+bidirectional EncStack适配多层hidden state，再由8-layer lightweight cross-attention decoder生成；stage1在40M bilingual pairs训练adaptor/decoder，stage2用239K ComMT joint tune。encoder output becomesimmutable per-request state，decoder KV只随target增长。
- **Evidence contract:**En↔De/Cs/Ru/Zh、WMT23与ComMT，COMET/BLEU/TSR/HTER；Transformers同framework比较，source lengths/batches下相对Llama3-8B decoding 2.4～6.5×，theoretical KV factor少75%。数字不含vLLM/beam-optimized engine、encoder prefill amortization、TTFT/production SLO；low-resource方向弱于mT5，paper承认random decoder pretraining cost与small decoder bottleneck。
- **Boundary / owner:**拆分提高decode效率，却新增encoder/decoder/adaptor artifacts、two-stage data和cross-version compatibility；general chat/continuation任务仍适合decoder-only，专用seq2seq吞吐场景才获益。`Alternative Branch`；owner `INFER-PREFILL-DECODE`（Ch44），handoff `MODEL-DECODER-ONLY`（Ch18）与 `INFER-KV-CACHE`（Ch45）；读Ch43/45。`Books Pending — Refine Existing Argument`。

### More Documents, Same Length

- **Identity / access:** 2025-W10，27/30，`more-docs-same-length`，arXiv v1 + code/data；v1 2025-03-06。已读 https://arxiv.org/html/2503.04388v1 的controlled MuSiQue transformation、six-model setup、document-count/context controls、random-distractor/contamination analyses、results与limitations。
- **Problem / mechanism:**RAG性能随documents增多下降常与总tokens增长混杂。作者固定supporting evidence与其position，把20 documents逐步减为15/10/8/2～4，并用各document所属Wikipedia page的额外文字扩回相同token length；因此document boundary/semantic similarity成为独立变量。retriever ownsdocument set，prompt assembly ownsbounds/order，model must consolidate acrosssources。
- **Evidence contract:**MuSiQue validation 2,417 questions，Llama3.1 8B/70B、Qwen2 7B/72B、Gemma2 9B/27B，small models A6000、large Together API、temperature0.8、F1。多数models少documents提高5～10%，Qwen2例外；random unrelated distractors反而缓解confusion。它证明所测related distractors/document boundaries有额外cost，不证明真实retrieval、all prompts/orders、citation quality或large document counts。
- **Boundary / owner:**扩写同一Wikipedia page仍改变local coherence，document count与topic redundancy/conflict未完全解耦；实验只2～20 docs且未测retriever errors。更多evidence在diverse independent sources下仍可能提升recall。`Direct Evolution`；owner `AGENT-RAG`（Ch76），handoff `MODEL-LONG-CONTEXT`（Ch22）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch75/77。`Books Pending — Refine Existing Argument`。

### Trajectory Distribution Matching / TDM

- **Identity / access:** 2025-W10，29/30，`tdm-few-step-diffusion-distillation`；arXiv:2503.06674 v1 2025-03-09，Hugging Face于3月17日推荐，故回拨W10而非W11/W12。已读v1的trajectory/distribution background、reverse-KL score objective、step-conditioned fake score、surrogate loss、T2I/T2V experiments、training-cost/user-study contract、component/solver/divergence ablations、algorithm/derivations与appendices；论文没有独立limitations section。
- **Problem / mechanism:**instance-level trajectory distillation要用昂贵teacher ODE solver逐点匹配，受数值误差与student capacity限制；one-step distribution matching忽略中间trajectory，增加steps也难继续获益。TDM只采student的K-step trajectory，在每个intermediate timestep使student marginal反向KL匹配teacher marginal；额外fake-score model近似student score，importance sampling聚焦当前trajectory邻域。TDM-unify把desired step count K同时条件化student与fake score，避免不同step distributions共用score而相互干扰；Pseudo-Huber surrogate归一化大gradient。
- **Evidence contract:**JourneyDB只提供prompts，SD1.5/SDXL/PixArt-α/CogVideoX teachers；PixArt 4-step用batch32、generator lr2e-6、fake-score lr2e-5、500 iterations，作者报告2×A800-hours；SDXL为2 A800-days。HPS/Aesthetic/CLIP/FID与20 prompts、约40 responses的匿名user study；T2V只报告CogVideoX-2B在VBench 80.91→81.65。sampling-step conditioning、importance sampling、surrogate、GAN/SFT、ODE solver、clean/noisy target与Fisher divergence有消融。不同GPU代际/实现的training-days不可直接比较，未披露end-to-end latency、batch inference、precision、energy或production SLO。
- **Boundary / owner:**data-free指不读取真实images，并不免除teacher、real/fake score和student计算；student上限受teacher distribution限制，作者也建议先用高质量real data微调弱teacher。reverse-KL与HPS可能偏向高偏好mode，40份user responses不足以证明普遍超越teacher；4 NFE也不自动等于25×wall-clock。原始多步teacher在质量上界、可调CFG或无需额外distillation artifact时仍合理。`Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `INFER-TENSORRT-LLM`（Ch49）与 `TRAIN-CHECKPOINT`（Ch35）；读Ch23/25。`Books Pending — Experimental`。

### ProJudge

- **Identity / access:** 2025-W10，28/30，`projudge-multimodal-process-evaluation`；arXiv:2503.06553 v1 2025-03-09，Hugging Face于3月17日推荐，故回拨W10。已读v1的benchmark/data construction、seven-error taxonomy、human quality control、ProJudge-173k双路径生成/filter、Dynamic Dual-Phase objective、11-model evaluation、cross-domain/model/error analyses、LoRA ablation、training details与prompts；论文没有独立limitations section。
- **Problem / mechanism:**final-answer accuracy会接受“错误过程碰巧得到正确终点”，但通用judge自身也可能误看图、误算或偏爱同family reasoning style。ProJudgeBench将400 scientific problems扩成2,400 model-generated solutions/50,118 step labels，每step标记correctness、7类error和explanation。训练集一支由GPT-4o向correct solution注入已知错误，一支收集9个MLLM自然错误再由GPT-4o标注；DDP在direct evaluate与“先独立解题、再比较student solution”两种目标间动态切换。
- **Evidence contract:**四学科、K12/OlympiadBench/OlympicArena，6位通过考试的human annotators；re-annotation与会议解决disagreement，但未公布IAA数值。ProJudge-173k共173,354 samples，GPT-4o同时承担error injection/annotation，Qwen2.5-72B负责step splitting。11个base judges与3个LoRA models按相同prompt测试；8×H100、一epoch、global batch16。step-correctness提升很大，但error-type accuracy仍低且不均衡；DDP相对普通FT的增益仅约1～5 points。没有explanation-quality metric、calibration、false-positive cost、out-of-domain production traces或human adjudication study。
- **Boundary / owner:**process label粒度由splitter和taxonomy共同定义；same-family judge advantage、visual-error低检测率与judge自身错误生成暴露相关偏差。先解题再judge可提供reference，却增加tokens/latency并可能产生共同错误；正确final answer作为hint也改变任务。deterministic calculator/solver、domain expert与outcome verifier仍是高风险claim的authority。`Direct Evolution`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `TRAIN-SFT`（Ch29）；读Ch65/67。`Books Pending — Refine Existing Argument`。

### ARMOR v0.1

- **Identity / access:** 2025-W10，27/30，`armor-asymmetric-unified-multimodal-generation`；arXiv:2503.06542 v1 2025-03-09，Hugging Face于3月17日推荐，故回拨W10。已读v1的architecture/loss、four data modes、WoHG三阶段训练、9 understanding benchmarks、GenEval、forward-switch ablation、mixed-output appendix与conclusion；论文没有独立limitations、完整optimizer/batch/SLO或artifact release evidence。
- **Problem / mechanism:**从头联合训练understanding+generation成本高且可能相互干扰；给MLLM直接扩展统一vocabulary又让text/image tokens在巨大的混合output space竞争。ARMOR保留InternVL2.5理解路径，加入Chameleon VQGAN decoder、8192 image tokens、0.7B adapter/output parameters，并用`<imgbos>/<imgend>`切换text head与image head。WoHG依次训练“选择输出modality”（text loss）、“学习image generation”（image loss）、“组合interleaved response”（joint loss），通过不同freeze/train sets减少原理解权重变化。
- **Evidence contract:**stage1各100K t2t/ti2t/t2i/t2ti，stage2各2.5M t2i/t2ti，stage3各50K；多项为self-constructed且provenance/filter未披露。作者报告8B、5M train images、160 H100-days、256px GenEval0.37，仅与Chameleon同属interleaved-output group；understanding保留约95%基于9 benchmark。0.5M/5-epoch ablation只比较dual-head vs full mixed head的loss/qualitative images，没有同compute quantitative FID/GenEval、catastrophic-forgetting trajectory、interleaved factual consistency或human evaluation。
- **Boundary / owner:**modality head缩小classification space并让commit token可见，却新增mode misrouting、head calibration、codebook/version和跨image/text rollback；“只增加7%参数”不包含base model、VQGAN与5M-data训练总成本。低分辨率generation落后专用models，self-constructed interleaving可能塑造style。separate understanding/generation services在quality、independent scaling与failure isolation优先时仍合理。`Alternative Branch`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `TRAIN-SFT`（Ch29）；读Ch23/25。`Books Pending — Experimental`。

### GoalFlow

- **Identity / access:** 2025-W10，27/30，`goalflow-goal-conditioned-trajectory-flow`；arXiv:2503.05689 v1 2025-03-07，后续至v6。v1 HTML错误渲染author-response template，已完整读取12页v1 PDF的perception/goal vocabulary/scorers/rectified-flow planner、losses、NavSim setup、baselines、component/step/noise/model-scale ablations与conclusion；不使用v2-v6扩展事实。
- **Problem / mechanism:**无约束diffusion生成的multimodal trajectories过度发散，后置map scorer难以从许多不可行候选中选择；固定command/goal若偏离scene truth又会降低trajectory quality。GoalFlow融合camera+LiDAR为BEV，在训练trajectory endpoints上cluster 4096/8192 goal vocabulary；Transformer scorer同时预测distance-to-ground-truth与shadow-vehicle drivable-area compliance，选goal条件化rectified flow生成128条4-second trajectories，最终scorer按goal consistency与scene evidence选一个。
- **Evidence contract:**OpenScene120h，NavSim 1,192 trainval/136 test scenarios、2Hz samples，LQR插值到10Hz；4 nodes×8 RTX4090/3090。GoalFlow PDMS90.3对TransFuser84.0；component ablation从flow85.6、distance goal88.5、DAC89.4到scorer90.3。20→1 step将denoise time177.8→10.4ms、PDMS89.9→88.9，但只是planner denoise而非end-to-end sensor latency。noise sigma>0.1急剧崩溃，说明multimodality operating point敏感；SDDC因benchmark issue被省略，NavSim非reactive simulation不能证明真实closed-loop safety。
- **Boundary / owner:**goal decomposition降低trajectory divergence，却把endpoint vocabulary、drivable polygon labels与scorer errors变成新failure owners；训练用ground-truth endpoint而test用predicted goal形成exposure gap。128-candidate selection也不是“单步端到端”。rule/optimization planner在hard constraints、certification与rare events下仍合理；real deployment需latency、calibration、sensor failure、interaction与intervention evidence。`Direct Evolution`；owner `MULTIMODAL-EMBODIED-VLA`（Ch26），handoff `MULTIMODAL-WORLD-MODELS`（Ch25）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch25/27。`Books Pending — Experimental`。

### DropletVideo

- **Identity / access:** 2025-W10，28/30，`dropletvideo-integral-spatiotemporal-generation`；arXiv:2503.06053唯一v1为2025-03-08，HF于3月18日推荐。已读v1的dataset pipeline、caption teachers、3D causal VAE/MMDiT/MAG architecture、training、qualitative/quantitative comparison、dense-prompt rewrite与conclusion；论文没有独立limitations、training hardware/steps/total compute或controlled component ablations，artifact只作identity。
- **Problem / mechanism:**分别学习object motion和camera control不能表达“镜头转动后新对象出现、旧事件仍延续”的联合状态。pipeline从2.81M YouTube links用optical flow/PySceneDetect切107.6M clips，20K人工camera labels训练VideoSwin filter，再用aesthetic/DOVER筛至10M；fine-tuned InternVL2-8B生成平均206词captions。模型以CogVideoX-Fun初始化，3D causal VAE+42-layer/48-head MMDiT联合text/video experts；Motion Adaptive Generation用全clip均匀采样定义motion intensity M并经expert AdaLN注入时间/运动控制。
- **Evidence contract:**10M clips/2.21B frames/20.4K hours，来源为网络视频且仅academic non-commercial；caption human expert评估没有样本数/IAA。训练分49×512²与85×896²两阶段、bf16/DeepSpeed/Adam、text length400，但GPU/steps/batch/energy未披露。VBench++的1,118 prompts又被600-pair LoRA prompt rewriter扩写为camera-aware文本，DropletVideo与baselines未必接收等价原始condition；主表只比较四个I2V models，camera motion37.93 vs Cosmos37.56，dynamic degree显著低于Cosmos。closed-source qualitative comparisons也缺同版本/seed/setting contract。
- **Boundary / owner:**camera+plot joint captions让state transition更可学，却继承optical-flow selection、teacher hallucination、copyright/license、aesthetic filtering和prompt-expansion bias；7.3s average clips与85 frames不证明long narrative memory，paper也承认360° consistency失败。它生成observations而非action-conditioned transition或persistent revisable world state，因此不是World Model。`Direct Evolution / Data-Mechanism Coupling`；owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `TRAIN-DATA`（Ch27）、`MULTIMODAL-WORLD-MODELS`（Ch25）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch23/25。`Books Pending — Refine Existing Argument`。

### Mechanistic Interpretability Adversarial Attack / SSR

- **Identity / access:** 2025-W10，26/30，`ssr-mechanistic-refusal-subspace-attack`；arXiv:2503.06269唯一v1为2025-03-08，HF于3月18日推荐。HTML不可访问，已读33页v1 PDF的contrastive datasets/models/judge、probe/refusal-direction/head analyses、three SSR objectives、GCG comparison、chat templates/judging/ablation/transfer appendices与limitations；official code/datasets用于artifact identity，hardware未披露。
- **Problem / mechanism:**GCG只沿output loss搜索discrete suffix，忽略内部refusal circuit，强aligned models上昂贵且失败。SSR先用60个AdvBench harmful prompts及最小改写harmless pairs，取last-token residual activations；Probe-SSR让suffix把多层representation推入linear-probe acceptance region，Steering-SSR逼近negative refusal-direction intervention同时保持orthogonal component，Attention-SSR重定向/压低safety heads。token search仍用top-k coordinate gradients，但forward可在最后目标层提前停止。
- **Evidence contract:**Llama3.2 1B/3B、Gemma2 2B、Qwen2.5 1.5B，greedy decode；bag-of-words→LLM judge→ambiguous manual review。Probe SSR ASR 0.80～0.91，Qwen/Llama1B/Gemma nanoGCG为0.85/0.06/0.53，Llama3B为0；Llama1B 3-token suffix可约16秒生成，但GPU、batch、precision未披露。Attention-SSR对Qwen随机late heads也有效，作者明确该结果应discard；带*值是multi-attempt，真实single-attempt更低。loss最低候选也未必成功，说明subspace proxy与harmful-output judge不一致。
- **Boundary / owner:**linear separation不等于单一causal refusal mechanism；SSR可能同时改多个components，长suffix产生semantic drift，probe还偏向cyber/Python data。attack几乎不跨模型，依赖weights/activations/gradients和exact chat template，不适用于black-box threat actor；缺少large-model、defense-aware和benign-utility tests。解释工具既可用于防御也会降低攻击成本，Security应把white-box access、artifact leakage与latent monitoring纳入threat model。`Threat-model Evolution / Principle Reuse`；owner `PLATFORM-SECURITY`（Ch72），handoff `PLATFORM-EVALUATION-SYSTEM`（Ch66）与 `TRAIN-DPO`（Ch34）；读Ch71/73。`Books Pending — Refine Existing Argument`。

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。
- W10 当前共 53 个scored owner events：47 个 `20+` Full Source Reviews、6 个低分/版本事实核验，ordinary pending为零。
- Scholar/OpenAlex/DBLP historical export 与部分 engineering release feed 是 declared Discovery Gap，不支持“年度无遗漏”。

## Cross-Week Deduplication

- 事件按 first-public date 归属本周；后续 revision、模型卡补充和工程集成回链本周，不重复创建新事件。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。
- Phi-4 Mini/Multimodal report 与模型卡并入 W09 launch family；LADDER、Babel、Remasking、Predictive Data
  Selection、Chain of Draft、DeepSolution、ViDoRAG、LettuceDetect、TeleRAG、DexGraspVLA、DuoDecoding 与
  LLM as a Broken Telephone 按 v1 回拨 W09，不在 W10 重复计分。

## Knowledge Tree Position

- `INFER-SPECULATIVE-DECODING`：EAGLE-3。
- `TRAIN-DATA` / `TRAIN-GRPO` / `TRAIN-DPO` / `TRAIN-PIPELINE-PARALLEL`：RDS、SampleMix、KodCode、
  Visual-RFT、Cognitive Behaviors、Mask-DPO、Process Self-Rewarding、PipeOffload。
- `MODEL-SELF-ATTENTION` / `MODEL-SAMPLING` / `INFER-TENSORRT-LLM`：Liger、IVR、RSQ。
- `MULTIMODAL-REPRESENTATION` / `MULTIMODAL-GENERATIVE-PARADIGMS`：STORM、Audio Flamingo 2、Gen3C。
- `PLATFORM-EVALUATION-SYSTEM`：uncertainty、HoT；Mistral OCR 仅作 version/product fact。
- `AGENT-MEMORY` / `AGENT-PLANNING` / `AGENT-TOOL-CALLING` / `AGENT-MULTI-AGENT`：AppAgentX、MPO、
  ToolRet、START、MultiAgentBench。

## Recommended Action

- 45 个 `20+` family 均已达到 Source Review 门槛，Books disposition保持`Books Pending`，等待独立Books阶段。
- 6 个低分/版本事实保持 Weekly Only；不得因产品可用性或窄 benchmark 修改长期机制正文。

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

W10 Candidate Evidence Gate在ARMOR、GoalFlow与后续DropletVideo完成后按declared-gap规则再次通过；Historical Books Gate仍关闭。本轮只完成Weekly
证据恢复，没有修改 Books；`Books Pending` 不是已吸收声明。年度 Archive Completion Gate 仍 Open。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。
- Difix3D+、DiffRhythm、Kiss3DGen、OneRec、Qilin、VideoUFO、PodAgent 等 domain/application papers 已检查
  identity/abstract；没有改变当前 AI System owner 的独立长期机制，留作 discovery noise，不以热度强行升分。

## Repository Changes

- `papers/2025/weekly/2025-W10/README.md` 当前53个scored events均拥有disposition，ordinary pending为零；Candidate Evidence Gate再次通过。
- 同步 `papers/2025/weekly/README.md` 的逐项账本与 forward cursor；同步 `docs/LEARNING_STATE.md` 的暂停断点。
- 未修改 Books、ROADMAP 或 DECISIONS；未 stage、commit 或 push。

## Open Questions

- draft acceptance、verification cost 与 target batch opportunity cost 的联合最优仍依赖 workload。
- Mistral OCR 的结构保真、错误可见性与下游恢复证据仍不足。
- Scholar/OpenAlex/DBLP historical export 能否发现 HF/arXiv feed 之外的新 owner？
- engineering repositories 的不可导出历史 release feed 是否需要用户提供 snapshot？这些进入年度 Materials Request Ledger。
- W11 fixed-source replay继续可能暴露W10 owner；本次ONNX Runtime v1.21.0已回拨闭合，不在W11重复计分。

## W11 Discovery Spillback Resolution（2026-08-21）

W11 replay 的 2025-03-10 discovery feed 暴露以下 7 个 v1 实际属于 W10 的 Source Family。7项均已完成
primary-source Full Source Review、评分、owner与disposition，不在W11重复计分。W10最终账目为29个`20+` reviews、
6个低分核验、0 ordinary pending；Candidate Evidence Gate再次通过，年度Archive gaps保持Open。

- Unified Reward Model — arXiv 2503.05236，v1 2025-03-07。
- Sketch-of-Thought — arXiv 2503.05179，v1 2025-03-07。
- Forgetting Transformer — arXiv 2503.02130，v1 2025-03-03。
- R1-Searcher — arXiv 2503.05592，v1 2025-03-08。
- SafeArena — arXiv 2503.04957，v1 2025-03-07。
- Learning from Failures in Multi-Attempt RL — arXiv 2503.04808，v1 2025-03-06。
- Linear-MoE — arXiv 2503.05447，v1 2025-03-08。

## W11 Later-page Spillback Resolution（2026-08-21）

继续扫描3月13～14 feed后新增两个W10 owner；两项均已完成Full Source Review、评分、owner与disposition。
W10最终账目为31个`20+` reviews、6个低分核验、0 ordinary pending，Gate再次通过：

- WildIFEval — arXiv 2503.06573，v1 2025-03-09。
- Shifting Long-Context LLMs Research from Input to Output — arXiv 2503.04723，v1 2025-03-06。

## March 12 Curation-Lag Resolution

- 2025-03-12 Hugging Face推荐页延迟暴露5个W10 owner：VisualSimpleQA（v1 03-09）、Mixture of Experts Made Intrinsically Interpretable（03-05）、Capacity-Aware Inference（03-07）、Collapse of Dense Retrievers（03-06）与OTTER（03-05）。
- 五项均已完成event-time v1全文、实验/ablation/limitations、owner与disposition；Capacity-Aware Inference明确隔离2026 v5/ICLR mechanism revision。
- W10现为36个`20+` Full Source Reviews、6个低分核验、0 ordinary pending，Candidate Evidence Gate再次通过；年度Archive gaps仍Open。

## March 12 Second Curation-Lag Resolution

- MagicInfinite（arXiv:2503.05978，v1 2025-03-07）、Benchmarking AI Models in Software Engineering（arXiv:2503.05860，v1 2025-03-07）与Beyond Decoder-only MT（arXiv:2503.06594，v1 2025-03-09）由同一推荐页后续条目延迟发现，按first-public date回拨W10。
- 三项均已完成event-time v1全文、实验/limitations、owner与disposition；MagicInfinite vendor benchmark与LaMaTE decoding speed均保留完整workload boundary，AI4SE review锁定v1 census。
- W10现为39个`20+` Full Source Reviews、6个低分核验、0 ordinary pending，Candidate Evidence Gate再次通过；年度Archive gaps仍Open。

## March 13 Curation-Lag Resolution

- `More Documents, Same Length`（arXiv:2503.04388，v1 2025-03-06）由3月13推荐页延迟发现并回拨W10；已完成controlled multi-document experiment、six-model evaluation、analysis、limitations与owner审计。
- W10现为40个`20+` Full Source Reviews、6个低分核验、0 ordinary pending，Candidate Evidence Gate再次通过；年度Archive gaps仍Open。

## W11 Fixed-source Spillback Resolution（2026-08-21）

- ONNX Runtime v1.21.0（official release 2025-03-08）由W11工程源重放发现并回拨W10。
- 已完成release/migration/GenAI pipeline/execution-provider全文审计、26/30评分、owner与Books-deferred disposition。
- W10现为42个`20+` Full Source Reviews、6个低分核验、0 ordinary pending；TDM按v1日期从W12推荐页回拨并完成审计，Candidate Evidence Gate再次通过，年度Archive gaps仍Open。

## Sources

- MagicInfinite v1 — https://arxiv.org/html/2503.05978v1（First Public: 2025-03-07；Accessed: 2026-08-21）
- AI4SE benchmark review v1 — https://arxiv.org/html/2503.05860v1；https://arxiv.org/abs/2503.05860（First Public: 2025-03-07；Accessed: 2026-08-21）
- LaMaTE v1 — https://arxiv.org/html/2503.06594v1（First Public: 2025-03-09；Accessed: 2026-08-21）
- More Documents, Same Length v1 — https://arxiv.org/html/2503.04388v1（First Public: 2025-03-06；Accessed: 2026-08-21）
- ONNX Runtime v1.21.0 — https://github.com/microsoft/onnxruntime/releases/tag/v1.21.0（Released: 2025-03-08；Accessed: 2026-08-21）
- Trajectory Distribution Matching / TDM v1 — https://arxiv.org/html/2503.06674v1（First Public: 2025-03-09；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- ProJudge v1 — https://arxiv.org/html/2503.06553v1（First Public: 2025-03-09；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- ARMOR v0.1 — https://arxiv.org/html/2503.06542v1（First Public: 2025-03-09；HF Recommended: 2025-03-17；Accessed: 2026-08-21）
- GoalFlow v1 metadata / PDF — https://arxiv.org/abs/2503.05689；https://arxiv.org/pdf/2503.05689v1（First Public: 2025-03-07；HTML mismatch；Accessed: 2026-08-21）
- DropletVideo v1 — https://arxiv.org/html/2503.06053v1（First Public: 2025-03-08；Full Source Review Complete；Accessed: 2026-08-21）
- Mechanistic Interpretability Adversarial Attack v1 PDF — https://arxiv.org/pdf/2503.06269v1（First Public: 2025-03-08；Full Source Review Complete；HTML unavailable；Accessed: 2026-08-21）

- VisualSimpleQA v1 — https://arxiv.org/html/2503.06492v1（First Public: 2025-03-09；Accessed: 2026-08-21）
- MoE-X v1 — https://arxiv.org/html/2503.07639v1（First Public: 2025-03-05；Accessed: 2026-08-21）
- Capacity-Aware Inference v1 — https://arxiv.org/html/2503.05066v1；https://arxiv.org/abs/2503.05066（First Public: 2025-03-07；Accessed: 2026-08-21）
- Collapse of Dense Retrievers v1 — https://arxiv.org/html/2503.05037v1（First Public: 2025-03-06；Accessed: 2026-08-21）
- OTTER v1 — https://arxiv.org/html/2503.03734v1（First Public: 2025-03-05；Accessed: 2026-08-21）

- EAGLE-3 — https://arxiv.org/abs/2503.01840（First Public: 2025-03-03；Accessed: 2026-07-31）
- Mistral OCR — https://mistral.ai/news/mistral-ocr（First Public: 2025-03-06；Accessed: 2026-07-31）
- Visual-RFT — https://arxiv.org/html/2503.01785（v1: 2025-03-03；Accessed: 2026-08-20）
- Cognitive Behaviors — https://arxiv.org/html/2503.01307（v1: 2025-03-03；Accessed: 2026-08-20）
- LLM uncertainty — https://arxiv.org/html/2503.01688（v1: 2025-03-03；Accessed: 2026-08-20）
- Liger — https://arxiv.org/html/2503.01496（v1: 2025-03-03；Accessed: 2026-08-20）
- Large-Scale Data Selection — https://arxiv.org/html/2503.01807（v1: 2025-03-03；Accessed: 2026-08-20）
- SampleMix — https://arxiv.org/html/2503.01506（v1: 2025-03-03；Accessed: 2026-08-20）
- RSQ — https://arxiv.org/html/2503.01820（v1: 2025-03-03；Accessed: 2026-08-20）
- MultiAgentBench — https://arxiv.org/html/2503.01935（v1: 2025-03-03；Accessed: 2026-08-20）
- MPO — https://arxiv.org/html/2503.02682（v1: 2025-03-04；Accessed: 2026-08-20）
- Mask-DPO — https://arxiv.org/html/2503.02846（v1: 2025-03-04；Accessed: 2026-08-20）
- PipeOffload — https://arxiv.org/html/2503.01328（v1: 2025-03-03；Accessed: 2026-08-20）
- IVR — https://arxiv.org/html/2503.02368（v1: 2025-03-04；Accessed: 2026-08-20）
- AppAgentX — https://arxiv.org/html/2503.02268（v1: 2025-03-04；Accessed: 2026-08-20）
- HoT — https://arxiv.org/html/2503.02003（v1: 2025-03-03；Accessed: 2026-08-20）
- Process-based Self-Rewarding — https://arxiv.org/html/2503.03746（v1: 2025-03-05；Accessed: 2026-08-20）
- KodCode — https://arxiv.org/html/2503.02951（v1: 2025-03-04；Accessed: 2026-08-20）
- Gen3C — https://arxiv.org/html/2503.03751（v1: 2025-03-05；Accessed: 2026-08-20）
- ToolRet — https://arxiv.org/html/2503.01763（v1: 2025-03-03；Accessed: 2026-08-20）
- START — https://arxiv.org/html/2503.04625（v1: 2025-03-06；Accessed: 2026-08-20）
- STORM — https://arxiv.org/html/2503.04130（v1: 2025-03-06；Accessed: 2026-08-20）
- Audio Flamingo 2 — https://arxiv.org/html/2503.03983（v1: 2025-03-06；Accessed: 2026-08-20）
- JAX 0.5.2 — https://github.com/jax-ml/jax/blob/main/CHANGELOG.md#jax-052-march-4-2025（Accessed: 2026-08-20）
