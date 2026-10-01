# 2026-06-04 V3 recovery blockers

## 当前恢复停点（2026-10-01）

窗口为 `[2026-06-03 09:00, 2026-06-04 09:00)` BJT。作者 `sep22_resume_v3` 独立重读当前合同后接手；拥有当日 Report/本 packet，Books仅root授权Ch81/Ch72各两段窄锁，不改索引。

1. `official-arxiv-first-public-owner-receipt-v1.json` 的日期合同明确使用 DataCite `created` 作公告周期，实际 41 旧身份不能据此获公开上界。只恢复官方当批公开证据，不制造 `[08:00,09:00)`；旧 64 候选表不是本轮已核准候选，也不自动成为必要全文队列。
2. 本日 `source-review-receipts.json` 与 `arxiv-submission-history-receipts.json` 实际零字节；旧完成标签不能弥补来源证据。保留已有必要正文与机制笔记，不宣称证据全无，也不清除有效 Books。
3. 上述有界恢复已执行：Kimi 0.9.0 与 Anthropic Navigator 两确定家族必要包、OpenAI五条核心关闭、Dreaming窗外时钟、每日14源实际有限停止已同步正式六部分；arXiv逐64身份加MetaPoint独立DateHold合65，外部日期/目录限制隔离而非普通待读。
4. 旧 EvalStop实际正文及 UltraEP撤回清理是既有变化，不是本轮采用授权；先日期闭合再决定是否需要必要机制复核。root已通过两个发布家族必要source→owner/提案并授窄锁；实际写入Ch81:1150/1152与Ch72:671/673，root亲读实际两段及邻接写后PASS，窄锁已释放；未 stage/commit/push。

当前普通可执行待办0；两个实际窄段已获root非作者写后PASS，root最终日级安全终态Gate亦PASS，正式Report已同步完成。source→owner与授权实写已完成，不是日期缺失导致永久等待。当前完成态V3与限定diff-check实际PASS，65身份表已机械核唯一；65不是全文/证据/日期通过。Kimi记录重放失败的catch cleanup不扩大为parent resume await之外所有失败。root独立release API、OpenAI原RSS三运营/政策事件与Wasmer/blueprint负侧及UltraEP admin风险核准，Anthropic精确嵌入时钟复用作者原HTML而非root403后重新获取；其余stop与5历史缺口只验收隔离，不宣称全站无漏项。

### 当前已核公开入口（2026-10-01 07:35 BJT）

- OpenAI 官方 `https://openai.com/news/rss.xml` 以 curl UA 读取 1240 条并按窗口过滤，实际五条：Biodefense `Thu, 04 Jun 2026 00:00:00 GMT`；Rosalind `Wed, 03 Jun 2026 13:15:00 GMT`；Wasmer `Wed, 03 Jun 2026 12:00:00 GMT`；public-policy-agenda 与 frontier-safety-blueprint 均 `Wed, 03 Jun 2026 10:00:00 GMT`。五篇核心说明均已实际读；前两为暂缓的 life-science/biodefense 应用，后两为机构政策提案而非新增可执行模型/系统机制；Wasmer 是客户案例，10–20×及一年→两周不是受控 Agent 机制对照，不准入、不评分。Rosalind 页面还含 September 11 update，不能把后来开放范围当六月新事件。
- Dreaming 原始 `pubDate=Thu, 04 Jun 2026 09:00:00 GMT`，即 06/04 17:00 BJT，窗外，旧本日缺日期已关闭；仅给 06/05 原始恢复线索，不在本日采用或审阅其正文。
- Kimi 官方 GitHub release API `releases/tags/%40moonshot-ai%2Fkimi-code%400.9.0`：release id `333758230`，`published_at=2026-06-03T14:01:42Z`，即 22:01:42 BJT；draft/prerelease 均 false，`updated_at=14:06:27Z` 非首次公开时间。release 核心全读，拟 2+2+2=6；ACP adapter、ephemeral `/btw`、saved-subagent lazy resume 与 provider goal/completion cap 是本窗兼容/执行边界变化，按合同深入受影响内容。
- Kimi exact release 所链 commits：368 `3eafa79f39c06b67d18bd2c1fd5321d2d889ed90` docs/en/reference/kimi-acp.md 实际 patch 全读；338 `ba7dd736a3b295b2a29c229a944208c232d51458` projector、ephemeral child 与 permission 必要 patch 已读；380 `86391053139ad4ea437afe79f472412fb1b106a1` session/index.ts 全 patch 实读；365 `6a2252343a0d624b326b2d369ec908bc8d60092d` goal schema/budget/provider cap 必要 patch 已读。不是运行测试或生产验证。380 只恢复 main，saved children 首次访问才 replay；promise memoization、parent-cycle rejection、记录重放失败在对应catch删除 pending entry（parent resume await在try之外，不泛称全部parent失败清理），不等于任意崩溃/副作用恢复保证。338 拷贝工具定义为 cache reuse，但 DenyAllPolicy 与 InMemoryRecordPersistence 使旁路不获原 Tool effect authority、不登记 durable child；history closure 不等于任务成功证明。365 正整数 rounds normalization/具体 provider token-key 与 declared cap 不是端到端工具/费用预算保证。338 snapshot 关联及368 auth/session/cancel code已补齐；root必要源→actual owner/pre与实际写后均PASS。
- Anthropic Research 内嵌目录真实 `publishedOn`：`attack-navigator=2026-06-03T18:00:00.000Z`（06/04 02:00 BJT），news `AI-enabled-cyber-threats-mitre-attack=2026-06-03T10:55:00.000Z`（06/03 18:55 BJT），两记录去重为一个报告家族。research article 核心、dataset、ARiES score、§Novelty and sophistication 与 limits 实读，候选入口为加法 attention-priority 不等于 attack-success probability，以及 technique-count taxonomy 遗漏自主编排；不是新增攻击步骤或模型本身普遍 uplift。

### 必要源→实际 owner（root pre/actual write-after PASS）

精确入口：338 [startBtw](https://github.com/MoonshotAI/kimi-code/blob/ba7dd736a3b295b2a29c229a944208c232d51458/packages/agent-core/src/session/subagent-host.ts)、[history copy](https://github.com/MoonshotAI/kimi-code/blob/ba7dd736a3b295b2a29c229a944208c232d51458/packages/agent-core/src/agent/context/index.ts)、[tail closure](https://github.com/MoonshotAI/kimi-code/blob/ba7dd736a3b295b2a29c229a944208c232d51458/packages/agent-core/src/agent/context/projector.ts)、[deny](https://github.com/MoonshotAI/kimi-code/blob/ba7dd736a3b295b2a29c229a944208c232d51458/packages/agent-core/src/agent/permission/policies/deny-all.ts)；380 [lazy session](https://github.com/MoonshotAI/kimi-code/blob/86391053139ad4ea437afe79f472412fb1b106a1/packages/agent-core/src/session/index.ts)。官方 API commits/SHA patch 可替代raw网络reset。338 test/session/init.test.ts 的snapshot/nonpersistent和拒绝LookupNote/Read脚本测试已读作者代码，未运行，不称验证生产全工具完备隔离。

Anthropic [research](https://www.anthropic.com/research/attack-navigator) 与 [news](https://www.anthropic.com/news/AI-enabled-cyber-threats-mitre-attack) 两官方入口；news先公开摘要，research同窗公开详细score/调查报告，合一家族。§3所列是research事件时刻，不把它当全家族最早时间；两时钟原值和BJT转换均保留。

Kimi 338 `agent/context/index.ts::useProjectedHistoryFrom` 实读：`clear()` 后 `pushHistory(...trimTrailingOpenToolExchange(source.project(source.history)))`，不是 live history subscription；338 `permission/policies/deny-all.ts` 的 evaluate 恒返回 deny/side_question。368 `server.ts::authenticate` 只接受 login 并验证现有 harness auth；`cancel` 为 notification，未知session或失败仅log，不提供取消完成的client response；`session.ts::handleApproval` await reverse requestPermission，RPC失败明确 rejected。上述是实现代码检查，未运行测试。Ch83:94–105 的五契约/adapter-runtime-policy分责实际覆盖 ACP 的长期分层，但不覆盖 ephemeral branch 的投影/持久性选择；Ch81:1140–1148 的 revision-bound review与resume性质亦没有把旁路问答和 persisted workflow child 分开。Ch81 Resume末→Logical Plan前两段已实际写入1150/1152、SF-KIMI-CODE-0-9唯一，root source→owner及write-after PASS：冻结已闭合history、独立ephemeral records与deny-all；代价为stale snapshot与不能跨restart恢复，欲执行动作转回主turn重核当前状态/权限（工程推断）；lazy child 只表示按需replay，parent/cycle与记录重放catch的pending清理边界并非全部ready或exactly-once。

Anthropic 核心 §About the dataset/ARiES/Novelty/Limits 全读。832 是有足够调查细节的 banned subset；13,873 actions/482 subtechniques/V18；ARiES以 threat35+vulnerability35+impact30 为优先注意力目标而非攻击成功概率，部分impact是潜在结果、skill由Claude评分，interface也进入V。去掉skill后的局部 r=.28 与 technique-breadth r=.27 不是模型uplift的因果识别；33.5→56.1%的shift原文承认检测改进混杂。GTG单案例的自主编排可见，但末段提取仍human-directed，不能据此说全链无人。Classifier/probe部署是厂商声明，无防线效果验证。Ch72:665–681 SecurityAgent/Containment 实际保存trace、authority/effect并限制attack-success，但没有priority-score目标与taxonomy遗漏orchestration这一差额。Ch72 SecurityAgent末→Containment前两段已实际写入671/673、SF-ANTHROPIC-ATTACK-NAVIGATOR唯一，root source→owner及write-after PASS：分账priority/probability，technique频次与编排/effect证据分开；保selected population/潜在impact/检测漂移与有限关联，不将score、taxonomy或产品部署当安全概率证明。

### 日期终态隔离依据

官方 `https://arxiv.org/list/cs.CL/260604` direct curl HTTP404、web cache miss；正确 `https://arxiv.org/list/cs.CL/2026-06?skip=0&show=25` 与 show2000 月列表均只有June总2718、ascending IDs，没有 daily announcement headers。只读首切片及目录结构，不把月2718或旧575当本窗材料。官方 advanced 明文 announcement date 仅year/month，submission date虽day不等于first-public。精确 EvalStop04145v1原页只给 `Tue, 2 Jun 2026 19:03:39 UTC` 提交史（及June10/14修订），不能补公告上界；官方域两次有限精确announcement/list搜索无可用原公告。DataCite Created/Updated、正常schedule最早时刻均不可制造公开上界。64旧arXiv逐身份DateHold；只接受该identity exact事件的官方当批公告、带时区作者公开正文receipt或可复查原始公开快照到达后重开，不再读64全文。

UltraEP04101v1 exact abs admin明确许可权缺失而removed，v1 withdrawn/noPDF；旧已去入选/评分/采用，保持原始排除，不拿访问故障请求正文。当前只轻量核官方标记，未比较所有旧版本或重新采用其性能。当前针对UltraEP/2606.04101全Books exact identity grep无命中，旧撤回采用链无残留；不泛删其他EP论点。旧 EvalStop/Covert/04929 已有正文/证据保留，日期未准不计本轮I/E，不一刀删除其他有效论点。

MetaPoint2606.05031v1在Seed目录Jun03，exact v1 submission June03 15:58:56UTC只是提交；原目录PublishDate日历占位不能证明早公开，且不在旧64集合。只定点复用未变身份/原稿贡献，不复用June03完成标签。独立DateHold使本轮具名日期保留为65；不准入/评分/Books，不声称65证据已审。

## 旧快照（非本轮分母或验收）

> **2026-09-11 post-write update：** 最终分母为 64 Candidate / 511 Close：UltraEP（2606.04101）因官方 v1/v2/v3 全部 withdrawn 而去准入；2606.04071/04929 为 `已有覆盖`，2606.04145 EvalStop 已真实写入 `TRAIN-RLHF`/Ch31 并通过非作者 post-write audit。UltraEP Books residue 为 0；2606.04071 的旧 adoption trace 已精确删除；当前 blocker 为 0。

## Denominator

可读基线为 575 raw / 41 prior / 534 closure proposals。435 项共用的 incremental closure 理由被反例击穿后已全量重审，其余 99 项按 embodied / benchmark / theory / vertical 逐项复核，41 prior 也重新检查。

首轮 Candidate 210 / Close 365 被严格复核推翻：该轮仍把大模型对象或章节可映射性误当作贡献准入。作者侧二次 checkpoint 为 Candidate 73 / Close 502：旧 534 closure proposals 中只恢复 38 项，旧 41 prior 中关闭 6 项；首轮另有 137 项 Candidate 因缺少跨 workload 的长期 state/data/control、execution/evaluation/release contract 而撤回。非作者复核再关闭 9 项，最终 authority 为 Candidate 64 / Close 511；逐项和逐族理由及 10+10 FP/FN 抽查见 V3_SCREENING_LEDGER.md。

## Books write queue

当前 Books 只读快照：

| Source Family ID | Target | Body anchor | Trace anchor | 队列 |
| --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-04929 | books/part-06-ai-infrastructure/72-security.md | semantic-body-binding:SF-2026-ARXIV-2606-04929（约 1379 行） | daily-books-trace:SF-2026-ARXIV-2606-04929（约 2158 行） | 正文已存在；只复验 exact-v1 边界 |
| SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS | books/part-07-agent/77-memory.md + books/part-06-ai-infrastructure/72-security.md | Ch77 `Stateless API 仍可能承载跨调用的 Implicit Memory` + Ch72 `多 Agent Cascade 需要跨 Channel 的 Influence Graph` | 无 | `已有覆盖`；旧 adoption trace 已删除，不新增正文 |
| SF-EVALSTOP | books/part-04-training-system/31-rlhf.md | `训练停止不能只看 Training Loss 或 Reward Model Score`；`semantic-body-binding:SF-EVALSTOP` | daily-books-trace:SF-EVALSTOP | 已写入并通过非作者 post-write audit |

此旧队列不是本轮采用授权。有效正文保留；若有官方撤回信号则定点清除相关采用链，不按日期缺口一刀删除。


## 本轮具名日期保留（64旧身份 + MetaPoint = 65）

本表不是确定候选，也不是64篇Evidence通过；仅列原身份与统一、精确重开条件。原旧研究证据在下方旧§4及V2_1/V3_BATCH档案保留，不继承其日期/评分/采用验收。

| 原材料身份 | 本轮状态 | 采用边界 |
| --- | --- | --- |
| [Neither Layer Alone: Epistemic Integrity Requires Hierarchical Joint Design for Long-Running AI Agents](https://arxiv.org/abs/2606.04017v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Token Budgets: An Empirical Catalog of 63 LLM-Agent Budget-Overrun Incidents, with an Affine-Typed Rust Mitigation as a Case Study](https://arxiv.org/abs/2606.04056v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Covert Influence Between Language Models](https://arxiv.org/abs/2606.04071v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Proof-Carrying Agent Actions: Model-Agnostic Runtime Governance for Heterogeneous Agent Systems](https://arxiv.org/abs/2606.04104v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [EvalStop: Using World Feedback to Detect and Correct Reward Overoptimization in Multi-Tenant RLHF Platforms](https://arxiv.org/abs/2606.04145v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Notarized Agents: Receiver-Attested Confidential Receipts for AI Agent Actions](https://arxiv.org/abs/2606.04193v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Puffin-Backed Vector Indexes: Attaching Approximate Nearest Neighbor Indexes to Apache Iceberg Snapshots for Compute-Disaggregated Query Engines](https://arxiv.org/abs/2606.04196v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Can Generalist Agents Automate Data Curation?](https://arxiv.org/abs/2606.04261v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [The Saturation Trap and the Subjectivity of Intervention Timing: Why Affect-Based Triggers and LLM Judges Fail to Time Interventions on Autonomous Agents](https://arxiv.org/abs/2606.04296v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [LazyAttention: Efficient Retrieval-Augmented Generation with Deferred Positional Encoding](https://arxiv.org/abs/2606.04302v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Organizational Control Layer: Governance Infrastructure at the Execution Boundary of LLM Agent Systems](https://arxiv.org/abs/2606.04306v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Exploring Cross-Scenario Generality of Agentic Memory Systems: Diagnostics and a Strong Baseline](https://arxiv.org/abs/2606.04315v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [The Digital Apprentice: A Framework for Human-Directed Agentic AI Development](https://arxiv.org/abs/2606.04321v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents](https://arxiv.org/abs/2606.04329v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Not All Errors Are Equal: Consequence-Aware Reasoning Compute Allocation](https://arxiv.org/abs/2606.04402v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [FlexNPU: Transparent NPU Virtualization for Dynamic LLM Prefill-Decode Co-location](https://arxiv.org/abs/2606.04415v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [What If Prompt Injection Never Left? Rethinking Agent Security through Cross-Session Stored Prompt Injection](https://arxiv.org/abs/2606.04425v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Token Rankings are Unforgeable Language Model Signatures](https://arxiv.org/abs/2606.04459v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [ANN Search: Recall What Matters](https://arxiv.org/abs/2606.04522v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Cartridges at Scale: Training Modular KV Caches over Large Document Collections](https://arxiv.org/abs/2606.04557v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Multi-SPIN: Multi-Access Speculative Inference for Cooperative Token Generation at the Edge](https://arxiv.org/abs/2606.04581v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Ekka: Automated Diagnosis of Silent Errors in LLM Inference](https://arxiv.org/abs/2606.04594v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [RAMPART: Registry-based Agentic Memory with Priority-Aware Runtime Transformation](https://arxiv.org/abs/2606.04628v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Description-Code Inconsistency in Real-world MCP Servers: Measurement, Detection, and Security Implications](https://arxiv.org/abs/2606.04769v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [UModel: An Agent-Ready Observability Data Modeling Method at Scale](https://arxiv.org/abs/2606.04799v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Provably Auditable and Safe LLM Agents from Human-Authored Ontologies](https://arxiv.org/abs/2606.04903v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [GNStor: Design of GPU-Native High-Performance Remote All-Flash Array](https://arxiv.org/abs/2606.04908v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2606.04923v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Sequential Data Poisoning in LLM Post-Training](https://arxiv.org/abs/2606.04929v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [SharedRequest: Privacy-Preserving Model-Agnostic Inference for Large Language Models](https://arxiv.org/abs/2606.05004v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Validity Threats for Foundation Model Research](https://arxiv.org/abs/2606.05029v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Self-Reflective APIs: Structure Beats Verbosity for AI Agent Recovery](https://arxiv.org/abs/2606.05037v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Strabo: Declarative Specification and Implementation of Agentic Interaction Protocols](https://arxiv.org/abs/2606.05043v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Novel Aspects of IEEE SA P3109 Arithmetic Formats for Machine Learning](https://arxiv.org/abs/2606.04028v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Toward Pre-Deployment Assurance for Enterprise AI Agents: Ontology-Grounded Simulation and Trust Certification](https://arxiv.org/abs/2606.04037v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Need to Know: Contextual-Integrity-Grounded Query Rewriting for Privacy-Conscious LLM Delegation](https://arxiv.org/abs/2606.04067v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Caught in the Act(ivation): Toward Pre-Output and Multi-Turn Detection of Credential Exfiltration by LLM Agents](https://arxiv.org/abs/2606.04141v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval](https://arxiv.org/abs/2606.04391v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Context-as-AI-Service: Surfacing Cross-File Dependency Chains for LLM-Generated Developer Documentation](https://arxiv.org/abs/2606.04397v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Trivium: Temporal Regret as a First-Class Objective for Causal-Memory Controllers](https://arxiv.org/abs/2606.04421v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Cascading Hallucination in Agentic RAG: The CHARM Framework for Detection and Mitigation](https://arxiv.org/abs/2606.04435v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [AgentJet: A Distributed Swarm Training Framework for Agentic Reinforcement Learning](https://arxiv.org/abs/2606.04484v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Temporal Order Matters for Agentic Memory: Segment Trees for Long-Horizon Agents](https://arxiv.org/abs/2606.04555v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Selectivity Estimation for Semantic Filters on Image Data](https://arxiv.org/abs/2606.04610v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Bridge the Last-Mile Gap to Semantic Analytics: Compiling Natural-Language Queries into Semantic Operator Pipelines](https://arxiv.org/abs/2606.04641v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [CYGNET: Cypher Gate for Neural Execution Triage and Cost Containment](https://arxiv.org/abs/2606.04645v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Rethinking Continual Experience Internalization for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.04703v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents](https://arxiv.org/abs/2606.04780v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [AIP: A Graph Representation for Learning and Governing Agent Skills](https://arxiv.org/abs/2606.04781v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Learning While Acting: A Skill-Enhanced Test-Time Co-Evolution Framework for Online Lifelong Learning Agents](https://arxiv.org/abs/2606.04815v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Channel Fracture: Three Instances of Cross-Boundary Silent Delivery Reliability Failures in Multi-Agent Systems](https://arxiv.org/abs/2606.04896v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Audio Interaction Model](https://arxiv.org/abs/2606.05121v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Streaming Communication in Multi-Agent Reasoning](https://arxiv.org/abs/2606.05158v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Discourse-Role Labels as Presentation-Time Variables for Context Use in Language Models](https://arxiv.org/abs/2606.04109v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?](https://arxiv.org/abs/2606.04455v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [QO-Bench: Diagnosing Query-Operator-Preserving Retrieval over Typed Event Tuples](https://arxiv.org/abs/2606.04646v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Revisiting Vul-RAG: Reproducibility and Replicability of RAG-based Vulnerability Detection with Open-Weight Models](https://arxiv.org/abs/2606.04739v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [AutoLab: Can Frontier Models Solve Long-Horizon Auto Research and Engineering Tasks?](https://arxiv.org/abs/2606.05080v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Failed Reasoning Traces Tell You What Is Fixable (But Not by Reading Them)](https://arxiv.org/abs/2606.05145v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Beyond Single-Policy: Evaluating Composed Organization-Specific Policy Alignment in LLM Chatbots](https://arxiv.org/abs/2606.04394v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [MemoryDocDataSet: A Benchmark for Joint Conversational Memory and Long Document Reasoning](https://arxiv.org/abs/2606.04442v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Benchmarking Living-Screen-Native GUI Agents on Short-Video Platforms](https://arxiv.org/abs/2606.04701v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Auditing CoT Answer-Hijack Patches: Source-Control Certificates with Type-I Guarantees](https://arxiv.org/abs/2606.04717v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents](https://arxiv.org/abs/2606.04874v1) | DateHold：首次公开上界未证 | 保留原研究材料；本轮不评分、不计正面审阅或Books采用 |
| [MetaPoint](https://arxiv.org/abs/2606.05031v1) | DateHold：Seed目录日历不证首次公开，v1提交不证公告上界 | 与64身份disjoint，不评分/不计正面采用 |

## 原正式§4快照（非本轮证据/Books/日期验收）

以下是改稿前保存的旧机制笔记，保持其证据可恢复；‘深入完成/已有覆盖/已整合/队列清零’及旧日期属于旧过程，不签发当前采用。这不是当前必要源已全审声明。当前只有上方两确定发布必要包继续执行。

## 4. 证据与知识整合

### [Kimi Code 0.9.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.9.0)

官方 GitHub Release 的 `published_at=2026-06-03T14:01:42Z`。release notes 披露 ACP adapter 以 stdio 接入外部 client，并以 `/btw` side-channel 避免旁路问题污染主 conversation；它证明公开接口存在，不证明跨 client interoperability、durable replay、消息次序或生产 SLO。`AGENT-MCP` 已覆盖协议适配器、transport/session identity、旁路控制与失败边界，故维持 `No Change — Existing Coverage`。

旧候选的 Method/Evaluation/Limitations 与 exact-v1 保留在归档中，但旧 Books disposition 不继承；UltraEP 的归档记录仅是历史证据，不再构成当前 Source Review。独立复核确认 2606.04071 与 2606.04929 为 `已有覆盖`：前者跨 `AGENT-MEMORY` 的 Stateless API/Implicit Memory 与 `PLATFORM-SECURITY` 的 Influence Graph，后者使用 Ch72 的 `semantic-body-binding:SF-2026-ARXIV-2606-04929` Review notes 前正文 anchor。2606.04145 EvalStop 已整合至 Ch31“训练停止不能只看 Training Loss 或 Reward Model Score”：外部 Evaluation Run 产生带版本的 downstream-quality trajectory，RLHF controller 只提出 stop proposal，训练作业 owner 提交停止，GPU Scheduler 仅消费资源释放事件。正文保留了固定预算的共存边界、额外评测与反馈延迟等 trade-off，以及连续窗口、人工 gate 等 fallback。其 exact-v1 证据只限离散事件模拟、Poisson arrival、slot GPU、2-minute preemption 与 synthetic/parameterized curves；没有生产 workload、生产 SLO 或 versioned artifact。以下 31 项是本轮新恢复 Candidate 的同标题、同 URL Evidence；旧 33 项的完整 exact-v1 审阅继续由 [V2_1_EVIDENCE_ARCHIVE.md](./V2_1_EVIDENCE_ARCHIVE.md) 提供。

### [Novel Aspects of IEEE SA P3109 Arithmetic Formats for Machine Learning](https://arxiv.org/abs/2606.04028v1)

`arXiv:2606.04028v1`，§III Datum Sets、§IV Operations、§V Formal Verification 与 §VIII Block Operations；贡献是数值格式语义、运算与验证边界，不是某个模型的新结构。 §X Discussion and Limitations；标准仍为 draft，不能外推为所有 accelerator 已实现或取得端到端收益。 Books 复核为`Only report`；可路由至训练数值稳定性相邻 owner，但尚不足以改变书稿的通用精度机制链。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](./V3_EVIDENCE_BATCH_01.md)。

### [Toward Pre-Deployment Assurance for Enterprise AI Agents: Ontology-Grounded Simulation and Trust Certification](https://arxiv.org/abs/2606.04037v1)

`arXiv:2606.04037v1`，§2.2 Agent Operational Envelope、§2.3 Ontology-to-Scenario Generation、§2.4 Trust Certificate 与 §2.5 Implementation Architecture；把 ontology 约束、scenario coverage、certificate 与 deployment gate 连成发布合同。 这是 proposed framework；经验有效性依赖 ontology 完整度、judge 校准与 ground-truth controls，不能视作生产认证标准。 Books 复核为`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；现有评测/发布门已覆盖预声明边界、独立 ground truth 与阻断式 gate。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](./V3_EVIDENCE_BATCH_01.md)。

### [Need to Know: Contextual-Integrity-Grounded Query Rewriting for Privacy-Conscious LLM Delegation](https://arxiv.org/abs/2606.04067v1)

`arXiv:2606.04067v1`，§3 DelegateCI-Bench 与 §4 Method（framework、reward、policy training）；将 disclosure decision 放在 delegation 前的 query-rewrite boundary。 独立 Limitations；medical/general-domain slice、judge 与本地 reformulator 的边界不能外推为任意隐私域或密码学保密。 Books 复核为`已有覆盖`，owner=`PLATFORM-SECURITY`；最小披露、数据边界与外部模型调用前的 policy enforcement 已有机制 owner。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](./V3_EVIDENCE_BATCH_01.md)。

### [Caught in the Act(ivation): Toward Pre-Output and Multi-Turn Detection of Credential Exfiltration by LLM Agents](https://arxiv.org/abs/2606.04141v1)

`arXiv:2606.04141v1`，§3 Threat Model、§4.1 System Overview、§4.2 CIFT、§4.3 DP-HONEY 与 §4.4 NIMBUS；把 pre-output activation signal、honeytoken 与跨轮泄漏预算组合成 control plane。 §6 明示小型 in-house benchmark、white-box requirement 与 preliminary prototype；不证明 API-only 黑盒或生产 FPR/SLO。 Books 复核为`已有覆盖`，owner=`PLATFORM-SECURITY`；credential least privilege、跨轮状态、独立 detector 与阻断边界已有正文机制。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](./V3_EVIDENCE_BATCH_01.md)。

### [Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval](https://arxiv.org/abs/2606.04391v1)

`arXiv:2606.04391v1`，§3 formalization 与 §4 skill extraction、state-grounded retrieval、injection/execution；skill state 由页面状态而非只由任务文本选择。 独立 Limitations；只验证 WebArena/指定模型，retrieval state 与 skill quality 不代表跨 GUI/workload 泛化。 Books 复核为`已有覆盖`，owner=`AGENT-MEMORY`；现有 memory/skill owner 已覆盖写入、检索、版本与执行反馈循环。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](./V3_EVIDENCE_BATCH_01.md)。

### [Context-as-AI-Service: Surfacing Cross-File Dependency Chains for LLM-Generated Developer Documentation](https://arxiv.org/abs/2606.04397v1)

`arXiv:2606.04397v1`，§3 Source Ingestion、Storage and Indexing、Retrieval Interface、Review Layer；把跨文件依赖作为可追溯 context service 返回。 独立 Limitations；两个匿名案例与文档任务不足以证明通用代码理解或自动合并安全。 Books 复核为`已有覆盖`，owner=`AGENT-RAG`；索引 owner、dependency-aware retrieval、citation/evidence trail 与人工 review handoff 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](./V3_EVIDENCE_BATCH_01.md)。

### [Trivium: Temporal Regret as a First-Class Objective for Causal-Memory Controllers](https://arxiv.org/abs/2606.04421v1)

`arXiv:2606.04421v1`，§3 Three-Regret Functional、drift-robust replan/dispatch coupling 与 Trivium algorithm；持久 causal log 显式记录 why/when，并影响后续 dispatch。 §5 Conclusion, Impact, and Limitations；受合成 SCM、probe assumptions 与 pilot deployment scope 限制。 Books 复核为`已有覆盖`，owner=`AGENT-MEMORY`；现有 episodic/semantic memory、provenance、失效与再规划链已覆盖该长期机制。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](./V3_EVIDENCE_BATCH_01.md)。

### [Cascading Hallucination in Agentic RAG: The CHARM Framework for Detection and Mitigation](https://arxiv.org/abs/2606.04435v1)

`arXiv:2606.04435v1`，§III problem formalization、§IV CHARM 与 §V mitigation architectures；在每个 stage 维护跨阶段置信与 verifier，而非只验最终答案。 §VII Discussion；作者验证的是指定注入轨迹与 datasets，不能证明 Bayesian calibration、judge 或所有 retrieval failure 在生产中稳定。 Books 复核为`已有覆盖`，owner=`AGENT-RAG`（相邻 `PLATFORM-EVALUATION-SYSTEM`）；分阶段 citation/verification、fallback 与 end-to-end evaluation 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](./V3_EVIDENCE_BATCH_01.md)。

### [AgentJet: A Distributed Swarm Training Framework for Agentic Reinforcement Learning](https://arxiv.org/abs/2606.04484v1)

`arXiv:2606.04484v1`，§3 Swarm Architecture、Swarm RL、episode batching 与 context tracking；client/server 解耦让异构 agent、environment 与 learner 各自拥有生命周期和故障边界。 exact-v1 未定位独立 Limitations 章节；边界由作者披露的 Werewolves/translation/AppWorld 等 workloads 推得，未建立任意环境、网络分区或生产多租户公平性结论。Books 复核为`已有覆盖`，owner=`TRAIN-DISTRIBUTED-TRAINING`；现有 actor/rollout/learner 解耦、trajectory ownership 与 backpressure/failure recovery 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](./V3_EVIDENCE_BATCH_01.md)。

### [Temporal Order Matters for Agentic Memory: Segment Trees for Long-Horizon Agents](https://arxiv.org/abs/2606.04555v1)

`arXiv:2606.04555v1`，§4.1 Conversation Segment Tree、§4.2 online construction 与 §4.3 structure-aware retrieval；显式保留 temporal order 与 hierarchical segment owner。 §6 Limitation and future work；指定 benchmark/backbone 与 online implementation 不能证明所有长期历史或事实更新模式。 Books 复核为`已有覆盖`，owner=`AGENT-MEMORY`；时间索引、层级摘要、检索传播与陈旧/冲突处理已有正文。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](./V3_EVIDENCE_BATCH_01.md)。

### [Selectivity Estimation for Semantic Filters on Image Data](https://arxiv.org/abs/2606.04610v1)

`arXiv:2606.04610v1`，§2 offline embeddings/online estimation、§3 specificity model、compressed KV-cache batching 与 ensemble；把 semantic filter selectivity 变成 query optimizer 的 cost signal。 §3.1 Limitations 与 §6；依赖 embedding/LLM specificity proxy，数据分布漂移和 estimator error 会破坏计划质量。 Books 复核为`已有覆盖`，owner=`AGENT-RAG`；现有检索/query-plan owner 已覆盖质量估计、缓存成本与执行期 fallback。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](./V3_EVIDENCE_BATCH_01.md)。

### [Bridge the Last-Mile Gap to Semantic Analytics: Compiling Natural-Language Queries into Semantic Operator Pipelines](https://arxiv.org/abs/2606.04641v1)

`arXiv:2606.04641v1`，§3 query-data linker、semantic planner、backend code generation 与 cost summary；分离 data-aware semantics 与 backend-specific execution。 §5 Conclusion；对 reference docs、backend API 稳定性和五个 datasets 的依赖不证明开放世界自然语言可无歧义编译。 Books 复核为`已有覆盖`，owner=`AGENT-RAG`；query planning、operator contract、backend adapter 与可验证执行结果已有机制链。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](./V3_EVIDENCE_BATCH_01.md)。

### [CYGNET: Cypher Gate for Neural Execution Triage and Cost Containment](https://arxiv.org/abs/2606.04645v1)

`arXiv:2606.04645v1`，§2 architecture/schema sources、validator backends、mirror graph、equivalence verification、cost gate 与 corrector；在数据库执行前隔离结构错误和高成本计划。 §5 Conclusions；mirror graph/schema coverage、Neo4j planner 与 CypherBench 的结论不外推到任意 tool/database。 Books 复核为`已有覆盖`，owner=`AGENT-TOOL-CALLING`；现有 schema validation、dry-run/sandbox、cost budget 与执行前 authorization 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](./V3_EVIDENCE_BATCH_01.md)。

### [Rethinking Continual Experience Internalization for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.04703v1)

`arXiv:2606.04703v1`，§3 formulation 与 §5 granularity、injection pattern、internalization regime、multi-iteration stability；区分 contextual experience 与 parametric capability 的 owner。 独立 Limitations；指定任务、训练配方与多轮规模不能证明不会遗忘、污染或跨域退化。 Books 复核为`已有覆盖`，owner=`AGENT-MEMORY`；现有“外部记忆优先、参数化吸收需 release/eval gate”已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](./V3_EVIDENCE_BATCH_01.md)。

### [PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents](https://arxiv.org/abs/2606.04780v1)

`arXiv:2606.04780v1`，§3 lifecycle state、online evidence insertion、confidence update、offline consolidation 与 path retrieval；把 persona 更新与证据路径显式化。 exact-v1 未定位独立 Limitations 章节；边界由 benchmark 与 synthetic/curated persona evidence 推得，不能证明真实用户 consent、删除权、身份合并或长期漂移已解决。Books 复核为`已有覆盖`，owner=`AGENT-MEMORY`；现有 provenance、confidence、consolidation、冲突与生命周期 policy 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](./V3_EVIDENCE_BATCH_01.md)。

### [AIP: A Graph Representation for Learning and Governing Agent Skills](https://arxiv.org/abs/2606.04781v1)

`arXiv:2606.04781v1`，§3 Agent Instruction Protocol；把 free-form skill 拆成 graph nodes/edges、preconditions 与 execution/governance metadata。 §4.5 Limitations；单一 benchmark、agent harness 与 graph authoring cost 不能证明所有 skill 可结构化或自动治理。 Books 复核为`已有覆盖`，owner=`AGENT-PLATFORM`；capability registry、typed precondition、version/release 与 policy ownership 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](./V3_EVIDENCE_BATCH_01.md)。

### [Learning While Acting: A Skill-Enhanced Test-Time Co-Evolution Framework for Online Lifelong Learning Agents](https://arxiv.org/abs/2606.04815v1)

`arXiv:2606.04815v1`，§3.1 online lifelong formulation、§3.3 verifier-guided skill learning 与 §3.4 online skill internalization；把 action feedback、skill store 与 test-time policy 更新连成闭环。 §5 Conclusions and Further Work；指定 environments/verifier 的改善不证明开放世界长期安全，也未消除 skill poisoning、遗忘和回滚成本。 Books 复核为`已有覆盖`，owner=`AGENT-MEMORY`；skill write/read、verifier、online update 与 release/fallback 边界已有正文。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](./V3_EVIDENCE_BATCH_02.md)。

### [Channel Fracture: Three Instances of Cross-Boundary Silent Delivery Reliability Failures in Multi-Agent Systems](https://arxiv.org/abs/2606.04896v1)

`arXiv:2606.04896v1`，§3 三种 injection channels/root-cause/fracture pattern 与 §4 CADVP v1.1；关键机制是 receiver-visible confirmation，而不是 writer-side success。 §5 Discussion；只有一个 Hermes/Holographic-memory 实现族和三种通道，不能推为所有多 Agent runtime 的发生率或完整协议。 Books 复核为`已有覆盖`，owner=`AGENT-MULTI-AGENT`；现有跨 Agent handoff、delivery acknowledgement、receiver verification 与 fallback 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](./V3_EVIDENCE_BATCH_02.md)。

### [Audio Interaction Model](https://arxiv.org/abs/2606.05121v1)

`arXiv:2606.05121v1`，§3 always-on perceive–decide–respond、streaming construction/training 与 asynchronous FIFO inference；把 continuous audio 的 state 与 scheduling contract 显式化。 exact-v1 未定位独立 Limitations 章节；边界由作者披露的 audio models/dataset/benchmarks 推得，FIFO 稳定性不等于任意设备、噪声、延迟和 barge-in SLO 已满足。Books 复核为`已有覆盖`，owner=`MULTIMODAL-REPRESENTATION`（系统调度 handoff 至 inference owner）；流式 chunk/state、异步调度与端到端验收边界已有正文链。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](./V3_EVIDENCE_BATCH_02.md)。

### [Streaming Communication in Multi-Agent Reasoning](https://arxiv.org/abs/2606.05158v1)

`arXiv:2606.05158v1`，§3 step streaming algorithm、effectiveness/efficiency characterization；下游 Agent 在上游完整结束前消费经验证的 reasoning step。 §6 Limitation；数学推理 benchmarks、commercial backbones 与固定 topology 不证明任意异步依赖或 tool workflow 保持正确。 Books 复核为`已有覆盖`，owner=`AGENT-MULTI-AGENT`；streaming handoff、partial-state provenance、backpressure 与 correction authority 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](./V3_EVIDENCE_BATCH_02.md)。

### [Discourse-Role Labels as Presentation-Time Variables for Context Use in Language Models](https://arxiv.org/abs/2606.04109v1)

`arXiv:2606.04109v1`，§3 framework/methodology；content-fixed paired variants 隔离 Reference/Evidence/Instruction/Example 标签对 context adoption 的影响。 §7；模型、语言、短答案 probe 与 presentation setting 的边界不等于完整 RAG pipeline 效果。 Books 复核为`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；现有 prompt/template versioning、paired control 与 context-conflict evaluation 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](./V3_EVIDENCE_BATCH_02.md)。

### [The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?](https://arxiv.org/abs/2606.04455v1)

`arXiv:2606.04455v1`，§3 formulation、protocol、sandboxed evaluation architecture 与 integrity；将 agent-building artifact、开发预算和 unseen test 分离。 结果受 task suite、API/time budgets、Harbor sandbox 与 evaluator 实现限制，不能证明自主 agent development 的开放世界能力。 Books 复核为`Only report`，route=`PLATFORM-EVALUATION-SYSTEM`；它是有用的 benchmark contract，但未改变当前通用评测 owner。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](./V3_EVIDENCE_BATCH_02.md)。

### [QO-Bench: Diagnosing Query-Operator-Preserving Retrieval over Typed Event Tuples](https://arxiv.org/abs/2606.04646v1)

`arXiv:2606.04646v1`，§3 denotational retrieval、operator preservation/execution 与 tractable subclass；把 filter/intersection/join preservation 与回答分离验收。 独立 Limitations；financial-event tuple schema、derived gold 与模板集合不代表所有开放文本 query。 Books 复核为`已有覆盖`，owner=`AGENT-RAG`；retrieval recall、operator semantics、structured execution 与 answer verification 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](./V3_EVIDENCE_BATCH_02.md)。

### [Revisiting Vul-RAG: Reproducibility and Replicability of RAG-based Vulnerability Detection with Open-Weight Models](https://arxiv.org/abs/2606.04739v1)

`arXiv:2606.04739v1`，§3 Vul-RAG reconstruction 与 §4 dataset/models/metrics/implementation；贡献是对既有结果的复验边界。 垂直 vulnerability dataset/model slice 不能外推为一般 RAG，且复现失败只约束原 claim 所列设置。 Books 复核为`Only report`，route=`PLATFORM-EVALUATION-SYSTEM`；用于提醒复现与开放权重基线，不形成独立长期机制增量。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](./V3_EVIDENCE_BATCH_02.md)。

### [AutoLab: Can Frontier Models Solve Long-Horizon Auto Research and Engineering Tasks?](https://arxiv.org/abs/2606.05080v1)

`arXiv:2606.05080v1`，§2 task formulation/construction/composition 与 Appendix A scoring anchors/gates；以可执行 artifact 和长时迭代状态验收，而非单轮答案。 独立 Limitations and Broader Impact；32 个系统/CUDA/model tasks 与 harness 资源限制不代表真实科研自主性或安全部署。 Books 复核为`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；现有长程 task、artifact gate、cost/failure taxonomy 与 harness ablation 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](./V3_EVIDENCE_BATCH_02.md)。

### [Failed Reasoning Traces Tell You What Is Fixable (But Not by Reading Them)](https://arxiv.org/abs/2606.05145v1)

`arXiv:2606.05145v1`，§2 operator-class setup/features/recoverability regimes，§3 routing test-time compute，§4 prospective routing policy；用可操作性而非语言解释分配重试。 §9；problem-unit、operator class、temperature 与 backbone 的边界不证明任意 reasoning failure 可被观测或修复。 Books 复核为`已有覆盖`，owner=`INFER-SCHEDULING`（相邻 Evaluation）；failure-aware compute routing、budget 与 fallback 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](./V3_EVIDENCE_BATCH_02.md)。

### [Beyond Single-Policy: Evaluating Composed Organization-Specific Policy Alignment in LLM Chatbots](https://arxiv.org/abs/2606.04394v1)

`arXiv:2606.04394v1`，§3 grounding、composition、query generation 与 policy-handling evaluation；将多条组织 policy 的冲突/组合变成测试对象。 独立 Limitations；30 worlds、synthetic compositions 与 judge 不能代表全部真实制度冲突或法律正确性。 Books 复核为`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`（相邻 Security）；policy composition、冲突矩阵与多层验收已有机制。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](./V3_EVIDENCE_BATCH_02.md)。

### [MemoryDocDataSet: A Benchmark for Joint Conversational Memory and Long Document Reasoning](https://arxiv.org/abs/2606.04442v1)

`arXiv:2606.04442v1`，§3 micro-world/source-dimension benchmark 与 §4 six-stage collection/verification pipeline；显式区分 conversation-only、document-only 与 hybrid evidence。 synthetic micro-worlds、50 worlds/1000 QA 和自动生成 pipeline 不能证明真实长期会话的隐私、更新与噪声边界。 Books 复核为`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`（相邻 `AGENT-MEMORY`）；source-dimension、hybrid evidence 与检索分层验收已有正文。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](./V3_EVIDENCE_BATCH_02.md)。

### [Benchmarking Living-Screen-Native GUI Agents on Short-Video Platforms](https://arxiv.org/abs/2606.04701v1)

`arXiv:2606.04701v1`，§3 continuous evolving state、agent-initiated observation、task construction 与 accuracy/efficiency metrics。 独立 Limitations；short-video platform replica、语言/文化与 annotation scale 使结果不能外推至全部 GUI environments。Books 复核为`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；Ch66“Judge 从被动 Scorer 演进为有预算的 Evidence Acquisition Policy”与 Living-world Evaluation/Run Identity 已覆盖动态观察预算、环境推进与运行身份。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](./V3_EVIDENCE_BATCH_02.md)。

### [Auditing CoT Answer-Hijack Patches: Source-Control Certificates with Type-I Guarantees](https://arxiv.org/abs/2606.04717v1)

`arXiv:2606.04717v1`，§3 K-shot layer disruption、recovery/spread metrics、pre-specified diagnostics；通过 paired source controls 区分 patch 来源与答案恢复。 §10 明示两个 model families、主要 benchmark 与 white-box operator；不构成生产 patch defense 或通用因果证明。 Books 复核为`Only report`，route=`PLATFORM-EVALUATION-SYSTEM`；作为 activation-patching 审计案例，不新增通用系统机制。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](./V3_EVIDENCE_BATCH_02.md)。

### [Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents](https://arxiv.org/abs/2606.04874v1)

`arXiv:2606.04874v1`，§3 task/data/metrics，把 decomposition、tool selection、constraints、broken tools 与 unsolvable tasks 分轴验收。 独立 Limitations；合成 robustness scenarios、tool catalog 与 judge 不能证明真实 workflow 的全部 side effects。 Books 复核为`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；规划分轴、失败注入、不可解判定与 executable validation 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](./V3_EVIDENCE_BATCH_02.md)。

### [Neither Layer Alone: Epistemic Integrity Requires Hierarchical Joint Design for Long-Running AI Agents](https://arxiv.org/abs/2606.04017v1)

精确版本 `2606.04017v1` 的机制与适用条件：把 model 与 harness 分别升级能保持模块自治，却会让 belief、capability 和 goal 在接口处语义漂移。该 position 以 interface contract 组织 goal validity、action archetype、tool instance 与 invocation failure 四级结构，要求持久状态跨 session/版本守恒。 论文提出 architecture/evaluation agenda，没有实现或 benchmark；它支持 long-running Agent 需要 joint conformance，不证明这四层已经充分。contract versioning 和兼容测试有成本，短期无持久状态任务仍可使用平面 action loop。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#neither-layer-alone-epistemic-integrity-requires-hierarchical-joint-design-for-long-running-ai-agents)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../../books/part-07-agent/84-agent-platform.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Token Budgets: An Empirical Catalog of 63 LLM-Agent Budget-Overrun Incidents, with an Affine-Typed Rust Mitigation as a Case Study](https://arxiv.org/abs/2606.04056v1)

精确版本 `2606.04056v1` 的机制与适用条件：- The 21 sub-projects comprising the catalog corpus were selected from GitHub repositories tagged llm-agent , agent-framework , ai-agent , or llm-orchestration with ≥ 1,000 \geq 1{,}000 stars as of January 2026 in Python, TypeScript, or Rust, and filtered to those that either (a) expose a budget/cost/token-limit option in their public API or (b) have a GitHub issue mentioning cost overrun or runaway-spend in the title. Retained projects span the LangChain/LangGraph, AutoGPT, CrewAI, AutoGen, Pyd（完整论证及边界见下方原文审阅，不以此摘录代替它）

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#token-budgets-an-empirical-catalog-of-63-llm-agent-budget-overrun-incidents-with-an-affine-typed-rust-mitigation-as-a-case-study)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Covert Influence Between Language Models](https://arxiv.org/abs/2606.04071v1)

精确版本 `2606.04071v1` 的机制与适用条件：- §3–4: a sender model can encode influence in apparently ordinary generated content consumed by a receiver, shifting provenance and trust ownership from human-visible text to the model-to-model channel.

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#covert-influence-between-language-models)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../../books/part-06-ai-infrastructure/72-security.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Proof-Carrying Agent Actions: Model-Agnostic Runtime Governance for Heterogeneous Agent Systems](https://arxiv.org/abs/2606.04104v1)

精确版本 `2606.04104v1` 的机制与适用条件：- Abstractly, PCAA seeks a control mechanism M M that minimizes severe missed escalations while respecting review budgets and runtime-boundary constraints: The important point is not the specific loss function. PCAA does not treat average scoring quality as the sole endpoint. It treats selective routing, explicit review semantics, and certificate closure as the actual runtime trust problem.

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#proof-carrying-agent-actions-model-agnostic-runtime-governance-for-heterogeneous-agent-systems)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../../books/part-06-ai-infrastructure/72-security.md))；现有正文对照及采用边界以本报告当前判断为准。

### [EvalStop: Using World Feedback to Detect and Correct Reward Overoptimization in Multi-Tenant RLHF Platforms](https://arxiv.org/abs/2606.04145v1)

精确版本 `2606.04145v1` 的机制与适用条件：- Recall the architecture overview in Figure 1 . EvalStop is a composable wrapper around any base scheduling policy. It monitors eval-score trajectories (the world feedback signal) and early-stops jobs when quality is irrecoverably declining.

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#evalstop-using-world-feedback-to-detect-and-correct-reward-overoptimization-in-multi-tenant-rlhf-platforms)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为整合：`TRAIN-RLHF`（[books/part-04-training-system/31-rlhf.md](../../../../../books/part-04-training-system/31-rlhf.md)）；正文锚点“训练停止不能只看 Training Loss 或 Reward Model Score”；下游 world-feedback/eval trajectory 驱动多租户 RLHF 作业 early stop 与 GPU 释放；现有正文对照及采用边界以本报告当前判断为准。

### [Notarized Agents: Receiver-Attested Confidential Receipts for AI Agent Actions](https://arxiv.org/abs/2606.04193v1)

精确版本 `2606.04193v1` 的机制与适用条件：- A Sello receipt is a COSE_Sign1 envelope wrapping an HPKE-encrypted payload. The structure is: p ​ k owner pk_{\text{owner}} is the owner’s X25519 public key, bound to the authorization token (Section 4.2) s ​ k service sk_{\text{service}} is the service’s Ed25519 private signing key The body is defined in CDDL [ Birkholz et al., 2019 ] notation, where ? denotes an optional field: receipt-body = { agent-identifier: tstr, ; derived from token hash action-type: tstr, ; e.g.

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#notarized-agents-receiver-attested-confidential-receipts-for-ai-agent-actions)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../../books/part-06-ai-infrastructure/72-security.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Puffin-Backed Vector Indexes: Attaching Approximate Nearest Neighbor Indexes to Apache Iceberg Snapshots for Compute-Disaggregated Query Engines](https://arxiv.org/abs/2606.04196v1)

精确版本 `2606.04196v1` 的机制与适用条件：- §3–4: the ANN index is attached to an Apache Iceberg snapshot through Puffin metadata, making index identity and lifecycle follow immutable table snapshots rather than an external mutable service.

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#puffin-backed-vector-indexes-attaching-approximate-nearest-neighbor-indexes-to-apache-iceberg-snapshots-for-compute-disaggregated-query-engines)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-RAG`（[books/part-07-agent/76-rag.md](../../../../../books/part-07-agent/76-rag.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Can Generalist Agents Automate Data Curation?](https://arxiv.org/abs/2606.04261v1)

精确版本 `2606.04261v1` 的机制与适用条件：- Three additional LLM-driven components are part of the methodology rather than the writing process. The four trajectories labels in Table 1 (new policy, grounded, effective, shallow) are produced with LLM assistance using Claude Opus 4.7, following the rubric in Section 2.2 . We treat these labels as diagnostic annotations rather than ground-truth scientific claims, and we provide rubrics and trace examples to support auditing.

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#can-generalist-agents-automate-data-curation)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`TRAIN-DATA`（[books/part-04-training-system/27-data.md](../../../../../books/part-04-training-system/27-data.md))；现有正文对照及采用边界以本报告当前判断为准。

### [The Saturation Trap and the Subjectivity of Intervention Timing: Why Affect-Based Triggers and LLM Judges Fail to Time Interventions on Autonomous Agents](https://arxiv.org/abs/2606.04296v1)

精确版本 `2606.04296v1` 的机制与适用条件：- We separate the system into three independent layers, a structure maintained throughout development and documented in a contemporaneous design log.

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#the-saturation-trap-and-the-subjectivity-of-intervention-timing-why-affect-based-triggers-and-llm-judges-fail-to-time-interventions-on-autonomous-agents)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有正文对照及采用边界以本报告当前判断为准。

### [LazyAttention: Efficient Retrieval-Augmented Generation with Deferred Positional Encoding](https://arxiv.org/abs/2606.04302v1)

精确版本 `2606.04302v1` 的机制与适用条件：- In this section, we show how the positional information of reused documents can be adjusted during the attention calculation. Then we analyze the cost of deferred positional encoding for prefilling and decoding, respectively. Inspired by the analysis, we present how to integrate LazyAttention with FlashAttention ( Dao et al., 2022 ; Dao, 2024 ; Shah et al., 2024 ) seamlessly to achieve efficient computation.

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#lazyattention-efficient-retrieval-augmented-generation-with-deferred-positional-encoding)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Organizational Control Layer: Governance Infrastructure at the Execution Boundary of LLM Agent Systems](https://arxiv.org/abs/2606.04306v1)

精确版本 `2606.04306v1` 的机制与适用条件：- We study how platforms should control agent-mediated economic decisions before they affect real users, merchants, or transactions.

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#organizational-control-layer-governance-infrastructure-at-the-execution-boundary-of-llm-agent-systems)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../../books/part-06-ai-infrastructure/72-security.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Exploring Cross-Scenario Generality of Agentic Memory Systems: Diagnostics and a Strong Baseline](https://arxiv.org/abs/2606.04315v1)

精确版本 `2606.04315v1` 的机制与适用条件：- Algorithm 1 defines the canonical AutoMEM design: a multi-step plan–execute–judge loop that can re-query memory when the judge finds the trace insufficient. This iterative form is what delivers the accuracy in Table 8 . On top of long context’s single LLM call, the loop issues three to four calls per question (planner, optional dump, judge, answerer), and the outer loop can issue further calls when the judge requests more evidence (Table 9 ).

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#exploring-cross-scenario-generality-of-agentic-memory-systems-diagnostics-and-a-strong-baseline)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../../books/part-07-agent/77-memory.md))；现有正文对照及采用边界以本报告当前判断为准。

### [The Digital Apprentice: A Framework for Human-Directed Agentic AI Development](https://arxiv.org/abs/2606.04321v1)

精确版本 `2606.04321v1` 的机制与适用条件：- Per-skill autonomy tiers, explicit human graduation and runtime drift correction form an inference-time authorization/control plane.

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#the-digital-apprentice-a-framework-for-human-directed-agentic-ai-development)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../../books/part-07-agent/84-agent-platform.md))；现有正文对照及采用边界以本报告当前判断为准。

### [From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents](https://arxiv.org/abs/2606.04329v1)

精确版本 `2606.04329v1` 的机制与适用条件：MPBench 把攻击拆为 memory write channel、结构漏洞、写入策略与后续检索触发。memory store 持有持久状态，外部 payload 是不可信数据，write/retrieve policy 掌握纳入上下文的控制权；实现以一次投毒写入和后续独立会话中的读取构成端到端事务。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260604329--from-untrusted-input-to-trusted-memory-a-systematic-study-of-memory-poisoning-attacks-in-llm-agents)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../../books/part-07-agent/77-memory.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Not All Errors Are Equal: Consequence-Aware Reasoning Compute Allocation](https://arxiv.org/abs/2606.04402v1)

精确版本 `2606.04402v1` 的机制与适用条件：轻量 consequence predictor 从任务描述估计错误成本，scheduler 在总预算下选择模型/思考层级。request 保存 consequence estimate，候选解是数据流，budget allocator 掌握额外推理调用的控制权。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260604402--not-all-errors-are-equal-consequence-aware-reasoning-compute-allocation)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为仅报告：当前窗口上下文，不形成独立长期机制；现有正文对照及采用边界以本报告当前判断为准。

### [FlexNPU: Transparent NPU Virtualization for Dynamic LLM Prefill-Decode Co-location](https://arxiv.org/abs/2606.04415v1)

精确版本 `2606.04415v1` 的机制与适用条件：FlexNPU 在 phase granularity 暴露虚拟 NPU，并动态映射 prefill/decode execution state。runtime 持有虚拟资源与队列，KV/request phase 是数据状态，placement/isolation controller 决定算力和带宽归属。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260604415--flexnpu-transparent-npu-virtualization-for-dynamic-llm-prefill-decode-co-location)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`INFER-PD-DISAGGREGATION`（[books/part-05-inference-system/55-pd-disaggregation.md](../../../../../books/part-05-inference-system/55-pd-disaggregation.md))；现有正文对照及采用边界以本报告当前判断为准。

### [What If Prompt Injection Never Left? Rethinking Agent Security through Cross-Session Stored Prompt Injection](https://arxiv.org/abs/2606.04425v1)

精确版本 `2606.04425v1` 的机制与适用条件：论文建立 write–persistence–incorporation–activation 生命周期和 sandbox。持久介质保存攻击状态，clean victim query 触发重新纳入，context constructor 掌握从存储到可执行上下文的数据控制权。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260604425--what-if-prompt-injection-never-left-rethinking-agent-security-through-cross-session-stored-prompt-injection)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../../books/part-07-agent/77-memory.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Token Rankings are Unforgeable Language Model Signatures](https://arxiv.org/abs/2606.04459v1)

精确版本 `2606.04459v1` 的机制与适用条件：方法把多次 query 的 token order 组成 ranking signature，再做识别/近似参数恢复。API response 持有排序数据，query adversary 控制采样输入，signature matcher 掌握模型归属判定。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260604459--token-rankings-are-unforgeable-language-model-signatures)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为仅报告：当前窗口上下文，不形成独立长期机制；现有正文对照及采用边界以本报告当前判断为准。

### [ANN Search: Recall What Matters](https://arxiv.org/abs/2606.04522v1)

精确版本 `2606.04522v1` 的机制与适用条件：论文用 1/Ratio@k 比较返回邻居与真实邻居的距离质量，并把 metric 作为 index tuning objective。索引持有候选集合，distance 是数据证据，benchmark/tuner 决定 latency–quality operating point。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260604522--ann-search-recall-what-matters)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Cartridges at Scale: Training Modular KV Caches over Large Document Collections](https://arxiv.org/abs/2606.04557v1)

精确版本 `2606.04557v1` 的机制与适用条件：CAS 用 dynamic distractor mixing 训练可组合 per-document cartridges，并由 budget manager 在 GPU 与持久存储间轮换。cartridge 是版本化 KV artifact，selector 决定加载集合，cache manager 掌握驻留和 token budget。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260604557--cartridges-at-scale-training-modular-kv-caches-over-large-document-collections)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Multi-SPIN: Multi-Access Speculative Inference for Cooperative Token Generation at the Edge](https://arxiv.org/abs/2606.04581v1)

精确版本 `2606.04581v1` 的机制与适用条件：Multi-SPIN 让设备 SLM 产出 drafts、edge LLM 批量验证，并联合优化 draft length、频分带宽和计算分配。每用户 draft/acceptance 是状态，radio/compute budget 是资源数据，central optimizer 掌握分配控制。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260604581--multi-spin-multi-access-speculative-inference-for-cooperative-token-generation-at-the-edge)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`INFER-SPECULATIVE-DECODING`（[books/part-05-inference-system/48-speculative-decoding.md](../../../../../books/part-05-inference-system/48-speculative-decoding.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Ekka: Automated Diagnosis of Silent Errors in LLM Inference](https://arxiv.org/abs/2606.04594v1)

精确版本 `2606.04594v1` 的机制与适用条件：Ekka 对齐 target 与 reference implementation 的中间 execution states，逐层/逐算子做 differential diagnosis。reference trace 是正确性证据，target trace 是观测数据，alignment/search controller 定位首个 divergence。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260604594--ekka-automated-diagnosis-of-silent-errors-in-llm-inference)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-TRACE`（[books/part-06-ai-infrastructure/69-trace.md](../../../../../books/part-06-ai-infrastructure/69-trace.md))；现有正文对照及采用边界以本报告当前判断为准。

### [RAMPART: Registry-based Agentic Memory with Priority-Aware Runtime Transformation](https://arxiv.org/abs/2606.04628v1)

精确版本 `2606.04628v1` 的机制与适用条件：RAMPART 以 named block registry 保存 provenance/priority/authorship，并在 compile context 前执行 promote、gate、write、evict、rollback。registry 持有状态，blocks 是数据，policy engine 掌握上下文编译权。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260604628--rampart-registry-based-agentic-memory-with-priority-aware-runtime-transformation)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../../books/part-07-agent/77-memory.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Description-Code Inconsistency in Real-world MCP Servers: Measurement, Detection, and Security Implications](https://arxiv.org/abs/2606.04769v1)

精确版本 `2606.04769v1` 的机制与适用条件：DCIChecker 联合 schema-aware static analysis 与 LLM classifier，对 description、signature、implementation effects 建立一致性检查。代码与描述是双份接口数据，server owner 维护实现，release gate 决定不一致是否阻断发布。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260604769--description-code-inconsistency-in-real-world-mcp-servers-measurement-detection-and-security-implications)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-MCP`（[books/part-07-agent/83-mcp.md](../../../../../books/part-07-agent/83-mcp.md))；现有正文对照及采用边界以本报告当前判断为准。

### [UModel: An Agent-Ready Observability Data Modeling Method at Scale](https://arxiv.org/abs/2606.04799v1)

精确版本 `2606.04799v1` 的机制与适用条件：UModel 建虚拟 ontology，把 telemetry、entities 与 expert knowledge 映射为 object graph，并由 U-SPL pipeline 查询。object identity/relations 是共享状态，source adapters 供数据，query planner 掌握跨源探索控制。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260604799--umodel-an-agent-ready-observability-data-modeling-method-at-scale)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-TRACE`（[books/part-06-ai-infrastructure/69-trace.md](../../../../../books/part-06-ai-infrastructure/69-trace.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Provably Auditable and Safe LLM Agents from Human-Authored Ontologies](https://arxiv.org/abs/2606.04903v1)

精确版本 `2606.04903v1` 的机制与适用条件：Ontology-First design 由人定义 typed domain ontology/roles，Agentic Redux 用 typed lambda calculus 约束步骤并写 append-only ledger。ontology 持有规范状态，typed terms 是数据，checker/role policy 掌握执行授权。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260604903--provably-auditable-and-safe-llm-agents-from-human-authored-ontologies)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为仅报告：当前窗口上下文，不形成独立长期机制；现有正文对照及采用边界以本报告当前判断为准。

### [GNStor: Design of GPU-Native High-Performance Remote All-Flash Array](https://arxiv.org/abs/2606.04908v1)

精确版本 `2606.04908v1` 的机制与适用条件：GNStor 把 NVMe-over-RDMA request path 和部分 AFA functionality 下沉到 GPU，GPU queues 持有 I/O state，RDMA/NVMe buffers 是数据，GPU-side stack 掌握提交与完成控制。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260604908--gnstor-design-of-gpu-native-high-performance-remote-all-flash-array)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为仅报告：当前窗口上下文，不形成独立长期机制；现有正文对照及采用边界以本报告当前判断为准。

### [Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2606.04923v1)

精确版本 `2606.04923v1` 的机制与适用条件：CHERRL 可控注入 judge bias，跟踪 reward divergence/hacking onset，并用 agent detector 搜索作弊行为。rubric/judge 持有评价状态，policy outputs 是数据，RL optimizer 把 judge signal 转成权重更新控制。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260604923--reproducing-analyzing-and-detecting-reward-hacking-in-rubric-based-reinforcement-learning)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Sequential Data Poisoning in LLM Post-Training](https://arxiv.org/abs/2606.04929v1)

精确版本 `2606.04929v1` 的机制与适用条件：论文定义分别污染 SFT/preference datasets 的多攻击者 threat model，比较单阶段、分预算与协作 poison。dataset owners 持有阶段数据，checkpoint 传递隐藏状态，pipeline orchestrator 掌握阶段顺序和晋级。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260604929--sequential-data-poisoning-in-llm-post-training)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../../books/part-06-ai-infrastructure/72-security.md))；现有正文对照及采用边界以本报告当前判断为准。

### [SharedRequest: Privacy-Preserving Model-Agnostic Inference for Large Language Models](https://arxiv.org/abs/2606.05004v1)

精确版本 `2606.05004v1` 的机制与适用条件：SharedRequest 生成 noisy prompt variants、按语义等价 instruction 分组并在 batch level 共享请求。client 持有敏感原文和扰动，grouping service 控制批合并，remote model 只接收混合后的请求集合。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260605004--sharedrequest-privacy-preserving-model-agnostic-inference-for-large-language-models)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为仅报告：当前窗口上下文，不形成独立长期机制；现有正文对照及采用边界以本报告当前判断为准。

### [Validity Threats for Foundation Model Research](https://arxiv.org/abs/2606.05029v1)

精确版本 `2606.05029v1` 的机制与适用条件：框架把研究设计映射到 statistical、internal、external、construct validity，并为三类低成本 strategy 建立 characteristic threat profile。experiment design 持有 estimand，observations 是证据数据，claim gate 决定可外推范围。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260605029--validity-threats-for-foundation-model-research)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Self-Reflective APIs: Structure Beats Verbosity for AI Agent Recovery](https://arxiv.org/abs/2606.05037v1)

精确版本 `2606.05037v1` 的机制与适用条件：self-reflective API 返回 machine-readable recovery_feedback.suggestions[]，将失败字段、修复动作和 retry 输入结构化。server 持有 schema truth，error payload 是控制数据，agent retry loop 决定是否应用建议。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260605037--self-reflective-apis-structure-beats-verbosity-for-ai-agent-recovery)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-TOOL-CALLING`（[books/part-07-agent/78-tool-calling.md](../../../../../books/part-07-agent/78-tool-calling.md))；现有正文对照及采用边界以本报告当前判断为准。

### [Strabo: Declarative Specification and Implementation of Agentic Interaction Protocols](https://arxiv.org/abs/2606.05043v1)

精确版本 `2606.05043v1` 的机制与适用条件：Strabo 把 UCP checkout 建模为 declarative Langshaw protocol，并用 Peach agents 执行且与 Google UCP agents 互操作。protocol artifact 持有允许交互状态，messages 是数据，runtime verifier 掌握 transition control。

完整方法、评价、关键反证与未披露字段见[该家族的原文审阅](./V2_1_EVIDENCE_ARCHIVE.md#260605043--strabo-declarative-specification-and-implementation-of-agentic-interaction-protocols)；复用精确版本的证据，不继承旧报告完成标签或旧 owner。当前 Books 处置为已有覆盖：`AGENT-MULTI-AGENT`（[books/part-07-agent/82-multi-agent.md](../../../../../books/part-07-agent/82-multi-agent.md))；现有正文对照及采用边界以本报告当前判断为准。
