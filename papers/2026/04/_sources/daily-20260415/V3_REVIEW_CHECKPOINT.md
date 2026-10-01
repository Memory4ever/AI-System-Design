# 2026-04-15 V3 重审 checkpoint

状态：2026-09-27T11:59:07+08:00，独立日级 Gate 通过，正式日报 Complete。本记录不替代正式日报；以下批次“待核/未冻结”保留为过程历史，以本段为当前入口。

冻结123唯一家族：22实际整合、5具体已有覆盖、78仅报告、17争议终态、1必要正文受阻终态；41深入完成、64标准完成，18项隔离不计证据通过。22正文写后及5 Existing真实命题均通过非作者核；root有限否定侧、来源/日期与争议范围审查通过，具体范围见正式日报§6。普通可执行工作为0。546标题与240题摘不是候选分母或第二人全量深审数，精确外部保留项见日报§5，不支撑无遗漏或Books保证。后续04/18由apr01独立推进，重读AGENTS/当前合同，不继承本日状态。

- 窗口：`2026-04-14T09:00:00+08:00`～`2026-04-15T09:00:00+08:00`，左闭右开。
- 本轮检查时间：`2026-09-27T11:29:21+08:00`。
- 已重新读取当前 AGENTS、统一 Prompt、研究/Report 合同及 Daily 来源分组。历史 Daily 独立于 Weekly。
- 旧 V2.1 README 的 546 DOI-created 原始条目/25 候选不继承。库存仅提供身份与题摘线索；旧通用排除理由不作本轮证据。

## 来源实际停点

| 来源 | 实际入口与停点 | 结果与边界 |
| --- | --- | --- |
| Qwen | 官方 `https://qwen.ai/api/page_config?code=research.research-list` 60 静态项（最晚 2025-12-23）+ `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US` 40 动态项；邻域 04-02 04:00+08→04-15 10:00+08；GitHub QwenLM created-desc 58仓库至2023-08-03；Qwen3.6重要release API实际返回空数组 | 该官网可见研究列表及组织新仓库本窗无项；Qwen3.6-35B-A3B在截点后1小时。不用当前网页modified时间回拨。 |
| 混元 | 官方 POST `https://api.hunyuan.tencent.com/api/blog/publicList`，`pageNum=1,pageSize=100,renderType=0`，`totalNum=9,list=9`；`displayPublishTime` 的邻域 04-23/04-30→02-13 | 官方公开“全部”目录本窗无条目；不声称作者未列出的全部论文无更新。 |
| 智谱 | `https://www.zhipuai.cn/zh/research`首屏16条04-29→04-07→04-01；官方release-notes原标签06-16→04-07→02-12；GitHub zai-org created-desc53仓库至2021-05-25 | 这三个实际目录本窗无可见条目，不外推未列作者论文。 |
| Anthropic | 官方Research HTML `publishedOn=2026-04-14T13:01:00Z`，slug `automated-alignment-researchers`；前后04-09T16:34Z/04-22T14:12:30.673Z；技术正文`https://alignment.anthropic.com/2026/automated-w2s-researcher/`必要§1–7已读 | 1个本窗家族；weak-to-strong instance-dependent channel×strong prior→EM soft labels，2+2+2=6、gap深入，已实际整合`TRAIN-RLHF` Ch31 503–507；root必要源审阅+写后非作者PASS。其他AAR evaluator/holdout原则与Ch66/81具体既有正文相比不另追加；不采用PGRheadline为production保证。 |
| OpenAI | 官方完整 News RSS；邻域 04-14T00:00Z `scaling-trusted-access-for-cyber-defense`→04-15T10:00Z `the-next-evolution-of-the-agents-sdk` | 两项均窗外；RSS 不冒称 Research 历史分页已闭合。Research历史分页的实际有界恢复未形成日级停点，作为终态外部gap隔离；恢复条件是可复查官方历史分页/窗口清单，不循环重复失败入口。 |
| Google AI | Research官方月份页`https://research.google/blog/2026/04/`9条04-29→04-03，本窗邻域04-13→04-16；Publications当年358条但首15无日级字段；DeepMind Blog实际page3从April到March，`gemini-robotics-er-1-6` JSON-LD datePublished=`2026-04-14T16:00:00+00:00` | Robotics-ER1.6核心机制/评价caption已读，是本窗1个发布家族；FlashTTS原datePublished04-15T15Z、DiLoCo04-23均窗外。Publications日级停点仍是精确外部gap，不扫历年全目录。 |
| Meta | 官方Research提取0行后实际恢复`ai.meta.com/blog/`p1/p2；p1含04-08/04-06，p2含03-27但混排；官方Publications跳`/results/?content_types%5B0%5D=publication`却呈2016–2020记录 | 已执行有界替代，不能从混排页或旧publication目录证明本窗无事件。终态精确隔离历史窗口覆盖，需要可复查日级列表/可靠分页恢复后重开；不以失败当零。 |
| DeepSeek | 官网`/news`实际目录16条，2026-04-24V4preview→2025-12-01V3.2；组织created-desc39仓库至2023-10-20 | 该公开目录/新仓库本窗无项；官方主页web403后curl恢复成功，不用失败当零。 |
| Moonshot | Kimi官方Blog26条停在2025-11-07；MoonshotAI created-desc43仓库至2023-03-28，KimiK2.5 release目录实际空数组 | 新仓库本窗无项，但Blog可见2025目录不能证明2026完整，历史Blog是精确外部gap，不当全源零命中。 |
| ERNIE | 官方Blog第一页10项，04-30→04-15ERNIE-Image→02-06；608B壳页恢复至`/blog/posts/ernie-image/assets/zh-DoiglxkK.js`229B，继而`App-BsX3z_jp.js`392613B的实际发布正文；作者HF两model card可读 | 8B DiT/3B PE/50step SFT与8step Turbo披露已恢复；PE的GenEval反降及OneIG/文字目标差异保留。官网只有04-15日历日，HF API创建/commit有界补核超时；09:00归属仍需可验证的官方精确事件或同版本公开上界，不以缺秒级字段造时刻。 |
| Seed | 官方API`/api/get_article_list_v2`，article_type1/count20/order_desctrue/page_token20/header x-tt-localeUS；total242,next40，从05-13到04-09已越左界；type2 page0/20 total95从04-23→04-09→04-01，launch日期1770825600000=02-12 | Seedance2.0 paper卡PublishDate1776182400000为04-15日历桶，但record后期更新且arXiv2604.14148v1 Submitted04-15T17:59:40Z晚于截点。不将later正文支持早发modelcard；paper卡原始公开时间/正文精确隔离，Blog launch窗外已关闭。 |
| MiMo | 官方首页Paper8条06-29→03-13→02-03；blog14条无date；XiaomiMiMo created-desc18仓库至2025-05 | 公开paper列表/新仓库本窗无项；blog无历史日级停点，不能拿当前主页当全覆盖。 |
| MiniMax | 英文Blog12条05-26→03-18；中文`minimax.cn/blog`13条04-27→03-18；MiniMax-AI created-desc35仓库至2025-01；AgentTechBlog空列表、llms.txt48当前routes无历史时间 | 两语言可见Blog和新仓库本窗无项；AgentTechBlog历史停点不可得，隔离限制，不声称永远不可访问。 |
| arXiv | `arxiv-owner-replay-20260903/20260415/arxiv-owner-receipt.json` 的 546 库存身份，已读 546/546 标题及240完整题摘；原 `v1_updated_timestamp_revision_metadata_only` 保持原义 | 宽列表用于范围查漏，不成为候选或全摘要/全文队列。下节官方组合支持已核before01Z家族的08～09有据推断；97末端身份仅逐具体潜在贡献核日期例外，不据 DOI-created/submitted 孤证归属。 |

14个Daily来源已各有实际入口检查；尚存的普通恢复/筛选工作与必要历史外部缺口分别列于上表。不沿用旧“无更新”，也不把首屏/空响应当覆盖闭合。

## 首批完整题摘裁决范围

已实际阅读240个完整题摘，逐项见`V3_SCREENING_NOTES.md`（12234库存截断已官方恢复）；546标题浏览只用于范围查漏。root已非作者校准首批8正向/3否定，另校准9项新增准入/关闭例；未冻结分母或扩大为全库存全文审阅。
这些是工作信号，不是冻结候选；精确版本/撤回标记与日期仍须核验。

| ID | 原约束→原始题摘增量→待核判断 |
| --- | --- |
| 2604.11810 GRACE | 动态 coresets 结合 diversity/gradient importance 与 selective kNN 更新；需核是否比通用数据选择组合新增可迁移的成本/质量有效性条件，暂不因 training 名称直接 retain。 |
| 2604.11811 M* | 固定记忆设计无法跨任务迁移；schema/storage logic/workflow instructions 作为一个可执行程序联合演化；需核任务专化是否有独立设计分支而非仅框架包装。 |
| 2604.11838 Layer-wise SFT | 摘要同时称中层稳定、末层敏感，却称只更新中层关键区有效；保留为需核中层更新与已有层敏感性之间因果/选择机制的信号，不采用摘要的普遍局部化断言。 |
| 2604.11890 Normalization-free signal | LayerNorm→tanh/erf 的 APJN 深度增长从幂律变 stretched-exponential，限定初始化/双向 attention/对称 token；可能改变 norm-free 初始化稳定性解释，值得证据核。 |
| 2604.11943 ProbeLogits | 同基础模型单位置 logits 判 action 并在 kernel-mediated host functions 执行；须核复用分类成本与真实执行身份/不可绕过边界，不将 logit confidence 当安全真值。 |
| 2604.11947 ResBM | 低带宽 PP 不靠压缩既有 activation，而在 pipeline 边界嵌入可端到端训练 residual encoder-decoder + 低秩 identity；须核通信/训练目标/额外算力和收敛条件。 |
| 2604.11978 HORIZON | 跨任务构造长时依赖链与 trajectory-grounded failure attribution；须核 horizon 与其他难度混杂的分离、judge agreement 的受限意义；新增 benchmark 不自动 retain。 |
| 2604.12035 Visual pruning calibration | coverage vs attention selector 不只改变 accuracy；保留 evidence→confidence 错配、SCOPE同路径α干预及FastV外部2-pass路径的受限对照；当前v1不支持zeroing/removal的强比较，拟核进入评估/视觉压缩边界。 |
| 2604.12090 StableHLO modeling | 一份 IR 映射多架构、多 fidelity 性能模型，拟核预测趋势可迁移与模型误差，不能把 simulator 执行当 scaled physical validation。 |

下一步：240題摘的有限裁决与必要审阅已收口，123项工作家族均有作者侧处置；22项实际 Books 及非作者写后通过，普通贡献、证据/Books 待办0。17争议、5Existing及排除侧、来源/日期终态隔离提交root有限独立日Gate；此前八项精确采用与实际写后记录见 `V3_BOOKS_PENDING_8.md`。不把546宽库存扩成全文队列，不预先冻结或标日报Complete。SRC-SEED目录停点与卡片事件缺口已分开，卡片缺口终态隔离；12438本轮官方HTML定点仍404，原PDF两入口406记录保留，不重复失败路径。

## 官方日期组合（2026-09-26 实查）

官方 `https://export.arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:2604.11810&metadataPrefix=arXiv` 本轮实际返回 responseDate=2026-09-26T11:25:01Z，header datestamp=2026-04-15、created=2026-04-09、updated=2026-04-15，标题与库存/v1一致。created/submitted仅投稿字段，不改名为首发。官方相邻11809 v1为04-13T17:59:58Z，DataCite v1 Updated04-14T02:11:04Z；11890官方v1Submitted04-13T18:00:04Z处于EDT周一14:00截稿之后。DataCite created仍只是DOI登记，不证明公开。

`https://info.arxiv.org/help/availability.html` 明确永久ID在announcement过程赋予，正常周二20:00 EDT批次对应04-15T00:00Z=08:00+08。结合相邻批次、11810官方OAI、v1身份与449条库存v1Updated早于01:00Z，采用受限的08:00～09:00公开可用区间推断，不声称逐篇精确公开秒数，也不把Updated本身重新定义为首发。末端97条Updated未提供截点前上界，对题摘保留的具体家族记录日期缺口；贡献已具体关闭项不为发表史额外造队列。必要拟采用项继续检查更早正式正文、撤回/纠错与版本污染例外。

## 全日作者侧收口与独立验收索引

- 123 工作家族均有作者侧处置，未以状态宣称日级通过；22真实整合、5已有覆盖、78仅报告、17具名争议、1必要正文终态隔离。普通题摘、必要证据与 Books 待办为0。审阅表41深入完成、64标准完成、17争议、1受阻；候选数量不是546宽标题库存或240完整题摘数。
- 22真实 Books 的必要源/owner和实际正文相邻交接均有非作者写后通过；前14见 `V3_INDEPENDENT_THREE_CALIBRATION.md`，本轮8见 `V3_BOOKS_PENDING_8.md`顶部 root 独立写后记录。Books章末证据状态已窄同步为实际通过，未复现实验。
- 240完整题摘的具体准入/关闭在 `V3_SCREENING_NOTES.md`；546标题只用于主线/含糊信号查漏。已独立准入校准仅首11+另9题摘及具名采用批次，不冒称240全题摘/546全库存被非作者审核。否定侧重点已有成熟组合是否被误作无贡献、保护/纠错信号是否遗漏及主题相同是否被误当 Existing；不把全部raw转为全文队列。
- 5 Existing 实际命题：11838→Ch29可训练子空间须按预算/能力/安全验收；11943→Ch72 Policy-as-Data的sensor/typed decision/deterministic authorization分权；12116→Ch66 Act/Silent/Stop与committed effects；11867→Ch66 matched probe/heldout/judge格式偏差；12426→Ch5可读出→干预→行为的证据阶梯。各必要版本/实验限制在README §4同链接小节，不以章节主题相同作依据。
- 17具名争议均不写正面 Books 保证，经验机制与该局部争议分开；下表给非作者最窄复核/恢复材料，不要求全附件/更多benchmark。

| 家族 | 具体待核矛盾 / 精确重开材料 |
| --- | --- |
| 11947 ResBM | §3–4/Eq6矩形identity乘积不是端点identity；需一致维度/映射限定，不否定受限训练结果 |
| 11810 GRACE | §4.3原quadratic驻点需原权重总和归一，固定half混合缺objective桥；需一致objective与归一化证明 |
| 11841 PERA | AppA.3子集表达集合不能反推全集最优误差被达到；需覆盖最佳近似的条件/证明 |
| 12040 SIR-Bench | Eq5嵌套Hit与Table6同TP分母逆序；需原分母/计数及Eq3指标含义修正 |
| 12196 Radial Consensus | Eq4平方目标与Eq7非平方medoid非等价；需明确实际目标/算法及等价范围 |
| 12168 FHE Llama | §4.6.1/Eq7吞吐单位、表格计时对象及明文client/密文server范围；需原计数与保护合同 |
| 12216 TimeMark | April官方PDF-v1 §6.3非零误差不支持理论100%；需多窗/相关token/低熵与HSM信任范围 |
| 12247 SpecBound | Eq5极限/单调口径、全层执行与commit law缺桥；需真实采样修正与有界保证限定 |
| 12234 UniRec | Eq3跨item省略p(f|u)不保ranking；需固定归一化条件或修正solely coverage证明 |
| 12245 Socrates Loss | E.2单项与整分布entropy等式、动态EMA校准桥未立；需目标/等式/保证范围修正 |
| 12348 PrivEraserVerify | 旧update回放非无目标重训状态，privacy accountant与fingerprint全部删除桥缺；需合法隐私/删除对象合同 |
| 12452 LCT | Theorem1/AppA.2遗漏group multiplicity，零key/value差仍有输出差；需算法质量权重与证明一致 |
| 12479 PFT | Eq3普通条件CE与matched SFT同目标，pair不必严格缩cover/Lipschitz；需objective/预算/锚点条件与证明一致 |
| 12736 TLPO | Eq1熵梯度符号、AppC恒零项与strict mask保证；需正确多action推导/条件 |
| 12757 GF-Score | margin不自动给input L2半径；需空间/Lipschitz或平滑及认证映射条件 |
| 12820 RePAIR | ridge inverse非一般MP逆/精确映射，线性化与非线性MLP缺桥；需projection输入、残差与retain对象限定 |
| 11843 UniMark | Alg2零bit gate拒绝合法全零payload、CLT非有限精确FPR；需payload-aware统计与有限样本/解码合同 |

- 必要正文隔离：12438的HTML404、原PDF两入口406；需确切v1方法/评价可取后重开，不采用延迟headline。不将这个材料项或17D称为普通未读。
- 日期隔离：12086早期OpenReview/ICLR身份但公开时间未取，12175未得April截点前公开上界；不把Submitted/Updated单证定日。ERNIE-Image与Seedance2卡片有具体原始事件时间缺口；组合公告证据仅支持已核家族08–09推断，不宣称逐篇公开秒数。
- 14来源终态依据在上表/README §2。保留OpenAI历史Research分页、Google Publications日级目录、Meta混排历史、Kimi2026Blog、MiMo无日期Blog、MiniMaxAgentTech及ERNIE/Seed卡片原事件缺口；不可得不记零，不作覆盖无遗漏断言。已穷尽有界恢复的明确隔离项可按合同终态保留，不要求无限恢复。
- 最新验证：V3 validator通过，scoped `git diff --check`通过；两者仅证结构/可判定一致性，不代替本日语义验收。没有stage/commit/push或实验复现。

## 已审记录（历史小批状态以本节收口值为准）

已落盘README的部分工作集合为123项（22整合、5已有覆盖、78仅报告、17争议、1必要正文精确隔离；普通待办0），不是最终分母。此前14项真实正文与相邻交接已获非作者写后PASS：root核Ch31/17/77/28四项；apr02核11996/12035/12046三项Ch66；root核12012/12056/12119/12171四项；root和apr02核最新12002/12151/12176三项Ch33/5/66。本轮八项12342/12359→Ch72、12358/12506→Ch23、12373/12447→Ch66、12617→Ch24、12798→Ch49的必要源/owner和实际正文相邻交接均已由root独立写后PASS。后续批次作者側必要审阅及关闭见README/SCREENING；12438精确PDF两入口406后终态隔离，12479中心严格保证争议待非作者核。必要原文、真实owner差异、范围与反证见`V3_EVIDENCE_REVIEW.md`及`V3_INDEPENDENT_THREE_CALIBRATION.md`，实验未复现，单篇通过不预支整日Gate。

17项中心公式/评价争议为11947/11810/11841/12040/12196/12168/12216/12247/12234/12245/12348/12452/12479/12736/12757/12820/11843，各保留具体矛盾与重开条件；TimeMark用官方PDF-v1而非后发HTML，PASA、SpanKey只报告具体受限实现/安全边界。其余标准或深入审阅均有实际机制、评价条件与反证，不把同主题已有误写为算法Existing，不采用摘要宣传或将提交/DOI更新时间孤证改为首发。12086的更早同题OpenReview/ICLR正文仍是身份/日期隔离，不进本日确定候选；Google Robotics发布的Books比较已完成，仅报告其版本/受限评价条件，ERNIE正文已恢复但09:00归属仍有精确日期缺口。普通贡献/证据和 Books 队列已收口；仅保留具体隔离项与独立日级 Gate，不将已终态限制写成普通未读。
