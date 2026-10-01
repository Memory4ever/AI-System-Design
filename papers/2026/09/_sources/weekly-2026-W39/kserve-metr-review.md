# W39：KServe / METR 有限来源与 Books 对照

- 审阅者：apr01；2026-09-27 09:50（Asia/Shanghai）。
- 窗口沿 Weekly 合同：`[2026-09-20T09:00:00+08:00, 2026-09-27T09:00:00+08:00)`。
- 仅核两家族及 root 指定 FlashInfer 写后段；未修改 Books、Daily、LEARNING_STATE 或共享索引。本文是独立源级裁决，主任务仍负责准入 reconciliation 与日/周 Gate。
- 实际读取：当前研究合同、ROADMAP owner；Ch61 的 Desired/Applied/Observed、发布、Ch53/Ch62 handoff；Ch66 的完整对象、依赖/时间/可复现条件、授权边界及 Ch65/Ch67 handoff。用代码审阅技能核 KServe 错误路径与测试；本非交互式检查没有启动额外跨模型执行。

## 1. KServe v0.21.0：cleanup 与 desired-state 的错误责任必须分离

**家族：** `SF-2026-KSERVE-V0-21-0`；本次只采用 #6156 的保护行为，不把全部 release 变更纳入。

**日期：** 官方 [release](https://github.com/kserve/kserve/releases/tag/v0.21.0) API 的 `published_at=2026-09-25T17:04:20Z`，即北京时间 09/26 01:04:20；当周 release 事件成立。[PR #6156](https://github.com/kserve/kserve/pull/6156) 的 `created_at=2026-09-08T08:20:33Z`、`merged_at=2026-09-08T11:08:34Z`、merge commit `38c11d71d25c41c67c31cb0e131ff4e55f9f362a` 均窗前。不能把 release 所含机制重新标为本周首次发现；本周事件是可部署版本采用该保护。

**准入与评分：** 保留。删除等待 peer 路由收敛，但 peer 的无关配置 terminal failure 可能阻止清理；这不是普通格式修复，而是服务终止的正确性边界。V2 `Design Delta=2 / System Reach=2 / Durability=2 / Total=6`：局部实现承载重要生命周期机制，跨 controller/finalizer/route 状态责任，约束可复用。保护行为变化触发深入审阅，不抬分至 7。

**实际证据：** PR 说明、讨论和回归测试；API 所列精确 patch；并独立打开 release tag 下 [controller.go](https://github.com/kserve/kserve/blob/v0.21.0/pkg/controller/v1alpha2/llmisvc/controller.go) 的 Reconcile 与 [router_group_cleanup.go](https://github.com/kserve/kserve/blob/v0.21.0/pkg/controller/v1alpha2/llmisvc/router_group_cleanup.go) 的相关实现，确认不是仅凭 PR 文案推断部署版本。

实现先执行 cleanup，再执行正常 reconcile；两个错误可合并记录，但返回 cleanup error 时不带 desired-state 的 terminal classification。cleanup 只操作自己控制的 group route，保留无关匹配与存活 backend；缺失 route/CRD 和访问被拒必须区分。optimistic patch 冲突继续重试，status 按实际 member list 修复。已读 manager regression 与故障注入的目标断言：缺 preset 的存活 peer 不应阻塞另一个成员删除，清理失败不被 terminal 配置错误吞掉，也不应阻止有效 workload 的正常协调。未运行这些测试，未在集群复现。

**关键反证/限制：** PR 明确 user-authored rule 若只引用 peer、不包含 owner backend，后续从 spec 重渲染仍可重新加入 terminating peer；该类删除没有被本修复解决。故不能写所有 route/finalizer 都可靠终止，或 cleanup 自动越过授权、所有 controller 错误都可恢复。测试证明的是作者指定条件，非生产全故障矩阵。

**Books Decision：** `整合`，唯一 owner `PLATFORM-KSERVE` / [Ch61](../../../../../books/part-06-ai-infrastructure/61-kserve.md)，位置为“Desired、Applied 与 Observed 不能压成一个 Ready”末段、进入“发布、流量与回滚”前。写前现文 L104–126 保存 termination outcome 与组件分权，却没有说明清理不能依赖无关 desired-state 成功，也没有解释错误合并可吞 retry。root 已落实正文，实际写后独立核验见 §5。

最小拟写入命题：正常 desired-state 协调与退出清理可以共享观测，却不能共享错误的重试判定；把 cleanup 放在前面还不够，必须隔离 terminal 配置错误与 retryable 清理错误，并限制写入 ownership。代价是额外路由读写、冲突重试、状态修复和 error-path 测试；拓扑简单时常规生命周期仍合理。Ch53 继续拥有 LLM topology，Ch62 继续拥有入口策略，不在邻章重复推导。

**写前提交 root 的正文提案（保留提案上下文，实际正文核验见 §5）：** anchor 为 Ch61“普通 `InferenceService` 在 topology 简单时仍是低复杂度分支。”之后、“发布、流量与回滚”之前。

> 终止清理还不能依赖无关 peer 的 desired-state 已经有效。正常运行时按完整配置重建路由是合理路径，但删除某个 group member 需要存活 peer 先从自己控制的 route 中移除该 backend；若 peer 因缺少 preset 而进入 terminal 配置错误，复用正常 reconcile 就可能让 finalizer 永远等下去。更窄的生命周期分支先按已观察到的成员与路由状态清理 terminating backend，再继续正常协调；它只修改自身控制的 group route，不把其他服务的路由或无授权读取当作可越过的状态。

> 顺序独立还不够，错误分类也要独立：清理错误可以与配置错误共同记录，但不能把需要重试的清理失败与 terminal 配置错误合并返回，否则 retry 可能被抑制。路由 patch、冲突重试和 applied membership 修复增加控制面成本，状态提交也不等于所有用户规则已经收敛；原 spec 重渲染仍可能重新加入被清理的 peer。这一机制保留明确 owner 与可恢复错误的边界，不证明所有 finalizer 都能可靠完成，也不改变 runtime 的 token/KV 权力。

## 2. METR Opus 5.5：具体背景事件，不强造新评估机制

**家族：** `SF-2026-METR-OPUS-5-5`；[官方评估](https://metr.org/blog/2026-09-22-claude-opus-5-5/)。显示日期 09/22，当前原 HTML `datePublished=2026-09-22T00:00:00-07:00`。按作者日级 PDT 日期保存北京时间 `[2026-09-22T15:00:00+08:00, 2026-09-23T15:00:00+08:00)`，不把 midnight metadata 当已核首次可用时刻；整个范围在 W39 内。

**实际证据：** 已读 independence note、Summary of evidence、Conclusions A/B 与透明度脚注。报告区分模型可实现的研发助力，与开发期已经发生的助力；前者有十工作日 API、五任务评估，后者依赖另一团队更高权限的材料，正文团队不能获得底层依据。参与文字审阅的厂商、最终签字机构和公开证据权限也不同。原文不验证特定厂商 policy threshold 或 alignment。没有复现、私有数据或系统 card 全量审计；不把未公开研发加速估计采用为正面事实。

**准入裁决：前分母关闭，评分 `—`（不是零分）。** 当前材料没有新增可核的受控协议、失效机制或证据足以改变本项目评估选择。该具体事件可在 Weekly 背景/排除中说明，不能因 METR、前沿模型或“AI R&D”名词成为候选。不是因为证据私有就判所有评估无效；只是本次公开材料只支持受限说明，没有独立长期增量。

**真实已有命题对照：** `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：

- “第一个不变量：评估声明必须绑定完整对象”L157–180，已规定不同对象/输入/工具/环境不能因模型 alias 相同合并。A 的能力测试不能替 B 的历史生产过程作证。
- “Evaluation Object 必须携带依赖图、时间与可复现条件”L2695–2717，已明确时间、artifact/运行预算/独立 rerun，机构权威不能替代证据；不可公开关键条件只能降为受限 evidence，不能支撑 release gate。
- 授权边界 L2752 已明确可见证据与权限进入 run identity；全访问结果不能直接替代部署合同。

因此 Books `No Change`，不为一个模型名另加段落。“评估者自身可访问证据”与“受评 Agent 能访问证据”并非同一对象：本次判断主要依前两处公开可复现命题，不错误套用第三处作为唯一依据。没有宣布模型能力、研发生产率或风险阈值已被公开证实。

## 3. FlashInfer Ch49 有限写后核查

实际顺读 [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md) 新增“调优结果也是带执行条件的可复用资产”三段、前面的 cuBLAS/DeepGEMM 比较、后面的低 Batch collective，以及对应 `SF-2026-FLASHINFER-AUTOTUNER-V2` Review note。沿用此前已独立通过且未变化的 [官方 §1–3 / §5](https://flashinfer.ai/2026/09/22/autotuner-v2.html) 与 [release](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.7.0) 核验，不重审全年 PR。

准确之处：默认兼容策略没有被说成自动启用新策略；validation 可选、无 hook 的 trust 边界明确；atomic rename 只防半写，不保唯一 winner；同构 rank/共享 store/barrier/reload 的一致性没有被写成全局最优、正确性证明或任意故障恢复。三段融入真实 workload→调优资产→collective 协议的论证链，没有章末 paper append。

**两处窄修均已由 root 实写，09:51 定点重读后写后 PASS：**

1. “host 开销已被稳定摊销”已改为“摊销后的差异不足以改变排序”，不再由稳定性单独推出 device-time 排序有效。
2. CUDA Graph 已明确测 captured replay，不用重复 eager 调用代替；eager 前句仍保留 whole-call 的 host/device 成本。

无需新增 benchmark 数字；rank reduction 是另一可选收敛路线，当前正文选择讲 reload 不构成事实错误，不为穷举 API 再扩段。实际修改由 root 完成；我未写该章，因此本次是非作者 source/body/handoff 核验。正文三段与 Review note 的默认/validation/atomic/rank 限定均通过；没有运行代码或复现实验。

## 4. 本轮验证范围

已核来源、事件日期、准入、三维评分适用性、KServe 必要代码/回归测试与反证、具体 Books owner/handoff；未核全部 release 普通变更、所有评估附件、生产集群或未公开材料。KServe 与 FlashInfer 的实际写后独立确认均已通过，METR 是具体前分母关闭。W39 的 09/22 Daily 普通恢复仍未完成，本文不替代其工作或日/周 Gate，不得据此标 Weekly Complete。

## 5. KServe Ch61 实际写后独立核验

**2026-09-27 10:00（Asia/Shanghai），结果 PASS。** 审阅者 apr01 未参与 Books 写入；实际读取 Ch61 L128–130 的两段、L132 源族标记、L204 Review note，以及前后 Desired/Applied/Observed→发布、流量与回滚的正文。原文依据复用 §1 已核且未变的 v0.21.0 代码与必要测试、PR 反证，不虚报本次重跑代码或集群实验。

正文准确区分 cleanup 与正常 desired-state 协调的责任：清理先行并不能独自保证重试，还必须避免将 retryable cleanup failure 与 terminal 配置错误合并返回；共同日志不等于共同返回分类。controller-owned group route 是明确写入边界，授权拒绝没有被当作资源不存在或无需清理的证明。patch 冲突重试、applied membership 修复的成本与用户规则从原 spec 重渲染、重新加入 terminating peer 的反例均保留，因此没有外推所有 finalizer 都可靠完成。

前文的 terminate outcome 与组件 ownership 自然引出退出清理，后文明确“新 revision 已上线”不等于“旧 revision 已完全退出”，与发布/回滚链衔接成立。Ch53 继续拥有高级 LLM topology、Ch62 继续拥有入口策略，runtime 保留 token/KV 执行权；没有用此控制面修复越过相邻 owner。Review note 正确保存 09/08 PR 先公开与 09/26 release 采用的区别，并承认未在本项目集群复现。

无新增修正要求。此结论只确认这两段受限机制、反证及实际衔接已落实；不构成 W39 整体完成，也不将 09/22 尚待恢复的普通工作改称外部阻断。
