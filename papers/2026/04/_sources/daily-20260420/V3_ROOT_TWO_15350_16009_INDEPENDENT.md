# 04/20 两项有限非作者 Evidence→owner 复核

复核者：root；本日日报和必要源审阅作者为 apr20_resume。2026-09-28。仅重读决定处置的 exact-v1 主文/附录及目标命题，不代签日期、来源、其他候选或整日 Gate，也不复现实验。

## 2604.15350v1 — Spectral Geometry of Thought

[官方 v1](https://arxiv.org/html/2604.15350v1) §3.5、§4.7/Table 4、§6、Appendix E.1–E.2 与作者日报 §4 对照：谱指数是给定模型、层、阶段和 token 窗口的几何代理，不是“思想”或 correctness oracle。正确性分支六模型、每模型200题、5-fold CV；Qwen2.5-7B 的 ID AUC 1.000 是经过阶段/层选择的局部结果。Pythia 在该集全错，其表中 .500 不是具有双类标签的标准 AUC。OOD 仅四类各10题，7B 为 .600±.10、3B 为 .44±.29；§4.7 的“正确较低 α”与 E.1 的“正确较高 α、同方向”在当前 v1 自相冲突，code tracing 又反向。论文未提供足以把 response-phase 特征作为“最终答案生成前”稳定可得的独立时序与层选择验证。

与 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的传感代理、任务切片、评分身份与 release authority 对照，若谱指标能经独立条件校准，才可能升级为评测信号；当前作者的谱定义、模型/阶段差异仍是受限观察，不能进入生产质量门禁。认同 **2+1+3=6、中央 perfect/答前/普适方向保证争议隔离，Books 暂缓**；不因矛盾否定整篇相关性或作造假判断。此为具名窄 PASS，确切重开范围见日报 §5。

## 2604.16009v1 — MEDLEY-BENCH

[官方 v1](https://arxiv.org/html/2604.16009v1) §2.2、§5.2–5.3、Table 1 对照作者日报 §4：35模型/130案例的 A（独立）、B-Private（A＋自检提示）、B-Social（A＋八名分析者及共识）是隔离上下文条件，Social 并未实际读取 Private 输出。摘要/§5.2 某些“再修订”措辞不能把两支合成同一 trajectory 的社会增量因果。100项无单一 gold 的 Brier 对 jackknife 共识伪真值，ipsative 去均值只表示同一 rubric 内的相对弱项；表中的 Gemma-4 评价 62.3 低于较早 27B 72.9，也不支持单调规模定律或训练规模单因果。

[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已要求把 evaluator、外部真值、slice 和行为 outcome 分账；[Ch82](../../../../../books/part-07-agent/82-multi-agent.md) 已把共享共识与独立新信息分开。本研究的分支协议是有用的受限评价案例，但没有改变这些长期 owner 选择，且未证明内部自监测机制。认同 **2+2+2=6、标准审阅、仅报告、Books No Change**；作者未核的“社交摘要旧修复”不作为事实。此为具名窄 PASS，未对全部附件或后版重新审计。
