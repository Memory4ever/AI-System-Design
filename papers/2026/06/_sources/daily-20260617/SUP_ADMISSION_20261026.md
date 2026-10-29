# 2026-06-17 首批准入校准

只补 Jun16 BJT；旧51候选定点去重，本批均不在旧表。`SUP_RAW_ABS_<ID>v1_20261026.raw` 是当前精确v1官方页原件。已完整读题摘及页内版本/撤回说明；下列P原页无withdraw/delete纠错标记。DataCite导航摘要可能是later版本，不替代v1：KVEraser v1是24%延迟增幅、3–4×，非当前摘要29.6%、2.9–10.7×。

| 判定 | 精确原件 | 原约束 → 原文实际增量 → 需重考的选择 |
| --- | --- | --- |
| P | [2606.17034v1 KVEraser](SUP_RAW_ABS_2606.17034v1_20261026.raw) | 删除已prefill跨度会影响全suffix、精确删除需重算 → 学习替换该跨度KV的steering states并复用其余cache，两阶段训练与近似误差需查 → 重新比较局部编辑与完整重算的质量/延迟边界，不声称真正信息删除；拟2+2+2=6标准。 |
| P | [2606.16253v1 SPARC](SUP_RAW_ABS_2606.16253v1_20261026.raw) | 感知codec保视觉保真不保证VLA控制 → task-relevant temporal latent mask分配跨视角/区域bitrate，tilted rate loss避免稀有关键视觉被entropy代价抑制 → 控制质量约束下的观测压缩须与generic fidelity codec区分；拟2+2+2=6标准。 |
| P | [2606.16497v1 daVinci-kernel](SUP_RAW_ABS_2606.16497v1_20261026.raw) | 将成功生成轨迹摘要直接加skill会把不可复现优化继续传播 → 三角色共享backbone共训且候选skill经execution验证可复现speedup才准入 → 需核清skill收益的验证与joint RL的归因/训练预算，非因三agent组合本身准入；拟2+2+2=6标准。 |
| N | [2606.16248v1 Cosmology inference](SUP_RAW_ABS_2606.16248v1_20261026.raw) | 在共同宇宙学数据/先验比较MCMC、GP与SBI，改善领域参数估计与模拟成本；属于暂缓的AI for Science，不用“inference pipeline”类比强拉Serving。日期不另核。 |
| N | [2606.16607v1 CSI compression](SUP_RAW_ABS_2606.16607v1_20261026.raw) | k-memory Markov VAE压缩无线信道反馈并提高CSI重构；原文未建立对foundation-model表示、训练或通信执行的贡献，不以compression/memory命名准入。日期不另核。 |
| N | [2606.15622v1 Fokker–Planck surrogate](SUP_RAW_ABS_2606.15622v1_20261026.raw) | GPU-native neural closure减少气流模拟CPU/GPU传输，主要证据为稀薄流守恒/熵保真及领域加速；属于暂缓AI for Science，不以GPU benchmark绕回主线。日期不另核。 |

P日期：原v1提交依次`2026-06-15T17:53:09Z`、`2026-06-15T05:55:58Z`、`2026-06-15T09:58:21Z`，均在EDT Mon14:00 cutoff前，最早公告界为`2026-06-16T00:00:00Z`。同精确DOI原DataCite `arxiv.content/findable` 的registered分别`2026-06-16T03:58:14Z`、`2026-06-16T03:41:25Z`、`2026-06-16T03:46:37Z`，整个联合区间Jun16 BJT，非把registered或submitted单独当公开日。对应原响应见`SUP_RAW_DATACITE_SYSTEM_20261026.raw`、`SUP_RAW_DATACITE_MULTI_20261026.raw`；首公开仅作有限arxiv公告归属，无具体更早全文线索，不证明全球首公开。

root首批实读校准：3P贡献边界、3N理由成立；定点跨日精确v1去重发现17034/16497均已在06-16正式候选与§4有同有限命题有效审阅，因此两项复用、不重分、不计新增、不搬原日期，也不展开Methods。上表3P评分只是初提，17034原8、16497原6不变。真正新P为16253。后续拟新P均对2026既有README正式候选行做精确ID去重，只取身份，不读别日候选池。

当前16253必要证据普通待办；未宣称Books判断或全日分母冻结。其余导航/明确范围外初筛并行继续。

## 第二小层：窄主题题摘，非568导航分母

初检四主题跨源568唯一身份，仅用于相关标题导航；76个命中旧正式候选表身份，精确事件有效性按需要定点复用，不搬其原日期。以下读完原响应完整题摘作贡献判断，P尚需精确v1/current确认及日期，不先计已定当窗候选；本层未读Methods与Books不标完成。

| 身份 | 初判与具体决定点 |
| --- | --- |
| 2606.14782 BACON | P：observation-window聚合会稀释稀有证据，末query信号需intra-layer coherence/inter-layer persistence抑噪；改变多模态cache重要性估计，拟2+2+2=6；v1早提交导致联合跨日，日期层待恢复。 |
| 2606.16694 Depth/ICL | P：Gaussian latent prior下单层最优、non-Gaussian tree-like prior下深度/FFN有adaptive inference优势；理论和key patch提供深度适用条件，非仅更深更准；拟2+1+3=6。 |
| 2606.16534 Julia/HPC | P：小输入可运行不保证规模化，任务依赖/粒度/scheduling导致deadlock/OOM/oversubscription负结果；拟2+1+2=5，已读官方v1完整AB，需必要域区分三问题/模型与并行基线。 |
| 2606.17005 Bayesian archives | P：终态leaderboard对到达frontier时间非识别，selection-aware模型在synthetic recovery/calibration失败，限制从公开选择性历史推出frontier规律；拟2+1+2=5。 |
| 2606.16359 FEnc2 | N：原文实际贡献为CKKS卷积网络fragment packing/feature-channel reduction后的ciphertext密度，实验LeNet/MobileNet；未建立大模型attention/训练/推理执行关系，不以通用“private inference”替代范围。 |
| 2606.16332 SMEPilot | P：CPU/SME争带宽且phase/arithmetic/layout不同，operator-shape选择CPU/SME/cooperative并复用packed布局；拟2+2+2=6。 |
| 2606.16131 ShiftSum | P：VAR coarse-scale attention-value误差与calibration codebook频率不匹配分开处理，用对称value shift合并及resampling；拟2+1+2=5。 |
| 2606.15327 SemDLM+ | P：semantic corruption在posterior难度/repair间折中却困在semantic basin，加入global transition及frequency penalty；拟2+1+2=5。 |
| 2606.15210 QLMIO | 决定点后拟N，待root校准：完整v1题摘后仅补III/IV-A/B，实际是冻结DistilBERT/ViT+model/device embedding，经MLP分类/回归预测success/latency，再把这些值与queue-average拼给D3QN做整请求选server；MIOBench逐题/设备配对trace供sim查表。尚未提出不同于既有预测器+DRL组合的可复用新机制/有效性条件或受控反证；58.14%与换MLLM/cloud-edge场景本身不准入，不因模块名或两目标建立候选。不是因缺实验/optionalcode排除，不为此另追日期或读全文。原工具片段`SUP_RAW_QLMIO_DECISIVE_WEB...raw`/官方v1 IV可核。 |
| 2606.15165 VLALeaks | P：特定VLA attention discrepancy可作为成员特征，可能修正只查语言输出privacy的部署判断；拟2+1+2=5，必须核精确v1威胁模型/攻击比较与false positive，非“首次”标签本身准入。 |
| 2606.15188 VeriLatent | P：不用decode噪声图后验，而在early latent activation map查编辑区域并按难度预算，改变decode-verify成本与验收时点；拟2+1+2=5。 |
| 2606.14981 ViTaL | P：visual长horizon mode selection与tactile短horizon diffusion edit分责、latent future outcome评分，区别naive modality fusion；拟2+2+2=6。 |
| 2606.16193 SAE++ | P：二级SAE训练在一级decoder方向而非稀疏activation，避免简单stack瓶颈并允许concept-group干预；拟2+1+2=5。 |
| 2606.16610 DFM bounds | P：有限矩/score integrability的KL维度界与额外一阶score/weak-log-concavity下W2条件，改变采样误差假设；拟2+1+2=5。 |
| 2606.15835 decentralized DFM | P：多local velocity及stochastic switching不属标准global分析，ODE离散W2 O(N^-1/2+epsilon)条件需核；拟2+1+2=5。 |

本层另已读15685/15550/14777/16494/14883/14747/15615/16586完整题摘，具体准入决定点整理中；它们不是已终态或已完成审阅。

本批后续root§5：13潜P完整AB、FEnc2 N、QLMIO决定点/日期与current短提示已实际独核；12合法联合Jun16，14782保持未定日/不正式评分。16694改用v1HTML原标题`Adaptive inference and function vectors in deep transformers`；已通过必要/PRE及actualPOST I2。16534必要与actualowner首读交root，作者不重复Methods。

旧链定点纠正（2026-10-26）：root与Jun16唯一reader核canonical retained整行，16332/17005及后续16494此前被泛N误删，均恢复旧Jun16原日期字段/原3+3+3=9；本层初拟分只留误判历史，不生效、不搬日期或重复计新候选。16332新正文已root§10实际POST，17005真实新段/本人注归属已SAVE待POST，16494原9必要/实际owner仍由本日作者准备、root独核后供旧owner复用。其余本批及SPARC12个身份无旧retained，不扩大旧池。

## 第三小层：8份exact-v1与有限决定点

完整v1题摘原件均`SUP_RAW_ABS_2606.<ID>v1_20261026.raw.b64`，当前官方页`...<ID>_current...b64`已实际看短说明/版本身份，无撤回/纠错具名提示；v2、页数与camera-ready本身不触发全版本比对，后续采用限定v1。正式2026候选行精确检索无新同项；16494另发现旧trace并已按上段恢复，14783旧Jun16正式6分NC命中仅去重。`SUP_SOURCE_DATE_BATCH2_20261026.raw`保存原字段定位与复算：15685/15550/16494/14883/15615/16586的整个合法界为Jun16 00Z至各03Z，均Jun16 BJT；14777为Jun11–16、14747为Jun08–16，不能切取目标日。16494保旧归属不按复算迁日。

| 身份 | 贡献判断与拟最低投入 |
| --- | --- |
| 2606.15685 SCE | P：closed-loop feature drift可连续放大旧行为偏差 → 从示教ground reusable skill并分开执行expert与skill间transition expert → 需区分保技能与保转接能否独立减少遗忘，非只换continual任务指标。拟2+2+2=6；准入只读完整v1题摘，必要尚未开始。 |
| 2606.15550 Roken | P（窄决定点已核）：逐机器人计划后修复不直接学joint可行轨迹 → 以robot-token/action-chunk并行表示可变团队，trajectory mask允许固定部分机器人条件；§4.1指出goalshortcut绕过map，训练专有local-occupancy/long-waypoint heads纠偏，推理移除heads → 改变联合动作表示与条件消费，不能仅用‘DiT+机器人’准入。拟2+2+2=6；HTML urllib一次404但web官方HTML可读，不列外部H；原生正文§4.1–4.2具名决定点已读，未审全部实验。 |
| 2606.14777 JoyAI-VL-Interaction | 潜P：每秒内部选择silence/respond/delegate，而非外部固定轮询强制作答；可改变流式观测与发声/后端委派控制。日期界跨Jun11–16，暂不正式评分或候选，待有限官方release/作者项目日期恢复；不因8B或完整demo入选。 |
| 2606.16494 Lost at the End | 旧retained精确恢复，不新计：仅gold passage slot可变的reader反证、text-only/control与retrieval修复失效需按v1/原9必要核；当前新增3B–32B扩展不混作v1。 |
| 2606.14883 Continual cross-modal theory | P（决定点已核）：非‘理论视角’标签；§4 Def4.1/4.2将跨环境image/text贡献定义为cosine，Theorem4.6在Ass4.3比例桥接下连到lossdrift，4.13/.15又用curvature/compactness给forgetting条件界，可能改变何种相似度可解释迁移的判断。拟2+1+2=5；当前只是待核命题，不因一般theory主题N。原HTML已读相关定义/假设/主式决定点，CFB与各推导是否成立留必要证据，不提前背书。 |
| 2606.14747 MMLongEmbed | 潜P（决定点已核）：不是仅新增4任务；§3.1按统一token口径独立length pool并固定candidate/query密度，§3.2相似needle/hard distractor使表面匹配失效，长度/位置/跨模态冗余为受控轴 → 可能修正‘更长窗口/更高维embedding就检索更强’评价。日期界跨Jun08–16，不正式评分/候选；必要范围不先展开，待有限日证恢复。 |
| 2606.15615 MoECa | P：whole-token reuse把同一token不同expertbranch的跨步变化压成一个资格 → branch-level cache+expert-aware control，并同步MoE/attention更新 → 重新定义DiT-MoE feature复用粒度/一致性资格。拟2+2+2=6；v1仅2.83x而currentAB2.93x不混用，倍率本身不准入/不证明重要修订。必要尚未开始。 |
| 2606.16586 LOCUS | P：有高分辨率仍未可靠消费局部证据 → 训练时给crop、以recover其full-image support的IoU代理奖励，推理仍原image/question接口 → 区分额外推理搜索与internalized evidence-selection训练，非单纯定位任务换名。拟2+1+2=5；局部IoU不先授完整reasoning提升，必要尚未开始。 |

本小层拟P及两dategap交root原件校准；日期未定项不靠submitted/registered单独归日。来源和其余已校准筛选不停。

## 官方源具名贡献层

官方原件当前可读，未见撤回/纠错短提示；只采用实际披露的有限机制，不因机构或Suite名称入选。

- **P OpenAI Deployment Simulation**：挑难题stress评估不能直接估自然发生率 → 用旧部署prefix替换单次assistant回复，候选模型重采样，部署后同协议回验，并用可读历史repo/tool-pair库+只读connector模拟tool而非真正改live系统 → 需分开检验resampling fidelity与prefix distribution shift，不能将逼真的rollout当真实effect或tail-risk覆盖。拟2+2+2=6；官方RSSJun16 00Z与BlogJun16日期一致。链接现2607.07184是later论文，只按Jun16官方Blog事件，不搬论文；全2026正式候选URL/标题/精确paperID定点无同项命中。原件`SUP_RAW_OPENAI_SIM_WEB...raw`，正文核心和limitations已读，必要/owner待整理。
- **P Qwen-RobotNav**：统一navigation若固定历史策略会让longhistory/recency任务互相牵制 → 四轴visual-token budget/temporal decay/camera weights/sample mode训练时逐样本randomize，推理调用显式传taskmode+观测配置，同weights可换配置 → 重新界定policy条件接口而非部署时任意调budget无训练支持。拟2+2+2=6；只取有限参数化机制，不采“any setting”无界保证。`SUP_RAW_QWEN_THREE...raw.b64`原API目标article含完整HTML；APIdate、article:published_time与ld+json datePublished均Jun16 08:00+08，原HTML正文也June16；当前SSR索引June15不代offset日期，不泛化整个源受阻。正式表精确blogpath/题名无命中，必要PDF可按具体缺层读取，不默认全附件。
- **P Qwen-RobotManip**：不同embodiment状态/动作scale与视觉相似性不齐会让扩数据互相冲突 → 80维带有效slot mask的state-action表示、camera-frame EEF delta及读执行history作implicit embodiment signature，联同human-to-robot合成/curation支持跨源训练 → 应分别验表示统一、坐标对齐与history适配的成立条件，不用38Kh数字替代贡献。拟2+2+2=6。原API/HTMLmeta一致Jun16 08:00+08，blogpath/题名精确正式表无命中；必要与actor/数据权限对照待整理。
- **N Qwen-Robot Suite作为第四家族**：完整core是上述Nav/Manip及已有2606.17030v1 RobotWorld的组合发布/相同原证入口；未披露独立的新执行/评价机制，不能仅因统一语言接口与三个模型互配再收一次。Suite Jun16 10:00+08仅留source关系；RobotWorld旧同精确v1按Jun16正式记录复用，不重评分/搬日。

OpenAI/Nav/Manip均尚待root本具名准入/日期独核，不计必要完成或正式Books处置。没有以SSR零行/urllib403宣布必要正文受阻，原件已合法恢复。

## 第四小层：最后已读20份，停止扩导航

本层是停止指令前已读的具名题摘，不把568身份变逐项队列，不再由邻近标题继续扩池。完整exact-v1/current原件均`SUP_RAW_ABS_2606.<ID>v1_20261026.raw.b64`及`..._current...raw.b64`，原HTML gzip/base64；初次大响应截断废弃，四个每组五身份的成功小响应已保存；16222摘要中间另单独完整读回。当前短说明未见withdraw/erratum/具名重要纠错；15161题摘中的“absorption-aware correction”是方法词，不是纠错公告。15553 current数字不同，不由版本号触发全版本比较，仅采用v1。

`SUP_SOURCE_DATE_BATCH3_20261026.raw`保存20份原字段定位和复算。18份合法整个界Jun16 00Z—各03Z，同Jun16 BJT；14831跨Jun15–16、14752跨Jun09–16，尚须具名作者有限日期恢复。正式2026 README候选表精确ID无同项；15099/15405/15874/16364另有旧trace，root与Jun16唯一reader已定点核明确oldretained/deep/I/原9，均归旧Jun16。它们保原日期/原9，仅做旧采用正文必要核，不新评分/新计本日候选。

| 身份 | 具体准入决定点、原分或日期隔离 |
| --- | --- |
| 2606.15576 Hindsight Self-Distillation | P：answer-only privileged teacher不能定位中途分歧的信用 → 同组成功peer rollout提供hindsight、在与失败轨迹分歧处产生局部dense credit而不另采新rollout → 需重验成功信息如何进入策略更新及额外teacher成本。拟2+1+2=5，不凭最终正确率或self-distill名称准入。 |
| 2606.15161 Perturbation Absorption | P：局部重要性把剪枝扰动当独立损伤 → 在pruning尺度观察early放大/middle-late吸收，而小噪声各层均放大 → 重新考虑按扰动幅度与后续补偿能力分配剪枝，不能由局部小噪声敏感度直接决定层预算。拟2+1+2=5；深度普遍规律待必要，不先背书。 |
| 2606.15099 AVA-VLA | 旧retained恢复：Jun16 owner、原June13/sourceJun14/9分；不新计。潜在有限差额为按视觉/动作stream接口和执行验证适配，实际采用须读原机制与旧Ch26正文，不能旧I标签代替必要。 |
| 2606.14831 Playing Dead | 潜P：不可兼得的指令约束下并非总显式拒绝，而可伪造外部障碍/崩溃轨迹 → 原文以真实数据注入等干预检验解释 → 可能修正只核最终refusal而不核环境故障证据的判断。不采“不能被RLHF消除”的普遍结论；Jun15–16跨日，不正式评分/当窗候选，先有限日证。 |
| 2606.15405 T-Mem | 旧retained恢复：Jun16 owner、原June13/sourceJun14/9；不新计。Memory状态约束和更新机制须与实际Ch77完整body对照后处置，旧trace不证明已写。 |
| 2606.15753 RoboPIN | P：文字CoT可不保持实体对应 → 以name/id/view/spatial grounding的显式entity anchor承载中间步骤，并以anchor定位及跨步/视角identity作process reward → 需区分推理文字流畅与物理对象身份保持。拟2+2+2=6；anchor不先授真实几何或安全。 |
| 2606.16364 Looking, Not Picking | 旧retained恢复：Jun16 owner、原June15/sourceJun16/9；不新计。工具选择的输入可见性/候选消费条件需实际必要与旧Ch78正文核，不以旧高分认证新机制。 |
| 2606.15874 LLM-as-Code | 旧retained恢复：Jun16 owner、原June14/sourceJun15/9；不新计。模型输出程序与runtime所有控制的具体差额仍需必要，不从program/DAG命名或旧I推正文已完整。 |
| 2606.16360 Tyler | P：所有中间步骤一律文本化或固定latent迭代 → 每一步可发文本或调用typed latent operator（global plan/local update/procedural）且受预算策略控制 → 改变何种计算进入可见token与何时消费latent状态。拟2+2+2=6；若全文只是标签组合须据实际控制新事实再判，非名称准入。 |
| 2606.16222 Latent Thought Flow | P：确定性/只最大化reward的latent path缺少跨正确率与成本的概率分配 → variable-length stochastic continuous trajectory sampler匹配reward-induced posterior，以entropy-weighted subtrajectory balance和reference-prior稳定稀疏监督 → 需核轨迹权重、长度成本与探索是否真由此控制。拟2+1+2=5，不从9.5%/27.2%直接采用。 |
| 2606.16178 PRISM | 决定点：完整AB明确gated history抑spuriousaction与hierarchical local compression/temporal aggregation，但尚未辨明不同于gate+memory层次组合的实际条件或受控反证。只窄补gate如何区分当前观测与历史/更新权限决定准入，不为ReMemBench或四类memory新名称收候选，也不因Methods费时改N。 |
| 2606.16152 Quality–Utility Paradox | P：teacher trace正确/高reward不等student学习效用 → native RS与更高质量oracle trace比较，再以style-aligned logical repair干预拆出风格漂移/逻辑修复 → 改变如何挑蒸馏样本与把收益归因给正确率的判断。拟2+1+2=5；因果隔离是否充分留必要。 |
| 2606.16111 ParetoPO | P：质量与tool cost先标量化会丢Pareto顺序 → hypervolume动态权重后按dominance ranks形成advantage，而非只把多目标加权命名 → 需核轨迹/动作信用与frontier条件，决定是否改变policy更新。拟2+1+2=5，不以Pareto/hypervolume已知术语本身证明新贡献。 |
| 2606.16246 Data augmentations | P：固定数据多epoch可过拟合、继续加compute失效 → 区分token noise/permutation/target offset并以受控组合检验延后过拟合 → 修正data-constrained pretraining时只延训练的选择。拟2+1+2=5；current改题不另起家族，增强是否保语言语义与同预算反侧留必要。 |
| 2606.15553 Drifting RAE | P：semantic-cluster anisotropy使流轨迹弯曲、难做trajectory distill → 改以distribution-level drifting field直接训练单步生成，而极分散VAE空间并非同样适用 → 重新考虑latent几何与蒸馏目标的配对。拟2+1+2=5；v1为1.77/10ksteps，不混current1.48/16epochs，也不将几何观察当全因果。 |
| 2606.14752 XTokenizer | 潜P：不同action/visual表示混用可使VLA语义与精细重建争同码本 → residualquantization首层以MAM/semanticintent监督、深层保残差重建，配contrastivefoundation/nextVLfeature预测 → 需分开验semantic接口与下游动作消费。Jun09–16跨日，不正式评分/候选，先具名project有限日期恢复。 |
| 2606.15678 Reservoir attention | P：forward间无持续状态则须反复显式读历史 → 固定随机未训练reservoir在midattention读写、保跨forward压缩状态的小模型干预 → 需改变state初始化/重置与读取预算选择。拟2+1+2=5；只GPT2/Qwen有限证据，不采用“always-alive agent”生产叙事。 |
| 2606.16371 CacheMuon | P：每步重算polar-factor预条件器昂贵 → 依时域相近复用preconditioner并以staleness阈值/新solver残差约束重算 → 需核质量/算术前沿与净wallclock，不把省FLOPs当普遍提速。拟2+1+2=5。 |
| 2606.16154 WAPO | P：所有advantage符号一律同样更新可与entropy collapse相互作用 → 将advantage sign与当前token分布的梯度作用分解后，对positive-advantage分支采用clippedobjective → 修正何种负样本更新被视为必要。拟2+1+2=5；梯度分类与有效性范围待必要，非名称或高分准入。 |
| 2606.16256 KeepLoRA++ | P：只保护旧任务或只保pretrained主方向不足兼顾两者 → 同时投影避开两类特征子空间，并由浅至深重分update强度 → 需区分基础知识/旧task保持与新任务plasticity的约束。拟2+1+2=5；不先采用层知识普遍定位。 |

本层13个合法新拟P、1个合法决定点、4旧链、2跨日潜P；所有仍待root原件准入/日期层，不计必要完成或已定分母。支持与关键反侧足够即停，不为缺可选代码自动H。

16178窄决定点已恢复（待root准入）：原HTML`SUP_RAW_HTML_16178_20261026.raw.b64`。仅III-B/C真实接口及V-Q4/IX直接适用条件，未展开全部实验。确为借用post-attention sigmoid featuregate+local/global压缩，本身组合不够；但Q4同控制器去gate退16point、忽略逐步输入的per-layer scalar只+3point（29%对42%）、以attention sink替代亦无效，IX过平attention明显失败而较sharp非单调。该控制区分“有一个历史过滤模块”与“当前输入条件化、何种选择性”对闭环history消费的成立条件，足以修正仅延长memory/放dummytoken的设计。拟P，2+1+2=5；不采用‘spurious因果已全部识别’或所有长horizon普适，也不为新ReMemBench/5–12%指标准入。DATE_BATCH3合法整个Jun16与current短信号复用root§23，分母待本决定点校准后才冻结。

## 固定官方标题补检首5控制：exact-v1准入提案

官方六类月导航仅取2606.14700–17050固定号段的相关标题，补足主题术语盲点而非整月队列。首5具名原DataCite完整payload/字段/合法界见`SUP_RAW_TITLE_CONTROL5_20261026.raw.b64`；所有上下界同Jun16 BJT。实际发现PACT/HiMPO metadata是当前v2/v3描述，不能倒填v1，已逐份恢复并完整读exact-v1 AB、当前Comments及撤回/纠错短说明：原件`SUP_RAW_ABS_2606.<ID>v1_20261026.raw.b64`/`..._current...b64`。当前只见普通rev日期/Comments，没有具名撤回/纠错/安全修订提示；不做全版本比。2026正式候选行和Books精确ID无同项命中，尚未Methods或Book。

| 身份 | 原文增量与拟投入 |
| --- | --- |
| 2606.15079 Ling/Ring2.6 | P：从头重训不是唯一升级路 → architecture migration把既有base移入Lightning+MLA混合注意力，并在KPop对多类环境异步训练 → 需核迁移状态/长context与异步rollout的具体执行边界，不因1T/多模块或榜分准入。拟2+2+2=6；必要只取实际机制，不追整份所有宣传。 |
| 2606.16215 PACT | P（仅v1）：experttrace直接hint会让训练rollout偏离promptonly部署，纯RL又credit稀疏 → rollout仍promptonly，仅优化时traceconditioned surrogate与annealed reasoningprefix/toolcall SFT，另promptonlyanchor → 改变特权信息注入的位置/优化人口，非普通SFT+RL堆叠。拟2+2+2=6；current新增更明确标准RLanchor表述不倒填v1实现。 |
| 2606.16285 HiMPO | P（仅v1）：trajectory回报把tool失败归给memorywrite → 固定同prewrite状态比较旧/新memory可恢复的任务信息，hindsight boundedfilter再给memorytokens辅助advantage → 需核memory特定信用/其他token更新，非把最终reward换名。拟2+1+2=5；v3 targetloglikelihood具体公式不冒v1已披露，必要按v1。 |
| 2606.16633 DCP-Prune | P：超低token预算下仅重要性排序可保不住完整feature分布 → 删除前传context，distributionconsistency代理检测严重shift时重选代表token → 需重验分布恢复与token选择资格，而非16token数字本身。拟2+1+2=5；相关性不先授唯一性能因果。 |
| 2606.16808 Safe Trigger | P提案：初次unsafe回答与重读自己trace后的risk识别不同 → 从自身重呈现生成训练材料，显式safe tag在初始reasoning后触发安全分析，SFT后DPO保持该条件 → 可改变何时消费自生分析及训练/部署条件。拟2+1+2=5；不以latentawareness新名或SFT+DPO组合证明新机制，若该接口仅标签而无有效条件需窄决定点，不采almostnoimpact或安全保证。 |

这5的exact-v1/日期/短说明交root先校准，后续固定范围相关题摘仍按贡献筛选，不因候选审阅量删池或将所有303身份逐项关闭。不是五份currentDataCite摘要直接准入。

## 固定标题补检下一窄层：9拟P、3决定点与代表N

原DataCite完整payload与envelope分两原件`SUP_RAW_TITLE_RELATED_BATCH1_20261026.raw.b64`（15）/`...BATCH2...`（14）；只作身份/日期/当前AB恢复。9拟P与3决定点已另逐份完整读exact-v1题摘和current Comments/撤回纠错短信号，原件命名`SUP_RAW_ABS_2606.<ID>v1_20261026.raw.b64`/`..._current...b64`。12身份的2026正式README候选行逐项精确ID无命中。原字段均exactDOI、client=`arxiv.content`、state=`findable`，唯一v1提交为Jun12 18:54Z至Jun15 10:45Z，按公告日程最早Jun16 08:00BJT；registered原精度为Jun16 03:11:49.000Z至03:47:34.000Z，联合界均在Jun16自然日，不拿单字段当公开日。没有具名早稿/撤回/纠错信号；普通会议接受、project/code链接或rev日期不触发全版本比。

| 身份 | 具体增量与拟判断 |
| --- | --- |
| 2606.14892 Relational Structural Causal Models | P：可变对象组合的环境模型不能由旧对象组合观察量自动识别 → 给出连观察查询也不可识别的边界，再以relational causal graph/显式假设恢复包括潜混杂下的识别 → 改变WorldModel组合泛化和反事实声称的前提；不是给交通领域涨指标。拟2+1+2=5，必要只核拟采识别命题/反侧，不预采全部‘provablycorrect’。 |
| 2606.14943 AC-GPT | P：普通causal nexttoken不能直接支持任意past/future条件 → 修改同一causalTransformer以在保留LTR/NTP与既有权重适配条件下求arbitraryconditional → 改变补全/条件采样的接口选择，不以架构新名准入。拟2+2+2=6，单pass和不损原质量待必要限定。 |
| 2606.14997 AI Engrams | P：全局纠缠权重中的可编辑trace并非天然可分 → 将specificity/reactivation/sufficiency/necessity写成约束逆问题，闭式估计及自然梯度联系支持有限线性组合/擦除 → 需重验编辑独立性/叠加与曲率前提。拟2+1+2=5，不采用所有LLM任意记忆可无损删除。 |
| 2606.15080 AdaMame | P：恒定binary语言奖会在正确率/中途切语/长度间冲突 → v1以queryconditioned alignment factor在RL过程中渐增，从多语言探索到querylanguage利用 → 改变何时施加语言约束及其与accuracy信用关系。拟2+1+2=5，SFT+GRPO组合和Pareto宣传本身不算贡献，必要保具体退步与全费。 |
| 2606.15216 SPOKES | P：逐样本质量/去重proxy不能直接代表集合多样性 → 对G-Vendi集合目标构概率选择并用exponentiatedgradient优化，可和quality联立 → 改变给定数据预算的选择对象/优化权，不以+489指标准入。拟2+1+2=5，离散成集、embedding/质量混杂留必要。 |
| 2606.15345 XBCP | P：常规浏览把query/evidence同语言掩盖接口盲区 → 固定英文Q/A只改证据语言，连oraclegoldevidence直供仍退 → 将retrievalfailure与agent侧跨语整合分开验收，而不是只新增12语言榜单。拟2+1+2=5，翻译质量/控制人口与独立归因强度留必要。 |
| 2606.15476 FARM | P：多匹配物体/参照物关系不能靠单object描述或VLM全历史直接消费解决 → 视觉语言负责parse/visualscore，显式objectsymbols/relationalpredicates负责几何约束，memory保viewpointevidence → 改变开放词汇实体检索中的语言/空间计算分责。拟2+2+2=6，不因5–10Hz或榜分预授实时/因果。 |
| 2606.16449 PermaVid | P：视觉生成后发生编辑会使旧context失效，单纯更长memory不解决 → appearance/depth双bank并以editaware更新/检索维持后继条件支持 → 改变编辑后的memory失效/复用资格，而非RGB+depth组件组合命名。拟2+2+2=6，实际更新协议与非编辑/不变几何反侧留必要。 |
| 2606.16541 BPF/Faithfulness Gap | P：typecheck/可证不认证NL语义同定理 → 用双向consequence neighborhood、针对漂移的反事实probe和预算路由形成额外faithfulnesssensor → 改变formalizer的验证接口；不是新benchmark/理论名。拟2+1+2=5，有限probe与PAC/语义证书假设须必要核，不能先授普遍certification。 |
| 2606.15200 DirectMe | 决定点：AB仍只说增量structuredmemory/跟踪用户相对位置，未足区分已有perception+memory+reasoning组合。只补空间state/用户运动更新如何区分stale对象/视角的具体接口或控制证据，决定能否改变长期设计，不全读45页/不先评分。 |
| 2606.15367 S1-DeepResearch | 决定点：graphgrounded task+rollout+multiverify仍可能只是常见数据流水线。只核graph具体约束/verification如何验证openended synthesis而不只是LLM筛选与指标范围，够判即停，不以20榜单/32B准入。 |
| 2606.16523 SkillWiki | 决定点：AB列ingestion/provenance/governance/executiondrivenevolution未披露实际mutation/准入状态。只核execution如何使版本演化且受什么验收/失败回滚约束；单有生命周期组合/公开demo不足，不先评分。 |

代表性N及同理由层（29份current完整题摘均已读，不为清楚N投入Methods/日期配额）：14787商业图像编辑API的扰动指纹/表征聚类尚不能识别训练范式的因果机制；15078人类认知资本/债务宏观模型、16944人机心智参与SCM是人类/社会假设，不新增本项目模型学习或执行机制；15243图像恢复QAT的RL空间KD加权只组合已有奖励/权重/任务指标，未给foundation主线增量；15291业务AGO集合本体/查询与流程列举不新增执行机制；15300CODABench新codedata任务/文件场景和聚合正确率未披露受控新盲区；15507道德prompt的解释神经元标签/计数不认证所称语义或因果机制；15573DPprototype+公平QoS tokenallocation仿真未披露实际LLMserve机制/新条件；15911广告生成GenRM反馈迭代RL是领域套用，未见新的可迁移训练条件；16151GRACE步骤标注/8类错误与加入既有RL仅凭聚合准确率尚无足以改变判断的控制贡献；16491四臂人机系统/语音修正与碰撞组件/效率未披露新handoff或安全机制；16567通用NeuralODE verifier的区间/搜索scheduler与MNISTcontroller未建立foundation模型/生成sampler增量。以上不是因小模型、数学、benchmark或领域名称自动排除，实际区分机制/条件和套用/组合。

14700/14701/14702/14703原联合界同Jun15（非本补窗），仅记真实归属的恢复线索，不审别日或迁日。14721 DCMotion原界May29–Jun16跨窗，潜在coarse discrete/continuous residual增量不能先列确定本日候选/评分；无具名早稿入口时不无限搜索假想渠道，本窗日期隔离，重开需精确v1公告/作者dated原稿。9P/3决定点待root独立校准，未当必要完成或冻结分母。

## 固定六类末批标题差额：最终原件与准入提案（此后停止扩源）

完整官方月分页只提取固定2606.14700–17050标题，跨类1060唯一标题；与四主题568导航重492，另568不是逐项关闭队列。原303只最初四类局部导航，不能继续写作最终覆盖分母。最后这一差额中按实际相关标题选择63份，完整读原DataCite题摘（`SUP_RAW_TITLE_FINAL1/2/3_20261026.raw.b64`各21，含原payload），没有把1060、568或514变成AB配额。明确医学/农业/领域预测/科学应用标题不入队；有模型表示、优化、生成、VLA或Agent执行机制线索的题摘按同门槛判断，不因数学/小模型/负结果排除。

所有下表潜P/决定点已恢复精确v1与当前abs原HTML：`SUP_RAW_ABS_2606.<ID>v1_20261026.raw.b64`/`..._current...b64`，共51身份；逐份核v1完整AB身份，等同前面已读完整AB者复用原文，发生字句/机制变化者已实际读完整v1。显著差额：16184 v1名CoTriSyGen而非current EvoState；16730 v1确含linear-generator结构极限理论（root§62纠正），不能将其误说为没有理论；actual训练block不等该generator，current新增结论仍不倒填；16077 v1不含v2新增下界；14954 v1与current5的native-space限定措辞不同，若准入只核拟采定理实际假设，不沿版本号扩全史。当前短页只见普通接受/项目说明及16077‘v2新增结果’，没有官方撤回/勘误说明；15912的withdraw guidance和16969的corrected training不是撤回/erratum标记。

原字段+公开日复算见`SUP_SOURCE_TITLE_FINAL_DATES_20261026.raw.b64`，原payload亦可逐一回查。63中57身份联合界整个同Jun16；前6跨日，不把registered单字段改名为公告日。通过贡献者才需要日证，其余明确N不为日期另做请求。正式2026候选表对拟P/决定点逐项精确ID无行；Books只15306/16190命中旧trace，交root定点恢复旧retained，不先重计或重分。

| 身份 | 原有约束 → 原文具体增量 → 拟判断 |
| --- | --- |
| 2606.14900 GRASP | 多source同时融合须多模型驻留 → 逐source并入当前target、按target梯度方向逐参数准入后再适配 → 改变迁移state/negative transfer与内存前沿。拟2+1+2=5，不采O1即任意source无退步。 |
| 2606.14929 Low-rank embedding routing | 推荐item/embedding路由的常规regret会误设比较对象 → adversarial低秩expert+logquadratic policy与bandit feedback的可学习界 → 潜在改变模型路由的比较权限。拟2+1+2=5；项目范围须具体绑定embeddingmodel选择/表示学习，不把通用bandit定理自动当LLMserve贡献，待root范围校准。 |
| 2606.14954 Representation Costs | 参数weightdecay不一定诱导函数空间norm → 深度ReLU representationcost的quasiBanach/p=2/L结构与param/function优化连接 → 修正把深度归纳偏置当凸norm正则的解释。拟2+1+2=5，精确v1假设/current限定变化需必要窄核，不先采所有深度无条件结论。 |
| 2606.14958 MVEB | 同一audio输入在不同标签来源不等更完整groundtruth → 成对videoonly/AV、按annotation provenance出现方向相反收益 → 改变是否启用音频与多模态embedding评价人口。拟2+1+2=5，不以23task/33model榜单准入。 |
| 2606.14971 FastMix | 搜mixture多proxy贵 → 单proxy把sourceweight置入双层目标，验证feedback交替更新mixture/model → 改变样本人口、外层梯度与搜索成本，非‘自动选比’命名。拟2+2+2=6，等价权重/实际采样与近似梯度待必要。 |
| 2606.15085 YB Mixer | 顺序混合/变budget可能改函数 → 由局部代数约束构正交map及commutingtransfer、circulant长度扩展 → 潜在改变order/budget是否同一函数的架构解释。拟2+1+2=5，须必要核实际算子/假设，不以integrable名和数学外观认证稳定。 |
| 2606.15127 Bias acknowledgment | finalanswer不变掩盖trace未提示外部bias → 同注入人口分susceptibility与rubric表面acknowledgment，模型分离 → 改变trace可审计性与answeraccuracy的评价合同。拟2+1+2=5，不把表面提及当真实causalfaithfulness或安全。 |
| 2606.15162 GeoStream | 首帧固定3Dcache越frustum失效，自生成cache又递归带错 → 在线从生成帧重建/投影几何，并在训练也消费studentgenerated几何条件 → 改变二阶conditioningfeedback的人口/刷新合同。拟2+2+2=6，不采exacterror分布/真实物理或任意长稳定。 |
| 2606.15186 FreeSonic | 编辑目标与背景共享attention会互扰 → inversion后按时程解耦attention/区域限制，再按任务加noise → 改变何时允许局部条件改写背景。拟2+1+2=5，目标定位/背景保真与全费用待必要，不仅模块组合。 |
| 2606.15197 StarOR | fixedpolicy MCTS反复同偏差、只terminal credit稀 → 每非终结node用siblings比较组更新临时LoRA/GRPO → 改变searchstate/参数state与局部reward信用。拟2+2+2=6，v1不倒填current质量宣传/实现，reward无需gold不等语义正确。 |
| 2606.15217 Conformal Candidate Certification | 主动优化surrogate使候选分布偏离校准集 → Gibbs-tilt proposal导weights供加权conformal下界准入 → 潜在改变search后候选certificate的shift合同。拟2+1+2=5，范围/实际权重假设先校准，不以syntheticcoverage数字当普遍安全。 |
| 2606.15219 Single-index NN tradeoff | SQ下界不等梯度网络可达 → 标签变换/landscape smoothing与稀疏weightperturbation实现相应Gaussian模型featurelearning复杂度 → 修正计算/统计可达性关系。拟2+1+2=5，仅具体假设下可达命题，不读96页作配额或外推LLM scaling。 |
| 2606.15232 spatial PRISM | 相同encoder局部pooling与downsample会丢精细位置 → 受控spatialsoftmax比较+multiscale topdown crossattn保空间表示 → 改变低分辨率精密动作的表示瓶颈。拟2+1+2=5，和16178不同家族，不以同名/13.4数字准入。 |
| 2606.15268 Schatten-p | Muon式几何并非所有regime最好 → 低维/Chinchilla与noise/batch条件可使小p最优，SODA加速界 → 改变选范数/批量的适用域。拟2+1+2=5，必要核条件与非empirical通用处方。 |
| 2606.15306 LatentGym | 同task曲线不能区分跨任务探索与利用 → groundtruthlatent控制可分别量信息采集/使用及反馈条件 → 改变Agent经验学习验收，非新增环境榜单。旧Ch66 trace指Jun14，先待root旧链身份，不新评分。 |
| 2606.15332 Signature inversion | truncatedsignature非单射不支持单条路径恢复 → 条件分布目标+Bayes irreducibleerror基线、FM估计 → 改变何种恢复结果可识别/该验哪种error。拟2+1+2=5，只机制/理论人口，不采金融应用或‘wellcalibrated’无条件。 |
| 2606.15482 Ricci-Filtration | embedding近邻混入无关chunk → query/chunk图的curvatureflow过滤后再rerank → 需核结构community定理何时足以批准queryrelevance。拟2+1+2=5；潜贡献清楚/有效性留必要，不把curvature类比直接当事实过滤器。 |
| 2606.15493 Model multiplicity | targetfidelity相近被误当部署可替代 → 同Rashomon surrogate集比较ambiguity/discrepancy与groupfairness差异 → 改变抽取模型的兼容/经济推断，不采医学应用结论。拟2+1+2=5，实际非classicattack的权限待必要限定。 |
| 2606.15527 SSync | encoder/decoder全patch对齐传播各自噪声且成对二次费 → encoder只供边界/decoder只供内部pseudo监督并transitive合slot → 改变两个表示读者的监督准入和冗余身份。拟2+1+2=5，不因linear宣称免误差/全费。 |
| 2606.15534 Track2View | perframepose/pointcloud不显式跨view跨time连续对应 → source/target配对3Dtracks与几何transfer/时间聚合 → 改变video viewpoint conditioning的可见对应。拟2+2+2=6，tracker/paireddata/任意camera假设待必要。 |
| 2606.15569 Decision-theoretic TTT | 固定step/subspace在shift下会错配promptSNR → kernel/GP条件下spectralmatched更新、prompt evidence选步和方向 → 改变何时/多远/沿哪方向适配。拟2+1+2=5，理论角色不外推实际Transformer保证。 |
| 2606.15702 Schattor | matrix/vector混合和noise需不同geometry → Schattenfamily+matrix martingale stationarity、多block平衡 → 改变优化norm/参数块进展约束。拟2+1+2=5，仅拟采用条件定理，不以dimensionfreeheadline替证明。 |
| 2606.15832 SILAGE | globalfullgradient refresh或perexample controlvariate状态昂贵 → 利用nested groups保O(n) state/单localgroup更新与两层heterogeneity界 → 改变datasetpartition/refresh人口和训练state成本。拟2+1+2=5，不外推实际LLMkernel加速。 |
| 2606.15897 Topological FM | 欧氏reference忽略structured-domain连接 → Laplaciandrift改referenceprocess并保条件FM训练接口 → 改变生成路径/几何假设，不采用fMRI/海洋等暂缓科学应用。拟2+1+2=5。 |
| 2606.15912 Guided-OPD | student多轮小错进入teacher不熟悉state → 同rollout按turn混teacher/student并将interventionprob退到0 → 改变采样state/撤指导的部署分布合同。拟2+2+2=6，v1三环境单counter不采current改字的额外claim。 |
| 2606.15956 TDV | augmentation/mask的最优强度随data改变 → 对照biasstrength×datascale，再用frameembedding+encodedmotion预测下一表示 → 改变表征inductivebias随预算条件。拟2+1+2=5，不采‘无强假设’或仅pastcausesfuture即因果识别。 |
| 2606.16045 Low-rank data selection | cluster几何不代表全局低秩结构 → residualsampling/rowsubset与带加性rankerror的losscoreset → 改变数据选择误差对象/权重条件。拟2+1+2=5，不能漏additiveεΦk或把embedding条件当已验LLMloss。 |
| 2606.16184 CoTriSyGen（v1） | feedforward storyboard不回读已生成视觉 → 分intrashot重生成与intershot改prompt/mutableentitymemory → 改变生成事实对后续条件的反馈权限。拟2+2+2=6，仅v1机制，不倒填currentEvoState更细anchor/state标签。 |
| 2606.16190 Embedded Arena | simulator/静态估算不暴露真编译/flash/物理限制 → LLMloop实际读硬件反馈共同改model/firmware，no-feedback受控失败 → 改变candidate到真实deployment的验证边界。旧Ch66 trace指Jun16，先待root旧链身份，不新评分。 |
| 2606.16202 EgoPhys | 每object逆物理优化昂贵/难迁移 → 将逆解蒸馏进codebook预测dense springstiffness，对未见物体免perspringTTO → 改变RGBworldmodel初始化与可识别物理参数权限。拟2+1+2=5，真实robot物理主线，不采任意物性真值。 |
| 2606.16210 OQ-TSAE | 重建/任务准不能决定sensor支持哪些scene区分 → nuisancecanonicalization后的observationquotient与falsemerge/distinction控制 → 改变可表示/不可观测差别的验收。拟2+1+2=5，受控quotient标签前提留必要，不由radar应用指标入选。 |
| 2606.16317 Cumulative-energy sparseattention | fixedTopk/Top-p只保预算或mass一侧 → 以recall目标动态threshold/融合FA执行 → 改变mask预算与保真代理的耦合。拟2+1+2=5，massrecall不自动充分最终accuracy/免mask费留必要。 |
| 2606.16353 SelectStream | indiscriminatehistory稀释当前scene → 原currentobs直供、history只受queryconditionedlatentbudget暴露，write/consolidate/retrieve分责 → 改变current原证据与压缩memory消费权限。拟2+2+2=6，不以StreamingBench高分准入。 |
| 2606.16429 Taylor-Calibrate | copyteacher projections未定GDNdecay/write/outputdynamics → 用teacherattention统计定时标/gates/value并短layeralign → 改变hybrid转换初态与distill成本。拟2+2+2=6，matchedtargets/retainedlayerpolicy留必要，不采88x或9x普遍。 |
| 2606.16457 ResEdit | inversionnoise含冲突imagefeatures → 额外residualcondition补重建，并gradientreversal使其不携编辑condition → 改变identity保持与编辑通路的分责。拟2+1+2=5，不采完全disentangle或无配对免全部训练。 |
| 2606.16490 SAI | 两policy独立示教没见真实partner错相 → A与human学/B对deployedA学/再以失败附近介入修A → 改变合作策略curriculum的人口和耦合控制。拟2+1+2=5，不由无显式通信得无信息依赖/安全。 |
| 2606.16515 DCP | rawgoal远离访问域使条件无几何信息 → train选visitedsubgoal/方向幅度actor，deploy换最终goal并移除score，明确controllablesubspace失效 → 改变goalconditioning与train/deploy支持条件。拟2+1+2=5，不采任意learnedψ的HJB充分。 |
| 2606.16535 Symbol swapping | CBM高taskaccuracy/同conceptvocab不保证语义兼容 → 独立detector/head互换与减concept监督的受控collapse，多head可靠性约束 → 改变解释符号的compatibility验收，不以新metric命名准入。拟2+1+2=5。 |
| 2606.16661 SCAR | parent/staticwindow多拿上下文、fixedthreshold不跨embedding标度 → relevance相对主chunk加continuitypenalty决定邻块扩展 → 改变扩展资格/近似scaleinvariance条件。拟2+1+2=5，320query/同超参不授任意encoder免校准。 |
| 2606.16790 DW-FM | uniformfit误差不对应下游决策regret → endpoint决策权重改velocityregression/adjoint传输联系 → 改变generative训练loss人口与消费目标。拟2+1+2=5，不采用金融/traffic应用指标或idealweights自动可得。 |
| 2606.16883 Local robustness bound | globalrobustnessterm抹去各子域稳/不稳样本结构导致vacuous → 按子域stablecount重权的data/modeldependent界 → 改变何种鲁棒性统计支持generalization声称。拟2+1+2=5，必要只拟采假设/计数及直接反侧。 |
| 2606.16917 UMA | 异构动作/视频缺共同条件接口 → 3Dobjectmotion与robotaction共同maskedobjective，mask决定监督/部署模式 → 改变world/action目标的可消费角色。拟2+2+2=6，不采任意mask/无标签无先验或真实动力学保证。 |
| 2606.16969 Low-frame codec | 6.25Hz质量cliff被归音素碰撞/codebooksaturation → controlledframerate下改trainingclip/context token支持后cliff消失 → 改变低帧率表示容量/训练人口的归因。拟2+1+2=5，不以1.6Hz数字准入。 |
| 2606.16999 Frozen code falsification | 选择/修复常被当免费超BoN → leakagefree/matchedcompute的26operators负结果与extractor/signature修复正对照 → 改变coverage、selection信号与expressionharness分责。拟2+1+2=5，小1.5B不自动排除，不授全selector不可能。 |
| 2606.17037 Phase/sign transplant | 输入Fourierphase规律不自动说明hiddenidentity → hidden层跨样本phase/sign/magnitude干预，ReLU前后/DConly对照 → 改变readoutbasis与CNN/attention机制解释。拟2+1+2=5，不采所有模型magnitude可删或唯一texturecause。 |

另3只窄决定点、不评分：16436 V2P-Manip的两阶段refine须见具体物理约束/失效条件，不以3Dasset→trajectory→policy组合和领域成功率准入；16866 CustomShift须见实际attentiondistribution操作与sharedattention基线控制，否则dualbranch/maxentropy命名不足；17006 TuneJury须核newgenerator的anchorcalibration实际更新/比较约束，否则只是新偏好RM数据及现成BT+BoN/latentopt/EXIt组合。

末批清楚N：14715 exact-v1实为MiroBench（非后版ThreadBench），Reddit模拟分布差异及prompt改进未给本项目具体执行/学习条件（root§62纠正并保N）；14725 ConvNN把已有local/global邻域写进共同aggregation而未给改变设计的中间机制/条件；14765 MoFore forecast+contrastive+randomgap的UCF类聚合结果未隔离新有效性条件；14816是安全taxonomy/综述；14821 DOMprune+scrapersynthesis只组合通用流程和领域F1/reuse；14977是selectivelabel公平frontier统计，未建立模型能力/训练/推理机制的直接贡献；15141 EChO的plan/tool/evidence/verify组合及单项重要性尚未披露新的证据融合/验证条件；15641 B2B例子蒸馏分类criteria是领域prompt压缩套用，未给新训练/ICL条件；15669 actual§3/4及公开代码：球投影局部Jacobian不约束自由linear或layer(x)+x全残差，固定范数/切向1/R不授梯度不消失；已知投影改名及单设置MNIST未留可支持新长期条件，不因小模型排（root§62）；15760新几何testbed/estimator校准用途并未题摘披露足以修正具体旧bound/模型判断的结果；16038大SWE数据集/双teacher模式与榜分未给新distill机制/ controlledblindspot；16077 exact-v1是Booleanfamily的MBLG组合博弈上界，未建立本项目模型表示/学习/生成机制关系（currentv2下界不倒填）；16730 exact-v1确有linear-generator的ME/平衡结构极限理论，原‘无理论’理由错误；actual§1–5训练block非该generator，blockpool/zero gate与ODE映射及有限neutral结果尚未修正具体LLM判断，仅此贡献边界保N（root§62），不因理论/负结果排；16748 MyPCBench新persona/app/task/长轨聚合失败未展示控制人口下的新机制/盲区归因。不是按标题、理论、benchmark类别或审阅成本改N。

14723 crossmodelrouting有潜在同模型相关错/temperature0管线方差→disagreement只路由另一family增量，但联合界跨Jun02–16，暂不评分/列本窗。已恢复精确v1/current原页且无具名早稿链接/短说明；重开需当期精确v1公告/日列表或作者dated正文，不追全部假想渠道。63止于此固定末批；尚未展开必要者只是普通待办，不以source停止当DAY。此表待root准入/日期/范围及代表N实际独核，分母仍不预冻结。

末批准入校准修正（root消息，未变层复用）：14929实际是推荐query→item动作的低秩bandit、非embedding/LLM服务路由；15332实际是truncatedsignature病态逆问题/随机过程Bayes基线+现成FM，未建立foundation生成/表示新机制或条件；两项具体项目贡献前N，不保原拟分，也不因理论或金融名称泛排。15306/15345/16190三份明确旧Jun16 retained原9恢复，前两原June13/后一June15，Jun17不重计；Jun16作者/reader负责必要/实际层，本日不重复Methods。

15217范围窄决定点已实际关闭提N：原HTML`SUP_RAW_HTML_15217_20261026.raw.b64`，只Intro前段、§2应用变量、§5.1实验对象与§6Discussion确认。Intro明列proteinengineering/moleculardesign/materials，X是design/Y是实验response；§2是静态dataset训练surrogate再提候选design，§5只有一维合成函数的OOD设计压力测试。没有模型训练/架构/生成候选选择的具体对象或新机制，平台release联系仅本项目类比，故不符合当前主线/AIforScience边界，不准入不评分；未展开CCC方法/证明或给统计证书背书。准入决定足即停，不因本来拟P而全文审计。

16523 SkillWiki决定点关闭提N：原HTML`SUP_RAW_HTML_16523_20261026.raw.b64`，实际§2.2/2.3、§3.3/3.4、§4.2/Limits及B monitoring必要决定范围。确有candidate→snapshot/diff/review/release、executionhealth→maintenanceproposal、版本/来源图等可用软件系统，但这些是Git-style治理与常见asset lifecycle的组合；未给新的proposal验收、inflight版本切换/恢复或安全执行条件。§4.2只单API文档走过S0–S7的case，B以success/fail计数与reflection触发流程；未受控展示这份治理相对既有version/review新解决何种执行失效，Limit承认下游/长轨与长期稳定未测。不是因demo/规模小自动N，而是决定点后仍无足以改项目判断的机制增量；不评分/不读完整repo或生产125材料配额。

16808 SafeTrigger窄决定点事实（待root准入，不预Methods完成）：原HTML`SUP_RAW_HTML_16808_20261026.raw.b64`，实际§2、§3.1–3.2前部与§4.3限定受控人口。RISR是先成功输出unsafe的条件子集上额外安全prompt重呈现query+自生think，不能和全体ASR百分比作同分母对比或认证latentawareness。值得核的具体接口比AB标签组合更窄：二阶段数据生成先得think1/answer1，再对同query+think1安全审计得到think2/safe/answer2；SFT最终拼原think1+safe+answer2而舍弃think2，使审核内容在原推理前缀之后成为可学习的可选分支，general样本不含safe。部署不需要外部再提示，而由模型在reasoning后选择safe段；它改变训练context拼接/干预位置，不仅SFT+DPO命名。§4.3只safe-outcome交集上的entropy/长度不证明同预算安全因果，激活率也不是安全校准。拟P原2+1+2=5可只针对这份context/触发差额继续必要；若root判断仍只是现有selfcritique流程重编码，则按具体事实N，不以高ASR改善倒推。没有展开完整DPO奖励推导/全部主表，不授latent自知/无影响或安全保证。

15200 DirectMe决定点提N：原HTML`SUP_RAW_HTML_15200_20261026.raw.b64`，只§4.1–4.3与D3对应坐标/在线接口。具体是DA3depth/pose、DINO检测+SAMtrack、worldframe map/objectanchors，再在query时用inverseego pose把关系转回当前用户坐标、取subgraph/keyframes。已找到的状态更新只是标准worldalignedmapping/scenegraph+ego坐标转换与retrievalQA组合，没新增状态估计/失效处理或受控证明何种组合条件改变模型能力；不因benchmark规模和场景名入选。正文causalstreaming与D3offlinegraph/另一路spatialcaptions的口径差异不被当作排除理由或私补实现，仅不据此采严格在线/无futureleak。决定事实已足，不审45页/代码或为访问困难改N。

15367 S1-DeepResearch决定点提N：原HTML`SUP_RAW_HTML_15367_20261026.raw.b64`，只§3.1/3.2任务/约束生成、§3.3/3.4执行refinement/verifier与§5.3有无控制。实际是Wikidata/web双路扩图、connectedcommunity选taskcontext、九类约束注入/语义改写；rollout后重写report/lastThink、文字转文件/图片输入，再用引用/约束/LLMjudge与script存在性筛轨。未披露新的图执行/验收算法、openended事实核验资格或受控新失败条件，所示testtimescaling/参数榜分不把这套常见合成数据流水线变成机制增量。不是因开源/32B/组合有多模块自动N，决定点后仍只有任务覆盖和已有步骤的组合，不评分/不读全bench/附件/参数。

最后三个窄决定点原件均已实际恢复，以下拟P待root校准、不预必要整体或Book：

| 身份 | 实际决定事实/具体采用边界 |
| --- | --- |
| 2606.16436 V2P-Manip | 原`SUP_RAW_HTML_16436_20261026.raw.b64`，实际§3.2/4.3/A5起与Limits。不是只perception→policy组合：先全contactframes拟global scale/rigidoffset、再perframe姿态/接触/平滑修正；retarget后先仿真检查objectpose在有限steps内是否稳定，稳定帧保留，只对不稳帧作TWS/GJK接触wrench修正，再供imitator+residual。T3 Origin/w/oC1均0，w/oC2均54.4/full79.3仅所测8task/100episode，说明几何拟合与接触可行的不同准入角色，非高领域分本身。拟2+1+2=5，仅这份conditionalrefinement资格/对照；floatingbase无armreachability/仅rigid限制保留，不授全轨物理安全/精确metric或净省费，未核后续训练recipe/所有表。 |
| 2606.16866 CustomShift | 原`SUP_RAW_HTML_16866_20261026.raw.b64`，实际§3.2/3.3/4.3/4.4。maxentropy推softmax本身不是新增；可取的是reference在clean t0、各ref独立序列层对齐，再由x/p共同读refKV。§4.3.2实际把独立alignment换成多ref共享attention/tokencompetition，CLIPText略升而DINOidentity明显降，区分语言遵循/多reference身份消费权，不是dualbranch名。具体对照能改变是否先独立处理reference的选择，拟2+1+2=5；noising只图示没硬控不升理论，参数/超参匹配仍必要，不采任意ref无污染或线性复杂度。 |
| 2606.17006 TuneJury | 原`SUP_RAW_HTML_17006_20261026.raw.b64`，实际§6 Anchorcalibration及D的postcutofffailure/校准限定段。新增模型后不是通用重训：冻结原RM/encoders，以一个IDsystem β=0固定gauge，在postcutoffpairs上拟各system additive BT offset，目标是temporalcutoff的systembias；D同heldout 50/50/五seed比较fromscratch retrain，且FebMar小K offset转April反退、更多pair才近raw。这个identity/校准人口边界可改变新generator上线后选择重训还是局部校准，非新musicRM+BoN应用组合。拟2+1+2=5；不采25x普遍/encoderdrift全修或margin天然置信，未审三application/完整RM主表。 |

16184 CoTriSyGen exact-v1窄决定点（待root）：原HTML`SUP_RAW_HTML_16184_20261026.raw.b64`，只§3.2/Alg1相关读写/§5.4文字反侧与8.2.2.1实际MemoryController更新资格，不采用currentEvoState后增机制。v1 entry为(name,description,referenceimages,optionalbaseentitylink)，关键不是通用VLM重写：view/物理state/服饰发生continuitycritical变化时创建linked evolved entry，旧entity仅在visualform/state/viewpoint语义都匹配当前shot时复用。Keyframe前的缺entry会T2I生成并注册，postvideo再将新表现/变化写到M∪U并改下shotprompt；两种producer不能都称实际视频证据。§5.4 prekeyframe仍更新但取消postvideo synergy、或取消promptrefine时，会取过时paintingstate/不合dorsalview，至少指出同名对象不等当前appearance版本、refinement影响检索资格的具体条件（只文字病例，未看图像素/未认证全部因果）。这比初AB的memory+VLM组合多出state/view分支身份/复用资格，可支持拟P原2+2+2=6继续必要，若root认为仍为已知分支语义套用则据此决定，不以高榜分准入。Alg1预算耗尽SelectBest不是accept guarantee，generatedappearance只合成条件非物理truth；未读所有实验表/全部prompt或实现。

恢复后root§62已独立抽检末14N中的14715/14816/14977/15669/16730/16748六项，理由具体纠正如上；其余不是全量Methods认证。root§63实际六决定域后：16436/16866/17006各原5与16184原6准入；15200/15367具体N关闭。上面‘待root’均为原提案历史层，当前以本条/root canonical§63为准。原85+新4=新增89唯一家族（86arXiv/3官方），旧51另保；有限Source/准入层关闭并冻结，不再扩号段/导航，7日期和历史目录隔离不授Coverage通过。普通必要/actualowner仍63，不因冻结或决定层已读就预完成。
