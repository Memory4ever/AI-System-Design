# AI Research Weekly — 2025-W31

> Coverage Window: 2025-07-28～2025-08-03
> Research Mode: Retrospective Backfill
> Audit Status: Candidate Evidence Gate Passed — 48-row Discovery Replay and W32 Spillback Reconciliation Complete
> Historical Books Gate: Closed — existing decisions are provisional
> Initial Archive Accessed: 2026-07-31
> Prior Strict Review Accessed: 2026-08-22
> Discovery Replay Accessed: 2026-08-24
> Backfilled: 2026-07-31
> Last Re-audited: 2026-08-24

## Executive Summary

旧档案只保留 GLM-4.5 与 Kimi K2 report，不能代表本周学术和 runtime 召回。初轮 36-row closure 又被 W32 discovery 的 owner-date spillback 推翻；本轮逐项回拨 14 个 W31 owner，其中 RL-PLUS、Cognitive Kernel-Pro 已在 canonical ledger，另外 12 项补入并完成审计。最终闭合 48 个 scored owner：21 项 25～30 分、11 项 20～24 分、16 项低于 20 分。32/32 retained owner 均完成非模板化 Full Source Review，16/16 低分均完成来源、日期、评分与拒绝闭合，ordinary `Review Pending = 0`、`Unverified / Blocked = 0`。G-Core 的事件时 v1 已从作者上传镜像恢复并阅读全文，但因次日以“未经公司批准上传”撤回，保持 `Disputed — Withdrawn Source / Mechanism Evidence Frozen`，不转化为正常发布事实。Candidate Evidence Gate 与周级 Discovery Replay Gate 通过；年度 Archive Completion 与 Historical Books Gate 继续关闭，本轮不修改 Books。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；后续修订回链首次公开周。
- Scholar、OpenAlex、DBLP 负责 discovery/去重；论文事实回到正文。Crossref 仅交叉检验 metadata。
- 历史回填不创建 Daily；旧档已核来源保留原 `Accessed: 2026-07-31`，此前 strict review 保留 `Accessed: 2026-08-22`，本轮 discovery replay 新增、恢复或重试的来源记录为 `Accessed: 2026-08-24`，不得用统一日期覆盖实际访问批次。
- 作者/厂商 benchmark 缺少完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外模型公司、研究机构与 Hugging Face Blog。

- 保留：GLM-4.5（2025-07-28 release；technical report v1 属于 W32）与 Kimi K2 同族技术报告事件。
- 固定机构复核未发现另一项可由官方材料证明、且 first-public 落在本周的独立模型发布；HunyuanWorld、Step-3 等 discovery hit 均按 arXiv v1/官方首发日期重新路由或作为学术 owner 处理，不用 Hugging Face 上榜日期冒充事件日期。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1 正文核验。

- 保留 30 个正常论文 owner：Kimi K2、SLAI、Graph-R1、DICE、Graph-Augmented Agents survey、GMPO、RLSF、AutoTIR、Multi-Agent-as-Judge、MemTool、Persona Vectors、TriangleMix、Falcon-H1、Geak、TTS-1、Compressed History States、Self-Evolving Agents survey、Watch the Weights，以及从 W32 回拨的 CoT Mirage、Beyond Fixed、SitEmb-v1.5、LiveMCPBench、Representation Shift、A Glimpse to Compress、SWE-Exp、SWE-Debate、Cyber-Zero、FACTORY、RoboMemory、Web-CogReasoner；另将 withdrawn G-Core 作为 source-complete disputed owner 保留。
- 16 个外围论文完成低分 closure；H-MEM 的 v1 实际为 2025-07-23，回拨 W30，不在 W31 重复计分。ARPO、GEPA、Deep Researcher、Beyond Binary Rewards 与 Quantization Geometry 同理由 v1 日期回拨 W30。

## 3. AI Infra 与工程项目

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → Dynamo → TensorRT-LLM → Ray → KServe → Kubeflow → Kubernetes → Hugging Face → DeepSpeed → Megatron-LM → llama.cpp → ONNX Runtime → OpenXLA 扫描。

- 本周未发现新的 final release owner。TensorRT-LLM `v1.0.0rc4`（2025-07-22）、SGLang Q3 roadmap（2025-07-03）、Ray Q3 roadmap（2025-07-25）与 vLLM v0.9.2 均属于更早 owner week；TensorRT-LLM `v1.0.0rc5` 与 `v0.21.0` 为 2025-08-04，归 W32。普通 PR/issue 不因在本周有评论而升级为版本事件。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GLM-4.5 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；与 Qwen3/DeepSeek V3.1 比较 hybrid contract |
| Kimi K2 technical report | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Must Read；Books 只形成一个 K2 source packet |
| Optimal Scheduling Algorithms for LLM Inference / SLAI | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Source Review Complete — Emerging / Experimental / Artifact Not Disclosed |
| Graph-R1 | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete — Emerging / Experimental / Theory Claim Disputed |
| DICE | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full Source Review Complete — Emerging / Experimental / Formal Claims Disputed |
| Graph-Augmented Large Language Model Agents survey | 2 | 4 | 3 | 4 | 5 | 3 | 21/30 | Full Source Review Complete — Secondary Taxonomy / No Change Already Covered |
| Geometric-Mean Policy Optimization (GMPO) | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete — Emerging / Experimental |
| Reinforcement Learning from Self-Feedback (RLSF) | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete — Emerging / Calibration Boundary |
| AutoTIR | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete — Emerging / Experimental |
| Multi-Agent-as-Judge / MAJ-Eval | 4 | 3 | 4 | 4 | 5 | 3 | 23/30 | Full Source Review Complete — Emerging / Human-Alignment Boundary |
| MemTool | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Full Source Review Complete — Refine Candidate |
| Persona Vectors | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Emerging / Experimental |
| Accelerating Prefilling via Decoding-time Contribution Sparsity / TriangleMix | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Source Review Complete — Emerging / Experimental |
| Falcon-H1 technical report | 5 | 5 | 4 | 5 | 5 | 5 | 29/30 | Full Source Review Complete — Refine Candidate |
| GEAK Triton Kernel Agent and Benchmarks | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete — Refine Candidate |
| TTS-1 Technical Report | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Emerging / Experimental |
| Compressed History States for Web Agent Automation | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete — Emerging / Experimental |
| Self-Evolving Agents survey | 3 | 4 | 3 | 4 | 5 | 4 | 23/30 | Full Source Review Complete — Secondary Taxonomy |
| G-Core RLHF Trainer | 5 | 5 | 5 | 2 | 5 | 4 | 26/30 | Full Source Review Complete — Disputed / Withdrawn Source |
| Watch the Weights | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Emerging / Experimental |
| CoT Mirage / DataAlchemy | 4 | 4 | 3 | 4 | 5 | 4 | 24/30 | Full Source Review Complete — Emerging / Controlled Synthetic Evidence |
| Beyond Fixed / DAEDAL | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Emerging / Experimental |
| SitEmb-v1.5 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete — Refine Candidate |
| LiveMCPBench | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Full Source Review Complete — Refine Candidate |
| Representation Shift | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Emerging / Experimental |
| A Glimpse to Compress / GlimpsePrune | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Source Review Complete — Emerging / Experimental |
| SWE-Exp | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Full Source Review Complete — Refine Candidate |
| SWE-Debate | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review Complete — Emerging / Experimental |
| Cyber-Zero | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete — Emerging / Security Boundary |
| FACTORY | 3 | 4 | 5 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Refine Evaluation Contract |
| RoboMemory | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full Source Review Complete — Emerging / Experimental |
| Web-CogReasoner | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review Complete — Emerging / Experimental |
| FRED hallucination detection and editing | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Reject — narrow activation-editing study; no system contract |
| Conformative Decoding | 4 | 3 | 3 | 4 | 3 | 1 | 18/30 | Reject — method signal retained; project relevance too narrow |
| Text Embeddings survey | 2 | 3 | 3 | 4 | 3 | 2 | 17/30 | Reject — secondary overview; already covered |
| Multilingual Self-Taught Faithfulness Evaluators | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Reject — limited language/task transfer evidence |
| NeedleChain | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Reject — benchmark-only owner, limited system mechanism |
| IFEvalCode | 3 | 3 | 4 | 4 | 3 | 2 | 19/30 | Reject — evaluation asset, not a new system mechanism |
| Discrete Tokenization for Multimodal LLMs survey | 2 | 3 | 3 | 4 | 4 | 3 | 19/30 | Reject — secondary taxonomy; Part III already owns mechanism |
| PRGB Benchmark | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Reject — placeholder benchmark does not change RAG contract |
| CoT Mechanistic Interpretability with Sparse Autoencoding | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Reject — exploratory interpretability evidence |
| LENS multi-LLM confidence integration | 4 | 3 | 3 | 3 | 3 | 3 | 19/30 | Reject — ensemble confidence lacks deployment calibration |
| Super Experts in MoE LLMs | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Reject — analysis does not establish routing redesign |
| User Feedback as a Noisy Learning Signal | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Reject — observational evidence; no robust update mechanism |
| RL-PLUS | 4 | 3 | 3 | 3 | 3 | 3 | 19/30 | Reject — hybrid-policy claim not yet system-general |
| MetaAgent | 4 | 3 | 3 | 3 | 3 | 3 | 19/30 | Reject — tool meta-learning evidence too narrow |
| Pro2Guard | 4 | 3 | 3 | 3 | 3 | 3 | 19/30 | Reject — probabilistic-checking prototype lacks production contract |
| Cognitive Kernel-Pro | 4 | 3 | 3 | 3 | 3 | 3 | 19/30 | Reject — deep-research framework evidence not yet durable |

### Deep Analysis 1 — GLM-4.5

- First Public: 2025-07-28 (release); 2025-08-08 (paper v1)
- Status: Official open-weight release; report published later
- Primary Source: https://github.com/zai-org/GLM-4.5
- Evolution Relationship: Direct Evolution

#### Why

面向 agent 的模型开始把 reasoning、coding、tool use 与 non-thinking latency 放到同一 base model contract。

#### Principle and Mechanism

官方仓库披露 hybrid reasoning、MoE 尺寸、deployment paths 与 tool/reasoning parsers；论文 v1 在 W32，需分开记录。

#### Trade-off and Evidence Boundary

统一模型减少 fleet 分裂，却增加 parser compatibility、mode state、reasoning token 与引擎 feature matrix。作者排名不写成通用结论。

#### Connection and Evolution

知识树位置：第 20、21、29、45、46、74 章。Must Read；与 Qwen3/DeepSeek V3.1 比较 hybrid contract。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

### Deep Analysis 2 — Kimi K2 technical report

- First Public: 2025-07-28
- Status: arXiv v1; official technical report
- Primary Source: https://arxiv.org/abs/2507.20534
- Evolution Relationship: Layering / Dependency

#### Why

W28 的产品/权重事实需要报告补足 optimizer stability、训练数据、post-training 和 infrastructure boundary。

#### Principle and Mechanism

报告详细描述 MuonClip、MoE training、agentic data 与评测；这是对 W28 release 的证据补全，不是第二个独立模型事件。

#### Trade-off and Evidence Boundary

作者披露提升可审计性，但训练稳定性和 benchmark 仍需按实现、数据与硬件限定。

#### Connection and Evolution

知识树位置：第 21、24、29、32、45、74 章。Must Read；Books 只形成一个 K2 source packet。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

## Full Source Review

### GLM-4.5 release

- **Candidate / Week / Score:** GLM-4.5 release / 2025-W31 / 25/30。
- **Source Family ID:** `GLM-4.5-2508.06471`（与 W32 technical report 联读）。
- **Source Type:** official repository/open weights/model cards/deployment documentation；technical report后发。
- **First-public Date / Revision History:** release 2025-07-28；technical report arXiv v1 2025-08-08。release事件只保留当时 artifact/interface事实，报告机制在 W32归档。
- **Direct Primary Sources:** `zai-org/GLM-4.5` release-time README、model cards/config/weights；official inference examples。
- **Related Primary Sources:** arXiv:2508.06471；Transformers/vLLM/SGLang model/reasoning/tool parser support用于compatibility核验。
- **Access and Verification Status:** Verified for released model sizes, modes, weights/license and documented deployment；training/post-training mechanism由W32 report补证，production SLA/failure data Not Disclosed。
- **Full-read Coverage:** 已阅读release/model cards的355B-A32B与106B-A12B variants、thinking/non-thinking contract、BF16/FP8 artifacts、parser/runtime matrix与GPU memory examples；对照后发报告标记release未公开机制。
- **Original Problem:** agent workload既需要复杂reasoning/tool use，也需要低latency direct response；若拆成多个独立model fleets，会增加routing、evaluation与version governance。
- **Why the Previous Design Was Reasonable:** 专用reasoning model与chat model各自优化清晰，mode不混淆；外部workflow可显式选model并控制cost。
- **Changed Constraint:** 同一产品希望共享base capability、tool protocol与deployment stack，同时按请求切换thinking budget；open weights还必须交付parser和runtime compatibility。
- **Mechanism:** release可确认hybrid reasoning的thinking/direct response两种公开模式、355B/32B-active与Air 106B/12B-active、base/hybrid/FP8 artifacts；23T training、loss-free balancing与RL流程只由W32 report证明。
- **State Ownership:** artifact registry拥有model/config/tokenizer；request policy拥有mode选择；runtime parser拥有reasoning/tool channel解释；workflow拥有tool authority。model文本不能自行改变mode或权限事实。
- **Control Flow / Data Flow:** request+mode policy → chat template/parser config → MoE serving → reasoning/direct response或tool proposal → workflow验证；release文档没有公开provider内部router。
- **Implementation Details:** official repo列出Transformers/vLLM/SGLang parser路径与最低GPU组合（如BF16 16×H100、FP8 8×H100的示例）；它们是deployment guidance，不是吞吐/SLO保证。
- **Evaluation Setup:** release汇总12项benchmark并形成overall score；model/precision/harness/scaffold异构，且无统一hardware、concurrency、length与latency contract。
- **Baselines / Ablations / Sensitivity:** release无controlled architecture/training ablation；两种mode也没有production routing误差或cost-quality curve。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model size、BF16/FP8 artifact和最低H100配置示例可核；batch/concurrency、input/output、TTFT/TPOT、network与SLO Not Disclosed。
- **What the Evidence Actually Proves:** 证明同一open-weight family对外暴露mode contract并要求runtime/parser配套，形成“model artifact不是单一weights文件”的系统事实。
- **What It Does Not Prove:** 不证明统一hybrid model总优于双模型fleet，不证明FP8与BF16质量等价，不证明综合排名或GPU数量代表production efficiency。
- **Limitations / Threats to Validity:** repository当前包含后续GLM-4.6/4.7信息，必须版本隔离；release benchmark为作者评测；tool/reasoning parser兼容和外部runtime版本可能漂移。
- **Trade-offs / New Failure Modes:** 共享family减少fleet分裂，却新增mode/parser state、reasoning token成本、backend feature matrix、quantization parity与rolling upgrade coupling。
- **Where the Previous Design Still Applies:** SLO与行为隔离严格、traffic可预测或runtime不支持hybrid parser时，专用fast/reasoning model fleets仍更清晰。
- **Evolution Relationship:** `Direct Evolution`：separate chat/reasoning serving → one family with explicit mode contract；这不是内部统一router已公开的证据。
- **ROADMAP Node:** Ch20～21、Ch31、Ch45～48、Ch52、Ch74。
- **Target and Adjacent Chapters Read:** 已阅读 Ch19～22、Ch30～32、Ch44～48、Ch51～52、Ch73～75；主 owner 倾向model/runtime interface，待W32 mechanism packet后决定。
- **Existing Coverage:** Ch46～48已覆盖model config/parser/runtime contract，Ch52覆盖routing/cost；release主要补充Version/Product Fact，单独不足以修改核心设计结论。
- **Integration Decision:** `Weekly Only — Version/Product Fact`；与 W32 report 合并去重。
- **Changed Files or Rejection Reason:** 不改 Books；release 不独立驱动机制结论。
- **Open Questions:** release-time commit/model-card snapshot、mode contamination、FP8 parity、parser compatibility tests与production routing/SLO。

### Kimi K2 technical report

- **Candidate / Week / Score:** Kimi K2 technical report / 2025-W31 / 27/30。
- **Source Family ID:** `KIMI-K2-2507.20534`（与 W28 release同族）。
- **Source Type:** official arXiv technical report v1、v2 minor revision、weights/repository/artifacts。
- **First-public Date / Revision History:** arXiv v1 2025-07-28；v2 2026-02-03标为minor updates。历史结论以v1为准，v2只用于发现修订，不改变first-public。
- **Direct Primary Sources:** arXiv:2507.20534 v1 PDF/HTML与v2 revision；Kimi K2 base/instruct artifacts/repository。
- **Related Primary Sources:** Muon/Moonlight lineage、DeepSeek-V3 MLA/MoE/MTP lineage、公开agent benchmark harness。
- **Access and Verification Status:** Verified for full report and released artifacts；complete pretraining data、MuonClip/training code、RL environment implementation、kernel patches与independent reproduction unavailable。
- **Full-read Coverage:** 已阅读metadata/v1-v2 history、Introduction/architecture、MuonClip formula/ablation、pretraining data/recipe、distributed training/activation management、long-context extension、SFT/agentic data/RL、evaluation protocols与appendix、safety/known weaknesses/conclusion；并检查artifact config。
- **Original Problem:** 超大稀疏MoE在长训练中既要获得Muon的sample efficiency，又要避免attention logits爆炸；同时agent post-training需要可扩展environment和训练/rollout引擎切换。
- **Why the Previous Design Was Reasonable:** AdamW易理解且成熟；标准Muon改善矩阵参数更新；dense/GQA架构和独立训练/推理集群在较小scale下简化一致性与调度。
- **Changed Constraint:** 1T total参数、15.5T tokens、长context与MLA/MoE让optimizer数值稳定、activation memory、expert communication和rollout utilization共同成为约束。
- **Mechanism:** K2为1T/32B-active ultra-sparse MoE+MLA；MuonClip在Muon/weight decay/consistent RMS scaling之上监测attention logits并对Q/K updates做clip（threshold 100）；agentic post-training合成tool specs/agents/tasks/trajectories并在real/synthetic environments做joint RL。
- **State Ownership:** trainer拥有weights/optimizer与QK-clip statistic；data pipeline拥有15.5T corpus与agent specs；environment/verifier拥有outcome/reward；colocated runtime在training/rollout切换时必须维护权重版本与precision一致性。
- **Control Flow / Data Flow:** pretrain 4K context → MuonClip stability control → long-context stages（4K/32K并用YaRN到128K）→ SFT/agent data synthesis → environment rollout/self-critique rubric → group-relative RL + PTX regularization → checkpoint/artifact。
- **Implementation Details:** mid-scale 53B/9B-active ablation；H800 nodes每节点8 GPUs/NVLink/NVSwitch、inter-node 8×400Gbps RoCE；16PP×16EP+ZeRO-1，6TB parameter/gradient buffers跨256 GPUs；selective recompute、FP8-E4M3仅存activation并配FP32 scales、CPU offload、interleaved 1F1B overlap。训练用BF16参数/FP32 gradient accumulation。
- **Evaluation Setup:** non-thinking setting，通常最大output 8,192，SWE-bench 16,384；long-context测到128K；部分任务多次sampling或best-of-N内部verifier；agent benchmarks使用各自scaffold/environment，因此不能按单一harness横比。
- **Baselines / Ablations / Sensitivity:** 对MuonClip组件和attention-head选择做mid-scale study；64 heads相对更多heads权衡loss与128K inference FLOPs。未公开1T full-run optimizer对照、完整data ablation、RL environment/scaffold sensitivity或独立复现。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** pretraining topology/网络/precision/15.5T与global batch 67M tokens披露；serving hardware、batch/concurrency、TTFT/TPOT与SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在作者mid-scale实验中QK-Clip能抑制attention-logit增长；在K2 full run中作者报告零loss spike，并公开足够系统细节说明optimizer、parallelism、activation和context recipe协同，而非单一算法魔法。
- **What It Does Not Prove:** 不证明MuonClip普遍优于AdamW/其他stable optimizer，不证明零spike由它单独造成；agent benchmark不证明可靠自主性；vendor training efficiency不能外推到不同topology/kernel。
- **Limitations / Threats to Validity:** optimizer full-scale缺controlled baseline；data/RL代码不开放；activation FP8 storage与engine switching的一致性/容错边界未完整披露；agent模型会过度调用tool、产生未完成tool call，one-shot project可能弱于专用agent scaffold；safety judge具主观性。
- **Trade-offs / New Failure Modes:** ultra-sparse MoE降低active FLOPs却放大expert network与weight storage；MuonClip增加QK monitoring/control；activation压缩/offload节省HBM却引入precision与host bandwidth风险；colocation提高utilization却增加mode switch和版本一致性故障。
- **Where the Previous Design Still Applies:** 规模较小、network弱、稳定优先时dense/较小MoE+AdamW更简单；固定chat任务无需复杂agent environment；分离train/rollout clusters在故障隔离更重要时仍合理。
- **Evolution Relationship:** `Direct Evolution`：Muon → consistent scaling → QK-Clip；dense/less-sparse scaling → ultra-sparse MoE+MLA；SFT tool use → environment-grounded agent RL。三条链是layering，不是单一替代。
- **ROADMAP Node:** Ch21、Ch24、Ch29、Ch31～34、Ch45、Ch74～77。
- **Target and Adjacent Chapters Read:** 已阅读 Ch20～24、Ch28～35、Ch44～46、Ch73～77；需要在 Books Gate检查Ch21/32能否吸收“optimizer-control与topology协同”而不把K2写成产品案例堆叠。
- **Existing Coverage:** Ch21已有MoE routing/All-to-All；Ch32～34已有communication/PP；Ch29已有group-relative RL；长期新增点可能是optimizer数值control、activation storage precision与并行拓扑的共同稳定contract。
- **Integration Decision:** `No Change — Already Covered`；MoE、Muon、agentic post-training 与 serving contract 已在 Ch21/24/29/52/77 分层覆盖。
- **Changed Files or Rejection Reason:** 不改 Books；报告提供同族 evidence，但未改变这些章节的设计结论。
- **Open Questions:** v1-v2 exact diff、1T controlled optimizer baseline、checkpoint/recovery语义、engine switching protocol、agent data provenance与independent reproduction。

### Graph-R1

- **Candidate / Week / Score / Source Family:** Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning / 2025-W31 / 26/30 / `ARXIV-2507.21892`。v1于2025-07-29 15:01:26 UTC公开；v2 2026-06-02及ICML 2026材料只作forward revision。已核验v1全文和作者repository，但paper未pin event-time commit，current main不能冒充事件时快照。
- **Full-read Coverage:** 已读Abstract/Introduction/Related Work/Preliminaries、完整Method/公式/Algorithm、construction/retrieval/generation/OOD analyses、prompts、理论主张、datasets/baselines/evaluation/implementation/limitations appendices，并检查graph-build、retrieval-server、training script与dependencies。
- **Original Problem / Previous Design / Changed Constraint:** static chunk RAG状态和授权边界最简单；one-shot GraphRAG把关系预编译进graph，确定性retriever可直接读取；SFT适合固定query/tool format。多跳问题却可能根据新证据继续生成query并决定停止，graph representation、retrieval path与answer outcome需要在trajectory中协同，同时不能把外部retriever、policy token和final correctness混成同一状态。
- **Mechanism / Reward Boundary:** offline用GPT-4o-mini抽取n-ary relations构建hypergraph，以shared encoder建立entity/hyperedge index；online policy输出`<think>`后选择`<query>`或`<answer>`，query触发entity-to-hyperedge和direct-hyperedge retrieval，再以RRF融合Top-k并追加observation。GRPO对多轮trajectory做group-relative update。但v1实际reward只是`-1 + capped format reward + answer token-F1`，并未显式实现摘要/引言声称的retrieval relevance和path reliability；“end-to-end”仅指terminal outcome反传到interaction policy，不代表extractor/index/retriever共同训练。
- **State / Data and Control Flow:** corpus owner拥有authoritative text；extractor/index publisher拥有graph snapshot、schema、entity/hyperedge identity；retrieval service拥有encoder/top-k/fusion；agent policy拥有query/continue/stop/answer tokens；environment拥有trajectory observation；reward service拥有format/F1 semantics；trainer拥有old/current/reference policy与KL。corpus → extract/embed/index；question → reflection/query → dual retrieval/fusion → knowledge observation → repeat/answer；group trajectories → format/F1 reward → group advantage → GRPO update。ACL、freshness、delete和provenance owner未定义。
- **Implementation / Artifact Drift:** paper使用GPT-4o-mini、bge-large-en-v1.5、Qwen2.5 1.5B/3B/7B、4×A100 80GB、batch 128、max length 4096、top-5、GRPO 3 epochs；当前repo README称4×48GB，脚本使用Ray+VERL/vLLM、TP4、repeat5、KL0.001且total_epochs=1。由于没有event-time commit，这些差异保持artifact drift。dataset/hypergraph经TeraBox下载且没有immutable hash。
- **Evaluation Contract:** 六个QA datasets各取5,120 train和128 test；指标为EM、token F1、retrieval semantic similarity与GPT-4o-mini七维judge。作者表中Qwen2.5-7B Graph-R1平均F1 57.82，正文误写57.28；2Wiki cost表的CP1MT=$2.81却被正文称作per 1K tokens，local generation `$0`也只表示无外部API费，不是零GPU成本。precision、seed、variance/CI、API snapshot、concurrency、TTFT/TPOT、energy和failure recovery均未披露。
- **Evidence / Theory Dispute:** 作者harness支持multi-turn graph environment与combined method优于列示baselines，但w/o-RL等消融同时改变protocol-following能力，不能把全部gap因果归于RL。v1 Propositions 1–3将graph较高information density和adaptive rounds较高information gain写进假设，并把Fano inequality用于错误方向；因此理论优越性为`Disputed claim within Experimental source`，不能作为定理证据。
- **What It Proves / Does Not Prove:** 证明一个trainable query/stop/answer policy可使用hypergraph retrieval environment，并在作者六个sampled QA sets中有经验收益；不证明GraphRAG普遍胜过chunk RAG、GRPO普遍胜过其他RL、citation faithfulness、hallucination prevention、production cost/latency优势、robust OOD、安全授权或exact reproducibility。
- **Trade-offs / Previous Design / Evolution:** hypergraph增加relation inductive bias，也引入provenance、entity resolution、schema drift、rebuild/delete/ACL propagation和index cost；multi-turn retrieval增加tool latency、token cost、loop/premature stop、terminal credit ambiguity与攻击面；format reward可能只奖励协议合规。小而频繁更新、严格授权、低延迟或single-hop corpus仍适合static chunk/hybrid RAG；稳定graph和确定遍历仍适合one-shot GraphRAG。演进为static chunk → one-shot graph → multi-turn graph environment → outcome-trained query/retrieve/stop/answer policy → future typed credit/provenance/safe stopping。
- **Owner / Adjacent / Decision:** canonical owner `AGENT-RAG` / Ch76 / legacy Ch72，training handoff `TRAIN-GRPO` / Ch33 / legacy Ch29；已读Ch75～77与Ch33。现有章节已覆盖typed retrieval、Agentic Retrieval、joint query/compression/stopping、group reward与terminal-credit ambiguity，所以最终为`Emerging / Experimental — No Change Candidate`；claim-level theory保持Disputed，Historical Books Gate关闭。开放问题包括v1 commit/hash、reward mismatch、Fano修正、independent replication、ACL/delete、citation faithfulness与真实TCO。

### Optimal Scheduling Algorithms for LLM Inference / SLAI

- **Candidate / Week / Score / Source Family:** Optimal Scheduling Algorithms for LLM Inference: Theory and Practice / 2025-W31 / 27/30 / `ARXIV-2508.01002`。v1于2025-08-01 18:12:21 UTC公开；v2 2025-12-01只作forward revision。论文称SLAI基于Sarathi-Serve/vLLM，但没有公开code/data/commit/reproduction artifact。
- **Full-read Coverage:** 已读metadata、Background/Related Work、batch-cost model、RAD algorithm与证明、SLAI mechanism、implementation/evaluation、scheduler mapping、sensitivity、影响结论的Appendix和Conclusion。论文没有独立Limitations章，威胁由假设与实验边界提取。
- **Original Problem / Previous Design / Changed Constraint:** decode-priority保护TBT但利用率低；prefill-priority改善吞吐/TTFT却阻塞decode；Sarathi token-budget chunking是合理折中；PD分离相位但可能静态失衡并承担KV transfer。新约束要求同时优化throughput、TTFT、tail TBT、memory与tier-specific SLO，并面对随机arrival和未知输出长度。
- **Mechanism / Theory Boundary:** 将请求建模为prefill/decode iterations，并把GeMM tiling、per-request decode-attention GeMV和staircase cost纳入batch model。RAD按tile LCM组织prefill与decode，在identical nodes/same model、stationary Poisson、bounded i.i.d. lengths、non-preemptive iterations和已知tile parameters等假设下给出throughput-optimal characterization；这不是生产环境的通用最优定理。SLAI追踪decode TBT deadline，只在time-critical时加入decode，把slack让给prefill；SPF、memory-feedback offset与active/decode caps共同控制队列和KV压力。
- **State / Control Flow:** admission拥有accepted set和memory margin；scheduler拥有token budget、queues、deadline/criticality、caps；profiler拥有batch-time/tile/memory estimate及freshness；KV manager拥有residency/eviction/recompute；request policy拥有tenant/TBT class。arrival + prompt length + tier SLO → waiting prefill → 选择chunks并保留critical decode → execute → 采集time/memory → 更新criticality/offset/caps → completion释放KV；cluster routing不能与单节点SLAI state混为一谈。
- **Implementation / Evaluation Contract:** Python SLAI构建在Sarathi-Serve/vLLM上，但exact commit、dependency、patch、tests与profiler calibration未披露。实验为Mistral-7B、单NVIDIA RTX ADA 6000、OpenChat ShareGPT4并把每个conversation round视为独立request；基于数据长度合成Poisson arrival，total length≤8192。主实验paying=5%，TBT SLO 0.1s/0.5s，token budget 512，active/decode caps 128，offset 10或memory<96%时5。precision、GPU memory variant、软件栈、重复次数/CI、power/cost均未披露。
- **Evidence / Sensitivity:** 对Sarathi FCFS/SPF和vLLM，作者报告high-load median TTFT 1.5→0.7s；另一个满足median TTFT≤0.5s且TBT目标的crossing point从1.15→1.45 req/s，二者不能合并成同一条件的收益。已有FCFS/SPF、fixed/dynamic offset、tier ratio、prompt length和prefill-priority sensitivity；缺cross-model/hardware、burst/drift、prediction error、fairness/starvation、distributed/PD与prefix/speculation实验。
- **What It Proves / Does Not Prove:** 证明明确假设中的RAD理论结果，以及作者单GPU workload中deadline slack+SPF+memory feedback改善列示baseline的TTFT/TBT trade-off；不证明SLAI universal optimality、production generalization、公平性、multi-tenant isolation、burst robustness或distributed benefit。
- **Trade-offs / Previous Design Boundary / Evolution:** slack deferral可能逼近deadline或饥饿；SPF牺牲长prompt；stale telemetry会使threshold control抖动；tile identity随hardware/kernel变化失效。低负载可继续FCFS/vLLM；统一严格TBT可继续Sarathi保守策略；phase稳定且transfer便宜时PD仍合理。演进为fixed batching → iteration admission → token-budget chunked prefill → deadline/slack-aware mixed scheduling → memory-feedback control → calibrated goodput/fairness。
- **Owner / Adjacent / Decision:** canonical owner `INFER-SCHEDULING` / Ch56 / legacy Ch52；已读Ch46 Continuous Batching、Ch55 PD Disaggregation与Ch56。Ch56已有TTFT/TPOT/fairness/SLO admission与goodput，新增点是区分“假设模型内theorem”与“经验SLO policy”，并显式纳入deadline slack和memory feedback。`Emerging / Experimental — Refine Candidate`；Historical Books Gate关闭，本轮不改Books。开放问题包括artifact、fairness/starvation、hysteresis稳定性、burst/drift、tail TTFT与distributed扩展。

### DICE：demonstration set是随Agent observation更新的working state

- **Candidate / Week / Score / Source Family:** DICE: Dynamic In-Context Example Selection in LLM Agents via Efficient Knowledge Transfer / 2025-W31 / 24/30 / `ARXIV-2507.23554`。arXiv v1于2025-07-31 13:42:14 UTC公开且无后续revision。已读metadata、Abstract、Introduction、Related Work、完整Method/公式/理论主张、全部Experiments、ablation、analysis、cases、Conclusion与Limitations；论文多次指向Appendix，但13页v1 PDF以References结束，实际没有Appendix，也未找到官方code/data artifact。
- **Original Problem / Previous Design / Changed Constraint:** 固定few-shot prompt在短任务、稳定state下确定、可审计且cache-friendly；task-level kNN也足以处理粗粒度相似性。但ReAct/Reflexion/LATS多步执行中history随observation变化，最有用的成功轨迹可能逐step切换，完整静态demo会占用context并诱发spurious imitation。
- **Mechanism / State Ownership:** demo pool保存完整成功轨迹；每个step在action/observation更新history后重选top-M。Gemma-2-2b-it分别从候选demo抽取`TK_d`、从当前history抽取`TK_t`作为未观测action proxy，用cosine/InfoNCE式分母排序，再把选中的完整demo注入base Agent prompt。curator应拥有trajectory/verifier/tool-env-model version与ACL/expiry，extractor拥有prompt/checkpoint/decoding与summary provenance，selector拥有pool/query/score/top-M/fallback，assembler拥有replacement/order/token budget，environment拥有authoritative outcome；论文未定义stale/poison/delete/tenant owner。
- **Control / Data Flow / Implementation:** offline successful trajectories→verify/filter→pool→extract/cache demo knowledge；每step task+history→Gemma抽当前knowledge→与pool比较→选择demo→组prompt→GPT-3.5-turbo Agent→environment observation→下一step。所谓training-free只表示不更新参数，仍增加Gemma call、检索、prompt重组与prefill。repo/artifact、base model exact snapshot、pool size/seed/verifier、prompt、trajectory count/length与跨framework pooling均`Not Disclosed`。
- **Evaluation / Baselines / Ablations:** HotpotQA 500 subset、ALFWorld 134 unseen tasks、WebShop 500 test tasks上，DICE分别叠加ReAct、Reflexion与LATS；与random/KATE/EPR及taskwise DICE比较。stepwise DICE在作者复现中优于taskwise/static selector，例如ReAct Hotpot EM 32.1→41.4、ALFWorld SR 57.5→67.9、WebShop SR 28.0→35.0。论文还报告3 demos接近random ICL 6的图示，但无完整cost、variance或latency表。seeds、CI、significance、temperature、hardware、batch/concurrency、token cost与SLO未披露。
- **What It Proves / Does Not Prove:** 在三个受控benchmark和作者协议内，基于summary similarity的stepwise selection优于列示static/taskwise selectors，说明demo working set可随observation更新。它不证明`TK`具有causal identity、跨模型/领域普适、零额外成本、生产安全或完整demo优于TK-only，也没有隔离收益来自知识转移理论还是普通semantic retrieval。
- **Formal Claim Disputes:** 固定LLM capacity不使`I(d;TK_d)`对demo恒定；summary cosine不是无需分布、critic与temperature定义的MI estimator；文中的MI等式与stochastic channel需要额外条件；generalization bound不能直接推出Agent reward，更紧upper bound也不等于真实loss更小。因此经验机制保留Experimental，形式性能保证与causal interpretation单独标记`Disputed`。
- **Limitations / Trade-offs / Failure Modes:** 每step额外LLM与打分成本；successful-only产生survivorship bias并继承verifier错误；full demo可能泄漏stale tool ID和无关action；stepwise replacement破坏prompt/cache identity、KV reuse、position/order与行为稳定；summary会hallucinate或遗漏，pool scan随N增长。静态curated demo仍适合确定性、安全关键、短任务和强cache；state变化小可用taskwise kNN；pool陈旧、私有或poisoned时no-demo/direct policy更合理。
- **Evolution / Owner / Existing Coverage / Decision:** `static curated demos → task-level retrieval → stepwise state-conditioned demo working set → provenance/validity-aware selection → calibrated utility/cost-aware selector`。canonical owner为`AGENT-CONTEXT` / Ch75 / legacy Ch71；已读Ch74 Prompt、Ch75 Context，并复核Ch77 Memory、Ch79 Planning和Ch80 Reflection。Ch75已覆盖runtime context assembly、token budget与source-linked demonstration；未来仅可能`Refine — Existing Argument`，跨任务持久化才handoff Ch77。`Full Source Review Complete — Emerging / Experimental / Formal Claims Disputed`；Historical Books Gate关闭，本轮不改Books。
- **Open Questions:** official code与缺失Appendix、pool hash/size/split/verifier、Gemma prompt/schema/decoding、top-M/order、cache/latency、full-demo vs TK-only ablation、cross-model、variance、stale/poison/ACL/delete与fallback。

### Graph-Augmented Large Language Model Agents：同名Graph不等于同一类状态

- **Candidate / Week / Score / Source Family:** Graph-Augmented Large Language Model Agents: Current Progress and Future Prospects / 2025-W31 / 21/30 / `ARXIV-2507.21407-GRAPH-AUGMENTED-LLM-AGENTS-SURVEY`。v1于2025-07-29 00:27 UTC公开，v2 2025-08-30只作forward revision。已读v1全文、7 figures、references与companion repository；论文没有Method/Evaluation/Ablation/Appendix/Limitations，这是survey证据类型边界，不是阅读缺口。repo仅为分类paper/link list，无统一实现、数据或可复算结果。
- **Problem / Previous Design / Changed Constraint:** linear plan、flat memory top-k、tool list和fixed topology在短任务、关系稀疏、工具少或side effect强时状态少、易审计；当subtask依赖、跨episode evidence、tool compatibility与multi-agent communication edge增长，关系本身开始成为versioned state。Graph只有在edge语义和更新机制可验证时才成立，否则只是持久化错误关系。
- **Taxonomy / State Ownership:** survey归纳planning graph、interaction/knowledge memory graph、tool dependency graph、static→task-dynamic→process-dynamic MAS topology、communication pruning与threat propagation。它们是被引工作的taxonomy，不是survey验证的新机制。本项目必须分开Planner的dependency graph、Memory的fact/provenance graph、Tool Registry的authorized compatibility graph、Workflow的template/realized execution graph、Multi-Agent runtime的communication topology及Security/Evaluation evidence graph；LLM只能proposal node/edge，owner验证schema、authority、freshness后commit。
- **Implementation / Evaluation Boundary:** `Not Applicable — Survey`。无共同schema、update algorithm、loss、complexity、hardware、runtime、systematic search query、inclusion/exclusion、quality grading、normalized workload或survey-level experiment。文中“improves reliability/efficiency”必须回到各primary family，不能引用survey headline进入Books。
- **Evidence / Limits:** survey支持graph被用于多类Agent object的taxonomy事实，也揭示同一“graph”可指fact index、plan、workflow或communication topology。它不证明graph普遍减少hallucination、动态图优于静态workflow、GNN开销minimal或统一full-stack graph可行。MAS多轮退化与GNN oversmoothing仅为`Explanatory Analogy`，不是数学等价或直接演进。缺系统检索协议使coverage/exhaustiveness不可复算。
- **Trade-offs / Previous Boundary / Evolution:** Graph提供dependency、reachability、parallelism与传播审计，也新增schema、edge hallucination、stale topology、mutation race、rollback、ACL/delete propagation和sparsification误删。短顺序任务保留linear plan，局部高QPS facts保留flat retrieval，小toolset保留typed allowlist，高审计场景保留fixed topology。演进是多条平行分支：typed plan DAG、versioned support graph、authorized toolchain graph与bounded topology mutation，跨分支只是`Principle Reuse`。
- **Owner / Existing Coverage / Decision:** taxonomy归档owner为`AGENT-PLATFORM` / Ch84 / legacy Ch80；已读Ch77 Memory、Ch78 Tool、Ch79 Planning、Ch81 Workflow与Ch82 Multi-Agent。现有Books已更严格覆盖edge非真值、provenance/delete、tool authorization、template/realized graph、single-agent headroom、coordination tax与bounded repair，故`No Change — Already Covered / Weekly Only — Secondary Taxonomy and Source Map`。Historical Books Gate关闭，本轮不改Books。
- **Open Questions:** v1检索cutoff/纳入标准、companion event-time commit、各graph schema/update/delete/ACL cost、compute-matched single-agent baseline、threat graph error及如何避免统一graph造成authority coupling。

### Geometric-Mean Policy Optimization（GMPO）

- **Identity / sources / coverage:** `ARXIV-2507.20673`，v1 2025-07-28，26/30；阅读全文的背景、objective/gradient derivation、log-space algorithm、实验、clip/token-vs-sequence ablation、MoE/normalization appendices，并检查官方 `callsys/GMPO`。v2/v3 后续修订只作 lineage。
- **Problem / previous / changed constraint / mechanism:** GRPO 的算术平均和 token importance ratio 在 outlier 下会放大更新，但窄 clipping 又抑制 exploration；GMPO 用 sequence 内 importance ratios 的 geometric mean 统一加权 token policy gradients，并在 log space 实现、使用更宽的 token-level clipping。old/current/reference policy、rollout group、reward/advantage 与 optimizer state 仍由 trainer 拥有，算法只改 loss aggregation，不改变 verifier 正确性。
- **Evaluation / evidence boundary:** Qwen2.5-Math 1.5B/7B、DeepSeek-R1-Distill-Qwen-7B、Qwen3-32B MoE 与 Qwen2.5-VL-7B，数学及 Geometry3K；作者报告相对 GRPO 的 Pass@1、KL、entropy、ratio range，并做 clipping 与 component ablation。hardware、global batch、rollout concurrency、wall-clock/communication overhead、production SLO 未完整披露；较窄 objective range 不等于普遍较小 estimator variance，作者实验也不能证明所有 verifier/task 下稳定。
- **Trade-off / owner / disposition:** geometric averaging抑制单token outlier却把sequence内token更新耦合，可能弱化稀有关键token并增加log-space/zero handling；数据、reward或policy drift才是主因时旧GRPO+监控仍合理。owner `TRAIN-GRPO` Ch33，handoff Ch34/36；`Emerging / Experimental — Refine Candidate`，Historical Books Gate关闭。

### Reinforcement Learning from Self-Feedback（RLSF）

- **Identity / sources / coverage:** `ARXIV-2507.21931`，v1 2025-07-29，25/30；全文覆盖 confidence definition、CoT candidate generation、reward model、DPO/PPO、MultiArith/GSM8K/MMLU/RewardBench、ECE、bias、training configs、gamma sensitivity、limitations 与 ethics。无可核 event-time training artifact。
- **Problem / mechanism / ownership:** 外部偏好昂贵且 RLHF 后模型常失校准；RLSF 从 frozen policy 每题生成 `K=10` traces，以 final-answer token confidence 排序成 synthetic preferences，再训练 LoRA reward model并用 PPO/DPO更新policy。generator snapshot、confidence extractor、preference dataset、reward model与policy版本必须分离；“模型自信”是训练信号，不是部署时事实置信度。
- **Evaluation / evidence boundary:** Gemma-2-2B 与 Qwen2.5/DeepSeek-R1-distill-7B，比较 CoT、URM-RLHF、DPO/PPO，并报告 accuracy/ECE；结果随模型和任务不一致，DPO弱于PPO，RewardBench accuracy也显著低于监督URM/QRM。未证明自信与真实正确性在开放域、长回答或分布外保持校准，也没有外部 evidence verifier。
- **Trade-off / owner / disposition:** 无人标注降低成本，却可能把已有错置信、sampling bias与reward hacking反馈回policy；有可靠gold/verifier时外部reward仍更安全。canonical owner `TRAIN-RLHF` Ch31，handoff `PLATFORM-EVALUATION-SYSTEM` Ch66；`Emerging / Experimental — No Change Candidate`。

### AutoTIR

- **Identity / sources / coverage:** `ARXIV-2507.21836`，v1 2025-07-29，25/30；阅读全文 Method/reward equations、training mix、tool environment、10 benchmark、baselines、ablation、tool-selection/productivity metrics、appendix，并检查 `weiyifan1023/AutoTIR`。
- **Problem / mechanism / control flow:** fixed tool-use traces在需要工具的任务有效，却会在一般指令上过度调用并损伤 instruction following。AutoTIR以 Qwen2.5-7B-Instruct 做 GRPO，混合 retrieval、code、无需tool即可回答与general instruction data；answer/format/action rewards共同学习 `no tool / retrieval / code` 选择。policy只能proposal tool action，environment/executor仍拥有权限、timeout、结果与side effect commit。
- **Evaluation / boundary:** HotpotQA/2Wiki/MuSiQue/Bamboogle、AIME/MATH/GSM8K、LogiQA/IFEval，比较 text-only、code-only与retrieval methods，并报告 EM/accuracy/soft-accuracy、tool selection与productivity。训练数据与测试族相近，hardware、latency、sandbox cost、并发、真实API failure/SLO不完整；不能从benchmark选择准确率推出production authorization或通用工具自主性。
- **Trade-off / owner / disposition:** learned routing减少冗余调用但新增reward权重、tool identity、sandbox与拒绝/超时failure；静态allowlist和deterministic workflow在高风险任务仍优先。owner `AGENT-TOOL-CALLING` Ch78，handoff `TRAIN-GRPO` Ch33；`Emerging / Experimental — Refine Candidate`。

### Multi-Agent-as-Judge / MAJ-Eval

- **Identity / sources / coverage:** `ARXIV-2507.21028`，v1 2025-07-28，23/30；全文覆盖 stakeholder-document extraction、persona construction、independent score/debate/aggregation、两域人类评测、baselines/ablations、correlation/variance、prompts与limitations。代码与原始人类标注快照不足以完全复算。
- **Problem / mechanism / ownership:** 单一LLM judge把多维人类偏好压成一个隐式rubric；MAJ-Eval从domain documents抽取stakeholder personas，各judge先独立评分，再由moderator debate和aggregator合成。rubric/annotator population/document snapshot应由evaluation owner管理；judge agents不能自行成为ground truth，debate transcript也不是独立证据。
- **Evaluation / boundary:** children QAG 与 medical multi-document summary，比较 ROUGE/BERTScore/G-Eval/ChatEval，并以human ratings的相关性衡量。两域样本、model snapshot与prompt choice限制外推；多个同源LLM不是独立审稿人，debate可能放大共同偏差，未披露cost/latency/concurrency/SLO。
- **Trade-off / owner / disposition:** 多persona显式化rubric但引入角色生成、相关误差、moderator权力与不可重复性；高风险release仍需human adjudication。owner `PLATFORM-EVALUATION-SYSTEM` Ch66，handoff `AGENT-MULTI-AGENT` Ch82；`Emerging / Experimental — No Change Candidate`。

### MemTool

- **Identity / sources / coverage:** `ARXIV-2507.21428`，sole v1 2025-07-29，26/30；阅读全文 autonomous/workflow/hybrid algorithms、ScaleMCP dataset、100-turn protocol、13+ model tables、prompts、mode analyses和appendices。未找到immutable code/data release。
- **Problem / mechanism / state:** dynamic tool retrieval只会“加工具”时，multi-turn session会耗尽128/512 tool schema limit并污染context。MemTool把 active tool set 作为session working state：autonomous mode让model调用 Search/Remove；workflow mode用两个fresh LLM calls先prune再retrieve；hybrid固定prune、允许model add/use。registry拥有authoritative schema/ACL，session manager拥有active-set/version，model只提议mutation，executor拥有action commit。
- **Evaluation / boundary:** ScaleMCP 5,000 servers、top-k=5、100 consecutive interactions，比较 removal ratio与task completion；reasoning models autonomous removal约90–94%，较小模型差异大。工具是描述级模拟，未覆盖真实auth/side effect/schema drift/tenant隔离；API price、token/prefill/cache、latency/concurrency/SLO未统一，不能把高removal等同安全或质量。
- **Trade-off / owner / disposition:** dynamic active set节省context却破坏prompt/KV identity，错误remove会失能、错误add会扩大攻击面；小固定toolset仍用静态allowlist。owner `AGENT-CONTEXT` Ch75，handoff Ch78/83；`Refine — Existing Argument Candidate`。

### Persona Vectors

- **Identity / sources / coverage:** `ARXIV-2507.21509`，v1 2025-07-29，27/30；以v1结论为事件边界，阅读全文 automated direction extraction、deployment monitoring、fine-tune prediction/steering/data filtering、cross-trait/real-world data/SAE appendices，并检查官方 `safety-research/persona_vectors`。v2/v3扩展不倒灌。
- **Problem / mechanism / state:** prompt或fine-tune可引发sycophancy、evil/hallucination-like behavior shift，black-box eval常在行为已改变后才发现。方法用trait-positive/negative prompts生成activation差得到layer direction，监控projection shift，并通过activation steering或training-time regularization抑制变化，也用data projection差预测危险数据。direction/version、layer/hook、base model与calibration set必须共同身份化。
- **Evaluation / boundary:** 多traits、多model/fine-tune datasets、layer selection、prompt intervention、CAFT与filtering对照；相关性和steering提供受控causal evidence，但linear direction不是persona本体，hallucination trait projection不是事实核验器。硬件/serving overhead、false-positive operating point、OOD/long-context/attack robustness与production SLO不足。
- **Trade-off / owner / disposition:** 监控比纯output eval更早，却可能压制有用behavior、被context/quantization/kernel漂移破坏并提供新的steering攻击面；release gate仍需behavior/evidence evaluation。owner `PLATFORM-EVALUATION-SYSTEM` Ch66，handoff Ch72 Security；`Emerging / Experimental — Refine Candidate`。

### TriangleMix：decoding-time contribution sparsity

- **Identity / sources / coverage:** `ARXIV-2507.21526`，v1 2025-07-29，27/30；阅读全文 gradient probing、triangle mask/layer selection、kernel、RULER/LongBench/GSM-Infinite、dynamic-sparsity组合、accuracy/latency/ablation与appendix；官方artifact可访问但event-time commit未固定。
- **Problem / mechanism / data flow:** full prefill attention保留所有causal Q-K，dynamic sparse attention又要在线估计blocks。论文用ground-truth next-token logit对attention score的gradient分析“哪些prompt-prompt attention真正影响decode”，发现部分层middle Q-K只影响中间prompt token；于是部分层用静态triangle mask，其他层dense，并与dynamic methods叠加。mask/kernel/model-layer mapping属于execution plan，不能脱离model/version复用。
- **Evaluation / boundary:** Llama-3.1-8B、Llama-3-8B-262K、Qwen2.5-7B，最长128K；作者报告triangle attention kernel 15.3×与相对dynamic method再降TTFT 6–19%。这不是端到端模型吞吐；GPU/kernel/precision/batch/concurrency、absolute TTFT/TPOT与SLO必须绑定表格条件，gradient以chosen target token probing也不证明任意generation无损。
- **Trade-off / owner / disposition:** static mask省index estimation但可能在task/model/revision漂移后漏掉关键依赖；short prompt/full accuracy优先时dense仍合理。owner `INFER-PREFILL` Ch43，handoff `INFER-TENSORRT-LLM` Ch49；`Emerging / Experimental — Refine Candidate`。

### Falcon-H1 technical report

- **Identity / sources / coverage:** `ARXIV-2507.22448`，v1 2025-07-30，29/30；阅读全文 parallel attention+Mamba-2 architecture、channel/SSM/RoPE/width-depth/tokenizer ablations、data/training dynamics、effective LR/weight decay、muP、batch/warmup、DP/mixer/CP infrastructure、post-training、efficiency与appendices；检查官方weights/repository。当前v2内容不可倒灌。
- **Problem / mechanism / state:** pure attention长序列二次成本高，pure recurrent/SSM又弱化精确content access。Falcon-H1让attention与Mamba-2并行读同一normalized residual，concat后projection，再串行MLP；proxy sweep选择少量attention、大量SSM/MLP。训练又把parameter norm纳入effective LR/weight-decay分析并用可调muP multiplier迁移scale。SSM recurrent state与attention KV是两种typed decode state，runtime不能都称KV cache。
- **Evaluation / boundary:** 0.5B～34B、16K～256K、2.5T～18T tokens，多语言/long-context/efficiency与proxy ablations。作者benchmark和吞吐表支持其公开配置，不证明混合架构普遍胜attention；不同data/tokenizer/training budget使cross-family参数效率非controlled architecture ablation。precision、batch/concurrency、serving SLO需按具体表，不把“half size”写成通用成本。
- **Trade-off / owner / disposition:** hybrid降低部分attention成本，却增加state lifecycle、kernel/backend、parallelism与checkpoint compatibility；短context、成熟kernel或random-access质量优先仍可pure attention。owner `MODEL-SELF-ATTENTION` Ch14，handoff `INFER-KV-CACHE` 与 distributed training；`Refine — Existing Argument Candidate`。

### GEAK Triton Kernel Agent and Benchmarks

- **Identity / sources / coverage:** `ARXIV-2507.23194`，v1 2025-07-31，29/30；阅读全文 benchmark repair、30 ROCm kernels、generation/evaluation/reflection/optimization loop、test/performance harness、model/iteration ablations与kernel case appendix，并检查 AMD official GEAK agent/eval repositories。
- **Problem / mechanism / control:** general code generation不保证GPU kernel correctness或performance；GEAK让generator产Triton code，execution evaluator在isolated harness检查compile/correctness/runtime，reflection读error/profile，再迭代优化。benchmark固定task/reference/tests/hardware；executor拥有timeout/resource isolation，performance result只有在correctness通过后commit，LLM不能自报speedup。
- **Evaluation / boundary:** 184 repaired TritonBench kernels+30 ROCm kernels，AMD MI300X，frontier models/direct prompting与agent iterations；作者报告correct rate最高54.89%/63.33%及reference-relative speedup，但aggregate speedup会受失败过滤、reference质量、warmup/measurement protocol影响。不能外推CUDA/NVIDIA、其他Triton版本或production shapes；token cost、parallel attempts、wall-clock/concurrency/SLO需独立记账。
- **Trade-off / owner / disposition:** executable feedback真正有用，但扩大compile/run attack面、benchmark overfit与test blind spot；人工kernel仍适合高风险hot path。owner `INFER-TENSORRT-LLM` Ch49（通用 execution-plan / kernel owner），handoff `PLATFORM-EVALUATION-SYSTEM` Ch66与Agent workflow；`Refine — Existing Argument Candidate`。

### TTS-1 Technical Report

- **Identity / sources / coverage:** `ARXIV-2507.21138`，v1 2025-07-28，25/30；阅读全文codec/SpeechLM、约1M小时pretrain+200K小时SFT、GRPO composite rewards、audio markup/LoRA、streaming、benchmark、infrastructure与appendices，并检查open-source code。后续revision不改变first-public。
- **Problem / mechanism / state:** 16/24kHz codec或非流式生成难同时满足48kHz质量、style/speaker identity与实时拼接。TTS-1用单65536-codebook、50 tokens/s，super-resolution decoder升到48kHz；LLaMA SpeechLM自回归audio tokens；conditional WER/SIM/DNSMOS rewards做GRPO，same-speaker neutral/stylized pairs教markup；streaming用context-aware chunk与unvoiced-boundary concat。audio/token timestamp、speaker/reference consent和stream commit是独立state。
- **Evaluation / boundary:** 1.6B/8.8B，11 languages；RL每prompt 8 responses、1,000h subset，markup LoRA 8 GPUs/2048 length；训练约32 H100两月、16 A100三月。人类preference、WER/SIM/DNSMOS与streaming结果是作者条件内证据，未证明情感/身份安全、跨语言一致、production concurrency/TTFT/jitter/SLO。
- **Trade-off / owner / disposition:** compact codec利于streaming/storage却纠缠semantic/acoustic；composite reward会metric gaming；chunk拼接降低latency但可能边界artifact。owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24，handoff serving/evaluation/security；`Emerging / Experimental — Refine Candidate`。

### Compressed History States for Web Agent Automation

- **Identity / sources / coverage:** `ARXIV-2507.21369`，v1 2025-07-29，25/30；阅读全文 state-compression variants、web-agent loop、task suites、token/latency/success comparisons、ablations、error cases与limitations；artifact和event-time browser snapshot不足。
- **Problem / mechanism / state:** append-all browser history最可审计但prompt线性增长，截断又丢失前因。方法将prior observation/action/history压成compact state再进入下一step，比较保留recent、summary与structured variants。raw trace应由workflow/evidence store永久拥有，compressed state是可重建的derived context，必须带source range、compressor/version和supersession，不能覆盖事实日志。
- **Evaluation / boundary:** 受控web tasks和指定model/harness下比较success、token与latency；browser/site drift、login/auth、side effect、concurrency与recovery限制外推。摘要token下降不证明任务信息完整，也不证明对不可逆action安全。
- **Trade-off / owner / disposition:** compression降低prefill和distraction却引入遗漏、summary hallucination、stale selector与debug不可见；短任务仍用full history，高审计流程保留raw trace。owner `AGENT-CONTEXT` Ch75，handoff `AGENT-WORKFLOW` Ch81；`Emerging / Experimental — Refine Candidate`。

### Self-Evolving Agents survey

- **Identity / sources / coverage:** `ARXIV-2507.21046`，v1 2025-07-28、v2 7-30、v3 8-01，23/30；以v1为owner，阅读全文 what/when/how/where taxonomy、memory/tool/model/workflow evolution、feedback sources、benchmarks、risks/future directions与references。survey无统一artifact、controlled experiment或systematic-search completeness proof。
- **Mechanism / evidence boundary:** 它将evolution对象分为model、memory、tool与architecture/workflow，并按self-reflection、environment/human/multi-agent feedback组织更新；这是source map，不证明在线自修改安全或性能。系统上必须把proposal、sandbox evaluation、approval、versioned commit、canary与rollback分开，尤其不能让同一agent同时生成修改和最终验收。
- **Trade-off / owner / disposition:** continuous adaptation响应drift，却引入self-confirmation、memory poisoning、tool privilege growth、benchmark overfit与不可复现；stable workload继续offline release。owner `AGENT-PLATFORM` Ch84，handoff evaluation/security/workflow；`Weekly Only — Secondary Taxonomy / No Change`。

### G-Core RLHF Trainer

- **Identity / source recovery / coverage:** `ARXIV-2507.22789`，v1 2025-07-30，v2 2025-07-31撤回并注明“submission was not approved by the company”，26/30。arXiv正文不可下载，但ResearchGate保留作者署名、CC BY 4.0 的16页v1 full-text mirror；已阅读全文 introduction/background、parallel controllers、dynamic placement、Python/PyTorch implementation、checkpoint/data/balancing、evaluation、conclusion与references。因此不再是material blocker，但发布授权与结论身份保持Disputed。
- **Problem / mechanism / state:** single/hybrid controller在大image/video features、complex control与generative reward下会受CPU/RPC/memory瓶颈；静态placement又跟不上rollout/reward长度随训练变化。G-Core把top-level controller分解为parallel controllers并用collective协调；按role utilization逐步缩减低利用资源、重分配到bottleneck；结合vLLM/SGLang generation、Megatron-Core training、elastic distributed checkpoint、dataloader consumption state与按simulated workload排序。
- **Evaluation / boundary:** 8 machines/64 H20-96GB、NVLink、200Gbps RDMA，CUDA12.4/PyTorch2.5/Megatron-Core0.12/vLLM0.8.5；文中称实验至128 GPUs、production验证>512 GPUs。撤回稿没有完整baseline tables/variance、placement controller stability、failure injection、代码/commit、precision/batch/sequence mix和SLO，因此production claim不能独立核验，也不能把“approaches full utilization”当通用数字。
- **Trade-off / owner / disposition:** parallel controllers缓解单点资源瓶颈却新增distributed control consistency、collective failure与duplicate action；dynamic reallocation可能oscillation、checkpoint loss与online-training抢占；static colocated topology在稳定workload仍更简单。canonical owner `TRAIN-DISTRIBUTED-TRAINING` Ch36，handoff Ch40 Megatron、Ch41 DeepSpeed 与 platform scheduling；`Disputed — Withdrawn Source / Mechanism Evidence Frozen`，不得进入Books，后续若有公司批准的 WeChat-YATT source 只能作为新revision family evidence。

### Watch the Weights

- **Identity / sources / coverage:** `ARXIV-2508.00161`，v1 2025-08-01，26/30；阅读全文 weight-update representation、unsupervised monitoring/control、multiple fine-tune tasks/models/attacks、layer/step/data sensitivity、baselines、appendices和limitations，并检查公开artifact。
- **Problem / mechanism / state:** output eval可能在fine-tune完成后才发现undesired behavior；该方法直接从checkpoint weight deltas提取低维signals，检测并控制异常fine-tuning trajectory。baseline checkpoint、optimizer step、parameter subset、normalizer与detector calibration必须同版本；weight signal不是行为正确性，不能替代held-out eval。
- **Evaluation / boundary:** 多fine-tune datasets和model sizes比较weight-space detector与control，含unsupervised/limited-label settings；结果支持特定更新模式可被早期观察，不证明任意adapter/quantization/distributed optimizer、模型合并或OOD attack下稳定。存储/通信/online overhead、false-positive operating point与release SLO需补。
- **Trade-off / owner / disposition:** 早期weight telemetry可中止坏run，却可能阻断合法domain shift、被adaptive attacker规避并扩大checkpoint隐私面；output/evidence eval仍是release gate。owner `TRAIN-CHECKPOINT` Ch35，handoff `PLATFORM-MONITORING` Ch67与Evaluation；`Emerging / Experimental — Refine Candidate`。

### CoT Mirage / DataAlchemy

- **Identity / dates / sources / full-read coverage:** `ARXIV-2508.01191`，v1 first-public 2025-08-02，24/30；已阅读全文的distribution lens、DataAlchemy合成环境、task/length/format generalization、model-size/temperature studies、theorems/proofs、training details、additional cases与limitations，并检查官方 `ChengshuaiZhao0/DataAlchemy`。后续revision不倒灌事件周。
- **Problem / previous design / changed constraint / mechanism:** CoT在熟悉分布中能分解任务，因此把流畅intermediate steps当作reasoning proxy曾经合理；约束变成task operator、chain length或surface format偏离训练分布后，proxy可能失真。论文从scratch训练小型decoder-only model，在可控ROT/position transformations上分别改变element、operator、composition、length和format，比较answer/reasoning-chain exactness。dataset generator拥有distribution identity，evaluator拥有ground-truth transition；模型输出的CoT不拥有“推理正确”的事实权。
- **Evaluation / evidence boundary:** 基线为无CoT/不同CoT exposure、模型规模与temperature；metrics含exact match、edit distance与BLEU。证据支持该合成环境内CoT对distribution shift脆弱，但不证明production LLM只做memorization，也不证明其泛化bound可直接量化真实pretraining distribution；synthetic alphabet transforms、极小model和未知真实训练data限制外推。
- **Trade-off / owner / disposition:** CoT仍可提供可检查scratchpad与搜索预算，却新增“语言连贯被误当causal trace”的failure mode；有external verifier、tool execution或formal transition时应验证state而非相信叙述。canonical owner `WORLDVIEW-LLM-INTELLIGENCE` Ch8，handoff `PLATFORM-EVALUATION-SYSTEM` Ch66；`Emerging / Controlled Synthetic Evidence — Refine Candidate`。

### Beyond Fixed / DAEDAL

- **Identity / dates / sources / full-read coverage:** `ARXIV-2508.00819`，v1 first-public 2025-08-01，24/30；已阅读全文variable-length denoising problem、initial-length prediction、mask insertion/region expansion algorithm、LLaDA implementation、GSM8K/MATH500/MBPP/HumanEval、fixed-length baselines、component/initial-length ablations与limitations，并检查官方 `Li-Jinsong/DAEDAL`。
- **Problem / previous design / changed constraint / mechanism:** diffusion LM预分配固定generation length便于并行denoising与张量shape规划，但短配额截断复杂答案、长配额浪费compute并可能退化。DAEDAL先用model内部signal估计初始长度，再在denoising中定位不足区域并插入mask tokens扩展。scheduler拥有iteration/length budget，sequence state拥有mask/commit位置，模型只提供扩展信号；动态shape会反向影响batch和cache identity。
- **Evaluation / evidence boundary:** LLaDA-Instruct-8B/LLaDA-1.5-8B，8×A800-80GB、batch 8、官方generation code且不叠加后续cache优化；作者以accuracy/pass@1和effective token ratio比较多组fixed lengths，并做two-stage/initial-length ablation。证据仅覆盖这些DLLM与离线batch，不证明AR模型适用，也未给continuous serving、concurrency、tail latency、rollback或SLO。
- **Trade-off / owner / disposition:** 动态长度减少无效token却引入扩展位置误判、shape divergence、batch fragmentation与termination oscillation；可预测短输出仍适合固定长度。canonical owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24，handoff `INFER-SCHEDULING` Ch56；`Emerging / Experimental — Refine Candidate`。

### SitEmb-v1.5

- **Identity / dates / sources / full-read coverage:** `ARXIV-2508.01959`，v1 first-public 2025-08-03，25/30；已阅读全文situated embedding objective、chunk/context joint encoding、QA与semantic-association data、PlotRetrieval/DetectiveQA/BRIGHT等evaluation、baselines/ablations、training appendix与limitations；artifact/model revision另行身份化。
- **Problem / previous design / changed constraint / mechanism:** chunk-only embedding便于局部evidence retrieval且成本稳定，但长叙事中同一片段的意义依赖前后文；直接扩大chunk又稀释localized evidence。SitEmb把chunk置前、surrounding context置后，利用causal mask在一次forward中得到chunk-only与context-aware pooling，联合contrastive losses训练；document store拥有原文/range，embedding index拥有encoder+context-window version，retriever返回的仍是localized chunk而非整篇摘要。
- **Evaluation / evidence boundary:** SitEmb-v1.5-Qwen3基于Qwen3-Embedding-8B LoRA，8×A800-80GB训练、per-GPU batch 5、每query 1 positive+13 negatives、bf16 A100-40GB evaluation；比较BM25、dense/contextual embedding与long-context baselines。叙事/书籍任务收益不能证明代码、事实库或高drift corpus普遍受益，且index build/storage、update amplification、query concurrency与SLO未闭合。
- **Trade-off / owner / disposition:** contextual embedding改善跨段semantic association，却让同一chunk随document context/version改变identity，增加reindex、stale context与abstract-association false positive；独立短段与高频更新仍适合chunk-only。canonical owner `AGENT-RAG` Ch76，handoff `AGENT-CONTEXT` Ch75；`Refine — Existing Argument Candidate`。

### LiveMCPBench

- **Identity / dates / sources / full-read coverage:** `ARXIV-2508.01780`，v1 first-public 2025-08-03，26/30；已阅读全文95 tasks、LiveMCPTool 70 servers/527 tools、route/execute/respond agent loop、LiveMCPEval、10-model evaluation、retrieval configuration、human agreement/error cases、prompts和limitations；动态server snapshot与credentials不能完全复现。
- **Problem / previous design / changed constraint / mechanism:** 单server少工具benchmark适合验证tool-call syntax，但10,000+ MCP ecosystem把问题变成server/tool discovery、routing和跨工具组合。benchmark把hidden state、observations、route/execute/response actions、transition与terminal reward分开；agent先检索server/tool descriptions再执行，LiveMCPEval从task-specific key points自适应判断动态结果。registry snapshot拥有tool identity/schema，orchestrator拥有route与ACL，executor拥有side effect，judge不能重写事实结果。
- **Evaluation / evidence boundary:** 10个frontier/open models，ReAct agent与description-similarity retrieval；DeepSeek-V3主judge与human review约81% agreement。作者success rate包含model、retrieval、tool availability与judge共同作用，不是纯model capability；动态API drift、auth/tenant safety、tool side effect、cost/latency/concurrency和failure recovery限制跨时间复现。
- **Trade-off / owner / disposition:** live evaluation提高生态真实性，却牺牲snapshot determinism并扩大secret、network和irreversible-action风险；固定mock suite仍适合regression。canonical owner `AGENT-MCP` Ch83，handoff `PLATFORM-EVALUATION-SYSTEM` Ch66与`AGENT-TOOL-CALLING` Ch78；`Refine — Existing Argument Candidate`。

### Representation Shift

- **Identity / dates / sources / full-read coverage:** `ARXIV-2508.00367`，v1 first-public 2025-08-01，24/30；已阅读全文training-free representation-change metric、layer/token exploration、FlashAttention integration、video retrieval/QA与image classification、attention-score baselines、throughput/accuracy analyses和limitations。
- **Problem / previous design / changed constraint / mechanism:** attention-map importance适合传统kernel，却要求materialize attention map，与FlashAttention避免HBM I/O的设计冲突。Representation Shift以相邻layer token representation变化量估计importance，先执行fused attention再在layer边界prune，无需读取attention map。execution plan拥有prune schedule/ratio，model state拥有surviving token indices；位置/temporal identity必须随prune map传播。
- **Evaluation / evidence boundary:** UMT-B/L video tasks及image classifiers，training-free逐层pruning，比较attention-score token reduction与FlashAttention throughput；作者报告特定GPU/workload下throughput与任务指标。不能把kernel-level/单模型throughput外推LLM serving，未披露统一precision、batch/concurrency、end-to-end latency和dynamic-content SLO，representation change也不是semantic necessity proof。
- **Trade-off / owner / disposition:** 避开attention map使compression与fused kernel共存，却可能删除“当前变化小、稍后才关键”的token，并增加index remap/debug成本；短序列或accuracy-critical任务仍保留dense tokens。canonical owner `MULTIMODAL-REPRESENTATION` Ch23，handoff `INFER-TENSORRT-LLM` Ch49；`Emerging / Experimental — Refine Candidate`。

### A Glimpse to Compress / GlimpsePrune

- **Identity / dates / sources / full-read coverage:** `ARXIV-2508.01548`，v1 first-public 2025-08-03，23/30；已阅读全文visual information probe、single-pass dynamic pruning、enhanced fine-tune branch、Qwen2.5-VL/LLaVA experiments、fixed/adaptive baselines、ratio/position ablations、free-form VQA和appendices，并检查 `HVision-NKU/GlimpsePrune`。
- **Problem / previous design / changed constraint / mechanism:** 固定visual-token ratio让kernel shape和capacity planning简单，但scene complexity差异会使简单图像浪费token、复杂图像误删。GlimpsePrune先用visual information probe读取多层features，预测每个样本的保留token，再在约2/3 decoder位置一次prune；enhanced branch允许fine-tuning恢复质量。model/version、image resolution、probe和prune map共同构成execution identity。
- **Evaluation / evidence boundary:** Qwen2.5-VL-7B动态4～16,384 visual tokens与LLaVA-1.5-7B固定576 tokens，多个VQA/vision benchmarks；92.6%平均pruning和performance retention是作者aggregate，不代表所有scene/hardware。accuracy table不能证明真实latency/goodput；训练成本、GPU、precision、batch/concurrency、OCR/small-object tail与SLO需单独绑定。
- **Trade-off / owner / disposition:** per-input ratio减少平均compute，却造成ragged batch、quality tail、probe overhead和不可逆token loss；复杂安全视觉任务可选固定高保留率。canonical owner `MULTIMODAL-REPRESENTATION` Ch23，handoff `INFER-PREFILL` Ch43；`Emerging / Experimental — Refine Candidate`。

### SWE-Exp

- **Identity / dates / sources / full-read coverage:** `ARXIV-2507.23361`，v1 first-public 2025-07-31，26/30；已阅读全文trajectory collection、success/failure experience extraction、multi-facet bank、embedding/retrieval/rerank、Instructor/Assistant roles、MCTS integration、SWE-bench-Verified setup、baselines/ablations/leakage/threats和official code/data。
- **Problem / previous design / changed constraint / mechanism:** 每个issue独立MCTS可保持state隔离且避免旧经验污染，但会重复失败探索。SWE-Exp把raw repair trajectories离线提炼为comprehension与modification experience，按issue type/description索引；新issue检索top-N、rerank到top-1，由Instructor制定方向、Assistant执行search/view/edit/test。raw trace、derived experience、repository version、verifier result和supersession必须分离；同repo experience被排除以减轻leakage。
- **Evaluation / evidence boundary:** DeepSeek-V3-0324、temperature 0.7、最多20 iterations/2 finished nodes，SWE-bench-Verified；比较Agentless、SWE-Agent、SWE-Search、OpenHands等并做experience facet/数量ablation，作者报告41.6% Pass@1。不同baseline model/scaffold并非全都compute matched；benchmark patch通过不证明experience因果正确，token/cost/concurrency、poisoning、delete/rollback和cross-time repo drift未闭合。
- **Trade-off / owner / disposition:** derived repair memory减少重复探索，却可能传播错误pattern、泄漏benchmark、过拟合旧API并放大retrieval bias；新仓库或强版本漂移仍应从raw evidence开始。canonical owner `AGENT-MEMORY` Ch77，handoff `AGENT-WORKFLOW` Ch81；`Refine — Existing Argument Candidate`。

### SWE-Debate

- **Identity / dates / sources / full-read coverage:** `ARXIV-2507.23348`，v1 first-public 2025-07-31，24/30；已阅读全文dependency-graph fault traces、three-round specialized debate、consolidated edit plan、MCTS patch generation、SWE-bench Verified/Lite、baselines、chain-depth与component ablations、threats，并检查official code/data。
- **Problem / previous design / changed constraint / mechanism:** 单agent局部exploration成本低且责任清晰，但跨文件fault propagation与多个plausible fix location会陷入local solution。框架先遍历code dependency graph生成多条fault chains，再让不同视角agents竞争/反驳三轮，aggregator形成edit plan，最后交给MCTS editor与tests。graph snapshot、debate transcript、selected plan、code patch与test result是不同state；tests而不是多数意见拥有commit gate。
- **Evaluation / evidence boundary:** SWE-bench-Verified 500与Lite 300，比较Agentless、AutoCodeRover、SWE-Agent、SWE-Search、OpenHands等；作者报告41.4% Pass@1，去除multiple chains/debate/edit plan分别下降10.0/4.2/6.0 points。scaffold/model/token budgets不完全可比，debate相关错误、wall-clock/cost/concurrency与真实CI flakiness未充分披露。
- **Trade-off / owner / disposition:** 多视角提高localization coverage，却增加communication tax、shared bias、aggregator权力与token成本；小patch和强static analysis仍适合single-agent。canonical owner `AGENT-MULTI-AGENT` Ch82，handoff `AGENT-WORKFLOW` Ch81；`Emerging / Experimental — Refine Candidate`。

### Cyber-Zero

- **Identity / dates / sources / full-read coverage:** `ARXIV-2508.00910`，submission metadata 2025-07-29、first-public announcement 2025-08-02（Asia/Shanghai），26/30；已阅读全文129页v1 PDF的CTF source cleaning、dual-persona simulation、validation/rejection sampling、training、ENIGMA+、three benchmarks、ablations、security/limitations和official `amazon-science/cyber-zero`。无后续revision倒灌。
- **Problem / previous design / changed constraint / mechanism:** executable runtime trajectory最可信，但CTF环境常短命、受限或不可重建。Cyber-Zero从public writeups构造challenge metadata，让player model只看challenge、terminal model看writeup/flag并模拟command result和有限hint；exact flag、format、single-command与LLM alignment filters后用于SFT。writeup/provenance、simulator response、generated trajectory和real runtime evidence必须分级，synthetic terminal不能冒充执行事实。
- **Evaluation / evidence boundary:** 6,188 writeups/4,610 challenges、9,464≤32K trajectories；Qwen3/Qwen2.5/SWE-agent-LM，global batch16、LR5e-6、2 epochs；ENIGMA+在隔离containers并行评测InterCode-CTF、NYU CTF、Cybench共323 tasks、greedy/40 turns。作者报告最高平均+13.1 points，但不证明synthetic commands真实，也不证明对zero-day或生产网络授权；data leakage、dual-model共偏差与offensive misuse是核心边界。
- **Trade-off / owner / disposition:** 无runtime合成扩大训练覆盖，却引入simulator hallucination、unsafe capability transfer与false causal traces；可执行环境可用时仍应作为高等级verifier。canonical owner `TRAIN-DATA` Ch27，handoff `PLATFORM-SECURITY` Ch72与`AGENT-WORKFLOW` Ch81；`Emerging / Experimental — Security Boundary`。

### FACTORY

- **Identity / dates / sources / full-read coverage:** `ARXIV-2508.00109`，v1 first-public 2025-07-31，26/30；已阅读全文model-in-the-loop prompt generation、MassiveDS retrieval/filter、human revision、hard split、six-model evaluation、retrieval augmentation、claim verification、analysis/prompts/length appendix，并检查official dataset。
- **Problem / previous design / changed constraint / mechanism:** 自动生成factuality prompts规模大但可能不answerable、含歧义或只测head facts；全人工逐claim构造又昂贵。FACTORY先从Wikipedia titles/MassiveDS生成候选，用models和VeriScore筛出低precision questions，再由humans校验fact-seeking、answerable、unambiguous并修订；421 hard prompts按model表现后筛。prompt provenance、retrieval corpus snapshot、atomic claims、evidence与human adjudication必须可追踪。
- **Evaluation / evidence boundary:** Claude 3.7、Gemini 2.5 Pro、DeepSeek-V3、GPT-4o、Qwen3、Llama4，比较LongFact/FactBench与top-20 MassiveDS RAG；“约40% claims不 factual”是该prompt/model/evaluator条件的human study，不是LLM统一错误率。benchmark selection依赖当时models，MassiveDS snapshot、claim extraction、human disagreement、response length与search coverage限制可复现性。
- **Trade-off / owner / disposition:** adversarially筛难题提高evaluation power，却造成benchmark-model co-adaptation、长尾样本偏置与快速饱和；release gate需同时保留自然traffic与domain slices。canonical owner `PLATFORM-EVALUATION-SYSTEM` Ch66，handoff `AGENT-RAG` Ch76；`Refine — Evaluation Contract Candidate`。

### RoboMemory

- **Identity / dates / sources / full-read coverage:** `ARXIV-2508.01415`，v1 first-public 2025-08-02，24/30；已阅读全文preprocessor、spatial/temporal/episodic/semantic memories、dynamic KG、parallel update/retrieval、critic/loop mitigation、planner/executor、EB-ALFRED/Habitat与Mobile ALOHA experiments、ablations/appendices。project page在事件时未公开，artifact不足。
- **Problem / previous design / changed constraint / mechanism:** 单一episodic log实现简单且可回放，但physical embodied tasks同时需要location、sequence、experience和concept，并受闭环latency/infinite-loop约束。RoboMemory并行维护四类memory，以dynamic KG关联task state，critic检测plan failure/loop并触发replan，high-level planner把action交给low-level executor。sensor observation、world state、derived memory、plan与physical action commit必须分权；brain analogy只是解释，不是生物等价证据。
- **Evaluation / evidence boundary:** EB-ALFRED Base/Long 100 tasks、EB-Habitat、Qwen2.5-VL-72B与Voyager/Reflexion/Cradle等；真实Mobile ALOHA kitchen重复任务。作者success/steps指标和component ablation支持特定harness，不证明开放世界lifelong learning；baseline parity、real-world样本量、memory growth/latency、calibration/safety envelope、hardware/concurrency/SLO不完整。
- **Trade-off / owner / disposition:** typed parallel memory降低单store瓶颈，却引入cross-memory inconsistency、KG stale edges、critic false reset和delete/rollback复杂度；短任务仍用ephemeral state。canonical owner `AGENT-MEMORY` Ch77，handoff `MULTIMODAL-EMBODIED-VLA` Ch26；`Emerging / Experimental — Refine Candidate`。

### Web-CogReasoner

- **Identity / dates / sources / full-read coverage:** `ARXIV-2508.01858`，v1 first-public 2025-08-03，24/30；已阅读全文Factual/Conceptual/Procedural taxonomy、14-site Web-CogDataset、memorize/understand/explore curricula、knowledge-driven CoT、action space、training stages、Web-CogBench/VisualWebBench/live tasks、ablations和limitations。
- **Problem / previous design / changed constraint / mechanism:** screenshot-to-action imitation适合固定UI patterns，但unseen sites要求区分page facts、conceptual semantics与procedural policy。方法先构造三类web knowledge，再分阶段训练memorize/understand/explore；runtime按observable facts→concepts→procedure生成structured CoT、plan和click/type/scroll action。页面事实必须来自current observation，concept/procedure是versioned derived knowledge，browser executor拥有side-effect commit。
- **Evaluation / evidence boundary:** 7B model，8×A800-80GB，final stage max 8K、batch1、gradient accumulation16；评测Web-CogBench、VisualWebBench、WebVoyager与Online Mind2Web。作者结果混合dataset、curriculum、model和scaffold收益；live-site drift、auth/irreversible action、reasoning faithfulness、latency/cost/concurrency与failure recovery限制外推。
- **Trade-off / owner / disposition:** explicit knowledge layers提高traceability，却可能把stale procedure或错误concept制度化；熟悉稳定网站仍可用简化workflow。canonical owner `AGENT-WORKFLOW` Ch81，handoff `AGENT-CONTEXT` Ch75与`AGENT-PLANNING` Ch79；`Emerging / Experimental — Refine Candidate`。

#### W32 spillback owner、adjacent coverage 与 open questions

| Source Family | Canonical owner | Adjacent chapters checked | Existing coverage / unresolved evidence question |
| --- | --- | --- | --- |
| `ARXIV-2508.01191` | `WORLDVIEW-LLM-INTELLIGENCE` Ch8 | Ch7、Ch9、Ch66 | Ch8已有capability≠reliability；真实pretraining distribution下如何建立可反驳的CoT shift test？ |
| `ARXIV-2508.00819` | `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 | Ch23、Ch25、Ch48、Ch56 | Ch24已有mutable state/commit；dynamic length进入continuous batch后如何控制shape divergence和tail latency？ |
| `ARXIV-2508.01959` | `AGENT-RAG` Ch76 | Ch75、Ch77 | Ch76已有chunk/provenance/freshness；context-window变化时如何避免全量reindex并保持delete propagation？ |
| `ARXIV-2508.01780` | `AGENT-MCP` Ch83 | Ch66、Ch78、Ch82、Ch84 | Ch83已有discovery≠authorization；live API drift下怎样分离agent failure、tool outage与judge error？ |
| `ARXIV-2508.00367` | `MULTIMODAL-REPRESENTATION` Ch23 | Ch24、Ch43、Ch49 | Ch23已有representation identity；representation-shift threshold能否跨model/layer校准且保持small-object recall？ |
| `ARXIV-2508.01548` | `MULTIMODAL-REPRESENTATION` Ch23 | Ch24、Ch43 | 动态visual-token ratio如何进入ragged batching、quality-tail admission与可解释prune trace？ |
| `ARXIV-2507.23361` | `AGENT-MEMORY` Ch77 | Ch76、Ch81 | Ch77已有derived-memory provenance/supersession；跨repo收益在严格time split和compute-matched baseline下是否仍成立？ |
| `ARXIV-2507.23348` | `AGENT-MULTI-AGENT` Ch82 | Ch79、Ch81、Ch83 | Ch82已有single-agent headroom/communication tax；debate增益有多少来自dependency graph而非额外token budget？ |
| `ARXIV-2508.00910` | `TRAIN-DATA` Ch27 | Ch26、Ch28、Ch72、Ch81 | Ch27已有synthetic-data provenance；synthetic terminal trace如何取得不依赖同源LLM的state-transition verifier与安全release gate？ |
| `ARXIV-2508.00109` | `PLATFORM-EVALUATION-SYSTEM` Ch66 | Ch67、Ch76 | Ch66已有claim/evidence contract；hard split随model进步如何version而不造成leaderboard selection bias？ |
| `ARXIV-2508.01415` | `AGENT-MEMORY` Ch77 | Ch26、Ch76、Ch78 | Ch77已有typed/derived memory；四类memory冲突、physical-world correction与delete/rollback由谁仲裁？ |
| `ARXIV-2508.01858` | `AGENT-WORKFLOW` Ch81 | Ch75、Ch79、Ch80 | Ch81已有deterministic spine；knowledge-driven CoT是否忠实于observable page state，如何抵抗stale procedure和prompt injection？ |

## Low-score Source / Date / Rejection Closure

- `2507.20930` FRED、`2507.20956` Conformative Decoding、`2507.20783` Text Embeddings survey、`2507.20752` Multilingual Self-Taught Faithfulness Evaluators：均核验 v1 为 2025-07-28；19/18/17/19 分。前三项分别局限于activation editing、特定decoding objective与secondary overview；faithfulness evaluator仅覆盖有限language/task transfer，均未改变现有system owner。
- `2507.22411` NeedleChain 与 `2507.22462` IFEvalCode：v1 2025-07-30，18/19 分；分别是long-context intactness与controlled code-generation evaluation asset，缺独立runtime/training机制，Weekly保留source map后拒绝。
- `2507.22920` Multimodal Discrete Tokenization survey、`2507.22927` PRGB、`2507.22928` CoT SAE：v1 2025-07-30，19/18/19 分；survey和benchmark已由Ch23/24、Ch76、Ch66覆盖，SAE结论仍为exploratory representation evidence。
- `2507.23167` LENS、`2507.23279` Super Experts、`2507.23158` User Feedback：v1 2025-07-31，19/19/18 分；ensemble confidence未给deployment calibration，expert observation未推出routing redesign，user-feedback study为observational/noisy-signal evidence。
- `2508.00222` RL-PLUS、`2508.00271` MetaAgent、`2508.00500` Pro2Guard、`2508.00414` Cognitive Kernel-Pro：v1 2025-08-01，均19分；identity/full text/date可核，但各自仍是hybrid-policy、tool meta-learning、probabilistic enforcement或deep-research prototype，缺跨workload、artifact/version、failure recovery和production operating point，故低分闭合而非Review Pending。

## Pending、Blocked and Discovery Ledger

- **Review Pending（0项）:** 32/32 retained owner完成strict packet，16/16低分完成source/date/score/rejection closure。
- **Unverified / Blocked（0项）:** G-Core事件时v1已从作者上传的full-text mirror恢复；不再请求用户补PDF。
- **Disputed（3个claim/family边界）:** G-Core为withdrawn/unauthorized-source family；Graph-R1的reward/theory claims与event-time artifact drift；DICE的MI/generalization formal claims。三者均为source-complete终态，不伪装成阅读pending。
- **W32 spillback reconciliation:** W32指出14个W31 owner；RL-PLUS、Cognitive Kernel-Pro已存在且未重复计分，其余12项均已回拨canonical ledger并完成Full Source Review，W32不再拥有这些首次公开事件。
- **Routed outside W31:** H-MEM、ARPO、GEPA、Deep Researcher、Beyond Binary Rewards、Quantization Geometry回拨W30；TensorRT-LLM rc5/0.21.0归W32。

## Candidate Evidence Gate

- ISO window：Pass。
- Scored owner ledger：48项；21项25～30分、11项20～24分、16项低于20分，48/48六维Total可复算。
- Retained review：32/32；low-score closure：16/16；ordinary Review Pending 0；Unverified / Blocked 0。
- Source-family/date/dedup：Pass；G-Core以source-complete Disputed终态保留，未被误删或误当正常公司发布。
- Candidate Evidence Gate：`Passed`；W31 Discovery Replay Gate：`Passed`；年度 Archive Completion Gate：`Open`；Historical Books Gate：`Closed`。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / technical report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系是本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper v1 与后续集成若日期不同，分别记录证据角色，但只建立一个 Books source packet。
- 新方案不静默覆盖旧方案；记录新增状态、成本和 failure modes。

## Knowledge Tree Position

- GLM-4.5 → 第 20、21、29、45、46、74 章（Direct Evolution）
- Kimi K2 technical report → 第 21、24、29、32、45、74 章（Layering / Dependency）
- SLAI → `INFER-SCHEDULING` Ch56（deadline/slack-aware mixed scheduling）
- Graph-R1 → `AGENT-RAG` Ch76，handoff `TRAIN-GRPO` Ch33（multi-turn retrieval environment / terminal credit）
- DICE → `AGENT-CONTEXT` Ch75（stepwise demonstration working set；formal claims disputed）
- Graph-Augmented LLM Agents survey → `AGENT-PLATFORM` Ch84（secondary taxonomy / already covered）
- GMPO、RLSF → `TRAIN-GRPO` Ch33 / `TRAIN-RLHF` Ch31（policy-update stability与self-confidence reward边界）
- AutoTIR、MemTool → `AGENT-TOOL-CALLING` Ch78 / `AGENT-CONTEXT` Ch75（learned tool proposal与active tool-set ownership）
- Multi-Agent-as-Judge、Persona Vectors、Watch the Weights → `PLATFORM-EVALUATION-SYSTEM` Ch66 / `PLATFORM-MONITORING` Ch67（judge correlation、activation与weight telemetry均非ground truth）
- TriangleMix、Falcon-H1、GEAK → `INFER-PREFILL` Ch43、`MODEL-SELF-ATTENTION` Ch14、`INFER-TENSORRT-LLM` Ch49（execution plan、typed recurrent/KV state与executable kernel evidence）
- TTS-1 → `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24（audio-token generation与stream commit）
- Compressed History States、Self-Evolving Agents survey → `AGENT-CONTEXT` Ch75 / `AGENT-PLATFORM` Ch84（derived context、versioned evolution gate）
- G-Core → `TRAIN-DISTRIBUTED-TRAINING` Ch36，handoff Ch40～41（withdrawn evidence；parallel control与dynamic placement仅冻结为研究信号）
- CoT Mirage → `WORLDVIEW-LLM-INTELLIGENCE` Ch8（CoT distribution-shift boundary；controlled synthetic evidence）
- Beyond Fixed → `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24（diffusion LM dynamic length / mask-state expansion）
- SitEmb-v1.5 → `AGENT-RAG` Ch76（context-aware chunk identity与reindex contract）
- LiveMCPBench → `AGENT-MCP` Ch83（large tool ecosystem discovery、execution与live evaluation）
- Representation Shift、GlimpsePrune → `MULTIMODAL-REPRESENTATION` Ch23（FlashAttention-compatible与input-adaptive token pruning）
- SWE-Exp、RoboMemory → `AGENT-MEMORY` Ch77（derived experience与typed embodied memory）
- SWE-Debate → `AGENT-MULTI-AGENT` Ch82（dependency-guided bounded debate）
- Cyber-Zero → `TRAIN-DATA` Ch27，handoff `PLATFORM-SECURITY` Ch72（runtime-free synthetic trajectory的证据等级）
- FACTORY → `PLATFORM-EVALUATION-SYSTEM` Ch66（human-verified long-form factuality contract）
- Web-CogReasoner → `AGENT-WORKFLOW` Ch81（facts/concepts/procedures到browser action的分层状态）

## Recommended Action

- GLM-4.5：Must Read；与 Qwen3/DeepSeek V3.1 比较 hybrid contract
- Kimi K2 technical report：Must Read；Books 只形成一个 K2 source packet
- 32个retained owner均已完成strict packet；16个低分owner完成闭合。W32回拨14项已完成12项新增与2项去重。G-Core不再缺材料，但撤回授权争议未解决，保持Disputed并禁止进入Books。

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

`Frozen — Historical Books Gate Closed`。W31 Weekly证据已闭合，但本轮只完成历史Weekly，不以周级Evidence Gate通过替代年度Books Gate；所有Integration Decision仍是provisional，本轮不修改Books。


## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。

## Repository Changes

- 仅重建本文件：旧2项baseline经两轮discovery与W32 spillback reconciliation扩展并闭合为48个scored owner（32 retained strict、16 low closure）。
- 将W32发现的14个W31 owner逐项对账：RL-PLUS、Cognitive Kernel-Pro沿用既有低分closure，不重复；其余12项新增canonical评分与Full Source Review。
- 恢复G-Core事件时v1全文，将错误的`Unverified / Blocked`改为`Disputed — Withdrawn Source / Mechanism Evidence Frozen`。
- 保持Historical Books Gate关闭；未修改年度索引、Learning State、Books或ROADMAP。

## Open Questions

- GLM-4.5 release 与 W32 report 的最终主 owner 仍待 Books Gate。
- Kimi K2 的 optimizer、activation precision 与 topology 是一个联合稳定性 contract，需在 Ch21/32/34 之间选择唯一主 owner。
- SLAI fairness/starvation与threshold stability、Graph-R1 reward/theory mismatch和event-time artifact能否独立复现？
- GMPO是否在不同reward sparsity/rollout topology保持稳定；RLSF自信reward何时产生self-confirmation；MemTool active-set mutation如何绑定ACL、cache identity与rollback？
- G-Core后续获公司批准的WeChat-YATT材料是否与撤回v1同族、哪些机制/数字被正式保留？在官方来源出现前不得解冻。

## Sources

- GLM-4.5 — https://github.com/zai-org/GLM-4.5（First Public: 2025-07-28 (release); 2025-08-08 (paper v1)；Accessed: 2026-07-31）
- Kimi K2 technical report — https://arxiv.org/abs/2507.20534（First Public: 2025-07-28；Accessed: 2026-07-31）
- Optimal Scheduling Algorithms for LLM Inference — https://arxiv.org/abs/2508.01002（v1: 2025-08-01；Full Source Review Complete；Accessed: 2026-08-22）
- Graph-R1 — https://arxiv.org/abs/2507.21892（v1: 2025-07-29；Full Source Review Complete；Accessed: 2026-08-22）
- Graph-R1 official repository — https://github.com/LHRLAB/Graph-R1（event-time commit not pinned；Accessed: 2026-08-22）
- DICE — https://arxiv.org/abs/2507.23554（v1: 2025-07-31；Full Source Review Complete — Emerging / Experimental / Formal Claims Disputed；Accessed: 2026-08-22）
- Graph-Augmented Large Language Model Agents — https://arxiv.org/abs/2507.21407（v1: 2025-07-29；Full Source Review Complete — Secondary Taxonomy / No Change Already Covered；Accessed: 2026-08-22）
- G-Core — https://arxiv.org/abs/2507.22789（v1: 2025-07-30；v2: 2025-07-31 withdrawn；arXiv metadata verified，事件时正文由下一项作者镜像恢复；Accessed: 2026-08-24）
- G-Core event-time full-text mirror — https://www.researchgate.net/publication/394121452_G-Core_A_Simple_Scalable_and_Balanced_RLHF_Trainer（v1 full text recovered；withdrawn-source dispute retained；Accessed: 2026-08-24）
- GMPO — https://arxiv.org/abs/2507.20673（v1: 2025-07-28；Accessed: 2026-08-24）
- RLSF — https://arxiv.org/abs/2507.21931（v1: 2025-07-29；Accessed: 2026-08-24）
- AutoTIR — https://arxiv.org/abs/2507.21836（v1: 2025-07-29；Accessed: 2026-08-24）
- Multi-Agent-as-Judge — https://arxiv.org/abs/2507.21028（v1: 2025-07-28；Accessed: 2026-08-24）
- MemTool — https://arxiv.org/abs/2507.21428（v1: 2025-07-29；Accessed: 2026-08-24）
- Persona Vectors — https://arxiv.org/abs/2507.21509（v1: 2025-07-29；Accessed: 2026-08-24）
- Accelerating Prefilling / TriangleMix — https://arxiv.org/abs/2507.21526（v1: 2025-07-29；Accessed: 2026-08-24）
- Falcon-H1 — https://arxiv.org/abs/2507.22448（v1: 2025-07-30；Accessed: 2026-08-24）
- GEAK — https://arxiv.org/abs/2507.23194（v1: 2025-07-31；Accessed: 2026-08-24）
- TTS-1 — https://arxiv.org/abs/2507.21138（v1: 2025-07-28；Accessed: 2026-08-24）
- Compressed History States — https://arxiv.org/abs/2507.21369（v1: 2025-07-29；Accessed: 2026-08-24）
- Self-Evolving Agents survey — https://arxiv.org/abs/2507.21046（v1: 2025-07-28；Accessed: 2026-08-24）
- Watch the Weights — https://arxiv.org/abs/2508.00161（v1: 2025-08-01；Accessed: 2026-08-24）
- CoT Mirage / DataAlchemy — https://arxiv.org/abs/2508.01191（v1 first-public: 2025-08-02；Accessed: 2026-08-24）
- DataAlchemy official artifact — https://github.com/ChengshuaiZhao0/DataAlchemy（Accessed: 2026-08-24）
- Beyond Fixed / DAEDAL — https://arxiv.org/abs/2508.00819（v1 first-public: 2025-08-01；Accessed: 2026-08-24）
- DAEDAL official artifact — https://github.com/Li-Jinsong/DAEDAL（Accessed: 2026-08-24）
- SitEmb-v1.5 — https://arxiv.org/abs/2508.01959（v1 first-public: 2025-08-03；Accessed: 2026-08-24）
- LiveMCPBench — https://arxiv.org/abs/2508.01780（v1 first-public: 2025-08-03；Accessed: 2026-08-24）
- Representation Shift — https://arxiv.org/abs/2508.00367（v1 first-public: 2025-08-01；Accessed: 2026-08-24）
- A Glimpse to Compress / GlimpsePrune — https://arxiv.org/abs/2508.01548（v1 first-public: 2025-08-03；Accessed: 2026-08-24）
- GlimpsePrune official artifact — https://github.com/HVision-NKU/GlimpsePrune（Accessed: 2026-08-24）
- SWE-Exp — https://arxiv.org/abs/2507.23361（v1 first-public: 2025-07-31；Accessed: 2026-08-24）
- SWE-Exp official artifact — https://github.com/YerbaPage/SWE-Exp（Accessed: 2026-08-24）
- SWE-Debate — https://arxiv.org/abs/2507.23348（v1 first-public: 2025-07-31；Accessed: 2026-08-24）
- SWE-Debate official artifact — https://github.com/YerbaPage/SWE-Debate（Accessed: 2026-08-24）
- Cyber-Zero — https://arxiv.org/abs/2508.00910（v1 submission metadata: 2025-07-29；first-public announcement: 2025-08-02 Asia/Shanghai；Accessed: 2026-08-24）
- Cyber-Zero official artifact — https://github.com/amazon-science/cyber-zero（Accessed: 2026-08-24）
- FACTORY — https://arxiv.org/abs/2508.00109（v1 first-public: 2025-07-31；Accessed: 2026-08-24）
- FACTORY official dataset — https://huggingface.co/datasets/facebook/FACTORY（Accessed: 2026-08-24）
- RoboMemory — https://arxiv.org/abs/2508.01415（v1 first-public: 2025-08-02；project page Not Available at event time；Accessed: 2026-08-24）
- Web-CogReasoner — https://arxiv.org/abs/2508.01858（v1 first-public: 2025-08-03；Accessed: 2026-08-24）
- W31 low-score source identities — https://arxiv.org/abs/2507.20930, https://arxiv.org/abs/2507.20956, https://arxiv.org/abs/2507.20783, https://arxiv.org/abs/2507.20752, https://arxiv.org/abs/2507.22411, https://arxiv.org/abs/2507.22462, https://arxiv.org/abs/2507.22920, https://arxiv.org/abs/2507.22927, https://arxiv.org/abs/2507.22928, https://arxiv.org/abs/2507.23167, https://arxiv.org/abs/2507.23279, https://arxiv.org/abs/2507.23158, https://arxiv.org/abs/2508.00222, https://arxiv.org/abs/2508.00271, https://arxiv.org/abs/2508.00500, https://arxiv.org/abs/2508.00414（v1 dates verified；low-score closure；Accessed: 2026-08-24）
