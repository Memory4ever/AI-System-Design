# MetaKE12677：必要原证与中心桥定点争议

仅本17补03/16，准入/日级实体复用。resume_mar17实际读取[exact-v1 HTML](https://arxiv.org/html/2603.12677v1) §3–6/Eq1–10/Algorithm1/Table1、Appendix A与B.1–B.3；必要数学核回[同v1 PDF](https://arxiv.org/pdf/2603.12677v1) p6的β趋近1主张及p12–13的投影变量推导，避免把HTML转换误差当论文错误。2+1+2=5，具体target→solver反馈与理论反侧深入；未核artifact/复现，独核待做、不授safe。

## 支持与评价边界

FFN线性关联近似下先在activation中拟合target、再用old-key covariance/ridge约束权重执行，两目标不必一致。Eq7用最后层的固定key/covariance预计算row M，虚拟权重 W_L+(v−W_L k_L)M，meta目标含编辑NLL、locality输出KL及target到init距离；Algorithm1先15轮virtual更新target，最后另用multi-layer solver执行。它是近似单层反馈而非完整多层solver unroll，也不是线上模型知识数据库事务。最小方法差额可表述为先把拟写target经具体执行proxy再看输出，但不能由此预支可达性保证。

Table1只有ZsRE、GPT2-XL/GPT-J/Llama3、单A100、2000随机编辑/batch100、Adam meta15步/lr.005。GPT-J specificity的MetaKE29.43低于MEMIT31.42，三个指标非全胜；主文称five但只列three，不扩成五指标/多benchmark验证。Table1给±但重复数/seed及量含义未充分披露；precision、context/token预算、concurrency/tailSLO、定位/covariance/初始化target/15次虚拟forward-backward/最终solver及held-out回归总费用未披露。没有支持last-layer dominance、跨层drift、allocation近identity和α的数值表/独立消融，文本称empirically observed不替代实际测量。

## 具体中心反侧（本轮分析，不是作者实测或实现必错）

1. B.1 Eq18–24的单键闭式解为 Δ*=δM、δ_real=βδ、β=γ/(1+γ)、γ=kᵀ(C+λI)^−1k。固定k/C/λ时β不依赖输出target δ的方向或大小；§5/p6却说调整v使β→1。选择k=(1,0)、C=diag(99,1)、λ=1即可得γ=.01、β=1/101，任意旋转非零δ仍同一β。可提高最终NLL不等于上述β自动解除。输入key空间的谱约束与output target空间不可直接同轴；Mᵀ给output-gradient加权合法，但不是对output向量按C特征向量投影的证明。
2. B.1.4 Eq28–31把B=ΔP变为无约束B的ridge problem，遗漏BP=B这一可行域。P=diag(1,0)、k=(0,1)、δ非零、λ_iso>0时原ΔPk恒0，而无约束Eq31给非零Bk；因此称canonical Δ*=B*P不能满足Δ*P=B*。Eq34用||k||和Eq35用||Pk||也不能对一般P称同一系数。PDFp12–13确认原文如此，不是转换错误。不能继承AlphaEdit specialization的普遍执行/保护保证。
3. Theorem3的descent有last-layer dominance ρ<1、相容维度跨层C/k近似、allocation Jacobian近identity及nondegeneracy α>0/误差<1等额外条件，不由spectral consistency口号自动成立。B.3局部可在这些假设下给proxy误差界，但不修复前两条或证明实际AlphaEdit的15轮全部有效。Eq6直接依赖v的meta regularization还须与Eq8只列solver链路的梯度口径分清；Algorithm1写g=∇v L并未给具体实现，本轮不认证遗漏项的实际recipe。

当前[官方事件页](https://arxiv.org/abs/2603.12677)显示v3改题名/37页9图，[v2页](https://arxiv.org/abs/2603.12677v2)仍同题名/17页2图/work in progress，未给具体上述纠错映射；版本号/题名变更本身不授重要修订或修复，不无差别重读晚稿替代本窗v1。

## actual owner与拟处置

实际Ch16 250–290知识关联→rank-one recall/多跳/locality分验→MLP不必逐条事实→MoE及300–338交接，Ch15/17开篇，Ch29/30定点知识编辑/adapter搜索均读。唯一MODEL-FFN能承载target/权重执行差额；现263主要已覆盖recall与多跳访问分验，尚无这个具体反馈回路，不以主题相似假NC。但中心几何/投影桥未闭合，不绕其认证摘写正面Books段落。本轮拟保留5分候选，中心争议隔离、无Books、独核待做。

只请求一次：作者给固定/重算k,C及target更新到β变化的实际数学/最小trace；带BP=B的projected solver正确推导或实现与本窗实验映射；实际proxy→完整多层梯度的上述条件/测量以及完整meta-gradient定义。可接受受影响exact-version修正或对应实验commit的最小trace，不泛求整仓库/全部版本/附件。到达前不作正面理论/执行可达性/公平性能或Coverage保证；材料到达只重开12677受影响命题。普通未读与本中心争议严格分开。
