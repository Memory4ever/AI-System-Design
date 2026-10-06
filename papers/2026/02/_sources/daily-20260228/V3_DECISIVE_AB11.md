# AB11 六个含糊事实：一次决定性 core（待非作者准入校准）

仅本日固定窗口。原 exact-v1 完整题摘与 current Comments 已实际读，取得记录见 `V3_FETCH_AB11_ONCE.json`（2026-10-05T21:54:45～48Z）。决定性方法、对应控制与直接反侧如下；HTML 200 不代表全文已读，不运行 artifact、不比较窗外 revision。五项拟窄 IN5，23220 因已确认窗外同家族首次公开不收；未取得非作者准入／PRE／Books 写入授权，35 safe 不增加。

## 23153 Fase3D：拟 2+1+2=5

[v1](https://arxiv.org/html/2602.23153v1) blocks17–49/64–71 实际读。重 encoder 并不是保留 3D 全局上下文的唯一接口：几何 superpoint pooling 后，按四条坐标 space-filling curve 排序，再沿 token 轴做 window FFT/DCT 混频、逆排序平均与残差，配合稀疏 window-voting 图和 token merging。这个序列构造改变 **encoder 成本与序列邻接偏置的选择**，不是单凭 3D 指标或 Fourier 名称准入。Table3 同 optimization/data、声明逐因子控制下 superpoint 与 FFT 各有局部增益，full pretraining 行另计；Table4 视觉支路 Fourier residual 优于同时给语言支路，保留结构放置的反侧。

特别分开两种轴：44 的 GFM 沿每个 token 的 channel D 做 FFT，不能称为跨 token 全局 context 交互；25–30 才沿序列做混频。摘要的 permutation invariance 不当作任意输入／排序扰动严格证明：坐标排序、tie-breaking、SFC 邻接与图构造仍有条件；低频 gate 的 learnable/parameter-free 表述相冲突，37 的 kNN 与35避免 kNN 也不能混署一个已核实现。OT μ/ν 的归一化、entropy 符号和 Pᵀ pooling 是否中心坐标平均未审，不将所写 pseudocode 当正确性认证。准入所需真实序列接口与局部消融已足，停止初筛；后续只必要成本／边界与 actual Ch23 对照。

原 Submitted 2026-02-26T16:16:02Z；same-ID registered 2026-02-27T03:03:45Z。官方公告政策与该上界仅支持 arXiv 本窗半开区间 09:00～11:03:46+08，不把 Submitted 当公开。CVPR2026 身份无具体旧首公开信号；3/28 v2 窗外且没有必要纠错提示，不默认 diff。

### 23153 必要审阅与 Books 处置（2026-10-06）

非原 packet 作者 `feb28_ch23_finish` 实际独读 exact-v1 blocks17–73；79–86只定点 layer/curve/token 数边界，初次返回截断必要方法已重新取齐。不遍历全部 supplementary/artifact，不展开revision或整OT证明。沿用上述有效日期/完整题摘，保持2+1+2=5，具体owner差额聚焦深入。

几何superpoint内MLP/坐标feature平均→四SFC排序→token轴window混频、inverse/平均/residual→稀疏图merging；不是逐token channel GFM的跨token全局context。坐标curve/tie-breaking有条件，不授严格任意排列不变。25/66 parameter-free与29 learnable G冲突、35 window-voting避免kNN与37 kNN口径冲突保持隔离。μ normalization未定、ν=1/T时PᵀC不是常规归一化center平均；entropy符号未指定，不采用OT可执行配方或认证几何保真。

ScanNet v2室内1201train/312val，50k points→256token、最低128modes；Qwen2.5-3B float16、rank/α768首8层、B8、AdamW/wd.1、约100k iteration、七天up to4作者称custom A10064GB，task约30k；未代补revision承诺细节或总时延。Table3同optimization/data声明逐因子：point76.04、pool79.70、FFT82.97、both86.91 CIDEr，pretraining90.11另计；Table4视觉FFT86.91vs两路83.64，非各branch通用增益。Table1/2各项非全优：SQA3D/细纹理与空间relation失败，w/o external segmentation caption可降；clutter非欧氏远关系为直接限制。79–86层数/curve/token更多也非全metric单调。encoding/tokenization参数/FLOPs只前端口径，不能推完整LLM时间/常量内存；排序、graph/SVD、merging、LoRA、pretrain/task训练及external proposals均计费。

Books owner `MM-REP` Ch23 native3D表示：原sidecar/native几何identity与多视图state可维护，但未包含几何排序序列→token轴频谱混合的轻front-end选择。窄差额已融source-family23153单段，encoder/更多tokens/proposals共存，channel-axis与未核配方近文隔离。独立PRE完成；作者实际正文/完整邻接/自身末注顺读；root 非写入者已实际独读新增正文、完整邻接与自身末注，POST通过，五项窄锁释放，非日级 Gate。

## 23166 AgentVista：拟 2+1+2=5

2026-10-06 后续必要原证/actual owner终态：fresh非原packet作者实际必要blocks33–75，46–47实验配置及48–75权限/BoN控制已核，轻改prompt/固定30turn非全API预算；judge标签和selection不truth。采用2+1+2=5，具体差额深入后窄融PLATFORM-EVALUATION-SYSTEM/Ch66正文273/275，完整267–280，末注5697；final_audit必要原源/actual owner非写入者独核通过，root实际正文/完整邻接/自身末注POST通过，已同步并释放窄锁。精确v1身份/家族日期沿用本日原字段和政策下界、同ID注册秒上界，只支持09:00～11:04:05+08半开范围，不授注册首公开；未核实现/复现或全证明，非日级。

[v1](https://arxiv.org/html/2602.23166v1) blocks48–75 实际读。仅新增 hard benchmark／27.27% headline 不够；决定性局部证据是 **同评价与 inference hyperparameters 的工具权限消融，对模型不同的失效／增益条件**：Gemini search-only 接近 full，而 Claude vision-only 接近 full、search-only 退步。于是不能用总 tool call 数或全局难度替代模型×工具权限的验收；图像检查与外检索的采用顺序须按具体模型测，不视为所有模型同一瓶颈。

64 prompts 随可用工具轻度适配，工具权限之外并非所有文本完全相同；55 多图与单图来自不同实例，额外视角提供互补证据的解释是作者假说，不能作 multi-image 因果优势。70 Gemini-3-Flash 自动错因标签不认证真实根因。72–75 BoN vs Pass 差暴露 selector 与 proposal 支持的差别，但 Random1 的抽样起伏不是严格下界，Pass 是受测池 oracle 上界而非可交付质量；费用与调用分母后续必要核。该受限经验反侧可准入，不授全生产 grounding／独立可靠性结论。下一 actual Ch66/Ch76 最小 owner 比较，独立可选 Existing。

Submitted 2026-02-26T16:30:46Z／registered 2026-02-27T03:04:04Z；公告下界与 metadata 上界给 09:00～11:04:05+08。current v2 3/2 窗外，未见撤回／重要纠错说明，不默认比较。

## 23184 MTRAG-UN：拟 2+1+2=5

2026-10-06 后续必要审阅与actual owner：当前日报执行者非本packet作者，实际读取原v1 blocks18–24/29–49，独立核对本项采用的必要方法、评价与反侧；原日期精确v1/同ID/政策依据未变复用。实际Ch76正文569–576在sufficiency之后明确“证据尚未找到”与“意图未定/无法确定答案”不同，intent含糊须澄清而非query expansion，自身population/cost/gold及保守abstain边界完整，故**具体已有覆盖 AGENT-RAG / No Change**，不是benchmark新即写书。保468可答/部分可答检索与666总任务分母、Reference最多10gold对RAG5的不等context控制、80样本underspec judge局部效度；人造/stitched+LLM后人改reference非全部真实意图金标，IDK进步非澄清能力证明。2+1+2=5标准完成，未核实现/复现、非日级验收。

[v1](https://arxiv.org/html/2602.23184v1) blocks10–49 实际读。成熟 query rewrite 或新增领域样本本身不准入；实际新增 **underspecified intention 与 unanswerable evidence 分开标注／评价，且 oracle-reference 与 retrieved 条件分开后，模型仍会按未经确认的意图作答**。已有 IDK 进步不能推出会先澄清；37 的 underspecified metric 只用于该子集，不与其他答对／faithful 指标混算，47 的局部负侧改变多轮 RAG 是否澄清及按哪一分母验收的选择。Table3 RW 对 non-standalone 较大改善，控制说明最后一轮与历史依赖不同，但不是所有对话中 rewrite 必好。

人工与 stitched underspecified 构造、query expansion、LLM reference 后人改都形成 oracle 权限；468 answerable/partial 的 retrieval 分母与666总任务不能混算。Reference 最多10 gold passages，RAG top5，不是纯 retrieval 内容质量的等 context 对照；37 新 judge 的80样本96.2%是局部效度，不授全部多域意图真值。新 Banking/Telco 页长与同构／link 对困难的归因仅观察，不授独立机制。必要准入支持与反侧足，停止；后续实际 Ch76/Ch66 现有澄清／评价论点可判 Existing，不因新 benchmark 名制造 gap。

Submitted 2026-02-26T16:41:17Z／registered 2026-02-27T03:04:32Z，arXiv 区间09:00～11:04:33+08；current 仍v1，未见纠错撤回。

## 23201 Generalized Neural Memory：拟 2+1+2=5

2026-10-06 后续必要证据/actual owner终态：本人实际20–74/86–103；final_audit后续66–68/40/72/103独核，write/read bank、positive/control probes、随机overwrite/retention/test-ood择优反侧。原v1身份及first-public政策下界/same-ID注册秒上界复用未变有效依据，不把Submitted/注册直接当首公开；当前作者非原packet作者实际读必要owner并作窄差额，score2+1+2=5。实际正文670/672/完整656–680/末注1333已融入，作者完整近邻/自身末注已顺读，root非写入者actual POST通过；未核实现/复现，不授全附件或日级完成。

[v1](https://arxiv.org/html/2602.23201v1) blocks20–43/65–74/86–103 实际读。不是自然语言 RAG filter 的重命名：Learning pass 同时输入 document 与可变 instruction，向每层 embedding bank 写256新 memory、随机覆盖现有7098 tokens；训练在当前与历史 probes 上反传学习与读取，而 test 只更新 memory。**90 只允许 inference-step gradient 的直接消融丢失 selectivity 与 format 增益**，改变“仅教 query-time attention”还是“连 write-time update 一起训练”的选择。更新接口与读取接口的区别有具体控制，不能只用 abstract 的 lifelong／clinical 宣称。

87 新指令组合局部实验、94 target/distractor mean-direction alignment 只支持相应合成任务，100 early-layer identity/hypothesis 不当作通用 memory causal 机理。97 swap 整层含函数／分布改变，不认证只删除某一指令变量。72 baseline prompt 在 test-ood 上择优后训练，不能把该分割称严格 untouched 外推。103 随机 overwrite 约20steps后 retention 指数退、未训练有序冲突且冲突任务表现差，不保终身记忆、不保隐私逐条删除或安全领域部署。医疗仅例示通用 memory control，不属本次 AI for Science 应用纳入。next actual AGENT-MEMORY Ch77 最小比较；本条无未经授权书稿写入。

Submitted 2026-02-26T16:50:52Z／registered 2026-02-27T03:04:58Z，arXiv 区间09:00～11:04:59+08；v2 3/3 窗外无重要说明，不 default diff。

## 23205 EmbodMocap：拟 2+1+2=5，日期上界已定点恢复

[v1](https://arxiv.org/html/2602.23205v1) blocks17–46/58–68/102–103 实际读。双手机／成熟 COLMAP、SLAM、human reconstruction 组件组合本身不够。实际窄贡献为 **统一 metric world frame 中，单移动视角校准保留 facing-depth ambiguity，而 dual-view tracking约束与3Djoint项在直接消融／单视图对照中改变误差**；会影响 embodied training data 是否可以只用 monocular reprojection 同时认证全局位姿和深度。Table2 去track或kp3d的负侧与Table3单/双视图控制提供必要准入信号，不靠“affordable” headline。

固定 scene 先单手机 LiDAR/IMU建metric mesh；两流 laser-dot 人工同步与 background SIFT初始化，joint offset优化不是只凭深度自动获无偏世界真值。Table3 仅1participant/5 sequences/9420frames，chunk100/500/1000并非独立人物重复；光学GT拟合/接触同步、各方法预算及完整采集费尚未足以签一般精度。103 >约5m缺depth、动态主体场景毁SLAM、brightlighting毁COLMAP是直接边界；不得将仿真／机器人 downstream组合泛化foundation能力。下一实际 Ch26 的数据坐标／retarget owner对照，不扩大无关全部技能附录。

exact abs Submitted 2026-02-26T16:53:41Z 已读，原发现 same-ID 日期字段为空；只定点请求 DOI metadata（`V3_FETCH_AB11_DATE_BOUND.json`），实际返回同title/DOI `registered=2026-02-27T03:05:04.000Z`、v1 Submitted一致，故公告下界与此上界支持 arXiv 09:00～11:05:05+08 半开区间。不把 Available 月精度或 Updated 替代首公开。current 4/2v2无纠错说明，版本号本身不触发比较。

### 23205 必要审阅与 actual owner（2026-10-06）

后续：root非写入者实际读Ch26完整598–616及自身末注，actual POST通过；本项证据/实际整合终态，非日级Gate。

feb28_vla_last7非原packet作者实际核精确v1 §3–4/7 blocks23–68/103。scene RGB-D/IMU/SAI/PromptDA/TSDF metric anchor，laser-dot消失人工同步、backgroundSIFT/COLMAP初始offset、yaw-only优化tracking/chamfer/BA，fixedcamera/scenemesh后weighted triangulation/SMPLify；初始Eq1含scale但后续offset只yaw/translation，不发布原式为已核执行配方，camera外参/triangulation记号未核代码。single-view facingdepth误差是具体新增观测约束，不仅two-camera组件组合。Table2去track/3Djoint反侧成立，full jitter .0128略差于去3Djoint .0126/去chamfer .0131各不同指标不全优；SAM2/ViTPose/refineddepth proxy复用估计器。Vicon only1participant/5seq/9420frames，Mosh拟合/footcontact同步与100/500/1000chunk非独立人口，预算不同不能授通用精度。sensor >~5m、动态场景/强光注册失败与人工扫描/同步费用必要，未读无关downstream/skills附录、未授实时或robot action/safety。

2+1+2=5保留，Ch26数据/retarget虽有provenance与metricframe，但未承载单移动view reprojection不认证depth及双流tracking/3Djoint消费分工；具体gap深入后窄融数据provenance段，旧光学mocap/目标本体示教回退近文。原v1 Submitted16:53:41Z、same-ID精确registered03:05:04Z恢复与本窗09:00～11:05:05+08/current/家族未变事实沿用本日有效证据；不比较v2。实际正文/完整邻接/自身末注顺读，root非写入者actual POST通过，本项终态，不授日级Gate。

## 23220 STELLAR：窗外同家族事件，不收／不评分／不 Books

原v1题摘与 Comments明确SC25已出版，Related DOI [ACM 正式记录](https://dl.acm.org/doi/10.1145/3712285.3759887) 实际定点核到 **Published: 15 November 2025**，标题与作者同身份。2026-02-26 arXiv上传不改变首次公开所属；未见本窗实质新增／纠错事件信号，所以本窗排除，未声称其在11月已完成审阅。只读原blocks4–13确认身份／摘要一致后停止，不再为本窗深审全部 tuning/proof/owner，也不据其 scientific storage workload 一刀切成 science。五attempt成熟组合是否有学术经验贡献无需本窗再裁决。当前原v1是作者上传，不把索引登记当新研究公开。

## 停止与后续

五项作者拟 IN5 的准入仍待非作者校准；23205时间上界已恢复，五项arXiv区间成立不替代具体家族首公开检查。23220已确认旧事件，raw排除不增加候选。随后仅五项的必要实验条件／实际owner，以及已校准AB12/13具名潜力；不循环AB1～13初筛、不扩613库存或228标题slice为逐项关闭队列。所有未审PRE、必要写入与POST仍普通可执行工作，不授本日完成。

ACM日期证据备注：2026-10-06本轮网络检索工具实际从上述 primary正式记录恢复title、authors和Publication History。本地同URL抓取403保在AB11_DATE_BOUND，不把403当没有出版或用搜索相对月数推精确日期。

2026-10-06 root非作者一次准入原段独核：23153 17/24/29/37/46/49/64–71（68之后返回截短）；23166 33/36/41/45/62–71；23184 10/18–20/29/35–38/46–49；23201 20/29/32/35/40/42/65/72/87/89/90/94/97/103；23205 25/27/29/31/35/39/43/45/62/63/65/67/68/103。五项窄IN5准入通过，非全部附件审阅，必要缺段/评价条件、日期family事实与actual owner仍需落实，不从坐标授完整证明/Books。
