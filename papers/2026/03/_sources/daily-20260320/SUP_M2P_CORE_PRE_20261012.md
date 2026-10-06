# M2P2603.17813：本20必要Source与最小PRE准备

准备者resume_review17_18，仅03-20补03-19自然日。原2+1+2=5及准入/date复用本日独核§30；不自授Source/PRE PASS、安全完成或DAY，未写Books/Report/LS。请resume_mar17非准备者裁有限分采或中心暂缓，root协调窄锁。

## 1. 精确原证与停止范围

[M2P exact-v1](https://arxiv.org/html/2603.17813v1)，当前[abs](https://arxiv.org/abs/2603.17813) L8–28同题七作者/完整AB、单v1、无具名纠错/withdrawal；Submitted03/18不是firstpublic，已有日级夹证不重开。代码“upon acceptance”只是公开计划，不冒实现核验或访问受阻。

actual必要读取：III-A–D L90–210（Eq1–13/Alg1/三种消费路径），IV/TableI–VI L211–316，V/TableVII–IX和VI限制 L317–384，直接相关Supplementary L386–411/Eq14–20。恢复前有效必要读保留，本次定点补283–298 TableIV/V缺段、回对124–202和386–411决定性公式。不是全references/所有图像像素/外部代码或复现；没有版本全diff/新query。只拟采用下列局部接口，支持和直接反侧已够即停。

## 2. 支持的局部接口

静态VFM的语义相似度不足以替逐点跨帧对应；VOS对象mask又只标区域而无点轨迹。一条弱监督分支在模板mask内按坐标聚类、FPS采点，从同一VFM的相似度匹配中取每组3对高置信对应，拟合局部旋转/平移/统一尺度，传播为组内其余点的结构目标，以Huber项约束预测。这个目标来源是模型匹配和局部相似变换假设，不是独立点标签、真实刚体运动或遮挡证据。局部非刚体形变、错误种子与遮挡可违反假设。

另两项使用真实给定的mask而不是track标签：MLC取归一化相关图落在目标前景的质量，仅质量≤0.5时惩罚，允许边界部分出界；MBC比较组内归一化边界距离并提高模板近边界点的权重。它们约束前景/边界代理，不保证每点身份正确或全部点硬落前景。训练更新VFM各block的LoRA和两卷积点模块；不是仅增加一个部署阈值或冻结全部视觉表示。

三类consumer分账：直接弱监督tracking不再做额外synthetic TAP fine-tuning/TTO；M2P-Chrono仍在Kubric合成数据上再微调；M2P-Tracker替换Delta-DINO的motion adapter并保留DINOv2-L/14语义VFM，增加1×1 channel mapping与点模块，最后六层QKV LoRA test-time优化。不能把三类成本/权限合成一个“无点标签且无需适配的免费tracker”。

## 3. 评价、直接反侧及精确recipe隔离

- 预训练body/TableIII为3.4K YouTube-VOS/DAVIS训练videos；AB/introduction称3.6K，两口径不强合并。TableIX MoreData额外MOOSE数据集自身3.6K，是不同实验，不认证联合D+Y+MOOSE总量3.6K。原文说DAVIS训练与TAPVID test无重叠，不把这写成完全没有heldout。2RTX4090约一天、AdamW/B16/150Kiter/LoRA QKV-Proj-FC等是作者recipe；patch14/16与grid分辨率不同，III-D S/16和IV实现S/14还有配置差，不授精确统一部署规格。
- TAPVID DAVIS30、Kinetics1189为具有人标点track的评价；位置delta、occlusion OA、joint AJ分别验收。预训练无点标签不等评价不需要真实点标签。TIII DINOv2-B38→50.8与v3-B38.9→53.5是12.8/14.6百分点，且baseline零样本和额外VOS/LoRA/point-head训练预算不同。RGBStacking M2Pv3-B58低于Chrono67，不授全人口最优。
- TIV/V M2P-Chrono平均改善但Kinetics最细delta0 30.8<32.2，作者归因patch16vs14尚不授独立因果。TVI TTO deltaAvg79.1<80.4，虽然AJ65.4>64.6/OA89.8>88.1/BADJA72.9>72.4。2500vs10000iterations不等4×walltime；每video .7h vs .9h RTX4090是优化费用，不是fresh frame/controller deadline。0.5M/7.6M是trainable，不是全部驻留；原预训练/保留语义VFM、adapter与在线优化全费仍在。
- TVII LSC主要增量与MLC/MBC有限消融支持局部组织效果，不证明局部刚体或点真值。TVIII更高LoRA rank非单调，TIX直接点伪标签45.6<group-transformed50.8但多数据只有有限增量。VI明确distractor/强形变仍失败，memory future不纳为已有功能。CI/seeds、完整latency workload/batch/concurrency/SLO、所有硬件运行成本Not Disclosed，不授普遍稳健/实时/无损。
- **决定性公式桥不采：** Eq14/6写列向量target≈s R source+t；Eq18定义H=targetCentered·sourceCenteredᵀ，SVD H=UΣVᵀ，但Eq19用V D Uᵀ，方向与这个H的列向量映射相反。自构三点反例取单位圆等边点(1,0),(-1/2,√3/2),(-1/2,-√3/2)，target为其90°旋转，均值0，source协方差1.5I，H=1.5R90。Eq19给R90ᵀ、Eq20 scale1，拟合残差平方和12；合法R90/scale1残差0。退化奇异值不消除该反例：任何SVD的UVᵀ均为唯一polar R90、VUᵀ均为其逆。该反例针对**论文所印方向与closed-form optimal声明**，不证明作者实际代码必错或实验无效。Eq20 traceΣ在反射排除时也未带D，精确可微recipe不授；不由此降分或假EX/NC。

**一次精确重开请求：** 若要采用可执行最优Procrustes公式/其gradient或精确复现recipe，请提供与Eq14–20一致的target/source约定、rotation/determinant-corrected scale和非退化旋转/反射测试，连同训练实际实现；当前不采用这条桥。下列PRE只保“模型候选→局部拟合结构目标＋mask代理分验”有限接口，不照录Eq19/20、最优性或可微实现保证。非准备者若认定该有限接口不能分采则保原5中心暂缓，不以耗时/已有覆盖关闭。

## 4. actual唯一owner/差额与逐字PRE

sole owner `MULTIMODAL-REPRESENTATION` / [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。actual完整829–854时间/空间身份、pose/mask绑定→估计地图→空间规划邻接；定点85–91跨encoder Procrustes已有原则、952轨迹tokenizer、1112SGCoT消费者已有论点已读，不重核这些材料Source。Ch22长上下文、Ch24生成、Ch25环境转移及Ch26动作开篇边界只作交接：此处训练视觉对应表示，不复制点轨迹消费者或控制安全owner。既有mask不能签instance真值已经覆盖，但未承载**对象区域弱标与同模型候选局部结构/前景mass/边界约束共同训练点对应**这一具体接口；拟窄两段，非新增tracker章。提议位置Ch23 pose/mask绑定完整段846后/显式地图848前，保留原论点。

### 正文PRE 1

对象mask还只能指出区域，不能直接给出区域内每个点的跨帧身份。缺少点轨迹标注时，一条弱监督分支在mask内分组采点，由视觉表示先提出少量高置信对应，再用局部旋转、平移与统一尺度拟合成组内结构目标；同时约束相关图落在目标前景的质量和相对边界距离，更新视觉adapter与点匹配head。新增的是“模型候选如何变成受区域约束的训练目标”，不是从mask恢复真实点轨迹。高置信候选仍可能错误，局部相似变换也不适合任意形变与遮挡；前景质量和边界代理不能替点对应真值。<!-- source-family:SF-2026-ARXIV-2603-17813 -->

### 正文PRE 2

[Mask-to-Point的有限对照](https://arxiv.org/html/2603.17813v1)需分开直接弱监督tracking、合成数据再微调和test-time优化三种消费路径；细粒度位置与部分域/优化指标仍有反退，不能由平均提升签发全部点或遮挡正确。给定mask、伪对应筛选、局部拟合、adapter/point-head训练和在线优化都付费，较少trainable参数或优化轮数不等全部驻留、完整墙钟或控制deadline。原文精确旋转公式与坐标约定尚有冲突，不照录为可执行最优recipe；应分别验收点位置、可见性和完整消费者。对应或运动假设失配时，保留原帧、真实点监督/已有tracker与独立评价，不让区域一致替真实轨迹和动作授权。

### 静态来源注PRE

- [M2P2603.17813 exact-v1](https://arxiv.org/html/2603.17813v1)：必要III-A–D/Eq1–13/Alg1、IV–V/TableI–IX、VI和Supplementary Eq14–20。只采用对象mask弱标下模型候选局部结构目标及前景/边界代理分验；不授点真值、任意形变/遮挡保证或精确Procrustes recipe，保旋转方向冲突、人口/配置/精细位置反退、三种consumer和全部费用。未核artifact/复现。<!-- source-family:SF-2026-ARXIV-2603-17813 -->

## 5. 非准备者裁待执行

请resume_mar17独核必要支持/直接反侧与上述旋转反例、actual唯一owner/两literal/static；未裁、未root新锁不得写Books，未一次非writer actualPOST不计I，无DAY。原5/date保持，不展开全部图像/代码/其他版本。

## 6. resume_mar17 非准备者必要Source/owner/PRE裁

2026-10-12 实际独读exact-v1 III-A–D/Eq1–13/Alg1 L90–206、IV/TI–VI L207–321、V消融TVII–IX/VI限制 L326–376及Supplementary Eq14–20 L386–411，支持与直接反侧够证即止，没有全部图像、外部代码或版本比较。原两literal/static有限Source/PRE PASS，保2+1+2=5。自构等边三点→90°旋转独算：源协方差1.5I、H=1.5R90，所印VUᵀ是逆旋转；其残差平方和12而合法正向0。反例非退化、针对所印公式/optimal声明，不推实际代码错误或全部实验无效。

MLC确为目标前景概率质量≤.5才惩罚，MBC为归一边界距离代理；LoRA和point module更新、模型自身候选与区域标签不是点真值。训练3.4K、AB3.6K口径保留；原笔记MoreData窄澄清：L369写额外MOOSE数据集3.6K，不能从它直接确证联合D+Y+MOOSE总量3.6K，此数不在PRE。细粒度Kinetics30.8<32.2、TTO位置79.1<80.4与OA/AJ/BADJA不同指标、RGBStacking反退，rank128低于64、强形变/干扰仍失败，都保留。三consumer的合成再微调和TTO权限/全费不合并，.7/.9小时是每视频优化而非fresh deadline。

实际Ch23完整840–865和跨encoder Procrustes既有82–91顺读，Ch22/24入口及ROADMAP明确表示owner：旧pose/mask空间绑定与估计地图没有承载模型候选局部结构目标和前景/边界共同训练点对应的具体差额。原两PRE只采用该有限接口，不依赖Eq19/20的精确最优配方；原一次坐标/rotation/scale及实际训练实现请求保留。因此可分采而不是全篇center/假NC，root授Ch23窄锁后才能写，actual非writer POST前不计I或DAY。

## 7. resume_review17_18 授权后writer实际落实

2026-10-12 root授sole Ch23本family两原literal/static窄锁后，实际读取现有830–866及末尾来源邻注，在SF2601-11096完整两段之后/显式地图之前逐字写入两PRE。实际正文新850/852、自身静态源注1798；写后完整838–864及末9行回读，语义与原两literal/static一致，既有地图/空间规划和来源注保持。限定diff仅本family两正文+注六新增行，章numstat118/0→124/0、git diff --check无输出；未stage/commit/push。此为writer读回，不自授POST/I/DAY。请resume_mar17一次非writer完整838–864及1790–1798（本人与并发邻注）POST回对有效Source/PRE，由root接纳释放后再处理同章其他family，不合并CC-CDFSL。

## 8. resume_mar17 一次非writer actualPOST

2026-10-12 实际完整读Ch23 838–864（pose/mask空间绑定→新850/852弱mask点对应→估计地图/空间规划）及1790–1798本人与FineViT/并发来源邻注，逐字回对§4两literal/static和§6已有效必要原证。新增两段及静态注一致；对象区域不等点轨迹、模型候选与相似变换假设、前景/边界代理、旋转方向未采、三consumer与全费用/精细位置反退均近文保留；没有把地图或动作授权混入表示owner。限定git diff --check无输出。有限actualPOST PASS，交root接纳释放；不改Books身份注、不授DAY。
