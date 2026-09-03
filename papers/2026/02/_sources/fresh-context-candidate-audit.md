# February 2026 Fresh-context Candidate Audit

> **Status: Superseded finding checkpoint.** 本文件保留第一次 164-candidate
> 快照中发现的问题及其推理轨迹，不代表最终 Gate 状态。所有 finding 已在后续
> 12,520-row replay、284 个 exact-v1 Review、291-row Books audit 与 post-write
> semantic audit 中闭合；唯一最终状态源是
> `papers/2026/02/_sources/february-fresh-context-audit.json`。最终结果为
> Coverage / Evidence / Deep Selection / Books 四域 `passed`，unresolved=0。

## 审计边界与复算快照

本审计独立对读 `AGENTS.md`、`docs/RESEARCH_CONTRACT.md`、
`docs/REPORT_CONTRACTS.md`、`ROADMAP.md`，并检查 28 份
`screening-ledger-author.json`、28 份 `exact-v1-review-packet.json` 与
`papers/2026/02/01..28/README.md`。本文件只记录 finding，不修改 Books、Daily 正文或既有 ledger。

冻结快照复算结果如下：

- 28 个报告日；registered/full-screened = 12,520；retained = 164；pre-denominator closure = 12,356。
- Score V2：6 × 2、7 × 105、8 × 51、9 × 6。
- exact-v1：complete = 164、blocked = 0；deep = 162、standard = 2。
- 162 个 `score >= 7` 均标为 deep；2 个 score 6 均标为 standard。
- packet `problem` 中的 owner 与 `stable_node_id` 机械一致，0 个 mismatch。这只证明字段一致，不证明 owner 语义正确。
- 56 个 author-side JSON 的冻结聚合 hash：
  `9c2ae9b46b78130d81ed4efcf11979d1bd7a84978f8a85f0be2e8d62f5164633`。

Closure 抽样使用固定种子 `feb26-fresh-context-v1`：每个非空
`(report_date, reason_code)` stratum 取 SHA-256 最小项，再对每个非空
`(reason_code, primary_category)` stratum 同样取一项，最后按 arXiv ID 去重。
结果为 83 + 173 个 stratum、222 个唯一样本，覆盖 19 个有公告条目的日期、8 个
closure reason 与 76 个 primary category。该样本用于找反例，不用于估计总体 FN 比率。

## Finding 汇总

| Finding class | Confirmed / affected | Gate action |
| --- | ---: | --- |
| retained 明显 false positive | 4 | 从 denominator 移除，删除其 Review / Deep Analysis / Books 痕迹 |
| closure 抽样 false negative | 6 | 重开为 retained，执行 exact-v1 review |
| closure 定向复核 false negative | 9 | 重开为 retained，执行 exact-v1 review |
| Stable Node 语义误路由 | 8 | 改 owner 后重跑 Review、Selection 与 Books Comparison |
| 错误 limitations locator | 1 | 修复 locator/excerpt/claim boundary |
| `Not Disclosed` locator | method 19 / evaluation 4 / limitations 5 | 不得把缺失定位写成“公开了机制边界” |
| 通用 artifact 模板 | 164 | 逐 family 判断 artifact 是否为 claim-critical；53 个摘要显式披露 artifact 的条目优先补证 |
| receipt-list 冒充 Existing Proposition | 21 | Books disposition 退回 Not Assessed，改用真实命题后再判定 |
| 先验 `No Change — Existing Coverage` | 164 | 不能批量验收；按下文修正 Integrate / No Change / remove |
| withdrawn | 2 | exclusion 正确；补 authoritative status receipt |

因此四个 Daily semantic-audit scope（coverage、evidence、deep analysis selection、books）均应保持
`open`；结构 validator 通过不能提升为语义验收。

## A. Retained false positives

| arXiv ID | 日期 | Finding type | 建议动作 | 依据与边界 |
| --- | --- | --- | --- | --- |
| 2602.00003 | 2026-02-04 | FP / Books invalid | demote 为 `domain_application_without_system_delta`；删除 `MODEL-MOE` Review、Books row | exact-v1 显示这是跨境电商 whole-query 级多模型选择与 embedding fusion，不是 token-level MoE 的 router/capacity/expert-parallel 机制；验证只覆盖六个市场的 AUC/QPS。局部 domain ensemble 不足以进入长期 AI System 分母。 |
| 2602.02035 | 2026-02-04 | FP / selected narrative invalid | demote 为 `localized_method_without_ai_system_contract`；移除 `DA-20260204-1` | 摘要与 exact-v1 是通用 MARL 的 information bottleneck、VQ 与 gated communication，在机器人/群体环境中优化 bandwidth；没有 LLM-agent 的工具、记忆、delegation 或可迁移系统合同。 |
| 2602.18291 | 2026-02-24 | FP / selected narrative invalid | demote 为 `localized_method_without_ai_system_contract`；移除 `DA-20260224-1` | 方法是 MPE/MAMuJoCo 上的 online MARL diffusion policy 与 CTDE objective；没有视觉输入、语言接口或物理 VLA control contract，不能归 `MULTIMODAL-EMBODIED-VLA`。 |
| 2602.18415 | 2026-02-24 | FP / selected narrative invalid | demote 为 `survey_or_dataset_without_contract_delta`；移除 `DA-20260224-3` | 82 人、48,495 段对话的参与式隐私测量工作流与使用研究，提供的是研究数据采集方法，不是 release gate、scorer versioning、trajectory/environment evaluation contract。 |

## B. Pre-denominator closure false negatives

### B1. 固定种子分层样本内发现

| arXiv ID | 日期 | Finding type | 建议动作 | 摘要证据；exact-v1 前不得外推 |
| --- | --- | --- | --- | --- |
| 2602.00805 | 2026-02-04 | FN / sampled | retain，owner=`AGENT-RAG` 或 `PLATFORM-EVALUATION-SYSTEM`；exact-v1 核验 deployment/rollback contract | 摘要明确 shared dense-retrieval backbone 同时耦合 model selection、deployment、rollback，提出 component-wise mixed-stage configuration，并称已作为多应用共享检索服务部署；这已超过 `no_ai_system_mechanism_signal`。 |
| 2602.04431 | 2026-02-06 | FN / sampled / security override | retain，owner=`PLATFORM-SECURITY`，deep route | 摘要给出 Meta-Agent/Meta-Adversary 的 compromised-agent threat model、最坏攻击搜索与跨攻击目标/LLM 的评估；它改变多 agent safety evaluation contract，不只是局部质量方法。 |
| 2602.05780 | 2026-02-07 | FN / sampled | retain，owner=`TRAIN-DATA` 或 `AGENT-RAG`；exact-v1 核验 private-repo ingestion lineage | 摘要披露 enterprise private repository 的自动 ingestion、semantic-scope training-pair formation、RAG/FT 两条 customization path 和真实企业 case；存在数据与 customization ownership 变化。 |
| 2602.19762 | 2026-02-25 | FN / sampled | retain，owner=`INFER-TENSORRT-LLM`；exact-v1 核验编译 pass、支持面与 artifact | 摘要披露从 Triton/PyTorch 到 Qualcomm NPU binary 的 MLIR lowering stack、mega-kernel 与 TCM locality；即使 work-in-progress，也明显具有 compiler/runtime system mechanism，不能记为 `no_ai_system_mechanism_signal`。 |
| 2602.21140 | 2026-02-26 | FN / sampled | retain，owner=`INFER-SCHEDULING` 或 `PLATFORM-PRODUCTION-BEST-PRACTICE`；deep route | 摘要定义 MoE/attention colocated 与 disaggregated 两种 serving recovery path，在不重启 instance 的情况下恢复硬件故障，并称集成 Huawei Cloud MaaS/xDeepServe/XCCL；这是 failure/recovery ownership。 |
| 2602.22638 | 2026-02-28 | FN / sampled / author demotion | retain，owner=`PLATFORM-EVALUATION-SYSTEM`；deep route | 虽是 mobility workload，摘要给出 deterministic API-replay sandbox，隔离 live-service nondeterminism，并将 outcome validity、instruction、planning、tool use、efficiency 组成可复现 evaluation protocol；该合同可迁移，不能仅以 single-domain benchmark 关闭。 |

### B2. 分层样本之外的定向高信号复核

| arXiv ID | 日期 | Finding type | 建议动作 | 摘要证据；exact-v1 前不得外推 |
| --- | --- | --- | --- | --- |
| 2602.00286 | 2026-02-04 | FN / targeted | retain，owner=`MULTIMODAL-GENERATIVE-PARADIGMS` | 摘要建立 masked diffusion 的 generation order、parallelization bias、reverse-KL incoherence 与 verification cost 边界，直接改变并行生成的 commit/verification reasoning chain。 |
| 2602.00364 | 2026-02-04 | FN / targeted / security override | retain，owner=`PLATFORM-SECURITY`，cross-link `AGENT-RAG` | 摘要研究面向 LLM retrieval、RAG 与 agent memory 的 query-agnostic black-box poisoning/attack surface；即使攻击实现局部，threat model 应触发 security override。 |
| 2602.00966 | 2026-02-04 | FN / targeted | retain，owner=`AGENT-MULTI-AGENT` 或 `AGENT-PLATFORM` | 摘要给出 task-local decentralized routing、candidate screening、LinUCB、delayed feedback，以及 distribution shift/failure 下的 adaptive control，改变 multi-agent runtime route ownership。 |
| 2602.02499 | 2026-02-05 | FN / targeted | retain，owner=`MODEL-LONG-CONTEXT`，cross-link inference | 摘要提出 CPU suffix-automaton retrieval、model-state injection 与 async CPU/GPU pipeline；它同时改变可访问上下文与 execution path，不只是局部 accuracy 方法。 |
| 2602.02574 | 2026-02-05 | FN / targeted | retain，owner=`AGENT-MEMORY`，cross-link `PLATFORM-EVALUATION-SYSTEM` | 摘要将 store/merge/evict 写操作置于 byte budget 与 drift 下，并使用 byte-accurate cost model；这是 memory write policy/evaluation contract，`no_ai_system_mechanism_signal` 不成立。 |
| 2602.15831 | 2026-02-20 | FN / targeted | retain，owner=`AGENT-PLATFORM`，cross-link `AGENT-MCP` | 摘要明确 Human Card、formal communication schema 与 unified messaging abstraction，改变 agent-to-human identity/discovery/message interface；是否可执行须由 exact-v1/artifact 决定，不能预先关闭为局部方法。 |
| 2602.02585 | 2026-02-05 | FN / author demotion high risk | **最终建议 retain**，owner=`PLATFORM-MONITORING`，cross-link `AGENT-WORKFLOW` | 摘要给出生产 ReAct alert triage 的 log/API/runbook/RAG 控制流，并报告生产 deployment；核心是 observability action ownership，而非电商 domain 本身。90% MTI 声称须 exact-v1 限定。 |
| 2602.11790 | 2026-02-14 | FN / author demotion high risk | **最终建议 retain**，owner=`AGENT-WORKFLOW`，cross-link `MULTIMODAL-GENERATIVE-PARADIGMS` | 摘要给出 central orchestrator、shared production state、explicit quality gates、iterative critique 与 deterministic compiler；这是可执行 workflow state/commit contract。百万视频/日和 95% cost reduction 必须 exact-v1 核验，不得直接采用。 |
| 2602.14955 | 2026-02-18 | FN / author demotion high risk | **最终建议 retain**，owner=`PLATFORM-EVALUATION-SYSTEM`，cross-link `AGENT-PLANNING` | 摘要定义带 `depends_on` 并行依赖、结构化/非结构化工具 assignment、七维 plan evaluator、lineage 与 evaluator→optimizer loop；contact-center 只是 workload，plan evaluation contract 可迁移。 |

原 24 项 author demotion 中，上述 2602.02585、2602.11790、2602.14955、2602.22638
建议重开；其余 20 项按当前公开摘要维持 closure：
2602.00757、2602.01023、2602.02338、2602.03028、2602.04184、2602.04566、
2602.10869、2602.11076、2602.13301、2602.13808、2602.14033、2602.14200、
2602.15813、2602.15859、2602.16953、2602.17739、2602.17954、2602.19021、
2602.20577、2602.22059。这里的“维持 closure”不把摘要结果升级为完整机制结论。

## C. Stable Node owner 路由

| arXiv ID | 日期 | Finding type | 当前 → 建议 owner | 建议动作与依据 |
| --- | --- | --- | --- | --- |
| 2602.00397 | 2026-02-04 | owner | `MODEL-LONG-CONTEXT` → `INFER-PREFILL` | 主机制是 prefill-stage FFN predictive sparsity 与 TTFT；长上下文只是 workload。改 owner 后重写 problem、target chapter 与 adjacent refs。 |
| 2602.00509 | 2026-02-04 | owner | `MODEL-MOE` → `INFER-SCHEDULING` | PROBE 的 canonical delta 是 online prediction/planning/prefetch、dynamic expert replication、token assignment 与 co-scheduling；MoE 是被调度对象。 |
| 2602.02027 | 2026-02-04 | owner | `TRAIN-RLHF` → `MODEL-SAMPLING`（cross `PLATFORM-SECURITY`） | 训练只产生 safety expert/gate；实际控制发生在逐 token expert interpolation 的 inference-time decoding。 |
| 2602.03295 | 2026-02-05 | owner | `INFER-TENSORRT-LLM` → `INFER-PREFILL` | POP 的责任边界是 prefill-only layer skipping、prefill/decode transition、independent KV projection 与 first-token boundary，不是特定 compiler stack。 |
| 2602.03560 | 2026-02-05 | owner | `INFER-KV-CACHE` → `MODEL-LONG-CONTEXT`（cross KV） | HySparse 首先改变 full/sparse attention layer architecture；KV sharing 是架构的次级状态收益。 |
| 2602.10090 | 2026-02-12 | owner | `MULTIMODAL-WORLD-MODELS` → `TRAIN-DATA` 或 `AGENT-PLATFORM` | AWM 是 code/database-backed executable synthetic environment generator，不是学习 action-conditioned predictive dynamics 的 World Model。 |
| 2602.11301 | 2026-02-14 | owner | `AGENT-MULTI-AGENT` → `PLATFORM-SECURITY` | canonical claim 是 governance、context envelope、structured output、traceability/provenance/human gate；多 agent 是 reference-architecture 载体。 |
| 2602.11686 | 2026-02-14 | owner | `MODEL-MOE` → `TRAIN-DISTRIBUTED-TRAINING`（cross MoE） | FSEP、expert parameter sharding/restore、All-to-All scheduling 与 runtime re-layout 都属于 distributed training execution ownership。 |

## D. Exact-v1 evidence 与 claim-boundary findings

### D1. 逐项错误

| arXiv ID | 日期 | Finding type | 建议动作 | 依据 |
| --- | --- | --- | --- | --- |
| 2602.03295 | 2026-02-05 | evidence locator false positive | 将 limitations 退回 `Not Disclosed` 或定位真实 limitation；同步重写 excerpt 与 claim boundary | 当前 locator 是 `§2019. Limitations of the empirical fisher approximation...`，excerpt 实际来自参考文献条目，不是 POP 的 limitation。 |
| 2602.11301 | 2026-02-14 | evidence/claim unsupported | 在 method/evaluation/limitations 均未定位前，不能以 deep review complete 支持机制或 Books 判断 | 三个 locator/excerpt 全为 `Not Disclosed`，论文摘要又明确“future empirical validation”；最多可作 proposed reference architecture，不能写成已验证 enterprise architecture。 |
| 2602.11686 | 2026-02-14 | evaluation locator weak | 将 evaluation 定位到实际 experiments，而非 `Appendix A.6 Evaluation and expected results`；核对 1.69× 的硬件/拓扑/基线 | 当前 excerpt 是可复现性“expected”文字，不能单独承担 abstract 的 measured speedup claim。 |
| 2602.15763 | 2026-02-19 | claim-owner mismatch | 若 owner 保持 `TRAIN-RLHF`，method/evaluation 必须定位 async RL infrastructure/algorithm 与 system evaluation；否则把 general model-release/architecture 事实降为 context | 当前 method=`§2.1 Architecture`、evaluation=general reasoning benchmarks，不能支撑“async RL infrastructure 改变 TRAIN-RLHF”的 Books claim。 |

### D2. `Not Disclosed` 的具体 IDs

- method locator（19）：2602.03974、2602.04399、2602.04448、2602.05842、
  2602.11882、2602.11291、2602.11301、2602.11937、2602.09430、2602.02599、
  2602.03782、2602.02110、2602.01797、2602.23200、2602.15513、2602.16313、
  2602.08007、2602.07397、2602.08404。
- evaluation locator（4）：2602.11301、2602.01797、2602.17345、2602.07223。
- limitations locator（5）：2602.11301、2602.01797、2602.00780、2602.01801、
  2602.07616。

这些缺失本身可合法记录为 `Not Disclosed`，但对应 narrative 不能继续使用
“exact-v1 的 `Not Disclosed` 公开了机制边界”这种自相矛盾句式。24 个 claim boundary
直接包含 `Not Disclosed` 占位符；应改写为“该 facet 未披露，因此不支持相应 claim”，而不是将占位符当章节。

全部 164 个 `artifact_locator` 都是相同模板
“linked external artifact was not required ...”。其中 53 个 retained 摘要显式出现 code、GitHub、repository、
open-source 或 artifact signal。至少应对每项记录：artifact 是否为 claim-critical、实际 URL/commit/status，
或为何 manuscript 足以支撑本次 claim；不能用同一模板替代 paper-specific judgment。

## E. Withdrawn

| arXiv ID | 日期 | Finding type | 建议动作 | 依据 |
| --- | --- | --- | --- | --- |
| 2602.18914 | 2026-02-25 | withdrawn receipt incomplete | 保持 pre-denominator exclusion；补 arXiv authoritative status URL、retrieved-at、withdrawal date 与公开 reason（若披露） | ledger/packet 已清除 score/Review/Books，方向正确；但 ledger 只有“exact identity 明示 withdrawn”，packet 仅保存 ID，缺可审计 status receipt。 |
| 2602.19967 | 2026-02-25 | withdrawn receipt incomplete | 同上 | exclusion 正确，证据 receipt 不完整。 |

## F. Daily 四个 semantic-audit scope

### F1. Coverage

4 个 FP 与 15 个 FN 未解决前，28 份报告的 coverage audit 不能关闭。零候选日可维持
`In Progress`；不应把结构完整性解释为当日来源语义已接受。

### F2. Evidence

除 D 节外，92 个 limitations locator 指向 Conclusion/Future Work。Conclusion 可以包含 limitation，
但不能由标题自动视为反证。应逐项确认 excerpt 是否真的给出适用边界/failure，而不是作者总结；
否则保留 `Not Disclosed` 并缩小 claim。

### F3. Deep Analysis Selection

- 57 个 narrative unit 被 selected。
- 3 个 selected unit 来自本审计判定的 FP：`DA-20260204-1`（2602.02035）、
  `DA-20260224-1`（2602.18291）、`DA-20260224-3`（2602.18415）；应删除并从当日
  corrected eligibility frontier 重新选择。
- 9 个 selected unit 的 method locator 为 `Not Disclosed`：2602.02110、2602.03974、
  2602.04399、2602.05842、2602.08007、2602.11882、2602.11301、2602.15513、
  2602.16313。它们的 narrative 在补到 method evidence 前不能声称机制已公开；可以保留为待补证候选，
  或让有完整 receipt 的同日 family 替换。

### F4. Books Comparison

164/164 行都预填 `No Change — Existing Coverage`，不能作为独立 Books Decision。以下 21 个
Existing Proposition block 实际只摘录另一批 source-family receipt 列表，而非可与本 family 对读的长期机制命题：

2602.02035、2602.01640、2602.00748、2602.03495、2602.04711、2602.06038、
2602.05249、2602.11192、2602.11513、2602.12691、2602.13151、2602.14093、
2602.14337、2602.16520、2602.17345、2602.17692、2602.18415、2602.20379、
2602.20720、2602.21477、2602.22663。

这些 21 行应先退回 `Not Assessed`，改用目标章节中能陈述 constraint、state/control ownership、
trade-off 与 fallback 的真实 proposition，再决定 Integrate/No Change。相邻章节引用机械上均指向 ROADMAP
相邻章节；但 owner 错误的 8 项，其 adjacent refs 也随之失效，必须随 owner 重算。

明确 disposition 修正如下：

| arXiv ID | 当前 | 建议 | Books 依据 |
| --- | --- | --- | --- |
| 2602.00003、2602.02035、2602.18291、2602.18415 | No Change | remove / no Books row | 它们应先退出 candidate denominator。 |
| 2602.00397 | No Change at `MODEL-LONG-CONTEXT` | **Integrate** at `INFER-PREFILL` | 当前 Prefill 章讨论 token/block sparsity，但没有承担 block-wise context-aware FFN neuron prediction、error compensation 与 layer-wise sparsity schedule 这条分支。 |
| 2602.00509 | No Change at `MODEL-MOE` | **Integrate** at `INFER-SCHEDULING` | 当前 MoE proposition 讲 router/load semantics；PROBE 新增 next-layer prediction、replication、placement 与 split-phase prefetch 的 runtime control chain。 |
| 2602.02027 | No Change at `TRAIN-RLHF` | **Integrate** at `MODEL-SAMPLING`, cross security | Sampling 章当前只覆盖通用 logits transform；NGSD 增加 base/expert distribution interpolation 与 learned safety gate，应以受限安全解码 branch 写入。 |
| 2602.03295 | No Change at `INFER-TENSORRT-LLM` | **Integrate** at `INFER-PREFILL`，修证后 | Prefill-only layer skipping 与 decode transition/KV integrity 是新的 phase contract；当前 limitations receipt 还是错误的 bibliography hit。 |
| 2602.10090 | No Change at World Models | **Integrate** at `TRAIN-DATA`/`AGENT-PLATFORM` | code/database-backed executable environment、state transition 与 reward access 改变 agent training environment ownership；不能用 World Model 章节标题吸收。 |
| 2602.03560 | No Change at KV | **No Change after reroute** to `MODEL-LONG-CONTEXT` | 长上下文章已有 hybrid sparse/full attention、selector 与 cache/compute trade-off；改用该真实 proposition，并把 HySparse 保持为受限替代证据即可。 |
| 2602.11301 | No Change at Multi-Agent | **No Change after reroute** to `PLATFORM-SECURITY` | Security 章已有 identity/policy/evidence/human gate 的长期命题；PBSAI 无独立 method/evaluation/limitations，只能作为 proposed architecture，不足以触发 Integrate。 |
| 2602.11686 | No Change at MoE | **No Change after reroute** to `TRAIN-DISTRIBUTED-TRAINING` | 分布式训练章已有静态 EP→动态 token/weight placement、authoritative weight/optimizer owner 与 fallback；FSEP 可作替代证据，不能按当前 MoE target 判 No Change。 |
| 2602.15763 | No Change at RLHF system-cost bullet | **No Change after retarget** | RLHF/GRPO/Distributed Training 已有 async rollout/training、policy freshness 与 bounded-staleness 命题；应改 target 到该 proposition，并把 claim 限于论文真正定位的 async RL sections，而非 general benchmarks。 |

其余未列为 Integrate/remove/retarget 的 retained family，在修复真实 Existing Proposition、evidence locator
和 owner 后，可维持 **No Change**；这不是批量接受当前 164 行，而是要求每行重新给出可检查的 proposition-level
comparison。任何不能完成该对读的条目应保持 `Not Assessed`，而不是默认 No Change。

## Gate 结论

当前状态可以表述为：机器结构与计数自洽，但 fresh-context semantic audit 有未解决 findings。
Coverage、Evidence、Deep Analysis Selection 与 Books Gate 均不能通过；Daily 保持 `In Progress` 是正确状态。
