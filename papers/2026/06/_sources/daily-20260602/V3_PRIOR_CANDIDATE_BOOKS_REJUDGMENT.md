# 2026-06-02 旧前沿 44 项当前 V3 Books 重判

## Authority 与复用边界

本记录只覆盖当前 `V3_SCREENING_LEDGER.md` 保留的 44 个旧前沿 Candidate。论文 identity、exact-v1 Method、Evaluation、Limitations 与 artifact non-proof 复用 `V2_1_EVIDENCE_ARCHIVE.md` 的可定位证据；准入与 Books disposition 均重新判断，不继承旧 `Complete`、`Integrate` 或 `No Change` 标签。旧 trace 只用于发现待核验位置，不能授权当前 V3 Candidate，也不能证明章节正文已经吸收。

逐项重读当前 Stable Knowledge Node 正文并完成全部 owner 写回后，44 项分为 13 项 `Integrate` 已写入正文与 31 项 `Existing`；没有 `Only report`、`Structural Candidate`、`Deferred`、exact-v1 access blocker 或未决 proposal。

## Integrate 已写入（13）

| arXiv exact-v1 | Stable Knowledge Node | Review notes 前正文锚点 |
| --- | --- | --- |
| `2606.01091v1` | `TRAIN-GRPO` | “Evidence-derived Rubric 是版本化 Reward State” |
| `2606.01155v1` | `TRAIN-PRETRAINING` | “数据受限的 Scaling 必须把 Unique Data 与 Repetition 分账” |
| `2606.01680v1` | `TRAIN-DISTRIBUTED-TRAINING` | “退化链路仍在线时，Collective 需要 Bandwidth-state Schedule” |
| `2606.02218v1` | `TRAIN-GRPO` | “同步 Group Size 也可以由 Straggler Risk 有界调节” |
| `2606.00947v1` | `PLATFORM-EVALUATION-SYSTEM` | “Federated Personalization 的盲区是可见性合同” |
| `2606.01725v1` | `INFER-SCHEDULING` | “Task-DAG Simulator 只能校准 Capacity Plan，不能承诺线上 SLO” |
| `2606.01751v1` | `INFER-KV-CACHE` | “非 Prefix 复用必须绑定 Position-aligned Segment 与 Correction State” |
| `2606.01839v1` | `INFER-SCHEDULING` | “Conversation Placement 用已观察状态替代逐 Turn 预测” |
| `2606.01850v1` | `PLATFORM-EVALUATION-SYSTEM` | “Compression Release 必须同时验收 Accuracy 与 Calibrated Uncertainty” |
| `2606.01927v1` | `INFER-REQUEST-LIFECYCLE` | “并行扩展必须先移出不可扩展的 Host Critical Path” |
| `2606.02060v1` | `PLATFORM-EVALUATION-SYSTEM` | “Trajectory Error 需要 Span、Commitment 与 Claim Propagation 三层坐标” |
| `2606.02091v1` | `INFER-SPECULATIVE-DECODING` | “Draft Capacity 可以借用 Target Feature，但不能借走 Commit Authority” |
| `2606.02430v1` | `PLATFORM-EVALUATION-SYSTEM` | “数值 Fault 要沿 Layer、Operation、Token 与 Task 观察传播” |

## Runtime owner 最终复判（10）

| arXiv exact-v1 | Stable Knowledge Node | 最终 disposition 与正文锚点 |
| --- | --- | --- |
| `2606.00947v1` | `PLATFORM-EVALUATION-SYSTEM` | `Integrate`；“Federated Personalization 的盲区是可见性合同” |
| `2606.01725v1` | `INFER-SCHEDULING` | `Integrate`；“Task-DAG Simulator 只能校准 Capacity Plan，不能承诺线上 SLO” |
| `2606.01751v1` | `INFER-KV-CACHE` | `Integrate`；“非 Prefix 复用必须绑定 Position-aligned Segment 与 Correction State” |
| `2606.01839v1` | `INFER-SCHEDULING` | `Integrate`；“Conversation Placement 用已观察状态替代逐 Turn 预测” |
| `2606.01850v1` | `PLATFORM-EVALUATION-SYSTEM` | `Integrate`；“Compression Release 必须同时验收 Accuracy 与 Calibrated Uncertainty” |
| `2606.01927v1` | `INFER-REQUEST-LIFECYCLE` | `Integrate`；“并行扩展必须先移出不可扩展的 Host Critical Path” |
| `2606.02060v1` | `PLATFORM-EVALUATION-SYSTEM` | `Integrate`；“Trajectory Error 需要 Span、Commitment 与 Claim Propagation 三层坐标” |
| `2606.02091v1` | `INFER-SPECULATIVE-DECODING` | `Integrate`；“Draft Capacity 可以借用 Target Feature，但不能借走 Commit Authority” |
| `2606.02430v1` | `PLATFORM-EVALUATION-SYSTEM` | `Integrate`；“数值 Fault 要沿 Layer、Operation、Token 与 Task 观察传播” |
| `2606.02540v1` | `PLATFORM-SECURITY` | `Existing`；“Harness Backdoor 把单次写入变成跨 Run 控制状态”已覆盖跨 session reuse、revision/provenance/revoke、sandbox 与 rollback。 |

三条存续 trace 日期（`00947`、`01091`、`01155`）已修正；已撤回的 `2606.00997v1` 不在 44 项内，整条 adoption chain 已删除。

## Existing（31）

| Stable Knowledge Node | 已覆盖的候选与当前正文机制锚点 |
| --- | --- |
| `INFER-SCHEDULING` | `00946`：在线路由输入、workload/反馈更新与 recalibration fallback；`01007`：MoE workload identity、placement/routing/scheduling 协同。 |
| `AGENT-MULTI-AGENT` | `00953`：dependency graph、coordination tax 与 merge verification。 |
| `INFER-SPECULATIVE-DECODING` | `01019`：exact/lossy verification 分界与 target commit。 |
| `PLATFORM-EVALUATION-SYSTEM` | `01034`：judge calibration、abstain/disagreement；`01066`：generated evaluator admission、fuzz 与 meta-evaluation；`01317`：stateful workspace 的 outcome/effect 验收；`01462`：release identity、model/benchmark/harness/environment；`01365`：Agent/step trace 与 wasted-compute 定位。 |
| `INFER-KV-CACHE` | `01065`：cache lifecycle directive/identity；`01387`：claim identity、materialization predicate 与 fail-closed lowering。 |
| `AGENT-MEMORY` | `01138`：versioned memory read/write provenance；`01435`：evidence 与 policy、freshness/conflict 分离。 |
| `AGENT-PLATFORM` | `01139`、`01311`、`01314`：skill candidate、validation、promotion/revision lifecycle；`01416`：detect/isolate/recover/fallback；`01508`：Agent resource/control boundary；`01770`：正文“Harness Controller 是版本化策略，不是模型的隐式习惯”“自适应 Harness 只能提交保持成功约束的干预”及章节小结已覆盖 open-ended stream、history、routing、bounded adaptation、release authority 与静态 fallback。 |
| `TRAIN-GRPO` | `01143`：rollout prefix reuse 与 cache identity。 |
| `PLATFORM-SECURITY` | `01196`：safety action/outcome evidence；`01212`：RAG provenance/dataflow/poisoning；`01413`：DP data lifecycle/source/output boundary；`01494`：signal disagreement/adjudication；`01567`：skill admission/provenance/sandbox；`02302`：spec-driven security task 与 effect verification；`02483`：proposal/authorization/issue/execution 分权及 issue-time privacy。 |
| `INFER-PD-DISAGGREGATION` | `01502`：query/cache/fabric 三者共同决定跨实例控制。 |
| `AGENT-CONTEXT` | `02373`：外置 context/search state 与 environment ownership。 |
| `PLATFORM-MODEL-REGISTRY` | `02437`：adapter registry state、存储与 serving identity。 |

## 计数与 Gate

- 旧前沿：44/44 已有 exact-v1 Evidence 与当前 Books comparison。
- Books disposition：13 `Integrate` 已写入 + 31 `Existing` = 44。
- exact-v1 access blocker：0。
- 报告级剩余：0；非作者已按正文而非 trace 完成 post-write audit。
