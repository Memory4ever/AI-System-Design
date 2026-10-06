# Daily Research — 2026-02-09

**规范：** V3
**窗口：** 2026-02-08T09:00:00+08:00 ～ 2026-02-09T09:00:00+08:00
**补充窗口：** 2026-02-08 ～ 2026-02-08
**窗口说明：** 用户授权只补来源遗漏，保留原窗口、旧候选日期/评分与有效审阅；新增按前一北京时间自然日date-only，旧材料只去重，不搬移归属。
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-08T13:15:01+08:00

## 1. 结论

本窗确定候选 1 个唯一材料家族：Kimi Code VSCode 1.8.0 的错 MCP 目标用户报告。已完成标准审阅，并针对目标绑定的安全边界定点加深；结果仅支持未复现的用户观察，不支持已确证实现缺陷或生产安全结论。Books 决定为仅报告，实际改书 0。

14 个每日来源及实际触发的 Kimi issue 原源已做有限检查。arXiv 官方常规公告在本窗没有发布时槽；不能由此推断作者网站也无发布。Seed SAGE 完整题摘显示潜在贡献，但作者目录只有相交日级标签，必要首公开时间无法确定，隔离、不评分、不算正式候选。多个机构历史目录不能完整恢复，不算正面 Coverage、零事件或“无遗漏”证明。原始宽列表只用于发现，没有逐项全文队列。root 独立最终复核通过，可执行普通待办 0；旧 V2.1 空候选和完成标签未用于本轮验收。

2026-10-08增量补查：原1候选与连续§4冻结，补窗确定新增0，合计仍1。TSR-Adam完整题摘显示通信设计潜在增量，但必要公开日期未证，隔离而不评分/提前深审；MoE综述与Qwen用户图像编辑报告具名关闭。新增Books写入0；下表原审阅仍有效，但原完成不代替本轮补查验收。有限来源/筛选及root独立日级验收已完成，普通可执行待办0，来源/日期保留不授全Coverage、Evidence或无遗漏；详见[本次记录](../_sources/daily-20260209/supplement-20261008.md)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)与[官方 RSS](https://openai.com/news/rss.xml)；RSS 1245 项仅取本窗及邻近日期，前后为 Feb06 10:00 GMT、Feb09 11:00 GMT；[字段记录](../_sources/daily-20260209/feb09_stage7_1.txt) | 已检查 | 不保证 RSS 外修订或未收录事件 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)当前首屏及域内 Feb08/09 日期线索；定点[zero-days 原文](https://www.anthropic.com/research/zero-days)核更正说明，标注 Feb06 作者列表更正，非本窗新安全事件；[记录](../_sources/daily-20260209/feb09_stage4_1.txt) | 受阻 | 历史研究及 card 修订完整日期切片未恢复；不以搜索零命中补齐 |
| SRC-GOOGLE-AI | [Research pubs](https://research.google/pubs/)首屏、[2026/02 Blog](https://research.google/blog/2026/02/) 7 项日期目录、[DeepMind Blog page4](https://deepmind.google/blog/page/4/)相邻 Jan/Feb 切片；[原始切片](../_sources/daily-20260209/feb09_google_native_slice.txt) | 已检查 | pubs 历史首次公开及目录外修订未恢复，不保证全部事件 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)空提取；仅域内本日日期主题补检，未得到可核窗内原事件；[记录](../_sources/daily-20260209/feb09_stage2_3.txt) | 受阻 | 动态历史目录及公开日期缺失 |
| SRC-QWEN | [旧站](https://qwenlm.github.io/)末项 Sep2025并转[新站](https://qwen.ai/)、blog/research 动态页面；原页面及本日域内补检；[记录](../_sources/daily-20260209/feb09_stage6_1.txt) | 受阻 | 新动态历史条目及日期未提取，不能据空页记无发布 |
| SRC-DEEPSEEK | [官网](https://www.deepseek.com/)当前模型/报告链接；原 HTML无日期字段；updates 超时，news 实为 API入门页，停止错误入口；[记录](../_sources/daily-20260209/feb09_stage5_0.txt) | 受阻 | 当前链接不能恢复本窗历史公开/修订切片 |
| SRC-MOONSHOT | [Blog](https://platform.kimi.com/blog) 26 个当前条目止于 Nov2025；[CLI 1.9.0](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.9.0) API published_at 为 Feb06 18:38:03Z，窗前；本日日期线索定点回 GitHub issue 核核心；[记录](../_sources/daily-20260209/feb09_stage7_1.txt) | 已检查 | 当前 Blog/release首页不证明全部历史事件完整 |
| SRC-TENCENT-HUNYUAN | [Research 首查](https://hunyuan.tencent.com/research)动态空提取；浏览器两次超时及子线程 visibility 限制后，从公开 bundle 恢复 publicList。POST pageNum1/pageSize12/renderType0，zh 返回11项/total11；相邻日期 Feb03与Feb13；[字段](../_sources/daily-20260209/feb09_hunyuan_native.txt) | 已检查 | 英文9项与中文11项不同；current all不等于历史所有事件或删除/修订档案 |
| SRC-ZAI | [Research 首查](https://www.zhipuai.cn/zh/research)当前15卡片，相关日期以Feb02 GLM-OCR与Feb11 GLM5夹住本窗；[记录](../_sources/daily-20260209/feb09_stage2_0.txt) | 已检查 | 非完整 release/RFC或目录外历史修订证明 |
| SRC-BYTEDANCE-SEED | [Research/public_papers](https://seed.bytedance.com/en/research)公开原生 get_article_list_v2，x-tt-locale:US，2026 type1仅定点token60/80，返回19/2、total82、尾页has_more=false；type2 token0返回14、total19、has_more=false；[字段/停点](../_sources/daily-20260209/feb09_stage7_0.txt)、[SAGE完整AB](../_sources/daily-20260209/feb09_stage8_1.txt) | 受阻 | Publication19/20与Blog14/19差额未解释，不能授完整目录；日标签不证明首次公开时刻 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)第一页10项至Nov2025，Feb06 ERNIE5与Apr15后项相邻，停止于已有夹窗切片；[记录](../_sources/daily-20260209/feb09_stage2_1.txt) | 已检查 | 不涵盖目录外代码/报告修订 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)当前15卡片与原HTML无可恢复发布日期，本日域内查询未得原事件；[记录](../_sources/daily-20260209/feb09_stage3_0.txt) | 受阻 | 历史首公开与修订时刻不明 |
| SRC-MINIMAX | [English Blog](https://www.minimax.io/blog)11项当前列表，Jan27与Feb12/14夹住窗口；中文跳转页及[Agent Tech Blog](https://agent.minimax.io/docs/techblog)仅最小索引；[记录](../_sources/daily-20260209/feb09_stage2_1.txt) | 受阻 | Agent历史技术条目/日期不能由主Blog无卡片代替 |
| SRC-ARXIV | [官方 Announcement Schedule](https://info.arxiv.org/help/availability.html#announcement-schedule)：Friday/Saturday无公告，Sunday Feb08 20:00 EST=Feb09 09:00 BJT，恰为排除的右边界；规则覆盖常规new/replacement/withdrawal/cross-list；[原文](../_sources/daily-20260209/feb09_primary_initial_0.txt) | 已检查 | 不等于 Submitted 查询或全网首公开为0；具体 SAGE按原事件另隔离 |
| 表外：[MoonshotAI/kimi-agent-sdk issues](https://github.com/MoonshotAI/kimi-agent-sdk/issues/84) | 由每日Moonshot本日补检触发；读 #84完整核心、GitHub API精确created_at及当前0评论；[字段](../_sources/daily-20260209/feb09_stage5_0.txt)、[原正文](../_sources/daily-20260209/feb09_stage9_0.txt) | 已检查 | 用户报告未独立复现/维护者确认，不证明原因层 |
| 补检：[Web 域内检索](https://www.google.com/) | 各每日域限定Feb08/09及模型、训练、推理、Agent主题；[查询与结果](../_sources/daily-20260209/feb09_stage3_0.txt)只作定位。搜索命中的旧论文、哲学论坛、UI建议不转全量队列 | 检索受限 | 日期搜索及排名/摘要不证明历史覆盖、原始公开或缺陷成立 |

本轮补窗实际来源切片（不替换上表原观察，完整查询/原入口与停止点见[增量来源记录](../_sources/daily-20260209/supplement-20261008.md)）：

- SRC-OPENAI：Research首屏、官方RSS仅抽Feb06～10相邻事件；[字段](../_sources/daily-20260209/supplement-20261008-tail-fields-2.txt)只见Feb06/09；已检查，不授RSS外历史修订覆盖。
- SRC-ANTHROPIC：Research当前首屏、Feb08域内主题及zero-days原更正定点复查；[记录](../_sources/daily-20260209/supplement-20261008-specific-date.json)；受阻，完整Feb08历史/card切片未恢复，不以零搜索关闭。
- SRC-GOOGLE-AI：pubs首屏、2026/02 Blog全7日期项（Feb05/09夹窗）、DeepMind page4 Jan/Feb相邻切片；已检查，pubs首公开、DeepMind月标签及目录外修订非完整证明。
- SRC-META-AI：Research首屏空提取及Feb08域内主题；[原件](../_sources/daily-20260209/supplement-20261008-native-1.json)；受阻，动态历史切片/日期未恢复。
- SRC-QWEN：旧站转新blog空提取后，root DAY指出有限入口；本日实际GET `api/v2/article/retrieval?type=qwen_ai&language=en-US`仅投影40个title+extra.date，[原字段](../_sources/daily-20260209/supplement-20261008-qwen-native-dates.json)，Feb03 Coder-Next/Feb10 Image2.0夹Feb08；已检查有限元数据，不展开body，不授目录外历史修订。#2064为BJT Feb07观察、无Feb08新纠错，不作候选。
- SRC-DEEPSEEK：官网无日期后，本日实际恢复[news原页](../_sources/daily-20260209/supplement-20261008-deepseek-native-dates.json)5动态+10研究共15日期项及[HTML字段](../_sources/daily-20260209/supplement-20261008-deepseek-html-metadata.txt)，研究Jan28/Feb25、动态Dec01/Apr24夹Feb08；已检查有限目录，不展开15正文，不授“查看全部”及目录外修订覆盖。
- SRC-MOONSHOT：Blog当前26项止Nov2025、#84 API/body/created/updated/comments0精确复用；[字段](../_sources/daily-20260209/supplement-20261008-native-fields-3.json)；已检查，原同事件不新增家族，当前目录不保证全部历史。
- SRC-TENCENT-HUNYUAN：Research首查空，浏览器超时；POST publicList pageNum1/pageSize12/renderType0/zh，返回11/total11，Feb03/13夹窗；[字段](../_sources/daily-20260209/supplement-20261008-native-fields-0.json)；已检查，原en9/zh11差异和历史删除/修订限制保留。
- SRC-ZAI：Research当前15卡片，Feb02 GLM-OCR与Feb11 GLM5相邻；[原件](../_sources/daily-20260209/supplement-20261008-native-1.json)；已检查，非目录外所有事件保证。
- SRC-BYTEDANCE-SEED：原生US/type1 token60/80返回19/2,total82,尾has_morefalse；type2 token0返回14,total19,has_morefalse；[字段](../_sources/daily-20260209/supplement-20261008-finite-recovery-0.txt)；受阻，19/20、14/19差额保留；SAGE/Protenix为Feb09目录标签，非Feb08新增。
- SRC-BAIDU-ERNIE：Blog第一页10项，Feb06/Apr15相邻，止Nov2025；[原件](../_sources/daily-20260209/supplement-20261008-native-2.json)；已检查，不授目录外代码/报告修订覆盖。
- SRC-XIAOMI-MIMO：当前Paper8项现带日期：HySparse Feb03、ARL Mar13夹窗；Blog15卡片；[原件](../_sources/daily-20260209/supplement-20261008-native-2.json)；受阻，Paper当前日期观察有效，Blog历史日期仍缺。
- SRC-MINIMAX：英当前12项Jan27/Feb12夹窗、中13项Jan28/Feb12夹窗与Agent最小索引；[原件](../_sources/daily-20260209/supplement-20261008-native-tail.json)；受阻，Agent历史条目/日期仍缺，英中日期不同不授全历史。
- SRC-ARXIV：官方公告规则及两轮各四主题/同义词Feb08日期查询；[记录](../_sources/daily-20260209/supplement-20261008-themes.json)、[标题边界](../_sources/daily-20260209/supplement-20261008-bounded-titles.json)；受阻，Sunday无常规时槽只是背景；CL/DC列表Cache miss、AI月首25非目标日而止，不作全网零发布/全学科召回。
- 表外：[TSR-Adam作者代码](https://github.com/DKmiyan/TSR-Adam)：具体摘要链接触发，repo身份与4commit、Jan28 README仅作日期恢复，未深审代码机制；受阻，Jan28代码提交不证明论文首次公开；Feb08公开日期缺，精确隔离。
- 表外：[Qwen #2064](https://github.com/QwenLM/Qwen/issues/2064)：具体日期主题命中，完整body/API及1条Mar09 inactive-bot评论；[字段](../_sources/daily-20260209/supplement-20261008-tail-fields-0.txt)；已检查，窗前用户质量/UI观察无新机制/因果对照，具名关闭；非所有Qwen issues扫描。

## 3. 候选与判断

本次Feb08自然日补查不新增确定候选；原候选行逐字保留。完整题摘、查询/停止、具名关闭和TSR日期请求见[补查记录](../_sources/daily-20260209/supplement-20261008.md)。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kimi Code VSCode: Incorrect MCP reference when multiple Supabase MCPs have similar config #84](https://github.com/MoonshotAI/kimi-agent-sdk/issues/84) | 2026-02-08T11:06:18+08:00 | 相似MCP配置仍需保持目标隔离 → 用户报告1.8.0中指定RSX却调用FMMS且CLI反侧正常 → 应定点核模型选择到具体server目标的绑定；2 + 1 + 2 = 5（未证实版本信号的局部价值，不借用通用权限原则抬分） | 标准完成 | 仅报告 |

## 4. 证据与知识整合

### [Kimi Code VSCode: Incorrect MCP reference when multiple Supabase MCPs have similar config #84](https://github.com/MoonshotAI/kimi-agent-sdk/issues/84)

精确材料为本次取得的 issue正文/API快照。API `created_at=2026-02-08T03:06:18Z`，UTC秒精度，换算为窗内11:06:18北京时间；这是用户报告公开事件，不是1.8.0版本发布时间。核心位置为 Describe the bug、To Reproduce、Environment、Configuration Example、Additional context；[原字段与正文](../_sources/daily-20260209/feb09_stage5_0.txt)。

用户称两个不同名字的Supabase MCP命令/参数结构相同，仅project-ref不同；指定一个却引用另一个，而CLI没有同样问题。公开配置使用占位项目与token，没有真实call trace、server返回的资源身份、独立重跑或可核扩展实现路径。当前open、comments0也不能当作维护者认可。以上只确定报告内容和其可检验条件，无法把原因归到模型选名、Host注册去重、dispatch映射或下游服务；未证明数据泄露、写错目标或安全修复。

本次安全定点加深只处理“指定名字不能自动证明实际目标绑定”的采用边界，不审无关SDK附录或整个revision史。自己的设计推断是：若复现，须对照model proposal、注册server identity、dispatch配置及返回资源身份，而不能只观察工具显示名。它不是原文已实现的新机制或本次完成的测试；性能、硬件、batch/SLO与benchmark不适用，扩展构建版本/MCP解析版本与重复运行均未披露。

Books上下文及邻接已读取。[AGENT-TOOL-CALLING Ch78](../../../../books/part-07-agent/78-tool-calling.md#tool-contract)已要求tool identity/version，并在“模型输出只是Proposal”中独立做目标资源semantic validation；[AGENT-MCP Ch83](../../../../books/part-07-agent/83-mcp.md#lifecycle-与-version-contract)实际要求tool/resource绑定server identity与version，Host/Client/Server段拥有aggregation/isolation，协议比较段区分配置来源、连接和动作执行者。#84没有可核因果或新绑定设计，不能把通用现有边界重写为已证实新反例。因此仅报告，而非“已有覆盖的新增实证”或整合。实际Books diff为0；若维护者提供具体实现定位和复现证据，仅重新审这条采用链。

## 5. 缺口与下一步

本轮补查可执行普通待办：无。原SAGE保留项/原时间窗口冻结，但其官方目录Feb09日标签不属于新增Feb08补窗；本次不要求精确时刻、不把Submitted冒作公开日、不新建SAGE待办。

- 新增终态日期保留：[TSR-Adam 2602.08007v1](https://arxiv.org/abs/2602.08007v1)完整题摘的双边r² core同步、randomized-SVD refresh与embedding单独预算有具体通信设计潜力；官方[v1] Feb08仅为Submitted，作者repo Jan28创建/4提交Jan28或May07且Jan28 README只有代码训练示例，无Feb08论文公开正文。[原题摘与字段](../_sources/daily-20260209/supplement-20261008-core-fields.json)、[有限commit日期](../_sources/daily-20260209/supplement-20261008-finite-recovery-2.txt)。需要同稿作者公开正文日期或官方公开公告批次；当前不能确定落补窗，不评分、不深审、不Books、不支持Coverage/无遗漏。到达后只重开TSR身份/日期，确认Feb08才正式准入。
- 本次来源限制继续隔离：Anthropic/Meta完整历史切片、Qwen/DeepSeek已恢复有限日期目录以外的删除/改写/修订事件、MiMo Blog日期、MiniMax Agent目录日期未恢复；Seed type1返回19/20与type2返回14/19差额仍未解释；CL/DC有限列表Cache miss，AI月首25标题不是目标日切片，停止而不扩整月队列。只要求各来源Feb08日期档案/具体原材料或官方分页解释，不以搜索零命中、现有目录无卡片或Sunday无常规公告证明所有发布为0。

可执行普通待办：无。以下仅为本窗已隔离的外部保留项，按具体重开条件恢复，不扩扫其他日期。

本窗终态保留项不用于正面证据、Books、Coverage 或无遗漏断言；以下保留具体定点重开条件：

- [SAGE 2602.08354v1](https://arxiv.org/abs/2602.08354v1)：完整题摘的停止采样与混合group-RL潜在增量明确；Seed id1608 `PublishDate=1770566400000`只表示目录Feb09日标签（BJT整天与窗口仅相交），不把编码午夜补造成发布时刻。原始arXiv字段 `[v1] Mon, 9 Feb 2026 07:38:22 UTC`为Submitted，已在本窗后15:38:22BJT，不能反推此前作者网站首公开。作者页有限恢复失败，目录UpdateTime=1782898439000为后来的更新时间而非首次公开证明；[字段](../_sources/daily-20260209/feb09_stage8_1.txt)、[精确v1题摘和history](../_sources/daily-20260209/feb09_stage9_0.txt)。需要同稿作者公开正文及有时区的首次公开时刻/完全落窗范围或公开存档；到达后只重开SAGE日期与归属，确认落窗才正式准入/评分。窗外arXiv公告应在真实归属日恢复，不在这里深审。
- Anthropic、Meta、Qwen、DeepSeek、MiMo的历史切片/版本日期及MiniMax Agent子目录无法完整恢复，现已尝试原入口、邻近日期域内查询及可用公开元数据。替代为对应官方日期档案/RSS、带时间的发布说明或具体材料链接；只重开该来源本窗缺段，不补扫整月。
- Seed publication/blog返回数量差额，以及Google pubs与各当前目录未涵盖删除/改写事件的限制：需要官方过滤/分页解释或本窗历史档案；当前切片只支持表内所述观察。Hunyuan zh11/en9表示语言目录差异，本次两语言可见条目没有本窗日期，不能推出历史所有事件或日级标签就是first-public。
- #84未证明的机制不作为普通“等待复现”无限待办；当前只采用报告身份与未核信号。若有维护者确认、真实调用/资源身份与控制变量复现，重开该版本原因层及必要Books判断。

具名贡献前关闭保存在[筛选说明](../_sources/daily-20260209/FILTER_NOTES.md)：Kimi #1042独立context子代理请求、#1053自动标题UI；#1041单站Fetch缓存抱怨缺新机制/因果证据；Seed Protenix-v1、Google鸟类模型水下声学及DeepMind科学发现入口均按AI for Science暂停，不借通用节点重新收录。日期不会改变这些明确关闭理由，不补造时刻。

## 6. 复核

本次2026-10-08补查复核：

复核者：root（独立于本轮作者supplement_20260209）。
结论：通过

root实际读全部六部分增量、14源范围/四主题停止点、TSR/MoE两完整题摘及关闭理由、#84未变API/body去重复用、Qwen40及DeepSeek15日期原件。首轮发现Qwen/DeepSeek可执行有限入口，已实际恢复并解决，不把可执行差额当外部终态。准入/代表关闭独立样本为TSR与MoE2项；Qwen #2064及窗外具名线索的作者题摘/核心理由随六部分记录检查，不称独立全量复读。没有无差别重读所有旧附件。TSR未知公开日不评分/提前深审，Sunday排程/Submitted不授零发布；原1候选/评分/日期/窗口/连续§4冻结、新0/Books0、无新PRE/POST对象，其他有效层复用。通过的是安全终态，不授目录外/日期保留全Coverage、Evidence或无遗漏。

本轮实际完成态V3结构校验通过，README/补查记录75个本地引用无缺失，原候选行/原窗口/整个连续§4逐字比较通过；本日限定cached/unstaged diff-check通过。机器检查不替代以上root语义验收。没有新Books写入/新PRE-POST对象，未stage、commit、push，本日作者结束、不接下一日。

以下为冻结有效的原审阅复核，不以旧通过替代本轮验收。

复核者：root（独立于作者 feb09_fresh）。
结论：通过

root 实际顺读六部分，核唯一候选 #84（1/1）的 API/body、当前无评论与未复现采用边界；实际读 Ch78 Tool Contract/目标资源 semantic validation 和 Ch83 server identity/version、Host isolation，确认仅报告、不写书。带正确性反例信号的 #1041（1/1）已读完整核心，未提供新机制或因果证据，关闭成立。普通排除分层核 #1042/#1053 两项请求/UI、Protenix/Perch 两项科学范围，共4/5具名普通排除；未单独复核DeepMind科学发现条目的所有正文附件，不把抽检称全量。SAGE完整题摘/日期字段与隔离决定已核。

有限14来源的入口/停止表、Hunyuan原JSON、RSS/月目录、arXiv时槽与外部缺口已核；未无差别重读全部附件，也未复原全历史目录。首批准入校准与最终复核合并计入此范围。通过的是本窗安全终态，不是给日期/目录缺口授正面Coverage、Evidence或无遗漏保证。

完成态 V3 validator、Markdown/本地引用与限定cached/unstaged diff-check通过；机器校验不替代上述语义验收。未stage、commit、push，未改共享Books/索引/LEARNING_STATE。本日作者结束，不接下一日。
