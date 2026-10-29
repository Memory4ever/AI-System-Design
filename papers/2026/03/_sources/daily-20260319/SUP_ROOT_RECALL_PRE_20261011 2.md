# RecallTheory 15923：必要原证与受限 PRE

只处理本19既有准入家族，root独立准备；完整题摘/公开日夹证复用本日原件，不改旧日期或扩发现。2+1+3=6只给随机非正交表示下有限样本、上下文长度与检索学习的耦合，不给通用LLM容量律。发现HTML同v1路径的封面为August24，PDF同v1封面为March18、arXiv页边标2603.15923v1/16Mar；本包采用[精确v1 PDF](https://arxiv.org/pdf/2603.15923v1)必要正文，不把HTML的不同内容混进当窗证据，不展开全版本差分或全75页。

## 实际必要范围与采用边界

实际PDF§2/Eq2.1–2.5、§3/Assumptions1–3/Theorem1/Eq3.1与Theorem2、§4.1–4.3/Figs2–7的文字设置、§5关键signal/noise证明思路和Appendix E/Theorem4的观测接口。没有读取全部浓缩不等式证明或代码，图的精确像素/斜率拟合未独立重算；截图工具未能解析，不据失败称看过图。采用的是文字明确的模型与定理限定，不依赖精确拟合数值。

输入为均匀独立词、均匀informative位置、随机置换标签；informative位置由外给trigger方向标记，模拟上层已经完成标记，不证明模型从原始语言自行发现证据。输入/输出高斯embedding固定且独立，一头attention后接线性或随机固定MLP；只训练value与KQ，零初始化，三步value→KQ→value，小首步/大后步。容量条件与学得出分开：Attention-only d²够容纳词表、MLP md够容纳词表仍不是有限样本成功的充分全部条件，Theorem1要求检索信号压过估计波动、非零均值偏差和MLP噪声；N、d、L、m及V共同变化。Assumption1有L=V^c,c在(0,1)、N至少V log V且小于VL；多项式激活非零局部导数、Hermite/宽度条件不自动认证实际GELU/SwiGLU网络。

正文的lower bound不是所有Transformer学习器下界。Theorem2限定初始化attention输出/二阶量的带噪观测；Appendix E进一步给出含测量噪声的mean/covariance与label接口，Theorem4的0–1损失是整张置换精确恢复，不等于一般token平均accuracy。原文上下界不匹配，不能用此签发任意原始数据算法或训练轨迹的固有最优率。此中心“intrinsic”外推不采用，保留受限充分条件与明确接口；若要采用平均召回率普遍下界，需要具名转换证明，不因未采该外推而排除本篇局部机制。

实验是上述合成任务；三步MLP用0.7h2+0.3h3、m约d²或d³，受成本限制只探部分regime。多步Attention-only改为Adam、attention/output layer norm、LR0.005、batch约N/2（另N/16）、16epochs；迭代与batch改变容量拟合指数，直接反驳把早期条件写成固定全训练常数。主要斜率与图不能作为accuracy趋近1的有限样本证明；硬件、数值精度、完整预算与多次置信区间未在已读必要范围明确披露，不授训练部署成本、事实正确性或生产保证。归一化可能缓解mean bias是待研究解释，不给出已证因果修复。

## actual owner 与差额

sole `MODEL-SELF-ATTENTION`，actual Ch14完整197–266：短路径的表达、构造性featurizer、可解码/控制权及目标blind direction均已说明，未拥有“表示存储容量满足但随机几何＋有限样本＋干扰context使寻址学习信号不足”的具体条件。Ch12 225–278已有稀有token训练支持与表示容量一般边界，不重复作为第二owner；Ch13位置标记与Ch15多head开篇已读，当前只增Ch14学习边界中一段，避免把实验当Ch12新宽度最优处方或Ch28学习率recipe。

## 逐字 PRE（待非准备者，未授写入）

训练目标能提供梯度以后，还要区分“参数容得下这些关联”与“有限样本能把检索路径学出来”。把不同词放进非正交表示，可以在有限维度里承载更多关联，却也让干扰token的相关性进入寻址梯度；在[受控单层召回分析](https://arxiv.org/pdf/2603.15923v1)中，即使参数满足存储条件，作者给出的受限充分条件仍要求检索信号压过样本波动、均值偏差和读出噪声，所需样本、表示维度与干扰上下文长度因而耦合。它预先给目标token加了trigger标记，固定随机embedding，并分析特殊三步更新，不是大模型通用容量律或“加宽必能解决长上下文”。加数据、增宽或缩短干扰context各付出采样、参数与训练成本，增加MLP宽度也未必减少总参数；多步Adam和归一化对照又会改变早期拟合尺度。实际模型不满足这些条件时，应回到预算匹配的检索测试和训练支持度检查，保留短context、显式检索及原模型路径，不由表示容量或全局可见性认证可学习性和答案真值。<!-- source-family:SF-2026-ARXIV-2603-15923 -->

静态注：`SF-2026-ARXIV-2603-15923` — [v1 PDF](https://arxiv.org/pdf/2603.15923v1)§2–5、Assumptions1–3/Theorems1–2及Appendix E观测接口。仅有限样本/非正交表示/干扰context的受限学习边界；trigger外给、三步更新、固定随机embedding与多步尺度变化保留。不采任意LLM容量律、所有算法下界、精确参数最优或生产成本；未核代码/复现，HTML封面与PDF不同，本次只采PDF必要证据。

## 独立 Source/PRE 与 actualPOST

resume_mar17实际v1 PDF §2–5/Assumptions1–3/Th1–2/AppE Th4及actualCh14 195–266/Ch12支持度/Ch13–15交接，定点将必要性措辞修为“作者给出的受限充分条件仍要求”后逐字PRE通过。非preparer另实际看必要p1/4/5/6/9/59，不重拟合全部图；整置换0–1不能转平均token正确率（只交换两标签即失败而平均accuracy可1−2/V）反侧隔离。root窄写新260及静态注647并自读后，resume_mar17非writer实际完整244–285/本人末注与相邻两注回对原PRE，限定diffcheck通过；actualPOST通过，Ch14窄锁释放。不授本日DAY，不循环改Book注人员身份。
