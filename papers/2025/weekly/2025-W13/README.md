# AI Research Weekly — 2025-W13

> Coverage Window: 2025-03-24～2025-03-30
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 2 项与长期 AI System 认知相关的证据：Gemini 2.5 Pro、Tracing the thoughts of a large language model。重点不是记录发布热度，而是识别其改变了哪一项约束、机制与系统 trade-off。所有结论均按首次公开时间归档，性能或能力数字不脱离作者披露的模型、硬件、精度、输入输出、并发与 SLO 条件使用。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；访问日期统一为 2026-07-31。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：Gemini 2.5 Pro（2025-03-25）。
- 保留：Tracing the thoughts of a large language model（2025-03-27）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Gemini 2.5 Pro | 4 | 4 | 3 | 4 | 4 | 3 | 22/30 | Worth Watching；产品信号不直接修改 Books |
| Tracing the thoughts of a large language model | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；全文复核后只沉淀证据边界 |

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
- **Target and Adjacent Chapters Read:** 已读第 4 章模型学习、第 5 章神经网络学到什么、第 6 章 Transformer；核对第 62、68 章 evidence/security boundary。
- **Existing Coverage:** 第 5 章已有 correlation → decodability → intervention → mechanism 的证据阶梯、superposition与“观察只是投影”边界；但没有说明 replacement-model faithfulness、error-node dark matter、attention omission与 graph-pruning completeness，存在可明确 refine 的机制缺口。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch5，补 replacement-model faithfulness failure modes。
- **Changed Files or Rejection Reason:** 已更新 `books/part-01-worldview/05-what-neural-networks-learn.md`。
- **Open Questions:** 如何解释 attention QK circuits；如何量化 case selection bias；是否可自动化 labeling且保持可反驳性；CLT结论跨模型/版本稳定性。

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- 事件按 first-public date 归属本周；后续 revision、模型卡补充和工程集成回链本周，不重复创建新事件。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- Gemini 2.5 Pro → 第 20、22、52、62 章（Direct Evolution）
- Tracing the thoughts of a large language model → 第 5、8、62、68 章（Principle Reuse）

## Recommended Action

- Gemini 2.5 Pro：Worth Watching；产品信号不直接修改 Books
- Tracing the thoughts of a large language model：Must Read；全文复核后只沉淀证据边界

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。

## Repository Changes

- 新增 papers/2025/weekly/2025-W13/README.md。
- 本周候选已完成最终 Books disposition；实际章节修改或拒绝理由见各候选的 `Changed Files or Rejection Reason`。

## Open Questions

- Gemini 2.5 training resilience 与 Anthropic interpretability evidence 的最终 Books disposition 等 Evidence Gate 后统一裁决。
- 不得把 2025-07 technical report 的机制倒写成 2025-03 announcement 已公开事实。

## Sources

- Gemini 2.5 Pro — https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/（First Public: 2025-03-25；Accessed: 2026-07-31）
- Gemini 2.5 Technical Report — https://arxiv.org/abs/2507.06261（v1: 2025-07-08；Accessed: 2026-07-31）
- Gemini 2.5 Technical Report PDF — https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf（Accessed: 2026-07-31）
- Tracing the thoughts of a large language model — https://www.anthropic.com/research/tracing-thoughts-language-model（First Public: 2025-03-27；Accessed: 2026-07-31）
- Circuit Tracing: Revealing Computational Graphs in Language Models — https://transformer-circuits.pub/2025/attribution-graphs/methods.html（First Public: 2025-03-27；Accessed: 2026-07-31）
- On the Biology of a Large Language Model — https://transformer-circuits.pub/2025/attribution-graphs/biology.html（First Public: 2025-03-27；Accessed: 2026-07-31）
