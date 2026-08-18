# AI Research Weekly — 2025-W13

> Coverage Window: 2025-03-24～2025-03-30
> Research Mode: Retrospective Backfill
> Audit Status: Candidate Evidence Gate Passed — Discovery Replay Conditional
> Historical Books Gate: Closed — existing decisions are provisional
> Accessed: 2026-07-31
> Backfilled: 2026-07-31
> Last Re-audited: 2026-08-24

## Executive Summary

旧版只保留Gemini 2.5 Pro与Anthropic circuit tracing，无法证明2025-03-24～30完整来源已重放。
第二轮独立复核与本次再重放把scored ledger从60校准为62个owner identities：48个20+、14个低分；另有Gemma 3、Wan与
Gemini Robotics三项跨周related evidence，不在W13重复计分。新增遗漏是2025-03-30合入主线的Megatron-LM MTP实现
（25/30）与2025-03-27发布的DeepSpeed v0.16.5（16/30）；原60项因此不是最终分母。
48/48 retained owner均已完成primary-source全文或完整工程代码路径覆盖与非模板化strict schema；14/14低分项完成来源、
日期、评分和拒绝理由闭合。RLHF Data Scaling已从event-time v1 HTML/PDF恢复并全文审计，CaMeL原P1 blocker也已解除；
普通Review Pending与Blocked均为0。固定机构、每日arXiv/Hugging Face发现、当周工程release、W14 spillback和版本去重已重放，
没有已知未路由identity。由于历史Scholar/OpenAlex/DBLP/Crossref结果无法形成事件时不可变的exhaustive导出，Discovery
Replay为Conditional Pass，而不是“穷尽全网”的声明；Candidate Evidence Gate通过，Historical Books Gate继续关闭。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；旧baseline访问日期为2026-07-31，前轮新增核验访问日期为2026-08-22，
  本轮RLHF/Megatron/DeepSpeed恢复访问日期为2026-08-24。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：Gemini 2.5 Pro（2025-03-25）、Tracing the thoughts of a large language model（2025-03-27）、
  GPT-4o Image Generation（2025-03-25，Version Fact / Mechanism Not Disclosed）。
- 低分闭合：Anthropic Economic Index（2025-03-27）与Meta / Cornerstone XR case（2025-03-26）；
  前者只支持usage/sampling evidence，后者没有公开新机制。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 已完成primary-source全文覆盖的W13 owner主线包括reasoning representation/RL、KV与FFN、multimodal
  continual pretraining/generation/world models/VLA、Agent RAG、evaluation与quantization；周末回放另补
  DAT、Aurelia、Evolutionary Prompt Optimization、RARE与RLHF Data Scaling。每日arXiv/Hugging Face重放及W14
  spillback去重后，没有已知未路由W13 academic identity；所有可访问20+论文均已通过strict schema。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 本组补回Megatron-LM MTP：commit `dc385c7`于2025-03-30确认合入主线，代码、文档和unit tests共同构成
  25/30 implementation evidence；它证明MCore当时已有可调用的sequential MTP training path，不证明质量或吞吐收益。
  DeepSpeed v0.16.5于2025-03-27发布，作为16/30 patch-family fact闭合；vLLM Q2 2025 roadmap issue于
  2025-03-29创建，同为16/30 planning-intent evidence，不证明任何roadmap项目已经交付。PyTorch 2.7当时仍处于
  release-candidate稳定阶段，JAX 0.5.3与vLLM v0.8.2均按发布日期归W12，KServe v0.15归W14，不在W13重复计分。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Gemini 2.5 Pro | 4 | 4 | 3 | 4 | 4 | 3 | 22/30 | Worth Watching；产品信号不直接修改 Books |
| Tracing the thoughts of a large language model | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；全文复核后只沉淀证据边界 |
| Reasoning Features via SAE | 5 | 4 | 3 | 4 | 5 | 5 | 26/30 | Books Frozen — Experimental interpretability evidence |
| SimpleRL-Zoo | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Books Frozen — Verifiable-reward GRPO branch |
| xKV | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Books Frozen — Cross-layer KV factorization |
| FFN Fusion | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Books Frozen — Cross-layer FFN execution branch |
| Video SimpleQA | 4 | 4 | 4 | 5 | 5 | 5 | 27/30 | Books Frozen — Video factuality decomposition |
| Trajectory Balance with Asynchrony | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Books Frozen — Async rollout/learner branch |
| CoMP multimodal continual pretraining | 4 | 4 | 4 | 4 | 4 | 5 | 25/30 | Books Frozen — Continual alignment branch |
| Video-T1 | 5 | 4 | 3 | 4 | 5 | 5 | 26/30 | Books Frozen — Test-time trajectory search |
| Aether | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Books Frozen — Unified predictive state branch |
| LookAhead Tuning | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Audit Complete — Preview/KL safety-preservation boundary |
| CaMeL | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Audit Complete — Capability/data-flow prompt-injection boundary |
| CFG-Zero* | 5 | 4 | 4 | 4 | 4 | 5 | 26/30 | Audit Complete — Flow-guidance projection boundary |
| Reasoning to Learn from Latent Thoughts | 5 | 5 | 4 | 4 | 4 | 5 | 27/30 | Audit Complete — EM self-data bootstrapping boundary |
| FAR | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Books Frozen — Multilevel temporal state |
| Inference-Time Scaling for Flow Models | 5 | 4 | 3 | 4 | 5 | 5 | 26/30 | Books Frozen — Particle/budget search branch |
| ReSearch | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Audit Complete — Search-action RL/evidence boundary |
| Video Hallucination | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Books Frozen — Evaluation/mitigation boundary |
| Dita | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Books Frozen — Diffusion-action VLA branch |
| Think Twice | 3 | 3 | 4 | 4 | 4 | 5 | 23/30 | Books Frozen — Experimental self-revision branch |
| PS3 / Scaling Vision Pretraining to 4K | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Books Frozen — Selective high-resolution tokens |
| LogQuant | 4 | 5 | 5 | 4 | 4 | 4 | 26/30 | Books Frozen — Experimental 2-bit KV branch |
| LEGO Puzzles | 3 | 2 | 4 | 4 | 3 | 3 | 19/30 | Low Score — Narrow benchmark scope |
| Open Deep Search | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Books Frozen — Iterative retrieval/reasoning workflow |
| Qwen2.5-Omni Technical Report | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Books Frozen — Multimodal clock/streaming contract |
| ViLBench | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low Score — Narrow evaluation evidence |
| MCTS-RAG | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Books Frozen — Search-tree RAG branch |
| Synthetic Video Physical Fidelity | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low Score — Evaluation-only evidence |
| GPT-4o Image Generation | 4 | 4 | 5 | 5 | 4 | 3 | 25/30 | Weekly Only — Version Fact / Mechanism Not Disclosed |
| DAT / Dynamic Alpha Tuning | 3 | 3 | 4 | 4 | 5 | 4 | 23/30 | Audit Complete — Query-adaptive retrieval-fusion case |
| Aurelia | 4 | 4 | 4 | 4 | 4 | 5 | 25/30 | Audit Complete — Multimodal test-time reflection case |
| Evolutionary Prompt Optimization for VLMs | 4 | 3 | 3 | 4 | 4 | 5 | 23/30 | Audit Complete — Prompt/tool search case |
| RARE | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Audit Complete — Retrieval-conditioned SFT boundary |
| Shape and Texture Recognition in Large Vision-Language Models | 3 | 2 | 3 | 4 | 3 | 3 | 18/30 | Low Score — Representation diagnostic only |
| A Survey on Unlearnable Data | 2 | 3 | 3 | 4 | 3 | 4 | 19/30 | Low Score — Secondary synthesis only |
| Anthropic Economic Index: Insights from Claude 3.7 Sonnet | 2 | 3 | 3 | 5 | 2 | 3 | 18/30 | Weekly Only — Usage/sampling evidence |
| Meta / Cornerstone XR Training with Llama | 1 | 1 | 2 | 4 | 1 | 1 | 10/30 | Ignored Noise — Product case without mechanism contract |
| Unified Multimodal Discrete Diffusion | 5 | 4 | 4 | 4 | 4 | 5 | 26/30 | Audit Complete — Joint masked-state/commit boundary |
| JavisDiT | 5 | 5 | 3 | 4 | 5 | 5 | 27/30 | Audit Complete — Experimental joint A/V state and paired-commit evidence |
| AdaptiVocab | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental / Event-time Artifact Unavailable |
| Exploring Data Scaling Trends and Effects in RLHF | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Full Source Review Complete — Experimental / Data-quality and verifier-conditioned scaling |
| Scaling Laws in Scientific Discovery with AI and Robot Scientists | 3 | 3 | 2 | 4 | 3 | 3 | 18/30 | Low-score closure — Conceptual perspective without scaling evidence |
| ResearchBench | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | Audit Complete — Research decomposition/judge boundary |
| Olympiad Math Benchmark | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low Score — Incremental benchmark evidence |
| Agent Survey | 2 | 3 | 3 | 4 | 3 | 4 | 19/30 | Low Score — Secondary synthesis only |
| UI-R1 | 5 | 4 | 5 | 4 | 5 | 4 | 27/30 | Audit Complete — Single-state GUI reward boundary |
| Embodied-Reasoner | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Audit Complete — Simulator high-level action boundary |
| ReaRAG | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Audit Complete — Iterative retrieval/stop boundary |
| LeX-Art | 4 | 3 | 4 | 4 | 3 | 4 | 22/30 | Audit Complete — Synthetic data/evaluator coupling boundary |
| VBench 2.0 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Audit Complete — Video diagnostic/judge boundary |
| Lumina-Image 2.0 | 4 | 4 | 4 | 4 | 4 | 5 | 25/30 | Audit Complete — Unified-stream/training-budget boundary |
| Video-R1 | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Audit Complete — Temporal contrast/reward boundary |
| Understanding R1-Zero-Like Training | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Audit Complete — Dr. GRPO denominator/length-bias boundary |
| CodeARC | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Audit Complete — Interactive executable-evaluation boundary |
| Quamba2 | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Audit Complete — SSM-aware PTQ/kernel boundary |
| Landscape of Thoughts | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Audit Complete — Diagnostic projection / causal-state boundary |
| Towards Trustworthy GUI Agents | 3 | 4 | 3 | 4 | 2 | 3 | 19/30 | Low Score — Secondary source map |
| Megatron-LM Multi-Token Prediction support | 3 | 4 | 4 | 5 | 5 | 4 | 25/30 | Full Source Review Complete — Implementation Fact / No performance claim |
| Transformers 4.50 patch family | 1 | 2 | 4 | 5 | 1 | 1 | 14/30 | Low Score — Version patch family |
| DeepSpeed v0.16.5 | 2 | 2 | 3 | 5 | 2 | 2 | 16/30 | Low Score — Patch-family implementation facts |
| vLLM 2025 Q2 roadmap | 2 | 3 | 3 | 4 | 3 | 1 | 16/30 | Low Score — Planning intent, not shipped behavior |

### Deep Analysis 1 — Gemini 2.5 Pro

- First Public: 2025-03-25
- Status: Official experimental release
- Primary Source: https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/
- Evolution Relationship: Direct Evolution

#### Why

frontier model 把 reasoning 作为默认能力时，服务系统必须显式管理 reasoning budget、context 与 latency。

#### Principle and Mechanism

官方发布证明产品形态和 model card 边界，但未公开训练或 router 实现。

#### Trade-off and Evidence Boundary

更强 reasoning 与长 context 提高复杂任务能力，也增加 token 成本、不可预测 latency 和评测污染风险。

#### Connection and Evolution

知识树位置：第 20、22、52、62 章。Worth Watching；产品信号不直接修改 Books。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 2 — Tracing the thoughts of a large language model

- First Public: 2025-03-27
- Status: Anthropic interpretability research
- Primary Source: https://www.anthropic.com/research/tracing-thoughts-language-model
- Evolution Relationship: Principle Reuse

#### Why

输出 token 不能充分说明模型内部如何形成答案；安全和可靠性需要区分 verbalized rationale 与 latent computation。

#### Principle and Mechanism

研究使用 circuit tracing / attribution graph 分析受限任务中的内部计算路径，并报告跨语言概念与 planning 等案例。

#### Trade-off and Evidence Boundary

可解释图谱提供机制假设，但方法存在近似、选择偏差和规模限制，不能把案例当成模型普遍真实思维。

#### Connection and Evolution

知识树位置：第 5、8、62、68 章。Must Read；全文复核后只沉淀证据边界。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

> Schema Review（2026-08-24）：本节57个显式条目包含48个W13 retained-owner packet、3个跨周
> related-evidence packet与6个具有独立审计段落的低分owner；其余8个低分owner在下方统一ledger完成
> source/date/score/rejection闭合。48个retained packet均已覆盖Stable Node ID或明确owner、Current/Legacy
> Chapter、previous design、state/data/control flow、workload、evidence/non-evidence、disposition与Open Questions。
> 不得仅凭标题或“全文已读”把任一条目计作最终完成。

### Gemini 2.5 Pro

- **Candidate / Week / Score:** Gemini 2.5 Pro / 2025-W13 / 22/30。
- **Source Family ID:** `google-gemini-2.5-family`。
- **Source Type:** 2025-03 product/research announcement + 2025-07 technical report + model/safety materials。
- **First-public Date / Revision History:** Gemini 2.5 Pro Experimental 于 2025-03-25 发布，Blog 3 月 26 日更新；family technical report arXiv v1 为 2025-07-08。7 月报告可解释 family evolution，但不得当作 3 月发布时已经公开的机制。
- **Direct Primary Sources:** 3 月 Google/DeepMind announcement；《Gemini 2.5 Technical Report》官方 73 页 PDF / arXiv；model card / safety report。
- **Related Primary Sources:** Gemini 1.5 report、TPUv5p 与 Google safety framework仅用于演进背景。
- **Access and Verification Status:** Verified；announcement 全文、73 页报告 architecture/training/evaluation/safety/appendix 已读取。
- **Full-read Coverage:** metadata、architecture/dataset、training infrastructure、post-training、capability/evaluation protocols、long context/multimodal/agentic examples、safety/critical capability、appendix benchmark definitions。
- **Original Problem:** frontier model 需要把多模态、百万 token context、tool use 与可控 thinking 组合；训练端还要在多数据中心超大集群上承受频繁硬件故障与 silent data corruption。
- **Why the Previous Design Was Reasonable:** non-thinking dense/standard multimodal models有低 latency、可预测输出长度和更简单 serving contract；单 pod/整组重启在小规模训练中可接受，完整 replay 和静态资源简化正确性。
- **Changed Constraint:** reasoning/tool workflows 扩大输出 token 和长程 action；训练跨多个 8,960-chip TPUv5p pods、多个 datacenters，硬件故障每小时发生多次，整组等待/回滚成本过高。
- **Mechanism:** 报告披露 2.5 系列为 native multimodal sparse MoE transformers；较小 Flash models 使用 k-sparse teacher distribution distillation。训练使用同步 data parallel 跨多个 TPUv5p pods；slice-granularity elasticity 在局部故障时减少 slices 继续训练，报告称约 97% throughput、每次中断丢失几十秒；split-phase SDC detection 对可疑 step 做 lightweight deterministic replay，比较结果以定位硬件。post-training 增加 SFT/RM/RL data quality、RL compute、verifiable/model-based rewards 与 multi-step tool environments。
- **State Ownership:** training runtime 拥有 slice membership、step identity、data/RNG/optimizer state 与 replay decision；模型/router 负责 token→expert path；产品 API 暴露 thinking/tool behavior，但内部 reasoning budget policy 与 router 细节未完全公开。
- **Control Flow / Data Flow:** multimodal data → sparse MoE pretraining → SFT/RM/RL/tool environments → model serving；训练异常 metric → deterministic replay same step → compare → quarantine/reconfigure slice → continue。若 replay inputs/RNG/collectives 不同，SDC判定会被正常 nondeterminism 污染。
- **Implementation Details:** pretraining cutoff 2.5 为 2025-01；训练跨多个 8,960-chip TPUv5p pods。Flash distillation 用 vocabulary k-sparse distribution减少 teacher logits storage。更精确 architecture/router、parameter count、optimizer、token budget 与 serving topology `Not Disclosed`。
- **Evaluation Setup:** 报告覆盖 coding、math、factuality、long-context、image/audio/video、agentic与 safety；benchmark table给出 prompt/tool/scoring细节，部分 competitor numbers 来自 public leaderboards。1M context tests 明显低于 ≤128K，且不同 tasks scaling 不一致。
- **Baselines / Ablations / Sensitivity:** 与 Gemini 1.5/2.0 和 contemporaries 比较；公开报告没有完整 architecture/training ablation，也没有把 base model、post-training、thinking tokens、tools 分解为统一因果贡献。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 训练硬件为 TPUv5p，多 pods/多 datacenters；input 1M、2.5 output 上限 64K；precision、global batch、online concurrency、TTFT/TPOT/SLO 未充分披露。API capability benchmark 不等于 serving cost contract。
- **What the Evidence Actually Proves:** 3 月证明 experimental product existence与公开 capability claims；7 月报告证明 Google 后续披露了 sparse MoE、TPUv5p elastic/SDC mechanisms及受限评测结果。
- **What It Does Not Prove:** 不证明 visible thinking 等同内部因果过程，不证明 1M context 可稳定组合所有证据，不证明 vendor benchmark 可跨 scaffold/price/latency 比较，也不证明所有 3 月 checkpoint 与 7 月 family implementation一致。
- **Limitations / Threats to Validity:** architecture/training细节大量未披露；benchmark contamination、tool/scaffold敏感；leaderboard/competitor snapshot；无独立复现；报告发布时间晚于事件。
- **Trade-offs / New Failure Modes:** thinking提高复杂任务能力却扩大 token cost/latency variance；MoE降低 active compute却引入 routing/all-to-all；elastic training缩短停顿却让 membership、deterministic replay、checkpoint consistency成为协议；SDC detection会有 false positive/negative。
- **Where the Previous Design Still Applies:** latency敏感、任务简单或需严格输出预算时 non-thinking/Flash/non-MoE models 仍合理；较小训练规模可继续用 static membership和普通 checkpoint restart。
- **Evolution Relationship:** `Direct Evolution`：Gemini 1.5 long-context/multimodal → Gemini 2.x thinking/tool use + sparse MoE；training resilience 属 `Layering / Dependency`，不由产品发布直接证明。
- **ROADMAP Node:** 主 owner 第 24 章；第 21、22、32、52、62 章为 handoff。
- **Stable Knowledge Node ID / Current Chapter / Legacy Chapter:** `TRAIN-PRETRAINING` / Ch28 / Ch24。
- **Target and Adjacent Chapters Read:** 已读第 23 章数据、第 24 章 Pretraining、第 25 章 SFT；核对第 21、22、32、52、62 章职责。
- **Existing Coverage:** 第 24 章已有“training stability is multi-layer system problem”和 SDC/collective/checkpoint timeline，但没有 slice elasticity + deterministic replay 的具体演进机制；这可能形成长期 refine。第 22/52/62 已有最大长度、token budget 与 benchmark contract 边界。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch24，只吸收 training resilience contract。
- **Changed Files or Rejection Reason:** 已更新 `books/part-03-training-system/24-pretraining.md`；不搬运能力榜单。
- **Open Questions:** slice reconfiguration如何保持 optimizer/data/RNG exactness；SDC replay threshold；March/July checkpoint continuity；thinking budget与 production SLO。

### Tracing the thoughts of a large language model

- **Candidate / Week / Score:** Tracing the thoughts of a large language model / 2025-W13 / 25/30。
- **Source Family ID:** `anthropic-circuit-tracing-attribution-graphs-2025`。
- **Source Type:** 官方 Research Blog + methods paper + Claude 3.5 Haiku biology case-study paper + open interface/artifact。
- **First-public Date / Revision History:** 两篇 primary papers 与 Blog 均发布于 2025-03-27；网页论文无 arXiv revision history，版本变化需按网页存档追踪。
- **Direct Primary Sources:** 《Circuit Tracing: Revealing Computational Graphs in Language Models》；《On the Biology of a Large Language Model》；Anthropic Blog。
- **Related Primary Sources:** cross-layer transcoder / sparse autoencoder prior work和公开 attribution graph interface，仅用于方法依赖与 artifact verification。
- **Access and Verification Status:** Verified；两篇网页全文、method appendices、evaluation、case studies、limitations 与 artifact说明已读取。
- **Full-read Coverage:** CLT architecture/training、local replacement model、edge attribution、pruning、interventions、mechanistic-faithfulness evaluation、engineering、十类 Haiku case studies、limitations/open questions/appendices。
- **Original Problem:** neuron/attention-head 粒度受 polysemanticity 与 superposition影响；从 activation correlation 或可读出信息不能推出特定 prompt 的因果计算路径。
- **Why the Previous Design Was Reasonable:** probing、feature visualization、activation patching 与 component-level ablation成本较低，能定位表示或重要层；对于狭窄假设和小模型，它们仍提供有效证据，不必构建巨型 feature dictionary。
- **Changed Constraint:** 需要在 frontier model 上把可解释 features连成 prompt-specific computation graph，并区分“图中相关路径”与“干预后真的改变原模型输出”。
- **Mechanism:** cross-layer transcoder 用稀疏 features近似替换 MLP outputs；local replacement model 加入未解释 error nodes并冻结原模型 attention patterns。节点包括 token embeddings、CLT features、error nodes与 output logits；边用带 stop-gradient 的局部 Jacobian/virtual weights表示直接 linear attribution。图按 indirect influence pruning，研究者将 features人工归为 supernodes，再在原模型做 constrained patching/steering验证。
- **State Ownership:** 原模型仍拥有真实 attention/MLP computation；CLT拥有解释性 feature basis；local replacement model拥有 prompt-specific frozen attention与 error nodes；人类分析者拥有 feature labels/supernode grouping。任何一层都不能单独宣称“模型真实思维”。
- **Control Flow / Data Flow:** prompt → original activations/attention → CLT features + reconstruction errors → local attribution DAG → prune/label → formulate mechanism hypothesis → intervene in original model → observe feature/logit/output effect。
- **Implementation Details:** methods paper使用 18-layer pretraining-only model和 Claude 3.5 Haiku；最大 CLT约 10M/30M features。Haiku CLT混合 pretraining/finetuning data；features跨 accelerators sharded，每 batch partial predictions后 all-reduce。CLT per-accelerator FLOPs近似 PLT，但网络带宽约随 layers增加。
- **Evaluation Setup:** quantitative reconstruction/sparsity/LLM-based interpretability；node-to-logit和feature-pair intervention predictiveness；graph completeness/replacement/pruning；biology paper选择 multi-hop、poetry planning、多语言、addition、diagnosis、hallucination、refusal、jailbreak、CoT faithfulness、hidden goal等 case studies。
- **Baselines / Ablations / Sensitivity:** 与 direct attribution、activation magnitude、per-layer transcoders等比较；不同 pruning thresholds展示 completeness/graph size frontier；intervention strength/layer会改变结论。最大 18L CLT normalized reconstruction error约 11.5%、L0 88；Haiku约 21.7%、L0 235。作者估计仅约四分之一尝试的 prompts得到令人满意的 insight。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model为 18L与 Claude 3.5 Haiku；30M feature scale；具体 accelerator型号、precision、batch、prompt-length distribution、训练/分析 wall-clock多未披露。论文指出复杂 graph人工分析可超过一小时；无 online serving SLO。
- **What the Evidence Actually Proves:** 方法能在选定 prompts上生成可干预检验的机制假设；特定 Haiku案例中存在 multi-hop、planning、language-shared representations、known/unknown gating等路径的受限证据。
- **What It Does Not Prove:** 不证明图完整或全局通用，不证明所有 CoT faithful/unfaithful，不证明 feature labels是唯一语义，不证明 attention QK mechanism被解释，也不证明存在人类式“思维语言”。
- **Limitations / Threats to Validity:** frozen attention遗漏 QK circuits；21.7% reconstruction error和 error-node dark matter；prompt/case selection bias；manual labeling；pruning损失；inactive/inhibitory features难发现；replacement model可能 mechanistically unfaithful；复杂/分布外 prompt失败。
- **Trade-offs / New Failure Modes:** 更可读的 sparse basis引入 reconstruction error；更小图牺牲 completeness；更强 steering可能产生 off-manifold effects；人工 supernodes提高理解但带主观性；CLT规模造成通信/存储成本。
- **Where the Previous Design Still Applies:** 用于筛查的 probes/SAE/activation patching、小模型完整电路、黑盒行为评测仍必要；circuit tracing是证据链新增层，不替代 output evaluation、red team或安全控制。
- **Evolution Relationship:** `Direct Evolution`：neuron/component analysis → sparse feature discovery → transcoder computation units → prompt-specific attribution graph → intervention validation；biology cases是 `Layering / Dependency`，不是通用认知定律。
- **ROADMAP Node:** 主 owner 第 5 章；第 62、68 章只接评测与风险边界。
- **Stable Knowledge Node ID / Current Chapter / Legacy Chapter:** `WORLDVIEW-REPRESENTATION` / Ch5 / Ch5。
- **Target and Adjacent Chapters Read:** 已读第 4 章模型学习、第 5 章神经网络学到什么、第 6 章 Transformer；核对第 62、68 章 evidence/security boundary。
- **Existing Coverage:** 第 5 章已有 correlation → decodability → intervention → mechanism 的证据阶梯、superposition与“观察只是投影”边界；但没有说明 replacement-model faithfulness、error-node dark matter、attention omission与 graph-pruning completeness，存在可明确 refine 的机制缺口。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch5，补 replacement-model faithfulness failure modes。
- **Changed Files or Rejection Reason:** 已更新 `books/part-01-worldview/05-what-neural-networks-learn.md`。
- **Open Questions:** 如何解释 attention QK circuits；如何量化 case selection bias；是否可自动化 labeling且保持可反驳性；CLT结论跨模型/版本稳定性。

### Reasoning Features via SAE

- **Identity / Sources / Coverage:** 2025-W13，26/30，`reasoning-features-sae`；arXiv:2503.18878 v1为2025-03-24，v2为2025-08-05。已读v1 method、SAE training、feature selection、steering experiment与limitations；后续revision不倒写。
- **Problem / Mechanism / State:** verbalized rationale与probe只能证明可读出，不能定位因果representation。论文在DeepSeek-R1-Llama-8B第19层训练65,536-feature SAE，用lexical ReasonScore从约10M tokens筛feature，再人工审核和steering；SAE basis、reconstruction error、feature label与原模型activation由不同owner承担。
- **Evaluation Contract:** 1B training tokens，LMSys-Chat-1M/OpenThoughts各半，context 1024，batch 4096，LR 5e-5；top-200中确认46个候选。68.5% explained variance、L0 86和约+2.2%作者评测必须绑定该模型/层/judge/长度变化。
- **Evidence / Trade-off:** 支持“受限层存在可干预reasoning-associated features”，不证明lexical marker等于真实推理或SAE给出唯一电路。新风险是selection circularity、reconstruction loss、off-manifold steering与GPT-4o judge coupling；black-box eval、patching与circuit tracing仍需共存。
- **Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** corpus → layer activation → SAE encode/reconstruct → lexical ranking → manual review → steering → judge；属于`probe/readout → sparse decomposition → localized intervention`的`Layering / Dependency`，不替代完整circuit tracing。主owner `WORLDVIEW-REPRESENTATION` / Ch5 / legacy Ch5；已读Ch4～6。Ch5已经覆盖superposition、probe→intervention evidence ladder与reconstruction boundary，因此最终为`No Change — Already Covered`，仅保留为受限SAE案例；待验证cross-layer stability、matched random controls和off-manifold steering。

### SimpleRL-Zoo

- **Identity / Sources / Coverage:** 2025-W13，28/30，`simplerl-zoo-zero-rl`；arXiv:2503.18892 v1为2025-03-24，v3为2025-08-06。已读v1 GRPO/Zero-RL、data difficulty、model comparison、pass@k/length/clip analyses与limitations。
- **Problem / Mechanism:** SFT warm start在稀疏reward下合理，但可验证数学答案允许直接rule reward。论文从base model使用GRPO/Zero-RL，并比较Easy/Medium/Hard数据和不同open models，检查policy improvement与sampling/reranking边界。
- **Evaluation Contract:** GSM8K/MATH训练，每档约8k；评测GSM8K、MATH500、Minerva、Olympiad、AIME、AMC。硬件、完整rollout concurrency和等成本contract未充分披露，较长输出不能自动解释为更强reasoning。
- **Evidence / Trade-off:** 作者设置支持“无需SFT也可提高pass@1”，不支持不可验证任务或所有base models。减少SFT依赖换来exploration instability、reward hacking、length variance与difficulty-distribution narrowing；弱base或主观reward下SFT仍更稳。
- **State / Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** rollout worker拥有prompt/output，verifier拥有correctness/format reward，trainer拥有group statistics、policy/reference version与update；prompt → grouped rollouts → verifier → normalized advantage → clipped update。它是`SFT→RL`与`base→verifiable-reward GRPO`并存的`Alternative Branch`。主owner `TRAIN-GRPO` / Ch33 / legacy Ch29；已读Ch32～34。Ch33已经覆盖rule reward、difficulty/length bias、base/SFT coexistence与policy-lag边界，最终为`No Change — Already Covered`；待验证matched rollout compute、base capability threshold与主观reward任务。

### xKV

- **Identity / Sources / Coverage:** 2025-W13，29/30，`xkv-cross-layer-factorization`；arXiv:2503.18893 v1为2025-03-24，v2为2026-05-27。已读v1 cross-layer SVD/factorization、kernel、RULER/LongBench、baselines、ablations与limitations。
- **Problem / Mechanism / State:** 完整逐层KV在短context下保持exactness且实现简单；长context使容量与bandwidth线性放大。xKV利用跨层dominant singular-vector alignment共享basis并选择性重建；basis/version、layer coefficients、uncompressed recent/generated tokens和reconstruction policy共同定义cache identity。
- **Evaluation Contract:** Llama3.1、Qwen2.5、DeepSeek-V2；比较StreamingLLM、PyramidKV、SnapKV、KIVI、Quest、ShadowKV、MiniCache与Single-SVD。作者报告8× compression时准确度下降不超过约3%，但online mixed workload、generated-token cache、batch/concurrency/SLO未闭合。
- **Evidence / Trade-off:** 证明作者条件下cross-layer redundancy可用于压缩，不证明所有层/模型或production serving保持收益。新成本是SVD/reconstruction、共享误差、window sensitivity、kernel与invalidation；内存足够或精度优先时完整KV仍合理。
- **Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** K/V projection → shared-basis projection → coefficients + recent exact state → attention-time reconstruction；属于`per-layer exact KV → eviction/quantization → cross-layer shared-basis factorization`的`Direct Evolution`。主owner `INFER-KV-CACHE` / Ch45 / legacy Ch41，GPU-memory handoff Ch54；已读Ch44～46及Ch54。Ch45已覆盖cache identity、exact/approximate state、compression、invalidation与kernel contract，但cross-layer basis是明确缺口，最终为`Refine — Existing Argument Candidate`；待验证generated-token path、online basis update、prefix reuse与端到端scheduler收益。

### FFN Fusion

- **Identity / Sources / Coverage:** 2025-W13，28/30，`ffn-fusion-cross-layer-execution`；arXiv:2503.18908 v1为2025-03-24。已读method、405B experiment、MMLU/MT-Bench、layer/last-layer ablations与implementation limits。
- **Problem / Mechanism:** 逐层FFN保留独立非线性和可训练性，但深模型串行FFN增加latency/memory pressure。论文把跨层连续FFN融合为较少effective modules，重写sequential execution graph；405B Puzzle模型报告融合49/50 consecutive FFNs。
- **Evaluation Contract:** 能力表与70B/移层/末层方案比较；因单卡内存限制使用sequence splitting。缺完整training compute、kernel wall-clock、multi-seed与production serving contract。
- **Evidence / Trade-off:** 支持特定模型中高比例fusion可保持接近baseline的受限能力，不证明任意architecture或训练阶段。减少串行模块换来retraining、approximation、debug与representation-collapse风险；原始逐层FFN仍是稳定默认。
- **State / Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** architecture transform拥有fused layer set和generated weights，checkpoint converter拥有lineage，runtime execution plan执行fused call；residual → attention updates → fused FFN → residual。它是architecture-level `Alternative Branch`，不是普通bias/activation kernel fusion，也不是Dense→MoE替代。主owner `MODEL-FFN` / Ch16 / legacy Ch16，Ch49只作execution handoff；已读Ch15～17及Ch49。Ch16缺cross-layer structural fusion边界，最终为`Refine — Existing Argument Candidate`；待验证full-task regression、conversion reproducibility、latency/memory和continued-training stability。

### Video SimpleQA

- **Identity / Sources / Coverage:** 2025-W13，27/30，`video-simpleqa-factuality-decomposition`；arXiv:2503.18923 v1为2025-03-24，v2为2025-08-13。已读v1 task construction、per-hop grounding、model evaluation、error taxonomy与limitations。
- **Problem / Mechanism:** 单一Video-QA总分混合perception、knowledge、temporal grounding和reasoning。benchmark用objective factual QA与per-hop evidence contract拆分错误路径，dataset/evaluator owner必须保存clip、timestamp、claim与judge version。
- **Evaluation Contract:** 作者配置使用8×A100、temperature 1、max output 1024并三次重复；具体模型、frame sampling与evaluator条件必须与结果绑定。
- **Evidence / Trade-off:** 支持更细粒度归因，不证明benchmark score等于真实视频事实性或evaluator无偏。增加诊断性也增加annotation、temporal alignment、judge成本和constructor coupling；任务级objective scorer仍优先。
- **State / Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** benchmark拥有question/answer/hop，sampler拥有observation，evaluator拥有claim/timestamp/judge；video → sampled frames/audio → per-hop claims → judge → failure attribution。属于`task score → per-example evidence → per-hop multimodal attribution`的`Layering / Dependency`。主owner `PLATFORM-EVALUATION-SYSTEM` / Ch66 / legacy Ch62；已读Ch65～67并核对Ch23。Ch66已有EvalSpec、judge uncertainty和failure attribution，但缺timestamp/per-hop grounding实例，最终为`Refine — Existing Argument Candidate`；待验证judge calibration、frame-policy sensitivity、inter-annotator agreement与temporal verifier。

### Trajectory Balance with Asynchrony

- **Identity / Sources / Coverage:** 2025-W13，29/30，`trajectory-balance-asynchronous-search-training`；arXiv:2503.18929 v1为2025-03-24，v2为2025-12-03。已读v1 TB objective、searcher/trainer architecture、buffer/strategy ablations与appendix。
- **Problem / Mechanism / State:** 同步rollout便于on-policy correctness，但慢searcher会阻塞learner。Searcher nodes异步产生trajectories写replay buffer，Trainer以off-policy Trajectory Balance学习；trajectory version、behavior policy、reward、age、learner checkpoint与consumption offset必须共同标识。
- **Evaluation Contract:** math、preference tuning与automated red-team；比较search strategy、buffer和rollout设置。PFT用FP32且无DeepSpeed，2.8B checkpointing较慢，吞吐不能与不同precision/framework直接比较。
- **Evidence / Trade-off:** 证明作者任务内探索和学习可解耦，不消除staleness/off-policy bias。更高利用率换来freshness、policy mismatch、backpressure、dedup和recovery；采样便宜或严格on-policy时同步仍合理。
- **State / Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** Searcher拥有behavior-policy version与trajectory，buffer拥有reward/age/provenance，trainer拥有learner checkpoint；search → versioned replay → age-aware sampling → TB loss → checkpoint → async refresh。属于`synchronous rollout/train → async replay → age/version-aware correction`的`Direct Evolution`。主owner `TRAIN-GRPO` / Ch33 / legacy Ch29，Ch36只承接distributed runtime；已读Ch32～34及Ch36。Ch33已有policy lag与async rollout边界，Trajectory Balance是alternative correction branch，最终为`Refine — Existing Argument Candidate`；待验证staleness operating point、buffer eviction、failure recovery与matched-precision throughput。

### CoMP Multimodal Continual Pretraining

- **Identity / Sources / Coverage:** 2025-W13，25/30，`comp-multimodal-continual-pretraining`；arXiv:2503.18931 v1为2025-03-24，v3为2026-07-20。已读v1 alignment objective、position handling、freeze/update branches、data-scale and stage ablations。
- **Problem / Mechanism / State:** 完全重训昂贵，adapter在低成本下合理却可能破坏原视觉表示。CoMP用language-space alignment loss、compatible position encoding与冻结/部分更新策略连接vision foundation model；visual feature、word embedding、position coordinates与alignment target分别有owner，detach word-embedding gradient防collapse。
- **Evaluation Contract:** DINOv2、SigLIP、AIMv2，native resolution与最高约8M data scale；比较position、stage和update策略。2026 v3只作revision lineage，不倒写v1。
- **Evidence / Trade-off:** 支持作者设置中的continual alignment与部分能力保留，不证明跨encoder/data普遍成立。降低重训成本换来forgetting、position incompatibility与mixture sensitivity；独立encoder/adapter在稳定需求下仍合理。
- **State / Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** encoder拥有visual features，projector/alignment loss拥有mapping，detached word embedding提供target，controller决定frozen/updated parameter set；image → encoder → projected tokens + position → LLM → alignment/task loss。属于`projector-only adaptation → language-space alignment → continual multimodal pretraining`的`Direct Evolution`。主owner `MULTIMODAL-REPRESENTATION` / Ch23，训练handoff Ch28；已读Ch22～24并核对Ch27～28。Ch23已有modality boundary、shared space与position identity，但缺detached target和continual branch，最终为`Refine — Existing Argument Candidate`；待验证长期stream forgetting、encoder swap与position extrapolation。

### Video-T1

- **Identity / Sources / Coverage:** 2025-W13，26/30，`video-t1-test-time-trajectory-search`；arXiv:2503.18942 v1为2025-03-24，v2为2025-04-01。已读v1 random linear search、Tree-of-Frames、verifier、budget/branch evaluation与limitations。
- **Problem / Mechanism / State:** 单轨video diffusion/flow sampling延迟可控，却无法在测试时探索并纠正较差trajectory。方法按timestep分支、评分、剪枝并由verifier选择；partial trajectory、branch score、priority queue、compute budget与committed output形成typed state。
- **Evaluation Contract:** 不同search budget/branch方法和作者video metrics；hardware、online SLO及verifier calibration未形成portable contract。
- **Evidence / Trade-off:** 支持在base model和verifier边界内用更多compute改善部分质量，不越过capability ceiling。新成本是多倍NFE/state、verifier bias、latency variance和branch recovery；低延迟或judge弱时单轨采样仍合理。
- **State / Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** tokenizer拥有visual tokens，denoiser维护masked grid与schedule，controller决定confidence commit；masked visual/text state → parallel denoise → confidence selection → iterative commit。它是`autoregressive append-only → masked parallel refinement`的`Alternative Branch`。主owner `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24；已读Ch23～25。Ch24已覆盖mutable masked state、commit和AR coexistence，最终为`No Change — Already Covered / Experimental`；待比较相同committed-output SLO下的总compute、calibration与rollback。

### Aether

- **Identity / Sources / Coverage:** 2025-W13，28/30，`aether-unified-world-representation`；arXiv:2503.18945 v1为2025-03-24，v3为2025-07-28。已读v1 reconstruction/prediction/planning architecture、training data、depth/pose/navigation evaluation、ablations与limitations。
- **Problem / Mechanism / State:** 下一帧外观生成不自动形成action-conditioned环境状态。Aether统一reconstruction、prediction、planning，以camera pose trajectory为action，对RGB-D、pose与future observation建模；observation/action → latent state → predicted observation/depth/pose → rollout/planning。
- **Implementation / Evaluation:** CogVideoX-5B-I2V、synthetic RGB-D/pose、随机input/output modality组合；reconstruction用4 denoise steps。Sintel/TUM/ScanNet zero-shot depth/pose与generation/navigation，含depth-objective ablation。
- **Evidence / Trade-off:** 支持共享representation完成多种预测/导航任务，不证明完整因果world model或真实机器人长期planning。统一状态换复用，也引入modality conflict、synthetic-to-real gap和rollout drift；专用reconstruction/SLAM仍有边界。
- **State / Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** observation encoder拥有perceptual state，dynamics model拥有action-conditioned transition，planner消费imagined rollouts，environment拥有real transition；observation/action → latent state → predicted next state → rollout → policy → new observation。属于`next-frame generation → action-conditioned transition → planning-coupled world model`的`Direct Evolution`。主owner `MULTIMODAL-WORLD-MODELS` / Ch25，VLA handoff Ch26；已读Ch24～26。Ch25已有video generation/world model boundary、state transition与revisable world state，最终为`No Change — Already Covered`；待验证causal controllability、long-horizon drift与real-environment calibration。

### FAR

- **Identity / Sources / Coverage:** 2025-W13，28/30，`far-frame-autoregressive-flow-video`；arXiv:2503.19325 v1为2025-03-25，v3为2025-05-18。已读v1 frame-level AR、flow matching、multilevel cache、training/test extrapolation与ablations。
- **Problem / Mechanism / State:** pixel/token AR让长视频序列和history state过长。FAR在frame-level continuous latent上AR + flow matching，frame内full attention、frame间causal；近期高分辨率L1和压缩长期L2分级，frame退出L1时重编码进入L2，形成显式cache migration。
- **Evaluation Contract:** 约130M～674M variants，128 frames超过8k tokens；action prediction/video tasks、long-video training与cache/clean-context ablations。production memory/latency/concurrency未披露。
- **Evidence / Trade-off:** 支持作者设置中的multilevel temporal state，不证明真实world dynamics或普遍serving收益。新风险是L1→L2误差、cache identity/invalidation、rollout drift和训练成本；短视频全历史仍更简单。
- **State / Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** flow sampler拥有time/velocity/step state，autoregressive condition提供history，controller决定integration/commit；condition → velocity estimate → ODE update → next block/frame → commit。属于`single-step generation → iterative flow correction`，与world model只是`Layering / Dependency`。主owner `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24，Ch25仅作state-transition handoff；已读Ch23～25。Ch24已有flow/diffusion sampler state和commit边界，最终为`Refine — Existing Argument Candidate`以补causal-conditioning branch；待验证长rollout drift、step budget与production latency。

### Inference-Time Scaling for Flow Models

- **Identity / Sources / Coverage:** 2025-W13，26/30，`flow-model-inference-time-scaling`；arXiv:2503.19385 v1为2025-03-25，v5为2025-10-24。已读v1 SDE particles、interpolant、budget forcing、reward tasks与ablations。
- **Problem / Mechanism:** 固定ODE trajectory缺少多候选探索；方法将ODE转为随机SDE particles，用linear→VP interpolant扩大搜索，并以Rollover Budget Forcing动态分配NFE。
- **Evaluation Contract:** reward-guided image tasks；quantity reward使用GroundingDINO + SAM，包含interpolant/budget ablation。reward、model、NFE与image workload必须绑定，不能形成通用scaling law。
- **Evidence / Trade-off:** 作者reward下更多/动态compute改善部分指标，不证明reward等于human quality。换来particle memory、verifier cost、latency variance和reward hacking；固定采样在SLO严格时仍合理。
- **State / Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** base flow model拥有velocity field，test-time controller拥有compute budget、candidate/step schedule与selection；prompt → multiple/extended trajectories → score/select → committed sample。属于`fixed sampling budget → inference-time compute allocation`的`Layering / Dependency`，不是模型能力必然提升。主owner `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24；已读Ch23～25。Ch24已有sampler budget、iterative correction和SLO boundary，最终为`No Change — Already Covered / Experimental`；待验证matched-FLOPs、independent evaluator与tail-latency。

### Video Hallucination

- **Identity / Sources / Coverage:** 2025-W13，25/30，`video-hallucination-benchmark-mitigation`；arXiv:2503.19622 v1为2025-03-25。已读taxonomy、benchmark、frame/CoT analyses、SFT+DPO mitigation与limitations。
- **Problem / Mechanism:** 单一总分掩盖video hallucination来源，更多frames也可能带来噪声。论文分解hallucination type，比较model/scale/frame/CoT，并用SFT + thinking-weighted DPO缓解；frame sampler、clip identity、judge与preference pair共同拥有evidence state。
- **Evaluation Contract:** 不同模型有不同frame/resolution contract，例如Video-ChatGPT 100×224²、Valley-Eagle 100×384²；不可跨配置直接归因。
- **Evidence / Trade-off:** 支持作者benchmark中frame count先升后降的现象，不充分证明跨模型因果。更多视觉证据换来noise、attention dilution、distribution shift；DPO再引入judge/reward bias。
- **State / Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** benchmark拥有video/question/answer，model生成claim，evaluator按perception/temporal/knowledge分类，reporter聚合slice；属于`aggregate accuracy → hallucination taxonomy → evidence-bearing failure attribution`的`Layering`。主owner `PLATFORM-EVALUATION-SYSTEM` / Ch66，Ch23只作representation handoff；已读Ch65～67并核对Ch23。Ch66已覆盖claim-level evidence与judge uncertainty，最终为`No Change — Already Covered`；待验证taxonomy completeness、human agreement、frame sampling和executable temporal evidence。

### Dita

- **Identity / Sources / Coverage:** 2025-W13，28/30，`dita-diffusion-transformer-vla`；arXiv:2503.19757 v1为2025-03-25，v2为2025-09-06。已读v1 architecture、training、CALVIN/robot evaluation、observation/trajectory/denoise ablations与limits。
- **Problem / Mechanism / Flow:** AR action在连续多步与uncertainty下受限；Dita用diffusion Transformer预测action chunk，CLIP instruction、DINOv2 image、Q-Former FiLM、timestep/noised actions共同condition。observation/instruction → denoise action chunk → controller/environment → new observation。
- **Evaluation Contract:** CALVIN与real robot；7D actions、10 future chunks、MSE、AdamW 1e-4、15 epochs、batch 128、4×A100。缺开放环境、failure recovery和production control SLO。
- **Evidence / Trade-off:** 支持作者setup内diffusion action modeling，不证明通用sim-to-real或安全。并行chunk换来denoise latency、commit horizon、correction delay与controller mismatch；低层专用controller仍需共存。
- **State / Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** perception模块拥有observation，high-level reasoner拥有language-conditioned plan，controller拥有trajectory/action chunk，environment返回新state；observation → plan → action → transition → correction。属于`VLM perception → VLA proposal → closed-loop controller`的`Direct Evolution`。主owner `MULTIMODAL-EMBODIED-VLA` / Ch26；已读Ch25～27。Ch26已有controller分层、latency/control frequency、sim-to-real和safety envelope，最终为`No Change — Already Covered / Experimental`；待验证closed-loop frequency、calibration、human override与真实环境failure recovery。

### Gemma 3 Technical Report

- **Identity / Sources / Coverage:** 2025-W13，28/30，`google-gemma3-family-report`；arXiv:2503.19786 v1为2025-03-25。已读official report的architecture、training、multimodal/long-context、QAT、evaluation与safety/privacy；与earlier release family去重。
- **Problem / Mechanism / State:** global attention、可变visual tokens与long context同时放大KV/内存。Gemma 3提高local:global比例、缩短local span；冻结SigLIP并把896输入池化为固定256 image tokens；QAT提供int4/fp8。position/window、visual-token budget、teacher logits与quantized artifact均需versioned identity。
- **Evaluation Contract:** 1B～27B family；QAT约5k steps，per-channel/block int4/fp8，每token保存256 sampled teacher logits；作者vision/context/quantization/safety评测无统一serving SLO。
- **Evidence / Trade-off:** 支持官方family的部署折中，不证明固定256 tokens保留所有细节。local attention降KV却弱化远程交互；固定视觉预算稳定runtime却压缩细节；QAT节省memory但增加teacher/training依赖。
- **Owner / Decision:** `MODEL-LONG-CONTEXT`，handoff multimodal/KV；`Books Frozen — Refine Candidate`。

### Think Twice

- **Identity / Sources / Coverage:** 2025-W13，23/30，`think-twice-self-revision`；arXiv:2503.19855 v1为2025-03-25。已读prompted revision method、benchmark protocol、round/length results与limitations。
- **Problem / Mechanism:** one-pass decoding成本低但不能主动修正；方法把前一答案加入prompt要求重答，无learned verifier。每轮answer、sampling seed、prompt与commit policy必须分开记录。
- **Evaluation Contract:** QwQ-32B、DeepSeek-R1；max 32768、temperature 0.6、top-p 0.95；AIME 32 samples，LCB/GPQA 8 samples。
- **Evidence / Trade-off:** 部分benchmark多轮有收益且后续轮更短，不证明模型识别真实错误。额外tokens/latency、错误自强化和无证据confidence是新failure；简单任务仍应one-pass。
- **State / Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** generator拥有initial answer，critic/evaluator拥有feedback，controller拥有iteration budget与stop，workflow保留revision lineage；proposal → critique → revise → verify/stop。属于`single-pass generation → evaluator-guided reflection`的`Layering`。主owner `AGENT-REFLECTION` / Ch80 / legacy Ch76；已读Ch79～81。Ch80已有feedback independence、verifier、budget和stop contract，最终为`No Change — Already Covered / Experimental`；待验证critic independence、self-confirmation、matched-call baseline与calibrated stopping。

### PS3 / Scaling Vision Pretraining to 4K

- **Identity / Sources / Coverage:** 2025-W13，27/30，`ps3-selective-high-resolution-vision`；arXiv:2503.19903 v1为2025-03-25，v2为2025-08-03。已读v1 global/local representation、selector、data/training、4K evaluation与ablations。
- **Problem / Mechanism / State:** 全局低分辨率丢细节，全量4K patches又使token/compute爆炸。PS3组合低分辨率global view与prompt/saliency选择的local high-res regions，保留crop coordinate、selector provenance与prompt relation；可多次stage-3补regions。
- **Evaluation Contract:** 最多约2,560 selected patches，4KPro与VL tasks，包含algorithm/model/data/design ablations。4.3× fewer tokens等数字必须绑定该model/selector/hardware，detail-rich data未完全过滤。
- **Evidence / Trade-off:** 支持selective high-res比全局铺满更高效，不证明selector不会漏关键区域。token节省换来miss、provenance和multi-stage training复杂度；固定低分辨率在简单视觉任务仍合理。
- **State / Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** patch/tokenizer拥有spatial identity，encoder拥有multiscale representation，data pipeline拥有resolution/crop provenance；image → multiscale patches → encoder → shared token space → downstream task。属于`fixed low-resolution patching → scalable native-resolution representation`的`Direct Evolution`。主owner `MULTIMODAL-REPRESENTATION` / Ch23，data handoff Ch27；已读Ch22～24并核对Ch27。Ch23已有patch/object representation、position与resolution identity，最终为`Refine — Existing Argument Candidate`仅补scale/crop provenance；待验证compute-normalized gain、high-resolution aliasing和serving batch heterogeneity。

### LogQuant

- **Identity / Sources / Coverage:** 2025-W13，26/30，`logquant-two-bit-kv`；arXiv:2503.19950 v1为2025-03-25。已读2-bit log quantization、attention rearrangement、LongBench comparison与limitations。
- **Problem / Mechanism / State:** 极低bit KV破坏attention且per-position metadata削弱runtime。LogQuant按KV分布做2-bit logarithmic quantization，并用attention rearrangement实现position-agnostic handling；quantizer parameters、KV version和kernel layout共同拥有cache identity。
- **Evaluation Contract:** Llama3.1-8B、Qwen1.5-7B、LongBench，与KIVI等比较；end-to-end latency、online batch/concurrency、hardware与SLO未充分披露。
- **Evidence / Trade-off:** 作者设置中相对KIVI改善部分math/code，不证明相对FP16无损或生产可用。更低memory换distribution sensitivity、quantization error与kernel complexity；短context/精度优先仍用高bit。
- **State / Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** cache manager拥有request/layer/token identity与quant metadata，kernel执行log-domain quant/dequant；K/V → scale/log bucket → packed cache → dequant → attention。属于`high-bit exact KV → linear low-bit → distribution-aware logarithmic low-bit`的`Alternative Branch`。主owner `INFER-KV-CACHE` / Ch45 / legacy Ch41，Ch54承接memory；已读Ch44～46及Ch54。Ch45已有quantization identity、kernel与invalidation边界，最终为`No Change — Already Covered / Experimental`；待验证end-to-end latency、prefix reuse、mixed precision与distribution drift。

### Gemini Robotics Report Node

- **Identity / Sources / Coverage:** 2025-W13，29/30，`google-gemini-robotics-family`；arXiv:2503.20020 v1为2025-03-25。已读official report的ER/VLA split、embodiments、training/evaluation与safety boundaries；更早announcement若已归W11则不重复产品评分。
- **Problem / Mechanism / Flow:** VLM能解释但不能保证连续、低延迟、安全控制。family区分Gemini Robotics-ER embodied reasoning与end-to-end VLA；observation/instruction → embodied plan/representation → action proposal → low-level controller/environment → correction。
- **Evaluation Contract:** 多robot embodiments/tasks与实验室setup；hardware、control frequency、production latency、安全override和open-world denominator未完整披露。
- **Evidence / Trade-off:** 证明作者条件内跨embodiment/task能力，不证明通用sim-to-real或开放自治。端到端减少手工mapping，却增加opacity、calibration、safety envelope与embodiment-specific state；hierarchical controller仍必要。
- **Owner / Decision:** `MULTIMODAL-EMBODIED-VLA`；`Books Frozen — Same-family Report Evidence`。

### Open Deep Search

- **Identity / Sources / Coverage:** 2025-W13，28/30，`open-deep-search-agent`；arXiv:2503.20201 v1为2025-03-26，并检查author artifact。已读search tool、reasoning agent、FRAMES/SimpleQA、ablations与limitations。
- **Problem / Mechanism / State:** single retrieve-then-answer适合简单事实，却不能判断证据充分性或迭代query。agent在reasoning中搜索、读取、重构query与停止；query、evidence/provenance、reasoning checkpoint、budget与final claims是typed state。
- **Evaluation Contract:** DeepSeek-R1/Llama3.1，FRAMES/SimpleQA；search-only改善SimpleQA却可能伤害FRAMES，reasoning orchestration恢复复杂任务。无production latency/cost/SLO，search freshness与proprietary baselines不等量。
- **Evidence / Trade-off:** 支持retrieval与orchestration需联合评估，不证明自动搜索必然可靠。提高覆盖换网络不确定性、evidence contamination、cost和stop failure；简单查询仍单次RAG。
- **State / Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** search engine拥有result/freshness，agent拥有query proposal，workflow拥有evidence/provenance、budget与stop；question → search → read → evidence state → reformulate/stop → claim。属于`single retrieval → iterative evidence loop → workflow-controlled research`的`Direct Evolution`。主owner `AGENT-RAG` / Ch76 / legacy Ch72，planning/workflow handoff Ch79/81；已读Ch75～77并核对Ch79/81。Ch76已有iterative retrieval、evidence sufficiency、query dialect与cost/stop，最终为`No Change — Already Covered`；待验证freshness identity、source calibration、matched-call comparison与citation entailment。

### Qwen2.5-Omni Technical Report

- **Identity / Sources / Coverage:** 2025-W13，29/30，`qwen25-omni-family-report`；arXiv:2503.20215 v1为2025-03-26。已读official report的encoders、TMRoPE、Thinker–Talker、streaming speech、training/evaluation与limitations。
- **Problem / Mechanism / State:** text/image/audio/video拥有不同clock、tokenization和latency。block-wise audio/visual encoders与temporal multimodal RoPE进入Thinker；Talker以monotonic semantic→speech流式生成，并经历context continuation、speech-stability DPO和multi-speaker IFT。modality/time、semantic/speech token、speaker/timbre与stream commit必须分离。
- **Evaluation Contract:** 广泛multimodal/audio/video/speech benchmarks，但training hardware、batch、online concurrency、router和端到端latency多为Not Disclosed，跨模型表不视为统一contract。
- **Evidence / Trade-off:** 支持公开的unified multimodal/streaming architecture family，不证明生产full-duplex SLO。统一interface增加clock sync、alignment、stream rollback与cross-modal conflict；专用ASR/TTS仍有低延迟边界。
- **State / Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** modality encoder拥有clock/token identity，Thinker拥有semantic context，Talker拥有speech tokens/speaker state，runtime拥有stream commit/cancel；multimodal inputs → aligned tokens → Thinker state → Talker stream → playback commit。属于`modality-specific pipeline → shared semantic Thinker → monotonic speech Talker`的`Layering`。主owner `MULTIMODAL-REPRESENTATION` / Ch23，Ch24/Ch42作generation/request handoff；已读Ch22～24并核对Ch42。现有章节已覆盖clock、alignment与stream commit，最终为`No Change — Already Covered`；待验证full-duplex latency、rollback、speaker isolation与cross-modal conflict。

### Wan Technical Report

- **Identity / Sources / Coverage:** 2025-W13，27/30，`wan-video-generation-family`；arXiv:2503.20314 v1为2025-03-26，v2为2025-04-19。已读v1 3D VAE/DiT/flow matching、training stages、family tasks、evaluation与limitations；与earlier release去重。
- **Problem / Mechanism:** video generation同时承受temporal consistency、resolution、duration和control。Wan使用3D causal VAE + DiT + flow matching，先低分辨率image pretraining，再image-video joint training并逐级增加resolution/duration；family还包含cache、quantization、editing/I2V/personalization/camera control与Wan-Bench。
- **Evaluation Contract:** 作者benchmark与功能矩阵；training cost、dataset licensing细节和production SLO不完整，vendor/author metrics不能通用化。
- **Evidence / Trade-off:** 支持公开family形成较完整技术栈，不证明任意model/hardware优越。统一family复用能力却扩大data licensing、cache correctness、task conflict与evaluation complexity；专用生成器仍适用。
- **Owner / Decision:** `MULTIMODAL-GENERATIVE-PARADIGMS`；`Books Frozen — Refine Candidate`。

### MCTS-RAG

- **Identity / Sources / Coverage:** 2025-W13，27/30，`mcts-rag-search-tree`；arXiv:2503.20757 v1为2025-03-26，v2为2025-10-08。已读v1 action space、UCT/rollout/parallel expansion/pruning、datasets、budget ablations与limitations。
- **Problem / Mechanism / State:** fixed RAG无法探索evidence/reasoning branches。MCTS管理retrieval/reasoning actions；node保存query/evidence、reasoning state、visit/value、budget与final commit，parallel expansion增加吞吐也引入dedup/coordination。
- **Evaluation Contract:** Qwen2.5-7B、Llama3.1-8B；Bing/LangChain、100k CWQA snippets、140k GPQA corpus；4–16 rollouts及action/expansion ablations。无online cost/SLO和search-engine freshness控制。
- **Evidence / Trade-off:** 支持作者任务内tree search改善协调，不证明heuristic value等于correctness。早期错误证据、信息过载、重复分支与latency explosion是新failure；简单事实查询仍单次RAG。
- **State / Flow / Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** node拥有query/evidence/reasoning/visit/value，controller拥有frontier与global budget，retriever拥有corpus/result；select → retrieve/reason → evaluate → backpropagate → expand/prune → commit。它是`RAG evidence state + planning search policy`的`Layering`，不是RAG被MCTS替代。主owner `AGENT-RAG` / Ch76 / legacy Ch72，planning handoff Ch79；已读Ch75～77及Ch79。现有章节已覆盖evidence state、tree search与global budget，最终为`No Change — Already Covered / Experimental`；待验证calibrated node value、freshness、branch dedup与production deadline。

### GPT-4o Image Generation

- **Candidate / Score / Source Family / Dates:** 25/30，`openai-gpt4o-native-image-generation-2025`；官方发布与system-card addendum均为2025-03-25。
- **Sources / Coverage:** 已读官方announcement、capability boundary、deployment/safety、C2PA provenance、risk evaluation与limitations；没有公开足够的architecture、training objective、decoder或latent-state细节。
- **Problem / Previous Design / Changed Constraint:** 独立image generator容易隔离和扩缩，却难与text/image conversational state保持统一；native multimodal conversation要求在同一上下文中生成、编辑并保持多轮visual state。
- **Mechanism / Ownership / Flow:** 可验证的系统状态只有text/image input、conversation context、generated image、policy decision和C2PA provenance；input/context → opaque native generation → policy/provenance → output。不得从产品表现反推AR、diffusion或内部token机制。
- **Evaluation Contract / Evidence Boundary:** 官方capability/risk examples，部分样例为多次采样后的best-of；生成可能约一分钟。hardware、precision、batch、concurrency和formal SLO均`Not Disclosed`。证据只证明产品、安全与provenance contract，不证明具体生成架构或通用benchmark优势。
- **Trade-off / Evolution / Owner / Decision / Open:** native context提高交互与一致性，却扩大统一安全surface、provenance/abuse risk与latency；属于产品层`Version Fact`。owner `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24，已读Ch23～25；现有章节已有生成分支但本来源不披露机制，最终为`Weekly Only — Version Fact / Mechanism Not Disclosed`；待公开architecture、evaluation denominator与serving SLO。

### DAT / Dynamic Alpha Tuning

- **Candidate / Score / Source Family / Dates:** 23/30，`dat-query-adaptive-hybrid-retrieval`；arXiv:2503.23013，v1 2025-03-29，单版本。
- **Coverage / Problem / Previous Design:** 已读hybrid retrieval formulation、LLM scorer、dynamic alpha、datasets、baselines、prompt appendix与limitations。fixed BM25/dense weight低延迟且可复算，但不同query的lexical/semantic需求不同。
- **Mechanism / Ownership / Flow:** sparse/dense各自产生top-1，LLM对其effectiveness评0～5并归一化为query-specific alpha，再按0.1粒度融合normalized scores；retriever拥有候选，judge拥有scores，fusion controller拥有alpha/rounding/version。query → two retrievals → judge → alpha → rerank → top-K。
- **Evaluation Contract:** SQuAD 13 articles/585 paragraphs/2,976 questions与DRCD 318/908/3,000；比较BM25、Dense、fixed alpha=0.6与多个judge，指标P@1、MRR@20。hardware、precision、batch/concurrency和production SLO未披露，每query多一次LLM critical-path call。
- **Evidence / Trade-off / Previous Design:** 证明该构造corpus中adaptive fusion改善retrieval metrics，不证明open-domain RAG freshness或answer correctness；收益换judge latency/cost、top-1 bias与score drift。高QPS、稳定域或已校准mixture仍宜fixed alpha。
- **Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** `fixed sparse/dense fusion → query-adaptive router`，属于`Direct Evolution`。主owner `AGENT-RAG` / Ch76 / legacy Ch72；已读Ch75～77。Ch76已有hybrid retrieval、router/evidence identity和cost，最终为`No Change — Already Covered`；待验证offline router、judge calibration、freshness与end-to-end claim evidence。

### Aurelia

- **Candidate / Score / Source Family / Dates:** 25/30，`aurelia-audiovisual-test-time-reasoning-distillation`；arXiv:2503.23219，v1 2025-03-29，单版本。
- **Coverage / Problem / Previous Design:** 已读benchmark construction、multi-agent algorithm、prompts、18-model evaluation、iteration/threshold ablations与appendix。single-pass AVLLM成本低，但temporal synchronization和cross-modal ambiguity容易失败。
- **Mechanism / Ownership / Flow:** Reasoning Generator提出解释，Summarizer压缩，multimodal Evaluator评分并反馈；controller在threshold或iteration cap后把selected reasoning注入target AVLLM。generator、summarizer、evaluator、controller和target model各自拥有不同state，避免把反馈写成模型内部机制。
- **Evaluation Contract:** AVReasonBench 4,500 items、18 AVLLMs；T=1/3/5约16.28/45.66/74.01秒每样本，并做threshold ablation。hardware、precision、batch/concurrency及production SLO未披露。
- **Evidence / Trade-off / Previous Design:** 证明作者benchmark和judge setup中iterative reasoning能提高部分得分，不证明reasoning faithful或真实temporal grounding；收益换多模型调用、judge coupling、reasoning contamination与高latency。实时任务或独立verifier存在时single pass/direct verification仍合理。
- **Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** `AV representation → test-time proposal → evaluator-guided refinement`，属于`Layering`。主owner `AGENT-REFLECTION` / Ch80 / legacy Ch76，handoff Ch23/66；已读Ch79～81。Ch80已有feedback independence、verifier、budget/stop，最终为`No Change — Already Covered`；待验证faithfulness、independent evaluator与matched-call baseline。

### Evolutionary Prompt Optimization for VLMs

- **Candidate / Score / Source Family / Dates:** 23/30，`evolutionary-multimodal-prompt-tool-synthesis`；arXiv:2503.23503，v1 2025-03-30，单版本。
- **Coverage / Problem / Previous Design:** 已读prompt/mutation/hyper-mutation spaces、binary tournament、fitness、tool synthesis、benchmarks与limitations。manual prompt可审查且成本低，但难系统探索multimodal strategy space。
- **Mechanism / Ownership / Flow:** population evolution同时优化task prompt、mutation prompt与hyper-mutation prompt；fitness结合minibatch task score和LLM critique，evolved XML tool description再由第二模型编译成Python。registry拥有lineage，evaluator拥有fitness，sandbox必须拥有execution authority。
- **Evaluation Contract:** GPT-4o-mini，MathVista、M3CoT、GeoBench-VLM；比较base、CoT、PromptBreeder、evolved prompt与+Tools。hardware、precision、batch/concurrency和SLO未披露；额外generation、fitness和tool execution是主要成本。
- **Evidence / Trade-off / Previous Design:** 证明prompt-space search可找到有用decomposition/tool patterns，不证明prompt是稳定机制或generated code安全；收益换evaluator overfit、lineage drift、unsafe code、test leakage和compute explosion。高风险工具、低预算或稳定任务仍宜固定prompt。
- **Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** `manual prompt → prompt optimization → evaluator-driven prompt/tool search`的`Direct Evolution`。主owner `AGENT-WORKFLOW` / Ch81 / legacy Ch77；已读Ch80～82并核对Ch78/79。Ch81已有artifact lineage、evaluator search和sandbox/commit，最终为`No Change — Already Covered`；待验证holdout contamination、安全sandbox与cost-normalized gain。

### RARE

- **Candidate / Score / Source Family / Dates:** 27/30，`rare-retrieval-augmented-reasoning-modeling`；arXiv:2503.23513，v1 2025-03-30，v2 2025-05-17；W13只使用v1。
- **Sources / Coverage:** 已读formal objective、retrieval-conditioned distillation、training、datasets、baselines、results、conclusion与官方artifact。
- **Problem / Previous Design / Changed Constraint:** domain pretraining/SFT把知识与reasoning写进参数，离线稳定却难更新；inference-only RAG外置知识，却不训练模型如何使用evidence。新约束是在7B/8B预算下联合学习retrieval-conditioned reasoning。
- **Mechanism / Ownership / Flow:** query与retrieved evidence共同进入teacher/data pipeline，QwQ-32B生成reasoning，错误样本最多重采样8次，再以SFT训练；KB/retriever拥有freshness，dataset拥有query/evidence/output lineage，trainer拥有checkpoint，runtime必须保持training-serving retrieval parity。
- **Evaluation Contract:** Llama-3.1-8B、Qwen2.5-7B、Mistral-7B-v0.3；MedQA、PubMedQA、PubHealth、CoVERT、BioASQ；MedOmniKB top-3或ground-truth docs，对CoT、SFT、RAG和多种API/model baselines。hardware、precision、batch、epochs、retrieval latency、concurrency和SLO未闭合。
- **Evidence / Trade-off / Previous Design:** 证明作者medical-QA设置中retrieval-conditioned SFT优于列出baseline，不证明知识/推理可严格分离或医疗部署可靠；收益换retriever dependence、teacher rationale error、evidence contamination和training-serving skew。离线、严格低延迟或retriever不可靠时parametric knowledge仍必要。
- **Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** `domain SFT + inference RAG → retrieval-conditioned SFT → retrieval-grounded runtime`的`Layering`。主owner `TRAIN-SFT` / Ch29 / legacy Ch25，RAG handoff Ch76；已读Ch28～30及Ch75～77。Ch29已有retrieval-conditioned adaptation，但training/inference retrieval parity仍可增强，最终为`Refine — Existing Argument Candidate`；待验证noisy/stale retrieval、teacher faithfulness、knowledge leakage与medical calibration。

### LookAhead Tuning

- **Candidate / Week / Score / Source Family:** LookAhead Tuning / 2025-W13 / 24/30 / `lookahead-tuning-2503.19041`；primary paper arXiv:2503.19041，v1 2025-03-24，v2/v3/v4仅作revision；已读method、True/Virtual Preview、training、evaluation、ablation、overhead与limitations。
- **Problem / Previous Design / Changed Constraint:** 普通SFT在窄任务上简单有效，却可能扰动既有安全对齐；新约束是在学习目标任务时限制early-token distribution drift，而非只追求task loss。
- **Mechanism / Ownership / Flow / Implementation:** True Preview把答案前`m`个token加入prompt，Virtual Preview加入中性前缀；dataset transform拥有preview state，trainer仍执行masked SFT，inference无新增状态。LLaMA2-7B-Chat，3 epochs、LR 2e-5、batch64、BF16、4×A100-80GB、ZeRO-2。
- **Evaluation Contract / Baselines / Sensitivity / Overhead:** GSM8K、SAMSum、HEx-PHI；比较seed、vanilla FT、SDFT、constrained SFT并测prefix length；FLOPs增量约2.18%/3.90%。online concurrency与serving SLO不适用/未披露。
- **Evidence / Non-evidence / Limits:** 支持该模型和任务中较小early-token KL与安全保持相关；不证明KL是因果安全指标或跨模型、攻击、长对话通用。True Preview依赖ground-truth prefix，过长preview损害效用，Virtual Preview可能学格式捷径。
- **Trade-off / Previous Design / Evolution:** 用轻量data transformation换安全保持proxy与少量训练成本；无可靠preview、知识注入为主或追求最简pipeline时普通SFT仍合理。`Alternative Branch`：plain SFT → preview-constrained SFT。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `TRAIN-SFT` / Ch29 / legacy Ch25；已读Ch28、Ch29、Ch30并核对Ch72。Ch29已覆盖forgetting与regression，但未解释early-token preview/KL proxy。`Audit Complete — Books Pending`；待验证跨tokenizer/scale的KL calibration。

### CaMeL / Defeating Prompt Injections by Design

- **Candidate / Week / Score / Source Family:** CaMeL / 2025-W13 / 29/30 / `camel-prompt-injection-2503.18813`；paper + official artifact，arXiv:2503.18813 v1 2025-03-24、v2 2025-06-24。已从v1 PDF恢复formal model、appendix、AgentDojo contract、excluded attacks与repository；原P1 blocker解除。
- **Problem / Previous Design / Changed Constraint:** 单LLM同时读取system prompt和不可信内容最简单，但把data与control authority混在同一生成通道；Agent必须读取外部内容又不能让其改变高权限控制流或越权外传。
- **Mechanism / Ownership / Control and Data Flow:** Privileged LLM只看trusted query并生成受限Python plan；Quarantined LLM解析untrusted data但无tool authority；restricted interpreter传播capability/taint，policy engine在effect-time授权。trusted query → P-LLM plan → interpreter → Q-LLM value → capability propagation → policy → tool。
- **Implementation / Evaluation Contract:** AgentDojo Workspace/Banking/Travel/Slack，多组Gemini、Claude、GPT/o-series；事件时v1最佳约67%，不得倒写v2的77%/84%。hardware、precision、batch、concurrency与SLO `Not Disclosed`；Travel utility下降揭示隔离成本。
- **Evidence / Non-evidence / Threats:** 证明在其PI-SEC threat model下可阻止不可信data改变control flow；不覆盖misinformation、phishing、side channel、gadget chain、恶意trusted prompt或compromised memory。policy completeness、declassification与interpreter compatibility仍是风险。
- **Trade-off / Previous Design / Evolution:** 以capability separation换policy/integration/confirmation成本；无工具副作用、单一信任域或低风险只读问答仍可用单LLM context。`Direct Evolution`：prompt instruction hierarchy → architectural authority separation。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `PLATFORM-SECURITY` / Ch72 / legacy Ch68；已读Ch71～73并核对`AGENT-PLATFORM` Ch84/legacy Ch80。Ch72已有least privilege/effect-time authorization，缺P/Q-LLM capability formalism。`Audit Complete — Books Pending`；待验证安全declassification、mutable memory与跨工具provenance。

### CFG-Zero*

- **Candidate / Week / Score / Source Family:** CFG-Zero* / 2025-W13 / 26/30 / `cfg-zero-star-2503.18886`；arXiv:2503.18886，v1 2025-03-24、v2 04-03。已读Gaussian-mixture derivation、projection、zero-init、T2I/T2V experiments、component/K sensitivity与limitations。
- **Problem / Previous Design / Changed Constraint:** fixed CFG在已校准sampler上简单稳定，但flow estimator早期不准时会把trajectory推错；新约束是按conditional/unconditional velocity geometry动态修正direction。
- **Mechanism / State / Flow / Implementation:** 计算`s*=(v_cond^T v_uncond)/||v_uncond||^2`，最初`K`个ODE steps把guidance置零（默认K=1）；sampler拥有step、scale与denominator guard，model weights不变。
- **Evaluation Contract:** toy Gaussian、ImageNet-256 DiT/SiT、Lumina-Next、SD3/3.5、Flux、Wan2.1 1.3B/14B；FID/IS、T2I-CompBench、VBench和human preference；含steps、scale、K、component ablation。hardware/precision/batch/concurrency/SLO未统一披露。
- **Evidence / Non-evidence / Limits:** 支持所测flow models的trajectory improvement；Wan-14B总分仅小幅变化且部分temporal/style下降，不证明所有diffusion/flow或production latency受益。额外velocity、数值退化和converged-model zero-init伤害是failure modes。
- **Trade-off / Previous Design / Evolution:** 用geometry-aware state换更复杂sampler；estimator已充分训练、CFG已校准或追求最简kernel时fixed CFG仍合理。`Alternative Branch`：fixed scale → step/geometry-conditioned guidance。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 / legacy N/A；已读Ch23～25。Ch24已覆盖diffusion mutable state/commit，但无该flow-specific projection。`Audit Complete — Books Pending`；待测heterogeneous batched prompts下scale calibration。

### Reasoning to Learn from Latent Thoughts

- **Candidate / Week / Score / Source Family:** Reasoning to Learn from Latent Thoughts / 2025-W13 / 27/30 / `latent-thought-em-2503.18866`；arXiv:2503.18866 v1 2025-03-24、v2 2025-09-29。已读probabilistic formulation、BoLT EM、fixed/continual bootstrapping、implementation、多次evaluation与limitations。
- **Problem / Previous Design / Changed Constraint:** fresh raw text是最稳pretraining input，但供给增长慢于compute且重复raw data不创造中间推理信息；约束转为从当前model生成、筛选并version derived training state。
- **Mechanism / Ownership / Flow:** 建模`p(Z,X)=p(Z)p(X|Z)`并以同一LM给`q(Z|X)`；E-step采样、按`p/q` importance resampling，M-step在`(Z,X)`继续pretrain。model revision、latent pool、weights与augmented dataset必须绑定。
- **Implementation / Evaluation Contract:** TinyLlama-1.1B、FineMath-4+，seq2048、batch96/192、AdamW、BF16；4/8×H200训练，生成跨H100/H200/A100/A6000/A5000/A40/L40/3090。对raw repeat/raw fresh、WRAP-Orig/CoT，测MATH/GSM8K/MMLU-STEM与K/iteration/space ablation。
- **Evidence / Non-evidence / Limits:** 支持1B math continued-pretraining中的data efficiency；不证明生成文本等同人类latent thought或跨域/规模通用。self-data bias、importance collapse、bootstrap plateau、DCLM NLL回退与异构复现是风险。
- **Trade-off / Previous Design / Evolution:** 用inference/curation compute换稀缺推理data；数据持续增长、非推理域或筛选不可靠时raw fresh data仍优先。`Direct Evolution`：raw repetition → teacher/self-generated rationale → iterative latent-data EM。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `TRAIN-PRETRAINING` / Ch28 / legacy Ch24；已读Ch27～29。Ch28已有feedback-guided self-supervision和mid-training contract，缺importance-resampled iterative branch。`Audit Complete — Books Pending`；待验证importance calibration与termination防止self-confirming collapse。

### ReSearch

- **Candidate / Week / Score / Source Family:** ReSearch / 2025-W13 / 28/30 / `research-rl-search-2503.19470`；arXiv:2503.19470 v1 2025-03-25、v2 03-27、v3 09-23。已读search action、GRPO reward、implementation、cross-dataset evaluation、ablation与limitations。
- **Problem / Previous Design / Changed Constraint:** fixed top-k RAG对single-hop低延迟合理，却不训练何时重搜、改写或停止；新约束是让retrieval成为有成本的policy action并保留evidence provenance。
- **Mechanism / State / Flow:** GRPO生成`<think>/<search>/<result>/<answer>`trajectory，retrieved tokens不进入policy loss；policy拥有thought/query/stop，retriever拥有document evidence，environment result作为observation回流。
- **Implementation / Evaluation Contract:** Qwen2.5 7B/32B，MuSiQue 19,938训练、2 epochs；E5-base-v2 + 2018 Wikipedia top-5；8×H800、batch256、5 rollouts、temperature1、KL0.001。HotpotQA/2Wiki/MuSiQue/Bamboogle，对no-RAG、naive、IRCoT、Iter-RetGen。
- **Evidence / Non-evidence / Limits:** 支持单训练集rule-reward RL学到multi-step search；不证明live web freshness、citation correctness、tool safety或production SLO。over-search、retriever dependency、reward leakage和latency是新failure modes。
- **Trade-off / Previous Design / Evolution:** 用trajectory compute换adaptive evidence acquisition；单跳、evidence已知或严格低延迟仍用fixed top-k。`Layering`：RAG → iterative retrieval → RL-owned search policy。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `TRAIN-GRPO` / Ch33 / legacy Ch29；已读Ch32～34并核对`AGENT-RAG` Ch76/legacy Ch72。Ch33拥有GRPO contract，Ch76拥有query/evidence/stop，需避免双owner。`Audit Complete — Books Pending`；待把search cost、sufficiency和citation entailment组合为非投机reward。

### Unified Multimodal Discrete Diffusion

- **Candidate / Week / Score / Source Family:** Unified Multimodal Discrete Diffusion / 2025-W13 / 26/30 / `unidisc-2503.20853`；arXiv:2503.20853，仅v1 2025-03-26。已读factorization、training objective、sampler、matched baseline、ablation与limitations。
- **Problem / Previous Design / Changed Constraint:** AR提供append-only generation与成熟cache，却难原生支持双向理解、任意位置修正和inpainting；约束转为在统一multimodal vocabulary中维护mutable masked state。
- **Mechanism / State / Flow:** image/text各自tokenize后共享vocabulary/head与bidirectional attention；continuous masking、modality-dropout CFG、soft-min/min-SNR，MaskGIT按confidence提交token。joint masked grid、mask schedule与commit policy是runtime state。
- **Implementation / Evaluation Contract:** DataComp1B+CC12M约30M pairs/11B tokens；115M/340M/1.4B，256²图像256 tokens、text128，batch512、LR3e-4，约300 L40S GPU-hours。对matched Chameleon-style AR，测PPL/FID/CLIP/understanding并做QK norm、RMSNorm、mask、SNR/time ablation。
- **Evidence / Non-evidence / Limits:** 支持joint discrete diffusion承担理解/生成/inpainting；训练compute约需13.2×才接近AR loss，不证明普遍替代AR或达到相同online SLO。
- **Trade-off / Previous Design / Evolution:** iterative correction换mutable-state latency、confidence calibration和更高training compute；streaming text、append-only cache、低inference budget仍优先AR。`Alternative Branch`：causal factorization ↔ iterative masked refinement。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 / legacy N/A；已读Ch23～25。Ch24已有masked diffusion、editable state、commit与AR coexistence，论文主要是受限案例。`Audit Complete — Books Pending`；待比较相同committed-output SLO下总compute。

### ResearchBench

- **Candidate / Week / Score / Source Family:** ResearchBench / 2025-W13 / 23/30 / `researchbench-2503.21248`；arXiv:2503.21248 v1 2025-03-27、v2 2025-07-01、v3 2026-04-20。已读dataset construction、retrieval/composition/ranking tasks、expert validation、evaluation与limitations。
- **Problem / Previous Design / Changed Constraint:** 论文QA适合测知识回忆，却不能拆解“找到灵感—组合灵感—提出假设”；新约束是把research discovery分解为可审计中间state，同时不把文本相似度当scientific correctness。
- **Mechanism / State / Flow:** 从papers抽取question、background、inspirations、hypothesis；benchmark分别测retrieval、composition与ranking。paper snapshot、extraction prompt/model、positive/negative inspiration、distance与judge version必须versioned。
- **Evaluation Contract:** 1,386篇2024 papers、12 disciplines；5名PhD检查62篇；75 negative inspirations、3 distance levels；top-3/15与top-3/75 retrieval。hardware/precision/batch/concurrency/SLO不适用或未披露；无实验artifact execution。
- **Evidence / Non-evidence / Limits:** 支持该decomposition可测inspiration retrieval/combination；不证明2024数据无contamination、hypothesis新颖/可执行/正确。LLM extraction/judge bias、小专家样本和“sufficient decomposition”假设构成threats。
- **Trade-off / Previous Design / Evolution:** 诊断性换constructor/judge复杂度；domain experts与真实experiment仍是authority。`Layering`：text benchmark → structured research trace → executable science evidence（尚未达到）。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `PLATFORM-EVALUATION-SYSTEM` / Ch66 / legacy Ch62；已读Ch65～67并核对Ch81。Ch66已有judge uncertainty、contamination与executable evidence。`Audit Complete — Books Pending`；待加入feasibility、novelty和replication evidence。

### UI-R1

- **Candidate / Week / Score / Source Family:** UI-R1 / 2025-W13 / 27/30 / `ui-r1-2503.21620`；arXiv:2503.21620 v1 2025-03-27，后续v2～v5不倒写。已读GRPO/reward、data filtering、evaluation、ablation与limitations。
- **Problem / Previous Design / Changed Constraint:** GUI imitation/SFT在demonstration充足时稳定，但稀缺hard examples上不能利用可验证click geometry；约束转为用environment-derived rule reward训练action prediction，同时避免把single-state结果外推到long-horizon Agent。
- **Mechanism / State / Flow:** Qwen2.5-VL-3B + GRPO；action-type、click-coordinate-in-box、format rewards。screenshot/question、candidate action、group reward stats与policy version是独立state；没有live environment transition loop。
- **Implementation / Evaluation Contract:** 从ScreenSpot与AndroidControl筛136个困难mobile samples；测试ScreenSpot、ScreenSpot-Pro、AndroidControl single-state；比较base/SFT/RL并做reward/data ablation。hardware、precision、batch、rollout concurrency、latency/SLO `Not Disclosed`。
- **Evidence / Non-evidence / Limits:** 支持极小数据rule reward改善GUI action prediction；不证明long-horizon execution、recovery、安全或production latency。box tolerance、base-failure selection、single-state supervision与action-schema overfit是风险。
- **Trade-off / Previous Design / Evolution:** 用可验证geometry换reward-specific bias；demonstrations充足或outcome不可精确定义时SFT仍更稳。`Alternative Branch`：GUI SFT → single-state outcome RL → trajectory RL（未证明）。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `TRAIN-GRPO` / Ch33 / legacy Ch29；已读Ch32～34并核对`AGENT-PLANNING` Ch79/legacy Ch75。Ch33已有rule-reward contract，GUI仅作受限案例。`Audit Complete — Books Pending`；待扩展到副作用、rollback和partial observability trajectory。

### Embodied-Reasoner

- **Candidate / Week / Score / Source Family:** Embodied-Reasoner / 2025-W13 / 27/30 / `embodied-reasoner-2503.21696`；arXiv:2503.21696 v1 2025-03-27、v2 05-14。已读Observation–Thought–Action、training stages、sim/real evaluation与limitations。
- **Problem / Previous Design / Changed Constraint:** pure imitation适合稳定demonstration，却难在新场景显式探索/反思；新约束是联合reasoning与high-level action，同时必须区分simulator primitive和真实low-level control。
- **Mechanism / State / Flow:** imitation → rejection-sampling self-exploration → reflection tuning；image observation → five thought types → nine AI2-THOR high-level actions → simulator transition → next observation。trajectory、synthetic thought、action与environment truth独立。
- **Implementation / Evaluation Contract:** Qwen2-VL-7B，9,390 trajectories、64K images、约8M thought tokens、107 scenes；809 simulator tasks/12 unseen scenes、25 ultra-long tasks；real test仅30 tasks/3 rooms且human camera/operator辅助。hardware/precision/control frequency/SLO未披露。
- **Evidence / Non-evidence / Limits:** 支持simulator中search/reason/action联合训练；不证明autonomous robotics、real-time control、physical safety或sim-to-real。synthetic thoughts可能事后合理化，高层action隐藏控制难度，真实样本过小。
- **Trade-off / Previous Design / Evolution:** reasoning state换更长trajectory与teacher/simulator coupling；低层controller和显式safety envelope仍必须共存，固定policy在封闭任务仍合理。`Direct Evolution`：imitation → self-exploration/reflection → physical loop（未闭合）。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `MULTIMODAL-EMBODIED-VLA` / Ch26 / legacy N/A；已读Ch25～27并核对Ch81。Ch26已有observation/action/controller/environment及sim-to-real boundary。`Audit Complete — Books Pending`；待移除privileged state和human-operated perception后复验。

### ReaRAG

- **Candidate / Week / Score / Source Family:** ReaRAG / 2025-W13 / 28/30 / `rearag-2503.21729`；arXiv:2503.21729 v1 2025-03-27、v2 04-18、v3 05-19。已读Thought–Action–Observation method、training、evaluation、comparison与limitations。
- **Problem / Previous Design / Changed Constraint:** single retrieve-then-answer对single-hop合理，却不能按evidence gap改写query或停止；新约束是把Search/Finish变成显式action并维护bounded reasoning chain。
- **Mechanism / State / Flow:** observation → thought → `Search`或`Finish` → retrieved document → updated state；query、evidence/provenance、chain budget与final answer分别归agent/retriever/runtime所有。
- **Evaluation Contract:** MuSiQue、HotpotQA、IIRC、NQ；比较GLM/QwQ/Self-RAG/Search-o1等，使用EM与GPT-4o judge。model/hardware/precision、online index freshness、network latency、concurrency与SLO未形成统一contract。
- **Evidence / Non-evidence / Limits:** 支持local-document multi-hop QA中的iterative search；不证明live-web factuality、citation correctness、tool safety或reflection causality。discarded trajectories、answer-model confound、overthinking和search cost是风险。
- **Trade-off / Previous Design / Evolution:** 证据覆盖换latency与stop-policy failure；single-hop/evidence known时一次retrieval仍更简单。`Direct Evolution`：static RAG → iterative RAG → policy-controlled retrieval。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `AGENT-RAG` / Ch76 / legacy Ch72；已读Ch75～77并核对Ch79。Ch76已覆盖iterative retrieval、sufficiency、stop和evidence boundary。`Audit Complete — Books Pending`；待独立归因retrieval miss、reasoning error与answer error。

### LeX-Art

- **Candidate / Week / Score / Source Family:** LeX-Art / 2025-W13 / 22/30 / `lex-art-2503.21749`；arXiv:2503.21749，仅v1 2025-03-27。已读data construction、prompt enhancer、training、PNED evaluator、evaluation与limitations。
- **Problem / Previous Design / Changed Constraint:** generic T2I data/evaluators适合自然图像，却不能充分测复杂visual-text layout；约束变成共同管理synthetic data provenance、prompt refinement、generation filter和domain evaluator。
- **Mechanism / State / Flow:** DeepSeek-R1 prompt refinement → T2I synth/filter/recaption → LeX-10K；LeX-R1-60K distills enhancer，再训练FLUX/Lumina。PNED以NED matrix + Hungarian matching评分；generator、teacher、filter、captioner与evaluator revisions必须绑定。
- **Evaluation Contract:** LeX-Bench 1,310 prompts；PNED、OCR recall、aesthetic、CLIP、text attributes及pipeline ablation。hardware/precision/batch/concurrency/SLO `Not Disclosed`，composite pipeline没有完全隔离单因素贡献。
- **Evidence / Non-evidence / Limits:** 支持该组合改善visual-text rendering；不证明增益来自单一环节或跨domain通用。R1/GPT-4o label bias、OCR error、小数据与train/eval关联是threats。
- **Trade-off / Previous Design / Evolution:** domain coverage换synthetic/judge coupling与资产治理成本；有高质量human data/eval时人工curation仍更稳。`Layering`：data pipeline + task model + evaluator co-design。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `TRAIN-DATA` / Ch27 / legacy Ch23；已读Ch26～28并核对Ch24/Ch66。Ch27已有synthetic provenance/filter contract。`Audit Complete — Books Pending`；待做data/model/evaluator cross-swap归因。

### VBench 2.0

- **Candidate / Week / Score / Source Family:** VBench 2.0 / 2025-W13 / 24/30 / `vbench2-2503.21755`；arXiv:2503.21755 v1 2025-03-27、v2 08-20。已读taxonomy、generalist/specialist evaluators、human alignment、model comparison与limitations。
- **Problem / Previous Design / Changed Constraint:** aesthetics/temporal consistency对媒体生产合理，却无法诊断anatomy、physics与commonsense；约束转为多维证据且必须隔离judge、model version、fps/resolution差异。
- **Mechanism / State / Flow:** 五类18维；generalist VLM/LLM judge与anomaly/face/tracking/flow specialist组合。prompt set、generated artifact、model/version、evaluator和aggregation policy共同定义run identity。
- **Evaluation Contract:** 每维约70 prompts；HunyuanVideo、CogVideoX1.5、Sora、Kling；human-preference alignment；生成用8×A100，但模型length/resolution/fps不一致，不能横向归因production performance。
- **Evidence / Non-evidence / Limits:** 支持更细video diagnostics；不证明generator拥有causal world model。judge dependence、四模型、小prompt suite、aggregate correlation和API drift限制外推。
- **Trade-off / Previous Design / Evolution:** 诊断性换多evaluator校准/成本；旧aesthetic/temporal指标仍适用于media quality，不能被physics维度覆盖。`Direct Evolution`：surface metrics → intrinsic-faithfulness diagnostics → intervention evaluation（尚未实现）。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `PLATFORM-EVALUATION-SYSTEM` / Ch66 / legacy Ch62；已读Ch65～67并核对Ch25。Ch66已有model-judge calibration，Ch25区分video generation/world model。`Audit Complete — Books Pending`；待用controllable counterfactual environment test验证physics。

### Lumina-Image 2.0

- **Candidate / Week / Score / Source Family:** Lumina-Image 2.0 / 2025-W13 / 25/30 / `lumina-image2-2503.21758`；arXiv:2503.21758，仅v1 2025-03-27。已读architecture、UniCap/data stages、sampler/CFG、evaluation、ablation与limitations。
- **Problem / Previous Design / Changed Constraint:** double-stream text/image architecture易保持modality specialization，固定sampler成熟可靠；约束转为统一stream、逐级resolution训练和更少sampling steps，同时不能混淆architecture/data/sampler贡献。
- **Mechanism / State / Flow:** Unified Next-DiT把text/image tokens置于同一stream；UniCap生成多粒度caption；progressive 256²→1024²→HQ training；CFG-Renorm/Trunc与Flow-DPM控制generation trajectory。caption、dataset stage、sampler与artifact revision均需versioning。
- **Implementation / Evaluation Contract:** 2.6B/26 layers/M-RoPE/Gemma encoder；100M 256²、10M 1024²、1M HQ，约191/176/224 A100 GPU-days，AdamW、LR2e-4。GenEval、DPG、T2I-CompBench与online arena；含sampler/CFG ablation。Flow-DPM更快但不稳定，TeaCache易模糊；online concurrency/SLO未披露。
- **Evidence / Non-evidence / Limits:** 支持统一stream和staged training可行；不证明优于所有double-stream或samplers，也未完全隔离architecture/caption/budget贡献。captioner bias、多阶段artifact和benchmark/human mismatch是风险。
- **Trade-off / Previous Design / Evolution:** interface统一换modality interference与复杂training lineage；条件少、专用encoder或成熟sampler时旧方案仍合理。`Direct Evolution`：separate streams → unified tokens → staged data/sampler co-design。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 / legacy N/A；已读Ch23～25并核对Ch27/Ch49。Ch24已有生成范式/sampler trade-off，Ch23拥有joint representation identity。`Audit Complete — Books Pending`；待归因architecture、caption quality和training budget。

### Video-R1

- **Candidate / Week / Score / Source Family:** Video-R1 / 2025-W13 / 27/30 / `video-r1-2503.21776`；arXiv:2503.21776 v1 2025-03-27，后续v2～v4只作revision。已读SFT/RL data、T-GRPO reward、implementation、evaluation、ablation与limitations。
- **Problem / Previous Design / Changed Constraint:** multimodal SFT稳定但可能依赖静态shortcut；普通outcome RL又不能区分temporal order。新约束是用ordered-vs-shuffled contrast形成temporal reward，同时绑定frame sampling和双trajectory成本。
- **Mechanism / State / Flow:** Qwen2.5-VL-7B，165K CoT SFT冷启动 + 260K image/video RL；T-GRPO比较ordered与shuffled video reward。video/frame order、rollout pair、reward与policy version是独立state。
- **Implementation / Evaluation Contract:** 4×H20-96GB；train最多16 frames、inference 16–32；六个video benchmarks，exact/WER/ROUGE/regression rewards，含no-image/no-temporal ablation。batch、rollout concurrency、precision与serving SLO未完整披露。
- **Evidence / Non-evidence / Limits:** 支持该training mixture/temporal contrast改善所测benchmark；不证明shuffle reward捕获因果temporal reasoning或RL普遍优于SFT。双序列compute、frame bias与reward/benchmark mismatch是风险。
- **Trade-off / Previous Design / Evolution:** temporal signal换2× observation/rollout和artifact sensitivity；静态任务、demonstration充足或reward不可验证时SFT仍合理。`Alternative Branch`：multimodal SFT → outcome RL → contrastive temporal RL。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `TRAIN-GRPO` / Ch33 / legacy Ch29；已读Ch32～34并核对Ch23/Ch66。Ch33已有GRPO/zero-variance/reward contract。`Audit Complete — Books Pending`；待排除static shortcut与shuffle artifact。

### Understanding R1-Zero-Like Training / Dr. GRPO

- **Candidate / Week / Score / Source Family:** Understanding R1-Zero-Like Training / 2025-W13 / 29/30 / `r1-zero-critical-drgrpo-2503.20783`；arXiv:2503.20783 v1 2025-03-26、v2 2025-10-06。已读base/template analysis、GRPO normalization derivation、Dr. GRPO、training/evaluation、ablation与limitations。
- **Problem / Previous Design / Changed Constraint:** GRPO以group-relative reward省去critic，结构简单；但per-response length normalization与per-question reward-std normalization引入length/difficulty bias，且R1-Zero结果还混入base/template/pretraining priors。
- **Mechanism / State / Flow:** Dr. GRPO移除两种normalization，使用固定generation-budget denominator；prompt group、token length、reward statistics、policy/reference与generation budget分别versioned。
- **Implementation / Evaluation Contract:** Qwen2.5、Llama3.1、DeepSeek-V3 base；MATH/AIME/AMC/Minerva/Olympiad；7B recipe在8×A100约27h；包含base/template、coverage、domain pretraining与algorithm ablation。precision、rollout concurrency和production SLO未完整披露。
- **Evidence / Non-evidence / Limits:** 支持math contract中standard GRPO optimization bias与无效length growth；不证明shorter就是better reasoning，也不证明跨domain/reward/tool-cost通用。fixed denominator仍需budget/reward calibration。
- **Trade-off / Previous Design / Evolution:** 去除adaptive normalization换更明确的budget scale；group-relative GRPO在长度同质且std稳定时仍合理。`Direct Evolution`：GRPO normalization → bias diagnosis → fixed-budget denominator。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `TRAIN-GRPO` / Ch33 / legacy Ch29；已读Ch32～34并核对Ch28。Ch33已有group normalization contract，此项是denominator/length-bias核心证据。`Audit Complete — Books Pending`；待扩展到non-binary/process rewards与variable-cost tools。

### CodeARC

- **Candidate / Week / Score / Source Family:** CodeARC / 2025-W13 / 25/30 / `codearc-2503.23145`；arXiv:2503.23145 v1 2025-03-29、v2 08-08。已读interactive protocol、oracle、dataset construction、training/evaluation与limitations。
- **Problem / Previous Design / Changed Constraint:** static pass@k在pure functions和完整tests下简单可复现，却不能测主动query和counterexample-driven correction；新约束是把environment opportunity与model ability分开记账。
- **Mechanism / State / Flow:** Agent从10个I/O examples开始，可查询hidden function，总I/O budget30，最多2次differential oracle counterexample；hidden target、budget、candidate program、counterexample、execution trace共同定义run。
- **Evaluation Contract:** HumanEval+/MBPP+/APPS派生1,114 functions，18 models；o3-mini 52.7%；Llama3.1-8B使用GPT-4o privileged traces fine-tune。oracle由Pynguin/Mokav近似，不是program equivalence proof；hardware/precision/concurrency/SLO未披露。
- **Evidence / Non-evidence / Limits:** 支持interactive executable evaluation观察self-correction；不证明oracle完备，也不能把tool opportunity算成纯model capability。benchmark contamination、teacher privilege、Python subset与sandbox风险限制外推。
- **Trade-off / Previous Design / Evolution:** 诊断性换oracle/environment维护和安全成本；tests完备时static executable evaluation仍更简单。`Direct Evolution`：static tests → adaptive query → counterexample loop。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `PLATFORM-EVALUATION-SYSTEM` / Ch66 / legacy Ch62；已读Ch65～67并核对Ch81。Ch66已有artifact/harness opportunity/trajectory-outcome separation。`Audit Complete — Books Pending`；待把oracle opportunity与model ability独立计分。

### Quamba2

- **Candidate / Week / Score / Source Family:** Quamba2 / 2025-W13 / 28/30 / `quamba2-2503.22879`；arXiv:2503.22879 v1 2025-03-28，v2/v3/v4作revision。已读SSM-aware PTQ、state grouping、kernels、mixed precision search、evaluation、ablation与limitations。
- **Problem / Previous Design / Changed Constraint:** generic per-tensor/PTQ和FP16在成熟kernel上简单稳定，但Mamba input-dependent recurrence会放大量化误差；约束变为保持state ordering并为hardware提供fused execution plan。
- **Mechanism / State / Flow:** activation排序聚类，B/C用per-state-group quantization；offline重排weights保持recurrence ordering，配fused Hadamard/custom CUDA；artifact包含calibration、grouping、bit-width和kernel compatibility。
- **Implementation / Evaluation Contract:** W8A8/W4A8/W4A16及mixed-sensitive-layer search；Mamba1/2至8B，LM-Eval六项/MMLU；A5000、Orin Nano，batch1、prompt1024测TTFT/TPOT；与MambaQuant/Quamba比较并做component/bit ablation。
- **Evidence / Non-evidence / Limits:** 支持所测SSM/hardware的memory/latency改善；不证明Transformer、大batch、超长decode或其他kernels。accuracy degradation、state grouping、calibration和hardware-specific code是风险。
- **Trade-off / Previous Design / Evolution:** memory/edge latency换artifact/kernel复杂度；quality/SLO优先或缺专用kernel时FP16/W8A8仍合理。`Direct Evolution`：generic PTQ → architecture-aware state grouping → fused hardware execution。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `INFER-TENSORRT-LLM` / Ch49 / legacy Ch45；已读Ch48～50并核对Ch54。Ch49已是execution-plan/quantization owner，覆盖distribution-conditioned admission。`Audit Complete — Books Pending`；待验证超长recurrence error与batch/concurrency变化。

### Landscape of Thoughts

- **Candidate / Week / Score / Source Family:** Landscape of Thoughts / 2025-W13 / 24/30 / `landscape-of-thoughts-2503.22165`；arXiv:2503.22165 v1 2025-03-28，后续v2～v4只作revision。已读feature construction、visualization/verifier、evaluation、comparison与limitations。
- **Problem / Previous Design / Changed Constraint:** outcome accuracy和trace text可测最终表现，却难观察multiple-choice trajectory在candidate space中的移动；新约束是提供diagnostic projection，同时不得把投影误当causal internal state。
- **Mechanism / State / Flow:** 构造到answer choices的normalized probability/distance features，以t-SNE可视化并训练random-forest verifier；trajectory、candidate labels、token probabilities、projection与verifier version分别保存。
- **Evaluation Contract:** Llama3.1-70B为主，多MC datasets，CoT/LtM/MCTS/ToT；每类可视切片约50 questions，测consistency、entropy、thought perplexity和weighted voting。hardware/precision/batch/concurrency/SLO未披露。
- **Evidence / Non-evidence / Limits:** 支持answer-conditioned features对correct/incorrect trajectory有诊断信息；不证明内部causal reasoning state。t-SNE distortion、小样本、MC-only、probability access与distribution leakage是风险。
- **Trade-off / Previous Design / Evolution:** 可视诊断换projection/verifier bias；free-form/open-ended无显式candidate时普通trace/outcome eval更适用。`Explanatory Analogy`：probability landscape不是物理路径。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `PLATFORM-EVALUATION-SYSTEM` / Ch66 / legacy Ch62；已读Ch65～67并核对Ch69。Ch66已有trajectory uncertainty，Ch69已有execution trace，均禁止把projection当真实state。`Audit Complete — Books Pending / Experimental`；待跨模型/dataset calibration。

### Towards Trustworthy GUI Agents: A Survey

- **Candidate / Week / Score / Source Family:** Towards Trustworthy GUI Agents / 2025-W13 / 19/30 / `trustworthy-gui-agent-survey-2503.23434`；arXiv:2503.23434 v1 2025-03-30、v2 2026-02-24。v1 identity/date/PDF边界已核验；v2 taxonomy不倒写。
- **Source / Rejection Boundary:** secondary survey，不拥有primary mechanism或独立evaluation contract；与Ch72/Ch84已有trust、least privilege、effect-time authorization和trajectory safety高度重合。
- **Owner / Adjacent / Decision:** `PLATFORM-SECURITY` / Ch72 / legacy Ch68，handoff `AGENT-PLATFORM` Ch84 / legacy Ch80；已核对相邻安全/平台章节。`Weekly Only — Secondary Source Map`，Blocked=No，Books不吸收。

### vLLM 2025 Q2 roadmap

- **Candidate / Week / Score / Source Family:** vLLM 2025 Q2 roadmap / 2025-W13 / 16/30 / `vllm-2025q2-roadmap`；official GitHub issue #15735，创建于2025-03-29。
- **Source / Evidence / Rejection Boundary:** issue列出V1 feature closure、cluster-scale serving、PD disaggregation、KV offload、production testing与hardware/plugin方向；它是living planning document，只证明维护者当时的意图，不证明任一条目已经实现、达到性能目标或具有稳定API。
- **Owner / Adjacent / Decision:** `INFER-VLLM` / Ch50 / legacy Ch46，handoff Ch52、Ch55～56；已核对execution/runtime与distributed scheduling边界。最终为`Weekly Only — Planning Intent`，Blocked=No；交付事实必须由后续release/RFC/PR单独核验。

### Shape and Texture Recognition in Large Vision-Language Models

- **Candidate / Week / Score / Source Family:** 2025-W13 / 18/30 / `shape-texture-lvlm-2503.23062`；arXiv:2503.23062，v1 2025-03-29；后续v2～v5只作revision history。
- **Source / Evidence / Rejection Boundary:** primary benchmark已核验；它显示所测LVLM在shape/texture recognition上的低层表征弱点，但没有提出新的representation、training或runtime机制，也不能把benchmark weakness外推到所有LVLM。
- **Owner / Adjacent / Decision:** `MULTIMODAL-REPRESENTATION` / Ch23，handoff `PLATFORM-EVALUATION-SYSTEM` / Ch66；已核对相邻章节，最终为`Low Score — Representation Diagnostic Only`，Blocked=No。

### A Survey on Unlearnable Data

- **Candidate / Week / Score / Source Family:** 2025-W13 / 19/30 / `unlearnable-data-survey-2503.23536`；arXiv:2503.23536，v1 2025-03-30，v2/v3只作revision history。
- **Source / Evidence / Rejection Boundary:** secondary survey identity、scope和references已核验；可作poisoning/privacy/data-protection的source map，但不拥有primary mechanism或独立evaluation contract。
- **Owner / Adjacent / Decision:** `TRAIN-DATA` / Ch27，handoff `PLATFORM-SECURITY` / Ch72；最终为`Weekly Only — Secondary Synthesis`，Blocked=No。

### Anthropic Economic Index: Insights from Claude 3.7 Sonnet

- **Candidate / Week / Score / Source Family:** 2025-W13 / 18/30 / `anthropic-economic-index-claude37`；official report，2025-03-27。
- **Source / Evidence / Rejection Boundary:** 1M匿名Claude.ai conversations结合Clio/O*NET taxonomy只支持平台内usage与sampling evidence；产品选择、自选择、taxonomy和平台分布限制使其不能改变模型或AI System机制结论。
- **Owner / Adjacent / Decision:** `PLATFORM-EVALUATION-SYSTEM` / Ch66 / legacy Ch62；最终为`Weekly Only — Usage/Sampling Evidence`，Blocked=No。

### Meta / Cornerstone XR Training with Llama

- **Candidate / Week / Score / Source Family:** 2025-W13 / 10/30 / `meta-cornerstone-xr-llama-case`；official customer case，2025-03-26。
- **Source / Evidence / Rejection Boundary:** 公开内容仅说明使用Llama 3.1 8B、fine-tuning、RAG与prompt syntax驱动XR角色；训练、控制、安全、evaluation和runtime contract均未披露，不能据此推导新机制。
- **Owner / Adjacent / Decision:** 如保留仅映射`AGENT-WORKFLOW` / Ch81 / legacy Ch77；最终为`Ignored Noise — Product Case`，Blocked=No。

### JavisDiT: Joint Audio-Video Diffusion Transformer with Hierarchical Spatio-Temporal Prior Synchronization

- **Identity / coverage:** Source Family `ARXIV-2503.23377-JAVISDIT`，v1 first-public 2025-03-30 09:40:42 UTC，27/30；v2/ICLR 2026只作forward revision，2025-04-08 code release应归W15 forward artifact node。v1 Abstract、Related Work、Method/公式、Implementation、Evaluation、Ablation、Conclusion及Appendix A～F均已读；event-time code/model/data未公开。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch23与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Problem / previous / changed constraint:** T2A→A2V或T2V→V2A级联可复用成熟单模态generator、便于替换和归因，粗粒度joint coupling也能提供基础语义一致性；但复杂多声源、离屏声源、顺序/并发事件使上游误差放大，文本又不唯一规定事件的空间与时间，系统必须表达欠定性并维护paired mutable state，而非伪造唯一alignment。
- **Mechanism / state / flow:** 两个28-block、16-head、hidden1152的audio/video DiT并发做rectified-flow去噪。每层沿spatial/temporal轴执行self-attention、text cross-attention、ST-prior cross-attention、双向A/V cross-attention与FFN。HiST-Sypo以T5提供coarse semantics，ImageBind states和32 spatial+32 temporal queries经4层Transformer估计Gaussian `mu/sigma`并采样fine prior；同步A/V为正样本、空间/时间变换为负样本。BiCrossAttn共享attention matrix及transpose双向更新两侧。数据管线拥有A/V/text/timestamp/codec identity，prior拥有RNG与条件，audio/video branches各自拥有mutable latent，sampler拥有step/noise/CFG，最终必须paired atomic commit，不能单侧提交后仍声称同步。
- **Implementation / evaluation contract:** 总3.14B。Stage1从frozen OpenSora video weights初始化audio branch，用788K audio-caption、13 epochs；Stage2在611K同步triplets+异步负样本上训练prior，1 epoch、lr`1e-5`；Stage3冻结两侧self-attention与prior，只训练ST/Bi-cross，611K、2 epochs、lr`1e-4`。OpenSora/AudioLDM2 VAE冻结，bucketing为144p～1080p、2～16s；optimizer、global batch、training topology、precision与seeds多项未披露。推理30 steps、CFG7；作者称2s 720p/24fps/16kHz单H100约6分钟，未披露concurrency/SLO/energy。
- **Baselines / evidence boundary:** JavisBench 10,140 clips/5 dimensions/19 categories，mini 1K；JavisScore按2s window、1.5s overlap，用ImageBind A/V embeddings并取least-synchronized 40% frames均值。metric validation 3,000 pairs，作者报accuracy约75%；主评测240p/24fps/4s/16kHz，与AudioLDM2→A2V、OpenSora→V2A、MM-Diffusion等比较。60K subset消融支持ST attention、stochastic prior和bidirectional exchange在作者AVQ/AVC/AVS代理指标上各有增益。只证明该数据/代理metric下joint paired latent sampling可行，不证明prior恢复真实因果事件位置、ImageBind等同人类同步感知、joint普遍优于cascade、长程production稳定或event-time artifact可复现。
- **Trade-off / coexistence / disposition:** stochastic prior表达欠定性却引入run variance与控制歧义；joint coupling会跨模态传播错误并增加attention、显存和同步状态，冻结又可能锁死弱单模态表示；训练/评估同依赖ImageBind存在proxy circularity，paired partial failure会产生split-brain。authoritative单模态、低延迟SLO、paired data少、需独立替换/观测或一侧质量显著更成熟时cascade仍合理。演进为`one-way cascade → coarse joint coupling → joint mutable A/V state + stochastic ST prior → paired commit/evaluation`，不是World Model。Ch24缺paired commit与cross-modal synchronization state，future `Refine — Existing Argument / Experimental`；当前Books Frozen。
- **Open Questions:** event-time code/weights/data snapshot、human-calibrated scorer、long-form drift、paired rollback/partial failure与independent replication仍待验证。

### AdaptiVocab：缩短token sequence需要原子化model-tokenizer artifact

- **Identity / Coverage:** arXiv:2503.19693 v1于2025-03-25公开，26/30，`ARXIV-2503.19693-ADAPTIVOCAB`；v2/COLM及2025-08-29 GitHub initial commit均为forward evidence。已读v1 27页、Algorithms 1–2、全部实验与Appendix A–E；事件时code/data不可验证，故paper strict complete但非artifact reproduced。
- **Problem / Mechanism:** 通用tokenizer为开放域与checkpoint生态稳定而合理，但focused domain会把高频短语拆长。方法保持V不变，按frequency/overlap选择domain n-token替换rare IDs；removed token依merge table递归decompose，再longest-first merge。input row用递增权重强调末token，LM-head row用递减权重强调首token，并微调embedding、LM head和first/last layer。
- **State / Atomic Contract:** builder拥有corpus/tokenizer/merge table/candidate counts/ID remap；adaptor拥有rows/layers/base checkpoint；serving tokenizer拥有encode/decode patch、special-token与fallback。base architecture + weights + patched tokenizer + vocab map + LM head + generation metadata必须原子发布，否则silent semantic corruption；adapter、draft model、grammar/safety filter也需重验。
- **Evaluation / Boundary:** Mistral-v0.3 7B与Llama-2 7B、三个手选英文域；max n=3、replace10K，RTX A6000 48GB。相同输入token saving约22.9%–28.6%，FT后judge/QA接近baseline；但output saving对应不同生成文本。无wall-clock latency、TTFT/ITL、batch/concurrency、KV、tokenizer CPU cost或seeds/CI。只测BPE却声称any tokenizer/architecture，tied weights下相反row init也未处理，不能把25% token saving写成25% cost。
- **Trade-off / Owner / Decision:** 固定V不减少projection shape，新增domain routing、多variant storage、OOD rare-token fragmentation、domain drift、larger rollback unit、cache/speculation/structured-decoding和accounting incompatibility。通用、多语言、多域或强生态兼容时原tokenizer仍合理。owner `MODEL-TOKENIZER` Ch11，handoff Ch12/18/35/44；`Full Source Review Complete — Refine Existing Argument Candidate / Experimental`，Historical Books Gate关闭。

### Exploring Data Scaling Trends and Effects in Reinforcement Learning from Human Feedback

- **Candidate / Week / Score:** Exploring Data Scaling Trends and Effects in RLHF / 2025-W13 / 28/30。
- **Source Family ID:** `ARXIV-2503.22230-RLHF-DATA-SCALING`。
- **Source Type:** author primary research paper；event-time arXiv v1 HTML/PDF。
- **Event Date / First-public Date / Revision History:** arXiv v1于2025-03-28公开，归2025-W13。本文只使用
  `2503.22230v1`；后续NeurIPS 2025/OpenReview材料属于forward revision，不倒写进事件周。
- **Direct Primary Sources:** `https://arxiv.org/html/2503.22230v1`与
  `https://arxiv.org/pdf/2503.22230v1`。
- **Related Primary Sources:** 后续OpenReview版本只用于确认family lineage；事件时未找到作者公开代码、训练数据快照、
  reward model或evaluation artifact，因此不把artifact reproduction计为已完成。
- **Access and Verification Status:** Verified — event-time v1全文可访问；ordinary Review Pending已解除。
- **Full-read Coverage:** metadata、Abstract、Introduction、RLHF pipeline、Pre-PPO、curriculum、实验设置、Tables 1～3、
  ablation、reward-hacking与entropy分析、Discussion、Conclusion以及Appendix中的prompt分布、entropy图和case studies均已读。
- **Original Problem:** RLHF扩大prompt数量后并不自动延长有效学习：容易的prompt已被当前policy掌握，弱reward proxy又会让
  policy学习可得高分的syntactic shortcut；继续优化同时压低response diversity，最终出现reward上升但外部测试先升后降。
- **Why the Previous Design Was Reasonable:** 在prompt稀缺、policy弱且reward model覆盖训练分布时，均匀抽取更多prompt并用
  单一BT/GenRM做PPO最简单，所有样本共享一条数据管线、同一个reward interface与调度策略，便于复现与扩容。数量在普通
  supervised learning中也常是有效杠杆，因此先扩大dataset是合理baseline。
- **Changed Constraint:** 原1M prompts扩展5M open-source prompts后，作者的initial run并未优于baseline，约3500 step后
  evaluation下降；约90%新增prompts的reward score高于reference，说明“新收集”不等于对当前policy仍有训练信息。不同domain
  的reward distribution、verifier强度与response granularity又不可直接比较。
- **Mechanism:** Pre-PPO先用small policy/GenRM评分6M prompt pool，在domain内标准化score并只选bottom 10%难例，再与原始
  prompt set组合训练；为减少成本，large model复用small-model selection而不重做选择。训练curriculum从coding-only开始，逐步
  加入math，最后进入mixed-domain。Reward path联合BT、pairwise GenRM与Reasoning Task Verifier：reasoning任务可给GenRM
  ground-truth reference，代码可进入sandbox等RTV，其他任务的GenRM target来自SFT Best-of-N；policy用PPO优化并限制偏离原policy。
- **State Ownership:** data pipeline拥有prompt identity、domain、来源与selection snapshot；reward subsystem拥有BT/GenRM/RTV
  类型、ground-truth或SFT-BoN lineage、normalization version与score；curriculum controller拥有domain mixture和global step；
  learner拥有policy/reference/value、optimizer与checkpoint；evaluator必须独立拥有V1/V2/human slice和checkpoint-selection规则。
- **Control Flow / Data Flow:** `1M original + 5M collected prompts → small-policy responses → domain-normalized GenRM score →
  bottom-10% selection → coding→math→mixed curriculum → PPO with hybrid rewards/KL → every-100-step evaluation → best checkpoint`。
  large model沿用small-model选出的prompt identity，这一transfer是实验假设，不是无损系统属性。
- **Implementation Details:** 两个未命名pretrained model约25B与150B参数；PPO目标只披露“minimal deviation from original
  policy”。论文没有公开optimizer、learning rate、global batch、rollout batch/concurrency、KL coefficient、reward权重、
  sampling参数、token length、training topology、precision、seed、wall-clock或checkpoint policy。
- **Evaluation Contract:** TestSet V1/V2覆盖logical reasoning、instruction following、STEM、coding、NLP、knowledge、contextual
  understanding与OOD；两版有prompt overlap，V2更难。自动评估每100 steps用于选择4000步内最佳checkpoint，另有新subset的
  human evaluation。论文未披露完整dataset、judge prompt、per-slice样本量与生产SLO，因此分数只属于作者evaluation contract。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比original-data PPO baseline、expanded-data initial run、Pre-PPO、early
  math/code emphasis与二者组合。small-model ablation显示Pre-PPO把plateau从约2000步延后至4000步；large-model Table 3中
  Pre-PPO相对baseline overall约+1.1，加入curriculum后再约+0.3。将新增数据比例从10%扩到20%/50%反而下降。RTV、带ground-truth
  GenRM与BT/SFT-BoN GenRM在作者run中依次表现出更晚的退化窗口，但不是跨任务统一排序。prompt filtering与多reward服务的
  scoring、sandbox和storage开销未量化。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model约25B/150B；hardware、precision、输入/输出长度、
  batch、rollout并发、集群规模、吞吐、成本、latency与SLO均`Not Disclosed`。因此不能从分数推导训练效率或生产成本结论。
- **What the Evidence Proves:** 在作者两种model size、prompt pool、reward stack与evaluation上，按policy难度筛选prompt并把
  verifier较强的coding/math提前，可以比original-data PPO更晚达到plateau；V1/V2 overall约+1.1/+1.4，且某些slice有提升。
  人评overall为+4.4但`p=0.12`，不能称整体显著；部分individual dimensions显著，部分自动评测slice下降。
- **What It Does Not Prove:** 不证明RLHF存在随prompt数量单调增长的普适scaling law，不证明bottom-10%对其他policy/RM/domain
  最优，不证明small→large selection或hyperparameter transfer可靠，不证明RTV不会被hack，也不证明reward hacking或diversity
  collapse已被消除。Edit distance只是昂贵的coarse proxy，作者明确没有按它执行完整curriculum实验。
- **Limitations / Threats to Validity:** model与数据身份不公开、训练recipe和artifact缺失、V1/V2有overlap、best-checkpoint
  selection可能产生选择偏差、human overall未达统计显著、reward与test可能共享domain assumptions。作者对fine-grained-first
  的因果解释主要是hypothesis；creative/cosplay entropy上升、reasoning entropy下降也不能被压缩为“diversity普遍改善”。
- **Trade-offs / New Failure Modes:** difficulty mining提高有效样本密度，却带来selector bias、跨policy staleness、domain
  normalization drift和small-model blind spot；verifier-weighted curriculum减少部分proxy hacking，却会偏向可执行验证领域，弱化开放式
  preference任务；多reward ownership、sandbox安全、version skew与best-checkpoint leakage均成为新failure mode。
- **Where the Previous Design Still Applies:** policy较弱、prompt pool小、reward calibration稳定，或系统无法承担预评分与多verifier
  orchestration时，随机/均匀sampling与单reward pipeline仍是更清晰baseline；开放式创作等缺可靠verifier的任务也不能机械套用
  code-first curriculum。
- **Evolution Relationship:** `more prompts → policy-relative difficulty selection → verifier-aware curriculum → versioned data/reward/
  evaluation control plane`；属于`Direct Evolution + Layering / Dependency`，不是“data scale越大越好”的替代结论。
- **ROADMAP Node:** canonical owner `TRAIN-RLHF`（Ch31，legacy Ch27）；handoff `TRAIN-PPO`（Ch32）、`TRAIN-DATA`（Ch27）与
  `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读Ch29 SFT、Ch31 RLHF、Ch32 PPO与Ch34 DPO的当前相关段落。
- **Existing Coverage:** Ch31已覆盖preference data分布漂移、reward hacking、verifier与curriculum，Ch32覆盖rollout/advantage；
  尚缺“prompt quantity受policy-relative informativeness与reward resolution约束”这一完整实证链，但Historical Books Gate关闭。
- **Integration Decision:** `Refine — Existing Argument Candidate / Experimental；Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 只更新本Weekly的source packet与Gate，不修改Books、ROADMAP、年度索引或Learning State。
- **Open Questions:** event-time artifact、完整PPO recipe、selector跨policy/scale漂移、独立复现、统计功效、长期reward hacking、
  sandbox threat model与production cost仍待验证。

### Megatron-LM Multi-Token Prediction support

- **Candidate / Week / Score:** Megatron-LM Multi-Token Prediction support / 2025-W13 / 25/30。
- **Source Family ID:** `MEGATRON-MTP-DC385C7-2025-03-30`。
- **Source Type:** official repository implementation commit + documentation + issue/merge confirmation + unit tests。
- **Event Date / First-public Date / Revision History:** issue #1404于2025-02-14提出；maintainer于2025-03-30明确确认MTP已通过
  commit `dc385c7`合入main，implementation event归W13。后续Megatron Core正式release与扩展支持属于forward evolution。
- **Direct Primary Sources:** commit `https://github.com/NVIDIA/Megatron-LM/commit/dc385c7`；issue
  `https://github.com/NVIDIA/Megatron-LM/issues/1404`；commit内event-time MTP文档、配置、model、pipeline、gradient finalize与unit test路径。
- **Related Primary Sources:** DeepSeek-V3 Technical Report只解释objective origin；不作为Megatron实现已交付的替代证据。
- **Access and Verification Status:** Verified — 16-file diff（+1,381/-22）、文档、配置、核心代码与unit tests均已检查。
- **Full-read Coverage:** commit metadata、MTP API guide、`multi_token_prediction.py`、GPT model/layer specs、pipeline schedule、
  embedding/output synchronization、argument plumbing、training loss path与`test_multi_token_prediction.py`。
- **Original Problem:** standard next-token pretraining每个position只提供一个future target，不能直接训练同一hidden state预测更远token；
  把MTP objective从论文移入大规模训练runtime，还必须解决多depth模块、shared weights、pipeline stage与loss/gradient ownership。
- **Why the Previous Design Was Reasonable:** next-token loss拥有单一label shift、单一output head和成熟pipeline schedule，最容易
  checkpoint、并行和debug；在模型质量目标已满足或额外objective的收益未证实时，它仍是最低风险训练contract。
- **Changed Constraint:** DeepSeek-V3式sequential MTP要求每个depth保留完整causal chain，同时在Megatron的pipeline/data parallel
  环境维护重复embedding、shared output与额外loss；只增加一个CLI flag而不修改stage placement和gradient synchronization会产生
  silent wrong training。
- **Mechanism:** 设置正整数`mtp_num_layers`后构建D个sequential modules；第k层把前一depth同位置representation与未来第k个
  token embedding经projection组合，再过Transformer block和shared output head预测额外token。各depth MTP loss先平均，再乘
  `mtp_loss_scaling_factor`（默认0.3）作为主loss之外的训练目标。
- **State Ownership:** model config拥有depth/loss factor；MTP block拥有各depth hidden state与label shift；embedding group拥有
  duplicated/shared embedding-output weights及其gradient all-reduce；pipeline scheduler拥有MTP process stage、activation传递和loss
  reduction；checkpoint必须保存model config、MTP parameters与shared-weight layout。
- **Control Flow / Data Flow:** token/position/attention state进入main GPT block；main hidden与shifted future embedding按depth串行融合，
  每层产生logits/loss；平均auxiliary loss回到training step；embedding/output parameters在pre/post/MTP process stage间同步。
- **Implementation Details:** commit增加文档、Transformer MTP模块、GPT layer/model wiring、pipeline schedule、distributed gradient
  finalize、training argument与unit tests；同一次提交明确`Context Parallel`、arbitrary `AttnMaskType`与learned absolute position
  embedding尚不支持。当前实现把MTP层放在同一pipeline stage，placement自由度受限。
- **Evaluation Contract / Baselines / Ablations / Sensitivity / Overhead:** commit提供unit-level correctness与wiring evidence，没有公开
  end-to-end model-quality baseline、ablation、acceptance-rate、training throughput、memory、communication、scaling sensitivity或
  failure-recovery benchmark；默认0.3只是implementation default，不是普适最优值。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 未披露验证hardware、model size、precision、sequence length、
  global/micro batch、parallel degrees、throughput、cost或SLO；全部记为`Not Disclosed`。
- **What the Evidence Proves:** 2025-03-30的MCore main已经包含可配置的sequential MTP objective、pipeline/loss/weight-sync wiring和
  unit tests；这是一条公开implementation path，而不再只是paper proposal。
- **What It Does Not Prove:** 不证明MTP必然提高模型质量、data efficiency或speculative acceptance，不证明在任意parallel topology、
  mask、position scheme和checkpoint migration下正确，也不证明生产集群已有采用或性能收益。
- **Limitations / Threats to Validity:** merge commit缺独立benchmark和artifact run log；unsupported combinations明确存在；同stage
  placement可能形成memory/compute hotspot。unit tests只能覆盖已编码case，不能替代large-scale convergence与resume validation。
- **Trade-offs / New Failure Modes:** 更密训练信号换来额外Transformer计算、activation/gradient、loss权重调参、shared-weight通信、
  pipeline imbalance和checkpoint schema；配置或label shift错误会silent corruption，loss factor过高可能改变主objective。
- **Where the Previous Design Still Applies:** quality收益不确定、显存/通信受限、需要Context Parallel/learned absolute positions，或
  ecosystem/checkpoint兼容性优先时，纯next-token training仍更合理。
- **Evolution Relationship:** `paper objective → framework-native sequential modules → distributed shared-state contract → future serving
  draft/artifact lifecycle`；属于`Direct Evolution + Layering / Dependency`，不与普通next-token objective互斥。
- **ROADMAP Node:** canonical owner `TRAIN-PRETRAINING`（Ch28，legacy Ch24）；handoff
  `TRAIN-DISTRIBUTED-TRAINING`（Ch36，legacy Ch32）和未来speculative-serving节点。
- **Target and Adjacent Chapters Read:** 已读Ch28 Pretraining、Ch35 Checkpoint与Ch36 Distributed Training的相关state contract。
- **Existing Coverage:** Ch28已有next-token objective与training-state流，Ch36已有parallel ownership；尚未以event-time MCore案例
  连接auxiliary future-token loss、shared embedding和pipeline placement，但Books Gate关闭。
- **Integration Decision:** `Refine — Existing Argument Candidate / Implementation Fact；Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 只在本Weekly补回owner、score、review和source；不修改Books或其他账本。
- **Open Questions:** event-time large-scale convergence、quality/throughput/memory曲线、world-size resume、不同MTP depth/loss factor、
  pipeline rebalance和后续draft-serving compatibility仍待验证。

### Pending、Blocked 与 Low-score Ledger

#### 补充低分候选的来源、日期、评分与拒绝闭合

- **LEGO-Puzzles / 19/30（3/2/4/4/3/3） / `ARXIV-2503.19990-LEGO-PUZZLES`:** arXiv v1于
  2025-03-25 18:21:07 UTC公开；后续v2～v4不倒写事件周。primary benchmark只建立多步空间推理的受限测量面，
  没有新的representation、training、planning或runtime机制，结果也不能外推到所有MLLM与physical control，故
  `Weekly Only — Narrow Benchmark Scope`，Blocked=No。
- **ViLBench / 19/30（3/3/3/4/3/3） / `ARXIV-2503.20271-VILBENCH`:** arXiv v1于
  2025-03-26 06:38:31 UTC公开。论文提供vision-language process-reward评测与受限训练案例，但本周评分门槛下主要是
  evaluation evidence；它没有形成可跨任务复用的reward-state ownership、production verifier contract或独立系统机制，故
  `Weekly Only — Narrow Evaluation Evidence`，Blocked=No。
- **Synthetic Video Enhances Physical Fidelity in Video Synthesis / 19/30（3/3/3/4/3/3） /
  `ARXIV-2503.20822-SYNTHETIC-VIDEO-PHYSICAL-FIDELITY`:** arXiv v1于2025-03-26 00:45:07 UTC公开。
  primary paper支持作者数据与任务条件下synthetic rendered video可改善部分physical-fidelity proxy，却明确没有证明模型获得
  深层physics understanding，也没有建立通用world-state transition或closed-loop control contract；最终为
  `Weekly Only — Evaluation-bound Experimental Evidence`，Blocked=No。
- **OlymMATH / 19/30（3/3/3/4/3/3） / `ARXIV-2503.21380-OLYMMATH`:** arXiv v1于
  2025-03-27 11:20:17 UTC公开；v2/v3新增或修订内容不倒写W13。它是更困难的olympiad-level evaluation asset，
  能暴露语言、答案与formal-verification边界，但未提出新的reasoning、training或serving机制，故
  `Weekly Only — Incremental Benchmark Evidence`，Blocked=No。
- **Large Language Model Agent: A Survey on Methodology, Applications and Challenges / 19/30（2/3/3/4/3/4） /
  `ARXIV-2503.21460-LLM-AGENT-SURVEY`:** arXiv v1于2025-03-27 12:50:17 UTC公开。该文是329篇工作的
  secondary taxonomy与source map，不拥有primary mechanism、artifact或独立evaluation contract；Agent章节已有对应owner，故
  `Weekly Only — Secondary Synthesis`，Blocked=No。
- **Transformers 4.50 patch family / 14/30（1/2/4/5/1/1） /
  `HF-TRANSFORMERS-4.50-PATCHES-2025-W13`:** official GitHub release显示base `v4.50.0`于2025-03-21发布、
  canonical owner应在W12；W13只计`v4.50.1`（2025-03-25 14:34）、`v4.50.2`（2025-03-27 09:08）与
  `v4.50.3`（2025-03-28 18:21）。三项只闭合hub kernel、processor、generation、dtype等独立bug，未提供统一新机制、
  benchmark或workload/SLO contract，故`Weekly Only — Patch-family Implementation Facts`，Blocked=No。
- **Scaling Laws in Scientific Discovery with AI and Robot Scientists / 18/30（3/3/2/4/3/3） /
  `ARXIV-2503.22444-AI-ROBOT-SCIENTIST-SCALING-PERSPECTIVE`:** arXiv v1于2025-03-28 14:00:27 UTC公开，
  v2属于W14 revision。该文提出autonomous generalist scientist与未来scaling-law假设，但没有实际scaling dataset、fit、
  falsifiable exponent、closed-loop artifact或executable system contract，故`Weekly Only — Conceptual Perspective`，Blocked=No。

#### DeepSpeed v0.16.5 low-score closure

- **Candidate / Week / Score / Source Family:** DeepSpeed v0.16.5 / 2025-W13 / 16/30 /
  `DEEPSPEED-RELEASE-0.16.5-2025-03-27`。
- **Source / Date / Coverage:** official signed GitHub release `v0.16.5`，2025-03-27 21:47发布；release notes与linked PR identities
  已核验。内容包括Tecorigin SDAA accelerator、`offload_states`修复、TOCTOU→`fstat`修复、`torch.compile` graph-break修复、
  DeepSeek-V3 AutoTP和若干兼容/CI变化。
- **Rejection Boundary:** 这是跨多个独立patch的版本集合，没有统一的新系统机制、完整benchmark、hardware/model/precision/length/
  batch/concurrency/SLO contract或跨backend evaluation；不能把“支持/修复”外推为性能、可靠性或安全性普遍改善。
- **Owner / Decision:** 机制分别回到`TRAIN-DISTRIBUTED-TRAINING`、`INFER-TENSORRT-LLM`与platform security handoff；
  `Weekly Only — Patch-family Implementation Facts / Low Score`，Blocked=No。

- **Review Pending:** 0。RLHF Data Scaling已通过event-time v1 HTML/PDF完成Method、Evaluation、Ablation、Appendix、
  evidence boundary与相邻章节审计；Megatron MTP已完成commit/docs/code/tests strict review。
- **Blocked:** 0。CaMeL已通过arXiv v1 PDF、appendix与作者artifact恢复；W13只使用v1的67% AgentDojo结果，不把后续v2的77%/84%结果倒写进事件周。
- **Schema Pending:** 0。所有48项retained packet均已补齐previous-design、state/data/control flow、workload、
  evidence/non-evidence、adjacent chapters、Existing Coverage、disposition与Open Questions。
- **Low-score 14项:** LEGO Puzzles（19）、ViLBench（19）、Synthetic Video Physical Fidelity（19）、Olympiad Math Benchmark（19）、Agent Survey（19）、Towards Trustworthy GUI Agents（19）、Transformers 4.50 patch family（14）、DeepSpeed v0.16.5（16）、vLLM Q2 roadmap（16）、Shape and Texture Recognition（18）、Unlearnable Data Survey（19）、Anthropic Economic Index（18）、Meta / Cornerstone XR（10）与Scaling Laws in Scientific Discovery with AI and Robot Scientists（18）。14/14来源、日期、六维评分与拒绝理由均已核验；最后一项仅是概念性perspective，没有实际scaling dataset、fit或executable system contract。
- **跨周related evidence 3项:** Gemma 3 Technical Report回链W11 canonical family `google-gemma3-2025`；Wan Technical Report回链W09 `wan2-1-causal-video-vae-flow-matching-dit-open-weights`；Gemini Robotics first public为2025-03-12，应在W11建立canonical owner。三项不在W13重复评分。
- **W12 spillback:** 3月24/25 discovery重新浮现但v1属于W12的When Less is Enough、MAPS、Long Context Survey、MARS、RoboFactory、Creative Writing post-training、Bridging Continuous and Discrete Tokens、OpenVLThinker、Versatile Controls、MathFlow、ETVA、FastCuRL、AgentRxiv、Judge Anything、Vision-R1、LEMMA、V-Seek、CODA、Mind with Eyes、PhysTwin与MDocAgent，交由年度总账回拨去重，不在W13重复评分。
- **W14 spillback replay:** `2503.20783`、`2503.23145`、`2503.22879`、`2503.22165`与
  `2503.23434`均已按v1日期回拨W13，分别完成四项retained review与一项低分closure；KServe v0.15及其他
  2025-03-31事件归W14，不倒写W13。
- **Fixed-organization replay closure:** OpenAI、Anthropic、Google/DeepMind、Meta、Microsoft、NVIDIA等固定机构
  已按公开日期重放；Gemini 2.5、Anthropic circuit tracing、GPT-4o Image Generation和两项低分机构事实均已入账，
  未发现其他已知W13 owner。公告未披露机制时保持`Version Fact / Mechanism Not Disclosed`。
- **Academic daily replay closure:** 2025-03-24～30逐日arXiv/Hugging Face发现和后周spillback已按primary identifier
  与v1日期去重；月榜中DAPO、RWKV-7、Transformers without Normalization、Block Diffusion、SmolDocling等高热度项的
  v1均早于W13，已路由前周而未重复计分。当前没有只有标题、未建立identity的Discovery Gap。
- **Engineering replay closure:** PyTorch/JAX/vLLM/SGLang/Dynamo/TensorRT-LLM/Ray/KServe/Kubernetes/Transformers/
  Accelerate/DeepSpeed/Megatron-LM/MLX/llama.cpp/ONNX Runtime/OpenXLA顺序已重放；补回Megatron MTP与DeepSpeed
  v0.16.5。JAX 0.5.3和vLLM v0.8.2归W12，KServe v0.15归W14；PyTorch 2.7当周只有release-candidate稳定活动，
  不能当作stable release owner。

## Candidate Evidence Gate

- ISO window：Pass。
- Scored owner identities：62；另有3个related-evidence rows不计owner。
- Scored 20+ candidates：48（39项25～30、9项20～24）；primary-source全文或工程代码路径覆盖与strict
  schema-complete Full Source Review 48/48；
  Review Pending 0；Blocked 0；Disputed 0。
- Low-score source/date/score/rejection：14/14。
- 固定机构、每日arXiv/Hugging Face、W14 spillback与当周工程release replay：Pass；新增Megatron MTP和DeepSpeed v0.16.5
  后无已知未路由W13 identity。Scholar/OpenAlex/DBLP/Crossref的历史event-time排序/结果集不可冻结，故不宣称穷尽全网，
  Discovery Replay为`Conditional Pass — No Known Unrouted Candidate`。
- Historical Books Gate：Closed；W13 Candidate Evidence Gate：`Passed`；年度Archive Completion Gate仍Open。

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- 事件按 first-public date 归属本周；后续 revision、模型卡补充和工程集成回链本周，不重复创建新事件。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- Representation/Model：Anthropic circuit tracing、Reasoning Features → `WORLDVIEW-REPRESENTATION`；FFN Fusion → `MODEL-FFN`；Gemma 3 → `MODEL-LONG-CONTEXT`。
- Training：Gemini 2.5 report evidence与Megatron MTP → `TRAIN-PRETRAINING`；RLHF Data Scaling → `TRAIN-RLHF`；
  SimpleRL-Zoo与Trajectory Balance → `TRAIN-GRPO`；CoMP → `MULTIMODAL-REPRESENTATION`。
- Multimodal/World/VLA：Video-T1、FAR、flow-model scaling、Wan → `MULTIMODAL-GENERATIVE-PARADIGMS`；Aether → `MULTIMODAL-WORLD-MODELS`；Dita/Gemini Robotics → `MULTIMODAL-EMBODIED-VLA`。
- Inference/Platform/Agent：xKV与LogQuant → `INFER-KV-CACHE`；Video SimpleQA/Video Hallucination → `PLATFORM-EVALUATION-SYSTEM`；Open Deep Search与MCTS-RAG → `AGENT-RAG`；Think Twice → `AGENT-REFLECTION`。

## Recommended Action

- 48/48个scored 20+ owner已完成全文或工程代码路径覆盖与strict schema；14/14个低分owner已完成来源、日期、
  六维评分和拒绝闭合，普通Review Pending与Blocked均为0。
- Completed不等于Books已吸收；所有Books decision保持Frozen/provisional。
- 本周不需要用户补材料；年度流程可继续下一周。若未来取得事件时不可变的Scholar/OpenAlex导出，只用于recall审计，
  不推翻本轮primary-source证据边界。

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

Historical Books Gate关闭。62项scored owner与3项related-evidence的Weekly disposition保留为provisional evidence；
W13 Candidate Evidence Gate通过不等于年度Archive完成，也不授权Books Integration；本轮不修改Books。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。

## Repository Changes

- 在原60项账本上补回Megatron-LM MTP与DeepSpeed v0.16.5，校准为62个W13 scored owner identities：
  48项20+全部strict，14项低分全部闭合；Review Pending、Blocked与Disputed均为0，另有3项跨周related evidence。
- 完成RLHF Data Scaling event-time v1全文审计、MTP commit/docs/code/tests审计与DeepSpeed patch-family拒绝闭合；
  Candidate Evidence Gate通过，Historical Books Gate保持关闭。本轮只修改本Weekly。

## Open Questions

- Gemini 2.5 training resilience 与 Anthropic interpretability evidence 的最终 Books disposition 等 Historical Evidence Gate 后统一裁决。
- 不得把 2025-07 technical report 的机制倒写成 2025-03 announcement 已公开事实。
- RLHF Data Scaling缺公开event-time artifact与完整PPO/workload contract；MTP commit缺large-scale convergence/throughput证据，
  两者均已完成source review，但其机制收益仍是受限证据，不得升级成通用结论。
- 历史Scholar/OpenAlex/DBLP/Crossref无法提供事件时不可变的exhaustive结果集；当前没有已知未路由identity，未来新增发现
  应按Source Family和v1日期回拨，而不是把本次Conditional Pass解释成永久封闭召回。
- W12 spillback已识别但需由年度总账串行去重；Gemma 3、Wan与Gemini Robotics也不得在W13重复评分。Gemini Robotics canonical owner回拨会重新打开W11年度账本核验。

## Sources

- JavisDiT v1 — https://arxiv.org/html/2503.23377v1（First Public: 2025-03-30；Accessed: 2026-08-22）
- JavisDiT current repository — https://github.com/JavisVerse/JavisDiT（Forward Artifact: 2025-04-08；not event-time evidence）
- AdaptiVocab — https://arxiv.org/abs/2503.19693（v1: 2025-03-25；Full Source Review Complete — Experimental / Event-time Artifact Unavailable；Accessed: 2026-08-22）
- Exploring Data Scaling Trends and Effects in RLHF v1 HTML — https://arxiv.org/html/2503.22230v1（v1: 2025-03-28；Full Source Review Complete；Accessed: 2026-08-24）
- Exploring Data Scaling Trends and Effects in RLHF v1 PDF — https://arxiv.org/pdf/2503.22230v1（event-time v1；Accessed: 2026-08-24）
- Megatron-LM MTP merge commit `dc385c7` — https://github.com/NVIDIA/Megatron-LM/commit/dc385c7（Implementation Event: 2025-03-30；Full Source Review Complete；Accessed: 2026-08-24）
- Megatron-LM MTP issue #1404 — https://github.com/NVIDIA/Megatron-LM/issues/1404（merge confirmation: 2025-03-30；Accessed: 2026-08-24）
- DeepSpeed v0.16.5 — https://github.com/deepspeedai/DeepSpeed/releases/tag/v0.16.5（Released: 2025-03-27 21:47；Low-score closure；Accessed: 2026-08-24）
- LEGO-Puzzles — https://arxiv.org/abs/2503.19990（v1: 2025-03-25 18:21:07 UTC；Low-score Source/Date/Rejection Verified；Accessed: 2026-08-24）
- ViLBench — https://arxiv.org/abs/2503.20271（v1: 2025-03-26 06:38:31 UTC；Low-score Source/Date/Rejection Verified；Accessed: 2026-08-24）
- Synthetic Video Enhances Physical Fidelity in Video Synthesis — https://arxiv.org/abs/2503.20822（v1: 2025-03-26 00:45:07 UTC；Low-score Source/Date/Rejection Verified；Accessed: 2026-08-24）
- OlymMATH — https://arxiv.org/abs/2503.21380（v1: 2025-03-27 11:20:17 UTC；Low-score Source/Date/Rejection Verified；Accessed: 2026-08-24）
- Large Language Model Agent: A Survey on Methodology, Applications and Challenges — https://arxiv.org/abs/2503.21460（v1: 2025-03-27 12:50:17 UTC；Low-score Source/Date/Rejection Verified；Accessed: 2026-08-24）
- Transformers v4.50.1 — https://github.com/huggingface/transformers/releases/tag/v4.50.1（Released: 2025-03-25 14:34；Low-score patch-family closure；Accessed: 2026-08-24）
- Transformers v4.50.2 — https://github.com/huggingface/transformers/releases/tag/v4.50.2（Released: 2025-03-27 09:08；Low-score patch-family closure；Accessed: 2026-08-24）
- Transformers v4.50.3 — https://github.com/huggingface/transformers/releases/tag/v4.50.3（Released: 2025-03-28 18:21；Low-score patch-family closure；Accessed: 2026-08-24）
- Transformers v4.50.0 — https://github.com/huggingface/transformers/releases/tag/v4.50.0（Released: 2025-03-21 13:40；W12 canonical base, not rescored in W13；Accessed: 2026-08-24）
- Scaling Laws in Scientific Discovery with AI and Robot Scientists — https://arxiv.org/abs/2503.22444（v1: 2025-03-28 14:00:27 UTC；Low-score Source/Date/Rejection Verified；Accessed: 2026-08-24）

- Gemini 2.5 Pro — https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/（First Public: 2025-03-25；Accessed: 2026-07-31）
- Gemini 2.5 Technical Report — https://arxiv.org/abs/2507.06261（v1: 2025-07-08；Accessed: 2026-07-31）
- Gemini 2.5 Technical Report PDF — https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf（Accessed: 2026-07-31）
- Tracing the thoughts of a large language model — https://www.anthropic.com/research/tracing-thoughts-language-model（First Public: 2025-03-27；Accessed: 2026-07-31）
- Circuit Tracing: Revealing Computational Graphs in Language Models — https://transformer-circuits.pub/2025/attribution-graphs/methods.html（First Public: 2025-03-27；Accessed: 2026-07-31）
- On the Biology of a Large Language Model — https://transformer-circuits.pub/2025/attribution-graphs/biology.html（First Public: 2025-03-27；Accessed: 2026-07-31）
- Reasoning Features via SAE — https://arxiv.org/abs/2503.18878（v1: 2025-03-24；Full Source Review Complete；Accessed: 2026-08-22）
- SimpleRL-Zoo — https://arxiv.org/abs/2503.18892（v1: 2025-03-24；Full Source Review Complete；Accessed: 2026-08-22）
- xKV — https://arxiv.org/abs/2503.18893（v1: 2025-03-24；Full Source Review Complete；Accessed: 2026-08-22）
- FFN Fusion — https://arxiv.org/abs/2503.18908（v1: 2025-03-24；Full Source Review Complete；Accessed: 2026-08-22）
- Video SimpleQA — https://arxiv.org/abs/2503.18923（v1: 2025-03-24；Full Source Review Complete；Accessed: 2026-08-22）
- Trajectory Balance with Asynchrony — https://arxiv.org/abs/2503.18929（v1: 2025-03-24；Full Source Review Complete；Accessed: 2026-08-22）
- CoMP — https://arxiv.org/abs/2503.18931（v1: 2025-03-24；Full Source Review Complete；Accessed: 2026-08-22）
- Video-T1 — https://arxiv.org/abs/2503.18942（v1: 2025-03-24；Full Source Review Complete；Accessed: 2026-08-22）
- Aether — https://arxiv.org/abs/2503.18945（v1: 2025-03-24；Full Source Review Complete；Accessed: 2026-08-22）
- FAR — https://arxiv.org/abs/2503.19325（v1: 2025-03-25；Full Source Review Complete；Accessed: 2026-08-22）
- Inference-Time Scaling for Flow Models — https://arxiv.org/abs/2503.19385（v1: 2025-03-25；Full Source Review Complete；Accessed: 2026-08-22）
- Video Hallucination — https://arxiv.org/abs/2503.19622（v1: 2025-03-25；Full Source Review Complete；Accessed: 2026-08-22）
- Dita — https://arxiv.org/abs/2503.19757（v1: 2025-03-25；Full Source Review Complete；Accessed: 2026-08-22）
- Gemma 3 Technical Report — https://arxiv.org/abs/2503.19786（v1: 2025-03-25；Related Primary Evidence，canonical owner W11；Accessed: 2026-08-22）
- Think Twice — https://arxiv.org/abs/2503.19855（v1: 2025-03-25；Full Source Review Complete；Accessed: 2026-08-22）
- PS3 — https://arxiv.org/abs/2503.19903（v1: 2025-03-25；Full Source Review Complete；Accessed: 2026-08-22）
- LogQuant — https://arxiv.org/abs/2503.19950（v1: 2025-03-25；Full Source Review Complete；Accessed: 2026-08-22）
- Gemini Robotics report — https://arxiv.org/abs/2503.20020（v1: 2025-03-25；Related Primary Evidence，family first public 2025-03-12 / W11；Accessed: 2026-08-22）
- Open Deep Search — https://arxiv.org/abs/2503.20201（v1: 2025-03-26；Full Source Review Complete；Accessed: 2026-08-22）
- Qwen2.5-Omni Technical Report — https://arxiv.org/abs/2503.20215（v1: 2025-03-26；Full Source Review Complete；Accessed: 2026-08-22）
- Wan Technical Report — https://arxiv.org/abs/2503.20314（v1: 2025-03-26；Related Primary Evidence，canonical owner W09；Accessed: 2026-08-22）
- MCTS-RAG — https://arxiv.org/abs/2503.20757（v1: 2025-03-26；Full Source Review Complete；Accessed: 2026-08-22）
- LookAhead Tuning — https://arxiv.org/abs/2503.19041（v1: 2025-03-24；Full Source Review Complete；Accessed: 2026-08-22）
- CaMeL — https://arxiv.org/abs/2503.18813（v1: 2025-03-24；v1 PDF、appendix与artifact已恢复；Full Source Review Complete；Accessed: 2026-08-22）
- CFG-Zero* — https://arxiv.org/abs/2503.18886（v1: 2025-03-24；Full Source Review Complete；Accessed: 2026-08-22）
- Reasoning to Learn from Latent Thoughts — https://arxiv.org/abs/2503.18866（v1: 2025-03-24；Full Source Review Complete；Accessed: 2026-08-22）
- ReSearch — https://arxiv.org/abs/2503.19470（v1: 2025-03-25；Full Source Review Complete；Accessed: 2026-08-22）
- Unified Multimodal Discrete Diffusion — https://arxiv.org/abs/2503.20853（v1: 2025-03-26；Full Source Review Complete；Accessed: 2026-08-22）
- ResearchBench — https://arxiv.org/abs/2503.21248（v1: 2025-03-27；Full Source Review Complete；Accessed: 2026-08-22）
- UI-R1 — https://arxiv.org/abs/2503.21620（v1: 2025-03-27；Full Source Review Complete；Accessed: 2026-08-22）
- Embodied-Reasoner — https://arxiv.org/abs/2503.21696（v1: 2025-03-27；Full Source Review Complete；Accessed: 2026-08-22）
- ReaRAG — https://arxiv.org/abs/2503.21729（v1: 2025-03-27；Full Source Review Complete；Accessed: 2026-08-22）
- LeX-Art — https://arxiv.org/abs/2503.21749（v1: 2025-03-27；Full Source Review Complete；Accessed: 2026-08-22）
- VBench 2.0 — https://arxiv.org/abs/2503.21755（v1: 2025-03-27；Full Source Review Complete；Accessed: 2026-08-22）
- Lumina-Image 2.0 — https://arxiv.org/abs/2503.21758（v1: 2025-03-27；Full Source Review Complete；Accessed: 2026-08-22）
- Video-R1 — https://arxiv.org/abs/2503.21776（v1: 2025-03-27；Full Source Review Complete；Accessed: 2026-08-22）
- Understanding R1-Zero-Like Training — https://arxiv.org/abs/2503.20783（v1: 2025-03-26；W14 spillback；Full Source Review Complete；Accessed: 2026-08-22）
- CodeARC — https://arxiv.org/abs/2503.23145（v1: 2025-03-29；W14 spillback；Full Source Review Complete；Accessed: 2026-08-22）
- Quamba2 — https://arxiv.org/abs/2503.22879（v1: 2025-03-28；W14 spillback；Full Source Review Complete；Accessed: 2026-08-22）
- Landscape of Thoughts — https://arxiv.org/abs/2503.22165（v1: 2025-03-28；W14 spillback；Full Source Review Complete；Accessed: 2026-08-22）
- Towards Trustworthy GUI Agents — https://arxiv.org/abs/2503.23434（v1: 2025-03-30；Low-score Source/Date/Rejection Verified；Accessed: 2026-08-22）
- GPT-4o Image Generation — https://openai.com/index/introducing-4o-image-generation/（First Public: 2025-03-25；Version Fact / Mechanism Not Disclosed；Accessed: 2026-08-22）
- GPT-4o Image Generation System Card Addendum — https://openai.com/index/gpt-4o-image-generation-system-card-addendum/（First Public: 2025-03-25；Accessed: 2026-08-22）
- DAT / Dynamic Alpha Tuning — https://arxiv.org/abs/2503.23013（v1: 2025-03-29；Full Source Review Complete；Accessed: 2026-08-22）
- Aurelia — https://arxiv.org/abs/2503.23219（v1: 2025-03-29；Full Source Review Complete；Accessed: 2026-08-22）
- Evolutionary Prompt Optimization for VLMs — https://arxiv.org/abs/2503.23503（v1: 2025-03-30；Full Source Review Complete；Accessed: 2026-08-22）
- RARE — https://arxiv.org/abs/2503.23513（v1: 2025-03-30；Full Source Review Complete；Accessed: 2026-08-22）
- Shape and Texture Recognition in Large Vision-Language Models — https://arxiv.org/abs/2503.23062（v1: 2025-03-29；Low-score Source/Date/Rejection Verified；Accessed: 2026-08-22）
- A Survey on Unlearnable Data — https://arxiv.org/abs/2503.23536（v1: 2025-03-30；Low-score Source/Date/Rejection Verified；Accessed: 2026-08-22）
- Anthropic Economic Index: Insights from Claude 3.7 Sonnet — https://www.anthropic.com/news/anthropic-economic-index-insights-from-claude-sonnet-3-7（First Public: 2025-03-27；Low-score Source/Date/Rejection Verified；Accessed: 2026-08-22）
- Meta / Cornerstone XR Training with Llama — https://ai.meta.com/blog/cornerstone-transforming-training-llama/（First Public: 2025-03-26；Low-score Source/Date/Rejection Verified；Accessed: 2026-08-22）
- vLLM Q2 2025 roadmap — https://github.com/vllm-project/vllm/issues/15735（First Public: 2025-03-29；Low-score Source/Date/Rejection Verified；Accessed: 2026-08-22）
