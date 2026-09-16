# 2026-05-07 V3 第二次 Fresh-context 终审

**角色：** 未参与 05-07 作者修复或 Books 写回的独立 reviewer

**结论：** 未通过；日报保持进行中

**复核范围：** 当前 548 项 active ledger、151 项 evidence packet、前次复核的四项修复要求、三项新增 Books 正文、35 项关闭样本与 12 项候选样本。未扩日期或来源，未修改 Books。

## 已确认通过

- 当前账面守恒：`548 = 151 retained + 396 pre-denominator closure + 1 withdrawn`；候选 Evidence 为 `147 complete + 4 disputed + 0 pending`；处置为 `56 Integrate + 75 No Change + 16 Daily Only + 4 Disputed`。
- `2605.04069`、`2605.04295`、`2605.05029` 的 active `review_status` 已与 `2605.04243` 一样统一为 `disputed`，且四项都没有支持 Books。
- `2605.04256`、`2605.04450`、`2605.04922` 已恢复为候选，均有 exact-v1 方法、评价、限制、三维评分和唯一 owner；其正文分别位于 Ch83、Ch54、Ch81 的唯一章末 `## Review notes` 之前。
- 三段正文均保留了旧基线、改变的约束、状态/控制责任、trade-off、failure/fallback 与 evidence boundary。在线重开三份 arXiv HTML 后，核心机制与账本摘要一致；这只验证采用命题，不把作者实验外推为生产保证。
- 12 项候选分层抽查覆盖 standard/deep、Integrate/No Change/Daily Only/Disputed 和 4～7 分区间，未发现新的明确误收。报告本地链接无缺失；validator 与范围内 `git diff --check` 通过。机器结果不替代以下语义问题。

## 阻塞 Complete 的问题

### 1. `2605.04450` 的 canonical Source Family 尚未贯通 Books

active ledger 与 evidence packet 使用 `SF-2026-ARXIV-2605-04450`，Ch54 的唯一 marker 却仍是旧标题派生 ID
`SF-WHEN-KV-MEETS-EMBEDDINGS-DYNAMIC-GPU-MEMORY-ALLOCATION-FOR-ACCELERATING-`。当前 active 文件没有声明二者的 alias 关系，
因此“正文确实存在”成立，但“以当前 Source Family 可唯一追踪正文”不成立。最小修复是选择一个 canonical ID，并在 active
ledger、packet、README 与 Ch54 marker 中统一；若保留旧 ID，必须在 active evidence 中给出无歧义 alias，不能依赖 superseded
文件隐式解释。

### 2. 有界关闭抽查仍发现 6 个高置信度 false negative

本轮从不属于前次 36 项反查的 closure 中，按位置、学科与“训练替代 / world model / embodied / model control”高风险簇抽取
35 项，逐项重新阅读完整标题和摘要。以下材料已经越过 Candidate Denominator 门槛；是否最终 Integrate 仍必须由 exact-v1
Evidence 与 Books 比较决定：

1. `2605.04346`：不是普通图像分类增量。它直接改变全局反向传播与 activation 保存这一 Training contract，以 block-local
   goodness、协方差统计和可配置梯度传播范围交换准确率、深度与峰值内存。
2. `2605.04413`：给出 embodied counterfactual/world-model identifiability 的新充分条件与反例边界，以 mechanism-wise
   invertibility 和 context-independent inverse transport 替代 global monotonicity；这不是只能留在 MuJoCo 指标里的局部结果。
3. `2605.04525`：把长时域行为规划拆成 high-level diffusion subgoal 与 low-level rectified-flow trajectory，明确以探索能力交换
   实时执行成本，直接属于 Embodied / planning 的条件化设计分支。
4. `2605.04647`：离散 trajectory token、原位 masked revision、full-rollout RL credit 与共享 prefix KV/融合 unmasking 共同改变
   embodied planner 的训练—推理状态链；NAVSIM 与 Thor 数字只限制证据范围，不能作为分母前排除理由。
5. `2605.04980`：研究 LLM activation steering 从单方向到多维 subspace projection 的机制变化，并给出层选择、组合与退化输出
   的评价；它直接改变模型行为控制的表示假设，不是领域应用指标。
6. `2605.05017`：即使属于 position paper，其中心增量是把 embodied privacy 从阶段局部 patch 提升为跨感知、规划与交互的
   lifecycle control signal。它至少需要标准证据审阅并裁决 `Daily Only / No Change / Integrate`，不能因证据初步而在候选前关闭。

这些条目共享同一错误：把“局部 workload 或单领域评价”误当作“不存在长期机制增量”。研究合同允许局部证据进入候选，要求的
是收窄 claim，而不是先证明跨 workload 普适性。前次三项修复清零了当时发现的问题，但没有消除这个共享关闭理由的剩余影响。

## 有界 false-positive 复核

抽查 `2605.04075`、`2605.04135`、`2605.04305`、`2605.04373`、`2605.04467`、`2605.04539`、`2605.04712`、
`2605.04811`、`2605.04995`、`2605.05049`、`2605.05134`、`2605.05206`。它们的采用命题、证据边界与 disposition
可由当前 packet 支撑；本轮没有据此宣称其余 139 项已被重新全文审读。

## 最小修复与重验范围

1. 恢复上述 6 项候选，读取各自 exact-v1 中足以裁决拟采用命题的 Method、Evaluation 与 limitations，完成 V3 评分、owner 与
   Books comparison；不能仅凭本复核直接 Integrate。
2. 围绕这六项所暴露的共享错误理由，定点反查同簇 closure；无需重扫来源或无差别重审 548 项，也不能只改这六个 ID 而保留
   同理由的确定漏项。
3. 统一 `2605.04450` 的 canonical Source Family / alias 与 Ch54 marker。
4. 修复后重算分母、Evidence、Books 处置，替换 README 中旧的 148/53 叙述，再由未参与本轮修复的 reviewer 验收。

当前没有需要用户补充的 primary material。失败原因都是仓库内可执行的准入与可追溯性修复，不能以 validator 通过或三项正文
已经存在替代。
