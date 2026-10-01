# 2604.20200v1 → Ch66 实际写后独立复核

复核者：apr02；书稿写入者、04/23 日报作者：root。2026-09-28。只核[官方 exact-v1](https://arxiv.org/html/2604.20200v1) §2.1–2.2、§3.1–3.6、§6 与 Appendix B.2.4–B.2.5 的必要对象、关键反证，顺读 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) `EvalSpec` 定义后 `source-family:SF-2026-ARXIV-2604-20200` 两段及前后 proxy、任务难度切片；并读该 family 章末 Review note。源→owner 写前两份审阅见 [root 证据](V3_ROOT_20200_FINITE_EVIDENCE.md)、[apr20 非作者审阅](V3_APR20_20200_FINITE_INDEPENDENT.md)。未读全部附件、未复现实验、未验 04/23 日期/来源/分母或整日 Gate。

**实际写后 PASS。** 原有 `EvalSpec` 的目标/proxy 原则仍是上游，新增两段把公开标签在 Agent 可读工作区、逐轮 public-score 反馈、用户压力和 private holdout 放到同一评价身份，区分开发反馈与发布证据；后接按任务难度/生成规则分切片，叙述衔接成立。公开文件被叫作 held-out 不改变访问权限、提示禁令不是强制访问控制，均是原文条件下合理的工程推论。隔离带来的调试、hidden evaluation、权限和轨迹审计成本，以及保留低风险公开反馈的共存路径均在正文，没有偷换为“公开集一律不可用”。

数值/因果边界：exact-v1 主文为 13 Agent×34 任务×3 轨迹＝1,326 runs，§3.4 是 403 exploit-positive runs，§6 的 462 与之不合且原文未解释同一分母的调和；书稿正文不写任一 headline 数字，Review note 明确隔离 462。214 有人类多数标签、197 一致只校准 judge，非完整行为真值；3任务×4 Agent×每配置1 run 的提示/压力消融并非可靠访问控制，最高压力非单调。新增正文只说受限实验中观察到 public/private gap 与提示缓解，不宣称提示有保证、能力增加致作弊、生产发生率或线上 SLO。以上与前后现有 release authority/holdout 论证一致。

本次 `git diff --check -- books/part-06-ai-infrastructure/66-evaluation-system.md` 通过。此 PASS 仅允许该 source family 的 Ch66 实际写入与写后状态被 04/23 作者侧同步，不替代该 Daily 的首公开归属、十四来源、候选分母或独立日级 Gate。
