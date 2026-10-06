# 2025-09-05 非作者日级验收

复核者：sept07_10_author；报告作者：sept12_15_author。检查时间：2026-10-06T22:18:01+08:00。只验本日 2025-09-04T09:00:00+08:00～2025-09-05T09:00:00+08:00，压缩恢复重读当前 AGENTS、研究/Report 合同、Prompt、来源使用说明/每日/arXiv 和 ROADMAP；月 checkpoint 仅作路由。未读 Weekly、未扩大其他日或月份、未修改共享 Books。

结论：通过

## 1. 来源与有限停止

实际检查本日 capture/query/request 与 HISTORY_WEB 原件：四条主线查询 39+19+20+48=126 命中、103 去重题名；submittedDate 仅为发现字段，不是公告。没有把整类库存变成逐项全文队列。14 每日源均有具体入口、日期段或分页停止；核 RSS/机构列表及动态接口可返回范围。当前目录、draft 配置、空 API 响应都未被授予 2025 冻结或零命中。

独读 catchup-cl/cv 的原始请求与响应标题/正文，合法 subject/date/include_abs 请求确有“Catchup only allowed for past 90 days”；不能由普通日期 list 的 HTTP400 倒推期限。另只修复本日已有月表请求的 show 参数作有限诊断，不浏览月题名：

| 原始 URL | UTC检查时间 | 实际响应 | 原件必要内容 |
| --- | --- | --- | --- |
| https://arxiv.org/list/cs.CL/2509?skip=0&show=250 | 2026-10-06T14:17:59.802256+00:00 | HTTP404；8235bytes；SHA256 7a814d719b707730dabaa667474af45b17c7fda53aa94aeadf23982d5f759e40 | title: 404 Not Found \| arXiv e-print repository |
| https://arxiv.org/list/cs.CV/2509?skip=0&show=250 | 2026-10-06T14:18:01.442708+00:00 | HTTP404；8235bytes；同上 SHA256 | title: 404 Not Found \| arXiv e-print repository |

这只是本次可用入口的真实停止，不证明永久无法恢复；68 arXiv 潜力和七个历史目录缺口按 README§5 隔离。需要正式公告/同版原始公开时刻或可信等效冻结，恢复时只重开对应项，不请求68全文、不支撑覆盖完整或性能/安全保证。

## 2. 完整题摘与关闭分层

独立实际读原86完整 v1 题摘（exact-v1.raw 全部0～85，截断段另补），以及 exact-title-reopen-v1.raw 三个完整 v1 题摘；共89，不把 current 摘要替代 v1。全部68潜力均在此题摘核准入，不授日期通过或实验可信度。官方4家族另读核心说明，合计93完整筛选=正式1+日期潜力68+关闭24；14仅题名的范围外不是摘要已审。

明确关闭按机制组合/应用、综述、评价归因和撤回分层核：04324/03793/04139/03893/03827/03995/03903、04162/07996/03871、03890/03962/04152/03972均完整题摘复核；04537读决定准入核心；03658/04549复用 root 有效定点 FIRST 核心结论，并检查本日原始题摘/具体理由；04250 本 reviewer 与作者实际题摘/核心发现临床超先验与患者试验范围，root 后续独核接受关闭。不借自己的 LPD/statistical-power 批评发明主线贡献。

两个相关撤回信号独读官方 abs-06996、abs-04104-v1/v2：06996 current article Admin 撤回，不因旧v1可下载恢复采用；不声称实验全假。04104仅v1许可撤回，v2 November 恢复不能反向赋予9月v1有效性，也不把前版撤回传给当前家族。

14题名范围外实际核题名并限定对象，不声称全文已读。本次发现原17题名中10526/19305/04169含糊，定点补完整摘要而非扩库存：10526由层局部/连续ratio变全拓扑GAT+binary mask、19305由time-only变分频/跨频条件，分别保留有限模型压缩/轨迹生成潜力；04169原文LiRA分类适配和LSTM/N-HiTS forecasting MIA，LLM只有echo类比，未给可迁移主线新条件，关闭成立，不是按EEG/时序领域标签关闭。03918原件为thought路径/树冗余和column/cell双轴通信，已纠正表格flatten的错误释义。

## 3. 必要核心实际范围与反证

本 reviewer 实际定点读27个arXiv家族核心，另Anthropic完整核心1、两撤回状态轻核；不冒充作者44+1的全部核心或93 FullEvidence。具体版本均本日原件v1；HTML段号以inspect.py为准，03828/04198为PDF物理页。支持与反侧到足以限定命题处停止，不认证全部数学证明/附录、代码实现或实验复现。

| 实际家族 | 必要位置与核验结论 |
| --- | --- |
| 03768 | 45～63/69～75/85～95；SafetyClamp固定槽位不保证语义/完整法规，全条款仅7%/6%，local CPU index不授端到端LLM延迟 |
| 03888 | 19～30/39～54；ID近98%不抵消clean/OOD/trigger反侧；15～99pp下降仍有分布混杂，不授所有probe无语义 |
| 03647 | 9～29必要方法/评价；gold为模型多数非人类真值，97%非法票flip同时合法票不稳定 |
| 12221 | 73～113；routerρ、逐样本CE-gap和Lipschitz前提，ASR拒绝串不授真正有用性/安全 |
| 05367/05362 | TRIAL18～30/34～39/56～58；scambait45～63/96～105/148～161/260～279；多轮局部失败、helper/judge限制；噪声不授DP，secure aggregation实施/未来说法冲突，模拟engagement非真实诈骗安全 |
| 03730/03736/03805/04373 | 65～76；48～53/57～61/76～89；38～45/71～83/90～108；24～30/64～80；人格自报与行为分离、LLM judge局限、guess-sharing与提取recall反侧、probability/discrete分母区别 |
| 03615/04534 | 23～26/35～53；8～25/30～37；OCR同图/CPU与语种不对称；量化memory下降但latency/质量非单调，4×A10040GB不授消费单卡或临床安全 |
| 04537 | 15～18/28～40；相同GPT4o/prompt/memory群体行为未隔离pretraining内在动机，准入关闭而非因深审困难 |
| 03787 | 40～58/70～80/83～103/116～119；TREC22/27、8:2池/MonoT5 top10前提，judge非全人类，GPT5仅局部；未全读59～69/104～115，不授所有RAG或训练暴露因果 |
| 03985 | 60～81/100～131；linear probe/SNIP/投影与真实break有反侧，局部百例/合成攻击不授安全内部因果或普遍防御 |
| 04018 | 26～83；成功轨迹关键帧、监督最多3次且关键帧1.766s，不授真实碰撞安全/无时延；5任务×32局部执行 |
| 04292/04403/09700 | 16～35/38～56/75～81；22～43/60～84；23～75/82～87；非惯常指令/Best-of32选择边界、生成/judge同源、non-abstained分母与OOD任务范围，非安全保证 |
| 04343 | 21～32/42～62；NONE/EXPERT与固定行为协议有局部message/action差，问卷不认证真实人格/安全 |
| 03828/04198 | PDF3～8；7～9/11～12；catalog validID100%仍12/142语义错误；ComputerUse比RPA时延/成功反侧且P3仅首4invoice，不认证真实临床/生产流程 |
| 04154/04027 | 9～14/124～125/145～150/276～281；39～53/56～91/97～107必要段；线性SDE/可逆/各向同性/小角近似，不授任意attention精确Bayes；PAC-Bayes iid有界及上/下界不强制实际risk U形或普遍RL收敛 |
| 10526/19305 | 25～61/90～95/123；33～65/69～88；二阶段FLOPs reward不是hard runtime，EMA/nonstationarity与policy architecture绑定；H96/D4RL/5seeds/loss-ratio和Hopper条件消融不认证闭环稳定、真实环境或所有扩散模型 |
| 03990 | 31～59；C(s) posthoc只验证已写约束，部署memory冻结；60train/74test、Reflexion六轮test适应与MPR一次不等预算，不授全安全 |

作者其余17个arXiv定点核心没有被本 reviewer 全文重复：其完整题摘已独核，具体命题在 NECESSARY_CORE 限定，日期未明且不进入正面证据/Books。没有把未独验的全部公式/数值授为成立；新证据到达须按相应采用命题重开。root有效 FIRST 的未变化结论复用，不同层不相互替代。

## 4. 唯一正式候选与Books

Anthropic biorisk 原文0～44实际完整读（34输出截断另补）；article:published_time、JSON-LD datePublished、visible time三字段均2025-09-05T00:00:00.000Z=08:00BJT，非draft，正式发布事件完全落窗。dateModified=2026-07-08T20:53:48.000Z独立保留：不授全部当前正文冻结2025，不把后续修订混作当窗事件。

本文实际提供受限LLM安全measurement案例：expert quiz/两日文本plan相对internet-only的expert-rubric uplift不等真实复杂过程能力；2024基础wetlab n=8未见uplift也不排除所有风险，更大study仍是计划。precautionary ASL3/input-output classifiers是在不能排除能力风险下的取舍，非现实风险已证或公开可再实现新classifier算法。接受root FIRST的2+2+2=6；因安全发布边界，受影响正文深入审阅完成，不仅摘要。

Books纳入流程，最终仅报告。独立实际比对Ch66 proxy目标约125、refusal/harmful-uplift多轴约809～816，以及Ch72约2175～2179治理要求/探索假设/控制有效性分离，确有长期责任边界。当前案例不披露可再实现新classifier机制，且2026正文不能作为2025 exact-body机制冻结；因此不制造Book增量，也不把此次仅报告伪标已有覆盖。root无新Books写入，无POST改稿待办。

## 5. 修正与终态

04250关闭、Anthropic由配置-only hold恢复正式、三含糊标题两恢复一关闭、03918 thought机制措辞均已实际同步作者包/分母。最终93=正式1+潜力68+关闭24；正式候选1/1深入完成且1/1仅报告。来源历史缺口/68日期潜力仍隔离，不是Coverage/Evidence通过、不支持无遗漏。无可执行本日作者/复核/Books待办，条件符合完成。2026-10-06T22:22:14+08:00最终同步：V3 report validator通过；六部分齐全、README全部本地引用存在；限定git diff --check及两个未跟踪文件no-index空白检查无诊断（no-index状态1表示新增差异）。机器结果不能替代本记录的语义验收。仅写本日README及本独核记录，无Books/索引/LEARNING_STATE变更，无stage/commit/push。
