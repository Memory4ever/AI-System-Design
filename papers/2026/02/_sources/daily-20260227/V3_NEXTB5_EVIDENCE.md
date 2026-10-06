# 后续五项必要证据／实际owner待独立裁决

五项必要原源与实际owner已root独核：21704 Ch23具体Existing通过；21669 Ch29正文248/邻接244–255/own1319、21716 Ch23正文107/邻接99–113/own1332、21736 Ch26正文1158/邻接1152–1166/own1933、21743 Ch33正文99/邻接74–105/own2910四实际整合PRE及非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。累计33论文终态＝22整合、9具体已有覆盖、2中心争议；另Nano原release事实OnlyReport。普通剩余未完成，非日级Gate。

21669、21704、21716、21736、21743的精确v1完整题摘已由root独立准入校准；本包只核准备采用的命题及直接反侧，不重复附件或旧版本。编号为本目录`V3_BLOCKS_2602.<ID>.md`的block ID，不是文件行。源均为作者实验，未复现、未核代码；下列保留写前差额与PRE建议，以上实际终态为准。

## 21669 DWA-KD: Dual-Space Weighting and Time-Warped Alignment for Cross-Tokenizer Knowledge Distillation — 2+2+2=6

[v1](https://arxiv.org/html/2602.21669v1)实际blocks21–29、41–91、95–106、113–114、119、136–138、159–162。原机制在DSKD双空间projector/attention接口上，以student entropy×projected teacher max probability分配student侧token监督，以teacher entropy分配teacher侧监督，再对embedding/hidden序列加Soft-DTW与attention-entropy band penalty。不是把两个词表的token概率同索引相减；band是对完整cost matrix加软惩罚，不证明跳过二次矩阵或省内存。

决定原文：[27] “Because the projectors start at random, an auxiliary cross-entropy is used to warm them up; then a KL term matches … to the student distribution”；[57] “tokens the student already knows (low entropy) or where the teacher is unsure (low max-probability)”只是作者启发式解释，entropy/max不是知识或正确性真值。NormalizedDTW的对称/等幅宣传不作一般metric保证，不为这项外围记法争议隔离全部有限经验。

直接Table3[114]：GPT2平均DSKD16.68/EW17.23/DTW17.30/bDTW17.25/no-gate17.50/full17.68；TinyLlama23.54/24.28/23.71/24.11/25.03/25.06；full TinyLlama Vicuna17.63低于原18.74、no-gate SelfInst18.77/NI37.98中NI高于full36.59。band不是每项改善，gate平均差很小。强化DSKD-v2平均17.78高于原DWA17.68，对应DWA-v2为17.89，不能只比弱DSKD。五次generation seed的ROUGE-L平均不是五次训练重复；GPT4.1仅Dolly100对随机次序判分。

Table136实际full-SFT小模型与LoRA大模型训练安排，rank256/α8/dropout.1、batch8、15/20epochs；不沿叙述误写全部GPT2 full-SFT。Table162同batch4 DSKD .35s/26.38GB，DWA .45s/29.92GB；CDM batch1，不并成同负载比。hardware/precision未完整披露，offline projector、alignment搜索与额外teacher/student forward都付费。

TRAIN-SFT Ch29实际244–262已有density weighted residual、多层共享projector与latent loss≠行为；278明确“跨 tokenizer 的 sequence score …不等于 token 概率逐项可比”，280–282只处理同一词表／同prefix的跨模态KL。现有正文尚无**不同分词长度先learned双空间映射、再按序列warp约束对齐与监督权重**的接口。拟在distillation段加一个窄段：词表／prefix／projector与路径匹配责任分开，attention band和entropy gate仅提议监督位置，不认证语义一一对应或teacher正确；多余cost、强化baseline与局部退步近文，回退普通sequence-level/统一蒸馏或原student。请求PRE／具体Existing裁决。

## 21704 Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models — 2+1+2=5

[v1](https://arxiv.org/html/2602.21704v1)实际24–45、46、57–58、67、70–81、103。四semantic clusters的AMBER/SEED标签与wrong-answer注入构造最后token per-head差向量，PCA方向以question embedding存库并检索；另一向量比较(raw image, detector objects)与(noised image, replaced objects)，图像与文字一起变，不独立识别“visual-only”因果。每head差norm选topK，再注入两方向。标签、retriever、noise/objects、head selection和strength共同定义干预，不是无标签truth发现。

原[9]：“vectors are stored alongside their cluster embeddings in a key-value database”；[67]直接反侧Table4 LLaVA：full CHAIR-S30.8/CHAIR-I11.4/POPE81.70；no-visual34.2/11.7/81.67；no-truth42.4/13.2/81.40；no-both51/15.2/75.08。Table3 VTI CHAIR-I11.1好于full11.4，不采所有维度最优。固定vector控制有限，α/β/K grid-search不同配置退步／大strength崩坏；数据构库与eval有同源关系，未披露可靠独立held-out调参人口。

LLaVA1.5/QwenVL7B；原hardware字段RTX4090(48GB)本身不协调，不采为标准硬件规格。64/128/256 generation tokens部分runtime对照只支持该负载；不完整计detector/noise、离线标签库和calibration，非零开销或生产SLO。

拟具体Existing MULTIMODAL-REPRESENTATION Ch23实际939–953：read-best≠steer-best、同norm随机方向／位置预算；固定centroid→conditional per-head activation-dependent drift，labels/head/potential/sampling是共同identity、factual分布非truth manifold、额外计算与normal-ability回退。检索semantic vector与双向量是这条有条件干预的有限新验证，未改变既有固定／动态选择和真实性Gate主论点。请求root实际Existing，不为论文名新开段。

## 21716 TranX-Adapter: Bridging Artifacts and Semantics within MLLMs for Robust AI-generated Image Detection — 2+1+2=5，融合方向具体gap深入

[v1](https://arxiv.org/html/2602.21716v1)实际21–30、36–53、58–60、68–71、74、78–79。artifact keys高度相似使semantic→artifact对应反向读取（原artifact→semantic）attention变平的pilot只是attention/information-flow proxy，不是内部因果证书。TOP把artifact与semantic patches经预训练fake heads／CLIP fake prompt映到两class scores，Sinkhorn用**负JS cost**优先搬运task disagreement，并残差加入semantic；反方向X使用ordinary cross-attention，adapter训练而冻结MLLM。

决定原[41]：“Since the patches with substantial discrepancies should receive greater emphasis during feature transfer, we adopt the negative JS divergence”；[49] “artifact features serve as the query, while semantic features act as key and value”。两个方向不是同一个距离对齐操作；fake scores不是校准truth，negativeJS也不是更接近语义或通用最佳transport。

Table4[71] finite ablation baseline82.3、NPR86.0、X89.3、TOP90.3、both91.9；叙述+4.6不符合82.3→86.0，采用表值。Table5[74]相同PEFT参数预算40M LoRA69.1 vsTranX73.8，160M74.4 vs75.8，full-tune76.8更高，不称普遍胜full。RR[68] Qwen4B concat .855 vsTOP .909；full origin .981到transmission/redigitization仍约.790，非鲁棒性无损。

SD1.4+ImageNet训练→所列generators及三个MLLM backbone；未完整披露epoch/GPU/precision/全部训练搜索预算。额外NPR encoder/fake head、Sinkhorn迭代与adapter要计费，参数匹配不是FLOPs／壁钟匹配；flow proxy不证明细节被因果用来正确判定。

Ch23实际99–105保留summary/patch和producer/consumer层接口，133–151共享token/codec与native/staged取舍，389条件cross-attention改变cache identity；尚未明确**task-specific cue空间高度同质时，两个融合方向可承担不同传输目标，而非对称attention／最小语义距离**。拟99–105后单窄段承接独立encoder分责：task-conditioned disagreement路由与普通查询方向分开、labels/heads/cost/marginals/iteration绑定，局部表支持不是semantic truth，强simple concat/full-tune与总成本保留；失配回退原encoder+projector／concat。也接受root判定既有责任足够而Existing，不制造AIGC领域部署结论。

## 21736 Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild — 2+2+2=6

[v1](https://arxiv.org/html/2602.21736v1)实际24–42、55–63、99–102、119–124、135–139。predictive hidden既对有motion标签的chunk作CE，又对齐boundary-frame inverse latent；无motion标签只保留alignment。LAP读chunk start/end，LSP读重复initial frame，是训练privileged future接口，不授推理能访问future／无需动作监督。

原[39]：“LAP takes the motion chunk boundary frames … while LSP uses a duplicated initial frame”；[40]：“optimize the backbone using gradients from LSP … optimizing the queries using gradients from LAP”，随后相反方向EMA共享backbone/queries，α.999。比直接coupled alignment新增**gradient职责和两路EMA传播**，不由EMA保证不collapse或物理可执行。

[119]明确LAPA†同data/backbone，JALA-act仅有动作subset，w/o-dec为JALA-act移除decoupledEMA。Table2[122] two-view平均LAPA†83.5／JALA96.9；JALA-act94.3／no-dec56.6，是有限更新接口反侧，不是独立普遍最优证据。训练LAPA†两阶段29+57=86h，JALA68h，不是精确同compute；more-wild也新增数据／成本。Layer19同时是训练align位置，19读出更强不能升普适layer规律。

7.5M混合人视频含实验室tracked motions，128motiontokens/15framechunk，8A80080GB约68h一epoch；后续FM action head/proprio/embodiment适配与少于50demos/task LIBERO微调，未核实零机器人动作监督或所有实机安全。目标、alignment、两路模型／EMA版本与额外video encoder成本绑定。

MULTIMODAL-EMBODIED-VLA Ch26实际1152–1163已有latent action区别pixel/decoder代数约束与真实控制，1420–1423有latent使用及训练预算。尚无**有标motion目标＋无标inverse latent共享pretraining、LSP/LAP gradient分责**的具体形成分支。拟1153的两帧重构前后一个窄段说明预测监督可不重构全部像素、future inverse只train、动态分责不是物理truth；LAPA†预算/无dec反侧、encoder/EMA/机器人后训费与重构或显式motion/controller回退近文。请求PRE或Existing。

## 21743 Enhancing Multi-Modal LLMs Reasoning via Difficulty-Aware Group Normalization — 2+1+2=5，advantage尺度gap深入

[v1](https://arxiv.org/html/2602.21743v1)实际32–79、85–99、150–155。patch Gram谱entropy与response sequence likelihood分别提议batch内difficulty quartile buckets；不同题目的reward合并求bucket std，但**每条advantage numerator仍减同题mean**，不是把raw rewards跨题共用baseline。两种scale与原GRPO按α混合；likelihood／谱entropy不是校准difficulty，length/encoder/source改变proxy。

决定原[54]：“compute the shared standard deviation … of group rewards”；[55] Eq12 numerator r_(s,i)−mean(r_(s,1)…r_(s,G))、denominator std(R_a)，[56] bucket std含跨题mean。只调整比较尺度，不认证新reward truth、unbiasedobjective或稳定性；empty/constant bucket、quartile ties需数值保护，原Eq12未明确δ，不能取消原safe fallback。

[96] reasoning-only average58.4，在MathVerse比full更高；[97]combined avg59.3，不采各benchmark最优。[95] perceptual-only Hallusion +3.4为作者局部结果，不能唯一归因“视觉grounding真值”。Qwen2.5VL7B/EasyR1/8H20 96GB，Geometry3K2.1k＋.3k validation、另ViRL39k，LR1e−6/globalB128/rolloutB512/G8；precision/完整steps/seed/搜索费未全披露，.1format+.9accuracy仍verifier代理。谱计算、likelihood及分组/调参费纳入总训练预算。

TRAIN-GRPO Ch33实际74–105：同prompt条件、每题mean/std+δ；已有speech/text分别mean避免reward定义混杂。尚无**baseline population与scale population分开：同题中心化、相近proxy桶跨题共享尺度**。拟“sample-relative baseline”后单窄段明确这一接口、人口/同reward spec/零variance与tie责任、proxy/成本/局部单支胜combined反侧；失准回退每题std+δ或固定scale，不从共享桶宣称跨题raw reward可比。请求PRE／具体Existing裁决。
