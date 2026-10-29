# Jan14 三项独立必要复核 delta7（2026-10-08）

复核者：review_jan15_delta（非作者）。仅 root 授权的 07422 / 07072 / 07516。沿用本日当前合同及 BJT Jan13 完整自然日补充窗；未加载其他日期，未重开原17项/窗口，未改 Books、Report、LS、索引，未 stage / commit / push。不授 DAY。

完整题摘已逐项读 increment-abstracts-1/2/3/4/5-20261007.json 的对应行。各项贡献通过后才执行必要证据及 owner 判断。作者 proposed score 与独判相同：三项均 2+1+2=5、标准审阅。局部结果/诊断允许构成实际贡献，不以因果控制不完美、已有主题或弱实验直接否定准入。

## 日期与当前身份

复用本日已核正常公告/正式ID日期上下界，结合 increment-date-bounds-rest-20261007.json 的三行原字段：07422 v1 Updated Jan13 02:16:41Z → registered 04:02:29Z；07072 01:56:25Z → 03:54:15Z；07516 02:21:39Z → 04:04:42Z。归属仅 BJT Jan13，不把 Submitted、月级 Available 或 registered 独自当首次公开证据，不追秒级公开时点。

独立轻读当前官方 abs：07422 current v2（Apr15 / ACL2026 Main）、07072 v1、07516 current v2（Apr13 / ACL2026 Main camera-ready），页面未见具体撤回/纠错说明。未比较历史版本，v2/会议标记本身不授重要修订；采用下列 exact-v1 必要证据，不静默混入当前新版。

## 原证及实际范围

- 07422：increment-necessary-core-2601.07422v1-20261008.json 的完整 §2–5 / 限制；另实际官方 HTML 读 B1/B2/B4/B6 的 exact span、probe、人口及训练细节。
- 07516：increment-necessary-core-2601.07516v1-20261008.json 的 §3.1–3.3、§4采用结果/消融、限制。§3.3 和 §4.3 单独重读补齐此前输出截断；不将未消费的细粒度指标或完整附件列为通过。
- 07072：作者 increment-necessary-core-2601.07072v1-20261008.json 仅 observations，不能代原证。已独立恢复官方 v1 PDF 的 §2 threat、§5 end-to-end / Table2、§8 限制（实际 PDF 第13页，不是提案p12）。新保存 [独立必要原文](./increment-independent-delta7-necessary-20261008.json)，并含 07422 必要附录原文和三项 current 身份观察。仅采用决定事实，不遍历攻击 payload/artifacts 或完整附件。

## 逐项裁决

### 2601.07422 Two Pathways to Truthfulness — 5 / OnlyReport PASS

沿 question attention knockout 是否令原 probe 预测翻转定义 Q/A 类，再用正确样本的 exact question patch、answer-only forward 检查有限表征依赖，并让 expert/gate 与 attention reweight 服务检测。这比原始 attention 相关性多了限定干预与读出分工，贡献准入明确；没有把两类定义推成穷尽 truth/knowledge 因果路径。

拒答被排除，GPT4o_2024-11-20 最多5次提取，仅保有效 exact span；4QA 的2000 train / 2000 test、held-out best-layer、三 seed、head/gate训练和校准费用保留。正确率/popularity/IDK关联不等知识成因或意识，MoP/PR检测AUC不授生成truth改善。RandomGate局部退化是直接对照，不签所有人口效用。PR 的 positive alpha 不保证 1+s 非负，层/每head口径不拼完整工程 recipe。没有需改 Books 的已确认长期差额；Only 不是否定论文贡献，也不授当前黑箱可用。

### 2601.07072 Overcoming the Retrieval Barrier — 5 / 具体 Existing PASS

未知 corpus、单个注入外部项、仅 black-box embedding API 的 query-specific 检索进入约束，是本次标准采用的真实接口贡献；到达 top-K 和后续 instruction/action effect 分开测量。Table2 的 GPT4o R@5=1 与 answer ASR .02 / code ASR .04 是直接反侧，不能把 near-100 retrieval 推成控制/执行成功。RAG ASR 排除 clean 已产生目标的样本，属条件分母，不是部署事故率。

实际读 books/part-06-ai-infrastructure/72-security.md:663–710 完整邻接：673–688 的 retrieved input → source/consensus sensor → runtime influence → authority registry → step guard → deterministic execution policy，以及690–696对 input alarm、proposed action、actual execution effect 的分开计数，具体覆盖拟采用命题。不称本章已有 CEM 攻击算法，不需加算法段或引用堆叠。

保 Enron 单用户至少50邮件、10条ClaudeSonnet4合成FAQ、每query一注入、5seeds、agent query rewrite及不同角色边界。§8只评dense embedding检索，不签 hybrid/rerank/所有index普适，也不从迁移结果授所有架构。embedding搜索/index/model/agent/完整测试费用应分开，$.21非end-to-end全费。Existing无需Books锁/写入。

### 2601.07516 Coverage-Enhanced Latent Actions — 5 / OnlyReport PASS

稀缺 paired 下，text latent 经 P 进入 image-text latent，text-only 上以 P 的均值再经逆投影 cycle 训练，再用128-code inverse future-labelled latent训练 current-prefix policy；RL只更新policy、冻结decoder/world。这一数据域/训练接口有具体可迁移局部增量，不因组合成熟或conversation任务关闭准入。

投影不是新增真实paired，cycle并不认证跨模态语义。future inverse输入仅训练时privileged，不授推理期future访问。3B GRPO LS2 .837低于token .845；去cycle/投影/text-data消融同时改变训练或数据，不能全归因“覆盖”或某个单独部件。两conversation任务、外部judge与GT比值、三评测runs限制外推。Eq3的绝对logvariance项不当标准 signed Gaussian NLL；不替作者修recipe。1.08总RL训练与1.13rollout/推理阶段口径不同，不签总费用节省。未确认需要Books新增的长期命题；Only不授world真实性/物理state保证。

## 交接与停点

三项必要支持与决定性反侧已闭合：2 Only、1 concrete Existing，均5标准，无Integrate/POST。作者可同步这三项正式处置，不扩计整日完成；普通待办及 DAY 由主流程负责。root另授权07430/07208为下一具名两项，独立执行，不能由本轮PASS推其通过。
