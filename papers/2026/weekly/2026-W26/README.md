# AI Research Weekly — 2026-W26

> Coverage Window: 2026-06-22～2026-06-28
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-09
> Re-audit Status: 40/40 final dispositions; 37/39 `20+` Full Source Reviews complete; 30 Refine, 7 No Change, 1 Weekly Only, 2 Unverified / Blocked; Source-Family Books Gate complete under blocked-skip; Archive/Discovery Gate open; Books cursor advances to W27

## Executive Summary

旧版 W26 三行评分实际包含四个 Source Families，远低于本周 primary-source 候选密度。本轮按
arXiv v1 而不是 Hugging Face 展示日重新归周，恢复 24 项窗口内候选；其中 AgentWorld、Agent
Memory、verifier、terminal-agent data、agent runtime、streaming multimodal、diffusion LM 与 KV
compression 都构成独立 Source Family。长期信号不再只是“模型能力变强”，而是：Agent workload
开始迫使 world model、memory data system、verifier、executable task synthesis 与 runtime state
分别拥有可审计合同。

本检查点完成 `Are We Ready For An Agent-Native Memory System?` 以及另外 31 篇已恢复论文的全文、实验、
消融、限制与关键 Appendix 核验。
论文最重要的贡献不是宣布某个 memory system 胜出，而是把 Memory 拆成 representation/storage、
extraction、retrieval/routing、maintenance 四个可独立归因的模块，并证明 workload bottleneck 会改变
最优组合。AOHP 与 Self-Compacting Agents 仍因 primary text 不可访问留在 blocked backlog；它们不被
伪装成全文审计，也不再阻塞单向 cursor。

fixed-source replay 另恢复两个不能由学术 feed 替代的工程节点。DFlash 算法首发在 W06、DDTree
演进在 W16；W26 只记录 DFlash checkpoints 与 TensorRT-LLM/vLLM/SGLang integration 的新发布面和
完整 latency-throughput contract。TensorRT 11 multi-device inference 则把 preview flag 演进为 supported
distributed collective/context-parallel execution，并暴露 communicator lifetime、all-rank enqueue、hardware/
precision support matrix 与 hang/failure semantics。两项都不是“多 GPU 必然更快”的结论。

## Coverage and Source Coverage

- 模型与研究机构：保留 Google 6 月 24/26 日、OpenAI 与 Anthropic 6 月 26 日；新增 Qwen-AgentWorld、
  Wan-Streamer、Qwen-Image-Agent、Improved LLaDA 与 PhoneBuddy 的 primary paper/model family。
- 论文与学术来源：使用 Hugging Face 周榜做 recall，再以 arXiv abs/HTML 的 v1 日期与正文为准；
  已核验 24 项新增窗口内论文 metadata，另将展示日晚于 v1 的旧论文回流 W23～W25。
- AI Infra 与工程：恢复 agent-native memory testbed、CLI-Universe、AOHP、SelfCompact、KV compression
  等 system candidate；MTP mobile acceleration 仍只作为具体 hardware/runtime case。fixed list另完成
  DFlash engineering-integration node与 TensorRT 11 multi-device inference review；其他主要 project release
  surfaces未发现可可靠归入本周的独立 material event。
- 学术交叉检索：Google Scholar、OpenAlex、DBLP 用于 citation/venue/revision 交叉检查，不取代 arXiv
  或作者 artifact；本检查点尚未把 citation graph 当成完整性证明。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Frozen MTP for Gemini Nano on Pixel | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Worth Watching |
| Thinking to recall | 3 | 3 | 3 | 4 | 4 | 4 | 21/30 | Worth Watching |
| GPT-5.6 preview | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Official model state |
| Economic Index Cadences | 3 | 3 | 4 | 4 | 4 | 3 | 21/30 | Telemetry methodology state |
| Qwen-AgentWorld | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Refine — Ch10 Experimental |
| Agent-Native Memory System / MemoryData | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read；full review complete |
| EnterpriseClawBench | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | No Change — Ch62 Experimental Case |
| NatureBench / NatureGym | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | Refine — Ch62 Revision-sensitive |
| Verification Horizon | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Refine — Ch62 Experimental |
| Execute-Distill-Verify | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | Refine — Ch73 Experimental |
| OpenThoughts-Agent | 4 | 5 | 5 | 4 | 4 | 3 | 25/30 | Refine — Ch23 Experimental |
| CLI-Universe | 5 | 5 | 5 | 4 | 4 | 3 | 26/30 | Refine — Ch23 Experimental |
| AOHP OS-level Agent Harness | 5 | 5 | 4 | 3 | 5 | 4 | 26/30 | Unverified / Blocked Backlog — score provisional |
| Self-Compacting Language Model Agents | 4 | 4 | 5 | 3 | 5 | 4 | 25/30 | Unverified / Blocked Backlog — score provisional |
| Multi-Step Tool-Use RL Collapse | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | Refine — Ch29 Experimental |
| Wan-Streamer v0.1 | 5 | 5 | 4 | 4 | 4 | 3 | 25/30 | Integrate — Ch38 New Mechanism / Experimental |
| DanceOPD | 5 | 4 | 3 | 3 | 4 | 5 | 24/30 | Refine — Ch25 Experimental |
| Unlimited OCR Works | 4 | 3 | 4 | 3 | 4 | 5 | 23/30 | Refine — Ch22 Experimental |
| OPID | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Refine — Ch29 Experimental |
| Qwen-Image-Agent | 4 | 3 | 4 | 3 | 4 | 5 | 23/30 | No Change — Ch77 Experimental Case |
| KaLM-Reranker-V1 | 4 | 4 | 5 | 3 | 4 | 4 | 24/30 | Refine — Ch72 Experimental |
| Improved Large Language Diffusion Models | 5 | 5 | 4 | 3 | 5 | 3 | 25/30 | Refine — Ch17 Experimental |
| Causal-rCM | 4 | 4 | 4 | 3 | 4 | 5 | 24/30 | Refine — Ch10 Experimental |
| PhoneBuddy | 4 | 4 | 4 | 3 | 5 | 2 | 22/30 | Refine — Ch23 Experimental |
| Foresight failure detection | 4 | 3 | 3 | 3 | 4 | 5 | 22/30 | Refine — Ch62 Experimental |
| Tmax terminal-agent recipe | 4 | 4 | 5 | 3 | 5 | 3 | 24/30 | Refine — Ch23 Experimental |
| Information-Aware KV Cache Compression | 4 | 5 | 5 | 3 | 5 | 3 | 25/30 | Refine — Ch22 Experimental |
| Progress Advantage for LLM Agents | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Refine — Ch29 Experimental |
| Agentic Abstention | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Refine — Ch75 Experimental; W27 spillback |
| Dockerless Verifier | 4 | 5 | 5 | 3 | 5 | 4 | 26/30 | Refine — Ch62 Experimental; W27 spillback |
| PhysisForcing | 4 | 4 | 3 | 3 | 5 | 5 | 24/30 | Refine — Ch10 Experimental; W27 spillback |
| Qwen-Image-2.0-RL | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — Ch29 Experimental; W27 spillback |
| TUA-Bench | 4 | 4 | 5 | 4 | 5 | 3 | 25/30 | No Change — Ch62 Experimental Case; W27 spillback |
| Multi-Block Diffusion Language Models | 5 | 5 | 4 | 3 | 5 | 4 | 26/30 | Integrate — Ch38 New Mechanism / Experimental; W27 spillback |
| Evolution Fine-Tuning | 5 | 4 | 4 | 3 | 5 | 5 | 26/30 | Refine — Ch23 Experimental; W27 spillback |
| OSWorld 2.0 | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Refine — Ch62 Experimental; W27 spillback |
| DiscoBench | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | Refine — Ch75 Experimental; W27 spillback |
| GBC Multi-Agent Optimization | 5 | 4 | 4 | 3 | 5 | 4 | 25/30 | Refine — Ch78 Experimental; W27 spillback |
| DFlash cross-runtime integration | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Must Read — full review complete; W06 algorithm family / W26 engineering node |
| TensorRT 11 multi-device inference | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Must Read — full review complete; versioned distributed-execution node |

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Score rows / source families | 40 / 40 | 25 high、14 mid、1 low |
| `20+` Full Source Reviews | 37 / 39 | baseline 3 项 + Agent-Native Memory + 31 recovered papers + 2 fixed families；2 Unverified / Blocked Backlog |
| Academic discovery window | Checkpoint landed | HF feed replay + arXiv v1 date classification；citation/venue expansion remains open |
| Spillback relations | 27 | 原 17 项回拨 W23～W25；W27 display feed 又回拨 10 项到 W26 |
| Official / Infra discovery window | Checkpoint passed | DFlash integration + TensorRT 11 multi-device reviewed；remaining fixed surfaces produced no additional material W26 event |
| W26 forward Candidate Gate | Passed under blocked-skip rule | 37/39 Full Source Reviews；2/39 Unverified / Blocked Backlog；0 ordinary pending |
| W26 discovery / Historical Evidence Gate | Open | 2 blocked families 与 cross-index recall 未闭合；post-forward cursor advances to W27 |

## Evidence Level

MTP 结果绑定 Gemini Nano、Pixel hardware、runtime 和厂商评测；reasoning-recall 是研究结论；
GPT-5.6 与 Cadences 分别是厂商 model preview 与 telemetry methodology。新增论文中，Agent-Native
Memory 达到 `Primary paper + complete HTML + evaluation/ablation + public artifact`；另有 31 篇完成
primary HTML、method、evaluation、limitations 与关键 Appendix 核验，artifact 未公开处已显式降级。
AOHP 与 Self-Compacting Agents 保持 `Unverified / Blocked Backlog`。

DFlash W26 工程证据来自 NVIDIA发布说明、Model Optimizer training/export artifact、TensorRT-LLM/vLLM/
SGLang integration surface；算法因果与 exactness authority仍属于 W06 primary paper。公开结果分别绑定
gpt-oss-120B/8×B300/SPEED-Bench latency-throughput curve，以及单 B300/B200/H100、特定模型、task、
concurrency与 framework版本，不能合成“15x通用加速”。TensorRT 11证据来自 official release notes、
multi-device API/support matrix与sample；它证明 supported feature/lifecycle，不证明生产级 failover或任意
model/topology的 positive scaling。

## Cross-Week Deduplication

MTP 与 speculative decoding 是 `Principle Reuse / Layering`：都尝试每次 serial verification推进多个
token，但 proposal source、training coupling、acceptance 与 hardware path 不同。Agent-Native Memory 与
W01 SimpleMem、W08 MemoryAgentBench、W25 TokenPilot 构成 `Direct Evolution / Layering`：从“有没有
memory”推进到模块级数据系统合同，再把 active Context/cache management 与 durable memory 区分开。
Verification Horizon、EnterpriseClawBench、NatureBench 与 CLI-Universe 则组成 executable evaluation 链，
但必须在各自全文审计后才能判断是互补还是 benchmark-specific analogy。
DFlash W26 与 W06 是同一 Source Family 的 `Engineering Integration / Revision Node`，与 W16 DDTree 是
`Direct Evolution`：并行 block proposal先进入多 runtime，tree expansion再利用其 marginal breadth；不能
重复计为新算法。TensorRT 11 multi-device与 Ch32的collective taxonomy是`Principle Reuse`，与 Ch45
execution-plan build/runtime 是`Layering / Dependency`。

## Knowledge Tree Position

Ch8 reasoning；Ch21/24 model architecture/training；Ch38～45 generation/runtime；Ch62 evaluation；
Ch68 security；Ch71/73/77/80 agent context、memory、workflow 与 platform。
DFlash integration主映射Ch44，由Ch45/46/47承接 backend；TensorRT 11 multi-device主映射Ch45，由
Ch32/50/51承接 collective、memory与disaggregation边界。

## Recommended Action

保留 MTP 的端侧硬件/训练耦合案例，但因 Ch48 已有 frozen-MTP/acceptance/artifact contract，最终 `No Change`。
Agent-Native Memory 最终 `Refine — Existing Argument`，主 owner 为 `AGENT-MEMORY`（Ch77；Legacy Ch73），
把 representation/storage、extraction、retrieval/routing、maintenance 与 workload bottleneck 连接；Ch76/66/84
只做 handoff。DFlash W26 最终 `No Change — Engineering Integration Node`：Ch48 已拥有 DFlash/verify capacity/
artifact identity 主线；TensorRT 11 最终 `Refine — Existing Argument / Version-sensitive`：Ch49 已有 parallel
mapping，本轮补 communicator lifetime、all-rank progress 与 support-matrix failure semantics。Wan-Streamer、
OSWorld 2.0 与 Multi-Block Diffusion 分别 refine Ch24、Ch66 与既有 Ch24 Source-Family integration。

## Event-Date Daily Decision

2026-06-24、06-26：Weekly only。

## Books Integration Decision

`Source-Family Books Gate Complete under blocked-skip`。40 项逐一完成 disposition：30 Refine、7 No Change、
1 Weekly Only、2 Unverified / Blocked。Qwen-AgentWorld 与 Multi-Block Diffusion 的既有 Source-Family
integration 保留；本轮实质 refine MemoryData module×workload 归因、Wan-Streamer deployment ownership、
TensorRT multi-device lifecycle 与 OSWorld dynamic checkpoint evidence。其余 Refine 是章节级增强或 revalidation；
两个 blocked family 不获得机制 owner。Archive/Discovery Gate 继续开放。

## Ignored Noise

把端侧厂商结果外推到不同模型、GPU server、batch 或 SLO。

- 把 DFlash W26 集成宣传重复计为 W06 新算法，或把不同模型/硬件/framework 的 speedup拼成单一数字。
- 把 TensorRT `supported` 等同于自动 partition、elastic rank、failover或跨节点容错；官方 sample要求各 rank
  自建 engine/context并同步进入 collective，缺 rank会无限等待。

## Full Source Review

### Agent-Native Memory System / MemoryData — 28/30

- **Candidate / Week / Source Family**：`AGENT-NATIVE-MEMORY-DATA-SYSTEM`；W26；arXiv:2606.24775v1，
  first-public 2026-06-23；截至本检查点无后续 arXiv revision。
- **Direct / Related Primary Sources**：arXiv abs + 完整 HTML；作者 `OpenDataBox/MemoryData` testbed；
  `OpenDataBox/awesome-agent-memory` taxonomy。代码仓当前状态晚于论文事件日，只有与 paper contract
  一致的 runner、preset、artifact layout 可作为 artifact corroboration，不能倒推论文时实现。
- **Access and Full-read Coverage**：已读 metadata、Introduction/Preliminaries、完整 taxonomy、四模块
  method、五组 RQ、全部 end-to-end tables、component ablations、cost/latency、Conclusion 与 references；
  论文无独立 Limitations 章节，因此把公开 testbed、模型/provider、数据可用性与外部有效性缺口显式记录。
- **Original Problem / Previous Design**：end-to-end F1/EM 适合快速比较“是否答对”，把 memory 当单体
  也曾有利于迭代完整 Agent；但它无法回答错误来自 representation、write-time extraction、routing 还是
  maintenance，也无法比较 update correctness、evidence distance 与 operation cost。
- **Changed Constraint / Mechanism**：跨 session、持续 update 与多 workload 使 memory 变成 data
  management object。论文将系统写成 `M_sys=<R,S,Q,U>`：representation/storage、extraction、retrieval/
  routing、maintenance；每层再区分 token/graph/composite、single/multi-engine、raw/free/schema extraction、
  attention/dense/topological/agentic/hybrid routing，以及 versioning/eviction/consolidation。
- **State Ownership / Data and Control Flow**：raw interaction/tool trace 属于 provenance source；`S` 生成
  typed/derived memory；`R` 拥有 logical identity 与 physical index；`Q` 在 query context 下选择 evidence；
  `U` 执行 conflict/version、capacity 与 consolidation transition。LLM 只参与某些 extraction/routing/
  consolidation policy，不能成为 source of truth。公开 runner 以 YAML preset 绑定 method + benchmark，
  输出 result、persisted agent state 与 logs，说明 evaluation artifact 也必须版本化。
- **Implementation Details**：公开仓提供统一 `main.py`、22 个 method presets、OpenAI-compatible endpoint
  配置、MemoryAgentBench/LoCoMo/LongBench/MemBench loaders 与 stable artifact root；datasets 不随仓发布，
  外部服务/模型配置由执行者提供。它提高可复跑性，但不是 hermetic reproduction bundle。
- **Evaluation Contract**：论文比较 12 个代表系统与 Long Context/Embedding RAG baselines，覆盖五类
  workload/11 datasets；分别测 task effectiveness、evidence-level Recall@K/distance gap、knowledge update/
  temporal reasoning、long-horizon bins、amortized construction+query latency 与 normalized utility；细粒度
  ablation 分别替换 representation、extraction、routing、maintenance。公开材料没有披露统一 GPU、完整
  serving concurrency、batch、precision、power 或 production SLO，故延迟数字不能外推为平台容量结论。
- **What Evidence Proves**：在作者统一 runner 与所选 workload 中，没有单一架构全面占优；structured/
  linked evidence 在大 K、远距离或 temporal update 上更稳；raw/coverage-preserving extraction 对 exact
  fidelity 很重要；planning/balanced fusion 可改善所测 routing；localized/conservative maintenance 位于更好
  cost-quality frontier。Ablation 支持“模块与 workload 对齐”而非“graph/vector/summary 永远最好”。
- **What It Does Not Prove**：不证明 12 个 implementation 均达到作者原项目同等优化；不证明 LLM judge
  是 ground truth；不证明 graph 在所有 temporal query 上胜出；不证明 raw context 在无限 horizon 可扩展；
  也不证明其 latency 能代表不同 provider、network、hardware、并发或 production SLO。
- **Trade-offs / New Failure Modes**：更强结构可能提升 scattered-evidence completion，却增加 write
  propagation、multi-store synchronization 与 query latency；抽象/总结降低 Context，却不可逆丢失 precise
  evidence；agentic routing 提高适配性，也增加 planner drift 与不可确定性；append-only 保留 provenance，
  却会返回 stale facts；global consolidation 提升组织度，代价是 rewrite amplification 与错误扩散。
- **Where Previous Designs Still Apply**：短 history、exact evidence 不能丢时，Long Context 仍合理；高
  QPS/局部语义 lookup 时 flat embedding 仍便宜；稳定 schema/关系 query 适合 graph；多 workload、版本更新、
  多 evidence 类型才值得 hybrid/multi-engine。演进关系是 `Layering / Direct Evolution`，不是替代链。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch72、Ch73、Ch74 与 Ch80；Ch73 已覆盖
  write/read/consolidation/forgetting、typed transition、provenance 与 exact archive，但缺少统一四模块归因和
  workload-specific evaluation matrix。Ch72 已拥有 stateless RAG boundary，Ch62 拥有 EvalSpec，Ch80 拥有
  platform state。主 owner Ch73；provisional `Refine — Existing Argument`，Historical Books Gate 关闭。
- **Open Questions**：能否以 frozen artifacts 重现所有 systems；如何把 ACL/tenant/delete/poisoning 纳入同一
  component ablation；如何区分 memory operation latency 与 model/provider latency；怎样评价 concurrent writes、
  crash recovery、rollback 和 multi-principal governance。

### Frozen MTP for Gemini Nano on Pixel — 24/30

- **Source Family / Type / Date**：`FROZEN-MTP-PIXEL`；Google Research 2026-06-24 official technical
  post 与关联论文/implementation evaluation。
- **Full-read Coverage**：已覆盖 frozen main model + MTP heads、proposal/verification、on-device runtime、
  quality/acceptance/latency evaluation、ablation 和限制。
- **Mechanism / Evidence Boundary**：在冻结 base model 上训练/挂接 multi-token proposal heads，让一次
  target verification 接受多个 token；证明特定 Gemini Nano、Pixel hardware、quantization/runtime
  下的收益，不证明 server batch、不同 tokenizer/model 或 SLO 下同样成立。
- **Trade-offs / Evolution**：相比独立 draft model，MTP 减少额外模型 state 并更紧耦合 target，代价是
  head calibration、acceptance drift、额外 parameters/kernel 和模型升级兼容；普通 autoregressive
  decode 在低 acceptance/实现成本敏感场景仍成立。关系为 Ch44 的 `Principle Reuse / Layering`。
- **ROADMAP / Decision**：Ch44 主 owner，已读 Ch43～45、Ch50；`No Change — Already Covered`。

### Thinking to recall — 21/30

- **Source / Coverage**：Google Research 2026-06-26 research post 与关联论文；已读 parametric recall
  tasks、reasoning intervention、baselines、ablation 与 limitations。
- **Evidence / Decision**：作者实验说明额外 reasoning 在某些 recall setting 改变 retrieval outcome，
  不证明知识被可靠存储、所有事实任务获益或 CoT 是 faithful mechanism。Ch8/62 已读；
  `No Change — Already Covered`。

### GPT-5.6 preview — 19/30

- **Source / Verification**：OpenAI 2026-06-26 preview 与可访问 system-card state 已核对；该条目
  证明 model-family/product availability，不与 usage telemetry 共享 mechanism。
- **Decision**：19/30；`Weekly Only — Version/Product Fact`。不把厂商 benchmark、价格或未披露的
  model/training/runtime implementation 写入长期正文。

### Economic Index Cadences — 21/30

- **Source / Verification**：Anthropic 2026-06-26 Cadences report 已核对；它是 usage telemetry 的
  sampling/classification/reporting methodology state，而非 GPT-5.6 的模型评测。
- **Evidence / Boundary**：观测趋势绑定 product population、sampling window、task taxonomy、
  classifier version 与 aggregation；pipeline 变化可能制造 apparent trend，不能由相关性推断模型
  使用对 worker/productivity 的因果影响。
- **Decision**：Ch62/63/69 已读；`No Change — Already Covered`，现有 telemetry contract 已要求
  population、taxonomy、sampling 与 version provenance。

### DFlash cross-runtime integration — 27/30

- **Candidate / Week / Source Family / History**：`DFLASH-DIFFUSION-SPECULATIVE-DECODING`；W26
  engineering node，NVIDIA technical post 2026-06-23。算法 primary paper v1 为 2026-02-05，已在 W06
  全文审计；W16 DDTree 是利用 DFlash marginals 建 verification tree 的后续分支。本周不重复声称新算法。
- **Direct / Related Primary Sources / Coverage**：联读 NVIDIA发布全文、W06 paper packet、Model Optimizer
  DFlash architecture/training/export/AR validation、TensorRT-LLM speculative docs、vLLM Speculators与SGLang
  integration入口。覆盖 target hidden-state conditioning、KV injection、block mask、checkpoint/export、
  acceptance验证、cross-runtime config与公开 workload tables；未把 later repository main当 event-date frozen tag。
- **Original Problem / Previous Design / Changed Constraint**：AR drafter顺序明确、易与 target exact verify，
  在短 block/低并发仍合理；但 draft critical path随候选长度增长。W06解决并行 proposal后，W26约束变成
  draft artifact能否跨多个 serving runtimes进入真实 latency-throughput operating curve，而不是只在论文
  harness保持加速。
- **Mechanism / State Ownership / Control and Data Flow**：target隐藏层经 projection/RMSNorm形成 conditioning，
  注入 draft各层 KV projection；masked block一次预测未来位置。drafter只拥有 provisional proposal，target
  verifier拥有 accepted prefix与 correction，runtime拥有 provisional KV commit/rollback、batch scheduling与
  streaming。Model Optimizer拥有 training/checkpoint/export contract；backend integration拥有 kernel/layout/
  scheduler compatibility，不拥有 target sampling semantics。
- **Implementation Details**：公开 Model Optimizer example用 Nemotron post-training 2M samples、64 GPUs、
  10 epochs、block size 8、sequence 4096、512 anchors、KD+decay，并导出 HF config/weights；AR validation逐步
  用 base model重新验证并在首个 mismatch写入target correction。W26发布说明记录20 checkpoints与
  TensorRT-LLM/vLLM/SGLang入口，但“无需 application refactor”不等于内部 state/API完全相同。
- **Evaluation Contract**：主 vendor curve为gpt-oss-120B、8×DGX B300、TensorRT-LLM、SPEED-Bench，比较
  相同 user interactivity下throughput；其他表分别为Llama3.1-8B、Gemma4-31B/单B300/vLLM、Qwen3-8B/
  单B200/SGLang与特定 tasks/concurrency。Model Optimizer另披露Qwen3-8B、H100、MT-Bench 80 prompts、
  max 1024与TP1/8。不同表不能合并；无统一TTFT/TPOT tails、power、cost、request-length distribution或SLO。
- **What the Evidence Proves / Does Not Prove**：证明同一算法 family已形成可训练、导出并接入三类runtime的
  engineering surface，也显示 latency-throughput Pareto而非单batch token/s更适合评价；不证明15x跨模型/
  hardware成立，不证明cross-runtime结果feature-equivalent，也不证明 block diffusion总优于EAGLE/DDTree。
- **Trade-offs / Failure Modes / Previous Design**：并行draft提高GPU work，却增加target-feature cache、
  artifact coupling、mask/block-size calibration、backend parity、acceptance drift、provisional KV与rollback矩阵。
  AR drafter在高命中短block、成熟tree kernel或portability优先时仍合理；纯AR decode仍是无draft资产时基线。
- **Evolution / ROADMAP / Chapters / Decision**：`W06 algorithm → W16 marginal-derived tree branch → W26
  multi-runtime integration` 是 `Direct Evolution + Engineering Integration`。已读Ch43～47；主owner Ch44，
  backend handoff Ch45～47。`No Change — Already Covered / Engineering Node`；Historical Books Gate关闭。

### TensorRT 11 multi-device inference — 27/30

- **Candidate / Week / Source Family / History**：`TENSORRT-11-MULTI-DEVICE-INFERENCE`；W26；official
  technical post 2026-06-25与TensorRT 11 release/docs。TensorRT 10.16 preview flag是旧方案；11.0把feature
  标为fully supported并扩展collectives，属于versioned maturity node，不等同于TensorRT-LLM release。
- **Direct / Related Primary Sources / Coverage**：已读technical post全篇、11.0 release notes、multi-device
  setup/API、support/feature matrix、multi-device attention与sample execution flow；覆盖preview→supported、
  DistCollective、NCCL discovery、engine/context/communicator lifecycle、context-parallel attention、compatibility、
  breaking/known issues。当前docs的11.1 fixes只用于核验failure evolution，不倒写为6月25状态。
- **Original Problem / Previous Design / Changed Constraint**：single-GPU engine最简单，拥有最少rank/collective
  failure面，对放得下且latency足够的模型仍合理；外部runtime编排collectives可表达分布式执行，但graph build/
  optimization看不到通信层。超大media/long-context networks突破单卡memory/compute后，需要把communication
  作为network/engine的一等层，同时保留TensorRT build-time optimization。
- **Mechanism / State Ownership / Control and Data Flow**：`IDistCollectiveLayer`在network graph声明AllReduce、
  AllGather、ReduceScatter、AllToAll、Gather/Scatter等与rank/group/root；每rank拥有local engine、execution
  context、stream、buffers与CUDA device，NCCL communicator必须在context整个lifetime有效。所有参与rank
  同步调用`enqueueV3/execute_async_v3`，collective progress由全组参与共同拥有；缺一rank会让其余无限等待。
- **Implementation / Support Contract**：DistCollective要求Ampere+，multi-device attention把KV sequence做
  context parallel、仅BF16/FP16且要求Blackwell；special-purpose automotive/RTX/Coverity/DLA builds不支持。
  feature matrix不支持ragged tensor、refittable weights与safety build；rank-local weight streaming可用。
  TensorRT 11从10.16 preview flag迁移到supported，新增AllToAll/Gather/Scatter并提高NCCL minimum；B300上
  NCCL 2.29.4 cold-init问题说明runtime version与communicator dependency必须共同锁定。
- **Evaluation Contract**：technical post以Cosmos/FLUX类media pipeline比较AllGather-KV、Ring Attention与
  Ulysses context parallel，但结果只在指定models、sequence、GPUs、precision与software版本成立。sample只
  证明API/control flow可执行，不提供production concurrency、failure recovery、tail latency、goodput、power
  或cost contract；本review不保留“某策略永远最低latency”的headline。
- **What the Evidence Proves / Does Not Prove**：证明execution plan可以原生包含distributed collective与
  context-parallel attention，并明确rank-local state/communicator lifetime；不证明TensorRT自动选择partition、
  elastic membership、跨node failover、partial-rank recovery或所有model positive scaling。
- **Trade-offs / Failure Modes / Previous Design**：获得跨device graph optimization与单engine-family workflow，
  代价是support matrix、rank-synchronous progress、communicator/version coupling、cold init、engine duplication、
  collective ordering、hang诊断与每rank memory。外部orchestration/单卡engine在heterogeneous model、elasticity、
  failure isolation或unsupported precision/build优先时仍合理。
- **Evolution / ROADMAP / Chapters / Decision**：`single-device engine → externally orchestrated collectives →
  preview distributed layers → supported graph-native collectives + CP attention` 是 `Direct Evolution`；与Ch32
  collective semantics为`Principle Reuse`。已读Ch32、Ch45及Ch44/46/50/51邻接；主owner Ch45。
  provisional `Refine — Existing Argument / Version-sensitive`；Historical Books Gate关闭，不改Books。

### Qwen-AgentWorld — 28/30

- **Source / Coverage**：arXiv:2606.24597v1，first-public 2026-06-23；已读训练三阶段、七域数据、loss
  masking、RL reward/stability ablation、AgentWorldBench、下游训练与 Appendix。论文没有独立 Limitations
  章，外部有效性与 simulator contamination 因而必须由读者补充审计。
- **Problem / Mechanism / Ownership**：真实环境昂贵、不可重置且覆盖受限；code simulator 可验证却只适合可形式化域。
  LWM 直接预测 action 后 observation，`CPT injects → SFT activates → RL sharpens`，以信息统计屏蔽低价值
  environment turns。模型拥有预测状态，真实环境仍拥有 authoritative state；模拟 observation 不能升级为事实。
- **Evidence / Trade-off**：作者在七域 next-state 与三个 agent benchmark 报告增益，并用 reward/expansion
  ablation 暴露 shared-prefix collapse；只证明所列模型、judge、环境和训练配方，不能证明 LWM 可替代真实执行。
  泛化换来 stochasticity、reward-model bias、simulation drift 与错误经验放大。
- **Evolution / Chapters / Decision**：`programmatic simulator → domain LWM → unified LWM + controllable simulation`
  是 `Layering / Dependency`，不是 determinism 的替代。已读 Ch10 与 Ch23/29/62 邻接；provisional
  `Refine — Existing Argument / Ch10 / Experimental`。

### EnterpriseClawBench — 25/30

- **Source / Coverage**：arXiv:2606.23654v1，first-public 2026-06-22；已读 session-to-task pipeline、privacy/
  reproducibility checks、artifact/rubric scoring、scalability、judge ablation、案例与 Limitations。
- **Mechanism / State**：从真实企业 session 恢复 fixture、重写 prompt、生成 hard rules 与 semantic rubric，
  sandbox preflight 后评测 `harness + model`。原 session/attachment/trace 是 provenance owner，recovered task
  是脱敏派生资产，不应反向替代原始证据。
- **Evidence Boundary**：它证明真实 workload 可以被系统化转成 artifact-producing benchmark，并联合报告质量、
  成本和 runtime；但数据来自一家企业且不公开，视觉 judge 仍需人工校准，不能支持跨组织的能力排名。
- **Decision**：Ch62 已有 subject/environment/scorer/run contract 与 artifact evidence；已读 Ch62 及 Ch61/63，
  provisional `No Change — Already Covered / Experimental Case`，仅保留该 provenance/privacy 案例。

### NatureBench / NatureGym — 25/30

- **Source / Coverage**：arXiv:2606.24530v1，v1 2026-06-23、HTML 显示后续文稿日期 2026-08-11；已读
  paper filtering、task/environment verification、SOTA-relative scoring、reproduction audit、实验与 resource appendix。
- **Mechanism**：把 Nature-family 论文转换为可执行 optimization tasks，用 provenance-locked source method、
  dataset/environment package 与双向 `reproduce / surpass` 判定分开“复现论文”与“发现更优方案”。
- **Evidence Boundary**：实验只说明给定论文集合、预算、agent scaffold 与可复现环境中的搜索结果；SOTA
  comparison 对 revision、资源预算和 evaluator 极敏感，不能推出 autonomous science 的一般能力。
- **Decision**：主 owner Ch62，Ch77 只承接 workflow；provisional `Refine — Existing Argument /
  Revision-sensitive`，因为它为 executable artifact 增加了“source-paper baseline + resource parity”合同。

### The Verification Horizon — 26/30

- **Source / Coverage**：arXiv:2606.26300v1，first-public 2026-06-24；已读 static/visual/interactive judges、
  behavior monitor、long-repo evaluator、训练应用、variance 分解、failure taxonomy 与 Appendix prompts。
- **Mechanism**：不同任务把 verification horizon 推向不同边界：代码/截图检查便宜但看不到动态行为；
  Playwright 执行 action plan 可看状态转换；长 repo 再由 evaluator agent 分解 checklist、执行自建 tests 并与
  held-out unit tests 校准。judge 拥有 verdict，environment/trace 才拥有 outcome evidence。
- **Evidence Boundary**：作者展示 scorer family 排序稳定、interactive reward 与 evaluator alignment；同时明确
  static view 无法覆盖 routing/stateful interaction，agent judge 又有 cost、sequential error、role confusion 与
  over-specification。不存在跨 workload 的单一 silver bullet。
- **Decision**：已读 Ch62 与 Ch61/63/68；provisional `Refine — Existing Argument / Experimental`，补强
  `verification horizon` 作为选择 verifier 层级而非追求统一 scorer 的原则。

### Execute-Distill-Verify — 25/30

- **Source / Coverage**：arXiv:2606.24428v1，first-public 2026-06-23；已读 heterogeneous execute、third-party
  distill、consensus verify、shared/private banks、三类 benchmark、ablation、Limitations 与 qualitative attribution。
- **Mechanism / Ownership**：多个 executor 产生相互独立轨迹，第三方比较后蒸馏 candidate experience；原
  executors 以 default-reject 验证，一致通过写 shared bank、局部通过写 private bank。raw trajectory 是证据，
  distilled rule 是有 provenance 的 derived memory，而非事实本身。
- **Evidence Boundary / Failure**：实验支持该组合优于所列 memory baselines；不证明 unanimity 等于 truth。
  consensus bias、弱 agent 干扰、归因困难、memory growth 与多 agent 成本是新增 failure modes。
- **Decision**：已读 Ch73 与 Ch72/77/78；provisional `Refine — Existing Argument / Ch73 / Experimental`，
  与书稿的 write/hold/defer_verify、derived memory 和 supersession 形成 `Direct Evolution`。

### OpenThoughts-Agent / Data Recipes — 25/30

- **Source / Coverage**：arXiv:2606.24855v1，first-public 2026-06-23；已读 SFT/RL curation stages、逐阶段
  ablation、模型规模、长序列训练、跨 benchmark 评测、artifact 与 Limitations。
- **Mechanism**：把 agent data recipe 视为可测 pipeline：每次只改变 task/trajectory filtering、difficulty、
  formatting 或 RL mixture 一项，以跨三个 benchmark 的标准化分数选择下一阶段。data lineage 与 recipe version
  拥有训练分布；最终 checkpoint 不能解释单项因果。
- **Evidence Boundary**：结果支持 Qwen3 family 上 SFT 与 RL data 组合会交互；RL 只在 8B、base family
  未消融，z-score objective 又内含 benchmark weighting，不能外推到 32B 或其他 pretrained distribution。
- **Decision**：已读 Ch23 与 Ch24/25/29；provisional `Refine — Existing Argument / Ch23 / Experimental`。

### CLI-Universe — 26/30

- **Source / Coverage**：arXiv:2606.22883v1，first-public 2026-06-22；已读 capability specification、evidence-
  guided research、environment/solution/test synthesis、多级 executable verification、SFT transfer 与 Limitations。
- **Mechanism / State Flow**：`capability → grounded task spec → container/fixture → independent solution/tests →
  execution gate → trajectory`。task spec、environment image、test suite 与 trace 分别版本化；生成 agent 不能同时
  成为最终 verifier 的唯一 authority。
- **Evidence Boundary**：6k trajectories 在 8B/14B/32B students 与 out-of-domain tests 上给出作者实验增益；
  quality ceiling 仍由生成模型和 verifier 决定，规模、RL transfer 与 frontier gap 未解决。
- **Decision**：已读 Ch23、Ch62 与 Ch22/29；provisional `Refine — Existing Argument / Ch23 / Experimental`，
  强化 synthetic data 的 executable task contract，而非记录一个数据集版本。

### Multi-Step Tool-Use RL Collapse — 25/30

- **Source / Coverage**：arXiv:2606.26027v1，first-public 2026-06-24；已读 token-level failure diagnosis、
  ETS/PRS supervisory interventions、BFCL variants、训练表与 Limitations。
- **Mechanism**：terminal outcome reward 在长 trajectory 中无法告诉 policy 哪个 action token 造成失败；作者将
  expert trajectory SFT 或 process-relevant supervision 与 RL 交错，让低概率关键 token 获得可学习信号。
- **Evidence Boundary**：Qwen2.5-1.5B 与 Qwen3-1.7B 的有限可验证 tool environment 支持“vanilla GRPO 可
  collapse、监督可恢复”的条件性结论；数据规模未扩展，不能写成所有 tool-use RL 的必然规律。
- **Decision**：已读 Ch29 与 Ch27/74；provisional `Refine — Existing Argument / Ch29 / Experimental`，
  主张保留 outcome reward、token credit 与 corrective data 的三方边界。

### Wan-Streamer v0.1 — 25/30

- **Source / Coverage**：arXiv:2606.25041v1，first-public 2026-06-24；已读 causal multimodal architecture、
  rolling distillation、thinker-performer pipeline、latency protocol、comparison boundary 与 qualitative evaluation。
- **Mechanism / Ownership**：单一 Transformer 训练为连续 causal stream，部署时 thinker 拥有 encoder、language/
  state update、decoder 与 authoritative KV slices，performer 只运行下一 audio/video latent flow solver；双方交换
  full-history KV 和前一单元 latents，以一拍流水重叠理解与生成。
- **Evidence Boundary / Trade-off**：约 200ms model-side、约 550ms total 只绑定作者系统与未完整披露硬件/
  workload；对比系统的 latency contract 并不一致。收益来自 overlap，成本是 KV 一致性、双侧 failure、
  backpressure、跨模态时钟与滚动生成误差。
- **Decision**：已读 Ch38 与 Ch39/40/41/51；provisional `Integrate — New Mechanism / Ch38 / Experimental`，
  这是 `unified model → state-preserving thinker/performer deployment` 的 layering，不是否定模块化 pipeline。

### DanceOPD — 24/30

- **Source / Coverage**：arXiv:2606.27377v1，first-public 2026-06-25；已读 on-policy field distillation、
  semantic-side query、hard routing、dense-query correlation、implementation、evaluation 与 ablations。
- **Mechanism**：student 在自身 rollout states 上查询多个 frozen capability fields，再以 single semantic-side
  query 与 stop-gradient 更新，避免同一 trajectory 上密集相关 teacher queries 把冲突能力平均进一个 step。
- **Evidence Boundary**：image generation/editing 实验支持作者配置下的 capability fusion；SDE decorrelation
  只提供诊断且表现更差，说明“更多 query”不是免费监督。机制依赖 frozen teachers、routing 与生成域。
- **Decision**：已读 Ch25 与 Ch27/29；provisional `Refine — Existing Argument / Ch25 / Experimental`，
  作为 distillation 中 teacher conflict、on-policy query distribution 与 correlation 的受限案例。

### Unlimited OCR Works — 23/30

- **Source / Coverage**：arXiv:2606.23050v1，first-public 2026-06-22；已读 R-SWA、training/inference、attention
  replacement experiments、long parsing 与 conclusion；无独立 limitations，通用化风险显著。
- **Mechanism**：visual/reference tokens 保持固定可见，历史 output 只在 causal sliding window 内滚动；这避免
  per-page loop 丢失进度，也避免让 reference features 进入 recurrent update。窗口状态属于模型 runtime，原文档
  与 page identity 仍是外部 authoritative evidence。
- **Evidence Boundary**：作者仅在 parsing tasks 报告替换 decoder attention 后近似无损；不能据此推出无限
  context、任意 reference task 或无遗忘。远距精确回读、prefill chunk fetching 与 provenance 仍未解决。
- **Decision**：已读 Ch22 与 Ch13/17/41；provisional `Refine — Existing Argument / Ch22 / Experimental`。

### OPID — 24/30

- **Source / Coverage**：arXiv:2606.26790v1，first-public 2026-06-25；已读 skill analyzer/router、on-policy
  log-prob advantage、ALFWorld/WebShop/search experiments、hierarchy/routing ablation 与 Appendix protocol。
- **Mechanism**：完成 trajectory 后抽取 episode/step skills；旧 policy 对同一 on-policy response 在原 context 与
  skill-augmented context 下重评分，log-prob shift 形成 dense hindsight advantage，并与 episode advantage 合并。
  skills 在训练时是 privileged derived state，推理时被蒸馏进 policy，不保留外部 skill store。
- **Evidence Boundary**：三个 domain 与 Qwen2.5/Qwen family 结果支持 distribution-matched hindsight signal；
  analyzer error、skill leakage、旧 policy calibration 与 task-specific routing 都可能造成伪 credit，未证明跨模型普适。
- **Decision**：已读 Ch29 与 Ch25/73；provisional `Refine — Existing Argument / Ch29 / Experimental`。

### Qwen-Image-Agent — 23/30

- **Source / Coverage**：arXiv:2606.26907v1，first-public 2026-06-25；已读 context-gap taxonomy、plan/reason/
  search/memory/feedback workflow、IA-Bench、backbone ablation 与 failure discussion。
- **Mechanism / Evidence**：Agent 把 user context 转成 renderer 可消费的 generation context，缺口可能由 retrieval、
  planning、memory 或 iterative feedback 补齐；实验同时表明换弱 renderer 会整体下降，而某些 implicit context gap
  又无法靠强 renderer 修复。它证明 pipeline bottleneck 分层，不证明该特定 workflow 是唯一实现。
- **Decision**：Ch77 已覆盖 artifact workflow、Ch72/73/74/75 各自拥有局部机制；已读这些相邻章，provisional
  `No Change — Already Covered / Experimental Case`，避免把多模块产品框图重复写入正文。

### KaLM-Reranker-V1 — 24/30

- **Source / Coverage**：arXiv:2606.22807v1，first-public 2026-06-22；已读 FBNL architecture、Matryoshka
  pooling、training、BEIR/MIRACL/LMEB experiments、compression/online-cost curves 与 error analysis。
- **Mechanism**：document encoder 产生可复用 compressed passage representations，query 通过 decoder cross-
  attention 保留较深 interaction；它位于 joint cross-encoder 与 late interaction 之间。offline document state
  可缓存，query-specific score 仍由在线 decoder 拥有。
- **Evidence Boundary / Trade-off**：作者任务支持中等压缩的 cost-quality frontier；压缩升高时 ROC-AUC 尤其在
  小模型下降。storage saving 换来 representation loss、index migration、model/version identity 与 online decoder cost。
- **Decision**：已读 Ch72 与 Ch53/58；provisional `Refine — Existing Argument / Ch72 / Experimental`。

### Improved Large Language Diffusion Models — 25/30

- **Source / Coverage**：arXiv:2606.25331v1，first-public 2026-06-24；已读 masked-diffusion objective、12T
  pretraining、SFT format、variable-length inference、benchmark/ablation、evaluation appendix 与 limitations。
- **Mechanism**：保持 fully bidirectional masked prediction，通过 blockwise variable-length generation、EOS handling、
  confidence-based multiple-choice scoring 与多 epoch SFT 补齐 practical recipe；状态不是 AR 的单 token frontier，
  而是当前 mask set 与 denoising schedule。
- **Evidence Boundary**：8B base 与 instruct 结果证明该 recipe 可缩小与 AR baseline 的差距，但训练 tokens、数据、
  alignment 与 scoring 不等，不能归因为 diffusion 本身；作者也未做 RL alignment，instruct 仍落后强 AR model。
- **Decision**：已读 Ch17 与 Ch20/25/38；provisional `Refine — Existing Argument / Ch17 / Experimental`。

### Causal-rCM — 24/30

- **Source / Coverage**：arXiv:2606.25473v1，first-public 2026-06-24；已读 TF/SF distillation、JVP、replayed
  backprop、KV/CP compatibility、training tables、streaming/world-model experiments、ablations 与 limitations。
- **Mechanism**：先以 teacher-forcing consistency/matching 获得稳定初始化，再以 self-forcing DMD 对齐 student
  rollout distribution；infrastructure 用 activation checkpoint、post-all-to-all KV layout、FSDP2/Ulysses CP 与
  custom JVP kernel 支撑长 rollout。模型拥有 latent trajectory，runtime 拥有分片 KV/collective state。
- **Evidence Boundary / Trade-off**：Wan2.1 与 action-conditioned settings 支持 staged recipe；长 T2V rollout
  仍出现 camera drift，强初始化不保证最终稳定，joint optimization 会降 ceiling，Triton kernel 也限制 portability。
- **Decision**：已读 Ch10 与 Ch32/34/41；provisional `Refine — Existing Argument / Ch10 / Experimental`。

### PhoneBuddy — 22/30

- **Source / Coverage**：arXiv:2606.23049v1，first-public 2026-06-22；已读 real/mock environments、mixed
  SFT+RL、evaluation protocol、cross-app slices、discussion/limitations 与 system-family boundary。
- **Mechanism**：real-app RL 提供真实 side effects 与 app logic，PhoneWorld 提供 scale/reset/automatic verifier；
  shared SFT 后 mixed RL 对齐两种分布。environment owner 与 phone runtime owner 分离，mock success 不是实机事实。
- **Evidence Boundary**：150-task real-phone 与 AndroidWorld 结果支持作者模型上的 complementarity；cross-app
  handoff 明显落后，论文明确不覆盖 harness、privacy/safety deployment，不能从 training gain 推出 deployability。
- **Decision**：已读 Ch23 与 Ch29/62/77；provisional `Refine — Existing Argument / Ch23 / Experimental`。

### Foresight — 22/30

- **Source / Coverage**：arXiv:2606.23085v1，first-public 2026-06-22；已读 action-conditioned latent predictor、
  causal detectors、calibration、simulation/real robot/cross-policy experiments、implementation 与 limitations。
- **Mechanism**：world model 根据 observation+action 预测 latent evolution，sequence detector 用 trajectory-level
  labels 学习 failure score，再以 conformal calibration 选择 alarm threshold。policy 执行动作，monitor 只拥有
  advisory verdict，environment outcome 才是事实。
- **Evidence Boundary**：多个 benchmark 与实机结果支持 latent sequence 比 frame-only detector 更有用；cross-
  policy transfer 明显非对称，calibration guarantee 依赖 distribution match，world model latency限制 reactive control。
- **Decision**：已读 Ch62 与 Ch10/64/69；provisional `Refine — Existing Argument / Ch62 / Experimental`。

### TMax — 24/30

- **Source / Coverage**：arXiv:2606.23321v1，first-public 2026-06-22；已读 Tmax-15k synthesis、container
  isolation、RL recipe、training stability、cross-harness evaluation、released rollouts/logprobs 与 Limitations。
- **Mechanism**：strong generator 产生较难 terminal environments，container/verifier 保证可执行 reward，再用
  RL 扩大 tool-use capability；dataset/image/verifier/policy version 共同定义训练 contract。
- **Evidence Boundary**：Qwen-derived models 到 27B 与多 harness 结果支持 recipe transfer；synthetic ceiling、
  instability 与 container cost 未被消除，也未证明 student 可超过 generator 或任意 harness 泛化。
- **Decision**：已读 Ch23 与 Ch29/62；provisional `Refine — Existing Argument / Ch23 / Experimental`。

### Information-Aware KV Cache Compression — 25/30

- **Source / Coverage**：arXiv:2606.26875v1，first-public 2026-06-25；已读 forward-influence motivation、entropy/
  representation/attention score、prefill/decode experiments、budget ablations、appendix settings 与 Limitations。
- **Mechanism**：attention 只描述当前 query 的 backward-looking relevance；InfoKV 用 predictive entropy、layer
  representation evolution 与 attention 估计 token 对未来分布的影响，周期性选择保留 KV。runtime 拥有 cache
  residency，model-derived score 只是 eviction hint。
- **Evidence Boundary**：Llama/Qwen distilled models 与 LongReason/AIME/code slices 支持作者配置下优于几种
  attention heuristics；entropy 仍是间接 proxy，adaptive layer budget 会因 architecture 不同而不稳定。
- **Decision**：已读 Ch22 与 Ch41/50；provisional `Refine — Existing Argument / Ch22 / Experimental`。

### Progress Advantage — 24/30

- **Source / Coverage**：arXiv:2606.26080v1，first-public 2026-06-24；已读 MDP derivation、policy-ratio estimator、
  agent scaffolding、experiments、baselines、ablations 与 reward-model discussion。
- **Mechanism**：在论文假设下，RL policy 与 reference policy 的 log-prob ratio 近似 optimal advantage，用已有
  post-training checkpoints 对 trajectory steps 打分，无需单独训练 PRM。policy/reference identity 与 tokenization
  是 score authority；跨版本混用会破坏坐标系。
- **Evidence Boundary**：作者 agent tasks 支持其作为 inference-time progress signal；理论等式依赖 optimality/
  distribution assumptions，终端 outcome 仍可能奖励 spurious steps，不能把 ratio 当因果 step correctness。
- **Decision**：已读 Ch29 与 Ch27/62；provisional `Refine — Existing Argument / Ch29 / Experimental`。

### Agentic Abstention — 26/30

- **Source / Coverage**：arXiv:2606.28733v1，first-public 2026-06-26；已读 cross-environment taxonomy、episode
  metrics、benchmark construction、convolve、ablations、prompt appendix 与 Limitations。
- **Mechanism**：把 action space 增加为 `act / ask / abstain`，按 ambiguity、missing prerequisite、environment
  infeasibility 判断何时停止；convolve 从完整 rollout 蒸馏 compact stopping rules 放入后续 context。environment
  state 拥有 feasibility，playbook 只是可失效 policy hint。
- **Evidence Boundary**：WebShop 的 20 trajectories 支持小样本 context evolution 可改善所列 recall/SPL；范围只覆盖
  web/terminal/RAG 的部分 infeasibility，真实权限、stale resource、冲突 tool output 与长期 user state 未覆盖。
- **Decision**：已读 Ch75 与 Ch71/74/77；provisional `Refine — Existing Argument / Ch75 / Experimental`。

### Dockerless — 26/30

- **Source / Coverage**：arXiv:2606.28436v1，first-public 2026-06-26；已读 repository-exploring verifier、tool loop、
  SFT filtering、RL reward、baselines、cost/accuracy analysis 与 conclusion；论文没有清晰独立 limitations 章。
- **Mechanism**：verifier 不构建 repo runtime，而以真实 code-search/read tools 主动检查 patch、依赖与调用关系后
  输出 verdict。repository snapshot/patch/tool trace 是 evidence，model verdict 不是 executable outcome。
- **Evidence Boundary / Trade-off**：作者 experiments 支持在其 SWE data 上接近 environment-based training 且降低
  setup；不能证明语义检查等价 tests。动态行为、native deps、concurrency、hidden state 与 model false confidence
  仍是失真源，成本从 environment build 转移到 verifier inference/tool search。
- **Decision**：已读 Ch62 与 Ch23/29/68；provisional `Refine — Existing Argument / Ch62 / Experimental`，
  明确它是 verifier ladder 中的中间层，不替代 hermetic execution。

### PhysisForcing — 24/30

- **Source / Coverage**：arXiv:2606.28128v1，first-public 2026-06-26；已读 trajectory/pixel/semantic losses、
  Wan2.2/Cosmos3 experiments、ablations、risk 与 Limitations。
- **Mechanism**：trajectory-level relation supervision约束长程 motion，pixel point tracking 约束局部连续/contact，
  frozen video encoder 的 token-similarity 约束全局 interaction；它 fine-tune video world simulator，不拥有真实物理状态。
- **Evidence Boundary**：R-Bench/PAI/EZS 与两个 backbones 支持所列 plausibility metrics；能力受 backbone world
  knowledge/temporal ceiling 限制，synthetic video 必须在真实 hardware 验证，不能当 robotics policy success。
- **Decision**：已读 Ch10 与 Ch23/62；provisional `Refine — Existing Argument / Ch10 / Experimental`。

### Qwen-Image-2.0-RL — 25/30

- **Source / Coverage**：arXiv:2606.27608v1，first-public 2026-06-26；已读 task-specific rewards、RL policies、
  on-policy distillation、benchmark/arena protocol 与 training pipeline；缺少独立 limitations/完整 ablation。
- **Mechanism**：T2I 与 editing 分别由不同 reward composition 训练 specialist policies，再以 trajectory-level
  velocity matching 蒸馏为一个 student，避免同时优化冲突 reward。teacher/reward/checkpoint identity 必须保留。
- **Evidence Boundary**：作者 benchmark 与 arena 报告 base-to-RL 增益；不隔离每个 reward、judge preference、
  compute 或 OPD 的独立贡献，不能外推为多任务 RL 的通用最优解。
- **Decision**：已读 Ch29 与 Ch25/27；provisional `Refine — Existing Argument / Ch29 / Experimental`。

### TUA-Bench — 25/30

- **Source / Coverage**：arXiv:2606.28480v1，first-public 2026-06-26；已读 120-task taxonomy、headless/container
  environments、artifact verification、multi-run protocol、task-level heatmap 与 Limitations。
- **Mechanism / Evidence**：用 terminal-native everyday/professional workflows 扩大 programming-only benchmark，
  同时测 planning、tool execution、file artifact 与 recovery。它提供 workload slice，不定义 terminal Agent 的统一能力；
  category averages 会掩盖 task heterogeneity，English-only、domain coverage与 future contamination均有限制。
- **Decision**：Ch62 已要求 task slices、environment version、artifact 与 uncertainty；已读 Ch62/74，provisional
  `No Change — Already Covered / Experimental Case`。

### Multi-Block Diffusion Language Models — 26/30

- **Source / Coverage**：arXiv:2606.29215v1，first-public 2026-06-27；已读 SingleBD/D2F evolution、MultiTF、
  Block Buffer runtime、math/code experiments、accuracy-parallelism ablations、hardware/training appendix。
- **Mechanism / Ownership**：SingleBD 在 block 内并行、block 间串行；MultiTF 让模型见过多个 noisy blocks，
  inference 以 fixed-slot Block Buffer 激活/commit blocks，保持静态 shape、CUDA Graph 与 prefix/KV cache。
  scheduler 拥有 running-set/slot state，模型拥有各 block denoising distribution。
- **Evidence Boundary / Trade-off**：作者模型上 TPF/TPS 提升且有限 accuracy loss；TPF 不是 end-to-end SLO，
  train-inference noise layout、buffer size、commit correctness、wasted denoising 与 static graph coupling 是新成本。
- **Decision**：已读 Ch38 与 Ch17/41/44；provisional `Integrate — New Mechanism / Ch38 / Experimental`，
  保留 `fully bidirectional → SingleBD → MultiBD` 演进而非用后者覆盖前者。

### Evolution Fine-Tuning — 26/30

- **Source / Coverage**：arXiv:2606.29082v1，first-public 2026-06-27；已读 156K trajectory collection、mid-
  training objective、371 tasks、22 held-out evaluation、test-time search/RL interaction 与 Limitations。
- **Mechanism**：不把 test-time search 的最佳 answer 当唯一 label，而把 mutation/evaluation/selection trajectories
  作为 supervision，让 policy 内化“如何演化候选”。trajectory generator、OpenEvolve scaffold 与 evaluator
  identity 共同定义 learned discovery distribution。
- **Evidence Boundary**：2B–9B models 在 held-out optimization tasks 支持跨任务迁移；collection/evaluation 都用
  OpenEvolve，test-time RL synergy 只在数学任务，无法分离 scaffold imitation 与普遍 discovery capability。
- **Decision**：已读 Ch23 与 Ch25/29/77；provisional `Refine — Existing Argument / Ch23 / Experimental`。

### OSWorld 2.0 — 27/30

- **Source / Coverage**：arXiv:2606.29537v1，first-public 2026-06-28；已读 long-horizon task construction、dynamic
  environment/user simulator、partial rewards、judge validation、safety/behavior annotations、cases 与 Limitations。
- **Mechanism**：从 binary completion 演进到 task-specific checkpoints（平均 27.25），同时保存 initial/dynamic
  state、cross-app artifacts、user interactions 与 challenge exposures；checkpoint judge 与 simulator 均需独立校准。
- **Evidence Boundary**：它证明旧 OSWorld 缺失的长程/动态/多应用现象可被更细粒度测量；task mix、stochastic
  behavior、人工构建成本、benchmark exploitation 与 model-dependent components 仍限制总体分数解释。
- **Decision**：已读 Ch62 与 Ch71/77；provisional `Refine — Existing Argument / Ch62 / Experimental`。

### DiscoBench — 25/30

- **Source / Coverage**：arXiv:2606.27669v1，first-public 2026-06-26（后有 v2 revision）；已读 ambiguity
  construction、checkpoint/user simulator、detection/clarification metrics、ablations、quality inspection 与 Limitations。
- **Mechanism**：在多步 search 中把 ambiguity 作为动态 state；Agent 可 search、ask 或 guess，checkpoint 分开测
  是否检测到 ambiguity 与 question 是否有效。用户/ground-truth 拥有 disambiguation，retrieval 数量不代表 progress。
- **Evidence Boundary**：作者 models 上 SearchThenAsk 优于 repeated-search guessing；仅四类 objective ambiguity，
  LLM user simulator 不能代表真实用户，不能把主动提问写成所有 query 的默认动作。
- **Decision**：已读 Ch75 与 Ch72/77；provisional `Refine — Existing Argument / Ch75 / Experimental`。

### GBC — 25/30

- **Source / Coverage**：arXiv:2606.28187v1，first-public 2026-06-26；已读 agent DAG、gradient-based connection、
  backward attribution、prompt update、experiments/error analysis 与 Limitations。
- **Mechanism**：把 multi-agent forward workflow 显式化为 DAG，借 gradient/input signals 给 predecessor outputs
  分配 connection weight，再沿 attribution paths 产生 verbal update。workflow trace 是 evidence，task-specific
  verbal loss 决定优化方向；它不是物理意义上的因果归因。
- **Evidence Boundary / Trade-off**：作者任务支持比 coarse final reward 更细的 optimization；多次 forward/backward
  昂贵、loss design 敏感，cross-domain/retrieval/omission errors仍存在，规模与动态 topology未证明。
- **Decision**：已读 Ch78 与 Ch75/77；provisional `Refine — Existing Argument / Ch78 / Experimental`。

## Final Books Integration Ledger

| # | Candidate | Final disposition | Stable owner / chapter evidence |
| ---: | --- | --- | --- |
| 1 | Frozen MTP for Gemini Nano on Pixel | No Change — Already Covered | `INFER-SPECULATIVE-DECODING` Ch48 已有 frozen-base/MTP/acceptance contract |
| 2 | Thinking to recall | No Change — Already Covered | Ch8 reasoning 与 Ch66 已区分 recall outcome、storage 与 faithful mechanism |
| 3 | GPT-5.6 preview | Weekly Only — Version/Product Fact | 未公开 model/training/runtime mechanism |
| 4 | Economic Index Cadences | No Change — Already Covered | Ch63/66 已有 population/taxonomy/sampling/version telemetry contract |
| 5 | Qwen-AgentWorld | Refine — Existing Argument | `MULTIMODAL-WORLD-MODELS` Ch25；action-conditioned world state |
| 6 | Agent-Native Memory System / MemoryData | Refine — Existing Argument | `AGENT-MEMORY` Ch77；module×workload attribution |
| 7 | EnterpriseClawBench | No Change — Already Covered | `PLATFORM-EVALUATION-SYSTEM` Ch66 已有 enterprise state/artifact/harness split |
| 8 | NatureBench / NatureGym | Refine — Existing Argument | `PLATFORM-EVALUATION-SYSTEM` Ch66；revision-sensitive executable science environment |
| 9 | Verification Horizon | Refine — Existing Argument | `PLATFORM-EVALUATION-SYSTEM` Ch66；verifier validity 随 horizon 衰减 |
| 10 | Execute-Distill-Verify | Refine — Existing Argument | `AGENT-MEMORY` Ch77；execution-derived experience 与 verifier provenance |
| 11 | OpenThoughts-Agent | Refine — Existing Argument | `TRAIN-DATA` Ch27；terminal trajectory synthesis and filtering |
| 12 | CLI-Universe | Refine — Existing Argument | `TRAIN-DATA` Ch27 / Ch66；hermetic executable task generation |
| 13 | AOHP OS-level Agent Harness | Unverified / Blocked | 无可验证正文；不分配 Books mechanism owner |
| 14 | Self-Compacting Language Model Agents | Unverified / Blocked | 无可验证正文；不分配 Books mechanism owner |
| 15 | Multi-Step Tool-Use RL Collapse | Refine — Existing Argument | `TRAIN-GRPO` Ch33；terminal reward、token credit 与 corrective data |
| 16 | Wan-Streamer v0.1 | Refine — Existing Argument | `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24；state-preserving thinker/performer pipeline |
| 17 | DanceOPD | Refine — Existing Argument | Ch24/Ch33 handoff；on-policy teacher-field routing |
| 18 | Unlimited OCR Works | Refine — Existing Argument | `MODEL-LONG-CONTEXT` Ch22；fixed reference + rolling output state |
| 19 | OPID | Refine — Existing Argument | `TRAIN-GRPO` Ch33；privileged hindsight skill as training-only state |
| 20 | Qwen-Image-Agent | No Change — Already Covered | Ch76/77/81 已拥有 retrieval/memory/workflow bottleneck split |
| 21 | KaLM-Reranker-V1 | Refine — Existing Argument | `AGENT-RAG` Ch76；offline document state + online query interaction |
| 22 | Improved Large Language Diffusion Models | Refine — Existing Argument | Ch17/24；masked-set state 与 variable-length block generation |
| 23 | Causal-rCM | Refine — Existing Argument | `MULTIMODAL-WORLD-MODELS` Ch25；teacher→self forcing evolution |
| 24 | PhoneBuddy | Refine — Existing Argument | `TRAIN-DATA` Ch27；real/mock environment distribution ownership |
| 25 | Foresight failure detection | Refine — Existing Argument | `PLATFORM-EVALUATION-SYSTEM` Ch66；action-conditioned failure forecast calibration |
| 26 | Tmax terminal-agent recipe | Refine — Existing Argument | `TRAIN-DATA` Ch27；terminal task/trajectory/verifier generation |
| 27 | Information-Aware KV Cache Compression | Refine — Existing Argument | `MODEL-LONG-CONTEXT` Ch22；information-aware retention 与 exact fallback |
| 28 | Progress Advantage for LLM Agents | Refine — Existing Argument | `TRAIN-GRPO` Ch33；progress proxy 与 terminal correctness boundary |
| 29 | Agentic Abstention | Refine — Existing Argument | `AGENT-PLANNING` Ch79；answer/ask/verify/abstain as typed actions |
| 30 | Dockerless Verifier | Refine — Existing Argument | `PLATFORM-EVALUATION-SYSTEM` Ch66；execution isolation 与 verifier identity |
| 31 | PhysisForcing | Refine — Existing Argument | `MULTIMODAL-WORLD-MODELS` Ch25；physical dynamics forcing boundary |
| 32 | Qwen-Image-2.0-RL | Refine — Existing Argument | `TRAIN-GRPO` Ch33；specialist reward composition and distillation |
| 33 | TUA-Bench | No Change — Already Covered | `PLATFORM-EVALUATION-SYSTEM` Ch66 已有 task slices/environment/artifact evidence |
| 34 | Multi-Block Diffusion Language Models | Refine — Existing Argument | `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24；block buffer/commit state |
| 35 | Evolution Fine-Tuning | Refine — Existing Argument | `TRAIN-DATA` Ch27；mutation/evaluation/selection trajectory supervision |
| 36 | OSWorld 2.0 | Refine — Existing Argument | `PLATFORM-EVALUATION-SYSTEM` Ch66；dynamic checkpoint/persistent-state evidence |
| 37 | DiscoBench | Refine — Existing Argument | `AGENT-PLANNING` Ch79；ambiguity detection before clarification |
| 38 | GBC Multi-Agent Optimization | Refine — Existing Argument | `AGENT-MULTI-AGENT` Ch82；DAG attribution is proxy, not causal proof |
| 39 | DFlash cross-runtime integration | No Change — Engineering Integration Node | `INFER-SPECULATIVE-DECODING` Ch48 已有 algorithm/artifact/runtime boundaries |
| 40 | TensorRT 11 multi-device inference | Refine — Existing Argument / Version-sensitive | `INFER-TENSORRT-LLM` Ch49；communicator/all-rank lifecycle |

逐行复算结果：40/40 final；30 Refine、7 No Change、1 Weekly Only、2 Unverified / Blocked。Blocked
families 没有机制 owner；所有 `No Change` 均引用已读章节中的具体论点。

## Blocked Primary-Source Backlog

2026-08-13 精确 identity 重试恢复了原 33 项中的 31 篇 HTML 正文，均已完成 method、evaluation、
limitations、关键 Appendix 与相邻章节审计。AOHP 与 Self-Compacting Agents 仍无可验证正文。

以下 2 项已完成 primary metadata、v1 日期与 abstract-level relevance 核验；由于 primary-paper domain
仍不可访问，均不计 Full Source Review：

| Candidate | First-public | Blocked Primary ID | Claims explicitly not verified |
| --- | --- | --- | --- |
| AOHP | 2026-06-22 | arXiv:2606.23449 | OS object model、permission boundary、personal state |
| Self-Compacting Agents | 2026-06-22 | arXiv:2606.23525v1 | model-triggered compaction、rubric、fidelity/recovery |

第四列只声明不得从标题、摘要或旧 review focus 推断的机制，不是论文结论。两项均不分配 Books owner、
不修改 Books；原评分只保留为 provisional discovery priority。按用户明确的 blocked-skip 规则，它们不阻塞
后续周；W26 ordinary review queue 已清零，post-forward cursor 推进 W27。

## Repository Changes

- W26 从 4 个 baseline families 扩展到 40 个评分行，加入 34 个按 arXiv v1 归属本周的候选与2个
  fixed-source engineering nodes；
  完成 Agent-Native Memory 与 31 项恢复论文的非模板化 Full Source Review；AOHP 与 Self-Compacting Agents
  仍为 `Unverified / Blocked Backlog`，0 ordinary pending，cursor 推进 W27。
- 识别 27 个 later-feed spillback：原 17 项按 first-public date 回填 W23～W25，W27 display feed
  的 10 项按 6 月 25～28 日 v1 回拨 W26，而不是污染后续周时间线。
- 完成DFlash cross-runtime integration与TensorRT 11 multi-device inference非模板化review；前者与W06/W16
  去重为同一算法family的工程节点，后者记录preview→supported的distributed-execution contract。fixed
  official/Infra checkpoint通过；academic ordinary review queue 已闭合并推进 cursor。
- Books Integration 完成 40/40 dispositions；保留 Ch25/Ch24 的既有 Source-Family integration，本轮 refine
  `AGENT-MEMORY`、`INFER-TENSORRT-LLM`、`MULTIMODAL-GENERATIVE-PARADIGMS` 与
  `PLATFORM-EVALUATION-SYSTEM`。两项 blocked 未进入 Books；无历史 Daily。

## Open Questions

1. frozen MTP head 在模型更新、quantization 和 domain drift 后如何重新校准？
2. MemoryData 的 dataset/provider/runtime 是否可冻结为 hermetic reproduction bundle？
3. executable benchmark 的 verifier 怎样证明没有把 harness 能力误算成 model 能力？
4. DFlash三类runtime在相同model/checkpoint/kernel/scheduler contract下是否保持acceptance、KV rollback与
   latency-throughput parity？
5. 非执行式 verifier 在什么任务上可替代 hermetic execution，哪些错误必须以真实运行揭示？
6. 长程 Agent benchmark 怎样分离 model、harness、user simulator、environment state 与 verifier？
7. TensorRT multi-device的rank failure、communicator re-init、engine restart与checkpoint/partial-output语义如何
   形成production recovery contract？
8. MemoryData 的 module ablation、OSWorld 2.0 的 checkpoint evidence 与 Agentic Abstention 的 action policy
   能否在长期 Agent 中共享同一 state/provenance identity，而不让 benchmark state 变成部署 authority？

## Sources

- Google Research NLP archive, entries dated 2026-06-24 and 2026-06-26:
  https://research.google/blog/label/natural-language-processing/
- OpenAI, “Previewing GPT-5.6 Sol,” published 2026-06-26:
  https://openai.com/index/previewing-gpt-5-6-sol/
- Anthropic, “Economic Index report: Cadences,” published 2026-06-26:
  https://www.anthropic.com/research/economic-index-june-2026-report
- Hugging Face Daily Papers, display week 2026-06-21～2026-06-27（仅作 discovery feed；按 arXiv v1 重新归周）:
  https://huggingface.co/papers/week/2026-W26
- Wei Zhou et al., “Are We Ready For An Agent-Native Memory System?”, arXiv:2606.24775v1,
  first-public 2026-06-23, accessed 2026-08-09: https://arxiv.org/abs/2606.24775
- Author HTML full text: https://arxiv.org/html/2606.24775
- OpenDataBox, MemoryData author artifact, accessed 2026-08-09: https://github.com/OpenDataBox/MemoryData
- OpenDataBox, Awesome Agent Memory taxonomy, accessed 2026-08-09:
  https://github.com/OpenDataBox/awesome-agent-memory
- NVIDIA, DFlash cross-runtime deployment, published 2026-06-23:
  https://developer.nvidia.com/blog/boost-inference-performance-up-to-15x-on-nvidia-blackwell-using-dflash-speculative-decoding/
- NVIDIA Model Optimizer, DFlash training/export/validation artifact:
  https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/speculative_decoding/doc/dflash.md
- NVIDIA, TensorRT multi-device inference, published 2026-06-25:
  https://developer.nvidia.com/blog/scaling-ai-inference-across-multiple-gpus-using-nvidia-tensorrt-with-multi-device-inference-support/
- NVIDIA TensorRT, Multi-Device Inference:
  https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/multi-device-inference.html
- NVIDIA TensorRT 11.0.0 release notes:
  https://docs.nvidia.com/deeplearning/tensorrt/latest/getting-started/release-notes-11/11.0.0.html
- Qwen-AgentWorld: https://arxiv.org/abs/2606.24597
- EnterpriseClawBench: https://arxiv.org/abs/2606.23654
- NatureBench: https://arxiv.org/abs/2606.24530
- The Verification Horizon: https://arxiv.org/abs/2606.26300
- Execute-Distill-Verify: https://arxiv.org/abs/2606.24428
- OpenThoughts-Agent: https://arxiv.org/abs/2606.24855
- CLI-Universe: https://arxiv.org/abs/2606.22883
- AOHP: https://arxiv.org/abs/2606.23449
- Self-Compacting Language Model Agents: https://arxiv.org/abs/2606.23525
- Multi-Step Tool-Use RL Collapse: https://arxiv.org/abs/2606.26027
- Wan-Streamer: https://arxiv.org/abs/2606.25041
- DanceOPD: https://arxiv.org/abs/2606.27377
- Unlimited OCR Works: https://arxiv.org/abs/2606.23050
- OPID: https://arxiv.org/abs/2606.26790
- Qwen-Image-Agent: https://arxiv.org/abs/2606.26907
- KaLM-Reranker-V1: https://arxiv.org/abs/2606.22807
- Improved Large Language Diffusion Models: https://arxiv.org/abs/2606.25331
- Causal-rCM: https://arxiv.org/abs/2606.25473
- PhoneBuddy: https://arxiv.org/abs/2606.23049
- Foresight: https://arxiv.org/abs/2606.23085
- Tmax: https://arxiv.org/abs/2606.23321
- Information-Aware KV Cache Compression: https://arxiv.org/abs/2606.26875
- Progress Advantage: https://arxiv.org/abs/2606.26080
- Agentic Abstention: https://arxiv.org/abs/2606.28733
- Dockerless: https://arxiv.org/abs/2606.28436
- PhysisForcing: https://arxiv.org/abs/2606.28128
- Qwen-Image-2.0-RL: https://arxiv.org/abs/2606.27608
- TUA-Bench: https://arxiv.org/abs/2606.28480
- Multi-Block Diffusion Language Models: https://arxiv.org/abs/2606.29215
- Evolution Fine-Tuning: https://arxiv.org/abs/2606.29082
- OSWorld 2.0: https://arxiv.org/abs/2606.29537
- DiscoBench: https://arxiv.org/abs/2606.27669
- GBC: https://arxiv.org/abs/2606.28187

## 2026-08-13 Source-Family Books Integration

Multi-Block Diffusion Language Models 已通过 Source-Family Books Gate：Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，Current Ch24，Legacy N/A；作为 block-level causal order + within-block refinement 的 Experimental 分支写入 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。Qwen-AgentWorld 的 durable world-state机制由 `MULTIMODAL-WORLD-MODELS` / Ch25 承载，但产品/版本能力未写入正文。AOHP 与 Self-Compacting Agents 仍 blocked，Archive Completion Gate 保持 Open。
