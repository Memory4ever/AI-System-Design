# Sep12增量来源独立复核

## 1. Fresh上下文与原有效层

非作者Cicero，作者Meitner。本次真实检查已到2026-10-12，按human连续ownership仍只写本日`SUP_INDEPENDENT_20261011.md`，不擅改文件名或另建review账本。实际重读当前AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、SOURCES使用说明/Daily/arXiv、PROMPT、ROADMAP、最新State路由及本日完整原六部分README、HANDOFF、SCREEN、RECOVERY_SCREEN。只加载本日，不继承Sep10/其他日期研究队列；月checkpoint只路由，不自行更新计数。

新补Sep11完整BJT自然日，不catchup、不要求公开时分秒。原窗口`2025-09-11T09:00:00+08:00 ～ 2025-09-12T09:00:00+08:00`、旧候选日期/评分、有效审阅与连续原§4冻结；原formal0/Books0。原111唯一家族题摘=84日期潜力/27关闭，另46明确领域标题退出；其中原24 exact-v1与恢复87 current（52v1/35后续版本）分开，不把后续AB倒填2025v1，也不将518月邻段扩为队列。

原root有效独核实际范围是原/新增各六机制样本、九安全/设计反侧完整题摘及四退出样本；09082必要v1§3.1–3.3使训练分配潜力恢复，08867能耗与09448 TORSO必要局部已澄清，PLAS两精确旧doc/模型更新及性能算术反证有效，不因换reviewer重开全附件。未抽检旧普通退出不称非作者全量验证，九风险仅题摘不称威胁模型全面审阅；只在决定准入事实仍含糊或具体纠错影响时补必要core，P已清楚仅date未证不扩全面Evidence。

旧Vault官方Sep12日期/时刻交叉hold及PLAS重述关闭不迁日。Qwen3-Next原ISO Sep10T20Z为BJT Sep11，旧9am窗外但新完整自然日可能准入，需本日具名官方正文/date/当前说明、具体新增及必要证据/Books比较，不因机构/版本号自动收。先处理准备好的单篇，不等整批来源。所有新未读/含糊属于ordinary，不静默外部化。

只own本note；不写作者README/raw、Books/State/index/scripts，不stage/commit/push，不换模型，保护dirty。共享Books若有已确认长期缺口，先协调root/owner及实际写入，不以主题相似已有覆盖或仅报告绕过。新FIRST/全部拟入选/安全反侧、14source有限停止、必要Evidence与具体Books、六部分DAY/完成态FINAL继续推进，尚不授本日完成。

## 2. Qwen3-Next具名单篇先准入

本人实际结构读本日fresh`SUP_QWEN_20261012.raw`中完整Qwen3-Next item：id/title/author/date/tokenLinks。官方原ISO`2025-09-10T20:00:00.000Z`归属BJT Sep11，落新完整自然日；不改变旧9am窗外归属。实际读`SUP_QWEN_NEXT_BODY_20261012.raw`官方tokens正文Introduction、Key Features各项、Pretraining与Posttraining核心说明、Ultra-Long Texts的static YaRN限制及Summary，图像只看metadata，未读像素；当前已读核心未见撤回/纠错说明，不为证明无信号遍历全部版本。

**FIRST P通过。** 纯linear的recall弱与full attention上下文成本→3:1 Gated DeltaNet/gated attention混合、attention output gate与Zero-Centered RMSNorm/norm decay/router初始化稳定性、512专家/10 routed+1 shared的稀疏容量、native多步MTP训练→具体版本的训练/推理机制组合与状态成本选择。不是机构、参数量、榜单或10×数字倒推准入，借用既有DeltaNet/MoE/MTP原则不自动算本材料新增长期知识。

必要采用边界：仅官方披露的版本设计，不授3:1在所有任务/预算普适最优、sink/activation全面消失、每expert初始化无偏作为最终公平保证；15T与36T/各base比不是单因素受控归因，9.3%/10×未配完整hardware/precision/batch/concurrency/SLO/evaluator预算不外推同质量端到端。Native MTP说明multi-step训练/接受率目标，未读accept/correct实现不能继承AR精确投机语义。作者声称RULER胜出不证明只由hybrid因果；static YaRN固定factor可能损短文本的明确反侧保留。未运行/复现/API测试，未授artifact或完整模型代码验收。

准备好的单篇继续评分/最低必要Evidence及ROADMAP owner的实际具体Books差额，不等arXiv整批；本节仅准入/date有效层，尚不授Evidence/Books或DAY完成。当前不以缺机械freeze索要所有历史全文。

## 3. Qwen单篇评分、Evidence与Books实际裁决

实际读作者`SUP_FIRST_20261012.md`及`SUP_QWEN_NEXT_EVIDENCE_20261012.md`，并独立补读官方tokens105–174的部署文字/Note（不读代码即不授实现）：Transformers MTP并非一般可用，吞吐依赖实现；SGLang/vLLM的main支持不是任意release能力；默认256K无法启动时明确建议32768；环境override不证明容量。结合§2已经实际读的核心与static YaRN反侧，**接受2+2+1=5、标准完成**，只采用版本recipe与披露的互补状态选择。没有把成熟原则、高榜单或未核代码计入评分，未授复现/生产/完整性能保证。

Books实际定点读`MODEL-LONG-CONTEXT` Ch22当前§“从累加到定向编辑”及§“Output gate不等于跨时间的Memory gate”：前者明确GDN固定矩阵碰撞/遗忘与chunk执行、hybrid互补，后者保留SDPA/KV并区分输出门与跨时间更新。读`MODEL-MOE` Ch21当前112–140及655–704：active compute不等runtime、load balance不等语义公平、joint条件人口和校准/初始化分支；读`INFER-SPECULATIVE-DECODING` Ch48 515–545：native MTP仍需full target verification，架构绑定与独立drafter共存。不是只看标题或主题。

**仅报告通过，Books新写0。** 现书没有本版3:1、512/10+1与Zero-Centered配置，不称该版本已被覆盖；公开bundle未控制新比例/norm/router条件，尚不能改写长期选择规则。现有具体正文承载可采用的稳定边界，本版参数留报告，没有已确认共享Books gap或缺owner。实际新反证/受控条件到达才定点重开，不以仅报告逃避可执行整合。此为单篇裁决，不授DAY。

## 4. 新40 exact-v1首批与当前轻核

本人实际完整读`SUP_EXACT_0_20261012.raw`25条及`SUP_EXACT_25_20261012.raw`15条的**v1题名+完整摘要**，逐项读40个`SUP_CURRENT_<id>_20261012.raw`当前title/comments/submission-history与撤回/纠错信号。没有以当前AB替v1；submitted窗口只是发现线索，未授first-public日期。当前初判10P/19C/1撤回信号隔离/10必要含糊ordinary；N不是外部缺口，待必要core判明后本节追加最终差额。

| 2509身份（另注明2510） | 暂定 | 本人具体判断或必要差额 |
| --- | --- | --- |
| 08729 | P | 多轮压成单轮的进化模板搜索与length/StrongReject评分耦合，是攻击/评价条件潜力；不授成功率普遍性。 |
| 09058 | C | 基因variant pipeline特征预测执行时长与job-shop调度；无LLM训练/推理运行时的新条件，不由GPU词收录。 |
| 09116 | C | 叶片FM与text-attention的层级植物分割组合/跨品种指标，未建立基础模型一般学习/评价机制差额。 |
| 09195 | 隔离 | v1实际weather阈值/双decoder目标按AIfS退出；current评论明确整稿方向pivot后撤回、v2标withdrawn。保留v1事实与当前信号，不把v2倒填v1，也不采用该稿。 |
| 08827 | N | survey摘要只显taxonomy/未来方向；必要contribution/discussion判断是否实际新机制/反证，不以survey名关闭。 |
| 09052 | C | per-grid/lead-time weather模型ensemble gating改善RMSE，是天气目标，非主线MoE机制新增。 |
| 09014 | C | MSCOCO翻译与既有COMET/CLIP/backtranslation质量流程，新增语料未给独立评价盲区或筛选条件。 |
| 08824 | N | 葡语continual pretrain的数据filter选择可能改变数据取舍；读必要筛选对照，不能按language/dataset名关闭。 |
| 08826 | P | VLM yes-prob生成reward替代相似度/BT目标及scale设计；高variance不自证抗hacking，保留该安全反侧。 |
| 08803 | P | 模型scale与confidence/accuracy、语言/地域的局部反例改变校准评价；不是fact-check领域标签关闭。 |
| 08721 | P | heterogeneous节点不同policy共享rollout的异步RL接口取舍，94%不是普遍效率保证。 |
| 08825 | P | LLM标注导致Type I/II/S/M及可人为制造显著性，现回归correction不足是评价/数据反证。页内correction不是官方勘误。 |
| 08753 | P | prealigned delayed streams将read/write决策化为decoder序列关系，是流式跨模态机制，不按ASR应用关闭。 |
| 08785 | C | 既有RL建议+LM叙事的gridworld实验平台与未来研究可能性，未给实际新执行条件或已测影响。 |
| 08736 | C | 化学知识缩BO空间/伪数据及wetlab目标，AIfS；Agent词不重引入。 |
| 08755 | P | interaction horizon由exploitation逐步转exploration以防长程collapse，具体训练选择，不只framework。 |
| 08809 | N | student/noisy teacher的CAI一致性proxy可能是新评价条件，必要定义/关键对照判别，不能把一致性直接当正确性。 |
| 08813 | N | 3D FM pointmap+robot pose联合scale/calibration是否有独立系统约束，读必要optimization。当前v2改title不代v1。 |
| 08961 | C | wavelet/CBAM/GAT/TST用于ECG多病分类，foundation命名不建立主线机制新增。 |
| 08820 | P | VLM visual-target→VLA接口及success/compliance反馈，属真实VLA机制潜力，不能因化学载体默认退出；不授全安全。 |
| 08778 | P | Qwen早层attention与既有GPT MLP事实回忆结论不同，架构解释边界反证。 |
| 08757 | P | social-nav场景VLM低于规则/human一致性，具身前置感知能力盲区，不按benchmark/局部关闭。 |
| 08715 | N | 摘要只有compact encoder/1.2B指标，Q-gated实际机制缺，需方法/关键对照判别。 |
| 09130 | C | PET Radon/sinogram几何、lesion mask/ROI及任务内低样本指标，是医学采集物理目标；attenuation correction非勘误。 |
| 08935 | C | SAM3D传播+生存radiomics的医学预测链，未给基础模型主线失效条件。 |
| 09397 | N | DRiFt的task-agnostic/clinical feature分离+LoRA可能有shift机制，必要定义/对照，不因医学题名关闭。 |
| 09307 | C | 材料characterization专家任务benchmark及专业视觉差距，AIfS目标，未给主线一般评价新条件。 |
| 18122 | N | GAUSS skill隔离是否有实际新评价盲区/条件，必要task设计/关键对照；仅新增rubric/模型profile不足。 |
| 09482 | C | relational hetero-GNN的database view determinacy解释，未建立foundation模型形成/系统的直接桥。 |
| 09254 | C | 牙科instruction语料、五诊断维度、64模型domainaccuracy和SFT提升；未给跨模型评价机制/独立失效条件，不按医学标签本身退出。 |
| 09544 | C | financial ontology+LLM KG抽取做文献趋势归纳，未给新增执行/可靠性条件。 |
| 18123 | C | Soil moisture textualization+domainprompt用于灌溉检测，农业目标，不由LLM名收录。 |
| 09303 | N | positive-only LF是否形成可复用弱标签条件，必要loss/关键对照，不仅patent映射目标。 |
| 09740 | C | GO hypotheses embedding/一致性分离分数选择gene cluster resolution，AIfS。 |
| 09751 | N | crypto actor/judge/metajudge自改policy/评价是否有真实新增机制或自评失败边界，必要局部判别。 |
| 2510.15898 | N | HealthDial FSM与no unsafe advice强主张，必要execution/验证条件，不能仅按医学或UI平台关闭。 |
| 10570 | C | trajectory survey三类映射/融合/约束与未来研究方向，摘要未给新测安全/latency条件；survey标签非理由。 |
| 09251 | C | machinery fault的time-frequency augmentation/meta contrastive，目标内性能不建立foundation主线机制。 |
| 09229 | C | resume分类hybrid真实/合成样本与偏见愿景，未给具体LLM评价混杂证据。 |
| 09530 | C | US probe trajectory的local/global双encoder/fusion，领域几何目标，未改变foundation representation一般条件。 |

40个current仅09195明确撤回信号；其余已读官方轻层未见相关withdraw/erratum/correction，不为证明“没有标记”遍历所有版本。未来2025会议题名不触发全会议搜查；明确C无需为不影响处置的日期扩证据。含糊10项已请求作者保存必要exact-v1 core/raw，准入清楚P若只公开日未核即精确隔离不评分、不读全篇。

## 5. 必要core实际收敛与反侧

实际读13份`SUP_NCORE_<id>_20261012.raw`的下列**exact-v1必要局部**，不是13全篇/Evidence完成。10个N全部变为6P/4C，加3个既定P的直接安全/设计反侧；新40最终**16P/23C/1当前撤回信号隔离**。P只表示具体潜力，未核first-public的不评分、不入正式候选/Books，不以缺日期继续扩大全文。

| 身份 | 实际位置与最终裁决 |
| --- | --- |
| 08715 | §3、4.5、Limitations，P：pooled question与visual patch预测sigmoid residual gate，再投影pseudo tokens；Token Balance/Visual Query替代融合从60.8到58.7/55.7，提供具体融合选择/反退。冻结与unfreeze说明不完全一致，不授任意模型可部署/每个回答都正确。 |
| 08809 | §2/3，P：MiniLM从5%用户标注以top5 similarity选类，再与zero/single-shot teacher三路一致性构CAI；只有60%选对最佳模型，Massive Scenario差7.83pp，proxy不等真值、不等无任何监督或独立judge。 |
| 08813 | III/IV/VI，P：FM pointmap无metric scale，联合robot AX=XB、每camera scale与rigidity/重投影loss；无视野overlap时不能从视觉推共同scale，运动多样性不足限observability。联合与two-stage选择是实际系统差额，不因校准机器人应用退出；不授FM自动拥有真实坐标。 |
| 08824 | §3.2、4.2、4.4，P：相同TinyLlama起点下C4到约80B/单epoch后反退、MassiveWeb劣于未滤；教育/STEM混合在60–150B反而落后，晚期再优。具体过滤/预算边界不是只增葡语corpus；continued与scratch预算/初始化不同，不授单因素收益。 |
| 08827 | §1贡献列表/4.4，C：归纳既有reward/ratio/sampling及引用别人contradictory normalization/统一评价，没有本稿新增机制/独立对照或新纠错。没有因survey类型自动关闭，也未读117页全部附件。 |
| 09397 | §2/4，P：invariant/spurious投影、KL neutralization、conditional HSIC与LoRA/prompt组合改变shift条件；contrastive loss可损迁移、深prompt反退，属于foundation适配取舍，非仅医疗指标。正则目标不自证真实因果分离/安全。 |
| 18122 | §1/3/A1，P：由topic总正确率转skill-conditioned局部测试，区分recall/argument评价与theorem应用/计算/策略失败；保留这一小范围评价盲区，不只新增榜单。每subskill仅1–4题、o4完整control不可得，rubric不能证明认知因果隔离或防污染，不能外推GPT-5全能力。 |
| 09303 | §3.2.1/4.1，C：LLM概念抽取、RRF、positive-only MSE校准服务patent-SDG弱标签/下游回归，未形成foundation训练或一般可靠性新增条件。已有“未知非负例”取舍不因包装成LF成为突破；去application消融反更好与full最优文字冲突保留，不照用。 |
| 09751 | §1/2.2/3/4.2，C：三角色meta-reward loop明确借自既有框架，新金融returns/Sharpe/drawdown/sentiment通道和领域收益，没有新增loop可靠性或防reward drift控制证据。不是以crypto名关闭；财务收益不采用。 |
| 2510.15898 | §3/7，C：原有BML/FSM deterministic dialogue被LLM生成/UI编辑，人审后export；只不在runtime即兴生成，不保证draft正确/全部patient安全。pilot为主观可用性，缺无AI对照/客观安全评价，未给新执行机制或实际失败边界。安全强宣称已核而不授保证，不能普通忽略该信号。 |
| 08820 | §3.2/3.3/6，维持P：相似/透明物体使仅text与depth路径失效，visual目标接口+失败trial再执行/外monitor；严格quantification/time控制不适合，gripper/装配限制保留，不授全chemistry安全或新反应发现。 |
| 08826 | §4.4/5，维持P：pointwise→generative/pairwise/reference与CoT对照；high reward variance仅作者探索proxy，不是hacking攻击试验或消除保证；高scale未来收益不采用。 |
| 08729 | §3.3/4.5/6，维持P：固定GPT-4.1 judge、θ=.70，length–score相关及finite zero-success/5代search限制；作者自承verbosity bias与policy drift，不能从相关性授judge因果偏差或全部模型攻击/防御保证。 |

所有安全/局部负面潜力实际保留，必要C的强安全反侧亦实际核；没有普通未读冒充外部终态。原九风险与84日期P有效题摘层继续冻复用，不由新日期hold要求全部威胁模型。当前新材料日期恢复和14源有限停止、正式六部分DAY/FINAL尚未完成。

## 6. 来源停止与旧身份当前差额

实际读作者[14源停止](SUP_SOURCES_20261012.md)，并独立处理本轮raw的日期/title/列表或必要正文；不是以request成功授覆盖。OpenAI RSS两条Sep11治理/MOU完整description无模型机制；Anthropic解码174发布身份切片Sep5到Sep15；Google Research九月1→2/2共13条，Sep11 cascades旧2024贡献及Nucleo科学目标关闭，DeepMind5/6有限跨窗及原具名日期有效复用；Meta pubs5/6与Blog2/3的主序跨窗，pin/乱序不混；Qwen配置60条及确定单篇正文已见§2/3；DeepSeek更新Sep29/22→Aug21、Moonshot Blog Sep16→Sep5→Aug22、ERNIE1→2/2 Sep12→Aug14均仅有限切片，不授全站零事件。

Hunyuan首查shell后官方API EN9/total9、ZH11/total11最早2026Feb3；ZAI第一页16unique含featured、第二页18且停止，release本轮仅止2025Sep30；MiMo Paper8有日期、Blog15无日期，实际runtime及正确async6159/8557的slice/useState More只翻显没有额外fetch；MiniMax EN12/CN13、派生page2仍同12、Agent3条2026及llms索引无2025恢复入口。以上历史缺段精确隔离，不能授2025Sep11零发布。MiMo两次错路径404保留，后续正确路径200，不将前者写成仍有普通不可执行页。

Seed本轮type1/type2 page0各18条/total94和45/next20/has_more，实际非pin序分别Oct21→Sep21→Sep1和Oct22→Aug20跨窗；pin Seedream4另核BJT Sep9。paper接口已经恢复，不能沿用旧空响应作为当前失败；只验这个有界切片，不授total全部或全历史无漏。无Weekly/全会议/全仓扫描；Qwen正文、arXiv必要core及旧PLAS实际触发保留而不扩仓。

arXiv四主题44/17/25/33=119命中、95unique、55旧/40新已机械交叉核；start0/max200、total=returned，submitted proxy只是发现。官方Sep11 CL/LG日列表各400，不能授first-public或catchup。55旧对原24+87精确身份/最后有效版本比较，仅7项版本不同，实际读其current title/comments/history：09199、09245、09284、09311、09360、09372、09438。09199页首明确withdrawn、comment低质量、history v2(2026Feb2)withdrawn，当前稿不采用/不评分/不入Books；原v1只为冻结日期P且无采用链，不能倒填撤回版本或重用它正面证明。其余6已读轻层没有撤回/勘误信号，未来conference标签不触发全会议查；不以current AB替exact-v1或为版本变化默认全core。新增09195的独立撤回隔离见§4。新16P和原84P仅日期未证，普通核心歧义已清楚，不再据此扩Evidence。

## 7. DAY：六部分实际裁决

复核者：Cicero，非作者Meitner。**结论：研究语义DAY通过；完成态FINAL仍待作者状态与行政差额实际检查。** 实际回读本日README全部六部分、SCREEN/NCORE/Source note/单篇Evidence，并复用本note各实际读层，不无差别重读相同附件。

- §1：新唯一正式家族Qwen3-Next 1，2+2+1=5标准完成、仅报告、Books新增0；119/95/55/40与16P/23C/1当前撤回信号隔离、13必要局部数字一致。原111=84P/27C另46titleC及原0正式冻结，100日期潜力不是100已审候选；旧7版本轻核不是7新家族。
- §2：14 Daily行主题和停止自包含，实际来源范围见§6；4机构历史缺段与arXiv public-date隔离，不称全Coverage通过或零事件。Seed已恢复有限接口不能再称空失败；当前列表total/pin/乱序限制明确。按需触发未被无候选取消。
- §3：全部拟入选Qwen1日期/准入实际通过；新40完整v1题摘/current及全部13必要局部完成，16具体局部/负面潜力保留；23C不是标题/医学/benchmark一刀切。09195及旧09199当前撤回信号不用，原层无采用链。日期未知P不评分、不进入确定候选，不以当前AB替v1。
- §4：Qwen必要机制、对照可比性与部署反侧及Ch22/21/48具体正文差额已经§3实际审，recipe不构新受控长期条件，仅报告理由成立，不授主题相似已有覆盖；Books0无真实共享gap/待写。旧PLAS、energy、TORSO/root有效层及连续三旧段保持，旧第三段的0候选描述须由新增过渡句明确仅指原层，不否定补窗Qwen1。
- §5：研究ordinary0，必要日期材料及Hunyuan/ZAI/MiMo/MiniMax历史缺段按精确替代物/重开点终态隔离；未知Qwen受控消融不阻塞已收窄版本事实，也不授宣传或生产保证。旧Vault保留原hold，新Sep11不扩小时请求。
- §6：非作者身份、首批/全拟入选/全部安全反侧、新40和旧分层有效样本及未检查范围应同步本DAY；下载、机器V3或格式不代语义验收。待作者将status/§1/5/6改为本实际DAY结果、保留旧§4加窄过渡句并跑完成态检查，再由本人实际FINAL差额确认；此前不授最终完成。

本次只写本note，没有报告/Books/State/index/scripts/raw写入，不stage/commit/push。首批、单篇与DAY读层可有效复用；最后行政差额不触发整日再研究。

## 8. FINAL：完成态差额通过

本人实际回读完成态metadata与§1/5/6：status完成、复核通过，引用真实本note§2–7单篇/来源/DAY，ordinary研究0、Books0及100日期潜力隔离没有多授。§5明确终态保留项、不可用于正面证据/Books/0事件/无遗漏、精确替代物到达定点重开。初次完成态V3因缺“终态保留项”明确标签实际失败；作者只修该标签后本人重跑**exit0通过**，不把先前失败写成已过。冻结旧第三段后窄过渡已实际读到，旧0只指原层而不否定新增Qwen1。

**FINAL通过。** 本人实际核原时刻窗口exact、原空候选冻结、连续旧§4三段为运行前档逐字prefix；完整tracked diff已读，除补充自然日内容与完成态行政同步，没有改旧候选日期/评分/有效研究。限定README+本note的unstaged/cached diffcheck均通过；tracked README **41+/31-**，本日cached空；本note未跟踪新增，不在numstat分母内，不授整个dirty工作树检查通过。

实际机器范围为7份live README/SUP Markdown、24本地引用、0anchor均可达；另baseline副本5引用按原README目录解析也通过，合计8份/29引用，不把冻结档案相对基址当坏live链接。108份本轮SUP request/raw的SHA/bytes均匹配：104×200、2×400、2×404；400为两个public-date列表，404为已保留初次错路径，正确async后续200。未补造timeout，未改旧失败原件。这些检查只支持结构/一致性/范围，不代研究语义或源历史完备。

准确本日摘要：补Sep11完整BJT自然日；四主题119→95unique、55旧身份、新40 exact-v1完整题摘/current，13必要core，**16P/23C/1当前撤回信号隔离**；7旧changedversion轻核另隔离09199v2撤回，无采用链、不倒填v1。正式Qwen3-Next **1家族/5分/标准完成/仅报告/Books新写0**；旧111=84P/27C另46titleC及原0正式冻结，100日期潜力与4机构历史缺段终态隔离，非全面Coverage/Evidence或安全/性能保证。没有真实共享Books gap被跳过。

作者最后只回填FINAL指向与§1/5/6真实完成裁决，由本人窄行政回读后双方fresh Sep14；root维护State计数，无需第三全raw复核。本note之外无本人写入，不stage/commit/push、不换模型。

最后行政回读实际完成：metadata/§1/5/6已准确同步DAY§7与FINAL§8，数字、冻结和隔离边界不变，无新增采用命题。本人正确runtime重跑V3 exit0、限定unstaged/cached diffcheck均通过；README仍41+/31-、cached空，引用无新链接仍live7/24/0anchor（含baseline8/29）。双方直接fresh Sep14，不继承本日队列；root只维护计数，无需第三原件审。
