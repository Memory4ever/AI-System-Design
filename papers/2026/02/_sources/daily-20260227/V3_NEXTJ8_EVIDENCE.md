# J8：冻结池内必要core／actual owner（待root）

本日仍57safe/51普通；这些拟处置不计完成。全部已完整精确v1题摘准入校准。本轮恢复实际重读AGENTS、Research/Report合同、Sources usage+每日/arxiv、Prompt、ROADMAP与LS最新56/59路由。不扩大原始池，不做全proof、修订diff或无关artifact。HTML坐标为`V3_BLOCKS_2602.<ID>.md`的blockID；21600 HTML404后恢复同版PDF，机械提取带PAGE坐标，未安装新依赖。未复现。

## 21591 CADC — 2+1+2=5，拟Ch23窄差额

[v1](https://arxiv.org/html/2602.21591v1)21–71/74–89/118–122。UGAQ从hyperprior重建zbar与y残差估uncertainty，令spatial m≥1并量化**y/m**；[48–51]明确decoder不inverse-scale，降低signal strength/SNR由generative prior补细节，不是可逆量化step或精确恢复原高频。Auxdecoder只读前4channels，BLIP从**已经解码的auximage**生成caption，text再guidance one-step distilled SD2.1。Caption无额外wirebits，但加入BLIP prior、求值和文本conditioning；不是新环境信息，也不保证细节真实。

原[80]累计消融M0→UGAQ BDLPIPS−3.7/DISTS−2.7→aux−5.3/−3.5→caption−6.8/−5.5，非完整factorial。[85]channel energy/variance只代理信息，非mutual-information测量。DF2K/CLIC训练，hyperprior+four-step ARentropy、MSE/LPIPS/CLIP/GAN/aux多目标，lambda改变rate。Kodak24/768×512、DIV2K100/2K、CLIC428/2K分别评；Kodak因样本少不算FID/KID。RTX3090Kodak encode .034s优Stable .156/DLF .181，**decode .355s慢于.322/.195**，不把encode宣传当端到端。[121]认为BLIP导致费用只是解释，架构也不同。完整entropy/aux/BLIP/prior成本，无真实通信链路SLO；卫星仅应用例不采用。

ActualCh23 277–294已有rate/distortion/prior容量/decoder成本联合、consumer-quality控制与可逆shape/gain；37–55已有derivedmodality不能新增observation。缺**不反缩放的空间signal-strength codec与从其decoded支集派生caption共同消费固定prior**，不是加模态新事实。拟rate段后一个窄段，保恢复的是感知候选、不是不可逆细节真值，decode反退及普通可逆量化/原codec回退。若root认为该分责已充分覆盖可E，不靠论文名字制造gap。

## 21593 Consistent Semantic Injection — 2+1+2=5，拟中心量化争议／不写Books

[v1](https://arxiv.org/html/2602.21593v1)13–35/40–57。BLIP caption拆anchor/attribute，DDIM inversion复制CSWnoise，GPT4omini候选prompt先过text anchor再过regen-imagecaption anchor与watermark/noise checks。Eq1是概念优化，不是实测oracle或全对手搜索；copy noise不等所有prompt变化都免计算。SDv2/publicprompt，运行sample人口、硬件precision、完整LLM搜索费用及thresholdselection未披露，不补造。

关键原文[44]ASR定义：“proportion of tampered images still detected as watermark present under the threshold”。**目标是内容编辑后水印仍阳性，不是移除watermark至阴性。**Table1[25]/[45]SEAL 81% vsRPM7/LFA0；然而[48]称用一致可验证基准逐scheme看检测，**[50]SEAL最低patchmatch72也超过threshold12**，按这段所有样本应阳性100%。原源没有交代这两人口/阈值/分母怎样不同；不能自行补为不同protocol。且FID178.75vs未改164.27只set-level质量，不独立验收每图target attribute确已编辑且anchors未变；BLIP/GPT过滤共享偏差。WIND/WINE记名差非中心，不扩大纠错。

拟**中心定量ASR Disputed**，保方法与有限表格为报告事实但不授81/100通用攻击成功，不能Only抹掉原center-rate冲突。必要重开：同图ID的编辑成功标签、SEAL检测统计及决策阈值、Table1与Figure2实际人口/有效分母。Ch72实际1092–1112已watermark信号≠完整provenance/实际decoder工作点、质量分账；无Books正面采用。若root认定中心应收窄为方法/有限阳性而非量化率，请明确窄E的采用边界，不推定编辑真实性。

## 21596 Hidden Semantic Bottleneck — 2+1+2=5，拟Ch24有限条件接口差额

[v1](https://arxiv.org/html/2602.21596v1)24–56/59–74/188–199。六XL DiT族ImageNet1K，c=y+t进入AdaLN；高cosine和abs-magnitude PR本身不测semantic truth/collapse。决定反侧Table4[188]**REPA c cosine .9946/nPR1.43%，单独y cosine .5194/nPR41.60%**；UViT concat y+.t cosine .97917但单独y .00165。说明共同t与接口位置可掩盖条件差异，不能把sum统计称为class embedding都几乎相同或语义只15维。Continuous/task差别Table5仍有高y相似，只局部接口，不造普遍同一原因。

ActualpruningTable2[46]REPA baselineFID7.1694；每步剪38.94%tail FID7.2143、IS176.02→171.99；剪66.21% FID9.2202/IS125.15，**不采用66%大体无损headline**。仅初step剪38.94% FID7.1690、precision .8032→.7878；late-step precision/recall改善依population。[193]DeepFashion40%prune FID18.6372→18.6692等有小退。模型/官方checkpoint、timestep与mask位置绑定；figure42 sparse算子未有可读端到端runtime人口/硬件数字，不授66%维数等于节省主干算量。理论放大/噪声压制在[56/71]是hypothesis，不采allmodulation原理。

ActualCh24 238–241已有sequenceattention vs pooledmodulation、positive/negative方向与layer、训练费用/条件路径inactive；缺**先分解semantic条件y与共同t，再将combined几何、实际coordinate删除与生成质量分开检验**。拟附近一窄段，保tiny-signal可被消费者使用、PR不是信息维数、mask/timestep校准费用，原完整条件/低剪枝回退；不把余弦近1批成collapse或dense计算可省。

## 21600 AQR-HNSW — 2+2+2=6，拟具体Existing Ch76

[exact-v1 PDF](https://arxiv.org/pdf/2602.21600v1)pp3–6（`V3_PDF_2602.21600.txt`）。pp3Alg1/§3.1用kNN density/global variation调整**每dimension percentile bounds，所有向量仍uniform8bit**；不照introduction“不同region多bit”宣传。大集最多5000sample、其他point赋sample均值；Alg1每dimension权重同一个平均density，因而未支持不同dimension的独立density画像。只记录原限定pipeline，外围符号排版不全proof。

pp3–4§3.2粗uint8图导航→decode approximatevector和FPquery的asymmetric rerank→选定项读存储的**原FP32vector**exactrerank。Gap/ratio早停heuristic只见粗候选，不提供漏候选误差界或recall证书。OriginalFP32按Alg1line21仍保存，4×codecompression不等75%总resident/indexgraph memory。pp4§4 scalar M4Pro24GB；Table1仅60K/100K/1M datasets，不能照conclusion称billion-scale实测。pp6 SIMD两架构M4NEON/Xeon6444Y AVX512 iso95recall与scalar分账；调coarse/ef/rerank/gap原参数费用，buildspeed2.83～5.36，不全原source5×。

ActualCh76 219–225已coarse graphnavigation→低成本精化→裁候选→读取原完整向量，earlystop不是exactNN；same-recall QPS/P99、storage/calibration/indexrevision/构建分账及更高recall前级重新主导。本源uniform8bit/percentile和gap只是此分责的有限实现，不确立新regionadaptivebit机制，**E不因证据费时改EX**。无需新段，报告保原density/scale边界与totalmemory不明。

## 21611 Structurally Aligned Subtask Memory — 2+2+2=6，拟Ch77窄差额

[v1](https://arxiv.org/html/2602.21611v1)21–53/57–79/85/87–89。Agent预测Analyze/Reproduce/Edit/Verify phase及objective+keywords intent，**在当前subtask开始按category先硬过滤再同category语义Top1**；结束同backbone judge/extractor把局部trajectory成guidance后立即写bank，不等整issue结束。四category不是原始真实性，samebackbone不能称独立核验，硬filter可能错失跨stage解法；raw provenance仍须另保。

Mini SWE Agent/SWEVerified500、temp0，stepcap包括extractor而非只reasoning；emptybank streaming三shuffle-runs，AvgPass1和Best@3不是singlepatch三attempt通过率。Table1Claude3.7全instance memory52.2→51.1/subtask56.1；Table2structureonly53.2/full56.1、Table3globalretrieval53.8/full56.1、Table4raw53.4/full56.1有有限pairedcomparison，**不是allabstraction严格必要/均独立因果**；same stepcap不等全部token/APIcost。前200bucket净−1，后期改善也可能顺序/pop难度，不采无限memory规模定律；无taskleak控制细节或生产SLO。额外阶段预测/judge/embedding/存储/Top1cold-start与错误继承费用。

ActualCh77 780–799已有atomictransition与多view、拆碎crossdependency/hindsightbias、rawepisode回退；389–406已有粒度分层/抽取不授facts。缺**functional phase拥有检索支持集，phase-local intent先categoryfilter，局部episode终止即时写回**，不同于固定atomictransition或globalissue相似。拟derivedexperience附近一窄段，保phase错误/跨stage受限/费用与原global/完整raw fallback；不加四workflow小节或新Agent状态术语总章。

## 21619 When More Is Less — 2+1+2=5，拟具体Existing Ch23

[v1](https://arxiv.org/html/2602.21619v1)13–49。固定Qwen2VL7B/LLaVANext1.6-7B/BLIP3-5B，VSR66relations与EmbSpatial；GroundingDINO/SAM2/DepthAnything/OrientAnything构造spatialcues，ATOMIC retrieval threshold、CoT分别变input。Input intervention有限，可支持input差异作用，不由更少context直接诊断认知overload为唯一原因。

[37]数值orientation/depth部分−9.2%而verbalized改善，[41]先按single-cue effectiveness排序累加，多cuespeak后下降，选择排序人口非随机equalbudget；[43]threshold低同时改变amount+relevance，不能单归token量。CoT[32]EmbSpatialgainvsVSR−2.0%；[46]frame ambiguity例为qualitative，不证明“grounding充分”必要/充分定律。Figures没明确CI/repetition/hardware/precision，原offtheshelf构造不是真geometryoracle、moretruth输入也可能带errors，fees/count separate。

ActualCh23 574–594 contribution vs sample reliability+gatehint，597–610 captionproposal/原视觉独立、sceneIR四验收，37–55表示形式≠信息量都已承载**更精确数值/更多派生cue未必更可消费，独立输入真实性与任务收益分开**。E，不写新“cognitive overload”理论段或全CoT坏；具体负侧保报告。

## 21622 ADM-DP — 2+1+2=5，拟具体Existing Ch23/Ch26（唯一主owner Ch26）

[v1](https://arxiv.org/html/2602.21622v1)20–24/30–48/62–70/73–98。各arm独立policy但training与eval均共享allTCP；不是无通信分布式独立或任意新增arm已零重训验证。当前vision/RGB+PC、FSR tactile、TCPGAT经MLPgatedsoftmax融合；α是任务proposal不是当前reliability/conflict safety，inverse-distance不是完整geometrycollisioncertificate。训练70%fullcontact/30%partialcontact纠正（release-regrasp或tighten），有新实测接触输入但不能由NoTact将收益全部归30%数据。

20DDIMsteps/history3/predict8执行6再规划，七双/三arm仿真50/150 demonstrations每agent，TableI/full150avg57.1 vsFlow45.4，TableII一module一删平均57.4与主表57.1口径不合不合并；PassShoe graph−9pp/visiondominantPC负侧有限。[98]明确**real robot deployment是futurework**，Frankas/FSR规格不代表已真机SLO、安全或新arm泛化；未给episode数/CI/seed/hardware/precision。Entropy正号H被最小化鼓励集中；维度512/64直接sumprojection未述，不补完整实现。额外encoders/sensor/共享TCP/20steps成本；contactmonitor/verifiedskills/directcontroller仍执行fallback。

ActualCh23 574–594已taskcontribution gate不等reliability/真值；Ch26 381–395已当前触觉、预测触觉producer与真实反馈分权，855–876明确collision/force/contactmonitor与独立physicalcommit。源只对这些已有责任提供有限仿真实现/删除modality对照；30%refinement数据未独立隔离，**E**，不为architecture组合造新section或物理安全结论。

## 21626 Gimbal — 2+2+2=6，拟Ch21窄placement差额

[v1](https://arxiv.org/html/2602.21626v1)39–50/54–58/94–103/108–118/126–154。DP KVpressure/tokenload/useraffinity与prefillSJF+5saging为成熟局部request机制；新增选择只取**跨layer expert transition affinity与当前activationload的冲突**。MILP公式展示size/rowbalance/cuttradeoff，actualAlg3不用MILP求解：固定manualanchorGPU，全部threshold/topE affinitylinkedexperts放anchor，其余按新load greedy，每3000steps刷新。容量靠更严格threshold/更少topE截pool，不授所有关联都可同时驻留、全局最优或迁移免费。Random200requests统计跨layer不等真实traffic unbiased；profile/threshold/迁移与expertrevision/epoch成本保留。

vLLMimplemented.9.1而baseline.9.2身份不同，两A10080/NVLink/dualXeon6326/pplxkernels/Qwen3-30B-A3B默认chunkedprefill；precision ND。BurstGPT五modified distributions/各1000requests、1～1.4RPS，**主性能prefixcache禁用**；三个module单开ablation，EDR有限增益，不拆fulljoint当相同版本factorial。三seeds meanTTFT−17.76/TPOT−13.34且throughput近原，未授所有tailSLO或质量无损。ShareGPT10K×5的useraffinity仅hitcount+3%/hitrate+4.4%，不是答案质量/全流程latency，不能与Burst性能拼收益点。Metrics/load异步可stale，route useridentity不授权content。

ActualCh21 777–806已有router vs demand/topology/capacity placementepoch、迁移一致性/固定fallback；未明确**按cross-layer迁移关系先固定少量anchor再按各layer热度刷新其他placement**如何用通信换局部imbalance、裁affinitypool才满足容量。拟该交接一个窄段，只有限heuristic且owner仍runtimecontroller，保fixedlayout/普通EPLB回退/费用，不加成熟SJF/routing段；若现有实际同层/邻层分责足够可E。
