# 2026-05-07 V3 Fresh-context 最终复核

**角色：** 未参与 05-07 作者修复与 root Books 写回的独立 reviewer  
**结论：** 未通过；日报保持 Ongoing  
**复核范围：** 当前 548 项账本、8 个明确恢复项、36 项有界同层反查、3 个最终新增、Books 实际正文、跨日隔离与撤回终态。未扩日期或来源。

## 已确认通过的部分

- 账面守恒成立：`548 = 148 retained + 399 pre-denominator closure + 1 withdrawn`；148 项处置为 `53 Integrate + 75 No Change + 16 Daily Only + 4 Disputed`。
- 2605.04279、2605.04291、2605.04569 的 exact-v1 机制、边界和当前 Books 正文一致；三段正文均位于唯一章末 `## Review notes` 前，且各自保留理论/工作负载与 fallback 边界。
- 2605.04356 只保留撤回排除身份，没有评分或 Books 处置。
- NLA 与 2605.06548 已隔离为不属于本日分母的跨截点 identity，并具有精确重开条件。
- 四项 Disputed 均未支持 Books，且保留可操作的重开条件。

## 阻塞 Complete 的问题

### 1. 2605.04256 是明确 closure false negative，且 Books 已存在无账本绑定正文

exact-v1 把 phys-MCP 定义为异构 physical neural substrate 的 control plane：能力描述、时钟、生命周期、遥测、digital-twin、策略与安全分别取得明确状态/控制责任，并以三类 backend、fault recovery 和 wetware API 做 prototype-level 验证。这正是长期 AI System control/resource contract，而不是只提供某个领域 benchmark。

当前 active ledger 却将其关闭，同时 `books/part-07-agent/83-mcp.md` 已存在以 `arXiv:2605.04256v1` 为受限证据的机制正文。于是报告声称“关闭、不得进入候选”，Books 又真实采用其机制，两个事实源冲突。最小修复是恢复为 retained，完成 exact-v1 Evidence/Score/Books comparison，并把已有正文纳入唯一 Source Family trace；不得重复写一段新正文。

### 2. 2605.04450 是明确 closure false negative，且 exact-v1 identity 标题未对齐

exact-v1 标题是 **One Pool, Two Caches: Adaptive HBM Partitioning for Accelerating Generative Recommender Serving**，不是 active ledger 中沿用的后续题名。其机制不是“推荐效果改进”：EMB hot cache 与 KV cache 争用同一 HBM，online allocator、request router、burst recovery 与 P99 SLO 共同形成 memory/scheduling control loop；作者还给出 32-node A100、8K–15K sequence、三种 workload regime 和五次运行的受限系统评价。

工作负载专用只限制外推，不能把明确的 HBM 状态所有权、路由控制权和 tail-SLO contract 降为分母前关闭。最小修复是以 exact-v1 标题恢复候选，完成 Evidence/Score，并重新裁决 `INFER-GPU-MEMORY` / `INFER-SCHEDULING` 的唯一 owner；若 Books 已有等价主线可判 No Change，否则生成 root writeback queue。

### 3. 2605.04922 是明确 closure false negative

Evolving Idea Graphs 不只是“AI for Science 领域结果”。exact-v1 将 temporary text/chat state 改为 typed graph state，角色在 frozen snapshot 上并行提出 patch，固定顺序 realization 后由 graph-global commit head 决定是否提交；论文还分离 selected decision、materialized patch、realized transition 与 committed artifact。这直接改变 Multi-Agent / Workflow 的 durable state、merge 与 commit ownership。

AI for Science 暂停只排除领域结论，不能排除可迁移的 agent runtime 机制。最小修复是恢复候选，完成 Evidence/Score，并与 `AGENT-WORKFLOW`、`AGENT-MULTI-AGENT` 的现有命题逐项比较；不得因存在 ROADMAP 映射就自动 Integrate。

### 4. Active ledger 的 Review Status 与四项争议汇总不一致

packet 正确记录 4 项 `disputed`，但 active ledger 只有 2605.04243 的 `review_status=disputed`；2605.04069、2605.04295、2605.05029 分别仍写 `standard_complete`、`standard_complete`、`deep_complete`，仅 `access_status` 表示 disputed。机器读取因此得到 147 complete + 1 disputed，而报告宣称 144 complete + 4 disputed。最小修复是统一这三项 active `review_status` 为 `disputed`，并保持已完成的 Evidence 审读内容不变。

## 有界反查结论

本轮只重开与上述三项相同的高风险 closure strata，没有扩到其他日期或来源。2605.05092 与 2605.05126 仍可保持关闭：前者是驾驶舱双流预测的局部架构，后者是特定 VLA cross-view/scene 模块；当前题摘没有独立证明它们改变本书长期 owner/contract。其余 36 项中的领域 benchmark、局部模型改进或通用非 AI workload 也未发现必须恢复的同类项。

## 最小修复与重新验收范围

1. 只恢复 2605.04256、2605.04450、2605.04922，完成当前 V3 Evidence/Score/Books Decision；不重扫 548 项来源。
2. 统一三项 disputed 的 active ledger `review_status`。
3. 对 2605.04256 复用并 trace 已有 Books 正文；其余两项按逐命题比较决定 No Change 或进入 root queue，作者不得直接修改共享 Books。
4. 更新后重新核对分母守恒、处置合计、Books marker/body、README 与 JSON；再由未参与修复的 reviewer 签署。

当前没有 retained-candidate access blocker，也不需要用户补材料。失败原因是可执行的一致性与准入修复，不能用 validator 通过替代。
