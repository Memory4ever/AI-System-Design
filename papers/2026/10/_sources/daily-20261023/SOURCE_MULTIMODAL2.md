# Oct23 Daily — second multimodal necessary Source slice

仅root指派 exact-v1 29441/29537/29552/29581/29590/29688/29811/29854；既有效完整题摘/准入/初分5/5/5/6/5/6/6/6，不重做前31项。公开日复用本日 ARXIV 官方 Oct22 BJT cs.CV [67]/[74]/[76]/[78]/[79]/[89]/[99]/[103]，cross-list不重复计；提交时间不作公开日。AGENTS与当日合同/停点已恢复，root唯一Report/State/Books写者。官方正文提取 `multimodal2-source-2610.<id>-v1.txt`；原件保存不表示全部附件已读，以下逐项限定实际必要域。未运行代码、复现或认证生产能力，不预签独核/POST/DAY。

## W1 — ALLOT 2610.29441v1（2+1+2=5；标准必要完成，拟 Ch24 窄 gap）

[官方 exact-v1](https://arxiv.org/html/2610.29441v1) §3–5.6/Conclusion+limitations必要核心完整。每(layer,denoising-step)cell分配density：单cell其余dense的velocityMSE probe区分同一步各层/密度，sparsewindow的最终pixelMSE除windowprobe总和校准stepgain，再以gain×probe估计全输出损伤；不是局部attentionmass等最终损伤，也不是从局部MSE解析推出传播gain。First-order叠加、跨cell期望正交、跨layer相同stepgain等近似可能失效，ranking优于magnitude，不授全轨迹误差上界。

在离线measuredkernel latency table下Lagrangian解离散cell预算；proposition精确最优仅“table自身实际总cost等于budget”的估计目标，不是任意给定budget全局最优、真实videoerror最优或硬deadline。Density越高不一定sparse更快，超过crossover用dense；densitycutoff保ranking/kernel却去掉nativeperhead/perinputthresholdadaptation，不能简称原算法完全不变。默认新selection需新probes，固定model/strategy sensitivity稳定仅测试分布经验（Spearman .80–1.00）。

Wan2.1 1.3B/14B、Wan2.2A14B、HunyuanVideo，50steps，32VBenchprompts（某14B表16），4OpenVidprobevideos×8density×9noiselevel，8calibrationprompts/10five-stepwindows/b0.30；calibration非testprompt。PSNR/SSIM/LPIPS是同prompt/seed对dense生成，不是真实video质量；VBench部分退且不进win/tie判据，九pipeline设置六win三tie不等每cell全面好，HunyuanRadial有PSNR/LPIPS均退的tie。11.8dB headline不推通用质量收益。消融去trajectorygain损7.05dB支持其conditional作用，costproportional对齐墙钟后差不显著，不授latencytable唯因果。Offline约6–23GPUh/model、Wan2.2两experts>30，一次/model+strategy；CPU重解约4s不等重新校准免费。主文硬件/precision未充分给，不采用可迁移秒数或生产SLO；全部probe、dense/sparsewindow生成、profiling、solver及全采样计费。

actualCh24“加速不能静默改变生成轨迹”节已写离线layer/step/module敏感prior、局部cosine非finalquality，但缺用sparsewindow终端误差为单cellprobe跨step校准。唯一MULTIMODAL-GENERATIVE-PARADIGMS，在完整“受限敏感度加速对照…局部误差不能预测输出…保留原生成器”段/2603.07057marker后、完整“缓存的计算预算还可以从离线差异统计变成可训练的timestep×block执行mask…”段前，PRE：

> Layer–step 稀疏预算还可直接以最终输出校准，而不只按局部 feature 或 attention 指标分配：先测单 cell 扰动，再仅稀疏一段采样窗口，用终端视频偏差校准跨步传播，最后按实测 kernel latency 联合选择密度。[ALLOT 的受限构造](https://arxiv.org/html/2610.29441v1)保留 selector 排名与 kernel，却用 density cutoff 替换其自适应阈值；叠加、跨层可分与输入稳定仍是近似，离散估计目标的特殊最优条件不认证真实误差或任意预算最优。Probe、dense reference、窗口生成、profiling 与求解都付费，相似 dense 输出也不等更接近真实视频；模型/selector或预算改变须重验，失配时保原密集路径、固定已验分配和独立质量检查，不让较小局部误差或少块数签发最终保真与SLO。

## W2 — Melange 2610.29537v1（2+1+2=5；标准必要完成，拟仅报告/具体 NC）

[官方 exact-v1](https://arxiv.org/html/2610.29537v1) §2–5/§7–8必要核心完整。BBQ选7类视觉可表征场景，Flux分别造背景/两人物，filter/age-gender-race tags、non-target匹配+humancheck后合成；sexualorientation/nationality等无可靠visualcue排除。只ambiguousitems，gold全Unknown，FaiR实际测歧义下abstention；高分可能一般拒答或看不清，不等全部fairness/正确有信息时公平。未控制全部expression/clothingcolor等latentconfound，宗教marker可读而身份不可从外观认定；视觉标签是设计刺激而非真实protectedidentity。

23model/9families三setting（原text/fullcontext、image+左右选项、image+neutralcontext），prompt/answerreference表达随模态变，未纯因果隔离视觉通路或dense/MoE架构。同vendor/release不等预训/优化matched，不能采用其“isolates architecture”因果措辞。90–95%perception为7代表model的forcedtwo-wayattribute/detection且无Unknown，不是23全量一般视觉理解；conditioningseen仍只提供局部控制。Table2与Table3同model FaiR数值明显不一致（例Qwen72B .852 vs .898、LLaVA .066 vs .080），正文未给连接协议，故不把两表拼出精确净差、纯感知排除或通用公平曲线。12640scenarios与结论126400images的层级/人口也须保原口径，不把都写成独立eval题。

Questionpolarity改变stereotypicalanswer，polarityblind约.5可掩方向；polarityaware .770是已commit nonneutral且有stereotype标签人口，SES无、race27%/gender96%覆盖，非全场景biasrate。旧设计两crop-onlysetting因perchar原图已无而不复现，当前只三setting；这不是新增扫描缺口。生成/候选过滤、人审/tag、全model三输入/概率解析、perception与选项回归均付费，主文无完整hardware/预算不补。只采用有限benchmark blindspot与分母限制，不授消偏/部署安全。

具体NC/仅报告理由：actualCh66:254–256已要求偏差逐item方向/实际计分token/本地构念真值分开；520–529已要求target/cue/null、选项顺序及真实行为与scorer变化分验，不让关联或一个bias分数替公平保证；Ch23表示可读≠consumer使用亦已存在。新synthetic实例可保报告，但表间不一致不支持另写通用“视觉导致不公平”的因果结论，现有正文亦未把辨认属性等于公平，不制造纠错diff。待reader核。

## W3 — Generalized CycleGRPO 2610.29552v1（2+1+2=5；必要 Source 完成，本窗命题按真实早稿收窄）

[官方 current-v1](https://arxiv.org/html/2610.29552v1) §3–6必要域已读。真实早稿cue不是假想：[38]/§3.1/3.4/结论明确扩其ECCV工作，[官方旧v1题摘/历史](https://arxiv.org/abs/2607.11581v1)题名Actor as Its Own Critic、v1 Jul13/v2 Sep2，已讲image region→caption→region、无需captionGT的双向cycle。官方[repo](https://github.com/devinxzhang/CycleGRPO)还把image68.2 gIoU列为publicrelease rerun。本窗不把image原理/既有image指标再称首次公开；不恢复JulyDaily/旧全文，当前精确新增为temporalinterval/spatiotemporal统一regionconsistency与DOVE。

同一policy分别描述给定region、从description回定位；Ncaptions各Klocalizations，captionreward用innerconsistencymean，各localreward按同parent分组，双方梯度共同一次optimizerstep，localizer非冻结真值。Temporalinterval union/tIoU，timestampcaption惩罚并在innerprompt删除，避免直接抄给定边界；spatiotemporalanchors最大权一对一匹配、时差>3s交集0、unmatched/extra入union，防重复利用同一reference。Spatialmasktoken surrogate不是所有域都decodedIoU。仍需已具两接口/SFT、knownregions，reference-captionfree仅RL阶段；重构可行不等caption完整/流利/事实正确，implicitshortcuts与初始localizer差仍会污染奖励。

Temporal共享Qwen3VL4B co-SFT、同RLvideos/budget，caption-only/localization-only及joint；OMTG也另作初始化，不混Qwen51.9与OMTG51.8同条件。QVHighlights部分recall退、VideoMMMUperception76→75.7，别称原能力全部保持。Spatiotemporal由Openo3Video4B-RL经1epochinversecaption/videoQA co-SFT，再mixregiontasks与generalQA（后者仍answerreward）；gain不是单一纯cycle无辅助。BF16/frozenvision/FSDP，N×K全部outer/inner、KL/reference、regionchecker与SFT付费，主文未完整给硬件/完整训练总费，不补。

DOVE：180video/querygroups、530intervals，1223private Order/State/Outcomeprobes只覆盖529interval，另一例不入指标；同query重复occurrences，人审共同核specific/sharedfacts，privateprobes冻结后textonlyQwen2.5-72Bjudge只读caption不见video，非training时外部judge。给定targetinterval，不测自动发现boundary/audio；TEC为三type宏平均，ClipComplete另测全部probe，N/M不能当错误率。按video/querygroup bootstrap20k次非独立probe采样，18.5pt TEC gain是该protocol，不授完整语义/无幻觉。

actual Ch23“保存时间戳也不等于模型能从长视频准确生成时间边界”/2605.21973完整段已有candidateID→boundary refinement与分项验证，未有对同query多次出现的caption→temporalregion自监督及不能抄给定time的反侧。唯一MULTIMODAL-REPRESENTATION，在该完整段/marker后、完整“多变量序列还要决定何时引入变量间交互…”段前，PRE只收本窗video新增：

> 同一事件在视频中反复出现时，描述“发生了什么”还不够区分“是哪一次”。可从给定区间生成多份 caption，再各自从全视频回定位，以重构该区间的平均 overlap 奖励描述，并同时优化定位；caption 中的显式 timestamp 须惩罚或删去，防止把给定边界直接抄回。[Generalized CycleGRPO 的视频扩展](https://arxiv.org/html/2610.29552v1)沿用早先 image cycle，而新增 interval 与逐时空 evidence 的一致性接口；回到原region仍不证明描述完整、流利或全部事实正确，较弱 localizer 也会给出噪声奖励。已训双接口、region标签、全部嵌套rollout/训练及独立语义检查均付费；重复事件、implicit shortcut或原能力回归时保可信区间、原定位器与人工/独立probe，不由cycle闭合批准真实grounding或零文本监督。

## W4 — SNR tuning / spatial grounding 2610.29581v1（3+1+2=6；设计反证域深入必要完成，拟 Ch24 窄 gap）

[官方 exact-v1](https://arxiv.org/html/2610.29581v1) §3–6全部必要方法、对照、限制已读。真正改变fullfinetuning中t~logitnormal的分布μ，x_t=(1-t)x0+tε，μ大偏highnoise；不是推理时改scheduler立即解锁、不是不训练。100k合成train/1kheldout，1–10colorrectangles、normalized[0,1000]coords、prompt顺序给occlusionpriority，目标完全遮蔽者从metadata移除；colorIoU阈值2–25平均同时测颜色/几何，非纯layout真值。VAE重构分数只empirical参照，非所有生成的数学上界。

FLUX2-4B/9B、Flux1dev12B与QwenImage20B分别fine-tune；singleA10080GB/BF16/Adafactor/fusedbackward/checkpointing、batch1/100ksteps、lr1e-5→5e-6/EMA/10%null，25stepsCFG3做synthetic。FLUX2 256² μ0的25.9→μ1的80.8是同recipe有限对照，μ3颜色损导致69.4；更高resolution/aspectratio要重新搜索，但只以前配置best作后续lowerbound非完整网格，optimalμ不当定律。Architecture/textencoder/VAE一起变，不能由跨model表独归VLMencoder可访问性或VAElearnability。单seed/不确定性未充分给，未补普遍nearceiling保证。

COCO过滤crowds/dense/small<2%，61986train/2565val，FLUX2-9B512²/aspect≤3、lr1e-6/5epochs（另10epochs）、50stepsCFG4，冻结YOLOv11x测AP/AR非物体真值。μ0 AP1.0→μ3 57.3但FID/CLIP弱于部分专用method；生成AP50超GT detector77.2本身揭示“empirical ceiling”不是真上界，不可改写为超真实准确性。强shift仍损纹理/mergedanatomy/clockdetail，早期40–50%layoutcondition的探索也有AP退，非完整修复配方。全部合成/过滤、各μ/shape/model训练、EMA驻留与生成/检测评价付费，无新增结构≠无需适配或预算。

actual Ch24在线分箱/有效目标节已要求πw定义训练压力且推理网格分验，缺“已有结构模型的坐标grounding失败还须先排训练噪声支持不足”这一具体设计反证。唯一MULTIMODAL-GENERATIVE-PARADIGMS，在完整“在线分箱方法与反侧…独立检查训练分配和推理网格…”段后、完整“采样时没有x0可用。网络的噪声预测被换算成…”段前，PRE：

> 文本坐标没有被生成器落实，也不应立即归因为必须新增结构 adapter：固定模型与布局监督，只改变 fine-tuning 遇到的噪声分布，就可能改变其学习全局位置的机会。[受限 SNR 对照](https://arxiv.org/html/2610.29581v1)中偏高噪声训练改善部分模型/分辨率的布局，却会牺牲颜色与细纹理，最佳偏移也随输入几何变化；这不是推理时换 schedule 的免训练修复。VAE重构和检测器在真实图上的分数只是经验参照，生成超过它们也不认证真实物体或硬上界。合成/标注、完整适配与各配置搜索均付费；布局或细节回归时保原采样/模型、可信结构条件和独立质量检查，不由无新增架构批准通用空间能力。

## W5 — CineEvolve 2610.29590v1（2+1+2=5；标准必要完成，拟 Ch33 advantage 窄 gap）

[官方 exact-v1](https://arxiv.org/html/2610.29590v1) §3–5/Conclusion+Limitations必要完整；准入仅E-GRPO parent/historical guard，不因Director/Critic电影workflow组合收。共享Qwen3VL8Bpolicy分角色，critic→frozenintermediatecritic给本rounddirectorreward，再用teacher注新storyboard并50%旧+50%新refreshpool；部署自主loop≠训练无externalteacher/judge。CineTraj30kSFT/10kRL，teacherGemini3.1Pro只保severityweighteddefects严格减少的demo，不能忘失败构造费用或当自然成功率；100heldoutmovie sequences，scene-source严格不入policyinput但作externalnarrativejudgeanchor。

Revision新增severe被critic确认则rewardcap到parent p_g；r≤p的groupadvantage裁成≤0，防全组变差仍相对best得正。再用每task256fixedcalibrationinputs/一response在currentevaluator下mean b_k，把中心提高到max(groupmean,b_k,parent)，nonrevisionparent0；boundedinterpolation保≥半positiveadvantagemass、negative≤2×，按全optimizationbatch有效trainabletoken加权。b_k的正文只给currentevaluator口径，不补成跨代不变真值或未经明确的某旧checkpointlog。Proxy自身错、同源critic共同误判仍可放大，guard只约束该reward/advantage，不保证真实单调改善。

2epochSFT/lr1e-5/batch64，5alternatingrounds各role64steps/lr1e-6/batch16，16A100，frozen4stepFLUX2klein9Bstoryboard+8stepMiniMaxH3Turbo video；G4rollout/max10revision。固定critic、separatepolicies、originalGRPO对照支持整套guard/anchor但不分别隔离两项，不以“cognitive synergy”授唯一共享参数因果。Baseline统一backbones却额外expandedscript、完整revision/tool预算未matched，末video细motion不在storyboardfeedbackloop。Human25stories×20volunteers选7法最偏好，share非pairwisewin/generalpopulation；sameGemini teacher/evaluator非独立truth。Teacher/筛demo、replayrefresh、256calibration、全部render/revise/judge及训练总费均保，SFT成功过滤不消除失败成本。

actualCh33“这是一种sample-relativebaseline…完整response相对更好”与后继资源/统计人口段已解释组相对≠真实价值，但缺已知parentreference限制正更新的机制。唯一TRAIN-GRPO，在该完整sample-relative说明段后、完整“同prompt的rollout还必须得到可比较的执行机会…”段前，PRE：

> 修订任务若有 parent，还可限制“组内最好”是否获正更新：先在同一 evaluator 下比较 parent 与候选，对不优于 parent 的候选把正 advantage 截到零，再以固定校准输入的参考奖励抬高中心，有限混合这份信号。[CineEvolve 的受限 E-GRPO](https://arxiv.org/html/2610.29590v1)针对劣质整组仍有正相对分的问题，不是 critic 或历史均值取得真实质量权；同源评分错误仍会穿过 safeguard。参考人口、评估器快照、parent、有效 token 及校准时钟须共同保存，外部教师、全部候选/修改、校准与训练均付费。Proxy漂移、参考不可靠或真实任务回归时保可信outcome、原checkpoint与普通组比较，不由不降的自评分承诺跨代单调改善。

## W6 — Rethinking Post-hoc Debiasing 2610.29688v1（3+1+2=6；归因反证域深入完成，拟 Ch23 gap）

[官方 exact-v1](https://arxiv.org/html/2610.29688v1) §3–6/Conclusion必要完整。UrbanCars两同时shortcut（BG/CoObj），samefrozenCLIPViTL14+same-capacitylinearhead/optimizer/scheduler基线，PRISM/RoboShot/PRISMmini的correctedfeature可比未debias差；把LLM描述换groundtruthattributeprompts可改善仍不及undebiasedhead，说明仅识别bias不充分，非证明一切posthoc必失败。两个text方向cos.58只是overlap诊断，whac-a-mole不是已做完整因果隔离。

Frozenimagegeometry选高cos异class pairs作push、低cos同class固定subsample作pull，sets在训W之前固定；learnidentityinitializedlinearW并normalize，hingemargin控制何时不再推动，之后fixW另训head。只不用biasattribute annotations/LLM，不等没有classlabels、训练、val选择；异class相近不是biastruth，94.8%至少一shortcut仅UrbanCars986selected/16M allpairs的用hiddenlabels分析，依赖题设多数/少数关联及frozengeometry，不授任意数据可靠发现未知bias。

4datasetUrbanCars/BAR/BFFHQ/Waterbirds不同biasratio，three seeds/meanstd，W约.59M与backbone约300M不能免pairwisefeatures、筛选、投影/下游头训练。按dataset heldoutvalidation选hyperparams，正文未细分具体selectionmetric/所需group资格，故不把train不见bias说成全pipeline无任何group信息。WorstJoint只双shiftgroup，WBG/WCo不能混，rowcosine与linearhead分开；Table6单配置83.87与Table4三seed81.18±.93不拼同统计。单push/pull与去hinge都有强反侧，但更小d与4dataset不授普适公平或模型生成消偏；部分overallbaseline更强。硬件/全wall预算未主披露，classimbalance/DINO附录非拟采用命题不扩读。所有编码/近pair、valsearch、W/head、三seed与独立group评价均计费。

actualCh23:2081–2093已有textSVD/non-targetoverlap、SAEquery调制与描述依赖，未覆盖“即使oraclebiasidentity也不足、改用class-conditioned imagegeometry的备选”。唯一MULTIMODAL-REPRESENTATION，在完整受限CLIP/SAE段及2603.19028marker后、完整“理解和生成还可能使用两套不兼容的视觉token…”段前，PRE：

> 指定偏差属性也未必足以修复冻结表示：多种 shortcut 共现时，即使用正确描述替换语言模型的猜测，投影后的同容量 classifier 仍可能弱于原 feature。[受限 post-hoc 对照](https://arxiv.org/html/2610.29688v1)因而另从高相似异类与低相似同类图像对训练线性 map，改变的是按 class 支持的几何，不是无监督识别真实 bias。相近 pairs 在所测数据富集 shortcut，不保证新域仍如此；margin、validation、class 标签与原头都需保留身份。全量编码/选对、map与head训练、调参与群体评价均付费，相关性、原效用或最差群体回归时保原表示、可靠标注和专用读出，不由正确命名或单个worst-group分数批准普遍消偏。

## W7 — CZSL primitives 2610.29811v1（3+1+2=6；反证域深入完成，拟仅报告/已有覆盖）

[官方 exact-v1](https://arxiv.org/html/2610.29811v1) §3–5/Conclusion必要完整。Seen训练samples带attribute+objectlabels，GDE在全mean的tangentspace提按textalignment加权primitive；intrinsic版本每concept直接Frechet mean，二者测试各自打attribute/object分再加，不必先Exp(sumprimitive)形成每pairvector。仍用原训练label/均值/geometry/可选textbridge，zero-shot指unseenpair非unseenconcept/无支持；fullCartesianproduct时加分是factorizedreadout，不独立认证内部semanticfactor因果或真实逻辑AND。MAP/softmax输出不同protocol不授全部开放概念组合。

CLIP/DINOv2+Talk2DINO/MERU/HyCoCLIP跨sphere/Euclidean/hyperbolic，sameGRIT/backbone也不隔离loss/训练目标全部差异。MITStates/VAW/Clothing多改进，但UTZ原生lowvariance下GDEpair通常更好；whitening后intrinsicHM强，GDEprimitive仍可弱/退（MERUHM8.99→8.80，对pair12.79），不能录“consistently每种primitive更优”。Whitening同时改全geometry不是只变单一variance，低variance唯因果论不采用；CORR/MI部分低不等独立、truth或可识别。报告bestHM把seen/unseen两人口通过harmonicmean汇总，不是逐例两条件同时成功率，也不自行认证部署固定选择；training/selection支持与候选域须绑定，不补造具体校准搜索已核。

Waterbirds/CelebA仅objectprimitive与textzeroshot比较，多数WG改善但DINOWaterbirdsaverage/worstgap反而26.7→37.5，不能当无损普遍公平。Labelledprimitive参照不是与无labelzero-shot等输入预算；embedding、mean/LogExp、whitening拟合、textbridge、所有candidate打分与校准/独立评价都付费；未给完整重复seed/硬件不补。超曲origin/radial解释只是hypothesis，未证明物理/生成/Agent组合推理。

具体已有覆盖/仅报告：actualCh23完整2605.15942分解读出段已容许category/attribute分别编码后汇总，明确非独立事件概率/逻辑AND、seenatoms与heldout组合≠真新concept；邻近2602.16545分类头modifier与固定/条件prototype亦已保原监督/读出责任。当前Books未声称CZSL必须显式pair重组，本篇给出几何specificfactorizedclassifier与UTZ重要反例而不要求更正已写论点。保条件方法及variance混杂于报告，不硬添同类prototype段，不因NC降分/排入选。

## W8 — DiT aggregator–predictor 2610.29854v1（2+1+3=6；必要理论/机制审阅完成，拟 Ch24 gap）

[官方 exact-v1](https://arxiv.org/html/2610.29854v1) §2–6及C.1–C.2完整假设/证明已读。GlobalBayesdenoiser与givencontextlocalconditionalmean不同；GaussianMRF prior/graphblock-sparseSPDQ、独立isotropicnoise、positivea/b下，localityerror按graphdistance radius指数上界，graphneighbor不必空间连片。C1 Chebyshev逆矩阵多项式+条件期望投影，Q等各向同性时radius0exact；radius上界随noise单调仅0<σ≤由eigenvalues定义σ_abs，极大noise mean→0令绝对error界反降，不准外推全noise越大context必广或所有真实image成立。

PLD的可测聚合若保empiricallocalconditionalmean信息，σ>0/fullrowrankS+相应Γ才恢复empiricallocaldenoiser；不等population未知prior或trainednetworkexact。单attentionbranch可解释QK决定spatialweights、VOsharedchanneltransport、AdaLNGELUMLP作为learnedpatchpredictor；residualstack中各分支改后层routing，角色不是全网可分/唯一内部因果。Softattention与Jacobian sensitivity测不同量，真实DiT只是qualitative broadening。

CelebA64unconditionalcommonbackbone/400epochs、one seed each comparableparams，LPLDpositionmemory vs sharedSCA/SMLP/heads改变支持controlledpatchpredictor可行，不证明所有MLP藏一个sharedbank或conditional大模型可直换。12face/naturaltransferdirections只jointtuneQK/VO/MLP、固定AdaLN/global，再做8hybrids；转plantcompatibility不是各组件单独训最优，targetsourceagreement按matchednoise/DINOglobal/patchselfsimilarity归一，不是真targetquality或通用causalroles。SpatialMMD关联与VOreversionnonadditivity相关不唯一identifycomponent职责。完整source训练、目标joint/restricted适配、全部hybrid/seed求值、Jacobian与注意图、共享memory/heads均付费；main未充分硬件/端到端预算不补，不采用生产/高分辨率提升。

actualCh24已有noise目标/continuous-denoising路线与cache/dense近似，却没有“给定context的conditionalmean→aggregator/predictor条件分解；局部性定理限GMRF与branch/whole residual辨界”。唯一MULTIMODAL-GENERATIVE-PARADIGMS，在完整“图像和视频往往容忍整体画面同时从粗到细修正…文本mutabletokens成本更明显”段后、完整“对自适应提交的diffusion模型，输出token数相同也不等采样工作相同…”段前，PRE：

> 去噪器内部还可按“聚合哪些 context、如何预测当前 patch”提出功能分解：单 attention branch 的 QK 组织空间权重，VO 搬运特征，MLP 读取聚合状态作逐 token 更新。[受限 aggregator–predictor 分析](https://arxiv.org/html/2610.29854v1)只在 Gaussian MRF 与独立噪声等条件下证明 graph-local 条件均值能逼近全局去噪；真实 DiT 的 sensitivity/attention 趋势和组件移植只是条件证据，residual stack 的交互不因代数分解而消失。共享 memory predictor 的小图单seed可行，也不授任意MLP直接替换或高噪声总要更大窗口。训练、Jacobian探测、各hybrid适配与完整生成均付费，局部context或兼容性不够时保原全局denoiser、原组件与独立生成评价，不由局部定理签发自然图泛化与无损稀疏。

当前8项必要Source及实际owner已读；W2/W7具体NC/仅报告、六个最小PRE待reader校准。作者不写Books/Report/State、不授实际POST或本日完成。
