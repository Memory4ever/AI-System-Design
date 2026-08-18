# AI Research Weekly — 2025-W28

> Coverage Window: 2025-07-07～2025-07-13
> Research Mode: Retrospective Primary-Source Backfill
> Accessed: 2026-07-31
> Re-audited: 2026-08-24
> Audit Status: Candidate Evidence Conditional — 82/86 Retained Strict, 4 Exact Material Blockers, Review Pending 0
> Historical Books Gate: Closed

## Executive Summary

旧档案只保留 Kimi K2 release；重放后恢复并去重为 91 个 scored owner lower-bound：65 项 25～30 分、21 项 20～24 分、5 项低分。86 项 retained 中，82 项已经完成 event-time strict Full Source Review，4 项被转换为有精确材料请求的 `Unverified / Blocked`，`Review Pending = 0`；5/5 低分亦完成来源、日期、评分与拒绝/争议闭合。Spatio-Temporal LLM 与 NeoBabel 的 v1 正文已经恢复并纳入 strict coverage；POLAR、Response Attack、Agent KB 与 Teach Old SAEs 缺少可替代的事件时正文或 revision。RAT、GradOT、S³ 与 DP-Fusion 的 v1 均为 2025-07-06，评分 owner 已回拨 W27，W28 只保留 spillback 说明。DRAGOn 的机制可核，但 v1 baseline/evaluator 后来被明确修复并重算，实验结论保持 `Disputed / Superseded`。UQLM 按 2025-04-27 research v1 回拨 W18。fixed-organization、Hugging Face 与 AI Infra 固定序列的 best-effort replay 已闭合，未发现新的唯一 owner；只有无法取得 immutable export 的 academic cross-index recall 继续 Open。因此本周是 Candidate Evidence Conditional，而非 Archive Completion；Historical Books Gate 继续关闭。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；后续修订回链首次公开周。
- Scholar、OpenAlex、DBLP 负责 discovery/去重；论文事实回到正文。Crossref 仅交叉检验 metadata。
- 历史回填不创建 Daily；旧档案来源保留 Accessed 2026-07-31，本轮恢复与重试来源统一记录 Accessed 2026-08-24。
- 作者/厂商 benchmark 缺少完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外模型公司、研究机构与 Hugging Face Blog。

- 当前official owners至少包括Grok 4、SmolLM3、Kimi K2 release与NVIDIA Helix；Kimi K2 technical report的v1在W31，不能倒灌为release-day公开机制。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1 正文核验。

- 当前academic lower bound覆盖attention、training/post-training、KV、RAG、evaluation/security、multimodal、Agent与workflow；identity closure不等于全文审计。

## 3. AI Infra 与工程项目

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → Dynamo → TensorRT-LLM → Ray → KServe → Kubeflow → Kubernetes → Hugging Face → DeepSpeed → Megatron-LM → llama.cpp → ONNX Runtime → OpenXLA 扫描。

- 当前engineering owners包括vLLM v0.9.2、DeepSpeed v0.17.2与Transformers v4.53.2；release fact与长期机制分开审计。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Grok 4 official | 3 | 3 | 4 | 5 | 4 | 3 | 22/30 | Full Source Review Complete — Mechanism Not Disclosed |
| SmolLM3 | 5 | 5 | 5 | 5 | 5 | 5 | 30/30 | Full Source Review Complete |
| Kimi K2 release | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Release Fact |
| vLLM v0.9.2 | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Full Source Review Complete — Official Release/Code Evidence |
| DeepSpeed v0.17.2 | 2 | 3 | 4 | 5 | 4 | 3 | 21/30 | Full Source Review Complete — Version Fact |
| Transformers v4.53.2 | 2 | 2 | 4 | 5 | 3 | 3 | 19/30 | Low-score closure — Version Fact |
| NVIDIA Helix Parallelism | 5 | 5 | 5 | 5 | 5 | 5 | 30/30 | Full Source Review Complete — Simulated Evidence |
| RedOne / SNS domain post-training | 3 | 3 | 3 | 4 | 4 | 3 | 20/30 | Full Source Review Complete — Experimental Spillback |
| PRIME dual-memory (2507.04607) | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| Knowledge-Aware Self-Correction (2507.04625) | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure |
| Cross-Distillation (2507.04636) | 4 | 3 | 4 | 5 | 4 | 3 | 23/30 | Full Source Review Complete — Experimental |
| XiYan-SQL (2507.04701) | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| LOOM-Scope (2507.04723) | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Full Source Review Complete |
| CoSteer (2507.04756) | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — Experimental |
| Reason-to-Rote (2507.04782) | 4 | 3 | 4 | 5 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental |
| ArtifactsBench (2507.04952) | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Full Source Review Complete |
| Information Utility in KV Memory (2507.05158) | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |
| OpenS2S (2507.05177) | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — Experimental |
| POLAR policy discriminators (2507.05197) | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Unverified / Blocked — P1 Event-time v1 Full Text |
| Response Attack (2507.05248) | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Unverified / Blocked — P1 Event-time v1 Full Text |
| MemoryAgentBench (2507.05257) | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete |
| TokenShapley (2507.05261) | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Low-score closure |
| LCDS (2507.05319) | 3 | 4 | 4 | 5 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental |
| Cascade private inference (2507.05228) | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Experimental |
| Spatio-Temporal LLM (2507.05258) | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental / v1 Evidence |
| Red Teaming AI Red Teaming (2507.05538) | 4 | 5 | 4 | 5 | 5 | 3 | 26/30 | Full Source Review Complete — Position Evidence |
| Prompt-injection detector limits (2507.05630) | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full Source Review Complete — Experimental Failure Evidence |
| SpaceVerse (2507.05731) | 4 | 5 | 4 | 5 | 4 | 3 | 25/30 | Full Source Review Complete — Experimental |
| Function Calling vs MCP security (2507.06323) | 4 | 5 | 4 | 5 | 5 | 3 | 26/30 | Full Source Review Complete — Architecture-label Confounding Disputed |
| Agent KB (2507.06229) | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Unverified / Blocked — P3 Event-time v1 Revision |
| Next-token predictors and inefficient reasoning (2507.05362) | 4 | 3 | 4 | 5 | 4 | 3 | 23/30 | Full Source Review Complete — Experimental Trace Evidence |
| AutoTriton (2507.05687) | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete |
| MobileGUI-RL (2507.05720) | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental / Configuration Disputed |
| SARA (2507.05633) | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental / Event-time Artifact Not Disclosed |
| ECom-Bench (2507.05639) | 4 | 5 | 5 | 5 | 5 | 2 | 26/30 | Full Source Review Complete — Experimental / Event-time Artifact Not Disclosed |
| DRAGOn (2507.05713) | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Full Source Review Complete — Mechanism Verified / v1 Evaluation Superseded and Disputed |
| HIRAG (2507.05714) | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — Experimental / Event-time Artifact Not Disclosed |
| Omni-Router (2507.05724) | 5 | 5 | 4 | 5 | 5 | 3 | 27/30 | Full Source Review Complete — Experimental / Event-time Artifact Not Disclosed |
| OpenFActScore (2507.05965) | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Experimental |
| RabakBench (2507.05980) | 4 | 5 | 5 | 5 | 4 | 3 | 26/30 | Full Source Review Complete — Experimental |
| Conditional Multi-Stage Failure Recovery (2507.06016) | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Full Source Review Complete — Experimental |
| Data Compressibility Quantifies Memorization (2507.06056) | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| NeoBabel (2507.06137) | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — Experimental / Open Artifact |
| Skywork-R1V3 (2507.06167) | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| CriticLean (2507.06181) | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Full Source Review Complete — Experimental |
| Survey on Latent Reasoning (2507.06203) | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Low-score closure — Secondary Evidence |
| Reranking FLOPs (2507.06223) | 4 | 4 | 5 | 5 | 5 | 3 | 26/30 | Full Source Review Complete — Experimental |
| PERK test-time learning (2507.06415) | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Full Source Review Complete — Experimental |
| Reward Model Correct Itself (2507.06419) | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Full Source Review Complete — Experimental |
| PAPO (2507.06448) | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| Hybrid Linear Attention analysis (2507.06457) | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Experimental |
| Verbal Confidence robustness (2507.06489) | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Full Source Review Complete — Experimental / Failure Evidence |
| SpindleKV (2507.06517) | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete |
| SlimCaching (2507.06567) | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Experimental |
| LPPO (2507.06573) | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| Decoder-Hybrid-Decoder (2507.06607) | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Experimental |
| Uncertainty layer-wise dynamics (2507.06722) | 4 | 3 | 3 | 5 | 4 | 3 | 22/30 | Full Source Review Complete — Preliminary Evidence |
| Checklist Engineering LLM Judges (2507.06774) | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Full Source Review Complete — Experimental |
| Adaptive Termination (2507.06829) | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Experimental |
| Set Selection for RAG (2507.06838) | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| Open-source AI evaluation repository (2507.06893) | 3 | 4 | 5 | 5 | 5 | 3 | 25/30 | Full Source Review Complete — Practice Evidence |
| VisualTrap (2507.06899) | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete — Security Evidence |
| Verification for code generation (2507.06920) | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Experimental |
| FlexOlmo (2507.07024) | 5 | 5 | 5 | 5 | 5 | 5 | 30/30 | Full Source Review Complete |
| Frontier LLMs simple reasoning (2507.07313) | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Failure Evidence |
| CCQ low-bit quantization (2507.07145) | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete — Experimental |
| SAND (2507.07441) | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Full Source Review Complete — Experimental |
| RLEP (2507.07451) | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| Machine Bullshit (2507.07484) | 5 | 5 | 5 | 5 | 5 | 5 | 30/30 | Full Source Review Complete |
| PLAN-TUNING (2507.07495) | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Full Source Review Complete — Experimental |
| Teaching LLM to Reason (2507.07498) | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| Selective-DPO (2507.07725) | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — Experimental |
| Krul (2507.08045) | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete |
| Compactor (2507.08143) | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete |
| TruthTorchLM (2507.08203) | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Tooling Evidence |
| Simple Mechanistic OOC Reasoning (2507.08218) | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Full Source Review Complete — Experimental |
| KAT-V1 (2507.08297) | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental / Revision-bounded |
| ChainEdit (2507.08427) | 3 | 3 | 4 | 5 | 4 | 3 | 22/30 | Full Source Review Complete — Experimental |
| clembench dialogue-game evaluation (2507.08491) | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Practice Evidence |
| LLaPa procedural planning (2507.08496) | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — Experimental |
| KELPS verified autoformalization (2507.08665) | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — Experimental |
| KV Cache Steering (2507.08799) | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Full Source Review Complete — Experimental |
| Self-Improving Model Steering (2507.08967) | 4 | 3 | 4 | 5 | 3 | 3 | 22/30 | Full Source Review Complete — Experimental |
| OpenCodeReasoning-II (2507.09075) | 4 | 3 | 4 | 5 | 4 | 2 | 22/30 | Full Source Review Complete — Dataset Evidence |
| CompassJudger-2 (2507.09104) | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| Detrimental neuron pruning (2507.09185) | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — Experimental |
| Continual pretraining Dense/MoE Tibetan (2507.09205) | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental / Artifact Not Disclosed |
| DATE-LM (2507.09424) | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — Evaluation Evidence |
| Ref-Long (2507.09506) | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Benchmark Evidence |
| GoalfyMax (2507.09497) | 3 | 3 | 3 | 2 | 3 | 2 | 16/30 | Low-score closure — Disputed identity/approval |
| Teach Old SAEs New Domain Tricks with Boosting | 4 | 3 | 3 | 5 | 4 | 4 | 23/30 | Unverified / Blocked — P3 Event-time OpenReview Revision |

账目：91 scored owners = 65 high + 21 medium + 5 low；86 项达到 20+，其中 82 项 strict complete、4 项 `Unverified / Blocked`、`Review Pending = 0`；5/5 低分完成来源/日期/评分/拒绝或争议闭合。UQLM 回拨 W18，RAT、GradOT、S³ 与 DP-Fusion 回拨 W27，均不在 W28 重复计分。Disputed 包括 GoalfyMax 低分 identity/approval、Function Calling vs MCP 与 MobileGUI-RL 的 protocol/configuration 冲突，以及 DRAGOn v1 baseline/evaluator 被后续 bug-fix 与重算取代。Identity/date/source-family/score/owner closure 不等于 claim accepted；四个 blocker 也不计 strict complete。

### Blocked / Unverified Materials Ledger

`Review Pending = 0`。以下四项不是阅读排队，而是事件时 primary material 无法在本轮取得；后发 revision 不能静默替代 owner-week 证据。

| Priority | Candidate / Source Family | Known source | Missing material and insufficiency | Acceptable substitute / suggested file | Audit after recovery |
| --- | --- | --- | --- | --- | --- |
| P1 Full Text | POLAR / `ARXIV-2507.05197-POLAR` | https://arxiv.org/abs/2507.05197 | 2025-07-07 v1 PDF 超过当前提取上限，未能覆盖 Method、实验、Appendix；abstract 不足以维持 26 分结论 | 作者版 v1 PDF/HTML/TXT；`2507.05197v1-polar.pdf` | 全文、policy-discriminator 训练/推理流、baselines、ablation、limitations 与 artifact |
| P1 Full Text | Response Attack / `ARXIV-2507.05248-RESPONSE-ATTACK` | https://arxiv.org/abs/2507.05248 | v1 PDF 在当前来源通道无法完整提取；不能仅凭摘要确认 attack surface、threat model 与 evaluation contract | 作者版 v1 PDF/HTML/TXT；`2507.05248v1-response-attack.pdf` | threat model、attack/control flow、defense baselines、success criteria、limitations 与 code |
| P3 Revision | Agent KB / `ARXIV-2507.06229-AGENT-KB` | https://arxiv.org/abs/2507.06229 | current v5 与 repository 可读，但不能证明 2025-07-08 v1 当时公开的机制、实验和 artifact 状态 | arXiv v1 PDF/source 或作者保存的 v1；`2507.06229v1-agent-kb.pdf` | v1-to-v5 diff、event-time Method/Evaluation/Appendix、artifact chronology |
| P3 Revision | Teach Old SAEs / `OPENREVIEW-D4XXFVALV7-SAE-BOOSTING` | https://openreview.net/forum?id=d4XXFVAlV7 | 2025-07-08 OpenReview 原始 submission revision 未取得；2025-07-17 arXiv v1 属 W29 forward revision | OpenReview original PDF/source/export；`2025-07-08-teach-old-saes-openreview.pdf` | event-time mechanism、experiments、revision diff、artifact and limitations |

fixed-organization、Hugging Face 与 AI Infra 固定序列已完成 best-effort replay；Google Scholar/OpenAlex/DBLP/Crossref 无 immutable export，academic cross-index recall 仍 Open。当前 91 项是 scored-owner lower bound，而不是 discovery exhaustiveness 声明。

### Low-score Closure Ledger

- **Transformers v4.53.2 / 19/30:** official GitHub patch release first-public 2025-07-11；[primary release](https://github.com/huggingface/transformers/releases/tag/v4.53.2)。它证明 patch-version shipping 与修复集合，不提供新的长期 AI System mechanism、统一 benchmark 或 workload contract，故 `Weekly Only — Version Fact`。
- **Knowledge-Aware Self-Correction / 19/30:** `ARXIV-2507.04625-KNOWLEDGE-MEMORY-GRAPH`，v1 2025-07-07；[primary paper](https://arxiv.org/abs/2507.04625)。仅以 DistilGPT-2 和简单 factual prompts 演示 RDF-triple post-processing，缺少强 baseline、规模化/冲突/更新实验与完整 artifact contract，机制不足以进入 retained gate。
- **TokenShapley / 19/30:** `ARXIV-2507.05261-TOKENSHAPLEY`，v1 2025-07-07；[primary paper](https://arxiv.org/abs/2507.05261)。token-level Shapley+KNN attribution 的作者结果限四个 benchmark，计算成本、faithfulness 与 production evidence 不足；保留 discovery，不将 attribution score 写成 truth proof。
- **Survey on Latent Reasoning / 19/30:** `ARXIV-2507.06203-LATENT-REASONING-SURVEY`，v1 2025-07-08；[primary paper](https://arxiv.org/abs/2507.06203)。属于 secondary taxonomy，可导航 activation recurrence、latent CoT 与 diffusion branch，但不能替代各 primary source 的机制与实验审计，故 `Weekly Only — Secondary Evidence`。
- **GoalfyMax / 16/30:** `ARXIV-2507.09497-GOALFYMAX`，v1 2025-07-13；[primary paper](https://arxiv.org/abs/2507.09497)。A2A/MCP/Experience Pack identity 与作者批准/事件时 artifact 链不完整，摘要中的 protocol compliance、adaptability 与 benchmark superiority 无法独立核验，故 `Disputed — Identity/Approval`；不得进入 Books。

### Deep Analysis 1 — Kimi K2 release

- First Public: 2025-07-11 (release); 2025-07-28 (report v1)
- Status: Official open-weight release; report published later
- Primary Source: https://github.com/moonshotai/Kimi-K2
- Evolution Relationship: Direct Evolution

#### Why

agentic model 不只需要增大 MoE 容量，还需要稳定的大规模训练、可验证 tool-use post-training 与 serving ecosystem 协同。

#### Principle and Mechanism

官方仓库披露 1T-total/32B-active MoE、MuonClip、tool-use post-training 与部署接口；完整技术报告的 first-public date 落在 W31，机制阅读需回链本周 release 并注明版本。

#### Trade-off and Evidence Boundary

低 activated compute 不消除总权重、expert communication 与 memory footprint；Muon 的规模化稳定性、agent benchmark 和部署成本都受作者条件限制。

#### Connection and Evolution

知识树位置：第 21、24、29、32、45、74 章。Must Read；报告全文在 Books 阶段联合复核。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

## Full Source Review

### Kimi K2 release

- **Candidate / Week / Score:** Kimi K2 release / 2025-W28 / 27/30。
- **Source Family ID:** `KIMI-K2-2507.20534`（与 W31 technical report 联读）。
- **Source Type:** official release、open weights/model card、repository；technical report 于 2025-07-28 后发。
- **First-public Date / Revision History:** model/weights release 2025-07-11；technical report arXiv v1 2025-07-28、v2 2026-02-03。7 月 11 日事件只确认 release-time contract；报告细节记录在 W31，不回写成 release 当日已公开事实。
- **Direct Primary Sources:** Moonshot/Kimi official K2 announcement、`moonshotai/Kimi-K2` repository/model card、released base/instruct weights。
- **Related Primary Sources:** arXiv:2507.20534 v1/v2；Moonlight/Muon optimizer lineage；serving engine integration docs 仅作可运行性证据。
- **Access and Verification Status:** Verified for release, weights, license/model shape and public usage contract；训练机制须由 W31 report 补证，内部 production serving policy Not Disclosed。
- **Full-read Coverage:** 已阅读 release/model card/repository 的 model shape、context、chat/tool template、deployment notes、license/use policy 与公开 evaluation table；并对照后发报告全文确认哪些机制在 release 页面未披露。
- **Original Problem:** 让 open-weight model 同时具备大容量、较低 active compute 与 agent/tool behavior，并能被外部 runtime 实际部署。
- **Why the Previous Design Was Reasonable:** dense model 与普通 chat checkpoint 的权重/serving contract 更简单；将 agent logic 留给外部 workflow 也可减少 model-side protocol coupling。
- **Changed Constraint:** 1T 级总容量、32B active compute、128K context 与 tool-intensive workload 同时出现，要求 MoE routing、模板、parser、KV 与多机 serving 形成可交付 artifact contract。
- **Mechanism:** release-time 可确认 1T total/32B active MoE、128K context、base/instruct checkpoints 与 tool-use template；MuonClip、15.5T training、agentic data/RL 与训练并行属于后发 report evidence，不是 7 月 11 日 release page 独立证明。
- **State Ownership:** model artifact 拥有 immutable config/weights/tokenizer/template；serving runtime 拥有 expert placement、KV、parser 与 admission；workflow 拥有 tool side effects；这些 owner 不因“agentic model”标签合并。
- **Control Flow / Data Flow:** prompt/tool schema → tokenizer/chat template → distributed MoE forward → model emits text/tool proposal → runtime parser → authorized workflow/tool execution；release 不公开内部训练 control flow。
- **Implementation Details:** public artifact 暴露 MLA/MoE config 与 custom-code/runtime requirements；具体 MuonClip、pipeline/expert parallel、activation offload 等在 W31 packet 核验。
- **Evaluation Setup:** release/model card 列出 coding、math、agent benchmarks；不同任务使用不同 scaffolds/sampling，hardware、production concurrency、TTFT/TPOT/SLO 不形成统一 contract。
- **Baselines / Ablations / Sensitivity:** release 有 cross-model table 但无同 data/compute 消融；optimizer/architecture ablation 只在技术报告出现。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 1T/32B active、128K context 与部分 deployment precision 支持可核；release benchmark hardware、batch/concurrency、KV capacity 与 SLO mostly Not Disclosed。
- **What the Evidence Actually Proves:** 证明该日可取得、检查并自行部署一个 1T/32B-active open-weight model 及其 interface contract；证明开放 artifact 把 model/runtime compatibility 交给部署者。
- **What It Does Not Prove:** 不证明 MuonClip 是稳定训练的唯一原因，不证明 agent benchmark 等于可靠 workflow，更不证明任意硬件上的 throughput、cost 或 SLO。
- **Limitations / Threats to Validity:** release-oriented evidence 缺少训练/消融；benchmark scaffold 异构；权重开放后 safety、parser、quantization 与 runtime patch 责任转移给 operator。
- **Trade-offs / New Failure Modes:** sparse active compute 降低每 token 理论计算，却新增 expert placement/All-to-All、large artifact distribution、parser mismatch、quantization drift 与 multi-node failure surface。
- **Where the Previous Design Still Applies:** 规模较小、低并发、互联受限或追求简单升级/回滚时，dense model 或更小 MoE 更合理；non-agent chat 不需要复杂 tool parser。
- **Evolution Relationship:** `Layering / Dependency`：open-weight MoE release contract 依赖 training 与 runtime 两条链；W31 report 补充“为何能训练”，不把 release 变成第二篇论文。
- **ROADMAP Node:** Ch21、Ch24、Ch31～32、Ch45～48、Ch74。
- **Target and Adjacent Chapters Read:** 已阅读 Ch20～24、Ch31～33、Ch44～48、Ch73～75 的章节边界；主 owner 尚待 Books Gate 在 MoE、distributed training 与 serving runtime 之间择一。
- **Existing Coverage:** Ch21 已覆盖 active/total parameters、routing 与 All-to-All；Ch45～48 已覆盖 model artifact 到 runtime contract。release 本身主要是 Version/Product Fact，是否新增机制取决于 W31 report 的 MuonClip 与 training/agent environment 证据。
- **Integration Decision:** `Weekly Only — Version/Product Fact`；机制判断归并 W31 technical report。
- **Changed Files or Rejection Reason:** 不改 Books；避免 release 与 report 重复计入。
- **Open Questions:** release-time model card 精确版本、可复现 serving matrix、quantization accuracy、production failure data 与第三方完整复现。

### SmolLM3

- **Primary / date / owner:** Hugging Face official technical blog与`HuggingFaceTB/SmolLM3-3B` model card/config/checkpoints，2025-07-08，30/30；`TRAIN-PRETRAINING`，handoff long-context、SFT/DPO与request-lifecycle owners。没有独立arXiv report，未虚构revision。
- **Problem / mechanism / ownership:** 标准3B decoder易部署，但在固定容量下同时满足long context、multilingual、math/code、tool calling与think/no-think，不能只靠参数扩张。recipe结合GQA、每四层一层NoPE、intra-document mask、三阶段11.2T data mixture、WSD、4K→32K→64K continuation与YaRN 128K extrapolation，再做reasoning mid-training、dual-mode SFT、APO；APO损害long-context后，以0.9 APO+0.1 mid-training checkpoint merge恢复RULER。training pipeline拥有mixture/config/checkpoint lineage，runtime interface拥有mode flag/chat template。
- **Implementation / evaluation:** Nanotron/DataTrove/LightEval/TRL，BF16，384×H100、24天；AdamW、LR、WD、global token batch、warmup/decay、packing和loss mask均有披露。architecture、long-context、mode ratio与merge有作者ablations；benchmark与RULER/HELMET证明该recipe的条件性结果，不证明128K任意任务准确、生产并发/SLO或每个组件独立因果充分。
- **Trade-off / coexistence / disposition:** GQA省KV却减少heads，NoPE/YaRN扩大context但增加位置归纳风险，reasoning提高难题分数却增加tokens并曾伤害long-context，merge恢复一轴也可能稀释另一轴。短上下文/单模式下标准RoPE和普通post-training仍合理。Books Frozen；future `Refine — Existing Argument`。

### vLLM v0.9.2

- **Primary / date / owner:** GitHub release/tag `v0.9.2`（commit `a5dd03c`，2025-07-07）及EPLB PR #18343、native xPyD NCCL PR #18242、P/D abort lifecycle PR #19223，29/30；`INFER-VLLM`，handoff scheduling、MoE、P/D与execution owners。
- **Problem / mechanism / ownership:** 静态EP/TP与外部P/D connector在早期规模简单可靠；V1、aux-loss-free MoE skew、prefix cache和native disaggregation使scheduler/cache/expert placement state必须显式。EPLB收集logical expert load，维护logical→physical mapping和redundant copies，定期重算placement并shuffle weights；native P/D以P2P NCCL传KV，abort path负责释放P侧blocks。router只产生load，runtime才拥有physical placement与block lifecycle。
- **Evidence boundary:** release/PR/code review证明实现路径、兼容矩阵和migration contract；没有统一end-to-end benchmark、baseline、ablation、batch/length/concurrency/SLO，不能把feature list外推为性能提升。event-time EPLB仅支持特定DeepSeek family+FP8，更多MoE/quantization和async shuffle仍是TODO。
- **Trade-off / coexistence / disposition:** load collection、weight migration、redundant VRAM、mapping mismatch与ITL spike；P/D cancel/connector failure可能留下orphan block或stale KV。稳定traffic适合static EP，小规模/冻结fleet仍可V0，成熟外部connector仍有治理优势。Books Frozen；future `Refine — Existing Argument`。

### ArtifactsBench

- **Primary / date / owner:** `2507.04952` v1 2025-07-08及project evidence，29/30；`PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-WORKFLOW`。2025-09 v2仅作later revision。
- **Problem / mechanism / ownership:** code unit test、single screenshot、DOM或pixel proxy分别只观察artifact的一面；可执行、有state transition的web artifact需要功能、视觉与交互联合证据。1,825 tasks经license/quality/dedup/human verification后，在Playwright headless Chromium、1024×768、deterministic seeds中执行；before/during/after screenshots、source、task、answer和10维checklist组成冻结evidence packet，harness拥有environment/state trajectory，candidate只拥有artifact，referee只消费证据。
- **Evaluation boundary:** 30+ models、Gemini-2.5-Pro与Qwen2.5-VL-72B dual referee；280 query×6 model的engineer study、WebDev Arena rank comparison及截图/answer ablations支持execution evidence比静态proxy更贴近该contract的人类排序。它不证明三个截图覆盖long-horizon state、MLLM judge无偏、真实用户偏好或multi-turn debugging能力；GPU、serving concurrency/SLO不是本文目标。
- **Trade-off / coexistence / disposition:** 可扩展与可复现换sandbox security、browser determinism、judge version和script维护；明确functional invariant仍应unit/DOM test，高开放UX仍需human review。Books Frozen；future `Integrate — New Mechanism`候选，正文只沉淀executable state-transition evidence，不复制排行榜。

### AutoTriton

- **Primary / date / owner:** `2507.05687` v1 2025-07-08及artifact，29/30；`INFER-TENSORRT-LLM` execution-plan/kernel owner，handoff `TRAIN-SFT`与`TRAIN-GRPO`。全文覆盖method/公式、training、evaluation、ablations、limitations与prompt appendix。
- **Problem / mechanism / ownership:** Triton降低CUDA语法门槛，但tile/layout/memory pattern仍需hardware经验；general code LLM和纯SFT只模仿，不承担execution truth。pipeline从GitHub/HF/PyTorch kernels构建tests/reference，两条路径生成Triton data并经execution验证；Seed-Coder-8B先SFT，再用VeRL GRPO，reward仅在`is_Triton`且`test_passed`时为1。compiler/executor拥有syntax、invocation和numerical verifier state，policy只提交artifact。
- **Evaluation boundary:** SFT 8×A800约16h，RL 16×A800约32h；TritonBench-G/T和KernelBench分别测compile/call/execute与hardware-bound speedup。SFT+RL多数correctness channel改善，但部分fast2反而下降；作者还展示fake Triton、未调用kernel和回落PyTorch的reward hacking。论文证明executable verifier和DSL rule优于纯模仿的条件性结果，不证明生产kernel最优、跨GPU迁移或tests完整，且训练没有performance reward。
- **Trade-off / coexistence / disposition:** GPU sandbox/compile成本高，binary reward稀疏易hack，teacher/tests会带来ceiling和contamination；关键shape和跨hardware仍应人工kernel/compiler autotuning。Books Frozen；future `Integrate — New Mechanism`候选：artifact gate必须依次验证syntax→invocation→numerics→exact hardware/shape speed。

### FlexOlmo

- **Primary / date / owner:** `2507.07024` v1 2025-07-09（v2同周；8月revision不倒灌）及official code/models，30/30；`MODEL-MOE`，handoff `TRAIN-DATA`、`PLATFORM-SECURITY`与multi-tenant lifecycle。全文覆盖mechanism/equations、FlexMix、31-task evaluation、all component ablations、routing/opt-out/extraction/scaling及appendices。
- **Problem / mechanism / ownership:** 集中预训练在数据可汇聚且长期可用时最简单高效，但多owner closed data不能共享，还要求inference-time opt-in/out。FlexOlmo以public 7B anchor、shared attention与public FFN为坐标系，每个owner只训练自己的FFN expert和一行router embedding；合并时拼接weights/router rows，无需原始数据，opt-out移除对应expert/row。public anchor、expert artifact、router version和owner policy分别拥有状态；移除expert不是unlearning或数据删除。
- **Evaluation boundary:** 512×H100、1T public tokens、7 owners各50B continued-pretraining，最终37B total/20B active；31 tasks及prompt routing/model soup/BTM/BTX/unrestricted-MoE baselines，含coordination、embedding init、bias、active-expert与opt-out ablations。作者contract支持模块化合并和可观察opt-out，但“closed data”由公开数据模拟，未验证真实机构trust、malicious owner、heterogeneous architecture或production serving SLO；scaling还伴随约2.5× dense inference FLOPs。
- **Trade-off / coexistence / disposition:** data sovereignty与并行本地训练换anchor compatibility、router calibration、expert starvation/overactivation、sparse communication和weight leakage；proxy tuning可能泄漏或错配。集中同域、低延迟场景仍适合dense/standard MoE，严格隐私仍需DP/secure aggregation。Books Frozen；future `Refine — Existing Argument`。

### Machine Bullshit

- **Primary / date / owner:** `2507.07484` v1-only 2025-07-10及project/code/data，30/30；`PLATFORM-EVALUATION-SYSTEM`，handoff `TRAIN-RLHF`、observability与governance。全文覆盖Bullshit Index、taxonomy、三组datasets、RLHF/CoT/principal-agent experiments、human studies、prompts、limitations与broader impact。
- **Problem / mechanism / ownership:** factuality只问“说的是否真”，无法区分模型相信错误与输出根本不随其belief proxy变化，也漏掉paltering、空洞修辞与含糊措辞。Bullshit Index以MCQA首token probability作belief proxy、显式claim作action，计算`1-|r_pb(p,y)|`；行为侧用四类taxonomy判定。ground truth/context属于environment，belief只是不可直接观察proxy，claim是model action，human utility是downstream outcome。
- **Evaluation boundary:** BullshitEval 2,400 scenarios、Marketplace 1,200、Political Neutrality多组prompts；before/after RLHF、Base/CoT/PA、多模型/三domain sensitivity，含bootstrap、robust regression与1200+300 participant human validation。论文支持这些场景中preference optimization可能使claim更少依赖belief proxy并增加误导修辞，但不证明首token probability等于真实belief、RLHF是唯一因果、judge无偏或该指标跨生产域通用；human-human agreement本身很低。
- **Trade-off / coexistence / disposition:** 新diagnostic需要ground truth、token probability和binary claim extraction，易受class imbalance、calibration、prompt与ceiling影响；factuality、calibration/uncertainty、belief→claim与downstream harm必须并存。Books Frozen；future `Integrate — New Mechanism`，只能写成受限evidence dimension。

### SpindleKV

- **Primary / date / owner:** `2507.06517` v1 2025-07-09与ACL 2025 paper，29/30；`INFER-KV-CACHE`，handoff continuous batching、execution与memory management。全文覆盖equations、GQA mapping、reserve schedule、codebook reconstruction、LongBench/NIAH、all ablations、limitations与appendices。
- **Mechanism / evidence:** 深层按attention importance eviction，浅层将pre-RoPE K/V归一后按cosine相似度构建codebook，每token只保留index+magnitude，reconstruct后再施加RoPE；GQA可逻辑unfold以避免共享KV head的decision conflict。三类模型、多budget和component ablations支持作者benchmark的quality-memory frontier，但单RTX3090实验显示约17–18% throughput下降，不能写成无开销或production speedup。
- **Trade-off / disposition:** 增加codebook identity、threshold drift、incremental merge、budget overshoot、approximate logits和irregular kernel；显存充足/严格exactness仍应FullKV，纯eviction/quantization各有条件。Books Frozen；future `Refine — Existing Argument`。

### Krul

- **Primary / date / owner:** `2507.08045` v1 2025-07-10，29/30；`INFER-KV-CACHE`，handoff memory tiers、scheduling与multi-tenant lifecycle。全文覆盖conversation-specific layer pairing、restore optimizer/scheduler、implementation与4×A100 evaluation。
- **Mechanism / evidence:** inactive conversation在full recompute与full load之间，按当前conversation attention把layers分类并动态选择cross-layer sharing map；turn结束压缩/offload，恢复时校准compute-vs-load并以CUDA streams/I/O threads形成pyramid overlap。4×A100/PCIe Gen4、LongBench和ShareGPT合同支持TTFT/storage改善，但不证明真实arrival distribution、queueing/fairness、failure recovery、multi-node或tail SLO。
- **Trade-off / disposition:** selector误判、map staleness、compressed-state version、restore cancellation和hardware calibration drift；短history/HBM足够仍可retain，CPU bandwidth好可load，compute便宜可recompute。Books Frozen；future `Integrate — New Mechanism`。

### Compactor

- **Primary / date / owner:** `2507.08143` v1 2025-07-10及official repo identity，29/30；`INFER-KV-CACHE`，handoff execution、continuous batching与evaluation。全文覆盖leverage theory/proof、noncausal attention、calibration、H100 evaluation、all ablations与repo execution paths；event-time artifact commit未冻结。
- **Mechanism / evidence:** query未知时用right Gaussian sketch近似key leverage，再与chunk-level noncausal attention score融合选token；以原/压缩context下ground-truth answer NLL ratio拟合per-context retention curve。RULER/LongBench支持作者contract的query-agnostic adaptive budget，但实际k=64不满足理论bound，noncausal attention只是heuristic，“ANOVA不显著”也不是equivalence proof，end-to-end TTFT/throughput/SLO未披露。
- **Trade-off / disposition:** reusable prefix换sketch/SVD/block attention、random seed/calibration version、noncontiguous KV、under-compression OOM与silent quality loss；query已知可用query-aware eviction，strict exactness继续FullKV。Books Frozen；future `Integrate — New Mechanism`。

### NVIDIA Helix

- **Primary / date / owner:** `2507.07120` v1-only 2025-07-07及NVIDIA Research page，30/30；`INFER-SCHEDULING`，handoffKV/decode/MoE/execution。全文覆盖phase-specific sharding、exact-softmax reconstruction、roofline、simulator sweep、ablation与limitations；无event-time production code。
- **Mechanism / evidence:** 同一GPU集合在attention阶段按sequence/query-head分片，在FFN/MoE阶段重映射为更大tensor/expert parallel group；All-to-All partial output与log-sum-exp重构exact softmax，KV append按chunk分配owner。GB200 NVL72、FP4、Llama-405B/DeepSeek-R1 simulator支持latency-throughput Pareto移动；不证明生产E2E、真实1M-context quality、多节点或failure recovery。
- **Trade-off / disposition:** QKV replication、collective epoch、动态mapping、KV placement/invalidation增加状态复杂度；短context、`TP≤KV heads`或FFN非瓶颈时经典TP/KVP仍合理。Books Frozen；`Emerging / Experimental — Simulated Evidence`。

### VisualTrap

- **Primary / date / owner:** `2507.06899` v1 2025-07-09，29/30；`PLATFORM-SECURITY`，handoffmultimodal representation与tool/action。全文覆盖poison objective、Qwen2-VL setup、grounding/end-to-end/modular evaluation、sensitivity/defense与limitations。
- **Mechanism / evidence:** 少量pretraining samples加入patch trigger并替换coordinate target，使控制权从planner意图转移到poisoned visual grounding。Qwen2-VL 2B/7B与ScreenSpot/AITW/Mind2Web/OmniACT支持该供应链vulnerability；不证明真实数据可被污染、任意LVLM/trigger/defense或完整系统compromise。
- **Trade-off / disposition:** poison ratio/trigger size在stealth与ASR间权衡；模块化仍合理，但需provenance、independent coordinate verifier、canary/OOD tests、高风险confirmation与human override。Books Frozen；future `Refine — Existing Argument / Experimental Security Evidence`。

### CCQ / Convolutional Codebook Quantization

- **Primary / date / owner:** `2507.07145` v1-only 2025-07-09，29/30；execution-plan owner，handoffGPU memory与MoE。全文覆盖convolution code/scale equations、Triton/vLLM port、large-MoE quality、H20 operator tests与limitations。
- **Mechanism / evidence:** overlapping state bits把多个weights编码为packed index，runtime以shift/mask即时重建；artifact identity必须绑定CCQ tuple、grouping、scale format与kernel。DeepSeek-V3/ERNIE-4.5、2.06～2.75bpw与H20 specified shapes支持memory/quality/operator frontier；不证明dense model、E2E TTFT/throughput、其他硬件或普遍minimal loss。
- **Trade-off / disposition:** offline search、scale metadata、dequant与kernel specialization新增index/scale corruption和config mismatch。W8/W4、standard W2与VQ/trellis按稳健性/质量/部署控制共存。Books Frozen；`Emerging / Experimental`。

### MemoryAgentBench

- **Primary / date / owner:** `2507.05257` v1 2025-07-07及event-day code/data，28/30；`PLATFORM-EVALUATION-SYSTEM`，handoffAgent memory。全文覆盖incremental ingest、four competencies、tasks/baselines、chunk/top-k sensitivity、latency与limitations。
- **Mechanism / evidence:** sequential chunks先触发memory update，全部ingest后才query，区分retrieval、test-time learning、long-range understanding与conflict resolution；raw context、RAG index与derived memory拥有不同state。多类baseline显示各分支互有强弱且multi-hop conflict resolution很低；不证明真实持续对话、普遍ranking或因果algorithm superiority。
- **Trade-off / disposition:** 小chunk提高lookup却增构建成本并损全局结构，大top-k增context/cost；overwrite、FIFO遗忘、distributed-evidence miss要求provenance、supersession、rollback。Books Frozen；future `Refine — Existing Argument`。

### Grok 4 official

- **Identity / date / coverage:** xAI official announcement first-public 2025-07-09，22/30；`WORLDVIEW-LLM-INTELLIGENCE`，handoff long-context/evaluation/tool calling。全文核对RL scaling、native tool use、Grok 4 Heavy parallel test-time compute、official benchmarks与API/context/product contract；event-time technical/model/system card、architecture、training recipe、artifact和可复现harness均未公开。
- **Mechanism / ownership:** 官方只披露model可调用code interpreter、Web/X search，Heavy并行探索多个hypotheses；orchestrator拥有tool permission、timeout、budget、trace和result injection，外部tool拥有fresh evidence，model只拥有query/proposal。`256k context`是capacity fact，不等于reliable reasoning保证；200,000-GPU、6×efficiency等均是vendor claim而非公开机制。
- **Evaluation boundary / trade-off:** HLE、ARC-AGI-2、USAMO、Vending-Bench数字缺统一hardware/precision/batch/concurrency/SLO和完整ablation，只证明2025-07-09 version/product事实。tool use增加prompt injection、stale/poisoned evidence、permission与latency/cost；parallel TTC增加branch compute、aggregation和错误相关性。无工具/串行路径在低成本、静态知识和受限权限场景仍合理。
- **Disposition:** `Weekly Only — Version/Product Fact / Mechanism Not Disclosed`；Historical Books Gate关闭。

### DeepSpeed v0.17.2

- **Identity / date / coverage:** official release 2025-07-07、signed tag `15f054d`及autocast+ZeRO PR #6993，21/30；`TRAIN-DEEPSPEED`，handoff ZeRO/distributed training。已核release notes、32 commits/56 files、config/code path与tests；patch release无论文Method/Appendix且没有performance benchmark。
- **Mechanism / ownership:** legacy统一FP16/BF16训练简单但难保softmax等sensitive ops的FP32语义。`torch_autocast.enabled/dtype/lower_precision_safe_modules`让safe modules降精度、sensitive ops保FP32，ZeRO reduce-scatter/all-reduce和Stage-3 all-gather按configured dtype通信；config/autocast dispatcher、ZeRO partition state、GradScaler和compiled graph分别拥有控制权，且不能与旧`fp16`/`bf16` config同时开启。
- **Evidence boundary / trade-off:** release/code只证明autocast+ZeRO、DeepCompile stage1/2与若干dtype/device/compat fixes已交付；不证明更快、更省显存、收敛等价或全部model/operator安全。per-module policy增加safe-list、collective dtype、overflow/underflow、compiled-graph与version-matrix failure；不触发这些路径时v0.17.1仍可成立。
- **Disposition:** `Weekly Only — Version/Engineering Fact`；Books Gate关闭。

### RedOne / SNS domain post-training

- **Identity / date / coverage:** `2507.10605` v1 2025-07-13、v2 2025-10-12只作forward revision，20/30；从W29回拨W28。Owner `TRAIN-PRETRAINING`，handoff data/SFT/RLHF/DPO/evaluation。全文覆盖CPT/SFT/DPO pipeline、data filtering/RegMix、offline suites、stage ablations、online A/B、OOD、Limitations/Ethics/Appendix；event-time code、dataset/model artifact和commit未公开。
- **Problem / mechanism / ownership:** 单任务SFT易归因和独立回滚，但SNS多任务共享非正式、情绪化、interaction-heavy signals。pipeline为`Qwen2.5 base → general+SNS CPT → broad mixed SFT → SNS-heavy SFT → task-aware preference pairs → DPO(+0.3 SFT loss)`；data owner保存source/group/filter/mixture/privacy/delete lineage，preference owner保存expert/judge/pair provenance，training owner保存stage/checkpoint lineage，weights不拥有consent或policy。
- **Evaluation boundary / trade-off:** 7B/32B、General-Bench、8-task SNS-Bench、bilingual SNS-Trans、task-SFT、five-arm stage ablation、held-out/OOD和两个internal online scenarios支持作者私有合同下的domain gain及CPT→SFT→PO layering；不证明20B mixture、stage order、RegMix/judge各自因果、无general regression、online uplift可复现或数据治理完成。多任务共享提高复用却扩大negative transfer、forgetting、judge drift、delete difficulty与whole-model rollback radius。
- **Coexistence / disposition:** 任务少、风险隔离、局部rollback或知识需citation/delete时，single-task adapter或external retrieval仍更合理。现有Ch27～34已覆盖该组合机制，故`No Change — Already Covered / Experimental Case`；Books Gate关闭。

### PRIME dual-memory

- **Identity / date / coverage:** `2507.04607` v1 2025-07-07；later revisions只作forward evidence，26/30；owner `AGENT-MEMORY`。全文覆盖episodic/semantic memory、personalized-thinking distillation、CMV与LaMP evaluation、memory ablations和limitations；事件时repository commit未锁定。
- **Mechanism / ownership:** episodic memory检索原始用户历史，semantic memory以per-user LoRA/profile保存抽取后的稳定偏好，再通过synthetic thought distillation生成个性化推理轨迹。history store拥有原始provenance，derived-memory owner拥有抽取、版本、supersession与delete lineage，adapter registry拥有per-user artifact；weights不能替代原始授权和删除状态。
- **Evaluation boundary / trade-off:** 133个CMV query、41 users、7,514条history及LaMP1–5，只支持作者任务中dual memory相对单一路径的条件性收益，且不同数据集并非单调。它不证明真实长期用户偏好稳定、synthetic CoT忠实或per-user adapter可安全大规模运维。成本包括adapter explosion、retrieval latency、stale belief、privacy/delete与semantic/episodic冲突。
- **Disposition:** `Emerging / Experimental`；保留raw retrieval、profile和derived adapter三条可回滚分支，Books Gate关闭。

### Cross-Distillation / EI-BERT

- **Identity / date / coverage:** `2507.04636` v1 2025-07-07，23/30；owner `TRAIN-SFT`，handoff execution/evaluation/security。全文覆盖vocabulary pruning、teacher-head reuse、mutual distillation、INT8 PTQ、CLUE/internal Alipay evaluation和limitations；无官方artifact。
- **Mechanism / ownership:** attention-based vocabulary pruning缩小token state；teacher task head复用与teacher/student之间的MSE+KL mutual updates把任务知识压入tiny ALBERT-2；最后module-wise INT8 PTQ形成edge artifact。teacher、student、vocabulary map、task head与quantization calibration必须分别版本化，不能把distillation写成单一checkpoint事实。
- **Evaluation boundary / trade-off:** 8×V100训练、Chinese NLU与internal Alipay合同支持该tiny-model/edge路径的条件性可行性；不证明LLM reasoning、跨语言迁移、隐私安全或生产device/SLO。压缩节省部署成本，却引入teacher bias、vocabulary OOD、mutual-update instability、PTQ drift与私有benchmark不可复核。
- **Disposition:** `Emerging / Experimental`；成熟单向distillation或独立quantization仍是更可控分支，Books Gate关闭。

### XiYan-SQL

- **Identity / date / coverage:** `2507.04701` v1 2025-07-07，27/30；owner `AGENT-WORKFLOW`。全文覆盖schema filtering、multi-generator、execution feedback、clustering/selection、BIRD/Spider evaluation、ablations与limitations；事件时artifact可见但未形成生产commit contract。
- **Mechanism / ownership:** iterative column selection先缩小schema，再由多任务、多格式generator产生SQL候选；sandbox执行返回结果或错误，按execution result聚类后由learned selector选择最终artifact。schema/version、candidate SQL、execution trace、result cluster、selector score与最终commit分别由workflow state拥有，而不是由模型文本统一拥有。
- **Evaluation boundary / trade-off:** 32B generator、7B selector、BIRD/Spider和约10 candidates/query、约40.5秒的作者合同，支持execution-aware selection改善其benchmark；execution equality不等于语义正确或安全，且硬件、并发和生产SLO未闭合。multi-model voting提高覆盖，却增加成本、position bias、correlated error和sandbox风险。
- **Disposition:** `Emerging / Experimental`；read-only sandbox、query policy和human approval仍是高风险数据库的必要控制，Books Gate关闭。

### LOOM-Scope

- **Identity / date / coverage:** `2507.04723` v1 2025-07-07，27/30；owner `PLATFORM-EVALUATION-SYSTEM`。全文覆盖Benchmark/Deployment/Evaluator解耦、configuration contract、22 benchmarks/140 tasks、cost/acceleration comparisons、ablation与limitations；repository未锁定event-time commit。
- **Mechanism / ownership:** benchmark module拥有dataset/task/prompt，deployment module拥有model/runtime/precision/batch，evaluator module拥有metric/judge/version；冻结config把三者组合成可重放run identity。它把“模型分数”重构为workload、runtime和evaluator共同生成的evidence packet。
- **Evaluation boundary / trade-off:** 8K～2M item、H20/RTX3090等作者实验支持模块化harness的覆盖和成本分析，但部分加速比较混合batch、hardware和sample count，不能写成公平系统benchmark，也不证明替代官方harness。通用性换来adapter/version matrix、config drift和metric provenance维护。
- **Disposition:** `Refine — Existing Argument / Evaluation Contract Evidence`；只沉淀typed evaluation contract，不复制排行榜，Books Gate关闭。

### CoSteer

- **Identity / date / coverage:** `2507.04756` v1 2025-07-07，24/30；owner `INFER-DECODE`，handoff security/evaluation。全文覆盖local/cloud cooperative decoding、logit-delta objective、LightCoSteer、benchmarks、throughput和limitations；无官方artifact。
- **Mechanism / ownership:** edge SLM分别在有/无private context下前向，logit delta作为私有上下文对token偏好的影响；cloud接收query/logits并提出候选，edge按目标与delta选择/校正token，LightCoSteer以`T=1`降低交互。private context与final token authority留在edge，cloud只拥有proposal state。
- **Evaluation boundary / trade-off:** 作者报告约23.88→13.73→9.44 tok/s的不同路径，但hardware/network/concurrency/SLO未披露，只能证明该实验中的privacy-utility-latency trade-off。data locality不等于formal privacy；RTT进入每token critical path，tokenizer/logit alignment、weak delta和malicious cloud都可能失败。
- **Disposition:** `Emerging / Experimental`；local-only、RAG redaction、TEE和formal privacy分别适用于不同threat model，Books Gate关闭。

### Reason to Rote

- **Identity / coverage:** `2507.04782` v1 2025-07-07，later v2只作forward revision，24/30；official artifact可核。Owner `WORLDVIEW-REPRESENTATION`，handoff `WORLDVIEW-WHY-MODELS-LEARN`与`TRAIN-DATA`。v1全文覆盖FDA/THR training dynamics、logit lens/probes、EAP circuit、INLP、head/neuron ablation和Appendix A–I。
- **Mechanism / evidence boundary:** 小型from-scratch models在5% label noise下先学corrected/generalized answer，随后才用distributed late transformation覆盖为noisy label；中间层仍可读出clean answer，前后circuits大量重叠。两个受控任务支持memorization可复用generalizable computation，而非独立lookup；不证明frontier/long-CoT、真实数据或任意knowledge edit都同样成立，probe可读也不自动等于因果。
- **Trade-off / disposition:** distributed memory对局部ablation更稳健却更难删除和审计；localized facts或high-noise regimes仍可能更接近lookup。`Refine — Existing Argument / Experimental`，Books Gate关闭。

### InfoSteer / Information Utility in Key-Value Memory

- **Identity / coverage:** `2507.05158` v1 2025-07-07，later v2只作forward revision，25/30；owner `TRAIN-SFT`。v1全文覆盖FFN-coefficient intervention、entropy regularization、多模型SFT/OOD evaluation、layer/strength ablations、Appendix A–D与artifact。
- **Mechanism / evidence boundary:** 在SwiGLU down projection前对bottom `p%` coefficients做`alpha × layer mean` intervention，或以`L=L_LM-lambda ΣH(k_hat_l)`鼓励更广activation；coefficient是transient state，不是serving KV cache或外部memory。作者短上下文arithmetic/OOD合同支持modest improvement且层位/强度敏感，不证明entropy等于knowledge utilization、FFN是literal database或可泛化到RL/long-CoT。
- **Trade-off / disposition:** training hook和activation tracking增加复杂度，过强/过多层会退化；vanilla SFT仍适合稳定低风险路径。`Emerging / Experimental`，Books Gate关闭。

### OpenS2S

- **Identity / coverage:** `2507.05177` v1 2025-07-07、same-week v2；later v3只作forward revision，24/30。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff representation/inference runtime。v1全文覆盖Qwen2-Audio→Qwen3-8B→interleaved speech decoder→causal flow-matching vocoder、three-stage training和benchmark；repo/model/dataset artifact可核。
- **Mechanism / evidence boundary:** audio encoder以25Hz输出features；每`M=4`个LLM hidden states交织生成`N=8` speech tokens，再以chunk-aware causal flow matching和HiFi-GAN生成waveform。作者材料证明公开端到端streaming architecture与受限speech-to-text结果；S2S主要是qualitative demos，未证明numeric latency、empathy/safety、interleaving因果收益或production concurrency/SLO。
- **Trade-off / disposition:** interleaving潜在降latency，却耦合hidden/token rate并增加buffer、rollback和synthetic voice bias；需要独立gate和component replacement时cascade仍合理。`Emerging / Experimental`，Books Gate关闭。

### LCDS

- **Identity / coverage:** `2507.05319` sole v1 2025-07-07，24/30；ACL Demo paper与official repository。Owner `AGENT-WORKFLOW`，handoff RAG/evaluation。全文覆盖EMR normalization、field-source mapping、rule workflow、sentence attribution、expert review、150-EMR evaluation、limitations/ethics和appendices。
- **Mechanism / evidence boundary:** heterogeneous EMR先归一为JSON；短字段keyword、长字段ICL segmentation+BM25建立field→source mapping，各field选择extraction/summarization/judgment/inference逻辑。ChatGLM3-6B+LoRA只生成Silver proposal，GPT-4o给sentence-source pointer，physician edit后才promote为Golden dataset。source pointer不等于entailment，model不拥有clinical approval authority。
- **Trade-off / disposition:** 显式source scope与human promotion提高可审计性，却增加mapping/rule drift、review labor、false attribution和department lock-in；单机构结果不证明clinical safety/cross-site deployment。`Refine — Existing Argument / Experimental Domain Case`，Books Gate关闭。

### Cascade / Token-Sharded Private Inference

- **Identity / coverage:** `2507.05228` sole v1 2025-07-07，28/30；owner `PLATFORM-SECURITY`，handoff request/scheduling/KV。全文覆盖semi-honest threat model、vocab-matching attack、token/attention sharding protocols、security analysis、CPU/Ray experiments和Appendix A–G；无official code。
- **Mechanism / evidence boundary:** prompt positions被分给CompNode和AttnNode shards；每层各node计算partial Q/K/V和attention statistics，再以stable log-sum-exp合并。clustered-arithmetic sharding拉大同node可见token gap，使generalized attack cost随`V^g`上升；若token本身绝不能暴露，前L层仍需SMPC。作者128-token、colocated CPU、non-colluding合同支持相对SMPC baselines降低通信/运行成本，不提供cryptographic privacy、malicious/collusion/WAN或GPU decode保障。
- **Trade-off / disposition:** 用统计隐藏换速度和更多routing/KV ownership；更多shards增加bytes、barrier、node-loss和collusion surface。高敏感仍需SMPC/TEE/local inference。`Emerging / Experimental`，Books Gate关闭；related May attack `2505.18332`回拨W21 discovery gap，不在W28重复计分。

### Red Teaming AI Red Teaming

- **Identity / coverage:** `2507.05538` v1 2025-07-07；later v2只作revision，26/30；position/framework paper，无experiment、benchmark或artifact。Owner `PLATFORM-SECURITY`，handoff evaluation/production。全文覆盖red-team definition、macro lifecycle、micro model testing、meta coordination、six recommendations和limitations。
- **Mechanism / evidence boundary:** 提议把model jailbreak testing置于更大的system red-team lifecycle：inception、design、data、development、deployment、maintenance、retirement；macro findings下传micro tests，micro vulnerabilities上卷threat model、TEVV、disclosure、mitigation和monitoring。它证明作者提出了可审计taxonomy，不证明该流程降低事故率、优于既有RMF或具有可量化coverage/cost/SLO。
- **Trade-off / disposition:** 扩大scope可发现cross-component blind spot，却增加coordination、owner ambiguity、scenario explosion与governance theater；automated prompt suites仍适合高频regression。现有Ch72/66/73已覆盖相同owner chain，故`No Change — Already Covered / Position Evidence`，Books Gate关闭。

### How Not to Detect Prompt Injections with an LLM

- **Identity / coverage:** `2507.05630` v1 2025-07-08；later revisions只作forward evidence，27/30。Owner `PLATFORM-SECURITY`，handoff evaluation/context/RAG/tool。v1全文覆盖KAD axioms、black-box threat、Type-I/II failure、DataFlip、7-task/4-backend experiments、discussion和limitations；DataFlip无event-time artifact。
- **Mechanism / evidence boundary:** KAD把detector instruction、random key和attacker data放在同一LLM context；adaptive injection让detector抽取并返回当前key，使key presence失去instruction provenance。为降低旧Type-I error而强化对injected instruction的服从，会提高adaptive Type-II failure。作者合同证明shared prompt/key state不是稳健security predicate，不证明所有classifier、typed defenses或sandbox失效。
- **Trade-off / disposition:** canary detector可作低成本sensor，不能拥有authorization；隐藏key或更多adversarial tuning不修复control/data co-location。Ch72已明确model verdict不是authority，故`No Change — Already Covered / Experimental Failure Evidence`，Books Gate关闭。

### SpaceVerse

- **Identity / coverage:** `2507.05731` sole v1 2025-07-08，25/30；later ACM venue只作forward revision，v1内嵌DOI与正式metadata冲突，不用于family identity。Owner `INFER-SCHEDULING`，handoff multimodal/PD/evaluation。v1全文覆盖progressive confidence、region compression、Jetson/ground prototype、link trace、baselines、ablations和limitations；无official artifact。
- **Mechanism / evidence boundary:** onboard 2B先从visual feature估difficulty，必要时在partial tokens后再次估计；低confidence才offload到ground 7B。image再按prompt-region CLIP relevance做drop/downsample/retain。作者遥感、emulated Starlink、Jetson/RTX3090合同支持early routing+payload transformation改善受限offload frontier；confidence拟合2B/7B output similarity而非correctness，未证明calibrated uncertainty或真实on-orbit/SLO。
- **Trade-off / disposition:** progressive decision省部分local compute，却新增threshold drift、false local commit和partial-token state；region compression不可逆并引入small-object/global-context loss。satellite-only、GS-only和full-local-then-offload仍各有条件。`Refine — Existing Argument / Experimental Edge–Ground Case`，Books Gate关闭。

### Omni-Router: Sharing Routing Decisions in Sparse Mixture-of-Experts for Speech Recognition

- **Identity / coverage:** Source Family `ARXIV-2507.05724-OMNI-ROUTER`，v1 first-public 2025-07-08 07:18:33 UTC，27/30；v2/v3、Apple research page及later official repository/checkpoints只作forward evidence。v1 Abstract、Related Work、公式、shared-router Method、data/model/training/evaluation、Tables I～IV、expert-use/permutation/Cramér’s-V与training-instability分析均已读；v1无独立Limitations/Appendix。event-time code/checkpoint未披露。Owner `MODEL-MOE`（Ch21），handoff `MODEL-FFN`、`TRAIN-DISTRIBUTED-TRAINING`与`INFER-TENSORRT-LLM`。
- **Problem / previous / changed constraint:** 标准Switch MoE为每层独立学习router，允许各层按自己的hidden representation形成不同decision boundary，在低数据、层间语义不同或需要局部容错时合理；但约1M小时异质语音、16-layer Pre-LN encoder暴露跨深度specialization path松散和expert-count扩大时训练不稳。Pre-LN residual使相邻层表示变化较缓，作者据此把router coordinate升级为跨层共享状态。
- **Mechanism / ownership / flow:** 标准`P^l(X^l)=Softmax(X^l W^l)`改为所有MoE层共用`W_shared`，但每层仍以自己的`X^l`重新计算top-1 expert，各层expert FFN仍独立；继续使用逐层Switch load-balance loss。checkpoint拥有`W_shared`、各层experts、Pre-LN/residual、top-1 rule、load coefficient、CTC head/tokenizer；runtime只执行assignment与placement，不能改变routing语义。`audio → log-mel/frame stack → 16-layer encoder → per-layer X^l × W_shared → top-1 dispatch → layer-local expert → CTC → greedy decode`；共享router不消除逐层evaluation、capacity/drop或All-to-All。
- **Implementation / evaluation contract:** SpeechCrawl约1M小时English，WhisperX/Whisper-large-v2 segmentation/pseudo-label，<30s segments；12h/24 files dev selection。16 encoder blocks、8k word-piece CTC，dense 84M/140M/200M与2/4/8-expert Switch/Omni variants，最多1M steps/7 epochs、16×H100，dynamic batch最多7小时音频，grad clip0.1，AdamW、64k warmup至0.001。主评测覆盖SpeechCrawl及AMI、Callhome、Chime6、CommonVoice、Fleurs、LibriSpeech、Switchboard、TEDLIUM、VoxPopuli、WSJ等OOD WER，并在Libriheavy复核；比较dense、per-layer Switch、shared Omni，含expert-count/model-size、random expert permutation、Cramér’s-V与loss spike分析。precision、H100型号/topology、capacity/overflow、seed/CI、inference latency/throughput/concurrency/SLO均未披露。
- **Proof / non-proof / threats:** 作者合同支持在该非流式English ASR、top-1、16-layer Pre-LN setting下，共享routing coordinate可训练，并在多组WER表中较作者dense/Switch baselines同向改善，且相邻层assignment correlation与permutation sensitivity更高；这证明routing-state granularity是条件计算设计变量。不证明所有层选择同一expert、expert具有可命名/因果语义、Cramér’s-V等于更好specialization、适用于LLM/多语/streaming，也不证明active FLOPs、latency、memory、network、energy或fault robustness改善。内部SpeechCrawl、pseudo-label/license/dedup、12h dev、无seed/CI及部分Switch单独调LR/load-loss构成protocol confound。
- **Trade-off / coexistence / disposition:** 共享`W`减少router参数并提供共同坐标，却把所有层router gradients耦合到一个状态，某层/域可干扰其他层；Pre-LN相似假设失效时会系统性misroute，较高permutation sensitivity也可能表示fragility。expert placement、All-to-All、小expert batch、capacity overflow与checkpoint兼容仍未解决。低数据、Post-LN/heterogeneous blocks、layer-local semantics或共享梯度干扰高时per-layer router仍合理；若瓶颈是dispatch/communication，Omni-Router没有触及根因。Ch21已有router/top-k/load balance与model/runtime owner边界，但缺`per-layer router state → cross-layer shared coordinate`及成立条件，future `Refine — Existing Argument / Experimental`；当前Books Frozen。
- **Open Questions:** grouped sharing粒度、Pre-LN表示相似度与收益的关系、多seed统一protocol、capacity/drop与distributed dispatch成本、streaming/multilingual/LLM迁移以及shared-router corruption/fault amplification仍待验证。

### Teach Old SAEs New Domain Tricks with Boosting

- **Identity / event boundary:** OpenReview forum `d4XXFVAlV7` first-public为2025-07-08，canonical owner归W28；arXiv `2507.12990` sole v1 2025-07-17只作forward revision。arXiv v1与current OpenReview PDF全文、Appendix已读，但未取得7月8日原始submission PDF/revision blob，故本项为`Unverified / Blocked — P3 Event-time Revision`而非strict complete。
- **Problem / mechanism / ownership:** general SAE在训练分布上学习固定sparse dictionary，稀有domain概念可能留在reconstruction residual。方案冻结base SAE，新增domain residual SAE：encoder读取完整activation `x`，loss拟合`e=x-x_hat`，推断时以`x_hat+e_hat`重构；多domain module直接求和。base dictionary/feature IDs、domain module、threshold/top-k、LLM/layer/hook point、corpus provenance与composition manifest必须分别拥有版本身份。
- **Evaluation contract:** Qwen2.5-7B-Base与Llama3.1-8B-Base layer-24 residual、FineWeb-Edu general域、Russian/chemistry/UN domain、每域1B tokens、base `k=50`与residual `k=5`；EV、替换activation后的next-token CE与L0比较base、boost、Extended SAE、stitching和full fine-tune，并做多module、token curve、top-k sensitivity与feature inspection。hardware、precision、optimizer、batch、sequence length、seeds/CI、latency/concurrency/SLO均未披露。
- **Evidence boundary / dispute:** 作者两个base-SAE family与三个domain的实验支持“冻结base并拟合domain residual可改善其EV/CE proxy，并较full fine-tune少损general EV”；不证明feature canonical、monosemantic、faithful或被原模型因果使用，也不证明任意layer/domain与无限module组合。正文对50M/100M/200M训练收敛阈值不一致；chemistry dataset引用无法唯一识别，均保持Disputed，不能外推通用门槛。
- **Trade-off / disposition:** 以额外dictionary、每token额外encode/decode、L0上升与module registry换取冻结base；新增domain overlap/double correction、threshold drift、stale base/module mismatch和module-count线性成本。单一稳定分布、严格feature identity或latency敏感时，原SAE/重训仍合理。Ch5已覆盖解释replacement model与faithfulness evidence ladder，故future disposition为`No Change — Already Covered / Experimental Interpretability Case`；Historical Books Gate关闭。

### Function Calling vs MCP Security

- **Identity / coverage:** `2507.06323` sole v1 first-public 2025-07-08，26/30；作者artifact为`theconsciouslab-ai/llm-agent-security`，但event-time commit未锁定且当前顶层缺README所述requirements文件。全文覆盖7个surface、6个attack vector、simple/composed/chained formalization、Function Calling/MCP实现、3,250 scenarios、ASR/rejection、judge validation、recommendations、limitations与banking-agent Appendix；MCP 2025-06-18 architecture/authorization/tools规范作为协议边界primary evidence。
- **Problem / mechanism / ownership:** 单点prompt/schema test易归因，但Agent的system/user prompt、tool catalog、function arguments、execution output与final response跨越LLM和传统software boundary，前一阶段污染会成为后一阶段输入。论文把评估单位扩展为沿`Input → Configuration → Execution → Output → Response`传播的stateful attack chain。Host拥有conversation、catalog exposure、principal/policy和call decision；tool registry/server拥有schema与implementation；executor拥有authorization、side effect和authoritative outcome；model只拥有proposal；evaluator拥有scenario lineage和success rule。MCP separation提供可放置控制的边界，不自动授予isolation、least privilege或business authorization。
- **Evaluation boundary / dispute:** 作者称两种实现使用相同models/tools/payload/timing/resources，40% simple、30% composed、30% chained，每scenario三次；DeepSeek-R1 judge与300-case人工抽查报告`kappa=0.84`。但完整7-model API snapshot、MCP/SDK revision、Host permissions、transport、credential scope、sandbox、tool semantics与cloud guard均未披露；“default configuration”不是稳定deployment identity，300/3250也非精确10%。因此只支持“architecture adapter改变attack surface、isolated test不能替代cumulative chain test”，不支持Function Calling或MCP具有固定ASR；73.5%与62.59%及5-step 91～96%只属于作者custom contract，标记`Disputed — Implementation/Protocol Identity Confounded`。
- **Trade-off / disposition:** centralized Function Calling减少connection/auth/state协调，却可能共享credential/context并放大blast radius；MCP提供显式client/server/capability boundary，却增加server trust、session/version、supply-chain与cross-server aggregation风险。两者都需要schema+semantic validation、least privilege、token audience、approval、sandbox、output filtering与correlated audit。Ch72、Ch78、Ch83和Ch66已覆盖model-as-proposal、tool trust、MCP非授权与cumulative evaluation，故`No Change — Already Covered`；量化协议排名不得进入Books，Historical Books Gate关闭。

### Next-token Predictors Toward Systematically Inefficient Reasoning

- **Identity / coverage:** `2507.05362` v1 2025-07-07，23/30；v2只作forward revision。v1全文覆盖layered shortest-path generator、tokenization、trace algorithms、28.5M decoder training、main results、RR/DR controls、temperature/model-size/data-scale ablations、limitations与Appendix；官方repo在event-time前已有commits，但本轮未完整重取当时全部blob。Owner `TRAIN-DATA`，handoff pretraining/decoder-only/planning。
- **Problem / mechanism / ownership:** 全局最省步骤的bottom-up DP是自然teacher，但autoregressive learner最小化逐token条件损失，不直接最小化整条算法的operation count。作者用`eta`控制layered DAG探索：正值接近layer-by-layer DP，零值随机混合，负值depth-first并在更优partial path出现时backtrack；三者都生成正确增量trace，却有不同局部连续性。graph generator拥有拓扑/split，trace generator拥有`eta`、queue与best-path state，serialized row拥有data identity；独立parser和DP solver拥有correctness/optimality verdict，model token confidence没有验证 authority。
- **Evaluation boundary:** 默认`L=7,K=6,C=5,p_e=0.6`，32M/128M fixed-token budget与约200K equal-example comparison，5 seeds；另用random repetition和double repetition分离length/structure。该custom-language、小模型合同支持“中间trace优于direct answer，且系统性depth-first trace在相同token budget下优于全局更短DP trace”；DR只拉长反而退化，反证token越多越好。不证明自然语言/frontier model、RL、开放规划或显式CoT faithful，也不证明average sampled-token probability是generalization的因果解释或校准置信度。
- **Trade-off / disposition:** locally predictable trace增加training/decode token、KV、latency和逐步error surface，固定token budget下还减少unique examples；随机teacher policy会使conditional target多峰并诱发重复loop。已知算法、严格latency或可直接调用solver时，最短确定性trace仍合理。`Refine — Existing Argument / Experimental Trace-Structure Evidence`；Historical Books Gate关闭。

### MobileGUI-RL

- **Identity / coverage:** `2507.05720` sole v1 2025-07-08，27/30；未发布official code/model/task artifact。全文覆盖online Android environment、self-exploration/task synthesis、text-world-model filter、MobGRPO/reward、three-benchmark evaluation、ablations、tool schema/prompts与Appendix。Owner `TRAIN-GRPO`，handoff data/workflow/planning/platform。
- **Problem / mechanism / ownership:** offline GUI trajectories可复算且安全，但容易绑定旧UI；long-horizon online GUI又使terminal reward稀疏、group all-equal和异长credit退化。pipeline由Android random-walk trace生成任务，text world model用structured UI模拟可解性并按step count排curriculum；MobGRPO把terminal group advantage复制到trajectory全部action tokens，成功轨迹按长度衰减，早失败处罚，all-fail group过滤。environment拥有真实screen/transition，policy只提议action，curriculum持task acceptance/order，rollout保存policy+initial state+trajectory，terminal oracle持作者实验中的success verdict但不等于环境truth。
- **Evaluation boundary / dispute:** Qwen2.5-VL 7B/32B、1,251 generated/436 retained tasks、AndroidWorld和两套curated AITW，主结果与三项ablation支持该emulator合同下完整pipeline相对base同向增益。正文写7B每task 8 rollouts、32B 4，max 25 steps；Appendix却写统一8 rollouts和max 15，Introduction称4 benchmarks而实验仅3，且无seeds/CI、GPU数量、reward系数、oracle calibration与SLO，故绝对recipe/数字标`Disputed`。它不证明online RL普遍优于offline、binary oracle是ground truth或terminal credit具有因果性。
- **Trade-off / disposition:** online relevance换emulator nondeterminism、UI drift、straggler、policy staleness、oracle cost和副作用；simulation filter会产生curriculum bias，length reward可能鼓励shortcut或拖延，all-fail过滤会遗忘最难slice。Ch33/27/81已覆盖long-horizon group credit、policy-relative curriculum和durable environment state，故`No Change — Already Covered / Experimental GUI-RL Case`；Historical Books Gate关闭。

### SARA: Selective and Adaptive RAG with Context Compression

- **Identity / coverage:** Source Family `ARXIV-2507.05633-SARA`，sole arXiv v1 2025-07-08，27/30；later OpenReview/ACL 2026/code/HF artifact只作forward evidence，event-time artifact `Not Disclosed`。v1全文覆盖equations1～5、Algorithm1、九dataset evaluation、baselines、model/retriever generalization、ablations、sensitivity与Appendix A～D。Owner `AGENT-RAG`（Ch76），handoff `AGENT-CONTEXT`、`AGENT-MEMORY`与`MODEL-LONG-CONTEXT`。
- **Problem / mechanism / state:** raw top-k text保留精确entity、number与citation，短证据和audit workload下最可靠，却在hard Context budget中浪费redundant passages；pure dense/one-vector compression节省tokens，却会丢局部事实。SARA把每个256-token chunk经sentence embedder+MLP压成一个decoder-space vector，以alignment reconstruction和joint context reconstruction训练，再用LoRA让decoder读mixed representation。per-query selector从top-1开始，以embedding-set discrepancy或proxy-LM conditional self-information迭代加入relevant/non-redundant chunks；selected `k`保留raw text，其余retrieved chunks压成vectors。corpus/source拥有authoritative text，retriever/index拥有top-n pool，compressor+adapter是decoder-version-bound state，selector/packer拥有raw-vs-vector allocation，decoder不拥有evidence truth。
- **Implementation / evaluation contract:** PyTorch/Transformers/LlamaIndex，bf16，LoRA rank16/alpha32/dropout0.1，n=10、默认k=5，temperature0，6×A100；Mistral/Llama/Gemma多个base、BM25/bge/SFR retrievers。六training+evaluation与三个OOD datasets使用F1/ROUGE-L及GPT-4o/RAGAS-style claim metrics，八类baseline含vanilla RAG、LLMLingua、ICAE/xRAG、Raptor/GraphRAG/InstructRAG。不同baseline backbone与GPT-4o data/judge造成confound；batch、optimizer、steps、A100规格、latency/memory/concurrency/SLO未披露。作者结果和ablation支持该contract下hybrid Context优于tested branches，reconstruction是最大贡献，raw k约7～8后plateau；不证明universal improvement、calibrated truth、hallucination elimination、vector portability或production benefit。
- **Trade-off / limitations / coexistence:** learned compression减少prompt pressure，却增加projection/adapter训练、decoder coupling、opaque latent evidence、citation/provenance断裂与upgrade invalidation；CSI增加proxy compute并可能奖励surprising-but-irrelevant/adversarial text，embedding novelty不等于factual utility。raw top-k仍适合短/local/legal/exact-citation，extractive compression更可审计，pure vector适合低风险极限budget。缺显式Limitations section、human judge calibration、seeds/CI、same-task tuning/eval隔离和event-time artifact；OOD correctness增幅小于relevance，不能把retrieval improvement等同answer correctness。
- **Evolution / disposition:** `static raw top-k → extractive/latent compression alternatives → hybrid fidelity/coverage allocation + set-conditioned novelty selection → future provenance-aware decoder-versioned packing`。Ch76已有retrieval/rerank/dedup与joint Context policy，却未明确raw evidence与learned vectors的共存机制、decoder-version coupling和fidelity–coverage frontier，故future`Refine — Existing Argument`；当前Books Frozen，Historical Books Gate关闭。

### ECom-Bench

- **Identity / coverage:** Source Family `ARXIV-2507.05639-ECOM-BENCH`，v1 2025-07-08、v2/EMNLP 2025只作forward revision，26/30；official repo最早2025-09-29，故event-time artifact `Not Disclosed`。v1全文覆盖benchmark construction、`pass^k`公式、setup/results、8-run consistency、error/dimensional evaluation、persona 2×2×2 ablation、limitations与trajectory Appendix。Owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff tool/workflow/agent platform；v1只标注MCP-compliant tools，未披露spec revision/conformance，不能归给MCP mechanism owner。
- **Problem / mechanism / state:** single-turn/text benchmark能隔离单项能力，却无法测多轮persona、retrieval、multimodal evidence和有副作用DB操作的闭环可靠性。ECom-Bench用persona user simulator、JSON business DB、21类tools、53 human-reviewed tasks（18 multimodal）和domain docs构造环境；每轮ReAct Agent提议response/tool call，最多20 turns/600s。scorer同时比较final DB expected state、required retrieval-tool trace与required output keywords。对每task运行n次、成功c次，`pass^k=E[C(c,k)/C(n,k)]`衡量随机抽取k次全部成功，不是至少一次成功的Pass@k。environment拥有fixture/DB/tool trace与reward，simulator拥有next user utterance，planner只拥有proposal，tool runtime拥有side effect，scorer拥有verdict。
- **Evaluation / evidence boundary:** LangGraph+ReAct、temperature0.3、Qwen-Max simulator、Moonshot vision tool；53 tasks×8 runs，比较多个proprietary planners。作者结果显示平均success会掩盖repeat reliability下降，且final-state+trace+output contract比纯LLM judge更接近executable outcome。它不证明某API的一般客服能力、vision-as-tool因果优于end-to-end MLLM、persona对真实用户的因果效应、checker完备、工具符合可复算MCP规范或production SLO。model snapshot、hardware、precision、length、batch/concurrency、cost与run reset/seed isolation未披露；architecture comparison与simulator/model family强混杂。
- **Trade-off / coexistence / disposition:** executable state和persona提高交互真实性，却把validity绑定到simulator realism、fixture coverage、tool semantics、reset isolation和scorer correctness；rule checker降低judge variance但会漏等价合法路径或被keyword proxy误判。单轮QA、无副作用检索与固定脚本业务仍适合更小benchmark。Ch66/78/81/84已经拥有subject/environment/scorer identity、side-effect failure taxonomy、durable fixture、run isolation和Pass@k/`pass^k`边界，故`No Change — Already Covered / Weekly-only Domain Evidence`；Historical Books Gate关闭。

### DRAGOn: Dynamic RAG Benchmark On News

- **Identity / revision / coverage:** Source Family `ARXIV-2507.05713-DRAGON-DYNAMIC-RAG`，v1 `DRAGON` first-public 2025-07-08，25/30；v2 2025-07-15与v3/EACL 2026只作forward revisions。v1 metadata、Method、all experiments、Limitations/Ethics及Appendix A～J已读，并核event-time repo chronology。Repo在2026-01明确修复baseline metric与evaluator bugs，v3改变metrics、model set与result tables；因此v1机制可审计，但榜单/数字已被corrected revision取代。Canonical owner `PLATFORM-EVALUATION-SYSTEM`（Ch66，legacy Ch62），handoff `AGENT-RAG`（Ch76）。
- **Problem / previous / changed constraint:** 固定Wikipedia/QA snapshot可冻结population、ground truth和回归条件，在长期可比性上合理；当目标是recent facts时，污染、新闻修订和online corpus drift使静态题集逐渐失真。约束从固定model×corpus转为model/retriever/generator面对周期更新语料的联合系统，同时要求freshness与longitudinal comparability。
- **Mechanism / state / flow:** Daily news crawl对前一revision做diff，抽取entity relation triplets，以Wikidata候选+embedding+LLM归一化；去除完全匹配Wikidata的triplets，按simple/set/multi-hop/conditional graph templates生成QA，再经fluency、NER、no-context triviality、graph correspondence与eight-criterion judge过滤。Public texts/questions、private mapping/answers和static sandbox分别version；participant只提交found IDs与answer，portal以private data评分，leaderboard绑定dataset revision。可靠run必须pin dataset/scorer/code/model revision，`latest`不是evidence identity。
- **Evaluation contract / dispute:** v1使用500-character chunks、100 overlap、top-5 retrieval，比较4 retrievers与6 generators，报告Hit Rate/Recall/NDCG、ROUGE-L、Substring Match与judge score；只披露TP/context/max-new-tokens，hardware、precision、batch、concurrency、latency/cost/SLO均Not Disclosed。532 examples的judge-human calibration显示高precision但部分criteria recall仅0.52～0.62。2026 bug fixes与v3重算意味着v1 absolute metrics/ranking为`Disputed / Superseded`，不得当稳定evidence。
- **Proof / non-proof / trade-off:** 证据证明rolling public/private dataset、automatic KG-driven QA、submission portal与revision-bound leaderboard可组成dynamic RAG benchmark；不证明无contamination、跨revision score可直接聚合、private scorer可独立审计、synthetic QA代表真实queries或俄语新闻排名可外推。Freshness减少陈旧，却牺牲同分布可比；private labels保护完整性却降低透明度；automatic generation放大source/template/judge bias。应并行保留fixed anchor set与rolling fresh set。
- **Disposition / questions:** Ch66/76已覆盖versioned population、scorer revision、corpus freshness与joint RAG evaluation，因此`Disputed — Mechanism Verified / v1 Evaluation Superseded`；即便未来用corrected revision解除争议，也优先`No Change — Already Covered`。Historical Books Gate关闭。仍需v1具体bug diff、all historical dataset/scorer digests、fixed-anchor+rolling report与private-scorer independent verification。

### HIRAG: Hierarchical-Thought Instruction-Tuning Retrieval-Augmented Generation

- **Identity / revision / coverage:** Source Family `ARXIV-2507.05714-HIRAG`，v1 first-public 2025-07-08，24/30；v2/v3与EMNLP 2025 Findings只作forward revision。v1 21页全文、三层能力、Algorithm 1、六benchmark、ratio ablation、limitations、Appendix A/B均已读并对照later versions。没有official code/model/data artifact，corrected RGB与exact teacher/verification outputs均Not Disclosed。Canonical owner `AGENT-RAG`（Ch76，legacy Ch72），handoff `TRAIN-SFT`（Ch29）。
- **Problem / previous / changed constraint:** Generic reader+top-k在gold passage直接含答案、base model足够强时便宜且易回滚；当Context含同主题噪声、跨文档属性或需结合外部evidence与参数知识时，retrieval success不等于generator正确使用evidence。
- **Mechanism / ownership / flow:** Supervision递进为`Filtering → Filtering+Combination → Filtering+Combination+RAG-specific reasoning`，以`<|REASON|>`和`<|ANSWER|>`分隔trace；teacher-generated query/thought/answer/gold documents经second teacher revision、task filter、same-theme distractors和20% shuffle形成约120K synthetic samples，再以progressive mixture SFT。Corpus拥有facts，data builder拥有teacher/prompt/gold/distractor lineage，trainer拥有mixture/special-token/checkpoint，retriever拥有candidate set，generator只拥有proposal；visible CoT不是faithful reasoning或claim truth。
- **Implementation / evaluation contract:** Llama2-7B、Llama3-8B和Qwen2.5-7B，8×A100，LR `3e-5`、batch4、warmup0.5%、max train length4096；vLLM+Contriever-MS评RGB-noise/int、PopQA、HotpotQA、MuSiQue、PubMedQA，含英文/中文ratio ablation。Teacher identity在GPT-4-turbo、Qwen-MAX与Algorithm里的GPT-4o之间未形成统一immutable contract；optimizer、precision、A100型号、global batch、seeds、artifact、latency/SLO未披露。部分baselines取公开结果而非同harness rerun。
- **Proof / non-proof / limitations:** 作者contract支持RAG-specific SFT与filter/combine/reason data在selected benchmarks上改善点估计，也显示mixture ratio在noise与integration间有取舍；不证明visible CoT faithful、claims grounded、internal-knowledge补全可靠、curriculum而非more synthetic data/teacher quality导致增益，或production/multilingual通用。Ratio在RGB上选择、training corpus与evaluation family overlap、teacher/judge bias、corrected RGB未公开、无seeds/CI和citation audit构成主要威胁。
- **Trade-off / coexistence / disposition:** 增加teacher data、reason tokens与training compute，并引入ratio overfit、citation-token形式主义、reason trace injection、decode/KV cost及external/internal provenance ambiguity。Clean/short/direct-answer corpus仍适合generic reader；retrieval/rerank与extractive verifier不可被generator tuning取代。Ch76已有`retrieval relevance ≠ context sufficiency ≠ generation faithfulness`，但可在未来补filter/combine/reason task decomposition与mixture state，故future `Refine — Existing Argument / Experimental`；当前Books Frozen。

### Spatio-Temporal LLM

- **Primary / date / coverage / owner:** `ARXIV-2507.05258-SPATIOTEMPORAL-LLM`，v1 2025-07-07、26 页 event-time PDF 已读；后续 v2 的架构与结果只作 revision lineage。25/30；owner `MULTIMODAL-EMBODIED-VLA`，handoff `MULTIMODAL-REPRESENTATION`、world-model 与 evaluation。
- **Problem / mechanism / state flow:** 纯 2-D egocentric video 能识别画面，却缺少可度量的 3-D relative pose、distance 与 affordance state。REA 从 EPIC-KITCHENS/VISOR/EPIC-FIELDS 组合 point cloud、video 与 text，以 3-D positional encoding 和 cross-modal alignment 接入 LLM，依次评 relative direction/distance、find-my-item、furniture affordance 与 action planning；dataset 拥有 coordinate/frame identity，encoder 拥有 aligned tokens，model 只提出答案/plan。
- **Evaluation / boundary / trade-off:** v1 的多项 baseline overall 为 23.68～30.96%，ST-LLM 为 34.55%、categorical 44.02%，仅是作者在该数据构造和 harness 下的结果；不证明真实机器人闭环、sim-to-real、causal world model 或安全控制。3-D 重建增强 spatial grounding，却引入 calibration、timestamp drift、sensor alignment 与 data provenance failure modes。`Emerging / Experimental`；Books Frozen。

### OpenFActScore

- **Primary / date / coverage / owner:** `ARXIV-2507.05965-OPENFACTSCORE`，v1 2025-07-08，9 页全文、方法、实验与限制已读；28/30。owner `PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-RAG`。
- **Problem / mechanism / state flow:** 原 FActScore 依赖闭源模型，难复现 atomic-fact generation/verification。OpenFActScore 以 Hugging Face 模型完成 AFG，再从可信 KB 取 top-5 BM25/GTR passages 做 AFV；claim、retrieval snapshot、verifier version 与 aggregate score 分开拥有，BERTScore-F1 只比较 AFG，相对 human AFV error 评 verifier。
- **Evaluation / boundary / trade-off:** 作者报告与原实现 Pearson 0.99，且 Gemma/OLMo 在 AFG、Gemma/Llama3.1 在 AFV 更强；范围限 biography/Wikipedia，equal atomic weighting 只测 precision、不测 completeness，且 evaluator 敏感。开源提高可审计性但未消除 verifier bias、claim dependence 与 corpus staleness。`No Change — Already Covered / Experimental evidence`；Books Frozen。

### RabakBench

- **Primary / date / coverage / owner:** `ARXIV-2507.05980-RABAKBENCH`，v1 2025-07-08，36 页全文、taxonomy、construction、human validation、guardrail evaluation 与 appendix 已读；26/30。owner `PLATFORM-SECURITY`，handoff evaluation/governance。
- **Problem / mechanism / state flow:** 英文单文化 safety set 无法验证 Singlish、华语、马来语、泰米尔语的 code-switching 与本地风险表达。Generate→Label→Translate pipeline 构造 5k+ prompts、六类风险，13 个 guardrails 统一跑同一 policy taxonomy；source prompt、translation lineage、human label、guardrail output 与 operating threshold 分开拥有。
- **Evaluation / boundary / trade-off:** inter-annotator agreement 约 0.70～0.80、kappa 0.68～0.72，支持标签流程可用，不证明 taxonomy 完整或跨地区通用；LLM generation/translation 会传播偏差，Singapore-only population 限制外推。多语覆盖增加现实性，也增加 label drift、dialect shift 与 threshold calibration 成本。`Refine — Existing Argument / Experimental`；Books Frozen。

### Conditional Multi-Stage Failure Recovery

- **Primary / date / coverage / owner:** `ARXIV-2507.06016-CONDITIONAL-RECOVERY`，v1 2025-07-08，28 页全文、四阶段 recovery、TEACH/AI2-THOR setup、ablations、failure cases 与 limitations 已读；25/30。owner `AGENT-WORKFLOW`，handoff `AGENT-REFLECTION` 与 embodied owner。
- **Problem / mechanism / state flow:** 只在 episode 结束后反思能解释失败，却无法在长 physical trajectory 中及时止损。系统把 detection/diagnosis/replan 分散到三个 runtime checkpoints，再加 post-execution reflection；environment 拥有 authoritative scene/transition，agent 拥有 proposal 与 provisional diagnosis，workflow 拥有 checkpoint/rollback lineage。
- **Evaluation / boundary / trade-off:** 作者报告相对 no-recovery +11.5、相对 strongest prior +19，但 evidence 受 TEACH simulator physics、object localization 与 positioning bottleneck 约束。多 checkpoint 提高恢复机会，也增加 token/tool latency、false intervention 与 partial side-effect rollback 难题；简单短任务仍适合 end-only check。`Refine — Existing Argument / Experimental`；Books Frozen。

### Data Compressibility Quantifies Memorization

- **Primary / date / coverage / owner:** `ARXIV-2507.06056-COMPRESSIBILITY-MEMORIZATION`，v1 2025-07-08，33 页全文、entropy/compression formalization、experiments 与 privacy discussion 已读；26/30。owner `TRAIN-DATA`，handoff evaluation/security。
- **Problem / mechanism / state flow:** instance-level membership score常把偶然易样本当 memorization。论文将数据集视为集合，以 entropy/compressibility 与 edit-distance memorization 建立 EM Linearity，用 set-level statistic 推断训练数据属性；dataset snapshot、compressor/model、probe protocol 与 inference verdict必须版本化。
- **Evaluation / boundary / trade-off:** 证据支持所测模型/数据上的 set-level relation，不支持单样本成员判断、因果归因或通用 privacy guarantee；只使用一种 prompting/memorization metric。集合聚合降低噪声却牺牲个体定位，并可能泄漏 dataset-level property。`Emerging / Experimental`；Books Frozen。

### NeoBabel

- **Primary / date / coverage / owner:** `ARXIV-2507.06137-NEOBABEL`，v1 2025-07-08，event-time HTML 524 行已覆盖 architecture/objective、data curation、progressive pretraining/instruction tuning、evaluation、ablations、limitations 与公开 code/model/data links；24/30。owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff representation/data/evaluation。
- **Problem / mechanism / state flow:** translation-first text-to-image 能复用英文模型，但增加 semantic drift、latency 和 culture loss。NeoBabel 扩展 Gemma-2 embedding table加入 8,192 image tokens，MAGVIT-v2 把 256×256 image 编成 16×16 tokens；text 用 causal attention、image 用 bidirectional denoising attention，以 random mask objective 只优化 visual tokens。text/image tokenizer、modality boundary、mask schedule、checkpoint/data mixture各自拥有 identity。
- **Implementation / evaluation contract:** 六种语言、124M multilingual pairs、progressive 256→512 training、20 checkpoints 的 SMA/EMA/WMA merge；m-GenEval/m-DPG、EVA-CLIP/DINOv2 CLC 与 code-switch CSS。作者报告 2B model 的 multilingual m-GenEval 0.75、m-DPG 0.68，但 metric/model/data均同源，hardware、precision、batch/concurrency、energy 与 production SLO未形成完整 contract。
- **Proof / non-proof / trade-off:** 证据支持 native multilingual visual-token training 在该 corpus/harness 下优于 translation baselines，并显示 mixture/quality/resolution/merge 分支的 sensitivity；不证明六语之外、cultural fidelity、VQA 或 universal Pareto frontier。统一模型减少 translation service，却扩大 tokenizer/data governance、language imbalance、metric embedding bias 与 delete/retrain radius。`Emerging / Experimental / Open Artifact`；Books Frozen。

### Skywork-R1V3

- **Primary / date / coverage / owner:** `ARXIV-2507.06167-SKYWORK-R1V3`，v1 2025-07-08，21 页全文、architecture/post-training、critical-token entropy、evaluation 与 limitations 已读；26/30。owner `MULTIMODAL-REPRESENTATION`，handoff `TRAIN-GRPO`。
- **Problem / mechanism / state flow:** text reasoning RL 不自动解决 visual grounding；论文把 connector 视为关键接口，在不继续预训练的条件下用 post-training RL 迁移 reasoning，并以 critical-token entropy 观察 checkpoint 变化。vision encoder/connector 拥有 perceptual token mapping，policy 拥有 reasoning proposal，reward/evaluator 才拥有 provisional acceptance。
- **Evaluation / boundary / trade-off:** 作者报告 MMMU 76.0，但未证明 connector 是唯一因果因素、跨模型/任务通用或视觉 hallucination 已解决；hardware、production latency/SLO 未形成完整 contract。少预训练可降成本，却更依赖 base representation 和 reward coverage。`Emerging / Experimental`；Books Frozen。

### CriticLean

- **Primary / date / coverage / owner:** `ARXIV-2507.06181-CRITICLEAN`，v1 2025-07-08，40 页全文、CriticLeanGPT、CriticLeanBench、SFT/RL、compiler/evaluation 与 appendices 已读；25/30。owner `PLATFORM-EVALUATION-SYSTEM`，handoff reflection/workflow。
- **Problem / mechanism / state flow:** Lean compiler success只证明语法与定理可证，不证明自然语言命题被忠实 formalize。critic 对语义 fidelity 给过程反馈，SFT 后再用 RL 优化；NL statement、formal artifact、compiler proof、critic judgment 与 human semantic label是不同 owner。
- **Evaluation / boundary / trade-off:** 证据说明 compiler-only verifier 会漏 semantic mismatch，作者 critic 在其 benchmark 上改善 fidelity；不证明 judge 无偏、覆盖所有数学歧义或能替代 expert review。新增 critic 提高语义审计但增加 verifier coupling、reward hacking 和 compute。`Refine — Existing Argument / Experimental`；Books Frozen。

### Reranking FLOPs

- **Primary / date / coverage / owner:** `ARXIV-2507.06223-RERANKING-FLOPS`，v1 2025-07-08，10 页全文、closed-form estimator 与 evaluation 已读；26/30。owner `PLATFORM-COST`，handoff `AGENT-RAG`。
- **Problem / mechanism / state flow:** latency 强依赖硬件与实现，难比较 reranker 计算效率。RPP（ranking metric/PetaFLOP）与 QPP（queries/PetaFLOP）用 model/input contract 估算 FLOPs；query/candidate length、model config、estimated FLOPs、quality metric 与 observed latency应分别记录。
- **Evaluation / boundary / trade-off:** estimated FLOPs 与 latency 的相关性在 Qwen-7B 为 .88、Flan-T5-XXL 为 .94；未覆盖 kernel efficiency、bandwidth、energy、batching 与动态负载，故“hardware agnostic”仅指 normalized proxy。可比性提升但会掩盖 memory-bound 系统。`Refine — Existing Argument / Experimental`；Books Frozen。

### PERK Test-Time Learning

- **Primary / date / coverage / owner:** `ARXIV-2507.06415-PERK`，v1 2025-07-08，20 页 event-time PDF、inner/outer loops、truncated unrolling、benchmarks 与 limitations 已读；25/30。owner `MODEL-LONG-CONTEXT`，handoff `TRAIN-LORA` 与 `AGENT-MEMORY`。
- **Problem / mechanism / state flow:** retrieval 让 context 留在 prompt，长 context 成本随长度增长；PERK 在 test time 用 CLM inner loop 把 context 写入临时 LoRA，再由 meta outer loop 学会问答。base checkpoint、context-specific adapter、update steps 与 request identity必须绑定，adapter是 derived memory 而非事实源。
- **Evaluation / boundary / trade-off:** BabiLong/HotpotQA/TriviaQA/DIO 等、多个 model family 显示训练 8K 可外推更长，但结果不证明 production concurrency、privacy deletion 或 universal recall；permutation 会丢 order。它以额外梯度、adapter store/eviction 与 stale-memory risk 换 prompt/KV 长度。`Emerging / Experimental`；Books Frozen。

### Reward Model Correct Itself

- **Primary / date / coverage / owner:** `ARXIV-2507.06419-REFORM-RM`，v1 2025-07-09，44 页全文、controlled decoding、failure mining、REFORM、BoN/PPO/DPO evaluation 与 limitations 已读；25/30。owner `TRAIN-RLHF`，handoff DPO/GRPO/evaluation。
- **Problem / mechanism / state flow:** reward model 在固定 held-out preference set 上看似准确，却会给 distribution-shifted response 错分。controlled decoding 搜索高 reward/低真实质量样本，REFORM 将失败感知数据回灌重训；response、RM score、external preference label、failure set 与 retrained checkpoint分别拥有 lineage。
- **Evaluation / boundary / trade-off:** 证据证明方法能在作者模型/分布发现并缓解部分 mis-scoring，不解释因果 neuron、也非通用 XAI；architecture/distribution 依赖明显。自纠扩覆盖但可能形成 evaluator feedback loop、hard-negative overfit 与新盲区。`Refine — Existing Argument / Experimental`；Books Frozen。

### PAPO

- **Primary / date / coverage / owner:** `ARXIV-2507.06448-PAPO`，v1 2025-07-09，29 页全文、perception-aware objective、implementation、multimodal RLVR evaluation/ablation 与 limitations 已读；27/30。owner `TRAIN-GRPO`，handoff multimodal representation。
- **Problem / mechanism / state flow:** outcome reward 把视觉误读与后续 reasoning 错误混成一个 terminal signal；论文称约 67% errors 来自 perception。PAPO 将 visual grounding signal 纳入 policy gradient，可作为 GRPO/DAPO 插件；image/evidence、perception trace、answer、reward component 与 policy version分开追踪。
- **Evaluation / boundary / trade-off:** selected multimodal benchmarks 支持作者增益，不证明 67% 比例跨数据成立、perception label 无噪或无需 teacher 的实现完全免费；未充分验证 scale/model family。更细 reward 提高 credit assignment，却增大 reward specification 与 shortcut 风险。`Emerging / Experimental`；Books Frozen。

### Hybrid Linear Attention Analysis

- **Primary / date / coverage / owner:** `ARXIV-2507.06457-HYBRID-LINEAR-ATTENTION`，v1 2025-07-09，15 页全文、gating/recurrence variants、scaling experiments、sensitivity 与 limitations 已读；28/30。owner `MODEL-LONG-CONTEXT`，handoff self-attention/execution。
- **Problem / mechanism / state flow:** full attention 保持任意 token interaction，却平方扩展；纯 linear recurrence 有界但遗忘。论文系统比较 linear:full 层比例、gating、hierarchical recurrence 与 forgetting，发现 3:1～6:1 的 hybrid 区间；recurrent state 与 full-attention KV是两种不同 identity/lifecycle。
- **Evaluation / boundary / trade-off:** 模型只到 1.3B、context 4096，不能外推 frontier scale 或 serving latency；结果支持 hybrid branch，而非 linear 替代 full attention。降低 compute 会引入 state compression、reset 与 long-range loss。`Refine — Existing Argument / Experimental`；Books Frozen。

### Verbal Confidence Robustness

- **Primary / date / coverage / owner:** `ARXIV-2507.06489-VERBAL-CONFIDENCE`，v1 2025-07-09，50 页全文、confidence elicitation、attack/defense、datasets、appendices 与 limitations 已读；25/30。owner `PLATFORM-EVALUATION-SYSTEM`，handoff security。
- **Problem / mechanism / state flow:** 让模型“说一个置信度”便宜直观，却把 truth calibration 与生成风格混合。论文对多种 elicitation 施加 perturbation/jailbreak，比较 direct/indirect attacks 与 defenses；answer truth、reported confidence、attack transform、detector output 与 calibration curve必须分开拥有。
- **Evaluation / boundary / trade-off:** direct request 容易检测，indirect perturbation 更易绕过；不证明所有 verbal confidence 无价值，但证明其不是可信的安全边界。防御提高 robustness 仍付出 detector false positives、distribution drift 与 calibration maintenance。`Refine — Existing Argument / Failure Evidence`；Books Frozen。

### SlimCaching

- **Primary / date / coverage / owner:** `ARXIV-2507.06567-SLIMCACHING`，v1 2025-07-09，17 页全文、sub/supermodular formulation、algorithms、evaluation 与 limitations 已读；28/30。owner `INFER-SCHEDULING`，handoff GPU memory 与 `MODEL-MOE`。
- **Problem / mechanism / state flow:** edge device 无法缓存全部 MoE experts，固定 top-popular 缓存忽略请求组合与 expert dependency。SlimCaching 联合选择 limited experts/non-expert components；device cache、request router distribution、expert placement 与 miss/transfer cost分别拥有状态，K>1 时 interdependency 破坏简单 greedy guarantee。
- **Evaluation / boundary / trade-off:** 作者 workload 下优化优于 baselines，但不证明 online nonstationary routing、failure recovery 或真实 network/SLO。命中率提升换来 combinatorial planning、stale popularity 与 placement churn；小模型/稳定分布仍适合 static cache。`Emerging / Experimental`；Books Frozen。

### LPPO

- **Primary / date / coverage / owner:** `ARXIV-2507.06573-LPPO`，v1 2025-07-09，15 页全文、sample-centric schedule、PG-Sampling、tracking、evaluation 与 limitations 已读；26/30。owner `TRAIN-GRPO`，handoff data/evaluation。
- **Problem / mechanism / state flow:** batch-level统一难度和采样预算会让已掌握样本重复消耗、困难样本又缺探索。LPPO 为每个 sample 维护进度统计，以 partial expert prefixes/hints 做 PG-Sampling；sample identity、difficulty/history、expert hint、rollout 与 policy checkpoint共同版本化。
- **Evaluation / boundary / trade-off:** Qwen2.5-Math-7B 及作者设置报告 2～4pp 增益，范围限 math/small expert datasets，不证明跨域或无 teacher 依赖。个体化 curriculum 增加 tracking state、leakage 与 stale-difficulty 风险。`Emerging / Experimental`；Books Frozen。

### Decoder-Hybrid-Decoder

- **Primary / date / coverage / owner:** `ARXIV-2507.06607-DECODER-HYBRID-DECODER`，v1 2025-07-09，35 页全文、architecture、long-generation evaluation 与 conclusion/limitations 已读；28/30。owner `MODEL-LONG-CONTEXT`，handoff KV cache/GPU memory。
- **Problem / mechanism / state flow:** 全 decoder 长生成保持精确 attention 但 KV/compute 增长；纯 hybrid 压缩会损失输入与最近 token。方案以 decoder blocks 包住 hybrid/linear core，保留输入和 recent-token attention、压缩中间 history；exact KV 与 compressed recurrent state需独立标识和失效。
- **Evaluation / boundary / trade-off:** 作者实验支持该 sandwich branch，不提供普遍理论或 production concurrency/SLO；不能把 empirical quality 视为 exact-equivalence。节省状态换来层间接口、compression loss 与 recovery复杂度。`Emerging / Experimental`；Books Frozen。

### Uncertainty Layer-wise Dynamics

- **Primary / date / coverage / owner:** `ARXIV-2507.06722-LAYERWISE-UNCERTAINTY`，v1 2025-07-09，10 页全文、Tuned Lens setup、5 models/11 MCQ datasets、analysis 与 limitations 已读；22/30。owner `PLATFORM-EVALUATION-SYSTEM`，handoff interpretability。
- **Problem / mechanism / state flow:** 若错误在浅层就可见，early exit/abstention 可省 compute。论文比较 correct/incorrect output probability trajectory 与 prediction depth；layer lens、token distribution、final answer 和 label是不同 evidence owner。
- **Evaluation / boundary / trade-off:** 97% correlations 为正但 80% 低于 .3，正确/错误轨迹大体重叠，反而否定简单 layer-probe detector。结论是 preliminary competence relation，不是可靠 uncertainty controller。`No Change — Failure Evidence`；Books Frozen。

### Checklist Engineering for LLM Judges

- **Primary / date / coverage / owner:** `ARXIV-2507.06774-CHECKLIST-JUDGE`，v1 2025-07-09，14 页全文、CE-Judge design、three datasets、pointwise/pairwise evaluation 与 limitations 已读；25/30。owner `PLATFORM-EVALUATION-SYSTEM`。
- **Problem / mechanism / state flow:** 单一 rubric prompt 易漏 task-specific criteria。CE-Judge 先生成/选择 checklist，再逐项判断并聚合；task/rubric、checklist revision、judge response 与 final score需可追溯，judge不是 ground truth owner。
- **Evaluation / boundary / trade-off:** 多语 open model 在作者三套数据上对比 GPT-4o 有竞争力，不证明跨领域、跨语言和 adversarial robustness。结构化 criteria 提高可审计性，却增加 checklist omission、double counting 与生成成本。`Refine — Existing Argument / Experimental`；Books Frozen。

### Adaptive Termination / SEAT

- **Primary / date / coverage / owner:** `ARXIV-2507.06829-SEAT`，v1 2025-07-09，13 页全文、semantic entropy、parallel sampling、threshold/optimal stopping branches、five benchmarks 与 limitations 已读；28/30。owner `INFER-SCHEDULING`，handoff workflow/reflection。
- **Problem / mechanism / state flow:** self-consistency 固定采样数浪费 easy requests，单答案又不能识别不稳定。SEAT 用 semantic clusters/entropy 动态决定 parallel degree 与停止；request 拥有 sample set/cluster state，scheduler 拥有 budget/stop decision，verifier才拥有 task correctness。
- **Evaluation / boundary / trade-off:** 作者数据中 entropy 与 accuracy 负相关、两种 stopping branch 可省算力，但 calibration 随 task/model 变化且额外 samples/embedding 自身有成本。低 entropy 不是真值证明。`Refine — Existing Argument / Experimental`；Books Frozen。

### SetR: Set Selection for RAG

- **Primary / date / coverage / owner:** `ARXIV-2507.06838-SETR`，v1 2025-07-09，14 页全文、requirement inference、set selection、multi-hop evaluation 与 limitations 已读；27/30。owner `AGENT-RAG`。
- **Problem / mechanism / state flow:** independent reranking 假设每 passage 单独有用，无法保证集合覆盖多跳信息。SetR 先推断 information requirements，再选择 collectively complete set；query requirement graph、candidate passages、selected set 与 answer/citation verdict分开拥有。
- **Evaluation / boundary / trade-off:** selected multi-hop benchmarks 支持 set-level objective，不证明 requirement CoT faithful、retriever corpus complete 或 production latency。更完整 context 换来 reasoning/selection compute、冗余与错误 requirement amplification。`Refine — Existing Argument / Experimental`；Books Frozen。

### Open-source AI Evaluation Repository

- **Primary / date / coverage / owner:** `ARXIV-2507.06893-INSPECT-EVALS-PRACTICE`，v1 2025-07-09，7 页全文、8-month maintenance experience、70+ evals、QA categories 与 limitations 已读；25/30。owner `PLATFORM-EVALUATION-SYSTEM`。
- **Problem / mechanism / state flow:** benchmark code能跑不等于结果可复现；长期 repository 需要 model cohort、resampling、cross-model uncertainty 与 review。论文把 task definition、dataset revision、solver/scorer、run config 与 result artifact分层治理。
- **Evaluation / boundary / trade-off:** 这是实践证据而非单一机制 benchmark；不能证明其流程对所有组织最优。严格 QA 增加维护成本，却降低 silent evaluator drift。`No Change — Already Covered / Practice Evidence`；Books Frozen。

### SAGA: Verification for Code Generation

- **Primary / date / coverage / owner:** `ARXIV-2507.06920-SAGA-CODE-VERIFICATION`，v1 2025-07-09，24 页全文、test metrics、human-LLM TCG、TCGBench、evaluation 与 limitations 已读；28/30。owner `PLATFORM-EVALUATION-SYSTEM`，handoff workflow。
- **Problem / mechanism / state flow:** sparse public tests让错误程序 pass，并把 RLVR reward 变成弱 proxy。SAGA 用多维 test-suite metrics 和 human-LLM collaborative test generation；code artifact、test revision、execution sandbox、coverage/mutation evidence 与 verdict分别拥有。
- **Evaluation / boundary / trade-off:** 作者报告 90.62 detection、verifier accuracy 32.58、相对 LCB-v6 +10.78，只适用于其 languages/problems/harness；不证明完整程序正确性或隐藏测试无污染。更强测试提高成本并可能过拟合 generator。`Refine — Existing Argument / Experimental`；Books Frozen。

### Frontier LLMs on Simple Reasoning

- **Primary / date / coverage / owner:** `ARXIV-2507.07313-SIMPLE-REASONING-FAILURES`，v1 2025-07-10，54 页全文、procedural tasks、proof/travel/counting/FOL、Unpuzzles、error analysis 与 appendices 已读；26/30。owner `PLATFORM-EVALUATION-SYSTEM`，handoff worldview/reasoning。
- **Problem / mechanism / state flow:** popular benchmarks混入记忆与复杂知识，难分离基本 algorithmic failure。程序化生成控制 depth/length，并把 intermediate steps 与 final answer分开评分；generator seed、instance graph、model trace 与 verifier verdict有独立 identity。
- **Evaluation / boundary / trade-off:** frontier thinking models仍会 shortcut、intermediate error 和 long-context failure，不证明一般 intelligence 上限，也不代表真实 workload distribution。可控任务提高诊断性但牺牲生态真实性。`Refine — Existing Argument / Failure Evidence`；Books Frozen。

### SAND

- **Primary / date / coverage / owner:** `ARXIV-2507.07441-SAND`，v1 2025-07-10，16 页全文、action sampling、execution-guided critique、iterative SFT、interactive evaluation 与 limitations 已读；25/30。owner `AGENT-PLANNING`，handoff workflow/reflection。
- **Problem / mechanism / state flow:** 单条 demonstration 容易固化偶然轨迹。SAND 对 action 做 self-consistency sampling，以环境执行反馈批评并合成 stepwise deliberation，再迭代 SFT；environment transition是真值，trajectory/critique是derived training data，policy只提议 action。
- **Evaluation / boundary / trade-off:** 作者在 ALFWorld/WebShop 类任务平均约 +20% over SFT，不证明真实工具、副作用 rollback 或开放环境。更多执行提升数据质量但增加 interaction cost、self-bias 与 error reinforcement。`Emerging / Experimental`；Books Frozen。

### RLEP

- **Primary / date / coverage / owner:** `ARXIV-2507.07451-RLEP`，v1 2025-07-10，9 页全文、experience pool、replay/fresh mix、training details 与 limitations 已读；27/30。owner `TRAIN-GRPO`。
- **Problem / mechanism / state flow:** on-policy RL 每轮丢弃已验证成功轨迹，sample inefficient。RLEP 保存 verified successes，以 restart/replay 和 fresh GRPO rollouts 混合；pool item必须绑定 prompt、response、reward/verifier、policy lineage 与 age。
- **Evaluation / boundary / trade-off:** Qwen2.5-Math-7B、16 fresh+2 replay、input1024/output3072，pool 从 400 steps 建立且每 step <5s extra；AIME/AMC 增益限单域单模型。复用经验换来 staleness/off-policy bias 与 storage治理。`Refine — Existing Argument / Experimental`；Books Frozen。

### PLAN-TUNING

- **Primary / date / coverage / owner:** `ARXIV-2507.07495-PLAN-TUNING`，v1 2025-07-10，15 页全文、trajectory distillation、SFT/RL branches、GSM8K/MATH/OOD evaluation 与 limitations 已读；25/30。owner `AGENT-PLANNING`，handoff SFT/GRPO。
- **Problem / mechanism / state flow:** 小模型直接学答案会跳过 plan，在线调用大模型又昂贵。teacher 生成 plan trajectory，student 先 SFT 再以 RL 条件分支优化；teacher trace、filtered dataset、student checkpoint、reward/verifier 与 final answer有独立 provenance。
- **Evaluation / boundary / trade-off:** 作者报告约 7/10/12% 的不同设置增益，只在其 teacher、math corpus 与 OOD Olympiad/AIME contract 下成立；不证明 plan faithful 或跨域。distillation 降 runtime 成本，却继承 teacher bias 并增加长 trace token。`Emerging / Experimental`；Books Frozen。

### Teaching LLM to Reason / TeaR

- **Primary / date / coverage / owner:** `ARXIV-2507.07498-TEAR`，v1 2025-07-10，15 页全文、algorithmic problem curation、RL setup、17 benchmarks 与 limitations 已读；26/30。owner `TRAIN-GRPO`，handoff data/evaluation。
- **Problem / mechanism / state flow:** distilling现成 CoT 可能只复制表面答案模式。TeaR 以无代码的 algorithmic problems 和 executable/answer reward 让 policy 探索 reasoning paths；problem generator、verifier、trajectory 与 checkpoint分别版本化。
- **Evaluation / boundary / trade-off:** 2 base+3 long-CoT distilled models、1.5B～32B；作者报告 Qwen2.5-7B +35.9%、R1-distilled-7B +5.9%，不能外推其他 domains 或证明 trace faithful。可验证合成任务增强 credit，却可能形成 narrow algorithmic curriculum。`Emerging / Experimental`；Books Frozen。

### Selective-DPO

- **Primary / date / coverage / owner:** `ARXIV-2507.07725-SELECTIVE-DPO`，v1 2025-07-10，12 页全文、token selection objective、reference sensitivity、Arena-Hard/MT-Bench evaluation 与 limitations 已读；24/30。owner `TRAIN-DPO`。
- **Problem / mechanism / state flow:** sequence-level DPO 对所有 token 同权，会让格式/共有前缀稀释真正 preference-bearing token。方法按 current/reference log-prob delta 选择 high-impact tokens 再优化；pair、reference checkpoint、selection mask 与 policy version必须绑定。
- **Evaluation / boundary / trade-off:** stronger reference 改变 selection quality，说明收益依赖 reference，不是通用 free lunch；两套 chat eval 不能证明事实性/安全。稀疏梯度聚焦偏好，也可能漏掉分布式语义或放大 noisy token。`Refine — Existing Argument / Experimental`；Books Frozen。

### TruthTorchLM

- **Primary / date / coverage / owner:** `ARXIV-2507.08203-TRUTHTORCHLM`，v1 2025-07-10，12 页全文、30+ methods taxonomy、HF/LiteLLM API、three-dataset evaluation 与 limitations 已读；28/30。owner `PLATFORM-EVALUATION-SYSTEM`。
- **Problem / mechanism / state flow:** truthfulness方法散落在 black/white-box、grounded/non-grounded、supervised/self-supervised实现中，难比较。库统一接口，但每个 method 的 required logits/samples/evidence、calibration data 与 score semantics不同，不能把统一 API 当统一置信度。
- **Evaluation / boundary / trade-off:** TriviaQA/GSM8K/FActScore-Bio 仅展示工具覆盖，不证明某方法普遍最优或 score 已校准。统一框架提升复现，却可能隐藏方法假设与 evaluator coupling。`No Change — Already Covered / Tooling Evidence`；Books Frozen。

### Simple Mechanistic Out-of-Context Reasoning

- **Primary / date / coverage / owner:** `ARXIV-2507.08218-OOC-STEERING`，v1 2025-07-10，8 页全文、LoRA decomposition、steering-vector interventions、backdoor-like cases 与 limitations 已读；25/30。owner `MODEL-TRANSFORMER-LAYER`，handoff LoRA/security。
- **Problem / mechanism / state flow:** LoRA 学到的 out-of-context relation很难解释。论文发现研究任务中的 LoRA update常近似 constant steering vector，直接训练/注入 vector 可复现行为；base activation、adapter delta、steering vector 与 observed output是不同证据层。
- **Evaluation / boundary / trade-off:** 只解释所测 tasks/models，不证明所有 LoRA 或 OOCR 都是线性方向；backdoor-like case 说明可操控也带来供应链风险。低成本 steering 换来 context-independent overreach。`Emerging / Experimental`；Books Frozen。

### KAT-V1

- **Primary / date / coverage / owner:** `ARXIV-2507.08297-KAT-V1`，25 页 event-time v1 2025-07-11 已直接恢复；v2/v3 是后续 revision，正文核验锁定 v1 公开边界。25/30；owner `TRAIN-GRPO`，handoff inference scheduling。
- **Problem / mechanism / state flow:** 单一 reasoning mode 会让简单题过度思考、复杂题又缺预算。40B model 以 dual reasoning/non-reasoning tags、multi-agent synthetic data、MTP distillation、majority-vote cold start 与 Step-SRPO intermediate supervision组合；mode tag、trajectory/reward、checkpoint 与 runtime budget分开拥有。
- **Evaluation / boundary / trade-off:** v1 作者 benchmark 只支持该 recipe 的组合效果，后续版本数字不能倒灌；组件 attribution、production latency/hardware contract 不完整。双模态降低不必要 compute，却增加 mode routing、tag contamination 与 reward complexity。`Emerging / Experimental / Revision-bounded`；Books Frozen。

### ChainEdit

- **Primary / date / coverage / owner:** `ARXIV-2507.08427-CHAINEDIT`，v1 2025-07-10，14 页全文、KG rule construction、connected edit clusters、evaluation 与 limitations 已读；22/30。owner `PLATFORM-EVALUATION-SYSTEM`，handoff memory/data。
- **Problem / mechanism / state flow:** isolated fact edit只测单点记忆，不测逻辑 ripple。ChainEdit 用 KG logical rules 生成相连 edits，分别评 direct retention 与 propagation；source KG/rule、edit set、edited checkpoint 与 query verifier必须有 lineage。
- **Evaluation / boundary / trade-off:** 作者约 >30% logical generalization 说明现有方法弱，不证明 rule set代表开放世界或代码已可复现。关联测试提高因果诊断，但把 validity 绑定到 KG 完整性与 rule correctness。`Emerging / Experimental`；Books Frozen。

### clembench Dialogue-game Evaluation

- **Primary / date / coverage / owner:** `ARXIV-2507.08491-CLEMBENCH`，v1 2025-07-10，11 页全文、clemcore backend、game specs、transcripts/scores、runtime 与 limitations 已读；26/30。owner `PLATFORM-EVALUATION-SYSTEM`，handoff workflow。
- **Problem / mechanism / state flow:** static QA 可重复却不测互动策略；真人 eval真实但昂贵不可控。dialogue games 提供 controlled+interactive+repeatable 第三路径；game spec/environment、model registry、turn transcript、scorer 与 aggregate result分离拥有。
- **Evaluation / boundary / trade-off:** 14 text games/817 instances、5 multimodal/560，并披露 A100 runtime；不证明游戏覆盖真实用户/工具副作用。可重复互动提高诊断，却引入 simulator/game-rule validity。`No Change — Already Covered / Practice Evidence`；Books Frozen。

### LLaPa Procedural Planning

- **Primary / date / coverage / owner:** `ARXIV-2507.08496-LLAPA`，v1 2025-07-10，10 页全文、TER/CAR retrieval、ActPlan-1K、ALFRED evaluation 与 limitations 已读；24/30。owner `MULTIMODAL-EMBODIED-VLA`，handoff agent planning。
- **Problem / mechanism / state flow:** VLM 直接从图像生成长 action list易遗漏 affordance/ordering。Task-sensitive Example Retrieval 做 segmentation/reranking，Counterfactual Action Retrieval 补相似但错误的反例；observation、retrieved examples、plan proposal、controller execution 与 environment transition分开拥有。
- **Evaluation / boundary / trade-off:** ActPlan-1K/ALFRED 支持 procedural plan质量改善，不证明 low-level control、real-time feedback 或 physical safety。retrieval 降 hallucination却增加 corpus dependence、counterfactual contamination 与 latency。`Emerging / Experimental`；Books Frozen。

### KELPS Verified Autoformalization

- **Primary / date / coverage / owner:** `ARXIV-2507.08665-KELPS`，v1 2025-07-10，22 页全文、Knowledge Equations、Lean/Coq/Isabelle rules、60k corpus、MiniF2F evaluation 与 limitations 已读；24/30。owner `AGENT-WORKFLOW`，handoff evaluation。
- **Problem / mechanism / state flow:** NL→proof assistant直接翻译把语义解析与语法生成耦合。KELPS 先生成中间 Knowledge Equations，再用 semantic/syntactic rules编译到多 prover；NL source、IR、backend artifact 与 prover verdict分别拥有。
- **Evaluation / boundary / trade-off:** 作者报告 MiniF2F pass@1 88.9%，只在 corpus/templates/backends 下成立；compile/pass不保证 NL fidelity。IR提高可移植与审计，却增加 schema expressiveness bottleneck。`Emerging / Experimental`；Books Frozen。

### KV Cache Steering

- **Primary / date / coverage / owner:** `ARXIV-2507.08799-KV-CACHE-STEERING`，v1 2025-07-10，21 页全文、trace-derived intervention、reasoning/style transfer、evaluation 与 limitations 已读；25/30。owner `INFER-KV-CACHE`。
- **Problem / mechanism / state flow:** continuous activation steering需要每层每步hook，prompt steering又占 context。方法从 teacher/human trace提取 direction，一次性修改 request KV cache；base weights不变，steering artifact、cache block/request identity、layer/position 与 rollback point必须绑定。
- **Evaluation / boundary / trade-off:** 作者任务支持 reasoning/style transfer，不证明方向是事实知识、跨模型稳定或 production-safe。一次注入较便宜，却会污染 shared prefix、破坏 cache equivalence，并需要 isolation/invalidation。`Emerging / Experimental`；Books Frozen。

### Self-Improving Model Steering / SIMS

- **Primary / date / coverage / owner:** `ARXIV-2507.08967-SIMS`，v1 2025-07-11，16 页全文、self-generated contrastive samples、prompt ranking、iterative directions、evaluation 与 limitations 已读；22/30。owner `MODEL-TRANSFORMER-LAYER`，handoff evaluation/security。
- **Problem / mechanism / state flow:** external labeled contrast pairs昂贵。SIMS 让模型生成对比样本、排序 prompts、迭代估计 steering directions；generation set、ranker judgment、direction version 与 target model activation分别追踪。
- **Evaluation / boundary / trade-off:** 所测行为改善不证明方向 truthful 或 self-evaluation无偏。无标注降低数据成本，却可能 self-amplify bias、collapse diversity 或形成不可见 feedback loop。`Emerging / Experimental`；Books Frozen。

### OpenCodeReasoning-II

- **Primary / date / coverage / owner:** `ARXIV-2507.09075-OPENCODEREASONING-II`，v1 2025-07-11，16 页全文、2.5M triples、two-stage SFT、LiveCodeBench evaluation 与 limitations 已读；22/30。owner `TRAIN-SFT`，handoff evaluation。
- **Problem / mechanism / state flow:** code SFT只有 solution，缺少 critique signal。dataset为约35k问题构造 question-solution-critique triples，先训 generation 再联合 generation+critique；problem/test、solution、critique source 与 checkpoint lineage必须记录。
- **Evaluation / boundary / trade-off:** C++/LCB extension 结果只支持该语言与数据 pipeline，不证明 critique faithful 或无污染。更丰富 supervision 增 token/curation cost并可能复制 generator error。`Weekly Only — Dataset Evidence / Experimental`；Books Frozen。

### CompassJudger-2

- **Primary / date / coverage / owner:** `ARXIV-2507.09104-COMPASSJUDGER-2`，v1 2025-07-11，18 页全文、task-driven curation、verifiable rewards、margin policy gradient、JudgerBenchV2 与 limitations 已读；26/30。owner `PLATFORM-EVALUATION-SYSTEM`，handoff GRPO。
- **Problem / mechanism / state flow:** generic judge在跨域 task criteria 上不稳定。pipeline按任务构造数据、用 verifiable reward/rejection sampling过滤，再以 margin policy gradient训练；rubric/task、candidate pair、verification evidence、judge checkpoint 与 aggregate rank分开拥有。
- **Evaluation / boundary / trade-off:** 7B model在作者 cross-domain accuracy/rank consistency 上可比更大 judge，不证明独立 truth或对抗鲁棒。专用训练降低 size，却增加 rubric coverage 与 self-referential evaluation风险。`Refine — Existing Argument / Experimental`；Books Frozen。

### Detrimental Neuron Pruning

- **Primary / date / coverage / owner:** `ARXIV-2507.09185-DETRIMENTAL-NEURON-PRUNING`，v1 2025-07-11，20 页全文、Integrated Gradients selection、fine-tuning/pruning、OOD MCQ evaluation 与 limitations 已读；24/30。owner `MODEL-TRANSFORMER-LAYER`，handoff SFT。
- **Problem / mechanism / state flow:** fine-tuning 会强化 dataset-specific shortcuts并损害 OOD。方法用 Integrated Gradients 找支持高置信 shortcut 的 neurons，在 tuning 时 pruning；base neuron identity、attribution dataset、mask、checkpoint 与 OOD harness需绑定。
- **Evaluation / boundary / trade-off:** 所测 MCQ OOD改善不证明 identified neurons普遍“有害”或 attribution causal。pruning可抑制 shortcut，却可能删通用能力并依赖 probe distribution。`Emerging / Experimental`；Books Frozen。

### Continual Pretraining Dense/MoE for Tibetan

- **Primary / date / coverage / owner:** `ARXIV-2507.09205-TIBETAN-DENSE-MOE`，v1 2025-07-11，16 页全文、72GB corpus、CPT/SFT、dense-to-MoE、evaluation 与 limitations 已读；25/30。owner `TRAIN-DATA`，handoff pretraining/MoE。
- **Problem / mechanism / state flow:** low-resource language直接依赖 multilingual base会受 tokenizer/data imbalance。pipeline平衡 Tibetan/Chinese/English continued pretraining Qwen2.5-7B，再 instruction tune并扩为 50B-A10B MoE；corpus provenance/mixture、dense checkpoint、expert conversion、router 与 eval translation分别拥有。
- **Evaluation / boundary / trade-off:** translated/human-verified tests支持作者语言增益，artifact在事件时仅 promised，不能复算；不证明其他低资源语言或 50B serving cost。专项覆盖换来 catastrophic forgetting、translation bias 和 expert memory。`Emerging / Experimental / Artifact Not Disclosed`；Books Frozen。

### DATE-LM

- **Primary / date / coverage / owner:** `ARXIV-2507.09424-DATE-LM`，v1 2025-07-11，31 页全文、data-attribution taxonomy、selection/toxicity/bias/factual tasks、baselines 与 limitations 已读；24/30。owner `TRAIN-DATA`，handoff evaluation。
- **Problem / mechanism / state flow:** attribution方法常只在单一 removal/influence task 上宣称优越。DATE-LM用多个 operational tasks比较 methods；training example、attribution score、selection/filter action、retrained artifact 与 downstream metric形成完整因果链。
- **Evaluation / boundary / trade-off:** 无方法普遍占优且简单 baseline有竞争力，证明 design sensitivity，而非 attribution无用。更复杂 attribution增加 compute与超参，却未必改善 actionable outcome。`Refine — Existing Argument / Evaluation Evidence`；Books Frozen。

### Ref-Long

- **Primary / date / coverage / owner:** `ARXIV-2507.09506-REF-LONG`，v1 2025-07-11，20 页全文、synthetic-to-real subsets、13 LCLMs、human/error analyses 与 limitations 已读；26/30。owner `MODEL-LONG-CONTEXT`，handoff evaluation/RAG。
- **Problem / mechanism / state flow:** needle retrieval只找 isolated key，不测长文档中关系定位。Ref-Long要求返回支撑特定 key 的 document indexes，强调跨文档 referencing；corpus/order、query relation、gold index set、model citation 与 answer correctness分开拥有。
- **Evaluation / boundary / trade-off:** advanced models仍失败，说明 long context window不等于 relational referencing；不证明真实 corpus coverage 或 retrieval-free serving更优。更强 benchmark提高诊断却依赖 synthetic template与index annotation。`Refine — Existing Argument / Benchmark Evidence`；Books Frozen。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / technical report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系是本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper v1 与后续集成若日期不同，分别记录证据角色，但只建立一个 Books source packet。
- 新方案不静默覆盖旧方案；记录新增状态、成本和 failure modes。
- Teach Old SAEs以2025-07-08 OpenReview为W28 owner；2025-07-17 arXiv v1只作W29 forward revision，不重复计分。
- UQLM以`2504.19254` v1 2025-04-27为W18 owner；`2507.06196` v1 2025-07-08是same-family package descriptor，只保留formal API/release relation，不重复计分。

## Knowledge Tree Position

- Kimi K2 release → 第 21、24、29、32、45、74 章（Direct Evolution）

## Recommended Action

- 当前状态为`Candidate Evidence Conditional — 82/86 retained strict；4 exact blockers；Review Pending 0`。blocker-skip 只关闭候选阅读队列，不代表 discovery exhaustiveness。
- 5项低分已闭合；GoalfyMax保持`Disputed — Identity/Approval`，不得吸收其结论。
- fixed-org/HF/AI Infra replay 已闭合；academic cross-index immutable export 缺口保留。后续新family按 first-public date 加入 owner week，不以当前 91 项假装 exhaustive。

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

`Frozen — Historical Books Gate Closed`。本轮只重建 Weekly evidence；四项 blocked 与任何后续 discovery spillback 均不得写入 Books。


## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。

## Repository Changes

- 将旧 1 项账本校准并去重为 91 个 scored owner lower-bound；RAT、GradOT、S³、DP-Fusion 的 v1 均为 2025-07-06，评分 owner 回拨 W27；UQLM 按 research first-public 回拨 W18。
- 当前 82/86 retained 完成 strict Full Source Review，4 项为精确 `Unverified / Blocked`，`Review Pending = 0`，5 项低分闭合；本阶段未修改 Books。

## Open Questions

- 四项材料缺口何时可恢复：POLAR、Response Attack 的 event-time v1 全文，Agent KB 的 v1 revision，以及 Teach Old SAEs 的 2025-07-08 OpenReview 原始 submission？Spatio-Temporal LLM 与 NeoBabel v1 已恢复，不再列缺口。Omni-Router仍需event-time repository/checkpoint与capacity/dispatch runtime contract。
- Helix的simulator evidence、vLLM EPLB/P-D lifecycle、ArtifactsBench executable evidence与AutoTriton verifier hierarchy能否获得独立复现或production failure data？
- GoalfyMax是否能取得作者批准链和无冲突event-time artifact？

## Sources

除单独标注的 historical access 外，本轮恢复来源统一 Accessed: 2026-08-24；first-public/v1 date 以对应 Source Review packet 为准，later revision 不改变 owner week。

- Kimi K2 release — https://github.com/moonshotai/Kimi-K2（First Public: 2025-07-11 (release); 2025-07-28 (report v1)；Accessed: 2026-07-31）
- Kimi K2 technical report — https://arxiv.org/abs/2507.20534（v1: 2025-07-28；v2: 2026-02-03；Accessed: 2026-07-31）
- UQLM package descriptor — https://arxiv.org/abs/2507.06196（v1: 2025-07-08；Cross-week related only；canonical owner W18）
- SARA — https://arxiv.org/abs/2507.05633
- ECom-Bench — https://arxiv.org/abs/2507.05639
- DRAGOn v1 — https://arxiv.org/abs/2507.05713
- DRAGOn artifact — https://github.com/RussianNLP/DRAGON
- HIRAG v1 — https://arxiv.org/abs/2507.05714
- Omni-Router v1 — https://arxiv.org/html/2507.05724v1
- Omni-Router official repository — https://github.com/apple/ml-omni-router-moe-asr
- SmolLM3 technical blog — https://huggingface.co/blog/smollm3
- SmolLM3 model card — https://huggingface.co/HuggingFaceTB/SmolLM3-3B
- vLLM v0.9.2 release — https://github.com/vllm-project/vllm/releases/tag/v0.9.2
- ArtifactsBench — https://arxiv.org/abs/2507.04952
- AutoTriton — https://arxiv.org/abs/2507.05687
- FlexOlmo — https://arxiv.org/abs/2507.07024
- FlexOlmo artifact — https://github.com/allenai/FlexOlmo
- Machine Bullshit — https://arxiv.org/abs/2507.07484
- Machine Bullshit project — https://machine-bullshit.github.io/
- SpindleKV — https://arxiv.org/abs/2507.06517
- Krul — https://arxiv.org/abs/2507.08045
- Compactor — https://arxiv.org/abs/2507.08143
- Compactor artifact — https://github.com/vnchari/compactor-vllm
- NVIDIA Helix — https://arxiv.org/abs/2507.07120
- VisualTrap — https://arxiv.org/abs/2507.06899
- CCQ — https://arxiv.org/abs/2507.07145
- MemoryAgentBench — https://arxiv.org/abs/2507.05257
- MemoryAgentBench artifact — https://github.com/HUST-AI-HYZ/MemoryAgentBench
- Grok 4 official — https://x.ai/news/grok-4
- DeepSpeed v0.17.2 — https://github.com/deepspeedai/DeepSpeed/releases/tag/v0.17.2
- DeepSpeed autocast + ZeRO PR — https://github.com/deepspeedai/DeepSpeed/pull/6993
- Transformers v4.53.2 — https://github.com/huggingface/transformers/releases/tag/v4.53.2
- Knowledge-Aware Self-Correction — https://arxiv.org/abs/2507.04625
- TokenShapley — https://arxiv.org/abs/2507.05261
- Survey on Latent Reasoning — https://arxiv.org/abs/2507.06203
- GoalfyMax — https://arxiv.org/abs/2507.09497
- RedOne — https://arxiv.org/abs/2507.10605
- PRIME — https://arxiv.org/abs/2507.04607
- Cross-Distillation / EI-BERT — https://arxiv.org/abs/2507.04636
- XiYan-SQL — https://arxiv.org/abs/2507.04701
- LOOM-Scope — https://arxiv.org/abs/2507.04723
- CoSteer — https://arxiv.org/abs/2507.04756
- Reason to Rote — https://arxiv.org/abs/2507.04782
- InfoSteer — https://arxiv.org/abs/2507.05158
- OpenS2S — https://arxiv.org/abs/2507.05177
- LCDS — https://arxiv.org/abs/2507.05319
- Cascade private inference — https://arxiv.org/abs/2507.05228
- Red Teaming AI Red Teaming — https://arxiv.org/abs/2507.05538
- How Not to Detect Prompt Injections with an LLM — https://arxiv.org/abs/2507.05630
- SpaceVerse — https://arxiv.org/abs/2507.05731
- Function Calling vs MCP security — https://arxiv.org/abs/2507.06323
- Function Calling vs MCP artifact — https://github.com/theconsciouslab-ai/llm-agent-security
- Next-token predictors and inefficient reasoning — https://arxiv.org/abs/2507.05362
- Next-token predictor trace artifact — https://github.com/riccardoalberghi/DP
- MobileGUI-RL — https://arxiv.org/abs/2507.05720
- POLAR — https://arxiv.org/abs/2507.05197（Blocked: event-time v1 full text）
- Response Attack — https://arxiv.org/abs/2507.05248（Blocked: event-time v1 full text）
- Spatio-Temporal LLM v1 — https://arxiv.org/abs/2507.05258
- OpenFActScore — https://arxiv.org/abs/2507.05965
- RabakBench — https://arxiv.org/abs/2507.05980
- Conditional Multi-Stage Failure Recovery — https://arxiv.org/abs/2507.06016
- Data Compressibility Quantifies Memorization — https://arxiv.org/abs/2507.06056
- NeoBabel v1 HTML — https://arxiv.org/html/2507.06137v1
- NeoBabel artifact — https://github.com/mmderakhshani/NeoBabel
- Skywork-R1V3 — https://arxiv.org/abs/2507.06167
- CriticLean — https://arxiv.org/abs/2507.06181
- Agent KB — https://arxiv.org/abs/2507.06229（Blocked: event-time v1 revision）
- Reranking FLOPs — https://arxiv.org/abs/2507.06223
- PERK — https://arxiv.org/abs/2507.06415
- REFORM / Reward Model Correct Itself — https://arxiv.org/abs/2507.06419
- PAPO — https://arxiv.org/abs/2507.06448
- Hybrid Linear Attention Analysis — https://arxiv.org/abs/2507.06457
- Verbal Confidence Robustness — https://arxiv.org/abs/2507.06489
- SlimCaching — https://arxiv.org/abs/2507.06567
- LPPO — https://arxiv.org/abs/2507.06573
- Decoder-Hybrid-Decoder — https://arxiv.org/abs/2507.06607
- Uncertainty Layer-wise Dynamics — https://arxiv.org/abs/2507.06722
- Checklist Engineering for LLM Judges — https://arxiv.org/abs/2507.06774
- Adaptive Termination / SEAT — https://arxiv.org/abs/2507.06829
- SetR — https://arxiv.org/abs/2507.06838
- Open-source AI Evaluation Repository — https://arxiv.org/abs/2507.06893
- SAGA / Verification for Code Generation — https://arxiv.org/abs/2507.06920
- Frontier LLMs on Simple Reasoning — https://arxiv.org/abs/2507.07313
- SAND — https://arxiv.org/abs/2507.07441
- RLEP — https://arxiv.org/abs/2507.07451
- PLAN-TUNING — https://arxiv.org/abs/2507.07495
- TeaR — https://arxiv.org/abs/2507.07498
- Selective-DPO — https://arxiv.org/abs/2507.07725
- TruthTorchLM — https://arxiv.org/abs/2507.08203
- Simple Mechanistic Out-of-Context Reasoning — https://arxiv.org/abs/2507.08218
- KAT-V1 — https://arxiv.org/abs/2507.08297
- ChainEdit — https://arxiv.org/abs/2507.08427
- clembench dialogue-game evaluation — https://arxiv.org/abs/2507.08491
- LLaPa — https://arxiv.org/abs/2507.08496
- KELPS — https://arxiv.org/abs/2507.08665
- KV Cache Steering — https://arxiv.org/abs/2507.08799
- SIMS — https://arxiv.org/abs/2507.08967
- OpenCodeReasoning-II — https://arxiv.org/abs/2507.09075
- CompassJudger-2 — https://arxiv.org/abs/2507.09104
- Detrimental Neuron Pruning — https://arxiv.org/abs/2507.09185
- Continual Pretraining Dense/MoE Tibetan — https://arxiv.org/abs/2507.09205
- DATE-LM — https://arxiv.org/abs/2507.09424
- Ref-Long — https://arxiv.org/abs/2507.09506
- Teach Old SAEs OpenReview — https://openreview.net/forum?id=d4XXFVAlV7（First Public: 2025-07-08）
- Teach Old SAEs arXiv v1 — https://arxiv.org/abs/2507.12990（2025-07-17；forward revision）
