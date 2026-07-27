# AI Research Weekly — 2026-W05

> Coverage Window: 2026-01-26～2026-02-01
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31
> Discovery Recall Re-audit: 2026-08-09 — Candidate Evidence Gate Passed / 43 Full Source Reviews
> Books Review: 2026-08-13 — Source-Family Books Gate Complete / Discovery Coverage Limited

## Executive Summary

原周报只保留了 3 个候选，无法支撑“本周只有这些重要研究”的结论。本轮从 arXiv first-public
date、官方 Research publication node、作者 artifact 与 Hugging Face discovery index 重新回扫，恢复出
20 个达到 20/30 的候选，首轮账本共 23 项。新增证据覆盖 distributed post-training、low-precision RL、
hybrid model conversion、conditional-compute scaling、coding-agent data、Agent exploration、long-context
workflow evaluation、deep research completeness、domain continual pretraining 与 multi-agent credit assignment。

本周最稳定的系统结论不是某个 benchmark 数字，而是三条演进边界：

1. `collective synchronization → on-demand point-to-point` 能把同步粒度从 layer 放宽到 minibatch，
   但以跨节点通信效率、状态 ownership 与故障协议为新成本；
2. `BF16 rollout → FP8 rollout → end-to-end FP8` 需要分别处理 policy mismatch、KV capacity、MoE routing
   与 gradient range，不能把低精度写成一个开关；
3. 静态 long-context retrieval 不能代表 Agent workflow 的动态 state tracking；总 token 数相同，证据密度、
   turn fragmentation、minimum evidence span 与 stopping criteria 会产生不同 failure mode。

后续用 Hugging Face 2 月 2 日 discovery page 反查 next-business-day submissions，又恢复 20 个 arXiv v1
属于 1 月 26 日～2 月 1 日的候选。本轮补齐 PaperBanana 与 Sweet Spot Learning 的论文正文、appendix 与
官方 artifact 复核后，43 个候选已全部拥有非模板化 Full Source Review。W05 的 candidate Evidence Gate
已经通过。随后逐项阅读 owner 与相邻章节，并完成 43/43 最终 disposition：28 项 Integrate/Refine、
11 项 No Change、3 项 Weekly Only、1 项 Reject。Discovery census 仍受未完成机器可复算全量检索的限制；
因此本周 Source-Family Books Gate 已闭合，但 Archive Completion Gate 继续保持 Open。

## Coverage and Source Coverage

- **模型与研究机构：** 复核 Google Research、Anthropic Research 与 ByteDance Seed 的官方 publication
  node；官方 Blog 只用于确认事件日期或研究入口，存在论文时以论文为机制证据。
- **论文与学术来源：** 以 arXiv v1 日期固定 W05；后续 revision 只核验同一 source family，不倒算成历史
  新事件。43 项均已完成 metadata、method、implementation、evaluation、ablation/limitations 与相关 appendix
  阅读；超出单次 reader 大小限制的论文通过同一论文的可检索全文镜像恢复，并与 arXiv metadata、官方项目页
  和作者 artifact 交叉核对。
- **AI Infra 与工程：** 重点回扫训练通信、quantized RL、Agent training/runtime、coding-agent synthetic data
  与 artifact；没有把未公开机制的产品功能当作系统论文。
- **Discovery limitation：** 当前结果来自可复核的 arXiv/官方/作者 artifact 与若干 discovery index，尚不是
  `cs.AI/cs.LG/cs.CL/cs.DC/cs.CR` 的机器可复算全集。Hugging Face 页面日期仅用于发现，归周以 arXiv v1
  为准。

## Discovery Recall Reconciliation

- **Original scored rows:** 3。
- **First-pass recovered retained rows:** 20；均达到 20/30，并完成非模板化 Full Source Review。
- **Current scored rows:** 23；原有 3 项也重新复核，旧的完成性措辞已撤回为 provisional。
- **Second-pass date-verified hits:** 20；来自 2026-02-02 discovery list，但 arXiv v1 均落在 W05。20 项均完成
  Full Source Review，其中 19 项达到 20/30、1 项降为 18/30。
- **Date rule:** Scaling Agent Systems 的论文 v1 为 2025-12-09，但 Google 2026-01-28 的正式研究发布节点
  属 W05；其机制 first-public 与 publication event 分开记录。
- **Second-pass Batch A:** Golden Goose、Quartet II、ThinkSafe、R2M 与 V-pretraining 已完成全文、评分、
  revision 与 evidence boundary 复核。
- **Second-pass Batch B:** ASTRA、MemOCR、DS-MCM、KAPSO 与 PaperBanana 已完成全文、评分与 evidence
  boundary 复核；PaperBanana 的论文全文与官方项目、作者仓库联合核验，未把后续产品页面当作论文证据。
- **Second-pass Batch C:** SABER、TAM-Eval、Continual GUI Agents、RAPTOR 与 Sweet Spot Learning 已完成
  全文、评分与 evidence boundary 复核；后者的公式、实验设置、sample-efficiency、cross-task transfer、zone
  ablation 与 learned-reward discussion 均已核验。
- **Second-pass Batch D:** ReGuLaR、TTCS、Routing the Lottery、TAPPA 与 energy-performance scheduling 已
  完成全文、评分与 evidence boundary；最后一项因只有 SimPy 证据降为 18/30。
- **Gate status:** `Candidate Evidence Gate Passed / Source-Family Books Gate Complete / Discovery Coverage Limited`。
  该状态说明 43 项已发现候选均有完整证据和最终 disposition，不等于 discovery census 已穷尽；后续若恢复
  新候选，必须重新打开本周 Books Review。

### Second-Pass Candidate Ledger

以下条目记录第二轮发现及最终 disposition；`complete` 不表示达到 Books 门槛，`blocked` 也不得由摘要补写。

| Candidate | arXiv | First-public Date | Current Status |
| --- | --- | --- | --- |
| PaperBanana | 2601.23265 | 2026-01-30 | 23/30；Full Source Review complete；No Change |
| Golden Goose | 2601.22975 | 2026-01-30 | 28/30；Full Source Review complete；Refine Ch27 |
| Quartet II | 2601.22813 | 2026-01-30 | 29/30；Full Source Review complete；Refine Ch28 |
| ASTRA | 2601.21558 | 2026-01-29 | 28/30；Full Source Review complete；Refine Ch27 |
| THINKSAFE | 2601.23143 | 2026-01-30 | 27/30；Full Source Review complete；Refine Ch72 |
| ReGuLaR | 2601.23184 | 2026-01-30 | 26/30；Full Source Review complete；Integrate Ch18 / Experimental |
| TTCS | 2601.22628 | 2026-01-30 | 26/30；Full Source Review complete；Weekly Only / Experimental |
| MemOCR | 2601.21468 | 2026-01-29 | 27/30；Full Source Review complete；Refine Ch77 / Experimental |
| Statistical Estimation of Adversarial Risk under Best-of-N | 2601.22636 | 2026-01-30 | 29/30；Full Source Review complete；Integrate Ch66 |
| Real-Time Aligned Reward Model | 2601.22664 | 2026-01-30 | 26/30；Full Source Review complete；Refine Ch31 / Experimental |
| Sweet Spot Learning | 2601.22491 | 2026-01-30 | 25/30；Full Source Review complete；Refine Ch33 |
| TAM-Eval | 2601.18241 | 2026-01-26 | 27/30；Full Source Review complete；Integrate Ch66 |
| Deep Search with Hierarchical Meta-Cognitive Monitoring | 2601.23188 | 2026-01-30 | 25/30；Full Source Review complete；Refine Ch80 / Experimental |
| RAPTOR | 2602.00158 | 2026-01-29 | 24/30；Full Source Review complete；No Change / Experimental |
| Continual GUI Agents | 2601.20732 | 2026-01-28 | 26/30；Full Source Review complete；Refine Ch33 / Experimental |
| Routing the Lottery | 2601.22141 | 2026-01-29 | 21/30；Full Source Review complete；Weekly only |
| Why Attention Patterns Exist | 2601.21709 | 2026-01-29 | 28/30；Full Source Review complete；Integrate Ch45 |
| Learning What to Predict | 2601.22108 | 2026-01-29 | 28/30；Full Source Review complete；Integrate Ch28 |
| KAPSO | 2601.21526 | 2026-01-29 | 28/30；Full Source Review complete；Refine Ch81 |
| ML for Energy-Performance-aware Scheduling | 2601.23134 | 2026-01-30 | 18/30；Full Source Review complete；Reject：simulation only |

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Scaling Agent Systems | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | No Change — Ch82 已覆盖 topology/capability/error amplification |
| Post-LayerNorm Is Back / Keel | 4 | 4 | 3 | 3 | 4 | 5 | 23/30 | No Change — Ch17 已覆盖 controlled Post-LN coexistence |
| AI assistance and coding skills | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Weekly Only — human-learning evidence |
| DeepPlanning | 4 | 4 | 5 | 4 | 4 | 4 | 25/30 | No Change — Ch79 已覆盖 typed global planning |
| daVinci-Dev | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Refine — `TRAIN-DATA` repository-native trajectories |
| FP8-RL | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine — `TRAIN-GRPO` precision-flow identity |
| SAGE data synthesis | 4 | 4 | 5 | 4 | 4 | 4 | 25/30 | No Change — Ch27 failure-driven curriculum 已覆盖 |
| Revisiting Parameter Server / ODC | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Integrate — `TRAIN-DISTRIBUTED-TRAINING` minibatch commit |
| AACR-Bench | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | No Change — Ch66 environment/distribution contract 已覆盖 |
| TRACE reward-hack detection | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | No Change — Ch66 scorer/sensor boundary 已覆盖 |
| SPARK dynamic branching | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Integrate — `AGENT-PLANNING` dynamic branching |
| SERA soft-verified repository agents | 4 | 5 | 5 | 4 | 4 | 3 | 25/30 | Refine — `TRAIN-DATA` soft-verification boundary |
| Scaling Embeddings | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Integrate — `MODEL-EMBEDDING` hashed n-gram capacity |
| ConceptMoE | 5 | 5 | 5 | 4 | 4 | 4 | 27/30 | Integrate — `MODEL-MOE` sequence compression before routing |
| Token-level capability filtering | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Refine — `PLATFORM-SECURITY` training-state boundary |
| AgentLongBench | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` evidence shape |
| Self-Improving Pretraining | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | No Change — Ch27/28 teacher-feedback loop 已覆盖 |
| HALO / HypeNet | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Integrate — `MODEL-LONG-CONTEXT` hybrid-state migration |
| DeepSearchQA | 4 | 4 | 5 | 5 | 4 | 3 | 25/30 | Refine — `AGENT-RAG` set completeness and stopping |
| ECO quantized training | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Integrate — `TRAIN-PRETRAINING` low-bit graph |
| Mechanistic Data Attribution | 5 | 4 | 3 | 4 | 5 | 5 | 26/30 | No Change — Ch5 causal evidence ladder 已覆盖 |
| RedSage | 4 | 4 | 5 | 4 | 4 | 3 | 24/30 | No Change — Ch27/72 domain data-security chain 已覆盖 |
| MAPPA process rewards | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Refine — `TRAIN-GRPO` role-conditioned credit |
| Golden Goose | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine — `TRAIN-DATA` policy-relative learnability |
| Quartet II | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Refine — `TRAIN-PRETRAINING` stochastic low-bit update |
| THINKSAFE | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Refine — `PLATFORM-SECURITY` safety-data feedback loop |
| Real-Time Aligned Reward Model | 4 | 5 | 4 | 3 | 5 | 5 | 26/30 | Refine — `TRAIN-RLHF` policy-relative RM state |
| Learning What to Predict | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Integrate — `TRAIN-PRETRAINING` feedback-guided objective |
| ASTRA | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine — `TRAIN-DATA` stateful executable tool graph |
| MemOCR | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Refine — `AGENT-MEMORY` visual compression branch |
| Deep Search with Hierarchical Meta-Cognitive Monitoring | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | Refine — `AGENT-REFLECTION` selective monitor |
| KAPSO | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Refine — `AGENT-WORKFLOW` repository-as-state loop |
| PaperBanana | 4 | 3 | 4 | 4 | 4 | 4 | 23/30 | No Change — Ch24/81 generation–critic workflow 已覆盖 |
| Statistical Estimation of Adversarial Risk under Best-of-N | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Integrate — `PLATFORM-EVALUATION-SYSTEM` risk curve |
| TAM-Eval | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | Integrate — `PLATFORM-EVALUATION-SYSTEM` maintenance strength |
| Continual GUI Agents | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Refine — `TRAIN-GRPO` continual adaptation contract |
| RAPTOR | 4 | 3 | 4 | 4 | 5 | 4 | 24/30 | No Change — Ch5 probe-to-intervention ladder 已覆盖 |
| Sweet Spot Learning | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `TRAIN-GRPO` bounded proximity zones |
| ReGuLaR | 5 | 4 | 4 | 3 | 5 | 5 | 26/30 | Integrate — `MODEL-DECODER-ONLY` latent-state branch |
| TTCS | 5 | 4 | 4 | 3 | 5 | 5 | 26/30 | Weekly Only — Experimental transductive protocol |
| Routing the Lottery | 4 | 3 | 3 | 3 | 4 | 4 | 21/30 | Weekly only；no LLM-system claim |
| Why Attention Patterns Exist / TAPPA | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Integrate — `INFER-KV-CACHE` temporal-pattern budget signal |
| ML for Energy-Performance-aware Scheduling | 3 | 3 | 3 | 3 | 2 | 4 | 18/30 | Reject；simulation-only evidence |

## Deep Analysis 1 — ODC：改变同步粒度，不等于消灭同步

### Why → Principle → Mechanism

FSDP 的 all-gather / reduce-scatter 在每层形成 collective barrier；长短序列混排时，最快设备也必须等待
最慢设备。ODC 保留参数、梯度和 optimizer state 的分片 ownership，却把 collective 拆为按需 gather 与
scatter-accumulate：worker 就绪后主动拉取参数、推送梯度，minibatch 结束时再同步 optimizer semantics。

```text
layer-level collective barrier
→ point-to-point parameter fetch / gradient push
→ per-device independent microbatch progress
→ minibatch-level synchronous update
```

### Trade-off → Connection → Evolution

收益来自 workload imbalance，而不是通信本身更快。作者 microbenchmark 显示跨节点 ODC 明显慢于 NCCL
collective，因为 point-to-point RDMA 放弃了 hierarchical collective optimization。长序列计算可隐藏该成本，
短序列或网络受限场景则可能失去收益；hybrid sharding 可减少跨节点 traffic，却增加内存。它是 classic
Parameter Server 的 ownership principle 与现代 sharded DP 的重新组合，不是回到 centralized PS，也不意味着
bounded-staleness/asynchronous SGD 已被解决。

## Deep Analysis 2 — FP8-RL：低精度路径必须按状态与阶段拆开验证

### Why → Principle → Mechanism

RL 系统常由 BF16 trainer 生成权重、FP8 rollout engine 执行推理；这种混合精度同时改变 policy logits、KV
capacity、MoE routing 与训练 gradient range。论文按阶段区分 W8A8 attention/MLP/expert、FP8 KV calibration、
token-level importance sampling 与 end-to-end FP8。embedding、normalization 和 lm_head 等敏感路径并未简单
全部量化。

### Trade-off → Connection → Evolution

FP8 KV 的主要收益来自 cache capacity 增大、preemption 减少，依赖 memory-bound workload；token-level
importance sampling 只能修正可计算的 rollout/training policy mismatch，不能修复 MoE routing discontinuity。
作者的 pure E4M3 backward 因 gradient overflow 失败，最终采用 E4M3 forward / E5M2 backward。因而演进路线是
`inference-only quantization → rollout policy correction → routing-sensitive mixed precision → end-to-end range design`，
而不是“FP8 与 BF16 等价”。

## Deep Analysis 3 — AgentLongBench 与 DeepSearchQA：长度之外还有证据形状

### Why → Principle → Mechanism

静态 needle retrieval 保持 context 不变；真实 Agent 的 context 由自己的 tool/action trajectory 生成，早期选择会
改变后续 evidence。AgentLongBench 用 deterministic environment rollout 比较多 turns 的 concise history 与少
turns、高密度的 verbose tool logs；DeepSearchQA 则用 complete answer set 测量系统化搜集、entity resolution、
precision/recall 与停止条件。

### Trade-off → Connection → Evolution

同样总长度下，long-turn fragmentation 主要压迫 belief-state retention；dense tool response 主要压迫 evidence
localization 和 set operation。RAG/summary 的 lossy compression 在“每个历史约束都是必要前提”时可能切断逻辑链；
扩大搜索又会带来 hedging 与 extraneous answers。更合理的演进不是无限增大 window，而是显式维护 typed state、
provenance、coverage、dedup、stopping evidence 与 lossless/lossy boundary。

## Full Source Review

### Scaling Agent Systems

- **Source / dates / coverage:** Google Research 2026-01-28 publication node；论文 v1 2025-12-09、v3
  2026-04-08。已复核 topology/task formalization、260 configurations、六 benchmarks、regression、robustness、
  implementation appendix 与 limitations。
- **Problem / old design:** single agent 统一 history、低协调成本；parallel、centralized、decentralized 与 hybrid
  topology 分别换取 diversity、verification 或 information sharing。
- **Mechanism / state flow:** agent 持有 local history，environment 产生 observation，orchestrator 管理 aggregation、
  persistence、termination；跨 agent message 是有损 transfer，不是免费 shared memory。
- **Evidence boundary:** 支持 task–topology alignment、capability saturation 与 error amplification；有限 task
  subsets、最多九 agents，不能把论文阈值或百分比写成系统定律。
- **Evolution / ROADMAP / decision:** `Direct Evolution`；Ch78 主 owner，Ch75/77/80 相邻。既有覆盖重新变为
  `Final Books disposition recorded in Candidate Scoring ledger`，不在本步骤确认 No Change。

### Post-LayerNorm Is Back / Keel

- **Source / coverage:** arXiv:2601.19895，v1 2026-01-27；Seed 2026-01-30 publication node。已读理论、Highway
  residual architecture、64～1024+ layer experiments、ablation 与 limitations。
- **Problem / old design:** Pre-LN 为深模型提供成熟优化稳定性；Post-LN 的强层间变换伴随 gradient instability。
- **Mechanism:** Keel 用 gated carry/transform path 控制 forward/backward signal，而非简单移动 normalization。
- **Evidence boundary / trade-off:** 作者配置支持可控 Post-LN 分支；不证明普遍优于 Pre-LN。gate 增加参数、
  kernel/fusion 和 optimization coupling，production-scale replication 不足。
- **ROADMAP / decision:** `Direct Evolution`，Ch17 主 owner，Ch14～16/24 相邻；原 Ch17 修改保留为 provisional，
  `Final Books disposition recorded in Candidate Scoring ledger`。

### AI Assistance and Coding Skills

- **Source / coverage:** Anthropic 官方研究与 arXiv:2601.20245，2026-01-29；已读 randomized assignment、quiz、
  screen-recording annotation、interaction modes 与 limitations。
- **Evaluation contract:** 52 名主要 junior Python developers，在一小时 Trio task 后完成 debugging/code/concept
  quiz；treatment 平均 quiz 50%、control 67%，task time 无显著差异。
- **Evidence boundary:** 单 library、小样本、已知后测与 chat-sidebar UI 不能外推长期 productivity、expert teams
  或 coding agents。
- **Principle / decision:** implementation 可外包而 supervision mental model 未必形成；Ch62/69/77 相关，
  `Weekly evidence / Final Books disposition recorded in Candidate Scoring ledger`。

### DeepPlanning

- **Source / coverage:** arXiv:2601.18137，v1 2026-01-26；已读 dataset construction、tool sandbox、global
  optimization、agent runs、grading 与 error analysis。
- **Problem / mechanism:** 传统 QA 只验证单点答案；任务要求主动补信息、调用多 API、维护 constraints，再做
  global plan optimization。120 travel + 120 shopping tasks 在 offline sandbox 中执行。
- **Evaluation contract:** 9/15 APIs、最多 400 tool calls、四次运行；travel natural-language grading 含
  Qwen-Plus-2507 parser。最佳系统仍只有约 35% travel fully correct。
- **Boundary / trade-off:** 两个合成 domain、唯一解与封闭 API 限制外推；更强 planner 增加调用成本、state
  drift 与 grader dependence。
- **ROADMAP / decision:** Ch75 Planning 主 owner，Ch62/77 相邻；`Final Books disposition recorded in Candidate Scoring ledger`。

### daVinci-Dev

- **Source / coverage:** arXiv:2601.18418，v1 2026-01-26、v2 01-27；已读 data pipeline、trajectory generation、
  training、decontamination、SWE-Bench evaluation 与 appendices。
- **Mechanism / data flow:** contextually-native PR corpus 提供 breadth；environmentally-native Docker/tool/test
  rollouts提供 execution feedback。GLM-4.6 生成最多四条 rollout，包含 passing 与 failing trajectory。
- **Contract:** 26.7B general + 41.9B Python PR tokens；3.1B raw environment tokens（约 4.5B effective）；
  Qwen2.5-32B/72B，SWE-Bench Verified，并移除 benchmark repositories。
- **Boundary / trade-off:** PR authenticity 与 executable feedback 互补；环境数据昂贵、依赖 scaffold/teacher，
  不能从 benchmark 提升推出 production coding correctness。
- **ROADMAP / decision:** Ch27 data、Ch73 trajectory memory、Ch77 coding workflow；`Final Books disposition recorded in Candidate Scoring ledger`。

### FP8-RL

- **Source / coverage:** arXiv:2601.18150，v1 2026-01-26，后续 v2 仅核验 revision；已读 quantization path、
  TIS、KV calibration、MoE routing、end-to-end training、evaluation 与 failure analysis。
- **Mechanism / ownership:** trainer 持有 BF16/FP8 train state，rollout engine 持有量化权重/KV；每次同步重新
  quantize，TIS 校正 token policy ratio，router 保留 BF16 以降低 route mismatch。
- **Contract:** Qwen3-8B（8×H100）与 30B-A3B（2×8 H100），DAPO/AIME24，max response 20K，group 16；
  end-to-end tests 到 4×8 H100。性能数字只属于这些条件。
- **Boundary / failure:** KV gain依赖 cache-bound/preemption；TIS 不能修复 discrete route change；pure E4M3
  backward 因 fc1 gradient overflow collapse。
- **ROADMAP / decision:** Ch29 RL pipeline、Ch45 quantization、Ch49 KV；`Final Books disposition recorded in Candidate Scoring ledger`。

### SAGE Data Synthesis

- **Source / coverage:** arXiv:2601.18202，v1 2026-01-26；已读 generator/search-agent loop、hardness control、
  training transfer、ablation 与 limitations。
- **Mechanism:** generator 生成需多步检索的问题，search agent 执行并把失败/难度反馈给 generator；正确且有
  足够 search steps 的样本进入训练。
- **Contract:** Wikipedia 2018 + E5 retriever（每次 3 passages），20K training samples，Qwen 3B/7B；最多
  两轮反馈最佳，三轮更难但 learnability 下降。
- **Boundary:** 单一 corpus、≤7B、固定检索环境；向 Google Search 的 transfer 不等于 open-web robustness。
- **ROADMAP / decision:** Ch23 data curation、Ch27 SFT、Ch76 tool use；`Final Books disposition recorded in Candidate Scoring ledger`。

### Revisiting Parameter Server / ODC

- **Source / coverage:** arXiv:2601.19362，v1 落 W05；已读 FSDP barriers、ODC protocol、RDMA implementation、
  load balancing、parametric study、communication benchmark、discussion 与 appendices。
- **Mechanism / state:** 参数、gradient 与 optimizer shard 仍由各 device ownership；CUDA IPC/NVSHMEM 实现
  non-intrusive fetch/push，gradient accumulation daemon 在 minibatch end 交付同步 update。
- **Contract:** LongAlign、SWE-Smith SFT 与 GRPO/AIME；DeepSeek-R1-Distill-Qwen 1.5B～32B，最多 32×A100
  80GB，NVSwitch + per-node 800Gbps RoCE；RL time 不含 rollout。
- **Proves / not proves:** 在不均衡长序列 workload 下作者报告最高 36% SFT、10% RL training speedup；不证明
  balanced/short/network-bound workload 获益，也未实现 async SGD、elasticity 或 fault tolerance。
- **Trade-off / evolution:** cross-node point-to-point 更慢，hybrid sharding 用内存换网络；`Direct Evolution`：
  FSDP collective → decentralized PS-like ODC。Ch32 主 owner，Ch31/33 相邻；`Final Books disposition recorded in Candidate Scoring ledger`。

### AACR-Bench

- **Source / coverage:** arXiv:2601.19494，v1 落 W05；已读 curation、expert annotation、context taxonomy、
  retrieval/agent evaluation、language analysis、error cases 与 appendices。
- **Dataset / state:** 200 PR、50 repos、10 languages、1,505 comments；754 diff、518 file、233 repo-level。
  六模型补全候选 comments，再由专家 annotation，因而 ground truth 不是纯自然 review distribution。
- **Evidence:** context 并非单调增益；retrieval noise 会降低 local defect detection，Agent 可能 context tunneling。
- **Boundary:** benchmark 的 model-augmented labels、semantic matching 与 selected repos 限制外推；不能据此给某
  model 排定通用 code-review 能力。
- **ROADMAP / decision:** Ch62 evaluation contract、Ch77 coding workflow；`Final Books disposition recorded in Candidate Scoring ledger`。

### TRACE Reward-Hack Detection

- **Source / coverage:** arXiv:2601.20103，v1 2026-01-27；已读 taxonomy、trajectory generation、human
  verification、contrastive detector、evaluation 与 error analysis。
- **Mechanism:** 将单条 trajectory 与同任务的 benign/other trajectories 组成 cluster，利用跨轨迹差异识别
  semantic reward hacking；detector 不拥有 enforcement authority。
- **Contract:** 517 trajectories、54 categories、249 benign、平均 26 turns；3 engineers，kappa 0.82，约 81%
  acceptance；cluster size 1/5/10，open models 在 H200 上运行。
- **Boundary:** 大量 synthetic cases，结果依赖 cluster composition；semantic hacks 仍显著更难，不能当 runtime
  guarantee。
- **ROADMAP / decision:** Ch62/66/68；`Final Books disposition recorded in Candidate Scoring ledger`。

### SPARK Dynamic Branching

- **Source / coverage:** arXiv:2601.20209，v1 落 W05；已读 POMDP formalization、branching algorithm、GRPO、
  three environments、ablations、budget sensitivity 与 limitations。
- **Mechanism / state:** policy 通过 `<explore>` 暴露 epistemic uncertainty；每个 root 局部展开，global leaf
  budget N=8 限制 breadth。300 trajectories 冷启动，90% 由 Kimi-K2 retro-annotation。
- **Contract:** Qwen2.5-1.5B/7B，ALFWorld/ScienceWorld/WebShop，120 RL steps、batch16、single seed；固定
  branching 与 root-count/budget ablations。
- **Boundary:** 自报 uncertainty 依赖 base-model self-awareness；teacher-generated tag 与小模型/模拟环境限制
  generalization，不能把作者 success rate 外推生产 Agent。
- **ROADMAP / decision:** Ch29 RL、Ch75 planning、Ch78 topology；`Final Books disposition recorded in Candidate Scoring ledger`。

### SERA Soft-Verified Repository Agents

- **Source / coverage:** arXiv:2601.20789，v1 落 W05、v3 仅核验 revision；已读 SVG 两阶段 rollout、line-level
  recall、training、controlled comparison、specialization、ablation、variance 与 limitations。
- **Mechanism / flow:** teacher 先从随机 function/bug prompt 生成 reference patch，再把 trajectory 转成 synthetic
  PR；第二次 rollout 重做任务，以 patch line recall 分 hard/soft/unverified。训练价值被定义为 navigation 与
  intent-to-edit skill，而非每条 patch 的可执行正确性。
- **Contract:** Qwen3 8B/32B，GLM teachers，SWE-Bench Verified；context 32K/64K 分组，结果平均三 seeds。
  repo specialization 在 Django/Sympy/Sphinx 测试。
- **Boundary / failure:** soft/no verification 在当前数据和模型规模接近 hard verification；作者明确未验证更大
  model/data 饱和区，届时正确 code 可能再次成为必要条件。line overlap 也不是 semantic correctness。
- **ROADMAP / decision:** Ch27 data、Ch62 evaluation、Ch77 workflow；`Experimental / Final Books disposition recorded in Candidate Scoring ledger`。

### Scaling Embeddings

- **Source / coverage:** arXiv:2601.21204，v1 2026-01-29；已读 hashed n-gram embeddings、allocation laws、
  scale experiments、LongCat case、inference kernels/cache 与 limitations。
- **Mechanism:** 把部分参数/FLOPs 从 MoE experts 转到 hashed n-gram embeddings；N-gram 多 hash 聚合增加
  lexical capacity，同时 collision 与 cache identity 成为新状态。
- **Contract:** 280M/790M/1.3B active models、300B tokens；LongCat Lite 68.5B total、2.9～4.5B active，
  11T pretrain +1.5T midtrain；inference 在 8×H800、ISL4K/OSL1K。
- **Boundary / trade-off:** 仅在 expert sparsity diminishing-return 区间显示优势；过度分配 embeddings 或更深网络
  会衰减收益。吞吐依赖大 effective batch、spec decode、cache/custom kernels。
- **ROADMAP / decision:** Ch11 tokenizer/embedding、Ch21 MoE、Ch45 inference；`Final Books disposition recorded in Candidate Scoring ledger`。

### ConceptMoE

- **Source / coverage:** arXiv:2601.21420，v1 2026-01-29；已读 semantic boundary/chunk、concept compression、
  matched-compute strategies、long-context training、latency evaluation 与 ablations。
- **Mechanism:** encoder 将 token 转为 chunks/concepts，MoE 在 compressed sequence 上计算，再 dechunk/decoder；
  compression ratio R 改变 attention state length 与 per-token compute allocation。
- **Contract:** 12B～300B total trials；CT 90B 从 700B + 400B 32K + 40B 128K + 3B SFT；Hopper latency、
  prefill 4K～1024K、decode KV4K～64K、batch256。论文比较时不计 attention-map FLOPs。
- **Boundary:** R=4 损害 reasoning/math，R≈1.5～2 更稳；boundary distribution drift、noise regularization 与
  decoder reconstruction 是新增 failure modes。
- **ROADMAP / decision:** Ch14 architecture、Ch21 MoE、Ch22 long context、Ch45 serving；`Final Books disposition recorded in Candidate Scoring ledger`。

### Token-Level Capability Filtering

- **Source / coverage:** arXiv:2601.21571，v1 2026-01-29、v2 01-30；已读 classifier construction、loss mask/
  token removal、scaling interpolation、adversarial fine-tuning、ablations 与 limitations。
- **Mechanism / ownership:** Gemma2-9B SAE labels 蒸馏为 224M bidirectional classifier；data pipeline 对 token
  打 capability mask。loss masking 保持 sequence context，token removal 更强但破坏 syntax/distribution。
- **Contract:** medical proxy、FineWeb-Edu、61M～1.8B models、H200；“7000×”为 matched-loss interpolation，
  不是通用 compute law。
- **Boundary:** relevance classifier 不是 causal attribution；只测 medical proxy 与小规模，tools/in-context 可
  reacquire capability，larger scale 可能 U-shaped。
- **ROADMAP / decision:** Ch23 data、Ch24 pretraining、Ch68 governance；`Final Books disposition recorded in Candidate Scoring ledger`。

### AgentLongBench

- **Source / coverage:** arXiv:2601.20730，v1 2026-01-28、v3 01-30；因 HTML 缺失，已读 26 页 PDF、task
  generation、models/memory baselines、analysis、metric 与 appendices。
- **Mechanism:** deterministic lateral-thinking environment 生成 `[tool use, tool response, guess, environment
  response]` rollout；Knowledge-Free masking 分离 parametric memory，concise/verbose 控制 turns 与 density。
- **Contract:** 32 task types，32K～4M、每长度 800 samples；proprietary/open models 及 RAG、A-Mem、Mem0、
  MemoryOS。不同模型最大 context 不同，不能直接视为同等成本比较。
- **Evidence:** external memory 在该 benchmark 未稳定超过 Qwen3-30B backbone；这说明 lossy retrieval 可能切断
  necessary constraints，不证明所有 memory system 无效。
- **ROADMAP / decision:** Ch22 long context、Ch62 evaluation、Ch73 memory、Ch77 workflow；`Final Books disposition recorded in Candidate Scoring ledger`。

### Self-Improving Pretraining

- **Source / coverage:** arXiv:2601.21343，v1 2026-01-29；后续 v3 只核验 revision。已读 suffix rewriting、
  Online DPO/RF-NLL、thought mid-training、RLVR transfer、evaluation 与 limitations。
- **Mechanism:** stronger model 重写 suffix 并 judge policy rollouts；student 用 preference/filtered NLL 更新。
  另一分支插入 teacher thought，先 SFT 再以 DrGRPO 训练 suffix prediction，最后接 RLVR。
- **Contract:** Llama2 1.4B、Llama3/Qwen3 8B；Slim/RedPajama、DCLM/FineMath、DAPO Math14k；teacher/judge
  包含 GPT-OSS-120B 与 Llama3。
- **Boundary:** 多项评测依赖 judge，synthetic distribution 和 small-model setting 限制外推；部分 Qwen SFT
  stage 先退化、后由 RL 恢复。
- **ROADMAP / decision:** Ch23/24 data-pretraining、Ch27 SFT、Ch29 RL；`Experimental / Final Books disposition recorded in Candidate Scoring ledger`。

### HALO / HypeNet

- **Source / coverage:** arXiv:2601.22156，v1 2026-01-29；已读 layer conversion、selection score、distillation、
  long-context stage、single-GPU eval 与 limitations。
- **Mechanism:** 从 Qwen3 1.7/4/8B 出发，以 per-layer hidden-state MSE 转换，按 recall/CSR 保留约 25% attention，
  再做 KL distillation 与 long-context finetune；HyPE 将 RoPE 用于 RNN、NoPE attention 配 dynamic logit scaling。
- **Contract:** 总 conversion 约 2.3B tokens；单 A800、PyTorch2.9.1/CUDA12.4、batch1、BF16；long-context
  主要含 NIAH，512K speed 为作者设置。
- **Boundary / trade-off:** model 约增大 10%，GQA→MHA 与 gates 改变 kernel/state；FineWeb-Edu conversion
  可能侵蚀 instruction/alignment，且只测 transformer source。
- **ROADMAP / decision:** Ch14/15 architecture、Ch22 context、Ch45 inference；`Final Books disposition recorded in Candidate Scoring ledger`。

### DeepSearchQA

- **Source / coverage:** arXiv:2601.20975，v1 落 W05；已读 900-prompt construction、three-reviewer verification、
  set metrics、LLM judge、model evaluation、failure cases 与 limitations。
- **Mechanism / state:** task 以 causal dependency chain 聚合多源答案；最终 state 必须包含 entity identity、
  satisfied constraints、source provenance 与 stopping evidence。F1 同时惩罚遗漏与 hedging。
- **Contract:** 17 fields、time-anchored/static sources；Gemini 2.5 Flash zero-shot judge 做 semantic matching；
  outcome-only grading不观测 trajectory quality或 browsing cost。
- **Boundary:** leaderboard 比较混合 standalone models 与 deep-research agents，成本/工具栈不统一；ground truth
  仍可能受 web availability 和 judge equivalence 影响。
- **ROADMAP / decision:** Ch62 evaluation、Ch76 tools、Ch77 workflow；`Final Books disposition recorded in Candidate Scoring ledger`。

### ECO Quantized Training

- **Source / coverage:** arXiv:2601.22101，v1 2026-01-29；已读 quantized optimizer path、error feedback、
  convergence assumptions、dense/MoE experiments、rounding ablation 与 memory accounting。
- **Mechanism / state:** 去掉 full-precision master weights；每 step quantize 权重，并把 quantization error 注入
  optimizer momentum，不增加独立 error buffer。
- **Contract:** 30M～800M dense、Gemma3-1B、2.1B SMoE FP8、DeepSeek-MoE16B INT4 finetune；理论假设
  smoothness、bounded gradient 与 unbiased/bounded-variance quantization。
- **Boundary / trade-off:** 12→9 bytes/param 的 25% 仅在 static-state dominated accounting；stochastic rounding
  最符合理论，round-to-nearest 显示更高 noise floor。
- **ROADMAP / decision:** Ch24 pretraining、Ch32 distributed training、Ch45 quantization；`Final Books disposition recorded in Candidate Scoring ledger`。

### Mechanistic Data Attribution

- **Source / coverage:** arXiv:2601.21996，v1 2026-01-29；已读 EK-FAC influence approximation、component
  subspace、induction-head cases、causal remove/augment retraining、scale test 与 limitations。
- **Mechanism:** 在选定 component/activation subspace 中计算 training-example influence，把 behavioral pattern
  追溯到 data clusters，再以数据移除/增强做 causal validation。
- **Contract:** Pythia 14M～160M 做 causal retraining；OLMo 1B/7B 只验证 tracing scalability；8×A100，约
  800 GPU-hours。自动 pattern extraction 使用 DeepSeek-V3。
- **Boundary:** 组件选择与 curvature approximation 限制 completeness；large-model evidence 没有 causal
  retraining，不能把 attribution score 当完整因果解释。
- **ROADMAP / decision:** Ch5 interpretability、Ch23 data lineage；`Experimental / Final Books disposition recorded in Candidate Scoring ledger`。

### RedSage

- **Source / coverage:** arXiv:2601.22159，v1 落 W05、v2 仅核验 revision；已读 data filtering、CPT/SFT/DPO、
  benchmark generation/verification、evaluation、training cost 与 limitations。
- **Mechanism / data flow:** ModernBERT classifier 从 FineWeb 过滤 cyber corpus，混入 30% FineWeb-Edu replay，
  MinHash-LSH dedup；再用 curated seed 与 agentic augmentation 生成 multi-turn SFT，最后 DPO。
- **Contract:** 最终 CyberFineWeb 约 11.7B tokens，RedSage-Seed 28,637 items，RedSage-Conv 266K；Qwen3-8B，
  CPT 32×A100-64GB、ZeRO-3、global batch1024。
- **Boundary:** benchmark 与 training data 均部分由 LLM 生成，虽有 audit/decontamination 仍可能共享 bias；
  domain benchmark 优势不等于 interactive cyber-agent safety，且包含 dual-use 风险。
- **ROADMAP / decision:** Ch23 data、Ch24 pretraining、Ch27 post-training、Ch62/68 evaluation/security；`Final Books disposition recorded in Candidate Scoring ledger`。

### MAPPA Process Rewards

- **Source / coverage:** arXiv:2601.23228，v1 2026-01-30；已读 per-action coach reward、REINFORCE++、distributed
  runtime、MathChat/DSBench、specialization bias、reward backprop appendix 与 cost。
- **Mechanism / state:** 每 agent 拥有独立 policy parameters；coach 按 role/input/action/tool feedback 给 0～10
  process score。由于 upstream stochastic output 导致 intermediate states 不同，使用 global-normalized
  REINFORCE++ 而非 same-prompt group normalization。
- **Runtime:** Ray coordination、vLLM rollout、ZeRO-3 training；trajectory 按 agent routing，NCCL/IPC 同步权重，
  coach evaluation overlap。单节点 8×H100；coach call 是主要 latency/cost。
- **Contract:** MathChat 512 train、30 AIME25 +32 AMC test；DSBench 64 train +6 held-out tasks。只做 single
  training run、报告 best checkpoint，存在 optimistic bias。
- **Failure / trade-off:** stateless coach 对 regression 系统性高分，引发 classification regression；dense reward
  增加 judge bias、API dependency 与 reward hacking。不能由两种 sequential topology 推出 multi-agent 普遍可扩展。
- **ROADMAP / decision:** Ch29 RL、Ch62 evaluation、Ch78 multi-agent、Ch80 platform；`Final Books disposition recorded in Candidate Scoring ledger`。

### Golden Goose

- **Source / coverage / revision:** arXiv:2601.22975，v1 2026-01-30、v2 2026-02-02；W05 按 v1 固定。
  已读 data synthesis、source corpora、MCQ/open-ended 与 distractor ablation、ProRL recipe、15-benchmark
  evaluation、cyber experiment、related work、conclusion/impact 与 synthesis/training appendices。
- **Problem / previous design:** RLVR 依赖可执行 code、math verifier 或人工构造 environment，correctness
  边界清楚但数据域窄；开放 textbook/web reasoning 丰富却无法廉价验证。随着强 policy 很快把有限题库推到
  全对/全错，group reward 失去方差，数据“存在”却不再提供有效 learning signal。
- **Mechanism / data flow:** GPT-5 从 source text 选择关键连续 reasoning span，mask 后把原 span 作为唯一
  answer，再生成风格相近的 distractors；RL 只校验 option id。9-choice 把更多样本推入同组既有成功也有
  失败的中难度区；noisy FineWeb 先抽取 educational passage，再按 16 rollouts 过滤过易题。由此将
  `unverifiable source semantics` 转成 `verifiable constructed discrimination task`，而非验证原任务答案。
- **Contract / evidence:** GooseReason-0.7M 覆盖 AoPS、rStar-Coder、MegaScience；Qwen3-4B-Instruct 与
  ProRL variant 继续训练，作者报告在 15 benchmarks 上优于只重复 ProRL data；saturated 1.5B 对比用了
  约 1,100 H100 GPU-hours。Cyber 分支从 FineWeb 构建 180K MCQ、训练 100 RL steps，在三个列明
  benchmark 上平均提升 4.44 points。数字不外推到开放式 correctness 或其他 policy/recipe。
- **Boundary / trade-off / failure:** option selection 可能学习 elimination、surface continuity 或 synthesizer
  bias；source 本身错误时，“原 span”仍只是 reconstruction label。9 个 distractors提高难度也增加 generation
  cost；GPT-5 synthesis、许可/provenance、decontamination 与 domain harm control 是新的数据供应链状态。
  formal environments 与 executable verifiers 在需要真实语义/side-effect correctness 时仍不可替代。
- **Evolution / ROADMAP / decision:** `Direct Evolution`：有限人工可验证题 → procedural environments →
  将开放文本重构为局部可验证任务 → policy-relative difficulty filtering。主 owner Ch23 Data，邻接 Ch29
  GRPO、Ch62 Evaluation、Ch68 Security；`Final Books disposition recorded in Candidate Scoring ledger`。

### Quartet II

- **Source / coverage / revision:** arXiv:2601.22813，v1 2026-01-30、v2 2026-06-01；本轮阅读全文及
  theory、computation graph、LLM/Nanochat experiments、kernel design、speed appendix 与 limitations，W05
  只记录 v1 event，v2 用于核验后续完整证据。
- **Problem / previous design:** BF16/FP8 training 保持数值余量；NVFP4 提供 Blackwell tensor-core throughput，
  但 backward 的 persistent quantization bias 会长期改变 descent direction。element-wise stochastic
  rounding 保证 unbiased，却浪费 NVFP4 representation capacity、误差更高。
- **Mechanism / state/data flow:** forward 对 weight/activation 用 native 1×16 FP8 scale、per-tensor FP32
  range 与 deterministic `4/6` local scale selection；backward 对保存的量化 W/X 反量化、转置，再通过
  random Hadamard rotation 与 MS-EDEN rescaling 重量化，使 input-gradient/weight-gradient GEMM 的估计
  保持 unbiased。rotation、scale correction 与 re-quantization 都是训练计算图的一等状态，不能藏在
  “FP4 开关”后面。
- **Contract / evidence:** end-to-end 最高 1.9B parameters、38B tokens；Nanochat 与较小 ablations 对照 BF16、
  NVIDIA recipe、FourOverSix、TetraJet-v2，并包含三次 restart 的波动。作者 CUDA kernels 在 RTX 5090
  和 B200 逐层测试：小 B200 shapes 被量化 overhead 主导，较大 shapes 才出现 speedup；1B real training
  throughput 报告约 1.8×，不是任意 4.2× end-to-end 保证。
- **Boundary / trade-off:** 当前只验证 NVIDIA Blackwell 的 NVFP4 LLM pretraining；rotation group 与
  microscale group 受内维硬件约束，re-quantization/fixup 会吞噬小矩阵收益。Gaussian MSE 和 unbiased
  guarantee 不直接保证所有 architecture/optimizer 的终局质量；authors 也要求新的 rotation granularity
  tuning。BF16/FP8 在小模型、旧硬件、debuggability 或 accuracy-first 仍合理。
- **Evolution / ROADMAP / decision:** `Direct Evolution`：BF16/FP8 → FP4 stochastic rounding →
  rotation+debiasing → forward/backward 分工的 hardware-aware computation graph。主 owner Ch24，邻接
  Ch32/36/45；`Final Books disposition recorded in Candidate Scoring ledger`。

### THINKSAFE

- **Source / coverage / revision:** arXiv:2601.23143，v1 2026-01-30、v4 2026-05-13；已读 problem/theory、
  refusal steering、safe filtering、static SFT approximation、Qwen3/DeepSeek-R1-Distill experiments、baseline/
  ablations、guard variants、online GRPO comparison 与完整 limitations。
- **Problem / previous design:** external safety teacher 可生成拒答数据，但 student/teacher distribution mismatch
  会扰动 reasoning；直接拒答又易过拒。论文假设 reasoning post-training 压制而未删除 student 原有 latent
  safety knowledge，因此旧的 external distillation 并非错误，只是在该约束下不是最小 KL target。
- **Mechanism:** 对 harmful prompts 用 lightweight refusal steering 提高 student 自己产生 safe reasoning 的
  acceptance rate，由 safety guard 过滤；benign prompts 保留 helpful response。理论把安全重对齐写成对
  student safe-conditioned distribution 的 KL projection；实践没有在线投影，而是把过滤后的 harmful/benign
  pairs 合并为 static dataset，用 LoRA fine-tune，并可加 KL regularization。
- **Contract / evidence:** Qwen3 0.6B～8B 与 DeepSeek-R1-Distill 1.5B～8B；安全看 HarmBench、StrongReject、
  WildJailbreak，over-refusal 看 XSTest，reasoning 看 GSM8K/MATH500/AIME24/GPQA。每个 reasoning prompt
  8 samples，安全主要单样本并由 Llama-Guard-3/WildGuard 判分。作者结果支持列明 family 的 safety-reasoning
  trade-off，不证明 guard correctness 或真实 agent safety。
- **Boundary / failure:** 依赖先前 safety alignment、外部 guard taxonomy 与 refusal direction；static dataset
  会随更新变 off-policy。只做 LoRA、single-turn、有限规模；self-generated unsafe blind spot 可能被同一
  model/guard共同漏掉。base model、multi-turn tools、高后果 action 仍需要外部 policy/verifier/containment。
- **Evolution / ROADMAP / decision:** `Direct Evolution`：external teacher refusal → student self-sampling →
  steering提高 safe-sample coverage → guard-filtered self-distillation。主 owner Ch27，邻接 Ch30/62/68；
  `Final Books disposition recorded in Candidate Scoring ledger`，不把“self-generated”写成 self-verifying。

### Real-Time Aligned Reward Model

- **Source / coverage / revision:** arXiv:2601.22664，v1 2026-01-30、v4 2026-05-16；已读 motivation
  experiments、theory、architecture、GREBT objective、dialogue/TL;DR results、ablation、cost analysis 与
  implementation appendices。论文没有独立 Limitations 章节，记为 `Not Disclosed`。
- **Problem / previous design:** frozen RM 只从 prompt/response semantics 打分，接口稳定、易部署；但 policy
  在 RL 中持续漂移并学习 RM weakness，固定 decision surface 逐步失配。定期 full RM retraining 可追踪，
  却昂贵且会改变通用 representation。
- **Mechanism / ownership:** rollout 同时导出 policy last-layer hidden states；RM 用 sequence-to-token cross
  attention 将 policy feedback 与自己的 reward-token embedding 融合，并随 timestep 增大反馈权重。每个
  policy update 后，只更新 cross-attention 与 scoring head，冻结 RM backbone；Bradley-Terry preference loss
  加 group reward entropy sharpening 形成 GREBT。因而 policy representation、RM head version 与 trajectory
  必须共同 version，不能把 reward 当无状态 scalar service。
- **Contract / boundary:** Qwen2.5-3B、Llama3-8B dialogue 与 Pythia-2.8B TL;DR，比较 RLOO/GRPO/
  REINFORCE++/ReMax、pretrained/iterative-head variants；AlpacaEval 2、MT-Bench、TL;DR win rate 与
  UltraFeedback RM accuracy均由作者设置支持。performance 与 cost 图没有形成跨硬件/并发/SLO contract；
  reward entropy sharpening 也可能放大错误偏好。无独立 replication、长期 drift 或 failure recovery。
- **Trade-off / evolution:** `Direct Evolution`：frozen semantic RM → periodic RM retrain → policy-state-conditioned
  RM head。它降低 full update 成本，却引入跨模型 hidden-space compatibility、feedback storage、privacy、
  version skew 与 co-adaptation/reward collusion。主 owner Ch27，邻接 Ch28/29/62；`Experimental / Final Books disposition recorded in Candidate Scoring ledger`。

### Learning What to Predict / V-pretraining

- **Source / coverage / revision:** arXiv:2601.22108，v1 2026-01-29、v2 2026-06-11；HTML 不可用，已读
  32 页 PDF 的完整 framework/proof、language/vision experiments、compute controls、decontamination、
  ablations、multitask、overhead、limitations 与 implementation appendices。
- **Problem / previous design:** continued pretraining 固定 next-token/SSL task，再靠下游 checkpoint 评测事后
  调 data/objective，保持 unsupervised learner contract 但反馈粗。直接 SFT/RL 可对准任务，却改变训练阶段
  与 general representation。目标是让少量 verifiable examples 决定“哪个自监督 update 值得做”，而不把
  labels 直接作为 learner gradient。
- **Mechanism / invariant:** designer 为 unlabeled batch 构造 top-K soft token targets（vision 则构造 view/
  mask）；feedback batch 产生 detached `g_down`，candidate self-supervised update 产生 `g_pre`，designer
  最大化局部 alignment `g_down^T g_pre`。重算并 detach targets 后，learner 只接收原 pretraining loss；
  反馈 examples 永不进入 learner batch。这是 indirect supervision，不是“无监督”。
- **Contract / evidence:** language 用 Qwen1.5 多尺度与 Qwen2.5-0.5B、NuminaMath/OpenMathReasoning、
  1,024 GSM8K feedback；vision 用 DINOv3/I-JEPA、ImageNet、ADE20K/NYUv2。主比较 wall-clock matched；
  0.5B 的 +7.4 GSM8K points 是 single run，larger Qwen1.5 报 mean/std。decontamination 后 4B margin 从
  2.5 缩到 0.8 points；0.5B MMLU 从 38.08 降到 35.01，证明存在 narrow steering。
- **Boundary / failure:** theorem 仅是 smoothness/小步下的一步 lower bound，不保证长期 trajectory；实际
  AdamW update 只用 unpreconditioned alignment surrogate，且常只算最后若干层。feedback quality/drift、
  domain-gradient conflict、meta compute 与 small-model overspecialization 都是新成本。fixed pretraining 在
  general-purpose/无可信 verifier 或 feedback representativeness 不足时仍更稳。
- **Evolution / ROADMAP / decision:** `Direct Evolution`：固定 self-supervised task → checkpoint-level data
  retuning → step-level downstream-guided task construction → domain-matched multi-objective feedback。主 owner
  Ch24，邻接 Ch23/25/62；`Final Books disposition recorded in Candidate Scoring ledger`。

### ASTRA

- **Source / coverage / revision:** arXiv:2601.21558，v1 2026-01-29；已读 tool-chain synthesis、MCP server
  construction、QA decomposition、SFT/RL recipe、infrastructure、main evaluation、irrelevant-tool ablation 与
  conclusion。公开材料未给出 production fault-recovery 或真实用户交互实验。
- **Problem / previous design:** 单轮 function calling 与静态 API benchmark 易复算，却不能训练多步依赖、
  stateful side effects 和失败恢复；直接连接真实 MCP server 更接近部署，但覆盖窄、成本高且状态难复位。
- **Mechanism / state flow:** 从 1,585 个 MCP servers、19,036 个 tools 建 tool-dependency graph，经 random walk
  生成 tool chain；真实 server 与仅文档 server 并存，后者由 stateful emulator 执行并注入 20% failure。
  QA 被拆成独立、可执行或 rule-verifiable environment；SFT 学轨迹，online multi-turn RL 再对 environment
  outcome 优化。每个 instance 在隔离环境中持有自己的 tool state。
- **Contract / evidence:** 14B/32B models 在 BFCL、Tau2-Bench、ACE 上评测；Tau2 每题四次运行并用 GPT-5.1
  user simulator，inference 由 vLLM 执行。结果支持论文所列 agentic tool-use benchmark 上的提升及 irrelevant-
  tool robustness；不证明真实 MCP 生态的 semantic fidelity、权限安全或长时 fault recovery。
- **Boundary / trade-off:** synthetic rule contract 只能验证生成器定义的任务，不等于验证现实意图；SFT
  trajectory 的质量检查含 LLM judge。emulator 扩展覆盖却引入 environment-model bias；论文也把 interactive
  user agents 列为未来工作。真实 server 在高副作用、高合规任务仍不可由 emulator 取代。
- **Evolution / ROADMAP / decision:** `Direct Evolution`：静态 function-call labels → dependency-aware tool
  chain → stateful executable environment → multi-turn RL。主 owner Ch76，邻接 Ch27/29/62/77/80；
  `Final Books disposition recorded in Candidate Scoring ledger`。

### MemOCR

- **Source / coverage / revision:** arXiv:2601.21468，v1 2026-01-29；已读 representation、deterministic
  rendering、budget-aware GRPO、三类 training tasks、cross-dataset/length/budget evaluation、ablation、case
  study 与 limitations。
- **Problem / previous design:** text summary 可检索、可 diff、可访问，但固定 token budget 下要么截断证据，
  要么用生成式压缩不可逆地丢细节。视觉 memory 可利用二维密度，却把文字正确性转移给 renderer、OCR/VLM
  与 visual-token allocation。
- **Mechanism / state flow:** drafter 先输出 rich-text memory，格式本身编码视觉优先级；deterministic renderer
  生成 image，reader VLM 在给定 visual-token budget 下回答。GRPO 分别训练标准 QA、强下采样 memory 与
  detail-augmented QA，三个 reader advantage 聚合后更新 drafter，因而 memory layout 是可学习状态而非展示层。
- **Contract / evidence:** 约 30K HotpotQA training examples，测试 HotpotQA、2Wiki、NQ、TriviaQA 的
  10K/30K/100K context；Qwen2.5-VL-7B，visual budgets 16/64/256/1024 tokens，报告三次运行。结果只支持
  这些 QA contract 下的 accuracy–budget frontier；visual token 与 text token 的语义容量不可直接等价。
- **Boundary / trade-off:** blur/OCR error 会不可逆损坏细节；layout 可能 task-specific，rendering 与 VLM 增加
  latency。图片难以做 provenance、局部更新、审计和 accessibility；需要精确引用、合规删除或结构化状态时，
  text/typed memory 仍更合理。
- **Evolution / ROADMAP / decision:** `Principle Reuse`：verbatim history → text summarization → learned visual
  compression → budget-conditioned heterogeneous memory。主 owner Ch73，邻接 Ch49/62/77；`Experimental / Final Books disposition recorded in Candidate Scoring ledger`。

### Deep Search with Hierarchical Meta-Cognitive Monitoring

- **Source / coverage / revision:** arXiv:2601.23188，v1 2026-01-30；已读 fast/slow monitor、entropy calibration、
  memory construction、implementation、四 benchmark evaluation、ablation 与 conclusion；论文无独立
  Limitations/Threats 章节，记为 `Not Disclosed`。
- **Problem / previous design:** ReAct 的单一路径便宜且可解释，但 search error 与 reasoning drift 往往到终局
  才暴露；每一步都调用强 critic 可早停，却增加 latency、费用和 critic dependence。
- **Mechanism / state flow:** fast monitor 以 top-5 retrieved documents 的 embedding cluster entropy 估计
  searching entropy，并从 top-K token distribution 估计 reasoning entropy；在成功轨迹上拟合线性关系
  `RE=a*SE+b`，残差超过 `2 sigma` 触发 slow monitor。slow monitor 检索成功/失败 session memory，由 critical
  model 总结局部行为并回写、去重经验。
- **Contract / evidence:** Qwen3-A30B-A3B critical model、Qwen-Embedding-8B、FAISS；SGLang/A6000 与
  Google/Jina APIs，memory 由 GPT-5.2 构造。在 BrowseComp-Plus/ZH、xbench、GAIA 和三种 open-source
  backbones 上的作者实验支持该触发机制；proprietary-system numbers 来自既有 benchmark，不是同一 harness。
- **Boundary / trade-off:** token entropy 不是 epistemic confidence，embedding-cluster entropy 也不是 factual
  consistency；线性阈值依赖 calibration distribution。slow monitor 引入 memory poisoning、judge bias、隐私与
  version drift；没有公开长期在线更新、回滚或跨域 threshold 稳定性。
- **Evolution / ROADMAP / decision:** `Direct Evolution`：终局 outcome check → 每步强 critic → cheap uncertainty
  gate + selective slow reflection → experience memory。主 owner Ch77，邻接 Ch62/64/73/76；`Experimental / Final Books disposition recorded in Candidate Scoring ledger`。

### KAPSO

- **Source / coverage / revision:** arXiv:2601.21526，v1 2026-01-29；已读 API/agent loop、repository state、
  evaluator contract、knowledge/episodic memory、execution isolation、parallelism、MLE-Bench/ALE evaluation
  与 conclusion。论文无独立 Limitations 章节，记为 `Not Disclosed`。
- **Problem / previous design:** 单次 coding agent 容易部署，却把假设、实验、指标与失败历史留在聊天上下文；
  全自动黑盒 AutoML 可系统搜索，但难表达开放式 repository change 与研究知识累积。
- **Mechanism / ownership:** `evolve/deploy/learn/research` 接收自然语言目标、预算和 evaluator。每次实验在独立
  Git branch 修改 executable repository，evaluator 生成 measurement record 与 scalar utility/preference，agent
  决定 retry/pivot/complete。seed repository、typed knowledge graph 与 episodic memory 分别持有代码、稳定知识
  和轨迹；branch/history 是 provenance 与 rollback 边界。
- **Contract / evidence:** knowledge backend 使用 MediaWiki/Neo4j/Weaviate，作者收集约 2,000 repositories；
  MLE-Bench 报告 Leeroo 50.67、R&D Agent 35.11，ALE 最终 ELO 1909.4、6.1 percentile、成本约 914.8 美元。
  这些是作者 harness、预算和 score-selection 条件，不证明通用 scientific discovery productivity。
- **Boundary / trade-off:** 默认 local subprocess，只有 evaluator 要求时才 containerize；这不足以隔离不可信
  code。按 public score 选择再做 private evaluation 仍有 evaluator overfitting 压力；未公开 distributed fault
  tolerance、branch conflict、knowledge supersession 或 remote executor 实现。
- **Evolution / ROADMAP / decision:** `Direct Evolution`：chat-history coding → repository-as-state → evaluator-
  bounded experiment loop → provenance-bearing organizational memory。主 owner Ch77，邻接 Ch62/73/80；
  `Final Books disposition recorded in Candidate Scoring ledger`。

### PaperBanana

- **Source / coverage / revision:** arXiv:2601.23265，v1 2026-01-30；arXiv metadata、论文全文渲染、官方项目页
  与作者仓库已交叉核验。已读 motivation/related work、五 Agent architecture、benchmark construction、evaluation
  protocol、main results、ablation、statistical-plot extension、limitations、failure cases、human-evaluation、
  implementation 与 prompt appendices。arXiv PDF 为约 42.6 MB，超出单次 reader 大小限制；全文阅读由同一
  论文的公开渲染恢复，不以产品网站或社区复刻替代论文。
- **Problem / previous design:** TikZ/Matplotlib 等 code-based illustration 可编辑、数值精确，却难自动生成现代
  methodology diagram 的复杂布局与视觉语言；one-shot image generation 表达力更强，却容易遗漏方法关系、
  生成错误连线或不可读文字。人工绘图仍最可控，但成为自动化 research workflow 的最后一段高成本 handoff。
- **Mechanism / state flow:** 输入由 source context `S` 与 communicative intent `C` 组成。Retriever 从固定
  reference set 选取结构/风格示例；Planner 将原文、caption 与 examples 转为 initial description；Stylist 从
  references 归纳 aesthetic guideline 并产生 optimized description；Visualizer 渲染 image，Critic 对照原始
  source 生成修订描述，默认循环三轮。统计图分支不直接让 image model 编造数值，而由 Visualizer 生成并执行
  Matplotlib code。reference、description、render 与 critique 是显式中间 artifact，但论文未定义 durable replay、
  idempotency、approval 或跨进程 recovery，因此它是 agentic pipeline evidence，不是完整生产 Workflow engine。
- **Implementation / evaluation contract:** PaperBananaBench 从 NeurIPS 2025 的 2,000 篇抽样论文开始，经
  MinerU parsing、aspect-ratio/filtering、categorization 与人工清洗得到 584 项，随机拆为 292 test + 292
  reference；平均 source context/caption 长度约 3,020.1/70.4 words。默认 VLM 为 Gemini-3-Pro，image model
  比较 Nano-Banana-Pro 与 GPT-Image-1.5，temperature 1，并对齐 human reference 的近似 aspect ratio。评估由
  Gemini-3-Pro 进行 referenced comparison，维度为 faithfulness、conciseness、readability 与 aesthetics；50 项
  子集另做 cross-model/human alignment，主结果还以 3 位评审做 blind A/B。论文没有公开 hardware、并发、
  生成时延、费用或 production SLO；用于论文展示的图从多次生成中人工选优，不能当成 single-run reliability。
- **What the evidence proves / does not prove:** 在该 benchmark、model 与 judge contract 下，完整 pipeline 的
  overall score 为 60.2，vanilla Nano-Banana-Pro 为 43.2。更重要的机制证据来自 ablation：random retriever 与
  semantic retriever 接近，说明一般结构/风格 pattern 比精确 topic match 更关键；Stylist 提高 conciseness/
  aesthetics 却降低 faithfulness，Critic 与多轮 refinement 能部分补回。它不证明“publication-ready”已由编辑、
  审稿或跨学科专家验证，也不证明五个逻辑角色必须由五个独立模型/进程实现。
- **Limitations / trade-off / failure modes:** 论文明确承认 raster output 难以局部编辑，4K 只缓解缩放而不提供
  vector semantics；主要失败是 redundant edge 与 source-target mismatch，Critic 也常因 foundation-model
  perception limitation 漏检。VLM judge 与人类的 Kendall tau 为中等相关而非 ground truth；reference set 只来自
  NeurIPS 2025，generate-and-select 又把候选数、人工选择成本和失败率留在 aggregate score 之外。图像分支的
  visual expressiveness 与 code 分支的 numerical fidelity 因此是共存分支，不是新方案单向替代旧方案。
- **Evolution / ROADMAP / decision:** `Layering / Dependency`：manual/code-first figure → one-shot generative
  image → reference-conditioned linear planning → Visualizer–Critic iterative refinement → executable/vector
  representation + independent structural verifier。主 owner Ch77，邻接 Ch62/76/78；`Worth Watching / Final Books disposition recorded in Candidate Scoring ledger`。

### Statistical Estimation of Adversarial Risk under Best-of-N / SABER

- **Source / coverage / revision:** arXiv:2601.22636，v1 2026-01-30；已读 threat model、Beta-Binomial MLE、
  large-N theorem/small-N correction、anchored/plugin estimators、confidence interval、experiment、goodness-of-fit、
  error bounds、unbreakable/benign extensions 与完整 limitations。代码在论文事件时仅承诺未来发布。
- **Problem / previous design:** ASR@1/小预算评测成本低，适合模型迭代，却忽略攻击者可并行重复采样；直接测
  ASR@1000 更符合 operational threat model，但成本高，也无法从单点观察 scaling profile。
- **Mechanism / assumptions:** 对固定 attacker–victim–judge triplet，每个 harmful query 的 sample success
  probability 服从 Beta distribution，attempt 条件独立 Bernoulli；以 Beta-Binomial MLE 估计参数，推导
  `ASR@N ≈ 1 - C*N^(-alpha)`。anchored estimator 用已测 ASR@n 消去 leading constant，并由 delta method
  给 uncertainty。参数属于当前 query distribution 与 pipeline，不是模型常数。
- **Contract / evidence:** HarmBench 159 queries；Text Augmentation、ADV-LLM、Jailbreak-R1；victims 为
  GPT-4.1-mini 与 Llama-3.1-8B-Instruct；judges 为 HarmBench Classifier 和 LLM Classifier。用每 query
  `n=100` 外推 ASR@1000 时，作者五次运行报告 anchored estimator MAE 1.66、naive 12.04；该数字不外推
  到其他 benchmark、adaptive attack 或 stateful defense。
- **Boundary / trade-off:** i.i.d. 假设忽略 rate limiting、adaptive attacker、session state 与 correlated judge；
  部分 triplet 的 Beta goodness-of-fit 失败或 marginal。binary judge 隐去 severity，且剩余 error 倾向低估；
  论文只覆盖 textual HarmBench，未测 frontier victims。SABER 节省测量预算，却不能替代真实高预算 red team。
- **Evolution / ROADMAP / decision:** `Direct Evolution`：single-shot ASR → brute-force Best-of-N → small-budget
  distribution fit → budget-aware risk curve / Budget@tau。主 owner Ch68，邻接 Ch62/66/69；`Final Books disposition recorded in Candidate Scoring ledger`。

### TAM-Eval

- **Source / coverage / revision:** arXiv:2601.18241，v1 2026-01-26；已读 benchmark positioning、three-stage
  curation、create/repair/update construction、metrics、Docker infrastructure、attempt feedback、six-model
  evaluation 与 failure analysis。论文没有独立 Limitations/Threats 章节，记为 `Not Disclosed`。
- **Problem / previous design:** 单函数 test generation 和 exact-match benchmark 易比较，却不覆盖已有 suite
  的 repair/update；只看 pass rate 又会奖励执行成功但无断言、无 mutation sensitivity 的“空测试”。
- **Mechanism / verifier contract:** 1,539 validated scenarios 来自活跃 Python/Java/Go repositories；模型重写
  整个 test file，最多三次 attempt，后续输入 compiler/runtime feedback。sandboxed Docker 执行后联合记录
  pass rate、line-coverage delta 与 fixed-mutant mutation-coverage delta。repair defects 含 syntax、execution、
  coverage 和 assertion-efficiency；update 用旧 test file 对当前 focal file 构造版本差异。
- **Contract / evidence:** 六种模型经 OpenRouter、temperature 0.25、固定 seed；默认只给 focal/test file，框架
  可扩到 repository context。作者结果中最佳模型 Attempt@3 pass rate 42.37%，但 model API/version 与 prompt
  是评测状态；超过 60% invalid output 为 execution error。From Scratch 的 coverage gain 因 baseline 为零而天然
  偏大，不能与增量维护直接比较。
- **Boundary / trade-off:** synthetic repair injection 与 k-commit rollback 不完全代表真实 issue intent；coverage
  和 mutation killing 仍不能证明业务语义、oracle correctness 或 flaky-test safety。reference-free verifier 可扩展，
  但 toolchain、container、dependency availability 与 mutant generator 都会改变分数；三语言不是 language-agnostic
  已验证。
- **Evolution / ROADMAP / decision:** `Direct Evolution`：text similarity → compile/pass → coverage → mutation
  strength → iterative maintenance workflow。主 owner Ch62，邻接 Ch66/77/80；`Final Books disposition recorded in Candidate Scoring ledger`。

### Continual GUI Agents / GUI-AiF

- **Source / coverage / revision:** arXiv:2601.20732，v1 2026-01-28、当前 HTML v4 2026-03-25；已读 continual
  task formalization、APR-iF/ARR-iF rewards、RFT objective、training sequence、baselines、main/ablation、reversed
  order、text/icon bias、visualization 与 limitations。
- **Problem / previous design:** joint/static GUI grounding 在固定 distribution 上稳定；环境按 mobile→desktop→web
  或 normal→high-resolution 到来时，继续优化当前坐标/尺度会 over-adapt 并遗忘旧布局。完全 replay/joint
  training 可缓解，但需要保留历史数据且不符合顺序到达约束。
- **Mechanism:** APR-iF 奖励同一 instruction 多个 sampled bounding-box center 的 spatial exploration，ARR-iF
  奖励 region-scale diversity；它们与 ground-truth correctness advantage 一起进入 GRPO-like RFT，并加 reference-
  policy KL。state ownership 仍在 policy checkpoint 与顺序 dataset；该方法没有维护显式 GUI world model。
- **Contract / evidence:** Qwen2.5-VL-3B；Widget Captioning→ShowUI-web 的 domain sequence，ShowUI-web 1080p
  → OmniACT 最高 4K 的 resolution sequence；ScreenSpot V1/V2/Pro，对比 SeeClick、GUI-Actor、InfiGUI-R1、
  SE-GUI、GUI-G2。结果支持这两类受控 shift 下的 grounding retention，且 ablation 显示 current-task reward 与
  generalization reward 存在冲突。
- **Boundary / trade-off:** diversity reward 可能鼓励无意义 exploration，仍依赖准确 bounding-box labels；只测
  3B、三训练集、三 benchmark、domain/resolution 两类 shift。真实 app update、dark mode、localization、action
  side effect 与 multi-step recovery未验证；point grounding accuracy 也不是完整 task completion。
- **Evolution / ROADMAP / decision:** `Direct Evolution`：static grounding SFT → current-task RFT → replay/joint
  adaptation → flux-aware exploration reward。主 owner Ch76，邻接 Ch29/62/77；`Experimental / Final Books disposition recorded in Candidate Scoring ledger`。

### RAPTOR / Ridge-Adaptive Logistic Probes

- **Source / coverage / revision:** arXiv:2602.00158，v1 2026-01-29（编号跨月但 first-public 属 W05）；已读
  probe/steer setup、ridge selection、fold-back、GCAV strength、accuracy/stability/cost experiments、Gaussian
  teacher-student theory、steering appendix、separability diagnostics 与 discussion。无独立 Limitations 章节。
- **Problem / previous design:** unregularized/simple probe 成本低，但高维小样本下 concept direction 对数据删减
  不稳定；复杂 probe 可提高拟合，却更昂贵，且高 classification accuracy 不保证 direction 可复用。
- **Mechanism:** 每层只用 train statistics 标准化 hidden embedding，以 validation 选择 L2 ridge logistic
  regression，再把 weight fold 回原 activation coordinates 并 normalize 为 concept vector。GCAV 从 probe logit
  闭式选择最小 additive intervention strength；低于 reliability threshold 的 layer 可跳过。
- **Contract / evidence:** Qwen2.5、Llama3.1/3.3、Gemma instruction models，六个人工 binary concept datasets，
  与 GCS/xRFM 比 accuracy、drop-and-resplit cosine stability 和同硬件 wall-clock。Gaussian proportional-limit
  theory只解释 ridge 的定性趋势；real embeddings 不是该分布。steering 主要报告同一 probe coordinate 的 target
  success，且 intervention strength 有明显 long tail。
- **Boundary / trade-off:** linear decodability 不证明 causal representation；用 probe 定义方向、选强度并判断
  target 容易形成闭环自洽，不等于输出语义、安全或任务行为被控制。per-layer sweep 随模型深度增长，极端
  strength 可能破坏其他能力；跨 prompt/domain/model 的 causal validation 未完成。
- **Evolution / ROADMAP / decision:** `Principle Reuse`：linear probe → regularized/stability-aware direction →
  probe-conditioned activation steering → independent behavioral verifier。主 owner Ch5，邻接 Ch62/68；`Worth
  Watching / Final Books disposition recorded in Candidate Scoring ledger`。

### Sweet Spot Learning

- **Source / coverage / revision:** arXiv:2601.22491，v1 2026-01-30；已读 problem formulation、reward equations、
  task-specific proximity、ordering/SNR analysis、12-benchmark setup、main results、sample-efficiency、cross-task
  transfer、zone-granularity ablation、training/evaluation appendix 与 learned PRM/ORM discussion。直接 PDF 为约
  12.9 MB，超出单次 reader 大小限制；正文由 arXiv experimental HTML 与同一 primary PDF 的可检索文本恢复。
  论文未提供独立公开 code repository，也未披露训练 hardware。
- **Problem / previous design:** binary RLVR reward 便宜、objective 清楚，且不会要求额外 reward model；但同为
  success 或 failure 的 trajectories 完全同分，near-success 与低质量路径无法提供方向。连续 shaping 能恢复细粒度
  差异，却会把微小 measurement noise 和任意 scale 直接放大进 gradient。SSL 保留 terminal verifier，同时用
  离散 quality zones 提供中间方向。
- **Mechanism / ownership:** 对 trajectory `tau` 的每一步计算 task-specific proximity `h(s_t,a_t)`，聚合为
  `S(tau)`，再映射到有序 sweet-spot zone 得 `S_hat(tau)`；最终 reward 为
  `R_SSL(tau)=C(tau)+alpha*S_hat(tau)`。论文实验取 `alpha=0.2`，以 EasyR1 的 GRPO 更新 policy。GUI grounding
  用目标区域内的 spatial/distance proximity，Sudoku、maze 与 ARC 则用 task structure 的 partial progress。
  因而 reward state 的真正 owner 不是 policy，而是 ground-truth/environment-specific proximity function、zone
  boundaries、terminal verifier 与 trajectory aggregator 的共同版本。
- **Theory / implementation contract:** 作者分析在 proximity 与有用 policy gradient 对齐等条件下，tiered
  shaping 保留最优解 ordering 并提高 gradient signal-to-noise ratio；这是一组带前提的性质，不是任意 proxy 的
  保证。SFT 使用 Qwen2.5-VL-3B/7B 与 LLaMAFactory 训练一轮；RL 使用 EasyR1 超过三轮。GUI training 主要为
  Mix-3K，另抽取约 2K perception samples；统一零样本 inference prompt。评估覆盖 short/long-term GUI planning、
  fine-grained perception、Sudoku、maze、ARC-AGI-1/2 共 12 个 benchmark，并分别报告 action type、grounding、
  step success 或 accuracy。
- **What the evidence proves / does not prove:** 作者实验支持在这些空间/结构 proximity 可直接计算的任务上，
  tiered reward 相对 binary/continuous baselines 改善学习。所谓 `2.5x sample efficiency` 的严格边界是 SSL-3B
  使用 40% GUI training data 时达到或超过 RL-Binary-3B 使用全部数据的作者曲线，不等价于 wall-clock、token、
  GPU-hour 或任意任务的 2.5 倍。perception-to-planning transfer 的平均值改善，但 7B 在 GUI-Odyssey 某个 grounding
  metric 仍出现轻微回退，因此也不是逐 metric 单调增益。
- **Ablation / limitations / trade-off:** `K={2,4,8}` 中，作者 planning aggregate 以 `K=4` 最好，说明分区过粗
  丢信号、过细重新暴露 noise；zone 与 `alpha` 都是 task contract。论文没有与 GUI-domain PRM/ORM 直接比较，
  作者理由是缺少 step-level annotation、存在 multimodal domain mismatch 且无开源 baseline。代价是 proximity
  依赖 ground truth 或可手工编码的 task geometry；开放式 research、工具副作用、语义质量和稀疏现实反馈未必有
  可信“距离”。错误 proxy 会产生 reward hacking，local block progress 也可能与 global correctness 冲突。
- **Evolution / ROADMAP / decision:** `Direct Evolution`：terminal binary verifier → continuous reward shaping →
  discretized proximity zones + terminal gate → learned/hybrid process reward。旧的 binary verifier 在没有可靠
  proximity、风险要求 hard pass/fail 或 reward measurement 易被攻击时仍然成立。主 owner Ch29，邻接
  Ch28/62/76/77；`Must Read / Final Books disposition recorded in Candidate Scoring ledger`。

### ReGuLaR

- **Source / coverage / revision:** arXiv:2601.23184v1，2026-01-30；已读 variational formulation、conditional-
  independence assumption、rendered-CoT prior、inference algorithm、math/multimodal experiments、compression/
  generalization、六组 ablation、scalability appendix 与 future work。论文没有独立 Limitations 章节。
- **Problem / previous design:** explicit CoT 可审计并以 token anchor 保持局部逻辑，但 autoregressive decoding
  昂贵；Coconut/CoLaR 等 latent reasoning 减少 token，却可能因无离散锚点而 semantic drift。单纯缩短 CoT 与
  压缩 latent state 解决的不是同一个成本边界。
- **Mechanism / state flow:** 将每段训练 CoT 渲染为 image，经 frozen DeepSeek-OCR visual encoder 与 trainable
  adapter 得到 Gaussian prior mean；latent head 从 question 与历史 latent states 产生 posterior，ELBO 用 answer/
  reasoning reconstruction 加 KL 将 posterior 拉向 visual prior。render/visual state 只在训练期提供 guidance；推理
  时 latent state 递归采样，并由代表 token 判断 reasoning termination。
- **Contract / evidence:** 主要 backbone 为 frozen Llama-3.2-1B-Instruct + LoRA，也测 DeepSeek-R1-Distill-
  Qwen-1.5B；GSM8K-Aug/Aug-NL、GSM-Hard、SVAMP、MultiArith、AQUA-RAT、MATH，对比 iCoT/CODI/Coconut/
  CoLaR。8×A100 training，top-p 0.9、temperature 1.0 inference。结果支持这些小模型数学任务的 accuracy–latent-
  step frontier，不证明 wall-clock/token-throughput 或大模型复杂推理收益。
- **Boundary / trade-off:** 论文称 rendering lossless，但 visual encoder、fixed resolution、segmentation 与 latent
  bottleneck 都可能丢信息；conditional independence 与 Gaussian prior 是建模假设。训练仍需完整 CoT、OCR
  encoder 和离线视觉缓存；latent trace 难审计、难纠错。作者也承认 GSM8K reasoning 简单、理论上超越 explicit
  CoT 未证明。
- **Evolution / ROADMAP / decision:** `Direct Evolution`：explicit token CoT → recursively fed hidden state →
  learned compressed latent steps → teacher-guided variational latent state。主 owner Ch28，邻接 Ch14/22/24/45；
  `Experimental / Final Books disposition recorded in Candidate Scoring ledger`。

### TTCS / Test-Time Curriculum Synthesis

- **Source / coverage / revision:** arXiv:2601.22628，v1 2026-01-30；已读 test-time objective、co-evolving
  synthesizer/solver、capability/diversity rewards、GRPO loop、math/general-domain evaluation、scarce-data study、
  ablations、theory appendix 与 examples。无独立 Limitations/Threats 章节；hardware 未披露。
- **Problem / previous design:** self-consistency 在 test questions 上无需外部 label，却在难题上可能多数一致地
  答错；直接 test-time RL 样本又少、difficulty 固定。离线 curriculum 稳定但不能随当前 solver capability 移动。
- **Mechanism / ownership:** synthesizer 与 solver 从同一 pretrained model 初始化。synthesizer 围绕原 test
  question 生成 variants，reward 同时偏好 solver response variance 形成的 capability frontier、与原题相关性和
  group diversity；solver 对原题/合成题多次采样，以 majority self-consistency 作 pseudo-label。两 policy 轮流用
  GRPO 更新，因此 checkpoint、question family、pseudo-label 与 iteration 必须共同 version。
- **Contract / evidence:** Qwen2.5-Math-1.5B/7B、Qwen3-4B-Base；AMC23、AIME24/25、MATH-500、Minerva、
  OlympiadBench，另看 BBEH/MMLU-Pro/SuperGPQA。AIME 报 Mean@32、temperature 0.6，部分答案由 GPT-4o-mini
  辅助匹配；每个 benchmark 单独适配后再评测。作者结果和 ablation 支持 capability-aligned synthesis 的增益，
  不证明对未见 deployment distribution 的一般提升。
- **Boundary / trade-off:** 在 test questions 上更新本质是 transductive protocol，容易混淆 evaluation 与
  adaptation；self-consistency 不是 correctness verifier，同源 synthesizer/solver 可共振错误。在线双 policy
  更新成本高并产生 model rollback、data provenance、contamination 与 catastrophic drift 问题；真实 Agent
  action correctness 仍需外部环境验证。
- **Evolution / ROADMAP / decision:** `Direct Evolution`：static test-time scaling → pseudo-label test-time RL →
  capability-aligned synthetic curriculum → co-evolving solver/synthesizer。主 owner Ch29，邻接 Ch23/28/62/77；
  `Experimental / Final Books disposition recorded in Candidate Scoring ledger`。

### Routing the Lottery / Adaptive Tickets

- **Source / coverage / revision:** arXiv:2601.22141，v1 2026-01-29；已读 mask extraction、joint retraining、
  routing assumption、CIFAR-10/100、implicit neural representation、speech enhancement、collapse/semantic
  analyses、runtime appendix 与 conclusion。无独立 Limitations 章节。
- **Problem / previous design:** 一个 universal sparse ticket 保留单模型部署简单性，却假设所有 input subsets
  共享相同容量；每 subset 独立模型能专门化，但参数线性增长。RTL 尝试共享 dense initialization，只让 sparse
  mask 按 class/cluster/environment 分化。
- **Mechanism / state:** 先由 label 或 clustering 把 data 切成 subsets，逐 subset 迭代 magnitude pruning 得 mask，
  再固定 mask topology、balanced cyclic batches 联合训练 active weights。routing 不由 learned router 完成，而
  假设请求已有 class/environment context；mask similarity 用来诊断 subnetwork collapse。
- **Contract / evidence:** CIFAR-10/100、per-image INR 与 DNS speech environments；classification、reconstruction、
  SI-SNRi，对比 single-mask IMP 与 independent multi-model IMP。speech experiment 单 H100，RTL/多模型约 10h、
  single model 约 8h。结果支持这些小网络的 parameter-sharing specialization，不证明 Transformer/MoE routing、
  token-level conditional compute 或未知-domain dispatch。
- **Boundary / trade-off:** 预先知道 subset identity 把最难的 routing/shift detection 移出模型；unstructured
  masks 未必获得实际 kernel speedup。balanced repetition 可过采样少数 subset，recall 上升伴随 precision 下降；
  mask 数与 metadata 随环境增长。它对 AI System 只有 principle analogy，不是 LLM Infra 直接证据。
- **Evolution / ROADMAP / decision:** `Explanatory Analogy`：one dense model → universal sparse ticket → context-
  selected adaptive masks → learned conditional routing。关联 Ch21/36/45，但 `Weekly Only — No Books Change`。

### Why Attention Patterns Exist / TAPPA

- **Source / coverage / revision:** arXiv:2601.21709，v1 2026-01-29；已读 temporal framework、query/key/RoPE
  derivation、re-access/sequential/seasonal/periodic cases、perturbation ablations、KV allocation、layer pruning、
  DuoAttention/Expected Attention comparison、overhead 与 sensitivity appendices。无独立 Limitations 章节。
- **Problem / previous design:** sink/retrieval/diagonal heads 的经验 taxonomy 可直接驱动 sparse attention，却
  缺统一机制，容易把某模型上的 pattern label 固化为 universal head type。全 KV 保留最稳，但 memory 随 length
  线性增长；按历史 attention score eviction 又要维护 per-token state。
- **Mechanism:** TAPPA 以相邻时刻 query self-similarity 区分 predictable 与 unpredictable attention；query/key
  连续性加 RoPE relative rotation 导出近似 diagonal shift invariance，input periodicity 与 dominant RoPE frequency
  解释 seasonal/periodic pattern。工程上以 recent fixed window 的 q-similarity 修正 per-layer KV budget；低
  similarity layer 被视为更可能 retrieval-like，获得更多 cache。另把该 signal 加到 Block Influence 做 layer pruning。
- **Contract / evidence:** Llama-3.1-8B 与 Qwen2.5-7B、LongBench 16 subsets，KV budgets 512/1024/2048；对比
  StreamingLLM/H2O/SnapKV/PyramidKV/CAKE/DuoAttention。pruning 另含 Llama2-7B，PG19 calibration。32K 下
  q-sim overhead 的作者测量 <0.2ms/layer、8.69MB，仅属于 Llama-3.1-8B、window32 的实现条件。
- **Boundary / trade-off:** temporal continuity 是模型/层/数据相关统计，不是每个 head 的语义保证；q-similarity
  是 allocation proxy，不能证明某 KV token 不重要。per-model validation、extra query statistic 和 dynamic budget
  仍需管理；LongBench quality 不等于 production latency/SLO。理论 bounds 的平滑条件在 abrupt tool/code/
  multimodal sequence 上可能失效。
- **Evolution / ROADMAP / decision:** `Direct Evolution`：pattern taxonomy → mechanism-based predictability →
  layer-sensitive KV budget → runtime-adaptive state retention。主 owner Ch49，邻接 Ch15/22/44/45；`Final Books disposition recorded in Candidate Scoring ledger`。

### Machine Learning for Energy-Performance-aware Scheduling

- **Source / coverage / revision:** arXiv:2601.23134，v1 2026-01-30；已读 SimPy simulator、energy/latency
  equations、GP kernels、Sobol initialization、scalar/MOO objectives、fANOVA、robustness、Pareto analysis、future
  work 与 appendices。无真实 hardware experiment。
- **Problem / mechanism:** heuristic scheduler 参数在离散 core counts、frequency 与 scheduler strategy 的混合
  search space 中难手调；论文用 Gaussian-Process Bayesian Optimization，以 10 个 Sobol warm-up + 100 trials
  搜索 little/medium/big core count/frequency、FCFS/RR/Priority 和 time quantum，再用 Pareto frontier 避免把
  energy/time 永久压成单一权重。
- **Contract / evidence:** 所有结果来自 SimPy：1,000ms、500 synthetic tasks、Poisson arrival，processor
  energy/latency 由作者方程生成。Matérn/RBF、fANOVA、race-to-idle 与 core-role decoupling 因此只证明 optimizer
  能恢复 simulator 中编码的 landscape；没有 silicon power measurement、thermal throttling、DVFS transition、
  OS interference、memory/network bottleneck 或真实 workload。
- **Trade-off / decision:** BO 对昂贵黑盒评测有通用价值，Pareto contract 也长期有效，但本论文不能支撑 AI
  accelerator/scheduler 设计结论。surrogate 与 simulator 共用错误假设会产生精确但无效的 optimum；offline
  tuning 未覆盖 workload drift。评分 18/30，关联 Ch35/37/50 仅作 discovery rejection：`Reject — Weekly Only`。

## Knowledge Tree Position

- Model：`MODEL-EMBEDDING`、`MODEL-TRANSFORMER-LAYER`、`MODEL-DECODER-ONLY`、`MODEL-MOE`、
  `MODEL-LONG-CONTEXT`。
- Training：`TRAIN-DATA`、`TRAIN-PRETRAINING`、`TRAIN-RLHF`、`TRAIN-GRPO`、
  `TRAIN-DISTRIBUTED-TRAINING`。
- Inference：`INFER-KV-CACHE`。
- Platform：`PLATFORM-EVALUATION-SYSTEM`、`PLATFORM-SECURITY`。
- Agent：`AGENT-RAG`、`AGENT-MEMORY`、`AGENT-PLANNING`、`AGENT-REFLECTION`、`AGENT-WORKFLOW`、
  `AGENT-MULTI-AGENT`。

43 项均在目标章节与相邻章节阅读后获得唯一主 owner 或明确 Weekly-only/Reject disposition；跨章节只保留
handoff，不用同一论文重复拥有多个正文段落。

## Evidence Level

- 论文机制与性能均限定为作者实验结论；没有把 author benchmark 写成通用事实。
- 官方 publication node 与论文 first-public date 分开；后续 revision 不改变历史事件日期。
- 对未披露的 production SLO、fault recovery、serving concurrency、独立 replication 明确记为未证明。
- 当前 43/43 候选均有完整 Source Review 与评分；candidate Evidence Gate 已通过。Google Scholar/OpenAlex/DBLP
  等 discovery surface 尚未形成机器可复算的周级全集，所以此状态不等于 discovery census complete。

## Cross-Week Deduplication and Evolution

```text
collective FSDP
→ ODC point-to-point progress
→ 仍保留 minibatch sync；async SGD / elasticity / fault tolerance 尚未解决

BF16 training + rollout
→ FP8 rollout/KV
→ TIS 与 router-sensitive mixed precision
→ end-to-end FP8 仍受 gradient range 与 optimizer-state contract 约束

static long-context retrieval
→ dynamic environment rollout
→ typed state / provenance / stopping evidence
→ lossy memory 只能在明确可丢信息边界内使用

single outcome reward
→ per-action AI coach
→ credit assignment 更密集
→ coach bias、reward hacking 与 global policy balance 成为新控制问题
```

## Recommended Action

1. W05 的 43 项 candidate evidence 与 Books disposition 已逐项复核；下一检查点进入 W06，不把本周通过误写成年度完成。
2. 28 项已融入既有演进链，11 项以章节级证据去重，3 项仅保留 Weekly，1 项因 simulation-only evidence 拒绝。
3. discovery recall 仍需通过可复算 source ledger 与跨索引去重继续验证；目前不宣称“本周无遗漏”。

## Event-Date Daily Decision

Historical Backfill 只维护完整 ISO Weekly，不补造 2026-01-26～02-01 Daily。

## Books Integration Decision

`Source-Family Books Gate Complete / Archive Completion Gate Open`。

43 个候选均完成来源级复核、目标及相邻章节阅读与最终 disposition。Books 共 refine 17 个 owner chapters；
No Change 均绑定具体既有机制，Weekly Only/Reject 未进入长期正文。“Must Read”没有被等同为“必须写入”。

## Ignored Noise

- 只给出吞吐/准确率而未绑定 model、hardware、length、batch、precision 或 topology 的二次传播。
- 把 Hugging Face “submitted” 日期当 arXiv first-public date 的条目。
- “Post-LN 取代 Pre-LN”“FP8 等价 BF16”“soft verification 不需要 correctness”“更多 agents 必然更强”等
  越过论文条件的结论。

## Repository Changes

- 2026-08-07：W05 从 3 个评分行修复为 23 个；新增 20 个 recovered candidates 与逐项 Full Source Review。
- Second-pass Batch A 完成 Golden Goose、Quartet II、ThinkSafe、R2M 与 V-pretraining，当前账目为
  28 reviewed + 15 pending。
- Second-pass Batch B 完成 ASTRA、MemOCR、DS-MCM 与 KAPSO，当前账目为 32 reviewed + 11 pending；
  PaperBanana 当时因 reader 大小限制暂记 blocked。
- Second-pass Batch C 完成 SABER、TAM-Eval、Continual GUI Agents 与 RAPTOR，当前账目为 36 reviewed +
  7 pending；Sweet Spot Learning 当时因 reader 大小限制暂记 blocked。
- Second-pass Batch D 完成 ReGuLaR、TTCS、Routing the Lottery、TAPPA 与 energy-performance scheduling；
  后者经正文复核降为 18/30，当时账目为 41 reviewed + 2 blocked。
- 2026-08-09：通过论文全文渲染、arXiv HTML/PDF 文本与官方 artifact 补完 PaperBanana、Sweet Spot Learning；
  W05 更新为 43/43 Full Source Reviews，candidate Evidence Gate 通过，Books Integration 仍 pending。
- 2026-08-13：完成 43/43 Books disposition 与周级反向检查；28 项 Integrate/Refine 进入 17 个 owner
  chapters，11 项以具体既有论点去重，3 项 Weekly Only，1 项 Reject。
- 删除的同内容 `README 2.md` 副本属于单独已复核的清理步骤。

## Open Questions

1. W05 是否仍有未被当前 discovery index 覆盖、但在 arXiv v1 日期内达到 20/30 的候选？
2. ODC 的 minibatch-end consistency、daemon/RDMA failure 与 retry/idempotency 怎样定义？
3. FP8 rollout policy correction 如何与 MoE routing、optimizer state 和 distributed weight sync 联合验证？
4. Agent workflow memory 如何标注 lossless constraints、derived state、coverage 与 stopping evidence？
5. AI coach/process reward 如何校准跨 task-type bias，并避免把 judge preference 训练成系统 specialization？
6. PaperBanana 如何用 independent graph/connection verifier 替代同源 VLM Critic 对结构错误的漏检，并把
   generate-and-select 的候选数、延迟和人工成本纳入 operational contract？
7. SABER 的 i.i.d. scaling law 在 adaptive attacker、stateful defense、rate limiting 与 correlated judge 下如何
   重建？
8. TTCS 在不接触正式 test set、且有独立 correctness verifier 时，capability-aligned curriculum 是否仍有增益？当前仅留 Weekly。
9. Sweet Spot Learning 的 proximity、zone 与 terminal verifier 如何在开放式 Agent task 中避免 proxy gaming，
   并与 learned process reward 做同预算比较？

## Sources

- Google Research, “Towards a science of scaling agent systems,” 2026-01-28:
  https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/
- Post-LayerNorm Is Back / Keel, arXiv:2601.19895: https://arxiv.org/abs/2601.19895
- Anthropic, “How AI assistance impacts the formation of coding skills,” 2026-01-29:
  https://www.anthropic.com/research/AI-assistance-coding-skills
- DeepPlanning, arXiv:2601.18137: https://arxiv.org/abs/2601.18137
- daVinci-Dev, arXiv:2601.18418: https://arxiv.org/abs/2601.18418
- FP8-RL, arXiv:2601.18150: https://arxiv.org/abs/2601.18150
- SAGE, arXiv:2601.18202: https://arxiv.org/abs/2601.18202
- Revisiting Parameter Server in LLM Post-Training, arXiv:2601.19362:
  https://arxiv.org/abs/2601.19362
- AACR-Bench, arXiv:2601.19494: https://arxiv.org/abs/2601.19494
- TRACE, arXiv:2601.20103: https://arxiv.org/abs/2601.20103
- SPARK, arXiv:2601.20209: https://arxiv.org/abs/2601.20209
- SERA, arXiv:2601.20789: https://arxiv.org/abs/2601.20789
- Scaling Embeddings, arXiv:2601.21204: https://arxiv.org/abs/2601.21204
- ConceptMoE, arXiv:2601.21420: https://arxiv.org/abs/2601.21420
- Token-Level Capability Filtering, arXiv:2601.21571: https://arxiv.org/abs/2601.21571
- AgentLongBench, arXiv:2601.20730: https://arxiv.org/abs/2601.20730
- Self-Improving Pretraining, arXiv:2601.21343: https://arxiv.org/abs/2601.21343
- HALO / HypeNet, arXiv:2601.22156: https://arxiv.org/abs/2601.22156
- DeepSearchQA, arXiv:2601.20975: https://arxiv.org/abs/2601.20975
- ECO, arXiv:2601.22101: https://arxiv.org/abs/2601.22101
- Mechanistic Data Attribution, arXiv:2601.21996: https://arxiv.org/abs/2601.21996
- RedSage, arXiv:2601.22159: https://arxiv.org/abs/2601.22159
- Scaling Multiagent Systems with Process Rewards / MAPPA, arXiv:2601.23228:
  https://arxiv.org/abs/2601.23228
- Golden Goose, arXiv:2601.22975: https://arxiv.org/abs/2601.22975
- Quartet II, arXiv:2601.22813: https://arxiv.org/abs/2601.22813
- ThinkSafe, arXiv:2601.23143: https://arxiv.org/abs/2601.23143
- Real-Time Aligned Reward Model, arXiv:2601.22664: https://arxiv.org/abs/2601.22664
- Learning What to Predict, arXiv:2601.22108: https://arxiv.org/abs/2601.22108
- ASTRA, arXiv:2601.21558: https://arxiv.org/abs/2601.21558
- MemOCR, arXiv:2601.21468: https://arxiv.org/abs/2601.21468
- Deep Search with Hierarchical Meta-Cognitive Monitoring, arXiv:2601.23188:
  https://arxiv.org/abs/2601.23188
- KAPSO, arXiv:2601.21526: https://arxiv.org/abs/2601.21526
- PaperBanana, arXiv:2601.23265: https://arxiv.org/abs/2601.23265
- PaperBanana full-text paper rendering: https://www.researchgate.net/publication/400340137_PaperBanana_Automating_Academic_Illustration_for_AI_Scientists
- PaperBanana official project page: https://dwzhu-pku.github.io/PaperBanana/
- PaperBanana author repository: https://github.com/dwzhu-pku/PaperBanana
- Statistical Estimation of Adversarial Risk under Best-of-N / SABER, arXiv:2601.22636:
  https://arxiv.org/abs/2601.22636
- TAM-Eval, arXiv:2601.18241: https://arxiv.org/abs/2601.18241
- Continual GUI Agents, arXiv:2601.20732: https://arxiv.org/abs/2601.20732
- RAPTOR, arXiv:2602.00158: https://arxiv.org/abs/2602.00158
- Sweet Spot Learning, arXiv:2601.22491: https://arxiv.org/abs/2601.22491
- ReGuLaR, arXiv:2601.23184: https://arxiv.org/abs/2601.23184
- TTCS, arXiv:2601.22628: https://arxiv.org/abs/2601.22628
- Routing the Lottery, arXiv:2601.22141: https://arxiv.org/abs/2601.22141
- Why Attention Patterns Exist / TAPPA, arXiv:2601.21709: https://arxiv.org/abs/2601.21709
- Machine Learning for Energy-Performance-aware Scheduling, arXiv:2601.23134:
  https://arxiv.org/abs/2601.23134
