# 2026-02-03 补充：首批准入、必要证据与 Owner PRE

作者：supplement_20260203。补充窗口：2026-02-02 ～ 2026-02-02（用户授权仅补遗漏，保留原窗口、候选与有效审阅）。检查时间：2026-10-08T12:25:27+08:00。以下保留首包作者提案，root后续实核裁决见末节；本轮DAY已实际通过，普通待办0。

## SPARKLING — 拟准入 2+2+3=7

[官方 Seed 论文入口](https://seed.bytedance.com/en/public_papers) 的 API 查询见 [native-first](supplement-native-first-20261008.json)：type1/year2026/order_desc=false 第0页20项，next=20、total=82、has_more=true。仅浏览 Jan31 A²D→Feb02 SPARKLING→Feb04 VTok→Feb05 BABE 边界即停，不把82项变题摘队列。SPARKLING 的 PublishDate=1769961600000，即官方 Feb02 date-only；UpdateTime 是后续目录修改，不能换作首次事件。采用官方论文目录发布事件，不将 [v1 Submitted](https://arxiv.org/abs/2602.02472v1) 当公开日；论文精确版本仅用于机制证据。旧§5因原09点窗口隔离它，此次按授权自然日定点重开，旧内容不删除。

完整题摘已读，准入链：中途宽度增长既要保持前向信号，又需让新增容量离开旧轨道 → 原稿提供 RMS-preserving mapping、仅新参数 optimizer-state reset 与非对称 rewarm，并揭示复制权重/状态的 symmetry lock → 需修正“function-preserving mapping 已足以稳定增长”的训练状态判断。D=2 是重要条件与替代方案；R=2 涉及模型shape/optimizer/schedule恢复边界；T=3 是可复用状态迁移判断，不把单个成本数字计分。

必要 [exact-v1 HTML](https://arxiv.org/html/2602.02472v1) 已读 §3、§4、§5、§7.1–7.3 与 §8.1–8.2。证据原件：[core](supplement-core-first-20261008.json)、[evaluation](supplement-spark_eval-20261008.json)、[setup](supplement-spark_setup-20261008.json)。

- §3.3 Figure1 的 matched initialization 比较表明，扩容边界瞬时 loss 更小不意味着后续收敛更好；RMS-scaled late loss 较好，但不是全分布不变。方差推导依赖原坐标独立、centered、同方差等假设；双边复制需要协方差项。§7.2 c>1 式还隐含均匀复制，不能推广任意不均匀 mapping，本次不采用其通用闭式保证。
- §4.1–4.2 的确定性复制块在相同梯度与相同状态下同轨；多项式 Gram update 的交换对称性不能自动打破复制结构。保留旧状态、只清新块状态是有边界的干预；不是宣称随机训练中所有 optimizer 必然锁死。Figure2 固定 RMS scaling 后比较 Drop/Copy/Asymmetric Reset；Figure3 再比较 rewarm，能区分两条件，不能把三者混成一个 benchmark。
- §3.3/§8：OLMoE 风格模型，约0.45B active/2.56B total baseline、200B训练tokens，100B处扩张，inner/hidden/joint三轴；24层、64 experts/top8，固定head维度与QKV头数；64×A10080GB、seq4096、globalbatch768/microbatch3。评价是作者实验、未复现；训练precision与重复seed未披露，记 Not Disclosed。
- Table1 下游平均改善但 pretraining loss 仍劣于 target-width from-scratch，不可写成全面支配；各from-scratch目标规模使用不同LR配方，不是所有对照完全相同。Table2 的20–35%为6ND近似FLOPs减少，wall-clock是该集群的报告值，不是生产总账；扩容搬运/额外调参未完整分账。µP兼容和宽深共同扩张是§6未决，不签发免调参/任意形状保证。

拟处置：深入完成；Books **已有覆盖**。唯一 owner `TRAIN-PRETRAINING`，当前 [Ch28](../../../../../books/part-04-training-system/28-pretraining.md) §一次 training step 的状态流，实际正文 L249–264 已有 shape-aware mapping→activation-scale→新optimizer state差异→asymmetric rewarm→canary/rollback，并写明旧方案/代价与“函数近似不变不证明trajectory连续”。章末 L1697 已有SPARKLING Experimental引用。采用的双条件已经被正文承担；不因新增日期级候选制造书稿diff。任何额外数学或性能命题均未采用，No Change提案待root PRE实核。

## 代表性贡献前关闭提案

- [GLM-OCR官方Research](https://www.zhipuai.cn/zh/research)明示 Feb02；Feb03 API release 另事件。初始 README [8900d23f](https://github.com/zai-org/GLM-OCR/blob/8900d23f229308c9a5d4ef795958acefd96bcaec/README.md) 已完整读并存 [原件](supplement-glmocr-original-20261008.md)。CogViT/connector/0.5B、MTP+full-task RL 与 PP-DocLayout双阶段是披露的组件组合，未给出相对旧设计的机制差额/成立条件；94.62单榜与0.9B本身不够。本次拟贡献前关闭、不评分，不以未开源或缺大benchmark关闭，也不沿用旧09点日期受阻理由。若root识别可改变判断的具体新执行机制，则仅重开该命题。
- [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)：首包以parallel worktree/skills/审批产品组合判断关闭整个家族的提案**撤销**。它只说明这些产品组件没有新命题，不能推翻[02-02已冻结SF-2026-OPENAI-CODEX-APP-20260202](../../02/README.md)有效候选。现已定点实读该日原行与§4：6分、深入完成、Ch66两段实际整合和root写后通过；采用的是初始任务计数与持续随机continuation外部输入预算不等价，不是产品组件或7M tokens因果收益。同事件去重复用，不重列、不重评分、不新增Books写入；March4更新/当前披露精确版本边界保持。
- [Snowflake partnership](https://openai.com/index/snowflake-partnership/)：身份、core采用命题及原有效root负侧校准不变，复用§4既有“接入与合作路线，不是新系统机制”的贡献前关闭。
- [Anthropic Allen/HHMI合作](https://www.anthropic.com/news/anthropic-partners-with-allen-institute-and-howard-hughes-medical-institute)：官方Feb02，title/core是life-sciences合作，按ROADMAP AI for Science暂缓；不是Agent关键词即可绕过范围。[SR-Scientist](https://huggingface.co/blog/yoshitomo-matsubara/sr-scientist-iclr2026)科学方程发现同样范围前关闭，索引日不作为论文公开日。

## 日期保留提案（不是候选）

本轮有界主题搜索发现 [Embedding Perturbation 2602.02427v1](https://arxiv.org/abs/2602.02427v1) 与 [GapEval 2602.02140v1](https://arxiv.org/abs/2602.02140v1)，完整v1题摘已读；前者由前缀embedding扰动敏感度提出过程级不确定度sensor，后者对双方向同问题评价揭示理解/生成统一不等于知识共享。这两项具具体评价反证潜力，但只有Submitted Feb02，官方目标日list未恢复；不评分、不全文队列、不采用。需要首次正文公开日期的官方批次或作者可核原始日期记录，恢复时仅重开所证实项/真实归属日。原§5已有安全/评价/机制日期保留不改判、不重复材料请求。

## 访问与停止

RSS native 403、web XML不支持；保留原有效 stage4_0 日期边界，另读当前单篇原页而不把失败算零。arXiv exact-day CL/DC列表返回失败，没有catchup；Submitted搜索只发现，不授公开日。无90天恢复、无全月/全类逐项队列。写作风格检索工具未提供，沿项目六部分和用户明确偏好，不声称获得外部风格样本。

## root 非作者准入、Source 与 Owner PRE（已通过）

root实际重读官方Seed日期条目、完整v1题摘，以及exact-v1 §3.3/4.1–4.3/5 Tables1–2、§7.2–7.3/8.1–8.2；准入/7分/深入完成通过，采用仅双条件，不采用c>1任意复制、全面支配或总成本保证。root实际读Ch28 L249–278及源注，已有覆盖/No Change PRE通过，无需写锁。GLM-OCR初README核心独核，组件名/MTP+RL宣称/双阶段与单榜不建立新机制差额，关闭通过；不是以缺实验即拒收。Snowflake有效负側、暂缓Science范围关闭保持。Codex app改为有效同家族去重，不推翻原审阅（详上）。这是root发回的实核范围记录，不是作者自授。

root随后完整DAY实际通过：独读全部README增量diff、六部分、14来源逐条与停止/限制、唯一新增及Books已有覆盖、两日期请求、Codex有效旧证据去重、原§5/本轮状态区分；实读scan0/1日期边界和两项新潜在完整题摘，并fresh打开02427v1/02140v1，不将Submitted授公开日。此前已通过的必要v1/GLM core/Owner结果分批复用，不是第二人全量旧附件深读。Codex全家族负側误判已纠正，本日无Books新写入，普通待办0；历史/日期保留不授全Coverage/Evidence或无遗漏。仅同步该事实并结束本日，不接其他日期。

## 作者本地检查

V3一致性与本日限定git diff --check通过，原窗口保持，原§4连续前缀逐字保留。首次校验失败是第二来源/候选表表头被当数据、候选日期夹带说明和§4标题不匹配，已收为单候选表+逐源补充说明，纯日期不补造时刻；不是校验器窗口缺陷。机器检查不替代root DAY。
