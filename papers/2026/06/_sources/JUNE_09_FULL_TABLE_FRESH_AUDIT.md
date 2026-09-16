# 2026-06-09 全候选非作者语义终审

审计日期：2026-09-11（Asia/Shanghai）

## 结论

本次从 `115 Candidate / 1,120 Close` 的已冻结分母出发，逐项重新读取候选表、对应 exact-v1 Evidence 记录、Books owner 与相邻章节正文。旧 `Candidate`、评分、source trace 和 `Books=已有覆盖` 均不作为本轮判断依据。

- Candidate 分母：**115，Pass**。未发现应再次 de-admit 的候选，也未从 Close 恢复新候选。
- Books Decision：**115 Existing Coverage / 0 Integrate / 0 Only report / 0 de-admit**。
- Owner：**101 项保持，14 项需要纠正**。纠正只改变 canonical owner 与章节锚点，不产生新的正文授权。
- Books delta：**0 个 owner-level 新机制组**。当前 `Review notes` 前正文已覆盖所有 115 项的长期机制；本轮不以论文名逐条追加。
- 旧采用链：`2606.09774` 已不在 115 项分母，当前 Books 全文检索未再发现该 family 的 body/trace；撤销完成。

这不是“115 篇论文都很重要”的判断。分母内同时包含改变系统机制的论文，以及改变 evaluation/security 证据合同的反例与 benchmark；后者只保留其揭示的测量边界，不把榜单数字或局部方法写入 Books。

## 审计方法与边界

每项依次回答四个问题：

1. 对象是否确实是 LLM、Agent 或其 Training / Inference / Platform；
2. 贡献是否改变 state、data、control、resource 或 evaluation contract，而非只有局部模型、表示、recipe 或分数；
3. canonical owner 是否由机制所有权决定，而非标题关键词；
4. 若判 Existing，`Review notes` 前是否存在可独立成立的命题级正文。

75 个 prior candidate 使用 `V2_1_EVIDENCE_ARCHIVE.md` 的 exact-v1 Method / Evaluation / Limitations 记录复核；40 个 recovered candidate 使用 `V3_EVIDENCE_RECOVERED.md`。`2606.09483` 的 arXiv 主站正文超时，Evidence 已由同属 arXiv 官方域的 `export.arxiv.org` exact-v1 PDF 恢复，定位到 §2、§2.1～2.4、§3 与独立 Limitations。`2606.07571`、`2606.07665`、`2606.09421` 只有 official exact-v1 identity/abstract 可用，因此本轮只允许 `Existing Coverage`，不允许用它们授权新正文或性能结论。

## Owner correction — 14

| ID | 旧 owner | canonical owner | `Review notes` 前命题锚点与边界 |
| --- | --- | --- | --- |
| 2606.07684 | `AGENT-MEMORY` | `INFER-KV-CACHE` | Ch45“跨模型 KV reuse 更严格”“压缩、漂移与驱逐都需要可检验的误差预算”：传输的是模型执行状态，source/target mapping、patch、calibration 与 receiver fallback 属于 cache identity，不是 Agent 长期事实。 |
| 2606.07577 | `MULTIMODAL-REPRESENTATION` | `INFER-KV-CACHE` | Ch45“Multimodal KV 选择必须区分 Prefill key 统计与 Decode query 需求”：modality-aware budget、扰动敏感选择与 FullKV fallback 的 owner 是运行时 KV state；Ch23 只拥有输入表示 identity。 |
| 2606.07586 | `PLATFORM-PRODUCTION` | `AGENT-PLATFORM` | Ch84“可编程 Skill 需要输入、状态与副作用契约”“Skill Compiler 必须绑定 Target Profile”：人指导产生候选、数值正确性 gate、目标 NPU profile、admission 与回退组成 skill lifecycle；Ch49/Ch73 只接手编译执行与发布。 |
| 2606.07587 | `MODEL-MOE` | `INFER-SCHEDULING` | Ch56“Model Routing 与 Test-time Scaling 必须结算同一个 Budget”“Calibration 是在线 Routing State”：对象是 endpoint 选择、instance-specific value 与 oracle gap，不是 token-to-expert MoE router。 |
| 2606.08090 | `AGENT-RAG` | `INFER-SCHEDULING` | Ch56“Semantic Predicate 的 Token Cost 应成为 Query-planner State”：两阶段 semantic filter 改变 predicate ordering、selectivity/cost calibration 与执行计划，不拥有 RAG evidence truth。 |
| 2606.09079 | `AGENT-RAG` | `INFER-KV-CACHE` | Ch45“Future utility 的来源还可以进一步分叉”及 learned implicit lookahead / per-layer kept-index：indexer 预测未来 KV 需求，cache owner 决定 residency；Ch76 只拥有知识检索。 |
| 2606.09080 | `TRAIN-DATA` | `PLATFORM-EVALUATION-SYSTEM` | Ch66 的 runtime identity、端到端 workload 与 configuration-conditional evidence，配合 Ch49“硬件选择也不能只比较峰值 FLOPs”“单次最快 kernel 不能外推完整 Serving engine”：主要增量是 pruning 的真实加速评测合同，Ch49 为执行 handoff。 |
| 2606.08615 | `AGENT-MEMORY` | `MULTIMODAL-REPRESENTATION` | Ch23“Streaming Multimodal Identity 不止是 Token Type”“实时多模态表示还必须拥有可中断的时间状态”：per-second observation、长时 video memory 与响应 cadence 首先定义流式表示；Ch42/Ch77 分别接手 runtime 与持久 memory。 |
| 2606.09508 | `INFER-DECODE` | `INFER-KV-CACHE` | Ch45 的 adaptive per-head budget、future-importance kept set、compression/drift error budget：Prefill 选择和 Decode latent cache 压缩共同改变 KV residency；Ch43/Ch44 只描述阶段 handoff。 |
| 2606.09514 | `INFER-SCHEDULING` | `INFER-TENSORRT-LLM` | Ch49“Execution Plan 先拥有 State，再选择 Kernel”“Token-level 预算不能由三个独立近似器分别消费”：逐输入/逐 token depth routing 是模型内部 execution plan，不是 request/fleet placement。 |
| 2606.08300 | `AGENT-TOOL-CALLING` | `AGENT-PLANNING` | Ch79“Plan 不是解释文本”“从目标到状态图”“依赖、并行与 Critical Path”：QueryGraph 拥有多工具依赖图和确定性计划；Ch78 只拥有单次 tool proposal/receipt。 |
| 2606.09447 | `AGENT-PLATFORM` | `TRAIN-GRPO` | Ch33 的 environment / transformation graph、rollout identity、verifier 与 reward authority：Terraform 资源预置和 audit-log reward 是训练 rollout harness；Ch84 只接手训练后 Agent artifact。 |
| 2606.07595 | `PLATFORM-EVALUATION-SYSTEM` | `PLATFORM-SECURITY` | Ch72 的跨 channel data flow 与 `proposal → authorization → commit → effect receipt`：视觉文本传播到 tool arguments 是 action-boundary / trust-boundary failure；Ch66 只拥有复现实验和 scorer。 |
| 2606.08044 | `PLATFORM-SECURITY` | `PLATFORM-EVALUATION-SYSTEM` | Ch66“表征审计必须先消除模板混淆，再谈因果”“Evaluation-awareness 必须分开 Representation、Verbalization 与 Control”：干预可达的表征风险是评测证据边界；Ch72 接手风险处置。 |

上述 14 项全部判 `Existing Coverage`。它们揭示的是路由错误，不是正文缺口：若继续沿旧 owner 写，会把 KV state 误写成 Agent memory、把 endpoint routing 误写成 MoE、把 execution plan 误写成 fleet scheduling，反而破坏唯一 owner。

## 115 项全量 disposition 集合

以下集合是最终 authority。每个 ID 恰好出现一次；它同时给出最终 owner 与 `Existing Coverage` disposition，不以“未列 exception 即通过”的抽样方式省略候选。

- `AGENT-MCP` (1)：2606.07992
- `AGENT-MEMORY` (5)：2606.07711、2606.07909、2606.08151、2606.08702、2606.09483
- `AGENT-MULTI-AGENT` (4)：2606.07790、2606.07805、2606.07845、2606.08340
- `AGENT-PLANNING` (1)：2606.08300
- `AGENT-PLATFORM` (7)：2606.07586、2606.08106、2606.08348、2606.08867、2606.09122、2606.09316、2606.09421
- `AGENT-RAG` (1)：2606.08950
- `AGENT-REFLECTION` (2)：2606.08671、2606.08755
- `AGENT-TOOL-CALLING` (2)：2606.07904、2606.08790
- `AGENT-WORKFLOW` (4)：2606.07846、2606.08049、2606.08919、2606.09751
- `INFER-DECODE` (1)：2606.08411
- `INFER-GPU-MEMORY` (1)：2606.08761
- `INFER-KSERVE-TOPOLOGY` (1)：2606.09643
- `INFER-KV-CACHE` (7)：2606.07571、2606.07577、2606.07684、2606.07878、2606.08382、2606.09079、2606.09508
- `INFER-PD-DISAGGREGATION` (1)：2606.08635
- `INFER-PREFILL` (2)：2606.07703、2606.09441
- `INFER-REQUEST-LIFECYCLE` (1)：2606.08094
- `INFER-SCHEDULING` (5)：2606.07587、2606.07923、2606.08090、2606.09061、2606.09613
- `INFER-SPECULATIVE-DECODING` (1)：2606.07710
- `INFER-TENSORRT-LLM` (7)：2606.07581、2606.07665、2606.07713、2606.08891、2606.09514、2606.09682、2606.09686
- `MULTIMODAL-REPRESENTATION` (1)：2606.08615
- `PLATFORM-COST` (1)：2606.07632
- `PLATFORM-EVALUATION-SYSTEM` (28)：2606.07623、2606.07682、2606.07726、2606.07783、2606.07822、2606.07834、2606.07874、2606.07936、2606.08044、2606.08200、2606.08367、2606.08381、2606.08417、2606.08529、2606.08531、2606.08679、2606.08831、2606.08840、2606.08893、2606.08960、2606.09046、2606.09080、2606.09376、2606.09426、2606.09461、2606.09748、2606.09764、2606.09809
- `PLATFORM-MONITORING` (4)：2606.07631、2606.07889、2606.07968、2606.08590
- `PLATFORM-SECURITY` (16)：2606.07595、2606.07808、2606.07833、2606.07867、2606.07943、2606.08403、2606.08433、2606.08539、2606.08661、2606.08892、2606.09005、2606.09084、2606.09401、2606.09411、2606.09549、2606.09551
- `PLATFORM-TRACE` (3)：2606.08275、2606.09071、2606.09692
- `TRAIN-DATA` (1)：2606.07996
- `TRAIN-DISTRIBUTED-TRAINING` (3)：2606.08197、2606.08476、2606.09200
- `TRAIN-GRPO` (2)：2606.09138、2606.09447
- `TRAIN-PIPELINE-PARALLEL` (1)：2606.07881
- `TRAIN-RLHF` (1)：2606.09711

### 边界反例复核

以下项目看起来最容易因“局部/benchmark”被误删，本轮仍保留，但其 Evidence 权限被明确收窄：

- `2606.07845` 只支持“GRPO 在披露 coordination task 上没有自动闭合多 Agent gap”的负证据；它能挑战“单体后训练可直接迁移”的结论，不能证明 GRPO 普遍无效。
- `2606.08840` 只支持按语言和可执行 failure mode 拆开 aggregate pass rate，不保留模型排名为长期结论。
- `2606.08893` 的廉价 detector 只作 reward-hacking sensor；它不拥有安全裁决或 promotion authority。
- `2606.09461`、`2606.09764` 只保留异步参与者、跨模态/跨应用持久状态与环境复位的 evaluation contract，不外推 benchmark 排名。
- `2606.07623` 是形式化 certificate/threshold 框架，没有 production implementation；因此只能支持“声明的可判定性依赖观测模型与前提”，不能成为部署保证。
- `2606.08151` 的 memory-card 方法只作为 action-relevance 与 similarity-retrieval 的反例；50 个 SWE-bench 实例不授权通用收益。
- `2606.09751` 没有公开 evaluation，CHAP 只作为 typed session / handoff protocol 的概念证据，不证明协议已被生产验证。

## Books Existing Coverage 合并依据

除上表 14 个纠正项外，其余 101 项的 current owner 与当前正文一致。Existing 判断不是由 source trace 自证，而是按 owner-level 命题合并：

- Training：rollout/environment identity、reward/verifier 分权、异步 pipeline bounded inconsistency、collective/overlap 与 data provenance 已分别由 Ch33、Ch36、Ch38、Ch27 承载；
- Inference：Prefill/KV/PD/quantized execution/request scheduling 的 state identity、误差预算、admission 与 full/recompute fallback 已由 Ch42～56 承载；
- Platform：Evaluation、Monitoring、Trace、Cost 与 Security 已把 object identity、sensor/authority、uncertainty、effect boundary 和 release fallback 分开；
- Agent：Memory、Tool、Planning、Reflection、Workflow、Multi-Agent、MCP 与 Platform 已区分 information state、action proposal、dependency graph、durable commit 与 capability authority。

这些 owner 已包含旧方案为何合理、约束变化、状态/控制权、trade-off、failure mode 与 fallback。单篇论文只证明其披露模型、数据、硬件、环境和 evaluator 下的 operating point；没有任何作者 benchmark 被提升为跨系统常数。

## Gate

- Candidate semantic gate：**Pass（115/115）**；
- Evidence boundary gate：**Pass**；三项 abstract-only family 被限制为 Existing、无新正文授权；
- Owner identity gate：**Change required（14 项）**；Daily README 与 V3 artifacts 尚需同步上述 canonical owner；
- Books semantic gate：**Pass（115 Existing / 0 Integrate）**；
- Books residue gate：**Pass**；`2606.09774` 当前 Books 命中为 0；
- Report Complete：**尚不能标 Complete**，直到 14 项 owner/disposition 同步进 README 与 V3 artifacts，并由同步者重跑两个 validator 和跨文件集合检查。

本审计只新增本账本；没有修改 Books、Daily README、V3 artifacts、ROADMAP 或 `LEARNING_STATE`。
