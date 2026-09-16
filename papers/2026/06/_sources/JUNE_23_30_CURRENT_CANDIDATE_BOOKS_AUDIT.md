# 2026-06-23/24/25/26/29/30 Current V3 Candidate → Books Fresh Audit

审计时间：2026-09-11（Asia/Shanghai）
审计性质：非作者、fresh-context、逐项语义审计
审计对象：`papers/2026/06/{23,24,25,26,29,30}/README.md` 当前候选表、对应
`daily-202606DD/v3-admission-audit-20260910.json`、canonical raw identity、exact-v1 题摘/定位，以及各 canonical owner 在首个顶层
`## Review notes` 之前的正文。
写入边界：本账本是唯一修改；未修改 Books、Daily、V3 ledger 或 `LEARNING_STATE`。

## 1. 判定口径

1. `Actual Body`：长期机制确实位于目标章首个顶层 `## Review notes` 之前；段落必须同时说明旧边界、状态/控制机制、代价或 failure、回退/共存，marker 只作定位，不作证明。
2. `Existing Coverage`：候选属于 current Daily，但其长期命题已经由正文中的通用机制完整承载；后置 trace、owner-merged block 或 source note 不增加正文权威。
3. `Body Writeback Required`：候选有长期增量，但当前只在顶层 Review notes 后；需要按 Stable Node 合并后写回正文。
4. `De-admit`：题摘只表明垂直应用、通用 ML/硬件对象、局部表示/recipe 或 benchmark，不形成大模型/大模型基础设施的长期贡献。ROADMAP 映射、Books marker 与旧 candidate 身份均不能反向授权。

## 2. 总结

本轮按 Daily 当前表共有 230 项。写中审计曾发现 06-30 的 5 项真实正文缺口；作者随后把它们写入正确 owner 的顶层 Review notes 前正文，本账本以下按写后当前文件重新验收。

| 日期 | 当前表项 | Actual Body | Existing Coverage | Body Writeback Required | De-admit | Gate |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 06-23 | 50 | 11 | 39 | 0 | 0 | Candidate/Books PASS |
| 06-24 | 29 | 1 | 28 | 0 | 0 | Candidate/Books PASS |
| 06-25 | 30 | 1 | 26 | 0 | 3 | REOPEN：3 项准入撤销；strict JSON 身份错配 |
| 06-26 | 37 | 1 | 35 | 0 | 1 | REOPEN：1 项准入撤销 |
| 06-29 | 27 | 2 | 22 | 0 | 3 | REOPEN：3 项准入撤销；1 条 Books 采用链需撤销 |
| 06-30 | 57 | 6 | 48 | 0 | 3 | REOPEN：3 项准入撤销；6 项 Books 写后 PASS |
| **合计** | **230** | **22** | **198** | **0** | **10** | **4 个日报需重开** |

因此，若落实本审计，current candidate denominator 应由 230 调整为 220；Books 结论为 22 项 Integrate、198 项 Existing Coverage、0 个正文缺口。不能用 README 当前的 `整合：` 标签数量替代 Actual Body 计数。

## 3. Current authority 与 identity 审计

- 六个 Daily 表内 source family 没有跨日报告重复；230 个表内 ID 均能在同日 canonical raw identity 中找到，`resolved_owner_report_date` 均与日报日期一致。
- 06-23、24、26、29、30 的 README candidate set 与 `v3-admission-audit-20260910.json` candidate set 相同。
- **06-25 strict JSON 损坏**：README 当前保留 `2606.24934`、明确降级并移除 `2606.25453`；JSON 却把 `24934` 标为 `closed_before_candidate`，且其 reason 错写成 EmuGEMM 的题名/理由，同时把 `25453` 留为 candidate。精确差集是 `README-only=2606.24934`、`JSON-only=2606.25453`。current Daily 的人工表述与表格可还原正确意图，但 strict ledger 在修复前不能称 machine authority 闭合。
- `2606.24934` 的 canonical identity 是 *Unprivileged Topology Certificates for Cloud GPU Attestation*，owner date 为 2026-06-25；`2606.25453` 的 canonical identity 是 *EmuGEMM*。两者 hash 不同，不能互换 reason 或状态。

## 4. Actual Body：22 项逐项验收

| 日期 / family | Canonical owner | 顶层 Review notes 前的正文锚点 | Fresh 结论 |
| --- | --- | --- | --- |
| 06-23 / `21023` | INFER-GPU-MEMORY | `54-gpu-memory.md:523` 后 numerical-instability/HEAL 段 | PASS：kernel-boundary downcast → 补偿路径 → 精度/硬件 identity 与回退完整。 |
| 06-23 / `22327` | INFER-SCHEDULING | `56-inference-scheduling.md:1030` 后 geometry-aware scheduling 段 | PASS：workload shape/SLO slack、估计失准与保守 admission 共存完整。 |
| 06-23 / `22504` | PLATFORM-SECURITY | `72-security.md:1677` 后 resource/effect/phase capability 段 | PASS：grant/revoke/effect-time recheck、bypass 边界和旧路径完整。 |
| 06-23 / `22528` | AGENT-CONTEXT | `75-context.md:478` 后 compaction governance 段 | PASS：constraint pinning、typed state、effect-time fallback 完整。 |
| 06-23 / `22541` | INFER-PD-DISAGGREGATION | `55-pd-disaggregation.md:445` 后 async MoE prefill 段 | PASS：异步状态身份、stale/misroute、同步回退完整。 |
| 06-23 / `22560` | PLATFORM-GATEWAY | `62-gateway.md:194` 后 evidence-bound gateway provenance 段 | PASS：path/policy/endpoint/fallback receipt 与 hidden-provider 边界完整。 |
| 06-23 / `22593` | PLATFORM-MODEL-REGISTRY | `59-model-registry.md:275` 后 release-authority 段 | PASS：发布/撤回/metadata authority 与可见性限制完整。 |
| 06-23 / `22659` | PLATFORM-SECURITY | `72-security.md:1680` 后 severity-aware detector calibration 段 | PASS：shift slice、false-negative risk 与受测范围完整。 |
| 06-23 / `22698` | PLATFORM-TRACE | `69-trace.md:269` 后 black-box forensics 段 | PASS：probe/config identity、fingerprint 仅作 evidence、drift failure 完整。 |
| 06-23 / `22737` | PLATFORM-EVALUATION-SYSTEM | `66-evaluation-system.md:2539` 后 deterministic GroundEval 段 | PASS：predicate/event log、未编码目标和 judge 共存边界完整。 |
| 06-23 / `22932` | TRAIN-DISTRIBUTED-TRAINING | `36-distributed-training.md`“Gradient 不必在 Backward 与 Optimizer 之间完整物化”及 `:432` binding | PASS：两阶段旧边界、fused consume、step commit、数值/recovery 回退完整。 |
| 06-24 / `23743` | INFER-TENSORRT-LLM | `49-tensorrt-llm.md:1430` 后 typed execution artifact 段 | PASS：agent proposal/validator commit、instance-specific 收益与人评回退完整。 |
| 06-25 / `25353` | INFER-PREFILL | `43-prefill.md:347` 后 weight/attention placement 段 | PASS：双路径状态、同步/layout 代价和共置回退完整。 |
| 06-26 / `26383` | PLATFORM-MONITORING | `67-monitoring.md:359` 后 speed-of-light model 段 | PASS：校准上界只是诊断基线，失配回 direct profile/SLO。 |
| 06-29 / `27797` | TRAIN-DISTRIBUTED-TRAINING | `36-distributed-training.md`“Teacher 与 Student 不应共享一份并行 Plan” (`:674-680`) | PASS：非对称 plan、handoff identity、search/buffer 代价、对称基线回退完整。 |
| 06-29 / `27806` | AGENT-PLANNING | `79-planning.md`“学习到的 Transition 只能验证候选，不能提交环境事实” (`:67-73`) | PASS：proposal/commit authority 分离、共享盲点和真实 observation/人工回退完整。 |
| 06-30 / `28361` | AGENT-RAG | `76-rag.md`“跨轮压缩应保存可续写的结论状态，而不是反复搬运历史” (`:414-430`) | PASS：history 重放旧边界、conclusion-chain state、信息损失与原文回取完整。 |
| 06-30 / `28661` | PLATFORM-EVALUATION-SYSTEM | `66-evaluation-system.md`“相关采样会抬高 Coverage，却压低 Selection 上限” (`:2705-2711`) | PASS：coverage/selection/correlation 分离、非普适 ceiling 与 abstain 回退完整。 |
| 06-30 / `29151` | AGENT-RAG | `76-rag.md`“从固定 Retriever 演进到可提交的 Logical / Physical Plan” (`:636-650`) | PASS：typed operator/DAG/physical plan、commit owner、profile drift 与固定检索回退完整。 |
| 06-30 / `29472` | AGENT-PLATFORM | `84-agent-platform.md`“Observation Interface 必须独立于 Action Clock” (`:458-474`) | PASS：gated keyframe/audio/narration/receipt、token/隐私代价与高保真/人工回退完整。 |
| 06-30 / `29565` | INFER-REQUEST-LIFECYCLE | `42-what-happens-during-inference.md:320-324` | PASS：idle speculative state、base identity、accept/invalidate 与普通 Prefill/Decode 共存完整。 |
| 06-30 / `29601` | AGENT-MULTI-AGENT | `82-multi-agent.md`“声明式协议约束 Transition，而不是相信参与者会协调” (`:303-322`) | PASS：sayso/nono/nogo、protocol/workflow owner、规则冲突与串行/人工回退完整。 |

### 06-30 写后专项

新增五段均位于其 owner 的自然论证位置，而非章末孤立收据：`28361` 承接压缩控制并回到原文 provenance，`29151` 承接 typed retrieval state，`29472` 紧随 Agent Runtime State Machine，`29565` 延长 request lifecycle 后再进入自检，`29601` 紧随 Message/authoritative state 区分。owner、同日 canonical identity、exact-v1 limitation authority、相邻衔接、trade-off/fallback 均 PASS。`28379` 没有被强行补写，见下节 Existing Coverage。

## 5. Existing Coverage：198 项完整账目

下表按 Stable Node 合并；每一行列出的所有 family 都以该行给出的**现有、顶层 Review notes 前正文命题**覆盖。这里的判断来自正文语义，不来自 marker。

| Stable owner | Current family（省略 `2606.`） | 精确正文锚点 |
| --- | --- | --- |
| AGENT-CONTEXT | `26979, 27045, 29718, 30005` | `75-context.md`“Context Assembly Pipeline”“Context Compression 必须保留执行状态，而不只是语义”“Context Mutation 是 Agent Proposal，State Owner 负责校验与提交”。 |
| AGENT-MCP | `27027, 28690, 29073` | `83-mcp.md`“MCP 不等于 Tool Authorization”“从单工具扫描到组合级 Admission”“从静态 Endpoint 到受限 Tool Program”。 |
| AGENT-MEMORY | `20954, 22030, 23195, 23752, 24151, 24428, 24535, 24775, 25115, 25161, 25449, 26511, 27472, 28434, 28781, 29279, 29788, 30566` | `77-memory.md`“Memory Write 是高风险决策”“Compact Control State 与 Exact Evidence Archive”“先分解 Memory 组件，再判断 Graph 是否值得”“Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery”“Provenance 必须进入 read、action 与 repair 路径”。 |
| AGENT-MULTI-AGENT | `21666, 22203, 26156, 27288, 27409, 28925, 28958, 30602` | `82-multi-agent.md`“Message 不是 State”“Pairwise coupling 不能外推 group dynamics”“Verification Delay 也是拓扑控制状态”“多 Agent 拓扑必须先通过 Equal-budget Pareto Admission”。 |
| AGENT-PLANNING | `26918` | `79-planning.md`“学习到的 Transition 只能验证候选，不能提交环境事实”及 planning/evaluation 分权主线。 |
| AGENT-PLATFORM | `21399, 23983, 24311, 26924, 27416, 28235` | `84-agent-platform.md`“Agent Runtime State Machine”“三个平面”“Harness、Protocol 与 Credit 都是 Platform-owned Artifact”“Workspace 是长期行动的隔离单元”。 |
| AGENT-PROMPT | `26356` | `74-prompt.md`“条件化机制分支与共存边界”下的模块组合干扰命题；正文已有 Prompt/Context owner 边界，source-specific 单行不构成额外 Integrate。 |
| AGENT-RAG | `21777, 25191` | `76-rag.md`“Retrieval Control 应成为 Reader 外部的 Typed State”“Retrieval Router 选择的是检索系统，而不只是文档”“Escalation 与 Abstention Threshold 必须联合校准”。 |
| AGENT-TOOL-CALLING | `20922, 21409, 24551, 25605, 25819, 26669, 26978, 30531` | `78-tool-calling.md`“模型输出只是 Proposal”“Tool Discovery 与选择”“Tool Result 之后还需要独立的 Outcome Contract”“Tool Robustness 要按 Failure Stage 注入”。 |
| AGENT-WORKFLOW | `22175, 22741, 23797, 24598, 25447, 26721, 27009, 28279, 28379` | `81-workflow.md`“从一次性脚本到平台拥有的可编辑 DAG”“Template、Realized Graph 与 Trace 不是同一个对象”“Distributed Event Log 是 Partial Order，不是单一时间线”。`28379` 的 dependency graph/node-version/retrieval-repair 已由这三处完整覆盖。 |
| INFER-DECODE | `23521, 29207, 30389` | `44-decode.md`“Decode 的结束条件”“条件化机制分支与共存边界”“Decode-only Compute Branch 仍必须尊重单一 KV Owner”。 |
| INFER-GPU-MEMORY | `24506, 25519` | `54-gpu-memory.md` GPU memory lifecycle、precision/materialization 与条件化共存主线；冷权重/KV 分层和低比特隐性 token 成本不需要另立 owner。 |
| INFER-KV-CACHE | `21238, 21633, 23961, 24033, 24467, 26472, 26666, 26875, 28831, 29563` | `45-why-kv-cache-speeds-up.md`“从 workload-aware eviction”“压缩预算从单轴推进到 Token × Feature 二维”“从不可逆 Eviction 到可恢复的分层 Recall”“KV Eviction 应显式承认自己是有偏估计”。 |
| INFER-PD-DISAGGREGATION | `29708, 29986` | `55-pd-disaggregation.md` PD state ownership、异构 memory tier、transfer/SLO 与同步回退主线。 |
| INFER-PREFILL | `22968` | `43-prefill.md` Prefill pipeline、chunk/memory orchestration 与 placement contract 主线。 |
| INFER-SCHEDULING | `21401, 21712, 21868, 22983, 26607, 27743, 28565, 29094, 29424, 29629, 30391, 30560` | `56-inference-scheduling.md`“SLO-aware Admission”“Expert weights 与 KV 的联合 working set”“从逐配置压测到校准后的配置搜索”“Model Routing 与 Test-time Scaling 必须结算同一个 Budget”。 |
| INFER-SPECULATIVE-DECODING | `24957, 25091, 25097, 26744, 27550, 30265` | `48-speculative-decoding.md`“Verify Length 不是孤立的固定超参数”“Edge / Cloud 分离”“Acceptance 不是独立常数，在线决策必须结算系统状态”“Draft 结构必须同时优化 Coverage 与 Verification Waste”。 |
| INFER-TENSORRT-LLM | `26344, 26453` | `49-tensorrt-llm.md`“Kernel Agent 应生成 Typed Schedule，而不是自由文本 Patch”“Generated Kernel 必须先进入 Typed Schedule IR”“架构收益必须贯穿完整 Serving Pipeline”。 |
| MODEL-MOE | `29982` | `21-moe.md`“Router 选择 Expert，Placement 决定这次选择能否低成本执行”“Dispatch 与 Aggregation 是两种不同责任”。 |
| PLATFORM-EVALUATION-SYSTEM | `20668, 20695, 20724, 20820, 21255, 21678, 22329, 23915, 23937, 24020, 24996, 25487, 25760, 25782, 26071, 26185, 26300, 26429, 26836, 26990, 27226, 27406, 27669, 27934, 28013, 28050, 28430, 28839, 29033, 29054, 29159, 29490, 29914, 29920, 29957` | `66-evaluation-system.md`“Evaluation Identity 必须包含 Harness 与 Environment”“Agent and Outcome Evaluation”“Judge 只能提案，Evidence Gate 才能 Override”“Tool Robustness 要按 Failure Stage 注入”“部分评测必须预先声明停止与淘汰状态”。 |
| PLATFORM-GATEWAY | `27457` | `62-gateway.md` policy/path/endpoint identity、route/fallback receipt 与外部流量 owner 主线。 |
| PLATFORM-GPU-SCHEDULER | `25098` | `63-gpu-scheduler.md`“Power Budget 是分层资源契约”“从削峰响应到 Grid-responsive Compute”“没有可证稳定性，就不能承诺有限等待时间”。 |
| PLATFORM-MONITORING | `24119, 27679, 28116, 30449` | `67-monitoring.md` calibration-bound sensor、直接 profile/fallback 与 monitor 不拥有 truth/commit 的主线；`24119` 的单行 LoRA signal 不足以单独构成 Integrate。 |
| PLATFORM-PRODUCTION | `22013` | `73-production-best-practice.md`“Load test 是 SLO boundary search”及 adaptive capacity search/warm-up/arrival/artifact identity 段。 |
| PLATFORM-SECURITY | `21129, 21338, 21638, 21732, 21842, 21877, 22916, 23277, 23768, 23927, 23969, 24245, 24322, 24402, 24408, 24934, 25189, 25349, 25721, 26028, 26057, 26298, 26377, 26479, 26524, 26649, 27511, 27567, 27683, 27944, 28061, 28425, 28679, 28739, 29225, 30119, 30383` | `72-security.md`“从文本是否恶意到谁获得了行为控制权”“Agent authority BOM、channel coverage 与 executable PoV”“Canonical Action 与 Effect-time Authorization”“Taint 传播需要可隔离、可验证返回的恢复路径”“Unlearning 必须分开参数擦除与推理拒答”。 |
| PLATFORM-TRACE | `24626, 26449, 27154` | `69-trace.md` provenance/evidence 不等于 truth、contamination control-flow divergence 与 causal-process supervision 主线；`26449` 的单行 binding 只复述此通用边界。 |
| PLATFORM-TRAINING-OPERATOR | `29871` | `60-training-operator.md`“Reconciliation 状态机”“Live Training Control 必须是可审计 Proposal，而不是直接改 Run”。 |
| TRAIN-DATA | `24133, 24998` | `27-data.md`“Data Mixture 应先被当作交互实验，而不是比例预测”“Duplicate Detection 与 Retention Policy 必须分离”“Provenance 必须追踪到派生记录与 token”。 |
| TRAIN-DISTRIBUTED-TRAINING | `22768, 24143, 25759, 26997, 27153` | `36-distributed-training.md`“异步训练必须分开 Throughput、Freshness 与 Objective Ownership”“通信压缩必须把编解码写进 Critical Path”“二阶 Optimizer State 可以移出关键路径，但一致性成为 Runtime 状态”。 |
| TRAIN-DPO | `21089` | `34-dpo.md`“DPO 保留了什么难题”“Online Discovery 与 Offline Preference Update 可以分权”。 |
| TRAIN-GRPO | `21090, 22164, 26027, 28436` | `33-grpo.md`“Reward 轨迹的可推导性、感知依赖与 decision density”“Verifier 也成为 Policy 时，必须分离更新与权威”“Tool-use RL 的训练对象包含环境编排”。 |
| TRAIN-PIPELINE-PARALLEL | `30634` | `38-pipeline-parallel.md`“异步 Pipeline：去掉 Bubble 会把成本移到参数版本”“有界异步用多条反向流水填 Bubble，但不取消 Update Boundary”。 |
| TRAIN-PRETRAINING | `29554` | `28-pretraining.md`“Optimizer State 也必须服从数据与硬件契约”“训练稳定性是多层系统问题”。 |
| TRAIN-RLHF | `27578, 27580` | `31-rlhf.md`“Reward Heterogeneity 同时存在于 Rater Identity 与反馈时间”“在线 Credit 需要显式的时序状态”“多路反馈的混合权重应由噪声状态驱动”。 |

## 6. De-admit：10 项与撤销链

| 日期 / family | 当前 owner | De-admit 理由 | 必须撤销的采用链 |
| --- | --- | --- | --- |
| 06-25 / `25082` | PLATFORM-GPU-SCHEDULER | 通用 AI/ML job 的单 MIG simulation/RL repartitioning；题摘没有 LLM token/KV/parallel-state 或大模型 lifecycle contract。 | Daily 候选与深读项；删除 `63-gpu-scheduler.md:312` source-specific note。 |
| 06-25 / `25285` | INFER-GPU-MEMORY | MS-HiLoRA + feature mixer 是一次性多稀疏度的局部模型压缩 recipe；“可部署多个 sparsity”不等于 runtime/serving control contract。 | Daily 候选/`整合`；删除 `54-gpu-memory.md:632` source-specific note。 |
| 06-25 / `25608` | PLATFORM-SECURITY | 把标准 HybridRAG/KG/Multi-LLM 组合应用到德国 IT-Grundschutz 认证；贡献对象是垂直认证流程，没有新的通用 security authority/effect/release 机制。 | Daily 候选与证据项；Books 当前无正文采用。 |
| 06-26 / `27005` | PLATFORM-GPU-SCHEDULER | 通用异构 AI model population 的 fairness/interpretability composite-utility simulation；没有大模型特有 workload/state 或真实 infra contract。 | Daily 候选与证据项；Books 当前无采用。 |
| 06-29 / `27558` | PLATFORM-EVALUATION-SYSTEM | LinkedIn race/ethnicity fairness measurement 的通用产品 ML 隐私方案；不是大模型/大模型基础设施贡献。 | Daily 候选与证据项；Books 当前无采用。 |
| 06-29 / `27841` | PLATFORM-COST | 295 个通用 neural architectures 的 task-independent layer-wise energy estimator；对象与方法均未形成 LLM-specific inference/service contract。 | Daily 候选；删除 `70-cost.md:242-244` one-line semantic binding 和 `:346` source note。该单行也缺 trade-off/fallback，不能保留为 Actual Body。 |
| 06-29 / `27997` | PLATFORM-EVALUATION-SYSTEM | 主要对象是 TSC/推荐数据集子集选择，MTEB 只是补充实验；bootstrap/FAFI 排名保持是通用 benchmark 方法，不是大模型系统贡献。 | Daily 候选与证据项；Books 当前无采用。 |
| 06-30 / `28666` | PLATFORM-SECURITY | 把既有 TRiSM/least privilege/defence-in-depth 应用于医疗报告；题摘给出垂直实证，没有新增可迁移的 agent security state/authority contract。 | Daily 候选与证据项；Books 当前无采用。 |
| 06-30 / `29030` | AGENT-MEMORY | 在 MCQ agent 中插入错误 memory 并测 accuracy/ASR，只复现“memory 可污染输出”；没有 memory admission/provenance/repair 或新的评估控制契约。 | Daily 候选与证据项；Books 当前无采用。 |
| 06-30 / `29775` | PLATFORM-GPU-SCHEDULER | 摘要明确目标是 MIG 上的 smaller ML models；MF-MARL repartition + heuristic scheduling 是通用 GPU job scheduler，不是大模型基础设施特有贡献。 | Daily 候选与证据项；Books 当前无采用。 |

注意：`28434` 保留为 Candidate/Existing，不因其使用 Memory-aware GRPO 自动准入，而是因为它同时给出 runtime-visible 的 proactive/on-demand memory tool 与基于 trajectory state/context budget 的控制边界；其训练 recipe 本身不写入 Books。

## 7. 报告重开与最终 Gate

- **可通过本轮 Candidate/Books gate：06-23、06-24。** 原 `整合：` 中只有 11/1 项是 source-specific Actual Body，其余分别按上表降为 Existing Coverage；没有正文缺口。
- **必须重开：06-25。** 撤销 `25082/25285/25608`，修复 strict JSON 的 `24934/25453` 状态与 reason 错位，再重算 candidate/Books 统计。
- **必须重开：06-26。** 撤销 `27005` 并重算统计。
- **必须重开：06-29。** 撤销 `27558/27841/27997`；同时撤销 `27841` 的 Books binding/note，再重算统计。
- **必须重开：06-30。** 六项 current Integrate 的正文与写后语义验收均 PASS；仍需把 `28666/29030/29775` 降回候选前关闭并重算 57 的 denominator。`28379` 保持 Existing Coverage。

最终结论是：Books 当前没有遗留 Body Writeback Required；未闭环项全部位于 current Daily admission/authority 与三条旧 Books 采用链的撤销，而不是继续向 Books 增写段落。
