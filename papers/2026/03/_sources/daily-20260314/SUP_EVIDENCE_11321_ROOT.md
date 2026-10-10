# 11321 HAPO：必要理论反证与暂缓提案

root作者，只处理Mar14的Mar13自然日补充，不动旧候选。完整题摘/当前事件说明与日期夹证为`SUP_TITLE_ABS_11321.txt/.raw`、`SUP_DATE_11321.raw`、`SUP_DATE_SECOND.md`；同日公开上下界已核，提交日不单独当公开日。未识别具名撤回/修订说明；当前v1只审所需命题，不比较v2/v3。

实际读[精确v1](https://arxiv.org/html/2603.11321v1) §3.2–3.3/Eq2–6、§4全部/Alg1/Eq7–14、§5全部/Table1和§6直接结论。新增是同prompt当前group成功计数的Beta均值门，低于gamma时把最差trajectory替换成已验证teacher，然后重算组统计：teacher路径走shaping loss、其余路径走clipped RL。它不是采样一个Thompson posterior action，也不是把全部group变成纯CE。Gate/synthetic sample改变人口和loss，不把成熟Beta/GRPO另计新基础。

中心渐近无偏论证未成立。Theorem4.2允许mu*>gamma且小于1，Alg1每次仅用本组固定N的计数；即使policy已收敛到mu=.9>N门gamma=.8、N=8，c=(1+S)/10<.8等价S<=6，二项概率为0.18689527，仍不消失。Eq11的指数上界在固定N/固定mu下也不趋0；不能从时间t增加推出N增加或mu趋1。这是直接满足所述条件的反例，不是要求所有toy理论覆盖真实LLM。新增N增长/阈值退火或更强policy假设可能修复，但当前没有作为定理条件。Eq10的switch estimator还须条件均值/方差及有效下降方向，bounded stochastic variable本身不证动态目标收敛；不采用这些强保证或替作者补证明。

实验Qwen2.5-Math-7B，OpenR1-Math-46k-8192/DeepSeek-R1已验证示范；batch128、固定LR1e-6、group8/gamma.8、训练temp1、评价temp.6/max8192；AIME avg32与其他pass1不可混分母。Table1对LUFFY AIME同36.7、MATH50087.0>84.6、Olympiad51.4<51.8；Fig2 teacher使用仍波动，不是消失定理实证。总tokens/训练steps、hardware、precision、重复trainseed/CI、完整teacher费用未充分披露，SLO不适用离线实验。固定LR实验也不是定理衰减LR实例。未核代码或复现。

拟评分 **2+1+2=5**，中心训练目标/无偏性冲突需必要深入，已读到足以裁定上述命题；**争议/暂缓Books0**。实际 [TRAIN-GRPO / Ch33](../../../../../books/part-04-training-system/33-grpo.md) Group-relative Gradient节及前后430–525已明确组内耦合、不同estimator不能继承无偏、筛选改变人口与bias/variance分账；不能让本稿未闭合的渐近保证进入该论证。局部teacher-gate实验可在报告保留，不自封为新的长期正确性机制或把更多论文名追加正文。

重开只需修正后的精确定理条件/有效证明与对应估计器，或足以支持独立局部新机制的matched预算和teacher-use反侧；不请求整库版本比较。非作者mar14_supplement已实际核必要原证、独立反例及Ch33具体处置，见`SUP_DISPUTE_11321.md`，本项争议裁决通过；不授DAY或正面理论Evidence通过。
