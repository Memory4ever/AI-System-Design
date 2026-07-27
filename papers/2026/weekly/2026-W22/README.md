# AI Research Weekly — 2026-W22

> Coverage Window: 2026-05-25～2026-05-31
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-09
> Re-audit Status: 2026-08-14 Source-Family Books Gate Complete; 43/43 final dispositions; 42/42 `20+` Full Source Reviews complete; 0 Unverified / Blocked; 0 current-review pending; 1 low-score fact verified; broader Archive/Discovery Gate remains Open for cross-index replay; Books cursor advances to W23

## Executive Summary

> **Access-history note（superseded 2026-08-13）**：下文保留了修复过程中的旧 access-boundary 叙述，
> 仅用于说明当时为什么没有从标题或摘要推断机制。其 current status 以 Candidate Scoring、
> `Primary-Text Recovery Addendum — 27 Full Source Reviews` 与 Discovery Recall Ledger 为准：
> 42/42 个 `20+` families 已完成 Source Review，0 blocked，0 ordinary pending。

旧版 W22 只保留三项机构事件，未证明论文与 Infra 候选池完整。本轮先从 W22 feed 恢复 16 个
in-window academic families；重放 W23 的 “May 31～Jun 6” 展示窗后，又按 arXiv v1 日期回收
16 个实际属于 05-25～05-31 的 curation-lag families；W24 display feed 又恢复 v1 05-28 的
ResearchClawBench，W25 feed 又恢复 v1 05-29 的 Smaller Models Are Natural Explorers。W22 feed 中
6 个 v1 属于 W21 的条目仍回拨
前周。baseline 中 Anthropic 研究 coding agents 在社会科学中的使用，Google 发布 zero-trust aggregation 的
private analytics 工作，OpenAI 扩展 Rosalind biodefense trusted access。共同的系统问题是：
高价值 Agent 需要 telemetry 和 evaluation，但原始用户/领域数据又不能被集中暴露。因此
measurement architecture、privacy boundary 与 access governance 必须共同设计。

ScientistOne 论文 v1 归 W22，7 月 30 日 Google Research 文章仍只属于 W31 publication node。
它的全文、implementation appendices、audit procedure、failure taxonomy、limitations 与 Ch62/77
邻接已在 Live W31 source family 审计中完成，本周将这份阅读证据归回 first-public 周，而不复制
Books 内容。Gamma-World 又完成唯一 v1、21 页全文、Appendix A～F、NVIDIA project、06-16 后发
code/training/inference artifact 与 Ch10/13/14/40 邻接审计。它把单主体视频 world model 扩展为
exchangeable agent axis、hub-mediated shared state 与 bidirectional-teacher→causal cached-student 的联合设计，
暂定 Ch10 `Refine — Existing Argument / Experimental`；训练只覆盖 two-player、four-player/robot 主要是
定性 evidence，24 FPS 也缺少完整硬件/latency/SLO contract，故不外推为普遍实时或物理一致。AgentDoG 1.5
只能核验 05-28 唯一 v1 metadata、abstract 与 44-page paper surface，完整正文在当前允许路径不可读；W08 的
OpenClaw trajectory audit 只把 AgentDoG 当 judge，不能替代本篇审计。它转入 `Unverified / Blocked Backlog`，
不计 Full Source Review 且不阻塞 forward cursor。DVAO 已完成唯一 v1、全文、三个理论 Appendix、implementation/
limitations 与 Ch28～30 邻接审计。它把 multi-reward GRPO 从 raw Reward Combination、per-objective Advantage
Combination 推进到 group-wise variance-adaptive weighting，但仍依赖基础权重、可靠 reward 与足够大的 group；
dual-objective、`G=16` evidence 不支持任意多目标或生产稳定性外推。暂定 Ch29 `Refine — Existing Argument /
Experimental`。OmniRetrieval 已完成唯一 v1、全文、evaluation、current official repository/code path 与
Ch71/72/74 邻接审计。它保留 SQL/SPARQL/Cypher/search 的 native operator，以 source routing → native query
generation/execution → late evidence selection 代替把全部来源压成统一 embedding；但实验问题各自只有一个 gold
source，selector 只选一个候选，未证明真正的 cross-source join。freshness、ACL、schema drift、query safety、
partial failure、provenance 与生产 latency/SLO 也未进入 contract，故暂定 Ch72 `Refine — Existing Argument /
Experimental`。MobileGym 又完成 v1/v2 revision、全文与全部 Appendices、project/repository 和 Ch61～63/
Ch29/80 handoff 审计。其核心是用同一份结构化 environment state 支撑 configure/reset/fork、deterministic
judge、unexpected-side-effect diff 与 RL reward；但 browser surrogate 主动舍弃真实 backend、stochastic service
与完整 feature surface，real-device evidence 又是 outcome-stratified 的 59-task signal subset 加 15 项 negative control，
只能作为 transfer existence proof。暂定 Ch62 `Refine — Existing Argument / Experimental`。BES 已完成唯一 v1、
全部 Appendices、theory assumptions、三个 evaluation settings、ablation/cost 与 official project/repository 审计。
它把独立 rollout / expansion-only tree 扩展为可重组的 step-level candidate pool，再用 backward goal tree 的
local verifier 稠密化 selection signal；但 entropy-shell 结果只说明候选可离开 policy typical region，不证明语义
有效或最终正确，所谓 exponential advantage 又依赖 subgoal independence、可靠 decomposition/verifier 与可正确
recombine 的假设。作者 evidence 仅覆盖至 8B post-training 和三项 3-seed GPT-5 program search，故暂定 Ch20
`Refine — Existing Argument / Experimental`，Ch29/75 只承接 rollout generation 与 planning handoff。
ResearchMath-14K 又完成唯一 v1、全部 Appendices、current dataset artifact 与 Ch22～25/62
去重审计。它把 research-question data 分成 source quote、self-contained rewrite、mutable open-status evidence、
teacher attempt 与 filter verdict；但 self-containment/status/difficulty/filter 主要仍由同一代 model/agent judges
产生，且“filtered”定义在正文存在不一致。当前公开仓库只明确呈现 14,056 条问题记录，未见论文声称的
220K trajectories、5K filtered subset、training code 或 adapters；三模型 LoRA 结果也缺 hardware、optimizer/LR、
precision 与 benchmark decontamination contract。因此暂定 Ch23 `Refine — Existing Argument / Experimental`，
不把“wrong-but-reasonable”外推为无需正确性检查。How LoRA Remembers? 的 arXiv HTML/PDF 在当前允许
路径被明确拒绝访问，因此转入 `Unverified / Blocked Backlog`，不使用标题或摘要反推机制、不分配 Books owner、
不计 Full Source Review，也不阻塞 forward cursor。MemTrace 的 arXiv 与 Hugging Face paper surface 同样被当前
保存权限拒绝，仓库亦无可审计正文或作者 artifact；它也转入 blocked backlog，不把 pending focus 当作已证机制。
CUA-Gym 的 arXiv 域与最直接的 QwenLM/CUA-Gym 官方仓库路径也被保存权限拒绝，本地无对应材料；它转入
同一 backlog，不以产品/仓库名反推 environment、verifier 或 RL 机制。LaRA 只有同一受限 arXiv primary-source
surface，工作区和本地缓存无正文或作者 artifact；它也转入 backlog，不把待审的 geometry/contamination focus 当结果。
FluxMem 也只有受限 arXiv surface 与尚未发布的 planned-code 占位，本地没有 paper/code/artifact；它转入 backlog，
不从名称推断 memory connectivity、feedback、pruning 或 consolidation 机制。Skill0.5 的 Sources 也只有同一受限
arXiv URL；Pending 表中的“+ code”没有 repository URL、release 或 commit identity，本地无 artifact，因此转入 backlog，
不推断 internalize/externalize router 或 skill-conflict 机制。SkillGrad 也只有受限 arXiv URL 与无法定位的“+ code”
标签，本地无材料；它转入 backlog，不把 textual gradient/momentum/patch safety 当事实。Claw-Anything 只有同一
受限 arXiv surface，本地无正文或 artifact；它转入 backlog，不从“always-on”名称推断权限、隐私或主动行为。
Crafter 也只有受限 arXiv URL；`+ code/benchmark` 缺 repository/dataset/release/commit identity，本地无 artifact，
故转入 backlog，不把 SVG、multi-agent、verifier 或 visual-quality focus 当证据。Domino 的 `+ code` 同样没有
artifact identity，本地无材料；它转入 backlog，不推断 speculative architecture 或 acceptance/latency。
COLLEAGUE.SKILL 的 `open-source artifact` 也没有 URL/owner/release/commit identity，本地无材料；它转入 backlog，
不推断 trace-to-skill、capability/behavior split 或 rollback。GrepSeek 的 `+ code` 同样无法定位，本地无材料；
它转入 backlog，不推断 Tutor/Planner、GRPO、sandbox 或 byte-equivalence。TASTE 的 `+ benchmark` 也没有
repository/dataset/release/split identity，本地无材料；它转入 backlog，不推断 generation/judge/coverage/contamination。
Trust-Region Behavior Blending 只有受限 arXiv source，本地无正文或 artifact；它转入 backlog，不推断 KL bound、
annealing、prefix distribution 或 stability。Trust Region On-Policy Distillation 同样只有受限 arXiv source、本地无材料；
它转入 backlog，不推断 region split、KL estimator 或 mask/clip behavior。LongTraceRL 的 `+ code/data/models` 没有
repository/dataset/model/release/commit identity，本地无材料；它转入 backlog，不推断 distractor/rubric/reward-hacking。
该句记录当时的中间 checkpoint；后续十项均已转入有据可查的 Full Source Review 或明确的
`Unverified / Blocked Backlog`，本周最终 current-review queue 为 0。

## Coverage and Source Coverage

- 模型与研究机构：保留 Anthropic 5 月 27 日、Google 5 月 27/28 日、OpenAI 5 月 29 日。
- 论文与学术来源：重放 Hugging Face W22（页面覆盖 05-24～05-30），逐项核对 arXiv v1；
  累计恢复 34 个 W22 families，6 项回拨 W21。ScientistOne、Gamma-World、原 blocked ledger 的
  27 个 academic families，以及 DVAO、OmniRetrieval、MobileGym、BES 与 ResearchMath-14K 均已完成
  current-version 全文/Appendix 或 artifact/章节复核；Scholar、
  OpenAlex、DBLP 与 formal publication cross-check 仍 pending。
- AI Infra：fixed official replay 新增 Dynamo Snapshot、DynoSim、DOCA in-silicon security、Vera CPU、DSX OS
  与 STAC-AI workload-contract benchmark；六项均完成官方全文与相邻章节边界审计。Transformers 本周无新
  release，Kubernetes/vLLM/SGLang/KServe 未发现需新增的 in-window retained stable-release family；这不是
  对所有 PR 的 exhaustive absence proof。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Private analytics via zero-trust aggregation | 4 | 4 | 4 | 4 | 4 | 5 | 25/30 | Must Read |
| Coding agents in social sciences | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Worth Watching |
| Rosalind Biodefense access expansion | 2 | 3 | 3 | 5 | 3 | 3 | 19/30 | Governance record |
| Gamma-World | 5 | 5 | 4 | 4 | 3 | 4 | 25/30 | Full Source Review complete；provisional R / Ch10 / Experimental |
| AgentDoG 1.5 | 4 | 5 | 5 | 4 | 5 | 2 | 25/30 | Full Source Review complete；provisional R / Ch68 / Experimental |
| DVAO | 5 | 4 | 4 | 4 | 5 | 3 | 25/30 | Full Source Review complete；provisional R / Ch29 / Experimental |
| OmniRetrieval | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review complete；provisional R / Ch72 / Experimental |
| MobileGym | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full Source Review complete；provisional R / Ch62 / Experimental |
| Self-Improving LMs with Bidirectional Evolutionary Search | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Full Source Review complete；provisional R / Ch20 / Experimental |
| ResearchMath-14K | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review complete；provisional R / Ch23 / Experimental |
| How LoRA Remembers? | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review complete；provisional R / Ch26 / Experimental |
| MemTrace | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full Source Review complete；provisional R / Ch73 / Ch65 handoff / Experimental |
| ScientistOne / Chain-of-Evidence | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Must Read — full review complete |
| CUA-Gym | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Full Source Review complete；provisional R / Ch62 / Ch77 handoff / Experimental |
| LaRA contamination detection | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review complete；provisional R / Ch62 / Experimental |
| FluxMem | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Full Source Review complete；provisional R / Ch73 / Experimental |
| Skill0.5 | 5 | 4 | 4 | 4 | 5 | 3 | 25/30 | Full Source Review complete；provisional R / Ch80 / Ch29 handoff / Experimental |
| SkillGrad | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review complete；provisional R / Ch80 / Experimental |
| Claw-Anything | 4 | 5 | 4 | 4 | 5 | 2 | 24/30 | Full Source Review complete；provisional R / Ch62 / Ch68 handoff / Experimental |
| Crafter | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review complete；provisional R / Ch77 / Experimental |
| Domino speculative decoding | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full Source Review complete；provisional R / Ch44 / Experimental |
| COLLEAGUE.SKILL | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review complete；provisional R / Ch80 / Experimental |
| GrepSeek | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full Source Review complete；provisional R / Ch72 / Ch77 handoff / Experimental |
| TASTE agent-benchmark synthesis | 5 | 5 | 5 | 4 | 5 | 2 | 26/30 | Full Source Review complete；provisional R / Ch62 / Experimental |
| Trust-Region Behavior Blending | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review complete；provisional R / Ch25 / Experimental |
| Trust Region On-Policy Distillation | 5 | 4 | 4 | 4 | 5 | 3 | 25/30 | Full Source Review complete；provisional R / Ch25 / Experimental |
| LongTraceRL | 4 | 4 | 5 | 4 | 5 | 3 | 25/30 | Full Source Review complete；provisional R / Ch22 / Ch29 handoff / Experimental |
| dMoE | 5 | 5 | 4 | 4 | 5 | 2 | 25/30 | Full Source Review complete；provisional R / Ch21 / Experimental |
| SkillAdaptor | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review complete；provisional R / Ch80 / Experimental |
| Draft-OPD | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full Source Review complete；provisional R / Ch44 / Ch25 handoff / Experimental |
| SCOPE | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review complete；provisional R / Ch29 / Experimental |
| Harness Updating Is Not Harness Benefit | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Full Source Review complete；provisional R / Ch80 / Ch62 handoff / Experimental |
| SAAS over-search mitigation | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review complete；provisional R / Ch75 / Experimental |
| RAMP runtime Agent assessment | 4 | 5 | 4 | 4 | 5 | 3 | 25/30 | Full Source Review complete；provisional R / Ch62 / Ch65 handoff / Experimental |
| Masking Stale Observations | 5 | 4 | 5 | 4 | 5 | 2 | 25/30 | Full Source Review complete；provisional R / Ch71 / Experimental |
| ResearchClawBench | 4 | 5 | 5 | 4 | 5 | 2 | 25/30 | Full Source Review complete；provisional R / Ch62 / Experimental |
| Smaller Models Are Natural Explorers | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review complete；provisional R / Ch29 / Experimental |
| NVIDIA Dynamo Snapshot | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full review complete — provisional Refine Ch46/53 / Experimental |
| DynoSim serving-stack digital twin | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full review complete — provisional Refine Ch62 / Official Engineering Evidence |
| NVIDIA DOCA in-silicon security | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Full review complete — provisional Refine Ch68 / Official Engineering Evidence |
| NVIDIA Vera CPU agentic-workload contract | 4 | 5 | 4 | 4 | 5 | 3 | 25/30 | Full review complete — provisional Refine Ch50 / Official Engineering Evidence |
| NVIDIA DSX OS AI-factory control plane | 4 | 5 | 4 | 4 | 5 | 3 | 25/30 | Full review complete — provisional Refine Ch53/63 / Official Engineering Evidence |
| NVIDIA STAC-AI LANG6 workload contract | 3 | 4 | 4 | 5 | 4 | 3 | 23/30 | Full review complete — No Change / Ch62 |

当前账目为 43 行：30 个 `25～30`、12 个 `20～24`、1 个 `<20`。42 个 `20+` families 的 primary
text 均已恢复并完成 current-version review；评分只决定审计优先级，不等于 Books disposition。

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Baseline score rows | 3 | 2 项 `20+` reviews；1 项低分 governance fact |
| Recovered in-window families | 40 | 40 个 academic/official/Infra families 已完成 current-version review；0 blocked；0 current-review pending |
| Recorded `20+` candidates | 42 | 30 high / 12 mid；六维合计已复算 |
| Earlier-week spillbacks | 6 | 按 arXiv v1 date 回拨 W21，不在 W22 重复计分 |
| Later-feed spillbacks recovered | 18 | W23 display feed 16 项 + W24 ResearchClawBench + W25 Smaller Models 已归 W22 |
| Academic discovery window | Open | HF first pass complete；cross indexes pending |
| Official / Infra discovery window | Fixed-source checkpoint passed | NVIDIA inference/security/hardware/platform and STAC workload surfaces replayed；cross-index 与 exhaustive PR absence proof 仍开放 |
| W22 forward Candidate Evidence Gate | Passed | 42/42 `20+` Full Source Reviews complete；0 blocked；0 current-review pending；1/1 low-score boundary complete；broader discovery backlog 保持 Open，forward cursor 进入 W23 |

## Deep Analysis — Telemetry 的价值与集中化风险

集中原始 traces 最容易分析，却扩大隐私、租户隔离与 insider-risk 边界；zero-trust
aggregation 尝试让平台获得 aggregate evidence，而不要求单个主体完全信任聚合者。收益是
降低原始数据暴露，代价是协议复杂度、可调试性、dropout/adversary assumptions 与有限查询
表达力。它与 Agent telemetry 是 `Layering / Dependency`，不是通用 privacy 的完整替代。

### ScientistOne：从 Run Evidence 走向 Claim-level Provenance

传统 experiment tracking 保存 run、code、score 与 log，能回答“这次执行发生了什么”；多阶段
research workflow 还要回答“最终 prose 中每条 claim 由哪个 source region、log line、score file
或 code artifact 支持”。ScientistOne 将 literature、solution search、evaluation、ablation 与 writing
之间的映射提升为 typed evidence chain：Conceive 先产生带 inline evidence tags 的中间表示，Ground
做 deterministic existence/score checks，Critic 检查 overclaim/contradiction，Resolve 修订，Compose
写正文，Claim Verifier 再按 citation/numerical/methodological/conclusion 类型核验。后验 CoE Audit
则对任何 system 的 paper/code/evaluator/bibliography 做 score reproduction、specification violation、
reference existence 与 method-code alignment。

这条路线的价值是把 provenance 变成生成前约束，而不是在成文后补引用；新增成本是 artifact
retention、claim schema、source supersession、verification latency 与 model-judge false negative。
作者在 ADRS 的 75 篇适配论文和另外六项任务上提供受限证据，但 baseline adaptation 含人为判断、
method-code alignment 仍由 LLM majority vote、false negatives 未系统界定，且 deterministic evaluator
并不代表开放科学结论。因此关系是 `Layering / Dependency`：run-level reproducibility 仍是底座，
claim-level provenance 不替代 domain expert review。

## Evidence Level

private analytics 是作者研究；coding-agent 结论绑定研究样本；biodefense 是 access-policy
事实，不证明安全风险已被消除。ScientistOne 的论文和 artifact 证明其特定 research pipeline、
ADRS adaptation 与 audit procedure；不证明“human-level autonomous research”是跨领域通用能力。
已完成候选的机制与实验边界见各自 Full Source Review；27 项旧 access blocker 已由
`Primary-Text Recovery Addendum` 恢复为全文审计，旧 blocked 段落只保留为访问历史，不再代表当前状态。
W23 feed 的展示日期不构成 event date；本轮只用
arXiv submission history 归档，没有把 leaderboard/upvote 当 evidence。

## Cross-Week Deduplication

与 OpenAI Privacy Filter 分层：filter 处理内容，zero-trust aggregation 处理统计计算与信任。
ScientistOne paper v1 为 2026-05-25，归 W22；W31 只保留 07-30 Google Research official publication
node。SkillOpt、Foundation Protocol、SciAtlas、QUEST、ThriftAttention 与 SkillEvolBench 的 v1
属于 W21，已回拨且不在 W22 重复计分。
W23 feed 的 Crafter、Domino、COLLEAGUE.SKILL、GrepSeek、TASTE、TRB、TrOPD、LongTraceRL、
dMoE、SkillAdaptor、Draft-OPD、SCOPE、Harness Updating、SAAS、RAMP 与 Masking Stale
Observations 均按 v1 归 W22；NITP v1 05-24 归 W21。

## Knowledge Tree Position

`MULTIMODAL-WORLD-MODELS` → `MODEL-MOE` / `TRAIN-LORA` / `TRAIN-GRPO` →
`INFER-SPECULATIVE-DECODING` / `INFER-VLLM` → `PLATFORM-EVALUATION-SYSTEM` /
`PLATFORM-SECURITY` → `AGENT-RAG` / `AGENT-MEMORY` / `AGENT-PLATFORM`。

## Recommended Action

W22 的 43/43 final dispositions 与 owner review 已完成；27 个旧 blocker 已恢复，不再进入材料请求。
正文吸收多主体 World State、LoRA token-level recall boundary、heterogeneous retrieval operators、Memory
counterfactual attribution、并行 draft 的 architecture/training 双分支、execution snapshot、DPU security plane、
Skill update benefit decomposition 与 simulator promotion Gate。其余 Refine 逐项复用已有具体论点，No Change/
Weekly Only 保持证据边界。下一周为 W23；Archive/Discovery cross-index recall 继续作为独立开放 Gate。

## Event-Date Daily Decision

2026-05-27、05-28、05-29：Weekly only。

## Books Integration Decision

`Complete — Source-Family Gate`。最终账本为 38 Refine、3 No Change、2 Weekly Only。每个 Refine 都已
阅读 owner 及相邻章节；只有形成长期机制或修正演进链的内容修改正文，其他 Refine 是对现有具体论点的
primary-source revalidation。Zero-trust aggregation 与 ScientistOne 为章节级 No Change；coding agents in social
sciences 与 Rosalind access policy 为 Weekly Only。性能、模型、硬件、precision、length、batch、concurrency、
SLO 或 artifact 未披露时保持 `Not Disclosed`，没有把作者/厂商结论改写成通用事实。

## Ignored Noise

把 aggregate privacy 机制写成任何 threat model 下的“零数据泄露”。

## 2026-07-31 Full Re-Audit Addendum

- Zero-Trust Aggregation 的官方材料与链接论文已复核。secure aggregation + TEE
  attestation 改变的是 raw telemetry 的 state ownership；查询受限、dropout、证明与预算
  是新成本，已写入 Ch63。
- 安全结论只在声明的 client/protocol/TEE/query threat model 下成立。social-science coding
  Agent 继续 Weekly only。

## Full Source Review

### Private analytics via zero-trust aggregation — 25/30

- **Source Family ID / Type / Date**：`ZERO-TRUST-PRIVATE-AGGREGATION`；Google Research
  2026-05-27 official report、linked cryptographic aggregation paper 与 confidential federated
  analytics/attestation material。
- **Full-read Coverage**：已覆盖 threat model、one-shot client protocol、cryptographic security、
  TEE/attestation、public code/transparency、dropout/scale assumptions、query output 和 limitations。
- **Problem / Previous Design / Changed Constraint**：中心化 raw telemetry 易诊断但扩大 exposure；
  TEE-only 可部署但受 side channel/implementation trust；传统 secure aggregation 提供数学保证，
  多轮在线要求却不适合大规模 intermittent device。
- **Mechanism / Ownership / Flow**：client 本地形成 contribution 并单消息加密提交；cryptographic
  layer 只暴露 aggregate；TEE 执行公开协议并用 attestation 证明 code identity。client 拥有 raw
  data，protocol/TEE service 拥有中间密文和 attested execution，analytics owner 只接收受限 aggregate。
- **Evidence Boundary**：论文证明声明 adversary/dropout/query contract 下的 protocol security 与
  efficiency；不证明 endpoint 无恶意数据、TEE 无 side channel、aggregate 无 membership inference、
  differential privacy 自动成立或任意查询可安全开放。
- **Trade-offs / Evolution**：one-shot 降低在线性和单点信任，增加 protocol complexity、attestation/
  key lifecycle、受限 debug 与 query expressiveness；per-session detail 在 incident response 仍可能
  必需。关系为 `Layering / Dependency`。
- **ROADMAP / Chapters / Decision**：Ch63 主 owner，已读 Ch62～64、Ch67～68、Ch80；`Refine —
  Existing Argument`，补入 redaction、aggregation 与 Evaluation 的 owner handoff。

### Coding agents in social sciences — 22/30

- **Source / Coverage**：Anthropic 2026-05-27 research report；已核对 sample、task taxonomy、
  collaboration/verification method 和 limitations。
- **Evidence / Decision**：说明样本中 coding Agent 如何进入社会科学 workflow，不证明跨学科
  causal productivity 或模型独立完成 research。Ch62/69/77 已读；`No Change — Already Covered`。

### Rosalind Biodefense access expansion — 19/30

- **Source / Verification**：OpenAI 2026-05-29 access/governance release 已核对；属于 eligibility、
  trusted access 与 deployment policy 状态，非新模型/runtime 机制。
- **Score / Decision**：19/30 维持；`Weekly Only — Version/Product Fact`。

### ScientistOne / Chain-of-Evidence — 28/30

- **Candidate / Week / Source Family**：`SCIENTISTONE-CHAIN-OF-EVIDENCE`；W22；
  arXiv:2605.26340v1，2026-05-25。Google Research 2026-07-30 article 是同一 family 的官方
  explanation，属于 W31 publication node，不倒写成 W22 已公开事实。
- **Direct / Related Primary Sources**：arXiv metadata、709-line HTML/PDF 全文与 Appendices A～E、
  project artifact；7 月 Google Research explanation 只用于机制交叉核验。现有 Ch62 写入与 W31
  Full Source Review 也已反向检查其来源边界。
- **Access / Full-read Coverage**：已覆盖 Introduction、Related Work、CoE standard、Problem
  Investigator、Parallel Explore-Exploit、Paper Writer/Claim Verifier、四项 Integrity Audit、75-paper
  ADRS experiment、baseline adaptation、native claim provenance、review/solver results、MLE-Bench/
  Parameter Golf generalization、Conclusion、Limitations，以及 Appendix 的 failure cases、完整 system
  prompts/implementation、search scaling、audit reproducibility/human verification 和 per-metric failures。
- **Original Problem / Previous Design / Changed Constraint**：run-level experiment tracking 和最终
  paper review 在短 pipeline、人工作者能维持上下文时合理；长 research Agent 会让 literature summary、
  hypothesis、code、score 与 prose 连续变换，同一早期错误可在后续各阶段保持“内部一致”而脱离原始
  evidence。专业写作质量和最终 leaderboard score 因而不再能证明 claim integrity。
- **Mechanism / Ownership / Flow**：CoE 定义 citation、numerical、methodological、conclusion 四类
  claim 的 evidence-chain shape。PI 经 scholarly APIs 建 citation graph 并读取全文；PEE 分支执行
  evaluator、保存 code/log/ablation；Writer 先生成带 source tag 的 representation，经 deterministic
  Ground、LLM Critic、Resolve、Compose；Claim Verifier 再按 claim type 对 log、bibliography、method
  artifact 核验，blocking violation 清零后才发布。Evidence plane 持有 artifact identity/verdict；
  workflow 持有 stage/branch/promotion；writer 不拥有事实真值。
- **Implementation Details**：post-hoc adapter 把五套系统的 `paper.tex / solution code / references.bib`
  正规化。I1 在 golden evaluator 上重跑并按 `max(1%, 3σ/|mean|)` tolerance 对分数；I2 用多次 LLM
  vote 检查 task-spec exploit；I3 联查 Semantic Scholar、arXiv、OpenAlex、Crossref 并消歧；I4 对 method
  与 code 做 majority-vote alignment。Native numerical CPR 只有保存 write-time provenance 的系统可算。
- **Evaluation Contract / Evidence Boundary**：主审计是 5 systems×5 ADRS tasks×3 seeds=75 papers，
  task 含 Prism、Cloudcast、EPLB、LLM-SQL、TXN，每个 baseline 均需人工适配；evaluator 每项重跑
  五次。作者 headline 只证明这些 artifacts、adapters、models 和 judges 下的 integrity/solution results；
  它不证明跨科学领域的人类水平，不证明 CoE 覆盖 novelty、causal validity 或理论正确性，也不把
  automated review 当 peer review。
- **Baselines / Ablations / Threats**：论文比较四个 open research systems 并报告 audit failure shape、
  native provenance、search-budget behavior 和另外六项任务；但公平性受 adaptation choices 影响，
  reference check 主要验证 existence 而非 support，method-code judge 会漏错，false-negative rate 未被
  系统测量，ADRS 的确定性 evaluator 使证据链比开放实验科学更容易建立。
- **Trade-offs / New Failure Modes**：claim-level trace 增加 schema/storage/source retention、audit cost、
  verification latency、artifact permissions、supersession 和 redaction；模型 judge 仍可能错，严格要求
  每句 source 也可能压制必要推断。后验 audit 能发现已编码 taxonomy 的断链，不能恢复从未保存的
  state，也不能自动判定科学价值。
- **Where Previous Design Still Applies / Evolution**：短、人工监督强或 artifact 很少的研究仍可用
  conventional run tracking + expert review。演进为 `run/artifact retention → reproducible execution →
  typed claim provenance → pre-publication integrity gate → domain expert review`，是 `Layering /
  Dependency`，不是以后者覆盖前者。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch61～63 与 Ch77 邻接边界。Ch62 主 owner，已
  吸收 run→claim provenance、typed verifier 和 evidence-before-prose；Ch77 只拥有 durable stage 与
  promotion，Ch61/63 分别负责 lineage/telemetry。W22 不重复写入正文。
- **Integration Decision / Files / Open Questions**：`No Change — Already Covered by verified W31
  integration`；现有 `books/part-06-ai-infrastructure/66-evaluation-system.md` 保留。待验证：audit false
  negative 如何测量；source revision/supersession 如何传播到已发表 claim；敏感/专有 artifact 如何在
  provenance 与最小披露间折中；非 deterministic science 如何定义可接受 evidence chain。

### Gamma-World — 25/30

- **Candidate / Week / Score / Source Family**：Gamma-World: Generative Multi-Agent World Modeling Beyond
  Two Players；W22；25/30；`GAMMA-WORLD-MULTI-AGENT-VIDEO-WORLD-MODEL`。arXiv:2605.28816v1
  submitted 2026-05-27 17:59:31 UTC，当前仅 v1；project page 05-28 发布。Direct primary sources 为
  21-page v1 PDF、NVIDIA project page 与 official `nv-tlabs/Gamma-World` repository。完整 code/training
  pipeline 于 06-16 后发，作为 related artifact 核验实现，不倒写成 W22 event-time 已公开状态。
- **Access / Full-read Coverage**：已读 Abstract、Introduction、Related Work、完整 Method/公式、teacher/
  causal/distillation flow、Experiments、Discussion/Limitations、Appendix A～F、simplex proof、action schema、
  implementation/training settings、stage/hub ablations与 references；并核对 current codebase 的三种 model
  mode、checkpoint conversion、data contract、training launcher、KV-cached inference 与 Apache-2.0 license。
  已读 Ch10 及 Ch13/14/40 handoff；Ch78 只讨论语言/工具 Agent responsibility，不把同名 multi-agent
  机制混写。训练 dataset size/provenance/license、batch size、precision、seed/variance/CI、24-FPS 测量
  hardware 与端到端 latency 分解未披露。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint**：single-agent video world model
  或把多个视角做 spatial/frame concat，在 agent 数少、slot 固定、离线全上下文 generation 时实现简单；dense
  cross-agent attention 也能保留任意 pair interaction。约束变化是多个主体同时作用于同一世界：每个 action
  stream 要独立可控，视角必须互相一致，主体标签不应因输入 slot 获得特权，且 interaction cost 不能随 agent
  数平方增长。实时 rollout 又要求 future 不可见、能复用 history state，并承受 own-generation exposure。
- **Mechanism — Identity / Communication / Generation**：clean latent 显式加入 agent axis
  `[P,T,H,W,Cz]`；shared action encoder 将每主体 action 作为 per-layer/per-frame bias 注入。Simplex Rotary
  Agent Encoding 从 temporal low-frequency band 划出 agent band，将候选主体映射到 regular simplex vertices，
  训练时随机选择/排列 vertices，使 pairwise distance 对称且不依赖 slot。Sparse Hub Attention 禁止 agent 间
  direct attention：agent 只读自身 stream 与 hub，hub 读所有 agent/hub，形成 `agent -> hub -> agent` 两跳；
  固定 block/spatial/hub size 时 cross-agent cost 对 `P` 线性，而不是 dense path 的平方。
- **State Ownership / Control Flow / Data Flow**：per-agent observation/action stream 拥有局部 temporal state；
  learnable hub tokens 拥有 shared communication bottleneck；student runtime 分别持有每个 agent 的 KV Cache
  与共享 hub KV Cache。新 block 中 agent 只读自己的 past 与 hub history，hub 读取所有 agent/hub history。
  agent-to-simplex assignment、active count、action alignment、block generation、hub capacity 与 cache generation
  必须属于同一 rollout identity，否则可能发生 identity swap、cross-view contamination 或 stale shared state。
- **Training / Implementation Contract**：基于 Cosmos-Predict2.5-2B，hidden 2048、28 blocks、16 heads、head
  dim 128、MLP ratio 4、AdaLN-LoRA rank 256；RoPE bands 为 `(64,32,16,16)` 对应 `(t,p,h,w)`，simplex
  pool 4、training runtime slots 2，图像每 view 320×480。训练三阶段：32×GB200 上 bidirectional teacher
  93-frame 10k iterations + 189-frame 6k；32×GB200 causal multi-step student 93-frame 15k；再以 frozen
  teacher/real score、trainable fake score、DMD/self-rollout 做 400-iteration four-step distillation。current artifact
  发布 three checkpoint modes；released data loader 需要 per-view frames 与 frame-aligned action，默认 mock data
  不能当作论文训练数据。
- **Streaming Contract**：few-step student 每 block 使用 denoising timesteps `{1000,750,500,250}`，生成后以
  context-noise 128 re-forward 并写入 KV；rolling local window 为每 view 24 latent frames。current inference
  文档默认 189 frames、320×480、seed 1，并称 single 80GB GPU 可运行 four-step mode。论文 headline
  `24 FPS` 没有披露测量 GPU、batch、并发、frame-to-display buffering、action-to-frame latency、P50/P99 或
  长 rollout SLO，不能与 32×GB200 training contract 混为一谈。
- **Evaluation / Baselines / Ablations**：Minecraft main setting 比较 frame concat 与 Solaris，在 Memory/
  Grounding/Movement/Building/Consistency 上报告 FVD/FID；architecture ablation 比 spatial concat、sequence
  concat、learned view embedding、simplex/full attention 与 simplex/hub，并报告 FVD/FID/LPIPS/PSNR/SSIM。
  2/4/8-agent efficiency 用 full KV Cache 的 24-latent-frame rollout，latency 仅平均 3 次；analytical attention
  FLOPs 与 measured DiT/attention latency分列。stage ablation 显示 bidirectional quality 最好、causal 下降、
  distilled 部分恢复；hub `K=1/8/32/128` 呈 diminishing returns。four-agent zero-shot 与 bimanual robot
  主要为 qualitative figures，没有 task-success/intervention/physics-control metric。
- **What the Evidence Proves**：在作者的 Cosmos-derived two-player Minecraft training 与所列 test scenarios
  内，随机 simplex assignment、hub attention 与 causal distillation 能组成可运行的多视角 rollout branch；
  architecture/hub/stage ablations 支持 identity、communication capacity 与 causality-quality 是不同设计轴。
  后发 artifact 也证明三阶段代码/checkpoint/data interface 存在。证据支持“共享世界中的主体 identity、共享
  state、causal rollout 必须联合设计”，不支持更宽泛自治或物理理解结论。
- **What It Does Not Prove / Threats to Validity**：不证明从 2 到任意 `P` 的 quality 可扩展；simplex pool
  受固定 RoPE band/pool size 限制，8-agent只测 compute，不是 generation quality。FVD/FID 与 pixel metrics
  不证明 action causality、shared 3D state 或 control safety；“tracks shared latent world state”来自定性观察。
  未披露 dataset volume/provenance、batch/precision、seed/CI、held-out split 与 contamination；没有
  physics constraint，long rollout 会积累 inconsistency。post-event code 也无 W22 immutable tag，current behavior
  不能全部反推为 paper-day implementation。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：dense attention 在 agent 少、pairwise
  detail 关键时保留最短信息路径；fixed slot embedding 在 roster 固定且身份语义稳定时简单；bidirectional
  teacher 在 offline quality-first 场景合理。simplex identity 换取 exchangeability，却受 band/pool 容量约束；
  hub 将平方 interaction 压到 compact state，却可能丢失 pair-specific detail并形成 bottleneck/single shared-state
  failure；causal KV streaming 换取 responsiveness，承担 exposure bias、cache invalidation、identity reset、
  rolling-window forgetting 与 teacher-student quality gap。
- **Evolution Relationship**：`Layering / Dependency`：`single-view rollout -> concatenated multi-view ->
  slot-identified dense interaction -> exchangeable agent-axis identity + hub shared state -> bidirectional teacher ->
  block-causal multi-step student -> self-rollout few-step cached student -> future hierarchy/physics/intervention-aware
  multi-agent world model`。各旧分支仍按 roster、quality、latency 与 interaction-density 条件共存。
- **ROADMAP / Chapters / Existing Coverage**：Ch10 是主 owner，已覆盖 action-conditioned world prediction、
  video realism≠causal correctness、sim-to-real 与 long-horizon failure，却缺少 multi-observer shared-state 的
  identity/communication/causality 分解。Ch13 只承接 simplex RoPE 作为“额外语义轴”的受限例子；Ch14 承接
  sparse hub mask 与 bottleneck；Ch40 承接 causal block/KV streaming。Ch78 的 language-agent delegation 与本
  方法只属 `Explanatory Analogy`，不接收正文机制。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`，
  owner Ch10，Ch13/14/40 short handoff；Historical Books Gate 关闭，本轮不修改 Books。待验证 dataset manifest/
  split/license、multi-seed/CI、matched-compute dense/hub comparison、4/8+ agent quantitative quality、action
  intervention 与 cross-view state checker、long-horizon/physics consistency、full 24-FPS latency/SLO、cache
  reset/failure semantics、large-population hierarchical grouping 与 immutable event-time artifact。

### AgentDoG 1.5 — 25/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`AGENTDOG-1-5-AGENT-SAFETY-GUARDRAIL`；W22；
  arXiv:2605.29801v1，submitted/first-public 2026-05-28 11:48:37 UTC，当前仅 v1；arXiv 标记
  44 pages、12 figures、9 tables。
- **Verified Access / Related Evidence**：已核验 metadata、authors、submission history、abstract 与 PDF/HTML
  primary-text surface。摘要声明扩展 agent-safety taxonomy、taxonomy-guided data engine、influence-function
  purification、0.8B/2B/4B/8B variants、约 1K samples、Docker training environment 与 online guardrail，
  但这些仍是作者摘要主张。W08 的 OpenClaw trajectory-audit source family 只将 AgentDoG-Qwen3-4B 用作
  binary judge；它不是 AgentDoG 1.5 的 training、guardrail、benchmark 或 deployment evidence，不能替代本篇。
- **Access Boundary / Missing Full-read Coverage**：完整 44 页 HTML/PDF 通过当前允许路径不可读，因此 Method、
  taxonomy definitions、purification objective/influence approximation、data provenance、SFT/RL environment、
  online moderation control flow、threshold/calibration、baselines、ablation、latency/throughput、bypass/adaptive
  attack、false-positive utility、hardware/model/precision/length/batch/concurrency/SLO、Limitations、Appendix 以及
  model/data artifact identity 均未完成 primary-source verification。
- **Evidence Boundary / Disposition**：25/30 只保留为 discovery-stage priority，尚未通过内容与评分复算；
  不把 “comparable to GPT-5.4”、“two orders of magnitude” 或 “state of the art” 写成实验事实，也不由摘要
  反推 guardrail state ownership、inline/blocking semantics、fail-open/fail-closed、rollback 或 production safety。
  标记 `Unverified / Blocked Backlog`，不计 Full Source Review、不指定 Books owner、不修改 Books，且按用户决定
  不阻塞 W22 forward cursor；W30 forward sweep 后优先恢复全文、模型卡、数据卡与可执行 artifact 联读。

### DVAO — 25/30

- **Candidate / Week / Source Family**：`DVAO-MULTI-REWARD-GRPO`；W22；DVAO: Dynamic
  Variance-adaptive Advantage Optimization for Multi-reward Reinforcement Learning；arXiv:2605.25604v1，
  2026-05-25 08:55:16 UTC，当前仅 v1，CC BY 4.0。
- **Direct / Related Primary Sources / Access**：arXiv metadata、16-page PDF 与 392-line HTML 全文；已覆盖
  Introduction、Preliminaries、Method、Propositions 1～3、math/tool-use evaluation、training dynamics、Pareto
  sweep、Related Work、Conclusion、Appendix A～C proofs、Appendix D implementation 与 Appendix E limitations。
  页面没有链接作者 official code/model artifact；DBLP 只用于 publication identity cross-check，不替代正文。
- **Original Problem / Previous Design / Changed Constraint**：single-reward GRPO 用同 prompt group normalization
  获得 sample-relative baseline；当 deployment 同时要求 correctness、length、format 或 safety 时，需要组合多个
  reward。Raw Reward Combination 先按固定 `w_k` 合成 reward 再标准化，简单且在 reward 已校准、业务优先级稳定时
  合理，但 reward scale/correlation 会共同改变 denominator 与 update。Advantage Combination 先逐目标标准化再按
  固定权重合成，隔离 scale、便于控制优先级，却把 reward interaction 留在 normalization 之外。约束变化是目标间
  learning signal 随 policy 和 task 动态变化，固定 scalarization 可能让一个目标长期压过另一个。
- **Mechanism / State Ownership**：对 prompt `x_i` 的 `G` 个 rollouts，先为每个 objective `k` 保存 reward vector、
  group mean `mu_k`、std `sigma_k` 与 normalized advantage `A_k`；再把基础权重变成
  `w_tilde_k = w_k sigma_k / sum_l(w_l sigma_l)`，并计算
  `A_DVAO = sum_k(w_tilde_k A_k)`。rollout worker 拥有 version-pinned response/logprob；reward service 拥有每个
  objective 的 raw score 与 verifier version；advantage builder 必须在同 prompt、同 policy snapshot、同完整 group
  上原子计算统计；trainer 只消费带 group/reward/version identity 的 combined advantage。缺样本、超时或 reward
  service drift 会改变分母，不能静默把残缺 group 当完整 group。
- **Control Flow / Data Flow / Implementation**：`prompt -> G on-policy rollouts -> K reward functions -> per-objective
  group normalization -> variance-weight update -> combined sequence advantage -> token-level clipped GRPO update`。
  数学训练用 DAPO-MATH-17K；tool-use training 由 ToolACE 2K、Hammer 1K、xLAM 1K 组成。accuracy+length
  (`length <= 4,000`) 与 accuracy+format 都是 binary dual rewards；基于 `verl`，AdamW constant LR `1e-6`，
  prompt batch 128、`G=16`、500 steps、max generation 8,192 tokens，evaluation temperature 0.6、top-p 0.95，
  math 报 avg@16；单服务器 8×NVIDIA H20-3e + Intel Xeon Platinum 8575C。precision、distributed layout、
  checkpoint selection、token/s throughput 与 wall-clock/energy 均 `Not Disclosed`。
- **Theory Boundary**：Proposition 1 比较的是 group-normalized RC 与 fixed-weight AC 的组内平均平方 advantage；
  Proposition 2 证明在分母非退化且给定同一 group/base weights 时，`|A_DVAO| <= |A_sum|`；Proposition 3
  给出 raw reward sensitivity 中的 `A_DVAO*A_k` cross-term。它们说明相对 magnitude/sensitivity 结构，不证明
  policy gradient 在 clipping、importance ratio、token reduction 和 optimizer dynamics 后具有全局收敛或绝对小
  方差；`sigma_k=0`、数值 epsilon 与 incomplete group 的实现语义没有完整给出。DVAO 使用 marginal variance，
  不是显式估计完整 reward covariance，也仍保留基础 `w_k`，所以 “hyperparameter-free” 只可理解为无需额外固定
  dynamic-weight schedule，不能理解为产品价值权重消失。
- **Evaluation / Baselines / Sensitivity**：math 使用 Qwen3-4B/8B Base，在 AIME-2024/2025、MATH500、
  OlympiadBench、AMC23 比 accuracy 与 length compliance；tool use 使用 Qwen2.5-3B/7B Instruct，在 BFCL-v4
  Live/Non-Live/Multi-Turn 比 correctness 与 format。baselines 为 base、single-reward GRPO、RC、AC、GDPO；
  Pareto sweep 仅在 Qwen3-4B math 与 Qwen2.5-3B tool-use 上取基础 accuracy weight `{0.1,0.3,0.5,0.7,0.9}`。
  training curves 用 centered moving average 15。论文没有 `G` sensitivity、variance-estimator ablation、noisy/high-
  variance adversarial reward、reward-scale/correlation control、三目标以上实验、multi-seed/CI 或 independent reproduction。
- **What the Evidence Proves / Does Not Prove**：作者 contract 下，DVAO checkpoints 在四个模型尺度的两个双目标
  families 上报告更好的 accuracy-compliance trade-off，并在受限 Pareto sweep 中保持优势；这支持“group statistics
  可成为动态 reward-combination state”。它不证明任意 reward 数量、连续/learned/noisy reward、小 `G`、异步 rollout、
  non-stationary verifier 或生产 Agent 环境稳定，也不证明 variance 等于 useful signal。论文自己指出 `G<=4` 时估计
  可能噪声化、实验只有 dual objectives，且坏 reward 的高 variance 会被错误放大。
- **Trade-offs / Previous Designs Still Apply / Failure Modes**：RC 在 reward 单位已校准、强耦合且希望组合后统一
  标准化时最简单；AC/GDPO 在目标隔离、静态业务权重与可预测调参更重要时仍合理。DVAO 用额外 group-level reward
  state 换取动态 adaptation，却新增 small-group estimation noise、binary reward saturation、high-variance bad-reward
  amplification、group member dropout、reward-version skew 与 batch-to-batch weight jitter。moving average/cross-batch
  state 可缓解小 group，又引入 staleness、warmup、checkpoint/rollback state。无论哪种方法，Pareto priority 仍是
  产品/治理决策，不能交给经验方差自动决定。
- **Evolution Relationship**：`Direct Evolution`：`single-reward GRPO -> raw Reward Combination -> per-objective
  Advantage Combination/GDPO -> group-wise variance-adaptive combination -> future covariance-aware or history-
  stabilized multi-objective control`。后三者按 reward calibration、objective coupling、group size 与 policy/SLO 共存，
  不是后者单向覆盖前者。
- **ROADMAP / Chapters / Existing Coverage**：主 owner Ch29，已读 Ch28～30。Ch29 已覆盖 group size、reward scale、
  noisy measurement、verifier contract 与 zero-advantage groups，却缺少 multi-reward scalarization 的完整设计分支。
  Ch28 只承接 advantage/clip 的共同底座，Ch30 只说明离线 preference 路线不承担 on-policy multi-reward group state。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental` / Ch29；
  Historical Books Gate 关闭，本轮不修改 Books。待核验 code/artifact、zero-variance epsilon、dropped rollout semantics、
  `G=4/8/16/32` 与 reward-noise sensitivity、三目标以上和 learned rewards、multi-seed/CI、matched-compute overhead、
  weight jitter/EMA、异步 reward versioning、训练 wall-clock/precision/checkpoint selection 与 independent reproduction。

### OmniRetrieval — 24/30

- **Candidate / Week / Source Family**：`OMNIRETRIEVAL-HETEROGENEOUS-NATIVE-SOURCE-FEDERATION`；W22；
  OmniRetrieval: Unified Retrieval over Heterogeneous Knowledge Bases；arXiv:2605.29250v1，submitted/
  first-public 2026-05-28 02:10:35 UTC，当前仅 v1，21 pages。
- **Direct / Related Primary Sources / Access**：已读 arXiv metadata、HTML/PDF 全文的 Introduction、Related Work、
  Method、dataset construction、main/ablation/scale/cost experiments、Implementation、Limitations、Conclusion 与
  Appendix；并核验作者 official repository、entrypoint、evaluation path 与 `src/model/retrieval.py` 当前实现。
  repository 当前只有少量 commits、没有 event-time immutable release/tag，且默认 model identifiers 已相对论文漂移，
  因此 code 只作为后发机制交叉核验，不倒写成 W22 精确 artifact identity。
- **Original Problem / Previous Design / Changed Constraint**：lexical/dense retrieval 在单一或同构 corpus 上共享
  representation，索引简单、吞吐和 fusion contract 清晰；把 SQL tables、RDF ontology、property graph 与 text 全部
  扁平化进 embedding 也便于统一服务。但 join、path traversal、schema constraint 与 graph neighborhood 是 native
  operators，扁平化会丢结构语义。只 route 到一个 backend 可控制成本与攻击面，却在 source identity 不确定时提前
  丢失正确 evidence。约束变化是 query 可能来自多种结构化/非结构化 source，而 catalog 仍需统一发现接口。
- **Mechanism / State Ownership**：系统先把每个 source 注册为带 ID、type、description 与 schema/ontology/corpus
  context 的 catalog descriptor；shared LLM 在完整 catalog 上选择最多 `k` 个 sources，然后针对每个 source 生成
  native query，交给对应 engine 执行；execution result 被 verbalize 后，再由 evidence selector 选出最佳候选。
  durable control plane 应拥有 source identity、adapter/schema version、principal/ACL、freshness snapshot 与 query budget；
  per-request runtime 拥有 route decision、generated query、execution status/result、truncation record 与 selection decision。
  论文和当前 code 的 typed state 只显式覆盖 route/query/result/candidate，未覆盖 ACL、freshness/version 或 policy decision。
- **Control Flow / Data Flow / Implementation**：`question -> full-catalog source selection -> top-k source descriptors ->
  per-source native query generation -> search/SQLite SQL/Wikidata SPARQL/Neo4j Cypher execution -> verbalized candidate
  results -> LLM evidence selection -> answer`。当前 artifact 使用 BEIR dense retrieval（MiniLM + hypothetical passage）、
  SQLite、remote Wikidata SPARQL 与 Neo4j；selector 前只保留受限 preview，search 取前五条且截短文本，structured
  results 最多取前一百项。这种 late selection 保留 native operators，却也让 truncation、serialization 与 selector
  成为新的 evidence-loss boundary。无效 selector output 当前回退 candidate 0，不是可验证的 fail-closed policy。
- **Evaluation Contract**：13 datasets、309 KBs、每 dataset 300 questions：7 个 BEIR corpora、Spider 206 + BIRD 80
  个 SQL DBs、一个 Wikidata RDF KB 与 Text2Cypher 15 个 Neo4j graphs。比较四个 single-backend、single-source
  KB Routing、默认 top-3 OmniRetrieval 与 gold-source Oracle；统一表示只在受限 materialization subset 上作 feasibility
  comparison，论文明确不可与主表等价比较。五个 backbones 为 GPT-5.4、Gemini-3.1 Pro、Sonnet-4.6、Qwen3.5-27B、
  Gemma4-31B；closed models 经 API，open models 用单张 NVIDIA H200 + vLLM，temperature 0、max output 1,024。
  retrieval 对 text 报 NDCG@10、structured sources 报 Execution Match，最终结果用 GPT-5.4-mini judge，并对四类 source
  macro-average。没有 model/API snapshot、precision、batch、concurrency、latency/cost/SLO、multi-run/CI 或 human-judge
  calibration。
- **What the Evidence Proves / Does Not Prove**：在该 13-dataset、single-gold-source contract 下，top-k native-source
  federation 比 single-route baseline 报告更高平均 source selection、retrieval 与 judge score；`k={1,3,5,10}` 显示
  candidate breadth 增加 recall/quality 机会，也近似线性增加 generation/execution/selection cost，且 gold source 已在
  candidate set 时 selector accuracy 从 `k=3` 的 67.5% 降到 `k=10` 的 62.8%。backbone scale study 还表明小模型
  可能发生 source-diversity collapse。这支持“source identity + native operator + late selection”作为 federation design
  point，不证明跨源 join/composition、生产 source scale、动态更新、tenant isolation 或 universal unified retrieval；每题
  只有一个 gold source，selector 也只返回一个 best candidate。
- **Trade-offs / Previous Designs Still Apply / Failure Modes**：同构文档、稳定 embedding 与高吞吐 SLO 下，统一向量
  index 仍更简单；目标 source 高置信时 single routing 可减少 cost、latency 与 attack surface；结构操作主导时 native
  federation 才值得新增 adapter 和 selector。新 failure modes 包括 catalog/context overflow、schema drift、错误 native
  query、remote timeout/partial success、expensive query、credential/ACL leakage、stale snapshot、result truncation、
  serialization loss、selector bias 与 fallback-to-first。read-only query 仍可能泄露数据或耗尽资源，必须由 Ch74 的可信
  executor 做 typed validation、authorization、resource budget、timeout、redaction 与 provenance，而不是让 LLM 直接执行。
- **Evolution Relationship**：`Direct Evolution / Layering`：`single-corpus lexical/dense retrieval -> homogeneous multi-index
  fusion -> shared-representation flattening -> single native-source routing -> multi-candidate native execution + late evidence
  selection -> future policy/version/ACL-aware federated retrieval with typed provenance and cross-source composition`。各节点按
  source homogeneity、structural operator、catalog size、security boundary 与 latency/cost SLO 共存，不是后者覆盖前者。
- **ROADMAP / Chapters / Existing Coverage**：主 owner Ch72，已读 Ch71、Ch72、Ch74；Ch72 已覆盖 ingestion/index
  identity、ACL、authorized retrieval、fusion/rerank、provenance、freshness、conflict、budget 与 agentic retrieval，但缺少
  heterogeneous native-source federation 的 control/data-plane 演进。Ch71 只接收已授权且带 provenance 的 selected
  evidence，Ch74 负责 native query 的 typed/authorized execution 与 failure semantics；Planning/Memory/MCP 不重复拥有。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental` / Ch72；
  Historical Books Gate 关闭，本轮不修改 Books。待验证 cross-source joint-answer benchmark、catalog scale/context cost、
  schema/source revision、freshness/delete、tenant ACL/credential boundary、read-only/resource policy、timeout/retry/partial
  failure、snapshot/provenance identity、truncation sensitivity、independent human-judge calibration、latency/cost/concurrency/
  SLO 与 immutable artifact release。

### MobileGym — 27/30

- **Candidate / Week / Source Family**：`MOBILEGYM-STRUCTURED-STATE-VERIFIABLE-GUI-ENVIRONMENT`；W22；
  MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research；arXiv:2605.26114；
  v1 2026-05-25 17:59:49 UTC，v2 2026-05-27 05:27:30 UTC，二者均在 W22，first-public identity 取 v1、
  technical review 以 v2 当前 revision 核验。
- **Direct / Related Primary Sources / Access**：已读 v1/v2 metadata、HTML/PDF 的 Abstract、Introduction、Related
  Work、platform/state/task design、benchmark protocol、GRPO/Sim-to-Real/efficiency experiments、Limitations、Ethics、
  Conclusion 与 Appendices A～N；并核验 official project 和 repository 的 benchmark/state/app/task contracts。
  repository 的首个 stable `v0.1.0` 与 RL code 发布于 06-27，是 post-event related artifact，不倒写为 W22 已发布状态。
- **Original Problem / Previous Design / Changed Constraint**：真实设备最贴近 deployment，适合最终验证；Android
  emulator 能复现 system/open-source apps，也保留真实 OS 行为。但 everyday app 的关键 state 藏在 proprietary backend、
  cache 与 live account 中，难以读取、初始化、reset 或 fork，动作还可能真实发信、付款或删号；grouped online RL 又要求
  从同一 initial state 并行采样。约束变化不是“需要更像手机的 UI”，而是训练和评测需要可写、可复制、可比较且无真实
  副作用的 authoritative environment state。
- **Mechanism / State Ownership**：MobileGym 把 environment 拆为 read-mostly World Data、per-instance Runtime
  Overlay 与 OS Runtime；agent 只通过 screenshot/17-action interface 交互，benchmark owner 则可将 structured JSON
  configure、serialize、restore、fork 和 diff。declarative EFSM 同时驱动 navigation、guard/update semantics、静态检查与
  trajectory enumeration；task template 拥有 setup injection、typed goal checks 与 AnswerSheet matchers。因而 environment
  revision、world-data digest、runtime snapshot、task/judge/reward version、agent/action adapter、seed/parameter instance 和
  rollout policy 必须共同定义一次 run，不能只记录 model name。
- **Control Flow / Data Flow / Implementation**：`task template + sampled parameters -> initial JSON snapshot -> N identical
  browser instances -> screenshot-only policy observation -> normalized actions through Playwright -> EFSM/runtime state transition
  -> deterministic goal/progress/side-effect checks -> terminal metrics or shaped reward -> reset/fork next rollouts`。每个 app
  以 manifest、React entry、Zustand state、navigation declaration 与 replaceable defaults 分层；full-environment initial/final
  diff 捕获 goal 之外的 mutation。AnswerSheet 把 query result 变成 typed GUI fields，避免 free-text matcher 把 reasoning 中
  偶然出现的答案判为成功；它也新增 app-switch/fill cost，因此单独增加 15-step budget。
- **Evaluation / Training Contract**：MobileGym-Bench 有 416 parameterized templates（160 train、256 test，声明严格
  disjoint）、28 apps；test 中 36% 为 cross-app，step budgets 为 15/30/45/60，AnswerSheet 再加 15。九个 agents 中 open
  models 重采样四次，两个 proprietary rows 是 single run，Gemini 额外重复一次；结果同时报告 SR、PR、False Complete、
  Overdue Termination 与 Unexpected Side Effects。GRPO 使用 Qwen3-VL-4B-Instruct、3×RTX Pro 6000、96 browser instances、
  group 8、batch 12、10 steps、LR `1e-6`、KL 0.01、asymmetric clip 0.2/0.28、max prompt 32,768、response 1,024，reward
  由 progress 加 AnswerSheet/side-effect/false-complete/termination penalties 构成。环境每 action 固定等待 0.8s。
- **What the Evidence Proves / Does Not Prove**：在作者 surrogate/test contract 下，structured state 能让 reset/fork、
  programmatic success/progress 与 off-target mutation detection 共用一个 control-plane primitive，并支撑单节点 96-way
  online RL。作者报告 256-task simulation SR `9.4% -> 22.2%`；real-device study 只选择 simulation 中出现 uplift/mid/
  stable-pass signal 的可安全等价 59 项，另抽 15/189 stable-fail 作 negative control，在 Redmi Note 12 Turbo 上报告
  `32.2% -> 72.9%`。论文自己称其为 existence proof；outcome-stratified selection、single-device pass@1、十个 training
  steps 与人工恢复状态不证明全 256 tasks、其他 devices/apps/backends 或长期 policy 都保持 95.1% gain。
- **Judge / Efficiency Boundary**：作者人工审计 118 条 signal-subset real-device trajectories，Qwen3.6-Plus 与 GPT-5.4
  各误判 12 条但实例部分不同；这证明该保存轨迹上的 model-judge error，不证明 deterministic judge 自动无错。项目对
  416 released task checks 报告零 false accept/reject，但 judge 与 simulator 共享作者 specification，可能共同遗漏合法替代
  路径或 backend-only side effect。`~400 MB`/instance、`~3 s` cold start、256 instances `<10% CPU`/`~100 GB RAM`/
  `~6 min` 是特定 server/browser/headless contract；与 AndroidWorld 的资源比较受 Docker/no-KVM 配置影响，不能外推为
  所有 emulator 或 model-serving bottleneck。
- **Trade-offs / Previous Designs Still Apply / Failure Modes**：real device 仍是最终 backend/app/version/permission/latency
  fidelity 的 owner；emulator 适合真实 OS/system-app behavior；trajectory replay 适合低成本 deterministic regression；
  lightweight surrogate 适合大量 resettable rollout。MobileGym 用 interaction fidelity 和 controllability 换取 backend、
  stochastic service、fraud/policy check、real-time feed、animation/icon 与长尾 feature fidelity，新增 simulator-reward
  co-bug、task/judge overfitting、state-schema drift、world/runtime overlay omission、snapshot isolation、parallel resource
  interference、synthetic-content bias 与 Sim-to-Real selection bias。deterministic 只说明同一 specification 可重复执行，
  不说明 specification 完整或与生产 outcome 等价。
- **Evolution Relationship**：`Direct Evolution / Layering`：`real-device outcome + manual/model judge -> emulator + external
  programmatic checks -> app/backend hooks -> lightweight trajectory replay/surrogate -> authoritative structured state shared by
  reset/fork/judge/reward -> future stochastic/fault-injected surrogate + real-device shadow/canary calibration`。这些路线按
  fidelity、reproducibility、cost、safety 与 rollout scale 共存；受控 simulator 不是 real-device evidence 的替代品。
- **ROADMAP / Chapters / Existing Coverage**：主 owner Ch62，已读 Ch61～63，并复核 Ch29/80 handoff。Ch62 已覆盖
  subject/environment identity、executable verifier/simulator、trajectory/action/outcome/side-effect evidence、scorer audit 与
  offline→online progression，却尚未把 `authoritative state -> reset/fork -> judge/reward` 作为同一 evaluation-environment
  control plane 展开。Ch61 只拥有 rollout compute placement，Ch63 只聚合 health signals；Ch29 负责 grouped reward/
  policy update，Ch80 负责 Agent run/environment revision 与 sandbox rollout，不重复评价 benchmark validity。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental` / Ch62；
  Historical Books Gate 关闭，本轮不修改 Books。待验证 v1→v2 exact change log、event-time code commit、task/judge mutation
  testing、alternative-path false rejection、state-schema/snapshot consistency、parallel nondeterminism、full 256-task multi-device
  transfer、backend/fault injection、longer/multi-seed RL、held-out authoring contamination、inference-side compute/latency/cost 与
  independent reproduction。

### Self-Improving LMs with Bidirectional Evolutionary Search — 26/30

- **Candidate / Week / Source Family**：`BIDIRECTIONAL-EVOLUTIONARY-SEARCH`；W22；Self-Improving
  Language Models with Bidirectional Evolutionary Search；arXiv:2605.28814v1，2026-05-27 17:59:15 UTC；
  submission history 只有 v1。官方 repository 公开 logical/multihop/inference 三套 self-contained artifacts，
  无 release/tag；current repository 只能核验机制映射，不能充当 event-time immutable implementation snapshot。
- **Direct / Related Primary Sources / Access**：已读 arXiv metadata、891-line HTML/PDF 的 Abstract、Introduction、
  Preliminaries、Method、theory、三组 experiments、Related Work、Conclusion 与 Appendices A～H；核验 official project、
  repository overview、logical/multihop/inference artifact layout。全文覆盖 formula/proof assumptions、operator definitions、
  goal-tree update、three training/inference contracts、ablation、cost、prompts、case study、identified programs、limitations
  与 broader impacts。
- **Original Problem / Previous Design / Changed Constraint**：best-of-N 易并行且在中等难度下能提高 coverage；tree
  search 通过 prefix expansion 将预算集中到 promising branches，所以二者在 verifier 稀疏、候选可由模型原生分布覆盖时
  都合理。困难任务暴露两个边界：terminal reward 不能区分“部分解决了哪些子问题”，expansion-only 又只能沿既有 prefix
  继续生成。约束变化是固定 policy-call budget 下既需要跨轨迹复用局部进展，又需要可检查的 intermediate signal。
- **Mechanism / State Ownership**：forward search 拥有 step-level partial-trajectory pool，除 expansion 外加入 combination、
  deletion、translocation 与 crossover；single-parent selection 使用由 backward score 驱动的 Boltzmann sampling，two-parent
  selection 使用 joint subgoal coverage，temperature 随预算 anneal。backward search 将 root goal 分解成带 local verifier 的
  goal tree，以 parent verifier 与 child-average 的 recursive blend 为每个 forward node 评分，并每隔 `K` 个 forward steps
  扩展尚未解决的 leaf。search runtime 拥有 candidate identity、parentage、operator、goal-tree revision、verifier/version、
  score、policy-call budget 与 terminal state；policy 只负责 expansion/decomposition/operator prompt，不拥有 acceptance truth。
- **Control Flow / Data Flow / Implementation**：`root task -> initial candidate pool + goal tree -> select one/two parents ->
  expansion or evolutionary edit -> syntax/executable checks -> local-subgoal recursive scoring -> archive/pool update -> periodic
  unresolved-leaf decomposition -> repeat until policy-call budget -> terminal verifier selects answer`。post-training path 把选中的
  trajectories 送入 MaxRL/GRPO；inference path 直接返回 terminal verifier 得分最高者。sequence task 可直接编辑 step spans，
  program-search task 则把“operator”实现为 GPT-5 对两个 parent programs 的 prompted joint rewrite，二者不能当作同一低成本
  splice primitive。
- **Theory Boundary**：entropy-shell analysis 假设 per-step surprise bounded、step dependence 衰减、block total
  correlation 线性增长，且 evolution/verification 相比 policy calls 便宜；结论是 recombined candidate 的 expected native
  surprise 可离开 expansion-only typical shell，不是它语义有效、可执行或正确。exponential sample advantage 又假设 leaf
  satisfaction 独立、terminal success 要求所有 leaves，并在“pool 已含各 leaf evidence”后继续依赖 backward search 正确识别、
  operator 正确重组；论文没有证明 learned/generated local verifiers 可靠或 recombination 保持跨步骤语义。弱模型 decomposition
  也是作者承认的限制，Gemma-1B logical setting 实际使用 largely templated goal tree。
- **Evaluation / Training Contract**：Knights-and-Knaves 使用 Gemma-3-1B-it：1K 个 `n=2～4` SFT examples、5K 个
  `n=4～6` post-training examples、1,287 个 `n=2～10` validation problems、group 8、每题 200 policy calls、2×H200 trainer
  加独立 vLLM auxiliary GPU；不足 8 条 terminal trajectories 时以 i.i.d. rollout 补齐，正文只给 EMA curve。MuSiQue 使用
  Llama-3.2-3B/3.1-8B、3～4 hop solvable training split、official validation、group 8、budget 50、K-parallel 4、最多
  3 turns；2×H200 trainer、1×H200 E5/2018-Wikipedia FAISS retriever、1×H200 8B decomposer，local verifier 是
  `all-MiniLM-L6-v2` query/subquestion cosine `>=0.6` 且顺序检查。作者报告 3B/8B exact match 从 base
  `4.0/6.6` 到 BES `7.0/10.4`；GRPO 的 `2.1/5.6` 与 valid-search/finish proxy 支持 reward-hacking suspicion，不能证明单一因果。
- **Inference / Cost / Ablation Contract**：open problem solving 以 GPT-5 high reasoning、single CPU node、ShinkaEvolve
  SQLite archive、100 generations、archive 40、one island、每 run `$50` cap，circle-square `n=26`、rectangle `n=21`、
  Heilbronn-convex `n=13` 各 3 runs；OpenEvolve/GEPA/ShinkaEvolve 数字取自 SkyDiscover 的 claimed same-setting results，
  本文未重跑。BES 在三项 comparable open-source baselines 上报告最佳 mean，但没有超过列出的 AlphaEvolve/human best。
  Knights-and-Knaves 的 remove-answer-reweighting/remove-evolution ablation 均低于 full BES，却没有完整逐 operator、
  backward-only 或 verifier-quality sensitivity；MuSiQue median step time 为 GRPO 64s、Tree 240s、BES 309s，program-search
  API cost 约 `$13.7～18.6`，未给 token-equivalent end-to-end compute、post-training multi-seed CI 或独立复现。
- **What the Evidence Proves / Does Not Prove**：证据表明在作者的三类可自动验证任务、指定 decomposition/verifier 与
  compute contract 下，candidate recombination 加 dense subgoal selection 可以优于被测 i.i.d./tree/evolution baselines；
  不证明“越偏离模型概率壳越正确”、任意自然语言任务都可可靠分解、BES 对大模型/subjective task/long-horizon Agent 通用，
  也不证明收益来自某个单独 operator。作者明确要求 objective reward，未测试 academic writing 等 subjective evaluation，
  post-training 最大只到 8B；更强 search 还扩大 misuse capability。
- **Trade-offs / Previous Designs Still Apply / Failure Modes**：best-of-N 在请求可并行、selector 可靠、任务不需局部拼接时
  仍简单；beam/tree search 在 prefix semantics 强、重组易破坏因果时更安全；human-designed decomposition 适合安全关键且
  task structure 稳定；program evolution 适合 executable objective。BES 以更宽 candidate support 和稠密反馈换取 goal-tree/
  verifier state、operator validity、lineage、score recomputation、stagnation trigger 与额外 wall time，新增 false subgoal、
  coverage-proxy hacking、semantic splice conflict、invalid candidate、archive contamination、premature convergence、decomposer/
  verifier correlated error 与 search-level overfitting。subjective/不可逆/昂贵反馈任务仍应保留少量候选、外部审查与 abstain。
- **Evolution Relationship**：`Direct Evolution / Layering`：`single autoregressive sample -> best-of-N + terminal selector ->
  expansion-only beam/tree search -> population/archive mutation with executable objective -> recombinable trajectory pool + backward
  goal-tree scoring -> future typed operator preconditions + verifier ensembles + lineage-aware rollback`。backward decomposition 是
  selection layer，evolution operators 是 proposal layer；它们可独立演进，不应把 BES 写成对旧搜索的普遍替代。
- **ROADMAP / Chapters / Existing Coverage**：主 owner Ch20，已读 Ch19～21，并复核 Ch29、Ch75、Ch77 的相关段落。
  Ch20 已覆盖 parallel trajectory coverage、selector/verifier、comparison-graph state、budget 与 correlated self-verification，
  尚未展开 expansion-only support boundary、cross-trajectory recombination 和 backward subgoal-scoring state。Ch29 只负责
  selected trajectories 怎样进入 grouped RL、reward/rollout provenance；Ch75 负责 goal decomposition 与 search-based planning；
  Ch77 负责 executable artifact population、sandbox/evaluator/lineage，不重复拥有通用 candidate-search topology。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental` / Ch20；
  Historical Books Gate 关闭，本轮不修改 Books。待验证 immutable event-time code commit、exact logical accuracy table、
  operator-by-operator/backward-only ablation、decomposition/verifier error calibration、invalid-recombination rate、compute/token-
  matched baselines、post-training multi-seed variance、larger backbones、subjective/non-executable tasks、cross-domain replication、
  held-out search overfitting 与 total generation/verifier/decomposer latency/cost/SLO。

### ResearchMath-14K — 24/30

- **Candidate / Week / Source Family**：`RESEARCHMATH-OPEN-PROBLEM-DATA-AND-IMPERFECT-TRAJECTORIES`；W22；
  ResearchMath-14K: Scaling Research-Level Mathematics via Agents；arXiv:2605.28003v1，2026-05-27 05:54:41 UTC；
  paper 明示 `Work in progress`，submission history 只有 v1。官方 Hugging Face dataset 首次 commits 为 05-28，
  属同一 W22 family 的 post-paper artifact node。
- **Direct / Related Primary Sources / Access**：已读 v1 metadata、496-line HTML/PDF 的全部主章节、tables/figures、
  Conclusion/Future Work 与 Appendices A～H；核验 current official dataset card、viewer、schema、files 和 commit history。
  公开目录当前只有一个 47.9 MB `data/train.jsonl` 与 14,056-row question dataset；未定位到 paper 宣称一并 release 的
  220K ResearchMath-Reasoning、5K filtered subset、training code、trained adapters、filter logs 或 frozen evaluation outputs。
- **Original Problem / Previous Design / Changed Constraint**：contest/textbook math data 有明确答案，适合 correctness-first
  filtering；少量专家 research benchmarks 适合 evaluation，但直接训练会污染稀缺 held-out evidence。约束变化是开放数学问题
  本来没有完整 ground truth，而且 statement 依赖论文局部定义、其 open status 还会随文献演进。旧的 verified-solution pipeline
  因此无法低成本扩展，单纯把论文段落当 prompt 又会制造不自洽任务。
- **Mechanism / State Ownership**：Extractor（Codex/GPT-5.5 xhigh）逐篇读取公开 source，保存 verbatim question quote 并
  补局部 context；Refiner（Claude Code/Opus 4.7 medium）重读 source、搜索至多十篇 later papers，生成 self-contained rewrite、
  taxonomy 与 `open/partially_solved/solved/unknown` status/evidence。Qwen3-Embedding-8B 对 original/rewrite 分别做 near-duplicate
  detection，任一 cosine `>0.9` 即合并，优先保留 paper source。teacher models 再产生 attempts；reference-span extractor、
  web-search Agent 与 surface counters 给 trajectory 添加 filter verdict。source owner、status verifier、dataset curator、teacher、
  filter 与 downstream trainer 必须是不同 identity，不能由最终 JSON/dataset name 抹平。
- **Control / Data Flow**：`1,233 public source documents -> 20,835 extracted quote+rewrite records -> contextual/status refinement
  -> original/rewrite embedding dedup -> 14,056 problem records -> two teachers x about 16 attempts/problem -> 220K trajectories
  -> behavior/reference filtering -> 5K training subset -> LoRA on three Qwen3 bases -> answer-verifiable downstream evaluation`。
  durable row identity 至少包括 source URL/page/quote、extractor/refiner model+prompt、search cutoff、status evidence/revision、rewrite、
  taxonomy、dedup cluster/threshold、teacher/config、filter/verifier verdict 与 artifact digest。
- **Dataset / Audit Contract**：source partition 为 524 arXiv open-problem papers（8,182 extracted）、161 Google-discovered
  web pages（5,331）与 548 workshop/problem sheets（7,322）；paywalled documents 被排除。dedup 从 20,835 降至 14,056，
  但 threshold sensitivity 只给 borderline examples，未给 cluster-level human precision/recall。500-record self-containment audit
  由 Codex/LLM judge 完成：refined `471/500`（94.2%），仍有 29 个 context gaps，不是数学专家 validation。released status
  分布为 open 8,313、partial 2,083、solved 1,171、unknown 2,489，说明 dataset 不是“14K 个仍未解决问题”的同义词。
- **Behavior / Factuality Contract**：两位 teachers 为 GPT-OSS-120B 与 Qwen3-30B-A3B；unfiltered Qwen3-4B run 被报告
  近零退化，但作者未给分数或完整 contract。八模型×ResearchMath 90 traces 的 720-trace audit 中，629 含 reference-like
  object、389 至少含一项 fake；19,864 mentions 中 3,492 被判 fake。reference verifier 只检查对象能否在 Web 找到，不检查
  source 是否支持当前 claim。`5.6x` references / `5.0x` fakes 是四组 older→newer models 在该 no-search harness 的 aggregate，
  不能归因于 internet-search RL；论文也只把它列为 plausible explanation。
- **Filtering Ambiguity**：Section 5 的动机称排除被 rule-based counters 或 Agent judges 标记的 trajectories，训练设置却只
  具体说明检索每个 reference-like span，并删除任何含 fake reference 的 trace；`assume/abandon` 是否实际进入 5K subset
  filter、阈值与各 stage retention 未披露。因而不能把 `ResearchMath-Reasoning-Filtered` 当作可复现的稳定 policy，也不能从
  “citation exists”推断推理正确、引用支持 claim 或 partial mathematics 有价值。
- **Training / Evaluation Contract**：Qwen3-4B/8B/30B-A3B base 各以 rank-64、alpha-128、dropout 0.05 LoRA，在
  ResearchMath filtered 或 5K DASD control 上训练；每 setting 3 seeds，per-device batch 1，global batch 为 32/32/16，
  sequence truncation 为 24,512/24,512/32,768。评测 AIME 2024～2026 `n=90`、integer-only HLE `n=315`、
  SOOHAK Challenge+Mini `n=501`，用 math-verify；作者报告 9 个 model×benchmark cells 全部高于 base，平均 `+9.2` points，
  对 DASD 为 8/9 cells，HLE+SOOHAK 平均 `+2.6`。hardware、optimizer、learning rate、precision、epochs/steps、token
  budget、checkpoint selection 与 source/semantic decontamination 未披露；没有在真正无已知答案的 training problems 上验证
  proof correctness，结果只证明 downstream answer-verifiable tasks 的迁移。
- **What the Evidence Proves / Does Not Prove**：作者 setup 支持“带原始 quote/status evidence 的 literature extraction 能扩展
  research-level prompt supply，且在删除若干显性失败后，未证正确的 teacher attempts 可作为受限 behavioral supervision”。
  它不证明 14,056 statements/status 全部正确、GPT-5-mini difficulty Elo 等于专家难度、wrong reasoning 普遍优于 correct
  demonstrations、新模型天然更不 factual、fake-reference filter 捕获所有有害错误，或训练模型取得 research breakthrough。
- **Artifact / Governance Boundary**：current dataset card 将 config split 声明为 `test`、文件名却是 `train.jsonl`，usage example
  又请求 `split="train"`，split semantics 内部不一致；它没有 source-level immutable license/derivative-policy manifest。paper
  与 card 声明 MIT，且排除 paywall，仍不能由顶层 license 自动证明每个公开 source 的改写、再发布和 downstream training
  obligations。open status、source correction 与 later resolution 还要求 supersession，而不是原地覆盖旧 row。
- **Trade-offs / Previous Designs / Failure Modes**：专家题目/解答最贵但 correctness 与 attribution 强；literature extraction
  扩 coverage，却增加 context omission、status staleness、source/license skew 与 judge correlated error；synthetic hard-problem
  generation 可控制 schema，却可能脱离真实研究；open attempts 可提供 tactics/style，却也会蒸馏 false lemmas、fake support、
  premature authority 与 teacher bias。verified solutions 仍适合 proof correctness，open attempts 只适合分层标记的 exploratory
  behavior supervision；必须保留 rejection、expert sample audit、held-out provenance 与 correction/rollback。
- **Evolution Relationship**：`Direct Evolution / Layering`：`solved exercise + ground-truth answer -> expert research benchmark ->
  source-grounded open-question extraction -> self-contained rewrite + mutable status evidence -> unverified teacher attempts ->
  negative-behavior filtering -> future claim/lemma-level provenance + expert/solver feedback + supersedable dataset`。task curation、
  trajectory curation 与 evaluation correctness 是三层 gate，后层不能回头证明前层正确。
- **ROADMAP / Chapters / Existing Coverage**：主 owner Ch23，已读 Ch22～24，并复核 Ch25/62 handoff。Ch23 已覆盖 collection
  protocol、model-filter bias、synthetic trajectory/verifier lineage、dedup/decontamination、partition policy 与 immutable manifest，
  但尚未显式区分 ground-truth-unavailable 的 task、mutable knowledge-status evidence 与 “incorrect but potentially useful”
  demonstration tier。Ch25 只负责这类 traces 作为 SFT target 的 correctness/capacity risk；Ch62 负责 downstream score、judge
  calibration 与 contamination claim，不能替数据 owner 接受 row。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental` / Ch23；
  Historical Books Gate 关闭，本轮不修改 Books。待核验 220K/5K/code/adapters 的真实公开 artifact、event-time manifest、
  exact filter composition/retention、expert statement/status audit、dedup precision/recall、status refresh/supersession、source-level
  license、train/eval overlap、full optimizer/hardware/precision/token contract、per-cell raw runs、correct-vs-incorrect trace ablation、
  fake-reference-only vs multi-filter ablation、learning without citation style、larger/different students 与 independent reproduction。

## 2026-08-13 Primary-Text Recovery Addendum — 27 Full Source Reviews

本节替代下方保留的旧 access-failure 记录。27 个精确 arXiv HTML 已全部恢复；逐篇覆盖 metadata/revision、
Introduction/Related Work、Method/公式、implementation、evaluation/baselines/ablations、Appendix/limitations 与
可用 artifact。旧记录只解释为何此前 blocked，不再代表当前状态。

### Batch A — Memory、Skill、Safety 与 Harness

| Candidate | Verified mechanism and state boundary | Evaluation / trade-off boundary | Owner / provisional disposition |
| --- | --- | --- | --- |
| AgentDoG 1.5 | 固定三轴 risk-source / failure-mode / harm taxonomy，按 Codex/OpenClaw 扩 leaf；taxonomy-guided data、influence purification、finite-state training env 与 final-delivery guardrail 共用 trajectory identity | 0.8B～8B、约 1K samples、text trajectories；Docker 100× 与 frontier comparison 只对作者 harness，不能替代 multimodal/process enforcement | Ch68；`Refine / Experimental` |
| How LoRA Remembers? | exact-token memory 出现 probability≈0.5 phase transition；MemFT 只给 stubborn tokens 保留梯度，避免 easy-token over-optimization | 仅 8B、greedy decoding；law 未验证其他 scale/sampling，parametric recall 不等于 reasoning/generalization | Ch26；`Refine / Experimental` |
| MemTrace | 把 memory execution 建成 graph，以 counterfactual node bypass / observation attribution 区分 extraction、storage、retrieval、answer errors | 覆盖有限 memory systems/benchmarks；LLM judge 偏严格，attribution cost/causality 不是生产真值 | Ch73，Ch65 handoff；`Refine / Experimental` |
| FluxMem | memory 从 immutable items 演进为 online step connection、context verification/topology editing、offline skill induction/consolidation | LoCoMo/Mind2Web/GAIA 与指定 backbones；迭代 LLM latency/token/API cost 未系统计量，错误 edge 会传播 | Ch73；`Refine / Experimental` |
| Skill0.5 | policy 同时 internalize general skills、按 state retrieve external skills，避免 full-context overload 与 full-parametric rigidity | ALFWorld/WebShop text environments；OOD gains 不证明 open-web/code/multimodal transfer，skill conflict/capacity 仍存在 | Ch80，Ch29 handoff；`Refine / Experimental` |
| SkillGrad | 把 skill package 视作参数，以 task diagnosis 作 gradient、pattern memory/overlay 作 momentum、layer-aware patch 作 update | spreadsheet/WikiTQ 为主；类 gradient 只是 operational analogy，无 convergence theorem，patch 需要 regression/rollback | Ch80；`Refine / Experimental` |
| COLLEAGUE.SKILL | 从 selected human interaction evidence 蒸馏 portable/inspectable/editable/versionable/consent-bound skill package，而非模拟完整人格 | expert selection、consent、privacy、staleness 与 impersonation 风险；公开 gallery success 不证明跨领域正确 | Ch80；`Refine / Experimental` |
| SkillAdaptor | 从 trajectory 定位 first actionable fault，将 correction 映射至负责 skill section，再 validation-gated patch | WebShop/PinchBench/Claw-Eval；稀疏延迟反馈或缺工具会削弱 attribution，长期 drift 未测 | Ch80；`Refine / Experimental` |
| Harness Updating Is Not Harness Benefit | 固定 backbone，分离 updater ability、consumer benefit 与 harness state revision，防止“会改 prompt/skill”被当成收益 | 只测 non-parametric harness update；未覆盖 weight/hybrid adaptation，harness/model tier 强耦合 | Ch80，Ch62 handoff；`Refine / Experimental` |

### Batch B — Agent Environment、Search、Evaluation 与 Workflow

| Candidate | Verified mechanism and state boundary | Evaluation / trade-off boundary | Owner / provisional disposition |
| --- | --- | --- | --- |
| CUA-Gym | instruction-context pair、session-isolated app state、独立 setup/reward agents、state-diff verifier 与 adversarial information barrier | terminal-state reward 不能区分 destructive-but-restored process；mock apps、reward proxy 与 leakage 仍是 failure modes | Ch62，Ch77 handoff；`Refine / Experimental` |
| LaRA | 对 semantic-equivalent 与 information-removal perturbations 比较 layer representation stability/shift，补充 output contamination detector | RL-trained model/dataset controls 有限；hidden-state extraction 昂贵，AUC 不是 causal memorization proof | Ch62；`Refine / Experimental` |
| Claw-Anything | event stream、多 service、CLI+GUI、proactive trigger 与 long horizon 共同定义 always-on assistant subject | mock services/device coverage 有限；proactive Pass@1 低且 access 增加 privacy/permission risk | Ch62，Ch68 handoff；`Refine / Experimental` |
| Crafter | planner/generator/critic 以 structured directive state 生成并迭代 editable SVG，避免自然语言 correction 跨轮冲突 | closed image models与 judges、limited scientific figures；multi-agent cost 与 judge bias 未隔离 | Ch77；`Refine / Experimental` |
| GrepSeek | Agent 直接在 frozen corpus 上用 rg/grep pipelines 检索；engine 仅对 shard-independent transformations 并行，unsafe global pipeline 回退顺序执行 | lexical surface-form、file-order ranking 与 sandbox/security 限制；不是 semantic retrieval 的替代 | Ch72，Ch77 handoff；`Refine / Experimental` |
| TASTE | 以 adaptive contrastive n-gram 与 negative evidence 生成 benchmark candidates，再由 hint-assisted verifier 验证 | verifier 只在有限 Airline/Retail sample 校准；生成器/verifier shared blind spot、validity 不等于 coverage realism | Ch62；`Refine / Experimental` |
| SAAS | search-enabled/disabled rollouts估计 evolving search boundary；boundary-aware reward + stage-wise curriculum 避免 static penalty 诱发不搜索 | 七个 QA benchmarks；search freshness/cost、boundary classifier error 与 reward hacking 仍受限 | Ch75；`Refine / Experimental` |
| RAMP | persistent compiler workflow 保留 serial artifacts、checkpoint/resume/retry，并记录 token/turn/command/time 与 failure taxonomy | compiler 单域、metric weights/model-harness confound；runtime observability 不等于 production representativeness | Ch62，Ch65 handoff；`Refine / Experimental` |
| Masking Stale Observations | retention window K 在 retriever弱/model强等 regime 降低 stale observation attention，但 model saturated 时可能丢证据 | K=5、500 turns、GPT-5-mini judge；形成 regime map 而非 universal context policy | Ch71；`Refine / Experimental` |
| ResearchClawBench | 以 paper target、code/data、experiment execution 与 report rubric 评 end-to-end re-discovery，区分报告完整与机制/协议正确 | dry-lab 与 final-report scoring 为主；榜单混合 model、harness、tools、budget，不能视为模型能力 | Ch62；`Refine / Experimental` |

### Batch C — Training、MoE、Distillation 与 Inference

| Candidate | Verified mechanism and state boundary | Evaluation / trade-off boundary | Owner / provisional disposition |
| --- | --- | --- | --- |
| Domino | parallel draft backbone 保留低延迟，轻量 GRU causal encoder + low-rank correction 恢复 intra-block dependency | Qwen3、A100、Transformers/SGLang low-concurrency；5× speedup 不外推不同 hardware/concurrency/kernel | Ch44；`Refine / Experimental` |
| Trust-Region Behavior Blending | 每 prefix 求接近 teacher 且受 `KL(mu||student)<=epsilon` 约束的 behavior policy，仅 warmup 后回纯 student OPD | 两个 Qwen3 math settings；teacher co-residency/decoding 增加成本，epsilon/schedule 不保证迁移 | Ch25；`Refine / Experimental` |
| Trust Region OPD | 识别 teacher-student outlier region，对 OPD token update 施加 trust mask/constraint以避免 unreliable ratios 主导 | 1.5B/1.7B reasoning post-training；缺 deployment/mid-training evidence，不能当通用 distillation rule | Ch25；`Refine / Experimental` |
| LongTraceRL | 从 search trajectories 构造 long context、hard distractors 与 positive rubric reward，训练 evidence selection/reasoning | KILT/Wikipedia 单源、rubric/entity overlap 与 downstream transfer；污染、reward hacking、domain diversity受限 | Ch22，Ch29 handoff；`Refine / Experimental` |
| dMoE | diffusion LM 先聚合 token router score 为 block-level expert coreset，再在 coreset 内 token route；top-p 调计算质量 | 语言 dLLM、披露 model/tasks；动态 expert count 新增 dispatch/load/kernel complexity，未证明其他 modality/serving SLO | Ch21；`Refine / Experimental` |
| Draft-OPD | drafter own-policy block 导致 SFT distribution mismatch；target-assisted rollout + verification-error replay 保留可训练 on-policy states | 速度依 target/drafter/backend/temperature/hardware；训练更贵，draft instability 与 verification identity 必须治理 | Ch44，Ch25 handoff；`Refine / Experimental` |
| SCOPE | Challenger 生成 frontier tasks/rubrics，Solver RL 更新，两 policy co-evolve；rubric quality 是 self-judge 瓶颈 | 7～8B、额外多阶段 compute；open-ended judge correlation 与 collapse 风险，不能替代 curated/human evidence | Ch29；`Refine / Experimental` |
| Smaller Models Are Natural Explorers | early rollouts 混入 frozen smaller policy 的高 policy-level diversity，随后 transition 到 large policy GRPO | math RLVR 与 verifiable reward；capacity/entropy/compute confound，未验证 open-ended domain | Ch29；`Refine / Experimental` |

### Recovery Review Result

- 27/27 原 blocked families 均恢复 primary text，42/42 `20+` W22 candidates 完成 current-version Full Source Review。
- 所有性能数只保留在上述 workload contract 内；未披露 hardware、precision、length、batch、concurrency 或 SLO
  的条目统一视为 `Not Disclosed`，没有用标题或作者 benchmark 外推。
- 相同机制按 Source Family 去重：两项 trust-region distillation 是并列分支；Domino 与 Draft-OPD 分别解决
  draft architecture 与 training distribution；Skill0.5/SkillGrad/SkillAdaptor/Harness Updating 分别拥有
  parametric-external hybrid、patch optimizer、fault attribution、benefit measurement，不合并成单一“skill evolution”。
- Historical Books Gate 仍关闭；本节只形成 provisional owner/disposition，不修改 Books。

### Historical Access Record — How LoRA Remembers? — 24/30 — Resolved 2026-08-13

- **Candidate / Week / Source Family**：`HOW-LORA-REMEMBERS-PARAMETRIC-MEMORY`；W22；
  arXiv:2605.30260，既有 discovery ledger 记录 first-public 2026-05-29。
- **Verified Access Boundary**：本检查点对 arXiv HTML/PDF 的读取被当前保存的访问权限明确拒绝；仓库中也没有可审计的
  本地正文或作者 artifact。因此只有 candidate identity、既有日期账目与 primary-source URL 被保留，标题中的
  “remembers” 以及 pending focus 中的 rank/data/step/forgetting 不能作为机制或实验事实。
- **Missing Full-read Coverage**：Metadata revision history、Abstract、Introduction、Related Work、Method、公式、
  implementation、evaluation setup、baselines、causal controls、ablations、hardware/model/precision/data/step contract、
  limitations、appendices 与 author artifact 均未完成读取；不得把任何 parametric-memory law、scaling relation 或
  forgetting behavior 写成作者已证明结论。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 完成后，仅在 primary text 可访问时重试；在此之前
  Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### MemTrace — 27/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`MEMTRACE-MEMORY-ERROR-TRACE-ATTRIBUTION`；W22；
  arXiv:2605.28732，既有 discovery ledger 记录 first-public 2026-05-27。
- **Verified Access Boundary**：arXiv primary text 与 Hugging Face paper surface 均被当前保存的访问权限明确拒绝；
  工作区、临时目录与 Downloads 中也没有对应正文或作者 artifact。因此本检查点仅保留 candidate identity、既有
  first-public 账目与 primary-source URL；不得由题名或 pending focus 推断 taxonomy、attribution 或 intervention 机制。
- **Missing Full-read Coverage**：Metadata revision history、Abstract、Introduction、Related Work、Method、状态所有权、
  trace schema、control/data flow、implementation、evaluation contract、baselines、causal intervention、observability overhead、
  failure modes、limitations、appendices 与 author artifact 均未读取，任何性能或有效性结论均为尚未验证。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在 primary text 可访问时重试；Historical
  Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### CUA-Gym — 28/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`CUA-GYM-EXECUTABLE-ENVIRONMENT-SYNTHESIS`；W22；
  arXiv:2605.25624，既有 discovery ledger 记录 first-public 2026-05-25。
- **Verified Access Boundary**：本检查点已知 arXiv 域被保存权限拒绝；周报所记 Qwen artifact 的最直接
  `QwenLM/CUA-Gym` GitHub 路径也被保存权限明确拒绝，工作区、临时目录与 Downloads 无对应 primary material。
  因此只保留 candidate identity、既有日期账目与两个 primary-source surface，不把 repository/product identity 当机制证据。
- **Missing Full-read Coverage**：论文 metadata/revision、全文/Appendix、environment generator、state ownership、task schema、
  reset/fork/isolation、verifier/reward、RL rollout、implementation、leakage/decontamination、evaluation setup、baselines/ablations、
  hardware/model/precision/length/concurrency/SLO、limitations，以及 artifact README/code/data/license 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在 paper 与 artifact 至少一者可审计、且论文
  full-read coverage 可完成时重试；Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### LaRA contamination detection — 24/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`LARA-LAYERWISE-CONTAMINATION-DETECTION`；W22；
  arXiv:2605.29888，既有 discovery ledger 记录 first-public 2026-05-28。
- **Verified Access Boundary**：候选账本只列 arXiv primary source，而该域在本检查点已被保存权限明确拒绝；
  工作区、临时目录与 Downloads 中未找到对应正文、代码、数据或作者 artifact。因此只保留 candidate identity、
  既有日期账目与 URL，不由名称推断 LaRA 缩写、layer-wise signal、contamination score 或适用模型。
- **Missing Full-read Coverage**：Metadata/revision、Abstract、Introduction、Related Work、Method/公式、layer/state ownership、
  probe or detector implementation、contamination construction、SFT/RL controls、clean/contaminated baselines、false-positive/
  false-negative calibration、model/data/precision/hardware contract、ablations、limitations、appendices 与 artifact 全部未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在全文可审计时重试；Historical Evidence Gate
  保持 Open、Historical Books Gate 保持 Closed。

### FluxMem — 26/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`FLUXMEM-DYNAMIC-MEMORY-CONNECTIVITY`；W22；
  arXiv:2605.28773，既有 discovery ledger 记录 first-public 2026-05-27。
- **Verified Access / Artifact Boundary**：账本中的唯一 paper surface 属于本检查点已被保存权限拒绝的 arXiv 域；
  artifact 仅标记为 `planned code`，没有可访问 release/commit identity。工作区、临时目录与 Downloads 也未发现对应
  paper、repository snapshot、dataset 或 model artifact。因此不得将项目名或 pending focus 当作机制披露。
- **Missing Full-read Coverage**：Metadata/revision、全文与 Appendix、memory-node/edge representation、state ownership、
  feedback/control flow、connectivity update、pruning/consolidation、rollback/supersession、implementation、evaluation setup、
  baselines/ablations/overhead、hardware/model/precision/length/concurrency/SLO、limitations 以及 code/data/license 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在论文全文和实际 artifact identity 可审计时重试；
  Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### Skill0.5 — 25/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`SKILL0-5-INTERNALIZE-EXTERNALIZE-SKILLS`；W22；
  arXiv:2605.28424，既有 discovery ledger 记录 first-public 2026-05-27。
- **Verified Access / Artifact Boundary**：Sources 只保存受限 arXiv URL；Pending 表虽写 `+ code`，但周报没有
  repository URL、organization、release、tag 或 commit，工作区、临时目录与 Downloads 也没有 paper/code/model/data
  artifact。缺少 immutable artifact identity 时，不能把“有代码”视为来源已核验，更不能由候选名恢复实现。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、skill representation、router state/ownership、
  internalization/externalization control flow、difficulty tiers、training data、OOD definition、conflict detection/resolution、
  implementation、evaluation/baselines/ablations/overhead、hardware/model/precision/length/SLO、limitations 与 code provenance 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在论文和可定位 code artifact 可审计时重试；
  Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### SkillGrad — 24/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`SKILLGRAD-TEXTUAL-GRADIENT-SKILL-UPDATE`；W22；
  arXiv:2605.27760，既有 discovery ledger 记录 first-public 2026-05-26。
- **Verified Access / Artifact Boundary**：Sources 只列受限 arXiv URL；Pending 表的 `+ code` 没有 repository URL、
  owner、release、tag 或 commit，工作区、临时目录与 Downloads 也没有 paper/code/data artifact。因而只保留
  candidate identity、既有日期账目与 URL，不能由名称或待审字段恢复 update algorithm。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、textual-gradient representation、critic/updater ownership、
  momentum/history state、patch proposal/acceptance/rollback、skill versioning、training/evaluation data、held-out regression、
  baselines/ablations/overhead、model/hardware/length/cost/SLO、limitations 与 code provenance 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在 paper 和可定位 code artifact 可审计时重试；
  Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### Claw-Anything — 24/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`CLAW-ANYTHING-ALWAYS-ON-PROACTIVE-AGENT`；W22；
  arXiv:2605.26086，既有 discovery ledger 记录 first-public 2026-05-25。
- **Verified Access Boundary**：Sources 只列本检查点受保存权限限制的 arXiv URL；工作区、临时目录与 Downloads
  没有 paper、code、environment、trace 或 evaluation artifact。因此只保留 candidate identity、既有日期与 URL，
  不从 “Claw” 或 “always-on” 命名推断产品集成、background execution、权限或数据保留行为。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、initiative policy、trigger/silence/stop state、authority
  boundary、consent/rejection handling、environment/tool identity、privacy/data retention、implementation、proactivity and
  restraint metrics、human/simulator contract、baselines/ablations、cost/SLO/failure recovery、limitations 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在完整 primary text 或作者 artifact 可审计时重试；
  Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### Crafter — 25/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`CRAFTER-MULTIAGENT-EDITABLE-SVG-ARTIFACT`；W22；
  arXiv:2605.30611，既有 discovery ledger 记录 first-public 2026-05-28。
- **Verified Access / Artifact Boundary**：Sources 只列受限 arXiv URL；Pending 表的 `+ code/benchmark` 没有
  repository、dataset、organization、release、tag 或 commit identity，工作区、临时目录与 Downloads 也无对应
  paper/code/benchmark/output artifact。因此不能由候选名或待审字段重建 workflow、roles 或 SVG representation。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、role/agent ownership、shared-state and edit protocol、
  SVG/component representation、artifact validation、verifier/human rubric、task provenance、implementation、benchmark split、
  baselines/component ablations、visual and semantic failure modes、model/tool/cost/latency contract、limitations 与 artifact license 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在 paper、code 和 benchmark 至少能形成可定位
  evidence chain 时重试；Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### Domino speculative decoding — 27/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`DOMINO-SPECULATIVE-DECODING`；W22；
  arXiv:2605.29707，既有 discovery ledger 记录 first-public 2026-05-28。
- **Verified Access / Artifact Boundary**：Sources 只列受限 arXiv URL；Pending 表的 `+ code` 没有 repository、
  organization、release、tag 或 commit identity，工作区、临时目录与 Downloads 也无 paper/code/model artifact。
  因此不能从 “Domino” 名称或待审字段恢复 draft/target topology、head design 或 runtime integration。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、parallel backbone、causal refinement head、training
  curriculum、draft/target state ownership、proposal/verification/rollback flow、acceptance measurement、implementation/backend、
  evaluation baselines/ablations、model/hardware/precision/prompt/output/batch/concurrency/SLO、quality and latency failure modes、
  limitations 与 code provenance 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在论文与可定位 code artifact 可审计时重试；
  Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### COLLEAGUE.SKILL — 24/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`COLLEAGUE-SKILL-TRACE-DISTILLATION`；W22；
  arXiv:2605.31264，既有 discovery ledger 记录 first-public 2026-05-29。
- **Verified Access / Artifact Boundary**：Sources 只列受限 arXiv URL；Pending 表写 `+ open-source artifact`，
  但未记录 repository URL、owner、release、tag、commit、dataset 或 model identity，工作区、临时目录与 Downloads
  也没有对应 artifact。因此不能由名称或 artifact 标签恢复 skill schema、distillation flow 或 evaluation。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、source trace selection、skill representation、
  distiller/updater/consumer ownership、capability-vs-behavior definition、acceptance/correction/rollback、versioning/provenance、
  implementation、evaluation setup、baselines/ablations、measured-vs-claimed capability boundary、model/tool/cost/SLO、
  limitations 与 artifact license/reproducibility 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在 paper 和 immutable artifact identity 可审计时重试；
  Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### GrepSeek — 27/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`GREPSEEK-TRAINED-REPOSITORY-SEARCH`；W22；
  arXiv:2605.29307，既有 discovery ledger 记录 first-public 2026-05-28。
- **Verified Access / Artifact Boundary**：Sources 只列受限 arXiv URL；Pending 表的 `+ code` 没有 repository URL、
  owner、release、tag、commit、training data 或 model identity，工作区、临时目录与 Downloads 也没有对应 artifact。
  因而不能由名称或待审字段恢复 repository-search runtime、trainer 或 byte-sharding implementation。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、Tutor/Planner ownership、trajectory generation/filter、
  GRPO reward/group contract、shell/tool sandbox、repository snapshot and shard state、byte-equivalence invariant、retrieval/search
  control flow、implementation、evaluation/baselines/ablations、lexical/semantic failure regimes、hardware/model/precision/context/
  concurrency/cost/SLO、limitations 与 code/data license 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在 paper 与 immutable code/data identity 可审计时重试；
  Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### TASTE agent-benchmark synthesis — 26/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`TASTE-AGENT-BENCHMARK-SYNTHESIS`；W22；
  arXiv:2605.28556，既有 discovery ledger 记录 first-public 2026-05-27。
- **Verified Access / Artifact Boundary**：Sources 只列受限 arXiv URL；Pending 表的 `+ benchmark` 没有
  repository/dataset URL、owner、release、tag、commit、version、split 或 license identity，工作区、临时目录与 Downloads
  也没有 paper/benchmark artifact。因此不能由名称或待审字段恢复 task generator、tool schema 或 grader。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、source-task provenance、tool-sequence generation、
  environment/tool state、validity judge、coverage/difficulty objective、contamination/decontamination、grader independence/
  calibration、implementation、benchmark tasks/splits、baselines/ablations、model/tool/cost/SLO、limitations 与 dataset license 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在 paper 与 versioned benchmark artifact 可审计时重试；
  Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### Trust-Region Behavior Blending — 24/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`TRUST-REGION-BEHAVIOR-BLENDING`；W22；
  arXiv:2605.31159，既有 discovery ledger 记录 first-public 2026-05-29。
- **Verified Access Boundary**：Sources 只列本检查点受限的 arXiv URL；工作区、临时目录与 Downloads 没有
  paper、code、config、checkpoint 或 run artifact。因此只保留 candidate identity、既有日期与 URL，不能由题名
  判断 trust-region 作用于 behavior policy、token distribution、trajectory、loss 还是 deployment mixer。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、behavior/policy ownership、KL direction/estimator、
  constraint/clip/penalty formulation、blending and annealing schedule、prefix/on-policy distribution、implementation、two-setting
  evaluation、baselines/ablations/sensitivity/seeds、stability/outlier/failure analysis、model/data/hardware/precision/cost/SLO、
  limitations 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在完整 primary text 可审计时重试；Historical
  Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### Trust Region On-Policy Distillation — 25/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`TRUST-REGION-ON-POLICY-DISTILLATION`；W22；
  arXiv:2606.01249，既有 discovery ledger 记录 first-public 2026-05-31。
- **Verified Access Boundary**：Sources 只列本检查点受限的 arXiv URL；工作区、临时目录与 Downloads 没有
  paper、code、configuration、checkpoint 或 run artifact。因此只保留 candidate identity、既有日期与 URL，
  不由标题推断它与 TRB、teacher/student policy 或特定 KL estimator 的关系。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、teacher/student/reference policy ownership、
  reliable/outlier-region definition、reverse/forward-KL estimator、mask/clip/threshold、on/off-policy sampling and guidance、
  implementation、evaluation/baselines/ablations/sensitivity/seeds、stability/failure analysis、model/data/hardware/precision/
  rollout/cost/SLO、limitations 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在完整 primary text 可审计时重试；Historical
  Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### LongTraceRL — 25/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`LONGTRACERL-LONG-HORIZON-DISTRACTOR-RL`；W22；
  arXiv:2605.31584，既有 discovery ledger 记录 first-public 2026-05-29。
- **Verified Access / Artifact Boundary**：Sources 只列受限 arXiv URL；Pending 表的 `+ code/data/models` 没有
  repository/dataset/model URL、owner、release、tag、commit、version、checksum 或 license identity，工作区、临时目录与
  Downloads 也无对应 artifact。因此不能从项目名或待审字段恢复 trajectory construction、reward 或 checkpoints。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、source trajectory ownership、distractor generation、
  positive-only rubric reward、policy/reward/verifier flow、reward-hacking controls、contamination/decontamination、implementation、
  data/model artifact schema、evaluation/baselines/ablations/seeds、model/hardware/precision/trajectory length/batch/cost/SLO、
  limitations 与 artifact provenance 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在 paper 与 versioned code/data/model artifacts
  可审计时重试；Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### dMoE — 25/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`DMOE-DISTRIBUTED-MOE-BLOCK-EXPERTS`；W22；
  arXiv:2605.30876，既有 discovery ledger 记录 first-public 2026-05-29。
- **Verified Access / Artifact Boundary**：Sources 只有当前策略拒绝访问的 arXiv URL；Pending 表的 `+ code`
  没有 repository、owner、release、tag、commit、version、checksum 或 license identity，工作区、临时目录与 Downloads
  也没有对应 paper、code、configuration、checkpoint 或 run artifact。候选名与评分仅保留为 discovery record，
  不能据此反推 block-level expert placement 或 runtime data flow。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、block/expert partition、parameter/optimizer/KV state
  ownership、dispatch/routing 与 collective control flow、activation/parameter/memory traffic、kernel/runtime implementation、
  topology、failure recovery、quality/latency/memory evaluation、baselines/ablations/sensitivity、model/hardware/precision/
  sequence length/batch/concurrency/SLO、limitations、code-path identity 与 later-revision boundary 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在 paper 与 immutable code artifact 可审计时
  重试；Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### SkillAdaptor — 24/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`SKILLADAPTOR-FAULT-ATTRIBUTED-SKILL-ADAPTATION`；W22；
  arXiv:2606.01311，既有 discovery ledger 记录 first-public 2026-05-31。
- **Verified Access / Artifact Boundary**：Sources 只有当前策略拒绝访问的 arXiv URL；Pending 表明确只是
  `planned code`，没有 repository、owner、release、commit、schema、dataset、license 或可执行 artifact identity，
  工作区、临时目录与 Downloads 也无对应材料。因此不能把 planned release 当作 implementation evidence。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、first-actionable-fault definition/attribution、
  skill responsibility 与 ownership、trajectory-to-update control flow、acceptance checks、regression tests、rollback/
  supersession、conflict resolution、implementation、benchmark construction/realism、baselines/ablations/sensitivity、
  gain magnitude/variance、model/data/hardware/precision/trajectory length/batch/cost/SLO、limitations 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在完整 paper 与 versioned artifact 可审计时
  重试；Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### Draft-OPD — 27/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`DRAFT-OPD-ON-POLICY-DISTILLATION`；W22；
  arXiv:2605.29343，既有 discovery ledger 记录 first-public 2026-05-28。
- **Verified Access / Artifact Boundary**：Sources 只列当前策略拒绝访问的 arXiv URL；没有 technical report、
  author repository、release、model/data card 或 immutable artifact identity，工作区、临时目录与 Downloads 也无
  primary text。候选名与 Pending Focus 不是机制证据。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、teacher/student/reference policy ownership、
  target-assisted rollout、verification-error replay、on-policy signal construction、sampling/update control flow、
  acceptance/throughput conditions、implementation、baselines/ablations/sensitivity/seeds、quality/cost/stability、
  model/data/hardware/precision/length/batch/concurrency/SLO、limitations 与 failure recovery 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在完整 paper 与 supporting artifact 可审计时
  重试；Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### SCOPE — 25/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`SCOPE-CHALLENGER-SOLVER-COEVOLUTION`；W22；
  arXiv:2605.31433，既有 discovery ledger 记录 first-public 2026-05-29。
- **Verified Access / Artifact Boundary**：Sources 只列当前策略拒绝访问的 arXiv URL；没有 author repository、
  dataset、model card、release、judge implementation 或 immutable experiment artifact，工作区、临时目录与 Downloads
  也无 primary text。因此不由标题或 Pending Focus 构造 co-evolution loop。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、challenger/solver/judge state ownership、task
  generation 与 solution/update control flow、self-judge rubric/calibration、open-ended reward validity、acceptance/
  rollback、implementation、compute-matched baselines、ablations/sensitivity/seeds、reward hacking/collapse、model/data/
  hardware/precision/trajectory length/batch/cost/SLO、limitations 与 failure recovery 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在 paper、judge contract 与 versioned artifact
  可审计时重试；Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### Harness Updating Is Not Harness Benefit — 26/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`HARNESS-UPDATING-VS-HARNESS-BENEFIT`；W22；
  arXiv:2605.30621，既有 discovery ledger 记录 first-public 2026-05-28。
- **Verified Access / Artifact Boundary**：Sources 只列当前策略拒绝访问的 arXiv URL；Pending 表的 `+ code`
  没有 repository、owner、release、commit、benchmark split、license 或 run artifact identity，工作区、临时目录与
  Downloads 也无对应材料。不能从题名推断 updater/consumer 分离已经被实验验证。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、updater/consumer/model/harness state ownership、
  update→activation→following control flow、harness identity/versioning、model-tier controls、acceptance/rollback、
  implementation、task construction、baselines/ablations/sensitivity/seeds、failure taxonomy、model/data/hardware/
  precision/trajectory length/batch/cost/SLO、limitations 与 external validity 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在完整 paper、code 与 benchmark identity
  可审计时重试；Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### SAAS over-search mitigation — 24/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`SAAS-OVERSEARCH-MITIGATION`；W22；arXiv:2605.29796，
  既有 discovery ledger 记录 first-public 2026-05-28。
- **Verified Access / Artifact Boundary**：Sources 只列当前策略拒绝访问的 arXiv URL；Pending 表的 `+ code`
  没有 repository、owner、release、commit、search backend、dataset、license 或 run identity，工作区、临时目录与
  Downloads 也无对应材料。不能从标题推断 over-search 的定义、奖励或停止策略。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、policy/search/reward state ownership、
  self-awareness reward、search-depth shaping、stage-wise curriculum、query/result control flow、stop/continue decision、
  live-search freshness/availability、implementation、accuracy/cost Pareto、baselines/ablations/sensitivity/seeds、
  model/data/hardware/precision/length/batch/concurrency/cost/SLO、limitations、reward hacking 与 evidence-loss failures 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在完整 paper、code 与 live-search evaluation
  contract 可审计时重试；Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### RAMP runtime Agent assessment — 25/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`RAMP-RUNTIME-AGENT-ASSESSMENT`；W22；arXiv:2605.27492，
  既有 discovery ledger 记录 first-public 2026-05-26。
- **Verified Access / Artifact Boundary**：Sources 只列当前策略拒绝访问的 arXiv URL；Pending 表的
  `+ platform artifact` 没有 platform URL、owner、release、commit、deployment version、trace schema、license 或
  run identity，工作区、临时目录与 Downloads 也无材料。不能用平台名称或待审字段替代 runtime evidence。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、workflow/run/stage/tool/recovery state ownership、
  serial control flow、checkpoint/resume/retry semantics、utility metrics、resource accounting、failure injection、
  implementation、platform topology、baselines/ablations/sensitivity/seeds、production-transfer sampling、model/data/
  hardware/precision/trajectory length/concurrency/cost/SLO、limitations 与 threat to validity 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在完整 paper 与 versioned platform/run
  artifact 可审计时重试；Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### Masking Stale Observations — 25/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`MASKING-STALE-OBSERVATIONS-AGENT-CONTEXT`；W22；
  arXiv:2606.00408，既有 discovery ledger 记录 first-public 2026-05-29。
- **Verified Access / Artifact Boundary**：Sources 只列当前策略拒绝访问的 arXiv URL；Pending 表的
  `+ trajectories` 没有 dataset URL、owner、revision、schema、split、checksum、license、collection policy 或
  run identity，工作区、临时目录与 Downloads 也无对应材料。不能用 trajectory 标签补造 context-manipulation evidence。
- **Missing Full-read Coverage**：Metadata/revision、全文/Appendix、observation/turn/retrieval state ownership、
  stale-observation definition、masking policy/control flow、retriever/model interaction、token-for-turn allocation、
  inverted-U measurement、implementation、trajectory construction、baselines/ablations/sensitivity/seeds、evidence-loss/
  recovery failures、model/data/hardware/precision/context length/batch/cost/SLO、limitations 与 external validity 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；不计 Full Source Review，不分配 ROADMAP/Books owner，
  不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在完整 paper 与 versioned trajectory artifact
  可审计时重试；Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### ResearchClawBench — 25/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`RESEARCHCLAWBENCH-END-TO-END-RESEARCH-EVALUATION`；W22；
  arXiv:2606.07591，arXiv v1 date 已在 W24 spillback ledger 核验为 2026-05-28，因此归 W22。
- **Verified Access / Artifact Boundary**：相邻周只证明 event-date dedup；本周 Sources 的 arXiv URL 当前被策略
  拒绝访问。Pending 表的 `+ benchmark/code` 没有 repository、dataset、release、commit、task split、grader version、
  checksum、license 或 run identity，工作区、临时目录与 Downloads 也无材料，故不能把展示页归档当全文证据。
- **Missing Full-read Coverage**：完整 metadata/revision、全文/Appendix、task/source/experiment/artifact provenance、
  literature→hypothesis→execution→artifact chain、environment/tool state、grader rubric/calibration、human agreement、
  contamination/decontamination、implementation、baselines/ablations/sensitivity/seeds、cost/reproducibility、model/data/
  hardware/precision/trajectory length/concurrency/SLO、limitations 与 benchmark governance 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；日期回拨已核验，但不计 Full Source Review、不分配
  ROADMAP/Books owner、不修改 Books，也不阻塞 W22 forward cursor。W30 forward sweep 后仅在完整 paper、versioned
  benchmark/code 与 grader contract 可审计时重试；Historical Evidence Gate 保持 Open、Historical Books Gate 保持 Closed。

### Smaller Models Are Natural Explorers — 25/30 — Unverified / Blocked Backlog

- **Candidate / Week / Source Family**：`SMALLER-MODELS-NATURAL-EXPLORERS`；W22；arXiv:2605.30789，
  v1 date 已由 W25 spillback ledger 回拨为 2026-05-29。
- **Verified Access / Artifact Boundary**：相邻周只证明 event-date dedup；本周 Sources 的 arXiv URL 当前被策略
  拒绝访问，没有 author repository、rollout dataset、model card、checkpoint、training configuration 或 immutable
  experiment artifact，工作区、临时目录与 Downloads 也无 primary text。论文标题不证明 scale 与 exploration 的因果关系。
- **Missing Full-read Coverage**：完整 metadata/revision、全文/Appendix、small/large policy ownership、exploration/
  exploitation metric、policy-level diversity、rollout collection、annealing 与 off/on-policy boundary、teacher/student
  control flow、implementation、compute-matched baselines、ablations/sensitivity/seeds、quality/cost trade-off、model/data/
  hardware/precision/length/batch/concurrency/SLO、limitations、capacity confound 与 external validity 均未读取。
- **Disposition / Gate Effect**：`Unverified / Blocked Backlog`；日期回拨已核验，但不计 Full Source Review、不分配
  ROADMAP/Books owner、不修改 Books，也不阻塞 forward cursor。W22 current-review queue 因此清零，forward cursor
  进入 W23；W30 sweep 后仅在完整 paper 与 versioned artifact 可审计时回补。Historical Evidence Gate 保持 Open、
  Historical Books Gate 保持 Closed。

### NVIDIA Dynamo Snapshot — 29/30 — Full Review Complete

- **Candidate / Source Family / Date**：`NVIDIA-DYNAMO-SNAPSHOT`；NVIDIA Technical Blog 2026-05-27，
  联读 Dynamo Snapshot docs、CRIU、`cuda-checkpoint` 与 vLLM/SGLang quiesce hooks，访问日 2026-08-12。
  这是 early prototype / preview；未 upstream 的 CRIU optimizations 与未来 multi-GPU/TensorRT-LLM support
  不写成当前稳定事实。
- **Original Problem / Previous Design / Changed Constraint**：从 image + weights 冷启动可重建、可移植，
  在稳定容量和分钟级 rollout 中合理；弹性 inference 遇到 traffic burst 时，weight load、kernel warmup、graph
  compile 与 distributed-runtime setup 让已经分配的 GPU 长时间不产 token，capacity arrival 晚于 SLO deadline。
- **Mechanism / State Ownership / Flow**：readiness 后先由 workload hook quiesce，释放 non-checkpointable
  distributed resources；`cuda-checkpoint` 把 CUDA context/streams/device mappings 导出到 host process memory，
  CRIU 保存 CPU process tree、files/namespaces 与 container writable layer。restore 由 privileged node
  DaemonSet 创建 placeholder pod、恢复 filesystem/process/device state，再由 resume hook 重建 external
  connections。KV physical allocation 在未服务请求的 snapshot 中被 unmap/release，但保留 baked into CUDA
  graph 的 virtual address；GMS/parallel restore 等路径把 large weights 与 process state 的传输进一步拆开。
- **Evidence Contract / Non-proof**：官方实验覆盖 single-GPU vLLM 0.20.0、Qwen3-0.6B/8B 与 gpt-oss-120b
  等指定模型/硬件/storage setup；例如 Qwen3-0.6B B200 artifact 在 KV unmap 后约 190 GiB→6 GiB。headline
  startup multiplier 不外推；文章明确 CRIU parallel/AIO patches 尚未 upstream，overlay 很小，multi-GPU/
  multi-node、network identity、live traffic、tenant isolation 与 production failure rate 未验证。
- **Trade-offs / Failure Modes / Previous Design**：获得 warm execution-state reuse，却新增 privileged agent、巨大
  artifact、compatibility matrix、credential/file descriptor freshness、GPU identity/topology mismatch、stale
  connections、snapshot tampering 与 quiesce correctness。普通 cold start 在模型小、更新频繁、跨硬件迁移或
  trust/portability 优先时仍合理；prewarmed replicas 与 weight-only cache 也是更简单 alternatives。
- **Evolution / ROADMAP / Decision**：`image+weight reconstruction -> prewarmed replica -> weight/engine cache ->
  host+device execution snapshot -> distributed recoverable serving artifact` 是 `Direct Evolution`。已读 Ch31、
  Ch45～46、Ch52～55；主 owner 暂定 Ch46/53 refine / Experimental，Ch31/55 只接 artifact identity、signing、
  compatibility 与 lifecycle handoff。Historical Books Gate 关闭。

### DynoSim Serving-Stack Digital Twin — 29/30 — Full Review Complete

- **Candidate / Source Family / Date**：`NVIDIA-DYNOSIM-DYNAMO-TWIN`；NVIDIA Technical Blog 2026-05-29，
  联读 Dynamo Mocker/Router/Planner/KVBM references，访问日 2026-08-12。当前公开材料是官方工程说明，
  不是独立 peer-reviewed validation。
- **Problem / Previous Design / Changed Constraint**：单 engine throughput model 对少量 static settings 便宜；
  当 TP、PD split、worker count、scheduler、router、KV tiers、autoscaling 与 topology 互相作用时，局部 kernel
  improvement 会把 bottleneck 移到 queue、transfer 或 planner，逐项实机搜索成本过高。
- **Mechanism / Ownership / Flow**：discrete-event virtual clock 将 arrival、scheduler pass、forward timing、KV
  transfer、worker startup 与 Planner action 放入同一 event queue。backend-specific mocker 决定 batch/chunk/
  preemption/retraction，AIC 只提供 chosen pass timing；multi-engine Router/Planner/KVBM 根据当前 simulated
  cache/load/SLA state 产生新 events。trace collector 输出 throughput、TTFT、TPOT、E2E latency、reuse 与 cost，
  optimizer/agent 只在此 evidence loop 中提配置或代码候选，真实 cluster 是外层 validation owner。
- **Evaluation Contract / Evidence Boundary**：公开案例包括 23,608-request Mooncake FAST25 toolagent trace、
  MiniMax-M2.5 FP8 / HGX B200 / TP=4 / vLLM 0.14.0 / ISL=OSL=1K，以及另一组 Qwen3-32B TP=2 H200
  planner experiment。scheduler-aware replay 比 timing-only 更贴近该 contract 的 hardware observations；但
  simulation 不是 bit-exact emulator，reported Pareto/thresholds 不能外推到其他 workload、backend、topology、
  failures、transfer contention 或 software revision。
- **Trade-offs / Failure Modes / Previous Design**：simulation 让广搜便宜，却把 calibration drift、trace bias、
  missing rare failure、model discrepancy、optimizer overfit 与 direct-apply risk 带进控制面。Analytical model 在
  rough capacity planning 仍合理；microbenchmark 用于 kernel truth；shadow/canary/real-cluster replay 仍是 promotion
  gate。不得让 same simulator 同时生成候选并独占最终 verdict。
- **Evolution / ROADMAP / Decision**：`analytical capacity model -> engine timing model -> scheduler-aware replay ->
  full-stack discrete-event twin -> simulate-first / hardware-verify outer loop` 是 `Direct Evolution`。已读 Ch48、
  Ch52、Ch62～64；主 owner 暂定 Ch62 refine，因长期缺口是 simulation evidence 的 calibration/promotion contract；
  Ch48/52 只接具体 component state。Historical Books Gate 关闭。

### NVIDIA DOCA In-Silicon Security — 27/30 — Full Review Complete

- **Candidate / Source Family / Date**：`NVIDIA-DOCA-BLUEFIELD-SECURITY-PLANE`；NVIDIA Technical Blog
  2026-05-31，联读 DOCA Argus/Flow references，访问日 2026-08-12；为厂商工程证据，性能 headline 未获独立复核。
- **Problem / Previous Design / Changed Constraint**：host agent 能直接读取 OS state、易部署，在 host 尚可信且
  load 可接受时合理；若被保护 host 已被攻陷，monitor 与 enforcement 共享 failure/trust domain，攻击者可篡改
  telemetry、禁用 agent 或利用高负载隐藏行为。
- **Mechanism / Ownership / Flow**：BlueField DPU 形成独立、attestable execution domain。Argus 经限定 DMA 读取
  kernel-version-specific memory structures并产生 event/alert；Vault 在 storage/file path 执行 zero-trust access；
  Flow 在 infrastructure/network layer 执行 policy。DPU 拥有 sensor/enforcement state，host 是被观察对象，XDR/
  control plane 拥有 correlation/response decision；AI analysis 不能绕过 deterministic policy owner。
- **Evidence / Non-proof / Trade-offs**：公开 material 证明 product architecture 与 declared interfaces，不证明
  “无法绕过”、所有 host/kernel layout 正确、DMA inspection 无 privacy/availability risk，亦不验证 `1000x`、
  `800 Gb/s` 在任意 policy/workload 下成立。独立 plane 提高 tamper resistance，却新增 firmware/root-of-trust、
  policy sync、DPU compromise、opaque false positives、forensic retention、DMA blast radius 与 fail-open/closed
  选择。host-based EDR 对 application semantics、无 DPU 环境或快速规则更新仍必要。
- **Evolution / ROADMAP / Decision**：`host-local sensor -> isolated infrastructure sensor -> DPU enforcement ->
  shared telemetry with deterministic response` 是 `Layering / Dependency`。已读 Ch63、Ch67～69；主 owner 暂定
  Ch68 refine / Official Engineering Evidence，Ch63 接 evidence plane。Historical Books Gate 关闭。

### NVIDIA Vera CPU Agentic-Workload Contract — 25/30 — Full Review Complete

- **Candidate / Source / Mechanism**：`NVIDIA-VERA-CPU-AGENTIC-WORKLOAD`；NVIDIA Technical Blog 2026-05-31，
  访问日 2026-08-12。Agent/RL loop 把 sandboxed code、tools、retrieval/data processing、results computation 与
  orchestration 放在 CPU critical path；88 Olympus cores、branch prediction、wide OoO、SCF 与 LPDDR5X memory
  是对此 workload 的厂商 co-design response。
- **Evidence Boundary / Trade-offs**：`1.8x sandbox`、IPC/memory/power 数字缺少完整 competitor、compiler、
  workload mix、concurrency、tail latency、GPU idleness 与 end-to-end token/SLO contract，只保留 component-role
  evidence。高单核+高并发可减少 sequential tool stalls，却不能解决 external API wait、sandbox startup、GPU
  queue 或 workflow dependency；x86/Grace 在已有 fleet、软件兼容和成本边界下仍成立。
- **Evolution / ROADMAP / Decision**：`GPU-centric token path -> CPU-GPU alternating workflow -> role-specific
  CPU co-design -> workflow-visible heterogeneous scheduling` 是 `Layering / Dependency`。已读 Ch50、Ch59、
  Ch77/80；主 owner 暂定 Ch50 refine / Official Engineering Evidence，Agent chapters 只接 workload shape。

### NVIDIA DSX OS AI-Factory Control Plane — 25/30 — Full Review Complete

- **Candidate / Source / Mechanism**：`NVIDIA-DSX-OS-AI-FACTORY-CONTROL`；NVIDIA Technical Blog 2026-05-31，
  联读 DSX component/docs/GitHub links，访问日 2026-08-12。DSX Exchange 以 MQTT bridge 让 grid/power/cooling/
  thermal 与 software workload signals 相互可见；MaxLPS/Flex 把 power/grid response 变成 policy input；Infra
  Controller/DOCA 管 bare-metal lifecycle 与 tenant boundary；Fleet Intelligence 提供 health/integrity；MCP
  surface 只提供 tool discovery，不自动授予 operational authority。
- **Evidence Boundary / Trade-offs**：官方 material 证明 product/component map 与公开入口，不证明全套已在同一
  production deployment interoperable，也不保留 `40% more GPUs`、time-to-revenue 等缺完整 facility/workload/
  SLO contract 的 claims。统一 IT/OT plane 获得 cross-domain correlation，却新增 schema/time synchronization、
  control-loop oscillation、facility safety、credential/tool authority、vendor coupling 与 correlated failure。
- **Evolution / ROADMAP / Decision**：`separate facility/IT dashboards -> shared event bus -> policy-linked power/
  lifecycle/health controllers -> Agent-accessible but authorization-gated operations` 是 `Layering / Dependency`。
  已读 Ch53、Ch63、Ch65～69、Ch79；主 owner 暂定 Ch53/63 refine / Official Engineering Evidence，Ch79 只接
  MCP transport boundary。Historical Books Gate 关闭。

### NVIDIA STAC-AI LANG6 Workload Contract — 23/30 — Full Review Complete

- **Candidate / Source / Coverage**：`NVIDIA-STAC-AI-LANG6-2026-05`；NVIDIA official 2026-05-27，联读
  STAC LANG6 benchmark description。已核对 Llama 3.1 8B/70B、EDGAR4/5、batch/interactive modes、GH200
  FP8、B200/RTX PRO 6000 NVFP4、TensorRT-LLM runtime 与 throughput/interactivity distinction。
- **Evidence Boundary / Decision**：结果只证明 audited/declared hardware-software-model-dataset/precision modes；
  derived per-GPU comparison、vendor-selected configs 与不同 quantization 不能变成架构通用倍率，OpenShift 的
  “no measurable overhead”也只属于相应 submission。Ch62 已明确 workload contract 与 benchmark 不等于 production
  SLO，故 `No Change — Already Covered`；保留作为完整 benchmark-contract case，不复制数字到 Books。

## Post-forward blocked retry — 2026-08-12

本检查点按周内顺序把 27 个 blocked candidates 分成三批，逐一重试既有 ledger 中的精确 arXiv HTML
入口：AgentDoG 1.5、How LoRA Remembers?、MemTrace、CUA-Gym、LaRA、FluxMem、Skill0.5、SkillGrad、
Claw-Anything；Crafter、Domino、COLLEAGUE.SKILL、GrepSeek、TASTE、Trust-Region Behavior Blending、
Trust Region On-Policy Distillation、LongTraceRL、dMoE；SkillAdaptor、Draft-OPD、SCOPE、Harness Updating Is
Not Harness Benefit、SAAS、RAMP、Masking Stale Observations、ResearchClawBench、Smaller Models Are Natural
Explorers。27 个入口均未返回可验证的 primary paper text。

2026-08-13 再次重试时，27 个 HTML 入口已全部恢复。上文 Recovery Addendum 已逐项记录机制、状态边界、
evaluation/limitations、trade-off、章节 owner 与 provisional disposition；旧的 2026-08-12 失败结果只保留作
访问历史。W22 当前为 42/42 `20+` Full Source Reviews、0 blocked / pending；cross-index discovery 仍使
Historical Evidence Gate 保持 Open，Books Gate 保持 Closed。

## Pending Full Source Review Queue

| Candidate | First-public Date | Primary Source | Pending Focus |
| --- | --- | --- | --- |

## Repository Changes

- 2026-08-14 完成 43/43 final disposition 与 17-owner review，并实际 refine Ch25、Ch30、Ch48、Ch50、
  Ch66、Ch72、Ch76、Ch77、Ch84；下方 2026-08-13 以前的“Books Gate unchanged / 未追加 Books”只描述
  当时检查点，已由最终账本 supersede。
- 2026-08-13 重新逐行复算为 43 scored（30 high、12 mid、1 low）：42/42 当前 `20+` Source
  Reviews、0 blocked / ordinary pending、1 个低分事实边界。27 个旧 blocker 的 HTML 全部恢复并完成
  non-template review；broader discovery 与 Books Gate 状态不变。
- W22 从 3 个 baseline 扩展为 43 个 scored families；ScientistOne 的既有全文/Appendix/artifact/
  adjacent-chapter review 已归正到 v1 first-public 周，Gamma-World 已完成全文、Appendix、官方
  project/repository 与相邻章节复核；AgentDoG 1.5 因 44 页 primary text 当前不可读转入
  `Unverified / Blocked Backlog`；DVAO 完成唯一 v1、三项理论证明、dual-objective evaluation、
  implementation/limitations 与 Ch28～30 邻接，暂定 Ch29 refine / Experimental，并保留基础权重、小 group、
  noisy high-variance reward、三目标以上、无 multi-seed/CI/code 的边界；OmniRetrieval 已覆盖唯一 v1、
  heterogeneous source-native routing/query/execution/selection、13-dataset evaluation、official current code 与
  Ch71/72/74 邻接，暂定 Ch72 refine / Experimental；single-gold-source、single-best-candidate、无 freshness/ACL/
  query-safety/failure/provenance/production-SLO contract 的边界保持显式；MobileGym 已覆盖 v1/v2、完整正文/
  Appendices、official project/repository 与 Ch61～63/29/80 handoff，暂定 Ch62 refine / Experimental；其 structured
  state control plane、deterministic judge、side-effect diff 与 grouped rollout 机制被保留，59-task selected real-device
  subset、surrogate/backend gap、shared simulator/judge specification 和 workload-specific efficiency 边界保持显式；
  BES 已覆盖唯一 v1、全部 Appendices、theory assumptions、三个 experiment contracts、ablation/cost、official
  project/repository 与 Ch19～21/29/75/77 去重，暂定 Ch20 refine / Experimental；其 candidate-pool/operator/
  backward-goal-tree state 被保留，而 entropy-shell 不等于 correctness、independent-subgoal/reliable-verifier assumptions、
  task-specific implementation、最大 8B post-training、3-seed program search 与 compute-accounting 缺口保持显式；
  ResearchMath-14K 已覆盖唯一 v1、全部 Appendices、current dataset card/files/history 与 Ch22～25/62 去重，
  暂定 Ch23 refine / Experimental；保留 source quote→rewrite→status evidence→teacher attempt→filter verdict 的
  lineage，而 model-judge correlated error、filter-definition ambiguity、current public artifact 缺口、split/card inconsistency、
  source license/status supersession、decontamination 与完整 training contract 保持显式；How LoRA Remembers? 因
  arXiv primary text 被当前允许路径拒绝访问转入 `Unverified / Blocked Backlog`，不计 Full Source Review、不推断机制、
  不分配 Books owner；MemTrace 的 arXiv 与 Hugging Face paper surface 亦被权限拒绝，本地无可审计正文或作者
  artifact，故同样转入 blocked backlog，不把 taxonomy/attribution/intervention pending focus 当证据；CUA-Gym 的 arXiv
  与最直接 QwenLM/CUA-Gym official artifact surface 亦被保存权限拒绝、本地无正文或 artifact，故不推断 environment/
  verifier/RL 机制并转入 blocked backlog；LaRA 只有同一受限 arXiv primary-source surface，本地无正文或 artifact，
  故不把 geometry/contamination/RL-vs-SFT/false-positive pending focus 当证据并转入 backlog；FluxMem 的 arXiv
  正文同样受限，`planned code` 没有可审计 artifact identity，本地也无对应材料，故不推断 connectivity/feedback/
  pruning/consolidation 并转入 backlog；Skill0.5 的 Sources 只有受限 arXiv URL，`+ code` 无 repository/release/commit
  identity 且本地无 artifact，故不推断 internalize/externalize router、difficulty/OOD 或 conflict semantics 并转入 backlog；
  SkillGrad 的 `+ code` 同样无 repository/release/commit identity，本地也无材料，故不推断 textual-gradient/momentum/
  patch/held-out mechanisms 并转入 backlog；Claw-Anything 只有受限 arXiv URL 且本地无 artifact，故不推断
  always-on authority/privacy/proactivity/environment semantics 并转入 backlog；Crafter 的 `+ code/benchmark` 无
  repository/dataset/release/commit identity 且本地无 artifact，故不推断 roles/SVG/verifier/visual evaluation 并转入 backlog；
  Domino 的 `+ code` 无 repository/release/commit identity 且本地无材料，故不推断 backbone/head/curriculum/
  acceptance/backend mechanisms 并转入 backlog；COLLEAGUE.SKILL 的 `open-source artifact` 无 URL/owner/release/
  commit identity 且本地无材料，故不推断 trace distillation、capability/behavior、correction/rollback 或 measured claims；
  GrepSeek 的 `+ code` 无 repository/release/commit/data/model identity 且本地无材料，故不推断 Tutor/Planner/GRPO/
  sandbox/byte-equivalence mechanisms；TASTE 的 `+ benchmark` 无 repository/dataset/release/split/version identity 且本地
  无材料，故不推断 generation/judge/coverage/difficulty/contamination/grader mechanisms；Trust-Region Behavior Blending
  只有受限 arXiv source 且本地无材料，故不推断 KL/annealing/prefix/two-setting/stability mechanisms；Trust Region
  On-Policy Distillation 同样只有受限 arXiv source、本地无材料，故不推断 region/KL/mask/clip/off-policy mechanisms；
  LongTraceRL 的 `+ code/data/models` 无 immutable identity 且本地无材料，故不推断 distractor/rubric/reward-hacking/
  contamination mechanisms；dMoE 的 `+ code` 无 immutable identity 且本地无材料，故不推断 block/expert
  distribution、state ownership、memory traffic、runtime 或 quality/latency contract；SkillAdaptor 只有 planned-code
  占位且本地无材料，故不推断 fault attribution、skill responsibility、acceptance、rollback 或 benchmark claims；
  Draft-OPD 只有受限 arXiv surface，故不推断 target-assisted rollout、verification-error replay、on-policy signal
  或 acceptance/throughput contract；SCOPE 只有受限 arXiv surface，故不推断 challenger/solver state、
  co-evolution、self-judge、open-ended reward 或 compute-matched evidence；Harness Updating 的 `+ code` 无
  immutable identity 且本地无材料，故不推断 updater/consumer、activation/following、model-tier controls 或
  harness identity；SAAS 的 `+ code` 无 immutable identity 且本地无材料，故不推断 self-awareness reward、
  search-depth shaping、curriculum、accuracy/cost Pareto 或 live-search validity；RAMP 的 platform artifact 无
  URL/version/run identity 且本地无材料，故不推断 workflow identity、recovery、utility/resource accounting 或
  production transfer；Masking Stale Observations 的 trajectories 无 URL/version/schema identity 且本地无材料，
  故不推断 inverted-U、retriever/model interaction、token-for-turn trade-off 或 evidence-loss failures；
  ResearchClawBench 的 benchmark/code 无 immutable identity 且本地无材料，故只保留 W24→W22 日期回拨，
  不推断 research chain、grader validity 或 contamination；Smaller Models Are Natural Explorers 只有受限 arXiv
  surface，故只保留 W25→W22 日期回拨，不推断 scale→exploration、policy ownership、annealing 或 rollout compute。
  current-review queue 已清零，forward cursor 进入 W23；W22 feed 中
  6 个 W21 spillbacks 已回拨，W23 feed 回收 16 个 W22 spillbacks，W24/W25 feed 又回收
  ResearchClawBench 与 Smaller Models Are Natural Explorers。既有 Ch63 privacy handoff 与
  Ch62 claim-provenance 内容保留；fixed official / Infra replay 又完成 Dynamo Snapshot、DynoSim、DOCA、
  Vera CPU、DSX OS 与 STAC-AI 六项非模板化审计，本轮未追加 Books。

## Open Questions

1. Agent telemetry 的哪些诊断必须保留 per-session detail，哪些可以安全聚合？
2. 同周还有哪些 private telemetry、attestation、secure aggregation 或 privacy-accounting primary
   sources 可形成交叉验证？
3. 已恢复的 27 个旧 blocker 中，哪些 Experimental mechanism 能在独立复现后从受限案例升级为稳定设计分支？
4. fixed official/infra release scan 是否恢复影响 deployment contract 的同周事件？
5. Gamma-World 的训练数据 manifest/license、4/8+ agent quantitative quality、action-intervention
   checker、long-horizon physics consistency 与完整 24-FPS latency/SLO contract 能否获得交叉证据？
6. Dynamo Snapshot 怎样对 artifact signing、GPU/topology compatibility、credential/network freshness、quiesce/
   resume failure 与 multi-node state 建立可验证 restore contract？
7. DynoSim 怎样防止 trace/calibration drift 与 optimizer-overfit；哪些 policies 必须在 shadow/real cluster 外层
   validation 后才能 promotion？
8. DPU security plane 的 DMA scope、firmware/root-of-trust、policy version、fail-open/closed、forensic retention
   与 host/DPU correlated failure 怎样验证？

## Sources

- Anthropic Research index, coding-agents entry dated 2026-05-27:
  https://www.anthropic.com/research
- Google Research May 2026 archive: https://research.google/blog/2026/05/
- OpenAI Research release index, biodefense entry dated 2026-05-29:
  https://openai.com/research/index/release/
- NVIDIA Dynamo Snapshot（published 2026-05-27；accessed 2026-08-12）:
  https://developer.nvidia.com/blog/nvidia-dynamo-snapshot-fast-startup-for-inference-workloads-on-kubernetes/
- Dynamo release/docs surface（accessed 2026-08-12）: https://github.com/ai-dynamo/dynamo/releases
- NVIDIA cuda-checkpoint（accessed 2026-08-12）: https://github.com/NVIDIA/cuda-checkpoint
- DynoSim（published 2026-05-29；accessed 2026-08-12）:
  https://developer.nvidia.com/blog/dynosim-simulating-the-pareto-frontier/
- NVIDIA DOCA in-silicon security（published 2026-05-31；accessed 2026-08-12）:
  https://developer.nvidia.com/blog/advancing-ai-infrastructure-for-agentic-ai-with-nvidia-doca-in-silicon-security/
- NVIDIA Vera CPU agentic-workload contract（published 2026-05-31；accessed 2026-08-12）:
  https://developer.nvidia.com/blog/nvidia-vera-cpu-sets-a-new-standard-for-agentic-workloads-in-ai-factories/
- NVIDIA DSX OS（published 2026-05-31；accessed 2026-08-12）:
  https://developer.nvidia.com/blog/nvidia-dsx-os-delivers-open-modular-software-for-operating-ai-factories-at-scale/
- NVIDIA STAC-AI LANG6（published 2026-05-27；accessed 2026-08-12）:
  https://developer.nvidia.com/blog/nvidia-blackwell-sets-stac-ai-record-for-llm-inference-in-finance/
- Hugging Face Papers, 2026-W22 discovery index: https://huggingface.co/papers/week/2026-W22
- ScientistOne paper: https://arxiv.org/abs/2605.26340
- ScientistOne HTML: https://arxiv.org/html/2605.26340
- Google Research ScientistOne explanation (W31 publication node):
  https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/
- Gamma-World metadata: https://arxiv.org/abs/2605.28816
- Gamma-World full paper: https://arxiv.org/pdf/2605.28816
- NVIDIA Gamma-World project: https://research.nvidia.com/labs/sil/projects/gamma-world/
- Gamma-World official repository: https://github.com/nv-tlabs/Gamma-World
- Gamma-World training guide: https://github.com/nv-tlabs/Gamma-World/blob/main/docs/training.md
- Gamma-World inference guide: https://github.com/nv-tlabs/Gamma-World/blob/main/docs/inference.md
- AgentDoG 1.5: https://arxiv.org/abs/2605.29801
- DVAO metadata: https://arxiv.org/abs/2605.25604
- DVAO full HTML: https://arxiv.org/html/2605.25604v1
- DVAO full paper: https://arxiv.org/pdf/2605.25604
- OmniRetrieval: https://arxiv.org/abs/2605.29250
- OmniRetrieval full HTML: https://arxiv.org/html/2605.29250v1
- OmniRetrieval full paper: https://arxiv.org/pdf/2605.29250
- OmniRetrieval official repository: https://github.com/JinheonBaek/OmniRetrieval
- OmniRetrieval retrieval implementation:
  https://github.com/JinheonBaek/OmniRetrieval/blob/main/src/model/retrieval.py
- MobileGym: https://arxiv.org/abs/2605.26114
- MobileGym v1 HTML: https://arxiv.org/html/2605.26114v1
- MobileGym v2 HTML: https://arxiv.org/html/2605.26114v2
- MobileGym paper: https://arxiv.org/pdf/2605.26114
- MobileGym official project: https://mobilegym.dev/
- BES metadata: https://arxiv.org/abs/2605.28814
- BES full HTML: https://arxiv.org/html/2605.28814v1
- BES full paper: https://arxiv.org/pdf/2605.28814
- BES official project: https://guoweixu.com/bes/
- BES official repository: https://github.com/Embodied-Minds-Lab/BES
- ResearchMath-14K metadata: https://arxiv.org/abs/2605.28003
- ResearchMath-14K full HTML: https://arxiv.org/html/2605.28003v1
- ResearchMath-14K full paper: https://arxiv.org/pdf/2605.28003
- ResearchMath-14K official dataset: https://huggingface.co/datasets/amphora/ResearchMath-14k
- ResearchMath-14K dataset files: https://huggingface.co/datasets/amphora/ResearchMath-14k/tree/main
- ResearchMath-14K dataset history: https://huggingface.co/datasets/amphora/ResearchMath-14k/commits/main
- MobileGym official repository: https://github.com/Purewhiter/mobilegym
- Bidirectional Evolutionary Search: https://arxiv.org/abs/2605.28814
- ResearchMath-14K: https://arxiv.org/abs/2605.28003
- How LoRA Remembers?: https://arxiv.org/abs/2605.30260
- MemTrace: https://arxiv.org/abs/2605.28732
- CUA-Gym: https://arxiv.org/abs/2605.25624
- LaRA: https://arxiv.org/abs/2605.29888
- FluxMem: https://arxiv.org/abs/2605.28773
- Skill0.5: https://arxiv.org/abs/2605.28424
- SkillGrad: https://arxiv.org/abs/2605.27760
- Claw-Anything: https://arxiv.org/abs/2605.26086
- Hugging Face Papers, 2026-W23 curation-lag cross-check: https://huggingface.co/papers/week/2026-W23
- Crafter: https://arxiv.org/abs/2605.30611
- Domino: https://arxiv.org/abs/2605.29707
- COLLEAGUE.SKILL: https://arxiv.org/abs/2605.31264
- GrepSeek: https://arxiv.org/abs/2605.29307
- TASTE: https://arxiv.org/abs/2605.28556
- Trust-Region Behavior Blending: https://arxiv.org/abs/2605.31159
- Trust Region On-Policy Distillation: https://arxiv.org/abs/2606.01249
- LongTraceRL: https://arxiv.org/abs/2605.31584
- dMoE: https://arxiv.org/abs/2605.30876
- SkillAdaptor: https://arxiv.org/abs/2606.01311
- Draft-OPD: https://arxiv.org/abs/2605.29343
- SCOPE: https://arxiv.org/abs/2605.31433
- Harness Updating Is Not Harness Benefit: https://arxiv.org/abs/2605.30621
- SAAS: https://arxiv.org/abs/2605.29796
- RAMP: https://arxiv.org/abs/2605.27492
- Masking Stale Observations: https://arxiv.org/abs/2606.00408
- ResearchClawBench: https://arxiv.org/abs/2606.07591
- Smaller Models Are Natural Explorers: https://arxiv.org/abs/2605.30789

## 2026-08-14 Final Source-Family Books Integration Ledger

最终计数为 43/43：38 Refine、3 No Change、2 Weekly Only。旧 access-failure 段落已由 27 项
Primary-Text Recovery Addendum supersede，不再产生 blocked disposition。

| Source Family | Final Disposition | Stable Owner | Current / Legacy | Books Review Result |
| --- | --- | --- | --- | --- |
| Private analytics via zero-trust aggregation | No Change | `PLATFORM-MONITORING` | Ch67 / Ch63 | 原始 telemetry ownership、aggregate/verbose 分层与 threat-model boundary 已具体覆盖 |
| Coding agents in social sciences | Weekly Only | — | — | 使用观察，不足以形成新的 system mechanism |
| Rosalind biodefense access expansion | Weekly Only | — | — | Access-policy fact；不等于 safety mechanism 已披露 |
| Gamma-World | Refine | `MULTIMODAL-WORLD-MODELS` | Ch25 / N/A | shared scene 与 per-agent state 分离，保留 intervention/identity 与未观测意图边界 |
| AgentDoG 1.5 | Refine | `PLATFORM-SECURITY` | Ch72 / Ch68 | taxonomy、trajectory identity、training guardrail 与 final-delivery guardrail 分层复核 |
| DVAO | Refine | `TRAIN-GRPO` | Ch33 / Ch29 | multi-reward group variance weighting 是 reward-side state，不升级为通用稳定性保证 |
| OmniRetrieval | Refine | `AGENT-RAG` | Ch76 / Ch72 | 统一 query plan，保留 source-native operators、ACL、partial failure 与 provenance |
| MobileGym | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | structured resettable state、deterministic verifier 与 real-backend transfer gap |
| Bidirectional Evolutionary Search | Refine | `MODEL-SAMPLING` | Ch20 / Ch20 | step pool、backward goal tree 与 recombination；可靠 verifier/independence 是前提 |
| ResearchMath-14K | Refine | `TRAIN-DATA` | Ch27 / Ch23 | source→rewrite→status→attempt→filter lineage；mutable truth 与 correlated judge 不被抹平 |
| How LoRA Remembers? | Refine | `TRAIN-LORA` | Ch30 / Ch26 | exact recall 的 stubborn-token boundary；不外推 8B greedy phase transition |
| MemTrace | Refine | `AGENT-MEMORY` | Ch77 / Ch73 | frozen graph counterfactual intervention用于 fault triage，不把 attribution 当因果真值 |
| ScientistOne / Chain-of-Evidence | No Change | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | claim→evidence→test→update 与 verifier-first evidence chain 已覆盖 |
| CUA-Gym | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | session-isolated state、setup/reward ownership 与 terminal-state verifier 限制 |
| LaRA | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | representation perturbation 是 contamination sensor，不是 causal memorization proof |
| FluxMem | Refine | `AGENT-MEMORY` | Ch77 / Ch73 | immutable items→online connections→topology edit→offline consolidation |
| Skill0.5 | Refine | `AGENT-PLATFORM` | Ch84 / Ch80 | parametric general Skill 与 state-conditioned external Skill 并存 |
| SkillGrad | Refine | `AGENT-PLATFORM` | Ch84 / Ch80 | diagnosis/patch/momentum 只作 operational analogy，必须 regression/rollback |
| Claw-Anything | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | always-on subject identity需联合 event、service、GUI/CLI 与 proactive trigger |
| Crafter | Refine | `AGENT-WORKFLOW` | Ch81 / Ch77 | structured directive 与 editable artifact 使跨轮 correction 可追踪 |
| Domino | Refine | `INFER-SPECULATIVE-DECODING` | Ch48 / Ch44 | parallel proposal 加轻量 causal correction；不等于解决 on-policy drift |
| COLLEAGUE.SKILL | Refine | `AGENT-PLATFORM` | Ch84 / Ch80 | selected/consented evidence→portable Skill；不复制人格或自动授予 authority |
| GrepSeek | Refine | `AGENT-RAG` | Ch76 / Ch72 | lexical pipeline 是 typed retrieval program，仅安全并行 shard-local transformations |
| TASTE | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | adaptive candidate generation 与 hint-assisted verifier 必须分 owner |
| Trust-Region Behavior Blending | Refine | `TRAIN-SFT` | Ch29 / Ch25 | teacher behavior 只在 warmup trust region 内介入，保留纯 student 分支 |
| Trust Region On-Policy Distillation | Refine | `TRAIN-SFT` | Ch29 / Ch25 | outlier-region mask/constraint 防止不可靠 ratio 主导，不外推通用 distillation |
| LongTraceRL | Refine | `MODEL-LONG-CONTEXT` | Ch22 / Ch22 | hard distractor、rubric reward 与 evidence selection；污染/reward hacking 仍需审计 |
| dMoE | Refine | `MODEL-MOE` | Ch21 / Ch21 | block-level expert coreset→token routing，动态 expert count新增 dispatch/load state |
| SkillAdaptor | Refine | `AGENT-PLATFORM` | Ch84 / Ch80 | first actionable fault→responsible section→validation-gated patch |
| Draft-OPD | Refine | `INFER-SPECULATIVE-DECODING` | Ch48 / Ch44 | own-policy rollout与 verification-error replay 修复 training distribution mismatch |
| SCOPE | Refine | `TRAIN-GRPO` | Ch33 / Ch29 | Challenger/Solver co-evolution受 rubric/self-judge quality 约束 |
| Harness Updating Is Not Harness Benefit | Refine | `AGENT-PLATFORM` | Ch84 / Ch80 | 固定 backbone，拆开 updater ability、harness revision 与 consumer benefit |
| SAAS | Refine | `AGENT-PLANNING` | Ch79 / Ch75 | search boundary 是 evolving policy state，不用 static penalty 取消搜索 |
| RAMP | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | persistent artifact/checkpoint/retry 与 runtime cost evidence 共同定义 run |
| Masking Stale Observations | Refine | `AGENT-CONTEXT` | Ch75 / Ch71 | retention window 必须按 retriever/model regime 选择，不能成为 universal K |
| ResearchClawBench | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | paper/code/data/experiment/report 分层；榜单不等于模型能力 |
| Smaller Models Are Natural Explorers | Refine | `TRAIN-GRPO` | Ch33 / Ch29 | early small-policy diversity→large-policy transition；容量/熵/compute confound 保留 |
| NVIDIA Dynamo Snapshot | Refine | `INFER-VLLM` | Ch50 / Ch46 | image/weight→quiesced host+device execution snapshot→compatibility-gated restore |
| DynoSim | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | analytical→scheduler-aware digital twin→real-cluster promotion Gate |
| NVIDIA DOCA in-silicon security | Refine | `PLATFORM-SECURITY` | Ch72 / Ch68 | host-local sensor→attested DPU plane→correlated evidence；不宣称不可绕过 |
| NVIDIA Vera CPU workload contract | Refine | `PLATFORM-GPU-SCHEDULER` | Ch63 / Ch59 | Agent CPU/GPU/tool burst进入 heterogeneous workload contract，不保留厂商倍率 |
| NVIDIA DSX OS | Refine | `PLATFORM-FOUNDATIONS` | Ch57 / Ch53 | facility/IT signals→shared event bus→policy controllers；MCP 不授予 authority |
| NVIDIA STAC-AI LANG6 | No Change | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | workload contract、precision 与 benchmark≠production SLO 已具体覆盖 |

### Owner Review

17 个 Stable Node owners 被修改或重新验证。实际正文强化了九条长期路线：多主体 World State、
token-level parametric recall、heterogeneous/programmable retrieval、Memory counterfactual diagnosis、
parallel draft 的 architecture/training 双分支、execution-state restore、独立基础设施安全面、
Skill updater/consumer benefit 分解，以及 digital-twin→真实集群 promotion。其余 Refine 均能定位到
现有章节中的具体论点，没有建立论文列表式附录。

Archive/Discovery Gate 仍因 Scholar/OpenAlex/DBLP cross-index recall 保持 Open；它与已完成的
Source-Family Books Gate 分离。W22 无 blocked、pending 或 Disputed family。
