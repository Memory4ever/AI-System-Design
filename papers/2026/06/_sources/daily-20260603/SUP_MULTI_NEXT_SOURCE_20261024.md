# 06-03 多模态单篇必要审阅

## 00299 Real2SAM2Real：几何cache是生成条件，不是真实动态状态

root作者；沿R62完整题摘/具体贡献与Jun02联合日证，不第三日期。实际打开[当前abs](https://arxiv.org/abs/2606.00299)，所见v2/Oct13修订无撤回提示；本次只用[exact-v1 HTML](https://arxiv.org/html/2606.00299v1)§3、§4.1–4.4/T1–2与§5，不把当前约2000样本倒入v1的300。未看图像素、附录、代码或复现；无性能采用，不为补主文未披露的hardware/采样费扩无关附件。

必要判断：单图生成前景完整mesh并由用户对象/相机轨迹渲染masked normals；背景仍由视频prior补。Normal条件经VAE/patch embedding加到视频hidden，绕过appearance reference tokens；训练用视频估计normals加实例级扰动。生成隐面、用户轨迹与真实观察不同，闭合mesh不证明隐藏几何正确、物理运动或环境动力学。冻结base仍有LoRA更新，不凭“完全保留prior/消除所有歧义”采用绝对主张。

评价边界：v1 Wan2.2-I2V-A14B/300 clips/720p81frames，200camera cases与100object cases；T1完整方案RPE-R不如ReCamMaster，部分消融motion smoothness还更高，故非全指标胜。Warp基线使用同WorldForge proxy，不等各方案整体几何输入相同；GLOMAP/Evo/VBench是代理而非真实几何/控制许可。硬件、全采样与CI主文未披露；资产生成、伪标、扰动、LoRA、render/生成与独立验收全计费。只保接口取舍，不引性能数字进书。

拟2+2+2=6：具体geometry/appearance分路及软条件化；跨资产/训练条件/视频consumer；可复用的隐面与条件责任界限。actual `MULTIMODAL-WORLD-MODELS` Ch25已实读Persistent world state开篇、VerseCrafter两段、E³C完整段及前后，邻Ch24/26开篇职责。已有中心/协方差和静态点云，不含完整前景cache→normal-only软注入/训练估计与推理渲染两类条件差额；只补一自然段，不另设owner或复制diffusion目标。

### 最小逐字PRE，未独核/未写

完整前锚：

评价也必须匹配载荷：ObjMC 检查中心控制，不独立认证完整 covariance、遮挡或深度；静态 aesthetic 54.78 仍低于对照 55.52。作者采用冻结 Wan2.1-14B、81 frames、1–6 对象和 16×96GB GPU/380h 的有限设置，depth/mask 估计、几何 renderer、adapter 与生成费用都在主干之外。几何失配或长 rollout 不稳时，保留原短 horizon、camera-only/观测条件生成，以新观测重建几何，不让扩大对象状态替代真实控制验收。

拟增：

仅保存已见表面会在大幅转视角或遮挡后留下空洞，另一条[受限分支](https://arxiv.org/html/2606.00299v1#S3)先生成可编辑的完整前景mesh，由给定对象运动与camera轨迹渲染masked normals，外观仍来自参考图、背景仍由视频prior补全。几何条件经软加性注入绕过外观reference tokens；训练用视频估计的normal与实例扰动，缓解其和推理时粗mesh渲染条件的差异。它增加资产生成、伪标、适配、渲染与采样成本，生成的隐藏面不是真实新观测，用户给定的运动也不是学得的物理transition；有限相机/对象评价还有反退，不能认证完全解耦或无歧义。几何、条件支持或质量失配时，保留已测资产、原观测条件生成和短horizon重置，不让可编辑cache取得真实状态或动作提交权。<!-- source-family:SF-2026-ARXIV-2606-00299 -->

完整后锚：

静态空间载荷与人的运动条件也可以分路：把历史视图重建的稀疏点云及逐点外观特征渲染到目标相机视角，以保持已见场景；另将完整目标 ego 关节与手腕姿态编码成常驻 tokens，让身体离开画面或自遮挡时，运动条件不随二维骨架投影一起消失。这是在给定未来相机与人体轨迹下的条件生成，不是模型已预测未来动作或真实环境 dynamics；常驻条件也不等可更新的物理世界状态。E³C 的有限分支依赖 mostly-static 场景、SLAM/标定与动作监督，未显式输入 visibility/depth，生成器补出的纹理仍不是新观测，人物出视野再入时外观也可能漂移。几何与外观制备、姿态估计/编码、训练、全部采样与独立几何/控制验收均计费；地图、姿态或动态场景支持不可靠时，保留显式 renderer、短段观测条件与真实重观测，不让较高视频质量或 pose adherence 签发行动安全。<!-- source-family:SF-2026-ARXIV-2605-26316 -->

本人true-H2注只在独核通过且真实保存后记录实际状态。其余22项尚未必要，不预I/DAY；不把一篇review变成全3D领域补扫。

## 00267 StressDream：局部压力提案不等条件风险分布

root作者；R62题摘/贡献/Jun02联合日证复用。实际打开[当前官方abs](https://arxiv.org/abs/2606.00267)，所见v2 Oct06无撤回/勘误提示，不读后版方法；必要[exact-v1](https://arxiv.org/html/2606.00267v1)§3–4、6、B.6、D.4–5、F实际读完，停止于本命题支持/关键反侧。原HTML的pgf/TeX annotation造成首次输出截断，未冒已读；后定点剔重复annotation/SVG再读§4完整6350字元，公式只采可读的目标分责，不把残损Eq8补为已核实现。未看图像素、代码或复现，不做全部B浓缩证明/E例图。

机制是固定观察/action的diffusion初始noise局部优化：VLM yes/no log-prob差提供语义目标，半径/随机分块二阶矩/谱白化作Gaussian prior的regularizers，近似noise梯度免完整denoiser反传。它们不认证物理正确或校准条件后验；F明确local而非global search、base WM不含的真实分支不能补出、reward hacking和多段noise顺序优化。相同N候选/iteration不等相同费用，B.6还要verifier backward；单H100 Vista 50step样本1–2min/20次优化约30min只是作者配置，不授实时。§6驾驶100目标事件+200临碰片段、操控100failure轨迹是选定人口；D.4 heldout WMB/Gemini与操控人审不变真实物理oracle。D.5仅40成功demonstration/task再按imagined风险调loss与sampling，10kstep/H100、20rollout/task的有限支持不隔离两重加权或一般安全。保作者有限政策改善，不删正面观察；无图像素/完整预算或CI认证，不引比率进书。

拟2+2+2=6：noise提案/语义criterion/regularizer接口，跨生成与评估/训练消费者，可复用的压力样本与风险估计分责。actual Ch25已读条件分布评价前后完整组与Ch24/26职责，现文有重复采样/reference分布和planner诱导覆盖，但没有该局部noise压力接口，不能称完整已有覆盖。拟紧接“即使分布更接近reference…matched-budget policy evaluation…”完整段后、24578动作代数组之前单段，保原H3/原组不重排。

### 00267最小逐字PRE，未独核/未写

完整上锚：

它把 world model 从 plausible video generator 进一步约束为 stochastic transition sampler。代价是更高采样成本、outcome
离散化误差、reference distribution 构造成本和 seed/runtime identity；有限样本下没有观察到某个 rare outcome，也不证明
它的概率为零。单次 deterministic transition test 在近确定性场景、smoke test 或预算很低时仍合理；只有环境固有随机性会
影响 planning/risk 时，distribution-level alignment 才成为发布条件。即使分布更接近 reference，也仍需 matched-budget
policy evaluation 才能证明它改善决策。

拟增：

重复随机采样难以发现低频高影响结果时，可另设一条压力提案路径：固定初始观察与候选action，局部调整视频diffusion的初始noise，让VLM语义目标寻找指定失败，同时以noise半径、分块二阶矩和谱统计限制偏离原先验。[StressDream的受限分支](https://arxiv.org/html/2606.00267v1#S4)用近似梯度免完整去噪反传，仍支付全部生成、verifier与反向费用；相同iteration数不等相同预算。这些正则只约束learned WM所支持的生成，不能修复base物理错误、找回缺失的真实分支或保证全局最坏结果；VLM还可能被reward hacking利用。应把定向发现的风险样本与独立随机采样的频率分账，不能用压力命中率估真实风险概率；用于轨迹重权训练后还要验真实策略结果。支持、criterion或预算不合时，保随机/已验simulator压力测试、短horizon与真实反馈，不让“看似合理的最坏想象”取得安全或动作提交权。<!-- source-family:SF-2026-ARXIV-2606-00267 -->

完整下锚：

<!-- semantic-body-binding:SF-2026-ARXIV-2605-24578:start -->
只比较像素或 latent 预测误差，在 action 很弱、评估只关心下一帧时成本最低；它却无法回答模型是否学到了 action 的代数结构。对具有 identity、inverse 与 composition 的环境，更强的诊断是固定初态，分别执行空动作、动作及其逆、以及组合动作，检查预测状态是否满足相应关系。这样可以把“画面像”推进到“transition 对 action 可组合”的受限证据。

这些 probe 仍只是结构化 surrogate。它们降低了发现动力学错误的成本，却依赖 pose recovery、group-action 假设和可辨识的状态表示；latent 中满足近似等式不等于真实环境也满足。假设失效、恢复误差过大或 probe 与任务结果分离时，应回退真实 rollout、传感器状态测量与 planner-induced evaluation，而不是把代数一致性当成完整物理正确性。现有证据只覆盖论文定义的 action family、regularization 与实验环境。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-24578:end -->
<!-- source-family:SF-2026-ARXIV-2605-24578 -->

本人trueH2注待必要/actualowner/PRE独核后才随真存，未I/DAY。其余21项尚未本轮必要，不把本任务扩到真实机器人部署、完整噪声证明或所有worldmodel论文。

## 02486 AHEAD：预测式补时不等低方差就安全

root，2026-10-25；独立06-03补Jun02自然日，R62完整题摘/贡献/联合日证复用。当前[官方abs](https://arxiv.org/abs/2606.02486)见v2 Oct03，无撤回/勘误提示；只采用[exact-v1 HTML](https://arxiv.org/html/2606.02486v1)，实际必要读§3–6、B.3/B.5–8、C.5–6、D.1与E.2–5。浏览器文本Table15–16也已读；未看图像素、代码或复现，不冒全附件。方法/直接反侧已足，不为未采用精数扩读所有baseline实现。

正式拟2+2+2=6：当前观察到执行之间对象移动→冻结VLA特征上的选择性预测、运动外推及sample-variance horizon→比较缩短推理与改变动作条件两种补时设计；不是泛机器人关联或单成功率。具体gap按受影响域深入。

§4.1–4.3以三帧RAFT光流/差分形成每patch速度加速度，语言相关或运动floor选patch；条件flow逐步预测，未选patch保当前值，decoder读取拼回grid的未来条件。固定加速度只在短时适用，image-plane flow不恢复depth。多个样本方差越训练阈值或达到cap即停；这是sample proxy非校准风险，不能自行把首次越界步改成已实现的最后安全步、也未证明预测时点恰等实测sensor-to-actuation延迟。§6.1称共享RAFT估计且未完整传播速度不确定性，B.6另有按速度5%加Gaussian噪声；保两处限定，不把启发噪声当可靠校准或照录完整不确定recipe。

B.7另以冻结动作decoder的输出差训练feature alignment，故feature-MSE低不单独证明consumer动作同语义；其validation来源用于训练alignment，不能称全程未见heldout测试。§4.4/B.8 manipulation视频预训/约200本体轨迹适配，冻结基础VLA不等免训练或保所有原能力。B.3单H10080GB、224²、bf16、parallel/chunk action head的约158ms仅作者点计时，无尾部deadline；E.5 S1/3/5/10开销递增，不能复述“并行sample无额外费”。C.6全部pretrain/alignment/fine-tune仍计费，未给完整部署并发或物理SLO。

§5模拟5seed×100rollout/cell、实机五任务各30次，速度sweep每点10次，不混人口；baseline训练预算、动作接口/数据仍不同，静态case接近不唯一隔离全部预测因果。E.2 rolling-ball constant-velocity切片可更好，E.3 full prediction的pole-push可更好；E.4固定K5/8的最优随场景，不能用它证明adaptive在chaotic上优于固定，D.1明确该ablation留待后续。撞击/遮挡及深度运动破近似；真机失败含joint-limit guard、迟到与接触弹出，几何目标正确不保证当时可达/可执行。其有限正面成功保留，但不授任意本体、普遍实时或物理安全。

实际owner为`MULTIMODAL-EMBODIED-VLA` Ch26。已读本章开篇、world-action三接口、state/freshness、latency、fast-slow及chunk分工；邻Ch25预测状态/风险与Ch27数据能力链交接已读。现有低频预测几何、异步缓存/短chunk与未来latent条件均有效，尚未具体承载**独立运动patch→当前/未来grid拼接供冻结decoder→样本方差限制预测视野**的补时分支，不用主题相近判完整已有覆盖。只拟在Latency H2后、原“压缩动作专家之前”完整段前两自然段，不新增owner/H3、不改原压缩论证；未授写位/未写书。

### 02486最小逐字PRE，待首次独核

上锚为唯一`## Latency 与 control frequency`；其前完整base-action residual段保留，分节不移动。

拟增两段：

场景在观察到执行之间已经移动时，只缩短推理仍可能追着旧位置行动；另一条补时分支先在冻结VLA的feature空间预测未来条件，再交给原动作decoder。用短观察序列估计patch运动，以语言相关性和运动选择要预测的位置，未选部分保当前feature；选中部分由条件flow展开，经单独的动作敏感alignment后拼回输入grid。[AHEAD的受限分支](https://arxiv.org/html/2606.02486v1#S4)再以多个预测样本的方差限制展开视野。它改变的是动作消费者所见的时点，不是获得未来新观测；冻结主干也不免预测器、对齐层和本体适配训练。

短时加速度外推会在碰撞、遮挡或深度运动中失配，样本共享的运动估计及启发噪声也不能给出完整校准；低方差不是物理安全或“未来恰好等于执行时刻”的证明。更多样本、光流、展开、对齐和原action head均计费，单GPU平均计时不能替完整控制deadline；有限对照仍有更简单运动模型或全patch预测更好的切片，固定视野和自适应停止也未在所有扰动上完成同预算比较。执行器仍须检查可达性、时限与真实反馈；运动支持、预测条件或预算不可靠时，缩短视野、重新观察，保留原reactive policy、显式状态估计和独立controller/停止接管，不由较高局部抓取率批准开放环境行动。<!-- source-family:SF-2026-ARXIV-2606-02486 -->

完整下锚：

压缩动作专家之前，还应先检验已有checkpoint是否真的需要全部积分步。固定policy、观测初态与噪声，配对比较一次Euler和原步数，再用预先声明的质量等价界而非“不显著”判断是否可省。[六种flow VLA的受限研究](https://arxiv.org/html/2610.30735v1#S3)发现充分训练与较强预训表征下常有这种零重训分支，但部分小模型、长任务和早停checkpoint仍有差异；真机样本不足以确认同样等价，单步还可能减少有效动作模式。少一次action-head求值不等整机频率同比提升，配对回归、感知与控制都计费；任务质量、行为多样性或完整deadline不合时，保留原多步、较短执行段与独立controller，不把局部一步成功外推为所有flow、RL更新或安全保证。<!-- source-family:SF-2026-ARXIV-2610-30735 -->

true-H2本人注只在必要/actualowner/PRE独核及真实保存后记事实。原00267 R81真实POST有效，待Report行政同步；02486尚未独核、未I/DAY，其余20项尚未必要，不因本包扩大导航或异地机器人实验。

## 00773 SafeVLA-Bench：先声明哪些约束适用，再比较成功与违例

root，2026-10-25；R62题摘/准入/Jun02联合日证有效复用。当前[abs](https://arxiv.org/abs/2606.00773)为v3/Oct02，无所见撤回/勘误标记；只用[exact-v1](https://arxiv.org/html/2606.00773v1)，不将v3的27entries/后训练case倒填v1的9entries。已必要读§3–5/Eq1/T2–5、C.2–6/D及E统计方法；未看图像素、代码、全部分任务CI或复现。支持与直接反侧足，停止。

实际增量是task机制/物体/可用信号决定适用谓词，再保留success×violation联合人口与最坏违例深度；不是泛“成功不安全”。正式拟2+2+2=6：新增具体测量接口/有效性条件、跨task-policy评估选择、可复用长期边界。初筛暂拟Design3基于可能修正只看成功的判断，必要层确认现书早已不以success签安全，故实际新命题不计该成熟原则，只计接口Delta2；不是因访问/工作量/拟处置降分。安全测量及具体gap仍深入。

§3.1–3.2可用信号、真实referent、任务是否本来要求该行为共同决定active set。插酒瓶必须倾斜、拉抽屉必须移动，不能被无条件标签误判；复合任务的invalidating tag按全episode排除，除非另做phase-segmented scoring，故少违例也可能是覆盖较窄。正文84→27同时改orientation语义与applicability，不把差额全归registry。C.5/6没有接触/actuator信息的host不能无代价迁移；纯平滑/速度等因缺风险context只诊断不计安全conjunction。

§3.3 SBU是全部rollout中success且unsafe的联合比例，SBU/SR才是成功条件下unsafe；Safety为全部rollout中满足active conjunction的比例。VSI是各适用谓词负robustness按严重锚线性归一/clip后取每episode最坏，再跨episode平均，不是持续伤害总量/真实风险。二值self-collision直接饱和不等校准深度；调严重锚/适用集会改排名。阈值为透明simulator proxy，不能从ISO名称认证实际硬件安全，亦不直接复制具体阈值进书。

§4五LIBERO策略×四suite、四RoboCasa策略，200/2000/900不同人口；作者保持native protocol和固定seed可比，不是同训练/相同能力预算的因果试验。T4 OpenVLA低SBU但高VSI、T5高SR不随Safety同序，支持分项诊断而非RL必更安全。A.4/正文阈值变化会显著改Safety，有限放宽后非零仍只限这些规则。E Wilson/episode-bootstrap把阈值当固定，未覆盖规范选择不确定性，不能视作多训练seed或真实机器人CI。§5限两个MuJoCo host、role-projected per-step peak而非校准接触trace，不覆盖实机/人近场/全部hazards，也未实现在线shield或已验证post-training修复。hardware/precision/完整在线时延主域未披露；不采用性能数字，采集/adapter、标签/阈值审计、回放/统计和真实回归均计费。

实际Ch26开篇、安全包络、Evaluation ladder/00089与RTPC直接段、逐条STL/logits和邻Ch25/27职责已读。已有成功非安全、off-log与dynamics分责，并未承载**task-valid active set、四格联合人口、最坏深度非累计风险**三者共同绑定的测量接口。唯一owner仍`MULTIMODAL-EMBODIED-VLA`；不把泛统计转Ch66或复制安全controller。最小两段拟在Evaluation ladder H2之后、原“安全评估必须区分偏离日志与违反动力学”H3之前，保原二者和所有原论证；未SAVE。

### 00773最小逐字PRE，待首次独核

上锚：`## Evaluation ladder`；下锚为`### 安全评估必须区分“偏离日志”与“违反动力学”`及其完整首段/00089独立marker，当前实读保持。

拟新增两段：

即使能读取整条轨迹，也要先确定每个安全谓词在这个任务中是否有意义。插入酒瓶本来需要倾斜，打开抽屉本来需要移动柜体；把所有任务套同一约束，会把正确行为计成危险。应先由可用信号、任务机制和物体属性确定适用集，再保存对应阈值、坐标与时间范围；复合任务若全程排除某条规则，不能将覆盖缩小误称安全改善。[SafeVLA-Bench的受限接口](https://arxiv.org/html/2606.00773v1#S3)保留原成功判据，另记录全部轨迹中的规则满足率、成功且违例的联合比例，以及成功条件下的违例率；后两者分母不同，不能只挑成功样本或只比平均成功率。

频率还应与严重度分账：可按预先声明的严重锚，将每条适用规则的负robustness归一并截断，取一次轨迹中最坏深度，再跨轨迹统计。该分数不累计持续伤害，也不是实际风险概率；二值碰撞告警直接饱和，更不能伪装成连续物理标定。改变适用集、阈值或严重锚都可能改变排序，区间估计也须说明哪些规范量被固定。受限模拟对照支持这种诊断，而非在线shield或实机认证；记录/adapter、规则审计、回放和真实闭环回归均付费。信号缺失或规则语义不清时保Unknown、分项报告与原物理测量/独立controller，不由较低代理违例或较高任务成功批准执行安全。<!-- source-family:SF-2026-ARXIV-2606-00773 -->

本人trueH2注仅在必要/owner/PRE独核与实际SAVE后记录。00773尚未独核/评分通过/写书；其余19尚未必要，日报仍进行中，不增年度日数。

## 00435 TC-LIA：输入相关性sensor与候选答案放行分责

root，2026-10-25；R62完整题摘/准入/Jun02联合日证复用。当前[官方abs](https://arxiv.org/abs/2606.00435)为v5/Oct01，无所见撤回/勘误；只用[exact-v1](https://arxiv.org/html/2606.00435v1)。实际必要读§3–6、§7 T3/错误结构/答案质量、§9、A.2–4、B.1与K/L；未看图像素、全T1各backbone行、D全证明、所有负实验、代码或复现。不采用v5的训练免疫/10域/14模型/跨backbone新结果，医学只为通用VLM测量负载，不采用临床或AI-for-Science结论。

正式拟2+1+2=5：固定CLIP末层读出用于各层patch-question轨迹，与输入有效性/structured class分别成为release sensor，是局部表示读取替代接口；不是模型自信/“related就correct”。具体owner gap故必要域深入，非泛幻觉综述或所有附件。Source采用范围如下：

- §4用固定post-LN/projection读出各层patch，和question text cosine后取top10均值，组合late/gain/slope/finalcos及固定IAS；作者明确intermediate并非经过该投影专门训练的exactCLIPspace，局部趋势不是语义真值。§5的gain只在layer-invariant shortcut分解成立时消去共同项；不采用一般因果/所有shortcut已被去除，未重审D全证明。
- 空白/噪声pixel gate、粗domain routing、上述features、VLM structured class再由训练ensemble融合。§4 Stage4、A.2 Inference/A.4明确**VLM先产class和候选answer，再决定release/替拒答**，所以正文“before generation”不作为免VLM生成成本或未回答前就全部决定的证据；不是下游全部由独立CLIP控制。
- §3 MR分母是全部三类input人口，不是nonrelated条件FPR/正确性后验；类比例变动会改值，Related仍可答错。§6每原样本扩related/unrelated/blank三条件，A.2按域原图随机抽100再留剩余；未披露足够group-by-source图像/重复问题分组防泄漏与所有unrelated配对细节，不能从random split授无泄漏泛化。每backbone单独训练、训练split五折选classifier，不采未见backbone或跨域无校准保证。
- T3的finalcos-only MR2.1低于full2.8而accuracy90低于94.6；不能说所有指标单调更好。移VLMclass的accuracy下降最多，不将full全部归给内部轨迹。B.1 feature选择另200pair开发，和主测试身份关系未充分闭合，不授特征选择全无泄漏。K承认Related原prompt有更高answer-overlap；三condition平均BLEU/ROUGE/BERTScore含refusal参考，改善不等Related事实质量不变。L收紧MR会降低Related recall，阈值目标不是新域风险保证，校准与测试分离细节不足则不采实现保证。
- 必要域未充分披露完整GPU/precision/服务batch并发与E2E latency/SLO，Not Disclosed；本次不采用性能量化，只保测量与表示接口。额外CLIP各层读出、路由、VLM候选生成、ensemble训练/校准及拒答误拒费用均保。未核实现/复现，不因可选code未读阻塞受限命题，也不拿医学标签作安全认证。

实际读Ch23开篇、主动观察末组、任务贡献/可靠性完整机制与其完整后组；Ch22/24开篇职责已读。当前sample reliability已有policy hint非truth、共同噪声/校准费用及Ch66 risk-coverage归属，却未具体承载**同一末层readout探测跨层局部轨迹→与候选structured class融合→输出放行而非免生成**。唯一owner`MULTIMODAL-REPRESENTATION`，不复制Ch66通用confidence或临床知识。拟只在可靠性机制完整段后/训练干预router完整组前两段，不新H3，未SAVE。

### 00435最小逐字PRE，待首次独核

完整上锚：

可靠性估计器拥有的是 policy hint，不是真值概率。用 predicted variance、confidence 或 reconstruction error 调整
权重，可以避免一条受污染模态拖累全部表示；但估计器自身也会漂移，并可能在相关噪声下共同自信。它用额外
训练、校准和故障切片换取 sample-adaptive fusion。数据稳定或 calibration evidence 不足时，静态权重、late fusion
与单模态 fallback 仍更可解释。相关受限实验只证明特定情感数据、模型、硬件和随机种子下的分支可行性，不支持
把 inverse variance 外推为跨任务 truth authority；第 66 章负责验证 calibration、risk–coverage 与 abstention。

拟新增两段：

对图文问答，sensor还可以先检查“图像与问题是否相关”，而非只估计整张图像清不清楚。将冻结CLIP的同一末层读出应用到多个视觉层的patch，再比较其与问题的局部相似度，可用晚层top-K、早晚增量和变化斜率提出相关性信号。这里是共享探针，不是中间层已被训练成精确CLIP空间，也不由gain升高证明已找到因果证据。[TC-LIA的受限分支](https://arxiv.org/html/2606.00435v1#S4)将这些信号、空白检测和粗域路由与VLM自己的结构化类别交给受训融合器；完整路径先生成类别及候选答案，再决定是否发布，不能称在生成前已省去VLM调用。

相关性通过仍不认证答案正确；以全部输入为分母的误放比例也不等非相关输入条件下的错误率或事实置信度，类比例、校准人口和拒答覆盖须一起报告。有限对照中更低误放与更高分类准确并不总同时取得，平均答案相似度还混有正确拒答的收益，不能据此声称相关样本质量无损或全部收益来自内部轨迹。逐层特征、域路由、候选生成、融合训练与重新校准均付费；探针、域或误拒预算不可靠时，保留较简单的全局相似度/固定输入检查、原模型与独立答案验收，必要时拒答或补观察，不让相关性sensor取得真值权。<!-- source-family:SF-2026-ARXIV-2606-00435 -->

完整下锚为“选择干预路径的标签也可以来自有监督的输入对照”起的完整2509-15361训练router段及其独立marker；该组未拆分/移动。本人trueH2注待首次必要/owner/PRE后随实际SAVE记录，未预I/DAY。00773 R89/90已成、Report78/68/5NC有效；其余18未本轮必要，不把宽导航转逐项全文配额。
