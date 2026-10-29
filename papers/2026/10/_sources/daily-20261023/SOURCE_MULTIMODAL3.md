# Oct23 Daily — MULTIMODAL3 必要 Source / Books 提案

范围仅 Oct22 BJT 的本批八家族；日期/完整题摘/准入及初分复用 [ARXIV](ARXIV.md) 的官方 list mapping 和既成独核，不第三次判日期。作者只写本文件和本批原件；root 唯一 Books/Report/State writer。以下 PRE 仅为送审文本，不表示已保存或 POST。

## P1 2610.29915 CausalAlign — 2+1+2=5，标准 Source；拟整合

- exact-v1：[官方 HTML](https://arxiv.org/html/2610.29915v1)，已实读 §3.1–3.5、§4.1–4.3/表1–4及结论；必要正文原件 [文本](multimodal3-source-2610.29915-v1.txt)。
- 新命题不是“probe 能读出即有物理世界”：分别做相邻 frame hidden-transition 的相对 pose probe，以及固定 prompt/noise/seed、相对 norm-matched random controls 的 mask/shuffle/replace/inject。对 layer/step 的归一 probe+干预分数下降位置做选择，再以 LingBot-Map teacher 的连续帧变化学习 delta 空间；先学 teacher delta，再冻 teacher/VGM 学 projector，最后冻 projector 和 camera decoder，只更新所选层 LoRA，以 delta matching+相对 pose loss 训练。需要 pose 标注，并非纯无监督几何发现；主协议不提供 reference trajectory 作为生成条件。
- DL3DV/RE10K 各90/10划分；teacher token 用训练集30%，projector10%，最后 LoRA 全训练集。Wan2.2-14B-I2V 相同采样/seed/输入比较，几何由相同冻结估计器读出，重投影8.4→6.5但 depth-flow 5.5仍弱于 FantasyWorld5.4，FVD182.4→182.7退步。matched-width equally-supervised partitions 对照支持局部结构，raw8192/4096 vs128比较不是等维控制。Fast-WAM另做人类预训、每任务500示范、50k步、三camera/proprio，43.5→54.2不能归为免训练直接控制。没有 isolated full-factor 结果就不声称唯一层位/唯一机制已证明；proxy与干预只对所测 generator/轨迹成立。
- 实际 owner `MULTIMODAL-WORLD-MODELS` Ch25：当前 VGGT-World 两段分预测接口/联合几何decode，AEON 段分生成→几何翻译；尚未承载“先分别诊断生成状态可读/被用，再在遗忘处训练变化状态”的反向监督接口。只补这个 gap，不另开 VLA owner。
- PRE 精确位置：Ch25 当前完整 AEON 段（起“视频生成先验与几何解码器也可保留各自坐标”，止“...控制安全。”、marker2610-28631）之后；完整下一段起“可推进状态也可以直接是一组带材料标签的物体与执行器粒子”之前。
- 逐字 PRE：

> 几何模型还可以反过来监督视频生成器的内部变化状态，而不只解码其输出。先分别检验相邻帧表示能否读出相对相机运动，以及固定输入与随机性后的受控干预是否改变轨迹，再在诊断到信息衰减的层与去噪位置对齐 teacher 的帧间 delta；冻结 teacher/projector，仅以相对 pose 与变化 token 监督适配生成器。[CausalAlign 的受限方法与对照](https://arxiv.org/html/2610.29915v1#S3)要求 pose 标注和多阶段训练，probe、同源几何估计与局部干预不认证真实动力学或唯一因果位置；部分视觉/几何指标仍反退，另训动作模型的成功率也不是直接控制保证。诊断、teacher 特征、delta/projector/adapter 与动作回归均付费；几何来源、运动或 horizon 失配时保留原生成器、显式几何/真实观测与独立 controller，不把可解码或更一致签成物理事实。
>
> <!-- source-family:SF-2026-ARXIV-2610-29915 -->

## P2 2610.29989 FCP — 2+1+2=5，标准 Source；拟整合

- exact-v1：[官方 HTML](https://arxiv.org/html/2610.29989v1)；已实读 §3.1–5.6、方法/表1–4及结论所需；[原件](multimodal3-source-2610.29989-v1.txt)。
- clean-history teacher forcing 可借相邻外观捷径；FCP 不同于制造自产误差：令 clean/noisy source chunk 的中层 feature 分别预测隔开的 future chunk，不给中间 chunks；多层features拼接MLP→tokenwiseAdaLN，offset独立3-block predictors，不共享链式隐藏状态，也不给 predictor 独立 text cross-attention。主干仍有文字，当前chunk表示也可能已经编码文字，故不是全模型 text-free。offset集合可含1，不能说每个aux目标都跳一chunk。aux flow loss回传主干，推理丢aux。
- 同数据/训练配置 Wan1.3B IQ27.6→30.9，5B I2V30.4→33.8；部分分指标退步，cross-model leaderboard不作方法因果证据。chain3/5offset 5B V2V40.5/39.9弱于TF40.6，支持限定设计选择，不认证唯一信息泄漏根因。算力曲线是 estimated training compute，42.6/50.7%是相对 full-history FCP 达到IQ29/30，不是相对TF端到端节省或实测墙钟。aux参数、前反向/optimizer/多offset、数据和独立rollout评价计费；无部署额外head不等训练免费，representation maps不证明action causal state。
- actual owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24：Helios 两段已讲历史压缩和 train/infer误差，未覆盖“正确近邻历史过易，所以辅助目标主动隔离未来中间证据”。插于完整 Helios 第二段（起“推理继续消费自己生成的历史”，止“...既有 dense 路径。”、marker2603-04379）之后；完整“连续视频切到新shot时，近期自产chunk与跨shot参照不能沿用同一默认历史...”段之前。
- 逐字 PRE：

> 正确历史也可能过于容易：相邻视频 chunks 高度冗余，teacher forcing 的低去噪误差未必迫使表示预测更远的演化。一条[受限 future-chunk 监督分支](https://arxiv.org/html/2610.29989v1#S4)让当前 clean/noisy chunk 的中间表示条件化独立 offset predictors，预测不读取中间视觉 chunks 的未来目标；各 predictor 不串接隐藏状态，也没有独立文字入口，辅助损失回传生成器，部署再移除这些模块。这与训练自产历史误差互补，不证明模型不再利用任何文字捷径或获得物理因果状态。同配置的有限视频对照支持局部收益，部分分指标仍退步；估算训练算量不等墙钟，所有辅助训练与 rollout 验收均付费。收益、时距或预算失配时保留普通 teacher forcing、较短预测与直接历史监督，不把无部署 head 当免费训练或无限稳定。
>
> <!-- source-family:SF-2026-ARXIV-2610-29989 -->

## P3 2610.30036 Attn-Forcing — 2+1+2=5，标准 Source；拟整合

- exact-v1：[官方 HTML](https://arxiv.org/html/2610.30036v1)；已实读 §3.1–3.3/式1–17、§4.1–4.4/表1–4、结论；[原件](multimodal3-source-2610.30036-v1.txt)。
- 新接口是 learned latent proxy→native DiT KV，监督对象是 query-conditioned 历史attention响应而非仅重构历史token。淘汰visual latent经cross-attention+gated module更新3个proxy latent，额外DiT forward形成各层proxy KV，放在sink与local中间。训练将淘汰KV累积为 positive random feature S/z，对当前query计算近似历史响应，stop-gradient MSE只更新proxy相关参数，DMD共同更新generator+proxy。M=128有限近似不是exact fullcontext，proxy单独归一的attention matching也不保证与sink/local联合softmax后完全相同。
- Wan2.1-1.3B 832×480，16H20/batch32，700short+2300long步骤，60s tuning，sink3/local9/4denoise，最后6层监督。60s128MovieGen prompt 总分80.03 baseline→80.16proxy→82.37+AM，动态贡献大，background/smoothness反退；30s semantic低于LongLive，60s subject/background/smoothness皆非最优。把LongLive窗口12改120在inference质量退、240OOM只是train-test mismatch有限现象，不是长context本身有害。直接以S/z近似替换KV会随时blur，是重要反侧，不将它称精确历史或无损。额外proxy更新+DiT约多13% H20端到端视频生成时间，连同teacher/fakescore/longtuning/统计和cache费用不可忽略。
- actual owner Ch24现有2604.10103两段已讲线性历史统计和先更新再淘汰，但没有“近似统计只当训练靶，部署改用native proxy KV”的分责。位置：其完整第二段起“把这一结构直接装入尚未形成稳定表示的少步生成器”，止“...action-conditioned environment transition。”及marker2604-10103之后；完整下一段起“流式生成器还可把原视频当作每一步都重新构造的条件”之前。
- 逐字 PRE：

> 历史统计也可以只当训练监督，而不直接替换部署 attention：在淘汰前用旧 visual latents 更新固定量 learned proxies，再让它们经过原 DiT 产生 native KV，和 sink/local 一起供新 query 读取。[Attn-Forcing 的受限分支](https://arxiv.org/html/2610.30036v1#S3)以累积 random-feature 统计近似旧历史对当前 query 的响应，只用它监督 proxy；有限统计与单独响应匹配不等完整 joint softmax 精确保留，直接拿统计响应生成反会逐渐模糊。局部消融支持显式 attention-level 训练，却伴一致性指标反退和额外 proxy/DiT 推理费用；teacher、长序列训练、统计与 cache 也付费。精细旧证据、质量或净预算失配时保留更大原生窗口、直接历史/重算与重新锚定，不把固定代理状态批准为无损全历史或无限视频稳定。
>
> <!-- source-family:SF-2026-ARXIV-2610-30036 -->

## P4 2610.30089 ProactEgoMem — 2+1+2=5，标准 Source；仅 Daily track，拟整合

- [exact-v1](https://arxiv.org/html/2610.30089v1) 实读 §3.1–3.3、§4、§5.1–5.4/表3–4、§5.6、K.3 QA 必要；[正文](multimodal3-source-2610.30089-v1.txt)、[K.3](multimodal3-source-2610.30089-v1-K3.txt)。Sci track 不采用，不新增其发现/论证/Books；正文保存含其描述不表示其准入。
- 新命题是捕获本身可失败：Notification单次消息，与Intervention工具start/maintain/stop异步生命周期，再测捕获memory能否答后来问题。Daily是300clips/239source/16h、1242events、1000QA；IC/ST/LT各100clip。给定task prompt引导，不是无任何意图条件的自由自主agent；1fps、每video秒一request、最近10frames、context仅active+最近5complete，unparseable当silence，因此是模拟流而非实测200ms实时SLO。Hungarian先受LLM语义门/时间窗限制再匹配；Start@.2只对matched人口，不能代表all-event及时率；mIoU未匹配为0，检测F1另惩漏报误报。
- Daily最高NotificationF1仅19%，最高InterventionmIoU17.2%，QA不能替生命周期指标。K.3：IC是captured segments+最多40均匀frames；ST/LT只含对象状态/位置和start/end的文字；NoMemory则全clip均匀40frames。Oracle按GTwindows给相应记忆，故memory-vs-oracle差是当前管线的捕获/表示/消费联合作用，不是纯捕获因果量；ST/LT即使oracle也不足70%，提示reading仍受限。强制四选一、模板/LLM语义judge和已有Ego4D原视频不支持“绝无预训泄漏”。全部逐秒视觉调用、tool trace存储、QA/人标与judge均计费；不采用正文将时延唯一归为模型天性/streaming训练因果的宣传。
- actual owner `AGENT-MEMORY` Ch77：“从按需读取到选择性主动干预”已有bank/controller与PASK分开查/打断，但仍假定已有bank，缺“主动取得未来可读证据的开停生命周期”验收。精确位：完整PASK段（起“介入时机还可以与读取预算分开”，止“...批准实际 action。”、marker2604-08000）之后；完整“提醒的另一条受限分支是将未来承诺显式记录为 dated/trigger ledger”之前。
- 逐字 PRE：

> 视觉记忆还要先取得才有得可查，提醒正确不代表捕获生命周期正确：应把单次 notification、后台记录/追踪的 start–maintain–stop，以及后来仅凭已留证据答题分开验收。[ProactEgoMem 的 Daily 协议](https://arxiv.org/html/2610.30089v1#S3)用有限流式窗口观察这些差额，但逐秒模拟调用与 matched-event 的严格时间分数不是实际低延迟保证；高 recall 可以伴大量误打断，较高 QA 也不能补掉漏开、过早停止或不停止。Oracle 与自产 memory 的差还混有表示和后续读出条件，不能直接称纯捕获因果损失。逐帧调用、记录维护、QA 与判分均计费；授权、时机或存储质量不合时保留明确用户触发、固定取样/原证据与 passive retrieval，不让主动保留获得事实或外部行动权限。
>
> <!-- source-family:SF-2026-ARXIV-2610-30089 -->

## P5 2610.30120 ALPS — 2+1+2=5，标准 Source；具体已有覆盖 / NC

- [exact-v1](https://arxiv.org/html/2610.30120v1) 实读 §3.1–3.2、§4共享评价、§5.1–5.4/表1–5、§6限制；[原件](multimodal3-source-2610.30120-v1.txt)。
- 同组ViT-B/16 patch tokens上联合image-text contrastive、captioning、pixel reconstruction与dense crop correspondence（不是仅三项loss；三种用途）。两caption各自softmax避免互负；stage2冻结stage1teacher，已知crop/scale位置queries只预测重叠teacher patches，非学习未知3D correspondence/未见区域。无video预训练不等无teacher知识：synthetic captions来自带CLIP的captioner。12.8B128²+1B224²样本，stage2另5M单图；全部captioner/训练/adapter/probe/policy/WM/decoder费用。
- 15encoders frozen同protocol，stateprobe用16frames和已知未来1/3s动作读simstate，与latent WM未来预测另验。state误差相对Stage1归一、mean六设置，不等真实cm；native text tower n/a不是无语义。重建是另训19k/1k SDXL adapter，不是直接复用train decoder。ALPS均state误差.829但VJEPA-L当前readout .741优于.842；非全任务最强，CLIP分类/LPIPS/MAE重建、Rope/Reacher规划有更强对照。移除重建在10%budget更低state误差，移除caption也改善，不授三目标无代价最优或单个objective唯一因果。stage2三encoder同预算支持局部language retention差，线性平均读出抵消零均变化只是条件解释，不是所有局部更新都zero-mean。simcontrol与planning分开测试，完整language-guided pixel-verifiable planner未交付、真机未验。
- actual owner `MULTIMODAL-REPRESENTATION` Ch23 COMiT完整两段（固定message→语义对齐/flow reconstruction，当前语义和重构需分验、模型更大可语义反退）已承载共同表示的用途/容量取舍；Ch25 latent-state入口明确“reconstruction好不证明control sufficient；必须action-conditioned outcome验”。ALPS是可替代的联合预训与已知几何cross-view refinement实现，所读消融没有推翻这条chain，也没交付完整三用途planner。具体三接口性能/训练条件留报告，不再为一个encoder新增同义“共享token不等所有消费者同优”段；NC不表示未审或排除候选。

## P6 2610.30127 VoxProg — 2+1+2=5，标准 Source；具体已有覆盖 / NC

- [exact-v1](https://arxiv.org/html/2610.30127v1) 实读 §3.1–3.4、§4.1–4.4/表1与三方法消融、§5；[原件](multimodal3-source-2610.30127-v1.txt)。HTML无abstract段，从实际Introduction（不是TOC）保留正文。
- 输入已知mesh/initialposes/目标objectidentity，VLM像素raycast锚点；LLM先写directed evidence graph，local voxel surface grids上array/component/normal选择witness，保view/resolution/source-mesh/provenance，再另写pose program读离散bounds及clipped originalmesh normals求SE3。数值+VLM反馈可分别修选面/姿态；已固定witness在initialworld坐标，candidate更新必须用TT0^-1转换，不是重建真实动态scene。不是从rawcamera自动恢复完整几何，也不是机器人动作轨迹。
- 71人工curated单目标摆放任务，known generatedassets+人工GTpose；DreamSim IArank是同methodpool相对次序，不是绝对intent accuracy，表1 4方法83.10不能与3方法消融66.90直接比较。PhysicalValidity只静态support/interpenetration。MeshEvidence与Vox同95.8，voxel主要提升该pool意图rank；两阶段和反馈本身仍增调用，不能由sharedLLM/config当全预算matched。19RoboCasa+13Open6DOR改成final-state场景不是原闭环任务/真机通过。原件有悬空和碰撞失败，geometry完整性/choice既定，不授languageproof或物理安全。
- actual owner `MULTIMODAL-EMBODIED-VLA` Ch26目前2509.06233完整双对象段已承载“逐面affordance→语言生成几何代价→终态SE3→独立motion planner/controller”的责任链，并明确功能面非接触真值、终态不保证路径/IK、对象/坐标/代价代码来源与费用。VoxelView+witness是这个前端取证/测量接口的组件替代，不改变终态/执行边界；现有论点不要求必须固定keypoints或单次wholemesh程序，因此不需要新平行流水线。局部程序化evidence的可复查细节留报告/原件；NC不把“code执行了”当geometry已认证。

## P7 2610.30129 CADRE — 3+1+2=6，codec 选择反证定点深入；拟整合

- [exact-v1](https://arxiv.org/html/2610.30129v1) 实读 §2–5.3/式1–3/图2–7文字与表1、§7限制，以及直接影响动作/时延解释的D–E完整必要域；[正文](multimodal3-source-2610.30129-v1.txt)、[D–E](multimodal3-source-2610.30129-v1-D-E.txt)。不遍附录图像/全部数据源，不把研究变复现或codec榜单。
- CADRE冻结DINOv3多层feature，每压缩点另训单3Dconv bottleneck（64channels），与time-causal diffusion decoder及one/few-step self-distill组合；“share recipe/architecture”不等所有点共享同一已训decoder权重。7压缩点在4环境同1.2B WM、训练steps/frames/recipe；latent按自身stats规范，noise shift随latent大小/token数变，不是每个数值hyperparam完全相同。CADRE/MIRA同data/extractor/budget对照支持decoder选择；其他off-the-shelf AE预训/参数/data更多，cross-codec不是compression唯一因果。
- 直接选择反证：机器人固定相机与human近固定，相比导航movingcamera，空间/时间压缩的局部代价方向不同。固定s=16扫tau与近1100tokens预算对照区分时间跨度和空间粗化；tau2粗空间robot FVD约2.4×，FID几乎不变、ARR下降；navigation该差小。摄像机运动是leading explanation，但动作/scene/domain也不同，不得写成控制camera变量已唯一证因果。静态camera的长时间latent也有boundary seams，不能说“毫无代价”。同grid autoencoder压缩对WM patching，FVD在2×32²例外、tau8 actionARR .72/.56；不能把像素重建目标唯一因果解释当已完全隔离的证明。
- 评价40realframes/2s→96futureframes/4.8s，2048共同heldoutepisodes最后16frames；FID/FVD/PSNR/LPIPS与ARR分账。ARR是同一每环境冻结probe从8decodedframes读动作，对realR²归一、负R²裁下界-1，再跨dim平均；human102D只评价12wrist维，不能称全部手指控制。48frame-shifted指令control gap有限支持actiondependence，不证明真实因果/安全，data行为support外不保。one/two-stepdecode不同质量/速度不得拼成同配置。
- D严格时序：每latent frame要等其tau个action齐、chunk间causal，chunk内可读取所有tau动作，非每一rawframe严格实时因果。actiondelay含tau/f收集等待+WMcall/cachepass+decode；table4是first-action worst-case、singleH100/batch1/bf16/compile/32latentwarmup后平均kernel时长，最大sustainableFPS≠20Hzdisplay，8-step主文实时演示不能用10-step表4拼接。非causal LTX另window re-decode；所有训练/feature/bottleneck/decoder/distill、40realcontext encode、WM/缓存和decode均计费。230ms人体参考不是通用交互SLO，不采用；policytraining/planning/generalist还未验证。
- actual owner `MULTIMODAL-WORLD-MODELS` Ch25 latent dynamics 入口目前只有“它可以更快rollout，却可能丢失contact...reconstruction好不证明control sufficient”，未讲codec时空stride如何改变action观察delay以及相同图像质量掩盖运动丢失。精确位：完整该段“它可以更快 rollout，却可能丢失 contact、object identity 或安全关键细节。reconstruction 好不证明 latent 对 control sufficient；必须用 action-conditioned outcome 验证。”之后；完整下一段“Latent state也可以先作为训练数据的可更新部分...”之前。
- 逐字 PRE：

> 压缩还会改变何时看见动作后果，而不只减少 tokens：若每个 latent 覆盖多帧、须等这一组 actions 齐全才预测，较大时间 stride 省调用却增加收集等待；chunk 间因果也不等 chunk 内每帧只见过去动作。[CADRE 的受限 codec 对照](https://arxiv.org/html/2610.30129v1#S5)在相同 world-model recipe 下发现，近静态相机的操作更能容忍时间压缩，却可能在图像质量相近时因空间粗化丢掉小区域运动和动作可读性；移动视角导航的局部取舍相反。相机运动仍与场景/动作差异混杂，长 latent 也有接缝，不是通用最优 stride。重建、rollout 画质/运动、动作 probe、收集等待与全部编码/生成/解码费用须分别比较；吞吐和局部计时不授实时控制 SLO。运动、动作支持或 deadline 不合时保留较细空间/时间粒度、原 codec、短预测与真实反馈，不以清晰单帧批准控制充分性。
>
> <!-- source-family:SF-2026-ARXIV-2610-30129 -->

## P8 2610.28814 T-WLA — 2+2+2=6，标准 Source；拟整合

- [exact-v1](https://arxiv.org/html/2610.28814v1) 实读 §3.1–3.4、§4.1–4.4/表1–3、§5及D.1–D.2必要时钟/分母；[正文](multimodal3-source-2610.28814-v1.txt)、[D](multimodal3-source-2610.28814-v1-D.txt)。日期/当窗event复用ARXIV独核，不用submission header反推公告日期，不重开其他Daily。
- visualupdate把当前RGB/instruction/state/FOV和最近K=8 memory sets的query retrieval合成M，生成并缓存baseactionchunk；两次视觉更新间M与base固定。tactile encoder+smallTransformer+FiLM/residual head读causal tactile history和elapsedtime，只改valid/unexecuted位置，缺touch手zeroresidual；每次残差都加在原cachedbase，不是在上次改后动作上累加，防止把它误成积分控制/全计划重算。必要前提base在视觉间隔仍有用，失准时触觉未必救得回。
- futureimage/futurepressure是训练辅助非部署planner。视觉action+image先训，touch先预训，随后冻visual，仅训练touch/editor+image侧adapter/pressurehead，aux不改变控制所用cachedmemory；最后移除两predictionheads。D行动138有效+54padding，H16；pressure前缀索引ceil(cmdrate*elapsedtime)与already-executed mask/评估horizon分开，不能用tactileindex等同真实时钟。
- tactileaugmented baselines同touchstream/encoder/head/optimizationbudget，但native multirate不同，119.1是该protocol有效correctionrate，硬件/全链尾延迟不闭则不授机器人119Hz安全控制SLO。EgoTouch wristlocal MPJPE .50→.35，Tachin .63→.46不代表所有closedloop贡献；robot30demo/task，withtouch50% vs同架构without47.25%，cup仍17→17，SmolVLA50%-16.75%差不能全归touch。去worldprediction是在editor阶段不是从头删pretrain，仅小差，futureaux不证真实worldstate。D contact-filtered是causal-admitted subset、noncontacthand不进分母，不可和unfilteredcompleteheldout混；metrics按valid手/时间先序列平均，EgoTouch再五环境macro，不是全帧pool。无完整trial/hardware/接触安全测试，不复刻或补造。
- actual owner `MULTIMODAL-EMBODIED-VLA` Ch26 Action chunk目前FFDC只“最新视觉verifier触发整段重规划”，Chronos处理capture/execution时钟；缺“同缓存慢视觉计划由快touch只修尚未执行suffix，且残差锚定原base”的可替代修订通路。精确位：完整FFDC段（起“较长 chunk 也可以边执行边检查”，止“...物理提交。”、marker2605-06222）之后；完整下一段“固定序号的 action chunk 隐含观测和执行都落在同一时间网格...”之前。
- 逐字 PRE：

> 中途新接触也不一定要求重跑视觉主干：慢视觉更新可同时缓存任务/历史 memory 与 base action chunk，让较快 tactile editor 读取二者、最新触觉和真实 elapsed time，只为尚未执行的有效位置提出 residual。[T-WLA 的受限接口](https://arxiv.org/html/2610.28814v1#S3)每轮都相对原 cached base 修正，而非不断累加上一轮 residual；训练用的未来图像/压力预测又不进入部署控制。它假设视觉间隔内 base 仍有意义，错计划或未接触时触觉不能保证救回；人手预测改善、有效更新频率与有限机器人成功率也不是同一安全结论。同步标定、memory、触觉/editor训练和完整闭环费用均计入；base 陈旧、触觉缺失或 deadline 不合时保留原动作/零修正、短 chunk、视觉重规划与可信低层 controller，不让局部 residual 自行批准物理提交。
>
> <!-- source-family:SF-2026-ARXIV-2610-28814 -->

本批作者必要层八项已就绪：P1–4/P7–8 六个最小 PRE，P5–6 两个具体 NC。仅送独立复核，不签实际 Books 保存、POST 或日报 DAY。

## 六个 PRE 的实际完整邻段（只作定位快照，不代实际保存后 POST）

### P1 — books/part-03-multimodal-world-models/25-multimodal-world-models.md

完整上段：

> 视频生成先验与几何解码器也可保留各自坐标，只学习两者之间的翻译：冻结 video generator，把其生成的视频 latent 映射到几何 backbone 的中间 tokens，继续用余下网络预测 camera、depth 和一组带时间可见性与速度的显式 primitives；随后换 camera 重渲染同一表示，不必再次生成整段视频。[AEON 的受限构造](https://arxiv.org/html/2610.28631v1#S3)以线性对齐初始化加非线性残差接入，再用 RGB teacher 的几何/属性/feature 与最终 render 监督适配；这不是任意 latent 可直接互换，也没有由单目图像辨识唯一米制世界。有限消融支持 translator、teacher 和 render refinement 各有作用，但未直接证明优于同预算 RGB 解码再重建；生成质量与重建指标不认证 action 后果。恒速/时间 opacity 只在既定 window 内描述所生成场景，未见区域仍会露洞，跨 window 融合仍是待实现方向。几何标注/teacher、各阶段训练、video generation、adapter 与 primitive 驻留及 render 全付费；接口、视角覆盖或动态失配时，保留普通视频、独立 RGB 重建、短 window 与真实观测/可信 simulator，不把可重渲染或局部几何一致签成长期物理世界与控制安全。<!-- source-family:SF-2026-ARXIV-2610-28631 -->

完整下段：

> 可推进状态也可以直接是一组带材料标签的物体与执行器粒子，而不总保留视觉encoder的latent网格。先从立体图与分割提出点云，把位置、给定材料类别和执行器运动共同编码，以attention交互后预测逐粒子位移；[受限多材料分支](https://arxiv.org/html/2506.23126v1)再用点集平均邻距与最坏偏差的混合监督多步rollout，兼顾平均局部对齐与大偏差点。免固定邻接阈值不等真实力/接触图已识别，点集接近也不证明粒子身份、遮挡处状态或守恒；相机、mask、材料与动作时间索引均须随transition版本保存。规划器可比较这些预测，但仍要以真实观测刷新并独立验动作后果，不能把较低预测误差签为控制安全。原件按场景训练，混合loss在部分平均距离反退；立体/分割、粒子attention、多步训练、候选rollout和控制回归全付费。材料或观测支持不足、horizon/费用失配时，保留显式局部图/较短预测、可靠simulator与真实反馈，不由软交互或更完整点云批准通用动力学。
> <!-- source-family:SF-2025-ARXIV-2506-23126 -->

### P2 — books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md

完整上段：

> 推理继续消费自己生成的历史，因此训练可对历史逐帧加入扰动，模拟累积误差而非只见干净 teacher-forcing 条件。该分支支付额外训练、历史压缩与 anchor 依赖，并与 coarse-to-fine 采样、少步蒸馏分别验收；降低 motion 可能改善某些 smoothness/aesthetic 指标，不等于所有质量都更好。[Helios v1 §3.1–3.3、§5.1–5.4](https://arxiv.org/html/2603.04379v1) 的去 anchor、去 frame-aware corruption 消融支持受测长视频中的局部收益，不证明任意长度稳定或通用实时吞吐。精细历史、运动或身份一致性退化时，保留更短生成段、更大历史窗口或既有 dense 路径。<!-- source-family:SF-2026-ARXIV-2603-04379 -->

完整下段：

> 连续视频切到新shot时，近期自产chunk与跨shot参照不能沿用同一默认历史：一个有限cache分支在当前shot保留local窗口，在边界重采已有shots的稀疏帧更新global context，并清空local。每份历史条件保留自己所属shot的caption，另读global caption，而不把新shot文字当作旧帧原来的解释；位置offset只帮助区分来源，不保证零混淆。固定条件预算还会丢细节，历史shots超过预算时有些旧shot不再有样本，不能把global命名当全历史保留或persistent world state。<!-- source-family:SF-2026-ARXIV-2603-25746 -->

### P3 — books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md

完整上段：

> 把这一结构直接装入尚未形成稳定表示的少步生成器，可能压缩噪声并加剧漂移。因此训练可先用 dense attention 蒸馏，再启用 hybrid history/local paths；训练与推理共同采用相同 temporal position cap，并以同初始 noise 的 teacher rollout 对首步 latent 作正则。这个分支支付额外训练、teacher目标构建和历史近似成本，不是免费缩小窗口。作者 Wan1.3B、单 H100、832×480及30秒定量协议只支持所测质量/执行，长视频展示不证明无限稳定，更强 sparsity 也有退步。精细历史或位置外推验收失败时，应保留更长窗口、dense基线或重新训练；本章拥有生成状态迁移，第25章仍须另验 action-conditioned environment transition。

完整下段：

> 流式生成器还可把原视频当作每一步都重新构造的条件，而不先反演它再沿原轨迹编辑：source分支从固定clean帧与本轮noise插值，target分支从自己的clean预测与同一noise继续；分别保存两路历史，再让source/target的Q、K混合及低noise阶段的sourceKV为生成提供约束。两路noise共享不使endpoint相同，trigger-word attention提出的编辑mask也不是物体真值。[有限少步编辑分支](https://arxiv.org/html/2605.21466v1)因此把sampler接口与条件注入分开验收，而不保证编辑区外严格不变。它仍支付双路求值、clean pass/KV、mask及可能的首帧编辑；少NFE不等实时，移除保真约束还能提高编辑成功代理却损坏背景。原文跨硬件秒帧和未计首帧制备不能证明净加速，sourcevelocity残差也不认证target真实误差；保真、编辑语义或预算失配时，保留较强原条件、较多步数/原编辑器与逐段回看，不把流式或免训练名称当无限稳定与无损证书。<!-- source-family:SF-2026-ARXIV-2605-21466 -->

### P4 — books/part-07-agent/77-memory.md

完整上段：

> 介入时机还可以与读取预算分开：先选择 silent、只用当前 Context 的 fast response，或触发较深的 memory retrieval；深读由另一消费者整理返回，主 actor 在读回之后仍可保持沉默。这样避免把“决定查记忆”直接等同“已经值得打断”。[PASK 的受限实现](https://arxiv.org/html/2604.08000v1)复用前一步 workspace 与 event anchor，再异步补 subtree evidence，但旧 anchor 可能漏掉新事件，MemLoader 摘要也不签发 freshness 或事实权限；offline merge 不证明整个生命周期费用恒定。Demand label、summary/memory 条件、消费者版本、超时与最终介入理由应分别记录，模型调用、检索、维护和误打断都计费；其平均 latency 已高于1秒，不能当严格实时保证。状态过期、证据未到或介入质量回归时，回到 passive/always-off、只读当前 Context 或等待刷新，不由三种控制 token 批准实际 action。<!-- source-family:SF-2026-ARXIV-2604-08000 -->

完整下段：

> 提醒的另一条受限分支是将未来承诺显式记录为 dated/trigger ledger，在离线阶段链接到 memory，查询时只做日期或条件匹配和 arithmetic ranking。Ledger 保留 action、触发条件与 resolved 状态，完成后记录 resolution 而不删除事实；open、已触发且未解决时令 b=1，以 cosine·(1+Wb) 调整 linked memory 的分数。[Prospective term](https://arxiv.org/html/2609.22091v1)因而不需要 query-time LLM，但仍有抽取、链接和生命周期维护成本。乘法令 cosine=0 仍为零、负 cosine 未必升分，小 W 也可能救不回深埋记录；增加 W 或加 floor 会改变 relevance 的取舍，不能把“保留 relevance”写成所有排名和授权都安全的定理。

### P7 — books/part-03-multimodal-world-models/25-multimodal-world-models.md

完整上段：

> 它可以更快 rollout，却可能丢失 contact、object identity 或安全关键细节。reconstruction 好不证明 latent 对 control sufficient；必须用 action-conditioned outcome 验证。

完整下段：

> Latent state也可以先作为训练数据的可更新部分，而不要求每次由固定encoder直接给出：初始化一份逐时刻state，每个epoch用当前模型预测下一state，时间移位后回写为下轮输入，序列首state归零；感官mask、分段和偶尔关闭历史attention，再迫使单state携带可续接的信息。这改变了数据state与参数训练的共同生命周期，不把回写出的向量当真实环境标注；跨epoch state identity、mask时是否回写与部署的顺序生成必须分清。

### P8 — books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md

完整上段：

> 较长 chunk 也可以边执行边检查，而不只能固定短周期全部重算：计划时保留预测 future、动作与指令，执行中让小 verifier 对照最新真实 observation，低于配置阈值便重新规划。预测只提供预期，真实新观测才提供偏离证据；verifier 分数不是校准概率，更不是 controller 的安全许可。[FFDC-WAM 的有限对照](https://arxiv.org/html/2605.06222v1)用0.5阈值和部分人工 corruption 负例，不能覆盖所有真实失败；其一次缓存又允许 future tokens 读取更新观测的依赖尚需实现澄清，不授任意 mask 下 KV 精确复用。长 chunk 训练本身与基线不同，真实两任务的成功提高也伴随比短 chunk 更多调用与时间，不能把收益全归 verifier 或宣全费用下降。WAM、verifier、观测与重规划都付费，失配时缩短 chunk、重建计划状态并回真实闭环/独立 controller，不让预测一致代替物理提交。 <!-- source-family:SF-2026-ARXIV-2605-06222 -->

完整下段：

> 固定序号的 action chunk 隐含观测和执行都落在同一时间网格；当多模态 capture 间隔、measurement delay 或推理时间变化时，相同 token 位置便不再代表相同物理间隔。可让观测保留各自 capture time，让 action token 查询预计 execution time，再以 time-aware rotary position 将 pairwise elapsed time送入attention，内容表示不必直接加时间向量；训练的 temporal randomization同时保留原timestamp，使时序变化可被解释。[Chronos 的有限对照](https://arxiv.org/html/2610.13929v1#S3)中，无显式时间的增广在多传感任务反而退步，RoPE也非所有nominal条件最优。异步执行仍需估计延迟、丢弃已过执行时刻的动作并由controller验收，当前fixed action rate不证明任意控制频率迁移。时钟/传感标定、增广训练、估计和完整控制链均付费；时间失真或deadline无法验收时，保留固定网格同步、短chunk、重新观测与可信controller，不让查询时间代签真实执行或安全。<!-- source-family:SF-2026-ARXIV-2610-13929 -->



