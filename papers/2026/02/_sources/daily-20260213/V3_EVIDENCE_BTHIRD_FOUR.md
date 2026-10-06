# 本日B必要证据：10556 / 10560 / 10564 / 10568

精确v1、准入已独立校准；四项日期均属于已核119包络。root已实际核本组必要笔记与10556/10560原源、owner PRE及正文POST；两项整合完成，10564仅报告；10568对现有专门unlearning正文比较后的仅报告判断通过。不授日级完成，不把完整附件保存/读取视为验收。

## [LAP](https://arxiv.org/html/2602.10556v1)

5（2+1+2），若以下具体gap成立则受影响深入。§3.1–3.4 deterministic language-action是end-effector chunk的net translation/rotation；坐标+x forward/+y left/+z up、Euler右手，50%base/50%end-effector frame并把frame名放prompt。实际幅度整数cm，不采用“任意精度”宣传；net displacement不能保留chunk内部路径。VLM CE监督该低频语言表示；动作expert用flow、cross-attention，raw动作与语言动作互相不可见，隔断expert→VLM梯度。部署不AR生成语言动作，只由continuous expert执行，因此不是把自然语言变为actuator指令。

OXE/MolmoAct混合训练，原16M明确是shuffle buffer size，不是dataset大小；255bins proprio/固定q1/q99归一、PaliGemma3B；64 TPUv6e、B2048、15kstep约10h/0.65epoch、LR1e−4、warm5k、224²最多2图，部署RTX4090 25Hz。对照replicated π0/π0.5同backbone/data，区别VLM动作监督而非新controller架构。三unseen单臂Franka/YAM/Kinova加seenDROID、五类任务各两个变体各20trial/95%CI，不能授所有embodiment零适配。hard task仍需finetune、Oracle最终略高；§5明确高频/极高精度和bimanual未评。t-SNE重叠不证明因果或通用无损表示；训练precision、部署batch/SLO未披露，不将15pt或30pt描述混为总体定律。

拟Ch26差额：现135–177承载VLM/controller分工、离散codec/continuous policy，但没有把“训练用chunk净位移的frame-tagged语言监督”与“部署用连续flow执行”分开。可窄融这一训练/执行接口及chunk路径/精度失真，不授语言动作直接控制或泛化安全。原源：V3_BTHIRD_METHOD_0.txt Source120–161/205–245；V3_BTHIRD_CLOSE.txt Source262–292（必要限制已实际补读）。邻章/正式Books上下文尚待写前实际读，未写。

## [GRU-Mem](https://arxiv.org/pdf/2602.10560v1)

5（2+1+2），标准并对可能memory机制gap定点深入。精确v1 HTML404，PDF已恢复完整，实际render读印刷p5/6。memory agent同一步产生candidate memory、update gate和exit gate；update false采用旧memory而discard candidate，不能自动宣称省掉所有候选生成计算。exit true才break扫描并交answerer。结构化think/check/update/next均生成；两gate不是真实证据充分性的保证。

§3.2/p6–7：update奖励需GT判该chunk是否含所需evidence，exit奖励需GT最后必要evidence turn，早退−.75/晚退−.5/正确0；同轨迹outcome与turn-local centered update advantage相加，不是无需答案/证据标注，也不授因果credit。训练exit始终启用，部署global-question可关闭；p11限制只QA，额外reward更不稳定、需更低off-policy与更长收敛。p16 AppendixB实际核：chunk5000/maxprompt8192/response2048、LR1e−6/clip.2、B128/N16/minibatch128、trainT1 topP1、valT1 topP.7、warmup20、按validation reward收敛停；eval 8GPU node但具体型号/precision/concurrency/SLO ND，不能把400%当普适E2E。

Table1/p8直接反侧：7B平均MemAgent76.07、UG无exit75.59、UG+exit76.37；3B则63.87/69.04/65.33（加exit退步），7B multi-question UG96.43 vs Mem88.37、exit84.12。Multi-value全局收集不适合early exit。速度、memory长度需与具体任务质量一同核；无训总token/compute匹配保证。

拟Ch77差额：现151–175有outcome/local reward/hold与credit分责，没有将chunk evidence更新与“已读到最后必要证据”的退出分两项gate及两个GT条件。若长期gap成立只融训练标签可用、candidate已生成、global tasks回退无exit和3B/MQ质量反侧，不把learned gate授事实权威。原源：V3_BTHIRD_NEXT_1.txt、V3_BTHIRD_LAST_2.txt PDF Source190–425；V3_BTHIRD_METHOD_1.txt完整PDF定位；V3_BTHIRD_PDF_LIMITS_RAW.txt印刷p11；V3_BTHIRD_PDF_B_RAW.txt印刷p16。原PDF只取必要方法/评价页，不读prompt/cases。

## [SplitCom](https://arxiv.org/html/2602.10564v1)

6（2+2+2），标准完成拟仅报告。§III样本ID按epoch缓存activation：sender投影比较cos(current,cached)>threshold才跳过，server复用旧完整activation，上传时双方更新cache。旧activation与新模型不天然相同，cos忽略范数也不给gradient-error bound；正文footnote实际用homogeneous cut。BBC依validation PPL调整阈值，DDPG收益同时量loss/bytes；downlink/Ushape是额外gradient cache方案，不混成全部固定配置。

GPT2small117m与XL1.5B、10 IID client、三NLG集合E2E/DART/WebNLG，smallrank8α4/XLrank24α4、标准前3layer，B8len512/AdamW/drop.1/clip1、model FP16但activation/gradient精度不是同一声明，50epoch与10epoch不能跨规模直接比较。4 RTX4090 server+10JetsonOrinNX8GB、gRPC1.69/PT2.4.1/Python3.8.10；实际网络bandwidth/生产SLO ND。INT8是额外baseline variant，不是所有主结果量化。Ushape另20/50epoch与不同LR/interface θ，不合并协议。

TableIV直接质量反侧：标准E2E XL fixed uplink10%和7.62h vs24.68h，但BLEU69.4<70.7；small DDPG69<71.7；Ushape small WebNLG52.8<68.7。只报uplink百分比不能称总通信降90%，不把阈值复用授恢复一致性/隐私。有限IID、模型与任务质量损伤、无误差界/故障恢复验证，不能把该cache policy转为一般训练正确性合同；本篇的确切质量/流量取舍保留报告，现Ch36一般state/completion语义不需为模型化身份要求造diff。原源：V3_BTHIRD_METHOD_2.txt Source91–150/230–266；V3_BTHIRD_LAST_3.txt Source267–326；V3_BTHIRD_CLOSE.txt Source327–374及初始TableIV。不因Books仅报告降分。

## [K-FADE](https://arxiv.org/html/2602.10568v1)

6（2+2+2），安全反侧受影响深入。II-B/C用retain输出KL的局部second-order approximation作curvature约束，forget CE ascent方向经damped GN/Fisher precondition；KFAC假设block及activation/backprop factor独立，EKFAC另retain pass。步长小/本地Taylor与非线性近似retrieval假设不能给删除保证；Eq4负号与ascent/算法不一致、return-index局部错误不照抄。每层factor O(d²+m²)+EK dm、求逆/分解时间并非模型规模全线性。

WMDP Zephyr7Bβ、Wikitext retain/Bio-Cyber population、MMLU/MTBench GPT4/Alpaca specificity；Bio/Cyber30.1/27.7不是对ELM29.8/27.3绝对更强。TOFU Llama2-7B fictionalauthor5/10%，ForgetQuality是KS p-value，不是delete概率或分布相同的证明；retain九metrics harmonic utility。单KFAC ascent/damp1e−8/step2.5e−3–1.1e−2、2H10080GB fit；Phi1.5 ablation fullprecision单H100、KFAC/EKFAC比diagonal更佳但speed/utility tradeoff，完整EKFAC fit约retrain成本，不能只量cache后单步。TableIII忘记人口输出仍有fluency损伤。

IV-D直接反侧：Zephyr7Bβ全参数AdamW B8 LR1e−5仅200step在Wikitext/retain/少量forget数据就恢复几乎全部Bio能力；所有测试方法不抗openweight finetune。仅provider仍控制weights时重加旧update方向能恢复部分suppression；这不是用户权重已不可改、永久遗忘或DP式保证。§VI明确无DP式unlearning保证/有限TOFU empiricalapprox，不授一般重训等价。HW524的8H100 BF16/FP32 factors是另Hessian-scale实验，不并成TOFU配置。

仅报告（原拟gap撤销，不改准入评分）：实际对照Ch72 §unlearning正文2583–2612，2597承载checkpoint/data/parameterization/damping绑定的curvature artifact与继续训练失效，2599承载GGN/diagonal/LoRA近似、成本及非重训等价，2601–2603保留weight restore与继续finetune反攻。KFAC/EKFAC retain-output KL是这一近似branch的具体实例；provider-controlled重施更新不新增open-weight保证，故不制造Books diff，也不称现有正文已包含该篇精确公式。原源：V3_BTHIRD_METHOD_3.txt Source78–155/164–203；V3_BTHIRD_LAST_3.txt Source226–275；V3_BTHIRD_CLOSE.txt Source289–335；V3_BTHIRD_KFADE_TAIL.txt Source323–386。root实际owner/core复核通过；未运行代码/未复现，不待可选artifact。
