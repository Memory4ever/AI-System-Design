# Gemma Scope 2：必要证据与Books局部提案

作者2026-10-02T20:00+08。原始[官方Blog](https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/) published_time=2025-12-19T12:00:00Z，release事件落20窗。当前modified=2026-07-06，不能声称不可变2025正文。[官方所链18页PDF](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/Gemma_Scope_2_Technical_Paper.pdf)首页打印2025-09-16，不据该打印日期授论文首公开；采用当前该报告明确的机制与受限实验，不重写paper归属。

## 实际必要阅读与命题

PDF pp1–13：§2.1–2.6定义、§3.1–3.3数据/训练/初始化、§4.1–4.5评价、§5openproblems。作者拟2+2+2=6，因Ch66具体解释验证缺口深入相应位置；不因110PB/1T参数打分。

- SAE重建activation，transcoder重建MLP computation output；skip branch显式承担仿射项，dictionary承担非线性新项。弱因果crosscoder限制encoder只来自单层、decoder只重建当前及未来层，不偷看未来层重建过去。CLT多层preMLP→MLP output；不是因果真实模型的自动证明。
- §3.3只拼接单层字典会有相同概念跨层冗余；按earlier decoder与later encoder点积抑制近似latent，再由初始化L0逐渐减到目标，属实际初始化机制。不是所有概念都被清除重复的保证。
- **Table1/§3.1：全层SAE/skiptranscoder覆盖270M–27B，但CLT只270M、1B**；不能把跨层结果宣传为27B已验证。IT从PT字典finetune实际chatrollout，不能直接用PT校准授所有chat安全行为。
- §4.1 FVU只反映activation重建，不考虑error对后续输出因果效应；deltaLMloss是替换SAE后LMcrossentropy变化，二者不互换。2048×1024序列，specialtokensmask，pretrain同分布，不授OOD。
- §4.3自动解释=模型生成解释再预测fire/nonfire，不是人工concepttrue或causalfaithfulness。§4.4/Fig4 skip改善FVU/L0取舍；Fig5 1BIT固定prompt的cumulativeinfluence图，CLT/skip更少节点达到给定influence，**不是广泛jailbreak/CoT可靠性的结果**。新增skip参数与单prompt限制保留。
- §4.5decoder初始化cosine仍高仅支持初始化近似，未给controlled端到端速度表；§5jailbreak/faithfulness/SAEdarkmatter为openproblems，不写成安全证明。Workload=Gemma3不同site/sparsity，hardware、precision、endpointSLO、concurrency=Not Disclosed或非在线评价不适用；未运行/复现。

## Owner实际差异

`PLATFORM-EVALUATION-SYSTEM`：[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)当前198–216已实际对读：adapter制造方法改变signal、内部probe不自动release、SAEclassifier报警依layer/span/labels；2002–2011已有干预需controlsurvival/accuracygate。**已有覆盖的是sensor≠decisionauthority与干预≠纠错**，不说整项已有覆盖。未见本报告具体“FVU vs output loss vs autoexplanation vs circuitproxy”分账及跨层字典参数化造成归因对象变化。Ch65开头调度owner与Ch67开头Monitoringmeasurement交接实际对读；不转给Monitoring或Model组件owner。

拟由root协调在Ch66当前SAEsensor两段之后、HarnessIdentity之前新增下列局部草案；我未写共享Books，亦未声明已整合。需要root/Feynman独立准入/必要源核与当前文章版本适用边界确认。

> 内部解释工具也有自己的measurement contract。逐层SAE只重建该site的activation时，较低重建误差并不表示被丢掉的方向对输出不重要；应分别记录normalized reconstruction error、替换重建后的LMloss以及解释者对latent firing的预测。自动解释能预测在哪些文本上激活，仍不证明概念唯一、目标算法已恢复或干预安全。跨层transcoder改为近似多层MLP计算，skip分支再显式分担线性传递，会改变字典与attribution graph所描述的对象，不能直接与原逐层feature图当作同一因果证据。
>
> 因而一套可复用的解释artifact至少要冻结目标模型/PT或IT、activation site、字典宽度/sparsity、跨层因果mask、skip路径与实际验证分布；先分开验证重建保真、输出扰动、解释预测与任务干预，再决定它能承担哪种审计。Gemma Scope 2的受限结果支持skip与跨层表示的局部取舍，不证明大模型复杂安全行为均可解释。多层字典增加训练、sharding和验证成本；只有单site诊断时保留便宜逐层SAE，跨层解释尚不稳定时回到独立行为测试与人工核验，不让更稀疏的图自动成为release证书。

公开事件时间可核；报告当前版本身份未声称immutable。作者必要审阅完成，独立Evidence/Books写入待协调，不算外部日期隔离。
