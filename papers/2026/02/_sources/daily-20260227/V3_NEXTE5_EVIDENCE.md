# 后续5项必要原证＋actual owner（root终态通过）

精确v1完整题摘及必要原证/实际owner均已root非作者核验；21947/21952/22010具体Existing，21978/21997实际正文、完整邻接及自身末注POST通过，窄lease释放。block坐标`V3_BLOCKS_2602.<ID>.md`并非文件行；不遍历外围proof/附件，不授日级完成。

## 21947 Large Language Models are Algorithmically Blind — 2+1+2=5

[v1](https://arxiv.org/html/2602.21947v1)必要18–40/47–59/63–72/89–90：4causaldiscovery算法×13datasets×100bootstrap共5200作者executions，8LLM×52condition×3prompt1248calls，平均各prompt的**预测区间**看是否包含实际empiricalmean，共1664比较。9benchmarks+4syntheticlinearGaussian，算法default超参，不是对实际代码/数据有全部visibility的通用runtimepred。Table1/4 coverage15.9%、Claude39.4vsrandom36.5、其它5.8～15.4，说明这些冻结描述型prompt不足代替真实算法测量；不声称没有任何可诱发性能预测能力。

关键边界：randomuniform endpoints只比intervalcontainsmean，不匹配LLMwidth或properintervalscore；宽区间可提高coverage、metric本身未要求95%nominal预测概率，因此**15.9%不是所有任务95%校准的general failure率**。Empiricalbootstrapmean也有uncertainty；F1/precision/recall/SHD相关，90已承认，不能把1664作完全独立总体。LiNGAM assumptionsnonGaussian与syntheticGaussian不匹配，本身改变算法行为，原69–72“algorithm差异排除difficulty、只memorization”过强，90也明确indirectsignals不能排除其它解释；不采memorization因果，更不因此否认有限实际forecast miss。3prompt/zeroshot且89承认CoT/RAG可改善；CPU/hardware/precision完整执行时间、API版本receipt/repeatedLLMs不全，无复现。

拟具体Existing：WORLDVIEW-LLM-INTELLIGENCE Ch8 actual57–73区分复述/给规则推演/真实实验发现，语言模型提假设、真实算法/环境提供结果；PLATFORM-EVALUATION-SYSTEM Ch66 actual339–351区分模型评分/下游区间推断/有限bootstrapmean并留估计条件。采用仅**文本先验性能区间非executedmeasurement**有限验证；不把blindness标题/memorizationinvalid当新的通用纠错命题，不新增因果应用段。如root认为需要“预测区间宽度比较”窄gap只补真实measurement边界，不全audit所有统计。

## 21952 MindDriver: Introducing Progressive Multimodal Reasoning for Autonomous Driving — 2+2+2=6

[v1](https://arxiv.org/html/2602.21952v1)必要29–42/44–52/56–60/66–73/98：6surroundcurrent+4frontpastframes，textsemanticCoT→futureimage(128×192ARvisualcodebook)→6trajectorypoints；annotationdecisionfilter读GTtrajectory/logicQwen3judge，max3errorfeedback重标，futureGT是trainprivilege，不是deploy真实observation。Stage1CLIP-imagecosine+format，Stage2trajectoryADE+format；semanticCLIP不是像素空间criticalobject位置或physicaltruth、sixparsablepoints也不是安全合法。Table4[60]noCoT L2 .99/coll.56、text .96/.46、image1.06/.55、I2T1.01/.47、T2I.95/.41；imagealoneL2反退，不授dream默认有效、T2I人类causalchain识别。Table6[68]rawCoT2.48/1.40 vsnone.99/.56，3filters.98/.53+feedback.96/.46，换数据与oracle/judge费。

Table7[72]noneRL.95/.41/FID9.8、one-stage.97/.42/9.7、progressive.93/.38/9.4；固定one-stageweights .33/.67非全joint优化recipe，steps1200vsbaseline/总annotationfee不全，不授唯一curriculum原因。ST-P3过去平均与UniAD逐步口径分别；GTtrajectorycollisionoffline不是realdriving安全。CARLA220routes SR39.55 <largerdataAutoVLA57.73，budget不同，noon-road。16H20/96GB/encoderfreeze/SFTfull12/6epochs B32/RFTLoRAr32B16 stages700+500 or1400+1000，precision/完整latency/SLO/重复不全，生成与judge都费。

拟SpecificExisting MULTIMODAL-EMBODIED-VLA Ch26 actual328–377三种future→action接口、future只是provisional、jointloss不证future真正causal使用、训练目标竞争/ID-OOD/physicalcommit分责。该finite语义→image→trajectory排列/阶段reward验证没有反驳原论点，不为drivingframework新名加recipe；仅finitequality/control取舍，不授安全。

## 21978 CxMP: A Linguistic Minimal-Pair Benchmark for Evaluating Constructional Understanding in Language Models — 2+1+2=5

[v1](https://arxiv.org/html/2602.21978v1)必要49–60/63–71/77–98/122–127。9constructions用语义plausible/implausible续句pair、name/noun/Name+alphabet和entityswap控制词汇/位置；GPT5生成+自己过滤到43k，被modelconfirmed集非全语义oracle。896items×3nativeannotators96.65%majority/83.59%allagree，但Conative Table3[125]67.86/44.64，不能把整体保证搬每construction。CLMlengthnormalizedlogp vsMLMpseudologlikelihood，GPT5只能promptchoice不是真logp同协议；大model/data/objective不同data/budget不因果配对。

关键有限controlledlearningcurve：原79 OLMo2 7/13B对应tokencheckpoint、BLiMP与CxMP同likelihood读出；82 BLiMP约50Btoken达80%后1–2point，而CxMP10B到后期持续增长，**formalacceptability不认证formmeaning**。71sameLlama3.1 base/instruct标准argumentstructure改善但Let-alone/CC退；86entityswap后仍选同name是诊断，非读出了所有内部heuristics。98四construction换Wuggywug词分下降但abovechance，determiners/inflection/形态残留，不能认证纯句法或无lexical任何信息。语言只English且构造sentence可自然度变，generationfilter/human/query成本、硬件/精度/batch完整不全；不是新benchmark条目本身准入。

actualWORLDVIEW-LLM-INTELLIGENCE Ch8 37–51把grammar/semantics都列为预测可压缩结构，没有明确两种能力的**学习时间/行为验收不相互代签**。拟PRE其“从表面统计到可复用结构”后单窄段：samecheckpoint分别formalacceptability与constructionmeaning、meaning/entityswap读出分账，metric/generator/word控制边界及成本/原likelihood基线，不扩传统语言学章；若现书具体论点足承载请Existing。未授新scaling律/语言普遍机制。

## 21997 Enhancing LLM-Based Test Generation by Eliminating Covered Code — 2+2+2=6

[v1](https://arxiv.org/html/2602.21997v1)必要28–53/58–68/75–86。AST取内外依赖外部定义LLMsummary；实际coverage结果定义uncovered，**每轮从原source重新**双向CFG-BFS保未覆盖及路径相关节点，修branch形成temporarypromptslice、清history后再generate。Originalsource不被改写，所有新tests执行**originalfile**，不是把删代码版本通过当完成。39原文：“All previously generated tests … coverage … original Python file”；52明确slice可能不保syntax/programlogic，conditionalProposition49依赖soundCFG/allneededdependencies/semanticsrewrite，不照抄为一般Python行为preservation；有限prompt干预/实测可保，非centralDisputed整个empirical。

9projects/123complexfunctions CC>10,length>50，各refsha给定；GPT4o T1/output8096/dialogue5round，Pynguin100iterations，CUT/HITS Java→Python自己适配，TELPA无公开实现自己重构，端到端budget不匹配。Table2[75]Avgcoverage42.21vsCUT24.98/TELPA32.72/HITS31.67/Pynguin5.76；dataclasses24.27<CUT25.12、pytutils34.87<TELPA41.28。Table3[80]pass37.69vsPynguin65.29（Pynguin很多0tests/N/A分母），coverage不测试oracle充分；mimesiscoverage78.82但pass24.45。Table4[83]fiveprojects w/oElimination45.49→30.40/w/oIteration16.22；cookiecutter42.62与main47.28不同表口径不合并。费用未完整call/token/host/hardware/precision/variance，baseline改造不要泛化比较。

actualPLATFORM-EVALUATION-SYSTEM Ch66 371–395 testrevision/requirements/coverage与executionevidence原语已有；窄差额是**coverage驱动改变给LLM的context，但效用验收继续绑定未改originalsource**。拟PRE regression段一小段，不推演正式Pythonslice等价：originalcode/coverage支持/slice/summary身份、所有test回原源执行，coverage与pass/语义oracle/总budget分开，CFG+LLMcalls成本与fullcontext/原regression回退。Agentworkflow不重复制，authorrealstepclosedloop足有限采用。

## 22010 World Guidance: World Modeling in Condition Space for Action Generation — 2+2+2=6

[v1](https://arxiv.org/html/2602.22010v1)必要25–47/58–73/85–110/125/131–136。Stage1frozenDINO+Wan/SigLIP futurefeatures→trainableQformer lowdimcondition，每DiTblock与currentz crossattn指导actionflow。Stage2冻结futureencoder，以cosinealignment训练currentVLMqueries预测futurecondition，**actionhead只读currentz，不读预测condition**（40），未来只auxsupervision，不把conditionalfactorizationEq1叫deployworldrollout。Deterministicdynamics假设不使两个marginal losses自动等jointdistribution，predictionproxy非control-sufficientstate证书；采用有限表征分工不认证理论等价。

Table8[105]matchedvanilla150ksteps vs100kfutureguided+50kco-train、same30epochfine：P&P45→60/Fold40→60，no-cotrain45/30；no-cotrain/Fold低vanilla，futuretrainprivileged不总益。Table9[109]unannotatedhumanstage2 P&P60→70，但Fold60→50/OODlight35→30；有220hannotatedhuman改变condition支持/额外budget，不称humanlabels无须普遍迁移。GoogleTable3 dino69.5>defaultdinosiglip69.4/Drawer dino56<62.5；受限不同feature/task，不能全归encoder因果。realUR5/Robotiq/D435/4090、20matchedrandomtrials/3tasks，predict16执行8，50/100/200demos，precision/SLO/repetitionCI未全，Gaussian?无需另proof。Encoder/Qformer/trainfuture/loss/cost非免费；actionauthority真实controller。

拟具体Existing MULTIMODAL-EMBODIED-VLA Ch26 actual336/360–377：future只trainprivilege或latent接口，jointfutureloss非部署因果使用/controlcertificate、component/objective/ID-OOD反側分账与currentfreshness/真实controller。当前auxcondition与预测未来video的不同成本已有三分支清晰承载，有限methodsetup不造新worldmodels小节；若root认为“预测condition只loss而notheadinput”真实gap，最多原future-to-action诊断一窄句，不收理论equivalence保证。
