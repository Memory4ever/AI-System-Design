# AI Research Weekly — 2026-W17

> Coverage Window: 2026-04-20～2026-04-26
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-09；Gate Closed: 2026-08-10
> Re-audit Status: 22/22 scored families reviewed and dispositioned; 19/19 `20+` Full Source Reviews complete; 3/3 low-score boundaries verified; Discovery and Candidate Evidence Gates Passed; Source-Family Books Gate Complete; Archive Completion Gate Open

## Executive Summary

旧版 W17 的三行评分实际至少包含五个 Source Families，且 ReasoningBank 的论文 first-public
date 属于 2025，2026-04-21 只是 Google Research 的传播/项目节点。baseline 仍保留：Google
ReasoningBank 把 Agent experience 组织为可复用 memory；OpenAI Privacy Filter 提供
open-weight PII detection/redaction；GPT-5.5 与 Seed3D 2.0 则是 model-family 和垂直生成
更新。恢复扫描先找到 11 个本周候选，并把 6 个 first-public date 属于 W16 的项目回拨；继续
检查后续 curation feed 又按 v1 日期补回 5 个 W17 families。现已完成 ClawEnvKit、Agent-World、
OpenGame、Computer Use Reliability 与 River-LLM 的全文审计：前两项共同说明 executable
environment 既是训练数据也是有状态系统；OpenGame 把稳定 scaffold、渐进式读取和可执行修复组织成
长期 workflow；reliability study 说明单次成功率不能替代重复运行稳定性；River-LLM 则把 early exit
重新表述为 KV 完整性问题。第二批又完成 AJ-Bench、AI-scientist epistemic study、Chat2Workflow
和 SkillLearnBench：judge 需要主动取证但不能成为 truth owner；结构合法的 workflow 不等于执行成功；
没有外部新证据的 self-refine 可能递归漂移；科学任务的 outcome 还需绑定 evidence uptake、hypothesis
testing 与 belief revision。第三批完成 COSPLAY、VLAA-GUI、OMC 与 ClawMark：可复用 skill 需要
contract 与 retirement，GUI recovery 需要预算感知的 verifier，Multi-Agent 组织层需要 typed state
transition，而 living-world evaluation 必须把外生变化写入 run identity。最后三项也已完成：HiLight
把 instance-level evidence selection 与 frozen Solver 解耦；Agentic World Modeling 只作为能力分类与
evaluation boundary；Last Harness 仍是无实证的 conceptual protocol。fixed-list 重扫又恢复 KServe
v0.18.0 RC family：它把 LLMInferenceService 的 scaling desired state 映射为 WVA 加 HPA/KEDA，
同时暴露 missing-CRD、actuator ownership 与 stale-resource cleanup 边界。记录内 19/19 `20+` 已审计；
31 个具名 topical hits 已对账为 22 个 scored families、8 个跨周归档和 1 个低门槛 patch release，
W17 Discovery 与 Candidate Evidence Gates 通过。
另有 Stochastic KV Routing 的 v1 实际为 4 月 3 日，已回拨
W14；TCOD 的 v1 为 4 月 27 日，将归 W18，均不在 W17 重复计分。

## Coverage and Source Coverage

- 模型与研究机构：保留 Google 4 月 21 日、OpenAI 4 月 22/23 日、Seed 4 月 23 日和
  Anthropic 4 月 24 日条目；fixed institution Research/Blog/model-card index 已闭合，未恢复额外
  达到 20 分的 in-window family。
- 论文与学术来源：ReasoningBank 按作者实验；Privacy Filter 按官方 model/research release；
  2026-04-20～04-26 的 arXiv/Hugging Face discovery 已完成扩大召回，恢复 16 个 in-window
  families，并识别 6 个 W16 spillbacks、1 个 W14 spillback 和 1 个 W18 event。OpenReview/
  TMLR、DBLP、Scholar/OpenAlex 交叉检验未恢复新的 20 分候选；索引日期未替代 arXiv v1 日期。
- AI Infra：fixed release/RFC/PR list 恢复 KServe v0.18.0-rc0/rc1 为一个 family；Ray 2.55.1 仅修复
  `ray-llm` image SSH connectivity 和 slim base packages，低于 retention threshold。其余被扫项目在
  04-20～04-26 无达到 20 分的具名 release family。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ReasoningBank Google Research publication node | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Cross-year paper family; Full Review Complete |
| OpenAI Privacy Filter | 3 | 4 | 5 | 5 | 4 | 4 | 25/30 | Full Review Complete |
| ClawEnvKit | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read — full review complete |
| Agent-World | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full Review Complete — provisional Refine |
| OpenGame | 4 | 4 | 5 | 4 | 5 | 3 | 25/30 | Full Review Complete — provisional Refine |
| Reliability of Computer Use Agents | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Full Review Complete — provisional Integrate |
| River-LLM | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Full Review Complete — Experimental |
| Chat2Workflow | 4 | 4 | 5 | 4 | 5 | 3 | 25/30 | Full Review Complete — No Change |
| AJ-Bench | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Review Complete — provisional Refine |
| SkillLearnBench | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Review Complete — provisional Refine |
| AI scientists produce results without reasoning scientifically | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Full Review Complete — provisional Integrate |
| COSPLAY: Co-Evolving Decision and Skill Bank Agents | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Review Complete — provisional Refine |
| VLAA-GUI | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Full Review Complete — provisional Refine |
| From Skills to Talent: OMC | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Review Complete — provisional Refine |
| ClawMark | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Full Review Complete — provisional Refine |
| KServe v0.18.0-rc0 / rc1 | 3 | 4 | 4 | 5 | 4 | 2 | 22/30 | Full Review Complete — Weekly Only / Pre-release |
| Agentic World Modeling | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Review Complete — No Change |
| Learning Evidence Highlighting for Frozen LLMs | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Review Complete — provisional Refine |
| The Last Harness You'll Ever Build | 4 | 4 | 4 | 3 | 4 | 3 | 22/30 | Full Review Complete — Experimental / Conceptual |
| GPT-5.5 release | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Record Only |
| Seed3D 2.0 | 3 | 3 | 3 | 4 | 2 | 3 | 18/30 | Record Only |
| Project Deal | 2 | 2 | 3 | 4 | 3 | 3 | 17/30 | Record Only |

本轮账目为 22 行：15 个 `25～30`、4 个 `20～24`、3 个 `<20`。评分只决定阅读优先级，
不等于 Books disposition。

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Baseline score rows / source families | 5 / 5 | 2 项 `20+` reviews；3 项低分 version/research facts |
| Recovered in-window academic families | 16 | 16 项 Full Source Review complete |
| Recovered in-window infra families | 1 | KServe RC family；Full Source Review complete |
| W16 spillbacks | 6 | 按 arXiv v1 回拨，不在 W17 重复计分 |
| Other-week attribution | 2 | Stochastic KV Routing 回拨 W14；TCOD 归 W18 |
| Below-retention screened | 1 | Ray 2.55.1 patch release；不进入 Candidate Scoring |
| Total topical hits screened | 31 | 22 scored + 8 cross-week + 1 below-retention |
| Total score rows | 22 | 15 high / 4 mid / 3 low；六维合计已复算 |
| Cross-year deduplication | 1 | ReasoningBank paper first-public 2025；W17 只保留 Google publication node |
| Academic discovery window | Closed | arXiv/HF recall + OpenReview/TMLR/DBLP/Scholar/OpenAlex cross-check |
| Official / Infra discovery window | Closed | fixed institution + release/RFC/PR lists；KServe recovered，Ray patch rejected |
| W17 Evidence Gate | Passed | 19/19 `20+` reviews complete；31-hit disposition reconciled |

## Deep Analysis — Experience Memory 必须带 Validity Contract

Agent 从过去 trajectory 提取经验，可以减少重复探索；但错误经验、环境变化与工具版本漂移
会把“记忆”变成持久化故障。ReasoningBank 的长期意义是把 experience reuse 显式化，不能
据单篇研究断言某种 memory representation 已经通用。演进关系为：

```text
raw trajectory retention
→ summarized experience
→ retrieved reasoning memory
→ 需要 provenance、version、confidence、expiry 与 feedback correction
```

Privacy Filter 位于输入/输出治理层，与 memory 是 `Layering / Dependency`：过滤器降低 PII
暴露风险，但也会产生 false positive、false negative 与语义损失。

## Deep Analysis — Environment Automation 把 Benchmark 变成有状态系统

静态 benchmark 对固定输入输出、低成本回归和长期可比仍然合理；当 Agent 要调用工具、修改环境、
恢复失败并产生副作用时，只保存 prompt 与 final answer 已不足以说明发生了什么。ClawEnvKit 把
environment 显式写成 `E=(P,M,C)`：`P` 是任务规范，`M` 是 tools 与 server-side audit，`C` 是
对 trajectory、audit、文件和输出的评分函数；parser、generator、validator 再从自然语言产生并
检查这一 contract。演进关系是：

```text
fixed text benchmark
→ hand-authored executable sandbox
→ parameterized task/service/scorer templates
→ on-demand generated and validated environments
```

它获得 coverage、refresh 与 failure injection，却把新的状态和偏差带进 evaluator：generator 与
judge 可能共源，validator 只能执行已编码的不变量，mock service 缺少真实 authentication、schema
drift 和外部状态；unseeded errors 与 provider routing 也削弱可重复性。因此 live evaluation 不能
覆盖 frozen benchmark，自动生成的 environment 必须版本化，并与独立 held-out、人工审计和真实
shadow evidence 并存。

## Evidence Level

ReasoningBank 与 ClawEnvKit 为作者实验；Privacy Filter 是官方发布，模型效果仍绑定数据和
threat model。ClawEnvKit 的 harness/model 数字只对其 mock services、scorer、v4 model roster、
Apple M-series Docker setup、timeout 与 OpenRouter routing 成立。
其余论文结论只在各自公开的 model、environment、verifier 与 evaluation contract 内成立；Agentic
World Modeling 与 Last Harness 分别是 taxonomy/survey 和 conceptual protocol，不提供新的因果实证。
KServe RC 只证明 pre-release API、controller 与 resource ownership 行为，不代表 stable release 或
production workload/SLO 结果。

## Cross-Week Deduplication

与 6 月 Dreaming memory 的关系是不同层的 `Principle Reuse`：前者偏 agent experience，
后者偏用户长期 memory synthesis。W17 feed 中 SkillFlow、EvoMaster、AgentSPEX、OpenMobile、
Scaling Test-Time Compute 与 BEHEMOTH 的 v1 日期均落在 W16，已回拨而不重复计分；Stochastic
KV Routing 回拨 W14，TCOD 归 W18。ReasoningBank 论文仍归 2025，W17 只记录 Google Research
publication node。

## Knowledge Tree Position

Ch23 Data → Ch29 Post-training → Ch40/44/52 Inference → Ch57 Serving Platform →
Ch62 Evaluation → Ch68 Security → Ch71 Context → Ch73/75 Memory and Planning →
Ch76 Reflection → Ch77 Workflow → Ch78 Multi-Agent → Ch80 Agent Platform。

## Recommended Action

W17 的 13 个稳定机制已按 owner 进入既有章节，4 个 No Change families 已完成章节级去重，KServe RC 与
三个低分事实保持 Weekly Only，Last Harness 保持 Emerging/Conceptual。ClawEnvKit 只补足 on-demand
environment generation 的 validator/revision/mock-real boundary，不复制作者 benchmark；River-LLM 只沉淀
early-exit KV completeness，不写 speedup 常数。Source-Family Books Gate 已完成，游标进入 W18。

## Event-Date Daily Decision

2026-04-20～04-26：Historical Weekly only；不补造 Daily。

## Provisional Books Integration Decision — Superseded 2026-08-14

`Blocked — Not Started`。ReasoningBank 与 Dreaming 所形成的 episode → strategy
extraction → consolidation 演进由 Ch73 拥有；本轮补明 derived strategy 不能凭历史 success
直接改写 approval、retry、budget 或 side-effect semantics。Privacy Filter 对 policy taxonomy、
operating point、distribution shift 与 human escalation 的边界已由 Ch68 完整覆盖，不重复追加。
ClawEnvKit 暂定 Ch62 refine；Agent-World 暂定 Ch29 refine，OpenGame 暂定 Ch77 refine，Computer
Use Reliability 与 AI-scientist epistemic evaluation 暂定 Ch62 new mechanism，AJ-Bench 暂定 Ch62
refine，SkillLearnBench 暂定 Ch80 refine；Chat2Workflow 属 Ch77 已覆盖，River-LLM 保持
Experimental；COSPLAY、VLAA-GUI、OMC、ClawMark 与 HiLight 已形成 provisional refine，Agentic
World Modeling 已由 Ch75/Ch62 覆盖，Last Harness 保持 Experimental/Conceptual。既有 Books 内容
保留待复核；KServe RC family 仅是 pre-release/version fact，不触发 Books 修改。
W17 候选池与 recorded reviews 已闭合；只有全历史 Evidence Gate 通过后才进入 Books Integration。
此段保留为审计历史，最终决定见文末 `Final Books Integration Ledger`。

## Ignored Noise

将 memory benchmark 提升为通用长期可靠性，或把 PII filter 当成完整 privacy solution。

## 2026-07-31 Full Re-Audit Addendum

- ReasoningBank 论文与 appendix 已全文复核；成功/失败轨迹蒸馏、memory-aware exploration、
  judge noise、retrieval 与 consolidation 边界已写入 Ch73。
- Privacy Filter model card 已全文复核；它是 policy-bound data-minimization sensor，不是
  anonymization/compliance guarantee，已写入 Ch68。
- 两项作者 benchmark 均保留其 dataset、judge、taxonomy 和 operating-point 条件。

## Full Source Review

### Agent-World — 27/30

- **Candidate / Week / Source Family**：`AGENT-WORLD-ENVIRONMENT-RL`；W17；arXiv:2604.18292，
  v1 2026-04-20，唯一公开版本，Comments 标为 `Working in progress`。论文 HTML 首页出现的
  7 月日期与 arXiv submission history 不一致，归周以 arXiv v1 时间为准。
- **Direct / Related Primary Sources**：arXiv abstract、v1 HTML/PDF 与作者 project page；project
  page 重述论文并展示 demo，不是独立复现实验。公开入口未提供可核验的训练代码、dataset snapshot
  或完整 environment artifact，因此 `19K+ tools` 等规模由作者材料单源支持。
- **Access / Full-read Coverage**：已读 metadata、Introduction、POMDP formalization、environment /
  database / tool discovery、graph/programmatic task synthesis、multi-environment GRPO、diagnosis/
  targeted curriculum、23-benchmark setup/results、environment-scaling 与 two-round evolution analysis、
  conclusion 和 project page；论文没有独立 Limitations、完整 ablation 或 hardware/cost section。
- **Original Problem / Why Previous Design Was Reasonable**：固定、手写 tool environments 有明确
  schema、oracle 和版本，适合可重复训练与回归；但 stateful multi-tool workload 的组合数、数据状态和
  difficulty 漂移，使手工扩展速度跟不上 Agent policy 与工具生态变化。
- **Changed Constraint / Mechanism**：系统从 MCP specification、tool docs 与 industrial PRD 收集
  environment themes，以 deep-research agent 挖掘数据库，再由 tool-design agent 生成接口和 unit tests；
  仅保留可编译、测试 accuracy `>0.5` 且非空的 environment。Graph route 用 weighted dependency
  random walk 形成 tool chain、ground truth 与 rubrics，并要求 ReAct 五次中至少两次得到一致答案；
  programmatic route 生成带 loop/branch/aggregation 的 executable solution。训练后在 held-out arena
  生成新任务，diagnosis agent 根据 failure trace 定位 weak environments，再 complexify database、
  合成 targeted tasks 并继续 GRPO，构成 policy/environment co-evolution。
- **State Ownership / Control Flow / Data Flow**：database 拥有外部 mutable state；tool runtime 执行
  read/write 并产生 observation；dialogue history 只记录可见交互；task generator 拥有 candidate task；
  rubric/code verifier 产生 reward；diagnosis agent 只派生 weakness/guideline；trainer 才拥有 checkpoint
  transition。正确链路是 `source themes → database/tools/tests → task + oracle → isolated rollout →
  trace/reward → weakness diagnosis → targeted curriculum → versioned policy`，diagnosis 不能反向改写
  原始 run evidence。
- **Implementation / Evaluation Contract**：作者报告 1,978 environments、19,822 tools，使用
  Qwen3-8B/14B backbone 与 GRPO，并在 23 个 tool-use、assistant、reasoning、search/coding 和 knowledge
  benchmarks 上评估。two-round arena experiment 在 MCP-Mark/BFCL-V4/τ²-Bench 上同时测试
  Agent-World-14B 与 EnvScaler-8B。公开文本未披露训练 GPU、batch、token budget、rollout 并发、
  wall-clock、cost、全部 reward/judge calibration 或 contamination audit，不能形成生产训练 contract。
- **What the Evidence Proves / Does Not Prove**：作者实验支持“多样 environment + targeted second-round
  curriculum”在指定 backbones、verifiers 和 benchmarks 上关联到增益，并显示同一 loop 对 EnvScaler
  初始化也有改善；它没有隔离 web-mined database、tool synthesis、GRPO 与 diagnosis 各自贡献，不能
  证明 self-evolution 无污染、自动 diagnosis 因果正确，或规模指标本身带来 general intelligence。
- **Trade-offs / New Failure Modes / Previous Design**：动态 curriculum 获得 coverage 与针对性，却
  引入 web-data provenance、generated oracle error、generator/verifier 共源、diagnosis feedback loop、
  benchmark overlap、environment revision 与 reward hacking。固定人工 environment 在监管、高风险
  side effects、独立 oracle 和长期可比场景仍更合理；两者应以 frozen core + evolving arena 共存。
- **Evolution / ROADMAP / Chapters**：相对静态 tool RL 是 `Direct Evolution`，相对 ClawEnvKit 的
  on-demand evaluation 是 `Layering / Dependency`。主 owner 暂定 Ch29，已读 Ch29 的 verifiable
  reward、measurement identity 与 rollout lifecycle，并联读 Ch23、Ch62、Ch77、Ch80；现有正文已覆盖
  reward environment 也是 specification，真正缺口是 failure evidence 如何在不污染 held-out evidence
  的前提下成为 versioned targeted curriculum。
- **Decision / Files / Questions**：provisional `Refine — Existing Argument`；Historical Books Gate
  关闭，只更新 W17。待验证公开 artifact、训练资源、task split/contamination、diagnosis calibration，
  以及同一 failure family 何时应升级 environment、何时应修正 policy。

### OpenGame — 25/30

- **Candidate / Week / Source Family**：`OPENGAME-GAME-SKILL-WORKFLOW`；W17；arXiv:2604.18394，
  v1 2026-04-20，唯一版本。作者 repository 已公开，但当前仓库内容与论文宣称的复现边界并未在
  arXiv v1 中给出 commit/tag 锁定，不能把 today 的 repository state 倒写为 event-date artifact。
- **Access / Full-read Coverage**：已读 metadata、Related Work、CPT/SFT/RL pipeline、six-phase agent
  workflow、Template/Debug Skill、execution algorithm、150-task benchmark、baselines、三组 ablation、
  qualitative genre analysis、Conclusion、system/tool prompts 与 repository tree/README。
- **Original Problem / Previous Design / Changed Constraint**：直接从 prompt 一次生成代码，对单文件和
  短任务简单有效；完整交互式项目却同时要求跨文件 lifecycle、physics、assets、build 与 runtime state。
  Long context 不能自动保证 salience，通用 repair loop 也缺少 domain invariants，因此系统改用 archetype
  scaffold、typed extension points、分阶段 context 和 executable repair。
- **Mechanism / Ownership / Flow**：Physics-first classifier 选择 template family；runtime 复制 core、
  modules 与 docs，GDD 生成器把需求转换为 file-level todos；asset protocol 约束 multimodal artifacts；
  code 只在 hooks/extension points 内实现；build/headless execution 驱动 diagnosis/repair。Template Skill
  owner 管理可复用 skeleton library，Debug Skill owner 保存经验证的 `(signature,cause,fix)`，workflow
  拥有 todo/phase/run state，generated game artifact 保留独立 identity。CPT→synthetic SFT→unit-test RL
  提供 backbone domain prior，但不拥有 workflow correctness。
- **Implementation / Evaluation Contract**：OpenGame-Bench 含 150 个五类 Phaser 3 prompts，测量 Build
  Health、Visual Usability、Intent Alignment；动态执行与 VLM judging 补充 static checks。作者用相同
  Claude Sonnet 4.6 backend 做 workflow ablation：移除 hook-driven implementation、three-layer reading
  或 physics-first routing 都降低三个指标；training ablation 在同一 OpenGame scaffold 中逐步加入
  CPT/SFT/RL；skill ablation 比较 static skeleton、partial/full library 与 debug protocol。公开论文未披露
  training GPU、tokens、sampling variance、judge calibration、per-task confidence interval 或生产 SLO。
- **Evidence Boundary**：ablation 支持“结构约束、渐进读取、可执行修复”在作者 Phaser benchmark 与
  chosen backends 下贡献明显，也显示 headline gain 大部分来自 workflow 而非仅 backbone training；
  但没有证明 template family 可跨 engine/domain 通用，living protocol 不会累积错误，或 VLM score
  等同可玩性。约 34.9% weighted mechanics 仍部分/完全未满足，是明确残余边界。
- **Trade-offs / Failure Modes / Previous Design**：stable scaffold 降低 wiring error，却限制 novel
  architecture；three-layer reading 降 context noise，也可能遗漏跨层依赖；living fixes 提高复用，却需要
  provenance、scope、supersession 和 rollback。一次性生成在微型 prototype、需求窄且人工即时 review
  时仍合理；人工架构在安全、性能或不可逆发布上继续作为 authority。
- **Evolution / ROADMAP / Chapters**：这是从 free-form generation 到 constrained workflow 的
  `Direct Evolution`，相对 Ch80 skill registry 是 `Layering / Dependency`。主 owner 暂定 Ch77；已读
  Ch77 的 deterministic spine、task IR、evaluator-driven search、replay 与 compensation，并联读 Ch62、
  Ch73、Ch80。缺口不在列出六阶段，而在说明 reusable scaffold/fix 必须是带 applicability、evidence、
  version 和 rollback 的 workflow artifact。
- **Decision / Files / Questions**：provisional `Refine — Existing Argument`；只更新 W17。待核验 repository
  event-date tag、VLM judge/human agreement、failure protocol 的 admission/supersession 和跨 engine transfer。

### On the Reliability of Computer Use Agents — 26/30

- **Candidate / Week / Source Family**：`CUA-REPEATED-RUN-RELIABILITY`；W17；arXiv:2604.17849，
  v1 2026-04-20，唯一版本，33 页。
- **Access / Full-read Coverage**：已读 metadata、POMDP/metric formulation、model/OSWorld setup、
  stochastic decoding、fixed-plan 与 cosmetic environment perturbation、instruction clarification、user
  simulator retry、plan extraction/refinement、paired statistics、related work/conclusion，以及 Appendix
  的 prompts、evaluator-code context、human-correction examples 和 perturbation details。
- **Original Problem / Previous Design / Changed Constraint**：single-run pass rate、mean across runs 与
  Pass@k 适合衡量“至少能否成功一次”；生产 computer use 还要求同一 task 多次执行不随机失败，且
  instruction、evaluator 与 environment 的轻微差异会改变 trajectory。评估对象从 capability snapshot
  变成重复执行下的 outcome distribution。
- **Mechanism / Ownership / Flow**：对每 task 做三次 run，使用 `Pass^3` 表示三次都成功，并以
  McNemar paired transition 检查同一 task 在 intervention 前后从 unreliable→reliable 与反向变化；
  Wilcoxon 检查 per-task success count。Benchmark owner 拥有 instruction/evaluator/environment version，
  workflow 产生 action trajectory，outcome verifier 给 ground-truth success，analysis layer 才派生
  reliability transition。Clarification 使用 evaluator context 生成但需人工纠错；user simulator 仅在
  failed retry 后给 mismatch feedback；plan refinement 从历史 success/failure 提取指导。
- **Evaluation Contract**：OSWorld 上比较 GPT-5、Claude Sonnet 4.6、Kimi 2.5 及若干 open models，
  使用 provider-required temperature 或 0.7；controlled study 还测试 temperature 0、batch-invariant
  inference、fixed plan 与 cosmetic perturbations。三次重复只估计短期 consistency，模型、harness、
  OS image、task/evaluator version 和 retry policy 都是 run identity；论文没有生产 side-effect、长期
  drift、成本或更大 `k` 的置信区间 contract。
- **What the Evidence Proves / Does Not Prove**：作者实验表明降低 sampling randomness 并不自动保证
  outcome reliability；clarification 通常改善 Pass^1/Pass^3，但将 evaluator information 注入 instruction
  会有 leakage/trivialization 风险；从历史轨迹提炼 plan 的作用随模型不同，Claude 甚至出现中间轮次
  regression。它没有证明固定策略普遍优于探索、LLM user simulator 等同真实用户，或三次成功足以
  满足高风险 deployment reliability。
- **Trade-offs / Failure Modes / Previous Design**：重复执行暴露 variance，却线性增加环境成本；更明确
  instruction 减少歧义，也可能把 benchmark oracle 泄漏给 agent；stable plan 降低 behavior variance，
  也会固化错误并失去适应性。Pass@k 仍适合 search/candidate generation；Pass^k 适合 reliability claim，
  二者回答不同问题而非彼此替代。
- **Evolution / ROADMAP / Chapters**：相对 single-run/Pass@k 是 `Direct Evolution`，相对 trajectory
  judge 是 `Layering / Dependency`。主 owner 暂定 Ch62；已读 Ch62 的 evaluation object、uncertainty、
  trajectory evidence、run identity 与 release gate，并联读 Ch64、Ch77、Ch80。现有章节已写“均值不是
  可靠性”，但缺少 repeated-run conjunction、paired transition 和 instruction/evaluator ambiguity 的
  可执行区分。
- **Decision / Files / Questions**：provisional `Integrate — New Mechanism`；Books Gate 关闭，只更新
  W17。待确定 production 中 `k`、retry budget、side-effect reset、user clarification 与 evaluator leakage
  如何共同进入 EvalRun identity。

### River-LLM — 26/30

- **Candidate / Week / Source Family**：`RIVER-LLM-KV-SHARED-EARLY-EXIT`；W17；arXiv:2604.18396，
  v1 2026-04-20，v2 05-06，v3 05-25；历史事件归 v1，当前全文采用 v3 核验并明确 revision drift。
- **Access / Full-read Coverage**：已读 metadata/revisions、Related Work、sequence/token exit、KV Cache
  Absence、recompute/state propagation/mask/mono-decreasing alternatives、KV-shared exit layer、phase-aware
  inference、accuracy/throughput/memory/latency evaluation、quantization comparison、limitations/conclusion。
  arXiv 未链接作者代码；artifact reproducibility 未验证。
- **Original Problem / Previous Design / Changed Constraint**：sequence-level fixed depth 保持所有历史
  token 在各层的 KV 一致，kernel 友好但无法让每个 token 按难度选择深度；token-level exit 理论上更
  灵活，却使 skipped layers 缺少该 token 的 K/V。Mask 保持低计算但损害上下文，recompute 保真却
  抵消速度，state propagation 近似补齐，mono-decreasing exit 则牺牲后续 token 的自由度。
- **Mechanism / State / Flow**：每个 backbone block 旁串联 lightweight quantized exit layer；token
  在某层退出后沿 Exit River 继续流过后续旁路层，因此这些层同时生成预测输出和所有 skipped depth
  需要的 K/V。exit controller 使用 backbone block input/output cosine similarity 作为累计 value-error
  proxy，并以 batch 内最小 similarity 与阈值 `τ` 决定退出。Prefill 采用 sequence-level exit 保持并行
  kernel，Decode 才使用 token-level exit。KV store 仍拥有完整 layer/token identity，controller 只决定
  compute path，scheduler 需记录 phase、threshold、batch coupling 与实际 exit depth。
- **Evaluation Contract**：作者在 Llama3.2-1B、Llama3.1-8B、Ministral3-8B 上以 BoolQ、HellaSwag、
  ARC、MMLU、GSM8K、MATH、HumanEval 等测试 accuracy/exit depth；wall-clock throughput 在单张
  NVIDIA A40 上报告，generation 表格含 tokens/s，memory test 覆盖 4K～64K、batch size 1。结果没有
  披露完整 prompt/output lengths、并发、TTFT/TPOT、kernel/version、功耗或 production SLO，且最大
  模型仅 8B。作者比较 HQQ full quantization 和几种 KV recovery/exit 策略，但缺少 production engine
  integration 与多租户调度实验。
- **Evidence Boundary / Trade-offs**：结果支持作者实现下 KV integrity 是 early-exit wall-clock 收益的
  关键约束，并在指定模型/任务/A40 上给出约 1.53～2.16× generation speedup；它不证明 24B/70B、
  tensor parallel、continuous batching、长 prefill 或通用 serving SLO 下仍成立。“near-lossless”也不能
  脱离每个 benchmark accuracy delta 使用。Exit River 新增参数/memory、threshold calibration、batch
  最小值耦合与路径分歧；早退 token 仍可能累积语义误差。
- **Evolution / ROADMAP / Chapters**：相对 KV recompute/mask/state propagation 是 `Direct Evolution`；
  与 quantization 是可组合但不同的 design branch。主 owner 暂定 Ch41，已读 Ch41 与相邻 Ch39/40、
  Ch42/44，并联读 Ch50/52；现有 KV 章节强调 cache 是 per-layer historical state，正好解释为什么
  arbitrary token exit 不能只按 FLOPs 估算。下一阶段压力是 engine kernel、batch scheduler、KV layout、
  threshold calibration 与 tail-SLO 的联合验证。
- **Decision / Files / Questions**：`Emerging / Experimental`；不在 Historical Books Gate 前写 Books，
  之后也只有 production engine evidence 或可复现 artifact 足够时才考虑 Ch41 refine。

### AJ-Bench — 25/30

- **Candidate / Week / Source Family**：`AJ-BENCH-ENVIRONMENT-AWARE-JUDGE`；W17；
  arXiv:2604.18240，v1 2026-04-20，ACL 2026 Findings；论文、project page 与公开 code/data
  入口已核对，唯一论文版本。
- **Full-read Coverage**：已读 benchmark construction、Search/DS/GUI trajectory collection 与人工
  labeling、environment construction、models/implementation、main results、reasoning/turn/modality
  ablations、confidence intervals、failure taxonomy、limitations，以及 Appendix 的 prompts、human
  annotation、framework/model ablation 和 false-positive/false-negative metrics。
- **Problem / Previous Design / Changed Constraint**：rule verifier 在 schema、database state 和已知
  invariant 上透明可靠；LLM judge 可读开放文本，却只能利用已提供的 trajectory。开放 search、GUI 和
  data-system task 常需查询外部事实、重放状态或检查关键 action，judge 因而从 passive scorer 演进为
  有 budget 的 evidence-acquisition policy。
- **Mechanism / Ownership / Flow**：task-solving trajectory 是待审 claim；judge agent 通过 search、
  filesystem/Postgres、GUI screenshot/accessibility tools 收集 evidence，再输出 binary verdict。Environment
  与 task-specific verifier/human label 拥有 outcome truth；judge 只拥有 evidence-selection 和 verdict，
  不能用自己的行动覆盖被评 trajectory。正确链路是 `frozen task/trajectory → judge tool plan →
  timestamped observations → evidence-backed verdict → compare with human/verifier label`。
- **Evaluation Contract**：155 tasks、516 balanced annotated trajectories，覆盖 Search、Filesystem/
  Postgres 和 PPT/Word/Excel；同 base model 比较 agentic/non-agentic judge，三次独立运行报告 F1 与 95%
  CI。Agent judge 只用 gpt-5-mini-low 与 deepseek-v3.2，interaction-budget 与 modality ablation 显示更多
  turns 往往有益，但 high reasoning effort 并不稳定更好。Search page 由同一模型 summarise，external
  network 会漂移；论文未给 production latency/cost/SLO 或高风险 error budget。
- **Evidence Boundary / Failure Modes**：作者数据支持 tool/environment access 在该 suite 上提高平均 F1，
  但总体约 0.72 F1 仍不适合直接作为 release oracle。失败包括不调用/漏调用工具、选错工具、误读输出、
  即使证据正确仍推理错误；multimodal input 还可能增加 noise。任务多由既有 benchmark 修改，Search
  environment 非冻结，因此不能外推所有 domain、模型或长期稳定性。
- **Trade-offs / Old Branch / Evolution**：active judging 提高 evidence access，也增加 calls、credentials、
  side effects、network drift 和 judge/tool attack surface。Exact verifier 在可形式化场景仍优先；人工专家在
  高风险、开放语义和争议 adjudication 中仍是 authority。相对 LLM-as-a-Judge 是 `Direct Evolution`，
  相对 executable verifier 是互补 `Layering / Dependency`。
- **ROADMAP / Decision**：主 owner 暂定 Ch62，已读 Ch62 的 scorer、trajectory evidence、claim-level
  provenance、EvalRun identity，并联读 Ch64、Ch77、Ch80。现有正文已要求 tool/result evidence，缺口是
  judge 作为 bounded evidence-acquisition policy 时的 budget、observation provenance 与 no-side-effect
  contract。provisional `Refine — Existing Argument`；Books Gate 关闭，只更新 W17。

### AI scientists produce results without reasoning scientifically — 26/30

- **Candidate / Week / Source Family**：`CORRAL-EPISTEMIC-AGENT-EVALUATION`；W17；
  arXiv:2604.18805，v1 2026-04-20，PDF 109 页；作者 Corral code 与 manuscript-matched Zenodo DOI
  已公开。PDF title page 标 4 月 22 日，但 historical event 仍按 arXiv v1 归周。
- **Full-read Coverage**：已读 Introduction、八类 scientific environments、model/scaffold attribution、
  diagnostic IRT/latent model、manual/LLM trace annotation、epistemic graph taxonomy、trace intervention、
  reliability experiment、Methods、25-trace agreement audit、domain/tool appendices、Scope and Limitations，
  并核对 code/archival artifact 入口。
- **Problem / Previous Design / Changed Constraint**：outcome score 对 procedure-fixed workflow 足以回答
  是否完成，却不能说明开放科学结论如何处理 evidence、矛盾和 alternative hypotheses。随着任务从执行
  protocol 走向 hypothesis-driven inquiry，evaluation object 必须包含 epistemic process，而不是把流畅
  rationale 当作 reasoning proof。
- **Mechanism / Ownership / Flow**：论文把 trace steps 标为 hypothesis、evidence、test、judgment、update、
  commitment，并以 directed dependencies 识别 refutation loop、convergent evidence、untested claim、
  evidence non-uptake 等 motifs。Environment/tool output 拥有 observed evidence；agent trace 是 claim；
  annotation pipeline 产生 derived graph；domain expert 与 task outcome 负责 calibration；scaffold 只编排
  prompts/tools，不拥有 base-model epistemic capability。
- **Evaluation Contract**：三个明确版本模型（GPT-4o-2024-08-06、Claude Sonnet 4.5、
  gpt-oss-120b）× ReAct/structured-tool scaffolds，八个科学 domains、15+ scopes、90+ tools、25k+
  runs。主评估 temperature 0、每 task 20～40 LLM calls；trace intervention 另用 temperature 0.7 的
  15 runs/task registry。latent model 以 PSIS-LOO 选型；三位 domain experts 在 25/626 traces 上复核，
  agreement 高但样本小且 class imbalance 使 raw κ 偏低。
- **What It Proves / Does Not Prove**：作者结果在其 minimal scaffolds 中显示 model choice 对解释方差的
  贡献远高于 scaffold choice，并观察大量 untested claim/evidence non-uptake；near-complete successful
  trace injection 仍未稳定修复高 epistemic-demand task。它不证明所有 scaffold/workflow 无价值，也没有
  测 plan-execute、retrieval/summarization、multi-agent、model-specific hardening、不同 temperature/budget
  或真实实验室。`reasoning itself becomes a training target` 是作者建议，不是该实验已验证的 remedy。
- **Trade-offs / Failure Modes / Old Branch**：process annotation 暴露 outcome 隐藏的 epistemic failure，
  却依赖 taxonomy、edge inference 和 judge calibration；过度形式化还可能惩罚合法但未显式 verbalize 的
  reasoning。Outcome verifier 对 deterministic workflow 仍必要；process evidence 在开放 discovery 上是
  加层，不是替代。
- **Evolution / ROADMAP / Decision**：相对 outcome-only 是 `Direct Evolution`，相对 Ch76 reflection 是
  `Layering / Dependency`。主 owner 暂定 Ch62，已读 Ch62 的 outcome/trajectory/claim evidence 和 scorer
  boundary，并联读 Ch29、Ch76、Ch77、Ch80。provisional `Integrate — New Mechanism`：未来只沉淀
  “claim–evidence–test–update”结构及适用边界，不复制 headline percentages，也不写成 model/scaffold
  普遍排序。Books Gate 关闭，只更新 W17。

### Chat2Workflow — 25/30

- **Candidate / Week / Source Family**：`CHAT2WORKFLOW-EXECUTABLE-WORKFLOW-BENCH`；W17；
  arXiv:2604.19667，v1 2026-04-21，v2 05-26；event 按 v1，当前阅读锁定 v1，后续 revision 仅核验
  metadata。作者 repository 提供 dataset、nodes、converter、pass/resolve scripts、Dify 1.9.2 与 plugin
  versions，但 current main 未绑定 event-date commit/tag。
- **Full-read Coverage**：已读 dataset reverse construction、多轮 instruction、JSON graph/schema、
  Pass/Resolve pipelines、human calibration、15-model three-run evaluation、domain/error analysis、
  limitations、Appendix prompts，并核对 repository 的 generation/conversion/evaluation paths。
- **Problem / Previous Design / Changed Constraint**：自然语言或结构相似度便于评估 workflow draft，
  但 graph 能 import 不代表 variables、branches、tool parameters 和 external dependencies 能产生正确
  outcome。生成对象从文本升级为平台可导入、可执行且通过测试的 versioned graph artifact。
- **Mechanism / Ownership / Flow**：对 production Dify/Coze workflows 反向生成多轮 instructions；模型
  输出 reasoning + JSON nodes/edges，经 converter 变成 YAML 并 import。Pass gate 顺序检查 parse/schema、
  conversion/import、variable consistency 和 LLM logical checks；Resolve gate 在三个 test cases 上实际执行，
  检查 error/empty、file type 和 text requirement。Workflow platform 拥有 execution semantics，converter
  拥有 representation translation，test/evaluator 拥有 outcome verdict，generator 不拥有 success state。
- **Evaluation Contract / Evidence Boundary**：六 domains、20 high-frequency node types、15 models、每项
  三次 run；DeepSeek-V3 judge 在抽样 500 Pass/1,282 Resolve cases 上与人工 reported agreement 为
  100%/98.83%。作者结果显示 Pass 可明显高于 Resolve，支持“representation validity 是必要非充分条件”；
  但只有三 cases/task、简化 interfaces、有限 nodes、vendor platform/version 和 LLM judge，不能代表复杂
  industrial workflow、side effects、credentials、retry/idempotency 或 production SLO。
- **Trade-offs / Evolution**：typed graph 增加 importability 和静态检查，却可能把模型优化到 schema；真实
  execution 增加证据，也增加 external service flakiness、cost 和 destructive-action risk。相对 text/schema
  evaluation 是 `Direct Evolution`，相对 durable Workflow 是受限 test layer。
- **ROADMAP / Decision**：主 owner Ch77；已读 Ch77 的 state machine、task IR、evaluator-driven search、
  replay/retry/compensation，并联读 Ch62、Ch80。现有正文已经明确 specification compilation 与 execution
  evidence、artifact identity，且比论文覆盖更多生产语义；`No Change — Already Covered`，保留在 Weekly
  作为 benchmark evidence，不为制造 diff 重复写 Books。

### SkillLearnBench — 25/30

- **Candidate / Week / Source Family**：`SKILLLEARNBENCH-CONTINUAL-SKILL`；W17；arXiv:2604.20087，
  v1 2026-04-22，唯一版本；作者 code/data repository 已核对。
- **Full-read Coverage**：已读 benchmark/task selection、human skill curation、three-level metrics、One-Shot/
  Self Feedback/Teacher Feedback/Skill Creator methods、main results、task/model sensitivity、round analysis、
  cost/token analysis、skill pattern/content/trajectory cases、judge repeatability、data augmentation、prompts、
  hyperparameters、solver/verifier 和完整 instance list。
- **Problem / Previous Design / Changed Constraint**：one-shot human-authored skill 稳定、可 review，却扩展慢；
  自动生成可从 execution experience 更新，但“写出一份 instructions”不等于可复用、会被 Agent 采用或
  能执行成功。Skill evaluation 必须拆成 artifact quality、trajectory adoption 与 outcome。
- **Mechanism / Ownership / Flow**：20 tasks 各有多 instances；learning method 从 task/trajectory/feedback
  生成 skill set，solver 在后续 instances 选择并执行。Level 1 测 coverage/alignment/safety，Level 2 测
  trajectory keypoints/order/completeness 与 usage，Level 3 用 task verifier 测 success。Teacher Feedback
  注入外部 execution evidence；Self Feedback 只让同一模型重写。Registry 拥有 skill version/provenance，
  solver 拥有 adoption decision，verifier 拥有 outcome，generator 不能凭自评分晋级 skill。
- **Evaluation Contract**：20 tasks（17 adapted SkillsBench、3 new），四种 learning methods、多种 generation
  LLM/solver 组合，最多 100 turns/1,800 秒的部分 tasks，并报告 tokens。Human-authored skill 经过任务对齐、
  pruning/reconstruction，不是 untouched neutral baseline；LLM judges 的 executability/safety test-retest
  Spearman 仅 0.76/0.61，说明中间指标本身有噪声。几乎所有 generated skills 只有 instructions，几乎
  没有 scripts，更无 MCP/subagent composition。
- **Evidence Boundary / Trade-offs**：作者实验支持 external teacher feedback 可在若干 rounds 提升，而
  self-feedback 无新信息时会重排/漂移；clear reusable workflows 获益较多，open-ended tasks 有时退化；
  stronger generator 不保证更好 skill。它不证明统一 continual method、自动 skills 可安全自发布，或
  human-authored skill 的优势能泛化到未经筛选任务。高 alignment/usage 仍可能低 outcome accuracy。
- **Evolution / ROADMAP / Decision**：相对 static skill 是 `Direct Evolution`，相对 Memory/Reflection 是
  `Layering / Dependency`。主 owner 暂定 Ch80，已读 Ch80 skill identity、feedback/release/rollback，
  联读 Ch73 的 derived procedural memory、Ch76 的 feedback independence、Ch77 的 execution authority。
  provisional `Refine — Existing Argument`：长期缺口是 skill admission 必须绑定 independent outcome、
  applicability、supersession 和 rollback，而非允许 recursive self-edit 直接覆盖 active version。Books Gate
  关闭，只更新 W17。

### ClawEnvKit — 28/30

- **Candidate / Week / Source Family**：`CLAWENVKIT-AUTO-ENVIRONMENT-GENERATION`；W17；
  arXiv:2604.18543，v1 2026-04-20，v2 04-28，v3 04-29，v4 06-10。历史事件按 v1 归周；
  v4 只用于补充核验 revision 后公开的实现与实验，不能把 6 月 model/harness roster 倒写成
  4 月 20 日已公开事实。
- **Direct / Related Primary Sources**：arXiv abstract、v4 HTML/PDF、作者 repository
  `xirui-li/ClawEnvKit`；Claw-Eval 只作为作者选取的 human-curated comparison，不替代本论文证据。
- **Access / Full-read Coverage**：已读 metadata/revision、Introduction/Related Work、environment
  formalization、parser/generator/validator、execution/grading、quality/scaling experiments、live testbed、
  limitations/conclusion，以及 Appendix 的 prompts、12 项 structural checks、semantic coverage、sandbox、
  error injection、15 类 scorer、示例任务、model/harness settings、reproducibility 与 mock-service audit。
- **Original Problem / Why Previous Design Was Reasonable**：hand-authored static benchmark 便于人工
  审查、冻结版本和长期比较；但面对持续变化的 Agent tools、跨服务状态与失败恢复，逐任务编写
  task、mock service、fixture、rubric 和 grader 成本高，覆盖速度低于 capability/tool drift。
- **Changed Constraint / Mechanism**：论文把 environment 写成 `E=(P,M,C)`：`P` 是自然语言任务
  specification，`M=(T,O)` 是 callable tools 与 server-side audit log，`C={(c_i,w_i)}` 是消费
  trajectory/audit/output/file 的检查集合。Parser 一次 LLM call 抽取带 `action/object/constraint`
  的 intent atoms；Generator 生成 task YAML、tool/interface、fixtures 与 scorer；Validator 用 12 项
  structural checks 和按 atom 类型的 semantic coverage 拒绝缺字段、权重错误、tool/action 不存在、
  safety/scoring 冲突和未闭合 asset，并把错误反馈给最多三次 regeneration。
- **State Ownership / Control Flow / Data Flow**：generation pipeline 拥有 candidate specification；
  validator 只拥有 admission decision，不能创造遗漏的业务 ground truth；每个 sandbox 拥有独立
  fixture 与 mock-service state；server-side audit 是 action fact；agent trajectory/output 是 run
  evidence；GradingEngine 产生 derived scores；release/benchmark owner 决定 environment/version
  是否进入 suite。正确流向是 `intent → typed atoms → generated E → validation → isolated run →
  audit/artifacts → scoring → immutable evaluation record`，不得让 score 反向改写原始 audit。
- **Implementation Details**：service-order shuffle、focus-action rotation 与最近 10 个 task names
  促进多样性；每个 task container 使用 `--network none`、read-only task YAML 和 `/workspace`
  fixtures。API mock 通过 middleware 对默认 25% POST calls 注入 429、500 或 2～4 秒延迟；三类
  harness 分别使用 native plugin、MCP、`SKILL.md + curl`。Safety violation 将总分清零；completion
  是 weighted checks，robustness 是 injected errors 中在后续 5 条 log 内恢复的比例。LLM judge
  权重上限为 API task 55%、file task 65%；Pass^3 要求同一任务三次都过阈值。
- **Evaluation Contract**：Auto-ClawEval 从 104 个 Claw-Eval scenario/service anchors 各生成 10 个
  variants，共 1,040 tasks、24 categories；Mini 取每个 anchor 一个，共 104。v4 比较 4 个 model
  families 与 8 个 harnesses；harness comparison 固定 Claude Haiku 4.5。运行于单台 Apple M-series
  Mac 的 Docker Desktop，无 GPU；temperature 0，最多 20 tool rounds、每 call 4096 tokens、
  per-task 300 秒、per-call 120 秒。LLM judge 占最终分数 40%～60%，OpenRouter 可路由不同 backend，
  error injection 未设 seed；作者估算不同模型 API 成本，但没有生产并发或 tail-SLO contract。
- **What the Evidence Proves**：在作者生成器、validator、mock services 与 scorer 下，可以批量产生
  结构闭合的 executable tasks，并在同一 model 下观察 harness 间差异；104-task Mini 与 1,040-task
  full set 在作者报告的聚合分数上接近。对 52 个 `>=10` tool calls 且 score `<0.4` 的案例，作者
  人工复核未发现 alternative-valid solution 被误罚。这是指定样本的 verifier audit，不是通用
  false-negative guarantee。
- **What It Does Not Prove / Threats to Validity**：`100% validity` 是自有 structural validator 的
  通过率，不证明任务语义完整；clarity/coherence 受 LLM judge 和可见 rubric 格式影响；从 52 个
  高投入低分样本得出的 `0%` 不能外推所有 1,040 tasks。Mock API 缺少 OAuth、真实 rate tier、
  schema drift、跨用户外部状态和不可逆副作用；“contamination-free by construction”也不能由
  generation 本身保证。judge failure 返回 0.5、robustness 在未注入错误时取 1，以及 unseeded
  injection/provider routing 都可能掩盖基础设施波动。论文没有披露 production privacy、retention、
  tenant isolation 或真实服务 incident contract。
- **Trade-offs / New Failure Modes**：自动生成获得 coverage、refresh、可参数化 failure injection
  与较低人工成本，却引入 generator–validator coupling、同源模型偏差、benchmark self-reference、
  scorer gaming、mock-real gap 和 revision drift；扩大 tasks 数量也可能重复相同 anchor bias。冻结
  benchmark 仍适合长期可比和 regression，人工 environment 仍适合高风险语义、不可逆 action 与
  independent adjudication。
- **Evolution Relationship**：相对 static benchmark 是 `Direct Evolution` 到 executable/on-demand
  environment；相对第 77 章 Workflow 和第 80 章 Agent Platform 是 `Layering / Dependency`，因为
  environment 测量 workflow outcome，却不拥有 production action authority。下一阶段压力是让
  generated specification 有独立 oracle、真实 API shadow、seeded replay、schema/auth drift tests、
  provenance 与 supersession，而不是只继续扩大 task 数量。
- **ROADMAP / Target and Adjacent Chapters / Existing Coverage**：主 owner 为 Ch62；已读 Ch62 的
  evaluation object、executable evidence、scorer、dataset governance、run identity 与 release gate，
  并联读 Ch23、Ch29、Ch77、Ch80。现有 Ch62 已覆盖 `artifact + environment + execution trace`、
  scorer 非真相、frozen/synthetic suites 与 EvalRun contract；真正缺口是 on-demand environment
  generator 的 validator ownership、revision identity 和 mock-real co-existence，不需要新章节。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument`；
  Historical Books Gate 关闭，当前只更新 W17。待确认：怎样用独立 oracle 避免 generator/scorer
  共源；random injection、provider routing 与 LLM judge 如何形成 replayable run identity；v1 到 v4
  哪些 task/scorer 变化需要 invalidation 旧结果。

### ReasoningBank Google Research publication node — 25/30

- **Source Family ID / Type / History**：`REASONINGBANK-MATTS`；arXiv:2509.25140，first-public
  2025-09-29；Google Research 2026-04-21 为后续传播/项目节点，不改写 first-public date。
- **Access / Full-read Coverage**：已读论文 metadata、Introduction/Related Work、memory extraction、
  retrieval/update、MaTTS、web/software benchmarks、baselines、ablation、efficiency、limitations 与
  appendix；作者 artifact 的 prompt/memory schema 同步核对。
- **Problem / Previous Design / Changed Constraint**：raw trajectory 或只存成功 routine 实现简单且
  可审计；持续任务中它们检索噪声高、重复错误，并缺少失败对照，推动从 history retention 转向
  derived reasoning memory。
- **Mechanism / Ownership / Flow**：agent 自判轨迹成功/失败，memory constructor 从对比经验抽取
  generalizable strategy；下轮检索相关 memory 注入推理，再把新 experience 合并回 bank。MaTTS
  以更多交互生成对比信号。memory service 拥有 derived record，workflow 拥有 task outcome，
  judge 仅提供带噪 label。
- **Evaluation Contract / Evidence Boundary**：作者在 web browsing 和 software engineering
  benchmark 比较 raw trajectory、successful routine 等 memory baseline，并报告 ablation/efficiency；
  它证明特定 judge、retriever、model 和 benchmark 下的改进，不证明自判正确、跨版本稳定、
  长期无污染或生产环境自我演化安全。
- **Trade-offs / Failure Modes / Evolution**：summary 降低检索成本却丢失 provenance；failure-derived
  strategy 提供负例但会固化 judge error；MaTTS 增加 compute。raw history 仍是审计/回滚依据，
  derived memory 需要 version、supersession、expiry、review 和 delete。关系为 `Direct Evolution`。
- **ROADMAP / Chapters / Existing Coverage**：Ch73 主 owner，已读 Ch72～77；现有正文已写入
  derived procedural memory、judge noise 与 consolidation/rollback contract，本轮补足与 Ch77 policy
  authority 的 handoff。
- **Decision / Files / Questions**：`Refine — Existing Argument`；更新 Ch73，明确 derived strategy
  是 advisory state 而非 Workflow policy。
  未决：谁批准 supersession，environment/tool version 变化如何触发失效。

### OpenAI Privacy Filter — 25/30

- **Source Family ID / Type / Date**：`OPENAI-PRIVACY-FILTER`；OpenAI 2026-04-22 announcement、
  model card 与公开 repository/model artifact。
- **Full-read Coverage**：已覆盖 taxonomy、bidirectional token classifier、BIOES/Viterbi span decode、
  training-data construction、operating points、PII/secret/multilingual/adversarial evaluation、限制和
  deployment guidance。
- **Problem / Previous Design / Changed Constraint**：regex/DLP 对结构化 identifier 透明可审计，
  但在非结构化、上下文依赖和长文本中 recall/precision 受限；把原始文本送云端过滤又先产生
  exposure，推动小模型本地化 sensor。
- **Mechanism / Ownership / Flow**：1.5B total/50M active token-classifier 单次 forward 标注最多
  128k context，再以 constrained Viterbi 输出八类 spans；policy owner 选择 operating point，
  filter 只产生 detection，workflow 决定 redact/mask/quarantine，audit 保存 policy/version。
- **Evaluation Contract / Evidence Boundary**：官方给出 PII-Masking-300k 原始与修订 annotation 的
  precision/recall/F1、domain adaptation、secret 和 stress tests；这些结果绑定 taxonomy、修订
  dataset 和 threshold，不证明匿名化、legal compliance、linkability 消除或零 false negative。
- **Trade-offs / Failure Modes / Evolution**：本地 sensor 减少 pre-filter exposure，仍会误删语义、
  漏检新 identifier、被 adversarial context 绕过，并需要 policy/version drift 监控；regex、allowlist、
  encryption、access control 与 aggregation 继续作为 layered controls。关系为 `Layering / Dependency`。
- **ROADMAP / Chapters / Existing Coverage**：Ch68 主 owner，已读 Ch63、Ch67～69、Ch73；当前
  正文已有 policy-bound sensor 而非 compliance guarantee。
- **Decision / Files / Questions**：`No Change — Already Covered`；保留 Ch68 provisional 内容。
  未决：跨语言/领域 operating point、audit retention 与被遮盖内容的授权恢复。

### GPT-5.5 release — 19/30

- **Source / Date / Verification**：OpenAI 2026-04-23 official release entry 已核对；它只证明
  model-family availability 与公开 product/evaluation state。
- **Score / Decision**：19/30；`Weekly Only — Version/Product Fact`。未公开到足以支持 model
  architecture、training 或 runtime 长期机制的证据。

### Seed3D 2.0 — 18/30

- **Source / Date / Verification**：ByteDance Seed 2026-04-23 official release 已核对；属于 3D
  generation/model family 的垂直发布，不与 GPT-5.5 共用机制。
- **Score / Decision**：18/30；`Weekly Only — Version/Product Fact`。公开材料没有形成与本书
  lifecycle、training system 或 serving runtime 相关的新通用 contract。

### Project Deal — 17/30

- **Source / Date / Verification**：Anthropic 2026-04-24 research entry 已核对；它是独立研究项目，
  不属于 GPT-5.5 或 Seed3D 的 model family。
- **Score / Decision**：17/30；`Weekly Only — Research State`。当前 evidence 不足以建立可迁移的
  model/runtime/Agent mechanism，保留日期与来源而不写 Books。

### COSPLAY — 25/30

- **Candidate / Source Family / History**：`COSPLAY-COEVOLVING-SKILL-BANK`；arXiv:2604.20987，
  v1 2026-04-22，26 页，当前唯一公开版本。论文 Appendix 写的是代码“will release”，本轮未找到
  event-date 可执行 artifact，故机制和数字均为作者单源实验。
- **Access / Full-read Coverage**：已读 metadata、Introduction/Related Work、MDP/trajectory 定义、
  Decision Agent、trajectory segmentation、skill contract learning、bank maintenance、SFT/GRPO
  co-evolution、六个游戏的 setup/results、ablation、hyperparameters、reward definitions、prompts、
  reproducibility 与 appendix；论文无独立 Limitations 章，限制需从实验与复现声明反推并明确标注。
- **Problem / Previous Design / Changed Constraint**：primitive action policy 或固定 hand-authored skill
  在短任务中边界清晰、易审计；长 horizon、partial observation 与 delayed reward 使单步 action
  很难归因，固定 bank 又会和 evolving policy 脱节。COSPLAY 因而从“检索已有 skill”推进到从
  unlabeled trajectories 分段、验证和维护带 contract 的派生 skill。
- **Mechanism / Ownership / Flow**：Decision Agent 总结 observation、检索候选、维护 intention 并执行
  primitive action；Skill Bank Agent 把 episode 分成可能重复的 segments，学习含 purpose、precondition、
  plan、success/abort criteria 与 post-state contract 的 proto-skill。候选不会立即发布，而进入 buffer，
  再经 materialize/refine/merge/split/retire。environment 拥有 transition/reward，raw trajectory 是
  immutable evidence，curator 产生 derived candidate，bank owner 才拥有 admission/version；Decision
  Agent 只消费已发布 skill，不能凭一次成功直接改写 bank。
- **Implementation / Evaluation Contract**：Qwen3-8B decision model 以 SFT、GRPO 和 multi-adapter LoRA
  迭代；单人游戏每设置 16 rollouts，多人游戏每 player 10 rollouts，训练 opponent 用 GPT-5-mini、
  evaluation opponent 用 GPT-5.4。六个 game 的 reward/action/horizon 各异，API opponent 版本漂移会
  改变可复现性；公开文本没有独立代码 release、完整硬件/成本或跨 seed confidence interval。
- **Evidence Boundary / Trade-offs**：ablation 支持 final bank、co-evolution 与 policy optimization 在
  作者游戏配置下共同贡献，不能证明自动 segmentation 因果正确、contract 跨 domain 稳定，或 headline
  平均 reward 可外推真实 workflow。派生 skill 降低重复探索，却新增错误分段、相似 skill 错 merge、
  stale contract、self-reinforcing reward bias 与 retirement 误删。固定人工 skill 在安全、高风险副作用和
  稳定 SOP 场景仍更合理。
- **Evolution / ROADMAP / Decision**：相对 static skill retrieval 是 `Direct Evolution`，相对 Ch73
  derived procedural memory 与 Ch80 registry 是 `Layering / Dependency`。主 owner 暂定 Ch73，已读
  Ch72～Ch77、Ch80；现有正文已有 provenance/supersession/rollback，新增价值是把 pre/post-state 与
  abort criteria 作为 admission contract。provisional `Refine — Existing Argument`；Books Gate 关闭。

### VLAA-GUI — 26/30

- **Candidate / Source Family / History**：`VLAA-GUI-STOP-RECOVER-SEARCH`；arXiv:2604.21375，v1
  2026-04-23、v2 04-24；历史事件按 v1 归周，v2 只用于 revision 核验。
- **Access / Full-read Coverage**：已读 metadata、Related Work、Manager action loop、mandatory
  Completeness Verifier、three-tier Loop Breaker、on-demand Search/Coding/Grounding agents、OSWorld-
  Verified 与 WAA setup、component/step-budget ablation、failure analysis、case、broader impact/
  limitations、action space、role prompts 和 appendix configurations。未披露训练硬件；系统主要调用
  hosted models，不应虚构 GPU contract。
- **Problem / Previous Design / Changed Constraint**：单一 GUI perceive-reason-act loop 对短任务简单且
  Context 一致；在长任务中，模型会把 partial progress 当完成，或在相同 screen/action 上循环。增加更多
  helper 也会消耗本来用于完成任务的 step budget，因此 recovery 不能是免费附加项。
- **Mechanism / Ownership / Flow**：Manager 始终拥有 task/action sequence；每次 action 后 mandatory
  verifier 只依据 UI-observable success criteria 接受或拒绝 `done`。Loop Breaker 根据 no-change、重复
  screen 和持续失败依次触发 modality switch、strategy change、external reflection；Search、Coding 和
  Grounding 是同一 action space 内按需调用的工具。environment screenshot/state 是事实，verifier 是
  completion gate，reflection 只提 proposal，Manager 继续执行，workflow controller 拥有 budget/termination。
- **Evaluation Contract / Evidence Boundary**：OSWorld-Verified 361 tasks、WAA 154 tasks，比较 15/50/100
  step budgets 和五类 backbone/component 组合。ablation 显示组件贡献依 backbone 和预算变化：在较弱
  backbone 的 15-step 设置中 verifier/search 反而挤占动作并显著退化。作者数字支持指定 harness 下的
  false-completion 与 looping 修复，不能证明单次 77.5% 等同生产可靠性、跨 run 稳定或 verifier 独立于
  Manager 的错误。
- **Trade-offs / Previous Design / Evolution**：mandatory gate 降早停，增加 model calls、latency 和
  correlated judge risk；loop escalation 降重复，却可能在 progress 缓慢时误判；Coding Agent 的独立 loop
  又新增 sandbox/side-effect 边界。短任务、低预算或已有 deterministic checker 时，单 Agent loop 仍成立。
  这是从 best-effort reflection 到 budgeted recovery control 的 `Direct Evolution`。
- **ROADMAP / Decision**：主 owner 暂定 Ch77，已读 Ch76～Ch78；现有 deterministic spine、retry、
  termination/compensation 已覆盖基本原则，新增价值是 verifier utility 必须绑定 backbone efficiency 与
  remaining action budget。provisional `Refine — Existing Argument`；Books Gate 关闭。

### From Skills to Talent: OMC — 25/30

- **Candidate / Source Family / History**：`OMC-ORGANISATIONAL-AGENT-RUNTIME`；arXiv:2604.22446，
  v1 2026-04-24，33 页，唯一公开版本；作者站点/market 与论文联合核验，但跨 domain case 仍是作者演示。
- **Access / Full-read Coverage**：已读 metadata、six typed interfaces、Talent/Container/Employee identity、
  Talent Market、E²R tree、DAG scheduler、on-demand dispatch、self/organisational evolution、PRDBench
  setup/result/cost、四个 cases、related work、limitations、formal signatures、OS analogy 和 appendix。
  论文没有 component ablation；self-evolution 也未量化拆分。
- **Problem / Previous Design / Changed Constraint**：prompt role/skill 与固定 team 对单 runtime、单 session
  足够简单；异构 backend、持久 identity、动态 capability gap 与 crash recovery 使“谁会什么”和“在哪里
  执行”必须解耦。OMC 把 portable Talent 与 runtime Container 组合成 Employee，并把 orchestration
  放在 model 之外。
- **Mechanism / Ownership / Flow**：task node 保存 description、assigned employee、finite state、result 与
  cost；DAG scheduler 以 bottom-up completion 派生 project status，不另存可漂移的完成 flag。组织层维护
  workforce/resource/memory，backend executor 保持相对 stateless。七项 invariants 覆盖 acyclicity、每人
  单任务、idempotent scheduling、bounded review、cancel cascade、dependency completion 与 crash recovery；
  pre/post hooks 产生 guardrail、memory/reflection proposal，但权威 transition 属 scheduler。
- **Evaluation Contract / Evidence Boundary**：PRDBench 50 个软件任务，作者报告 OMC 的聚合结果与约
  6.91 美元/task，并提供跨领域 cases。它支持 typed orchestration 可以承载异构 backend 和可恢复 DAG，
  不能证明 company metaphor 是必要 abstraction、market 中 capability claims 独立验证、自我改进有效，
  或跨 domain case 构成 systematic generalization。论文明确承认非 coding evaluation 和 longitudinal
  self-evolution ablation 缺失。
- **Trade-offs / Previous Design / Evolution**：portable Talent 增强复用与替换，却带来 supply-chain、
  benchmark gaming、credential scope 和 version compatibility；Multi-Agent 提高 parallelism/专业化，也增加
  约 6.91 美元/task 的 coordination cost。简单 query 应回落 single-agent adaptive dispatch。相对固定 team
  是 `Direct Evolution`，相对 Ch77 durable workflow 是 `Layering / Dependency`，OS 类比仅为
  `Explanatory Analogy`。
- **ROADMAP / Decision**：主 owner 暂定 Ch78，已读 Ch77～Ch80；Ch78 已覆盖 identity、delegation、typed
  shared state 与 coordination tax，真正缺口是“能力包 identity”和“执行 substrate identity”分离，以及
  scheduler invariants 不能由 agent chat 维护。provisional `Refine — Existing Argument`；Books Gate 关闭。

### ClawMark — 26/30

- **Candidate / Source Family / History**：`CLAWMARK-LIVING-WORLD-EVALUATION`；arXiv:2604.23781，
  v1 2026-04-26、v2 05-05；事件按 v1 归 W17，v2 仅作 revision/artifact 核验。
- **Access / Full-read Coverage**：已读 metadata、benchmark definition、100-task/13-scenario distribution、
  task construction/release gate、five-service sandbox、multi-day mutation、weighted/strict metrics、seven-
  system setup、turn/failure analysis、task parser/checker、container/inference settings、three-sweep stability、
  cases、repository/harness 与 700 traces。论文无独立 Limitations 章，已从 contract 与 released artifacts
  明确推导但未把推断写成作者事实。
- **Problem / Previous Design / Changed Constraint**：single static episode 便于 reset、冻结与重复比较；
  persistent coworker workflow 中 email/calendar/KB/file 可在 Agent 休眠时独立变化，旧 benchmark 无法区分
  “记住上次 state”与“重新观察世界”。ClawMark 因而把每个 turn 定义为一个 in-universe working day，
  在 turn 间注入 loud/silent external mutations。
- **Mechanism / Ownership / Flow**：每个 `task.py` 定义 turns、seed hooks、injection layers、supporting
  artifacts 与 weighted checker；filesystem/email/calendar/KB/spreadsheet 五个 sandbox services 拥有事实状态，
  exogenous injector 拥有 between-turn mutation，Agent 只观察 wake-up prompt 与可访问 evidence。1,537 个
  deterministic Python checkers 检查 post-turn service state；red-line 是高权重 hard constraint。task admission
  要求两次独立 rerun 得到 bit-identical verdict/diagnostic，score 不拥有原始 service truth。
- **Evaluation Contract / Evidence Boundary**：100 tasks、2～6 turns、13 scenarios，per-turn agent timeout
  2h、LLM idle 30m、4～8 compose stacks；provider-default sampling/extended thinking，main table 每模型仅一轮
  full sweep。两模型各三轮的总分跨度为 2.8pp/1.0pp，只能约束这两模型的 run noise，不能证明全部模型
  排名稳定。确定性 checker 证明 rubric 可重复，不证明 rubric 完整、task distribution 代表生产或 silent
  mutation rate 合理。
- **Evidence / Trade-offs / Failure Modes**：作者实验显示 silent-change detection 与 backend writeback 是
  指定 corpus 的主要 failure families，说明 outcome 不能只看 reasoning transcript。living world 提高
  temporal realism，却新增 mutation provenance、cross-turn identity、state reset、artifact availability 与
  long timeout/cost；silent event 也可能考察 benchmark 作者假设而非真实权限。static frozen suite 在回归、
  低成本和长期 trend 中仍合理，两者应并存。
- **Evolution / ROADMAP / Decision**：相对 static executable benchmark 是 `Direct Evolution`，相对
  Ch65 tracing、Ch73 memory 与 Ch77 workflow 是 `Layering / Dependency`。主 owner 暂定 Ch62，已读
  Ch62～Ch65、Ch73、Ch77；现有 EvalRun identity 已覆盖 environment/revision，新增价值是显式加入
  between-turn mutation log、pre/post state version 与 external actor。provisional `Refine — Existing Argument`；
  Books Gate 关闭。

### KServe v0.18.0-rc0 / rc1 — 22/30

- **Candidate / Source Family / History**：`KSERVE-0.18-RC-LLMISVC-CONTROL-PLANE`；official GitHub
  pre-releases `v0.18.0-rc0`（2026-04-20）与 `rc1`（04-22）属于同一 release family，不重复计分。
  这是 release-candidate evidence，不等同 stable 0.18.0 的最终行为。
- **Access / Full-read Coverage**：已读 rc0/rc1 release notes、LLMInferenceService autoscaling PR #5194
  的 design/behavior/tests/review history，并核对 storage migration、InferencePool readiness、TLS、llm-d
  dependency 与 reconciliation 条目；联读 Ch57、Ch58 及 Ch49/52 的责任边界。Release 没有 workload
  benchmark、hardware、SLO 或 migration failure study。
- **Problem / Previous Design / Changed Constraint**：固定 replica 或通用 HPA 对常规 predictive service
  简单透明；LLM workload 的 queue、variant 与 accelerator topology 使 CPU utilization 不足以表达 desired
  capacity。RC 将 scaling intent 纳入 `LLMInferenceService.spec.scaling`，由 controller 组合 workload-
  variant signal 与显式 actuator backend。
- **Mechanism / Ownership / Flow**：controller 为 service 创建 `VariantAutoscaling`，再由用户二选一 HPA
  或 KEDA；HPA 经 Metrics API 消费 `wva_desired_replicas`，KEDA 直接查询 Prometheus。CEL 保证 actuator
  互斥，owner reference 管 cleanup；删除 scaling config 时清理 stale resources，缺少所需 CRD 时阻断
  reconcile。runtime metric/WVA 拥有 recommendation，HPA/KEDA 拥有 replica actuation，KServe controller
  拥有 desired-resource composition；推理 scheduler 仍拥有 token/KV state。
- **Evidence Boundary / Trade-offs**：merged PR 和 tests 证明 resource construction、semantic equality、
  finalizer/label preservation、missing-CRD path 被实现/测试，不能证明 WVA 信号稳定、scale-out 满足 TTFT/
  TPOT，或 rc API 向后兼容。多 actuator 适配带来选择自由，也新增 Prometheus auth/TLS、CRD dependency、
  ownership conflict、metric freshness 与 cleanup race。固定 replicas 在稳定负载、启动慢或最小 gang 大时
  仍可能更安全。
- **Evolution / ROADMAP / Decision**：相对 CPU/generic autoscaling 是 `Direct Evolution` 到 LLM workload-
  aware desired state，相对 llm-d/WVA 是 `Layering / Dependency`。主 owner Ch57 已明确 queue/KV/TTFT
  signal 和 declarative control/data plane 分工，Ch58 拥有 request routing；RC 未改变长期结论。
  `Weekly Only — Pre-release Version Fact`；不写 Books，待 stable release、schema migration 与 SLO evidence。

### The Last Harness You'll Ever Build — 22/30

- **Candidate / Source Family / History**：`LAST-HARNESS-META-EVOLUTION`；arXiv:2604.21003，v1
  2026-04-22、v2 04-28、v3 05-01。事件按 v1 归周；v1 是三作者、纯形式化版本，不能用后续 revision
  的图表或主张补造 event-date evidence。
- **Access / Full-read Coverage**：已读 v1 metadata、Introduction、Harness definition、task/Worker/
  Evaluator/Evolution interfaces、两层 algorithms、meta-learning formulation、proposed evaluation protocol、
  Conclusion 与 references。全文没有 implementation、experiment、dataset、result、ablation、hardware、
  artifact 或 Limitations；“evaluation protocol”是建议指标，不是已执行 evaluation。
- **Problem / Previous Design / Changed Constraint**：人工 harness engineering 对特定 domain 可结合专家
  knowledge、debugger 和 tests，且变更可 review；跨 domain 反复设计 prompt、tools、observability 与
  orchestration 成本高，于是论文提出把 harness 本身变成优化对象，再把优化协议当作外层优化对象。
- **Mechanism / Ownership / Flow**：inner loop 保存 `(harness, report, score, verdict)`，每轮 reset environment、
  Worker 执行、Evaluator 对 ground-truth state/criteria/latency 评分、Evolution Agent 从 best harness 与全历史
  产生新版本；outer loop 在 meta-train tasks 上运行 inner loop、聚合分数并修改 evaluator/scoring/
  observation/orchestration protocol。environment 拥有 task truth，Evaluator 产生派生 score，version
  controller 拥有 best/current/rollback；Evolution Agent 不应直接发布生产 harness。
- **Evidence Boundary / Trade-offs**：论文只证明定义和 algorithms 可写成一致的 two-level optimization，
  没有证明收敛、held-out transfer、安全、成本或 evaluator 不被共同优化而 gaming。搜索 harness space
  可能减少人工调参，也会扩大可执行代码变更权限、evaluation overfit、recursive Goodhart、不可比 state、
  compute explosion 与回滚复杂度。人工设计在 policy、credential、irreversible action 和独立 oracle 上仍是
  authority。
- **Evolution / ROADMAP / Decision**：相对 prompt optimization 是 `Direct Evolution` 到 whole-harness
  search，相对 Ch80 release loop 是 `Principle Reuse`。已读 Ch76～Ch80；Ch80 已有 evidence→change→
  offline replay→governed rollout，论文没有足够实证改变结论。`Emerging / Experimental — Conceptual Only`；
  不进入 Books，待公开 artifact、held-out experiments、budget 与 rollback contract。

### Learning Evidence Highlighting for Frozen LLMs — 24/30

- **Candidate / Source Family / History**：`HILIGHT-FROZEN-SOLVER-EVIDENCE-EMPHASIS`；
  arXiv:2604.22565，v1 2026-04-24、v2 06-08；事件按 v1 归周，本 Review 以 v1 的方法和实验为主。
- **Access / Full-read Coverage**：已读 metadata、Introduction/Related Work、budgeted token policy、tag
  construction、grouped policy gradient/regularization、frozen Solver prompt、四 benchmark setup/baselines、
  main results、pruning/tag/budget/loss/actor-size ablation、cost/latency、solver transfer、visualization、
  conclusion、benchmark details、Actor architecture、hyperparameters 与 training settings。无独立 Limitations
  章，未披露硬件型号与并发/SLO，不能把 per-query latency 当 production contract。
- **Problem / Previous Design / Changed Constraint**：完整 raw context 保留 connective evidence 与可审计性，
  但长输入中 sparse signal 会被 distractors 稀释；retrieval/pruning 缩短输入，却可能删掉 multi-hop bridge。
  HiLight 保留原文，只在实例级选择 spans 并插入最小 boundary tags，把 evidence selection 与 reasoning
  从一次 Solver forward 中部分解耦。
- **Mechanism / Ownership / Flow**：Actor 对 context tokens 输出 Bernoulli importance policy，以
  `gamma*L` budget 投影、coalesce adjacent spans 并插 tags；每个 mask 调一次 frozen Solver，task reward
  在 group 内标准化后训练 Actor，length/entropy terms 防全选与过早 collapse。source document 拥有原始
  evidence，Actor 只产生 derived emphasis mask，Solver 产生 answer，task verifier 产生 reward；highlight
  不能改写、删除或授权 evidence。
- **Evaluation Contract / Evidence Boundary**：Amazon-Beauty、HotpotQA、SQuAD 2.0、PubMedQA，比较 no-
  highlight、random、few-shot、pruned、prompt/RL baselines，并做 Qwen3 source Solver 到 Qwen/Gemma/Llama
  target Solvers 的 zero-shot transfer。结果支持指定 datasets、prompts、tag formats 与 Actor/Solver 组合中
  highlighting 优于 pruning/no-highlight；不证明 Actor 找到因果 evidence、跨 domain/更新后稳定，或 tags
  不受 prompt-injection/position bias。multi-turn cache-aware reuse 明确留作未来工作。
- **Trade-offs / Previous Design / Evolution**：保留全文减少 deletion loss、提高 provenance，却增加 Actor
  pass、mask version、错误 emphasis 和 cache identity；训练每个 mask 需 Solver query，optimization 成本
  不等于低 inference overhead。强 retrieval、短 Context 或 deterministic evidence field 仍可省去 Actor。
  相对 static ranking 是 `Direct Evolution` 到 query-conditioned derived view，非 model attention 机制替换。
- **ROADMAP / Decision**：主 owner 暂定 Ch71，已读 Ch22 dependency、Ch71～Ch73；Ch71 已覆盖
  collect→rank→compress→place 与 source-linked Context，新增价值是“emphasis without deletion”这一
  alternative 及其 cache/version cost。provisional `Refine — Existing Argument`；Books Gate 关闭。

### Agentic World Modeling — 24/30

- **Candidate / Source Family / History**：`AGENTIC-WORLD-MODELING-POSITION-SURVEY`；
  arXiv:2604.22748，v1 2026-04-24、v2 05-18、v3 06-16。它自述为 position-driven survey；后续 revision
  只用于核对 taxonomy 完整性，不能当作 W17 新实验。
- **Access / Full-read Coverage**：已读 metadata、scope/related surveys、POMDP notation、L1 Predictor/
  L2 Simulator/L3 Evolver 定义与 boundary conditions、physical/digital/social/scientific regimes、代表系统、
  evaluation/MREP、representation-dynamics-control design space、trade-offs、open problems、conclusion 和
  capability matrices/implementation appendix。该文整合大量二手论文，未提供统一新 implementation、
  experiment 或 artifact；每个被引用系统的效果不能由本 survey 独立验证。
- **Problem / Previous Design / Changed Constraint**：以 modality 或 one-step prediction accuracy 组织 world
  models 对感知/生成研究清晰有效；Agent 要比较 action futures、检查约束并用反证更新假设时，视觉逼真
  不等于 decision-usable，促使 taxonomy 改按 capability 与 governing-law regime 划分。
- **Mechanism / Ownership / Flow**：L1 学 observation/action-conditioned short transition；L2 要满足
  long-horizon coherence、intervention sensitivity、constraint consistency；L3 再从 execute→observe→
  falsify→revise 更新 parameters、architecture 或 hypothesis space。environment/experiment 拥有 evidence，
  world model 拥有 belief/prediction，planner 消费 rollouts，hard validator 拥有 enforceable constraints，
  revision gate 才能提交 model change。
- **Evidence Boundary / Trade-offs**：taxonomy 能揭示“one-step accurate”与“planning-ready”之间的声明缺口，
  但分类与 benchmark coverage labels 含作者判断，不能证明 L1→L2→L3 是必然成熟路径或所有 domain
  共享同一 representation。latent state 可扩展却会 alias/drift；deterministic dynamics 紧贴 value 却缺
  uncertainty；symbolic state 可审计但建模成本高。旧 modality/domain-specific taxonomy 仍适合机制细节。
- **Evolution / ROADMAP / Decision**：相对 prediction-only framing 是 `Principle Reuse`，不是某个系统的
  direct successor。主 owner 暂定 Ch75，已读 Ch62、Ch71、Ch73、Ch75～Ch77；Ch75 已把 plan 定义为
  belief 上的 action/state hypothesis，Ch62 已要求 environment/execution evidence，Ch73/77 已约束 revision
  authority。`No Change — Already Covered`：保留 survey 作为 cross-chapter evidence map，不重复引入
  L1/L2/L3 命名。未决是如何以 primary studies 校准三项 L2 boundary 与 L3 falsification gate。

## Pending Full Source Review Queue

Recorded candidate queue is empty (`19/19` `20+` Full Source Reviews). Discovery Recall and Candidate Evidence
Gates are closed; any later spillback is recorded in the annual Backlog Ledger without rewinding the forward cursor.

## Repository Changes

- W17 从 5 个 baseline families 扩展为 22 个 scored families；完成 ClawEnvKit、Agent-World、
  OpenGame、Computer Use Reliability、River-LLM、AJ-Bench、AI-scientist epistemic study、
  Chat2Workflow、SkillLearnBench、COSPLAY、VLAA-GUI、OMC、ClawMark、HiLight、Agentic World
  Modeling、Last Harness 与 KServe RC family 全文 Source Review，recorded queue 归零，并把 6 个
  curation-lag 候选按 v1 日期回拨 W16；另将
  Stochastic KV Routing 回拨 W14、TCOD 归入 W18。既有 Ch68/Ch73 修改保留为 provisional
  input，本轮未新增 Books 修改。
- 2026-08-13 周级复算确认 22 scored（15 high / 4 mid / 3 low）、19/19 `20+` Full Source Reviews、
  3/3 low-score boundaries、0 pending；31 个 topical hits 的 22 scored + 8 cross-week + 1 below-retention
  关系保持一致。W17 Discovery/Candidate Gates 继续 Passed，backlog cursor 进入 W18；未修改 Books。

## Open Questions

1. experience memory 的失效与纠错由 retrieval、reflection 还是 workflow owner 决定？
2. GPT-5.5、Seed3D 2.0 与 Project Deal 的 direct technical report/model card/artifact 是否公开了
   足以升级当前低分边界的独立机制？
3. ClawEnvKit 的 generator 与 scorer 怎样通过独立 oracle 或 human audit 降低共源偏差？
4. KServe stable 0.18.0 是否保持 RC 的 scaling/migration contract，并提供可对齐的 workload/SLO evidence？

## Sources

- Google Research April 2026 archive: https://research.google/blog/2026/04/
- OpenAI Research release index, entries dated 2026-04-22 and 2026-04-23:
  https://openai.com/research/index/release/
- ByteDance Seed, “Seed3D 2.0,” published 2026-04-23:
  https://seed.bytedance.com/en/blog/seed3d-2-0-released-higher-precision-and-greater-usability
- Anthropic Research index, Project Deal dated 2026-04-24:
  https://www.anthropic.com/research
- ClawEnvKit: https://arxiv.org/abs/2604.18543
- ClawEnvKit HTML: https://arxiv.org/html/2604.18543
- ClawEnvKit repository: https://github.com/xirui-li/ClawEnvKit
- Agent-World: https://arxiv.org/abs/2604.18292
- Agent-World HTML: https://arxiv.org/html/2604.18292v1
- Agent-World project page: https://agent-tars-world.github.io/-/
- OpenGame: https://arxiv.org/abs/2604.18394
- OpenGame HTML: https://arxiv.org/html/2604.18394v1
- OpenGame repository: https://github.com/leigest519/OpenGame
- On the Reliability of Computer Use Agents: https://arxiv.org/abs/2604.17849
- On the Reliability of Computer Use Agents HTML: https://arxiv.org/html/2604.17849v1
- River-LLM: https://arxiv.org/abs/2604.18396
- River-LLM v1 HTML: https://arxiv.org/html/2604.18396v1
- AJ-Bench: https://arxiv.org/abs/2604.18240
- AJ-Bench HTML: https://arxiv.org/html/2604.18240v1
- AJ-Bench project/code/data: https://aj-bench.github.io/
- AI scientists produce results without reasoning scientifically: https://arxiv.org/abs/2604.18805
- Corral code: https://github.com/lamalab-org/corral
- Corral archived artifact: https://doi.org/10.5281/zenodo.19659851
- Chat2Workflow: https://arxiv.org/abs/2604.19667
- Chat2Workflow v1 HTML: https://arxiv.org/html/2604.19667v1
- Chat2Workflow repository: https://github.com/zjunlp/Chat2Workflow
- SkillLearnBench: https://arxiv.org/abs/2604.20087
- SkillLearnBench HTML: https://arxiv.org/html/2604.20087v1
- SkillLearnBench repository: https://github.com/cxcscmu/SkillLearnBench
- COSPLAY: https://arxiv.org/abs/2604.20987
- COSPLAY PDF: https://arxiv.org/pdf/2604.20987
- VLAA-GUI: https://arxiv.org/abs/2604.21375
- VLAA-GUI HTML: https://arxiv.org/html/2604.21375v1
- The Last Harness You'll Ever Build: https://arxiv.org/abs/2604.21003
- The Last Harness You'll Ever Build v1 HTML: https://arxiv.org/html/2604.21003v1
- From Skills to Talent: https://arxiv.org/abs/2604.22446
- From Skills to Talent HTML: https://arxiv.org/html/2604.22446v1
- Learning Evidence Highlighting for Frozen LLMs: https://arxiv.org/abs/2604.22565
- Learning Evidence Highlighting v1 HTML: https://arxiv.org/html/2604.22565v1
- Agentic World Modeling: https://arxiv.org/abs/2604.22748
- Agentic World Modeling v1 HTML: https://arxiv.org/html/2604.22748v1
- ClawMark: https://arxiv.org/abs/2604.23781
- ClawMark HTML: https://arxiv.org/html/2604.23781v1
- ClawMark repository: https://github.com/evolvent-ai/ClawMark
- KServe releases: https://github.com/kserve/kserve/releases
- KServe LLMInferenceService WVA/HPA/KEDA autoscaling PR #5194:
  https://github.com/kserve/kserve/pull/5194
- Ray releases（2.55.1 below-retention patch）: https://github.com/ray-project/ray/releases
- PyTorch releases: https://github.com/pytorch/pytorch/releases
- SGLang releases: https://github.com/sgl-project/sglang/releases
- vLLM releases: https://github.com/vllm-project/vllm/releases
- Kubernetes releases: https://github.com/kubernetes/kubernetes/releases
- Hugging Face Transformers releases: https://github.com/huggingface/transformers/releases
- Hugging Face Accelerate releases: https://github.com/huggingface/accelerate/releases
- DeepSpeed releases: https://github.com/deepspeedai/DeepSpeed/releases
- Megatron-LM releases: https://github.com/NVIDIA/Megatron-LM/releases
- llama.cpp releases: https://github.com/ggml-org/llama.cpp/releases
- ONNX Runtime releases: https://github.com/microsoft/onnxruntime/releases
- PyTorch/XLA releases: https://github.com/pytorch/xla/releases

## 2026-08-14 Final Books Integration Ledger — 22/22

| Candidate / Source Family | Score | Stable Owner | Current / Legacy | Final Disposition | Chapter-level Review Evidence |
| --- | ---: | --- | --- | --- | --- |
| ReasoningBank Google publication node | 25 | `AGENT-MEMORY` | Ch77 / Ch73 | No Change — Already Covered | episode→strategy extraction→consolidation 已覆盖；2026 publication node 不重算 2025 paper family |
| OpenAI Privacy Filter | 25 | `PLATFORM-SECURITY` | Ch72 / Ch68 | No Change — Already Covered | policy taxonomy、operating point、distribution shift 与 human escalation 已覆盖；filter 不是 privacy guarantee |
| ClawEnvKit | 28 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — Existing Argument / Experimental | static benchmark→generated typed environment→validator admission→isolated run；simulator/mock 成为 measurement subject |
| Agent-World | 27 | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — Existing Argument / Experimental | generated environment/oracle→verified rollout→failure diagnosis→targeted curriculum，并隔离 final holdout |
| OpenGame | 25 | `AGENT-WORKFLOW` | Ch81 / Ch77 | Refine — Existing Argument / Experimental | archetype scaffold、typed extension 与 executable fix 形成带 applicability/version/rollback 的 workflow artifact |
| Reliability of Computer Use Agents | 26 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — New Mechanism / Experimental | Pass@k 与 Pass^k 分责，增加 repeated-run conjunction、paired transition 与 reset/retry identity |
| River-LLM | 26 | `INFER-KV-CACHE` | Ch45 / Ch41 | Refine — Existing Argument / Experimental | token early exit 必须保持 future-consumed layer/token KV completeness；不保留作者 speedup 常数 |
| Chat2Workflow | 25 | `AGENT-WORKFLOW` | Ch81 / Ch77 | No Change — Already Covered | graph/schema validity、platform import、executable Resolve、retry/idempotency 与 artifact identity 已覆盖 |
| AJ-Bench | 25 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — Existing Argument / Experimental | passive judge→bounded evidence acquisition→timestamped observation→与 human/executable authority 校准 |
| SkillLearnBench | 25 | `AGENT-PLATFORM` | Ch84 / Ch80 | Refine — Existing Argument / Experimental | Skill artifact quality、trajectory adoption 与 executable outcome 三层 admission，禁止无新证据 recursive self-release |
| AI-scientist epistemic study | 26 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — New Mechanism / Experimental | claim→evidence→test→judgment→belief update graph 补充 outcome，不把 verbalized rationale 当思维真相 |
| COSPLAY | 25 | `AGENT-MEMORY` | Ch77 / Ch73 | Refine — Existing Argument / Experimental | trajectory candidate→pre/post/abort contract→isolated validation→Skill admission/retirement |
| VLAA-GUI | 26 | `AGENT-WORKFLOW` | Ch81 / Ch77 | Refine — Existing Argument / Experimental | completion verifier 与 loop recovery 的 utility 绑定 backbone、remaining action budget 与 call cost |
| From Skills to Talent / OMC | 25 | `AGENT-MULTI-AGENT` | Ch82 / Ch78 | Refine — Existing Argument / Experimental | portable capability identity 与 runtime/container identity 分离，由 scheduler invariants 拥有 DAG transition |
| ClawMark | 26 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — Existing Argument / Experimental | living-world EvalRun 加入 between-turn external mutation、pre/post state 与 external-actor identity |
| KServe v0.18.0 RC family | 22 | `PLATFORM-KSERVE` | Ch61 / Ch57 | Weekly Only — Pre-release Fact | RC 证明 controller/resource path，不证明 stable API、migration 或 workload/SLO 结论 |
| Agentic World Modeling | 24 | `MULTIMODAL-WORLD-MODELS` | Ch25 / N/A | No Change — Already Covered | predictor/simulator/evolver taxonomy 与 world-state/control/evaluation boundaries 已由 Ch25～26 和 Ch66 覆盖 |
| Learning Evidence Highlighting / HiLight | 24 | `AGENT-CONTEXT` | Ch75 / Ch71 | Refine — Existing Argument / Experimental | full source→query-conditioned emphasis mask→tagged view→frozen Solver；mask 不拥有事实或授权 |
| Last Harness | 22 | `AGENT-PLATFORM` | Ch84 / Ch80 | Emerging / Conceptual — Weekly Only | 只有 two-level optimization 定义，无 implementation、experiment、artifact、cost 或 rollback evidence |
| GPT-5.5 release | 19 | N/A | N/A | Weekly Only — Low Score | model-family release fact，不披露可迁移系统机制 |
| Seed3D 2.0 | 18 | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | Weekly Only — Low Score | 垂直生成更新不足以改变通用生成范式结论 |
| Project Deal | 17 | N/A | N/A | Weekly Only — Low Score | research/program fact，没有长期 AI System mechanism |

### W17 Gate Result

- Scored candidates: `22/22` final disposition；`19/19` scored `20+` Full Source Reviews retained。
- Final mix: `13 Refine + 4 No Change + 4 Weekly Only + 1 Emerging = 22`。
- Owner chapters changed: 8 Stable Nodes；没有新增 Part、章节或孤立论文笔记。
- Source-Family Books Gate: `Complete`；Archive Completion Gate: `Open`。
- KServe RC、三项低分事实、Last Harness 与 No Change families 未被强行写入机制正文。

Repository changes: Ch33、Ch45、Ch66、Ch75、Ch77、Ch81～82、Ch84。
