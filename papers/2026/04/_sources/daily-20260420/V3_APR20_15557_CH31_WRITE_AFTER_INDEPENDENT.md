# 04/20 2604.15557 Ch31 实际写后非作者有限复核

复核者 `apr20_resume` 不是该次 Ch31 正文写入者（写入者 root）。本记录只签 `2604.15557v1` 的必要 source→实际新增命题及相邻衔接，不签 04/20 的来源、日期、其他候选或整日 Gate；报告作者身份不代替最后日级非作者复核。

## 实际核验

- [官方 exact-v1](https://arxiv.org/html/2604.15557v1) §3.2–3.5 定义的 `A_lin` 是中间状态经最终 norm 与固定 unembedding 后的单 token top-1，不是任意线性可读性或模型内部知识真值；residual MLP 的 80/20 probe 是另一条读出路径。§4.2–4.3 以实际注入的目标 token 概率变化 `ΔP` 衡量 steering，trained linear probe 在早层高于93%而 `ΔP` 近零，是“可读不等干预成功”的受限反例。§5 及必要 Appendix D/F/H/J 的按层/家族相关、少数 target、层选择和外推限制没有给通用生产 controller 或 safety guarantee。
- 实际顺读 [Ch31](../../../../../books/part-04-training-system/31-rlhf.md) 新增段及两侧：前文把 conditional activation intervention 定位为可撤销 actuator，原有评价/权限 Gate 仍在；新增正文在它之后、按层反馈控制之前，将 probe 可读、原 output head 对齐、实际干预效果分成三步，再接选层/幅度与回退。此顺序让“选择干预位置”先于“控制施加量”，没有把两篇后续方法混成一项。新增正文写明冻结模型/tokenizer/概念/方向、非目标行为回归，以及单 token、未知输入、分布漂移与授权边界。
- 章末 Review note `SF-2026-ARXIV-2604-15557` 的 official exact-v1、必要方法/反证及 Mamba/RWKV 不作 steering 的范围与正文一致。`git diff` 限本家族是两段正文和一条 Review note，未将作者的三阶段解释、全模型定律、oracle 选层效果或在线 SLO 写成定论。

**结论：实际写后 PASS。** 这是唯一 `TRAIN-RLHF` Ch31 的窄长期选择边界；可在 04/20 正式表计为已落地整合，同时保留 2+1+3=6 的原评分与深入审阅原因。该判断不证明本日报 99 项、50 项前闭、十四来源或 first-public 统一通过。root 应将共享 Ch31 Review note 中“写后待验”的状态据此同步；本文不直接改共享 Books。
