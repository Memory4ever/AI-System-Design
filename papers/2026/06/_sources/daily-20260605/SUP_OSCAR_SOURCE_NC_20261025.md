# 04463 OSCAR：首次必要Source / actual Ch25具体NC提案

当前行政结论：R69–70已实际完整读回，首次必要/6分/actual Ch25四组具体已有覆盖通过；README已按真实处置转已有覆盖并复跑V3通过，不改Book/本人注、无PRE-POST或新I，累计仍新增15＋旧Kimi1合16。下文作者NC准备态保为历史，不第三有效原证。

仅Daily2026-06-05补Jun04；作者supp_20260605_author。R33–36完整题摘/准入/精确v1日证复用，不第三AB/date。当前采用[OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics exact-v1](https://arxiv.org/html/2606.04463v1)，不是后版Action-Conditioned标题/摘要。`SF-2026-ARXIV-2606-04463`官方HTML实际GET200/391502bytes，保存`SUP_2606.04463v1_20261025.html`，SHA256 `c189f9f161a398f9d24a7e8f4c40f09c2973401e24bd8892ca62996973eb51d0`。

实际读§3–6/Eq1/T1–4/Limitations、A.1.1数据说明/A.2–A.5、A.6关键负侧与A.10必要协议/校准。未展开全caption prompt、全部逐task/逐本体表与定性图像素、代码或复现。支持和直接反侧已足；不因已有覆盖省必要源，也不为论证无缺口而扩全附件。

## 机制与评价支持

§3从Cosmos-Predict2.5-2B rectified flow起步，首时位在每步去噪覆盖为真实首帧VAE编码；URDF/FK将joint motion传播到link origins，经相机内外参投影，按本体native树画2D线/点及gripper状态。human改用MANO拓扑/pose，统一的是渲染格式而非共同joint向量、控制语义或接触。纹理/背景由首RGB锚定，骨架仅粗运动，视频prior补细节。Skeleton方案明确沿VAP采用，不作为本篇首创加分。

骨架RGB序列与目标视频帧对齐，走同WAN2.1 VAE；各自patch embed后相加送DiT。它是给定动作轨迹的条件生成，不是模型自主预测未知动作或已实现其物理后果。相机/kinematics错配直接伤骨架–RGB对齐；Limitations只用2B/标定限制，不构成所有本体无关泛化证明。

§4从robot/human源做长度≥70frame、static-camera、非静止动作、骨架可见过滤。去重先五帧SigLIP cosine>0.95找visual候选，再64-step重采样轨迹RMS/自适应阈值核对；同背景但不同运动不自动去重。Qwen3-VL caption是派生语义，不是完整动作/物理真值。T1的180657是保留规模，不把“filtered out”文字误作删除量：robot94830/human85827合此数。A.1 InternData为synthetic，其他来源real；RH20T缺proprio/标定错的配置未纳，不称全公开视频皆可转。

A.2的200clip按caption×motion kmeans去近场景、完整horizon末端可见及各源sqrtN配额选择；不是任意自然分布/全部遮挡动作人口。必要域未披露明确held-out split/跨源训练评测去重边界，不补无泄漏证明，也不据缺说明断言已有污染。A.3单GH200、batch16、AdamW3e-5、81frame训练窗偏grasp/release、按帧数温度T3采样，15k robot-only后混human，Stage2总iteration/完整准备费未明确，不声称全预算等价或净降本。A.4 latent baseline将80×14动作flatten成global adaLN/time条件，对照并非所有latent-action接口的不可避免上限。

§5/T2平均视觉指标含PSNR/SSIM/LPIPS、tLPIPS、FVD/FID/latentL2，最多支撑重建/连贯/分布相似，不是独立action跟随或真实接触指标。七baseline的尺寸/条件/数据不同（A.5），不能把全部差唯一归skeleton。T3同robot-only/同基座比较更窄：mesh的tLPIPS .013优于skeleton .015、latentL2 .109优于.117；作者称两者统计不可区分但未给重复/CI/检验，不采用正式等效性定论。加human/robot warm-start改善有限均值，不授更多human或两阶段普适必优。

A.6 AIROA-MoMa直接反侧：OSCAR PSNR20.77/LPIPS.254/tLPIPS.035弱于Genie23.31/.195/.015，也弱于部分其他指标对照；DROID tLPIPS .020劣于Genie .005。IRASim因7DoF接口与双臂/mobile不合而在两个子表排除，不能合成每baseline覆盖完全相同的平均人口。单GH200 FPS2.214小于IRASim2.330但后者质量和接口不同；首49帧评价不等完整policy实时/生产SLO，长度/batch/concurrency/重复计时未完整披露。

## Policy评价必要反侧

§5.4/A.10取RoboArena中人工认为左相机overlay标定较好的65session×7policy=455cell。DROID平台Franka/Robotiq/ZED，MoGe-v2内参/CtRNet-X外参估计；标定筛选人口与未知机体泛化分开。给定recorded firstframe和robot action自回归生成，再judge，并没有披露policy每步重新读取generated observation输出下一动作的闭环。因此不能从“autoregressive rollout”或七policy名称改写成policy-in-world闭环测试。

GPT-5 gpt-5-2025-08-07/high读每视频32帧/512×288和task，不读用于条件生成的caption，输出binary/partial/reason。1365pairwise preferences=65×C(7,2)，不是1365独立session或额外物理试验。BT/rank的MMRV与Spearman、per-policy mean binary success的Pearson/SISR是不同量；只有7个policy聚合点，不能用455cell/1365pair当相关推断独立N。

T4 skeleton MMRV .571/Spearman .750/SISR1.73pp较好，但Pearson .852低于latent .867，故“全部相关均最强”不采用；rank相关不证episode预测正确或所有policy相对关系稳定。A.10在100个真实平衡50成功/50失败clip上与人标78/100一致、specificity .90/recall .66/r .58，仅真实clip校准，不自动校准generated视频的幻觉/可见性；100平衡人口也不提供自然部署precision/所有任务阈值保证。定性差例仍有人标/视频/机器裁决口径差；不以“保守”证明整个world model无高估。

总训练/数据筛选/标定/FK与MANO/渲染/编码/全部rollout/GPT判分与真实校准都计费。有限rank/视觉结果不授真实动力学、物理安全、unknown embodiment、独立episode校准或完全替代真机评价。未核代码/图像素或复现；不需要为上述受限命题扩所有许可证或上游算法。

## 评分、actual owner与具体已有覆盖提案

作者建议2+2+2=6，待首次非writer必要源/实际owner/NC：受限标准化筛分与robot→human训练支持、render条件对照和selected policy评价的反侧，能修正凭大数据/更细geometry/总相关选模型的判断，跨conditioning/data/evaluation接口而可复用。不借既有VAP/flow/codec原则、模型大小或headline加分；已有Books覆盖不撤候选/降分。

启动已重读AGENTS/当前合同/Prompt、ROADMAP/三Books公共上下文、来源使用/Daily/arxiv/恢复及仅2026路由。actual owner `MULTIMODAL-WORLD-MODELS` Ch25；实际完整读235–274 action-conditioned transition/schema组、485–505 pose/appearance两完整段、1500–1538 action-realization/pointmap/native-skeleton组、1646–1678校准与评价组，邻Ch24/26真实开头。对以下**受限可采用命题**提具体NC，不改书/不另拟PRE或本人注：

1. Ch25:251完整段已要求joint/URDF/camera/timing可追溯schema，明确统一的是conditioning protocol不是物理语义；1534完整native-connectivity段直接覆盖human/robot keypoints投影为同格式skeleton，标定/FK/人工keypoint与条件编码成本、未训练dataset非未见embodiment。原文渲染/拓扑格式的长期接口已具体承载，新增逐layer patch相加不改变这条责任边界。
2. 498–500已有pose视频与RGB同time/resolution、同video VAE，拆motion与appearance消费者；包括首帧appearance、估计/decoder误差、skeleton漏细节和全部codec/训练/生成费。OSCAR从给定FK条件生成而不forecast pose是该已述条件consumer的实例，不需要再重写“共享codec非相同语义”。
3. 1525–1533完整nominal command/joint encoder回放与环境response分工，明确logged future state不能泄漏为未知部署候选、pointmap较准不等接触/守恒及更清晰画面非安全。已承载本次recorded action rollout不能升级为政策闭环/部署前未知运动的限制；原显式simulator/短horizon真实反馈回退保留。
4. 1673起已具体区分状态真实性/策略实际影响/证据不足克制；WorldReasonBench完整段要求固定帧/时间密度/QA与judge、人审范围、独立留出校准及真实transition/Unknown，不让总体视频或偏好分认证物理/规划/安全。OSCAR的7-policy聚合rank、65标定选择和real-only judge校准属于这一评价合同的新受限实例，不提供新的独立验证方法或保证须另造正文；这些实例和负侧留Report/本Source。

视觉+trajectory两级dedup和static/visible筛分是有意义的具体训练构造/coverage人口，局部结果无需证明通用定理才有价值；保其实际增量、完整参数/人口与反侧于Report证据，不以NC撤候选。本次拟采用的长期判断是schema/运动与外观条件/动作实现/评价权限这四项，已由上列现文具体承载；不为增加保留数或抄数据阈值另造正文。所采新增实证未与现文冲突，因此仅提具体已有覆盖/NC，待首次独核，不预NC/I；若reader指出两级筛分或另一受限机制仍有具体长期gap，再定点处理，不把此作者提案当最终无增量判断。

## 本阶段停点

04463 exact-v1首次必要/6分/actual Ch25四项具体NC ready待首次独核；无Book正文/注/PRE/POST/I。04708 R67–68已真实行政同步整合生效，累计新增I15＋旧Kimi1＝16；04315 NC等有效层不第三。其余五04306/04104/04896/04364/04485和有限相关官方标题stop/最终DAY仍ordinary，不扩73/706配额。本单篇ready交root即结束准备阶段释放槽，不等其他Methods，不表示暂停或完成本日。无共享Books新正文/他注、State/index/他日/stage/commit/push。
