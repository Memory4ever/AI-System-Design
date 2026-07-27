# AI Research Weekly — 2026-W01

> Coverage Window: 2025-12-29～2026-01-04（完整 ISO week，Monday～Sunday）
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31
> Books Integration Review: 2026-08-13 — 11/11 Dispositions Complete / Discovery Coverage Limited / Archive Gate Open

## Executive Summary

原报告把本周判断为没有达到 20/30 的候选。该结论经 discovery recall 回扫后被推翻：仅按
arXiv v1 首次公开日期核验，就恢复出 11 个达到保留门槛的候选。它们不是同一条“新技术替代旧技术”
路线，而是暴露出四组长期系统问题：怎样让真实 control plane 可在虚拟 GPU 时间上运行；怎样把
RL 生成、训练与网络重配置的异构节奏编排起来；怎样把 KV、fast weights、规则或对话记忆的状态
所有权做显式化；以及怎样让 tool-use 的数据、评测与故障恢复不只依赖理想 API。

其中 Revati、OrchestrRL、Tarragon 的共同点不是某个 speedup，而是把状态与控制边界前移：Revati
保留真实 serving control plane、只虚拟化 GPU execution；OrchestrRL 让 compute scheduler 与可重构
fabric 联合决策，但物理实验只覆盖 compute scheduler；Tarragon 将 Attention/KV 与 Expert compute
解耦，并用增量 checkpoint/restore 缩小 worker failure 的恢复域。三者都用更多 metadata、协调器和
恢复协议换取更高利用率或更短恢复时间。

RIMRULE、HardGen、Beyond Perfect APIs 与 Does Memory Need Graphs? 则共同修正了 Agent 侧的
一个直觉：保存更多 trace、增加 graph 或生成更多调用样本并不自动产生可靠能力。需要把 failure
signal、抽象/合并规则、检索表示、API 异常、verifier 与 provenance 分开建模，否则 benchmark improvement
很容易混入 generator、judge、environment 或 harness 的贡献。

本周 11 个 retained candidates 已完成非模板化 Full Source Review，并按 Source-Family Books Gate 逐项
完成 Books Integration：10 项形成长期机制 refine/integration，DiT-HC 因系统原则已由 Ch36 覆盖而判定
`No Change`。Books 的完成不关闭 Archive Gate；discovery 仍不是可机器复算的全类别 census，因此 W01
不能标成 full-recall complete，后续新增命中仍须重新打开本周 Books Review。

## Coverage and Source Coverage

- **模型与研究机构：** 检查固定官方 Research / Blog 入口；没有把年度回顾、产品营销或机制未披露的
  能力声明提升为长期候选。此处是已检查入口的结果，不是对所有机构发布的绝对否定。
- **论文与学术来源：** 以 arXiv primary source 的 v1 日期固定事件周，窗口上界为 2026-01-04；
  2026-01-05 首次公开的论文归入 W02。对 retained candidates 阅读 metadata、方法、实现、评测、
  ablation/appendix 与 limitations；后续 revision 只用于核验，不回写成 W01 新事件。
- **AI Infra：** 检查 PyTorch、vLLM、SGLang、Dynamo release 入口；未发现达到长期门槛且可核验机制的
  stable release。论文中的 prototype 不因此被写成 framework version fact。

## Discovery Recall Reconciliation

- **Original scored rows:** 0。
- **Recovered retained candidates:** 11；全部完成 Full Source Review。
- **Screened below threshold:** 4；完成日期、范围与拒绝理由核验，不用于填充 retained set。
- **Date boundary:** 2025-12-29～2025-12-31 首次公开的事件属于 2026-W01；1 月 5 日及之后归入 W02。
- **Discovery limitation:** 当前回扫恢复了 `cs.DC`、`cs.AI`、`cs.LG`、`cs.CL` 的一组可验证命中，
  但还没有形成所有分类、cross-list 与 replacement/revision 的机器可复算目录快照。因此本清单是
  **最低命中集**，不得解读为“本周只有这些论文”。Google Scholar、Semantic Scholar、OpenAlex、
  DBLP 等 discovery index 只用于补漏与元数据交叉检验，技术结论仍回到 primary source。
- **Gate status:** `Source-Family Books Gate Complete / Discovery Coverage Limited / Archive Gate Open`；
  当前 11 项均有最终 disposition，但候选召回完备性仍未闭合。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| RIMRULE | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Refine — `AGENT-MEMORY` / Ch77 (legacy Ch73) |
| Beyond Perfect APIs | 4 | 4 | 4 | 4 | 4 | 5 | 25/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` / Ch66 (legacy Ch62) |
| Revati | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Integrate — `PLATFORM-EVALUATION-SYSTEM` / Ch66 (legacy Ch62) |
| FlexSpec | 4 | 4 | 4 | 3 | 4 | 4 | 23/30 | Refine / Experimental — `INFER-SPECULATIVE-DECODING` / Ch48 (legacy Ch44) |
| FwPKM | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Integrate / Experimental — `MODEL-LONG-CONTEXT` / Ch22 |
| OrchestrRL | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Integrate / RFabric Experimental — `TRAIN-GRPO` / Ch33 (legacy Ch29) |
| Does Memory Need Graphs? | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Refine — `AGENT-MEMORY` / Ch77 (legacy Ch73) |
| FLOP-Efficient Training | 4 | 4 | 3 | 3 | 4 | 4 | 22/30 | Integrate / Experimental — `TRAIN-PRETRAINING` / Ch28 (legacy Ch24) |
| Tarragon | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Integrate / Experimental — `INFER-PD-DISAGGREGATION` / Ch55 (legacy Ch51) |
| HardGen | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Refine / Experimental — `TRAIN-DATA` / Ch27 (legacy Ch23) |
| DiT-HC | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | No Change — covered by `TRAIN-DISTRIBUTED-TRAINING` / Ch36 (legacy Ch32) |

## Full Source Review

### RIMRULE

- **Candidate / Week / Score:** RIMRULE / 2026-W01 / 26/30；
  `Source Family ID: rimrule-mdl-tool-memory`。
- **Source / Date / Coverage:** arXiv:2601.00086v1，2025-12-31。已阅读 v1 PDF 的方法、MDL 目标、
  symbolic retrieval、数据划分、baselines、cross-model reuse、ablation、limitations 与 appendix；v2/v3
  不作为 W01 新证据。
- **Original Problem / Previous Design / Changed Constraint:** few-shot retrieval 保留原始样本、global
  prompt 固定且易脆、weight tuning 成本高；当工具和错误模式持续变化时，需要能从失败抽象、压缩、
  检索且跨模型复用的外部知识，但抽象不能丢掉适用条件。
- **Mechanism / State Ownership / Flow:** failure trace→LLM 提议自然语言 atomic rule→固定字段 symbolic
  representation→以 `L(H)+L(D|H)` 权衡规则长度和失败纠正率，贪心 prune/generalize→按工具 scope
  coarse filter、symbolic-field similarity rank→top-k 规则以自然语言注入 prompt。rule library 属 Agent
  memory/policy layer，不是模型权重，也不是直接 symbolic execution engine。
- **Evaluation Contract:** ToolHop train 392/test-rand 70/test-unseen 51；BFCL Live-Multiple train 735、
  test 175/143，Multi-Turn-Base train 90、test 60/50。规则由 Llama3.2 或 GPT-4o 失败生成并复用于
  Llama3.2、Llama4、GPT-4o、o1；比较 zero-shot、few-shot、SEE、SFT/function-calling。ablation 支持
  symbolic retrieval 与 MDL consolidation 在该设置中均有贡献。
- **Evidence Boundary / Trade-offs:** 证明作者数据与模型上的 accuracy gain 和一定 cross-model reuse；
  不证明规则为因果机制、不会冲突或能安全用于 side-effectful tools。依赖可用且可靠的 failure signal；
  greedy MDL 无全局最优保证，规则质量受失败多样性限制，并新增 version、scope、supersession、review、
  deletion 与 stale-rule 风险。raw episodic memory 在需要审计具体轨迹时仍成立，weight tuning 在需要
  内化高频技能时也未被替代。
- **Evolution / ROADMAP / Decision:** `Direct Evolution`：raw trace retrieval→failure-derived rule→
  compact symbolic index→runtime retrieval。主 owner `AGENT-MEMORY` / current Ch77 / legacy Ch73，邻接
  Ch78 Tools、Ch81 Workflow；`Refine — Existing Argument`，已写入 Ch77。

### Beyond Perfect APIs

- **Candidate / Week / Score:** Beyond Perfect APIs / 2026-W01 / 25/30；
  `Source Family ID: api-complexity-agent-evaluation`。
- **Source / Date / Coverage:** arXiv:2601.00268v1，2026-01-01。已阅读 taxonomy、benchmark generation、
  isolated/cumulative protocols、10-model evaluation、error-handling judge、结果与 limitations。
- **Problem / Previous Design / Changed Constraint:** 只测 schema 正确、参数 exact match 的理想 API
  能隔离 model capability，却掩盖真实工具中的临时失败、无关字段、限制提示、含糊描述与跨 API 依赖；
  deployment contract 变化后，恢复和澄清本身成为 Agent 能力的一部分。
- **Mechanism / Flow:** 从 7 个 domain、86 个可执行 API 构造 60 个 scenarios / 32K configurations，
  注入八类 specification/execution complexity；300 个多轮 conversations 共 3,525 calls。isolated 模式
  给 gold history 测单点处理，cumulative 模式让早期错误进入后续 context，区分局部 robustness 与
  workflow error propagation。
- **Evaluation / Evidence Boundary:** 10 个模型、zero-shot ReAct、最多 15 steps；API exact-call accuracy
  与 LLM judge 共同评分。作者报告平均 degradation 与 cumulative amplification，只适用于合成注入环境；
  不证明生产 API 的真实故障分布、用户恢复体验、延迟/成本或授权安全。数据生成和部分判分使用 LLM，
  形成 generator/judge dependency。
- **Trade-offs / Evolution / Decision:** 更接近真实故障会降低可控性并增加 oracle 设计成本；理想 API
  benchmark 仍适合隔离 model planning。`Layering / Dependency`：function-call correctness→error-aware
  interaction→cumulative workflow resilience。主 owner `PLATFORM-EVALUATION-SYSTEM` / current Ch66 /
  legacy Ch62，邻接 Ch67 Observability、Ch78 Tools；`Refine — Existing Argument`，已写入 Ch66。

### Revati

- **Candidate / Week / Score:** Revati / 2026-W01 / 29/30；
  `Source Family ID: revati-control-plane-faithful-simulation`。
- **Source / Date / Coverage:** arXiv:2601.00397v1，2026-01-01。已阅读 architecture、CUDA/NCCL
  interception、virtual time、memory emulation、predictor、implementation、evaluation 与 limitations。
- **Original Problem / Previous Design / Changed Constraint:** analytical/discrete-event simulator 重写
  scheduler/control plane，速度快却会随 vLLM/SGLang 演进而语义漂移；直接在真实 GPU 上测试更可信，
  却昂贵且难做大规模 what-if。需要复用真实 control code，只替换 expensive execution substrate。
- **Mechanism / State Ownership / Control Flow:** 原 serving process 与 scheduler 照常运行；`LD_PRELOAD`
  拦截 CUDA，kernel 不执行而转换成预测 duration；central Timekeeper 以最小 target-time barrier 推进
  virtual clock。actors 可推进时间，observers 只观察；NCCL collective 被转换为同步 barrier。小于约 4MB
  的 control metadata host-backed，大 compute buffer 只保留 virtual allocation；CPU 读取虚拟大 buffer
  属 fatal unsupported path。协调失败时退化为 real sleep，而不是回滚已发生的 host control state。
- **Implementation / Evaluation Contract:** 约 800 行 C++ Timekeeper、6K 行 emulator、对框架少于 50 行
  patch；predictor 扩展 Vidur。vLLM/SGLang，Llama-3.1-8B TP1、70B TP4、Qwen3-30B-A3B EP2、
  chunked-prefill mixed batch 512；4×H200 fully-connected NVLink、AMD 9334 128 cores、ShareGPT Poisson。
  作者报告 median/tail error 与 5～17× wall-clock acceleration，只绑定上述条件。
- **Evidence Boundary / Trade-offs:** 适用于 GPU value 不回流影响 control flow、token length 可预定且
  predictor 足够准确的 workload；不证明 data-dependent GPU branches、任意 topology、kernel version、
  memory threshold 或高 jitter 下仍忠实。它用更低实验成本换来 predictor/model validity 风险；真实
  hardware replay 仍是最终 validation，纯模拟仍适合尚无可执行 control plane 的设计空间。
- **Evolution / ROADMAP / Decision:** `Direct Evolution`：abstract simulator→trace replay→真实 control
  plane + virtual GPU time。主 owner `PLATFORM-EVALUATION-SYSTEM` / current Ch66 / legacy Ch62；Ch52
  Dynamo、Ch56 Scheduling 与 Ch67 Observability 为 handoff。`Integrate — New Mechanism`，已写入 Ch66。

### FlexSpec

- **Candidate / Week / Score:** FlexSpec / 2026-W01 / 23/30；
  `Source Family ID: flexspec-edge-cloud-speculation`；Status: Emerging。
- **Source / Date / Coverage:** arXiv:2601.00644v1，2026-01-02。已阅读 anchor/draft architecture、
  adaptive speculation controller、latency model、设备/模型实验、baselines 与 limitations；v1 未提供可核验
  artifact，部分 mobile results 明确为 simulation。
- **Problem / Mechanism:** cloud target 持续 fine-tune 时，为每个版本同步 edge draft 代价高；固定 K 又
  不能适应网络带宽、draft acceptance 与 device/cloud marginal latency。方案冻结共享 anchor backbone，
  让 edge draft 对一族 target 保持近似，并由 controller 根据 EMA acceptance、channel rate 与边云延迟
  在线选择 K；cloud verifier 接受前缀并 rollback mismatch。
- **Evaluation Boundary / Trade-offs:** 涵盖 H800/A800/V100 cloud、Jetson Orin 等 edge 及若干 simulated
  devices，Llama/Mixtral 与六个 datasets；结果不能外推到所有 target drift、tokenizer/architecture 改变、
  multi-tenant cloud 或真实蜂窝 tail。冻结 anchor 降低同步成本，却把 draft aging、网络波动、privacy、
  rollback traffic 和 controller instability 变成新状态。target 稳定且同机部署时，标准 speculative
  decoding 更简单；低 acceptance/低带宽时直接 cloud decoding 仍合理。
- **Evolution / ROADMAP / Decision:** `Direct Evolution`：static draft/target pair→decoupled reusable draft→
  network-aware K control。主 owner `INFER-SPECULATIVE-DECODING` / current Ch48 / legacy Ch44，邻接
  Ch54 GPU Memory；`Refine — Existing Argument / Experimental`，已写入 Ch48。

### FwPKM

- **Candidate / Week / Score:** FwPKM / 2026-W01 / 27/30；
  `Source Family ID: forward-updated-product-key-memory`。
- **Source / Date / Coverage:** arXiv:2601.00671v1，2026-01-02。已阅读 PKM background、fast-key/value
  update equations、entropy objective、gating/lookahead、training setup、long-context tests、ablation、
  throughput 与 limitations。
- **Original Problem / Previous Design / Changed Constraint:** attention/KV 对当前 sequence 精确且通用，
  但 context 持续增长时状态和计算线性增加；静态 PKM 容量大、稀疏访问，却不能在 inference 中把新
  信息写入可跨 chunk 重读的 external parameters。变化后的约束是以低 FLOPs 持续更新长期状态。
- **Mechanism / State Ownership / Flow:** 512×512 product-key slots 经 sparse top-k addressing；每个 chunk
  在 forward/inference 内用 local MSE 对 fast keys/values 更新，key marginal-entropy 防止槽位 collapse，
  gate 混合 memory output，lookahead target 训练写入可预测未来的信息。fast weights 属 session/model
  runtime；batch 共享状态意味着 tenant/session isolation 不能省略。
- **Evaluation Contract:** QwenNext-like 12-layer hidden-768，PKM/FwPKM 位于 2/6/10 层；训练 10B
  tokens（LongContext-64 + FineWeb-Edu），训练长度 4K。每项 long-stream eval 8M tokens、batch 1；
  NIAH 500 samples、5 needles、4K～128K，并测试多次 rereading。吞吐实现显著慢于 GDN，论文没有
  efficient custom kernels。
- **Evidence Boundary / Trade-offs:** 反复 reread 的 NIAH improvement 支持 fast weight 可积累部分信息，
  但不证明一次阅读、开放域事实、并发用户或真实 agent memory；128K 两遍仍下降且更多遍才恢复。
  容量/稀疏 FLOPs 的收益换来在线更新稳定性、shared-state leakage、order dependence、忘却/污染与
  checkpoint/rollback 问题。短上下文仍由 attention 更可靠，显式 RAG 在 provenance/delete/ACL 要求
  下更可控。
- **Evolution / ROADMAP / Decision:** `Principle Reuse`：context tokens→external sparse slots→inference-
  time fast weights。主 owner `MODEL-LONG-CONTEXT` / current Ch22，`AGENT-MEMORY` 仅保留边界 handoff；
  `Integrate — New Mechanism / Experimental`，已写入 Ch22。

### OrchestrRL

- **Candidate / Week / Score:** OrchestrRL / 2026-W01 / 28/30；
  `Source Family ID: orchestrrl-compute-fabric-coordination`。
- **Source / Date / Coverage:** arXiv:2601.01209v1，2026-01-03。已阅读 RL profiling、compute scheduler、
  RFabric/OCS topology templates、cost model、physical and simulated evaluation、ablation 与 limitations。
- **Original Problem / Previous Design / Changed Constraint:** colocated synchronous RL 简化 policy
  freshness，但 generation memory/latency-bound、training compute-bound，静态 GPU allocation 会互相
  等待；单步异步可重叠，却仍受长尾请求和固定网络 topology 限制。新约束是生成、训练 phase 与通信
  pattern 都随 iteration 改变。
- **Mechanism / Ownership / Flow:** compute scheduler 主动切换 parallelism/resource allocation，并在
  generation 内做 request migration；RFabric 以 always-on EPS 提供细粒度连接，以 OCS 在预测 slack
  足够时切换 mesh/isolated-pod/tree circuit。若 `W < T_ocs` 或计划错过窗口则沿用旧 topology，避免
  reconfiguration 阻塞 critical path。scheduler 拥有 phase/queue model，fabric controller 拥有 circuit
  state；两者需要显式 epoch 和 fallback。
- **Evaluation Contract:** 72×H800 characterization 使用 Qwen2.5-14B、OpenR1 220K；physical compute-
  scheduler 评测为 48 GPUs、Qwen-14B/32B，报告 1.40×/1.34×。1024/2048 H800 的网络部分来自 RLSim，
  Qwen2.5-72B、假设 3D MEMS 10ms，并比较 FT、oversubscription、rail、TopoOpt；2.2～3.1× cost-
  efficiency 是 simulation 结论，不是物理 OCS deployment 证明。
- **Trade-offs / Previous Design Still Applies:** 联合调度可降低 phase mismatch，却引入 topology epoch、
  stale prediction、migration cost、circuit failure、control-plane race 与 optical hardware cost。物理集群
  已有高带宽 non-blocking fabric、规模较小或 RL phase 稳定时，固定网络更简单；严格 on-policy 训练
  仍需限制 async lag。
- **Evolution / ROADMAP / Decision:** `Layering / Dependency`：static colocated RL→disaggregated compute
  scheduling→phase-aware compute/fabric co-orchestration。周级 Review 将主 owner 修正为 `TRAIN-GRPO` /
  current Ch33 / legacy Ch29；`TRAIN-DISTRIBUTED-TRAINING` 与平台资源调度仅作 handoff。RFabric 维持
  `Experimental`；`Integrate — New Mechanism`，已写入 Ch33。

### Does Memory Need Graphs?

- **Candidate / Week / Score:** Does Memory Need Graphs? / 2026-W01 / 27/30；
  `Source Family ID: controlled-agent-memory-design-space`。
- **Source / Date / Coverage:** arXiv:2601.01280v1，2026-01-03。已阅读 six-tuple abstraction、stage-wise
  comparison、representations/index/maintenance/retrieval、LongMemEval/HaluMem setup、results 与 limitations。
- **Problem / Previous Design / Changed Constraint:** memory papers常同时改变 extraction、representation、
  organization、retrieval 与 answering，因此 graph improvement 无法归因；raw session memory 虽简单，
  却可能长、冗余且检索困难。需要控制变量，而不是把“graph”当单一机制标签。
- **Mechanism / State Ownership:** 用 key/value/query/index structure/index operations/retrieval/answering
  六元组统一系统；逐阶段替换 raw session、summary、fact、keyword 与 graph variants，分离 representation、
  organization、maintenance 和 retrieval 的贡献。memory system 拥有 derived representation 与索引，
  source conversation 仍是 provenance owner。
- **Evaluation Contract / Boundary:** LongMemEval 为主要 benchmark；HaluMem 只用 Medium、LLM-as-judge。
  extraction/answering 使用 Llama-3.1-8B、Contriever，8×H100 80GB。结论支持在这些 controlled settings
  中，若干 system choice 的影响可大于 graph structure，graph benefit 不普遍；不证明 graph memory 无用，
  也不覆盖 strict real-time、personalization、ACL、deletion 或开放域 agent workflow。
- **Trade-offs / Previous Design Still Applies:** graph 提供显式关系与 multi-hop traversal，却增加 extraction
  error、schema drift、maintenance 与 stale edge；session/summary 在短历史和低更新率下仍更可审计。
  derived memory 必须保留 provenance、supersession 和 rollback，否则压缩会把错误固化。
- **Evolution / ROADMAP / Decision:** `Explanatory Comparison`：raw history→derived summaries/facts→graph
  organization→controlled component attribution。主 owner `AGENT-MEMORY` / current Ch77 / legacy Ch73，
  邻接 Ch76 RAG；`Refine — Existing Argument`，已写入 Ch77。

### FLOP-Efficient Training

- **Candidate / Week / Score:** FLOP-Efficient Training / 2026-W01 / 22/30；
  `Source Family ID: ttc-aware-early-stopping`；Status: Emerging。
- **Source / Date / Coverage:** arXiv:2601.01332v1，2026-01-04。已阅读 learning-curve/TTC fitting、algorithm、
  break-even derivation、all experiments、patience/fluctuation ablation、limitations 与 appendices。代码在 v1
  只承诺未来公开。
- **Problem / Mechanism:** 传统 early stopping只看 validation curve，默认最终 checkpoint + 单次 inference；
  当 test-time sampling/search 可换取质量时，训练停止点与部署 K 应联合选择。论文用 exponential curve
  预测 full-budget accuracy，以 K=1/2/4 拟合 sigmoid 估计最小 `K*`，同时满足 accuracy 与 total-FLOPs
  inequality；patience 防止一次预测触发过早停止。
- **Evaluation Contract:** TinyLlama 1.1B、Pythia 1/2.8/6.9B、FineMath 3B 与 Qwen3-A3B-Instruct；
  HumanEval、DROP、Math-500、GSM8K；8×V100 FP16、input 1024/output 512、temperature 0.8。FineMath
  还测试 majority/DVTS/compute-optimal search。92% 是 TinyLlama 特定 checkpoint/benchmark 的 training-
  FLOPs saving；70B samples 是 3T training tokens、output 1024、`lambda≈1.2` 的 illustrative bound。
- **Evidence Boundary / Trade-offs:** 公开 intermediate checkpoints 主要≤6.9B，curve form、K extrapolation、
  verifier quality 与 task metric 可共同失配；Pass@K 不是实际单答案 accuracy。省训练换来持续更高 inference
  成本和 refresh/deployment-volume 假设；高流量长期 serving 可能越过 break-even，训练一次、推理很少
  的模型则可能受益。full training 在要求单样本质量或 TTC latency 不可接受时仍合理。
- **Evolution / ROADMAP / Decision:** `Direct Evolution`：training-only early stop→lifecycle training+inference
  objective。主 owner `TRAIN-PRETRAINING` / current Ch28 / legacy Ch24，邻接 Ch42 Inference Overview、
  Ch66 Evaluation；`Integrate — New Mechanism / Experimental`，已写入 Ch28。

### Tarragon

- **Candidate / Week / Score:** Tarragon / 2026-W01 / 29/30；
  `Source Family ID: tarragon-disaggregated-moe-fault-recovery`。
- **Source / Date / Coverage:** arXiv:2601.01310v1，2026-01-04。已阅读 architecture、ERT/REFE routing、
  shadow experts、incremental KV checkpoint、recovery protocol、implementation、failure injection、
  evaluation、ablation 与 limitations；v1 声称 code 将公开，当前未把后续 artifact 倒算为事件证据。
- **Original Problem / Previous Design / Changed Constraint:** monolithic MoE replica 将 attention/KV 与 expert
  compute 绑定，worker failure 常触发整组 restart；replica restart 语义清楚但恢复域过大。独立扩缩容又
  要解决 request state、expert placement 与 routing version 的一致性。
- **Mechanism / State Ownership / Flow:** stateful Attention Workers 持有 KV，stateless Expert Workers 执行
  experts；ERT/REFE 将 logical expert 映射到 physical worker。spare GPU memory 放 shadow experts；KV
  按 token segment 异步增量写到 RDMA checkpoint store。AW failure 后新 worker 恢复该 request KV，EW
  failure 则重路由到 shadow/provisioned expert，避免全局 replica restart。orchestrator 必须原子协调
  membership、routing epoch、checkpoint version 和 in-flight request。
- **Implementation / Evaluation Contract:** 约 16K C++ +2K Python；vLLM AW、自定义 libtorch/libibverbs
  EW、C++ orchestrator/store。3 个 GCP A3 Ultra 节点，每节点 8×H200 141GB、8×400Gbps ConnectX-7、
  NVLink 3.6Tbps；Mixtral-8x7B、8 AW +8 EW、额外 checkpoint-store node；ShareGPT 与 10-in/128-out
  random、Poisson 30～70 RPS，failure probing 10ms。64s→0.4/0.3s、1147 vs 1148 throughput、up to
  1800× restore 都只属于作者 fail-stop injection 和该 topology。
- **Evidence Boundary / Trade-offs:** 未覆盖多点/Byzantine failure、checkpoint store failure、network
  partition、跨 epoch duplicate token 或真实 spot/preemption。收益来自 spare memory、额外 store/network、
  continuous checkpoint traffic 与更复杂 control plane；pause-based checkpoint 更简单但阻塞明显。规模小、
  failure 少或 strict exactly-once 优先时，monolithic restart 仍合理。
- **Evolution / ROADMAP / Decision:** `Direct Evolution`：replica-level restart→compute/state disaggregation→
  role-specific recovery。主 owner `INFER-PD-DISAGGREGATION` / current Ch55 / legacy Ch51，邻接 Ch52
  Distributed Runtime 与 Ch56 Scheduling；`Integrate — New Mechanism / Experimental`，已写入 Ch55。

### HardGen

- **Candidate / Week / Score:** HardGen / 2026-W01 / 24/30；
  `Source Family ID: hardgen-failure-driven-tool-data`；Status: Emerging。
- **Source / Date / Coverage:** arXiv:2601.01498v1，2026-01-04。已阅读 API graph construction、trace sampling、
  tool evolution、Reasoner-Verifier loop、27K dataset、SFT/RL setup、BFCLv3/v4、ablation、manual annotation、
  training appendix 与 limitations。v1 仅承诺代码/模型/数据将开源。
- **Problem / Mechanism:** random tool/data synthesis 常生成浅层、同质轨迹。HardGen 先让两个模型在
  2,095-tool environment 自评，将共同失败的 tools 与 dependency/parameter relation 写入 API Graph；
  从 failure-prone path 采样 hard trace，再由 Tool Maker 合成 advanced tool、Hard-query Generator 构造
  logical bridge，Reasoner/Verifier 最多 3 次利用 execution feedback 修正；只有完整 M-step 调用正确才保留。
- **Evaluation Contract:** 生成 27K trajectories、1～8 calls、平均 3.21；Qwen3-30B-A3B-Thinking 作为生成
  backbone，Qwen3-4B/Llama-3-3B 做 RL ablation；SFT batch 1024、5 epochs、max length 20,480，RL batch
  512、16 rollouts。BFCLv3 用官方 script；held-out BFCLv4 提供额外验证。advanced-tool difficulty 部分由
  GPT-4o judge 并辅以人工标注。
- **Evidence Boundary / Trade-offs:** 支持 failure-driven selection、hard query 与 verifier feedback 在作者
  environment 中提高训练数据效用；不证明超过闭源模型的数字代表通用 agent capability，也不能排除
  benchmark/tool overlap、generator/judge/harness 的贡献。必须有可执行环境；proprietary API、外部 side
  effect 与不规则 tool chain 难验证。它以更高生成/执行成本换取难例，并可能过拟合当前模型的失败分布。
- **Evolution / ROADMAP / Decision:** `Direct Evolution`：random synthesis→failure-aware curriculum→
  executable verification。主 owner `TRAIN-DATA` / current Ch27 / legacy Ch23，邻接 Ch66 Evaluation、
  Ch78 Tools；`Refine — Existing Argument / Experimental`，已写入 Ch27。

### DiT-HC

- **Candidate / Week / Score:** DiT-HC / 2026-W01 / 25/30；
  `Source Family ID: dithc-cpu-training-memory-hierarchy`；Status: Emerging。
- **Source / Date / Coverage:** arXiv:2601.01500v1，2026-01-04。已阅读 LX2 architecture、CFTP、AutoMem、
  OPM/DDR movement、NUMA kernels、PyTorch/MPI backend、ImageNet/remote-sensing evaluation、scaling、
  ablation 与 limitations。
- **Original Problem / Mechanism:** GPU-centric DiT training 假设 HBM/accelerator tensor cores；高容量 CPU
  platform 若沿用 MPI tensor-parallel 会让同 die 的共享-memory traffic 仍走通信栈。CFTP 让同一 LX2 die
  内 partitions 处于同 process/shared memory，仅跨 dies 做 DP reduction；AutoMem 通过 PyTorch hooks、
  warmup/reference tracking 管理 OPM/DDR prefetch/offload，SDMA/专用 cores 搬运；NUMA/L2-aware tiling 和
  HCOps 提供算子，custom MPI backend 用 nonblocking all-reduce 与专用通信 cores。
- **Evaluation Contract:** OpenEuler 22.03、Clang17、OpenMPI、nativeBLAS+oneDNN 3.6.2、PyTorch2.5.1；
  DiT S/B/L/XL，ImageNet/Gaofen-2/Sentinel-2，并以 H100 做 accuracy validation。作者报告 single-step
  8.2× vs native CPU、CPU 13.5s vs 2×8 H100 7.6s（batch 3584），256 nodes/1024 processes weak-scaling
  90.6%；部分 tuned experiment 因 allocation 只到 128 nodes。
- **Evidence Boundary / Trade-offs:** “communication-free”只指 die 内 shared-memory tensor partition，
  不是全系统无通信；结果高度绑定 LX2 的 OPM、SDMA、core count、NUMA 与软件栈，不能外推普通 x86
  CPU 或 GPU training。收益换来硬件专用 kernel、memory planner、large-page/NUMA placement 与 backend
  维护。commodity GPU 在 dense tensor compute 和成熟 ecosystem 下仍成立，MPI process isolation 在
  fault containment/多节点边界仍有价值。
- **Evolution / ROADMAP / Decision:** `Hardware Co-design`：GPU/HBM assumption→many-core CPU memory
  hierarchy→shared-memory partition + explicit tiering。周级 Review 判定 `No Change — Already Covered`：
  `TRAIN-DISTRIBUTED-TRAINING` / current Ch36 / legacy Ch32 已具体区分 same-host shared memory、MPI
  semantics/runtime、topology mapping 与 process isolation；LX2 OPM/SDMA、专用 kernel 和作者 benchmark
  高度绑定单一硬件，未形成额外长期机制。邻接 Ch40 Megatron 与 Ch49 execution plan 已读，不新增正文。

## Evidence Level

| Claim Type | Evidence | Boundary |
| --- | --- | --- |
| 日期与版本 | arXiv metadata / v1 PDF or HTML | first-public event 固定到 W01 |
| 方法与控制流 | 论文正文、公式、算法与实现章节 | 作者公开设计，不等同生产实现 |
| 性能与质量 | 作者实验、ablation 与 appendix | 只绑定列明 workload/hardware/model |
| 跨论文演进 | 本报告综合 | 明确属于工程推断，等待人工 Review |

## Cross-Week Deduplication

- 2025-12-29～31 的首次公开事件保留在 2026-W01，不移回 2025-W52。
- arXiv 2026-01-05 首次公开的候选进入 W02；不能因编号前缀为 `2601` 混入 W01。
- RIMRULE 后续 revision、以及论文承诺但后来才公开的 code/artifact，只用于核验 source family，不倒算成
  W01 已公开能力。
- Does Memory Need Graphs? 与后续 memory papers 是 component-attribution 关系，不因都出现 graph/memory
  关键词而互相去重。

## Knowledge Tree Position

- Model/Training：`MODEL-LONG-CONTEXT` Ch22；`TRAIN-DATA` Ch27 (legacy Ch23)；
  `TRAIN-PRETRAINING` Ch28 (legacy Ch24)；`TRAIN-GRPO` Ch33 (legacy Ch29)；
  `TRAIN-DISTRIBUTED-TRAINING` Ch36 (legacy Ch32, DiT-HC No Change evidence owner)。
- Inference：`INFER-SPECULATIVE-DECODING` Ch48 (legacy Ch44)；
  `INFER-PD-DISAGGREGATION` Ch55 (legacy Ch51)。
- Platform/Agent：`PLATFORM-EVALUATION-SYSTEM` Ch66 (legacy Ch62)；
  `AGENT-MEMORY` Ch77 (legacy Ch73)。
- 本轮未发现必须新增 Part 或章节的结构性缺口；每项候选已确定唯一主 owner，跨章节仅保留短 handoff。

## Recommended Action

1. 11 个 retained candidates 的 Source-Family Books Review 已完成；以后若 discovery 新增候选，重新打开
   W01 的逐项 Integration Review，不把当前 11 项误写成 full-recall census。
2. 继续恢复可机器复算的跨类别 discovery census；在完成前保持 Archive Completion Gate Open。
3. 人工重点 Review：OrchestrRL owner 从 Distributed Training 修正为 GRPO 是否符合全书边界；以及 DiT-HC
   的 `No Change` 是否接受“不沉淀硬件专用数字，只保留既有通信/拓扑原则”的判断。

## Event-Date Daily Decision

历史回填只维护完整 ISO Weekly，不补造 2025-12-29～2026-01-04 Daily。

## Books Integration Decision

`Source-Family Books Gate Complete — 10 Integrated/Refined, 1 No Change; Archive Gate Open`。

- `AGENT-MEMORY` / Ch77：RIMRULE 与 Does Memory Need Graphs? 补全 failure-derived procedural rule、
  component attribution、provenance 与 supersession 演进。
- `PLATFORM-EVALUATION-SYSTEM` / Ch66：Beyond Perfect APIs 与 Revati 分别补全 API complexity protocol
  和 real-control-plane / virtual-execution fidelity ladder。
- `INFER-SPECULATIVE-DECODING` / Ch48：FlexSpec 补全 edge/cloud artifact reuse、network-aware K 与 fallback。
- `MODEL-LONG-CONTEXT` / Ch22：FwPKM 补全 sparse fast-weight mutable state 及 session isolation。
- `TRAIN-GRPO` / Ch33：OrchestrRL 补全 RL phase-aware compute/fabric orchestration，RFabric 保持 Experimental。
- `TRAIN-PRETRAINING` / Ch28：FLOP-Efficient Training 补全 training/test-time lifecycle break-even。
- `INFER-PD-DISAGGREGATION` / Ch55：Tarragon 补全 stateful/stateless role-specific recovery。
- `TRAIN-DATA` / Ch27：HardGen 补全 failure-driven executable curriculum。
- DiT-HC：`No Change — Already Covered`，具体章节级去重证据见 Full Source Review。

上述决定只覆盖当前已审计的 11 个 Source Families，不关闭 discovery coverage limitation。

## Ignored Noise and Below-Threshold Screening

- **PonderTTT（arXiv:2601.00894v1，2025-12-31）：** online test-time training 有研究价值，但当前命中
  与项目的 system ownership/engineering contract 关联弱，且需要与后续 revision/source family 联读；
  19/30，暂不 retained。
- **Memory Bank Compression（arXiv:2601.00756v1，2026-01-02）：** 压缩式 memory bank 在有限 QA 设置
  中有信号，但独立机制、failure semantics 与长期工程价值不足；18/30。
- **Geometric MoE analysis（arXiv:2601.00457v1，2026-01-01）：** 偏理论解释，当前未形成 router→dispatch
  的新系统机制；18/30。
- **Trajectory Guard / collusion 等关键词命中：** source date 或证据范围未达到本轮 retained 门槛，保留为
  discovery leads，不把摘要判断写成技术事实。
- 年度回顾、预测、营销 benchmark、后续日期旧内容重发均不计入。

## Repository Changes

- 删除与 canonical 文件 byte-identical 的 `papers/2026/weekly/2026-W01/README 2.md`。
- 重建本文件：撤回错误空周结论，新增 discovery reconciliation、11 个评分与 Full Source Review、
  4 个 below-threshold screening、Evidence Gate 和逐项 Books disposition。
- 更新 8 个 owner chapters：Ch22、Ch27、Ch28、Ch33、Ch48、Ch55、Ch66、Ch77；均按旧方案边界→
  约束变化→新机制→证据边界→新增 failure mode→共存条件重排，不复制 Weekly 摘要。
- 幂等更新本 Weekly 的 Stable Node ID、current/legacy chapter、最终 disposition、Repository Changes
  与 Open Questions；未生成历史 Daily。

## Open Questions

1. W01 全类别目录级 census 是否还会恢复新的 ≥20/30 候选？若恢复，必须重新打开 Books Review。
2. Revati 的 control-plane fidelity 怎样覆盖 GPU value-dependent branches 与 framework upgrade？
3. OrchestrRL 的 physical OCS、failure recovery 与 topology-epoch correctness 能否独立复现？
4. Tarragon 的 routing/checkpoint epoch 在多故障、partition 与 duplicate-token 下如何提交？
5. Agent derived memory 如何统一 rule/graph 的 provenance、supersession、ACL、delete 与 rollback；模型内部
   fast weights 又应如何保持 session isolation 而不被误归为 Agent Memory？
6. TTC-aware early stopping 在高 deployment volume 下何时越过 total-lifecycle break-even？
7. DiT-HC 的专用 CPU memory hierarchy 若出现跨硬件可复现 artifact，是否会形成超出现有 Ch36 的通用
   execution-plan principle？

## Sources

Primary sources，均于 2026-08-07 访问：

- RIMRULE v1: https://arxiv.org/pdf/2601.00086v1
- Beyond Perfect APIs v1: https://arxiv.org/html/2601.00268v1
- Revati v1: https://arxiv.org/html/2601.00397v1
- FlexSpec v1: https://arxiv.org/html/2601.00644v1
- FwPKM v1: https://arxiv.org/html/2601.00671v1
- OrchestrRL v1: https://arxiv.org/html/2601.01209v1
- Does Memory Need Graphs? v1: https://arxiv.org/html/2601.01280v1
- FLOP-Efficient Training v1: https://arxiv.org/html/2601.01332v1
- Tarragon v1: https://arxiv.org/html/2601.01310v1
- HardGen v1: https://arxiv.org/html/2601.01498v1
- DiT-HC v1: https://arxiv.org/html/2601.01500v1
- arXiv abstract/metadata pages: https://arxiv.org/abs/2601.00086 and linked candidate records
- PyTorch Releases: https://github.com/pytorch/pytorch/releases
- vLLM Releases: https://github.com/vllm-project/vllm/releases
- SGLang Releases: https://github.com/sgl-project/sglang/releases
- NVIDIA Dynamo Releases: https://github.com/ai-dynamo/dynamo/releases
