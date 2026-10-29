# Oct24 World/Action：必要Source交接

执行者oct24_org，仅本文件；root唯一Books/Report/State writer，oct24_reader独立复核。本组唯一ownership：30814/30320/30735/31423/31613/30197/30319。同日AGENTS重读，合同未变化复用；先读本日ARXIV完整题摘/公开日身份，再复用REVIEW R3准入；30197/30319由reader另行准入通过后才开正文。日期沿本日官方Oct23 new事件，不把HTML顶部Oct21/22提交日改称公开日。均精确v1 HTML，本次未见撤回提示；未运行代码/实验，以下Source-ready不等独核、Books或DAY通过。

## 30814 DRILL — Source-ready

[精确v1](https://arxiv.org/html/2610.30814v1)。`2+2+2=6`，标准审阅并加深§4反证。Owner提案 `MULTIMODAL-WORLD-MODELS`。

采用命题：next-frame MSE与imagined policy更新用途不等；外层优化目标须是内层GRPO更新后在目标环境取得的return，不由world model自己评价自己。§3 Eq3–7：VWI以visitation×signed advantage×confidence重权像素误差，stop/clipped权只给局部更新方向；IMG经混合导数/HVP反传内更新，K=2、每外步30 simulator rollouts。

§4.1 Eq8必须保留score-compatibility、局部stationary visitation、Gaussian head及trajectory/demo-anchor residual小的条件；VWI非IMG精确等式。§4.2只是fixed-policy outer subproblem收敛，不是联合过程全局保证。§5五仿真器、pi0-3B/部分OpenVLA7B，主五seed/消融三seed，mean±std与Welch/CI；Sim-PPO匹配模拟器交互，WMPO额外compute控制。§5.4短horizon两者可相当，IMG约1.4倍外步成本与额外交互，horizon H=200的噪声使收益回落。§6明确无真机；17k H20-hours不是端到端部署效能。精度/并发/SLO未披露，不引用吞吐保证。建议root对照Ch25 policy-useful rollout目标；若已有pixel fidelity≠decision utility完整论证可NC，不为论文名建段。

## 30320 FRED — Source-ready

[精确v1](https://arxiv.org/html/2610.30320v1)。`2+1+2=5`，标准审阅；Owner提案 `MULTIMODAL-EMBODIED-VLA`。

§3 Eq1–4可采用：action decoder实际消费noise单步产生的未来latent，故对该latent用EMA teacher从有噪真实未来帧提取的目标作patch KL；历史帧给motion条件。视频backbone不收action loss梯度；不是“单步完整视频生成”或已经做显式跨embodiment对应。§4.1 Wan5B/14B＋独立16/24层DiT，teacher noise0.25；§4.4同RoboCasa移除SD/history由68.8降65.1/64.8，均移除61.4；对齐目标与历史有互补局部证据。

评价含DROID→新环境和OpenArm人视频混训；长任务为partial progress，不把81.7全叫成功率。OpenArm七任务每任务12试验，人视频1187条；没有人视频时transfer成功接近0；Table2的50%为有限task transfer，不证明通用模仿。附F：语言grounding依赖原视频backbone，跨embodiment对齐隐式且成功有限。反复视频denoise减少不等action ODE只一步。采用该目标分离机制即可，不摘跨架构榜单普遍领先；完整算力/精度/端到端SLO未披露。root实际对照Ch26视频先验→动作接口，已有覆盖可NC。

## 30735 One Step Enough — Source-ready

[精确v1](https://arxiv.org/html/2610.30735v1)。`2+1+2=5`；设计反证的§3–5及训练成熟度域加深。Owner提案 `MULTIMODAL-EMBODIED-VLA`。

采用命题：大且充分训练的flow VLA不应默认必须多步Euler/另蒸馏；先固定checkpoint做一步/原步数配对验证。§3相同种子/初始化，真机盲A/B并固定噪声；六VLA450M–4.7B＋211M DiT；LIBERO、LIBERO+、CALVIN、RoboTwin及四Franka任务。TOST等价界3pp、CALVIN0.15，90%CI，不将不显著当等价。§4 36仿真cells中23等价、4多步优、2单步优、7不确定；训练/规模与预训练混杂通过部分ablation收窄，FLOWER早停checkpoint有差、末checkpoint差缩，不能仅以参数规模定律解释。

反侧§4.4/5：单步轨迹多样性降低；真机个别task可差13pp，任务聚合非严格iid；released checkpoint缺格，无VLA-scale RL验证。单步Euler只在straight flow严格精确，本研究不是证明所有flow直线。Table1 latency单A100、原4–10步对一步，1.6–4.8倍是模型动作生成，不等闭环控制频率/全系统。精度/batch/concurrency/SLO未完整披露，不外推图片diffusion。root对照Ch26已有限步采样与控制周期论证，可作限定反证或NC。

## 31423 FocusVLA — Source-ready

[精确v1](https://arxiv.org/html/2610.31423v1)。`2+1+2=5`，标准审阅；Owner提案 `MULTIMODAL-EMBODIED-VLA`。

§3采用：多视角输入≠按任务阶段实际利用互补视角；intent bridge由当前多模态/state和短动作历史预测未来chunk各步local-interaction概率，以固定有界映射混合global/local action-side context；另有chunk intent token。训练标签从夹爪/速度/轨迹弱监督产生，非真语义阶段，推理不读取真实未来动作。注意力比例不是因果证据；§3.1单StackBlocks/20rollouts view masking只是诊断补充。

§4.5九task×两训练seed×100 trials、20K steps匹配数据/算力对照；same-architecture E2E action-loss-only 55.7对Full73.7，以及Static67.5/OnlyRouting63.3，支持额外intent监督/样本步级路由/intent token的局部贡献，不仅增加网络容量。§4.1 RoboTwin50task×100trials，真机Piper＋两D435i、六task×30trials；main同demonstration/steps/testseeds，无通用camera/embodiment验证。§6对此明确future work。精度/并发/统一SLO/路由端到端开销Not Disclosed，不把轻量标签升级为已测低延迟。root实际对照Ch26观测分配阶段条件；不转成一般attention算法owner。

## 31613 Progress Probes — Source-ready（性能聚合不采用）

[精确v1](https://arxiv.org/html/2610.31613v1)。`2+1+2=5`，标准审阅；Owner提案 `MULTIMODAL-EMBODIED-VLA`。

§V Eq2–4采用：成功demo按1−t/T标签训练activation线性readout，将预测“剩余progress”减去1−t/平均成功长度；落后超过阈值报警，快速执行不罚。probe不要求failure训练数据≠不用成功数据/校准。§VI VLABench pi0.5，300成功轨迹80/20训练验证/校准，600评估轨迹成功失败各半；§VII Franka3/DROID、360训练及120评估轨迹六task，unseen为20种3/3划分。

必要反侧：§VI TableIII在5%FPR下episode末TPR0.64、平均首次检出0.60episode，不能只报AUROC冒充及时阻止。§VII Coffee Bean小范围随机泄漏时probe失效，内部policy activation可对视觉微小物理故障不敏感；§VIII仅pi0.5/VLM层，非所有action experts/架构可迁移。表IV显示逐task值与某些Average列无法直接算术复现（如SAFE-MLP），且正文绝对“all baselines”不由每task结果支持；因此本次不采用硬件聚合数值/普遍胜出、也不据此否认机制。只用训练/评分构造及该具名失效边界。latency测A6000，但缺完整batch/precision/SLO，不摘倍数；监控不是恢复控制或安全证明。root可把demo-only内部progress作为Ch26 monitor的可选信号，已有“不独立、需校准、不能保安全”完整论点可NC。

## 30197 Alpha — Source-ready

[精确v1](https://arxiv.org/html/2610.30197v1)。`2+1+2=5`，标准审阅并加深设计归因反证；Owner提案 `MULTIMODAL-EMBODIED-VLA`。

可采用§III/IV/VI：同physical seeds/geometry/fault配对oracle与LLM能把end-to-end失败定位到不同接口。特别F4是人为删JSON键/截断，LLM走Pydantic fail-stop空plan，而oracle直接domain object绕过此故障。因此64%对44%的全差异不证明认知推理差；排F4后60pair两者33/60相同，只证该cohort无discordant pair，不证明LLM没有任何intrinsic reasoning deficit。安全fail-stop可降低completion而改善无畸形动作约束。

§V单PyBullet pick/place、75pair、master42，各强度n5，单Llama3/Ollama greedy；§IX明确wideCI、sensor history≤0.5s、F4不测语义认知、无真机/跨模型。§VI F3的continuous placement/safety事件仍可不同，不把binary matched提升系统行为完全一致。169pilot不是150主实验，99外部API abort也非LLM推理失败。硬件/精度/并发/SLO缺，walltime差异不作公平性能结论。root若Ch26已有失败分层与动作schema边界，可具体NC而不新增故障清单。

## 30319 TerraTransfer++ — Source-ready

[精确v1](https://arxiv.org/html/2610.30319v1)。`2+1+2=5`，标准审阅；Owner提案 `MULTIMODAL-EMBODIED-VLA`。

采用§2：vector-state selfplay PPO teacher→rollout实际未来训练flow trajectory teacher→冻结teacher head/ego encoder，DINOv3视觉backbone只训adapter，以action distribution KL＋teacher主子空间batch关系loss（planner另trajectory目标）对齐。两个loss互补：KL不能唯一确定latent，关系角度对旋转/平移不敏感不能保证head action。§3.5匹配1.83M nuPlan paired frames/compute，无HUGSim adaptation，both0.574对action-only0.434/struct-only0.373，是必要局部证据。

边界：demonstration-free仅不用expert行为轨迹作target；仍依赖HD map、image/state paired感知标签、logged endpoint作goal。headline有evaluation scenes自身渲染300K frames（覆盖10%route）domain adaptation，不把它宣传纯零样本迁移；teacher privileged不是同camera对照。HUGSim native stand-in decel计划与其他方法真实plan协议不同，NAVSIM pseudo closed-loop不是真闭环/真车；Extreme tier有反向收益与保守让行失败。故不采用全榜领先/道路安全结论。训练一次alignment 8A100×10h不含完整selfplay/teacher成本，precision/端到端SLO未披露。机制作为privileged simulator监督与视觉行动接口的替代，而非自然而然消灭数据依赖；root据Ch26实际覆盖选NC/最小差额。

## 本组停止边界

七项均必要核心/评价/反侧已读足上述采用命题；未遍全附件、不复现、不第三读机构两篇。不写Book/Report/State/REVIEW。等待独立reader核必要域和root具体owner差额，不自签Books/DAY。

## 实际owner比较（只读Books，不写）

Books方法/指南、PROJECT_CONTEXT已完整读；Ch24生成表示/采样接口与Ch27数据provenance交接已读相关开篇，Ch25/26按目标机制与完整直接邻接定点读取，不把巨大Review notes当正文。以下只提逐篇处置，root/reader仍实际核。

### NC-30320：具体已有覆盖提案

Ch26 `World-action model` 当前正文：第一段“显式rollout保留可观察的中间未来…”已明确训练期真实future/frozen dynamics teacher塑latent、部署一次prefill而不materialize video；其后DIAL完整段（现约656）明确native真实future target、暖启与自产future/action consumer支持分验；再后2603.16195完整段（约662）明确首步内部feature→teacher future representation→action expert，动作头仍可多步、teacher偏差/全部训练费及退路。故FRED本次稳定采用命题“监督action实际消费的单步未来latent，而非把一张更好视频当动作充分证书”已被这些实际段承载。EMA/patch KL和历史帧是本次局部训练配方，与已有两类target/gradient分责共存，保留在Report证据即可；不宣称书里已有FRED精确实现，不增正文或note。

### NC-31423：具体已有覆盖提案

Ch26 `Perception 可以分流，协同 Action 仍需显式耦合` 中MoPA两完整段已把执行消费者的观测需求分流与action耦合分责；紧邻2602.23024完整段从“分路感知/动作之外，还可以按阶段改变读取尺度…”开始，已有历史action增量＋当前global feature产生动态perception权重、同fixed尺度消融、错路屏蔽/额外loss成本与controller退路。FocusVLA新增future-intent弱标签/step-routing仅作为同一阶段感知选择分支的局部验证，不足迫使再加一套同构论证。NC只覆盖该稳定采用命题，不声称现有段已经实现其global/local固定有界映射或future标签。原文收益及same-architecture消融仍在本次Report证据保留。

### NC-30197：具体已有覆盖提案

Ch26 `Coordinate-frame mismatch`明文要求schema/version执行前校验；`Error amplification across modules`明文逐边界evidence；`Evaluation ladder`内“失败时是否询问人…”完整两段要求按failure family、固定注入原因、分离sensor可诊断性与model利用/repair，离线oracle不能授安全执行；同节“Native goal首次为真…”两段已有停止方式、真实后效、同分母和一条失效链不重复计数。Alpha所需“失败分层，schema拒绝造成不行动不等认知失败/物理安全”已有明确承载。其F4 oracle绕JSON的强不对称仅使该有限比较不能辨识认知差，不改变这些设计选择；保Report反侧而NC，不采作者zero intrinsic deficit，也不造一段planner新机制。


## 四项窄PRE（仅提案，未写Book）

每项插入原直接上下锚之间，仅新增给定一段及独立source marker，不改锚内既有内容。锚随并发可能漂移，root保存前应按完整文字重定位；reader须先核Source/owner/原段，而非只看本说明。

### PRE-30814：Ch25 小差额提案

已有optimism回写dynamics段只调高imagined回报的transition权重，update/hold段只验收候选；尚未承载“对内层policy更新后的外部return反传world-model”的目标区别。唯一owner仍Ch25，不把GRPO数学搬来。

完整上锚：

```markdown
因此 optimism 强度、entropy 与 replay 拟合需要共同验收：过强偏置可崩坏，受测任务也有反退，额外反向与训练时间不能省略。tabular 渐近结论依赖逐渐减小但累积增长的权重条件，不能移植为常数权重神经 POMDP 的最优策略或 regret 保证；较高 imagined reward 更不能替代真实 outcome。拟合漂移、质量或预算退步时，保留无该偏置的 dynamics、短 rollout、真实反馈刷新与保守 objective；这与分歧 sensor 是不同权责。<!-- source-family:SF-2026-ARXIV-2602-10044 -->
```

拟新增逐字段：

```markdown
若世界模型将被用于训练策略，还可以把“学到怎样的策略”直接放进它的目标：先在当前模型中做一次策略更新，再用目标环境的结果评价更新后的策略，并把这份外层信号回传模型；这不同于仅让模型偏向高回报的想象。[DRILL的受限对照](https://arxiv.org/html/2610.30814v1#S3)在仿真中支持这种用途对齐，像素误差更低却未必产生更有用的更新。低成本访问/带符号优势加权只是score兼容、短程与示教锚残差较小时的局部surrogate，不等完整meta-gradient；后者增加模拟器交互、截断反传与内存，短horizon未必值得，长rollout仍可因噪声退步。没有真机证据或可靠外层反馈时，保留预测拟合、较短想象与独立update/hold审计，不用模型自评或条件收敛结果批准联合训练与物理执行。<!-- source-family:SF-2026-ARXIV-2610-30814 -->
```

完整下锚：

```markdown
ensemble的一步分歧下降，并不保证想象rollout更可靠。不同模型可能共同落入latent attractor，使同动作、同horizon下预测更加相似，同时真实outcome误差或奖励乐观偏差继续增长；因此uncertainty sensor要按rollout horizon对真实结果校准，不能把低分歧直接当低错误或长期计划的放行信号。
```

### PRE-30735：Ch26 小反证差额提案

已有低步数分支多要求新初始化/teacher/corrector/probe；缺对既有充分训练checkpoint不重训直接一步的配对反证。放Latency开头，先做低成本反证测试再改架构，后接MambaAct减少每步重复成本，不混一步meta-action。

完整上锚：

```markdown
## Latency 与 control frequency
```

拟新增逐字段：

```markdown
压缩动作专家之前，还应先检验已有checkpoint是否真的需要全部积分步。固定policy、观测初态与噪声，配对比较一次Euler和原步数，再用预先声明的质量等价界而非“不显著”判断是否可省。[六种flow VLA的受限研究](https://arxiv.org/html/2610.30735v1#S3)发现充分训练与较强预训表征下常有这种零重训分支，但部分小模型、长任务和早停checkpoint仍有差异；真机样本不足以确认同样等价，单步还可能减少有效动作模式。少一次action-head求值不等整机频率同比提升，配对回归、感知与控制都计费；任务质量、行为多样性或完整deadline不合时，保留原多步、较短执行段与独立controller，不把局部一步成功外推为所有flow、RL更新或安全保证。<!-- source-family:SF-2026-ARXIV-2610-30735 -->
```

完整下锚：

```markdown
动作求解的重复成本应与一次感知成本分开：在同一policy query内，先将视觉/语言prefix压成带全局摘要的条件vector，预计算各block的FiLM scale/shift/gate，多个denoise步骤只重算noisy action、flow time和小型sequence mixer。它用条件瓶颈与重新训练换取少做重复cross-attention，不保证空间细节无损，也不意味着recurrent state跨真实观测自动记忆。[MambaAct的受限替换](https://arxiv.org/html/2610.22951v1)保持十步求解，将311.5M action expert压到29.7M；同checkpoint预算下三seed LIBERO均值改善，但prefix从40.76升46.61ms，不能说所有阶段都快。<!-- source-family:SF-2026-ARXIV-2610-22951 -->
```

### PRE-31613：Ch26 sensor替代小差额提案

已有生成几何alarm与内部信息sensor，但未承载成功demo时间归一化线性progress、与nominal均值时长差作为alarm；仅新增这一传感替代，不改现有alarm/commit分权。

完整上锚：

```markdown
Flow trajectory 偏离理想 affine sink 时，现有 denoising evaluations 的 acceleration 可作为无需额外采样的 prefix sensor，并经成功轨迹校准后驱动 CUSUM alarm。它只感知生成路径几何，不感知任务成功语义；不同 solver、步数、embodiment、geometry-normal failure、分布漂移和错误 FPR calibration 都可能让它失效。monitor 只拥有告警，外部 safety controller 才拥有 actuator commit；验收必须保存 false positive、miss 与 detection delay，超界时减速、重规划或交还人工。该分支是 heuristic sensor，不得包装成 certified confidence。

<!-- semantic-body-binding:SF-2026-ARXIV-2607-27933 -->
```

拟新增逐字段：

```markdown
监控信号也可以来自策略已经计算的内部状态，而不另运行视觉语言评判器：用成功示范的归一化剩余时间训练线性progress读出，再与平均成功时长对应的名义进度比较，落后超过校准阈值才告警。[Progress Probes的有限对照](https://arxiv.org/html/2610.31613v1#S5)只在受测π0.5中验证这条低增量计算分支，不要求failure训练样本，却仍需要成功示范、activation读取与独立阈值校准。时间落后可能是正常绕行，细小随机洒漏也可能不改变policy表征；高AUROC不等及时止损，误报、漏报和检出延迟仍需并列。分布、节奏或policy版本改变后应重验，支持不足时保留外部视觉/接触监控和controller veto，不让同源线性读出替代独立安全证据。<!-- source-family:SF-2026-ARXIV-2610-31613 -->
```

完整下锚：

```markdown
### 从 Unsafe Trajectory 到可训练分支，必须保留同一状态锚点
```

### PRE-30319：Ch26训练监督替代小差额提案

已有多来源/teacher关系对齐，但未承载selfplay行为head冻结后以action分布＋低秩scene关系联合对齐视觉、同时保留监督来源非零数据的链。放数据分层主张后而非3Dteacher里面，不把通用KL/SVD重复推导。

完整上锚：

```markdown
后一步没有否定前一步。越远离真实 embodiment，数据越容易扩展，action semantics 越弱；越接近真实 robot，成本越高，物理证据越强。
```

拟新增逐字段：

```markdown
模拟器还可以先供应行为，再由成对图像与场景状态供应视觉接口，而不要求人类动作成为模仿目标：先用向量状态自博弈训练teacher，固定其决策head，让视觉adapter同时匹配动作分布与teacher主子空间中的场景关系；前者约束行为，后者补足同动作logits未决定的表示几何。[TerraTransfer++的受限消融](https://arxiv.org/html/2610.30319v1#S3.SS5)支持两信号的互补，不证明逐坐标一致或通用最优蒸馏。无expert行为目标不等无数据，仍需地图、paired感知标签与目标条件；teacher可见而相机被遮挡的信息也无法由对齐恢复。自博弈、teacher、视觉训练与域适配都付费，评价场景适配、pseudo闭环和特殊scorer须另列；观察不对称、稀有天气或真实闭环支持不足时，保留目标域示教、显式状态估计和独立controller，不由模拟分数批准道路安全。<!-- source-family:SF-2026-ARXIV-2610-30319 -->
```

完整下锚：

```markdown
derived label 必须保存 provenance。VLM 自动生成的 state-transition description 是推断，不是传感器事实；固定 clip boundary 可能切断任务；跨 embodiment action mask 可能掩盖坐标和关节差异。
```

