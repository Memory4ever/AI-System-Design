# Loop / MoST / Queue：必要采用范围待 root 核

三项root实际完整AB已准入；各 exact-v1-primary.txt 已缓存。非全附件队列，未核artifact/复现。normalSubmitted+正常公告且无先行正文条件公开范围，下界BJTJan16 09，上界registered秒+1完全落窗。

## 10242 Loop as a Bridge（6=2+2+2，设计反证深入）

actual §2.4–4.2 L80–141。必要§3setup/result L123–131与§4injection L134–141：Ouro1.4/2.6B/reasoning各1–8loop，80%depth linearprobes；BeaverTailstrain8k+8k/test1k+1k；DeepMath Qwen235B生成每题10答案，40–60%题筛后train8k+8k/test2k+2k。probe训练与文本judge各自测准确率/F1，gap缩小同时线性probe下降，不能写“内部knowledge被证明丢失”。50concept对100background均值、每concept64trials，跨extract/injectloop matrix；Qwen235Bjudge、real-noinjection detection与识别主要final-loop，不认定所有loop无introspection/内部语义因果。

未披露probe超参/seed/hardware/precision/总预算及data按题独立split；balancedpopulation不认证部署risk，文本prompt与probe接口不同，无非线性probe控制不能授representationceiling。§2 supremum hierarchy需要probe emulates languagehead/策略集合假设，不将有限线性probe当supremum；Claim1重解一致性也不自动证明verifier accuracy上界，理论不采用。图的作者局部trend可支持分账，不造不可读的数值/CI。

actualowner `PLATFORM-EVALUATION-SYSTEM` Ch66 L2064–2074已有可解码≠纠错authority/独立干预，但没有两项分数gap缩小可因probe下降而“向下对齐”的检查。拟该heading两段之前或既有probe机制之后两短段：joint报告selfverification/probe两个绝对量，loop/层/监督人口绑定，不由gap得分改称latentknowledge/自省；额外probe/injection/judge成本、unknown与直接行为验收退路邻接。Ch17只拥有recurrence计算，非此评价owner。

日期 SubmittedJan15T10:01:21Z、UpdatedJan16T01:34:03Z、created02:50:40Z/registered02:50:41Z → BJTJan16[09:00:00,10:50:42)。

## 10272 MoST（6=2+2+2，模态路由具体gap深入）

actual §3 L94–167/Algorithm1：frozenHuBERT连续输入→projection，输出仍预测HuBERTtokens/HifiGAN+speaker，不采“完全continuouswaveform无离散”的headline。all-expertsoftmax→typedmodalitymask→TopK权重sum（未写mask后renormalize，不自补）只用对应组；另parallelsharedMLP处理所有tokens并相加。modalityindicator决定eligibility，不是由routerentropy证明语义specialization。共享MLP是否真正crossmodaltransfer须独立任务验，不由alltokens访问自然证明。

actual §4.2 L174–176、§6 L350–363、B1/B2L665–670、D1L726–732、Table2L292–346/Table5L734–767。DeepSeekv2Lite→ASR/TTS→mixedinstruction，controlledLlama3.2 3B同init；vanilla/NoShared/full同routedexpert数、10ksteps/B256，不等总参数/activecompute（shared删除即改budget），figure-onlybenefits不造exactscore/CI；正文71.18/Phi71.84与Table2MoST71.94/Phi69.00不一致，不采排行榜平均；NoShared totalbudget未match，不能说精确单因果。B1B128 vs§6B256人口不同，48A100/peakLR5e−5/WD.01/10k/warm1k/mix1:1，precision/seed/e2etime ND。D1把pretrainedexpert说成random neutral不获源码/干预支持，不采用neutralpartition/无knowledge loss。MMLU55.4低MinMo58.5，不能用多texttask分证明无forgetting（无basepaired）。

actualowner `MULTIMODAL-REPRESENTATION` Ch23 L292–296早融合及sharedattention元数据/L14representationcontract，Ch21genericload/topK不拥有modaleligibility。拟earlyfusion之后两段，typedgroupeligibility与parallelshared消费接口，加上mask/softmax/TopKbudgetidentity和source局部/混杂/原modalencoder路径退路；不大段复制genericMoE或由低entropy授专家语义。

日期SubmittedJan15T10:43:29Z、UpdatedJan16T01:36:18Z、created02:51:23Z/registered02:51:24Z→BJTJan16[09:00:00,10:51:25)。

## 10274 Queue / Optimal Reasoning-token Allocation（5=2+1+2，条件queue标准要求；必要模型/稳定域已深入）

评分纠正：原3+1+3将借用PK理论与可联想到的普遍调度认知计入新增命题。只采用task-type tokenbudget联动service二阶矩目标接口，D2重要条件机制而非已改变生产设计结论；Reach1单FIFO负载；Durability2可复用边界而非新长期认知基础。不是因发现反证降分或减少审阅，必要模型与稳定域已实际深核保持。

actual §II L116–176、IIIA L181–210必要曲率/IIIBL211–265、IIIC/D条件L266–288/312–350、IIIE L389–414、TableI L415–464/IV L465–523。只采用per-typeaccuracy与service-time拟合→Poisson/FIFO单nonpreemptive服务器M/G/1的first/secondmoment→coupledreasoningbudget objective；PK成熟公式不作为新发明。新差额是每type追加token同时改变其它请求平均等待，非单requestcost。J=alpha∑πp−E[S]−λE[S²]/(2(1−λE[S]))；确定每typeexactbudget、affine t0+cℓ、independenttypes/Poisson、concave saturatingaccuracy、ρ<1需真实满足，不覆盖continuousbatching/PD/multiGPU/preemption或tailSLO。

曲率假设/推导已定点核，**不采用**全box solver/rounding保证：Lemma2/3要求ρmax=λE[S(lmax)]<1，TableI c约.012–.014、λ=.1/lmax32768实际整boxρmax约41，不满足globalstablebox；boxprojection本身不保证stability，严格稳定域非无边界compact，不能继承“所有feasible点收敛”。integerceil/round后须重新验ρ，不能自动仍稳定；Eq41二阶矩粗界不作采用。最优性只在所定义relaxed模型内，不认证生产globaloptimum/无误预算。

IV Qwen3 8B/A10080Colab/T.1、6typesuniform/250eachbudget/3runs、10k模拟Poisson/λ.1/α30，fits数值非实际batchservingqueue，precision/promptlength/answerreserve/总prefill生成budget ND。相同fit数据选择optimal、无heldoutcalibration，长budget假设非所有taskmonotonic；uniform仅0/100/500三对照。零budget类型不是普遍无reasoning价值。需fit/probe/solver/latency外部开销，不报无条件收益。

actualowner `INFER-SCHEDULING` Ch56 L191–214已有perrequestmarginalgain/budget与metacognitivemonitor，但没将请求类别分布的service secondmoment加入thinkbudget的跨请求外部成本。拟solvability段后/长推理跨轮状态前两短段：只讲条件singleFIFO时均值/方差共同校准budget，stabilitymargin/round再验，补actualmodel/模拟限制与固定预算/admission退路；不采solver缺口或额外theorem。无需其余proof展开。

日期SubmittedJan15T10:47:11Z、UpdatedJan16T01:36:31Z、created02:51:26Z/registered02:51:27Z→BJTJan16[09:00:00,10:51:28)。
