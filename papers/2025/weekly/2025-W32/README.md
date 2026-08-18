# AI Research Weekly — 2025-W32

> Coverage Window: 2025-08-04～2025-08-10
> Research Mode: Retrospective Backfill
> Accessed: 2026-08-24
> Backfilled: 2026-07-31
> Audit Status: Historical Weekly Evidence Gate Passed — 41/41 Scored, 16/16 Retained Full Source Review, 25/25 Low-score Closure
> Historical Books Gate: Closed

## Executive Summary

本周完成固定来源与学术 discovery replay，共核验 41 个周内候选、17 个跨周 spillback；16 项达到 20/30 并完成非模板化 Full Source Review，25 项以来源、日期、评分与拒绝理由闭合。新增证据集中在四条演进链：开放权重与在线路由的责任迁移、AR 到 block-wise diffusion 的生成状态变化、从静态 SFT 到 environment-coupled Agent RL、以及 verifier / multimodal distributed runtime 的可执行 contract。论文与厂商 benchmark 均保持其 workload 边界。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；后续修订回链首次公开周。
- Scholar、OpenAlex、DBLP 负责 discovery/去重；论文事实回到正文。Crossref 仅交叉检验 metadata。
- 历史回填不创建 Daily；本轮实际访问日期为 2026-08-24。
- 作者/厂商 benchmark 缺少完整 workload contract 时不外推。
- Hugging Face featured/submission date 只作 discovery；owner week 一律由官方首次公开日、arXiv v1 或 release tag 决定。
- Scholar/OpenAlex discovery export 无法形成封闭召回证明，因此本周 Gate 表示固定来源 replay 与已知候选闭合，不宣称全球论文穷尽。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外模型公司、研究机构与 Hugging Face Blog。

- 保留：gpt-oss（2025-08-05）、GPT-5（2025-08-07）、Qwen-Image（2025-08-04）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 event-time arXiv versions 核验；同周多版合并，后续周 revision 只记录演进、不倒灌。

- 保留：Seed Diffusion、Agent Lightning、SWE Agent RL、VeriGUI、SEAgent、CompassVerifier、R-Zero、Dynamic Fine-Tuning、VeOmni、ToolTrain、AttnTrace 与 GLM-4.5 technical report。

## 3. AI Infra 与工程项目

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → Dynamo → TensorRT-LLM → Ray → KServe → Kubeflow → Kubernetes → Hugging Face → DeepSpeed → Megatron-LM → llama.cpp → ONNX Runtime → OpenXLA 扫描。

- 保留：TensorRT-LLM v0.21.0；v1.0.0rc5 是同日同 release train 的 related event，不重复计分。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| gpt-oss | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Must Read；联合模型卡与 safety paper 全文复核 |
| GPT-5 | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Worth Watching；只作为 inference policy 信号 |
| GLM-4.5 technical report | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；不重复计算为第二个 Books 事件 |
| Qwen-Image technical report | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Must Read；多模态表示与生成 owner |
| Seed Diffusion | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Must Read；parallel decoding 受限案例 |
| Agent Lightning | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Must Read；trajectory schema 与 training-agent disaggregation |
| SWE Agent RL | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Must Read；stateful environment RL contract |
| VeriGUI | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；subtask-level executable verification |
| SEAgent | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Must Read；derived guidebook、world-state reward 与 curriculum |
| CompassVerifier | 4 | 5 | 5 | 5 | 4 | 4 | 27/30 | Must Read；verifier 是 versioned evaluation/reward component |
| R-Zero | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Must Read；challenger-solver curriculum branch |
| Dynamic Fine-Tuning | 5 | 4 | 5 | 4 | 5 | 3 | 26/30 | Must Read；token-gradient weighting 的受限替代分支 |
| VeOmni | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Must Read；model-centric distributed recipe |
| ToolTrain | 4 | 4 | 5 | 4 | 5 | 3 | 25/30 | Must Read；tool policy 与 repo-search environment coupling |
| AttnTrace | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Worth Watching；attention attribution 不等于因果证据 |
| TensorRT-LLM v0.21.0 | 3 | 5 | 5 | 5 | 5 | 3 | 26/30 | Must Read；typed feature-combination 与 known-issue contract |
| Goedel-Prover-V2 | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Weekly Only；formal proof domain，机制主线已有覆盖 |
| TRACEALIGN | 4 | 3 | 3 | 3 | 3 | 2 | 18/30 | Emerging；理论与经验边界不足以形成 owner |
| IFDecorator | 3 | 3 | 4 | 4 | 3 | 2 | 19/30 | Weekly Only；instruction-following data method，长期独立性不足 |
| Skywork UniPic | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Weekly Only；统一图像生成案例，未改变 Ch24 结论 |
| Beyond the Trade-off | 4 | 3 | 3 | 3 | 3 | 2 | 18/30 | Emerging；self-supervised instruction-following RL 仍依赖作者 evaluator |
| Trainable Dynamic Mask Sparse Attention | 4 | 4 | 3 | 3 | 3 | 2 | 19/30 | Emerging；未形成可迁移 runtime contract |
| Sparse-dLLM | 4 | 3 | 3 | 3 | 3 | 2 | 18/30 | Emerging；与 Seed Diffusion 同路线但证据较弱 |
| Dynaword | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Weekly Only；动态 tokenization 案例 |
| Sculptor | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Weekly Only；active context management 未改变 context owner 主线 |
| CoAct-1 | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Weekly Only；computer-use action case |
| InfiAlign | 3 | 3 | 3 | 4 | 4 | 2 | 19/30 | Weekly Only；alignment data pipeline case |
| DeepPHY | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Emerging；physics-grounded video case，机制外推受限 |
| Genie Envisioner | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Emerging；embodied imagination case，环境闭环未充分验证 |
| CellForge | 3 | 2 | 3 | 4 | 2 | 2 | 16/30 | Domain Only；AI for Science workflow 未改变系统 contract |
| HarmonyGuard | 3 | 3 | 4 | 4 | 3 | 2 | 19/30 | Weekly Only；safety benchmark case |
| Learning to Reason for Factuality | 3 | 3 | 3 | 4 | 4 | 2 | 19/30 | Weekly Only；factuality RL 证据边界不足 |
| ChartCap | 3 | 2 | 3 | 4 | 2 | 2 | 16/30 | Domain Only；chart understanding dataset |
| StepFun-Formalizer | 3 | 2 | 3 | 4 | 2 | 2 | 16/30 | Domain Only；formalization model fact |
| MiDashengLM | 3 | 3 | 3 | 4 | 2 | 2 | 17/30 | Domain Only；audio model release case |
| LeanK | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Weekly Only；learnable K-cache channel pruning 的受限 KV 优化分支 |
| Double-Bench document RAG evaluation | 3 | 3 | 4 | 4 | 4 | 1 | 19/30 | Weekly Only；evaluation snapshot，未改变证据框架 |
| Sotopia-RL | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Emerging；social-agent reward case |
| VLM RL in synthetic worlds | 4 | 3 | 3 | 3 | 3 | 2 | 18/30 | Emerging；sim-to-real 边界未闭合 |
| Agentic e-commerce evaluation | 3 | 3 | 4 | 4 | 4 | 1 | 19/30 | Weekly Only；domain harness case |
| Multi-agent document QA / MACT | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Weekly Only；未给 compute-matched single-agent headroom |

### Deep Analysis 1 — gpt-oss

- First Public: 2025-08-05
- Status: Official open-weight release + model/safety cards
- Primary Source: https://openai.com/index/introducing-gpt-oss/
- Evolution Relationship: Direct Evolution

#### Why

开放 reasoning model 需要同时满足可部署 memory budget、tool-use contract、可定制性与开放权重的 worst-case safety evaluation。

#### Principle and Mechanism

gpt-oss 采用 MoE、local/global attention、MXFP4 weights、Harmony format 与 reasoning/tool post-training，并发布 malicious fine-tuning 风险评估。

#### Trade-off and Evidence Boundary

量化开放权重降低部署门槛，也把 fine-tuning 与 misuse 能力交给部署方；单卡可装载条件不等于满足生产吞吐和 SLO。

#### Connection and Evolution

知识树位置：第 20、21、23～25、29、45、46、68 章。Must Read；联合模型卡与 safety paper 全文复核。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

### Deep Analysis 2 — GPT-5

- First Public: 2025-08-07
- Status: Official proprietary release + system card
- Primary Source: https://openai.com/index/introducing-gpt-5/
- Evolution Relationship: Direct Evolution

#### Why

产品从用户手动选择 reasoning model 转向由 router 在 fast model 与 deep reasoning 间做实时决策。

#### Principle and Mechanism

官方材料确认 unified system、reasoning router、工具能力与 safety evaluation；路由算法和训练机制未公开。

#### Trade-off and Evidence Boundary

自动路由简化用户界面，却引入错误分流、不可预测成本、版本耦合与评测归因问题。

#### Connection and Evolution

知识树位置：第 20、52、62、68、74～77 章。Worth Watching；只作为 inference policy 信号。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

### Deep Analysis 3 — GLM-4.5 technical report

- First Public: 2025-08-08
- Status: arXiv v1; official report
- Primary Source: https://arxiv.org/abs/2508.06471
- Evolution Relationship: Layering / Dependency

#### Why

W31 release 的 hybrid reasoning 和 agent claim 需要完整训练、数据和 evaluation 证据。

#### Principle and Mechanism

报告补足架构与 post-training 细节；与 W31 合并为一个 source packet。

#### Trade-off and Evidence Boundary

报告仍是作者实验，不能用综合排名替代 workload-specific evaluation。

#### Connection and Evolution

知识树位置：第 20、21、29、45、46、74 章。Must Read；不重复计算为第二个 Books 事件。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

## Full Source Review

### gpt-oss-120b / gpt-oss-20b

- **Candidate / Week / Score:** gpt-oss / 2025-W32 / 27/30。
- **Source Family ID:** `OPENAI-GPT-OSS-2025-08`。
- **Source Type:** official announcement、35-page model card、adversarial fine-tuning safety paper/model artifacts/reference implementations。
- **First-public Date / Revision History:** release/model card 2025-08-05；后续 safeguard model与runtime optimizations不回写为初始release能力。
- **Direct Primary Sources:** OpenAI `Introducing gpt-oss`；gpt-oss-120b/20b Model Card；official weights/config/tokenizer/reference inference；malicious fine-tuning report。
- **Related Primary Sources:** Harmony format、MXFP4 spec/runtime implementations、Preparedness Framework；W44 safeguard为后续同族事件。
- **Access and Verification Status:** Verified for model card, artifacts, evaluation and published safety methodology；pretraining corpus、SFT/RL implementation、full fine-tuning data、production deployment SLO Not Disclosed。
- **Full-read Coverage:** 已阅读model card的executive summary、architecture/tokenizer/training、capability/tool/health/multilingual evaluations、safety/refusal/jailbreak/instruction hierarchy/CoT/hallucination、Preparedness与malicious fine-tuning、external-review appendix及未采纳建议；核对weights/config/reference implementations和配套safety paper。
- **Original Problem:** open-weight reasoning model要在单节点/consumer memory预算内提供可定制reasoning/tool use，同时假设operator可移除拒绝、修改权重并选择任意runtime，因此风险边界不同于hosted API。
- **Why the Previous Design Was Reasonable:** proprietary serving允许provider控制weights、moderation、rollback与abuse monitoring；BF16 dense/smaller open models减少quantization和MoE runtime复杂性。
- **Changed Constraint:** 用户要求本地/私有部署、Apache 2.0定制与16/80GB级memory target；open weights使部署者而非provider拥有最终safety/runtime policy。
- **Mechanism:** 120b为117B total/5.1B active、36 layers、128 experts选4；20b为21B/3.6B active、24 layers、32 experts选4；交替dense/local-banded attention、grouped multi-query attention、RoPE/YaRN到128K，并用MXFP4量化MoE weights。SFT+high-compute RL教reasoning/tool/Harmony contract。
- **State Ownership:** artifact producer拥有immutableweights/config；operator拥有runtime、fine-tune、moderation与telemetry；Harmony parser拥有channels/tool protocol；model的visible CoT不是trusted policy state，也不能直接展示而无过滤。
- **Control Flow / Data Flow:** mostly-English text pretraining → SFT/high-compute RL → MXFP4 artifact → operator runtime loads/dequantizes/runs MoE → Harmony separates analysis/tool/final → external workflow executes authorized tools；open release后provider不能撤回本地weights。
- **Implementation Details:** native128K；attention head denominator有learned bias允许“attend to none”；unconventional SwiGLU含clamp/residual；H100+PyTorch+expert Triton kernels训练，120b约2.1M H100-hours，20b近10×更少；完整optimizer/data/parallelism Not Disclosed。
- **Evaluation Setup:** high reasoning effort与o3/o3-mini/o4-mini比较；AIME有tool/no-tool差异，SWE-bench/TauBench使用任务scaffold；hallucination在无browse SimpleQA/PersonQA测；safety含production/refusal/jailbreak/instruction hierarchy。不同eval的tool、sampling与grader不同。
- **Baselines / Ablations / Sensitivity:** 有reasoning-level/tool/no-tool与model-size比较；缺MXFP4-vs-higher precision、MoE/local attention、SFT/RL和training-data controlled ablation。恶意微调只对120b，且竞争open models未获同等内部RL stack。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** training H100-hours、model sizes、MXFP4、128K与16/80GB fit claims披露；fit-in-memory不等于throughput，serving GPU/kernel、batch/concurrency、TTFT/TPOT/SLO不完整。
- **What the Evidence Actually Proves:** artifact与model card可核实open-weight MoE/quantization/interface；作者评测揭示120b/20b在instruction hierarchy和无browse hallucination上弱于o4-mini，证明开放部署需要system guardrails；高预算恶意微调测试在其framework内未达High。
- **What It Does Not Prove:** 不证明“接近o4-mini”跨所有任务成立，不证明16/80GB设备达到production latency，不证明公开CoT faithful/safe，不证明恶意微调上界覆盖所有攻击者、scaffold和未来方法。
- **Limitations / Threats to Validity:** mostly-English/text-only；smaller models knowledge不足且hallucination更高；system-prompt抗覆盖较弱；malicious fine-tune使用near-final checkpoint与内部stack，外部models比较条件不对称；若干external-review建议未实施，包括广泛best-of-N。
- **Trade-offs / New Failure Modes:** MXFP4+MoE降低memory/active compute却增加kernel/backend与quality parity风险；open weights带来自主部署/审计也转移patch、policy、abuse monitoring、prompt injection和fine-tune风险给operator。
- **Where the Previous Design Still Applies:** 需要central revocation、统一safety telemetry、low-ops burden或closed data governance时hosted model仍合理；质量/精度敏感且硬件足够时higher precision artifacts合理。
- **Evolution Relationship:** `Direct Evolution`：hosted reasoning API → open-weight reasoning artifact；dense/BF16 capacity → sparse MoE+MXFP4 memory contract。开放不是简单“更自由”，而是control ownership迁移。
- **ROADMAP Node:** canonical owner `PLATFORM-SECURITY` / current Ch72 / legacy Ch68；handoff `MODEL-MOE`、`TRAIN-RLHF`、`INFER-QUANTIZATION`、`AGENT-TOOL-CALLING`。
- **Target and Adjacent Chapters Read:** 已阅读 Ch19～22、Ch30～32、Ch44～47、Ch61～69、Ch73～75；Ch68 已按 model card 的实际弱点与 threat-model 边界最终复核。
- **Existing Coverage:** Ch21已有MoE cost边界，Ch45/46已有quantization/runtime contract，Ch68已有open-weight责任迁移。可能无需重复model规格，但instruction hierarchy、visible CoT和malicious fine-tuning threat model可refine security evidence。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch68，开放权重将 moderation/rollback/telemetry 责任转移给 operator。
- **Changed Files or Rejection Reason:** 已复核 `books/part-05-ai-infrastructure/68-security.md`；不将 fit-in-memory 写成 serving 性能。
- **Open Questions:** MXFP4 independent quality/throughput、full training/parallel recipe、third-party malicious fine-tuning upper bound、Harmony parser hardening与long-term patch provenance。

### GPT-5 unified system

- **Candidate / Week / Score:** GPT-5 / 2025-W32 / 24/30。
- **Source Family ID:** `OPENAI-GPT5-2025-08`。
- **Source Type:** official product/research pages、60-page system card、API model documentation。
- **First-public Date / Revision History:** GPT-5 system/product release 2025-08-07；later GPT-5.x system-card updates属于后续family revisions，不倒灌本周。
- **Direct Primary Sources:** GPT-5 System Card PDF/page；Introducing GPT-5 for developers；official API model/feature documentation。
- **Related Primary Sources:** safe-completions research and Preparedness Framework，只作safety机制背景。
- **Access and Verification Status:** Verified for public system composition、router signals、API/ChatGPT distinction与evaluation；model architecture、router model/objective、hardware、routing error rates与production SLO Not Disclosed。
- **Full-read Coverage:** 已阅读system card的system composition、safety training/evals、instruction hierarchy/prompt injection/hallucination、health、bio/cyber/AI self-improvement、external assessments与appendices；联读developer page的API model/mode/tool parameters和detailed benchmark caveats。
- **Original Problem:** 用户不应为每个query手工判断是否值得deep reasoning；单一fixed-compute model又难以同时优化latency、cost与hard-task quality。
- **Why the Previous Design Was Reasonable:** 显式model selection使cost/behavior可预测、评测归因清晰；独立fast/reasoning models可分别优化与回滚。
- **Changed Constraint:** 大量混合workload、tool requirements与用户对“think harder”的显式意图，使每请求动态compute选择成为产品控制问题。
- **Mechanism:** ChatGPT GPT-5是fast `gpt-5-main`、deeper `gpt-5-thinking`与real-time router组成的系统；router参考conversation type、complexity、tool needs与explicit intent，并用model switch、preference和correctness signals持续训练。API `gpt-5`则是thinking model，不等同ChatGPT统一router；usage limit后有mini fallback。
- **State Ownership:** router/control plane拥有model/mode selection与quota fallback；model worker拥有inference；API caller拥有reasoning effort/verbosity/tool contract；evaluation必须记录实际route/model而不能只记“GPT-5”。
- **Control Flow / Data Flow:** conversation + policy/quota + tool need → router selects main/thinking/mini → chosen model executes/tool calls → response/user switches/correctness signals进入后续router training；内部feature/objective/online update cadence Not Disclosed。
- **Implementation Details:** public材料不披露router architecture、threshold、calibration、exploration、rollback或per-tenant policy；API另有minimal reasoning、verbosity/custom tools grammar，是developer contract而非ChatGPT router实现。
- **Evaluation Setup:** system card分别评估main/thinking并在不同任务使用browse/tool/CoT/LLM grader；prompt injection含browse、tool-call与coding；部分factuality grader与human约75%一致。它不是router end-to-end误分流评测。
- **Baselines / Ablations / Sensitivity:** 有相对前代models和tool/browse条件比较；没有公布auto router vs user oracle、routing confusion matrix、cost-quality Pareto、quota fallback影响或route stability ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** architecture、parameter count、hardware、precision、batch/concurrency、route latency与SLO Not Disclosed；API产品参数和价格不能反推内部执行。
- **What the Evidence Actually Proves:** 官方明确区分“统一产品系统”和“API thinking model”，并证明compute/model selection可以成为在线control plane；system card也显示prompt injection需model training+cached-browse等system mitigations组合。
- **What It Does Not Prove:** 不证明router总选对、不证明统一系统必然优于显式选择、不证明benchmark提升来自routing；也不能把产品名称当成单一model checkpoint。
- **Limitations / Threats to Validity:** route outcome与错误率不可见；signals可能受用户偏好/selection bias影响；quota fallback改变behavior；model-graded eval与tool/browse条件异构；proprietary机制不可复现。
- **Trade-offs / New Failure Modes:** 自动routing简化UI并分配test-time compute，却新增misrouting、unpredictable cost/latency、route drift、evaluation attribution、fallback regression与policy/version coupling。
- **Where the Previous Design Still Applies:** regulated workload、strict latency/cost cap、reproducible evaluation或显式quality tier时，caller-selected model/mode仍更合理；简单请求无需deep reasoning。
- **Evolution Relationship:** `Direct Evolution`：manual model tier selection → policy-driven per-request routing → future pressure toward one model with continuous compute control；这是产品control-plane演进，不证明architecture替代。
- **ROADMAP Node:** canonical owner `INFER-SCHEDULING` / current Ch56 / legacy Ch52；handoff `PLATFORM-EVALUATION-SYSTEM`、`PLATFORM-SECURITY`、`AGENT-WORKFLOW`。
- **Target and Adjacent Chapters Read:** 已阅读 Ch19～20、Ch37～39、Ch51～53、Ch61～69、Ch73～77；Ch52应是主owner候选，Agent章节只短handoff到tool/workflow ownership。
- **Existing Coverage:** Ch52已覆盖routing要绑定SLO/cost，Ch62覆盖model/version/harness identity，Ch77覆盖workflow state。新增长期信号是“route本身必须成为evaluation evidence”，但缺router机制可能只适合refine而非新增专节。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch52，route/effort 决策进入 serving 与 evaluation identity。
- **Changed Files or Rejection Reason:** 已更新 `books/part-04-inference-system/52-inference-scheduling.md`；内部 router mechanism 保持 Not Disclosed。
- **Open Questions:** route logging/observability、misrouting与oracle baseline、quota fallback、router update governance、per-route safety/cost regression。

### GLM-4.5 technical report

- **Candidate / Week / Score:** GLM-4.5 technical report / 2025-W32 / 25/30。
- **Source Family ID:** `GLM-4.5-2508.06471`（与 W31 release同族）。
- **Source Type:** official arXiv technical report v1、release artifacts/repository。
- **First-public Date / Revision History:** arXiv v1 2025-08-08；截至核验仅v1。2025-07-28 release归W31，报告不重复计算为第二个Books事件。
- **Direct Primary Sources:** arXiv:2508.06471 v1 PDF/TeX；`zai-org/GLM-4.5` model artifacts/config。
- **Related Primary Sources:** Qwen3/DeepSeek-V3.1 hybrid reasoning lineage、open agent benchmark harness。
- **Access and Verification Status:** Verified for report/artifacts；pretraining corpus、expert-model iteration data、reward code、RL infrastructure code与training hardware Not Disclosed。
- **Full-read Coverage:** 已阅读metadata、Introduction/architecture、23T pretraining、expert-model iteration、SFT、reasoning/agent/general RL、RL infrastructure、evaluation setups/results与safety/conclusion；报告无独立limitations章节，未披露项按threats记录。
- **Original Problem:** 单一foundation model要兼顾agentic、reasoning、coding和direct response；post-training还需让static verifiable tasks与interactive environment tasks共享训练而不混淆reward/data flow。
- **Why the Previous Design Was Reasonable:** dense或较浅model、单一thinking mode与分离domain fine-tune易于稳定；static dataset的offline SFT/RL比environment rollout便宜。
- **Changed Constraint:** 23T-scale pretraining、MoE容量、长tool trajectories与hybrid mode使architecture efficiency、expert balance、sandbox throughput与rollout/training precision一致性同时成为系统约束。
- **Mechanism:** 355B/32B-active与Air 106B/12B-active MoE，3 dense+89 MoE layers、1 MTP layer；sigmoid gating/loss-free balance、GQA/partial RoPE/QK-Norm。post-training经expert model iteration，再分别做reasoning RL、agent RL和general RL，形成thinking/non-thinking contract。
- **State Ownership:** pretraining router拥有expert assignment/bias；expert iteration pipeline拥有candidate data与filter；sandbox/environment拥有tool outcome；RL trainer只优化model tokens，environment feedback tokens不进入loss；runtime mode/parser拥有部署时thinking state。
- **Control Flow / Data Flow:** 23T pretraining → expert model iteration/SFT → static reasoning rollout+verifier → web-search/coding environment rollout → group-wise policy update → general alignment → hybrid artifact；training BF16而rollout FP8时在dispatch前online block-wise quantization。
- **Implementation Details:** deeper/narrower design；loss-free balancing避免auxiliary-loss梯度干扰；agent data来自web-search与PR/issues，使用加固sandbox；RL基础设施处理BF16 training/FP8 rollout格式切换。training cluster/topology/checkpoint recovery未披露。
- **Evaluation Setup:** open toolkit汇总ARC benchmarks；TAU-bench使用优化user simulator；AIME Avg@32、GPQA Avg@8、HLE以GPT-4o judge；SWE-bench用OpenHands v0.34、最多100 iterations、history truncation、temperature 0.6/top-p 1。
- **Baselines / Ablations / Sensitivity:** 有architecture scaling与training-stage结果；static reasoning curriculum中全0/全1 group无advantage signal。缺loss-free balance/full-scale MoE controlled ablation、BF16↔FP8 rollout误差、sandbox/scaffold与mode contamination sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/active parameters与train BF16/rollout FP8披露；training GPU/topology/global batch、rollout concurrency、context/output distribution、serving SLO Not Disclosed。
- **What the Evidence Actually Proves:** 作者报告给出hybrid model从architecture、data到多个RL domain的可审计pipeline，并揭示interactive agent RL需要sandbox与只对model tokens优化的loss boundary；benchmark只证明作者harness下结果。
- **What It Does Not Prove:** 不证明统一hybrid model普遍优于separate fleets，不证明综合rank，不证明loss-free balance或FP8 rollout对所有MoE稳定；不能把SWE/TAU结果等同production agent reliability。
- **Limitations / Threats to Validity:** 无独立limitations section；数据/reward/infra不开源；LLM judge与user simulator偏差；SWE harness含100-step和history truncation；hardware与SLO缺失；static全0/1 group失去梯度说明curriculum/sampling强依赖当前policy。
- **Trade-offs / New Failure Modes:** deeper sparse model降低active compute却增加pipeline/expert routing；hybrid mode减少fleet数量却增加parser/mode contamination；BF16↔FP8切换提高rollout效率却新增numeric mismatch；sandbox扩展带来isolation与environment drift。
- **Where the Previous Design Still Applies:** 狭窄domain、严格behavior isolation或backend不支持时separate models更简单；reward不可验证/环境昂贵时SFT和human evaluation仍必要；auxiliary load balance在loss-free控制不可用时仍是成熟方案。
- **Evolution Relationship:** `Layering / Dependency`：MoE efficiency → loss-free routing control；single-domain post-training → reasoning/agent/general RL branches；separate model fleets → explicit hybrid mode。三条演进互相依赖但不互相覆盖。
- **ROADMAP Node:** canonical owner `TRAIN-RLHF` / current Ch31 / legacy Ch27；handoff `MODEL-MOE`、`TRAIN-GRPO`、`TRAIN-DISTRIBUTED-TRAINING`、`AGENT-WORKFLOW`。
- **Target and Adjacent Chapters Read:** 已阅读 Ch20～30、Ch31～35、Ch44～48、Ch51～52、Ch61～63、Ch73～77；W31 release与本packet最终只选一个Books主owner。
- **Existing Coverage:** Ch21已有routing/load trade-off，Ch29已有group-relative reward边界，Ch45～48已有precision/runtime contract，Agent chapters已有environment ownership。潜在新增点是training-vs-rollout precision转换与multi-domain RL state，而非榜单或model规格。
- **Integration Decision:** `No Change — Already Covered`；training/rollout precision、MoE routing 与 agent workflow 已由 Ch21/24/29/45/77 的 contracts 覆盖。
- **Changed Files or Rejection Reason:** 不改 Books；保留报告为 bounded model-system case。
- **Open Questions:** training topology/checkpoint、loss-free balance sensitivity、FP8 rollout parity、mode contamination、sandbox isolation与independent reproduction。

### Qwen-Image technical report

- **Candidate / Week / Score / Source Family:** Qwen-Image / 2025-W32 / 27/30 / `ARXIV-2508.02324-QWEN-IMAGE`；arXiv v1 2025-08-04 11:49 UTC，截至 2026-08-24 无后续 arXiv revision。Direct sources 为 v1 HTML/PDF、QwenLM 官方项目页与公开 artifacts。
- **Access / Full-read Coverage:** 已读 metadata、Introduction/Related Work、architecture、data pipeline、progressive curriculum、image generation/editing、evaluation、appendices 与 conclusion；训练数据清单、过滤阈值、完整优化器/集群拓扑、独立复现和 production SLO 未公开。
- **Problem / Previous Design / Changed Constraint:** 通用图像模型既要处理像素级纹理，又要理解段落文字与保持编辑对象身份。单一 VAE/diffusion conditioning 在纯生成上合理，但难同时保留 semantic identity 与 reconstructive detail；中英文复杂排版和编辑一致性把表示 owner 从单一路径变成多视图 contract。
- **Mechanism / State / Flow:** Qwen2.5-VL 提供语义表示，VAE 提供重建表示，MMDiT 在统一生成/编辑任务中融合；数据经收集、过滤、annotation、合成、balancing，再按 non-text → simple text → complex/paragraph text curriculum 训练。原图分别进入 semantic/reconstructive encoder，conditioning 与 latent state 必须保留 source image、crop/resize、prompt、task type 与版本 identity。
- **Implementation / Evaluation Contract:** 报告比较多个 text-rendering、generation 与 editing benchmark；模型、采样设置、分辨率和 grader 随 benchmark 变化，作者排名不是跨 workload 通用事实。缺硬件、precision、global batch、并发、端到端延迟、功耗和置信区间。
- **Evidence / Limits / Trade-offs:** 证据支持 dual encoding 与 multi-task curriculum 是该模型的公开机制，并在作者 harness 中改善文字与编辑；不证明任何 encoder 对所有模态最优，也不证明 benchmark quality 等于可控编辑可靠性。双表示提高 fidelity/semantic consistency，却新增 alignment drift、identity mismatch、两路缓存和训练配比敏感性；简单 T2I 仍可用更小单路模型。
- **Evolution / Owner / Decision:** `single latent conditioning → semantic + reconstructive identity → unified generation/editing`。Owner `MULTIMODAL-REPRESENTATION` / current Ch23 / legacy N/A，生成范式 handoff `MULTIMODAL-GENERATIVE-PARADIGMS` / current Ch24 / legacy N/A；已读 Ch22～25。`Emerging / Experimental — Refine Candidate`；Historical Books Gate 关闭。Open questions：artifact 对齐、data provenance/delete、两路表示消融、跨语言排版和 serving cost。

### Seed Diffusion

- **Candidate / Week / Score / Source Family:** Seed Diffusion Preview / 2025-W32 / 27/30 / `ARXIV-2508.02193-SEED-DIFFUSION`；arXiv v1 2025-08-04 08:43 UTC，截至 2026-08-24 无后续 arXiv revision。Direct sources 为 v1 HTML/PDF 与 ByteDance Seed 项目页；无可复现训练/runtime artifact。
- **Access / Full-read Coverage:** 已读全文及公式：two-stage corruption、trajectory distillation、on-policy objective、block-wise inference、benchmark、speed section和discussion；后续页面显示日期不作为 v1 event。参数量、训练 token、optimizer、internal kernel/code 与完整 serving profile 未公开。
- **Problem / Previous Design / Changed Constraint:** 左到右 AR 与 KV cache 在语法序列上自然、质量稳定，但 token dependency 限制并行度；纯 mask diffusion 理论上任意顺序，却面对无效 order、迭代步数和单次 full-sequence forward 成本。
- **Mechanism / State / Flow:** 前 80% 使用 mask corruption，后 20% 加 edit corruption，迫使模型重新判断未 mask token；从候选 denoising trajectories 中按 ELBO 选择约束顺序，再用 verifier-coupled on-policy objective压缩 steps。推理按 block 保持块间 causal、块内并行，已提交 block 进入 KV cache，未收敛 token 是 mutable proposal state。
- **Implementation / Evaluation Contract:** code-only dense Transformer；作者在 H20 上报告 2,146 token/s，但明确 Mercury 使用 H100、Gemini hardware 未知，条件不可直接比较。评测覆盖 Aider、CanItEdit、MBXP、HumanEval/MBPP、BigCodeBench、LiveCodeBench；batch、concurrency、precision、TTFT/TPOT、block size distribution 与 SLO 不完整。
- **Evidence / Limits / Trade-offs:** 证明在作者 code workload 与内部 runtime 中，semi-AR diffusion 可形成不同于 token-by-token 的 speed/quality branch；不证明 2,146 token/s 可跨硬件/长度复制，也不证明 diffusion 取代 AR。并行 proposal换来反复验证、mutable state、commit/rollback、block-size sensitivity和质量/延迟耦合；短输出、低 batch 或 exact prefix cache 场景 AR 仍合理。
- **Evolution / Owner / Decision:** `AR token commit → full masked refinement → constrained trajectory → block-wise proposal/commit`。Owner `MULTIMODAL-GENERATIVE-PARADIGMS` / current Ch24 / legacy N/A，handoff `INFER-SPECULATIVE-DECODING` / current Ch48 / legacy Ch44；已读 Ch23～25、Ch47～49。`Emerging / Experimental — Refine Candidate`。Open questions：independent runtime、per-step acceptance、rollback semantics、KV invalidation、quality-matched goodput和能源成本。

### Agent Lightning

- **Candidate / Week / Score / Source Family:** Agent Lightning / 2025-W32 / 29/30 / `ARXIV-2508.03680-AGENT-LIGHTNING`；arXiv v1 2025-08-05 17:50 UTC，截至 2026-08-24 无后续 arXiv revision。Direct sources 为 v1 论文、Microsoft 官方 repository/docs；artifact revision 必须绑定 commit。
- **Access / Full-read Coverage:** 已读 MDP/interface、LightningRL credit assignment、Training-Agent Disaggregation、runtime、OpenTelemetry trajectory、text-to-SQL/RAG/math experiments、discussion及附录；跨任意 Agent 的生产稳定性与安全隔离尚无证据。
- **Problem / Previous Design / Changed Constraint:** 将整条 Agent transcript 拼成训练 sequence 并 mask 非模型 token，在固定单 Agent loop 中简单；多 Agent、动态 workflow、多模型/tool call 会混淆谁产生 action、reward 应归给谁以及 runtime 如何与 trainer 升级解耦。
- **Mechanism / State / Flow:** 每次 LLM call 视作 action，state snapshot、semantic variables、model/tool name/version/endpoint/sampling parameters 与 observation 组成统一 transition；OpenTelemetry 捕获 execution trace，credit module把 workflow trajectory 分解为可训练 transitions。controller/server 负责训练与 rollout orchestration，client/runtime 保持原 Agent execution。
- **Implementation / Evaluation Contract:** 三类任务跨 LangChain、OpenAI Agents SDK、AutoGen/自建 runtime；比较 base/SFT/RL 并给学习曲线。框架“almost zero code modification”是作者集成结果，不代表 tool authorization、trace completeness 或 reward correctness自动成立；hardware、precision、fleet concurrency、trace loss、tail latency与生产 SLO未完整披露。
- **Evidence / Limits / Trade-offs:** 支持 trajectory schema、observability 与 trainer/runtime disaggregation能降低框架耦合，并在作者任务中带来回报提升；不证明 arbitrary Agent 都满足 MDP/credit assumptions。统一 trace 增加可训练性和审计，也新增 PII/secret capture、span loss、version drift、credit leakage及 replay side effect。
- **Evolution / Owner / Decision:** `concatenated transcript → typed transition ledger → credit decomposition → disaggregated trainer/runtime`。Owner `AGENT-PLATFORM` / current Ch84 / legacy Ch80，handoff `AGENT-WORKFLOW` / current Ch81 / legacy Ch77、`TRAIN-RLHF` / current Ch31 / legacy Ch27；已读 Ch80～84、Ch30～33。`Refine — Existing Argument Candidate`；Books Gate关闭。Open questions：trace redaction、exactly-once reward、multi-agent attribution、off-policy freshness、rollback与tenant isolation。

### Training Long-Context, Multi-Turn SWE Agents with RL

- **Candidate / Week / Score / Source Family:** SWE Agent RL / 2025-W32 / 27/30 / `ARXIV-2508.03501-SWE-AGENT-RL`；arXiv v1 2025-08-05 14:30 UTC，v2 2025-10-10。W32 的机制与评分以 v1 为准，v2 仅作为同族后续 revision 核验；SWE-rebench、SWE-bench Verified 与公开 scaffold 为 related primary sources。
- **Access / Full-read Coverage:** 已读 problem formulation、RFT、modified DAPO、multi-turn environment、65K→131K curriculum、training/evaluation、ablations和appendices；训练代码、exact cluster、container image与 checkpoint未完整公开。
- **Problem / Previous Design / Changed Constraint:** 单轮数学/代码 RL 可把答案视作一个 action sequence，binary verifier便宜；真实 repo repair 要在 stateful filesystem/test environment 中循环行动，observation 会改变下一步，长 trajectory 还受 context和环境 nondeterminism约束。
- **Mechanism / State / Flow:** Qwen2.5-72B-Instruct 先从成功 trajectories做 rejection fine-tuning，再以每题多条完整 rollout、modified DAPO group advantage和 length penalty做 RL；训练从65K扩到131K context，并过滤全成/全败 groups。repo snapshot、tool schema、container/test result、trajectory、policy/reference版本都是 reward identity。
- **Implementation / Evaluation Contract:** SWE-rebench 训练集经正确性、复杂度与 deterministic test过滤；论文报告基线约11%，RFT约20%，RL在 SWE-bench Verified 约39%，并在相同 scaffold 比较 open-weight models。结果绑定 Qwen2.5-72B、作者 harness、tool budget与benchmark snapshot；training hardware/precision、并发、wall-clock/TCO、variance和 contamination residual不完整。
- **Evidence / Limits / Trade-offs:** 支持 RFT 建立协议能力后，environment-coupled RL 可提高该 scaffold 下 repair success；不证明 RL 普遍优于更多 SFT、39% 等于生产 mergeability，也不隔离长 context、data filtering与RL各自贡献。收益以昂贵 sandbox rollout、flaky tests、reward hacking、context truncation和 side effect recovery为代价。
- **Evolution / Owner / Decision:** `single-turn verifier RL → successful-trajectory RFT → stateful multi-turn RL → long-context curriculum`。Owner `AGENT-WORKFLOW` / current Ch81 / legacy Ch77，training handoff `TRAIN-GRPO` / current Ch33 / legacy Ch29；已读 Ch32～34、Ch78～82。`Emerging / Experimental — Refine Candidate`。Open questions：reproducible environment image、test flakiness、compute-matched SFT、rollback、security sandbox与真实 PR acceptance。

### VeriGUI（v1；后续 revision 改名为 VeriWeb）

- **Candidate / Week / Score / Source Family:** VeriGUI / 2025-W32 / 25/30 / `ARXIV-2508.04026-VERIGUI-DATASET`；arXiv v1 2025-08-06 02:38 UTC，v2 2026-02-27 将标题改为 *VeriWeb: Verifiable Long-Chain Web Benchmark for Agentic Information-Seeking*，并将公开对象重构为 302 个 web information-seeking tasks。W32 owner、评分和机制证据严格绑定 v1 VeriGUI；v2 是同一 identifier 的重大 revision，不另行重复计分。
- **Access / Full-read Coverage:** 已读 v1 PDF/TeX 的 long-chain construction、subtask decomposition/verifiers、desktop/web trajectories、agent evaluation、limitations与artifact说明，并核对 v2 metadata、标题、范围和 302-task 声明的 revision delta；official GitHub/Hugging Face artifact 只在能固定 event-time commit/hash 时支持 v1。不得把 v2 的 web-only范围、任务数或后续数据倒灌为 event-time v1事实。
- **Problem / Previous Design / Changed Constraint:** outcome-only短任务 benchmark易复算，适合验证单步工具能力；数百步 GUI workflow 中最终失败无法定位，且从起点重跑使恢复/局部规划不可测。
- **Mechanism / State / Flow:** 人工将 long-horizon goal 分解为相互依赖、可从任一 subtask 起步的 checkpoints，并为每个 subgoal定义可执行 verifier；agent action更新 GUI/environment state，verifier提交 checkpoint outcome，后续 subtask消费已验证state。canonical state由 environment拥有，标注只定义可观测 contract。
- **Implementation / Evaluation Contract:** 数据覆盖 desktop/web，多种 foundation model/agent在 success rate与 completion/progress类指标上比较；作者观察 long-chain能力明显不足。模型/API snapshot、UI版本、网络条件、retry、并发、延迟、人工标注一致性和完整统计需随dataset revision冻结。
- **Evidence / Limits / Trade-offs:** 证明 subtask-level executable evidence比单一 terminal label提供更可定位的 evaluation contract；不证明 subtasks 完全独立、不证明 verifier覆盖所有副作用或高分Agent可安全部署。细粒度 verifier增加标注与维护成本，并可能奖励局部完成而忽略全局 invariant；短、原子、强终态任务仍适合 outcome-only。
- **Evolution / Owner / Decision:** `terminal success → milestone state → executable subtask verifier → resumable workflow evaluation`。Owner `PLATFORM-EVALUATION-SYSTEM` / current Ch66 / legacy Ch62，handoff `AGENT-WORKFLOW` / current Ch81 / legacy Ch77；已读 Ch65～67、Ch80～82。`Refine — Existing Argument Candidate`。Open questions：event-time dataset hash、verifier false positive、hidden side effects、resume semantics和版本漂移。

### SEAgent

- **Candidate / Week / Score / Source Family:** SEAgent / 2025-W32 / 27/30 / `ARXIV-2508.04700-SEAGENT`；arXiv v1 2025-08-06 17:58 UTC，v2 2025-08-12。W32 全文审计绑定 v1，v2 作为同族次周 revision，不倒灌；Direct sources 为 versioned arXiv 全文和 official repository。
- **Access / Full-read Coverage:** 已读 autonomous exploration、World State Model、Curriculum Generator、failure imitation/GRPO、specialist-to-generalist、OSWorld experiments、sensitivity、prompts、algorithm和broader impacts；真实桌面安全、长期 retention与independent replication未验证。
- **Problem / Previous Design / Changed Constraint:** human demos在固定软件版本中可靠，但新/专用软件缺标签且 GUI持续变化；仅 terminal reward无法说明哪一步引入失败。
- **Mechanism / State / Flow:** Actor执行任务；World State Model读取完整 state/action trajectory，生成 state-change caption和逐步判断；Curriculum Generator维护可更新 software guidebook并生成更难任务；成功action以typed distance reward+GRPO强化，失败action用negative/adversarial imitation远离。先训练specialists，再把成功轨迹SFT蒸馏为generalist并继续multi-software RL。
- **Implementation / Evaluation Contract:** 基于 UI-TARS、五个 OSWorld professional apps；作者报告11.3%→34.5%，并比较 direct generalist、specialists及loss/curriculum sensitivity。数字绑定其软件镜像、task generator、reward model与rollout protocol；hardware、precision、并发、成本、seed/CI和环境更新未充分披露。
- **Evidence / Limits / Trade-offs:** 支持 derived guidebook+step reward+specialist curriculum在作者环境改善成功率；不证明“无人工监督”（base model、OSWorld、verifier training仍含人工先验），也不证明 world-state judge可靠等于环境真值。self-generated tasks可扩展，却会累积 judge hallucination、curriculum collapse、guidebook poisoning、specialist interference和危险操作。
- **Evolution / Owner / Decision:** `human demos → autonomous exploration → derived guidebook → verifier-coupled curriculum → specialist-to-generalist`。Owner `AGENT-MEMORY` / current Ch77 / legacy Ch73，workflow handoff `AGENT-WORKFLOW` / current Ch81 / legacy Ch77、GRPO handoff `TRAIN-GRPO` / current Ch33 / legacy Ch29；已读 Ch76～78、Ch80～82、Ch32～34。`Emerging / Experimental — Refine Candidate`。Open questions：guidebook provenance/delete、reward calibration、environment rollback、安全授权和跨版本 transfer。

### CompassVerifier

- **Candidate / Week / Score / Source Family:** CompassVerifier / 2025-W32 / 27/30 / `ARXIV-2508.03686-COMPASSVERIFIER`；arXiv v1 2025-08-05 17:55 UTC，截至 2026-08-24 无后续 arXiv revision。Direct sources 为 v1 论文、OpenCompass repository、VerifierBench dataset/model artifacts。
- **Access / Full-read Coverage:** 已读 verifier taxonomy、data/meta-error construction、training、multi-domain evaluation、ablation、outcome-reward experiments、appendix与artifact docs；event-time commit/hash与所有 judge calls需在复现时冻结。
- **Problem / Previous Design / Changed Constraint:** regex/exact match在结构稳定答案上确定且便宜，general LLM judge能覆盖开放格式但昂贵、prompt-sensitive；多子题、公式、sequence和异常输出使 reward/evaluation parser成为共享故障点。
- **Mechanism / State / Flow:** VerifierBench收集多源model outputs并由人工分析 meta-error patterns扩充；轻量 verifier接收 question/reference/candidate与answer type，输出正确性/异常判断，既可服务离线 evaluation也可作为 outcome reward。dataset split、normalizer、verifier checkpoint、prompt/schema与abstain policy共同定义 evidence identity。
- **Implementation / Evaluation Contract:** 论文跨 math、knowledge、reasoning、多种 answer types与 abnormal responses比较规则、通用LLM及专用 verifier，并做data/model ablation；公开结果只证明给定 benchmark分布。硬件、batch/concurrency、延迟/SLO、API judge snapshot、跨语言/OOD与校准曲线不完整。
- **Evidence / Limits / Trade-offs:** 支持专用 typed verifier可减少重复规则并在作者 benchmark提高准确性；不证明它是 ground truth，也不证明用同一 verifier训练和评测不会 reward hacking。统一 verifier降低维护分散，却形成单点偏差、version drift、overfitting和 false-positive release风险；强类型任务仍应优先 executable verifier。
- **Evolution / Owner / Decision:** `exact matcher → prompted judge → typed learned verifier → versioned verifier ensemble/abstention`。Owner `PLATFORM-EVALUATION-SYSTEM` / current Ch66 / legacy Ch62，training handoff `TRAIN-RLHF` / current Ch31 / legacy Ch27 与 `TRAIN-GRPO` / current Ch33 / legacy Ch29；已读 Ch65～67、Ch30～34。`Refine — Existing Argument Candidate`。Open questions：calibration/abstention、independent gold、judge leakage、event-time artifact hash、latency和dual-use reward governance。

### R-Zero

- **Candidate / Week / Score / Source Family:** R-Zero / 2025-W32 / 27/30 / `ARXIV-2508.05004-RZERO`；arXiv v1 2025-08-07，v2 2025-08-27、v3 2026-01-09、v4 2026-02-13。W32 的方法、实验与评分绑定 v1；后续版本仅作同族 revision 节点，不将新增模型、数据或结论倒灌。Direct sources 为 versioned paper 与作者 artifacts。
- **Access / Full-read Coverage:** 已读 challenger/solver formulation、alternating optimization、task filtering、reward、multi-backbone experiments、ablations、limitations和appendices；“zero data”仅指无预置 task/label，不等于无 pretrained prior、grader或人工设计。
- **Problem / Previous Design / Changed Constraint:** curated math/reasoning data提供稳定监督，但覆盖上限受人类题库；无约束 self-play又会生成过易、不可解或不可验证任务。
- **Mechanism / State / Flow:** 从同一 base 初始化独立 Challenger 与 Solver；Challenger因提出靠近 Solver 能力边界且可验证的任务获奖，Solver因解题获奖，二者交替更新形成自适应 curriculum。task文本、difficulty estimate、verifier outcome、model checkpoint和round id必须作为训练state，防止用未来solver重写历史难度。
- **Implementation / Evaluation Contract:** 作者在多个 backbone 与 math/general reasoning benchmark报告提升，包括 Qwen3-4B-Base 的作者结果；比较若干 data/self-training baselines并做round/role消融。训练compute、污染检测、verifier false positives、长期回合稳定性、seed/CI、硬件/precision和TCO不完整。
- **Evidence / Limits / Trade-offs:** 支持 adversarial/co-evolving curriculum在列示配置中生成有用训练信号；不证明能力可无限自举、不证明问题新颖或超出 pretrained distribution，也不证明 Challenger/Solver互不共谋。减少人工题库依赖，却新增 reward collusion、difficulty drift、mode collapse、无效题和 verifier exploitation；高风险/领域任务仍需 curated authoritative data。
- **Evolution / Owner / Decision:** `static curriculum → model-generated tasks → capability-boundary challenger → co-evolving solver`。Owner `TRAIN-RLHF` / current Ch31 / legacy Ch27，handoff `AGENT-MULTI-AGENT` / current Ch82 / legacy Ch78；已读 Ch30～34、Ch81～83。`Emerging / Experimental — Refine Candidate`。Open questions：novelty audit、verifier governance、role collapse、compute-matched synthetic-data baseline和长期稳定性。

### Dynamic Fine-Tuning

- **Candidate / Week / Score / Source Family:** On the Generalization of SFT / Dynamic Fine-Tuning / 2025-W32 / 26/30 / `ARXIV-2508.05629-DFT`；arXiv v1 2025-08-07，v2 2025-10-16、v3 2026-02-27（ICLR 2026）。W32 结论绑定 v1，后续理论、实验或venue状态只作 revision evidence。Direct sources 为 versioned paper 与 official code repository。
- **Access / Full-read Coverage:** 已读 SFT-as-policy-gradient derivation、reward rectification、token probability rescaling、experiments、offline-RL comparison、ablations和appendices；理论解释与 empirical benefit分开处理。
- **Problem / Previous Design / Changed Constraint:** token cross-entropy稳定、简单且有确定 teacher target，但容易让低概率 token产生过大的相对更新，并把数据频率隐式当reward；OOD/generalization需求使每 token gradient权重成为 design choice。
- **Mechanism / State / Flow:** DFT按当前 policy 对 teacher token 的概率动态重标 objective，使 token update不再等同固定 imitation weight；data sequence→forward probabilities→per-token rescale→loss/backprop。概率必须来自与梯度一致的 model/version/precision，detach与数值clamp决定其真实优化行为。
- **Implementation / Evaluation Contract:** 作者跨多个 base model与reasoning/instruction benchmark比较标准SFT、DFT和offline-RL，并给 weighting ablation；“single-line change”不代表无系统代价，概率权重会影响 mixed precision、sequence reduction与distributed reproducibility。完整硬件、global batch、seed/CI、data contamination、长期 stability和cost不全。
- **Evidence / Limits / Trade-offs:** 证据支持该 rescaling 在作者 data/model上改善列示 generalization；不证明标准SFT的唯一问题是隐式reward，也不证明 DFT普遍替代 SFT/RL。它保留离线训练简洁性，却增加 policy-dependent weighting、早期低质量概率反馈、数值敏感与 objective drift；高质量窄域 imitation仍可用标准SFT。
- **Evolution / Owner / Decision:** `uniform teacher-token CE → policy-aware token weighting → offline reward rectification`，是 SFT 的 alternative branch，不是 RL 的通用替代。Owner `TRAIN-SFT` / current Ch29 / legacy Ch25，handoff `TRAIN-RLHF` / current Ch31 / legacy Ch27；已读 Ch28～32。`Emerging / Experimental — Refine Candidate`。Open questions：detach/clamp、sequence-length bias、calibration、distributed parity、compute-matched baselines与跨domain replication。

### VeOmni

- **Candidate / Week / Score / Source Family:** VeOmni / 2025-W32 / 27/30 / `ARXIV-2508.02317-VEOMNI`；arXiv v1 2025-08-04、v2 2025-08-05、v3 2025-08-07，三版都在 W32 window 内并归同一 Source Family；全文审计以 v3 收束当周 revision，不能重复评分。Direct sources 为 versioned paper 与 ByteDance official repository/docs。
- **Access / Full-read Coverage:** 已读 model-centric recipe abstraction、3D parallelism、heterogeneous modality integration、implementation、scaling/evaluation和appendices；event-time code commit、完整 fault recovery与production support matrix需冻结。
- **Problem / Previous Design / Changed Constraint:** 把 TP/PP/DP逻辑写入每个 model在单模态固定结构中直接，但 omni-modal encoder/connector/decoder、MoE和不同sequence shape使组合爆炸，communication与module边界难复用。
- **Mechanism / State / Flow:** 以 model/module topology描述可切分单元，用 recipe zoo将 compute graph映射到 DP/TP/PP等 communication plan，尽量把并行逻辑从模型定义解耦；modality batch→各 encoder→connector/token stream→LLM/MoE，recipe controller拥有 placement/group/collective identity，checkpoint需记录model与parallel layout。
- **Implementation / Evaluation Contract:** 作者报告30B omni-modal MoE在128 GPU、160K context下扩展，并给 throughput/scaling comparisons；2,800 tokens/s/GPU需绑定其模型、GPU、precision、sequence mix、batch和并行配置，不能外推。网络拓扑、failure/restart、heterogeneous load variance、成本/能耗与CI不完整。
- **Evidence / Limits / Trade-offs:** 支持“model-centric recipe”降低多模态模型与并行实现耦合，并在作者集群工作；不证明任意 model/modality零改动，也不证明不同 topology上的最优性。抽象提升复用，却新增 planner correctness、recipe/version compatibility、collective deadlock、load imbalance和 checkpoint migration；结构稳定的小模型仍适合显式并行代码。
- **Evolution / Owner / Decision:** `model-embedded parallelism → reusable distributed recipe → modality-aware placement`。Owner `TRAIN-DISTRIBUTED-TRAINING` / current Ch36 / legacy Ch32，handoff `TRAIN-TENSOR-PARALLEL` / current Ch37 / legacy Ch33 与 `MULTIMODAL-REPRESENTATION` / current Ch23 / legacy N/A；已读 Ch23、Ch35～41。`Refine — Existing Argument Candidate`。Open questions：event-time commit、recipe legality checks、elastic recovery、checkpoint remap、network sensitivity与independent scaling。

### ToolTrain

- **Candidate / Week / Score / Source Family:** Tool-integrated RL for Repo Deep Search / ToolTrain / 2025-W32 / 25/30 / `ARXIV-2508.03012-TOOLTRAIN`；arXiv v1 2025-08-05、v2 2025-08-06，均在 W32 window 内并归同一 Source Family；全文审计以 v2 收束当周 revision，不能重复评分。Direct sources 为 versioned paper 与 official repository/artifacts。
- **Access / Full-read Coverage:** 已读 repo-deep-search formulation、rejection-sampled SFT、tool-integrated RL、retrieval tools、issue-localization/end-to-end evaluation、ablations与appendix；artifact snapshot与sandbox image需复现时固定。
- **Problem / Previous Design / Changed Constraint:** embedding/BM25一次检索在局部 bug和明确符号上便宜；真实 issue 与代码之间存在多跳依赖，Agent需根据前一步结果继续搜索、停止并提交 location。
- **Mechanism / State / Flow:** 第一阶段保留成功 tool trajectories做 SFT，第二阶段让 policy在 repository environment中调用 search/navigation tools并以 localization/outcome reward优化。repo commit、index version、tool schema/result、query history、token budget、final file/function location构成 trajectory identity；retriever不是无状态 API。
- **Implementation / Evaluation Contract:** 作者在 issue localization与 end-to-end resolution任务比较 agent/model baselines，并报告32B模型在其 function-level harness超过 Claude-3.7；该数字绑定 repository split、scaffold、tool budget、grader和model snapshot。硬件、precision、并发/latency、token/TCO、test flakiness与confidence不完整。
- **Evidence / Limits / Trade-offs:** 支持显式训练 search policy可改善该 repo-deep-search任务，并可能传导到 repair；不证明 localization提升必然产生正确patch，也不证明工具RL优于更强index/context。多步搜索减少单次retrieval盲点，却增加tool成本、loop、stale index、reward shortcut、权限与prompt-injection风险；小repo/明确symbol仍可静态检索。
- **Evolution / Owner / Decision:** `one-shot retrieval → successful tool-trajectory SFT → environment-coupled search RL → localization-to-repair handoff`。Owner `AGENT-TOOL-CALLING` / current Ch78 / legacy Ch74，RAG handoff `AGENT-RAG` / current Ch76 / legacy Ch72、workflow handoff `AGENT-WORKFLOW` / current Ch81 / legacy Ch77；已读 Ch75～79、Ch80～82。`Emerging / Experimental — Refine Candidate`。Open questions：commit/index identity、tool authorization、search-budget fairness、compute-matched long-context baseline和真实review acceptance。

### AttnTrace

- **Candidate / Week / Score / Source Family:** AttnTrace / 2025-W32 / 23/30 / `ARXIV-2508.03793-ATTNTRACE`；arXiv v1 2025-08-05，v2 2026-04-10、v3 2026-04-17（IEEE S&P 2026）。W32 方法与评分绑定 v1，后续 venue/revision 只作演进核验。Direct sources 为 versioned paper 与 official code。
- **Access / Full-read Coverage:** 已读 attention traceback construction、两项修正、theoretical discussion、context-attribution evaluation、prompt-injection application、ablations和appendix；attention availability限制适用模型范围。
- **Problem / Previous Design / Changed Constraint:** leave-one-out/perturbation traceback能近似回答“哪段 context影响输出”，但对长 context需大量forward；直接平均attention便宜却受layer/head/token聚合与attention-not-explanation问题影响。
- **Mechanism / State / Flow:** 从生成过程中已有 attention weights构建 source-span contribution，并用文中校正处理生成token与context位置关系；prompt/context span→single generation trace→attention aggregation→ranked spans→可选 detection。trace必须绑定model/checkpoint、prompt tokenization、layer/head规则、generation output和runtime是否暴露权重。
- **Implementation / Evaluation Contract:** 作者比较 TracLLM等 traceback baseline，在多种长context设置报告accuracy/latency，并演示 attribution-before-detection定位 injected instruction；硬件、kernel、precision、batch/concurrency、KV setting、完整tail latency和production SLO不全。
- **Evidence / Limits / Trade-offs:** 支持该 attention heuristic在作者任务比列示perturbation baseline快且更准；不证明 attention具有因果解释、不证明高 attribution即事实evidence，也不能用它自动授权删除上下文。复用权重降低额外forward，却增加白盒依赖、聚合偏差、model-version drift和 adversarial attention manipulation；安全关键归因仍需 perturbation/executable checks。
- **Evolution / Owner / Decision:** `black-box perturbation → white-box attention heuristic → attribution-assisted detection`，属于 explanatory evidence而非 truth proof。Owner `PLATFORM-OBSERVABILITY` / current Ch67 / legacy Ch63，security handoff `PLATFORM-SECURITY` / current Ch72 / legacy Ch68、context handoff `AGENT-CONTEXT` / current Ch75 / legacy Ch71；已读 Ch66～68、Ch71～72、Ch74～76。`Emerging / Experimental — No Change Candidate`。Open questions：causal validation、closed-model fallback、trace storage/privacy、adversarial robustness与runtime overhead。

### TensorRT-LLM v0.21.0

- **Candidate / Week / Score / Source Family:** TensorRT-LLM v0.21.0 / 2025-W32 / 26/30 / `GITHUB-NVIDIA-TENSORRTLLM-V0.21.0`；official release 2025-08-04。v1.0.0rc5同日吸收0.21 train并作related preview，不重复评分。
- **Access / Full-read Coverage:** 已读 official announcement、release notes、full changelog入口、known issues及相关feature docs/PR links；未把 main branch后续行为当成 event-time 0.21事实。
- **Problem / Previous Design / Changed Constraint:** 单模型单节点 engine可逐项启用量化、speculation和KV管理；large-scale EP、PD disaggregation、NIXL/fabric memory与多种 attention/speculation组合后，“支持某功能”不代表组合正确。
- **Mechanism / State / Flow:** 0.21增加large-scale EP、disaggregated service中的NIXL、fabric-memory KV transfer、W4A8 MXFP4/FP8与rowwise FP8、Qwen3 disaggregation/EAGLE3、chunked/sliding-window kernels等。release同时披露 disaggregation+MTP+overlap scheduler可能accuracy错误，以及Llama4 Hopper >8K性能回退；因此 feature tuple、model、backend、quantization、hardware与scheduler应形成typed execution-plan identity。
- **Implementation / Evaluation Contract:** release notes是版本事实，不是统一benchmark；没有同一模型/硬件/长度/batch/concurrency/SLO下对每项功能的完整收益。fix/known issue证明组合测试是runtime contract的一部分，不能从功能列表推断生产性能。
- **Evidence / Limits / Trade-offs:** 证明0.21公开支持这些路径并存在明确不兼容/回退；不证明NIXL、fabric KV或FP8在任意fleet更快、更准。更丰富组合提高覆盖，却扩大 compatibility matrix、warmup/graph、KV transfer、numeric parity与rollback状态；简单稳定模型仍应使用较少 feature tuple。
- **Evolution / Owner / Decision:** `single-engine optimization → disaggregated data plane → typed feature-combination contract`。Owner `INFER-TENSORRT-LLM` / current Ch49 / legacy Ch45，handoff `INFER-SPECULATIVE-DECODING` / current Ch48 / legacy Ch44 与 `INFER-SCHEDULING` / current Ch56 / legacy Ch52；已读 Ch47～50、Ch54～56。`Weekly Only — Version Fact / Refine Candidate`；Books Gate关闭。Open questions：event-time compatibility matrix、per-combination tests、NIXL failure recovery、KV ownership、accuracy canary和rollback。

## Sub-20 Source, Date and Rejection Closure

下列候选均已回到 primary identity 核对首次公开日；评分低于 20 不代表内容错误，而是本轮不承担长期 owner。后续 revision 若出现新机制，作为同一 Source Family 的演进节点重新评估。

| Candidate | Source Family / primary identifier / v1 | Score | Rejection closure |
| --- | --- | ---: | --- |
| Goedel-Prover-V2 | arXiv:2508.03613 / 2025-08-05 | 19 | formal-proof domain的重要实现，但本周证据未改变通用 training/evaluation contract。 |
| TRACEALIGN | arXiv:2508.02063 / 2025-08-04 | 18 | 保留理论/经验边界；没有足够 artifact 与跨设置验证形成 owner。 |
| IFDecorator | arXiv:2508.04632 / 2025-08-06 | 19 | instruction-following data方法是受限 training case，长期独立性不足。 |
| Skywork UniPic | arXiv:2508.03320 / 2025-08-05 | 19 | image generation/editing统一案例，未改变 Ch24 已有条件分支。 |
| Beyond the Trade-off | arXiv:2508.02150 / 2025-08-04 | 18 | self-supervised instruction-following RL为作者设置结果，reward外推不足。 |
| Trainable Dynamic Mask Sparse Attention | arXiv:2508.02124 / 2025-08-04 | 19 | 1.7B/作者训练设置下有效，未形成可迁移 kernel/runtime contract。 |
| Sparse-dLLM | arXiv:2508.02558 / 2025-08-04 | 18 | cache eviction与diffusion acceleration保留为 Seed Diffusion 邻接案例，证据较弱。 |
| Dynaword | arXiv:2508.02271 / 2025-08-04 | 18 | dynamic tokenization案例；token identity、serving compatibility和独立复现不足。 |
| Sculptor | arXiv:2508.04664 / 2025-08-06 | 18 | active context管理是Agent策略案例，未改变 context owner 的长期结论。 |
| CoAct-1 | arXiv:2508.03923 / 2025-08-06 | 18 | coding-as-action是computer-use分支，未给足安全/latency与跨环境证据。 |
| InfiAlign | arXiv:2508.05496 / 2025-08-07 | 19 | alignment data pipeline值得归档，但没有改变 data/provenance contract。 |
| DeepPHY | arXiv:2508.05405 / 2025-08-07 | 19 | physics-grounded video生成只在作者评测成立，不能等同可控world transition。 |
| Genie Envisioner | arXiv:2508.05635 / 2025-08-07 | 19 | embodied imagination案例；闭环environment causality与sim-to-real未闭合。 |
| CellForge | arXiv:2508.02276 / 2025-08-04 | 16 | AI-for-Science domain workflow；multi-agent headline不替代可执行artifact验证。 |
| HarmonyGuard | arXiv:2508.04010 / 2025-08-06 | 19 | web-agent safety/utility case；policy extraction、authority和attack coverage不足。 |
| Learning to Reason for Factuality | arXiv:2508.05618 / 2025-08-07 | 19 | 多目标reward揭示precision/detail/relevance trade-off，但仍依赖自动factuality evaluator。 |
| ChartCap | arXiv:2508.03164 / 2025-08-05 | 16 | chart-caption dataset/metric是domain case，不把作者hallucination下降外推。 |
| StepFun-Formalizer | arXiv:2508.04440 / 2025-08-06 | 16 | formalization model/data fact；不形成通用系统机制owner。 |
| MiDashengLM | arXiv:2508.03983 / 2025-08-06 | 17 | audio-language release；TTFT/throughput只在作者硬件协议下成立。 |
| LeanK | arXiv:2508.02215 / 2025-08-04 | 18 | K-channel pruning是KV优化分支；缺跨模型、kernel和SLO证据。 |
| Double-Bench document RAG evaluation | arXiv:2508.03644 / 2025-08-05 | 19 | 组件级证据与无support仍回答现象值得保留，但benchmark snapshot不改变通用evidence框架。 |
| Sotopia-RL | arXiv:2508.03905 / 2025-08-05 | 18 | utterance-level multi-dimensional reward为social-agent domain case，judge validity受限。 |
| VLM RL in synthetic worlds | arXiv:2508.04280 / 2025-08-06 | 18 | synthetic→real benchmark transfer有限；真实control-loop与安全包络未验证。 |
| Agentic e-commerce evaluation | arXiv:2508.02630 / 2025-08-04 | 19 | ACES提供受控因果实验，但属于marketplace domain harness，不直接改变Agent runtime。 |
| Multi-agent document QA / MACT | arXiv:2508.03404 / 2025-08-05 | 18 | 缺compute-matched single-agent headroom与生产协作成本，保持domain case。 |

## Cross-Week Owner Spillback Ledger

以下 17 项由 W32 discovery页发现，但 v1/首次公开日不属于 2025-08-04～2025-08-10；本周不计分、不重复建立 Full Source Review，交由 owner Weekly 处理：

| Source Family / identifier | First public | Owner week | W32 decision |
| --- | --- | --- | --- |
| CoT Mirage / arXiv:2508.01191 | 2025-08-02 | 2025-W31 | Spillback；不按HF推荐日归档。 |
| Cognitive Kernel-Pro / arXiv:2508.00414 | 2025-08-01 | 2025-W31 | Spillback。 |
| Efficient Agents / arXiv:2508.02694 | 2025-07-24 | 2025-W30 | Spillback。 |
| Beyond Fixed / arXiv:2508.00819 | 2025-08-01 | 2025-W31 | Spillback。 |
| SitEmb-v1.5 / arXiv:2508.01959 | 2025-08-03 | 2025-W31 | Spillback。 |
| LiveMCPBench / arXiv:2508.01780 | 2025-08-03 | 2025-W31 | Spillback。 |
| Representation Shift / arXiv:2508.00367 | 2025-08-01 | 2025-W31 | Spillback。 |
| InstructVLA / arXiv:2507.17520 | 2025-07-23 | 2025-W30 | Spillback。 |
| A Glimpse to Compress / arXiv:2508.01548 | 2025-08-03 | 2025-W31 | Spillback。 |
| SWE-Exp / arXiv:2507.23361 | 2025-07-31 | 2025-W31 | Spillback。 |
| SWE-Debate / arXiv:2507.23348 | 2025-07-31 | 2025-W31 | Spillback。 |
| Cyber-Zero / arXiv:2508.00910 | 2025-08-02 | 2025-W31 | Spillback。 |
| RL-PLUS / arXiv:2508.00222 | 2025-07-31 | 2025-W31 | Spillback。 |
| FACTORY / arXiv:2508.00109 | 2025-07-31 | 2025-W31 | Spillback。 |
| Dens3R / arXiv:2507.16290 | 2025-07-22 | 2025-W30 | Spillback；从W32低分账本移除。 |
| RoboMemory / arXiv:2508.01415 | 2025-08-02 | 2025-W31 | Spillback；从W32低分账本移除。 |
| Web-CogReasoner / arXiv:2508.01858 | 2025-08-03 | 2025-W31 | Spillback；从W32低分账本移除。 |

## Evidence Level

- **Official / Artifact Verified:** gpt-oss、GPT-5公开系统边界、TensorRT-LLM v0.21.0 release/known issues；只证明公开接口、artifact和版本事实。
- **Author Experimental:** 13个论文 family 的机制、ablation和结果；未等同独立复现，benchmark必须绑定各自model/hardware/precision/length/batch/concurrency/SLO披露情况。
- **Version Fact / Mechanism Not Disclosed:** GPT-5 router内部结构、训练目标、误路由率与production SLO；不得由产品行为反推。
- **Project Inference:** Source Family演进、state ownership和canonical owner是基于primary evidence的系统归纳，已与论文事实分开。

## Cross-Week Deduplication

- 17项 HF W32 discovery结果已按v1回拨W30/W31，详见 spillback ledger；featured/submission date不再误作event date。
- GLM-4.5 report与W31 release同属`GLM-4.5-2508.06471`，本周只补充report evidence，不建立第二个family。
- TensorRT-LLM v0.21.0与同日v1.0.0rc5按同release train去重；0.21为stable event owner，rc5是related preview。
- gpt-oss公告、model card、weights与malicious fine-tuning report合成一个family；GPT-5 product/developer/system card亦合成一个family。
- VeriGUI v1 与 2026-02-27 改名、重构后的 VeriWeb v2 共用 arXiv:2508.04026；W32只使用 v1 证据，v2不新建候选也不反写 v1 dataset事实。
- VeOmni v1/v2/v3 与 ToolTrain v1/v2 的 revisions 均发生在本周，分别合成一个 Source Family、一个评分行。

## Knowledge Tree Position

- `PLATFORM-SECURITY` Ch72 / legacy Ch68：gpt-oss open-weight responsibility transfer。
- `INFER-SCHEDULING` Ch56 / legacy Ch52：GPT-5 route-as-evidence；router mechanism Not Disclosed。
- `TRAIN-RLHF` Ch31 / legacy Ch27：GLM-4.5 multi-domain RL、R-Zero challenger-solver curriculum。
- `MULTIMODAL-REPRESENTATION` Ch23、`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24：Qwen-Image与Seed Diffusion。
- `TRAIN-SFT` Ch29 / legacy Ch25：Dynamic Fine-Tuning alternative branch。
- `TRAIN-DISTRIBUTED-TRAINING` Ch36 / legacy Ch32：VeOmni model-centric recipe。
- `INFER-TENSORRT-LLM` Ch49 / legacy Ch45：TensorRT-LLM typed feature-combination contract。
- `PLATFORM-EVALUATION-SYSTEM` Ch66 / legacy Ch62：VeriGUI与CompassVerifier。
- `PLATFORM-OBSERVABILITY` Ch67 / legacy Ch63：AttnTrace evidence boundary。
- `AGENT-MEMORY` Ch77 / legacy Ch73：SEAgent derived guidebook。
- `AGENT-TOOL-CALLING` Ch78 / legacy Ch74：ToolTrain。
- `AGENT-WORKFLOW` Ch81 / legacy Ch77：SWE Agent RL。
- `AGENT-PLATFORM` Ch84 / legacy Ch80：Agent Lightning trajectory/trainer contract。

## Recommended Action

- **Refine candidates after Historical Books Gate:** gpt-oss、GPT-5、Qwen-Image、Agent Lightning、SWE Agent RL、VeriGUI、SEAgent、CompassVerifier、R-Zero、Dynamic Fine-Tuning、VeOmni、ToolTrain。
- **Emerging / Experimental:** Seed Diffusion；保留parallel proposal/commit机制与严格workload boundary。
- **No Change / bounded case:** GLM-4.5 report、AttnTrace；现有章节已覆盖主结论，保留新证据边界。
- **Weekly Only / Version Fact:** TensorRT-LLM v0.21.0；只有通过Books Gate后才能抽象为feature-combination contract，不能复制release功能表。

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

`Historical Books Gate Closed`。本轮只闭合 Weekly evidence；16项20+候选均得到 provisional disposition和Stable Node owner，但不得据此宣称Books已吸收，也未修改任何Books文件。

## Pending, Blocked and Gate Ledger

- `Review Pending: 0`：41/41周内评分行均有最终source/date/score/disposition。
- `Full Source Review: 16/16`：所有20+候选均完成非模板化机制、state/control flow、implementation、evaluation、evidence boundary、trade-off、owner与open-question复核。
- `Sub-20 Closure: 25/25`：均完成primary identity、v1日期、评分和拒绝理由。
- `Cross-Week Spillback: 17/17 routed`：W30/W31 owner已明确；本文件不重复计分。
- `Unverified / Blocked: 0`：本轮被计分候选的paper/report/release正文均可取得；没有以摘要替代20+ Full Source Review。
- `Disputed: 0 family-level`：作者benchmark/理论主张的限制已在各review内按claim级边界记录，没有未决身份或日期冲突。
- `Discovery Gap: 0 within fixed replay`：固定机构、arXiv/学术索引和AI Infra release lane已重放；这不是对全球论文的数学穷尽证明。
- `Historical Weekly Evidence Gate: Pass`；`Historical Books Gate: Closed`。

## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。
- HF upvote/featured ranking只用于发现，不进入评分；不同硬件、prompt、tool和grader下的速度/榜单不做横向合并。

## Repository Changes

- 幂等重建 `papers/2025/weekly/2025-W32/README.md`：评分账本由3项扩展为41项，Full Source Review由3项扩展为16项，并新增25项低分闭合与17项spillback ledger。
- 纠正旧的“Books Gate已完成”冲突状态；本阶段未修改Books、年度索引、Learning State或ROADMAP。

## Open Questions

- gpt-oss 的 open-weight ownership transfer 与 instruction-hierarchy weakness 是否需修正 Ch68，待 Books Gate。
- GPT-5 router 没有公开误路由评测；可沉淀 route-as-evidence 原则，但不得反推内部算法。
- Seed Diffusion的quality-matched goodput、mutable token commit/KV invalidation能否独立复现？
- Agent Lightning与SWE Agent RL的trace completeness、credit assignment、sandbox exactly-once和off-policy freshness如何校准？
- VeriGUI v1/VeriWeb v2 与 CompassVerifier 如何发布 event-time dataset/verifier hash、revision migration、abstention与false-positive release policy？
- VeOmni recipe legality、elastic checkpoint remap和heterogeneous modality load如何形成production contract？
- TensorRT-LLM feature-combination matrix能否成为machine-readable admission/canary/rollback input？

## Sources

- gpt-oss announcement/model card — https://openai.com/index/introducing-gpt-oss/ ; https://cdn.openai.com/pdf/419b6906-9da6-406c-a19d-1bb078ac7637/oai_gpt-oss_model_card.pdf（2025-08-05；Accessed 2026-08-24）
- GPT-5 system/developer sources — https://cdn.openai.com/gpt-5-system-card.pdf ; https://openai.com/index/introducing-gpt-5-for-developers/（2025-08-07；Accessed 2026-08-24）
- Qwen-Image — https://arxiv.org/abs/2508.02324（v1 2025-08-04；Accessed 2026-08-24）
- Seed Diffusion — https://arxiv.org/abs/2508.02193（v1 2025-08-04；Accessed 2026-08-24）
- Agent Lightning — https://arxiv.org/abs/2508.03680（v1 2025-08-05；Accessed 2026-08-24）
- SWE Agent RL — https://arxiv.org/abs/2508.03501（v1 2025-08-05；v2 2025-10-10；Accessed 2026-08-24）
- VeriGUI v1 / VeriWeb v2 — https://arxiv.org/abs/2508.04026（v1 2025-08-06；v2 renamed/reworked 2026-02-27；Accessed 2026-08-24）
- SEAgent — https://arxiv.org/abs/2508.04700（v1 2025-08-06；v2 2025-08-12；Accessed 2026-08-24）
- CompassVerifier — https://arxiv.org/abs/2508.03686（v1 2025-08-05；Accessed 2026-08-24）
- R-Zero — https://arxiv.org/abs/2508.05004（v1 2025-08-07；v2 2025-08-27；v3 2026-01-09；v4 2026-02-13；Accessed 2026-08-24）
- Dynamic Fine-Tuning — https://arxiv.org/abs/2508.05629（v1 2025-08-07；v2 2025-10-16；v3 2026-02-27；Accessed 2026-08-24）
- VeOmni — https://arxiv.org/abs/2508.02317（v1 2025-08-04；v2 2025-08-05；v3 2025-08-07；Accessed 2026-08-24）
- ToolTrain — https://arxiv.org/abs/2508.03012（v1 2025-08-05；v2 2025-08-06；Accessed 2026-08-24）
- AttnTrace — https://arxiv.org/abs/2508.03793（v1 2025-08-05；v2 2026-04-10；v3 2026-04-17；Accessed 2026-08-24）
- GLM-4.5 technical report — https://arxiv.org/abs/2508.06471（v1 2025-08-08；Accessed 2026-08-24）
- TensorRT-LLM v0.21.0 — https://github.com/NVIDIA/TensorRT-LLM/discussions/6606 ; https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/release-notes.md（2025-08-04；Accessed 2026-08-24）
- Sub-20 primary papers — https://arxiv.org/abs/2508.03613 ; https://arxiv.org/abs/2508.02063 ; https://arxiv.org/abs/2508.04632 ; https://arxiv.org/abs/2508.03320 ; https://arxiv.org/abs/2508.02150 ; https://arxiv.org/abs/2508.02124 ; https://arxiv.org/abs/2508.02558 ; https://arxiv.org/abs/2508.02271 ; https://arxiv.org/abs/2508.04664 ; https://arxiv.org/abs/2508.03923 ; https://arxiv.org/abs/2508.05496 ; https://arxiv.org/abs/2508.05405 ; https://arxiv.org/abs/2508.05635 ; https://arxiv.org/abs/2508.02276 ; https://arxiv.org/abs/2508.04010 ; https://arxiv.org/abs/2508.05618 ; https://arxiv.org/abs/2508.03164 ; https://arxiv.org/abs/2508.04440 ; https://arxiv.org/abs/2508.03983 ; https://arxiv.org/abs/2508.02215 ; https://arxiv.org/abs/2508.03644 ; https://arxiv.org/abs/2508.03905 ; https://arxiv.org/abs/2508.04280 ; https://arxiv.org/abs/2508.02630 ; https://arxiv.org/abs/2508.03404（Accessed 2026-08-24）
- Discovery index — https://huggingface.co/papers/week/2025-W32（仅用于发现与去重；Accessed 2026-08-24）
