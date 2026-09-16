# 2026-06-08 V3 recovery blockers

> **2026-09-11 final report-side checkpoint：** 非作者 fresh audit 已冻结 `498 = 48 Candidate + 450 Close`；Evidence、Books proposal 均为 `48/48`，exact-v1 blocker 为 0。最终 disposition 为 45 项 `已有覆盖`、3 项 `仅报告`、0 项 `整合`。本文件只记录共享 Books 当前快照的 post-write/trace reconciliation；旧 trace 或 Review notes 不参与 V3 准入或正文授权。

## Denominator 与撤销链

作者侧 `50 / 448` 仅保留为审计历史。非作者复核关闭 2606.06818、2606.07017、2606.07119、2606.07190、2606.07412，并恢复 2606.06915、2606.06991、2606.07054，最终冻结为 48 / 450。

root 已移除 2606.06818、2606.07067、2606.07470 的正文或 trace adoption chain。当前 Books 全树检索不到这三个 ID；没有待补正文，也没有残留采用链需要继续清除。

## Existing Coverage 的当前正文锚点

以下十项均由 Review notes 前已存在的正文机制承载；章末 trace 只需校正 Daily 日期，不能反向授权正文：

- `2606.06521` / `SF-P-CAST-PRECISION-FP8-ATTENTION-SINK-INDUCED` → `books/part-05-inference-system/49-tensorrt-llm.md`：约 L55–70 的 `phase/shape → plan revision → safe fallback` 身份合同，以及约 L628–642 的“量化验收不能只看平均分：逐例一致性与分布漂移”。
- `2606.06523` / `SF-LEAN4AGENT` → `books/part-07-agent/81-workflow.md`：约 L96–128 的 state alignment、Deterministic Spine、平台验证与恢复边界，以及约 L192–221 的 workflow-level admission、authority 与 outcome verification。
- `2606.06697` / `SF-2026-ARXIV-2606-06697` → `books/part-06-ai-infrastructure/72-security.md`：约 L1528–1532 的 accelerator-driver buffer/address/permission/command provenance 合同，以及约 L1730–1746 的 OS 级 effect boundary 与 proposal/authorization/execution/rollback 分权。
- `2606.07131` / `SF-2026-ARXIV-2606-07131` → `books/part-06-ai-infrastructure/72-security.md`：约 L1076–1109 的 Skill side-effect ground truth、sandbox receipt、持久 carrier lifecycle、版本化 diff 与 rollback。
- `2606.07150` / `SF-2026-ARXIV-2606-07150` → `books/part-06-ai-infrastructure/72-security.md`：约 L313–352 的 authority registry、跨 channel provenance/influence graph，以及约 L396–400 的 effect-stage trace contract。
- `2606.06888` / `SF-2026-ARXIV-2606-06888` → `books/part-04-training-system/28-pretraining.md`：约 L903–906 的 exact `semantic-body-binding`，覆盖数据受限重复消费、masked-input regularization 与适用规模边界。
- `2606.06924` / `SF-2026-ARXIV-2606-06924` → `books/part-05-inference-system/56-inference-scheduling.md`：约 L675–697 的 calibration identity、候选实现域、model/quantization/placement admission 分权，以及约 L907–960 的 value/cost/SLO admission、capability profile 与保守强模型 fallback。
- `2606.07019` / `SF-2026-ARXIV-2606-07019` → `books/part-04-training-system/36-distributed-training.md`：约 L177–189 的“从静态通信配置到受验证的 Collective Policy”，含 versioned policy、verifier/ABI、completion receipt 与静态 NCCL fallback。
- `2606.07379` / `SF-2026-ARXIV-2606-07379` → `books/part-06-ai-infrastructure/66-evaluation-system.md`：约 L1707–1778 的 trajectory evidence、environment transition、task-specific completion 与 deterministic verifier 分层。
- `2606.07462` / `SF-2026-ARXIV-2606-07462` → `books/part-06-ai-infrastructure/66-evaluation-system.md`：约 L1124–1142 的 reference-artifact-first admission，以及约 L1786–1823 的 artifact/process/environment evolution 与 research-agent run identity。

## 仅日期修复的 trace 队列

当前共享 Books 快照中共十条存续 trace，均应把 `Daily` 改为 `2026-06-08`；不改正文，不新增 adoption chain：

| Source family | 当前 Daily | 文件与 trace 锚点 |
| --- | --- | --- |
| `SF-P-CAST-PRECISION-FP8-ATTENTION-SINK-INDUCED` | 2026-06-03 | `books/part-05-inference-system/49-tensorrt-llm.md`，约 L1658–1662 |
| `SF-LEAN4AGENT` | 2026-06-03 | `books/part-07-agent/81-workflow.md`，约 L1120–1124 |
| `SF-2026-ARXIV-2606-06697` | 2026-06-05 | `books/part-06-ai-infrastructure/72-security.md`，约 L2243–2247 |
| `SF-2026-ARXIV-2606-06888` | 2026-06-06 | `books/part-04-training-system/28-pretraining.md`，约 L1178–1182 |
| `SF-2026-ARXIV-2606-06924` | 2026-06-06 | `books/part-05-inference-system/56-inference-scheduling.md`，约 L1312–1316 |
| `SF-2026-ARXIV-2606-07019` | 2026-06-06 | `books/part-04-training-system/36-distributed-training.md`，约 L1550–1554 |
| `SF-2026-ARXIV-2606-07131` | 2026-06-06 | `books/part-06-ai-infrastructure/72-security.md`，约 L2249–2253 |
| `SF-2026-ARXIV-2606-07150` | 2026-06-06 | `books/part-06-ai-infrastructure/72-security.md`，约 L2255–2259 |
| `SF-2026-ARXIV-2606-07379` | 2026-06-06 | `books/part-06-ai-infrastructure/66-evaluation-system.md`，约 L3325–3329 |
| `SF-2026-ARXIV-2606-07462` | 2026-06-06 | `books/part-06-ai-infrastructure/66-evaluation-system.md`，约 L3331–3335 |

Books owner 完成这十个日期修复后，06-08 仍需由 root 对当前共享快照做一次独立 post-write 检查并登记 Gate；在此之前 Daily 保持“进行中”。
