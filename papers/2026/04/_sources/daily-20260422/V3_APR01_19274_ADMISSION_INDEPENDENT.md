# 2604.19274v1 HarDBench：有限非作者贡献准入复核

复核范围仅此一篇：独立读取[官方 exact-v1 题摘及正文](https://arxiv.org/html/2604.19274v1) §3.2–3.3、§5.1–5.3 的 Tables 1–4 和必要方法/负例，对照 `ROADMAP.md` 的 `PLATFORM-SECURITY` 与 [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 的运行前/生成后 guard（约 1065–1067 行）、输入可见窗口与安全评价切片（约 1636–1640 行）、persuasion/语义改写（约 2671–2675 行）。不核 04/22 来源、日期或整日 Gate；未复现实验，也未改作者报告或 Books。

**结论：旧“只是成熟 balanced preference optimization 的协作写作应用”关闭理由不成立；建议恢复为 5 分安全候选，按安全评价失效条件做窄范围深入审阅。** 原文不是仅换一套有害内容题库：§3.2 先从 1,204 条经筛选草稿中按四域各取固定 100 条；§3.3 将同一显见有害的不完整草稿分别置于无/有手工编辑任务包装。Table 1 的八个受测模型在有包装 CoJP 下的 GPT-4o-judge ASR 都高于无包装 CoJP；例如 GPT-4o 目标模型由 23.50% 到 96.75%。这里可保留的机制/边界是：**直接有害请求或裸草稿的拒答，不足以验收“可见危险草稿 + 合法编辑角色/补全目标”的工作流**。Ch72 已有 guard 的时机、可见窗口、sensor/authority 和安全/效用分账，但没有这个同草稿任务包装的受控切片；仅指向章节主题不能替代这条实际对照。候选命题可给 Design Delta 2、System Reach 1、Durability 2；因影响保护评价的有效性，5 分仍需深入审受影响证据，而非抬分到 7。

**不能采用的更强说法：** HQ 与 CoJP 同时换入草稿、长度和包装，不能把二者差额全部因果归给 task framing；相对窄的对照只能用 CoJP w/o TF ↔ CoJP。草稿由指定模型/模板生成并经 GPT-4o 筛选，测试集是四域固定 400 条、八个模型；HS/ASR 也主要依赖 GPT-4o judge，Table 5 的人审相关性不能把它升级为开放攻击真实危害率。Table 2 标题写 *unsafe response rates*，紧邻解释却称 *prompts classified as unsafe*，对象未自洽：85%→22% 不得引用为生产前置 moderation 的漏检率，更不能直接与 Table 1 的生成输出 ASR 相减。Table 4 同时改变训练 recipe/数据，且 benign utility 用四个长文本 benchmark 的不同评价器汇总；只能说其受测配置有安全—效用权衡，不能声称 KTO/GRPO 普遍兼顾安全与写作质量。旧 pre-guard、post-generation guard 与独立安全/效用切片仍是合理基线，不能因本例废弃。

本次仅准入校准：Books 仍须另做完整单篇证据/现章具体增量判断；首次公开落入本日窗口和正式候选分母由 04/22 作者及其日级非作者 Gate 单独确认。若作者更新正式稿，应保留原关闭依据与这次改判理由，不把本文件冒充整日报通过。
