# AI Research Weekly — 2025-W32

> Coverage Window: 2025-08-04～2025-08-10
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 3 项长期证据：gpt-oss、GPT-5、GLM-4.5 technical report。重点是约束、机制、trade-off 与演进，不是发布热度。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；后续修订回链首次公开周。
- Scholar、OpenAlex、DBLP 负责 discovery/去重；论文事实回到正文。Crossref 仅交叉检验 metadata。
- 历史回填不创建 Daily；Accessed 统一为 2026-07-31。
- 作者/厂商 benchmark 缺少完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外模型公司、研究机构与 Hugging Face Blog。

- 保留：gpt-oss（2025-08-05）。
- 保留：GPT-5（2025-08-07）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1 正文核验。

- 保留：GLM-4.5 technical report（2025-08-08）。

## 3. AI Infra 与工程项目

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → Dynamo → TensorRT-LLM → Ray → KServe → Kubeflow → Kubernetes → Hugging Face → DeepSpeed → Megatron-LM → llama.cpp → ONNX Runtime → OpenXLA 扫描。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| gpt-oss | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Must Read；联合模型卡与 safety paper 全文复核 |
| GPT-5 | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Worth Watching；只作为 inference policy 信号 |
| GLM-4.5 technical report | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；不重复计算为第二个 Books 事件 |

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
- **ROADMAP Node:** Ch20～21、Ch31、Ch45～46、Ch62、Ch68、Ch74。
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
- **ROADMAP Node:** Ch20、Ch38、Ch52、Ch62、Ch68、Ch74～77。
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
- **ROADMAP Node:** Ch21、Ch23～25、Ch27～29、Ch32～35、Ch45～48、Ch52、Ch62、Ch74～77。
- **Target and Adjacent Chapters Read:** 已阅读 Ch20～30、Ch31～35、Ch44～48、Ch51～52、Ch61～63、Ch73～77；W31 release与本packet最终只选一个Books主owner。
- **Existing Coverage:** Ch21已有routing/load trade-off，Ch29已有group-relative reward边界，Ch45～48已有precision/runtime contract，Agent chapters已有environment ownership。潜在新增点是training-vs-rollout precision转换与multi-domain RL state，而非榜单或model规格。
- **Integration Decision:** `No Change — Already Covered`；training/rollout precision、MoE routing 与 agent workflow 已由 Ch21/24/29/45/77 的 contracts 覆盖。
- **Changed Files or Rejection Reason:** 不改 Books；保留报告为 bounded model-system case。
- **Open Questions:** training topology/checkpoint、loss-free balance sensitivity、FP8 rollout parity、mode contamination、sandbox isolation与independent reproduction。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / technical report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系是本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper v1 与后续集成若日期不同，分别记录证据角色，但只建立一个 Books source packet。
- 新方案不静默覆盖旧方案；记录新增状态、成本和 failure modes。

## Knowledge Tree Position

- gpt-oss → 第 20、21、23～25、29、45、46、68 章（Direct Evolution）
- GPT-5 → 第 20、52、62、68、74～77 章（Direct Evolution）
- GLM-4.5 technical report → 第 20、21、29、45、46、74 章（Layering / Dependency）

## Recommended Action

- gpt-oss：Must Read；联合模型卡与 safety paper 全文复核
- GPT-5：Worth Watching；只作为 inference policy 信号
- GLM-4.5 technical report：Must Read；不重复计算为第二个 Books 事件

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。

## Repository Changes

- 新增 papers/2025/weekly/2025-W32/README.md。
- 新增 3 个候选级 Full Source Review；本阶段未修改 Books。

## Open Questions

- gpt-oss 的 open-weight ownership transfer 与 instruction-hierarchy weakness 是否需修正 Ch68，待 Books Gate。
- GPT-5 router 没有公开误路由评测；可沉淀 route-as-evidence 原则，但不得反推内部算法。
- GLM-4.5 的 loss-free balance、BF16/FP8 rollout 与多域 RL 需和现有章节逐项去重。

## Sources

- gpt-oss — https://openai.com/index/introducing-gpt-oss/（First Public: 2025-08-05；Accessed: 2026-07-31）
- gpt-oss model card — https://cdn.openai.com/pdf/419b6906-9da6-406c-a19d-1bb078ac7637/oai_gpt-oss_model_card.pdf（Published: 2025-08-05；Accessed: 2026-07-31）
- GPT-5 system card — https://cdn.openai.com/gpt-5-system-card.pdf（Published: 2025-08-07；Accessed: 2026-07-31）
- GPT-5 for developers — https://openai.com/index/introducing-gpt-5-for-developers/（Published: 2025-08-07；Accessed: 2026-07-31）
- GLM-4.5 technical report — https://arxiv.org/abs/2508.06471（First Public: 2025-08-08；Accessed: 2026-07-31）
