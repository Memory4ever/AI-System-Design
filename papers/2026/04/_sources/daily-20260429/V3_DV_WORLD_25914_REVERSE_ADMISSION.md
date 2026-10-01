# 2604.25914v1 DV-World：贡献前分母反向审

作者侧准入重审，待非作者负侧抽样。[官方 exact-v1](https://arxiv.org/html/2604.25914v1) §2.1–2.4、§3.1–3.5、§4.1–4.2；[官方 v1 身份](https://arxiv.org/abs/2604.25914v1)。本项旧 60 题摘原列潜在，现只针对“有无超出领域 benchmark 的可保留设计／评价反证”定点消歧，不遍历附录或实现。因拟贡献前关闭，不为排除另追独立首公开史；v1 `submitted=04/28T17:58:21Z` 不能被写成首次公开时间。HTML 正文另出现作者文字 `date: August 24, 2026`，与 v1 身份页不一致，不借该内文日期反向迁移本窗。

原文确有工作量和真实局部价值：260 个可视化任务分为原生 spreadsheet chart/create/fix/dashboard `130`、跨 Python/ECharts/Vega-Lite/D3/Plotly 的演进 `80`、含含糊意图与模拟用户澄清的交互 `50`。§2.2 同时看原生数据表 coverage、native chart must-fix specs、视觉 rubric、ISR；§2.3 由 18 名领域人员从论坛问题改写，保留复杂表结构并扰动数据。§3.2/Table 3–5 在其 agent/harness 下展示原生编辑、图表演进和交互低分；不能以“只是应用”或小题量一刀切否定。

但准入问题不是新增一套数据集是否有用，而是它是否修正本书的可迁移评价/设计选择。五类任务把已知责任分别实例化：图表的 data binding／native object 与像素美观须分账，编辑要验旧 artifact 保留，含糊请求要先澄清再验 effect，simulator/rubric/judge 与真实用户还须分账。[Ch66 的结果/语义/协议/环境分层](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)及其 artifact-preservation、judge 校准与分阶段 outcome 已承载这些判断；[Ch84 的 Human Participant 与 task state](../../../../../books/part-07-agent/84-agent-platform.md)已把用户澄清/commit 与 Agent 提案分权。论文没有受控地证明“只看图片／一次任务成功／只看 ISR”在共同任务上产生**当前合同未能预见的决策反转**，也未给超出这些 owner 的新 verifier/authority/state 机制。§3.3 的原生 chart 失败和 §3.5 的 clarification→execution gap 在该 260-task 样本中是局部观察，不成为所有 Agent 或可视化系统的一般定律。

边界还包括：§2.2 的最终分数人为加权 rubric＋Table Coverage/ISR，不是统一正确性概率；Table 5 不共享同一模型/成本/工具预算的全方法对照；§4.1 的模拟用户由 GPT-5-mini 和规则构造，150 条人工审阅只能校准所测行为，不证明隐藏意图或用户情绪全面逼真；§4.2 的 210-task 多 judge 排名稳定不授权个案分数为人类真值。它是值得保留为该领域 benchmark 的测例，但本次项目贡献门槛没有被跨越。

作者侧**维持既有的具名前分母关闭**：不评分、Books 不改。[本日检查点“四项准入消歧”](./V3_REOPEN_NOTES.md)此前已把 25914 计为前关闭；本次补强其原文与 owner 依据，**不再次扣减**。因此在 BARRED 25203 恢复后的最新题摘工作账仍是 `106=70 潜在+36 前闭`，旧 60 仍为 `40+20`；24842 Co-Director 反向提案另待核。若有同一任务、同运行/人类判据下的对照证明现有 Ch66/84 的 native-object/intent/effect 分账仍漏掉可迁移失效，再定点重开；无需为排除追全附件、后续版本或绝对公开时刻。本项作者自核不代替非作者负侧抽样、来源或整日 Gate。
