# 第四包：四个实际差额与一具体已有覆盖

仅整体PRE提案，未SAVE。writer已重读Books上下文/ROADMAP正式owner、实际完整直接两侧及相关相邻交接；reader仅必要独核/整体PRE，不第二全文。所有分数为本次采用命题，不借成熟通用原则抬分；本包五项均未核代码/复现。

## 12159 DPL / 2+1+2=5 / MULTIMODAL-REPRESENTATION Ch23

Source实际域见EVIDENCE_WRITER与reader R24有效必要，不重第一Methods。旧masked-average prototype是确定的summary；新扩散变体再归一融合后用于query匹配，把随机carrier生成与消费者相似度耦合。只有该差额深入，不采所谓spatial mean/std为真实坐标、Eq10与文字矛盾recipe或全部增强保语义/净速。单4090/30Kiter/1shot/20step，NoReverse同时改Spatial及50step反退均保留。

actual Ch23四identity/同shape不等语义与serialization段不承担“由同一个prototype采多变体并融合”的生成消费身份。拟在完整`把 shape 统一，只解决了…Tensor compatibility…`段后、完整serialization段前加一自然段；不是另建医学owner。

正文：

用于匹配的表示也可以先生成多个候选，而不始终消费一个确定prototype：从有标签support区域池化表征，在该空间中加噪、条件化去噪，再归一融合为query的相似度参考。[受限单样本分割分支](https://arxiv.org/html/2510.12159v1)改变的是原型载荷及其读出，不是新取得真实像素或解剖知识；用feature均值、方差作条件，也不使这些统计自动成为空间坐标或真实形状。训练与部署即使使用同一增强算子，support/query人口、噪声日程、融合和最终mask仍须分别验收，不能由流程相同证明分布一致。完整编码、采样/反向步骤、融合训练和独立分割回归均付费，更多采样步还可能退步；语义支持、数值日程或总预算不可靠时，保留原确定prototype、可信mask与专用监督，不由随机变体数或较高均分批准真实细节、临床可靠性和净加速。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12159 -->`

本人末注：

- `SF-2025-ARXIV-2510-12159` — Herschel，Daily2025-10-16补Oct15；[exact-v1](https://arxiv.org/html/2510.12159v1) III-A–C/IV-B/IV-D完整TIII–IV，2+1+2=5，随机prototype消费差额深入。仅support池化→噪声候选→融合匹配；保统计非坐标、Eq10方向未闭、NoReverse混改及50步反退/全费，不采语义守恒/临床或净速。未核代码/复现；PRE/真实SAVE/完整自读/sole actualPOST仅本日canonical后到真实层。

## 12195 DPO segmentation / 2+1+2=5 / MULTIMODAL-REPRESENTATION Ch23 具体NC提案

actualSource §3完整/4.4/5完整T1，reader R24必要复核。4s/hop2s acoustic next-breakpoint、8K CoVoST2 pairs按BLEU/AL而非人preference选，SeamlessM4Tv2消费。原式缺reference项，不采用标准DPO精确recipe或普遍在线无损；日/中延迟3120/3160差SHAS3050/3090，四A100/五epochs/B1及窗口与AL不同单位不抹。

actual Ch23:145–147完整ReinPatch两段及上下：右边界为动作、同序列多切分按当前backbone任务loss供相对reward，另分训练硬预算/在线因果阈值与费用。它已承载本次采用的“边界policy与下游任务消费者/等待预算分验”；12195的BLEU/AL是该目标的具体载荷，未证明新的全局可行域/因果流式保证，故拟具体NC，不写marker/注。不是仅同名segmentation，也不以缺standard DPO式自动H。

## 12387 learned SCR prior / 2+1+2=5 / MULTIMODAL-REPRESENTATION Ch23

actual v1 §3.1–3.2/3.5、§4.2–4.3/T1/T3、§6.1–6.4最小必要全部已读，reader R24既有必要支持复用。冻feature/训scene head的reprojection与learned prior联合，heldout ScanNetV2训练冻diffusion，scale20/5120points；mapping5K后才启regularizer，5K–25K映到diffusion10–0，头1K升至weight1000，score-grad归一。不是把真实mapping误差证明为预训Gaussian noise；prior制备、mapping额外3–7分钟均费，pose pGT非独立真值，小ATE差/不同prior反退保留。仅读足所采用的两种时钟/数据与prior权限，不采精确posterior或全部重定位优胜。

actual Ch23深度→光流consumer完整段已有“prior不是几何真值”，但没有将**冻结prior score当训练正则、按另一mapping时钟启用/定尺度**分开。拟在SF-2025-ARXIV-2509-05297完整段及独立marker后、原`监督中的运动标签也须先声明参考系…`完整段前加一段，唯一Ch23；Ch25真实环境状态只交接，不复制。

正文：

几何prior还可以只在训练时约束坐标读出，而不作为部署时额外观测：冻结图像特征，训练scene-specific坐标head，以已知相机的重投影误差约束数据一致性，再用预训点云diffusion的score提出正则方向。[受限坐标回归分支](https://arxiv.org/html/2510.12387v1)先等待mapping进入一定阶段，再把其迭代时钟映到去噪时钟并调节正则权重；这是一项适配选择，不证明早期坐标误差就是预训高斯噪声，也不把生成prior升级为独立几何真值。点采样、坐标尺度、两份训练人口、score模型与启用时机须共同保存，分别验重投影、真实重定位与外部重建质量。Prior预训、全部mapping与额外正则前向/求导、选参及独立场景回归均付费，不同prior/切片仍会退步；尺度、噪声支持或消费者质量不合时，保留原数据项、可信深度/相机监督和无生成prior的坐标训练，不由较平滑点云或一次较低误差批准真实场景和通用后验推断。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12387 -->`

本人末注：

- `SF-2025-ARXIV-2510-12387` — Herschel，Daily2025-10-16补Oct15；[exact-v1](https://arxiv.org/html/2510.12387v1) §3.1–3.2/3.5、4.2–4.3/T1/T3、6.1–6.4必要，2+1+2=5。只冻结生成prior作坐标head训练正则与mapping/denoising双时钟；保noise mismatch、pGT/小差与prior反退/额外mapping全费，不采精确posterior或普遍重定位优胜。未核代码/复现；PRE/真实SAVE/完整自读/sole actualPOST仅本日canonical后到真实层。

## 12370 Legibility Modulator / 2+1+2=5 / MULTIMODAL-EMBODIED-VLA Ch26

actual v1 §4完整/§5.1/5.3、VI/VII完整必要，R24独核已成域复用；此前EVIDENCE_WRITER尚缺的IPF定义已实际补读。空间Gaussian posterior proxy忽略速度，8-waypoint上层path与下层state/action diffusion分训，两个候选goal、2D及PandaGym，无真人intent识别或碰撞/硬件deadline证据；legible不是最短，最高proxy不替真实执行。仅分层接口差额深入，不复制无关IPF全公式/推人类心智。

actual Ch26:29–38完整SparseDrive词库/pathvelocity与跨本体latentgoal两完整段之间，没有**同目标动作可预测性与让观察者早辨目标**两个目标的分责。拟在SparseDrive独立marker后、cross-embodiment semantic-body-binding start前加一段，唯一Ch26，Ch25/27交接已实际读。

正文：

同一目标下，动作还可能需要让旁观者较早辨认“要去哪里”，而不只让已知目标的人预测下一步。可以先按目标及可调可辨识性条件生成粗waypoint路径，再让动作policy读取当前状态、历史和这条路径；这把路径形状偏好与本体控制分成两个消费者。[受限两阶段diffusion分支](https://arxiv.org/html/2510.12370v1)用候选目标的空间距离构造标签proxy，忽略速度与真实观察者判断，因此更高可辨识分不等人已理解意图，偏离最短路径也不自动更安全。目标集合、路径标签/坐标与执行时钟须共同保存，分别核几何proxy、真人识别和控制结果，不能由前两层之一替其余层签字。路径造数、两阶段训练、全部采样与闭环评价均付费；proxy、目标支持或动力学不合时，保原最短/已验planner、显式意图信号和独立controller，不由平滑或更“可读”的轨迹批准碰撞安全与通用人机协作。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12370 -->`

本人末注：

- `SF-2025-ARXIV-2510-12370` — Herschel，Daily2025-10-16补Oct15；[exact-v1](https://arxiv.org/html/2510.12370v1) §4/5.1/5.3/VI/VII必要，2+1+2=5，唯一路径意图消费差额深入。保Gaussian空间proxy/忽略速度、两目标/仿真、无真人与碰撞验收及两阶段全费，不采human intent真值或社会安全。未核代码/复现；PRE/真实SAVE/完整自读/sole actualPOST仅本日canonical实际后到层。

## 12326 DeePAQ / 2+1+2=5 / PLATFORM-EVALUATION-SYSTEM Ch66

actual §2全/3全/4.1–4.2必要，准入提案与直接反侧见SCREENING末。MERT95M/24kHz/4s、qv r8/alpha16/B32/weak ViSQOL＋codec内bitrate rank，460h内部music制备及多个codec/bitrate人口、九test的人评独立性须分开；same-clean train/val分开而同codec条件，不等所有distortion独立。Degraded/clean reference与69nonmatching reference不可并protocol，PEASS反退保留，test上探索LoRA配置不冒独立选择holdout；硬件/precision未披露写Not Disclosed。原loss正距离exp/codec集合式未闭不补recipe，辅助rank-label 1–3%不是独立真实质量收益保证。

actual Ch66“条件性证据”完整段/下方NASP约束人口段，及量尺、judge相对尺度等具体段已读，未承担**同codec内proxy排序、embedding rank与拟合主观量尺**三者分开。拟在完整`问题不在于分数无用…评估就会退化为不可解释的排行榜。`后、`约束指标还须保留使约束生效的人口…`前加一段；不是Ch23再开同机制，Ch65资源/Ch67监控只交接。

正文：

质量sensor还应分开“训练proxy规定的次序”“表示距离的排序能力”与“到主观分数的量尺映射”。例如按同一codec内bitrate及另一客观sensor教音频表示，再用参考音频距离预测质量，不能把跨codec同码率当同等失真；后拟合的非线性映射可以改善线性相关，却没有因此恢复新的排序信息。[受限音频对照](https://arxiv.org/html/2510.12326v1)还发现预训来源、speech/music及未见distortion会改变读数，整体高相关仍可伴source-separation切片失败。应保存原信号/参考资格、codec与失真人口、proxy/encoder、映射拟合和独立人评划分，分报rank、线性拟合与逐失真误差，不以一个相关均值批准所有听感或语义质量。编码制备、预训/适配、参考集与全部sensor/拟合、人评和新域回归均付费；reference、量尺或失真支持不足时，保留原信号、分项客观读数与独立听评/Unknown，不让弱标签和更好拟合自行认证主观真值或普遍质量保证。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12326 -->`

本人末注：

- `SF-2025-ARXIV-2510-12326` — Herschel，Daily2025-10-16补Oct15；[exact-v1](https://arxiv.org/html/2510.12326v1) §2–3完整/4.1–4.2必要，2+1+2=5，proxy-rank-mapping差额深入。仅codec内弱排序/embedding距离/主观量尺分责；保PEASS/OOD/selection人口、印式未闭与全部reference/训练/评价费，不采loss完整recipe、全音频真实质量或普遍鲁棒。未核代码/复现；PRE/真实SAVE/完整自读/sole actualPOST仅本日canonical实际后到层。
