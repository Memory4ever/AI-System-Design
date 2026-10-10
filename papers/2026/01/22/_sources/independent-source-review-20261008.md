# 2026-01-22 增量候选：非作者必要原证复核

复核者：jan22_source_review（非报告作者）。本次仅处理作者最短导航的26普通Only、4中心争议、3代表关闭，共33项；12303/11778/12193及9项Books PRE/POST由root负责，不重复申请。日期/题摘校准复用root本日结果，不重算旧67项、原窗口或分数。使用当前研究/Report合同与daily-research-closure技能；正文只读拟采用窄命题的必要方法、关键评价和直接反侧，不将文件取得、题摘或旧完成标签计为深审，不遍历附件或新增来源池。

结论：**26项普通Only窄命题可支持；4项中心争议的隔离边界可支持（不是争议Evidence通过）；12680/13437关闭可支持；13137原关闭理由不通过，建议重开为局部负面Only。** 此外12901/13143/12468/12962摘要有具体措辞/顺序需纠正，见下。全部指定33项已实际读必要原证；不是整日报DAY、Coverage、Books或全量关闭项验收。

## 实际读到的位置与判断

以下短名均为本目录原件：`12346`/`12359`为`supplement-20261008-12346.txt`/`supplement-20261008-12359.txt`；`min4`/`theory3`/`motion3`/`system3`/`repr3`/`audio3`/`extra3`/`feedback3`为`supplement-20261008-<短名>.txt`；`eval3`/`repr_more3`/`align3`为`supplement-<短名>.txt`；完整补源ID为`supplement-2601.<ID>v1.txt`。行号是保留文本中的实际物理行，不是PDF页码。仅采用以下已实际核过的窄证据，不为作者较长摘要中未逐个核验的额外数字授权。

| ID | 实际必要原证 | 非作者判断及直接限制 |
| --- | --- | --- |
| 12346 | 12346:85–121、477–506（§4.2/4.3、§5.1、judge-swap） | Only支持：报告综合、claim–URL可访问/支持与视觉对应分账；同140报告judge替换使各轴漂移而总均值相消，不证明排名或真值稳定。 |
| 12359 | 12359:70–108、139–180（§4、§5/6） | 安全必要核心已核；Only支持paired clean/injected drift与阈值条件。编码器曾task FT且须clean counterpart，不是无参照zero-shot；FPR cap3%下Llama实报5.5%，不授部署保证。SBERT数字及time冲突不能改为正面保证。 |
| 12594 | min4:26–33、184–204、260–262、384–385（§2.1/2.2、设置、消融） | Only支持varlen packing/local-global attention与EMA masked objectives的局部分支；CAP式未log不采用，109M规模不单独构成准入，未匹配算力消融不授通用归因。 |
| 12731 | theory3:855–875、941–963（§3、§4、Limitations） | Only支持early cross-language/late in-language probe差额；human IRT不是模型真实难度，unseen split选λ/层存在选择偏差，原文也明确probe不授causal作用。 |
| 12761 | motion3:93–106、219–230、267–271（§3.2/§4） | Only支持同构U-Net motion residual first-step feature迁移；synthetic六motion/定点feature选择、EPE退步和qualitative ablation，不泛化为任意身体/控制器或全pipeline效率。 |
| 12894 | motion3:374–386、420–428、663–671、749–756（§2.2/2.3、§3.2/3.3） | Only支持observation-conditioned pruner与同类block共享zigzag cache；受训pruner不是零样本，不授lossless/通用生产速度；不同采样步数baseline不等成本。 |
| 12901 | 12901v1:135–180、202–229、382–415（§4.2/4.5、§5） | Only支持闭环RFT的context/ref-conditioned Beta guidance；uniform diversity最高却性能最差反驳“加噪越多越好”。**冻结的是reference DiT/IL prior，不是受RFT目标planner本身**；§4.2明确无地图/车辆碰撞硬约束，不授安全闭环。 |
| 12917 | system3:695–723、787–797、825–833、891–910（Alg1、DTC、设置、§5） | Only支持public-cloud BP guided perturbation与client ZOO纠正的通信/资源分支；BP、广播、INT4→FP16与解压非免费；质量主要BERT，Llama侧内存/传输，不把条件隐藏当实测zero overhead。 |
| 12925 | 12925v1:57–101、172–176、247–270、293–321（未来feature、设置、RQ4–6） | Only支持two-observation→next feature与mid injection；未来GT只训练监督且非action-conditioned WM。Top5-checkpoint选择有乐观偏差，mid非每task最好；epsilonCons与feature-MSE式不采用。 |
| 13143 | system3:368–390、497–515、551–552（FastAV、设置、结论） | Only支持离线100非test rollout校准固定删尾与在线lastQ×K fine prune；**在线评分针对remaining tokens，不只音频**。延迟是single-token forward，不能授E2E；不把在线无full map改写为从不读full map。 |
| 14210 | repr3:941–963、1006–1027、1121–1142、1188–1194（方法、main/OOD、限制） | Only支持query hidden-state detector与answer-conditioned detector分账；answer更强而10/12 headline不直接授question-only，MMLU反侧/短single-turn限制保留，AUROC不授校准/真实confidence。 |
| 12555 | repr3:58–91、132–140、217–236（§3/4.1/5/6） | Only支持same-fact direct/indirect mediated recall与name/transliteration控制；3ICL/10token/prefixgold协议及heterogeneous name影响限定，不把Infini-gram过滤当所有训练数据未见或普遍因果定位。 |
| 11995 | audio3:69–109、372–379（ILI/LIR、设置、§6） | Only支持teacher-logit dependency graph→student sampling/soft LIR；2C graph与C索引不补造完整算法。作者§6明确不作causal claim且依赖teacher quality、small class sets，不授图因果或大规模可迁移。 |
| 12146 | extra3:52–82、802–810、832–839（§III、结果、validity） | Only支持compiler反馈的编译成功与语义/功能正确分责；agent5尝试对baseline1次，原文明说未测functional/runtime。不把BLEU/ROUGE/CodeBERT分数当程序正确性。 |
| 12360 | extra3:1030–1049、1069–1088、1337–1363、1370–1379（Group/instantiation、Alg1、coverage） | Only支持semantic feature groups、实例化与coverage feedback；提升promotion是整组不是单feature因果。LLVM unique7796<7919直接反对全面优胜，Jaccard/不同union population不授普遍创新覆盖。 |
| 12468 | extra3:1648–1656、1666–1710、1925–1930、2065–2066（DCAC/Alg1、setup、cache反侧） | Only支持高entropy predicted-class FIFO cache与当前校准接口；**先raw预测p/entropy→入cache→校准当前预测**，不要写成raw预测前先入cache。D-Out不匹配、C-Out污染、empty warmup不稳定与synthetic shuffled stream边界保留。 |
| 12491 | feedback3:895–920、931–945、1223–1226（VASTU构造、models、FPR/FNR） | Only支持community-score proxy下prompt conservatism/high FN与FT/prompt局部差额；vote不是通用质量、人群规范真值；0.8/0.2 stratified、model/data预算不同，不授causal community norm或公平同预算优势。 |
| 12436 | audio3:434–482、620–640（purification/fusion、loss、§3.3） | Only支持clean-mel L1/perceptual L2与fusion bottleneck的局部取舍；-5dB babble特定token count/Whisper改善但训练更慢，视频overlap条件非通用mask-free安全表示。 |
| 13669 | eval3:70–108、144–148、282–289、299–321、331–335（task/contracts、vote估计、设置/限制） | Only支持point mode/distribution JSD/judge generation分责与community profile条件；net vote+post-ratio prior不识别真比例，long-tail与train-vs-sample不授人口意见/同预算因果。 |
| 13300 | eval3:473–491、712–766、851–925、970–986（OI定义、ASR、defense、position） | 安全受影响必要核心已核，Only支持固定q/gold的option interference。ASR原答对后任何错误含formaterror，不只选E；DPO/PPO MMLU ASR高于base及位置swap反侧保留，不授任意推理劫持/通用防御。 |
| 13886 | repr_more3:111–188、734–740（§4各objective、setup、scaling反侧） | Only支持global/SSL/pseudo grounding/depth联合监督的条件；负KL式不采用；teacher/data/compute未matched且>1B seen时correspondence下降，不把成熟模块组合升级独立causal全任务优势。 |
| 12890 | repr_more3:1761–1783、1840–1846、2532–2571（GNN gate、设置、K预算） | 安全必要核心已核；Only支持flagged package→LLM subgraph的有限预算接口，§4.5.2明确highest-K可以独立支持窄命题；GNN FN无回访，K30/50更多token却accuracy/benign recall退步，不授安全完备性；不采用Eq2/11含糊selector。 |
| 12962 | align3:108–173、543–576、627–630（persona effect/CDF、设置/schedule、限制） | Only支持controlled persona edits/CDF effect matching；ignorability是作者假定而非人类causal identification。**实际schedule epoch1 anchor→epoch2 effect**（573–576），删去导航及README“CDF再anchor”反序措辞；不冒称同步blend。 |
| 12758 | align3:719–752、773–795、932–960、982–1004、1036–1054（top6、modes、fixed比较、人审/限制） | Only支持context value selector/modes的有限协议；Top6 vs fixed10非matched，Gemma coverage/Steer退步，人审100且两annotator为作者、κ.471，English/ontology限制，不授独立人群校准或全域普遍优势。 |
| 13612 | 13612v1:35–62、96–113、231–234、278–303（threat/model、设置、outdoor/defense） | 安全受影响必要核心已核，Only支持外部文本通道到action planner的风险切片；ASR5δSPL、outdoor任意偏离算fail、simple reminder局部下降，surrogate matching/训练100与search预算限制，不授物理实机或所有blackbox可迁移攻击保证。 |
| 12591 | audio3:700–782、871–885（soft targets、训练、encoder/grid反侧） | Only支持intra-modal soft target CLAP训练取舍；冻结audio/固定5s与learnable text条件，no encoder dominates；setupγ.1/β.5与selectedγ.5/β.1不一致不抹除，grid选点不授独立test最优。 |
| 12580 | repr_more3:969–990、1030–1047、1343–1380、1658–1681（validation、Thm5.2、simulation/global barrier） | 中心一致性隔离通过：valid每delta不推出valid联合状态，证明少兼容merge前提；250scripted symbolic agents/globaltick waitall不证明无协调真正异步正确性。只保留原文主张/冲突，不授positive Evidence，协议/证明澄清后定点重开。 |
| 14000 | motion3:854–866、1150–1209（条件/Thm1、limits/proof） | 中心无损symmetrization保证隔离通过：每旋转policy/function pair最优，不能因occupancy convex就推平均最优；fixed f linear不意味着max-f后的目标linear或共享f。不得自修定理，明确group-invariance条件与成本，证明澄清后重开。 |
| 12639 | feedback3:717–808（objective Eq1–6、Table1、safety解释） | 安全中心因果隔离通过：min task−λKL与约束说法冲突，DPO无ref、ORPO非odds且不同control/pref数据；GSM8K KL11.5>SFT8.5不支持一致更安全。保留双方，不授objective安全因果；精确objective/训练协议澄清后重开。 |
| 12879 | HAGD-exact-v1:361–398、510–523、615–738、759–769（Thm1、TableII/V/VI、limits） | 复杂度/效率中心隔离通过：层级启发式决策与exhaustive不同搜索空间，无完整性/最优前提；TableV noHierarchy Time0.3×方向与正文冲突，II28400s与VI28.4h未给相同协议。PDF已可读不是访问hold；不会猜代码/修公式。 |
| 12680 | min4:453–483、491–498、610–617（meta算法、setup/results） | 关闭支持：所示每query变distractor/toolset训练，无独立inner/outer新工具heldout机制；MTA部分FT反退但未形成可修正长期独立机制，不能仅凭meta或new-tool标签收录。 |
| 13437 | eval3:1403–1420、1426–1429（OSLD方法、baseline与限制） | 关闭支持：energy/CLS clustering/TFIDF/40% retrain，主要train-vs-frozen扩大class空间比较与组合benchmark，未控出独立机制/反证，不以低资源/小模型/未写Books排除。 |
| 13137 | align3:1108–1114、1144–1150、1264–1270、1526–1531（训练/数据/评价、ZBIW错误分析） | **原关闭不通过，写回后新增Only通过**：1528原文明确“value consistency但time/location factual errors”，是实际本地负面评价边界，不只成熟模块标签。只采作者局部错误分析以区分normative consistency与事实正确性；不采用该rubric作truth、不独立裁定历史政治事实/因果，不保证安全或泛化。174 bilingual rubric与Qwen judge一致性非独立事实验收。 |

## 对作者包的必要纠正

1. 13137由关闭重开为局部负面Only；理由是已读评价反例，而非改配额。由报告作者/root决定本新增项的评分并同步候选/关闭分母，旧67项不动。可以沿5–6标准审阅，当前必要方法、evaluator和直接错误分析足够支持上述窄命题；不作Books长期差额授权。
2. 12901冻结reference DiT/IL prior，不是fine-tuned DiT；13143在线lastQ×K对remaining tokens，不仅音频；12468raw预测在cache update前，当前校准在update后；12962训练顺序只保留anchor→effect，删反序表述。这四项不改变Only处置/原评分。
3. 12680/13437关闭通过的是具体证据缺少独立长期机制/修正，不采用“模块成熟所以必关”或“没写Books所以关”通用理由。13137展示局部负面反例可以独立准入；未形成其余关闭集合共同误判，不扩无关池。

## 定点写回复核

已实际读作者当前README及supplement中的五项写回：12901冻结ReferenceDiT/IL prior而目标仍RFT；13143对remaining tokens在线评分；12468raw预测→门限入cache→校准当前raw；12962epoch1 anchor→epoch2 effect。这四处必要纠正均已落实，窄命题Only处置不变。

13137实际补读1144–1150的数据/模型定位，连同上表方法、评价及1528直接反侧，支持作者改判的1+2+2=5标准Only。当前候选表、§4及过程记录均限定为作者单子域定性反例，排除政治立场、事实独立裁决、知识遗忘/规模因果与普遍安全优势；此边界和未改Books处置通过。作者可将“仍待reviewer回执”更新为本回执。

**本分工终结论：33/33必要原证已核，修正后PASS（27项窄Only、4项中心争议终态隔离、2项代表关闭）；争议不是positive Evidence。** 不为摘要中的额外未逐个核验数字、其余关闭项、root所有项、Coverage或整日DAY授通过。

当前文件是本日短审查结果，不是新永久账本；整日验收仍由root负责。未改Books、README、LEARNING_STATE，不stage、commit、push。
