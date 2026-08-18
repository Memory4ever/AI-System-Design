# AI Research Weekly — 2025-W25

> Coverage Window: 2025-06-16～2025-06-22
> Research Mode: Retrospective Primary-Source Backfill
> Re-audited: 2026-08-24
> Audit Status: Candidate Evidence Gate Passed — 47/47 Retained Full Source Review Complete
> Historical Books Gate: Closed

## Executive Summary

旧档案只保留MiniMax-M1与Gemini 2.5 GA，明显欠召回。本轮按完整Monday～Sunday窗口重放固定机构、arXiv、跨索引与AI Infra来源，最终闭合58个owner identities：47项达到`20+`并全部完成非模板化Full Source Review，11项低分完成来源、日期、评分与拒绝核验；普通pending、blocked与family-level disputed均为0。AceReason-Nemotron 1.1与Guru各保留一项`Disputed numerical subclaim`，但局部数字冲突不升级为整项family disputed。Candidate Evidence Gate通过；Historical Books Gate仍按年度规则关闭。

本周机制主线横跨queryable training-data view、长rollout RL、reasoning-path measurement、训练优化器与稀疏更新、diffusion context extrapolation、多模态生成、长视频tool workflow、近似checkpoint recovery、KV eviction、可执行Agent安全与evaluation harness。这里的“通过”只表示W25候选证据闭合，不表示Historical Books Integration已获授权。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 归档；搜索收录日与后续修订不替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery 与去重；论文机制回到正文。Crossref 仅做 Weekly metadata 交叉检查。
- 历史回填不补造 Daily；本轮未单独标注的source均于2026-08-24访问，旧packet保留其2026-07-31或2026-08-22访问记录。
- benchmark 缺少模型、硬件、长度、batch/concurrency、precision/quantization 与 SLO 时不做通用结论。
- 06-19～22的HTML/PDF回退、固定机构与固定工程项目release/RFC/tag扫描已重放；Scholar/OpenAlex/DBLP仅用于identity/metadata交叉检查，不以搜索摘要代替全文。没有可证明为W25 owner的额外官方机制事件；未披露内部机制的产品事实不进入机制结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- official owner为Gemini 2.5 Pro/Flash GA；固定机构扫描未发现第二个可由本周primary event date确认且改变长期机制的官方owner。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 最终定位54个论文owner；44个20+ paper family全部完成Full Source Review，10个论文低分family闭合拒绝。另有Gemini GA、SGLang工程报告、TensorRT-LLM release与Ray patch四个官方/Infra owner；revision仍归同一Source Family，不重复计分。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- SGLang GB200 PD/EP工程报告与TensorRT-LLM v0.20.0完成primary code/release联合审计；Ray 2.47.1闭合为16分patch fact。其余固定release/RFC/PR/tag未发现满足owner、日期与机制门槛的本周Infra事件。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| MiniMax-M1 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| Gemini 2.5 Pro/Flash GA | 3 | 3 | 3 | 4 | 4 | 3 | 20/30 | Full Source Review Complete — Version Fact |
| Essential-Web v1.0 | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete |
| Ego-R1 | 4 | 4 | 3 | 4 | 4 | 5 | 24/30 | Full Source Review Complete |
| AceReason-Nemotron 1.1 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental / Numerical Subclaim Disputed |
| RLVR Implicitly Incentivizes Correct Reasoning | 5 | 4 | 3 | 4 | 5 | 5 | 26/30 | Full Source Review Complete — Experimental / Judge-calibration Boundary |
| LongLLaDA | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | Full Source Review Complete |
| Xolver | 3 | 3 | 3 | 4 | 4 | 4 | 21/30 | Full Source Review Complete — Experimental |
| Reasoning with Exploration | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental / Entropy-actuator Boundary |
| Stream-Omni | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental |
| From Bytes to Ideas | 5 | 3 | 3 | 4 | 4 | 4 | 23/30 | Full Source Review Complete — Experimental |
| Ring-lite | 4 | 4 | 3 | 3 | 4 | 4 | 22/30 | Full Source Review Complete — Experimental |
| AgentSynth | 4 | 5 | 5 | 4 | 4 | 3 | 25/30 | Full Source Review Complete — Experimental |
| xbench | 4 | 5 | 4 | 4 | 5 | 3 | 25/30 | Full Source Review Complete — Evaluation |
| MultiFinBen | 3 | 3 | 3 | 4 | 3 | 4 | 20/30 | Full Source Review Complete — Evaluation |
| Efficient Medical VIE via RL | 3 | 3 | 4 | 4 | 3 | 3 | 20/30 | Full Source Review Complete — Experimental |
| Align Your Flow | 4 | 3 | 3 | 4 | 3 | 3 | 20/30 | Full Source Review Complete — Experimental |
| Guaranteed Guess | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Source Review Complete — Experimental |
| Optimizing Length Compression | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental |
| Taming Polysemanticity | 5 | 4 | 3 | 4 | 4 | 5 | 25/30 | Full Source Review Complete — Experimental |
| Sekai | 3 | 3 | 4 | 4 | 4 | 3 | 21/30 | Full Source Review Complete — Dataset / Experimental |
| All is Not Lost / CheckFree | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Full Source Review Complete |
| ProtoReasoning | 4 | 3 | 3 | 4 | 4 | 4 | 22/30 | Full Source Review Complete — Experimental |
| Embodied Web Agents | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | Full Source Review Complete — Experimental |
| SwarmAgentic | 4 | 3 | 3 | 4 | 4 | 4 | 22/30 | Full Source Review Complete — Experimental |
| Semantically-Aware Rewards | 4 | 3 | 3 | 4 | 4 | 4 | 22/30 | Full Source Review Complete — Experimental |
| SciVer | 4 | 5 | 5 | 5 | 4 | 3 | 26/30 | Full Source Review Complete — Evaluation |
| Truncated PPO | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | Full Source Review Complete — Experimental |
| MoTE | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental |
| Evolutionary Caching / ECAD | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental |
| OS-Harm | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Full Source Review Complete |
| GenRecal | 4 | 3 | 4 | 4 | 4 | 3 | 22/30 | Full Source Review Complete — Experimental |
| ImmerseGen | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure |
| GMT | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure |
| PictSure | 3 | 2 | 3 | 4 | 3 | 3 | 18/30 | Low-score closure |
| Guru / Cross-domain RL | 5 | 5 | 5 | 4 | 4 | 3 | 26/30 | Full Source Review Complete — Experimental / Numerical Subclaim Disputed |
| Show-o2 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental |
| SonicVerse | 3 | 2 | 3 | 4 | 2 | 3 | 17/30 | Low-score closure |
| RE-IMAGINE | 4 | 3 | 3 | 4 | 4 | 3 | 21/30 | Full Source Review Complete — Evaluation |
| Ray 2.47.1 | 1 | 2 | 3 | 5 | 3 | 2 | 16/30 | Low-score closure — Patch Fact |
| LazyEviction | 5 | 5 | 4 | 4 | 4 | 3 | 25/30 | Full Source Review Complete — Experimental |
| EvoLM | 5 | 5 | 5 | 4 | 4 | 4 | 27/30 | Full Source Review Complete — Experimental |
| SparseLoRA | 4 | 5 | 5 | 4 | 3 | 3 | 24/30 | Full Source Review Complete — Experimental |
| SCALE Optimizer | 4 | 5 | 4 | 4 | 3 | 4 | 24/30 | Full Source Review Complete — Experimental |
| GRPO-CARE | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental |
| LMR-BENCH | 4 | 5 | 5 | 4 | 4 | 3 | 25/30 | Full Source Review Complete — Evaluation |
| TabArena | 4 | 5 | 5 | 4 | 4 | 3 | 25/30 | Full Source Review Complete — Evaluation |
| LLM Safety under Latent Perturbations | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | Full Source Review Complete — Security / Experimental |
| Mathematical Proof Litmus Test | 3 | 4 | 4 | 4 | 4 | 3 | 22/30 | Full Source Review Complete — Evaluation |
| Tower+ | 4 | 4 | 4 | 4 | 3 | 4 | 23/30 | Full Source Review Complete — Experimental |
| DualTHOR | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure |
| Hunyuan3D 2.5 | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure — Vendor Case |
| Vision-guided Chunking | 3 | 3 | 3 | 3 | 3 | 3 | 18/30 | Low-score closure |
| Multi-hop RAG Generation | 3 | 3 | 2 | 3 | 3 | 3 | 17/30 | Low-score closure |
| OmniReflect | 3 | 3 | 3 | 3 | 4 | 3 | 19/30 | Low-score closure |
| MEXA | 3 | 3 | 3 | 3 | 4 | 3 | 19/30 | Low-score closure |
| SGLang GB200 PD + Large-scale EP | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full Source Review Complete — Engineering Case |
| TensorRT-LLM v0.20.0 | 4 | 5 | 5 | 5 | 4 | 3 | 26/30 | Full Source Review Complete — Version + Public Mechanism |

账目：58 owner rows；47项`20+`、11项低分；47/47 Full Source Review Complete、普通pending 0；11/11低分闭合；blocked 0、family-level disputed 0；AceReason-Nemotron 1.1与Guru各保留1项Disputed numerical subclaim。

### Deep Analysis 1 — MiniMax-M1

- First Public: 2025-06-16
- Status: arXiv v1; open weights; Experimental
- Primary Source: https://arxiv.org/abs/2506.13585
- Evolution Relationship: Direct Evolution

#### Why

长 reasoning rollout 同时放大 attention 成本与 RL sampling 成本；模型架构和 policy optimization 不能分开优化。

#### Principle and Mechanism

M1 延续 hybrid Lightning Attention/MoE，并提出 CISPO，对 importance-sampling weights 而非 token update 进行 clipping，以扩展长上下文 RL。

#### Trade-off and Evidence Boundary

混合 attention 降低长序列成本，CISPO 改变优化稳定性；但作者训练成本和 benchmark 绑定 H800 集群、数据与实现，需全文核验。

#### Connection and Evolution

知识树位置：第 14、21、22、29、45、52 章。Must Read；与 MiniMax-01 建立架构→RL 演进链。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 2 — Gemini 2.5 Pro/Flash GA

- First Public: 2025-06-17
- Status: Official stable product release
- Primary Source: https://blog.google/products-and-platforms/products/gemini/gemini-2-5-model-family-expands/
- Evolution Relationship: Layering / Dependency

#### Why

reasoning model 从 preview 到 stable 会把 latency/cost tiering 变成生产选择。

#### Principle and Mechanism

官方页面证明 GA 和模型族定位，不公开新的长期机制。

#### Trade-off and Evidence Boundary

多档模型改善 cost-quality 选择，也增加 routing、evaluation matrix 和 version governance。

#### Connection and Evolution

知识树位置：第 20、52、69 章。Record Only；不以 GA 状态修改核心章节。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### MiniMax-M1

- **Candidate / Week / Score:** MiniMax-M1 / 2025-W25 / 26/30。
- **Source Family ID:** `MINIMAX-M1-2506.13585`。
- **Source Type:** arXiv v1 technical report、official weights/repository/deployment guides。
- **First-public Date / Revision History:** arXiv v1 2025-06-16；截至本次核验只有v1，不能把后续framework support当作论文revision。
- **Direct Primary Sources:** arXiv:2506.13585 HTML/PDF；MiniMax-AI/MiniMax-M1 repository、model artifacts。
- **Related Primary Sources:** MiniMax-01 report（architecture predecessor）、CISPO引用的GRPO/DAPO与vLLM/Transformers integration。
- **Access and Verification Status:** Verified。全文、公式、训练/评测章节与artifact可访问；训练代码、完整data、kernel patch与可复现RL pipeline未开源。
- **Full-read Coverage:** 已阅读metadata、Introduction、continual pretraining/SFT、CISPO公式与controlled comparison、hybrid-attention precision/optimizer/repetition fixes、rule/model reward data、curriculum、40K→80K scaling、全部evaluation setup/results、conclusion；报告没有独立limitations章节，未披露项按threats记录。
- **Original Problem:** test-time reasoning越长，dense attention rollout cost与RL sampling成本越高；PPO/GRPO token clipping在多轮off-policy update中可能过早丢掉低概率但关键的reflection tokens。
- **Why the Previous Design Was Reasonable:** dense softmax提供精确content addressing；PPO/GRPO clipping限制policy drift并在常见模型/较少off-policy update下稳定。
- **Changed Constraint:** 40K–80K reasoning rollout、16轮off-policy update、hybrid attention kernel与极小gradient使原有cost/precision/clipping假设失效。
- **Mechanism:** 456B/45.9B-active、32 experts的hybrid model每7个Lightning/TransNormer blocks插入1个softmax block；CISPO保留所有token的`log pi` gradient，只对stop-gradient importance weight做上界clip，使用GRPO group-relative advantage、token-level normalization、dynamic sampling和length penalty且无KL项。
- **State Ownership:** rollout policy产生trajectory；rule verifier/generative RM拥有reward；trainer拥有old/current policy version、IS ratio与optimizer；inference/training kernels共同承担概率一致性contract。
- **Control Flow / Data Flow:** continual pretrain 7.5T tokens → long-CoT SFT → 40K RL（rule + model feedback curriculum）→ staged 48/56/64/72/80K RL；rollout token probability与training re-score必须对齐，reward进入group-relative advantage后更新policy。
- **Implementation Details:** LM head升为FP32将train/inference token-prob correlation从约0.9x提高到0.99x；AdamW设`beta=(0.9,0.95), eps=1e-15`；连续3000 token概率>0.99触发repetition truncation；context从32K四阶段平滑扩至1M，output窗口分六阶段扩至80K。
- **Evaluation Setup:** 512 H800、3周是full RL作者报告；核心评测temperature 1.0/top-p 0.95；AIME/GPQA 32 samples，coding 16 samples，SWE-bench用修改的Agentless scaffold，TAU-bench用GPT-4.1 user model/40 steps，LongBench-v2与MRCR覆盖长上下文。
- **Baselines / Ablations / Sensitivity:** Qwen2.5-32B-base zero-RL controlled comparison GRPO/DAPO/CISPO；CISPO在相同steps表现更高并用50% steps匹配DAPO（作者实验）；有RL step/length curve，但没有在456B M1上完整algorithm ablation，也没有hybrid-vs-dense等质量的wall-clock end-to-end消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 512 H800、456B/45.9B active、LM-head FP32、1M input/40K或80K output披露；RL global batch、parallelism、serving precision/concurrency、TTFT/TPOT/SLO不完整。
- **What the Evidence Actually Proves:** 在作者Qwen2.5-32B controlled setup中，clipped IS weight可避免token drop并提高step efficiency；在作者M1 pipeline中，hybrid attention、precision fixes与staged length scaling共同使长rollout RL可运行。
- **What It Does Not Prove:** 不证明CISPO普遍优于GRPO/DAPO，不证明长输出本身导致accuracy，不证明理论FLOPs比例转化为相同production latency/cost；vendor benchmark不能分离model、data、harness与sampling。
- **Limitations / Threats to Validity:** 仅v1作者报告；核心training pipeline/data/kernel未开放；CISPO梯度因weight clipping略有bias；无KL与16次off-policy update的稳定性边界未知；长序列有repetition/pattern collapse；部分评测用model judge和定制scaffold。
- **Trade-offs / New Failure Modes:** hybrid attention降低长序列成本却引入两类state/kernel和probability mismatch；CISPO保留rare-token gradient却弱化trust-region语义、依赖IS cap；长rollout增加reward hacking、repetition、variance与tail straggler。
- **Where the Previous Design Still Applies:** 短rollout、dense model、少量on-policy update或需严格KL/trust-region时，GRPO/PPO仍合理；需要精确远程retrieval时周期softmax层仍不可省。
- **Evolution Relationship:** `Direct Evolution`：MiniMax-01 hybrid architecture → M1长reasoning/RL；GRPO/DAPO → CISPO属于同一policy-optimization branch，不是简单替代。
- **ROADMAP Node:** Ch14、Ch21、Ch22、Ch29、Ch45、Ch52。
- **Target and Adjacent Chapters Read:** 已阅读 Ch13～15、Ch20～22、Ch28～30、Ch44～46、Ch52；Ch22 与 Ch29 的 MiniMax/CISPO 边界已最终复核。
- **Existing Coverage:** Ch22已保留hybrid linear/softmax演进，Ch29已解释CISPO的IS-weight clipping与新failure modes；Books Gate必须根据本packet重审precision mismatch、staged length与“16 off-policy rounds”是否值得refine，避免只留算法口号。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate`；Historical Books Gate关闭，本轮不以既有章节文字替代Weekly证据审计。
- **Changed Files or Rejection Reason:** No Books change authorized by this Weekly re-audit；仅记录后续Gate通过时需要复核的Ch22/Ch33边界。
- **Open Questions:** training/inference kernel exact version、RL parallelism/global batch、full data/reward-model audit与independent CISPO reproduction。

### Gemini 2.5 Pro/Flash GA

- **Candidate / Week / Score:** Gemini 2.5 Pro/Flash GA / 2025-W25 / 20/30。
- **Source Family ID:** `GEMINI-2.5-2025`。
- **Source Type:** 官方GA announcement + Gemini 2.5 technical report/model documentation。
- **First-public Date / Revision History:** model family preview与technical report早于本周；2025-06-17只把Pro/Flash标为stable/GA并引入Flash-Lite preview，不是机制first-public。
- **Direct Primary Sources:** Google 2025-06-17 announcement；Gemini 2.5 technical report；official model docs/model card。
- **Related Primary Sources:** Cloud/API availability和pricing只作为production contract。
- **Access and Verification Status:** Verified for GA/version status；architecture、training data、hardware与routing内部机制仍有大量Not Disclosed。
- **Full-read Coverage:** 已联读GA announcement与此前technical report中model family、thinking budget、multimodal/long-context、evaluation与safety章节；本周页面没有新增method章节。
- **Original Problem:** preview model到production需要稳定identifier、support与cost/latency tiers，不能只依赖一次benchmark snapshot。
- **Why the Previous Design Was Reasonable:** preview阶段允许快速迭代；单一大模型在traffic简单时减少routing/evaluation matrix。
- **Changed Constraint:** production workload需要stable version，同时高吞吐/低延迟场景需要不同cost-quality tier。
- **Mechanism:** 本周只有`Version Fact / Mechanism Not Disclosed`：Pro/Flash GA，Flash-Lite preview；thinking budget、tool与1M context属于family能力，不是6月17新机制。
- **State Ownership:** provider model registry/API拥有version与availability；consumer platform拥有routing、evaluation、budget与rollback。
- **Control Flow / Data Flow:** request policy根据task/SLO选择model tier与thinking budget；response经过相同evaluation/release governance。
- **Implementation Details:** Not Disclosed beyond public API/model contracts。
- **Evaluation Setup:** announcement引用quality/latency图和technical report，但不提供一套绑定production concurrency、region、hardware与SLO的GA benchmark。
- **Baselines / Ablations / Sensitivity:** technical report含model comparisons；GA event没有新增机制消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 1M context与产品tier披露；hardware、precision、batch/concurrency与SLO Not Disclosed。
- **What the Evidence Actually Proves:** 证明Pro/Flash于该日成为stable product，Flash-Lite仍是preview。
- **What It Does Not Prove:** 不证明GA改变model机制，不证明cost-speed Pareto在任意workload成立，不证明model tier可自动路由。
- **Limitations / Threats to Validity:** product announcement、closed implementation、version alias与provider-side更新。
- **Trade-offs / New Failure Modes:** 多tier扩大cost-quality选择，也增加routing policy、evaluation matrix、fallback语义、version drift与budget governance。
- **Where the Previous Design Still Applies:** 固定workload/单一已验证model可避免dynamic routing复杂性。
- **Evolution Relationship:** `Layering / Dependency`：model family → product lifecycle；不是architecture evolution。
- **ROADMAP Node:** Ch20、Ch52、Ch62、Ch69。
- **Target and Adjacent Chapters Read:** 已阅读 Ch20、Ch52、Ch62、Ch69；已有production contract与release gate足以容纳该事实。
- **Existing Coverage:** 当前Books已明确model capability与delivery/runtime分层；GA状态没有新增长期机制。
- **Integration Decision:** `Weekly Only — Version/Product Fact / Historical Books Gate Closed`。
- **Changed Files or Rejection Reason:** No Books change authorized by this Weekly re-audit；GA/price/availability不改变既有机制结论。
- **Open Questions:** stable alias是否固定weight snapshot；provider更新、deprecation与cross-region fallback如何影响reproducibility。

### Essential-Web v1.0

- **Identity / coverage:** `2506.14111`，v1 2025-06-17、v2 06-19；technical report、公开dataset/taxonomy、pipeline、distillation、statistics、training、decontamination、Appendix与limitations已读。Owner `TRAIN-DATA` Ch27，handoff Ch28/Ch66。
- **Problem / mechanism / ownership:** 可下载web corpus不等于可按workload重组的训练资产。作者从248.4B raw documents中保留23.6B/约24T tokens，以12类taxonomy、Qwen2.5-32B teacher与EAI-Distill-0.5B全量label，再用SQL-style predicate materialize不同training views。crawl pipeline拥有raw/dedup/provenance，classifier version拥有label semantics，query/manifest拥有mixture identity。
- **Evaluation contract:** student约82B synthetic labeled tokens；两套约2.3B base models，各320B train+80B anneal；DCLM/Stack等baselines与多domain slices；作者报告约90K MI300X GPU-hours及13-gram Bloom-filter decontamination。完整precision、batch与online SLO未披露。
- **Proves / not / trade-off:** 支持taxonomy+distilled annotator把固定corpus转成可查询、可版本化data view，并改变downstream profile；不证明taxonomy普适、teacher label是真值或所有tokens合法安全。灵活selection换来classifier/version/lineage debt与静默scale amplification；小corpus或高价值domain仍适合curated rules。
- **Disposition:** `Books Pending — Refine Existing Argument Candidate`；no Books change authorized。

### Ego-R1

- **Identity / coverage:** `2506.13654`，v1 2025-06-16；Method、CoTT、SFT/RL、tools、evaluation、ablation、Appendix已读。Owner `AGENT-WORKFLOW` Ch81，handoff Ch76/77/78。
- **Problem / mechanism / ownership:** days/weeks级egocentric video不能整体塞入MLLM context，uniform sampling会漏稀疏证据。Ego-R1以H-RAG、Video-LLM与frame-level VLM三类tool，让policy生成`thought/tool call`，先CoTT SFT再rule-reward GRPO。H-RAG拥有timestamped summaries，tool runtime执行调用，Agent只proposal，Workflow拥有budget/termination，source video保持evidence authority。
- **Evaluation contract:** 4.4K QA、25K CoTT traces、平均7.42 tool calls；SFT/RL 4×80GB A100，baseline inference 1×A100；VideoMME-long、EgoSchema、EgoLifeQA、Ego-R1 Bench及base/RL-only/SFT-only/SFT+RL、RAG-only/full-tools ablations。precision、batch、并发与端到端SLO未披露。
- **Proves / not / trade-off:** 在作者环境中dynamic multi-granularity tool loop比固定frame/RAG更适合稀疏long-video evidence，SFT有助tool-schema cold start；不证明CoTT faithful、开放视频或实时workload泛化。降低context成本却引入retrieval miss、summary loss、wrong range、tool cascade、stale index、隐私与调用成本；短视频/dense evidence仍可直接MLLM。
- **Disposition:** `Books Pending — Refine Existing Argument Candidate`；no Books change authorized。

### AceReason-Nemotron 1.1

- **Identity / coverage:** Source Family `ARXIV-2506.13284`，sole v1 first-public 2025-06-16 09:27:48 UTC，24/30；official model/data同日发布，model commits `5888c19`/`7de383a`与SFT data commits `8b98dc5`/`2323e24`可核。Method、GRPO公式、SFT/RL stages、全部evaluation/ablation、Appendix A～D及model/data cards已读；evaluation toolkit链接可核但README受HF 429，内部代码不冒充已审计。Owner `TRAIN-GRPO`（Ch33，legacy Ch29），handoff `TRAIN-SFT`、`TRAIN-RLHF`、`TRAIN-PPO`与`TRAIN-DPO`。
- **Problem / previous / changed constraint:** SFT以高质量teacher trajectories离线训练，成本、语义和复现都稳定；固定temperature、length和truncation也便于控制。但更强SFT起点、数百万长reasoning demonstrations、8K→32K rollout、math/code verifier差异与overlong samples共同出现后，“多数据”与“继续RL”不再是单一旋钮，初始化、探索、长度、难度、domain order与verifier noise必须联合成为training control state。
- **Mechanism / state / flow:** prompt去重并做9-gram benchmark overlap过滤，DeepSeek-R1生成多response teacher data，Qwen2.5-Math-7B先SFT并把`rope_theta`改为1,000,000；随后用veRL做strict on-policy GRPO：global batch128、每prompt `G=8/16` rollouts、一次rollout后一次update、group reward mean/std形成sequence advantage、token-level loss、无KL。curriculum从Math 8K/16K/24K，经Code 24K/32K再回Math 32K，并按前一checkpoint全解情况移除easy prompts。data curator、SFT checkpoint、current-policy rollout、math/code verifier、temperature/length/overlong controller与artifact registry分别拥有状态；model不拥有ground truth。
- **Implementation / evaluation contract:** 论文SFT blends为36K→2.2M samples，公开dataset约3.96M rows（约2.67M math、1.30M code），但缺manifest把final checkpoint精确绑定到公开rows/order/repetition。默认评测temperature0.6、top-p0.95、max output32768、vLLM0.7.3；AIME/HMMT/BRUMO avg@64、LCB avg@8、MATH500/EvalPlus avg@4，pass@K对math每题256 outputs、code每题128 outputs并重复100次。hardware、training precision、optimizer/LR、throughput、total time/cost与SLO未披露；artifact为BF16不能反推training precision。
- **Ablation / proof boundary:** 七个SFT blends比较prompt diversity、responses-per-prompt与epoch；七点log regression的`R²=0.989`不能升级为一般scaling law。temperature0.6/0.85/1.0、8K→32K length、overlong mask、stage skip、warm-up steps、math→code transfer与K sensitivity均有作者实验。证据支持在该7B、math/code、rule-verifier contract下，强SFT与verification RL可组合，起点仍影响终点，temperature/length/truncation/difficulty是curriculum state；不证明entropy约0.3、unique prompts优先、更多epoch、math→code transfer、无KL/GRPO或stage order具有通用因果性，也不证明生产latency、安全或开放域correctness。
- **Limitations / numerical dispute:** 论文无独立Limitations；stage同时改变length、difficulty、domain与filter，code tests/math matcher有false result风险，9-gram不能排除semantic contamination，公开3.96M corpus不等于final 2.2M blend，baseline含官方与自测数字。Table 1/model card报AIME25 `64.8`、LCB v5 `57.2`，Conclusion报`63.2`、`52.8`；该headline为`Disputed numerical subclaim`，不得引用为稳定事实，但不阻断机制审计。
- **Trade-off / coexistence / disposition:** 更大SFT提高覆盖却增加teacher bias、duplicate weighting与lineage debt；strict on-policy减少policy lag却降低rollout复用，较大`G`线性放大generation/verifier/storage；progressive length扩大探索却使stage、truncation与checkpoint成为持久控制状态；删除easy prompts可能遗忘能力并把noisy verifier升级为curriculum authority。短任务、稳定demonstrations或昂贵/不可靠verifier仍适合纯SFT；需要trust region可保留PPO，只有高质量offline preference可选DPO。Ch33已覆盖grouped rollout、verifier ownership、curriculum、temperature/entropy与truncation，future仅`Refine — Existing Argument / Experimental`；当前Books Frozen。
- **Open Questions:** 冲突数字的作者更正、final training manifest、hardware/precision/optimizer/LR、entropy target跨checkpoint/reward复现、matched-data math→code attribution及evaluation toolkit event-time revision仍待核验。

### LongLLaDA

- **Identity / coverage:** `2506.14429`，v1 2025-06-17，v2 06-22、v3 11-11为forward revisions；RoPE analysis、NIAH/LongBench/RULER、sampling sensitivity与Appendix已读。Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24，handoff Ch13/22。
- **Problem / mechanism / ownership:** diffusion LLM的bidirectional denoising与AR causal decode不共享同一context extrapolation规律；稳定perplexity也不等于远距离retrieval。作者分析symmetric relative-position exposure与local perception，并以NTK-aware RoPE scaling做training-free extension；scheduler拥有mask/denoising step，position transform拥有phase，block refinement反复更新masked state。
- **Evaluation contract:** LLaDA-8B Base/Instruct、LLaDA-1.5、Dream-v0，NIAH 2K–32K、LongBench/RULER，steps 1/4/8/16，NTK lambda 4/14/31/55，对比LLaMA3-8B；hardware、precision、batch/concurrency、SLO未披露。
- **Proves / not / trade-off:** 支持作者models中stable PPL与retrieval failure共存、NTK scaling能部分恢复能力；不证明diffusion优于AR、window真正扩展或PPL代表comprehension。方案便宜但增加position distortion、locality bias、denoising/cache/rollback成本；训练长度内或causal streaming仍适合标准RoPE/AR。
- **Disposition:** `Books Pending — Refine Existing Argument Candidate / Experimental`。

### All is Not Lost / CheckFree

- **Identity / coverage:** `2506.15461`，v1 2025-06-18；v2 2026-04-04只作related evidence。算法、pipeline placement、failure assumptions、experiments与theory Appendix已读。Owner `TRAIN-CHECKPOINT` Ch35，adjacent Ch36/38。
- **Problem / mechanism / ownership:** spot/decentralized PP中checkpoint持续付网络/storage成本，redundant computation持续付compute成本。CheckFree在failure时以相邻stage参数的gradient-norm-weighted average近似重建中间stage；CheckFree+再交换首尾stage部分microbatch并复制embedding。runtime拥有topology/failure detector，neighbors提供state，trainer拥有optimizer/LR，embedding replica是额外持久state。
- **Evaluation contract:** 120M TinyStories、500M OpenWebText、1.5B RedPajama，5/10/16% failure与checkpoint/redundancy baselines；作者报告5% failure下最高约12% wall-clock改善。v1完整hardware、precision、network topology与batch未充分披露。
- **Proves / not / trade-off:** 只支持作者模拟条件中近似邻层恢复可降低部分churn区间wall-clock；不证明大模型、真实多节点failure、optimizer精确恢复或最终质量等价。省storage/compute却引入lossy reconstruction、optimizer inconsistency、stage coupling与silent quality drift；严格reproducibility与低failure仍应exact checkpoint。
- **Disposition:** `Books Pending — New Mechanism Candidate / Experimental`；no Books change authorized。

### OS-Harm

- **Identity / coverage:** `2506.14866`，v1 2025-06-17，v2 10-29为forward revision；taxonomy、tasks、harness、judge validation、model evaluation、sensitivity与Appendix已读。Owner `PLATFORM-SECURITY` Ch72，adjacent Ch66/69/73，handoff Ch78。
- **Problem / mechanism / ownership:** text refusal benchmark不能测GUI Agent是否真的造成危险environment transition。OS-Harm在OSWorld VM中提供150 executable tasks，覆盖deliberate misuse、prompt injection与model misbehavior；trace-aware judge评task success、安全和first unsafe step。environment拥有application truth，Agent只proposal，harness拥有reset/trace，judge提供observational verdict，policy gate拥有release decision。
- **Evaluation contract:** 50 tasks/category、11 apps、53 files；o4-mini、GPT-4.1、Claude3.7、Gemini2.5；human comparison的task/safety F1约0.76/0.79，并分析temperature、step budget、observation type。closed-model hardware/precision未披露，约$53/5h/3-way parallel只属于作者harness。
- **Proves / not / trade-off:** executable environment能暴露文本拒答看不到的unsafe action，judge与人类只有有限一致；不证明任一模型普遍不安全、static injection等于adaptive attacker或judge是真值。更接近deployment却成本高、环境脆弱并混合model capability与tool opportunity；大规模early screening仍适合prompt eval。
- **Disposition:** `Books Pending — Refine Existing Argument Candidate`；no Books change authorized。

## Evidence Level

- 官方 Blog / Release 只证明公开事实；未公开实现保持未知。
- arXiv v1 默认 Status: Experimental；作者实验不等于独立复现。
- 跨来源连接是本项目推断，以 Evolution Relationship 标记。

### RLVR Implicitly Incentivizes Correct Reasoning

- **Candidate / Week / Score / Source Family:** Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs / 2025-W25 / 26/30 / `ARXIV-2506.14245`。v1于2025-06-17 07:06:56 UTC公开；v2 2025-10-02只作forward revision。论文全文和EvalHub artifact可访问，但event-time commit、完整run config与raw verifier outputs未锁定。
- **Full-read Coverage:** 已读metadata、Introduction/Related Work、全部理论定义/假设/证明、CoT-Pass@K公式、五个benchmark实验、DAPO reproduction/training dynamics、Discussion/Limitations/Conclusion、Appendix data sources、三次verification aggregation、verifier prompt与人工case studies，并联查EvalHub、VERL与DAPO artifacts。
- **Original Problem / Previous Design / Changed Constraint:** final-answer exact verifier便宜、确定、可扩展，Pass@K适合衡量solution-finding；GRPO用组内binary outcome构造advantage也避免独立critic。但当问题变为“是否提高逻辑正确且完整的推理路径”，错误/不完整CoT偶然得到正确答案会使terminal outcome与reasoning quality分离，且K增大放大混淆。
- **Mechanism / Theory Boundary:** response拆为CoT `c_i`与answer `a_i`，训练reward仍只取answer correctness。若`alpha=P(answer correct|CoT correct) > beta=P(answer correct|CoT incorrect)`、group足够大且reward variance非零，简化GRPO下correct-CoT的conditional expected advantage为正、incorrect-CoT为负。评估定义同时满足CoT与answer正确的数量D，并计算`CoT-Pass@K`，同时报告`P(CA)`与`P(CC|CA)`。process judge不参与训练；结论依赖latent CoT correctness和terminal answer相关性，不能表述为RLVR直接验证了每一步。
- **State / Data and Control Flow:** checkpoint拥有generation distribution；harness拥有prompt/sampling/K；answer verifier拥有CA；DeepSeek-R1-0528-Qwen3-8B与prompt/version/RNG产生fallible CC verdict；any/majority/all aggregation拥有operating point；人工audit只覆盖抽样；training controller拥有policy/checkpoint/update state。rollouts → answer verifier → 每条CoT三次同源judge → vote aggregation → per-prompt C/D → Pass@K与CoT-Pass@K；model或judge都不拥有ground truth。
- **Implementation / Evaluation Contract:** base/post pair为Qwen2.5-32B与DAPO-Qwen-32B，测试AIME24/25、MATH-500、AMC23、Minerva，K最高1024。训练复现用Qwen2.5-32B、DAPO-Math-17k、VERL、32×AMD MI300X并运行超过两周；作者只复现到约44% Pass@1，未达到DAPO宣称的>50%。precision、global batch、optimizer/LR、max response、temperature/top-p、judge concurrency、cost与SLO均`Not Disclosed`。
- **Sensitivity / Evidence:** any/majority/all三种vote rule形成judge operating-point band，benchmark/domain slice显示AIME24/25保持post-RLVR gap，MATH-500/AMC23较弱，Minerva无改善并有domain/format mismatch。缺少独立judge family、盲人工标注集/confusion matrix、finite-G sensitivity、完整training ablation与端到端成本；三次CoT judge和最高1024 rollouts本身非常昂贵。
- **What It Proves / Does Not Prove:** 在大G简化与`alpha>beta`假设下，terminal reward的conditional advantage sign可与CoT correctness相关；作者合同下，Pass@K与CoT-Pass@K会给同一base/post pair不同结论。它不证明finite-G/clipping/KL下correct-CoT概率单调上升、RLVR创造新算法、natural-language CoT faithful、judge verdict是真值、所有domain都改善、标准Pass@K无用或RLVR普遍优于SFT/PPO/DPO。
- **Limitations / Trade-offs / Previous Design:** 三次同源judge误差可能强相关，人工核验不是独立校准集；仅数学域、静态benchmark且base training data未知。CoT-Pass@K减少偶然正确的false positive，却把judge identity、prompt、seed、vote rule和audit set变成新state；all/any/majority分别改变false-negative/false-positive operating point。只关心最终可执行结果、形式化答案或成本敏感回归时，terminal verifier + Pass@K仍是正确baseline；可信process verifier存在时应直接使用。
- **Evolution / Owner / Adjacent / Decision:** `Layering + Measurement Refinement`：Pass@K继续回答solution-finding，CoT-Pass@K增加judge-defined reasoning-path gate；理论只是对GRPO outcome-credit的受限解释，不是新RL算法。canonical owner `TRAIN-GRPO` / Ch33 / legacy Ch29，handoff `PLATFORM-EVALUATION-SYSTEM` / Ch66 / legacy Ch62；已读Ch32～34与Ch65～67。`Books Pending — Refine Existing Argument Candidate / Experimental`；Historical Books Gate关闭，本轮不改Books。
- **Open Questions:** event-time EvalHub commit与完整generation/judge config；同源judge error correlation与human confusion matrix；finite-G/all-equal group/clipping/KL下理论；不同judge family、code/open-domain与faithfulness intervention的稳定性；如何避免judge同时垄断reward和release authority。

### Guru / Cross-domain RL

- **Candidate / Week / Score / Source Family:** Revisiting Reinforcement Learning for LLM Reasoning from A Cross-Domain Perspective / 2025-W25 / 26/30 / `ARXIV-2506.14965`。v1于2025-06-17 20:24 UTC公开且无paper revision。已读38页全文、公式、五阶段data pipeline、六域reward、cross-domain analysis、17-task evaluation、Pass@k/sampling、Limitations与Appendix，并核验Reasoning360及dataset/model cards；2025-08-20 W&B logs只作forward artifact，event-time commit/full manifest未锁定。
- **Original Problem / Previous Design / Changed Constraint:** math/code RL依赖final answer或tests，单域数据、binary reward和单verifier简单易复现；扩展到Math、Code、Science、Logic、Simulation、Tabular后，答案结构、execution、pretraining exposure、difficulty、reward noise和length dynamics均不同，uniform prompt mixture不等于uniform有效gradient。
- **Mechanism / State / Flow:** 684.3K raw examples经strict-substring dedup、heuristic filter、uniform cap和policy-relative difficulty得到91.9K/约92K；difficulty由Qwen2.5-7B-Instruct与Qwen3-30B-A8B各16次pass rate按域过滤。reward按`data_source`路由到rule/symbolic matcher、sandboxed tests或1.5B entailment verifier，再用Qwen2.5-7B/32B Base直接GRPO，比较六个single-domain 3K、uniform 18K和full 92K。curator/filter/checkpoint/reward-router/verifier/sampler/trainer/evaluator分别拥有lineage、difficulty、verdict、mixture、rollout/update与selection；model不拥有ground truth。
- **Implementation / Evaluation Contract:** veRL+GRPO，AdamW `1e-6`、10-step warmup，prompt batch512、每prompt16 responses、mini-batch64、每step8 updates、temperature1.0、input4K/output8K、clip ε=.2、无KL/entropy。7B 3 epochs、32B 2 epochs，各约3天；20 nodes×8 Hopper GPUs，具体型号、precision、parallelism、network、throughput、cost与SLO未披露。offline 17 tasks、online 13 signals用于checkpoint selection；按任务avg@4/32或subsample。
- **Ablations / Evidence:** 六个3K single-domain与18K mixed在7B/32B重复；hard-filtered math提升AMC/AIME却降低HumanEval/HiTab，length按domain变化，Pass@k对scale和sampling敏感。证据只支持作者Qwen/Guru合同内transfer依赖domain/difficulty，uniform mixture可超过部分单域run，hard filtering可造成negative transfer；不证明new skill排除了pretraining exposure、template memorization、verifier adaptation或sampling shift，也不证明GRPO优于PPO/DPO/SFT、mixture可无限扩展或verifier等于真值。
- **Limitations / Numerical Dispute:** 只覆盖Qwen2.5；3K single-domain与18K mixed不data/coverage matched，online best-checkpoint混入selection；无semantic decontamination、seed variance、reward-router ablation、gradient-bearing share或Science judge human confusion matrix，Code最多8 tests且30s/10GB。Abstract称7B/32B高7.9%/6.7%，Results写9.0%/6.7%；table `43.29−35.42=7.87`只支持7.9，故为`Disputed numerical subclaim`，不升级family-level disputed。
- **Trade-offs / Previous Boundary / Evolution:** multi-domain共享rollout infrastructure，却新增reward-router/version、sandbox/judge cost、domain quota、gradient-mixture drift和checkpoint-selection debt；difficulty filter会固化policy/verifier blind spot并导致遗忘。单一目标、可靠verifier或审计优先时，单域fixed manifest仍合理。演进为`single-domain verifiable RL → typed reward routing → mixed-domain GRPO`；difficulty filtering是curriculum branch，不是越难越好。
- **Owner / Existing Coverage / Decision:** canonical owner `TRAIN-GRPO` / Ch33 / legacy Ch29；已读Ch32～34、Ch27～28和Ch66。Ch33已有group conditions、all-equal reward、curriculum/domain drift与`prompt mixture != effective gradient mixture`；Guru补六域受限证据。`Full Source Review Complete — Refine Existing Argument Candidate / Experimental / Numerical Subclaim Disputed`；Historical Books Gate关闭，本轮不改Books。
- **Open Questions:** exact event-time commit/full manifest、semantic decontamination、per-domain effective-gradient share/all-equal rate、verifier error、matched seeds、non-Qwen transfer、science human calibration与dynamic rebalance。

### Reasoning with Exploration：Entropy是credit actuator，不是correctness authority

- **Identity / Coverage:** arXiv:2506.14758 v1于2025-06-17 17:54 UTC公开；后续revision与AAAI publication只作forward evidence。25/30，`ARXIV-2506.14758`。已读v1全文、PPO/GRPO公式、method、training dynamics、reasoning analysis与Appendix A～C；无官方code/model/checkpoint/run artifact，hardware、precision、seed和duration/cost未披露。
- **Problem / Mechanism:** terminal verifier+PPO/GRPO exploitation简单稳定，direct entropy regularization也能维持随机性；但long reasoning RL可能提高Pass@1同时收窄large-K coverage。作者对sampled token计算current-policy entropy `H_t`，detach后以`min(alpha*H_t, |A_t|/kappa)`重塑advantage；`kappa>1`保留sampled-token coefficient sign，高entropy成功token强化、失败token较弱惩罚。它不对entropy反传，不是maximum-entropy RL，也不证明overall parameter-gradient direction不变。
- **State / Implementation:** rollout/old logprob、current entropy、terminal verifier、PPO critic或GRPO group statistics、alpha/kappa/clip与policy version分别拥有状态；entropy不拥有correctness。Qwen2.5 Base/Math 7B、veRL、DAPO；AdamW `1e-6`、batch512、8 samples/prompt、mini-batch256、每rollout16 updates、response 8K、train temp1、clip(.2,.28)、kappa2，GRPO alpha.4/PPO .1。
- **Evaluation / Boundary:** AIME24/25、AMC23、MATH500，eval temp.6/top-p.95，Pass@K最高256。多数作者cells改善，但Math AIME24 Pass@256从83.3降到80.0、MATH500 average仅+0.1，因此不是单调优势。无alpha/kappa sweep、factorial ablation、multi-seed/error bar或overhead；full-vocabulary entropy并非“一行代码等于零成本”。证据只支持两种7B Qwen、math RLVR与指定sampling下的受限收益，不证明high entropy causally identifies reasoning、length/keyword等于faithfulness、跨domain/scale成立或deployment utility提升。
- **Trade-offs / Evolution:** 新增每token entropy计算、hyperparameter/current-policy state、verbosity、错误高entropy token弱惩罚与verifier exploit。coverage足够、低成本/短输出时standard PPO/GRPO仍合理；direct entropy regularization是另一分支。演进为standard advantage → direct entropy gradient或detached entropy-conditioned advantage shaping。
- **Owner / Decision / Open:** `TRAIN-GRPO` Ch33 / legacy Ch29，handoff `TRAIN-PPO` Ch32与`PLATFORM-EVALUATION-SYSTEM` Ch66；已读相邻章。`Full Source Review Complete — Refine Existing Argument Candidate / Experimental`；Historical Books Gate关闭，不改Books。待核artifact、current entropy重算与overhead、alpha/kappa/group/update/length sensitivity、matched-compute seeds、code/tool transfer、causal intervention与large-K cost frontier。

### Xolver

- **Identity / coverage:** `ARXIV-2506.14234`，v1 2025-06-17；35页PDF、planner/agent/judge/verifier、episodic与shared memory、Algorithm 1、五benchmark、component/cost ablation与Appendix已读，HTML不可用不构成正文blocked。Owner `AGENT-MULTI-AGENT` Ch82，handoff Ch77/79/81。
- **Problem / mechanism / state:** single-pass reasoner把每题孤立处理，fixed-agent team也不会积累跨题经验；Xolver由planner生成动态角色，首轮从external/self episodic memory检索，后续多agent只读写固定大小shared memory，judge按score保留top-m traces，最终verifier格式化或调用外部debugger，并可把best trace写回episodic store。planner、两个memory、judge、tool runtime与verifier分别拥有state；model不拥有ground truth。
- **Evaluation contract:** GSM8K、MATH-500、AIME24/25与LiveCodeBench v5；QWQ-32B及o3-mini backbones，temperature0.2、默认3 agents/2 iterations，AIME/LCB 16/32 runs，简单集greedy；比较direct models、Search-o1、OctoTools、CheatSheet、CodeSim并消融retrieval/tools/agents/iterations/memory。closed-model hardware、token/cost、judge calibration与production tail SLO未完整披露，部分baseline引用官方数字而非matched runs。
- **Proof boundary / trade-off / decision:** 只证明作者harness内多源experience+shared-memory迭代可提高这些math/code结果；不证明judge feedback faithful、episodic write无污染、增加agents单调获益或跨开放任务成立。收益换来多次sampling、shared-error amplification、memory poisoning、judge/verifier coupling与高communication cost；简单任务仍适合single pass。`Books Pending — Refine Existing Argument Candidate / Experimental`；待artifact与独立复现。

### Stream-Omni

- **Identity / coverage:** `ARXIV-2506.13642`，v1 2025-06-16；architecture、三阶段训练、streaming inference、评测与Appendix已读。Owner `MULTIMODAL-REPRESENTATION` Ch23，handoff Ch24/54。
- **Problem / mechanism / state:** 串联ASR→LLM→TTS易丢语调且增加latency；作者把vision tokens拼接到文本序列，以底/顶层speech modules经CTC映射到共享词表，顶层speech以局部文本窗口`W=5`、wait `K=3`流式生成。text/speech token clocks与cross-attention window是显式state。
- **Evaluation contract:** 约23K小时speech，vision-text→speech-text→tri-modal三阶段；与级联/统一模型比较语音理解、视觉与speech generation。训练hardware、precision、batch、production concurrency及TTFT/TPOT未充分披露。
- **Proof boundary / trade-off / decision:** 支持作者模型中shared vocabulary+local alignment实现低等待流式speech response；不证明级联普遍落后或跨语言/噪声稳定。统一模型减少handoff却增加clock drift、错误级联和双状态rollback。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### From Bytes to Ideas / AU-Net

- **Identity / coverage:** `ARXIV-2506.14761`，v1 2025-06-17；method、公式、implementation、全部ablation与limitations已读。Owner `MODEL-TOKENIZER` Ch11，handoff Ch14/28。
- **Problem / mechanism / state:** byte-level模型消除固定tokenizer却令序列变长；AU-Net以pooling encoder、memory layers和upsampling decoder构成U形计算，把局部bytes压缩到较短latent再恢复token-level输出。pooling boundary、memory identity与upsampling alignment由model runtime拥有。
- **Evaluation contract:** DCLM English split，H100 80GB、FSDP、sequence packing、full attention、`torch.compile`静态max length；比较token/byte baselines并消融pooling、memory layer与upsampling。中文弱、FSDP overlap与静态shape均是限制。
- **Proof boundary / trade-off / decision:** 证明作者English workload内hierarchical byte computation可改善效率/质量折中；不证明tokenizer不再需要或多语言同样成立。省词表债务却引入pool boundary、information bottleneck和kernel复杂度。`Books Pending — New Mechanism Candidate / Experimental`。

### Ring-lite

- **Identity / coverage:** `ARXIV-2506.14731`，v1 2025-06-17；C3PO data、SFT checkpoint、GRPO训练、稳定性诊断、评测与Appendix已读。Owner `TRAIN-GRPO` Ch33，handoff Ch29/66。
- **Problem / mechanism / state:** 从弱或低entropy SFT起点做reasoning RL会reward collapse、length drift与gradient spikes；作者以高entropy SFT checkpoint和fixed-token-budget C3PO curriculum训练math/code/science。curator、checkpoint、rollout policy、verifier与token budget分别拥有状态。
- **Evaluation contract:** proprietary science与公开math/code混合，做SFT epoch/model、curriculum与training-dynamics消融；作者展示GRPO稳定性与benchmark变化，但hardware、precision、完整manifest、seed与成本未充分披露。
- **Proof boundary / trade-off / decision:** 支持作者合同中初始化entropy与token budget影响RL稳定性；不证明高entropy必然更好或跨domain因果成立。更广探索增加无效rollout、verifier exploit和data lineage debt；可靠窄域仍可低entropy SFT。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### AgentSynth

- **Identity / coverage:** `ARXIV-2506.14205`，v1 2025-06-17；task synthesis、persona、verification、screenshots、human validation、agent evaluation与failure analysis已读。Owner `AGENT-WORKFLOW` Ch81，handoff Ch66/78。
- **Problem / mechanism / state:** web-agent benchmark人工构造昂贵且容易泄漏答案；AgentSynth利用information asymmetry和persona生成可解子任务，再以自动verifier、screenshot filter与>80%抽样人工验证闭合。task generator不拥有truth，environment/verifier拥有可执行状态。
- **Evaluation contract:** 覆盖click/state/recovery failures与不同summary levels；不含credential/login任务，训练价值仅作future work。浏览器版本、站点漂移、完整并发/成本与event-time artifact未锁定。
- **Proof boundary / trade-off / decision:** 证明作者环境内可扩展synthesis能产出一批可执行任务；不证明task distribution代表真实生产或自动filter无偏。规模换来environment drift、verifier coupling和隐私边界。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### xbench

- **Identity / coverage:** `ARXIV-2506.13651`，v1 2025-06-16；profession design、rubrics、judge pipeline、model evaluation与limitations已读。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Problem / mechanism / state:** 通用QA分数不能代表职业任务交付；xbench以profession-aligned tasks、rule checks与rubric LLM judges拆解结果。task version、rubric、judge prompt/model与artifact共同构成evidence identity。
- **Evaluation contract:** 多模型、真实职业型任务与rule/rubric双评；hardware/precision对closed models不披露，judge-human confusion、cost/concurrency和长期重测不足。
- **Proof boundary / trade-off / decision:** 只支持作者task/rubric下的相对表现，不证明职业胜任或部署自治。真实性增加annotation/judge drift与保密成本；快速回归仍可保留静态benchmark。`Books Pending — Refine Existing Argument Candidate / Evaluation`。

### MultiFinBen

- **Identity / coverage:** `ARXIV-2506.14028`，v1 2025-06-16；34 datasets、5 languages、text/vision/audio、difficulty construction、22-model setup、cost与limitations已读。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Problem / mechanism / state:** 单语言文本金融benchmark遗漏多模态与跨区域差异；作者将34个公开集规范化，以GPT-4o和Llama3.1-70B平均标准分估difficulty。dataset/license、modality adapter、prompt与judge version是harness state。
- **Evaluation contract:** API temperature 0、本地模型vLLM，作者报告约$80K评测成本；模型hardware/precision/并发不统一，公开数据许可、domain coverage和difficulty proxy构成限制。
- **Proof boundary / trade-off / decision:** 支持统一harness暴露跨语言/模态差异；不证明平均模型分数等于内在难度或金融部署能力。覆盖度换来schema/judge/cost debt。`Books Pending — Refine Existing Argument Candidate / Evaluation`。

### Efficient Medical VIE via RL

- **Identity / coverage:** `ARXIV-2506.13363`，v1 2025-06-16；视觉信息抽取pipeline、reward、训练、evaluation、ablation与limits已读。Owner `TRAIN-GRPO` Ch33，handoff Ch23/66。
- **Problem / mechanism / state:** 医疗文档VIE格式复杂，SFT只模仿答案且难直接优化结构正确性；作者以规则/结构reward进行RL，图像、schema、prediction与verifier verdict分属数据、model与harness。
- **Evaluation contract:** 医疗VIE数据、SFT/RL baselines及组件消融；作者设置未完整公开真实医院distribution、privacy、hardware、precision、batch与production SLO。
- **Proof boundary / trade-off / decision:** 仅证明作者静态dataset内structured reward可改善抽取指标；不证明临床正确、安全或跨模板泛化。更强格式约束可能reward hack并牺牲语义召回；高风险场景仍需规则+human review。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### Align Your Flow

- **Identity / coverage:** `ARXIV-2506.14603`，v1 2025-06-17；AYF-EMD/LMD公式、autoguidance、training、ImageNet512/text-image/user study、multi-step/one-step sensitivity已读。Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24。
- **Problem / mechanism / state:** 多步flow matching质量高但sampling慢，直接一步蒸馏会错配teacher trajectory；AYF对齐student flow map与teacher transport，并以EMD/LMD和autoguidance约束。teacher trajectory、noise/sample pair与student map由distillation pipeline拥有。
- **Evaluation contract:** ImageNet512和text-to-image，对比distillation baselines，含step数、objective与guidance ablation/user study；一阶略弱，多步更稳，hardware/precision/并发/SLO不完整。
- **Proof boundary / trade-off / decision:** 支持作者image workloads中aligned flow distillation改善少步生成；不证明一步等价teacher或跨video/text成立。低latency换来teacher dependence、transport approximation与mode bias。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### Guaranteed Guess

- **Identity / coverage:** `ARXIV-2506.14606`，v1 2025-06-17；CISC-to-RISC任务、data generation、unit-test verifier、training/eval/limitations已读。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66，handoff Ch79。
- **Problem / mechanism / state:** LLM代码生成的自然语言“置信”不能提供执行保证；作者把复杂instruction transpile为受限primitive program，以unit tests定义bounded guarantee。spec、compiler flags、tests、sandbox与artifact version拥有truth contract。
- **Evaluation contract:** LLaMA-Factory、ZeRO3、Liger、FA2、vLLM；single A100 40GB、32.7K context、deterministic decoding，比较-O2等设置；缺compiler/symbolic baselines，`36 requests/s`口径不清。
- **Proof boundary / trade-off / decision:** guarantee只等于测试集内通过，不是program correctness theorem。受限ISA改善验证却降低表达力并引入test blind spot/compile drift；小任务可继续直接生成。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### Optimizing Length Compression

- **Identity / coverage:** `ARXIV-2506.14755`，v1 2025-06-17；LC-R1双reward、两模型七benchmark、training/evaluation与ablation已读；论文无独立limitations。Owner `TRAIN-GRPO` Ch33，handoff Ch66。
- **Problem / mechanism / state:** correctness-only RL会奖励冗长CoT；LC-R1把correctness与compression reward联合，policy、reference length、verifier和weight schedule是控制state。
- **Evaluation contract:** 两个模型、七个数学/推理benchmark；作者报告约50%长度削减伴随约2% accuracy下降，并比较reward variants。hardware、precision、seed、latency与token-price operating point未完整披露。
- **Proof boundary / trade-off / decision:** 支持作者合同中的accuracy-length Pareto，不证明短CoT更faithful或所有任务同权重最优。省token换来premature answer、hard-case退化和length gaming；高风险任务仍可保留长推导。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### Taming Polysemanticity

- **Identity / coverage:** `ARXIV-2506.14002`，v1 2025-06-16；GBA理论、稀疏混合假设、SAE实现、Qwen2.5-1.5B实验、TopK/L1 baselines与Appendix已读。Owner `MODEL-INTERPRETABILITY` Ch17。
- **Problem / mechanism / state:** SAE feature在polysemantic activation上混合概念，单一sparsity penalty难控制bias；GBA以bias adaptation调节activation sparsity。encoder/decoder weights、bias与feature activation由probe拥有，不等于base model的causal state。
- **Evaluation contract:** Qwen2.5-1.5B、L1/TopK对比及sparsity/reconstruction/interpretability指标；定理依赖sparse-mixture假设，跨层/大模型/causal intervention与hardware成本不足。
- **Proof boundary / trade-off / decision:** 支持受限假设与作者模型中bias control改善SAE折中；不证明feature是唯一语义或解释具有因果性。稀疏度可控却增加超参和feature instability；简单probe仍适合诊断。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### Sekai

- **Identity / coverage:** `ARXIV-2506.15675`，v1 2025-06-18；data collection、codec、caption/depth/camera pipeline、YUME experiment与limitations已读。Owner `MULTIMODAL-WORLD-MODELS` Ch25，handoff Ch23/66。
- **Problem / mechanism / state:** world-model训练缺少大规模first-person motion data；Sekai收集5000+小时、101国/750城YouTube+game视频，以TransNetV2、PyNVideoCodec/CV-CUDA、H265 720p30 4Mbps处理，GPT-4o/Qwen2.5-VL/MegaSaM/VideoDepthAnything生成metadata/caption/camera。
- **Evaluation contract:** 约600h trajectory、400h high-quality subset；YUME仅用小subset，部分视频无可靠trajectory。版权、来源偏差、caption/depth error、训练规模不足是明确限制。
- **Proof boundary / trade-off / decision:** 证明可构建大规模ego-video asset pipeline，不证明dataset等于可控world dynamics或全球代表性。规模换来provenance、自动label与privacy debt；高质量control data仍需精采。`Books Pending — Refine Existing Argument Candidate / Dataset`。

### ProtoReasoning

- **Identity / coverage:** `ARXIV-2506.15211`，v1 2025-06-18；PDF、Prolog/PDDL prototype construction、interpreter verifier、training、logical/planning/MMLU/AIME evaluation与Appendix已读。Owner `TRAIN-DATA` Ch27，handoff Ch33/79。
- **Problem / mechanism / state:** reasoning traces难验证且人工合成昂贵；作者从symbolic prototypes实例化任务，用interpreter验证答案再生成可扩展synthetic curriculum。prototype、instance generator、interpreter和manifest分别拥有state。
- **Evaluation contract:** logical/planning、MMLU、AIME及data-scale/format comparisons；hardware、precision、contamination、seed和真实语言分布匹配不完整。
- **Proof boundary / trade-off / decision:** 支持symbolic generator提供低噪可执行监督并产生transfer；不证明synthetic reasoning等于自然任务或排除template memorization。可验证性换来coverage bias与generator blind spot。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### Embodied Web Agents

- **Identity / coverage:** `ARXIV-2506.15677`，v1 2025-06-18、v2 06-20、v3 07-29；v1 owner，后续revision只作演进证据。统一3D/web simulation、tasks、datasets、evaluation与artifact已读。Owner `AGENT-WORKFLOW` Ch81，handoff Ch26/66。
- **Problem / mechanism / state:** browser benchmark与embodied benchmark各自隔离，无法测试跨界workflow；环境统一indoor/outdoor 3D与web interfaces，覆盖cooking/navigation/shopping/tourism/geolocation。simulator与web backend拥有truth，agent只拥有observation/action proposal。
- **Evaluation contract:** 多任务、多agent baseline与成功率/轨迹；后续revision不能冒充v1条件，真实网页漂移、sim-to-real、hardware/latency与安全边界不足。
- **Proof boundary / trade-off / decision:** 支持统一harness暴露跨环境planning负担，不证明simulator performance迁移真实世界。统一接口增加state synchronization、reset与opportunity confound；单域回归仍更稳定。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### SwarmAgentic

- **Identity / coverage:** `ARXIV-2506.15672`，v1 2025-06-18；language-driven particle-swarm algorithm、failure-driven adaptation、MGSM/creative/NaturalPlan/TravelPlanner、ablation与limitations已读。Owner `AGENT-MULTI-AGENT` Ch82。
- **Problem / mechanism / state:** fixed multi-agent角色/拓扑无法适配任务；作者以particle-swarm搜索agent prompts与collaboration structure，并依据failure feedback更新。orchestrator拥有population/topology/budget，agents仅拥有局部context。
- **Evaluation contract:** 四类任务与prompt/topology/feedback ablations；无强priors，text-only，硬件/并发/communication cost和多seed不足。
- **Proof boundary / trade-off / decision:** 支持作者tasks中联合搜索agent与协作结构可胜fixed baselines；不证明增加agent单调获益。自适应换来communication tax、shared-error amplification和不可复现拓扑。single-agent headroom高时仍应单Agent。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### Semantically-Aware Rewards

- **Identity / coverage:** `ARXIV-2506.15068`，v1 2025-06-18；PrefBERT reward、GRPO integration、ROUGE/BERTScore baselines、task evaluation与limitations已读。Owner `TRAIN-GRPO` Ch33，handoff Ch66。
- **Problem / mechanism / state:** lexical reward无法识别语义等价，多维quality又难用单规则表示；作者以小型PrefBERT产生semantic multidimensional reward供GRPO。reward model/version/prompt与policy分别拥有state。
- **Evaluation contract:** 窄域generation tasks、lexical/semantic baselines与reward ablation；无7B reward model、跨域human calibration、hardware/precision/cost与adversarial robustness。
- **Proof boundary / trade-off / decision:** 仅支持作者任务内learned semantic reward优于部分lexical proxy；不证明reward是真值。更柔性却新增reward hacking、model bias与版本漂移；可执行任务仍优先rule verifier。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### SciVer

- **Identity / coverage:** `ARXIV-2506.15569`，v1 2025-06-18；expert annotation、paragraph/table/chart evidence、RAG/VLM setup、judge、error analysis与limitations已读。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66，handoff Ch75。
- **Problem / mechanism / state:** scientific claim verification不能只查纯文本；SciVer绑定claim与paragraph/table/chart evidence。corpus/index、retriever、VLM filter、evidence set和verdict必须分开版本化。
- **Evaluation contract:** CS/arXiv专家数据；OpenAI embedding RAG recall@5约81%，Qwen2.5-VL oracle/filter比较；限制为CS-only、遗漏equations/images、annotation昂贵，hardware/precision/并发/SLO不完整。
- **Proof boundary / trade-off / decision:** 支持多模态evidence retrieval/verification可作为独立harness；不证明verdict是科学真值或跨领域泛化。证据增强降低无依据回答却增加retrieval miss、judge依赖和成本。`Books Pending — Refine Existing Argument Candidate / Evaluation`。

### Truncated PPO

- **Identity / coverage:** `ARXIV-2506.15050`，v1 2025-06-18；truncation、Extended GAE、successive batching、training config、ablation与limitations已读。Owner `TRAIN-PPO` Ch32，handoff Ch33/39。
- **Problem / mechanism / state:** long rollout超过worker window导致PPO等待和memory压力；T-PPO截断policy rollout，critic只对finished trajectories做MC，并以`V(s_l)=V(s_{l-1})`近似边界接续。unfinished trajectory、bootstrap state与batch queue归trainer/runtime所有。
- **Evaluation contract:** Qwen2.5-32B、batch512 prompts×16、mini-batch512、max24K/window8K、无KL、H800 BF16、AIME24/DAPO-Math；作者报告约2.5×吞吐、60% wall-clock reduction，仅单模型/窄域。
- **Proof boundary / trade-off / decision:** 支持作者系统内截断+successive batching减少straggler；不证明value boundary假设无偏或普遍保质。吞吐换来staleness、credit truncation与unfinished-state debt；短/均匀rollout仍适合标准PPO。`Books Pending — New Mechanism Candidate / Experimental`。

### MoTE

- **Identity / coverage:** `ARXIV-2506.14435`，v1 2025-06-17；ternary MoE upcycling、shared/routed precision、initialization/recipe、Qwen2.5 0.5/1.5/3B实验与ablation已读。Owner `MODEL-MOE` Ch21，handoff Ch23/49。
- **Problem / mechanism / state:** multimodal dense model扩容昂贵；MoTE把部分dense weights upcycle为ternary experts，并保留shared/routed branches。router、expert placement、precision metadata与load balance由model/runtime共同拥有。
- **Evaluation contract:** 1+4或0+4 experts/top-k variants、shared/routed precision与training recipe ablation；小模型、作者tasks，缺理论、large-scale hardware/communication/tail SLO。
- **Proof boundary / trade-off / decision:** 支持作者规模中ternary experts形成容量/成本折中；不证明量化MoE普遍胜dense。省memory/compute却增加routing、scale calibration与expert imbalance。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### Evolutionary Caching / ECAD

- **Identity / coverage:** `ARXIV-2506.15682`，v1 2025-06-18；binary cache mask、genetic search、calibration、baselines、ablation与limitations已读。Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24，handoff Ch45/54。
- **Problem / mechanism / state:** diffusion cache policy手工固定且不同steps/layers敏感；ECAD对off-the-shelf model搜索binary reuse mask，在quality/latency Pareto上选择policy。calibration prompts、population、mask、cached tensor identity与generation schedule均是state。
- **Evaluation contract:** 100 prompts×10、population72、100 generations；ImageReward/FID/CLIP/latency，并做prompt/population/image ablations。training-free但搜索成本高，metric overfit与硬件依赖未消失。
- **Proof boundary / trade-off / decision:** 支持作者diffusion models中search可找到优于手工mask的局部Pareto；不证明跨prompt/model/hardware稳定。加速换来stale-cache error、calibration overfit和决策不可解释；固定workload仍可静态policy。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### GenRecal

- **Identity / coverage:** `ARXIV-2506.15681`，v1 2025-06-18；recalibrator、regularization、distillation pipeline、InternVL2.5 78B→8/4/2/1B、cosine ablation与evaluation已读。Owner `TRAIN-DISTILLATION` Ch29，handoff Ch23。
- **Problem / mechanism / state:** large-to-small VLM蒸馏直接对齐logits会把teacher scale与student capacity mismatch传入；GenRecal用recalibrator和regularization调整target。teacher checkpoint、recalibrator、student与loss weights独立版本化。
- **Evaluation contract:** InternVL2.5 family多scale、多个multimodal benchmark和cosine/regularization ablation；论文无充分limitations，hardware、precision、data lineage、latency/SLO未完整披露。
- **Proof boundary / trade-off / decision:** 支持作者family内recalibrated distillation改善部分student；不证明teacher knowledge无损传递或跨family成立。提高student fit却增加teacher bias、extra module与tuning debt；同scale/充足data可直接distill。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### Show-o2

- **Identity / coverage:** `ARXIV-2506.15564`，v1 2025-06-18；spatial-temporal fusion、understanding/image/video generation、CFG/inference/stage ablation与limitations已读。Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24，handoff Ch23/25。
- **Problem / mechanism / state:** unified multimodal model难同时保留high-level semantics与low-level visual detail；Show-o2融合spatial/temporal multi-scale features，并共享理解与生成主干。modality tokens、noise state、fusion features与generation schedule为model state。
- **Evaluation contract:** 理解、image/video generation与stage/CFG/inference ablations；限制包括text rendering、小物体、resolution、misuse/copyright，hardware、precision、并发与SLO不完整。
- **Proof boundary / trade-off / decision:** 支持作者模型中fusion路线兼顾多任务；不证明统一模型优于专用pipeline。共享表示减少模型数却增加objective interference、mutable generation state和安全面。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### RE-IMAGINE

- **Identity / coverage:** `ARXIV-2506.15455`，v1 2025-06-18；computation-graph mutation、Bi-CounterFactual、GSM8K/CruxEval/Loop、mutation/ICL/complexity ablation与limitations已读。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Problem / mechanism / state:** benchmark静态题面让模型依赖semantic cues与memorization；RE-IMAGINE从symbolic computation graph生成语义等价或反事实变体。base graph、mutation seed、rendering与answer interpreter共同定义task identity。
- **Evaluation contract:** GSM8K、CruxEval、Loop及mutation level/composition、ICL、complexity ablation；不覆盖开放世界，surface naturalness和graph generator bias有限制。
- **Proof boundary / trade-off / decision:** 支持counterfactual mutation暴露cue brittleness；不证明所有下降来自缺乏reasoning。更强contamination resistance换来synthetic distribution shift与generator monoculture；原题仍适合生态效度。`Books Pending — Refine Existing Argument Candidate / Evaluation`。

## Recovered 2025-06-19～22 Source Families

### LazyEviction

- **Identity / coverage:** `ARXIV-2506.15969`，v1 2025-06-19；importance recurrence、observation window、timestamp/MRI、eviction algorithm、GSM8K/MATH500实验、ablation与limitations已读。Owner `INFER-KV-CACHE` Ch45。
- **Problem / mechanism / state:** FullKV正确但显存线性增长，static heavy-hitter规则不能适应token价值变化；LazyEviction以近期attention观察窗更新token importance和most-recent-importance timestamp，再以MRI优先淘汰。KV block、importance、timestamp与eviction policy归runtime拥有。
- **Evaluation contract:** DeepSeek-R1-Distill-Llama-8B、Qwen-7B，GSM8K/MATH500，FullKV/H2O/TOVA/RaaS，50%/65% retention，并消融window/alpha/importance；hardware、precision、concurrency、TTFT/TPOT与tail SLO不充分。
- **Proof boundary / trade-off / decision:** 支持作者reasoning workload内temporal importance改善quality-memory折中；不证明跨长上下文任务或生产tail稳定。省KV换来metadata、误删和不可逆context loss；短上下文仍用FullKV。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### EvoLM

- **Identity / coverage:** `ARXIV-2506.16029`，v1 2025-06-19；>100 models、pretrain/CPT/SFT/PPO-RLVR、in/out-domain evaluation、artifact与limitations已读。Owner `TRAIN-PRETRAINING` Ch28，handoff Ch29/33。
- **Problem / mechanism / state:** 单一final checkpoint无法解释能力如何随训练阶段演化；EvoLM系统化保存1B/4B models及stage lineage，比较pretrain→CPT→SFT→PPO。dataset mixture、checkpoint、objective与evaluation manifest是演化state。
- **Evaluation contract:** 从头训练100+模型，in/out-domain、多阶段与training-budget curves；限制为≤4B、reasoning-centric、只测PPO类RL，硬件/精度/成本与大模型外推有限。
- **Proof boundary / trade-off / decision:** 支持作者scale中diminishing return、forgetting与CPT bridge等阶段效应；不证明普适scaling law。全链实验提高因果可读性却成本高且stage交互多。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### SparseLoRA

- **Identity / coverage:** `ARXIV-2506.16500`，v1 2025-06-19；SVD sparsity estimator、dynamic sparse gradient branch、LoRA integration、LLaMA2/3实验、iso-FLOP/LR/layer-token-step sensitivity已读。Owner `TRAIN-LORA` Ch30。
- **Problem / mechanism / state:** dense base-gradient计算使LoRA仍有activation/compute cost；SparseLoRA以training-free SVD estimator选择main-branch sparse updates，LoRA branch保持dense。mask、layer/token/step schedule与adapter version归trainer拥有。
- **Evaluation contract:** LLaMA2/3 7B/13B、多datasets、A6000/A100，作者最高约1.6×；含LR sweep与iso-FLOP，但无独立limitations、production kernel/communication/SLO不完整。
- **Proof boundary / trade-off / decision:** 支持作者tasks中动态稀疏可降低部分训练成本而保质量；不证明所有layer/token可安全跳过。加速换来mask estimation、irregular kernel与optimization drift；小adapter/compute充足时dense LoRA更稳。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### SCALE Optimizer

- **Identity / coverage:** `ARXIV-2506.16659`，v1 2025-06-20；column-normalized SGD、last-layer momentum、memory analysis、C4 LLaMA scaling、baselines与limits已读。Owner `TRAIN-PRETRAINING` Ch28，handoff Ch39。
- **Problem / mechanism / state:** Adam states占显存，低内存optimizers常损失稳定性；SCALE按列归一梯度并只对last layer维护momentum，缩小optimizer state。parameter group、column norm与momentum owner为trainer。
- **Evaluation contract:** LLaMA 60M–1B，BF16、seq256、batch512；7B单次run用8×H200 141GB/19.7B tokens，对比Adam/Muon/GaLore/Fira/APOLLO/SWAN，部分baseline因代码不可用引用结果；作者报告35–45% memory reduction。
- **Proof boundary / trade-off / decision:** 支持作者C4合同中的memory-quality折中，不证明7B以上、多objective或distributed稳定。省state换来scale sensitivity、最后层特例与基线公平性风险；AdamW仍是稳健默认。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### GRPO-CARE

- **Identity / coverage:** `ARXIV-2506.16141`，v1 2025-06-19；CARE objective、EMA reference、vision RL pipeline、SEED-Bench-R1设置、ablation与Appendix已读。Owner `TRAIN-GRPO` Ch33，handoff Ch23。
- **Problem / mechanism / state:** binary answer reward在group全错/全对时无gradient，multimodal RL又易漂移；GRPO-CARE对correct groups加入EMA-reference likelihood bonus，去掉KL。current/EMA policy、answer verifier与group statistics是trainer state。
- **Evaluation contract:** Qwen2.5-VL-7B，SEED-Bench-R1 50,269 train与多个val splits，16 frames，resolution 128×28×28，SFT/GRPO 6K pilot、rule answer reward；hardware/precision/cost与跨dataset不足。
- **Proof boundary / trade-off / decision:** 支持作者vision benchmark内EMA consistency缓解部分group degeneracy；reference likelihood不是human truth，不证明无KL普遍稳定。新增EMA lag、confirmation bias与reward coupling；有可靠process reward时可不用。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### LMR-BENCH

- **Identity / coverage:** `ARXIV-2506.17335`，v1 2025-06-19；28 tasks/23 NLP papers、masked functions、Docker tests、LLM judge、OpenHands evaluation、failure taxonomy与limitations已读。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66，handoff Ch81。
- **Problem / mechanism / state:** research coding benchmark常只测短函数或文本答案；LMR-BENCH遮蔽论文repo中的真实函数，让Agent在repository context中修复并以Docker unit tests+judge验证。repo commit、environment、tests与judge共同构成evidence identity。
- **Evaluation contract:** 9 categories、GPT-4o/4.1/o4-mini与agents；agents unit-test accuracy更低，LLM/human agreement62.5%、contradiction9.5%。PhD annotation昂贵、规模有限，hardware/concurrency/cost不完整。
- **Proof boundary / trade-off / decision:** 支持真实repo任务暴露harness/agent失败，不证明unit tests完备或judge等于真值。生态度换来环境脆弱和维护成本；小函数benchmark仍适合快速回归。`Books Pending — Refine Existing Argument Candidate / Evaluation`。

### TabArena

- **Identity / coverage:** `ARXIV-2506.16791`，v1 2025-06-20；living benchmark、51-task selection、16-model/HPO/eval/ensemble设计、results与limitations已读。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Problem / mechanism / state:** tabular benchmark固定少数datasets和default configs，不能区分模型/HPO/ensemble贡献；TabArena把dataset split、200 random configs、hardware/time budget与ensemble统一版本化。
- **Evaluation contract:** 51 tasks从1053筛选，约25M runs/约15年累计wall time；限制为固定200 configs、hardware/time comparability、严格dataset筛选与无feature engineering。
- **Proof boundary / trade-off / decision:** 支持harness内model/HPO/data/eval分解，不证明leaderboard顺序跨budget稳定。公平性提高却带来巨量compute与selection bias；小规模平台仍需cost-aware subset。`Books Pending — Refine Existing Argument Candidate / Evaluation`。

### LLM Safety under Latent Perturbations

- **Identity / coverage:** `ARXIV-2506.16078`，v1 2025-06-19；ASA/NLL probe、LAPT、ASABench、12-model evaluation、seed/normalization/judge ablations与Appendix已读。Owner `PLATFORM-SECURITY` Ch72，handoff Ch17/66。
- **Problem / mechanism / state:** input-output refusal测试看不到hidden-state局部脆弱性；ASA在指定layer/token注入归一化activation perturbation，以原安全response NLL探测脆弱方向；LAPT在fragile layers加入扰动训练。threat model、layer/step、perturbation与judge version均为security state。
- **Evaluation contract:** AdvBench前100 prompts、12 open models、43,200 samples，QwQ-32B judge；ASABench 4,862 validated cases，60/40 split，并测MASR/PASR/LASR与general capability。judge相关、白盒access和有限prompts限制外推。
- **Proof boundary / trade-off / decision:** 支持aligned models对特定latent perturbation不稳且LAPT提高该attack robustness；不证明表面alignment“无效”或现实攻击同威胁模型。鲁棒性换来额外training、attack overfit与能力风险。`Books Pending — Refine Existing Argument Candidate / Security Experimental`。

### Mathematical Proof Litmus Test

- **Identity / coverage:** `ARXIV-2506.17114`，v1 2025-06-20；200 proof problems、10 error categories、model/judge setup、manual analysis、limitations与Appendix已读。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Problem / mechanism / state:** final-answer benchmark掩盖proof validity；该benchmark把完整proof作为artifact，以formal/mathematical rubric分类logical gaps、unsupported steps和circularity。problem version、reference proof、judge与human adjudication分离。
- **Evaluation contract:** 200题、多advanced reasoning models，某些模型严格correct低于20%；未披露closed-model hardware/precision，题域/标注规模与judge reliability限制外推。
- **Proof boundary / trade-off / decision:** 证明final answer与proof correctness可显著分离；不证明模型总体数学能力或10类taxonomy完备。强过程审计更昂贵且judge争议大；可执行答案仍适合first-pass筛查。`Books Pending — Refine Existing Argument Candidate / Evaluation`。

### Tower+

- **Identity / coverage:** `ARXIV-2506.17080`，v1 2025-06-20；CPT→SFT→preference→RLVR training、2B/9B/72B models、multilingual evaluation、stage ablation与limitations已读。Owner `TRAIN-PRETRAINING` Ch28，handoff Ch29/31/33。
- **Problem / mechanism / state:** translation specialization提升目标任务却易侵蚀general capability；Tower+按CPT、SFT、preference、RLVR分阶段，并保留general/translation双评。dataset mixture、stage checkpoint、reward/verifier和language sampling是training state。
- **Evaluation contract:** 2B/9B/72B、多语言translation与general benchmarks，比较stage贡献；vendor/author results受data、judge、hardware/precision与cost未完全披露限制。
- **Proof boundary / trade-off / decision:** 支持作者family中分阶段post-training改善specialization/generalization折中；不证明固定stage order普适。能力增益换来forgetting、language imbalance与stage-selection debt；单域小模型仍可直接SFT。`Books Pending — Refine Existing Argument Candidate / Experimental`。

### SGLang GB200 PD + Large-scale EP

- **Identity / coverage:** `SGLANG-GB200-PD-EP-2025-06-16`，官方工程报告first-public 2025-06-16；Methods、end-to-end setup、batch-size ablation、hardware topology、reproduction instructions与Future Work已读。Owner `INFER-DISTRIBUTED-RUNTIME` Ch55，handoff Ch49/52/54。
- **Problem / previous / mechanism / state:** H100跨节点RDMA下，TP与communication overlap是合理默认；GB200 NVL72扩大NVLink domain、memory capacity和bandwidth后，旧overlap/placement假设改变。作者组合Blackwell DeepGEMM/DeepEP/FMHA/CUTLASS MLA/Mooncake、PD disaggregation与large-scale EP；prefill/decode pool、expert placement、KV transfer与batch queue由runtime拥有。
- **Evaluation contract:** DeepSeek 671B，14个GB200 NVL72 nodes中12 decode、其余prefill；input/output 2000/100，比较复用的H100 baseline，作者报告2.5–3.4× per-GPU decode throughput区间并做batch-size ablation。baseline含模拟MTP且未matched全套hardware/cost，small batch、prefill、latency与未饱和kernel均明确未优化。
- **Proof boundary / trade-off / decision:** 只证明作者饱和decode合同中hardware/topology-aware PD+EP co-design可显著改变Pareto，不证明GB200、PD或EP各自的独立因果收益，也不证明相同ITL即production SLO。收益换来typed pools、KV transfer、expert routing与failure recovery state；小batch/单节点仍可TP。`Books Pending — Refine Existing Argument Candidate / Engineering Case`。

### TensorRT-LLM v0.20.0

- **Identity / coverage:** `TRTLLM-V0.20.0-2025-06-19`，official release/tag first-public 2025-06-19；release notes、linked PR/code paths、breaking/API/infrastructure changes、known issues与benchmark support已审。Owner `INFER-EXECUTION-ENGINE` Ch50，handoff Ch45/52/55。
- **Problem / previous / mechanism / state:** 单体static TensorRT workflow曾以稳定graph与kernel性能为目标；多模态、LoRA、MLA KV reuse、disaggregated serving与PyTorch workflow要求per-request state和更动态的scheduler。v0.20公开piecewise CUDA Graph、chunked context、MLA KV reuse、KV-cache-aware router、overlap scheduler default、multi-LoRA+TP与multimodal request field；release/version、dependency ABI、router/cache identity与scheduler config归runtime/platform所有。
- **Evaluation contract:** release notes证明feature/code availability与breaking changes，不提供一套matched model、hardware、precision、length、batch、concurrency、TTFT/TPOT/tail-SLO benchmark；依赖锁定CUDA12.9、TensorRT10.10、PyTorch2.7、NCCL2.25.1，known issue含RTX Pro 6000 multi-GPU。
- **Proof boundary / trade-off / decision:** 证明这些公开接口/代码在v0.20成为版本合同，不证明任一feature普遍提速或生产稳定。动态能力增加cache/router/scheduler/ABI migration与rollback debt；静态single-model deployment仍可旧workflow。`Weekly Version Fact + Books Pending — Refine Existing Argument Candidate where mechanism already owned`。

## Low-score Closure Ledger

- **既有5项:** ImmerseGen 19、GMT 19、PictSure 18、SonicVerse 17与Ray 2.47.1 16均已核对title/author或release owner、v1/release date、六维Total与拒绝理由；分别只是窄域world/embodied/representation/audio案例或patch fact，机制证据不足20分门槛。
- **新增6项:** DualTHOR 19（`2506.16012`，双臂humanoid simulator窄域）、Hunyuan3D 2.5 19（`2506.16504`，vendor shape+PBR case）、Vision-guided Chunking 18（`2506.16035`，有限视频分块实验）、Multi-hop RAG Generation 17（`2506.16037`，窄benchmark方法）、OmniReflect 19（`2506.17449`，reflection case）与MEXA 19（`2506.17113`，局部evaluation方法）均已核对v1 2025-06-19/20、摘要/正文可得边界和低分原因；不因“低分”冒充全文机制结论。
- **状态边界:** 上述11项均为`No Change / Weekly Only`，不是blocked、pending或Books候选。后续若出现独立复现、正式artifact或跨workload机制证据，按同一Source Family重开，不新增重复owner。

Candidate Evidence Gate：`Passed`。58个owner rows中47个20+全部完成Full Source Review，11/11低分闭合；普通pending 0、blocked 0、family-level disputed 0，另有2项numerical subclaim dispute。Historical Books Gate保持关闭。

## Cross-Week Deduplication

- 同一技术后续 revision 与工程集成回链首次公开周。
- 新版本不覆盖旧方案；年度索引记录 old constraint → new mechanism → new failure mode。
- CRITICTOOL（2506.13977）与FedNano（2506.14824）v1分别为06-11与06-12，回拨W24，不计W25 owner。
- HF display feed暴露的CoMemo、VideoMolmo与MoE-meets-ICRL回拨W23；其余06-09～15 owner回拨W24，不能因W25 feed出现而重复评分。
- DeepResearch Bench（2506.11763）、Feedback Friction（2506.11930）、Scaling Test-time Compute for Agents（2506.12928）、Wait/NoWait（2506.08343）、EmoNet Voice（2506.09827）与ChartIR（2506.14837，feed日期需以v1 metadata为准）均由first-public date回拨W24；W25只保留dedup ledger，不重复打分。
- vLLM v0.9.1官方tag为2025-06-10，回拨W24；不能因06-16以后使用/issue记录而改写release owner week。

## Knowledge Tree Position

- Model/Training owner：`MODEL-TOKENIZER`、`MODEL-MOE`、`MODEL-INTERPRETABILITY`、`TRAIN-DATA`、`TRAIN-PRETRAINING`、`TRAIN-LORA`、`TRAIN-PPO`、`TRAIN-GRPO`、`TRAIN-CHECKPOINT`。
- Multimodal/Inference owner：`MULTIMODAL-REPRESENTATION`、`MULTIMODAL-GENERATIVE-PARADIGMS`、`MULTIMODAL-WORLD-MODELS`、`INFER-KV-CACHE`。
- Runtime/Platform/Agent owner：`INFER-KV-CACHE`、`INFER-EXECUTION-ENGINE`、`INFER-DISTRIBUTED-RUNTIME`、`PLATFORM-EVALUATION-SYSTEM`、`PLATFORM-SECURITY`、`AGENT-PLANNING`、`AGENT-WORKFLOW`、`AGENT-MULTI-AGENT`；跨章只保留handoff，不复制owner机制。

## Recommended Action

- W25 Candidate Evidence Gate已闭合；年度Historical Evidence Gate打开后，按Source Family disposition而非论文数量进入Books Integration。
- 优先重审`TRAIN-GRPO`、`PLATFORM-EVALUATION-SYSTEM`、`MULTIMODAL-GENERATIVE-PARADIGMS`与`INFER-KV-CACHE`的owner边界；numerical subclaim dispute不得进入稳定结论。

## Event-Date Daily Decision

历史回填不创建 Daily；事件与证据边界直接保留在本 Weekly。

## Books Integration Decision

`Books Frozen — Historical Gate Closed`。47个Full Source Review的owner/disposition只是未来Source-Family Gate输入；本轮不修改Books、ROADMAP或DECISIONS，也不把W25通过误写成年度Gate通过。


## Ignored Noise

- 忽略旧内容重发、二手转述、缺条件 benchmark 与纯可用性更新。
- discovery 排名和引用量不替代 novelty、reliability 或 longevity。

## Repository Changes

- 将旧2项扩展为58个唯一owner identity，写入47项20+与11项低分评分账本。
- 完成47/47 Full Source Review、11/11低分closure、固定来源与06-19～22 replay、跨周回拨和owner mapping；仅修改本Weekly文件。

## Open Questions

- AceReason-Nemotron 1.1与Guru的冲突headline能否由作者更正？RLVR Correct Reasoning的event-time EvalHub、judge calibration与finite-group条件能否恢复？
- LazyEviction、SparseLoRA、SCALE、T-PPO与ECAD在matched hardware、precision、concurrency和tail-SLO下能否独立复现？
- CheckFree的近似恢复如何在真实cluster、optimizer state与quality drift下验证？

## Sources

- MiniMax-M1 — https://arxiv.org/abs/2506.13585（First Public: 2025-06-16；Accessed: 2026-07-31）
- Gemini 2.5 Pro/Flash GA — https://blog.google/products-and-platforms/products/gemini/gemini-2-5-model-family-expands/（First Public: 2025-06-17；Accessed: 2026-07-31）
- Essential-Web v1.0 — https://arxiv.org/abs/2506.14111（v1: 2025-06-17；Accessed: 2026-08-22）
- Ego-R1 — https://arxiv.org/abs/2506.13654（v1: 2025-06-16；Accessed: 2026-08-22）
- AceReason-Nemotron 1.1 — https://arxiv.org/abs/2506.13284（v1: 2025-06-16；Strict Full Source Review Complete）
- AceReason-Nemotron 1.1 official model — https://huggingface.co/nvidia/AceReason-Nemotron-1.1-7B
- AceReason 1.1 SFT dataset — https://huggingface.co/datasets/nvidia/AceReason-1.1-SFT
- RLVR Implicitly Incentivizes Correct Reasoning — https://arxiv.org/html/2506.14245v1（v1: 2025-06-17；Full Source Review Complete；Accessed: 2026-08-22）
- RLVR Correct Reasoning evaluation artifact — https://github.com/ysy-phoenix/evalhub（event-time commit not pinned；Accessed: 2026-08-22）
- LongLLaDA — https://arxiv.org/abs/2506.14429（v1: 2025-06-17；Accessed: 2026-08-22）
- Xolver — https://arxiv.org/abs/2506.14234（v1: 2025-06-17；Full Source Review Complete）
- Reasoning with Exploration — https://arxiv.org/abs/2506.14758（v1: 2025-06-17；Full Source Review Complete — Experimental / Entropy-actuator Boundary；Accessed: 2026-08-22）
- Stream-Omni — https://arxiv.org/abs/2506.13642（v1: 2025-06-16；Full Source Review Complete）
- From Bytes to Ideas — https://arxiv.org/abs/2506.14761（v1: 2025-06-17；Full Source Review Complete）
- Ring-lite — https://arxiv.org/abs/2506.14731（v1: 2025-06-17；Full Source Review Complete）
- AgentSynth — https://arxiv.org/abs/2506.14205（v1: 2025-06-17；Full Source Review Complete）
- xbench — https://arxiv.org/abs/2506.13651（v1: 2025-06-16；Full Source Review Complete）
- MultiFinBen — https://arxiv.org/abs/2506.14028（v1: 2025-06-16；Full Source Review Complete）
- Efficient Medical VIE via RL — https://arxiv.org/abs/2506.13363（v1: 2025-06-16；Full Source Review Complete）
- Align Your Flow — https://arxiv.org/abs/2506.14603（v1: 2025-06-17；Full Source Review Complete）
- Guaranteed Guess — https://arxiv.org/abs/2506.14606（v1: 2025-06-17；Full Source Review Complete）
- Optimizing Length Compression — https://arxiv.org/abs/2506.14755（v1: 2025-06-17；Full Source Review Complete）
- Taming Polysemanticity — https://arxiv.org/abs/2506.14002（v1: 2025-06-16；Full Source Review Complete）
- Sekai — https://arxiv.org/abs/2506.15675（v1: 2025-06-18；Full Source Review Complete）
- All is Not Lost / CheckFree — https://arxiv.org/abs/2506.15461（v1: 2025-06-18；Accessed: 2026-08-22）
- ProtoReasoning — https://arxiv.org/abs/2506.15211（v1: 2025-06-18；Full Source Review Complete）
- Embodied Web Agents — https://arxiv.org/abs/2506.15677（v1: 2025-06-18；Full Source Review Complete）
- SwarmAgentic — https://arxiv.org/abs/2506.15672（v1: 2025-06-18；Full Source Review Complete）
- Semantically-Aware Rewards — https://arxiv.org/abs/2506.15068（v1: 2025-06-18；Full Source Review Complete）
- SciVer — https://arxiv.org/abs/2506.15569（v1: 2025-06-18；Full Source Review Complete）
- Truncated PPO — https://arxiv.org/abs/2506.15050（v1: 2025-06-18；Full Source Review Complete）
- MoTE — https://arxiv.org/abs/2506.14435（v1: 2025-06-17；Full Source Review Complete）
- Evolutionary Caching / ECAD — https://arxiv.org/abs/2506.15682（v1: 2025-06-18；Full Source Review Complete）
- OS-Harm — https://arxiv.org/abs/2506.14866（v1: 2025-06-17；Accessed: 2026-08-22）
- GenRecal — https://arxiv.org/abs/2506.15681（v1: 2025-06-18；Full Source Review Complete）
- ImmerseGen — https://arxiv.org/abs/2506.14315（v1: 2025-06-17；Low-score closure）
- GMT — https://arxiv.org/abs/2506.14770（v1: 2025-06-17；Low-score closure）
- PictSure — https://arxiv.org/abs/2506.14842（v1: 2025-06-16；Low-score closure）
- Guru / Cross-domain RL — https://arxiv.org/abs/2506.14965（v1: 2025-06-17；Full Source Review Complete — Experimental / Numerical Subclaim Disputed；Accessed: 2026-08-22）
- Show-o2 — https://arxiv.org/abs/2506.15564（v1: 2025-06-18；Full Source Review Complete）
- SonicVerse — https://arxiv.org/abs/2506.15154（v1: 2025-06-18；Low-score closure）
- RE-IMAGINE — https://arxiv.org/abs/2506.15455（v1: 2025-06-18；Full Source Review Complete）
- Ray 2.47.1 — https://pypi.org/project/ray/2.47.1/（Release: 2025-06-17；Low-score closure）
- LazyEviction — https://arxiv.org/abs/2506.15969（v1: 2025-06-19；Full Source Review Complete）
- EvoLM — https://arxiv.org/abs/2506.16029（v1: 2025-06-19；Full Source Review Complete）
- SparseLoRA — https://arxiv.org/abs/2506.16500（v1: 2025-06-19；Full Source Review Complete）
- SCALE Optimizer — https://arxiv.org/abs/2506.16659（v1: 2025-06-20；Full Source Review Complete）
- GRPO-CARE — https://arxiv.org/abs/2506.16141（v1: 2025-06-19；Full Source Review Complete）
- LMR-BENCH — https://arxiv.org/abs/2506.17335（v1: 2025-06-19；Full Source Review Complete）
- TabArena — https://arxiv.org/abs/2506.16791（v1: 2025-06-20；Full Source Review Complete）
- Probing LLM Safety to Latent Perturbations — https://arxiv.org/abs/2506.16078（v1: 2025-06-19；Full Source Review Complete）
- Mathematical Proof Litmus Test — https://arxiv.org/abs/2506.17114（v1: 2025-06-20；Full Source Review Complete）
- Tower+ — https://arxiv.org/abs/2506.17080（v1: 2025-06-20；Full Source Review Complete）
- DualTHOR — https://arxiv.org/abs/2506.16012（v1: 2025-06-19；Low-score closure）
- Hunyuan3D 2.5 — https://arxiv.org/abs/2506.16504（v1: 2025-06-19；Low-score closure）
- Vision-guided Chunking — https://arxiv.org/abs/2506.16035（v1: 2025-06-19；Low-score closure）
- Multi-hop RAG Generation — https://arxiv.org/abs/2506.16037（v1: 2025-06-19；Low-score closure）
- OmniReflect — https://arxiv.org/abs/2506.17449（v1: 2025-06-20；Low-score closure）
- MEXA — https://arxiv.org/abs/2506.17113（v1: 2025-06-20；Low-score closure）
- SGLang GB200 PD + Large-scale EP — https://lmsys.org/blog/2025-06-16-gb200-part-1/（First Public: 2025-06-16；Full Source Review Complete）
- TensorRT-LLM v0.20.0 — https://github.com/NVIDIA/TensorRT-LLM/releases/tag/v0.20.0（Release: 2025-06-19；Full Source Review Complete）
