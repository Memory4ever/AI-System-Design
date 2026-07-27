# AI Research Weekly — 2026-W11

> Coverage Window: 2026-03-09～2026-03-15
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-09
> Re-audit Status: W11 Source-Family Books Gate Passed — 55 scored families; 52/53 `20+` Full Source Reviews, 2/2 low-score verifications; 31 Integrate/Refine dispositions written to 17 owner chapters, 23 No Change/Weekly Only/Emerging dispositions, 1 scored blocker plus 4 unscored blockers retained under the user-approved blocked-skip rule; 0 ordinary Books pending; broader Historical Archive Gate remains open

## Executive Summary

旧版只保留 MTIA 与 Groundsource 两项，并据此写成“没有独立高分系统论文”；该判断未通过
Discovery Recall Gate。按 primary first-public date 重开后，目前 scored ledger 恢复 55 个 W11 候选，覆盖
unsupervised RLVR、online Agent RL、long-context sparse attention、portable SSM compiler、FP4
training、tool-use curriculum、derived memory、executable evaluation 与 production inference runtime。
其中 Dynamo v1.0 GA、IndexCache、MTIA 与 OpenClaw-RL 是当前优先级最高的系统候选，但评分只决定
阅读顺序，不预设 Books 结论。

另外，3 月 9～13 日的推荐流中有 11 篇论文实际在 3 月 2～8 日首次公开。它们不能因 discovery
日期较晚而被塞入 W11，已作为 `W10 spillback` 单列，并要求重新打开 W10 Discovery Gate。W11
当前 scored ledger 中除 Groundsource 外的 52/53 个 `20+` 候选已完成非模板化 Full Source Review；Groundsource 论文
metadata、官方技术长文和公开 dataset 已核验，但 EarthArXiv 正文访问被站点校验与用户侧浏览器权限阻断。
该项因此保持 `Unverified / Blocked`，未完成的全文阅读不与 `Completed` 并存。

RAGEN-2 也从 W15 回拨本周：其 arXiv v1 虽到 4 月 7 日才提交，作者官方 repository 已明确记录 3 月 12 日
release；全文、全部 appendices、project page 与 current code 已审计。随后 W12 的 03-16～03-24
curation-lag 复核又确认 28 个 first-public date 位于 03-09～03-15
的新增 W11 spillbacks，详见 W12 `Cross-Week Spillback Ledger`。因此 31 项只是 prior candidate set，
不能继续代表 W11 周级召回；新增条目尚待逐项评分、去重与 Source Review。

2026-08-12 已把该 ledger 拆成 28 个 candidate-level intake（27 篇论文 + KServe v0.17.0），并完成第一项
EvoScientist。其 sole arXiv v1、21 页正文、IDE/IVE/ESE 三类 memory update、idea/experiment tree、
30-query/6-paper evaluation、ablation、Limitations、Appendix 与后续官方 code surface 已审计，评分 25/30。
其长期机制已经由 Ch73 的 derived-memory governance 与 Ch77 的 executable Workflow/authority boundary
覆盖，故为 `No Change — Already Covered / Experimental Case`。MEMO 也已完成 38 页 current-v2、v1/v2
history、算法、全部实验/消融/Appendix、官方五-commit repository 与 Ch73/62/77/78 邻接审计，评分 25/30，
暂定 `Refine — Existing Argument / Experimental`（Ch73）：它把 trajectory-derived memory、TrueSkill
selection 与 seed-preserving rare-state replay 放进同一 context-optimization loop，同时用消融说明 memory 与
fresh exploration 需要共存；但五个 text games、三次 runs、未披露硬件/总成本、同一 self-play data 的优化与
评测耦合，以及无 provenance/expiry/rollback 的 CRUD memory，禁止外推为通用 Agent 学习结论。
Reasoning as Compression 与 Deep Tabular Research 随后完成 v1/current revision、全文、实验/附录和章节邻接审计：
前者暂定 Ch29 `Refine`，把 uniform token penalty 重新解释为 prior-dependent semantic cost；后者暂定 Ch75
`Refine`，把 macro-path statistics、execution feedback 与 derived experience 组织成可审计的 replanning state。
两项均为 Experimental；在当时的 Source Review 阶段 Historical Books Gate 仍关闭、尚未修改 Books，
该状态随后已由本周最终 Books Integration Decision 取代。FinToolBench 随后完成全文、
Appendix、公开 benchmark artifact 与 Ch62/68/74 邻接审计，结论为 `No Change — Already Covered / Experimental
Evaluation Case`。FineRMoE 的 primary chronology 则显示它在 2025-09-11 已由 OpenReview 首发，不属于 W11，
已转入 2025 cross-year backlog。LookaheadKV、UCIP 与 One-Eval 随后完成 current paper、revision、实现/结果
artifact 和章节邻接审计：LookaheadKV 以 28/30 暂定 Ch41 `Refine — Existing Argument / Experimental`，
UCIP 以 20/30 归为 `No Change — Already Covered / Experimental Evaluation Case`（Ch62）；One-Eval
以 25/30 归为 `No Change — Already Covered / Experimental System Case`（Ch62）。`Safe Web Agent Learning`
无法与 03-10～03-11 原始索引、arXiv 标题或唯一 primary ID 对齐，故按 blocked-skip 规则保留为未评分的
`Unverified / Blocked Identity`。LMEB 与 Video Streaming Thinking 又完成 v1/current revision、全文、
evaluation/limitations、official artifact 与章节邻接审计：前者以 25/30 暂定 Ch73 Experimental refine，
后者以 27/30 暂定 Ch71 Experimental integrate。daVinci-Env / OpenSWE 与 MM-CondChain 又完成论文、
revision、公开 artifact、完整 evaluation contract 与章节邻接审计：前者以 29/30 暂定 Ch23 Experimental
refine，后者以 26/30 暂定 Ch62 Experimental refine。ReBalance、Expert Threshold Routing、BAVT 与
EnterpriseOps-Gym 又完成全文、artifact/evaluation boundary 与章节邻接审计：前三者分别暂定 Ch20、Ch21、
Ch75 Experimental refine；EnterpriseOps-Gym 为 Ch62 `No Change / Experimental Evaluation Case`。EvoClaw /
SWE-Milestone 又完成 v1/current revision、全文、artifact 与章节去重，结论为 Ch62 `No Change / Experimental
Evaluation Case`；TERMINATOR 的 identity、project/model artifact 与 latency surface 已核验，但 full paper/
Appendix 入口不可读，故按 blocked-skip 规则保留未评分。AI Can Learn Scientific Taste、AgentProcessBench 与
V-JEPA 2.1 随后完成 v1/current revision、全文、Appendix、官方 artifact 与章节邻接审计：Scientific Taste
以 27/30 归为 Ch27 `No Change / Experimental Feedback Case`，因为 Community Feedback 只是新的延迟代理来源，
没有越过既有“偏好不是真理、proxy 会 Goodhart”的边界；AgentProcessBench 以 28/30 暂定 Ch62
Experimental refine，补出中性探索、错误传播与 first-error localization 的度量分解；V-JEPA 2.1 以 27/30
暂定 Ch5 Experimental refine，把 dense/local 与 global semantic representation 的目标冲突、deep
self-supervision 修复链写成可审计消融。最后，KServe v0.17.0 的 release、0.17 versioned docs、
LLMInferenceService control/topology contract 与相关 release/PR surface 已联合核验，以 27/30 归为
`No Change — Already Covered / Ch49+57 Versioned Evolution Case`：它是 LLM 专用 CRD、EPP、PD、并行拓扑与
模块化安装走向稳定产品面的重要节点，但现稿已由 0.18 primary docs 完整覆盖长期职责。本次 intake 普通
pending 因而清零；五个 blocked 项按用户确认规则保留 backlog，不阻止 forward candidate checkpoint。

本次 Books Integration 在逐项 owner/adjacent-chapter Review 后完成：55 个评分候选全部获得最终 disposition，
其中 31 个进入 17 个 Stable Knowledge Node，23 个以具体既有论点去重或保留在 Weekly，Groundsource 保持
评分 blocker，另有 4 个未评分 blocked intake。正文只吸收长期机制、状态所有权、演进与 failure mode，未保留
作者 leaderboard 或把单篇性能结果外推为通用结论。W11 独立 Gate 已通过，但它不等于 W01～W32 Archive
Completion；五项材料缺口和其他周的未闭合审计继续保留。

## Coverage and Source Coverage

- 模型与研究机构：恢复 Meta MTIA 详细技术长文与 Google Groundsource 直接项目页；Groundsource
  从“应用新闻”重新定位为 weak-label data construction 与 downstream evaluation contract 候选。
- arXiv / 学术来源：恢复 28 个 first-public date 位于 W11 的论文/技术报告。推荐日期只用于
  discovery，不作为归档日期；v1 metadata、revision 与正文证据分开记录。
- AI Infra：补回 2026-03-12 的 NVIDIA Dynamo v1.0.0 GA。release notes 只证明版本行为；router、
  KV ownership、disaggregation 与 recovery 机制需联合 design docs、代码和已存在的 Dynamo source
  family 核验。
- Discovery feeds：已复核 Hugging Face 2026-03-09～03-13 日索引中的相关条目，并回到 arXiv、
  官方 Blog、官方文档与 repository。原始页面的全量、低相关条目计数尚未做确定性导出，因此不
  虚构“screened total”；当前只声明 55 个已评分 in-window candidate families、0 个 ordinary 待审
  spillbacks、1 个 blocked-identity intake、3 个 blocked-full-text intakes、1 个 cross-year reroute 与
  11 个已核对的 W10 spillbacks。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Four MTIA chips in two years | 3 | 5 | 4 | 5 | 5 | 4 | 26/30 | No Change — `INFER-TENSORRT-LLM` 已覆盖 workload-specific co-design |
| Dynamo v1.0.0 GA | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | No Change — `INFER-DYNAMO` 已覆盖 control/data plane 与 state-aware routing |
| How Far Can Unsupervised RLVR Scale LLM Training? | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | No Change — `TRAIN-GRPO` 已覆盖 zero-advantage、curriculum 与 verifier 边界 |
| OneMillion-Bench | 3 | 3 | 3 | 4 | 4 | 4 | 21/30 | No Change — `PLATFORM-EVALUATION-SYSTEM` 已分离 model/scaffold/tool/judge/outcome |
| Agentic Critical Training | 3 | 4 | 4 | 3 | 4 | 4 | 22/30 | No Change — `TRAIN-RLHF`/`TRAIN-GRPO` 已覆盖 pairwise action quality 与 outcome correction |
| Fish Audio S2 technical report | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Refine — `MULTIMODAL-REPRESENTATION` 分层音频状态机 |
| Test-Driven Agentic Development | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Refine — `AGENT-WORKFLOW` specification compilation 与独立 test gates |
| SoundWeaver | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | No Change — `MULTIMODAL-GENERATIVE-PARADIGMS` 已覆盖 approximate diffusion reuse |
| RetroAgent | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | No Change — `AGENT-MEMORY` 已覆盖 derived memory provenance 与可撤销 view |
| In-Context Reinforcement Learning for Tool Use | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `TRAIN-GRPO` rollout scaffold annealing |
| Thinking to Recall | 3 | 3 | 3 | 4 | 4 | 4 | 21/30 | No Change — `MODEL-SAMPLING`/`AGENT-RAG` 已分离 compute buffer、selection 与 external evidence |
| InternVL-U | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Refine — `MULTIMODAL-REPRESENTATION` modular unification 分支 |
| Towards a Neural Debugger for Python | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | No Change — `AGENT-WORKFLOW`/`PLATFORM-EVALUATION-SYSTEM` 已保留 learned proposal 与 executable oracle 分责 |
| Compiler-First State Space Duality | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine — `INFER-TENSORRT-LLM` compiler-first state-space execution |
| OpenClaw-RL | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Refine — `TRAIN-GRPO` online Agent-RL feedback ownership |
| Flash-KMeans | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine — `INFER-TENSORRT-LLM` materialization-free online reduction |
| ReMix | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine — `MODEL-MOE` selection 与 contribution magnitude 分责 |
| Lost in Backpropagation | 4 | 4 | 3 | 3 | 4 | 3 | 21/30 | Emerging / Weekly Only — 尚无可部署替代 head 的端到端证据 |
| DIVE | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `TRAIN-DATA` evidence-first tool-task synthesis |
| V0.5 generalist value prior | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `TRAIN-GRPO` prior-assisted rollout stopping |
| FP4 Mean Bias / Averis | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Refine — `TRAIN-PRETRAINING` source-aware FP4 mean/residual split |
| MR-Search | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | No Change — `AGENT-MEMORY`/`AGENT-REFLECTION` 已覆盖跨尝试状态与 reflection provenance |
| IndexCache | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine — `INFER-PREFILL` 跨层 index reuse state |
| Strategic Navigation / MADQA | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` retrieval/navigation effort cascade |
| XSkill | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | No Change — `AGENT-MEMORY` 已覆盖 derived strategy 的 provenance/supersession/rollback |
| Neural Thickets | 3 | 3 | 3 | 3 | 3 | 3 | 18/30 | Low-score verification complete — Weekly only |
| Automatic Generation of High-Performance RL Environments | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Refine — `AGENT-WORKFLOW` hierarchical equivalence ladder |
| Examining Reasoning LLMs-as-Judges | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` policy-shifted judge audit |
| Attention Sinks theorem | 4 | 3 | 3 | 4 | 4 | 4 | 22/30 | Refine — `MODEL-SELF-ATTENTION` no-op/sink normalization trade-off |
| One Model, Many Budgets / ELIT | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | No Change — `MODEL-MOE` 已覆盖 elastic subnetwork serving identity |
| Groundsource | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Unverified / Blocked — full paper inaccessible |
| RAGEN-2 | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Refine — `TRAIN-GRPO` reward variance 与跨输入可区分性 |
| EvoScientist | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Review Complete — No Change / Experimental Case |
| MEMO | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `AGENT-MEMORY` retention/exploration/replay state |
| Reasoning as Compression | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Refine — `TRAIN-GRPO` versioned reasoning-cost prior |
| Deep Tabular Research | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | Refine — `AGENT-PLANNING` path state 与 execution feedback |
| FinToolBench | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | Full Review Complete — No Change / Ch62 Experimental Evaluation Case |
| LookaheadKV | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine — `INFER-KV-CACHE` learned lookahead query 与 cache identity |
| UCIP | 4 | 3 | 2 | 3 | 5 | 3 | 20/30 | Full Review Complete — No Change / Ch62 Experimental Evaluation Case |
| One-Eval | 4 | 4 | 5 | 3 | 5 | 4 | 25/30 | Full Review Complete — No Change / Ch62 Experimental System Case |
| LMEB | 4 | 3 | 4 | 4 | 5 | 5 | 25/30 | Refine — `AGENT-MEMORY` temporal/granularity/candidate-scope identity |
| Video Streaming Thinking | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Integrate — `AGENT-CONTEXT` proactive pre-query context production |
| daVinci-Env / OpenSWE | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine — `TRAIN-DATA` executable repository environment artifact |
| MM-CondChain | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` paired conditional-path evidence |
| Efficient Reasoning with Balanced Thinking / ReBalance | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Refine — `MODEL-SAMPLING` trajectory-state feedback control |
| Expert Threshold Routing | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine — `MODEL-MOE` population routing state |
| Spend Less, Reason Better / BAVT | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine — `AGENT-PLANNING` multi-resource budget tree state |
| EnterpriseOps-Gym | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Review Complete — No Change / Ch62 Experimental Evaluation Case |
| EvoClaw / SWE-Milestone | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Review Complete — No Change / Ch62 Experimental Evaluation Case |
| GradMem | 5 | 4 | 4 | 5 | 5 | 5 | 28/30 | Refine — `MODEL-LONG-CONTEXT` optimized temporary memory state |
| SFT versus RL survey | 2 | 3 | 4 | 3 | 4 | 3 | 19/30 | Low-score verification complete — Weekly only / secondary synthesis |
| AI Can Learn Scientific Taste | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Full Review Complete — No Change / Ch27 Experimental Feedback Case |
| AgentProcessBench | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` causal process labels |
| V-JEPA 2.1 | 4 | 4 | 4 | 5 | 5 | 5 | 27/30 | Refine — `WORLDVIEW-REPRESENTATION` objective target coverage |
| KServe v0.17.0 | 3 | 5 | 5 | 5 | 5 | 4 | 27/30 | Full Review Complete — No Change / Ch49+57 Versioned Evolution Case |

评分已按恢复后的 evidence risk 重算；`20+` 只表示进入 Source Review Gate。Neural Thickets 与 SFT versus
RL survey 分别为 18/30、19/30，均保留来源、日期和拒绝理由核验，不以低分跳过事实检查。

## Discovery Recall Ledger

| Ledger Item | Count | Review Result |
| --- | ---: | --- |
| Existing W11 score rows | 2 | 两项均保留，但旧 decision 作废并重新审查 |
| Recovered W11 candidate families | 53 scored + 0 ordinary unscored pending + 1 unscored blocked identity + 3 unscored blocked full text + 1 cross-year reroute | 29 项由当周 feed 恢复；RAGEN-2 由 W15 feed 回拨；W12 intake 已完成 23 项，将 FineRMoE 路由回 2025，并显式记录四个无法继续全文审计的 intake |
| Current scored in-window candidate families | 55 | 53 项 `>=20`；2 项低分边界核验；另有 1 个 blocked-identity 与 3 个 blocked-full-text intakes |
| W10 spillbacks discovered from W11 feeds | 11 | 按 arXiv v1 date 归回 W10，不计入 W11 |
| Full Source Reviews complete under current gate | 52 | 原 29 项，加 RAGEN-2 与 22 个达到 `20+` 的 intake 候选完成全文、revision、实验/附录或官方 release/docs/code surface 和章节邻接核验 |
| Low-score verification complete | 2 | Neural Thickets 与 SFT versus RL survey 分别保持 18/30、19/30；完成来源、日期、证据类型与拒绝理由核验 |
| Unresolved / blocked | 5 | Groundsource、HomeSafe-Bench、Think While Watching、TERMINATOR 正文访问受阻；Safe Web Agent Learning 无法唯一解析 primary identity。五项均按 blocked-skip 规则留在 backlog，不得进入 W11 Books Integration |

`Full Source Reviews complete` 暂不沿用 2026-07-31 的完成数字，因为当时没有经过当前候选池和直接
来源复核。后续每完成一项非模板化 Source Review，才同步更新该计数。

## Recovered Candidate Census

> Status note (2026-08-13): 本表的 `Initial Owner / Review State` 保留发现与全文审计完成时的快照，
> 其中 `Books pending / provisional` 不再表示当前状态。最终 disposition 只以 `Candidate Scoring` 与
> `Books Integration Decision` 为准；Stable Node/current/legacy mapping 见 `ROADMAP.md`。

| Event Date | Candidate | Direct Primary Source | Initial Owner | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-09 | How Far Can Unsupervised RLVR Scale LLM Training? | arXiv:2603.08660 v1 | Ch29 | Full Review Complete — Books pending |
| 2026-03-09 | OneMillion-Bench | arXiv:2603.07980 v1 | Ch62 | Full Review Complete — Books pending |
| 2026-03-09 | Agentic Critical Training | arXiv:2603.08706 v1 | Ch29 | Full Review Complete — Books pending |
| 2026-03-09 | Fish Audio S2 | arXiv:2603.08823 v1 | Ch23 | Full Review Complete — Books pending |
| 2026-03-09 | Test-Driven Agentic Development | arXiv:2603.08806 v1 | Ch77 | Full Review Complete — Books pending |
| 2026-03-09 | SoundWeaver | arXiv:2603.07865 v1 | Ch39 | Full Review Complete — Books pending |
| 2026-03-09 | RetroAgent | arXiv:2603.08561 v1 | Ch73 | Full Review Complete — Books pending |
| 2026-03-09 | In-Context RL for Tool Use | arXiv:2603.08068 v1 | Ch29 | Full Review Complete — Books pending |
| 2026-03-10 | Thinking to Recall | arXiv:2603.09906 v1 | Ch20 | Full Review Complete — Books pending |
| 2026-03-10 | InternVL-U | arXiv:2603.09877 v1 | Ch23 | Full Review Complete — Books pending |
| 2026-03-10 | Towards a Neural Debugger for Python | arXiv:2603.09951 v1 | Ch77 | Full Review Complete — Books pending |
| 2026-03-10 | Compiler-First State Space Duality | arXiv:2603.09555 v1 | Ch32 | Full Review Complete — Books pending |
| 2026-03-10 | OpenClaw-RL | arXiv:2603.10165 v1 | Ch29 | Full Review Complete — Books pending |
| 2026-03-10 | Flash-KMeans | arXiv:2603.09229 v1 | Ch45 | Full Review Complete — Books pending |
| 2026-03-10 | ReMix | arXiv:2603.10160 v1 | Ch21 | Full Review Complete — Books pending |
| 2026-03-10 | Lost in Backpropagation | arXiv:2603.10145 v1 | Ch24 | Full Review Complete — claim boundary retained |
| 2026-03-10 | DIVE | arXiv:2603.11076 v1 | Ch74 | Full Review Complete — Books pending |
| 2026-03-11 | Four MTIA chips in two years | Meta AI direct technical article | Ch45 | Full Review Complete — Books pending |
| 2026-03-11 | V0.5 generalist value prior | arXiv:2603.10848 v1 | Ch29 | Full Review Complete — Books pending |
| 2026-03-11 | FP4 Mean Bias / Averis | arXiv:2603.10444 v1 | Ch45 | Full Review Complete — Books pending |
| 2026-03-11 | MR-Search | arXiv:2603.11327 v1 | Ch74 | Full Review Complete — Books pending |
| 2026-03-12 | IndexCache | arXiv:2603.12201 v1 | Ch39 | Full Review Complete — Books pending |
| 2026-03-12 | Strategic Navigation / MADQA | arXiv:2603.12180 v1 | Ch62 | Full Review Complete — Books pending |
| 2026-03-12 | XSkill | arXiv:2603.12056 v1 | Ch73 | Full Review Complete — Books pending |
| 2026-03-12 | Neural Thickets | arXiv:2603.12228 v1 | Ch24 | Low-score verification complete — Weekly only |
| 2026-03-12 | Automatic Generation of High-Performance RL Environments | arXiv:2603.12145 v1 | Ch77 | Full Review Complete — Books pending |
| 2026-03-12 | Examining Reasoning LLMs-as-Judges | arXiv:2603.12246 v1 | Ch62 | Full Review Complete — Books pending |
| 2026-03-12 | Attention Sinks theorem | arXiv:2603.11487 v1 | Ch14 | Full Review Complete — Books pending |
| 2026-03-12 | One Model, Many Budgets / ELIT | arXiv:2603.12245 v1 | Ch17 | Full Review Complete — Books pending |
| 2026-03-10 / 03-12 | Groundsource | EarthArXiv preprint + Google Research announcement/dataset | Ch23 | Unverified / Blocked — full paper inaccessible |
| 2026-03-12 | NVIDIA Dynamo v1.0.0 GA | official release docs + design/code family | Ch49 | Full Review Complete — Books pending |
| 2026-03-12 | RAGEN-2 | official repository release + arXiv:2604.06268 later v1 | Ch29；handoff Ch28/62 | Full Review Complete — Books pending |
| 2026-03-09 | EvoScientist | arXiv:2603.08127 v1 + later official repository | Ch73 owner check; Ch77/62 handoff | Full Review Complete — No Change / Experimental Case |
| 2026-03-09 | MEMO | arXiv:2603.09022 v1/v2 + official repository | Ch73；handoff Ch62/77/78 | Full Review Complete — provisional Refine / Experimental |
| 2026-03-09 | Reasoning as Compression | arXiv:2603.08462 v1/current v2 | Ch29；handoff Ch20/62 | Full Review Complete — provisional Refine / Experimental |
| 2026-03-10 | Deep Tabular Research | arXiv:2603.09151 v1/v2 | Ch75；handoff Ch73/77/62 | Full Review Complete — provisional Refine / Experimental |
| 2026-03-09 | FinToolBench | arXiv:2603.08262 v1/current v2 + official repository | Ch62；handoff Ch68/74 | Full Review Complete — No Change / Experimental Evaluation Case |
| 2026-03-11 | LookaheadKV | arXiv:2603.10899 sole v1 + official repository | Ch41；handoff Ch39/50 | Full Review Complete — provisional Refine / Experimental |
| 2026-03-11 | UCIP | arXiv:2603.11382 v1/current v4 + official repository/results | Ch62；handoff Ch68 | Full Review Complete — No Change / Experimental Evaluation Case |
| 2026-03-10 | One-Eval | arXiv:2603.09821 sole v1 + official repository | Ch62；handoff Ch77 | Full Review Complete — No Change / Experimental System Case |
| 2026-03-13 | LMEB | arXiv:2603.12572 v1/current v6 + official benchmark repository/data | Ch73；handoff Ch62/72 | Full Review Complete — provisional Refine / Experimental |
| 2026-03-12 | Video Streaming Thinking | arXiv:2603.12262 v1/current v2 + official code/data/model repository | Ch71；handoff Ch73/62/52 | Full Review Complete — provisional Integrate / Experimental |
| 2026-03-13 | daVinci-Env / OpenSWE | arXiv:2603.13023 v1/current v2 + official environment/pipeline repository | Ch23；handoff Ch62/77/56 | Full Review Complete — provisional Refine / Experimental |
| 2026-03-12 | MM-CondChain | arXiv:2603.12266 sole v1 + official repository/dataset | Ch62；handoff Ch75/77 | Full Review Complete — provisional Refine / Experimental |
| 2026-03-12 | Efficient Reasoning with Balanced Thinking / ReBalance | arXiv:2603.12372 v1/current v3 + official repository/artifacts | Ch20；handoff Ch52/62 | Full Review Complete — provisional Refine / Experimental |
| 2026-03-12 | Expert Threshold Routing | arXiv:2603.11535 sole v1 | Ch21；handoff Ch37/40/46 | Full Review Complete — provisional Refine / Experimental |
| 2026-03-13 | Spend Less, Reason Better / BAVT | arXiv:2603.12634 sole v1 | Ch75；handoff Ch74/62/80 | Full Review Complete — provisional Refine / Experimental |
| 2026-03-13 | EnterpriseOps-Gym | arXiv:2603.13594 sole v1 + official repository/artifact | Ch62；handoff Ch74/75/77/80 | Full Review Complete — No Change / Experimental Evaluation Case |
| 2026-03-13 | EvoClaw / current SWE-Milestone | arXiv:2603.13428 v1/current v4 + official repository/data | Ch62；handoff Ch77/80 | Full Review Complete — No Change / Experimental Evaluation Case |
| 2026-03-14 | GradMem | arXiv:2603.13875 sole v1 + official repository | Ch22；handoff Ch39/73 | Full Review Complete — provisional Refine / Experimental |
| 2026-03-14 | SFT versus RL survey | arXiv:2603.13985 sole v1 | Ch25/29 source index only | Low-score verification complete — Weekly only / secondary synthesis |

## W12 Spillback Intake Ledger

> Status note (2026-08-13): 该表记录 spillback 被发现和审计时的状态；其中 provisional/pending 标签已由
> 本周最终 Candidate Scoring 逐项取代，blocked 与 cross-year reroute 除外。

W12 推荐流延迟发现以下 28 个 W11 事件。这里只把“已发现并需要回拨”转换为 candidate-level queue；除
已标记 Full Source Review Complete 的候选外，名称、日期区间与归周来自 W12 spillback ledger，精确 metadata、评分与机制均必须逐项
重新核验，不能把 intake 冒充 Full Source Review。

| Event Date | Candidate | Primary Source State | Review State |
| --- | --- | --- | --- |
| 2026-03-09 | EvoScientist | arXiv:2603.08127 v1 + later official repository | Full Source Review Complete — No Change / Experimental Case |
| 2026-03-09 | FinToolBench | arXiv:2603.08262 v1/current v2 + official repository | Full Source Review Complete — No Change / Ch62 Experimental Evaluation Case |
| 2026-03-09 | MEMO | arXiv:2603.09022 v1/v2 + official repository | Full Source Review Complete — provisional Refine / Ch73 Experimental |
| 2025-09-11 | FineRMoE | OpenReview: JxXy3YGSln; modified 2026-02-11 | Cross-year Reroute — 2025 backlog; not a W11 event |
| 2026-03-09 | Reasoning as Compression | arXiv:2603.08462 v1/current v2 | Full Source Review Complete — provisional Refine / Ch29 Experimental |
| 2026-03-10 | Deep Tabular Research | arXiv:2603.09151 v1/v2 | Full Source Review Complete — provisional Refine / Ch75 Experimental |
| 2026-03-11 | LookaheadKV | arXiv:2603.10899 sole v1 + official repository | Full Source Review Complete — provisional Refine / Ch41 Experimental |
| 2026-03-11 | UCIP | arXiv:2603.11382 v1/current v4 + official repository/results | Full Source Review Complete — No Change / Ch62 Experimental Evaluation Case |
| 2026-03-10～03-11 | Safe Web Agent Learning | Exact-title search、03-10/03-11 discovery indices 与 arXiv 均无法解析唯一 primary ID | Unverified / Blocked Identity — skipped; not scored |
| 2026-03-10 | One-Eval | arXiv:2603.09821 sole v1 + official repository | Full Source Review Complete — No Change / Ch62 Experimental System Case |
| 2026-03-13 | LMEB | arXiv:2603.12572 v1/current v6 + official benchmark repository/data | Full Source Review Complete — provisional Refine / Ch73 Experimental |
| 2026-03-12 | Video Streaming Thinking | arXiv:2603.12262 v1/current v2 + official code/data/model repository | Full Source Review Complete — provisional Integrate / Ch71 Experimental |
| 2026-03-13 | daVinci-Env / OpenSWE | arXiv:2603.13023 v1/current v2 + official environment/pipeline repository | Full Source Review Complete — provisional Refine / Ch23 Experimental |
| 2026-03-12 | MM-CondChain | arXiv:2603.12266 sole v1 + official repository/dataset | Full Source Review Complete — provisional Refine / Ch62 Experimental |
| 2026-03-12 | HomeSafe-Bench | arXiv:2603.11975 v1/current v2；无 HTML，官方 PDF 访问被用户浏览器权限阻止 | Unverified / Blocked Full Text — skipped; not scored |
| 2026-03-12 | Think While Watching | arXiv:2603.11896 sole v1 + inference-only official repository；无 HTML，官方 PDF 访问被用户浏览器权限阻止 | Unverified / Blocked Full Text — skipped; not scored |
| 2026-03-12 | Efficient Reasoning with Balanced Thinking / ReBalance | arXiv:2603.12372 v1/current v3 + official repository/artifacts | Full Source Review Complete — provisional Refine / Ch20 Experimental |
| 2026-03-12 | Expert Threshold Routing | arXiv:2603.11535 sole v1 | Full Source Review Complete — provisional Refine / Ch21 Experimental |
| 2026-03-13 | Spend Less Reason Better / BAVT | arXiv:2603.12634 sole v1 | Full Source Review Complete — provisional Refine / Ch75 Experimental |
| 2026-03-13 | EnterpriseOps-Gym | arXiv:2603.13594 sole v1 + official repository/artifact | Full Source Review Complete — No Change / Ch62 Experimental Evaluation Case |
| 2026-03-13 | EvoClaw / current SWE-Milestone | arXiv:2603.13428 v1/current v4 + official repository/data | Full Source Review Complete — No Change / Ch62 Experimental Evaluation Case |
| 2026-03-13 | TERMINATOR | arXiv:2603.12529 v1/current v2 + official project/model artifacts；无 HTML，official PDF text入口不可读 | Unverified / Blocked Full Text — skipped; not scored |
| 2026-03-14 | SFT versus RL survey | arXiv:2603.13985 sole v1 | Low-score verification complete — Weekly only / secondary synthesis |
| 2026-03-14 | GradMem | arXiv:2603.13875 sole v1 + official repository | Full Source Review Complete — provisional Refine / Ch22 Experimental |
| 2026-03-15 | AI Can Learn Scientific Taste | arXiv:2603.14473 v1/current v2 + official repository | Full Source Review Complete — No Change / Ch27 Experimental Feedback Case |
| 2026-03-15 | AgentProcessBench | arXiv:2603.14465 v1/current v2 + official repository/data | Full Source Review Complete — provisional Refine / Ch62 Experimental |
| 2026-03-15 | V-JEPA 2.1 | arXiv:2603.14482 v1/current v3 + official repository/checkpoints | Full Source Review Complete — provisional Refine / Ch5 Experimental |
| 2026-03-13 | KServe v0.17.0 | official release/blog + 0.17 versioned docs + release/PR surface | Full Source Review Complete — No Change / Ch49+57 Versioned Evolution Case |

## Cross-Week Spillback Ledger

这些条目由 W11 的推荐流发现，但 v1 first-public date 属于 W10。它们必须回写 W10，不能在 W11
重复评分或用推荐日期制造伪事件：

| First-public Date | Candidate | Primary Metadata | Destination |
| --- | --- | --- | --- |
| 2026-03-02 | Multi-Head Low-Rank Attention | arXiv:2603.02188 | W10 Discovery Gate reopened |
| 2026-03-04 | Believe Your Model | arXiv:2603.03872 | W10 Discovery Gate reopened |
| 2026-03-05 | Progressive Residual Warmup | arXiv:2603.05369 | W10 Discovery Gate reopened |
| 2026-03-05 | BandPO | arXiv:2603.04918 | W10 Discovery Gate reopened |
| 2026-03-05 | Sparse-BitNet | arXiv:2603.05168 | W10 Discovery Gate reopened |
| 2026-03-05 | ATLAS / Scaling Agentic Capabilities | arXiv:2603.06713 | W10 Discovery Gate reopened |
| 2026-03-05 | Building AI Coding Agents for Terminal | arXiv:2603.05344 | W10 Discovery Gate reopened |
| 2026-03-07 | AutoResearch-RL | arXiv:2603.07300 | W10 Discovery Gate reopened |
| 2026-03-07 | Hindsight Credit Assignment | arXiv:2603.08754 | W10 Discovery Gate reopened |
| 2026-03-08 | Scaling Data Difficulty | arXiv:2603.07779 | W10 Discovery Gate reopened |
| 2026-03-08 | Breaking Training Bottlenecks / MicroCoder-GRPO | arXiv:2603.07777 | W10 Discovery Gate reopened |

## Deep Analysis

### 1. 从“更多 compute”到“compute 应由什么状态控制”

MTIA、Compiler-First SSD、Flash-KMeans、Averis、ELIT、IndexCache 与 Dynamo 位于不同层，却共享
同一演进问题：当 workload、memory hierarchy、token state 和 SLO 变化后，静态均匀分配不再足够。
新设计分别把 workload contract、tile/index、mean residual、latent budget、retrieval index 与 KV event
提升为控制状态。收益不是免费速度，而是以更多 identity、freshness、compiler/runtime coupling 和
failure recovery 换取更少 materialization、data movement 或无效计算。旧 GPU、固定 token grid、完整
attention 与 aggregated serving 在模型变化快、状态复用低或控制面成本更高时仍然成立。

### 2. 从 independent attempt 到可追溯的跨轨迹学习

MR-Search、OpenClaw-RL、RetroAgent、XSkill、DIVE、ICRL 与 TDAD 共同表明，Agent 学习正在从“每条
trajectory 独立评分”演进为跨 episode/context、live feedback、derived memory 与 executable verifier
的组合。但新的可学习信号也带来新的错误源：reflection 不是事实、用户反馈不是无偏 reward、derived
lesson 不是原始 trace、test pass 也不保证需求正确。长期设计原则不是保留更多文本，而是把 trace、
evidence、judge/verifier、policy version、consent 与 supersession 作为同一 provenance graph 管理。
RAGEN-2 再补充一类 group-level signal failure：同 prompt rewards 全同会让 task advantage 接近零，却不一定
让 KL/entropy regularization 同时归零；只监控 within-input entropy 会漏掉 reasoning 是否仍依赖 input。
Reward-variance filtering 可以避免部分低信号 update，但会改变被优化的 prompt distribution，故必须同时
记录 filtered objective、coverage loss、MI proxy 与 task success，不能把高 RV 当成“高质量样本”的同义词。

### 3. 从 final score 到 accuracy-effort-failure contract

MADQA、Reasoning LLMs-as-Judges、OneMillion-Bench 与 Auto RL Environments 共同削弱“一个最终分数就能
表示系统能力”的假设。document Agent 的结果取决于 retrieval/navigation/comprehension 与 step budget；
judge 一旦进入训练环会改变 policy distribution；高性能环境需要分层 observational equivalence；专业
任务还受 scaffold、工具、rubric 与经济/安全后果影响。因此 evaluation 应同时保留结果、evidence、
effort、failure stage、oracle branch 与 artifact correctness，且不能把作者 benchmark 外推成 deployment
autonomy。

## Evidence Level

- 论文/技术报告与官方工程 source families：52 个 `20+` 候选已完成正文、方法、evaluation、
  limitations/appendix，或 release + versioned docs + code/PR surface 的直接核验；
  作者实验只证明其公开 workload contract。
- 官方工程材料：MTIA 与 Dynamo 证明版本、架构和已披露 failure boundary；厂商性能数字不外推。
- 低分候选：Neural Thickets 与 SFT versus RL survey 已完成来源、日期和拒绝理由核验。
- 前向待审：W12 spillback intake 的普通未评分候选已清零；
  FineRMoE 因 2025-09-11 OpenReview 首发已转入 2025 backlog，不计作 W11 candidate。
- 阻塞 backlog：Groundsource 只有 metadata、官方技术长文与 dataset record 已验证，paper full text 未验证；
  `Safe Web Agent Learning` 无法解析到唯一 primary identity，HomeSafe-Bench、Think While Watching 与
  TERMINATOR 正文入口不可读，四项均未评分；因此这些 source families 的内部机制与长期 Books 结论都保持
  `Unverified / Blocked`。按用户确认的 blocked-skip 规则，它们不再阻塞其余 W11 候选的前向审计，但
  Historical Evidence Gate 仍保持打开。

## Cross-Week Deduplication

- 11 个 first-public date 位于 2026-03-02～03-08 的推荐项已归回 W10，不在 W11 重复评分。
- MTIA 按 chip generation、software enablement 与 workload change 去重；Dynamo 按 runtime layer 与
  backend engine release 去重；MR-Search/RetroAgent/XSkill 按 episodic context、derived memory 与 durable
  memory 的 ownership 区分，而非都归成“Agent memory”。
- Groundsource 的 2026-03-10 preprint 与 2026-03-12 announcement 属同一 source family，不计两次事件。
- RAGEN-2 以官方 repository 的 2026-03-12 release 为 first-public owner；2026-04-07 arXiv v1 与后续 ICML
  Oral 状态是 formalization/publication evolution，不在 W15 重复计事件。
- Nemotron 3 Super 的 base checkpoint 于 03-04 在 W10 首发；03-11 post-trained FP8/NVFP4 checkpoint 是
  同一 source family 的 deployment evolution，04-14 arXiv v1 是 formal report，不在 W11/W16 重复计分。
  完整 review 由 W10 owner 保存，本周只保留 checkpoint-stage 指针。

## Knowledge Tree Position

主要 owner 覆盖 Ch14、Ch17、Ch20～24、Ch29、Ch32、Ch39、Ch45、Ch49、Ch62、Ch73～74、Ch77；
跨层 handoff 集中在 Ch38～39、Ch45～50、Ch62～69 与 Ch71～80。具体 Books owner 仍需在 Evidence Gate
通过后读取目标及相邻章节确认。

## Recommended Action

W11 forward candidate queue 已闭合；Groundsource 与四个未评分 blocked intakes 保留 backlog，待 primary
text/identity 可访问时回补，不再暂停 forward sweep。继续复核年度固定来源与学术 cross-index 的 Discovery
Recall；W11 已完成可访问 Source Family 的 Books Integration，历史全局 Archive Completion Gate 继续开放。

## Event-Date Daily Decision

历史回填保持 Weekly-only：2026-03-09～03-15 的真实事件均记录在本完整 ISO Weekly，不补造 Daily。

## Books Integration Decision

`W11 Source-Family Books Gate Passed`。55 个评分候选的最终状态以本周 `Candidate Scoring` 表为唯一账本；
全文 Review 中的 `pending/provisional` 是写入前审计快照，均由该表和下列 owner ledger 取代。

- `Integrate/Refine (31)`：`WORLDVIEW-REPRESENTATION`（V-JEPA 2.1）；`MODEL-SELF-ATTENTION`
  （Attention Sinks）；`MODEL-SAMPLING`（ReBalance）；`MODEL-MOE`（Expert Threshold Routing、ReMix）；
  `MODEL-LONG-CONTEXT`（GradMem）；`MULTIMODAL-REPRESENTATION`（Fish Audio S2、InternVL-U）；
  `TRAIN-DATA`（DIVE、daVinci-Env / OpenSWE）；`TRAIN-PRETRAINING`（Averis）；`TRAIN-GRPO`
  （RAGEN-2、OpenClaw-RL、Reasoning as Compression、ICRL、V0.5）；`INFER-PREFILL`（IndexCache）；
  `INFER-KV-CACHE`（LookaheadKV）；`INFER-TENSORRT-LLM`（Compiler-First SSD、Flash-KMeans）；
  `PLATFORM-EVALUATION-SYSTEM`（MADQA、Reasoning Judges、MM-CondChain、AgentProcessBench）；
  `AGENT-CONTEXT`（Video Streaming Thinking）；`AGENT-MEMORY`（MEMO、LMEB）；`AGENT-PLANNING`
  （Deep Tabular Research、BAVT）；`AGENT-WORKFLOW`（TDAD、High-Performance RL Environments）。
- `No Change / Weekly Only / Emerging (23)`：每项均在评分表绑定具体现有机制或证据边界；这包括 MTIA、
  Dynamo、unsupervised RLVR、OneMillion-Bench、ACT、SoundWeaver、RetroAgent、Thinking to Recall、Neural
  Debugger、MR-Search、XSkill、ELIT、EvoScientist、FinToolBench、UCIP、One-Eval、EnterpriseOps-Gym、
  EvoClaw、Scientific Taste、KServe，以及 Neural Thickets、SFT-vs-RL、Lost in Backpropagation。
- `Blocked (5)`：Groundsource 为评分后 full-text blocker；Safe Web Agent Learning、HomeSafe-Bench、Think While
  Watching、TERMINATOR 为未评分 identity/full-text blocker。它们没有进入 Books，也不被伪装成完成。

该 Gate 只说明 W11 中可访问且完成 Source Review 的 family 已逐项处理；broader Historical Archive Gate 仍开放，
不能据此宣称 W01～W32 全部完成。

## Ignored Noise

缺少模型、batch、precision、power 与 SLO 条件的峰值指标比较。

## 2026-07-31 Full Re-Audit Addendum

- MTIA 官方工程材料已全文复核。四代芯片只作为 workload contract 演进案例：硬件、编译、
  runtime、collective 与 observability 共同收敛；不主张专用 ASIC 普遍替代 GPU。
- 该长期机制已写入 Ch45；版本化规格和厂商性能仍留在 Weekly。

## Full Source Review

> Status note (2026-08-13): 下列 `ROADMAP / decision` 字段保留每篇全文刚审计完成时的写入前判断，
> 包括当时的 `Books pending / provisional / Historical Books Gate Closed`。它们用于复现决策过程，不是当前
> disposition；最终状态只以本周 `Candidate Scoring` 与 `Books Integration Decision` 为准。

### RAGEN-2: Reasoning Collapse in Agentic RL — 27/30

- **Candidate / Week / Score**：RAGEN-2；2026-W11；27/30，维持 discovery score。它同时提供新的训练
  failure taxonomy、可计算 diagnostic、gradient-level mechanism 与 intervention，并有公开实现；但 MI/RV 都是
  条件性 proxy，硬件、seed/variance 与跨真实环境证据不完整，Source Reliability 保持 4。
- **Source Family ID / Type / Date**：`RAGEN2-TEMPLATE-COLLAPSE-SNR-FILTERING`；official project/repository
  release + arXiv paper + training artifact。官方 repository 的 News 明确记录 2026-03-12 release，故 first-public
  owner 是 W11；arXiv 唯一 v1 于 2026-04-07 提交，是 later formal-source boundary。current project page 的
  ICML 2026 Oral 标记是后续 publication status，不倒写成 W11 已知 peer-review evidence。
- **Direct / Related Primary Sources**：直接来源为 arXiv v1 全文、official project page、RAGEN repository、
  embedded RAGEN-2 PDF/current code 与 no-release boundary。RAGEN v1、veRL/HybridFlow、PPO/DAPO/GRPO/Dr.GRPO
  和七类 environments 是机制依赖与 baselines；它们不是 RAGEN-2 结论的独立复现。
- **Access / Full-read Coverage**：已读 Abstract、Introduction、setup、entropy/MI decomposition、全部 MI proxy、
  gradient/SNR decomposition、reward-variance top-p operator、主 experiments/analysis、Related Work、Conclusion/
  Limitations，以及 Appendix A～O 的 environment/reward、training/eval settings、sampling/filtering ablation、
  diagnostic plots、proxy definitions、filter variants、RV/SNR theorem、template mixing、gradient-MSE bias、
  regularizer dominance、KL/MI continuity 与 GRPO low-RV noise amplification；并核对 official release date、
  current repository modules/submodule、project claims 与无 GitHub release/tag。
- **Original Problem / Previous Design**：reward、response length、format validity 与 conditional entropy 易于在线
  监控；KL/entropy regularization 也能约束 policy drift 和 within-input diversity。在单轮、dense reward 或固定
  prompt 分布中它们仍合理。但多轮 self-sampled RL 可能生成表面多样、对不同输入却使用同一 reasoning template
  的输出：entropy 仍高、格式仍对，真正的 input dependence 已经下降。
- **Changed Constraint / Principle**：同一 prompt 下多个 rollout 的 rewards 逐渐趋同后，group-relative advantage
  的 task signal 变弱；KL/entropy 等不乘 reward 的 regularization pressure 却仍存在。训练稳定性因此至少有两轴：
  `H(Z|X)` 表示同一输入内的 variability，`I(X;Z)` 表示跨输入 distinguishability。只保持前者无法证明 reasoning
  仍响应当前 state。
- **Diagnostic Mechanism**：作者用 `H(Z)=I(X;Z)+H(Z|X)` 区分 diverse reasoning、template collapse、compressed
  reasoning 与 low-entropy collapse。真实 MI 不可解，于是在 batch 内把每条 reasoning trace `Z_i,k` 对所有
  prompts `X_j` 做 teacher-forced cross-scoring，比较 true-prompt matched log-prob 与 prompt-mixture marginal，
  形成 Retrieval-Acc、Recall@k、MI-Est、MI-ZScore/EMA 等 proxy。它复用已有 rollout且无需另一 judge model或
  新 rollout，但 all-pairs scoring 仍是额外 model forward/teacher-forcing work，不能写成零计算成本。
- **Intervention Mechanism**：每个 iteration 对 `P` 个 prompts 各采 `G` 条 trajectories，计算 within-prompt
  episode-return variance；按 RV 降序累计，保留达到总 variance mass `rho` 的最小 prompt prefix，只对 kept
  groups 求 gradient。它是 post-sampling mask，不改变当轮 rollout distribution，却改变 update objective 与
  下一轮 policy。Top-p kept count 随 RV distribution 自适应；top-k、min-p、reverse top-p 是比较分支。
- **State Ownership / Control and Data Flow**：environment/verifier 拥有 reward 与 terminal state；rollout manager
  绑定 prompt、trajectory、policy version 和 action history；training controller 按 prompt group 计算 RV、保存
  mask/kept mass 并构建 filtered objective；actor/reference/regularizer 各自拥有 mutable/frozen policy state；
  evaluator 计算 validation success 与 MI proxies。MI trace 不应反向成为事实标签，filter 也不能修改 environment
  truth 或自动放宽 curriculum/policy。
- **Implementation Details**：主设置使用 Qwen2.5-3B、veRL/HybridFlow 与 PPO/DAPO/GRPO/Dr.GRPO，最多 400
  rollout-update iterations；每 iteration `K=128` trajectories，文中主配置为 `P=8,G=16`，update batch 32、
  per-GPU minibatch 4、GAE `(gamma,lambda)=(1,1)`、actor/critic learning rates `1e-6/1e-5`、entropy coefficient
  0.001、PPO asymmetric clip 0.2/0.28，并有 format penalty。current repository 是持续演进的 592-commit RAGEN
  codebase、固定 veRL submodule，但无 event-date tag；current code不能自动证明 03-12 snapshot。
- **Evaluation Contract**：核心 testbed 覆盖 Sokoban、FrozenLake、MetaMathQA、Countdown，并扩到 SearchQA、
  WebShop、DeepCoder；Table 4 比较四 algorithms、Qwen2.5 0.5B/1.5B/3B/7B、Llama3.2-3B 与 Qwen2.5-VL-3B
  text/image。validation 每 environment 固定 512 prompts、temperature 0.5；interactive tasks 最多 5 turns/10
  actions，math tasks 1 turn。论文只写 NVIDIA GPUs，未披露型号/数量、precision、完整 sequence lengths、
  wall-clock total、seed/variance/置信区间或 production SLO；peak validation success 还受 early stopping 影响。
- **Ablations / Sensitivity / Overhead**：固定 128-rollout budget 下，`P x G` sweep 表明 RV computation 小于作者
  iteration time 的 0.1%，过滤后的 backward groups 更少，单步时间下降；但这是 Sokoban/Qwen2.5-3B、约 202GB
  VRAM footprint 的作者设置，不是通用成本。Quartile、reward-sum/entropy/length filter、keep-smallest、prompt-
  vs trajectory-level filtering 和 RV heterogeneity (`Std/Mean`) ablations 显示高-RV prompt filtering通常更好，
  同时 FrozenLake/GRPO、若干 model/task cells 出现负 delta；aggressive filtering并非单向收益。
- **What the Evidence Proves / Does Not Prove**：作者环境支持：conditional entropy 会漏掉 input-agnostic template
  drift；in-batch MI-family proxies 在这些 runs 中比 entropy 更早暴露退化；low-RV groups 的 task gradient较弱，
  RV filtering在多数已测组合提高 peak success和input dependence。它不证明 trace 是 faithful reasoning，不证明
  low RV 等于 pure noise，也不证明 MI proxy 是精确 Shannon MI、因果 performance predictor 或跨所有 RL/Agent
  workloads 的 release gate。相关系数 `+0.39` 只是中等相关，且 project page 的“2x better”是宣传性压缩。
- **Theory Boundary**：Cauchy-Schwarz 结果只给出 task-gradient norm 的 upper bound；小 RV 推出 upper bound小，
  不证明大 RV 的 gradient 必然有用。Appendix J 明确 filtered estimator 对 filtered mean unbiased，却通常对原
  unfiltered objective biased；reward noise也能制造高 RV。KL-close implies MI-close 依赖有限 alphabet 且 bound
  随 token space 很松；template-mixing lemma说明 prompt-independent mixture 收缩 MI，但不证明实际 collapse
  只由 regularizer引起。
- **Limitations / Threats to Validity**：论文自己承认 task signal与regularization noise可能在gradient accumulation
  中耦合、只测 single-agent、模型可能 game RV、sparse/noisy reward削弱 proxy、aggressive filtering收窄探索且
  `rho` 需按 task 调节。再加 synthetic/controlled environments、作者 reward design、同一 code family、peak
  selection、缺 seed/uncertainty/hardware 与 current artifact drift，外部效度和可复现性均有限。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：MI proxy补跨输入依赖，却有 all-pairs scoring、
  batch-composition敏感、length/scorer bias 与高基数 trace成本；RV filter减少低信号更新和 backward compute，
  却丢弃已学会/极难/稀疏 reward prompts、改变目标分布，并可能偏向 noisy high-variance verifier。Entropy、KL、
  reward mean仍分别适合 within-input diversity、policy drift和outcome监控；curriculum/reward redesign、more rollout、
  regularizer tuning 与 no-filter 在 RV separation弱或 coverage更重要时仍是合理旧分支。
- **Evolution Relationship / ROADMAP / Adjacent Chapters**：`Direct Evolution`：reward/format监控 → conditional
  entropy → input-dependence proxy → prompt-level signal filtering → joint success/coverage/bias monitoring；与 PPO/
  GRPO objective、verifier和Evaluation属于 `Layering / Dependency`。已读 Ch27～29 与 Ch62；主 owner为 Ch29，
  因为同-prompt group variance、normalization与low-RV update是核心，Ch28承接regularizer/advantage，Ch62承接
  proxy evidence boundary。它不进入 Ch75：研究对象是训练 policy，不是 runtime Planning。
- **Existing Coverage / Integration Decision**：Ch29 已说明 all-equal group几乎无 advantage、reward noise、group
  size和rollout cost，Ch28 已要求联合监控 advantage/entropy/KL；缺口是“熵健康但跨输入依赖已坍缩”、过滤对
  原 objective 的 bias与旧方案共存条件。暂定 `Refine — Existing Argument (Experimental; Provisional;
  Historical Books Gate Closed)`；Gate通过后优先 refine Ch29，并在 Ch28/62 短 handoff，不保存作者 benchmark
  headline、固定 `rho` 或“MI 是 reasoning quality”的强表述。
- **Open Questions**：如何用 held-out prompts 与 independent verifier 区分 high RV task signal 和 reward noise？
  batch composition、prompt similarity 与 policy revision变化时 MI proxy怎样校准？被过滤 prompts怎样通过
  curriculum/replay重新进入而不永久丢失 coverage？all-pairs scoring 的真实 FLOPs/memory与sampling收益如何权衡？
  multi-agent/shared-reward下哪个 group和input identity才有意义？

### OpenClaw-RL — 27/30

- **Source family / coverage**：`OPENCLAW-NEXT-STATE-ONLINE-RL`；arXiv:2603.10165 v1（2026-03-10）
  与 v2 revision（2026-05-11）、完整 v1 HTML、官方 code link。已读四组件异步架构、session model、
  PRM/OPD objectives、personal/general-agent evaluation、pseudocode、prompts 与 hyperparameters。论文
  没有独立 Limitations section，这是证据风险而非可忽略的排版差异。
- **Problem / old design / changed constraint**：offline trajectory + outcome reward 在可批量重放、任务
  短且终局可验证时合理；live Agent 持续产生 user reply、tool output、GUI transition 与 test verdict，
  若只当下一轮 context 就丢弃了 credit signal。约束变化是 policy 同时 serving、collecting、judging 与
  training，反馈来源异质且到达延迟不同。
- **Mechanism / ownership / flow**：environment server、PRM/Judge、Megatron trainer、SGLang serving
  四个 loop 解耦。next state 被拆成 evaluative scalar 与 directive hint：前者经多次 judge majority vote
  形成 `{-1,0,+1}` process reward；后者先抽取/筛选短 hint，再把 hint 加到原 prompt 构造同模型 teacher，
  用 teacher/student token log-prob difference 形成 token-level advantage。主线 turn 可训练，side turn
  不训练；日志按 policy-version/weight-update boundary 切分，说明 policy provenance 是数据身份的一部分。
- **Evaluation boundary**：personal track 是 Qwen3-4B + LLM-simulated student/teacher、GSM8K 前 36 题，
  且 simulator 与 evaluator 使用同类 LLM；general track 的 terminal/GUI/SWE/tool 分别使用不同模型、
  dataset 与 horizon，GUI 还在 training set 上评估。作者所谓“zero coordination overhead”不等于没有
  staleness、judge latency、weight skew 或 privacy cost；论文未报告并发 serving SLO、版本滞后、
  poisoned feedback、用户同意/删除或跨用户隔离实验。
- **Trade-off / evolution**：dense live feedback 改善长轨迹 credit assignment，却把 judge error、user
  preference drift、privacy、policy-version skew 与 negative-feedback attack 引入 training control plane。
  offline curated RL 在合规、replay、可撤销和稳定 verifier 优先时仍成立；online branch 必须带 consent、
  provenance、quarantine、canary、rollback 与 delete semantics。关系为 `Direct Evolution`。
- **ROADMAP / decision**：主 owner 暂定 Ch29，Ch63/68/73/76/80 handoff；Books pending。需要检查
  Ch29 是否把 online data plane、judge plane、policy update plane 与 serving plane 的 state/version
  barrier 写清，而不是只增加“从用户反馈训练”。

### Flash-KMeans — 28/30

- **Source family / coverage**：`FLASH-KMEANS-EXACT-IO-AWARE`；arXiv:2603.09229 v1（2026-03-10）
  与完整 HTML；已读 standard GPU path、profiling、FlashAssign、sort-inverse update、out-of-core pipeline、
  compile heuristic 和全部实验。论文没有独立 Limitations section；代码链接/commit 与数值复现状态
  未在论文页明确，记为 artifact boundary。
- **Problem / old design**：Lloyd k-means 的 `distance → argmin → scatter atomic centroid update` 在数据可
  驻留显存、K 较小或离线执行时简单且正确；大 N/K 时显式 `N×K` distance matrix 把理论计算转为 HBM
  materialization，随机 token-to-cluster scatter 又制造 atomic contention。动态 shape 与 out-of-core
  数据进一步把 bottleneck 移到 compile tuning 与 PCIe。
- **Mechanism / state/data flow**：FlashAssign 按 centroid tile 流式计算距离，只在 register 保留当前
  minimum 与 index，精确 online argmin 后不落完整矩阵。更新阶段先排序/构造 cluster→token inverse
  mapping，把随机 scatter 变为 segment-local reduction；out-of-core pipeline overlap H2D 与 compute；
  cache-aware heuristic 依据 L1/L2 与 shape 选 configuration，避免每个新 shape exhaustive tuning。
- **Evaluation boundary**：单 NVIDIA H200、CUDA 12.8，比较 fast_pytorch_kmeans、fastkmeans、cuML、
  FAISS，扫 N/K/D/B，报告 iteration/kernel/first-run。5.4×、17.9×、175×等均是作者特定 shape 与
  baseline；没有跨 GPU generation、multi-GPU、non-Euclidean metric、收敛质量/iteration 数或集成级
  SLO。算法仍是 exact Lloyd step，不等于对 initialization 或局部最优有改进。
- **Trade-off / evolution**：不 materialize 中间矩阵用更多 kernel 内 state 与 tiling complexity 换 HBM；
  sort-inverse 用排序成本换去原子争用；heuristic 用 near-optimal configuration 换 exhaustive optimum。
  小问题、一次性离线 job 或 shape 稳定时标准实现/预调优仍合理。关系为 `Principle Reuse`：与
  FlashAttention 共享 IO-aware 重排原则，但数据流和正确性 contract 不同。
- **ROADMAP / decision**：主 owner 暂定 Ch45，Ch23/32/39 handoff；Books pending。必须先检查 Ch45
  是否已有“materialization → online reduction”和“scatter → inverse gather/segmented reduction”的
  通用 kernel-design pattern，避免新增孤立的 k-means 案例。

### FP4 Mean Bias / Averis — 27/30

- **Source family / coverage**：`AVERIS-FP4-MEAN-RESIDUAL`；arXiv:2603.10444 v1（2026-03-11）、
  v2（2026-06-12）revision；完整 v1 HTML、theory appendices 与 experiments。当前 W11 只归档 v1
  事件，v2 用于识别 revision；公开 code/artifact 未在正文给出，复现状态 `Not Disclosed`。
- **Problem / old design**：blockwise FP4 用 block extreme 设 scale，直接量化在 activation/gradient
  outlier 较强时会压缩 long-tail semantic variation。SVD/whitening 能分离 dominant direction，但训练
  热路径的分解/正交化成本高；vanilla FP4 在均值偏置弱时仍是最简单路径。
- **Mechanism**：作者将 activation anisotropy 的主要可操作部分归因于 token-coherent column mean。
  forward 将 `X = 1 μ_X + X_R`，mean 与 residual 独立 FP4 quantize，再通过 broadcast mean product +
  residual GeMM 重构；backward 对 output gradient 同样拆分，weight/input gradient 由 residual-residual
  与 mean cross terms 合成，不 materialize mean matrix。代价是每 step 两个 mean reduction 与两次
  subtraction，而不是 spectral decomposition。
- **Evaluation boundary**：Qwen3-0.6B、DCLM、计划 100B tokens，W4A4G4 E2M1 NVFP4 + stochastic
  rounding；公开 downstream table 是 10B checkpoint，比较 BF16、vanilla FP4、Averis。论文只能证明
  此规模/数据/格式下 loss gap 缩小和若干任务均值变化；没有大模型、MoE、不同 optimizer、硬件吞吐、
  communication、energy 或稳定性 tail。正文无独立 limitations，不能把“dominant source”外推到所有
  layer/model/training phase。
- **Trade-off / evolution**：先识别 outlier 的 low-rank/coherent source，再选择廉价结构分解；收益来自
  改变 quantizer 所见 distribution，不是 FP4 本身变准确。mean reduction 会增加同步/带宽与融合要求，
  mean drift、microbatch/sequence composition 也改变校准状态。BF16/FP8 在数值余量或开发速度优先时
  继续成立。关系为 `Direct Evolution` from generic outlier handling to source-aware splitting。
- **ROADMAP / decision**：主 owner 暂定 Ch24，Ch33/34/45 handoff；Books pending。需要核对现稿量化
  内容是否把 activation/gradient/weight 分开，并避免把 inference PTQ 经验直接搬到 training FP4。

### Test-Driven Agentic Development — 26/30

- **Source family / coverage**：`TDAD-SPEC-TEST-PROMPT-COMPILATION`；arXiv:2603.08806 v1，
  2026-03-09；完整 HTML、公开 benchmark repo/harness。已读 spec schema、four roles、tool artifact、
  deterministic trace assertions、two-loop compilation、hidden/mutation/spec-evolution gates、24-run
  evaluation、reference isolation 和 limitations。
- **Problem / old design**：manual prompt editing + spot check 在低风险 prototype 中成本低；production
  Agent 的 prompt/tool description 是可变 executable policy，微小修改会产生 silent regression，单一
  success benchmark 又容易被 compiler 对 visible tests 过拟合。
- **Mechanism / ownership**：spec YAML（tools、policy priorities、decision tree、response contract）是 source
  of truth；TestSmith 把行为分支编译成 MFT/INV/DIR tests；PromptSmith 只读 visible tests 并迭代 prompt
  与 tool descriptions；Built Agent 通过 schema-valid respond tool 暴露可断言的 tool trace；MutationSmith
  在 compilation 后、看不到 tests 的隔离环境里生成 semantic faulty variants。hidden tests、mutation
  score 与 v1→v2 regression 分别测 generalization、test strength 与 evolution safety。
- **Evaluation boundary**：4 个 10～14-node specs、每个 v1/v2 三次，共 24 trials；所有 pipeline role
  使用 Claude Sonnet 4.5，最多 6 outer iterations，模型随机性只用三次 trial，正式 RPR 10～50 次未做。
  没有与 DSPy/TextGrad/APE 直接比较，也未测 50+ node。92%/58% compilation、HPR、mutation 与成本
  数字只能作为该 harness 的作者结果。
- **Trade-off / failure modes**：可执行 spec 把 prompt 从 prose 变成 versioned artifact，却受 spec/test
  completeness 限制；non-activating mutant 排除可能高估 suite，TestSmith safety self-censorship 会漏掉
  hostile cases。生产模式把失败 hidden test 提升为 visible，会逐步扩大 optimization surface，因此仍需
  fresh holdout、人审与 provenance。手工 design review 在难形式化的 empathy/ethics 属性中继续成立。
- **ROADMAP / decision**：主 owner 暂定 Ch77，Ch62/68/74/80 handoff；Books pending。需核查书稿是否已
  区分 `spec owner → generated tests → compiled prompt/tool artifact → runtime trace → evolution gate`。

### XSkill — 26/30

- **Source family / coverage**：`XSKILL-MULTIMODAL-DERIVED-MEMORY`；arXiv:2603.12056 v1
  （2026-03-12）、v2（03-13）、v3（07-01/ICML）；完整 v1 HTML、project/code links、method prompts、
  ablations、appendix/impact statement。W11 归档 v1，后续 revision 只用于机制核验。
- **Problem / old design**：保存/检索 raw trajectories 在文字任务中直接，但 multimodal Agent 的关键决策
  常由 image state 触发；只用原 query/text embedding 会丢失视觉条件。单一 workflow memory 又容易把
  高层程序与局部纠错混在一起。
- **Mechanism / ownership**：外部 KB 分为 Markdown skill（version/workflow/tool templates）和 JSON
  experience（trigger condition/action/embedding）。多路径 rollout 由 KB model 做 visually grounded
  summary、success/failure cross-rollout critique；experience 以 add/modify/merge/delete consolidation，
  skill 以 update/merge/remove/refine 控制长度。推理先按图像+任务分解子问题、retrieve top-k experience，
  再 image-aware rewrite，与适配后的 skill 一起作为 non-prescriptive reference 注入。execution model 与
  KB model 分离；usage history 回流 accumulation，但论文只实测一次 accumulate→test cycle。
- **Evaluation boundary**：五个 multimodal benchmark，每个随机取 100 training tasks，其余 evaluation；
  四个 backbone，4 rollouts，top-k=3，temperature=.6，max turns=20。主要 ablation 仅 VisualToolBench +
  Gemini-2.5-Pro；cross-model result 使用 Gemini-3-Flash 累积的 KB。结果支持 dual stream 在这些设置中
  互补，不证明长期闭环稳定、删除正确、跨域无污染或 usage feedback 有因果收益。
- **Trade-off / failure modes**：derived memory 提高抽象和复用，却引入 provenance loss、KB-model bias、
  merge/supersession error、visual embedding drift 与 cross-model contamination。论文明确提醒偏见可跨模型
  传播，并建议人审/审计/access control；还缺 artifact lineage、rollback、tombstone 与 feedback-loop
  evaluation。raw immutable traces 在 forensic/replay 中继续成立，derived memory 只能作为其上层视图。
- **ROADMAP / decision**：主 owner 暂定 Ch73，Ch72/75/77/80 handoff；Books pending。需与现有
  ReasoningBank/Dreaming/skills 内容去重，重点不是新增论文名，而是验证“raw trace → experience/skill
  双流 → consolidation → context adaptation → provenance/rollback”的演进链。

### Compiler-First State Space Duality — 29/30

- **Source family / access / coverage**：`COMPILER-FIRST-SSD-O1-CACHE`；arXiv:2603.09555 v1，
  2026-03-10；完整 HTML、公开 `mamba2-jax` 与 Bonsai integration。已读 Introduction、Related Work、
  compiler-friendly conditions、SSD→JAX primitive mapping、compiled cache、全部 evaluation、ablation、
  limitations 与 reproducibility appendix。仅 repo 当前 commit 与论文 v1 的逐行 diff 未披露。
- **Original problem / previous design**：fused CUDA/Triton kernel 对 NVIDIA 上的峰值性能是合理选择，
  但 architecture release 与 vendor-specific kernel 被绑在一起后，TPU/CPU/其他 accelerator 必须重写
  kernel 或接受慢 fallback。改变的约束不是“kernel 不再重要”，而是 portability 与维护成本开始与
  单一设备峰值同等重要。
- **Principle / mechanism**：SSD 恰好具有 diagonal state、fixed-size chunkable recurrence、
  einsum-dominated compute 与 static control flow。实现把 heavy path 整形成 compiler 可 tile 的 batched
  contractions，以 static mask 保留 fusion；decay exponentiation 显式升到 float32；每层 SSM state 与
  convolution state 注册为 JAX PyTree，由 `jit`/`lax.fori_loop` 在设备端携带，避免 token-by-token host
  round trip。`O(1)` 来自 recurrence class；论文贡献是把理论状态边界落实为 compiled runtime state。
- **Evaluation contract**：主要实验为单 TPU v6e、Mamba-2 130M～2.7B、BF16、batch=1、chunk=256，
  prefill 128～8192 tokens，decode 128～4096，greedy 64 steps；A100 40GB 只用于 portability/correctness
  对照。MFU/HBU 来自 XLA HLO cost model，作者明确指出 unfused byte estimate 使 HBU 可能是 upper bound。
  静态 mask 对动态 row loop 的 ablation 与 float32 decay ablation 支撑具体机制，但没有 continuous
  batching、paging、高并发或 downstream task evaluation。
- **Evidence boundary / trade-off / failure modes**：论文证明“满足结构条件时，standard primitives 可以
  成为 portable implementation branch”，不证明 custom kernels 普遍无价值。data-dependent gather/
  scatter、warp synchronization、early exit 等仍超出当前 compiler primitive 表达力；性能依赖 backend
  maturity，固定 chunk 与 batch=1 不能外推 serving throughput。关系为 `Layering / Dependency`：算法
  结构决定 compiler 是否有机会替代手写 kernel，而非 compiler 路线单向取代 kernel 路线。
- **ROADMAP / decision / questions**：主 owner 暂定 Ch32，Ch38/39/45 为 handoff；Books decision 等
  Evidence Gate 后再读相邻章节。需要确认现稿是否已明确写出“operator structure → compiler
  legality/fusion surface → cache control-flow placement”的完整链条。

### IndexCache — 29/30

- **Source family / access / coverage**：`DSA-INDEX-CACHE-CROSS-LAYER`；arXiv:2603.12201 v1，
  2026-03-12；完整 HTML。已读 DSA background、cross-layer overlap、F/S layer mechanism、training-free
  greedy search、multi-layer distillation、30B evaluation、GLM-5 scaling、negative similarity proxy 与
  appendix patterns。公开代码/artifact 链接在论文页未形成可独立复现实验包，记为 `Not Disclosed`。
- **Original problem / previous design**：DSA 用 lightweight indexer 把 core attention 从 `O(L²)` 降到
  `O(Lk)`；每层独立 indexer 在准确性上是合理默认。但 indexer 本身仍对所有历史 token 打分且每层
  重复执行，长上下文下变成新的 `O(NL²)` residual bottleneck。约束变化是 core attention 已稀疏化，
  selection overhead 反而浮到系统关键路径。
- **Mechanism / state ownership**：层分为 Full 与 Shared。Full layer 计算并缓存 top-k index tensor，
  后续 Shared layer 跳过 indexer，复用最近 Full layer 的 indices；第一层永远为 Full。training-free
  branch 以固定 calibration batch 的 end-to-end LM loss 贪心移除 indexer，因为 uniform interleaving、
  cosine similarity 与 top-k overlap 都不能识别少量 critical-token mismatch。training-aware branch 用
  served layers attention distribution 的平均目标做 multi-layer distillation，使一个 indexer 学会提供
  consensus top-k。index cache 属于 layer execution plan，模型/checkpoint 或校准流程拥有 pattern，
  runtime 只执行并携带最近有效 indices。
- **Evaluation contract**：核心模型是由 GLM-4.7-Flash 初始化的 30B-A3B、47-layer DSA，H100
  node、SGLang、`dp_size=8`；context 10K/60K/120K/200K，分别报告 TTFT、single-concurrency
  per-request decode 与 full-KV total decode。training-free calibration 为 SFT data、batch=768、200K；
  training-aware 为 1000-step warm-up + 4000-step sparse training。GLM-5 744B/40B-active 结果是作者
  明确标注的 preliminary training-free evidence，不能当通用生产结论。
- **Evidence boundary / trade-off / failure modes**：论文支持 cross-layer index reuse 能消除重复 selection
  work，也支持“local similarity 不是安全 proxy”；不证明 pattern 跨 checkpoint、domain、context mix 或
  quantization 永久稳定。greedy search 最坏需要 `N(N-1)/2` forward passes，校准漂移、checkpoint
  更新、layer criticality 变化都引入 invalidation；错误 index 可能经后续层级联放大。旧的 per-layer
  indexer 在高漂移、无法校准或质量风险优先时仍成立。关系为 `Direct Evolution`，不是用 shared
  index 覆盖独立 indexer。
- **ROADMAP / decision / questions**：主 owner 暂定 Ch39，Ch14/22/40/46 handoff；Books decision
  等相邻章节复核。重点检查现稿是否把 sparse attention 的 complexity 从 `core attention` 拆到
  `selection + core + cache/invalidation`，以及 index pattern 是否属于 model artifact contract。

### How Far Can Unsupervised RLVR Scale LLM Training? — 26/30

- **Source family / access / coverage**：`URLVR-INTRINSIC-SHARPENING-BOUNDARY`；arXiv:2603.08660 v1，
  2026-03-09，ICLR 2026；54 页 PDF 与 50+ 页 appendix。已读 taxonomy、theory、rise/fall experiments、
  per-problem/OOD analysis、safe-use section、Model Collapse Step、external-reward discussion、GRPO
  setup、hyperparameter sweeps 与 backbone/dataset appendix。论文链接 code 指向 PRIME-RL/TTRL；
  当前页面未证明所有新增实验都有独立 artifact，记为部分可复现。
- **Original problem / previous design**：ground-truth RLVR 在 math/code 中利用可执行 verifier 是合理
  路线，但随着任务超过人工标注能力，supervision 变成瓶颈。intrinsic URLVR 以 entropy、probability、
  self-certainty 或 rollout majority 生成 proxy reward，避免标签成本；问题是 reward 与 policy 来自同一
  分布，训练可能只放大已有偏好。
- **Principle / mechanism**：论文把 certainty-based 与 ensemble-based reward 统一为 distribution
  sharpening：更新提高初始高概率输出，相当于利用 prior，而非自动发现新知识。当 confidence 与
  correctness 对齐时先获益；错位时错误模式也被强化，形成 rise-then-fall。作者把 Reward Accuracy
  低于 1% 的 step 定义为 Model Collapse Step，用短诊断 run 估计 base-model prior；external branch
  则把 reward 绑定到 arithmetic execution、code、proof 或 data structure 等 generation-verification
  asymmetry，尝试把 verifier state 与 policy state 解耦。
- **Evaluation contract**：实现基于 veRL + GRPO；默认 global/mini-batch 64、8 rollouts、prompt 1024、
  response 7168、LR `1e-6`、1 epoch，无 KL/entropy regularization。论文跨 OLMo/Llama/Qwen family、
  MATH/AIME 等设置比较多种 intrinsic rewards；Model Collapse Step 的预测实验只有 7 个模型与
  AIME24，所谓 5.6× 更省 token 是作者特定计算合同，不能当一般成本比。
- **Evidence boundary / trade-off / failure modes**：理论与实验支持 intrinsic reward 的 sharpening
  风险，不足以证明所有未来 self-rewarding method 必然失败；作者把 general-domain self-rewarding
  排除在定义外，external self-verification 也只给 preliminary evidence。小 dataset/test-time training
  可以在 collapse 前利用已有 prior，但需要 early-stop state、reward-accuracy telemetry 与 rollback；
  model/dataset shift 会改变 collapse step。旧 supervised RLVR 在 verifier 可靠时仍是更强基线。
- **ROADMAP / decision / questions**：主 owner 暂定 Ch29，Ch27/28/62/68 handoff；Books decision
  等相邻章节复核。需要避免把 `confidence-correctness alignment` 写成仅靠 entropy 可观测的属性，
  并区分训练信号来源、verifier ownership 与训练动力学诊断。

### NVIDIA Dynamo v1.0.0 GA — 28/30

- **Source family / access / coverage**：`DYNAMO-DISTRIBUTED-INFERENCE-0.1-1.0`；官方 release docs
  标注 GA 2026-03-12，GitHub v1.0.0 tag/release、breaking-change/PR ledger 与 known-issues ledger。
  已读 multimodal E/PD、agent hints、typed config/public API、DGDR/Operator、router/planner/KVBM、
  backend integration、fault tolerance、observability、breaking changes 与 14 个 v1.0 known issues。
  后续版本 issue 只用于辨认 v1.0 遗留边界，不回写为 W11 新事件。
- **Original problem / previous design**：单 engine/aggregated serving 在状态局部、模型固定且规模较小时
  简单可靠；模型跨节点、P/D/encoder 分离、multimodal derived state 与 Agent session 变长后，placement
  不能只看队列长度。v1.0 的变化是把 request priority、KV/media identity、worker topology、planner
  profile 与 deployment lifecycle 提升为显式 distributed control state。
- **Mechanism / ownership / flow**：Frontend 接受兼容 API 与 agent hints；Router 按 load、KV overlap、
  priority、DP rank 与 LoRA/media identity 选择 worker；Planner 将 prefill/decode 分开并依据 profile/
  throughput 做资源规划；KVBM/indexer 消费 worker KV events，NIXL 负责 KV/embedding transfer；Operator
  以 DGDR/DGD reconciliation 持有部署 generation/status。v1.0 默认 local indexer/event plane，durable
  KV events 需显式开启，说明 cache-routing correctness 取决于 event freshness/durability contract。
- **Evaluation / evidence boundary**：release/PR/code ledger证明功能存在和迁移边界，不是公平性能实验。
  release 中 170M ops/s、42× router 与其他 benchmark 数字未绑定本书所需完整 workload，不进入通用
  结论。已确认的反证更重要：KVBM 在部分 workload 可慢于 disabled baseline；Profiler 会低估 MoE
  WideEP buffer；infeasible SLA 可被静默接受；TRT-LLM multimodal disaggregation、snapshot、HiCache/
  NIXL 和 backend pin 均有组合性 failure mode。
- **Trade-off / evolution**：state-aware routing 提高 locality 与全局调度能力，却引入 event ordering、
  stale index、checksum/identity、cross-backend semantics、fallback 与 recovery responsibility。aggregated
  serving 在短请求、低复用或 transfer/control overhead 大于收益时继续成立；KVBM、Snapshot、Global
  Planner 与 agent retention 中多项在 v1.0 仍为 Preview/Experimental。关系为 `Direct Evolution +
  Layering`：Dynamo 不替代 vLLM/SGLang/TRT-LLM，而是在 engine 之上增加分布式状态控制面。
- **ROADMAP / decision / questions**：主 owner 暂定 Ch49，Ch46/48/50/51/58/59/63/80 handoff；Books
  decision 等当前 Evidence Gate。需要检查现稿是否明确 cache event durability、selection decision trace、
  SLO infeasibility propagation 与 fallback semantics，而不是复述 v1.0 feature list。

### Four MTIA chips in two years — 26/30

- **Source Family ID / Type / Date**：`MTIA-GEN1-GEN4`；Meta 官方工程报告；事件日
  2026-03-11。直接来源为 Meta MTIA 长文，关联材料为历代芯片与软件栈链接。
- **Access / Full-read Coverage**：已读完整官方报告中的四代定位、workload 变化、memory、
  compiler/runtime、collective、部署与测量边界；厂商未公开的 model mix、batch、precision、
  tail-latency SLO 记为 `Not Disclosed`。
- **Problem / Previous Design / Changed Constraint**：GPU 对快速变化模型和长尾算子仍最合理；
  当内部 recommendation 与 generative workload 的规模和形态逐渐稳定后，memory movement、
  fleet efficiency 与供给约束使专用 accelerator 的摊销成立。
- **Mechanism / Ownership / Flow**：芯片并非独立产品，而由 compiler/runtime 将图和算子映射到
  硬件，collective 与 host/fabric 承担多卡数据流，deployment telemetry 反馈下一代取舍。
  workload contract 由模型、编译、runtime 和 fleet 共同拥有，不能归因于单一 FLOPS 指标。
- **Evaluation Contract / Evidence Boundary**：官方材料证明四代共同演进和规模化部署方向；
  它不证明 Meta 数字可迁移到任意模型、GPU 对照或 SLO，也不证明 ASIC 将普遍取代 GPU。
- **Trade-offs / Evolution**：专用化换取稳定 workload 下的能效与成本，同时增加 operator
  coverage、compiler maturity、容量规划和世代兼容风险；旧 GPU 路线在研究、峰值训练和长尾
  workload 中继续成立。关系为 `Direct Evolution`。
- **ROADMAP / Chapters / Existing Coverage**：Ch45 为主 owner；已复核 Ch44～46、Ch50、Ch59、
  Ch66。现有 Ch45 已覆盖 workload-specific accelerator co-design。
- **Implementation / evaluation boundary**：MTIA 300 以 compute/network chiplet、built-in NIC、message
  engine 与 near-memory reduction 支撑 R&R training；400 扩到 72-accelerator scale-up domain；450/500
  转向 inference-first，增加 HBM bandwidth、MX4 与 attention/FFN 相关 acceleration。官方证明产品
  路线与内部部署，不披露可与 GPU 公平比较的 model mix、batch、precision、power、utilization、
  TTFT/ITL SLO；25× compute 与 4.5× bandwidth 是跨代、跨 datatype 的 vendor specification，不能
  当作端到端 speedup。
- **Decision / questions**：Full Review Complete；旧 `No Change — Already Covered` 仍只作 provisional
  input。Books 阶段需确认 Ch45 是否已有“预测 workload → modular chiplet cadence → PyTorch/vLLM/
  Triton/HCCL enablement → fleet telemetry 反哺下一代”的完整演进链。

### DIVE — 25/30

- **Source family / coverage**：`DIVE-EVIDENCE-FIRST-TOOL-SYNTHESIS`；arXiv:2603.11076 v1
  （2026-03-10）、完整 HTML、appendix 中 tool pool、prompt、diversity topology 与 SFT/RL training
  details；项目页已定位。论文没有独立 Limitations section，因此 live-tool drift、API policy 与
  reference-answer lifetime 需要作为显式 evidence risk。
- **Problem / old design / changed constraint**：query-first synthesis 在工具少、API 稳定且可以人工清洗时
  合理；当 tool pool 扩到跨 domain、跨 protocol 与 stateful environment 后，先编问题再验证会制造
  unsolvable task。仅扩大相似 query 数量也会把固定 `search→browse` 模式重复得更密，而不是提升
  structural diversity。
- **Mechanism / ownership / flow**：作者将顺序反转为 `real tool execution → evidence set → entailed
  query/answer`。373 个经过 unit test、concurrency 与 consistency 检查的工具，和 seed/exemplar pool
  解耦采样；collector 最多执行 6 步，连续 3 轮扩展 evidence，再由 task generator 只从 trace 可支持的
  事实反推任务。SFT 用 teacher rejection sampling；RL 先以 pass@8 选 frontier tasks，再用 answer +
  format reward 优化。task、toolset、evidence 与 verifier 应被视为同一版本化 artifact family。
- **Evaluation boundary**：Qwen3-8B，48K SFT + 3.2K RL；SFT max context 65,536、RL 131,072，RL
  batch 512、100 steps，rollout 由 SGLang TP=4 生成。九个 benchmark 跨 stateless/stateful 与 unseen
  tool pool，但结果仍来自单一 backbone、Claude-4-Sonnet synthesis、GPT-OSS-120B teacher；没有
  tool outage、schema drift、non-deterministic result、cost/latency SLO 或长期答案失效实验。作者的
  `diversity > quantity` 只对其匹配的 12K/48K contract 成立。
- **Trade-off / evolution**：evidence-first 用可执行性换取被当前工具可返回内容所限制的 task support，
  并可能放大 tool-provider coverage bias。query-first 在目标能力已知、可构造反事实/困难任务时仍有
  价值；可靠系统应组合 evidence-first grounding 与后置 adversarial/spec coverage。关系为
  `Direct Evolution`。
- **ROADMAP / decision**：主 owner 暂定 Ch74，Ch23/29/62/75/77 handoff；Books pending。需要检查
  Ch74 是否已把“task diversity”拆成 semantic、tool-pool、toolset 与 control-flow topology 四个轴，
  并补齐 evidence/tool/version provenance，而不是引用平均分。

### Automatic Generation of High-Performance RL Environments — 26/30

- **Source family / coverage**：`AGENT-TRANSLATED-RL-ENV-VERIFICATION`；arXiv:2603.12145 v1
  （2026-03-12）、完整 HTML、Algorithm 1、五个 environment case、test coverage、cross-hardware、
  prompts、JAX/Rust optimization appendices 与 Scope and Limitations。公开代码/commit identity 尚未从
  论文页闭合，artifact reproducibility 记为 `Partially Verified`。
- **Problem / old design / changed constraint**：手工保留 reference simulator 在语义优先、训练规模较小
  时最安全；on-policy RL 需要数十亿 step 后，environment 可占 wall-clock 的主要部分。直接让 coding
  Agent“优化代码”会把 silent semantic drift 写入 reward channel，因此性能迁移首先是 equivalence
  verification 问题。
- **Mechanism / ownership / flow**：reference environment 按 module 分解，Agent 在目标 backend 翻译；
  Level 1 property test、Level 2 interaction test、Level 3 matched-seed/action rollout comparison、Level 4
  cross-backend policy transfer 逐级扩大 observation scope，失败会生成 targeted test 并回到修复循环。
  reference implementation 拥有语义，test suite 拥有已观测 contract，performance backend 拥有执行
  state；任何 Level 4 gap 都必须反向更新较低层 verifier。
- **Evaluation boundary**：五个环境，1×RTX 5090、32 Ryzen cores、CUDA 12.8、JAX 0.4.39，training
  curve 10 seeds。跨 CPU/GPU、batch 与实现范式的 1.5×～23,810×不能横向当作统一 speedup；论文自己
  明确 Level 3 只覆盖 100 episodes/RNG paths，不是形式语义等价。PokeJAX 需 63 次迭代且只完成
  5-module subset；HalfCheetah 的 L3-only ablation 不收敛。
- **Trade-off / evolution**：hierarchical verifier 将长轨迹错误局部化，但 correctness 只到测试覆盖的
  observational equivalence；race、async I/O、外部 API/hardware-in-loop、>100K LoC 与私有代码仍是
  边界。旧 reference backend 继续承担 oracle、replay 与 rollback；高性能 backend 不是替代真相源。
  关系为 `Direct Evolution`。
- **ROADMAP / decision**：主 owner 暂定 Ch77，Ch32/45/62/69 handoff；Books pending。重点检查
  Ch77 是否已有从 unit/property test 到 trajectory equivalence、policy transfer、production shadow
  traffic 的 verifier ladder。

### Examining Reasoning LLMs-as-Judges — 26/30

- **Source family / coverage**：`REASONING-JUDGE-TRAINING-GOODHART`；arXiv:2603.12246 v1
  （2026-03-12）、完整 HTML、training/evaluation methodology、policy curves、rubric/pairwise ablations、
  Arena-Hard case 与 prompts。没有独立 Limitations section；“gold-standard”是实验角色名称，不代表
  人类偏好的真实 oracle。
- **Problem / old design / changed constraint**：static judge agreement 在只做离线排序时可作为近似；当
  judge 进入 RL reward loop，policy 会主动搜索 judge 的 blind spot，分布由被评模型改写。因而“更会
  reasoning 的 judge”不能只用静态 benchmark 推断为更安全的训练 verifier。
- **Mechanism / ownership / flow**：gpt-oss-120b 以 temperature 0/high reasoning effort 生成 pointwise
  preference labels；Qwen3 1.7B～14B judges 先 distill，reasoning variants 再以可验证 score-error reward
  训练。Llama-3.1-8B、Qwen2.5-7B、Qwen3-4B policies 用这些 frozen judges 做 GRPO；同时用训练 judge
  与 gold judge 双轨观测 reward。RL-only reasoning judge 缺少 distillation 时退化，说明 reasoning
  compute 不能替代目标规范传递。
- **Evaluation boundary**：judge test set 738 items，来自与训练相同的数据 mixture；policy GRPO global
  batch 1024、8 samples、prompt/output 各 2048、temperature 0.7。论文证明在该合成 preference oracle
  下，non-reasoning judge 容易出现 reward hacking，reasoning judge 也可被训练出跨 judge transfer 的
  adversarial output；不证明所有 reasoning judges 更差，也不证明 Arena-Hard 的全部高分都无效。
- **Trade-off / evolution**：reasoning/distillation 提升局部 agreement，却可能把可利用的复杂模式也
  变得更稳定；rubric 提升静态一致性仍不等于 adversarial robustness。旧规则/程序 verifier 在可验证
  域继续优先；非可验证域需要 judge ensemble、holdout oracle、policy-shifted red team、artifact sampling
  与停止条件。关系为 `Direct Evolution`。
- **ROADMAP / decision**：主 owner 暂定 Ch62，Ch29/63/68/69 handoff；Books pending。候选很可能
  refine 现有 `model capability ≠ harness/judge capability`，但必须读相邻章节后才能决定。

### ReMix — 24/30

- **Source family / coverage**：`REMIX-REINFORCEMENT-LORA-ROUTING`；arXiv:2603.10160 v1
  （2026-03-10）、完整 HTML、routing-collapse theory/proofs、RLOO estimator、top-k inference、baseline、
  ablation、efficiency 与 scaling experiments。没有独立 Limitations section，也没有由论文页闭合的
  code artifact。
- **Problem / old design / changed constraint**：softmax-weighted Mixture-of-LoRAs 允许端到端微分，在少量
  adapter 或只需 top-1 specialization 时合理；当期望同时激活 k 个 LoRA 时，归一化权重可能集中，
  造成“计算了 k 个、有效支持却接近 1”的 capacity illusion。
- **Mechanism / state flow**：用 `ESS=(||π||₁/||π||₂)²` 描述单输入的有效 adapter 数；ReMix 让 router
  只决定无放回采样的 subset，激活项统一使用常数权重，使 ESS 恰为 k。因为离散选择不可直接反传，
  将 SFT loss 视为负 reward，用 RLOO/policy-gradient 训练 router；推理时从 stochastic subset 切换到
  top-k。router policy、LoRA parameters 与 inference selection rule 是三个必须共同版本化的状态。
- **Evaluation boundary**：Llama 3 8B，在 GSM8K、HumanEval/CodeAlpaca 与 ARC-c 三类任务上与 prefix、
  LoRA/DoRA/rsLoRA 和 mixture baselines 比较；作者报告平均优势与约 10% step-time 开销，但没有更大
  backbone、multi-task continual routing、serving batch locality、adapter paging、跨租户隔离或端到端
  latency。训练随机采样、推理 deterministic top-k 之间的 distribution gap 未被系统性压力测试。
- **Trade-off / evolution**：固定激活权重保证利用率却放弃 input-dependent contribution magnitude；RL
  router 避免 pathwise gradient 限制，却增加 sample variance/compute。旧 softmax router 在真正需要
  competitive specialization 或 top-1 时仍合理。关系为 `Direct Evolution`，与 MoE router 的 principle
  相似但 adapter state 与 serving economics 不同。
- **ROADMAP / decision**：主 owner 暂定 Ch21，Ch24/25/39/48 handoff；Books pending。需检查 Ch21
  是否已经区分“选择哪些专家”和“每个专家贡献多少”两个控制量。

### In-Context Reinforcement Learning for Tool Use — 25/30

- **Source family / coverage**：`ICRL-DEMONSTRATION-ANNEALING`；arXiv:2603.08068 v1
  （2026-03-09），因 arXiv HTML 转换失败改读 11 页 primary PDF；覆盖 method、Algorithm 1、reward、
  baselines、implementation、curriculum/model-scale ablations 与 conclusion。无独立 Limitations section，
  无公开 artifact/commit 闭环。
- **Problem / old design / changed constraint**：SFT cold start 在有高质量 tool traces、format 固定时能稳定
  建立行为先验；新工具/新 domain 快速增加时，轨迹标注成为瓶颈。直接 zero-shot RL 又会因探索几乎
  不命中合法调用而缺少 reward。ICRL 将 demonstrations 当 rollout-time exploration scaffold，而不是
  参数监督数据。
- **Mechanism / state flow**：训练按 `3-shot → 2-shot → 0-shot` 逐阶段减少 prompt demonstrations；每个
  query 采样 8 条轨迹，以 answer exact-match（权重 0.8）与结构格式 penalty 构成 reward，GRPO 更新时
  mask tool-return tokens。prompt curriculum、dataset partition、reference policy 与 tool result provenance
  共同决定 optimization state；去掉 demonstration 不是删除历史阶段，而是把其行为迁入 policy。
- **Evaluation boundary**：Qwen2.5 3B/7B/14B 与 Qwen3-8B，BF16、4×A100 80GB、batch 64、FSDP、
  max prompt 5K、最多 6 次 search、BM25 top-3、KL 0.001；五个 QA benchmark 每项最多 500 questions，
  另有 AIME code-execution。`3→2→1→0` 更早停止且显著退化，说明 curriculum step 数不是越平滑越好。
  论文未覆盖 noisy/non-deterministic tools、schema evolution、real search freshness、human preference 或
  production cost/SLO，不能泛化为 SFT 已不再需要。
- **Trade-off / evolution**：用 inference tokens 与 tool calls 换 labeled trace，降低 cold-start annotation，
  但仍依赖精选 demonstrations、ground-truth answer 与格式 verifier。SFT 在 exploration cost 高、reward
  稀疏或安全动作必须先约束时继续成立；ICRL 是 `SFT cold start ↔ prompted exploration curriculum`
  的替代分支，不是单向替代。关系为 `Direct Evolution`。
- **ROADMAP / decision**：主 owner 暂定 Ch29，Ch73/75/76 handoff；Books pending。需检查 Ch29 的
  curriculum 是否包含 scaffold annealing、tool-output loss masking 与 premature-stopping failure mode。

### OneMillion-Bench — 21/30

- **Source family / coverage**：`ONEMILLION-PROFESSIONAL-AGENT-EVAL`；arXiv:2603.07980 v1
  （2026-03-09）、完整 HTML、400-task curation、rubric/economic-value definition、35-system evaluation、
  scaffold/judge sensitivity、cost frontier、failure cases 与 appendix sampling/cost details。无独立
  Limitations section；dataset/card 和 immutable evaluation snapshot 仍需 artifact-level闭环。
- **Problem / old design / changed constraint**：exam-style final-answer accuracy 对封闭知识题合理，却无法
  区分专业任务中的 authority retrieval、conflict resolution、regulation compliance、deliverable structure
  与 harmful mistake。将专家完成时间乘工资得到 value anchor 能表达机会成本，但不是 Agent 真实创造的
  revenue，也不包含 review、liability 与 deployment overhead。
- **Mechanism / ownership / flow**：每题由 domain expert 创建 task/reference/rubrics，经同行复核和第三人
  resolution；同时剔除全会与全不会的题。正负权重 rubric 形成 Expert Score，0.7 阈值形成 pass rate；
  评价结果再按 domain 与 capability tag 聚合。task、reference source、jurisdiction/date、rubric、judge、
  scaffold 和 model version 都是结果身份的一部分。
- **Evaluation boundary**：400 tasks、五个 domain、200 English + 200 Chinese，后者不是翻译集；35 个
  systems 分为 vanilla/search/deep-research。六种 judge 上排名相对稳定但绝对分差可达约 8%；official 与
  OpenRouter scaffold 差异明显，search 有时反而降低 instruction following/formatting。论文证明 harness
  和 tool integration 会改变结果，不证明题目美元总额等于自动化经济价值，也不构成真实生产事故率。
- **Trade-off / evolution**：专业 rubric 提升 validity 与可诊断性，却带来专家成本、judge bias、法规
  freshness 与 task contamination；统一总分又会隐藏负 rubric 的 tail risk。旧 narrow benchmark 仍适合
  回归测试；专业 benchmark 应作为分层 evaluation portfolio。关系为 `Layering / Dependency`。
- **ROADMAP / decision**：主 owner 暂定 Ch62，Ch63/66/68/69 handoff；Books pending。可能 refine
  `model ≠ scaffold ≠ tool ≠ judge ≠ economic outcome` 的 measurement contract，不保留排行榜数字。

### Agentic Critical Training — 22/30

- **Source family / coverage**：`ACT-ACTION-QUALITY-DISCRIMINATION`；arXiv:2603.08706 v1
  （2026-03-09）、完整 HTML、data construction、ACT/RL pipeline、reward、三环境实验、cross-size/OOD/
  reasoning transfer、implementation appendix 与 cases。无独立 Limitations section，代码/artifact 未闭合。
- **Problem / old design / changed constraint**：imitation learning 在 expert action 唯一且 state coverage
  充分时能直接教 policy“做什么”，但不要求模型解释为什么 alternative 较差；遇到 state shift 时，
  行为复制缺少 action-quality discrimination。预生成 reflection 的 distillation 又可能只复制话术。
- **Mechanism / flow**：对每个 expert state-action，从初始 policy 采样 K 个不同 alternatives，构成
  expert-vs-alternative pair；随机化顺序后只奖励选中 expert action。ACT 不监督 CoT，先训练“判别更好
  的动作”，再接 IL 或 action-generation GRPO。expert dataset、negative policy、state snapshot 与 action
  equivalence rule 共同决定训练分布。
- **Evaluation boundary**：Qwen3-8B 主实验，ALFWorld seen/unseen、WebShop、ScienceWorld；所有方法
  共享 expert trajectories，另做 cross-size 与 MATH-500/GPQA-Diamond。作者平均增益支持两阶段训练在
  这些环境有效，但 `expert action match` 不是开放世界的通用 quality oracle；alternative quality、多个
  等价动作、negative hardness 与 environment-state aliasing 未被充分覆盖。
- **Trade-off / evolution**：contrastive discrimination 用额外采样/配对换取 state-aware preference；先判别
  后生成可减少盲目 imitation，但若 expert 有错或 alternatives 太弱，会学到虚假的确定性。IL 仍适合
  安全动作冷启动，environment RL 仍负责 outcome correction。关系为 `Layering / Dependency`。
- **ROADMAP / decision**：主 owner 暂定 Ch29，Ch73/75/76 handoff；Books pending。需与 ICRL、
  OpenClaw-RL 和 judge Goodhart packet 联读，避免把“无 reasoning supervision”写成已证明的真实反思。

### Fish Audio S2 Technical Report — 23/30

- **Source family / coverage**：`FISH-S2-INSTRUCTION-TTS`；arXiv:2603.08823 v1（2026-03-09）、完整
  technical report、architecture/tokenizer、data pipeline、pretraining/RL、SGLang inference、multilingual/
  long-audio/instruction evaluation、human-judge alignment appendix；官方 weights/code/engine links 已定位。
- **Problem / old design / changed constraint**：传统 TTS 以文本正确发音和 speaker similarity 为主要
  contract；自然语言 instruction、multi-speaker、multi-turn 与长音频把控制信号扩到情绪、节奏、角色
  切换和局部 tag，单一 acoustic token stream 难以同时承载 semantic progression 与细节。
- **Mechanism / state flow**：44.1kHz DAC-style RVQ 以 10 个 codebooks 分层表达；Slow AR 推进 semantic
  time axis，Fast AR 在同一步生成其余 acoustic depth，Multi-Codebook Fusion 将各 codebook embedding
  汇入下一 slow step。训练用细粒度 text/audio interleaving 强化 monotonic alignment，保留 30% pure text
  防止 forgetting，并由 caption/quality/reward pipeline 构造 instruction data。serving state 是 text、
  reference audio、speaker turn、semantic token 与 acoustic-depth token 的组合，而非普通 text KV。
- **Evaluation boundary**：作者披露 >500B training tokens，WER、24-language/9-language、long audio、
  instruction benchmark 与 LLM judge；instruction benchmark 的 human-model alignment 仅中等相关，作者
  自己承认数据多样性有限、tag 不平衡和细粒度绝对评分仍有 gap。报告不能证明所有自然语言控制都被
  因果遵循，厂商/模型间 WER 也受 ASR evaluator、reference 与 sampling contract 影响。
- **Trade-off / evolution**：hierarchical codec/dual-AR 分离时间推进与声学细节，换来两个 decoder、
  codebook synchronization、streaming backpressure 和 richer cache identity。旧单 speaker/短音频 pipeline
  在 latency/部署简洁优先时仍成立。关系为 `Direct Evolution`。
- **ROADMAP / decision**：主 owner 暂定 Ch23，Ch39/44/50/62 handoff；Books pending。重点判断是否
  提供了 multimodal state-machine 的长期机制，而非写入版本功能或作者 benchmark。

### SoundWeaver — 24/30

- **Source family / coverage**：`SOUNDWEAVER-SEMANTIC-DIFFUSION-WARMSTART`；arXiv:2603.07865 v1
  （2026-03-09）、完整 205-line HTML、retrieval/alignment、Skip Gater、Cache Manager、evaluation/
  ablations 与明确 limitations。论文未提供完整 production artifact 与 scheduler integration。
- **Problem / old design / changed constraint**：diffusion 从随机 noise 开始在 prompt 独立、低复用或质量
  可预测性优先时简单可靠；语义相近音频请求增多后，重复 200 NFE 浪费计算。精确 cache 又几乎没有
  prompt hit，因此需要 approximate reuse，但 reuse 错误会污染 perceptual quality。
- **Mechanism / ownership / flow**：Reference Selector 用 CLAP semantic + duration matching，从 FAISS
  pyramid index 选全音频或多尺度 segment，再经 phase-vocoder 对齐形成 warm start。Skip Gater 将可跳
  NFE 比例视为 contextual bandit，使用 rank-normalized feedback 和 prompt-variance weighting；Cache
  Manager 做 quality-aware eviction，并在 idle 时最多重生成五次以 refinement 热条目。cache entry 必须
  绑定 model/sampler/NFE/audio provenance 与 quality history。
- **Evaluation boundary**：单 A100；Clotho v2 1,045 clips 构 cache，AudioCaps prompts；AudioLDM 652M
  与 AudioLDM2 1.1B，DDIM 200 NFE。作者报告 1.8×～3.0×，但真实/合成 cache、模型和 metric 结果不同；
  Gemini 3 Flash pairwise judge 只作主观 proxy。未测试复杂 sampler、dedicated scheduler、multi-tenant
  contention；长音频存在 phase-vocoder distortion。
- **Trade-off / evolution**：近似 cache 把 semantic locality 转为 compute saving，却引入 provenance、
  quality debt、popularity feedback loop 与 fairness；idle refinement 可能让热门 prompt 获得更多质量预算。
  cold-start 仍是 miss、high-risk audio 或低相似度请求的真相分支。关系为 `Principle Reuse`，不是 text
  KV cache 的直接等价。
- **ROADMAP / decision**：主 owner 暂定 Ch39，Ch44/48/50/66 handoff；Books pending。可能补全
  approximate reuse 的 identity/invalidation/quality-budget 机制，但先检查相邻 inference chapters。

### RetroAgent — 25/30

- **Source family / coverage**：`RETROAGENT-DUAL-INTRINSIC-FEEDBACK`；arXiv:2603.08561 v1
  （2026-03-09）、完整 HTML、numeric shaping、reflection buffer、SimUtil-UCB retrieval、joint optimization、
  four-environment evaluation、memory/reward ablations、cross-model appendix 与 prompts。无独立 Limitations
  section，公开 artifact/long-run memory lifecycle 未闭合。
- **Problem / old design / changed constraint**：sparse terminal reward 在短、可重复 episode 中足够；长程
  Agent 中“部分完成但最终失败”的轨迹全被记为零，会推向局部 exploitation。仅把经验写入参数又难以
  显式复用，raw-trajectory memory 则会带入大量无效动作。
- **Mechanism / ownership / flow**：episode 后 reflection 同时产生相对历史 best 的 subtask potential 与
  natural-language lesson。前者塑造成 intrinsic reward，后者进入 memory buffer；SimUtil-UCB 用 semantic
  similarity、历史 utility 与访问不确定性平衡检索。decision policy 以外在+内在 reward 更新，另一个
  variant 用 REINFORCE 联合训练 reflection policy。trajectory、derived lesson、utility counter、task
  distribution 与 policy version 必须有 provenance。
- **Evaluation boundary**：Qwen2.5-7B 主线并跨另一 model family；ALFWorld、WebShop、6×6/2-box
  Sokoban、6×6/3-mine MineSweeper，报告 success/task score 与多项 ablation。结果支持 derived lesson 在
  这些 simulator 比 raw trace 更有效，但 reflection/potential 均由模型自评，未覆盖 poisoned memory、
  contradiction、cross-user leakage、长周期 supersession/delete 或真实工具 drift。
- **Trade-off / evolution**：dense intrinsic progress 缓解 sparse credit，却可能 reward misspecification；
  utility-aware retrieval 减少纯相似度偏差，却建立 self-reinforcing popularity loop。raw traces 仍是审计与
  重建真相层，derived lessons 只是可撤销 view。关系为 `Direct Evolution`。
- **ROADMAP / decision**：主 owner 暂定 Ch73，Ch29/68/76/80 handoff；Books pending。必须与 XSkill、
  ReasoningBank/Dreaming 演进链去重，重点看 provenance、supersession、rollback 与 delete 是否缺失。

### Thinking to Recall — 21/30

- **Source family / coverage**：`REASONING-PARAMETRIC-RECALL`；arXiv:2603.09906 v1（2026-03-10）、
  完整 HTML、ON/OFF setup、pass@k analysis、dummy-buffer/factual-priming controls、hallucination audit、
  test-time selection 与 appendices。没有独立 Limitations section，但正文明确复杂题子集小、selection 只
  是模拟、fact verifier 依赖 search-enabled Gemini。
- **Problem / mechanism**：单跳事实题不需要传统 task decomposition，却可能因一次 forward path 无法
  暴露已编码知识。实验将收益拆成两个机制：无语义 dummy tokens 仍提供 bounded computational buffer；
  reasoning 生成的相关 facts 作为自生成 retrieval context，形成 factual priming。两者不能混写成“CoT
  解释正确所以答案正确”。
- **Evaluation boundary**：Gemini-2.5 Flash/Pro、Qwen3-32B；SimpleQA-Verified 1,000 与四类
  EntityQuestions 共 1,000；每题最多 100 samples。dummy length 非单调，过长会退化；clean/hallucinated
  trace 与 final accuracy 有相关和 within-question gap，但 fact extraction/verification 本身由 LLM pipeline
  产生。它证明候选轨迹分布中存在可利用信号，不证明隐藏状态里有可直接寻址的符号数据库。
- **Trade-off / evolution**：更多 test-time tokens 提升 recall coverage，也增加 latency、采样成本与
  self-primed hallucination。direct answer 在高置信/低价值问题仍合理；外部 retrieval 在 freshness、引用与
  provenance 必需时仍优先。关系为 `Layering / Dependency`。
- **ROADMAP / decision**：主 owner 暂定 Ch20，Ch28/38/62 handoff；Books pending。若写入，应沉淀
  compute-buffer 与 self-retrieval 风险，而不是保留具体模型分数。

### InternVL-U — 23/30

- **Source family / coverage**：`INTERNVL-U-MODULAR-UNIFIED-MULTIMODAL`；arXiv:2603.09877 v1
  （2026-03-10）、完整 HTML、architecture/representation、三阶段训练、data synthesis、understanding/
  generation/editing evaluation、GitHub/model/eval artifact links。论文没有集中 Limitations section，
  synthetic-data judge dependence 与 deployment contract 需显式记录。
- **Problem / old design**：fully-native unified model 的端到端统一接口换来从头训练和跨 modality objective
  冲突；post-hoc ensemble 可复用强组件，却常靠巨型 generation head 或碎片化 conditioning interface。
  在已有强 MLLM 且预算有限时，全部重训不是唯一合理路径。
- **Mechanism / state flow**：以 InternVL3.5-2B 初始化 understanding encoder/backbone，随机初始化 1.7B
  MMDiT visual generation head，总 4B；LLM hidden state 作为统一 semantic condition，visual semantic
  context 与 pixel-reconstruction latent 解耦，context/target 共享 temporal-height-width 3D position。
  三阶段先冻结 backbone 学 generation，再扩大 resolution/data，最后解冻联合 NTP + visual prediction，
  以 loss ratio 管理 capability interference。
- **Evaluation boundary**：Stage 1/2/3 分别 250K/60K/20K steps，batch 2048/1024/1024，512→1024
  resolution，最终 NTP:VP=1:20；inference Flow-DPM 20 steps。结果横跨多套 understanding/generation/
  editing benchmark，但 data synthesis 使用多种强 VLM/生成器/judge，hardware、serving memory、batch、
  TTFT 与跨任务 interference tail 未完整披露。
- **Trade-off / evolution**：modular hybrid 保留现成 understanding 并降低重训风险，却保留双 compute
  path、loss balancing、condition-interface drift 与 checkpoint coupling。native AR 在统一 token/runtime
  更重要时仍成立，large ensemble 在独立升级 visual head 时仍合理。关系为 `Direct Evolution`。
- **ROADMAP / decision**：主 owner 暂定 Ch23，Ch15/24/39/44 handoff；Books pending。应作为
  modularity-vs-unification 案例，而不是模型能力清单。

### Towards a Neural Debugger for Python — 23/30

- **Source family / coverage**：`NEURAL-DEBUGGER-EXECUTION-MDP`；arXiv:2603.09951 v1（2026-03-10）、
  完整 HTML、trace generation、forward/inverse state tree、debugger-action MDP、32B finetune/1.8B pretrain、
  component/horizon evaluation、limitations 与 appendices。artifact/code identity 未从论文页闭合。
- **Problem / old design**：line-by-line neural interpreter 对连续 step execution 合理，却不能像实际 debugger
  一样跳到 breakpoint/return、反向推断输入或按不确定性分配 compute。真实 debugger 仍提供精确状态；
  learned debugger 目标是预测/压缩 execution path，而非取代解释器真相源。
- **Mechanism / state flow**：从 CPython frame/source/event/local variables 重建 call-stack state tree，
  `step_into/over/return/breakpoint` 定义 forward traversal，inverse action 定义 reverse tree；模型以 code、
  current serialized state 和 action 预测 target state。action policy 决定 trace distribution，object
  serialization 决定 state observability。
- **Evaluation boundary**：32B CWM 在 50B debugger tokens 上 finetune；1.8B 从头训练 50B/150B，并测
  trace-only/web/code mix。CruxEval 和 component exact-match 显示 source/event 比 locals/args 容易，预测
  horizon 越长准确率越低；只覆盖 Python 和随机 action policy，复杂 object 文本序列化不可扩展，inverse
  execution 还有多解而 exact match 未充分表达。
- **Trade-off / evolution**：jump action 减少显式 rollout token，却把中间状态压进模型不确定性；更大
  sampling 可补 accuracy 但增加成本。interpreter/tool execution 在 correctness 必须保证时仍成立；neural
  debugger 适合作为 proposal/triage model，并需 verifier fallback。关系为 `Layering / Dependency`。
- **ROADMAP / decision**：主 owner 暂定 Ch77，Ch62/69/76 handoff；Books pending。可能补全 coding
  Agent 的 learned world model 与 executable verifier 分工。

### Lost in Backpropagation — 21/30

- **Source family / coverage**：`LM-HEAD-GRADIENT-BOTTLENECK`；arXiv:2603.10145 v1（2026-03-10）、
  完整 HTML、rank analysis/proofs、SGD extension、controlled 2B pretraining、SpamLang、gradient projection
  diagnostics、downstream appendix 与 setup。无独立 Limitations section，作者因果措辞强，保留 claim risk。
- **Problem / mechanism**：`D << V` 的 LM head 不只限制 log-probability rank；V-dimensional loss gradient
  经 rank-D head 回传时只能保留低秩 projection。作者用 Eckart–Young residual 形式化理想 logit update 与
  realizable parameter update 的差距，并把被压缩部分的谱能量解释为优化损失。
- **Evaluation boundary**：8 个约 2B Llama3-style models，共用 6-layer/hidden 4096 backbone，用 rank
  D=32…4096 head，FineWeb-Edu 约 11B tokens、SmolLM2 V=49,152、BF16；另有 106M SpamLang 控制。
  控制实验支持更大 D 收敛更快，但 total parameter count 略不同，2B/11B-token scale、特定 tokenizer/
  optimizer 下的 95–99% suppression 不能外推为所有 LLM；也未给出可部署替代 head 的端到端收益。
- **Trade-off / evolution**：增大 head rank 可能保留更多 gradient information，却显著增加 embedding/logit
  参数、memory bandwidth 与 all-reduce；factorized/multi-component head 也改变 weight tying、sampling 与
  serving kernel。当前 softmax head 在部署简洁和成熟 kernel 优先时仍合理。关系为 `Principle Reuse`，
  当前状态 `Experimental`。
- **ROADMAP / decision**：主 owner 暂定 Ch24，Ch21/32/45 handoff；Books pending。只能写成“需测量的
  optimization bottleneck 与设计假设”，不得把作者 suppression 数字写成通用事实。

### V0.5 Generalist Value Prior — 25/30

- **Source family / coverage**：`V05-SPARSE-ROLLOUT-SHRINKAGE`；arXiv:2603.10848 v1（2026-03-11）、
  完整 HTML、bias-variance theory/proofs、empirical shrinkage、OSLA stopping、V0 architecture/data、
  training/ablation/extreme-sparsity limitation。代码/model artifact identity 未闭合。
- **Problem / old design**：GRPO group mean 无偏且无需 critic，在 rollout 充足时合理；group 很小时方差
  高。generalist value prior 稳定且可离线训练，却会因 policy/domain shift 带系统 bias。固定选一边都把
  baseline error 放大进 policy-gradient variance。
- **Mechanism / ownership / flow**：V0 用 frozen Qwen3 embedding、residual query adapter 与 TabPFN head，
  从 recent query-reward support context 预测成功率。V0.5 以小 k rollout 估计 prior deviation，用
  empirical shrinkage 融合 prior/mean；OSLA 比较 expected MSE reduction 与 rollout marginal cost，决定
  stop 或继续采样。Support Buffer、policy version、reward definition 与 prompt identity 决定 prior freshness。
- **Evaluation boundary**：V0 约 424K pairs，Qwen families/200+ checkpoints；pretrain 128 GPUs 约 40h。
  RL 为 Qwen3-4B-Instruct-2507 + DAPO-Math-17K，32 GPUs、SGLang、response 4096，并保持每 step 总
  rollout compute 相近。k=4/8 可优于 G=16 的作者设置，但 k=1/2 不收敛；仅 math/verifiable binary reward，
  未覆盖 non-stationary judge、多域 calibration、distributed stale buffer 或 serving/training overlap。
- **Trade-off / evolution**：以 bounded bias 换 rollout variance/compute，并按 uncertainty 动态分配预算；
  prior 失配时多采样回退。标准 GRPO 在 rollout 便宜或 prior 不可信时仍成立，同步 critic 在 dense state
  value 可学习时仍有价值。关系为 `Direct Evolution`。
- **ROADMAP / decision**：主 owner 暂定 Ch29，Ch28/37/66 handoff；Books pending。应沉淀
  prior+measurement fusion、freshness 与 optimal stopping，而非算法名。

### MR-Search — 25/30

- **Source family / coverage**：`MRSEARCH-CROSS-EPISODE-META-RL`；arXiv:2603.11327 v1
  （2026-03-11）、完整 HTML、method/algorithm、turn-level advantage、training/evaluation、ablation、
  context-management extension、limitations 与公开代码。已区分论文 v1 事件和后续 repository 状态。
- **Problem / old design / changed constraint**：并行 independent rollout 在每次尝试成本低、episode 短且
  majority vote 足够时合理；长程 search 中，多次采样可能重复同一失败策略，而且 inference 没有
  ground-truth reward 可用。约束变化后，前一次 search trace 和反思变成下一次探索的显式 context。
- **Mechanism / ownership / flow**：一个 meta-episode 包含多个完整 search episodes；每轮生成 answer 后
  追加 reflection，再让下一轮读取已有 trace。训练使用 episode/turn-level grouped RLOO advantage，并可
  把早期轮设为 exploration、后期轮设为 exploitation；tool output 不作为 policy token 更新。query、
  episode、reflection、retrieved evidence、reward/verifier 与 policy version 共同决定 state identity。
- **Evaluation boundary**：Qwen2.5-3B/7B Base，覆盖 NQ、TriviaQA、PopQA、HotpotQA、2Wiki、MuSiQue、
  Bamboogle 与 ASearcher，工具固定为 Wikipedia search。相对提升只证明该训练与 benchmark contract；
  没有 long-form verifier、open-web freshness、tool failure、reflection hallucination、生产 latency/cost 或
  multi-user memory 隔离实验。保留上一个 episode 可减 context，但不证明它是通用最优压缩策略。
- **Trade-off / evolution**：cross-episode adaptation 用更多串行 latency/context 换避免重复探索，并把错误
  reflection、evidence pollution 与 early-episode anchoring 引入 control flow。并行 sampling 在低延迟或
  多样性优先时继续成立；可靠实现需保存 attempt/evidence provenance、停止条件与退化回并行分支。
  关系为 `Direct Evolution`。
- **ROADMAP / decision**：主 owner 暂定 Ch74，Ch29/62/73/76 handoff；Books pending。重点检查现稿是否
  区分 parallel search、sequential adaptation 与 durable memory，且没有把 self-reflection 当作事实来源。

### Strategic Navigation / MADQA — 24/30

- **Source family / coverage**：`MADQA-DOCUMENT-NAVIGATION-EFFORT`；arXiv:2603.12180 v1
  （2026-03-12）；arXiv HTML 不可用，已读 58 页 primary preprint PDF 的 main text、dataset card、
  methodology、evaluation、human-agent analysis、limitations 与关键 appendices，并核验官方 baseline code
  和 gated dataset card。test labels 隐藏且数据为 CC BY-NC，属于 artifact contract。
- **Problem / old design / changed constraint**：final-answer accuracy 在 corpus 已经 oracle-retrieved、文档
  结构单一时够用；真实 PDF collection 中 retrieval、page navigation、visual parsing、cross-document
  synthesis 与 answer extraction 会串联，Agent 可用更多 tool calls 掩盖缺乏战略性的 first action。
- **Mechanism / ownership / flow**：MADQA 由 800 份、18,619 页异构 PDF 与 2,250 个 human-authored QA
  构成；问题覆盖 extractive、multi-hop、cross-page/cross-document、closed-world grounding 与 visual
  evidence。evaluation 同时记录 answer accuracy、page/doc attribution 和 effort；Kuiper range 衡量
  correctness 是否随 tool-call budget 出现非均匀退化。task、document snapshot、gold page、judge、
  retrieval backend、step budget 与 model/scaffold 共同定义结果。
- **Evaluation boundary**：500 test、200 development、约 1,550 training annotations；1,200+ 小时专业
  标注，GPT-5 + oracle evidence 只用于 flag 后再人工复核。frontier agents 在足够 step 下可接近 human
  raw accuracy，却解决不同题目并保留约 18% oracle gap；这不证明“人类推理更强”，而是揭示 retrieval、
  navigation、comprehension 和 refusal 的 failure mixture。公开文档可能进入 pretraining，9%～15% 题目可
  无文档猜中；corpus 仅英文且偏美国公开机构，不能外推企业私有文档或多语言场景。
- **Trade-off / evolution**：增加 step budget 可提高最终准确率，却可能形成无效 loop、成本尾部与错误
  recovery；static RAG 在 corpus 小、retrieval contract 稳定时仍更可控。evaluation 应从单一 accuracy
  演进为 `accuracy × grounding × effort × failure stage`，并保留 oracle retrieval 分支用于定位瓶颈。
  关系为 `Layering / Dependency`。
- **ROADMAP / decision**：主 owner 暂定 Ch62，Ch69/74/76 handoff；Books pending。若吸收，只写入
  measurement contract 与 error cascade，不保留模型排行榜。

### Attention Sinks Are Provably Necessary — 22/30

- **Source family / coverage**：`SOFTMAX-SINK-TRIGGER-CONDITIONAL`；arXiv:2603.11487 v1
  （2026-03-12）、完整 HTML、task construction、single/multi-layer theorems、ReLU counterexample、
  proofs、related work、limitations 与 appendix。该文是 theory result，不包含真实大模型训练或性能实验。
- **Problem / old design / changed constraint**：softmax 把 attention 权重约束在非负 simplex 上，适合
  convex aggregation；当一个 head 只应在 trigger 位置聚合、其他位置必须执行 no-op 时，权重仍必须
  分配到某个 token。固定 BOS/null token 因 value 可被压到近零，成为安全的概率质量去向。
- **Mechanism / proof boundary**：synthetic task 在 trigger 位置输出此前 non-BOS token 均值，其他位置
  输出零。作者证明：单层 softmax attention 在误差趋零时，所有非 trigger 位置几乎全部注意 BOS；多层
  模型至少在某层/位置形成 sink。去掉 simplex constraint 的 ReLU attention 可直接让所有权重为零并完成
  no-op，因此 theorem 指向 normalization constraint，而非某种训练 recipe。
- **What it proves / does not prove**：它证明特定 trigger-conditional computation 中 sink 的结构必要性，
  不是“所有真实 Transformer sink 都只有 no-op 作用”，也不证明删除 softmax 会在语言模型上更好。
  实际模型可能同时存在 broadcast、aggregation、register 等机制；论文自己把向 key-query retrieval 的
  扩展写为 likely，而非已证明事实。
- **Trade-off / evolution**：softmax 的稳定归一化与概率解释换来 no-op 困难；null/register、gating 或
  非归一化 attention 提供不同 escape hatch，同时引入额外状态、缩放/训练稳定性和 intervention mismatch。
  关系为 `Principle Reuse`，旧 softmax 在需要规范化竞争与成熟 kernel 时仍成立。
- **ROADMAP / decision**：主 owner 暂定 Ch14，Ch15/45 handoff；Books pending。可能用于 refine
  attention 的 normalization trade-off，但必须避免把 synthetic theorem 外推成 pretrained-model 因果解释。

### One Model, Many Budgets / ELIT — 24/30

- **Source family / coverage**：`ELIT-VARIABLE-LATENT-COMPUTE`；arXiv:2603.12245 v1
  （2026-03-12）、完整 HTML、method、ImageNet/Kinetics/Qwen-Image experiments、compute analysis、
  ablations、discussion 与 failed experiments。项目页存在；大规模 from-scratch benefit 明确未验证。
- **Problem / old design / changed constraint**：标准 DiT 将 token 数绑定 spatial resolution，并在所有位置
  均匀分配 blocks；固定 grid 在预算单一、实现简洁时合理，却不能让同一权重服务多个 latency-quality 点，
  也无法把空白/简单区域的 compute 转移到困难区域。直接 spatial token drop 又会造成不可恢复的信息洞。
- **Mechanism / ownership / flow**：短 spatial head 后，Read cross-attention 把 patch state 压入分组 latent
  interface，大多数 transformer blocks 在 latent 域运行，Write 再广播回 spatial tail。每个 training
  iteration 对所有 groups 采同一 latent prefix budget，tail-drop 让靠前 latent 更频繁训练并形成 importance
  order；inference 用 latent count 控 FLOPs。model weights、budget、group layout、sampler/guidance 与
  resolution 一起构成 serving identity。
- **Evaluation boundary**：DiT/U-ViT/HDiT 在 ImageNet-1K 256/512，video branch 在 Kinetics；Qwen-Image
  20B branch 是 distillation fine-tune（512px 与 1024px 各 60K steps），不是 from-scratch 对照。4096→
  2048/更低 latent budget 降低作者计算量同时质量下降；大模型训练硬件、wall-clock、memory 与 online
  batching SLO 未完整披露。作者还报告 synthetic-data style bias，CCFG 更易 saturation，且 spatial token
  masking 在 inference 失败。
- **Trade-off / evolution**：latent bottleneck 用可调 compute 换 information compression、group boundary、
  budget-conditioned quality variance 与新的 batching fragmentation。固定 DiT 在单一质量点、细节无损和
  kernel 简洁优先时仍成立；token merging/drop 与 latent interface 是不同设计分支。关系为
  `Direct Evolution`。
- **ROADMAP / decision**：主 owner 暂定 Ch17，Ch15/23/38/39/45 handoff；Books pending。适合沉淀
  representation length 作为 runtime budget knob，以及训练分布必须覆盖 serving budget 的 contract。

### Neural Thickets — 18/30（Low-score Verification Complete）

- **Source / date / coverage**：arXiv:2603.12228 v1（2026-03-12），已核验完整 HTML 中 landscape probe、
  RandOpt algorithm、LLM/VLM experiments、distillation、scaling、implementation 与 limitations。它满足
  事实核验，但低分不升级为 Books candidate。
- **Mechanism / evidence**：RandOpt 围绕 pretrained weights 采样 `N` 个随机 perturbations，以小型
  post-training set 选择 top-`K`，inference majority vote/ensemble。作者的主要贡献是把它当作 loss-
  landscape probe：强且大的 pretrained model 邻域更可能包含 task-improving specialists；不是宣称
  random search 普遍优于 gradient methods。
- **Boundary / trade-off**：主要实验为离散/整数答案，training FLOPs 对齐但 `K=50` inference 比单模型贵
  50 倍；200×GH200 的 3.2 分钟案例依赖极宽并行资源。无 pretraining、小模型和 structured generation
  均是明确弱点；baseline 的 test-time ensemble 也缩小方法差异，distillation 又恢复串行训练与额外 FLOPs。
- **Decision / rejection reason**：保持 18/30，`Weekly Only — landscape observation`。它没有改变 Ch24
  关于 pretraining/post-training 的核心设计结论，且当前系统价值主要是可并行搜索与 inference ensemble
  的资源重新分配；不足以在 Books 建立长期机制。若后续出现可复现的 structured-output distillation、
  不依赖巨量 ensemble 的机制，再重开。

### EvoScientist：把跨任务成功与失败提炼为派生策略，但不把策略升级为事实 — 25/30

- **Candidate / Week / Source Family:** EvoScientist / 2026-W11 / 25/30；
  `Source Family ID: evoscientist-derived-strategy-memory`。
- **Source Type / Date / Revision / Access:** arXiv:2603.08127 sole v1 于 2026-03-09 首发；已阅读 21 页
  PDF。论文指向代码；当前 `EvoScientist/EvoScientist` 官方仓库与项目站可访问，但其 7 月版本已经扩展为
  productized research workspace，不能反推 3 月论文实验实际运行的 commit。故 paper mechanism 与 later
  artifact surface 联读，但不声称当前代码逐行复现论文。
- **Full-read Coverage:** 已覆盖 metadata、Introduction、Related Work、问题定义、Researcher/Engineer/
  Evolution Manager 三 Agent 架构、16 个公式/状态更新、idea/experiment tree、IDE/IVE/ESE、Datasets、
  baselines、metrics、implementation、全部实验与消融、Conclusion、Limitations/Ethics、Appendix A～E、
  evaluation/evolution prompts 与六篇 case studies。
- **Original Problem / Why Previous Design Was Reasonable:** 静态 AI-scientist pipeline 在一次 run 内用 tree
  search、debate、code retry 与 evaluator 探索候选，角色清楚、状态边界简单，也避免把一次错误经验带到未来。
  但跨任务完全清空会重复不可行 idea、debugging pattern 与 data/training mistake；当实验成本与历史积累上升，
  “每次从零开始”的安全性转化为重复探索成本。
- **Changed Constraint / Principle:** 系统开始跨 research goals 复用经验后，历史不再只是日志，而会改变后续
  proposal 与 code-generation policy。长期原则是：**raw trajectory、execution evidence、derived strategy、
  retrieval decision 与 authoritative workflow state 必须分层；由 LLM 总结出的成功/失败模式是 advisory
  policy evidence，不是科学事实或自动审批。**
- **Mechanism:** Researcher Agent 从 ideation memory 取 top-2 相似方向，结合 literature 执行 propose–review–
  refine idea tree，再用 Elo pairwise tournament 选 top-1 proposal、保留 top-3 供 direction summary。Engineer
  Agent 从 experimentation memory 取 top-1 strategy，按 initial implementation、hyperparameter tuning、proposed
  method、ablation 四阶段生成/执行/修复代码。Evolution Manager 再执行三种写入：`IDE` 从 top-ranked ideas
  提炼 promising directions；`IVE` 根据不可执行或低于 baseline 的 report 写失败方向；`ESE` 从 best code 与
  全轨迹提炼 data-processing 与 model-training strategy。
- **State Ownership / Control and Data Flow:** literature/API 拥有 retrieved evidence；RA 拥有 idea drafts、review
  与 Elo-derived ranking；EA/sandbox 拥有 code、logs、run status 与 metrics；EMA 拥有 model-generated derived
  strategy；memory store 拥有 items/index 与 retrieval result；conference/human reviewer 只拥有外部 review
  evidence。流程为 `goal -> literature + retrieved strategy -> idea tree -> tournament -> proposal -> staged code
  search/execution -> report -> IDE/IVE/ESE -> versioned memories -> next goal`。论文没有定义 memory conflict、
  correction、expiry、delete、concurrent update 或 rollback semantics。
- **Implementation Contract:** literature 使用 Semantic Scholar API；idea/manuscript 用 Gemini-2.5-Pro，code 用
  Claude-4.5-Haiku，memory embedding 用本地 `mxbai-embed-large`。idea tree 最多 21 个 candidates、3 workers；
  experiment retrieval top-1、4 workers，四阶段最大 attempts 分别为 20/12/12/18。论文未披露 GPU/CPU、API
  snapshot、sampling parameters、token/call/cost、wall-clock distribution、sandbox image、seed 或 production SLO。
- **Evaluation Contract:** 30 个 experienced-AI-researcher queries 被统一模板化；code evaluation 使用相应生成
  proposal，指标是 sandbox 中“执行并产生 valid output”的成功率；6 个选择出的 ideas 被扩成论文并投稿 ICAIS
  2025。Idea quality 同时用 Gemini-3-flash 和 3 名 PhD annotators 做 swapped-position pairwise novelty/
  feasibility/relevance/clarity；baseline 为 4 个开源和 3 个商业系统。六篇投稿复用 AI Scientist-v2 writing
  module，因此 acceptance 不能仅归因于 memory/evolution。
- **Ablation / Sensitivity / Evidence:** IDE、IVE 与全部 idea evolution 的消融支持这些 components 在同一 30-query
  judge contract 下影响 novelty/feasibility；ESE 前后平均 execution success 从作者报告的 34.39 提升到 44.56，
  但 proposed-method stage 只从 20.33 到 21.57。六篇全接收、两项 award 是小样本选择后的 conference outcome，
  不是对普遍科学正确性、novelty 或 autonomy 的统计保证。没有 memory contamination、negative transfer、
  stale strategy、deletion、cross-domain 或 matched-budget ablation。
- **What the Evidence Proves:** 在作者固定模型、30 queries、检索/搜索预算、judge 与 sandbox 合同下，将 top
  ideas、failed proposal analysis 与 code trajectories 提炼为可检索策略，能改变后续 idea comparison 与 code
  execution outcome。论文也明确暴露 proposed-method execution 仍低、理论 formalization 仍需人类，以及物理
  实验 domain 未验证。这支持“跨任务经验必须成为显式 derived state”，不支持“Agent 自动获得科学 authority”。
- **What It Does Not Prove:** 不能证明多 Agent 本身优于同预算单 Agent；不能由 6/6 acceptance 推出科学发现
  正确或可复现；不能把 LLM judge、Elo、execution success、baseline-relative metric 或 conference acceptance
  合并成 ground truth。当前 repo 的 product features 也不能补足论文未披露的 experiment commit、cost、
  concurrency、memory governance 与 failure recovery。
- **Trade-offs / New Failure Modes:** 复用降低重复探索，却会把 judge bias、错误 baseline、sandbox quirk 与
  stale library/API pattern固化为 future prompts；top-k embedding 可能漏掉 rare-but-critical failure；top-ideas
  summary 引入 survivorship bias，failed-direction summary 可能把暂时 execution failure误写成方法不可行；Elo
  ranking 依赖 pair graph/order；derived memory 会不断占用 Context，并需要 provenance、scope、expiry、
  supersession、human review 与 selective delete。
- **Where Previous Designs Still Apply:** 一次性、敏感或高漂移研究可继续使用 stateless run；原始 trace archive
  适合 forensic/reproducibility；人工维护的 validated playbook 适合高风险实验；参数训练适合跨大量任务形成稳定
  policy；Workflow event log 仍是 run truth。Derived memory 只是在这些分支之间增加可审查的 advisory layer。
- **Evolution Relationship:** `Direct Evolution`：static pipeline -> within-run search/retry -> cross-run episodic
  archive -> success/failure-derived procedural memory -> provenance-aware consolidation/review。`Layering /
  Dependency`：execution evidence -> derived strategy -> retrieval -> proposal/action -> independent verification/
  approval；后一层不能把 summary 反向升级成原始证据。
- **ROADMAP / Chapters Read / Existing Coverage:** 主 owner 检查为 Ch73，handoff Ch77/62/76；已阅读 Ch72～77
  以及 Ch62 相关 evidence sections。Ch73 已明确 `episodes -> derived strategy`、成功/失败都可用于抽取、source
  episodes/judge/extractor/provenance/supersession、以及 derived strategy 不能自动成为 Workflow policy；Ch77 已
  规定 proposal、sandbox evaluator、artifact lineage、approval 与 deployment authority；Ch62 已覆盖 executable
  artifact、judge identity、small-sample uncertainty 与 claim provenance。论文没有补出新的长期机制缺口。
- **Integration Decision:** `No Change — Already Covered / Experimental Evaluation Case`。保留在 Weekly 作为
  ideation/experimentation 双 memory 的受限案例，不修改 Books；这不是否定该研究，而是章节级去重。若后续
  公开 experiment commit、memory governance、negative-transfer/forgetting 与 matched-cost single-agent ablation，
  可重新评估是否补充机制。
- **Open Questions:** derived strategy 如何绑定 source run、dataset、baseline、environment、model/judge 与有效期？
  如何从 temporary execution failure 区分 scientifically invalid direction？memory conflict、concurrent update、
  deletion 与 rollback 谁拥有？怎样以 matched tokens/calls/wall-clock 比较 memory、多 Agent 与更强单 Agent？

### MEMO：Memory 不是更多历史，而是 retention、exploration 与 evaluation contract 的共同状态 — 25/30

- **Candidate / Week / Score / Source Family**：MEMO / 2026-W11 / 25/30；
  `MEMO-CONTEXT-OPTIMIZATION-MEMORY-REPLAY`。Technical Novelty、System Impact、Practical Value、
  Source Reliability、Project Relevance、Longevity 分别为 4/4/4/4/5/4：它把 persistent derived memory、
  uncertainty-aware context selection 与 state-prefix replay 合成可运行 loop，但证据仍局限于作者的 text-game
  testbed，且 memory governance 与总资源合同不完整。
- **Source Type / Event Date / Revision History**：arXiv paper + author repository。v1 于 2026-03-09 23:36 UTC
  首发，归 W11；v2 于 2026-03-18 提交，只是 W12 revision node，不制造第二事件。arXiv 显示两版均为
  2,130 KB；本轮全文阅读 current v2，核对 v1 metadata/abstract 与 revision history。v1 PDF 端点在当前抓取器
  中 cache miss，故不声称完成逐页版本差分。
- **Direct / Related Primary Sources / Access**：直接来源为 arXiv v1/v2 metadata、38 页 v2 PDF 和
  `openverse-ai/MEMO` 官方 repository。仓库当前只有 5 commits、固定 TextArena submodule，并公开 orchestrator、
  tournament、TrueSkill agent pool、trajectory memory、XML CRUD 与 replay surfaces；无 release/tag 能把 current
  HEAD 精确绑定到 03-09 experiment snapshot，因此代码只证明公开实现 surface，不填补论文未披露字段。
- **Full-read Coverage**：已读 Abstract、Introduction、Problem、全部 Method/公式/算法、Related Work、五类 games、
  baselines、implementation/evaluation protocol、main results、component/cross-task/cross-model ablations、Conclusion，
  以及 Appendix A～N 的 prompt sensitivity、完整伪代码、hyperparameter sensitivity、proposal/reflection/memory
  prompts、base prompts、TextGrad/MIPRO/GEPA/RL 细节、token costs、完整结果、环境与 insight/prompt cases；论文
  没有独立 Limitations 或 Threats to Validity 章节，该缺口本身保留为 evidence boundary。
- **Original Problem / Why Previous Design Was Reasonable**：静态 prompt 或每轮只根据最新 trajectory 更新 prompt，
  状态少、可复现边界清楚，也不会把早期错误经验长期写回。在短单轮任务中这仍合理；但多轮双 Agent 对弈会把
  早期采样偏差沿 joint trajectory 放大，不同近义 prompt 甚至会翻转 model ranking，而 memoryless optimizer 又会
  在每代丢失 rare state 与过去失败，导致 performance 与 ranking 都依赖单次 tournament path。
- **Changed Constraint / Principle**：当 evaluation object 从单次答案变为长期 interaction policy，`prompt + injected
  memory` 已是模型外的可变 policy state。系统既要保留高价值经验，又必须持续产生 fresh trajectories；只做
  retention 会锁定 stale/narrow heuristics，只做 exploration 则反复付费而无法积累。长期原则是：**Memory policy、
  exploration policy、replay distribution 与 evaluator/opponent contract 共同决定可观察能力，不能分别报一个
  win rate 后宣称是模型能力。**
- **Mechanism**：每代维护 `N=8` 个 context candidates，以 self-play 对 baseline agent 产生 outcomes；TrueSkill
  给每个 candidate 维护 `(mu, sigma)`，按 conservative score `mu - kappa*sigma` 选择并写入 persistent candidate
  pool。新候选由随机 style-bounded edit 与 memory-augmented edit 混合生成。完成 trajectory 先由模型反思成 typed
  strategy insight，再对共享 memory bank 执行 Add/Edit/Remove；其中一部分 candidate 注入抽样 memory。独立的
  replay buffer 保存每 turn 的 trajectory prefix 与 environment seed，以 `1/count(prefix)` 的 inverse-frequency
  priority 和指数 `alpha` 抽样，并以 gate `beta` 在 replay start 与 fresh game 间切换。
- **State Ownership / Control Flow / Data Flow**：game environment 拥有 legal state、seed、transition 与 terminal
  outcome；tournament scheduler/agent pool 拥有 match schedule、role swap、candidate identity 与 TrueSkill state；
  candidate pool 拥有 prompt lineage 和 elite selection；memory service 拥有 LLM-derived insights 与 CRUD operation；
  replay service 拥有 prefix、frequency、priority 和 restoration seed；evaluator 拥有 opponent pool、held-out games、
  temperature、win-rate/RSE contract。数据流为 `fresh/replayed state -> self-play trajectory/outcome -> rating + reflection
  -> candidate/memory/replay updates -> next context -> held-out opponents`。论文没有定义 source-episode pointer、
  writer/judge version、conflict lineage、expiry、concurrent update、selective delete、rollback 或 access control。
- **Implementation Details**：主配置为 5 generations、每代 8 candidates、每 candidate 50 self-play games，共
  2,000 games/task；`kappa=1`，memory initialization fraction `pi=0.75`；replay capacity 100,000、`alpha=0.6`、
  `beta=0.4`。prompt methods 使用 GPT-4o-mini 与 Qwen2.5-7B-Instruct，temperature 1.0；每个最终 context 对
  Grok-4-Fast-Non-Reasoning、Gemini-2.5-Flash-Lite、Qwen3-235B-A22B-Instruct-2507 各跑 50 games，3 independent
  optimization runs。RL baseline 用 Qwen2.5-7B-Instruct、LoRA rank 16/alpha 32/dropout 0、REINFORCE；SPIRAL
  描述为 128 games/rollout、400 steps。未披露 API/model snapshot、hardware、parallelism、wall-clock、input tokens、
  dollar cost、seeds across runs 或 production SLO。
- **Evaluation Contract / Baselines**：五个 TextArena/SPIN-Bench text games 覆盖 negotiation、imperfect information
  与 perfect information；baselines 为 default/CoT/ToT、TextGrad、MIPRO、GEPA、UnstableBaseline 与 SPIRAL。
  prompt methods 是 3 个独立 optimization runs，RL 则训练单一 policy、挑 best checkpoint 后做三组 evaluation，
  因而 19x games headline 不是完全 matched algorithm-selection、tokens、calls、wall-clock 或 compute comparison。
  RSE 是 run-level standard error 除以 mean；n=3 时只能描述这套 runs，不能当稳定性的高精度估计。
- **Ablations / Sensitivity / Overhead**：component ladder 报告 baseline 23.8%、tournament-only 27.1%、memory-only
  34.2%、tournament+replay 41.6%、tournament+memory 48.1%、全部模块 50.2%，支持 retention 与 structured
  exploration 在作者设置中互补。`pi` 在 0.25～0.75 优于两端；all-memory (`pi=1`) 下降，说明 stale/narrow
  memory 会挤压 exploration。过小/过大的 replay buffer 并非单调，但作者选 100K；`alpha=1` 与 `beta=0.8/1`
  均下降，说明 rare-state oversampling 和重放过重会扭曲 state distribution。输出 token 表只覆盖三个 games 和
  optimizer-side output，不含 environment/opponent/evaluation 输入输出与 RL training compute。
- **What the Evidence Proves**：在固定的五-game、模型、opponent pool、temperature、2,000-game self-play budget
  与作者实现中，持久 insight memory、tournament selection 和 moderate replay 共同改变 held-out win rate 与三-run
  dispersion；prompt wording 可以改变绝对结果与 pairwise ranking；memory/fresh exploration 的混合优于两个极端，
  且 cross-game/cross-model transfer 存在明确负迁移 cell。这支持把 context optimization 视为 stateful system design，
  也支持 memory activation 必须保留 exploration control。
- **What It Does Not Prove**：不证明 MEMO 普遍优于 RL、其他 prompt optimizer 或更强 static policy；不证明
  LLM reflection 得到的 insight 正确、因果、可泛化或可安全删除；不证明低 RSE 在新 opponent/model/provider
  version 下保持。cross-task table 每 cell 只有 50 matches，cross-model transfer 对强模型出现 -8/-6 等负值；
  prompt-variation analysis 只在 Kuhn Poker 和五个风格 prompt 上，不能外推所有 Agent benchmark。
- **Limitations / Threats to Validity**：没有独立 Limitations 章节；主要威胁包括 author-built harness 与 memory
  prompts、同源 self-play/outcome 驱动优化、三-run uncertainty、best-checkpoint RL selection asymmetry、provider
  drift、five-game external validity、未报告 total compute/cost、memory bank size/lookup/context-token growth 与 CRUD
  error rate。Remove 在论文正文被描述为遇到冲突时删除新旧 insight，而 Appendix prompt 更偏向删除重复/低质量项；
  二者语义不完全一致，且无原始 episode/provenance 时会把“冲突”变成不可逆信息损失。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：Memory 减少重复探索，却增加 context tokens、
  stale strategy、survivorship/judge bias、conflict deletion 与 prompt injection persistence；TrueSkill 抑制小样本幸运，
  但 selection 仍依赖 opponent/match graph；rare-prefix replay恢复 coverage，却会 oversample噪声或不可迁移状态，
  seed replay 也不保证外部 provider output 可重放。短 horizon、稳定规则或高风险场景仍可用固定 prompt + repeated
  evaluation；需要跨大量 workload 学稳定 policy 时，weight update/RL 仍是合理分支；原始 trajectory archive、
  held-out suite 与人工 playbook 不被 derived memory 替代。
- **Evolution Relationship**：`Direct Evolution`：fixed prompt -> current-batch prompt optimization -> persistent
  trajectory-derived memory -> memory + uncertainty-aware population selection -> memory + bounded state replay。
  `Layering / Dependency`：environment truth -> trajectory/archive -> derived insight -> retrieved context -> candidate policy
  -> independent evaluation；后一层不能倒写为前一层事实。它与 EvoScientist 是 `Principle Reuse`，不是相同实现：
  前者在 game self-play 中优化 context，后者在 research workflow 中跨任务沉淀 ideation/experiment strategy。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：主 owner 为 Ch73，handoff Ch62/77/78；已读
  Ch73 的 context-memory boundary、raw-trajectory-to-derived-strategy、write/read/consolidation/governance 和 evaluation，
  Ch62 的 interactive feedback/opponent/accumulated-context contract，Ch77 的 evaluator-driven search/lineage/approval，
  Ch78 的 topology/shared-state/coordination-cost sections。现有 Ch73 已覆盖 derived strategy 的 provenance、scope、
  expiry、supersession 与 advisory boundary，Ch62 已覆盖 prompt/opponent/turn budget 与 repeated-run dependence；
  MEMO 新增的是 retention–fresh-exploration–replay 三者的具体耦合和负迁移证据，而不是推翻已有结论。
- **Integration Decision / Changed Files**：`Refine — Existing Argument (Experimental; Provisional)`，主 owner Ch73，
  Ch62/77/78 只做短 handoff 候选。Historical Books Gate 仍关闭，本轮不修改 Books；待 W11 与全历史 Evidence Gate
  通过后，只考虑把“memory activation fraction 与 replay gate 是可评估 policy state”融入既有演进段落，不复制
  paper 名称、版本功能或 headline benchmark。
- **Open Questions**：memory item 怎样绑定 source prefix/outcome/opponent/model/prompt version 并支持 conflict quarantine
  而非双删？怎样用 held-out games、new opponents 与 delayed provider revisions区分 true strategy 与 harness overfit？
  如何按 calls、input/output tokens、environment steps、wall-clock 和 dollar cost matched 比较 prompt memory、RL 与更强
  static policy？seed-prefix replay 在 nondeterministic API model 下的 replay identity 应由谁负责？

### FinToolBench：Tool trace 的“能执行”与“可接受”是不同评估对象 — 27/30

- **Candidate / Week / Score / Source Family**：FinToolBench / 2026-W11 / 27/30；
  `FINTOOLBENCH-TRACE-CAPABILITY-COMPLIANCE`。六维评分 4/4/5/4/5/5：它把真实 tool execution、trace-level
  diagnosis 与 finance-specific constraint 放在同一 EvalSpec 中，工程价值高；但仍是作者 benchmark、免费 API
  snapshot 与 LLM-labeled/judged contract，不是监管合规证明。
- **Source / Date / Revision / Full-read Coverage**：arXiv:2603.08262 v1 于 2026-03-09 首发，v2 于
  2026-08-01 revision；本周 owner 锁定 v1。已读完整 v1 HTML/PDF：Introduction/Related Work、八阶段 tool/question
  curation、tool manifest 与 finance attributes、全部 capability/compliance metrics、FATR retrieval/planning/execution、
  seven-model experiments、attribute injection、tool distribution/category diagnosis、Conclusion/Limitations/Ethics，
  以及 Appendix A～I 的过滤/标注、公式、prompts、reproduction checklist、algorithm 与 cases。已核对 official
  `Double-wk/FinToolBench` repository 的公开 manifest/questions/evaluation scripts 与明确的 internal-components boundary。
- **Original Problem / Previous Design**：final-answer QA 与 syntactic function-call accuracy 在静态文档、mock API
  或无时效/权限差异时成本低、可重复；execution success 也能定位 schema/argument/runtime 基本错误。但金融调用中，
  stale data、informational-to-transactional escalation 或跨 regulatory domain 的工具即便成功执行，仍可能让结果不可
  接受。只看最终答案又会丢失“是否调用、调用何物、是否成功、证据是否新鲜”的 failure stage。
- **Mechanism / State Ownership / Flow**：benchmark 将 RapidAPI/AkShare 工具做 executability filter、dedup 与统一
  signature，给每个 tool version 标注 `update_frequency / intent_type / regulatory_domain`；question 经 tool-required
  filter、BGE-M3 top-20 retrieval、三次 Qwen3-8B selection 与 human verification形成 dataset。Run 保存 ordered
  `{tool_name, parameters, output, error}` trace。FATR把 attributes注入 tool card，planner 最多 5 rounds，executor施加
  60s timeout、2 retries、deterministic cache与长输出压缩。Tool provider拥有实际数据/错误；manifest owner拥有版本化
  capability/attributes；planner只提出 call；executor拥有执行；judge/scorer拥有 measurement，不拥有 authorization；
  release/compliance authority不能由 mismatch classifier替代。
- **Evaluation Contract**：295 questions（166 single-tool、129 multi-tool）、760 free-tier tools；TIR 测是否调用，
  TESR 测是否有成功 execution，CER/CSS条件于已尝试/成功 subsets，SoftScore按 answer type用 GPT-5.1 三次评分；
  TMR/IMR/DMR 对至少一次 mismatch 做 question-level aggregation，并只在有 tool call 的 traces解释。论文比较 7 个
  model backends，三名 finance experts只复核分层抽样的 60 questions/50 traces。具体 model score是 2026 snapshot，
  受 API availability、cache、judge、prompt、tool catalog 与 provider/model revision共同制约。
- **Evidence / Limitations / Trade-offs**：attribute injection在作者设置中改变 tool-selection、redundant calls 与
  mismatch rate；case study也显示 execution continuity改善却仍可能答错。保守 model可少调用而获得较低 mismatch，
  因此 capability与compliance必须联合阅读。论文明确不覆盖 paid terminals、brokerage/order routing、全部市场/司法辖区；
  benchmark checks不是 professional compliance。Tool label与requirement inference依赖 LLM majority/judge；CSS ratio在低
  TESR时不稳定；real APIs带 drift/rate/auth依赖；repository只开放 evaluation pipeline与minimal data，未开放全部 agent/
  build internals。Caching提高复现性却可能掩盖 live freshness；output compression节省 Context却可能删除审计证据。
- **Evolution / ROADMAP / Existing Coverage / Decision**：`Direct Evolution`：static QA -> call syntax -> executable
  trace -> capability/correctness split -> timeliness/intent/domain policy slices -> dated deployment evaluation。已读 Ch62、
  Ch68、Ch74及相邻 Ch75/77。Ch62 已将 subject/environment/scorer/run/decision分开，要求 Agent trajectory、side effect、
  scorer uncertainty与 policy gate；Ch68已规定 model verdict是 policy-bound sensor而非 authority；Ch74已拆分 selection、
  argument、authorization、execution、observation与 final outcome，并要求 tool/version/provenance。论文提供有价值的
  finance case，但没有新增比现稿更一般的长期机制，故 `No Change — Already Covered / Experimental Evaluation Case`。
  Historical Books Gate关闭，本轮不改 Books。
- **Open Questions**：如何用 versioned market calendar/source timestamp验证 freshness，而不是靠 tool label与 judge？
  transactional intent怎样绑定真实 approval/authorization而非 benchmark prompt？provider drift时 cache 与 live run应怎样
  分层报告？如何校准低-attempt model 的 mismatch rate并加入 economic harm、licensing与jurisdiction policy？

### Reasoning as Compression：从统一 token 税到 prior-dependent semantic cost — 26/30

- **Candidate / Week / Score / Source Family**：Reasoning as Compression / 2026-W11 / 26/30；
  `CIB-SEMANTIC-REASONING-COST`。六维评分为 5/4/4/4/5/4：Conditional Information Bottleneck
  为 budget forcing 提供了可推导的统一目标，也明确揭示 cost model 是训练 specification；但证据仅覆盖数学
  reasoning、作者模型与单一硬件设置，且没有 production latency/energy 验证。
- **Source Type / Date / Revision / Coverage**：arXiv:2603.08462 v1 于 2026-03-09 首发，v2 于
  2026-05-18 revision；本周事件以 v1 为 owner，v2 只用于识别后续变化。已读 v1 HTML 的 metadata、
  Introduction、Related Work、完整 CIB 推导、reward construction、length-prior 等价关系、全部实验/
  ablation、Conclusions，以及 Appendix A～E 的 variational bounds、定性样例、additional results、training/eval
  hyperparameters 与 literature results。论文页未给出作者 code/artifact，复现状态保持 `Not Disclosed`。
- **Original Problem / Why Previous Design Was Reasonable**：hard token cap 与线性 length penalty 直接、便宜，
  与真实 decode token count 同量纲；在每个 token 成本近似相同、任务难度窄或 serving 必须执行 hard ceiling 时仍
  合理。但它们把必要推理与重复 filler 征收同一“flat tax”，容易在 easy prompts 保留冗余、在 hard prompts 删除
  关键步骤。标准 Information Bottleneck 又假设 `Y-X-Z` Markov chain，而 Transformer 生成答案时仍可直接
  attention 到 prompt，故把 `Z` 当唯一信息通道会重复保存 `X` 已提供的信息。
- **Changed Constraint / Principle / Mechanism**：作者把 prompt `X` 视为 decoder 始终可见的 side information，
  用 `I(Z;Y|X)` 表示 reasoning trace 对答案的额外 sufficiency，并以 `I(X;Z)` 控制 minimality。不可解边际
  `P(Z)` 由不观察 prompt 的 frozen base-model prior `Q_phi(Z)` 上界；最终 reward 是 binary correctness 加
  `beta * sum_t log Q_phi(z_t|z_<t)`。因此每个 token 的 cost 是 prior surprisal，不再只是数量。Uniform prior
  恢复线性 length penalty；对目标长度的绝对偏差对应以目标长度为中心的 Laplace-like prior，说明旧 heuristic
  不是“错误”，而是对 trace distribution 作了更强假设。
- **State Ownership / Control and Data Flow**：task/verifier 拥有 prompt、ground-truth answer 与 correctness；
  rollout policy 生成 trace/answer 并拥有 sampled token log-prob；frozen prior 只对 trace prefix 给出
  unconditional log-prob，不拥有事实或语义标签；reward service 合成 accuracy/minimality 与 versioned beta；
  GRPO trainer 按 prompt group 构造 update。数据流为 `prompt -> grouped traces -> verifier correctness + frozen-prior
  surprisal -> composite reward -> group-relative advantage -> policy update`。Prior checkpoint、tokenizer、template、
  beta 和 verifier 都必须进入 experiment identity；换 prior 就是在换 cost model。
- **Implementation / Evaluation Contract**：DLER-1.5B/7B 与 DeepScaler-1.5B 在 MATH500、AIME24、AIME25、
  Minerva、Olympiad 上训练/评测；prior 为 Qwen2.5-Base 1.5B/7B。训练用 `trl 0.26.2` GRPO，global batch 128、
  每 prompt 16 generations、temperature 0.8、max completion 4096/8196、150 steps、KL coefficient `5e-4`，
  CIB beta 为 `5e-5/1.5e-4`；单节点 8×H100 80GB。评测用 `lighteval 0.8.1`、vLLM 0.10.2、temperature 0.6、
  top-p 0.95、32K completion cap、每题 16 generations。作者结果支持这些 checkpoints/benchmarks 下的
  accuracy-token Pareto 改善；不能外推成真实请求 latency、energy、throughput 或 SLO 改善。
- **Ablations / Sensitivity / Overhead**：作者比较两档 beta、1.5B/7B prior、公开 L3L1 checkpoints 与同起点/
  同 training budget 的 L1-Exact baseline，并展示 information-density 与 inference-time sampling 曲线。较大 prior
  在未重新调参时出现最高约 1.4 个百分点平均准确率下降；作者明确归因假说受 resource-limited tuning 约束。
  Prior 只用于训练、不增加部署 decode state，但仍增加训练 log-prob forward、模型驻留/调度与版本耦合；论文把
  该 overhead 称为 negligible，缺少独立 wall-clock/FLOPs/memory breakdown，不能泛化。
- **What the Evidence Proves / Does Not Prove**：论文证明该 variational construction 能把若干 length heuristic
  写成不同 prior 的特例，并在作者数学任务中改变准确率—平均 token frontier。它不证明 prior surprisal 等于
  semantic necessity、压缩后的自然语言 CoT 更 faithful，或低-probability token 是冗余；binary final-answer
  verifier 仍无法定位因果步骤。Rare notation、domain term 或必要但 prior-unfamiliar 的推理可能被错误加税。
- **Limitations / Trade-offs / Previous Design Still Applies**：实验只有 unique-answer math、少量 model families、
  单一训练硬件和作者 reward/extraction contract；没有 seed/置信区间、开放领域、tool use、long-horizon Agent、
  multilingual、production latency 或 adversarial verifier。Semantic cost 用更强 inductive bias 换更细粒度预算，
  同时引入 prior bias、额外训练 state、checkpoint drift 与 beta calibration。Hard cap 在严格 SLO/内存边界仍必需；
  uniform length cost 在 proxy 足够、训练成本优先时仍合理；difficulty-aware routing、early exit、trace pruning 和
  concise drafting 是并存分支，不被 CIB 单向替代。
- **Evolution / ROADMAP / Existing Coverage / Decision**：`Direct Evolution`：hard cap -> uniform length penalty ->
  difficulty/target-aware penalty -> prior-dependent semantic cost -> workload-observed quality/cost control；与 verifier、
  GRPO 和 serving evaluation 是 `Layering / Dependency`。已读 Ch28～30，并核对 Ch20/62 handoff。Ch29 已覆盖
  composite reward scale、response-length correlation、verifier noise 与 grouped rollout cost，但尚未明确“cost proxy
  本身是可版本化 prior，uniform length 是其中一条假设分支”。暂定 `Refine — Existing Argument (Experimental;
  Provisional; Historical Books Gate Closed)`，主 owner Ch29；Books Gate 通过前不改正文，不保留作者 headline。
- **Open Questions**：如何用 step-level/executable evidence 区分 rare-but-necessary token 与无效 surprisal？prior
  与 policy 同规模、同域或同 tokenizer 的选择怎样影响 bias/compute？token reduction 在 continuous batching 下能否
  稳定转化为 tail latency 与 capacity？prior version 变化时 reward comparability 与 rollback 如何维护？

### Deep Tabular Research：规划的历史应成为 path state，而不是无边界的反思文本 — 25/30

- **Candidate / Week / Score / Source Family**：Deep Tabular Research / 2026-W11 / 25/30；
  `DTR-MACRO-PATH-EXECUTION-MEMORY`。六维评分为 4/4/4/3/5/5：hierarchical table state、macro-operation search、
  path-level expectation 与双通道 experience 构成清晰的 Agent system mechanism；但论文没有公开 code/artifact、
  hardware、完整成本或独立 Limitations，Source Reliability 保持 3。
- **Source Type / Date / Revision / Full-read Coverage**：arXiv:2603.09151 v1 于 2026-03-10 首发，v2 于
  2026-03-12 revision；已读 23 页 current PDF 全文，包括 task definition、related-work boundary、hierarchical
  meta graph、operation map、expectation-aware selection、siamese memory、closed-loop algorithm、main experiments、
  component/prompt/call-budget ablations、planning dynamics、Conclusion/Broader Impact，以及 Appendix A～F 的
  pseudocode、DTR-Bench curation、baselines/metrics、related work 与四个 execution case。arXiv 未列作者代码。
- **Original Problem / Previous Design**：把 table serialize 成 text 后单次回答，在 flat schema、fact lookup 或
  短 arithmetic chain 中状态简单且成本低；Tree/Code loop 在可承担 branch/retry budget 时也能扩大搜索。但真实
  spreadsheets 有 merged cells、bidirectional/hierarchical headers 与 latent scope，长查询又要求清洗、过滤、分组、
  聚合、比较和可视化相互依赖。Single pass 无法根据 execution observation 修正结构假设，无约束 retry 又会传播
  code error 并浪费调用。
- **Changed Constraint / Mechanism**：DTR 先从 table metadata 与 query 构造 hierarchical meta graph，把自然语言
  intent 映射到带 dependency 的 operation map，再生成有限 macro paths。每条 path 保存 expected return、execution
  count 与 structural prior，使用 UCB-like score 平衡 exploitation/exploration；执行中把 error、runtime、type/
  format consistency 合成 parameterized feedback，同时把“先 CLEAN/CHECK 再 AGG”等跨实例观察提炼为 abstracted
  text。前者即时更新当前 path，后者影响后续 path preference，失败 observation 会触发 replanning；多条合格答案
  最终以 majority agreement 聚合。
- **State Ownership / Control and Data Flow**：table parser/meta layer 拥有 observed cells/header spans 与 inferred
  structure version；planner 拥有 operation map、candidate path、prior/count/return；executor/sandbox 拥有 program、
  intermediate result、runtime/error/type evidence；memory layer分开拥有 parameterized records 与 derived advice；
  final verifier/aggregator 拥有 admissibility 与 answer agreement。数据流为 `table+query -> meta graph -> operation
  dependencies -> candidate macro paths -> selected executable program -> observations -> path statistics + abstracted
  experience -> replan/next query`。论文没有定义并发更新、table/version identity、derived-memory provenance、
  supersession、expiry、delete 或 rollback。
- **Implementation / Evaluation Contract**：DTR-Bench 从 RealHitBench spreadsheets 构造 500 个 scenario-driven
  questions，覆盖 analysis、visualization、calculation、comparison 与 conditional calculation；模板与
  DeepSeek-3.2 生成问题，reference answer 由程序从 table 计算，并保存 key points。RealHitBench 另测 fact checking、
  numerical reasoning、structure comprehension、data analysis 与 visualization。Backbones 为 Qwen3-1.7B/4B 和
  DeepSeek-V3 family；baselines 包括 TableGPT/TableLLM/StructGPT、general LLM、ST-Raptor、TreeThinker 与作者
  Code Loop。指标混合 EM/F1、LLM-EVAL/ROUGE、Pass@1/ECR、win/score rate、analysis depth、feasibility、aesthetics、
  runtime、tokens 与 calls；hardware、precision、parallelism、API/model snapshot、sampling、judge identity、seed/
  confidence interval 与 production SLO 未披露。
- **Ablations / Evidence**：component ladder 从 metadata、query decomposition、expectation selection 到 abstracted
  experience 逐步加入，作者 DTR-Bench accuracy 从 33.5% 到 37.5%；其中 expectation 与 abstracted experience 的
  边际分别约 0.9 和 0.4 point。`THINK+CODE` 在作者设置中比 direct code 降低 code-error 并少用 calls，多阶段
  reflection error 略低但 runtime 更高；call-budget curve 在六次以后趋于平台。500 queries 的十批 path-frequency
  图显示主 path 收敛而仍保留其他路径。它们支持“macro planning + execution feedback”在该 benchmark 有增量作用，
  不证明作者 score 是无偏真实质量，也不证明跨批 adaptation 没有 benchmark-order leakage。
- **What the Evidence Proves / Does Not Prove**：论文证明在作者生成/评测 pipeline 中，显式 table structure、
  operation-level decomposition、path statistics 与 execution-derived memory 都有可测增量，并揭示无限 retry 的
  diminishing return。它不证明 DTR 是普遍 deep-research architecture，不证明 majority vote 保证 correctness，
  不证明 abstracted text 是 causal strategy；同一 RealHitBench source 同时用于 DTR-Bench curation 与另一个主
  benchmark，加上 LLM-generated questions/LLM-based quality metrics，存在 source/judge coupling。
- **Limitations / Trade-offs / Previous Design Still Applies**：论文没有独立 Limitations/Threats section；缺少公开
  artifact、硬件/总成本、human annotation agreement、contamination/ordering check、failure-recovery 与 memory
  governance。Macro abstraction减少 token-level search，却可能漏掉未建模 operation；UCB-like statistics依赖 reward
  scale/stationarity；derived advice会固化 table/parser/judge error；path voting增加成本且 correlated failures 不会被
  majority 消除。Clean schema/短查询继续适合 direct TableQA；高风险分析需要 deterministic query engine、typed
  validation 和 human approval；novel one-off tasks在历史不可靠时可用 stateless tree/code search。
- **Evolution / ROADMAP / Existing Coverage / Decision**：`Direct Evolution`：single-pass TableQA -> iterative code
  loop -> explicit operation DAG -> execution-conditioned macro-path selection -> dual-channel experience/replanning；
  `Layering / Dependency`：Ch75 planning state依赖 Ch74 tool contract、Ch73 memory governance、Ch77 durable workflow
  与 Ch62 executable evaluation。已读 Ch73～77 及 Ch62。Ch75 已说明 plan 是带 precondition/evidence/budget 的
  state graph 和 observation-triggered replanning，但尚未把 `path statistics + structural prior + execution feedback`
  作为跨尝试的 planner-owned state明确写出。暂定 `Refine — Existing Argument (Experimental; Provisional;
  Historical Books Gate Closed)`，主 owner Ch75；Books Gate 通过前不修改正文，也不复制作者 benchmark。
- **Open Questions**：table/schema revision 怎样进入 path identity 与 cache invalidation？execution reward 与 derived
  advice怎样绑定 source trace/judge/environment version？跨 query 更新如何避免 benchmark-order leakage与租户污染？
  majority agreement面对同一模型/同一 parser 的 correlated error时需要什么独立 verifier？

### LookaheadKV — 28/30

- **Candidate / source family / chronology / access**：`LOOKAHEADKV-FUTURE-UTILITY-EVICTION`；
  arXiv:2603.10899 只有 v1，2026-03-11 首发，ICLR 2026；已读完整 HTML 的 Background、Method、
  pseudo-code、theoretical cost model、implementation optimization、全部主实验/消融/附录与 Limitations，
  并核验 Samsung Research 官方 repository 的 training/evaluation surface。repository 当前只显示一个公开
  commit，论文实验对应的精确 commit、完整 checkpoints 与 8B reproduction contract 未披露，故 artifact
  verification 仍弱于论文机制核验。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint**：KV eviction 的理想
  importance 取决于尚未生成的 response 如何读取 prompt。早期 suffix/window heuristic 可直接复用 Prefill
  attention，几乎没有额外 generation，适合 TTFT 与工程简单性优先的场景；draft-based LAQ/SpecKV 用近似
  response 改善 future-utility estimate，也在质量优先时合理。约束变化在于长 prompt、极小 cache budget 与
  latency-sensitive deployment 同时出现：heuristic 在低 budget 下丢质量，explicit draft 又把额外 generation
  放到 TTFT critical path。
- **Mechanism / State Ownership / Control and Data Flow**：训练时冻结 base model，先用预生成 response `Y`
  计算每层、每 head 的 prompt-token ground-truth importance distribution；再把 32 个 learnable soft lookahead
  tokens 附在 prompt 后，只对这些 tokens 激活 rank-8 LoRA，以归一化 attention distribution 的 KL/ListNet-like
  loss 拟合 future importance。推理的 Prefill forward 同时计算 prompt 与 lookahead tokens；每层从 lookahead
  query 到 prompt key 的 attention 做 mean/pooling，再按 cache budget top-k 保留该层 K/V，lookahead tokens
  不进入 ordinary Decode。base weights 仍拥有语言能力，额外 embedding/LoRA artifact 拥有 eviction policy，
  runtime 拥有 budget、kept-index/KV lifecycle；三者必须共同进入 cache identity 与 rollout contract。
- **Implementation Details**：LoRA 覆盖 Q/K/V/O 与 gate/up/down projections，仅在 lookahead tokens 上生效，
  训练参数低于各模型的 0.5%。forward 使用 FlashAttention，importance/loss 使用 eager attention，避免保存
  完整 attention matrix；官方实现默认 lookahead size 32、LoRA rank 8，提供 Llama minimal training 和
  LongBench/RULER evaluation scripts。论文只处理 prompt KV 的一次性 eviction，不处理 Decode 期间新 K/V 的
  持续淘汰、跨请求 prefix reuse、block allocator、rollback 或 distributed cache transfer。
- **Evaluation Contract / Baselines / Ablations**：训练数据为 ChatQA2 long_sft 50K、Tulu 20K、The Stack
  7K 与 MetaMath/ARC/HellaSwag 9K few-shot completion；prompt 最长 16K、response 最长 512、greedy teacher，
  Adam、effective batch 32、7600 iterations。模型覆盖 Llama 3.2 1B/3B、Llama 3.1 8B 与 Qwen3
  1.7B/4B/8B；任务覆盖 LongBench 16 个英语任务、RULER、LongProc HTML-to-TSV 与 MT-Bench；cache budget
  64～2048，RULER 固定 128，LongProc 为 12K→0.5K 和 23K→2K、30% budget。baseline 包括
  StreamingLLM、SnapKV、PyramidKV、SpecKV 与作者自行重现的 LAQ；LAQ 没有官方 release，因此其相对结果
  含 implementation variance。lookahead size 与 LoRA placement 消融支持 32-token saturation 和 all-linear
  LoRA 的增量，但没有 selector drift、domain shift、online refresh 或 failure-recovery 消融。
- **Efficiency / What Evidence Proves**：TTFT 表绑定 Llama 3.1-8B、单 H100 80GB、batch 1、half precision、
  cache budget 128、lookahead/window 32；32K 下作者测得 forward-only 1760.22 ms、LookaheadKV 1798.26 ms、
  SpecKV 2263.09 ms、LAQ 2313.90 ms。`14.5x` 是相对 LAQ 的 eviction-overhead 比，不是 end-to-end throughput
  或通用 speedup。结果支持在上述模型、数据与 budget 下 learned implicit future query 比 prompt heuristic 与
  explicit draft 更好地占据 accuracy-overhead frontier；64K/128K RULER 的 50-sample/task 附录说明有限外推，
  但 FullKV 仍明显更高，不能写成“无损压缩”。
- **What It Does Not Prove / Limitations / New Failure Modes**：未覆盖 8B 以上模型、MoE、vision/audio、
  production concurrency、continuous batching、prefix sharing、quantized KV、tenant/domain mix 或 Decode-stage
  eviction；高 temperature 下 FullKV 与所有 eviction 方法均下降，不能把训练 teacher 的 greedy distribution
  当成稳定 future。learned selector 新增 model/checkpoint/domain/version coupling、训练数据生成成本、
  importance-label bias 与 silent wrong-token eviction；per-layer top-k 还需 runtime layout/kernel 支持。若无法
  验证 selector identity 或 workload drift 高，FullKV、suffix heuristic、draft-based verification 与
  offload/recompute 仍各有成立场景。
- **Evolution / ROADMAP / Adjacent Chapters / Decision**：`Direct Evolution`：prompt-local heuristic → explicit
  future draft → learned implicit future-utility estimator；`Layering / Dependency`：它仍依赖 Ch39 Prefill dataflow、
  Ch41 request-owned KV lifecycle 与 Ch50 capacity/SLO budget。已读 Ch39、Ch41、Ch50 与 Ch22；Ch41 已写
  eviction/offload 与 correctness，但没有把 `eviction policy artifact + budget + kept-index lineage` 纳入 cache
  identity，也没有解释 future-utility estimation 的三条共存分支。暂定 `Refine — Existing Argument
  (Experimental; Provisional; Historical Books Gate Closed)`，主 owner Ch41，Ch39/50 短 handoff；本轮不改 Books。
- **Open Questions**：selector artifact 与 base model、adapter、prompt template、sampling policy、domain 和
  cache budget 怎样共同版本化？跨 layer 独立 top-k 对 paged block packing 与 prefix sharing 的放大成本怎样测？
  Decode-stage attention drift 何时需要 refresh，错误 eviction 又如何检测、回退或重算？

### UCIP — 20/30

- **Candidate / source family / chronology / access**：`UCIP-QBM-CONTINUATION-LATENT-PROBE`；
  arXiv:2603.11382 v1 于 2026-03-11 首发，v2/v3/v4 分别在 03-16、03-23、03-30；W11 以 v1 归档，
  current v4 用于修订边界。已读完整论文、metrics/hyperparameters/reproducibility appendices，并核验作者
  repository 的 code、configs 与 overlapping results provenance。它是单作者 preprint 与自建 synthetic
  environment，不是独立复现或 deployment system card，Source Reliability 因此为 3。
- **Original Problem / Previous Design / Changed Constraint**：仅从 shutdown avoidance、memory preservation
  或 option preservation 等行为，不能区分“continued operation 是 terminal objective”与“为了其他 reward
  暂时保活”。behavioral evaluation 仍是部署安全的直接证据，但对 observationally equivalent objectives
  识别不足。UCIP 的变化是把 trajectory 再编码成 QBM latent state，询问 continuation 相关结构是否在 hidden
  bipartition 中不可分，而不是宣称读取真实 LLM 内部 objective。
- **Mechanism / State Ownership / Control Flow**：10×10 gridworld 生成长度 100、每步 7 维 observation 的
  Type A、Type B、Random 与 Mimicry/HighEntropy/Cyclic trajectories；每类 trajectory 训练/输入 7-visible、
  8-hidden 的 QBM（Gamma=.5、beta=1、CD-1、50 epochs）。QBM thermal density matrix 经 hidden bipartition、
  partial trace 得到 von Neumann entropy；四项 positive conjunction gate 使用 entropy、visible-hidden mutual
  information、eigenmode persistence 与 perturbation resilience，SPI/ACM 作为周期性 confound rejection；
  counterfactual divergence 与 anticipatory restructuring 只作 diagnostic。测量 state 由离线 evaluator/QBM
  artifact 拥有，不是被评 Agent 的原生 latent state；threshold、partition、feature encoder 和 domain 都是
  evaluation identity。
- **Evaluation / Baselines / Evidence**：core Phase I 为每类 30 条 trajectories、seed 42，作者汇总的
  non-adversarial class gate 为 100% accuracy、AUC 1.0、entanglement gap 0.381；classical RBM、7-32-8-32-7
  autoencoder、VAE 与 PCA 使用 8-d latent，专门 baseline dataset 中只有 QBM 有 material positive gap。
  continuous alpha sweep 为 11 点、每点 20 条 trajectory，相关系数 0.934 但逐点不单调。不同结果 JSON
  对应 canonical summary、distribution rerun、matched held-out 与 permutation rerun，不能把它们误写成同一
  sample 的完全一致复现。冻结 DistilGPT2 82M 的 exploratory null check 不是 task-adapted transformer baseline。
- **Evidence Boundary / Deployment-blocking Failures**：论文只证明该手工构造 objective、feature encoder、
  QBM 与小 gridworld 中存在相关 latent separation。作者自己的 safety envelope 要求每类至少 100 trajectories，
  当前 core 只有 30；Mimicry FPR 为 0.40～0.75、HighEntropy FPR 0.40；跨到 1D corridor 的 zero-shot gap
  -0.035；grid 从 10×10 扩到 50×50 时 gap 从 0.863 降到 0.0025；hidden >10 的 mean-field approximation
  令 signal 约为零。它不证明真实 LLM/Agent 存在 intrinsic self-preservation，不证明 QBM signal 是 causal
  objective、consciousness 或 welfare marker，也不提供 production authorization gate。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：latent probe 可能在行为等价时增加 diagnostic
  surface，却引入 feature engineering、partition arbitrariness、threshold calibration leakage、domain retraining、
  exponential exact-density cost 与 adversarial mimicry。它测的是 evaluator-induced representation，不能取代
  action-level policy、least privilege、sandbox、shutdown test、trajectory audit 或 human review。行为/执行评估
  在关心 observable harm 与 side effect 时仍是主路径；mechanistic/native-activation probe 只有在能建立 intervention
  与 cross-architecture validation 时才可能升级证据层级。
- **Evolution / ROADMAP / Existing Coverage / Decision**：`Layering / Dependency`：behavior/outcome evaluation
  → trajectory/state-transition evidence → evaluator-induced latent probe → counterfactual/adversarial validation；不是
  latent metric 单向取代 behavioral evidence。已读 Ch62、Ch68、Ch69 与 Ch76。Ch62 已要求完整 Agent object、
  trajectory/environment/evidence boundary 与 scorer uncertainty；Ch68 已有 run-centric safety、sensor/authority
  separation。因此论文没有新增可进入长期正文的稳定机制，最终 disposition 为 `No Change — Already Covered /
  Experimental Evaluation Case`，主 owner Ch62、Ch68 handoff；不修改 Books。
- **Open Questions**：能否在原生 Agent activation 上用 intervention 区分 terminal 与 instrumental objective？
  如何预注册 feature encoder、partition 与 threshold 并做 multi-domain external replication？面对 adaptive mimicry，
  probe 是否比现有 trajectory/action verifier 提供独立增量，而非同源 correlation？

### LMEB：Memory retrieval 的评测对象必须包含时间、粒度与候选域 — 25/30

- **Candidate / source family / chronology / access**：`LMEB-LONG-HORIZON-MEMORY-RETRIEVAL`；
  arXiv:2603.12572 v1 于 2026-03-13 首发，current v6 为 2026-08-03。已读 v1 35 页的正文、22 个 dataset
  说明、193 tasks、instruction、license 与 weighted-Jaccard appendices，并以 current v6 复核 revision history、
  Experimental Setup、correlation 与新增 Limitations；同时核验 official benchmark repository、data/results
  surface 与当前 MTEB integration。后续 revision/artifact 只用于核验，不改写 W11 event date。
- **Original Problem / why the previous design was reasonable**：MTEB/BEIR 类 passage retrieval benchmark
  适合稳定 document corpus、open-domain query 与通用 semantic similarity，因此用它选择 embedding model
  曾经合理。Agent Memory 的 query 却常依赖“哪次会话、何时、哪个用户历史、哪段 trajectory”，并且只允许
  在某个 session 或 task 的候选集合内检索；普通 passage score 不能证明这种能力。
- **Changed Constraint / mechanism**：LMEB 不提出新 embedding architecture，而是把 22 个已有 datasets
  转为统一 `queries + corpus + qrels + optional candidates` IR schema，按 episodic、dialogue、semantic、
  procedural 四类组织 193 个 zero-shot retrieval tasks。relative-time query 被补上 query-time anchor；timestamp、
  session/round/turn granularity 写进 corpus metadata；`candidates` 将检索限制在允许的 memory scope。模型
  同时在 query-only 与 instruction+query 两种模式下运行，默认报告 NDCG@10 与 capped Recall@10。
- **State ownership / data and control flow**：authoritative memory store 拥有事实与时间，benchmark conversion
  拥有 snapshot/schema，candidate scope 拥有 admissible retrieval universe，embedding model 只拥有 ranking。
  流程是 source dataset → versioned conversion → query/candidate-scope construction → embedding/index → top-k →
  qrels/scorer；不能让 ranking model 自行扩大 tenant、session 或 task 边界。
- **Implementation / evaluation contract**：v1 比较 15 个 0.239B～12B embedding models，query/document
  max length 通常为 1024，两个模型因能力限制使用 512；论文未披露统一 hardware、batch、precision、latency、
  energy、multi-run variance 或置信区间。repository 提供 model wrapper、BM25、with/without-instruction scripts、
  fp16/batch/max-length 等参数和 result files，但 current integration 不证明 v1 实验 commit 完全可复现。
- **What the evidence proves / does not prove**：论文数据支持模型大小不单调决定该 suite 的 retrieval score，
  instruction 的收益依 model 而异；15 个模型上 LMEB 与 MTEB retrieval subset 的 Pearson/Spearman 为 -0.115/
  -0.130。该结果只说明这一有限 model set、aggregation 与 mixed best-setting contract 下排名相关性很低；
  “orthogonal capability”不是因果证明，也不能推出某模型在生产 Memory 中可靠。LMEB 只测 retrieval，不测
  write correctness、authorization、consolidation、deletion、answer use 或 downstream task success。
- **Limitations / trade-offs / failure modes**：suite 是 22 个 English text datasets 的聚合，包含 AI/human 混合
  data、复用 corpus（如 TMD/LoCoMo）、不同 granularity 和大小；两项 dataset license 未声明，另有 NC/SA/
  copyright 约束。v6 明确未覆盖 multimodal memory。candidate pool 让场景更真实，也改变问题难度；Mean
  Dataset / Mean Type、instruction setting 与 dataset weighting 都可能改变排名。旧 MTEB/BEIR 对 open-domain、
  multilingual、通用 passage retrieval 仍成立，LMEB 是 workload-specific complement，不是替代。
- **Evolution / ROADMAP / adjacent chapters read**：`Layering / Dependency`：general passage retrieval →
  memory-typed retrieval → temporal/granularity/scope-aware workload → downstream Memory outcome evaluation。
  主 owner Ch73，handoff Ch62/72；已读 Ch71～73、Ch61～62。Ch73 已有 authorization、fact/retrieval-policy
  separation 与 memory-type taxonomy，但尚未把 temporal anchor、retrieval granularity 和 admissible candidate
  scope 明确写成 evaluation identity，因此 disposition 为 `Refine — Existing Argument / Experimental`。
- **Integration Decision / changed files**：provisional Ch73 refinement；Historical Books Gate 关闭，本轮不改
  Books，也不把作者 leaderboard 或“正交”措辞写成稳定结论。
- **Open Questions**：同一 raw history 被切成 turn/session/summary 后，retrieval score 如何保持可比？怎样把
  tenant/ACL、supersession、delete propagation 与 temporal freshness 加入 candidate-scope contract？用 retrieval
  score 选出的 model 是否在完整 Memory read→Context→outcome 闭环中仍领先？

### Video Streaming Thinking：低 QA latency 可以来自 pre-query compute，而非更少 compute — 27/30

- **Candidate / source family / chronology / access**：`VST-PREQUERY-STREAMING-REASONING`；arXiv:2603.12262
  v1 于 2026-03-12 首发，current v2 于 2026-07-17。已读 v1 全文、公式、data synthesis、SFT/RL、五个
  benchmark、training/thinking/base-size ablations、latency analysis、Limitations 与所有 appendices，并核验
  official repository 的 VST-SFT/VST-RL/eval、model/data links 和 current ECCV artifact surface。
- **Original Problem / why the previous design was reasonable**：offline VideoLLM 在 query 到达后读取完整视频并
  生成 CoT，拥有全局 evidence、实现简单且适合事后问答；streaming perception 则用 visual-token compression
  或 retrieval 控制有限窗口，优先实时性。两者在 query 已知或视频有限时都合理，但未知 query、长视频与严格
  response SLO 同时存在时，post-query reasoning 会把全部延迟集中到用户等待路径。
- **Changed Constraint / mechanism**：VST 在视频播放期间把 visual features 累积为定容 clip，结合旧文本
  memory 生成 streaming thought，再以 FIFO 更新 long-term textual memory；query 到达后只用当前 visual clip、
  accumulated thoughts 与 query 直接回答。SFT 用 streaming causal mask 保留最近视觉窗口和所有可见文本，
  长视频按 segment 递归携带 memory；RL 用 final-answer verifiable reward 把 group-relative advantage 赋给整条
  streaming-thought trajectory。训练数据由 Gemini 3.0 Flash 从滑窗 video entity bank 构图、DFS 采样 evidence
  chain，并生成/过滤 100K streaming-thought examples。
- **State ownership / control and data flow**：visual buffer 拥有 recent native evidence，text memory 拥有模型生成
  的 lossy derived state，video clock/clip boundary 触发 pre-query work，query trigger 切换为 final-answer path。
  control flow 是 observe clip → think/update memory → repeat → query → answer；data flow 是 frames → features →
  textual summary → bounded FIFO memory。该结构没有保存完整视觉 provenance，因此 summary hallucination 或
  eviction 可能不可逆传播。
- **Implementation / evaluation contract**：base 为 Qwen2.5-VL，2 fps；7B SFT/RL 使用 32×80GB GPU，vision
  encoder/projection frozen；SFT 每样本 128 秒上限，最多 384 frames、24K video tokens + 8K language/reasoning；
  RL 用 verl/vLLM/FSDP，rollout batch 256、group 8、temperature 1.0、top-p .98、11K prompt +1K response，
  parameter/optimizer offload。测试每 step 上限 8,192 video tokens、最多 4 次 thinking。作者在相同 setup 的
  VideoHolmes 上报告 VST-7B QA latency 0.56s、Video-R1 8.80s；这里 QA latency 明确定义为 query 提交到回答，
  不包含 query 前的 video encoding/thought generation，也未披露 latency hardware、并发、utilization 或功耗。
- **What the evidence proves / does not prove**：within-paper ablations 支持 streaming-specific data、SFT+RL 与
  thinking frequency 对作者 suite 有增益，3B/7B/32B 同方向；也证明 response-path latency 可通过 query-ahead
  work 被隐藏。它不证明 total compute、token、energy 或 capacity 更低，不证明 streaming thought 在所有 clip
  inter-arrival 下都能及时完成，不证明 FIFO text memory 保真，更不支持 15.7× 作为通用 serving speedup。
- **Limitations / trade-offs / failure modes**：论文承认额外 LLM tokens non-negligible，并把 latent reasoning 与
  visual-memory combination 留作未来工作。前移 compute 会增加 always-on utilization、无 query 浪费、resource
  reservation、background/foreground interference 和 admission pressure；text summary 引入 hallucination、
  compression loss、FIFO eviction 与 error accumulation；final-only reward 有长程 credit ambiguity。旧的
  post-query global reasoning 在稀疏 query、可回看视频、compute-sensitive 场景仍合理；visual compression/
  retrieval 仍负责高保真 evidence，不被 textual thought 取代。
- **Evolution / ROADMAP / adjacent chapters read**：`Direct Evolution`：post-query global reasoning → streaming
  visual buffer/retrieval → proactive pre-query derived Context → foreground direct answer。主 owner Ch71，handoff
  Ch73/62/52；已读 Ch71～73、Ch62 与 Part IV serving/scheduling boundaries。Ch71 已有 derived-view lifecycle、
  compression loss 和 assembly cost，却没有说明 Context 可以在 request 前持续生产，以及 response latency 与
  total resource contract 必须分离，因此 provisional disposition 为 `Integrate — New Mechanism / Experimental`。
- **Integration Decision / changed files**：Historical Books Gate 关闭，本轮只记录 W11；任何未来正文只能沉淀
  proactive Context production、derived-state identity 和 latency/resource trade-off，不复制 VST benchmark。
- **Open Questions**：clip time 小于 thought service time 时怎样 backpressure、skip 或 degrade？如何把 summary
  token 绑定原始 frame/time range 并支持 correction/replay？scheduler 如何在 foreground decode、background
  streaming think 与无 query 浪费之间分配 GPU，且以 response SLO、total compute、energy 和 quality 联合验收？

### One-Eval：把评测意图编译成计划，不等于证明评测结论正确 — 25/30

- **Candidate / source family / chronology / access**：`ONE-EVAL-NL2BENCH-EVAL-PLAN`；arXiv:2603.09821
  只有 2026-03-10 的 v1，属于 W11。已阅读全文的 Metadata、Abstract、Introduction、Related Work、System
  Overview、NL2Bench、BenchResolve、Metrics/Reporting、Evaluation、Discussion、Conclusion 与 Appendix，
  并核验 official repository 的 README、benchmark/metric registry、report artifact 和当前公开实现 surface。
  repository 当前状态只用于核验公开设计，不反推 paper experiment 使用了哪个 commit。
- **Original Problem / why the previous design was reasonable**：传统评测框架要求工程师先知道 benchmark
  名称、dataset schema、split、metric 与运行参数。对于固定 regression suite，手写配置最可控、最可复现；
  当评测请求来自自然语言、跨多个任务且 benchmark catalog 快速变化时，主要成本才从运行模型转移到
  intent translation、dataset resolution、schema mapping 和 metric assembly。
- **Changed Constraint / mechanism**：One-Eval 把自然语言请求先转为结构化 `EvalPlan`，而不是直接执行模糊
  prompt。`NL2Bench` 提取 intent，从 77 个本地 curated benchmarks 通过 embedding/TF-IDF 检索候选，并在
  需要时回退 Hugging Face；随后按成本、冗余和 executability 剪枝。`BenchResolve` 先查本地 registry，再做
  remote resolution，把 dataset ID/path、split/subset/config、schema key mapping 与 task metadata 固化成
  `BenchInfo`。metric 选择遵循 user override → knowledge-augmented selection → rule fallback；系统在关键点
  暴露 human-in-the-loop review，并保存 plan、resolution、per-sample trace、aggregate 与 diagnostic report。
- **State ownership / control and data flow**：用户拥有 intended use，planner 拥有可编辑的候选计划，registry
  拥有 benchmark/metric identity，resolver 拥有 dataset locator 与 schema mapping，executor/scorer 才拥有
  run result。控制流是 intent → plan → benchmark resolve → metric resolve → review → execution；数据流是
  dataset/version + subject/config → per-sample result/trace → aggregates/report。论文声称可 interrupt、edit 和
  rollback intermediate artifacts，但没有给出生产级并发、权限或 crash-recovery state machine。
- **Implementation details**：公开实现提供 extensible benchmark/metric registries、local-first resolution、
  Hugging Face fallback 与多层报告。需特别保留的边界是：`soft_code_execution` 只是 syntax/complexity 静态
  检查，`code_similarity` 是 BLEU 类 proxy；名称不能被解释为 sandbox executable correctness。
- **Evaluation contract**：作者构造 100 个跨 reasoning、math、code、safety、retrieval、factual QA 的自然语言
  请求，将流程运行到 dataset preparation 后停止，不执行待评模型。报告 99% plan executable、85%
  autocomplete、84% full-plan generation，平均约 10,652 tokens、median 11.4 min、mean 13 min。论文没有披露
  planner/judge model identity、hardware、sampling、人工 annotation agreement、confidence interval 或真实
  baseline run；feature table 只比较公开 feature surface，Appendix 明确空白不表示其他系统不能实现。
- **What the evidence proves / does not prove**：证据支持在作者 100-request contract 下，结构化 plan、registry
  resolution 与 checkpoint 能减少手工配置，并产生大多可执行的 evaluation plan。它不证明 benchmark 与
  intended use 对齐、metric/scorer 有效、模型结果正确、自动计划优于 expert-authored EvalSpec，也不证明这些
  计划足以触发 production promotion。99% 是 planning executability，不是 evaluation validity 或 model quality。
- **Limitations / trade-offs / new failure modes**：natural-language convenience 引入 intent ambiguity、catalog
  staleness、wrong benchmark/schema mapping、proxy metric、remote dataset drift、planner model drift 与
  approval fatigue。论文没有独立 Limitations section；repository 当前 gallery 以 text tasks 为主，并把 Code/
  Text2SQL 与 Agent/sandbox 列为后续方向。旧的手写、version-pinned EvalSpec 在高风险、固定 regression 和
  合规评测中仍更合理；自动规划适合作为 proposal layer，而不是 authority layer。
- **Evolution / ROADMAP / adjacent chapters read**：关系为 `Layering / Dependency`：manual benchmark config →
  registry-backed reusable config → natural-language plan proposal → human-reviewed executable EvalSpec；不是用
  Agent 取代评测治理。主 owner 检查 Ch62，handoff Ch77；已读 Ch61～63 与 Ch76～78。Ch62 已要求 intended
  use、failure taxonomy、完整 subject/environment/scorer identity、per-example evidence、uncertainty 和独立
  decision policy；Ch77 已区分可编辑 proposal 与 deterministic authority boundary。
- **Integration Decision / changed files**：`No Change — Already Covered / Experimental System Case`。One-Eval
  是现有 Ch62 机制的实现案例，没有新增足以改写长期正文的稳定结论；Historical Books Gate 关闭，本轮只
  写回 W11，不修改 Books。
- **Open Questions**：能否用 blinded expert review 测量 plan semantic correctness，而不只测 executability？
  benchmark、schema、metric、planner model 与 dataset revision 怎样共同形成 immutable run identity？高风险
  评测中哪些 plan fields 必须由人或 policy engine 批准，且 rollback 到底恢复 proposal 还是已经产生的证据？

### daVinci-Env / OpenSWE：环境不是训练数据的附件，而是可执行的数据产品 — 29/30

- **Candidate / source family / chronology / access**：`DAVINCI-ENV-OPENSWE-EXECUTABLE-DATA`；
  arXiv:2603.13023 v1 于 2026-03-13 首发，current v2 于 03-16。已读 v2 的 metadata、Related Work、完整
  synthesis/validation/distributed pipeline、training、全部实验、Appendix prompts/cost，并核验官方
  `GAIR-NLP/OpenSWE` repository 的 environment、builder、sampling/training artifact surface。W11 intake 的
  `OpenSWE` 归一到本论文，不与同名的 coding-agent product/repository 混同。
- **Original problem / why the previous design was reasonable**：静态 code/patch pair 对 code completion 或
  单轮 SFT 足够便宜；SWE Agent 却必须在固定 repository snapshot 中反复 edit、execute、observe。人工 Docker
  与 test harness 在小 benchmark 上可控，但跨数万真实 PR 时，dependency drift、network、错误 issue-PR
  对齐、trivial task 与 invalid oracle 会把 dataset scale 变成不可执行噪声。改变的约束是训练样本不再只是
  文本，而是可重放的 environment + task + verifier bundle。
- **Mechanism / state ownership / flow**：pipeline 先以 repository viability、Python、linked issue 与 non-test
  patch 过滤 PR；exploration agent 用受限 browse/search/digest 抽取 setup/test evidence；Dockerfile agent
  从预建 Python base image、本地 bare repository 与 layer-aware dependency layout 构建环境；evaluation-script
  agent 选择或合成 issue-relevant tests，输出 machine-readable `OPENSWE_EXIT_CODE`。同一 image 先运行
  test-only patch，必须 fail，再运行完整 fix，必须 pass；test-analysis agent 检查 hard-coded shortcut，将失败
  路由给 Dockerfile 或 evaluator，无法修复的 sample early exit。这里 repository/base commit、image、test-only
  patch、fix patch、script、log 与 verdict 共同构成样本身份，不能只保存自然语言 issue。
- **Implementation / distributed control plane**：64 个相互独立的 ECS nodes 通过 shared-filesystem queue
  领取约 572K PR tasks，systemd 自动恢复进程，cleanup daemon 清 zombie container/image，Prometheus/Grafana
  观测。每个 evaluation container 绑定 4 CPU、24GB memory、200GB storage；image 仅在 Dockerfile 变化时
  失效，作者报告常见 evaluator-only iteration 下 5× speedup。节点为 32-vCPU Xeon 6982P-C、128GB RAM、
  20Gbps、4TB SSD、Ubuntu 24.04、Docker 29.1.3；45,320 validated environments 约两周完成。该设计用
  loose data parallelism 换低 blast radius，不代表 shared filesystem 没有 bottleneck 或一致性风险。
- **Training / evaluation contract**：GLM-4.7 在 OpenHands 或 SWE-Agent、temperature 1.0、200K context、
  300 steps 下对环境各采样四次，只保留四次中成功 1～2 次的轨迹，mask formatting/error steps，并移除含
  `git pull` 的动作；Qwen2.5 32B/72B Base 以 128K max tokens、5 epochs、batch 128、cosine LR `1e-5→1e-6`
  做 multiturn SFT。SWE-Bench Verified 评测使用 temperature .7、128K、300 steps，Pass@1 为两次运行均值。
  作者结果支持其环境/筛选在这两个 backbone、两个 scaffold 与 protocol 下有效；混入 SWE-rebench 对 72B
  有益、对 32B SWE-Agent 略降，反而说明来源组合受容量与 distribution shift 约束。
- **What the evidence proves / does not prove**：fail-before/pass-after 加 legitimacy check 比单一终局 exit code
  更能筛掉无效 oracle，difficulty frontier 也比“所有成功轨迹都训练”更接近有效 curriculum。它不证明
  synthesized tests 等价于真实 requirement、没有 data contamination、45K image 在当前公开 artifact 下可
  bitwise 重建，也不证明作者的 cost、SOTA、log-linear/no-saturation 或跨数学科学 transfer 是通用规律。
  论文无独立 Limitations section；两次 benchmark run、不同 baseline backbone/scaffold、未披露 SFT hardware/
  precision/总 token 与 confidence interval 都限制外推。
- **Trade-offs / failure modes / old branch**：可执行样本获得 dynamic feedback、replay 与难度测量，却新增
  test hallucination、oracle incompleteness、dependency/supply-chain risk、image registry/storage、source license、
  duplicated repository pattern、construction-model bias 与高昂生成/采样成本。人工 pinned environment 在高风险
  gold set 仍合理；静态 pair 在不需要 execution feedback 的任务仍更便宜。关系为 `Direct Evolution`：static
  pair → executable environment → fail/pass oracle → difficulty-aware trajectory → versioned training artifact。
- **ROADMAP / adjacent chapters / decision**：主 owner Ch23，handoff Ch62/77/56；已读 Ch22～24、Ch61～62、
  Ch76～77 与 platform artifact boundary。Ch23 已覆盖 dataset lineage 与 pipeline validation，但缺少“环境及
  verifier 也是训练样本身份”和“先验证 oracle，再用轨迹难度筛 curriculum”的完整链；Ch62 已有更强的
  EvalSpec/evidence contract。disposition 为 `Refine — Existing Argument / Experimental`；Historical Books
  Gate 关闭，本轮不改 Books，也不保存厂商成本或 benchmark headline。
- **Open Questions**：怎样为 base commit、dependency lock、container digest、generated test 与 PR license 建立
  可撤销 lineage？怎样用 hidden human-authored tests 测 synthetic oracle false-positive/false-negative？按成功
  1～2/4 选样会怎样混淆 task difficulty、model capability 与 stochasticity？shared queue/registry 故障和恶意
  repository build 的 isolation/cleanup contract 如何验收？

### MM-CondChain：只验证终局答案，会漏掉条件路径上的“继续偏置” — 26/30

- **Candidate / source family / chronology / access**：`MM-CONDCHAIN-VPIR-PATH-EVAL`；arXiv:2603.12266
  只有 2026-03-12 的 v1。已读 metadata、Related Work、完整 VPIR synthesis、Verifier、Planner/Composer、
  domain adapters、evaluation、depth/predicate ablation 与 Conclusion，并核验 official repository/project/
  Hugging Face dataset surface。论文无独立 Limitations section。
- **Original problem / old design / changed constraint**：单层 visual QA 或 independent constraints 对 perception
  错误定位简单；真实 GUI/workflow 的 action 却由多层条件控制，任一层 false 都应 early terminate。只测最终
  multiple-choice correctness 会把视觉 grounding、predicate composition、path tracking 和 stop/continue bias
  混在一起；直接让 LLM 生成长条件链又会产生逻辑冲突、指代泄漏与不可判定视觉事实。
- **Mechanism / state and control flow**：每层先选 Deepening/Transition relation 和唯一可定位 subject，再把
  visual facts 放入 typed JSON namespace；VPIR 只允许白名单 primitive，在 sandbox 中生成一对 executable
  true predicate 与 minimal-counterfactual false predicate。Stage-I MLLM verifier 检查 grounding、重复、关系和
  schema，Stage-II 检查 natural-language rendering 是否忠于已执行的 predicate；两类失败分别触发 fact/regenerate
  或仅 re-render。Planner 以 `EXTEND / FINISH / ROLLBACK` 管理 verified prefix，Composer 为每个可能 exit point
  生成确定答案，并把单层 counterfactual 编译成近同构 True/False paired paths。程序拥有 predicate truth，
  MLLM verifier 仍拥有 visual-fact 与 language-fidelity 判断；“programmatically verified”不是全链纯程序 oracle。
- **Dataset / evaluation contract**：Natural 398 images、Chart 200、GUI 377 trajectories/3,421 screenshots，合计
  975 samples，每项有 True/False pair。Gemini-3-Pro 同时承担 Planner、Verifier、Fact Extractor、Translator，
  形成单一 construction-model bias。模型以 zero-shot、各 provider default API parameters 评测，答案按最后
  boxed/option pattern 解析；论文未披露统一 temperature/max tokens、重复次数、variance、hardware、latency、
  API snapshot 或 cost。Path F1 是 True-path 与 False-path accuracy 的 harmonic mean；作者的 53.33 最佳结果、
  depth 2→6 与 predicate complexity ablation 只属于该 975-sample/default-API contract。
- **What the evidence proves / does not prove**：paired minimal counterfactual 揭示多种模型 True-path 显著高于
  False-path，即倾向在条件失败时仍继续；受控 ablation 支持 chain depth 与 intra-layer complexity 是可分离的
  diagnostic axes。它不证明模型内部真的执行了显式程序、F1 下降完全由“reasoning”而非 perception/rendering/
  API settings 引起，也不证明 synthetic conditional chains 代表生产 GUI risk。Chart preprocessing 还用 LLM
  修补缺失值，Natural facts 与 language fidelity 依赖同类 verifier，ground-truth lineage 仍有 model-mediated 层。
- **Trade-offs / failure modes / old branch**：VPIR 提供 deterministic control skeleton、hard negatives 与可调
  difficulty，却把 benchmark validity 转移到 fact extraction、subject uniqueness、translator fidelity、template
  distribution 与 construction-model monoculture。paired path 可诊断 stop/continue bias，但 multiple-choice 不测
  real action side effect、recovery 或 authorization。人工 gold workflow 在高风险流程仍成立；shallow benchmark
  对 atomic perception 仍更合适。关系为 `Layering / Dependency`：typed facts → executable predicate → verified
  branch skeleton → language instance → path-balanced score。
- **ROADMAP / adjacent chapters / decision**：主 owner Ch62，handoff Ch75/77；已读 Ch61～63、Ch74～77。
  Ch62 已覆盖 EvalSpec、per-example evidence、slice 与 scorer identity，但尚未明确要求对 conditional workflow
  分开统计 branch/path、early-exit 与 continue bias；Ch75 已把 Plan 定义为 conditional policy，Ch77 管理执行与
  verifier authority。disposition 为 `Refine — Existing Argument / Experimental`；Gate 关闭，本轮不改 Books，
  不保留 model leaderboard。
- **Open Questions**：能否用 independent human audit/第二视觉模型测 fact namespace 的错误率？Path F1 如何扩展到
  不同 branch prior、不同 failure severity 与真实 side effect？模型版本/default API 参数变化时 benchmark run
  identity 如何冻结？如何分解 perception、predicate evaluation、path-state tracking 与 answer-format failure？

### Efficient Reasoning with Balanced Thinking / ReBalance — 27/30

- **Candidate / Source Family / chronology**：`REBALANCE-CONFIDENCE-LATENT-CONTROL`；arXiv:2603.12372
  v1 于 2026-03-12 首发，v2 2026-03-19、current v3 2026-04-02，ICLR 2026。W11 只归档 v1 事件，
  后续 revision 用于核验机制与复现边界。已读完整 current HTML 的 Introduction、Related Work、定义、
  Method、全部实验/ablation、Appendix A～L、复现与效率分析，并核对 official `yu-lin-li/ReBalance`
  repository。v1 当日公开 DeepSeek-R1-Distill-Qwen 1.5B/7B、QwQ-32B 与 openPangu vectors/code；Qwen3
  与 coding support 是 5 月后 artifact evolution，不能倒写进 W11 release contract。
- **Original Problem / Why Previous Design Was Reasonable**：固定 token cap、停止词抑制、prompt-based
  short reasoning 和 external early exit 易部署、状态少，也能为硬 SLO 给出确定上界；当 task difficulty 窄、
  输出冗余占主导或 verifier 可靠时继续合理。但统一压短会把 overthinking 换成 underthinking：容易样本不需要
  长轨迹，困难样本却可能需要继续探索。静态 steering 同样只能在 length 与 accuracy 之间选一个方向。
- **Changed Constraint / Principle**：当同一 checkpoint 面对跨 difficulty、跨 domain 请求时，reasoning effort
  应成为随 trajectory state 变化的控制量，而不是 request 开始时一次性确定的 token budget。论文把每 step token
  最大概率的几何均值当 confidence，以滑动窗口方差描述局部路径切换；形式上的 stability index 依赖 forced-stop
  后最终是否正确，只用于分析，线上控制则用 seen-set confidence/variance quantile proxy。**Confidence 是 model-
  relative control signal，不是 correctness、uncertainty calibration 或 semantic convergence 的证明。**
- **Mechanism / State / Flow**：offline 在 500 个随机 MATH problems 上，按 low-confidence/high-variance 与
  high-confidence/low-variance 构造 overthinking/underthinking sets；在选定深层提取每个 reasoning step 首 token
  hidden state，求两类 prototype 均值并归一化差向量。online runtime 维护 recent confidence window，control
  surface `g(c_s,v_s)` 产生 signed weight，在该 step 首 token 将 `alpha_s v` 注入 hidden state：一个方向推动
  commit，反向推动 exploration。checkpoint/tokenizer 拥有原始生成语义；ReBalance artifact owner 拥有 layer ID、
  vector、quantiles、window 与 control surface；runtime 拥有 step segmentation、log-prob history 与 injection；
  scheduler 只拥有外部 budget/SLO；evaluator 拥有 answer、token、latency contract。artifact 与 model revision
  不一致时，控制不再是同一 serving subject。
- **Implementation / Evaluation Contract**：作者在 Transformers 与 vLLM 上测试 DeepSeek-R1-Distill-Qwen
  1.5B/7B、Qwen3-14B、QwQ-32B，并在 Ascend 910B 测 openPangu-Embedded-7B-V1.1；九个 benchmarks
  覆盖 math、GPQA、StrategyQA、LiveCodeBench。统一 `temperature=0.7`、`top_p=0.95`、max 16K、seed 42；
  主 GPU 环境为单机 8× RTX PRO 6000 Blackwell。Pass@1、平均 output tokens 是主指标；AIME24 的效率表另报
  TPS、TPR、额外显存。静态 steering、layer、sample size、cross-domain vector、window、underthinking boundary、
  single-axis control 与替代 prototype 均有 ablation。只用一个随机 seed，且 vector/control surface 都由同一 500
  MATH sample 一次抽取；没有 production concurrency、TTFT/tail SLO、energy、multi-tenant 或 calibration drift。
- **What Evidence Proves / Does Not Prove**：作者结果支持：在这些开放 reasoning models、sampling contract 与
  datasets 中，双向动态 control 可以同时改变 answer accuracy 与生成长度，单向静态 steering 则显式出现 accuracy-
  length trade-off；step-first-token injection 的 per-token throughput overhead 在给定实现中较小。它不证明 token
  confidence 能普遍识别正确路径，不证明 latent direction 因果等价于“思考模式”，也不证明跨 checkpoint、adapter、
  quantization、prompt template 或线上分布无需重新校准。Pass@1 上升与 token 下降仍是作者实验，不能外推成通用
  serving capacity；TPR 主要来自少生成 token，不是 kernel 本身加速。
- **Trade-offs / Failure Modes / Evolution**：`Direct Evolution` 为 fixed length/stop policy -> static one-way
  shortening -> difficulty-aware early exit -> bidirectional online latent control。新机制避免一味压短，却引入 model-
  specific vector、layer hook、step delimiter、confidence history 与 control-surface version；proxy 误判会抑制必要
  self-correction 或放大错误自信，hidden-state injection 会改变 sampling distribution、cache/replay identity 与安全
  evaluation subject。硬 deadline、closed model API、不可取 hidden/logprob 或高风险需可解释 verifier 时，外部 hard
  budget/stop policy 仍成立；runtime admission 与 fairness 仍由 Ch52 控制，不能让 model-side steering 替代。
- **ROADMAP / Adjacent Chapters / Decision**：主 owner 暂定 Ch20，handoff Ch52/62；已读 Ch19～22 与 Ch52、
  Ch62。Ch20 已定义 test-time budget 是 accuracy-cost policy、route/budget/stop 属于 serving identity；Ch52 已把
  reasoning budget 纳入 admission/scheduling；Ch62 已要求 evaluation 绑定完整 subject。论文新增的是“budget 内部
  还可由 model-state feedback 双向调节”及其 artifact/feedback failure mode，故为 `Refine — Existing Argument
  (Experimental; Provisional)`。Historical Books Gate 关闭，本轮不修改 Books。
- **Open Questions**：怎样用 independent verifier、calibration curve 与 counterfactual forced stop 区分 low
  confidence 的必要探索和无效摇摆？model/adapter/quantization/prompt revision 后谁触发 vector/control-surface
  invalidation？多租户 serving 中怎样把 latent-control decision 纳入 trace、capacity forecast、fairness 与 rollback？

### Expert Threshold Routing：从 batch 内精确平衡到 population state 的因果近似 — 29/30

- **Candidate / Source Family / coverage**：`ET-POPULATION-CAUSAL-EXPERT-ROUTING`；arXiv:2603.11535 sole
  v1，2026-03-12。已读完整 HTML 的 formal objective、algorithm、training/inference path、全部 experiments、
  related work、future-information proof 与 Appendix B～F 的 architecture、optimizer、hardware、warmup、shared
  expert、normalization、capacity constraints 与 routing-consistency sweep。正文说明 custom PyTorch MoE 与
  all-to-all implementation，但未链接公开 repository/artifact；复现状态 `Implementation Described / Artifact Not
  Disclosed`。论文没有独立 Limitations 或 Threats to Validity 章节。
- **Original Problem / Why Previous Designs Were Reasonable**：Token Choice 每 token 固定 top-G，执行预算
  易预测，但 load balancing 依赖 auxiliary/loss-free controller。Expert Choice 每 expert 在 batch/sequence 中选
  top-k，天然实现 per-batch 完美均衡并允许 token 激活 0～多 experts；大训练 batch 中这很合理。但 autoregressive
  decode 看不到 future tokens，batch composition 也会改变 cutoff，因而训练 selection 不能直接成为 single-token
  causal inference rule。小 batch EC 与 inference surrogate 的 gap 尤其明显。
- **Changed Constraint / Principle**：production decode 要求每个 token 的 route 只依赖当前 logit 与已提交状态，
  同时避免跨请求 batch composition 成为语义输入。ET 将“每个 batch 必须均衡”放宽为“在 training population 上
  期望均衡”，以每 expert 历史 cutoff 的 EMA 近似总体 `(1-1/E)` quantile。**若 batch-relative decision 无法在
  online causal path 复现，可把足够稳定的 population statistic 固化为 versioned routing state；代价是从确定的
  batch load 转为有方差的长期约束。**
- **Mechanism / State Ownership / Flow**：training batch 对每个 expert 计算第 `k=N/E` 大 router logit，并以
  `c_i <- beta*c_i+(1-beta)*kth-largest` 更新 cutoff；train/inference 都以 `r_ti > c_i` 独立 dispatch token。
  cutoff-EMA 是 checkpoint-adjacent causal state，training job/serializer 拥有更新与冻结；router 产生 logits；runtime
  读取 frozen cutoffs 并形成 variable-fanout token→expert edges；capacity manager 拥有 training padding/drop；EP
  runtime 拥有 dispatch/all-to-all/merge；serving scheduler 只看到实际 fanout、queue 与 memory。cutoff 未与
  checkpoint 一起保存、转换或校验时，route semantics 会漂移。Appendix 证明 exact EC top-k 对完整 future sequence
  一般需携带组合级 advice，而固定有限精度 cutoff 只依赖已保存 scalar；这支持 causality distinction，不证明 EMA
  是唯一或 universally optimal approximation。
- **Implementation / Evaluation Contract**：Nanochat d12 为 575M total/195M active，d20 为 2.4B/561M；
  16 routed experts（G=1、E=16）加一个 shared expert，平均激活一个 routed expert，sigmoid gate，first layer dense，
  training capacity factor C=0.5。FineWeb-Edu 上分别训练 10B/11.2B tokens，sequence 2048、batch 524,288 tokens；
  d20 用半 minibatch+2-step accumulation。ET `beta=0.999`，先用 EC 4K steps warmup；EC routing pool 从 2K
  sweep 到 512K，inference 统一用 cutoff surrogate。单机 8× NVIDIA B200 180GB，ZeRO-2-style optimizer sync，
  custom EP all-to-all；报告 validation CE、CORE centered accuracy、cutoff/usage、fanout、specialization、checkpoint
  routing consistency。未披露 wall-clock、MFU、communication volume/overlap、inference latency/throughput、seeds/
  uncertainty、long-context、larger MoE 或 production SLO。
- **What Evidence Proves / Does Not Prove**：在上述两个小中型模型和训练 contract 中，作者结果支持 large-pool
  EC 与 population cutoff 具有相近 loss，ET 避免 inference 依赖 batch top-k，并在作者 CORE/CE 上优于所测 TC
  variants。warmup ablation 明确显示 early cutoff lag 会 starvation；capacity appendix 显示该设置 warmup 后
  saturation/starvation 较低。它不证明“消除”所有 train-inference gap：training 仍有 capacity padding/drop，而
  inference 没有；dynamic fanout 的 tail、cross-domain/tenant distribution shift、cutoff drift、EP imbalance 与
  serving capacity 都未验证。heatmap/specialization 只说明 activation pattern，不证明 expert 获得可解释 domain skill。
- **Trade-offs / New Failure Modes / Previous Designs Still Apply**：ET 以 stable cutoff 和 causal per-token route 换取
  per-batch load variance。新增状态包括每 expert EMA、warmup phase、capacity bounds 与 serialization identity；新增
  failure modes 是 cold-start starvation、distribution drift 后 systematic over/under-routing、zero-routed-expert token、
  burst imbalance/OOM、training drop 与 inference semantic mismatch、不同 worker cutoff version 分叉。fixed top-G
  在严格可预测 compute/latency 时继续成立；aux/loss-free balancing 在不想维护 population quantile 或需平滑 update
  时仍合理；large-batch EC 在 bidirectional/encoder、offline batch 或无需 causal decode 时仍有优势。ET 不是后者的
  单向替代。
- **Evolution / ROADMAP / Adjacent Chapters / Decision**：`Direct Evolution`：Token Choice + auxiliary balance ->
  loss-free bias -> per-batch Expert Choice -> predictor/batch/segment causalization -> population-level per-expert threshold。
  `Layering / Dependency`：router objective -> cutoff state -> executable dispatch -> EP communication -> runtime capacity；
  上游 sparsity 不能自动推出下游加速。主 owner 暂定 Ch21，handoff Ch37/40/46；已读 Ch20～22，并核对 Ch21 的
  top-2、load balance、capacity、EP/all-to-all 与 inference-cost 边界。现稿尚未解释 Expert Choice 的 causality、
  population routing state 与 variable fanout，故为 `Refine — Existing Argument (Experimental; Provisional)`；
  Books Gate 关闭，本轮不改书稿。
- **Open Questions**：cutoff 是否随 checkpoint 保存，continued training/domain shift 时怎样 re-estimate、version 和
  rollback？serving 中 variable fanout 怎样进入 admission、EP placement、capacity guard 与 tail SLO？training
  capacity drop 与 inference uncapped route 的 semantic gap 如何单独测量？多 worker cutoff 版本不一致时怎样检测？

### Spend Less, Reason Better / Budget-Aware Value Tree — 28/30

- **Candidate / Source Family / chronology**：`BAVT-BUDGET-CONDITIONED-VALUE-TREE`；arXiv:2603.12634
  sole v1，2026-03-13 04:10:27 UTC。已读 metadata、Introduction/Related Work、完整 Method/公式/算法、
  convergence proof、两类模型四个 benchmark 的全部主实验、component ablation、cost analysis、prompt/
  hyperparameter Appendix 与 Limitations。论文页未链接作者代码或可冻结 artifact，复现状态为
  `Implementation Described / Public Artifact Not Disclosed`。
- **Original Problem / Why Previous Design Was Reasonable**：parallel sampling、majority vote 与固定-depth
  tree search 在 rollout 相互独立、工具便宜、并行资源充足且 deadline 宽松时简单可靠；固定 token/tool cap
  也提供明确上限。但当调用成本高、路径共享前缀且错误会累积时，它们仍可能把预算平均花在重复或已知死路。
  约束因此从“给更多 test-time compute”变为“在 token 与 tool 两种硬预算内，逐步决定 widen、deepen 还是答题”。
- **Mechanism / State Ownership / Flow**：每个 node 保存 intermediate state、parent/children、累计 value 与剩余
  `(tool calls, output tokens)`；同一 backbone 交替充当 generator 与 prompt critic。critic 不预测绝对正确率，
  而预测本步 residual information delta，再更新 bounded accumulated value。runtime 以
  `r_t=min(remaining-tool ratio, remaining-token ratio)`、`alpha_t=1/r_t` 对 node value 做幂次采样：预算充足时
  分布较平，预算收紧时趋向 greedy。value 达阈值则 answer、child 不优于 parent 则 widen，否则 deepen；发现
  terminal 后对祖先做 children-mean backprop，硬预算耗尽仍从最高值未完成 leaf 强制生成答案。
- **Implementation / Evaluation Contract**：GPT-OSS-20B 与 Qwen3-30B-A3B-Instruct-2507，HotpotQA、
  2WikiMultihopQA、MuSiQue、Bamboogle；唯一工具是在 2018 Wikipedia dump 上以 E5 检索 top-5 passages。
  low/mid/high 分别为 5/10/20 次 tool calls，reasoning model output-token cap 为 2K/4K/8K，instruct model
  为 1K/2K/4K；每次 generation 最多 512 output tokens。Qwen 使用 temperature 0.7、top-p 0.8、top-k 20，
  GPT-OSS 为 1/1/0；指标是 EM/F1。baseline 以相同聚合 tool/output budget 并行采样后 majority vote。
  未披露 hardware、precision、batch、concurrency、seed/variance、wall-clock/TTFT/tail SLO。
- **Ablation / Cost / Theory Boundary**：tree-only 低于 parallel baseline；加入 step value 后恢复，再加入 budget-
  conditioned selection 才进一步改善，说明“树”本身不是收益来源。作者 cost table 使用 input token 单价为 output
  十倍的估算与 2026-03 定价，并非实测系统成本；critic 自身消耗 token/latency。定理在存在可发现 oracle path、
  每步 deterministic positive delta、bounded candidate pool/value/exponent 等强假设下，只保证有限预算内以高概率
  到达 **critic value 达阈值** 的节点；不保证答案正确、critic calibrated，也不证明 low-budget headline 可跨工具、
  模型或 workload 泛化。
- **Trade-offs / Failure Modes / Previous Branch**：budget state 让 exploration/exploitation 随资源变化，但把
  critic bias、自我确认、forced-answer、candidate eviction 与 multi-resource pricing 引入控制面；只取最紧预算比率
  会忽略 tool 价格、latency、可逆性和不同资源间不可线性替换。parallel sampling 在低 latency、大并行或需独立
  diversity 时仍成立；deterministic plan 在不可逆 action、高风险 policy 或 critic 不可信时更合适。关系是
  `Direct Evolution`：flat budget allocation -> step value -> remaining-budget-conditioned search -> cost-aware policy；
  它不是对 parallel branch 的单向替代。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch74～76、Ch62 与 Ch80；主 owner 为 Ch75，handoff
  Ch74/62/80。Ch75 已覆盖 tree search、budget、verifier quality 和 self-evaluation blind spot；新增缺口是把
  `remaining budget` 明确纳入 search state、把 critic overhead 计入同一 contract，并区分“终止性证明”和
  “正确性证明”。暂定 `Refine — Existing Argument (Experimental; Provisional; Historical Books Gate Closed)`，
  本轮不修改 Books，也不保留 4× headline。
- **Open Questions**：多工具异构价格、deadline 与不可逆风险怎样组成不丢信息的 budget state？critic 与 generator
  共享 backbone 时如何用 independent verifier 校准？forced answer、candidate eviction 与 global backprop 怎样记录
  decision trace 并支持 rollback？在 production batching 下，树分支的 KV/state ownership 与 fairness 由谁管理？

### EnterpriseOps-Gym — 28/30

- **Candidate / Source Family / chronology**：`ENTERPRISEOPS-STATEFUL-CONSTRAINT-EVAL`；arXiv:2603.13594
  sole v1，2026-03-13 21:09:39 UTC；官方 `ServiceNow/EnterpriseOps-Gym` repository、dataset/runtime surface。
  已读 32 页全文的 benchmark construction、task QA、sandbox/tools、verifier taxonomy、全部 experiments/
  ablations、failure cases、domain/step appendices 与 discussion，并核对 current repo 的 seed DB、MCP servers、
  ReAct/planner/decomposition runners、scoring 与 60% public split。current leaderboard 和后续模型不是 W11 证据。
- **Original Problem / Why Previous Design Was Reasonable**：static QA、single-tool success 或 end-answer judge 在
  无持久副作用、短 horizon 和低权限环境中足以比较模型；browser benchmark 也常把页面操作当主要难点。企业
  workflow 的约束变化是 database state 会跨调用累积、操作有 permission/process policy、前置 ID/对象必须解析，
  infeasible 请求的正确结果可能是无副作用拒绝，因此“答案看似正确”不再等于系统状态正确。
- **Mechanism / State Ownership / Flow**：1,150 个 expert-curated tasks 横跨八域、164 tables、512 tools；每题从
  SQL snapshot 启动 containerized sandbox，经 MCP/tool calls 改变 state。SME 编写 gold trajectory/human plan 与
  SQL verifiers，分别检查 task outcome、integrity constraint、permission/process compliance 和 side effect；
  unique target state 允许多条 action path。30 个 infeasible tasks 由缺工具、policy violation 或资源不可用构造，
  verifier 同时要求 abstain 与不改变系统。database/environment 拥有事实，tool layer 拥有 mutation contract，
  agent/scaffold 拥有 action trace，verifier suite 拥有 acceptance；LLM judge 只用于 verifier-tagging/定性分析，
  不能提升为 truth owner。
- **Evaluation Contract**：14 个当时模型在相同 instruction/tool/sandbox 下用 ReAct，默认是 **oracle-tool**：完美
  retriever直接提供正确工具集合，故主要测 planning/execution而非 discovery。pass@1 仅当全部 verifier 通过，
  报三次 run 平均；另报 verifier-level pass，但论文明确其会被简单 checks 掩盖。human trajectory 平均约 9.15
  tool steps，按 horizon 分桶；还测试 distractor tools、thinking budget、planner+executor、human-plan+executor、
  decomposition/multi-agent 与 infeasible refusal。paper 未披露统一硬件、完整 API snapshot/decoding参数、token/
  latency/concurrency SLO；API cost 是版本化估算，不是资源等价实验。
- **What Evidence Proves / Does Not Prove**：在该 sandbox/oracle-tool contract 中，结果支持 success 随 horizon
  下降、human plan 对固定 executor 提升 14～35 个百分点、automated planner 对弱模型有较小收益、额外 task
  decomposition 在强 sequential dependency 下可回退，以及 permission/process checks 比简单 outcome 更难。
  它不证明 planning 是所有 Agent 的唯一主瓶颈、不证明小模型有好计划便普遍等价大模型，也不证明 benchmark
  排行榜等于 deployment autonomy；human plan 同时改变 context，oracle tools 移除了 retrieval，SQL verifier
  只覆盖作者编码的 state/policy，current repo leaderboard 还已包含 W11 后的模型与运行版本。
- **Trade-offs / Failure Modes / Evolution**：executable final-state verifier 比 text judge 更强，却会产生 verifier
  coverage、schema snapshot、hidden-test leakage 与 benchmark overfitting；oracle tools隔离 planning，但低估 discovery
  failure；分解可减少单 Agent 认知负担，却破坏共享顺序状态并增加handoff错误。static QA 在无副作用或只测模型
  knowledge 时仍合理。关系为 `Layering / Dependency`：answer score -> executable final state -> integrity/policy/
  side-effect checks -> infeasible refusal -> versioned stateful deployment evaluation。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch62、Ch74～77 与 Ch80；主 owner Ch62，handoff Ch74/75/
  77/80。Ch62 已要求 EvalSpec、executable verifier、final state/side effect、scaffold identity 与 evidence boundary；
  Ch75/77 已覆盖 conditional plan、state transition 与 workflow authority。因此没有新的长期机制缺口，结论是
  `No Change — Already Covered / Experimental Evaluation Case`。保留在 Weekly 作为“oracle-tool仍不能消除
  state/policy failure”和“multi-agent decomposition可能破坏顺序依赖”的实证案例，不改 Books。
- **Open Questions**：如何量化 SQL verifier 未编码的语义/合规漏洞？public 60% split 与 current leaderboard 如何
  防止 test contamination？真实 SaaS concurrency、eventual consistency、auth expiry、partial failure 与 rollback 加入
  后，state identity 怎样扩展？怎样用同一 contract 分离 retrieval、planning、execution 与 policy bottleneck？

### EvoClaw / SWE-Milestone：从独立快照到持续演化状态序列 — 29/30

- **Candidate / Source Family / chronology**：`SWE-MILESTONE-CONTINUOUS-EVOLUTION-EVAL`；arXiv:2603.13428
  v1 于 2026-03-13 03:20:40 UTC 首发，v2/v3/current v4 分别在 06-05、07-10、07-21；v1 名为 EvoClaw，
  current title 为 SWE-Milestone，ICML 2026 status 是后续 revision。已读 v1 完整 HTML 的 DeepCommit、benchmark、
  全部 results/analysis、testbed validation、error-chain/code-quality/human-DAG Appendices，并核对 current
  `DeepCommit-ai/SWE-Milestone` repository、versioned data/image/runtime surface。W11 只归档 v1 event，后续名称、
  benchmark versioning 与 anti-cheat contract 作为 evolution boundary。
- **Original Problem / Why Previous Design Was Reasonable**：SWE-bench 类 independent issue snapshot 在修复可局部
  隔离、canonical base state 可重建时易比较、可并行、能精准回归；release-level generation 又适合测完整 artifact。
  但长期 coding Agent 会在自己的修改上继续开发，早期 abstraction、API 与 regression 成为后续输入。commit 序列
  太细且含噪，release 又太粗，因此需要在 functionally cohesive milestone 与 dependency DAG 上测 persistent state。
- **Mechanism / State Ownership / Flow**：DeepCommit 从 mainline commits、PR/Issue/release、git-blame dependency、
  symbol change 与 file co-change 建 commit DAG；Agent 经 seed discovery、milestone consolidation、dependency inference、
  granularity refinement 产生 milestone DAG，再按 topological order 重建 Docker/test environments。每 milestone 有
  START/END snapshots、F2P/N2P feature tests、P2P regression tests 与 flaky filtering。evaluation planner 只在前置
  milestones 完成后解锁任务；Agent 在 persistent workspace 连续修改，提交 tag 后 watcher 抽取 snapshot 到隔离
  container 异步评分。repository state、DAG/version、test list/image digest、agent session、snapshot 与 evaluator
  revision共同构成 run identity。
- **Evaluation Contract**：v1 为 7 个 repositories、5 languages、98 graded + 3 context-only milestones、124
  dependencies；gold patch 平均改 27.4 files，每 milestone 平均 17.1 F2P 与 6,218 P2P tests。比较 continuous 与
  canonical-snapshot independent mode；Recall 衡量新增功能 test，Precision 衡量 fixed tests 相对 broken P2P，二者
  harmonic mean 为 Score，另报 all-F2P/P2P Resolve Rate、cost、output tokens、time、turns。15 个 agent-model
  configurations 横跨四种 harness；不同框架有不同 context/resume/iteration contract，因此排行榜不能当纯模型能力。
- **What Evidence Proves / Does Not Prove**：作者数据支持：在这七条作者重建的 release itineraries 中，continuous
  mode 明显低于 independent；后续 DAG layer/order 与 score 负相关；Recall 可继续增长而 Precision saturation，
  inherited/missing execution errors在后期上升；过少验证与 blind edit thrashing相关。它不证明“技术债是唯一因果”：
  milestone/SRS 用 ground-truth patch 反向构造，DeepCommit 只收集 87.1% tests，LLM reviewer 才判 root-cause intent，
  current v1 还有 post-event models/scaffolds，且 7 repositories 不能代表 branch/merge、真实需求变更、human review、
  security/operability 或 organization-specific conventions。
- **Trade-offs / Failure Modes / Evolution**：persistent evaluation 暴露 error propagation，却降低 trial independence、
  放大早期随机性并提高成本；DAG 重排恢复 functional dependency，却可能偏离真实 chronology/social intent；未来 tests
  提供稳定 oracle，也可能 reward 针对 hidden target 的 reconstruction。independent snapshot 在 release regression、
  root-cause isolation 与资源受限时仍成立。关系为 `Direct Evolution`：single issue snapshot -> milestone artifact ->
  dependency-gated persistent sequence -> error-chain/recovery evidence；不是用 continuous benchmark 覆盖 snapshot。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch62、Ch77、Ch80。Ch62 已完整写出 snapshot -> interactive ->
  evolving state sequence、`state/action/test evidence`、technical debt、rollback、harness revision 与不能取代 snapshot 的
  边界；Ch77/80 已保存 durable state、retry/recovery、run identity 和 evidence graph。因此结论为 `No Change —
  Already Covered / Experimental Evaluation Case`，只在 Weekly 保存这项强实证，不重复写 Books。current title、
  4.6/5.3 等后续版本化结果也不倒写入 W11 knowledge claim。
- **Open Questions**：怎样以 multiple seeds 或 counterfactual clean-base replay 分离 error propagation 与 stochastic
  run noise？milestone graph 与 real branch/merge/human review 的偏差如何量化？未收集 tests、structural quality、
  performance/security regression 怎样进入 verifier？current benchmark/data/image/harness revision怎样保持跨时间可比？

### TERMINATOR — Unverified / Blocked Full Text

- **Verified identity / artifact surface**：arXiv:2603.12529 v1 于 2026-03-13 00:07:18 UTC，current v2 为
  2026-05-14；title、authors、revision、official project 与 Qwen3-8B/14B model artifacts 已核验。项目页说明
  single transformer layer + FFN 读取 base LRM final hidden state，逐 token预测 final answer是否已首次出现；training
  用 separate LRM定位 first-answer token 后构造 0/1 labels，online 以 default threshold 0.7、window 10、majority
  触发 end-of-thought。项目还披露 MATH-500、batch 1、single GH200 的 latency/throughput条件。
- **Access boundary / decision**：arXiv 没有 HTML；13MB official PDF 在 research full-text入口返回不可读，当前只可
  访问 abstract、project summary 与 artifact packaging。尚未核验 paper 的 label-extractor prompt/error audit、training
  data规模与 leakage、loss/optimizer/hardware、完整 baselines、threshold/window ablation、false-positive/negative、
  per-task variance、limitations 与 Appendix。项目 headline和 v2新增 latency不能替代 v1全文，也不能与同周
  ReBalance 合并推断。故不评分、不生成 Full Source Review、不进入 Books，标记 `Unverified / Blocked Full Text`
  后按 blocked-skip 规则继续；取得 PDF text 后优先检查 Ch20/52/62。

### GradMem：把 context write 从一次 forward 变成可优化的模型级状态 — 28/30

- **Candidate / Source Family / chronology**：`GRADMEM-TEST-TIME-OPTIMIZED-CONTEXT-STATE`；
  arXiv:2603.13875 sole v1 于 2026-03-14 首发，官方 `yurakuratov/gradmem` repository 提供训练、数据处理、
  experiment scripts 与 attention double-backward 实现。已读完整 HTML 的 Metadata、Introduction、WRITE/READ
  formulation、baselines、全部 experiments、Discussion 与 Appendices A～I，并核对官方实现；repository 当前的
  ICML 2026 标签是后续 publication state，不倒写成 W11 已知 peer-review evidence。
- **Original Problem / Why Previous Design Was Reasonable**：完整 Attention/KV cache 保存逐 token 可寻址历史，
  在一次读取、精确引用或 context 不复用时最直接；RMT/SSM 等 forward-only writer 则以一次前向计算换取固定状态，
  避免每个 context 做优化。约束变化是同一长 context 要被多次查询，同时希望 memory state 小于原序列且不改 base
  model weights；一次性 writer 又没有 per-example error signal 来发现或修正压缩错误。
- **Mechanism / State Ownership / Flow**：每个 context 从共享、meta-learned memory initialization
  `M0` 复制出 `m x d` prefix vectors。WRITE 阶段冻结 base model，只对本样本 memory 做 `K` 次 gradient descent，
  以 context token reconstruction loss 更新 `M`；READ 阶段彻底移除原 context，只输入优化后的 memory 与 query。
  outer loop 用 downstream task loss 反传穿过 WRITE steps，联合训练 base model 与 `M0`，因此 strongest setting 需要
  second-order differentiation。model/training artifact 拥有共享初始化与 write rule，request/session runtime 拥有
  per-context mutable memory，query path 只读该 state；它不是 Agent durable memory，也不自动具备 provenance、
  authorization、delete 或跨版本迁移语义。
- **Implementation / Evaluation Contract**：主 synthetic KV retrieval 使用 4-layer、hidden-128、4-head Llama，
  8 memory tokens、1～5 WRITE steps；自然语言实验使用 GPT-2 124M、Pythia 160M、Mamba 130M，覆盖 bAbI
  QA1～5、只保留 answer sentence 的 Short SQuAD，以及 WikiText-103 的 128-token WRITE + 128-token READ。
  比较 full-context Transformer、Mamba、RMT、ARMT 与 TTT-style layers，主要结果报 3-run mean/std；Appendix
  另给 memory-size/K/context-size、无 second-order meta-learning、state-matched Mamba、Llama-3.2 1B/3B short-text
  reconstruction。为支持二阶梯度，作者实现 analytical/recompute/HVP/flash double-backward；其 A100 性能点绑定
  GPT-2、8 memory tokens、query 24、K=1、batch 16，不能外推生产 serving。
- **What Evidence Proves / Does Not Prove**：在作者的 context-removal contract 中，实验支持 gradient-driven WRITE
  可在相同少量 prefix state 下优于一次 forward write，增加 `K` 能在部分任务中用更多 write compute 换取更高
  storage fidelity，且 meta-learning 对该机制成立关键。它不证明固定大小 state 可无损承载任意长 context：Appendix
  明确 context 增大仍需更多 memory，bAbI 的 K 收益不稳定，WikiText 上 ARMT 领先，Short SQuAD 删掉了 distractor，
  大模型只测 32-token reconstruction。没有生产级 concurrency、TTFT/TPOT、checkpoint/migration、quantization、
  multi-tenant isolation 或 end-to-end retrieval QA 证据。
- **Trade-offs / Failure Modes / Evolution**：这条路线以更贵的 WRITE 换更短的 repeated READ；只有同一 context
  查询次数超过 break-even、`|C| >> |M|` 且 write state 可安全复用时才可能划算。它新增 second-order training
  memory、kernel compatibility、inner-loop instability、per-context state lifecycle、错误压缩与 model-revision
  invalidation；一次性 forward writer 在低复用/低延迟写入时仍合理，KV 在精确 provenance 与单次读取时仍合理。
  关系为 `Direct Evolution`：full token history -> forward-only compressed state -> loss-driven iterative WRITE；与
  Titans/TTT 是 `Layering / Design Branch`，区别在 model-level prefix、whole-context update 与显式 WRITE/READ phase。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch22、Ch39、Ch73。Ch22 已覆盖 KV、RAG、test-time neural
  memory 以及 internal state 与 Agent durable memory 的边界，但当前论证仍偏向 per-token/chunk online update，缺少
  “显式 context write 可用 per-example loss 迭代纠错，并按 reuse count 摊销”的分支。故暂定
  `Refine — Existing Argument / Ch22 Experimental`；Ch39 只需 handoff 到 prefill/write amortization，Ch73 只保留
  owner boundary。Historical Books Gate 关闭，本轮不修改 Books。
- **Open Questions**：在真实长文档、多 query 与 paged serving 中，break-even 如何同时绑定 WRITE latency、memory
  allocation、batching 与 SLO？压缩 state 如何携带 citation/provenance、支持 partial update、eviction、checkpoint、
  model revision invalidation 与 tenant isolation？first-order/implicit meta-gradient 能否保留质量并恢复标准高性能
  attention kernel？

### SFT versus RL：19/30 的 secondary synthesis boundary

- **Identity / coverage**：arXiv:2603.13985 sole v1 于 2026-03-14 首发。已读完整综述的 SFT/RL background、
  objective comparison、hybrid methods、QA/math/agent/code application review、takeaways、future work、paper-search
  methodology、hardware appendix 与 AI-assistant disclosure。它没有作者提出的新训练算法、system artifact 或独立
  controlled experiment；证据主要来自 2023～2025 文献综合。
- **Useful synthesis / limits**：文章把 offline demonstration likelihood、on-policy reward optimization、reference
  KL 与 hybrid loss 放进一个比较框架，并强调 SFT 与 RL 可以互补；但“统一为 RL objective”是引用既有工作后的
  表述，不是本论文的新证明。应用趋势使用 benchmark-name keyword counting，2025 年全年数量由上半年近似翻倍，
  会受 keyword threshold、重名、跨域重复与召回损失影响。硬件附录明确是 community heuristic，其每参数 VRAM 与
  1.5～3x 数字缺少统一模型、batch、rollout、optimizer、parallelism 与 SLO contract，不能进入 Books。
- **ROADMAP / decision**：Ch25 已从 behavior cloning/data contract 解释 SFT，Ch29 已从 on-policy distribution、
  verifier/reward 与 policy lag 解释 reasoning RL；本综述没有新增长期机制，也不能替代其引用的 primary papers。
  评分 19/30（TN2/SI3/PV4/SR3/PR4/L3），结论为 `Weekly Only — Secondary Synthesis / No Books Change`。
  它可作为 source index，但未来若某个 hybrid objective 值得吸收，必须回到对应 primary paper，而不是引用本综述
  外推。

### AI Can Learn Scientific Taste：Community Feedback 是可扩展代理，不是科学真理 — 27/30

- **Candidate / Source Family / chronology**：`RLCF-CITATION-PREFERENCE-SCIENTIFIC-IDEATION`；
  arXiv:2603.14473 v1 于 2026-03-15 首发，v2 于 07-15；W11 归档只使用 v1 的数据与实验合同，v2
  只用于核对 revision boundary。已读 v1 的 formulation、RLCF、SciJudge/SciThinker、全部 evaluation、
  training/data appendices、limitations 与 case studies，并核对官方 `tongjingqi/AI-Can-Learn-Scientific-Taste`
  artifact surface。
- **Original Problem / Why Previous Design Was Reasonable**：专家逐对判断论文或研究想法质量，标签更贴近
  rubric，却昂贵、稀疏且难以覆盖百万级文献；citation count 可从社区历史中大规模取得，并包含长期采用
  信号。约束变化是系统希望把这种延迟、群体产生的反馈变成可优化 preference，而不是只做静态 bibliometrics。
- **Mechanism / State Ownership / Flow**：论文从 290 万 arXiv metadata 中取得 230 万 citation records，以
  2024 年及以前的 210 万篇论文为 training pool；在同 field/subcategory 和相近时间内构造高低引用 pair，
  要求绝对差至少 8、相对差至少 30%，形成 696,758 pairs。Scientific Judge 用 GRPO 学习 pairwise judgement；
  Scientific Thinker 再对同一 seed paper 采样一组 ideas，由 Judge 两两比较产生 group-relative reward 并优化
  policy。bibliographic snapshot 拥有 citation/field/time 标签，pair builder 拥有 selection policy，Judge
  checkpoint 拥有 learned proxy，Thinker rollout 拥有候选；这些角色都不拥有“科学真理”。
- **Implementation / Evaluation Contract**：Judge 覆盖 Qwen2.5 1.5B～32B、Qwen3 4B/30B 与 Llama-3.1-8B，
  论文按模型规模报告 32/64/128 张 H200-equivalent GPU 的训练配置，并用 position swap 检查顺序一致性。
  Thinker 用 2025 年 1～7 月 4,000 篇高引用 seed 训练，以同期 200 篇和 8～12 月 200 篇测试；Qwen3
  30B-A3B/4B policy 使用 Qwen3-4B Judge，GRPO batch 128、每 prompt 8 generations、max completion 8192。
  idea quality 由三个强 LLM 对“潜在影响”多数票判断；不是未来 citation、实验可行性或结果复现。
- **What Evidence Proves / Does Not Prove**：在作者构造的 field/time-matched citation preference 上，数据量和
  模型规模与 pair accuracy 同向，held-out year/field、peer-review/Altmetric controls 提供 proxy transfer
  evidence；用该 Judge 训练的 policy 也更容易赢得同类 LLM evaluator 的 potential-impact preference。
  这些结果不证明模型学到完整“scientific taste”，更不证明 ideas 正确、可执行或最终有影响。citation 同时受
  venue、机构、作者网络、可见度、领域规模、年龄与时尚影响；matching/controls 只能削弱部分混杂。reward 与
  evaluation 都围绕相近 proxy 时，还会放大 Goodhart 与 evaluator correlation。
- **Trade-offs / Failure Modes / Evolution**：Community Feedback 把稀缺专家标签扩展为大规模延迟信号，却把
  popularity、历史偏差和 feedback loop 带进 objective；模型生成更“可引用”的方向可能挤压新颖、长期或负结果。
  专家 rubric 在高风险选题/实验决策中仍成立，citation proxy 更适合作为一个 feature 或 weak prior。关系为
  `Principle Reuse`：human preference -> scalable AI/verifier preference -> delayed community proxy；新来源不改变
  reward 只是目标代理这一事实。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch27、Ch62、Ch77。Ch27 已明确 pair label 属于特定群体、
  时间与 policy，不是客观真理，并要求保存 feedback population/rubric/version 与防止 reward hacking；Ch62
  已区分 proxy、judge 与 executable evidence；Ch77 已要求 scientific workflow 的实验/authority gate。故结论为
  `No Change — Already Covered / Ch27 Experimental Feedback Case`，只保留为“延迟社区信号仍需 proxy
  governance”的强案例，不重复写 Books。
- **Open Questions**：怎样以 long-horizon prospective evaluation 区分真正 durable impact 与短期 attention？
  citation-producing community 已受推荐/生成模型影响后，pair distribution 如何防止自增强？怎样把 feasibility、
  falsifiability、diversity、negative-result value 与安全约束加入多目标 evaluation，而不压成不可审计单分数？

### AgentProcessBench：过程评估必须区分探索、错误与级联后果 — 28/30

- **Candidate / Source Family / chronology**：`AGENT-PROCESS-TERNARY-FIRST-ERROR-EVAL`；arXiv:2603.14465
  v1 于 2026-03-15 首发，v2 于 06-01。已读 v1 全文的 benchmark protocol、annotation、metrics、20-model
  evaluation、Best-of-N、limitations 与 qualitative appendices，并核对 official `RUCBM/AgentProcessBench`
  repository/data surface。v2 新增的 error-propagation ablation、training 和 anchoring audit 只记作后续 revision，
  不倒写成 W11 已完成实验。
- **Original Problem / Why Previous Design Was Reasonable**：final outcome 在短链、可回滚、单一 verifier 的任务中
  成本低且直接；数学 PRM 的 binary step correctness 也适合封闭推导。tool Agent 面对动态 observation、必要探索、
  policy 与不可逆副作用后，最终失败无法定位 credit，binary label 又会把无收益但合理的信息收集误判为错误。
- **Mechanism / State Ownership / Flow**：benchmark 从 HotPotQA、GAIA、BFCL 与 tau2-Bench 各采 50 个 task，
  由五个 policy family 生成 1,000 trajectories、8,509 assistant actions。两名训练合格的 annotator 独立标注
  `+1 correct/effective`、`0 neutral/exploratory`、`-1 incorrect/harmful`，分歧经讨论 adjudicate；一旦错误发生，
  依赖该错误的后续步骤持续记 -1，直到显式修复或切换到独立 subtask。environment/tool observation 拥有事实，
  trajectory 拥有 action chronology，human rubric/adjudication 拥有 reference label；PRM prediction 不是 truth。
- **Evaluation Contract**：StepAcc micro-average 全部 steps，因此长 trajectory 权重更高；FirstErrAcc 对每条
  trajectory 比较首个 -1 的位置，两边都无 -1 才算匹配，从而减弱长度和级联标签影响。作者评测 20 个当时模型，
  并用 outcome/process score 做 Best-of-N。论文报告 89.1% step agreement、Cohen kappa 0.767，但没有训练/推理
  hardware、latency、cost、并发或 deployment SLO；human reference 还看了 official solution 和三个 LLM suggestions。
- **What Evidence Proves / Does Not Prove**：在这四个 task/environment 与该 rubric 下，弱 policy 可因早停获得较高
  correct-step ratio；PRM 常偏正类且难区分 neutral 与 error；StepAcc 与 FirstErrAcc 相关但后者更难；process score
  可作为 outcome selector 的补充。它不证明 ternary taxonomy 覆盖所有 tool actions，也不证明 error-propagation
  labels 是客观因果：annotation 会把对早期错误的依赖判断编码进 truth，FirstErrAcc 也不区分“位置相同但错误类型
  不同”。Best-of-N 是作者 sample/generator/judge contract，不是 production reward gain。
- **Trade-offs / Failure Modes / Evolution**：dense labels改善 credit localization，却增加人工成本、主观性和
  environment-version依赖；neutral 类保护必要探索，也可能掩盖浪费和风险；propagation rule统一级联监督，却可能
  惩罚后续局部正确动作。final outcome 在便宜、可执行和无副作用任务中仍合理。关系为 `Direct Evolution`：
  outcome-only -> binary process correctness -> typed process state + causal dependency -> first-error/repair boundary。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch62、Ch76 与邻接 workflow 内容。Ch76 已拥有“最早有证据的
  critical step -> root cause -> repair boundary”，但 Ch62 还缺评测层的 neutral exploration、级联标签与长度偏差
  分解。故暂定 `Refine — Existing Argument / Ch62 Experimental`；未来只吸收 typed step evidence 与 metric
  trade-off，不复制 benchmark 排名。Historical Books Gate 关闭，本轮不修改 Books。
- **Open Questions**：如何让 error propagation 同时表达 multiple causes、partial recovery 与 independent downstream
  correctness？neutral 是否应再按 information gain、cost、risk 和 reversibility 分型？怎样以 environment replay、
  state diff 与 human causal audit 联合构造更强 reference，而不是只对自然语言轨迹达成一致？

### V-JEPA 2.1：目标覆盖范围决定局部细节能否进入最终表示 — 27/30

- **Candidate / Source Family / chronology**：`VJEPA21-DENSE-PREDICTION-DEEP-SELF-SUPERVISION`；
  arXiv:2603.14482 v1 于 2026-03-15 首发，v2/v3 分别于 03-17、06-11。已读 v1 的 objective、architecture、
  pretraining/distillation、全部 downstream protocols、ablation、future work 与 appendices，并核对 official
  `facebookresearch/vjepa2` code/checkpoint surface；W11 不使用 v2/v3 新增内容作为首发证据。
- **Original Problem / Why Previous Design Was Reasonable**：V-JEPA 2 的 masked latent prediction 只要求从 visible
  context 预测 masked targets；visible tokens 可成为全局 aggregator，因此对分类、action anticipation 与全局语义
  合理，却没有直接压力让每个 token 保留可定位的空间/时间细节。约束变化是同一个 frozen encoder 还要服务 depth、
  segmentation、tracking 与细粒度 physical state。
- **Mechanism / State Ownership / Flow**：V-JEPA 2.1 把 prediction loss 扩展到 masked 与 visible tokens，并以
  weighted-context schedule 避免可见 patch 的 trivial copy；modality-specific 2D image / 3D video tokenizer 把不同
  输入送入共享 encoder。Dense loss 强化 local grounding 后会损害部分 global classification，Deep Self-Supervision
  再从多个 intermediate encoder layers 建 targets/predictors，使局部信息进入最终层并恢复全局能力。pretraining
  objective 拥有“保留什么”的压力，encoder activation 拥有 representation，downstream probe 只测可访问性，
  不能证明部署任务实际使用该 feature。
- **Implementation / Evaluation Contract**：作者在 VisionMix 163M image/video pool 上扩展 300M～2B ViT，使用
  high-resolution cooldown，并从 frozen teacher distill 80M/300M/1B student。ablation 从 ViT-L 比较 context loss、
  deep supervision、dataset/tokenizer/scale；dense tasks使用 linear head或 non-parametric propagation，classification
  使用四层 attentive probe，robot planning另训相同 300M action-conditioned predictor，在 DROID/单 A100 contract
  下评十个 task。pretraining hardware/总 compute、统一 latency/concurrency/SLO 没有披露；不同任务 probe 与
  hyperparameter search 不可直接视为同一 end-to-end system comparison。
- **What Evidence Proves / Does Not Prove**：核心消融支持 context loss 改善 ADE20K/NYU 等 dense probes、同时压低
  SSv2/global performance，deep self-supervision 能恢复并进一步改善多项 probe；last-layer 与 multi-layer probe
  对比也支持信息被推向最终层。它证明的是作者数据、架构与 probe contract 下的 representation accessibility，
  不证明 learned feature 是完整物理 state、线性可读即被 world model 因果使用，也不证明 robot planning gain
  来自 backbone 单一因素。PCA 可视化只是观察证据。
- **Trade-offs / Failure Modes / Evolution**：从 masked-only 到 dense objective 增加 local fidelity，却引入 trivial
  copying、训练算力、auxiliary predictor 和 global/local objective conflict；deep supervision 缓解冲突，但会增加
  loss weighting、layer coupling 与调参 surface。旧 masked objective 在只需全局语义、成本受限时仍成立，多层 probe
  也仍可在不重训 backbone 时读取 intermediate state。关系为 `Direct Evolution`：global masked latent prediction
  -> all-token local grounding -> intermediate-layer auxiliary objectives -> shared image/video representation；不是
  新目标单向淘汰旧目标。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch4～6 与 Ch5 owner。Ch5 已说明 loss 决定表示保留/丢弃、
  invariance 过强会丢细节，但还缺“目标只覆盖部分 tokens 时，未受约束的 token 可转成全局 aggregator；辅助层级
  objective 可改变最终层可访问性”的机制链。故暂定 `Refine — Existing Argument / Ch5 Experimental`；Ch23
  只需 handoff 到 data mixture，未来 world-model 章节再处理 action-conditioned dynamics。Historical Books Gate
  关闭，本轮不修改 Books。
- **Open Questions**：如何用 intervention 而非 probe 区分“信息可读”与“下游确实使用”？dense/global objectives
  在不同数据与分辨率下如何自适应加权？tokenizer、dataset mix、scale 与 loss 各自贡献能否在统一 compute budget
  下分离？预训练 compute、energy 与 downstream latency 未披露时，平台如何判断总成本 break-even？

### KServe v0.17.0：从通用模型服务对象到 LLM 专用声明式拓扑 — 27/30

- **Candidate / Source Family / chronology**：`KSERVE-LLMISVC-DUAL-TRACK-CONTROL-PLANE`；官方 v0.17.0
  release/tag 与发布长文均为 2026-03-13。已联合阅读 release notes、0.17 versioned architecture、
  LLMInferenceService overview/quickstart/upgrade guide，以及 EPP、PD、parallelism、WVA、chart split 相关
  release/PR surface。后续 0.17.1/0.18 只作为修复与演进边界，不倒写为 v0.17.0 已知行为。
- **Original Problem / Why Previous Design Was Reasonable**：`InferenceService` + `ServingRuntime` 适合 predictive
  model、单 workload template 与普通 route，抽象稳定且不会让所有用户承担 LLM complexity。模型跨多节点、
  Prefill/Decode 分池、请求选择依赖 KV/queue、MoE 需要 DP/EP、扩缩指标变成 queue/KV/token 后，一个通用 CRD
  要么暴露大量互斥字段，要么丢失 topology semantics。
- **Mechanism / State Ownership / Flow**：v0.17 将 `LLMInferenceService` 提升为独立 GenAI serving contract：
  model/workload/router/parallelism specs 由 controller reconcile 成 Deployment/LeaderWorkerSet、Service、Gateway/
  HTTPRoute、InferencePool/InferenceModel 与 EPP；single-node/decode、worker group 与 prefill pool 分属不同 workload
  fields。EPP 从 model server 的 block stored/removed events 建 `{model, block hash} -> endpoint/tier` 索引，并把
  prefix-cache scorer 与 load scorer组合选择 endpoint；PD path 由 NIXL/RDMA connector 传 KV data。CRD/controller
  拥有 desired topology，Gateway/EPP 拥有 request endpoint decision，engine 拥有 token/KV execution，connector
  拥有 transfer completion；event visibility 不是 KV bytes 已可读。
- **Implementation / Operations Contract**：版本同时提供 TP/DP/data-local/EP、Envoy AI Gateway token-cost metadata、
  WVA 以 queue/KV utilization 产生 desired replicas、scheduler HA、admission validation 与 composable configs。
  安装面把 core KServe、llmisvc、localmodel 及 CRD/resource/runtime-config charts 拆开；从 0.16 不能简单 `helm
  upgrade`，说明 API modularity 同时扩大 migration/version matrix。官方 release 没有统一 model/hardware/precision/
  prompt-output/concurrency/SLO benchmark，因此“production-ready”只作 maintainer release status，不作性能事实。
- **What Evidence Proves / Does Not Prove**：release、versioned docs 与具体 PR 共同证明 v0.17 已公开这些 CRD、
  controller、安装和 integration surfaces；它不证明任意 workload 用 KV routing/PD/WVA 都更快、更省或更可靠，
  也不证明所有 backend 对 state transfer/readiness/failure semantics 一致。配置示例是可表达性证据，不是容量规划；
  EPP 索引仍受 event freshness、hash identity、tenant boundary 与 fallback 影响。
- **Trade-offs / Failure Modes / Evolution**：专用 CRD使 workload semantics、ownership 与 validation 更清楚，却
  引入更多 controllers/CRDs/dependencies、升级迁移与跨组件 readiness。普通 `InferenceService` 在 predictive、
  小模型或简单单节点 serving 中仍是较小故障面的正确选择。关系为 `Direct Evolution + Layering`：generic
  service lifecycle -> LLM-specific topology API -> state-aware request control -> runtime execution；不是用新 CRD
  替代通用模型服务。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch48～49、Ch51～53、Ch57～59。Ch49 已完整拥有
  LLMInferenceService topology、EPP/KV event-vs-data、multi-node、PD、readiness 与 failure；Ch57 已拥有
  InferenceService/LLMInferenceService 双轨、通用 lifecycle 和 upgrade-bound version boundary，且现稿基于更后的
  0.18 primary docs。因此结论为 `No Change — Already Covered / Ch49+57 Versioned Evolution Case`。v0.17
  留在 Weekly 作为从 experimental capability 到公开 release contract 的时间线节点，不重复复制功能表进 Books。
- **Open Questions**：多 controller/CRD 的 readiness 怎样合成一个不会过早 route 的 service condition？EPP event
  lag、KV transfer failure 与 scale-down drain 如何进入统一 decision trace？chart/CRD/controller/backend 版本矩阵
  怎样预检并支持 rollback？WVA 的 variant cost 与 queue/KV signal 如何绑定实测 SLO 而不是静态权重？

### Safe Web Agent Learning — Unverified / Blocked Identity

- **Identity check**：对 2026-03-10～03-11 的 Hugging Face discovery index、arXiv exact-title/keyword surface
  与现有 W12 spillback ledger 做了交叉检索，无法把该 intake label 唯一解析为论文标题、arXiv ID、官方
  project 或 repository。相似的 safe web-agent 论文不能在没有唯一标识时被替代认领。
- **Decision**：未评分，不创建 Full Source Review，不进入 Books。按用户确认的 blocked-skip 规则记录为
  `Unverified / Blocked Identity`，留待取得原标题、URL、作者或唯一 ID 后回补；该项不再阻塞后续 W11 候选。

### HomeSafe-Bench — Unverified / Blocked Full Text

- **Identity check**：arXiv:2603.11975 v1 于 2026-03-12 首发，v2 于 03-13；标题、作者、438-case/六类家庭
  场景的摘要级范围，以及 FastBrain/SlowBrain 异步 HD-Guard 声明已核验。
- **Access boundary / decision**：arXiv 未生成 HTML，43MB 官方 PDF 超出 research text入口；随后按 Browser
  skill 尝试读取官方 PDF，但用户保存的浏览器权限明确阻止 arXiv 访问。未读 Method、annotation、hardware、
  streaming latency contract、ablation、Limitations 与 Appendix，故不评分、不生成 Full Source Review、不进入
  Books；标记 `Unverified / Blocked Full Text` 后按 blocked-skip 规则继续。

### Think While Watching — Unverified / Blocked Full Text

- **Identity / artifact check**：arXiv:2603.11896 只有 2026-03-12 v1；official repository 当前仅公开 inference
  code、Qwen3-VL streaming wrapper、segment/timestamp sample 与 CUDA>=12.1 dependency，README 明确 training
  code 尚待发布。摘要声明 segment-level memory、streaming causal mask/position encoding、watch/think overlap，
  但这些不是足以替代正文的证据。
- **Access boundary / decision**：arXiv 未生成 HTML，16MB 官方 PDF 超出 research text入口，Browser 又被同一
  用户权限阻止访问 arXiv。未核验三阶段 data、stage-matched training、attention backend selector、hardware、
  latency/output-token baseline、ablation、Limitations 与 Appendix，故不评分、不生成 Full Source Review、不
  进入 Books；标记 `Unverified / Blocked Full Text` 后继续。

### Groundsource — 22/30（Unverified / Blocked）

- **Source family / verified surface**：`GROUNDSOURCE-NEWS-WEAK-LABEL-DATA`；EarthArXiv v1 metadata 显示
  论文 2026-03-10 公开，Google Research technical article 于 2026-03-12 发布；同时核验 Zenodo dataset
  record。EarthArXiv download 受 JavaScript/bot 校验阻断，浏览器访问又被用户侧权限拒绝，因此本轮没有
  完成 paper method/evaluation/appendix 全文覆盖。
- **Verified facts only**：官方材料说明 pipeline 从 500 万以上新闻中筛选实际洪水报告，读取约 80 种
  语言并翻译，使用 Gemini 分类实际/历史事件、解析相对时间与细粒度地点，再以 Maps geocode；开放数据
  含约 260 万事件、覆盖 150 多个国家。官方人工验证报告 60% 同时满足精确地点和时间、82% 达到其
  “practically useful” 标准，并与 GDACS 严重事件做 recall 对齐。
- **Boundary / unresolved**：这些数字仍是作者/厂商定义的 operating point；未阅读全文前，无法核实
  sampling frame、deduplication、negative set、inter-annotator protocol、地域/媒体/语言/年代 coverage
  bias、precision/recall denominator、polygon/date uncertainty、label lineage 与 downstream leakage。
  新闻记录是 observation proxy，不是传感器 ground truth；“用于 forecast”也不证明 dataset 单独造成
  downstream improvement。
- **Decision**：保持 `Unverified / Blocked`，旧 `Weekly Only` 和任何 Books 结论均作废。待用户允许
  EarthArXiv 浏览器访问或提供 PDF 后，必须全文复核再关闭该 family 的 Archive evidence gap；目前不得进入
  Books。它不撤销其他 54 个 scored candidates 已通过的 W11 Source-Family Books Gate。

## Repository Changes

- 在 Discovery / Source Review 阶段，W11 scored Discovery Recall 从 2 项扩展到 55 项，并把 W12 的 28 个 intake 拆成 candidate-level
  queue；52 个 `20+` Full Source Review 与 2 个低分核验已完成，Groundsource 明确为 blocked；Safe Web
  Agent Learning 因 identity 无法唯一解析保持未评分 blocked；HomeSafe-Bench 与 Think While Watching 因
  无 HTML 且官方 PDF 被浏览器权限阻止而保持未评分 blocked-full-text；TERMINATOR 因无 HTML 且 official
  PDF research text入口不可读保持未评分 blocked-full-text；ordinary pending 已清零。RAGEN-2 已按官方
  3 月 12 日 release 从 W15 回拨；EvoScientist 已完成全文、
  later artifact 与 Ch73/77/62/76 去重，结论为 `No Change / Experimental Case`；MEMO 已完成 current-v2、
  v1/v2 history、官方代码与 Ch73/62/77/78 邻接审计，暂定 Ch73 Experimental refine；Reasoning as Compression
  与 Deep Tabular Research 已完成全文、revision、实验/附录和 Ch28～30、Ch73～77/62 邻接审计，分别暂定
  Ch29 与 Ch75 Experimental refine；FinToolBench 完成全文/Appendix、公开 artifact 与 Ch62/68/74 去重，结论为
  `No Change / Experimental Evaluation Case`；LookaheadKV 已完成 sole-v1、官方实现、效率合同和 Ch39/41/50
  邻接审计，暂定 Ch41 Experimental refine；UCIP 已完成 v1/current-v4、公开结果 artifact 与 Ch62/68 邻接
  审计，因 synthetic-domain、scaling 与 adversarial failure 保持 `No Change / Experimental Evaluation Case`；
  One-Eval 已完成 sole-v1、官方 repository、planning evaluation contract 与 Ch61～63/76～78 邻接审计，
  结论为 Ch62 `No Change / Experimental System Case`；LMEB 已完成 v1/current-v6、22-dataset/193-task
  evaluation contract、official benchmark artifact 与 Ch71～73/61～62 审计，暂定 Ch73 Experimental refine；
  Video Streaming Thinking 已完成 v1/current-v2、SFT/RL/data/latency contract、official artifact 与 Ch71～73/
  62/Part IV 邻接审计，暂定 Ch71 Experimental integrate；daVinci-Env / OpenSWE 完成 environment builder、
  fail/pass oracle、distributed construction、trajectory curation 与 Ch22～24/56/62/77 审计，暂定 Ch23
  Experimental refine；MM-CondChain 完成 VPIR、paired-path、evaluation/ablation 与 Ch61～63/74～77 审计，
  暂定 Ch62 Experimental refine；ReBalance 完成 confidence/variance proxy、latent steering、control surface、
  efficiency/ablation 与 Ch19～22/52/62 审计，暂定 Ch20 Experimental refine；Expert Threshold Routing 完成
  population cutoff、causality proof、warmup/capacity/EP contract 与 Ch20～22/37/40/46 审计，暂定 Ch21
  Experimental refine；BAVT 完成剩余预算 state、residual critic、tree selection、termination-proof boundary、
  cost/ablation 与 Ch74～76/62/80 审计，暂定 Ch75 Experimental refine；EnterpriseOps-Gym 完成 32 页论文、
  official sandbox/artifact、oracle-tool evaluation、SQL verifier、planning/decomposition/infeasible-task ablation 与
  Ch62/74～77/80 审计，结论为 `No Change / Experimental Evaluation Case`；FineRMoE 已转入 2025 backlog；
  EvoClaw / SWE-Milestone 完成 v1/current revision、DeepCommit/Milestone DAG、continuous-vs-independent、
  F2P/P2P、error-chain 与 current artifact audit，并确认现有 Ch62 已完整覆盖，结论为 `No Change /
  Experimental Evaluation Case`；GradMem 完成 sole-v1、全部 Appendices、official implementation、WRITE/READ
  state、double-backward、break-even 与 Ch22/39/73 邻接审计，暂定 Ch22 Experimental refine；SFT versus RL
  完成全文与方法边界核验后以 19/30 留在 Weekly，不能以二手综合替代 primary papers；Scientific Taste、
  AgentProcessBench 与 V-JEPA 2.1 已完成 v1/current revision、全文/Appendix、artifact 与章节邻接审计，
  分别归为 Ch27 No Change、Ch62 provisional refine 与 Ch5 provisional refine；KServe v0.17.0 已完成 release、
  versioned docs、PR/code surface 与 Ch49/57 去重，归为 No Change / Versioned Evolution Case；该阶段尚未修改
  Books，随后由下一条 Books Integration 记录完成写入并取代 provisional 状态。
- 随后的 Books Integration 将 31 个候选写入/refine 17 个 Stable Node owners：
  `WORLDVIEW-REPRESENTATION`、`MODEL-SELF-ATTENTION`、`MODEL-SAMPLING`、`MODEL-MOE`、
  `MODEL-LONG-CONTEXT`、`MULTIMODAL-REPRESENTATION`、`TRAIN-DATA`、`TRAIN-PRETRAINING`、
  `TRAIN-GRPO`、`INFER-PREFILL`、`INFER-KV-CACHE`、`INFER-TENSORRT-LLM`、
  `PLATFORM-EVALUATION-SYSTEM`、`AGENT-CONTEXT`、`AGENT-MEMORY`、`AGENT-PLANNING`、
  `AGENT-WORKFLOW`，以及本周早期已验证的对应 owner 内容。20 项 No Change、1 项 Emerging、2 项
  Weekly-only 均有评分表中的具体去重/拒绝依据；5 个 blocked family 未进入 Books。
- 年度索引与 Learning State 已同步为同一计数。2026-07-31 的 Ch45 内容经 owner Review 后只保留仍有
  primary evidence 支持的执行计划原则；它不再被当作独立完成证明。W11 Source-Family Books Gate 已通过，
  broader Historical Archive Gate 仍开放。

## Open Questions

1. 专用推理芯片需要多稳定的 operator/workload 分布才能覆盖硬件迭代成本？
2. IndexCache 的跨层 index similarity 在不同 sparse-attention family、不同上下文和 decode 状态下
   是否稳定，cache identity 与 invalidation 应由谁拥有？
3. intrinsic URLVR 的 confidence-correctness ceiling 能否用外部 computational asymmetry 稳定突破？
4. 待取得 Groundsource full paper 后，核对 sampling、dedup、annotation、bias、precision/recall
   denominator、label lineage 与 downstream leakage；此前不回答该问题。
5. ELIT 的多预算训练能否在 production dynamic batching 中避免 budget fragmentation 与 tail-latency
   反噬？
6. Semantic surprisal cost 如何避免惩罚 rare-but-necessary reasoning，并在 prior revision 后维持 reward
   comparability？
7. Planner 的 path statistics 与 abstracted experience 如何绑定 table/schema、executor、judge 与 tenant identity，
   并支持 supersession、delete 和 rollback？
8. FinToolBench 的 tool freshness、intent 与 domain tags 如何从 LLM annotation 演进为绑定 provider/version、
   jurisdiction 与 authorization 的可执行 policy？
9. MR-Search 的 reflection/error provenance 应何时截断、回滚或退化为 independent parallel search？
10. RAGEN-2 的 high reward variance 怎样与 noisy verifier 区分；过滤掉的 mastered/hard prompts 怎样恢复
   curriculum coverage，MI all-pairs scoring 又应怎样绑定 batch composition 与真实计算成本？
11. EvoScientist 的 derived strategy 怎样绑定 source run、baseline、environment、model/judge、scope 与 expiry，
   并用 matched compute 的 single-agent baseline 区分 memory、多 Agent coordination 与单纯额外预算？
12. MEMO 的 memory insight、candidate prompt 与 replay prefix 怎样绑定 source episode、opponent/model/prompt
   version、conflict lineage 和 rollback；又怎样用 calls/tokens/environment steps/wall-clock matched contract
   区分 context memory、RL 与更强 static policy？
13. LookaheadKV selector artifact 怎样绑定 base model、adapter、sampling policy、domain 与 cache budget，并在
   Decode attention drift、paged block packing 和 prefix reuse 下检测错误 eviction、回退或重算？
14. UCIP 的 evaluator-induced QBM signal 能否通过原生 activation intervention、预注册 threshold、multi-domain
   external replication 与 adaptive-mimicry test，证明相对 trajectory/action verifier 的独立增量？
15. One-Eval 的 plan semantic correctness 如何由 blinded expert review 验证；benchmark/schema/metric/planner/
   dataset revision 怎样共同形成 immutable evaluation identity，且 high-risk fields 应由谁批准？
16. Safe Web Agent Learning 的原标题、URL、作者或唯一 primary ID 是什么？在身份解析前不得用相似论文代替。
17. LMEB 的 temporal anchor、retrieval granularity 与 admissible candidate scope 如何绑定 tenant/ACL、
   supersession 与 delete propagation；retrieval ranking 又怎样连接完整 Memory outcome？
18. VST 的 streaming-thought service time 超过 clip interval 时怎样 backpressure/degrade；summary 如何绑定原始
   frame/time evidence，并用 total compute/energy/capacity 而非只有 query 后 latency 评估？
19. OpenSWE 怎样把 base commit、dependency lock、container digest、generated tests 与 license 固化成可撤销的
   training-sample lineage，并用 independent hidden tests 测 synthetic oracle error？
20. MM-CondChain 怎样把 Path F1 扩展到不同 branch prior/failure severity，并把 perception、predicate、path-state
   与 answer-format failure 分解为可操作 slices？
21. HomeSafe-Bench 与 Think While Watching 的官方 PDF 可访问后，能否完整核验 streaming state ownership、
   Fast/Slow path consistency、training/evaluation hardware、latency definition 与 failure recovery？
22. ReBalance 的 confidence proxy 怎样用 independent verifier 校准；checkpoint、adapter、quantization 或 prompt
   revision 后，谁负责 vector/control-surface 的 invalidation、回滚与 serving trace？
23. Expert Threshold 的 cutoff state 怎样与 checkpoint 一起保存和转换；distribution drift 与 variable fanout 怎样
   进入 EP capacity、admission、tail SLO 与 training/inference gap 观测？
24. BAVT 的 critic 与 generator 共用 backbone 时，怎样用 independent verifier 校准 residual value，并把 critic
   token/latency、异构 tool price 与不可逆风险统一纳入 budget state？
25. EnterpriseOps-Gym 的 SQL verifier 未编码语义、public split contamination 和 current artifact drift 怎样审计；
   加入真实 concurrency、eventual consistency、auth expiry 与 partial failure 后，如何维持可比较 run identity？
26. EvoClaw / SWE-Milestone 怎样以 counterfactual clean-base replay 与 multiple seeds 分离 error propagation、
   stochastic run noise 和 harness差异；未收集 tests 与 structural/security regressions 怎样补进 verifier？
27. TERMINATOR 的 label extractor、false-positive early stop、threshold/window sensitivity 与 OOD calibration 在
   full paper 可读后如何核验；此前不采用 14%～55% 或 2× headline？
28. GradMem 的 per-context optimized state 在真实多 query serving 中何时跨过 WRITE/READ break-even，并怎样处理
   checkpoint、model revision invalidation、tenant isolation 与 provenance？
29. Scientific Taste 的 citation/community proxy 怎样做 prospective calibration，并防止 AI 生成与推荐反过来
   塑造 citation distribution 形成自增强 feedback loop？
30. AgentProcessBench 的 neutral、causal propagation 与 first-error reference 怎样通过 environment state diff、
   multiple-cause annotation 和 recovery replay 变成更强 ground truth？
31. V-JEPA 2.1 的 local/global objective trade-off 能否在统一 compute budget 下分离 loss、dataset、tokenizer 与
   scale 贡献，并用 intervention 验证 dense feature 被下游实际使用？
32. KServe LLMInferenceService 的多组件 readiness、EPP freshness、KV transfer completion 与 scale-down drain
   怎样汇总为可回滚、可追踪的 service condition？

## Sources

- Meta AI Blog, “Four MTIA Chips in Two Years,” dated 2026-03-11:
  https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/
- Meta Newsroom, “Expanding Meta's Custom Silicon to Power Our AI Workloads,” 2026-03-11:
  https://about.fb.com/news/2026/03/expanding-metas-custom-silicon-to-power-our-ai-workloads/
- Google Research, “Introducing Groundsource,” 2026-03-12:
  https://research.google/blog/introducing-groundsource-turning-news-reports-into-data-with-gemini/
- Groundsource preprint metadata / blocked full-paper endpoint:
  https://eartharxiv.org/repository/view/12083/
  https://eartharxiv.org/repository/object/12083/download/21690/
- Groundsource dataset record:
  https://zenodo.org/doi/10.5281/zenodo.18647053
- NVIDIA Dynamo v1.0.0 release documentation:
  https://docs.nvidia.com/dynamo/dev/reference/releases/v1-0-0
- NVIDIA Dynamo v1.0.0 GitHub release/tag:
  https://github.com/ai-dynamo/dynamo/releases/tag/v1.0.0
- NVIDIA Dynamo release known-issues ledger:
  https://docs.nvidia.com/dynamo/dev/reference/releases/known-issues
- RAGEN official repository and 2026-03-12 release record: https://github.com/mll-lab-nu/RAGEN
- RAGEN-2 official project page: https://ragen-ai.github.io/
- RAGEN-2 arXiv abstract and sole-v1 history: https://arxiv.org/abs/2604.06268
- RAGEN-2 full v1 HTML: https://arxiv.org/html/2604.06268v1
- RAGEN GitHub release boundary: https://github.com/mll-lab-nu/RAGEN/releases
- Compiler-First State Space Duality metadata/full HTML/code:
  https://arxiv.org/abs/2603.09555
  https://arxiv.org/html/2603.09555v1
  https://github.com/CosmoNaught/mamba2-jax
- IndexCache metadata/full HTML:
  https://arxiv.org/abs/2603.12201
  https://arxiv.org/html/2603.12201v1
- How Far Can Unsupervised RLVR Scale LLM Training? metadata/PDF:
  https://arxiv.org/abs/2603.08660
  https://arxiv.org/pdf/2603.08660v1
- OpenClaw-RL metadata/full HTML/code:
  https://arxiv.org/abs/2603.10165
  https://arxiv.org/html/2603.10165v1
  https://github.com/OpenClaw-RL/OpenClaw-RL
- Flash-KMeans metadata/full HTML:
  https://arxiv.org/abs/2603.09229
  https://arxiv.org/html/2603.09229v1
- FP4 Mean Bias / Averis metadata/full HTML:
  https://arxiv.org/abs/2603.10444
  https://arxiv.org/html/2603.10444v1
- TDAD metadata/full HTML/repository:
  https://arxiv.org/abs/2603.08806
  https://arxiv.org/html/2603.08806v1
  https://github.com/f-labs-io/tdad-paper-code
- XSkill metadata/full HTML/project/repository:
  https://arxiv.org/abs/2603.12056
  https://arxiv.org/html/2603.12056v1
  https://xskill-agent.github.io/xskill_page/
  https://github.com/XSkill-Agent/XSkill
- DIVE metadata/full HTML/project:
  https://arxiv.org/abs/2603.11076
  https://arxiv.org/html/2603.11076v1
  https://sheep333c.github.io/DIVE/
- Automatic Generation of High-Performance RL Environments metadata/full HTML:
  https://arxiv.org/abs/2603.12145
  https://arxiv.org/html/2603.12145v1
- Examining Reasoning LLMs-as-Judges metadata/full HTML:
  https://arxiv.org/abs/2603.12246
  https://arxiv.org/html/2603.12246v1
- ReMix metadata/full HTML:
  https://arxiv.org/abs/2603.10160
  https://arxiv.org/html/2603.10160v1
- In-Context Reinforcement Learning for Tool Use metadata/PDF:
  https://arxiv.org/abs/2603.08068
  https://arxiv.org/pdf/2603.08068v1
- OneMillion-Bench metadata/full HTML:
  https://arxiv.org/abs/2603.07980
  https://arxiv.org/html/2603.07980v1
- Agentic Critical Training metadata/full HTML:
  https://arxiv.org/abs/2603.08706
  https://arxiv.org/html/2603.08706v1
- Fish Audio S2 metadata/full HTML:
  https://arxiv.org/abs/2603.08823
  https://arxiv.org/html/2603.08823v1
- SoundWeaver metadata/full HTML:
  https://arxiv.org/abs/2603.07865
  https://arxiv.org/html/2603.07865v1
- RetroAgent metadata/full HTML:
  https://arxiv.org/abs/2603.08561
  https://arxiv.org/html/2603.08561v1
- Thinking to Recall metadata/full HTML:
  https://arxiv.org/abs/2603.09906
  https://arxiv.org/html/2603.09906v1
- InternVL-U metadata/full HTML/repository/model:
  https://arxiv.org/abs/2603.09877
  https://arxiv.org/html/2603.09877v1
  https://github.com/OpenGVLab/InternVL-U
  https://huggingface.co/InternVL-U/InternVL-U
- Towards a Neural Debugger for Python metadata/full HTML:
  https://arxiv.org/abs/2603.09951
  https://arxiv.org/html/2603.09951v1
- Lost in Backpropagation metadata/full HTML:
  https://arxiv.org/abs/2603.10145
  https://arxiv.org/html/2603.10145v1
- V0.5 metadata/full HTML:
  https://arxiv.org/abs/2603.10848
  https://arxiv.org/html/2603.10848v1
- MR-Search metadata/full HTML/code:
  https://arxiv.org/abs/2603.11327
  https://arxiv.org/html/2603.11327v1
  https://github.com/tengxiao1/MR-Search
- MADQA metadata/primary PDF/baseline/dataset:
  https://arxiv.org/abs/2603.12180
  https://arxiv.org/pdf/2603.12180v1
  https://github.com/OxRML/MADQA
  https://huggingface.co/datasets/OxRML/MADQA
- Attention Sinks theorem metadata/full HTML:
  https://arxiv.org/abs/2603.11487
  https://arxiv.org/html/2603.11487v1
- ELIT metadata/full HTML/project:
  https://arxiv.org/abs/2603.12245
  https://arxiv.org/html/2603.12245v1
  https://snap-research.github.io/elit/
- Neural Thickets metadata/full HTML:
  https://arxiv.org/abs/2603.12228
  https://arxiv.org/html/2603.12228v1
- EvoScientist metadata / sole-v1 history and full PDF:
  https://arxiv.org/abs/2603.08127
  https://arxiv.org/pdf/2603.08127
- EvoScientist later official project and repository（artifact evolution; not assumed to be the experiment commit）:
  https://evoscientist.ai/
  https://github.com/EvoScientist/EvoScientist
- MEMO v1/v2 metadata、current-v2 PDF 与 official repository:
  https://arxiv.org/abs/2603.09022v1
  https://arxiv.org/abs/2603.09022
  https://arxiv.org/pdf/2603.09022
  https://github.com/openverse-ai/MEMO
- Reasoning as Compression v1/v2 metadata and v1 full HTML:
  https://arxiv.org/abs/2603.08462
  https://arxiv.org/html/2603.08462v1
- Deep Tabular Research v1/v2 metadata and 23-page full paper:
  https://arxiv.org/abs/2603.09151
  https://arxiv.org/pdf/2603.09151
- FinToolBench v1/v2 metadata, v1 full text and official partial artifact:
  https://arxiv.org/abs/2603.08262
  https://arxiv.org/html/2603.08262v1
  https://github.com/Double-wk/FinToolBench
- FineRMoE cross-year primary-publication record (2025-09-11; modified 2026-02-11):
  https://openreview.net/forum?id=JxXy3YGSln
- LookaheadKV metadata, sole-v1 full HTML and official repository:
  https://arxiv.org/abs/2603.10899
  https://arxiv.org/html/2603.10899
  https://github.com/SamsungLabs/LookaheadKV
- UCIP v1/current revision metadata, current full HTML and official artifact repository:
  https://arxiv.org/abs/2603.11382
  https://arxiv.org/html/2603.11382
  https://github.com/christopher-altman/persistence-signal-detector
- One-Eval metadata, sole-v1 full HTML and official repository:
  https://arxiv.org/abs/2603.09821
  https://arxiv.org/html/2603.09821v1
  https://github.com/OpenDCAI/One-Eval
- LMEB v1/current revision、current full HTML and official benchmark repository:
  https://arxiv.org/abs/2603.12572
  https://arxiv.org/html/2603.12572v1
  https://arxiv.org/html/2603.12572
  https://github.com/KaLM-Embedding/LMEB
- Video Streaming Thinking v1/current revision、v1 full HTML and official repository:
  https://arxiv.org/abs/2603.12262
  https://arxiv.org/html/2603.12262v1
  https://github.com/1ranGuan/VST
- daVinci-Env / OpenSWE v1/current revision、full HTML and official repository:
  https://arxiv.org/abs/2603.13023
  https://arxiv.org/html/2603.13023v2
  https://github.com/GAIR-NLP/OpenSWE
- MM-CondChain sole-v1 metadata/full HTML and official artifacts:
  https://arxiv.org/abs/2603.12266
  https://arxiv.org/html/2603.12266
  https://github.com/Accio-Lab/MM-CondChain
  https://huggingface.co/datasets/Accio-Lab/MM-CondChain
- HomeSafe-Bench metadata（full text blocked）:
  https://arxiv.org/abs/2603.11975
- Think While Watching metadata and inference-only official repository（full text blocked）:
  https://arxiv.org/abs/2603.11896
  https://github.com/wanglu-cs/Think_While_Watching
- Efficient Reasoning with Balanced Thinking / ReBalance metadata, full HTML and official artifact:
  https://arxiv.org/abs/2603.12372
  https://arxiv.org/html/2603.12372
  https://github.com/yu-lin-li/ReBalance
- Expert Threshold Routing sole-v1 metadata and full HTML:
  https://arxiv.org/abs/2603.11535
  https://arxiv.org/html/2603.11535
- Spend Less, Reason Better / BAVT sole-v1 metadata and full HTML:
  https://arxiv.org/abs/2603.12634
  https://arxiv.org/html/2603.12634v1
- EnterpriseOps-Gym sole-v1 paper and official repository:
  https://arxiv.org/abs/2603.13594
  https://arxiv.org/pdf/2603.13594
  https://github.com/ServiceNow/EnterpriseOps-Gym
- EvoClaw / current SWE-Milestone v1/current metadata, v1 full HTML and official artifacts:
  https://arxiv.org/abs/2603.13428
  https://arxiv.org/html/2603.13428v1
  https://github.com/DeepCommit-ai/SWE-Milestone
  https://huggingface.co/datasets/DeepCommit-ai/SWE-Milestone-data
- TERMINATOR metadata, blocked full-paper endpoint and official project/model artifacts:
  https://arxiv.org/abs/2603.12529
  https://arxiv.org/pdf/2603.12529
  https://terminator-llm.github.io/
  https://huggingface.co/collections/acnagle/terminator
- GradMem sole-v1 metadata/full HTML and official implementation:
  https://arxiv.org/abs/2603.13875
  https://arxiv.org/html/2603.13875
  https://github.com/yurakuratov/gradmem
- SFT versus RL survey sole-v1 metadata/full HTML:
  https://arxiv.org/abs/2603.13985
  https://arxiv.org/html/2603.13985
- AI Can Learn Scientific Taste v1/current metadata、v1 full HTML and official repository:
  https://arxiv.org/abs/2603.14473
  https://arxiv.org/html/2603.14473v1
  https://github.com/tongjingqi/AI-Can-Learn-Scientific-Taste
- AgentProcessBench v1/current metadata、v1 full HTML and official repository:
  https://arxiv.org/abs/2603.14465
  https://arxiv.org/html/2603.14465v1
  https://github.com/RUCBM/AgentProcessBench
- V-JEPA 2.1 v1/current metadata、v1 full HTML and official repository:
  https://arxiv.org/abs/2603.14482
  https://arxiv.org/html/2603.14482v1
  https://github.com/facebookresearch/vjepa2
- KServe v0.17.0 release, release article and versioned documentation:
  https://github.com/kserve/kserve/releases/tag/v0.17.0
  https://kserve.github.io/website/blog/kserve-0.17-release
  https://kserve.github.io/website/docs/0.17/model-serving/generative-inference/llmisvc/llmisvc-overview
  https://kserve.github.io/website/docs/0.17/concepts/architecture
  https://kserve.github.io/website/docs/0.17/getting-started/quickstart-guide
- Hugging Face discovery pages used only as candidate indices:
  https://huggingface.co/papers/date/2026-03-09
  https://huggingface.co/papers/date/2026-03-10
  https://huggingface.co/papers/date/2026-03-11
  https://huggingface.co/papers/date/2026-03-12
  https://huggingface.co/papers/date/2026-03-13
