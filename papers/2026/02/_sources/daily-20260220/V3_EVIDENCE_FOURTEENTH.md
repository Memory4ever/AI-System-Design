# 02/20 第十四有限必要包：16704 / 16705 / 16710 / 16712

四项完整题摘已root独立准入校准；16712精确v1一次core限定canonical morphology/action interface，不授LLM/VLA或通用控制。各项必要支持/关键反侧读够即停，root必要PRE与四处真实正文/完整邻接/自身末注POST均通过；三文件窄锁已释放，非日级验收。下文位置为 `V3_extract_html.py < V3_REVIEW_2602.<ID>v1.html | awk 'NF' | nl -ba`。

| ID | v1 Submitted UTC | 同ID DOI Registered UTC | 北京公开范围（官方bridge推定，含起不含止） |
| --- | --- | --- | --- |
| 16704 | 2026-02-18T18:53:18Z | 2026-02-19T02:52:52Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:52:53+08:00 |
| 16705 | 2026-02-18T18:55:02Z | 2026-02-19T02:52:53Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:52:54+08:00 |
| 16710 | 2026-02-18T18:59:05Z | 2026-02-19T02:53:00Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:53:01+08:00 |
| 16712 | 2026-02-18T18:59:57Z | 2026-02-19T02:53:03Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:53:04+08:00 |

Registered只沿首包官方公告/ID/DOI桥接推定上界、1秒精度，不把DataCite Created/Updated当正文公开。四当前官方abs已有Comments/history轻核：16704/710仅v1；16705现v3标题/摘要改变、16712现v2 RSS accepted但无明确纠错/撤回声明。只采用精确v1，不把版本号当重要事件，不扩全版本比较。

## [Reinforced Fast Weights with Next-Sequence Prediction](https://arxiv.org/html/2602.16704v1)

2+2+2=6，训练目标/rollout接口差额深入。§3.1–3.3（155–218）：对整条S做一次teacher-forced前向得到NTP entropy和GT续文last-layer states，平滑entropy、S均分c块、每块softmax抽一个位置，不是只取最大entropy。各真实截断prefix生成k-token on-policy续文，逐位置cosine(pred-state,GT-state)平均作reward；GT-state仍来自policy，不是外部teacher或独立semantic oracle。对同一S的不同prefix rollout rewards标准化后用GRPO，保全S NTP CE与phase权重；不能混称同prompt多iid completion。TTT用binarytokenmatch、posttrain混合binary/cosine。CE本身也定义序列概率，不采用“CE完全忽略语义”宣传。

§4设置/A1（756–788）：LaCT760M fastweights vsDeltaNet1.3B parallel memory；midtrain与SFT同100steps/b128、约200Mtokens，但生成/GTstate/前缀重算开销未匹配FLOP。RULER/LongBench与Booksum评价不同，Booksum误差条为3trial min/max，不推所有实验3seed。Table6/7与k/c切片（803–859）：binary→cosine局部差额小；entropy-weighted相对uniform/max/min有增益，k5后k7退步、更多c增加generation，作者“sharpness”原因未单独证明。Limitations/FutureWork（860–872）长rollout/context依赖与truncatedprefix间fastweight高效transfer仍待架构工作，不能说fixed memory让训练免费。A4 TableD1（1463–1521）Adam/lr1e-6、KL0、gradclip .2等；硬件/precision采用段Not Disclosed。不采headline普遍加速/semantic保证，未核实现/复现。

actual TRAIN-PRETRAINING Ch28:72–82已有并行future-token辅助CE及外部teacher earlylayer cosine；MODEL-LONG-CONTEXT Ch22:634–668已有当前KV绑定/历史行为压缩/fastweight写入生命周期。未承载**从真实prefix产生policy续文，用同policy GT-state proxy作sequence rollout辅助目标，sampling人口与保NTP分工**。拟Ch28未来目标/LET段后、记忆目标前仅一段，保proxy/跨prefix group、k/c/完整compute与NTP旧支路；不重复fastweight架构或推GRPO新定理。

## [Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation](https://arxiv.org/html/2602.16705v1)

2+2+2=6，foundation视觉→低层task-space接口差额深入。精确v1标题/AB77–100采用3.2x宣传不作结果；正文自身也含2.44cm，但TableIV清楚该行为MOCAP oracle，不借当前v3把它倒填learned模型。§III-A（219–244）从EEgoal经IK/碰撞planner得到referencejointtrajectory，trackingpolicy同时消费EEresidual，输出29DoF jointcommands接50Hz PD。§III-B（256–294）analyticFK加learnedSE3 residual及static-feet legodometry；MOCAP2htrain+1hvalidation/encoder绑定，非运行时持续MOCAP。§III-C/D（296–304）漂移时周期replan，goaladjust只放大translation残差且近目标关停，不是直接改所有jointtargets或忽略rotation。§IV（306–324）GroundingDINO/SAM/AnyGrasp→Dex3retarget再controller；orientationclip/可达workspace，不授任意openworld。

§V-A/D（376–396、470–490）固定180目标/3table heights、同目标retrainAMO/FALCON、MOCAP测EE误差，jointerror由encoder测。TableIII/§V-D1（490–581）EE改善同时jointtracking反而较差，**低jointerror≠低task-space error**；TableIV（537–590）FK/learned/GT pose输入control，2.44为oracle，learned2.56，本包不采用数值排名。TableV/§V-D3（591–626）replan/goaladjust消融全部MOCAP pose，不能当自主estimatedpose下每项因果增益；60rollout曲线不等独立trainedseed。§V-E/VI（628–637、678–689）滑脱/撞倒、FoV目标消失、staticfeet/规划扭曲与LVM错误仍在。B6（1587–1592）RTX5070Ti laptop，DINO1.5需onlineAPI而base可本地，precision/整体SLO Not Disclosed。有限抓取定义lift>2s、3trial/object/height不签安全。未复现。

actual MULTIMODAL-EMBODIED-VLA Ch26:139–158有模块化语义handoff/controller，48–83有frame/calibration/canonicalbody decoder；缺的是**foundation model物体proposal之后，analyticFK估计/浮动base误差如何进入task-space residual与重规划，以及jointtracking指标可能掩盖真实EE偏差**。拟VLM-conditioned controller首段后仅一段，保静足、MOCAP离线成本/视域/估计失配与传统精密固定base FK共存，不授planner/整体安全。

## [EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data](https://arxiv.org/html/2602.16710v1)

2+2+2=6，data-scale与embodiment-alignment分责差额深入。§2.1–2.4（114–170）：SLAM+handtracking把humanvideos改为relativewrist SE3与22DoF Sharpa-retarget joints；不是raw视频自己产生robot真值。StageI20,854h含829hEgoDex辅助精跟踪；StageII同相机/标定与Vive/Manus的alignedhuman50h+robot4h、344tasks，StageIII任务示教。human缺proprioception用learnableplaceholder，sharedwrist/backbone/DiT+embodimentinput/outputMLPadapters，few追加本体不是agnosticdecoder。I100ksteps256GB200/b8192；II50ksteps冻结VLMbackbone、更新visionencoder/DiT；III10kstepsvision是否冻依II，无allstage同freeze。§2.5（172–180）R1Pro固定base/torso，不将bimanualtabletop授loco。

§3.1/3.2（190–233）五任务100robotdemos（shirt20）；2trainedseeds、10trial/checkpoint，原文L210把“TaskIII/4bottles”列同一例外而任务编号III是tongs/V是syringe，IV才bottle，本包保文字口径冲突，不继承精确每任务统一trial分母。四stage checkpoint比较支持局部complementarity但并非全pipeline等compute；§3.3（235–257）1k–20kh/heldout2000episode/20timestep/16samples平均MSE与任务关联，不授数据scale唯一原因或新通用law。§3.4（259–272）one-shot仍加每任务100alignedhuman demos、失败残留，不写一条示教即可；§3.5（274–290）G1追加alignedplay、lowerbody另Homie，不是零targetdata。§3.6（292–304）wrist-only/fingertip+MLP/retargetjoints比较，指尖误差可变成不合理joints，但未隔离每次retarget唯一因果。precision/controlSLO Not Disclosed，未核实现/复现。

actual TRAIN-DATA Ch27:670–690已有humanpose驱动generatedvideo与派生robottrajectory/provenance，MULTIMODAL-EMBODIED-VLA Ch26:256–258已有geometrycode+embodimenthead/训练预算边界；并未承载**真实humanvideo行动标签可扩scale，但专门同传感/动作的少量aligned中训仍是另一个anchor，规模和alignment不相互替代，one-shot须披露额外human监督**。拟Ch27 Physical→Digital Teleoperation段后仅一段，区分真实视频恢复标签/生成视频及robot控制证据，保retarget、stagefreeze/placeholder、aligned采集成本与原真实teleop；不另重复Ch26code架构，不采loglinearlaw。

## [One Hand to Rule Them All: Canonical Representations for Unified Dexterous Manipulation](https://arxiv.org/html/2602.16712v1)

2+1+2=5，canonicalaction接口具体差额深入。精确v1AB/III（217–245）capsule人手样up5finger22DoF，统一palm/jointaxes，82params（173extended不是本实验无损证明）；smallerhands inactivejoints/removelinks，原URDFjoint-to-joint/signmapping双向转换，不把zero值当active自由度。IV-C（260–264）frozenmorphologyVAE+objectencoder形成condition，diffusion wristtranslation显式给R，再MLP joints；不是新抓取算法或LLM/VLA。V-B TableII/III（283–329）original↔canonical replay，LEAP reorientation有退步；Allegro omission轴造成transfer下降，不采“所有动力学无损”。V-C（358–379）24764filteredgrasps/三手/10unseenobjects、specificvsunified训练局部收益，同data总训练费用/independentseed未完整披露；0.13s非全链SLO，D(R,O)在Allegro/Shadow更好。A modeling assumptions（548–571）nonthumb同linklength/coplanar/jointaxis先验，不能泛任意URDF。未采LEAPzero-shot普遍能力，不扩全部realexperiment或附件。

actual MULTIMODAL-EMBODIED-VLA Ch26:48–83已有camera/robotframe与body25D canonicaldecoder，256–258已有几何码与nativehead；两者没有**canonicalhand action人口/activejoint与URDFaxis双向映射，以及结构省略会在actionreplay中产生差额，需把morphology schema与policy同时验收**。拟Ch26坐标归一化generic段后最多一段，保布局先验/axis缺失/额外解析和校准、nativeURDF/directretarget共存，不把canonical接口授通用control安全，也不把无foundation名称当事后scopeEX。
