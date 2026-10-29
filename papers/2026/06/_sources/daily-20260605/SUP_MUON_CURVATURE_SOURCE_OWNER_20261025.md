# 04662 Muon曲率分析：首次必要 / 5分 / actual Ch28两段PRE

最新行政事实：reader R99–100已实际完整采用，唯一actualPOST通过/指定Ch28窄位释放，新增I20＋旧Kimi1合21。下列待PRE/SAVE/POST均为过程时态，不第三证据/技术正文或E，未授DAY。

作者supp_20260605_author，仅2026-06-05补Jun04。AGENTS/当前合同/Prompt、来源Daily/arxiv/恢复、ROADMAP/三Books公共上下文与本日停点已重读；R89–91完整题摘/收窄准入/精确v1 Jun04组合日证实际采用，不第三abs/DOI。当前notice无撤回信号有效复用。LazyAttention R94–95唯一actualPOST已行政采用，I20保持，未重正文/必要层。

## 原件与真正读取域

https://arxiv.org/html/2606.04662v1 ，GET200/823123bytes，`SUP_2606.04662v1_20261025.html`，SHA256 `dd9f5cfb3f68161f4fc09d177a567ffd9ff7aa1e89b2ee0ac9fb098799bd529b`。首次读§3更新定义/§4.1–4.4全部正文与F1–4文字/Eq4.1–4.2、§5.1–5.2假设/模型/定理陈述与5.3部分解释，A.1/A.2训练配置与B按步数对照。只采用§4局部诊断和其评价条件；§5仅限定其模型与Adam不适用边界，**未读足Appendix E完整证明，不采用Thm5.5的严格有限步优越结论/速率或完整recipe**。未看图曲线像素、全D矩阵拟合流程、代码/后版/复现，不为小诊断扩全附件。

exact04662/Lazy?已定点Books family身份检索，无04662同事件有效必要/owner链；相近Muon主题不能代新判断，也不以无marker认定gap。当前只本文一次score，成熟Taylor/HVP不是新发明。

## 拟采用的具体命题与反侧

§4.1对当前batch/参数W及实际更新Z，realized decrease=L(W)−L(W−Z)，二阶predicted=<G,Z>−(1/2)<Z,H[Z]>；二者近似，不是无条件等式。作者记录各optimizer自己的训练轨迹，在相近validation loss下比较，按相邻checkpoint线性插值；**不是同一个W/同Hessian上的配对干预，也不是相同步数/等墙钟**。Intro的same-iterate措辞不能覆盖实际protocol，不补“同点因果已隔离”。Muon predicted略小于realized，作者承认higher-order贡献未闭，不能把全部收益唯一归二阶项。

§4.2对非零Z定义NDS=<Z,H[Z]>/||Z||F²，因而二阶项=(1/2)||Z||F²*NDS。数学分解区分update scale与direction沿当前H的曲率，不证NDS是参数化不变/无条件非负或泛化真值，也不能丢一阶项和余项后按NDS单独择optimizer。所测F1–2一阶收益相近、update norm相近，Muon较低NDS解释受限二阶差额；loss-aligned Adam/Muon均值比1.76而Appendix B step-aligned2.94，不当两次独立验证同一个比较量，也不把插值当CI。Figures说明across seeds但A.1未闭完整seed数/误差区间，未补显著性。

A.1为124M NanoGPT/12层12head d768、GPT2词表50257、FineWeb10B/seq1024、4×A10080GB。Muon用于除embedding/lm_head外矩阵，momentum .85→.95前300步、5次Newton–Schulz、无decay；embedding/lm_head/1D仍Adam，baseline全部Adam β1.8/β2.95。两者LR grid {1,2,5}×{1e−1,1e−2,1e−3,1e−4}，HVP每500步。故Muon不是全参数同一规则；precision、完整主run步数/总train+search+HVP墙钟/seedCI未充分披露，不采约两倍全链训练性能或任何SLO。

§4.3/A.2另为9M NanoGPT（4层4head d256）、Zipf-PCFG语法/latent topic语料、词表4412、seq1024、有效8192tokens/step、10k步；train s=0/.5/1，validation固定s0。Muon矩阵LR.005/.95/5NS，其他Adam LR.01/.8/.95；baseline全部Adam .01/.8/.95。比值在Muon s0归一后Adam1.63→2.38、Muon1→1.25，差额.63→1.13只是这组训练人口的数据不平衡干预，不能授真实web语料或所有optimizer的重尾定律/公平收益。

§4.4分解全Hessian的within/cross项并以全更新norm²归一，不是每层分别归一可直接相加的比例。Muon within fraction约14%→44%，仍非过半，不把作者“dominant”解释成已经忽略cross项或纯block-diagonal Hessian。跨层贡献、checkpoint和完整更新必须保留；局部曲率小不代表旧能力/held-out更好。

§5理论为固定matrix-block二次近似、低Kronecker秩、共同正交eigenbasis、正曲率两组少数sharp mode、梯度同paired rank-one modes及组内常数/对齐等强条件；empirical拟合分数.892/.845、positive子空间捕获梯度.871不是精确满足假设。理论Muon关momentum/精确spectral update、两方法从0起/每步exact line search，比GD而非Adam；Adam仅toy近似相似。不能借定理为真实混合Muon/Adam、非凸训练或一般Adam普胜签字。本文不输出该定理保证，故没有为此扩整E证明；如果未来采用保证必须重开具体proof/非零更新域与实际recipe桥接。

诊断需要额外HVP、checkpoint/interpolation、优化器搜索和配对/held-out回归费用；matched loss不免不同训练时长/搜索预算，数据改变亦可改loss尺度。保原AdamW/Muon recipe并联合验真实质量与总成本，而非把更低曲率读数自签加速或泛化。

## 正式5分与actual owner

Design Delta2＋System Reach1＋Durability2＝5：新增更新尺度与局部方向曲率、validation-loss与step两比较轴的可检查归因接口及局部反侧，改变只按名义LR/步数/损失改善解释Muon优势的判断；单optimizer/训练组件，不按2倍宣传或成熟Taylor常识加分。因长期具体缺口深入受影响域，不机械扩大理论/附件。

`TRAIN-PRETRAINING` Ch28。实际读450–486二阶step实际位移控制/optimizer非参数化无关/局部surrogate/stability/geometry、LITE sharp-flat分支、Optimizer Recipe数据变换及normalizer交互；510–547basis/symmetry及理想margin-flow边界，邻Ch27/29真实开篇。现文有scale/state/参数化、数据谱与独立质量，LITE是用已有proxy改变flat drive/damping，并未具体承载非零实际update的NDS分解及loss-aligned不同轨迹的归因界。因此仅补局部诊断两段，不重写Muon算法/泛曲率主线；未以主题相近假NC，也不重其他来源必要域。

拟唯一位在完整LITE段之后、`### Optimizer Recipe 也包含数据变换`真标题前。完整上锚：

> 统一提高更新幅度在各方向压力相近时简单；曲率强烈各向异性时，一条分支从已有 preconditioner/gradient-covariance 提出 sharp 子空间，再在其正交补上提高 drive 与 gradient-damping 系数，而保留 sharp 方向较保守的参数。[LITE v1 §5–6](https://arxiv.org/html/2602.22681v1)的 Muon proxy 与 SOAP eigenspace/soft mask 不是精确 Hessian oracle，有限对照中 uniform 增大系数反而比原 Muon 更差；仅增强 drive 或 damping 也不等联合分支。连续 River/common-eigenbasis 假设不能直接认证 noisy 离散 LLM 更新，较少达到同 loss 的 steps 也不是同 FLOPs/总墙钟。投影近似、阈值、搜索和额外算术付费；方向失配、head敏感或质量反退时，回到原 Muon/SOAP 或已调 AdamW，不把局部谱分配写成所有层都可加速的保证。<!-- source-family:SF-2026-ARXIV-2602-22681 -->

直接下侧真标题 `### Optimizer Recipe 也包含数据变换`，其完整首段：

> 同名优化器在不同 augmentation、sample mixing、label smoothing 与 gradient spectrum 下并不是同一训练机制。尤其对矩阵型更新，收益可能来自优化器与数据管线共同改变的梯度几何，而非单独的 update rule。可复现 artifact 因此必须绑定 optimizer state、数据变换、loss smoothing 与谱诊断；收益是能解释 recipe portability，代价是实验矩阵扩大。数据分布简单且梯度谱稳定时，较小的 optimizer-only contract 仍可接受。现有比较只约束作者披露的 Muon 配方，不证明某一优化器在所有视觉或语言任务上更优。

## R96逐字批准原两段（真实SAVE及R99唯一POST已通过，以下原文不第三）

要判断较快下降来自“走得更远”还是“方向更合适”，还可以对实际非零更新`Z`分解局部预测：二阶loss下降近似为`<G,Z>−||Z||F²·NDS/2`，其中`NDS=<Z,H[Z]>/||Z||F²`把更新幅度与沿该方向的曲率分开。[一项受限预训练诊断](https://arxiv.org/html/2606.04662v1)在各自轨迹的相近validation loss处比较Muon与Adam，发现一阶收益和更新范数相近、Muon的方向曲率较小；按相同步数比较又会放大差额。对齐loss并不使参数点/Hessian相同，也不是等墙钟或同点因果干预；二阶预测与真实下降仍有余项，不能把全部收益唯一归因于NDS，更不能用较低曲率读数替代任务质量。

这项诊断同时依赖数据、参数组和测量预算：主对照的124M模型把embedding与输出头留给Adam，合成9M语料的不平衡试验也不证明真实长尾语料的普遍定律。层内与跨层曲率都参与完整更新，不能因某项占比增加就忽略另一项；固定二次模型的无动量/精确line-search及梯度—曲率对齐条件，更不能借作真实Adam或大模型的优越保证。应记录checkpoint、实际位移、HVP批次/时点、loss对齐与插值、数据分布及完整optimizer recipe，计入HVP、搜索和质量回归成本；近似失准、质量或净费用不合时保留已调AdamW/Muon及原schedule，不按单个sharpness proxy替换训练方案。<!-- source-family:SF-2026-ARXIV-2606-04662 -->

## 当前停止

### 当前R96–98实际采用 / root新窄授后真实SAVE

已实际完整读回R96–98：首次必要/正式5分/actual Ch28具体gap与原两段PRE逐字通过，无修句；R97两cue准入/date亦有效。root本轮fresh LITE完整单段/22681marker、直接真实H3/完整首段与唯一Review notes后新窄授，作者仅将上列两段原文逐字SAVE于LITE段后/Optimizer Recipe H3前，加本人true-H2注。完整新增、直接完整上段、下侧真实H3/完整首段及本人整注均实际selfread，Taylor余项/非同点因果、混合parameter groups、within-cross、GD理论不借Adam和全费/回退完整保留。

写前快照`/private/tmp/muon-0605-save.oQOwK1/ch28-before.md`，SHA256 `4127be98322c2feff47962cd949eb36e25f8d8297c55ef4924fa396e354c655d`；写后SHA256 `587019c36bb3d49d8a7069b803702e367de10c9420d2dfe413e2802688a74657`。仅逆除本两段及本人注后整章字节等写前，body family marker/本人注各1，最近前置真H2为Review notes。原两侧/marker/所有他注/并发差额保护，范围核不代reader语义POST。

当前R99–100唯一actualPOST已通过/指定窄位释放，I21既成；本人注/Report/本Source只行政同步，不第三必要Source/PRE或未采用的Thm5.5/E。下文首次准备/SAVE态为历史过程，不再是当前待办。State/index/他日不改，无stage/commit/push。

首次必要/5分/actual Ch28具体gap与原两段PRE ready，交唯一reader，不等其余六Methods；无新Book授写/SAVE/本人注/POST/I。I20保持。两cue04145/04581仅AB/日期校准请求见SUP_TITLE_STOP_BATCH4末节，04032仍跨日；不先其Methods、不扩NAV/73/706/他日。未stage/commit/push。
