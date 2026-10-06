# Owner合并8项必要原证与实际差额（root终态通过）

完整exact-v1题摘、必要原证及实际owner均已root非作者核验；22067/22070/22072/22091具体Existing，22056/22122/22124/22142实际正文、完整邻接及自身末注POST通过，窄lease释放。坐标均为`V3_BLOCKS_2602.<ID>.md`的block而非行号。外围proof/科学应用不展开，未核代码/复现，不授日级完成。

## 22056 FlowCorrect — 2+2+2=6

[v1](https://arxiv.org/html/2602.22056v1)43–99/111–120/122–136。冻结ManiFlow backbone，head LoRA修改vectorfield；记录原noise x0、baseaction、humanrelativeSE3 corrections与mask，重新积分同noise拟合纠正终点；成功无纠正rollouts作anchor。Gate读当前observationcondition，label为整个预测horizon内任一mask正，推理>.5硬开闭，**不保证只改变单个已纠正位置**。Source88明确LoRA可global effects；128：“a single locality gate … can lead to over-correction”相近ID/OOD纠正相反时ID-hard仅3/10。96写H=-α(1−α)称binaryentropy/促decisive，但最小化此项自身偏向.5，故不采用这条促极端解释；BCE+有限gateablation仍可支持有限经验，不将记法外围错误升级整篇Disputed。

UR10/Robotiq/ToF+proprio，2obs/14predict/10execute/10Hz；human≈15Hz vspolicy≈1Hz不等闭环安全。Base8demos3000epochs；FC/RT同10corrected+5success每failure、500epochs/4090/B64；TableII FC4.35GB/30.24min vsRT19.23/52.93，含人工/基础训练未免费。TableIII fullID74.45 vsnoGate61.11/noRollouts66.67，但OOD70 vsnoRollouts83.33/RT96.67。任务不同OOD（位移 vs杯高）不可合成普遍泛化，10repeat/条件有限。拟PRE Ch26 actual275–291 frozenlimitedinterface/HIL/anchor论证：**同noise重放对vectorfield局部编辑＋horizon gate仍可冲突**是窄差额；保直接BC/完整retrain/人工接管，额外积分、gate/纠正费用近文。不授locality/safety证书；Ch26有28窄lease时等释放。

## 22067 Semantic Partial Grounding via LLMs — 2+2+2=6

[v1](https://arxiv.org/html/2602.22067v1)18–21/25–31/32–40。PDDL原domain/problem语义→pruneobjects/predicates/actions并一致删initialatoms；syntax、boundedsolve、集合subset与goal相同只soundnessproxy，21明说“rather than … guarantee”、原任务未必valid。实际后验VAL核原taskplan；不认证保全部solutions/最优或completeness。175tasks/7domains/GPT5 snapshot2025-08-07/K1，与PLOI仅arity≤2的100tasks不同支持。36/175prunedtasks不能yield原validplan；FG161/175 vsSPG139/175，PLOI90/100不可直接总体合。Table1只commonlysolved人口：Agricola grounding103→22s但search156.7→251.3，Hiking/TPPplanCost变坏；10task仅SPG解出也不证明全面优越。M2/24GB剪枝API与Xeon8GB/1800sLAMA两阶段，LLMcalls/原模型training/fullfees未全。

拟SpecificExisting AGENT-PLANNING Ch79 actual77–81 partialsupport≠完整任务覆盖/原fullaction回退；175–177形式签名/solver自一致≠原语义；195剪枝可恢复/原更宽搜索。有限语义剪枝改变grounding成本与合法解人口验证这些具体边界，不为PDDL新名字加段。若root判实际cost人口差额未承载，仅原剪枝论证补句，不采通用soundness。

## 22070 Language Models Exhibit Inconsistent Biases Towards Algorithmic Agents and Human Experts — 2+1+2=5

[v1](https://arxiv.org/html/2602.22070v1)20–28/33–35/40–47/50–54/63–65/91–98。主8snapshots数据mid2024：27task100ratings无performance；6task200bets给两expert各10binaryhistory，90%vs50%身份random、顺序random，T.3/top-p.99。Statedgap5.14～30.68偏human，revealedalgorithm选多；neutral9.9%剔除且94%来自GPT4，需留完整人口。Bothalgorithm A/B控制无性能选择偏差；不由textchoices授真实生产delegationeffect/内在人类偏好。64承认两study未engineer directlycomparable：信息有无、任务子集、rating vsbet奖励一起变，**不授单独‘format’因果**。

Jan2026原v1附6newsnapshots决定反侧：GPT5statedgap反向，其余meanneutral；strongalgorithm系数1.46/p.06不是显著唯一人偏，stated/revealedRR转<1且两model不显著。主旧趋势不能静态当2026通用模型行为；版本、任务、信息、choice/denom各固定。API/serverless且硬件/precision/SLO/fullfees/repeatedtraining未全，无human内在状态。

拟SpecificExisting Ch66 actual159–176 source/协议身份与selfreport不是权威来源；419–436声明不是行为receipt、需要真实trace/outcome，456–460不同prompt/CoT输出接口分账。此有限statedvsperformance-conditionedtextchoice验证**声明不能代决策验收且版本会反转**，不制造通用偏好/安全新段。

## 22072 Understanding Artificial Theory of Mind — 2+1+2=5

[v1](https://arxiv.org/html/2602.22072v1)29–56/59–81/Table1[83]/Table2[84]/87–95/102–104/189–191。7humanstages×10perturbation+16templates共1088question、人工每sentencebeliefsets允许ambiguous多合法链；6open33–132B/A100/T0，one-shotJSON malformed剔除、模型minorprompt差异。Gold proper-subsequence测文本belieftrack、Rouge/transitionoverlap另proxy。Table1unperturbedmean67.2→89.6但全perturbed49.9→53.8；preposition32.9→24.2/automatic55.7→43.6/sentiment37.6→25.5，CoT不是全提升。50%十类门槛是作者操作定义非心理ToM证书，表非独立1088人类认知样本。

79以CoTcorrect/finalcorrect相关φ≥.4声称causal；Table2.342～.584与102“不makingup”不识别cause，正确答案也进入proper-subsequence终态定义，相关部分被接口绑定。Mixtral错误CoT也改善的95反侧只说明答案/trace不同步，不把placebo认定唯一机制。采用有限trace与final、perturbation配对诊断，不采用faithfulness因果认证/所有模型心理缺陷。新humanbaseline/closedmodels未核、artifact需作者请求，不依赖代码。

拟SpecificExisting Ch66 actual2176–2196 graphagreement与textsensor≠truth、456–460 directCoT与长度/截断分账、419–436过程vs终局；Ch8现行为能力不授真实理解。标准有限负面支持这些论点，无新ToM收纳段。

## 22091 Learning to Drive is a Free Gift — 2+2+2=6

[v1](https://arxiv.org/html/2602.22091v1)25–50/76–86/104–110/125–131。π3teacher看N+M整段 unposedvideo，student只N past，AR futuretokens→point/pose/confidence；SegFormer每futureframe伪semantic，GroundedSAM2+CoTracker+teacherpoint轨迹阈值生成motion。41作者：“not self-supervised”；**label-free不是无supervisedteacher、无futureprivilege/先验**。7semanticclasses/motion阈值不是真实metricstate或causalactiondynamics。32A100/BF16/40ksteps/OpenDV约2Msamples；1.45B/5090reported5Hz缺batch/end2endplanningSLO。Finefreezeencoder、sameanchorhead/3frontpastframes，LFG用lastfuturelatent，baseline加temporaladapter不同总pretrainbudget。

Table4 sameencoderhead LFG1/10/100label66.3/81.4/85.2 vsπ3 56.2/77.5/82.8；DiffusionDrive多camLiDAR88.1full更好非LFG全支配。Table7 AR去掉1%66.3不变、10%77.7<81.4；doublepretraindata与longerhorizon低label收益但full84.8<85.2。−segmotion84.6；A1 PPGeo sameOpenDV改善10/100但1%退，不唯一因果归sequencefuture。仅NAVSIM离线score无onroadsafety。

实际Ch25 18–34 futureprediction≠actioncounterfactual、Ch26 93–105 teachertrainingprivilege/nonruntimegeometry與336–377 futurelatent/objectives已承载。拟SpecificExisting Ch26：**sequence-levelfutureteacher监督是训练支持，不是真实新观测/无prior**，必要有限matchedtransfer/反側验证；若root认为整段teacher支持与逐frameprior需明确局部差额，可Ch25predictivebranch一句，但不为4Dname新段。

## 22122 Probing the Geometry of Diffusion Models with the String Method — 2+1+2=5

[v1](https://arxiv.org/html/2602.22122v1)26–41/50–60/66–85/89–104/128。仅model/image路线，protein科学应用不采。固定两endpoint反ODE到noise，71stringpoints evolution+equal-arclengthreparam；puretransport依赖初始path，强score近mode，finiteTwalker/Voronoireject+EMA；score近data不可靠要quench。原91区间写`0.1≥t≥0.95`空，应不采用精确schedule为可复现实装；Figure4–6仍有限比较。SiTXL/256/VAE4×32×32/γ15图简化vsγ.01更real，T.1/.5/.9后者逼真且likelihood降向validation分布；作者显示likelihood直方图非独立人评/全FID质量。Approxlearnedscore/finitequench不授exactMEP/principalcurve/物理transitionstate保证。

强γ要求Δt=O(γ^-2)、71points/walkers/reparam/likelihoodODE都费，原speed不是目标，hardware/precision/总walltime未披露；不能把低density缺失的重要state恢复。有限图诊断只支持**最大点density与典型人口/perceptualquality可分离**，不称所有模型模式不是缺陷或一般学到正确能量。

实际Ch24 104–119采样迭代/schedulecost、222 likelihoodproposal改变人口与最终修正但未讲点density高不等typical路径。拟PRE Ch24扩散采样机制旁一窄段：路径诊断比较transport/强score/finiteT、endpoint/score误差与成本、likelihoodvsperceptual分账，保原sampler/固定budget，不纳protein与普遍收敛证明。

## 22124 SWE-Protégé — 2+2+2=6

[v1](https://arxiv.org/html/2602.22124v1)17–39/42/47–49/52/56–63/93–96。SLM保decisionmaker，askexpert是policyaction，expert读recent5msg而SLM历史processor特保expertreply[95]，不等完整原history无压缩。SFTteacher+expert看goldpatch生成resolved~4.8k，evaluation不看gold；160RL/100tasks/G6/B16，loopgate+expertwarrant+followthrough复合奖励；expert自己judge共享偏差，finalexpertreply需posthocjudge否则无nextcallcarry。48第二阶段无expertcall硬−10，不能宣传完全自由的不调用也最优。

QwenCoder7B/SWEagent75steps/$2/≤6expertcalls，8A100/H100、vLLM/APIbackend限定。Table2RL+1.2/+6.2/+2.8，−loop31%→.8%但loopphase准确只小变，后followphase其它权重也变，非单因素因果。61关键对照：Loop/fullCtx33.4vs29.0；recent5Ctx29.4有无Loop均同；forcedfixed19.6/random24.2比policy自主29.4低却专家调用不少。Inplace加入experttext14.2<原17，freshcoherenttrace不同数据支持；frontierteacher有gold不授无prior。专家输出11.9%并未包括inputmedian8885/p9520716/max43031或student约300ktokens、train/hiddenjudges，4.2×/8.2×只expertfee不全流程省。heldout400发布时间不认证无mem。

实际Ch82 847–853按状态与uncertainty委派/返回验证/单agentfallback；Ch80 225–238 selectivecritic与预算/proxy非truth。尚缺**学会怎么调用不等什么时候求助／是否后续使用，反loop与follow两个验收**。拟PRE Ch82 delegation处一窄段：policyhelpaction+boundedcontext/可见advice、warrant/follow共享judge非authority、hardnocall训练偏置/forcedschedule反侧、全费与原单agent/显式loopguard回退。若现具体论点足够请Existing，不以7B胜32B当成熟专业化新原理。

## 22142 WeaveTime — 2+2+2=6

[v1](https://arxiv.org/html/2602.22142v1)32–49/54–66/69–73/79–91。train timestampinterleaving，shuffleframecontents重建trueorder后QA，不加外head；timestampcue可能支撑重排，原100cases无timestamp-only/static控制，不授唯一visualcausalmanifold。Inference localwindow初答entropy<δ直接，else再次Answer C2Fhistory，先framepooledcosine→withincoarse maxsim topK，漏coarse不能fine恢复。Entropy只是触发proposal非truth，低entropy仍可自信错，历史KV来自当时可见prefix/nonfuture。

30koffline LLaVA synthetic IT/1epochLoRA/lr1e-5/8GPUtype未披露、LLaVAOV7B/ReKV/1FPS/max64recall/δ.6；多turnvs其它offline单turn不混。Table3ReKV53.56→timestamp49.88→+TR55.70→+cache57.57；Streaming66.15→65.91→68.49→72.13。Table2完整LLaVA-ReKV61.72/68.82与Table3不同子集口径勿合并，partialFPDours75.24<StreamBridge76.23。Table4C2F25.2recall/55.2AccvsReKV23.9/54.3、fineOOM但hardware/完整memory未全。Fig5thresholdtradeoff只作者曲线57.57局部最佳非跨task最优；30k/8GPUvs121k/32GPU不是matchedtotal费用。

实际Ch23 900–925时序训练支持与真实arrivedprefix分开、历史固定memory与trigger，尚缺**时间顺序显式重建与current-first是否recall是两个干预，timestamponlyfine-tune可退**。拟PRE该stream论证单窄段：ordertraining/entropyrecall分责、current/history身份与coarse漏证、local/宽historyfallback、二次answer/存取/训练与阈值成本近文。KVkernel不复述Ch45，不授strictstreamdeadline/temporalgrounding证书。
