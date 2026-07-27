# AI Research Weekly — 2026-W19

> Coverage Window: 2026-05-04～2026-05-10
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-09
> Re-audit Status: 2026-08-14 Source-Family Books Gate Complete; 35/35 final dispositions; 25 Refine, 6 No Change, 3 Weekly Only, 1 Unverified / Blocked; 19 Stable Node owners changed or revalidated; Historical Archive/Discovery Gate Open

## Executive Summary

旧版 W19 只保留三项机构来源，无法证明论文和 AI Infra 候选池完整。baseline 中 Anthropic 的
Natural Language Autoencoders 与 Teaching Claude why 分别探索内部状态的
自然语言可读接口和基于解释/原则的行为训练；OpenAI 更新 voice models。长期价值在于：
可读解释、训练理由与外部行为是三类证据，必须通过 intervention 和 deployment evaluation
连接，不能互相替代。扩大扫描恢复 22 个本周 `20+` 学术候选，并把 5 个 first-public date
属于 W18 的条目回拨。ARIS 已完成全文审计：它把 research harness 分成 execution、orchestration
和 assurance，并以 evidence-to-claim ledger、fresh reviewer 与 artifact contract 对抗“看似成功、
证据不足”；但当前只有单条 observational deployment trajectory，compute-matched controlled
benchmark 明确仍是 future work。HeavySkill、T2PO 与 PhysicianBench 已完成全文审计；MolmoAct2
的 v2 正文、代码、数据和部署说明现已恢复，审计保留 v1 事件日期与 v2 机制证据的边界。OpenSeeker-v2、Rethinking
Reasoning-Intensive Retrieval、Workspace-Bench、AI co-mathematician、Auto Research with
Specialist Agents、A2TGPO、STALE、UniPrefill、LLMs Improving LLMs、HyperEyes、Soohak、MCP-Cosmos、MemPrivacy 与 Geometry Conflict
也已完成全文审计。OpenSearch-VL 与 Skill1 的正文也已恢复并完成 method、implementation、evaluation、
Appendix 与 limitations 审计；StraTA 的 arXiv 正文仍被当前访问路径阻断，只保留已核验 metadata 与
精确材料请求，不以摘要代替全文。fixed official/Infra 复扫又恢复 EMO、GPT-5.5 Instant、ERNIE 5.1、Kubernetes manifest
admission、declarative validation、server-side sharded list/watch、DRA 1.36、NCCL Inspector real-time
mode、vLLM 0.20.1～0.20.2 patch series 与 NSF OMAI 十个 source families。EMO 已按完整论文、Appendix、
代码、模型和数据入口审计；其 document-level shared expert pool 说明 MoE modularity 必须在训练目标中形成，
不能从 token-level sparse routing 自动推出。Kubernetes 四项机制分别恢复 policy bootstrap、validation
shadow/takeover、controller state partition 与 device allocation readiness 的长期系统边界。当前 scored
candidate review queue 已闭合；一项 blocked source 与尚未闭合的 Scholar/OpenAlex/DBLP 历史交叉召回
进入 post-forward backlog，不再阻塞已验证 Source Family 的 Books Gate。35 项已有最终 disposition，
25 项机制级 refine 已由 19 个 Stable Node owners 吸收或章节级复核；Archive/Discovery Gate 继续保持打开。

## Coverage and Source Coverage

- 模型与研究机构：保留 Anthropic 5 月 7/8 日与 OpenAI 5 月 7 日条目；补入 OpenAI GPT-5.5
  Instant 的 5 月 4 日 system card / 5 月 5 日 product node、Ai2 EMO 5 月 7 日论文与 5 月 8 日
  release、Baidu ERNIE 5.1 5 月 9 日正式发布，以及 Ai2 NSF OMAI 5 月 7 日基础设施状态。
- 论文与学术来源：已重放 Hugging Face W19/W20 推荐流并逐项核对 arXiv v1，恢复 22 个
  in-window families、回拨 5 个 W18 spillbacks；ARIS 与 EMO 已完成正文、appendices 与 artifact
  entry 审计。OpenReview/TMLR、DBLP、Scholar/OpenAlex 的历史交叉召回仍 pending。interpretability/alignment
  结论继续标记 Experimental。
- AI Infra：已核验 Kubernetes 1.36 四项 feature Blog + docs/KEP、NCCL 2.30 Inspector Blog +
  repository、vLLM 0.20.1/0.20.2 releases + relevant PR。voice API 与 vLLM patch series 都保留
  version boundary；任何 latency/throughput 数字都没有脱离其公开 workload contract。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Natural Language Autoencoders | 4 | 4 | 3 | 4 | 4 | 5 | 24/30 | Worth Watching |
| Teaching Claude why | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Worth Watching |
| OpenAI voice models | 3 | 3 | 4 | 5 | 3 | 3 | 21/30 | Official product state |
| MolmoAct2 | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full review complete — provisional Refine Ch10 / Experimental |
| ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Must Read — full review complete |
| Skill1 | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full review complete — provisional Refine Ch73 / Experimental |
| OpenSearch-VL | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Full review complete — provisional Refine Ch29 / Experimental |
| OpenSeeker-v2 | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Full review complete — provisional No Change Ch23 |
| Rethinking Reasoning-Intensive Retrieval | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full review complete — provisional Refine Ch72 |
| StraTA | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Unverified / Blocked Backlog — paper full text unavailable |
| HeavySkill | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full review complete — provisional Refine Ch78 |
| AI co-mathematician | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full review complete — provisional Refine Ch77 |
| Auto Research with Specialist Agents | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full review complete — provisional Refine Ch77 |
| A2TGPO | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Full review complete — provisional Refine Ch29 |
| Workspace-Bench 1.0 | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Full review complete — provisional Refine Ch62 |
| T2PO | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Full review complete — provisional Refine Ch29 |
| PhysicianBench | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full review complete — provisional Refine Ch62 |
| MemPrivacy | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Full review complete — provisional Refine Ch68 / Experimental |
| Soohak | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full review complete — No Change Ch62 |
| LLMs Improving LLMs | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Full review complete — provisional Refine Ch77 |
| HyperEyes | 5 | 5 | 5 | 4 | 4 | 3 | 26/30 | Full review complete — provisional Refine Ch29 |
| MCP-Cosmos | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full review complete — No Change Ch75 |
| Geometry Conflict | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Full review complete — provisional Refine Ch25 / Experimental |
| STALE | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full review complete — provisional Refine Ch73 |
| UniPrefill | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full review complete — provisional Refine Ch39 |
| GPT-5.5 Instant system card and release | 3 | 5 | 4 | 5 | 5 | 4 | 26/30 | Full review complete — No Change Ch62/68; W17 source-family branch |
| EMO: Pretraining Mixture of Experts for Emergent Modularity | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Full review complete — provisional Refine Ch21 / Experimental |
| ERNIE 5.1 official release | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Full review complete — provisional Refine Ch29/37 / Official Engineering Evidence |
| Kubernetes Manifest-Based Admission Control | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full review complete — provisional Refine Ch68; Alpha |
| Kubernetes Declarative Validation GA | 4 | 5 | 5 | 5 | 4 | 3 | 26/30 | Full review complete — provisional Refine Ch53 |
| Kubernetes Server-Side Sharded List and Watch | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Full review complete — provisional Refine Ch53; Alpha |
| Kubernetes DRA 1.36 evolution | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full review complete — provisional Refine Ch59 |
| NCCL Inspector Prometheus Mode | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full review complete — provisional Refine Ch63 |
| vLLM v0.20.1-v0.20.2 stabilization series | 3 | 4 | 4 | 5 | 5 | 3 | 24/30 | Full review complete — Weekly Only / Ch46 version evidence |
| NSF OMAI compute online | 2 | 3 | 3 | 5 | 3 | 2 | 18/30 | Low-score boundary — infrastructure availability, mechanism not disclosed |

本轮账目为 35 行：27 个 `25～30`、7 个 `20～24`、1 个 `<20`。评分只决定阅读优先级，
不等于 Books disposition。

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Baseline score rows | 3 | 3/3 `20+` Source Reviews retained |
| Recovered academic candidate families | 23 | 22 项 recovered families 已完成 Full Source Review（含 EMO）；StraTA 为唯一 blocked backlog；0 current-review pending |
| Recovered official / Infra families | 9 `20+` + 1 low | 9/9 `20+` Full Source Reviews；NSF OMAI 完成低分来源/边界核验 |
| W18 spillbacks | 5 | 按 arXiv v1 回拨，不在 W19 重复计分 |
| W20-feed spillbacks | 8 | v1 在 05-07～05-10，归 W19 而不按推荐流周标签归档 |
| Academic discovery window | Open | HF first pass + EMO correction complete；formal/cross indexes pending |
| Official / Infra discovery window | Checkpoint Passed | fixed accessible sources replayed；product/version facts separated from mechanisms |
| W19 Evidence Gate | Open | 34 total `20+`；33 Full Source Reviews complete；1 blocked backlog；1/1 low boundary；0 current-review pending；cross-index coverage 未闭合；fixed-source forward checkpoint passed |

## Evidence Level

自然语言重建内部状态不自动等于 faithful explanation；alignment behavior 的改善绑定训练与
评测设置；voice model 结论绑定官方产品环境。GPT-5.5 Instant 的 safety 结果绑定 system-card
scaffold、reasoning effort、grader、sample 与 safeguards，不能作为基础模型或生产流量的普遍比例。
ARIS 是作者 technical report 与公开 artifact
支持的系统描述，不是 controlled effectiveness study：单次八小时 run 只能证明 workflow 能执行，
不能证明 cross-family reviewer 优于 same-family/self-review，或证明两 Agent 是最优拓扑。

## Deep Analysis — Research Agent 的核心对象从回答变成 Claim Lineage

长任务最危险的失败不一定是 crash，而是 artifact 看起来完整、claim 却超出 raw evidence。
ARIS 将这一风险拆成三层：experiment-integrity 检查 reference、metric、result file 与 scope；
result-to-claim 将结果变成 supported/partial/invalidated ledger；fresh reviewer 再从 manuscript
回查 ledger、configuration 与 raw artifacts。其演进路线是：

```text
single-agent end-to-end generation
→ self-review / same-context revision
→ independent artifact review
→ evidence-to-claim lineage with separate assurance state
```

它获得可恢复的 artifact contract、明确的 claim downgrade 和 reviewer independence，却引入
额外模型成本、reviewer bias、context disclosure 与 convergence-policy 风险。fresh context 减少
confirmation bias，却丢失跨轮问题历史；cross-round reviewer 能检查修复，却可能继承 framing。
两者应按 assurance stage 共存，不能把“换一个模型”当作独立真相。human owner 仍拥有研究方向、
证据接受与提交 authority。

## Cross-Week Deduplication

与 W04 assistant axis 的关系是 interpretability evidence ladder 上的后续案例，不应将
decodability 静默升级为 causal control。W19 feed 中 Ctx2Skill、MiniCPM-o 4.5、Web2BigTable、
WindowsWorld 与 Beyond Semantic Similarity 的 v1 属于 W18，已回拨。W20 推荐流中的 MemPrivacy、
Soohak、LLMs Improving LLMs、HyperEyes、MCP-Cosmos、Geometry Conflict、STALE 与 UniPrefill
也按 v1 归回 W19。ARIS 与 W17 ClawEnvKit、
W18 AutoResearchBench 是 `Layering / Dependency`：environment 产生可执行 evidence，research
workflow 维护 claim lineage，reviewer 只做带偏差的 judgment。GPT-5.5 Instant 是 W17 GPT-5.5
source family 的 deployment/safety branch，不重复解释未公开模型内部；ERNIE 5.1 则是 W18 Preview
的 formal release node，Preview 没有被倒写成已经公开完整 runtime。Kubernetes DRA 1.36 延续
W18/W20 的 device/workload scheduling evolution；NCCL Inspector real-time mode 是旧 JSON/offline
Inspector 上的 `Direct Evolution`，不是替代 fine-grained trace。

## Knowledge Tree Position

Ch5 representation → Ch27 alignment → Ch62 evaluation → Ch68 safety → Ch77 Workflow →
Ch80 Agent Platform。ARIS 主 owner 暂定 Ch77，Ch62/Ch80 只作 handoff。

## Recommended Action

W19 的 Source-Family Books Gate 已完成；后续只在 Archive backlog 追踪 StraTA 正文与
Scholar/OpenAlex/DBLP 交叉召回。已吸收内容按 owner 章节继续维护，不按论文追加：EMO 进入 MoE objective；
UniPrefill 进入 Prefill execution-state；ARIS 进入 Evaluation assurance；STALE 进入 Memory adjudication；
Kubernetes validation/sharding 进入 Platform control-plane；NCCL Inspector 进入 Monitoring。新来源若不能改变
这些机制、适用条件或 failure modes，应保持 `No Change`，避免重复正文。

## Event-Date Daily Decision

2026-05-04～05-08：Historical Weekly only；不补造 Daily。

## Books Integration Decision

`Source-Family Books Gate Complete`。35/35 final dispositions：25 `Refine — Existing Argument`、
6 `No Change — Already Covered`、3 `Weekly Only`、1 `Unverified / Blocked / No Books Change`。
19 个 Stable Node owners 完成修改或章节级复核；详细 owner、current/legacy chapter 与证据边界见文末最终账本。
StraTA 与 cross-index recall 只保持 Archive Gate open，不允许进入 Books，也不再把已验证 family 的 Books
Integration 伪装成未开始。

## Ignored Noise

把可读文本当成模型真实、完整、无损的“思想”；把单条 overnight research run 或 reviewer
internal score 当成 cross-model assurance 有效性的因果实验。

## Full Source Review

### ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration — 27/30

- **Candidate / Week / Source Family**：`ARIS-RESEARCH-HARNESS-ASSURANCE`；W19；
  arXiv:2605.03042 v1，2026-05-04。当前只有 v1；仓库/technical report 的版本事实按访问时状态
  记录，不把后来 code changes 倒写为首发机制。
- **Direct / Related Primary Sources**：arXiv abstract、完整 HTML/PDF、作者 GitHub repository；
  相关 autonomous-research 与 multi-agent 文献只用于比较，不能替代 ARIS 自身 evaluation。
- **Access / Full-read Coverage**：已读 Introduction、三层 architecture、五条 design principles、
  cross-model collaboration、完整 assurance stack、skill/wiki/workflow/tool implementation、
  meta-optimization、deployment evidence、limitations/responsible use、Related Work、Conclusion，及
  Appendix A～E 的 workflow figures、skill inventory、reviewer access/context matrix、CLI details
  和尚未执行的 controlled benchmark protocol。
- **Original Problem / Why Previous Design Was Reasonable**：single-agent pipeline 或 same-model
  self-review 部署简单、context 共享、token/API 成本低，并适合低风险 draft 与短任务；但长周期
  research 会跨 literature、code、experiment、claims 和 manuscript，显式 crash 之外还存在
  `plausible unsupported success`：结果可能真实但被错报，或 claim 超出 evidence scope。
- **Changed Constraint / Principle**：当 artifact 跨 session、模型和执行环境持续演进时，review
  不能只读 executor 的摘要；持久状态、模块化恢复与独立 assurance 必须成为 workflow state。
  cross-family reviewer 是降低相关误差的 candidate mechanism，不是已证明的 universal rule。
- **Mechanism**：execution layer 提供 65+ Markdown skills、model/tool bridges 与 research wiki；
  orchestration layer 组合 idea discovery、experiment bridge、auto-review、paper writing、rebuttal；
  assurance layer 先审 evaluation code/result integrity，再把 result 映射为 supported/partial/invalidated
  claims，最后让 fresh zero-context reviewer 将 manuscript quantitative claims 回查 raw results、
  config 与 ledger。review loop 默认阈值 6/10、最多四轮；experiment failure 最多三次 retry，且
  至少尝试两种 remediation，之后可引入第三模型诊断。
- **State Ownership / Control Flow / Data Flow**：workflow owner 持有 stage、budget、checkpoint 和
  convergence；skill invocation 持有局部 procedure；artifact store/wiki 持有 papers、ideas、
  experiments、claims 与 typed relations；executor 产生 code/result/manuscript；reviewer 产生 advisory
  issue/verdict；human 持有最终研究方向、evidence acceptance、harness patch 与 submission authority。
  正确流向是 `raw run/config → integrity audit → result-to-claim ledger → manuscript claim audit →
  human decision`，review score 不得反向成为实验 ground truth。
- **Implementation Details**：skills 用 `SKILL.md` 与共享 policy documents 表达，跨 stage 通过
  versionable Markdown artifacts 传递；wiki 使用 canonical IDs 和八类 typed relations，并保留
  rejected ideas。reviewer 配置把 access scope（document/artifact/repository）与 context policy
  （fresh/cross-round）分成正交轴。FigureSpec 在固定 renderer/font 下生成 SVG；prototype
  meta-loop 记录 events、分析 failure/override/plateau，只将 `>=7/10` 的 harness patch proposal
  交给用户，不能 auto-apply。repository-level external review 可能暴露代码，local-only path 尚未实现。
- **Evaluation Contract**：论文没有完成 controlled benchmark。部署证据包括 3 个 tested executor、
  3 个 adaptation guides、6+ reviewer families、4 类 GPU backend，以及一条约八小时、四轮 review、
  20+ GPU experiments、internal score 5.0→7.5 的 trajectory。作者明确称全部为 observational；
  没有 task pool、same-family/self-review control、matched tokens/cost/latency、blinded human labels、
  variance 或 failure-rate comparison。Appendix E 仅提出未来 12+ drafts、五种 compute-matched
  conditions、issue recall/false-positive/actionability/revision quality/cost/latency 与三名 blinded
  raters/Krippendorff alpha 的计划，不是已获得的结果。
- **What the Evidence Proves**：公开实现和单条 run 证明该 harness 可以把 skills、checkpoint、
  artifact lineage、claim downgrade、fresh review 与 human-gated meta-change 组合为可执行 workflow；
  不能证明 cross-family review 的独立增益、两 Agent 最优、review score 等价科学质量，或任何
  productivity/correctness headline。
- **What It Does Not Prove / Threats to Validity**：executor/reviewer 可能共享训练数据、evaluation
  taste 与 blind spots；reviewer bias 会在多轮中被放大；fresh context 降低 framing carry-over 但
  丢失历史，cross-round context 相反。claim ledger 只能约束被记录的 evidence，不能发现全部
  fabrication、novelty conflict 或 methodological error。报告由系统自身协助撰写，虽有人工负责，
  仍存在 self-referential selection bias。
- **Trade-offs / New Failure Modes**：独立 assurance 增加 issue recall 的可能性，也增加 API cost、
  latency、confidentiality exposure、false positives、reviewer preference overfitting 与 convergence
  deadlock；artifact persistence 提高 replay，却引入 stale claim、supersession、retention 和 access
  control。fresh/cross-round review 不是单向升级，而是 independence 与 continuity 的选择。
- **Where Previous Design Still Applies / Evolution**：短、低风险、容易 deterministic verify 的任务
  仍适合 single-agent 或同模型 self-check；高风险 claim、跨 session experiments 与外部 publication
  才值得多层 assurance。关系是 `Direct Evolution`：single pipeline → artifact review → claim
  lineage；相对 Ch62 evaluation 与 Ch80 platform 是 `Layering / Dependency`，reviewer 不拥有
  evaluator truth 或 deployment authority。
- **ROADMAP / Chapters / Existing Coverage**：主 owner 暂定 Ch77；已读 Ch77 与 Ch80，并核对
  Ch62 的 EvalSpec、per-example evidence、claim provenance 和 decision contract；联读 Ch78 的
  topology/communication tax。现有 Ch77 已覆盖 deterministic spine、evaluator-driven search、
  artifact identity、replay、approval 与 human authority；长期缺口是 evidence-to-claim cascade 与
  fresh/cross-round reviewer 两轴，不需要新增章节。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument`；
  Historical Books Gate 关闭，当前只更新 W19。待验证：controlled protocol 完成后 cross-family
  effect 是否仍存在；claim ledger 的 supersession/invalidation 谁拥有；repository review 如何在
  local-only、secret redaction 与 least-privilege 下保持 artifact access。

### Natural Language Autoencoders — 24/30

- **Source Family ID / Type / Date**：`NLA-INTERPRETABILITY`；Anthropic 2026-05-07 research post、
  transformer-circuits full paper、code 与 interactive artifact。
- **Full-read Coverage**：已覆盖 activation→language encoder、language→activation reconstructor、
  reconstruction objective、experiments、comparisons、interventions、failure cases 与 limitations。
- **Problem / Previous Design / Changed Constraint**：SAE/attribution graph 提供局部 feature/circuit
  证据且可干预，但解释成本高；自然语言接口提高人类可读性，却必须防止“能重构”被误认为
  “完整忠实描述”。
- **Mechanism / Ownership / Flow**：一个模型把 activation 压缩为文本，另一个模型从文本重构
  activation；reconstruction 作为训练 proxy。interpretability pipeline 拥有 explanation artifact，
  原模型 activation 是被测状态，reviewer 必须用 counterfactual intervention 判断 causal relevance。
- **Evidence / Limits / Trade-offs**：作者案例显示文本 bottleneck 可保留对某些 downstream behavior
  有用的信息并辅助调试；它不证明文本覆盖全部内部状态、无 evaluator/model prior 泄漏或是模型
  “真实思想”。readability 换来 lossy bottleneck、plausible narrative 和同源模型 bias。
- **Evolution / Decision**：SAE/graph→NLA 是 `Layering / Explanatory Interface`，不是替代；
  Ch5 主 owner，已读 Ch4～6、Ch27、Ch62、Ch68；`No Change — Already Covered`，现有 evidence
  ladder 已要求 correlation→intervention→replication。

### Teaching Claude why — 24/30

- **Source Family / Coverage**：`PRINCIPLE-BASED-ALIGNMENT-TRAINING`；Anthropic 2026-05-08 官方
  technical report；已覆盖 direct eval-distribution training、constitutional documents、stories、
  demonstrations+reasons、data diversity、held-out honeypot evaluation 和 limitations。
- **Mechanism / Evidence Boundary**：把行为例子与其原则/理由共同训练，试图使 policy 在 OOD
  场景复用更抽象的 decision rule；作者案例显示 held-out alignment assessment 改善，但来自单一
  model family 和自有 eval，不能证明普遍 OOD robustness 或内部价值稳定。
- **Trade-offs / Evolution**：direct behavior cloning 对已知分布高效但易窄化；principle/reason
  增加抽象迁移，也引入文字原则歧义、reward/evaluator coupling 和 rationalization。两者共存。
- **ROADMAP / Decision**：Ch27 主 owner，已读 Ch26～28、Ch62、Ch68；
  `No Change — Already Covered`，现有 alignment 章节已保留 principle、demonstration 与 eval 分层。

### OpenAI voice models — 21/30

- **Source / Verification**：OpenAI 2026-05-07 official release 与 API model documentation 已核对；
  支持的 modality/availability 属版本事实，训练和 realtime runtime 机制 `Not Disclosed`。
- **Decision**：Ch38～40、Ch74 已读；`Weekly Only — Version/Product Fact`。无完整 hardware、
  concurrency、audio length、latency distribution 与 SLO，不写通用 voice serving 结论。

### MolmoAct2 — 27/30 — Full Source Review Complete

- **Source Family / Revision / Access**：`MOLMOACT2-OPEN-VLA`；arXiv:2605.02881 v1 的
  first-public date 为 2026-05-04，全文核验使用可访问的 v2（2026-05-08）以及作者代码、模型和数据入口。
  v2 只补足机制与限制，不倒写成新的 W19 event。
- **Original Problem / Previous Design**：离散 VLM 擅长空间推理，连续高频控制则需要平滑 action
  trajectory；旧方案在每一步生成密集 reasoning token 或预测帧，能提高 grounding，却让 reasoning
  latency 支配闭环控制。直接用 embodiment-specific policy 计算更轻，但难以复用跨平台知识。
- **Mechanism / State and Data Flow**：系统先以 specialize-then-rehearse 训练 Molmo2-ER，再用公开的
  FAST tokenizer 预训练离散 action token。post-training 增加 DiT-style continuous action expert；每层
  expert cross-attend 对应 VLM layer 的 projected KV，flow-matching loss 只更新 expert/adapters，KV 在
  进入 expert 前 detach，VLM 仍由 LM loss 更新。MolmoAct2-Think 只重预测相邻时刻发生变化区域的
  depth token，以利用场景时间冗余。model owns reasoning/action generation；embodiment adapter、camera、
  calibration 与 action convention 仍由 deployment owner 管理。
- **Implementation / Evaluation Contract**：post-training 的 robot/VLM sequence length 分别为
  2,100/4,200，global batch 128，64 张 H100，约 2,304 GPU-hours；论文覆盖 7 个模拟/真实环境、
  out-of-box/fine-tune/OOD robustness、conditioning/flow samples/depth/fine-tune ablation 与 inference
  speed。真实机器人比较绑定 DROID、SO-100/101 的特定相机、对象和任务设置，不能外推为任意
  embodiment 的可靠性。
- **Evidence Boundary / Trade-offs**：实验支持 per-layer KV conditioning、adaptive-depth 与特定
  fine-tune recipe 在作者设置中的增益；不证明跨机器人零配置迁移，也不证明实时控制已解决。论文明确
  action chunks 缺少 real-time re-chunking，并需要 embodiment-specific adaptation；新增 failure modes
  包括 stale chunk、calibration/action-space mismatch、expert/backbone coupling 和多数据源分布漂移。
  低延迟旧 policy 在稳定单一 embodiment 仍合理。
- **ROADMAP / Disposition**：已读 Ch10、Ch17、Ch23、Ch38 及邻接节点。主 owner 暂定 Ch10，
  Ch17/23/38 只作 architecture/training/serving handoff；`Refine — Existing Argument`，
  `Status: Experimental`。Historical Books Gate 关闭，不写 Books。

### OpenSearch-VL — 26/30 — Full Source Review Complete

- **Source Family / Date / Coverage**：`OPENSEARCH-VL-MULTIMODAL-SEARCH`；arXiv:2605.05185 v1，
  2026-05-06。已读 data construction、SFT/RL、tool environment、evaluation、ablation 与 Appendix；
  可访问正文未提供独立 production deployment study。
- **Original Problem / Changed Constraint**：text-only search agent 无法处理图像实体、文档布局和模糊视觉
  证据；单纯增加 ImageSearch 又会把“找到相似图”误当成可引用证据。workload 变成多跳、跨模态、
  需要图像修复/OCR/裁剪并把 observation 放回推理链。
- **Mechanism / Ownership / Flow**：Wikipedia hyperlink path 产生 2～4 hop VQA，经过 fuzzy rewrite、
  source-anchor image grounding、tool-demand filtering 和真实工具环境 rejection sampling，形成
  SearchVL-SFT-36K 与 RL-8K。agent 生成 query/tool action；environment 拥有 TextSearch、ImageSearch、
  OCR、Crop、Sharpen、SuperResolution、PerspectiveCorrect 的执行和 observation；训练时 observation
  token 不归 policy 生成。fatal-aware GRPO 在工具致命失败后 mask suffix，并只让有利 advantage 更新
  失败前 action，避免错误环境后缀污染 credit。
- **Evaluation Contract / Boundary**：在 Qwen3-VL 8B、30B-A3B、32B 上评测 7 个 multimodal search
  benchmark；expert trajectory 使用 Claude Opus 4.6，rejection/process judge 与 Pass@1 evaluator 使用
  GPT-4o。实验和 ablation 支持该 data/tool/RL recipe 在作者 harness 中有效，但 evaluator coupling、
  remote API 漂移和 Wikipedia 构造分布限制了外推；没有公开生产并发、端到端成本、SLO 或 tool outage
  failure distribution。
- **Trade-offs / Evolution**：从 text retrieval 演进为 multimodal observation loop，获得可恢复的视觉
  证据与工具组合，却新增 remote-service provenance、图像 URL 可达性、OCR/修复失真、judge bias、
  tool error masking 和 prompt injection 面。纯文本检索在 evidence 已文本化、成本/SLO 更紧时仍合理。
- **ROADMAP / Disposition**：已读 Ch29、Ch72、Ch74、Ch77 及相邻章节。主 owner 暂定 Ch29，
  Ch72/74 只承接 retrieval/tool boundary；`Refine — Existing Argument`，`Status: Experimental`。
  Historical Books Gate 关闭。

### Skill1 — 27/30 — Full Source Review Complete

- **Source Family / Revision / Coverage**：`SKILL1-SELECT-USE-DISTILL`；arXiv:2605.06130 v1，
  2026-05-07；全文核验使用当前 v3（2026-05-12），revision 不作为新事件。已读 algorithm、reward、
  experiments、ablation、statistics、hyperparameters 与 limitations。
- **Original Problem / Previous Design**：静态 skill library 能复用历史经验，但 selection、utilization 与
  distillation 常被分开优化：selector 不知道执行结果，executor 不影响 library，新增 skill 也未与现有
  coverage 比较。简单保存成功 trajectory 在小库中合理，但规模增长后会出现冗余、低效检索与 stale skill。
- **Mechanism / State Ownership**：policy 先用 embedding top-K 和 learned reranking 选 skill，再执行任务；
  成功 rollout 反思出 strategy 与 applicability description。library 对每个 skill 维护 utility EMA、selection
  count 与容量；训练时 UCB 兼顾探索，评测时 greedy，达到 5,000 容量后按 utility 与使用次数联合淘汰。
  utilization 用 task outcome；selection 的 query 通过 rollout prefix 获得 policy gradient，reranker 另有
  utility-weighted signal；distillation reward 衡量新成功结果是否超过已检索 skill 的 utility。policy owns
  generation，library service owns admission/utility/retirement；这一边界不能混成“模型自然记住技能”。
- **Evaluation Contract / Evidence**：ALFWorld 与 WebShop，GRPO learning rate 1e-6、group size 16、
  prompt/response 16,384/2,048、vLLM TP=4；结果三次独立 seed，并报告 ablation 与 Welch test。部分
  baseline 数字来自既有论文，只有 RetroAgent 用官方实现复现，因而 headline 排名不是严格统一
  compute/system contract。
- **Trade-offs / Failure Modes**：共同信用分配获得 library-policy co-evolution，却新增 non-stationary
  utility、UCB exploration cost、成功样本偏置、错误反思进入库、retirement 不可逆和 library provenance/
  rollback 缺口。作者实验只覆盖两个 text environments，没有验证跨域迁移、并发更新、恶意 skill、
  privacy/delete 或长期 supersession；小而稳定的 curated skill set 仍适合高风险生产环境。
- **ROADMAP / Disposition**：已读 Ch29、Ch73、Ch80 及相邻章节。主 owner 暂定 Ch73，Ch29/80 只作
  training/registry handoff；`Refine — Existing Argument`，`Status: Experimental`。Historical Books Gate
  关闭。

### StraTA — 26/30 — Unverified / Blocked Backlog

- **Source Family / Date / Access**：`STRATA-TRAJECTORY-ABSTRACTION`；arXiv:2605.06642 v1，
  2026-05-07。候选 metadata、日期与 trajectory abstraction、credit assignment、strategy/action
  ownership、overhead 等待审范围已经登记；当前无法取得完整正文或可联合核验的作者 artifact。
- **Verified Boundary / Why This Is Not a Full Review**：无法判断 abstraction 是训练时 latent state、
  显式 strategy artifact 还是 rollout 后处理，也无法核验 action-level credit、控制流、state ownership、
  matched-compute baseline、sensitivity、failure case 与实际 overhead。因此不能把候选主题写成已经证明的
  agentic-RL 演进。
- **Disposition**：`Unverified / Blocked Backlog`。保留 26/30 discovery score，不计入 Full Source
  Review，不进入 Books。primary source 恢复后再决定 Ch29、Ch77 或 Ch78 的 owner；forward cursor
  继续后续候选。

### Post-forward blocker recovery — 2026-08-13

MolmoAct2、OpenSearch-VL 与 Skill1 的 arXiv HTML 已恢复；三项按正文、Appendix 及可用 artifact
完成非模板化 Source Review，并保留 first-public version 与当前可读 revision 的边界。StraTA 的精确
arXiv HTML 仍返回访问错误，也没有定位到可替代正文的作者 artifact；它是 W19 唯一剩余 blocked family。

### AI co-mathematician — 25/30

- **Candidate / Source Family / Revision**：`AI-CO-MATHEMATICIAN-STATEFUL-WORKBENCH`；W19；
  arXiv:2605.06651 v1，2026-05-07。全文核验使用 2026-05-13 的 v2；v2 只用于补足机制、案例、
  benchmark 与 limitations，不倒写为 W19 新事件。
- **Direct / Related Primary Sources and Full-read Coverage**：已读 arXiv v2 的 design principles、
  workspace walkthrough、hierarchical delegation、hard constraints、review/final artifact、interactive
  evaluation、三个 mathematician case studies、internal benchmark、FrontierMath、全部 challenges/
  limitations 与 conclusion。产品 prototype 和内部实现未公开，公开事实边界以论文为止。
- **Original Problem / Previous Design / Changed Constraint**：单轮 solver、formal prover 和可验证
  program search 在目标固定、answer contract 清晰时合理；真正 research 却要持续澄清问题、并行探索、
  管理不确定性、保存失败分支并让人类中途改变方向。约束从“求一个答案”变为“维护可审计的未知状态”。
- **Mechanism / State Ownership / Flow**：human 与 project coordinator 先迭代定义并批准 question/goals；
  coordinator 为每个 goal 创建可追加的 parallel workstreams，workstream coordinator 再调用 literature、
  code、Deep Think 等 specialists。共享 filesystem 保存 incremental report、attachments、failed outcomes
  与 working paper；internal messaging 承担 escalation。每个 workstream 产出带 margin annotations、内部/
  外部链接和 research-process exposition 的 LaTeX artifact，经持久 reviewer agents 审批；无法收敛则
  标记 unfinished 并上报，而非伪装完成。human 拥有 goal approval、steering、trust weighting 与最终
  scientific judgment；reviewer approval 不是 theorem truth。
- **Evaluation Contract / Evidence**：三个 early-user case studies 来自小规模 professional-user release，
  作者明确报告满意度不一且个案缺少多次采样/controlled condition。内部 benchmark 为 100 个未泄漏、
  research-level、code-checkable problems；只报告 system 对 Gemini 3.1 Pro/Deep Think 的提升，没有公开
  完整逐题 contract。Epoch AI blind 操作 FrontierMath Tier 4 UI，排除两个公开样题后为 23/48；system
  每题可运行 48 小时、没有 model-call/token 上限，并使用自有工具，不能与受限 harness/model call 做
  matched-compute 因果比较。该结果证明 harness+models+tools 的系统能力，不隔离 branching、review、
  filesystem 或 model upgrade 的单独贡献。
- **Limitations / Trade-offs / New Failure Modes**：review loop 可能收敛到 reviewer 不再能识别错误的
  false consensus，也可能因 disagreement non-termination 后进入 hallucination death spiral；长时间自主
  工作增加 controllability 风险。精美 LaTeX 会制造 rigor illusion，生成吞吐也把 verification 成本推给
  人类与 peer review。自动 reviewer 擅长局部 logical/citation checks，不拥有 elegance、depth、novelty
  或 significance 的判断权。
- **Evolution / Previous Design Still Applies**：`single answer → tool-using solver → persistent workspace
  + parallel workstreams → human-steered uncertainty lifecycle` 是 `Layering / Dependency`，不是自治替代
  人类。固定、可形式验证的题仍适合短 solver/formal prover；开放 research 才需要 goal approval、negative
  history、native artifacts 与 escalation。下一阶段压力是 human-in-loop collaboration、halt/disclose
  uncertainty 和 verification labor 的可重复评测。
- **ROADMAP / Adjacent Chapters / Decision**：主 owner Ch77；已联读 Ch76～78，并核对 Ch62 与 Ch80。
  Ch77 已覆盖 durable state、artifact identity、approval/replay 与 human authority；本项新增的稳定缺口是
  `goal approval → branching workstream → reviewed native artifact → unfinished escalation` 以及 reviewer-
  pleasing/non-termination 的对称 failure semantics。provisional `Refine — Existing Argument`；Historical
  Books Gate 关闭，当前只更新 W19。

### Auto Research with Specialist Agents Develops Effective and Non-Trivial Training Recipes — 27/30

- **Candidate / Source Family / Revision**：`AUTO-RESEARCH-SPECIALIST-LINEAGE`；W19；
  arXiv:2605.05724 v1，2026-05-07；作者公开 repository 与 frozen trace/archive。
- **Full-read Coverage**：已读 methodology、task/evaluator contract、submitted-trial loop、specialist
  partition、lineage/anti-anchoring、parallel throughput、三个 headline runs、matched controls、discussion/
  limits、全部 Appendices A～L 的 prompts、tools、status taxonomy、run configuration、hardware、
  calibration、no-lineage ablation、final recipes、failure/audit cases 与 releasable trace schema。
- **Original Problem / Previous Design / Changed Constraint**：HPO/grid search 与单 Agent proposal 在搜索面
  小、参数可枚举时便宜透明；但真实 training recipe 同时包含 architecture、data、optimizer、loss、kernel
  与 hard budget，crash/oversize/accuracy miss 也携带下一次 edit 所需的信息。当每个 experiment 可在有限
  时间内由外部 evaluator 返回，research object 可从建议变为连续的 executable feedback loop。
- **Mechanism / Ownership / Flow**：task package 固定 editable files、metric、legality、submission path、
  prompts/knowledge 与 specialist taxonomy；bounded session 从 current-best code 与 compact lineage 读取
  frontier、recent role/adjacent-role trials、crash/dead-end banlist，提出 hypothesis、生成 canonical code
  diff 并提交。recipe 不能编辑 evaluator；外部 evaluator 写 append-only score/status/time/bytes/failure，
  supervisor 更新 shared blackboard，后续 session 才消费。role 只是 proposal-surface prior，truth 由
  evaluator-owned measurement 和 legality gate 决定；human 在一次 setup/launch 后没有选 trial、改 recipe、
  override score 或修 crash，但仍拥有 task/evaluator/budget 和最终采用权。
- **Implementation / Evaluation Contract**：Parameter Golf 每 trial 为 fresh 8×H100、16 MB artifact、
  10-minute train 与 600-second evaluation；NanoChat-D12 也是 fresh 8×H100、90-minute pretraining；CIFAR
  在 long-lived GPU worker 上保留预热 CUDA context，以 0.96 accuracy gate 约束 speed。全部 roles 使用
  Claude Opus 4.7，thinking budget 8000、最多 200 tool turns；48-hour deadline 或 4-hour no-improvement
  grace 停止。headline 有 900/200/97 个 trials，另有三个 matched 200-trial Parameter Golf controls；
  public calibration 负责避免 stale denominator。
- **What the Evidence Proves / Does Not Prove**：在三套固定、廉价、机器可验证环境中，公开 trace 证明
  Agent 能把 code edit、valid result、crash、budget overrun、size block 与 gate miss转成后续 program-level
  edits。Parameter Golf 同 budget 对照显示 role+lineage、generic-10、single generalist、no-lineage 的最终
  bpb 和有效改进数不同；no-lineage 还显著更常撞 evaluation cap，支持“measured lineage 是 active search
  state”。三个 headline 的 0.81% bpb、38.7% CORE、4.59% wallclock 仅属于各自起点、数据、hardware、
  evaluator 与 budget；不证明跨任务通用收益、paradigm-level invention 或 specialist 数量的普遍最优。
- **Ablation / Threats / Trade-offs**：no-lineage ablation 关闭 prompt、tools 与 blackboard reads，但仍保留
  current-best score/code 与 static priors，这是可编辑 loop 的不可消除 residual。role swarm 与 generic
  control 的差异主要是 idea diversity/boundary discipline 而非 raw throughput；共享 GPU queue 与 filelock
  使 10-way efficiency 低于 1。proposal-cluster 指标来自 hypothesis text，只描述 submitted surface，
  不代表 latent ideas。系统更适合 objective、fast、trusted feedback；subjective/slow/non-reproducible
  research 会让 lineage stale、Goodhart 或过拟合 evaluator。
- **Evolution / Previous Design Still Applies**：`one-shot suggestion → executable trial → evaluator-owned
  append-only lineage → role-partitioned parallel search` 是 `Direct Evolution`。小搜索面仍适合 grid/HPO；
  单 Agent 在低并发与强局部上下文中更简单；只有便宜且可隔离 evaluator 的实验才值得持续 swarm。
  失败不是噪声，而是带类型、时间、budget 与 diff lineage 的 boundary evidence。
- **ROADMAP / Adjacent Chapters / Decision**：主 owner Ch77，Ch62/Ch78 短 handoff；已联读 Ch76～78、
  Ch62 与 Ch80。Ch77 已有 evaluator-driven search 与 durable workflow，本项补足 `submitted trial` 作为
  research unit、evaluator/write isolation、failure taxonomy、anti-anchoring lineage 和 matched no-lineage
  evidence。provisional `Refine — Existing Argument`；Books Gate 关闭，当前不改 Books。

### A2TGPO — 26/30

- **Candidate / Source Family / Revision**：`A2TGPO-TURN-GROUP-CREDIT`；W19；
  arXiv:2605.06200 v1，2026-05-07；作者 repository `CuSO4-Chen/A-TGPO`。
- **Full-read Coverage**：已读 motivation/related work、formal rollout/IG definition、三项 method 与完整
  objective、七个 datasets/三种 backbones、所有 baselines、main results、component ablations、training/
  advantage dynamics、Algorithm 1、reward/prompt/search environment、hyperparameters/hardware、overhead、
  single-hop ablation、beta sensitivity、turn/context distributions、theoretical assumptions 与 case study。
- **Original Problem / Previous Design / Changed Constraint**：trajectory reward/GRPO 对 final answer 稳定且
  无额外 process model，但多轮 tool trajectory 无法知道哪个 turn 有贡献；PRM 增加 evaluator，tree rollout
  限制多样性，IGPO 用 policy 对 ground-truth answer 的概率变化提供内生信号，却把不同 turn position
  混合归一化、随 remaining depth 累加不同数量的项，并用固定 clip 处理信息量不同的 turns。
- **Mechanism / State Ownership / Flow**：environment 拥有 observations，rule-based evaluator 拥有 final
  exact-match/format reward，policy 产生 turns 并以自身对 ground-truth answer 的 likelihood difference 计算
  stop-gradient IG。A2TGPO 在同一 prompt、同一 turn index 的 rollout peers 内 z-normalize IG；若该深度
  只剩一个 rollout 则过程信号置零。下游 normalized IG 反向折扣累加并除以 remaining-turn count 的平方根，
  再加 per-prompt outcome advantage；同一 normalized IG 通过 bounded sigmoid 调整该 turn 的 clipping
  range。importance ratio 以 turn 内 token-ratio 几何均值计算，credit、ratio 与 update granularity 对齐。
- **Evaluation Contract**：local e5-base-v2 retriever 覆盖约 21M Wikipedia entries、每次 top-3，最多 6 个
  tool turns；rollout group 16、train batch 64、mini-batch 8、max prompt 2000、response 6192、AdamW 1e-6。
  Qwen3-4B/8B 与 Qwen2.5-7B 在单节点 8×NVIDIA H20 上训练评估，比较 ReAct、GRPO、DAPO、GSPO、
  Tree-GRPO、GiGPO、IGPO、AEPO，覆盖四个 multi-hop 与三个 single-hop QA，主指标 EM。Tree-GRPO 在
  Qwen3 reproduction 频繁 crash，故只在 Qwen2.5-7B 报告，不能按空白结果宣称优势。
- **Evidence / Ablation / Sensitivity**：三种 backbone 的表格与 Qwen3-4B additive ablation 支持在该
  contract 下 turn-group normalization、sqrt-rescaled accumulation、adaptive clipping 各有增益；
  beta 在 0.2～0.4 区间相对稳定、0.3 最佳。context similarity 随 turn 深度下降，说明“同 turn 等价状态”
  只是早期更强的近似。额外 IG forward pass 约 164 秒，但因 generation 变快，作者测得 240 steps 中
  per-step 约 525s vs 511s、净 +2.9%；该 offset 依赖 length/batch tail，不能外推其他 serving/training。
- **What It Does Not Prove / Threats**：IG 需要训练时 ground-truth answer，policy likelihood 既不是事实
  correctness 也不是 tool-call causal contribution；错误校准或 shortcut memorization 会污染 credit。
  深 turn 的 peer group 变小且 trajectory 已分叉，z-score 方差增加；平方根方差推导依赖弱相关近似，
  covariance 非零时并非严格同方差。单一 local-Wikipedia search、EM reward、最多六 turns 不证明长 horizon、
  subjective、open-ended 或异构工具任务有效。
- **Trade-offs / Evolution / Previous Design Still Applies**：`trajectory outcome → state/tree/process credit →
  IGPO pooled turn signal → position-conditioned IG + depth-normalized credit + adaptive update` 是 `Direct
  Evolution`。可验证答案且同 prompt 有足够 rollout peers 时 A2TGPO 有意义；ground truth 不可得、group
  很小、turn identity 与 semantic state 偏离或额外 forward 成本过高时，outcome-only、PRM 或 explicit
  environment-state grouping 仍成立。新 failure mode 是把 policy confidence 递归强化为训练 authority。
- **ROADMAP / Adjacent Chapters / Decision**：主 owner Ch29；已联读 Ch27～30，并核对 Ch62、Ch77。
  Ch29 已覆盖 group-relative reward、partial rollout、staleness 与 credit boundary；本项补足“comparison
  cohort、credit accumulation 与 policy-update granularity 必须同构”的 turn-level机制。provisional
  `Refine — Existing Argument`；Historical Books Gate 关闭期间不修改 Books。

### HeavySkill — 24/30

- **Candidate / Source Family / Revision**：`HEAVYSKILL-PARALLEL-DELIBERATION`；W19；
  arXiv:2605.02396 v1，2026-05-04；作者 code repository。当前 revision history 只有 v1。
- **Full-read Coverage**：已读 Introduction、parallel reasoning、serialized/pruned/shuffled memory
  cache、sequential/iterative deliberation、readable skill、STEM/general/tool-use experiments、trajectory
  selection、RL scaling、limitations/trade-offs、appendix prompts 与 artifact入口。
- **Original Problem / Previous Design**：Best-of-N 或 majority vote 对独立 samples 选择/聚合，机制简单、
  并行度高、适合 verifier 清晰且 candidate 中已有正确答案的任务；完整 multi-agent harness 则能表达
  tool、memory 与角色分工，但容易把模型本身的 test-time reasoning headroom 误归因给 orchestration。
- **Changed Constraint / Mechanism**：当多条 trajectory 包含互补局部证据时，仅投票丢失推理路径。
  HeavySkill 先以同一输入并行生成 K 条 trajectory，再裁剪、打乱并序列化到 memory cache，由第二阶段
  deliberator 生成 K' 个综合答案；可迭代把前轮综合结果写回 cache，也可封装为可移植 skill。state
  owner 是 orchestrator/cache，不是任何一条 trajectory；summarizer 只产生新 candidate，不拥有 truth。
- **Evaluation Contract**：主实验采用 K=8/16、temperature 1.0、top-p 0.95、top-k 10，通常两阶段使用
  同一模型；比较 Mean@K、Pass@K、Vote@K、Heavy Mean/Pass@4，覆盖 AIME25、BeyondAIME、HMMT、
  GPQA、LiveCodeBench、IFEval 与 Arena-Hard，并以 Python tool-use 做扩展。Appendix 还从每题 256 条
  trajectories 比较 random、max-diversity、max-length 与 high-frequency selection。公开结果支持：
  verifiable STEM/code/instruction tasks 常受益，Arena-Hard 这类 preference task 收益小或为负；迭代
  depth 提高平均结果时会降低 potential pass，显示历史噪声/偏差累积。没有 matched end-to-end
  latency、KV/memory footprint、provider pricing、cross-seed confidence interval 或生产任务研究。
- **Evidence Boundary / Failure Modes**：论文证明“并行样本 + synthesis”在给定模型、prompt、采样与
  benchmark 下可以超过均值/投票，并有时合成原始 answers 中未出现的正确结果；不证明它内化成了
  参数能力、取代 Multi-Agent/Workflow，或在主观/高副作用任务有效。新增成本是 K-fold generation、
  cache truncation、position/order bias、summarizer correlated error、verbosity noise 与 iterative
  contamination；max-length selection 的退化也说明 longer reasoning 不是质量 proxy。
- **Evolution / Previous Design Still Applies**：`single response → Best-of-N/vote → parallel reasoning +
  sequential deliberation → learned depth/width` 是 `Direct Evolution`，不是线性替代。答案可验证且
  latency budget 充足时 synthesis 值得；低延迟、subjective preference、强顺序工具或 candidate 已有
  deterministic verifier 时，单样本/BoN/固定 Workflow 更合理。
- **ROADMAP / Adjacent Chapters / Decision**：主 owner Ch78；已读 Ch77～78，并核对 Ch29 的 group
  rollouts 与 Ch62 scorer boundary。Ch78 已要求先比较 single Agent、deterministic verifier 与 parallel
  tools，但尚未明确“并行 reasoning + synthesis”作为 multi-agent 之前的强 baseline，以及 iterative
  depth 的信息污染。provisional `Refine — Existing Argument`；Books Gate 关闭，当前不改 Books。

### T2PO — 26/30

- **Candidate / Source Family / Revision**：`T2PO-MULTITURN-EXPLORATION-CONTROL`；W19；
  arXiv:2605.02178 v1，2026-05-04；作者 code 基于 verl/vLLM。当前只有 v1。
- **Full-read Coverage**：已读 background、uncertainty signal、TTI、TDS、policy update、WebShop/
  ALFWorld/Search QA setup、main results、module/control-method ablations、sensitivity、efficiency、policy
  lag、hyperparameters、algorithms、codebase 与 failure case。
- **Original Problem / Previous Design**：trajectory filtering、process reward、GRPO/GiGPO credit
  assignment 和 hard length budget 分别降低坏 trajectory、稀疏 reward 或 rollout 成本，且在短任务中
  易实现；但多轮 rollout 会在 token 内持续低信息 over-thinking，也会跨 turn 重复无进展 action，稀疏
  reward 把这些噪声一起归因，造成高方差甚至 collapse。
- **Mechanism / Ownership / Flow**：策略在每 token 输出 entropy 与 top-j confidence，沿当前
  trajectory 归一化并融合为 self-calibrated signal；TTI 在滑窗内边际变化低于阈值后强制发出
  `</think>\n<action>`，只允许一次触发。TDS 把每 turn token uncertainty 作几何聚合，与前 turn
  比较；变化低于阈值则在同一 environment state 重采样，直到信息变化或预算耗尽。environment 拥有
  state/reward，rollout controller 拥有 stop/resample budget，policy 产生 proposal，learner 用 trajectory
  与 turn-relative advantage 更新；uncertainty 是控制信号，不是 correctness authority。
- **Implementation / Evaluation Contract**：memory context 只保留最近 P turns；RFT cold start、format
  penalty 与 group-in-group advantage 和 TTI/TDS 共同存在。主实验用 Qwen3-RFT 系列、8×H100 单节点、
  synchronous vLLM rollout、TP=1、group size 5/8，max response 500、thinking budget 450；WebShop 最多
  15 turns，ALFWorld 50，Search 4。相对 GRPO、GiGPO、GiGPO+DAPO 及 length reward、short-CoT、
  hard budget、void-turn filtering做比较，并分别消融 TTI/TDS、alpha 与响应长度。结果支持在这些
  environment/seed/config 下更低方差、更少无效 turns 和更高 success；16% fewer turns 只属于
  ALFWorld 作者实验，不能外推成通用效率。
- **Evidence Boundary / Threats**：论文没有证明 entropy/confidence 的局部稳定等价“没有有效新思路”，
  也未隔离 RFT、format penalty、memory window、advantage estimator 与 TTI/TDS 的全部交互。信号按单条
  trajectory 自归一化，跨 task/calibration 可漂移；强制结束可能截断 late recovery，turn resampling
  增加 tail cost。appendix 明确 pipelined rollout 会产生 policy lag；正文实验却使用 synchronous
  rollout，因此“自然扩展 async”是实现主张，不是异步稳定性证据。
- **Evolution / Previous Design Still Applies**：`fixed max length → reward/filter-based coarse control →
  token stop + turn resample → policy-learned adaptive exploration` 是 `Direct Evolution`。确定性短任务、
  calibration 不可靠或 resampling 昂贵时 fixed budget/void filtering 仍成立；长 horizon 且环境可安全
  reset/replay 时，分层控制更有价值。
- **ROADMAP / Adjacent Chapters / Decision**：主 owner Ch29；已读 Ch27～29，并核对 Ch77 的 durable
  workflow state。Ch29 已覆盖 group-relative reward、rollout cost、partial rollout、staleness 与 reward
  measurement，但缺少“exploration control 本身也是 rollout policy”的 token/turn 双层机制。provisional
  `Refine — Existing Argument`；不在 Historical Books Gate 前修改 Books。

### PhysicianBench — 27/30

- **Candidate / Source Family / Revision**：`PHYSICIANBENCH-EXECUTION-GROUNDED-EHR`；W19；
  arXiv:2605.02240 v1，2026-05-04；官方 project/repository。当前只有 v1。
- **Full-read Coverage**：已读 Related Work、FHIR environment formalization、task/checkpoint curation、
  physician review、agent loop/tool inventory、three grader types、model setup、reliability/failure analysis、
  privacy pipeline、robustness guards、additional results 与 representative failure trajectory。
- **Original Problem / Previous Design**：医学 QA、static record 与 single-step tool benchmark 成本低、
  易复现，适合隔离 knowledge/retrieval/API correctness；但不能证明 Agent 能完成“检索→临床判断→
  structured write→documentation”的 composite workflow，尤其会把文字上说要做的动作误当成已执行。
- **Mechanism / State Ownership / Flow**：100 个 physician-authored/reviewed tasks 在 task-local Docker
  中运行独立 HAPI FHIR R4 server；agent 只能主动查询部分 observation，并通过 13 个 FHIR read/write
  tools 与一个 file tool 改变 state。670 checkpoints 分为 retrieval、clinical reasoning、action execution、
  documentation；code grader 查询 post-execution FHIR state，hybrid grader 用 LLM 提取后与确定性
  ground truth 比较，rubric grader处理开放文本。EHR server 拥有 clinical state，tool executor 拥有
  mutation，checkpoint evaluator 拥有 evidence mapping，model narrative 不拥有 completion truth。
- **Evaluation Contract**：真实 e-consult cases 经二次去标识/扰动和 clinician validation，11 名 clinicians
  对 clarity、reasoning、completeness、safety、EHR consistency 做多轮 diff approval。模型共享最小 tool
  loop、最多 100 turns、reasoning effort high（若支持）、provider default temperature、3 trials；主要指标
  pass@1/pass@3、checkpoint success 与 reliability。公开 headline 受这 100 tasks、21 specialties、FHIR
  tool schema、model/API revision 和 2026 provider defaults 限制；不能代表临床 deployment safety。
- **Evidence / Failure Modes**：结果支持当前 Agent 的失败不是单一“医学知识不足”：reasoning 正确却
  未创建 FHIR resource 的 output gap、documentation 继承上游错误、遗漏 rubric elements 与 retrieval
  failure 必须分开。它不证明真实医院 workflow、patient interaction、multimodal data、human collaboration、
  live permissions/latency 或 adverse-event risk。LLM extraction/rubric graders仍可能受 judge bias；
  de-identification/perturbation改变 distribution；real-record origin不等于真实在线部署。
- **Engineering Trade-offs**：execution-grounded checkpoint 提高可诊断性，却引入 environment reset、
  artifact retention、grader version、PHI governance 和 partial-credit aggregation。runtime 还需要 structured
  tool errors、10k-output truncation hint、repeated-error/call/batch detection与 novelty abort；这些 safeguards
  防止 harness hang，但也可能提前终止合法恢复路径。真实生产必须额外有 authorization、human approval、
  audit 与 rollback，benchmark sandbox不能授予 autonomy。
- **Evolution / Previous Design Still Applies**：`static QA → atomic tool intent → long-horizon environment →
  post-state checkpoint cascade → deployment governance` 是 `Direct Evolution`。知识诊断、单 API regression
  与高频 unit tests 仍应保留；composite benchmark 用于集成证据，而不是替代前者。
- **ROADMAP / Adjacent Chapters / Decision**：主 owner Ch62；已读 Ch62、Ch68、Ch74、Ch77，并核对
  trajectory judge 的 narrative→action→environment→completion evidence order。现有框架已覆盖主要原则，
  但 PhysicianBench 提供“reasoning/action/documentation 四段 checkpoint 与 post-state verifier”的机制解释，
  可作为受限 clinical case refine，而非新增章节。provisional `Refine — Existing Argument`；Books Gate
  关闭期间只更新 Weekly。

### OpenSeeker-v2 — 26/30

- **Candidate / Source Family / Revision**：`OPENSEEKER-TRAJECTORY-CURATION`；W19；
  arXiv:2605.04036 v1，2026-05-05；作者 model 与 code artifact。当前只有 v1。
- **Full-read Coverage**：已读 Introduction、三项 data modifications、SFT objective、model/tool/context
  setup、baseline table、主结果、trajectory-length analysis、conclusion 与公开 artifact boundary。论文没有
  独立 limitations、ablation、seed variance 或 training-compute appendix；这些是缺失证据，不补推。
- **Original Problem / Previous Design**：CPT→SFT→RL 的多阶段 search-agent recipe 能分别扩大 domain
  exposure、模仿轨迹与优化 outcome，面对复杂搜索是合理的；但训练和 rollout 成本高，academic team 很难
  复现。普通 SFT pipeline 更便宜，却容易被 shallow、低信息 trajectory 主导。
- **Mechanism / Flow / Ownership**：数据生成先扩大 source graph，令 query 依赖更多相关 nodes；扩大 tool
  set 后生成 ReAct trajectory；再丢弃 tool-call steps 低于阈值的样本，最终仅用标准 SFT。dataset pipeline
  拥有 graph expansion、tool schema、filter 与 row lineage；model 只学习筛选后行为。step count 是 curation
  heuristic，不拥有 task difficulty 或 evidence correctness 的真值。
- **Evaluation Contract**：Qwen3-30B-A3B-Thinking-2507（30B total/3B active）、256k Context、最多
  200 tool calls，10.6k SFT rows；报告 BrowseComp、BrowseComp-ZH、HLE、xbench，与约 30B ReAct
  baselines及更大模型的公开数字比较。作者仅说明 masking Hugging Face links；baseline 训练数据、search
  backend、harness、tool/result formatting、sampling、token budget、cost/latency、trial count 与 contamination
  contract并不完整。平均 64.67 calls 只描述 retained training trajectory，不证明 difficulty 或 production
  efficiency。
- **Evidence Boundary / Trade-offs**：结果支持在这一 backbone、数据和公开 benchmark 组合下，小规模
  filtered SFT 可以达到有竞争力的 search score；不能证明 SFT 普遍替代 CPT/RL，也不能将跨报告 headline
  当作 compute-matched causal comparison。扩大 graph/tool set增加 evidence/tool diversity，也增加 generator
  hallucination、tool-distribution coupling 与 provenance burden；低-step filter去掉 trivial examples，却会
  把冗长、绕路和重复调用误当困难，减少 short-path competence并放大 cost prior。
- **Evolution / Previous Design Still Applies**：`unfiltered synthetic trajectories → structure/difficulty-aware
  curation → executable outcome filtering → SFT/RL joint curriculum` 是 `Direct Evolution`。本论文只到第二步；
  它不能越过 verifier、contamination 与 matched-compute gate。简单任务、低延迟服务或可靠短路径仍需要
  short trajectories，CPT/RL 在 domain coverage、exploration 与 outcome optimization 上继续成立。
- **ROADMAP / Adjacent Chapters / Decision**：主 owner Ch23；已读 Ch23 与 Ch72，并核对 Ch62。Ch23 已明确
  synthetic data 的 generator/judge blind spot、executable specification、row lineage 与 verifier ownership；
  OpenSeeker-v2 没有形成超出该框架的新机制，反而是“length 不等于 quality”的受限案例。provisional
  `No Change — Already Covered`；保留 Weekly，不进入 Books。

### Rethinking Reasoning-Intensive Retrieval — 27/30

- **Candidate / Source Family / Revision**：`BRIGHTPRO-EVIDENCE-PORTFOLIO-RETRIEVAL`；W19 event 以
  arXiv:2605.04018 v1（2026-05-05）归档；全文审计使用同源 ACL 2026 peer-reviewed 31-page version。
  后续正式版本用于核验机制、appendix 与限制，不另算 W19 新事件，版本化结果不得倒写成 v1 已披露事实。
- **Full-read Coverage**：已读 Related Work、expert annotation、aspect weighting/positive collection、static
  与 fixed/adaptive agentic protocols、RTriever-Synth、LoRA implementation、13 retrievers、main/qualitative
  results、limitations、metrics、reference validation、prompts、backend/tool/budget details 与 case studies。
- **Original Problem / Previous Design**：lexical/dense top-k、single-passage relevance 与 static NDCG 简单、
  易复现，适合单事实 query；但复杂问题需要互补 evidence portfolio。Agent 可以多轮弥补 retriever miss，
  同时付出更多 rounds、latency，并可能反复命中同一 aspect。
- **Mechanism / State / Flow**：BRIGHT-Pro 让领域 annotators 把 query 分解成带权 reasoning aspects，重审并
  补充每个 aspect 的 positive passages；static evaluation用带 novelty penalty 的 α-nDCG 与 weighted
  aspect recall。agentic protocol固定同一 agent/prompt/tool，只替换 retriever；每次返回 top-5、每文档截断
  2048 tokens，比较 fixed 1/2/3 rounds 与 adaptive 最多 100 rounds。RTriever-Synth 先生成 reference
  answer，再分解成 2–3 complementary aspects，并用 positive-conditioned missing-aspect negatives训练
  retriever。corpus/index 拥有 evidence state，retriever拥有 ranking policy，agent拥有 query/stop proposal，
  evaluator拥有 coverage/answer claim；任何一层都不拥有 source truth。
- **Training / Evaluation Contract**：RTriever-4B 从 Qwen3-Embedding-4B 以 LoRA r=16/alpha=32、InfoNCE
  temperature 0.02 训练；140k filtered bundles、5 epochs、bf16、DeepSpeed ZeRO-2、2×B200、effective
  batch 768、2048 truncation。static experiments 在 H200 cluster比较 BM25、general-purpose与
  reasoning retrievers；agentic sample 为 739 queries 中固定 175 条，agent backends 为 GPT-5-mini 与
  Qwen3.5-122B-A10B，tool schema/top-k/truncation/budget一致。reference/judge依赖 GPT-5 与小规模人工
  validation；不是完全 deterministic ground truth。
- **What Evidence Proves / Does Not Prove**：aspect-aware metrics 揭示 single-passage NDCG 隐藏的 coverage
  failure；static rank 与 agent utility不严格同序，BM25 可被具体 follow-up query部分补偿；好 retriever
  常减少 rounds，但 agent/retriever compatibility改变排序。它不证明 aspect taxonomy 完备、LLM judge 无偏，
  或 7 个 StackExchange domains 能代表 enterprise/private corpus。RTriever gain还混合 synthetic generator、
  LoRA recipe与base model，不能归因某一组件。
- **Trade-offs / Failure Modes**：portfolio supervision提高互补 coverage，却增加 expert annotation、aspect
  ontology、weight/judge bias与index cost。agentic loop新增 early termination、retrieval saturation、aspect
  tunnel vision与 hypothesis hopping：more queries并不自动扩张 evidence frontier。adaptive stopping降低
  平均成本，也可能 premature stop；100-round cap不是生产 SLO。
- **Evolution / Previous Design Still Applies**：`topical relevance → single-passage reasoning relevance →
  complementary evidence portfolio → retriever-in-agent-loop evaluation → joint retrieval/query/stop policy`
  是 `Direct Evolution`。lexical/static test仍适合 exact identifier、高频回归和组件隔离；portfolio/agentic
  protocol适合多方面综合，但不替代 authorization、freshness与claim verification。
- **ROADMAP / Adjacent Chapters / Decision**：主 owner Ch72；已读 Ch72、Ch73，并核对 Ch62。现有 Ch72
  已覆盖 relevance/sufficiency/faithfulness、diversity、agentic retrieval与 query/compression/stop joint policy；
  缺口是把“互补 aspect coverage”明确为 retriever objective/evaluation axis，并说明 static ranking和 workflow
  utility可能换序。provisional `Refine — Existing Argument`；Books Gate关闭，当前只记录 Weekly。

### Workspace-Bench 1.0 — 26/30

- **Candidate / Source Family / Revision**：`WORKSPACEBENCH-FILE-DEPENDENCY-EVAL`；W19；
  arXiv:2605.03596 v1，2026-05-05；官方 project、dataset、runner与judge repository。当前 repo 的 7 月
  metadata/rubric/runner修订只作为 artifact evolution，不能假定首发实验已使用。
- **Full-read Coverage**：已读 benchmark comparison、workspace/task construction、dependency annotation、
  rubric conversion、sandbox/result collection/rollback、judge/metrics、harness/model setup、difficulty/persona/
  efficiency/error analysis、five-stage framework、appendix tables/prompts与当前 reproducibility docs。
- **Original Problem / Previous Design**：single-file或预选小文件 benchmark成本低、容易隔离 parser/tool
  能力；但现实 workspace包含嵌套目录、旧版本、异构格式和隐式 lineage，final artifact看似合理也可能引用
  错版本或漏掉 supporting file。
- **Mechanism / State Ownership / Flow**：五类 persona workspace由目录结构生成、真实/合成文件填充与
  controlled noise构成；25 annotators为388 tasks指定instruction、reference output、7,399 binary rubrics与
  minimal file-dependency graph。runner从 Sandbox Pool分配task-isolated workspace，收集显式路径、统一
  copy与metadata fuzzy match所得 artifacts，再与baseline snapshot做并行 tree diff/restore。workspace
  filesystem拥有task state，dependency graph/rubric拥有evaluation specification，runner拥有reset与artifact
  capture，agent narrative只提供候选 path，不证明文件完整。
- **Evaluation Contract**：5 workspaces、20,476 files、74 types、最大20GB、平均4.7 required files/5.1
  dependency edges/19.1 rubrics；full 388 tasks与Lite 100 tasks。论文评估多 harness/model组合，并报告
  rubric pass、TCR thresholds、dependency node/edge F1、token与turns；judge读取input/output、rubric与trace，
  由trace抽取 predicted graph。当前 repo可记录container image digest与资源 profile，但这些后来增强不能
  反证首发 run已完全隔离。
- **Evidence Boundary / Threats**：研究支持“找到文件”与“理解文件关系”是不同能力，edge F1普遍低，
  hard tasks把model与harness耦合暴露出来；不证明生成workspace等价真实企业权限、协作、网络盘、mutable
  SaaS或长期用户状态。Agent-as-a-Judge可能把 narrative当evidence、rubric可能不 grounded或排斥合法替代；
  7 月 repo新增 grounded rescoring且明确只是 provisional，说明 benchmark自身也在修订。human baseline、
  provider defaults与模型版本同样限制 headline可比性。
- **Trade-offs / Failure Modes**：dependency graph提高可诊断性，却把隐式关系压成annotator-defined minimal
  graph；大 workspace逼近真实，也增加IO/cache、nondeterministic file parsing、artifact discovery与reset
  成本。fuzzy output collection提高recall却可能误收旧文件；snapshot rollback提高重复性，却需证明删除、
  permission、symlink、hidden state与外部side effects均被恢复。
- **Evolution / Previous Design Still Applies**：`provided file → small selected workspace → dependency-annotated
  sandbox → mutable workspace with post-state evidence → governed enterprise workflow` 是 `Direct Evolution`。
  单文件 tests继续做parser/tool regression；Workspace-Bench测integration，但不能替代真实 ACL、collaboration、
  retention、approval与rollback演练。论文L0–L4是作者概念框架，不是已证明的必然成熟度模型。
- **ROADMAP / Adjacent Chapters / Decision**：主 owner Ch62；已读 Ch62、Ch73、Ch77，并核对 Ch74。
  Ch62 已覆盖 trajectory evidence order 与 rubric state；长期可补的机制是将 `workspace snapshot + dependency
  graph + artifact diff + reset proof` 作为 environment-level EvalSpec，而非把 final output当唯一 subject。
  provisional `Refine — Existing Argument`；Historical Books Gate关闭期间不改 Books。

### STALE: Can LLM Agents Know When Their Memories Are No Longer Valid? — 27/30

- **Candidate / Week / Source Family**：`STALE-IMPLICIT-MEMORY-CONFLICT`；W19；
  arXiv:2605.06527 v1，2026-05-07。全文审计以当周 v1 为事件边界；没有把后续同主题 benchmark
  当成 STALE 的首发证据。
- **Direct Primary Sources / Full-read Coverage**：已读 arXiv HTML 的 metadata、Introduction、Related
  Work、implicit-conflict definitions、benchmark construction、三类 probe、model/memory-system protocol、
  main results、retrieval/attention diagnostics、CUPMem method、limitations、conclusion，以及 Appendix 的
  data generation、human validation、judge agreement、repeat-call variance、prompts 与完整 CUPMem design。
  未找到可独立核验的作者代码仓库，因此 artifact reproducibility 不补推。
- **Original Problem / Why Previous Design Was Reasonable**：raw dialogue、vector retrieval 与 summary
  memory 首先解决“历史是否还能被找到”；显式覆盖或删除也适合直接否定。但现实变化常不包含同义反转，
  新事实可能只使旧事实的适用条件失效，故 retrieval success 不等于 current-state resolution。
- **Changed Constraint / Mechanism**：STALE 把冲突分成 co-referential Type I 与跨属性传播的 Type II，
  并分别用 State Resolution、Premise Resistance、Implicit Policy Adaptation 检查模型能否识别过期状态、
  拒绝用户问题中的旧前提并把新状态用于下游行动。CUPMem 用 typed two-level schema 保存 temporal
  evidence，把 entry 标为 `ACTIVE/STALE`，在旧 default 已不安全但替代值未知时显式产生
  `UNKNOWN_CURRENT`；write path 对 direct/affected/global bounded candidates 做局部 adjudication，read
  path 再按 query intent、premise 与 action 过滤，并用 `SUPPORTED/OUTDATED/UNRESOLVED` verifier 阻止
  stale state 静默进入回答。
- **State Ownership / Control and Data Flow**：source event 拥有原始 evidence；memory store 拥有 version、
  status、provenance 与 supersession lineage；adjudicator 只提出状态迁移；retriever 只返回候选；reader/
  verifier 决定当前 query 能否消费某版本；用户或 authoritative system 仍拥有真值纠正。正确路径是
  `later evidence → bounded conflict search → temporal adjudication → status commit → status-aware retrieval →
  premise/action verification`，而不是检索到新文本后让生成模型自行猜测覆盖关系。
- **Implementation / Evaluation Contract**：benchmark 有 400 个 expert-validated scenarios、1,200 queries、
  100+ topics、最长 150K tokens。plain models 使用完整对话；memory frameworks 统一 GPT-4o-mini backbone，
  先 ingest 后冻结 memory，再独立运行三类 probe。Gemini 3.1 Flash-lite judge 与人工标签的一致率为
  95.83%，Cohen's kappa 0.9152，但 1.5% false-positive 与 7.48% false-negative 说明 judge 略保守。
  表中最佳 plain model overall 55.2；这些数字只属于该数据、prompt、model/API revision 和 judge，不是
  生产 memory accuracy。LightMem 即使较常取回 updated evidence，仍暴露 state adjudication gap。
- **What Evidence Proves / Does Not Prove**：研究证明“找到新 evidence”与“把旧 belief 判为失效并改变
  action”是不同能力；CUPMem 说明 typed status、temporal causality 和 premise verifier 是可执行 baseline。
  它不证明 schema 完备、CUPMem 是通用 open-domain memory，也不证明 attention pattern 是因果机制；
  attention analysis 仅是 diagnostic。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：保留 stale history 支持 audit/rollback，却
  增加 storage、conflict graph、adjudicator error 与 read latency；`UNKNOWN_CURRENT` 避免错误 default，也会
  降低 answerability。一次 conflict-pair、LongMemEval distractors 与生成后专家复核的数据不能覆盖重复 drift、
  coupled update、多用户 authority、并发 transaction 或真实 deletion。append-only episodic log 仍适合审计，
  simple overwrite 仍适合单 owner、显式替换且低风险的 slot；只有隐式传播和高后果行动才值得支付完整
  adjudication 成本。
- **Evolution / ROADMAP / Decision**：`retrieve history → explicit overwrite → versioned supersession →
  propagation-aware adjudication → premise/action verification` 是 `Direct Evolution`。主 owner Ch73；已读
  Ch72～74。Ch73 已有 typed transition、pending/superseded separation 与 provenance，但缺口是“retrieval
  success 不等于 current-state adjudication”以及 `UNKNOWN_CURRENT` 作为安全状态。provisional
  `Refine — Existing Argument`；Historical Books Gate 关闭期间只更新 Weekly。

### UniPrefill: Unified Sparse Prefill for Hybrid-Attention Models — 27/30

- **Candidate / Week / Source Family**：`UNIPREFILL-HYBRID-SPARSE-PREFILL`；W19；arXiv:2605.06221 v1，
  2026-05-07；作者 repository `qhfan/UniPrefill`。后续 repository state 只核验实现入口，不倒写首发结果。
- **Full-read Coverage**：已读 Abstract、Introduction、Related Work、hybrid block abstraction、importance
  estimation、top-p guarantee、block-wise mask propagation、四个 fused Triton kernels、tensor-parallel 与
  continuous-batching integration、全部 experiment/ablation/sensitivity、limitations、conclusion 与 appendices，
  并核对 vLLM integration 的 metadata/KV-slot bookkeeping 说明。
- **Original Problem / Previous Design**：dense Prefill 与 per-layer sparse attention 实现简单、语义清晰，
  在短 context、exactness 或不稳定 pattern 下仍合理。已有 sparse Prefill 多只缩减 full-attention layer，
  对 linear/full 或 sliding-window/full hybrid block 的后续 attention/FFN/GEMM 不能回收同一批 token work，
  且 batch-1 prototype 难以接入 continuous batching。
- **Mechanism**：每个 hybrid block 从 full-attention layer 的最后 `n` 个 queries 估计 block importance，
  先在完整 key dimension 上做 online softmax，再选取累计质量达到 `p` 的最小 block set；始终保留前 128
  attention sinks 与 query window。被丢弃 positions 在后续 attention/linear/sliding/FFN sublayers 中不再计算，
  但其旧 hidden state 原样携带，到下一个 full-attention block 重新拼回并计算。它与 SnapKV 不同：后者先
  完成 Prefill 再压缩 Decode KV；UniPrefill 直接减少 Prefill 后续层的 FLOPs。
- **State Ownership / Control and Data Flow**：full-attention score path 产生 per-request block mask；TP ranks
  先 all-reduce partial scores，随后必须使用一致 mask。runtime 拥有 packed `cu_seqlens`、active-token map、
  per-layer query starts、sequence lengths 与 physical KV slot map；每个 request 还要保存 layer-aware drop
  history，使 Decode 使用正确的 effective KV length。model layer 只消费已提交的 typed metadata；若 mask、
  sequence progress 与 slot identity 不一致，错误可能表现为静默语义偏差而不是显式 OOM。
- **Implementation Details**：四个 fused Triton kernels 在 packed representation 上完成 importance、top-p、
  select/drop/reconstruct，避免 per-request padding/materialization。接入 vLLM v0.16.0 时需要逐层 patch
  attention metadata、`query_start_loc`、`seq_lens`、`num_actual_tokens`，并因 global/sliding layers 物理布局
  不同重新计算 slot mapping；不改 PagedAttention allocator 或 weights 不等于 state contract 没有变化。
- **Evaluation Contract**：作者使用 Llama 3.1 8B full attention、Qwen3-Next 80B-A3B linear/full 3:1、
  Gemma 3 12B sliding/full 5:1；`p` 分别 0.99/0.99/0.98，block 64、recent query 128、sink 128。
  accuracy 在 RULER 4K～128K；TTFT 表是 Hugging Face Transformers batch 1；serving 使用 vLLM v0.16.0、
  TP=8、CUDA 12.8，context 4K～128K、batch 1/4/16/64。论文报告的最大 TTFT 与 throughput gain 只能绑定
  这些模型、长度、实现和阈值；未披露完整 GPU 型号、arrival process、tail TTFT/TPOT 或 production SLO，
  不外推为通用倍率。block-size 与 recent-query ablation 支持 64/128 是本实验折中，不是默认配置。
- **Evidence Boundary / Critical Finding**：结果支持同一 full-attention selection mask 可以在这些 hybrid
  architectures 的后续 sublayers 复用，并可在特定 vLLM packed batch 中保持 bookkeeping；不证明跨任务
  exactness、Decode 加速、训练收益或异构硬件可迁移。论文理论段给出的渐近 FLOPs ratio 按其展示公式
  `(L-l)Nd^2/(N^2 d_k)` 在固定 `d` 时应随 `N` 减小，而正文却称 `N→∞` 时趋于无穷；这是内部代数不一致，
  本审计不采用该渐近结论，只保留可核验的机制和实测边界。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：sparsification 获得后续 layer/GEMM work
  reduction，却新增 importance selection、top-p、collective、mask propagation、reconstruction、per-layer KV
  history 与 fallback。错误 mask 会丢失 evidence；coarse block 减少 selection overhead 却保留更多 token；
  更长 probe window 提高代表性却增加开销。短输入、strict exactness、unsupported hybrid order、pattern drift
  或 metadata path 不完整时，dense/FlashAttention 仍是正确 baseline；fixed top-k 在硬 compute envelope 下
  也可比 top-p 更可控。
- **Evolution / ROADMAP / Decision**：`dense full Prefill → per-layer sparse attention → full-block selection +
  downstream token propagation → continuous-batching typed metadata` 是 `Direct Evolution`，不是对 dense
  或 Chunked Prefill 的替代。主 owner Ch39；已读 Ch38～40，并核对 Ch42/46 的 scheduling 与 KV state
  contract。Ch39 已覆盖 FlashPrefill 的 selection overhead、ephemeral indices、shape/fallback；UniPrefill
  新增的长期缺口是 hybrid block 的跨层 token-state propagation 与 per-layer runtime identity。provisional
  `Refine — Existing Argument`；Books Gate 关闭期间不改正文。

### LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling — 26/30

- **Candidate / Week / Source Family**：`AUTOTTS-CONTROLLER-DISCOVERY`；W19；arXiv:2605.08083 v1，
  2026-05-08；全文核验使用 v2（2026-05-12）修复后的 25-page PDF 与官方 `zhengkid/AutoTTS` repository。
  v2 用于补足结果/appendix，不作为 W20 新事件，也不把后加事实倒写成 v1 明示内容。
- **Full-read Coverage**：已读 width-depth formalization、state/action/cost objective、offline replay、
  agent-driven discovery、history/trace design、beta parameterization、实验设置、全部 main/generalization/
  ablation/efficiency/evolution analyses、related work、limitations、完整 discovery prompt 与 Appendix D 的
  discovered Confidence Momentum Controller code；HTML 转换缺失结果表，故回读 PDF。
- **Original Problem / Why Previous Design Was Reasonable**：Self-Consistency、adaptive consistency、
  early stopping、branch/prune/probe 等 handcrafted TTS policy 容易解释并直接实现，在稳定 workload 与小
  policy space 中仍合理；但它们只覆盖 structured allocation space 的少量手工轨迹，threshold tuning 容易
  依赖直觉和 search benchmark。
- **Changed Constraint / Mechanism**：AutoTTS 把 width/depth allocation 表达为 controller synthesis：state
  包含 active branches、depth、prefixes、已揭示 probe 与剩余 budget，action 为 branch/continue/probe/prune/
  answer。先为每题预采样 trajectories 与 probe signals，候选 controller 在 deterministic replay 中便宜运行；
  explorer coding agent 读取所有历史实现、accuracy-cost curve 和 decision traces 后改写 controller。单一
  monotone `beta` 映射所有内部 hyperparameters，压缩搜索空间并生成可扫描的 budget family。
- **State Ownership / Control and Data Flow**：replay dataset 拥有固定 trajectory/probe evidence；controller
  拥有本次 branch/depth/probe state；discovery workflow 拥有 round、history、code lineage 与 selection；
  evaluator 拥有 accuracy/token measurement；explorer 只提出代码，不拥有 objective、ground truth 或部署
  authority。`precollect → replay candidate → emit curve + traces → propose patch → select on search set → freeze →
  held-out evaluation` 把 generation cost 从每次搜索移到前置数据采集，但不消除数据生成成本。
- **Implementation Details**：五轮中每次只编辑 `OptimalController`，共享 64-branch ceiling、seed methods、
  evaluator 与 trace interface。最终 CMC 用 EMA confidence level + trend 控制 stopping，置信度增长时抑制
  widening、停滞/回落时扩宽；对与 pool winner 对齐的 branches 分配更多 depth，只有持续偏离才 abandon，
  且至少保留两条 active branches。所有 critical knobs 是 `beta` 的确定函数，trace 记录 init/forward/
  update/terminate/finish，体现“行为证据优于单一 scalar”。
- **Evaluation Contract**：四个 Qwen3 sizes（0.6B/1.7B/4B/8B），每个 model-problem 预采样 128 条
  trajectories，temperature 0.7、500-token probe interval；每个 controller 从 pool 随机抽样并独立评估 64 次。
  AIME24 作为 search set，五轮 Claude Code discovery；AIME25/HMMT25 held out，并另测
  DeepSeek-R1-Distill-Llama-8B/HMMT25 与 Qwen3-1.7B/GPQA-Diamond。主要 metrics 只有 accuracy 与总 tokens；
  未给在线 GPU hardware、batch/concurrency、wall-clock inference、TTFT/TPOT/tail SLO。39.9 美元与 160 分钟
  是一次 replay discovery cost，不包含完整 trajectory 预采样，也不是 deployed inference cost。
- **What Evidence Proves / Does Not Prove**：matched replay 中的主表、held-out transfer 与 ablation 支持
  beta search-space constraint 和 execution traces 对本次发现过程有用；不带 beta 的 controller 在 held-out
  accuracy 下降，去除 traces 则使用更多 tokens 且效果更弱。它不证明 AutoTTS 超过所有 online/adaptive
  TTS、controller 对开放任务稳定，或 frontier coding agent 是必要条件；offline replay 不能表示策略改变后
  会产生的新 trajectory，也无法测线上 queue、KV、parallelism 和 hardware cost。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：replay 使 evaluation 便宜、确定且可复查，
  代价是 support-set lock-in、counterfactual blindness 与 precollection/storage 成本；单 beta 降低 overfitting，
  也压缩可表达 policy family。execution trace 提高诊断性，却增加日志、隐私和 history selection 成本。
  简单、高风险或不可自动评分的问题仍应使用人工 policy + formal review；handcrafted strategies 也是稳定
  regression baseline，而不是应被“agent-discovered”方案覆盖。
- **Evolution / ROADMAP / Decision**：`fixed-width sampling → handcrafted adaptive stop/prune → structured
  controller state/action space → offline replay program search → held-out/online governance` 是 `Direct
  Evolution`。主 owner Ch77，Ch75/38/52 作短 handoff；已读 Ch75～77，并核对 Ch38/52。Ch77 已覆盖
  problem compilation、evaluator-driven search、lineage 与 held-out verification；AutoTTS 补足“replay
  environment 将 expensive action 与 controller search 解耦、trace 暴露 allocation failure、single-knob
  regularization”的受限机制。provisional `Refine — Existing Argument`；Historical Books Gate 关闭期间不改 Books。

### HyperEyes: Dual-Grained Efficiency-Aware Reinforcement Learning for Parallel Multimodal Search Agents — 26/30

- **Candidate / Week / Source Family**：`HYPEREYES-PARALLEL-TOOL-EFFICIENCY-RL`；W19；
  arXiv:2605.07177 v1，2026-05-08。全文核验使用 v2（2026-05-11）及官方
  `DeepExperience/HyperEyes` repository；v2 用于核对 appendices 与 revision，不另算 W20 事件。
- **Full-read Coverage**：已读 formulation、Unified Grounded Search、两类 synthetic data、Progressive
  Rejection Sampling、SFT/RL data selection、TRACE reward、failed-rollout OPD、IMEB/CAS、六个 benchmark
  的 setup/results/ablations、limitations、全部 data/evaluation/training appendices、三次 RL seed、noise stress
  test、controlled grounding-paradigm comparison 与 case study。
- **Original Problem / Previous Design**：serial crop-then-search 的 ownership清楚，适合依赖链、动态观察与
  每步需要前一步证据的任务；但多实体可独立检索时，它把可并行 work 变成长 interaction chain，且 early
  crop error 会传播。只优化 final accuracy 又可能让并行 tool call 退化成一轮内的 brute-force spam。
- **Mechanism / Credit Assignment**：UGS 把多个 bounding boxes 与 text/image retrieval 合并为同一 atomic
  action，使一轮可发出并行 grounded queries。PRS 在逐步放宽 turn budget 时保留最短成功 trajectory；TRACE
  同时记录 tool-call rounds `t_c` 与总 invocations `t_s`，每 epoch 只用当前成功 rollout 收紧 reference，只有
  accuracy正确且两项都不超 reference 才获得正效率 reward，避免用单轮海量调用投机。trajectory reward 对
  failed rollout 的所有 tokens 过粗，故 OPD 只在失败轨迹上用冻结、同 family 且已 efficiency-aligned 的 235B
  teacher 做 reverse-KL token correction；成功轨迹保持由 TRACE 探索。
- **State Ownership / Flow**：tool environment 拥有 search observation；policy 拥有 query decomposition 与
  action proposal；runtime 拥有 parallel dispatch、round/total-call accounting、timeouts 与 result collection；
  per-sample reference ledger 拥有当前可达 efficiency boundary；judge 拥有 task correctness；teacher只提供
  token distribution，不拥有 ground truth。`task → parallel action → observations → answer/judge → update
  success-conditioned cost reference → group advantage + failed-only distillation` 中，round latency 与 call volume
  必须分开，不能只优化其中一个。
- **Evaluation Contract**：30B/235B backbones 为 Qwen3-VL MoE；30K LoRA SFT，RL data 6,056/9,337，
  每 prompt 8 rollouts。SFT 与 RL 均使用 8 nodes × 8 NVIDIA H20 141GB；RL rollout 是 SGLang，30B/235B
  分别约 48/72h，OPD teacher在独立 inference cluster。evaluation 限 19 turns/18 tool calls、38K sequence、
  每图 1,200 visual tokens，SerpAPI text/reverse-image search。作者主表的 9.9-point 与 5.3x headline受不同
  baseline prompts、tools、checkpoint availability 与 search pipelines 限制；论文自己明确这些比较并非
  fully matched。CAS 以经验权重把 token 与 tool round 都近似成一秒，不能视为真实 latency/cost model。
- **Evidence / Ablation Boundary**：SFT→TRACE→aligned-teacher OPD 的 ablations 支持当前 data/model设置下，
  dynamic reference减少冗余，failed-only dense correction可再提高 accuracy；vanilla teacher反而明显退化，
  证明 teacher alignment是机制条件。三次 RL seeds只说明同一 SFT checkpoint上的训练稳定性。controlled
  UGS/crop comparison与48样本 distractor test提供方向证据，但不覆盖 live web drift、tool failures、P95/P99
  latency、API cost、rate limits或真实并发。
- **Trade-offs / Previous Design Still Applies**：parallel dispatch缩短critical path，却增加burst concurrency、
  quota、result ordering、duplicate query与partial-failure语义；monotone-best reference可能被偶然短轨迹锁得过紧，
  teacher带来额外训练服务与同源错误。静态image/text、same-family teacher与synthetic mosaic限制外推到video/
  audio和frontier scale。依赖性强、high-side-effect或每步需验证的任务仍应串行；并行适合独立、只读、可合并的
  retrieval，不是“越宽越好”。
- **Evolution / ROADMAP / Decision**：`serial tool loop → parallel-capable action schema → outcome-only RL →
  round+invocation cost reward → failed-only token correction → runtime SLO governance` 是 `Direct Evolution`。
  主 owner Ch29，Ch75/77/78 作 handoff；已读 Ch29、Ch75、Ch77、Ch78。Ch29 已覆盖 sequence reward 的
  token-credit边界与 measurement-as-reward；HyperEyes补足 dual-grained cost、success-conditioned moving
  reference和teacher-alignment条件。provisional `Refine — Existing Argument`；Historical Books Gate关闭，
  不修改正文。

### Soohak: A Mathematician-Curated Benchmark for Research-Level Mathematics — 24/30

- **Candidate / Week / Source Family**：`SOOHAK-GOVERNED-MATH-BENCHMARK`；W19；arXiv:2605.09063 v1，
  2026-05-09；v2/v3 分别为 2026-05-17/19。W19 事件按 v1 归档，全文使用当前 v3 核验补充细节，
  不把后续模型结果倒写成 v1 已披露事实。
- **Direct Sources / Full-read Coverage**：已读 arXiv metadata 与 revision history、Introduction、Related Work、
  contributor terms、五阶段 collection pipeline、三层 model-gated routing、双人 manual review、translation、
  refusal subset、evaluation/judge protocol、结果与 compute scaling、human baseline，以及 Appendix B/D/E/F 的
  compensation、leakage control、quality control、generation configuration、human protocol 与完整 retrospective。
  数据集截至论文当前版本仍在 embargo，故不能独立重放 item-level evaluation。
- **Original Problem / Previous Design**：从公开竞赛、教材和论文抽取题目便宜、可复用、容易获得自动评分，
  因而适合建立早期 benchmark；但随着训练语料覆盖和能力饱和，公开来源增加 contamination 与重复优化风险。
  完全保密能延长寿命，却牺牲透明度、独立复现和错误发现。
- **Changed Constraint / Mechanism**：Soohak 把 benchmark authoring 变成受治理的供应链：原创/no-AI/IP/NDA
  agreement → automated screening 与 similarity checks → 三层 model-failure gates → 两位人工 reviewer → contributor
  opt-in → inclusion。撤回/拒绝条目即时删除并限制 pre-opt-in access；Challenge 聚焦 340 个 graduate/research-
  adjacent items，另用 99 个 ill-posed items 检查模型能否拒答而非强行给数值答案；702-item Mini 提供较低难度层。
- **State Ownership / Data Flow**：contributor 拥有原始题目与 reference solution；collection service 持有 submission、
  agreement 与 gate state；model panel 只提供 difficulty routing signal；两位 reviewer 拥有 correction/acceptance evidence；
  contributor 再决定 opt-in；evaluation runner 拥有 model revision、sampling 与 parsed answer；GPT-5-Mini judge 只比较
  parsed answer 和 gold answer，不读取题目或推理。LLM subject labels 只是 coverage annotation，不能成为 ground truth。
- **Implementation / Governance Details**：全体 accepted pool 为 105 位贡献者，primary system 86 位来自 31 个组织，
  另有 19 位 ScienceBench contributors；总 compensation pool 26 万美元，单题 36～3,623 美元、单人上限 2 万美元。
  论文报告 87 个 items 经 reviewer correction，并剔除 AI-generated submissions。双语流程用 LaTeX placeholders、
  professional post-edit 与 independent QA；这些控制提高 provenance，却不能证明每题无误或无泄漏。
- **Evaluation Contract**：每个 model-question pair 独立采样三次，报告 avg@3/pass@3；human baseline 只覆盖 79 题、
  五组 25 人、4.5 小时，允许非 AI 工具，但 session/proctoring 未完全标准化。论文当前版本的 439 题、模型名单、
  token/reasoning settings 和分数是版本化结果；human wall-clock 与 model token budget 不可直接比较。作者也明确指出
  contest-trained undergraduates 优于 research team 主要反映 task format，而不是研究能力排序。
- **Evidence Boundary**：论文证明可以通过付费 expert authoring、access control、model gates 与人工复核生产一个
  较大、暂未公开的数学评测资产，并把 invalid-problem refusal 独立切片；不证明 embargo 排除所有 contamination、
  integer-answer task 等同真实 mathematical research、model judge 无误，或排行榜差异可泛化到其他学科。约 55 万美元
  总成本、四个月 schedule、review capacity、difficulty incentive 与 field coverage 均是作者 retrospective 中的限制。
- **Trade-offs / Evolution / Previous Design Still Applies**：`public scraped set → freshly authored set →
  access-controlled expert pipeline → refusal/invalid-input slice → later public release and refresh` 是 `Direct Evolution`。
  它获得 freshness、difficulty headroom 与 provenance，代价是高成本、访问不对称、复现延迟、review bottleneck 与
  incentive distortion。公开 frozen benchmark 仍适合可重复 regression；private set 适合短期 capability audit；二者需
  recent production/risk slices 补足，而不是互相覆盖。
- **ROADMAP / Existing Coverage / Decision**：主 owner Ch62；已读 Ch61～63，并核对 Ch23 的 data provenance。
  Ch62 已明确 dataset identity/digest、source/license/consent、sampling/slice、rubric、contamination、refresh、access/
  retention，以及 frozen/golden/adversarial/recent-production 分层；也已经要求 human/model judge 校准和环境身份。
  Soohak 为这套原则提供完整案例，但未暴露新的跨章机制。最终 `No Change — Already Covered`；只留 Weekly 作为
  版本化 evidence，不修改 Books。

### MCP-Cosmos: World Model-Augmented Agents for MCP Task Execution — 24/30

- **Candidate / Week / Source Family**：`MCP-COSMOS-SIMULATED-TOOL-PLANNING`；W19；arXiv:2605.09131 v1，
  2026-05-09，当前只有 v1。
- **Direct Sources / Full-read Coverage**：已读 arXiv metadata、Introduction、BYOWM interface、world-model simulation、
  proactive planning、real execution、MCP-Bench subset、三种 agent architectures、三类 world models、全部 metrics/
  results/gap analysis/ablation/limitations/conclusion，以及 token/latency appendix、完整算法与 24 项 task list。
  arXiv 未提供可核验的作者 code/artifact link，因此实现结论只限论文披露。
- **Original Problem / Previous Design**：ReAct 逐步调用真实工具，observation 与 authoritative environment 同步，
  适合 dynamic schema、可恢复 trial-and-error 和低 simulation fidelity 场景；但 exploration 本身会消耗 API quota、
  latency、token 和副作用预算。预先生成固定 plan 可减少 live calls，却容易在现实 observation 偏离时失效。
- **Changed Constraint / Mechanism**：MCP-Cosmos 把 planning 与 execution 分为两条 trajectory。planner 针对候选
  tool calls 请求 world model 生成 pseudo-observations，积累 `tau_wm` 后由 LLM policy 或 MCTS 选择计划；executor
  再在真实 MCP servers 上执行并记录 `tau`。论文算法允许 real action failure 后调整余下计划，但因成本将该机制
  排除在 benchmark 外，因此实验验证的是 open-loop plan-then-execute，不是完整 closed-loop recovery。
- **State Ownership / Control and Data Flow**：world model 只拥有 predictive/simulated state；planner 拥有候选计划
  与 search budget；MCP server/environment 拥有 authoritative tool state；executor 拥有真实 call、observation、
  error 与 side-effect evidence；final synthesizer 只能从 actual trajectory 形成答案。pseudo-observation 可只是摘要、
  示例或形似真实输出的数据，不能写回真实 state，也不能代替 schema/version/authorization probe。
- **Implementation / Evaluation Contract**：从 MCP-Bench 的 28 live servers/257 tools 中因调用成本筛选 24 个
  2～3-server tasks、12 类任务、300+ trajectories；比较 ReAct、ReAct-Plan-Exec、SPIRAL-Exec，planner/world model
  使用 gpt-oss-120b、Claude Sonnet 4.6 与 Arctic-AWM-4B，o4-mini 作为 judge。实验环境披露 M1 Max 32GB 与 cloud
  model calls，但没有 production concurrency、tail latency、write-side-effect 或 evolving-schema contract。
- **What Evidence Proves / Does Not Prove**：在该小型 subset 中，world-model variants 改善部分 tool selection、
  parameter accuracy 和 parallel efficiency，却没有超过 ReAct 的 task fulfillment、dependency awareness 与总体
  completion。它们减少真实 tool calls，但 token/latency 可能更高；例如部分配置平均 token 是 baseline 的数倍，
  local 4B model 也可能因部署路径更慢。结果不证明 world model 普遍降低总成本、MCP servers 足够稳定，或 simulation
  fidelity 能覆盖 write/destructive actions。
- **Metric Boundary / Trade-offs**：Execution Quality 将 tool-call success 与 cohort 内 min-max 反向归一化的平均
  calls 等权组合；论文自己限定它只适合同一 planner baseline 的 cohort comparison，不能跨实验比较。simulation
  降低 live probing，却新增 prompt/context、model inference、stale-schema、hallucinated observation、plan commitment
  与 reconciliation 成本。强 planner 可能探索更宽；world model 能约束 live calls，但不等于缩短 wall time。
- **Evolution / Previous Design Still Applies**：`reactive live probing → upfront plan → simulated lookahead → real
  execution → observation-triggered replan` 是 `Layering / Dependency`。dynamic/low-risk/read-only 工具仍可用 ReAct；
  稳定、昂贵或有副作用的环境可先 simulation，但执行前必须重新验证 precondition，执行后以真实 observation 更新
  belief。只有把 excluded revision path 纳入 evaluation，才能判断闭环 recovery 是否成立。
- **ROADMAP / Existing Coverage / Decision**：主 owner Ch75，Ch74/76/79 作邻接；已读 Ch74～76 与 Ch79。
  Ch75 已把 plan 定义为部分可观测环境中的可验证状态转移假设，并要求 observation-triggered replanning；Ch74 已规定
  server-side validation、real principal、side-effect/retry 与不可信 observation；Ch79 已明确 MCP 不拥有 planning、
  durable state、retry 或 task success。MCP-Cosmos 强化既有边界，但没有形成新的长期缺口。最终 `No Change —
  Already Covered`；保留为 Weekly case，不修改 Books。

### MemPrivacy: Privacy-Preserving Personalized Memory Management for Edge-Cloud Agents — 27/30

- **Candidate / Week / Source Family**：`MEMPRIVACY-EDGE-CLOUD-PSEUDONYMIZATION`；W19；
  arXiv:2605.09530 v1，2026-05-10；v2/v3 分别为 2026-05-12/14。W19 事件按 v1 归档，全文、代码与
  model collection 按当前 v3/repository 核验；后续版本不另算事件。
- **Direct Sources / Full-read Coverage**：已读 arXiv metadata/revision、Introduction、Related Work、problem
  definition、三阶段 architecture、PL1～PL4 taxonomy、MemPrivacy-Bench construction/annotation、SFT+GRPO、
  全部 extraction/utility experiments、Conclusion，以及 Appendix A～D 的 dataset、human protocol、model variants、
  prompts、memory testbeds 与完整 training recipe；并核对官方 GitHub `src/privacy_masking.py`、README、evaluation
  entry 和 Hugging Face model collection。
- **Original Problem / Why Previous Design Was Reasonable**：cloud 直接处理原文最能保留 personalization semantics，
  也最容易接入已有 memory systems；irreversible redaction 则把原始值留在 edge，但会同时抹掉 email、health、
  relationship 等 semantic role，降低写入、检索与回答质量。DP、cryptography 与 unlearning 保护的对象和生命周期
  不同，不能直接替代 inference-time raw-span minimization。
- **Changed Constraint / Mechanism**：系统在 edge 用 detector 输出 span、privacy level 与 type，按 user policy 选择
  PL threshold，将原值替换为稳定 typed placeholder（如 `<EMAIL_1>`），只让 placeholderized prompt/memory 进入
  cloud；响应返回后 edge 依据本地 mapping 还原。类型保留让 cloud 继续推理“这是邮箱/健康信息”，但不获得原值；
  稳定 index 允许跨 session 指向同一实体。PL1 是默认不提取的低敏 preference，PL2～PL4 逐步提高 identifiability、
  harm 与 exploitability；threshold 是 policy，不是 detector 自行决定。
- **State Ownership / Data Flow**：edge detector 只拥有 candidate sensitive spans；local policy 拥有保护级别；local
  mapping store 是唯一可逆 source of truth；cloud memory 只拥有 typed aliases 与非敏感 context；restorer 只能在
  authorized response boundary 解引用。mapping lifecycle 必须绑定 user/tenant namespace、encryption、device backup、
  rotation、deletion、concurrency 与 audit；placeholder 本身仍泄露 type、equality、frequency 和 relation structure。
- **Artifact Boundary / Critical Finding**：论文称 mapping “securely stored”，但当前公开代码使用单个 SQLite 表保存
  plaintext `original_text/type/level/mask`，以 `original_text` 全局唯一去重并按 type count 生成序号；没有公开的
  encryption、tenant/user scope、authorization、integrity tag、atomic sequence allocation、key rotation 或 deletion
  propagation。`unmask_dialogue` 会对任意匹配本地 regex 且能查到的 placeholder 直接还原，所以 untrusted cloud
  output 注入 alias、跨用户 DB 误配与 local-store compromise 都属于未解决风险。代码证明 reference mechanism，
  不证明 production security contract。
- **Training / Evaluation Contract**：benchmark 为 200 个 synthetic users、155K+ privacy instances，中英各半；
  evaluation splits 经 Gemini-3.1-Pro/GPT-5.2 初标与六位人工逐 item 核验。模型为 Qwen3 0.6B/1.7B/4B，26K SFT +
  1K GRPO；SFT bf16、max length 4096、ZeRO-3，RL max input/completion 4096/1536、8 generations、ZeRO-2、vLLM
  rollout。hardware 型号、edge device class、energy、P95/P99、concurrency 与 production SLO 未披露。
- **What Evidence Proves / Does Not Prove**：作者在 MemPrivacy-Bench 与 20-user PersonaMem-v2 subset 上对
  LangMem/Mem0/Memobase、统一 GPT-4.1 memory/QA path 的结果支持 typed placeholders 比 complete/untyped masking
  更保留本实验 utility，specialized detector 在作者 metric/judges 下优于 prompt-only general models。它不证明
  attack-defined privacy leakage risk 公式真的被测量：实验主要测 extraction F1 与 task utility，没有执行
  re-identification、linkage、placeholder injection、mapping-store compromise、deletion/backup 或 adaptive attacks。
  “utility loss within 1.6%”只适用于特定系统、mask levels、judge 与 synthetic/test subset。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：typed pseudonymization 获得可逆性与 semantic
  utility，却把风险集中到 edge detector 和 mapping store，并保留 structural leakage；漏检直接上传原文，过检损害
  task，错 type 会污染 retrieval，alias collision/renumbering 会破坏 identity，cloud 生成不存在或恶意 alias 会造成
  restoration ambiguity。PL4 credentials 更适合 block/zero-retention 而非可逆长期 alias；需要强 anonymity、不可链接
  发布或 aggregate statistics 时仍应使用删除、generic masking、cryptography/DP 等其他机制。
- **Evolution / ROADMAP / Decision**：`plaintext cloud memory → irreversible masking → untyped alias → typed reversible
  pseudonymization at edge → scoped encrypted mapping + output-authenticated restoration` 是 `Direct Evolution`。
  主 owner Ch68，Ch73/62 作 handoff；已读 Ch67～69、Ch72～74。Ch68 已覆盖 policy-bound detector、mask/remove/
  pseudonymize 与“本地运行不等于匿名”，但尚未展开 reversible alias 的 state ownership 与 output-side restoration
  attack surface；Ch73 已覆盖 memory provenance、authorization、deletion 和 privacy cost。provisional
  `Refine — Existing Argument` / Ch68，`Status: Experimental`；Historical Books Gate 关闭期间不改 Books。

### Geometry Conflict: A Geometric Perspective on Catastrophic Forgetting — 26/30

- **Candidate / Week / Source Family**：`GEOMETRY-CONFLICT-CONTINUAL-UPDATE-MERGING`；W19；
  arXiv:2605.09608 v1，2026-05-10。当前只有 v1；作者 repository 按访问日核对，不把后续代码状态
  倒写成首发 artifact contract。
- **Direct Sources / Full-read Coverage**：已读 arXiv metadata、Abstract、Introduction、Related Work、
  problem formulation、covariance geometry、Bures-Wasserstein conflict、barycenter、whiten-merge-recolor、
  incremental update、全部 domain/capability experiments、correlation、ablation、sensitivity、runtime、
  theorem、limitations、Conclusion 与相关 Appendices；并核对作者 `GCWM` repository 的 merge/config/
  memory policy surface。公开仓库是整理后的 GCWM-only package，不能证明首发时所有 baseline 路径均可复现。
- **Original Problem / Why Previous Design Was Reasonable**：顺序 SFT 在每一步只优化当前任务，部署和
  optimizer 语义直接；EWC 约束重要参数、replay 保留旧数据、参数平均/Task Arithmetic 在无法访问旧数据时
  合并 task updates，这些方案分别在数据可留存、任务较少或 update directions 相容时合理。但 model scale、
  capability mix 和 privacy/storage constraint 变化后，单看 update norm 或逐参数平均无法表达多个 task updates
  在 representation subspace 上如何重排能量，也无法区分“当前两任务冲突”与“累计状态已经偏离历史几何”。
- **Changed Constraint / Mechanism**：对每层 task update `Delta_i` 构造正则化 covariance
  `C_i = Delta_i^T Delta_i + lambda I`；以截断 right-SVD union basis 把活跃 updates 投到共享子空间，
  用 normalized Bures-Wasserstein discrepancy 计算 conflict。系统聚合 pairwise conflict 经 sigmoid 形成
  layer gate，以 Gaussian Wasserstein barycenter 定义共享 metric；再对各 update whiten、用加权 WUDI 合并、
  recolor，并与 plain parameter merge 分支混合。incremental execution 只应用“当前 merged state 与上一步
  merged state 的差”，避免重复叠加完整历史 update。
- **State Ownership / Control and Data Flow**：common pretrained checkpoint 定义 task-vector origin；每个 task
  checkpoint 拥有相对 base 的 update；memory policy 决定 active set（全历史、最近 N 个，或 previous merged
  anchor + current）；per-layer geometry builder 拥有 union basis、covariances、conflict 与 barycenter；merge
  controller 拥有 gate、inner weights 和 outer step size `eta_t`；continual state 只接收 incremental delta。
  任务数据在 merge-time 可缺席，但 checkpoint identity、base compatibility、task order、active-set policy 与
  prior merged state 成为新的 lineage contract。
- **Implementation / Evaluation Contract**：使用 Qwen3 0.6B/1.7B/4B/8B/14B。domain sequence 为
  MMLU-Pro 14 个 subdomains、每域 1k training samples；capability sequence 使用 30k math Nemotron 与
  30k CodeFeedback experts，并在 GPQA-D、GSM8K、MATH-500、HumanEval、MBPP、MMLU-Pro 上评估。
  比较 Seq SFT、EWC、FOREVER replay、AIMMerging 与多个 data-free merging baselines；主 evaluation 采用
  5 个独立 runs/decoding seeds（适用时）。task experts 最多使用 64 张 NVIDIA H800；核心 geometry/merge
  分析在 dual-socket Intel Xeon Platinum 8480CL CPU 上运行。runtime profiling 只覆盖少量 8B/14B steps，
  不构成 production throughput、并发、tail-latency 或 SLO contract。
- **Correlation / Ablation / Sensitivity**：250 个 step observations 的 run-cluster bootstrap 为 2,000 次、
  permutation 为 3,000 次。global aggregation 中 update norm、active conflict、state-relative gap、global gap
  与 forgetting 的相关性分别约为 -0.48、+0.30、-0.45、-0.59，但方法内高度异质：Seq SFT 的 state/global
  gap 约 -0.68/-0.70，FOREVER 仅约 -0.06/-0.10，AIMMerging 甚至约 +0.10/+0.01；孤立 pairwise GC
  与 immediate drop/forgetting 接近零或很弱。domain 0.6B ablation 的 full 27.1 对 26.7/26.8，差异小；
  capability 1.7B/8B 上去 gate 或去 whitening-barycenter 会下降，但 task-wise 结果不一致。`tau/r/kappa`
  在测试范围内较稳，outer `eta_t` 却主导结果：0.1、0.3、1.0 的平均结果约 67.3、70.8、34.3，说明它是
  必须显式治理的 stability knob，而非可自动忽略的实现参数。
- **What Evidence Proves**：在作者任务顺序、checkpoint family 与 merge contract 下，state-relative/global
  covariance geometry 比 isolated pairwise conflict 更能描述某些方法的 forgetting trajectory；whiten→merge
  →recolor 和 conflict gate 能形成可执行的 data-free merge 分支，并在部分 scale/task 上改善 retention。
  证据同时说明 continual learning 的冲突不能压缩成单个 pairwise scalar，update magnitude 与 accumulated
  state displacement 需要联合观测。
- **What It Does Not Prove / Evidence Conflict**：论文不证明 geometry conflict 是跨方法的统一因果解释，
  也不证明 data-free merging 普遍优于 replay、regularization 或再训练。局部 theorem 只在假设与未知非负常数
  下界定 GCWM 相对 plain merge 的 loss difference，不保证绝对改善或更少 forgetting。正文/Appendix 对
  1.7B 的 `+5.78` 描述与表中 58.26 对 strongest data-free baseline 56.82（即 `+1.44`）不一致；该数字
  标记为作者内部冲突，未经澄清不得引用。GCWM 在 0.6B 与 4B 也并非最佳，FOREVER 使用 replay data，
  resource/data budget 又未对齐，不能作简单排名。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：data-free merge 避免保存旧样本，却需要保留
  compatible task checkpoints、共同 base、active history 与昂贵的 SVD/metric state；active set 增长会增加
  CPU time/memory，truncation 可能丢失低能量但关键方向。错误 base、task order、outer step、rank 或 memory
  eviction 会导致不可解释 drift；geometry signal 还可能只是 optimizer/data order 的伴随量。允许保存代表性
  数据且需最强 retention 时，replay 仍可能更好；任务少且方向相容时，plain merge 更简单；在线单任务适配仍可
  用低 learning rate、regularization 或 adapter isolation。
- **Evolution / ROADMAP / Decision**：`顺序更新 → magnitude/importance regularization → replay → task-vector
  merge → state-relative update geometry → gated barycentric merge` 是 `Direct Evolution`，不是后者替代前者。
  主 owner Ch25，Ch26/31 作 handoff；已读 Ch24～26 与 Ch31。Ch25 已覆盖 catastrophic forgetting 的现象与
  replay/lower update/adapters/early-stop 分支，但缺少“task update integration 是独立 control path”以及
  state-relative geometry 与 pairwise conflict 的证据边界；Ch26 已指出多 adapter 冲突，Ch31 已拥有 checkpoint
  identity/lineage。provisional `Refine — Existing Argument` / Ch25，`Status: Experimental`；Historical Books
  Gate 关闭期间不改 Books。
- **Open Questions**：如何用 intervention 区分 geometry signal 与 optimizer/data-order confounder；如何为
  `eta_t` 建立无需 merge-time data 的安全选择规则；limited-memory eviction 如何保持 supersession/rollback
  lineage；作者将如何解释 1.7B 增益数字冲突并发布可复现实验环境。

### GPT-5.5 Instant System Card and Release — 26/30

- **Candidate / Source Family / History**：`OPENAI-GPT55-INSTANT-DEPLOYMENT-SAFETY`；OpenAI system card
  PDF dated 2026-05-04，official card/product pages dated 2026-05-05。它是 W17 GPT-5.5 family 的
  Instant deployment branch，不是第二次基础模型发明事件；主要比较对象是 GPT-5.3 Instant。
- **Full-read Coverage / Evidence Contract**：已读 21 页 system card 的 data/training boundary、disallowed
  content、vision、dynamic mental-health simulation、robustness、connector prompt injection、HealthBench、
  hallucination、bias、Preparedness capability/safeguard sections 与全部表格。评测混合 base-model、不同
  reasoning effort、LLM graders、挑战样本与端到端 safeguards；作者明确很多集合不代表平均 production traffic。
- **Mechanism / State Ownership**：公开材料没有披露 base architecture。可核验的系统机制是 model behavior、
  automated monitors、actor-level enforcement 与 security controls 分层；memory sources 让用户查看、删除或修正
  被引用的历史来源，但页面同时声明所示 sources 未必穷尽全部影响因素。产品层拥有 personalization retrieval，
  model 只消费被选 context，用户保留 source correction/delete authority。
- **What It Proves / Does Not Prove**：它证明该 Instant deployment 首次按 OpenAI Preparedness Framework 在
  Cybersecurity 与 Biological/Chemical 两类作为 High capability 治理，并启用对应 safeguards；不证明 low-effort
  production deployment 等于 xhigh-elicited capability，也不证明离线 grader 比率是线上风险发生率。部分 safety
  slices 有回退，端到端 monitor 又改善结果，说明 model-only 与 deployed-stack safety 必须分开报告。
- **Trade-offs / Evolution / Decision**：`model-only behavior → system-level safeguards → actor enforcement →
  post-deployment monitoring` 是 `Layering / Dependency`。更强 personalization 减少重复输入，却扩大 retrieval、
  stale-memory、consent 与 deletion surface。已读 Ch62、Ch67～69；这些边界已存在，故最终 `No Change —
  Already Covered` / Ch62+68，作为 W17 source-family 的 W19 deployment/safety node 保留。

### EMO: Pretraining Mixture of Experts for Emergent Modularity — 28/30

- **Candidate / Source Family / Revision**：`EMO-DOCUMENT-POOL-MOE-MODULARITY`；arXiv:2605.06663 v1
  2026-05-07、v2 2026-05-10；Ai2 release 2026-05-08。已联合核验 current v2 HTML、Appendix、官方代码、
  1T/130B checkpoints、training/evaluation scripts 与 data entry。
- **Original Problem / Previous Design**：standard token-level MoE 以 conditional compute 扩容量，在通用服务中
  合理；但一个 document 的 tokens 可能遍历几乎全部 experts，expert 又常按 lexical/syntactic pattern 分化，
  因此 active parameters 少并不等于只需加载一个小而语义完整的 expert subset。
- **Changed Constraint / Mechanism**：EMO 用 document boundary 作 weak supervision。每个 document 先得到一个
  shared routed-expert pool `D`，其 tokens 再只在 `D` 内 top-k；pool size `d` 从 `[k,n_r]` 均匀采样，使同一
  checkpoint 适应不同 subset size。global load balancing 跨 data-parallel groups 聚合 routing frequency，避免
  micro-batch balancing 把同文档 token 强行摊散到全部 experts。
- **State / Control / Data Flow**：training data document identity 拥有 pool-scope；router 拥有 token-level
  choice；global batch statistics 拥有 balance signal；deployment selector 用少量 domain validation examples
  排名每层 experts，并生成 domain-specific checkpoint subset。subset identity、selection data、layer-wise expert
  list、base revision 与 fallback-to-full-model 必须成为 artifact/runtime contract。
- **Evaluation Contract**：architecture-matched EMO 与 standard MoE 都是 1B active / 14B total、127 routed +
  1 shared expert、token top-8，在同一 OLMoE corpus 上训练 1T tokens + 50B annealing；130B ablations 比较 dense、
  memory-matched MoE 与 pool-size/load-balance choices。任务含 MC9、Gen5、MMLU/MMLU-Pro domains、GSM8K；
  expert selection 使用 validation split。公开文本未提供可外推的 serving concurrency、device-memory residency、
  expert-loading latency、hardware topology、tail SLO 或多 seed 主结果。
- **Proof Boundary / Failure Modes**：作者数据支持 EMO 在该模型/任务下限制到 25%/12.5% experts 时比 matched
  standard MoE 更保留 accuracy，并出现更强 domain-level routing structure。它不证明 expert clusters 是
  faithful capability modules，不证明任意新 domain 可组合，也不证明总 latency 等比例下降；`Other` catch-all
  类在小 subset 上弱于 memory-matched models，validation format 又会影响 selection。global balance 还新增
  collective cost，错误/陈旧 selector 会形成 silent quality regression。
- **Evolution / ROADMAP / Decision**：`token-level conditional compute → document-consistent routing → selectable
  expert subset → versioned modular deployment` 是 `Direct Evolution`，但 full-model standard MoE 仍适合通用、
  混合或未知 workload。已读 Ch20～22、Ch32/36/45/50；主 owner Ch21，handoff Ch32/45/50。Ch21 已警告
  statistical preference 不等于可命名领域，但尚缺“modularity 必须由 objective + selection contract 共同形成”。
  provisional `Refine — Existing Argument` / Ch21，`Status: Experimental`；Books Gate 关闭期间不写入。

### ERNIE 5.1 Official Release — 26/30

- **Source Family / History / Access**：`ERNIE51-ASYNC-AGENTIC-RL-RUNTIME`；W18 Preview 的 2026-05-09
  formal-release node。官方 Blog 全文可读；未找到独立 technical report、system card、代码或可复现实验 artifact，
  因而标记 `Official Engineering Evidence / Mechanism Partially Disclosed`。
- **Problem / Mechanism Claim**：官方材料把 long-horizon RL 的 training-inference divergence、资源低利用与
  long-tail rollout 作为约束，声明以 RL Controller 解耦 training、inference、reward、agent-loop 四子系统，
  通过网络数据组件形成分离 control/data plane，并让各阶段独立伸缩和 pipeline overlap；另声明统一 FP8 operator、
  Rollout Router Replay、两阶段 compute/communication overlap、KV pooling 与 elastic CPU verifier/sandbox pool。
- **Evidence Boundary**：这些是厂商机制披露，不是公开 implementation proof。参数、成本、KL 与榜单数字缺少足够的
  cluster topology、tokens、batch、concurrency、precision baseline、variance 和 SLO contract，全部保留为作者主张，
  不进入长期 benchmark。Blog 也不能证明 fully asynchronous pipeline 的 staleness、policy lag、backpressure、
  retry、checkpoint consistency 与 failure recovery 已被通用解决。
- **Evolution / Trade-offs / Decision**：`sequential SFT/RL stages → disaggregated subsystem pipeline →
  asynchronous heterogeneous scaling` 是 `Direct Evolution`；旧同步/colocated path 在小规模、强一致或调试场景
  仍更简单。新方案引入 policy-version lineage、sample freshness、cross-stage queues、router replay identity、
  CPU/GPU failure domains 与全局收敛判断。已读 Ch28～30、Ch34～37 与 Ch56；provisional `Refine — Existing
  Argument` / Ch29（algorithm-state）+ Ch37（runtime），但只有未来 technical report/artifact 可使其进入 Books。

### Kubernetes Manifest-Based Admission Control — 27/30

- **Source / Status / Coverage**：`K8S-136-MANIFEST-ADMISSION-BOOTSTRAP`；official Blog 2026-05-04、docs 与
  KEP-5793；Kubernetes 1.36 alpha，feature gate disabled by default。已核验 startup/load/reload、metrics、
  self-contained reference 与 multi-apiserver semantics。
- **Problem / Previous Design**：API-stored admission policy 支持集中管理和 steady-state updates，但 bootstrap、
  etcd recovery 与 policy self-protection 存在 chicken-and-egg gap：policy 尚未创建时不能保护请求，admission
  configuration resources 又为避免循环依赖而不能拦截自身变更。
- **Mechanism / Ownership**：每个 apiserver 从 `staticManifestsDir` 在 serving 前加载 `.static.k8s.io` policies；
  policy 不依赖 etcd，不能引用 `paramKind`、Service webhook 或 manifest set 外对象。runtime file watch 先校验再
  atomic swap，失败保留 last-known-good；initial invalid config 则 fail closed、阻止 apiserver 启动。每个 replica
  独立持有配置，hash metric 用于发现 drift，不提供同步。
- **Trade-offs / Decision**：它关闭 bootstrap/self-deletion gap，却把 disk/config-management/root access、replica
  drift、startup availability 与 break-glass recovery 变成新的 authority surface。`API policy → immutable bootstrap
  anchor + API policy` 是 `Layering / Dependency`，不是废弃动态 admission。已读 Ch53/67～69；provisional
  `Refine — Existing Argument` / Ch68，handoff Ch53/63/69；Alpha 状态和多副本 rollout 证据不得泛化。

### Kubernetes Declarative Validation GA — 26/30

- **Source / Status**：`K8S-136-DECLARATIVE-VALIDATION-RATCHET`；official Blog 2026-05-05 + reference docs；
  framework GA，但 established APIs 仍在持续迁移，不能把“框架 GA”写成“全部 legacy rules 已转换”。
- **Problem / Mechanism**：handwritten Go validation 难以统一、发现和静态分析。`validation-gen` 从 Go type 上的
  `+k8s:` markers 生成 validation functions；ambient ratcheting 以 `oldObject` 判断未改变字段，使新增严格规则
  不必立即拒绝已有 legacy value。structured rules 还能由 linter/OpenAPI tooling 消费。
- **Migration State / Evidence**：Alpha/shadow rules 与 handwritten path 并行运行，mismatch 写日志并增加
  `declarative_validation_mismatch_total`；Beta rules 可成为 authority，遇到 regression 可通过 feature gate
  回到 shadow。rollback 若此前错误允许 invalid object 落库，旧 validator 可能阻断后续 update，极端情况下需
  手工修复 persisted state。
- **Evolution / Decision**：`opaque handwritten rules → generated shadow comparison → mismatch telemetry →
  authoritative rule + rollback` 是可复用的 control-plane migration pattern。它降低规则漂移与 review 成本，
  却新增 generator correctness、marker semantics、dual-path divergence 和 persisted-invalid-state failure mode。
  已读 Ch53、Ch55 与 Ch62～64；provisional `Refine — Existing Argument` / Ch53，handoff Ch63；不把 GA 标签
  外推为 CRD 或所有 ecosystem validator 的行为。

### Kubernetes Server-Side Sharded List and Watch — 28/30

- **Source / Status**：`K8S-136-SERVER-SHARD-LIST-WATCH`；official Blog 2026-05-06、KEP-5866、API docs 与
  implementation PR；Kubernetes 1.36 alpha、disabled by default。
- **Problem / Previous Design**：controller replicas 做 client-side filtering 时，每个 replica 仍接收、反序列化并
  cache 全量高基数对象；水平扩容反而让 API/network/memory cost 近似乘以 replicas。旧模式在小集群或需要每个
  replica 完整视图时仍最简单可靠。
- **Mechanism / Ownership**：client 在 ListOptions 提交 `shardSelector`；apiserver 对 UID 或 namespace 作确定性
  64-bit FNV-1a hash，只返回 `[start,end)` 范围的 list/watch。response `shardInfo` 是 server-acknowledged
  contract；若缺失，client 必须把结果当全量并自行过滤。replica identity/lease/controller 拥有 range assignment；
  apiserver 只执行 selector，不拥有 rebalance、leader election、coverage overlap 或 failover。
- **Trade-offs / Failure Modes / Decision**：它把 event filtering 前移至 server，降低 replica data-plane cost，
  却新增 shard-map ownership、gap/overlap、rebalance、hot shard、resync 与 version compatibility 风险。`full watch
  per replica → client filter → server-acknowledged partition` 是 `Direct Evolution`，但不等于完整 distributed
  work ownership protocol。已读 Ch53、Ch56～58、Ch63；provisional `Refine — Existing Argument` / Ch53，
  handoff Ch63；没有公开 cluster-scale benchmark 时不声称固定节省比例。

### Kubernetes DRA 1.36 Evolution — 28/30

- **Source / Status**：`K8S-136-DRA-READINESS-FALLBACK-WORKLOAD`；official Blog 2026-05-07 + current DRA docs。
  必须逐项区分 stable prioritized list、beta extended-resource bridge/partitionable devices/device taints/device
  binding conditions/resource health，以及 disabled-by-default alpha workload claims、node allocatable、pool status、
  deterministic selection 与 device metadata。
- **Changed Constraint / Mechanism**：heterogeneous accelerators 使单一 device class 太僵硬。prioritized
  subrequests 表达 H100→A100 等 ordered fallback；partitionable device 表达物理设备到逻辑实例；device taint
  管理 faulty/reserved devices；PreBind binding conditions 在 external device ready 前延迟 Pod bind，并以 failure
  condition/timeout 终止。PodGroup-linked ResourceClaim 把共享 claim 从逐 Pod 手工管理推进到 workload scope。
- **Ownership / Failure Modes**：scheduler 拥有 selection/bind transition，driver/ResourceSlice 拥有 inventory、
  attributes、health 与 readiness，external controller 拥有 preparation，workload 必须接受同一 ReplicaSet 不同 Pod
  可能选择不同 fallback。health visibility 不自动触发 eviction；prioritized fallback 也不保证性能等价。新增的
  stale inventory、prebind timeout、partial preparation、driver ordering influence、metadata version 与 gang rollback
  都需显式治理。
- **Evolution / Decision**：`integer extended resource → typed claim/allocation → fallback/partition/health →
  readiness-gated workload claim` 是 `Direct Evolution`；MIG/static profile 和 legacy extended resource 在强隔离或
  渐进迁移中仍成立。已读 Ch56、Ch59～61、Ch63/69；provisional `Refine — Existing Argument` / Ch59，handoff
  Ch56/60/61/63；版本阶段不同，不能用 DRA core stability 替子特性背书。

### NCCL Inspector Prometheus Mode — 28/30

- **Source / History / Coverage**：`NCCL-INSPECTOR-REALTIME-TELEMETRY`；NVIDIA Blog 2026-05-07、NCCL
  2.30 Inspector README、Grafana template；与此前 JSON/offline Inspector 联读。已核验 plugin state、dump
  interval、labels、file lifecycle、Prometheus/OTLP output、cardinality 与示例 triage。
- **Problem / Mechanism**：offline per-rank JSON 支持深度分析，但文件随 collectives、communicators 持续增长，
  不适合持续 fleet dashboard。Prometheus mode 在每 GPU/rank 聚合 operation type、message bucket、algo/proto、
  time 与 bandwidth，持续覆写 textfile，由 node exporter 收集；默认聚合 OTLP 走本地 plaintext collector。
- **State / Evidence Boundary**：NCCL plugin 拥有 communicator/rank operation state，per-GPU UUID 区分 device，
  exporter 拥有 scrape，Prometheus 拥有 time series，Grafana 只展示派生视图。官方案例展示指标与 network
  slowdown 同期相关，不能单凭 correlation 证明 root cause；所谓 minimal overhead 没有公开完整 profiler-on/off、
  topology、model、precision、concurrency 与 tail-SLO 对照。
- **Trade-offs / Decision**：`offline event log → periodic aggregate metrics → temporary verbose drill-down` 是
  `Direct Evolution`。聚合降低 storage/cardinality，却丢失单 operation lineage；verbose OTLP 官方说明可把
  cardinality 放大约 100 倍，只应短期开启。已读 Ch32、Ch62～65；provisional `Refine — Existing Argument` /
  Ch63，handoff Ch32/65；fine-grained trace、network counters 与 application throughput 仍需联合证据。

### vLLM v0.20.1-v0.20.2 Stabilization Series — 24/30

- **Source Family / History**：`VLLM-020-DEEPSEEKV4-STABILIZATION`；v0.20.1 released 2026-05-04、v0.20.2
  2026-05-10；联合核验 official release notes 与 persistent-topk fix PR。它延续 W18 v0.20.0，不拆成两个独立
  architecture events。
- **Mechanism / Evidence**：v0.20.1 为 DeepSeek V4 增加 multi-stream pre-attention GEMM、BF16/MXFP8
  one-sided A2A、FP4 conversion 与 integrated kernels，同时因 cooperative deadlock / RadixRowState race 暂时
  disable persistent top-k；v0.20.2 又在 Hopper 恢复路径并修复 CUDA-graph memset、MTP=1 hang、V1 KV block
  allocation、MXFP4 compile 与 heavy-load boundary errors。
- **Proof Boundary / Evolution**：release/PR 证明特定代码路径与 failure 修复，不证明对所有模型、GPU 或 workload
  有端到端收益。`optimization enable → concurrency/capture failure → guarded disable → corrected re-enable` 表明
  fast path 必须拥有 capability gate、fallback、race/capture tests 与 rollback；这已经被 Ch46 的 shared scheduler/
  KV correctness 和 version-boundary 论证覆盖。最终 `Weekly Only — Versioned Stabilization Evidence` / Ch46，
  不修改 Books，不引用无完整 contract 的性能数字。

### NSF OMAI Compute Online — 18/30

- **Boundary Review**：Ai2 official announcement 2026-05-07 只核验 Blackwell Ultra-powered compute 进入
  operational state、NSF/NVIDIA funding 与 fully-open ecosystem intent。页面未披露 cluster topology、scheduler、
  storage/network、allocation policy、reproducibility ledger、SLO 或 implementation artifact。
- **Decision**：这是重要科研基础设施可用性/治理事件，但不是新的 AI System mechanism；`Weekly Only —
  Infrastructure Availability / Mechanism Not Disclosed`，无 Books owner。开放目标不能替代每次训练的 data、code、
  checkpoint、environment 与 cost provenance。

## Pending Full Source Review Queue

当前 scored candidate set 无 pending。仅 StraTA 保持 `Unverified / Blocked Backlog`，其缺失材料为
arXiv:2605.06642 的 v1 正文或同版 PDF/HTML；cross-index 与
OpenReview/TMLR recall 仍是 W19 Historical Evidence Gate 的未闭合项。fixed official/Infra
source-list checkpoint 已通过，不再与学术交叉索引 backlog 混记。

## Repository Changes

- 2026-08-13 重新逐行复算为 35 scored（27 high、7 mid、1 low）：33 个 `20+`
  Full Source Reviews、1 个 scored blocked identity、1 个低分边界、0 ordinary pending。blocked 项未被计入
  全文阅读，也未阻塞 forward cursor；academic cross-index 仍未闭合，Historical Books Gate 保持关闭。
- W19 从 3 个 baseline families 扩展为 35 个 scored families：34 项达到 `20+`，其中 33 项
  Full Source Reviews 已完成，StraTA 因正文不可访问保留在明确 blocked backlog；NSF OMAI 完成
  1/1 低分来源与机制边界核验。fixed official/Infra
  checkpoint 恢复并审计 GPT-5.5 Instant、EMO、ERNIE 5.1、四项 Kubernetes 1.36 机制、NCCL
  Inspector 与 vLLM stabilization series；scored candidate review queue 已闭合，forward cursor 保持在
  W20 之后的既有单向位置。
  已把 5 个 curation-lag candidates 按 v1 日期回拨 W18；另将
  W20 推荐流中 8 个 v1 日期属于本周的 families 归回 W19。保留三项
  baseline reviews 与 disposition 作为输入。2026-08-14 已完成 35/35 最终 disposition，并把长期机制
  整合到 Ch21、Ch26、Ch43、Ch57、Ch66、Ch67、Ch77；其余 owner 完成具体论点级复核，未重复追加摘要。

## Open Questions

1. language autoencoder 的 reconstruction faithfulness 怎样通过 counterfactual intervention
   验证？
2. ARIS 的 compute-matched protocol 若执行，cross-family reviewer 是否仍能提高 issue recall，
   其 false-positive、cost 与 latency 代价是多少？
3. Geometry Conflict 的 pairwise/state-relative/global geometry 指标如何通过 intervention 区分因果机制与
   optimizer/data-order confounder，作者如何修正 1.7B 增益数字冲突？
4. OpenReview/TMLR、DBLP、Scholar/OpenAlex 的交叉召回还会恢复哪些遗漏？

## Sources

- Anthropic Research index, entries dated 2026-05-07 and 2026-05-08:
  https://www.anthropic.com/research
- OpenAI Research release index, voice-model entry dated 2026-05-07:
  https://openai.com/research/index/release/
- Hugging Face Papers, 2026-W19 discovery index: https://huggingface.co/papers/week/2026-W19
- ARIS: https://arxiv.org/abs/2605.03042
- ARIS HTML: https://arxiv.org/html/2605.03042
- ARIS repository: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep
- MolmoAct2: https://arxiv.org/abs/2605.02881
- MolmoAct2 repository: https://github.com/allenai/molmoact2
- HeavySkill: https://arxiv.org/abs/2605.02396
- HeavySkill HTML: https://arxiv.org/html/2605.02396
- HeavySkill repository: https://github.com/wjn1996/HeavySkill
- T2PO: https://arxiv.org/abs/2605.02178
- T2PO HTML: https://arxiv.org/html/2605.02178
- T2PO repository: https://github.com/WillDreamer/T2PO
- PhysicianBench: https://arxiv.org/abs/2605.02240
- PhysicianBench HTML: https://arxiv.org/html/2605.02240
- PhysicianBench project: https://healthrex.github.io/PhysicianBench/
- OpenSeeker-v2: https://arxiv.org/abs/2605.04036
- OpenSeeker-v2 HTML: https://arxiv.org/html/2605.04036
- OpenSeeker repository: https://github.com/PolarSeeker/OpenSeeker
- Rethinking Reasoning-Intensive Retrieval: https://arxiv.org/abs/2605.04018
- Rethinking Reasoning-Intensive Retrieval, ACL 2026 full text:
  https://aclanthology.org/2026.acl-long.1705/
- Workspace-Bench 1.0: https://arxiv.org/abs/2605.03596
- Workspace-Bench HTML: https://arxiv.org/html/2605.03596
- Workspace-Bench repository: https://github.com/OpenDataBox/Workspace-Bench
- OpenSearch-VL: https://arxiv.org/abs/2605.05185
- Skill1: https://arxiv.org/abs/2605.06130
- StraTA: https://arxiv.org/abs/2605.06642
- AI co-mathematician: https://arxiv.org/abs/2605.06651
- AI co-mathematician HTML: https://arxiv.org/html/2605.06651
- Auto Research with Specialist Agents: https://arxiv.org/abs/2605.05724
- Auto Research with Specialist Agents HTML: https://arxiv.org/html/2605.05724
- Auto Research with Specialist Agents repository: https://github.com/cxcscmu/Auto-Research-Recipes
- A2TGPO: https://arxiv.org/abs/2605.06200
- A2TGPO HTML: https://arxiv.org/html/2605.06200
- A2TGPO repository: https://github.com/CuSO4-Chen/A-TGPO
- STALE: https://arxiv.org/abs/2605.06527
- STALE HTML: https://arxiv.org/html/2605.06527
- UniPrefill: https://arxiv.org/abs/2605.06221
- UniPrefill HTML: https://arxiv.org/html/2605.06221
- UniPrefill repository: https://github.com/qhfan/UniPrefill
- LLMs Improving LLMs: https://arxiv.org/abs/2605.08083
- LLMs Improving LLMs PDF: https://arxiv.org/pdf/2605.08083
- AutoTTS repository: https://github.com/zhengkid/AutoTTS
- HyperEyes: https://arxiv.org/abs/2605.07177
- HyperEyes HTML: https://arxiv.org/html/2605.07177
- HyperEyes repository: https://github.com/DeepExperience/HyperEyes
- Soohak: https://arxiv.org/abs/2605.09063
- MCP-Cosmos: https://arxiv.org/abs/2605.09131
- MemPrivacy: https://arxiv.org/abs/2605.09530
- Geometry Conflict: https://arxiv.org/abs/2605.09608
- GPT-5.5 Instant product note: https://openai.com/index/gpt-5-5-instant/
- GPT-5.5 Instant system card page: https://openai.com/index/gpt-5-5-instant-system-card/
- GPT-5.5 Instant system card PDF:
  https://deploymentsafety.openai.com/gpt-5-5-instant/gpt-5-5-instant.pdf
- EMO: https://arxiv.org/abs/2605.06663
- EMO HTML: https://arxiv.org/html/2605.06663
- EMO repository: https://github.com/allenai/EMO
- EMO official release: https://allenai.org/blog/emo
- ERNIE 5.1 official release: https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/
- Kubernetes Manifest-Based Admission Control:
  https://kubernetes.io/blog/2026/05/04/kubernetes-v1-36-manifest-based-admission-control/
- Kubernetes Declarative Validation GA:
  https://kubernetes.io/blog/2026/05/05/kubernetes-v1-36-declarative-validation-ga/
- Kubernetes Declarative Validation reference:
  https://kubernetes.io/docs/reference/using-api/declarative-validation/
- Kubernetes Server-Side Sharded List and Watch:
  https://kubernetes.io/blog/2026/05/06/kubernetes-v1-36-server-side-sharded-list-and-watch/
- Kubernetes KEP-5866: https://github.com/kubernetes/enhancements/issues/5866
- Kubernetes API concepts: https://kubernetes.io/docs/reference/using-api/api-concepts/
- Kubernetes DRA 1.36 updates:
  https://kubernetes.io/blog/2026/05/07/kubernetes-v1-36-dra-136-updates/
- Kubernetes DRA reference:
  https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/
- NVIDIA NCCL Inspector Prometheus mode:
  https://developer.nvidia.com/blog/real-time-performance-monitoring-and-faster-debugging-with-nccl-inspector-and-prometheus/
- NCCL Inspector README:
  https://github.com/NVIDIA/nccl/blob/master/plugins/profiler/inspector/README.md
- vLLM v0.20.1: https://github.com/vllm-project/vllm/releases/tag/v0.20.1
- vLLM v0.20.2: https://github.com/vllm-project/vllm/releases/tag/v0.20.2
- vLLM persistent top-k repair: https://github.com/vllm-project/vllm/pull/41665
- Ai2 NSF OMAI compute status: https://allenai.org/blog/omai-compute-now-live

## 2026-08-14 Final Source-Family Books Integration Ledger

MolmoAct2 的 2026-08-13 独立 Gate 结论已并入本账本。W19 不按论文顺序向章末追加，而先复核 owner
章节及相邻章节，再把真正缺失的机制放回既有演进链。最终计数为 35/35：25 Refine、6 No Change、
3 Weekly Only、1 Unverified / Blocked。

| Source Family | Final Disposition | Stable Owner | Current / Legacy | Books Review Result |
| --- | --- | --- | --- | --- |
| Natural Language Autoencoders | No Change | `WORLDVIEW-REPRESENTATION` | Ch5 / Ch5 | 已有 correlation→intervention→replication evidence ladder；可读重建不升级为 faithful internal state |
| Teaching Claude why | No Change | `TRAIN-RLHF` | Ch31 / Ch27 | principle/explanation supervision 已由 behavior/evidence boundary 覆盖 |
| OpenAI voice models | Weekly Only | — | — | Version/Product Fact；内部机制未披露 |
| MolmoAct2 | Refine | `MULTIMODAL-EMBODIED-VLA` | Ch26 / N/A | reasoner→generator→controller 分层、action identity 与 physical evidence boundary 已吸收 |
| ARIS | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | claim-level provenance 增加 fresh/cross-round assurance 与 correlated-reviewer boundary；Workflow 仅 handoff |
| Skill1 | Refine | `AGENT-MEMORY` | Ch77 / Ch73 | Skill extraction、admission、utility evidence、supersession/retirement 已作为 derived memory lifecycle |
| OpenSearch-VL | Refine | `TRAIN-GRPO` | Ch33 / Ch29 | modality/phase-specific credit 与 verifier ownership 已吸收；作者结果不外推 |
| OpenSeeker-v2 | No Change | `TRAIN-DATA` | Ch27 / Ch23 | executable reasoner/verifier data loop 已有具体论点 |
| Rethinking Reasoning-Intensive Retrieval | Refine | `AGENT-RAG` | Ch76 / Ch72 | query distribution、retrieval budget、evidence use 与 outcome 分层已覆盖 |
| StraTA | Unverified / Blocked | — | — | 缺 v1 正文；不按标题推断 trajectory abstraction 或 state ownership |
| HeavySkill | Refine | `AGENT-MULTI-AGENT` | Ch82 / Ch78 | trajectory aggregation 保留 read-only evidence、segment provenance 与 coordination cost |
| AI co-mathematician | Refine | `AGENT-WORKFLOW` | Ch81 / Ch77 | human-steered state、termination、review disagreement 与 artifact authority 已吸收 |
| Auto Research with Specialist Agents | Refine | `AGENT-WORKFLOW` | Ch81 / Ch77 | append-only trial lineage、specialist handoff 与 no-lineage control 已吸收 |
| A2TGPO | Refine | `TRAIN-GRPO` | Ch33 / Ch29 | cohort、credit 与 update granularity 对齐为 typed reward contract |
| Workspace-Bench 1.0 | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | workspace artifact、environment state、post-state verifier 与 ACL/repository boundary 已吸收 |
| T2PO | Refine | `TRAIN-GRPO` | Ch33 / Ch29 | phase-specific/turn-level credit 已并入 terminal-gate 演进线 |
| PhysicianBench | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | reasoning/action/documentation checkpoints 与 post-state evidence 已吸收 |
| MemPrivacy | Refine | `PLATFORM-SECURITY` | Ch72 / Ch68 | edge detector、typed policy、cloud storage 与 local restoration 分层；不宣称端到端隐私 |
| Soohak | No Change | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | domain benchmark 仍服从完整 subject/distribution/scorer contract |
| LLMs Improving LLMs | Refine | `AGENT-WORKFLOW` | Ch81 / Ch77 | controller discovery、fixed replay 与 online execution cost 分离已覆盖 |
| HyperEyes | Refine | `TRAIN-GRPO` | Ch33 / Ch29 | hindsight relevance 保持 proxy，不升级为 causal credit |
| MCP-Cosmos | No Change | `AGENT-PLANNING` | Ch79 / Ch75 | planning state、tool/environment opportunity 与 outcome 已分层 |
| Geometry Conflict | Refine | `TRAIN-SFT` | Ch29 / Ch25 | pairwise、state-relative 与 global update geometry 共存；冲突数字排除 |
| STALE | Refine | `AGENT-MEMORY` | Ch77 / Ch73 | retrieval 与 adjudication 分离，新增 `UNKNOWN_CURRENT` 与跨属性失效传播 |
| UniPrefill | Refine | `INFER-PREFILL` | Ch43 / Ch39 | sparse attention 扩展为 hybrid-block token-state propagation 与逐层 KV-slot identity |
| GPT-5.5 Instant | No Change | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | W17 family 的 system-card branch；不推断基础模型机制 |
| EMO | Refine | `MODEL-MOE` | Ch21 / Ch21 | document-scoped pool 说明 modularity 由 objective + selector contract 形成 |
| ERNIE 5.1 | Refine | `TRAIN-GRPO` | Ch33 / Ch29 | official engineering evidence 仅支持异步 rollout/control-plane 分层，不采用 benchmark headline |
| Kubernetes Manifest-Based Admission | Refine | `PLATFORM-FOUNDATIONS` | Ch57 / Ch53 | immutable bootstrap trust anchor 与动态 policy 共存，不把 Alpha 当通用安全保证 |
| Kubernetes Declarative Validation GA | Refine | `PLATFORM-FOUNDATIONS` | Ch57 / Ch53 | shadow/mismatch/takeover 属于控制面迁移，不等于 CRD 自动兼容 |
| Kubernetes Server-Side Sharded List/Watch | Refine | `PLATFORM-FOUNDATIONS` | Ch57 / Ch53 | server partition 与 replica work ownership 分离，保留 gap/overlap/rebalance failure modes |
| Kubernetes DRA 1.36 | Refine | `PLATFORM-GPU-SCHEDULER` | Ch63 / Ch59 | typed claim→fallback/partition/health→readiness-gated allocation 演进已复核 |
| NCCL Inspector Prometheus Mode | Refine | `PLATFORM-MONITORING` | Ch67 / Ch63 | offline event→periodic aggregate→temporary verbose drill-down；相关性不等于 root cause |
| vLLM v0.20.1–0.20.2 | Weekly Only | `INFER-VLLM` | Ch50 / Ch46 | Versioned stabilization evidence；fast-path disable/re-enable 不形成新通用机制 |
| NSF OMAI compute online | Weekly Only | — | — | Infrastructure availability；topology、allocation 与 SLO mechanism 未披露 |

### Owner Review

19 个 owner 被修改或重新验证：`WORLDVIEW-REPRESENTATION`、`TRAIN-RLHF`、
`MULTIMODAL-EMBODIED-VLA`、`PLATFORM-EVALUATION-SYSTEM`、`AGENT-MEMORY`、`TRAIN-GRPO`、
`TRAIN-DATA`、`AGENT-RAG`、`AGENT-MULTI-AGENT`、`AGENT-WORKFLOW`、`PLATFORM-SECURITY`、
`AGENT-PLANNING`、`TRAIN-SFT`、`INFER-PREFILL`、`MODEL-MOE`、`PLATFORM-FOUNDATIONS`、
`PLATFORM-GPU-SCHEDULER`、`PLATFORM-MONITORING` 和 `INFER-VLLM`。其中 Ch21、Ch26、Ch43、Ch57、
Ch66、Ch67、Ch77 是本周实际吸收或既有独立 Gate 的正文修改点，其余是具体论点级覆盖复核；因此 owner
名单多于 modified file 数，不代表重复写入。

本周实际新增或强化的主线是：objective-shaped MoE modularity；hybrid Prefill 的跨层 active-token state；
claim ledger 的独立 assurance；Memory 的 unknown-current adjudication；Kubernetes bootstrap validation 与
server-acknowledged partition；collective telemetry 的 aggregate→drill-down 分层。其他 Refine family 已在当前
Books 的 typed reward、Skill/Workflow、RAG、Evaluation、Security、DRA 和 Embodied 主线中逐项复核，未重复
追加论文摘要。StraTA 与 Archive Completion Gate 保持 Open；没有来源材料的机制没有进入 Books。
