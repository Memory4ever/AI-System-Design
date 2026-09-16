# 2026-06-03 prior Candidate current Books rejudgment

本记录只覆盖严格题摘重审后存续的 39 个 prior Candidate。候选身份、exact-v1 Method/Evaluation/Limitations 与 claim boundary 复用 `V2_1_EVIDENCE_ARCHIVE.md` 的逐项 Review Completion Receipt；旧 `Integrate` / `No Change` 标签不作为当前结论。本轮重新读取 current owner 正文，并以正文机制是否真实存在作 Books Decision。

## Current rejudgment

| Source Family | Primary | Stable Node | 当前判定 | Current body comparison |
| --- | --- | --- | --- | --- |
| `SF-RAG-INFERENCE-COST-ATTACK` | `2606.02643v1` | `PLATFORM-SECURITY` | Existing | Security 已将 token/tool/retry/concurrency budget 放在外部 state machine，并覆盖 retrieval/context resource abuse；模型或攻击 detector 不拥有放行权。 |
| `SF-RINGELMANN-MAS` | `2606.02646v1` | `AGENT-MULTI-AGENT` | Existing | Multi-Agent 已要求先测 single-Agent baseline、coordination tax、边际信息价值与 equal-budget Pareto admission；nominal agent count 不是有效扩展量。 |
| `SF-CONSENT-INTEGRITY` | `2606.02668v1` | `PLATFORM-SECURITY` | Integrated | 正文锚点“Approval Summary 必须由待执行 Effect 反向渲染”已写入顶层 Review notes 之前，覆盖 mediator、approval 与 execution/effect receipt 分权。 |
| `SF-ECHELON-AGGREGATE-ONLY-ADAPTATION` | `2606.02958v1` | `TRAIN-DISTRIBUTED-TRAINING` | Existing | 正文存在 `semantic-body-binding:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION`，已写 aggregate-only、non-export state 与 fallback；仅 trace 日期需修正。 |
| `SF-GATEAI-OPERATING-POINT-EVAL` | `2606.02959v1` | `PLATFORM-EVALUATION-SYSTEM` | Existing | Evaluation 已把 threshold、operating point、FP/FN、slice 与 release policy 共同版本化，单一 aggregate safety score 不拥有发布权。 |
| `SF-KFORGE-CROSS-PLATFORM-KERNEL` | `2606.02963v1` | `INFER-TENSORRT-LLM` | Existing | TensorRT-LLM owner 已分离 kernel proposal、backend compilation、numerical correctness、hardware/profile 与 fallback，跨平台生成不接管 runtime truth。 |
| `SF-ASYMCACHE-MULTI-SEGMENT` | `2606.02964v1` | `INFER-KV-CACHE` | Existing | KV owner 已有 segment/page identity、position/role、eviction/reconstruction、physical layout 与 FullKV fallback。 |
| `SF-DRIFTSCHED-TOKEN-DRIFT` | `2606.02982v1` | `INFER-SCHEDULING` | Integrated | 正文锚点“Token Drift 改变剩余工作时，要重算队列承诺”已写入顶层 Review notes 之前，覆盖 estimate/observed reconciliation 与 SJF/aging fallback。 |
| `SF-FOLD-ONLINE-DEDUP` | `2606.03001v1` | `TRAIN-DATA` | Existing | 正文存在 `semantic-body-binding:SF-FOLD-ONLINE-DEDUP`，已写增量索引、bitmap/Jaccard identity、online admission 与证据边界。 |
| `SF-SAE-QUANT-FIDELITY` | `2606.03002v1` | `PLATFORM-EVALUATION-SYSTEM` | Existing | Evaluation 已要求 compression/quantization release 分离 perplexity、feature/claim transition、calibration slice、runtime artifact 与 rollback。 |
| `SF-MUSE-AGENTIC-HARNESS` | `2606.03005v1` | `AGENT-PLATFORM` | Existing | Agent Platform 已将 harness、tool/MCP、parser、environment、terminal evidence 与 deterministic verifier 作为 run identity。 |
| `SF-MOSAIC-MOA-SCHEDULING` | `2606.03014v1` | `INFER-SCHEDULING` | Existing | Scheduling 已按 request/workload、routing skew、generation variance、batch/concurrency、tail SLO 与 fallback 管理多模型/多 Agent 服务。 |
| `SF-SKILLGUARD` | `2606.03024v1` | `PLATFORM-SECURITY` | Existing | Security 已将 skill/source/revision 作为 principal，权限、effect policy、sandbox、revoke 与 runtime receipt 分权。 |
| `SF-DELIBERATION-EVIDENCE-ATTRITION` | `2606.03032v1` | `AGENT-MULTI-AGENT` | Existing | 正文存在 `semantic-body-binding:SF-DELIBERATION-EVIDENCE-ATTRITION`，已把 deliberation 建模为 evidence-flow，并以事实保留率而非共识验收。 |
| `SF-AGENT-CAPABILITY-TRUST-LAYER` | `2606.03034v1` | `AGENT-MCP` | Existing | MCP 已有 server/agent identity、capability advertisement、provenance/freshness、discovery authorization 与 executable verification。 |
| `SF-JUDGE-SUBSPACE-ALIGNMENT` | `2606.03043v1` | `PLATFORM-EVALUATION-SYSTEM` | Existing | 命题锚点“Judge Agreement 不是单一数字”已将 agreement 限定为 measurement signal，要求完整 run identity、分布与复核，明确 judge 不取得 truth authority；subspace 是该诊断边界的实现实例。 |
| `SF-TOOLGATE-PRECALL-CONTROL` | `2606.03054v1` | `AGENT-TOOL-CALLING` | Existing | Tool Calling 已分离 proposal、issue、execute、effect receipt 与 abstain/clarification；pre-call sensor 不取得 execution authority。 |
| `SF-SKILLDAG-TYPED-SKILL-STATE` | `2606.03056v1` | `AGENT-PLATFORM` | Existing | Agent Platform 已有 typed skill dependency/conflict、permission、executable-set validation、promotion/version/revoke。 |
| `SF-ASYMPO` | `2606.03070v1` | `TRAIN-GRPO` | Existing | 正文锚点“正负 Advantage 不必共享同一 Clipping Contract”已经覆盖 current-policy self-anchored positive branch、behavior-bounded negative branch、stale-rollout 风险与标准对称 clipping fallback；相邻“ Asynchronous RL 必须把 Policy Staleness 写进 Advantage”保留 policy identity。 |
| `SF-LIBRA-AGENTIC-RL` | `2606.03077v1` | `TRAIN-DISTRIBUTED-TRAINING` | Existing | 正文锚点“RL Phase 资源可以成为弹性函数，但训练语义不能随实例伸缩”“Agent RL 从 Trainer 中心演进为版本化 Dataflow”与 long-tail rollout scheduler 已覆盖 rollout/learner owner、异构资源、tool wait、phase reallocation、policy identity 与固定池 fallback。 |
| `SF-EVOTRAINER-HARNESS` | `2606.03108v1` | `TRAIN-GRPO` | Existing | GRPO 已要求 policy、harness、environment、reward/verifier 与 checkpoint 共同版本化，并由 held-out backtest/release gate 约束共同演进。 |
| `SF-SPOQ-ORCHESTRATED-QUEUE` | `2606.03115v1` | `AGENT-WORKFLOW` | Existing | Workflow 已覆盖 dependency waves、specialist ownership、pre/post validation、handoff evidence、human approval 与 rollback。 |
| `SF-AGENTIC-QUERY-OPT` | `2606.03152v1` | `AGENT-WORKFLOW` | Existing | Workflow 已把 plan/execution 交织、tool/query cost、quality evidence、budget/stop 与 terminal outcome 纳入同一 run contract。 |
| `SF-OAN-TRUST-INFRA` | `2606.03161v1` | `AGENT-MCP` | Existing | MCP 已有互联前 identity、capability provenance、freshness、governance、authorization、revocation 与 effect verification。 |
| `SF-DECA-DECENTRALIZED-FPFT` | `2606.03209v1` | `TRAIN-DISTRIBUTED-TRAINING` | Integrated | 正文锚点“去中心化全参数微调必须显式切分 Optimizer Ownership”已写入顶层 Review notes 之前，覆盖 block owner、round/base identity、non-IID/拓扑 failure 与 centralized/PEFT fallback。 |
| `SF-CONTAMINATION-AUDIT-RELIABILITY` | `2606.03305v1` | `PLATFORM-EVALUATION-SYSTEM` | Integrated | 正文锚点“Contamination Detector 必须随 Scale 与 Distribution 重新校准”已写入顶层 Review notes 之前，覆盖 FP/FN calibration、Unknown 与 non-release-authority。 |
| `SF-PROMPT-HARDENING-LIMITS` | `2606.03308v1` | `PLATFORM-SECURITY` | Existing | Security 已把 prompt filter 视作 detector，保留 policy/tool mediation、pass-only blind spot、attack mutation 与 fail-closed fallback。 |
| `SF-IMPLEMENT-KUBERNETES-POD-LEVEL-REMOTE-ATTESTATION-CONFIDENTIAL` | `2606.03323v1` | `PLATFORM-SECURITY` | Existing | Security 的 hardware-attestation 分支已要求 workload/pod/image/config/dispatch binding 与 adversary tier，而非只证明 Guest OS。 |
| `SF-AI-MODEL-EXTRACTION-ATTACKS-BYPASSING-SINGLE-CLIENT-ASSUMPTIONS` | `2606.03381v1` | `PLATFORM-SECURITY` | Integrated | 正文锚点“Extraction Budget 必须跨身份聚合”已写入顶层 Review notes 之前，覆盖 global budget/correlation、Sybil failure 与保守 fallback。 |
| `SF-PIPEDREAM-THEORY` | `2606.03498v1` | `TRAIN-PIPELINE-PARALLEL` | Existing | Pipeline Parallel 已覆盖 stale weight/version、microbatch schedule、bubble/throughput、correctness boundary 与同步 fallback；理论结果不改 owner。 |
| `SF-OVERLAYING-GOVERNANCE-COMPOSITIONAL-AUTHORIZATION-FRAMEWORK-DELEGATION-S` | `2606.03518v1` | `PLATFORM-SECURITY` | Existing | 命题锚点“多跳 Delegation 必须保留 Human Principal”已覆盖 append-only principal/delegate/scope/parent/expiration chain、least authority、revoke/replay 与 fail-closed fallback；无需按论文重复正文。 |
| `SF-COEVAL-RANKING-LANGUAGE-MODELS-CUSTOM-TASKS-WITHOUT` | `2606.03650v1` | `PLATFORM-EVALUATION-SYSTEM` | Existing | Evaluation 已分离 unlabeled benchmark、judge/model roles、cross-evaluation、uncertainty 与 independent release authority。 |
| `SF-VLA-DEPLOYMENT-SAFETY` | `2606.03724v1` | `MULTIMODAL-EMBODIED-VLA` | Existing | VLA 已要求 checkpoint 与 unnormalizer、controller、observation/action convention、runtime revision、safety envelope 和 physical outcome 共同发布。 |
| `SF-E2LLM-EDGE-SERVING` | `2606.03770v1` | `INFER-SCHEDULING` | Existing | Scheduling 已把 heterogeneous accelerator/memory/network、model split/placement、request class 与 tail SLO 放入控制面。 |
| `SF-AI-AGENTS-ENABLE-ADAPTIVE-COMPUTER-WORMS` | `2606.03811v1` | `PLATFORM-SECURITY` | Existing | Security 已覆盖 Agent-driven reconnaissance、adaptive exploit proposal、tool/effect mediation、credential/network boundary 与 deterministic containment。 |
| `SF-TREEFLASH` | `2606.03819v1` | `INFER-SPECULATIVE-DECODING` | Existing | Speculative Decoding 已覆盖 parallel block/tree proposal、target exact verification、branch/KV rollback、tree shape 与 goodput admission。 |
| `SF-REAL-AGENT-BENCHMARK` | `2606.03889v1` | `PLATFORM-EVALUATION-SYSTEM` | Existing | Evaluation 已要求真实 session 的 model×harness×environment×scorer identity、state reconstruction、trajectory receipt 与 terminal verifier。 |
| `SF-AGENT-LIBOS` | `2606.03895v1` | `AGENT-PLATFORM` | Integrated | 正文锚点“快速演进的 Skill / Tool Layer 不能拥有 Primitive Effect Authority”已写入顶层 Review notes 之前，覆盖 operation proposal、typed primitive、capability/resource/information-flow enforcement、effect receipt 与 read-only/reject fallback。 |
| `SF-NETKV` | `2606.03910v1` | `INFER-SCHEDULING` | Integrated | 正文锚点“Network Cost Oracle 只提交 Placement Score”已写入顶层 Review notes 之前，覆盖 KV residency/transfer、decode selection、TTFT slack 与 recompute fallback。 |

## Result and separated queues

- Current disposition：32 `Existing`，7 `Integrated`，0 `Only report`，0 `Deferred`；exact-v1 blocker=0。
- 正文补写队列：无。五项真实增量已写入 owner 正文；Judge Subspace 与 Overlay Governance 经 fresh-context 顺读改判 Existing。
- 仅日期修正队列（2）：`SF-CONSENT-INTEGRITY` 的 trace Daily `2026-06-02 → 2026-06-03`；`SF-ECHELON-AGGREGATE-ONLY-ADAPTATION` 同样修正。
- 已有正文核验（5）：除 `SF-ECHELON-AGGREGATE-ONLY-ADAPTATION`、`SF-FOLD-ONLINE-DEDUP`、`SF-DELIBERATION-EVIDENCE-ATTRITION` 外，`SF-ASYMPO` 与 `SF-LIBRA-AGENTIC-RL` 也已有命题级机制覆盖，均判 Existing。实际写入（2）：`SF-DECA-DECENTRALIZED-FPFT`、`SF-AGENT-LIBOS`。
