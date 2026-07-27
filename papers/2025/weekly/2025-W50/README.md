# AI Research Weekly — 2025-W50

> Coverage Window: 2025-12-08～2025-12-14
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 2 项长期证据：Differentially private chatbot-use analytics、GPT-5.2。重点是约束、机制、trade-off 与演进关系。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；revision 回链 first-public week。
- Scholar、OpenAlex、DBLP 用于 discovery/去重；论文回到正文。Crossref 只做 metadata 交叉检验。
- 历史回填不创建 Daily；Accessed 为 2026-07-31。
- benchmark 缺完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外一线模型公司、研究机构与 Hugging Face Blog。

- 保留：Differentially private chatbot-use analytics（2025-12-10）。
- 保留：GPT-5.2（2025-12-11）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1/官方论文正文。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按固定工程项目顺序扫描训练、编译、推理、平台与硬件 runtime。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Differentially private chatbot-use analytics | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；与 Monitoring/Security 建立可观测性边界 |
| GPT-5.2 | 4 | 4 | 3 | 4 | 4 | 3 | 22/30 | Record Only；无公开新机制 |

### Deep Analysis 1 — Differentially private chatbot-use analytics

- First Public: 2025-06-05（paper v1）；2025-12-10（Google Research follow-up）
- Status: Google Research official follow-up to an earlier primary paper
- Primary Source: https://research.google/blog/a-differentially-private-framework-for-gaining-insights-into-ai-chatbot-use/
- Evolution Relationship: Direct Evolution

#### Why

线上聊天遥测能改进产品，却可能泄露高敏感 prompt；传统聚合不足以给出个体贡献边界。

#### Principle and Mechanism

研究把 DP aggregation、taxonomy/classification 与统计发布组合为 usage-insight pipeline。

#### Trade-off and Evidence Boundary

形式化隐私降低个体泄露风险，也引入噪声、稀有群体抹除、taxonomy bias 与审计成本。

#### Connection and Evolution

知识树位置：第 62、63、68 章。Must Read；与 Monitoring/Security 建立可观测性边界。进入 Books 时保留旧方案条件，并区分官方事实、作者实验和本项目推断。

### Deep Analysis 2 — GPT-5.2

- First Public: 2025-12-11
- Status: Official proprietary release + system card
- Primary Source: https://openai.com/index/introducing-gpt-5-2/
- Evolution Relationship: Direct Evolution

#### Why

long-running agent 与 professional artifact 评测继续推动更高 reasoning budget，但发布数字高度依赖 tools、judge 和 task definition。

#### Principle and Mechanism

官方材料披露模型族、reasoning effort、tool calling 与 system card；内部机制未知。

#### Trade-off and Evidence Boundary

能力提升不等于可靠自治；更长 context/effort 增加 cost、latency 和 judge uncertainty。

#### Connection and Evolution

知识树位置：第 52、62、74～77 章。Record Only；无公开新机制。进入 Books 时保留旧方案条件，并区分官方事实、作者实验和本项目推断。

## Full Source Review

### Differentially private chatbot-use analytics

- **Candidate / Week / Score:** Differentially private chatbot-use analytics / 2025-W50 / 25/30。
- **Source Family ID:** `GOOGLE-URANIA-DP-TEXT-2025`。
- **Source Type:** Google Research official Blog、arXiv primary paper及algorithm appendices。
- **First-public Date / Revision History:** Urania paper v1 2025-06-05，已在W23加入source-family chronology pointer；2025-12-10 Blog为production-facing research synthesis。本周候选保留为official follow-up evidence，不重算机制首次公开。
- **Direct Primary Sources:** arXiv:2506.04681 HTML全文；Google Research Blog。
- **Related Primary Sources:** Google DP clustering library、DP partition selection/histogram论文；用于核验privacy composition。
- **Access and Verification Status:** Verified；真实production deployment、user-level adjacency、完整runtime cost Not Disclosed。
- **Full-read Coverage:** 已阅读全文metadata、formal problem/DP定义、Simple-Clio、Urania algorithm/theorem、四种keyword选择、evaluation setup/results/discussion、limitations/future work、formal appendices、privacy attack与prompts。
- **Original Problem:** chatbot conversation analytics需要输出可读主题，但LLM去PII、k-anonymity式大cluster和LLM auditor只是heuristic，无法给单条记录贡献的formal bound。
- **Why the Previous Design Was Reasonable:** heuristic summarization可保留丰富语义且实现简单；当数据低敏或只做内部探索时，formal DP的效用损失与复杂度未必值得。
- **Changed Constraint:** 高敏prompt、对外发布insights与模型版本漂移要求privacy guarantee不能依赖某个LLM“按提示不泄露PII”。
- **Mechanism:** conversation先独立生成summary/embedding；DP k-means只发布centers，record再assign；cluster size经DP histogram/threshold；每record最多贡献5个keywords，DP histogram/partition selection选词；最终LLM只根据DP keywords生成summary，依post-processing得到端到端record-level DP。keyword set若由private data生成，额外privacy budget必须composition。
- **State Ownership:** data controller定义record/adjacency与budget；DP clustering/histogram拥有随机机制与accounting events；LLM只做per-record transform或DP output post-processing；release layer不得发布内部record-to-summary mapping。
- **Control Flow / Data Flow:** private conversations → per-record summary/embedding → DP centers → internal assignment → noised size/threshold → bounded keyword contributions+DP release → LLM summary；用于evaluation的record映射不允许release。
- **Implementation Details:** KwSet-TFIDF、KwSet-LLM满足DP但各自消耗budget；KwSet-Public依赖public corpus；Hybrid用public seed再对private candidates做partition selection。Theorem 4.1通过composition与post-processing给出总budget。
- **Evaluation Setup:** LMSYS-1M-Chat，Gemini-2.0-Flash-001；KwSet-Public使用WildChat；比较Simple-Clio，自动lexical/topic/embedding、LLM pairwise与membership-inference-style attack。
- **Baselines / Ablations / Sensitivity:** privacy从较松到较紧时topic coverage从0.723降至0.078，cluster约3700降至300；同privacy下keyword strategy显著改变utility。作者也指出LLM偏好private summary但独立质量均约1.4/5，定性样例显示specificity丢失。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** LLM/dataset与部分privacy settings披露；hardware、precision、corpus规模的完整filter、batch/concurrency、wall-clock、cost/SLO Not Disclosed。
- **What the Evidence Actually Proves:** 证明可把LLM当DP post-processing与bounded keyword operator组合，给最终summary set formal record-level guarantee；也证明privacy会非均匀抹除topic/minority utility。
- **What It Does Not Prove:** 不提供user-level/cross-session DP，不证明semantic summary高质量，不证明LLM evaluator可靠，也不证明production可扩展或跨周期budget已解决。
- **Limitations / Threats to Validity:** first-public归档错误需修正；public dataset、Simple-Clio proxy ground truth、LLM judge bias、record-level而非user-level、稀有topic系统性丢失、经验attack很弱。
- **Trade-offs / New Failure Modes:** formal privacy换来noise、small-cohort suppression、taxonomy/keyword bias、budget composition、distribution shift与semantic broadening；内部mapping误发布会破坏guarantee边界。
- **Where the Previous Design Still Applies:** 低敏内部分析、需要细粒度debug或小样本topic时heuristic/manual access可在严格访问控制下使用；formal DP适合对外/广泛共享的aggregate release。
- **Evolution Relationship:** `Direct Evolution`：prompt-based redaction/k-anonymity heuristic → DP aggregate primitives → LLM post-processing；LLM没有提供privacy，privacy来自前置机制与release contract。
- **ROADMAP Node:** Ch62、Ch63、Ch68。
- **Target and Adjacent Chapters Read:** 已读 Ch62～69；Ch68 为 privacy/telemetry 主 owner。
- **Existing Coverage:** Ch68 provisional已写DP telemetry与taxonomy bias；必须核对是否明确record vs user adjacency、internal mapping与post-processing边界。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch68，保留 telemetry adjacency、taxonomy bias 与 post-processing 边界。
- **Changed Files or Rejection Reason:** 已复核 `books/part-05-ai-infrastructure/68-security.md`。
- **Open Questions:** user-level adjacency、跨周composition、minority utility、taxonomy drift、内部mapping访问控制与production cost。

### GPT-5.2

- **Candidate / Week / Score:** GPT-5.2 / 2025-W50 / 22/30。
- **Source Family ID:** `OPENAI-GPT-5.2-2025-12`。
- **Source Type:** official model/product announcement、Deployment Safety Hub system-card update。
- **First-public Date / Revision History:** 2025-12-11；system card声明旧模型comparison使用其latest versions，不能与各自launch数值直接比较。
- **Direct Primary Sources:** OpenAI announcement；GPT-5.2 system-card update全文。
- **Related Primary Sources:** GPT-5/GPT-5.1 system cards与Preparedness Framework；只用于继承mitigation，不反推新架构。
- **Access and Verification Status:** Verified for公开model family、evaluation与safety deployment；architecture、参数、训练算力、runtime internals Not Disclosed。
- **Full-read Coverage:** 已阅读announcement的model variants、reasoning effort、tools与professional/agent eval setup；阅读全文system-card update的数据/训练类别、baseline safety、jailbreak/prompt injection、CoT、preparedness、bio/cyber/AI self-improvement与limitations/statistical caveats。
- **Original Problem:** professional artifact与长时agent tasks需要更高test-time compute和tool scaffold，但benchmark improvement易被误写成新的系统机制或可靠自治。
- **Why the Previous Design Was Reasonable:** 固定reasoning budget/短benchmark便于cost与latency治理；model-only安全测试更易比较。
- **Changed Constraint:** 用户任务跨度更长、工具更多、artifact更复杂，模型提供多个reasoning effort，评测也引入最长1000 turns、24～100小时environment等scaffold。
- **Mechanism:** 公开事实仅为Instant/Thinking等model variants、reasoning effort与tool support；system card说reasoning models用RL学习内部CoT。更具体architecture/training/runtime mechanism未披露。
- **State Ownership:** model拥有generation；API/product拥有effort/tool interface；agent harness拥有environment/turn budget；safety system拥有classifiers/monitoring；grader拥有success definition。
- **Control Flow / Data Flow:** task+effort/tools → model rollout → environment/hidden tests → grader；preparedness eval在不同scaffold、turn/time预算下测能力，因此score是system-level observation。
- **Implementation Details:** system card将Thinking在Bio/Chem按High capability处理并启用相应safeguards；cyber与AI self-improvement未达High。它明确评测是能力下界，更多scaffolding可能提高结果。
- **Evaluation Setup:** production safety benchmarks故意选困难失败样本，error rate不代表平均traffic；cyber range可达1000 turns；OpenAI PRs用pre-PR repo+CLI/Python+hidden tests；MLE-Bench给GPU并允许24h/部分100h。
- **Baselines / Ablations / Sensitivity:** comparisons混用latest prior-model versions；没有公开model architecture/training ablation或effort-token/cost/latency完整curve。bootstrap CI可能低估小数据problem-level variance。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model variants和部分context/effort设置由产品页给出；hardware、precision、batch/concurrency、TTFT/ITL、P95/P99与生产SLO Not Disclosed。
- **What the Evidence Actually Proves:** 发布了特定model family并在明确scaffold下完成能力/安全评测；system card对评测选择偏差、下界与不确定性给出重要边界。
- **What It Does Not Prove:** 不公开新架构，不证明benchmark等于可靠自治，也不证明相对旧模型数字为launch-to-launch可比。
- **Limitations / Threats to Validity:** proprietary model、vendor/internal tasks、scaffold和grader依赖、旧model版本漂移、小样本CI与极长rollout成本。
- **Trade-offs / New Failure Modes:** 更高effort增加capability同时增加latency/cost、tool side effects、long-horizon drift、monitoring load与tail-risk；product routing使归因更复杂。
- **Where the Previous Design Still Applies:** 严格SLO、低风险或简单任务继续使用低effort/小模型/显式workflow；长agent scaffold不应成为默认路径。
- **Evolution Relationship:** `Direct Evolution`：fixed model call → effort-routed reasoning → long-horizon tool scaffold；新增的是system operating point，不是公开的新模型机制。
- **ROADMAP Node:** Ch52、Ch62、Ch74～77。
- **Target and Adjacent Chapters Read:** 已读 Ch52、Ch62、Ch74～77；无公开新机制，按版本事实去重。
- **Existing Coverage:** Ch52、Ch62 与 Ch77 已明确 effort/scaffold/route 属完整 subject identity；本候选没有公开新机制。
- **Integration Decision:** `Weekly Only — Version/Product Fact / Mechanism Not Disclosed`。
- **Changed Files or Rejection Reason:** 不改 Books；effort/scaffold attribution 已由 Ch52/62/77 的 subject identity 覆盖。
- **Open Questions:** effort-token/latency曲线、model vs scaffold消融、production routing、long-rollout side effects与monitorability。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系为本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper、model card 与工程集成按证据角色回链，不重复形成 Books 观点。
- 新方案不覆盖旧方案；保留适用条件、新增状态与 failure modes。

## Knowledge Tree Position

- Differentially private chatbot-use analytics → 第 62、63、68 章（Direct Evolution）
- GPT-5.2 → 第 52、62、74～77 章（Direct Evolution）

## Recommended Action

- Differentially private chatbot-use analytics：Must Read；与 Monitoring/Security 建立可观测性边界
- GPT-5.2：Record Only；无公开新机制

## Event-Date Daily Decision

历史回填不创建 Daily；证据直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、榜单、缺条件 benchmark 与无新机制的价格/可用性变化。
- 不以“更新”自动否定旧设计。

## Repository Changes

- 新增 papers/2025/weekly/2025-W50/README.md。
- 本周候选已完成最终 Books disposition；实际章节修改或拒绝理由见各候选的 `Changed Files or Rejection Reason`。

## Open Questions

- DP telemetry 的 taxonomy drift、small-cohort utility 与跨周期 composition 仍需持续审计。
- GPT-5.2 的内部训练与 runtime 机制未知，不从能力数字反推系统设计。

## Sources

- Differentially private chatbot-use analytics — https://research.google/blog/a-differentially-private-framework-for-gaining-insights-into-ai-chatbot-use/（First Public: 2025-12-10；Accessed: 2026-07-31）
- Urania — https://arxiv.org/abs/2506.04681（v1: 2025-06-05；Accessed: 2026-07-31）
- Urania HTML — https://arxiv.org/html/2506.04681（Accessed: 2026-07-31）
- GPT-5.2 — https://openai.com/index/introducing-gpt-5-2/（First Public: 2025-12-11；Accessed: 2026-07-31）
- GPT-5.2 system-card update — https://deploymentsafety.openai.com/gpt-5-2（Published: 2025-12-11；Accessed: 2026-07-31）
