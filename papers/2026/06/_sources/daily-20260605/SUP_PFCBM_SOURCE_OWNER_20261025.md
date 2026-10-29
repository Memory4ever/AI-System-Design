# 04364 PF-CBM：首次必要Source / actual Ch5最小PRE

最新行政采用：R81–82已实际完整读回，唯一actualPOST通过，真实整合生效/Ch5窄位释放，新增I17＋旧1合18。Report/本人注仅事实同步，不第三Source/PRE/POST；pending行按真实I转整合后实际V3通过。下方待POST为此前过程，不是当前待办；最后04485/有限title stop/DAY仍ordinary。

当前真实状态：R79–80已实际完整采用，必要/5分/actual Ch5通过，唯一T3修句后的原两段PRE通过。root本轮fresh明确新窄授后，两修后段逐字真实SAVE于compositional usefulness完整上段后/encoder消费几何完整下段前，加本人true-H2 Review notes一注；完整新增/完整直接两侧/本人整注已实际自读。当前仅待唯一非writer actualPOST，未I/DAY；下方未授写/待首次核为此前过程，非当前待办。

作者supp_20260605_author，仅Daily2026-06-05补Jun04。`SF-2026-ARXIV-2606-04364`，[Spatially Grounded Concept Bottleneck Models via Part-Factorized Attention exact-v1](https://arxiv.org/html/2606.04364v1)。R33–36有效完整题摘/准入与Jun04联合日证复用，不第三AB/date。**本次标题和机制均按v1**：不是发现摘要的后版Part-Factorized题名，也不是“prior不足、极少alignment loss才闭gap”。官方HTML GET200/188765bytes，实存`SUP_2606.04364v1_20261025.html`；SHA256 `15e4d1ebaf567e9f097fb00f557f8ca823ce62eeda7a75857d1fbc5656ecf298`。

实际必要读§3.1–3.5/Eq1–7/T1、§4数据/指标/实现、§5.1–5.5/T2–4与F2文字caption、§6限制。§1–2定位问题和与软OT/slot方法的区别，不扩上游原件、完整代码/历史/后版或全部refs。支持与关键反侧足即止；未核实现/复现，不把公开论文的forward定义当代码已验证。

## 机制：限制可读token，不把名字当真实部位

Frozen DINOv3 ViT-B16在512×512输入给32×32、N1024/D768 cached patch features。P12 named parts、C312概念、K200类、attention内维384。Eq1小MLP给whole-object前景g，不用per-part box；Eq2 logits为QK/√d＋log(g+ε)＋各part isotropic Gaussian log prior（μ、logσ可学，σ初值5，ε1e−6）。Eq3单头softmax加权V为part token、另算attention centroid。Gaussian与gate是soft bias，不是把其他patch从support绝对移除；这点直接来自有限logit/ε和softmax，而不是声称原文已做严格局部信息隔离实验。

Eq4 μ离线由训练集visible keypoint平均位置初始化，raw15 keypoints的双侧eye/leg/wing合并到12parts。它提供population级部位顺序先验，不是每张图训练/测试都用keypoint。v1把它解释为打破query置换/塌缩的对称性；初始化仍消费有标注训练图，不能称零keypoint来源/全无监督。训练μ继续漂移，平均先验也不保证每图姿态适合。

Eq5固定c2p map将293个局部概念直接copy对应part token；另外19个size/shape全局概念按softmax混合各part tokens，不是后版独立无prior global query。Eq6各概念独立线性head/温度τ∈[.5,5]/sigmoid，再线性class head只读概念概率。改变其他part token不影响该局部概念，是给定内部token上的readout结构性质；不等图像别处的pixels改变不会通过encoder/attention影响assigned token，更不自动证明该token取到了正确解剖/概念值真实。后一句是forward依赖边界的工程推断，不冒原文已用pixel counterfactual证明局部因果。

Eq7 concept certainty-weighted BCE、foreground BCE、visible centroid smooth-L1 alignment和entropy项加分类损失。PCA foreground target按每图中心相对边缘集中度选feature主成分并归一，只做训练target，推理仍learned gate。Stage1十epoch wcls0预训head，Stage2九十epoch分类/温度lr3e−4、gate/attention/head3e−5；低lr保grounding是作者解释，不能等同冻结grounding路径。Spatial-prior条件关闭per-image keypoint alignment，以dataset平均初始化代替；baseline保box+alignment，box-free另改foreground/features，不能把全部条件差额唯一归某一个模块。

## 评价人口与反侧

§4仅CUB-200-2011，约11788图/200类/312 binary concepts，train中分层留10%验证，native test。主配置seed0；keypoint-fraction sweep三seed、F2 ±1std，不把所有表当重复CI。Frozen backbone不在head训练/评价循环运行，是预先cache features/spatial side info；完整编码/cache/标注/所有候选训练费用仍在，不授免费foundation-model训练/服务加速。硬件/precision/完整time与内存、统计检验详情不全，Not Disclosed，不采用生产SLO。

T2 baseline top1 88.95/Point36.38/Dist1.074；spatial_prior88.85/52.57/1.042，box-free PCA88.26/59.16/.797，tight PCA88.85/59.74/.778；no_bbox_no_kp84.33/2.93/5.954，pseudo_kp85.04/10.78/6.704，tight pseudo86.71/21.40/4.603。局部结果支持分类/grounding分验，也保无identity退化和pseudo prototype可能学branch/fence背景，不能用分类高分认证部位。Routing始终开启，原文无routing-off等预算消融，不能把局部差额唯一归固定map。

§5.2 prior平均初始化用0.1–100%训练图，三seed，0.5%约27图起称与5394全训练图相近；“statistically indistinguishable”仅原文描述，未给完整检验/功效，不能当等效性证明。它测初始化subset，不是后版每图alignment loss的sparse-label训练。原文所谓去掉所有per-image supervision只指box/keypoint等空间信号；class/concept labels仍在，不能宣传无标签学习。正文/摘要还称PCA+Gaussian组合约88.6/70%point，但T2无同名70%行、T3相近configuration有不同口径，不自行对齐这些checkpoint/结果或造精确统一均值；本提案不采用70%数值。

T3同一表的joint312 top1 87.7、ECE.233/MI.697/Point60.2；sequential31276.0/.020/.323/64.3。112概念joint82.1→seq68.7、ECE.214→.041，显示分类/概念校准可相反变化，grounding不随classification同步。Sequential另加stage冻结grounding路径只训classifier；不是同计算预算或完全相同head优化条件。Random corrupt half concepts时seq1.4/joint68.2是受限观测，corruption精确分布/完整controls未披露，MI本身也不证明全部soft-score信息均非语义；只保soft概念概率可能携带binary标签外任务信号，不授“seq已绝无leakage”的普遍证书。

§5.3 per-part oracle edit经线性class weights传播，约−1到−1.2pt的所谓oracle gap/更快下降不证明概念修正必提高真实class accuracy，也不识别pixel级因果。Grounding指标是argmax距keypoint一patch内或centroid距离，不等完整part segmentation、全attention support、概念真值或人类解释可信。T4跨DOT-CBM backbone/DINO版本/标签接口不同，不能用较小ViT-B和较高top1独立证明固定routing普胜soft OT。§6仅单对象/较canonical姿态，isotropic marginal先验无part coupling，遮挡/elongated parts/多对象视角需另验；无spatial identity信号的去监督仍未解。

## 5分 / actual owner与最小差额

R79实际采用的必要限定：T3所谓sequential为在同一joint之后冻结everything except linear classifier、消费frozen concept probabilities；若同一checkpoint/概率/attention及test人口，单改class矩阵不能改变concept ECE.233→.020或Point60.2→64.3。MI对象亦未闭，不能自行补温度更新/不同checkpoint/前序训练或指标定义去解释。原表保配置关联和相反取舍，**隔离classifier-only冻结阶段已证导致概念校准/定位改善的因果与recipe**，不采genuinely constrained/完整消除leakage；不否定另有支持的固定consumer连接。Report与修后逐字PRE同保此限制，不重GET或借后版补原v1。

作者评分Design Delta2＋System Reach1＋Durability2＝5：固定concept→part读出结合soft foreground/population prior，是单模型表示与读出的具体结构分支，新增分类/空间支持/概念校准三层可分验的受限证据，约束长期可复用；不是按CUB指标/冻结大backbone/能映owner评分。因长期结构差额，深入受影响机制/反侧，但不机械扩全部附件。

重读AGENTS/当前研究及Report合同/Prompt、ROADMAP/三Books公共上下文、来源使用/Daily/arxiv/恢复与仅2026路由/本日停点。actual `WORLDVIEW-REPRESENTATION` Ch5；实际读93–109好的表示、176–210 inductive bias/shortcut组、364起证据阶梯及概念/局部consumer例、703–719标签非feature identity、558–586工程多层验收，邻4/6真实开头。现有语义标签/decodability/干预阶梯与shortcut监督边界保留；不因都是视觉放Ch23，也不在Ch66再造评价owner。

当前Ch5已区分可读/被用/可干预和局部support非真值，但尚未在“好的表示”主线解释：通过固定中间readout连接收窄命名概念的可消费token，与该token的空间grounding/soft概念校准仍是三层不同合同。最小两段拟第三项compositional usefulness完整段后/后续几何重建完整段前；不扩写模型百科/重新解释SAE，保原有表示及简单分类方案。

完整直接上锚：

> 第三是 **compositional usefulness**。中间特征应能被后续层组合，支持更复杂的判断。单个特征未必对应完整概念，它的价值可能只体现在与上下文中的其他特征共同计算时。

完整直接下锚：

> 后续计算需要的几何，也不一定就是预训练encoder原样输出的几何。固定encoder后，可以先对一组表示归一化，再以局部邻域映射重建较低维的消费空间，让聚类及无标签的簇数选择在这份产物上执行，而不是重训backbone；[受限图像对照](https://arxiv.org/html/2509.07184v1)中，原空间的聚类准确率较高，内部聚类指标却未必能选到较好的簇数。变换后的指标更有用，只说明该人口与消费任务的几何可能更合适，不证明真实语义类别被发现、信息无损或新样本也保持同样关系。拟合人口、邻域规则、维数、候选簇数范围与随机初始化共同定义表示产物；按内部指标选结果，与另用独立标签/真实任务验收是两份职责，不能让较大内部得分自行认证质量。编码、邻域图、所有候选聚类/搜索及外部评价都付费，预训练支持与选择先验也没有消失；人口变化、映射不稳定或真实任务质量/总预算失配时，保留原表示、可信标签约束或较保守的固定聚类，不把降维与漂亮二维图当成通用改进。

## 待首次独核的原两段PRE（未授写，非SAVE）

若中间坐标还被赋予人可读的概念名，分类正确就不再是唯一验收对象：相关的别处证据也可能预测对这个概念。一条[受限视觉概念瓶颈分支](https://arxiv.org/html/2606.04364v1#S3)先冻结encoder，由少量part queries汇聚patch，再用固定concept-to-part map让局部概念头只读取指定part token，最后从概念概率线性分类；全局概念另混合各part tokens。固定连接切断的是概念头读取其他part token的路径，不是证明指定token真的对应正确部位。软前景门和按少量训练keypoint均值初始化的可学习Gaussian prior能约束attention，却仍须独立验空间支持；概念命名、可消费连接与真实语义因此不是同一张保证。

这类结构保留可编辑概念接口，却可能把分类信息藏进连续概率的幅度，而非忠实报告binary属性。原文CUB表中，联合与顺序配置呈现分类准确率和概念校准的相反取舍；但所述顺序阶段只重训分类头，不能解释冻结概念概率的校准及定位分数为何同时改变，相关训练或检查点口径仍未闭合。固定路由一直开启，也未单独证明它使全部grounding改进成立。应分别核最终任务、部位定位、概念值和干预结果，不由其中一项通过代签其余项。平均位置先验依赖单对象和较稳定姿态，不能自动处理多对象、遮挡或任意视角；小量keypoint只用于初始化也不等没有概念/类别监督。特征编码与cache、结构映射、标注、全部训练和独立干预都付费；部位定义或先验失配时，保留普通分类表示、较软读出或补可信空间监督，不从一个命名bottleneck批准完整因果解释。<!-- source-family:SF-2026-ARXIV-2606-04364 -->

## 当前bounded停点

当前实际V3退出1且唯一PF-CBM Books普通待判断枚举无效，CF行已按R77真实已有覆盖先复跑通过。新普通待PRE不冒“暂缓”或先记I；不改validator/合同。README限定diff --check与新Source no-index空白核无诊断（no-index退出1仅表示新增差额），机械不代语义验收。

04364首次必要/5分/actual Ch5最小两段PRE ready，待首次非writer必要/owner/PRE，无新Books授权/写入/本人注/POST/I。CF R77–78具体NC已行政采用，V3先真实通过，累计仍新增I16＋旧1合17。新候选普通待判断不冒暂缓/预I，校验结果见恢复末节；下一04485首次必要层、有限相关官方标题stop与完整DAY仍ordinary。该单篇ready即交root结束作者准备阶段释放槽，不等其他日/余Methods，不扩附件/73/706导航；非暂停或完成本日。State/index/他日不改，无stage/commit/push。

## R79采用 / 唯一修句后真实SAVE与selfread

恢复重读AGENTS/当前适用合同/Prompt、ROADMAP/三Books上下文、来源使用/Daily/arxiv/恢复、仅2026路由与本日精确停点；R79–80已完整实际读回，不第三必要Source/PRE/AB/date。Source先按R79唯一替句窄修PRE，另明确T3 classifier-only frozen与concept ECE/Point/MI变化口径不闭；Report同保限定，不补训练/温度/检查点实现或借后版解释。

root fresh当前Ch5双锚/邻4/6后新窄授仅修后两段＋本人true-H2注，作者当前再次完整读双锚/外侧marker与邻4/6交接。修后PRE逐字真实保存于Ch5:105/107；本人整注在真正`## Review notes`下当前735。完整新增两段、直接compositional usefulness完整上段和消费几何完整下段及外侧marker、本人整注/邻接均已实际自读，命名连接/soft空间支持/概念语义三层仍分责，T3只保关联与未闭，不冒因果改善或完整leakage消除。

只读限定检查：两修后段连文一次、family正文marker一次、本人注一次/trueH2正确；只移除本两段/本人注后整章与写前快照字节完全一致，保护原两侧/marker/他注及并发差额。快照`/private/tmp/pfcbm-0605-save.NLfvyZ/ch5-before.md`；before SHA256 `61414c70872b893bc4680148403bcfec7cf9b73bea19361ce1b4936169e09ed3`，after `1b0ca2f0e0544cbc5969f7ef12c40cd8916719149f8395d79c4679ac19aad806`。README/Source/本人注仅待唯一非writer actualPOST，不预I/DAY；现I仍新增16＋旧1合17。

本写入ready即交root结束bounded作者阶段释放槽，供同reader唯一actualPOST，不因等待扩最后一篇Methods；04485、有限title stop与最终完整DAY普通保持。V3普通待POST枚举如实失败，不冒暂缓/改脚本，限定检查另记本日恢复。无State/index/他日/stage/commit/push。
