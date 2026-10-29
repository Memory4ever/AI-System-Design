# 第十包：Ch26四个互斥动作接口差额

完整PRE，未SAVE。Books上下文/ROADMAP与Ch25→26→27交接有效复用；本轮actual完整读下列四处的完整上/下段，必要与key沿本日EVIDENCE_WRITER及R43/R56，不第二Methods/全附件。唯一MULTIMODAL-EMBODIED-VLA，不全章锁，四处gap互斥。

## 12477 HRC / 2+1+2=5

实际必要III-A/B/C/IV-B/D/Algo2与R56 key已成。Ch26现有adaptive subgoal stack/DeCo把计划与完成分权，但没有**变长剩余任务集→固定维连续query→最近任务映射**；这不是新controller或新安全guard。插位在三个时间尺度及完整`让一个大模型直接拥有所有时间尺度...自然边界。`段后、完整CHORUS首段`多个机器人也可共享一套policy权重...`前。完整三个time轴与CHORUS两段已读，不拆两段。

正文：

高层任务集合变化时，策略输出维数不一定随候选数增长：可让policy输出固定维坐标，再由显式映射器在当前剩余任务中选最近目标，交低层planner重新求路径；[受限协作分支](https://arxiv.org/html/2510.12477v1)只有规划/执行反馈成功后才更新任务集与reward。坐标query、被选任务身份、规划请求和实际完成因此是四个对象，最近并不保证最有益、可达或安全；新增/删除任务也会让相同query映到不同对象。应绑定剩余集合revision、距离/同距规则、当前人体/机器人几何和planner结果，不让策略选择自行删任务。抽象任务matrix与有限实体试验不是同一几何人口，同一碰撞guard下策略比较也不证明guard充分。感知/标定、策略训练、全部重规划与失败执行和独立人机安全验收均付费，重规划次数少不等总时间短。集合、几何或反馈失配时，保显式离散选择、已验planner/固定分配与停机接管，不由固定动作维数或任务reward批准真人安全和任意规模任务最优。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12477 -->`

本人末注：

- `SF-2025-ARXIV-2510-12477` — Herschel，Daily2025-10-16补Oct15；旧III-A/B/C/IV-D/Algo2必要及本轮IV-B配置、Cicero R56 key，2+1+2=5。仅变长剩余任务→固定维坐标query→最近task→真实planner反馈差额深入；保抽象matrix非实体geometry、同guard比较非安全/重规划count-time分责及全费。未核代码/复现；整体PRE/真实SAVE/fullselfread/solePOST仅本日canonical实际层。

## 12717 Residual MPC / 2+2+2=6

III/IV/V-A–D必要及R56 key已成。Ch26已有DiffMPC完整段拆GPU批量训练/CPUsolver部署，已有residual段是对原policy动作做局部修正；未承担**简化MPC的力矩与学习joint target经过PD两条控制通道**及两通道互相对抗。插在完整DiffMPC正文与独立marker后、完整`感知与执行重叠时，还须把action buffer...`guard-prefix首段前；上方Sobolev两段/完整DiffMPC、下方LiveVLN两段已读。

正文：

简化动力学prior也可以直接产生一条控制分量，再让学习器补充另一条通道：MPC提出力矩，残差policy给关节目标，经PD转成力矩后共同作用于机体。[受限残差MPC分支](https://arxiv.org/html/2510.12717v1#S3)中，joint-target为零仍可能产生非零PD力矩，不能把数值零等同没有干预；残差亦可能对抗原MPC，简化floating-base约束更没有自动覆盖所有关节/self-collision。两通道的单位、控制率、增益/饱和、状态和solver版本须共同绑定，分别验先验误差、组合动作与真实反馈；不同动作空间采用相同正则系数也不等同约束强度。训练端批量GPU求解可复用每次solve的因子分解，部署却是另一个CPU solver，批量每秒环境step不能替在线控制deadline；残差训练在所测设置中仍慢于端到端基线。模型/编译、矩阵分解与回代、全部rollout/训练、CPU迁移和实体回归均付费。先验失效、通道对抗或真实动力学/预算失配时，保可信原controller、单通道受限适配、重新标定或停机，不由仿真稳定和名义100Hz批准力矩安全与普遍净加速。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12717 -->`

本人末注：

- `SF-2025-ARXIV-2510-12717` — Herschel，Daily2025-10-16补Oct15；exact-v1 III/IV/V-A–D必要，Cicero R56 key，2+2+2=6。仅MPC torque/learned joint-target→PD双控制通道、solver训练/部署分账差额深入；保零joint非零torque、动作尺度混杂、简化约束/实机反侧、残差训练更慢及全费。未核图像素/代码/复现，不授完整碰撞/在线SLO；整体PRE/SAVE/fullselfread/solePOST仅本日canonical实际层。

## 12392 Self-Guidance / 2+2+2=6

§3/4/6与R43 key已成。已有Rolling段改变旧tail/fresh noise比例与去噪预算，已有检索futurechunk段改参考输入；没有**同一noisy action的当前/过去状态两score差分及queue续接/替换分责**。插在完整Rolling段/inline marker后、完整`检索到的动作也不必直接替换当前chunk...`前；上方memoization完整接口/回退、Rolling与下方检索完整段都实际读。

正文：

同一轮动作去噪还可以比较当前与过去状态给出的两份score，以它们的差分调节本次proposal，而不把过去条件或局部外推升级为未来真实观察。[受限self-guidance分支](https://arxiv.org/html/2510.12392v1#S3)可把两个条件拼成一次batched调用，但两条计算分支仍有费用；局部平滑/短时差假设也不保证接触突变时预测正确。其队列另按新旧首动作的接近程度决定延续旧tail并补末端，还是替换队列；每步仍产生新chunk，相似度只是续接proposal，不是跳过重规划或保物理连续性的证书。应绑定两状态的时刻、同一noise身份、guidance幅度、queue及已执行prefix，分别验轨迹质量、反馈新鲜度和真实控制率。有限单任务实体对照不授通用VLA/未来观测能力，adaptive chunking成本亦可接近closed-loop。全部双条件前向、每步生成/比较、队列维护和独立闭环回归均付费；状态突变、score或续接失配时，清空旧tail、fresh短chunk重算并交原controller，不由一次API调用或更平滑动作批准零额外算力和安全执行。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12392 -->`

本人末注：

- `SF-2025-ARXIV-2510-12392` — Herschel，Daily2025-10-16补Oct15；exact-v1 §3/4/6必要与Cicero R43 key，2+2+2=6。仅current/past同noise双score与queue续旧/替换差额深入；保Taylor记号未齐/局部假设、每步新chunk、batched双分支非免费、单pick-place及全费，不授未来观测/通用VLA或物理安全。未核代码/复现；整体PRE/SAVE/fullselfread/solePOST仅本日canonical实际层。

## 12724 TRO-Grasp / 2+2+2=6

III/IV/F必要与R56 key已成。Ch26完整跨手codec两段以本体专属latent decoder恢复joint；前canonical geometry两段仍不是**用各link pose作节点/相对几何作边，先松关节再IK恢复**。插在完整跨手codec第二段/inline SF2603-10158 marker后、完整`共享动作码还可以主要服务训练对齐...`前；完整canonical上两段、跨手两段与下方UniT两段已读，不拆旧source-family。

正文：

跨手抓握也可先避开不同关节数，直接在各link的刚体pose上生成：节点保存SE(3)姿态，相对边由节点重新计算，在放松关节连接的空间去噪，再由目标本体IK恢复原生joint。[受限关系表示分支](https://arxiv.org/html/2510.12724v1#S3)由此把关系自洽与机构可执行性分成前后两层，网络输出自身不包含完整collision/joint-limit保证，后续IK亦须独立检查而非只证明可解。URDF/几何编码、link对应/填充、坐标与本体decoder、观察支持和IK版本必须共同保存；多手训练不等任意新手zero-shot，训练测试都有的部分遮挡也不等未知遮挡泛化。固定batch的内存与各自max-fit的吞吐是不同预算，局部含IK每grasp速率不代表完整感知到执行SLO；扰动下位移小也不是所有抓握安全。几何/codec训练、图构造、全部denoising、IK与实体抓持/碰撞回归均付费；新本体、遮挡、可达或接触失配时，保原生joint模型、目标手示教与已验显式planner/controller，必要时拒绝抓取，不由关系一致批准物理提交。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12724 -->`

本人末注：

- `SF-2025-ARXIV-2510-12724` — Herschel，Daily2025-10-16补Oct15；exact-v1 III/IV/AppendixF必要及Cicero R56 key，2+2+2=6。仅link-SE3 node/derived edges→relaxed graph→目标IK/joint consumer差额深入；保新hand zero-shot差、50%遮挡人口、batch/maxfit分责和全费，不授SO3全域recipe/网络硬碰撞或SLO。未核代码/复现；整体PRE/SAVE/fullselfread/solePOST仅本日canonical实际层。

四项请sole reader整体正文/独立marker/本人注PRE；若已成必要足不重Methods，实际缺层只核采用差额。尚未SAVE/POST，无全章锁/root第三批准。
