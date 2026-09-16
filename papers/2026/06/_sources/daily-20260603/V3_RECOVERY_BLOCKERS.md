# 2026-06-03 V3 恢复阻塞与 Books 队列

## 分母

- 可读 raw packet：719 identities。
- 可读 semantic checkpoint：44 prior candidates + 675 closure proposals；这是恢复时的初始 pending 状态，现已全部重判闭合。
- 旧顶部冲突声明：747 identities、55 retained、691 closures、1 supporting version；支撑这些数字的 V9 denominator/evidence/Books/independent 文件均为 0 字节。
- 当前已从 719-row packet 冻结 87 Candidate / 632 Close：旧 44 项为 39/5，旧 675 closure 为 48/627；不得凭旧 55 反推成员。逐项结果见 `V3_SCREENING_LEDGER.md`。

## Books trace-to-body

| Source Family | Target file | Trace anchor | 当前状态 |
| --- | --- | --- | --- |
| `SF-CONSENT-INTEGRITY` | `books/part-06-ai-infrastructure/72-security.md` | “Approval Summary 必须由待执行 Effect 反向渲染” | Integrated；trace Daily 已修正为 06-03 |
| `SF-ECHELON-AGGREGATE-ONLY-ADAPTATION` | `books/part-04-training-system/36-distributed-training.md` | `daily-books-trace:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION` | body-existing：`semantic-body-binding:SF-ECHELON-AGGREGATE-ONLY-ADAPTATION`；trace Daily 已修正为 06-03 |
| `SF-DRIFTSCHED-TOKEN-DRIFT` | `books/part-05-inference-system/56-inference-scheduling.md` | “Token Drift 改变剩余工作时，要重算队列承诺” | Integrated；trace Daily 已修正为 06-03 |
| `SF-FOLD-ONLINE-DEDUP` | `books/part-04-training-system/27-data.md` | `daily-books-trace:SF-FOLD-ONLINE-DEDUP` | body-existing：`semantic-body-binding:SF-FOLD-ONLINE-DEDUP` |
| `SF-DELIBERATION-EVIDENCE-ATTRITION` | `books/part-07-agent/82-multi-agent.md` | `daily-books-trace:SF-DELIBERATION-EVIDENCE-ATTRITION` | body-existing：`semantic-body-binding:SF-DELIBERATION-EVIDENCE-ATTRITION` |
| `SF-JUDGE-SUBSPACE-ALIGNMENT` | `books/part-06-ai-infrastructure/66-evaluation-system.md` | “Judge Agreement 不是单一数字” | Existing；agreement/subspace 只作 diagnostic signal，judge 不取得 truth authority |
| `SF-ASYMPO` | `books/part-04-training-system/33-grpo.md` | “正负 Advantage 不必共享同一 Clipping Contract” | Existing；current-policy positive/negative scale 分支、staleness 与对称 clipping fallback 已有命题级正文 |
| `SF-LIBRA-AGENTIC-RL` | `books/part-04-training-system/36-distributed-training.md` | “RL Phase 资源可以成为弹性函数，但训练语义不能随实例伸缩”“Agent RL 从 Trainer 中心演进为版本化 Dataflow” | Existing；rollout/learner owner、heterogeneous phase pool、long-tail tool wait 与固定池 fallback 已覆盖 |
| `SF-DECA-DECENTRALIZED-FPFT` | `books/part-04-training-system/36-distributed-training.md` | “去中心化全参数微调必须显式切分 Optimizer Ownership” | Integrated；正文位于顶层 Review notes 前 |
| `SF-CONTAMINATION-AUDIT-RELIABILITY` | `books/part-06-ai-infrastructure/66-evaluation-system.md` | “Contamination Detector 必须随 Scale 与 Distribution 重新校准” | Integrated；FP/FN calibration、Unknown 与 release authority 已闭合 |
| `SF-AI-MODEL-EXTRACTION-ATTACKS-BYPASSING-SINGLE-CLIENT-ASSUMPTIONS` | `books/part-06-ai-infrastructure/72-security.md` | “Extraction Budget 必须跨身份聚合” | Integrated；global budget/correlation 与 Sybil failure 已闭合 |
| `SF-OVERLAYING-GOVERNANCE-COMPOSITIONAL-AUTHORIZATION-FRAMEWORK-DELEGATION-S` | `books/part-06-ai-infrastructure/72-security.md` | “多跳 Delegation 必须保留 Human Principal” | Existing；compositional chain、least authority、revoke/replay 与 fail closed 已覆盖 |
| `SF-AGENT-LIBOS` | `books/part-07-agent/84-agent-platform.md` | “快速演进的 Skill / Tool Layer 不能拥有 Primitive Effect Authority” | Integrated；正文位于顶层 Review notes 前 |
| `SF-NETKV` | `books/part-05-inference-system/56-inference-scheduling.md` | “Network Cost Oracle 只提交 Placement Score” | Integrated；KV placement/transfer、TTFT/SLO arbitration 与 recompute fallback 已闭合 |

当前 prior 队列为 32 项 Existing 与 7 项已写入正文；恢复候选为 38 项 Existing、9 项已写入正文与 1 项 Only report。Inference / Platform proposal 已清零，exact-v1 blocker=0。
