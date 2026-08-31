# 2025-05-01 Books Writeback Receipt / Independent Audit Queue

root 已按事件时间顺序 `COSMOS → ZipLLM → Galvatron` 完成三项正文写回。本文件现在保存写回事实与独立审计收据；存在 Source Family marker 本身只证明 trace 可定位，最终通过状态来自未参与本日报主要写作或共享 Books 写回的 reviewer 对 owner 与相邻章节的重读。

**Writeback status:** executed；**Independent Books audit:** passed；**Daily Books Gate:** Passed。

## 1. SF-2025-COSMOS-ADAPTATION

- Writeback observed: `books/part-06-ai-infrastructure/70-cost.md`，`semantic-body-binding:SF-2025-COSMOS-ADAPTATION`

- Primary: `arXiv:2505.01449v1`，first public `2025-04-30T02:06:26Z`
- Stable owner: `PLATFORM-COST`
- Target: `books/part-06-ai-infrastructure/70-cost.md`，建议插入“训练成本”与 `cost_to_quality_target` 之后、进入推理成本之前
- Adjacent review: `books/part-06-ai-infrastructure/66-evaluation-system.md`、`books/part-04-training-system/29-sft.md`
- Existing boundary: 成本章已经把训练、失败、推理与平台开销绑定到 outcome，但尚未把 fine-tuning、retrieval-augmented ICL 与组合策略表述为同一个受预算约束的 adaptation portfolio。
- Long-lived proposition: 决策者不应先固定 adaptation 方法再计算账单；在 task/data/model/hardware/price/evaluation contract 冻结后，quality/cost predictor 可以提出策略候选，但真实 evaluation 与已发生的 resource accounting 才拥有选择真值。
- Evolution and coexistence: 单一已知方法在任务稳定且数据访问边界清楚时仍合理；当可选路径增多、训练与检索成本不可直接比较时，才引入联合预测。收益是减少无效 sweep，代价是 predictor calibration、价格漂移与 failed-run 归因；预测越界时回退直接 measurement。
- Evidence boundary: 只支持论文披露的 11 个 NLP classification tasks、模型 roster 与 A100 条件；不证明生产 workload、价格变化或分布漂移下仍能准确选择。
- Writeback acceptance: 不能把作者预测值写成生产节省；正文必须同时保留旧方案成立条件、proposal owner、evaluation owner、失败模式和回退。

## 2. SF-2025-ZIPLLM-STORAGE

- Writeback observed: `books/part-06-ai-infrastructure/59-model-registry.md`，`semantic-body-binding:SF-2025-ZIPLLM-STORAGE`

- Primary: `arXiv:2505.06252v1`，first public `2025-04-30T04:16:32Z`
- Stable owner: `PLATFORM-MODEL-REGISTRY`
- Target: `books/part-06-ai-infrastructure/59-model-registry.md`，建议插入“Registry 与 Artifact Store 的边界”中 `URI + content digest + provenance + access policy` 之后
- Adjacent review: `books/part-06-ai-infrastructure/58-kubeflow.md`、`books/part-06-ai-infrastructure/60-training-operator.md`
- Existing boundary: Registry 已分离 metadata/index 与 artifact store，但尚未解释大量同源 checkpoint 的物理共享为什么不能合并逻辑模型身份。
- Long-lived proposition: artifact store 可以对同源 checkpoint 执行 tensor/chunk-level dedup、family clustering 与 lossless delta compression；Registry 仍必须保存每个逻辑模型的 base/delta lineage、完整性 hash、authorization、deployment reference 与可独立 materialize 的恢复路径。
- Evolution and coexistence: 完整 checkpoint 在规模小、独立恢复优先或 family 相似性不稳定时仍最简单；model-family 数量和重复权重增加后才引入物理共享。收益是容量与传输下降，代价是 clustering 误判、base deletion、恢复放大、加密/量化兼容和跨租户泄露风险。
- Evidence boundary: exact-v1 与项目 artifact 支持论文所测 Hugging Face families 和 BitX 组合；不证明任意 encrypted、quantized 或 license-separated artifact 都可共享。
- Writeback acceptance: 物理去重不得改变 Registry 的 logical identity；必须写出 base deletion、独立 rollback、hash 验证与 unsupported artifact 的 fallback。

## 3. SF-2025-GALVATRON

- Writeback observed: `books/part-04-training-system/36-distributed-training.md`，`semantic-body-binding:SF-2025-GALVATRON`

- Primary: `arXiv:2504.21411v1`，first public `2025-04-30T08:11:45Z`
- Stable owner: `TRAIN-DISTRIBUTED-TRAINING`
- Target: `books/part-04-training-system/36-distributed-training.md`，建议在 static/dynamic plan 与 cost-model 讨论附近加入可校准 planner 分支，而不是在 Review notes 堆叠论文摘要
- Adjacent review: `books/part-04-training-system/37-tensor-parallel.md`、`books/part-04-training-system/38-pipeline-parallel.md`
- Existing boundary: 本章已有 cost model、collective 与静态/动态计划边界，但 automatic plan search 的状态 owner、prediction calibration 与失效回退仍不完整。
- Long-lived proposition: planner 只拥有候选 execution plan；model shape、cluster topology、memory cap、parallel/kernel revision 与 collective profile 共同定义 plan identity，runtime telemetry 才拥有 predicted throughput/memory 是否成立的上线真值。
- Evolution and coexistence: 手写 DP/TP/PP 组合在 workload 与拓扑稳定时容易验证并能复用 process groups；组合空间扩大后再引入 profile/cost-model/search。收益是自动探索，代价是 profiling、search explosion、错误 memory estimate、plan churn 与拓扑漂移；预测失真时回退已验证静态 plan。
- Evidence boundary: exact-v1 与 Hetu-Galvatron artifact 证明作者 workload 下的搜索与执行链，不证明 cost model 能跨硬件、版本、拓扑拥塞或 elastic failure 稳定外推。
- Writeback acceptance: 正文必须区分 proposal、execution 与 telemetry owner，并保留固定静态方案的共存条件和明确 fallback。

## 独立 Books 语义验收

**Auditor:** `fresh-context:may03_daily_cross_review_20260831`

1. 已重新读取每个 marker 的上下文与目标章两侧 handoff，确认三项都进入机制正文，而不是论文卡片式追加。
2. COSMOS 保留直接 measurement，ZipLLM 保留完整 checkpoint，Galvatron 保留静态 plan；三项均明确 proposal/decision owner、收益、代价、failure mode、证据边界与 fallback。
3. 复核发现 Books Comparison 中三个失效 adjacent ref，已在日报修正为 `15-multi-head-attention.md`、`78-tool-calling.md` 和 `71-multi-tenant.md`。
4. 三项 Decision 维持 `Integrate`；日报已同步为 `Complete / Closed / Passed / Passed`，未解决 finding 为零。
