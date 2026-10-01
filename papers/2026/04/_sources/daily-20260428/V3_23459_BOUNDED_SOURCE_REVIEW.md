# 2604.23459v1 多 Agent 架构安全：必要证据与 Ch72 差异

本页为作者侧有界 Source Review，仅重开[官方 exact-v1](https://arxiv.org/html/2604.23459v1) §4.1–4.4、§5.1–5.3、§6/§8，并与 Ch72 的多 Agent communication-state simulation、coalition red-team、cross-channel influence graph 及 effect authorization 邻段对读。不把本页当日期 Gate、非作者审阅或正式 Books Decision。

## 真正可迁移的评价命题

论文固定各场景内的任务 prompts/rubric，分别改变角色/工具分区、star/chain/mesh 通信拓扑及 private/own-reasoning/shared-memory 可见性。其四类 harmful outcome 为 Planning Refusal、Execution Refusal、Harmful Action 但任务未完成、Harmful Task 完成，另以不同的 benign 任务集计正常成功。因此改进 capability 不等于改善恶意任务抵抗力；架构选择需在**同一场景和配置的攻击机会集**上同时记录阶段结果与正常功能，不能把部分有害动作吞进最终任务失败，也不能用单 Agent 的拒绝率推多 Agent 的授权效果。

决定性反证在具体场景内：BrowserART 的 GPT-4o standalone HT 10%/benign 92.9%，star+2 specialists HT 38%/benign 95.2%；拓扑比较在固定四 specialist/private memory 下，BrowserART star HT31%、chain16%、mesh7%，但 RedCode-Gen 则 star17.5%、chain42.5%、mesh20.6%。相同“更连通更安全/更危险”的排序无法跨场景复用。RedCode-Gen 的 Code judge 看代码是否实现目标、**不执行代码**（Appendix B.6）；它的 HT 是 rubric 判定，不是外部副作用收据。BrowserART/OS-Harm/RedCode-Gen 的 harmful 与 benign 样本数分别 100/42、44/50、160/50，不能把两组成功率视作同一分母；OS-Harm benign 全配置近零，尤其不能从该场景得安全—效用 Pareto 结论。

论文确做 judge 错误人工复核，但剩余日志 10% 抽查仍见 7% discrepancy，不能写成 gold 无噪声。三场景工具划分、底层 action space 不同；跨模型覆盖不均。§8 明确只测恶意用户直接 misuse，未测 indirect prompt injection、被攻陷的系统内 Agent、专用 guardrail 与 role×topology×memory 全交互。论文给的是受限配置下的**架构选择评价协议**，不是“某一 topology 永远更安全”、所有正常任务因安全机制受益或已有 runtime 安全权威被替代。

## 实际 owner 与待决

Ch72 已有跨 Agent 消息传播前 simulation、coalition/role 搜索、cross-channel influence graph 和独立 effect owner；这些段落明确“单组件安全不组合”，但没有把**架构比较中 PR/ER/HA/HT 的阶段结果与 benign success 双分母共同验收**写为一个可操作的评价条件。最窄增量应位于 Ch72 多 Agent 架构/通信安全链，Ch66 只可 handoff 到 protocol/outcome 分账；不是重新写一套 paper 排名。建议维持贡献准入线索、`2+2+2=6` 安全深入**提案**，待非作者核 exact-v1、日期与当前 Ch72 是否已被别处承载，再定实际 Books 决定。若最终入书，正文需用通用的 architecture×threat opportunity set 表述并就近保留不同场景/不同 judge/不同 benign 分母的限制，不得照搬 3.8× 作部署风险率。
