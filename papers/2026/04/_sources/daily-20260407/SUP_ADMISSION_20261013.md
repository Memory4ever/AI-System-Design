# 04-07补充：本日准入、证据与精确停点

作者supp_apr07_author；仅补2026-04-06完整BJT自然日。当前为待root首批校准/必要Source复核的工作稿，不是日级通过。

已保存[补查前报告](baseline-before-supplement-20261013.md)。原46候选整行/原窗口冻结，连续原§4正文43031字符、SHA256 `6bbf0d441abeba61e882ade0487c3346a026b39d92d464be92ac6dc205870b69`。邻日04-06原47是有效研究，补窗与其重叠时只按具体ID/版本/event复用，不重复候选/评分/Books、不移归属。未读旧Weekly；shared Books/State/索引均未写，无锁。

## 首批准入与代表性排除校准请求

三个拟入选ID02945/03044/03098均不在原本日46或邻日04-06原47表。02945/03098原04-06 V3_REVIEW_CHECKPOINT的前分母关闭具体理由存在错误：前者因摘要未给完整运行配置而拒绝已清楚机制，后者把内部辅助reward错误要求为替代独立environment verifier。此处只定点恢复这两处共同准入问题，不推翻原47或全部旧排除。原完整题摘、精确v1正文与当前官方身份已实际读取；所见没有撤回/更正标记，JoyAI有04-08v2但不比较版本、不用v2事实回填。

日期只复用邻日[V3_DATE_RECONCILIATION](../daily-20260406/V3_DATE_RECONCILIATION.md)的02333–03231连续ID、前后边界和官方Sunday20ET公告slot组合依据。三项本次实际DataCite字段核得Updated/v1分别04-06T00:36:30、00:42:07、00:45:33Z，Submitted分别04-03；自然日推断归属04-06，不将Updated/Submitted/DOI created任一字段改名首发，不追秒级成功日志。原件`SUP_{02945,03044,03098}-{doi,v1}_20261013.raw`及同名request保存URL/HTTP200/执行14:56Z。

- **02945 MSAO**：模态保留/压缩与草稿长度、网络状态联合选择，而不是统一offload，潜在改变端云推理调度接口；拟2+2+2=6。必要exact-v1 §4.1/Eq7、§4.2/Eq8–16/Alg1、§5.1–5.4已读。MAS语义、per-request固定压缩与per-step entropy阈值分工明确，但中心收益/保证争议：§5.3.2 `128/35`总倍率3.66与`(128−35)/35`相对增幅2.66都可复算，原文improvement×和摘要1.5–2.3×的分母语义未统一，不能直接断言算术错或选一倍率外推；同Cloud-only准确率随带宽76.3→77.8只显示相同评价人口/生成/超时条件未说明，不独自证明实验无效；Alg1未展开完整拒绝校正与provisional-state rollback，不能由同tokenizer给target-law exactness；Eq15–16未提供其GP regret/EMA convergence所需假设与证明。§5.1.1实际edge RTX3090-24GB/Qwen2-VL-2B、cloud A100-40GB/Qwen2.5-VL-7B、200/300/400Mbps、RTT20ms、三runs；precision/输入输出长度/batch/concurrency/SLO均Not Disclosed。拟深入完成→争议/暂缓，中心性能和正确性不进Books；不能改低分或贡献前排除。恢复条件为作者澄清相同评价人口、吞吐分母、真正verification/rollback接口和必要保证条件。
- **03044 JoyAI-LLM Flash**：token-wise ratio与sequence平均ratio各有缺口；Eq1–5以trajectory正负log-ratio聚合base gate乘token相对聚合的residual logclip，拟2+2+2=6，深入接口。§3.3.1–3.3.3/Fig5–7核心已读；只拟保留两尺度乘法接口、非凸rollback区与额外统计/校准成本，不采用硬trust-region/单调改进/因果token credit保证。单域DAPO-Math17k→AIME24、共同verl/LR1e-6、从同SFT/DPO低entropy checkpoint开始，作者称匹配基础设施；seed数、统计区间、完整每算法token/GPU费用与base/fiber独立消融未披露，不把图中表现视通用支配。其理论原稿引2603.08239，仅本报告的明示接口/受限验证；未核该引用证明，不遍历其附件。Ch33当前704–713附近只讲GSPO与token/sequence两个独立surrogate的凸混合，未承载trajectory aggregate×signed residual接口；需root Source/PRE确认后才申请窄写。
- **03098 Self-Guide**：长程终局反馈稀疏→同policy先生成guidance条件化动作、按polarity映射±0.1/0并求和→与environment reward通过stage-dependent lambda相加，再做组advantage。Eq6保留environment outcome，绝非自评替代真值；拟2+2+2=6，深入。必要§3/Eq1–10、§4.1–4.5/T1/Fig3–6和Appendix A提示/预算已读。warmup仅guidance、ramp、full、late annealing；按step40/50/70/80固定schedule不是运行时已证reliability门。Fig5即时满reward39.7低于guidance-only49.2，晚退火56.3仅所测配置；offline32B→1.7Bguidance不稳定是分布迁移局部反侧，未证明唯一因果。Qwen3-1.7B/4B、Qwen2.5-7B-Instruct，text-only ALFWorld/ScienceWorld/WebShop、100updates、温度train1/eval.4；prompt4096/8192、response1024、episode50/30/15，GPU/precision/seed数/batch/concurrency/SLO与总额外guidance token费用Not Disclosed。不声称普遍无外部evaluator/免费densification。Ch33现有过程proxy与reference likelihood shaping，但未承载guidance用途与reward权重的独立阶段晋升/退火；root Source/PRE后才写。

代表性前分母关闭（完整题摘/核心说明实际已读）：

- [OpenAI Safety Fellowship](https://openai.com/index/introducing-openai-safety-fellowship/)官网04-06，RSS04-06T10:00Z：人才申请、导师/算力资源安排，尚待未来研究产出，没有本公告新技术命题。不评分/Books，不进入OpenAI产品文档技能。
- [Meta Alta Daily](https://ai.meta.com/blog/alta-daily-fashion-app-segment-anything/)官网04-06：已有SAM用于服装背景分割，八类别内部比较与API费用描述没有新增模型/执行机制或可核对照边界；不是SAM3.1新版本事件。范围/具体贡献前关闭，不把两千万应用规模当可比benchmark。
- [02755](https://arxiv.org/abs/2604.02755v1)：CPU/GPU异构内存处理物理仿真状态，神经代理只用其生成数据；没有大模型训练特有状态机制，科学应用按暂缓范围关闭。
- [03145](https://arxiv.org/abs/2604.03145v1)：通用K8s CPU/memory/disk/network压力的Granger关联，不测模型状态或训练/推理SLO；不能靠云平台类比准入。
- [02990 FedSQ](https://arxiv.org/abs/2604.02990v1)：冻结ReLU结构副本给CNN跨silo固定gate，局部affine refinement稳定weight averaging；未说明与Transformer/MoE或大模型训练问题的可迁移约束。不能仅因固定gate联想MoE入池。若认为该学习/优化边界直接支撑主线，需按具体机制校准，不以小实验本身拒绝。

## 本日来源发现正在进行

四组arXiv窄主题API查询按CL/LG、DC/AR/PL/OS/PF、CV/RO、AI/IR/MA分类+同义表达，submittedDate04-02T18Z～04-03T18Z仅作Sun20ET批次线索，不证明public date。实际model fetch failed、system timeout、multi/agent429；请求/14字节错误原件保留，不作空命中。一次web四主题date搜索未恢复历史结果。官方cs.DC4月页388条标题原件已恢复，**只投影02333–03231的12条标题**，一般distributed/DB/科学条目未变全篇队列；正文更深读限上述02945及三个代表性范围样本。CL复用04-05原抓2000/2532页，只投影同批相关身份标题；误以为逆序造成的一次tail恢复实际532条为更晚cross-list，不含目标批次，明确不用作本窗召回。未声称全月都筛或API/所有分类通过；待有界主题恢复或历史slice安全出口。

官方机构原件复用daily-20260405/SUP_*raw/request，已实际读本窗字段：Qwen40 extra.date04-02→04-15；Hunyuan9/9 displayPublishTime02-13→04-22T16Z（publicAt存在差异，原因未知不当first-public）；Seed papers18/243 next60 has_more=true，相关04-07T16Z diffusion→03-25机器人，夹03-31Science仅日期邻界，Blog15/95 next20，04-08T16Z→03-31T16Z；Anthropic publishedOn04-02T10:56Z→04-07T09:35Z。MiMo8 datedPaper03-13→06-29，15无日期Blog单独切片隔离；MiniMax中文03-18→04-27、英文03-18→05-26，Agent当前三篇09-19/22/10-08，不宣称旧历史无事件。Google本次web04月Blog04-03→04-08，DeepMind首屏30/265 selected03-22→04-22，Publications首屏1–15/11614只有year/venue，日级切片未恢复；Meta Research0行/publications当前首屏非时间有序，到Next止，历史切片隔离。OpenAI Research Index首屏9cards09-10～10-07/Load more，必要历史Research切片隔离。余源具体字段与停点将融入正式六部分。

## root 独立准入与第一批采用复核

**本轮实际采用层补齐：** root另实际读SIEVE §3/Alg1与4.4.1/Table2和8H100训练字段；SWAY §3.1总体比例公式；Vocabulary-bans §2.3–2.8控制/解析/compliance人口；LT-MIA §3.1–3.3、T1/T2、5.3/T3与§7。对应Ch27合成数据、Ch66旧framing到人口cue、Ch72 Min-k到adapter、Ch16准确限定后的完整新增/邻接及本人末注均实际对读，C/D/E/F/G actual POST通过；A/B实际Ch33两处/完整邻接/本人合注先已POST通过。共7真实采用，五个canonical文件，旧机制和交接保持；限定diff-check通过。后续仅作者同步本人notes实际验收身份、读回/释放，不能由本段提前授整日DAY。

MSAO终态Source实际核4.2.2/Alg1/Eq15–16、5.1.1、5.3.1/Table1及5.3.2：GP regret/EMA最优均方收敛缺必要条件，verification/rollback与匹配评价配置未闭合，中心争议安全隔离通过。不把128/35的总倍率3.66与相对增幅2.66混用，也不直接断言算术错误；带宽切片的cloud accuracy差异只能提示未说明的评价人口/生成条件，不单独证明实验无效。恢复条件保具体、仅相关证明层；不降分、贡献前排除或写Books性能/正确性保证。

root已重读当前AGENTS/适用合同与本日停点，实际完整读七项题摘（02945/03044/03098/02339/02423/02699/03199），均有具体机制或反证潜力，不以标题/章节匹配代替准入。两个错误前分母理由仅定点重开；原46及邻47同事件不重复评分/研究。root亲开两官方Blog核心全文，Safety Fellowship只有人才项目、Alta Daily为既有SAM应用与未给可比协议的内部效果，具体贡献前关闭通过；02755科学仿真及03145泛云Granger的完整官方题摘范围关闭通过。FedSQ完整题摘涉及固定选择与参数平均条件，不能仅CNN/未测Transformer排除，已有限恢复必要原文，不扩FL入口。

第一批实际必要原证：Self-Guide §3/Eq1–10及4.4–4.5反侧；FiberPO §3.3.1–2/Eq1–5和受限比较；FedSQ III-A/B/Alg1。root对读Ch33 Process-reward插点及GSPO/凸混合前后、Ch32/34交接、Ch16两层公式/扩维/activation邻接。逐字A/B/G采用范围通过：只分开guidance与reward用途、trajectory aggregate×token residual接口、input-affine与joint参数平均区别；不采用同policy真值、动态可靠性证书、普遍trust-region/因果credit或FL收敛。5x/4x是本书公式的数学推断，不冒论文定理。Ch33和Ch16窄锁已授；实际POST未发生前不计整合/日级完成。其他C/D/E/F必要Source/owner及整日仍待root实际核，不由此批预支。

## 普通待办（非受阻）

root首批准入校准；必要Source与两项owner/PRE；剩余有界发现/重复出口；本日README补查六部分、独立DAY/FINAL。三材料原文可读，不能把尚待Source/owner当受阻。无Books写入、无锁；不stage/commit/push。

## 第二批：四个CL新命名/设计反证的定点增量

只在已限定02333–03231标题切片中选此四个强机制/负侧信号，不把78CL标题变队列。实际完整题摘与精确v1必要核心正文已读。四者不在原46/邻47候选；DataCite Updated/v1分别04-06T00:00:17/00:02:22/00:20:28/00:50:04Z，Available均2026-04；同批组合依据支持04-06日级推断，不把SIEVE02-02 Submitted当公开日期，也不将它强行移二月。所见无撤回/勘误；脚本/原件`SUP_{02339,02423,02699,03199}-{v1,doi}_20261013.raw/request`已存（15:05Z）。

### 02339 SIEVE — 拟2+2+2=6，深入知识差额

§3/Alg1/Eq1–3、§4/T1–2/F2–4、A/T3–4：将context拆原子unit，base-model选coherent seed、instruction-model逆生query，再遍历全部unit核applicability，不能把生成seed直接等同最后必要context。教师读query+applicable子集产生top100 soft-target，学生不读context；decompose/verification只model判断、不具外部oracle。完整corpus与三个seed是输入，不是总训练量只有三例。Qwen3-8B不thinking，另Retail下Llama3.1/Rnj1-8B；4096合成样本33.98对oracle-query/full-context CD27.11只是所测Retail反侧，不证明过滤唯一因果；T2固定teacher-generation次数下4096×1优于512×8，1024×8反优8192×1，diversity/重复收益随regime改变。8H100、batch1×acc8/effective64、lr1e-5、ZeRO3、max16384、Retail/NBA2epoch、MTOB5epoch；precision/seed数/concurrency/SLO与完整生成/核applicability成本Not Disclosed。新差额应由`TRAIN-DATA` Ch27的Synthetic-data论证拥有query/context配对身份，不在Ch29重推已成熟CD objective；Ch27原351–361有generator/judge、learner-refresh与seed joint diversity，但没有seed与verified applicability两份支持集分离。

### 02423 SWAY — 拟2+1+2=5，深入测量反证

§3.1–3.2/S公式、§4.3.1–4.3.2、A.1/A.4及必要结果：同题保持content、变polarity/commitment/clause，S为总体reference-category生成比例的加smooth log10比，不是逐tokenlikelihood或任意item稳定性。AITA/LFQA/DebateQA每500items、六backbone、Bedrock temperature0/max1token；mitigation有额外固定10fewshots/counterfactual scaffold，不能授同token预算。三集reference只是约定stance，不是真实正确label；aggregate S≈0允许两个item相反flips抵消，不证明每itemrobust。Gemma中commitment切片反增、Haiku过度反迎合仍保；evidence responsiveness只Claude Sonnet/DebateQA、不能外推全model。硬件/precision/输入长度/batch/concurrency/SLO未披露或托管Not Disclosed；bootstrap以题为unit比条件副本独立更适当，未运行artifact。Ch66原630正反framing同类别映射与逐framing结果具体已覆盖，但尚未明确用总体stance比例比会抵消item-level flip，以及无答案真值的neutrality不授correctness。可仅在这一测量差额窄refine，具体counterfactual CoT配方仅报告，不给通用安全承诺。

### 02699 Vocabulary Bans — 拟2+1+2=5，深入具体反侧

§1.2–1.4、§2.3–2.8、T2、§3.1/3.9、§5、A必要checker说明：两结构ban、neutral filler-ban与metacognitive control构成active对照。六托管模型/130items×4temperatures-repeats（1个T0+3个T.7），max2048，seed42在provider支持处；15600计划→14482去重→13633可解析→12402firstpass→11919compliance，是不同人口。neutral+6.0pp(all-trials)对+6.7pp筛后，不把条件筛后人口合并。E-Prime retry指令从firstpass即在context、仅其能保证compliance；约束不合规/不可解析不能默认删后当自然效果。初checker29flag/17trial precision27.6%，bigram修后估>85%仍非完备；首2600Sonnet fixedorder，只排查可见drift，未排所有order混杂。activecontrol否定“特定词汇结构唯一认知重构”是所测负侧；post-hoc outputregularizer解释未证内部因果，部分任务亦退步。无GPU/precision/并发/SLO或全retry/call费用。Ch66现有paired semantic/prototype controls不覆盖新方法动机中的neutral词控制及compliance人口/expectedretry信息两层混杂；拟只窄refineactive-control与筛后estimand，不推通用禁词提高reasoning。

### 03199 LT-MIA — 拟2+2+2=6，安全深入

§3.1–3.3、§4/T1–2、§5/T3/F3–4、§7、B/C必要access与配置：fine-tuned目标和同架构pretrainedreference都必须返回full-vocabularylogits，非普通chat黑箱API。154维逐tokentarget/reference差分、logit/rank与globalstats序列由小Transformer分类，先pool成标量会损位置结构；30组合固定总18000训练时增加diversity的迁移比较和T3相同feature序列对meanpool的0.925/0.875支持这一限定sensor分支。10Transformer×3traincorpora、7heldoutTransformer+Mamba/RWKV/RecurrentGemma×4evalcorpora；不把不同family+dataset均值AUC识别为architecture不变定律。T2在.1%FPR上RecurrentGemma LT-MIA.166低于EZ-MIA.226，Mamba两者.240持平，不能沿正文“所有family显著更好”外推低FPR普勝。reference原已熟悉WikiText时AUC跌.781/.796；实际fine-tuning only，不授pretraining/RLHF、membership法律真值或关闭API无泄漏。target3epoch/batch16/lr5e-5/len128，多数TransformerLoRA16/alpha32/drop.05，非Transformer全参，单H200、~30GPUhr为作者估算；precision/seed/部署batch-concurrency/SLO未披露。Ch72原335–369有identifiability、Min-k位置权与不同access sensor，但未有“同架构reference-logit差分序列＋classifier跨family迁移不扩大access/真值权限”的具体接口。拟窄添于Min-k位置sensor后，保lowFPR反退、混合finetune与额外feature/training费用。

上述四项仍待root非作者Source/PRE，未据作者完成read标正式入选/Books通过。普通剩余是七项独核/处置、拟稿与写后、正式六部分DAY/FINAL；已读valid层不再重读。两次API恢复失败后不无限重试，必要topic/public history slice保精确外部缺口，不把其余标题变待审或全量排除。

## FedSQ定点恢复（8项中的第8项，覆盖旧EX）

root完整官方题摘校准要求定点恢复02990，CNN/未迁移Transformer不是范围门槛；本作者实际v1 III-A/B/Alg1、IV/T1及currentAB已读，原件`SUP_02990-{v1,doi}_20261013.raw/request`保存。拟2+1+2=5标准＋重要分解边界深入，已清楚具体潜力，不再列排除。其SK冻结共同pretrainedcheckpoint，各输入生成固定binarymask；QK每层z乘mask，各客户端只更新/聚合QK，存储两份权重并非trainable参数减半。原非ReLUbackbone也改用binarysurrogate，不证明保原activation函数。

原文“区域内输入affine”不能升为“所有QK参数联合线性”或“模型参数平均等函数平均”：多层权重乘积仍有cross terms。这是本作者数学边界推断，不冒作者定理。仅一个可训练linear head、其他变换与gate固定时，才有这项线性平均条件；原AlexNet仅classifier与ResNet18 block4+classifier不是同条件。10clients全参与/E1；batch64/SGD1e-2/WD1e-4、iid/Dirichletalpha.5，共同ImageNetwarmstart/central calibration schedule；T1 Alex iid68.10<68.31，ResNetDirichlet两者best都round30，正文earlier不普遍。硬件/precision/seed数量/并发/SLO/双copy前向与central calibration总费用未披露，fixedseed不等多seed统计。DataCite v1 Submitted04-03/Updated04-06字段＋同批条件仍自然日推断，不独字段定公开。

潜在Ch16唯一owner差额是“冻结gate使输入分区affine，不保证joint参数平均/优化”：原29–68 FFN两矩阵与activation解释中尚未明确这层学习边界。需要root决定窄refine是否成立；若只支持本联邦transfer受限实现，则仅报告具体方法/反退而不承诺新大模型聚合或迁移。不会借此创建FL章节或扩扫来源。

## 写前逐字草稿（PRE待非作者，不是已写Books）

已读Books适用PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE、ROADMAP与最新相关路由；Ch27原351–361/合成数据邻接与Ch26/28，Ch33原164–240/285–305/697–713与Ch32/34交接，Ch66原620–639/125–156与Ch65/67，Ch72原335–369与Ch71/73交接已实际对读。下面仅拟窄插入，没有共享锁/写入。Source均精确v1，不核代码、复现、后版差异或未用证明。

### A. Ch33 Self-Guide：紧接现有“Process reward、step verifier…”段

过程信号还可以由正在行动的同一policy生成，却先只拥有guidance权限：每轮根据已见history给正/中/负的简短自评，再据此生成动作；训练时另将这份polarity映射为有界局部值、沿trajectory求和，以阶段系数加到原environment outcome上，之后仍做同题group归一。这不是独立步骤真值或由模型接管终局验收。一个[受限分支](https://arxiv.org/html/2604.03098v1)先让guidance随原outcome训练，随后提高其辅助reward权重，末期再退火；“能指导动作”与“获准改变训练目标”是两个接口，schedule按训练step预设，并非已校准的动态可靠性证书。<!-- source-family:SF-2026-ARXIV-2604-03098 -->

这会增加guidance生成、轨迹token和非平稳reward状态，未经长度归一的polarity总和也可能随episode长短改变辅助压力。所测text-only三个环境中，立即使用满强度内部reward低于仅guidance，离线强教师guidance也不能稳定迁移；这些反侧支持保留warm-up与独立outcome，不证明唯一schedule或通用自我改进。同update数不等总生成/环境费用，硬件与训练seed未披露。自评漂移、额外成本或最终success回归时，应关闭辅助reward、保留原outcome-GRPO或可靠process verifier，不能用更密的自评分数批准部署。

### B. Ch33 FiberPO：紧接两个surrogate凸混合分支后、演化metadata总结前

两尺度也可以在ratio内部组合，而不是把两个clipped surrogates相加。一个[受限接口](https://arxiv.org/html/2604.03044v1#S3.SS3.SSS1)先分别聚合同trajectory正/负token log-ratio，以聚合gate形成共享base weight，再乘每token相对其sign-channel聚合量的gated residual；因此trajectory漂移和局部偏离分别拥有阈值。它仍消费原advantage，不由ratio残差创造token语义真值；分段gate的rollback和零输出也不是实际参数的硬trust-region或单调改进保证。<!-- source-family:SF-2026-ARXIV-2604-03044 -->

双统计、分段梯度及阈值校准增加数值与恢复状态。作者低entropycheckpoint上的有限数学RLVR比较只支持这一可审更新分支，未披露完整seed与逐方法token/GPU费用，图中相关诊断不独自归因每个gate；多域recipe又加入课程与采样改变，不能合并成算法通用支配。比值、sign分区或预算失配时，应保留原GRPO/GSPO、独立clip混合与freshness门，在同质量和完整成本下重新比较。

### C. Ch27 SIEVE：Synthetic-data起始段后、learner-refresh例前

当要学习的是一份自然语言规则corpus，合成query的seed与最终适用context也要分开：先拆出原子unit、选coherent seed逆生成query，再回查全部unit，形成仅供该query使用的子集；生成seed不保证包含所有必要规则，也可能含无关规则。模型的applicability判断仍是可错过滤器，保留unit/seed/query/核后子集与teacher条件的lineage，才可交第29章的context-distillation目标；不能把同模型teacher或三个query种子说成没有监督。<!-- source-family:SF-2026-ARXIV-2604-02339 -->

[有限context-learning对照](https://arxiv.org/html/2604.02339v1#S3)提供这种配对数据的局部支持，而非三例完成全部训练：实际生成数千query、执行子集核验与teacher前向，再训练student。固定teacher-generation次数下，多样query与重复rollout的收益会随规模反转，不能永远优先一侧；规则遗漏、model过滤偏差与跨chunk依赖继续存在。分解/核验费用与8H100训练都计入，原少域结果不授真实任务的持久可靠。applicability无法复查或heldout退步时，保留完整可信context、固定合成配方与独立oracle，不凭更少提示tokens认证知识完整。

### D. Ch66 SWAY：现有正/负framing映射段后

用正反nudge下的总体reference-category比例构造比值时，还须保留逐item的配对transition：总体差接近零，可能是稳定，也可能由方向相反的flips抵消；它更不证明答案真实正确。[受限stance诊断](https://arxiv.org/html/2604.02423v1#S3)在无独立正确标签的意见/偏好题上测framing敏感性，额外counterfactual scaffold是干预而非score本身。应同时区分reference标签约定、item-level变化与对新证据的响应，不能用低aggregate sensitivity替代这三个对象。<!-- source-family:SF-2026-ARXIV-2604-02423 -->

配对生成、模板与额外fewshots都有成本；固定单token/temperature0与少量model/题域只支持该评价协议，部分干预仍过度反迎合或放大敏感性，单模型的evidence probe不能替全域验收。nudge语义、映射或正确性依据不明时，保留逐条件原始结果、独立label与人工抽核，不由counterfactual措辞授内部因果或普遍安全。

### E. Ch66 Vocabulary-control：与配对control的测量合同相邻

若某prompt干预被解释为特定认知机制，比较对象不能只有无约束baseline；还应构造含相近监测负担、却删除所声称关键成分的active control。一个[受限禁词复核](https://arxiv.org/html/2604.02699v1#S2)以中性词约束和metacognitive提示对照结构性禁词，说明总体accuracy改善不能唯一归给被禁词汇的认知角色；另一种“输出regularizer”解释仍是事后假说，不由反驳旧解释自动证明。<!-- source-family:SF-2026-ARXIV-2604-02699 -->

control又必须核人口和上下文：只有一侧知道会被重试、按约束compliance或可解析性事后筛选，都会改变实际estimand，first-pass标签不能消除prompt里的retry预期。应分别保存全部请求、解析/违规结果、条件筛后分母与checker误判，而非将重复API输出当独立训练seed。原有限任务有退步、checker小样本与部分固定顺序限制，调用、重试及判分费用也另计；无法匹配控制或核人口时，保留未筛结果与独立人工审校，不从选择后的更高分签发机制因果。

### F. Ch72 LT-MIA：Min-k位置分数后、gradient-adapter探针前

位置结构还可以由受监督的sequence sensor学习，而不是先把token分数pool成标量：同时读取fine-tuned目标与其同架构pretrainedreference的完整logits，形成逐token差分/rank/分布统计序列，再用多model–dataset组合训练分类器。一个[受限迁移审计](https://arxiv.org/html/2604.03199v1#S3)支持把这些差分与顺序作为sensor身份；跨family复用分类器不移除每个目标自身的reference访问，也不把普通chat返回升级为full-logit接口。<!-- source-family:SF-2026-ARXIV-2604-03199 -->

该路径增加特征读取、参考前向与classifier训练成本，只验fine-tuning的已知membership人口，不认证pretraining/RLHF、版权或真实个人。原对照在极低FPR时仍有持平/反退，reference原已熟悉文本也会弱化shift；多family的平均AUC不能证明architecture不变定律。LoRA/全参recipe与单H200估算费用须保留，阈值按目标人口另验。访问、reference或matched controls不成立时，保持Unknown，回退原score、provenance/canary与正式privacy合同，阴性不签发无泄漏。

G. FedSQ是否新增Ch16或仅报告，等root定点Source/owner判断，不先伪造PRE通过；MSAO争议只Report，不申请Books。以上6段PRE如通过，root只授对应owner的原位小增量＋自身末注窄锁，不改其他正文或增结构。

### G. Ch16 FedSQ：扩维解释之后、activation选择前，一段窄PRE

固定某输入区域的activation gate，会让FFN对输入表现为affine map，却不让同时更新的多层权重变成一个线性参数：在正区域固定gate的标量两层例中，两组权重`(1,1)`与`(3,3)`的输出平均为`5x`，平均权重`(2,2)`的输出却是`4x`。这是由本章两层乘积直接得到的数学边界，不是某篇论文的平均模型保证；只有其余变换与gate固定、仅一个线性参数块变化时，才有相应的函数平均条件。[一个有限DualCopy提案](https://arxiv.org/html/2604.02990v1#S3)将冻结结构副本产生的binarymask与可训练定量副本分开，后者才参与跨客户端平均；它用双份权重储存与额外结构前向换固定选择路径，trainable数并不因此减半。所测CNN的warm-start/central calibration和部分反退只支持这项条件设计，不授Transformer/MoE迁移、joint参数平均等函数平均或全域收敛。gate或目标分布需要变化时，保留原activation/完整微调与独立质量验收，不能仅因“区域内线性”签发合并正确性。<!-- source-family:SF-2026-ARXIV-2604-02990 -->

作者已实际Ch16原61–115扩维/activation/conditioning邻接与Ch15/17交接；标量x=1读取公式验算平均输出5/平均权重输出4。root请求的严格权限边界均在本段，不用原文未给的聚合定理。G同样待root逐字PRE与授锁，不提前写入。

## 00:08本轮结构检查与下一精确位置

正式README现进行中，已添加授权补窗及显式冻结档案字段；V3通过，46原候选整行相等、43031字符连续原§4仍全包含/未改。首次V3因未加冻结档案字段把46旧日期按补窗校验报错；仅添加既有支持字段解决，不改校验器或移动日期。检查时间取本机实际00:08:38+08。本日限定diff-check通过。

待root逐项Source/PRE与窄Books锁；正式8行和证据补段将按真实结果同步。API两次失败、CL/DC有界停点和14机构实际字段仍待正式§2归并；不因此预写完成。无锁、无shared Books/State/index写入，未stage/commit/push。

## A/B/G本轮实际写入（00:20以后，POST仍普通待办）

root实际必要Self-Guide/FiberPO/FedSQ原文与三处owner邻接/逐字PRE通过，授Ch33 A/B各2body＋自身notes及Ch16 G1body＋自身notes窄锁；作者已实际原位写入并读回全部新增/前后：Ch33 A约299、B约722，Ch16 G79；新增只PRE批准内容，没有推FL全章/新owner。Ch33第一次patch只写A且在metadata总结中多加空行，下一依赖patch已移除空行并正确插B，完整总结三行仍连续，不保断句错误。有限diff-check通过，不授语义验收。

当前持有Ch33/Ch16窄锁，等待root非writer实际POST及notes状态同步后释放；C/D/E/F仍Source/PRE待root，无锁/写入。正式§2现已归并14本轮实际入口/停止；CL78/DC12目标ID标题事实按原件计数，18个旧有效same-v1事件只复用去重，不搬归属。正式报告46旧行与43031连续原§4依然冻结/可核，V3通过。

read-only Git检查见本日早期26新增_sources已外部暂存、其中ADMISSION/fetch script另有unstaged增量，作者未执行任何Git mutation、不改index；不能说index为空。后4/02990等本轮原件当前untracked。后续checked范围需同时cached+unstaged，不覆盖任何并发/已有修改。

本次另实际去script后核Z.ai DOM：Research明示2026/04/07 GLM-5.1与04/01 GLM-5V；release-notes明示2026-04-07，按自然日只作为补04-06窗外列项，不新建未知时区请求。旧09点原窗口的GLM-5.1未明示时区请求仍归旧§5，不迁移。已将正式§2窄修为本轮日值切片已检查，未授历史完整性。

## A/B POST通过；G accuracy窄修；C～F Source通过/窄PRE校正

root实际新增Ch33 A299–301/B722–724与完整前后/本人合注POST通过，作者仅同步本人notes为真实POST并释放Ch33锁。Ch16 G须把affine论断限制在ReLU这类piecewise-linear activation及binary gate；作者已实际开头限定“这个计算直觉还要区分输入空间与参数空间：对ReLU这类分段线性activation，固定同一输入区域的binary gate…”，其余5x/4x、单参数块条件/原文权限/费用反退不动，待root读回accuracy改句POST，不把一般GELU/SwiGLU叫affine。

root明确C/D/E/F必要Source与采用边界已核；C逐字草稿中末句“独立oracle”本轮写入将精确改为“独立验证”（原稿历史保留可核，不能默认本论文存在外部oracle）。E实际插入位置明确为：**Ch66现有正/负framing原段末source-family2602-04306之后，先插D两段，再插E两段，之后仍接原“人口属性也不能只用一种提示线索定义。名字、方言、对话历史和显式类别标签…”完整段。** 即E紧邻新D的counterfactual诊断，补prompt机制归因的active-control与compliance人口；不搬原pair-mapping、demographic-cue或别条反证。C插原Synthetic-data开头两行完整段后，F插Min-k位置sensor两段后，等待root授Ch27/66/72窄锁再写。MSAO不写Books，中心争议Source终态仍须root确认。

## C/F实际原位写入，POST待非writer

root Source/实际插点/PRE通过后授Ch27 C两body＋本人注、Ch72 F两body＋本人注。作者实际写入并完整读回新增/局部前后/本人注：Ch27约357–359（“独立验证”准确措辞）、Ch72约361–363，原后续learner-refresh与gradient-adapter论证均连续，未搬或改旧段。限定diff-check通过。现Ch27/Ch72两窄锁待root实际POST；A/B Ch33已释放，G accuracy窄修仍Ch16待POST，D/E Ch66未写/未持锁，不等整批。

## D/E已写；MSAO实际必要Source终态校正

root原anchor/PRE授Ch66 D/E各2body＋两本人notes，作者已原位实际写入632/634与636/638、完整前后/自身notes已读，原framing/personal-cue全部保持、限定diff-check通过。POST仍普通待root，非作者actual之前不释放该锁或计完成。

root实际MSAO Alg1/Eq15–16、5.1.1、5.3.1/T1、5.3.2后确认6分深入争议安全隔离PASS：128/35=3.66是总倍率，(128−35)/35=2.66是相对增幅，**不能直接断言算术错误**；原improvement×与摘要倍率比较分母语义未统一。Cloud accuracy随带宽变化只显示同人口/生成/超时条件未说明，不单独证无效。作者已实际修本记录首MSAO及正式§4/候选措辞；保真正未决GP regret/EMA最优均方收敛的假设/更新式、verification/rollback协议与匹配评价条件，需要作者澄清才只重开这些命题。中心保证不采、不写Books，不降分/删除贡献，不据争议重读无关附件。

## 后批实际POST通过与整日交接

root非writer实际读Ch27 357/359全部局部邻接/本人注、Ch66 632–638四body/原framing/后cue/two notes、Ch72 361/363完整两段/Min-k/后adapter/本人注及Ch16准确性修订ReLU段79/前后/本人注，Source/PRE吻合，POST通过。作者只同步本人notes为真实审阅身份后释放Ch16/27/66/72全部窄锁，Ch33先批已释放；不改任何批准正文或旧notes。正式54行＝原46整行冻结＋新增8（7真实整合＋1 MSAO深入争议），普通来源处理/候选审阅/Books待办0，DAY/FINAL仍待root实际审阅。

Git index包含外部既有暂存，不执行stage/commit/push或任何Git mutation。cached immutable HTML/raw自身含上游trailing whitespace，不能将未经配置的cached diff-check声称通过，也不清洗原件；基线有末尾附加空白行， substantive原46与连续§4未变。工作树正文/notes和README限定diff-check单独核验，raw免清洗与cached差异明确交root，不把机器格式检查冒充语义Gate。

## DAY前Coverage恢复：LG/CV可读listing，不冒充受阻

root独立DAY前发现模型/多模态主题API失败不等官方month不可读。作者各一次https://arxiv.org/list/cs.LG/2026-04?skip=0&show=2000与CV同路径恢复HTTP200，原件SUP_lg-april_20261014.raw/SUP_cv-april_20261014.raw和request，2000/3899与2000/3262。只投影02333–03231本批80/105标题，不读月余文，不成为全篇队列；20个强机制ID membership只查本/邻日正式候选（同event不限定v1）。02525/02638/02715/02816/03118共5个04-06有效same-v1即去重复用，不重评分/Books。

另15完整官方v1题摘实际读，具有具体机制/反证，请求root准入校准：02338共享PEFT专家调制/无参router；02355entropy-guided reward更新/bonus；02371逐页证据trace/低强度merge；02492视觉文字token成本/渲染反退；02556 NF4 shared LUT/index；02570细粒度执行pattern/weightedSVD；02689初层attention去偏/动态rebalance；02751MMSE-FI-FIR几何分解；02817双流zero-init teacher/单流student；02870backward tokenwarp；02956parameter/token重要性互扰/多stage策略；02979cache/predict/recompute与active frame；03072featureMI sensor；03114prompt抑制≠conceptforget评测反证；03231CLIP/DINO多层entropy/正交/gridfusion。15均无本/邻日正式候选同event，AB原件/request SUP_[id]-ab_20261014，必要core/DOI请求独立保存；不能保持首批后普通0或在新15未审时声称DAY通过。首批7实际采用POST/锁释放仍有效，不重做；MSAO6分中心争议仍隔离。

root随后明确15停在完整AB准入层，先分清旧约束→实际增量→改变解释/选择，尤其CoME/Efficient3D/MMPhysVideo/CoMP/MI-Pruner不能因领域新模块就保留。作者已捕获HTML/DOI但尚未展开必要core、不授Source完成；只对校准成立者进必要证据，含糊者仅定点核心辅助准入。此15为潜在线索而非已retain/评分家族，不批量推owner写入。

## 本日最终单篇归并，待root六部分DAY

LG/CV后续准入/必要Source与actual owner逐字PRE/真实非writerPOST见[同一本日恢复证据](./SUP_LG_CV_REVIEW_20261014.md#final-actual-single-item-closure-awaiting-root-six-part-day)。root全15完整v1AB与两定点core校准后14具体贡献入选、NF4有效EX原封复用；14必要Source均实际支持/关键反证通过。12实际最小整合（H/I/J三、K/L/M/N四、O/P/Q/R/S五）及02371/03114两具体已有覆盖全部终态；所有本人末注同步actual身份并实读回，全部Books窄锁释放。此前54/普通0只是Coverage复核前checkpoint，不是本日最新结论。

正式68＝原46整行/日期/评分/原窗口冻结＋本轮新增22（19真实整合/10唯一owner/26新body、2具体已有覆盖、1MSAO中心争议安全隔离）；总42I/18C/7R/1D。旧连续原§4保持，邻日04-06原47不迁移、不重复评分/Books。普通扫描/筛选/必要Source/owner/正文与notes写后待办0，六部分DAY和完成字段FINAL仍需root实际验收，不从单篇POST提前整日通过。精确API/historical public-event/revision及机构source slice限制、旧43日期/8源限制和MSAO重开条件仍不作正面Coverage/Evidence/无遗漏；没有未读普通工作转受阻。未Git mutation/stage/commit/push，外部暂存/并发修改保持。

## DAY前Meta有限actual补核，只投影Apr06

同级author提供精确入口/Next停点，并明确curl三页reset/000无可读原件；本作者不继承其日候选/日期结论，2026-10-14实际web重新打开三URL：

- https://ai.meta.com/results/?content_types%5B0%5D=publication — 总433行，近期2026段L42–193为Oct2→Jul17，Next实际可见；尾legacy2016–2020混排不作历史有序止。
- https://ai.meta.com/results/?content_types%5B0%5D=publication&page=2 — 总436行，近期2026段L42–194为Jul13→Apr16，Prev/Next实际可见；尾legacy混排。
- https://ai.meta.com/results/?content_types%5B0%5D=publication&page=3 — 总435行，初次三页合输出第三被截断，不冒实读；本作者另单独完整打开实际读L42–195近期段Apr14→Jan2。其中L57–68显示Apr09/Think in Strokes，L72–81显示Mar26/in-silico neuroscience，随后Mar24/17与更早日期。页尾legacy混排且Next仍在；只用近期切片跨Apr06而止，不称全catalog有序遍历完成。

本次实际所见display-date投影无Apr06 publication条目，不把目录显示日期当所有论文first-public。可用web目录不能被curl000称不可恢复；仅窄修README SRC-META-AI原“首屏Next止/分页历史不可恢复”口径，近期三页slice已处理。Research0/历史未列删改与first-public完整性仍非已证明，具体dated原稿/当日官方导出到达才单源重开。Alta Daily原实际核心EX保持；新发现波、当窗新候选/评分/Books写均0。其余13来源、22采用处置与所有POST/NC/锁释放不变；DAY/FINAL仍待root，LG_CV packet末尾由root拥有，不写该处。
