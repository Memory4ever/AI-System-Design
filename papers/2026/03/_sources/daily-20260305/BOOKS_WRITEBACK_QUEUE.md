# Books Writeback Queue — 2026-03-05

Status: partially applied; root final reconciliation and post-write Books audit remain open.

## SF-2026-ARXIV-2603-02376

- Writeback: applied to `INFER-TENSORRT-LLM`; marker `source-family:SF-2026-ARXIV-2603-02376`; post-write audit pending.

- Primary: `arXiv:2603.02376v1`
- Exact source: https://arxiv.org/html/2603.02376v1
- Stable Node: `INFER-TENSORRT-LLM`
- Target: `books/part-05-inference-system/49-tensorrt-llm.md#从手写 Host Collective 到可验证的 Device-initiated Kernel`
- Adjacent: `books/part-04-training-system/36-distributed-training.md#小结; books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题; books/part-05-inference-system/50-vllm.md#本章要回答的问题`
- Existing proposition: 第 49 章拥有从 routing/parallel semantics 到 executable data movement、kernel plan 与安全 commit 的映射；第 36 章只提供训练 collective 的语义与拓扑约束。
- Proposed mechanism: CUCo 把 backend、communication placement、同步范围、issuer granularity 与 chunk size 显式化，由 correctness-first fast path 生成保守 seed，再由 slow path 用测量反馈搜索 fused device-initiated kernel。
- Evidence boundary: 只接受 arXiv:2603.02376v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。

## SF-2026-ARXIV-2603-02601

- Writeback: applied to `PLATFORM-EVALUATION-SYSTEM`; marker `source-family:SF-2026-ARXIV-2603-02601`; post-write audit pending.

- Primary: `arXiv:2603.02601v1`
- Exact source: https://arxiv.org/html/2603.02601v1
- Stable Node: `PLATFORM-EVALUATION-SYSTEM`
- Target: `books/part-06-ai-infrastructure/66-evaluation-system.md#Agent Regression Testing 需要分配 Evidence Budget (line 187)`
- Adjacent: `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`
- Existing proposition: 例如，模型离线比较可以固定 prompt 和 decoding；RAG 评估必须把 index 与 retriever 放进对象身份；Agent 评估还需要记录 tools、sandbox、workflow、budget 和 environment。若只记录 `model_name`，同一模型搭配不同系统组件产生的行为会被错误合并。
- Proposed mechanism: AgentAssay 选择高信息量 trace/断言并在 token budget 内重复测试，把 regression evidence 从单输出扩展到 workflow behavior。
- Evidence boundary: 只接受 arXiv:2603.02601v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。

## SF-2026-ARXIV-2603-02885

- Writeback: applied to `TRAIN-LORA`; marker `source-family:SF-2026-ARXIV-2603-02885`; post-write audit pending.

- Primary: `arXiv:2603.02885v1`
- Exact source: https://arxiv.org/html/2603.02885v1
- Stable Node: `TRAIN-LORA`
- Target: `books/part-04-training-system/30-lora.md#多租户 Fine-tuning：从共享权重转向复用 Backbone 执行 (line 289)`
- Adjacent: `books/part-04-training-system/29-sft.md#本章要回答的问题 (line 10); books/part-04-training-system/31-rlhf.md#本章要回答的问题 (line 10)`
- Existing proposition: S0 Tuning 为这一 adaptation surface 提供 Experimental 证据，但 paper/model-card 的层数、hardware 与 base identity
- Proposed mechanism: MuxTune 在空间和时间上复用 backbone 计算/参数，只隔离 tenant-specific 更新与状态。
- Evidence boundary: 只接受 arXiv:2603.02885v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。

## SF-2026-ARXIV-2603-02765

- Writeback: applied to `MULTIMODAL-WORLD-MODELS`; marker `source-family:SF-2026-ARXIV-2603-02765`; post-write audit pending.

- Primary: `arXiv:2603.02765v1`
- Exact source: https://arxiv.org/html/2603.02765v1
- Stable Node: `MULTIMODAL-WORLD-MODELS`
- Target: `books/part-03-multimodal-world-models/25-multimodal-world-models.md#从重建 Observation 到预测可推进的 Representation (line 172)`
- Adjacent: `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10)`
- Existing proposition: 只保存下一帧或一段 latent trajectory，适合一次性预测，却无法承载长期规划中的假设、外部修正与撤销。进入可交互场景后，world state 需要把 geometry、free space、hypothetical insertion 和 observation-backed correction 分成 typed fields；Agent 只能通过有 schema、版本和回滚边界的 spatial tools 读写。这样 hypothetical state 不会静默覆盖观测事实，代价是状态合并、冲突检测与工具延迟。纯视频生成在只需视觉连续性时仍更简单，真实行动提交仍由第 26 章的 controller 和 safety envelope 拥有。[受限证据：arXiv:2605.09218v1]
- Proposed mechanism: Next Embedding Prediction 直接预测未来 representation，并让状态转移围绕可用于下游决策的 embedding 展开。
- Evidence boundary: 只接受 arXiv:2603.02765v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。
