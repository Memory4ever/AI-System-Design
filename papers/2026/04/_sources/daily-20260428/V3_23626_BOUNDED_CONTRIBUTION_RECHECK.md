# 2604.23626v1 GraphPlanner：贡献门槛有界重判（作者侧）

本记录只裁决旧前关闭被独立反查推翻后的**贡献准入**，不是候选评分、日期终验、Books 写入或整日 Gate。原始身份和完整题摘见本日 `V3_ARXIV_ADMISSION_BATCH2.md`；独立反查见 `V3_APR01_ADMISSION_BATCH2_INDEPENDENT.md`。

| 核项 | 必要依据与判定 |
| --- | --- |
| exact-v1 实际机制 | [官方 v1 §3.1–3.2](https://arxiv.org/html/2604.23626v1) 的每步动作是 `(planner/executor/summarizer role, LLM backbone)`，有首尾及最大 planner 次数的 action mask；`G_workflow` 保存当前轮轨迹，完整 episode 再进入 `G_history`，异构 Query/Agent/Response 关系用于策略打分。故旧理由“只是单轮选模型、未隔离历史图贡献”确实不成立。 |
| 有效对照与代价 | [§4.3](https://arxiv.org/html/2604.23626v1#S4.SS3) 有 w/o History、同构图、异构图、inductive/transductive 对照；w/o History 同时去掉状态信息，不能单独归因 graph encoder。§4/Tables 2–3 的推理 `Cost` 是输入/输出 token 数乘模型价格；Table 4 另列训练 `GPU Compute` 却用 GiB，二者不是同一成本分母，论文未给将该量转成显存、训练 GPU-hours 或部署成本的可复算桥。Table 3 中 GraphPlanner 平均推理 Cost 605.0 也高于 Router-R1 的 76.3，不能概称既更准又更省成本。Phase 1 固定 workflow，只优化 backbone；Phase 2 联合选 role/backbone。14 个 QA/推理任务、有限模型池不是长时工具副作用或生产延迟验收。 |
| 真实 owner 对读 | [Ch81](../../../../../books/part-07-agent/81-workflow.md) 的 template→realized graph→trace 与 deterministic transition 已把 workflow 状态/结构提交权给 runtime；[Ch82](../../../../../books/part-07-agent/82-multi-agent.md) 的动态 topology、task-context＋peer capability posterior＋历史 outcome ledger、角色参与和端到端 topology/role/execution-policy 优化，已经把受限 joint routing 的设计对象与事实/结果权分开。GraphPlanner 更具体的 Query/Agent/Response 异构图、固定三角色 `3K` 动作、PPO 是一种 state encoding/selector 实现，不改变该分责或需要新的 release/evaluation contract。 |
| 作者侧处置 | 建议从“继续核贡献”改为**具名前分母关闭**，而非沿用已失效的“无历史消融”理由。新关闭理由是：在当前长期知识树中，逐步联合选择 role/backbone 与历史 outcome 条件化 routing 已由 Ch81/82 承载；论文增加的异构图编码和固定 action mask 在披露的 14 任务范围内未形成独立状态、控制或验收 owner。保留论文受限对照和成本量纲冲突，不把它写成“无新方法”或“图无用”。若非作者指出 Ch82 缺少 role×backbone 能力矩阵在同一 workflow revision 下的**具体不同决策责任**，只重开该窄命题。 |

日期：本日记录中 v1 Updated `2026-04-28T00:52:46Z` 与官方公告/连续 ID 可作有界本窗线索，但本记录不把 Updated 当首次公开，也未独立检查更早官方全文；前分母关闭不依赖日期定论。
