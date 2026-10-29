# VirPro17470：本20必要证据与有限PRE

resume_mar17 sole准备，仅03-20补03-19自然日；原准入/day与2+1+2=5复用。不自授Source/PRE独核、Books写锁、I或DAY。交resume_review17_18非准备者必要核。

## 1. 精确源与停止范围

[VirPro exact-v1](https://arxiv.org/html/2603.17470v1)，Visual-referred Probabilistic Prompt Learning for Weakly-Supervised Monocular 3D Detection。实际必要§3 L92–164/Eq1–11、§4 L165–231/Tables1–6、§5 L232–235、Supplementary§8 L308–315/Eq12–13、§10 L372–375及§11 L377–387已读。current abs实际同五作者v2 Mar20/CVPR2026 Findings接受，无具体纠错说明；不因版本号机械全diff，采用仍v1。未读无关图像、完整其他附录、代码或复现；支持/直接反側够本接口即止。

## 2. 真实训练与消费者接口

固定类别文本不能表达同类实例的场景差异。Stage1以2D检测ROI/弱空间信息为边界，每对象可学习多scenario prompt bank；object token随机位置、冻结CLIP文字encoder，mean经文字残差MLP/self-attention，variance读取视觉特征。重参数化Gaussian采样后maxpool成ROI文本embedding，同一ROI图文作为正对，其他batch ROI进入对比目标。§8 L315明确同i正对，Eq12裸sim_ij的j记号不完整，不能自行补成所有同场景对象正对。scene-consistency与方差只作者目标/代理，不授语义独立、校准不确定性或完整场景真值。

Stage2用D2OD MSE把预训练表示迁移给单目3D检测encoder，保留既有弱监督3D pseudo-label训练。没有额外prompt模块运行不取消预训练/蒸馏/2D检测/空间标签费用，也不等无LiDAR或无3D监督。学习的条件文字表征仍来自ROI人口与空间标签，非开放世界任意框的可靠接口。

## 3. 有限评价与直接反側

KITTI raw33530图预训练、3711训练/3769验证/7518测试。Table1作者val/AP40/IoU.5协议不与test headline合并；VirPro+WeakM3D在BEV55.09低于58.20，虽3D50.97高于50.16，不能采全指标改善。Table2不同监督人口的Hard3D 3.64与WeakMono4.45不当匹配因果消融。Table3 multi的HardBEV28.55低于single29.58。Table4有限maxpool消融支持选择但不证明方差真实；Table6 CH2.62/2.54与负Silhouette -.498/-.630仅聚类代理，不是uncertainty calibration。§5直接承认框不准确、背景crop和分辨率偏差会影响提示。

预训练单4090/25epochs/B16/AdamW1e-4/冻结CLIP/NROI4，32prompts中随机抽8个构造ROI embedding；Eq5的Ns未固定为每prompt8次采样；下游WeakM3D50epochs、GGA120epochs。训练人口、backbone、标签和baseline预算不可合并为一个无损因果提升。precision/完整硬件、总标注/LiDAR/检测/CLIP/promptbank采样/蒸馏/训练/独立回归成本及推理SLO Not Disclosed，不采用headline速度/免费部署。

## 4. actual唯一owner与逐字PRE

sole `MULTIMODAL-REPRESENTATION`/[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。实际开篇1–33 raw表示身份、769–790 caption/DeBias/FineViT区域监督→三alignment目标完整邻接已读；Ch24/26开篇及Ch25 1–25交接已读。FineViT拥有真实/生成bbox-文字/OCR地址监督与下游权限，尚未承载同ROI视觉条件Gaussian prompt→maxpool文本对比→弱空间标签下游迁移的具体分支。不是同样“局部监督”主题即NC；仅区域语义辅助表征归Ch23，不把3D检测指标扩为WorldModel transition或控制安全。拟FineViT第二完整限制段后、三alignment目标前两段，待root窄锁；没有写Books。

### 正文PRE 1

有区域框但缺少细粒度文字描述时，也可保留固定类别提示作为低成本基线，再学习实例条件的文字辅助表征。一条受限分支为每个ROI维护多组场景提示，冻结文字encoder，以提示特征产生均值、以同一ROI视觉特征产生方差，采样并汇聚为该实例的文字embedding，再与同ROI图像表示作对比训练；下游把预训练表示蒸馏给检测encoder，同时保留弱空间标签与既有训练目标。改变的是局部图文正对和监督传递接口，不是让采样方差自动成为真实不确定性，也没有取消区域框、空间标签或视觉先验。<!-- source-family:SF-2026-ARXIV-2603-17470 -->

[有限区域提示证据](https://arxiv.org/html/2603.17470v1)来自弱监督单目3D检测：更多提示和迁移后的表示并非所有难度或BEV/3D指标都改善，聚类分数也不证明场景一致或语义独立。ROI错框、背景混入和分辨率会共同影响文字条件；检测器、空间标签、提示采样、预训练、蒸馏及下游回归都付费，运行时不保留提示模块不等于全流程免费。应分别验收区域表征、空间预测与独立质量/成本人口；条件、标签或净收益失配时保留静态类别提示、真实区域监督和原检测encoder，不让概率形式代替视觉事实或物理执行保证。

### 静态来源注PRE

- [VirPro2603.17470 exact-v1](https://arxiv.org/html/2603.17470v1)：必要§3/Eq1–11、§4/Tables1–6、§5及补充§8/Eq12–13、§10–11相关接口/费用。仅ROI条件提示分布→同ROI图文对比→弱空间标签下游表征迁移；保方差非真不确定性、正对记号边界、错框/背景偏差、BEV/难度反退和全部费用，不采完整场景真值、无空间监督、所有指标无损或物理执行。current-v2无具体纠错信号，未核代码/图像或复现。<!-- source-family:SF-2026-ARXIV-2603-17470 -->

必要Source/实际owner/PRE仍待非准备者裁；未授写入前不计安全处置。

## 5. 非准备者必要Source/actualowner/原两literal裁（resume_review17_18）

2026-10-12只本20，实际exact-v1 §3/Eq1–11、§4/Tables1–6/设置、§5和Supplement8/Eq12–13、10–11直接接口/反侧、current abs已独读；不授全部图像、附录、代码或复现。Mean由prompt residual/self-attention，variance读visual-language context，sample/maxpool及同ROI正对、D2OD MSE与原pseudo-label loss共存实际成立；方差和scene cluster分数不认证uncertainty/真实语义独立。Table1 WeakM3D+VirPro BEV55.09<58.20、Table3 multi HardBEV28.55<29.58和非匹配监督Hard人口保留，不照录全指标改善。Eq12裸j不完整但315明确同i正对，不扩大为同scene全部互正。主文179是32prompts中抽8，非每prompt8 samples；准备笔记两处WeakEasy/每prompt8已窄纠并实际定点回读，原无数值两literal/static未改。

actualCh23完整759–798 caption/DeBias→FineViT区域监督→三alignment目标和1–28、相邻Ch24/25/26开篇分责已读/有效复用。既有区域监督不承载ROI条件Gaussian文本辅助分支→局部正对→弱空间label消费者差额，sole Ch23拟FineViT限制完整后成立。原两literal/static有限Source/owner/PRE PASS：保prompt来源/visual variance权限、错框/背景/分辨率、LiDAR/空间label与全生命周期费用，不授场景真值、无监督/全免费、校准或物理执行。原5/day不动，未写POST不计I/DAY，支持与直接反侧足采用命题即停。

## 6. resume20_author_new实际窄写（writer读回，非POST）

root恢复后授本family唯一Ch23窄锁，复用§5必要Source/两PRE PASS，不重核心。写前完整756–798与末12已读；仅原两literal逐字落789/791（FineViT完整限制后、三alignment目标前），本人静态注1832。写后完整767–801及末10顺读，原两literal/static各唯一1份逐字机械一致，限定diffcheck0；局部区域表征→弱空间consumer与三alignment目标衔接成立，方差/场景代理不授真值或物理执行。交reader一次nonwriter实际正文/完整邻接与本人/邻注POST，writer读回不代独核、不自计I或DAY，不新增身份流程注。

## 7. resume20_reader_new一次非writer实际POST

2026-10-12复用原§5已通过且未受影响的Source/owner/原PRE，不重读源。实际完整Ch23 779–805（页面/形式→DeBias→FineViT完整两段→新789/791→三alignment目标及下文目标接口）及1822–1832本人/CC/VLM2Rec/SCEP/MCoT/PCA-Seg邻注顺读；两正文与本人静态注逐字机械回对批准PRE，各唯一1份。限定unstaged diff只有本family两正文＋一注六新增、cached/unstaged diffcheck均0；旧正文与所有邻注保留。

局部ROI条件文字辅助分支的监督来源、同ROI正对、弱空间label消费者、方差非校准、错框/背景/分辨率、反退与全费用近文明确；FineViT区域监督后接文字条件分支，再回三种alignment分责，顺读成立。不授场景真值、全部指标无损、无空间监督/免费或物理执行。**一次有限actualPOST PASS**，仅交root接纳并释放soleCh23锁，不自计I/日级完成，不改静态审阅身份或再建身份循环。
