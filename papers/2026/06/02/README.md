# Daily Research — 2026-06-02

**规范：** V3
**窗口：** 2026-06-01T09:00:00+08:00 ～ 2026-06-02T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-01T03:15:23+08:00

## 1. 结论

本轮未确认有同时通过具体贡献与真实落窗依据的候选，不等于本窗零新材料。14每日来源已作限定检查；Google Research、Qwen、MiMo与arXiv历史目录/公开日期缺口为精确终态保留，不支持全源无遗漏。机构列出的本窗政策、基础设施投资与平台可用性事件读核心后因无新机制关闭；窗外事件不移入本日。

旧110家族（旧32整合/75已有覆盖/3仅报告）已从正式候选表移至[唯一恢复packet](../_sources/daily-20260602/V3_RECOVERY_BLOCKERS.md#110旧工作家族具名datehold清单)，统一DateHold，评分/完成与采用标记仅为历史工作记录，未经此次日级验收。原1,449发现及旧66恢复不成为本轮逐项全文队列，也不继承全110证据通过。针对旧“无平台ownership/跨workload/大模型”理由，实际恢复00944、00997、00981、01128、01600、01185六项必要机制和关键反证；六项与旧110身份不重叠，共116具名日期保留，非116候选或已审证据。日期未闭合，均不授权本日Books写入。

本轮Books实际新增0。旧32I的书稿保留其他有效来源与已经存在的机制，但当前日采用链未通过本次验收，不计本轮整合；不以日期受阻一刀删正文。PRISM的一般GL adaptive不变性反例、OALM有限统计反例、Auto-formalization数值冲突、LocalMixVR配方/中间公式差异与其余两项小样本/选择边界均保留，未升级为普遍正确性、性能或安全保证。root非作者限定安全终态日级复核通过，普通可执行工作为0：116终态日期保留，无已核准当窗候选，旧32I本轮不验收；完成不等于116项证据或Books全量通过。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 10/01实际从[Research](https://openai.com/research/)→[官方RSS](https://openai.com/news/rss.xml)，仅过滤本窗UTC[06/01 01,06/02 01)；3事件均读核心说明：AI政治立场06/01 17Z、Michigan基础设施12Z、AWS availability10Z，分别关闭为政策/施工投资/平台可用性，不新增机制。RSS边界前两条06/01 00Z、后一条06/02 02Z，不移入本窗 | 已检查 | 当前RSS历史保留不能证明已删除事件无遗漏；不继承旧Codex日期 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)可见10条后See more无效，但实际官方HTML hydration含173个publication字段；只提取目标窗及相邻日期，06/03 10:55Z/18Z→05/27 17:51:10.599Z跨窗，未见本窗条目，停止，不读取其他日期正文 | 已检查 | 当前目录元数据不证明历史删除项或未收录项目；不是搜索无命中推零 |
| SRC-GOOGLE-AI | [DeepMind News第2页](https://deepmind.google/blog/page/2/)实际06月→05月边界，相邻原页核Gemma4 12B=06/03、Singapore partnership=05/20，不移入本窗。[Google Research Publications](https://research.google/pubs/)仅年度目录，Blog当前页到08/26；补检site:research.google/blog/、June1/2 2026无结果 | 受阻 | Google Research本窗first-public历史停止范围未恢复；当前年度目录/搜索空不能证明零，隔离此覆盖缺口，重开需目标日期官方目录或带时区原始事件，不扩全年 |
| SRC-META-AI | Research空响应后恢复[官方publication第1页](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=1)，实际相邻06/05→05/27跨窗，停止；日期限定补检读[SA-3DAO原页](https://ai.meta.com/datasets/sa-3dao-sam-3d-artist-objects/)核心：06/02无时区，原2025 SAM3D benchmark的100公开/900holdout与数据下载说明，未提出新的机制、反证或协议变化，pre-denominator关闭，不追不影响处置的时刻 | 已检查 | 官方列表存在旧年份乱序/保留局限，不宣称全目录无遗漏；SA页面日期不作当窗新论文 |
| SRC-QWEN | [qwenlm](https://qwenlm.github.io/)静态目录到2025/09指向[qwen.ai/research](https://qwen.ai/research)；新页web0行、直接HTML仅壳/SEO，无目标日期；两轮限定该官方域June1/2及2026/06/01–02搜索无命中 | 受阻 | 有限原始入口/补检后未恢复2026本窗目录；不作为零命中/正面采用依据。重开需官方目标日期列表或带时区发布，不扩全年 |
| SRC-DEEPSEEK | [官方News/研究索引](https://www.deepseek.com/news/)实际显示研究06/24→02/25、动态09/10→04/24跨过本窗；仅核这两相邻日期边界，不读取其他日正文 | 已检查 | 查看全部为动态控件，当前可读目录切片不保证未列出或已删除事件 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)完整Overview26入口最新2025/11/07；[官方organization](https://github.com/MoonshotAI)核实legacy kimi-cli与kimi-code是两项目。kimi-code官方release API page1/per_page100返回81项（至05/26），仅提取目标窗和相邻metadata，0.6.0=05/29 14:24:54Z→0.7.0=06/02 02:23:53Z跨窗；legacy首release页1.47.0=06/05 10:35:01Z→1.46.0=05/29 05:56:52Z跨窗，停止 | 已检查 | 0.7.0是06/02 10:23:53BJT，窗外，不扩读PR或移入本日；release保留列表不证明已删除事件与整个organization零新材料，静态blog仍有保留局限 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)两次超时且浏览器不可用；从该页实际公开JS的Blog→publicList调用恢复[官方公共目录](https://api.hunyuan.tencent.com/api/blog/publicList)，pageNum1/pageSize100/renderType0，totalNum9/list9读完，仅核日期与标题；显示时间07/07→04/30跨窗，publicAt也无本窗项 | 已检查 | 当前英文9项公共目录不保证已删/未列/其他语言目录；publicAt与displayPublishTime不同均保留，不将显示日一律当首公开 |
| SRC-ZAI | [Research“全部”时间排序](https://www.zhipuai.cn/zh/research)实际读06/16 GLM5.2→05/20 ZCube相邻边界，已越过本窗，停止 | 已检查 | 当前官方目录不证明历史删除项；无需读取该两篇窗外正文 |
| SRC-BYTEDANCE-SEED | [论文目录第1/13页](https://seed.bytedance.com/en/public_papers)实际06/03 MetaPoint→05/29跨窗，停在05/29，不读下一页。Blog实际五类目录：foundation06/19→02/16、visual07/08→04/23、audio07/20→04/09、ai-infra最新2025/08/14、frontier07/07→2025/12/02，均至窗前停止，未读窗外正文 | 已检查 | 当前目录保留不证明已删除事件；未泛扫AI for Science或其余242论文 |
| SRC-BAIDU-ERNIE | [中文Blog](https://ernie.baidu.com/blog/zh/)实际第1/2页最新05/09、以下均更早到2025/11；已越过本窗，停止，不读更老第2页 | 已检查 | 可读blog目录中无本窗；不声称所有项目release无遗漏 |
| SRC-XIAOMI-MIMO | [首页Paper](https://mimo.xiaomi.com/)实际06/29→03/13跨窗；Blog15标题无日期，从页面公开4752.2908c99e.js恢复route metadata，具日期相邻06/08 UltraSpeed→05/30 inference跨窗；两轮限定官方域June1/2搜索无结果。未逐篇展开其余未标日期custom页面 | 受阻 | 无日期Blog条目仍不能证明本窗事件覆盖；有界入口已穷尽为隔离保留，不支撑零/正面采用。重开需相应官方页面first-public日期或完整日期目录 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)06/09→06/01 M3→05/27；[中文Blog](https://www.minimax.cn/blog)06/09→06/01 M3→05/25，均读至窗前停止。M3[原页](https://www.minimax.io/blog/minimax-m3)JSON-LD datePublished=2026-05-31T17:31:18.000Z，即06/01 01:31:18BJT窗前；[Agent TechBlog](https://agent.minimax.io/docs/techblog)及其[官方llms目录](https://agent.minimax.io/docs/llms.txt)仅列Agent Team已知窗前家族，不移入 | 已检查 | 当前Blog与TechBlog目录不证明历史删改无遗漏；无时间的Tech文档不作本窗新事件 |
| SRC-ARXIV | 旧canonical raw是1,449身份/19分类宽发现，仅作具名恢复，不扩池；旧51 owner receipt及七批笔记可定位精确版本。旧Atom为0字节。实际有限访问官方旧日入口与月列表：短2606为404/Invalid Year，正确[2026-06 cs.CL月列表](https://arxiv.org/list/cs.CL/2026-06?skip=0&show=2000)有条目但无daily公告headers，未浏览整月题摘；官方advanced公告日期仅年月粒度。定点00944 DataCite字段保留Submitted05/31 01:19:03Z、Updated v1 06/02 00:54:21Z、Available2026-06、Created04:03:34Z | 受阻 | historical公告批次与本窗主题覆盖不能恢复。DataCite Created不是公开，Updated也不是Available；normal schedule只给最早可能，不证明无hold或公开上界。110旧表及六恢复具名项均DateHold，不作本窗正面证据、Books或零命中依据。重开需当日官方批次/带时区公开receipt，或provider明确字段代表已公开的定义 |


## 3. 候选与判断

本轮确定的当窗候选：无已核准项。不是零命中声明；arXiv真实公告归属无法恢复，不能先列统一08–09范围。110旧家族的标题、精确版本、旧拟贡献/分数与owner定位保留在[具名DateHold清单](../_sources/daily-20260602/V3_RECOVERY_BLOCKERS.md#110旧工作家族具名datehold清单)，未作当窗候选或正面采用。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

## 4. 证据与知识整合

六项必要恢复按原问题→具体增量→反证→actual owner记录在[同一packet](../_sources/daily-20260602/V3_RECOVERY_BLOCKERS.md)，可供后续真实归属日定点复用，不代表本日正式入选或全部110已经审阅：

- [PRISM 2606.00944v1](https://arxiv.org/html/2606.00944v1)：切空间clip/noise的窄结果与一般GL adaptive更新的可行反例分开；Ch30拟缺口成立方向经root有限源核，日期未准，不写。
- [OALM 2606.00997v1](https://arxiv.org/html/2606.00997v1)：固定target次序改变log-product与variance的二轴诊断；理论有固定product/凹性条件，IFEval低variance反例及p>.05不能删。Ch24拟缺口未作本日采用。
- [Auto-formalization 2606.00981v1](https://arxiv.org/html/2606.00981v1)：IR faithfulness、compiler/solver分账与running resource保留；C3叙述/Table16不一致，简化Robo不能外推真实Robotouille。拟Ch79，未写。
- [LocalMixVR 2606.01128v1](https://arxiv.org/html/2606.01128v1)：共同分布/凸性与三项误差界下同步对象含耦合gradient correction；理论与gamma=.95实验配方不同，F中间1/M公式未决不用于更强保证。拟Ch36，未写。
- [RoboTrustBench 2606.01600v1](https://arxiv.org/html/2606.01600v1)：可行/不可行任务completion评价方向不同，三guardrail非返回排除影响分母；仅180人工子集、离线视频，不是闭环控制安全率。拟Ch25，未写。
- [Skill issues 2606.01185v1](https://arxiv.org/html/2606.01185v1)：trace/commit/state/final response分层验收与skills组合失败；25任务、四技能31.9%平均改善、两multi-skill未改善，不使用v2数字。root对读exact-v1 §3.1/3.2.2/Table1/§4与实际Ch81:292–298、Ch66:282–344，确认长期命题已有覆盖，可复用No Change判断；日期未准，不计本轮候选或已有覆盖产出。

[旧110具体证据定位](../_sources/daily-20260602/V3_RECOVERY_BLOCKERS.md#旧110证据与采用定位仅为待核过程记录)及原七批/44项存档保留；其旧完成、标准/深入与整合措辞仅历史记录，不等于本次读完或验收。当前无June02新Books修改，因此无本輪新写后成果。

## 5. 缺口与下一步

普通可执行工作：无。root非作者已完成本次限定安全终态复核；作者已同步结果与状态，不等待材料无限重试，不新discover或第三轮全文。

本窗终态保留：

- arXiv 110旧工作家族及00944/00997/00981/01128/01600/01185：缺官方本窗New/重要revision公告或可证公开时刻。Submitted+normal schedule只约束最早可能；DataCite Updated是资源更新，Available仅月份，不能构造[08,09)上界。已有限访问日入口、正确monthly/advanced与具名元数据；当前不能采用/计入正式候选。替代为当天官方公告/首公开正文可访问receipt，或arXiv明确Updated字段公开语义；只重开对应家族日期与依赖采用链，不重读有效机制。
- Google Research/Qwen/MiMo：具体历史目录与未标日期Blog缺口如§2，空搜索/动态壳不算零命中。需目标窗官方目录或带时区事件原文，届时只恢复该来源/事件；不支持本次候选与Books断言。
- PRISM一般GL adaptive保证、Auto-formalization矛盾数字、LocalMixVR中间公式：具体位置及支持/未支持命题见packet，中央保证或冲突数值不作正面证据；重开需作者勘误或直接必要证明，不靠有限跑分消除反例。尚待读的材料不冒充外部故障。

窗外线索：Kimi Code0.7.0官方published_at=2026-06-02T02:23:53Z（10:23:53BJT）在本窗结束之后，仅日期去重；不展开PR、不归本日、不阻塞本窗。

## 6. 复核

复核者：root（本轮非作者）

结论：通过

root实际检查最终六部分、14来源具体查询与停止范围及四项缺口、110行110唯一身份全部DateHold与六恢复身份不重叠（共116）、无本轮正面采用以及旧采用链未经此次验收的边界。root重新打开DataCite dateType、arXiv advanced/月目录，结合现有必要来源确认没有公开上界；独立恢复Seed论文目录06/03→05/29、Baidu最新05/09、Hunyuan公共列表9项验证有限停止，不扩窗外正文。六必要包保留机制与关键反证，前五有效必要源核复用；Skill issues exact-v1 §3.1/3.2.2/Table1/§4及上述实际owner对读通过长期已有覆盖判断，但日期未准仍不计候选。作者已清除正式110候选/08–09合成归属与本轮110Evidence/Books完成声明。

本次通过限定为安全隔离终态：116终态日期保留，无已核准当窗候选，旧32I本轮不验收；不是1449全题摘、全110全文、全116证据或Books采用通过。所有日期/目录及中央争议精确重开条件见§5，普通0。

当前V3机械校验与本轮两文件限定diff-check通过，仅检查可判定一致性，不替代上述语义复核。未stage、commit、push或执行破坏性操作；dirty/staged及其他日期/书稿保留。
