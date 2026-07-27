# AI Research Weekly — 2025-W25

> Coverage Window: 2025-06-16～2025-06-22
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 2 项长期证据：MiniMax-M1、Gemini 2.5 Pro/Flash GA。记录聚焦约束、机制、证据边界与演进关系，不收集一般新闻。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 归档；搜索收录日与后续修订不替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery 与去重；论文机制回到正文。Crossref 仅做 Weekly metadata 交叉检查。
- 历史回填不补造 Daily；Accessed 统一为 2026-07-31。
- benchmark 缺少模型、硬件、长度、batch/concurrency、precision/quantization 与 SLO 时不做通用结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：Gemini 2.5 Pro/Flash GA（2025-06-17）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 保留：MiniMax-M1（2025-06-16）。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| MiniMax-M1 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Must Read；与 MiniMax-01 建立架构→RL 演进链 |
| Gemini 2.5 Pro/Flash GA | 3 | 3 | 3 | 4 | 4 | 3 | 20/30 | Record Only；不以 GA 状态修改核心章节 |

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
- **Integration Decision:** `Refine — Existing Argument`；Ch22/29 已吸收 long-context architecture 与 long-rollout cost 的联合边界。
- **Changed Files or Rejection Reason:** 已复核 `books/part-02-model/22-long-context.md` 与 `books/part-03-training-system/29-grpo.md`；不保留 benchmark。
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
- **Integration Decision:** `Weekly Only — Version/Product Fact`。
- **Changed Files or Rejection Reason:** 不改 Books；GA/price/availability 不改变 W13 的机制结论。
- **Open Questions:** stable alias是否固定weight snapshot；provider更新、deprecation与cross-region fallback如何影响reproducibility。

## Evidence Level

- 官方 Blog / Release 只证明公开事实；未公开实现保持未知。
- arXiv v1 默认 Status: Experimental；作者实验不等于独立复现。
- 跨来源连接是本项目推断，以 Evolution Relationship 标记。

## Cross-Week Deduplication

- 同一技术后续 revision 与工程集成回链首次公开周。
- 新版本不覆盖旧方案；年度索引记录 old constraint → new mechanism → new failure mode。

## Knowledge Tree Position

- MiniMax-M1 → 第 14、21、22、29、45、52 章（Direct Evolution）
- Gemini 2.5 Pro/Flash GA → 第 20、52、69 章（Layering / Dependency）

## Recommended Action

- MiniMax-M1：Must Read；与 MiniMax-01 建立架构→RL 演进链
- Gemini 2.5 Pro/Flash GA：Record Only；不以 GA 状态修改核心章节

## Event-Date Daily Decision

历史回填不创建 Daily；事件与证据边界直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略旧内容重发、二手转述、缺条件 benchmark 与纯可用性更新。
- discovery 排名和引用量不替代 novelty、reliability 或 longevity。

## Repository Changes

- 新增 papers/2025/weekly/2025-W25/README.md。
- 本周候选已完成 Source Review；Books Integration 仍受年度 Evidence Gate 约束。

## Open Questions

- 已完成 MiniMax-M1 的 Books disposition；未来只在出现新机制、纠错证据或新的演进关系时重新开启审计。
- 已完成 Gemini 2.5 Pro/Flash GA 的 Books disposition；未来只在出现新机制、纠错证据或新的演进关系时重新开启审计。

## Sources

- MiniMax-M1 — https://arxiv.org/abs/2506.13585（First Public: 2025-06-16；Accessed: 2026-07-31）
- Gemini 2.5 Pro/Flash GA — https://blog.google/products-and-platforms/products/gemini/gemini-2-5-model-family-expands/（First Public: 2025-06-17；Accessed: 2026-07-31）
