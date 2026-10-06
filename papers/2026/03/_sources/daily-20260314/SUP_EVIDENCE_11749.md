# 11749：受控consistency/truth反证与Ch5具体差额

当前结果：root实际必要原证/具体Ch5差额及两段PRE通过并窄写；作者实际非writer完整局部/新两段/本人note回原证POSTPASS（SUP_POST_11749.md），root已同步本人note与释放。正式2+1+2=5深入整合，不授DAY。下文末待核为原提案时状态，不再作为普通待办。

mar14_supplement；Mar13BJT自然日。官方v1题名/唯一作者Konstantin Krestnikov/完整题摘/current v1初版说明与v1–v3 history实际已读 `SUP_ABS_11749.txt`；没有具名先稿/撤回/重要纠错信号，未遍历所有版本。日级门复用root第四六项official字段/公告规则夹证通过，`SUP_DATE_FOURTH.md`、`SUP_DATE_11749.raw`，不单拿Submitted作公开日。HTML不可得，观察abs的精确v1 PDF链接后必要下载 `SUP_PDF_11749.raw`，GET200/2620331B/2026-10-09T16:08:09.684960UTC，`SUP_PDF11749_FIFTH_DATE_MANIFEST_RESULT.json`。按实际取得的URL版本/题名作者识别，不补造PDF首次timestamp。

## 必要Source

实际读PDF物理1–2身份/主张、5–8方法/指标/MDL资格、10–12 Tables1b/2/2a/3/3a、18–20固定step规模/匹配multi-rule关键控制与chained入口、23–25直接讨论/限制。3–4/9/13–17/21–22/26–32没有全读，仅部分开头作必要定位；不采用其未实际核结论/附录。未读code/artifact或复现。PDF页码保留便于定点核，没有声称32页全文。

3.5/11/26/86M character GPT2-like模型、vocab57、AdamW lr3e-4/weightdecay.01/seq256/B32/5000steps、多数四seed。SymPy检数学四类，random单个plausible错误、one compact coherent错误规则、contradictory inverse破坏分别构造。主要指标是在同prompt下只比较correct/incorrect completion NLL，corpus窗口loss辅助且受prompt/长度/boundary混杂；sumNLL/共享最短长度robustness不完全消除所有训练文本长度混杂。held-out pair bootstrap/Wilcoxon与训练seed不确定性分开；大paired sample的小p非四seed强普遍推断。

匹配paired random50:50为83.1%、coherent47.2%、contradictory49%，不是corpus“随机强/矛盾弱/一致零”三层程度都在matched pair得到验证。random10/90 paired约67%仍偏正确，而corpus delta−.0016反向，不能用人口平均loss证明模型在同题失去辨别。coherent20/80 paired9.6%正确，说明一致假规则随频率可占优；但未量化description length或隔离truth/frequency/coherence全部因素，MDL明确heuristic不是有限SGD定理。将“compressibility是唯一原因/通用truth机制”收窄为该受控错误族的可复查反证。

多规则必须对应自身held-out题分布：N1/2/3/5/10为46.6/77.6/82.8/84.8/88.3%，N2低于random83.1，不采用单一跳变、所有multi-rule更难或混single-rule测试的旧式对比。较大模型5000固定step非compute-matched，coherent近chance47–53不能外推frontier、universal/inverse scaling law。chained/自然语言/观察纠正未完整核必要全部对照，不写其70.9/57.7或唯一验证因果到Books；直接Limitations的文字明确稀疏验证/长度/收敛/现实领域推广仍未定。本PDF主文random10/90 rounding与abs不同微精度保留，不以其改评分，不追无关revisiondiff。hardware/precision/完整wallclock/在线SLO未在本必要局部确认，Not Disclosed。

拟 **2+1+2=5，标准最低，因具体Ch5缺口深入所需局部**：controlled coherent-false与random噪声在matched同题下的分离修正“更容易压缩就更真”的重要边界2；学习结果的单组件解释1；损失估计单位与独立truth门稳定2。不为MDL成熟原理、模型尺寸、机构/术语或实验数量额外加分。

## actual owner与逐字PRE

实际Ch5 169–190完整selection边界→记忆/泛化/压缩→coverage/compression distortion→真实分布/隐私邻接，Ch4 383–401目标代理/交接与Ch6开篇actual已读；Ch28 next-token局部只作角色校准。唯一owner `WORLDVIEW-REPRESENTATION`，现177/179有共享结构压缩直觉，181/183有coverage与有损参数记忆；没有把已学习的coherent假规则与随机错误区别、并分开paired同题与corpus人口loss。Ch4的一般代理目标不是该具体差额覆盖，不在Ch28再重复知识机制。拟插Ch5 179压缩直觉后/coverage-distortion之前两段，保留原两类错误分解而不替代。

结构容易压缩，也不等于它对应真实规则。若错误各自需要不同例外，共享的正确规律可能更经济；若假规则本身简洁而一致，预测目标仍可能把它压成可复用计算。在一组[受控数学语料](https://arxiv.org/pdf/2603.11749v1)中，同一问题配对比较正确与错误 completion 的 NLL：随机错误下模型较常偏向正确答案，换成一致但错误的规则后则接近随机选择；假规则占比增大还会让这种选择偏向错误。它支持把“学到稳定结构”与“结构为真”分开，不证明现代大模型只按压缩率决定事实，也不把理想 description-length 直觉当作有限梯度训练的定理。

检查这种现象时，先固定要比较的对象：语料整体平均 loss 混合了频率、共同题型与文本长度，同题、同 prompt 下的 completion 比较才直接检验当前候选偏好；两者可以给出相反方向。配对比较仍要记录错误族、held-out 人口、长度处理与训练 seeds，较小显著性数值不消除训练不确定性，固定训练步数的尺寸趋势也不是同计算预算的 scaling law。更复杂的错误族须匹配自己的测试分布，不能借另一个规则族放大效果。新的语料构造、训练与验证均付费；缺少独立事实依据时，应保留外部检查、检索或拒答，不让低 NLL、规则一致或模型间 agreement 获得 truth 权。<!-- source-family:SF-2026-ARXIV-2603-11749 -->

尚待非Source作者必要原证/具体owner与逐字PRE独核，没有写Books或授POST/DAY。
