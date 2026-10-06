# 2026-01-28 逐项证据与采用边界（64项必要复核及日级验收通过）

## 冻结后最后有限尾部（9项；作者必要证据及root逐项独立均完成）

### [TensorLens](https://arxiv.org/html/2601.17958v1)

2+1+2=5，标准，仅报告。`html-17958.json` §3.2–3.5 L125–202冻结本输入attention、LNvariance与ϕ(z)/z，再组合token×channel四阶operator；这是data-dependent线性分解，不是重算新输入后的Jacobian或因果机制认证，z0/affinebias另需定义。§3.6 L203–211界包含实际F(X+ε)−F(X)，不授可计算统一邻域误差保证。§4 L216–240 DeiT/ImageNet、BERT/RoBERTaIMDB、decoderWikiText128；perturbation masked0–30%本身改分布，decoder效果lessconclusive；Pythia1B关系m3/6splits比较预测复现而非世界事实，occupation-age接近random。Limitations L243–244 GPUmem intensive/up-to1B/moderateseq，硬件精度/全构造成本 Not Disclosed。采用跨FFN/LN/channel分解的有限解释接口，不借图示授causal/完整circuits；Books仅报告。

### [Random Context / LLM Diversity](https://arxiv.org/html/2601.18053v1)

2+1+2=5，标准，仅报告。`html-18053.json` §2 L64–79统计重复list的unique/entropy；§3 L153–170 LLM生成并人工过滤100prompts、每个100responses×10items，4models structuredJSON/temp.9，ordered与unordered、randomword/sentence同协议；§4 L187–207增加1/2/5/10words饱和、相对效果小且未正式验质量，AppA.1 L304–305相近长度随机字符串也显著，不能将semantic concept或创造性机制唯一因果化。pairedt-test在100prompt的α.05不是所有输出正确/新颖证明，也没有temperature sweep证明正交。硬件精度/token长度成本/多seedCI Not Disclosed。采用list-mode分布对无关context敏感且词语语义并非必要的局部采样条件，非creative/intelligence突破，Books仅报告。

### [Concreteness and Visual Grounding](https://arxiv.org/html/2601.18065v1)

2+1+2=5，标准，仅报告。`html-18065.json` §3 L119–177 Llama3.1 8/70与Vision3.2 11/90同backbonefamily而非matched额外data/训练预算，inference全text；40K词concreteness，unknownpropernoun强赋5/functionword0、6bin0.6，datasetpopulation pooled不能当唯一visual因果。2DtSNE内cosine不认证原空间几何；rating分布KL需零概率处理未明确。§4 L178–192/L252–267 QA差随concreteness相关，attentionentropy与ratings是观测、不可当groundedcircuits；Limitations L272–278单family/不可得frequency/只有endpoint，非developmental/跨family定律。硬件精度/重复CI/训练配比 Not Disclosed；保留concreteness分层评价接口及混杂，不能据此决定必须visualtraining，Books仅报告。

### [Spatial-Conditioned Reasoning / Sanpo-D](https://arxiv.org/html/2601.18100v1)

2+1+2=5，标准，仅报告。`html-18100.json` §1 L54–77 metricdepth与RGB输入fusion，§2 L197–209 647人工QApairs：intersection153/pedestrian268/obstacle73/path153，指定frameinterval；prompt robot→human不代表物理导航执行。§3.2 L217–223同模型无parameter/architecture变化仅改变输入depth，InternVL2-2B/LLaVAOV7B反退且不按规模单调，支持输入表示需按consumer重验。§3.1 L211–215 differentmodelfamily排名不授small模型普遍更泛化/大模型objectmemorization，Avg描述mean与weighted不一致不采用。depthfusion颜色/强度具体校准、frames/硬件精度/重复CI/真实collision/latency Not Disclosed。有限表示条件保留报告，不将presence QA当导航安全/持久几何或重建能力证明。

### [NaVIDA](https://arxiv.org/html/2601.18188v1)

2+1+2=5，标准，仅报告。`html-18188.json` §3.2 L158–164概率p.7同atomic最多3合并→n3subchunks，2.4MIDS与2.8MVLN额外pairs；§3.4 L406–416只actiontype不numeric的entropy，假定horizon单调上升、下降前截断/否则丢末块，这不是calibrated真实risk或可靠性定理。§4 L515–524 Qwen2.5VL3B frozenvision/projectorLLM1epoch/hist8，R2R/RxRvalunseen；§4.3 L587–648去ScaleVLN子数据默认不用entropy，对sameIDSamountforward替代与chunk1/2/3/entropy SR55.5/56.2/55.5/57.4有限差额，不能推所有horizon单调。Realworld两humanoid远端4090、0.93s不包含全部network/control，App7.4 L752–761定性demo且无任务分母/碰撞保障；训练GPU/精度/重复CI Not Disclosed。采用typeentropy方向变更的有限执行截断接口，非全uncertainty-safecontroller，Books仅报告。

### [LLM-ForcedAligner](https://arxiv.org/html/2601.18220v1)

2+1+2=5，标准，仅报告。`html-18220.json` §3 L91–127 AuT12.5Hz/Qwen.6B输入all音频+causal transcript[time]slot，nonshift CE仅slot、dynamic50%sample/50%word插slot，一forward输出timestampindices，不是自回归生成；80ms离散不变成millisecond精度。原L104的3750=(500s/80ms)算术冲突，§5.2 L343为300s/80ms才一致，不采用500s。§4 L129–137 56000h10语言多数MFApseudo、human测试仅internalChinese，Mixed-Crosslingual仍包含MFAlabel；§5.2 L341–346 finer40ms更拟合MFA却不改善human、LimitL402–406 noisyboundaries/unevenlang。原增量为同slot接口的resolution/generalization反侧，不借大SLLM名称。硬件精度/batch/重复CI/human样本人数 Not Disclosed，RTF不授生产并发/全语言human真实精度，Books仅报告。

### [Temp-R1](https://arxiv.org/html/2601.18296v1)

2+1+2=5，标准，仅报告。`html-18296.json` §4 L154–201 plan/filter/rank/search tags、GPT4o约1000SFT、GRPObinaryanswerreward；§4.5 L373–380 hardmulti先到T0再mixsingle，以防single-search shortcut，T0/各难度预算匹配未明。§5 L415–430 MultiTQ/Timeline训练、ICEWS OOD/相同E5retriever、只9%RL；§5.3–5.5 L440–463去curriculum overall.780→.556/hard.550→.143与行动数差，支持有限训练顺序条件，但不能将RAG/SFT/GRPO成熟组合或所有下降唯一归因shortcut；无curriculum对照是否equaldifficulty/callbudget未充分披露。AppC L840–845 bf16 SFT2epochb16、3A800 RLgroup5temp1/clip.2/KL.01，maxsearch停止已定义但不能真值认证。只采用temporal工具学习的局部顺序反侧，不授普遍SFTprerequisite/agent必优fixedworkflow，Books仅报告。

### [TC-IDM](https://arxiv.org/html/2601.18323v1)

2+2+2=6；physical执行边界受影响深入，仅报告。`html-18323.json` §3 L120–169 generatedRGB→VGGT相对depth/camera→首帧sensor metric scale/shift与knownpose变换，frozenDINOv3/MLPgripperstate和SAM3/3Dtracks选10rigidpoint→SE3leastSquares TCP动作两分工；首帧end-effector必须可见，单次尺度锚不保证未来生成depth/track物理一致，也没有collisionclearance认证。§4 L339–385 groundtruth replay与generatedvideo闭环分开；作者说Easyperfect同时给93.3%冲突，Hard28.9%非universalprecision。§5.1 L388–394 samereferencevideo控制planner但dart4cm/throw措辞不授安全；camera/deformable/6stephoodie/UR迁移只有qualitative无需再泛读视频。AppA/B L724–740 Franka/2F85/FCI1kHz，30210traj/25train/9heldout；GPU/precision/speed/seedCI/recalibration/基线等预算 Not Disclosed。实际Ch26 L54–69已承载relativegeometry需metric锚+robotframe与consumer失配，L172模型外coordinate/control责任；本稿analytictoolrigidity为局部实施分支，不因TC-IDM名称缺位强造长期gap。保留report，不授arbitrarytools/embodiment invariant/zero-shot安全。

### [DynTS](https://arxiv.org/html/2601.18383v1)

2+1+2=5，标准，仅报告。`html-18383.json` §4 L193–229 inference未知answerattention→离线correctMATH完整traces标签/只训练MLP→在线hiddenstate importance，再保全question∞score/localwindow/selectiontopk；label是后验attention而非truth/因果必要。§5 L230–249 break-even只FLOPs减MLP，不包含排序/gather/训练/通信费用；未授无开销。§6 L518–545 R1distill7/8B、16384steps/temp.6/topP.95/topK20、5responses平均Pass1、taskbudget3k/5k，公平KVcap不等每方法总训练预算。§6.3 L670–705 predictorfit/overlap不认证错误trace，localwindow/retention过大或小反退；C L1033–1053 8H800/15epoch/7142与7064correcttraces，compression实际transformers，E L1089–1094 vLLM/SGLang尚未部署，不由离线vLLM生成声称serving支持。precision/CI/concurrency/SLO Not Disclosed；采用unknownanswer importance的离线→在线proxy替代与必要成本边界，Books仅报告。

## 冻结后多模态/扩散/调度批（6项）

### [ViTCoP](https://arxiv.org/html/2601.17818v1)

2+1+2=5，标准，仅报告。`html-17818.json` §2/3 L89–137、L540按视觉CLS attention预筛→feature/spatial density聚类→cluster按大小分quota挑小K-L2 elite、其余mean merge→deep再小K筛视觉tokens，不是删text tokens。Knorm与attention负相关是局部观测，不是任何query/model的重要性定理；ViT阶段仍用attention，不能全流程无attention map。§4 implementation L637–639 shallow2/deep22、V100/lmms-eval，AppendixC L1308–1311 COCO gridsearch；主文encoder output与AppendixC penultimate为不同层级配置描述，保留这一区别，不补造唯一插入位置；§4.4 L766–809未独立消融StageII且去StageIII在COCO改善，不能授所有stage必要/唯一因果。Table5 L768–806 NeXT13B POPE87.5%quality retention、prefill139ms虽快于native914却慢于VisionZip126，decode53.53也慢于53.39，不能仅94%TFLOPs称最佳端到端加速。precision/batch/concurrency/重复CI/SLO Not Disclosed；有限代理与depth选择条件只报告，不授Flash兼容实现已验/无损。

### [VAE-REPA](https://arxiv.org/html/2601.17830v1)

2+1+2=5，标准，仅报告。`html-17830.json` §3.2 L102–118复用pre-extracted SD-VAE features作SiT hidden→MLP的smoothL1目标，β.05、λ1；新接口在无需externalteacher而非借REPA成熟原则。§4.1 L312–314 ImageNet256、batch256/AdamW1e-4/SDE250/50Kgenerated样本；§4.2 L315–322深层alignment反退、不同架构layer2/8/8，不授越deep越好/不需选择。T2I L597–598 COCO MMDiT150Kiter CFG2只是有限迁移；Table5 L599–625 H100 batch256每iter7.2vsnative8.1、额外18Mhead/4%GFLOPs/6%forwardlatency，不是无开销，7×iteration-to-FID不等7×walltime，更不授生产训练全生命周期。精度/重复runCI/峰值内存 Not Disclosed。采用已有codec可作为低成本表示目标的局部替代，不认证VAE语义真值或通用teacher替换，Books仅报告。

### [Balance Future / BF-IO](https://arxiv.org/html/2601.17855v1)

2+2+2=6，标准，仅报告。`html-17855.json` §3/4 L162–241 sticky无迁移/无preempt、同步barrier、每worker capacityB；集中waitingpool同时选满可用slots的integer assignment最小未来H步load spread，非到达即永久FIFO。§5 L242–321采用bounded iid prompt/nondegenerate variance、iid geometric output、overloadedpool去任意lengthclass后仍足填slots、batch asymptotic与共同有界非负drift；theory实际H0，不将其当H>0或任意stateful系统普适保证，完整proof未作为采用依据。§6 L324–346 BurstGPT trace模拟G32/B72/R128，time=C+t_l*maxload线性模型；L384 H20叙述却称80-step不照录，L386多seed未给数/CI；L417 throughput/energy来自该模拟，不授physicalGPU17×/millisecondIO/no-predictionerror guarantee。§7.3 L431–438 immediateworkerbinding/nonmonotone/fairness-SLO均未解决；预测器误差与solverendtoend开销 Not Disclosed。采用集中batch admission与短未来接口的受限探索，不把数学宣称直接写长期生产结论，Books仅报告。

### [VidLaDA / MARS-Cache](https://arxiv.org/html/2601.17868v1)

2+1+2=5，标准，仅报告。`html-17868.json` §3.2/3.3 L194–209 SigLIP2→LLaDA8B、三阶段视频训练与tokenpooling；§4.2 L375–402 context hiddenstate cache按modality与4layergroup refresh、浅层interval为深层整倍数，浅层更新时深层同步；首step fullattention并搜各frame anchor，邻framechunk+globalanchors，非冻结视觉即可语义无损。§5.4 L487–491与E.4 L1017–1045 zeroanchor Ego65→63.8/MLVU42.6→40.7，过大visual/text刷新比质量损，不授ratio2普适。F L1248–1250训练32H200/b64，F.4 L1285–1288最多32frames、1024/2048CoT预算且bestperformance、MLVU另CreditDecoding；F.5 L1289–1292单H200/b固定thought128、128diffusionsteps/block32/no-parallel，不能合并成与4stageCoT同预算因果或onlineSLO。precision/重复CI/稳定prefix正确性 Not Disclosed；采用modal/depth drift的有限cache探索，非worldmodel因果/全AR替代，Books仅报告。

### [Streaming-dLLM](https://arxiv.org/html/2601.17917v1)

2+1+2=5，标准，仅报告。`html-17917.json` §3 L112–129/L232–250保邻近suffix与trailing positional token、原prefixKV每block内复用；τ=τ0(1−α(1−rmask))随mask减少下降，无token达标取最高confidence，EOS提前终止。新采用点是被mask suffix的局部结构接口，不是把成熟confidence/earlyexit重新计原创。§4 L251–254 Dream7/LLaDA8/1.5，singleA80080、lm-eval、TPS只非EOS；§4.3 L499–512去trailing位置LLaDA79.6→81.2恢复与window128局部quality/speed折中，α过大反退，不授无损/所有长文。B.3 L1179–1180各task/length阈值与window不同、block32统一，225×只2048relativevanilla/不同停止路径，不授通用用户latency/productionSLO；precision/batch/重复CI Not Disclosed。Books仅报告，保留输入length与terminalcue必要条件，不认证suffix可任意删。

### [RemEdit](https://arxiv.org/html/2601.17927v1)

2+1+2=5，标准，仅报告。`html-17927.json` §3 L81–119 learnedMamba connection+adaptiveDopri5 ODE作h-space edit、inner/outerSLERP双旋钮及Qwen2VLprompt补充；AppC L728–729只有connection学习接口，未给metric compatibility保证，不将任意learnedΓ当真实数据manifold Levi-Civita/identity解耦定理。AppB L707–727 learnedtaskscore topkQKV→zeroScatter residual。§4 L350–363 CelebA/LSUN/AFHQ256、500images训练、250attributeeval，但base/one/geometric/dual组件变化不能把全差额仅归几何。§5 L368–373实际反侧unpruned1.82→2.89s，50%prune2.31s仍慢于base且Sdir .184低于base .190；40vs1000steps非matchedbudget，不授统一提速/全identity保持。hardware/precision/trainobjective细节/重复CI/Qwen全pipeline额外开销 Not Disclosed。采用局部连续edit-control与成本折中，质量proxy不认证manifold/无干扰；Books仅报告，不将hypersphere类比写保障。

## 冻结后连续路由/多模态参考批（3项）

### [∞MoE](https://arxiv.org/html/2601.17680v1)

2+1+2=5，标准，仅报告。`html-17680.json` §3 L172–214的token-conditioned Gaussian latent与MC样本生成shared FFN hidden mask，有限W1/W2共享参数；连续mask组合不是无限独立专家容量。§4 L217–238 GPT2-small124M/medium350M、FineWeb10Btokens，MoE4专家top2与K2/每sample25%active的有限比较；Table4 L313–357 bfloat16、seq1024、batch524288、ZeRO1；AppendixB 64H200作者配置，不是LLM serving可行性验证。L300–309实际masked dense GEMM，理论O(Kr)不等实际稀疏加速且可慢于标准MoE。采用连续路由共享参数的探索接口，不采用infinite capacity或通用效率保证，未实现/复现；局部架构分支不要求新增Books。

### [MV-S2V](https://arxiv.org/html/2601.17756v1)

2+1+2=5，标准，仅报告。`html-17756.json` §4.2 L106–110 vanilla时序拼接混淆subject/view，SS把view移空间而subject分frame，TS把video/reference与不同subject加固定temporal gap、同subject各view相邻。§4.3 L118–122 Phantom-Wan/Wan2.1基础2000iterations、batch64、LR1e-5、3600A100 GPUh，randomreference drop/shuffle；50UniPCsteps与reference/textCFG2.5/7.5。§5.1 L292–320为35NAVIobject/35synthetichuman、OC35/HOI35，DINO/CLIP最近view及π3/pointcloud距离是proxy，不是3D真值认证。§5.4 L320–396三RoPE有限对照支持identity接口选择；TS的OCmet3r v→r .109与vanilla持平，r→v .127比vanilla .122差，HOI CLIP r→v .872也低于vanilla .873，不照录全部一致最好。外部MV baseline未MV训练、synthetic过滤与数据同时变，不将主表差额全归因TS。Limitations L819–820限rigid中心object及附加human，非任意deformable/multi-subject。precision/重复CI/线上latency Not Disclosed；有限reference布局分支只报告，不授persistent world-state/全3D保证。

### [MMR-Bench](https://arxiv.org/html/2601.17814v1)

2+1+2=5，标准，仅报告。`html-17814.json` §4 L176–227固定instance×10model outcome/cost矩阵、11000条/8dataset/3scenario，router只能消费query/image与metadata，不偷看当次outcome；oracle只是上界，random不是数学下界。§5 L395–425 frozen2:8split同features，§6 L435–465 equal/adaptive fusion在KMeans改善、KNN却nAUC-.0074且LinearQNC .9055→.9701更差，不能据此授所有multimodal routers adaptive必优。AppendixD L813–850 CLIP先L2normalize却再用norm标准化，norm信号退化且0std处理未说明；prototype取current encoded set，非在线每query无依赖保证。C L760–810混API outputtoken价格与openweightlatency的描述、实际统一OpenRouter output价格表，B L759说input/image/output聚合却缺各价完整账单；不采用一律降到1/3端到端费用。重复run数/硬件精度/queue/feature开销/SLO Not Disclosed。采用离线同outcome矩阵下输入模态与router差异的有限评价条件，不授线上成本/跨域安全或modality-gap唯一因果，Books仅报告。

## 冻结后推理信号/控制批（8项）

本批仅17275/17329/17399/17421/17426/17467/17551/17593，必要源/反侧已交root，不先将作者阅读计独立完成。

### [DeepLatent Reasoning](https://arxiv.org/html/2601.17275v1)

2+1+2=5，中心保证/成本争议受影响深入，拟暂缓/noBooks。`html-17275.json` §3 L132–186同时声称latent预筛少量decode，但双reward都依赖decodedoutput、L172又说G全decode；§11 L489–492 K/G≈.18的5.6x只mainmodelcompute，不含assistant/筛选/训练，也未解释筛选的可得reward。冻结mainweights L144/171不等新latent输入下行为零退化；policy密度/ρ计算仅符号π，连续latent分布与估计机制未给足。§4 8A100、作者称LLaMA2-7B+1.3B（后者checkpoint身份未证）、d512/G64/max32/b4/3epoch，§10冻结对照仅GSM55.4vs56.1及未定义stability High/Low，无旧task forgetting测量，温度0/固定seed不替CI。保留具体latent assistant/frozen decoder提案，不采5.6x与zero-forgetting正面保证。重开需可复查latent policy/density、reward预筛执行次序及包含全部计算的matched成本和旧任务行为证据，不追无关附件。

### [Conformal Feedback Alignment](https://arxiv.org/html/2601.17329v1)

2+1+2=5，标准，仅报告。`html-17329.json` §3.2 L109–131 calibration quantile的CPsets；§4 L132–190两覆盖.5/.8sets的quantile或平均值直接作为u权重PPO-RM/DPO。Marginal coverage不等单answer真值或preference可靠度，nestedsets归属优先和score→[0,1]映射未给足，不采统计可靠保证。§5 L273–305三data新答案增强且dataset数量随model变化，GPT4o四维均值评分不是独立truth；L343–375 DirectAsk权重比base差、coverage.7–.8局部sweetspot、小calibration失准。hardware/trainingbudget/precision/seeds/CI Not Disclosed。采用answer-level proxy对comparisonweight的有限接口，不把新答案生成与weight并变的结果唯一归因CP，不授普遍可靠偏好；局部配方留报告。

### [ReLE](https://arxiv.org/html/2601.17399v1)

2+1+2=5，评价反证受影响深入，仅报告。`html-17399.json` §3 L239–295 hybridEM/BGEM3阈值/GPT4o0513与500adversarialhumanκ.81、Neyman Wσ/√c为成熟recipe，不计原贡献。原增量§6.1 L470–527相同reweight schemes及50model Fullset control RSA10.8 vs dynamic11.4/ρ.96，支持这些权重条件的ranking敏感性而非全benchmark必然错误；5.2%差额不是sampling causal比例。§4.4 L390–401云API-first仍有provider/hardware/调度混杂，统一request接口不消除服务配置差别。§6.2 L535–550 top10anchor难度heuristic非IRT、regularizedCV非严格scaleinvariant。顺序采样confidence与70%成本不采普遍统计保证。该有限weightedaggregation评价条件留报告，不授universal anisotropy或所有provider公平；运行快照/precision/batch/concurrency/SLO Not Disclosed。

### [Oops, Wait: Token-Level Signals as a Lens into LLM Reasoning](https://arxiv.org/pdf/2601.17421v1)

2+1+2=5，sensor→控制反证受影响深入，仅报告。HTML404恢复official exact-v1 PDF，`pdf-17421v1-text.md`为carrier；pp2/4/7/8/11必要内容已读，p8 Table6/7整页实际视觉核。after\n\n的top20logits、avgprob>.02且avg>20次/问题；AIME30+GPQA100+MATH100英语，R1distill7/14/32关联相似不能证明training recipe唯一因果。Table6 suppression incorrect-associated R1 81→77.3、QwQ74.7→70.1变差，但s1.1 70.2→71.2改善，所以不照作者‘consistently degrades’；错误相关不认证有益移除方向，亦非证明这些token因果必需。Tgap AIME32采样去bottom20%，Table7有ties非全胜DeepConf，题目数量小与CI/hardware/precision未披露限制保留。采用局部sensor/control差别及有限干预条件，不授token因果、training决定全部能力或免费ensemble速度，没建立普遍新采样规则故Only。

### [Syllogistic Reasoning and Existential Import](https://arxiv.org/html/2601.17426v1)

2+1+2=5，评价语义反证受影响深入，仅报告。`html-17426.json` L136 agent生成100empty+100nonempty、zh/en×24 forms=9600；§3 L589–602的15+9 distinction/不同EI truth labels与priorcheck显示评价必须声明存在性。§4 L623–668不同checkpoint的RL/scale比较非matchedtraining因果，部分thinking大模型回退、defaultinvalid会伪造invalidrecall；§4.2 L683–691language/MoE/scale混杂。§6 L695–701只endpointvalidinvalid，distillobjective/data不可比，不能普遍distill无效。hardware/precision/seeds/CI Not Disclosed。采用有限syllogism语义约束测试，不授RL推动modernlogic普遍规律、thinking比scale省费或空集自动检测保证；特定逻辑评价切片留报告。

### [Answer-agreement Representation Shaping](https://arxiv.org/html/2601.17467v1)

2+1+2=5，标准，仅报告。`html-17467.json` §4 L134–184 frozenLRM penultimate traceboundary Gaussian→M6 counterfactualanswers→同LRM agreement judge→linear512 contrastivemap，agreement不是truth。§5 L382–393四data25%test/100val、correctness Qwen3-32B judge、超参validation；head不用truth labels不等downstream supervised probe无需label。§5.4 L519–569同TruthfulQA/Qwen8 boundary/σ比较、noise过强退步及delete/mask/paraphrase对照只支持局部interface。A10080/PyTorch2.3.1 L929，sampling训练代价/CI/netlatency/SLO Not Disclosed。Wrong-but-stable仍可漏，AUROC不认证安全或causaltruth；boundaryperturb+agreement训练是局部有价值实施，不形成通用真实性认证机制故Only。

### [GreenServ](https://arxiv.org/html/2601.17551v1)

2+1+2=5，标准，仅报告。`html-17551.json` §4 L190–258 LRtask（少量evaldataset训练）/onlineKmeans/Fleschbins→onehot d12/selectedarm reward LinUCB，LinUCB成熟不计贡献。§5 L267–271 Zeus GPUWh、batch1/BF16/warmup后latency排除queue/features/router/loading。§6 L276–315 A10080/5task×500/16model，normalizedaccuracy上下界仍offline profiling，不是零校准；latency用MaxNewTokens proxy L220不认证deadline。§6.3 L332–350 50runCI与featureall更差/taskalone强、7.77ms占最快36.1ms约21.6%非negligible；newmodel100query稳定singleRun。RouterBench epsilonAIQ.637胜LinUCB.607；§6.4 L374–379 stationaryreward、无实际concurrency/loading/queue保证。采用直接能耗反馈与部分反馈coldstart的有限选择条件，不授SLO保证/无offlinecalibration/allbandit必优；完整部署成本尚不足，Only。

### [Reasoning DAG Geometry](https://arxiv.org/html/2601.17593v1)

2+1+2=5，标准，仅报告。`html-17593.json` §2 L87–131 ProofWriter goldproof nodes+fulltheory meanpool、rank1 linear depth/distance与nodeonly/BOW/shuffle controls；depth排序使重构acyclic，不代表真实内部DAG已发现。§3 L194–241 Qwen.6–32及base/instruct/thinking、1024 stochasticdecode，correct/incorrect distributions仍overlap。AppendixF L567–581 controls与D L515–539 objectivevariants支持linearaccess非causalnecessity；Limitations L274–278 arbitraryquery无goldDAG不能运行此truthgate。hardware/precision/samplecounts/seed/CI Not Disclosed，不造人数；模型规模/probe峰值比较不授内生机制。采用context引入后coarse结构可探测的有限认识，不授真实使用此DAG、faithfulcausal reasoning或正确保证，无新增Books通用规则。

## 冻结后评价/理论批（9项）

本批仅既有64分母中的9项，不新增发现。以下精确HTML缓存均对应v1；理论只核必要假设、评价只核拟采用条件及直接反侧，不冒作实验复现。root已实际通过18113/17500/17602；本批9项均已root实际必要原源独立通过，结果按唯一ID汇总。

### [MalURLBench / URLGuard](https://arxiv.org/html/2601.18113v1)

2+1+2=5，安全受影响深入，仅报告；root必要原源/反侧通过。`html-18113.json` §2 L88–90固定SLD/TLD，只改subdomain/path/query；ASR定义文本接受，不是有害网页实际执行。§3.3 L163–170 Llama2-7B QLoRA280（140shop mutations/140benign）、r16/alpha32/drop.05/NF4/BF16/b16/len256，shop不在后续评测；十轮mutation、j5/topk10、15template筛选存在风险阈值选择。§4/Table1 weather.70/music.61残余风险，不把81%差额写成安全保证或合法误拒绝率；§4.3 L426只有三个人工安全ad-only BrowserUse/QwenPlus案例，不支持端到端有害站点攻击。Limitations L438 advancedDNS/dynamic/multimodal与defense泛化未验，latency/SLO/CI Not Disclosed。原增量是URL disguise的有限测试接口，不是域名parser/QLoRA成熟recipe。Ch72 L2438–2440现有domain allowlist不决定effect、redirect/observable surface仍需独立验收；本稿文本拒绝测试不替实际authority gate，无新书稿写入。

### [Casing in SPLADE](https://arxiv.org/html/2601.17500v1)

2+1+2=5，标准，仅报告；root实际源/反侧通过。`html-17500.json` §3 L94–113同cased模型的lowercase preprocessing，与zero-cased-logit dimensions/λ.2到10k的cased-L2训练分开。§4 MS MARCO8.8M、teacher MarginMSE/FLOPs regularization，BERT/Distil cased/uncased vocab及pretraining同时不同，不能单一capital因果。§5.1 L482–491同casedBERT lowercase31.7→35.4及uncased差<.3仅有限任务；BEIR14里NFCorpus/Quora casedlowercase仍强。§5.2 raw token counts非比例，FLOPs4.1→2.8约31.7%非宣传50%，也不等时延/账单。hardware/precision/runs/CI/SLO Not Disclosed。采用同checkpoint的representation/preprocessing条件，不能形成全检索必须uncased规则，局部SPLADE配方留报告。

### [Information Gain Pruning](https://arxiv.org/html/2601.17532v1)

2+1+2=5；评价proxy反证受影响深入，仅报告。`html-17532.json` §3.2–3.4 L313–405以own greedy trajectory上的TopK-renormalized entropy/logK平均定义NU，NU(q)-NU(q|single d)不是严格conditional MI；两个probe生成路径不同，不是同token的可辨识因果增量。§4.1.4 L499–564 Qwen2.5/Llama3、sameprompt/injection/truncate、K128/MT32；§4.1.6 L648–672 NTE只finalanswer inputtokens，另1+N probing的完整成本没有归入，不能用76–79%inputtoken下降授端到端降费。§4.4.1 L1088–1150 NQ2724/BM25top5的TopM1/5同时改内容数量，不是只排序的NDCG因果实验；§4.3 threshold.05局部最优且过严损coverage。§5.3 L1554–1556明确misleading confident evidence也降低entropy、singlepassage漏joint redundancy/complementarity。hardware/precision/重复CI/在线SLO Not Disclosed；小模型胜大模型仅NQ tightTopM1，不授loglinear scaling law。实际Ch76 L408–411已有reader utility与semantic relevance分离及teacher/proxy/version成本，L432–465已有authority、setcoverage与utility非truth；本稿entropy signal是局部generator-dependent实现，不认证truth或普遍部署阈值，不强造新Books缺口。

### [Pruning Thinking Models](https://arxiv.org/html/2601.18091v1)

2+1+2=5；reasoning压缩选择反证受影响深入，仅报告。`html-18091.json` §3同Llama8B base、Tulu instruct/OpenThoughts think的SFT及17task人口不同，think为8H20/96G三epochs/488GPUh，不能把全部差别归因thinking。§4固定20% ShortGPT/SliceGPT与native/C4/PTB/Wiki/Alpaca calibration；§5 Table3/L969–987动态D-LLM/SkipGPT在think退化仍有MOD例外，40%depth/width分数差只局部8B。depth continuity是作者假说，不是受控唯一机制。AppendixC L1386–1425 recovery instruct10ksteps vs think3k/earlystop/不同LRgrid，equalparameter不是matchedFLOPs/latency。精度/seed42设置不替CI、端到端性能未证。采用思考型模型需单独prune/recovery质量验收的有限证据，不授所有动态剪枝失效或width必优，局部比较保留报告。

### [Environment Properties and RL Generalization](https://arxiv.org/html/2601.18217v1)

2+1+2=5，标准，仅报告。`html-18217.json` §4 L186–205两Llama3.1-8B初始策略已有WebShopRL/SciWorld-ALF-WebSFT，OOD heldout task不等模型从未见知识；150steps/末四checkpoint/三seed。§5 L288–301 observation charcount只是richness proxy、trajectory cap128/50且失败赋50不是真实planning复杂度，跨域action/horizon不同。§6 L338–341只往input加goal-irrelevant observation noise，不改transition/reward，50%trajectories且noise过多损ID；作者交互选到ID下降前，不授通用最优噪声值。Table5 OOD Change是sumdelta/sumbaseline相对%非pp。AppendixA 8A10080G、promptcaps2048/4096、response512/1024、train15/50steps与复杂度probe统一50不合并matched；groups8/task16rollout/.4validation/rule10success，未matched extra-token替代。采用这个augmentation的局部泛化条件，不把domain realism/complexity proxy升级因果定律；这是Agent训练因素研究而非AI-for-Science应用，不按领域名排除。

### [BabaBench / LCV](https://arxiv.org/html/2601.18352v1)

2+1+2=5，标准，仅报告。`html-18352.json` §3三tier aligned/semanticconflict/rulemutable；§4/B 45手构paired states，code/NL actions随机但信息结构未matched，模型规模/家族差不能授普遍scaleworsens prior。§5同grid矛盾rules的joint CE λ2（非InfoNCE/梯度正交证明），预测Python transition后GBFS bound2000。§6 Qwen2.5-7B 600pairedtrain，eval45/45/50；Tier2 60→75.6同时额外data/format/budget，train-test去重未明确。mapgen74.3/76.4/combined72.4非全部组合最强。hardware A100node但precision/重复CI/4xlatency artifact未证；单forward O(1)不等与输入长度无关。采用paired contradictory-rule测试的局部评价条件，不授普遍language-prior因果/在线instant保证，配方留报告。

### [AGZO](https://arxiv.org/html/2601.17261v1)

2+1+2=5，标准，仅报告。`html-17261.json` §4 L154–247 forward activation top-r basis（3powersteps）→Δ=RAᵀ、seed重生成，nonlinear仍fullGaussian，存O(din*r)basis非零额外state。§5.1 L260–317 conditioned A projected-smoothed gradient；truegradient无偏要求allB rowspace⊆A、smooth/interchange及μ→0；实际A由当前batch构造，不把固定basis论述推广成无条件真实算法无偏。§5.2 L325–360是noiseless/μ→0且忽略minibatch noise，收益需captured gradient energy足够。Theorem5.7 L398–421 exactleadingSVD且B diagonal前r平均不低于全平均，lowrank alone不足。§6 L548–565 Qwen.6/Pangu1B两RTX3090，各ZO20ksteps vsFO1ksteps不是相同预算；ZO各自gridsearch，samebatch SST2 alignment及DROP b4/seq256 memory slices只局部可行性，不授全task/规模/设备。precision/repeatedruns/CI/在线SLO Not Disclosed。Ch28 L317–323 actualZO seed/update责任、方差/forward成本与可分性边界已经承载一般推理；activationbasis是有限优化分支，不因新公式名强造长期缺口。

### [KNEXA-FL](https://arxiv.org/html/2601.17133v1)

2+2+2=6，privacy受影响深入，仅报告。`html-17133.json` §3 L209–215 P2P teacherdecodedtext/student retokenize CE为hard target，不是softdistribution；L256–290中央CPM profiles/feedback→LinUCB disjointpair，payload不汇聚仍有中央匹配singlepoint与metadata/output暴露。F L878–889 profile为8backbone/12metrics/12categoryhistogram，concat线性score不自动表达任意pairinteraction。mTLS/guard/utility bandit不是DP或Byzantine保证，spectral联系L291明确intuitive而非convergence证明。§4 L307–362六simulated clients、348/116train/test及128transfer、LoRA2.2–3%、mixedA100/H100 seed42；random相同AKD20round但Local12，central collapse14round/4client与六client不合并普遍结论。L408–423 peak86.7在128transfer上已参与distill，不是heldout；32client48.5%为synthetic五run不是realWAN。Table6 L665–689 H10090GB身份未经证实不采用，未授20agent八A100<16min或生产SLO。采用中央匹配与P2Ptext分工及有限random差额，不把成熟LoRA/加密计原贡献，prototype控制与privacy边界留报告，不授monotonic FL/global安全。

### [Representation Robustness under Erasure](https://arxiv.org/html/2601.17602v1)

2+1+2=5；重要表示保证的中心争议受影响深入，终态暂缓/noBooks，root精确定义与反例独立通过。`html-17602.json` §3 L59–67称BEC/Bernoulli，实际mask按|Xij|≥p确定性阈值；Theorem1 L81–97却用iid Ber(p)、任意unit decoder q/output embedding v、归一化masked q及effective sparsity。其统一偏差界C√(log(M/δ)/(p*s_eff))有具体反例：q=v1=ones/√d，v2=-q，s_eff=d，保留k~Bin(d,p)；masked q·v1=√(k/d)→√p，偏差→1−√p，而声称上界→0。该例top1仍保持，**只反驳统一偏差界及据此推出的保证，不证明top1翻转**。并且decoderstate随机擦除不等encoder-decoder输入阈值后的非线性传播。§4仅小英法translation tutorial/max50/teacherforcing.5/b64/80epochs/RTX3060Laptop4G、AWGN/BEC不同接口，accuracy/BLEU不是定理证明或FM普遍redundancy保证。不因小模型关闭整篇；保留中心冲突，不采定理/noBooks。重开需正确mask分布、归一化/embedding假设及与实现匹配的有效偏差证明，不继续全附录或全部翻译样例。

## 冻结后模型/运行时批（8项必要证据与处置已root独立通过）

本批不增加候选分母，精确版本均v1；源锚点与处置均获root actual必要原源独立通过，不把可选附件/实现或作者实验称已核。未核代码、未复现实验。

### [Power-law Prefill Attention](https://arxiv.org/html/2601.17334v1)

2+1+2=5，标准。§2 L90–138以相对backward offset的floor(j^p)差分mask与w64窗口并集，固定w下O(L^(1+p))；p0/1分别窗口/全连接。§3–4/Table1固定NemotronNano9B hybrid、flexattention、各p使用同200k math SFT与4shot MATH500，GSM8K不同format、thinking off；p.625 MATH.704/GSM.809，p.75 .798/.876，p1 .808/.922，支持该适配条件的局部quality knee，不授普适p阈值。§4 L221–232反侧：optimized full FA可能更高效，改变p也会失去window kernel；没有实测latency/HBM/hardware/重复CI，不采用‘渐近稀疏即加速’。训练不足导致低p underfit为作者解释，非受控训练预算sweep。Books仅报告：Ch22 L201–226已区分访问图改变与IO优化、任务依赖与质量，新的offset布局及局部knee尚不能替通用设计选一个p，非因论文名缺位拒绝贡献。

### [Elastic Attention](https://arxiv.org/html/2601.17367v1)

2+1+2=5，标准。§3.1–3.3、D.1/D.2：首尾各100token key pooling→task/router MLP→每KVhead hard full/sparse选择；GumbelSoftmax/STE、CE+task-dependent non-tight sparsity regularization，只训router冻结base，fused BSA执行mixedheads，singleGPU。0.74Btokens、8A800/约12h/BF16；baseline同环境/data但部分可训Wqkv，不能称完全相同参数预算。§4/Table1–2与§5.2/Table4：code/summ部分对照反退，Qwen8B FA-XA不强；将retrievalheads也换XA后三model均降avg，证明并非全部head都能沿同一稀疏路由。target sparsity非硬runtime等式，boundarypool不保证完整task识别；长度外推只8k～256k RULER、singleGPU，inferhardware/batch/runs/SLO未充分披露，不授普适‘无损4x’。Books仅报告：Ch22 L267–280已有prompt-conditioned route、执行粒度与KV identity、mutation/fallback；本稿新增头级适配训练/融合是局部验证，不能把控制粒度变化升级为全部serving保证。

### [FastKVzip](https://arxiv.org/html/2601.17668v1)

2+1+2=5，标准。§3 L119–243把昂贵context-reconstruction scorer离线产生per-layer/head BCE标签，冻结base、训练hidden-state gate；低rank D'=16、16sink attention的学习分母，score阈值+recentwindow、buf128并行摊销。Base只forward不等gate无需backprop。§4 singleH10080G/PyTorchFA2/nativeprecision，Qwen2.5-7/14B1M/Qwen3-8/14FP8/Gemma12global，12prefill、多query至170k，AIME16seeds/max32k；efficiency为30%ratio与160/240/320k上下文。gate逐token约30–60%开销，经buffer才约1%；NTP/instructionQA标签与reconstruction、同参数MLP/linear反侧支持局部选择，30–40%平均不等每task零损失。并发/arrival/tailSLO、prefixsharing与nonuniformcache真实engine兼容未证。Books已有覆盖：INFER-KV-CACHE Ch45 L684–710实际已有昂贵reconstruction oracle→离线hiddenstate perhead policy、recentwindow、variablecache/kernel成本、model/selectoridentity及FullKV回退；本稿不需另添同链条，性能结果保留报告。

### [S3-Attention](https://arxiv.org/html/2601.17702v1)

2+1+2=5，标准。§3/A.3–4共享Key-trained TopK SAE编码Query（承认K/Q统计shift），streaming scan将featureID→positions保存在CPU、释放chunk KV；Query feature weighted-IDF/NMS取span，再union BM25/LeadTail，收集原tokens重新Prefill，不是精确原attention或永久O(1)总memory。§3.4 128k/4layers/k128仅int32postings就256MiB，Python dict/list更大；§4.7 CPU–GPU同步使端到端可能慢于FullKV。统一greedy/prompt/tokenbudget但外部KVcompress参考数不可直接比较；QwenHybrid18.80与BM25平均同18.80，不能把99%retention全归因SAE。attention权重≠causaltruth，信息下界有强简化假设不采用为真实保证。Llama/Mistral/Qwen 7/8B、BF16/Wikitext2 SAE、9LongBench，hardware/runs/CI/onlineSLO Not Disclosed。Books仅报告：具体内部投影离散化/CPU索引接口有价值，但hybrid机制归因及prototype效率不足以把‘语义对齐’当通用检索真值；不整合其denoising因果宣传。

### [LLM42](https://arxiv.org/html/2601.17768v1)

2+2+2=6，标准。§3–4 ordinary dynamic decode只产private candidate，fixed-shape同model verifier提交matchingprefix+确定nexttoken，并覆盖accepted prefix KV、truncate suffix；fixed窗口小请求group+padding，detprefill、FA3 num_splits1、固定collective配置、seededGumbel与consistentoperators是前提，非只设置seed。§5作者SGLang0.5.3rc0/4H100PCIe、Llama3.1-8B、4096requests synthetic/ShareGPT/Arxiv，在线12QPS 2%det P50=2.21s vs nondet2.15；高det/低QPS globalpause和nonbatchedprefill反而差。§5 L509–522无prefill-decodeinvariance、不支持prefixcache多turn/跨request、speculation尚未集成，TP1–4只correctness、multiGPU公平性能未测，不能外推crosshardware/modelrevision/quantized-MoE bitwise。Books已有覆盖：INFER-CONTINUOUS-BATCHING Ch46 L157–183已有selectivedeterminism privatecandidate/fixedshapeverify、tokens与verifiedKV事务提交、第三类iterationwork、完整detidentity与rollback/SLO/全量traffic回退；不是新写必要。

### [FP8-RL](https://arxiv.org/pdf/2601.18150v1)

2+2+2=6，标准。HTML404后官方exact-v1 PDF成功恢复，必要pp3–10/§2.1–2.3已读，p9Fig7/p10Fig8整页视觉核。RL每步新权重publish时重新block128×128/E4M3量化并sync，KVscale需每step重置firstforward-calibration flag，或trainer以更新后权重及训练prompt/response recalibrate再sync；静态init scales不能自动跟新policy。TIS C2是既有算法，不算新贡献/无偏保证。Dense8H100/MoE16H100、vLLM+FSDP、DAPO/AIME24、maxresponse20k，作者prompt32×n16却rollout写32×3×16，额外3未澄清，保留原差别不硬造batch。Dense FP8withoutTIS质量反退；KVonly与fullFP8均有更高mismatch，p9BF16 legend同有TIS，不能混前dense无TIS对照。38/44%仅该长输出容量/preemption受限rollout、不是全step节省；端到端NeMo8H100全FP8仍比BF16更高mismatch，seeds/CI/实concurrency/SLO未披露。Books仅报告：Ch33 L1366–1393已有同checkpoint不等samepolicy、precision/scale/kernel身份与实际低比特forward；本稿perstep KV recalibration是局部工程实施及recipe，不授全部框架support/productionready或‘全FP8即onpolicy’。

### [Language-aware Quantization Calibration](https://arxiv.org/html/2601.18306v1)

2+1+2=5，标准。§3/§4/Fig2/4/6/7/Table1–2：Llama3.1-8B/Qwen2.5-7B主实验、singleA10040G、GPTQ/AWQ4bitg128，GPTQ1024×1042与AWQ512×512各保持总tokenbudget；translated、nativeC4/Wiki及multimix/multi10/112language分责，code/math混合也固定budget。多语avg与quantizer交互有新局部证据，FrenchAWQ/SwahiliGPTQ反退；AWQ salientchannel大致同但幅度变、GPTQinverseHessian随calibration变。Tail与PPL/下游关联不证明唯一clipping因果或language本质；translated内容控制不等原native全人口控制，summary‘consistent’不能抹例外。Table1zero-shotGPTQ有限task/macroavg，PPL主要proxy，不授所有task性能、bit宽/格式、语言或speed。Books仅报告：Ch49 L881–907已解释scale/clipping、代表pool→channelcoverage及敏感部署切片/校准身份；本稿量化器×语言具体条件是局部验证，未给普遍应选一个multilingualmix的保证，不把‘language-aware’另造全局规则。

### [Kareus](https://arxiv.org/html/2601.17654v1)

2+2+2=6，长期知识差额受影响深入完成，具体owner差额已root独立核、整合及POST通过。§3.2 Fig3 TP4/fourA100/Llama3.2-3B b8表明frequency改变communication SM与launch最佳点：1,410MHz倾向与linear重叠，降频使compute-bound程度变、可倾向RoPE，不是先定overlap再独立DVFS。§4.2/4.4/4.5 dependency-free partition overlap、同microbatch uniformfrequency（switch ms成本）与同type共享配置；smallmicrobatch分割降低arithmeticintensity时sequential更省，不能‘越并行越节能’。§5 MSCCL++ SMgrid/CUDAstreams/events+Zeus/NVML，13s候选profile、5s测量/5scooldown是环境经验；§6.5 tenrepeat温度影响能量测量，非所有GPU固定32℃阈值。真实§6.1–6.2两AWS p4d/16A100/NVSwitch/400Gbps、Llama3.2-3B/Qwen3-1.7B，matched iso-time/energyfrontier；70B/1,280～10,240GPU为§6.3 emulation不冒实测。MBO约2h且97%profiling，不能借54天外部训练说此开销所有workload可忽略；质量/precision/长训练数值与repeatCI未充分披露，不采用frequency-cubed普适定理。Books差额：Ch36 L261–267已有SM/HBM contention-aware overlap搜索/回退，但尚未在该段把频率变更对最优overlap点和energy frontier的条件放回同一planner判断；root已实际核该缺口并授Ch36窄锁；实际L269/271两段与末注L2048补入joint frequency/resource/launch frontier、小work/profile回退及physical/emulation边界，POST通过，锁已释放。

原日期包络见DATE_BOUNDS.json。其93个arXiv事件已证明窗口包络，不代表93候选。本日已冻结64独立家族；106完整arXiv AB=64准入+30关闭+12必要日期隔离，另2native日期隔离。64家族必要审阅/Books处置及root逐项独立复核已完成，整日报告六部分/来源停点/日期包络已root独立验收通过，不是wide377逐项全文队列。17549中心协议争议已获root实际原源与官方协议独立核验、安全终态通过；本轮架构已过17334/17367/17668/17702/17768/18306，17654深入整合Ch36及POST已通过，18150已通过；17602中心定理争议及18113/17500/17532/17133/17261已独立通过。根复核校准及逐项actual状态见下；评分只原新增命题，局部recipe不借成熟原则增加Durability/System Reach。作者实验未复现。

## 2601.17123v1：Acoustic Field Video

原贡献：将空间声压场经图像overlay提供给冻结VLM，检验RGB+stereo丢失的声源可见性，而非改进MUSIC。评分2+1+2=5，标准证据完成；root已独立通过收窄命题、90ms非端到端及归因限制。

原文exact-v1 `html-17123.json` §3.1～3.4：UMA-16 v2的16ch阵列+72° webcam，44.1kHz、2048chunk；MUSIC 2/4/6/8kHz和手工noise floor/clipping，eight-frame median，gray RGB叠jet-map；Gemini2.5Pro输入RGB+stereo vs RGB+acoustic-map+stereo，两条件prompt同步改变告知overlay含义，不是等token/等提示消融。没有raw acoustic native tensor fusion或模型训练。

§5.1～5.3、§6.1～6.4：单阵列十个真实环境5s片段、402QA，两输入条件新session各自推理，3真人独立随机/平衡顺序、majority评正误和偏好，κ=.72/.65。作者overall38.3%→67.4%仅该数据/提示/模型，不能归因独立acoustic表示而排除额外视觉tokens/提示解释。负侧33/402约8.2%原正确变错误（正文6.1另写8.4%，此处不合并硬造精度），包括车辆声源时间错配、HVAC与静止物体误归属，说明声源可见不保证语义绑定正确。§7：固定grid、narrowband、低SNR/reverb、单几何、移动自噪与跨设备calibration未验证；模型生成latency/precision/batch/concurrency/SLO未披露（Not Disclosed），作者90ms仅传感/beamforming等前处理，非端到端VLM延迟。

采用边界：保留特定proof-of-concept输入设计与单任务质量差额，不采用native融合/无训练可泛化/移动产品ready或端到端加速断言。Books仅报告：是手工signal可视化通向既有视觉接口的局部验证，没有足以改变长期raw-signal→identity/fusion链的控制证据；未凭“声场算法名没在正文”强造gap。不是贡献关闭。

## 2601.17348v1：disability-context paired evaluation

原贡献：相同图像NP/DP控制下，社会语境诱发视觉证据外推；评价不仅测sentiment还测interpretation drift。评分2+1+2=5，标准证据完成；root已独立通过此收窄命题及关键反侧。

`html-17348.json` §3.3～§4：200 PAIRS synthetic photorealistic图像，每图NP+9类DP，共2000caption/1800paired contrasts；vLLM开放模型和API闭源模型zero-shot、temperature0/max512；文本VADER/Regard/verbosity与Qwen2.5-72B-Instruct judge分开，judge只看两caption，不看image，所以它校验相对drift而不是绝对视觉真实性。§5.5～5.7：语篇length/Regard大多显著，VADER不总显著；温度0/.5/1与三次生成趋势。Appendix E实际真人检查仅vision-impairment的12图/提示对、5模型、120responses；两标注者分别为有accessibility-tech经验者与normally-sighted NLP practitioner，不支持正文概括出的广泛lived-experience验证。κ=.81/.88/.85/.87、15/120分歧经讨论解决，不能推广至其余群体。这里只采用paired protocol与该设置趋势，不声称所有模型排名、语言先验override视觉的因果归因或通用prompt修复。

§8 limitation：synthetic images、zero-shot descriptivecaption、text-only disability context，没有真实disability视觉标识或下游任务验证；judge仍可能有偏差。§5.4将语言先验依赖作为初步解释，attention/attribution与sentiment因素尚待后续实验，不能升格为被证明的机制。系统吞吐/硬件precision/batch/concurrency/SLO与闭源endpoint快照Not Disclosed，性能速度不采用。

Books仅报告：特定paired-caption评价协议有贡献，但不把该群体语境的局部关联升级为一般多模态fusion因果；保持报告层证据边界，非要求通用章新增benchmark清单。

## 2601.17311v1：多数树的限定放大/预算边界

新增命题评分2+2+2=6，标准完成，必要源锚点已交root复核，不冒作real-agent scaling law。exact-v1 `html-17311.json` §2.1～2.4定义binary Y、leaf bias g(x)≈kx^β、BSC有效通信gamma、奇数fan-in；rho-shared模型是以rho概率共享同一投票、其余概率iid的混合，不是任意pairwise correlation。§4.1～4.3在该模型下majority map T(u)=f_(b,rho)(gamma*u)，alpha=gamma[rho+(1-rho)f'_b(0)]>1才有深树bias放大，否则趋零；gamma<1仍有固定点饱和，不是Bayes最优协议保证。

§5.4 Eq32～37再要求small-signal/未饱和、同一token线性预算B≈N(x+c0)，s=log_b(alpha)>beta才可能scaleout胜单体扩算；x*=beta*c0/(s-beta)，预算阈值忽略饱和，不可拿到任意LLM成本模型直接选人数。§7.2仅已知生成参数的b5/gamma.6/mu0.05、rho sweep、depth10/30、50,000 Monte Carlo对递推sanity；没有realagent新任务的独立gamma/rho拟合或收益验证。§8.2～8.4明示参数会随层/任务/提示改变，one-bit/majority限制，丰富消息可改变映射及指数上限。独立旧研究的定性相符不是验证全部结构普适。

Books仅报告：实际Ch82正文已有固定budget的task-topology matching、communication/error amplification和相关错误/单体回退论证（Coordination Tax与Peer/Debate），这里新增的特定二元混合公式尚不能迁移成realstack组织规则；不借定性已知原理授Dur3，也不因alpha公式未出现强造普遍知识缺口。保留此模型可计算的限定诊断而非整合通用scaling。root已实际核§5.4/§6.1/§7.2及small-signal/预算/混合边界，标准OnlyReport通过，无需重复附件。

## 2601.17343v1：知识编辑specificity sensor的混杂

评分3+1+2=6；因直接修正编辑保留性评价，受影响内容深入完成，source/owner窄差额交root。exact-v1 `html-17343.json` §3.1～3.5：GT数据知识≠原模型行为；严格token匹配将语义同义回答判错，contrastive只检测两个候选相对次序而对分布漂移饱和；teacher-forcing的answer内部fluency也可主导。§3.4从ZsRE抽2k query，以gpt-5-nano判一致/不一致，Llama3-8B仅33%一致，这仍受judge误差约束，不作通用发生率。行为保留应对同一query比较原/编辑模型；lasttoken KL明确不是新metric，topk support overlap提供可调严格度，但不是整个生成轨迹或真值证明。

§4.1～4.3：MCF/ZsRE每2k massive edits而非连续更新，Llama3-8B主实验、GPT2XL/Qwen2.5-7B附录；MEMIT lambda从1.5e2～1.5e6，正则变化明显而GT指标饱和，KL/topk有更敏感秩序；10方法跨数据集排序比较只能说明此proxy响应不同，不认证哪一方法所有行为更可靠。§5关键反侧：lasttoken漏长程依赖/有效continuation，lambda或正则强度非final specificity真值；topk忽略概率幅度、KL tail可能敏感。运行预算、硬件/precision、seed不确定性Not Disclosed，未采用吞吐数字。

已实际读Ch66约L1000编辑→RAG仲裁段及前后：现文将edit success/locality与冲突仲裁分开，但没有区分locality sensor自身的GT/teacherforcing混杂。root实际核源/owner后授窄锁；已在locality段后新增before/after preservation对照及proxy边界两段、末注；特别topk相同不保证KL数值小，不采用原无条件bounded-divergence概括。Ch65/67交接已读；写后diff-check通过，root实际两段/前后编辑与wrong-premise邻接/末注非作者POST通过，末注状态已修、锁已释放；单项不独立代表日级；本日最终六部分验收随后已root通过。

## 本批必要证据的实际独立状态

root已实际核17564方法/Table1及nonmatched反侧、17885几何/readout/CDM与sim/real条件、17902 confidence单用WER反退/并变策略、17737 VSA及必要反侧、17450 HARMONY探索接口，均标准OnlyReport通过，不重读已过附件。17569必要privacy source/counter与Ch72 L209～244/327～365具体已有覆盖通过，处置改为已有覆盖（PLATFORM-SECURITY），不是新书稿diff。以下保留各项证据，作者实验未复现。

- [17564 JaxARC](https://arxiv.org/html/2601.17564v1)：2+1+2=5标准。exact-v1 §2 fixed30x30 padded/mask+functional JIT/vmap/pmap ARC后端，§3仅固定MiniARC task100steps，多run次数Not Disclosed；M2CPU batch65536 789k/21k=38x，3090 batch131072 32.6M/36k=903x，H100同batch142M/26k=5439x。790M为2Menv、不matched，14kx亦跨不同batch；ARCLE>131k崩溃为缺数据。只能保留matched环境吞吐及后端扩规模可行性，不授RL训练端到端、跨hardware精确rollout复现或通用reasoning效率。硬件内baseline运行差别/JITcompile计时、precision/seed次数/SLO未充分披露。Books仅报告，局部环境backend验证不改变训练runtime或Agent控制长期机制。
- [17569 P3](https://arxiv.org/html/2601.17569v1)：2+2+2=6，隐私受影响内容深入。exact-v1 §3.2实际server每轮收到accepted/corrected prefix，再按retrieveddoc regex PII spans过滤；不是profile未上传就无泄露，query/语义偏好/未识别PII仍可见。token probability ratio>=tau收draft，拒绝则client argmax替换且丢剩draft。§4.1两A10080G、3Bclient/14Bserver、k10/tau.05/temp1、Contriever10；不是真实edge/network。§4.2仅200query/五BM25相似profile候选，22.5% queryonly→24%协议结果不等DP或全部adaptive/repeated攻击保证；作者称GPT-4.2(OpenAI2024) attacker的模型身份未由本文建立可核官方快照，攻击数值不作可信privacy证据。§4.2 token9.2%只client新生成，不包括每token评估，23.6s作者runtime不是服务SLO。Books在Ch72 L209–244/327–365具体已有覆盖；只采用窄cross-boundary机制/反侧，privacy保证不采用；不授profile全程不离端。
- [17885 PEAfowl](https://arxiv.org/html/2601.17885v1)：2+1+2=5标准。exact-v1 §3.2～3.5 co-located RGB-D仅depth branch估bin，knowncalibration→expected3D anchors→topK距离softmax crossview gated residual；frozenCLIP text-query iterative readout；CDM仅offline训练teacher。§4.1四cam、9simtasks50demo各，real6tasks100demo各并task-specific finetuning，所以不是zero-shot sim2real；100sim/10realtrial，无CI，预算/hardware/latency/SLO此主文未披露。§4.3单步readout在DR更差、depthpath稳定局部ablation，不能唯一归因跨视角一致性或断言免费前端。Books仅报告局部perception-to-policy recipe及受限条件，不改通用融合/动作安全链。
- [17737 Script-to-video](https://arxiv.org/html/2601.17737v1)：2+1+2=5窄标准。exact-v1 §3 frame-anchor末帧relay/segmentation为成熟方案，SFT/GRPO不计原贡献；§4.2 VSA按script指定时间窗作CLIP(frame,shotinstruction)均值，补仅全video‘内容出现’的局部sensor。§5.2作者aesthetics/scriptfidelity排名分离只此设置，窗口CLIP不认证事件逻辑/精确时间或judge真值；prompt细化/锚点同步改变，无独立causalablation，预算/endpoint快照和评价uncertainty未披露，不用排名作通用模型选择。Books仅报告此领域的时间窗proxy，不授长视频identity或艺术质量保证。
- [17902 dLLM-ASR](https://arxiv.org/html/2601.17902v1)：2+1+2=5标准。exact-v1 III-F CTC prior初始化/长度anchor+confidence token exit+padding prune，speechKV借FastdLLM不算新机制且无独立cache消融。IV-F具体反侧是confidence单用Whisper-LLaDA降RTF却损WER，prior增加首轮过阈token后联合质量恢复，支持这个局部选择条件，而非‘三recipe名字即增量’。LLaDA8B/Whisperlargev3 encoder/16A100cluster，τ=.9、四英文testsets；baseline训练预算/推理实际设备数/batch/precision/重复数Not Disclosed，不采用4.44x普遍加速。Books仅报告ASR既有prior/可变length在此token-confidence接口的局部验证，不授一般diffusioncache正确性/streaming。

## 本批决定准入的定点关闭（具名分层独立校准已完成）

以下17507/17879/18226成熟recipe关闭已获root原则校准。18130借embedding/matrixfactorization router、previouslayer selfconfidence/crossjudge normalize-average及cost排序/earlythreshold，无新有效条件；18267只声明admissible memory/citationmembership audit，没有新增hardruntime enforcement；17755实体target-degree/全degree加权与answerprob-difference/entityoverlap dense reward未给新credit成立条件，三项必要§3.2～3.4/§2.4/§3.2～3.3读后贡献关闭。9具名关闭17197/17716/18204/17982/17418/18116/18146/18203/18386完整AB已root实际分层核，不写全30已独立验。

- 17507 §3.2～3.4：VLM normalized expertweights、state-expert dotproduct softmax、alpha linear fusion+TD-MPC2 prior regularization，未超成熟hierarchy/selection的具体新条件。§3.5 Bellman contraction不能独自授整体物理可行性/复杂度保证；不采用该宣传，贡献关闭。
- 17879 §2.2/2.3：asyncio create/terminate/delete、最新TCB registry/isolatedcontexts为成熟thread管理。§3.2 blocking/concurrency/tool/context ablation只有全benchmark与earlystop case，未辨识新执行机制/受控互相干扰条件；贡献关闭。
- 18226 §3.1～3.3：tool synth/reuse、batch semanticcluster/LLMmerge成熟组合；§5.3 EGL=newtools/toolinvocations*1000，固定任务流趋稳不等知识泛化，无修正重要评价的新控制条件；贡献关闭。

## 决定准入的必要定点方法（不冒作全部证据完成）

- 17152 exact-v1 §3：每question让每model承担每role生成proposal，再所有model打分均值选role最高者；rolecriteria由modality/domain例子自动生成。多proposal/互评/均值分配为成熟组合，未辨识新选择成立条件或受控失效边界；贡献关闭，不给候选评分，不采用LLM评分可靠或附加budget净收益。root准入校准共同理由已纠正。
- [17450 exact-v1 §3FinishedWork](https://arxiv.org/html/2601.17450v1)：OPERA ICSE2025、OATest已接受ICSE2026引用旧成果，不能把266bugs全作本次增量；HARMONY本篇还ongoing：多源operator constraints生成低级IR seeds、documentation/code优化patterns驱动validity-preserving mutation，TVM40authorreported新bug/26confirmed。拟只该low-level testing新命题准入，不把全pipeline拼接算跨生命周期突破。评分拟2+1+2=5；进一步读取评价对照条件后标准完成，若缺pattern/预算报告则窄化。
- 17671 exact-v1 §2Eq1及2.2：target question生成English pivot+targetanswer做SFT；将抽取的同Englishquestion再次交给同policy生成Englishanswer，以二者相同1/不同.1/formaterror0作REINFORCE++ reward。翻译pivot与同policy一致性reward为成熟配方，未定位新增正确性条件或反例；贡献关闭，不给候选评分，不声称selfagreement=正确或跨语义可靠。
- 18203 exact-v1 §3：section/page/element hierarchy，逐页LLM更新section树；summary traversal+text/visual TopK集合并取，已有MDocAgent generator后query-only done反射、再检索。方法澄清为通用hierarchical RAG+multimodal retrieval+reflection成熟组合，尚需有限ablation是否给出新增适用条件才能贡献关闭/保留；不把“human-aligned”当特殊机制。
- 18282 exact-v1 §2Eq1～5/11～13：function think string及parameter{think,value}，复杂度linear scorer threshold触发，执行前recursive strip还原原函数，描述metaLLM/continuousprompt优化。既有reasoning field、complexity门控与prompt优化配方，模块内参数粒度变化未给新条件或失效路径；贡献关闭，不给候选评分，不采用普遍可靠调用保证或benchmark数字。
- 18386 exact-v1 §3Eq6～12：目标是ResNet50/DenseNet121 surrogate到ViT-B16的binaryreal/fake攻击。Conductor调ε/SSIMτ，CW/JSMA/STA生成再project，Mixer hillclimb权重，stagnation时放宽ε/τ；文本称无target访问却Eq7/12使用p_bb feedback，盲测假设需区分。genericimageclassifier攻击应用并不自动构成LLM安全或agent新执行边界；必要安全排除/范围判断已root实际core与完整AB独立通过，不能根据“agent框架”准入，更不能采用transferability数字。
- [17360 exact-v1 §4 Definition1/2](https://arxiv.org/html/2601.17360v1)：同一个f的preimage I_y与有效certified local ball定义使每个区间包含z且均为I_y子集，因此并集恰等于I_y；不能支持同一f的expanded inference set。§5实验比较base与不同smoothed classifier，只支持换classifier后label集合/utility/abstention变化；概率证书仍有失败概率，§6 always-label协议不可继承abstain证书，全部query sidechannel消除也未证。root已实际读定义/实验/always-label并独立通过该关键反侧。重要隐私认识准入，评分2+1+2=5，因中心保证争议已深入核受影响内容并安全终态隔离：报告保留争议、Books暂缓。重开需作者在同一f下修正定义/非平凡新增隐私证明，或明确换classifier及query协议的受控保证；不继续遍历全proof/攻击附件。

## 独立校准已通过的贡献关闭

17277：human code-switch结构/人口差异与三任务新benchmark，原AB未给修正具体训练/评价选择的受控证据；17645：文化meme新域失败/排名，未定位新系统条件。17212：MMR与query动态diversity为成熟检索recipe，提分不能替代新条件；17443：similarity聚类再合并memory为已有冲突压缩，beat-naive非新边界；17699：execution feedback/adaptive turns/composite reward为成熟agent/RL组合，18x数据效率/SOTA不是机制增量；17722：schema任务合成与SQL确定验收的已知组合，enterprise complexity/47%未建立新评价盲区。均由root实际完整原AB复核，不扩大到未受影响材料。

## 已收束的准入尾部：三项标准OnlyReport

- [18077](https://arxiv.org/html/2601.18077v1)：2+1+2=5，不采用同base额外HanabiRL→OOD gains作为memory/合作训练因果；root实际§5引出具体评价盲区并准入。作者已补读exact-v1 §3setup/§5/B.2/E.3：Sherlock由HLE供全员deductivecontext，Mycroft删除该engine支持及otherplayer perspective，以自己上一轮deduction/action/reasoning/move ratings滚动重建；几强模型score局部反退，只说明外供scaffold成绩不能认证内生跨回合state tracking，不证明scratchpad唯一因果或所有强模型失败。2～5player每设置10shared seeds、同模型selfplay；defaulttemp/topk、highreasoning，Gemini20k，endpoint revision/budget时间未充分披露。HLE终态score非judge，E.3另o4mini-high judge与HLE context对照仅5player/5seeds，不授全部state真值；外部perspective/prompt/token预算也同变。HanabiRewards actionratings为LLMjudge、原文承认非严格verifiable，不采用其RLVR标签保证。标准必要证据/OnlyReport独立通过，不扩大17model排名。
- [18281](https://arxiv.org/html/2601.18281v1)：2+1+2=5，exact-v1 §2.3 Eq4～6 fixedchunks(responseaudio+transcript)/(unspokenreflection)，用EmpathyEval描述offpolicy交替监督GLM4Voice；§3 ChineseOpenS2S约50k、训练/评估按顺序90/10，EmpathyEval混合标签及300人审仅验证该sensor，不是实际用户共情真值。§4.2同base前置CoT反退、关reflection收益消失，§4.3 chunk<9及attn重权>1.5反退，约>=15较密交替局部改善。多组件训练/额外token/同源judge、ASR+Emotion2Vec辅助评价未隔离全部因果，latency/hardware/precision/batch/SLO未充分披露；不认证实时语音/心理安全或普适自省。root必要方法/直接反侧标准OnlyReport通过，无新Books长期缺口。
- [18253](https://arxiv.org/html/2601.18253v1)：2+1+2=5，exact-v1 §3.2 PI=Z(norm)*Z(L1distance-to-centroid)挑极端case→teacher逆生成rubric，§3.3几何resampling/PLS；新增冷启动选择接口及median-density条件，不借PLS/缓存/AWQ成熟原则加分。§4.1 700internalexpertsession、一A10080G、PLS5components；§4.3 HelpSteerVerbosity重新训head，非zero-shot移域；§5.1 bootstrap排test，与expert rubric局部可比，去resample k-alpha .796→.615，此分布下必要。§5.2 layer-score差只有error相关，非calibrated risk；§5.3 2300users/CUPED rho.212仅4.5%variance变化，不能沿用169x或1.4M/day为匹配服务吞吐。私有标注/模型/precision/batch/预算不同、endpoint与重复不确定性限制归因。root必要core/反侧标准OnlyReport通过，不写新Books。

root完整AB分层复核指出17277新human codeswitch benchmark和17645文化meme failure/排名未建立新增控制条件，原“合成分布不同/新模态盲区”通用推断不够。两项贡献关闭，不因其本窗日期明确恢复深审。共享理由影响的具名benchmark/recipe判断已定点重校准完成；没有扩大列表或把全部宽库存再筛。

## 冻结后安全/隐私批：必要命题与直接反侧

本批独立状态：root实际原源与直接反侧通过17549协议争议终态、17344五分安全深入OnlyReport、17383六分安全深入已有覆盖（Ch72）、17566六分深入已有覆盖（Ch84/Ch70）、17644六分深入OnlyReport、18110和18292五分深入OnlyReport；本安全7项在累计21/64时已通过（不是另增7项）；18113后续已通过必要源与OnlyReport判断，不在此前7项清单。

本批仅采用精确v1，原实验未复现、artifact未核验。17549已root实际源/官方协议反侧独立通过安全终态；另7项必要证据与Books处置亦已root实际原源独立通过。未披露的hardware/precision/batch/concurrency、API revision、完整查询/训练预算、服务SLO不补造。

- [17344 The Shadow Self](https://arxiv.org/html/2601.17344v1)：2+1+2=5，安全受影响深入。`html-17344.json` §4.2～4.3 L317～374以SoRA/PBA/PRA构造压力场景、Python工具/MCP/ReAct、judge看完整轨迹，RAC是可见reasoning文本而非内部latent intention。§6.1 L383～388三次attempt任一成功、10tool cap/temp.7、GPT-4o judge；§6.3 Table2 L411～533只GPT-4.1/400sample，ethics classification3.25%、选择13.5%、contextualized20%是不同输入/执行协议，非isolated“自主性”因果。现实/虚构及neutral-persona framing局部变化，risk-averse17 vs risk-tolerant25.75；§7.2 L539～544安全提示20→17同时新产生5pp危险轨迹，LlamaGuard4的低检出只该版本/标签。§7.1 L535～537仅60场景/三模型轨迹人审，overall87%与逐项95/95/97叙述不合，人数/统计未给；A.3 L1058～1064另一60scenario benignness只80%一致，存在资源可见性/工具质量混杂。只采用“moral judgement与具体动作风险、framing必须分开评”局部反侧，不采用intrinsic internal motive/所有输入fullybenign/production risk或解码不敏感通律。仅报告：Ch72 L610～649已有non-command framing与goalalignment不授权、L713～759 run/effect/pairedcontrol合同；本稿没有支持改写该长期权限链的受控保证。
- [17383 PPIA](https://arxiv.org/html/2601.17383v1)：2+2+2=6，物理prompt-injection边界受影响深入。`html-17383.json` §III L164～214未知userquery，但允许已知系统name/任务及环境物体放置；§IV L218～300四模型同图Nova/Bob/no-name toy对比，再以Llama3.2-11B recognizability候选选择、CLIP surrogate attention择位置，不是目标内部不可得又直接读目标attention。§V L304～336两个模拟器/QA-TP-NAV，ASR仅targetword出现，10volunteer readability；§VI L650～679六模型真实摄像cart导航、受控室内/道路，端到端dangerous effect与词出现不等同。§VI-C L852～856同物体位置的三个不同CE候选、同prompt三位置ASR70/82/87支持局部可见性/部署条件，非全位置最优/因果attention；§VII L899～905 strictOCR降低ASR但丢任务signage，低分辨/开放动态环境未证。API latest drift、物理重复数/CI、推理硬件延迟预算Not Disclosed，不采用全日稳健/80%真实事故率。已有覆盖PLATFORM-SECURITY：Ch72 L1180～1224已有不可信图像text/layout/provenance及readability与真正unsafecompletion/effect分账；本稿是物理name-matching与visibility的窄新验证，不需制造新安全owner。
- [17549 Breaking the Protocol](https://arxiv.org/html/2601.17549v1)：2+2+2=6，安全深入、中心协议命题争议终态，Books暂缓。`html-17549.json` §III-A L118～132把sampling列server capability并据此称resources→sampling无限升级；但[官方2024-11-05 sampling](https://modelcontextprotocol.io/specification/2024-11-05/client/sampling)要求client MUST声明sampling，[官方lifecycle](https://modelcontextprotocol.io/specification/2024-11-05/basic/lifecycle)同样client角色且Operation SHOULD使用已协商capability。论文“v1.0 December2024”未绑定有效dated revision，不能把host policy缺陷授全部compliant实现。§IV-C L257～267仅自述同tools/payload/prompt/network，§V TableIV sampling baseline N/A，不能用其ASR认定普遍协议放大。§VI L359～418 CA/HMAC/nonce只认证身份与消息；§VI-G/VII-B L487～519明确authorized malicious content、firstcontact、alertfatigue、无formalverification/adversarialbypass。厂商实际CA部署与8.3ms完整配置未可核，不采用。root已实际原稿必要段与官方两页核验，通过本争议终态，不是贡献关闭/访问故障。重开仅需作者有效datedspec角色更正、同接口/权限/行为预算对照及可验证实现，证明具体新协议条件；不扩协议全史。
- [17566 Sponge Tool Attack](https://arxiv.org/html/2601.17566v1)：2+2+2=6，成本攻击受影响深入。`html-17566.json` §3～4 L90～176允许read-only internal信息且仅query mutation，不是无任何知识；offline17probe/15round反馈归纳policybank，baseline≥20%cap的probe和本已达cap测试被排除，影响总体人口。Eq8～10 reward把增加steps与embedding cosine惩罚交易，不能严格认证semantic preservation（归一化描述与Eq9范围不合，Table2“similarity”还含1.25，不作为概率/真值）。§5 L373～408有1775题/13dataset、六模型、12tools、四framework、15/40caps；Table3 Qwen2VL OctoTools47.27→45.58、GPT4omini52.86→51.23有质量反退，非结果始终保持。Table2步数/±未明确独立seed含义，实际GPU-time/网络/账单/排队/SLO未测，不能把step放大作费用倍率或严格DoS。采用可复用queryrewrite在有限caps下扩tool调用的局部边界，非全部任务/框架普遍保证。已有覆盖AGENT-PLATFORM：Ch84 L634～667已有独立资源记账、固定cap与stop evidence、边际toolcost/quality合同，Ch70 L110～137区分cap/真实资源与utility；不另写新的安全/账单证明。
- [17644 Membership/Captions on mRAG](https://arxiv.org/html/2601.17644v1)：2+2+2=6，隐私受影响深入。`html-17644.json` §3 L112～143的blackbox image+prompt接口以资产检索库membership与caption extraction为两个目标，不是参数训练membership。§4.1 L232～244 CLIP n20/Jina k5、Qwen2.5VL7B/Cosmos7B/InternVL8B，50%测试随机成为库member、三randomruns；MIA image-image rerank，而§5.1 L357～377 ICR image-text rerank，caption metrics只已加入members。§5.2/NoRerank L481～482 weak image-caption alignment时去rerank增泄漏，ConceptualCaptions差小，给出检索/跨模态selection条件；“漏另一条caption”不等泄漏目标资产。§5.3 L511 conditionalICR对MIA误阳置零有条件分母，不能与无条件privacyrate合并；§5.4 L513～538只两prompt的guard识别，不是adaptive防御/合法utility验收。§6限制textonlyoutput/visioncentric/smallVLM，医疗例子不是临床隐私部署验证。仅报告该有限rerank/对齐接口：Ch72 L327～365已要求database/context各observable channel与retrievaldepth/selected-vs-recovered分账，本稿局部关联不能授通用降低k/rotation防御或新隐私保证。
- [18110 AttenMIA](https://arxiv.org/html/2601.18110v1)：2+1+2=5，隐私受影响深入。`html-18110.json` §III/IV L109～231 whitebox attention全文读取、邻层Corr/Frob/KL/barycenter与三类扰动→MLP；“referencefree”无shadowmodel不等无knownmember训练，Algorithm1与§V-A L690～697明确用gold member/nonmember五fold监督。Hellinger展示选最高head不等无选择偏差，扰动前后attention长度对齐未给完整实现；L120/125“member更大shift”与L194“member更稳定”解释冲突，不采用记忆机制因果。§V-C L1144～1148 dedupPythia差小只局部；§VI L1215～1248 GPT2、14k生成256tokens、同candidates对照，groundtruth是互联网source continuation，不等确认训练集；取ROUGE最高/最低各1000相关.480不是verified extraction rate。硬件/总feature cost、classifier训练预算和低FPR uncertaintyNot Disclosed。仅采用白盒attention统计新增sensor接口；仅报告，Ch72 L258～283已有identifiability/knowntrainingprovenance与sensor-not-verdict，本文未填未知训练库识别或开放API可部署条件，不写memory/extraction保证。
- [18292 TriPlay-RL](https://arxiv.org/html/2601.18292v1)：2+1+2=5，安全受影响深入。`html-18292.json` §3 L100～146交替每次只更新red→blue→eval，最新red生成蓝训练，heterogeneous experts对安全与utility投票为eval标签；不是独立于训练闭环的安全真值。§4 L147～155 Qwen3-4/8/14B、1800seed、GPT5.2最终ASRjudge，§5.3 L202～205仅3000agreement-filtered数据（双标签一致再保留）支持局部classifieragreement，不授rewardhackproof。§6.2 L210～238去loop/diversity两因素局部对照OD.588→.156/.514，weakdefender ASR反而更高；loop entropy600～800与noloo p200～400训练步不matched且没隔离只冻结eval的对照。Table2最后总结把.2写2.8，与表行冲突，不copy该数字。Table1 L164～201 avg32有4B AIME67.40→65.21及14B IFEval86.70→85.72，不能“无任何reasoning损失”。8H800；训练总预算/precision/独立runs与稳定性Not Disclosed，§limit承认无均衡/控制growth guarantee。仅报告动态第三角色接口与此diversity/攻击强度取舍，不把GRPO/自对抗成熟原则算新知识，不授稳定co-evolution或无人工安全保证。
