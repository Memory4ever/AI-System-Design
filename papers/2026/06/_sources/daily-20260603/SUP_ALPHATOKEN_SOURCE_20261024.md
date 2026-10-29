# Jun03 AlphaToken：必要 Source 与 SFT 监督选择差额

root只补Jun02自然日。当前AGENTS、适用研究/Report/Daily来源及恢复、统一Prompt、ROADMAP与Books三上下文已读；贡献与联合日证复用本日B5及独核R22/R28。精确v1提交Jun01 03:40:35Z，同DOI arxiv.content/findable registered Jun02 04:20:18Z，完整公告联合区间Jun02 BJT，不搬旧候选归属。首次必要审阅在本记录；尚未独核Source/PRE、未写Books或计整合。

## 原始证据与采用边界

本轮实际打开[当前abs](https://arxiv.org/abs/2606.01635)，唯一v1，当前所见无撤回/删除/勘误。实际读[exact-v1](https://arxiv.org/html/2606.01635v1) §3.1–3.5/Eq1–14/Algorithm1、§4主文假设、§5.1–5.6/T1–3及Limitations、C.5、D.1/D.2与D.6；没有把所有证明、图像像素、可选数据集或代码都称已核。拟2+1+2=5：目标适配/参考漂移与局部/下游路径两条轴共同提议监督位置，是单训练组件的稳定取舍；不将作者Shapley名义、完整因果或无遗忘保证计分。

普通局部概率门易把监督价值和当前置信度混同。AlphaToken用held-out目标小批的梯度方向测适配，用reference参数差乘缓存对角Monte-Carlo Fisher提出旧能力保留的proxy，再分别计算局部token与有限后续窗口的Value路径贡献，合成排序后在batch内top-rho产生detached loss mask。整段teacher-forcing context仍在，mask不是删除token、剪完整forward或真实知识归因。reference Fisher由目标域prompts、reference自采样标签一次估计，不需要旧任务标签，不等完全无数据/无准备；目标验证集虽不直接进masked loss，反复控制mask仍参与训练选择，不是最终独立测试。

局部线性层的梯度内积可由activation/error收缩，未物化全部逐token参数梯度；后续Value路径只保有限W及末K层、忽略score-propagation，是近似，不给完整AR梯度或反事实语义信用保证。Fisher-drift也依赖近驻点、旧loss Hessian与目标prompt Fisher的匹配、较小参数漂移；旧能力缺失就更不能由这个proxy认证已保留。这里不采用§4/完整AppendixB的普遍误差证明，也不由D.2 attention-weight×value-gap图断言全部残差已实测有界。

SFT用Magicoder→HumanEval，DPO从UltraChat warm-start→UltraFeedback，ARC-C/HellaSwag/MMLU/GSM8K仅有限retain人口；Llama3.2-3B/Gemma3-4B/Qwen3.5-9B，四A100、三seed，默认rho.5/lambda1.5/W32/K3，32目标验证样本与1000 Fisher prompts排出训练池。主文声称backbone/split/训练步与协议匹配，不等总准备或scoring费一样；precision/全部sequence和部署SLO本段未核，不采用可迁移效率数字。

直接反侧：T1 Llama HumanEval弱于ordinaryFT，所有基座retain均未完整回到pretrained；T3 adaptation-only目标65.48高于full62.15，stability-only retain52.18高于full50.26，full只是所选平均折中，不是所有轴Pareto改进。D.1 diagonal与Kronecker的近似比较支持局部成本取舍，不认证任意未见旧任务。D.6 epoch包含scoring/mask/update但排除一次Fisher准备，且AlphaToken在所列token-selection基线中实际更耗时/显存；不能由只更新一半位置称训练加速。额外验证forward/backward/cache、参数参考/Fisher存储、AP contraction、搜索与新旧任务回归均计费。DPO使用未mask logit的detached系数和正负分支独立mask，是新surrogate更新，不宣原DPO梯度等价。未复现/核实现。

## actual owner 与最小 PRE

唯一 `TRAIN-SFT` / [Ch29](../../../../../books/part-04-training-system/29-sft.md)。实际读原trace归因、ProFit概率门两完整段、下接weak/strong pseudo-label段及后续InfoSFT/ConservativeSFT/输入reference组，定点查正文与notes无01635/AlphaToken。同章已有mask不删历史/不免forward等成熟边界，不重复将其冒新增；具体缺的是held-out梯度和reference Fisher漂移两轴、直接与有限Value路径共同排序的监督分配。Ch28拥有通用优化/数据，Ch30拥有参数化更新空间，本篇不据DPO分支再建第二完整owner。相关两章开篇已读。

拟在ProFit第二完整限制段后、弱增强提出pseudo-label完整段前插一自然段；不改变现有概率门有效条件。

上锚完整段：
> 这种在线门不增加 reference，却会错过低概率实体、罕见标记或确需纠正的内容；阈值提高也可能损害长尾任务。有限数学/知识任务对照只支持一个可选的概率门，应把 base、模板、阈值、detach 与分母定义绑定，并配对检查监督 token 数、更新规模、训练预算和不同质量切片，而非由平均分认定高概率必为核心。前向和历史处理并未随 loss 位置减少而消失；罕见事实回归、学生置信度不可靠或预算无法匹配时，普通 verified CE 或完整可信 trace 仍是直接退路。<!-- source-family:SF-2026-ARXIV-2601-09195 -->

拟融合完整段：
> 若能额外支付目标验证梯度与可信reference的准备费，监督选择还可分别问“这个位置的更新是否帮助目标任务”和“是否增加参考模型的加权参数漂移”。一个[受限路径感知分支](https://arxiv.org/html/2606.01635v1#S3)将前者的梯度对齐、后者的对角Fisher-drift proxy，各拆成局部项与有限后续窗口的Value路径近似，再按合成排序生成detached loss mask；未选位置仍作可见历史，不授完整因果信用或剪去全部前反向。Fisher来自目标prompt上的reference自采样，不是未知旧任务的真实梯度；验证样本即使不直接进loss，持续决定mask仍参与训练选择。近驻点、分布/曲率匹配或小漂移不成立时，proxy不能保证旧能力保持，有限对照也在目标或retain切片退步。验证求值、activation cache、reference/Fisher构建与存储、收缩和独立回归均计费；少监督位置可反而更慢。质量或预算不合时，保留原概率门、完整可信CE与经核验replay，不由一个平均折中分数批准免费适配或无遗忘。<!-- source-family:SF-2026-ARXIV-2606-01635 -->

下锚为以“当前置信度还可以选择监督对象，而不只决定是否更新或给定目标的权重”开头的完整weak/strong pseudo-label段，加其独立2509-09926 marker；保存时整段保留。本人注仅记录上述实际必要域、未采用的完整证明、独核与实际保存状态。尚待独核，不计Source/Books完成。
