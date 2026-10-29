# 04485：收窄分析事件必要Source / actual owner / 最小PRE

最新行政事实：reader R87–88已实际完整采用，LiMiX唯一actualPOST通过，真实整合生效/指定Ch12窄位释放；累计新增I18＋旧Kimi1合19。本文此前待PRE/待POST为过程时态，不重做有效必要层或技术正文。DAY尚未通过。

作者supp_20260605_author，仅2026-06-05补Jun04。已实际读回reader R83–84：收窄事件准入通过；R34 Jun04精确v1联合日证有效复用。旧2M release、RBF、hard exponent/perkernel amplitude gate及smf排序去重不再评分。原件、当前notice无撤回信号、早README/代码/PDF与Oct/Nov日期冲突均保存在[事件包](SUP_LIMIX_EVENT_DELTA_20261025.md)，不第三恢复/重GET或扩同家族全史。以下首次必要层不冒已获reader批准。

## 精确原域和采用范围

官方exact-v1原件`SUP_2606.04485v1_20261025.html`，897422bytes，SHA256 `0190c4c8e4409645456ff9a72f9fa8def5662c2b9be087c8b4cb684a647414df`；https://arxiv.org/html/2606.04485v1 。当前notice `SUP_2606.04485_NOTICE_20261025.html`同事件包，不借v2/接受日期。前阶段必要读取有效，本阶段只补核实际§B.2 Theorem B.1、§B.3 Proposition B.2全部证明/解释、§4.2 Eq1–10与§5.1–5.2 T2–5/C.3关键消融；支持与直接反侧已足，不读全dataset表、全部引用、后版或复现。

### 共享仿射、归一化和attention的三个不同对象

§B.2 ThmB.1：固定feature j，pre-LN为z_i=wx_i+b；跨样本居中精确外积Ztilde=(x−mean(x))w^T，故rank≤1（w或居中x为零则rank0）。在LN之后再加、只依赖列j的a_j，会在同feature跨样本居中时消失。这里不是证明ID无用：列身份仍可区分列；也不是任意把ID放入LN/非线性内部的结构定理。离散词表ID本来不应当有数值顺序，不能把该数值tokenizer建议反套为直接投影词表编号。

§B.3 PropB.2假设固定LN gain/bias，centered w和b记u/v，LN(wx+b)=beta+(Dgamma*u)x/sigma(x)+(Dgamma*v)/sigma(x)。因此同一feature的归一化token位于固定至多二维affine子空间，不是归一化之后仍rank1；单scalar的曲线参数维与有限点云matrix rank也不同。线性V投影保留该affine形式，归一化attention权重和为1使公共offset固定，每head的输出变化至多在两个方向上。H heads输出投影后，每个输出token对N个该feature数值的d×N Jacobian K_tj有rank≤min(d,N,2H)。其证明不要求attention权重常数，但要求这些token仍是同一feature的上述输入、normalized加权和与固定线性V/output，不借完整残差/FFN/跨feature模型。

原文堆叠所有位置的Nd×N Jacobian给≤2HN；其自然界已≤N，故这个较松界本身不证明全局低秩/全网宽度冗余或整模型瓶颈。纯串行下游的Jacobian乘积不增rank，不等有旁路/residual、跨feature输入或变架构后仍可套同一全网络定理。§3/Appendix A无positional条件的纯affine/attention rank界另有假设，不混为有ID且带完整block的统一界。本文强解释“宽度必然无用”不采，只保在该入口和第一层每输出上增加width不自动扩大数值变化方向的条件。

### 新数学分支不是旧artifact的实证签字

§4.2 Eq1–4按列zscore→localized RBF bank→共享线性投影/LN；可学习center/width由quantile/local variability初始化。Eq5–10以bounded log2-magnitude bins soft assignment＋sign embedding，经小MLP/Softplus产生每cell两个positive shared scalar，分别缩放全部centers和widths。区别事件包已核旧hard floor(log10)/逐kernel gamma-beta调幅，不能把旧artifact、权重或同名模型实验称为已核新式实现。有限bins、tau offset和自由bin embedding没有给出严格scale-equivariance恒等条件，原文对此强称不采；sign变化处也不由soft magnitude assignment自动取得全实轴可微保证。

这是本文定义的受限输入分支，不是宣称RBF本身Jun04首创。非线性basis可让跨不同数值取样的向量不再局限原affine直线，但标量仍是标量，不增加输入信息或自动增加语义自由度。拟正文不需要新门控实现或benchmark归因才能成立；仅介绍数学选择及独立验证责任。

### 关键对照、代价与直接反侧

§5.2称同2M/SNF/相同训练配置只替tokenizer，T5前三层numerical rank58.41→78.62、rank99 13.94→25.35、rank95 6.73→12.31，为作者有限诊断，不是每层/每feature/Jacobian的同一定义，也不认证无损、task quality、gate因果或速度。T2有MLP/Periodic胜出任务，T1截断rank5明显质量退化；不采通用优越、宽度均可删。§5.1 MLP与小Transformer的局部收益不能由此归为所有新gate而排除初始化/训练recipe影响。

C.3 Table8宽度32比16/64好、Table13 fixed sigma优于learnable，Table12 uniform优于random，与§4.2 learnable/local-init主说明不构成单一完整已核recipe。Table11 orthogonal的AUC89.03但其他指标变化有限；不补成统一最优配置/统计显著。旧代码和新定义不同，不能用这些消融填补新式实现身份。比较需要绑定归一化拟合人口、missing/outlier处理、bin范围/temperature、center-width及checkpoint；原文未全披露的记Not Disclosed，不能自行修复。

全部basis、bin权重、小MLP/投影、训练和搜索有额外费用；per-column统计不能默认可见test真值或任意未来数据。完整预训练总费/precision/ensemble/cache时点等未全披露。C.6仅synthetic900×60、EPYC9354/RTX4090、三run均值，不签线上SLO/普遍加速；本正文不采用时间/榜单数值。质量需在匹配人口/预算下独立验，不能由rank读数自签。该数学分支可在实现未核情况下安全解释，不需要扩完整代码/后版补齐才能继续。

## 正式5分与actual owner差额

Design Delta2＋System Reach1＋Durability2＝5：新增针对数值输入的条件化value-rank/局部敏感性分析和数学接口分支，改变只加宽/只加列身份即可解除入口限制的设计判断；单模型输入组件，不把整个表格系统/跨层联想计Reach，不把旧RBF/SNF/榜单再计贡献。因实际长期缺口深入受影响条件/反侧，不为了工作量降分或造全网络定理。

actual owner `MODEL-EMBEDDING`，Ch12。实际读本章18–59 ID/lookup，225–281输入宽度/精确升降维/ALBERT/多来源压缩/Leviathan两完整段，375–387维度读数与能力区别；邻Ch11/13实际开头与交接，Ch14只检相关主题位置，不冒整章已审。ROADMAP和三Books上下文已重读。当前已覆盖线性EP rank与非线性生成离散ID、不让rank代能力；尚缺连续数值的value变化与列身份分责、LN前/后条件和第一层每输出敏感性界，非主题相似即可NC。最小两段可把该接口边界接在线性宽度取舍后，不在Ch14重复attention主线，不建新章。

拟唯一窄位：ALBERT完整验收段后、下一多来源表示压缩完整段前。完整上锚：

> [ALBERT 的 §3.1 与 §4.4](https://arxiv.org/html/1909.11942v6)提供因式分解设计与宽度对照实验，支持这是一条可行分支，没有证明普遍无损。验收应固定 tokenizer、数据与可比较的训练预算，同时比较 held-out loss、任务质量及稀有符号／语言切片，并把允许的退化范围与参数、显存、吞吐收益一起规定；压缩已有表时，重构误差只是额外诊断，不能代替行为测试。质量收益不足时保留较宽接口，checkpoint layout 与 weight-tying contract 也应随架构选择一起冻结。

完整下锚：

> 多来源表示的压缩还可先保留各自的子空间，而不是把全部坐标拼起后只做一个统一投影：分别归一并降维，再按来源权重缩放、拼接并归一，把每路维数与可为零的权重作为联合选择。[一个受限融合分支](https://arxiv.org/html/2507.06622v1#S3)对文本和两种知识图表示采用这种接口，但保方差的SVD不保证保任务充分信息，零权重也不证明该来源没有真实价值。维数、投影拟合人口、来源版本和下游consumer须共同保存；拟合与验证的隔离不能只凭保留train/test名字默认成立。原对照同时改变每路容量与总维数，局部得分仍有反退，不把收益全归投影顺序或称普遍无损。来源编码/图构建、压缩拟合、维数权重搜索与任务验证都付费；覆盖、质量或总成本失配时保留普通concat、统一投影或较宽表示，以独立任务评价而非更短向量签收。

## R85两处消歧后批准原两段（root新窄授后已SAVE，待唯一POST）

输入本来是连续数值时，还要把“数值怎样变化”与“来自哪一列”分开，而不能沿用词表编号的任意顺序。若每格标量都经共享仿射映射`z=wx+b`，固定列跨样本居中后的矩阵只是外积，秩至多1；在归一化后另加、只依赖列的身份向量会被这种居中消去，不扩大该列的数值变化方向。一个[受限表格模型分析](https://arxiv.org/html/2606.04485v1)进一步区分：固定gain/bias的LayerNorm使这组数值token位于至多二维affine子空间，第一层只沿同列样本、用H个头做归一化加权时，每个输出token对这些数值的Jacobian秩至多`2H`。这是入口与单输出的条件界，不是归一化后仍秩1、整模型全局低秩或宽度无用的证明；标量曲线维、取样矩阵秩和任务能力也不是同一量。

可以先把真实数值展开为多个局部basis响应，再投影到模型宽度，而不是只增加线性坐标；论文还定义按soft log-magnitude分箱、由每格两个正标量共享调节整组RBF中心和宽度的分支。非线性取样可改变输入几何，却不增加原始标量的信息，也不自动保证严格尺度等变、语义或质量更好。该数学定义与同家族更早公开的hard exponent/逐kernel调幅实现不同，不能由旧代码、同名权重或较高rank读数替新式签实现与收益归因；消融中固定RBF带宽又可胜过可学带宽，也不宜拼成唯一最优recipe。应联合保存列统计拟合人口、basis/gate和checkpoint，按匹配数据与预算独立验质量，并计全部展开、门控、投影、训练和搜索费用；分布、数值稳定性或净收益不合时，保留共享仿射、普通MLP或已验证的数值编码，不把这条连续输入分支反套成词表ID的有序数值。<!-- source-family:SF-2026-ARXIV-2606-04485 -->

## 当前停止 / 下一层

### 当前R85–86采用 / root新窄授后真实SAVE

已实际完整读回R85–86必要/5分/actual Ch12具体gap与仅两处消歧后PRE通过；未重GET或第三必要层。root本轮fresh双锚/ID核心/邻11与13及三Books上下文后明确新窄授，仅上述修后原两段插ALBERT完整验收段后/多来源压缩完整段前，加本人true-H2 Review notes一注。已真实SAVE，并实际完整自读新增两段、直接完整上下锚及本人整注。第一层明确定义H头；fixed RBF带宽非embedding宽度；其他逐字批准稿不变，旧模型事件去重及新式非artifact/反侧保留。

写前快照`/private/tmp/limix-0605-save.RFR11U/ch12-before.md`，SHA256 `ae9eea962d10409c6756d8340b3cb58d18d9f2cd93119df2c0b97021ae2bdad6`；写后SHA256 `fdcdd0346dfc134fdd01cc121c042c092f21c6d7d0a4ee01165c4887ef4c5403`。只逆除本新增两段/本人注后整章字节等于写前；正文family marker/本人注各唯一，注最近前置真H2为Review notes。该范围检查不代reader语义POST，原两侧/其他组/他注及并发差额完整保护。

当前仅待唯一非writer actualPOST，未预I，既成仍I18。本作者真实写入阶段ready即释放供独核；其后本日finite title stop/六节合并与完整DAY仍ordinary，不扩73/706/全史/全Methods、不改State/index。以下“首次必要ready”保留为本次SAVE前过程，不再是当前待办。

本必要层/5分/actual Ch12具体gap及原两段PRE准备就绪，交本日唯一reader首次必要/owner/PRE；无新Book授权、SAVE、本人注、POST或I，不预NC/整合。既成I18不变。有限官方相关标题stop与六节最终收束仍普通可执行，下一阶段只做这些实际停点，不扩73/706/全史或无关Methods。当前材料支持与直接反侧已足，停止追加附件。
