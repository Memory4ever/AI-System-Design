# 第二十五包：AB13 四项必要证据与实际 owner（待非作者复核）

35safe不增；没有Books lease。这里只记录已读支持/直接反侧、具体owner差额与拟采用范围；公式子命题隔离不自动升级为全篇争议。没有读取全部proof/artifact，也没有默认比较revision。

## 23353 SOTAlign：拟2+2+2=6，Ch23少量配对锚与未配对几何一段

[exact-v1](https://arxiv.org/html/2602.23353v1)必要blocks29–82/83–110/120–126及263–304实际读；后段只因主公式与局部梯度不一致定点查证。少量paired数据先训练CCA/Procrustes/linear-contrastive teacher，再让unpaired图像与文本的student maps学习同空间；新分支保留teacher的OT transport geometry，而非每行取argmax当InfoNCE伪配对或要求严格CKA。冻结DINOv3ViT-L/NVEmbedv2、global CLS+meanpatch，1024维linear map；teacher CCA eigenregularization .1。这使弱配对监督可以迁为集合级soft关系，不赋予teacher语义真值或未见域无损可识别性。

独立复核纠正旧材料误读：主Eq12（block74）明确为 KL(teacher OT || student OT)，与 Appendix C.4 同向，不存在原记录的 KL 方向冲突。真实受影响对象是主Eq13梯度分母写teacher epsilon*、Appendix294/301/303写student epsilon；配置 teacher .01/student .05，不能当相同记号。只采用两阶段几何蒸馏接口和作者有限经验，不采用所写统一KL梯度、等价性或内存消除保证。未核实现，不称代码必错；精确重开需所运行温度与对应梯度明确一致。

Table1固定encoder/CC3M关系的局部控制：CCA noSSL21.5、CKA23.5、InfoNCE24.1、KL-OT30.3，contrastive teacher24.2→28.5；Table4 COCO检索26.5/34.1 vs同10K-paired SAIL21/27.4，但1M-paired上界35.5/45.5更高。不把基座/调参人口不同的全表排名写为唯一因果。100paired时两分支都失败，1000～10000paired收益递减；unpaired越接近train域越好只是受限关联，不证Platonic真空间。10Kpaired、最多1MunpairedCC3M、batch≤32K、LION最高1e−4/wd1e−5/cosine2000iterations、alpha∈1e−3/4/5由CC3M validation选择、A10080GB；precision、多seedCI、总墙钟Not Disclosed。两encoder、teacher、Sinkhorn100iterations与大batch均计费，weak/bias anchor或域偏移时保留真实paired、原encoder与简单map。

actual `MULTIMODAL-REPRESENTATION` Ch23 59–82完整小节邻接实际读：已有配对identity、共同正交reference/cycle、residual校正、跨模态kernel强假设与partial projection边界；595–626拥有不同alignment目标与caption限制。尚无 **paired teacher的transport关系迁到unpaired student、soft集合关系替代hard伪pair而继承teacher偏差** 的具体条件。拟在共同reference链附近单段，只保epsilon梯度子命题隔离；主Eq12方向经独立复核无冲突与两stage费用，非为论文名造gap；root若判现有论点已足承载可Existing。

Submitted2026-02-26T18:55:06Z、same-ID registered2026-02-27T03:08:47Z；结合已核官方公告下界，arXiv事件09:00～11:08:48+08。current ICML2026后续说明不凭acceptance倒推旧public。

### 23353 独立必要复核与 Books 处置

非原 packet 作者 feb28_ch23_finish 从 exact-v1/本地 primary blocks29–110、120–126 独立读方法、控制、设置与反側；286–304 仅为温度梯度定点核验，没有扩成全 proof/artifact 或 revision 对比。旧准备意见不作通过结论；评分2+2+2=6保留。实际 Ch23 已有 paired identity/共同 Procrustes/kernel 条件，却不含“paired teacher 的 soft transport 关系传到 unpaired student，并继承弱 anchor/域偏差”接口；因此不是泛化 No Change，Books Decision 为具体深入。正文只增加该窄段，费用与真实 paired/原 map 回退近文；温度分母公式子命题隔离，不隔离可读材料或全部候选。独立必要原证/actual owner PRE完成；正文/完整邻接/自身末注作者已顺读，root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放，非日级验收。

## 23358 A Dataset Is Worth 1 MB / PLADA：拟2+2+2=6，Ch27共享raw基座上的task payload一段

[v1](https://arxiv.org/html/2602.23358v1)22–62/66–111/175–193/115–125必要源实际读；压缩表随所读块展示，不另逐表扩审。旧模型或合成数据传输适合独立接收方；若各接收方预装相同ImageNet raw reference与pretrained backbone，server target teacher只传subset index与hard pseudo-label，让receiver自己训练。新选择是 **以共享reference identity和本地训练换task通信payload**，不是文本编码本身的新机制，也不是整任务成本<1MB或通用model-independent无损迁移。

ConvNeXtV2-tiny IN21K teacher目标fine-tune；receiver ResNet18 pretrained IN21K/IN1K，分别5/30epochs，A5000、AdamW1e−3/cosine。low-energy保留参考子集在远OOD会让pseudo-class collapse；按teacher pseudo-label计Nc、quota Kc∝Nc^alpha校正不是groundtruth class覆盖。alpha<0时Nc=0与quota取整仍须分支，不授硬保证。Table3同1%budget energy+quota使RESISC58.16→75.65，却Aircraft53.62→44.58、Food75.50→71.66；CUB也82.49→80.53。远OOD切片只作为通用proxy失效诊断，不采用科学/医学应用路线；该反侧足以限制“highconfidence都可传”。

bitmap仅14.2M reference索引已1.69MB；delta/RLE+Zstd19用于实际payload。Appendix Table192的1%为84.83～206.08KB，.5%45.48～108.84KB，不混成45～200KB同预算。Table2 Food的DD77.6高于本法75.5，不能全基线胜出。1%local训练约20min/A5000、≥25%可3days；预装raw、backbone、teacher训练、local算力和压缩都在通信数之外，precision/总墙钟/严格seed不确定性Not Disclosed。duplicate检查按pixel统计bucketing再L1阈值，不能排除重编码重复或pretraining exposure；25Pets/2Caltech test交叉并非零污染证明。

actual `TRAIN-DATA` Ch27 105–146、237–267完整邻接实际读。已有q(x)、train/store分配、reuse、quality proxy选择与分布改变；尚无 **原始reference已共享时index+label是条件化传输产物，其teacher类别quota与隐藏preload/receiver训练费用**。拟数据分配处一段，而非在Ch76或模型压缩重复；energy失准/缺共同raw identity/本地预算不够时回退显式数据、模型artifact或独立标注，不让payload认证任务保真。

Submitted2026-02-26T18:59:03Z、registered2026-02-27T03:08:54Z；arXiv事件09:00～11:08:55+08。current必要说明未见具体撤回/早公开信号，不造全部版本已核。

## 23360 Model Agreement through Anchoring：拟2+1+3=6，Ch5预测空间agreement条件一段

[v1](https://arxiv.org/html/2602.23360v1)11–18/61–96/218–232/44–45/247–278实际读，最后局部只核midpoint closure与强凸假设，不遍历allproof。旧agreement若靠两模型都接近真值解释，就依赖低绝对risk；新分析用midpoint anchor给prediction disagreement bound，即使绝对risk不小。MSE恒等式D=2(Rf1+Rf2−2Rmid)，若两预测器是Fn上epsilon近population最优、F2n含其midpoint，则D≤4(R(Fn)−R(F2n)+epsilon)。ReLU DAG构造以double graph到2n建立closure，不是same parameter平均，也不是任意LLM token agreement law。

强凸扩展要求loss在prediction上mu>0、连续可微和可行midpoint；不是网络参数目标强凸。独立训练数据iid同P、agreement也同P；global population近最优不能由普通SGD的empirical loss替代。高agreement仍可两者都错：f1=f2=0而y=1时D0/MSE1。原232的log-range表述还依赖初始risk≤1归一，不能当无尺度通用bound。交叉熵logits不具全域统一强凸，不能转授所有loss。理论无硬件/precision实验人口，不机械要求运行benchmark，也不称优化器达到条件已证。

actual `WORLDVIEW-REPRESENTATION` Ch5 122–161及421–436完整相邻论证实际读：已有inductive bias/shortcut、目标错配、几何诊断非泛化、probe/行为不等真概念。尚无 **prediction-space midpoint anchor将agreement与可扩模型族的risk差关联，而非与低绝对误差等同**。拟归纳偏置处极窄条件段，不落成agreement认证truth；条件不可核就保留独立held-out/OOD与真实错误率。若现有泛化诊断边界已充分，可Existing有效，不为定理名追加。

Submitted2026-02-26T18:59:32Z、registered2026-02-27T03:08:56Z；arXiv事件09:00～11:08:57+08。

## 23361 VGG-T3：拟2+2+2=6，Ch23离线scene fast-weight表示一段

[v1](https://arxiv.org/html/2602.23361v1)29–59/61–88/99–106必要方法/对应控制/直接反侧实际读。离线whole-view collection bidirectional global attention可由固定SwiGLU MLP fastweights承载，再冻结服务新query；不同于causal streaming memory。whole batch/shards都从同theta取梯度后SUM更新，训练1innerstep/推理2，QK L2不带learned参数；V的3×3 ShortConv2D破坏逐token K/V线性平凡拟合前提，conv本身不因“ShortConv”就数学非线性。

所写inner loss L=T_theta(k)^T v并minimize的符号与促进alignment目标有歧义，只隔离该公式，不称所运行代码必错；重开需objective符号与实际实现对应。57称all-to-all、77称DDP update-only，不自造具体collective协议。102明确global QKV/output projections与新增TTT一起训练、其他VGGT参数冻结，不能按62笼统称所有原projection冻结。

固定MLP不等全scene/query O(1)：105仍保留所有mapping camera tokens，query camerahead继续softmax；QKV/offload/input或输出状态亦随N增长。Table6相同small224/2–24views：softmax CD.061/mAA76.33，ours.074/72.16，加ShortConv.066/74.14仍不及softmax。Table1七sceneCD.030>.024、ETH.480>.279，Table3 TUM poseATE.037差于VGGT.012/TTT3R.025；ordered/unordered评价又非同protocol。Table4 singleGPU1500views ours173.1s慢于TTT3R90.1s；1000view58s对11min是该A10080GB局部结果，不外推全部query/端到端成本常数。

100Ktrain8A100、训练2–24views/约48images每GPU、longside518/jitter、GT covisibility>.3；outerAdamW1e−4/wd.05/betas.9/.95/warm1000/cosine1e−6，innerMuonlr.1/NS5、dim1024hidden4x；作者12%训练比率不提供完全可比预算。precision/seedCI/全墙钟Not Disclosed，GT数据选择、offline write、camera state与多GPU协调仍计费；几何评价Sim3/关键帧人口不签物理真值。

actual `MULTIMODAL-REPRESENTATION` Ch23 848–900完整scene/camera身份邻接实际读；Ch22 638–664完整test-time写入目标作为交接只读。Ch23已有3D primitives/sidecar/track持久表示，但没有 **离线多view写入固定MLP与显式camera-token旁路并存、写入全量可并行而查询仍付scene-state费** 的具体分支。此稿唯一owner拟Ch23，Ch22已拥有通用fastweights目标不重复推导。保softmax精度反侧、固定MLP非完整状态常数与训练/离线写入费用；重建或pose质量/预算不合算时保显式view attention或专用3D pipeline。未核artifact，不能授生产状态协议。

Submitted2026-02-26T18:59:33Z、registered2026-02-27T03:08:58Z；arXiv事件09:00～11:08:59+08。current CVPR2026说明是后来会议线索，非早公开证据。

### 23361 独立必要复核与 Books 处置

非原 packet 作者 feb28_ch23_finish 独立读 exact-v1/primary blocks29–59、61–88、99–106，限whole-view写入、查询接口、small-scale消融、pose/large-scale反侧和运行设置，不扩全proof/artifact/revision。2+2+2=6保留。actual owner Ch23已有native geometry/track state而没有离线MLP scene写入与camera-token旁路并存，Ch22只拥有通用写入目标；Books Decision为具体深入，在3D状态链增加窄段，不授causal streaming或完整query O(1)。Camera tokens随N增长、pose退步/pointmap head替代、softmax更强切片与离线训练/梯度通信费用近文；dot-product目标符号与all-to-all/DDP口径隔离，不判代码必错。独立必要原证/actual owner PRE完成，作者实际正文/完整邻接/自身末注已读，root非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放，未核实现或复现，非日级验收。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）本项落实：23360：2+1+3=6，prediction midpoint/population近最优与闭包，agreement非truth；必要原v1/直接反侧与actual owner独核，Ch5正文161/自身640及完整邻接root非写入者actual POST通过；23358：2+2+2=6，共同raw reference上index+pseudolabel payload，非任务TCO；必要原v1/直接反侧与actual owner独核，Ch27正文140/自身1572及完整邻接root非写入者actual POST通过。保原有效身份/精确版/采用命题，必要原段见本项；作者已实际顺读，费用、人口、错误子保证和原路径回退近正文，窄锁释放；不授全附件/实现复现或日级。
