# AI Research Weekly — 2025-W10

> Coverage Window: 2025-03-03～2025-03-09
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 2 项与长期 AI System 认知相关的证据：EAGLE-3、Mistral OCR。重点不是记录发布热度，而是识别其改变了哪一项约束、机制与系统 trade-off。所有结论均按首次公开时间归档，性能或能力数字不脱离作者披露的模型、硬件、精度、输入输出、并发与 SLO 条件使用。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；访问日期统一为 2026-07-31。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：Mistral OCR（2025-03-06）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 保留：EAGLE-3（2025-03-03）。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| EAGLE-3 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Must Read；与后续 MTP/SpecForge 联合进入第 44 章审计 |
| Mistral OCR | 4 | 3 | 3 | 3 | 3 | 3 | 19/30 | Record Only；未达 Books 门槛 |

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

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- 事件按 first-public date 归属本周；后续 revision、模型卡补充和工程集成回链本周，不重复创建新事件。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- EAGLE-3 → 第 40、44、45、47、52 章（Direct Evolution）
- Mistral OCR → 第 11、23、71 章（Layering / Dependency）

## Recommended Action

- EAGLE-3：Must Read；与后续 MTP/SpecForge 联合进入第 44 章审计
- Mistral OCR：Record Only；未达 Books 门槛

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。

## Repository Changes

- 新增 papers/2025/weekly/2025-W10/README.md。
- 更新 books/part-04-inference-system/44-speculative-decoding.md。

## Open Questions

- draft acceptance、verification cost 与 target batch opportunity cost 的联合最优仍依赖 workload。
- Mistral OCR 的结构保真、错误可见性与下游恢复证据仍不足。

## Sources

- EAGLE-3 — https://arxiv.org/abs/2503.01840（First Public: 2025-03-03；Accessed: 2026-07-31）
- Mistral OCR — https://mistral.ai/news/mistral-ocr（First Public: 2025-03-06；Accessed: 2026-07-31）
