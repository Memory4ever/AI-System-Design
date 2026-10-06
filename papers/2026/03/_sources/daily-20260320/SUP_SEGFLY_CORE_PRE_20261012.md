# SegFly17920：本20必要原证与最小PRE

resume20_author_new sole准备，仅03-20补03-19；原5分/准入day复用，不自授Source/PRE、写锁或DAY。

## 1. 精确源与读取范围

[exact-v1](https://arxiv.org/html/2603.17920v1)必要§3.1–3.4/Eq1–7、§4消费者/§5.1–5.3/T2与§6/T3–6/§7已读，current abs同七作者v2 July1/ECCV2026，无具体纠错说明，标题添Dataset及data/code available只是轻量事件字段，不全版本diff或自行授artifact核。未读全图像、完整补充训练配方、代码或复现；采用机制不依赖它们。

## 2. 最低接口与直接反側

高重叠RGB经SfM/MVS→2D标注升到semantic pointcloud→多数投票/距离kNN补全，再按每camera pose/intrinsic/distortion投影。Z-buffer→局部不同类更近depth过滤→splats→depth priority/再kNN填密，并非每pixel真值。thermal另重建、被动target标定、ICP配准pointcloud与lens/crop回映，geometry registration不等真实同时采样；静态场景/high overlap前提仍在，§5.1还用software time-sync采集，不能写成不需任何同步/标定。

动态/细结构实际不可靠：Person/Bicycle/FlyingAnimals/Cables/Cranes被转unlabeled，稀类并GroundObstacle，unlabeled人口必须保。manual586张50m供标签，all-view reconstruction与30/40m再渲染可摊销但非零总费。T2额外135RGB/60thermal人标未参与标签生成；registration60pairs将同warp施于manual RGB与thermal labels，只semantic一致性不等逐pixel几何硬证书；T5scene8 ablation用参与生成的manual标签，不代heldout评价。RGB-T val/test实际同split，不称独立调参验收。

T4 UPerNet adaptation accuracy33.48→34.74但FWmIoU32.21→31.98反退；T6 AnyThermal10→15类人口改变非同label-domain因果。consumer训练/匹配预算、precision/hardware/latency/batch/concurrency/SLO/全重建/标定/填密费用未齐；三阶段冻结RGB路径是参数分责，不授跨modal无损、实时或控制安全。

## 3. actual唯一owner与差额

sole `MULTIMODAL-REPRESENTATION`/[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)：actual853–884完整time/pose/transform身份→位置/subject绑定→M2P局部候选→估计地图；1095–1119静态groupproposal/多视图输入与开篇、相邻Ch24/26开篇已读。现文已有mask→point弱监督与对象地址，但未承载static semantic cloud将稀RGB标注跨view/modality投为派生pixel标签及offline几何注册与时间事实分责。拟元数据后200ms/augmentation完整段后、subject-binding段前两短literal。只此表示/监督来源接口，不另写Ch27数据量或Ch26飞行应用owner；reader可按actual差额改NC但不得仅主题相似。

### 正文PRE 1

空间身份还可以成为跨视图监督的中间层：高重叠且近似静态的场景中，先用多视图重建把少量RGB区域标签升到语义点云，再按各相机的pose、intrinsics与distortion投回RGB或其他传感器视图。深度冲突处理、遮挡过滤与局部填密能扩大标签覆盖，却生成的是派生监督，不是补拍的新观察；几何配准也只对齐估计空间，不使异时输入自动成为同刻事实。点云、原标签、相机标定、投影与填密规则须共同保留身份。<!-- source-family:SF-2026-ARXIV-2603-17920 -->

[有限跨传感器标签转移](https://arxiv.org/html/2603.17920v1)仍对动态对象和细结构存在缺口，部分类别被置为unlabeled；静态对齐分数不批准这些对象，也不保证下游每项指标改善。应分开标签生成、参与制备的数据和独立人工检查，保留未标注人口；重建、传感器标定、配准、填密、训练与回归全计费。场景变化、标定或覆盖失配时，回到原视图/时间戳、真实标签与独立传感器消费，不让离线几何一致性代替视觉事实或控制安全。

### 静态来源注PRE

- [SegFly2603.17920 exact-v1](https://arxiv.org/html/2603.17920v1)：必要§3/Eq1–7、§4消费者、§5/T2及§6/T3–6。仅静态semantic pointcloud跨view/modality派生标签与空间/时间身份分责；保动态细类unlabeled、标定/软件同步、制备/额外人工人口、同val/test、下游反退与全费用，不采逐pixel硬配准、无同步/标定、普遍无损或控制保证。current-v2无具体纠错说明，未核全图像/补充配方/代码或复现。<!-- source-family:SF-2026-ARXIV-2603-17920 -->

必要Source/actualowner/两literal待非preparer裁，尚未写Books。

## 5. resume20_author_new实际窄写（writer，非POST）

root soleCh23本family窄锁批准后复用reader§4 Source/owner/两PRE PASS。写前853–875/末7、写后853–882/末7完整顺读，原两literal/static逐字落868/870/static1838，机械唯一各1、限定diffcheck0。time/spatial/provenance元数据→static语义标签跨视图→位置/subject身份→mask点对应链顺接；动态细类unlabeled、标定/异时/费用边界近文保持。不扩source、不改身份注，交reader一次nonwriter完整局部与本人/邻注actualPOST，writer不自计I/DAY。

## 4. resume20_reader_new非准备者必要Source/actualowner/两PRE裁

2026-10-12实际exact-v1必要§3.1–3.4/Eq1–7/L117–177、§4消费者/L178–183、§5.1–5.3/T2/L184–217、§6/T3–6/§7/L218–280及current同七作者v2轻量说明读。只派生监督与几何/时间分责，不核全图像、全部补充训练/代码或复现；v2添加Dataset/data-code事实不授artifact核、无具体纠错不机械全diff。

高overlap静态SfM/MVS、少量RGB标签lift/多数投票/kNN、z-buffer/遮挡/depth填密、独立thermal重建/标定/ICP与warp成立。空间registration不等同时采样，§5.1实际software sync与所有标定费仍保；动态细类unlabeled、额外135RGB/60thermal人标与参与生成的scene8 ablation、同val/test分账已核。T4 adaptation的UPerNet FWmIoU退步、T6 class人口变化不授同任务因果，原两PRE/static保反侧/身份/全部费用，不采硬配准/无同步/普遍无损或控制安全。

实际Ch23完整850–895 time/pose/provenance→200ms/augmentation→subject绑定→M2P/估计地图/位置编码及开篇、Ch24/26分责有效读域复用。既有对象地址/弱点目标不承载static semantic cloud跨view/modal派生pixel标签的具体来源链，soleCh23差额成立；拟元数据完整段后两PRE再接subject身份顺读成立，不新写数据/飞行应用owner。**必要Source/actualowner/原两literal/static有限PASS**，原5/day不动，rootsole锁后才可写，仍需一次实际非writerPOST；不预I/DAY。

## 6. resume20_reader_new一次非writer实际POST

复用§4有效Source/owner/PRE，不重原证。rootsoleCh23授权作者实写后，完整858–888元数据→200ms/augmentation→新868/870→subject两段→M2P两段/估计地图交接，以及1828–1838本人/VirPro/PCA-Seg/MCoT/SCEP/VLM2Rec邻注顺读。原两literal/static逐字机械唯一各1；本family六新增与先前已验VirPro六新增分账、cached/unstaged diffcheck均0。派生标签/时间事实分责、静态/动态unlabeled、标签生成/独立人工人口/下游反退与全费近文保持，不授同步/硬配准/无标定/普遍无损或控制保证。**一次有限actualPOST PASS**，交root接纳释放soleCh23，不自计I/DAY或改静态身份。
