# 2026-06-03 V3 Books Post-write Audit Scope

## 当前写回

| Source Family | Owner | 当前决定 | 正文锚点 |
| --- | --- | --- | --- |
| `SF-CORRECT-SET-TURNOVER-RLVR` | `TRAIN-GRPO` | Integrated | “Mastered Set 需要 Acquisition–Retention Turnover Ledger” |
| `SF-FEDERATEDSKILL` | `AGENT-PLATFORM` | Integrated | “跨用户演进时，这一边界还要求把 private episode 与 shared skill revision 分开” |
| `SF-ARBOR-REUSABLE-RUBRIC-BUFFER` | `TRAIN-GRPO` | Integrated | “Rubric Pool 还需要 Admission、Consolidation 与 Retirement” |
| `SF-Q0-HYPER-EPOCH-PRETRAINING` | `TRAIN-PRETRAINING` | Integrated | “超多 Epoch 训练会把单一 Checkpoint 演进为模型群体状态” |
| `SF-DECA-DECENTRALIZED-FPFT` | `TRAIN-DISTRIBUTED-TRAINING` | Integrated | “去中心化全参数微调必须显式切分 Optimizer Ownership” |
| `SF-AGENT-LIBOS` | `AGENT-PLATFORM` | Integrated | “快速演进的 Skill / Tool Layer 不能拥有 Primitive Effect Authority” |
| `SF-ASYMPO` | `TRAIN-GRPO` | No Change — Existing Coverage | “正负 Advantage 不必共享同一 Clipping Contract”“Asynchronous RL 必须把 Policy Staleness 写进 Advantage” |
| `SF-LIBRA-AGENTIC-RL` | `TRAIN-DISTRIBUTED-TRAINING` | No Change — Existing Coverage | “RL Phase 资源可以成为弹性函数，但训练语义不能随实例伸缩”“Agent RL 从 Trainer 中心演进为版本化 Dataflow” |
| `SF-MULTILINGUAL-UNLEARNING` | `PLATFORM-SECURITY` | Integrated | “Unlearning Release 要测试跨语言迁移、可逆性与未知 Trigger Family” |
| `SF-ROGUEMERGE` | `PLATFORM-SECURITY` | Integrated | “Model Merge Input 是对权重的 Supply-chain Write Access” |
| `SF-MODEL-MERGE-ROUTER-CALIBRATION` | `PLATFORM-MODEL-REGISTRY` | Integrated | “MoE Merge 的发布身份还要包含 Router Calibration” |
| `SF-ADAPTIVE-LLM-ATTACK-BASELINE` | `PLATFORM-EVALUATION-SYSTEM` | Integrated | “Attack Success Rate 不能压平 Attack Profile” |
| `SF-BACKDOOR-UNLEARNING-GENERALIZATION` | `PLATFORM-SECURITY` | Integrated | “Unlearning Release 要测试跨语言迁移、可逆性与未知 Trigger Family” |
| `SF-CONSENT-INTEGRITY` | `PLATFORM-SECURITY` | Integrated | “Approval Summary 必须由待执行 Effect 反向渲染” |
| `SF-DRIFTSCHED-TOKEN-DRIFT` | `INFER-SCHEDULING` | Integrated | “Token Drift 改变剩余工作时，要重算队列承诺” |
| `SF-CONTAMINATION-AUDIT-RELIABILITY` | `PLATFORM-EVALUATION-SYSTEM` | Integrated | “Contamination Detector 必须随 Scale 与 Distribution 重新校准” |
| `SF-AI-MODEL-EXTRACTION-ATTACKS-BYPASSING-SINGLE-CLIENT-ASSUMPTIONS` | `PLATFORM-SECURITY` | Integrated | “Extraction Budget 必须跨身份聚合” |
| `SF-NETKV` | `INFER-SCHEDULING` | Integrated | “Network Cost Oracle 只提交 Placement Score” |
| `SF-KVARN` | `INFER-KV-CACHE` | No Change — Existing Coverage | “Quantization Objective 应对齐 Attention Distortion”中的 repeated state feedback |
| `SF-JUDGE-SUBSPACE-ALIGNMENT` | `PLATFORM-EVALUATION-SYSTEM` | No Change — Existing Coverage | “Judge Agreement 不是单一数字” |
| `SF-OVERLAYING-GOVERNANCE-COMPOSITIONAL-AUTHORIZATION-FRAMEWORK-DELEGATION-S` | `PLATFORM-SECURITY` | No Change — Existing Coverage | “多跳 Delegation 必须保留 Human Principal” |

## 作者侧结构检查

- 六个新增 binding 均唯一，且第一次出现都位于所属章节顶层 `## Review notes` 之前。
- 新增正文均保留旧方案成立条件、约束变化、状态或控制所有权、代价、failure 与 fallback。
- ASymPO 与 Libra 以当前命题级正文改判 Existing，没有重复追加论文段落。
- Inference / Platform 的 10 项真实增量均在 owner 章节形成连贯正文；KVarN、Judge Subspace 与 Overlay Governance 由现有命题级正文完整覆盖，没有为制造 diff 重复追加。

## 闭合状态

无。

全 87 项最终为 70 Existing / 16 Integrated / 1 Only report；proposal=0、Deferred=0、exact-v1 blocker=0。独立 fresh-context 检查已核对正文锚点、证据边界、Review notes 位置与相邻 handoff，最终报告结构、集合一致性与工作树范围检查通过。
