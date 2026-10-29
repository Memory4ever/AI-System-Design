# 第九包：合成依赖结构、联邦双权重与三项具体覆盖

仅整体PRE提案，尚未SAVE。Books适用上下文/ROADMAP与2025路由已重读；Ch27/28/35/36/37交接及以下actual完整目标/直接邻接已实际读。必要首读属Cicero R14/R17/R35/R38/R49，不重复第一Methods；支持与反侧足停，未核代码/复现。两I独立窄位，不全章锁；三NC不写marker/注。

## 11944 TopoAlign / 2+1+2=5 / TRAIN-DATA Ch27

消费R14 exact-v1 §3.1–3.2/4/5表1必要。当前Ch27编译式路线把ground truth置于NL生成前，完整共享ontology限制段后直接转长文QA骨架；它未承担**从现有程序的函数依赖提取结构，再生成入口函数这一种监督制备顺序**。邻近课程图是从解答拆子题/调难度，并非函数级AST约束。唯一插位：完整`这条路线也产生新的上限...防止measurement channel被优化。`（当前实际分成多行的整段）之后、完整`没有合适长文语料时，也可先固定短的question–answer–evidence骨架...`之前。完整上方编译路线/上下段与后QA段已读，不改旧source-family。

正文：

结构化监督也可以从已有程序反向提取，而不先自由生成整份解答：先按AST识别函数依赖，为局部函数产生描述，再按依赖顺序组织上下文、生成入口函数，使生成器在组合阶段看到已声明的局部接口。[受限结构对齐分支](https://arxiv.org/html/2510.11944v1#S3)把这类代码与数学材料混合用于训练，却不使函数摘要成为完整行为specification，类型检查也不能证明译出的形式命题等价于原自然语言命题。原程序/AST、依赖顺序、描述器、生成器、类型检查与语义审校及mix比例应分别版本化，保存检查前人口和失败路径；同样本数不等同token量或总制备预算，结构对齐与数据mix同时改变也不能独占收益归因。有限迁移任务仍有退步，不据此批准一般数学正确性。AST提取、摘要/生成、检查重试、全部训练和独立语义回归均付费；局部接口、命题保义或净质量失配时，保留原程序/人工spec、可信配对及原mixture，不由可编译或通过类型检查签发训练标签与最终答案真值。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-11944 -->`

本人末注：

- `SF-2025-ARXIV-2510-11944` — Herschel，Daily2025-10-16补Oct15；消费Cicero R14 exact-v1 §3.1–3.2/4/5表1首必要，2+1+2=5，函数AST依赖/局部描述→入口生成的制备顺序差额深入。保typecheck非原命题等价、Herald部分BEq反退、mix/对齐共变与全部token/制备训练费；未第二Methods/代码/复现，不采通用形式正确。整体PRE/真实SAVE/完整自读/solePOST只本日canonical实际层。

## 12132 FedHUG / 2+2+2=6 / TRAIN-DISTRIBUTED-TRAINING Ch36

消费R49 Methodology/Experiments首次必要；只采两级权重producer/消费者不同，不采Eq10/12完整recipe或vMF精确/有界证书。Ch27 data控制面拥有样本weight，Ch36 actual联邦节拥有参与者update聚合；本项长期差额是**同一协议内client聚合和client内batch-loss的两个反馈位置及不同统计历史**，唯一Ch36完整解释，Ch27不另复制。当前完整SpectralFed段只update谱/rank权重，下一完整层次聚合段是client–edge分组/两级model平均，均不承担局部loss与server聚合两种作用位置。唯一插位完整SpectralFed段/inline marker之后、完整`层次聚合还应检查“哪些client先组成同一edge组”...`前；上方GradsSharding两段和下方层次聚合完整段/独立marker已读。

正文：

同一轮协议里的权重还可能作用在两个不同位置：服务端按各client原始与增强观测的输出相似度提议聚合比例，客户端另以当前局部与历史全局表示统计的差异重权batch loss。[受限无标签联邦分支](https://arxiv.org/html/2510.12132v1)因此同时改变“哪些局部更新更被采用”与“各局部更新怎样产生”，不能把两处反馈合称一次更可信的平均，或由增强一致认定语义正确、由分布差异认定稀有样本必有益。应分别保存两权重producer、表示checkpoint、增强/统计人口、历史时点、实际loss归约和参与者，按各端及全局目标分别消融；表示更新会使旧统计改变含义，未闭的方向统计/指数归约不补成有界权重recipe。联邦阶段无标签也不抹去先前有标签预训练，上传统计/模型更不自带隐私保证。预训练、增强、统计拟合/历史驻留、全模型通信、本地训练与独立各端回归均付费，有限任务的相关系数反退不当显著性证明。统计、稀有支持或净质量失配时，保留普通本地目标、声明清楚的固定平均和独立held-out验收，不由相似度或差异proxy批准无偏聚合、隐私和任意域泛化。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12132 -->`

本人末注：

- `SF-2025-ARXIV-2510-12132` — Herschel，Daily2025-10-16补Oct15；消费Cicero R49 exact-v1 Methodology/Experiments首必要，2+2+2=6，仅server SSM聚合与local/history vMF batch-loss的双作用位置/统计时钟差额深入。保Eq10/12未闭、labeled预训/unlabeled FL、相关系数非p-value及逐任务反退/全费；不授精确recipe/无偏或privacy。未第二Methods/代码/复现；整体PRE/SAVE/fullselfread/solePOST只本日canonical实际层。

## 三项具体NC提案 / 唯一TRAIN-DATA Ch27

| 身份/分数/必要层 | 本次采用与实际完整覆盖 |
| --- | --- |
| 12225 HoneyBee，2+1+2=5，R17 §3.3/4/表4/5.3 | 只image、question、CoT扩展的计量轴/输入与条件回答支持，保五下游hill-climbing选checkpoint与独立unseen人口、MathVista反退及40.1→41.4非绝对3.3pp。actual Ch27开头完整rawsample/codec/frame/action单位段、同prompt多response完整两段SF2606-00544，分别拆输入覆盖与条件输出模式，并保存producer/selector、token/全部造数/训练预算，实际承担本次轴/资格分责；类型标注完整段另拒caption更长即监督更全。不采新的CoT质量或规模因果，拟NC。 |
| 11897 annotator loops，2+1+2=5，R35 §3.2–3.3/4.1–4.2/6 | 只证据优先/后审权限与标签支持域、annotator人口混杂；7internal/40external及24survey、pay/experience/年龄/自审并变不授反馈单因果。actual Ch27 SF2603-25269完整两段允许裁决者另答并拒agreement即truth，紧后SAM3D完整段明确择优/拒绝不能找回支持域外候选、专业构造与择优不同权限，具体承担本次review不可改问题/加passage的边界；全读/返工/QA费保留，不按内部更优加结论，拟NC。 |
| 11842 Replay，2+1+2=5，R38 §3–5/A.1末/B/C | 只固定token下replay/unique支持与保留能力分责，保Task20排除、r的正文反向措辞、GSM8K因遗忘移出主均值及15%任务特定回放恢复，拒5–10%普遍保能力。actual Ch27 SF2604-28075完整段共同冻结tokenizer/unique内容/epoch与独立能力、全费，SF2604-27932完整段拆quota与跨epoch刷新、重复尾部不造新证据、原任务/长尾独立回归；已有重复机制段保新unique条件边界。实际承担本次曝光/保留资格，不将静态/动态算法冒为该论文算法，拟NC。 |

三NC都保P/原分数及完整必要边界，不减池，不声称全部论文细节已有覆盖；若发现新差额仅重该项。请sole reader整体审两完整正文/marker/本人注及三具体NC，未SAVE/不预POST。
