# 2026-05-10 既有 Daily 来源补充（唯一作者记录）

作者：may10_supp_author。非报告作者复核：may10_supp_reader，独立记录见 [SUP_REVIEW](./SUP_REVIEW_20261018.md)。本记录不代替独立验收。

## A1 范围与冻结

已完整读取当前 AGENTS、RESEARCH_CONTRACT、RESEARCH_SOURCES 使用说明/每日组/arXiv主题与恢复、REPORT_CONTRACTS、CODEX_RESEARCH_PROMPT、ROADMAP，以及 LEARNING_STATE 的 `进行中：2026 年已有 Daily 增量来源补查 → 本次恢复（2026-10-18）`：128/279 已验收，至05-08；尾部113/279为旧快照，不作当前路由。

本轮仅 own `papers/2026/05/10/README.md` 及本日日源目录，补查窗口为2026-05-09北京时间完整自然日。原小时窗 `2026-05-09T09:00:00+08:00 ～ 2026-05-10T09:00:00+08:00`、原0候选和连续原§4保留于[补查前原件](./baseline-before-supplement-20261018.md)。旧空表不是本轮零候选依据；旧“投稿/DataCite/周末整体失效”不继承为新筛选规则。有效旧审阅逐层复用。本轮不动旧436/57/29材料，不将宽列表变成全文队列；不扫描Weekly/Live/2025，不stage/commit/push，不改Books/LS/公共文件。

## A2 首批实际判断与校准请求

1. **ERNIE 5.1 同事件去重**：[官方正文](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/)本次实际读取核心§Technical Features及post-training三分支。页面May09日值及原metadata `2026-05-09T00:00:00Z`属于本轮May09补窗，不能沿用旧09:00起点排除。但是定点读取[05-09原日报](../../09/README.md)确认它已经是原1候选，公开日05-09、原7分，具有深入完成/Ch33（Ch21、Ch31相关）已有覆盖的有效层；同一次release不在May10重复列候选、评分、做Books，也不搬原归属。reader已实际核同一原文与原行，通过独立R1；不是贡献排除。
2. **Seed1667 / arXiv2605.09233v1，日期线索而非当窗候选**：[官方精确v1](https://arxiv.org/abs/2605.09233v1)完整题摘已实际读，给出复杂image-editing单轮指令混淆与序列误差累积之间的机制取舍，不能只按“模块组合”否定。官方v1原字段为 `Sun, 10 May 2026 00:23:05 UTC`，v2为Jun01；当前Seed API `PublishDate=1778342400000`（May10 BJT）、`UpdateTime=1783049568000`。这些均不提供May09首次正文；目录日不替代arXiv公告，已具名恢复到补窗之后，不评分或写Books。没有具体更早作者稿线索，不无限假想渠道。
3. **MiMo science应用代表C**：实际首页Blog卡片 `How Xiaomi MiMo-V2.6-Pro Boosts Productivity in New Materials R&D` 的核心说明是文献、分子设计与PFAS材料dry-lab，属ROADMAP明确暂缓AI for Science，不因使用Agent而重入主线；日期不影响该关闭，不另造日期请求。其余无日期Blog技术卡不伪称已核May09没有发布，保来源限制。
4. **搜索噪声代表C**：官方域May09定点检索出现OpenAI Developer Community的[Frustration with short free limits](https://community.openai.com/t/frustration-with-short-free-limits/1380546)、[Cool Feature Request ! Hierarchical Projects](https://community.openai.com/t/cool-feature-request-hierarchical-projects/1380213)等；标题明确是用户支持/产品反馈而非原始研究，不把它们当机构研究准入或建立逐项全文队列，不虚增为逐条完整题摘数量；未用社区评价证明产品或研究事实。

本轮首批没有确定新增P；上述同事件与日期边界/代表范围C交reader实际准入校准，不以零P免除独核。

## A3 十四每日来源：本日实际入口、停止与权限

检查执行于2026-10-18，本次网络读取不继承05-09作者的来源结果；只定点复用其API路由与ERNIE去重身份。

| 来源 | 本轮实际入口与停止 | 结果与限制 |
| --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)与Research index入口；`site:openai.com "May 9, 2026"`，另原站`/news/research/`直接GET403 | 搜索只出社区支持噪声，Research显示当前精选；历史May09完整日级目录未恢复，保留不授完整Coverage/零遗漏 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)直接GET288320字符，实际读取嵌入记录publishedOn/slug；[Alignment](https://www.anthropic.com/research/team/alignment)可见历史列表 | nearest before为teaching-claude-why `2026-05-08T12:18:00.000Z`，after为2028-ai-leadership `2026-05-14T17:06:12.172Z`；前者BJTMay08，不移May09。嵌入当前已列记录不等全站历史保证 |
| SRC-GOOGLE-AI | [DeepMind Research](https://deepmind.google/research/)和[Google Publications](https://research.google/pubs/)实际当前页；`site:deepmind.google "May 9, 2026"`与May2026定点补检 | 未恢复May09日级历史分页停止，Publications当前年份/领域过滤不是已读本日论文清单；保历史slice限制，不冒零命中 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)返回0行，官方域May09定点查询未得研究事件 | 空正文和检索无命中不是完整覆盖；必要历史slice受阻，不授正面覆盖 |
| SRC-QWEN | [旧Blog](https://qwenlm.github.io/)迁移指向qwen.ai；实际`GET https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=zh-CN`，data仅articles、实40；全部40的id/title/extra.date本次逐项读取 | 无May09；跨窗邻项Qwen-Scope id66eb554c… `2026-04-30T12:00:00+08:00`与LiveTranslate ide3d5b6b8… `2026-05-19T17:40:00+08:00`。返回无序/无next字段，只闭合当前zh-CN40条，保历史删条/所有语言限制 |
| SRC-DEEPSEEK | [News](https://www.deepseek.com/news/)本轮实际当前列表与[Change Log](https://api-docs.deepseek.com/updates/) | News研究相邻Feb25→Jun24、动态Apr24→Sep10；Change Log Apr24→Jul31，未列May09；只检查这些明确当前公开入口，不授全机构绝无更新 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog)本轮列表最晚2025Nov07；[MoonshotAI](https://github.com/MoonshotAI)当前组织页直接GET309486字符，定点May09检索无相关结果 | 当前Blog未覆盖2026May、组织页非历史发布索引；日级slice仍缺，不把缺口当零命中 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)空壳后，本轮实际POST`https://api.hunyuan.tencent.com/api/blog/publicList`，JSON`{"pageNum":1,"pageSize":100,"renderType":0}`，code0/success、totalNum9、实返9 | 全英语；displayPublishTime跨窗前id100039 Apr30 15:00BJT、后id100064 Jul08；余Sep22/Aug28/Aug06/Jul21/Apr23/Feb13/Feb03。九行无May09，总数等实返可止此响应；不冒中文/删除历史范围 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)web两次超时后，本轮direct GET1097165字符成功，实读可见日级列表（不是updatedAt媒体字段） | `2026/04/29 Scaling Pain`→`2026/05/20 ZCube`跨窗、无May09，已恢复本片段；无须把一次web超时记永久不可得 |
| SRC-BYTEDANCE-SEED | [Papers](https://seed.bytedance.com/en/public_papers)及官方GET`/api/get_article_list_v2`，`article_type=1/2,publish_year=2026,page_token=0/20,count=20,order_desc=true`，头x-tt-locale US | type1/page0实18、next20/true/total86；page20实20、next40/true，May16→Apr15穿过May09后停止。type2/page0实15、next空/false/total20后止；无May09目录行。实返与total差额/英语范围保留，1667定点v1见A2，不以目录覆盖首次公开 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)与ERNIE5.1完整核心 | May09真实事件，经A2同事件去重到既有05-09，不当零事件或本日新候选 |
| SRC-XIAOMI-MIMO | [MiMo](https://mimo.xiaomi.com/)Paper列表+Blog卡片实际读取；Paper跨窗相邻Mar13 ARL-Tangram→Jun29 MOPD；本域May09定点查询 | Paper该片段无May09；Blog缺日期历史索引，受限且具名，Science卡按A2范围关闭。只为日级日期请求，不全读所有后版卡 |
| SRC-MINIMAX | [Blog](https://www.minimax.io/blog)本次实际可见Research列表 | 跨窗Mar18 M2.7→May26 Sparse Token Forgetting，后May27/Jun01等已见，未列May09；有限当前列表不外推全部历史 |
| SRC-ARXIV | [availability](https://info.arxiv.org/help/availability.html)本次实际schedule/deferred说明；精确09233v1；本日四主题日期查询、十二类官月表形状和DataCite registered窄补，实际范围见A4 | 无常规batch；无具名May09可采用事件。日级列表/异常延迟历史slice未恢复，不把此限制或registered0当无遗漏，亦不把旧436项作为新全文队列 |

Weekly组没有加载扫描；按需源没有实际触发需审事件，不另扫描。

## A4 arXiv 有限发现收口及失败诊断

本次实际按ROADMAP四切片发出官方advanced查询（all fields、计算机分类、含crosslist、size50）：①language model OR transformer OR mixture of experts；②training OR inference OR GPU OR kernel；③multimodal OR world model OR vision language OR diffusion；④agent OR retrieval OR memory。from/to均2026-05-09，date_type=announced_date_first。四响应约30k字符，标题为Advanced Search而不是论文结果。实际剥离页面字段后确认 `End date must be later than start date`，且官方帮助明确 announcement date只支持year/month granularity；因此四次均是诊断失败，不计四个零结果或正面主题覆盖。不改成submitted_date冒充公开日期，不为日级补查把整月改作全文队列。

本次十二分类 `cs.CL/LG/AI/DC/CV/RO/AR/PL/OS/PF/IR/MA` 官月表 `https://arxiv.org/list/<category>/2026-05?show=2000` 均实际GET成功，只读取页形状/总数及查找日界元字段，不声称已逐条读标题。实示总条目2844/6573/6561/459/3828/1168/186/120/29/94/464/433；CL/LG/AI/CV仅前2000，其他不超过2000。页面是Authors and titles for May 2026，没有本日可用的daily日期分隔；`/list/cs.CL/2605`以及`/list/cs.CL/260509`等直接日键恢复失败。这里不把月表全量或首2000当May09覆盖，也不重开所有月条目。此前web 404后已改用实际有效年/月路由，不能将一次失败说成原站全部不可得。

针对异常/延迟线索，实际定点搜索 `site:arxiv.org "Sat, 9 May 2026" language model`、`"9 May 2026"`加language/diffusion/agent/Transformer/inference，以及 `site:status.arxiv.org "May 9, 2026"`、arXiv Blog May2026 delay announcement，未恢复具名本日相关公开稿/延迟说明；搜索跨月无关结果（天文观测、一般项目delay）不当研究候选，也不用于阴性保证。

DataCite窄补已做有效性控制：第一种 `query=client.client-id:arxiv.content AND registered:[...]` 在May09和相邻工作日均0，不能授阴性权限，已停用。修为REST `client-id=arxiv.content` + `query=registered:[...]` 后，相邻May08控制返回total1461/sample DOI `10.48550/arxiv.2605.06476`、registered `2026-05-08T13:29:46Z`；只验证过滤器，不读取/扩入邻日论文池。精确 `10.48550/arxiv.2605.06241`接口显示state=findable、relationships.client.id=arxiv.content、registered=`2026-05-08T13:20:12.000Z`，确认字段/登记方形状而非本日候选。

最终[原始窄响应](./datacite-registered-window-20261018.json)采用BJTMay09完整日的UTC界 `2026-05-08T16:00:00Z`至`2026-05-09T15:59:59.999Z`，page1/size1，meta.total0/data空、无下一页。**这只表示当日注册发现切片无记录，不证明没有公告、较晚登记或作者更早公开稿，也不以created替代registered。** 加上官方无常规batch和机构有界入口、题摘与具名事件检查，当前没有确定新P或仍可执行的具名日期队列。arXiv历史精确日级/异常延迟切片作为来源限制隔离，重开条件为取得May09官方公告清单/状态归档或具名原始发布；不对互联网无遗漏担保。

### 当前窄停点

有限来源与初筛已收口，确定新增候选0、Books新增0、普通待办0；reader R4有限权限、R5完整六部分DAY及R7保存完成态FINAL均已实际通过。所有本日ownership释放，无Books锁，不自行接下一日。

## A5 六节已保存与作者检查

README已实际融入六节，状态仍进行中/复核未通过。原小时窗与连续原§4（含标题共688字符）实际逐字包含，原空候选表仍是0，新增0非冻结旧零所得。已保存本轮边界、ERNIE有效同事件去重、09233窗后资格、四主题失败诊断/十二类官月表非daily权限及全部来源终态限制；没有Books新写或占锁。

初次V3检查仅因baseline文件名不匹配校验器的固定`baseline-before-supplement-YYYYMMDD.md`规则失败；已读取该规则，用apply_patch Move原件为`baseline-before-supplement-20261018.md`，原文不变并同步正式/作者链接，无删除历史内容。重跑V3通过、7本地引用0missing、原窗/连续原§4比较通过，README与作者SUP限定cached/unstaged diff-check通过。此为当前本日限定结果，不代表全工作树或并发index清洁。

reader独立R1–R4已实际通过首批准入/日期/同事件及有限源权限；R5已实际顺读完整六节DAY并独立复算原窗、连续原§4、0候选与本地引用/V3/两层diff-check通过。作者在其通过后仅行政同步README状态/结论/§5/§6与检查时间，不动任何研究判断或Books。R6实际完成态检查指出§5前缀不匹配受控词，作者只改“本窗终态保留项／来源限制”；R7实际回读该保存态与必要字段、重跑完成态V3及两层限定diff-check通过，授权仅同步FINAL既成结果。作者依此行政更新，无新研究/新复核收据，不替reader签复核；本日ownership及所有锁释放，不自行续日。
