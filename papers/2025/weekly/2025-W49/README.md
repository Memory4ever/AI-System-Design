# AI Research Weekly — 2025-W49

> Coverage Window: 2025-12-01～2025-12-07
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 3 项长期证据：DeepSeek-V3.2、Mistral 3、Google Research 对 Titans + MIRAS 的官方综合说明。Titans 与 MIRAS 的首次论文事件分别回链 W01 和 W16，本周只记录机构级解释与证据补强。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；revision 回链 first-public week。
- Scholar、OpenAlex、DBLP 用于 discovery/去重；论文回到正文。Crossref 只做 metadata 交叉检验。
- 历史回填不创建 Daily；Accessed 为 2026-07-31。
- benchmark 缺完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外一线模型公司、研究机构与 Hugging Face Blog。

- 保留：Mistral 3（2025-12-02）。
- 保留：Google Research synthesis of Titans + MIRAS（2025-12-04；follow-up evidence）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1/官方论文正文。

- 保留：DeepSeek-V3.2（2025-12-01 release；2025-12-02 paper v1）。

## 3. AI Infra 与工程项目

按固定工程项目顺序扫描训练、编译、推理、平台与硬件 runtime。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| DeepSeek-V3.2 | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Must Read；全文审查后优先 refine Long Context/Inference/Agent handoff |
| Mistral 3 | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Worth Watching；作为 cost-quality portfolio 信号 |
| Google Research synthesis of Titans + MIRAS | 3 | 4 | 4 | 5 | 4 | 2 | 22/30 | Worth Watching；回链 W01/W16，不重复计算首次公开机制 |

### Deep Analysis 1 — DeepSeek-V3.2

- First Public: 2025-12-01 (release); 2025-12-02 (paper v1)
- Status: Official release + arXiv v1 + model card
- Primary Source: https://arxiv.org/abs/2512.02556
- Evolution Relationship: Direct Evolution

#### Why

V3.2-Exp 的 DSA 只有在完整模型训练、长上下文 serving 与 thinking-in-tool-use 中同时成立，才构成从 research mechanism 到系统 contract 的演进。

#### Principle and Mechanism

报告组合 DeepSeek Sparse Attention、scalable RL 与 thinking integrated tool use，并披露训练/evaluation/limitations；需与 W08 NSA、W40 Exp 联读。

#### Trade-off and Evidence Boundary

稀疏注意力降低长上下文计算，但新增 indexer、kernel、cache state 与质量风险；大规模 RL 改善 reasoning/tool use，也增加 rollout infrastructure 与 evaluator dependence。作者对 frontier 模型的比较不外推。

#### Connection and Evolution

知识树位置：第 14、22、29、39～41、45、46、50、74 章。Must Read；全文审查后优先 refine Long Context/Inference/Agent handoff。进入 Books 时保留旧方案条件，并区分官方事实、作者实验和本项目推断。

### Deep Analysis 2 — Mistral 3

- First Public: 2025-12-02
- Status: Official open-weight model-family release
- Primary Source: https://mistral.ai/news/mistral-3/
- Evolution Relationship: Layering / Dependency

#### Why

模型族用 dense small models 与 large sparse MoE 覆盖不同部署预算，提示架构选择应由 workload/SLO 而非“最大模型”驱动。

#### Principle and Mechanism

官方发布披露模型族和参数结构；benchmark 为厂商报告。

#### Trade-off and Evidence Boundary

多尺寸改善选择空间，也增加 evaluation、routing、quantization 和生命周期矩阵。

#### Connection and Evolution

知识树位置：第 21、45、46、66 章。Worth Watching；作为 cost-quality portfolio 信号。进入 Books 时保留旧方案条件，并区分官方事实、作者实验和本项目推断。

### Deep Analysis 3 — Google Research synthesis of Titans + MIRAS

- First Public: 2025-12-04（官方综合说明；Titans/MIRAS 论文 first-public 分属 W01/W16）
- Status: Google Research official follow-up + primary-paper links
- Primary Source: https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/
- Evolution Relationship: Layering / Dependency

#### Why

attention 保留精确上下文但成本随长度增长；固定状态 RNN/SSM 线性扩展却压缩过强。长期记忆需要在精确访问与在线压缩间建立新层次。

#### Principle and Mechanism

官方说明将 Titans 的 test-time neural memory 与 MIRAS 的四维设计空间放进同一研究路线，并补充研究团队对两者关系的解释；具体机制与实验仍以 W01/W16 的论文正文为准。

#### Trade-off and Evidence Boundary

online learning 扩展记忆容量，却新增更新稳定性、污染、遗忘、回滚、并发 session ownership 和可解释性问题；论文结果仍为作者实验。

#### Connection and Evolution

知识树位置：第 14、22、73 章。Worth Watching；作为 W01/W16 Source Packet 的机构级解释，不创建第二套 Books 观点。

## Full Source Review

### DeepSeek-V3.2

- **Candidate / Week / Score:** DeepSeek-V3.2 / 2025-W49 / 29/30。
- **Source Family ID:** `DEEPSEEK-NSA-DSA-V3.2-2025`（W08 NSA → W40 V3.2-Exp/DSA → W49 V3.2）。
- **Source Type:** official model release/model card、arXiv technical report、official artifacts。
- **First-public Date / Revision History:** release 2025-12-01、paper v1 2025-12-02；paper 2025-12-05版本修正RoPE layout mismatch。revision事实不回写为v1已经正确。
- **Direct Primary Sources:** arXiv:2512.02556 HTML全文；DeepSeek official release/model cards与GitHub artifacts。
- **Related Primary Sources:** W08 NSA论文、W40 V3.2-Exp Source Review；DSA同架构机制只在family中解释一次。
- **Access and Verification Status:** Verified；训练硬件数量/拓扑、完整数据与部分environment实现 Not Disclosed。
- **Full-read Coverage:** 已阅读全文metadata/revisions、background、DSA method/algorithm、two-stage training、scalable GRPO、agent task synthesis/environment、thinking-in-tool-use、evaluation setup/tables/ablation/context management、limitations、appendices与官方artifact。
- **Original Problem:** 长上下文dense attention成本高；大规模reasoning RL受off-policy、MoE routing与rollout mask影响；agent训练还需要真实可验证环境，而非只扩充文本CoT。
- **Why the Previous Design Was Reasonable:** dense MLA提供稳定精确attention；标准GRPO和短任务环境实现简单；每轮隐藏thinking可控制context。规模较小时额外indexer/environment orchestration成本不值得。
- **Changed Constraint:** 128K context、1T级MoE、海量rollout与百步tool tasks使attention compute、routing drift、environment throughput与context management成为共同瓶颈。
- **Mechanism:** DSA用轻量lightning indexer选择top-2048 token，再对MLA latent KV做sparse attention；从dense checkpoint经2.1B-token dense warmup与943.7B-token sparse stage迁移。RL采用corrected unbiased KL、negative sequence mask、Keep Routing与Keep Sampling Mask；agent训练保留tool message间reasoning，环境含真实/合成任务与verifier。
- **State Ownership:** indexer拥有token-selection scores；attention/KV runtime拥有latent KV与sparse gather；MoE router/learner共同约束sample/train route；agent harness拥有tool history、context policy、environment与verifier。
- **Control Flow / Data Flow:** prefill生成index scores与latent KV → top-k gather → sparse attention；RL rollout记录tokens/routes/masks → learner按约束更新；agent轨迹在tool message间保留reasoning，新user message重置相关state。
- **Implementation Details:** indexer本身仍O(L²)但小维度/FP8以降低成本；DSA与main attention loss分离；报告说明某些把tool result模拟成user message的framework不适合thinking mode并建议non-thinking。
- **Evaluation Setup:** context128K、temperature1；general/reasoning/coding/search/tool benchmarks有逐项harness；agent训练表列约24,667 code、50,275 search、4,417 general、5,908 code-interpreter environments/tasks（类别含real/synthetic）。
- **Baselines / Ablations / Sensitivity:** dense attention、V3.2-Exp、frontier model comparisons；context management对BrowseComp从51.4（不处理）到67.6（discard-all），summary策略平均60.2且约364 steps，证明harness policy是强混杂变量。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/128K/context、indexer FP8与top-k=2048等已披露；训练GPU数量/互连、serving batch/concurrency、TTFT/ITL、SLO与全部序列分布 Not Disclosed。
- **What the Evidence Actually Proves:** 在作者checkpoint、训练与harness下，DSA可从dense MLA迁移并支撑完整模型；RL稳定化与agent environment是独立于架构的系统机制；context policy会显著改变agent得分。
- **What It Does Not Prove:** 不证明sparse attention普遍优于dense/其他方法、不证明frontier benchmark superiority可外推，也不证明environment规模等于production reliability。
- **Limitations / Threats to Validity:** 作者实验、revision中RoPE bug、vendor/internal harness、知识差距、token效率、困难任务仍弱；sparse index quality与kernel/runtime生态依赖。
- **Trade-offs / New Failure Modes:** 节省长序列attention compute，却新增indexer训练/版本、top-k miss、sparse gather/kernel、cache identity、dense fallback；RL新增route/mask coupling；agent新增verifier漏洞、context truncation与环境漂移。
- **Where the Previous Design Still Applies:** 短上下文、低并发、质量优先或缺成熟sparse kernel时dense MLA合理；简单RL不必引入Keep Routing；短tool任务可显式workflow而不保留隐藏reasoning。
- **Evolution Relationship:** `Direct Evolution`：NSA研究 → DSA experimental checkpoint → full-model V3.2 + scalable RL + agent environment；每层解决不同约束，不是单一路径全面替代。
- **ROADMAP Node:** Ch14、Ch22、Ch29、Ch39～41、Ch45～46、Ch50、Ch74。
- **Target and Adjacent Chapters Read:** 已读 Ch21～23、Ch28～30、Ch38～52、Ch73～75；Ch22 为 sparse-attention 主 owner。
- **Existing Coverage:** provisional Ch22已写sparse index/staged migration，Ch73有边界handoff；必须以全文重新审计是否遗漏RL/agent state或写成过度泛化。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch22，确认 NSA→DSA→full-model staged evolution；Ch52 只接 runtime policy。
- **Changed Files or Rejection Reason:** 已复核 `books/part-02-model/22-long-context.md`；agent/RL 产品结果不倒灌为 sparse-attention 机制。
- **Open Questions:** independent sparse-kernel证据、indexer质量监控与fallback、cache identity、route replay、context policy可比性。

### Mistral 3

- **Candidate / Week / Score:** Mistral 3 / 2025-W49 / 23/30。
- **Source Family ID:** `MISTRAL-3-FAMILY-2025-12`。
- **Source Type:** official model-family announcement/model docs、后续official arXiv paper。
- **First-public Date / Revision History:** model family 2025-12-02；Ministral 3 architecture/training paper arXiv v1为2026-01-13。后续论文作为Source Family补强，不倒写为2025发布时已公开。
- **Direct Primary Sources:** Mistral announcement与model docs/cards；arXiv:2601.08584 HTML全文（仅覆盖Ministral 3 dense family，不覆盖Large 3训练细节）。
- **Related Primary Sources:** vLLM/TensorRT-LLM/SGLang support release；只证明compatibility，不证明性能。
- **Access and Verification Status:** Verified for release facts与Ministral 3 paper；Mistral Large 3完整architecture/training mechanism仍Not Disclosed。
- **Full-read Coverage:** 已阅读release的3B/8B/14B dense与675B/41B-active MoE portfolio、license/hardware/inference claims；阅读全文Ministral paper的architecture、Cascade Distillation、pruning、short/long context、SFT/ODPO/GRPO、evaluations、teacher/verbosity ablations与conclusion。
- **Original Problem:** 同一组织为edge与frontier workload分别从零训练多尺寸模型成本高；“最大模型”也无法满足local memory、latency、license和quality的组合约束。
- **Why the Previous Design Was Reasonable:** 独立从零训练允许每个尺寸优化data/architecture且避免teacher bias；单旗舰简化评测、routing和lifecycle。
- **Changed Constraint:** 多deployment tier需要一组可授权、可量化模型；训练预算要求从已有teacher复用能力，同时reasoning与chat verbosity目标不同。
- **Mechanism:** release用3/8/14B dense与675B total/41B active sparse MoE构成portfolio。后续Ministral paper提出Cascade Distillation：从MS3.1逐级prune-distill-repeat，层按activation norm ratio、hidden维按PCA、FFN维按activation importance裁剪；16K短context后用YaRN扩到262K；instruct走SFT+ODPO，reasoning走SFT+GRPO+ODPO。
- **State Ownership:** model lifecycle层拥有teacher/student lineage与variant矩阵；training pipeline拥有prune/distill/RL stages；serving layer拥有量化、hardware placement和route；业务router拥有workload/SLO选择。
- **Control Flow / Data Flow:** parent checkpoint → prune到目标shape → teacher-logit distill短context → 作为下一child起点/长context扩展 → 分叉instruct或reasoning post-training → 独立部署/路由。
- **Implementation Details:** dense models为GQA/RoPE/SwiGLU/RMSNorm、256K，冻结410M ViT并重训projection；reasoning最大generation在RL中从32K增至80K。Large 3只公开MoE规模、H200训练与若干format，不公开同等深度recipe。
- **Evaluation Setup:** Ministral paper内部统一harness比较Qwen/Gemma，base/instruct/reasoning使用不同benchmark；reasoning报告pass@16（LiveCodeBench pass@5）。release的Large 3/portfolio claims缺同等完整methodology。
- **Baselines / Ablations / Sensitivity:** paper比较不同teacher强度/阶段、base vs post-trained teacher、long-CoT比例与ODPO；显示更强teacher在pretraining未必更好、post-training却受益，long CoT提升STEM但导致反思/回退/冗长。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Large 3训练称3000 H200，Ministral规格/256K已披露；训练tokens/FLOPs、Ministral硬件、servingprecision/batch/concurrency/TTFT/ITL不完整。NVFP4运行claim不是通用SLO。
- **What the Evidence Actually Proves:** portfolio应按workload contract选择；Ministral作者实验支持逐级prune/distill及teacher-task匹配比“teacher越强越好”更关键，并揭示reasoning quality与verbosity trade-off。
- **What It Does Not Prove:** 不证明Mistral 3整体cost-quality最优、不证明Large 3 mechanism等同Ministral、不证明paper中2026披露在2025已知，也不证明vendor benchmark普遍成立。
- **Limitations / Threats to Validity:** paper晚于事件、作者/internal harness、training compute细节不足、Large 3机制缺失、3B对hyperparameter更敏感、long-CoT副作用。
- **Trade-offs / New Failure Modes:** 模型族扩大选择空间，却增加lineage、quantization、routing、evaluation和deprecation矩阵；distillation带teacher bias/capacity gap；reasoning variant增加verbosity/loop和SLO风险。
- **Where the Previous Design Still Applies:** 单一workload、充分训练预算或需独立architecture时从零训练/单模型更简单；teacher与student capacity mismatch大时distillation未必合适。
- **Evolution Relationship:** `Layering / Dependency`：single model → teacher-derived size/behavior variants → SLO-aware portfolio routing；portfolio不是架构优劣排序。
- **ROADMAP Node:** Ch21、Ch23～25、Ch29、Ch45～46、Ch66。
- **Target and Adjacent Chapters Read:** 已读 Ch21、Ch23～25、Ch29、Ch45～46、Ch52、Ch66；Ch25 为 Cascade Distillation 主 owner。
- **Existing Coverage:** 后续全文披露的 Cascade Distillation/teacher capacity gap 已进入 Ch25；model portfolio 版本事实仍只留 Weekly。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch25，吸收 Cascade Distillation 与 teacher-capacity gap。
- **Changed Files or Rejection Reason:** 已更新 `books/part-03-training-system/25-sft.md`；明确 2026 report 不能倒写成 2025 release disclosure。
- **Open Questions:** Large 3完整技术报告、Cascade Distillation compute/data contract、independent reproduction、portfolio router的cost/quality calibration。

### Google Research synthesis of Titans + MIRAS

- **Candidate / Week / Score:** Google Research synthesis of Titans + MIRAS / 2025-W49 / 22/30。
- **Source Family ID:** `GOOGLE-TITANS-MIRAS-2025`（机制源回链 W01/W16）。
- **Source Type:** Google Research official synthesis Blog、linked primary papers。
- **First-public Date / Revision History:** synthesis 2025-12-04；Titans论文first-public 2024-12-31归W01，MIRAS v1 2025-04-17归W16。机构说明不生成新的first-public mechanism事件。
- **Direct Primary Sources:** Google Research synthesis全文；Titans/MIRAS arXiv papers由W01/W16 Source Review承载。
- **Related Primary Sources:** Titans/MIRAS official code/artifact若有；不重复构造第二套实验结论。
- **Access and Verification Status:** Verified；Blog为研究路线解释，性能与机制证明仍以原论文为准。
- **Full-read Coverage:** 已阅读全文的attention/RNN/SSM问题 framing、Titans neural long-term memory、surprise update、MIRAS四维设计空间、两者关系、实验摘要与limitations；并与W01/W16全文packet交叉核对。
- **Original Problem:** attention精确访问但长序列成本高；固定状态RNN/SSM线性扩展却压缩过强，需要可在线学习的长期memory层。
- **Why the Previous Design Was Reasonable:** attention适合精确短期上下文，固定状态适合流式稳定/低成本；多数请求不需可写神经记忆。
- **Changed Constraint:** 超长非平稳序列希望在test time根据surprise选择性更新memory，而不是保存所有token或固定压缩。
- **Mechanism:** Titans是具体架构，把deep neural memory module作为test-time可学习状态并与attention组合；MIRAS将memory architecture、attentional bias、retention gate、learning algorithm抽象为设计空间。
- **State Ownership:** neural memory module拥有可变参数/fast weights；retention/optimizer控制更新与遗忘；session/runtime必须决定tenant/session隔离、checkpoint、rollback与并发。
- **Control Flow / Data Flow:** token表示 → surprise/gradient-like signal → memory update/retention → attention或read path访问；错误更新会持久影响后续token。
- **Implementation Details:** synthesis帮助区分具体Titans实例与MIRAS generalization；它没有新增production implementation、multi-tenant semantics或独立benchmark。
- **Evaluation Setup:** Blog复述论文语言建模、long context等作者实验；完整模型、hardware、precision、length/baselines见W01/W16 packets，本周不重复数字。
- **Baselines / Ablations / Sensitivity:** 原论文比较Transformer、recurrent/SSM与memory variants；synthesis无新增ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 本Blog不新增完整workload contract；全部deployment字段 Not Disclosed。
- **What the Evidence Actually Proves:** 官方作者团队将Titans视为具体test-time memory设计，将MIRAS视为统一框架；这补强二者是layering/generalization而非两个互斥版本。
- **What It Does Not Prove:** 不证明production-ready、不证明online update安全隔离、不提供独立复现，也不证明替代attention/RAG/KV cache。
- **Limitations / Threats to Validity:** 机构自述、机制与实验重复原论文、无production state semantics；online memory可能污染、遗忘、不可解释。
- **Trade-offs / New Failure Modes:** 可扩展memory容量换来update stability、session contamination、rollback、tenant leakage、optimizer-state恢复与并发ordering。
- **Where the Previous Design Still Applies:** 短context、精确引用、只读knowledge、强隔离或需要可审计provenance时attention/RAG/显式memory store仍更适合。
- **Evolution Relationship:** `Layering / Dependency`：Titans具体实例 → MIRAS设计空间解释；与attention/RAG是分层/替代分支，不是日期驱动取代。
- **ROADMAP Node:** Ch14、Ch22、Ch73。
- **Target and Adjacent Chapters Read:** 已读 Ch14、Ch22、Ch71～73；本来源只回链 W01/W16，不重复写入。
- **Existing Coverage:** Ch73 provisional handoff已存在；本候选本身没有新增机制，但可纠正关系标签与状态所有权表述。
- **Integration Decision:** `No Change — Already Covered`；Ch22 的 test-time memory 与 Ch73 的 durable-state boundary 已覆盖。
- **Changed Files or Rejection Reason:** 不改 Books；本来源只补强 W01/W16 证据并纠正关系标签。
- **Open Questions:** online memory tenant isolation、checkpoint/rollback、concurrent update ordering与可验证forgetting。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系为本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper、model card 与工程集成按证据角色回链，不重复形成 Books 观点。
- 新方案不覆盖旧方案；保留适用条件、新增状态与 failure modes。

## Knowledge Tree Position

- DeepSeek-V3.2 → 第 14、22、29、39～41、45、46、50、74 章（Direct Evolution）
- Mistral 3 → 第 21、45、46、66 章（Layering / Dependency）
- Google Research synthesis of Titans + MIRAS → 第 14、22、73 章（Layering / Dependency；回链 W01/W16）

## Recommended Action

- DeepSeek-V3.2：Must Read；全文审查后优先 refine Long Context/Inference/Agent handoff
- Mistral 3：Worth Watching；作为 cost-quality portfolio 信号
- Google Research synthesis of Titans + MIRAS：Worth Watching；回链 W01/W16，不重复沉淀

## Event-Date Daily Decision

历史回填不创建 Daily；证据直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、榜单、缺条件 benchmark 与无新机制的价格/可用性变化。
- 不以“更新”自动否定旧设计。

## Repository Changes

- 新增 papers/2025/weekly/2025-W49/README.md。
- 本周候选已完成最终 Books disposition；实际章节修改或拒绝理由见各候选的 `Changed Files or Rejection Reason`。

## Open Questions

- DSA 的 indexer quality、cache identity 与 serving fallback 仍需更多独立实现证据。
- Mistral 3 的 model-family portfolio 不改变现有 workload/SLO 驱动的模型选择结论。
- Mistral 3 后续全文披露的 Cascade Distillation 与 teacher capacity gap 是否补全现有训练章节，需在 Books Gate 重新判断。
- test-time neural memory 的生产隔离、恢复与并发 ownership 仍待验证。

## Sources

- DeepSeek-V3.2 — https://arxiv.org/abs/2512.02556（First Public: 2025-12-01 release；2025-12-02 paper v1；Accessed: 2026-07-31）
- DeepSeek-V3.2 HTML — https://arxiv.org/html/2512.02556（v1: 2025-12-02；Accessed: 2026-07-31）
- Mistral 3 — https://mistral.ai/news/mistral-3/（First Public: 2025-12-02；Accessed: 2026-07-31）
- Ministral 3 technical paper — https://arxiv.org/abs/2601.08584（v1: 2026-01-13；Source Family follow-up；Accessed: 2026-07-31）
- Google Research synthesis of Titans + MIRAS — https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/（First Public: 2025-12-04；论文首次公开见 W01/W16；Accessed: 2026-07-31）
