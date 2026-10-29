# 01166 BraveGuard：必要证据与 Ch72 最小整合提案

仅补 Jun03 报告的 Jun02 BJT 自然日。已重读当前 AGENTS、Research/Report/Sources 适用分组、统一 Prompt、ROADMAP、Books 公共上下文及本日停点。完整题摘、资格与日期采用本日 R62/精确 batch4 有效层，不第三恢复或移动旧候选：v1 提交 `2026-05-31T11:16:18Z`，原精确 DOI 的 arxiv.content/findable/registered 与适用公告日程组合限定 Jun02；不将提交或注册字段冒充实际公开时刻。当前 [官方 abs](https://arxiv.org/abs/2606.01166) 有 v1/v2、所见无撤回/勘误信号；v2 存在本身不触发前后 diff。

## 读到哪里、支持什么

实际读 [精确 v1 HTML](https://arxiv.org/html/2606.01166v1) §3.1–3.4、§4.1–4.3、Tables 1–3 与 Appendix A；未读完整攻击 payload/所有案例、全部附录、代码或运行实验。这里采用的是防御训练/评价分工，不执行攻击。足以支持机制与直接反侧后停止。

静态 prompt guard 对单步文本学习，不等对多步执行效果的监督。该分支将有 cutoff 的研究威胁整理为 category/pattern/failure 三元组，再生成可执行任务并收集 OpenClaw 完整 rollout；unsafe、拒绝/中止及抵抗轨迹均保留。训练输入序列化真实 action/observation/environment/final，实际优化目标为 binary safe/unsafe；category/rationale 是 annotation metadata，不能声称已训练完整结构化理由。内部生成轨迹的 held-out validation 错误回拨 keyword/taxonomy/task 分布和下一批训练，外部 benchmark instances/labels 不用于该反馈、checkpoint 或调参，公开 benchmark 论文仍可能参与 taxonomy，不能称完全不知评价主题。

Appendix A 实际用截至 Jan01,2026 的110篇、97条查询形成32方法/28风险；这些是论文的数据来源，不是 Jun02 Daily 的发现队列，也不是已经验证持续接入真实未来威胁。抽象可重复循环不等部署中持续适应能力。真实已完成全轨迹的事后分类也不证明副作用发生前可告警或拦截。

Table1 为 AgentHazard-Strongest、OpenClaw3.11 生成的相同轨迹上比较 detector，四 backend GPT5.5/Sonnet4.6/Gemini3.1Pro/Qwen3-235B；八A100服务器，精度、各训练样本数/步数与完整 wallclock、在线 concurrency/SLO 在采用域未闭，记 Not Disclosed，不自补。38.79→82.38 是 GPT5.5 backend 下不同 guard 集合均值，不是跨所有 backend、同一 backbone 或训练预算匹配的纯因果收益；GPT5.5 judge 因高拒绝换用 GPT5.4，不能抹去 evaluator 差额。

同 Qwen3-Guard8B 的 Table3 从 off-the-shelf→static→dynamic→full 增益支持受限训练分布分支，但未给 matched 数据数量/训练和搜索预算、循环轮数，不能唯一归因动态 taxonomy 或开放世界发现。Table2 ATBench500 采用其原生格式、不改 OpenClaw：Brave F1 86.1 低于两个 AgentDoG 的88.8/88.4；作者将差异归格式，但未有只改格式的因果对照。不能照采“全部设置均支配”或未见威胁检测保证。数据收集、任务合成/rollout、标注、再训和独立误拒/漏检回归全计费；无需为本命题读攻击细节/其余消融来补通用安全证书。

## 正式评分与具体 owner 差额

Design Delta2 + System Reach2 + Durability2 = 6：新增选择是把 guard 更新从固定标签集再训，推进为外部威胁结构→可执行轨迹→内部失败引导的数据分布更新，并将外部评价与适应回路隔离；跨训练分布和执行监测，不是一般“安全需闭环”或组件名加分。已确认小知识缺口，深入受影响内容，未要求全附件。

唯一 `PLATFORM-SECURITY` / [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)。实际完整读安全数据 augmentation 段、Policy-as-Data 三段和其前后，以及“局部合理动作会累积成有害轨迹”的完整 AgentHazard/跨轮/委派组；Ch71/73 开篇及 ROADMAP 交接已读。现文分别承载 generator/guard 共盲、运行时 policy 版本与 sensor/authority、多步累计 harm，却未具体讲威胁结构改变训练任务分布及内部 validation 与外部 holdout 的隔离。不是凭无 marker 认定缺口，也不重复 trajectory monitor 本身。

拟位是现有“安全数据闭环还可由当前 policy 生成 adversarial candidates”完整段之后、`### Policy-as-Data` 之前。它从当前模型失败 frontier 接出外部威胁分布如何进入再训，再由下一节区分更快的规则作为输入更新；不把数据训练与运行时 policy 更新写成替代关系。仅以下两段及唯一 family marker 待首次独核，不预授权/SAVE/I/POST/DAY。

## 原两段 PRE

当新的工具与攻击路径改变威胁分布时，只围绕当前policy生成样本，仍可能遗漏已有模型尚未暴露的失败。另一条受限分支把有截止日期的外部威胁材料整理为风险、攻击模式与失败机制，再转成可执行任务，收集正常抵抗与有害执行的完整轨迹供guard再训练；内部验证集上的失败继续改变任务与训练分布。[这一分支](https://arxiv.org/html/2606.01166v1)改变的是监督数据的生产回路，不是让检索到的安全文章直接获得授权权力。威胁来源、任务生成器、执行环境、标签与guard版本应共同保留，外部验收集不能被拿来挖hard cases或选择checkpoint，否则“越来越安全”可能只是评价泄漏。

完整轨迹标签只证明事后检测，不证明有害副作用发生前已能阻断；公开威胁参与训练也不等对未知威胁持续适应。受限对照中，动态任务和内部失败扩展同时增加训练数据，尚不能把全部收益唯一归因发现机制；跨轨迹格式时也不总优于已有guard。研究筛选、合成与rollout、标注、再训及独立误拒/漏检回归都付费。应把这一路线保留为训练分布更新分支，继续使用前面的确定性授权、最小权限和effect-time gate；数据来源失真、judge共盲或独立验收未过时，保留已验guard与人工升级，而不是自动晋升新版本。<!-- source-family:SF-2026-ARXIV-2606-01166 -->

## 停点

首次必要/正式6分/actual Ch72 小 gap 与原两段仅提案，待非writer 独核。未改 Books/Report/State/其他日期，不引入完整攻击材料或别日池。当前日仍普通推进，年度154/279不变。

## 已采用的后续事实

R153首次必要/正式6/actual Ch72原两段PRE通过后，root已在指定上/下完整锚之间真实逐字保存两段及章末本人注；R154唯一实际写后复核通过。只此窄位整合生效，无未完成POST；前文提案/停点为当时准备状态，不授DAY。未扩攻击材料/代码/其他日期。
