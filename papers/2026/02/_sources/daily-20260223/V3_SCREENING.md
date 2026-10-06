# 2026-02-23 V3 有界来源与准入记录

窗口：02/22 09:00～02/23 09:00+08；作者 feb23_v3；检查2026-10-05。

原始请求按 V3_NATIVE_FETCH、RECOVERY、FINAL_RECOVERY、EXTRA 保存；对应文本为 V3_NATIVE_<name>.txt。HTTP成功只证明响应到达，不证明日期过滤、正文或覆盖。前次V2.1报告/ledger作为旧证据保留，本次未继承其候选、完成标签、注册表生效日期或“只arXiv required”口径。

## 本窗停点

- arXiv标准公告：availability原文含new/cross/replacement/withdrawal；window=[Sat20ET,Sun20ET)，Sunday20ET正好不含终点，标准批次0。没有把Monday日期列表、v1 submitted或后窗标题送入本日队列。
- DataCite恢复query created:[2026-02-22T01:00:00Z TO 2026-02-23T00:59:59Z]，prefix10.48550，page100，实际total0/totalPages0/end。只辅助非标准线索恢复，不代替原源公开时间，也不支持全网零遗漏。
- OpenAI完整RSS可读，最近前后FirstProof 02/20 14:30Z→FrontierAlliance02/23 05:30Z/SWEVerified11Z，零窗内feed事件。
- Anthropic research raw JSON实际publishedOn：02/18 15:10Z autonomy；02/23 11:52Z fluency/11:53Z persona；illustration_createdAt不是发布字段。
- Google研究Blog /blog/?page=6 实际页面12卡片，Feb17 map→Mar4 Bayesian相邻，已穿过本窗。year/month参数无效，已纠正，不称过滤成功。Google pubs首页年精度且只当前20卡片，未作为题摘队列；DeepMind RSS返回HTML、备用feed404、历史分页web不可达，隔离G1。
- Meta当前Research+Blog页1/2已到Feb9 DINO及Mar11 MTIA，日期列表夹杂2025，不能作完整论文历史切片，G2。
- Qwen旧站迁移、新站两入口均客户端壳；Qwen3.5窗口commit[]，G3。
- DeepSeek当前首页+V3.2窗口commit[]；Moonshot Blog停2025/11+K2.5窗口commit[]，各不能代表机构完整历史，G4/G5。
- Hunyuan Research初始动态壳；IAB两timeout、一次子线程visible unsupported；官方api pageNum1/pageSize100/renderType0返回英文9/9，无下一页需求。窗前最近TokenGradient 02/13 08:36:03Z，之后04/22；Accept-Language中文重试仍9英文。未把英文集称全部，G6。
- Z.ai研究15卡片时间排序02/21 GLM5→03/15 Turbo，release02/12→04/07；GLM5窗口commit[]，没有已观察窗内修订。
- Seed asc论文page_token0实际20卡片（全非pinned），末两个02/25，窗前FLAC02/13→FlowPortrait/WorldGuidance02/25；blogs实际9卡片，前三02/12～14→04/01，再含后窗pinned，但无窗内卡片。has_more/next20照实保留；不翻后窗页、不将总82库存变初筛分母。
- ERNIE Blog页1日期02/06→04/15，repo commit[]。MiMo Blog2025/12/16及repo[]不能证明全部历史，G7。
- MiniMax中英文Blog达到Forge英02/14/中02/12、M2.5 02/12→后窗03月；AgentTech只有05/13分组；M2.5 commit[]。

## 代表排除与不评分依据

| 身份 | 实际读到的原始字段/核心说明 | 本次处置 |
| --- | --- | --- |
| OpenAI Our First Proof submissions | RSS 2026-02-20T14:30:00Z | 早于窗口，不继承其其他日候选或正文判断；不评分 |
| OpenAI Why we no longer evaluate SWE-bench Verified | RSS 2026-02-23T11:00:00Z | 后于终点，路由02/24，不在本日审阅 |
| Anthropic AI-fluency-index / persona-selection-model | publishedOn 02/23 11:52Z/11:53Z | 后于终点，路由02/24，不挪窗 |
| Z.ai GLM-5技术报告 | 官方Research显示02/21；release02/12；窗口repo无commit | 目录/发布均窗外，版本名不构成本窗修订；无当前纠错信号触发 |
| Meta Reducing Government Costs and Increasing Access to Greenspaces in the UK with DINO | Blog2日期02/09；核心说明以DINOv2提升造林应用 | 窗外；且应用结果没有公开新增基础模型/系统机制，不按Evaluation/Data节点重引应用 |
| MiniMax Forge | Blog英02/14/中02/12；核心说明Agent RL三角约束 | 潜在相关增量不能因版本/主题排除，但两显示日期均窗外；本日不为无归属争议扩读全文/旧版本 |
| Seed BABE / Protenix-v1 | API题名与显示日期：Biology Arena BEnchmark / Biomolecular Structure Prediction，02/05/02/09 | 均窗外；标题已明确科学应用范围，不宣称本日完整题摘或全文审阅；AI for Science暂缓，不通过Data/Agent重引；不计本窗排除分母 |

确定当窗家族0，贡献候选0，证据审阅0，Books No Change0写入。上述7行是校准样本/日期旁证，不是本日七个原始命中或七篇全文审阅。历史目录无法恢复与当前未观察到事件分开记录，§5 G1～G7具名终态隔离；不支持Coverage/Evidence Passed。

普通待办：0。root已实际原源校准/最终DAY复核通过；空拟入选与Books No Change成立，七组外部限制隔离。完成态V3与本日限定cached/unstaged diff-check通过。无Books写入任务。未stage/commit/push。

Hunyuan定点历史边界复用：本次native英文9条；前次同官方原源daily-20260222/V3_NATIVE_hunyuan_zh.txt中文11条实际重读发布日期邻界为TokenGradient02/13 08:36:34Z→Hy3preview显示04/22（后者publishedAt06/24，不把显示日授精确初公开）。当前并未恢复中文请求的确切语言选择，故不猜参数、不再无界重试，仍隔离G6，不授当前中文全量覆盖。
