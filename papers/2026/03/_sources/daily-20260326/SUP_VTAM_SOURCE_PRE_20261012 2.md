# VTAM necessarySource / sole Ch26 差额与两PRE

2026-10-12，原2+2+3=7/date25不改。[2603.23481v1](https://arxiv.org/html/2603.23481v1) actual必要§3.1–3.3/Eq1–10、§4.1–4.6/T1–2、§5、A训练与B评价、C315的箭头解释。未逐读所有预测示例/图片，不声称code、复现或全部附件通过。支持/直接反侧够即停。

## 可采用接口及直接反侧

两个RGB视角与GelSight触觉图用同video VAE编码，交替intra-view与跨view attention；先以future多视角视觉/触觉latent FM塑造表示，conditioning frame不作预测target。第二阶段把action/virtualforce/propriostate拼成joint FM目标，action expert逐层crossattend视频hidden。forceproxy是no-contact I0→当前It的opticalflow均值ux/uy与平均divergence，**不是标定物理力**；不输入真实force传感器/不能取得物理安全界。原Eq7 action7=EEF6DoF+gripper，state16，condition action/force零填10而保当前state，不等未来proprio实测可见。

必要recipe冲突不可隐藏：A295明确StageII冻结video backbone，故§3.2声称force loss使tactile branch gradient保持平衡/防表示collapse不能直接作为backbone实际更新保证；MSE同形式/λ=1与normalized velocity也不证明每模态方差/梯度自然平衡。§3.3 action EEFpose 与A297 absolute joint position schema未闭合，不猜转换；这些配方与强保证隔离，仍可独立采用“future tactile表示训练→消费该条件的动作头同时预测deformation proxy”接口。joint state prediction不能凭名字保证物理一致性。C315力箭头只是visualization，模型消费raw tactile tokens，无明确force输入。

xArm6/parallelgripper/GelSightMini/两D455，采集与execution30Hz，而每次policy inference1Hz，不等完整决策30Hz/最坏deadline。100chip+105wipe+61peel同步teleop轨迹；VTAM/GE StageI50K、StageII20K/4A10040GB/bf16/ZeRO2/perGPU16/192×256/9frame/54action，GE保持该训练预算；Pi0.5不同pretrainedbase、224²/50action/FSDP与10K任务步，不能全归因forceproxy。inferencehardware/precision/B/solversteps/end-to-endlatency/concurrency/SLO Not Disclosed，不拿训练3.4s/step代替推理。

T1 chip90/peel85/wipe95为作者局部成功率；正文20trial/task总80（flat与45°wipe各20）而三列wipe聚合人口未逐项披露，GE wipe2.5不能冒单20分母。B peeling20连续motions同一fixed cutting position、height逐步变化，不把它当20独立新cucumber；随机初态与consecutive对象依赖、训练seed/区间未披露，不授“预测触觉是普遍必要/vision不可能”。T2chip每variant10次：vision0、latefusion0、noforce10、full90支持该任务局部接口反侧，但未独立剥离全部预训练、future预测/融合/forceproxy组合收益，也未实测balancedgradient。§4.5定性预测不授calibrated contact dynamics。传感器/参考帧/flow制备、双阶段训练、多模态prefill/actionFM与观察刷新全计费；fragile物体break/drop仍安全失败，不由90%自签force上界。

## actual owner 差额与窄锚

actual Ch26完整402–445 World-action（latentfuture/teacher/directpolicy→jointtime→RTP→inverse→World2Act）和943–976 ContactFeedbackLoop完整旧快慢层/ExpForce/MoDE/interactionframe/UMIFT邻接；Ch25/27开篇亦实际回读。World/action分支未承载触觉future同表示训练与joint deformationproxy监督，快慢loop原文拥有当前force memory/reactive proposal correction而非预测触觉训练合同；ExpForce初始force经验不等proxy辅助目标。sole `MULTIMODAL-EMBODIED-VLA` Ch26，不在Ch25复制。

拟插入ContactFeedbackLoop原第三完整段末“安全关键接触任务则不能用学习式 reactive loop 取代经过验证的低层控制器和 human override。”之后、下一完整ExpForce“接触反馈能够修正夹持力…”之前。保旧快慢路径/全部原块，两PRE＋本人纯静态证据注；尚未独核/锁/实际写。

## 两逐字PRE

反应式力反馈之外，接触状态也可以先成为预测表示的训练目标，而不只在动作头末端追加一个传感器通道。一个受限分支把相机与光学触觉图编码到共同视频 latent，先训练未来多视角与触觉变化，再让动作 expert 消费这份条件；动作训练还同时预测由无接触参考图到当前触觉图的光流均值与散度构成的 deformation proxy。这个辅助目标与动作、proprioception 一起去噪，提供接触相关监督，却不是标定物理力或执行器的力命令；参考帧、传感器、时间与目标坐标须随训练和部署绑定。<!-- source-family:SF-2026-ARXIV-2603-23481 -->

预测触觉与 reactive correction 可以共存，不能把局部成功归结为一种普遍必要架构。原实现说明动作阶段冻结视频 backbone，因而不能由辅助 loss 自授其内部梯度已重新平衡；动作坐标的正文与训练说明也未闭合，不照抄为控制配方。有限任务中的少量与连续试验、不同基线预算和定性未来画面不认证 calibrated dynamics 或易碎物体安全，采集与执行频率也不等于完整感知决策 deadline。参考帧/flow 制备、传感器对齐、双阶段训练、条件读取与动作去噪均计费；接触预测、标定、坐标或刷新预算失配时，保留真实新触觉、原视觉 action chunk、reactive loop、已验证低层 controller 与停机/人类接管，由独立安全层决定提交。

## 自身静态证据注PRE

- `SF-2026-ARXIV-2603-23481` — [VTAM exact-v1](https://arxiv.org/html/2603.23481v1)必要§3/Eq1–10、§4/T1–2、§5与A/B及C315；仅future visuo-tactile训练条件与joint deformationproxy辅助目标接口。保未标定力、StageII frozenbackbone与gradient宣传/动作schema不闭合、有限连续trial/基线预算、30Hz≠1Hz决策/未披露完整deadline和制备训练推理全费；不授recipe、calibrated dynamics、普遍必要性或物理安全，未核code/全部图片/复现。
