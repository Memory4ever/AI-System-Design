# 13069 PIFS：必要原证与中心桥（待独核）

仅本17新增03/16自然日；作者resume_mar17。原完整题摘、日级夹证与准入复用SUP_AB_MULTIMODAL/SUP_DATACITE_MULTIMODAL及独核对应记录，不追公开时分秒。精确题名 Fractals made Practical: Denoising Diffusion as Partitioned Iterated Function Systems，采用[exact-v1](https://arxiv.org/html/2603.13069v1)。当前[官方事件页](https://arxiv.org/abs/2603.13069)实际header/完整AB/history只有v1，未见本页撤回/纠错信号；不冒称全网无勘误。只审确定性DDIM，不扩Flow Matching附录或新发现。

## 必要读取与潜力

实际HTML §2 DDIM Eq4–7与PIFS定义、§3 Theorem6/9/Corollary8/11、§3.3 Theorem13–15、§4 Theorem16/17/19/22/23及直接证明、§5 Eq43–50/Theorem25–27、§6.1/6.2/6.3/Theorem32、§6.5.3/6.5.4、§7.1–7.7/Tables3–11及§8结论；不冒未读§6.5.1–2/全部附录或图像像素。决定性同v1 PDF原文p9 PC/Cor11、p16–17 release符号、p19–20 hard attention、p33 SNR再校对，与HTML一致；截图cachemiss，不冒视觉读取或访问整稿受阻。未核代码/复现。

潜力不是按fractal主题映射：连续/平均score误差解释→逐patch对角与跨patch Jacobian分解、schedule阈值→局部收缩/采样步预算及导数资格需分别检验。保2+2+2=6，理论与设计反证必要深入，不借成熟Banach定理抬分，不因中心疑点EX或降分。

## 支持的条件分支

Eq7 Jacobian为aI+bJnoise，b<0。Theorem6要求C1各点统一下界及残差界、C2标量项非负；不能仅算schedule-only L*即认证实际网络收缩。Theorem9/PC以完整对角块operator norm和所有跨块norm行和控制block-max norm，Cor11明确全部steps满足时，整条映射重复迭代收敛到唯一固定点。Theorem17 f_t只限block-diagonal Gaussian、perfect score；现实抑制S要测网络导数，不是schedule独立真值。§4.3训练到MM明确A1–A3 heuristic，不是一般DSM保证；注意保留该作者限定。

## 中心争议（本轮分析，不说作者实测或代码必错）

- **PC/吸引子身份**：PC是全空间block-max收缩，全部steps满足仍意味着单个固定点/零维吸引子，不能由“仅patch”获得正维数。Cor11与§5.1“PC恰可正维数”缺同一对象桥；不否定允许部分steps不满足PC后的其他可能性，但该分支需要新的稳定/不变集合证明。Th25 Gaussian乘积大于1的线性方向，原点是排斥方向，不自行构成有界吸引子；单次noise→image与反复把output再当noise迭代Φ不可混同。
- **方向到norm/全谱**：Prop19只证明沿指定v的Rayleigh quotient<1，不证明block operator norm<1（条件例diag(.5,2)，v=e1时.5而norm2）。§4后续把同符号用于方向值和norm，再以top方向值重复n_k次及forward marginal平均log替完整固定点轨迹Jacobian谱，现实非Gaussian/crosspatch未证明该替换。有限signed-Rayleigh测量不等真实Lyapunov全谱。
- **hard attention反例**：Th23(d)任意winner j*(k)在τ→0推出cross=0不成立。两scalar patches取WQ=WK=WV=1、FF恒等、p=(1,2)，query1唯一选择patch2，远离tie极限Jacobian d output1/d p2=1，故DDIM跨块为b≠0；只有winner=self等额外条件才可能去掉这种跨patch值路由。原式41保留A_kℓ Wv项。此为解析条件例，未运行paper实现。
- **release/SNR字面冲突**：MM2写∂tγ<0而反向链t递减，不能同时称γ沿反向下降；Th22(a) trel低方差更大，与(c)∂trel/∂λ>0相反，(b)区间起点大于终点。Prop34说high-noise高SNR、小t低SNR，违背自身SNR=αbar/(1−αbar)且αbar随t减；clamp乘γ/SNR≤1不等raises该项。Th35自定义difficulty=1/L*的minimax可作为设定问题，但固定ν/δ时L*较小反而放宽C1，不能将这个定义当实际contraction workload/AYS误差最优已证明。保留局部公式，不认证统一设计最优解释。

## 评价、反侧及费用

CIFAR32 pretrained google/ddpm-cifar10-32、8×8 patches、50step DDIM、JVP/VJP power迭代20/10/30次与4/5/7seed人口不同，seed8因极端3386排除；50k训练图估cov。T3只测S与λ的rank正相关，不证明MM1的∂S/∂λ>f′或MM2；有限trajectory点不证全x supremum。T5 fine t20 diag1.211/cross.186与§7.5/T8 fine diag.991–.995/positivePC不同，需protocol映射；T8 t40 mean.006412<min.006518字面不合。T6熵/耦合反向相关且cross随定位增长，不能当attention-localization降低coupling因果。§7.7 Celeb256 checkpoint在64²、200图cov、8trajectories/20t插值到49step，预测负指数与signed proxy同号不是完整谱/真实分布维数验证；末段又称CIFAR λ低于λ**，与前18.7–44.4远高于约1.05矛盾。不借单符号细节否定全部局部观察，但统一中心经验验收未闭合。

推理hardware/precision/batch/concurrency/tailSLO/全部诊断及拟regularizer训练费用Not Disclosed；耗费JVP/VJP、cov估计、插值与实际score求值，model-free只限部分schedule/Gaussian公式。理论不机械索求所有performance配置，但不能授免费诊断/新sampler效率/普遍生成质量或多样性。

## Owner与安全处置提案

actualCh24 356–369完整离散迁移→模态边界几何→Jacobian资格→解析reference flow已实际顺读，开头生成责任及Ch25 1–22观察/预测边界也读。唯一候选MULTIMODAL-GENERATIVE-PARADIGMS；现文具体覆盖“函数/导数/solver分别验收”，但不承载新的PC维数/attention统一桥，不能虚NoChange。中心争议先安全隔离、无Books，不绕争议写一般收缩原则。不授正面Evidence/Coverage/性能或维数保证；仍待非作者必要原证独核，未计safe/DAY。

仅请求一次正式局部修正或同实验最小trace：界定Φ重复迭代的吸引子/PC成立区间，给方向代理→norm/完整谱的条件，修正任意winner与release/SNR桥，并交代Tables5/8及CIFAR阈值身份。接受精确修订证明/必要配置原表，不求全部代码/附件；到达只重开本family，普通其余未读继续。
