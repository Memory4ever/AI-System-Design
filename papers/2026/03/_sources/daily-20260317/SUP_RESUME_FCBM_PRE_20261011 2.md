# 13163 f-CBM 必要原证与概念接口差额

resume_mar17，仅本17补03/16自然日。完整v1题摘/匹配DOI日级夹证有效复用SUP_AB_MULTIMODAL第11行及原独核。当前官方abs只有v1，无已给出的撤回/勘误标记；不遍历网站或版本史。2+1+2=5，具体表示接口与直接反侧深入；未写/PRE未独核，不计safe。

## 必要 Source 与边界

[exact-v1](https://arxiv.org/html/2603.13163v1)实际§2.1、§3.1–3.3/Eq1–2、§4.1–4.3/Eq3–7、§5.1–5.2/Tables1–2及§6。不冒图中像素已独立视觉核、所有artifact或复现。CLIP两encoder拼接后预测concept vector；概念目标来自LLM选concept、CLIP-large/sentence-transformer cosine合并，CUB合成文本由原属性生成，非独立人类语义真值。N24仅4类/195concept、CUB仅15类/112属性，77token输入限制保留。

新支路让每个预测concept与标签的KDE互信息靠近该concept目标与标签的互信息：Eq5平方差同时罚过高与过低，不等单侧消除信息，也不是条件互信息或联合瓶颈证书。leave-one-out KDE需类别非singleton、正bandwidth/H(y)等条件；running-mean归一的零值guard未披露，不采用精确数值recipe。KAN是单层可学习逐concept一元基函数再加和，不称任意交互的通用多层KAN。只支持读出容量与concept监督共同调节的受限训练分支；相关的CTL/ICL及干预改善不证明概念只编码指定语义。

Table1 CUB-base79.3低blackbox91.3、CUB-large85.3低95.8；large CUB cRMSE .273高CT .201且CTL .045高Independent .025，不能采“所有数据/全部指标最低leakage”。Table2 Independent N24 cRMSE +15.7%是退步，§5.2文字所称反向与表不一致，仅保表原对照/不给最佳无损headline。§5.2消融支持有限head/loss取舍，但重复/CI、完整sample split、batch/epochs/HW/precision/SLO与制备/训练费用未齐，不签归因幅度或免费可靠性。干预排序用validation gain后test替换，目标仍自动注释，不能称逐样本人类专家纠正或所有介入必改善；图趋势只按文字作为作者有限声明。

互信息代理反例仅本轮分析：独立binary A/B及Y=A xor B，逐轴I(A;Y)=I(B;Y)=0而联合足以恢复Y，故低逐轴CTL不证明联合无任务信息；这不声称本文单层additive KAN实现该XOR或作者代码必错。语义重命名也可保持互信息；MSE/独立语义核验不能由该proxy替代。中心“完全faithful/只含语义”不采用，但受限代理训练接口不依赖其保证，可准备Books。若未来要认证完整leakage或精确recipe，仅一次请求联合/条件信息与独立concept真值、KDE退化guard、对应原表/干预人口及完整配置；不扩大附件队列。

## 实际 owner / 逐字 PRE

已实际读Ch23 43–101 tensor/semantic→encoder/projector→stitch→共同maps完整邻接及207–218残余/离散codes，Ch24 19–31生成factorization交接与Ch66 265–294内部sensor/解释工具边界。Ch23原残余dropout控制的是codec重建旁路，不承载监督概念坐标携带类信息与读出容量共同优化的具体接口；Ch66已有测量资格不拥有训练表示机制。soleMULTIMODAL-REPRESENTATION。拟在Ch23 stitching两段后/多语言map前，仅两段及静态source注，待非准备者Source/PRE与root ownership授权。

若消费者需要可命名、可人工纠正的属性，encoder 表示还可先映为一组监督概念坐标，再交给分类读出；直接使用完整 feature 更灵活，而概念瓶颈换取可读接口，也会让任务优化把额外类信息藏进细小数值。一个受限训练分支用可微密度估计，使每个预测概念与标签的互信息接近其监督目标的对应值，并把线性读出改成可学习的逐概念一元响应之和，减轻有限读出容量对概念层的压力。它联合约束概念检测与任务预测，不把互信息接近认证成语义相同，也不由单轴代理签联合瓶颈完全无泄漏。[f-CBM 的必要对照](https://arxiv.org/html/2603.13163v1)支持这条接口，而非任意多模态消费者的通用解释保证。<!-- source-family:SF-2026-ARXIV-2603-13163 -->

概念目标、encoder、读出函数与介入顺序应共同版本化；自动相似度注释不是人类语义真值，验证集选过的概念纠正也不等任意逐样本修改都有效。有限对照仍有概念误差、任务和泄漏代理的反向取舍，较低的边际互信息不能排除概念组合中的任务信息；须分验概念准确、完整消费者输出与实际介入回归，而不只看曲线是否容易命名。概念制备、密度估计、两 encoder、联合训练及独立介入验证均付费。概念集不足、数值估计退化或纠正损伤任务时，保留独立概念监督、线性读出与完整 feature 路径，明确其可读性代价，不以“faithful”标签批准部署。<!-- source-family:SF-2026-ARXIV-2603-13163 -->

静态源注：

[^src-fcbm]: [f-CBM](https://arxiv.org/html/2603.13163v1)（2026-03-16，exact-v1）。必要审阅§3–6/Eq1–7/Tables1–2；仅采用概念检测、逐轴信息代理和读出容量共同训练的受限接口，目标/介入与表格反侧保留，不授语义纯净、完全无泄漏或普遍性能，未核artifact或复现。

## root 独立 Source/PRE（2026-10-11）

实际打开精确 v1 §3–5/Eq1–7/Tables1–2与介入协议，核对自动概念目标、逐轴平方差代理和 additive 单层读出；实际顺读 Ch23 专用 encoder/projector→stitching→共同映射局部。PRE 对目标信息与语义、边际与联合信息、可读与可介入的区别成立；表内反向取舍不被 headline 覆盖。两段只补监督概念接口，不把原残余 codec 或 Ch66 测量职责迁来，前后可以连续进入另一映射分支。受限 Source、两逐字 PRE 与本人静态注通过；授 resume_mar17 Ch23 窄写，实际非writer POST 前不计整合。未视觉核 Figure 趋势或核代码，不授 faithful 保证。

实际非writer POST：root 顺读写后 Ch23 69–87 stitching→新77/79概念接口→原多语言map的完整局部，以及章末含本人静态源注/Camera邻注。仅多合法脚注引用，实际两段与已核PRE相符；语义与互信息权限、联合信息、目标/介入反侧及费用/回退未丢，原文有效路径保留。正文与本人注回对原证通过，释放Ch23窄锁；可归并一项实际整合，不预授整日DAY，不追加身份尾注循环。
