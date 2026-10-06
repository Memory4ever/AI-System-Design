# 02/13 最后四家族必要证据与 Books 判断

仅精确 v1；日期复用已核当窗119包络/新增字段，不把 Submitted 当 public。以下完成作者必要审阅，不代替 root 独立语义验收。缓存 V3_CEIGHTCORE/MORE/LAST0–3.txt 与 V3_CEIGHTTAIL.txt 保留原源行标；取到的其他行不宣称全部读过。

## [11137 Weight Decay Improves Language Model Plasticity](https://arxiv.org/html/2602.11137v1)

6分，受影响深入。CORE0 L84–147、MORE0 L279–343、LAST0 L344–365：固定各模型的其他预训练配方扫描 AdamW decay，再用固定任务 SFT 配方比较 base CE 与适配后评价。Llama2 .5/1/4B 为20 tokens/parameter，OLMo“1B”实际1.5B有20/140两预算；数据分别FineWeb-Edu/OLMoMix，不能合并为单一模型因果。OLMo140TPP λ.1的CE2.6088好于λ.3的2.6208，但下游偏好后者；基准CE最优与该SFT目标最优不必一致，强λ10又损害训练。Pearson相关对移除一个配置敏感，不采用统一趋势或“最佳λ=1”。部分大模型/140TPP λ.1基线来自先前实验，不能声称所有配对seed均新重训。准确率/16sample Maj、ORM/RM、Pass与CorrectRatio协议分开，ORM是模型代理。

AppendixA1–A2绑定 AdamW、bf16、batch/length/LR与warmup/cosine（OLMo140为WSD）；SFT按模型固定LR、B64、3epoch、len2048。模型、token预算和SFT损失相同不是所有任务训练token/FLOPs完全匹配；未披露的SFT硬件细节、seed/CI、完整HPO总资源写Not Disclosed，不从rank/probe倒推塑性因果。拟采用只有“decay可作为base quality与后续适配目标不同的受控选择轴”，不采用所有表示机制解释。

作者当前owner比较：TRAIN-PRETRAINING [Ch28](../../../../../books/part-04-training-system/28-pretraining.md) L704–721 已有schedule×returned-estimator及base checkpoint×SFT update尺度，不等于同预训练配置下的decay扫描；L1243–1249是sharpening和reader可读性，不承载这个不同评价目标的控制轴。拟在joint验收坐标后融入两短段：将decay/TPP/模型与固定SFT协议交叉验收，同时保留base收敛优先/旧decay recipe和HPO成本。具体新增为候选PRE，尚未锁/写，root可以按当前正文NoChange，不能凭缺论文名强行整合。

## [11139 TabICLv2](https://arxiv.org/html/2602.11139v1)

5分；因拟长期接口差额定点加深。CORE1 L236–254：在列inducing聚合与dataset ICL的query上，按坐标应用 `q_hi × MLP_base(log n)_hi × (1+tanh(MLP_gate(q_h)_i))`。两个64隐藏GELU MLP；gate在(0,2)，base并无正值/单调保证，不能称确定保持logn趋势。按坐标缩放会改变方向，不是一个每head scalar temperature。toy needle15K的结果限tabular任务，不授LLM长窗或数值稳定普遍保证。

LAST1 L321–357/§7与TAIL L273–282：最终500K+40K+10K多stage、8head模型不是280K/4head ablation的同预算对照；应只用后者单组件增删比较。60 validation datasets、每项最多2048 training samples、两个split；prior作用最大且旧prior下新architecture失败，不能把总成绩归QASSMax。大样本/million、缺失/分布转移、语义column都有限；头数描述col/row与caption col/icl有披露不一致，不据其推实现保证。新增MLP与校准成本、生产精度/latency/SLO未披露。当前v2说明有smaller corrections，V3_CEIGHTREVISION.txt仅定点L251–259核采用接口仍相同；不授其他纠正或后来实验已核。

作者当前owner比较：MODEL-SELF-ATTENTION [Ch14](../../../../../books/part-02-model/14-self-attention.md) L276–285已有score-gap temperature和Lp pair-specific scalar，不承载per-coordinate length×query条件乘子。拟在两者之间融一两段，说明方向/长度/content联合接口与base无约束、toy/局部配对消融及prior混杂；保留成熟scaled QK与分桶校准回退。具体PRE尚未锁/写，不把整个TabICL组件组合或bench搬书。

## [11144 GENIUS](https://arxiv.org/html/2602.11144v1)

5分，评价反侧受影响深入；仅报告。CORE2 L95–165/LAST2 L180–218：510人工curated样本、20subtask、5task，RC/VC/AQ权重6:3.5:0.5由Gemini3Pro配expert gold评分；三输出run不是全部模型/格式的matched计算预算。VQA multiple-choice appearance gold加三个干扰项与生成分别测，支持受限“看懂/生成执行”差别诊断，但不是唯一encoder/decoder因果定位或任意用户意图真值。两模型各选100图、五human的局部相关不能使judger universally correct。text/multimodal expert hints改变可用信息，plan/reflection小增益不是统一机制保证；attention可视化也不是因果证据。

MORE2 L219–271的线性/构造损失与bias补偿理论不采为实际训练因果或一般ICL等价；不照录有归一化歧义的式6–8。实际三phase关键词→相关性→logit bias与TAIL L407–421限定selected decoder layer/time/key zscore加λ，新增关键词/相关性计算，λ/层选择全配置未披露。新增局部诊断证据成立，但尚未得到足以重写长期可靠性条件的受控机制；Ch23已有representation与generation执行分责、Ch24已有conditioning/solver验收原则，不称具体GENIUS算法已覆盖，不为该配方追加Books。

## [11146 DiNa-LRM](https://arxiv.org/html/2602.11146v1)

5分，标准完成；仅报告。CORE3 L129–170/MORE3 L170–232：把clean preference标签应用到加噪pair，Thurstone variance `k σ(t)^2+σ_u^2`（k2/clean .1经验设定）、fidelity loss；chosen/rejected共享epsilon。冻结VAE的SD3.5M latent reward backbone LoRA，0.8M HPDv3 pair/1epoch/8×80GB GPU、AdamW/LR/batch/EMA绑定该设置，GPU具体型号/生产precision与SLO Not Disclosed。concat三noise level feature仍需三个backbone forward，不是免费ensemble。LAST3 L232–299/Table1–3：HPSv3总平均仍更好，ensemble平均增益但HPDv3退步；Fixed σ_u.5与NC clean .1+kσ²不只改变noise slope，不能把增益归为已校准的不确定性。uniform fixed有些dataset更好；必要反侧已足够。

ReFL150updates B256仅换rewardsource，heldout PickScore也是proxy不是human gold。1024²/B1的单step VRAM/FLOPs对不同2B/7B reward model，不授总训练wallclock或统一效率。长程出现grid artifacts、latent不可见pixel问题、跨backbone未证原文明确，不能声称latent reward免hacking。保留新noise-conditioned preference配方和局部对照；尚不足改变Ch31 reward provenance/heldout验收与Ch24噪声state/latent decode已有长期边界，不称该算法已入书。

作者至此完成112个有效落窗家族的必要处理：106项标准/受影响深入及6项4分关闭；实际Books36已POST，最后两PRE与10旧PRE的最终具体差额比较尚可执行，日级未授完成。

最终状态同步（2026-10-04）：本组四项必要源与处置已由root实际独立核通过：11144/11146仅报告；11137 Ch28、11139 Ch14实际两段/邻接/末注非作者POST通过。10旧PRE当前差额已收束为8实际POST整合、10478已有覆盖、10217仅报告；112家族本次必要处理完，46实际Books，不授日级（整日报告另验）。
