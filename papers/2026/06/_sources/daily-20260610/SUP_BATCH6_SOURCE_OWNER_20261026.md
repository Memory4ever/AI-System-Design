# Jun09 第6批必要与actual owner（不替代唯一独核）

本批当前采用状态：09828/09507/09803/08810/08357/09056/09150七限定整合均已按root具体窄授真实保存、作者完整自读，jun10_review分别§68/70/72/73/78/79/80唯一actualPOST通过。09159中心H由§74必要/actualowner核通过，无diff；09150同家族controller/perf子命题隔离，不另计I/H家族。下文‘待reader/root’保留为准备阶段原稿，不是当前普通未做；所有必要/Books普通0，日级验收另按终存README。未核代码/复现的范围不因整合改写为已核。

## 09828 Mirage（2+2+2=6）：3D cache直接读latent，像素往返移到chunk更新

作者实读exact-v1 §3–6/A1/A3必要；不借Aug27v2。Depth/camera重建后按latentgrid缩K/depth，以VAE每cell C维feature做3Dpoint attribute；targetpose下zbuffer投影/取frontmost、zero填hole另visibilitymask，直接sidebranch条件denoise。不同于RGBpointcloud逐read render→VAEencode；update仍decode每chunkframes→depth/pose/Qwen3VL+SAM3动体/skyfilter→reencode→backproject并union，未给boundedcache/动态actor状态。Feature来自nativeVAE不证明跨view等变/warpedfeature仍在encoder分布，sidebranch是学习消费hint，不是真几何或lossless3Dlatent。

geometryA1明确world→cameraSE3/halfcell坐标/latentK同比缩放，depth估计/插值/discretization/遮挡仍误差。点数约pixelgrid的1/s²，不等总bytes同倍率（每点C48 vsRGB3，坐标/visibility/临时量另计），不采‘s² per spatial dimension’措辞作s⁴。五chunk读cache测量不授无限horizon/constantmemory，union与重复表面融合未闭不补recipe。

Wan2.2TI2V5B，VAEstride4×16×16/C48，9latentframes/44×80→33RGBframes704×1280；train32A100/globalbatch64/BF16/FSDP，sidebranch冻backbone/VAE stage1lr1e-5，stage2rank64LoRA qkvo+branchlr1e-4、UniPC40/CFGoff，iter/训练样本数/重复seedCI未披露。训练RealEstate10K静态支撑，defaultDepthAnything3/替换MapAnything/UniDepth均是估计不是GT。

WorldScorefull70.36vsRGBablation67.71可支持同backbone/recipe局部替代；完整跨模型表不同backbone/trainpipeline不授全部收益单因latent。CameraControl55.36<Spatia75.66、Content42.09<69.95、motion等亦退；RE10K PSNR18.38<Spatia18.58与closedLPIPSC.228>.213，不称所有metricwin。Fig5正文/caption实际singleH100 cache-read/peak cache随5chunk，headline‘E2E10.57x/55x’缺完整update/generation成本口径，不用cache-read计时签整rollout服务收益。训练/深度分割、cachegrow、重编码、projection与全部采样计费；movingactors明确不持久。

actual作者Ch25:635–716相关persistentstate段与921–950已读，直接AnyRecon两完整段及相邻objectaddress实际重读：已有referenceviewlatentKV+derivedgeometry检索，未有每3Dpoint存native latent并直接targetlatentgrid读取、pixelupdate移出readpath的具体producer/consumer差额。唯一`MULTIMODAL-WORLD-MODELS`，拟AnyRecon完整两段后/ObjectAddress H4前一段+本人真H2注，不改原capture/derivedgeometry边界。待reader一次必要/owner/唯一literal核/root窄授：

> 空间memory也可直接保存生成器消费的latent，而不每次把RGB点云渲染后重新编码：按降采样depth与相机内参把每个VAE cell连同feature锚定到3D，目标视角以latent-grid投影/z-buffer读出，并用独立visibility mask区分空洞与零feature。[受限latent-cache分支](https://arxiv.org/html/2606.09828v1#S4)把像素decode、重估depth/分割和re-encode留到chunk更新，减少readpath往返，却未消除这些费用；点数减少不等全部byte同倍率，所测cache读计时不签完整rollout加速。来自VAE的feature也不因几何warp就保证跨view语义或真实状态，生成错误会在回写中累积；动态物体/天空过滤使它主要保静态场景，而非完整actor dynamics。Depth/pose、codec/sidebranch与cache身份须共同校准，长期增长、遮挡或质量失配时，保原capture/RGB或viewbank、短段生成与新观测重置，不让缓存自洽代替真实重访和行动验收。<!-- source-family:SF-2026-ARXIV-2606-09828 -->

## 09507 Prisma-World（2+2+2=6）：同步多view jointdenoise的agent/time坐标与相对camera接口

作者实读exact-v1 §3–5全部必要；main无appendix/traininghardware/精度/优化steps/seedCI/latency预算，不补造代码已核。‘Agent’是摄像机控制视点，不是Ch82语言worker或已验证物理交互。Wan2.2TI2V5B/冻VAE，各agent首frame保持clean，其他framesnoise，展平全部N×T×H×W作同fullattentionjointdenoise；不是N份独立sample后拼接，也不是一条view被当后续time。MA-RoPE保所有view相同t坐标，y/x分别offset nH/nW区分view，model按agentindex坐标并不自动permutation-invariant。

另parallelcamera-aware attention给Q/K施相对camera表示P_i P_j^-1；Eq4仅写投影矩阵作用，未交代embeddingd如何扩展SE3block，不采用可执行扩维公式。Pose接近identity也不保证dotproduct更大/语义严格一致；fullattention、MA-RoPE与camera条件只是学习耦合，不是几何硬约束/epipolar证明。Overlapdecayingcurriculum从同panorama高overlap到较独立轨迹；variableN线性noiseshift未给具体scale，minimap由VAE/Gaussian局部窗提供初始layout hint，非真实状态或可达性验收。

PrismaDataset UE5 static场景96panorama/79perspective、620h，单panorama派生C±30±60yaw的五同步views共享轨迹；MultiAgentBench来自heldoutscenes的这五view转移/组合，不把其当不同物体交互、任意平移baseline或真实sim2real。主Table1对Lingbot/MultiWorld不同pipeline，FVD/PSNR/SSIM/LPIPS及depth/pose派生RPE只各测局部画面/重投影，非contact/dynamics/可操控完整world。Table2 w/oMA-RoPE14.12→13.58/InterRPE.084→.113、w/ocurriculum→13.67/.108支持局部组件，不独立证camera分支必要；minimap和dyshift主要Fig5定性/未核像素，不采精确人数无限扩展或净速度。

全attention成本随N×T×H×W token数至少二次attention增，variableagenttrain不等任意N实时/constantmemory。训练/encoder、joint多viewresident、camera分支/minimap及全部sampling/独立几何回归均计费；未提供actioncounterfactual/可交互causalrollout/真实闭环对照，不将跨view自洽升真实共享状态。

actual作者Ch25:635–670完整已读，2603.17375双目分支明确固定rectifiedrig与同time行内crossview读，后接关节状态建模；新差额是Nviewjointfullattention下同步time与viewidentity分开的具体坐标接口，而非泛‘共享世界’。唯一`MULTIMODAL-WORLD-MODELS`，拟17375完整两段后/“位置持久化还不够…”前单段+本人真H2注，不改双目有效边界。待reader一次必要/owner/唯一literal核/root窄授：

> 不限于固定双目rig时，还可将多个受控视点放进同一次joint denoising，但不能简单把view接成更长时间轴：同步帧应共享time坐标，view identity另占可区分的空间坐标，并由相对camera条件调制跨view读取。[受限多视点分支](https://arxiv.org/html/2606.09507v1#S3)保各view首帧条件、对其余tokens作full attention，因而与独立生成后合并或行内epipolar读取是不同分支；坐标/pose耦合并不硬性保证共同实体、任意view顺序不变或物理一致。静态合成场景、同panorama派生视图与有限消融支持局部一致性，不能升级成可交互多主体dynamics或真实共享地图。Agent数增加同时扩大joint token与attention费用，训练/相机或minimap处理和全部采样都计费；时间同步、标定、跨view质量或预算不合时，保独立短段、已核双目/几何renderer与真实新观测，不由自洽画面签发行动安全。<!-- source-family:SF-2026-ARXIV-2606-09507 -->

## 09803 Echo-Memory（2+2+2=6）：同接口下replay与return的选择反转，不授完整架构因果

作者实读exact-v1 §3–8、AppendixA/B全部及C总说明/C1；C2以后未为采用单篇再重复读（主§7含对应直接反侧）。共同videoDiT、per-frameVAE、relativeRT12、Context-as-Memory数据、FoV检索与target-onlyflowloss，将Context/Compression/Spatial/StateSpace配置放同memoryprofile接口，训练/采样路径尽量固定。§3与A没有给完整modulearchitecture，不能认证blockwise不可bypass或空间grid带宽是唯一原因，不扩全代码来为有限比较补做架构证明。

§7Table3/C1具体rank反转：Spatial replayPSNR13.60但openreturnVLM6.00；blockwise recurrence replay9.59而return69.00，ContextK20 replay12.54/return58.63。注入none的Spatial在replay14.66高于13.60但return15.50，限制‘replay增益即实际memory使用’；不同内容因果替换仍由既有2609.12090负责。K1/5/20只是容量基线而非纯容量因果曲线：K1LR1e-4，K5/20为5e-5；固定5ksteps也非同FLOPs/参数或residentmemory。不能只凭表授SSM普遍最优或Spatial必然不保identity。

81frame/352×640/8A10080G、AdamW/perdevicebatch1/5ksteps、contextsuffix/drop.1、shift15与flowshift1；精度、重复seed/CI/完整推理计时未披露。C总说明revisit仅8cases/row，20×8为QwenEdit首帧候选池，不说160全部评测；replay三chunks/GTcamera，ID180deg有GT，open45deg无pixelGT用visualproxy+Qwen3VL30B语义评分，三人口不可混。Qwen/Opus4.6/GPT5.5/人审subset相关>.90，但subsetsize/人审细节未披露，不授全pool独立真值。生成、检索、显隐state、judge及训练全费，归一效率图不等完整serving收益；更多pose噪声/训练预算/dataset可改变局部排序。

actual作者Ch25:681–758及900–1033完整相关段已读：已有2608.30692的hiddenstate intervention、StEvo控制分母、2609.12090内容替换识别repair-vs-recall，及Memory架构各具体分支，但未有共享camera/生成路径下Spatial与recurrence的replay-return排序反转和rawcontext基线的这个原比较证据。不是借‘指标分账’泛论制造diff。唯一`MULTIMODAL-WORLD-MODELS`，拟2609.12090完整内容审计段/marker后、“视频世界模型还暴露了两个…”前单段+本人真H2注；不改现因果测试或后压缩轴。待reader一次必要/actualowner/唯一literal核/root窄授：

> 内容替换能审计是否使用memory，但选择表示还要看它服务哪种复访：在共享camera接口和生成路径下，分别验GT轨迹replay、有GT的闭环返回及无pixel真值的语义返回，并保原始context容量基线。[受限同接口对照](https://arxiv.org/html/2606.09803v1#S7.SS1)中，空间memory的replay PSNR优于block-wise recurrence，语义返回排序却相反；因此按replay挑出的表示未必适合离开后找回同一对象，不能由平滑画面批准删去历史。这个反转是有限配置/八例返回的选择证据，不证明递归state不可绕过、空间存储必然失效或固定steps等全部预算，容量曲线还含学习率变化。应把内容依赖审计、返回质量和总训练/检索/state/judge费用一起验收；新场景、相机误差或语义评分不可靠时，保未压缩context与短段真实重观测，不从局部排名授真实状态或控制安全。<!-- source-family:SF-2026-ARXIV-2606-09803 -->

## 08810 Continuous Language Diffusion（2+2+2=6）：连续轨迹的native-decoder接口，不把probe变采样保证

作者实读exact-v1 §3–4，§5主setup/5.1–5.9、5.10必要BGEE/MDP/ZSBD/RBN与residualtail、5.11–5.14及§7/AppendixA。一次全§5显示中段被截后已定点重读5.5–5.10；不把§6额外扩展/全部AppendixB–D列已读。支持与直接反侧足够，不扩所有下游代码/plots。

连续状态还原MSE主要能由covariance解释，必须与真正训练配对的非线性native decoder分开测；定义tokenlogit margin superlevel为操作性basin，并非凸/球/全局势函数。局部Lipschitz条件内||δ||<m/L保argmax是充分界，正文未估完整L谱，不把它当概率校准或任务正确界；PCA同维还原/固定checkpoint控制可保大方差却伤margin/顺序。ZSBD是同T5有标签token表cosine lookup（非无prior）；MDP用generatedfinalstates的nativeargmax作监督（非真实文本/独立token），97.89% agreement不是去掉native完整校准，数值/rare/subword低margin尾更难。

ELFB/M/L公共PyTorchcheckpoint/OWT，四24G工作站，core/A明确4RTX3090；B32stepSC3/512样本四128shard，M/L与SDE/ODE确认每run512、不是独立训练seed。SCdelta与margin关系随phase/scale变，早/中/后符号不同，不是任意模型confidence或真实内在comparison算法。frontload三1024sample samplingseed的PPL小改善，MAUVE2048/GPT2featurizer、shuffled/time-reverse等只局部支持，未获人工/推理benchmark普胜；linear小readout低PPL可伴低agreement，entropy-matched后反退，nativeconfidence也不签longform topic保持。

5.10/A BGEE用预测cleanlatent的native margin p10连续阈值/半split验证，B/M/L heldout NFE省16.6/23.4/27.6%，agreement>.96不是原sample law或正确率无损。必须全decode监控，四32sampleGPUshard/三repeat smoke：普通64step25.3s、每step监控45.5s、保守earlyexit44.0s，实际更慢。固定earlyexit可在同frontier；randomtime控制只对某matchedcompute点，不能授全固定步支配。ZSBD/MDP训练集、监控、decoder/全部采样与评估均计费。训练side5k/10k noiseCE可改善受噪恢复，marginhinge未胜；不扩成最终trainrecipe/跨接口定律。

actual作者Ch24:185–225完整局部段已读：现有diffusion iteration/成本与masked异步commit、pass计费、aggregator功能分解均在，但缺连续语言latent→精确native decoder的margin/敏感度接口及其NFE-vs-expensive-monitor反侧。唯一`MULTIMODAL-GENERATIVE-PARADIGMS`，拟“连续 diffusion 从噪声逐步 denoise…”完整导入段后/“它的优势不是…”前单段+本人真H2注；不把通用margin定理或PPL警句单独造新段。待reader一次必要/actualowner/唯一literal核/root窄授：

> 连续语言latent还要进入与它配对的decoder接口，而不是只把MSE降小：同样的latent误差，可能因当前token margin与局部敏感度不同而跨过不同离散边界。[受限接口诊断](https://arxiv.org/html/2606.08810v1#S4.SS3)因而同时看native-decoder低尾margin、最终token一致性和顺序/语义保留；冻结token表近邻与拟合native标签的线性readout只是不同probe，不等原decoder或真实语言质量。有限checkpoint中，按margin早停减少NFE却因逐步解码监控而墙钟更慢，且高margin仍可伴长文主题漂移；不能把decoder-readable升级成任务正确、采样law不变或安全commit。Codec层/归一/decoder版本、监控、全部迭代和独立质量回归都计费；接口失配、尾部token或净延迟不合时，保native decoder、原步数与独立任务验收，而不让latent平滑或较少步数替输出负责。<!-- source-family:SF-2026-ARXIV-2606-08810 -->

## 08357 FReDA（2+2+2=6）：递归sampler-induced边际作训练人口，而非预设forward恢复

作者实读exact-v1 §3–4、A5–6/C/D全部必要，未借Aug04v2/完整先前proof。与既有self-predicted双输入的一次错误恢复不同，从blank递归当前模型draft，随机取1..K步，只最后步对同context clean target反传、前步stopgrad，训练人口随sampler变化；softargmax-token/BLANK confidence混合在train/infer共用，block4双向内部/前block因果，清洁target当前block不可见。D2另有GT替换.3→.1，不把‘forward-free’误称完全没有clean token/mask或无训练成本。

Eq10联合KL经marginalization上界成立需相同coupling边际；context条件draft不能直接套无条件productjoint。A5 zerojointKL→p0只是理想结论；monotonic要求family含identity且直接全局最小化真实marginalKL，不等实际surrogate/有限网络/greedy/启发式BoN必单调或stationarity。Eq15 Gumbel(0,1)原score不含τ但Eq16含τ，实际C/D选proposal loglikelihood+.1scorer/greedybeam非该随机kernel，不签精确采样law或定理证明实测最佳。正文‘N=4四negative’与A/C正样本加nslots口径分清，不采用混合N公式recipe。

Qwen3-4B base→10Btoken continuedpretrain(8B+self/BoN分支2B)，64GH200/globalbatch128/seq4096/BF16/seed42，40%math36%code22%edu2%logic、作者decontam未独立审计。BlockDiff同初始/数据/nominaltokens是较近对照，但递归额外forward/stopgrad与BoN/scorer不同，非同totalFLOPs。外模型不同pretraining/规模/shot及finetunedDiffuLLaMA GSM8K不同人口，不授跨family全部收益单因。QwenAR MMLU71.76>FReDA69.11、GSM84.99>BoN84.15、HumanEval65.24>63.41；4步width2→4涨.52是局部无CI。TPF及Pareto_envelope随iterations/confidence扫描，未披露真实decode硬件/batch/并发/wallclock，1.5–1.8x只forwardproxy不服务速度；全部candidate/backbone/scorer/KV/soft词表投影和训练/搜索费保。

actual作者Ch24:1044–1074/1158–1179完整：2604.08302已有单次selfpredicted错误与softtoken接口，18839从腐化target展开短窗全反传；新差额是blank起始、当前sampler递归边际作为训练人口、仅末步stopgrad训练和理想marginal目标vs实际选择分账。唯一`MULTIMODAL-GENERATIVE-PARADIGMS`，拟2604.08302完整两段后/“未提交位置的中间状态也可…”前一段+本人真H2注，不重复softembedding配方或通用BoN。待reader一次必要/actualowner/唯一literal核/root窄授：

> 若不希望预设corruption决定全部中间状态，还可从blank开始递归采样当前模型的draft，再以同context的干净目标训练末次refinement；前几步停梯度，训练人口随实际sampler而变，而不是只从一次masked预测恢复答案。[受限递归边际分支](https://arxiv.org/html/2606.08357v1#S3)让目标从手设破坏路径转向模型自己的错误分布，但实际有限网络的surrogate、greedy与候选打分不继承理想marginal-KL最优化的单调保证，也不证明多修几轮必更好或原采样law不变。它仍使用干净目标、少量GT条件和块内/块间可见性约束，额外draft前向、softstate、候选与scorer均有费用；TPF较高不等完整墙钟更快。递归人口、前缀支持、质量或总费失配时，保预设corruption、原单步训练与较短refinement，以独立输出质量选择，不让fixed-point叙述代替收敛与正确验收。<!-- source-family:SF-2026-ARXIV-2606-08357 -->

## 09159 Unified Energy（2+2+2=6）：潜贡献保留，中心归一/严格改善证明争议拟H

作者实读exact-v1 §3–5、7.2–7.6完整必要；7.7后全benchmark/case不扩。原潜增量是把跨揭示上下文的不变性与组内依赖一并置于AR-proxy energy，并声称闭式partition/严格KL改善；候选6保留，不能因证明错直接preN或降分。中心争议不等普通未读或可选代码故障。

§7.5 Eq29–35仅以真实planner Ω顺序、baseline近均匀、energy重权后同顺序且归一，推出加权loglikelihood严格变好；这个推论不成立。直接反例Ω=(.4,.6)，old=(.5,.5)，new=(.01,.99)，满足同向严格排序与归一且old完全相等，但KL(Ω||old)=.0201355，KL(Ω||new)=1.1750866。能选正energy差使new如此重权，rankcorrect不限制overshoot；故不能授Lemma4.2所有非独立/非不变情形严格改善，也不证明所有energy启发式无效。

§7.4先由A⊥C|B推B⊥C|A（非一般成立），又在Eq21–22把单个joint logratio直接改写为逐token KL之和，欠期望与因子分解；因此β=r/(x+y)的无偏比例不能据此认证。正文§4.3 Eq15在固定x_s时对x0求和可作代数消去，但得到的F显式依赖x_s；实际Alg2每候选配不同x_s并argmin E，不是从该固定x_s归一密度精确采样。Alg3第8行重建x_s又把其他位置全MASK，未保已decoded x_t；不将打印伪码补成正确完整kernel。AR对任意maskcontext的精确posterior本身要边缘化未知位置，主文不能以pAR(x0)/pAR(xt)称已高效精确取得。

有限实验仅报告：OWT/七zeroshot，MDLM+GPT2small，AR直接组合与NCE微调分开，NCE4H200/perGPUbatch16/max1Mstep/lr3e-4/dev.1%选checkpoint。默认k2/w.2但GenPPL及部分消融w1，不拼单工作点；modelPPL依所争议归一/ELBO，不采精确likelihood改进。GenPPL随外scorer/entropy与不同引用baseline来源限定，Table1 NCE Pubmed42.74>MDLM41.89，非全metric胜。DLLM LLaDA8B/Dream7B+Qwen.5B，k3/m4/w.2/7bench，quality主表局部提高不证明energy严格解独立/不变；main未披露此在线GPU/精度/batch/重复CI，10.5vs13.5s是DLM操作点非DLLM服务SLO。全部ARproxy/candidates/候选x_s/重权、训练与选择费保。

actual作者Ch24:1117–1137/1302–1318完整相关段已读：已有Glauber局部conditional/partialenergy与内部dependency graph，不是此跨未来揭示invariance energy/closedpartition的覆盖；不造泛‘proxy不是真值’警句，也不以主题E抹潜增量。拟Books暂缓/no diff：重开需具名修正partition条件/候选联合目标与对应合法kernel、Lemma4.1的依赖/期望条件及Lemma4.2的定量不overshoot资格或勘误；有限启发式若独立采用，须在上述法则外明确原target、实际实现与可比预算对照。当前已足中心争议核，待reader一次必要/actualownerH独核，不扩全proof/全repo。

## 09056 MilliVid（2+2+2=6）：fine最近帧与coarse未来共同消费，避免独立rollout/upscale的选择脱节

作者实读exact-v1 §3–6/全部AppendixA1–3必要文本/captions，未核视频/图像素/代码。Hierarchical per-frame encoder一次产生四level，各level单独decode重建整pyramid；随机只留一层，highest用MSE+LPIPS/其余MSE。不是直接meanpool旧fine latent，也不是无损保fine细节。单DiT消费level/frame/row/col身份、固定S/context-target token数，先长coarse rollout再逐级fine；每次读最近highest-resolution帧和仍只coarse的futureframe，fixed/pending不读。改变的是时间推进与细节解析的依赖，不以coarsecounterfactual是真实未来；正文‘ensuring不冲突’过强，训练cleancontext而推理自产仍会漂移。

Loopcraft20万1024frame/256² MineRL，条件只是left/right/forward三值、非任意robotcontrol。Test从100actionseq/低Chamfer10取1到10000renderedcandidate，再取移动距离最高1000，高overlap易回访选择，不含被卡住等原任务人口；flatplanar代理不保证真实collision/遮挡覆盖，不能证明这种过滤保所有方法相对rank。up_to256GTcontext+GT全部futureactions，生成768frame；pixel/LPIPS/DINO/LightGlue是同轨迹复现代理，非真实地图或actioncounterfactual。无seedCI/人审披露。

ViTB codec32channel/patch16/fourlevels，8H200/BF16/codec128kstep/globalbatch1792约1天；DiTB192k/global384约2天，Muon/AdamW/1e-3、DDIM50/noCFG。FramePack matched3840S/context255但只predict3fine，fullres3584S/context7/predict7；不能把相同S叫全部FLOPs/信息或samehistory。小ablation1280S256kstep不同主192k；hierarchycascade对照支持局部接口，hierarchical FramePack反而不稳定低于random一致性，mirrored虽短history部分一致性更好但quality退，不能说层次表示本身总赢。

A3 batch8×768frame粗计MilliVid/FramePack均约30min、fullres约11min；MilliVid多33%rollout/理论optimizedFramePack可少25%时间。未明确此timing单独设备配置，不能补成8H200推理或实时；不把O(F)等同constanttime或只数finepass。Codec/多层token/全部coarsefine50step、训练、采样与评价费全保，longrange粗structure取舍承认fineidentity可忘。

actual作者Ch25:998–1045包含12090审计、两压缩轴整段/fence、后causalstream两段已读；已覆盖通用hierarchy，但未有每次同时消费最近fine与尚粗future的rollout解析依赖，也没有与单纯meanpool/hierarchicalFramePack反侧这个具体差额。唯一`MULTIMODAL-WORLD-MODELS`，拟“两条路线都在移动成本…”完整段后/“从双向视频补全到可交互的因果少步Rollout”H3前单段+本人真H2注。待reader一次必要/actualowner/唯一literal核/root窄授：

> 层次压缩若还承担未来生成，就不能让时间推进与细节解析各自独立决定同一内容：长段先在coarse层产生，再逐级细化时，每步同时读取最近的fine帧与尚只存在coarse表示的未来帧，用共同level/time身份协调两类条件。[受限层次rollout](https://arxiv.org/html/2606.09056v1#S3)为每层单独训练可解码表示，并不等把旧fine latent均值池化就能得到同一接口，也不保证纹理身份或真实未来。有限游戏回访支持这项取舍，但换成层次latent的其他rollout仍可不稳；生成未来不能伪装成新观测，更多coarse pass还可比普通full-resolution rollout更慢。Codec、多层状态、全部粗细采样和训练/回访评价都计费；细节、action响应或总预算不合时，保fine history、普通短段与新观测重置，不让较长的粗结构保持签发完整物理状态。<!-- source-family:SF-2026-ARXIV-2606-09056 -->

## 09150 Ultra Flash（2+2+2=6）：上游当前条件与自身历史双暴露；cache producer替代与速度归因隔离

作者实读exact-v1 §2–3、B/C、K1–3、N2、G1/H1及F Alg3 cache lines39–58（直接HTML/math alttext）；未扩全F/其余G–N全附件，不以文件已在扩队列。原准入的具体差额是SR不能只见GTLRcondition：训练整个LRgenerator→latentupsampler→SR→HRdecoder自滚动，仅SR更新，当前条件受上游误差且后段同时读自己的SR历史。Preference来自Wan2.2-5B多步pixelSR强参照，不是GT/真实状态，DPO不认证物理一致、排除全部暴露偏差或自动提高所有内容。

基座Wan2.1T2V1.3B，c→2c零初始化projection只是核心blocks保留，非完全不改architecture；causalmemoryupsampler/decoder各异scale，framewise状态不等长时世界memory。低分辨率首chunk4steps后3、one-stepSR与compactSRwindow分别改变producer/预算，不能把step数字一列当完整四步全工作。IQA高于τ时重用最后noisy x_t产生KV而跳过predictedclean x0额外forward，是不同cache producer，不由IQA认证语义等价/可见性；SRwindow未给可执行完整selectionrule。

必要冲突隔离：K1 Table18阈值.50标alwaysrefresh/.80rarelyrefresh且越大FPS越高，与正文/C/Alg3 q>τ skip在同score人口下方向相反，不自行取反。K3 Table20称8frames/chunk31.2ms→32.1FPS，实际8/.0312≈256FPS，给的是1/.0312；且H20030FPS与mainH20017/B20030冲突。N2 70%×6.8−1.8=2.96ms，表写+4.8、正文+3.0，后者算术可闭不默改表。K2 causalcontext当后chunk噪声有效降.7并据log(1/σ)推NFE属未证解释。G1时长表68/42h与prose5.5→3.8day不一致。上述中心精确controller/无损实时归因暂缓，不以headline补完整recipe或生产SLO。

有限质量只报告：Table6全pipeline TC97.2 vsnoDPO95.6，DPO同时强teacher与额外训练，不是纯双暴露因果；cache去项IQ.690 vs.692/MUSIQ73.6vs73.8/TC97.1vs97.2不叫严格lossless，K2少LRstep质量也小退，IQA/MUSIQ又是训练reward本身。H1虽同outputresolution，FlashVSR仍768×1408不是960×1664；不同SR/streaming预算不授38–375x同口径加速。B声称4K受限、消费者GPU较差保。C训练32H200/BF16，clip1vs10内部冲突不抄recipe；新增训练所有stage+strongoracle费用，且pipeline/upscaler/decoder/IQA/缓存与失败均付费。无seedCI/独立human protocol完整披露，不把丰富附录视为已复现。

actual作者Ch24:145–176完整：已有自生history扰动、teacherhistory失配与ShotStream local/global分stage，未有上游LR当前条件+自身SR历史的跨stage双暴露，以及cache选择从cleanpass改noisypass的producer身份差额。唯一`MULTIMODAL-GENERATIVE-PARADIGMS`，拟ShotStream两个完整段后/CausalCine检索段前一段+本人真H2注。拟只采限定机制接口，阈值/完整recipe/速度中心争议仅报告隔离；若reader认为该差额不足独立脱离中心争议，则整项H，不借泛exposurebias/缓存警句造diff。待一次必要/actualowner/唯一literal核/root窄授：

> 级联生成还多一条与自身history不同的误差入口：高分辨率SR当前消费上游自产LR条件，下一chunk又消费自己已生成的HR历史，因此只在GT低分辨率条件上训练，不覆盖这两者的联合人口。[受限级联自滚动分支](https://arxiv.org/html/2606.09150v1#S2.SS3.SSS2)运行整条上游—升采样—SR链而只更新SR，使条件误差和历史误差共同进入训练；强模型偏好参照仍非真实HR或物理状态。部署时若改用最后noisy状态产生的KV替代clean预测额外前向，改变的又是cache producer身份，不由上一chunk画质评分证明两份KV等价；原阈值方向与计时口径有冲突，不能照录完整无损cache策略或实时倍率。上游/teacher、全部级联训练、升采样、SR、解码、评分和重算均计费；条件、历史或缓存失配时，保GT条件校准、cleanpass刷新、更长窗口与较短生成段，分别验质量及完整延迟，不由高分画面签发安全commit。<!-- source-family:SF-2026-ARXIV-2606-09150 -->
