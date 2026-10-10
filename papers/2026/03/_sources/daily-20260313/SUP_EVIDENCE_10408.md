# 10408 Motion Forcing：共享双时钟深度producer/外观consumer必要Source/PRE（待非作者）

只03-13补Mar12自然日。完整v1题摘/准入及DATE3日级Mar12已独核有效复用；本次实际题名/五作者/完整AB/history对回SUP_ABS3_10408.txt，SubmittedMar11T04:44:46Z/registeredMar12T02:00:46Z（实际DATE3原字段），v1无可见withdraw/correction/具名venue。项目link只身份，不要求遍历repo证明不存在早稿；Sep26v2不以号码扩审。官方 https://arxiv.org/html/2603.10408v1 GET200/198893bytes/UTC2026-10-10T01:52:52.412875Z，SUP_CORE_10408.raw/txt及manifest/result已保存。

## 具体增量与拟评分

给定pose/depth同时引导一个RGB生成状态便于复用旧模型，却不显式分开“深度怎样产生”与“外观怎样消费”→本文在一个共享DiT中temporal-concat depth/RGB两个latent流，用各自timestep调制，训练随机只去噪一个流、另一流分别固定pure-noise或clean-depth→部署先完成depth，再冻结预测depth/重抽RGBnoise做第二loop。这改变中间条件的生产、训练支持与两次消费状态，不只是Point/Shape/Appearance标签或把既有control模块拼一起。Masked point corruption是训练支持配方，不单凭它或Physics-IQ奖励声称发现物理定律。

拟 **2+1+2=5**：共享backbone两模式的中间depth生产→外观固定消费接口重要替代2；仍单视频生成路径1，不因两个流、自动驾驶/robot标签或World Model名字抬跨系统；teacher clean-depth训练与predicted-depth部署、两个clock和两loop须共同验收的稳定支持边界2，不借普通teacher-forcing/双模态/几何真实性成熟原则抬基础。actual Ch24具体缺口及强物理保证/预算反侧触发必要局部深入；只有受限视频生成接口拟采用，不授closed-loop World Model/动作执行。

## 必要原件实际读取

精确v1直接§3.1–3.5完整（449–1241），Eq1–8与训练/推理两模式全部，§4所有setup/Tables1–2/4.1–4.2、§5完整限制（1242–1507）。2253行后半主要references，不遍历其余旧论文/原视频/代码。Figure1/3–6只caption，未看pixels或videos；不能据caption签全部collision/robotgeneralization。首次宽Books检索输出截断只发现，实际target局部另完整读1568–1584与311–329，Ch25章首1–33完整界定相邻owner。

Point：每object逐帧最大内切圆centroid/radius绘canvas再VAE编码，半径只是投影尺度相关，不能唯一恢复object深度/形状/密度/碰撞。Camera perframe R/t/K由VGGT估计；Eq1–3从首depth D0 unproject→targetcamera project→splat作为conditioning W，不是每帧重新观测真实depth。正文最后明确splat的**值仍D0(u)**，不是显式targetcamera z；若R=I、首点z3、target t_z=−1，targetcamera z应2但W仍写3。它可作为带reference-depth身份的control cue，本包不认定代码必错或全部条件无效，但不把这份W叫已验证的metric目标深度。首depth/标签来源、invalid/遮挡/holes、坐标标定未由所读setting闭合。

共享DiT：two independent diffusion timesteps τd/τv，two streams temporal-concat，conditions I0/P/W各VAE后channel-concat，AdaLN在两stream用各timestep的scale/shift；norm_out又依次用两embedding。双clock是控制不同corruption状态，不等表示/梯度或语义严格解耦。ModeI τv=Tmax固定noise，只depth τd采uniform0..Tmax−1，depthloss；ModeII τd=0用完整clean-depth标签，只RGB τv采同range，RGBloss；stochastic switch选择一mode，不等同时独立采两clock全组合训练，mode频率/完整实施细节未披露不补造。

MPR：ego W与object P各在uniform.3..1 cutoff后truncate，spatial Bernoulli wholeobjecttrajectory drop，始终监督完整depth。pdrop具体数值、三mask联合频率/边界object输入来源未披露；正文“从targetD deduce”是训练监督，不可读成推理带未来GT。初始I0依旧含物体/场景；去掉未来controls并恢复depth可学数据关联，未由本文独立验证惯性/因果/碰撞定律。Table2没有MPR开关对照，不把其他替代的收益唯一归给masking。

Inference：stage1两流随机初始化，固定RGBnoise到depth完成；stage2固定**预测**depth latent（τd=0），重新抽RGBnoise另DDIMloop。训练ModeII用clean标签而部署用可能有误的prediction，不保证renderer训练覆盖这类中间误差；depth“可inspect/edit”是可观察的接口，不是论文实现了独立verifier/必经acceptance gate。生成depth存在错误或手改depth域外时，appearance可以继续放大同一错误。本包只采用先生产/再消费分责与验收需求，不认证已做teacher-predictedmix训练或新闭环执行。

## 关键评价/反侧/资源

主Table1作者100Waymo test videos：ours FVD157.8，低于MOFA272.6但**差于one-stage152.4、Seed112.5/Wan118.3**（更低更好）；FVMD205.2优于one-stage218.4/Seed345.6/Wan316.2，Physics-IQ33.2优于one-stage28.7/Seed30.5/Wan31.2。支持本文配置中中间depth与motion/物理proxy的取舍，不是三目标同胜或“trilemma稳定”。单阶段版本与两阶段完整denoising work/预算是否匹配未给，不能只归因dualclock而排除更多NFE/训练支持差异；closed baselines读取text、MOFA读取different trajectory/scenecontrols，输入条件不是同一人口。

Table2替segmentation167/228.8/29.7、opticalflow173/224.3/28.4、softmaxsplat160.3/251.7/28.5、cameraAdaLN159.6/243.8/29.1，作者当前setup中ours较好；没有CI/seed重复信息、外观/几何处理的数据量与全训练预算单因果控制，所以不签“每个组件都物理必需”/任意backbone。Physion与Jaco Play只有所读qualitative说明/caption，没有同等quantitative合同或真实机器人执行数据；可保图像生成场景，不授机器人动作安全/控制器能力。限制明确密集行人/骑行者及高度遮挡会退化、depth会错occlusion ordering，需保原I2V/more explicit控制退路。

CogVideoX1.5-5B-I2V fine-tune，8H100/DeepSpeedZeRO2/BF16，AdamWlr1e−5 β(.9,.95)/WD1e−4 warmup100，33frames320×480stride2，10epochs/effectiveB8。Waymo/DrivingDojo/YouTube，样本总量/划分细节、GT-depth如何生产、two-mode比例、DDIM两loop NFE/CFG、所有preprocess/pose/depth/VAE预算、wallclock/memory/batchconcurrency/tailSLO Not Disclosed。没有免费“单unified model”或实时/全部预算优势；two loops串行且shared attention仍消费两个latent流。没有artifact/视频pixels/复现 claim。

## actual唯一owner/差额

ROADMAP `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24。实际1568–1584相机/动画时钟→Camera/Motion分阶段交接两段→交互视频稀疏控制两段全local；311–329 sparse-scaffold/FlexAM、shared motion+video CoMoVi两完整段与上下游全读。已有早pose+depth后pose的condition strength schedule，也已有两个noisy producer共同推进/3Dhead另读；都不等**同一backbone随机固定另一流的训练mode，以及depth先完成后在第二loop固定消费**。已有边界保留，不按depth主题泛NC，不算这些旧原则为新增。

Ch25章首1–33实际区分video/predictive/actionconditionedstate；此稿control是投影trajectory与camera，未测动作后果、uncertainty/observation correction/persistentstate，不将其自动升级Ch25worldstate/Ch26真实动作owner。Ch23负责表示来源，Ch24拥有clock/生成条件支持与采样consumer；唯一Ch24，不建第二owner或结构候选。

拟在Camera/Motion原semantic-body-binding两段与end注之后、稀疏交互control两段之前窄写，不插原一条论证中间。

### 逐字PRE

中间几何也可以先生成，再交给外观分支消费，而不只是随去噪时刻减弱已有 depth 条件。一条受限视频分支在共享 DiT 中排列 depth 与 RGB 两个 latent 流，各用自己的 timestep 调制；训练轮流固定 RGB 为纯噪声去预测 depth，或固定 clean depth 标签去生成 RGB。部署先完成 depth，再固定这份预测、重新初始化 RGB 噪声执行第二条去噪 loop。稀疏对象点与相机重投影只提供控制线索；截断或删去部分轨迹后恢复完整 depth 是训练支持，不把生成几何批准为观测事实或已学物理定律。

[Motion Forcing 的有限视频对照](https://arxiv.org/html/2603.10408v1)支持这项生成条件交接，运动和物理 proxy 改善仍伴 FVD 反退；不同输入与两阶段工作量不构成所有变量相同的因果对照。训练消费 clean depth、部署消费预测 depth，几何误差和域外编辑需要分别验收，能查看中间结果不等已有 verifier。点/相机/深度标签制备、共享模型训练、两个 latent 流和两条采样 loop 都付费；密集小对象、遮挡或条件支持失配时，保留单阶段 I2V、更明确的控制与独立几何/视频检查，而不由画面逼真批准 World Model 的动作后果或机器人执行。<!-- source-family:SF-2026-ARXIV-2603-10408 -->

## 停点

以上为原PRE准备停点。后续root非准备者实际Source/Ch24与Ch25边界/逐字PRE通过并窄写两段；本作者非Books writer实际1558–1608完整局部/1923本人注回§3.3–3.5，SUP_POST_10408.md POST通过，root已回读并同步本人注PASS/放锁。本日正式36第19整合家族，2+1+2=5必要局部深入，不授DAY。未由本作者改Books/State/索引，不补未来GT推理或真实robot/physics证据；未读代码/视频不伪造外部blocked，不扩全附件/其他日期。
