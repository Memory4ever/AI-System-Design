# AI Research Weekly — 2026-W04

> Coverage Window: 2026-01-19～2026-01-25
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31
> Discovery Recall Re-audit: 2026-08-13 — 23 Candidate Reviews Complete / Source-Family Books Gate Complete / Discovery Coverage Limited

## Executive Summary

本周形成两条值得长期观察的路线。Anthropic 的 assistant axis 与 Claude constitution 分别
从内部表征和显式规范讨论“assistant character 怎样形成并被稳定”；Google GIST 则讨论
训练数据 smart sampling。共同原则是模型行为不只由参数规模决定，还受 representation
方向、训练规范与样本选择共同约束，但三者属于不同层，不能画成直接演进链。

Recall repair 已完成的第一个系统候选 Sutradhara 增加了另一条长期路线：当 workload 从单次
request 变成 LLM→tool→LLM 的动态 workflow，优化对象必须从单次 TTFT 扩展到最终可见 token 的
critical path；orchestrator 掌握的 dependency / reuse semantics 需要以窄接口进入 engine，但由此也
引入 pinned state、priority fairness、partial-prefill cleanup 与跨层 failure semantics。

HeteroCache 与 DataStates-LLM 又分别暴露了 inference state 和 training state 的共同约束：异步化
不会消除状态一致性与持久化成本，只是把它们移到 tier ownership、buffer backpressure、commit 和
recovery contract。前者仍属于作者实验中的 Emerging KV tiering，后者则是对 2024 版
DataStates-LLM 的直接机制扩展，不能仅因同名而去重掉。

StaleFlow 则把同一原则推进到 RL post-training：fully disaggregated rollout/reward/training 提高资源
重叠，却让“哪个 policy version 生成的 trajectory 被哪个 training version 消费”成为算法语义。
它用 trajectory-level staleness buffer 把性能调度置于显式 `eta` 约束之下，但不等于已经解决 control
plane 故障、trajectory exactly-once 或更广任务上的 convergence。

LLM-42 则把 determinism 从“所有 kernel 永远 batch-invariant”的全局属性，重新表达为请求级的
verify/commit contract：普通 Decode 可以走高吞吐快路径，需要确定性的请求才用 fixed-shape verifier
重放窗口，并同时提交 token 与 verifier KV state。它保留 dynamic batching，却新增 rollback、verification
pause、prefix-cache incompatibility 和 operator/collective/sampler consistency 约束。

Universal Load Balancing 把另一类 Decode 问题定位在 barrier 之前：当 request/KV assignment sticky，
每个 worker 的 resident token load 会持续漂移，跨 worker 同步的 step time 由最重者决定。BF-IO 用短期
active-workload view 选择新请求 placement；其理论与 simulation 有价值，但 centralized waiting pool、
non-preemption、non-decreasing drift、solver overhead 和 energy model 限定了证据外推范围。

## Coverage and Source Coverage

- 模型与研究机构：保留 Anthropic 1 月 19、22 日与 Google Research 1 月 23 日官方研究。
- 论文与学术来源：assistant-axis 与 GIST 的机制结论按作者研究处理，标记 Experimental。
- AI Infra：原周报“未发现”不能继续视为有效 negative evidence。2026-08-07 的 `cs.DC` 回扫已命中
  training、checkpoint、collective、inference、agent control-plane 等多项系统论文；其 discovery 与
  full-read 账目在下节分开维护。

## Discovery Recall Reconciliation

- **Original scored rows:** 3（Assistant Axis、Claude Constitution、GIST）。
- **Recovered primary-source hits (first pass):** 9；arXiv v1 日期均落在 2026-01-19～2026-01-25，但全文与 venue
  核验发现 Scaling All-to-all 已于 SC Workshops 2025 公开，不能算作 2026 first-public event。
  StaleFlow、Sutradhara、HeteroCache 与 DataStates-LLM 已完成 Full Source Review，分别以 29/30、
  28/30、26/30、28/30 进入 retained set；Scaling All-to-all 以 19/30 和 cross-year duplicate 排除；
  Kareus、Faramesh、LLM-42 与 Universal Load Balancing 分别以 28/30、26/30、29/30、25/30 进入
  retained set；Faramesh 与 Universal Load Balancing 因实现/评测边界标记 `Emerging`。9 个命中均已
  完成 disposition。
- **Discovery limitation:** 当前可复核 `cs.DC` 与部分 cross-list，尚不能形成 `cs.AI/cs.LG/cs.CL`
  全类别机器可复算 census；下面是最低命中集，不是“本周只有这些论文”的声明。
- **Second-pass correction:** 在复核 W05 的 Hugging Face discovery list 时，发现该站的“Daily submitted”
  日期可能晚于 arXiv first-public date。回到 arXiv metadata 后，至少恢复出 Jet-RL（01-20）、
  CooperBench（01-19）、LongCat-Flash-Thinking-2601（01-23）、SWE-Pruner（01-23）、Endless
  Terminals（01-23）、Least-Loaded Expert Parallelism（01-23）、Agentic Search in the Wild（01-24）
  与 Fast KVzip（01-25）。8 项现已逐篇完成 Full Source Review，不能被第一轮账本静默遗漏。
- **Third-pass correction:** 2 月 2 日 discovery list 继续反查出 RM-RF（01-19）、Memorization Dynamics
  in Knowledge Distillation（01-21）与 Fission-GRPO（01-22）。三篇均已按 arXiv v1 日期归回 W04，
  并完成全文 Source Review、评分与 evidence boundary。
- **Gate status:** `23 reviewed + 0 pending / Source-Family Books Gate Complete / Discovery Coverage Limited`。
  现有 23 个评分行均有最终 disposition，并已完成逐候选写入或去重、周级反向检查；跨类别目录级 census
  仍未关闭，因此只表示当前 ledger 内候选完成 Books Gate，不表示 W04 已达到 archive-level full recall。

### Discovery Candidate Ledger

第一轮 9 个 recovered hits 与第二轮 8 个候选均已完成全文或可信拒绝核验。后续 revision 只用于核验
同一 source family，不改变 W04 事件日期；跨 `cs.AI/cs.LG/cs.CL`
的完整目录级回扫仍是明确 coverage gap，不能用当前 ledger 推断“本周只有这些论文”。

### Second-Pass Pending Ledger

| Candidate | arXiv | First-public Date | Current Status |
| --- | --- | --- | --- |
| CooperBench | 2601.13295 | 2026-01-19 | 26/30；Full Source Review complete |
| Jet-RL | 2601.14243 | 2026-01-20 | 28/30；Full Source Review complete |
| LongCat-Flash-Thinking-2601 | 2601.16725 | 2026-01-23 | 27/30；Full Source Review complete |
| SWE-Pruner | 2601.16746 | 2026-01-23 | 25/30；Full Source Review complete |
| Endless Terminals | 2601.16443 | 2026-01-23 | 24/30；Full Source Review complete |
| Least-Loaded Expert Parallelism | 2601.17111 | 2026-01-23 | 28/30；Full Source Review complete |
| Agentic Search in the Wild | 2601.17617 | 2026-01-24 | 25/30；Full Source Review complete |
| Fast KVzip | 2601.17668 | 2026-01-25 | 27/30；Full Source Review complete |

### Third-Pass Candidate Ledger

| Candidate | arXiv | First-public Date | Current Status |
| --- | --- | --- | --- |
| RM-RF | 2601.13097 | 2026-01-19 | 23/30；Full Source Review complete；proxy triage only |
| Fission-GRPO | 2601.15625 | 2026-01-22 | 27/30；Full Source Review complete；Refine Ch33 |
| Memorization Dynamics in Knowledge Distillation | 2601.15394 | 2026-01-21 | 26/30；Full Source Review complete；Integrate Ch29 |

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Anthropic assistant axis | 4 | 4 | 3 | 4 | 4 | 5 | 24/30 | No Change — Ch5 evidence ladder covered |
| Claude constitution | 3 | 4 | 4 | 5 | 4 | 4 | 24/30 | Weekly Only — official specification |
| Google GIST smart sampling | 4 | 3 | 4 | 4 | 4 | 4 | 23/30 | No Change — Ch27 data selection covered |
| StaleFlow | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Integrate — Ch33 staleness invariant |
| Sutradhara | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Integrate — Ch81 orchestrator–engine contract |
| HeteroCache | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Integrate — Ch45 recoverable tiering |
| DataStates-LLM | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Integrate — Ch35 state providers |
| Scaling All-to-all Operations Across Emerging Many-Core Supercomputers | 3 | 3 | 3 | 5 | 2 | 3 | 19/30 | Reject；2025 first-public + CPU MPI-only evidence |
| Kareus | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Integrate — Ch40 time–energy frontier |
| Faramesh | 4 | 5 | 4 | 3 | 5 | 5 | 26/30 | Integrate — Ch72；Emerging |
| LLM-42 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Integrate — Ch46 selective determinism |
| Universal Load Balancing | 4 | 5 | 3 | 3 | 5 | 5 | 25/30 | Integrate — Ch56；Emerging |
| CooperBench | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Integrate — Ch82 commitment protocol |
| Jet-RL | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine — Ch33 precision-flow identity |
| LongCat-Flash-Thinking-2601 | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Refine — Ch33 domain-mixture contract |
| SWE-Pruner | 4 | 4 | 5 | 4 | 4 | 4 | 25/30 | Integrate — Ch75 structured pruning |
| Endless Terminals | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | No Change — Ch27 already covers mechanism |
| Least-Loaded Expert Parallelism | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Integrate — Ch36 dynamic EP spill |
| Agentic Search in the Wild | 4 | 4 | 5 | 4 | 4 | 4 | 25/30 | Integrate — Ch67 session trajectory sensor |
| Fast KVzip | 5 | 5 | 5 | 4 | 4 | 4 | 27/30 | No Change — Ch45 learned eviction covered |
| RM-RF | 4 | 3 | 4 | 4 | 4 | 4 | 23/30 | Weekly Only — experimental proxy triage |
| Fission-GRPO | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Refine — Ch33 corrective branch |
| Memorization Dynamics in Knowledge Distillation | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Integrate — Ch29 KD privacy boundary |

## Full Source Review

### Anthropic assistant axis

- **Candidate / Week / Score:** Assistant Axis / 2026-W04 / 24/30；
  `Source Family ID: persona-vectors-assistant-axis`。
- **Source Type / Dates / Sources:** Anthropic 官方 Research、所链接论文与 Neuronpedia demo；
  2026-01-19 publication event。它延续 2025 Persona Vectors，而非证明单一“人格模块”。
- **Access and Full-read Coverage:** Verified；已检查 persona-space construction、axis extraction、long
  conversation drift、activation steering/capping、跨 open-weight models 实验、limitations 和 demo。
- **Problem / Previous Design / Changed Constraint:** 仅从 output 观察 persona drift 难定位内部状态；
  probe/steering direction 可提供局部 sensor/intervention，但 post-training behavior 是高维、上下文依赖的。
- **Mechanism / Ownership / Flow:** character/persona prompts→activation samples→direction extraction→
  monitor projection；运行时 activation capping 限制沿该方向漂移。模型 runtime 拥有 activation，policy
  system 仍拥有可接受行为与 escalation，axis 不能自行授权输出。
- **Implementation / Evaluation Contract:** 证据来自若干 open-weight models、选定 prompts、harmful
  drift conversations 与 steering experiments；没有证明 direction 对所有模型、语言和任务稳定。
- **Evidence Boundary:** steering 支持该方向在实验设置中的因果作用；不证明它完整解释 persona、
  model goal 或所有 harmful behavior，也不证明 capping 没有 capability side effect。
- **Trade-offs / Previous Design Still Applies:** 内部 sensor 可提前发现 drift，却增加 layer/model
  coupling、threshold calibration、false positive 和 evasion；output evaluation/red teaming 仍覆盖无法被该
  axis 表示的行为。
- **Evolution / ROADMAP:** `Direct Evolution` from Persona Vectors；Ch5 主 owner，Ch68 相邻。
  已读 Ch4～6、Ch67～69；Ch5 的 correlation→intervention→replication ladder 已完整限定此类证据。
- **Integration Decision:** `No Change — Already Covered`；现有 Ch5 已把 probe/steering 当局部 replacement
  model，不把可解码方向等同完整机制。
- **Open Questions:** axis 在不同 checkpoint、语言、long-context 与 tool-use trajectory 中是否可复现，
  capping 对有益 role adaptation 的代价如何测量？

### Claude constitution

- **Candidate / Week / Score:** Claude constitution / 2026-W04 / 24/30；
  `Source Family ID: claude-constitution-2026`。
- **Source Type / Date / Sources:** Anthropic 官方行为规范及发布说明；2026-01-22；CC0 文档。
- **Access and Full-read Coverage:** Verified as specification；已检查 intended values、priority/reasoning
  framing、training role、公开许可与官方“outputs may not always adhere”限制。训练 recipe 未披露。
- **Problem / Previous Design / Changed Constraint:** 零散 label/rule 难表达冲突目标与理由；长形式
  constitution 为训练与评审提供可版本化 normative input，但规范文本不是 runtime guarantee。
- **Mechanism / Ownership / Flow:** constitution→data/feedback/evaluation pipeline（公开说明）→model
  behavior；具体 sampling、loss、weighting 和 enforcement Not Disclosed。Policy owner 管理规范版本，
  model/runtime 只产生受经验影响的行为。
- **Evidence Boundary:** 证明该文档是 Claude training input 和 desired behavior 说明；不证明每个输出
  compliant，不证明规范内在一致，也不能把其条文当作 mechanistic interpretability 结果。
- **Trade-offs / Previous Design Still Applies:** reason-rich specification 改善可审计性，却产生解释空间、
  version migration、conflict resolution 与 eval coverage 债务；硬 policy、tool authorization 和 output
  filters 在可执行边界仍不可替代。
- **Evolution / ROADMAP:** `Layering / Dependency`；Ch27 data/feedback，Ch62 evaluation，Ch68 policy。
  已读 Ch26～28、Ch62、Ch67～69；现有正文已区分 normative target、learned sensor 与 enforcement。
- **Integration Decision:** `Weekly Only — Official Specification / Mechanism Not Disclosed`；不把厂商
  constitution 内容写成全书通用安全设计。
- **Open Questions:** constitution revision、training data lineage、policy exception 与 runtime evidence
  怎样形成可审计 mapping？

### Google GIST smart sampling

- **Candidate / Week / Score:** GIST / 2026-W04 / 23/30；
  `Source Family ID: gist-diversity-utility-subset-selection`。
- **Source Type / Dates / Sources:** Google Research 官方技术解读 + NeurIPS 2025 primary paper；博客
  2026-01-23，机制 first-public 属 2025 proceedings。
- **Access and Full-read Coverage:** Verified；已检查 max-min diversity、monotone submodular utility、
  threshold graph、bicriteria greedy approximation、hardness bound、ImageNet experiment 与 baselines。
- **Problem / Previous Design / Changed Constraint:** random、uncertainty/margin、k-center 或纯 submodular
  各自优化覆盖或 utility，却无法同时避免 redundancy 和保留任务价值；大数据使 exact joint optimum
  NP-hard。
- **Mechanism / Flow:** 遍历 distance thresholds→构建相似性 graph→在 independent-set constraint 下
  greedy 最大化 utility→从候选 thresholds 选解。Selector state 属 data pipeline，embedding/utility/
  threshold version 决定最终 dataset identity。
- **Evaluation Contract:** 理论保证针对论文定义的 metric/function class；经验部分以 ResNet-56、
  ImageNet 和单次 subset selection 等条件比较 random、margin、k-center、submodular variants。
- **Evidence Boundary:** 证明特定组合优化的 bicriteria guarantee 与作者实验；不证明 embedding distance
  等于语义多样性，也不证明 LLM pretraining quality、rare safety coverage 或在线重采样收益。
- **Trade-offs / Previous Design Still Applies:** 保证 diversity-utility 平衡，却依赖 distance/utility
  proxy，可能丢失 rare-but-close examples，并增加 pairwise/threshold computation；random sampling 在
  unbiased estimation，domain quota 在 policy coverage 中仍合理。
- **Evolution / ROADMAP:** `Principle Reuse`；Ch23 主 owner，Ch22/62 相邻。已读 Ch22～24 与 Ch62；
  Ch23 已要求 quality、diversity、coverage、dedup 和 lineage，不需要引入单一算法作为默认答案。
- **Integration Decision:** `No Change — Already Covered`；作为受限算法案例保留 Weekly。
- **Open Questions:** 如何把 subpopulation/safety coverage、data licensing 和 training-loss contribution
  加入 utility，而不让 proxy 被优化器利用？

### StaleFlow

- **Candidate / Week / Score:** StaleFlow / 2026-W04 / 29/30；
  `Source Family ID: staleflow-bounded-staleness-rl-runtime`。
- **Source Type / Dates / Revision / Artifact:** arXiv primary systems paper v1 首次公开 2026-01-19；
  本轮访问 2026-08-07。已用 v1 HTML 固定 W04 证据；作者 PSRL repository 于 2026-07-28 才公开，
  只用于核验当前 artifact 与论文的 Reserve/Occupy/Consume、PS、NIXL 路径，不倒算为 1 月公开证据。
- **Full-read Coverage:** 已阅读 metadata、Introduction/Related Work、RL workflow、staleness/skew
  characterization、trajectory version、virtual buffer protocol、compatibility、TS/PS architecture、
  snapshot-command cycle、cost model、routing/synchronization/migration、全部 evaluation、Conclusion，
  以及 parameter synchronization、cost-model、redundant-rollout、完整策略伪代码等 Appendices。论文
  没有独立自身 Limitations / Threats 章节，也没有 failure/crash/timeout evaluation，记为
  `Not Disclosed`。
- **Original Problem / Previous Design / Changed Constraint:** 同步 colocated rollout→reward→training
  保持 trajectory on-policy 边界最清楚，却让 generation 和 training 串行且资源形态互相牵制；简单
  disaggregation / one-step pipeline 增加重叠，但通过限制 in-flight data 控制 staleness 时又限制 partial、
  redundant、multi-version 和 migration。变化后的约束是 reasoning trajectory 长度高度偏斜，必须在
  workload balancing 与 policy lag / convergence 之间联合决策。
- **Mechanism / State Ownership / Invariant:** 每条 trajectory 绑定最旧生成版本 `V_traj`，每个 training
  buffer 绑定 `V_buf`，核心不变量为 `V_traj + eta >= V_buf`。Staleness manager 只拥有 ID/version 与
  lifecycle metadata：Reserve 从允许范围的最新 buffer 反向占位，reward 完成后 Occupy 贪心放入最早
  可用位置，Ready buffer 才能 Consume；含 unfinished reservations 的满 buffer 为 Stuck 并产生背压。
  因而吞吐调度不能绕过训练语义 gate。
- **Control Flow / Data Flow:** trajectory server 持有 initial/partial trajectories，parameter server 持有
  latest parameters，rollout coordinator 以 Pull、Route、Interrupt 组合 partial rollout、migration 与
  per-instance model update，Abort 则不可逆丢弃。PS 通过 read-write lock 让 Push 与 Pull 互斥、多个
  Pull 并发；coordinator 的 speculative state `P` 只接受已反映此前 commands 的新 snapshot，并对
  Interrupt→Route、Pull→Route 依赖执行 wait/pending。
- **Implementation Details:** 论文报告约 22K 行 Python，training 支持 Megatron/FSDP2（评估用
  Megatron），rollout 基于 vLLM；CPU-side distributed PS 用 NIXL/UCX，统一 training/PS/rollout 的
  parameter slicing，Push 可与下一 training step overlap、但须在 optimizer mutation 前完成，Pull 阻塞
  target instance generation。作者选择 PS 与 rollout colocate 并 fully replicate，使 Pull 走 local PCIe、
  Push 走 RDMA；这是列明部署选择，不是所有 disaggregated RL 的必然结构。
- **Evaluation Contract:** 16 台机器、每台 8×NVIDIA H20；DAPO、DAPO-Math-17k、AIME24，prompt /
  response limits 2K/20K，batch 128、group 16，即每 step 2,048 trajectories。模型涵盖
  Qwen2.5-14B R1-distill、Qwen2.5-32B base/distill 与 Qwen3-30B-A3B，使用 64/128 GPUs；比较 VeRL、
  VeRL-Pipeline、VeRL-Async、AReaL、Roll Flash，并为各系统调优 rollout/training GPU ratio。
  StaleFlow 参数为 `mu=0.3`、`phi_wait=3`、`phi_throughput=5`，主要比较不启用 redundant rollout。
- **Evidence Boundary:** 作者结果支持在上述 workload/hardware 与统一 `eta` 比较下，相对 synchronous、
  one-step 和 strict-staleness baselines 的 throughput improvement；最强 strict-control baseline
  VeRL-Async 的上限为 1.42×。Convergence 只在 Qwen2.5-32B 100 steps、Qwen3-30B-A3B 50 steps 上显示
  `eta=1～3` 与同步 baseline 相近、`eta=10` collapse；这不证明所有 RL objective、reward sparsity、
  multi-turn/agent environment 或更长训练都存在同一安全 bound。成本模型在单列明设置平均误差
  10.52%，不是通用 scheduler oracle。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** 协议用 metadata reservation 换取
  staleness hard bound，却增加 centralized manager/coordinator、Stuck buffer、version bookkeeping、
  trajectory interrupt/re-prefill、PS replication/RDMA 和 snapshot-command ordering。Redundant rollout
  会主动丢弃 long tails 并造成 length distribution shift，作者因此未纳入主比较。论文没有定义 manager /
  TS/PS crash recovery、command retry/idempotency、trajectory exactly-once、partial environment side
  effects 或 split-brain semantics；同步/one-step 路线在短 trajectory、严格 on-policy、故障语义优先或
  scale 较小时仍更简单。
- **Evolution / ROADMAP / Adjacent Chapters:** `Direct Evolution`：synchronous on-policy loop →
  one-step/disaggregated overlap → configurable bounded staleness → trajectory-level lifecycle gate +
  staleness-aware scheduling。主 owner `TRAIN-GRPO`（当前 Ch33，legacy Ch29），邻接
  `TRAIN-PPO`、`TRAIN-CHECKPOINT` 与 `TRAIN-DISTRIBUTED-TRAINING`；已读 owner 与相邻章节。
- **Integration Decision:** `Integrate — New Mechanism`；已在 Ch33 把 `algorithmic staleness invariant`
  与 trajectory lifecycle、rollout scheduling 组合为一等 contract，并保留同步/one-step 路线的适用边界。
- **Open Questions:** `eta` 应由哪个 convergence signal 动态收紧；Reserve/Occupy 状态怎样 checkpoint；
  coordinator/TS/PS 故障、重复命令和 side-effectful agent environment 怎样恢复；跨 policy segments 的
  logprob / advantage correction 怎样定义？

### Sutradhara

- **Candidate / Week / Score:** Sutradhara / 2026-W04 / 28/30；
  `Source Family ID: sutradhara-workflow-aware-agentic-serving`。
- **Source Type / Dates / Revision:** arXiv primary systems paper v1，首次公开 2026-01-19；本轮访问
  2026-08-07。无后续 revision，未用相关工作标题替代本文证据。
- **Full-read Coverage:** 已阅读 metadata、agent execution model、6,000-request characterization、
  replay method、three findings、five-call API、prompt splitting、streaming dispatch、semantic KV
  policy、request scheduling、implementation、evaluation、ablation、related work 与 conclusion。论文
  没有独立 Limitations / Threats 章节，记为 `Not Disclosed`。
- **Original Problem / Previous Design / Changed Constraint:** request-response API 对普通单轮 serving
  是合理的隔离边界，engine 可独立优化 TTFT/TPOT；但 tool agent 的用户可见 FTR 横跨多次 prefill、
  decode 和 tool call，engine 看不到 iteration/dependency，orchestrator 又不能控制 cache/scheduling。
  新约束是动态 workflow critical path，而不是单个 inference request latency。
- **Mechanism / State Ownership / Control Flow:** orchestrator 保留 prompt template、tool dependency、
  agent-request/iteration identity 与 semantic reuse hint；engine 仍拥有 batching、KV blocks 和 schedule。
  五个 API 支持 partial prefill submit/extend、token callback、KV tag 与 reuse priority：tool-independent
  prefix 与 tool execution overlap；完整 JSON object 一生成就 dispatch；cache 依
  `RESPONSE→TOOL_OUTPUT→USER_QUERY→SYSTEM_PROMPT→PARTIAL_PREFILL` 顺序淘汰，并以原始 agent
  arrival time 排 iteration priority。
- **Failure / Cleanup Semantics:** partial prefill 必须持有 continuation handle 并 pin KV；tool timeout /
  failure 时 orchestrator 丢弃 continuation、降低 hint、允许释放 state。实现只有 heartbeat membership，
  论文将 leader election / stronger fault tolerance 留作扩展；这意味着 API 需要 idempotency、lease、
  orphan cleanup 与 recovery contract，不能只看 latency fast path。
- **Implementation / Evaluation Contract:** 约 3,500 行 Python、vLLM 0.11.0、asyncio orchestrator、
  PD colocated、chunk size 256；Qwen3-14B 与 Gemma-12B、A100 80GB。分析数据是大型云平台生成的
  6,000 条 synthetic enterprise requests；实验从中分层抽取两组各 60 条 tool-heavy / iteration-heavy
  traces，以 Poisson arrivals replay，并按原 tool/LLM ratio 模拟 tool latency；真实工具实现不可访问。
- **Evidence Boundary:** 作者实验支持在上述 replay、模型与 A100 条件下，prompt splitting、streaming
  dispatch 与 semantic KV policy 可降低 FTR/E2E；其 ablation 从 KV baseline 逐步加入 PS/DS。
  15.83% median FTR、12.3% p99 与其他百分比只属于列明 trace/QPS；高于 engine capacity 后收益缩小。
  不证明任意 tool latency、真实 side effect、multi-node engine、PD disaggregation 或公平性约束下成立。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** cross-layer semantics 提高 critical-path
  可见性，却让 engine API 承担 tag validity、priority inversion、tenant isolation、pinned-cache pressure、
  streaming parser correctness 与 cancellation。静态 DAG 已知时 declarative planner 更易做全局优化；
  tool 很短、cache 足够或 workflow 浅时黑盒接口更简单；不完整参数不可安全执行的 tool 仍不能提前跑。
- **Evolution / ROADMAP / Adjacent Chapters:** `Layering / Dependency`：single-call TTFT/TPOT → compound
  LLM DAG → non-clairvoyant agent scheduling → tool-aware orchestrator/engine co-design。主 owner
  `AGENT-WORKFLOW`（当前 Ch81，legacy Ch77），邻接 KV Cache、Inference Scheduling、PD 与 Agent
  Platform；已读 owner 与相邻章节。
- **Integration Decision:** `Integrate — New Mechanism`；已在 Ch81 写入窄 orchestrator–engine hints、
  partial-prefill continuation 的 lease/idempotency/cleanup contract，并保留黑盒 request API 的成立条件。
- **Open Questions:** continuation handle 的一致性、lease 与 rollback 如何定义；semantic priority 如何与
  per-tenant quota、deadline、fairness、tool authorization 和 distributed KV ownership 组合？

### HeteroCache

- **Candidate / Week / Score:** HeteroCache / 2026-W04 / 26/30；
  `Source Family ID: heterocache-head-aware-tiered-kv-retrieval`。
- **Source Type / Dates / Revision:** arXiv primary paper v1 首次公开 2026-01-20；v2 于
  2026-04-18 修订，后收入 ACL 2026。W04 按 v1 计入，本轮用 16 页 v2 PDF 核验方法、实验与
  limitations，不把后续 venue 当作新事件。
- **Full-read Coverage:** 已阅读 metadata、Introduction/Related Work、head observations 与公式、
  four-role taxonomy、stability allocation、hierarchical retrieval、algorithm、三个 benchmark、latency、
  ablation、Limitations、完整 Appendix 中 calibration、transferability、system specs、CPU memory /
  bandwidth、multi-needle、tail latency 与 constrained-interconnect tests。
- **Original Problem / Previous Design / Changed Constraint:** FullAttention/FullKV 保留所有历史，避免
  irreversible information loss；static eviction 在 attention 分布稳定时低开销，但 attention drift 会让
  早期被删 token 后来变重要。把完整 KV 放 CPU 并逐步检索可逆，却会放大 PCIe traffic。变化后的
  约束是：不同 head 的时间稳定性与同层冗余并不均匀，不能用统一 budget/retrieval frequency。
- **Mechanism / State Ownership / Data Flow:** offline calibration 用 top-k attention-overlap 得到 per-head
  stability/similarity，划分 anchor、volatile，并将相似 heads 聚成 pivot/satellite；volatile/pivot 在 GPU
  保留 FullKV，anchor/satellite 只保留按 inverse-stability 分配的 top-`l_i`。satellite FullKV 由 CPU
  持有；pivot 以 sliding-window median 监控相对 prefill baseline 的 drift，越阈值才异步拉取相应
  satellite KV 并更新 baseline。新增状态是 taxonomy、thresholds、budget、CPU reservoir 与 drift history。
- **Implementation / Evaluation Contract:** Llama-3.1-8B-Instruct、Qwen2.5-14B-Instruct、
  DeepSeek-R1-Distill-Llama-8B；LongBench、LongBench v2、InfiniteBench、NIAH/U-NIAH。主系统为
  A100 PCIe 80GB、Xeon Gold 6338、256 GiB DDR4、PCIe 4×16；budget 0.3/0.5。decode latency 取生成
  50 tokens 的均值，tail test 连续生成 1K tokens；224K 的约 3× 只对应作者该设置。
- **Evidence Boundary:** 作者结果与 ablation 支持在上述 models/datasets/thresholds 上，non-uniform
  allocation 和 pivot-triggered retrieval 都贡献 accuracy/latency；128K 时报告 CPU peak 17.95 GB、
  PCIe 21.07 GB/s，1K-token tail test retrieval trigger 0.823%。这些不能证明所有 heads/模型/任务共享
  taxonomy，也不能把单请求 PCIe 余量外推到高并发、多租户或 NUMA / CXL / remote tier。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** 通过 CPU capacity 避免 irreversible
  eviction，却增加 calibration drift、proxy miss、pivot/satellite coupling、PCIe contention、async update
  ordering 与 stale baseline。作者承认当前是高层 PyTorch、无 custom sparse/retrieval CUDA kernel，
  极低带宽下不能完全隐藏 I/O。短上下文、高并发 PCIe 饱和或 correctness-first 场景仍可选 FullKV；
  稳定 workload 中 static compression 更简单；KV quantization 与本机制正交而非后者替代前者。
- **Evolution / ROADMAP / Adjacent Chapters:** `Direct Evolution`：FullKV → irreversible static eviction →
  coarse CPU recall → head-aware tiering + sparse drift-triggered recall。主 owner `INFER-KV-CACHE`
  （当前 Ch45，legacy Ch41），邻接 Attention、Compression、Engine 与 Heterogeneous Memory；已读 owner
  与相邻章节。
- **Integration Decision:** `Integrate — New Mechanism`；已在 Ch45 接续 learned eviction，写入可恢复
  tier、drift-triggered recall 与 CPU/PCIe ownership，不把实验吞吐外推为通用结论。
- **Open Questions:** model/adapter/RoPE/context distribution 改变时 taxonomy 如何失效检测；CPU reservoir
  的 version、tenant isolation、backpressure、deadline、cancel 与 asynchronous update rollback 怎样定义？

### DataStates-LLM

- **Candidate / Week / Score:** DataStates-LLM / 2026-W04 / 28/30；
  `Source Family ID: datastates-composable-asynchronous-checkpoint`。
- **Source Type / Dates / Revision:** arXiv primary systems paper v1，首次公开 2026-01-23；本轮访问
  2026-08-07。它明确把 HPDC 2024 DataStates-LLM（arXiv:2406.10707）作为
  `DataStates-LLM-Old` baseline，因此属于同一 source family 的 `Direct Evolution`，不是旧论文重发。
- **Full-read Coverage:** 已阅读 metadata、Background/Related Work、checkpoint size / immutability /
  3D heterogeneity / serialization 分析、五项 design principles、persistent layout、DeepSpeed integration、
  C++/CUDA implementation、platform/model/dataset contract、scaling/frequency experiments、ablation、
  microbenchmark、Conclusion 与 references。论文没有独立 Limitations / Threats 章节，记为
  `Not Disclosed`；公开正文也未报告 failure injection 或 restore-correctness experiment。
- **Original Problem / Previous Design / Changed Constraint:** 同步 `torch.save()` 对小模型与低频保存
  的优点是语义直接：save 返回时 checkpoint 已持久化；早期异步多层 checkpoint 利用 host staging
  缩短 pause，2024 DataStates-LLM 又利用 forward/backward 中 model/optimizer state 不可变的窗口重叠
  copy 与 I/O。新约束是 TP/PP/DP、ZeRO、mixed precision 与 host control objects 形成 residency、type /
  precision、shard/cardinality 三维异构；全对象序列化、多小文件与粗粒度搬运成为新的关键路径。
- **Mechanism / State Ownership / Control Flow:** training runtime 在 optimizer update 后发起 logical
  checkpoint；各 state provider 保留对象的 type、layout、residency 与 serialization knowledge，并以
  byte-stream iterator 暴露 tensor 或序列化对象；C++ engine 用预分配 pinned circular host cache、专用
  CUDA streams 和 background workers 流式执行 GPU→host→Lustre。若 lazy D2H 在下一次 update 前未
  完成，training 必须等待；若 host cache 饱和，producer-consumer backpressure 会阻塞后台 flush 或训练。
- **Persistent Layout / Recovery Contract:** 已知 tensor size 使用 fixed offsets；大小未知的 serialized
  objects 在 tensor 区之后 concurrent log-structured append；末尾 metadata header 描述两类对象以供
  recovery。该 layout 解决动态 chunk 与流式 I/O 的兼容，但 durable completion、跨 rank atomic commit、
  corrupt/incomplete file rejection 和 latest-pointer policy 在论文正文中没有完整 protocol。
- **Implementation / Evaluation Contract:** DeepSpeed 0.16.6 backend，C++/CUDA、liburing `O_DIRECT`；
  Polaris 节点为 4×A100 40GB、NVLink、PCIe Gen4、AMD Milan、512GB DDR4，Lustre PFS 公布 aggregate
  peak 650GB/s。实验使用 BLOOM/Llama-derived 3B/7B/13B/33B/70B，TP=4、PP 随节点数、通常 DP=1，
  DP 实验用 ZeRO-1；OSCAR-en 79K、Llama 2 tokenizer、sequence 2048、micro-batch 16、每节点 80GB
  pinned host cache。比较 DeepSpeed、TorchSnapshot、2024 DataStates-LLM 与新版；指标是 slowest-rank
  blocking time 定义的 effective throughput、iteration time 与 15/50 iterations 的 end-to-end time。
- **Evidence Boundary:** 作者实验支持在上述 Polaris、模型、parallel layout、checkpoint frequency 与
  bounded host-cache 条件下，composable providers、选择性序列化和 stream-oriented multi-tier flush
  降低 blocking / end-to-end overhead；论文汇总结论为 3～4.2× throughput 与 1.3～2.2× end-to-end
  improvement。它不证明不同 PFS/object store、FSDP/ZeRO-2/3、超出单 checkpoint host capacity、
  preemption、rank failure 或 cross-layout restore 下仍有同等收益，也未用恢复后的 loss continuity
  验证“可反序列化”等于“正确恢复”。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** 性能来自预留 pinned host memory、
  并发 I/O 与更复杂的 provider/layout protocol；代价包括 NUMA/PCIe/PFS contention、pending checkpoint
  backpressure、header/append corruption、后台任务退出前 flush、跨 rank commit 与版本兼容债务。
  小模型、低频 checkpoint、host memory 紧张或要求 save-return 即 durable 的场景，blocking save 仍更
  简单；旧版 lazy asynchronous design 在 homogeneous tensor-heavy state 中仍成立，新 provider 层是为
  heterogeneity 与 serialization bottleneck 增层，不是否定旧机制。
- **Evolution / ROADMAP / Adjacent Chapters:** `Direct Evolution`：blocking durable save → host-staged
  asynchronous save → exploit immutable phases / lazy capture → heterogeneous state providers + selective
  serialization + streaming persistent layout。主 owner `TRAIN-CHECKPOINT`（当前 Ch35，legacy Ch31），
  邻接 Distributed Training、Megatron 与 DeepSpeed；已读 owner 与相邻章节。
- **Integration Decision:** `Integrate — New Mechanism`；已在 Ch35 将 state provider、流式 layout、
  backpressure 与 restore boundary 接入既有 async staging/transactional commit 主线。
- **Open Questions:** 怎样把 provider-produced files 纳入跨 rank atomic manifest；故障发生在 header
  append、background flush 或 update barrier 时 loader 应选择哪个 checkpoint；restore correctness、
  host-cache admission 与 object-store backend 如何验证？

### Scaling All-to-all Operations Across Emerging Many-Core Supercomputers

- **Candidate / Week / Score:** Scaling All-to-all / discovery in 2026-W04 / 19/30；
  `Source Family ID: sc25-many-core-cpu-alltoall`。
- **Source Type / First-public Correction:** SC Workshops 2025 peer-reviewed workshop paper，会议日期
  2025-11-16～21，DOI `10.1145/3731599.3767393`；arXiv v1 到 2026-01-24 才上传。SC25 proceedings、
  论文 ACM metadata 与作者 PDF 均证明 2025 已公开，因此 W04 只记录 cross-year dedup，不将它算成
  2026 event。
- **Full-read Coverage:** 已阅读 Background/Related Work、Bruck/pairwise/nonblocking、hierarchical /
  multi-leader、node-aware/locality-aware、multi-leader + node-aware algorithms、全部三机实验与 component
  breakdown、Discussion、Future Work 和 Conclusion。论文没有独立 Limitations / Threats 章节。
- **Original Problem / Previous Design / Changed Constraint:** Bruck 用少量 steps 换更大 byte volume，
  适合 small messages；pairwise direct exchange 限制 contention，却有 `p-1` 同步 steps；single-leader
  hierarchy 减少 inter-node messages，却把 many-core node 的 gather/scatter 和单 leader 变成瓶颈。
  约束变化是单节点 96/112 CPU cores、socket/NUMA 层级与 NIC injection limit，使“local”不再是单一成本。
- **Mechanism / Trade-off:** multi-leader 把 ranks 分组并增加 leaders，降低 local gather/scatter，代价是
  更多 inter-node participants；locality-aware node aggregation 缩小 intra-node redistribution region，代价
  是更多跨 region steps；组合算法先 group-local gather、leaders 间 node-aware exchange、node-local
  redistribution、再 scatter。不存在普遍最优 leader count，message size、process count、NUMA 与 network
  共同决定 crossover。
- **Evaluation Contract:** Dane/Amber 为 112-core Intel Sapphire Rapids + Omni-Path，Tuolomne 为
  96-core AMD MI300A CPU cores + Slingshot-11；OpenMPI/Cray MPICH 与列明 LibFabric。使用每节点全部
  cores、2～32 nodes、每 process 4～4096 bytes，并测试 4/8/16 processes per leader；每点报告 3 次
  运行的 minimum。最大 3× 只属于特定 32-node Sapphire Rapids/system-MPI 比较，且 proprietary
  MPI 内部算法未知。
- **Evidence Boundary / AI Relevance:** 结果支持 CPU MPI equal-sized `MPI_Alltoall` 的 locality/message-size
  crossover；Tuolomne 的大消息反而是 system MPI 最快，nonblocking 还出现 run variability。论文没有
  GPU kernel/NCCL、GPU Direct、MoE token skew、`Alltoallv`、端到端 training 或真实 AI workload，作者
  也把 GPU 与 AI collectives 明确列为 future work。因此不能把结果直接外推到 expert parallelism。
- **Evolution / ROADMAP / Adjacent Chapters:** `Principle Reuse`：flat collective → node hierarchy →
  multi-leader/locality-aware decomposition；其长期原则已由 Ch32 的 semantic/algorithm/runtime/transport/
  topology 五层与 message-size crossover 覆盖。已核对 Ch32 与 ROADMAP；若未来出现 GPU/MoE 的
  primary evidence，应建立新 source family，而不是沿用这组 CPU benchmark 数字。
- **Integration Decision:** `Reject from 2026-W04 retained set — 2025 first-public and 19/30`；不修改
  Books，也不迁移/改写 2025 Weekly，以免超出本轮范围。
- **Open Questions:** 该设计在 GPU-resident uneven expert traffic、multiple NICs、GPUDirect 与
  `Alltoallv` 下的 crossover 是否仍成立？minimum-of-three 会怎样影响 tail/variance 判断？

### Kareus

- **Candidate / Week / Score:** Kareus / 2026-W04 / 28/30；
  `Source Family ID: kareus-joint-training-time-energy-frontier`。
- **Source Type / Dates / Revision:** arXiv primary systems paper v1，首次公开 2026-01-25；本轮访问
  2026-08-07。论文建立在 Zeus、Perseus、Megatron-LM、Nanobatching 与 MSCCL++ 上；无公开 Kareus
  artifact link，框架行为只按论文实现描述记录。
- **Full-read Coverage:** 已阅读 metadata、GPU power model、prior-system comparison、dynamic/static
  energy breakdown、六组 schedule case studies、optimization formulation、partition model、multi-pass
  multi-objective Bayesian optimization、frontier composition/generalization、implementation、14-workload
  evaluation、baselines/metrics、large-scale emulation、MBO overhead、thermal sensitivity、Related Work、
  Conclusion，以及 constant-frequency theorem 与 search-space/hyperparameter/frontier Appendices。论文
  没有独立 Limitations / Threats 章节，记为 `Not Disclosed`。
- **Original Problem / Previous Design / Changed Constraint:** Megatron-style sequential kernels 语义简单；
  Nanobatching 通过 compute/communication overlap 缩短 iteration、降低 idle/static energy；Perseus 对
  off-critical-path microbatches 降频以减少 dynamic energy。两者简单叠加仍不最优，因为 frequency 会
  改变 compute/communication relative duration，而 SM allocation 与 launch timing 又改变 critical path；
  三个变量必须联合优化，不能把“更多 overlap”或“更低 frequency”当单向收益。
- **Mechanism / State Ownership / Control Flow:** Kareus 把一个 nanobatch 的 communication kernel 与
  另一个 nanobatch 中无依赖的连续 compute kernels 组成 partition；每个 partition 的候选由
  communication SM count、launch position 和 GPU frequency 定义。MBO 用 time/energy surrogate，分别按
  total/dynamic/static hypervolume improvement 加 uncertainty pass，生成 partition Pareto frontier；同类
  partitions 共享配置，microbatch 内统一 frequency，再把 partition→microbatch→1F1B iteration frontiers
  组合。Runtime 按 job latency/energy target 选 point，而不是硬编码一个“最佳频率”。
- **Implementation Details:** 基于 Megatron-LM；custom `torch.autograd.Function` 包住 Transformer
  partitions，compute/communication 使用不同 CUDA streams、CUDA events 控制 launch timing，MSCCL++
  grid size 控制 communication SMs，Zeus Pipeline Frequency Optimizer 控制 frequency。连续
  communication 或短 memory-bound kernels 会被组合；小 workload 下 partitioned overlap 可能降低
  arithmetic intensity，因此 sequential execution 也作为 frontier candidate。frequency switching 为毫秒级，
  所以不允许每个短 partition 独立切频。
- **Energy Measurement Contract:** Zeus/NVML 采集 GPU energy；论文把 P0 ready-state power × iteration
  time 定义为 static energy，total-static 为 dynamic energy。NVML 约 100ms sampling 无法直接可靠测
  millisecond partitions，作者对每个 candidate 重复 5 秒并 cooldown 5 秒至低于 32°C；单 candidate
  约 13 秒。该定义只覆盖 GPU board 侧测量，不等于服务器 CPU、network、cooling 或 facility energy。
- **Evaluation Contract:** 两台 AWS p4d.24xlarge、共 16×A100，节点内 NVSwitch、跨节点 400Gbps；
  实机为 Llama 3.2 3B 与 Qwen3 1.7B，PP=2、8 microbatches，TP8 或 CP2+TP4，microbatch 8/16、
  sequence 4K/8K，并启用 activation checkpointing。比较 Megatron-LM、Megatron+Perseus、
  Nanobatching+Perseus；max-throughput 以 Megatron 为 baseline，iso-time/iso-energy frontier 以
  Megatron+Perseus 为 baseline。Llama 3.3 70B、PP10/TP8/global batch 2048 是基于小规模 profiling 的
  emulator，不是 70B 实机训练。
- **Evidence Boundary:** 作者实验支持在上述 A100、Megatron/MSCCL++、model/shape 与 energy model
  下，联合控制三变量 Pareto-dominate 各 baseline；28.3% iso-time energy 与 27.5% iso-energy time 是
  14 个配置中的最佳值，不是所有 workload 的预期收益。MBO 平均 2 小时/32 GPU-hours，70B 结论依赖
  Perseus emulator。Appendix 的 constant-frequency theorem 依赖 `P_dyn=k f^3`、constant static power 和
  equal time at equal average frequency 三项假设，不能当作任意 GPU/DVFS workload 的无条件定律。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** 收益换来 workload-specific profiling、
  thermal protocol、surrogate miss、configuration invalidation、frequency-control permission、MSCCL++
  kernel coupling 和 search overhead。model shape、microbatch、parallel degree、GPU SKU、driver/kernel 或
  cooling 改变都可能使 frontier stale；per-GPU asynchronous switching 还需要 collective peers 的执行
  compatibility。短小 workload、搜索成本无法摊销、power control 不可用或 sequential kernel 已饱和时，
  默认 Megatron / Nanobatching / Perseus 仍分别是更简单方案。
- **Evolution / ROADMAP / Adjacent Chapters:** `Direct Evolution`：sequential max-frequency execution →
  off-critical-path DVFS（dynamic energy）与 nanobatch overlap（static energy）两条分支 → joint
  frequency/SM/launch scheduling → explicit time-energy frontier。主 owner `TRAIN-MEGATRON`（当前 Ch40，
  legacy Ch36），邻接 communication、pipeline 与 Cost；已读 owner 与相邻章节。
- **Integration Decision:** `Integrate — New Mechanism`；已在 Ch40 把 launch timing、SM partition 与
  frequency 写入 time–energy Pareto execution plan；Cost 章节只保留 outcome/accounting handoff。
- **Open Questions:** frontier 何时因 thermal/driver/model/parallelism drift 失效；multi-node ranks 采用不同
  frequency 时怎样保持 collective progress；job-level carbon/power cap 怎样映射为 per-partition target；
  profiler 自身能耗和 32 GPU-hours search cost 何时可以摊销？

### Faramesh

- **Candidate / Week / Score:** Faramesh / 2026-W04 / 26/30；
  `Source Family ID: faramesh-action-authorization-boundary`；`Status: Emerging`。
- **Source Type / Dates / Revision / Artifact:** arXiv primary preprint v1，首次公开 2026-01-25；本轮访问
  2026-08-07。作者报告实现了 micro-benchmark harness，但论文和 arXiv metadata 均未提供公开代码、
  artifact 或外部部署，故实现与数值只能按作者实验记录，不能独立复现。
- **Full-read Coverage:** 已阅读 metadata、Introduction/Related Work、reproducible micro-evaluation、
  security invariants、AAB/CAR definition、canonical schema、enforcement state machine、deployment/
  consistency/failure semantics、decision artifact lifecycle、provenance/replay、synthetic evaluation、
  baseline comparison、complexity、alternative architectures、system implications、Limitations/Future Work，
  以及 state-machine/CAR examples 等 Appendices。未披露真实 production trace、外部 red team、跨节点
  governor 实现、durable ledger artifact、key management 或 independent replication。
- **Original Problem / Previous Design / Changed Constraint:** IAM/RBAC、API gateway、prompt guardrail、
  tool-local validation 与事后 logs 各自合理：它们分别管理 principal、transport、模型行为、局部业务
  约束和效果证据。但 autonomous agent 可以经不同 framework/protocol 产生语法不同而效果相同的
  action，并在 retry、并发、policy/state 变化中产生真实副作用；若没有 effect 前的共同 gate，日志无法
  反推出“哪一版 policy 基于什么 state 允许了哪个具体 action”。
- **Mechanism / State Ownership:** agent 先产生 intent `I`；canonicalizer 丢弃非 authoritative reasoning，
  提取 Actor、Target、Operation、Resource、typed Parameters、Blast Radius 与 Context，规范 defaults、
  vocabulary 和字段顺序，得到 CAR `A` 及 digest `h=H(A)`。AAB 再确定性计算
  `Eval(A,P,S) -> PERMIT | DEFER | DENY`。Policy owner 拥有 `P`，authoritative systems 提供 evaluation
  state `S`，governor 拥有 decision/ledger，executor 只接受绑定实际 `h` 的有效 PERMIT artifact；model、
  planner 和 tool transport 都不拥有最终授权。
- **Control Flow / Artifact Lifecycle:** effectful path 必须经过 canonicalization→policy/state evaluation→
  append-only decision record→signed artifact validation→execution。artifact 可绑定 action hash、policy
  version、state digest、validity window 与 one-time constraint；过期、撤销、policy/state mismatch 或
  governor timeout/partition 必须重新评估、DEFER 或 DENY。相同 `(A,P,S)` 的并发请求由 `h` 对应的
  `NONE→PENDING→FINAL` ledger transition 合并；single-use action 还需 `Consumed(h)`。这是论文规定和
  prototype 行为，不是跨服务 exactly-once 的通用证明。
- **Provenance / Replay Semantics:** decision record 绑定 `(A,P,S,d,t,prev_hash)`；重放解析同一 canonical
  action、精确 policy version 与 state snapshot/digest，可验证当时 decision，或在新 `(P',S')` 下做
  counterfactual re-evaluation，而不重新运行非确定性 agent reasoning。它记录的是 authorization
  provenance，不等于远端 tool 的实际 outcome、事务 commit、compensation 或业务 reconciliation。
- **Implementation / Evaluation Contract:** 作者的 Python 3.11 单进程 governor 运行在 Apple M1
  8-core、32GB、NVMe/macOS，本地 append-only ledger；action 来自 8 类 synthetic tools，policy 数为
  64/256/1024、state digest 为 4KB/64KB/512KB、batch 1/8/32。主量化实验为 50,000 canonical actions、
  10 个 seeds；默认 256 policies、64KB state、batch 8。另有 10,000 次 intent determinism、各 10,000
  次 direct/alternate/cached bypass probes、50,000 次 stale-policy probes、64 workers 上 1,000,000 次
  duplicate requests，以及 500 个 DEFER waiters。
- **What the Evidence Proves:** 作者 harness 中，artifact-bound executor 能拒绝列明的 missing/mismatched/
  expired artifact probes，canonicalization 在构造的 semantic-equivalence variants 上产生稳定 hash，固定
  `(A,P,S)` 可重复 decision，ledger 可记录 decision provenance；默认单机路径报告 p50/p95 2.24/9.61ms。
  这些结果支持“action identity、authorization 与 provenance 应成为独立 execution contract”的机制价值。
- **What It Does Not Prove / Threats to Validity:** synthetic schemas 由同一作者定义，没有 production
  agents、真实 adversarial semantic mutation、外部 tool failure 或 independent baseline implementation；
  所谓 coverage、attack matrix 与 concurrency correctness 只验证 instrumented executor/harness。
  CAR 只能保证作者 schema 内的结构规范化，不能证明 action 忠实表达 latent intent 或现实后果；policy
  可能错误/不完整；canonicalizer、decision engine、signing key、ledger 与 executor compliance 一旦失陷，
  论文的不变量就不成立。正文也承认 mutable state 下完整消除 TOCTOU 需 global locking，并未给出跨
  region consistency、key rotation、revocation propagation、ledger recovery 或 Byzantine operator 证据。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** mandatory gate 将安全与 audit 变成
  execution precondition，却新增 canonical schema evolution、semantic alias/collision、policy/state snapshot
  freshness、signing/revocation、ledger growth、hot-key contention 和 control-plane availability；fail-closed
  又会把 governor outage 转成业务 outage。IAM/RBAC 仍定义主体/权限，gateway 仍控制 ingress，sandbox
  限制 capability，tool-local business validation 检查真实资源状态，workflow 负责 retry/approval/
  compensation，outcome logs 记录执行结果；AAB 是 layering，不是它们的替代品。
- **Evolution / ROADMAP / Adjacent Chapters:** `Layering / Dependency`：prompt/output guardrail 与 IAM →
  transport/tool-local checks → canonical action identity → mandatory effect-time authorization → decision
  provenance/replay。主 owner 为 `PLATFORM-SECURITY`（当前 Ch72，legacy Ch68），邻接 Monitoring /
  Governance；Agent 侧由 Tool Calling 落实 proposal/executor boundary，Workflow 拥有 durable approval、retry 与 outcome state。已核对 ROADMAP 与上述
  章节，现有正文已有基本边界，但尚未完整展开 decision artifact 的 identity/freshness/revocation contract。
- **Integration Decision:** `Integrate — New Mechanism / Status: Emerging`；已在 Ch72 写入 canonical typed
  action、decision artifact 与 effect-time authorization；因无公开 artifact 和 synthetic-only evaluation，
  不采纳性能数字。
- **Open Questions:** 谁验证 canonicalizer 对真实业务语义的 completeness；action/policy/state digest 的
  schema migration 如何兼容历史 replay；多 region governor 如何处理 revocation 与 stale reads；decision
  record 如何与真实 tool commit/outcome、compensation 和 incident evidence 建立不可混淆的关联？

### LLM-42

- **Candidate / Week / Score:** LLM-42 / 2026-W04 / 29/30；
  `Source Family ID: llm42-selective-deterministic-inference`。
- **Source Type / Dates / Revision / Artifact:** arXiv primary systems paper v1 首次公开 2026-01-25，v2 于
  2026-01-30 修订；本轮访问 2026-08-07，并以 v1 HTML 固定 W04 机制/实验边界。v1 已链接 Microsoft
  repository 但写作“will be available”；当前 repository 与 SOSP artifact 只用于核验后续公开实现，不倒算为
  1 月 25 日已完成 artifact evaluation 或 venue acceptance。
- **Full-read Coverage:** 已阅读 metadata/revision、Introduction/Background、floating-point 与 dynamic-
  batching root cause、batch/position invariance observations、DVR/grouped verification、KV repair、attention/
  collective/sampling constraints、offline/online evaluation、rollback/recomputation ablation、Related Work、
  Conclusion 与 Discussion/Limitations，并核对当前 repository 的 SGLang base、核心路径、默认 window/
  verify batch 和 artifact 入口。论文无独立 Appendix；跨硬件 bitwise equivalence 与 failure recovery
  未披露。
- **Original Problem / Previous Design / Changed Constraint:** 禁用 dynamic batching 最容易获得稳定 shape，
  batch-invariant kernels 则让 reduction order 不随 batch 变化；二者对 debugging/evaluation 很合理，却分别
  牺牲 serving utilization，或要求长期维护一套不能充分使用 split-K/shape-aware optimization 的 kernels。
  新约束是只有部分 evaluation/audit/CI traffic 需要 reproducibility，不能让一个 deterministic request 为
  同 batch 所有普通请求施加全局性能税。
- **Principle / Mechanism:** 论文区分 batch-invariant、shape-consistent 与 position-consistent reduction。
  Fast path 继续用普通 dynamic batching 逐 token Decode；对标记 deterministic 的请求，每积累固定窗口后，
  verifier 用固定总 token shape（末尾以 dummy tokens padding）并行重放候选。只提交从已知 consistent state
  开始、与 verifier 相同的最长前缀，再额外提交 verifier 产生的下一 token；首个 mismatch 后的 suffix 被
  丢弃，下一轮从 repaired boundary 继续。即使全部 mismatch，verifier 仍产生至少一个新 consistent token，
  形成 forward-progress 下界。
- **State Ownership / Commit Boundary:** scheduler 拥有 request 的 deterministic flag、candidate/verified
  length、group 和 rollback transition；verifier 是 deterministic reference execution。Fast-path token 在验证前
  不得流给用户；更关键的是 fast path 生成的 KV 即使 token 恰好相同，也可能包含数值漂移，所以 verifier
  KV 必须覆盖对应窗口，block table、committed token length、stream position 与 KV valid prefix 在同一边界
  原子前进。否则 token-level match 之后仍会从 stale KV 再次分叉。
- **Grouped Verification / Scheduling:** 小窗口降低一次 mismatch 的 rollback suffix，却使 verification
  memory-bound；大窗口提高 arithmetic intensity，却放大 recomputation。Grouped verification 把多请求的
  小窗口拼成固定大 shape，在保持 per-request 短 rollback 的同时摊薄 target forward。它把 verification
  变成与 Prefill/Decode 竞争 GPU 的第三类 iteration work，必须显式参与 priority、admission 与 SLO，而不
  能作为隐藏 post-processing。
- **End-to-end Determinism Contract:** 固定-shape GEMM/RMSNorm 只解决部分 reduction path。v1 prototype
  的 verifier attention 使用 FlashAttention-3 且 `num_splits=1`；collective 需要支持 consistent reduction 的
  multimem/NVLS，或在旧平台选择固定 NCCL tree/protocol/channel；随机 sampling 使用 seed-bound sampler。
  因此“同 prompt”还必须绑定 model/tokenizer、weights、precision、kernel/runtime/driver、parallel topology、
  attention/collective config、sampling parameters 与 seed。论文证明目标不是跨版本、跨 GPU 或跨 TP degree
  产生同一 bit pattern。
- **Implementation / Evaluation Contract:** prototype 基于 SGLang 0.5.3rc0，FA-3；性能实验只使用
  Llama-3.1-8B-Instruct、4×NVIDIA H100 PCIe 80GB、64-core host 与约 1.65TB DRAM。ShareGPT 与 ArXiv
  traces 加六组 synthetic length configurations；offline 每组 4,096 requests，deterministic traffic 从
  2% 到 100%；online 使用 ShareGPT、12/14/16/18 QPS；ablation 在 12 QPS、100% deterministic traffic
  下扫描 16～512-token windows 与 1～32-request verify groups。吞吐、E2E、TTFT、rollback 和 recomputed
  tokens 都只能在该 contract 内解释。
- **What the Evidence Proves:** 作者实验显示 selective deterministic traffic 减少时，DVR 的 overhead
  随之下降；在列明 offline configurations 中，相比全局 SGLang deterministic baseline 多数更快。作者还
  测得不同 workload 的 rollback 差异很大：100% deterministic 时 ArXiv recomputation 为 10.97%，而
  ShareGPT 为 0.32%，证明 window/group policy 必须 workload-aware，不能只引用最佳 throughput。
  correctness 另在 Qwen 系列与 1～4 GPUs 上测试，但性能只报告上述 Llama/H100 环境。
- **What It Does Not Prove / Limitations:** baseline 是同一 prototype 中的 SGLang deterministic/non-
  deterministic modes，没有与优化后的未来 batch-invariant stack、不同 GPU interconnect 或 production
  multi-tenant load 比较。当前 verification 会暂停所有 in-flight requests，Prefill 不任意 batching；作者
  明确报告 Prefill/Decode reduction 不一致，因此不支持同请求多轮或跨请求 prefix-cache sharing，也未与
  speculative decoding 组合。论文没有验证 process/GPU failure 中 candidate/verified KV 的 crash recovery、
  streamed-token retraction、PD 分离、preemption、quantization、MoE expert collectives 或 cross-version
  reproducibility。
- **Trade-offs / Previous Design Still Applies:** DVR 避免全面 kernel rewrite 与全局 determinism tax，却
  增加 unstreamed output buffer、verification queue/global pause、额外 target compute、KV overwrite、rollback
  memory/state、operator allowlist 和 deterministic configuration debt。全局 batch-invariant kernels 在全部流量
  都需稳定、prefix sharing 必须保留、rollback tail 不可接受或 verifier 会严重扰动 SLO 时仍是清晰分支；
  单请求/固定 batch 仍适合小规模 debugging。普通 non-deterministic path 对创意生成也仍然合理。
- **Evolution / ROADMAP / Adjacent Chapters:** `Principle Reuse`：disable batching → batch-invariant kernels →
  position-consistent fixed-shape verification → selective decode/verify/rollback → grouped verification。它借用
  Speculative Decoding 的 proposal/verify/rollback 结构，但目标是 reproducibility 而非减少 target serial
  steps，不能写成 classical draft/target 的直接替代。主 owner `INFER-CONTINUOUS-BATCHING`（当前 Ch46，
  legacy Ch42）的 iteration work/request policy，Speculative Decoding 只拥有 verification/KV transaction
  类比，邻接 Decode、SGLang 与 Evaluation。
  已读目标及相邻章节；现有调度和 rollback 原则原先尚未拥有 determinism
  contract 与 verified KV commit 这一独立机制。
- **Integration Decision:** `Integrate — New Mechanism`；已在 Ch46 写入 request-scoped selective
  determinism、fixed-shape verify、token/KV atomic commit 与 rollback boundary；没有把它误写成经典
  speculative sampling。
- **Open Questions:** 怎样在不全局暂停的情况下调度 verifier 并保护普通请求 tail SLO；verified KV overwrite
  如何与 paged blocks、preemption、PD transfer 和 crash recovery 组成事务；prefix-cache identity 能否包含
  reduction provenance；quantized/MoE/heterogeneous GPU 下哪些 operators 真正 position-consistent？

### Universal Load Balancing

- **Candidate / Week / Score:** A Universal Load Balancing Principle and Its Application to Large Language
  Model Serving / 2026-W04 / 25/30；`Source Family ID: bfio-sticky-barrier-load-balancing`；
  `Status: Emerging`。
- **Source Type / Dates / Revision / Artifact:** arXiv primary theory/systems preprint v1 首次公开
  2026-01-25，v2 于 2026-02-01 修订；本轮访问 2026-08-07，并以 v1 HTML 固定 W04 结论。当前 arXiv
  摘要属于 v2，出现 28% experimental energy reduction 与 52% fleet-scale claim；v1 正文的列明结果是
  simulation 中 396→383kJ（3.3%/3.4%）。这些 revision 数字不得倒灌进 W04。论文没有公开 simulator、
  router implementation 或 solver artifact。
- **Full-read Coverage:** 已阅读 metadata/revision、Introduction/Related Work、general workload model、
  FCFS baseline、short-lookahead BF-IO integer program、`H=0` theoretical specialization、homogeneous/
  geometric/non-decreasing drift theorems与 proofs、BurstGPT/proprietary trace说明、simulation、metrics/
  power model、Discussion/Limitations，以及 FCFS、proof、energy appendices。没有真实 serving deployment、
  implementation overhead、solver scaling、failure experiment、SLO/fairness ablation 或 independent replication。
- **Original Problem / Previous Design / Changed Constraint:** Round-robin/FCFS/JSQ 在无状态或 service time
  近似均匀时便宜且合理；若 request 可以迁移，错误 placement 也可后续修正。论文研究的变化是 PD 后
  Decode request 与增长中的 KV sticky 在一个 worker，而本地 attention 后还有跨 data-parallel workers 的
  barrier/model-parallel stage；每步耗时近似 `max_g local_load_g + sync`。request 数相同不代表 resident KV/
  token work 相同，早期 placement error 会长期制造 straggler 与 barrier idle。
- **Model / State Ownership:** 每个 request `i` 有未知 workload profile `W_i`；一旦分配到 worker `g(i)`，
  non-preemptive、non-migratable，直到 output 完成。Worker active set 拥有 resident KV，router 只维护
  current aggregate load `L_g(k)`、free slots 与 centralized waiting pool。目标不是最小 queue length，而是
  最小化 `G*max_g L_g - sum_g L_g`，即同步屏障下的 aggregate idle-work proxy。
- **Mechanism / Control Flow:** 每次 slot release/arrival decision，BF-IO 从 waiting pool 选择可填满当前
  capacity 的 requests，并在 binary assignment variables 上最小化未来 `h=0..H` 的累计 predicted imbalance。
  `H=0` 只看当前 workload，不需预测 output length；`H>0` 只需估计现有 active requests 在短窗口内的
  load/completion，而不是预测新请求完整 lifespan。短 horizon 可以预见即将释放的 capacity，过长 horizon
  则会被未知 arrivals 和未来 decisions 污染。
- **Theory Contract:** strongest LLM guarantee 只证明 `H=0` 相对论文定义的 FCFS。在 overloaded regime
  下，waiting pool 必须有足够 prompt-length diversity 来填充 free slots；prefill lengths 是 bounded i.i.d.
  non-degenerate distribution，output lengths 在核心模型中为 fixed 或 i.i.d. geometric，assignment sticky、
  no preemption，且 `sqrt(G)=o~(B)`。general theorem 仍要求所有 alive requests 共享 bounded、
  non-negative deterministic drift。`Omega(sqrt(B log G))` 是这些假设下 imbalance ratio 的 asymptotic
  lower bound，不是 throughput、energy 或任意生产 trace 的同倍率保证；`H=20` 没有同等 worst-case proof。
- **Implementation / Evaluation Contract:** evaluation 是 router simulator，不是 GPU-serving benchmark。
  request lengths 来自 BurstGPT，并称包含 proprietary industrial workloads，但 proprietary trace/distribution
  不公开。默认 `G=32` simulated GPU workers、per-worker batch `B=72`、revelation target `R=128`；每 step
  duration 被建模为 `C + t_l*max_g L_g`，所有 active requests 同步产生一个 token。比较 FCFS、JSQ、
  BF-IO `H=0/20`，报告多 seeds 的 imbalance、derived throughput/TPOT 与 modeled energy。
- **Energy Evidence Boundary:** energy 并非 32 GPUs 的实机 measurement，而是把 simulated throughput
  映射到 MFU，再套用 `P_idle=100W`、`P_max=400W`、`mfu_sat=0.45`、`gamma=0.7` 的 power-utilization
  function 积分。v1 的 BF-IO `H=20` 相对 FCFS 报告 throughput +14%、TPOT -13%、energy -3.3%，只能
  作为该 simulator/power model 的作者结果。论文开头的 3-minute、436-step proprietary trace 说明真实
  imbalance 现象，不等于 BF-IO 已在该生产系统端到端部署。
- **What the Evidence Proves:** 数学部分证明在明确 stochastic/sticky/overload model 内，用 resident
  workload 而非 request count 做 admission placement 可系统性降低 barrier imbalance；simulation 说明短期
  active-state signal在 BurstGPT-derived workload 中优于论文实现的 FCFS/JSQ。这支持长期原则：对
  barrier-synchronized stateful workers，routing state 应表达未来几步的 resource contribution，而不只是
  queue cardinality。
- **What It Does Not Prove / Threats to Validity:** BF-IO pseudocode 枚举 feasible allocations，但论文未
  报告实际 integer solver、近似算法、调度 latency 或大 waiting pool 的复杂度；因此“millisecond production
  router 可用”未被验证。step-time linearity忽略 kernel shape、continuous batching、attention implementation、
  EP token skew、communication overlap、KV paging/offload、heterogeneous GPUs 与 network tail。也未比较
  locality-aware routing、KV migration/rebalancing、preemption、tenant fairness 或 SLO-aware policies。当前
  v2 摘要的更大能源数字需要按 v2 独立 source packet，不能用 v1 支持。
- **Trade-offs / Previous Design Still Applies:** workload-aware centralized placement减少 barrier idle，却
  新增全局 load freshness、waiting-pool buffering、optimization latency、prediction/calibration 与 single control
  point；延迟 dispatch 还可能恶化 TTFT。Centralized pool 不存在、requests 立即进入 per-worker FIFO、
  workload non-monotone、migration便宜、worker heterogeneous 或 fairness/deadline 优先时，theory 不直接适用。
  FCFS/RR 在低负载、均匀短请求、无跨 worker barrier 或观测成本高时仍是更简单分支；KV-aware routing 与
  BF-IO 还需联合权衡 locality 与 load，不能彼此替代。
- **Evolution / ROADMAP / Adjacent Chapters:** `Direct Evolution` within routing policy：request-count
  balancing → current resident-work balancing → short active-work lookahead under sticky state；与 KV migration/
  preemption 属 alternatives。主 owner `INFER-SCHEDULING`（当前 Ch56，legacy Ch52），邻接 distributed
  state-aware selection、endpoint picker、PD sticky handoff 与 Cost。已读 owner 与相邻章节。
- **Integration Decision:** `Integrate — New Mechanism / Status: Emerging`；已在 Ch56 写入
  barrier-synchronized resident-work placement，并明确 simulator、solver overhead、sticky/non-preemptive
  假设和生产验证边界。
- **Open Questions:** 可部署的近似/solver 怎样在 routing deadline 内工作；load snapshot stale 时 decision
  是否稳定；KV locality、migration cost、EP skew、fairness 与 deadline 怎样进入 objective；对 non-monotone
  hybrid state、speculative rollback 和异构 workers，理论中的 common drift 能否放宽？

### CooperBench

- **Candidate / Week / Score:** CooperBench / 2026-W04 / 26/30；
  `Source Family ID: cooperbench-agent-coordination`。
- **Source / Coverage:** arXiv:2601.13295v1，2026-01-19。已阅读 652-task construction、container/test
  pipeline、OpenHands communication runtime、Solo/Coop/agent-count experiments、communication ablation、
  failure taxonomy、human validation 与 appendices。
- **Problem / Previous Design / Changed Constraint:** 把两个 feature 串给一个 Agent 会牺牲并行度但保留
  单一 world state；两个 Agent 并行可分摊工作，却必须协调 overlapping code、接口承诺与 merge order。
  新约束不是“能否写代码”，而是双方只有部分 specification 且异步修改共享 repository。
- **Mechanism / Ownership / Flow:** 两个 OpenHands agents 各自在隔离 container 中实现自己的 feature，
  通过 SQL-backed asynchronous message tool 协调；最终 patches 先由 `git merge-file` 合并，trivial conflict
  可由 Qwen3-Coder-1.5B resolver 处理，再运行双方 expert-written tests。agent 持有 local history/patch，
  repository base、messages、merge result 与 tests 分属不同 state owner，不能把“发过消息”视为 commit。
- **Evaluation Contract / Evidence Boundary:** 12 repos、4 languages、199 features、52 pools、652 pairs；
  77.3% gold solutions 有重叠，features 平均约 52.3 changed lines/1.4 files。比较 GPT-5、Claude Sonnet 4.5、
  MiniMax-M2 与两个 Qwen variants；四 Agent scaling 仅 46 tasks/3 sets。结果支持该 harness 下存在 Solo-
  Coop gap、通信可降 textual merge conflicts却未显著提高端到端 success；不证明 Agent 天生不能协作，
  也不隔离更强 transactional workspace、typed protocol 或 supervisor 的收益。
- **Trade-offs / Evolution / Decision:** 自由自然语言协作给出灵活性，却带来重复、unresponsiveness、
  unverifiable claims、broken commitment 与 divergent architecture；严格 workflow/lock/typed handoff 在
  低灵活性下可提供更强一致性。`Direct Evolution`：parallel workers→message passing→verifiable
  commitment/shared-state protocol。主 owner `AGENT-MULTI-AGENT`（当前 Ch82，legacy Ch78），邻接
  Workflow / Agent Platform；`Integrate — New Mechanism`。已在 Ch82 写入 base revision、typed proposal、
  reservation/conflict detection、verified patch/tests 与 atomic commit/rebase contract。

### Jet-RL

- **Candidate / Week / Score:** Jet-RL / 2026-W04 / 28/30；
  `Source Family ID: fp8-rl-policy-numerics`。
- **Source / Coverage:** arXiv:2601.14243v1，2026-01-20。已阅读 BF16-train/FP8-rollout failure analysis、
  compute-graph alignment、quantization granularity、kernels、RL setup、long-rollout/challenging-task experiments、
  throughput breakdown 与 appendix。
- **Problem / Previous Design / Changed Constraint:** BF16 training + FP8 rollout 看似兼顾 convergence 与
  generation speed，且对 short/easy rollouts 近似成立；但 policy 每步更新、8K～16K trajectories 会累积
  numerical divergence，使“同一 weights”在 trainer 与 rollout engine 中成为不同 behavior policy。
- **Mechanism / State Ownership / Flow:** Jet-RL 令 inference graph 成为 training-forward graph 的子图，
  统一 weight/activation 的 precision 与 granularity；保留 BF16 master weights/gradient transport，FProp、
  DGrad、WGrad 用 FP8 GEMM，weights 128×128 block，activation/gradient 1×128 group。rollout/trainer
  同步的不再只是 parameter version，还包括 quantization recipe/kernel identity。
- **Evaluation Contract / Boundary:** Qwen2.5/Qwen3 dense settings、GSM8K/MATH500/GPQA/SuperGPQA，
  4K/8K/16K rollout；作者报告 rollout、training 与 end-to-end speedup。即使 Jet-RL 在列明设置更稳定，
  表中 16K 某些任务仍低于 BF16；不证明所有 FP8 formats、MoE、optimizer、hardware 或 RL objective
  on-policy，也不能把 numerically closer 等同 trajectory identical。
- **Trade-offs / Evolution / Decision:** 统一低精度减少 mismatch/calibration，却扩大低精度到 training
  forward/backward，新增 master-copy、scale update、kernel coverage、overflow/underflow 与 checkpoint
  compatibility；BF16 在敏感任务/缺少成熟 FP8 kernel 时仍合理。`Direct Evolution`：rollout-only FP8→
  precision-flow contract。主 owner `TRAIN-GRPO`（当前 Ch33，legacy Ch29），邻接 RLHF、Distributed
  Training 与 Quantization；`Refine — Existing Argument`。已在 Ch33 将 policy identity 从 weight version
  扩展到 precision、granularity、kernel/runtime recipe，并保留 BF16 分支。

### LongCat-Flash-Thinking-2601

- **Candidate / Week / Score:** LongCat-Flash-Thinking-2601 / 2026-W04 / 27/30；
  `Source Family ID: longcat-agentic-training-dora`。
- **Source / Coverage:** arXiv:2601.16725v1，2026-01-23。已阅读 model/training stages、environment synthesis、
  multi-domain DORA、noise curriculum、Heavy Thinking、Zigzag Attention、benchmarks 与 appendices。报告没有
  独立 Limitations / Threats 章节，硬件、并发/SLO 与大量训练成本 `Not Disclosed`。
- **Problem / Mechanism:** 静态文本 pretraining 不含充足 tool/environment interaction；同步 RL 又被
  long-tailed multi-turn environment latency 拖慢。报告先用 contextually/environmentally native trajectories
  做 mid-training，再用 RolloutManager→SampleQueue→Trainer 的多版本异步 DORA 承载最多 32K concurrent
  environments；按历史 pass rate 对低吞吐/高难 domain oversample，使 per-domain contribution 与
  asynchronous throughput 折中。随后渐进注入 instruction/tool noise，而不是假设 perfect environment。
- **State / Evidence Boundary:** queue 必须同时拥有 policy version、domain、task difficulty、environment
  outcome 与 advantage group；oversampling 近似 dynamic budget，不等于无偏 sampling。560B total/27B
  activated、20+ domains、公开 agent benchmarks 与 noisy variants 支持作者 model family 的综合效果，
  但 end-to-end co-design 无法把提升唯一归因 DORA、noise curriculum 或某个 architecture；厂商 benchmark
  不可外推为通用训练定律。
- **Trade-offs / Evolution / Decision:** 多域异步提高覆盖/利用率，却新增 staleness、domain mixture drift、
  rare-domain backpressure、verifier bias 与 environment security；同步小规模 RL 在 freshness/可审计优先时
  仍成立。`Layering / Dependency`：text mid-training→environment-native data→async multi-domain RL→
  noise curriculum。主 owner `TRAIN-GRPO`（当前 Ch33，legacy Ch29），邻接 Pretraining、RLHF 与
  Multi-Agent；`Refine — Existing Argument`。已把 domain mixture、oversampling 与 environment noise
  写入异步 rollout 的 provenance/budget contract，没有把厂商综合 benchmark 归因给单一机制。

### SWE-Pruner

- **Candidate / Week / Score:** SWE-Pruner / 2026-W04 / 25/30；
  `Source Family ID: swe-pruner-task-aware-context`。
- **Source / Coverage:** arXiv:2601.16746v1，2026-01-23。已阅读 dataset synthesis、goal hint、0.6B neural
  skimmer/CRF、adaptive threshold、tool middleware、four-benchmark experiments、baselines、latency、
  cross-model appendix 与 limitations；公开 code/model 存在。
- **Problem / Mechanism:** coding agent 的 read/search output 占大量 tokens；token-level compression 会破坏
  syntax，coarse RAG 会漏局部 dependency。Agent 先把当前 goal 变成 focus hint；wrapper 保留原 tool
  contract，在 hint 存在时让 0.6B skimmer按 query-conditioned line relevance 选择完整 code lines，动态阈值
  在压缩率与 confidence 间调节，无 hint 则 bypass。
- **Evaluation Contract / Boundary:** Qwen3-Reranker-0.6B，8 GPUs、batch128、3 epochs；Mini-SWE-Agent
  等 harness、Claude Sonnet 4.5/GLM-4.6，SWE-Bench Verified、SWE-QA、LongCodeQA/completion。作者报告
  23～54% token reduction 与单轮最高 14.84× effective compression；不能外推到其他语言、runtime tool、
  adversarial code、跨 turn stale goal 或所有 success-rate preservation。latency <100ms 只属于列明 setup。
- **Trade-offs / Evolution / Decision:** task-aware pruning降低 context cost，却引入 hint correctness、false
  negative、line-dependency break、versioning与 extra model latency；raw tool output 在 debugging/audit 或
  uncertainty高时仍需可恢复。`Direct Evolution`：raw context→generic compression→goal-conditioned structured
  pruning。主 owner `AGENT-CONTEXT`（当前 Ch75，legacy Ch71），邻接 Monitoring、RAG 与 Tool Calling；
  `Integrate — New Mechanism`。已在 Ch75 写入 goal-conditioned line pruning、versioned hint 与 raw-artifact
  fallback。

### Endless Terminals

- **Candidate / Week / Score:** Endless Terminals / 2026-W04 / 24/30；
  `Source Family ID: endless-terminals-procedural-environments`。
- **Source / Coverage:** arXiv:2601.16443v1，2026-01-23。已阅读 four-stage environment generation、
  Apptainer/Harbor conversion、verification/solvability filtering、PPO training、three model families、
  TerminalBench evaluation、failure analysis 与 limitations。
- **Problem / Mechanism:** curated terminal tasks 可靠但难扩展，teacher distillation 带来成本与 capability
  ceiling。pipeline 生成 task spec→构建 container/prerequisite tests→生成 hidden completion tests→用 o3
  pass@16 过滤可解性；Agent 每 turn 输出一个 non-interactive command，episode 由 done/16 turns/16K tokens
  结束，最终 container state 由 hidden tests 判分。
- **Evaluation / Boundary:** 3,255 Apptainer tasks、约 2,500 Harbor；Llama3.2-3B、Qwen2.5-7B、Qwen3-8B，
  PPO；TerminalBench2.0 用 64 turns/sliding context并五次运行。best setup 仅 6.7%，failure 以 loop/turn
  exhaustion 为主；filter 丢掉约一半 o3 16 次皆失败候选，因而同时删除 invalid 与可能超越 teacher 的任务。
  procedurally generated specs 更像 competitive programming，不代表 messy user terminal work。
- **Trade-offs / Evolution / Decision:** executable verifier提高 scale/correctness，却把训练分布绑定 generator、
  container可构建性、teacher ceiling 与 hidden tests；human tasks 在 ambiguity/clarification/security上仍不可替代。
  `Direct Evolution`：curated env→procedural executable env→RL feedback。主 owner `TRAIN-DATA`（当前
  Ch27，legacy Ch23），邻接 Evaluation / Tool Calling；`No Change — Already Covered`。Ch27 已有生成、
  过滤、可执行 verifier、teacher ceiling 与 data-lineage 机制，本候选没有形成新的长期缺口。

### Least-Loaded Expert Parallelism

- **Candidate / Week / Score:** LLEP / 2026-W04 / 28/30；
  `Source Family ID: llep-dynamic-expert-spill`。
- **Source / Coverage:** arXiv:2601.17111v1，2026-01-23。已阅读 routing imbalance characterization、latency/
  memory model、LLA/LLAS algorithms、backward path、Torch/NCCL implementation、synthetic and full-model
  evaluation、SFT experiment、sensitivity/appendix。无独立 limitations 章节，failure recovery `Not Disclosed`。
- **Problem / Mechanism:** 标准 EP 假设 router load 足够均衡，local experts 固定可避免每步搬 weights；
  domain specialization让某些专家长期/逐 batch 过载时，All-to-All 后最重 GPU 决定 barrier 且可能 OOM。
  LLA 按 expert load 降序，将 native capacity 之外的 token spill 到 least-loaded GPU，并生成对应 expert-
  weight P2P transfer；cost/memory threshold 只有 transfer 便宜时才触发，backward 把 spilled-weight gradients
  回送 native owner 累加。低 imbalance ratio 直接走 standard EP fast path。
- **Evaluation Contract / Boundary:** Torch NCCL All-to-All/P2P、Python planner；8×H200，synthetic routing
  覆盖 gpt-oss-120B/DeepSeek-V3/Kimi-K2 shapes，per-GPU batch 32K/16K；真实 gpt-oss-20B/120B +
  Megatron-Math，并有 ZeRO-3/CPU offload SFT。MoE-layer最高约 6.1×、full model最高 2.2×/1.88×、SFT
  1.25×均绑定这些 load/hardware。planner、weight transfer、topology与 grouped-GEMM choice在平衡负载可抵消收益。
- **Trade-offs / Evolution / Decision:** 精确 computation 不改 token-expert semantics，却新增 per-batch global
  load collection、plan/weight movement、temporary memory、gradient return、epoch/failure recovery；静态 EP
  在平衡或慢互联时仍合理，expert replication 在热点稳定且有余量时可摊 amortized cost。`Direct Evolution`：
  static EP→replication/capacity→dynamic token+weight spill。主 owner `TRAIN-DISTRIBUTED-TRAINING`
  （当前 Ch36，legacy Ch32），邻接 MoE、Megatron 与 Resource Scheduling；`Integrate — New Mechanism`。
  已写入 per-batch token/weight spill、gradient return、cost threshold 与静态 EP/replication 共存边界。

### Agentic Search in the Wild

- **Candidate / Week / Score:** Agentic Search in the Wild / 2026-W04 / 25/30；
  `Source Family ID: agentic-search-log-dynamics`。
- **Source / Coverage:** arXiv:2601.17617v1，2026-01-24。已阅读 log source/sessionization、privacy plan、
  intent/transition classifiers、benchmark-overlap test、CTAR metric、temporal analyses、discussion、prompts
  与 appendices。v1 说 logs “plan to release”；后续 release 不倒算为 W04 artifact。
- **Problem / Mechanism:** benchmark success隐藏 search trajectory 的重复、pivot 与 evidence reuse。作者从
  DeepResearchGym 14.44M requests/3.97M sessions sessionize logs，用 LLM 标注 declarative/procedural/
  reasoning intent及 repetition/specialization/generalization/exploration moves；CTAR 统计新 query terms 是否
  可追溯到累积 retrieved evidence，形成 workflow sensor而非新的 search policy。
- **Evidence Boundary / Trade-offs:** <0.4% benchmark-similar query 支持 logs 不只是四个 benchmark replay；
  但只有一个 API/provider population，session cutoff、lexical CTAR 与 LLM taxonomy 都是 proxy。54% term
  traceability不证明 evidence被正确理解，repetition也可能是合理 retry。PII scrub/anonymization减少风险，
  但保留 sequence/intent 仍有 residual privacy 与 selection bias。
- **Evolution / Decision:** 固定 retrieval budget 简单；intent/trajectory-aware budget可能节省成本，却新增
  classifier error、gaming、state与 escalation threshold。`Principle Reuse`：single-query IR metrics→session
  dynamics→evidence-grounded control signal。主 owner `PLATFORM-MONITORING`（当前 Ch67，legacy Ch63），
  邻接 Evaluation、Cost 与 Workflow；`Integrate — New Mechanism`。已写入 versioned sessionization、
  trajectory sensor、CTAR proxy boundary 与高基数隐私约束。

### Fast KVzip

- **Candidate / Week / Score:** Fast KVzip / 2026-W04 / 27/30；
  `Source Family ID: fast-kvzip-learned-eviction`。
- **Source / Coverage:** arXiv:2601.17668v1，2026-01-25。HTML unavailable，已阅读 v1 PDF 的 formulation、
  offline gate-label generation、sink-attention architecture、prefill/decode integration、12-dataset evaluation、
  baselines、architecture/sensitivity ablations、latency/memory、appendices 与 limitations；source code可用。
- **Problem / Mechanism:** runtime KV importance计算可精确但本身增加 prefill/attention overhead；static
  recency/sink eviction便宜却不随 input/task变化。Fast KVzip 用 frozen LLM 的 context reconstruction
  attention生成 per-KV importance labels，只训练每层低秩 sink-attention gate；运行时从当前 hidden state
  预测 future-use score，保留 local window并按 score eviction，避免再次跑 full runtime compressor。
- **Evaluation Contract / Boundary:** Qwen2.5-1M、Qwen3 dense/MoE、Gemma3等，12 retrieval/QA/code/
  reasoning datasets；gate training约 0.59～0.83 H100-hours、0.11～0.30GB（列明三模型），S=16、D'=16。
  30% cache ratio near-lossless 是归一化作者结果，不保证所有 sequence/attention drift、concurrency、
  prefix sharing或 serving SLO；论文 future work 也承认 structured hardware execution尚未形成。
- **Trade-offs / Evolution / Decision:** offline learned gate移除在线 compression cost，却引入 model/checkpoint/
  adapter耦合、label bias、irreversible false eviction与 gate kernel；FullKV 在 correctness-first/短上下文仍成立，
  CPU recall/tiering 在可恢复性更重要时是另一分支。`Direct Evolution`：online importance compression→
  distilled lightweight eviction predictor。主 owner `INFER-KV-CACHE`（当前 Ch45，legacy Ch41），邻接
  Compression / Engine；`No Change — Already Covered`。Ch45 已由 W03 KVzap 形成 offline learned
  importance、runtime lightweight gate 与 irreversible-error contract；这里只作为独立证据入口。

### RM-RF

- **Candidate / Week / Score:** RM-RF / 2026-W04 / 23/30；
  `Source Family ID: rm-rf-run-free-unit-test-proxy`。
- **Source Type / Dates / Revision / Artifact:** arXiv primary paper v1 首次公开 2026-01-19，已接收
  SANER 2026；无后续 revision。作者公开代码与数据，但本轮结论以论文给出的 execution-label pipeline、
  holdout 与 limitations 为界，不把 repository existence 当作独立复现。
- **Full-read Coverage:** 已阅读 metadata、Introduction/Related Work、dataset construction、三类 label、
  model/tuning setup、validation/holdout、execution comparison、rank correlation、Discussion、Limitations、
  Conclusion 与 artifact 声明。论文没有报告并发或 serving SLO，记为 `Not Disclosed`。
- **Original Problem / Previous Design / Changed Constraint:** compile、execute、coverage 与 mutation testing
  提供最接近实际语义的反馈，因此作为 generated-test verifier 是合理旧方案；但在大规模 test generation
  或 RL sampling 中，逐候选构建与运行成本过高。变化后的约束是需要低延迟密集反馈，同时又不能把
  “看起来像正确测试”误当成已执行正确性。
- **Mechanism / State / Data Flow:** 作者先在 Java、Python、Go repository 中把 focal code、existing tests
  与 generated addition 送入真实 build/test/coverage/mutation pipeline，得到 correctness、coverage delta、
  mutation-kill delta label；随后让 code model 只读 source/test text，预测 binary 或 continuous target。
  该模型拥有的是从训练分布学到的 proxy score，不拥有 compiler、runtime、filesystem 或 mutation state，
  因而不能提交 executable correctness。
- **Implementation / Evaluation Contract:** 数据集共 22,285 samples，repository-disjoint validation 1,192；
  候选来自人工与 Qwen2.5-Coder 生成，超 30 秒执行被排除。比较 Qwen2.5 1.5B/7B/14B 与
  Codestral-22B 的 zero-shot、full SFT 或 LoRA；论文列明 A100、BF16、Adafactor。Qwen2.5-Coder-7B
  fine-tuned 在三目标上的平均 weighted F1 约 0.69；holdout 结果按语言与目标波动，mutation prediction
  尤其不稳定。跨六个 test-generating models 的 useful-test aggregate ranking 与 execution 的总体
  Spearman 为 0.74，但逐语言仅 0.4～0.6。
- **Evidence Boundary / Limitations:** 结果支持该 proxy 可在作者三语言、公开 repository 与过滤后样本中
  做排序或预筛；不证明它能替代 per-test execution、捕获 environment/flake/security/side effect，或在
  新框架、新语言和私有代码上保持 calibration。作者明确承认只覆盖三语言、未做 per-language specialist、
  未把 RM-RF 放入 RL loop，并存在 pretraining contamination 风险；论文把“substitute full-scale test
  runs”写得比现有证据更强，Weekly 不采纳该外推。
- **Trade-offs / Evolution / Previous Design Still Applies:** `Layering / Dependency`：executable verifier →
  learned proxy triage → selective execution。proxy 省下平均筛选成本，却引入 distribution drift、false
  accept、calibration 与 reward hacking；因此 compile/run/mutation 仍应拥有最终 gate，RM-RF 只能决定
  哪些候选优先执行或提供低权重 dense reward。
- **ROADMAP / Integration Decision:** 主 owner `PLATFORM-EVALUATION-SYSTEM`（当前 Ch66，legacy Ch62），
  邻接 SFT、GRPO 与 Workflow；
  `Weekly Only — Experimental Proxy`。Ch62 已有 scorer 与 executable evidence 分层，本候选强化边界但
  暂不构成新的长期机制缺口，不修改 Books。
- **Open Questions:** repository/语言迁移时怎样校准 operating point；怎样用 uncertainty 触发真实执行；
  proxy 与 executable verifier 的 sampling budget 如何在 RL 中避免 reward hacking？

### Fission-GRPO

- **Candidate / Week / Score:** Fission-GRPO / 2026-W04 / 27/30；
  `Source Family ID: fission-grpo-on-policy-error-recovery`。
- **Source Type / Dates / Revision / Artifact:** arXiv v1 首次公开 2026-01-22；v2 于 2026-04-20 修订并
  被 ACL 2026 Main 接收。W04 事件日期按 v1 固定，本轮用 v2 HTML 核验完整方法、实验、limitations 与
  appendix；后续 revision 不是新的 W04 事件。
- **Full-read Coverage:** 已阅读 metadata、Introduction/Related Work、GRPO objective、reward design、
  三阶段 fission loop、error simulator、LIFO buffer、corrective resampling、dataset/training、三组 benchmark、
  baselines、error-recovery decomposition、feedback/simulator/trigger ablation、compute-matched comparison、
  case study、Evaluation Scope、Computational Overhead、Conclusion 与算法/训练曲线 appendices。
- **Original Problem / Previous Design / Changed Constraint:** 普通 GRPO 用 group reward 提升基础 tool-call
  accuracy，保持简单且完全 on-policy；离线纠错数据也便宜稳定。但 sparse failure reward 丢失“为什么错”，
  静态错误集又会落后于持续变化的 policy failure distribution。新约束是多轮工具执行中的错误状态依赖
  当前 policy、dialogue 与 runtime feedback，训练必须同时学习诊断与恢复，而非只惩罚失败终局。
- **Mechanism / State Ownership / Control Flow:** Stage 1 按 GRPO 生成并更新；Stage 2 从失败 trajectory
  识别 format/function/parameter error，由 fine-tuned Error Simulator 结合 ground-truth call 生成受约束的
  runtime-like feedback，将原 context、failed call 与 feedback 组成 corrective context，以
  `(x, failed trajectory)` 去重并写入 LIFO buffer；Stage 3 从最新错误弹出 batch，对每例采样多个 recovery
  rollouts，再以更有信息量的组内 advantage 更新当前 policy。LIFO 与 trigger interval 是保持近似
  on-policy 的显式 freshness/compute contract，不是无成本的数据增强。
- **Implementation / Evaluation Contract:** 630 条经 Claude Sonnet 4 生成/过滤并由 Qwen3-235B 与
  Kimi K2 一致核验的训练 instances；Error Simulator 由约 2K error logs 训练。Qwen3 1.7B/4B/8B，
  Verl，单节点 8×H800 80GB，LR 1e-6、batch 8、每 query 8 rollouts、prompt 12,800、response 4,096；
  BFCL v4 Multi-Turn、TAU-Bench、TAU2-Bench，并与 GRPO、DAPO、Dr.GRPO、AWPO 等比较。
- **Evidence Boundary:** 作者实验支持在上述 synthetic-data/benchmark contract 下，8B 的 BFCL overall
  从 GRPO 42.75% 到 46.75%，error-recovery rate 平均提升 5.7 points；static-feedback 与 dynamic-feedback
  ablation 表明“从失败 context 重采样”和“精确反馈”分别贡献增益，compute-matched test 表明不只是更多
  update。它不证明真实 side-effectful tools、web/code environment、开放世界 schema 或长期 policy drift
  下的 recovery；simulator quality 还部分依赖 Claude judge，ground-truth call 也未必在生产环境可得。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** fission 把失败变成 dense corrective
  supervision，却新增 simulator hallucination/leakage、LIFO starvation、错误分类 bias、额外 `G'` rollouts、
  trigger scheduling 与 recovery overfitting。作者明确承认范围只覆盖 tool-calling benchmarks；真实 API
  越昂贵，绝对开销越大。错误稀少、反馈不可信或 environment side effect 不可安全 replay 时，普通 GRPO、
  offline curated repair 或 runtime compensation 仍更合理。
- **Evolution / ROADMAP / Integration Decision:** `Direct Evolution`：terminal sparse reward → offline
  correction traces → current-policy error interception → freshness-aware corrective resampling。主 owner
  `TRAIN-GRPO`（当前 Ch33，legacy Ch29），邻接 Tool Calling、Reflection 与 Workflow；
  `Refine — Existing Argument`。已在 Ch33 写入 failure-derived LIFO corrective branch、freshness 与
  simulator provenance；它是训练时 failure ownership，不等价于部署时 reflection/retry。
- **Open Questions:** 无 ground-truth call 时 feedback 如何获得可信 verifier；LIFO 如何避免旧但高风险错误
  永久饥饿；simulator、policy 与 tool schema 分别升级时如何做 provenance、rollback 与 regression gate？

### Memorization Dynamics in Knowledge Distillation

- **Candidate / Week / Score:** Memorization Dynamics in Knowledge Distillation / 2026-W04 / 26/30；
  `Source Family ID: kd-memorization-dynamics`。
- **Source Type / Dates / Revision:** arXiv primary research paper v1 首次公开 2026-01-21，无后续 revision；
  本轮访问 2026-08-07。论文无独立 Limitations / Threats 章节，未公开完整 training hardware/compute，
  对应字段记为 `Not Disclosed`。
- **Full-read Coverage:** 已阅读 metadata、Introduction、KD 与 extraction definitions、Pythia/OLMo-2/Qwen-3
  setup、FineWeb/WikiText/Nemotron experiments、memorization overlap、cross-seed/model-family analysis、
  pre-distillation classifier/filtering、entropy/log-prob mechanism、soft/hard KD、Related Work、Conclusion，
  以及跨模型/数据、classifier、pretraining-distillation appendices。
- **Original Problem / Previous Design / Changed Constraint:** hard-label cross-entropy 对 SFT 很自然，因为
  target 明确、teacher logits 常不可得；KD 通常也首先为 capability transfer 与 compression 服务。但大
  teacher 可能记忆训练样本，问题从“学生能否复现能力”扩展为“学生继承了哪类记忆，以及 objective 如何
  改变泄漏风险”。
- **Mechanism / State / Experimental Design:** 主设置以 1M 条、长度 256 的 FineWeb 样本训练 Pythia
  12B teacher 与同尺寸 1.4B baseline/student；baseline 用 cross-entropy，soft student 用 KL 匹配完整
  teacher distribution。memorization 用给定 prefix 后逐字 extraction 判定，并比较 teacher、baseline、
  student 的交集；扩展到 OLMo-2、Qwen-3、WikiText 与 Nemotron。作者再用 zlib entropy、teacher/baseline
  perplexity 与 KL feature 训练 logistic classifier，预测高风险样本并在 distillation 前过滤。
- **Evidence / Mechanism Boundary:** 在列明设置中 student 的 memorization rate 低于同尺寸 baseline：
  Pythia FineWeb 0.07% vs 0.17%，OLMo-2 0.09% vs 0.40%，Qwen-3 0.26% vs 0.86%；同时 validation
  loss/PPL 更优。entropy/log-prob 分析支持一个机制解释：hard one-hot loss 会迫使容量受限 baseline 对
  高 entropy 样本给出高置信，而 KL soft target 允许 student 保留不确定性。该分析是相关性加受控 objective
  对比，不是已经证明所有 KD 的因果定律。
- **Soft/Hard Trade-off:** hard sequence distillation 在 teacher logits 不可访问时仍合理；作者设置中其
  总 memorization rate 与 soft KD 相同，且下游效用优于 baseline，但它继承的 teacher-only difficult
  examples 数量是 soft KD 的 2.7 倍。因而演进不是“hard 被 soft 淘汰”，而是 logits access、capacity、
  utility 与 privacy inheritance 之间的选择。
- **Limitations / Failure Modes:** 样本、prefix/exact-extraction 定义、少数模型家族与受控 fine-tuning
  限定外推；没有 membership-inference/semantic regurgitation、真实私有语料、larger-scale production
  deployment 或完整硬件成本。预过滤从 1,698 降到 4 的 99.8% 是在同一数据/feature pipeline 内获得，
  不能当作通用 privacy guarantee；过滤也会改变数据分布并产生新的 memorized examples。
- **Evolution / ROADMAP / Integration Decision:** `Principle Reuse`：hard-label fitting → soft-distribution
  transfer → memorization-aware data gating。主 owner `TRAIN-SFT`（当前 Ch29，legacy Ch25），邻接
  Data、Pretraining 与 Security；`Integrate — New Mechanism`。已在 Ch29 写入 soft/hard KD 的不确定性、
  memorization inheritance 与过滤 trade-off，并明确 KD 不是隐私技术。
- **Open Questions:** extraction、membership inference 与 semantic leakage 如何联合评估；classifier 在
  teacher/data drift 后怎样校准；过滤高风险样本对 rare knowledge 与 tail utility 的代价是什么？

## Evidence Level

constitution 是官方行为规范；assistant axis、GIST 与 Sutradhara 的有效性来自作者实验。规范描述
desired behavior，不证明所有运行时轨迹都满足；表征方向不等同完整因果机制；Sutradhara 的
production-derived synthetic replay 也不等同真实工具、副作用和分布式故障下的生产验证；
HeteroCache 的作者实验只证明列明模型、数据、budget 与 PCIe contract，不证明通用 head taxonomy；
DataStates-LLM 的作者实验绑定 Polaris、DeepSpeed、Lustre 与列明 parallel layout，未验证故障恢复正确性。
StaleFlow 的 staleness invariant 是明确系统机制，但 convergence 仍是两个 base-model 短程实验，不能
外推为任意 `eta<=3` 的算法保证。
Scaling All-to-all 是可靠的 2025 CPU MPI 论文，但不是 2026 新事件，也没有直接 AI workload 证据。
Kareus 的 A100 实机结果证明特定 workload 的 time-energy frontier 增量；70B 仅为 emulation，GPU
energy 也不等于 whole-system/facility energy。
Faramesh 提供的是单机 synthetic harness 与形式化架构论证；其 CAR/AAB 能力、latency、coverage 和
dedup 数字不能外推为真实 Agent 平台、分布式 governor 或业务 exactly-once 保证。
LLM-42 的吞吐与 rollback 证据绑定 SGLang 0.5.3rc0、Llama-3.1-8B 和 4×H100 PCIe；额外 Qwen/多卡只
报告 correctness，没有相应性能 contract。确定性也只在固定 execution/sampling identity 内成立。
Universal Load Balancing 的理论只在列明 stochastic/overload/sticky assumptions 下成立；v1 serving
收益全部来自 simulator，energy 来自 modeled power curve，不能写成 32-GPU 实机节能或 fleet guarantee。
RM-RF 的 learned score 是 execution-derived proxy，不是 executable evidence；Fission-GRPO 的增益绑定
synthetic tool-call data、三个 benchmark 与 H800 training contract；KD memorization 结论绑定 exact
extraction、受控模型/数据与 objective，不构成通用 privacy guarantee。

## Cross-Week Deduplication

后续 persona selection、alignment 与 interpretability 工作若引用 assistant axis，应标记
`Direct Evolution` 或 `Layering` 的 primary evidence，不能仅因主题相似自动串联。
Sutradhara 与 Autellix、Parrot、Conveyor、KVFlow 等按 workflow visibility、clairvoyance、tool
semantics 与 cache ownership 去重，而不是笼统归为“Agent serving”。
HeteroCache 与 static eviction、ShadowKV/OmniKV、KV quantization 按 recoverability、retrieval
granularity、tier ownership 与 interconnect contract 去重；v2/ACL 只归入同一 1 月 20 日 source family。
DataStates-LLM 2026 与 2024 版本按 provider abstraction、serialization 和 persistent layout 的增量记录为
同一 source family 的直接演进，不能因标题相同删除，也不能把新版结果倒灌为旧版能力。
StaleFlow 与 synchronous VeRL、one-step pipeline、AReaL/Roll Flash/VeRL-Async 按 staleness guarantee、
trajectory coordination 与 version ownership 记录演进；7 月 PSRL release 归入同一 family 的后续 artifact，
不作为新的 W04 事件或 1 月代码公开证明。
Kareus 与 Perseus/Nanobatching 不是简单替代：前两条路线分别保留为 dynamic-energy 与 overlap
分支，Kareus 是在 execution variables 相互影响时的 joint-control 层。
Faramesh 与 IAM、gateway、sandbox、workflow 和 audit logs 是 `Layering / Dependency`：它增加统一的
canonical action 与 effect-time decision boundary，但不替代 identity、capability containment、业务
validation、outcome recording 或 compensation。
LLM-42 与 classic speculative decoding 是 `Principle Reuse`，不是同一优化目标；与 batch-invariant kernels
是可共存的 alternatives，选择取决于 deterministic traffic ratio、prefix reuse、rollback 与 SLO contract。
Universal Load Balancing 与 KV-aware locality routing 是 `Layering / Dependency`：前者减少 barrier max-load，
后者减少 Prefill/transfer/recompute；两种 score 必须在同一 SLO objective 中组合，不能只优化其一。
RM-RF 与 compile/run/mutation testing 是 `Layering / Dependency`，只能在 executable gate 前做筛选；
Fission-GRPO 与 deployment reflection 是 training/runtime 两层，不得合并为同一 retry 机制；
soft 与 hard KD 是带不同可见信息和 memorization inheritance 的共存分支，不按时间线互相覆盖。

## Knowledge Tree Position

本周使用 Stable Knowledge Node ID 作为长期 owner；旧章节号仅保留为 legacy mapping：

- `WORLDVIEW-REPRESENTATION`（Ch5 / legacy Ch5）：assistant axis；constitution 只作规范事实并由
  `WORLDVIEW-SYSTEM-EVOLUTION`（Ch9 / legacy Ch9）承接系统规范位置。
- `TRAIN-DATA`（Ch27 / legacy Ch23）：GIST、Endless Terminals，均 No Change。
- `TRAIN-SFT`（Ch29 / legacy Ch25）：KD memorization。
- `TRAIN-GRPO`（Ch33 / legacy Ch29）：StaleFlow、Jet-RL、LongCat、Fission-GRPO。
- `TRAIN-CHECKPOINT`（Ch35 / legacy Ch31）：DataStates-LLM。
- `TRAIN-DISTRIBUTED-TRAINING`（Ch36 / legacy Ch32）：LLEP；CPU-only Scaling All-to-all 拒绝。
- `TRAIN-MEGATRON`（Ch40 / legacy Ch36）：Kareus。
- `INFER-KV-CACHE`（Ch45 / legacy Ch41）：HeteroCache；Fast KVzip No Change。
- `INFER-CONTINUOUS-BATCHING`（Ch46 / legacy Ch42）：LLM-42。
- `INFER-SCHEDULING`（Ch56 / legacy Ch52）：Universal Load Balancing（Emerging）。
- `PLATFORM-EVALUATION-SYSTEM`（Ch66 / legacy Ch62）：RM-RF（Weekly Only）。
- `PLATFORM-MONITORING`（Ch67 / legacy Ch63）：Agentic Search。
- `PLATFORM-SECURITY`（Ch72 / legacy Ch68）：Faramesh（Emerging）。
- `AGENT-CONTEXT`（Ch75 / legacy Ch71）：SWE-Pruner。
- `AGENT-WORKFLOW`（Ch81 / legacy Ch77）：Sutradhara。
- `AGENT-MULTI-AGENT`（Ch82 / legacy Ch78）：CooperBench。

这些候选共享 state/evidence boundary 原则，但分别属于训练、推理、平台和 Agent，不构成一条替代链。

## Recommended Action

W04 当前 23 个 scored candidates 已完成逐项 disposition、16 项 Books 写入/重构与周级反向检查。
由于跨 `cs.AI/cs.LG/cs.CL` 的目录级 census 仍未机器复算，W04 保持 `Discovery Coverage Limited`，
不把当前命中集称为 full recall；若后续发现新 candidate，重新打开该周的 Source-Family Books Gate。

## Event-Date Daily Decision

2026-01-19～01-25 的命中事件直接写入 Weekly；历史回填不创建 Daily。

## Books Integration Decision

`Source-Family Books Gate Complete / Archive Completion Gate Open`。23 项最终 disposition 为：
16 项 `Integrate / Refine`、4 项 `No Change`、2 项 `Weekly Only`、1 项 `Reject`。已写入 Ch29、Ch33、
Ch35、Ch36、Ch40、Ch45、Ch46、Ch56、Ch67、Ch72、Ch75、Ch81、Ch82；没有将 Emerging、厂商
benchmark 或作者性能数字改写为通用结论。Archive/Discovery Gate 仍因目录级 recall limitation 保持 Open。

## Ignored Noise

把 constitution 当作 mechanistic interpretability 证明、把可解码方向当成完整人格模块，以及把
title/abstract screening 当作全文证据或最终评分。

## Repository Changes

- 2026-08-07：新增 9 项 primary metadata discovery ledger；完成 StaleFlow、Sutradhara、HeteroCache、
  DataStates-LLM 与 Scaling All-to-all 全文、评分和 Source Packet；前四项 retained，Scaling All-to-all
  因 2025 first-public 与 19/30 排除；完成 Kareus、Faramesh、LLM-42 全文并分别以 28/30、26/30、
  29/30 retained，Faramesh 因 synthetic-only evidence 标记 Emerging；完成 Universal Load Balancing
  全文并以 25/30 retained，但因 v1 simulation-only、无 solver overhead/artifact 标记 Emerging；9 项命中
  已全部 disposition，无历史 Daily 或 Books 修改。
- 第二轮从 Hugging Face discovery submission date 反查 arXiv first-public metadata，恢复 8 项 W04 候选；
  已完成 CooperBench、Jet-RL、LongCat、SWE-Pruner、Endless Terminals、LLEP、Agentic Search 与
  Fast KVzip 的全文、评分和 evidence boundary。
- 第三轮从 2 月 2 日 discovery list 反查恢复 RM-RF、Fission-GRPO 与 KD Memorization；已完成三篇
  全文、评分和 evidence boundary。
- 2026-08-13：完成 23/23 逐候选 Books disposition 与周级反向检查。16 项长期机制进入或 refine
  `TRAIN-SFT`、`TRAIN-GRPO`、`TRAIN-CHECKPOINT`、`TRAIN-DISTRIBUTED-TRAINING`、
  `TRAIN-MEGATRON`、`INFER-KV-CACHE`、`INFER-CONTINUOUS-BATCHING`、`INFER-SCHEDULING`、
  `PLATFORM-MONITORING`、`PLATFORM-SECURITY`、`AGENT-CONTEXT`、`AGENT-WORKFLOW` 与
  `AGENT-MULTI-AGENT`。4 项已有覆盖、2 项仅保留 Weekly、1 项跨年低分拒绝。Discovery limitation
  仍未关闭，不把 source-family Books 完成误写为 archive 完整。

## Open Questions

1. 行为规范、训练目标与内部表征之间需要什么 intervention evidence 才能建立因果链？
2. Universal Load Balancing 的可部署近似、routing overhead 与 v2 新能源实验能否由公开 artifact 复核？
3. Jet-RL 与 W05 FP8-RL 对 mismatch 的不同解决路径，在相同 kernel/hardware/workload 下怎样对齐？
4. LLEP 的 per-batch planning、weight movement 与 recovery protocol 在多机弱互联下是否仍有净收益？
5. Learned evaluation proxy 的 uncertainty sampling、Fission feedback provenance 与 KD privacy metrics，
   应分别以什么 production evidence 才能越过 Books Integration Gate？

## Sources

- Anthropic Research index, entries dated 2026-01-19 and 2026-01-22:
  https://www.anthropic.com/research
- Google Research, “Introducing GIST,” published 2026-01-23:
  https://research.google/blog/introducing-gist-the-next-stage-in-smart-sampling/
- StaleFlow, arXiv v1 published 2026-01-19; accessed 2026-08-07:
  https://arxiv.org/abs/2601.12784 ; HTML reviewed: https://arxiv.org/html/2601.12784v1 ;
  later PSRL artifact, open-sourced 2026-07-28: https://github.com/psrl-project/psrl
- Sutradhara, arXiv v1 published 2026-01-19; accessed 2026-08-07:
  https://arxiv.org/abs/2601.12967 ; HTML reviewed: https://arxiv.org/html/2601.12967v1
- HeteroCache, arXiv v1 published 2026-01-20, v2 revised 2026-04-18;
  accessed 2026-08-07: https://arxiv.org/abs/2601.13684 ; PDF reviewed:
  https://arxiv.org/pdf/2601.13684 ; ACL record: https://aclanthology.org/2026.acl-long.1999/
- DataStates-LLM, arXiv v1 published 2026-01-23; accessed 2026-08-07:
  https://arxiv.org/abs/2601.16956 ; HTML reviewed: https://arxiv.org/html/2601.16956v1 ;
  2024 predecessor: https://arxiv.org/abs/2406.10707
- Scaling All-to-all Operations Across Emerging Many-Core Supercomputers, SC Workshops 2025,
  arXiv uploaded 2026-01-24; accessed 2026-08-07: https://arxiv.org/abs/2601.17606 ;
  HTML reviewed: https://arxiv.org/html/2601.17606v1 ; SC25 proceedings:
  https://sc25.supercomputing.org/proceedings/workshops/workshop_pages/ws_exampi109.html
- Kareus, arXiv v1 published 2026-01-25; accessed 2026-08-07:
  https://arxiv.org/abs/2601.17654 ; HTML reviewed: https://arxiv.org/html/2601.17654v1
- Faramesh, arXiv v1 published 2026-01-25; accessed 2026-08-07:
  https://arxiv.org/abs/2601.17744 ; HTML reviewed: https://arxiv.org/html/2601.17744v1
- LLM-42, arXiv v1 published 2026-01-25, v2 revised 2026-01-30; accessed 2026-08-07:
  https://arxiv.org/abs/2601.17768 ; v1 HTML reviewed: https://arxiv.org/html/2601.17768v1 ;
  later/current artifact: https://github.com/microsoft/llm-42
- A Universal Load Balancing Principle and Its Application to Large Language Model Serving,
  arXiv v1 published 2026-01-25, v2 revised 2026-02-01; accessed 2026-08-07:
  https://arxiv.org/abs/2601.17855 ; v1 HTML reviewed: https://arxiv.org/html/2601.17855v1
- CooperBench v1: https://arxiv.org/html/2601.13295v1
- Jet-RL v1: https://arxiv.org/html/2601.14243v1
- LongCat-Flash-Thinking-2601 v1: https://arxiv.org/html/2601.16725v1
- SWE-Pruner v1: https://arxiv.org/html/2601.16746v1
- Endless Terminals v1: https://arxiv.org/html/2601.16443v1
- Least-Loaded Expert Parallelism v1: https://arxiv.org/pdf/2601.17111v1
- Agentic Search in the Wild v1: https://arxiv.org/html/2601.17617v1
- Fast KVzip v1: https://arxiv.org/pdf/2601.17668v1
- RM-RF, arXiv v1 published 2026-01-19; accessed 2026-08-07:
  https://arxiv.org/abs/2601.13097 ; HTML reviewed: https://arxiv.org/html/2601.13097v1
- Memorization Dynamics in Knowledge Distillation for Language Models, arXiv v1 published
  2026-01-21; accessed 2026-08-07: https://arxiv.org/abs/2601.15394 ;
  HTML reviewed: https://arxiv.org/html/2601.15394v1
- Fission-GRPO, arXiv v1 published 2026-01-22, v2 revised 2026-04-20;
  accessed 2026-08-07: https://arxiv.org/abs/2601.15625 ;
  current HTML reviewed: https://arxiv.org/html/2601.15625
- arXiv January 2026 `cs.DC` monthly listing, accessed 2026-08-07:
  https://arxiv.org/list/cs.DC/2026-01?show=2000
