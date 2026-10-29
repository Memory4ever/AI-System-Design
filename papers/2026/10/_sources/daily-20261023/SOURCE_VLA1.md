# Oct23 Daily — SOURCE_VLA1

本批仅 28880/28882/29161/29168/29203v1/29246/29264/29282。Oct22 BJT 公告日、完整题摘与准入/初分复用 [ARXIV](ARXIV.md) 已有效独核，29203不用次日v2。只写本批 source/原件；root 唯一 Books/Report/State writer；PRE不等实际保存或POST。

## V1 2610.28880 R2Sem2R — 2+1+2=5，必要标准 Source；具体 NC

- [exact-v1](https://arxiv.org/html/2610.28880v1)，实读III-A–F、IV-A–E/表I–II、V限制；[原件](vla1-source-2610.28880-v1.txt)。
- 一个RGB示范仍需phone扫描、实物metricheight、静态tableplane、相机/robot初始化和cousin照片。DINO-distilled splat render-compare tracking，手遮挡mask；HaMeR经metricdepth对齐和depthoffset搜索，carry frames采100 grasp扰动并筛collision/antipodal。Wholeobject semanticICP后，VLM挑关键帧/region，feature相似扩展功能面并20倍加权ICP；把manipulated及target cousin共同映射，再转grasp/IK，不是任意新对象自动学真实接触。
- IsaacSim kinematiccarry与MuJoCo contact两条分开；后者仅接受settled目标成功、前者更photoreal，主结果除指定对照均IsaacSim。2000保留episodes/约2h RTX5090包括生成失败，但另25min预处理、共同30minrobotsetup、policy训练都不能省略；生成训练58–93ksteps、teleop30k、类别coverage16mugs9machines vs4×4teleop，不把不同人时/步数当等预算因果。R2R2R+同pipeline/同2000/同源视频、仅无cousins，较适合限定semanticaugmentation。
- 两robot四tasks各50rollout（drill40）、测试位置在训练spatialdistribution；tracking主实验maskIoU对同SAMmask非independentposegold，YCB初始化GT并首帧scale，不能泛称超真实depth FoundationPose（后者ADD-S95.8 vs本法51.4）。MuJoCo同2000数据xArm placement90→62%，不证明contactphysics无价值。Rigid-only、单目标functionregion、kinematicomit接触和失败仍保。
- actual owner `MULTIMODAL-EMBODIED-VLA` Ch26现2602.12734完整段已写semantic cousin非同实例、metric scale/对应→simtrajectory的接口；其后ShapeGen2604.15569完整两段已要求共同变换观察与动作、functionalregions与gripper correction、真实闭环另验及原示范/对应/坐标身份。R2Sem2R去人工功能点、增加target cousin是这个数据producer的组件替代，并未改变这条已承载的交互一致性与sim/real边界；不为新工具链另添同义段。新原件保具体双对象生成配置与有限证据，NC不缩候选/改分。

## V2 2610.28882 inr2action — 2+1+2=5，必要标准 Source；拟整合

- [exact-v1](https://arxiv.org/html/2610.28882v1)，实读III-A–C、IV-A–C/表I–II、V限制；[原件](vla1-source-2610.28882-v1.txt)。
- 每episode从共同MAML origin拟合NeRV，用delta而非绝对参数作为episode object；7tensor groups各独立rowmap/pool8→56tokens，再给TinyLlama1.1B QA或另Pythia400M jointreadout。不是把机器人policy权重在线写入同一个流式memory；输入先拟合500 fullbatch Adam，当前实验是offline。1600sourceepisodes70/15/15、每源10randomcut→16000独立INR/config，64²，不能把100至100000frames fixedparameter结构当已验证长视频保真/恒定fitcost。
- QA在closedchoices以有无weighttoken的NLL差读出、候选within-task，2seeds；47.2±2.6 vs34.6chance、taskgoal33 vs29.5，非freeform回答。MatchedGaussian noise掉11.4pp有限支持episodecontent依赖，不同randomorigin非一切commonorigin方案的普遍不可能。Action是cut末绝对jointcommand单点BC、8dimmeanR².51，非policy rollout；pooled7continuousR².53不同分母。无直接framesVLM/externalbaseline，无在线fit/TTT，仿真有限任务。INRmetatrain/percut500步、projector/两backbone微调、每candidate双NLL和全部存储计费，模型大小fixed不等信息/计算无限。
- actual owner `AGENT-MEMORY` Ch77“External Procedure→Weight Update”目前讲经验混入planner参数后逐条删除不天然成立；这里是可独立寻址episode artifact的参数，不是更新basepolicy，故补反向边界，避免“凡weights必不能逐episode丢弃”的过宽解释。精确位：完整“一旦进入 weights，逐条 provenance、selective deletion 与 exact rollback 不再天然成立；必须冻结 training set...Memory Intelligence Agent...production-safe。”段后，完整“固化经验还有一条失败回退分支：先按 query 与派生规则...”段前。
- 逐字 PRE：

> 参数式记忆还可属于单独 episode artifact，而非写进共享 Planner：从同一已版本化初始化拟合各段视频，保存各自 weight delta，再投影成 consumer tokens；共同 origin、拟合规则与 projector 一起定义可比较坐标。[inr2action 的受限读出](https://arxiv.org/html/2610.28882v1#S3)不在查询时取帧，却仍需离线逐 episode 优化，固定参数量不保证任意长历史保真或恒定写入费用。可分别丢弃 artifact 也不证明其他缓存、训练消费者中没有残留；closed-choice QA 与单点动作回归更不等闭环执行。元训练、全部拟合与读出训练/查询均付费；细节、来源或更新成本不合时保留 raw evidence、external store 与原 policy，不用可寻址 delta 代签事实、完整遗忘或在线控制。
>
> <!-- source-family:SF-2026-ARXIV-2610-28882 -->

## V3 2610.29161 SimPT — 2+2+2=6，必要标准 Source；拟整合

- [exact-v1](https://arxiv.org/html/2610.29161v1)，实读III-A–D、IV-A–D/表I–II、V；[原件](vla1-source-2610.29161-v1.txt)。
- Task source/privileged state adapters→3 candidate progressgraphs/最多2修订→静态check/简约选择→expert replay校阈/动态修订，运行时graph固定免LLM。progress/regression可invalidate依赖stage，不把21/21静态通过当状态语义正确证明。保stage最新snapshot、失败后从较高级完整simstate恢复CuRoboexpert，失败回退更早/初态；成功suffix接policy prefix供完整纠错trajectory。并非真实机器人可撤销失败或在线runtime safety gate。
- PG与naive同parent/240seeds/expert但独立rollouts，不是同失败episode逐个paired；attempt3781→945=-75%，perrecovery7.62→1.79=-76.5%，success93.4→98.9三分母分开。7RoboTwin/π.5、50demo起训、10kposttraining、40validation seeds/task；最终200expert-valid seeds/task=1400，bootstrap条件于已训policy，不代表多trainingseeds。PG改善RECAP等却FlowPRO76.07→71.86，不能推所有算法用其data必强。
- CF-LPF另一个有限算法实例：5fold trajectory out-of-fold value、30Hz上的zero-phase Butterworth1Hz后50-stepadvantage，非在线因果filter/通用阈值；两项合用未单独全因子归因。heldout76.50→79.36，95%pairedseed CI .36–5.36pp，部分task退；真实25scenarios cable insertion18→24/25，使用1672真实HIL trajectories，并没有把privileged PG snapshot复原搬到真机。Graph/expertreplay/恢复失败/五valuemodels/全部policy训练和评估费用保留。
- actual owner Ch26“Online RL 应通过受限 Action Interface 接入 VLA”现有HIL段规定human correction/terminalreward，未区分可复原simstate上事后产生纠错data与真实在线接管。补此producer/恢复资格边界，不另开框架或valuefilter owner。精确位：完整“较少可训练状态换来样本效率和可回滚性...”段及semantic-body end之后，完整“有限交互预算下，策略学习还可交替使用局部梯度更新与参数子空间搜索...”之前。
- 逐字 PRE：

> 纠错数据也可以在可恢复的 simulator 中事后生成，而不是要求人类当场接管：以受校验的阶段图读取 privileged state、保存阶段快照，失败后从较晚阶段调用 expert，无法继续再回到更早状态，将成功恢复段接回原 policy 前缀。[SimPT 的受限比较](https://arxiv.org/html/2610.29161v1#S3)减少了恢复搜索，却不使阶段判据成为真值，也不保证每种后训练算法都受益；同初始 seeds 的独立采集不是同一次失败的逐对控制。完整模拟状态复原是数据资格，不是现实机器人 undo 权限；运行评价仍应移除 graph、expert 与 privileged inputs。编图/校准、失败恢复、expert与全部后训练均付费；状态不可复原、接触或真实域失配时保留人类纠错、原示教与独立 controller，不用模拟可恢复性批准真实继续执行。
>
> <!-- source-family:SF-2026-ARXIV-2610-29161 -->

## V4 2610.29168 WAM priors — 2+1+2=5，必要标准 Source；仅报告 / NC

- [exact-v1](https://arxiv.org/html/2610.29168v1)，实读§3.1–3.2、§4.1–4.2、§5.1–5.2、§6/限制及表1；[原件](vla1-source-2610.29168-v1.txt)。
- 本文是观察诊断不是新的policytraining算法：40clean observations估计中心化feature矩阵39个非零SVD方向，对1200同simstate visualshift pairs计算displacement落在该span外的能量比例，逐层/样本平均。所谓IDmanifold是有限样本线性span，不是真实流形/任务充分表示；降rank让orth分数自然升，不是质量变好。9backbones跨image/video及scratchFLUX，平均orth与LIBEROPlus性能有限同向，不是pretrainingobjective唯一因果或可直接部署的模型selection保证；初始模型/架构/tokenizer/data/已有不同policy配置均混杂。Camera shift也可能改可见性，不泛称任意nuisance真action-preserving。
- postpolicy nuisance suppression是在每checkpoint分别拟合basis/variance后标准化的位移比，不要求raw位移缩小。ImageWAM IDvariance13.4×而两位移2.73/2.48×，不能写成所有视觉变化都被物理抹除；FastWAM4.42× vs5.63/3.18×，成分有未抑制。PCA各panel独立fit/scale不可直接横比距离，监督probe不等内部机制已因果识别。限定模拟visualshifts，不涵盖language/actioncomposition；全部pairedrender/SVD/层特征及多WAM训练评估计费。
- actual owner Ch26“Future-to-Action...”中2609.24048完整段已解释frozen encoder时间prior可熟悉任务好却OOD脆、action通路/ID-OOD/梯度目标与outcome分开验；并未按image/video名称选择模型或宣称probe越好必robust。本文的有限样本orthogonality相关指标/事后归一位移不能替代这些验收，未改变现有设计因果解释。新经验关联保报告，NC不删其候选或把相关写成结构性不变性准则。

## V5 2610.29203 NavBind exact-v1 — 3+1+2=6，设计反证必要域深入；拟整合

- [exact-v1](https://arxiv.org/html/2610.29203v1)，已实读§3.1–7.7/式1–9/表1–7、§8/限制；[原件](vla1-source-2610.29203-v1.txt)。只用v1，既成公告mapping/[v1身份](arxiv-ab-29203v1.json)有效，不混次日v2。
- 新反证是goal success不等语言条件有效：两源route须同directed segment到fork、非terminal且两branch可执行、edge-exact语言boundary；fixed同row history/prefix/pose/observation，只换剩余完整suffix；1648sourcepairs最终3252sharedcontexts，四步内reference在各native action scale均分歧。不是只换“left/right”造成不可能路线。跨row补充实验同时改history+prefix，不是纯prefix因果；recombination可能语言不自然，数据来源/筛选保有限条件。
- 无teacherforcing生成SameSeq与fixedreference teacherforcedNLL分开；NLL用fullvocab、actiontokens平均，single-step policy按GT执行历史采样状态，独立memory；SKL另在4legalactions归一，不可等同PPL/target支持。Both+要求两reference各自正确suffix更高似然，25%只是独立50%符号假设，不是已校准chance或统计显著性。d=.0127→1.28%是跨token/target/context几何平均概率比例，不是完整trajectory likelihood、success或1.28pp。
- Raw attention比较同target；gradient/attention×gradient比较各自matchingGT，所以同时换instruction和explainedaction，不授热图因果或相关region真值。IoU在原grid top25%，resize只展示；laterGTview分歧时single-step gradient只forkfirstaction。四models同contexts但native increments不同physichorizon、UniNaVid sampling vsStreamgreedy，SameSeq不可作绝对随机性控制后的排名；SR是官方RxRvalunseen而诊断混source，不是同run成功分组因果。更高SR者binding更弱是具体有限反例，不授通用语言无用或全导航失败。prefix长弱响应仅分桶相关，非长度唯一因果；attention/attribution/多targetteacherforcedscore与全部回放均付费。
- actual owner `MULTIMODAL-EMBODIED-VLA` Ch26 VLA policy首段只定义联合vision-language-action与输出schema，随后马上进入mobile/manip接口；后面的future干预针对未来通路，不足以证明instruction改变动作。精确位：完整“VLA 联合建模 vision、language 与 action，减少中间手工接口。常见输出可以是离散 action token、连续 pose、flow/diffusion action chunk 或 trajectory representation。”后；完整“统一移动与操作的数值向量容易实现...”段前。
- 逐字 PRE：

> 联合输入也不证明动作遵循语言：到达目标可能依赖视觉或既有路线。可固定同一 state、观察历史与已完成指令前缀，只替换为另一条真实可执行分支的 suffix，分别比较自产动作是否变化，以及同一 reference actions 在两条指令下是否更受 matching suffix 支持。[NavBind exact-v1 的局部诊断](https://arxiv.org/html/2610.29203v1#S5)把行为变化与目标似然分开，避免把随机换动作或更大分布差当正确绑定；attention 热图变化也不证明被选区域相关或有因果作用。四动作窗口、native 步长/解码和重组文字限制外推，官方 goal success 排名不能代签这一 Gate。成对场景/路线、回放与全部打分付费；指令或动作接口不足时保留明确短目标、原 policy 与独立执行检查，不由共享 backbone 或局部 likelihood 批准真实遵令与安全。
>
> <!-- source-family:SF-2026-ARXIV-2610-29203 -->

## V6 2610.29246 DepState-JEPA — 2+1+2=5，必要标准 Source；具体 NC

- [exact-v1](https://arxiv.org/html/2610.29246v1)，实读§3.1–3.5/式1–11、§4.1–4.5/表1–3和消融、§5；[原件](vla1-source-2610.29246-v1.txt)。
- registeredRGB/metricdepth/intrinsics把visiblepatch lift到camera3D并加PE，separate encoders→shared/privateMLPs；只有shared进入64×384 genericqueries state，private只decode。alignment/covariance/variance正则不证明纯因素分解。raydirection/timequery不用targetdepth，maskeddepth不进online lift；已知calibration不是自动恢复metricgeometry。transition输入command、q、qdot、真实Δt，预测state复用readout及固定initialprivate；outputrobotstate提供下一步条件，objectpose从suppliedinitialpose积分但不反馈state。FK只已知chain约束joint/TCP一致性，不证明动力学/接触。
- 初始RGBD adaptation是非causalfeature任务，不冒机器人rollout。Table2特征forecast每步recordedproprio，control/internalablation则recursivepredictedproprio，不能拼表2优点认证闭环免漂移。sharedreference/probe完成/transfer不同消费者，score非真实像素/场景真值；cross-system比较训练/容量/适配不同。私有path删去L1 .340→.390但SR83.4→83.2近不变，说明visualdecode与action价值分开；separateddecoders .333更好且SR同83.4代价容量更大，不授shareddecoder必更优；FK删82.5 vs83.4有限效应。
- DMC20/MW50同interaction/searchbudget，sim2real两task三seeds×30trial，60s仅robotexecution不含inference/search，不能称60s总延迟。没有真深度/固定calibration支持时不能照搬；双encoder/EMA/metricdata/objectlabels/FK、actorcritic或MPC/search与真实回归全费。
- actual owner `MULTIMODAL-REPRESENTATION` Ch23 2605.21059完整两段已明确共享相关因素与private decoder/readout分责、对齐≠consumer兼容；`MULTIMODAL-WORLD-MODELS` Ch25 latent dynamics入口和2603.12655两段已要求定义可预测接口/compatible decoder、reconstruction不等control充分、imaginedstate不改rawfact。DepState给这些职责一个RGBD/固定private的组件实现，不推翻已有论点，也没有证明共享/private分解为可识别真实状态。固定private、recorded-vs-recursive条件及新实现数据留报告；不另添一条同义representation framework chain。

## V7 2610.29264 TIDE deployment — 2+2+2=6，必要标准 Source；拟整合

- [exact-v1](https://arxiv.org/html/2610.29264v1)，实读III-A–B/式1–2、IV-A–B/全部Q1–4、V–VI；[原件](vla1-source-2610.29264-v1.txt)。
- critic/rewardmodel/actionscorer-free是provenance-conditioned SFT，不是无成功筛选或无人监督：只manualconfirmed successfulepisodes commit，其余fail/timeout/abort/stale/unrecovereddiscard。连续executedactions和sourceflags→50step全human标0/全policy标1、mixed整horizon排除、无额外交接exclusionwindow。source是生产者不是qualitylabel；全部自主rollouts固定humanmode0。offline/online两buffer以1/6、5/6选取，online human/policy再balance，非每条相同权重/全policyepisode当expert。mirror/timescale受taskpreserving前提约束。
- client在HIL交接清空queuedchunks；server每rollout只用一个policygeneration，learner异步prefetch/publish但只episodeboundary adopts，不把“weights可用”当正在执行chunk能安全换权。全3B backbone/Qformer/action/sourceembeddings更新，textencoder/VAE冻，非低开销只训tinyhead。0.2optimizerstep/newcommitframe、每5commit发布是实验schedule不是通用配方/单调准入。humanmode是目标条件，不证明expertquality或策略校准。
- 四UR5e bimanual tasks/同初态每method20no-takeover，milestonenormalized progress与binarycompletion k/20分开。FixedPolicy同collectionduration、同objective/filter/buffer/总optimizerbudget，TIDE final仅相近：bit/部分progress相同，binary后两towel多1rollout、chain多2，不授显著更佳最终质量。TIDE区别是部署中checkpoint availability，interventionratio下降混有session时序、选择成功人口，不是无监督性能量或learning唯一因果。单任务去provenance/onlyhuman支持有限局部差，不跨任务泛化。
- <1h是从deploymentstart到finaldeployable，8H100/约.4sstep，含异步execution/HIL/reset/train/checkpoint，排除setup和finalevaluation；41commit/38839frames21.6min/control30Hz是bit示例，不代表all wallclock。无重复online sessions方差/长期retention/多平台，全部人时/失败采集/训练和eval仍计费。
- actual owner Ch26现有HIL online-RL段采用critichead/compacttoken，但尚未给“按已执行动作来源标注SFT、successful筛选与模型发布边界分离”的无critic替代。定位与V3同一HIL之后局部区间，建议最终局部顺序：旧完整“较少可训练状态换来样本效率和可回滚性...”及semanticend → V7 TIDE → V3 SimPT → 完整“有限交互预算下，策略学习还可交替使用局部梯度更新与参数子空间搜索...”段。root写前协调该窄位，不把旧锚当写后现态。
- 逐字 PRE：

> 部署中更新也可以采用来源条件化的监督学习，而不增加 critic：按实际执行记录区分 human 与 policy 产生的纯来源 action chunks，混合交接窗口另行排除；成功确认只决定 episode 能否进数据，不把来源标签当动作质量。[TIDE 的受限实现](https://arxiv.org/html/2610.29264v1#S3)异步收集、训练和发布权重，但交接先清空旧动作队列，episode 内固定同一 policy generation，仅在边界采用新 checkpoint。四任务有限比较的最终性能与固定 policy 收集后再训相近，收益是更新更早可用，不是更好质量或稳定学习保证；成功筛选、人类接管与全模型训练仍有成本和偏差。标签、handoff、旧能力或控制预算失配时保留原 checkpoint、离线更新与人工接管，不让 available weights 自动取得物理执行权限。
>
> <!-- source-family:SF-2026-ARXIV-2610-29264 -->

## V8 2610.29282 Relational Geometry Forcing — 3+1+2=6，几何对齐设计反证必要域深入；拟整合

- [exact-v1](https://arxiv.org/html/2610.29282v1)，实读§1诊断、§3.1–3.3/式1–10、§4.1–4.6/表1–5、§5限制，以及A.1–A.3/B.1–B.3必要pointwisecontrol/配对/计算域；[正文](vla1-source-2610.29282-v1.txt)、[A–B](vla1-source-2610.29282-v1-A-B.txt)。不遍历无关逐任务附件/rollout图。
- pointwise control视频patch bilinear重采teacher同位置cosine，对action则将projector reshape各view去拟合每步pool的VGGT scenevector（排camera tokens），视频/动作各weight.5；加action后LIBERO三variants相对各自baseline只-.05/-.15/-.05pp，没reportedtrainingseed区间，near-ceiling差极小，不能当统计显著/所有pointwise必伤action。与video-only-.35/-.40/-.45pp亦不唯一证明“dense内容过度约束”机制，auxgradstrength/投影任务等替代解释未全隔离。视频patch与compactaction不同consumer义务可据此质疑默认同target，不直接照录作者强因果解释。
- 新替代是projectednormalizedfeatures的cosineGram relations，不同维仍可同shape。video同framepatchrelations+crossviewallpairs；action32steps与32真实连续observation pooledscene descriptors配对，独立于9video-frame subsampling，不做temporalinterpolation。selfrelation去diagonal/padding，allcrossentries，Huber各validentries平均；VGGT finalfeatures预缓存只训练targets，teacher/projection/relation推理移除。只保相对cos关系，不交metric尺度/真实contact或动作物理truth；语义似然关系不能成为actioncausalgraph。
- 同Wan2.2-5B+1Bactionexpert Uncond/Joint/IDM和同protocol，fullRGF+1.05/.60/.55pp；table4 temporalalone-.15、intra+temporal-.25，all+1.05非各项独立有效，相互补偿未证明crossview唯一“stabilizer”。relationloss三equalweights总体.5与PW两个.5并非已证梯度预算匹配，DINOvsVGGT/formulation crosscondition不能分离全部supervision内容。不同系统主榜有pretrain/容量差，tiny .09pp不宣传普遍SOTA优势。
- LIBERO4×500=2000rollout，RoboTwin50task每clean/rand100、train50/500demo；realFranka3ZED、4base+3singleBowlvariants，每setting20同randomplacement，50demo/task。65.71 vs57.14是7settings平均，bowl同85、toy60仍低π.5的65，非alltasks强。硬件/compute：LIBERO8H20约16h/run、RoboTwin32H20约65h/run，全部targetcache/teacher、平方relation矩阵、数据与闭环eval费用；“部署无额外module”不等训练免费/控制deadline或独立真实几何已验。
- actual owner `MULTIMODAL-EMBODIED-VLA` Ch26 2610.28164当前完整段已分geometryqueries与motor targets，但没有“不另造motor target而匹配几何关系”的替代、也不允许把densegeometry逐点监督默认搬到action。精确位：完整“几何与motor监督还可沿不同表示路径交接...”段（marker2610-28164）之后；完整“重建完整未来特征也可能把大部分监督预算花在静态背景...”段之前。
- 逐字 PRE：

> 不另建 motor target 时，还可以只迁移 teacher 的关系，而不要求 compact action features 逐点拟合 dense scene 内容：对 video patches 匹配帧内及跨视图相似关系，对 action steps 匹配相应场景序列的时间关系，teacher 只在训练提供 targets。[RGF 的必要对照](https://arxiv.org/html/2610.29282v1#A1)给出这种不同维表示的替代接口，但逐点 action 对齐的退步很小、未报训练重复，不能泛化成几何监督必然损害动作；关系项单独或部分组合也会退步。Cosine relations 不含完整 metric scale、contact 或动作因果真值，有限均值改善不能代签。几何 teacher/cache、全部成对关系与训练计费；配对时钟、监督强度或闭环质量失配时保留 video-only 对齐、显式动作监督与原 policy，不把更接近关系矩阵当作可执行世界模型。
>
> <!-- source-family:SF-2026-ARXIV-2610-29282 -->

本批八项作者必要层已就绪：V2/V3/V5/V7/V8 五个逐字 PRE；V1/V6 具体已有覆盖，V4 仅报告。复核、root实际保存和POST仍单独进行，不签DAY。

## 五 PRE 的当前完整两侧快照

V3/V7共享同一原始窄位，建议最终顺序见V7；以下仅写前原段，不代root保存后的实际邻接/POST。

### V2 — books/part-07-agent/77-memory.md

完整上段：

> 一旦进入 weights，逐条 provenance、selective deletion 与 exact rollback 不再天然成立；必须冻结 training set、
> update job、checkpoint lineage、judge 和 before/after evaluation。外部 memory 在频繁更正、隐私删除和小样本场景
> 仍更合理。Memory Intelligence Agent 提供 Experimental loop，不证明 online weight update 已经 production-safe。

完整下段：

> 固化经验还有一条失败回退分支：先按 query 与派生规则的联合表示形成 cluster，以当前规则和 base model 既有规则之间的 gap 作为风险 proxy，尝试把低 gap 经验训练成 Expert adapter；若候选 checkpoint 未通过预设模拟评价，或 gap 较高，则不强行发布该 Expert，而训练 Critic 在运行时给 base 的初答提供反馈，再由 base 重答。它把“经验进入 weights”拆成直接改回答者和只改反馈者两条路径；日志、cluster、规则、adapter 与评价人口仍须冻结。gap 不是噪声真值，Ward 合并的方差增量也不证明 cluster 有固定直径；checkpoint verifier 选择更高分候选，不拥有生产 release 的授权。<!-- source-family:SF-2026-ARXIV-2602-06470 -->

### V3/V7 — books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md

完整上段：

> 较少可训练状态换来样本效率和可回滚性，却可能让 token 成为信息瓶颈、让 anchor 阻碍必要适应，或在 contact-rich phase 产生危险探索。作者证据限于几小时实践和四项真实机器人任务，并依赖上述 human-in-the-loop contract，不支持通用 online-RL 保证；任务需要表征重写时仍需更广 fine-tuning，安全证据不足时回退 frozen policy、离线数据或人工接管。
> <!-- semantic-body-binding:SF-2026-ARXIV-2604-23073:end -->

完整下段：

> 有限交互预算下，策略学习还可交替使用局部梯度更新与参数子空间搜索：从近期梯度取低秩基，在当前policy附近用少量真实rollout建立坐标—回报context，再由预训练表格模型筛选较大候选池。每次只执行少量候选、补回真实回报，最后仍以已实际评估者接纳更新；[受限连续控制对照](https://arxiv.org/html/2604.27667v1#S3)中的低维“global search”不覆盖全部参数空间。基点或子空间改变后，旧坐标和surrogate不再可直接复用；排名相关也不认证每个top candidate或安全。SVD、预训练模型、全部搜索/失败rollout与局部更新都计费，同搜索评估次数不等全链同成本。排序失准、收益难摊销或真实任务不允许试错时，保留原actor–critic、有限随机搜索、离线验证和独立controller，不把更少真实候选评估当机器人执行许可。<!-- source-family:SF-2026-ARXIV-2604-27667 -->

### V5 — books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md

完整上段：

> VLA 联合建模 vision、language 与 action，减少中间手工接口。常见输出可以是离散 action token、连续 pose、flow/diffusion action chunk 或 trajectory representation。

完整下段：

> 统一移动与操作的数值向量容易实现，却可能让模型在操作阶段重新发出底座运动；可选的较窄接口先输出导航 direction 与 distance/angle value，只有 `stop` 分支才继续解析 manipulation values，把动作阶段写进 schema，而不只依赖同一向量中的数值模式。[有限实机对照](https://arxiv.org/html/2602.22663v1)在两任务各10次中由纯 value 的2/10、1/10变为4/10、4/10，只支持这个表示选择，不认证真实停稳、碰撞安全或任意本体统一。它仍使用预训练视觉语言骨干，所谓无 pre-training 仅指不依赖大规模跨机器人预训练；同域 post-training、fine-tuning、tokenizer 与多视角输入都有成本。小模型/较细词表和更长 chunk 也非单调改进，受测 chunk20与部分seen任务明显反退；schema失配、底座未停稳或接触精度不足时，保留分开的导航/操作policy、连续head和独立controller，以新观测决定执行，不让 `stop` token取得物理停机证明权。<!-- source-family:SF-2026-ARXIV-2602-22663 -->

### V8 — books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md

完整上段：

> 几何与motor监督还可沿不同表示路径交接：冻结3D特征先形成带视角与时间身份的几何状态，再由相邻状态差分经动作监督提取motor target；后训练时，geometry queries拟合前者，动作通路的中间层拟合后者，teacher与真实未来只作训练特权信息。[受限对照](https://arxiv.org/html/2610.28164v1#S3)支持这种消费者分工，不证明差分排除了相机运动或两表示已因果解耦；统一表示/普通aux仍能受益，部分任务与encoder选择仍反胜，更强几何权重也会退步。3D teacher、多阶段预训练、特权视频与双目标后训练均付费，删除部署teacher不等零新增成本；表示支持、接触信息或闭环预算不足时，保留普通aux、原policy、真实重观测与独立controller，不以probe或均值成功签发物理安全。<!-- source-family:SF-2026-ARXIV-2610-28164 -->

完整下段：

> 重建完整未来特征也可能把大部分监督预算花在静态背景。导航中的一个局部分支，先由上游定位系统把机器人带到目标近邻，再以目标入口的 bounding box 训练 intent；动作训练阶段冻结 backbone 与 intent，用未来帧光流幅度最高的区域作为辅助重建目标，同时训练 waypoint decoder。辅助 decoder 在推理时删除，运动区域只是训练目标的选择器，不是无先验目标定位，也不等于目标 salience 或真实动作因果；waypoint proposal 仍须交给 controller 与环境反馈验收。<!-- source-family:SF-2026-ARXIV-2602-06427 -->



