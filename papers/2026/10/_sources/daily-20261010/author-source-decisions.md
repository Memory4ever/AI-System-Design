# 2026-10-10 作者必要 Source 与 owner 差额

仅处理2026-10-09北京时间自然日。live1010_author实际读取下面exact-v1的选定方法、主评价和直接反侧；原文选段保存在同目录 arxiv-core-batch1～5.json、arxiv-mimo-core.json、arxiv-tensor-mimo-core.json、arxiv-dlcb-core.json。选段不是“已读全部附件”，未核代码、复现或生产部署。首次26完整题摘及代表5EX由root实际独立校准通过；4Tensor中心反证和MiMo另经root校准。评分不借用成熟原则。所有新增Books由root串行写，作者只提出PRE和实际POST。

## VFold — 2610.12338v1，2+1+2=5

§4的每head可逆V变换与Wo逆变换是精确代数折叠；CCA/Hungarian校准后跨层平均则是有损近似。只在本步attention之后更新共享值，保护4sinks+128recent；K的RoPE不能照搬任意可逆变换。128×2048 Wikitext校准，三GQA模型LLama3.1-8B/MistralSmall3.1-24B/Qwen3-8B，RULER16K/LongBench，与unaligned、MiniCache-V/CommonKV对照。LLama质量92.48→91.14/50→49.4。A10080GB/batch1/8192in256out/3timing runs，V减50%=总KV减25%，1.11→.84GB，TPOT21→27.8ms反退，TTFT781→786ms；精度/线上SLO未披露，不授普遍加速。§6.1/6.2消融与composition足够支持局部共享机制。
PRE Ch45 565–655已有uniform/trained共享，缺同head可逆折叠及post-attention更新差别；root新增582/584两段，作者实际POST完整uniform→新增→trained邻接通过。

## TokenRouter — 2610.12242v1，2+2+2=6

§4.1–4.3请求中心编程与模型中心子engine解耦；running转pending保留模型本地KV，回到该模型只append已提交tokens，不重准入。异步本身会碎batch，delayed threshold再合批但有等待/饥饿/死锁代价。DTMC依固定并发/路由概率/步时建吞吐模型，不给任意SLO。§5/A与必要D.3/D.4：8A10080GB，Qwen.6B与32B TP2/2GPU CUDA MPS；AIME100in2048/8192out、SWESmith8192in1024out闭环Nworkers，总生成tokens/time；部分baseline无CB，不能把2–64x当普遍engine gain。N8逐项132.78→230.79→296.86→372.48只属该工程/async/delay链；delta.1是局部校准。不重建未完整提取的硬公式。
PRE Ch56 277–344 handoff兼容已有但缺pending localKV/模型局部delay；root写296/298，作者actual POST完整邻接通过。

## Attic-KV — 2610.12133v1，2+1+2=5

§3诊断未知未来问题下全文rehearsal分散极紧KV预算；真实question+answer oracle5%93.5vsfull94.7只作诊断。§4.3每4096chunk用KeyDiff anchors所在句token数估计rehearsal数量，再取该数量的salient tokens，而非保完整句；另合成6QA且每答≤256tokens并引用context。两路rehearsal保留分数取max，不是先合成QA再从它估计全部anchor预算，也无本文已执行的压缩后readback gate。
Qwen3 4/8/14B与LLama8B，RULER4/16K、14自然LongBench、LooGLE105短文1951问/60长文459问；dev/test分离。3%73.4vs全文31.5，20–30%差≤.7不再有优势；长LooGLE ROUGE22.9低于KV²23.6。10doc/20q计时126vs154.8s未披露GPU/precision/batch，不能当可移植cost。
PRE Ch45 722–790未来utility/LORE已有，但缺content-adaptive rehearsal与自问read-outs两路分配。root写LORE之后/gist之前两段；作者实际POST首次发现两路误合和未有readback，已请求root窄修；修后需重读，不自授通过。

## SGUID — 2610.12367v1，2+1+2=5

§3完整bank先参与200step探测，以Verify×Gate的signed正signal及late≥early/τ与最小late量排序选compact bank；从同一base重新训练200steps，不把prune写成单次训练免费收益。R1 K6、R2 K3 coevolution只属该recipe。§4–5 OLMo3-7B/Qwen3-1.7/4/8B、DAPO17K、4H200 LoRA、traincap1024关闭thinking而eval开启，三bench avg@12以最佳checkpoint均值选点，有选择偏差。25step探测4B退1.7pp，K2损覆盖，删persistence65.1→62.3；三random-skill-selection seeds非全部训练独立重复。单轮数学不证明工具Agent经验泛化，probe+restart+skill generation成本保留。
PRE Ch33 1055–1095 DerivedSkill已有当前policy反事实utility，缺跨阶段信号持久性选择并重启compact蒸馏；root写1074/1076，作者actual POST完整DerivedSkill→新增→Privileged邻接通过。

## LCT — 2610.12376v1，2+1+2=5

§2–4先用MDL/bidirectional entropy/HMM发现latent morphotactic pieces，再按频率收益pack成固定surface vocabulary；推理min-token DP+bytefallback。latent语言结构不等最终模型发出单元，balanced language evidence不等equal vocabulary quotas。§5/C.1固定104语言FineWeb8GiB、RTD DeBERTaXSmall seed42/15ksteps/256batch/1.97Btokens/8A10040GB BF16；200k MEM compression4.866vsBPE4.295、Morphscore.5209vs.441，Gini.1341≈.1342。MEM不最短、τ.2优于equal0，lowresourceBelebele还低.07；仅encoder训练，不授decoderLLM增益或加速。finetuneseed正文与Table5列名不一致不自行消解；Python慢tokenizer未实现高效runtime。
PRE实际Ch11 270–345语言fertility→词表优化→pretokenizer→global objective→checkpoint，缺latent分析与fixedsurface packing分层；拟词表优化开头后两段。

## Elastic Expert Routing — 2610.11575v1，2+1+2=5

§3 E[K]=8对称6–10离散Gaussianσ1.5，在训练token×layer随机改变top-k前缀，从rank j得到P(K≥j)暴露，非softtopk或在线可变预算。推理固定k8。§4–5 OLMoE1B7B/Qwen3-30BA3B SFT和1.42BA365M/128experts/26.25Btokens从头训练，匹配expected active-expert FLOP。SFT均值31.41vs30.57/58.44vs56.42，QwenTruthQA51.93<53.14、OLMoE Math6.44<6.52；router/expert swap部分收益说明共适应非router独因。SFT periter+3/5%、pretrain局部-.06，不把expectedk当真实dispatch/peakmem/wallcost相同。16GPU EP4 BF16 GPU型号未披露，middlelayer选择为exploratory。
PRE Ch21 429–520已有fixedk/cutoff/selection-v-contribution，但缺training rank-exposure随机化而inference固定k分支。

## PTP-U — 2610.11915v1，2+1+2=5

§2–3给固定sampled knowledge unit normalized likelihood对比约束S_u≤b_u，non-target BaseKL anchoring；KFAC阻尼子空间localQP唯一依fullrowrank，是局部非global。Attention更新后FFN重线性化，actual model验证/回滚。StageII固定mixture(q=(1−α)current+αBase，target stopgrad)恢复，必须forget约束仍满足且BaseKL下降，否则rollback/减恢复；非全局最近投影。
§4–5 LLama3.1-8B/Qwen14B、RWKU/WMDP/MUSE/TOFU、4RTX4090；noStageII MMLU57.92vs63.80但forget29.23vs28.99，removeconstraint retain64.84且forget44.62，直接显示恢复会返知识。35.5min42.7GB加成本，1.2s未有完整长度/batch/precision不可外推。HTML appendix被引但未有对应正文，仅采用已足够的方法/消融，不授未读proof、未知queries删除或法律erasure。
PRE Ch72 2760–2880 sampling/tail/curvature/edit/refusal/precision已有，缺恢复retention时actual-model forget gate与rollback独立；拟曲率后两段。

## SFT-as-Context — 2610.11132v1，2+1+2=5

§2–5先领域SFT回答，再父模型读原问题+SFT文本+固定instructions，双pass非权重恢复。19对(8math8code3nutrition)/11bench，保92%专化gain与补94.2%general gap是所测平均；仍有domain退步/小parent只boxed格式失效。NutriBench counterfactual own-response AB只对该slice排除secondpassalone，不能全task因果。理论需共享domain条件律/perfect SFT domain law/posterior concentration及OOD lowerbound，不是实际LLM保证。
§A4/C2/I maxseq32768/Nutriresp8192，greedy或benchmark推荐3generation runs；math/code第二答案≤13%，nutrition198.1%/143.9%，且tokens口径未计extra prefill和双model memory；hardware/precision/batch/SLO未披露。不声称省成本或parameter恢复。
PRE Ch29 963–1047现仅weight/训练期forgetting mitigation，无父模型读取SFTresponse的runtime组合分支。

## TRACE — 2610.11678v1，2+2+2=6

§2–5及§7/E分三个证据对象：fresh pairedwhole-system受控重跑、行为trajectory检查、保持trajectory不变的scorer重判；非所有score变化都是能力改变。ResearchOps25deterministicscripts三同结果seed标签不是真独立rollout，alias mapping修复250→0具体系统bug。Tau2四agents30→158tasks/3runs及heldout88，self-rerun14.7–16.3%/Laguna35.6% flip显示singlepair噪声；误导性names positivecontrol可解164不是全等价证明。
7/8等价±.10，Qwenformat一项9.3pp excess inconclusive(6Bonferroni)。118固定轨迹两judges3calls surface stable但57%disagree，procedure-v-outcome多数163/201 GPT objections由keyword heuristic归类；原grader非groundtruth。未知mutationfamily/部署率不能推出。
PRE Ch66现harnessidentity、freshjudge、repeatattempt、clean-twin均已有，但缺上述三层实验分开估计behavior/noise/scorer；拟harness总论两段。

## OnTrack — 2610.12375v1，2+1+2=5

§3–5/Limits三accessregimes：reference+schema可L2alignment/L3gate、schemaonlyL1/L3、norefonlyL1vitals，不冒全对象score。stream DAG full/partial/missing metadata，shell隐藏dependency可漏；provisionalgraph retro更新。固定nodemass1/meanrefsize避免prefix伪增，frontier parents/young age/explorationTTL3/leak25%约束OT coupling。
fastwarmCG clippedGWgradient+L1是diagnostic，非exactUFGWobjective/globalopt；escalatedconverged仍非global。M5Max t=m40/K3 p50.85/p951.6ms，30mssolver budget不覆盖长≥100状态且O(n²)memory。
2288SWEtrajs430resolved1858unresolved/oneinstanceeach，228calibration+5references。阈值.6是illustrativeposthoc，resolved falseabort20.7%，节约17.9%是unresolved成本非alltraffic完成价值；earlyk5 steps baseline更强，k15cosine差消失，lengthmatchedAUROC.526，GWablationwithinnoise。不批准automated halt/成功保证。
PRE Ch66 3172–3220 diagnosticgraph/interval与4029–4057prefixcounterfactual已有，缺frontier partial-reference结构matching的online分支；建议interval之后两段，仅sensor/保留真实runtime权限。

## DreamTrue — 2610.12468v1，2+1+2=5

§3/4/B/C用URDF action-render image+depth amodalmask+Plucker/gripper背景三个image-space条件；RoMa/SAM3跨view/time robotcorrespondence离线camera/mount calibration。Wan2.1VACE14B，3view240×320/101frames/0.7B LoRA128；先2232h/5robots/4datasets paired train，再冻generator只RL LoRA。SE3endpoint扰动+IK合法不等真实未来；Qwen3.5-9B human L1/2/3 defect classifier的negative概率是plausibility reward，非counterfactual physics truth，GDPO分三渠道+DiffusionNFT。
800heldoutpaired与160CF54task6models960videos/3blindannotators分母不同，object31.88→3.12、interaction48.12→6.25仅CF人审；paired PSNR不可搬至CF。RL后EWM72.84→72.51总体反退/若干physics维度更差；L1F169.37vsacc96.69反映rareclass。nativecondition/budget不同不可纯架构因果。RoboTwin3tasks×2settings×4VLA×10=240，FP26→12、MAE12.92→7.08point与rank24不签单轨迹truth/physicalsafety；occlusion仍物理错误视觉合理，hardware/precision/完整时延未披露。
PRE Ch25 1176–1269完整integrity/offexpert/embodiment/render/calibration，缺action-render表示与未配对CF奖励边界；拟offexpert gate之后两段。

## REACT — 2610.12007v1，2+2+2=6

§3滚动H50/K5/S10buffer，block不同noiseτ=(j+1)/K，每freshobs一次Euler，跨K观察refine再front不可逆commit、shift追加noisytail；warmK−1 holdresetpose不能计真实action。staircase train匹配time/position不保证完整conditiondistribution，换K/S zero-shot未验。
DualDecoupling sensor/M2VLM/DiTworker异步同RTX409024GB，latestready用capturetimestamp单调publish；30Hzsensor/S为3Hz条件freshness。DD语义age均233ms/p95383/max416，3Hzperiod333ms，故不采用“始终最多落后一帧”。
§4/C/E RoboTwin7tasks100eval/50demo，真实6taskplatform×30trials；DD sim44.86/19.86<49.71/20.86、real64.8<65.7质量取舍，pouring63vs57局部。734±94vsRTC747±123不证humanlike统计优势，jerk仅成功人口；无independenttrainingseeds。BF16AdamW sim30kbatch32、real20epoch128/256batch，不授hardrealtime/safety。
PRE Ch26 894–957/1515已有buffers/asynclateKV/blockdiffusion，缺多noise滚动与跨观察每步update；拟streaming总论后两段。

## BudgetPix — 2610.12307v1，2+1+2=5

§3entropy quadtree平铺image，coarse encoder resize+detail aggregator、scale decoder+localrefiner，全管线finetune支持固定image size可变tokens，不是drop-in删tokens。main default随机layout比例与appendixb.1ofthe-rest不同不合并。质量推理先pred-clean再重建layout每5步，timing once-frozen layout CUDAgraphs是另一操作点。
§4/C/D七parent+MeanFlow：budget-parent无额外FT而ours有FT，RTI有trainedadapter对别的untrained方法，收益不可全部归layout。seed0一个FTseed，pixel25% GenEval.725vsunadapted.323，own100%.741vsdensebaseline.721说明有adaptation；JiT低budgetFID差于dense，pooled25%FID20.39>fixed19.79。
1H100BF16，JiTbatch50/32、mini20/pixel8、textpreencoded、2–3timedcalls/perlayoutgraph；bitidentity仅部分，others20/27/34dB、pixelgraph23dB因此不用graph，不能跨quality/timingvariant拼端到端SLO。40kFT、warmlayout、layout rebuild与refiner皆付费；小human/VLMstudy非truth。
PRE Ch24 1197–1245已有refinement/decoder/pixeldecoder，但缺retrainedvariablepatch表示；拟OutputDecoder前2段，保留两operatingpoint/成本/反侧。

## LeWAM — 2610.12407v1，2+1+2=5

§3–6/C/D四mode：latentforward/backward+inverse/policy同backbone，每batch四forwards，liveencoder无EMAstopgrad/SIGReg。noise steering优化Gaussian policy inputε，经确定性8Euler flowpolicy成actions，再latent rollout；norm投影√A sphere只限半径，不认证整个Gaussian训练support或物理安全。
41MViTtiny224/384CLS，4frames skip5/5stepchunk，6PushT/robomimic200demos90%data、5trainingseeds300epoch；250closedloop各task，41–43M架构不同、RecVAE另3.9Mfreeze，不纯JEPA对照。64candidates×3iters H5sampler预算匹配非真实inferencecost/hardware匹配。rawactionMPC3–8%而noisesteering也利RecWAM，非JEPA独因；CanDS78.8<policy82.8、Square去inverse82>80.4、no-policyDS极差展示policyprior作用。无realrobot，goal取demonstration最近latent后25steps、planningstill慢。保留8Euler×候选成本与短闭环fallback。
PRE Ch25 900–978、1000–1032 search/value/geometry已读，无noise-space方案；拟搜索价值策略sharedowner之后两段。

## MiMo-V2.6 — 2610.11959v1，2+2+2=6

当前report以官方Oct9公告归属，不把Sep27 tool-call blog重算。必要§4.1/4.2.5–6/4.3/5.1/5.3–5.5/6.3–6.4：1568prompts/G16/25Kseq、2.7–3.7Btokens每step、RL成本2.6M/.9M；micro/partialrollouts新policy后re-prefill，mini-harness50→66为整stage非singlemodulecausal。
窄采用SampleMixer：target合格group B_i、acceptance r_i，attempt demand B/r再乘平均duration t分并发；αB/r+(1−α)deficit/r weightedRR α.5对0/1trace simulation不含training/staleness/replay/creditlatency。startup replay只初始policy或fresh window bootstrap，先完成短轨迹低估duration导致GPU/CPU KVOOM；mempacking/EP>30x内部图不capacitycertificate。
GRS pass×rubric×behavior，GAR已confirmedhack置0再重算组advantage/rank-positive/uncappedmass，cap/recenter改变严格界；grader unusablefallback；128promptcodeFlashablation只局部长度趋势，loggedhack<2%不unknownrate。routerfreeze restorelayer9 routingbalance诊断不能泛化allrouter；SWA/R3/FP8成熟原则不抬分，不据quantizedrollout QPS签RL质量。
PRE Ch33 1375–1430服务group readiness/VenusRL已有但缺acceptance×duration×deficit/startupbias；root两段actualPOST完整邻接通过。

## 4Tensor — 2610.11716v1，2+1+2=5；中心争议暂缓

必要method/evaluation已读。rank4 jointsemantic/temporaltimefiber attention对全(x,t)归一，时间不causalmask；shiftlossS1..S3 targets已在window，只有lastS4未见。input/readoutrank1而internalbilinear，局部设计潜力保留，不因one seed或小模型排除。
ROCStories97929train3742validation非test，vocab含val、截断2457sentences，val32173nonpad。AR free-running sequential训练与tensor目标/execution不同；attention参数100.7vs33.6M、embedding4.7vs75.2M虽总172.5vs175.9M接近，不能归因attentionmechanism。2RTX3080/batch64/AdamW3e−4/drop.1/oneinit，CE5.554vs5.701、2.4vs45.2h只作带混杂作者结果，不正面采用walltime或普遍accuracy。videoencoder/render/planner在外不宣称实现。
root独立认可准入及此中心争议安全终态；Books暂缓，不进入正面采用。重开只需matchedobjective/readmask/parameterallocation必要控制或可信独立局部分析，不要求baseline全重实现、不把普通未读当材料受阻。

## DLCB — 2610.10547v1，2+1+2=5

事件门已核：官方 cs.PL/recent Fri9五项中DLCB[2]为原categorynew，后[3–5]明确cross-list，发表于Oct9；abs Aug19 submitted不当公开归属。native列表一次误返abs后官方web成功，只定点核身份不扩category队列。
§2PyTorchJIT支持子图与native fallback，safe shape generalization、dimexpr fixed-point rewrite、预编GPU CUDA binary加16opcode residualhost程序launch前resolve/CHK_EQ/BROADCAST，dynamicrankknown/dimunknown AOT参数化、unknownrank才JIT；dynamic vectorization runtime contiguity/divisibility guard，scalarfallback。statictrace broadcast hint须runtimecheck，rank/type/constantargument cache身份与不能任意solvesystem边界。§5 H100/CUDA13.2/cuDNN9.20/PT2.11/FP16/3warm5timed，static1.10×、dynamic.92×vs eager平均，compilemedian.84vs9.4s≈10×不等推理10×，GPUindexdivision/单vectorwidth/layout缺优化有反退。batch/具体shape网格/数值容限NotDisclosed，未核artifact/生产。
PRE Ch49 20–94现graph/staticinput/不规则KV/lowering未承载fixedrank parameterAOT+hostresidual/unknownrankJIT分层；拟静态接口前两段。

## 独立复核与恢复

最终局部POST：作者实际回读Ch45 LORE-KV→Attic→gist完整邻接（775–805），两路分别为内容密度预算与引用原文QA read-outs，共同选择KV；修复后的成本只含QA生成、rehearsal与排序，未虚构压缩后读取检验。与必要原证一致，Attic非writer POST通过。其余实际写入及具名非writer POST由两独立审阅笔记承载：5 RL/OPD见independent-training-evidence.md，6模型/评价见independent-model-evaluation-evidence.md，14系统/多模态家族见arxiv-system-topic-note.md。这里只复用有效单项结果，不签DAY。

作者不会自签Source独立权限或DAY。必要源提议+owner实际PRE已交root逐篇独核，Books actual修改仍由root，未写项不计已整合；上面明确actualPOST的项只授对应局部。13机构有界原记录由root负责。GooglePubs公开日期段、Qwen/Hunyuan动态目录、MiMo剩余无日期Blog是已隔离外部来源限制，不授无遗漏；这里所有作者候选必要正文已可用，没有普通Source待办可外部化。

