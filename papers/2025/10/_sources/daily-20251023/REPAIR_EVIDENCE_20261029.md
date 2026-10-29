# 本日恢复候选必要证据

仅已实际读取的域计入下述记录；HTML/txt下载不等阅读或全篇验收。精确元数据日门见POTENTIAL_FULL三raw及POTENTIAL_BOUNDS。6跨目标界（17917/17925/17853/17862/17858/17845及其精确字段）尚需具名事件恢复，不能以registered独断日；本表不签这些项正式候选。下述评分按新增命题，不以Books决定、访问或品牌计分。未核代码/图像像素、未复现实验。reader记录按身份版本命题复用。

## 2510.18179 AdCo

精确v1已取得；writer实际读A.1/Eq7和A.5.3：以往PR增量的动作均值+探索项选协作/竞争；协作取上一轮最高PR轨迹，竞争请历史平均PR最高peer批评，然后发布S(t)/PR(t)。这不等当前state条件价值已独立估计，初轮无交互，未补N(a)=0完整实现recipe。reader R4首次必要反侧已完整消费：PRM质量未做退化/对抗曲线，理论/状态探索仍未来、强worker升级可被majority抵消、全部调用/延迟和默认provider超参付费。2+1+2=5；具体自适应动作consumer差额须深入owner比较，不采20%普适保证。已读当前Ch82 peer选择与相邻Ch81/83交接，尚未授PRE/Books决定。

## 2510.18586 TokenCake

writer实际精确v1 §3.1–3.2、4.1–4.3/Alg1、5.1–5.2/Alg2、§6、7.1–7.4。DAG/FuncNode传call_start/call_finish及developer估时，EWMA预测工具完成；仅当预测空隙减双向传输还容纳waiting request才offload未共享KV，预取前分轮预留GPU块，CPU free-list缓冲burst，copy完才释放源GPU块。空间scheduler按结构/运行分数和历史用量分reserved/shared，非全图最优证明。公式动态priority正文称偏短/防饥饿，但`wait*log(tokens/wait)`与该直觉不直接一致，且Alg2配额/比率未闭clamp；不照作已验公平或精确SLO recipe。

§7.1 Qwen2.5 14B/A10080GB与32B/H200140GB、CPU swap100GB，Code-Writer/Deep Research/ShareGPT-AgentCode/Poisson到达。因模型不能稳定tool call，**工具调用及其时长模拟**，不证明真实工具分布或所有Agent行为；baseline vLLM/LightLLM版本、precision、输入输出完整分布/尾SLO/置信区间未披露，不补。低load0.05QPS与vLLM近似，高load差额不能单独归因每个component，KV block utilization不等GPU kernel利用率。§7.4 allocator和预留优化自身决定迁移代价，传输比重算快也非所有链路普遍结论。图像数值未测不再摘读额外点；不采摘要47%/16.9为部署保证。2+2+2=6，停等KV生命周期与critical配额是具体长期机制，待reader证据与owner对照。

## 2510.18121 CAD / DistCA

writer实际精确v1 §4.1–4.2、§5、6.1、6.3及§8。CA-task为query shard加完整context K/V，CPU profiler+greedy依迁移FLOPs/bytes平衡；block-size128约束，不能把它描述成任意K/V子区间任务。独立池是逻辑分工，实际**in-place attention server**让同GPU在CA和其余层间切角色，避免独立池显存闲置。两nano-batch ping-pong、TP intra-node与跨节点CA通信覆盖；PP重排forward/backward tick，warm/drain借空闲GPU。不是无通信/无临时activation，stateless仅无trainable参数。

§6.1 Llama8B/34B、DGX H200每节点8×140GB、TP8、PP/DP/CP搜索、每配置30batches，Pretrain长文上采样/ProLong两合成长度分布，平均throughput非收敛/质量或尾时延。WLB-ideal为作者重实现，未实现改变训练动态的deferred execution，不能称完整WLB系统等条件胜出。§6.3 compute太小不能全隐藏通信、tolerance过严/宽均可损时延；§8仅完整KV、通信模型忽略resident KV而高估bytes，dedicated pool/fault tolerance仍未来。precision/CUDA/完整网络profile未披露，不补硬件配方或1.35x普适保证。2+2+2=6，token粒度分离与内存/通信取舍待实际Ch36 owner比较。

## 2510.18480 DLM效率

reader R6必要配置/关键反侧直接复用：单A80080GB/FP16/同SDPA，强制固定输出64–2048、batch1–64、GSM8K100例0/5shot，cross-checkpoint非同质量Pareto；大batch反转不等所有DLM永慢，roofline非kernel profile。2+1+2=5；长期命题为batch/长度/总求值与质量共同冻结，当前Ch24“跨token/跨request batch”及2510.04146段已具体承载，需reader确认实际已有覆盖而不为制造diff改书。

## 2510.18525 SPEQ

reader R10必要机制/直接反侧复用。2+2+2=6；权重bits共享可省draft副本，但BF16指数截断近似、per-tensor scale、draft/target hidden/KV修复与exact rejection未闭，不采lossless保证。28nm/500MHz综合功耗仿真不是GPU或流片速度，5模型×3任务不写成15模型。拟只表示/执行接口，尚未writer补支持之外的内容或Books采用。

## 2510.18821 SSP（支持域进行中）

writer精确v1实际§3.1–3.3/Eq1–5/Alg1：同policy不同prompt扮proposer/solver，预置答案集，proposer search文档交RAG solver，再经LLM语义judge与格式过滤取得题池，solver GRPO/proposer REINFORCE按solver失败奖励。RAG可答只是指定文档/同源solver下的一致性，不等唯一答案/外部事实认证。Alg1 RAG式未显式写文档参数，不能自行补实现已核。完整实验/关键ambiguous-answer反侧尚未读足，普通待办，不签完成。

随后实际补读§4.1、§4.4 noisy-doc完整论述与AppendixE非唯一答案例。训练/评价E5+Wiki2018 top3，七QA各500/Bamboogle125，Qwen2.5-32B judge pass1；verl/SGLang、prompt4096/output8192、150–200steps。既定答案集和LLM judge仍外部监督，不称无任何监督。Temptations例直接表明特定文档可答不保证开放query唯一；噪声文档4比7较好仅该消融，不是验证证书或普遍阈值。模型/工具环境/题池/双角色多重rollout与RAG验证均付费；未读取全部表点/完整hyperparameter表，不采用额外速度/全部模型统一提升。2+2+2=6，资格过滤与对抗难度消费的命题标准支持已足，具体Books若有差额再深入，非实现已核。

## 2510.18544 SLICE

writer精确v1实际IV-A–D/Alg1–3、V实验及高load分组论述。utility×TPOT贪心选任务，profile估1s周期可行再用decode-mask按rate分配不同轮次；这是平均周期quota，不证明任意相邻token间隔上界。Eq2 TTFT不等号方向与“不得超时”冲突，Alg3包含端点循环/ceil-floor和矩阵列索引未闭，不照抄完整recipe/最优或硬TPOT保证。高优先real-time获益会牺牲non-real-time，高load后者仍低，不能用整体35x作全类SLO保证。ChatGLM2-6B/RTX4060Ti16GB、三TPOT100/120/250ms、到达0.1–7与任务比例7:3限定作者结果；完整precision/engine版本/输出分布/重复置信未披露，不补。2+1+2=5，仅quota-v-gap/分优先级验收，待owner具体已有覆盖比较。

## 2510.18085 R2BC

writer精确v1实际III/IV Alg1、V-A/B、VI及VII-A/B、VIII。每episode一名agent受人示范、其余当前policy执行，各自buffer/BC定期更新；不要求human联合控制，也不是语言MAS消息学习。四VMAS任务2–3agent，10seed/固定50初始、normalized reward不是任务完成概率；真实三HeRo+/中心相机ArUCo和mock LiDAR，local policy不等分散感知。作者在模拟中两套240示范，物理两任务各5初始、0/1/2次3s人工介入；零介入navigation高方差/p=.0773，不采普遍sim2real显著或无人安全。BC/MSE、online示范/物理标定与人工纠错均付费，nonexpert负担与收敛/shift理论仍未来。2+2+2=6，单agent示范与联合执行数据分责具体，待Ch26而非Ch82通用编排owner比较。

## 2510.18003 BadScientist（必要域未完）

writer精确v1实际§3.1–3.5、4.1：单pass reviewer只读稿、无运行/联网证据，三review模型均同提供商，不由角色数授错误独立。rate-matching和isotonic阈值拟human acceptance而非真实性；subGaussian/独立review假设的集中界仅latent mean/阈值，不证明fabrication检出。GPT5生成/concern judge，o3/o4mini/GPT4.1评分、ICLR2025分层200校准，合成5000算术验证不等真人审核。4.2和5.2实际结果/mitigation尚待必要读，普通待办，不签完成。

## 2510.18477 LAFA

writer实际精确v1 III-B/C/D与IV-A、IV-C/D：known FA skeleton→coarse/fine prompt DAG→跨subquery复用/后处理，backend承担encryption/DP，非新密码协议。uniform schema且每client一条记录、semi-honest假设不由LLM DAG自动保持。GPT4/T0、20合成query/两schema，operation count不等实测加密吞吐/网络或privacy budget组合；少DP节点可能改输出相关性，不能由prompt“structural validity”直接认证语义等价或隐私。无optimizer完成率仍100%，贡献只冗余操作变化，不把completion提升归optimizer。2+1+2=5，workflow编译与隐私executor分责的受限例，待实际Ch81/72已有覆盖比较，不采安全保证。

## 2510.18798 WebSeer

writer精确v1实际§2.2–2.5与3.3–3.4：reasoner/verifier多轮rejection只保groundtruth一致反馈及最终成功trace，SFT不训tool observation；RL允许answer_submit后回传与gold的F1再继续，按次数指数折扣和长度惩罚。训练反馈有真值权限，不等部署开放问题可自证；web reader同模型摘要不是原网页原证。小3B/7B可重复/坏JSON崩溃而14B改善，长trace多也不保证accuracy；单提交/无coldstart局部消融不隔离全部数据/采样预算。Qwen14B、HotpotQA/SimpleQA与Google/reader/code工具；完整硬件/所有超参和置信未核，不采用current72.3/90数字反投v1。2+1+2=5，训练反馈与部署权限分责，仍需§3.1配置最小核齐再决定标准完成。

## 2510.18596 CUARewardBench

writer实际精确v1 §2.2/2.3、3.2–3.5、4/5。272轨迹/346关键step人工标注，排无agent成功/8+成功和>25步，成功轨迹也可含bad step，step不是整条结果回填。UPE全体正/负同意才判，否则abstain；precision/NPV变好付coverage/采样代价，未在真实RL loop验证。specialist32B低于base、不同prompt改变时间视野和严格度，不能独归“reasoning退化”。截图可能根本不显示file size，独立effect/script仍必要；不用人类标签模拟概率式当真实因果p测量。2+1+2=5，过程/终态及选择性coverage评价，待Ch66已有具体覆盖比较；未核完整模型超参/全部表点，不采跨模型一般排名。

## 2510.18488 AndroidControl-Curated

writer实际精确v1 §2.1完整/3.1–3.4：point→bbox接受域改变、全强模型共同失败只是候选heuristic，LLM改label后仅大随机样本人审，不证明全量错标。任务修改会改变难度/人口，不由benchmark分升授同题原能力或生产可用；bbox包含不等真实effect。GA段称所有benchmark用bbox与ablation原point说法冲突，不能混为固定量尺因果。3B模型/2400 curated与旧31k不同训练，不独归质量胜数量；70%缺陷等样本口径/全部底层轨迹未核，不照录泛比率。2+1+2=5，只评价support和候选筛选分责，待Ch66具体已有覆盖，非部署通过。

## 2510.18483 StarBench

writer精确v1实际§4.1/4.2、5.2/5.3/7。DC原图→pixel/key；TA同时给YOLO每task约400标注、OCR信息和语义动作到bbox执行，差额不是只多一种action syntax。ask只TA episode前一次，hint后续每turn注入，无中途多次搜索；不能按摘要“when ask”补在线策略。RTX4070Ti/1920×1080/0.5s输入延迟、八trial/task、10次invalid终止，0DC不证理论上不能玩。指导效应/asking自选与跨trial历史不识别纯因果，实时client漂移/OS抖动仍在。标注、OCR/YOLO、hint与每turn模型/真实输入均付费。2+1+2=5，观察支持/动作执行/指导三条件分开，待Ch66已有覆盖比较。

## 2510.18476 SToM

writer实际精确v1 §3.2–5：3–5个意图hypothesis、GPT4o likelihood更新belief、归一entropy转confidence并prompt问澄清/追目标。候选意图支持与LLM likelihood都非真实人心概率，confidence仅该模型内集中度；policy Qwen2.5-7B、partner/judge/IM/LHM同GPT4o，90/14场景自称多seed但具体次数未披。oracle还被限定固定轨迹、SToM多探索，超过oracle分数不能证明超真实intent信息上界/概率机制独因果。全部额外模型/上下文费计入，无参数更新不等免费。2+1+2=5，仅belief proposal与action consumer分责，待Ch82已有覆盖；不采ToM真实性/一般social competence。

## 2510.18032 OptAgent

writer精确v1实际§3.3–3.6、4.1：单agent初始utility乘积给edge概率；reflect看交互前后正确/连贯，act增删边，score乘性调整，最终每agent至少一peer并majority。verbal RL不是模型参数RL，reflect正确性权限/标签可用性不能自动授线上oracle。每任务三训练点、100评价/三run、GPT3.5/GPT4o/Llama70B APIs/T.5，完整token预算不等同单agent；top_k=1.0命名不补provider参数语义。全边访问/反思/最终聚合费另算，无通用最优图/正确保证。2+1+2=5，动态图feedback与任务验收，待Ch82实际已有覆盖比较；未采全任务提升。

## 2510.18383 MENTOR

writer精确v1实际§3.3、4.1、5.2/限制。**v1是teacher tool-set exact match**（不是current AB的柔性F1最佳）：只要求同工具集合、不强制完整轨迹，另奖励teacher=gold参考下的答案一致和每call成功执行。v1消融strict set优于F1，不能由当前摘要抹掉；valid execute非答案/副作用安全证明。Qwen3-235B teacher、Qwen2.5/3四student，数学Python训练、RAG/BFCL-v4 OOD，原表有各任务反退，不用overall授统一泛化。verl两epoch/采样随model建议，E5/Wiki2018 top5，未核全部GPU/随机不确定性；teacher采样、tool执行/训练/全部验证计费。2+1+2=5，结果/工具集合/执行三reward权限，待Ch29具体已有覆盖比较。

## 2510.18091 APT

writer实际精确v1 §3.1–3.3/4.1–4.2/4.4与B硬件。熵阈值在quadtree patch尺度决定合并，resize再加原高分辨率subpatch embedding经conv/ZeroMLP残差，进ViT前就形成变长token；packing blockmask隔离各图，dense任务重复大patch feature恢复网格。像素entropy非问题语义重要度，简单背景仍可被问题问到；阈值/packing/rearrange都有费，“network无overhead”不等pipeline零费。MAE/timm基线、layer merge重实现以FlashAttention且禁weighted attention，不能泛比所有原后端；8A100分类/8A6000 dense、inference单GPU，不授并发SLO/无质量损。2+1+2=5，输入codec与dense-consumer网格接口，待Ch23具体比较。

## 2510.18358 Hydra Ensembles

writer实际精确v1 §4.2/4.3/5.1–5.3。同base剪head造M3成员，grouped投影保各head流、MLP权重平均共享，reshape分别在token/depth轴承载member。不是三独立模型原函数严格等价，更不是单次forward就无member工作/activation；Taylor与uncertainty circuit需要不同验证信息，supervised各member仍finetune，zero-shot不等无原pretrain。ViT-B/ImageNet-CIFAR/OpenOOD与BERT/SST2；BERT Deep-Ensemble(D)只是共享pretrain+classifier不同seed，非完全独立pretraining对照。图像分类accuracy还比DE低，局部BF16时间近single不能泛化所有precision/hardware。剪枝/恢复/uncertainty校准及全部分支费计入，不采用理论noise条件推普适robust。2+1+2=5，仅member计算共享与校准独立验收，待Ch15/66唯一owner判断。

## 2510.18117 ICD

writer实际精确v1 §4–5与A.4.1。在线测试stream由teacher补demonstration pool，image-text→image-image→text-text三筛；student生成平均entropy先决定ICL，仍高再异步teacher标注供后来请求。无参数更新，不等teacher免费/当前请求等teacher完成；pool freshness、teacher错误与decoder entropy非正确性概率。GPT4o三次一致才收、caption BLEU2>.5只是proxy，阈值0.4/1.6依任务；SigLIP替各baseline encoder，不能偷称旧CLIP公平原配置。主要4–12B VLM/3-shot、classification/VQA/caption与CodeCarbon/EcoLogits估费，非实测全部碳/速度SLO；prefill/demo读取、teacher重复和pool检索费均计。2+1+2=5，derived demo更新与当前answer权限，待Ch75/29唯一owner比较，不采“distill已改变权重”。

## 2510.18583 CovMatch

writer实际精确v1 §3.1–3.2、4.1–4.3/结论。冻结encoder的局部线性contrastive内层只优化projection，化成cross-covariance目标；实际用Frobenius距离替unbounded trace，加各模态feature matching，并用real数据更新online encoder，最后synthetic数据训双encoder。局部线性/分解可达条件不自动等真实InfoNCE非线性全局最优，未读完整C推导则不采该强保证。Flickr30k/COCO、NFNet/BERT、IR/TR@K；旧MTT-VL/LoRS冻结text而本法可训练，增益不独归一个loss，synthetic抽样少仍消耗完整real特征/online更新。ρ/λ依规模，更多pair不自动更省；所有real/teacher特征、合成/训练与encoder维护费计入，2+1+2=5。只第二阶跨模态配对统计与边缘feature约束不同，待Ch27/23唯一owner比较。

## 2510.18148 Attention Rules

writer实际精确v1 §3.1–3.2、4.2/4.3/5。以query-key和output-value feature交互提skipgram、distractor抑制与counting候选，规则排序只查top100×100并选梯度/权重；不是所有SAE feature的全局解释。假设重要key/value feature相关，原文明确可分离；多feature/位置交互及MLP忽略使描述不完备。GPT2-small第一层干预prepend distractor降低激活，仅保此操作反侧，不证下游行为必由该rule唯一决定或所有层神经真值。SAE训/规则搜索/读数与counterfactual费计入，2+1+2=5；还需§4 setup/评价样本最小核齐，不签完成。

## 2510.18135 World-in-World

writer实际精确v1 §2.1–2.4/3.1–3.2/4。proposal→WM候选rollout→revision/score→实际只执行选段再观察，统一API仅转text/viewpoint/lowlevel控制，不保证各接口因果等效。Habitat四类任务/特定episodes与RLBench四任务50各，posttrain scene不交eval；视频漂亮/视觉质量不认证action controllability、物理contact、policy效用。不同base/proposal/revision共同决定结果，more-data一epoch也改变总训练计算；inference候选多的相关性不授无限scaling law。panorama转换损分辨率/收益不一致、manipulation提升有限/长horizon和动力学未来，所有候选WM、revision、posttrain与真实执行费均计。2+2+2=6，visual quality/action control/closed-loop utility分责，待Ch25实际已有覆盖，不采普遍替simulator。

## 2510.18315 Sorting representation

writer实际精确v1 §4.1–4.3/5.1–5.5/6.1–6.3。475小transformer/PPO/H100、6/8元素枚举，维2–128与训练步1/2/10M；accuracy是correct swap比例，不是所有真实任务成功。order metric原W为QK/sqrt的**softmax前**相似度，别当概率attention；更大维继续改善readout但accuracy较早平，成功agent子集和长度8未收敛人口分开。top2与order相关不证唯一内部算法/环境world model，未做表征因果干预/鲁棒迁移，原local-greedy故事不转一般定律。训练/全部seeds/枚举及解释费计入，2+1+2=5，仅能力/表征读数不同验收，待Ch5实际已有覆盖。

## 2510.18795 ProCLIP（支持）

writer实际精确v1 §3.1–3.3：LLM embedding先离线提取，stage1 MLP把其投向CLIP text原空间，以instance+pair-distance继承；stage2 InfoNCE调vision与projection，EMA vision teacher加同类regularization。不是LLM全文参数在线继续训练，也不是所有空间数值等价；stage1旧知识与stage2新目标约束不同，额外text提取/EMA与双loss费存在。reader关键实验/反侧待到，普通项，不签Evidence。

## 2510.18114 Latent discrete diffusion（支持）

writer实际精确v1 §3.1–3.2。v1名LDDM、latent仅continuous（discrete留未来），不能把current Co/Di-LADD反投。token/latent独立forward noise，FUJI双通道联合denoise、SEQ先clean latent再condition token，仍各channel内部factorized。fixed encoder variance1e-4、loss ramp与unit norm防latent增幅SNR gaming，ELBO端点项实际忽略且权重可改，不由理想ELBO自动签真实训练精确似然。reader理论/评价反侧待到。

## 2510.18087 Planned Diffusion（支持）

writer实际精确v1 §4.1–4.4。AR先生成topic/长度计划，async内bidirectional/跨span隔离直到sync，plan tags验证只格式不证语义独立；同步后才消费完整span及新cache。steps ratio乘最长span长度，不把它当固定总NFE；未定span内KV不能冻结，后续plan可读前段cache。Gemini标SlimOrca、词表tags/padding/attention-mask需成套训练，不是直接换sampler或原AR分布恒等。reader关键评价反侧待到。

## 2510.18457 VFM-VAE（支持）

writer实际精确v1 §3.1–3.4。冻结VFM多层feature经可训投影成Gaussian latent，decoder global style每scale、spatial仅低scale注入、逐scale ToRGB监督；冻结VFM不等整个codec不训/latent无信息损失。representation KL/VF与L1/GAN/LPIPS多目标，多层取出/投影/decoder/对抗训练均计费。reader关键评价反侧待到。

## 2510.18353 Diffusion-DRO（支持）

writer实际精确v1 §3.1–3.4。最终图reward换成整trajectory surrogate，expert正/当前policy负的ranking，periodic同步policy/learned概率模型与thresholded margin避免过拟合。没有独立标量reward网络不等不需要偏好/负样本或只维护一个模型；原段称“eliminates negative samples”只对成对人工负样本，不抹online policy负。理想density推导/forward专家trajectory近似不替实际收敛保证，reader直接理论/实验反侧待到。

## 既成支持与关键反侧接合（恢复后保存）

18795/18114/18087/18457/18353：R19已实际到达，分别限定分类/检索取舍、ELBO与实际loss/双channel总NFE、计划独立假设与质量/时延不等运行点、teacher/codec混杂与proxy语义、trajectory下界/测试选点/online负样本。支持与反侧合用，均2+1+2=5，普通Books比较继续；不重复reader域，不以旧“待到”作当前未读。

## 2510.18314 / 18204 / 18131 / 18563 / 18123 / 18541 安全支持

writer此前实际精确v1支持，现保存：Genesis§3.2–3.5把成功策略log转可检索库并继续进化；RESCUE§2.1–2.2从漏洞修复/CWE归纳及PDG双向切片提因果/接口检索线索，draft反馈多facet/RRF消费；BlueCode§3.3知识constitution加LLM筛查后动态测试再融合；TrustParadox III-A/B将敏感集合和任务必要aggregate分账且tau同时改变gate/冗余；SafeCoop§4.1–4.2语义/位置/时序多层检查，字段max后跨agent/层平均，并非单票否决；Backdoor§4.2高层机制是组合trigger在蒸馏数据少见仍可能由组成token留下teacher信号，不展开操作模板。关键评价/直接反侧完整复用R12/R13，未执行攻击/毒化/复现实验。各2+1+2=5；安全限制深入完成于所采用窄命题，Books具体比较交reader W8，不默认安全通过。

## 2510.18313 OmniNWM

writer精确v1实际§3.1–3.3/4.1–4.3：RGB/semantic/depth共同panorama VAE/PDiT，预测occupancy再构造碰撞/边界/速度reward；自己预测的世界给自己规划打分不是独立物理安全证据。Plücker/reference intrinsics归一不证明任意跨camera metric几何。frame/view noise forcing；48A800、11.22B、batch48/NuScenes，planner主要150场景自身world，不能把对预测世界的改善当真实道路因果闭环。不同backbone/训练预算混杂，未采跨模型性能倍数；所有生成/occupancy/reward费计入。2+2+2=6，待Ch25实际已有覆盖比较。

## 2510.18165 Saber

writer精确v1实际§4.1–4.4/5.1–5.4/6.3/AppendixC限制：历史unmask confidence均值作阈值，旧token置信下降可被remask；c>=tau下阈值升高允许更少，正文某单调叙事相反，不照录。至少remask1可能撤销进度，不采形式终止/原分布严格无损。LLaDA8B/单A6000 48GB/长度256/block128/T0，五greedy运行非独立统计种子；质量/步数与代码测试仅局部，回退费另计。2+1+2=5，修订/commit与总步数分责，待Ch24具体比较。

## 2510.18337 MoT-VLA

writer实际精确v1§3.1–3.3/4.1–4.3采用相关段：冻结generalist与同级domain expert以global/local mask交互，expert motion hidden条件action DiT，不由token BLEU认证物理动作。主实验14B组合，1B只局部时延说明，不冒单7B无增参；300sim×3任务、50pick/place+200bussing，baseline不同预训练/finetune预算不能全归mask。推理幻觉仍会传播，真实controller保执行权。未核所有硬件时延表不采用速度保证。2+1+2=5，待Ch26实际比较。

## 2510.18744 Diffusion Buffer（采用范围）

writer实际精确v1 III-B/IV/VI-A–D/VII-A–C。不同物理年龄frame处于不同noise level，每hop一次NN不等每frame只一次求值或零等待；每frame在buffer累积步骤，DSM固定(B−1)延迟与DP可调d-frame是不同接口。原buffer继承[1]，本次只采用新预测/生成联合与延迟质量取舍，不称首次发明buffer。16k/STFT nFFT510 hop256/K128，EARS+WHAMv2 54h/A100~一天200epoch/batch32；OOD1.5h脉冲噪声是指定分布。匹配条件原DB可差于predictive，DP/g32增加参数且d=0逊SEMamba，优势须绑定允许延迟；文中部分时延公式量纲疑点不采。未读V-D具体BC-UNet则不采用其lookahead实现保证。2+1+2=5，待Ch24具体比较。

## 2510.18716 SSD

writer精确v1实际§3.2–3.3/4.1–4.6：以窗口外mass分head，local窗口/sink与semantic heavy-hitter/recent各自缓存；CFG条件/无条件KV-MSE差是相关线索，不是语义因果定位。Janus1/7B、24²grid/384²、CFG5、A10080GB、batch至256、GenEval553/DPG1065；大batch吞吐非单请求SLO，峰值memory比非全部参数免费，追踪/刷新buffer费计入。head角色阈值/模型/网格变化需重测，丢KV并非严格target分布不变。2+1+2=5，待Ch45实际比较。

## 2510.18113 Dark Patterns

writer实际精确v1 III-A/C、IV、V-A/D/E及VI/VII采用相关段：四自建站/14pattern/32tasks/88单pattern情景、六agent各三run，logical action-trace条件+录像核task与susceptibility；手建ID/可控后端不直接等真实开放web。四象限DC/DF/EC/EF把完成与受骗分开，低DPSR可能由early-exit或interaction paralysis造成，50随机EF定性支持而非全体因果证明。UI代码/vision变化还改变可识别性，不能只归视觉更安全/更差；tailored prompt仅两scenario/三run且仍可受骗，不授通用防御。GPT4o主配，API/backend版本/生产base-rate未闭，不采泛排名。2+1+2=5，评价分母/暴露与安全分账，待Ch66实际覆盖比较（writer承担，W8九项之外）。

## 三项必要缺层已补足

BadScientist18003：实际补§4.2、5.1–5.2及限制。50真实+50合成的检测人口，ReD警告增加仍可能提高accept，DetOnly偏召回高FP；AI-generated标签不等fabrication，GPT5 concern judge不是人审/真实性真值。三同提供商reviewer的浓缩界不能证明错误独立/事实正确，警告与gate分离的局部反侧可保，2+1+2=5。WebSeer18798：补§3.1，九集各512+Bamboogle125，LLMjudge/单提交，训练Wiki限域而推理live Google/Jina，12prompt×8trajectory/至30turn、100step/60A800GPUh；population/工具变化限制公平比较，标准必要域足够。AttentionRules18148：补§4setup/A.2；正文100正负/两split与附录150/三split有口径冲突，不合并数量；top激活对随机零值偏好recall，binarization丢幅度且无正预测precision定1，不把F1当全激活或行为解释。两者各5分，支持/反侧足以窄采用，不再普通待读。

## 2510.18491 Crucible / 18725 SemiLoRA / 18291 GeoDiff 重开后必要

Crucible：实际§3.1–3.3/4.1及本次补4.2–4.4/5。代码逻辑改写+Bayes数值调参形成优化可达性量尺；V(E)归一化/环境similarity及权重由当前搜索器/预算构造，不是算法内在普适potential。Claude3.7、Bayes0/10/20与reflection1/2/3预算，ABR/调度/CartPole；纯LLM约60%情景无显著收益、加Bayes仍约20%，不同state/搜索预算不能授简单算法永远更可调。WiFi/Dashjs局部不等生产部署验收，无黑盒内部逻辑修改。2+1+2=5，待Ch66/80实际比较。

SemiLoRA：实际§4.1–4.4/5/6。bartMNLI句级domain伪标→r16 domain LoRA，推理以embedding centroid cosine路由，非仅换小语种主题；全域混合baseline在general/wiki-news反更强，分域标签/数据和adapter容量共同变化，不保普遍胜fullFT。NLLB600M/两A10080，仅英→爱尔兰语高质量数据，webcrawl/反向/其它任务未测；伪标/centroid维护/路由费不免费，不采未测latency。2+1+2=5，待Ch30实际比较。

GeoDiff：实际§3.2–3.3/4.1–4.2/5.3与补7.2/7.3/9/11。已知pose下光度backwarp指导latent与positive scale/shift，正则限制逐timestep梯度；分辨率/scene与specular illumination影响约束。更高depth优化可改善photometric却恶化AbsRel，故consumer一致性不等metric真值。RTXA6000约7s/768且不含prep，不授实时。2+1+2=5，待Ch25实际比较。ParaVul17919只日期跨界保留，不由此抹最小机制已读层。
