# 2603.09571 — 必要Source与中心等价反例（root独核通过，中心Disputed）

[An Optimal Control Approach to Transformer Training exact-v1](https://arxiv.org/html/2603.09571v1)。第一包准入/当前唯一v1、公开日03-11BJT夹证已经review_mar12实际独核，SUP_EXACT_FIRST.json保留；current无已见撤回/纠错或accepted先稿信号。拟评分2+1+3=6，中心理论冲突触发受影响内容深入，不为中心不成立降分/改EX。作者实际必要读取§2全、§3.1/3.2可见定义与compact前提、§3.3/3.4全、§4三重量化构造/规模/算法前后与nearoptimal命题，§6/7全；§3/4初次大输出有截断，已对决定性§3.3/3.4完整恢复，不把截断或取回算全稿审阅。§5/无关附录的全部证明未读，不采用其普遍稳定/泛化结论。

## 支持的窄结构与条件

§2 Eq1定义固定宽度、单head、FF+全序列attention的简化Transformer dynamics，不含任意LLM残差/Norm/causal模型实现验收。位置作为(p_i,x_i) superstate保留，shared weight是layer的action，所有token和训练样本共同被centralized controller消费；不是每token自己选weights。§3.2要求particle状态S与action U compact，norm-bounded权重只解释一种约束选择，须保证实际动态在定义状态域内；有界数据本身不自动保证所有层hidden state有界。

§3.4利用deterministic flow，把已求得的closed-loop policy沿训练初始分布展开为固定每层U_t。这个展开支持训练分布依赖、部署realized-input-independent的权重，不是新输入运行时重新求feedback weights，也不是对任意新输入都最优。它作为结构分工可独立理解，但不修复下述cost等价。

§4分别离散S、probability simplex与U；单measure grid规模为binomial(ell+|X_n|-1,|X_n|-1)，K数据ensemble再取乘积。理论有限不等于工程可行，源码/实现未核。原三重量化near-optimal相对于其lifted Wasserstein objective，不可在位置等价失败时授原按位置MSE训练的全局最优。

## 决定性反例：Theorem5的lambda界不能强制同位置匹配

精确§3.3 Eq13/14采用平均W_{2,lambda}平方cost，点对cost平方为|x-y|²+lambda|p-q|²。Theorem5/紧邻Assumption3.3写lambda > (N/2)diam(S)²，并直接声称最优permutation必须identity、故lifted objective等价OP按位置MSE。原证明把一个上界当成强制配对依据；无需泛化实验即可定点核。

作者反例（非作者仍待独算）：S=[0,1]、N=2、K=1、T=1，p=(1/2,1)，initial x=(0,1)、target y=(1,0)，lambda=3/2满足原界lambda>1。取compact action space为单元素U=(W=1,A=1,b=0,Q=0,K=0,V=0)，ReLU在S上令Eq1恒等，S闭合，因此唯一terminal仍(0,1)，原OP最低平均MSE=(1+1)/2=1。同位置coupling的cost亦1；交换两token的coupling保留feature完全匹配，其平均平方cost=((3/2)(1/2)²+(3/2)(1/2)²)/2=3/8=0.375。故lifted minimum至多0.375<1，identity不最优，并且singleton action使最优值本身也不等；不是仅比较某个非optimal权重。该反例符合compact/共享权重/固定位置前提。不能据此说所有条件下DP不存在最优，也不由作者自行发明修正lambda界替论文证明。

## 关键评价与停止边界

§6 toy：二维[-1,1]序列N4、T2、ReLU、beta.5；35train/15test，拟合identity-weightattention生成函数；state n10/measure ell20固定、每次加10 sampled actions/10→100。不是完备action网格误差证明，不是语言模型任务或与GD matched对照。test在20action .00737→30/40 .01171反退，70–90 .00363→100 .00384再退；training .01561→.00460不能说明有限test单调。runtime6秒→6分43秒，未披露hardware/precision/重复/CI，不把其有限T2拟合quadratic时间扩为任意N/K/d/T复杂度。§7明确not scalable solver、not competitor to gradient descent，摘要“globally optimal robust alternative”必须收窄。

此处支持与直接反侧已足以决定中心采用，不再读无关附录以拖延定点裁决。Books暂缓：`TRAIN-PRETRAINING`拥有训练参数求解选择，中心cost等价/原训练nearglobal主张Disputed隔离，不进入Books正面证明；fixed-weight展开不据此单独制造两段常识diff。恢复仅需作者修正可核的position-cost等价条件/证明及依赖Theorem5的后续结论，不需新速度数字或全文重复。root已实际核exact-v1 Eq1/2、OP平均损失、compact S/U、Eq13/14、Theorem5及紧邻Assumption3.3、Theorem7范围，并独立用有理数枚举identity=1/swap=3/8，确认singleton动态闭合；必要Source与中心Disputed处置通过，不授全部DP不存在/全部附录错误。以上“待核”字样保留为提案阶段原记录，不代表当前未核；未写Books、不授DAY。
