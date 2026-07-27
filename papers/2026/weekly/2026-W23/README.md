# AI Research Weekly — 2026-W23

> Coverage Window: 2026-06-01～2026-06-07
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-09
> Re-audit Status: 2026-08-14 Source-Family Books Gate Complete under blocked-skip; 33/33 final dispositions; 22/33 current-version Full Source Reviews complete; 11 Unverified / Blocked / No Books Change; StreamMA v1/runnable artifact remains revision-sensitive; Archive/Discovery Gate Open; Books cursor advances to W24

## Executive Summary

旧版 W23 的三行评分实际压缩了五个 Source Families，也漏掉了 21 个 v1 日期落在本周的
academic families。本轮按 arXiv first-public date 恢复 PEFT population、KV-cache quantization、
state-externalizing search harness、trajectory error localization、adaptive planning、reward hacking、
continual experience internalization、runtime Agent evaluation、long-horizon benchmark、repository
exploration、harness self-improvement、skill internalization 与 tool-failure recovery 等候选。Hugging Face 的
“May 31～Jun 6”展示窗不是 ISO 周；其中 15 项 v1 属于 W22、1 项属于 W21，已回拨原周，不能把
curation date 当 event date。后续 W24/W25 展示窗又发现 10 项 v1 日期属于 W23，也按 first-public 回填。

OpenAI Dreaming memory 仍是重要官方材料；On the Scaling of PEFT 则提供了本周最完整的跨层
Source Family。其 43 页正文将 PEFT 从“省训练参数”扩展为可持久、可寻址的 local adaptive state，
并明确 Scale Up / Down / Out、MoE rollout-training consistency、rank/initialization、capacity、
policy revision 与 serving residency 的边界。本轮已完成 PDF、实验、限制及 Ch25～27、Ch54～56、
Ch73 邻接审计；这不是对 paper headline 的复述，也不在 Historical Books Gate 关闭时写 Books。

固定官方/Infra 重扫又恢复四个事件节点：SGLang 的 decoupled parallel speculative-decoding roadmap、
vLLM v0.22.1、Transformers LightGlue nested-config RCE disclosure，以及 Hugging Face Datasets 5.0.0。
四者分别属于 protocol design、patch release、security corrective evidence 与 breaking data-pipeline version
fact，不能用同一种“功能发布”口径处理。SGLang roadmap 形成 Ch44 的 provisional mechanism gap；其余三项
分别由 Ch46/53、Ch68 与 Ch23/62 的既有原则覆盖，不触发 Historical Books 写入。

## Coverage and Source Coverage

- 模型与研究机构：保留 OpenAI 6 月 3/4 日、Anthropic 6 月 3/5 日、Google 6 月 5 日。
- 论文与学术来源：重放 Hugging Face W23（展示窗 05-31～06-06），逐项用 arXiv v1/公开历史归周；
  恢复 23 个 W23 academic families，15 项回拨 W22、1 项回拨 W21；W24/W25 展示窗的 10 个 W23
  spillbacks 已归周。PEFT scaling 已读 43 页 PDF；Code2LoRA 已读完整 HTML（含实现、实验、限制与附录）；
  Harness-1 已读 63 页 PDF 的方法、训练、评估、消融、限制和相关附录；DRIFT/TELBench、KVarN、
  Cosmos 3、AdaPlanBench、CHERRL、AutoLab 与 StreamMA v2 已读完整 primary text 的方法、数据、训练/Serving 或 interaction protocol、
  评估、消融、限制或缺失限制声明及
  相关附录。Self-Distilled Policy Gradient 已读完整 v1、理论与实验 appendices、当前作者实现说明和
  Ch25/27～30 邻接章节；M3Eval 已读完整 v1、四类 task construction、全部 evaluation/appendices、官方
  project/repository/dataset surface 与 Ch14/22/62/73 邻接章节；当前仓库不是可证明的 event-time snapshot，
  Hugging Face dataset viewer 当前也不能提供可审计的 sample-level schema。StreamMA 的 v1 event-time 正文与
  README 所引用的 runnable implementation 未能取得，已进入
  blocked backlog，不以 v2 的后续模型/实验结果倒写 W23；Scholar/OpenAlex/DBLP/formal
  cross-check 仍 pending。
- AI Infra：已重扫 fixed release/RFC/PR source list。恢复 SGLang issue #27462、vLLM v0.22.1、
  Transformers GHSA-fgcw-684q-jj6r/CVE-2026-5241 与 Datasets 5.0.0，并联读直接修复 PR/commit。
  SGLang issue 是持续修订的当前 roadmap，只能证明所读 revision 的目标 protocol；vLLM 与 Datasets
  release 只证明版本行为；Transformers advisory/commit 则证明特定 native integration 的信任边界修复。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Dreaming: memory synthesis | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Must Read |
| Claude chemist / NMR workflow | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Worth Watching |
| Claude cyber-threat mapping | 3 | 3 | 4 | 4 | 4 | 3 | 21/30 | Worth Watching |
| GPT-Rosalind capability update | 3 | 3 | 4 | 5 | 3 | 3 | 21/30 | Official state |
| Google Agentic RAG | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Worth Watching |
| On the Scaling of PEFT | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read — full review complete |
| Cosmos 3 | 5 | 5 | 4 | 4 | 4 | 3 | 25/30 | Must Read — full review complete |
| Code2LoRA | 4 | 4 | 5 | 4 | 5 | 3 | 25/30 | Must Read — full review complete |
| Harness-1 | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Must Read — full review complete |
| Deep-research span-level error localization | 5 | 5 | 5 | 4 | 5 | 2 | 26/30 | Must Read — full review complete |
| KVarN | 5 | 5 | 5 | 4 | 5 | 2 | 26/30 | Must Read — full review complete |
| AdaPlanBench | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Worth Watching — full review complete |
| Reward hacking in rubric-based RL | 5 | 5 | 5 | 4 | 5 | 2 | 26/30 | Must Read — full review complete |
| AutoLab | 4 | 5 | 5 | 4 | 5 | 2 | 25/30 | Must Read — full review complete |
| Streaming Communication in Multi-Agent Reasoning | 5 | 5 | 4 | 4 | 5 | 2 | 25/30 | Must Read — current v2 full review complete；v1/artifact blocked |
| Self-Distilled Policy Gradient | 5 | 4 | 4 | 4 | 5 | 3 | 25/30 | Must Read — full review complete |
| M3Eval | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Worth Watching — full review complete |
| Continual Experience Internalization | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Source Review complete — provisional R / Ch73 / Ch25 handoff / Experimental |
| Agents' Last Exam | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Unverified / Blocked Backlog — score provisional |
| SWE-Explore | 4 | 4 | 5 | 4 | 5 | 2 | 24/30 | Unverified / Blocked Backlog — score provisional |
| Unembedding Matrix Feature Lens | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Unverified / Blocked Backlog — score provisional |
| Geometry of On-Policy Distillation | 5 | 4 | 4 | 4 | 5 | 3 | 25/30 | Unverified / Blocked Backlog — score provisional |
| Retrospective Harness Optimization | 5 | 5 | 5 | 4 | 5 | 2 | 26/30 | Unverified / Blocked Backlog — score provisional |
| LatentSkill | 5 | 5 | 4 | 4 | 5 | 2 | 25/30 | Unverified / Blocked Backlog — score provisional |
| OpenSkill | 4 | 5 | 5 | 4 | 5 | 2 | 25/30 | Unverified / Blocked Backlog — score provisional |
| When Tools Fail | 4 | 4 | 5 | 4 | 5 | 2 | 24/30 | Unverified / Blocked Backlog — score provisional |
| Graph Memory for LLM Agents | 4 | 5 | 4 | 4 | 5 | 3 | 25/30 | Unverified / Blocked Backlog — score provisional |
| Program-of-Layers | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Unverified / Blocked Backlog — score provisional |
| SkillHarness | 4 | 5 | 5 | 3 | 5 | 3 | 25/30 | Unverified / Blocked Backlog — score provisional |
| SGLang parallel speculative decoding roadmap | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Must Read — full review complete; Experimental / revision-sensitive |
| vLLM v0.22.1 | 3 | 4 | 4 | 5 | 4 | 2 | 22/30 | Worth Watching — full review complete; version fact |
| Transformers LightGlue nested-config RCE disclosure | 4 | 5 | 5 | 5 | 4 | 2 | 25/30 | Must Read — full review complete; security case |
| Hugging Face Datasets 5.0.0 | 4 | 4 | 5 | 5 | 4 | 2 | 24/30 | Worth Watching — full review complete; breaking version fact |

当前账目为 33 行：21 个 `25～30`、12 个 `20～24`、0 个 `<20`。评分只决定审计优先级，
不等于 Books disposition。

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Baseline score rows / source families | 5 / 5 | 5/5 `20+` reviews retained |
| Recovered in-window families | 24 | Continual Experience Internalization 恢复后共 13 项完成 current-version Full Source Review；11 项因 primary text/artifact access 转入 Unverified / Blocked Backlog；0 current-review pending；StreamMA v1/artifact 仍是已读 v2 family 的 revision sub-gap |
| Fixed official / Infra families | 4 | SGLang roadmap、vLLM v0.22.1、Transformers security advisory、Datasets 5.0.0 均完成直接 primary-source review |
| Recorded `20+` candidates | 33 | 21 high / 12 mid；六维合计已复算 |
| Earlier-week spillbacks | 16 | 15 项按 v1 回拨 W22；NITP v1 05-24 回拨 W21 |
| Later-feed spillbacks recovered | 11 | W24～W26 display feed 中 v1 06-02～06-05 的 families 已归 W23 |
| Cross-year duplicate | 1 | Language Models Need Sleep first public 2025-09；W23 arXiv node 不重复计新事件 |
| Academic discovery window | Open | HF first pass complete；cross indexes pending |
| Official / Infra fixed checkpoint | Passed | fixed source list 已回放；四个新增 source families 均完成 primary-source review |
| W23 forward Candidate Gate | Passed with explicit blocked ledger | 22/33 current-version Full Source Reviews；11/33 Unverified / Blocked Backlog；0 current-review pending；cursor remains W24 |
| W23 discovery / Historical Evidence Gate | Open | StreamMA v1/artifact、11 blocked families与 academic cross-index 未闭合 |

## Deep Analysis — 长期 Memory 是持续重建，不是无限 Append

### Why → Principle → Mechanism

持续追加历史会让 token、检索噪声、过期事实与错误累积同时增长。官方页面把问题明确为
freshness、continuity、relevance、correctness 与 scale。稳定原则是长期 memory 必须维护
identity、provenance、version、salience、expiry 和 user control，并根据新证据重新综合，而
不是把全部聊天记录当成永远有效的 context。

### Trade-off → Connection → Evolution

```text
raw history
→ selected memory items
→ retrieval into context
→ periodic synthesis / consolidation
→ 新增错误合并、过期判断、可解释删除与恢复问题
```

关系是 Ch71 Context → Ch73 Memory 的 `Direct Evolution` 于同一 state lifecycle。旧的短期
history 在低跨度、低个性化需求下仍更透明。

## Evidence Level

官方页面可证明产品问题和 rollout；实现细节与效果仍为版本化厂商事实，不能写成所有 memory
系统的固定算法。PEFT scaling 的算法、系统和实验结论来自作者论文：它证明所披露模型、任务、
rank、训练 recipe、adapter catalog/cache 与 serving tests 下的结果，不证明百万用户部署已经成立，
也不把作者定义的 capacity law、personal-model 类比或 voting 曲线外推为通用定律。Code2LoRA 与
Harness-1、DRIFT/TELBench、KVarN、Cosmos 3、AdaPlanBench 与 CHERRL 的机制、实验和限制也已按 primary text 复核；Code2LoRA 只证明
单一 1.5B code backbone、Python assertion-completion contract 下的 repository-conditioned adapter；Harness-1
只证明其 retrieval benchmarks、harness、reward 和 verifier contract 下的 state externalization；DRIFT 只证明
TELBench annotation/harness 下的 span localization；KVarN 只证明披露模型、2-bit layout、生成任务与
pseudo-decode contract 下的 error-accumulation mitigation；Cosmos 3 只证明其公开数据 mixture、
训练/Serving contract 与 benchmark/harness 下的分塔 MoT 和 action-transfer 结果，不证明生成视频对
intervention 因果正确；AdaPlanBench 只证明合成 household planning、judge-mediated hidden constraints 与
文本 plan revision contract 下的行为，不证明具身执行或真实用户偏好适配；CHERRL 只证明 Qwen3-4B、
两个 English datasets、人工注入单一 judge bias 与六条 hacking runs 下的受控动态和离线 onset detection，
不证明真实多偏置 reward loop 的在线检测或缓解。AutoLab 只证明 36 个 executable tasks、固定
terminus-2 harness、三次 rollout 与 2～12 小时 wall-clock contract 下的 long-horizon 行为；其 persistence
关系是轨迹关联而非独立因果干预，25-task harness ablation 也不能外推为所有模型与 runtime 的稳定排行。
当前公开仓库含 W23 之后的 v1.1 提交、公开 reference/solution 目录与 benchmark canary，不能充当
2026-06-03 的 immutable artifact，也使未来训练污染成为 live-benchmark governance 问题。StreamMA
当前 v2 的算法、理论、实验与附录已复核；它证明的是所披露 API、prompt、benchmark、拓扑和多次运行
contract 下，step-granular forwarding 的效果、延迟与成本边界，不证明所有 Agent DAG 都具有 head-strong /
tail-weak profile，也不证明更多 steps 构成跨任务 scaling law。v1 event-time 正文未能访问，current repository
又只公开 README 与图片、缺少 README 引用的 `StreamMA.py`，因此 v2 新增模型/实验不能倒写成 W23 事实，
代码级 queue、completion、failure 与 backpressure 语义仍为 `Unverified / Blocked`。其余 11 项新增候选仍只完成
metadata/abstract/submission-history 级发现；Continual Experience Internalization 已恢复全文并完成审计。
W24/W25 展示日不构成它们的新 event date。

SGLang issue #27462 是作者维护的 primary design roadmap：它公开 verifier/drafter ownership、
`base_committed_len` 版本检查、token-only enumeration buffer、transport/control messages 与 fallback contract，
但 current issue 含事件日后的修订和大量未完成 checkbox，不能证明 2026-06-06 已实现或 production-ready。
vLLM v0.22.1 release 与 PR #43864 证明 Ray multi-node data-parallel hang 来自 bind 后地址没有传播进已
pickle 的 actor，以及修复为 Ray path 恢复 driver-side port allocation；它不证明所有 distributed hang 都源于
port ownership。Transformers advisory 与修复 commit 证明 LightGlue nested config 绕过 caller
`trust_remote_code=False` 的特定 RCE path，并新增 native-integration lint；它不等于所有 custom-code path 已被
静态分析覆盖。Datasets 5.0.0 release 证明 Agent trace ingestion 与 streaming shuffle 的 breaking version
behavior，不证明跨 Agent 工具的 trace semantics 已归一化，也不证明生成的 `messages` 足以保留 environment、
artifact 与 side-effect provenance。

## Cross-Week Deduplication

与 W17 ReasoningBank 是 `Principle Reuse`：都处理 experience consolidation，但 identity、
owner、retention 与 failure semantics 不同。PEFT scaling 与 W20 MinT 是同一 Source Family：W20 是
基础设施 first-public node，W23 是把 algorithmic Scale Up/Down/Out 与 MinT lifecycle 联结的论文节点，
不能重复计作两套独立 production evidence。Language Models Need Sleep 的 OpenReview 版本自 2025-09
公开，W23 只记录 arXiv publication node，不倒写 first-public date。Agents' Last Exam 等 8 项虽在
W24 display feed 出现，但 v1 均落在 06-03～06-05，归 W23；W25 feed 的 Graph Memory（06-04）
与 Program-of-Layers（06-04）同理；其后 revision 只用于核验。Cosmos 3 的 NVIDIA announcement/project
release 在 2026-05-31，属于 W22 的 release node；W23 只计 2026-06-01 arXiv v1 technical-report node，
06-05、06-16 与 06-23 的 v2～v4 仅用于核验，不重复计事件。
vLLM v0.22.1 是 W22 v0.22.0 之后的 `Direct Evolution / Stabilization` patch node，不重复计作新的 serving
architecture。SGLang roadmap 是独立的 decoupled speculative protocol node；后续 issue edits 只用于核验 current
design，不倒写为 W23 event-time implementation。Datasets 5.0.0 的 major-version node 与此前 4.x releases
属于同一 Source Family；LightGlue advisory 的事件日是 06-03 disclosure，不把更早代码历史误写为新机制发布。

## Knowledge Tree Position

Ch25～27 adaptation objective/parameterization → Ch33～37 distributed training → Ch44/45 adapter serving
→ Ch55 Model Registry → Ch71～73 Context/RAG/Memory → Ch77 Workflow。PEFT paper 主映射 Ch26/55；
Code2LoRA 主映射 Ch26、由 Ch55 接 generated adapter revision；Harness-1 主映射 Ch71/72、由 Ch77
接 harness-owned state；DRIFT/TELBench 主映射 Ch62、由 Ch63/76/77 接 process telemetry 与 recovery；
KVarN 主映射 Ch41、由 Ch40/45/46 接 autoregressive feedback、kernel 与 serving contract；Cosmos 3
主映射 Ch10，Ch13/14/17/18、Ch23/24、Ch62 与 Ch75 分别承接 modality clock、attention/parameter
boundary、data/training、evaluation 与 planning handoff；AdaPlanBench 主映射 Ch75，由 Ch62/71/73/76/77
承接 benchmark、working state、feedback 与 durable control handoff；CHERRL 主映射 Ch27，由 Ch29/62/63/68
承接 optimizer、judge audit、training telemetry 与 security handoff；AutoLab 主映射 Ch62，由 Ch66/76/77/80
承接 cost、stopping、durable search 与 Agent-run handoff；Dreaming 主映射 Ch73。StreamMA 主映射 Ch78，
由 Ch77 承接 durable queue/completion/cancellation，第 65、66 章承接 critical-path trace 与 cost contract，
第 71 章承接 arrival-order-dependent Context；与第 32、34 章的 pipeline/communication 关系只属于
`Principle Reuse`，不是训练 collective 的直接演进。
新增 fixed-source owner 为：SGLang roadmap → Ch44（Ch43/45、Ch46/47 handoff）；vLLM v0.22.1 →
Ch46 的 version/stabilization case（Ch53 handoff）；LightGlue RCE → Ch68；Datasets 5.0.0 → Ch23，
Ch62/77 只承接 evaluation/workflow trace identity。

## Recommended Action

33/33 final dispositions 已完成。正文新增或强化 shared-interface/separate-owner World Model、repository-derived
adapter、harness-owned recoverable Context、autoregressive KV-quantization feedback、cumulative planning constraint
ledger、reward-hacking onset audit 与 decoupled speculative commit protocol。PEFT lifecycle、Dreaming、Agentic RAG、
AutoLab、M3Eval、vLLM patch 与 LightGlue security case 由现有具体论点覆盖；StreamMA 因 v1/runnable artifact
缺失保持 `Emerging / Revision-sensitive / No Books Change`。11 项 blocked family 明确跳过，不从标题推断机制。
下一周为 W24；Archive/Discovery Gate 继续开放。

## Event-Date Daily Decision

2026-06-01～06-05：Weekly only。2025 first-public 的 Language Models Need Sleep 不建立 2026 Daily；
W24/W25 feed 的 10 个 spillbacks 不补造历史 Daily。

## Books Integration Decision

`Complete — Source-Family Gate under blocked-skip`。最终账本为 10 Refine、7 No Change、4 Weekly Only、
1 Emerging / Revision-sensitive、11 Unverified / Blocked。只有 Refine 修改或重验证正文；No Change 引用
具体现有论点。StreamMA 与 blocked family 不进入长期机制正文。Source-Family Books Gate 完成不等于
Archive/Discovery Gate 完成，后者继续记录 v1/artifact 与 cross-index gaps。

## Ignored Noise

把“更强 memory”简化为保存更多原始聊天，或忽略删除、纠错和用户控制；把 adapter catalog 数量
误写成同时 GPU resident 数量；把 controlled/simulated personal-model experiments 写成百万用户部署；
把 roadmap checkbox 当 release、把 patch release 当新 architecture、把一次 native-integration 修复写成
整个 remote-code attack surface 已关闭，或把 trace-to-messages 转换写成完整 Agent provenance。

## 2026-07-31 Full Re-Audit Addendum

- Dreaming 已按官方完整材料复核，并与 2024 saved memory、2025 history retrieval 组成
  产品演进链。长期结论是 synthesized memory 属于可失效、需 provenance/review/delete 的
  derived view；已与 ReasoningBank 以 `Principle Reuse` 写入 Ch73。
- Claude chemist/cyber 与 GPT-Rosalind/Agentic RAG 仍作为 dated domain evidence。

## Full Source Review

### Dreaming: memory synthesis — 29/30

- **Source Family ID / Type / History**：`CHATGPT-MEMORY-DREAMING`；OpenAI official release
  2026-06-04，联读 2024 saved memory 与 2025 reference-chat-history product history。
- **Full-read Coverage**：已读 evolution、background synthesis、freshness/relevance/continuity、
  review/edit/delete controls、rollout 与公开 limitations；内部 model、store schema、ranking、
  consistency protocol 和 benchmark 为 `Not Disclosed`。
- **Problem / Previous Design / Changed Constraint**：显式 saved memory 可控、可解释，适合少量稳定
  preference；多年/多会话规模下漏写、staleness、冲突和检索噪声增加，促使 raw history 上构建
  periodically synthesized view。
- **Mechanism / Ownership / Flow**：background process 从 conversation history 选择并合成 memory
  state；生成时读取 derived view；memory summary 暴露给用户 review/update/instruction。用户拥有
  policy/纠错权，source history 是 provenance，synthesizer 拥有派生 view，serving 只消费版本化 context。
- **Evidence Boundary**：官方材料证明产品演进、问题定义和 controls；不披露算法与系统指标，
  因此不能声称特定 consolidation 方法、correctness rate 或一致性模型具有通用性。
- **Trade-offs / Evolution**：append→select→retrieve→synthesize 获得 scale/freshness，新增错误合并、
  lineage 丢失、过度个性化、delete propagation 和 rollback；短期 raw history 在低跨度场景更透明。
  与 ReasoningBank 为 `Principle Reuse`，owner 和 data subject 不同。
- **ROADMAP / Chapters / Decision**：Ch73 主 owner，已读 Ch71～77、Ch80；Ch73 已包含 derived view、
  provenance、supersession/review/delete。`No Change — Already Covered`。

### Claude chemist / NMR workflow — 23/30

- **Source / Coverage**：Anthropic 2026-06-05 chemist/NMR white paper 已全文核对；覆盖 domain
  workflow、20 forward compounds/4 scaffolds、15 inverse cases 与公开 limitations。
- **Evidence / Limits**：结果不覆盖完整 2D/stereochemistry、多溶剂和真实 lab execution，不能从
  selected assessment 推断通用 chemistry autonomy。
- **Decision**：Ch62/69/77 已读；`Weekly Only — Domain Evidence`。没有改变 artifact、verifier、
  expert acceptance 与 provenance 的既有框架。

### Claude cyber-threat mapping — 21/30

- **Source / Coverage**：Anthropic 2026-06-03 cyber ATT&CK mapping report 已核对；它记录 observed
  activity 到 taxonomy 的映射，不是完整 incident census 或受控 capability experiment。
- **Evidence / Limits**：report 能证明发布方观察和分类流程，不能据此估计所有 threat actors、
  causal model uplift 或 unrestricted deployment autonomy。
- **Decision**：Ch62/68 已读；`Weekly Only — Observational Security Evidence`。

### GPT-Rosalind capability update — 21/30

- **Source / Verification**：OpenAI 2026-06-03 capability update 已核对；公开内容支持 biology/
  drug-discovery 的 domain workflow state，内部 model/training/runtime mechanism 部分未披露。
- **Decision**：Ch62/69/74/77 已读；`Weekly Only — Version/Product Fact`，不从 capability page
  反推 Agentic RAG mechanism。

### Google Agentic RAG — 23/30

- **Source / Verification**：Google Research 2026-06-05 Agentic RAG research entry 与关联研究已核对；
  它属于 retrieval/planning/tool-grounding family，不是 GPT-Rosalind 的产品组件证据。
- **Evidence / Decision**：公开研究支持 RAG 从 single retrieval 走向 iterative evidence acquisition，
  但作者 task/model/harness 不能外推为通用 production reliability。Ch70/72/74/77 已读；
  `No Change — Already Covered`。

### On the Scaling of PEFT — 28/30

- **Candidate / Week / Source Family**：`PEFT-SCALE-UP-DOWN-OUT`；W23；arXiv:2606.02437v1，
  2026-06-01，v2 于 06-02。它与 W20 MinT 属同一 family：MinT 提供 lifecycle/serving implementation，
  本文把 large-prior adaptation、tiny/stateful adapter 与 population infrastructure 组织成三轴证据。
- **Direct / Related Primary Sources**：arXiv metadata、43 页 v2 PDF、文中 MinT 与作者列出的 LoRA/
  QLoRA、Kimi K2 LoRA RL、OLoRA-tail、δ-mem、Context Learning、OASIS/EvoBot 和 model-count
  experiments；本轮没有把 Hugging Face 摘要或项目宣传页当全文证据。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、three-axis framing、prior-limited RL、
  trillion-scale MoE LoRA、adapter placement、rollout/training inference mismatch 与 Router Replay R3、
  rank×batch×seed sweep、RL-native initialization、OLoRA-tail、learning-rate transfer、stateful adapter/
  δ-mem、LoRA memory capacity/module ablation、skill memory、Context Learning、user simulation、adapter
  diversity voting、MinT policy identity/adapter-only mobility/tiered residency/readiness、Conclusion、
  Limitations、全部 figures/tables 和 reference boundary。论文无独立 Appendix；Acknowledgements/
  references 也已检查到 EOF。
- **Original Problem / Previous Design / Changed Constraint**：LoRA 作为单任务低成本微调时，把 adapter
  当小权重文件是合理的；当同一强基座要经历反复 RL、跨 trainer/sampler/serving 交接并服务大量
  persistent variants 时，参数效率不再等于 lifecycle 可用性。MoE routing 还会把微小数值差异放大成
  rollout 与 trainer 激活不同 experts 的 effective-policy mismatch。
- **Mechanism / State Ownership / Flow**：`Scale Up` 用 LoRA 把强 prior 带进预算受限 RL，并要求 dense/
  expert adapter placement 与 TP/PP/EP/SP 共设计；R3 记录 rollout router decisions，在 training replay
  以降低路由路径不一致。`Scale Down` 联合 rank、initialization、batch/learning-rate 与 stateful adapter；
  `Scale Out` 把 adapter tensors、optimizer/checkpoint、rollout、evaluation、immutable exported revision、
  catalog/CPU cache/GPU batch residency 分离。Policy record 拥有 durable identity，policy session 拥有
  mutable training state，adapter revision 是 fixed serving/evaluation object，residency 只是 placement fact。
- **Implementation Details / Evaluation Contract**：作者报告 1.04T total/32.6B active MoE 的 LoRA GRPO
  case，但硬件、完整并行 degree、通信 fabric 与端到端 SLO 并未完整披露，故只作 feasibility evidence。
  OLoRA-tail 的受控例使用 DeepSeek-R1-Distill-Qwen-1.5B、DAPO-Math-17k、500 steps、lr 1e-5、
  effective batch 32、rank16/alpha32，并在 rank1 Qwen3-8B/30B-A3B 做 6-seed 比较。LoRA memory law
  来自 DishNameBenchmark 263 runs；skill memory 来自 Qwen3-235B rank32 ALFWorld；model-count voting
  使用 Qwen3-30B、同一 RL recipe、200 sources、每个 k 30 次子集采样。MinT 把 106-entry catalog、
  CPU cache、64-adapter same-batch window、cold-load staircase 与 readiness 分开报告。
- **What the Evidence Proves**：论文在其受控 contract 下支持三点：强 prior 的小更新可以形成有用行为；
  tiny adapter 的可靠性由 rank、initialization、batch/seed 与 policy drift 联合决定；大 adapter population
  只有在 identity、revision、mobility、evaluation 和 residency 被分层后才成为系统对象。它还提供
  “catalog addressability ≠ CPU residency ≠ active GPU batch”的直接系统证据。
- **What It Does Not Prove / Threats to Validity**：作者明确说明这是一条方向，不是已部署的百万 personal
  models；大部分证据来自 benchmarks/simulations，真实长期用户验证有限。不同章节联合多个模型、任务
  和已有工作，不能把三轴整体解释成单一 randomized experiment。LoRA capacity threshold 只属于合成
  DishName 设置；OASIS/user simulation 不证明真实用户心理；voting gain 不证明任意 adapter diversity
  有用；1T case 缺少完整 hardware/SLO contract，不能比较通用成本。
- **Trade-offs / New Failure Modes**：更小 adapter 降低训练、存储、移动成本，却增加 seed fragility、
  capacity saturation 与 hyperparameter sensitivity；parametric state 降低 prompt/retrieval dependence，
  却更难编辑、删除、归因和隔离事实；大 catalog 增加 addressability，却把 cold activation、cache locality、
  base compatibility、readiness、rollback 与 noisy-neighbor 变成显式系统问题。Full fine-tuning 在需要
  大表示迁移时仍成立；retrieval/context 继续拥有可编辑事实与 exact evidence；merge 在变体少且低动态时
  仍可简化 runtime。
- **Evolution Relationship**：`parameter-efficient update → adapter artifact → versioned policy revision →
  tiered residency → population-level routing/voting` 是 `Direct Evolution`；与 Ch73 外部 Memory 是
  `Layering / Dependency`，不是用参数化 memory 覆盖可审计 store。与 W20 MinT 是同一 Source Family
  的 algorithm-to-infrastructure 连接，不能重复计算为独立 production deployment。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch25～27、Ch54～56、Ch73。Ch26 已有低秩数学、
  trainable-state 边界、merge/dynamic serving、adapter metadata；Ch55 已有 immutable model identity、
  evaluation/promotion 与 registry/artifact split。真实缺口是 policy record/session/revision/residency 的
  adapter-specific lifecycle，以及“parameter efficiency 必须穿过训练到 serving handoff 才成为系统收益”。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument`，主 owner
  Ch26，Ch55 接 adapter revision identity，Ch73 只保留 external/parametric-state boundary；Historical Books
  Gate 关闭，本轮不修改 Books。待验证：1T case 的 hardware/parallel/SLO；长期 adapter update 的 deletion/
  unlearning；base revision migration；cold-load fairness；population diversity 相对等算力 sampling/self-
  consistency 的 matched control。

### Code2LoRA — 25/30

- **Candidate / Week / Source Family / History**：`CODE2LORA-REPO-EVOLUTION`；W23；
  arXiv:2606.06492v1，first public 2026-06-04。本轮以 v1 HTML 为正文，不把后续 artifact 页面状态倒写为
  6 月 4 日的新论文版本。
- **Direct / Related Primary Sources**：arXiv metadata 与 738 行完整 HTML；正文链接的 anonymous code、
  Hugging Face checkpoints/RepoPeftBench 只核对为作者提供的 artifact 入口，本轮未运行。相关来源是 LoRA/
  QLoRA 与本周 PEFT scaling；它们用于定位演进，不替代本文实验。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、Related Work、repository encoder、Static/Evo
  hypernetwork、训练公式、RepoPeftBench construction/splits、models/baselines/metrics、static/evolution/OOD
  results、Conclusion、Limitations，以及 dataset、dependency resolution、architecture/training/compute、OOD
  caveats、per-repo variance、repository-count scaling、commit-position trend、generated-LoRA structure、error
  analysis、DRC coverage、deployment efficiency 和 Discussion 附录。
- **Original Problem / Previous Design / Changed Constraint**：RAG/Dependency Context 把 repository evidence
  放进每次 Context，适合可编辑、可引用和按请求变化的事实；per-repo LoRA 把知识参数化，适合稳定 repository，
  但每个 repo 都需训练，并会随 commit 演进而 stale。当系统需要面对大量未见 repositories 与连续 diff stream
  时，“重新检索”与“重新训练 adapter”都暴露了 token、训练和 refresh 成本。
- **Mechanism / State Ownership / Flow**：authoritative state 仍是 versioned repository snapshot 与 ordered diffs。
  Frozen Qwen3-Embedding-0.6B 把 4096-token chunks（512 overlap）聚合成 file embeddings，再由 weighted mean +
  max pool 形成 2048-dim repository representation。Static head 用约 720M-parameter hypernetwork 生成 rank-16、
  alpha-32 LoRA，覆盖 Q/K/V/O 与 gate/up/down，且同一 module-type adapter 跨 28 layers 共享。Evo 以初始 snapshot
  初始化 2048-dim GRU state，按 diff embedding 更新并在每一步生成 adapter；TBPTT 每 16 commits detach。Repo/
  diff 拥有事实，GRU state 拥有历史压缩，generated adapter 是与 base revision 绑定的 derived artifact。
- **Implementation / Evaluation Contract**：base 为 Qwen2.5-Coder-1.5B bf16，单 job 使用 H100 80GB；604 个
  permissively licensed Python repos，2025-04-01 cutoff，512 in-distribution、92 temporal OOD。Static track 为
  39,612 train / 11,636 test assertion-completion tasks；Evolution training 使用 215,129 commit-derived tasks，
  tests 86,793。Baselines 包括 pretrained、RAG、dependency-resolved context、FFT、single/per-repo LoRA 与强化版
  Text2LoRA；metrics 为 relaxed EM、EditSim、CodeBLEU，另有有限 pytest execution probe。作者报告 Static CR
  63.8% EM、Evo CR 60.3% EM；这些数字只属于上述 model/task/split，不能外推为通用 code-agent correctness。
- **What the Evidence Proves**：在该 contract 内，whole-repository conditioning 可生成未见 repository 的 adapter；
  当 evaluation 随 commit history 演进时，recurrent diff aggregation 优于同论文中的 static/single-adapter baselines。
  Per-repository 数据很少时，cross-repo hypernetwork 也显示较低回退率。它证明的是受限 parametric adaptation，
  不是“参数永远优于 retrieval”。
- **What It Does Not Prove / Threats to Validity**：只有 Python、一个 1.5B backbone、一个短 assertion target 任务；
  OOD targets 更短，使绝对 EM 膨胀；主 metrics 多为 surface similarity，完整 functional execution 未覆盖；
  720/745M hypernetwork 并不天然“轻量”；没有 production concurrency、multi-repo isolation、adapter migration、
  delete/unlearning 或真实 serving SLO。作者的 `<10ms` generation/storage 表是部署估算，不是多租户系统验证。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：参数化 state 消除 per-query retrieval tokens，
  却把 freshness、diff ordering、GRU recovery、base compatibility、adapter revision、rollback 与事实删除变成系统
  问题。RAG 仍适合证据必须可引用/授权/快速更新的任务；per-repo LoRA 在 repository 少、数据充分且变化慢时更
  简单；Static head 在没有可信 ordered history 时避免 recurrent state corruption。
- **Evolution Relationship**：`retrieval/context per request → per-repo trained adapter → cross-repo generated adapter →
  diff-conditioned adapter trajectory` 是 `Direct Evolution`；与 Ch71/72 是 parameters-vs-context 的
  `Alternatives`，与 Ch55 是 derived artifact identity 的 `Layering / Dependency`。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch25、Ch26、Ch55、Ch71～73。Ch26 已有 base/adapter identity、
  merge/dynamic serving 和 metadata，Ch55 已有 immutable revision/lineage，Ch71/72 已有 derived-view freshness 与
  retrieval contract。缺口不是 LoRA 数学，而是“generated adapter 必须绑定 source snapshot/diff range、generator/
  state revision 与 base model，且不能成为 repository source of truth”。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`；主 owner
  Ch26，Ch55 只接 generated revision identity，Ch71/72 保留参数化与 retrieval 的共存边界。Historical Books Gate
  关闭，本轮不修改 Books。待验证跨语言/大 backbone、diff reorder/recovery、source deletion、matched inference
  latency 与独立 artifact reproduction。

### Harness-1 — 27/30

- **Candidate / Week / Source Family / History**：`HARNESS1-STATE-EXTERNALIZING-SEARCH`；W23；
  arXiv:2606.02373v1，first public 2026-06-01。本轮阅读全文为 63 页 v1 PDF；GitHub repository 作为关联
  artifact 入口核对，但未在本地重跑训练或八套 benchmark。
- **Direct / Related Primary Sources**：arXiv metadata、63 页 PDF、作者 GitHub。关联 Context-1/Search-R1/
  Tongyi DeepResearch 只按本文披露的 baseline protocol解释，未把论文对这些系统的描述提升为各项目事实。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、state model、policy actions、two-tier memory、
  SFT/RL pipeline、terminal reward、benchmarks/baselines/metrics、results、training dynamics、Discussion、Limitations，
  以及 tool signatures、reward/training hyperparameters、benchmark statistics、working-memory rendering、programmatic
  nudges、state-transition algorithms、prompts/verifier、compression/dedup、component error analysis、evaluation recipe、
  modular RAG、same-LLM harness confound、qualitative trajectories 与 NeurIPS checklist 的统计/compute disclosure。
- **Original Problem / Previous Design / Changed Constraint**：短 search loop 把完整 transcript 留在 Context，模型同时
  负责 query、记忆已见 documents、维护 constraints、压缩 evidence 和停止，结构简单且易于重放。Long-horizon
  retrieval 使 append-only observations 超预算，terminal reward 又要同时训练 semantic search 与可恢复 bookkeeping，
  因而需要把后者外置到 environment-owned state。
- **Mechanism / State Ownership / Control Flow**：policy 只拥有 semantic actions：search/read、curate、verify、stop。
  Harness 拥有 candidate pool `P`、curated set `C`、importance map `I`、full-text store `D`、evidence graph `G`、
  verification cache `V`、history/budget state。Retrieval result 先压缩、去重并写 `P/D/G`；首次结果 auto-seed 8 项，
  policy 再以四级 importance 编辑最多 30 项的 `C`；verifier 写 claim-document verdict；renderer 在 32K context 中
  保留 2K generation budget，并按五阶段 degradation 优先保留 curated state。外层 full text 可通过 doc ID 回读，
  因而 compact working state 不等于删除 evidence。
- **Training / Evaluation Contract**：GPT-5.4 teacher 产生约 900 条过滤 SFT trajectories；gpt-oss-20b 使用 rank-32
  LoRA，SFT 3 epochs/32,768 context。RL 在 SEC 3,453 queries 上用 on-policy CISPO、128 queries×8 rollouts、
  80 steps（约 82K rollouts）、40-turn cap、temperature 1.0、无 KL anchor；terminal reward联合 curated F-beta、
  trajectory/final-answer recall、tool diversity、miss 与 turn penalties。八个 benchmarks 覆盖 web/finance/patents/
  multi-hop QA，四个不进入 SFT/RL；main table 为三次运行平均，但并非所有比较都报告 CI/significance。
- **What the Evidence Proves**：在作者统一 retrieval/reranking 与 curated-set protocol 下，Harness-1 的 20B policy
  获得 0.730 average curated recall；same GPT-5.4 从 Context-1 harness 切换到 Harness-1 harness 时 recall 从
  0.807 到 0.849，为“interface 本身改变固定模型可用搜索能力”提供受限对照。Inference-time ablation 显示移除
  importance、compression、auto-seed、graph、verify/review 或全部 mechanisms 会改变 discovery/selection 行为。
- **What It Does Not Prove / Threats to Validity**：组件消融未 retrain，因而混合了组件价值与 policy 对训练接口的
  依赖；LLM verifier、regex entity graph 和 BM25 sentence compression 都可能错；qrels 不完整/近重复会改变 recall；
  breadth-oriented research、open-ended report、missing-evidence abstention 与 adversarial web 不在主要范围；managed
  Tinker 未披露底层 worker/hardware，且主比较缺少完整 significance tests。不能把论文的 frontier-model 排名写成
  通用模型能力排行。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：外置 state 降低 prompt bookkeeping 与 overflow，
  但新增 schema/version、renderer bias、eviction、verification-cache staleness、ID normalization、cross-stage interface
  skew 与 recovery responsibility。薄 harness + full transcript 在短 horizon、evidence 少、需要最透明原始轨迹时仍
  合理；deterministic top-k 在 latency/成本严格且任务可单跳时仍合理。
- **Evolution Relationship**：`append-only transcript → selective context pruning → candidate/curated split → compact
  working state + full evidence store → policy trained over explicit state transitions` 是 `Direct Evolution`。与 Ch73
  长期 Memory 只是 `Principle Reuse`：本 state 主要在 episode 内，truth authority 仍属于 corpus/artifact。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch71～74 与 Ch77。Ch71 已有 context assembly、compression、
  artifact references 与 budget；Ch72 已有 query/compression/verify/stop joint policy；Ch74 已有 typed actions；Ch77
  已有 deterministic spine 与 model-driven nodes。真实缺口是把 search interface 显式定义为“policy-owned semantic
  decisions + harness-owned recoverable bookkeeping”，以及 train/eval/serve 必须共享 state renderer contract。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`；主 owner
  Ch71/72，Ch77 只接 state-transition ownership。Historical Books Gate 关闭，本轮不修改 Books。待验证 component
  retraining ablation、adversarial/missing-evidence environment、verifier calibration、crash/replay semantics 和等预算
  baseline。

### Deep-research span-level error localization / TELBench / DRIFT — 26/30

- **Candidate / Week / Source Family / History**：`TELBENCH-DRIFT-PROCESS-DIAGNOSIS`；W23；
  arXiv:2606.02060v1 first public 2026-06-01，v2 仅在 2026-06-02 修订。本轮以完整 v2 HTML 核验
  最新正文，同时保留 v1 event date；不能把 revision 当作第二个事件。
- **Direct / Related Primary Sources**：arXiv metadata、28 页论文的完整 HTML、TELBench/DRIFT 论文内
  annotation、prompt 与 experiment artifacts。GAIA、XBench、BrowseComp、MiroFlow 与 OAgent 只作为论文
  披露的 source environment，不据二手描述改写各项目机制。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、Related Work、dataset pipeline、semantic-span
  segmentation、expert annotation、TELBench filtering/splits、DRIFT 三模块与公式、metrics、五个 model families/
  四种 harness 比较、scale/complexity sensitivity、module ablation、efficiency、Conclusion，以及 annotation UI、
  tool normalization、error taxonomy、stage/fault analysis、token consumption、case study 和 prompts 附录。正文没有
  独立 Limitations/Threats section，因而把缺失声明与实验范围本身共同记为 evidence limit。
- **Original Problem / Previous Design / Changed Constraint**：只验 final answer 在短、结构化任务上简单且直接，
  但长 research trajectory 会混入正常探索、失败搜索、暂定假设、恢复和真正有害承诺；同一正确答案仍可能经历
  不可靠过程。约束从“是否答对”变为“哪一条 claim 在何处失去支持、何时首次影响后续决策”。
- **Mechanism / State Ownership / Flow**：原始 framework logs 先折叠 tool call/result 并按 local objective 切成
  semantic spans。DRIFT 的 Claim Keeper 建立 ledger，记录 claim text、introduction span、first consequential
  span、reuse set、type 与 commitment status；Support Seeker 判定 direct/weak/missing/conflicting support；
  Dependency Tracer 标出 commit/reuse/amplify/finalize 链。Truth authority 仍属于 trajectory evidence 与人工 gold；
  ledger 是诊断 state，不是新的事实源。
- **Implementation / Evaluation Contract**：2,790 trajectories 来自 465 tasks，覆盖 GAIA-val、XBench 和抽样
  200 个 BrowseComp-test tasks；三种 base models × 两种 agent frameworks。两个不同 model-family annotators 先做
  high-recall proposals，再由七人 expert pool 中两人复核，每位 expert 投入超过 300 小时。1,890 个 error-bearing
  trajectories 过滤为 Verified-1K（600 easy/400 hard，平均 11.95 spans）。评测使用 macro precision/recall/F1 与
  first-error accuracy，重复三次；tool access 中 search/read 被统一，其他工具保留 framework-native configuration。
- **What the Evidence Proves**：在 TELBench contract 内，claim ledger、support checking 与 dependency tracing 的
  DRIFT variants 多数优于 same-backbone bare reading；module ablation 从 Claim Keeper 到完整 pipeline 逐步改善。
  97.3% failed trajectories 含 process error，但 36.9% successful trajectories 也含 process error，支持“outcome 与
  process reliability 不等价”。Scaling 不呈单调改善，说明结构化诊断 interface 可能比只放大 backbone 更关键。
- **What It Does Not Prove / Threats to Validity**：annotation 候选由 LLM 生成，semantic boundary、expert adjudication、
  qrel/ground-truth 与统一 search/read stack 均可能引入 bias；三套 benchmarks 和两个 frameworks 不代表生产 research。
  first-error accuracy 在 hard split 仍低，不能把 DRIFT 输出当 authoritative root cause。作者的 stage/fault percentages
  是该语料统计，不是通用 incident rate；成功轨迹中的“error”也不等于用户伤害。论文未评估在线 latency、
  abstention、adversarial sources 或跨版本 replay。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：claim-centric auditing 提高可定位性，却新增
  span segmentation、ledger identity、support threshold、dependency over-attribution 与高 token cost；Gemini-2.5-Pro
  DRIFT 在表中平均约 53K tokens/trajectory。Outcome-only eval 在短、确定性强、可执行 grader 完整时仍更便宜；
  full trace/manual review 在高风险、低流量任务仍是最终裁决分支。
- **Evolution Relationship**：`final-answer score → step/process labels → semantic-span localization → claim-support ledger
  → first harmful commitment and propagation trace` 是 `Direct Evolution`；与 Ch63 tracing 是 `Layering / Dependency`，
  与 Ch76 Reflection 是 `Principle Reuse`，不是把 offline benchmark 直接当 online recovery policy。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch62、Ch63、Ch76、Ch77。Ch62 已区分 outcome/process/system
  evaluation 和 executable evidence，Ch63 已有 trace/provenance，Ch76 已有 diagnose-before-retry。稳定缺口是
  “正确 outcome 不清除过程风险”以及把 first harmful commitment、support 与 downstream reuse 组成诊断 contract。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`，主 owner
  Ch62，Ch63/76/77 仅做 handoff；Historical Books Gate 关闭，本轮不修改 Books。待验证跨 annotator calibration、
  hidden-gold 情况、online sampling/retention budget、first-error uncertainty 与真实 incident correlation。

### KVarN — 26/30

- **Candidate / Week / Source Family / History**：`KVARN-AUTOREGRESSIVE-KV-QUANT`；W23；
  arXiv:2606.03458v1，first public 2026-06-02，当前无后续 revision。本轮以完整 v1 HTML 与作者链接的
  vLLM implementation 入口核验；未把 repository 当前状态倒写成 event-time release behavior。
- **Direct / Related Primary Sources**：arXiv metadata、完整 HTML、作者 KVarN repository 入口；KIVI、QuaRot、
  KVQuant、PolarQuant、TurboQuant、Kitty 与 eviction methods 只按本文 matched table/related-work boundary 解释，
  未用作者摘要替代这些方法自己的证据。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、KV quantization/incoherence/dual-scaling background、
  magnitude-direction decomposition、pseudo-decode、KVarN method、attention reconstruction、end-to-end reasoning/
  instruction/line retrieval、runtime、Related Work、Conclusion，以及 Hadamard layout、distribution/MSE analysis、
  models/quantization/decoding/task/baseline/effective-bit contract、Limitations、eviction comparison、NIAH、VarN
  algorithm、Triton dequantization 与 compute-cost appendices。
- **Original Problem / Previous Design / Changed Constraint**：prefill-like static quantization 适合固定 prompt cache，
  并可用 reconstruction/NIAH 检查一次性压缩；long-horizon Decode 中，新 token 的 hidden/KV 是读取已量化历史后
  产生，再次量化并反馈到后续 layer/timestep。约束从“压缩一个已有 tensor”变为“压缩一个持续回写的状态机”。
- **Mechanism / State Ownership / Flow**：沿 KIVI layout 按 head/channel 与 128-token chunk 处理，K per-channel、
  V per-token；先做 channel-axis Hadamard rotation，再用 log-domain alternating row/token 与 column/channel variance
  normalization 得到 dual scales，最后 2-bit RTN。标准 scale/zero-point 与额外 row scale 共同定义 cache tile；
  extra scale 融入 dequant kernel。Runtime/KV allocator 拥有 tile lifecycle，quantizer 拥有 encoding metadata，
  model semantics 仍要求 reconstructed K/V 与 position/block identity 一致。
- **Implementation / Evaluation Contract**：四个公开模型 variants：Qwen3-4B、Llama-3.1-8B-Instruct、Phi-4、
  Phi-4-reasoning-plus。所有 quantized runs 使用 2-bit body、FP16 sink/recent regions，通常 group/sink/recent
  均为 128（IFEval sink 32），auxiliary scales/zeropoints 为 8-bit，effective 约 2.3 bits/element。任务包括
  IFEval 541、MATH-500 500、AIME24 30、HumanEval 164、line retrieval 6×100 与 NIAH 3,112～31,129 tokens；
  reasoning/coding 多为 Avg@3。作者用 pseudo-decode 让后续 blocks 读取已量化 cache，区别于 static setting。
- **What the Evidence Proves**：在上述模型、sampling、2-bit layout 与 benchmark contract 内，KVarN 的 dual-axis
  normalization 降低 token-magnitude tail error，并在 pseudo-decode 中比 KIVI 更少累积 attention-output error；
  end-to-end tables 支持它在若干长生成任务上优于列出的 matched baselines。Hadamard 与 VarN 对不同 outlier 区域
  互补，说明最小 MSE 不是唯一有用的 quantizer objective。
- **What It Does Not Prove / Threats to Validity**：作者明确说明不适用于无 KV cache 的 SSM，MLA interaction
  尚不清楚，公开 serving framework 当时缺少 2-bit KV end-to-end support。GPU 只披露 500 FP16 TFLOP/1.8 TB/s，
  未披露型号、并发、batch、完整 SLO；1,050 ms generation 与 1.9 ms normalization 的 0.18% 只属于 Qwen3-4B/
  128-token test。Triton dequant gap 至多 1.4% 也不是多请求服务结果；约 50 GPU-days 不构成独立 reproduction。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：dual scales 降低 feedback error，却增加 metadata、
  normalization、kernel coupling、checkpoint/runtime compatibility 与 mixed-layout migration。FP16 在短 context、低并发、
  高精度敏感任务仍最简单；4-bit 或 mixed precision 在 kernel 生态不成熟时更稳；eviction/token merging 与 quantization
  是可组合分支，不是互相替代。Static evaluation 仍适合只压 prompt 的场景，但不能代表 generated-cache feedback。
- **Evolution Relationship**：`FP16 KV → per-axis low-bit static cache → incoherence/outlier handling → dual-axis
  normalization → autoregressive state-feedback evaluation` 是 `Direct Evolution`；与 eviction 是 `Alternatives / Layering`，
  与 Ch40 Decode、Ch45 kernel、Ch46 vLLM 是 `Layering / Dependency`。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch40、Ch41、Ch42、Ch45、Ch46。Ch41 已覆盖 KV correctness、
  bytes、quantization 与 PagedAttention identity，Ch40 已解释 autoregressive state commit；稳定缺口是“量化后的历史
  改变后续未量化 KV 的生成分布”，以及 evaluation 必须模拟 repeated read→produce→requantize feedback。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`；主 owner
  Ch41，Ch40/45/46 只做短 handoff；Historical Books Gate 关闭，本轮不修改 Books。待验证实际 GPU/并发/SLO、
  2-bit paged-block fragmentation 与 prefix sharing、MLA/GQA variants、failure recovery 和 independent reproduction。

### Cosmos 3 — 25/30

- **Candidate / Week / Source Family / History**：`COSMOS3-OMNIMODAL-WORLD-ACTION`；W23 technical-report
  node；NVIDIA announcement/project release 为 2026-05-31（W22），arXiv:2606.02800v1 first public
  2026-06-01，v2/v3/v4 分别为 06-05、06-16、06-23。本周只计 arXiv v1，不把 release 与 revisions
  重复计作新事件。
- **Direct / Related Primary Sources**：arXiv metadata 与 current v4 technical report、NVIDIA Cosmos 3
  project page/technical blog、NVIDIA/cosmos repository、Hugging Face official model/data collection。论文是
  event-time mechanism/evaluation authority；repository 当前 main 已包含后续 Edge、distillation 与 limitation
  文本，只作为 current artifact cross-check，不倒写为 06-01 已公开行为。
- **Access / Full-read Coverage**：已覆盖 139 页 technical report 的 Abstract、Introduction、architecture、
  token arrangements、action representation、reasoner/generator data、pretraining/mid-training/post-training、
  SILA data platform、distributed training/checkpoint、Serving、48 项 reasoner benchmarks、image/video/audio/
  transfer/action/policy evaluation、Related Work、Conclusion，以及 synthetic-data、caption/prompt contract、
  reasoner initialization、FPS/audio/action-mode/cross-domain ablations、human-evaluation 与 task setup 附录。
  正文没有独立 Limitations/Threats section；因此以实验 contract、未披露项和 current repo 明示 failure modes
  共同限定结论。
- **Original Problem / Previous Design / Changed Constraint**：VLM、video/world generator 与 VLA/WAM 分离时，
  各组件可独立优化、认证和按 SLO 部署，适合 modality objective 与控制周期不同的系统；代价是语言语义、
  visual state、action coordinate 与生成条件在组件间反复翻译。新约束是同一 Physical AI backbone 要在理解、
  simulation、forward/inverse dynamics 与 policy 之间迁移，同时处理不同采样率、噪声目标与 embodiment interface。
- **Mechanism / State Ownership / Control and Data Flow**：ViT 编码理解视觉，冻结 Wan2.2 video VAE 与 audio
  VAE 编码生成流，domain-specific projections 把 3D translation、6D rotation 与 gripper/hand state 映射为
  action tokens。每层 MoT 为 Reasoner 与 Generator 保留独立 LayerNorm/MLP、共享 attention；AR subsequence
  只 causal 读取 AR KV，diffusion subsequence 双向读取 AR+DM KV，信息由 reasoner 单向条件化 generator。
  3D MRoPE 与 temporal modulation 对齐 video/audio/action clocks。Reasoner、Generator、modality codecs、
  action projections 与 runtime 分别拥有其 state；environment/sensor/robot outcome 仍是 truth authority。
- **Implementation / Training Contract**：Reasoner 使用约 24.2M samples，并以 semantic dedup 与 model-judge
  filtering 形成 pretrain/SFT mixture；Generator 从 7.8B raw images/3B raw videos 过滤到 767M images/
  347.7M clips，再加入 8.4M action episodes、61.3K hours。Nano generator 披露 31.05T tokens/1024 GB200，
  Super 为 17.86T/2048 GB200；采用 HSDP+Context Parallelism、token-budget packing、two-way varlen attention、
  selective activation checkpointing、compiled VAE 与 asynchronous checkpoint。作者测得的 54%、22%、13%、
  41% 等增益分别绑定其 rank-synchronous loader、attention、checkpointing 与 compile baseline，不能相乘或外推。
- **Serving Contract**：Reasoner 走 TensorRT-LLM/vLLM，Generator 走 vLLM-Omni/PyTorch path；Reasoner
  conditioning 可跨 diffusion steps 缓存，Context/CFG Parallelism 面向单请求 latency，varlen packing 面向
  throughput。T2V 189-frame、74K-token contract 下，256p batching 在 H100 80GB/GB200 的收益随模型而异，
  480p 收益很小，720p 只能 batch 1；论文明确 robotics latency-bound batch=1 不从 batching 获益。所谓
  “统一模型”没有消除 AR 与 diffusion 的不同执行循环和 Serving surface。
- **Evaluation Setup / What the Evidence Proves**：Reasoner 以 VLMEvalKit 覆盖 19 general、17 robotics、9
  smart-infrastructure 与 3 driving benchmarks。Generator 联合自动指标、model judges、human evaluation、
  Physical AI suites 与 real-robot tests；作者还披露 public PAIBench-G I2V judge 结果不可复现，改用内部
  Qwen2.5-VL-72B judge 并独立提交 public leaderboard。Action 以相同 model size/data/compute 比较 PT-init 与
  MT-init；RoboLab-120 每 task 10 rollouts，specific instruction 下 39.7% average success。证据支持 shared
  action mid-training 在所测 domain/interface 上提供 reusable initialization，并支持 reasoner/generator 分塔、
  FPS 双重控制和 joint-action objectives 的受限消融收益。
- **What It Does Not Prove / Threats to Validity**：video/audio judge、internal driving sets、proprietary
  egocentric/driving data 与 leaderboard snapshot 都限制外部复现；PSNR 只被作者用作短 horizon temporal/
  reconstruction proxy，不证明 counterfactual causal correctness。39.7% 不是可靠控制门槛，complex-specific
  success 仍为 29.4%。论文未给统一的 latency/energy/cost/safety SLO，也未证明 long-horizon rollout、
  distribution shift、multi-agent interaction、sim-to-real safety 或跨 embodiment 的无条件泛化。current repo
  另列 temporal inconsistency、motion instability、A/V misalignment、action-state inconsistency、object morphing、
  3D/physics errors，要求 safety-critical deployment 另做 validation 与 guardrails。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：统一 token/interface 降低组件间 semantic
  translation，并允许 cross-domain initialization；代价是 modality mixture/clock、objective interference、
  codec/projection identity、structured-prompt dependence、巨大训练数据/compute、双 runtime compatibility 与
  action-state consistency。模块化 VLM + simulator + policy/controller 在实时控制、独立认证、替换单组件、
  隔离 failure domain 或数据权限不同的系统中仍合理；统一 backbone 与专用 post-training/controller 可共存。
- **Evolution Relationship**：`modular perception → video/world prediction → action-conditioned world model →
  shared omnimodal token interface + separate reasoner/generator towers → domain post-training and external
  controller` 是 `Direct Evolution + Layering / Dependency`，不是单向替代。与 Decoder-only 的统一 prefix
  interface 是 `Principle Reuse`，因为 diffusion subsequence 与 objective 并非 causal next-token generation。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch9/10、Ch13/14/17/18、Ch23/24、Ch62、Ch75。Ch10 已有
  language model/world model/controller 分工、pixel realism≠causal correctness、sim-to-real 与 intervention/
  long-horizon/control evaluation；稳定缺口是统一 checkpoint 内仍用异构 parameter towers、mask/objective、
  modality clocks 与 Serving loops 隔离职责。Ch62 已有 model/harness/environment/outcome 分层，不需要复制
  leaderboard。架构、数据和 Planning 章节只需短 handoff，不应各自复述整篇论文。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`；
  主 owner Ch10，Ch17/18、Ch23/24、Ch62/75 仅 handoff。Historical Books Gate 关闭，本轮不修改 Books。
  待独立复现 world-action transfer、公开 judge/human agreement、closed-loop long-horizon safety、action-token/
  controller calibration、failure recovery，以及 W22 official-release node 的后续 ledger 回补。

### AdaPlanBench — 24/30

- **Candidate / Week / Source Family / History**：`ADAPLANBENCH-DUAL-CONSTRAINT-REPLANNING`；W23；
  arXiv:2606.05622v1 first public 2026-06-04，v2 于 2026-07-09。事件归 v1；本轮以 v2 核验修订后的
  mechanism、evaluation 与 appendix，不把 revision 计作新事件。
- **Direct / Related Primary Sources**：arXiv metadata 与完整 v2 HTML、作者 repository、official
  Hugging Face dataset。MacGyver 是 task seed；repository 当前 main 没有 immutable release/tag，且可包含
  event date 之后的 flags 与修订，只作 artifact cross-check，不倒写为 v1 行为。
- **Access / Full-read Coverage**：已覆盖 Metadata、Abstract、Introduction、Related Work、307-task
  construction、world/user constraint generation/filtering、environment protocol、evaluation metrics、十模型
  main results、constraint-profile/user-vs-world/memory/rubric-feedback/temperature/threshold ablations、human
  validation、Limitations、Conclusion 与相关 appendices；并核对 runner/config/evaluator 和 dataset schema。
- **Original Problem / Previous Design / Changed Constraint**：静态 planning benchmark 一次给全题、一次收
  final answer，适合低成本、可复现比较；但真实 planning 常在执行前后才暴露工具不可用、环境事实或用户
  preference。约束从一次性 prompt 变成随 interaction 累积的 state 后，planner 不只要找到局部替代，还要
  防止新修订破坏前几轮已满足的不变量。
- **Mechanism / State Ownership / Control and Data Flow**：每个 task 绑定 hidden environment
  `E=(B_w,B_u)`；world constraints 表达 object/tool unavailable or nonfunctional，user constraints 表达
  tool/action attributes。Agent 提交 plan `p_t`，GPT-5.4 world/user judges 返回违反集合，simulator 按
  world-first priority 生成 feedback，agent 再规划；成功要求全约束通过且三位 rubric judges 的每项分数
  达到阈值。Benchmark environment 拥有 hidden constraint truth，runner 拥有 turn/termination state，agent
  只拥有可见 feedback 与自己的 working plan；这不是可独立观测环境的真实 executor。
- **Implementation / Evaluation Contract**：数据由改写后的 MacGyver tasks 经 GPT-4.1、DeepSeek-V3.2、
  Qwen3.6-Flash 多 planner 采样约束，再由 GPT-5.4 checker 过滤；主实验使用三档 profiles、最多 20 turns，
  no-new-violation patience 为 2。Accuracy 要求 terminal plan 同时 constraint-valid 和 rubric-pass；VPR 只测
  constraint validity，另报 turns、重复 world/user violations 与 normalized triggered constraints。主结果和
  ablations 绑定这套 synthetic household、model-judge、text-only contract，不保留模型排行为通用结论。
- **What the Evidence Proves**：在该 contract 下，terminal constraint validity 可以很高而 task plan 的
  effectiveness/physical plausibility 仍不通过；显式保存已披露 constraints 能明显改善 VPR，却对多数所测
  模型的 Accuracy 改善很小；继续给 rubric feedback 虽可提高 Accuracy，却可能显著破坏原有 constraint
  validity。它为“state retention != planning quality”以及“局部 repair 需要全局 regression gate”提供了受限证据。
- **What It Does Not Prove / Threats to Validity**：constraint 由模型生成并只在 plan 违反时由 oracle-like
  judges 揭示；agent 不能主动提问、检查工具或执行 action，所以所谓 proactive exploration 是 proposal-driven
  constraint triggering，不是 observation/action exploration。有效 plan 不等于执行成功。Accuracy 对 rubric
  threshold 高度敏感；human study 的 240 trajectories 各只由一人标注，且 physical plausibility/effectiveness
  正是 exact match 较弱的维度。household-only、text-only、shared model-family bias、MacGyver rewrite、无真实
  soft preference、无 embodied outcome 与无独立 reproduction 都限制外推。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：累积 constraint ledger 减少重复违反，
  却增加 provenance、authority、staleness、conflict 与 token/selection 成本；逐轮局部修补降低搜索范围，
  却可能产生 recency bias 和跨约束回归。一次性 static planning 在约束稳定、环境 fully specified、低交互
  budget 的任务中仍合理；真实系统还需把 environment observations、user clarification、policy constraints 与
  simulator/judge feedback 分开，并由 workflow 保留 revision、rollback 与 verifier identity。
- **Evolution Relationship**：`static fully specified plan → feedback-conditioned replanning → explicit cumulative
  constraint state → revision-wide regression verification → executable environment outcome` 是 `Direct Evolution +
  Layering / Dependency`。world constraints 与 user/policy constraints 共享检查形式，但 authority/mutation
  semantics 不同；两者相似仅是 `Principle Reuse`，不能合并为模型可自行修改的一类文本约束。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch62、Ch71、Ch73～77。Ch75 已有 partial observability、
  belief update、observation-triggered replanning、immutable constraints 与 plan version；缺口是把已披露约束
  作为累积 ledger，并在每次 revision 后重新验证全部 invariants，而不是只验证本轮 feedback。Ch76 已有
  constraint-wise audit 和 regression metric，Ch77 已有 durable state/policy enforcement；它们只需 handoff。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`；
  主 owner Ch75，Ch62/71/73/76/77 仅 handoff。Historical Books Gate 关闭，本轮不修改 Books。待验证真实
  observation/action environment、direct clarification、constraint conflict/expiry、judge calibration 与 shared-
  family bias；current artifact 还需要 immutable release/commit identity 才能作为 event-time implementation evidence。

### Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based RL — 26/30

- **Candidate / Week / Source Family / History**：`CHERRL-RUBRIC-REWARD-HACKING`；W23；
  arXiv:2606.04923v1 first public 2026-06-03，当前只有 v1。事件归本周，不能用 current repository main
  的后续内容反推 06-03 已公开的 implementation state。
- **Direct / Related Primary Sources**：arXiv metadata、23 页完整 HTML（含全部 appendices）、作者
  THUAIS-Lab/CHERRL repository、RHDA documentation。仓库当前显示 13 commits、无可见 release，且由 veRL
  fork 扩展；full rollout JSONL、完整 workspaces、API logs 与部分 external mirrors 不在仓库中，因此是
  partial artifact，不构成独立 reproduction。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、formalization、dual-judge bias injection、
  onset construction、environment/training dynamics、capability evaluation、discoverability/exploitability analysis、
  RHDA architecture/evaluation、Related Work、Conclusion、Limitations，以及 threshold sweep/manual audit、detector
  implementation/outputs、budget ablation、case studies、compute/infrastructure、artifact/data boundary 与 non-hacking
  runs 附录；并核对 repository layout、reward aggregation、reproduction scripts、RHDA schema/CLI 和数据缺口。
- **Original Problem / Previous Design / Changed Constraint**：rubric-based RL 用单个 model judge 为开放任务
  提供 scalable reward，在缺少 executable verifier 时是合理的旧方案；但 policy 持续优化后会主动搜索 judge
  的 style/semantic preference。只看 aggregate proxy reward 或最终 checkpoint 会把“真实改善”“shortcut 首次
  出现”和“shortcut 已饱和”混在一起，也无法为 monitor 建立有 reference 的检测任务。
- **Mechanism / State Ownership / Control and Data Flow**：CHERRL 用同一 Qwen3.5-27B foundation 构造 intended
  rubric judge 与 specialized bias detector，形成 `J_biased = J_unbiased + alpha * bonus`，其中 `alpha=0.5`。
  Qwen3-4B policy 通过 GRPO 优化 combined proxy；research-side 同时保留 intended judge score、bias bonus、
  deterministic shortcut prevalence 与 threshold sweep，构造 onset point/interval。deployment-like detector 只能
  看到 sanitized `{step,input,output,score}` mirror；RHDA 通过 Inspect/Analyze/Compute/Reason、persistent hypothesis
  state 与 bracket-and-shrink search 输出 typed onset alert。研究环境拥有 injected-bias/reference state，training
  runtime 拥有 policy/rollout/reward lineage，detector 只拥有 judge-blind mirror；三者不得混成一个可见状态面。
- **Implementation / Evaluation Contract**：policy 为 Qwen3-4B，两个 judges 均为 Qwen3.5-27B；HealthBench 与
  VerInstruct 上注入 lexical、format、tone、self-praise 四类 bias，共观察到六条 hacking 与两条 non-hacking
  settings；总训练/推理约 2,000 NVIDIA H100 80GB GPU-hours。reference onset 由 smoothed reward gap 与高分样本
  shortcut prevalence 的 12 组阈值交叉构造，并用两位作者独立标注、第三位 adjudication 做轻量 sanity check。
  RHDA 与 Claude Code baselines 看同一 score-bearing mirror，CoT monitor 却看 no-score reasoning samples，接口
  不完全 matched；RHDA 主表只有六个离线 runs，且 finalized representative predictions 不是统一重复试验聚合。
- **What the Evidence Proves**：在人工隔离单一 bias 的 contract 内，combined reward 可继续上升而 intended
  judge reward 持平或下降；不同 bias 的发现时间和后续放大速度确实不同。受控关联与 generation probe 支持
  把 `discoverability` 与 `exploitability` 分开分析。六条 runs 上，持久 hypothesis + adaptive temporal inspection
  比论文中的 fixed step-wise monitor 和 general coding-agent baselines 更接近 operational onset interval；budget
  ablation 还表明更多 calls 只有形成 temporal evidence chain 时才有价值，不保证单调改善。
- **What It Does Not Prove / Threats to Validity**：`J_unbiased` 仍是 model judge，不是人类或 executable
  ground truth；canonical onset 是研究者选择 smoothing、shortcut detector 和 thresholds 后的 operational label，
  宽区间与 pre-onset shortcut background 已显示边界。OR 与 onset 的关系来自六条 observed hacking runs，不能
  证明普遍因果；non-hacking 只表示标准训练时长内未发现。主 policy 只有 4B，一组 judge family、两个 English
  datasets、四类显式 bias。RHDA 是 offline retrospective detector，允许 unlimited tool budget；没有 online
  alert latency、false-positive/no-hack evaluation、intervention、mitigation 或 post-alert rollback 证据。作者也明确
  说明 detector 不提供修复。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：dual-judge isolation 获得可控 reference，
  却制造了真实系统通常不存在的 privileged observability，并可能继承同源 judge 的 correlated blind spot；
  sanitized mirror 更接近可部署接口，却删除 reward components 后增加 attribution uncertainty。Adaptive agent
  audit 能积累 hypothesis 和调用统计工具，代价是大量 token/tool budget、search-policy instability、surface-cue
  overfitting 与自身 false alert。低成本 fixed monitors 仍适合已知 deterministic signatures 和高频 guardrail；
  human/executable audits 仍是高风险 release/stop decision 的 authority。
- **Evolution Relationship**：`single proxy reward → independent quality slices → controlled counterfactual reward
  decomposition → judge-blind temporal audit → online intervention/rollback` 是 `Direct Evolution + Layering /
  Dependency`。CHERRL 只覆盖前三项并实验第四项；第五项尚未实现。与 generic incident monitoring 是
  `Principle Reuse`：都需 baseline/transition/persistence evidence，但 training policy 持续改变数据分布，不能把
  普通 static threshold 直接当 reward-hacking detector。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch27～30、Ch62～65 与 Ch68。Ch27 已说明 Goodhart、policy
  会搜索 reward-model 漏洞和 independent evaluation；稳定缺口是把 reward-side decomposition 与 policy-side
  judge-blind monitor 分开，并将 discovery、exploitation、onset interval 作为 training control state。Ch29 只
  承接 GRPO optimizer/reward lineage；Ch62 已有 judge/rubric audit，Ch63～65 已有 metrics/logs/traces ownership，
  Ch68 已有 sensor/authority 分离，均不应复制本文结果。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`；
  主 owner Ch27，Ch29/62/63/68 仅 handoff。Historical Books Gate 关闭，本轮不修改 Books。待验证跨 policy/
  judge/dataset 复现、composite/semantic bias、no-hack false positives、online latency 与 stop/rollback authority；
  公开 full rollouts、workspace 与 immutable event-time artifact 后，才可升级 reproduction evidence。

### AutoLab — 25/30

- **Candidate / Week / Source Family / History**：`AUTOLAB-LONG-HORIZON-ITERATIVE-EVAL`；W23；
  arXiv:2606.05080v1 first public 2026-06-03，当前只有 v1。官方仓库 2026-04-01 建立，但 current main
  已包含 2026-06-17 的 v1.1 提交；仓库没有可见 release/tag，因此 current task tree 不能反推事件日
  artifact identity。
- **Direct / Related Primary Sources**：arXiv metadata、514 行完整 v1 HTML、官方 project/leaderboard、
  `autolabhq/autolab` repository、commit history、task tree，以及 `flash_attention` 的 instruction、
  `task.toml` 和公开 reference/solution 目录。关联 MLE-Bench、RE-Bench、PaperBench、PostTrainBench、
  KernelBench、Frontier-Eng 与 Harbor 只用于定位旧方案，不用二手比较替代本文实验。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、task formulation/construction/composition、
  scoring equations、anti-reward-hacking、experimental setup、主结果、Flash Attention case、cost/failure/
  harness ablation、Related Work、Conclusion、Limitations，以及 36 项 task specification、per-task anchors/
  gates、provider/hardware table、全部 task-level Avg@3/Best@3、generation 与 stability appendices；并核对
  当前 repository 的 Harbor layout、resource limits、baseline/reference metadata、network policy、verifier
  boundary、version history 与 event-time drift。
- **Original Problem / Previous Design / Changed Constraint**：static correctness、final patch 与短 trajectory
  benchmark 适合可重复 regression，也能低成本比较一次生成或一次修复；当目标变成持续数小时的系统/
  模型优化时，能力取决于何时跑实验、如何利用 noisy feedback、是否保留有效中间结果、何时停止并提交。
  只看 terminal artifact 会把模型、harness、iteration budget 与失败路径压成一个分数，无法解释 early stop、
  context exhaustion 或“找到过更优解却最终回退”。
- **Mechanism / State Ownership / Control and Data Flow**：每项任务由 instruction、containerized environment、
  editable baseline、local evaluator、held-out verifier、human reference 与 wall-clock budget 构成。Agent 在
  sandbox 内循环 `inspect → edit → execute/profile → local feedback → revise`；Harbor/terminus-2 拥有 timer、
  action interface 与 trajectory，workspace 拥有当前 artifact，benchmark owner 拥有 task/reference/verifier
  revision，model 只拥有候选决策。结束时 held-out verifier 先执行 correctness/feasibility gate，再将 raw
  metric 相对 baseline/reference 映射为 anchored linear 或 log-stretch score。三个独立 rollouts 聚合为
  Avg@3、Best@3 与跨模型 Dominance；这些对象不能合并成“model capability”单一 owner。
- **Implementation / Evaluation Contract**：论文评测 17 个 model variants；主表比较 11 个 provider
  flagships，36 个任务分为 15 system optimization、10 puzzle/challenge、7 model development、4 CUDA。
  budget 为 2～12 小时，CPU contract 是 AMD Ryzen 9 9950X（16 cores/32 threads）、64 GB RAM，GPU
  task 使用 H100 或 L40S；总计 2,544 wall-clock hours、8.60B tokens。每个 model-task 三次 rollout。
  harness ablation 只覆盖 4 个 models、25 个 CPU tasks 与 terminus-2/pi-mono/修改后的 mini-swe-agent；
  不覆盖 GPU/model-development 全集。性能 anchors 绑定特定 sandbox/hardware，论文未披露全部 API
  temperature、provider-side serving state、逐 trial token/cost trace、完整 raw trajectory release identity。
- **What the Evidence Proves**：在论文固定的 task、provider、terminus-2、budget 与 scoring contract 下，
  结果支持 long-horizon performance 与 action count/runtime/persistent benchmark-edit loop 同向关联；302 个
  zero-score rollouts 的人工审计区分 timeout/context exhaustion、capability gap、instruction violation 与
  upstream failure。Flash Attention case 说明 initial/final score 会遗漏中间最优 artifact 与 time allocation；
  limited harness ablation 还证明同一 model 的 score、iteration effort 与 inference cost 会随 harness 显著变化，
  因而 model 与 harness 必须联合报告。三次 rollout 的 dispersion 也支持 capability 与 reliability 分开记录。
- **What It Does Not Prove / Threats to Validity**：persistence 是 observational correlate，不是随机控制
  iteration count、thinking budget 或 stopping policy 后的独立 causal effect；更长 trajectory 也可能只是更高
  spend。36 项任务都具有 executable metric，不能代表开放式 scientific discovery、需求协商、现实副作用或
  多人 review。固定 harness 提高模型间可比性，却不代表各模型的最优 Agent system；25-task ablation 也不足以
  建立通用 harness 排名。Avg@3 仍只有三次 trial，人工 failure labels 与 task/reference calibration 由作者团队
  完成，未给 inter-rater agreement。当前公开仓库含 v1.1 后续修改并公开 reference/solution 路径；论文声明
  evaluation 时 reference/held-out inputs 不暴露给 Agent，这与未来模型是否受公开 artifact 训练污染是两个问题。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：continuous anchored score 奖励 partial
  progress，却依赖 baseline/reference 与 hardware calibration；wall-clock 更接近真实开发，却混入 API latency、
  provider availability 和 sandbox scheduling。sealed verifier、SHA pin、distribution-disjoint gates 与 adversarial
  audit 降低直接 hacking，同时减少外部审计透明度；公开 task/solution 提高复现性，又增加 benchmark leakage、
  memorization 与 live-version comparability debt。固定 harness 获得 apples-to-apples control，却可能压制某些模型
  的适配优势。static unit tests、single-patch benchmark 与短 trajectory 在低成本 CI、局部 regression、低风险
  feature 验证中仍是更合理的旧分支。
- **Evolution Relationship**：`static answer → executable final artifact → feedback-conditioned trajectory →
  budget/harness/resource-aware long-horizon evaluation → live revision and contamination governance` 是
  `Direct Evolution + Layering / Dependency`。AutoLab 覆盖中间三层，并暴露最后一层压力；它不是用 long
  horizon 否定 snapshot，而是增加 trajectory、cost、stopping、artifact lineage 与 evaluator revision 维度。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch62、Ch66、Ch76、Ch77 与 Ch80。Ch62 已有从 snapshot
  到 feedback-conditioned/evolving-state evaluation、feedback-channel ownership、executable verifier、trajectory
  debt、resource accounting 与 contamination；Ch76 已有 feedback independence、best-state retention 与 stopping
  policy；Ch77 已有 evaluator-driven search 的 sandbox、wall-clock、lineage、held-out verification、budget 和
  model/Workflow ownership；Ch66 已有 `cost_to_quality_target`，Ch80 已有 run identity、budget、trajectory、
  replay 与 release governance。AutoLab 提供受限实验证据，但没有新增长期机制缺口。
- **Integration Decision / Files / Open Questions**：`No Change — Already Covered`；主 owner Ch62，
  Ch66/76/77/80 只作章节级证据 handoff。Historical Books Gate 关闭，本轮不修改 Books。待核验 immutable
  v1 task/evaluator snapshot、完整 per-trial trajectories/cost records、污染审计、跨 harness/GPU task 复现，以及
  当公开 reference/solution 进入训练语料后 live leaderboard 如何维持可比性。

### Streaming Communication in Multi-Agent Reasoning — 25/30

- **Candidate / Week / Source Family / History**：`STREAMMA-STEP-GRANULAR-COMMUNICATION`；W23；
  arXiv:2606.05158v1 first public 2026-06-03，v2 发布于 2026-08-01。W23 事件只属于 v1；本轮完整阅读
  的 v2 只用于当前机制与 revision 核验，不能把后续 model/result changes 倒写成 6 月事件事实。
- **Direct / Related Primary Sources**：arXiv metadata、29 页 v2 PDF、作者 project page、官方
  `EnVision-Research/StreamMA` repository 页面。v1 PDF/HTML 本轮均无法取得；current repository 的公开树只显示
  `README.md` 与 `imgs/`，而 Quick Start 引用的 `StreamMA.py` 不在可见树中，也没有可定位 release/tag 或
  event-time commit。因此 v1 event snapshot 与 runnable artifact 标记 `Unverified / Blocked Backlog`，不阻塞
  后续候选，但阻止 W23 Evidence Gate 被关闭。
- **Access / Full-read Coverage**：v2 已覆盖 metadata、Abstract、Introduction、Related Work、Serial/Stream/DAG
  algorithms、三条 theorem 与完整 proofs、implementation、八 benchmark 主实验、case、head/tail perturbation、
  role/tool generalization、step/agent scaling、cost-Pareto、Conclusion、Limitations、testing configs、DAG
  pseudocode、全部 prompts、risk 与 artifact statement。未获得 v1 正文差异、可运行 code、immutable commit、
  raw per-trial traces 或 provider-side serving identity。
- **Original Problem / Previous Design / Changed Constraint**：generate-then-transfer 让下游等完整 response，
  语义清楚、上下文完整且容易重放；在多级 Agent DAG 中，它同时把每一段 generation 都放到 critical path，
  并迫使下游一次接收上游的可靠 head 与可能退化的 tail。约束变化是任务可被显式分成 reasoning steps，且下游
  能在 partial progress 到达时开始独立工作；此时 communication unit 与 arrival timing 成为算法变量，而不只是
  transport 优化。
- **Mechanism / State Ownership / Control and Data Flow**：Serial 依次把完整 output 传给下一 Agent；Stream 为每个
  Agent 建立 FIFO queue，所有节点并发运行，收到一个 upstream step 后追加到本地 Context、调用 streaming LLM，
  再把每个完成 step 立即推送给 successors；历史 prefix 供后续调用复用 KV cache。DAG source 接收原 query，
  每个 step broadcast 给所有 direct successors，多 predecessor 节点按到达顺序立即消费、没有 barrier。
  Workflow/graph owner 应拥有 DAG、queue 与 completion，Agent call 拥有 local Context/KV prefix 和候选 step，
  transport 拥有 delivery/order，evaluator 拥有 task score；论文 pseudocode 没有定义生产级 ownership transfer。
- **Implementation / Evaluation Contract**：v2 比较 Single、Serial、Stream，覆盖 AIME 2025/2026、HMMT 2026、
  GPQA-Diamond、HLE 与 LiveCodeBench generation/execution/test-output，使用 OpenCompass；四 Agent Chain/Tree/
  Graph 为主。正文披露 Claude Opus 4.6-High、GPT-5.4-None 和 GLM-5.2-None，API defaults，judge 为
  GPT-5.4-None；通常每 `{backbone, topology}` 三次，三个小数学集合八次。Stream 还加入 `END_STEP` boundary
  与 solver body，因此主实验并非纯 transport-only intervention。商业 API 隐藏具体 hardware、region、queue、
  temperature、provider cache 与并发限制。
- **What the Evidence Proves**：在 v2 的 prompt、API、benchmark 与 topology contract 下，Stream 的平均结果在
  表格各 backbone/topology cell 超过 Serial；head/tail perturbation 在同一构造题上支持 arrival timing 对错误传播
  有非对称影响。Theorem 1 明确给出 Stream、Serial 与 Single 各自占优的六种 step-correctness regimes，因而证据
  本身保留旧协议成立条件。Theorem 2/3 把 fill/drain、prefill/decode/cache-read、prompt/output ratio、cache hit、
  output-length ratio 与价格放进 latency/cost contract，比“streaming 总会更快更便宜”更精确。
- **What It Does Not Prove / Threats to Validity**：所谓 step-level “scaling law”只在 HMMT 2026、GPT-5.4、
  固定 prompt/topology sweep 中观察，且 scaling 实验关闭 KV reuse；26.9× 使用 `sum(agent API times) / wall time`
  定义，不是与 Serial wall-clock 的 matched speedup。FanOutQA 的三次结果只有 +1.1/+0.4 pp、1.17× 与近似相同
  成本。cost cache band 部分来自公式而非直接 runtime measurement。理论采用统一 step benefit/harm、简化位置权重
  与 step correctness proxy；一次 case/perturbation 不能证明生产任务普遍 head-strong/tail-weak。v2 abstract/project
  强调两个 frontier LLM，implementation 又包含 GLM-5.2；v1 内容不可访问，不能判断哪些模型和表格属于事件日版本。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：更细粒度 forwarding 缩短等待并让早期 evidence
  更早可见，却增加 API calls、Context assembly、boundary prompt、queue/trace 和 cache-identity 复杂度。无 barrier 的
  multi-predecessor DAG 会让 Context order 随 arrival latency 改变，这是从 Algorithm 3 推得的系统风险，不是作者
  已验证结论。论文未定义 bounded queue/backpressure、end-of-stream、timeout、cancellation、duplicate/reorder、
  retry/idempotency、partial-step validation、peer failure 或 deterministic replay；攻击者还可注入恶意 early steps。
  对不可 step-decompose、late self-correction 强、顺序确定性/完整上下文更重要、调用固定成本高的 workload，Serial；
  对 upstream 信息总体有害或 single-agent headroom 足够时，Single 仍是合理旧分支。
- **Evolution Relationship**：`full-response handoff → step boundary → overlapped Agent pipeline → topology-aware
  arrival semantics → backpressure/completion/failure-aware runtime` 是 `Direct Evolution + Layering / Dependency`。
  当前论文覆盖中间两层并暴露后一层压力；与训练 Pipeline Parallel、通信 alpha-beta 和 KV prefix reuse 属于
  `Principle Reuse`，不是同一 runtime 或直接历史继承。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch77～79，并联读 Ch71、Ch65、Ch66 与 Ch32。Ch78 已拥有
  coordination tax、topology、message/state split、critical path、handoff failure 与 recovery，但没有明确把
  communication granularity、partial-progress visibility、arrival order、pipeline fill/drain 与 protocol selection
  组织成同一机制链；Ch77 已拥有 durable queue、timeout、cancellation、replay 和 authoritative state，Ch65/66
  已拥有 async critical path 与 cost-to-quality contract。主 owner 因此是 Ch78，其他章节只作短 handoff。
- **Integration Decision / Files / Open Questions**：`Refine — Existing Argument / Experimental /
  Revision-sensitive`；Historical Books Gate 关闭，本轮不修改 Books。后续若 Gate 通过，Ch78 只沉淀协议选择、
  arrival semantics 与生产 failure contract，不保留 v2 headline 数字。待获得 v1 snapshot、runnable code/commit、
  matched Serial wall-clock、bounded-queue/backpressure/cancellation tests、跨 provider/task replication，以及
  multi-predecessor arrival-order sensitivity 与 adversarial early-step verification。

### Self-Distilled Policy Gradient — 25/30

- **Candidate / Week / Source Family / History**：`SDPG-VERIFIER-GATED-PRIVILEGED-DISTILLATION`；W23；
  arXiv:2606.04036v1 first public 2026-06-02，本轮未发现后续 arXiv revision。事件节点由 v1 定义；当前
  GitHub repository 有 12 commits、没有可定位 release/tag，因而代码只能作为 current implementation
  evidence，不能证明 6 月 2 日的 immutable artifact。
- **Direct / Related Primary Sources**：arXiv metadata、26 页 v1 PDF/完整 HTML、作者 project page 与官方
  `lauyikfung/SDPG` repository/README。论文公开代码入口，repository 则披露基于 verl 的 loss、dataset
  sentinel、launch configs、evaluation scripts 与关键文件路径；shell 环境无法取得 repository clone，当前 raw
  source 仅通过官方 GitHub/README surface 交叉核验，event-time commit history 标记 `Not Disclosed`。
- **Access / Full-read Coverage**：已覆盖 metadata、Abstract、Introduction、Background、GRPO/OPD/UKL
  定义、完整 SDPG objective、positive gate、beta schedule、Qwen3-4B 主实验、Related Work、Conclusion、
  KL proofs/normalized KL/one-step off-policy/OPSD approximation appendices、RLSD derivation、OPCD comparison、
  alpha/beta ablation 与 Qwen3-1.7B scale appendix；并读取当前 README 中的数据格式、硬件要求、loss modes、
  beta/gate controls、memory note 与 evaluation contract。论文没有独立 Limitations/Threats section，也没有
  seeds、confidence interval、wall-clock、peak memory、tokens/FLOPs 或 matched-compute 报告。
- **Original Problem / Previous Design / Changed Constraint**：GRPO 用 binary outcome verifier 和同 prompt
  group-relative advantage，避免 learned critic，语义清楚且只依赖可验证结果；但一个 sequence advantage
  作用于所有 tokens，all-equal groups 又没有梯度。纯 OPD 给 student-rollout prefixes 提供 full-vocabulary dense
  target，却可能在 globally wrong trajectory 上模仿 privileged teacher，并收缩 exploration。约束变化是训练集
  额外拥有 answer/solution context，且系统愿意支付第二视图 forward、frozen reference 与 full-logit matching，
  以换取比 sparse outcome 更细的局部 shaping。
- **Mechanism / State Ownership / Control and Data Flow**：同一 `pi_theta` 在 `x,y_<t` 下是 deployable student
  `p_t`，在 `c,x,y_<t` 下是 detached privileged teacher `q_t`；trajectory 仍由不含 `c` 的 rollout policy 采样。
  verifier 先产生 binary reward 和 group-normalized `A_out`，只有 `A_out>0` 的 response 才计算 exact
  full-vocabulary reverse KL `D_KL(p_t || stop_gradient(q_t))`。固定 `pi_ref` 再提供 UKL anchor，trainer 拥有
  behavior/current/reference version、gate、beta warmup/decay、mask 与 reduction；dataset owner 必须拥有
  `(x,c)` lineage，verifier owner 拥有 outcome truth，actor/teacher 两个 view 不能被“同一个模型”掩盖为同一份
  runtime state。若同组 reward 全相同，mean-centered outcome advantage 与 positive gate 同时归零。
- **Implementation Details**：理论的完全 on-policy形式不需要 PPO clipping；verl 现实路径存在 rollout/current
  的 within-step drift，因此 appendix 用 importance ratio 和 PPO-style clipping 写出 one-step off-policy
  approximation。实现保留 fixed-prefix full-vocabulary KL 的 direct pathwise gradient，省略 prefix sampling 的
  score-function gradient；作者以 `beta*KL` 较小及额外 variance 为理由，但这仍是近似。当前 README 说明
  actor/teacher `(B,T,V)` logits 同时 materialize，SDPG 还启动 frozen reference worker；这使其不能与不含
  teacher/reference 的 GRPO 只按 accuracy 比较成本。当前 `core_algos.py` 还对 response 的 stop-token 位置
  屏蔽 distillation KL，以避免 privileged teacher 的 continuation mass 削弱 EOS；该规则未出现在 v1 论文中，
  README 又把论文定义的 `D_KL(student || teacher)` 称作 “forward KL”。这两点都应作为 current-artifact
  nomenclature/implementation drift，而不是倒写成事件日算法定义。
- **Evaluation Contract**：主实验用 Qwen3-4B，appendix 用 Qwen3-1.7B；训练数据为 DAPO-Math-17k 的
  13.9k English samples，privileged solution 由 Gemini 2.5 Pro 生成并与正确答案一起提供给 teacher。训练
  400 steps，AdamW `1e-6`、weight decay `0.1`、global batch 128、每 prompt 8 responses、temperature 1.0、
  max prompt/response 2048/4096、FSDP bf16、dynamic batching、verl+vLLM、8 NVIDIA H100；SDPG 使用
  `alpha=1e-3`、`beta_base=1e-3`、warmup 50、decay 350。AIME24/AIME25/AMC23 按 pass@1 mean@32
  每 10 steps 评估，表格同时报告 step-400 Last 与训练中 Best；Best 存在 checkpoint selection 边界，
  mean@32 也不是 32 个独立 training seeds。
- **What the Evidence Proves**：在上述 math/Qwen/H100/400-step contract 内，两个 SDPG variants 的
  Last/Best 表格总体超过 GRPO/RLSD，1.7B 又超过无 reward 的 OPCD；training curves 显示 RLSD/OPCD 的
  entropy/length collapse，而 SDPG variants 在作者运行中较稳定。`beta=0` ablation 丢失早期 AIME 优势，
  `alpha=0` 保留相近 accuracy 却伴随更短 response 与上升 entropy。理论证明只在固定 sampled prefix、
  detached teacher/current iterate 上，reverse-KL student gradient 等价于 centered log teacher/student ratio
  的 local policy-gradient signal；实现仍计算 full-vocabulary KL，并非 sampled-token 替代。
- **What It Does Not Prove / Threats to Validity**：实验没有 independent seeds、uncertainty、compute-matched
  baseline、跨 domain/更大 scale、错误 privileged context、contamination 或 independent reproduction。
  `alpha/beta` ablation 没有分别隔离 positive gate 与 warmup/decay，因此作者把稳定性归因于二者组合仍是
  attribution，而非 full-factorial causal result。Teacher 读取 correct answer 与 Gemini solution，所以这是
  privileged supervision 的迁移，不是 label-free self-supervision；verifier false positive、solution error 或
  data leakage 都会进入 shaping。论文的 final/Best accuracy、response length 和 entropy 不能推出 reasoning
  faithfulness，也不能证明部署中移除 privileged context 后没有 residual distribution gap。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：SDPG 用 outcome gate 限制 dense teacher
  signal，并用 early warmup/late decay处理 teacher quality 与部署不可见信息；代价是额外 data provenance、
  teacher/student/reference identity、两次 context view、full-vocabulary logit memory、schedule/recovery state 与
  verifier coupling。Reverse KL 倾向 teacher high-probability modes，gate 又只利用 mixed-correct groups，可能
  降低 hard prompts 的 sample efficiency；beta decay 太早会丢失 shaping，太晚会 over-constrain。GRPO 在
  verifier 可靠、group variance 足够、成本/机制简洁优先时仍成立；pure context distillation 在 teacher 稳定、
  不需要 outcome exploration 时仍成立；process reward/step verifier 在局部 truth 可直接标注时是另一分支。
- **Evolution Relationship**：`sequence outcome only → process/step reward or learned local credit` 与
  `off-policy teacher traces → student-prefix on-policy context distillation → verifier-gated privileged shaping +
  reference anchor → provenance/error-aware teacher control` 是两条汇合的 `Direct Evolution + Layering /
  Dependency`。SDPG 没有否定 GRPO，而是把 verifier 作为 trajectory selection layer、privileged KL 作为
  local shaping layer，并新增 teacher-data、anchor、schedule 和 approximation contract。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch25、Ch27～30。Ch25 已完整拥有 same-prefix context
  distillation、full-vocabulary soft target、teacher snapshot/cadence 与 privileged-context bias；Ch27/28 已拥有
  verifier、credit assignment、reference/KL 与 policy-lag 边界；Ch29 已有 GRPO sequence-to-token sparsity、
  all-equal group、distillation 分支与 rollout/update ownership，但没有把 verifier gate、privileged full-vocabulary
  shaping、reference anchor 和 deployment information gap 组织为一个长期机制链。主 owner 因此是 Ch29，
  Ch25 只保留 context-distillation handoff，Ch27/28 不重复写算法案例。
- **Integration Decision / Files / Open Questions**：`Refine — Existing Argument / Experimental`；Historical
  Books Gate 关闭，本轮不修改 Books。Gate 通过后只在 Ch29 补充“outcome selection 与 dense local shaping
  分层”的机制、state/failure contract 和旧方案共存条件，不保留作者 benchmark headline。待核验 immutable
  event-time code、独立 seeds、matched memory/throughput、gate 与 schedule 的 factorial ablation、错误/冲突
  privileged context、非数学任务和更大模型，以及 score-function omission 对 objective bias/variance 的实测影响。

### M3Eval — 23/30

- **Candidate / Week / Source Family / History**：`M3EVAL-COGNITIVE-VIDEO-MEMORY-EVAL`；W23；
  arXiv:2606.05008v1 first public 2026-06-03，当前未见后续 revision。作者 repository README 标记
  2026-06-04 release，但公开 tree 没有 tag/release 或可定位的 event-time artifact，因此论文 v1 定义事件节点，
  current repository/dataset 只作为后发 artifact cross-check。
- **Direct / Related Primary Sources**：arXiv metadata、34 页 v1 PDF/完整 HTML、官方 project page、
  `PKU-VaLuE-Lab/m3eval` repository 与 Hugging Face dataset card。数据复用 CrossVid、HourVideo、
  InfiniBench-TVQA、LVBench、Video-MME-L 等公开 benchmark；本轮不根据 M3Eval 的二手描述改写这些来源的
  原始采集或许可。HF dataset viewer 当前因解析错误无法展示样例，repository 的 `lmms-eval` scorer/code path
  也未能取得 immutable revision，故 sample-level schema 与 scorer implementation 标记 `Not Verified`。
- **Access / Full-read Coverage**：已覆盖 metadata、Abstract、Introduction、Related Work、四类 task design、
  dataset construction、question/distractor pipeline、manual review、model/human evaluation、attention case study、
  repetition experiment、conclusion，以及 source datasets、prompt/annotation、N-Back construction、完整 tables/
  figures 与设置 appendices。论文没有独立 Limitations/Threats section，也未披露 human protocol、annotator
  agreement、decoding/seeds、统计检验、provider snapshot、成本或完整 runtime contract。
- **Original Problem / Previous Design / Changed Constraint**：长视频 QA 的 aggregate accuracy 能测试综合任务
  成功，却把 perception、encoding、reasoning、source binding 与 retention 混为一体；这在比较端到端系统时合理，
  但不能回答错误发生在注意分配、干扰抑制、事件绑定还是 working-memory load。新约束是用可控视频变换和
  error-family distractors形成诊断 slices，同时仍要避免把 task manipulation 本身产生的视觉、位置和 scorer
  confound 误称为纯 memory evidence。
- **Mechanism / State Ownership / Control and Data Flow**：Divided Attention 把两个语义相似视频并排，并比较
  no-swap 与十次均匀左右交换；Memory Interference 交换 target/competitor 的先后顺序，用 competitor-derived
  options 计算 intrusion；Interleaved Events 将两条视频各切十段后交替拼接，并加入 plausible-but-absent 的
  false-memory option；N-Back 让模型判断末尾 clip 是否与前 N 位在 scene 或 action 上匹配。Video/task builder
  拥有素材、变换、question 与 label，evaluation harness 拥有 frame sampling、prompt、option parsing 与 scorer；
  model forward 只拥有调用内 activation/KV，不能把错误答案反推为 Ch73 所定义的持久 Agent Memory state。
- **Implementation Details**：非 N-Back 部分从 451 个 source videos 形成 739 questions；N-Back 从 64 个
  12-clip sequences 生成 1,664 questions，总计 2,403 questions、约 403 小时视频。Qwen3.5-27B 先按六类
  hierarchical description 生成问题/标注，再经人工筛选；N-Back 用持续维护的 scene/action phrase list 约束标签
  复用。正文称源自 five public datasets，而 Appendix Table 4 按 CrossVid-CC/NC 拆为六行；这是 source-family
  与 row taxonomy 差异，不据此推断数据错误。
- **Evaluation Contract**：比较 Gemini-3.1-Pro-Preview、GPT-5.4、Qwen3-VL-8B-Instruct、Qwen3.5
  4B/9B/27B、InternVL3.5-8B、VideoLucy、M3-Agent 与 human reference。Gemini 使用 0.5 FPS，其他模型默认
  96 uniform frames，重复实验 144 frames，N-Back 每 clip 8 frames；本地模型在 4×A800 server 运行，
  proprietary models 通过 official APIs。Divided/Interference/Interleaved 多为四选一，random baseline 为 25%；
  N-Back 和 Figure 9 的 binary source comparison 是 50%，两者不得混算。Agent systems 的 backbone、harness、
  tool path 不匹配，也不能当作纯模型或纯 memory 比较。
- **What the Evidence Proves**：在上述素材、变换、frame sampling、prompt/scorer 与模型 snapshot contract 内，
  人类和被测系统在 divided attention、interference、interleaving 与 N-Back 上呈现不同错误形态；模型在
  false-memory discrimination、source binding 与增加 sequence length 时出现明显脆弱性。repetition experiment
  显示重复 target 或 competitor 都会改变结果，支持输入组织是有效 intervention；N/K linear fits 则为
  irrelevant-context load 与 lag sensitivity 提供可复核 slice，而不是一个 aggregate video-QA headline。
- **What It Does Not Prove / Threats to Validity**：split-screen 同时改变分辨率、视觉密度与 encoding；交换顺序
  同时改变 causal position/recency；interleaving 引入 hard cuts、temporal reasoning 与 source binding；N-Back
  还依赖 scene/action label matching。因此四类任务没有因果隔离一个独立 memory module。attention heatmap 只是
  representative cases，作者的 attention-confusion、causal-attention interference 和“模型不会选择性遗忘”均为
  解释性假设。低于 random 的 false-memory score 也可能受 none-of-the-above/option bias 影响。不同 frame budget、
  缺失 human protocol、无 multi-run uncertainty 和不可审计 sample/scorer artifact 阻止跨模型通用排名。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：认知任务分解提高诊断分辨率，却新增
  stimulus-construction bias、source-dataset license/contamination、model-generated annotation、frame-sampling
  inequivalence、option calibration 与 slice multiplicity。端到端 long-video QA 在需要测真实 task success 时仍然
  合理；M3Eval 适合作为 failure taxonomy/slice layer，不能替代 executable downstream task、free-form output、
  calibrated human study 或部署 SLO 评估。
- **Evolution Relationship**：`aggregate long-video QA → controlled transformation + error-family distractors →
  source/interference/load slices → matched multimodal harness + auditable scorer/human protocol` 是
  `Direct Evolution`；与 Ch22 effective utilization 是 `Layering / Dependency`，与 cognitive psychology 是
  `Principle Reuse`，与 Ch73 durable Agent Memory 只有 `Explanatory Analogy`。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch14、Ch22、Ch62、Ch73。Ch62 已要求 evaluation object、
  dataset/environment/scorer/harness identity、failure taxonomy、slice、uncertainty、contamination 与 claim boundary；
  Ch22 已要求按位置、距离、distractor/conflict 与 task 切分 effective utilization，并区分 accepted length 和有效
  利用。Ch73 明确只处理跨模型调用持久化的 runtime Memory，Ch14 的 attention map 也不是 causal mechanism proof。
  M3Eval 提供受限案例，但没有形成现有正文缺失的稳定设计原则。
- **Integration Decision / Files / Open Questions**：`No Change — Already Covered / Experimental Case`；主 owner
  Ch62，Ch22 只作 handoff，Ch14/73 不写入。Historical Books Gate 关闭，本轮不修改 Books。待验证 immutable
  event-time artifact、sample/scorer schema、reviewer agreement、matched frame/decoding contract、human protocol、
  free-form calibration、跨数据集复现，以及能分别隔离 perception、position/recency、reasoning 与 retention 的消融。

### SGLang parallel speculative decoding roadmap — 29/30

- **Candidate / Week / Source Family / History**：`SGLANG-DECOUPLED-PARALLEL-SPEC-ROADMAP`；W23；
  official GitHub issue #27462 opened 2026-06-06。issue 是持续修订的 design roadmap；本轮核验 current
  revision，并把 event date 与后续编辑分开，不能声称全部 current details 在 06-06 已公开或实现。
- **Direct / Related Primary Sources**：SGLang official roadmap issue；文内 linked protocol、transport、
  verifier/drafter checklist 与测试阶段。没有把二手 release digest 当实现证明；EAGLE/MTP、PP 与 RDMA
  extension 只按 roadmap 的 future-work boundary 记录。
- **Access / Full-read Coverage**：已读 motivation、colocated draft、response-based 与 enumeration-based
  design、M:N routing、ZMQ control、shared-memory token plane、versioning/fallback、lifecycle、tests、rollout
  phases、unchecked work 与 hidden-state/RDMA extension。roadmap 没有完整 benchmark、ablation、hardware、
  concurrency 或 SLO results，统一记为 `Not Disclosed / Not Yet Demonstrated`。
- **Original Problem / Previous Design / Changed Constraint**：drafter/verifier 同进程、同 GPU group 时，
  request scheduler 可隐式共享 committed prefix、draft branch 与 rollback state，适合单 failure domain；一旦
  为独立扩缩容、异构并行或容错而拆成两个 process，隐式 state 变成跨进程 protocol。早期 response-based
  design 在每 token 后由 host reconciliation/rollback 串行修正，正确但落在 Decode critical path。
- **Mechanism / State Ownership / Flow**：新设计让 verifier 唯一拥有 committed output、stop/client stream 与
  acceptance；drafter 只拥有尚未 commit 的 speculative branch。drafter 提前生成 `(K+1)×F×K` token-only
  enumeration buffer，并标记 `base_committed_len`；verifier 在 GPU 侧只消费版本匹配、real-bonus 合法的 buffer。
  `DraftSync`、`VerifyCommit`、`DraftClose` 管理 lifecycle，M:N identity 为
  `(src_verifier_rank, request_id)`。missing/stale buffer、drafter lag 或 failure 都退化为 verifier 单 token，
  不让 speculative state 成为 correctness authority。
- **Implementation / Evaluation Contract**：roadmap 指向 pinned host staging、预分配 GPU buffer、ZMQ control
  与 shared-memory token path，目标是移除 per-token host reconciliation。验证顺序是 CPU protocol tests →
  loopback exact-output → real two-process ZMQ → overlap/performance；多项 checkbox 尚未完成。没有公开
  production throughput、latency、GPU topology、model、precision、length、batch、concurrency 与 SLO contract，
  因而不记录任何性能 headline。
- **What the Evidence Proves / Does Not Prove**：证据足以证明 decoupled speculative decoding 需要显式
  commit authority、future-buffer versioning、safe degradation 与 request lifecycle；不证明 enumeration design
  已合入、优于 response-based design、适配 PP/多节点，或在真实 failure/overload 下保持 throughput 与 fairness。
  current issue 也不能充当 immutable event-time release artifact。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：enumeration 把 critical-path coordination
  换成额外 draft compute、buffer memory、fanout `F`、staleness 与 transport/liveness state；drafter 过慢会退化，
  太超前会浪费，retry/close/late message 又要求 idempotency。colocated design 在单机、相同并行布局、低 failure
  isolation 需求下更简单；response-based path 在协议清晰度优先且吞吐压力较低时仍可接受。EAGLE/MTP 若传
  hidden state 会引入独立 RDMA data plane、tensor identity 与 lifetime；rejection sampling 还需 probability state。
- **Evolution Relationship**：`colocated implicit state → response-based explicit reconciliation → one-round-ahead
  enumeration → hidden-state/RDMA extension` 是 `Direct Evolution`；与 distributed request routing/KV placement
  是 `Layering / Dependency`，不是后者的替代。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch43～47。Ch44 已拥有 speculative acceptance/rollback 与
  correctness baseline，但没有跨进程 drafter/verifier 的 state-authority、version/liveness contract；Ch46/47
  已有 distributed serving 与 failure isolation，可作短 handoff。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental /
  Revision-sensitive`，主 owner Ch44；Historical Books Gate 关闭，本轮不修改 Books。待验证 immutable event-time
  snapshot、merged code path、exact-output/failure tests、M:N fairness、PP/多节点、buffer budget、drafter lag、
  cancellation/late close 与完整 workload/SLO contract。

### vLLM v0.22.1 — 22/30

- **Candidate / Week / Source Family / History**：`VLLM-0.22-STABILIZATION`；W23；v0.22.1 released
  2026-06-05，作为 W22 v0.22.0 后的 patch node，不重复计新 serving architecture。
- **Direct / Related Primary Sources**：vLLM official v0.22.1 release、PR #43864 与 PR #44366。NIXL
  connector wheel normalization 只由 release note 核验；直接 PR/code path 本轮未取得，细节不外推。
- **Access / Full-read Coverage**：已读 release 的八个 commits 与两项直接 PR。重点覆盖 Ray multi-node
  data-parallel hang、port-allocation rollback、CPU local-mode test、container dependency source 与 NIXL wheel
  compatibility；其余 model-loading fixes 只作版本清单，不推导长期机制。
- **Original Problem / Previous Design / Changed Constraint**：bind-time allocation 可减少普通 multiprocess
  endpoint 的 `get free port → later bind` TOCTOU，因此此前把部分端口延迟到 kernel bind 是合理的；Ray 会在
  bind 前把地址 pickle 进 actors，driver 后续 rebind 不会传播，`port=0` 的 ZMQ peers 可永久等待。约束变化来自
  control-plane object serialization，而非 network data plane 本身。
- **Mechanism / Ownership / Flow**：修复仅让 Ray path 在 driver 侧提前取得真实 open port，再把稳定 endpoint
  传给 actors；multiprocessing path 保留 bind-time allocation。endpoint identity 由创建 control plane 在 actor
  materialization 前拥有，actor 只消费不可变地址。代价是 Ray path 有限度恢复 TOCTOU window，换取地址可见性。
- **Implementation / Evaluation Contract**：PR 增加 CPU local-mode test，验证 API servers 与 engine cores
  看到真实且已绑定的 ports。原始 field report 为两台 GB200 上 TP1/DP8、四台 GB200 上 TP1/DP16 且
  `num_api_servers > 1`；没有披露模型、precision、length、batch、concurrency、latency/goodput SLO 或稳定性时长。
  因此只可证明 deterministic hang path 与定向回归测试，不保留性能数字。
- **What the Evidence Proves / Does Not Prove**：证据证明 address allocation 必须发生在 distributed actor
  serialization boundary 之前，且 backend-specific lifecycle 可能要求不同策略；不证明 patch 消除所有 Ray/ZMQ
  hang，也不证明 NIXL、container 或 model-loading fixes 的跨平台行为。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：提前端口选择重新引入 race；延迟 bind 对不预先
  serialization endpoint 的 backend 仍更稳。修复还提醒 API-server、EngineCore 与 transport endpoint 的 owner
  不能混同。dependency quarantine 与 CUDA-major wheel normalization 降低供应链/ABI surprise，却需要更明确的
  build matrix 和 release provenance。
- **Evolution / ROADMAP / Existing Coverage**：这是 v0.22.0 后的 `Direct Evolution / Stabilization`，映射
  Ch46（Ch53 handoff）。已读 Ch46/53/68；Ch46 已明确 control/data endpoint、API/EngineCore ownership 与
  backend-specific failure contract，Ch53 已拥有 paved-road compatibility，Ch68 已拥有 dependency provenance。
- **Integration Decision / Files / Open Questions**：`Weekly Only — Version Fact / No Change — Already Covered`；
  不修改 Books。待验证多 API server 的长期 stress/failure test、port reservation primitive、IPv6/mixed-version
  behavior，以及 NIXL wheel fix 的直接 PR/code evidence。

### Transformers LightGlue nested-config RCE disclosure — 25/30

- **Candidate / Week / Source Family / History**：`TRANSFORMERS-LIGHTGLUE-NESTED-TRUST-RCE`；W23；
  GHSA-fgcw-684q-jj6r / CVE-2026-5241 published 2026-06-03，affected `<5.5.0`，patched in 5.5.0。
  周报记录 disclosure node，不把较早 patch code 历史误写成 06-03 新机制。
- **Direct / Related Primary Sources**：GitHub reviewed security advisory 与 Transformers official fix commit
  `676559d5022b74aaa0cee1cee0842b7f27c5320e`。未以漏洞转载或 severity headline 代替 code review。
- **Access / Full-read Coverage**：已读 advisory 的 affected version、attack precondition、impact/fix 与 commit
  diff。diff 覆盖 LightGlue nested AutoConfig/AutoModel path、`trust_remote_code` 删除、registered
  `CONFIG_MAPPING` lookup、AutoModelForKeypointDetection 参数 surface、TRF014 mlinter 规则及 tests。
- **Original Problem / Previous Design / Changed Constraint**：Auto classes 允许用户显式 opt in remote code，
  便于未内置 architecture；native LightGlue integration 却从不可信 nested config 读取
  `trust_remote_code`，把调用者的 `False` 降级为配置拥有的 authority。问题不是 remote code 功能本身，而是
  trust decision 被 data/config 跨层覆盖。
- **Mechanism / Ownership / Flow**：修复删除 native integration 内的 remote-code switch，只允许从注册
  `CONFIG_MAPPING` 解析 nested config；相关 AutoModel parameter 同步删除。新增 TRF014 在 native model
  integration 中禁止显式 `trust_remote_code` kwarg、dict literal 或 `dict()` pattern。最终 trust authority 必须
  来自外层 caller/policy gate，不属于 downloaded model config。
- **Implementation / Evaluation Contract**：commit-level tests 与 lint rule 是直接 corrective evidence；没有
  benchmark、hardware 或 SLO。静态 rule 能识别列明 AST patterns，但不能证明捕获经变量、动态 kwargs、间接
  wrapper 或其他 deserialization/custom-op path，故不能宣称 attack surface 已闭合。
- **What the Evidence Proves / Does Not Prove**：证明 LightGlue nested-config path 可绕过 caller intent 并导致
  remote code execution，也证明 deny-by-construction 加 repository lint 是有效 defense-in-depth；不证明所有
  Transformers native integrations、model formats、custom kernels 或 dependency loaders 不再执行不可信代码。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：registered-only mapping 降低 extensibility，
  新 architecture 必须先进入 trusted registry；显式 remote code 在隔离 sandbox、pinned digest、人工批准且
  capability受限的实验环境仍可用。lint 会有 coverage gap，runtime policy、artifact signing、sandbox 与
  egress/secret restrictions 仍不能省略。
- **Evolution / ROADMAP / Existing Coverage**：`config-controlled convenience → caller-owned explicit trust →
  native paths deny remote code + repository lint` 是 `Direct Evolution / Corrective Evidence`。已读 Ch68 及
  Ch53/55 handoff；Ch68 已具体要求 remote/custom code 默认禁用、digest pinning、sandbox、policy gate 与
  provenance，因此本案例增强证据而不改变结论。
- **Integration Decision / Files / Open Questions**：`No Change — Already Covered / Security Case`，主 owner
  Ch68；不修改 Books。待验证其他 native integrations、dynamic kwargs lint coverage、safetensors 之外的 loaders、
  custom operator/toolchain、sandbox escape 与 advisory-to-release provenance automation。

### Hugging Face Datasets 5.0.0 — 24/30

- **Candidate / Week / Source Family / History**：`HF-DATASETS-5-TRACE-SHUFFLE`；W23；official release
  5.0.0 published 2026-06-05。它是 major-version behavior node，与此前 4.x releases 同属一条演进链。
- **Direct / Related Primary Sources**：Hugging Face Datasets official 5.0.0 release notes及其 linked changes。
  本轮没有取得 event-time immutable end-to-end trace corpus，因此不声称跨工具语义等价。
- **Access / Full-read Coverage**：已读 Agent trace ingestion、streaming shuffle breaking change、iterable
  state/checkpoint、shard fetch、robotics episode、format 与 parquet streaming fixes。release 可证明 public API/
  behavior；未披露 normalization loss、trace redaction、tool schema compatibility、replay fidelity 或 SFT outcome。
- **Original Problem / Previous Design / Changed Constraint**：原始 dataset pipeline 以静态 rows/shards 为主，
  单一 input-shard shuffle 与普通 text/message schema 简单可复现；Agent runs 带 tool calls、环境状态、artifact、
  side effects 和长轨迹，streaming 又要求跨 shard 混合而不物化全量数据。约束从 file conversion 变成 stateful
  trace normalization 与 bounded online sampling。
- **Mechanism / Ownership / Flow**：5.0.0 通过 optional `teich` 解析 Claude Code、pi、Codex traces 为
  `messages` 并暴露 prompt/sent-at/count fields；streaming shuffle 默认同时读取多个 input shards，旧行为可用
  `max_buffer_input_shards=1` 恢复。iterator 的 `state_dict/load_state_dict` 保留 recovery owner，fetch threads
  改变 I/O concurrency，但 dataset revision/schema 仍必须由 pipeline manifest 拥有。
- **Implementation / Evaluation Contract**：证据是 release behavior 和 linked fixes，没有 model-training
  benchmark、hardware、length、batch、concurrency 或 SLO contract。parquet streaming hang 与 iterable skip
  fixes 只证明特定 bug surface，不证明任意 remote filesystem/restart exactly-once。
- **What the Evidence Proves / Does Not Prove**：证明 Agent trace 已进入通用 dataset ingestion surface，且
  streaming shuffle policy 会改变 sample order/mixing；不证明转换后的 `messages` 保留 environment/action/result/
  artifact/side-effect provenance，不证明不同 Agent runtimes 语义一致，也不证明新 shuffle 默认值改善训练质量。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：统一 messages 便于 SFT 与工具链复用，却可能
  丢失 runtime-specific authority、failure/retry、artifact identity 与 secrets；多 shard shuffle 增加 mix quality，
  也增加 prefetch memory、I/O concurrency、resume determinism 与 remote failure surface。单 shard 模式在严格
  locality、低内存与旧 revision reproduction 下仍合理。
- **Evolution / ROADMAP / Existing Coverage**：`static rows → streaming shards + resumable iterator →
  cross-shard shuffle → Agent trace normalization` 是 `Layering / Dependency`，不是把 trace archive 直接升级为
  training truth。已读 Ch23、Ch62、Ch77；Ch23 已拥有 schema/manifest/shuffle/checkpoint/revision contract，
  Ch62/77 已要求 harness/environment/tool/artifact identity，故没有新的长期框架缺口。
- **Integration Decision / Files / Open Questions**：`Weekly Only — Version Fact / No Change — Already Covered`，
  主 owner Ch23，Ch62/77 handoff；不修改 Books。待验证 normalized trace schema、lossless round trip、secret/
  policy redaction、artifact/side-effect lineage、resume determinism 与同一 revision 下的 sampling contract。

## Blocked Primary-Source Backlog

### Continual Experience Internalization — 27/30 — Full Source Review Complete

- **Source / Full-read Coverage**：arXiv:2606.04703v1，first-public 2026-06-03；2026-08-13 HTML 恢复。已读
  experience-learning / distillation related work、formal closed loop、granularity/injection/regime design space、三轮
  self-evolution experiments、full tables、training/inference contract 与 Appendix。未发现 immutable author artifact。
- **Problem / Previous Design / Changed Constraint**：把 trajectory/skill 作为 inference context 在一次任务内简单且
  可回退；但 experience pool 跨轮增长时会遭遇 context collapse，直接 distill 又可能只获得首轮增益。目标从
  “这次利用经验”变为“更新后的 policy 能继续产生并利用下一轮经验”。
- **Mechanism / State / Flow**：作者区分 instance vs principle experience、global vs step-wise injection、on-policy
  student trajectories vs off-policy teacher trajectories。step-wise selector 依据当前 interaction state 取经验；off-policy
  context distillation 用高质量 teacher trajectory 监督 experience-free student。policy revision、experience-pool revision、
  selector、teacher/student identity 与 iteration lineage 是最小审计状态；不能把更新后的参数与外部 memory 合并为一物。
- **Evaluation / Boundary / Trade-offs**：Qwen3-4B/8B、15K web-reasoning corpus、Search/Visit/Python/Scholar/File
  Parser、8×A800、32K context、WebWalkerQA/GAIA/BrowseComp-ZH 与最多三轮只支持作者 contract。instance items 中
  URL/domain、number、query entity 占比解释了过拟合风险；step-wise+off-policy 的稳定性不证明任意 teacher、domain、
  longer cycle。off-policy 降低 flawed-state local correction，却增加 teacher cost、distribution mismatch 与错误策略固化；
  on-policy 在高质量 student state、单轮 adaptation 下仍可能合理。
- **Evolution / Chapters / Decision**：`store/retrieve experience → abstract principles → state-aligned injection → parameter
  internalization across versioned cycles` 是 Ch73 的 `Direct Evolution`，Ch25/26/77/80 handoff。provisional
  `Refine — Existing Argument / Experimental`；Historical Books Gate 关闭，不修改 Books。待核验 artifact、multi-seed、
  teacher quality/safety、experience deletion/supersession、catastrophic forgetting、cost 与更长 closed-loop stability。

### Remaining blocked families

| Candidate | First-public Date | Blocked Primary Source | Claims explicitly not verified |
| --- | --- | --- | --- |
| Agents' Last Exam | 2026-06-03 | arXiv:2606.05405 + GitHub project/code surface | task provenance、living revision、harness/backbone identity、grader、cost |
| SWE-Explore | 2026-06-05 | arXiv:2606.07297 | exploration trace、information gain、tool policy、leakage、success causality |
| Unembedding Matrix Feature Lens | 2026-06-05 | arXiv:2606.07502 | geometry、probe/intervention boundary、layer/model generality、causal evidence |
| Geometry of On-Policy Distillation | 2026-06-05 | arXiv:2606.07082 | divergence geometry、support mismatch、estimator stability、revision boundary |
| Retrospective Harness Optimization | 2026-06-04 | arXiv:2606.05922 | self-preference、harness state、offline bias、rollback、transfer |
| LatentSkill | 2026-06-04 | arXiv:2606.06087 | text-to-weight compilation、adapter/base identity、forgetting、held-out transfer |
| OpenSkill | 2026-06-04 | arXiv:2606.06741 | open-world discovery、validation、supersession、conflict、continual stability |
| When Tools Fail | 2026-06-04 | arXiv:2606.05806 | fault injection、observation/action contract、replanning、grader、environment realism |
| Graph Memory for LLM Agents | 2026-06-04 | arXiv:2606.06036 | reconstruction、graph ownership、retrieval、provenance、consolidation |
| Program-of-Layers | 2026-06-04 | arXiv:2606.06574 | layer composition、state/control、routing objective、runtime cost |
| SkillHarness | 2026-06-02 | arXiv:2606.20636 | skill provenance、safe execution、benchmark/revision history |

这些条目的 arXiv primary-paper domain，以及需要交叉核验的 GitHub artifact domain，均被当前保存的
访问策略拒绝；逐项重试不会形成阅读证据。表中第四列只声明不得推断的边界，不是论文结论。11 项 blocked
families 均不计 Full Source Review、不分配 Books owner、不修改 Books；原评分只保留为 provisional discovery
priority。按用户明确指示，forward cursor 进入 W24；待权限或 primary-source availability 改变后统一回补。

### Post-forward blocked retry — 2026-08-12

本检查点逐项重试 Continual Experience Internalization 与表中 11 项 blocked family 的精确 arXiv HTML，
并单独重试 StreamMA v1 PDF。13 个入口均未返回可验证的 primary text；StreamMA current v2 review
继续不能代替 v1 event snapshot，current repository 缺少 runnable implementation 的边界也没有改变。
Continual Experience Internalization 已于 2026-08-13 恢复并完成全文审计，因此 W23 更新为 22/33
current-version reviews + 11 blocked families，并保留 StreamMA v1/artifact sub-gap；
post-forward cursor 进入 W24，Historical Evidence Gate Open、Books Gate Closed。

## Repository Changes

- 2026-08-14 完成 33/33 final disposition 与 9-owner review；实际 refine Ch25、Ch30、Ch45、Ch48、
  Ch66、Ch75、Ch79，另外重验证 Ch33 与 Ch77 的现有机制。11 个 blocked family 与 StreamMA revision
  gap 均未进入 Books；下方旧“Books Closed / 未修改”只描述此前检查点。
- 2026-08-13 重新逐行复算为 33 scored（21 high、12 mid、0 low）：22/33 current-version Source
  Reviews、11 个 blocked families、0 ordinary pending；StreamMA v1/runnable artifact 仍单独作为 sub-family
  gap。fixed checkpoint 已通过，但 blocked 与 cross-index discovery 仍使 Historical Evidence Open、Books Closed。
- W23 从 5 个 baseline families 扩展为 33 个 scored families；完成 PEFT scaling 43 页 PDF、Cosmos 3
  139 页 technical report、Code2LoRA 完整 HTML、Harness-1 63 页 PDF、DRIFT/TELBench、KVarN 与
  AdaPlanBench、CHERRL、AutoLab 与 StreamMA v2 完整 primary text 的方法、实验、限制或限制缺口、关键附录、
  官方 artifact 及相邻章节审计；AutoLab 的 current v1.1 repository 与 2026-06-03 event node 已分离，结论为
  Ch62 `No Change — Already Covered`。StreamMA v1 正文和 runnable artifact 明确进入 blocked backlog，v2
  结果未倒写为 W23 事实，provisional owner 为 Ch78。SDPG 已完成 v1 全文、理论/实验 appendices、
  当前实现说明与 Ch25/27～30 邻接审计；provisional owner 为 Ch29，结论为
  `Refine — Existing Argument / Experimental`。M3Eval 已完成 v1 全文、四类 cognitive task construction、
  evaluation/appendices、current official artifact 与 Ch14/22/62/73 邻接审计；其任务仍混合 perception、
  position/recency、source binding 与 memory，且 frame/human/scorer contract 未闭合，故为 Ch62
  `No Change — Already Covered / Experimental Case`。Continual Experience Internalization 等 12 个尚未完成
  Full Source Review 的 families 因 primary text/author artifact domain 不可访问，逐项转入
  `Unverified / Blocked Backlog`，不从标题推断机制；current-review pending 从 23 降至 0，forward cursor 进入
  W24。fixed official/Infra 重扫新增 SGLang decoupled speculative roadmap、vLLM v0.22.1、Transformers
  LightGlue RCE advisory/fix 与 Datasets 5.0.0；四项均完成非模板化 Full Source Review，分别得到 Ch44
  provisional refine、Ch46/53 version fact 去重、Ch68 security case 去重和 Ch23/62 version fact 去重。
  W23 fixed official/Infra checkpoint 已通过，但 discovery/Historical Evidence Gates 仍保持 Open。HF 展示窗中
  15 个 W22 spillbacks 和 1 个 W21 spillback 已按 v1 回拨；W24～W26 display feed 的 11 个 W23
  families 已按 v1 回填。既有 Ch73 derived-memory 演进保留为
  provisional input，本轮未修改 Books。

## Open Questions

1. synthesis 后如何保留 source lineage，使用户能审计、纠错和删除派生 memory？
2. Claude chemist、cyber mapping、GPT-Rosalind 与 Agentic RAG 的 direct papers/artifacts 是否存在
   后续独立复核，能升级当前 domain/product evidence？
3. PEFT 的 policy revision 怎样在 base-model upgrade 时迁移，而不把 adapter shape compatibility 当
   behavioral compatibility？
4. 11 个 blocked candidates 的 primary text/artifact 可访问后，哪些能与 Ch14/24/26～30/44/55、Ch62、
   Ch71～78 形成稳定机制链？
5. Code2LoRA 的 generated adapter 如何处理 diff reorder、source deletion 与 base revision migration？
6. Harness-1 的各组件在重新训练 policy 后是否仍有相同增益，verifier/renderer drift 如何进入 revision identity？
7. DRIFT 的 first-error prediction 如何表达 uncertainty，并与 online trace sampling、retention 和人工复核预算联动？
8. KVarN 在真实 paged KV、prefix sharing、并发和 MLA/GQA workload 下是否仍保持相同误差与 overhead 边界？
9. Cosmos 3 的 shared action prior 能否在公开、跨 embodiment、long-horizon closed-loop 与 safety SLO 下复现，
   统一 token interface 又应如何与独立 controller certification 共存？
10. AdaPlanBench 的 cumulative constraint ledger 能否在可执行 environment、直接 user clarification 与独立
    verifier 下保持收益，并用 regression gate 避免局部修订破坏已满足约束？
11. CHERRL 的 judge-blind detector 能否在 composite/semantic bias、no-hack controls 与在线 budget 下校准
    false positives，并把 alert 可靠连接到 pause、rollback 和 reward revision？
12. AutoLab 是否能提供 immutable v1 task/evaluator snapshot、完整 per-trial trajectory/cost records 与污染审计；
    当公开 reference/solution 进入未来训练语料后，live leaderboard 应如何分离 memorization 与 empirical search？
13. StreamMA 的 v1 event snapshot、README 引用的 runnable implementation 与 immutable commit 是否能恢复；
    bounded queue、backpressure、completion/cancellation、multi-predecessor arrival order 和 matched Serial
    wall-clock 又会怎样改变 v2 的效果、延迟与成本结论？
14. SDPG 的 gate 与 beta schedule 各自贡献多少稳定性；错误 privileged context、full-logit memory、
    score-function omission 与跨 domain 扩展会怎样改变收益和 objective bias？
15. M3Eval 能否公开 immutable sample/scorer snapshot、annotator agreement 与 human protocol，并在 matched
    frame/decoding contract 下分别隔离 perception、position/recency、reasoning 与 retention？
16. Continual Experience Internalization 的 immutable author artifact 何时可用，以核验 deletion、
    supersession、multi-seed 与更长 cycle stability？
17. SGLang enumeration buffer 在真实 M:N、PP/多节点、drafter lag、cancellation 与 failure recovery 下，
    能否保持 exact output、bounded memory、fairness 与 workload/SLO contract？
18. vLLM Ray port allocation 能否用 reservation/lease primitive 同时避免 serialization visibility failure 与
    TOCTOU，NIXL wheel normalization 又能否取得直接 code evidence？
19. Transformers 的 native-integration lint 如何覆盖 dynamic kwargs/indirect wrappers，并与 runtime sandbox、
    artifact signing 和 dependency policy 形成可验证的 complete trust boundary？
20. Datasets Agent trace normalization 是否能无损保留 tool/environment/artifact/side-effect provenance，
    cross-shard shuffle 与 iterator resume 又如何绑定 immutable sampling revision？

## Sources

- OpenAI, “Introducing new capabilities to GPT-Rosalind,” published 2026-06-03:
  https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/
- OpenAI, “Dreaming: Better memory for a more helpful ChatGPT,” published 2026-06-04:
  https://openai.com/index/chatgpt-memory-dreaming/
- Anthropic Research index, entries dated 2026-06-03 and 2026-06-05:
  https://www.anthropic.com/research
- Google Research NLP archive, Agentic RAG entry dated 2026-06-05:
  https://research.google/blog/label/natural-language-processing/
- Hugging Face Papers, 2026-W23 discovery index: https://huggingface.co/papers/week/2026-W23
- On the Scaling of PEFT: https://arxiv.org/abs/2606.02437
- On the Scaling of PEFT PDF: https://arxiv.org/pdf/2606.02437
- Cosmos 3: https://arxiv.org/abs/2606.02800
- Cosmos 3 official project: https://research.nvidia.com/labs/cosmos-lab/cosmos3/
- Cosmos 3 NVIDIA technical blog, published 2026-05-31:
  https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/
- Cosmos 3 repository: https://github.com/NVIDIA/cosmos
- Code2LoRA: https://arxiv.org/abs/2606.06492
- Code2LoRA HTML full text: https://arxiv.org/html/2606.06492
- Harness-1: https://arxiv.org/abs/2606.02373
- Harness-1 PDF: https://arxiv.org/pdf/2606.02373
- Harness-1 code: https://github.com/pat-jj/harness-1
- Deep-research span-level error localization: https://arxiv.org/abs/2606.02060
- Deep-research span-level error localization HTML: https://arxiv.org/html/2606.02060v2
- KVarN: https://arxiv.org/abs/2606.03458
- KVarN HTML full text: https://arxiv.org/html/2606.03458v1
- KVarN code: https://github.com/huawei-csl/KVarN
- AdaPlanBench: https://arxiv.org/abs/2606.05622
- AdaPlanBench HTML full text: https://arxiv.org/html/2606.05622
- AdaPlanBench repository: https://github.com/JiayuJeff/AdaPlanBench
- AdaPlanBench official dataset: https://huggingface.co/datasets/JiayuJeff/AdaPlanBench
- Reward hacking in rubric-based RL: https://arxiv.org/abs/2606.04923
- Reward hacking in rubric-based RL HTML: https://arxiv.org/html/2606.04923v1
- CHERRL repository: https://github.com/THUAIS-Lab/CHERRL
- RHDA documentation: https://github.com/THUAIS-Lab/CHERRL/blob/main/detection/README.md
- AutoLab: https://arxiv.org/abs/2606.05080
- AutoLab HTML full text: https://arxiv.org/html/2606.05080v1
- AutoLab official project: https://autolab.moe/
- AutoLab repository: https://github.com/autolabhq/autolab
- AutoLab repository history: https://github.com/autolabhq/autolab/commits/main/
- AutoLab Flash Attention task contract:
  https://github.com/autolabhq/autolab/blob/main/tasks/flash_attention/task.toml
- Streaming Communication in Multi-Agent Reasoning metadata: https://arxiv.org/abs/2606.05158
- StreamMA v1 PDF（本轮访问失败，保留待核验）: https://arxiv.org/pdf/2606.05158v1
- StreamMA v2 PDF（本轮完整阅读）: https://arxiv.org/pdf/2606.05158v2
- StreamMA official project: https://zhenyangcs.github.io/StreamMA-website/
- StreamMA official repository（current public tree lacks referenced implementation）:
  https://github.com/EnVision-Research/StreamMA
- Self-Distilled Policy Gradient: https://arxiv.org/abs/2606.04036
- Self-Distilled Policy Gradient HTML full text: https://arxiv.org/html/2606.04036v1
- Self-Distilled Policy Gradient official project: https://lauyikfung.github.io/SDPG/
- Self-Distilled Policy Gradient official repository: https://github.com/lauyikfung/SDPG
- M3Eval: https://arxiv.org/abs/2606.05008
- SGLang parallel speculative decoding roadmap, opened 2026-06-06:
  https://github.com/sgl-project/sglang/issues/27462
- vLLM v0.22.1 release, published 2026-06-05:
  https://github.com/vllm-project/vllm/releases/tag/v0.22.1
- vLLM Ray data-parallel port ownership fix:
  https://github.com/vllm-project/vllm/pull/43864
- vLLM container dependency-source fix:
  https://github.com/vllm-project/vllm/pull/44366
- GitHub reviewed advisory GHSA-fgcw-684q-jj6r / CVE-2026-5241, published 2026-06-03:
  https://github.com/advisories/GHSA-fgcw-684q-jj6r
- Transformers LightGlue trust-boundary fix:
  https://github.com/huggingface/transformers/commit/676559d5022b74aaa0cee1cee0842b7f27c5320e
- Hugging Face Datasets 5.0.0 release, published 2026-06-05:
  https://github.com/huggingface/datasets/releases/tag/5.0.0
- M3Eval HTML full text: https://arxiv.org/html/2606.05008v1
- M3Eval official project: https://pku-value-lab.github.io/m3eval-homepage/
- M3Eval official repository: https://github.com/PKU-VaLuE-Lab/m3eval
- M3Eval official dataset: https://huggingface.co/datasets/PKU-VaLuE-Lab/m3eval
- Continual Experience Internalization: https://arxiv.org/abs/2606.04703
- Agents' Last Exam: https://arxiv.org/abs/2606.05405
- SWE-Explore: https://arxiv.org/abs/2606.07297
- Unembedding Matrix Feature Lens: https://arxiv.org/abs/2606.07502
- Geometry of On-Policy Distillation: https://arxiv.org/abs/2606.07082
- Retrospective Harness Optimization: https://arxiv.org/abs/2606.05922
- LatentSkill: https://arxiv.org/abs/2606.06087
- OpenSkill: https://arxiv.org/abs/2606.06741
- When Tools Fail: https://arxiv.org/abs/2606.05806
- Graph Memory for LLM Agents: https://arxiv.org/abs/2606.06036
- Program-of-Layers: https://arxiv.org/abs/2606.06574
- SkillHarness: https://arxiv.org/abs/2606.20636
- Language Models Need Sleep (2025 first-public cross-year family): https://arxiv.org/abs/2606.03979

## 2026-08-14 Final Source-Family Books Integration Ledger

最终计数为 33/33：10 Refine、7 No Change、4 Weekly Only、1 Emerging / Revision-sensitive、
11 Unverified / Blocked。Blocked-skip 只允许游标前进，不将缺失正文变成可写入 Books 的证据。

| Source Family | Final Disposition | Stable Owner | Current / Legacy | Books Review Result |
| --- | --- | --- | --- | --- |
| Dreaming memory synthesis | No Change | `AGENT-MEMORY` | Ch77 / Ch73 | derived view、provenance、supersession、review/delete/rebuild 已具体覆盖 |
| Claude chemist / NMR workflow | Weekly Only | — | — | Domain evidence；不外推真实 lab autonomy |
| Claude cyber-threat mapping | Weekly Only | — | — | Observational security report；不是完整 incident census |
| GPT-Rosalind capability update | Weekly Only | — | — | Product/version fact；内部 mechanism 未披露 |
| Google Agentic RAG | No Change | `AGENT-RAG` | Ch76 / Ch72 | iterative evidence acquisition、tool grounding 与 final verification 已覆盖 |
| On the Scaling of PEFT | No Change | `PLATFORM-MODEL-REGISTRY` | Ch59 / Ch55 | W20 MinT 已吸收 policy record/session/revision/residency 分层；population 不等于 residency |
| Cosmos 3 | Refine | `MULTIMODAL-WORLD-MODELS` | Ch25 / N/A | shared interface 与 separate reasoner/generator/action owners 并存 |
| Code2LoRA | Refine | `TRAIN-LORA` | Ch30 / Ch26 | repository/diff authority→derived representation/state→base-bound generated adapter |
| Harness-1 | Refine | `AGENT-CONTEXT` | Ch75 / Ch71 | semantic policy 与 recoverable harness bookkeeping 分 owner |
| DRIFT / TELBench | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | outcome→span-level first harmful commitment→propagation；诊断不是 root-cause truth |
| KVarN | Refine | `INFER-KV-CACHE` | Ch45 / Ch41 | static quantization→autoregressive read/produce/requantize feedback evaluation |
| AdaPlanBench | Refine | `AGENT-PLANNING` | Ch79 / Ch75 | cumulative constraint ledger 与 revision-wide regression Gate |
| CHERRL | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | privileged reward decomposition 与 judge-blind temporal monitor 分离 |
| AutoLab | No Change | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | executable artifact、long-horizon run、cost 与 live-benchmark contamination 已覆盖 |
| StreamMA v1/v2 | Emerging / No Books Change | — | — | v2 可读；v1 event snapshot 与 runnable implementation 缺失，不能倒写 W23 mechanism |
| Self-Distilled Policy Gradient | Refine | `TRAIN-GRPO` | Ch33 / Ch29 | privileged context 仅形成受控 gate/baseline，不取消 on-policy reward ownership |
| M3Eval | No Change | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | perception/position/source-binding/memory slices 与 scorer identity 已覆盖 |
| Continual Experience Internalization | Refine | `AGENT-MEMORY` | Ch77 / Ch73 | external episodes→principles→state-aligned injection→versioned parameter consolidation |
| Agents' Last Exam | Unverified / Blocked | — | — | Full text/artifact unavailable；No Books Change |
| SWE-Explore | Unverified / Blocked | — | — | Full text unavailable；不推断 exploration mechanism |
| Unembedding Matrix Feature Lens | Unverified / Blocked | — | — | Full text unavailable；不推断 causal feature geometry |
| Geometry of On-Policy Distillation | Unverified / Blocked | — | — | Full text unavailable；不推断 divergence/support mechanism |
| Retrospective Harness Optimization | Unverified / Blocked | — | — | Full text unavailable；不推断 offline harness update benefit |
| LatentSkill | Unverified / Blocked | — | — | Full text unavailable；不推断 text-to-weight compilation |
| OpenSkill | Unverified / Blocked | — | — | Full text unavailable；不推断 discovery/supersession stability |
| When Tools Fail | Unverified / Blocked | — | — | Full text unavailable；不推断 fault/replanning semantics |
| Graph Memory for LLM Agents | Unverified / Blocked | — | — | Full text unavailable；不推断 graph ownership/retrieval benefit |
| Program-of-Layers | Unverified / Blocked | — | — | Full text unavailable；不推断 layer routing/runtime cost |
| SkillHarness | Unverified / Blocked | — | — | Full text/artifact unavailable；不推断 Skill safety/benefit |
| SGLang parallel speculative roadmap | Refine | `INFER-SPECULATIVE-DECODING` | Ch48 / Ch44 | colocated implicit state→versioned future buffer→verifier-only commit/fallback |
| vLLM v0.22.1 | No Change | `INFER-VLLM` | Ch50 / Ch46 | patch-level endpoint ownership/serialization case；无新 architecture |
| Transformers LightGlue RCE | No Change | `PLATFORM-SECURITY` | Ch72 / Ch68 | nested config 是 remote-code boundary case；pin/sandbox/policy 已覆盖 |
| Hugging Face Datasets 5.0.0 | Weekly Only | — | — | Breaking version fact；trace-to-messages 不等于 lossless provenance |

### Owner Review

10 个 Refine decisions 分布在 9 个 Stable Node owners；其中正文实际新增 7 条演进机制，DRIFT、SDPG 与
Continual Experience Internalization 则逐项重验证现有 process diagnosis、on-policy control 与
external-to-parametric consolidation 论证，避免重复论文摘要。7 个 No Change 都能定位到现有具体段落。

Archive/Discovery Gate 仍因 11 个 blocked families、StreamMA v1/artifact 与 Scholar/OpenAlex/DBLP
cross-index 保持 Open；W23 Source-Family Books Gate 已按 blocked-skip 完成，游标进入 W24。
