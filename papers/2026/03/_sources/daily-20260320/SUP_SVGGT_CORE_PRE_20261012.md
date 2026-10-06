# S-VGGT17625：离线多视图的结构分组与共同参照 / 必要准备

resume_review17_18，2026-10-12，仅03-20补03-19；author明确本family sole准备分工，原2+2+2=6及独核§30准入/date有效复用。准备者不自授Source/PRE、safe/I或DAY，不写Books/Report/LS；本文供resume_mar17非准备者一次有限裁，root随后协调唯一窄锁。

## 1. 实际必要原证与停止

[exact-v1](https://arxiv.org/html/2603.17625v1)实际读II-A–E L63–126、III/TablesI–II/关键设置与直接质量/组合/analysis L111–171；完整AB L40–44及[current abs](https://arxiv.org/abs/2603.17625) L8–29核同题五作者、单v1/ICME2026 accepted与代码入口轻量说明，无影响采用命题的revision标记。日期只复用原title/URL匹配的DataCite03/19字段与本日准入，不把Submitted03/18或后来acceptance当firstpublic。网页带回references/页尾只属传输邻接，未作核心证据；未读代码/全部图像像素、旧修订、其他论文或全venue。

支持与直接反側够即止：只拟保留frame-level独立attention输入和共同reference接口，不采用精确grouping recipe、硬平衡/连通/几何保证、数学完全正交/无损或端到端速度结论。

## 2. 真实机制及必须隔离的桥

VGGT先逐frame DINOv2得到patch，加camera/register，再交替frame/global attention；global同时消费N(P+5) tokens。S-VGGT先把逐帧patch均值形成descriptor，用pair cosine建N×N similarity图，按图提议grouping，而非只在每帧内部merge token。Soft A经过coherence/balance/sharpness目标、有限梯度迭代，再argmax硬分配并按similarity重分少量frame以适应batch；这是推理时预处理优化，不是权重fine-tuning，也不能由strict feed-forward话术称全路径无迭代/零费用。

各group前置同一个global Frame0，再独立运行原重建backbone。原模型把坐标参考绑定第一帧，此共享输入给子任务共同的参照身份；它不从输入相同推出所有不同context下的scale/pose/depth严格一致、所有seam无错、碰撞安全或任意低重叠capture有效。原论文没有给anchor独立消融表或可靠性阈值，III-E“catastrophic misalignment”文字是作者解释，不当独立已量化因果。

具体recipe/理论不采：II-B L87 density大经min(density,Kmax)得到K，与紧接“大density更少更大group”方向不齐；不造另一公式或统一可执行K选择。coherence loss比较group similarity-profile均值和global均值，不是显式组内连通证明；balance与sharpness是有限加权软惩罚，argmax后仍需纠偏，不授硬平衡或几何连续定理。A的初始化/概率保持更新、exact threshold/修正tie、duplicate Frame0处理未闭合，非准备者不需为本有限接口遍历可选代码。

II-E的O((NT)^2/K)仅理想均分attention项；固定K仍随N平方增长，pair图仍O(N²)，实际每组还消费共享anchor。由此不能称“消除quadratic”、无内存瓶颈、精确K倍全流程提速或所有parallel成本免费。三种loss与组数选择/复制anchor/packing/readout均计费。Token merge与结构分组可同时实施的有限实验不证明数学独立、gauge不变或所有质量无损。

## 3. 关键评价与反側

单A100/bfloat16，Kmax通常8随longer输入调整、soft assignment通常10iterations，VGGT权重不finetune；三数据集ScanNet/NRGBD/7Scenes，500/1000-frame受限capture。VGGT*是VRAM-efficient variant非未经优化全attention任意实现。各项FPS是作者局部协议结果，显存实测、输入resolution/完整batch与concurrency/SLO、图/优化/传输/完整output费用边界、场景分母、seed/CI在此必要范围Not Disclosed，不授生产加速/规模上限。

TableI NRGBD median Acc .022劣于VGGT* .019、NC mean .622<.642及median .717<.767；7Scenes meanAcc .022>.019、median .011>.009、NC .622<.632/.697<.716。Comp部分改善不代表“without compromising reconstruction fidelity”。TableII ATE .145<.190和ARE改善但RPE-trans .053>.038且劣于FastVGGT .030，RPE-rot .665也劣于FastVGGT .656，不采全面几何优势。

III-D Ours+Fast正文只支持NRGBD受限长度300/700frame局部合用speedup；未核Fig4/5所有像素点/独立quality表，不采“完全正交/组合无损”，III-E profile文字不补未披露fraction/完整cost。高cosine非真实overlap、reference输入不是metric真值。Sparse/wide-baseline/noisy/dynamic capture的可靠性不由dense室内表认证，部署需原view/pose与独立几何用途验收；不为有限证据缺失把原6降分/EX或假NC。

## 4. actual唯一owner与两literal PRE提案

sole `MULTIMODAL-REPRESENTATION`，[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。实际完整1048–1088几何参照/多视图表示与1090–1116 native3D→track/SGCoT→VGG-T3 scene-fitting，Ch22/24/25入口和Ch25 235–265 VGGT-World交接已读。初次search输出截断只作定位，随后完整必要局部实读，不将search当正文审阅。原原生几何/track讲state与consumer，VGG-T3把离线场景写成fastweights；尚未具体承载把长多视图attention输入拆成groups并显式共享first-frame reference。不是重写一般少token/分治原则，也不在Ch25复制世界rollout或Ch22写另一memory算法。

拟在SGCoT完整两段后、VGG-T3“若离线多视图需要……”完整段前插两literal，现Ch23约1110前；root如有并发移行以唯一完整段为锚，不改相邻family。

离线多视图重建保留全体图像共同 attention，最直接地让每个视图读取所有证据；密集 capture 增长后，也可先把逐帧特征均值间的相似图用于分组提议，再让较小的 frame groups 独立进入原几何 backbone。各组前置同一张全局首帧，使消费者明确共享哪个参考，而不是重建后默认各组坐标可直接拼接。[受限结构分组](https://arxiv.org/html/2603.17625v1)改变的是跨帧读取范围，不只是帧内 token 合并；共同参考仍是模型输入，不认证不同上下文下的尺度、pose、depth 或接缝严格一致。<!-- source-family:SF-2026-ARXIV-2603-17625 -->

这种选择以部分跨组证据和重复参考计算换取较小 attention 子任务：相似图、软分配迭代、硬分配纠偏、anchor复制、packing及全部几何读出仍付费，固定组数也未消除随输入增长的平方项。原 dense 室内对照有准确性、法向和相对位移反退，与 token merge 合用的局部提速不证明完整费用优势或无损正交。分组、参考支持、几何保持与最终用途应分别验收；视角重叠不足、参照污染或预算/质量回归时，保留全局 attention、较短输入与显式多视图对齐/专用重建，不能让共同首帧或高相似度签发几何真值、真实控制或实时保证。<!-- source-family:SF-2026-ARXIV-2603-17625 -->

静态源注：

- `SF-2026-ARXIV-2603-17625` — [S-VGGT exact-v1](https://arxiv.org/html/2603.17625v1)必要II-A–E/III/TablesI–II及直接组合/Analysis。仅frame-level attention分组与共同首帧参照接口；保density方向/软惩罚recipe隔离、anchor与几何资格、质量反退、固定K平方成本和全费用。不采硬平衡/连通/无损、完全正交、任意capture或生产实时，未核代码、图像像素或复现。

## 5. 待非准备者裁

交resume_mar17独立必要Source/actualowner/原两literal/static裁；可收窄或具体NC/中心暂缓，不改变原6或自动采强桥。只有非准备者通过并获root sole锁后才写Books，写后须另一非writer一次actualPOST；当前未safe/I/DAY。

### root授权后的实际writer落实（不代替非writer POST）

2026-10-12 root明确授resume_review17_18 sole Ch23本family窄锁后，实际重读SGCoT→VGG-T3完整邻接1097–1125和章末来源注，仅在SGCoT完整段后按原两literal写入1110/1112；静态源注1776。写后完整1097–1126及1768–1776顺读回对原PRE准确，保共同参考不认证几何、固定K平方项及反退/全费用；scoped family diff仅两段+自身注，git diff --check当前章无输出。原已通过Source/非准备者§6复用，不自授POST/I/DAY。交resume_mar17一次实际完整邻接与自身/邻注POST，root接纳后释放。

## 6. 非准备者必要Source/actualowner/PRE有限裁

2026-10-12 resume_mar17独立实际打开exact-v1，完整II-A–C 63–110（首次输出后半截断未冒读）、再精确II-D–E/III/TablesI–II 111–163、III-E/结论164–171；支持与直接反侧足即止。独立确认平均patch descriptor→N²相似图→软分组优化→argmax/纠偏→各group前置global Frame0后独立原backbone的真实消费者；共有输入不授metric尺度/pose/depth严格一致，10iter预处理不是所有计算零迭代。density→K公式/文字方向矛盾、软惩罚非硬平衡/连通、固定K仍N²与共享anchor费用必须近文保留。逐项读回TI NRGBD medianAcc/.NC及7Scenes Acc/NC反退、TII RPEtrans .053劣于原.038/Fast.030和RPErot .665劣于Fast.656；合用局部加速非无损数学正交。没有核代码/图像像素或独立复现。

实际完整Ch23 1048–1123、重点1090–1121的native3D/track/SGCoT→VGG-T3接口，以及Ch25 235–265 observed/predicted geometry交接已顺读。现正文未承载frame-group attention读取范围及共同首帧reference身份差额；两literal和静态注逐字审查符合sole MULTIMODAL-REPRESENTATION，限定分采成立。原6不变，有限Source/actualsole/原两PRE及static PASS；尚未授权写或POST，不计I/DAY。root协调Ch23窄锁后另一nonwriter验实际完整正文与本人/邻注一次即可。

## 8. 一次非writer实际POST

2026-10-12 resume_mar17作为非writer实际完整顺读Ch23 1097–1129（SGCoT→本两段→VGG-T3及下一标题）和1768–1776自身/邻注，回对原两literal与已核必要原证。实际新1110/1112、static1776逐字一致，共同首帧不授几何保证、分组费用/固定K平方项与质量反退近文准确；未改相邻SGCoT、VGG-T3、Identity或MoBa。当前章git diff --check无输出。有限actualPOST PASS，只结论记原包，不改Books过程身份；交root接纳/释放该family锁，不授本日报DAY。
