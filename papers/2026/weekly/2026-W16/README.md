# AI Research Weekly — 2026-W16

> Coverage Window: 2026-04-13～2026-04-19
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-09
> Re-audit Status: Discovery Recall Repaired; 42/42 scored families reviewed and dispositioned; 3/3 named low-score rejections verified; W16 Evidence Gate Passed; Source-Family Books Gate Complete; Archive Completion Gate Open

## Executive Summary

旧版 W16 只保留三项机构研究，不能证明完整论文与 AI Infra 候选池。三项 baseline 都在改变
“任务规范怎样进入模型系统”：Anthropic 用模型辅助 scalable oversight
研究；OpenAI GPT-Rosalind 面向 life-science workflow；Google 讨论以 mechanism design 和
first principles 构造 synthetic datasets。共同点是任务定义、验证器和数据生成过程开始成为
模型能力的一部分，而非外围 benchmark。本轮保留它们的 Full Source Review，但重开全窗口
discovery。按 first-public date 已恢复 34 个候选，并完成 CodeTracer、BEHEMOTH、Sema Code 全文与
公开 artifact 审计；OccuBench 的两版论文、公开 data/code 与 simulator/verifier 边界也已完成
全文审计；Agentic Aggregation 的论文、appendix、公开 rollouts/code 与 evidence-navigation
边界也已完成审计；ClawGUI 的论文、training/eval/deployment modules 与 real-device claim 边界
也已完成审计；Rethinking On-Policy Distillation 与 AiScientist 的论文、公开 artifact 和章节邻接
也已完成审计；W17 curation feed 又暴露 6 个实际属于 04-13～04-19 的 spillbacks。第二轮逐日
HF/arXiv 召回又确认 15 个此前静默遗漏的本周 `20+` families。DR3-Eval、
Corpus2Skill、OpenMobile 与 Scaling Test-Time Compute 的论文、appendices、
公开 evidence 与适用域边界也已完成审计。W16 的 42 个 scored families 已全部获得最终 Books disposition；
本周 Gate 已通过，但全年度 Archive Completion Gate 仍保持 Open。

## Coverage and Source Coverage

- 模型与研究机构：除 Anthropic 4 月 14 日、OpenAI 与 Google Research 4 月 16 日条目外，
  补回 Google DeepMind 4 月 14 日 Gemini Robotics-ER 1.6；model card 于 W17 才发布，只作
  related later evidence，不倒灌事件日期。固定机构清单已重扫，长尾 Weekly-trigger institutions
  仍需做最终 archive-level closure。
- 论文与学术来源：自动化 alignment 与 synthetic-data 结论按作者实验处理；2026-04-13～04-19
  的 arXiv v1 与 Hugging Face Daily Papers 已完成两轮恢复，新增 CodeTracer、Sema Code、
  Agentic Aggregation、ClawGUI、On-Policy Distillation、AgentSPEX、OpenMobile、SkillFlow 等
  第一轮 19 个 family；第二轮又恢复 MEDS、CocoaBench、KnowRL、LMM-Searcher、Lightning OPD、
  YOJO、DDTree、RationalRewards、UI-Copilot、SemaClaw、TIP、SD-Zero、KV Packet、LongAct 与 C2；
  OpenReview/TMLR、formal proceedings 与 04-18～04-19 discovery pages 已完成 first-public-date 与
  source-family 去重；ICLR 2026 accepted records 首次公开在 1 月、TMLR 4 月刊中的 project-relevant
  entries 可追溯到更早 preprint/submission，没有新增属于 W16 的 `20+` family。
- AI Infra：固定项目重扫补回 SGLang Q2 Roadmap、Megatron Core 0.17.0、NVIDIA Dynamo agentic
  inference、NemoClaw/OpenShell reference stack 与 Hugging Face PEFT 0.19.0；vLLM 0.19.1、
  DeepStream coding-agent tutorial 与 PEFT 0.19.1 仅为 patch/tutorial 级低分项，保留在 below-threshold ledger。
  fixed release/RFC/PR list 与 Weekly-trigger archives 已闭合；未发现其他达到 20 分且属于本周首发的事件。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Automated alignment researchers | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | Worth Watching |
| Synthetic datasets from first principles | 4 | 3 | 4 | 4 | 4 | 4 | 23/30 | Worth Watching |
| GPT-Rosalind | 3 | 3 | 4 | 5 | 3 | 3 | 21/30 | Official model state |
| CodeTracer: Towards Traceable Agent States | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read — full review complete |
| Self-Evolving LLM Memory Extraction / BEHEMOTH | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read — full review complete |
| Sema Code | 3 | 4 | 4 | 3 | 5 | 4 | 23/30 | Worth Watching — full review complete; score corrected after evidence review |
| OccuBench | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Worth Watching — full review complete |
| Agentic Aggregation | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read — full review complete; score corrected after evidence review |
| ClawGUI | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Worth Watching — full review complete; score corrected after evidence review |
| Rethinking On-Policy Distillation | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read — full review complete; score corrected after evidence review |
| Toward Autonomous Long-Horizon Engineering | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Must Read — full review complete; scoring axes corrected after evidence review |
| AgentSPEX | 3 | 4 | 4 | 3 | 5 | 4 | 23/30 | Worth Watching — full review complete; score corrected after evidence review |
| Memory Transfer Learning | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Worth Watching — full review complete; score corrected after evidence review |
| Exploration and Exploitation Errors Are Measurable | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read — full review complete |
| DR3-Eval | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Worth Watching — full review complete; score corrected after evidence review |
| Dive into Claude Code | 3 | 4 | 4 | 3 | 4 | 4 | 22/30 | Worth Watching — full review complete |
| Don't Retrieve, Navigate | 4 | 4 | 5 | 3 | 4 | 4 | 24/30 | Worth Watching — full review complete; score corrected after evidence review |
| OpenMobile | 4 | 4 | 5 | 3 | 5 | 3 | 24/30 | Worth Watching — full review complete; score corrected after evidence review |
| Scaling Test-Time Compute for Agentic Coding | 4 | 5 | 4 | 3 | 5 | 4 | 25/30 | Must Read — full review complete; score corrected after evidence review |
| SkillFlow | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Worth Watching — full review complete; score corrected after evidence review |
| EvoMaster | 3 | 4 | 4 | 3 | 5 | 4 | 23/30 | Worth Watching — full review complete; score corrected after evidence review |
| The Past Is Not Past / MEDS | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read — full review complete |
| CocoaBench | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Worth Watching — full review complete |
| KnowRL | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Worth Watching — full review complete |
| LMM-Searcher | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Worth Watching — full review complete |
| Lightning OPD | 4 | 5 | 5 | 2 | 4 | 3 | 23/30 | Disputed — full review complete; theoretical proof boundary corrected |
| You Only Judge Once / YOJO | 3 | 4 | 4 | 4 | 4 | 3 | 22/30 | Worth Watching — full review complete |
| Block Diffusion Draft Trees / DDTree | 4 | 5 | 4 | 4 | 5 | 3 | 25/30 | Must Read — full review complete |
| RationalRewards | 4 | 3 | 3 | 4 | 4 | 4 | 22/30 | Worth Watching — full review complete |
| UI-Copilot | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Worth Watching — full review complete |
| SemaClaw | 3 | 4 | 4 | 3 | 5 | 4 | 23/30 | Worth Watching — full review complete |
| TIP: Token Importance in OPD | 4 | 5 | 5 | 4 | 4 | 3 | 25/30 | Must Read — full review complete |
| Self-Distillation Zero | 4 | 4 | 5 | 4 | 5 | 3 | 25/30 | Must Read — full review complete |
| KV Packet | 5 | 5 | 5 | 4 | 5 | 2 | 26/30 | Must Read — full review complete |
| LongAct | 4 | 4 | 4 | 3 | 4 | 4 | 23/30 | Worth Watching — full review complete |
| C2 Rubric-Augmented Reward Modeling | 3 | 4 | 4 | 3 | 4 | 4 | 22/30 | Worth Watching — full review complete |
| Gemini Robotics-ER 1.6 | 3 | 4 | 4 | 4 | 4 | 3 | 22/30 | Weekly Only — version/capability fact; mechanism not disclosed |
| SGLang Q2 2026 Roadmap | 3 | 5 | 2 | 5 | 5 | 3 | 23/30 | Emerging — roadmap, not landed behavior |
| Megatron Core 0.17.0 | 2 | 4 | 4 | 5 | 4 | 3 | 22/30 | Weekly Only — release family; no single new mechanism claim |
| Full-Stack Optimizations for Agentic Inference with NVIDIA Dynamo | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read — full review complete; mixed current/future boundary |
| NemoClaw + OpenShell local-agent reference stack | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | No Change — reference deployment; full review complete |
| Hugging Face PEFT 0.19.0 | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Must Read — release-family review complete; individual paper claims not inherited |

本轮账目为 42 行：14 个 `25～30`、28 个 `20～24`、0 个 `<20` scored rows。另有 3 个
named below-threshold screened items。评分只是全文阅读优先级，
不是 Books disposition。

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Baseline score rows | 3 | 3/3 `20+` Source Reviews 保留 |
| Recovered candidate families | 39 | 第一轮 18/18、第二轮 15/15、official/infra closure 6/6 non-template Full Source Reviews 完成；Nemotron 3 Super 按 03-04 首发回拨 W10 |
| Total score rows | 42 | 14 high / 28 mid / 0 low；另有 3 个 named below-threshold screened items；六维算术复核通过 |
| Academic discovery window | Closed | arXiv/HF 两轮恢复完成；OpenReview/TMLR/formal proceedings/weekend discovery 完成 first-public-date 去重，无新增 W16 family |
| Official / Infra discovery window | Closed | fixed/weekly-trigger sources 补回 6 个 `20+` families 与 3 个 named low-score items；release/RFC/PR attribution 已复核 |
| W16 Evidence Gate | Passed | 42/42 `20+` reviews complete；3/3 named low-score rejection verified；candidate、coverage 与 attribution queues 清零 |

### Below-Threshold Screened Items

| Candidate | Score | Verification / Rejection Reason |
| --- | ---: | --- |
| vLLM 0.19.1 | 19/30 | 2026-04-18 official patch release；以 Transformers/Gemma4、quantized MoE、Eagle3、LoRA 与 media-placeholder fixes 为主，没有独立的新系统机制或完整 workload evidence |
| NVIDIA DeepStream coding-agent tutorial | 17/30 | 2026-04-16 tutorial；展示把 coding agent 用于 video-analytics pipeline，但没有可归因的新 runtime/evaluation mechanism |
| PEFT 0.19.1 | 17/30 | 2026-04-16 patch release；兼容性与 bug-fix 价值明确，但不足以改变本书关于 parameter-efficient update 的长期结论 |

### Second-pass Discovery Attribution Review

逐日推荐页只用于 discovery，归周以 primary source 的 first-public date 为准。第二轮已逐项拆开
“论文首发”和“HF 推荐/提交日”，避免把旧论文的二次传播误记为 W16：

| Candidate | Primary first-public date | Attribution / Triage |
| --- | --- | --- |
| Multi-User Large Language Model Agents | 2026-03-19 | 回拨 W12；不是 W16 新事件 |
| AgentSwing | 2026-03-29 | 回拨 W13；不是 W16 新事件 |
| Backdoor Attacks on Decentralised Post-Training | 2026-03-31 | 已回拨 W14 Unverified / Blocked Backlog；primary identity 未定位；不是 W16 新事件 |
| Cactus | 2026-04-05 | 已回拨 W14 Unverified / Blocked Backlog；primary identity 未定位；不是 W16 新事件 |
| SkVM | 2026-04-03 v1；04-06/11 revisions | primary identity arXiv:2604.03088 已定位；完整 Source Family 与 Full Source Review 回拨 W14；不是 W16 新事件 |
| GameWorld | 2026-04-08 | primary identity arXiv:2604.07429 已定位并回拨 W15；metadata/project/repository 已审，primary PDF full read unavailable，维持 blocked backlog |
| Process Reward Agents | 2026-04-10 | primary identity arXiv:2604.09482 已定位；Full Source Review 回拨 W15；不是 W16 新事件 |
| BERT-as-a-Judge | 2026-04-10 | primary identity arXiv:2604.09497 已定位；Full Source Review 回拨 W15；不是 W16 新事件 |
| Many-Tier Instruction Hierarchy | 2026-04-10 | primary identity arXiv:2604.09443 已定位；Full Source Review 回拨 W15；不是 W16 新事件 |
| SCOPE (OPD) | 2026-04-12 | primary identity arXiv:2604.10688 已定位；Full Source Review 回拨 W15；不是 W16 新事件 |
| Tracing the Roots | 2026-04-12 | primary identity arXiv:2604.10480 已定位；Full Source Review 回拨 W15；不是 W16 新事件 |
| MEDS、CocoaBench、YOJO、RationalRewards、SemaClaw、SD-Zero | 2026-04-13 | 保留 W16；进入 Full Source Review queue |
| KnowRL、LMM-Searcher、Lightning OPD、DDTree、KV Packet | 2026-04-14 | 保留 W16；进入 Full Source Review queue |
| UI-Copilot、TIP、C2 | 2026-04-15 | 保留 W16；进入 Full Source Review queue |
| LongAct | 2026-04-16 | 保留 W16；进入 Full Source Review queue |

该表只记录已完成 first-public date 核验的 project-relevant candidates；视觉生成、3D reconstruction、
医学影像等窄域条目若未改变模型、训练、serving、evaluation 或 Agent 系统结论，保留在 discovery
coverage 而不进入 `20+` 账目。它们不是因热度低被忽略，而是因本书知识树相关性不足被筛除。

## Evidence Level

模型辅助 alignment 的 uplift 不证明可独立监督更强模型；synthetic data 的 controllability
不消除 sim-to-real gap；GPT-Rosalind 的领域 benchmark 属厂商评测。

## Cross-Week Deduplication

后续 LifeSciBench 与 AI chemist 是同一 science-workflow 路线的 evaluation/execution 层，
不重复记为新基础架构。按 first-public date 纠正 curation lag：Multi-User Agents 回拨 W12；
AgentSwing 回拨 W13；Backdoor Attacks 与 Cactus 回拨 W14；SkVM、GameWorld、Process Reward Agents、
BERT-as-a-Judge、Many-Tier Instruction Hierarchy、SCOPE 与 Tracing the Roots 回拨 W15；SPPO（2026-04-10）回填 W15，
SPEED-Bench（2026-02-10）回填 W07；EXAONE 4.5、TRACE、Efficient RL with Experience Replay
等 04-09～04-10 条目不计入 W16。W17 推荐流中的 BEHEMOTH（04-13）、AgentSPEX（04-14）、
OpenMobile 与 Scaling Test-Time Compute（04-16）、SkillFlow 与 EvoMaster（04-19）均按 arXiv v1
回拨 W16；Nemotron 3 Super 的 base checkpoint 已于 03-04 首发，post-trained checkpoint 于 03-11
发布，04-14 arXiv v1 只是 formal report revision，整条 source family 回拨 W10，并在 W11/W16 保留
演进指针；后续 revision 只用于核验，不改写事件周。

## Knowledge Tree Position

Ch23 Data → Ch27/29 Post-training → Ch62/65 Evaluation and Trace → Ch72/73 RAG and
Memory → Ch77/78/80 Workflow, Multi-Agent and Agent Platform。

## Recommended Action

保留“data generator + verifier + workflow”联合设计路线，并把 W16 的稳定机制分别吸收到 Memory、Evaluation、
Multi-Agent、SFT/GRPO/LoRA、RAG、Workflow、Agent Platform、KV Cache 与 Dynamo 的既有演进节点。
DDTree 的 Ch24 integration 经复核保留；Lightning OPD 维持 `Disputed`，roadmap/release/product facts 不进入
长期机制正文。W16 Source-Family Books Gate 已完成，游标推进 W17；全年度 Archive Completion Gate 仍 Open。

## Event-Date Daily Decision

2026-04-14、04-16：Weekly only。

## Provisional Books Integration Decision — Superseded 2026-08-14

`Blocked — Not Started`。三项 baseline 的 provisional dispositions 分别为两个 `No Change` 与一个
`Weekly Only — Version/Product Fact`；CodeTracer 暂定 `Refine — Existing Argument`，但只记录
候选机制，不写 Books；BEHEMOTH 暂定 `Refine — Existing Argument (Experimental)`；Sema Code
为 `No Change — Already Covered`；OccuBench、Agentic Aggregation、ClawGUI 与 On-Policy Distillation 暂定
`Refine — Existing Argument (Experimental)`；AiScientist 暂定 Ch77 `Refine — Existing Argument
(Experimental)`，Ch78 只作 handoff；AgentSPEX 为 Ch77 `No Change — Already Covered`；Exploration/
Exploitation Errors 暂定 Ch62 `Refine — Existing Argument (Experimental)`；Dive into Claude Code
为 Ch80 `No Change — Already Covered`，其 reverse-engineering observation 不升级为官方实现事实。
Memory Transfer Learning 暂定 Ch73 `Refine — Existing Argument (Experimental)`；DR3-Eval 暂定
Ch62 `Refine — Existing Argument (Experimental)`；Don't Retrieve, Navigate 暂定 Ch72
`Refine — Existing Argument (Experimental)`；OpenMobile 暂定 Ch25
`Refine — Existing Argument (Experimental)`，Ch23 只作 data-lineage handoff；Scaling Test-Time Compute
暂定 Ch78 `Refine — Existing Argument (Experimental)`，Ch62/77/80 只作 handoff；SkillFlow 为
Ch62/73/80 `No Change — Already Covered`，其 sequence-state、derived procedural memory 与 versioned Skill
边界已由现有正文拥有；EvoMaster 为 Ch77/78/80 `No Change — Already Covered`，其 reactive loop、
orchestration、trajectory 与 evaluator-driven refinement 已由现有章节拥有；Gemini Robotics-ER 1.6
为 `Weekly Only — Mechanism Not Disclosed`，SGLang Q2 为 `Emerging`，Megatron Core 0.17.0 为
`Weekly Only — Release Family`，NemoClaw 为 `No Change`；Dynamo agentic inference 暂定 Ch48
`Refine — Existing Argument`，Ch52/77 只作 handoff；PEFT 0.19.0 暂定 Ch26 `Refine — Existing
Argument`，Ch31/46 只作 artifact/runtime handoff；
W16/全历史 Evidence Gate
通过前不进入
Historical Books Integration。此段保留为审计历史，最终决定见文末 `Final Books Integration Ledger`。

## Ignored Noise

把 domain benchmark 写成真实科研闭环已经自治，或把 synthetic data 写成现实数据替代品。

## Full Source Review

### Self-Evolving LLM Memory Extraction / BEHEMOTH — 25/30

- **Candidate / Week / Source Family**：`BEHEMOTH-CLUE-MEMORY-EXTRACTION`；W16；arXiv
  2604.11610，唯一 v1 于 2026-04-13 15:15 UTC 首次公开；论文 HTML、全部正文与 Appendix A～C、
  作者 repository、公开 benchmark data/entrypoints 于 2026-08-10 核验。
- **Access / Full-read Coverage**：已覆盖 task formulation、18-dataset curation、static-prompt
  baselines、GEPA/ACE/MemEvolve、CluE 四阶段机制、ID/OOD results、stronger-seed、continual
  transfer、backend transfer、efficiency、per-dataset tables、cluster/taxonomy analysis、prompts、
  limitations，以及 repository 的 dataset adapters、evaluation/judge surface 与 evolution CLI。
- **Original Problem / Previous Design**：固定的 domain-specific extraction prompt 对单一 memory
  用途合理：personalization 需要事实/偏好，reasoning trajectory 需要策略/失败教训；但同一 assistant
  跨越异构任务后，单一 taxonomy 没有普遍最优。直接频繁更新会偏向最近 batch，低频全局更新又会
  让不相似反馈相互抵消。固定 prompt 仍适合边界稳定、风险高、需要人工审计的窄域 memory。
- **Changed Constraint / Mechanism**：BEHEMOTH 将 5 个 personalization、7 个 problem-solving、
  6 个 agentic datasets 统一为 `(source conversation, target query, reward)`。CluE 每轮先运行当前
  extraction prompt 形成 logs，再由 Summarizer 抽象 extraction scenario；Cluster Manager 可创建、
  合并或拆分 scenario clusters；Cluster Analyzer 分别提取成功/失败模式；Proposer 最后把局部建议
  合成为一个同时含跨域原则与分类规则的新 prompt，而不是逐条追加或全量重写。
- **State Ownership / Control and Data Flow**：原始 source/target/reward triple 属 benchmark/evaluation
  owner；extracted memory 是 model-derived candidate；cluster pool、per-cluster analysis、candidate
  prompt 与 tournament winner 是 optimizer-owned policy state；generation result 和 task reward 只为
  extraction policy 提供反馈。统一 prompt 是 derived control artifact，不能成为用户事实的 truth
  authority，也不能反向覆盖原始 conversation、consent 或 deletion record。
- **Implementation Details**：作者实现默认 5 rounds、每轮 35 training examples、3 个 proposed
  systems、2 个 tournament survivors、最多 7 clusters，并支持 async extraction 与 resume。训练集
  330 项：14 个 ID datasets 各 20 项，AIME 50 项；Qwen3-32B 默认同时完成 source trajectories、
  extraction 与 generation，LongMemEval、GPQA-Diamond、ToolBench 各作为一类的 OOD dataset。
  repository 暴露 per-dataset adapters、prompt registry、CluE/GEPA/ACE/MemEvolve entrypoints 和
  LLM-judge evaluation；无 tagged release，当前代码是论文 artifact 而非稳定 service contract。
- **Evaluation Contract**：主表固定 Qwen3-32B extractor/generator，以 per-dataset reward 的 macro
  average 和相对 Simple prompt 的 per-dataset ratio geometric mean 聚合；部分 stochastic tasks
  运行 3 次。CluE 从 Simple 起点的总体 relative gain 为作者协议下 `+9.04%`，但 per-dataset 仍有
  AIME、PersonaMem、ScienceWorld 等回退。OOD 只各留一个 dataset；continual 实验只选择 Game of
  24 与 AlfWorld，并固定 embedding top-1 retrieval + concatenation consolidation。Gemini-3-Flash
  transfer 仍在 Agentic 类别相对 Simple 回退 `-5.93%`。
- **Evidence / What It Proves**：在作者构造、模型和 evaluator contract 下，cluster-local analysis
  相对 small-batch recency bias 与 global heterogeneous-feedback dilution 提供了更稳的聚合方法；
  stronger seed 实验也支持“保留既有强项”是 prompt evolution 的独立目标。221 次 optimizer calls
  对比 MemEvolve 的 30 次，表明收益来自新增分析结构而非免费更新。
- **What It Does Not Prove**：downstream utility 同时混合 extractor、generator、dataset、sampling
  与 reward，不是 memory intrinsic correctness 或单条 memory 的因果贡献。source trajectories
  多由同一 Qwen3-32B 合成，extractor/optimizer/generator 的共享盲点未被独立排除；LongMemEval 和
  ToolBench 仍用 LLM judge。论文只研究 lifecycle 的 extraction stage；storage、authorization、
  retrieval、conflict/supersession、delete propagation、privacy、真实长期 drift 与 production SLO
  均未验证。Continual 结果选取两个单步已领先任务，不能外推为任意 memory stack 的稳定收益。
- **Trade-offs / New Failure Modes**：获得 heterogeneity-aware feedback isolation、可演化 taxonomy
  与较好的强 seed 保留；付出更多 optimizer calls、cluster/summarizer/proposer 版本状态、评估成本与
  release/rollback 复杂度。新风险包括 summary 丢失关键条件、cluster churn、相似场景误合并、少数
  任务信号被 aggregate 隐藏、reward hacking、全局 prompt 仍发生 negative transfer，以及 derived
  prompt 在新 model/tool/environment revision 下 stale。
- **Where Previous Designs Still Apply / Alternatives**：静态 typed prompt 适合窄域和可审计高风险
  写入；per-domain router 可避免把所有差异合成一份 prompt，但新增 routing error 与 cold-start；
  skill bank 保存多个 extraction policy，却需要 provenance、选择和 garbage collection；完整 raw
  history 在短且高风险的 trajectory 中仍可作为 no-extraction baseline。CluE 是这些分支之一，不是
  单向替代。
- **Evolution Relationship**：`Direct Evolution`：固定 extraction prompt → feedback-evolved global
  prompt → cluster-local analysis + cross-cluster synthesis；`Layering / Dependency`：extraction policy
  位于 authoritative raw history 与 storage/retrieval/consolidation lifecycle 之间；`Principle Reuse`：
  分群隔离异构反馈类似 mixture/router 思想，但这里路由的是 optimizer evidence，不是 token execution。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch72、Ch73 及下一章 action boundary；
  Ch73 已覆盖 typed memory、write validation、derived-state provenance、consolidation、forgetting、
  evaluation 与 raw/derived ownership。真正缺口不是再加一种 taxonomy，而是把 extraction policy
  本身建模为带 model/reward/task-distribution identity、regression suite、version、promotion 与
  rollback 的 derived artifact；主 owner 暂定 Ch73，Ch62/77/80 只需短 handoff。
- **Integration Decision / Open Questions**：provisional `Refine — Existing Argument (Experimental)`；
  Historical Books Gate 关闭，暂不写正文。待核验真实多用户 history、独立 extractor/generator/judge、
  adversarial/rare cluster、per-domain routing 对照、长期 prompt drift、privacy/delete propagation 与
  end-to-end cost/SLO。

### Sema Code — 23/30

- **Candidate / Week / Source Family**：`SEMA-CODE-EMBEDDABLE-AGENT-ENGINE`；W16；arXiv
  2604.11045，唯一 v1 于 2026-04-13 06:20 UTC 首次公开；论文内署日期 2026-04-10 不替代
  first-public date。论文 HTML、全部章节、两份作者仓库、current package/public API 与 tags 于
  2026-08-10 核验。
- **Access / Full-read Coverage**：已覆盖 Related Work、three-layer architecture、multi-tenant /
  hierarchical state、FIFO queue、session reconstruction、context compression、multi-agent runtime、
  interrupt/tool scheduling、Todo state machine、background execution、four-layer permission、async
  approval、MCP/Skill/Plugin ecosystem、model adapter、两项 deployment case 与 limitations；并检查
  current `SemaCore`/`SemaEngine` public surface、manager/service tree、npm metadata 与 VSCode client。
- **Score Correction**：`26→23/30`（TN `4→3`、SI `5→4`、PV `5→4`、SR `4→3`、L `3→4`）。
  engine/client decoupling 与多数机制有长期价值，但论文没有 quantitative benchmark、stress test、
  component ablation、failure injection 或 security evaluation；两个功能性部署不能支撑原来的
  Must Read / production-scale 强度。
- **Original Problem / Previous Design**：CLI/IDE/web monolith 把 reasoning loop、state 与 delivery
  form 绑定，对单一产品可减少 API surface 并优化 UX；企业需要复用同一 coding runtime 到多个
  channel、替换 model/provider、服务多个 session 后，这种耦合会复制 engine 与 policy。单体产品
  仍适合只服务一种交互、强 client-specific optimization 且无需第三方嵌入的场景。
- **Changed Constraint / Mechanism**：Sema Code 把 client rendering/channel、UI-free core engine 与
  model/tool/MCP services 分层，client 只订阅 typed event stream。engine 内又把 tenant instance、
  agent-local state 与 session-global abort/permission 分开；processing 时输入进入 FIFO，普通消息可
  batch、command 单独执行；long Context 在 75% 阈值触发 summary，失败时按 assistant boundary
  deterministic truncation。read-only tools 可并行，含 write 的 batch 全序列化。
- **State Ownership / Control and Data Flow**：client 拥有 presentation 与 approval interaction；core
  engine 拥有 session/queue/event/runtime state；每个 Agent 应拥有 local history/Todo/file-read state；
  session controller 拥有 abort 与 shared permission；service adapters 拥有 provider/tool/MCP protocol
  normalization；background manager 拥有 process lifecycle 与 observation handle。文件系统和外部
  service 仍是 authoritative environment，清空 in-process state 不能撤销已发生 side effect。
- **Implementation Details**：论文使用 Node.js `AsyncLocalStorage` 传播 per-engine resources，并在
  无 active context 时回退 global singleton；sub-agent depth 限一层，只回传最终 synthesized result；
  interruption 在 inference 后、tool 前、active tool 与 recursive boundary 四处检查；background task
  支持 proactive offload 与 timeout 后 takeover。permission 将 edit、shell、Skill、MCP 分层，结果为
  allow/deny/request；shell 先按 composed command head whitelist，再用 LLM static analysis；approval
  可 single-use、project-persistent、reject 或 corrective feedback。
- **Artifact / Revision Boundary**：current npm package 是 `sema-core` 2.0.7，公开 exports 为 core、
  types、events 与 MCP；current main 有 96 commits，GitHub tags 页面只显示 2026-04-16 的
  `docs-assets`，无可定位的论文代码 release。current `SemaCore`/`SemaEngine` 仍调用多个 global
  managers 与 singleton event bus；这可能是后续实现变化，也可能改变 instance-isolation surface。
  因缺 event-bound immutable commit，本审计不拿 current main 反证论文，但同样不把论文架构宣称
  当作当前稳定行为。
- **Evaluation Contract / Evidence**：论文只展示相同 engine package 驱动 VSCode extension 与
  Telegram/Feishu-oriented SemaClaw；前者覆盖单用户 compression/permission/background task，后者
  覆盖共享进程、queue 与 async approval。没有用户/请求数、throughput、tail latency、queue delay、
  context fidelity、tenant leakage test、permission false-positive/negative、crash recovery、horizontal
  scale 或 resource cost；“zero modification / mechanisms compose without interference”属于作者
  deployment observation，不是受控实验。
- **What It Proves / Does Not Prove**：公开 package 与两个 clients 证明 engine-first packaging 在
  功能上可行；它不证明 single-process multi-tenancy 达到安全隔离，不证明固定 `8000 token / 75%`
  compression 对不同 provider/model 正确，也不证明 event stream、WebSocket/gRPC、background
  processes 或 approval protocol 在故障下 durable/exactly-once。作者明确承认未做规模 stress、
  cross-language throughput/error recovery 和 horizontal-state synchronization。
- **Trade-offs / New Failure Modes**：复用 engine 减少产品复制并集中 policy，却扩大公共接口的
  compatibility、tenant isolation 与 blast radius。FIFO 保序但会 head-of-line block；semantic batching
  可能合并时间上不同的 user intent；summary/truncation 牺牲 evidence fidelity；全 write-batch
  serialization 安全但损失并行；global permission inheritance 减少 prompt fatigue，却可能给 sub-agent
  超出任务所需的 authority；background execution 解耦 observation，却新增 orphan process、retention、
  cancellation 与 crash-recovery 问题。
- **Where Previous Designs Still Apply / Alternatives**：单用户 CLI/IDE monolith、每 tenant 独立
  process、durable external workflow、stateless RPC service 与 channel-specific runtime 都是共存分支。
  process isolation 成本更高但故障/安全边界更强；event stream 适合 interleaved output，ordinary RPC
  仍适合短、确定调用；模型 summary 适合低风险 history，immutable artifact reference 适合代码、
  tool result 与需要精确回读的证据。
- **Evolution Relationship**：`Direct Evolution`：product-locked agent application → embeddable
  event-driven engine → multi-client runtime；`Layering / Dependency`：client/core 分离依赖 typed event、
  session identity、permission 与 lifecycle contract；它不替代 Workflow durability、Multi-Agent
  delegation policy 或 MCP trust boundary。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch74、Ch77～80。Ch74 已覆盖 proposal/
  execution、permission、interrupt/retry；Ch77 已覆盖 durable state、cancellation 与 background work；
  Ch78 已覆盖 local/shared state、bounded delegation；Ch79 已覆盖 MCP 不等于 authorization；Ch80
  已用 Agent definition/run 与 control/execution/evidence planes 定义 platform boundary。engine/client
  decoupling 是这些既有机制的具体 packaging case，没有形成新的长期缺口；主 owner 为 Ch80。
- **Integration Decision / Open Questions**：`No Change — Already Covered`。不把 production-ready、
  strict isolation、zero residue 或 cross-model uniformity 写入 Books。待核验 event-bound commit、
  instance/global manager boundary、tenant leakage/stress、compression fidelity、crash recovery、
  sub-agent least privilege、network backpressure 与 horizontal scale。

### OccuBench — 24/30

- **Candidate / Week / Source Family**：`OCCUBENCH-LANGUAGE-ENVIRONMENT-SIMULATION`；W16；
  arXiv 2604.10866，v1 于 2026-04-13 00:27 UTC 首次公开，v2 于 2026-04-16 更新；v1 的
  `Language World Models / LWM` 在 v2 改称 `Language Environment Simulation / LES`，但没有形成
  新事件。论文两版、全部正文、作者 repository、382-row dataset 与公开 reimplementation 于
  2026-08-10 核验。
- **Access / Full-read Coverage**：已覆盖 motivation、LES formulation、environment configuration、
  multi-agent synthesis/filtering、100 scenarios/65 domains/382 instances、fault injection、15-model
  evaluation、reasoning-effort 与 severity ablations、cross-simulator analysis、case studies、related
  work、limitations、repository harness、simulator/fault/verifier code 和 Hugging Face dataset schema。
  论文无 appendix；hardware、sampling、API snapshot、token/latency/cost、repeated seeds 与 confidence
  interval 为 `Not Disclosed`。
- **Original Problem / Previous Design**：真实 API、desktop、code repository 或人工 simulator 能给出
  较强 state fidelity 与可重复 transition，对窄域和高风险任务仍是最可信旧分支；但每增加一个医疗、
  金融、制造或公共服务 domain，都要建设环境、数据和 verifier，且许多系统不可公开访问或不能承受
  真实副作用。静态 QA 又看不到多步 tool use、恢复和 accumulated state。
- **Changed Constraint / Mechanism**：LES 用
  `c=(system_prompt, tool_schema, initial_state, state_description)` 配置 LLM simulator；Agent action 与
  历史上下文驱动下一条 JSON observation，latent state 由 simulator 在 context 中隐式维护。生成流程
  先产生 scenario/config/instruction/tool/solution/rubric，再以有计划和无计划 Agent 运行、三票 verifier、
  repair 与 `0%/100%/invalid` filtering；每题保留 autonomous success 最低的难度版本以提高区分度。
- **State Ownership / Control and Data Flow**：benchmark owner 拥有 task、initial state、tool schema、
  fault policy 与 rubric；simulator context 只拥有 derived latent state 和 observation，不是现实业务
  truth；Agent 拥有 action trajectory；model judge 输出三票 verdict，evaluation pipeline 聚合 completion
  rate。若 simulator 发明、遗漏或错误转移状态，Agent 无法仅靠 policy 修复 measurement apparatus，
  因而 simulator identity、prompt、history 与 revision 必须进入 EvalSpec。
- **Implementation Details / Artifact Boundary**：每个环境含 2～10 tools（median 5），最终任务平均
  5.5 tools、16.2 calls。E1 注入显式 timeout/500/refused/unavailable，E2 注入 valid-JSON 的截断、缺失、
  null 或 stale data，E3 混合二者；fault 通过追加 simulator system prompt 实现，默认 count/duration
  均为 2 且 transient。公开 verifier 用同一 trajectory/rubric 做 3-vote majority。作者明确说明论文
  内部 evaluation system 依赖未公开 proprietary agent framework，GitHub 只是 clean standalone
  reimplementation；repository 仅 10 commits、无 release，因此公开代码不能证明论文 harness 的
  bitwise reproducibility。
- **Evaluation Contract**：默认 simulator 为 Gemini-3-Flash-Preview，15 个 Agent model 在可用时开启
  thinking，可配置者用 high effort；completion rate 在 382 instances 上聚合，robustness 定义为
  `min(CR_E1, CR_E2, CR_E3) / CR_E0`。fault 结果在作者协议下显示 silent degradation 平均比显式
  error 更难；severity 只在 3 个模型上检查。cross-simulator 子实验用 8 个 Agent 和 3 个 simulator，
  同一 Agent 的绝对 completion 会大幅变化，pairwise model ordering 也并非全部保持。
- **What the Evidence Proves**：在合成任务与作者 harness 下，语言 simulator 能低工程成本扩展多域
  tool-interaction coverage；显式与隐式 fault taxonomy 能暴露“遇错即停”“重试不足”和“接受不完整
  数据”等不同恢复失败。cross-simulator 结果反而提供了最重要的机制证据：强 Agent 不等于强
  simulator，environment model 是 measurement system，而非可忽略的中性容器。
- **What It Does Not Prove**：scenario 映射职业名称不证明真实职业胜任力、医疗/安全/法律正确性或
  deployment autonomy。implicit LLM state 不保证 deterministic transition、完整约束或 physical
  fidelity；作者案例已出现 simulator 发明额外 rooms、遗漏 entity 和添加规则。没有 domain-expert /
  human calibration、real-environment anchor、independent verifier、cost-matched reasoning ablation 或
  完整复现 harness。以最低 autonomous-success 选择难度还把特定 generator/Agent 的 selection bias
  写入 benchmark；“增加 reasoning compute 是可靠策略”不能由未匹配 token、latency 与成本的两模型
  ablation 外推。
- **Trade-offs / New Failure Modes**：获得 domain coverage、低构建成本、controlled faults 与完整
  trajectories；付出 simulator stochasticity、context-state drift、prompt leakage、shared-model blind
  spot、judge correlation 和重跑成本。新增 failure modes 包括 impossible task、rubric/simulator
  disagreement、Agent 适应 simulator quirks、跨 simulator 排名翻转、silent fault 与自然模型错误无法
  区分，以及更新 simulator 后历史 score 失去可比性。
- **Where Previous Designs Still Apply / Alternatives**：deterministic simulator 适合规则可形式化和
  release-blocking invariants；real environment/shadow 在可承受风险时提供更强 construct validity；
  human/domain-expert review 适合不可逆高风险 outcome；LES 更适合早期 coverage expansion 和故障假设
  生成。hybrid 方案可用 deterministic state machine 拥有 truth、LLM 只生成自然语言 observation，或
  用多 simulator disagreement 发现脆弱 slice，但 ensemble 不能在 correlated error 下自动成为 truth。
- **Evolution Relationship**：`Direct Evolution`：static answer benchmark → hand-built interactive
  environment → configurable language simulator；`Layering / Dependency`：LES 仍依赖 task/rubric、
  verifier、trace、fault policy 与 real-world anchor；`Principle Reuse`：fault injection 从 distributed
  systems 测试迁移到 Agent evaluation，但 prompt-injected fault 不等于真实 network/service failure。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch61～63、Ch68 与 Ch77。Ch62 已覆盖
  subject/environment identity、executable simulator、judge calibration、trajectory outcome、offline→
  shadow/canary 和 failure evidence；缺口是把 simulator 本身提升为需单独验证的 evaluation subject，
  并把 simulator fidelity、cross-simulator disagreement 与 real-environment anchor 写进 construct-validity
  contract。主 owner 暂定 Ch62；Ch68 只承接高风险 domain 不得外推，Ch77 承接 fault/retry workflow。
- **Integration Decision / Open Questions**：provisional `Refine — Existing Argument (Experimental)`；
  Historical Books Gate 关闭，暂不写正文。待核验 event-time proprietary harness、domain-expert
  validation、simulator calibration set、deterministic invariant checker、API/model snapshot、seed/variance、
  total token/latency/cost，以及同任务在真实或 hand-built environment 中的 rank/behavior agreement。

### Agentic Aggregation — 25/30

- **Candidate / Week / Source Family**：`AGGAGENT-PARALLEL-TRAJECTORY-AGGREGATION`；W16；
  arXiv 2604.11753，唯一 v1 于 2026-04-13 17:26 UTC 首次公开。33 页 PDF 全文、Appendix A～C、
  prompts/cost/latency/trajectory statistics、作者 repository、PyPI-oriented package surface 与公开
  rollout collection 于 2026-08-10 核验。
- **Access / Full-read Coverage**：已覆盖 formulation、MV/WMV/BoN/FewTool/SolAgg/SummAgg、四项
  trajectory tools、六 benchmarks、三 model families、主结果、cost/latency、strong-aggregator、
  synthesis-vs-selection、tool-use analysis、qualitative cases、implementation、pricing、bootstrap、judge
  prompt 修正、全部扩展表/图与 published rollouts。论文没有独立 Limitations section；未报告
  tool-component ablation、retrieval recall、adversarial/corrupted trajectory、privacy 或 production failure。
- **Score Correction**：`26→25/30`（SI `5→4`、PV `5→4`、L `3→4`）。外部 evidence navigation
  是长期机制，但作者证据仅覆盖 completed search/deep-research trajectories；它没有验证含副作用的
  live workflow、durable state、tenant isolation 或 streaming aggregation，不能按通用 runtime 影响计 5 分。
- **Original Problem / Previous Design**：single rollout 对 latency/cost 敏感且可能漏掉证据；并行
  sampling 增加正确或互补候选，却把瓶颈从 generation 转成 aggregation。短、closed-form answer
  仍可用 majority/self-consistency；只读 final answer 的 solution synthesis 便宜，逐轨迹 summary 可压缩
  长 history。旧方案在答案同质、错误较独立或 context 足够时仍合理。
- **Changed Constraint / Mechanism**：长轨迹含 reasoning、tool call 和 observation，直接拼接 K 条会
  超 context，预摘要又不可逆丢信息。AggAgent 因而只在初始 context 放 task 与每条 trajectory 的
  steps/tokens/tool metadata，把完整 trajectories 留在外部 array；先 `get_solution`，再以
  `search_trajectory` 对单轨迹做 ROUGE-L keyword ranking，必要时 `get_segment` 读取连续 steps，最后
  `finish` 产生新 synthesis，而不是必须选择某条原答案。
- **State Ownership / Control and Data Flow**：rollout workflow 拥有 immutable trajectory 与 tool
  observation；trajectory store/index 是 evidence plane；Aggregator 只拥有 query/read cursor、working
  context、selection rationale 与 synthesized output，不能改写原始 run。最终 answer 是 derived artifact，
  必须保存其使用的 trajectory IDs、segments、aggregator model/prompt/budget 和 conflict decisions，
  否则无法判断是新证据综合还是 shared hallucination。
- **Implementation Details / Revision Boundary**：论文统一使用 Tongyi DeepResearch scaffold、native
  function calling、temperature 1.0、top-p 0.95、128K context、10K max output 与每 rollout 最多 100
  tool calls；到限后仅允许一次无 tool final answer。current package 暴露同样四个 tools，但默认
  approximate aggregation budget 为 102,400 tokens，超限强制 `finish`；这是 current main surface，
  不反写为 event-time 实验设置。repository 仅 4 commits、无 release；作者已发布四类 HF rollouts，
  BrowseComp 两类因 contamination 风险改由 Google Drive 分发。
- **Evaluation Contract**：每 task 先生成 N=8 independent trajectories，再 bootstrap K∈{1,2,4,8}；
  LLM aggregation 的组合数最多采样 3。样本为 BrowseComp/BrowseComp-Plus/DeepSearchQA 各 150、HLE
  155、Healthbench-Hard 100、ResearchRubrics 101。三 backbone 为 GLM-4.7-Flash 30B、
  Qwen3.5-122B-A10B、MiniMax-M2.5 229B，同模型默认同时 rollout/aggregate。除本地 100,195-document
  BrowseComp-Plus 外，search/visit 使用 Serper/crawl4ai。judge 为 ResearchRubrics 上的
  Qwen3.5-397B-A17B、其余 GPT-4.1；作者因原 prompt 假阳性和 negative-rubric 不可靠而修改两类 judge
  prompt。全部实验称使用 4×H100；顺序 latency 子集对 GLM 用 2×H100，其余 4×H100，只测 30 例 median。
- **What the Evidence Proves**：在作者抽样、价格和 judge contract 下，按需读取原始 trajectory
  segments 相对只读 final answer、压缩 summary 和浅层 heuristic 提供一致的平均增益；synthesis-vs-
  selection ablation 支持开放式 report 的价值分散在不同 trajectories，而 exact-answer task 更可能由
  single winner 覆盖。aggregator overhead 在 K=8 作者测量中低于逐轨迹 summary，但总 system cost 与
  latency 仍随 K 个 rollouts 增长。
- **What It Does Not Prove**：`full fidelity` 只表示 stored trajectory 未预先摘要，不表示 Aggregator
  读到了所有 evidence；keyword/ROUGE-L search、单 trajectory 查询、有限 context 和 early finish 都会
  造成 retrieval miss。超过 Pass@8 的个例/分数不证明 synthesis 创造了 ground truth，也可能组合
  correlated false evidence。judge prompt 被作者修改且开放式任务依赖 model judge，缺少 human/executable
  calibration；bootstrap 复用同一 N=8 pool，LLM aggregation 每 K 最多 3 combinations，不能当作大样本
  稳定性。无并发 SLO、memory/storage/IO、straggler/cancellation、sensitive trace 或 side-effect evaluation。
- **Trade-offs / New Failure Modes**：相对全量拼接，externalized evidence 保留可回读原文并控制 active
  context；代价是 index/query budget、lineage 和 derived-answer provenance。新 failure modes 包括错误
  keyword 导致关键 minority evidence 不可见、metadata/answer anchoring、挑选支持既有假设的 segments、
  source duplication 造成伪共识、malicious trajectory prompt injection、aggregator bottleneck、K-rollout
  straggler 与同模型 correlated error。更强 aggregator 还新增成本、供应商与 authority concentration。
- **Where Previous Designs Still Apply / Alternatives**：exact-answer 且错误较独立时 voting 最便宜；
  verifier 可执行时 Best-of-N + deterministic check 更可信；轨迹短时直接拼接减少 retrieval miss；
  long-form/互补证据适合 synthesis；高风险 conflict 应升级 human。streaming aggregation 可提前处理结果，
  但会引入 arrival-order bias 与 incomplete-set semantics；hierarchical aggregation 可扩 K，却增加多层信息损失。
- **Evolution Relationship**：`Direct Evolution`：single rollout → parallel candidates + vote/select → final-
  answer synthesis → summary aggregation → external trajectory evidence + on-demand synthesis；
  `Layering / Dependency`：它依赖 Workflow 产出 immutable traces、Evaluation 定义 scorer，Multi-Agent
  层只负责如何分配 rollout 与 aggregator 责任；不是“更多 Agent 必然更强”。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch62、Ch76～79。Ch78 已覆盖 single-agent
  baseline、coordination tax、independent exploration、central verification、aggregation rubric 与 correlated
  consensus；缺口是“不要把所有 peer history 塞进共享 context”，以及把 trajectory archive 明确成
  read-only evidence environment、把 synthesis 与 selection 作为不同 output contracts。主 owner 暂定
  Ch78，Ch62 承接 judge/Metric@K 边界，Ch77 承接 immutable run 与 straggler/cancellation。
- **Integration Decision / Open Questions**：provisional `Refine — Existing Argument (Experimental)`；
  Historical Books Gate 关闭，暂不写正文。待核验 per-tool ablation、segment retrieval recall、independent
  human/executable judging、malicious/corrupted trajectories、model-family diversity、total-cost-matched
  sequential search、K≫8、streaming/straggler、tenant isolation 与 provenance-aware synthesis。

### ClawGUI — 24/30

- **Candidate / Week / Source Family**：`CLAWGUI-GUI-AGENT-LIFECYCLE-HARNESS`；W16；arXiv
  2604.11784，唯一 v1 于 2026-04-13 17:52 UTC 首次公开；repository 将论文入口记为 04-14，是
  时区/页面日期差异，不形成新事件。论文 HTML 全文、RL/Eval/Agent 三模块、current repository 与
  public evaluation/model artifact 入口于 2026-08-10 核验。
- **Access / Full-read Coverage**：已覆盖 related work、Environment Manager、virtual/real-device
  backend、binary/PRM reward、GRPO/GiGPO、Infer→Judge→Metric、hybrid CLI/GUI、persistent memory、
  remote/local control、training/evaluation setup、reward ablation、benchmark reproduction、discussion 与
  current module docs。论文没有独立 Limitations、seed/variance/significance、PRM calibration、failure-
  recovery experiment、large-scale real-device training、deployment SLO/security/privacy 或 user study。
- **Score Correction**：`26→24/30`（TN `4→3`、SI `5→4`、PV `5→4`、L `3→4`）。环境管理、评估
  分层和 deployment packaging 有长期价值，但核心算法来自现有 GiGPO/verl/MobileWorld，实验证据只
  覆盖 virtual training 与 benchmark reproduction；不能以功能组合替代真机规模和生产验证。
- **Original Problem / Previous Design**：GUI policy 只在静态 SFT 或单 emulator 中研究时，环境状态
  可人工恢复、评测参数可由单论文固定，demo 也不必承担真实副作用；进入 online RL 后，长 episode、
  container drift、稀疏 terminal reward 和大量并行 devices 让 environment failure 直接污染 gradient。
  纯 CLI 在有稳定 API 时仍更快、可审计；GUI 适合 long-tail app，但 action 更多且观察更脆弱。
- **Changed Constraint / Mechanism**：ClawGUI 把环境抽象为统一 reset/action/observation/reward/
  termination interface。virtual backend 在 task 前 reset，以 root/database state + final-screen MLLM judge
  验证结果，维护 spare-server queue 并周期 teardown；real device 使用人工任务和 final-screen MLLM judge，
  因没有 root truth 而降低验证强度。训练将 episode outcome 与逐 step PRM 相加，GiGPO 再以同 task
  episode group 和相同 anchor state subgroup 计算 macro/micro relative advantages。
- **State Ownership / Control and Data Flow**：Environment Manager 拥有 device/container lease、health、
  reset generation、task assignment 与 backend identity；真实 app/database 才拥有 authoritative state，
  screenshot/MLLM verdict 是 observation/measurement。trainer 拥有 policy/rollout/logprob/advantage；PRM
  和 completion judge 拥有 derived reward。failover 若换到新 device，必须产生新 environment generation
  并从 clean task state 重开，不能把不同 world state 下的 suffix 当作原 trajectory 无缝 resume。
- **Implementation Details / Revision Boundary**：论文的训练使用 MAI-UI-2B、64 parallel virtual
  environments、8×A6000 48GB、group size 8、temperature 0.7、learning rate 1e-6、3 epochs、batch 8，
  PRM 为 Qwen3.5-72B。current RL docs 显示 Ray single-controller、FSDP workers、vLLM rollout、weight
  broadcast、server URL pool、restart/retry 和 episode replay，并称只在两台真机验证、未验证大规模真机
  训练。current master 已有 211 commits、无 release，后续新增 Skills/on-device app 等内容不反写为
  W16 论文机制；缺少 event-bound tag 使 exact historical artifact identity 不完整。
- **Evaluation Contract**：训练后的 ClawGUI-2B 只在 MobileWorld GUI-Only 117 tasks、max 50 steps 上
  测试。表中 GRPO+binary 得 14.5，GiGPO+dense 得 17.1；由于 algorithm 与 reward source 同时改变，
  这不是 GiGPO-only 或 PRM-only ablation。ClawGUI-Eval 覆盖 6 benchmarks/11+ models，但 reproduction
  统计只对有 official baseline 的 48 cells；`|delta|<=2%` 或 reproduced≥official 都算成功，得到 46/48，
  是作者定义的 tolerance hit rate，不是 exact reproduction、statistical equivalence 或 end-to-end navigation。
- **What the Evidence Proves**：公开代码和 virtual experiment 支持“环境 lifecycle 是 online Agent RL
  的一等系统对象”，以及 inference、judge、metric 分离能让旧 predictions 在 parser/judge 更新后重算。
  作者协议下的两配置差异说明 dense/process-aware reward 值得继续研究，但不能隔离具体贡献。公开
  modules 证明 functional integration 可运行，不证明声明的 production readiness。
- **What It Does Not Prove**：没有证据表明 64 virtual env 的收益来自 spare rotation、PRM、GiGPO 或
  其他配置中的哪一项；没有 simulator→real transfer、两台真机的任务数/训练曲线/故障率、HarmonyOS/
  iOS training、长期 user traffic 或 device diversity。final screenshot judge 看不到后台副作用、错误对象、
  中途越权或恢复后残留。自动抽取 contacts/preferences 并写 vector memory 没有 consent、authorization、
  delete/supersession 或 poisoning evaluation。`production-ready`、任意 app coverage、model scale 不如 RL
  和 95.8% 可比性均超出证据。
- **Trade-offs / New Failure Modes**：统一 interface 降低 backend 接入成本，却可能掩盖 virtual root
  verifier 与 real-device visual judge 的不同证据强度。spare rotation 提高吞吐但新增 lease、generation、
  task reset、duplicate episode 和 reward attribution 问题；PRM 增加 reward density，也引入 judge cost、
  correlated visual error 与 reward hacking；hybrid CLI/GUI 扩大 coverage，却要求跨 modality identity、
  authorization、side-effect dedup 和 replay；persistent memory 进一步扩大隐私与长期污染 blast radius。
- **Where Previous Designs Still Apply / Alternatives**：稳定 API/CLI + deterministic verifier 仍适合
  高副作用任务；single emulator 适合可复现调试；virtual fleet 适合规模化探索；真机适合 transfer/
  hardware/app validation，但需人工或 application-level oracle。binary outcome 在 verifier 很强和 horizon
  较短时简单可靠；dense PRM 只在经过独立 calibration 且收益超过额外偏差时使用。train、eval、deploy
  可以共享 artifact schema，而不必共用同一个大仓库或把配置等同为语义一致。
- **Evolution Relationship**：`Direct Evolution`：single sandbox + terminal reward → managed virtual fleet
  + health/reset/failover → real-device backend with weaker observable truth；`Layering / Dependency`：training
  environment、EvalSpec 和 deployment policy 共享 identity/evidence contracts，但不是一个 benchmark
  成功就自动晋级生产；`Principle Reuse`：spare rotation 借用 distributed worker failover，新增约束是
  trajectory/world-state consistency。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch27～30、Ch62、Ch68、Ch73/74/77/80。
  Ch29 已覆盖 grouped rollout、reward measurement、policy lag 与 trajectory lifecycle，但尚未明确 online
  environment 的 reset/health/lease/generation/failover 也是训练 state，且 backend abstraction 不保证
  verifier semantics 相同。主 owner 暂定 Ch29；Ch62 只承接 Infer/Judge/Metric 与 evidence-strength
  contract，Ch80 承接 real-device run、memory、authorization 和 rollout-to-production gate。
- **Integration Decision / Open Questions**：provisional `Refine — Existing Argument (Experimental)`；
  Historical Books Gate 关闭，暂不写正文。待核验 event-time commit/tag、GiGPO-only 与 PRM-only factorial
  ablation、PRM/human agreement、environment-failure rate 与 failover semantics、seed/CI、sim-to-real、
  large-scale multi-device training、后台 side-effect verifier、memory/privacy controls 与 deployment SLO。

### Rethinking On-Policy Distillation — 25/30

- **Candidate / Week / Source Family**：`OPD-STUDENT-STATE-DISTRIBUTION-ALIGNMENT`；W16；arXiv
  2604.13016 只有 v1，首次公开于 2026-04-14 17:54 UTC。论文 HTML 全文、Appendix A～D、作者
  OPD/verl/LLaMA-Factory artifact、公开 checkpoints/datasets 入口于 2026-08-10 核验；仓库后续把
  diagnostics 合入 verl 及 workshop 接收属于 revision context，不反写为 W16 事件。
- **Access / Full-read Coverage**：已覆盖 reverse-KL 与 sampled/full-vocabulary/top-k objectives、三项
  dynamic metrics、teacher/student pattern 与 knowledge comparisons、reverse distillation、shared-token
  ablation、cold-start SFT、prompt template/content selection、trajectory-depth experiments、global/local
  reward analysis、support-size ablation、全部训练参数、benchmark breakdown、overlap-mass diagnostics、
  dedup protocol 与 teacher-entropy appendix。论文没有独立多-seed/CI/significance、non-math domain、
  tokenizer mismatch、wall-clock/FLOP/memory、distributed failure 或 production SLO evaluation。
- **Score Correction**：`27→25/30`（TN `5→4`、SI `5→4`）。论文对 OPD 的局部机制和失败条件提供
  了强于发布摘要的系统证据，但全部实证来自小型 Qwen/DeepSeek-family math reasoning，且“gradient
  anisotropy”被作者明确标为未验证 hypothesis；不能把 domain-local diagnostic 提升为通用蒸馏定律。
- **Original Problem / Why Previous Design Was Reasonable**：off-policy SFT 使用固定 teacher traces，
  简单、可缓存且便于复现，但 student 部署时会访问训练集中未出现的 prefixes；OPD 改为让 student
  rollout，再让 teacher 在相同 prefix 上提供 token-level dense signal，以减轻 exposure bias。更强 teacher
  和更密 supervision 在短程、分布相近时是合理选择，但 teacher benchmark 更高不保证其在 student-
  visited states 上给出可利用的局部更新。
- **Changed Constraint / Mechanism**：关键约束不是参数规模，而是 teacher 与 student 在当前 state 的
  high-probability support 是否重合，以及 teacher 是否拥有 student 尚未学到的 capability。论文监控
  top-k overlap ratio、overlap-token advantage 和 entropy gap；成功 run 中 shared tokens 承载双方
  97%～99% probability mass，overlap 约从 72% 升至 91%，且只优化 shared top-k 基本匹配 student
  top-k。失败时可先用 200K teacher rollouts 做 full-parameter SFT cold start，或选择 teacher post-
  training-aligned prompts，使 rollout state 进入 teacher 可提供稳定 signal 的区域。
- **State Ownership / Control and Data Flow**：student policy 拥有 rollout state distribution 和 sampled
  prefixes；teacher checkpoint 只在这些 prefixes 上产生 target logits，不拥有 student trajectory；
  dataset/template selector 决定初始 state support；trainer 拥有 objective variant、top-k/support mask、
  token reduction、teacher/student checkpoint identity 与 optimizer state。overlap/entropy 是 derived
  diagnostics，不是能力真值或可替代 downstream evaluation 的 control signal。
- **Implementation / Evaluation Contract**：默认 OPD 为 global/mini batch 64、4 rollouts、student
  top-k=16、max prompt/response 1024/7168、temperature/top-p 1.0、lr 1e-6、1 epoch、KL coefficient 0，
  所有实验在 8×A800 80GB。评估仅 AIME 2024/2025、AMC 2023，validation 以 temperature 0.7、
  top-p 0.95、最多 31,744 response tokens 采 16 条并报 avg@16。cold start 另用 Qwen3-4B 生成
  200K OpenThoughts3 math traces，max 12,288，过滤 incomplete/repetitive 后，以 BF16、sequence
  length 14,336 完成 Qwen3-1.7B full SFT。仓库公开 OPD/GRPO scripts、checkpoint 与 grading pipeline，
  但当前 27 commits、无 event-bound release；实现可运行不等于所有论文图表可一键重现。
- **What the Evidence Proves**：在作者构造的 math/model-family 配对中，teacher/student 的局部
  distribution compatibility 与 teacher-added post-training capability 比 teacher headline score/size 更能
  解释 OPD outcome；reverse distillation 还显示 OPD 会覆盖 student 已有 thinking pattern。shared-token
  support ablation、cross-pair appendix 与 length sweep 支持“supervision 的可利用性随 visited-state 和
  horizon 改变”，并给出 cold-start/prompt selection 两种受限恢复路径。
- **What It Does Not Prove**：97%～99%、72%→91%、3K/7K sweet spot 和 1-token sufficiency 都绑定
  top-k=16、这些模型/数据/长度与实现，不能外推到 code、tool use、多轮 Agent 或不同 tokenizer。
  prompt-content 对照虽做 exact + embedding threshold 0.6 去重，仍把 teacher familiarity、domain slice
  与潜在 pretraining contamination 混在一起。sequence reward AUROC 相近只表明 global correlation，
  不证明 per-token gradient direction；anisotropic cancellation 未被直接测量。没有 total-compute-matched
  SFT/RL、seed variance、capacity sweep、failure recovery 或 online service evidence。
- **Trade-offs / New Failure Modes**：OPD 避免固定-trace exposure bias，却增加 teacher forward/logit
  transport、checkpoint/tokenizer compatibility 和长 trajectory storage；full vocabulary 为 `O(BTM)`
  memory，top-k 截断丢失 tail mass，sampled token 方差更高。cold start 提高 support overlap，却重新引入
  off-policy imitation 和 teacher bias；teacher-aligned prompts 提高局部可学性，却会压低 student entropy
  并缩窄 coverage。长 trajectory 上 teacher 被迫评价越来越陌生的 student prefixes，suffix instability
  可向前传播，dense reward 因而不是免费午餐。
- **Where Previous Designs Still Apply / Evolution Relationship**：高质量 fixed demonstrations 在可缓存、
  短任务和 student/teacher gap 大时仍是稳健起点；outcome RL 在 verifier 可靠且需要探索时仍保留；OPD
  适合 teacher 在 student states 上有新增且可利用 signal 的阶段。`Direct Evolution`：fixed teacher trace
  imitation → student-state OPD → compatibility diagnostics → cold-start/prompt-conditioned hybrid；
  `Layering / Dependency`：data/template 选择、checkpoint lineage 与 distributed logit path 共同定义训练
  contract，新方法不是对 SFT 或 RL 的单向替代。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch24～26、Ch29。Ch25 已覆盖 cascade
  distillation、same-prefix context distillation、teacher snapshot/cadence 与 objective contract，但仍把
  student-state coverage 写得偏正向；缺口是明确区分 **global teacher quality** 与 **local gradient
  exploitability**，把 support overlap、teacher novelty、horizon drift 和 cold-start entropy/coverage 作为
  选择 OPD 的门槛。主 owner 暂定 Ch25；Ch29 只短接 rollout horizon 与 dense/process reward 边界。
- **Integration Decision / Open Questions**：provisional `Refine — Existing Argument (Experimental)`；
  Historical Books Gate 关闭，暂不写正文。待核验 non-math/agentic replication、matched-compute baseline、
  tokenizer/cross-architecture ablation、seed/CI、full-vocab vs sampled/top-k 的 end-to-end cost、directional
  gradient test，以及 2026-07 privileged self-distillation 的相反结果应形成何种跨周 evolution family。

### Toward Autonomous Long-Horizon Engineering / AiScientist — 26/30

- **Candidate / Week / Source Family**：`AISCientist-LONG-HORIZON-ML-ENGINEERING`；W16。官方
  repository 记录 initial public release 为 2026-04-13，因此 event date 从 arXiv v1 的 04-14 修正为
  04-13，但不改变 ISO week。arXiv 2604.13018 截至本次审计只有 v1。
- **Direct and Related Primary Sources / Access**：已读 arXiv HTML 全文，包括 problem setup、system
  design、PaperBench/MLE-Bench experiments、ablation、failure discussion 与 conclusion；核验作者
  repository README、workspace/job layout、Docker sandbox 及当前 `inspect`/`resume`/`export` surface。
  当前仓库晚于事件日的变化仅用于理解 artifact semantics，不反写成论文当时已经具备的机制。
- **Original Problem / Previous Design / Changed Constraint**：单个 long-context coding Agent 把 plan 与
  conversation 留在 context 中，对短任务是合理方案。24 小时 ML paper reproduction 同时引入 context
  turnover、相互依赖的代码/实验、specialist re-entry、失败和部分进度；反复传递完整 transcript 或不断
  加长 summary 会让 controller 同时成为 context bottleneck 与脆弱的事实状态 owner。
- **Mechanism / State Ownership / Control and Data Flow**：AiScientist 采用 `thin control over thick state`。
  顶层 orchestrator 读取 compact workspace map 与 stage summary，再调用 permission-scoped specialists；
  specialists 从共享 filesystem 中的 `paper_analysis`、`submission`、prioritized tasks、plan、implementation/
  experiment logs 与 artifacts 重新落地。Tier-1 specialists 可有界派生 Tier-2；private context 可丢弃，
  workspace 才是 durable system of record，append-only logs 跨 invocation 传递 evidence。循环是
  comprehend/prioritize -> scaffold -> implement/run -> diagnose/patch -> revalidate。
- **Implementation and Evaluation Contract**：PaperBench 使用全部 20 个任务、Gemini-3-Flash 与 GLM-5、
  matched BasicAgent/IterativeAgent baselines 及 GPT-5.4 grader；MLE-Bench Lite 使用 22 个任务并比较
  AIDE、LoongFlow、ML-Master 2.0，leaderboard 数字只作背景。每个任务一张 H20、24 小时预算。
  PaperBench full 分数为 30.52/33.73，平均成本 15.67/12.20 USD；两个 backbone 在该 MLE subset 上均为
  81.82% Any Medal。这些数字只在此 model/task/hardware/time/grader contract 内成立。
- **Ablations / What Evidence Proves**：移除 File-as-Bus 后，作者报告 PaperBench 下降 6.41、MLE Any
  Medal 下降 31.82 个百分点，支持 durable artifact-mediated coordination 是该实现的重要组成部分。
  hierarchy 贡献主要由与 non-hierarchical systems 的比较推断，不是独立 hierarchy-only factorial
  ablation。File-as-Bus ablation 又同时改变 files、permissions、durable logs 与 prompt/tool interface，
  无法隔离究竟哪个子机制带来收益。
- **What It Does Not Prove / Limitations**：未披露 repeated seeds、CI 或 significance；PaperBench 依赖
  model grader，样本少且昂贵，MLE leaderboard comparison 也不是统一 harness 下的受控实验。论文未测
  concurrent writer conflict、stale/corrupt artifact、crash recovery、provenance enforcement、security/
  privacy、multi-tenancy 或 human approval。filesystem 因而不等于 transaction log、workflow engine
  或 trusted evidence store。
- **Trade-offs / Failure Modes / Coexistence**：externalized state 能跨 context reset 并帮助 specialist
  re-grounding，却新增 naming/schema drift、stale summary、ownership conflict、partial write、hidden
  ordering 与 sensitive artifact retention。短、低副作用任务仍可用 single Agent + compact transcript；
  长期或会改变外部状态的 Workflow 需要在 file layer 之上增加 versioning、atomic transition、lease/
  conflict policy、provenance、replay 与 rollback。
- **Evolution Relationship**：`Layering / Dependency`：in-context plan -> transcript summary -> durable
  artifact workspace -> typed/versioned workflow state。`Principle Reuse`：File-as-Bus 借用 blackboard/
  shared-state 模式，但除非 deterministic controller 拥有 authoritative transition，文件仍只是 data-plane
  artifact。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch76～78 与 Ch80。Ch77 已拥有 durable
  state、artifact、replay、idempotency 与 deterministic transition；Ch78 已区分 message 与 authoritative
  state 并要求 ownership/conflict rules；Ch80 已拥有 run identity 与 evidence plane。剩余长期缺口是把
  workspace map 明确为 authoritative state 上的 compact derived navigation view，而不是事实状态本身。
- **Integration Decision / Score Correction / Open Questions**：provisional `Refine — Existing Argument
  (Experimental)` in Ch77，Ch78 只作短 handoff；Historical Books Gate 仍关闭。Practical Value `5->4`、
  Longevity `3->4`，总分仍为 26，以区分 promising artifact evidence 与有限 production validation。
  待核验：加入 versioned writes、atomic commit、conflict handling、provenance、crash recovery 和非 model-
  judge verification 后，File-as-Bus 的收益能否在 repeated、total-cost-matched runs 中保持？

### AgentSPEX — 23/30

- **Candidate / Week / Source Family**：`AGENTSPEX-DECLARATIVE-WORKFLOW-HARNESS`；W16；arXiv
  2604.13346 唯一 v1 于 2026-04-14 23:16 UTC 首次公开。已核验 18 页 PDF、HTML 可读部分、全部
  Appendix A～E、官方 `ScaleML/AgentSPEX` repository、language guide/runtime layout 与 current run
  persistence surface；仓库无 release，当前 6-commit state 不作为 immutable event-time artifact。
- **Original Problem / Why Previous Designs Were Reasonable**：ReAct 把 control flow 与 state 留给模型，
  对短、开放任务实现成本低；Python graph/orchestration framework 把分支、重试和 memory 显式化，适合
  复杂类型、custom code 与成熟工程团队。约束变化在于 long-horizon workflow 需要 non-programmer 可读、
  可 diff 的规范，同时不希望模型在运行时重新解释整个流程，也不希望每次改 prompt 都侵入 Python runtime。
- **Mechanism / State Ownership / Control Flow**：AgentSPEX 以 YAML workflow 作为 executable
  specification，提供 `task/step`、`if/switch`、bounded `while`、`for_each`、`call`、`parallel/gather`、
  variable mutation、input 与 return。Interpreter 验证结构、解析参数/template、管理 recursion/scope，
  并为 operation 分配 hierarchical step ID；executor 只在 `task/step` 内运行 model-tool loop。`task`
  丢弃旧 conversation、通过 named variables 传递结果，`step` 保留多轮 history；workflow definition
  拥有 control flow，context store 拥有 named intermediate values，sandbox 拥有 tool side effects。
- **Composition / Harness / Data Flow**：workflow 可调用 workflow，也可注册成 agent-selected skill/tool；
  每次 run 在 Docker sandbox 中经 MCP 调用 50+ tools。模型 response、tool result、conversation state、
  metrics 与 sandbox snapshot 写入 trace/checkpoint；完成 step 后才 checkpoint，resume 恢复 context、跳过
  completed step 并重连原 sandbox。Selective replay 可固定 prior trace 的前若干 step 后继续 live execution。
- **Durability Boundary**：论文描述的是 step-boundary checkpoint，不是 exactly-once guarantee。若 tool
  在 step 中产生副作用后、checkpoint 前失败，resume 是否重复 action、sandbox 是否仍存在、外部 API
  outcome 如何 reconcile 均未定义。当前 README 的 timestamped run directory、run ID、persistent output、
  `--resume` 与 no-real-tool-call replay 提高可操作性，但这是 later current state，也没有补足 idempotency、
  checkpoint compatibility、migration、cancellation 或 compensation contract。
- **Evaluation Contract**：七个 benchmark 使用 pass@1：SWE-Bench Verified 500、AIME 2025 30、
  ChemBench 90-question stratified subset、SciBench chemistry 213、MMLU-Pro StemEZ physical chemistry 216、
  WritingBench 120、ELAIPBench 403。主要模型为 GPT-5，WritingBench 为 Claude-Sonnet-4.5-Thinking，
  SWE-Bench 为 Claude-Opus-4.5/4.6 high reasoning、temperature 1.0。CoT 与 ReAct 通常是对照；ReAct
  收到相同 workflow prompt 但不强制逐步执行。硬件、token/API cost、wall-clock、并发、seed/variance
  和生产 SLO `Not Disclosed`。
- **What the Evidence Proves**：在作者手写、coding-assistant 辅助的 workflow 与上述 harness 中，
  enforced execution 的七项 pass@1 都高于所列 comparator；Opus 4.5->4.6 时 AgentSPEX 在 SWE-Bench
  只变化 -0.2，而 mini-SWE-agent/Live-SWE-agent 分别 -1.2/-6.8。结果支持“显式 interpreter 可在这些
  workflow 中卸载部分 control-flow interpretation”，但不隔离 declarative syntax、context slicing、
  prompt content、tool budget、workflow quality 或 harness 的各自贡献。
- **User Study / Verification Boundary**：23 名均有 programming experience、agent experience 不同的
 参与者比较 AgentSPEX 与 LangGraph；前者在 readability、prompt visibility 与从零开始上更受欢迎，
  但复杂 multi-step workflow 多数选择 LangGraph。所谓 formal verification 只展示一个 7-node citation
  extraction plan/trajectory 的 inferred pre/postconditions 与 tool/schema checks；完整 theorem、soundness、
  coverage、adversarial path 和 verifier implementation evaluation 均不存在，论文也把正式 verification
  列为 future work。因此不得把示例写成“Agent workflow 已被形式化证明”。
- **What It Does Not Prove / Limitations**：没有 DSL-vs-Python matched implementation、component ablation、
  repeated run、developer productivity/time-to-fix、large-team maintenance、migration/versioning、安全、租户
  隔离或 failure injection。SWE-Bench comparator 混用了 published/local result，WritingBench 依赖 judge，
  science/math task 的 agentic horizon 有限；作者的 `production-ready` 描述没有 production workload、
  recovery、SLO 或 incident evidence 支撑。
- **Trade-offs / New Failure Modes / Coexistence**：DSL 降低 control-flow ambiguity 并使 spec 可 diff，
  代价是 expressiveness ceiling、schema evolution、template/type mismatch、parallel merge semantics、hidden
  escape hatch 与 visual/text round-trip drift。Python workflow 对复杂 custom logic、静态类型、成熟 testing
  与 debugger 仍合理；reactive loop 对短、探索性任务仍更轻。长期方向是 declarative stable core + typed
  extension boundary，而不是以 YAML 取代 general-purpose orchestration。
- **Evolution Relationship**：`Direct Evolution`：prompt-implicit flow -> Python-explicit graph -> declarative
  executable spec + interpreter；`Layering / Dependency`：language definition 不等于 durable runtime，后者仍需
  checkpoint identity、side-effect protocol、verification、policy 与 observability；`Principle Reuse`：借用
  workflow DSL/compiler 的 IR 思路，但 LLM node 的 probabilistic semantics 不能由 control-flow syntax 消除。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch76～80。Ch77 已明确 deterministic spine、
  model-driven nodes、durable event/state、replay、retry/idempotency/compensation 与 workflow testing；Ch78 已有
  typed handoff/parallel ownership，Ch79 已明确 MCP 不拥有 workflow reliability，Ch80 已有 definition/run
  identity 与 evidence plane。论文没有越过现有章节的长期机制，只提供一个受限 implementation case。
- **Integration Decision / Score Correction / Open Questions**：`No Change — Already Covered`，主 owner
  Ch77；不写 Books。TN `4->3`、SI `5->4`、PV `5->4`、SR `4->3`、L `3->4`，总分 `26->23`。
  待验证：在相同 workflow、tools、context/token budget 与 repeated seeds 下，单独强制 interpreter 是否仍
  带来收益；checkpoint-before/after-side-effect、parallel variable merge 和 schema migration 的真实语义是什么？

### Exploration and Exploitation Errors Are Measurable — 25/30

- **Candidate / Week / Source Family**：`MEASURABLE-EXPLORE-EXPLOIT-AGENT-TRAJECTORY`；W16；
  arXiv 2604.13151 唯一 v1 于 2026-04-14 17:59 UTC 首次公开。已读 36 页论文、全部公式与
  Appendix A～G、edge-case tables、prompt/harness/semantic experiments、additional runs/results，并核验
  官方 `jjj-madison/measurable-explore-exploit` repository、environment generator、metrics、agent variants、
  exported episode/trajectory/trace artifacts 与 tests；当前仓库 11 commits、无 immutable release。
- **Original Problem / Why Previous Designs Were Reasonable**：final success rate 对短、结果明确的任务
  成本低且容易比较；reference trajectory/process match 在存在唯一或专家路径时也合理。开放、部分可观测
  任务却允许多条有效路径，最终失败不能区分“未发现必要信息”与“知道后未利用”，固定 reference 又会
  把合理替代策略误判。作者因此只读取 action trajectory，不要求访问模型内部 policy/value。
- **Environment / State Ownership**：evaluator 生成 partially observable 2D grid 与 unknown symbolic task
  DAG。节点状态为 undiscovered/discovered/achieved，AND/OR edges 表示 prerequisite；Agent 每步只看到
  admissible moves 及当前格发现的 node relation。Evaluator 拥有完整 map、DAG、distance、unobserved set
  `U(t)` 与 prerequisites-satisfied pending tasks `P(t)`；Agent 只拥有 observation/context。故 metric 是
  **policy-agnostic 而非 environment-agnostic**，迁移到 coding/web/robotics 必须先定义可验证的 progress、
  frontier、dependency 与 state identity。
- **Mechanism / Formula / Control Flow**：根据 `P(t)`、`U(t)` 和 goal 是否 pending，evaluator 将当前
  opportunity 分为 exploration-only、exploitation-only 或 either，并构造 productive target set `T(t)`。
  action 若进入 target 或缩短到任一 target 的最短距离则有 gain；否则记 error。为避免对称 target 下无限
  oscillation 被漏掉，系统从最近一次 progress event 开始维护 no-progress segment，并计算 cyclomatic
  number `c_t`、edge 超过两次的 reuse `e_t`、node 超过两次的 revisit `n_t`；stale score
  `S_t=c_t+e_t+n_t` 增长时也记错。随后按 opportunity case 将同一错误归因 exploration、exploitation
  或两者，并分别用该 action type 可发生的 timestep 数归一化。
- **Why the Old Branch Still Applies / Metric Trade-off**：允许一次 probe/backtrack 和 gateway revisit，
  能避免“最短路径即唯一正确路径”；但阈值 2 来自 undirected graph exploration 与 node-level analog，
  在有向、动态、不可逆、代价不均或必须重复验证的现实环境未必合理。trajectory 决定自己经历多少
  opportunity，归一化 denominator 因 policy 路径而变，所以跨模型的 aggregate error 只能是 behavioral
  summary，不能独立充当整体质量分数或因果能力指标。
- **Evaluation Contract**：13 个模型、temperature 0；9 种 procedural map configuration（3 exploration
  levels x 3 DAG sizes），每格 3 seeds；8 个 prompt sets 合计每模型 216 episodes。DAG 为 4/6/8 nodes，
  density 0.1/0.25/0.4，corridor width presets，turn budget `B=3|O|`。Prompt variants 只改变一条 strategy
  sentence；harness experiment 使用同一 generated set。Semantic experiment 为 4 个 hand-crafted pasta
  maps、semantic/symbolic 两版、5 seeds、2 prompt sets，共每模型 80 episodes。硬件、token/cost、latency、
  API retry 和 model snapshot digest `Not Disclosed`。
- **What the Evidence Proves**：在这个 symbolic grid+DAG contract 中，log exploration error 与 success
  across tested models 的作者回归 `R^2=0.947`，exploitation error 为 `0.006`；这首先反映任务必须先发现
  node 的结构。相同 success 也可呈现不同 trajectory behavior。单句 explore/exploit prompt 会定向改变
  对应错误；rule-based memory manager 仅重组 history 可推导的 coordinate、visited/frontier、obstacle、
  discovered/activated/activatable state，就将 Gemini 3.1 Flash Lite success 51.9->88.9、GPT-4.1
  63.0->92.6，并同时减少两类 error 与 successful-run steps。
- **What It Does Not Prove**：上述数字不证明探索是所有 Agent 任务的通用主瓶颈，也不证明 structured
  memory 在语义、连续动作、多人、多工具或有副作用环境保持同幅收益。Harness 同时改变 state extraction、
  representation 与 prompt salience，没有拆分各组件。Semantic test 只有四个 pasta maps；同一语义使
  GPT-4.1 success 提升、却使 Gemini exploration 增加而 exploitation error 下降，说明 pretrained prior
  是策略组成而非可简单移除的 confounder。作者也承认 per-run/trajectory variance 与 weak demand-error
  correlation；三 seeds 不足以支撑通用模型排名。
- **Failure Modes / Evolution**：从 end outcome -> reference-step match -> environment-state-aware process
  metric，获得 failure attribution，却新增 oracle-state 依赖、opportunity denominator drift、progress-event
  misspecification、metric gaming 与 simulator-to-reality gap。更现实的演进应把 `raw trajectory + final
  outcome + evaluator-owned state reconstruction + uncertainty` 并存，而不是让 derived error 覆盖原始
  evidence；遇到 irreversible action、hidden side effect 或 changing world 时还需 domain verifier。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch62、Ch73～75、Ch77。Ch75 已有 partial
  observability、belief update、search/replanning，却没有把 exploration failure 与 exploitation failure 作为
  可测但 opportunity-conditioned 的 process taxonomy；Ch73 已说明 context 与 durable memory 边界；Ch77
  已拥有 authoritative workflow state。主 owner 暂定 Ch62，因为长期新增是 evaluation-object 与 metric-
  boundary 设计；Ch75 只需短 handoff，harness memory 不应重复写入 Ch73。
- **Integration Decision / Open Questions**：provisional `Refine — Existing Argument (Experimental)` in
  Ch62；Historical Books Gate 关闭，暂不写正文，分数保持 25。待核验：在真实 coding/web/tool trace 中，
  evaluator 如何在不知道完整 state/optimal path 时定义 `U/P/T`；如何用 matched opportunity、paired map、
  confidence interval 与 human labels 校准 metric；repeated action 何时是必要 verification 而非 stale error？

### Dive into Claude Code — 22/30

- **Candidate / Week / Source Family**：`DIVE-INTO-CLAUDE-CODE-DESIGN-SPACE`；W16；arXiv
  2604.14228 v1 于 2026-04-14 17:59 UTC 首次公开，v2 于 2026-07-02 修订。W16 事件只使用 v1；
  v2 新增 Hermes Agent comparison、后续 security/agent signals 与扩展 source notes，仅用于记录
  revision drift，不反向写成 4 月已有证据。
- **Access / Full-read Coverage**：已读 v1 的 46 页正文、architecture、query loop、permission、
  extensibility、context/memory、subagent、persistence、OpenClaw comparison、discussion、limitations、
  related work、package/evidence appendix；并对照 v2、作者 companion repository 及 Anthropic 当前
  公开的 agent loop、compaction、permission 与 subagent docs。没有把 current docs 当作 v2.1.88 的
  event-time code proof。
- **Source Type / Evidence Boundary**：作者来自 VILA Lab/MBZUAI/UCL，不是 Anthropic。研究对象是
  公开 package 中的 Claude Code TypeScript v2.1.88，加官方文档和 community analysis；Tier A
  product docs 可证明公开 contract/intent，Tier B static code 可定位结构、分支和 feature gate，Tier C
  reconstruction/comparison 只能支持推断。它不能确认某 flag 在 production 实际启用、路径出现频率、
  Anthropic 的真实 design intent 或未发布行为，也不是官方 security audit。
- **Original Problem / Previous Design**：autocomplete、单轮 assistant 与一个简单 reactive `while`
  loop 对短、低副作用 coding task 合理：状态少、延迟低、控制流容易理解。进入长会话、外部工具、
  project-specific context、可恢复 session 与 delegated work 后，真正约束转向 Context budget、权限、
  side effect、extension supply chain 和 state continuity；旧 loop 没有失效，但必须被 harness 包围。
- **Mechanism / Control and Data Flow**：论文把 surface、core、safety/action、state、backend 五层与
  user/interface/query loop/permission/tools/persistence/execution 七组件分开。每 turn 依次 resolution、
  context assembly、五级 shaper、model stream、tool dispatch、permission gate、execution、stop/recovery；
  read/concurrent-safe tools 可并行，exclusive mutation 路径串行。五级 context degradation 先削减或引用
  tool output，再 snip/microcompact，继而以 collapse store 做 non-destructive read projection，最后才
  model summary；这保留 full history 与 active projection 的 owner 分离。
- **State Ownership**：transcript/sidechain 与 file checkpoint 是 runtime evidence；compact summary、
  CLAUDE.md/memory selection 和 model response 是 derived context；filesystem、git、remote service 与
  workflow state 仍是 authoritative environment。Session resume/fork 可恢复 message chain，却刻意不
  恢复 session-scoped permission，说明 data continuity 不等于 authority continuity。Checkpoint 只覆盖
  file change，不提供 remote side-effect rollback。
- **Authorization / Extensibility**：tool pool 在 model call 前做 mode/deny filtering，hook 可提出 deny/
  ask/modified input，rule evaluation 保留 deny-first，最终 executor/sandbox 才拥有 action authority。
  MCP、plugin、skill、hook 分别作用在 capability discovery、packaging、context injection 与 lifecycle
  interception，context cost 和 trust boundary 不同；协议接入不自动获得业务授权。Subagent 使用独立
  context/sidechain 并向 parent 返回 summary，换取 context isolation，但新增 delegation prompt loss、
  duplicated work、permission inheritance 与 shared-state conflict。
- **Implementation / Recovery Details**：核心是 streaming `AsyncGenerator` loop；论文记录 streamed-tool
  executor 与 fallback executor、最多三次 output-token escalation、每 turn 一次 reactive compaction、
  prompt-too-long、streaming/model fallback，以及 no-tool/max-turn/context-overflow/hook/abort stop path。
  Session 以 append-oriented JSONL、prompt history 和 sidechain 保存，compact boundary 用 head/anchor/
  tail identity 在 read time patch chain；这些是 snapshot observation，不应写成跨版本稳定 API。
- **Evaluation Contract / What It Proves**：`Not Disclosed`。论文没有 task benchmark、controlled
  ablation、latency/token/cost、hardware、concurrency、failure injection、security test、SLO 或 user
  study；因此只证明作者在公开 snapshot 中观察到上述 structure，并提供 deployment-context-aware
  design taxonomy。OpenClaw/Claude Code 的差异支持“同一设计问题可以有不同 fixed point”，不支持
  feature superiority、production reliability 或因果收益。
- **Trade-offs / New Failure Modes / Coexistence**：graduated compaction 用额外 state/versioning 换取
  bounded context；append log 用 query/rewrite 成本换 auditability；isolated delegation 用 token/copy/
  merge 成本换 context protection；per-action approval 用 interaction fatigue 换 fine-grained control；
  perimeter trust 与 gateway routing 则适合 single-operator/multi-channel context。多层防御若共享 parser、
  initialization window 或 policy blind spot 仍会共同失效；feature gates、mutable package snapshot、
  summary loss、stale permission assumption 和 extension supply chain 是新增风险。
- **Evolution Relationship**：`Direct Evolution`：suggestion/one-shot assistant -> reactive tool loop ->
  harness-managed action runtime；`Layering / Dependency`：Context shaping、authorization、persistence、
  delegation 与 protocol 分属不同 owner；`Principle Reuse`：append log、least privilege、control/evidence
  plane 来自 distributed systems；与 OpenClaw/Hermes 的对照是 deployment-context 分支，不是版本替代。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch68、Ch73、Ch74、Ch77～80。Ch68 已有
  untrusted model output、least privilege、sandbox 与 sensor/authority 分离；Ch73 已有 compact control
  summary + exact evidence archive；Ch74 有 typed action/approval；Ch77 有 durable workflow、replay、
  idempotency/compensation；Ch78 有 bounded delegation/typed handoff；Ch79 已说明 MCP 不授予 trust；
  Ch80 已以 identity/state/policy/evidence graph 收束 platform。论文提供了有用 implementation case，
  但没有形成这些章节尚缺的长期机制。
- **Integration Decision / Open Questions**：`No Change — Already Covered`，主 owner Ch80，Ch68/73/
  77～79 只保留本 Weekly 的证据映射；分数保持 22。待核验 event-bound immutable package artifact、
  feature-gate runtime prevalence、compaction fidelity/permission fatigue 的受控实验、multi-agent shared-state
  recovery，以及后续版本是否改变 owner/authority boundary。

### Memory Transfer Learning — 24/30

- **Candidate / Week / Source Family**：`MEMORY-TRANSFER-LEARNING-CODING-AGENTS`；W16；arXiv
  2604.14004 仅有 v1，于 2026-04-15 15:50 UTC 首次公开。已读全文、公式、main/Pass@1 tables、
  negative-transfer cases、abstraction model、benefit taxonomy 与 generation prompts，并核验 project page
  和作者 repository；repository 当前只有 7 commits、Harbor/mini-swe-agent trees 与 README，明确标注
  `Code: Coming Soon`，无 event-bound runnable artifact 或 release。
- **Original Problem / Why Previous Design Was Reasonable**：同域 episodic/trajectory retrieval 在任务、
  language、toolchain 和 evaluator 相近时能保留可直接复用细节，且 domain filter 降低误召回；但真实
  coding agent 横跨 function、repository、terminal、paper replication 与 ML experiment，按 benchmark
  隔离 memory 会丢掉 inspect-edit-test、interface compliance、environment recovery 等共享 procedural
  knowledge。旧的同域/raw branch 仍适合需要 exact command、相同 versioned environment 或高保真 replay
  的场景，不应被抽象 Insight 单向替代。
- **Mechanism / State Ownership / Data Flow**：先在六类 benchmark 上运行 agent，得到 task 与
  `(reasoning, action, observation)` trajectory；LLM judge 标成功/失败，再离线生成四种 derived memory：
  raw command/observation `Trajectory`、抽取动作序列的 `Workflow`、解释成败的 `Summary`、去掉文件/
  task detail 的 `Insight`。评测 target 的 memory pool 排除该 benchmark，使用
  text-embedding-3-small 建 index；Trajectory 以 source task 查询，其余格式先让模型写 4～5 句 target
  coding plan，再 cosine top-3，注入 system prompt 后执行 mini-swe-agent。Raw trajectory/evaluator outcome
  是 evidence，四类 memory、embedding/index 与 query plan 都是可失效 derived policy state；target
  repository、tests 和 benchmark harness 才拥有任务事实。
- **Abstraction Mechanism / Formal Boundary**：作者把 abstraction operationalize 为“能否从 Insight
  反推出原 task”的 LLM-inference similarity，再取 top/bottom 30% 比较；task-agnostic Insight 在三个
  benchmark 上平均高 1.1 个百分点。这控制了 format，却没有随机化 memory content、quality、length、
  source domain 或 retrievability，故不是 abstraction 的独立因果证明。Appendix 将 embedding 分成不可
  直接观测的 domain-invariant `z_inv` 与 domain-specific `z_sp`；“abstraction 越高，expected transfer
  越高”的 proposition 依赖 bounded capacity 和 `z_sp` 对 unseen task 只是 misaligned noise。Domain-
  specific detail 若恰是正确 API/tool/version contract，该假设不成立。
- **Evaluation Contract**：六个 benchmarks 为 LiveCodeBench v6、Aider Polyglot、SWE-Bench Verified、
  TerminalBench 2、ReplicationBench、MLGym-Bench；超过 100 项的集合随机抽 100，按各 benchmark 原生
  protocol 判 success，main report 为 Pass@3，Appendix 另给 Pass@1。Main pipeline 的 memory generator、
  coding model 和 LLM judge 均用 GPT-5-mini，agent 为 mini-swe-agent、platform 为 Harbor、每 query top-3。
  另测 DeepSeek V3.2 与 Qwen3-Coder-480B-A35B-Instruct。硬件、model snapshot、temperature、token/context
  budget、latency/cost、抽样 seed、confidence interval/significance、retry/failure policy 均 `Not Disclosed`。
- **What the Evidence Proves**：在作者 sampling 与 harness 下，GPT-5-mini Insight MTL 六 benchmark
  macro Pass@3 从 0.523 到 0.560；Pass@1 从 0.435 到 0.454。DeepSeek/Qwen 也有较小 macro gain，
  但存在单项持平或回退。三项 baseline comparison 中，431-memory MTL 高于 97-memory ReasoningBank
  与 5,899-memory AgentKB；memory count、source domains、representation 和 retrieval protocol 没有
  cost-match，故只能证明组合方法在该 contract 更好，不能把差异归因于“效率”。成功差分 cases 的
  GPT-5 categorization 指向 workflow/validation/environment meta-knowledge，algorithmic strategy 仅占
  5.5%；这属于 conditional post-hoc attribution，不是所有 run 的因果分解。
- **Negative Transfer / Retrieval Evidence**：Trajectory 会把 R-specific overwrite pattern 错套到 C++；
  Insight 也会把“pre-flight verification”扭成低质量 quick run。作者归纳 domain-mismatched anchoring、
  false validation confidence 与 misapplied best practice。LLM 从 embedding top-20 rerank 到 3、或重写
  top memories，均低于简单 embedding baseline；这反驳“更复杂 retriever 必然更好”，但没有搜索
  domain router、step-time retrieval、hard-negative training 或 verifier-gated adoption 的完整空间。
- **Cross-model / Scale Boundary**：不同 source/target model 的 Insight 在三个 benchmark macro Pass@1
  多数高于 zero-shot，但 self-generated memory 通常更好，证明 protocol 可以跨 model transport，不能
  证明内容与 model-neutral semantics。随机缩小 pool、增加 source-domain 数时平均趋势上升，只说明
  tested range 的 relevance opportunity 增加；没有报告 storage/index/token/latency growth、duplicate/
  poisoning density、long-tail dilution 或长期 plateau，不能外推“pool 越大越好”。
- **Trade-offs / New Failure Modes**：抽象 memory 减少 brittle command anchoring、提高跨域 reuse，
  却可能删除恰当的 version/API/precondition；具体 trace 支持 replay/debug，却在环境变化时产生强锚定。
  Shared pool 提高可复用面，同时新增 namespace/tenant authorization、source-domain skew、judge/extractor
  bias、contamination、duplicate strategy、model/tool version drift、false confidence 与 delete propagation。
  “retrieve”必须与“adopt”分开：derived advice 进入 Context 后，Workflow/Tool executor 仍按当前 task
  contract、tests、policy 和 side-effect boundary 验证。
- **Evolution Relationship**：`Direct Evolution`：same-domain raw episode reuse -> heterogeneous pool ->
  abstract procedural transfer + applicability/adaptation gate；`Layering / Dependency`：generation、index/
  retrieval、adoption verification 与 memory lifecycle 分层；`Principle Reuse`：transfer learning 从 weights
  移到 non-parametric policy artifact，但没有获得参数训练的 distribution contract。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch72～74、Ch77 与 Ch80。Ch72 已说明
  relevance 不等于 utility/sufficiency；Ch73 已覆盖 raw episode -> derived procedural lesson、provenance、
  model/reward/task identity、retrieval policy、negative writeback 与 advisory-state boundary；Ch77 已要求
  可迁移 control pass 声明 applicability/evidence，并由当前 task projection 和 evaluator 约束。新增缺口是
  明确 **cross-domain abstraction 不是压缩目标本身，而是 specificity benefit 与 mismatch risk 的选择**，
  且 source/target model、language/tool/environment/evaluator compatibility 应进入 retrieval/adoption contract。
- **Integration Decision / Score Correction / Open Questions**：provisional Ch73
  `Refine — Existing Argument (Experimental)`，Ch72/77 只作 handoff；Historical Books Gate 关闭，暂不写
  Books。SR `4->3`，总分 `25->24`，因为代码未发布且缺可复现 run、seeds/uncertainty、成本/SLO 与
  contamination audit。待验证 matched memory count/token budget、step-wise retrieval、hard negatives、
  independent judge、版本漂移、跨组织权限与真实 sequential lifecycle。

### CodeTracer: Towards Traceable Agent States — 28/30

- **Candidate / Week / Source Family**：`CODETRACER-TRACEABLE-AGENT-STATE`；W16；arXiv
  2604.11641，v1 2026-04-13、v3 2026-04-15；论文、HTML 正文、Appendix A～F 与作者仓库入口
  于 2026-08-09 核验。
- **Access / Full-read Coverage**：已覆盖 metadata/revision、Introduction、trajectory collection
  and filtering、annotation、Method、CodeTraceBench、setup、main results、component ablation、
  reflective replay、related work、conclusion、annotation rules、tracing details、metrics、prompts、
  extended results 与 industrial-agent appendix。作者仓库存在；本次未将 README 当作论文正文替代。
- **Original Problem / Previous Design**：end-to-end pass/fail 和 flat logs 对短、串行 Agent 合理，
  但 parallel tool calls 与 multi-stage code workflow 把早期错误埋在长轨迹中；人工逐条排查无法
  扩展。旧方案仍适合短轨迹、单一失败点和高风险 incident 的最终人工裁决。
- **Changed Constraint / Mechanism**：系统先用 evolving extractor 把异构 run directory 归一化为
  typed `action / observation / diff / verification` records；再把只读取环境的 exploration steps
  挂在当前 state 下，把会修改代码或环境的 steps 建成 child state transition；diagnosis 在这棵
  hierarchical trace tree 上定位 failure-responsible stage、error-relevant steps 与 compact evidence。
- **State Ownership / Control and Data Flow**：run artifact 与代码/环境变更是 workflow-owned fact；
  extractor registry 拥有 format adapter；trace tree 是 derived diagnostic index；人工标注提供 gold
  failure-critical state；replay agent 只消费诊断 hint，不得反向改写原始 run evidence。
- **Implementation Details**：新格式先生成 layout spec/parser 并注册复用；stage ranking 使用
  verification regression、diff magnitude、backtrack frequency 与 exploration-to-action ratio；每条
  trajectory 通常 3～15 stages，诊断成本随 stage 数近似线性。annotation 从失败 test 递归回溯到
  最早 error-critical step，并以 controlled vocabulary 标记 error type。
- **Evaluation Contract**：初始 7,936 trajectories 经 timeout、trace completeness、environment
  validity 与 trivial-success filters 后保留 3,326；覆盖 5 benchmarks、4 agent frameworks 与
  5 backbones。CodeTraceBench full/verified split 为 3.32K/1.06K，236 tasks、26 categories；主比较
  在 complete-coverage intersection 上使用 Claude-sonnet-4、GPT-5、DeepSeek-V3.2，统一 decoding
  和 matched localization budget，报告 per-instance macro step-level P/R/F1 与 token cost。15%
  double annotation 的 Cohen's kappa 为 0.73。
- **Evidence / Ablation**：在作者数据与协议下，hierarchical tracing 相对 Bare LLM/Mini-CodeTracer
  提升 failure-step localization；incremental ablation 将 evolving extraction 与 tree indexing 的
  贡献分开，后者是更大增益来源。失败 run 的 ineffective-step share 上升、correct state-changing
  share 下降，支持“找到 evidence 不等于采取正确 action”。更多 iterations 在约 40 steps 后趋于
  饱和，说明额外 loop 不能自动纠正早期错误承诺。
- **What It Does Not Prove**：不能证明自动定位等于真实根因；gold labels 全由作者团队产生，且
  ambiguous steps 默认 incorrect。Reflective replay 保持原 run 的 token/iteration budget，但诊断
  pass 另耗 5.2K～8.4K tokens，故不是 total-compute matched。Qwen–Terminus 组合仍有 pending data；
  Claude Code 来自不同 task distribution，只能做 qualitative comparison。没有公开 production SLO、
  privacy/retention contract、跨语言/非 coding domain 或独立复现。
- **Trade-offs / New Failure Modes**：获得跨框架 normalization、compressed causal navigation 与
  可行动诊断；新增 parser drift、derived-tree information loss、annotation bias、诊断模型误归因、
  sensitive artifact retention 和 replay anchoring。Parallel action 还会产生 ordering-sensitive causality，
  不能强行压成唯一 parent-child chain。
- **Evolution Relationship**：`Layering / Dependency`：metrics/logs/flat traces 保留 observed events，
  hierarchical state trace 在其上增加 state-change semantics 与 failure-onset hypothesis；
  `Principle Reuse`：从 software fault localization 借用 earliest-cause tracing，但 Agent trajectory 的
  probabilistic decisions、tool side effects 与 replay cost 需要额外 contract。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch62、Ch64、Ch65、Ch77、Ch80。
  Ch65 已有 distributed causal trace，Ch77 已有 authoritative workflow event log 与 deterministic
  replay，Ch80 已有 end-to-end Agent run trace；现有缺口是 exploration/state-changing action 的显式
  分层、failure-onset derived index 与 diagnosis/replay evidence boundary。主 owner 暂定 Ch80，
  Ch65/77 只需短 handoff。
- **Integration Decision / Open Questions**：provisional `Refine — Existing Argument`；Historical
  Books Gate 关闭，暂不写正文。待核验：跨框架 extractor 的长期 schema evolution、独立标注一致性、
  total-compute-matched replay，以及敏感 code/tool artifacts 的 retention 与 deletion policy。

### Automated alignment researchers — 23/30

- **Source Family ID / Type / Date**：`AUTOMATED-ALIGNMENT-RESEARCHERS`；Anthropic
  2026-04-14 research post 与 linked full study。
- **Full-read Coverage**：已覆盖 weak-to-strong setup、PGR 定义、research-agent workflow、
  baselines、ablation/失败案例与 limitations。
- **Problem / Mechanism**：human-only alignment research 难随模型能力扩展；系统让模型生成研究
  方向、实验和分析，并用 weak teacher/strong student 的 gap-recovery proxy 检验 scalable
  oversight。task spec、experiment environment 和 final acceptance 仍由 human/evaluation owner 控制。
- **Evidence Boundary**：研究说明当前模型能在受控任务上为 alignment research 提供 uplift；
  PGR 不是超人模型可监督性的证明，也不排除 shared-model blind spot、evaluation gaming 或
  researcher/evaluator collusion。
- **Trade-offs / Evolution**：automation 扩展实验吞吐，却放大 correlated error、resource cost、
  provenance 和 independent review 需求；human review 在高影响结论中仍成立。
- **ROADMAP / Decision**：Ch27、Ch62、Ch77 已读；`No Change — Already Covered`，现有 verifier、
  provenance 和 human gate 已覆盖长期机制。

### Synthetic datasets from first principles — 23/30

- **Source Family / Coverage**：`FIRST-PRINCIPLES-SYNTHETIC-DATA`；Google Research
  2026-04-16 官方研究及关联论文；已读 problem formulation、generator/control mechanism、
  experiments、ablation 与 sim-to-real limitations。
- **Mechanism / Evidence Boundary**：从任务机制和可控参数生成 data 可提高 coverage 与标签精度，
  但 generator specification 同时决定盲区；作者实验只证明特定 domain/task 的 utility，不证明
  synthetic data 可替代真实分布。
- **Trade-offs / Evolution**：从收集→规则增强→可控生成，获得 scale 和 counterfactual coverage，
  新增 specification bias、generator-model coupling 与 reality gap。Ch23/24/62 已读；
  `No Change — Already Covered`。

### GPT-Rosalind — 21/30

- **Sources / Verification**：OpenAI 2026-04-16 announcement、evaluation 与 access/safety 材料已核对。
  可确认面向 biology/drug discovery 的 literature、database、hypothesis、planning 与 tool workflow；
  训练架构和 runtime 内部机制 `Not Disclosed`。
- **Evidence / Decision**：厂商与 partner evaluation 不证明真实 wet-lab discovery、自主实验闭环或
  clinical outcome。Ch62/69/77 已读；`Weekly Only — Version/Product Fact`。

### DR3-Eval — 24/30

- **Candidate / Week / Source Family**：`DR3-EVAL-DEEP-RESEARCH-SANDBOX`；W16；arXiv
  2604.14683，唯一 v1 于 2026-04-16 06:40 UTC 首次公开；论文 HTML、全部 Appendix A～F、作者
  repository 与 Hugging Face dataset 于 2026-08-10 核验。
- **Access / Full-read Coverage**：已覆盖 benchmark construction、reverse construction、sandbox
  budgets、DR3-Agent 控制流、六项实际聚合指标、八模型实验、corpus/retrieval/framework ablation、
  live-web comparison、error attribution、judge validation、case study、PII 处理与公开 artifact。当前
  GitHub main 有 23 commits、无 tag/release；Hugging Face card 为 100 rows、2.61 GB，明确展示 query
  与 224 个用户文件，但公开结构未显式列出论文所需的 per-task static sandbox corpus、supportive/
  distractor/noise labels 或 event-bound digest。
- **Score Correction**：`25→24/30`（SR `4→3`）。论文与代码/用户文件数据均可访问，但静态 sandbox
  corpus 的完整公开/版本边界尚不能从 dataset card 复核；正文称随机抽取 50 份报告、4 名专家，
  Appendix D 却称 30 份、2 名独立专家。该内部冲突直接影响 judge-human calibration 的证据强度。
- **Original Problem / Previous Design**：live-web Deep Research eval 更接近真实信息环境，却受网页
  更新、搜索排序、地域与访问时刻影响而难以复现；固定 clean corpus 易复现，却把 retrieval noise、
  user files 与多模态整合从任务中删掉。两类旧方案都合理：前者适合 deployment relevance，后者适合
  regression 与受控机制比较，不能由一个混合 benchmark 单向替代。
- **Changed Constraint / Data Construction**：DR3-Eval 从真实用户提交的多模态材料出发，让 Gemini
  2.5 Pro 生成十个搜索关键词并区分 signal/noise，再对每词最多一百个网页做 crawl、dedup、clean，
  人工标成 supportive、distractor、noise。随后不是先写问题再搜答案，而是从已核 evidence 反向构造
  query，并用 implicit guidance、leave-one-out synthesis necessity、insight novelty 与 interpretive
  unambiguity 筛选；280 个初始任务删去 105 个歧义/不唯一和 75 个过易任务，保留中英文各 50 个。
- **Mechanism / State Ownership**：每题 sandbox 固定包含全部 supportive documents，再随 32K、64K、
  128K、256K、512K budget 增加 distractor 与 noise。benchmark owner 应拥有 query、user-file digest、
  source snapshot、support/distractor/noise taxonomy、gold insight、rubric 与 scorer version；Agent 只拥有
  run-local plan/context。DR3-Agent 的 main Agent 保留全局 context 与 Plan-Act-Observe loop，RAG subagent
  用 `text-embedding-3-small` 最多检索五轮，file-reader 最多三轮解析长文件；subagents 不共享全局状态，
  只回传压缩摘要，因此 retrieval miss 与 summary loss 都可能进入主 Agent 而不可恢复。
- **Evaluation Contract**：100 tasks 覆盖 3 大领域/13 子域，68% 含多模态文件，平均 2.24、最多 6 个
  用户文件；512K corpus 平均 465.5 pages。八个 API/backbone 在 64K/128K/512K 条件比较；judge
  temperature 为 0，单任务 run 约 300～400 秒、API 成本约 0.3～1 美元，evaluation 约 90 秒/0.1 美元。
  模型 snapshot、candidate decoding、硬件、batch、concurrency 与 SLO 未完整披露。六个聚合分量是
  user-file insight recall、sandbox insight recall、citation coverage、factual accuracy、instruction
  following 与 depth quality；前两类 gold insight 由模型抽取后人工核验，开放式 verdict 依赖 GPT-5.1
  或 Gemini 2.5 Pro judge。
- **Evidence / Ablation**：作者协议下，corpus 增大通常降低 sandbox recall、citation 与 aggregate，
  factual accuracy 相对稳定；20-task corpus ablation 中，去掉 distractor 有利，去掉 supportive 接近
  no-corpus，支持“相关证据是否存在”与“Agent 能否从干扰中找出它”是不同 failure surface。1/3/5/7
  retrieval turns 的收益非单调且依模型变化；OpenAI embedding 在该 corpus/三模型上优于比较的 Qwen
  embedding 与 BM25。Claude Sonnet 4 的 65.6 只属于 512K、DR3-Agent 与该 judge contract，不能成为
  通用模型排名。
- **What It Does Not Prove**：corpus budget 同时改变长度与 distractor/noise composition，不能单独证明
  long context 本身导致下降。live-web 子集的 aggregate 差异仅 -0.3/+0.7，却由 citation 与 recall 等
  大幅相反变化抵消；均值接近不证明 static sandbox 忠实替代真实 Web。DeerFlow 比较移植了 DR3 的
  Agentic RAG，不是两个原生 framework 的隔离对照。错误归因为 retrieval/reasoning/hallucination 是
  post-hoc taxonomy，不是因果定位。reverse construction 还引入 evidence-first selection 与 closed-world
  bias，可能排除真正开放、允许多种证据路线的研究任务。
- **Judge / Privacy Boundaries**：10K bootstrap、top-two Wilcoxon 与重复运行支持作者协议内的排名
  稳定性；但 human-alignment protocol 的 50/4 与 30/2 冲突未解释，不能写成已被强人工验证。
  作者声明自动 redaction 加人工 cross-check，却未披露 PII recall、false-negative 或隐私审计；
  “complete anonymization” 不是已证实的安全结论。aggregate 又等权混合六分量，权重本身属于 intended-use
  policy，不能由 benchmark creator 隐式替生产风险排序。
- **Trade-offs / New Failure Modes**：获得可冻结的 evidence/noise ratio、多模态 user-file contract、
  retrieval 与 generation 分层评分；付出 crawl/license/retention、snapshot storage、gold-insight maintenance、
  judge 成本和 corpus refresh debt。新增 failure modes 包括 reverse-construction leakage、support taxonomy
  偏差、遗漏 alternative evidence、sandbox 过时、summary truncation、同源 judge preference、分量平均抵消
  与公开 artifact 无法重建 event-time sandbox。
- **Where Previous Designs Still Apply / Evolution**：`Direct Evolution`：clean frozen corpus →
  per-task supportive/distractor/noise sandbox → 与 live-web component-wise calibration；`Layering /
  Dependency`：retrieval evidence、report claims、citations 与 judge verdict 必须各有 identity；live-web eval
  继续负责 freshness 与真实访问约束，static sandbox 继续负责 regression，二者是互证而非替代。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch61～63、Ch72、Ch77。Ch62 已有完整
  subject/environment/scorer/run contract、average/slice/uncertainty、Agent outcome、claim provenance、
  judge calibration 与 Offline→Online 演进；新增缺口是把 Deep Research environment 明确建模为
  `user files + frozen source snapshots + support/noise taxonomy + corpus budget`，以及要求 static/live
  对齐按 component 与 slice 比较，不能用 aggregate cancellation 宣称 realism。主 owner 暂定 Ch62，
  Ch72/77 只需短 handoff。
- **Integration Decision / Open Questions**：provisional `Refine — Existing Argument (Experimental)`；
  Historical Books Gate 关闭，暂不写正文。待作者澄清 human-validation protocol，并提供带 digest/license/
  timestamp 的完整 sandbox corpus、event-bound release、independent judge、open-ended task 对照、matched
  distractor-length experiment、contamination/privacy audit 与 repeated cost/SLO evidence。

### Don't Retrieve, Navigate / Corpus2Skill — 24/30

- **Candidate / Week / Source Family**：`CORPUS2SKILL-NAVIGABLE-RAG`；W16；arXiv 2604.14572，
  v1 2026-04-16 03:05 UTC，v2 04-29，v3 05-15。已读 v1 全文、Appendix A～I 与完整 traces，
  并将 v3 新增的 RAGBench generalization、soft assignment/entity cross-link、metrics/cost revision 作为
  later verification，不把 05 月结果倒记为 W16 新事件；作者 repository/current README/code surface 于
  2026-08-10 核验。
- **Access / Artifact Boundary**：当前 repository 有 7 commits、无 tag/release，README 明确标为
  `Work in Progress`。公开实现包含 load/embed、hierarchical clustering、summarization、skill builder、
  serve/eval 与 WixQA preparation；因此可核验机制入口，但没有 event-bound immutable artifact、production
  deployment、security review 或 incremental update path。
- **Score Correction**：`26→24/30`（TN `5→4`、SR `4→3`）。把 hierarchy 暴露给 Agent 并分离
  navigation metadata/evidence fetch 有价值，但 embed-cluster-summarize 延续 RAPTOR/cluster browsing 的
 既有结构；单篇作者实验、WIP artifact、无多 seed/uncertainty 与同一模型族 candidate/judge 边界不足以
  支撑原先的高可靠 Must Read 评分。
- **Original Problem / Previous Design**：BM25/dense/hybrid top-k 对高吞吐 factoid query 合理：query-time
  成本低、index 可增量维护、权限/过滤/latency 易工程化；但 generator 只看到命中的片段，不知道 corpus
  还有哪些主题，也不知道未检索到什么。Agentic RAG 可多次改写 query，却仍要在不可见 corpus 上猜 search
  terms。RAPTOR/GraphRAG 提供结构，但通常由固定 retriever/graph traversal 选择节点，模型看不到完整 routing
  map。旧路线没有失效，它们在开放域、精确 identifier、表格和低成本 query 上仍更合适。
- **Changed Constraint / Compile Mechanism**：离线 compiler 为每份文档生成 content-hash ID、截断并用
  Qwen3-Embedding-0.6B 表示；随后按 branching ratio `p` 做 normalized K-Means，LLM 汇总 cluster 的
  topic/question-types/key terms，再 embed summaries 并逐层聚类到不超过 `K` 个 roots。v1 使用 hard
  single-parent assignment；root、intermediate、leaf 分别物化为 SKILL.md/INDEX.md，full text 保存在
  `documents.json`。WixQA 6,221 docs 生成 6 skills、3-level tree、665 navigation files 与 13 MB store。
- **Serve Control / Data Flow**：Skills API 只预载 skill name/one-line description，Agent 再通过只读
  code execution 浏览 SKILL/INDEX，并用 `get_document(doc_id)` 读取 authoritative text。navigation summary
  只回答“去哪里找”，system prompt 禁止将其作为事实 evidence。Agent 可 direct descent、backtrack、保留
  多个候选 branch 或 cross-branch synthesis；理想 single-path inspection 为
  `O(p log_p N)` summaries，但真实多分支 traversal、重复 prompt content 与 accumulated context 会使成本更高。
- **State Ownership**：source document/ACL/deletion record 属 knowledge owner；content hash、tree revision、
  cluster memberships、summary/prompts、entity links 与 related-skill edges 是 index compiler 拥有的 derived
  state；Agent 拥有 run-local frontier、visited branches、retrieved document IDs 与 stopping decision；答案
  claims 必须指向 source document digest，不能把 summary 或 cluster label 升级为 truth。任何 source 更新/
  删除都必须传播到 tree、cross-links、cache 与 in-flight revision，而非只重写文件名。
- **Event-time Evaluation Contract**：v1 在 200 个 expert-written WixQA queries/6,221 support articles 上，
  统一 answer model/eval protocol 比较 BM25、Dense、Hybrid、RAPTOR、最多 10 rounds 的 Agentic RAG 与
  Corpus2Skill。compiler 在 32-CPU server 报告 6.5 分钟；LLM compile cost 约 5～10 美元。v1 主结果中
  Corpus2Skill 每 query 约 53,487 input tokens/0.172 美元，相对 Agentic 约 1.75×、RAPTOR 约 14×；
  API model snapshot、并发、cache hit、latency distribution、throughput 与 production SLO 未完整披露。
  Token F1/BLEU/ROUGE 与 model-judged Factuality/Context Recall 混合回答质量和 retrieval evidence。
- **Ablation / Failure Evidence**：v1 的 `p=5/10/20` 显示宽浅树同时降低质量并提高成本，说明 routing
  granularity 是机制变量而非目录美化；5/10/20 round budget 差异小，不能推断任意 corpus 不需探索；
  更小 serving model 提高 Context Recall 却降低 F1/Factuality，反驳“tree quality 是唯一主因”的强解释。
  62 个低分 query 中 38 个是 navigation miss，19 个 partial navigation，top-level taxonomy 是主要瓶颈；
  hard single path 会让跨主题文档被放错入口，soft/multi-parent 可缓解但增加 duplication、consistency 与成本。
- **Revision / Generalization Evidence**：v3 将协议扩到十个 RAGBench subsets，并把 train/val/test 文档
  content-hash 去重后合成 221～12,727 docs 的 retrieval pool。作者报告在含 WixQA 的 11 datasets 中
  7 胜、2 近似平、3 负：单域、主题可恢复 corpus 较适合 navigation；HAGRID open-domain、TatQA 同质表格、
  CUAD 长文 clause extraction 中 flat retrieval 更好。该 later revision 强化的是 scope boundary，不是
  “navigation 普遍替代 retrieval”。v3 又加入 soft assignment/entity cross-link、ephemeral prompt caching，
  使 WixQA compile time、成本、失败计数和 metrics 均与 v1 改变，跨版本数字不能拼成一个稳定 benchmark。
- **What It Does Not Prove**：所有主要结果来自作者构造与同一公开 benchmark family；无 independent
  replication、human preference、安全/ACL/poisoning、freshness/delete、incremental rebuild、crash recovery、
  parallel query、p95/p99 或 total-cost-matched production study。Context Recall 为不同方法只截取最后 5 份
  documents/8,000 chars，可能惩罚较早取到的证据；Claude Sonnet 4.6 同时作为服务模型和多个 judge metric，
  correlated preference 未排除。固定 seeds 只让 compile deterministic，不让 LLM summaries、Agent runs 或
  evaluator 具有已报告 uncertainty。
- **Trade-offs / New Failure Modes**：获得 corpus-wide observability、可解释 branch choice、backtracking、
  progressive disclosure 与 query-time 无 vector DB；付出 offline LLM compilation、tree/token storage、每轮
  prompt accumulation、provider Skills API coupling 和全量重编译。新 failure modes 是 taxonomy collapse、
  summary omission、wrong top-level commitment、multi-topic document orphan、cross-link stale、duplicate ACL/
  delete propagation、branch-loop、premature stop 与 navigation prompt injection。
- **Evolution / Alternatives**：`Direct Evolution`：flat top-k → hierarchical retriever → Agent-visible
  hierarchy + exact document dereference；`Layering / Dependency`：dense/lexical retrieval 可提供 coarse
  entry prior，navigation 管理 coverage/backtracking，exact dereference 提供 evidence；`Principle Reuse`：
  filesystem Skill 是 index materialization，不是 procedural memory。未来合理方向是按 query/corpus shape
  在 flat retrieval、RAPTOR、navigation 间路由，而不是让一种结构覆盖全部。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch71～73 与 Ch80。Ch72 已覆盖 lexical/
  dense/hybrid、parent-child retrieval、sufficiency、Agentic relevance prior、query/compression/stopping、
  freshness/delete/consistency；新增缺口是将 **Agent-visible corpus map** 定义为 versioned derived index，
  并以 taxonomy recoverability、branching factor、multi-parent policy、map/source identity 与 route trace 决定
  navigation 是否成立。主 owner 暂定 Ch72，Ch62/73/80 只需 handoff。
- **Integration Decision / Open Questions**：provisional `Refine — Existing Argument (Experimental)`；
  Historical Books Gate 关闭，暂不写正文。待验证 incremental/partial rebuild、event-time immutable release、
  independent judge、多 seed、hybrid per-query router、ACL/delete propagation、adversarial document、cache/
  latency/goodput/SLO，以及相同 total cost 下 navigation 与 multi-query retrieval 的边界。

### OpenMobile — 24/30

- **Candidate / Week / Source Family**：OpenMobile；2026-W16；`openmobile-trajectory-synthesis-and-policy-switching`。
  source type 为论文、project page、代码、dataset 与 model artifact；arXiv 仅有 v1，first-public date
  为 2026-04-16。project page 当前标注 COLM 2026 acceptance，属于后续 publication state，不改写事件周。
- **Direct / Related Primary Sources / Access**：已阅读全文、附录与实验表，核对 project page、当前
  OpenMobile-Code repository、OpenMobile-Data 与 OpenMobile-8B artifact。代码仓库当前 23 commits、无
  release，且包含论文之后的 Qwen3.5/SGLang 更新；这些 later repository facts 只用于验证 artifact drift。
  dataset 公开 raw trajectories、screenshots 与四个 LLaMAFactory JSON，但 viewer 当前存在 schema-cast
  error；model page 无 model card，页面所示 770k BF16 参数更像 adapter/incomplete artifact，不能据此验证
  完整 8B checkpoint identity。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint**：纯 expert demonstration
  以高质量成功轨迹教 imitation，在短任务和可枚举起点上合理；local trajectory-coupled task generation
  也能保证 instruction 与可执行 state 相连。但前者没有覆盖 learner 自己造成的 off-trajectory state，
  后者的任务多样性受单条局部轨迹限制。动态 mobile environment、长 horizon 与跨 app interaction 使
  error recovery、environment identity 和 side effect 成为数据 contract，而不只是 instruction 数量。
- **Mechanism / State Ownership / Control and Data Flow**：task synthesis 先在 emulator 中随机 walk 十步，
  从 accessibility tree 选可交互元素，记录 screen/action transition，并以 pHash 0.95 相似度去重；VLM
  基于前序 screen/action 标注功能，形成 `screen + neighbor graph + functionality annotation` 的 global
  environment memory。生成器看到当前功能、一个 predecessor、最多三个 successor 与三十个去相关 distant
  functions，再经 complexity/clarity/reasonableness filter、0.8 semantic dedup 与 per-app cap 产出任务。
  rollout 时 learner 先行动；monitor 观察最近动作和最后两张截图，检测偏离后让 expert 至少接管三步，
  最多两次 intervention，再把控制权交回 learner。SFT 只保留 expert steps，但其 conditioning history
  包含 learner error，expert 同时重写 reasoning。authoritative state 属 emulator、task initializer、app/
  version、action schema 与 verifier；environment memory、VLM annotation 和 neighbor graph 都只是 derived
  index，不能替代真实环境状态。
- **Implementation / Evaluation Contract**：论文报告约 2,800 instructions、34K action steps、20 apps，
  平均 12.2 steps 与 129-word reasoning；以 Qwen2.5-VL-7B、Qwen3-VL-8B 做 SFT，batch 32、learning rate
  `1e-5`、三 epochs、LLaMAFactory，vLLM inference。在 AndroidWorld 116 tasks/20 apps、AndroidLab
  138 tasks/9 apps 与 MobileWorld long-horizon cross-app tasks 上各运行三次，报告 mean、half-range 与
  Pass@3。训练/推理硬件、precision、token budget、concurrency、cost 与 SLO 均 `Not Disclosed`。
- **Baselines / Ablations / Sensitivity**：固定 1.5K trajectory 时，对比 OS-Genesis、local coupled 与
  global-memory generation；另比较 pure expert、self-evolution、random switching 与 error-triggered
  intervention，并由 50 条人工轨迹估算 error recovery。论文还用 text-embedding-3-large 测 instruction
  overlap，并删除最相似 10%/40% 数据。但 monitor、expert、filter、annotation 与 reasoning rewrite 多由
  同一 Gemini family 承担，ablation 没有拆开这些变量；prior-system comparison 也混合不同 base model
  与 setting，作者明确承认并非严格直接比较。
- **What Evidence Proves / Does Not Prove**：作者合同内证据支持 global environment view 能提高任务组合
  覆盖，并支持 error-triggered expert continuation 比纯 expert/self-evolution/random switching 更适合采集
  learner-reachable recovery states。它没有证明数值可外推到真实手机、其他 app/version、其他 teacher/
  learner、长期副作用或 production SLO；与 AndroidWorld 同一 environment/app suite 且只排除 benchmark
  test instructions，3.5% 高语义相似与删除实验不能排除 functional/state/template contamination。
- **Limitations / Threats / Trade-offs / New Failure Modes**：global memory 用 exploration、VLM annotation、
  dedup/index drift 换取组合覆盖；pHash 可能合并视觉近似但功能不同的 state，random walk 可能遗漏边，VLM
  annotation 可能幻觉。policy switching 用额外 teacher/monitor 调用、selection bias 与 off-policy mixture
  换取 recovery coverage；同源 model error 会相关，expert 也可能从 learner 无法自行恢复的 state 完成任务。
  full history、policy source、intervention、screen/action、reset 与 side effect 若没有 immutable provenance，
  无法区分 learner recovery、teacher substitution 与 environment drift。Appendix C 的 RL 未显著改善，作者只
  提出 environment diversity 与 RL stability 假说；论文没有独立 Limitations/Threats section。
- **Where Previous Design Still Applies / Evolution**：`Direct Evolution`：successful expert demonstrations
  → learner-state-aware intervention trajectories；`Layering / Dependency`：executable environment/verifier
  → derived environment memory → task generation → policy switching → SFT。短 horizon、低风险、起点稳定或
  learner error 很少时，pure expert data 更便宜且 attribution 更清晰；无法可靠 reset 或动作副作用较大时，
  离线 human-curated demonstration 仍优于自动 exploration。新机制不是 expert data 的替代，而是在 recovery
  state coverage 成为瓶颈时增加一个分支。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch23、Ch25 及 Ch62/77/80 handoff。Ch23 已覆盖
  language-first generator/judge 与 executable specification、environment/verifier lineage；Ch25 已覆盖
  synthetic demonstration bias、coverage、distillation，以及 filtered short-trace SFT 与 outcome RL 的分工。
  新缺口是把 **learner-reachable error/recovery state coverage** 写成 demonstration contract，并记录 teacher/
  monitor provenance、intervention selection bias 与 reset/side-effect boundary。主 owner 暂定 Ch25，Ch23
  只保留 environment-memory/data-lineage handoff。
- **Integration Decision / Score Correction / Open Questions**：provisional `Refine — Existing Argument
  (Experimental)`；Historical Books Gate 关闭，暂不写正文。因缺 dedicated limitations、硬件/cost/SLO、
  independent teacher/monitor ablation、完整 contamination contract 与可验证 model artifact，SR 4→3、
  Longevity 4→3，总分 25→24。待验证 event-time artifact digest、不同 teacher/monitor、真实设备、app/version
  drift、safe reset、matched-cost DAgger/self-evolution，以及 vLLM 与后续 SGLang runtime 下的可复现差异。

### Scaling Test-Time Compute for Agentic Coding — 25/30

- **Candidate / Week / Source Family**：Scaling Test-Time Compute for Agentic Coding；2026-W16；
  `agentic-rollout-representation-selection-reuse`。source type 为 sole-v1 preprint；arXiv first-public date
  为 2026-04-16，paper 内部 dateline 2026-04-21 不改写事件周。未找到作者 code、rollout dataset、prompt
  package 或 immutable artifact；full text、Appendix A～H、公式、tables 与 qualitative examples 已审计。
- **Direct / Related Primary Sources / Access**：以 official arXiv metadata/abstract 核对 title、authors 与
  first-public date，并阅读全文 public paper mirror。论文明确依赖 mini-SWE-agent、Terminus 1、SWE-Bench
  Verified 与 Terminal-Bench v2.0，但没有公开本研究的 executable implementation，故机制只能按作者论文
  实验审计，不能独立复现。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint**：short-answer test-time
  scaling 可对 bounded candidates 直接 majority vote、rank 或 refine；在单轮 math/code generation 中这是
  合理的小对象接口。long-horizon coding rollout 却混合 thought、command、observation、error、partial patch
  与重复 terminal output，raw trace 超长且难比较；增加 rollout 数量后，瓶颈从采样本身转为 prior experience
  的 representation、selection 与 reuse。
- **Mechanism / State Ownership / Control and Data Flow**：每个 rollout 在独立 container 中运行，完整
  trajectory `R` 由同一 model 通过 prompt 压缩为 structured summary `S`，保存 requirements、hypotheses、
  decisions、progress、verification 与 failure evidence。RTV 将 `N` 个 summaries 分为大小 `G` 的小组，
  每组采样 `V` 个 comparison votes，选一项进入下一轮，递归到 top-K 或 top-1。PDR 在 freshly initialized
  containers 中启动下一批 `N` rollouts，以选出的 `K` summaries 作为第一步额外 context；最终再用 RTV
  选 top-1。authoritative state 属 task input、container、repository/workspace、commands/results 与 hidden
  executable verifier；summary、judge vote 和 selected set 都是 derived control state，不能代替 patch/test
  evidence。两轮之间只传 summary，不传原 workspace、partial patch 或 derived tools。
- **Implementation / Evaluation Contract**：SWE-Bench Verified 用 bash-only mini-SWE-agent 全 500 tasks；
  Terminal-Bench v2.0 用 Terminus 1 的 88/89 tasks。模型为 Claude-4.5-Opus/Sonnet、Gemini-3.1-Pro、
  Gemini-3-Flash 与 GPT-5-0825；主配置 `N=16, T=2, K=4, G=2, V=8`。论文报告 pass@1/pass@16、
  mixed-pass task、step count、selection accuracy 与 fail→pass cases。model API snapshot、sampling temperature、
  token/context cap、hardware、parallelism、wall-clock latency、API failure accounting、dollar/energy cost 与 SLO
  均 `Not Disclosed`。
- **Baselines / Ablations / Sensitivity**：对比 raw trajectory 与 structured summary，flat 16-way 与 recursive
  group size 8/4/2，vote count 1/2/4/8/16，single-summary、random-K 与 RTV select-K refinement，并按 selected
  context 中 0～4 个 passing rollouts 切片。pairwise `G=2` 最佳，vote 增至约 8 后收益递减；multiple summaries
  优于 single，select-K 优于 random-K。它没有与 **相同 total generator + summarizer + judge token/call/
  latency budget** 下的 32 independent rollouts、execution-grounded verifier、diversity-aware selector 或更强
  single rollout 比较。
- **What Evidence Proves / Does Not Prove**：在作者的两个 coding harness、五个 vendor model 与固定
  `16×2` rollout contract 内，bounded structured summaries 比 raw traces 更适合 self-judged selection/reuse，
  local comparison + vote aggregation 能把一部分 rollout diversity 转成更高 final pass@1；selected-context
  quality 与 next-iteration success 强相关。证据没有证明 summary 因果充分、RTV 普遍优于 executable
  verification、同源 judge 独立可靠、结果可外推到有副作用工具/非 coding workflow，或总成本/latency 更低。
  “iteration-1 约少一半 steps”只描述单条 action rollout，不包含第二批 rollouts、summary 与 tournament
  judge work。
- **Limitations / Threats / Trade-offs / New Failure Modes**：summary 以 bounded context 换掉 raw-trace noise，
  也会丢失细微 diff、negative evidence、temporal order 与 verification identity；作者观察到 SWE-Bench 的
  subtle code diff/hidden test 比 Terminal-Bench command-output 更难 judge。self-generator/self-summarizer/
  self-judge 形成 correlated blind spot，Gemini-3.1-Pro 还受 API infrastructure failures 影响。更关键的是，
  iteration 1 虽提高平均 pass@1，却降低两个 benchmark 的 pass@16，并让一部分 task 退化为 0/16：RTV
  错选低质量 context 后，PDR 会把错误经验复制到整批 fresh rollouts。论文无 dedicated limitations、seed/
  confidence interval、failure injection、prompt sensitivity、security 或 side-effect evaluation。
- **Operational Cost Inference**：按论文算法，主配置至少包含每 task 两轮各 16 条 action rollouts、每条
  summary，以及 top-4 和 final top-1 的多轮 votes；这是由公开控制流推得的工作量，不是论文披露的精确
  billing。它支持“representation 是 scaling interface”，不支持用 final-vs-Iter0 headline 宣称 compute-
  optimal；adaptive stopping、admission 与 per-task budget 仍未解决。
- **Where Previous Design Still Applies / Evolution**：`Direct Evolution`：independent retry / best-of-N →
  summary-based recursive selection → selected-summary-conditioned retry → final selection；`Layering /
  Dependency`：sandbox/verifier → immutable rollout evidence → derived summary → judge/selector → fresh rollout。
  cheap deterministic tests、低 variance 或一条 rollout 已足够时，single Agent + verifier 更可靠；完整 trace
  可放入 context 且细节决定 correctness 时不应强制压缩；有可执行 oracle 时 execution-grounded selection
  优先于 model vote。RTV/PDR 是高不确定、可并行、可安全重跑时的分支，不是 retry 的普遍替代。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch62、Ch75、Ch77、Ch78、Ch80。Ch78 已覆盖
  single-Agent baseline、independent parallel exploration、centralized verification、correlated consensus、
  communication tax 与 topology matching；新增缺口是把 **bounded trajectory representation** 作为
  parallel selection 和 sequential reuse 的共同接口，并显式记录 coverage loss 与 bad-context amplification。
  主 owner 暂定 Ch78；Ch77 拥有 retry/budget/workflow state，Ch62 拥有 judge/executable evidence contract，
  Ch80 拥有 rollout identity/cost/trace。
- **Integration Decision / Score Correction / Open Questions**：provisional `Refine — Existing Argument
  (Experimental)`；Historical Books Gate 关闭，暂不写正文。representation/RTV 的 novelty、实际成本与公开
  可复现性弱于初筛预期，TN 5→4、PV 5→4、SR 4→3、Longevity 3→4，总分 27→25。待验证 immutable
  summary schema/lineage、summary-vs-trace coverage、independent/executable judge、equal-total-cost baseline、
  adaptive stopping、bad-context quarantine、跨 model/harness transfer 与 artifact-carrying refinement。

### SkillFlow — 24/30

- **Candidate / Week / Source Family**：`SKILLFLOW-LIFELONG-SKILL-EVOLUTION`；W16；arXiv
  2604.17308，唯一 v1 于 2026-04-19 07:51 UTC 首次公开。论文正文与 Appendix A～C、作者 project
  page、benchmark repository、task dataset 与 evolved-skill artifact 入口于 2026-08-10 核验；后续同名
  arXiv:2605.14089 属另一 source family，未混入本审计。
- **Access / Full-read Coverage**：已覆盖 Introduction/Related Work、DAEF formalization、four-stage task
  construction、Agentic Lifelong Learning protocol、patch schema/prompt、11 个 model–harness settings、
  success/turn/cost/token/skill metrics、family/domain analysis、six findings、human agreement/checklist、
  historical-trajectory control、全部 appendix figures/tables、runner/config/Docker layout 与公开数据入口。
- **Original Problem / Why Previous Design Was Reasonable**：静态 benchmark 提供预置 Skill，能隔离
  “是否会调用既有 procedure”，适合 capability regression；raw trajectory replay 又保留最高 evidence
  fidelity，短 history 下无需额外 abstraction。它们没有回答长期系统能否从失败中生成、修订、删除并
  重用 procedural artifact；history 变长后，偶然步骤、失败路径与 token cost 也会持续进入 Context。
- **Changed Constraint / Mechanism**：SkillFlow 将 166 个 executable tasks 组织为 20 个 family，每个
  family 共享 Domain-Agnostic Execution Flow：操作类型与 dependency topology 固定，仅改变 domain
  grounding、格式、规模、规则与难度。每个 family 从空 library 开始，按固定递增难度运行；task
  `T_t` 产生 native-harness trajectory `τ_t` 与 verifier-derived textual rubric `r_t`，模型在统一 prompt
  下生成 `Δ_t = Model_g(S_{t-1}, τ_t, r_t)`，再以 `S_t = Apply(Δ_t,S_{t-1})` 更新 library。
- **State Ownership / Control and Data Flow**：task instruction、Docker environment、verifier 与 rubric
  属 evaluator-owned state；trajectory 是 run evidence；`summary/upsert_files/delete_paths` patch、SKILL.md、
  scripts/references/assets 是 model-derived procedural state；native harness 决定 execution/tool behavior，
  benchmark runner 负责 family order、library carry-forward、reset 与 metrics。derived Skill 只能是
  advisory artifact，不能覆盖 authoritative environment、policy、approval 或原始 evidence。
- **Implementation Details**：patch 允许创建、全量覆盖或删除相对路径，并要求每个 Skill 有固定 YAML
  front matter；prompt 明确要求从成功与失败路径提取 decision rules，证据不足时返回 empty patch。
  benchmark 由 SkillsBench/GDPval 的 64 个 seed tasks 与 8,000+ public skills 起步，embedding 匹配后由
  human 抽象 DAEF；GPT-5.3-Codex Architect 与 Claude Opus 4.6 Critic 在 Docker 中生成/修订 family，
  再由人工检查 solvability、logic、environment closure、difficulty order、instruction leakage 与 DAEF
  membership。公开仓库只有 5 commits、无 tagged release，但包含 baseline/iterative runners、configs、
  Docker 与 analysis；task data 独立发布，README 明示 API endpoint/model/key 需自行配置。
- **Evaluation Contract**：主表在 Claude Code、Codex CLI、Qwen-Coder、Kimi-CLI 四种不同 native
  harness 上评估 11 个 model variants；每个 task 比较独立 vanilla run 与 family-local evolving-library
  run，并报告 166-task average completion、turns、USD cost、output tokens、final skill count 与 reuse rate。
  Claude Opus 4.6 在该协议下从 104/166（62.65%）到 118/166（71.08%），平均 turns 17.34→19.00、
  cost 0.665→0.615 USD、output 3.00K→2.39K；Kimi K2.5 的 66.87% reuse 只带来 +0.60 points，
  GPT-5.3-Codex、两个 Qwen settings 与 MiniMax M2.7 出现回退。论文未披露 sampling temperature、
  repeated seeds/variance、API snapshot、hardware、parallelism、wall-clock、failure accounting 或生产 SLO。
- **What Evidence Proves**：在作者构造的 closed、family-local、固定顺序 workload 中，外部化的可修订
  procedure 对部分 model–harness stack 有选择性收益；skill use 不等于 skill utility，compact library
  也不是充分条件。强结果更接近“能识别并修复错误 abstraction”，弱结果会发生 skill inflation 或把早期
  错误放大到后续 tasks。历史轨迹 control 支持结构化 externalization 与 raw context 是不同分支，但只对
  Claude Opus 4.6 做了一组 control。
- **What It Does Not Prove / Internal Evidence Conflict**：library 在 family 间清空，且任务按单一固定难度
  顺序执行，论文明确避免 heterogeneous retrieval confound；因此没有测跨 family retrieval、interference、
  forgetting、open-world drift、order sensitivity 或真正全局 lifelong library。不同 model 使用不同 harness，
  不能把差异归因于 weights。rubric 是 verifier 生成的 missing/incorrect-content 描述，也是 evaluator-to-policy
  information channel；收益不能仅归因于自主反思。正文 C.2 把 history-context completion 写为
  `47.41%`，Table 6 与 project page 写为 `51.04%`，同一 primary report 内部冲突；本审计不选择性消解，
  只保留“低于 vanilla 与 full protocol”的方向性结论。无随机顺序、confidence interval、contamination、
  patch-level causal ablation、malicious/poisoned Skill、concurrent update 或 crash/rollback evaluation。
- **Trade-offs / New Failure Modes**：结构化 Skill 降低反复重放 raw history 的 context tax，并让 procedure
  可复用；代价是新增 extractor/prompt、patch lineage、library growth、selection、review、revocation 与
  compatibility state。`upsert_files` 是覆盖语义，若 runner log 未成为 durable provenance，当前 library
  本身不能重建完整历史。新 failure modes 包括 rubric leakage/reward hacking、错误 Skill 持久化、overlap/
  fragmentation、delete collateral damage、stale tool/environment assumptions、harness-specific procedure、
  patch conflict 与高 reuse 下的系统性负迁移。
- **Where Previous Designs Still Apply / Evolution**：`Direct Evolution`：raw episodes → task-local notes →
  reusable Skill → failure-conditioned patch → consolidation/delete；`Layering / Dependency`：immutable run
  evidence → derived procedural artifact → verifier-gated adoption → versioned registry/rollout。短 history、
  细节决定 correctness 时保留 raw trace；高风险/稳定 workflow 继续使用人工审核的静态 Skill；异构开放
  任务需要 retrieval/router 与 global conflict/forgetting evaluation，不能直接沿用 family reset contract。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch62、Ch73、Ch77、Ch80。Ch62 已明确区分
  snapshot、feedback-conditioned trajectory 与 evolving state sequence，并要求保存每轮 state/evidence/
  rollback；Ch73 已覆盖 raw episode→procedural lesson、derived-state provenance、consolidation 与
  supersession；Ch80 已定义 Skill 的 immutable identity、dependencies、evaluation、policy、revocation 与
  rollout。论文为这些现有结论增加一个窄协议下的实验案例，但没有补出新的长期机制。
- **Integration Decision / Score Correction / Open Questions**：`No Change — Already Covered`；不把单篇
  benchmark 名称或 headline 写入 Books。family-local fixed-order、rubric information channel、model/harness
  confounding 与内部数值冲突使 Practical Value 5→4、总分 25→24。待验证 randomized/interleaved family、
  cross-domain library、independent feedback、patch lineage/rollback、adversarial Skill、long-term cost/SLO 与
  repeated statistically bounded results。

### EvoMaster — 23/30

- **Candidate / Week / Source Family**：`EVOMASTER-AGENTIC-SCIENCE-HARNESS`；W16 research-paper event；
  arXiv:2604.17406 v1 于 2026-04-19 12:26 UTC 首次公开，v2 04-21、v3 06-07、v4 07-01。repository
  更早于 02-06 发布 v0.0.1，03-01/03-24 有可定位 tags；README 声称 04-12 v0.1.1，但 tags 页未提供
  对应 tag。W16 保留 paper event，早期 code release 只作为 source-family lineage，不伪装为 04-19 首发。
- **Access / Full-read Coverage**：已分别阅读 event-time v1 与 current v4 的 Introduction、Related Work、
  four design principles、Playground/Exp/Agent architecture、Agent Engine、Capability/Skill/MCP、multi-agent
  orchestration、experiment harness、SciMaster ecosystem、全部 experiment tables、benchmark-specific setup、
  appendices/case studies 与 limitations；并检查 repository README、tags、current module layout 与 05-18
  才加入的 run-level self-evolution guide。
- **Original Problem / Why Previous Design Was Reasonable**：domain-specific scientific Agent 把 tool、
  evaluation 与 workflow 贴近学科，可减少抽象层并保留 domain semantics；single-pass loop 对短、可一次
  验证的任务更易复现。随着多个学科重复实现 context、tool、trajectory、retry 与 orchestration，复用
  harness 能降低工程成本；长 horizon 搜索也需要根据 experiment feedback 修订 artifact。旧分支在高风险
  实验、物理 apparatus、专用 verifier 或简单 task 中仍合理。
- **Changed Constraint / Mechanism**：框架把 execution 分成 Playground（跨 Agent/workflow orchestration）、
  Exp（single-experiment lifecycle/trajectory）与 Agent（reason→tool→observe→self-critique reactive loop）。
  YAML 管理 prompt/model/tool/environment，structured JSON 记录 dialogue/tool/token；ContextManager 以
  dynamic summary + sliding window 延长 run；Capability 层统一 MCP Tool、on-demand Skill 与 LLM adapter；
  AgentSlots 组合 sequential handoff、parallel exploration 与 iterative peer review。不同 SciMaster workflow
  再在该 harness 上实现 MLE 的 prefetch/draft/最多 20 rounds、Browse 的 Planner–Executor、HLE 的
  Solve–Critique–Rewrite–Select 等具体策略。
- **State Ownership / Control and Data Flow**：paper 把 current Context、self-critique 与 next action 交给
  model-driven Agent；Exp 保存单次 run/trajectory；Playground 编排 roles；YAML/registries 提供 definition；
  tools/environment/evaluator 提供 external observations。它没有公开定义 durable authoritative experiment
  state、idempotency、approval、artifact promotion、cross-run memory truth、crash replay 或 side-effect
  compensation；因此“trajectory 被记录”不等于 workflow state 可恢复，“self-critique”也不是独立 verifier。
- **Implementation / Revision Boundary**：event-time v1 只描述 run 内 reactive loop 与 task-specific
  cognitive cache，并无后来 repository 的通用 run-level evolution wrapper。current main 在 05-18 才新增
  baseline→TraceDigest→run-local Skill/prompt overlay→rerun：Skill/prompt 可自动应用，tool code 只生成 review
  proposal；每轮保留 workspace/trajectory/config/log，serial-only、single-task、original config 不覆盖。
  这是后续版本事实，能说明演进方向，不能倒灌为 W16 论文实现或实验机制。current main 288 commits、
  README roadmap 仍写 v0.x；没有 event-bound experiment artifact/tag 将论文 runs 与具体 commit 绑定。
- **Event-time Evaluation Contract (v1)**：只比较 EvoMaster 与 OpenClaw，四项都用 GPT-5.4；作者称 tools/
  skills 相同，在 RTX 4090 server 上运行，MLE-Bench Lite 限 24h。EvoMaster 却分别使用 X-Master、
  ML-Master 2.0、Browse-Master、X-Master 2.0，而 baseline 是 general-purpose OpenClaw；因此对比同时改变
  workflow、parallelism、retrieval、memory/cache、budget utilization 与 harness。v1 报告 HLE 41.1、MLE
  any-medal 75.8、BrowseComp 73.3、FrontierScience 53.3，并称相对 +159%～316%；没有 component ablation、
  equal-call/token/cost contract、repeated seeds/uncertainty、error bars 或完整 failure accounting，FrontierScience
  明示 single run。
- **Later Revision Evidence (v4)**：v4 扩展为 10 benchmarks、加入 OpenHands/Codex，统一 GPT-5.4-medium、
  benchmark-specific time limits/tools/splits，并披露部分 workload：PaperBench 20 tasks、24h/260 turns/
  100k context、20 parallel CPU containers；PostTrainBench 每 task 1×A800/16 CPU/10h；MLE 22 tasks、
  2×RTX4090/32 CPU/24h、最多 20 rounds；HLE 5 agents per each of 4 stages；多项 evaluation 使用 GPT-5/
  GPT-5.5 judge。v4 的新增结果与细节增强可核验性，但仍没有 harness-component ablation、matched total
  model/tool/judge compute、seeds/CI、wall-clock/cost aggregate 或 event-time artifact；不同 benchmark 使用
  不同 specialized workflow，所以 58.02% 的十项简单平均也不是单一系统能力或科学自治尺度。
- **What Evidence Proves**：公开 framework 与多种 playground 证明共享 Agent/Exp/Playground、typed config、
  trajectory 与 tool/Skill adapter 可以承载多个 computational workflows；在作者各自定制、强 evaluator/
  retrieval 与固定 backend 的协议内，iterative artifact refinement 在若干任务上优于所选 general baseline。
  v4 也保留反例：Codex 在 PostTrainBench 更高，部分 PRL 子领域、construction tasks 与 biomedical slices
  由其他 systems 领先，说明新 harness 不是单向支配。
- **What It Does Not Prove**：没有证据把收益拆成 self-critique、context compression、multi-agent、tool、
  domain prompt、search budget 或 base harness 的独立贡献；也没有证明跨 run 学习、scientific novelty、
  hypothesis truth、physical-lab autonomy、数日 crash recovery、reproducibility 或 production scale。
  JSON trace 记录 API/web/model nondeterminism 仍不等于可重演；同源 GPT-5.4 roles/judges 可能共享盲点。
  “约 100 lines”“days→hours”“100+ models/tools 可无缝替换”“最佳 foundational substrate”均是作者主张，
  不是实验结论。
- **Trade-offs / New Failure Modes**：共享 harness 降低重复实现并集中 observability，却扩大公共 abstraction
  的 blast radius、version compatibility 与 domain leakage；summary/sliding window 控制 Context，代价是
  evidence loss；parallel critic/rewrite 增加候选与纠错，也增加 correlated consensus、token/cost、selection
  error 与 critical path。task-specific overlays 提高效果却削弱“foundation-only”因果归因。current 自动
  Skill/prompt overlay 还新增 trajectory poisoning、overfit、secret leakage 与 regression；tool proposal 的
  manual gate 是合理旧边界，不能被“self-evolution”宣传抹去。
- **Where Previous Designs Still Apply / Evolution**：`Layering / Dependency`：domain workflow → reusable
  Agent/Exp/Playground harness → typed evidence and evaluator → specialized iterative search；`Direct Evolution`
  仅适用于 repository 后续版本：in-run reactive refinement → post-run local overlay → review/rerun。单 Agent +
  deterministic verifier 仍适合可执行、顺序强的任务；人工 scientific review、domain-specific runtime 与
  durable workflow 仍拥有真值、风险和副作用控制；多 Agent 只在可分解与 evidence 相对独立时成立。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch62、Ch73、Ch77、Ch78、Ch80。Ch77 已拥有
  deterministic spine、evaluator-driven artifact search、lineage/budget/held-out/approval/rollback 与 scientific
  physical-action boundary；Ch78 已覆盖 single-Agent baseline、topology matching、correlated consensus 与
  coordination tax；Ch80 已覆盖 definition/registry/runtime/evidence planes、trajectory/replay/rollout；Ch73
  已覆盖 derived procedural memory。EvoMaster 提供 framework case 与 later-version evolution pointer，未补出
  Books 当前缺失的长期机制。
- **Integration Decision / Score Correction / Open Questions**：`No Change — Already Covered`；TN 4→3、
  SR 4→3，总分 25→23。论文的 modular/reactive/multi-agent 机制成熟度低于初筛 novelty，且 event-time
  对照严重混合 specialized workflow、无 ablation/repeated uncertainty；不将 benchmark headline 或“自治科学”
  写入 Books。待验证 event-bound code/config/run artifact、matched-compute component ablation、durable
  experiment state/recovery、independent verifier、cross-run regression/rollback、physical lab safety 与真实
  developer-onboarding/time-to-domain evidence。

### CocoaBench — 24/30

- **Candidate / Week / Source Family**：`COCOABENCH-UNIFIED-DIGITAL-AGENT-EVAL`；W16；
  arXiv:2604.11201，唯一 v1 于 2026-04-13 首次公开。已读 task construction、evaluation functions、
  Cocoa-Agent scaffold、全量结果/cost/tool analysis、712 条失败轨迹 taxonomy 与 Appendix；论文没有
  独立 Limitations section。公开 benchmark/scaffold 链接可见，但本轮未发现 event-bound release digest。
- **Original Problem / Previous Design**：GUI、coding、search 单域 benchmark 能隔离某项能力，适合
  regression 与机制诊断；但真实 digital task 往往要跨模态取证、程序化处理和环境交互，单域高分不能
  证明 capability composition。完全开放的人类职业任务更真实，却依赖昂贵且一致性有限的人评。
- **Mechanism / State Ownership**：153 个 human-authored tasks 仅暴露 instruction、resources 与 per-task
  executable final-output evaluator，不绑定特定 runtime；98% 被标为需要多种 vision/search/coding 能力。
  Cocoa-Agent 以单 Docker sandbox 集成 browser DOM/screenshot、shell/file/code，并给 shared ReAct scaffold。
  benchmark owner 应拥有 task/resource snapshots、evaluator code/version、expected output schema 和 timeout；
  harness owner 拥有 tools/permissions/sandbox；system under test 拥有 model/scaffold identity；run 保存
  trajectory、tool result、final artifact 与 cost。final proxy 只能证明 evaluator outcome，不能倒推出正确
  process 或无副作用。
- **Evaluation Contract / Evidence**：complete systems 与 shared Cocoa-Agent 是两类不同实验；默认 30 分钟、
  50 turns，报告 153 tasks 的 success、平均成本和时间。Cocoa-Agent 失败分析由 Claude Sonnet 4.6 judge
  分类，而主 success 使用 task-specific executable evaluator。作者观察 coding tool usage 与 success
  正相关，但 model strength、scaffold、tool policy 和 task mix 共同混杂，不能推断“更多 coding calls
  导致更强”。外部网页/URL 仍会漂移；一次 task run、model snapshot、region/network、重试、并发和
  evaluator false-positive/negative calibration 未完整披露。
- **Trade-offs / Evolution**：`Direct Evolution`：single-capability benchmark → shared multi-tool scaffold →
  infrastructure-agnostic end-to-end tasks；获得 capability-composition 与真实 workflow coverage，代价是
  failure attribution 变弱、外部资源 drift、proxy loophole、模型×scaffold 交互和更高 run cost。单域/
  fixed-environment suites 继续承担诊断与稳定 regression；开放 benchmark 不能覆盖它们。
- **ROADMAP / Chapters Read / Decision**：已读 Ch61～63、Ch77 与 Ch80。Ch62 已明确
  `model+prompt+context+retrieval+tools+policy` subject identity、Agent outcome/trajectory/side-effect 分层、
  executable artifact 与 harness revision；CocoaBench 提供的是新的受限 benchmark 实例，没有补出新的
  长期机制。`No Change — Already Covered`，不写 Books。待验证 resource snapshots、proxy calibration、
  repeated runs/uncertainty、network drift、side effects、scaffold-component ablation 与 capability-conditioned
  slices。

### KnowRL — 24/30

- **Candidate / Week / Source Family**：`KNOWRL-MINIMAL-SUFFICIENT-HINT-CURRICULUM`；W16；
  arXiv:2604.12627，唯一 v1 于 2026-04-14 首次公开。已读 KP curation、S/T-LOO、CBRS、Constrained
  Subset Search、training/evaluation、ablation 和 appendices，并核对作者 code/model/data 入口。论文没有
  dedicated Limitations/Threats section，故跨域与 leakage 边界按公开协议保守处理。
- **Original Problem / Previous Design**：binary RLVR 在 hard prompt 上产生 all-zero groups，组内
  advantage 消失。增加 solution prefix/template hint 可把 policy 推进可奖励区域，但 token 多不等于信息
  更好：冗余/冲突 hints 增加 context 与 shortcut。无 hint RL 在 verifier 可靠、base success 足够时仍有
  最清楚 objective；full hint 适合教学/推理时允许外部知识的场景。
- **Mechanism / Data Flow**：对 1,374 math problems 先从 DeepSeek-R1 采到 verified correct solution，再
  抽取 atomic KPs、同模型 leakage review + manual repair。对每题估计 no-KP/full-KP/leave-one-out accuracy；
  LOO 会因相互依赖产生“单删有益、合删有害”的 pruning paradox。CSS 先剪候选，再在受限子集空间全局
  枚举，以离线 rollout accuracy 选择约 2.5 个 KPs。8.8K QuestA prompts 在训练时按需加入 `## Hint`，
  policy 用 rule reward 训练；inference 可去掉 hints。
- **State Ownership / Contract**：data pipeline 必须保存 problem、verified solution/verifier、KP text、
  extractor/reviewer identity、leakage verdict、候选集合、每个 subset 的 rollout seeds/count、CSS tolerance
  与 selected-set digest；RL run 保存 hint/no-hint flag、policy/reward versions。KP 是 derived curriculum，
  不是 authoritative knowledge；同一 teacher 同时生成 solution、抽取和审查会形成 correlated leakage。
- **Evaluation Boundary**：offline subset scoring 每配置 `8×32` samples；training batch 256、每题 8 rollouts、
  max response 24K、2,960 steps、64×H100（8 nodes×8 GPUs）、约 13 天，并在 step 2590 改 clip-high；
  evaluation 用 rule + fallback CompassVerifier、MATH/Olympiad mean@8，其余 mean@32。与 prior models 的
  leaderboard 含不同 recipes；CSS/CBRS matched-step comparison 支持 selection quality 影响 training，
  但整个 pipeline 同时改变 data、hinting、dynamic sampling 与 entropy annealing，不能把最终 +9.63
  单独归因于 CSS，也不能把 64-GPU/13-day pipeline称为低开销。
- **Trade-offs / Evolution**：`Direct Evolution`：no hint sparse reward → fixed/full hint → per-problem
  adaptive hints → interaction-aware subset curriculum。获得 mixed-outcome groups 与 compact guidance，
  付出昂贵离线 combinatorial evaluation、teacher/verifier dependence、selection overfit 和 knowledge
  leakage risk；新增 failure modes 是错误 KPs、互相消歧关系被剪断、benchmark-specific hints、subset
  estimate noise 与 curriculum/inference distribution gap。
- **ROADMAP / Chapters Read / Decision**：已读 Ch23、Ch28～30。Ch29 已覆盖 all-equal group、difficulty-
  dependent sample efficiency、curriculum/reward 调整；新增缺口是把 hint 视作 **带 provenance 的探索
  curriculum**，并说明单项 marginal ablation 不能代表联合删除。主 owner 暂定 Ch29，Ch23 只作 data-
  lineage handoff。provisional `Refine — Existing Argument (Experimental)`；Historical Books Gate 关闭。
  待 cross-domain、independent KP verifier、leakage audit、matched total-compute/no-hint curriculum、
  subset-search scaling、multi-seed 与 OOD evidence。

### LMM-Searcher — 24/30

- **Candidate / Week / Source Family**：`LMM-SEARCHER-VISUAL-ARTIFACT-PROGRESSIVE-LOAD`；W16；
  arXiv:2604.12890，唯一 v1 于 2026-04-14 首次公开。已读 context middleware、tool interface、query/
  trajectory synthesis、model merge、四 benchmark、interaction/data/tool ablations 与 case-study Appendix；
  paper 声称 code 将发布，当前 source identity 未形成 event-bound release。
- **Original Problem / Previous Design**：eager 把每轮网页图片塞进 context 语义直接、无需外部 pointer，
  但长 horizon 会积累 visual tokens；激进删图/只留 caption 节约 context，却丢失以后才发现重要的细节。
  固定 search-and-look workflow 在短任务或弱 visual agent 上仍更简单，paper 自身也观察到弱 backbone 对
  新 framework 的增益较小。
- **Mechanism / State Ownership / Flow**：middleware 截获 interleaved webpage，持久化图片，以 URL/UID
  替换 raw visual；context 保留 lightweight text pointer，Agent 需要时调用 `fetch_image` 恢复原图，再接
  crop/zoom 等 visual tools。source owner 拥有 bytes/URL/license/freshness；artifact store 应拥有 content
  digest、MIME、fetch time、ACL/retention 与 UID mapping；context 只持 pointer/caption；tool/runtime
  拥有 fetch result与 run-local residency。论文把有效 URL 直接当 UID，实际上 URL 不保证 immutable、
  unique、available 或同内容，故“一对一/永不丢失”是设计目标而非已证明 guarantee。
- **Training / Evaluation Contract**：用 synthetic multi-hop graph/fuzzification 构题，Seed-1.8 rejection
  sampling 保留 40 turns/64K 内成功轨迹，共 12,736 examples；Qwen3-VL-30B-A3B-Thinking SFT 3 epochs、
  batch 64、lr 1e-5，再以 α=0.8 与 MiroThinker merge。evaluation 30 turns/128K；100-turn variant 只保留
  最近 5 个 tool results，因而同时改变 horizon 与 context policy。论文未披露训练硬件、precision、
  sampling variance、cost、concurrency、network/cache contract 或 SLO；framework comparison 还混入
 不同 tools/prompts。fetch-image ablation 支持 active perception 有用，但不隔离 file store、caption、
  context truncation 与 model training。
- **Trade-offs / Failure Modes / Evolution**：`Direct Evolution`：eager multimodal context → caption/drop →
  pointer + on-demand exact fetch；获得 context locality 与可回访 evidence，付出 artifact store、lookup/
  latency、cache、ACL、garbage collection 与 pointer lifecycle。新增 stale URL、content substitution、broken
  link、caption hallucination、UID collision、prompt injection image、deletion leakage 与 fetch storm。
  真正系统 contract 应使用 content-addressed immutable snapshot，而不是把 URL 等同 identity。
- **ROADMAP / Chapters Read / Decision**：已读 Ch71～73、Ch77、Ch80。Ch72 已覆盖 evidence ingestion/
  retrieval/packing、Agent 局部 read、sufficiency 与 provenance；Ch77/80 已规定 artifact references、
  identity、event log 与 recovery。新增只是 visual artifact 的具体案例，没有超出现有机制。
  `No Change — Already Covered`；不写 Books。待 event-bound code/data、content-addressed snapshot、
  ACL/delete/freshness、matched-context ablation、latency/cache/fetch failure、independent runs 和真实 Web drift。

### Lightning OPD — 23/30（理论结论 Disputed）

- **Candidate / Week / Source Family**：`LIGHTNING-OPD-OFFLINE-TEACHER-CONSISTENCY`；W16；
  arXiv:2604.13010，唯一 v1 于 2026-04-14 首次公开。已读正文、全部公式与 proofs、implementation
  tables、training dynamics、teacher-cross ablation 和 evaluation templates；论文没有作者绑定的
  event-time code/release，网络上同名第三方 repository 不作为原始实现证据。
- **Original Problem / Why Previous Designs Were Reasonable**：standard OPD 从当前 student policy 采样
  rollout，再让 live teacher 对每个 student prefix 给 dense token-level log-probability；它能跟随 policy
  drift，但 teacher serving 与 actor training 长期并存，带来 GPU、调度、logit transfer 和故障耦合。固定
  teacher-generated SFT data 更便宜，却只覆盖 teacher state distribution。两者各自合理，问题是能否冻结
  student rollout distribution，同时保留 OPD 的 same-prefix dense supervision。
- **Changed Constraint / Mechanism**：Lightning OPD 先让某一 teacher 生成 SFT demonstrations，得到
  reference student `π_ref`；再从 `π_ref` 一次性采样 OPD rollouts，由同一 teacher 预计算每个 token 的
  log-probability，形成 immutable offline dataset。训练时只在线计算 student log-probability，以 clipped
  `log π_T - log π_θ` 更新。它把同步 `student rollout → live teacher score → update` 改为
  `reference rollout + teacher score materialization → repeated offline update`。
- **State Ownership / Control and Data Flow**：dataset owner 必须保存 prompt、response tokens/masks、
  SFT-teacher identity、OPD-teacher identity、reference checkpoint/tokenizer、teacher logits precision、
  rollout decoding contract 和 dataset digest；trainer 拥有 student/optimizer。所谓 teacher consistency
  不是名字相同，而是生成 demonstration 与打分的 checkpoint、tokenizer、template 和 policy contract
  可核对。冻结数据减少 live-service failure，却新增 stale coverage、large-logit storage、artifact deletion、
  corrupted/mismatched teacher score 和无法随 policy drift 补采样的 failure modes。
- **Implementation / Evaluation Contract**：Qwen3-4B-Base←Qwen3-8B 与 Qwen3-8B-Base←Qwen3-32B；
  SFT 3,000 steps、16,384 max sequence，OPD 150 steps、global batch 256、4,096 response、rollout
  temperature 0.8；evaluation 在 AIME 2024/2025、HMMT 2025、LiveCodeBench v5/v6，以 temperature
  0.6、top-p 0.95、math 32 samples/code 4 samples。作者报告 4B 72→20、8B 120→30 GPU-hours，
  但没有披露 GPU type、cluster topology、logit storage/I/O、重复 seeds/CI、energy、wall-clock、data
  preparation failure、并发或 production SLO；代码 OPD 还从 math checkpoint 初始化，混入 curriculum。
- **Empirical Evidence Boundary**：在该两组 Qwen teacher/student 与作者 pipeline 中，offline variant 与
  online OPD 的 benchmark 结果接近，且 teacher-cross grid 的 diagonal 均更好；这支持“teacher/data
  provenance 会影响 OPD”与“低 drift 时固定 rollouts 可成为工程分支”。它不证明 teacher identity 是
  所有 OPD 的必要条件，也不证明 3.6～4.0× 可迁移：对照缺硬件、variance 和等 I/O/storage contract，
  只测试两类 teacher family、单一 training horizon，且强 teacher/style/capability 同时变化。
- **Theoretical Claim Boundary / Dispute**：论文的 gradient-gap upper bound 依赖 bounded advantage、
  support coverage、bounded score 与 policy drift，只说明某些条件下 gap 可被界定；upper bound 中出现
  `Gσ_Δ` 不证明 mismatch 必然造成非零、不可消除 bias。更关键的是 Shared Fixed Point proof 声称：
  两个 mutually absolutely continuous measures 诱导 equivalent topologies，因此对某 tangent subspace
  在一个 inner product 下 orthogonal 也会在另一个 inner product 下 orthogonal。这个推论一般不成立：
  正权重改变 inner product，能保留零测集/拓扑，却不保留 orthogonality。后续把 stationary point 等同
  `KL(π_θ||π_T)` local minimum 的步骤也需要额外条件。因此“provably shares the same optimum”与
  “teacher consistency is necessary”标为 `Disputed`；这是本次数学审计结论，不是社区共识。
- **Trade-offs / Where Previous Designs Still Apply / Evolution**：`Direct Evolution`：teacher-generated
  demonstrations → student-on-policy + live teacher scoring → reference-policy offline materialization；
  获得 teacher service 解耦、可重放与较低在线资源，付出 teacher lineage lock-in、coverage drift、storage/
  I/O 和重建成本。policy drift 大、任务不断变化或需要探索新 states 时，standard online OPD 仍合理；
  只有 hard verifier 时 RLVR 仍可避免 white-box teacher；混合/未知 provenance 的 SFT 数据不能因本论文
  直接判废，应采用 mismatch diagnostics、reweighting 或重新 materialize。
- **ROADMAP / Chapters Read / Decision**：已读 Ch24～26 与 Ch28～30。Ch25 已有 same-prefix context
  distillation、teacher snapshot/refresh ownership、distribution gap 与 logit memory；新增价值是把
  **SFT demonstration teacher lineage 与 OPD scorer lineage** 纳入同一 artifact contract，并把 offline
  rollout materialization 作为 online OPD 的条件性分支。provisional `Refine — Existing Argument
  (Disputed theory, empirical mechanism only)`；Historical Books Gate 关闭，暂不写正文。待修正版证明、
  independent theory review、matched-hardware replication、mixed-teacher controls、logit storage/I/O、
  policy-drift threshold、不同 families 与长期训练 evidence。

### Block Diffusion Draft Trees / DDTree — 25/30

- **Candidate / Week / Source Family**：`DDTREE-BLOCK-DIFFUSION-SPECULATIVE-VERIFY`；W16；
  arXiv:2604.12989，唯一 v1 于 2026-04-14 首次公开。已阅读全文、公式、算法、全部实验、
  Appendix A 的数学证明与 Appendix B 的 benchmark 细节，并核对作者项目页和
  `liranringel/ddtree` 官方实现；repository 当前只有少量 commits、无 event-bound tag/release，
  因而代码可用于机制核验，但不能证明论文结果对应某个不可变版本。
- **Original Problem / Why Previous Designs Were Reasonable**：标准 speculative decoding 用小 drafter
  提议一条 continuation，再由 target 并行验证，在 drafter 便宜且命中率高时能保持 target distribution
  而降低 decode latency。EAGLE 类 autoregressive tree drafter 用 path-conditioned probability 建多分支，
  但通常每一深度仍需一次 drafter forward；DFlash 用一次 block-diffusion pass 同时产生未来各位置分布，
  drafting latency 更低，却只选一条路径。单路径在分布尖锐、verification kernel 不支持 tree mask、
  或高并发下 verifier 已是瓶颈时仍是合理设计。
- **Changed Constraint / Mechanism**：一次 DFlash pass 暴露的是每个未来位置的 marginal `q_i`，不是
  target 的 path-conditioned `p(y_i | y_<i)`。DDTree 将这些 marginals 乘成 factorized surrogate `Q`，
  在固定 node budget `B` 下最大化 surrogate expected acceptance length；所有 prefix mass 进入 max-heap，
  best-first 取 top-B nodes，且 top-B 自动满足 prefix closure，复杂度为 `O(B log B)`。构造出的 tree
  编译为 ancestor-only attention mask，在一次 target forward 中验证；runtime 沿 target 自身选择遍历，
  原子提交已接受 path，compact provisional KV，并把第一个 unmatched target token 作为下一轮 bonus。
- **State Ownership / Control and Data Flow**：drafter 只拥有单轮 ephemeral marginals；tree builder 拥有
  candidate nodes、parent/depth、surrogate mass 与 budget；target model 拥有输出语义和 accept/reject
  决定；serving runtime 拥有 tree mask、position IDs、provisional KV、commit/rollback；scheduler 应拥有
  `B` 与并发/显存预算。若把 surrogate score 当成 target probability，或未把 sibling KV 与 committed
  path 分离，就会破坏 correctness 与 cache lifecycle。
- **Implementation / Evaluation Contract**：实验覆盖 Qwen3-4B、Qwen3-8B、Qwen3-Coder-30B-A3B-
  Instruct 及对应 DFlash checkpoints，十项 math/code/chat tasks，temperature 0/1、最多 2,048 new tokens、
  bf16，tree budget `B∈{16,32,64,128,256,512,1024}`，在 8×H200 上 warm-up 后测试。DFlash drafter
  使用 FlashAttention-2；因其不支持 tree mask，DDTree target 使用 PyTorch SDPA，而 baselines 取 SDPA/
  FA2 中更快者。主表为每个 dataset-model-temperature **事后选择最佳 B** 的 speedup；各 task sample
  数从 AIME 的 30 到 HumanEval 的 164 不等。论文未披露 request concurrency、continuous batching、
  interconnect/topology、TTFT/TPOT tail、goodput、power、成本或 serving SLO。
- **What the Evidence Proves**：在上述 batch-1 风格作者协议中，利用一次 block-diffusion pass 的
  probability breadth 建树，能在所有 60 个 dataset-model-temperature cells 中提高相对 vanilla DFlash
  的作者测得速度；budget sweep 也显示 acceptance depth 随树变大通常增加，而 verifier work 最终抵消
  收益。数学最优性只对 factorized draft surrogate `Q` 和固定 node budget 成立，不是对 target distribution
  的 expected acceptance 最优性证明。
- **What It Does Not Prove**：best-B oracle 没有给出线上 budget controller，不能外推到 workload mix、
  paged KV、tensor parallel、continuous batching 或高并发。每位置 marginal 忽略已实现的前缀 token，
  因而高 `Q` path 未必是 target 高概率 path；实验没有将同等 target FLOPs、显存、kernel maturity 和
  queueing delay 下的 EAGLE/Medusa/OPT-Tree 做完整生产对照，也没有独立复现、quality regression、
  failure injection 或 stochastic exactness test。论文没有独立 Limitations/Threats section。
- **Trade-offs / New Failure Modes / Coexistence**：一次 drafter pass 的 breadth 换来更长接受路径，代价
  是 verifier tree nodes、irregular mask、KV compaction、metadata 与显存；过大 B 会降低速度。新增故障面
  包括 marginal/path mismatch、stale or mis-tuned budget、tree-mask kernel fallback、sibling KV 泄漏、
  partial commit、position-ID 错位和 batch fairness。分布尖锐或并发高时单路径 DFlash 更简单；强
  path-conditioned drafter 或已有高效 tree kernel 时 EAGLE/OPT-Tree 分支仍成立；无可靠 draft model 时
  autoregressive decode 仍是 correctness baseline。
- **Evolution / ROADMAP / Chapters Read**：`Direct Evolution`：autoregressive single-path draft →
  path-conditioned draft tree → one-pass block-diffusion single path → one-pass marginal-derived tree；
  `Layering / Dependency`：draft proposal → scheduler budget → target verification → transactional KV commit。
  已读 Ch43～45。Ch44 已覆盖 exact speculative sampling、verify depth as capacity、dynamic tree、drafter
  演进与 transactional KV；新增长期缺口是把 **surrogate probability 与 target probability 分离**，并将
  tree node budget 作为随并发、kernel 与 verifier cost 调节的 capacity，而不是固定“越大越好”。主 owner
  暂定 Ch44，Ch43/45 只需 placement 和 communication handoff。
- **Integration Decision / Open Questions**：provisional `Refine — Existing Argument (Experimental)`；
  Historical Books Gate 关闭，暂不写正文。待 event-bound artifact、独立复现、online B policy、等总
  verifier-work 对照、efficient tree-attention kernel、continuous batching/paged KV、TP/PP topology、
  stochastic exactness、tail latency/goodput 和 crash-safe KV commit 证据。

### TIP: Token Importance in On-Policy Distillation — 25/30

- **Candidate / Week / Source Family**：`TIP-OPD-TOKEN-SELECTION`；W16；arXiv:2604.14084，唯一 v1
  于 2026-04-15 首次公开。已读全文、两轴 taxonomy、descent-bound derivation、全部 math/agentic
  experiments、supplementary ablations、hyperparameters、qualitative examples 和 Limitations，并核对作者
  `HJSang/OPSD_OnPolicyDistillation` repository。当前 main 是多论文共享实现、17 commits、无 release/tag；
  可核验 training surface，但不能把 current code 当成 event-time immutable artifact。
- **Original Problem / Why Previous Designs Were Reasonable**：all-token OPD 对 student rollout 的每个
  output token 计算 teacher/student distribution divergence，objective 最清楚，且不会因 selector 丢掉
  稀有纠错信号；代价是 full-vocabulary logits、loss/gradient memory 与大量已掌握 token 的更新。只按
  student entropy 选择 uncertain tokens 可降低监督量，但 student 对“自信而错误”的 token 恰好低熵，
  因此 uncertainty 不能独立代表 teachability。
- **Mechanism**：TIP 以 student entropy `h_t` 和 teacher–student divergence `δ_t` 建四象限：高熵高分歧、
  高熵低分歧、低熵高分歧（Q3 overconfident error）、低熵低分歧。用 batch 内 min-max normalized
  Soft-OR `s=h+δ-hδ` 排序，保留 top-ρ tokens，仅对这些位置求 reverse-KL；Q3-only 实验则以
  forward-KL×confidence 找 confident disagreement。selector 计算依赖同一 teacher logits，因此节省的是
  **direct supervision/loss materialization**，不是跳过 student/teacher 对完整 prefix 的 causal forward。
- **State Ownership / Control and Data Flow**：rollout owner 保存 prompt/token/mask 与 generating-policy
  version；teacher scorer 拥有 teacher identity/logits；selector 拥有 entropy/divergence definition、KL
  direction、normalization scope、retention ratio、top-k tie policy 和 mask；trainer 只对 mask positions
  累积 OPD loss。multi-turn/tool trajectory 还必须区分 LLM tokens 与 environment tokens。若只保存筛后
  token 而丢掉上下文与 selector revision，就无法重放“为何这个 token 被监督”。
- **Theory Boundary**：oracle weight 来自 smoothness descent bound，但 token-separable derivation显式
  忽略 off-diagonal gradient covariance 并把 mean interaction 当 lower-order；它给出解释性 proxy，
  不是 Soft-OR 为全局最优 selector 的证明。Entropy sampling 只有在每个 token sampling probability
  非零且做 importance weighting 时保持 unbiased；deterministic Top-K mask 则有意接受 bias。Q3/Q4 的
  语义标签也由特定 teacher disagreement 定义，teacher confident error 会把错误信号升级为“重要”。
- **Evaluation Contract / Evidence**：math 覆盖 Qwen3 8B→4B、Llama 70B→8B、Qwen2.5 14B→1.5B；
  DAPO prompts，MATH-500 与 AIME 2024/2025，16 rollouts/prompt、8,192 response、batch 8、TP2，
  8×H200（前两组）或 4×H200。Agentic 以 Qwen3 14B/32B→1.7B，在 DeepPlanning 80/20 split 训练
  15 epochs；全部 evaluation 为 temperature 1.0 的 mean@16。50% entropy/Soft-OR retention 在多数
  cells 接近或超过 full tokens，Q3-only 少量 tokens 在若干 cells 接近 baseline；但 AIME sample size 小，
  没有 independent seeds、end-to-end wall-clock、throughput、energy、data-loader/I/O 或 production SLO。
- **What the Evidence Does Not Prove**：peak-memory 减少不等于训练 FLOPs 或 wall-clock 按 retention
  比例减少；未选 token 仍存在于 sequence context，且 teacher/student forward 未被消除。Soft-OR 并非
  所有 cells 最优，20% retention 有退化；DeepPlanning 的 constraint fraction 不等同真实 Agent side-effect
  correctness。结果不覆盖 forward-KL/JSD、black-box teacher、noisy/weak teacher、multilingual/code/tool
  traces、batch outliers、curriculum drift 或与 random/gradient-oracle 的完整 matched-budget 对照。
- **Trade-offs / Failure Modes / Evolution**：获得监督 token 与 peak-memory 压缩、显式保留 confident
  disagreement；付出 full teacher scoring、sorting/masking 和 selector bias。新增 failure modes 是 batch
  outlier 扭曲 min-max、retention threshold 抖动、teacher error 被高 divergence 放大、rare token 永久
  饿死，以及 reported “token efficiency”被误写成 compute efficiency。all-token OPD 在 teacher 可靠性未知、
  序列短或实现简单性优先时仍成立；entropy-only 在没有 teacher full distribution 或只需一阶 heuristic
  时更便宜；gradient/learnability selector 是另一条更昂贵分支。
- **ROADMAP / Chapters Read / Decision**：已读 Ch24～26 与 Ch28～30。Ch25 已覆盖 KL direction、
  token reduction、student-prefix supervision 与 teacher lineage；新增机制是把 **uncertainty 与
  disagreement 分成两个轴**，并要求 retention ratio、normalization、mask 和 teacher reliability 成为
  objective contract。主 owner 暂定 Ch25。provisional `Refine — Existing Argument (Experimental)`；
  Historical Books Gate 关闭，暂不写正文。待 immutable code/results、multi-seed、matched wall-clock/
  FLOPs、random/gradient controls、forward-KL/JSD、noisy teacher、long-horizon tool masks 与 adaptive
  normalization 复核。

### KV Packet — 26/30

- **Candidate / Week / Source Family**：`KV-PACKET-CONTEXT-INDEPENDENT-CACHE`；W16；
  arXiv:2604.13226，v1 2026-04-14、v2 04-17。事件按 v1 归周；v2 的文字与实验补充只用于
  revision 核验。论文 metadata、完整 HTML、公式、实验、ablation、limitations 与作者 repository
  入口于 2026-08-10 核验。
- **Access / Full-read Coverage**：已覆盖 KV/RoPE background、fine-tune 与 selective-recompute
  baselines、Header/Trailer soft-token formulation、self-supervised two-pass distillation、四个 datasets、
  FLOPs/TTFT contract、KV compression compatibility、universal/cross-domain adapters、token-count
  ablation、attention analysis、limitations 和 conclusion；论文没有独立 Appendix。
- **Original Problem / Why Previous Designs Were Reasonable**：prefix cache 在 prefix、position、model
  identity 完全一致时最可靠；动态 multi-document RAG 会改变每个 document 的前缀，使独立预计算 KV
  缺少跨块上下文。Full recompute 保持语义但 TTFT 高；selective recompute 用 online compute 修复关键
  tokens；model modification 把组合能力写入权重，却可能改变通用能力。三条旧路线分别适合高正确性、
  可接受 online compute 或可控制模型训练的场景。
- **Changed Constraint / Mechanism**：KV Packet 把每个 document cache 视作 immutable packet，在文档
  embedding 两侧加入全局共享、可训练的 Header/Trailer soft tokens，离线分别生成 packet KV；online
  只做 RoPE shift 与 cache concatenation。训练时 full-prefill self teacher 给出 continuation distribution，
  packet student 仅更新 adapters，以 token-level KL 学习消解块边界 attention artifact。
- **State Ownership / Control and Data Flow**：knowledge base/version owner 持有原始 document 与 chunk
  identity；offline cache builder 持有 `(model revision, tokenizer, RoPE config, adapter revision, document
  hash)` packet；retriever 只选择 packet；serving runtime 负责 positional realignment、residency 与拼接；
  query/decode 产生 request-owned KV。Adapter 是 model-specific derived state，不能改变 document truth，
  也不能在 model/adapter/chunk revision 后继续静默复用。
- **Implementation / Evaluation Contract**：8 Header + 8 Trailer tokens，adapter float32、model bf16；
  Llama-3.1-8B-Instruct 与 Qwen-3-4B-Instruct，单张 A100 80GB，256～512 samples、batch 64、30 epochs；
  NIAH、Biography、HotpotQA、MusiQue。TTFT 包含 CPU→GPU cache load、RoPE shift/recompute 与 query
  processing，但明确排除 offline packet generation；论文没有并发、batching、PCIe/NVLink topology、
  cache hit distribution、tail latency、goodput、energy 或 production SLO。
- **What the Evidence Proves**：在上述两类模型、四项任务与作者实现中，少量 boundary adapters 能显著
  修复 naive disjoint-cache concatenation，并把 online repair 从 partial forward pass 降为 rotation +
  concatenation；cross-domain/universal 与 token-count ablation 支持收益不只是单 dataset memorization。
  Attention 图只说明 adapters 吸收 boundary sink mass 与结果相关，不建立其为唯一因果机制。
- **What It Does Not Prove**：`near-zero FLOPs` 只计算 online alignment，不包含 offline cache build、
  adapter training、storage、transfer 与 cache miss；aggregate F1 不证明 logits 与 full-prefill 等价。
  两个 model families 和独立 documents 不能外推 dependent reasoning traces、强 OOD corpora、任意
  position encoding、quantization、LoRA/tenant adapters 或 serving concurrency。论文没有 failure
  injection、packet corruption、version mismatch、deletion propagation 或 security/ACL evaluation。
- **Trade-offs / New Failure Modes / Coexistence**：获得 recomputation-free composition 与 compression
  compatibility，付出额外 soft-token KV、offline packet materialization、adapter/version registry 和
  storage invalidation。新 failure modes 包括 stale packet、document–packet hash mismatch、不同 adapter
  混拼、OOD boundary failure、dependent-document semantics 丢失、CPU→GPU transfer 主导 TTFT，以及
  删除原文后 derived KV 仍残留。静态 prefix cache、full recompute 与 selective repair 仍分别在高 hit、
  高 fidelity 和无法预训练 universal adapter 时成立。
- **Evolution / ROADMAP / Chapters Read**：`Direct Evolution`：exact-prefix reuse → positional repair +
  selective recompute → offline learned packet boundary；`Layering / Dependency`：retrieval identity →
  packet registry → KV residency/concatenation → request decode。已读 Ch41～43；Ch41 已覆盖 prefix
  identity、lifecycle 与 correctness，Ch43 覆盖 physical placement。长期缺口是把 context-independent
  packet 作为带 model/chunk/adapter identity 和 invalidation contract 的 derived KV artifact；主 owner
  暂定 Ch41，Ch43/48/51 只作 placement/transfer handoff。
- **Integration Decision / Open Questions**：provisional `Refine — Existing Argument (Experimental)`；
  Historical Books Gate 关闭，暂不写正文。待复现 concurrent RAG、real hit/miss distribution、不同
  interconnect、quantized/LoRA models、dependent documents、packet corruption 与 delete/version rollover，
  并用 end-to-end TTFT/TPOT/goodput/cost 与 full/selective recompute 做同一 SLO 下比较。

### Self-Distillation Zero — 25/30

- **Candidate / Week / Source Family**：`SD-ZERO-VERIFIER-TO-DENSE-SELF-SUPERVISION`；W16；
  arXiv:2604.12002，v1 于 2026-04-13 首次公开，v2 2026-06-11。事件按 v1 归周；v2 只用于
  revision 核验。已读 metadata、全文、公式、Algorithm 1、实验、ablation、分析、Appendix 与作者
  code 入口。
- **Original Problem / Why Previous Designs Were Reasonable**：RLVR 的 binary outcome reward 通用且
  不要求逐 token 标注，但长 reasoning trace 的 credit assignment 稀疏；rejection SFT 只保留成功答案，
  简单稳定，却丢弃失败轨迹中的局部信息；external-teacher distillation 提供 dense logits，但增加 teacher
  provenance、能力差距与成本。三者分别在 verifier 可用、成功样本充足或外部 teacher 可信时合理。
- **Changed Constraint / Mechanism**：第一阶段 Self-Revision Training 让同一 base model 先生成尝试，
  binary verifier 标记正确/错误，再把完整尝试、reward 与“rephrase/start over”指令交给 reviser；仅保留
  revision 成功的轨迹，同时训练 revision 与 ordinary generation。第二阶段 current generator on-policy
  采样 `y`；冻结的 SRT checkpoint 在同一 prefix `y_<t` 上额外看到完整 `y` 与 reward，并输出 top-K
  token distribution；student 以 reverse-KL 模仿。Teacher 定期同步为新 student checkpoint，形成
  generation → hindsight revision → dense distillation → refresh 的闭环。
- **State Ownership / Control and Data Flow**：verifier owner 持有 problem、reference/final answer、
  execution/test policy 与 reward version；rollout owner 保存 prompt、完整 attempt、sampling config 和
  generator checkpoint；reviser/teacher state 包含 SRT checkpoint、privileged prompt、top-K truncation 与
  refresh cadence；trainer 保存 student、optimizer、teacher snapshot 和同步 recovery point。遗漏 teacher
  identity 或把不同 verifier 版本混入同一 buffer，会静默改变 dense target。
- **Implementation / Evaluation Contract**：Qwen3-4B-Instruct 与 OLMo-3-7B-Instruct，math/code tasks；
  15K questions 分给两个阶段，SRT 约 6K successful revision traces；sampling temperature 0.7、最大训练
  response 16K，evaluation 最大 32K 并报告 avg@8。Self-distillation 使用 4 GPUs、TP4、bf16、top-K=64；
  GRPO baseline 使用 8 GPUs/FSDP 等不同执行路径。论文用约 224.5M sampling tokens 与约 219M training
  forward tokens 描述预算，但没有统一 GPU-hour、wall-clock、energy 或 production SLO，因此只能称
  question/sample-budget 与近似 token-budget 对齐，不能称端到端 compute 等价。
- **What the Evidence Proves / Does Not Prove**：在上述两种 4B/7B 模型和作者 math/code contract 中，
  binary-verified self-revision 可产生比 sparse outcome 更密的 token targets，周期 teacher refresh 的
  ablation 支持多轮继续收益。KL hotspot 与关键词分析最多支持“teacher/student disagreement 集中于若干
  位置”，不证明模型因果定位了真实错误 token。`Zero` 只表示无外部 teacher/人工 demonstrations；系统仍
  依赖可验证 final answer、binary checker、成功 revision filtering 和 teacher 可见完整失败尝试的
  privileged hindsight，不能外推开放域偏好、不可验证 Agent 副作用或无需监督。
- **Trade-offs / New Failure Modes / Coexistence**：获得 dense supervision 与失败轨迹复用，付出额外
  reviser forward、teacher logits、top-K approximation、snapshot synchronization 和 verifier dependence。
  新 failure modes 包括 reward leakage、错误 verifier 被 dense 放大、teacher/student 共振塌缩、refresh
  后不可重放、长失败 attempt 暴露答案模式，以及把 sample efficiency 误报为 total-compute efficiency。
  RLVR 在探索和 verifier 可靠时仍成立；rejection SFT 在成功样本多且追求简单性时更稳；external teacher
  在需要跨模型能力迁移时仍可能更强。
- **Evolution / ROADMAP / Chapters Read / Decision**：`Direct Evolution`：binary outcome → filtered
  self-revision → same-prefix privileged distillation → periodic self-refresh。已读 Ch24～30；Ch25 已覆盖
  same-prefix context distillation、teacher snapshot/cadence 和 evidence boundary。新增可沉淀点是
  **binary reward 经 privileged reviser 转换为 dense target 时，必须记录 future-attempt visibility、
  verifier identity 与 refresh state**。主 owner 暂定 Ch25，Ch27/29 只作 reward-source handoff；
  provisional `Refine — Existing Argument (Experimental)`。Historical Books Gate 关闭，暂不写正文。

### C2: Scalable Rubric-Augmented Reward Modeling — 22/30

- **Candidate / Week / Source Family**：`C2-COOPERATIVE-CRITICAL-RUBRIC-RM`；W16；arXiv:2604.13618，
  唯一 v1 于 2026-04-15 首次公开，标注 ACL 2026。已读 metadata、全文、方法、reward definitions、
  四组 RM benchmark、DPO/best-of-N/rejection-sampling downstream、compute-matched comparison、noise
  stress、component ablation、latency、人工 error analysis 与 Appendix prompts/hyperparameters。
- **Original Problem / Why Previous Designs Were Reasonable**：scalar/pairwise reward model 不显式暴露
  判定依据，但一次 inference 简单、延迟低；外部强模型生成 rubric 可提高 criterion coverage，却增加
  annotation/serving 成本与外部依赖；self-rubric 便宜，但同一模型产生的低质量 criteria 可能反向误导
  verifier。旧方案分别适合延迟敏感、可承担强 teacher 或 rubric 风险较低的场景。
- **Changed Constraint / Mechanism**：base model 对每个 preference pair 采样 K=16 rubrics，分别测量
  rubric-free 与 rubric-conditioned judgment 对 gold preference margin 的变化；向正确 label 推动的样本标为
  helpful，反向推动标为 misleading。Generator 以 helpful/misleading contrast 训练；verifier 同时学习
  rubric-free judgment、rubric quality assessment 与 preference prediction。Inference 先生成 rubric，
  verifier 若判 helpful 才采用，否则回退/重试 rubric-free path。
- **State Ownership / Control and Data Flow**：preference-data owner 保存 pair、gold label、rubric/version
  和 provenance；synthesis owner 保存 base generator/verifier identity、sampling seed、K 与 margin rule；
  generator checkpoint 产出 candidate rubric；critical verifier 持有 assessment policy、retry/fallback 与
  final judgment。Rubric label 是 `(pair, gold label, base verifier revision)` 的 derived state，不是脱离
  verifier 的事实；更换 base verifier、position order 或 prompt template 必须重新生成或重新校准。
- **Implementation / Evaluation Contract**：Tulu3-8B-SFT 与 Qwen3-8B；从 UltraFeedback 取 5K pairs，
  形成约 14.8K/14.3K rubric-free、helpful、misleading instances；三 training seeds。RM 评测覆盖
  RewardBench、RM-Bench、RewardBench2、JudgeBench；downstream 用额外 20K prompts、每题 8 responses
  构造 DPO pairs，并由 GPT-4o/GPT-4.1 评估 AlpacaEval/Arena-Hard。C2 平均生成 token 约为 reasoning RM
  的 2.3～2.4 倍；单 A100 80GB/vLLM 上平均 latency 也约 2.3～2.4 倍。Compute-matched majority-vote、
  noisy-rubric stress、generator/verifier/negative-rubric ablation 和 80-sample blind author error analysis
  提供了机制边界，但没有 production concurrency、tail latency、cross-domain human calibration 或 SLO。
- **What the Evidence Proves / Does Not Prove**：在作者数据和两个 8B backbones 下，训练 generator 与
  selective verifier 的组合优于同数据 reasoning RM 和 naive self-rubric，且结果不只由生成 token 数解释；
  negative rubrics 对 critical gating 有实证价值。它不证明自生成 rubric 客观正确：helpfulness 是该 base
  verifier 相对 gold pair 的 margin shift，可能编码 position/length/style shortcut。Rubric quality 的一部分
  又由 GPT-5 或作者人工评分，downstream 由 model judges 评估；相关 evaluator bias 不能消除。弱模型在
  高质量 rubric 占比高时会错误拒绝有用 rubric，说明 selective gate 本身也有 false-negative cost。
- **Trade-offs / New Failure Modes / Coexistence**：获得显式 criterion、对 misleading guidance 的条件
  拒绝与较强 pair discrimination；付出 rubric generation、retry、约 2.4x latency/token、双 checkpoint
  版本和 derived-label regeneration。新增 failure modes 是 generator/verifier collusion、endogenous label
  feedback loop、rubric prompt injection、错误 fallback、criteria drift 与 preference dataset bias 被解释性
  文本包装。Latency-sensitive serving 仍可用 rubric-free RM；高风险领域可用独立专家/static rubric；
  verifiable tasks 优先 executable verifier，而不是生成 rubric。
- **Evolution / ROADMAP / Chapters Read / Decision**：`Direct Evolution`：opaque pair score → external/
  self rubric → contrastively trained rubric → verifier-gated rubric；`Layering / Dependency`：preference
  provenance → rubric synthesis → quality gate → final score → downstream policy selection。已读 Ch27、
  Ch30、Ch62～63；Ch27 已覆盖 reward provenance 与 Goodhart，Ch62 已覆盖 rubric version、judge
  calibration、independence 与 cost contract。C2 提供“负 rubric + fallback”这一具体机制，但不改变现有
  设计结论；provisional `No Change — Already Covered`，主 owner Ch62。Historical Books Gate 关闭，
  暂不写正文。

### The Past Is Not Past / MEDS — 25/30

- **Candidate / Week / Source Family**：`MEDS-HISTORY-AWARE-ERROR-REWARD-SHAPING`；W16；
  arXiv:2604.11297，唯一 v1 于 2026-04-13 首次公开。已读 27 页 PDF、theory proof、全部实验、
  clustering/representation ablation、diversity analysis、Appendix hyperparameters、examples、limitations 与
  作者 repository 入口。
- **Original Problem / Previous Design**：entropy bonus 鼓励 current policy 保持随机性，batch-level
  diversity weighting 避免同批 collapse，二者都不记得跨 epoch 重复出现的同一错误 basin；简单静态
  verifier/reward 易实现且状态少，在 rollout history 不可靠、任务变化快或隐私要求高时仍合理。
- **Mechanism / State and Data Flow**：对每个 prompt 维护 error memory `G_x`。失败 response 的 final-answer
  首 token 在后半 Transformer layers 上对应 token logit 被串接、L2 normalize；HDBSCAN 以 Euclidean
  distance 聚类。属于 cluster `C_k` 的 response 获得 `min(alpha log(|C_k|+1), beta)` 额外负 reward；
  noise cluster 不形成同等重复惩罚。rollout owner 保存 prompt/policy/verifier version；feature extractor
  保存 layer/token-selection contract；memory owner 保存 per-prompt vectors、cluster revision 与 retention；
  trainer 使用 shaped reward。它是训练期间的 derived state，不是可直接复用的语义 memory。
- **Theory / Evaluation Contract**：proof 在有限 response space、精确 KL-regularized Gibbs one-step update
  下成立，并显式假设 `c(y1)>=c(y2) => r(y1)<=r(y2)`，即重复更多的项不会有更高真实 task reward。
  HDBSCAN/logit proxy 是否满足该单调假设并未由定理证明。实验用 Qwen3-1.7B、Qwen3-8B、
  Qwen2.5-Math-7B，DAPO-Math-17K + MATH level 3–5，batch 512、每 prompt 16 rollouts、H200；
  response 上限 7,168 或 3,072 tokens。五项 math benchmark 以 temperature=1、top-p=1、seed=0、
  128 samples 报 pass@1/pass@128；未披露 H200 数量、wall-clock、memory growth、cluster rebuild latency、
  multi-seed uncertainty 或 production SLO。
- **Evidence Boundary / Trade-offs**：作者设置中 MEDS 平均优于 GRPO、DAPO 与 entropy-advantage，
  representation ablation、Claude-Haiku-4.5 对 800 failures 的 proxy taxonomy 与 diversity metrics 支持
  “历史聚类影响探索”，不证明 final-answer token logits 是通用 reasoning identity，也不证明 cluster
  agreement 导致性能提升。获得跨 step 避免重复错误，付出 O(prompts × history) state、online clustering、
  hyperparameter sensitivity 和 model-internal feature coupling。新 failure modes 是正确但常见 strategy 被
  误罚、同义错误逃逸、cluster drift、checkpoint 恢复丢 memory、跨 model revision feature 不兼容与
  private trace retention。
- **Evolution / ROADMAP / Decision**：`Direct Evolution`：stateless outcome reward → within-batch diversity
  → cross-step error memory → density-shaped reward。已读 Ch27～30、Ch57、Ch73；主 owner 暂定 Ch29，
  Ch57/73 只作 training-state/provenance handoff。现有 Ch29 已覆盖 exploration 与 reward shaping，但缺
  **history state 的 ownership、expiry、checkpoint atomicity 及误聚类边界**；provisional `Refine — Existing
  Argument (Experimental)`。Historical Books Gate 关闭，暂不写正文。

### You Only Judge Once / YOJO — 22/30

- **Candidate / Week / Source Family**：`YOJO-SINGLE-PASS-MULTI-RESPONSE-RM`；W16；arXiv:2604.10966，
  v1 2026-04-13、v2 04-15。事件按 v1 归周。已读 22 页 PDF、method、benchmark construction、training/
  GRPO、efficiency、design ablations、appendix、ethics、reproducibility 与 limitations；论文称 weights/data
  publication 后发布，event-time immutable artifact 未见。
- **Original Problem / Mechanism**：independent discriminative RM 对 N 个 candidates 重复编码相同 prompt/
  image/video，score 可独立缓存且语义稳定，但 FLOPs/latency 近线性增长。YOJO 把 N responses 用唯一
  separator 串接进一个 causal sequence，在每条 response 最后 token 取 hidden state，经 two-layer SiLU
  value head 产出 N scores，以 best-index cross-entropy 训练；N=2 时退化为 Bradley–Terry。后置 response
  可 attention 到前置 candidates，形成直接 comparative context。
- **State / Control / Semantics**：batch/list constructor 持有 prompt、media、candidate IDs、order、N 与
  truncation；model runtime 一次编码共享 media/prompt；value head 输出 list-conditioned scores；selector
  只在同组中选 best。训练随机 shuffle 候选以减弱 position bias，但 causal mask 仍使 score 依赖 order 和
  group composition，因此它不是可跨不同 candidate set 比较的绝对 reward。部署必须记录 permutation，
  并用 permutation consistency 作为 correctness metric。
- **Evaluation Contract / Evidence Boundary**：Molmo2-4B 与 Qwen3-VL-4B，LoRA rank 64、alpha 16、
  dropout .05、3 epochs、batch 64、max sequence 24,576；MR2Bench-Image 240 full rankings，
  MR2Bench-Video 由 497 questions/489 videos/约 94K pairwise labels 经 preference-graph denoising构造。
  单 H100 80GB 上 N=4 对 Molmo2 报最高约 3.9x latency/4.0x FLOPs reduction；共享 encoding 和 sequence
  shape 是该数字的适用条件，不是任意 N 的保证。实验只主测 N<=4（小样本 efficiency curve 到 16），
  video best-of-4 最高仅 50.7%；无 concurrency、tail latency、跨 request batching、长 list truncation 或 SLO。
- **Trade-offs / Evolution / Decision**：获得 shared encoding 与 listwise comparison，付出候选间干扰、
  order sensitivity、较长 context 和无法独立缓存 score。Independent RM 在 N 小、异步 candidates、需要
  stable scalar/caching 时仍成立；two-stage shortlist + joint rerank 是更实际共存路线。`Direct Evolution`：
  independent scalar → pairwise loss → single-sequence N-way rerank。已读 Ch27、Ch48、Ch62；Ch27/62 已
  覆盖 reward/judge contract，新增主要是 **list-conditioned score identity 与 permutation test**。主 owner
  暂定 Ch62；provisional `Refine — Existing Argument (Experimental)`。Books Gate 关闭。

### RationalRewards — 22/30

- **Candidate / Week / Source Family**：`RATIONALREWARDS-PARROT-VISUAL-CRITIC`；W16；
  arXiv:2604.11626，v1 2026-04-13、v2 04-14；正文 PDF title/section header 曾保留 “Think Before You
  Score”，source family 以 arXiv metadata 的 RationalRewards 为准。已读 31 页 PDF、ELBO derivation、
  PARROT 三阶段、pointwise projection、RM/RL/test-time experiments、ablation、prompts、hardware、dataset、
  benchmark、limitations，且核对 project/code/model/data release 声明。
- **Mechanism / State and Data Flow**：Qwen3-VL-32B teacher 在已知 pairwise preference label 条件下生成
  四维 rationale；同一 teacher 去掉 label 后重新判断，只有能恢复 gold preference 的 rationale 通过
  consistency filter。8B student 用这些 samples SFT，在不见 label 时生成 rationale/score。为支持单图
  deployment，teacher 再以 validated pair rationale 为 hint，把 pairwise judgment 投影成 pointwise 1–4
  scores。下游一条路把维度分数平均成 diffusion RL reward；另一条路把 critique 变成 refined prompt，
  低于 threshold 时重新生成。
- **Evidence Boundary**：约 80K raw pairs、约 57.6K filtered（约 72% retention），teacher-anchored + filter
  优于同数据 direct distillation；多个 visual preference benchmarks、generator families、RL 与 prompt-tuning
  experiments 支持该 pipeline 在作者 contract 下有用。它不证明 rationale faithful：同一 teacher 既生成又
  复核，filter 只测“能否恢复 preference”，不验证视觉事实或排除 label-conditioned post-hoc justification；
  pointwise projection 又超出 pairwise ELBO，假设 pairwise criteria 可转成绝对分数。所谓减轻 reward
  hacking 主要来自 curves/qualitative examples，缺独立 causal audit。
- **Implementation / Trade-offs**：Diffusion RL 用 16×A100-80GB（8 train + 8 reward）、group 16、LoRA
  rank 64；GCR 的 reward-model critique/refine 额外约 0.4s/image，但未包含重新生成的 dominant cost。
  获得多维可行动 feedback 与 parameter/prompt 两条优化接口，付出 teacher bias、rationale latency、score
  aggregation choice 与额外 generation。新 failure modes 是 persuasive hallucinated critique、同源 evaluator
  collusion、threshold oscillation、prompt over-specification、用户意图漂移及 bias amplification。Scalar RM
  在 latency/throughput 优先时仍合理；independent human/static rubric 在高风险任务更可信。
- **Evolution / ROADMAP / Decision**：`Direct Evolution`：opaque scalar → preference-anchored rationale →
  consistency-filtered student → pointwise critic → parameter-space or prompt-space optimizer。已读 Ch27、
  Ch62、Ch74、Ch77；主 owner 暂定 Ch62，Ch27/77 只作 reward/workflow handoff。Ch62 已覆盖 judge
  provenance、rationale 非证明、independent verifier 与 cost contract，因此 provisional `No Change —
  Already Covered`；其视觉生成案例保留 Weekly，不新增 Books 正文。Books Gate 关闭。

### UI-Copilot — 24/30

- **Candidate / Week / Source Family**：`UI-COPILOT-TIPO-DECOUPLED-GUI-STATE`；W16；
  arXiv:2604.13822 v1 2026-04-15，后续 ACL 2026 archival version 用于全文核验，不倒灌事件日期。已读
  architecture、TIPO objective、data construction、main/verified benchmark、inference/training/data ablations、
  error analysis、prompts、failed cases 与 limitations；未发现可核验的 event-time official code artifact。
- **Original Problem / Mechanism**：把全部 screenshot/thought/action history 留在 context 最简单且可重放，
  但长 GUI trajectory 易 context overload；每步都调用 planner/copilot 稳定但昂贵。UI-Copilot 把详细
  observations/trace 存为 local JSON knowledge，只把 compact progress summary 留在 dialogue；policy 每步
  选择 `Retriever`、`Calculator` 或 none。Retriever 读取 task、summaries 与 local history；Calculator 由
  Qwen3-4B 生成 Python 并执行。TIPO 把 tool selection 与 action execution 拆开：tool dataset 用 off-policy
  summaries 做 single-turn rule-reward learning，action dataset 用 self-generated multi-turn history 做 on-policy
  rollout，避免 expert-history 与 deployment-history mismatch。
- **State Ownership / Failure Semantics**：environment owner 持有 app/device state 与 side effects；trace store
  持有 raw observations、actions、timestamps 与 ACL；summary owner 维护 compact progress state；policy
  决定 tool type；copilot 只返回 derived result；executor 必须 sandbox code。论文没有定义 summary/raw-trace
  原子 checkpoint、stale retrieval、tool timeout/retry、Python capability、secret redaction、跨 session identity
  或 rollback，因此“memory decoupling”不能只按 prompt 压缩实现。
- **Evaluation Contract / Evidence Boundary**：Qwen2.5VL-7B policy + Qwen3-4B copilot；action RL 2,000
  trajectories、tool RL 600 queries、group size 8，动态重采样直到 advantage std >0.3。MemGUI-Bench 平均
  golden path 约 36 steps，reported pass@1 16.4%/pass@3 20.3%；AndroidWorld with tools 39.1%，比同表 base
  Qwen 22.0% 高 17.1 points。Verified subsets 仅 55/60 tasks，GPT-4o 参与 expert/tool data 与 error taxonomy；
  baseline rows混合作者复测与 paper-reported、不同 history/tool/workflow contract。结果支持 architecture +
  TIPO bundle，不隔离长期 state protocol 的 production correctness；无 seeds/CI、latency/cost、device reset
  failure、concurrency、security 或 SLO。
- **Trade-offs / Evolution / Decision**：获得 context isolation、按需 specialist 与 on-policy execution data，
  付出第二模型、trace store、summary drift、tool routing与更复杂 recovery。Full history 在短任务/强 audit
  时仍合理；always-on copilot 在高风险低吞吐任务可换稳定性；deterministic calculator/retriever service 可比
  model copilot 更易验证。`Direct Evolution`：full in-context trace → compact summary → external raw history
  → selective retrieval/calculation；`Layering`：state lifecycle → tool router → action policy。已读 Ch73～80；
  Ch73/77/80 已覆盖 source/derived memory、tool contracts、sandbox 与 recovery，因而 provisional `No Change —
  Already Covered`。Books Gate 关闭。

### SemaClaw — 23/30

- **Candidate / Week / Source Family**：`SEMACLAW-HARNESS-APPLICATION`；W16；arXiv:2604.11548
  唯一 v1 于 2026-04-13 14:37 UTC 首次公开。论文正文署 `March 28, 2026` 并链接
  `midea-ai/SemaClaw`，但公开 repository 页面与无 tag 的提交列表不能在本次核验中证明该日期已有
  等价公开 artifact，故事件仍按可验证的 arXiv v1 归 W16。它依赖已单独审计的
  `SEMA-CODE-EMBEDDABLE-AGENT-ENGINE`，不是重复计分，而是 runtime 上层 application harness。
- **Access / Full-read Coverage**：已读 arXiv HTML 的 Introduction、Technical Foundations、全部
  Design and Implementation、Open Questions、Conclusion/Limitations，并核对当前 repository README、
  project structure、文档入口和 85-commit history。当前 README 已包含论文之后的 plugin marketplace、
  reusable workflow、virtual agents 与 workbench，故只用来确认代码表面，不把后续功能倒灌进 W16。
- **Original Problem / Why Previous Designs Were Reasonable**：单 ReAct loop、全量 transcript、固定
  workflow 与 per-tool wrapper 在短任务、低权限、单用户环境中足够简单；但持久 personal agent 同时面对
  context 膨胀、跨 session state、动态任务分解、并发 tenant isolation 和有副作用工具。完全动态的
  orchestrator 能适应未知任务结构，却把依赖、失败来源与重放条件藏在 growing context；预先手写 DAG
  可观察，却无法覆盖运行前未知的 decomposition。
- **Changed Constraint / Mechanism**：SemaClaw 将 `sema-code-core` 的 execution/context/tool runtime 与
  channel、agent pool、memory、scheduler 和 UI application layer 分开。工作 Context 在 75% threshold
  触发 compaction，失败时退到 50% truncation，并重新注入 rules/todos；外部 memory 以 FTS5 BM25、
  sqlite-vec 和 token scan 三级降级。DAG Teams 让 LLM 一次性声明带 `dependsOn` 的 task graph，先做
  cycle check，再由 DispatchBridge 确定性轮询 timeout、依赖 terminal state 与 worker availability。
  PermissionBridge 则把高风险 tool approval 与 clarification 都建模为 suspend/resume request。
- **State Ownership / Control and Data Flow**：runtime 持有 session、compaction、tool event 与 engine
  isolation；AgentPool 持有 persona/workspace namespace；MemoryManager 持有 daily log、index 与 dirty
  state；orchestrator 只提出 DAG，DispatchBridge 持有 parent/task state、dependency、worker binding、
  timeout 与 terminal transition；PermissionBridge 用 request ID 将 response 路由回 suspended execution。
  这里最关键的边界是：模型拥有 plan proposal，不拥有 workflow truth；Markdown wiki 与 summary 是
  derived knowledge，不是 authoritative business state。
- **Implementation Details / Failure Semantics**：同一 admin agent 一次只运行一个 parent group，其余
  queued；worker 以 exact string 绑定到持久 persona。dependency 的 `done/error/timeout` 都被视为 terminal，
  下游仍会启动并收到 prerequisite statuses，这避免全图卡死，却把 fail-fast/skip/compensate 语义留给
  worker prompt。Dispatch state 由 stdio MCP subprocess 与主进程通过 JSON + lock file 协调；restart
  把遗留 active/queued parent 标为 done、in-flight task 标为 interrupted，不等于 exactly-once recovery。
  Internal MCP 被整体预授权；“internal”是否真无外部副作用依赖实现与 deployment capability，不能由名称保证。
- **Evaluation Contract / Evidence Boundary**：论文没有 controlled benchmark、matched baseline、fault
  injection、tenant stress、security test、latency/cost、seeds/CI 或 production SLO。文中引用的固定模型
  Terminal Bench uplift 来自外部 harness experiment，不是 SemaClaw evaluation。公开材料证明的是一组
  可检查的 architecture/implementation choices，不证明它们使系统“structurally safe by default”，也不
  证明 persistent persona routing、compaction、hybrid retrieval 或 DAG Teams 优于替代方案。
- **Trade-offs / New Failure Modes**：获得 plan/execution 分离、explicit dependency state、approval
  correlation、context/memory/persona 分层和 deterministic/script/agent scheduled modes；付出更多 bridge、
  index、JSON state、polling、namespace 与 recovery protocol。新增风险包括 LLM 一次性生成错误 DAG、
  failed prerequisite 被下游误当有效输入、lock/state-file corruption、approval TOCTOU、request ID/session
  mismatch、global bridge head-of-line pressure、summary corruption、stale index、pre-authorized internal tool
  越权，以及 persona/history 对任务分配形成 self-reinforcing bias。
- **Where Previous Designs Still Apply / Alternatives**：短、无副作用任务继续使用单 loop；结构固定且高风险
  的流程应手写 workflow；未知结构可采用动态 orchestrator；两阶段 DAG 适合需要 inspection/replay 的中间域。
  高风险 approval 还需要 action digest、policy snapshot、expiry 与 idempotency；memory/wiki 只适合用户可编辑
  knowledge，交易或审批状态仍留在 authoritative system。四种路线是并存分支，不是从旧到新的单向替代。
- **Evolution / ROADMAP / Decision**：`Direct Evolution`：single loop / static DAG → dynamic orchestrator →
  model-proposed DAG + deterministic executor；`Layering / Dependency`：runtime → context/memory → approval →
  workflow/team → application channels。已读 Ch73、Ch77、Ch78、Ch80；Ch77 已明确 deterministic spine、
  approval、timeout、replay、side-effect 与 failure semantics，Ch73/78/80 已覆盖 derived memory、multi-agent
  tax 与 platform governance。SemaClaw 的新价值主要是受限 implementation case，而非新的长期结论，故
  provisional `No Change — Already Covered`，主 owner Ch77；Books Gate 关闭。

### LongAct — 23/30

- **Candidate / Week / Source Family**：`LONGACT-ACTIVATION-GUIDED-RL-UPDATES`；W16；
  arXiv:2604.14922 唯一 v1 于 2026-04-16 15:30 UTC 首次公开。已读 13 页 PDF 全文、公式、Algorithm 1、
  main/ablation tables、perturbation analysis、discussion、limitations 与相关 appendix；未发现可核验的
  event-time author code/artifact，故实现结论限于论文描述。
- **Original Problem / Why Previous Designs Were Reasonable**：full-parameter RL 对所有参数应用 noisy
  policy gradient，容量充分且实现简单；LoRA 等固定低秩 adapter 通过更小 trainable state 降低成本，却在
  训练前固定 update subspace。长上下文 RL 的 rollout 昂贵、reward 稀疏，作者假设并非所有 attention
  feature dimensions 都同等参与 context processing，希望用当前 activation 选择更新位置。
- **Changed Constraint / Mechanism**：每个 training step 对 Q、K projection output 沿 sequence 维做
  L2 norm，再按 batch 平均，得到每个 head、每个 hidden feature 的 magnitude；每头选 top-`lambda`
  dimensions，把 local indices 映射到 `W_Q/W_K` 的 global rows，只保留这些行的 gradients。mask 每步由
  当前 activations 动态重算，训练结束后丢弃，不改变 inference graph。默认 `lambda=0.3`。
- **State Ownership / Control and Data Flow**：rollout/runtime 产生 sequence activations；selector 持有本步
  Q/K magnitude、top-k indices 与 transient mask；optimizer 只在 selected Q/K rows 上消费 gradient。
  重要边界是其余 `W_V`、`W_O`、MLP 等参数仍按论文 Algorithm 1 进行普通 dense update；因此
  `30% selected dimensions` 既不是整模型仅更新 30% 参数，也不推出 backward FLOPs、activation memory
  或 optimizer state 按 70% 等比例下降。论文也未定义 mask/optimizer-state checkpoint 的恢复语义。
- **Implementation / Evaluation Contract**：Qwen3-8B-base 先以 20K samples、max 16,384 tokens SFT
  900 steps，再把 DocQA-RL-1.6K 与 1K MemAgent prompts 混合做 DAPO；RL max context 32,768、batch 8、
  16 rollouts、temperature 1、max output 4,096、learning rate `1e-6`，硬件为 8×H800 80GB。评估使用
  LongBench v2、RULER、InfiniteBench，并在 vLLM 下固定 temperature 1、seed 0；论文还在 Qwen3-4B、
  GRPO、GSPO、SAPO、PPO 及 short-context GSM8K/HumanEval/TruthfulQA 上做迁移检查。
- **Evidence / What It Proves**：作者协议下，8B LongBench v2 overall 从 SFT 的 27.04、full DAPO 的
  32.80 到 LongAct 36.73；random/min-magnitude rows 较弱，20/30/40% 中 30% 最佳。把 top 30%
  activations clamp 到 global mean 后 503 个 LongBench cases 为 0 correct，clamp bottom 30% 为 108/503，
  支持 high-magnitude Q/K features 与当前任务行为有关。它证明的是该模型、数据、reward 与评测组合中的
  empirical utility，不证明 magnitude 是稳定因果 attribution，也不证明 sparse-row update 普遍优于
  full RL 或 LoRA。
- **What It Does Not Prove / Limitations**：只报告 4B/8B，作者 limitations 明确未扩到更大模型；未披露
  多 seed/置信区间、wall-clock、peak memory、optimizer-state bytes、communication、mask computation
  overhead 或 production SLO。clamp-to-mean 是强分布干预，0/503 可能包含 scale/normalization disruption，
  不能单独识别“long-context circuitry”。short-context gain 反而削弱“仅长上下文专属”解释；引用其他工作
  的 5%～30% functional subnetwork 不能替代本论文的 parameter-level measurement。
- **Trade-offs / New Failure Modes**：获得 input-adaptive update locality，不需 inference adapter 或 merge；
  付出每步 activation statistics/top-k、dynamic gradient masking 与更复杂 optimizer/checkpoint identity。
  新风险包括 magnitude 被 outlier 或 position distribution 支配、head-wise top-k 忽略跨 head interaction、
  mask churn 使 momentum/variance state 与 active rows 错位、低 magnitude 但关键 feature 永久学不到、
  model/data revision 后 saliency drift，以及只稀疏 Q/K 却被误报为整模型 efficiency。
- **Where Previous Designs Still Apply / Alternatives**：full update 适合容量优先且资源充足；LoRA/QLoRA
  适合需要小 artifact、可复用 base 与清晰 trainable-state contract；固定 module/row mask 更易复现；
  dynamic magnitude mask 适合愿意用额外 selection complexity 换实验性 update locality 的场景。它们改变的
  是 update parameterization/selection，不改变 RL reward、rollout 和 verification contract。
- **Evolution / ROADMAP / Decision**：`Direct Evolution`：full update → static restricted subspace →
  activation-conditioned row selection；`Layering / Dependency`：GRPO/DAPO objective → dynamic update mask →
  optimizer/checkpoint state。已读 Ch25～27、Ch29 及 Ch31；Ch26 已覆盖“trainable parameter 比例不等于
  FLOPs/activation/memory 比例”和 target-module/update-subspace 选择，但尚缺 dynamic sparse-row mask 的
  transient-state 与 optimizer/checkpoint 边界。主 owner 暂定 Ch26，Ch29/31 只需短 handoff；provisional
  `Refine — Existing Argument (Experimental)`。Historical Books Gate 关闭，暂不写正文。

### Gemini Robotics-ER 1.6 — 22/30

- **Candidate / Week / Source Family**：`GEMINI-ROBOTICS-ER-1.6`；W16；Google DeepMind release
  post 于 2026-04-14 发布。model card 于 2026-04-20 发布，属于 W17 related evidence，只用于核验
  architecture、inputs、limitations 与 safety boundary，不改写 W16 event date。
- **Access / Full-read Coverage**：已读完整 release post、全部 evaluation captions、instrument-reading、
  multi-view success detection、tool-use 与 safety 段落，并核对后续 model card 的 model information、
  training-data disclosure、hardware/software、evaluation、intended use、limitations 与 safety sections。
- **Original Problem / Previous Design**：传统 VLM 或 VLA 可以分别承担高层理解或低层动作；在任务短、
  环境固定且动作策略可枚举时，这种分层仍合理。约束变化来自多视角环境、开放世界知识、仪表读数、
  task planning 与 success detection 需要在同一高层 reasoning loop 中组合，并调用 Search、VLA 或用户函数。
- **Mechanism / State / Flow**：官方只披露它是基于 Gemini 3.0 Flash 的 VLM，接收 text/image/audio/
  video，输出 text，由 application 把高层判断交给 VLA 或其他 tools。camera observations、prompt 与 tool
  results 属 run input；模型输出是 proposal，不是 physical-world truth；actuation authority 仍由 robot
  controller、policy 与 safety interlock 持有。训练数据仅披露为 Gemini 3.0 data 加 embodied-reasoning
  datasets，TPU/JAX/Pathways 为实现事实；参数、训练 recipe、controller loop 与 failure recovery 未公开。
- **Evaluation / Evidence Boundary**：release post 报告 pointing、counting、success detection、instrument
  reading 与 safety 结果，但 single-view 与 multi-view success-detection examples 不同，不能横向比较；
  instrument reading 是否开启 agentic vision 也改变条件。作者结果支持“在其 benchmark contract 下能力
  提升”，不证明真实机器人端到端可靠性、闭环 latency、calibration、distribution shift 或 production safety。
- **Trade-offs / Evolution**：`Layering / Dependency`：perception/VLM → embodied-reasoning planner → VLA/
  tool executor → physical safety authority。获得可组合的高层 reasoning 与多视角解释，付出更长依赖链、
  tool/controller mismatch、stale observation、false success detection 与安全责任切分。固定 task policy、
  classical control 与专用 perception 在可验证、低延迟、安全关键任务中仍成立。
- **ROADMAP / Decision**：已读 Ch62、Ch68、Ch77 及 Ch80；现有正文已经区分 model capability、
  executable verifier、tool authority 与 deployment autonomy。`Weekly Only — Version/Product Fact /
  Mechanism Not Disclosed`；不凭 benchmark 反推内部机制，也不在 Books Gate 前写入正文。

### SGLang Q2 2026 Roadmap — 23/30

- **Candidate / Week / Source Family**：`SGLANG-Q2-2026-ROADMAP`；W16；official GitHub issue #22949
  于 2026-04-16 opened，当前仍标注 WIP。related RFC/roadmap links 只证明计划分解，不证明相应功能已落地。
- **Access / Full-read Coverage**：已读 issue 全文，包括 scheduler、KV、speculative decoding、P/D、API/
  Rust、parallelism、multimodal、hardware、kernels、reliability/observability、RL integration、Multi-LoRA、
  model coverage 与 CI sections，并核对 issue 的 open/WIP status。
- **Original Problem / Changed Constraint**：既有 serving engine 围绕较稳定的 decoder-only request path
  逐项加入优化是合理的；但 hybrid attention、hierarchical cache、agent session、multimodal/omni、RL rollout、
  多硬件与多种 parallelism 组合后，feature matrix 与 scheduler state 急剧膨胀，局部 patch 难以维持兼容性。
- **Mechanism / Ownership**：roadmap 提议让 scheduler 更 stateless、mixed chunked prefill 成为一等路径，
  统一 hybrid Radix cache，引入更通用 speculative abstraction、Rust gRPC/API path、可组合 CUDA-graph backend，
  并把 checksum、per-request tracing 与 rollout-engine API 纳入 contract。issue/RFC owner 拥有计划；merged
  code、release/tag 和 runtime telemetry 才拥有实现事实。路线图不能替代 landed behavior、benchmark 或 SLO。
- **Evidence / Limits**：这份来源证明项目维护者识别出的 architectural pressure 与工作方向；不证明目标
  已实现、不同 backend 行为一致、33K→10K LOC 等目标已达成，也不证明列出的性能数字能跨 model/hardware/
  batch 外推。每个子项都需要在其 PR、release、docs 与 tests 中重新核验。
- **Trade-offs / Evolution**：`Direct Evolution`：feature-specific scheduler/cache paths → shared abstractions；
  `Layering / Dependency`：roadmap → RFC → merged code → release → operational evidence。统一抽象降低组合爆炸，
  却新增 migration surface、semantic normalization、fallback 与 regression matrix；专用 fast path 在稳定 workload
  下仍可能优于通用层。
- **ROADMAP / Decision**：已读 Ch46～48、Ch51～52；这些章节已拥有 cache identity、engine/runtime 边界、
  P/D 与 scheduling contract。`Emerging — Roadmap, Not Implemented`，只保留为跨周追踪锚点；后续 landed
  PR 按真实 event week 重新审计。

### Megatron Core 0.17.0 — 22/30

- **Candidate / Week / Source Family**：`MEGATRON-CORE-0.17`；W16；official signed GitHub release
  `core_v0.17.0` 于 2026-04-16 19:59 发布，commit `9539a12`。后续 0.17.x backports 不倒灌本周。
- **Access / Full-read Coverage**：已读 release changelog 全部条目，并按 PR family 核对 MTP/mRoPE、hybrid
  model、SFTDataset、RL tests/logprobs、LatentMoE、EP+HSDP、1F1B overlap、distributed init、checkpoint、
  CUDA graph、M-FSDP、FP4/FP8 fusion、EAGLE+CP、tokenizer removal 与 inference-error handling。
- **Original Problem / Mechanism**：多维 parallel runtime 的难点不是单个算法缺失，而是 feature composition：
  MTP 与 mRoPE/hybrid model、SFT 与 TP、EP 与 HSDP、sequence packing 与 logprob、training CUDA graph 与
  RL reuse 必须共享 shape/process-group/checkpoint semantics。0.17.0 通过多项 support/fix/test 把这些组合从
  “存在 feature flag”推进到更明确的 integration surface；它不是一篇提出单一新算法的证据。
- **State / Flow / Implementation Boundary**：model config、parallel groups、packed-sequence metadata、optimizer/
  grad buffers、checkpoint shards 与 inference request counts 分属不同 owner；release 中 strict EP request-count
  matching、non-silent engine errors、DistributedInitConfig 与 checkpoint fixes 都说明组合正确性依赖显式状态。
  changelog 没有提供统一 architecture spec、hardware matrix、性能实验或 SLO，因此只能记录 version facts。
- **Evidence / Trade-offs**：signed tag 与 linked PRs 证明代码变更进入该 release；不证明所有组合都达到生产
  可靠性，也不能把 CI/golden test 当作跨 workload 性能证据。更广 feature composition 提高覆盖面，却扩大
  test matrix、checkpoint compatibility、process-group ordering 与 silent mismatch 风险。较小、固定的并行组合
  仍更易验证。
- **Evolution / ROADMAP / Decision**：`Layering / Dependency`：并行原语 → runtime composition → tests/
  checkpoint compatibility → release。已读 Ch31、Ch34、Ch36 及 Ch37；正文已明确 checkpoint 是并行组合的
  反向映射、pipeline schedule 与 global batch 必须一致、平台必须验证组合而非开关。`Weekly Only —
  Version/Release Family`；不以 changelog 堆砌 Books。

### Full-Stack Optimizations for Agentic Inference with NVIDIA Dynamo — 28/30

- **Candidate / Week / Source Family**：`DYNAMO-AGENTIC-INFERENCE`；W16；NVIDIA Technical Blog
  于 2026-04-17 发布。已联合核对文中 agent-hints docs、router/KV descriptions 及相关 implementation links；
  文中“will be sharing / building / actively exploring”内容保留为 future design，不写成 current behavior。
- **Access / Full-read Coverage**：已读全文的 workload observation、frontend multi-protocol representation、
  `nvext.agent_hints`、KV-aware routing、priority queue、custom router、multi-tier KVBM/HiCache、NIXL transfer、
  retention/token-range policy、prefetch、agent lifecycle 与 closing limitations。
- **Original Problem / Previous Design**：round-robin、request-level priority 与 local LRU 对独立短请求合理；
  agent workload 却呈长 prefix、tool pause、incremental append、多 subagent fan-out 与 context compaction，形成
  write-once-read-many KV。runtime 只看到 tokens，harness 却知道 session、blocked/resume、expected output、
  subagent lifetime，跨层信息缺失导致重复 prefill、错误 placement 与无差别 eviction。
- **Mechanism / State Ownership / Flow**：frontend 把 typed content 与 `priority`、estimated OSL、
  `speculative_prefill`、TTL/cache-control hints 规范化；router 用 global block index 的 overlap 与 decode load
  选 worker，并仅在过载阈值后进入按 effective-arrival 排序的 priority heap；engine 负责 backend-specific
  priority/preemption/eviction。KV block 由 runtime 生成，以 sequence hash 进入 immutable global identity，
  可写穿 GPU→CPU→NVMe→remote tier，经 NIXL 跨 worker/PD transfer。harness 提供 value/lifecycle hint，
  但不能成为 cache correctness authority；router index、block registry、TTL/priority 与 backend residency
  必须分别版本化并处理 stale events。
- **Evaluation Contract / Evidence Boundary**：85–97% hit、97.2% aggregate hit、11.7x read/write、
  170M index ops/s、4x p50 TTFT、1.5x p50 TPS 与 63% p50 reduction 来自不同 managed traces、index test 或
  NAT integration；来源未给出统一 model、hardware、input/output length、batch/concurrency、tail SLO 与
  failure condition，不能组合为通用性能结论。文章证明的是 design pressure、公开 interface 与部分实现，
  不证明 global retention/prefetch/lifecycle tagging 已全部 landed；明确未来时态的部分保持 Experimental。
- **Trade-offs / Failure Modes**：获得 workflow-visible scheduling、prefix reuse、跨 worker KV sharing 与更细
  eviction value；付出 hints trust/calibration、global-index freshness、metadata propagation、priority fairness、
  tenant isolation、storage/network bandwidth 与 failure recovery。新风险包括错误 OSL 导致 placement 偏差、
  priority starvation、TTL pinning 造成 cache capture、hash/identity mismatch、decode 新 KV 未及时发布、
  remote tier stale/read amplification，以及 harness/engine 对 lifecycle 语义不一致。
- **Previous Designs / Evolution**：local LRU 与 round-robin 在低 reuse、短请求、单 worker 或 metadata 不可信
  时仍合理；session affinity 简单但牺牲 balance/failover；recompute 在 transfer 比 prefill 更贵或 cache identity
  不可验证时仍成立。`Direct Evolution`：local request cache → KV-aware placement → distributed typed cache；
  `Layering / Dependency`：workflow semantics → hints → router → engine/KV manager；`Principle Reuse`：control-
  plane hints 不是 data-plane truth。
- **ROADMAP / Decision**：已读 Ch46～48、Ch50～52 与 Ch77；Ch48 已覆盖 Request/Control/State paths、
  KV-aware routing、selection-index、KVBM 与 failure correctness，Ch52 已覆盖 routing/placement/SLO，Ch77
  已覆盖 workflow visibility。真正可 refine 的长期缺口是把 hint provenance、calibration、fairness 与
  distributed retention invalidation 连成同一 contract。provisional `Refine — Existing Argument`，主 owner
  Ch48，Ch52/77 短 handoff；Historical Books Gate 关闭，暂不写正文。

### NemoClaw + OpenShell local-agent reference stack — 23/30

- **Candidate / Week / Source Family**：`NEMOCLAW-OPENSHELL-REFERENCE`；W16；NVIDIA tutorial 于
  2026-04-17 发布。已核对当日架构说明与 current official docs；后续 docs/release notes 只帮助识别演进，
  不倒灌为 04-17 已有行为。
- **Access / Full-read Coverage**：已读 tutorial 全文，包括 DGX Spark/Ollama prerequisites、component
  ownership、onboarding、sandbox connectivity、Telegram token flow、operator approval、remote tunnel、
  lifecycle commands、uninstall 与 security warning；并核对 official architecture/network-policy/security docs。
- **Original Problem / Mechanism**：long-running local agent 需要 model serving、channel gateway、memory/tool
  runtime 与 sandbox boundary。NemoClaw 是 host-side orchestration/installer；OpenClaw 在 sandbox 内拥有 agent
  workflow；OpenShell 以 network namespace、filesystem/process controls、credential/inference proxy 与 policy
  approval 持有安全边界。默认 network deny、host-side token registration 与 blocked-request approval 将
  “模型想访问”与“系统允许访问”分离。
- **Evidence / Limits**：官方教程证明参考 topology 与操作路径可被部署，不是 penetration test、prompt-
  injection immunity 或 multi-tenant isolation 证明。文章自己明确无 sandbox 可完全防御高级 prompt injection；
  “all inference local”只在选定 local provider 且 policy 未允许外部数据路径时成立。current docs 中更强的
  policy tiers、Landlock/seccomp/OPA 与 fail-closed changes 不能反推为 W16 initial stack 的全部行为。
- **Trade-offs / Evolution**：获得 data locality、deny-by-default egress、operator-visible approval 与 versioned
  blueprint；付出 local hardware/model latency、policy maintenance、channel/token attack surface、sandbox escape
  与 human approval fatigue。完全托管 API 在不需要 local data/control 时仍更简单；隔离主机与最小工具集在
  高风险探索中仍优于扩大 allowlist。`Layering / Dependency`：model runtime → sandboxed agent → policy gateway
  → human authority。
- **ROADMAP / Decision**：已读 Ch68、Ch77、Ch79、Ch80；现有章节已明确 MCP/tool protocol 不等于授权、
  policy sensor 不等于 authority、Agent Platform 需要 identity/run/policy/replay。`No Change — Already Covered`；
  本候选提供受限参考实例，没有新增足以进入正文的跨实现机制。

### Hugging Face PEFT 0.19.0 — 27/30

- **Candidate / Week / Source Family**：`HF-PEFT-0.19`；W16；official signed GitHub release v0.19.0
  于 2026-04-14 14:05 发布，commit `6d5a6f4`；v0.19.1 于 04-16 只是两项小修复，作为同 family patch，
  不覆盖主体 release。
- **Access / Full-read Coverage**：已读完整 release notes、九种新增 method summaries、conversion/
  initialization、Tensor Parallel、weight tying、low-precision、quantization、PrefixTuning、backend migration、
  backwards-incompatible fix 与 all-changes boundary，并核对 linked PR/code/docs surface。各 method 的作者论文
  未被本 release-family review 自动视为全文审计，因此不继承论文 benchmark 或普适机制结论。
- **Original Problem / Changed Constraint**：LoRA 用统一低秩 additive delta 获得小 artifact、低训练参数量与
  mergeability，仍是合理默认；但 expressivity、跨层共享、长上下文压缩、TP serving communication、RL 极低
  parameter budget、activation memory 与 forgetting 的约束不同，单一“rank 越小越省”无法描述真实选择空间。
- **Mechanism / State Ownership**：release 将 block-granular、block-diagonal、prefix-cartridge、probabilistic
  sharing、orthogonal subspace、data-routed cross-layer sharing、neural tweaker、extreme tiny update 与 adaptive
  subspace 等方法纳入同一 runtime。更重要的系统接口包括 lossy non-LoRA→LoRA conversion、LoRA-GA init、
  intruder-dimension post-processing、TP support、tied-weight preservation、FP8/LoftQ compatibility。base weight、
  adapter parameters、router/projection/init state、quantization config、TP layout 与 tied-weight identity 必须共同
  进入 artifact contract；trainable parameter count 不能代替 activation、communication、optimizer 与 runtime cost。
- **Evidence / What It Does Not Prove**：signed release 与 PRs 证明实现进入 0.19.0；release 中“promises”、
  “faster serving”“better performance”等仍是 method-paper/maintainer summary，不是统一 benchmark。没有同一
  model/data/hardware/rank/precision/TP/SLO 下的九方法比较，且 conversion 明确 lossy，不能写成任意 adapter
  可无损归一为 LoRA。0.19.1 的存在也说明 release identity 必须包含 patch level。
- **Trade-offs / Failure Modes**：获得更贴合 constraint 的 update parameterization 与更广 integration；付出
  method-selection complexity、adapter schema/version proliferation、conversion error、target-module/weight-tying
  mismatch、TP shard compatibility、quantized-base drift 与 serving backend coverage。LoRA 仍在 portability、
  ecosystem、mixed deployment 与简单审计上占优；full fine-tuning 仍适合容量优先且有完整资源的场景。
- **Evolution / ROADMAP / Decision**：`Direct Evolution`：one low-rank delta → structured/shared/routed
  update spaces；`Layering / Dependency`：method math → adapter artifact → quantization/TP layout → serving runtime；
  `Alternatives`：activation compression、prefix compression 与 parameter adaptation 不是同一资源轴。已读 Ch26、
  Ch31、Ch33 与 Ch46；Ch26 已拥有“trainable ratio 不等于系统成本”与 target/update-subspace contract，Ch31
  已覆盖 adapter/base/quantization artifact identity。provisional `Refine — Existing Argument`，主 owner Ch26，
  Ch31/46 短 handoff；Historical Books Gate 关闭，暂不写正文。

## Pending Full Source Review Queue

`42/42` scored candidates 已完成非模板化 Full Source Review；3 个 named below-threshold items 的日期、
来源与拒绝理由已核验；candidate、academic、official 与 infra queues 均清零。W16 Evidence Gate 通过，
但全历史 Historical Books Gate 仍关闭。

## Repository Changes

- W16 从 3 个 baseline 扩展为 42 个 scored families；39 个 recovered families 已完成非模板化
  Source Review，另记录 3 个 named below-threshold items；candidate-review queue 清零但 academic/
  source coverage 已闭合。新增 official/infra 复核把 Gemini Robotics、SGLang roadmap、
  Megatron Core 0.17.0、Dynamo agentic inference 与 NemoClaw 分别归为 capability fact、roadmap、release
  family、长期 serving mechanism 与 reference deployment，避免把五类证据混写成已落地架构；PEFT
  0.19.0 与 0.19.1 也拆成主体 release 和 patch，前者的 method/runtime surface 不再被后者静默遗漏；Sema Code
  26→23，Agentic Aggregation 26→25，ClawGUI 26→24，
  On-Policy Distillation 27→25；Nemotron 3 Super 按 03-04 base-checkpoint 首发回拨 W10；W17 feed 暴露的 6 个
  04-13～04-19 候选已
  回拨本周；AiScientist event date 由 arXiv v1 的 04-14 修正为 repository initial release 的 04-13，
  Practical Value/Longevity 轴重平衡但总分仍为 26；AgentSPEX 因机制新颖度、受控对照、可靠性与
  production evidence 边界从 26→23，并归为 Ch77 `No Change`；Exploration/Exploitation Errors 暂定
  Ch62 Experimental refine，明确 policy-agnostic 不等于 environment-agnostic；Dive into Claude Code
  明确为独立 reverse-engineering snapshot，Ch68/73/74/77～80 已覆盖长期机制，归为 Ch80 `No Change`；
  Memory Transfer Learning 暂定 Ch73 Experimental refine，但因 code `Coming Soon`、缺 seeds/
  uncertainty、cost/SLO 与 contamination audit 从 25→24；DR3-Eval 已完成 static/live、retrieval/report、
  judge/human 与 artifact 边界审计，暂定 Ch62 Experimental refine；因公开 dataset 未显式包含论文所需
  sandbox corpus，且 human-validation protocol 在正文/附录冲突，25→24；Corpus2Skill 已完成 v1 全文/
  appendices、v2/v3 scope revision、WIP code 与 Ch71～73/80 邻接审计，暂定 Ch72 Experimental refine；
  它只在可恢复 topical taxonomy 的 corpus 上形成 navigation 分支，不能替代开放域/表格/低成本 retrieval，
  且缺 incremental rebuild、uncertainty 与 production SLO，26→24；OpenMobile 已完成 v1、appendices、
  current code/data/model artifact 与 Ch23/25/62/77/80 邻接审计，暂定 Ch25 Experimental refine；它将
  successful expert demonstrations 推进为 learner-reachable recovery-state coverage，但同源 teacher/
  monitor/filter、incomplete artifact identity、环境重合、缺硬件/cost/SLO 与 contamination contract 使
  25→24；Scaling Test-Time Compute 已完成 sole-v1、Appendix A～H、两项 harness、five-model experiment、
  RTV/PDR ablation 与 Ch62/75/77/78/80 邻接审计，暂定 Ch78 Experimental refine；它支持 bounded
  trajectory representation 作为 selection/reuse interface，却没有 total-compute-matched baseline、公开
  artifact、cost/latency/SLO 或独立 judge，并出现 pass@16 下降与 0/16 failure amplification，27→25；
  SkillFlow 已完成 sole-v1、全部 appendices、project/repository/task/evolved-skill artifact 与 Ch62/73/77/80
  邻接审计，归为 `No Change`；其 family-local fixed-order protocol 支持“Skill 使用不等于效用、修复比生成
  更难”的条件性证据，却不测跨 family retrieval/forgetting，且 history-context control 在正文与 Table 6
  分别写为 47.41% 和 51.04%，因此 Practical Value 5→4、25→24；
  EvoMaster 已分别审计 v1/v4、全部 benchmark-specific setup/appendices、repository/tags/current evolution
  guide 与 Ch62/73/77/78/80；v1 四项 OpenClaw 对照混合 specialized workflow，v4 十项扩展仍无 component
  ablation、matched compute、seeds/CI 或 event-bound run artifact，且 05-18 run-level evolution 不倒灌 W16，
  因而 25→23 并归为 Ch77/78/80 `No Change`；
  无 Daily 或 Books 修改。
- 2026-08-13 周级复算确认 42 scored（14 high / 28 mid / 0 low）、42/42 `20+` Full Source Reviews、
  3/3 named below-threshold rejection checks、0 candidate/coverage/attribution pending；W16 Evidence Gate
  继续 Passed，backlog cursor 进入 W17。未修改 Books。

## Open Questions

1. AI-generated oversight research 怎样防止 shared-model blind spot 与 evaluator collusion？
2. `Automated alignment researchers` 的 linked study、revision 与 public artifact 是否存在同周或
   后续独立复核，能把当前 `No Change` 升级为新的 oversight mechanism？
3. 2026-04-13～04-19 的模型、论文与 Infra 固定来源还遗漏了哪些 candidate families？
4. CodeTracer 的 derived state tree 如何在 parallel tool calls 中表达 partial order，而不伪造唯一因果链？
5. 诊断 pass 计入 total compute 后，reflective replay 是否仍优于等预算重新采样或 human triage？
6. CluE 的 cluster-local prompt evolution 在独立 extractor/generator/judge、真实多用户 history、
   per-domain router baseline 与完整 deletion lifecycle 下是否仍能减少 negative transfer？
7. Sema Code 的 event-bound implementation 是否真实隔离每个 engine instance，且在 tenant stress、
   network backpressure、process crash 与 horizontal scale 下保持 queue/approval/background-task 语义？
8. OccuBench 的 LES 在 domain-expert calibration、deterministic invariant checker 与真实/hand-built
   environment 对照下，能否保持 task validity、state fidelity 与 model ordering？
9. AggAgent 在 provenance-aware index、恶意/重复 trajectory、K≫8 与 total-cost-matched sequential
   baseline 下，是否仍能稳定找到 minority evidence，并证明 derived synthesis 而非 judge preference？
10. ClawGUI 的 environment generation、lease、reset 与 spare-server failover 能否在大规模真实设备、
    crash/retry 与副作用校验下保持同一任务世界；PRM 和最终截图 judge 又如何证明没有遗漏后台状态、
    错误目标与中间违规？
11. OPD 的 support-overlap diagnostics 能否在 code/tool/Agent、多 tokenizer 与长 horizon 下复现；当
    global reward 有信息而局部 gradient 不可利用时，如何直接测量并修正方向性 cancellation？
12. AiScientist 的 File-as-Bus 收益能否在加入 versioned writes、concurrent conflict handling、
    provenance、crash recovery 与非 model-judge verifier 后，通过 repeated、total-cost-matched runs？
13. AgentSPEX 在 matched workflow/tool/context budget、repeated seeds 下，单独强制 interpreter 是否仍
    带来收益；step 内副作用后的 checkpoint、parallel variable merge 与 schema migration 语义是什么？
14. Exploration/Exploitation metric 如何在不知道完整 environment state/optimal path 的真实 coding/web/
    tool trace 中定义 opportunity set，并区分必要 verification、recovery 与真正 stale action？
15. Claude Code v2.1.88 的 feature gates、permission paths 与 compaction branches 在 event-time runtime 中
    实际启用多少；如何以 immutable artifact 和受控 trace 区分 static-code reachability 与 production prevalence？
16. 跨域 procedural memory 如何同时建模 specificity benefit 与 mismatch risk，并在 source/target model、
    language、tool、environment、evaluator 版本变化时以 verifier-gated adoption 避免 negative transfer？
17. DR3-Eval 的完整 static sandbox corpus、support/noise labels 与 event-time digest 能否公开；正文 50 份/
    4 名专家和 Appendix D 的 30 份/2 名专家究竟哪个 human-validation protocol 正确？
18. Corpus2Skill 能否在 ACL/deletion、增量更新、adversarial documents 与 matched total cost 下维护
    map/source identity；什么 query/corpus classifier 足以在 flat retrieval 与 navigation 间可靠路由？
19. OpenMobile 的 global environment memory 在 app/version drift、pHash collision、annotation hallucination
    与不完整 random-walk graph 下如何验证；不同 teacher/monitor、safe reset 与 matched-cost baseline 是否
    仍能证明 recovery-state coverage，而不是 teacher substitution 或 benchmark-environment leakage？
20. RTV/PDR 的 structured summary 在 immutable schema、lineage 与 evidence pointer 下能否保持决定性 diff、
    failed verification 与 temporal order；equal-total-cost、independent/executable judge、adaptive stopping 和
    bad-context quarantine 是否能避免 pass@16/coverage 下降与整批 failure amplification？
21. SkillFlow 在 randomized/interleaved family、global library、独立 feedback、adversarial Skill 与 durable
    patch lineage/rollback 下是否仍保留正迁移；history-context control 的 47.41%/51.04% 冲突应以哪份
    event-bound result artifact 为准？
22. EvoMaster 的 event-bound config/code/run artifacts、matched-compute component ablation 与 repeated
    uncertainty 能否把 base harness、domain workflow、multi-agent search、retrieval 和 judge 的贡献分开；
    current run-local overlay 又如何在 crash、poisoning、secret leakage 与 regression 时 promotion/rollback？
23. Dynamo 的 agent hints 如何证明来源可信、校准 OSL，并在跨 tenant priority、TTL pinning、index lag、
    distributed retention 与 failover 下维持 fairness、freshness 和 cache identity？
24. SGLang Q2 roadmap 中哪些子项在后续 PR/release 真正落地，哪些改变了原计划；应如何按 landing week
    建立 roadmap→RFC→code→release→operations 的演进链？
25. Gemini Robotics-ER 的 high-level planner、VLA/controller 与 physical safety authority 如何建立可回放的
    observation/action identity；公开 benchmark 在真实 closed-loop latency 与 distribution shift 下是否保持？
26. PEFT 的多种 update subspace 在相同 model/data/rank/trainable budget、activation memory、TP layout、
    quantization 与 serving SLO 下如何比较；lossy conversion 应怎样进入 adapter artifact 的 provenance？

## Sources

- Anthropic, “Automated Alignment Researchers,” published 2026-04-14:
  https://www.anthropic.com/research/automated-alignment-researchers
- OpenAI, “Introducing GPT-Rosalind,” published 2026-04-16:
  https://openai.com/index/introducing-gpt-rosalind/
- Google Research April 2026 archive: https://research.google/blog/2026/04/
- Google DeepMind, “Gemini Robotics-ER 1.6,” published 2026-04-14:
  https://deepmind.google/blog/gemini-robotics-er-1-6/
- Gemini Robotics-ER 1.6 model card, published 2026-04-20 (related later evidence):
  https://deepmind.google/models/model-cards/gemini-robotics-er-1-6/
- SGLang Q2 2026 Roadmap, opened 2026-04-16:
  https://github.com/sgl-project/sglang/issues/22949
- Megatron Core 0.17.0 release, published 2026-04-16:
  https://github.com/NVIDIA/Megatron-LM/releases/tag/core_v0.17.0
- NVIDIA, “Full-Stack Optimizations for Agentic Inference with NVIDIA Dynamo,” published 2026-04-17:
  https://developer.nvidia.com/blog/full-stack-optimizations-for-agentic-inference-with-nvidia-dynamo/
- NVIDIA, “Build a More Secure, Always-On Local AI Agent with OpenClaw and NVIDIA NemoClaw,”
  published 2026-04-17:
  https://developer.nvidia.com/blog/build-a-secure-always-on-local-ai-agent-with-nvidia-nemoclaw-and-openclaw/
- vLLM 0.19.1 release, published 2026-04-18:
  https://github.com/vllm-project/vllm/releases/tag/v0.19.1
- Hugging Face PEFT 0.19.0 release, published 2026-04-14:
  https://github.com/huggingface/peft/releases/tag/v0.19.0
- Hugging Face PEFT 0.19.1 patch release, published 2026-04-16:
  https://github.com/huggingface/peft/releases/tag/v0.19.1
- NVIDIA DeepStream coding-agent tutorial, published 2026-04-16:
  https://developer.nvidia.com/blog/how-to-build-vision-ai-pipelines-using-deepstream-coding-agents/
- CodeTracer: https://arxiv.org/abs/2604.11641
- CodeTracer repository: https://github.com/NJU-LINK/CodeTracer
- Sema Code: https://arxiv.org/abs/2604.11045
- Sema Code paper HTML: https://arxiv.org/html/2604.11045v1
- Sema Code Core repository: https://github.com/midea-ai/sema-code-core
- Sema Code VSCode extension: https://github.com/midea-ai/sema-code-vscode-extension
- OccuBench: https://arxiv.org/abs/2604.10866
- OccuBench paper HTML v2: https://arxiv.org/html/2604.10866v2
- OccuBench repository: https://github.com/GregxmHu/OccuBench
- OccuBench dataset: https://huggingface.co/datasets/gregH/OccuBench
- Agentic Aggregation: https://arxiv.org/abs/2604.11753
- Agentic Aggregation PDF: https://arxiv.org/pdf/2604.11753
- AggAgent repository: https://github.com/princeton-pli/AggAgent
- AggAgent public rollout collection: https://huggingface.co/collections/yoonsanglee/aggagent
- ClawGUI: https://arxiv.org/abs/2604.11784
- ClawGUI paper HTML v1: https://arxiv.org/html/2604.11784v1
- ClawGUI repository: https://github.com/zju-real/ClawGUI
- ClawGUI-RL module: https://github.com/zju-real/ClawGUI/tree/master/clawgui-rl
- Rethinking On-Policy Distillation: https://arxiv.org/abs/2604.13016
- Rethinking On-Policy Distillation paper HTML v1: https://arxiv.org/html/2604.13016v1
- OPD repository: https://github.com/thunlp/OPD
- Nemotron 3 Super: https://arxiv.org/abs/2604.12374
- Toward Autonomous Long-Horizon Engineering: https://arxiv.org/abs/2604.13018
- Toward Autonomous Long-Horizon Engineering paper HTML v1: https://arxiv.org/html/2604.13018v1
- AiScientist repository: https://github.com/AweAI-Team/AiScientist
- Memory Transfer Learning: https://arxiv.org/abs/2604.14004
- Memory Transfer Learning paper HTML v1: https://arxiv.org/html/2604.14004v1
- Memory Transfer Learning project page: https://memorytransfer.github.io/
- Memory Transfer Learning repository (`Code: Coming Soon`):
  https://github.com/KangsanKim07/MemoryTransferLearning
- Exploration and Exploitation Errors: https://arxiv.org/abs/2604.13151
- Exploration and Exploitation Errors paper HTML v1: https://arxiv.org/html/2604.13151v1
- measurable-explore-exploit repository: https://github.com/jjj-madison/measurable-explore-exploit
- DR3-Eval: https://arxiv.org/abs/2604.14683
- DR3-Eval paper HTML v1: https://arxiv.org/html/2604.14683v1
- DR3-Eval repository: https://github.com/NJU-LINK/DR3-Eval
- DR3-Eval dataset: https://huggingface.co/datasets/NJU-LINK/DR3-Eval
- Dive into Claude Code: https://arxiv.org/abs/2604.14228
- Dive into Claude Code paper HTML v1: https://arxiv.org/html/2604.14228v1
- Dive into Claude Code paper HTML v2 revision: https://arxiv.org/html/2604.14228v2
- Dive into Claude Code companion repository: https://github.com/VILA-Lab/Dive-into-Claude-Code
- Claude Code official architecture overview: https://code.claude.com/docs/en/how-claude-code-works
- Claude Code official permissions: https://code.claude.com/docs/en/permissions
- Claude Code official subagents: https://code.claude.com/docs/en/sub-agents
- Don't Retrieve, Navigate: https://arxiv.org/abs/2604.14572
- Don't Retrieve, Navigate paper HTML v1: https://arxiv.org/html/2604.14572v1
- Don't Retrieve, Navigate paper HTML v3 revision: https://arxiv.org/html/2604.14572v3
- Corpus2Skill repository: https://github.com/dukesun99/Corpus2Skill
- BEHEMOTH / Self-Evolving LLM Memory Extraction: https://arxiv.org/abs/2604.11610
- BEHEMOTH paper HTML: https://arxiv.org/html/2604.11610v1
- BEHEMOTH / CluE repository: https://github.com/ayyyq/heterogeneous-memory-extraction
- AgentSPEX: https://arxiv.org/abs/2604.13346
- AgentSPEX paper PDF: https://arxiv.org/pdf/2604.13346
- AgentSPEX repository: https://github.com/ScaleML/AgentSPEX
- OpenMobile: https://arxiv.org/abs/2604.15093
- OpenMobile paper HTML v1: https://arxiv.org/html/2604.15093v1
- OpenMobile project page: https://njucckevin.github.io/openmobile/
- OpenMobile repository: https://github.com/njucckevin/OpenMobile-Code
- OpenMobile dataset: https://huggingface.co/datasets/cckevinn/OpenMobile-Data
- OpenMobile model artifact: https://huggingface.co/cckevinn/OpenMobile-8B
- Scaling Test-Time Compute for Agentic Coding: https://arxiv.org/abs/2604.16529
- Scaling Test-Time Compute full-paper mirror used for Appendix A～H review:
  https://www.researchgate.net/publication/404020802_Scaling_Test-Time_Compute_for_Agentic_Coding
- SkillFlow: https://arxiv.org/abs/2604.17308
- SkillFlow project page: https://zhangzi-a.github.io/SkillFlow-project-page/
- SkillFlow repository: https://github.com/ZhangZi-a/SkillFlow
- SkillFlow task dataset: https://huggingface.co/datasets/zhang-ziao/SkillFlow-Task
- EvoMaster: https://arxiv.org/abs/2604.17406
- EvoMaster paper HTML v1: https://arxiv.org/html/2604.17406v1
- EvoMaster paper HTML v4 revision: https://arxiv.org/html/2604.17406v4
- EvoMaster repository: https://github.com/sjtu-sai-agents/EvoMaster
- EvoMaster tags: https://github.com/sjtu-sai-agents/EvoMaster/tags
- EvoMaster current run-level self-evolution guide (post-W16 feature):
  https://github.com/sjtu-sai-agents/EvoMaster/blob/main/docs/evolution.md

## 2026-08-13 Source-Family Books Integration

DDTree 已通过独立 Source-Family Books Gate：Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，Current Ch24，Legacy N/A。其 factorized draft surrogate、budgeted tree proposal、target-owned verification 和 provisional KV/commit boundary 已作为受限机制写入 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`；best-B oracle 与 8×H200 作者实验不外推为线上 controller 或通用 speedup。Archive Completion Gate 仍 Open。

## 2026-08-14 Final Books Integration Ledger — 42/42

| Candidate / Source Family | Score | Stable Owner | Current / Legacy | Final Disposition | Chapter-level Review Evidence |
| --- | ---: | --- | --- | --- | --- |
| Automated alignment researchers | 23 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | No Change — Already Covered | scalable oversight 仍受 judge、task generator、human-gold 与 capability gap 约束；既有 Evidence Level 与 scorer governance 已覆盖 |
| Synthetic datasets from first principles | 23 | `TRAIN-DATA` | Ch27 / Ch23 | No Change — Already Covered | controllability、generator/verifier lineage 与 sim-to-real gap 已由 synthetic-data contract 覆盖 |
| GPT-Rosalind | 21 | `AGENT-WORKFLOW` | Ch81 / Ch77 | Weekly Only — Version/Product Fact | 公开 benchmark 与产品能力不足以披露内部 workflow/runtime mechanism |
| CodeTracer | 28 | `AGENT-PLATFORM` | Ch84 / Ch80 | Refine — Existing Argument / Experimental | flat trace→derived partial-order state tree→failure-onset hypothesis→原始 evidence replay |
| BEHEMOTH / CluE | 25 | `AGENT-MEMORY` | Ch77 / Ch73 | Refine — Existing Argument / Experimental | 异构 feedback→scenario cluster→局部成败分析→versioned extraction operator；derived prompt 不成为事实 authority |
| Sema Code | 23 | `AGENT-PLATFORM` | Ch84 / Ch80 | No Change — Already Covered | Agent definition、run identity、tool policy、trace/replay 与 release boundary 已覆盖其平台机制 |
| OccuBench / LES | 24 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — Existing Argument / Experimental | language simulator 被提升为 measurement subject，并加入 cross-simulator disagreement 与 real-environment anchor |
| Agentic Aggregation / AggAgent | 25 | `AGENT-MULTI-AGENT` | Ch82 / Ch78 | Refine — Existing Argument / Experimental | immutable trajectory archive→bounded evidence navigation→selection/synthesis→segment provenance |
| ClawGUI | 24 | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — Existing Argument / Experimental | provenance-bound environment hints 只能在 hard outcome gate 下提供 bounded shaping |
| Rethinking On-Policy Distillation | 25 | `TRAIN-SFT` | Ch29 / Ch25 | Refine — Existing Argument / Experimental | student-owned state coverage 与 entropy/disagreement token allocation 分层；不把 uncertainty 当 correctness |
| AiScientist | 26 | `AGENT-WORKFLOW` | Ch81 / Ch77 | Refine — Existing Argument / Experimental | thin control over versioned thick state，保留 executable spec、artifact branch、evaluation 与 rollback |
| AgentSPEX | 23 | `AGENT-WORKFLOW` | Ch81 / Ch77 | No Change — Already Covered | deterministic spine、agentic nodes、durable state、evaluation 与 deployment authority 已覆盖 |
| Memory Transfer Learning | 24 | `AGENT-MEMORY` | Ch77 / Ch73 | Refine — Existing Argument / Experimental | source contract→type/applicability check→target mapping/store→held-out target gate，显式保留 negative transfer |
| Exploration and Exploitation Errors | 25 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — Existing Argument / Experimental | failure diagnosis 拆为缺少必要 opportunity 与已有证据下错误决策，并绑定可观察 opportunity set |
| DR3-Eval | 24 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — Existing Argument / Experimental | retrieval corpus、report artifact、sandbox/tool、static/live evidence 与 human-validation protocol 分离版本化 |
| Dive into Claude Code | 22 | `AGENT-PLATFORM` | Ch84 / Ch80 | No Change — Already Covered | reverse-engineered observation 不升级为官方事实；subagent、permission、trace 和 runtime contracts 已覆盖 |
| Corpus2Skill | 24 | `AGENT-RAG` | Ch76 / Ch72 | Refine — Existing Argument / Experimental | authoritative corpus→versioned compiler→navigable skill graph→source dereference；Skill 不是事实 authority |
| OpenMobile | 24 | `TRAIN-SFT` | Ch29 / Ch25 | Refine — Existing Argument / Experimental | privileged environment trace→observable-state projection→executable replay/filter→SFT artifact |
| Scaling Test-Time Compute for Agentic Coding | 25 | `AGENT-MULTI-AGENT` | Ch82 / Ch78 | Refine — Existing Argument / Experimental | single-agent headroom、parallel diversity、sequential repair 与 aggregation/verification cost 联合预算 |
| SkillFlow | 24 | `AGENT-PLATFORM` | Ch84 / Ch80 | No Change — Already Covered | trajectory→derived Skill→validation→release、schema/provenance/rollback 已有完整 owner |
| EvoMaster | 23 | `AGENT-WORKFLOW` | Ch81 / Ch77 | No Change — Already Covered | evaluator-driven search、branch isolation、artifact lineage、held-out gate 与 rollback 已覆盖 |
| MEDS | 25 | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — Existing Argument / Experimental | prior-error evidence 成为有 expiry/reset/provenance 的辅助 credit，不能越过 terminal outcome |
| CocoaBench | 24 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | No Change — Already Covered | task/environment/scorer identity、slice、uncertainty 与 executable evidence 已覆盖其 benchmark contract |
| KnowRL | 24 | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — Existing Argument / Experimental | environment knowledge 作为可撤销 exploration prior，并要求 no-hint counterfactual slice |
| LMM-Searcher | 24 | `AGENT-RAG` | Ch76 / Ch72 | No Change — Already Covered | multi-step query/compress/verify/stop joint policy、provenance 与 premature-stop evaluation 已覆盖 |
| Lightning OPD | 23 | `TRAIN-SFT` | Ch29 / Ch25 | Disputed — No Books Change | 理论证明边界存在冲突；只保留 empirical observation，不写成稳定机制结论 |
| YOJO | 22 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — Existing Argument / Experimental | list-conditioned score identity、candidate permutation 与 group composition 进入 EvalSpec |
| DDTree | 25 | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | Refine — Existing Argument / Experimental | 复核并保留 factorized draft surrogate、budgeted tree、target verification 与 provisional KV commit boundary |
| RationalRewards | 22 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | No Change — Already Covered | pointwise/pairwise/listwise scorer、rationale evidence 与 judge calibration 边界已有论证 |
| UI-Copilot | 24 | `TRAIN-SFT` | Ch29 / Ch25 | No Change — Already Covered | tool/action demonstration、privileged-state projection、replay/filter 与 deployment-state matching 已覆盖 |
| SemaClaw | 23 | `AGENT-PLATFORM` | Ch84 / Ch80 | No Change — Already Covered | tool protocol、policy authority、sandbox、run identity 与 trajectory release 已覆盖 |
| TIP | 25 | `TRAIN-SFT` | Ch29 / Ch25 | Refine — Existing Argument / Experimental | entropy 与 teacher-student disagreement 作为 token-selection diagnostic，不作为 correctness truth |
| Self-Distillation Zero | 25 | `TRAIN-SFT` | Ch29 / Ch25 | Refine — Existing Argument / Experimental | future/reviser privileged state 只生成受验证 target，并与 student deployment state 隔离 |
| KV Packet | 26 | `INFER-KV-CACHE` | Ch45 / Ch41 | Refine — Existing Argument / Experimental | document→immutable derived KV packet→position repair/composition→target verification，绑定完整 cache identity |
| LongAct | 23 | `TRAIN-LORA` | Ch30 / Ch26 | Refine — Existing Argument / Experimental | static update subspace→activation-conditioned transient row mask，并补 optimizer/checkpoint/mask-churn 边界 |
| C2 Rubric-Augmented RM | 22 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | No Change — Already Covered | rubric formation、criterion execution、partial order、abstain 与 calibration 已覆盖 |
| Gemini Robotics-ER 1.6 | 22 | `MULTIMODAL-EMBODIED-VLA` | Ch26 / N/A | Weekly Only — Mechanism Not Disclosed | release/model card 支持 capability fact，不披露足以写入 planner/controller 内部机制的证据 |
| SGLang Q2 2026 Roadmap | 23 | `INFER-SGLANG` | Ch51 / Ch47 | Emerging — Weekly Only | roadmap 不是 landed behavior；等待 RFC/PR/release/operations 形成版本链 |
| Megatron Core 0.17.0 | 22 | `TRAIN-DISTRIBUTED-TRAINING` | Ch36 / Ch32 | Weekly Only — Release Family | 多项 release capability 没有形成单一、可归因且长期稳定的新机制结论 |
| Dynamo agentic inference | 28 | `INFER-DYNAMO` | Ch52 / Ch48 | Refine — Existing Argument / Version-Grounded | workflow signal→typed hint→router/KV action→calibration；hint 不成为 correctness authority |
| NemoClaw + OpenShell | 23 | `PLATFORM-SECURITY` | Ch72 / Ch68 | No Change — Already Covered | sandbox、deny-by-default egress、approval、credential proxy 与 residual-risk boundary 已覆盖 |
| Hugging Face PEFT 0.19.0 | 27 | `TRAIN-LORA` | Ch30 / Ch26 | Refine — Existing Argument / Version-Grounded | structured/shared/routed update spaces 扩展 artifact schema；release 支持实现事实，不继承方法论文 benchmark |

### W16 Gate Result

- Scored candidates: `42/42` final disposition；另有 `3/3` named below-threshold rejections 保持 Weekly Only。
- Final mix: `23 Refine + 14 No Change + 3 Weekly Only + 1 Emerging + 1 Disputed = 42`。
- Owner chapters changed: 11 Stable Nodes；DDTree Ch24 为此前已完成并在本轮复核的第 12 个 owner。
- Source-Family Books Gate: `Complete`；Archive Completion Gate: `Open`。
- Lightning OPD、产品/roadmap/release facts 与 No Change families 没有被强行写入机制正文。

Repository changes: Ch29～30、Ch33、Ch45、Ch52、Ch66、Ch76～77、Ch81～82、Ch84；Ch24 integration 经复核保留。
