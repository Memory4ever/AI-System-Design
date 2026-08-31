# 2025-05-03 Books Writeback Queue

此队列保留 author-owned Books Comparison 与 root 串行写回 provenance。三项写回均已由未参与日报写作和 Books 修改的 fresh-context reviewer 核对 owner、相邻章节、正文语义绑定与 evidence boundary。

## HONEYBEE

- Writeback Status: `written_audited`

- Source Family: `SF-2025-ARXIV-250501538-HONEYBEE`
- Owner: `AGENT-RAG`
- Target: `books/part-07-agent/76-rag.md#L85`
- Adjacent: `books/part-07-agent/75-context.md`; `books/part-06-ai-infrastructure/71-multi-tenant.md`
- Anchor: 在 retrieval-time tenant filter 与 per-tenant index isolation 的二元路线之后。
- Long-term proposition: RBAC role graph 可成为 ANN physical partition input；overlapping partitions 用受控 replication 连续权衡 latency、memory 与 recall，同时必须显式承担 update fan-out、role churn 和 policy revision。
- Evidence boundary: 13.5×/90.4% 数字只属于作者 RBAC benchmark、HNSW 参数和 workload；不能外推为通用向量数据库结果。

## MoEQuant

- Writeback Status: `written_audited`

- Source Family: `SF-2025-ARXIV-250503804-MOEQUANT`
- Owner: `INFER-TENSORRT-LLM`
- Target: `books/part-05-inference-system/49-tensorrt-llm.md#L394`
- Adjacent: `books/part-02-model/21-moe.md`; `books/part-05-inference-system/50-vllm.md`
- Anchor: 在“quantization 可能改变行为、不能只看存储”之后。
- Long-term proposition: MoE calibration identity 必须覆盖 activated-expert distribution；token-average calibration 会掩盖低频 expert 的量化误差。expert-balanced sampling 与 affinity grouping 是实现分支，不是通用最优算法。
- Evidence boundary: 作者 family、dataset、bitwidth 与硬件范围不证明所有 expert 同 bitwidth 或端到端加速。

## CompleteP

- Writeback Status: `written_audited`

- Source Family: `SF-2025-ARXIV-250501618-COMPLETEP`
- Owner: `TRAIN-PRETRAINING`
- Target: `books/part-04-training-system/28-pretraining.md#L154`
- Adjacent: `books/part-02-model/17-transformer-layer.md`; `books/part-04-training-system/29-sft.md`
- Anchor: 在 optimizer/parameterization 与 global/layer-wise LR 区分之后。
- Long-term proposition: depth-wise HP transfer 与 non-lazy feature learning 是 parameterization contract 的两个独立条件；学习率 schedule 不能修复让深层长期停留在线性化邻域的参数化。该机制不推出逐层动态 learning rate 的普适方向。
- Evidence boundary: 12%–34% 只属于作者模型形状、training recipe 与 Cerebras CS-3；跨硬件/架构仍需 matched probe。
