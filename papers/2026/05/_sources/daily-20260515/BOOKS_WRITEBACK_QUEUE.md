# 2026-05-15 Books Writeback Queue

本文件是 date-local author queue；本 lane **未修改共享 Books**。必须经非作者 fresh-context audit 后，由 root 按日期串行写回并再做 post-write audit。

- Queue count: 13
- Status: `pending_independent_review`

## SF-2026-ARXIV-2605-14241
- Primary: `arXiv:2605.14241v1`
- Owner: `AGENT-TOOL-CALLING`
- Delta: 同功能 tool provider 的选择应由观察 runtime load、latency、reliability 与 answer-quality 的在线 router 决定；router 只拥有 provider selection，不拥有工具授权或结果 truth
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-14421
- Primary: `arXiv:2605.14421v1`
- Owner: `AGENT-MEMORY`
- Delta: 持久 Agent memory 的 action justification 应形成签名 provenance 与 derivation-lineage DAG；敏感 action 在 lineage 不闭合时 fail closed，而不是把 recalled text 当作 authority
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-15051
- Primary: `arXiv:2605.15051v1`
- Owner: `INFER-SPECULATIVE-DECODING`
- Delta: 生产 speculative decoding 的 latency model 必须把 request load、emergent batch、draft/verify cost 与 acceptance 联合建模；固定 batch microbenchmark 不能决定在线启用策略
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-15079
- Primary: `arXiv:2605.15079v1`
- Owner: `TRAIN-DATA`
- Delta: 受治理或本地大数据集需要把 schema inference、profile、semantic annotation 与 Croissant JSON-LD provenance 组织为可复跑 pipeline，而不是先上传公共平台再生成 metadata
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-15109
- Primary: `arXiv:2605.15109v1`
- Owner: `AGENT-RAG`
- Delta: Agentic GraphRAG 的 citation faithfulness 应绑定完整 traversal neighborhood、visited-but-uncited evidence 与最终 citation；只验证末端引用会丢失推理路径 provenance
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-15132
- Primary: `arXiv:2605.15132v1`
- Owner: `AGENT-WORKFLOW`
- Delta: 可并行 Agent workflow 应把 dependency DAG、task state、worker placement 与 aggregation commit 分离；吞吐扩展不能牺牲依赖一致性与 failure recovery
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-15185
- Primary: `arXiv:2605.15185v1`
- Owner: `MULTIMODAL-WORLD-MODELS`
- Delta: 视频 world-model 评测应把视觉质量与可度量的 3D geometric consistency 分开，并用 camera/scene geometry 诊断 perspective distortion；该指标不等于 causal controllability
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-15238
- Primary: `arXiv:2605.15238v1`
- Owner: `AGENT-WORKFLOW`
- Delta: 代码生成可把 incremental compiler checker 作为异步 sensor，并用 checkpoint/rollback 保留已验证前缀；compiler 只拥有 static-correctness feedback，不拥有 task correctness
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-15257
- Primary: `arXiv:2605.15257v1`
- Owner: `PLATFORM-MONITORING`
- Delta: CoT monitor 进入训练分布后，模型可能学习 monitor-aware obfuscation；监控合同必须包含 adaptive exposure、外部 signals 与不可由被监控模型控制的 escalation
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-15377
- Primary: `arXiv:2605.15377v1`
- Owner: `PLATFORM-MONITORING`
- Delta: AI control monitoring 应优先组合异质 signal 以降低共同盲区，而非只增加同类 monitor compute；ensemble 自身仍需校准、correlation audit 与独立 stop authority
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-15384
- Primary: `arXiv:2605.15384v1`
- Owner: `AGENT-MEMORY`
- Delta: 顺序演化 memory 的评测必须把 acquisition、retention、forgetting、transfer 与 interference 分成时间序列诊断，不能由最终平均分掩盖负迁移
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-15422
- Primary: `arXiv:2605.15422v1`
- Owner: `TRAIN-DISTRIBUTED-TRAINING`
- Delta: 共享 prompt 的大 rollout RL 训练可将 prompt K/V 与 response K/V 分开复用并保持 causal gradient；收益必须绑定 N、P、R、kernel 与 backward contract
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-18859
- Primary: `arXiv:2605.18859v1`
- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Delta: Agent model routing benchmark 必须给 router 真实 step prefix，并以完整 environment execution 验证替换后果；static replay 与 live dynamic track 应分开报告
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.
