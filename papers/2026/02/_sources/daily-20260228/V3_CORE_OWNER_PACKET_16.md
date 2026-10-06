# 第十六包：AB9剩五个具名潜力的必要核心与实际owner（待非作者PRE）

只续既有22896/22918/22936/22953/22960，不扩来源池。精确v1题摘与当前官方Comments已读；原HTML必要段实际读到支持、对应控制与直接反侧即停。FETCH_AB9_CORE执行2026-10-05T20:19:00～03Z，不以HTTP200当审阅。22953发现稿“五模型/fullfactorial”不代替原v1三模型配置；22960采用原题名UCM而非发现昵称。22896有本窗v2号码但没有已见的重要纠错/撤回信号，版本号本身不触发全文revision diff。以下均建议而非安全终态，无Books写入/lease。

## 同ID日期

原v1 Submitted在02/26UTC，晚于02/25 19:00Z；官方公告政策给02/27 09:00+08下界，同IDregistered已存在恢复秒精度上界加1秒。DataCite只恢复身份/上界，非技术或首公开公告。全区间含左不含右、完全落本窗。

| ID | submitted UTC | registered UTC | 公开区间+08 |
| --- | --- | --- | --- |
| 22896 | 02/26 11:34:36 | 02/27 02:57:24 | 02/27 09:00:00～10:57:25 |
| 22918 | 02/26 12:06:02 | 02/27 02:57:57 | 02/27 09:00:00～10:57:58 |
| 22936 | 02/26 12:26:32 | 02/27 02:58:25 | 02/27 09:00:00～10:58:26 |
| 22953 | 02/26 12:48:02 | 02/27 02:58:51 | 02/27 09:00:00～10:58:52 |
| 22960 | 02/26 12:54:46 | 02/27 02:59:02 | 02/27 09:00:00～10:59:03 |

## 22896 DySL-VLA，2+2+2=6，拟Ch26一段

2026-10-06 本项终态同步：root作为非原prepared作者实际必要原证/actual owner PRE并窄融正文；静态重要层+dynamic skip，post continuity失败dense重算；自检非truth。2+2+2=6，Ch26自身末注1464；final_audit作为非写入者已实际读取正文、完整邻接和自身末注，actual POST通过，root已释放锁。日报作者仅据这份独立交接同步处置，不冒称自己重读全部原证/附件；保原有效身份/精确v1/采用范围、费用及回退，不授实现复现或日级验收。

root 非原 prepared 作者实际必要原证/actual owner PRE：§3–4、blocks21–59/61–76；静态重要层+动态skip、post continuity失败执行前dense重算；自检非truth、质量反側与时延口径。精确v1身份/日期未变材料复用。当前主干已有窄整合及自身末注，作者正文/完整邻接顺读后交非写入者POST；不是报告完成、未核artifact/复现。

[原v1](https://arxiv.org/html/2602.22896v1) blocks21–76实际读。完整早退丢掉后段重要层、逐层controller也吞延迟；原机制用activation cosine变化识别静态保留层，动态层可经adapter直接跳到下一static层。再以最近k动作差分的连续性变化限制哪些controller可启用，检测到首次continuity下降后**用无跳层模型重算当前action**，不是动作执行后的物理验证。连续性是训练演示中的重要动作proxy，突发关键动作仍须先预测才可检测；平滑动作亦可能危险，不授correctness/safety保证。冻结LLM而训练adapter/controller；先拟合被跳层的activation，再用抽取单dynamic位置的soft mixture联合训，避免随机controller拒跳导致adapter不学。不是training-free，也不是动态跳任意层的无损变换。

直接控制Table4移除pre/post/static/two-stage分别退步或增加延迟；更少static层有更低latency却质量退，k=1/9都弱于5。Table2基线2.92而Table4写2.82，不能混作统一fullmodel质量收益；LIBERO平均原97.1→96.5也不是lossless。**所写移动公式局部隔离**：41–42给δl=ceil((Ct−Ct−1)/η)，下降−2η则δl=−2、li←li−2，与“下降时更多保留/前移”的解释相反；仅不采用该符号式作为已实现正确controller协议，保留经验模块/对照，不推实际code一定错或整项D。后验重算需额外全模型调用，平均耗时不授关键动作tail deadline。

RoboFlamingo3B/CALVIN D→D与ABC→D、OpenVLA-OFT7B/LIBERO四suite；RTX4090/A6000/JetsonOrin的LLM latency分别，Fig4额外3B FP32/9B FP16，不挪给所有表同dtype。Table2两skip方法6.7k步骤/7GPUhour，DeeR训练预算更高，跨方法总体不是等训练量纯结构因果。actionchunk8的23.2Hz是作者折算，不代表模型345ms内逐动作新观测闭环；batch、并发、重复seed/CI、完整robotpipeline/SLO未披露。

实际owner `MULTIMODAL-EMBODIED-VLA` Ch26 1175–1234完整邻接已读：1181–1193是action敏感度/观测freshness gate，1195–1197是固定出口与视觉KV合成，1199–1214是denoise/rollout cache；未承载**静态保留中段重要层＋动态跨段adapter跳转、过去连续性先限制controller＋当前首变重算**这一层深控制分支。拟在提前退出小节之后一段＋末注，保proxy/额外重算/公式隔离/原fullpolicy与独立controller退路，不复制缓存身份或授physical commit。

## 22918 Where Vision Becomes Text，2+1+3=6，拟Ch23一段

[原v1](https://arxiv.org/html/2602.22918v1) blocks25–99/100–128实际读。同图original/inpainted activation差、315图独立PCA训练集，在post-MLP residual各层对**全部visual/text tokens、prefill/decode**投影去topN单位PC；attention-head选择另以text-region/background ratio排序并置零输出。三inpainting/blur与matched非text boxes、93random heads10draws是直接反侧控制，但差向量仍只是该text-removal操作信号，不能把PC认证为唯一OCR circuit。

Qwen3-VL4B的L17–19干预减少OCR却Count+4.3、RWQ+1、spatial−2；同family8B counting改善却RWQ−14，2B/Phi一般quality退、InternVL早层普遍退。**architecture与训练/规模同时变化**，原DeepStack vs inputprojection解释是机制假说，不是单变量architecture因果。跨dataset仅方向有效，不是相同max-sensitivity层迁移（Table3可L4/L30）；总体72.9%是PC1对差向量variance，不是全部OCR信息量或压缩率。保按model/layer/task重新验收，不采“越大越独立”定律或安全defense。

五VLM、EgoTextVQA/OCRBench/InfoVQA与CountBench/EmbSpatial/RealWorldQA；normalized substring/97%subset judge是evaluator协议，单greedy全dataset运行无errorbars；randomhead10draw不提升全部结果为multiseed。4RTX6000Pro、每图约12GB/全层24GB、PCA315图约15min/model；precision、batch、完整latency/concurrency/SLO未披露。inpainting dense document/layout artifact、未测任务collateral、selection与投影成本保留。

实际owner `MULTIMODAL-REPRESENTATION` Ch23 765–807完整邻接已读；786–788已有Attention重排/FFN扩展与干预不普遍的分责，但未覆盖**paired text-removal→残差方向/层位干预、OCR下降与其他视觉能力保持或退步分账、direction transfer≠层位transfer**的具体诊断。拟在表示几何小节末一段＋末注，不同于22426视觉问题elicitation，也不因OCR字样制造第二owner。

### 22918 独立必要复核与 Books 处置

非原 packet 作者 feb28_ch23_finish 独立阅读 exact-v1/本地 primary blocks25–128：限采用命题的方法、对应实验、设置和直接反侧，不扩全 proof/artifact 或 revision 对比。旧 packet 只作材料，评分2+1+3=6保留。actual owner 为 Ch23 MULTIMODAL-REPRESENTATION：05668重排/扩展与probe/steer区别已有，但没有成对文字移除操作特异方向及分层控制的诊断链，因此 Books Decision 是具体深入而非泛化 No Change，已在相关机制主干写一窄段。三个文字编辑/随机非文字框对照、4B空间和8B阅读反退、InternVL早层全反退、greedy单run及原forward/OCR回退近文。必要原证/actual owner PRE完成；作者正文/完整邻接/自身末注已顺读，root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放，未复现、非日级Gate。

## 22936 Generalization Bounds of SGD in Homogeneous Neural Networks，2+1+3=6，拟Ch28一段

[原v1](https://arxiv.org/html/2602.22936v1) blocks26–89、90–123、171–194实际读；最后仅为明确schedule是存在的adaptive随机变量而非名义deterministic t^-1/2，未遍历其余proof。H>2 homogeneous **network与非负homogeneous loss**、有replacement的SGD、unit-sphere bounded loss、沿训练轨迹empirical loss≥一半非零Bayes optimum、sphere Lipschitz/(γ,β)approximate smooth且γ=o(T/n)是Theorem1权限。方向v=w/||w||上的有效步长是ηtilde=η||w||^(H−2)，Euler inner product=Hloss；设deterministic ηtilde≈1/(t+U)，名义η需按随机weight norm自适应，所写Eη=Ω(t^((H−4)/2))是存在性下界**不是任意该阶LR均泛化、也不是普遍推荐**。H3可慢到期望t^-1/2，仍须上述噪声/正下界与iteration/n/smoothness窗口，不能迁到AdamW/Transformer CE。

普通非凸stability基线积累exp(βΣη)，与此球面/范数控制的分析对象不同；loss form、normalization、weightnorm与实际schedule一起决定权限。Cor1一般loss还需ρ导数比正有界及zℓ'≤k2ℓ，noisy-label lower bound失败不得继承。原classification方向risk不是训练rawloss或生产quality证书，成立条件已足支持这条可选解释，不机械要求LLM实验。

**优化分离子命题不采**：Th2需PL/strong-growth/μ>4B²H²σbar²(1+α)等额外条件。Example3给μ≈19.7、H3、σbar²=2^(3/2)，B≥1（max individualnorm≥mean norm）、α>0时门槛至少101.82，例本身没有满足所声称兼容条件；只隔离该例对Th2/普遍优化收益的支持，非从局部失配否定全部Th1或遍历全部证。硬件/precision/batch/SLO对此理论命题不适用；Figure2仅illustration，不承担性能采用。

实际owner `TRAIN-PRETRAINING` Ch28 340–420完整邻接已读：349–351是loss/proximal stability index，408是fullbatch homogeneous exponentialtail implicit norm/margin；均没有**球面有效步长/随机范数适应＋本损失下有条件SGD stability**，不与implicit bias混合。拟在Optimizer非参数化独立旋钮附近一段＋末注，保特定正下界/γ/时长条件、非任意t^-1/2、调参/范数监控费用与成熟tunedSGD/AdamW/heldout回退。

## 22953 General Agent Evaluation，2+1+3=6，建议Existing Ch66

[原v1](https://arxiv.org/html/2602.22953v1) blocks16–39/40–52/53–110/217–225实际读。task/context/actions统一protocol，明确referenceagent原先隐含的信息/环境权限，用外部agent/benchmark adapters同步翻译，再以**5agents×3models×6environments=90configs**测量。原v1不是发现稿五模型；default model params、100turncap，参考SWE环境已克隆/patch生成不算能力目标；统一API仍不能自证任意adapter语义等价。

matched同model下ReAct/Short相对control、工具数468 vs128能力接口限制、APIrank与architecture相依和failed-run更长说明对象分责；pooled跨benchmark相关可由model差异驱动，非agent跨域generalization。**量化保证不采**：28.2/.6约47倍非85；interaction5/.6约8.33非4.5；AppendixE六bench100且Airline50按字面550，不是650有效sample；故不采这些倍数/通用CI半宽/significance保证。Table1/leaderboard胜败不是architecture纯因果，跨官方全量leaderboard与100samples不同，不说通用匹敌专家。failed-run统计又排zero-step、cap50去长尾约7%，非全失败成本。

Benchmark originalscorer/模拟用户/hiddentests条件分别；三API模型默认params无hardware/dtype，成本为January2026 LiteLLM listprice而非通用当前价格/完整workload TCO，seed/repeat/独立样本/总tokencost等未统一披露。Text-only、有限agents/models、扩benchmark仍需人工adapter工程；不授可视web/nointervention任意迁移。

实际owner `PLATFORM-EVALUATION-SYSTEM` Ch66 212–267完整邻接已读：225–229**已经具名GeneralAgentEvaluation并承载provider/parser/message/architecture wrapper改变subject与adapter semantics**，250–256具体`model×benchmark×harness×environment×scorer`、原trajectory与adapter equivalence；3946–3964完整邻接又在3952–3954承载模型家族/生态/任务方差制造benchmark相关与因果权限。拟采用的长期对象身份/混杂分责已真实覆盖，建议Existing/NoChange；不为该paper的variance数字和排行榜新插一段，报告保受限matched结果及口径隔离。

## 22960 UCM，2+2+2=6，拟Ch25一段

2026-10-06 本项终态同步：root作为非原prepared作者实际必要原证/actual owner PRE并窄融正文；PE warp视图/时间对应与clean/noisy双流；几何条件、质量费用反侧。2+2+2=6，Ch25自身末注1284；final_audit作为非写入者已实际读取正文、完整邻接和自身末注，actual POST通过，root已释放锁。日报作者仅据这份独立交接同步处置，不冒称自己重读全部原证/附件；保原有效身份/精确v1/采用范围、费用及回退，不授实现复现或日级验收。

root 非原 prepared 作者实际必要原证/actual owner PRE：§3–5、blocks28–51/52–55/61–68；PE warp的视图/时间对应与clean/noisy双流；质量/费用反側、几何条件与真实反馈。精确v1身份/日期未变材料复用。当前主干已有窄整合及自身末注，作者正文/完整邻接顺读后交非写入者POST；不是报告完成、未核artifact/复现。

[原v1](https://arxiv.org/html/2602.22960v1) blocks19–68/69–71实际读。先depth/pose把reference/history点云投到目标view，warp的是token**spatial PE并继承目标temporal index**而非把生成图像当世界真值；reference对每个target复制，memory只选最相关target避免全N组合，pose按VAE r帧平均要求该块运动近uniform。clean条件token只同frame selfattention、originalPE，noisy全体互读又仅读warp到同targetview的cleanKV；这是双stream读图限制而非所有history全jointattention，也非无条件cache永久可复用。

原历史/revisit scarcity用monocular pointcloud novelview render/mask+temporalshift扩训练，occlusionmask是条件availability不是depth正确认证。Wan2.1 1.3B内部I2V、561k801frame训练视频、81frame/21latent640×352、8A100 batch8/30ksteps约4天，50CFGsteps、STream3R depth和20FoV-IoU memory；112static场景quant/dynamicqual不同。samebase重实现C-a-M/VMem/VWM/UCPE并用同curation控制，但不是原release代码复现。camera pose评价也用DepthAnything3，是estimatedproxy；revisit相似度不授物理transition。

Table1 VWM可有更低TransErr/FID/FVD，不采用全面胜出；Table3撤dualstream cycle视觉可更好但5.14s/frame vs2.40，增加memory40质量可好但3.26s/frame，非免费memory。Table2/3同20memory的cycle数值不完全一致，保各表配置，不合并精确统一最优。2.40s/frame单A100作者结果不授实机实时deadline；dtype/batch/concurrency/seeds/CI/全pipelineSLO未披露，depth/storage随历史增长、dynamicobject artifact、clip误差积累与geometry/pose域外失配仍需短窗/干净观测回退。

实际owner `MULTIMODAL-WORLD-MODELS` Ch25 612–634与1028–1054完整邻接已读：622是history/memory corruption与student rollout，628是无序reference目标time身份的spatialpacking，1045是localpointcloud延迟融合/多anchorjointattention。未承载**reference每view复制与history单view映射、cleanframe局部/目标view条件读mask的双stream计算—质量取舍**。拟在camera-conditionedmemory 1045后一段＋末注，分清继承PE-field与新增time/consumer mask，保几何proxy/有损mask/更慢或更差反侧，不接管AgentMemory或runtime缓存chapter。

## 停点

5项拟4I1E均待root actual必要证据/owner PRE；子命题隔离不自动将可独立支持的贡献整项D。35safe=25I7E3D保持。没有Books lease、没有新Books正文，无全proof/artifact遍历或revision比较。下一步仅AB9既有七个含糊事实的一次决定性core，或root具名PRE回核后按实际sharedfile窄lease写入；不重扫库存，不自行启动别日。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）局部复核及实际落实：22936：原必要blocks41–79/171–177与actual owner独核；Ch28正文357/完整327–375/own1811 root非写入者actual POST通过。未变身份/精确v1/采用命题复用，费用、直接反侧/错误子保证及旧路径回退近文；不授全附件、实现复现或日级完成。
