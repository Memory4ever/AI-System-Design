# 10422 World2Act：必要Source / actual Ch26 owner / 两段PRE

只03-13补Mar12 BJT自然日。第三完整题摘与DATE3日级夹证独核有效复用，本次重对SUP_ABS3_10422.txt exact-v1题名、九作者、完整AB/history/Comments仅project：SubmittedMar11T05:11:44Z、SUP_DATE3_10422.raw actual registeredMar12T02:01:05Z；Updated不作公开依据。DataCite题名较早简式而同ID/日期身份未变，不据它授新事件。v1没有当前撤回/纠错/具名venue信号，May29v2不扩前版对比。官方 https://arxiv.org/html/2603.10422v1 GET200/355193bytes/UTC2026-10-10T02:01:41.235607Z，SUP_CORE_10422.raw/txt/manifest/result保留。

## 实际增量 / 拟评分

旧生成视频→IDM伪动作或reward链容易传递pixel artifacts；直接共生成action/video又耦合大的表示→本文先把生成视频latent与真实动作chunk映到固定共享bridge，再用这组固定表示对比监督当前真实rollout动作，更新冻结基础VLA之外的residual→预测prior是后训练信号producer而不是部署时每步必须显式生成的计划。这是**生成目标、对齐producer、动作更新consumer与真实执行反馈**的具体边界，不因WM/robot标签或InfoNCE/residual成熟原理准入。

拟 **2+2+2=6**：固定video/action bridge→在线residual action更新的替代接口2；跨生成先验/动作后训练和环境rollout分责2，非由两个模态名称抬分；固定teacher/bridge版本、chunk支持与实际执行验收是可复用接口约束2，不借物理真值/anti-collapse老原则抬3。actualCh26具体缺口触发必要局部深入；结论只采用这个受限训练接口，不采latent免幻觉、物理可靠或architecture-agnostic保证。待非准备者Source/owner/PRE，不formal。

## 必要原件实际读取与采用边界

精确v1 §3.1–3.3完整400–562、§4.1–4.2全部562–1212（Eq1/重建/全部stage职责）、§5.1–5.4及§6完整1213–1904（Tables1–4/settings/直接限制）、A全backbone选择/S1 2760–2894、B全必要S2–5/Stage1/跨task/实机与延迟2895–3255、C全部网络表S6 3256–3540、D失败3541–3586、E数据/完整schema prompt3587–3703。G决定区别只看已有直接说明，不扩所有旧论文。Figure3/5/7/8/S3/S4只caption及正文描述，没看pixels/视频；不认证曲线逐点单调或实机各任务点值，无代码/复现主张。宽owner rg截断只发现，目标局部另完整读。

Skill数据：gripper aperture闭合阈值δ≥Δ=.05m作为contact标记，完整non-contact→contact周期分段。E说明手工task schema+DeepSeek用给定indices过滤false positive、逐序匹配，不能造新frame；缺step丢弃。96.2%/86.9%“同步”定义只是subvideo数与atomic prompt数一一对应，不认证事件接触真实、语言/行为语义或时间精确。Door等非抓持会破分段。E的114192/67593 RoboCasa和11782/2007 LIBERO是切片增长，不是同等新独立轨迹。多视图2×2拼图不保3D一致。推理last-generated-frame→next-skill条件再concat会传播旧误差；本WM文本/首图条件，不提供同状态多action因果后果模型。

Stage1冻结finetunedSkill-WM，video adapter CNN+pool+MLP与action adapter MLP/train action decoder重建真实chunk。§4说extractvideo latents，B明确**Gaussian去噪生成latent**，不把它补成真实观测encoder标签。M=4 action frames拼chunk与temporal-compressed视频对应，D=32；bidirectional InfoNCE按同时间chunk cosine均值，easy不同skill/hard同skill其他demonstration（ratio.25），reconstruction+contrastive训练30k/B16后冻结两个adapter。重建只约束actiondecoder，不验证生成video dynamics；cosine相似与memorycompression不证明因果时间、唯一动作或所有信息保留。

Stage2冻结baseVLA与bridge，由真实current image/proprio+baseaction latent输入小residualnetwork，decoder从原动作重建初始化后为residual fine-tune；执行base+residual动作chunk M=4 open-loop，再真实s(t+1)更新直到trajectory。WM从rollout**initialization**生成目标视频latent，不读取每个实际后态作正确性gate；fixed Bv/Ba比较本环境的imaginedtarget与实际policy动作序列，平行不同初态同task作negative，不用成功/reward更新residual。reward-free指这项objective，不是无需真实rollout、demo/schema或安全反馈。环境状态对参数的反传/重新计算、variablelength/padding与clockalignment、actionbounds/安全限制没有在所读段闭合，不补造exact environment policygradient或可执行安全recipe。baseweights冻结不保augmented行为或原全部能力。

强“pixel失败但latent被动动力/接触准确”没有独立state对照：D列duplicatehandle/multiview消失/missinghandle，只是视觉例；另**TurnOffStove**想象抓到转动而真实VLA未抓稳，直接说明latent目标不等接触可达/执行认证。本包不否定局部实验，不推造假，隔离“latent自动可靠”与“同env正例即成功”保证。

## 关键评价 / 反侧 / 预算

Main50trials/seed×5seeds平均SR，Tables无CI/Std，不自行统计显著。RoboCasa GR00T1.6-ft .701→.726/DreamGen .705/VLARFT .710/Ctrl .698；Cosmos .657→.663仅.006。LIBEROGR .970→.981，但**Long .943→.940反退**；Cosmos .985→.986仅.001，Spatial .981→.980反退。因此平均提高不保所有horizon/任务或任意backbone。T4 Base→Skill GR .715→.726/Cosmos .661→.663，不能由两项直接授architecture-agnostic。WM vs baseline data/trainsupport不同，不唯一归因latent免artifacts。

S3chunk-biInfoNCE .726、single .720/marginal .707/global .693支持当前细时间匹配选择；没有独立物理真值或matched全compute因果证明。S2residual6.8h vsLoRAr32 15.3h/r16 14.6h，含不同初始化/optimizergraph，不能说完全配对纯结构更优；其时长不包括Skill-WM10k、bridge30k、生成/在线rollout/LLM全部费用。A各backbone 10k但默认大小/LoRA/fulltraining不同（LTX13B r128/Wan5B r32/Hunyuanr8/Cosmos2Bfull），S1IF QwenVL/PA VideoConPhysics只是指定judge，不授真实接触safe。MI210“48GB”按原文保留未替改硬件规格，不外推全单卡预算。

WM8AMDMI210、allbaseline eval RTX409024GB；主文每sim1000synthetic trajectories、GRft1000expert，Tables1 per-task原real/synthetic数不同、须分母绑定；1000何时含initial expert与onlineactual rollouts/全部step统计未闭合。C A12RoboCasa/A7LIBERO、M4/D32/proprio53/img256²/video16×60×104，residual2layer4head/3tokens。Precision、wholeWM/bridge/residual优化超参、fullstep/effect budget/训练硬件与显存峰值/whole闭环p95SLO Not Disclosed。

S5GR274.1Hz3.6ms→251.9Hz4.0ms；Cosmos20.8Hz48.1→20.5Hz48.8是**预测一个action的时间**，不是完整相机/调度/控制器deadline或免费残差。实机FrankaResearch3/thirdcamera/GELLO20demos每task、100generated/20trials每task×3，原文平均+6.67个百分点但Figure7点值未视觉核；不会声称普遍真实提升。B“CloseDrawer”实际玩具microwave门/磁扣，Pick+Place两atomic分别训练而测试需一次完成，不能与原sim机械任务直接合并。真实success是指定评判，不证明碰撞/rare-event安全/全部能力保持。

## actual唯一owner / 两段PRE

ROADMAP `MULTIMODAL-EMBODIED-VLA` Ch26。actual完整343–397：BC/Qgate与可逆likelihood→World-action model→explicit/joint/direct三接口→GigaBrain条件mask→双时钟joint/actionfreeze→RTPretain/replan→MVISTA固定future反求latent两完整段→Future-to-Action标题；另外26–36跨本体latent-goal完整分责。已有生成prior/部署prefill、假设future与真实反馈分账，不等**固定video/action bridge在posttrain中对比actual action rollouts，baseweights冻结但residual改变执行**。Ch25 actual276–322 inverse/forward/latent action(effect reference)完整交接拥有transition/表示可辨识，不承载此instruction-target监督的policy更新；Ch23表示、Ch27schema数据、Ch31更新实施只是handoff。唯一Ch26，非StructuralCandidate，不声称已吸收这组新实验。

拟MVISTA两完整段之后、Future-to-Action标题之前窄两段，保留旧explicit逆解路径与后续因果使用压力；需root共享窄写/实际nonwriterPOST才formal。

### 逐字PRE

生成未来也可只在后训练中提出动作目标，而不进入每个在线控制 step。一个受限分支先把生成视频 latent 与真实动作 chunk 通过重建和逐 chunk 对比训练映到共同空间，再冻结两个 bridge；部署基础 VLA 的权重不变，额外 residual 根据当前观测、proprioception 与基础动作提出修正。训练时执行这组修正动作、回收真实 observation，以同一初始化产生的想象 latent 对齐实际动作表示；不读取环境 success reward 更新 residual，也不等于没有真实 rollout 或已证明行为无损。视频 teacher、bridge、chunk 时间与本体坐标必须绑定，生成目标只提监督，不拥有接触真值或动作执行权。

[World2Act 的有限控制对照](https://arxiv.org/html/2603.10422v1)支持这条训练接口，但同环境 latent 正例与更高 cosine 不批准动作成功：平均收益伴长 horizon 反退，想象抓握成功也有实际未抓稳的案例。夹爪索引与 schema 的数量匹配不证明语义同步，首个生成片段作为下一片段条件仍会传播错误。世界模型、分段标注、bridge 预训练、在线环境 rollout 与 residual 求值都付费，单次 action 预测速度不是闭环 deadline；时序、接触或行为回归不通过时，保留基础 VLA、真实动作监督、显式短 future/逆动力学与独立 controller，以真实环境反馈验收，而不由 latent 空间批准物理安全。<!-- source-family:SF-2026-ARXIV-2603-10422 -->

## 停点

6分必要Source/actual owner gap及逐字两段PRE已由root非准备者实际核通过，root窄写Ch26两段；本作者非Books writer实际完整局部/本人注回必要源POST见SUP_POST_10422.md，root已实际回读接纳、本人注同步PASS/锁释放，正式整合完成。未授DAY，普通未看artifact/像素不外部化，不扩所有录像/附件/前版或其他日期。
