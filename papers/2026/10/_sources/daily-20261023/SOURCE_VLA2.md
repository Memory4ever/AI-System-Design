# Oct23 Daily — SOURCE_VLA2

仅本日29692/29702/29716/29730/29866/30097/30105/30117 exact-v1。公告日、完整题摘、准入及已校准分复用[ARXIV](ARXIV.md)官方list mapping，不第三审、不读别日。必要Source审阅不等复现；root唯一Books/Report/State写者。PRE待独核与保存，未签POST或DAY。

## X1 2610.29692 FlowVLA — 2+1+2=5；必要Source；拟整合

- [v1](https://arxiv.org/html/2610.29692v1)，实读III-A–D、IV-A–C/表I–III、V；[原件](vla2-source-2610.29692-v1.txt)。
- 图像/关节相似时持续流动物理量仍变。冻结GRU observer从快32样本/.25s与低通32样本/1s及joint产生8维belief；目标只给pour prompt/比较器，不给估计器。shared π.5分approach/pour/return；阶段边界action-loss mask与完整return anchor分开，不照抄训练配方。四head completion估计结合flow hardgate、积分及受限mass修正/monotone max；tail GRU预测固定return造成的剩余流量，Mhat+That对goal触发return，无足够历史则仅Mhat，stall一次重试后失败退出，切stage废旧chunk。
- 608/75/75主数据分割共758，scale10Hz仅离线label/验收，不线上读取；1453data-scale额外695仅π.5控制。20k训练/b32；重量身份仅load baseline校准前95.6g后19.9g，运动/晃动使wrist不可直接当电子秤。13.15g是79个完成mass试验的goal-balanced MacroMAE，不是123attempt全体；84抓住，端到端完成64.2%，±10%在完成中83.5%，全attempt联合53.7%。无gate的端到端66.0%高于full64.2%，不宣称全指标增强；固定.2s尾巴15.79g、只current19.06g有限支持tail预测。heldout goals仍同主模型；其他容器/液体分别训练，不是零样本转移。传感/离线scale标签、observer/tail、主policy、ensemble及实机失败全部付费。
- actual owner Ch26 `MULTIMODAL-EMBODIED-VLA` GoalVLA两段已管stage/target-padding与runtime stale suffix不同，但未管“观测近似不变而累计量继续变、撤回仍有尾流”的停止条件。只补累计量/停止后效，不新增pouring框架分支。
- 逐字PRE，完整“零动作 target 也不证明机器人会真实停止...”段后、完整“Action chunk还改变了‘表示可解码’的对象...”段前：

> 阶段结束还可能依赖持续累积、但当前图像几乎不变的物理量：可由带时间的力/本体反馈维护流量与累计量 belief，再预测执行既定撤回动作后仍会发生的尾量，以两者之和提出提前结束；阶段切换同时使旧 chunk 失效。[FlowVLA 的受限倒液对照](https://arxiv.org/html/2610.29692v1#S3)把目标比较与量估计分开，电子秤只作离线监督，不让 belief 变成传感真值。尾量依赖具体撤回轨迹、液体与标定，完成试验内的质量误差也不能代全尝试成功率；新容器另训并非零样本。传感/标签、observer、尾量与完整策略训练均付费；反馈或后效模型失准时，缩短 chunk、重新取证并回已验反应式控制/停止接管，不用预测达量批准物理安全。
>
> <!-- source-family:SF-2026-ARXIV-2610-29692 -->

## X2 2610.29702 CausGround — 1+2+2=5；必要Source；具体NC

- [v1](https://arxiv.org/html/2610.29702v1)，实读§3.1–3.3、§4.1–4.6/表1–3、§5；[原件](vla2-source-2610.29702-v1.txt)。
- 冻结MLLM提取对象属性/关系，从受控前置变化及成功失败经验提generic/instance preconditions/effects；goal backward effects检索与semantic检索并集合Ktask，初始建一次，planner每步仍读更新state。名称causal不证明SCM识别/完整物理guard，正文未给“稳定区分”的充分样本/阈值实现。
- VirtualHome用AI编辑render修正状态不一致；RoboCasa是atomic annotated skill高层阶段，不等原始motor policy部署；SWITCH四类是识别检验，bread/microwave真机定性不是全试验与SLO。samebackbone/input/action/frozen不等全部检索/context调用等预算；full62.7 vs仅knowledge53.3不足以证明现实state正确。抽取、受控经验、检索与新增context全部计费，真实条件失配仍独立取证。
- actual owner `AGENT-PLANNING` Ch79已实读开篇typed plan/precondition/expectedstate、partial observation与2603.17831完整两段：召回相关性、当前state相容、规则冲突和行动授权分责已具备。本文factorized符号表示与经验抽取是该producer的组件实现，没有建立更强因果/物理资格，不为框架名新增同义段。新有限实证留报告，NC不改分/删候选。

## X3 2610.29716 SpatialDex — 2+1+2=5；必要Source；具体NC

- [v1](https://arxiv.org/html/2610.29716v1)，实读III-A–C、IV-A–C/表I–III、V；[原件](vla2-source-2610.29716-v1.txt)。
- 人视频HaWoR/MANO近似metric手尺寸+VGGT-Omega depth/pose；跨整段/双手拟合共同scale、每帧刚体变换，再将未来wrist/geometry变到当前camera，finger保局部。scale不是深度/手尺寸真值。RGBD/intrinsics将valid patch lift为未归一metric点，Sonata联合几何编码再均值回patch，dual-gated residual经20k warmup；初始化/残差不保证训练后保原VLM。辅助future Chamfer目标来自这份估计，finger head消费预测wrist；robot仍适配actionheads并需RGBD部署，不是RGB-only。
- 1M视频、32A100/72h/b256，5步去噪16action/执行8/5Hz。sim9task×3seed×50，real6×10、每task50demo；sim76.3vs59.8但bucket79.3<84，real49/60vs26/60不授production。
- 强matched控制是六任务同视频/target/compute且同RGBD finetune接口；motiononly58.9→full73.1同时增加geometry输入与target，14.2pp不能归单一组件。per-frame63.8→sharedscale73.1支持当前配置跨帧标定，但估计噪声、geometry/forward目标与wrist条件各有局限。预处理、teacher/深度、全预训练/适配和闭环回归计费。
- actual owner Ch26已有camera/metric坐标producer→consumer、humanvideo2604.20841可见target非完整geometry，以及geometry/motor2610.28164完整段的辅助监督与真实动作分开验收；本法共同scale与输入/target是具体组件选择，未证明唯一表示/标定真值。现有链已承载其长期义务，NC，数据与控制反侧留报告。

## X4 2610.29730 Kernel variance — 2+1+2=5；任务覆盖/within-rank反证定点深入；拟整合

- [v1](https://arxiv.org/html/2610.29730v1)，实读§3.1–3.4、§4.1–4.6/表1–6、§5.1–5.8、§6；[原件](vla2-source-2610.29730-v1.txt)。仅必要域深入，不遍附录。
- frozen SmolVLA embedding上的GP conditional variance，无回归输出label；support标准化/PCA/whiten后核几何score，不是真failure概率。policy更新后重新embed/refit。Ctx一次prefix forward，Dec第9/10 denoise hidden需九步；exactCholesky的立方拟合/平方存储保留，>10k近似未验证。raw modality选择性部分由输入构造决定，fused错语言/scene交互不能当完整OOD认识。
- 3seeds，1437 demos含30其他任务和target0–2；15轮每轮5query/4kupdate，candidate包括已取过数据。75新demo vsRandom46.3等包含去重收益，非纯选择精度。全局calibration/referral在共同Random臂round0/10、10tasks×50init×3执行，paired supervisor哈希输入；任务计数null可匹配/胜learned scores。round0 variance约71–76%任务间、仅3–7%同任务内；round10同task增但44%执行随机性。
- global nAUC约.50/.51 vsVFD.48且差CI含零；within-task最佳Dec.11±.03、Ctx.05/VFD.07。reference任务计数并非可部署uncertainty；nAUC是相对random/带符号supervisor gain oracle，不是risk概率。跨重复hindsight一run预测另两run也仅.27，不应以完美oracle1判断全是模型失败。
- 扰动实验单独训练全部task政策/不同support；label-preserving shift detection不是控制伤害，harmlessnoise可告警。robustsupervisor训练同9扰动families，clean两者79/perturbed58vs71，occlusion supervisor还-9pp；不是unseen corruption通用救援。within nAUC Dec.46vsVFD.40差.06[.03,.10]、Ctx无显著差；逐扰动多比较未校正、3seed及hierarchicalbootstrap不含未见任务。
- “50×”是500条件评分Ctx.8 vsVFD38.8 GPUmin，不是全policy speed；acquisition1minvs43.8另有共同primary37min/轮及第二policy4GPUh，不能忽略总费。无真实humanhandoff、告警提前量/falsealarm/实机安全。采用任务间/任务内/重复随机性拆分，不采用通用GP部署recipe。
- actual owner `PLATFORM-EVALUATION-SYSTEM` Ch66现2610.25846完整段管confidence对象、resolution与prompt/null，但未分机器人任务覆盖与同任务episode可转交价值；只补这份具体评价盲区。精确位该完整段后/2605.20502联合sensor完整段前。
- 逐字PRE：

> 控制任务的 uncertainty 排名还应拆成任务覆盖、同任务内排序与重复执行噪声：少示教任务整体更难，足以让只看示教数的 null score 获得较好全局排名，却不能指出同一任务哪次执行更需要帮助。[冻结 VLA 上的受限审计](https://arxiv.org/html/2610.29730v1#S4)因此同时做全局与 within-task referral，并跨重复执行检查单次观察的排序可重复性；核方差只是相对训练 support 的覆盖代理，不是失败概率。交给 supervisor 还须量其真实增益，shift 检出不等接管能救，部分扰动下 supervisor 反而更差。支持集重编码/拟合、重复 rollout 与第二策略全部训练/查询均付费，局部评分提速不替总费；排序、接管收益或分布支持不足时保原策略、简单 task-count 基线与真实反馈，不以高 uncertainty 自授物理接管或安全。
>
> <!-- source-family:SF-2026-ARXIV-2610-29730 -->

## X5 2610.29866 GeoMem-VLA — 2+1+2=5；必要Source；具体NC

- [v1](https://arxiv.org/html/2610.29866v1)，实读§3.1–3.3、§4.1–4.5/表1–4、§5/Ethics；[原件](vla2-source-2610.29866-v1.txt)。
- Qwen3VL4B/GR00T生成GeoPlan tokens，训练VGGT pointmap confidenceweighted目标与demo EEF未来轨迹共同规范到VGGT frame。辅助scene/EEF flow与原actionflow分开，非直接nativefeature向量对齐，但梯度仍可能改VLM，不称冻结。部署teacher/辅助decode移除，latent构造/检索/gate/consolidation还在。
- visual tokens/finalstate及geotokens双bank；currentquery仅读prior、读后写入detachedhistory；容量满时最相似相邻pair均值merge/取较晚timestamp，不是真事件边界识别或完整provenance，也不保无限事实。几何branch消融同时删目标/tokens/bank/gate，不隔离“间接优于直接对齐”因果；memory消融删全部历史但保当前geometry。
- LIBERO98.9vs无geo97.9/无mem98.2、RT91.17vs89.71/90.18；跨已发表方法协议不同，不纯同预算排序。16frame demonstration memory诊断非真实闭环，EEF mm与归一pointRMSE非同单位。两平台5tasks各60demo/10trial、平均78%不证泛化；horizon8/50与自适应执行需按场景记录。geometry标签、全模型训练、状态/检索与实机回归计费。
- actual owner Ch26 episode-scoped latent memory开篇/2603.12942完整段明确derivedstate/reset/压缩与freshobservation分责；几何consumer2610.28164区分训练表示与真实执行；Ch77 EventMemAgent2602.15329既有episode/event压缩的derived非fact边界。GeoMem的双bank和相邻merge没有改变这些长期接口，未证压缩保充分状态，不另为模块名添书。具体新证据/代价留报告，NC。

## X6 2610.30097 AtomicRL — 2+1+2=5；必要Source；拟整合

- [v1](https://arxiv.org/html/2610.30097v1)，实读§3.1–3.5/式1–10、§4.1–4.4/表1–5、§5；[原件](vla2-source-2610.30097-v1.txt)。
- PCC估计semantic boundary，不是envdone。一步TD residual仍含Vnextbootstrap；GAE product只在semantic跨界乘gate，后续atom成功κ=1/失败κ<1，局部trace并非全删；依赖事后subtaskoutcome、value target也随V+gatedA改变，不是线上预知未来或无偏信用保证。
- BATE依atom成功EMA调全task采样（仍有baseline1覆盖）及bounded withinatom entropy，不是独立均匀抽atom；optional shaping又加auxreward。PCC从150trajectories VLM标记+人修，500eval片段95.92准确/89.2 recall非安全证书；42.4ms未硬件/endpoint全闭合。边界错分会错传播，N连续完成判据也非physicalgold。
- 200优化轮不是已匹配全wallclock；LIBEROLong10×50、两骨干+3.6/+4pp vsPPO，CALVIN1000seq五步80.1vs70.6与avglen4.56vs4.36不同指标。real3×25trial、100expert/task加real2sim构建与辅助观测，69.3vsPPO61.3/SFT48，+21.3pp相对SFT不是PPO。弱fewshot初始化的累加ablation非fullfactor，dense SAPO89.0还低于SubR89.4。9task×methodcells simreal相关不认证真实动力学。标注/PCC、全部sim rollout/失败与训练、域构建及真实验证全付费。
- actual owner Ch26闭环SimpleVLA-RL完整段管terminal组信号、不训练critic，未承载critic-based GAE在semanticboundary选择性衰减，故仅补训练credit对象，非Ch33 GRPO owner。精确该完整段含marker后/“### Online Correction 可以把 Counterfactual Proxy 与真实 Residual 分开”及其首段前。
- 逐字PRE：

> 终局信用之外，critic-based 后训练还可用有噪声的原子阶段标签限制 trace 传播：保留一步 TD residual 与后继 value bootstrap，只在语义阶段边界，根据事后完成标签衰减失败后缀向前传播的 GAE 权重，并让 value target 与该 advantage 一致。[AtomicRL 的受限实现](https://arxiv.org/html/2610.30097v1#S3)不是把阶段边界当 environment done，也不证明已分离每步真实因果；错阶段或完成标签会把信用分给错误前缀。按熟练度重采任务、调探索与额外过程 reward 又改变训练人口/目标，不能全算 trace gate 的收益。标注/阶段模型、全部失败互动、critic 与策略训练均付费；边界或净收益不可靠时保普通 PPO/原奖励、可信示教和独立 controller，不让训练中的阶段完成批准真实继续执行。
>
> <!-- source-family:SF-2026-ARXIV-2610-30097 -->

## X7 2610.30105 ASTEROID — 2+1+2=5；必要Source；拟整合

- [v1](https://arxiv.org/html/2610.30105v1)，实读§3–5.3/算法1–2、§6.1–6.9、§7；[原件](vla2-source-2610.30105-v1.txt)。未审全部formal appendix，不采用误差界/Bayes-optimal保证。
- 固定隐任务z跨Kepisodes的BAMDP与一般POMDP分开。student先部分可观测onpolicy context；同z另取expert trajectory，给history+expertprefix条件监督expertactions，并非对student每步动作逐个DAgger重标。一般POMDP需在student访问状态某t接管采expert剩余suffix。测试只历史/实际观测，长于训练用滑窗；特权专家不需要探索，student可从条件下动作分布学信息收集。
- 本文informal posterior近似仍有compliance（contextsource与监督label独立）、自身历史coverage/误差等条件；posteriorpolicy本身不等Bayesoptimal，缺expert action支持的探测动作学不到，探索可不安全。不由定性理论给真实探测权限。
- 11env多数3seed，Habitat1/一wristRL2，特定testbudget/heldoutgoals。100×是环境步数，不含privileged专家RL/domainrandomization/全部label与拟合费用；真实仅proprio joint/gripper、10trial，不是vision/tactile通用部署。ClaudeOpus5.5 codeagent另含demo/perception/prompt预算，非全frontier不能探索；offline context对照也改数据/多样性，不能独占归因。未采用无法从主文文本精确恢复的figure逐项数值。
- actual owner Ch26 episode-memory段内2509.11481是student visitedstate→teacher逐状态重标；本篇用context与expertquery解耦，形成“专家从未展示探索仍可教历史条件动作”的真实gap。精确该完整段及独立marker后/TempoFit完整段前；不移交Ch79另建一般planning理论。
- 逐字PRE：

> 特权 teacher 不必在自己的轨迹中展示探索，student 才可能学会取证：先让 student 在部分可观测条件下采集自身 history，再在相同隐藏任务中另采 teacher 轨迹，以这份 history 和 teacher prefix 监督后续 expert actions。[ASTEROID 的受限分支](https://arxiv.org/html/2610.30105v1#S5)不同于给 student 每个已访问动作直接重标；一般 POMDP 还需从实际到达状态接管采后缀，不能任意拼接别处轨迹。学得的条件动作分布不等 Bayes-optimal 或可安全探索，teacher 未支持的信息动作、history 分布失配仍会失败。特权专家训练、student rollout、全部标签与拟合都付费，较少环境步数不等全流程便宜；未知动力学或真实探测不可隔离时保原专用策略、可审计观测和独立 controller/停止接管，不让历史适配取得物理试错权。
>
> <!-- source-family:SF-2026-ARXIV-2610-30105 -->

## X8 2610.30117 CW-WAM — 2+2+2=6；必要Source；具体NC

- [v1](https://arxiv.org/html/2610.30117v1)，实读III-A–C、IV-A–B、V-A–G/表I–II、VI；[原件](vla2-source-2610.30117-v1.txt)。
- 运动10D由观测TCP delta变base绝对pose；6D wrench是bias/toolgravity compensated且在对应预测TCPframe/绕TCPorigin。历史24interval/1.6s每段至多16wrench样本/timestamps/validmask；150interval/10s long memory，与recent重叠止于current。PC mask [Ai,Wi]下三角Wi可见Ai而非反之，所有future仍共同denoise，不证明真实物理因果。video/action/wrench有效通道分别归一、λ=1，frozenVAE+50ksteps，4Euler产24pairs/1.6s，不decodevideoRGB控制。
- 20Hz外admittance用同nominal TCP frame与origin下预测/真实wrench误差，taskmask/gains手调；半隐式积分有加速度/速度/位移限与积分antiwindup，并非物理全安全界。progress按真实TCP沿nominalmotion匹配，单调且不超scheduled，非真实contactphaseoracle；0.5s quintic/50msreplan供1kHzimpedance。RTX5090 query .5–.6s含预处理/后处理不含network；等待保持末nominalpose+contactfeedback，C2bridge不等最坏deadline证明。
- 450demos/8H20，22testepisodes的373windows openloop按episode/task分母、训练模型固定bootstrap；PC isolate在noLTM，LTM保PC，full位置/朝向略差于noLTM，非全指标最优。validnormalization独立控制只openloop，real WAM+wrench用padded，不能把real SR差全归架构。真实每contacttask20、每load10，都示教分布附近；peg25→70%/adapter40→95%与wrenchinput/模型变化相关。admittance pegRMSE4.8→2.7N/wiping2.0→1.3N是成功人口，SR不变；adapter full接触力更高反侧保留。wiping simple全20/20，complex85.9%是另6selectedpatterns。C2与一频率不能代端到端SLO；一般新物体/任务未测。
- actual owner Ch26当前2604.27224完整段已将未来接触声明为desired低层跟踪目标、与真实sensor/执行权限分开；2602.22088、2601.09988完整两段又已有wrench/frame/origin、慢policy reference/virtualpose→快admittance/grasp双环、任务方向/标定/多频费用与失配回退。CW-WAM把连续6D目标接进WAM和pairmask，是这些已覆盖接口的组件生产方式；没有改变独立反馈/提交链，也不证明PC是物理因果。有限预测/成功反侧留报告，不重复增加slowfast/wrench框架段，NC不改6分。

## 四项PRE的完整actual上下锚快照

只作写前定位，不等root实际保存或POST；若他人同期增补，root须核当前邻接。

### X1

上段完整：

> 零动作 target 也不证明机器人会真实停止或保持安全；预测 goal 的空间偏差、阶段标注与实际 interaction pattern 都可能使训练条件失配。[GoalVLA 的受限对照](https://arxiv.org/html/2602.10983v1)没有隔离 zero-padding 与 goal-offset/relabel 各自的因果收益，basic 设置还有成功率退步，world-model 训练、goal 生成与 action policy 成本亦需分账。阶段标签或目标不可信时，重新观测并缩短 chunk，保留原监督、reactive policy 与已核 controller；不能由结构相似的 pick/place 任务结果授权开放环境或跨 embodiment 的物理提交。

下段完整：

> Action chunk还改变了“表示可解码”的对象：当前观测中的量可由固定probe读取，但执行一段动作后的量应写成ψ(Fu(x))，测量方向会随候选动作u变化。受限control-affine系统可用action path的signature记录有序作用，再与state的Lie-derivative系数组合成action-conditioned linear probe；uniform逼近依赖可达域、解析性、有界控制和足够短horizon。它是可构造表示的存在结论，不证明真实视觉state可识别或预训练VLA已经学到该坐标，扩大signature阶数也要付表示/计算费用。

### X4

上段完整：

> 比较confidence之前，还应先问三路读出是否测同一对象：自报分数依赖提问格式，prefill probe可能预测的是未来回答分歧而非正确性，多次采样agreement又支付另一份调用预算。[一项受限测量审计](https://arxiv.org/html/2610.25846v1#S4)中，很多浅层onset未胜prompt-only词面基线，较细层扫描还是看过粗扫描后设计的follow-up，不能把它写成模型早已知道真伪的深度。校准排名也须用相同可用item人口，并同时看resolution/区分力：分数都靠近base rate可有较小ECE，却不善于选择答案；换bin数、阈值或混合cell又可改变表面结论。probe、标签、格式、population/split与校准规则须共同冻结，保surface/null对照与未测的degenerate cells；采样、hidden提取、probe拟合和独立人审都计费。读出资格或迁移未建立时，保留任务verifier、简单校准基线与Unknown，不让一种低ECE或更早AUROC自动取得风险门禁权限。<!-- source-family:SF-2026-ARXIV-2610-25846 -->

下段完整：

> 多个sensor联合告警时，单路校准分也不能直接共用原阈值：可先把各路分数映到同一ID参考分位，组内取最小值后重新校准，再对组间最小值按联合误报预算选阈值。一个[有限多encoder分支](https://arxiv.org/html/2605.20502v1)采用这条两层组合；同一阈值下“任一路告警则联合告警”的集合包含，并不保证同FPR下继承最强检测力，因为维持联合FPR通常需要更低阈值。独立uniform两路、α=.05时，单路阈值.05而min阈值约.0253，分数.04/.9可被前者检出却被后者漏掉；相关sensor更不能照用独立Beta零分布，最终min也不是uniform。编码、各density求值、联合校准与独立shift回归都付费，少参数和较好AUROC不替误报、漏报或完整费用验收；相关性、人口或未知shift失配时，保留单路/简单联合基线、真实误报测量与Unknown，不让组合告警自授开放环境可靠性。<!-- source-family:SF-2026-ARXIV-2605-20502 -->

### X6

上段完整：

> 若 VLA 已能以可计算 likelihood 的离散 action tokens 采样，闭环训练还可以对同一任务采多条真实模拟轨迹，以终局 outcome 的组内差异更新整条动作策略，而不另训练 critic；相同任务/初态、policy revision、实际执行的 chunk 与 reward 身份仍须绑定，终局成功不提供每一步的独立因果信用。全成功或全失败组没有这种相对信号，剔除它们又改变训练人口，必须记录被跳过的任务、重采与停止预算。[SimpleVLA-RL 的有限对照](https://arxiv.org/html/2509.09674v1)保留了零成功先验仍零成功的反侧，不证明动态过滤能从任意初始化自动启动；categorical head、输入视图与重新 SFT 的改变也不能算同一原 checkpoint 的免费升级。示教、全部渲染/失败 rollout、组过滤和完整参数训练均付费，binary success 还可能奖励不安全的捷径。初始支持不足、组内无差异或真实闭环质量失配时，保留可信示教/直接 BC、原策略和独立 controller，不由模拟成功、少量示教或新轨迹标签批准真机安全。
> <!-- source-family:SF-2025-ARXIV-2509-09674 -->

下段完整：

> ### Online Correction 可以把 Counterfactual Proxy 与真实 Residual 分开
> 
> 只用模拟 counterfactual reward 更新 driving policy，样本便宜却会继承 future evaluator 偏差；只等真实失败再学习，证据可靠但代价高。中间路径先用 counterfactual proxy 形成候选更新，再以同一 visited-state distribution 上的 grounded residual 校正偏差，并用 EMA/anchor 限制策略突变。Proxy 提案、真实 residual 与 deployment policy 必须分别版本化，训练不能把模拟未来当作环境事实。

### X7

上段完整：

> Episode 内的历史状态还可以通过多本体教师的动作监督形成，而不先显式输出动力学参数：在模拟中为每个固定本体训练读取完整状态的teacher，先用teacher轨迹预热，再让student按自己的动作采集轨迹，由对应本体teacher对当前访问状态重标动作。部署student只消费实际可得观测与自身动作历史，递归状态承担条件适配，不获得teacher的真实motor state或本体参数；[受限四旋翼对照](https://arxiv.org/html/2509.11481v1#S4.SS2.SSS2)支持这份采集者、监督者与部署输入的分工，不证明隐状态唯一辨识真实动力学。参考轨迹经误差输入造成的变化也可能被误认成物理响应，传感器与固件延迟因此必须进入训练支持及真实闭环验收，不能只扩大静态参数范围。多teacher训练、当前student rollout、重标、状态估计与实机回归全部付费，模拟probe可读、较小网络和有限长轨迹均不签发任意时长、完整deadline或物理安全；原奖励与滤波数值式未闭时不照录成执行recipe。历史、时序或本体支持失配时，重置受影响状态、刷新观测并保留已验专用controller与停止接管，不让适配latent替代真实反馈和安全边界。
> <!-- source-family:SF-2025-ARXIV-2509-11481 -->

下段完整：

> 冻结的单帧 VLA 还可把历史条件接到 prefix attention 内部，而不另训 curator 或追加图像 tokens：仅在选定层保存带帧时间的 pre-RoPE K/V FIFO，以当前 K 在同一 key 空间读取历史 K/V，加 frame-gap recency bias，再 residual 加到当前 K/V、按原 per-token norm 重缩放并使用当前位置编码。层集合、缓存寿命、寻址、时间偏置与注入是五个独立选择；这改变当前 attention 状态，不是标准 AR 历史 K/V 的无损复用，保 norm 也不保方向、分布或控制安全。[TempoFit 的有限 VLA 对照](https://arxiv.org/html/2603.07647v1)中，全层读取、更多历史及不重缩放均可退步；当前项何时入库、reset/refresh 与 self-match 协议未完整披露，不补成可执行通用实现。缓存、检索、重缩放及原模型训练/维护均计费，模型逐步平均时延不替代传感器—动作 deadline；旧状态失配或动作回归时，清理受影响记忆、重新观察并回单帧/短 chunk policy 与真实 controller，而不由免新增训练批准物理提交。<!-- source-family:SF-2026-ARXIV-2603-07647 -->



