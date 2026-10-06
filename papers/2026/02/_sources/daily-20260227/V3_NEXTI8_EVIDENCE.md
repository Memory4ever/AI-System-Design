# I8：冻结池内八项必要原证＋具体owner（待root）

恢复已实际重读当前AGENTS、Research/Report、Sources使用+daily/arxiv、Prompt、ROADMAP与LS本任务最新56/59停点。57家族safe/51普通不变，以下未获非作者必要证据/Books裁决、不先计完成。全文题摘均已准入校准；坐标是`V3_BLOCKS_2602.<ID>.md`的blockID。没有运行代码/复现，不默认全proof或附件。

## 21340 HiPPO Zoo — 2+1+2=5，拟Ch22窄差额

[exact-v1](https://arxiv.org/html/2602.21340v1)30–45/47–76/178–204。固定线性历史编码与读出非线性可分开：OP系数的二阶Volterra readout显式表示成对lag作用，但N^k系数增长、有限basis截断并非免费可解释。Salience `s_dot=g(t)(As+bf)`、g>0给可逆timewarp；作者[64]明确这不是新selectivity本身，而是可视化历史measure，不称取代Mamba。主要窄采用：** temporal HiPPO state S 与单独OP associative bank C分责**，学习scalar write/query address，C沿当前basis向量以prediction residual定向更新，read取basis内积；reproducing kernel让相近address干扰可解释，不是无限精确tokenarchive。

[178–204]T12、24维随机token、dmodel32/nhippo32/nassoc32、fixedZOH timescale2、TBPTT一episode并detach、AdamW1e−3/MSE，展示任务学习与地址图，不含foundation-LM或matched throughput。Writegate<1与Eq[196]epsilon只接近目标值，不照[73]宣每次严格插值成功；正交basis也不保证任意地址/容量无碰撞。额外C状态、basis评估/gates、训练和二阶readout费用，need exact access时仍Attention/KV。

ActualCh22完整相关475–521：固定basis/learnedpole、内容相关gate和matrix delta定向编辑均已有；缺的是**历史压缩与地址函数bank独立，并由显式OP kernel暴露干扰几何**。拟fixedSSM到delta交接一窄段，保此区别与新增state费用；不把五动物园名称各写小节，也不采用forecasting全部定理。

## 21346 Alignment-Weighted DPO — 2+1+2=5，拟Ch34窄差额

[v1](https://arxiv.org/html/2602.21346v1)27–32/34–50/55/69–75/115–117/139–147。利用`</think>`把reasoning/finalresponse分段，judge分别评两段及fullanswer；full-score差筛pair，再用两段chosen/rejected差的归一比例加权**各段独立sigmoid DPO loss**，不是把weights塞全sequence一个sigmoid，也不是真实step信用。原[47–48]复用w同时指binarymask与continuousalignmentweights、[116]score-threshold解释与[40]差值筛pair不一致：不照录为精确可执行recipe；两段差可能异号/总差为零，原源未给可用guard，不授非负convexweight或通用安全保证。

同dataset Llama3.1-8B Table12[147]AW ASR.81%对普通DPO1.83%、utility58.27对57.66是有限方向；Table1 Mistralutility普通DPO41.45、AW54.70，CoTSFT54.95不全胜。LR5e−6 utility26.09明显退步；prefix空think Table10[139]ASR.58→.76也不是所有攻击不变。4A100、3epochs、k5/t.7、额外三类judge score费用；无需重核全部开源chat排名。Probe/deactivatehighscoreQKV仅局部行为证据，不由linear-readability宣布refusal没有理解。

ActualCh34 143–161已有tokenweights改变credit、等长分段独立非线性反馈、真实过程标签缺口；未解释**语义两段可分别异向失败，并用独立proxy调各段loss**。拟该局部目标后单窄段，只保分责/有限经验与weight人口/guard必要性，普通sequence DPO或人工/可执行段标签回退；不采用不明权重精确式。

## 21371 Interleaved Head Attention — 2+2+2=6，拟Ch15窄差额

[v1](https://arxiv.org/html/2602.21371v1)29–39/77–95/365–376。每head的Q/K/V在head轴分别learnedmix为P个pseudochannels，按token交错成NP虚拟位置，再做标准causalattention，pseudochannel有各自RoPEphase。它改变**softmax之前谁能与谁匹配**，不是原head输出concat后的W_O，也不是GQA少KVheads。参数mix O(H²P)小不等attention便宜：global O(P²N²d)，窗口/periodicglobal重新取预算，FlashAttention兼容不授无额外KV/延迟。数学superset/strictness[35–39]是无position的algebraic模型，不搬到有RoPE虚拟索引的实现作无损旧checkpoint转换。

2.4B/H20/dh128/26layers、240Btokens、128H200/BF16固定训练；局部window W=N/(2P²)和global交替[84/371–376]，constant级FLOP论证不等实测全训练cost，标题图N/(2P)与方法N/(2P²)不混用。Table2HumanEval17.1<17.2、Table1MBPP TalkingHeads15.9/43.1>IHA15.5/41.6；RULER44平均有限，64K适配有费，不证明所有reasoning已学poly算法。保projection/mix/扩序列/新position/checkpoint成本和MHA/GQA回退。

ActualCh15 59–93一对一head独立softmax→concatW_O、119–175分化及GQA状态tradeoff、214–245并行与压缩state接口；没有crossheadQK-pseudo-token matching。拟concat/W_O处单段区分表达与成本，不复制全部理想poly/CPM证明或误称增加H即可得到P²独立能力。

## 21424 Behavioural Representation and Preservation — 2+1+2=5，拟Existing Ch5

[v1](https://arxiv.org/html/2602.21424v1)24–42/91–105/142–160。先固定evaluation observation，对不同probe-induced history比较conditionalactiondistribution L1，测的是所选probe的behavioral dependency，不证明epistemic truth/意识。Gridworld300episodes，shortcut dominantprior .863而reversed .060，probe .810两侧；A2C10seeds continuedskew使responseprofile及hiddenseparation降，H32/64/128不完全修复。Appendix[149]**Stage1 goalreward+5、Stage2+1**同时改变rewardscale，不能把继续优化全变化只归prior；d下降与projectedgradient局部诊断不推广所有LLM/所有convexensemble。理论probe诱导state人口可能随policy变，不采用无条件mix收缩定理。

ActualCh5 100–122distribution/feedback偏差、251–301decodability与真实behavior/intervention、377–413切片/perturb/跨分布/内部与真实任务分账已经承载**平均训练reward保留≠少数history条件行为保留**。固定probe是此验收的有限实现，不改变现有设计选择，具体E，无新“epistemic”小节；保rewardscale混杂与有限control在报告。

## 21442 MINAR — 2+1+2=5，拟Ch5窄差额

[v1](https://arxiv.org/html/2602.21442v1)29–52/69–92/99–109/182–187。GNNclean/corrupt保持同V/E只改features，node对齐后mean EAP/EAP-IG分数；算法从rankededges逐个加入经过该edge的完整input→outputpath，修正只topK可能断路的**connected subnetwork**接口，而非证明唯一最小因果算法。O(K(Vc+Ec))构建、两forward+backward或m20积分是额外成本，分数均值可消掉符号/节点差异。

Bellman-Ford10params circuit保testloss.0545，removedloss21870；双task11edge保BFS.9831/full1.0但移除.8198恰匹配majorityreachable，不能叫randomchance。实际式[91]BFS由distance affine读出，跨balancedtreeOOD高分仍非独立BFS算法；epoch1000generalization与3000minimalcircuit分离，不授继续训练总能安全压缩。SALSA非所有任务generalize，WeightGrad有时优EAP；Eq17/18fidelity符号/名称存在反向问题，**不采用其Char headline**，不丢Bellman独立actualprune/retain与reuse证据。多initializationfunctionsame/neuron不同；graphfeature corruption不覆盖纯structure任务唯一counterfactual。RTXA6000原披露、SALSA7A10080GB、训练/配对/积分费用。

ActualCh5 251–281既有correlation→probe→intervention，377–405已有sufficiency/necessity与basis-invariantcores，但缺**候选局部edge需连成可实际执行输入输出子网，并分别retain/remove验证；高OOD行为仍可能共享shortcut**。拟evidence阶梯一窄段，不写GNN应用/算法目录，不把Char错误隔离全经验。

## 21508 WaterVIB — 2+1+2=5，拟Ch72窄差额

[v1](https://arxiv.org/html/2602.21508v1)26–69/72–90/109–114/223–238。Imagewatermarkdecode路径加入learnedGaussian bottleneck，train reparameterizednoise+BCE+KLprior，inference改μ；不是改变消息签名/归属权限。Regularization tradeoff可提高部分unseen-edit bitrecovery，但**representationminimalsufficiency不等生成编辑鲁棒证书**：IB目标没有显式限定未来attack，输入X/cover与watermarkedfeatures概念须分开，α缩放noise也不能把未缩放σ的KL当实际信息量。只采用有限bottleneck接口，不采用MSS必要/充分、β↔εbijective或allpurification为projection定理。

Table3localControlNet .13‰→.14‰退步、globalSDv1.5BER48.55%→38.34%仍高；Table5cropout29.61%→32.82%、Poisson.01‰→.02‰；rescale巨大收益非strictinvariance证明。β超过2e−4过压缩反退，two architectures30/100bit、COCO14/17、不同resolution/α、4090/B32or64/Adam；附CNN/MLP、训练与攻击/decoder/质量门禁成本，固定μdetector不能认证ownership/unforgeability。Body与表单位不一致采用表明确单位，不合并‰/%。

ActualCh72 187generator/decoderlifecycle与1092–1107已有DPI≠decoder工作点、编辑质量/移除痕迹/provenance分账；缺**decoder representation bottleneck可使部分编辑恢复变好但会丢payload且必须按attack/质量校准**。拟DPI附近单窄段，不代替签名/origin/隔离；原decoder、较弱压缩或独立metadata回退，不为理论外围错误放弃有限经验。

## 21543 Multi-Way Parallel Text Alignment — 2+1+2=5，拟Ch76窄差额

[v1](https://arxiv.org/html/2602.21543v1)15–30/42/49–68/83–89。每语均可anchor，同一源句四语共享positivegroup，pretrainedembedding L2anchor抑制漂移。NLLB3.3B生成六语、约76KEnglishroots；translation equivalence是训练proxy，不是真实语义/authority。LossEq1 denominator仅negative，不是标准含positive的normalizedlikelihood，实际还有boost低cospositive；不照原式宣精确SupCon概率。

同paircount比较N/6四语rows与N bilingualrow：bothall-languageanchors但semanticinstances/训练步数不等；Table1French94.8>80.7、German65.7<83.4，不能allmultiwaybest。English-onlyanchor明显低、English可省但仍有退步；addingEuro/Asian分别不必改善Hindi bitext，未训African amhclustering50→24.2。Earlystop/patience10/20epochs/B32，mE5 B128/5epochs各调temperature/regularization，A10080GB；NMT/校准/encoder更新与索引reencode都付费，generation未验且translationqualitysensitivity未评。

ActualCh76 241–270已有matchingobjective/encoderrevision/域转移与index重建，未明确**同translationgroup的all-language anchors与Englishpivot分开，pair预算相同不等语义样本/步数相同**。拟dense表示训练处单窄段保slice负侧、translationprior与旧bilingual/encoder回退，不路由Ch12tokenlookup或添语言bench名单。

## 21565 Training-free GFlowNet Composition — 2+2+2=6，拟Ch20窄差额

[v1](https://arxiv.org/html/2602.21565v1)41–63/68–92/129–172/212–214。同sharedDAG、非负reward/weights、trueZi与component终止分布Ri/Zi条件下，**state-conditionedweight vi·ui(s)/uM(s)**mix forwardpolicy；reachingprobability递推使终止分布恰为weightedrewardmixture。不同于每步fixedweight或无ui的ensemble。Linearexact仅β1且ui/Zi正确；[172]各自estimatedZi误差一律globalrescaling的说法不成立，隔离：两component相对Zi误差会改变weight，不宣learnedstateflow自动给exact结果。

Nonlinearcomposition δ(x)=uM(x)/NM(x)一般不常数，highreward区域近似观察不能签全support；localzero-denominator/unreachablestate也不自造实现guard。32×32三动作toy、2–5objectives/128preferences，Table1L1.003vsnaive.117有限；nonlinearTable2有classifier更优.142vsours.180，notalwaysbest/strictlogiccorrect。SubTB20kiterations/B128与basebank/replay有预训练费，“training-free”只新composition；每步多model forwards、flow estimates、residentbank、错误分区与轨迹开销。仅generic理论/toy/control，不采用分子科学领域结论；realworldtiming只支持作者未parallelized多模型有额外开销，不变生产SLO。

ActualCh20 328–347已finitecandidate或SMC校正完整pathlaw与localnormalization不同，未承载**pretrained forwardpolicy由state reachingmass组成终止reward目标、linear与nonlinear权限不同**。拟samplingdistribution校正交接单段、保true/estimatedflow与费用、普通单policy/直接终止mixture或重新训练回退；不遍历Appendix其他科学实验。
