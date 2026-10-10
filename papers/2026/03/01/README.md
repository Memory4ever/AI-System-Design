# Daily Research — 2026-03-01

**规范：** V3
**窗口：** 2026-02-28T09:00:00+08:00 ～ 2026-03-01T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-08T22:07:56+08:00
**窗口说明：** 用户授权保留旧窗口和既有候选日期，仅补来源遗漏；原完成声明与旧日期推导冻结复用，不作为本轮新增证明。
**补充窗口：** 2026-02-28 ～ 2026-02-28

## 1. 结论

2026-10-08补查完成：14每日源按本自然日有限查询/分页停点补查；103个arXiv邻域身份只是查漏线索，不是当天公开命中或全量题摘队列。新增确定候选0，旧1家族及其评分/日期/有效Source/Books判断逐字保留；45份完整相关题摘具备贡献潜力但必要首公开日未证，已一次原入口恢复后逐项外部隔离。Social-JEPA当前官方撤回，退出采用链路；TraceSIR一次必要core后具体关闭贡献。没有新增必要证据审阅/Books写入，不把旧OP1窄审重复计数。root本轮独立准入与六部分DAY实际通过，普通待办0；完成不授全Coverage/Evidence或无遗漏，未继承旧通过标签。

确定落窗候选为1家族，按安全部署约束变化完成窄深入审阅后仅报告；必要 Books 整合为0。14每日源均有限检查；OpenAI官方RSS恢复了本窗公告确时，其他目录/日期限制见§2/§5。非作者最终复核通过，普通待办为0；外部保留项不算正面覆盖或证据通过。

arXiv 常规日程在本窗无批次；Submitted、DOI registration、旧宽月份库存均不能补造 first-public。特殊延期/非例行批次历史不能排除。旧 EffectiveDate 豁免、9分、分母、Complete 标签不作为本轮判断，没有参考 Weekly。

OpenAI 2/28 公告披露云端部署及厂商保留安全栈控制权。RSS原字段给出02/28T12:30GMT，即北京时间20:30，落窗；当前正文以更新分隔线区分3/2后加措辞，后者不回填。本次只确认厂商公开的配置/责任声明，没有技术有效性证据，不形成Books机制增量。

## 2. 来源覆盖

2026-10-08新增实际查询、原响应/执行时间/分页与停止见[本日补查记录](../_sources/daily-20260301/SUPPLEMENT_QUERIES_20261008.md)和[首响应记录](../_sources/daily-20260301/SUP_FETCH_20261008.json)。表中旧检查描述仅冻结复用；补查描述才是本轮实际范围。旧CH11不因当前EN9而自动获得历史完整性。

实际主题、查询、首次响应和停止点见 [V3 查询记录](../_sources/daily-20260301/V3_QUERY_STOPPOINTS.md)；原始响应为本日 V3_RAW 文件。搜索空返、首页与年份表均不证明无遗漏，“已检查”仅指具名有限日期目录段。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| [SRC-OPENAI](https://openai.com/research/) | Research/Index失败后root实际curl[官方RSS](https://openai.com/news/rss.xml)，本窗1公告，pubDate原值见[日期恢复](../_sources/daily-20260306/V3_OPENAI_RSS_ROOT_RECOVERY.md)；原文更新分隔线下2/28正文与FAQ必要段已核；补查：实际本日官方RSS按北京时间2/28筛出仅旧OP1；当前事件页只看显式update信号仍3/2，不重审原有效必要正文 | 已检查 | RSS公开日期段已恢复；D1仅保留未列入feed的隐藏历史事件，不能授全机构无遗漏 |
| [SRC-ANTHROPIC](https://www.anthropic.com/research) | Research首10项，See more仍返回同页；窗口日期域查询首批；补查：Research首10项到9/4、See more未恢复历史；本窗日期域搜索首结果无新具名线索即止，不以空搜判零 | 受阻 | D2历史分页不可枚举，不能由无搜索命中推零研究。 |
| [SRC-GOOGLE-AI](https://deepmind.google/research/) | DeepMind blog page3跨二～三月，2/19及2/26 card；publications page12实际仍当前六月以上；Google Research pubs年级2026表及窗口域查询；补查：Research首页与pubs?year=2026首年级表；root RSS原XML100项本日有限浏览，BJT2/27→3/4跨本自然日无feed条目；不代替Pubs历史 | 受阻 | D3论文目录日级历史未恢复；年级表不扩成全文队列。 |
| [SRC-META-AI](https://ai.meta.com/research/) | 原入口提取0行，窗口域查询首批仅恢复旧主题页；补查：research取得动态shell；日期域首结果为旧年个人页/Blog，不扫全年题摘；无可枚举本日历史 | 受阻 | D4动态research历史目录；空提取不是零事件。 |
| [SRC-QWEN](https://qwenlm.github.io/) | 旧博客redirect至qwen.ai/blog，新站提取0行；日期域查询首批；补查：qwen.ai/blog动态shell、本日日期域首搜索无新具名线索；不以旧2025页面代表2026 | 受阻 | D5新站动态历史目录；旧站2025页不代替2026覆盖。 |
| [SRC-DEEPSEEK](https://www.deepseek.com/en/news/) | root补开官方Research & News；Research Index可见10项至2025/05/14，2/25 DualPath→6/24 V4跨过本窗；原updates两次timeout保留；补查：/en/research实404后/en/news/实际恢复10项ResearchIndex，2/25→6/24越过本日；停止2025末项 | 已检查 | 可见研究目录本窗段无条目；D6仅保留News隐藏View All与API updates历史限制，不外推全机构。 |
| [SRC-MOONSHOT](https://www.kimi.com/en/blog/) | root补开官方Research完整可见19项至2024/06/26，2/9 Agent Swarm→4/20 K2.6跨过本窗；补查：/en/research重定向产品主页后实际/en/blog/Research19项，2/9→4/20越过本日；不把产品首页当日期目录 | 已检查 | 当前可见研究目录无本窗条目；原platform博客止于2025不再充当2026目录不可恢复依据，撤销D7。 |
| [SRC-TENCENT-HUNYUAN](https://hunyuan.tencent.com/research) | 网页/浏览器失败后root按官方脚本生产publicList/renderType0,page1,size20恢复；total11/返回11，全可见目录已读；显示日期2/13→4/23跨过本窗，见[原始恢复](../_sources/V3_HUNYUAN_LIST_RECOVERY.md)；补查：本日POST publicList pageNum1/pageSize1000/renderType0，total9/list9全EN，2/13→4/23跨本日；动态CH浏览器初建/绑定两次timeout即止 | 受阻 | 当前可见目录无本窗条目，不证明未删除条目/全机构历史。D8撤销；browser失败过程保留；补查EN9仅有限EN范围，CH历史未恢复，不继承旧CH11为本轮完整证明。 |
| [SRC-ZAI](https://www.zhipuai.cn/zh/research) | Research全部可见列表8/26→2025/12/09，2/21 GLM-5报告→3/15 GLM-5-Turbo；release notes读至2025/07/15；补查：Research可见3/15→2/21越本自然日并到2025/12/09止，不把旧GLM5报告重审 | 已检查 | 可见窗口段无条目，停止已越过本窗，不宣称全机构无遗漏。 |
| [SRC-BYTEDANCE-SEED](https://seed.bytedance.com/en/research) | research可见表1/27→4/11；public_papers首20项/Page1of13；日期域查询首批；补查：Research1/27→4/11；Papers首20/total242/page1of13；?page=80路由探针仍首1页即止，不授80页或242逐项题摘 | 受阻 | D9完整论文历史分页未恢复，首页不证明全部研究无命中。 |
| [SRC-BAIDU-ERNIE](https://ernie.baidu.com/blog/zh/) | 中文博客可见日期4/15 ERNIE-Image跨到2/6 ERNIE5.0与1/29 PaddleOCR-VL；补查：博客首页5/9读到1/8，4/15→2/6跨本自然日无可见条目即止 | 已检查 | 官方博客窗口段无条目，停止已越过本窗，不外推全机构。 |
| [SRC-XIAOMI-MIMO](https://mimo.xiaomi.com/) | Paper完整8项，2/3 HySparse→3/13 ARL-Tangram；Blog可见15项及More；日期域查询首批；补查：Paper8项2/3→3/13跨本日；Blog15项/More无日期，历史仍限；科学应用仅标题退出 | 受阻 | D10 Paper本窗段无条目；Blog历史无日期且More未恢复。 |
| [SRC-MINIMAX](https://www.minimax.io/blog) | 英文与中文重定向minimax.cn/blog可见完整目录；Forge英文2/14、中文2/12原值分别保留，均窗外；M2.7为3/18；补查：EN/CN可见Blog段3/18→ForgeEN2/14/CN2/12；AgentTechBlog两9月项即止；3/11回顾中2/28活动不当公开日 | 已检查 | 可见窗口段无条目，没有把财报算研究，不外推全机构。 |
| [SRC-ARXIV](https://info.arxiv.org/help/availability.html#announcement-schedule) | 实读公告日程/2026节假日；本窗2/27 20:00 EST→2/28 20:00 EST；二/三月cs各首1～2000身份页无日批次即止；窗口announced_date_first主题查询首请求cache miss；补查：实际日程/假日及四组SubmittedDate邻域主题，语言69（50+19，start50止）、系统5、多模态33、Agent38；去重103身份仅相关题名差额题摘；16首提交北京03/01关闭该arXiv事件；45潜力abs一次日期恢复后隔离，Social当前withdrawn；不以Submitted或ID年月授public | 受阻 | AX1无常规slot，但非例行/延期历史不能排除；失败查询不记零命中。 |

没有扫描每周来源或额外按需发现源。arXiv 主线主题为 CL/LG/AI/DC 的 LLM/Transformer/MoE/训练优化/Agent，CV/RO 的生成基础模型/World Model/VLA，AR/PL/OS/PF 的 kernel/runtime，IR/MA 的 RAG/记忆/协作。无例行批次可浏览；宽月表只作身份查漏，不是逐项题摘/全文队列。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Our agreement with the Department of War](https://openai.com/index/our-agreement-with-the-department-of-war/) | 2026-02-28T20:30:00+08:00 | 云端部署/厂商安全栈控制权形成具体版本配置声明，但未披露可迁移机制；1 + 2 + 1 = 4 | 深入完成 | 仅报告：Version Fact / Mechanism Not Disclosed，无长期机制增量 |

只有这个唯一家族，3/2追加措辞不是本窗事件；窗外及明确范围外材料保留在筛选记录，不冒充当窗已审家族。

补充窗口新增确定候选0。45潜力仅缺必要公开日期，身份、完整题摘准入链和具体EX见[补查准入包](../_sources/daily-20260301/SUPPLEMENT_ADMISSION_20261008.md)，逐项缺项见[日期保留清单](../_sources/daily-20260301/SUPPLEMENT_DATE_REQUESTS_20261008.md)。不先列为当窗候选或给分、不用访问状态/成熟原则/owner映射调分。Social-JEPA当前withdrawn不评分/Books。

## 4. 证据与知识整合

### [Our agreement with the Department of War](https://openai.com/index/our-agreement-with-the-department-of-war/)

精确范围为更新分隔线下的2/28说明“Deployment architecture”、人员参与及FAQ，不采用3/2新增条款。原文公开cloud-only而非edge部署，由厂商运行/更新安全栈及classifier，特定人员参与；这能确认公开声明的控制权归属，不能证明检查完整性、真实执行路径或禁止行为不可能发生。其“可以独立验证”和绝对防止滥用的保证缺少威胁模型、实现与效果证据，不予采用。

root与mar02_v3独立读取上述必要正文及官方RSS原字段。对读`PLATFORM-SECURITY` [Ch72资产/信任边界与部署残余风险循环](../../../../books/part-06-ai-infrastructure/72-security.md)：该章解释主体、控制位置、mitigation验证和决策责任；本公告没有足以新增或修正它的机制证据。因此仅报告版本事实，不声称某专属架构“已覆盖”，也不修改Books。2/28旧响应保留，RSS日期纠正原日期隔离，未删除反证。

保留旧有效原文与账本；[旧日报快照](../_sources/daily-20260301/V3_LEGACY_REPORT_SNAPSHOT.md)仅用于恢复，不定义当前日期、分母或完成标准。本日未修改共享 Books、索引或 LEARNING_STATE。

### 补充窗口：证据与Books差额

45份原题摘只支持待核的具体贡献潜力，不等于实验可归因或当窗证据；每项当前官方abs一次检查只给Submitted/版本提交史，不能授首公开日，因此没有进入正面证据/Books判断。TraceSIR精确v1的§3.1式1、§3.2和Table2一次core仅见既有三元组解析/逐field阈值摘要；faithful是设计目标，未给新可验证保真约束或压缩归因边界，具体贡献关闭而非按三Agent字样关闭。Social-JEPA当前abs明确作者撤回，v2/3均withdrawn，API旧摘要不作为有效版本证据，保存原排除依据。上述差额均未重审旧OP1或改动共享Books；原§4三个连续段落逐字冻结。

## 5. 缺口与下一步

补查普通待办0。本轮独立准入与DAY实际通过；以下新外部保留项已精确隔离，不属于未执行工作，也不算Coverage/Evidence通过，不能用数量大或深审耗时变更准入。

- **SD45 — 45个具名材料的必要首公开日期**：[逐项身份/原入口与请求](../_sources/daily-20260301/SUPPLEMENT_DATE_REQUESTS_20261008.md)，仅缺首次公开正文的官方日/公告或作者dated原发布。当前完整题摘潜力明确、abs一次有限恢复仍只有Submitted；不评分、不正面引用、不进Books、不支持无遗漏。可接受对应ID官方公告/状态邮件，或作者具名正文dated发布；材料到达只重开该ID公开日，再依是否落窗审必要证据/Books。不要求时分秒、不再用全文绕过date。
- **补充CH混元历史限制**：本日EN9 total/list已读不证明CH历史；研究页动态浏览器两个只读attempt均timeout。可接受本自然日官方中文dated列表/发布正文，仅重开对应CH子入口；旧11项目录与撤销D8记录只冻结复用。

旧终态处置保留如下，其“普通待办0”与旧完成标签不替代本轮验收。以下为本窗终态保留项，不支持候选、正面证据、Books、无遗漏断言、安全或性能保证；材料到达后定点重开。

- **OP1原日期请求已解决**：官方RSS给出带时区发布时间，原2/28说明可由更新分隔线限定。仅当后续提供具体部署实现、验证协议或反证时，才重开本家族的机制/有效性判断；当前厂商保证不支持正面安全采用。
- **D1～D6、D9～D10 — 历史子目录**：来源身份、具体URL和停止点在 §2 对应行；D6仅为News隐藏分页/API updates。所需为本窗主线相关事件的可枚举dated archive/原发布/release列表或可访问动态历史过滤。当前原入口、有限搜索及必要浏览器尝试未恢复相应历史段；没有取得确定线索不等于零事件。D7的Kimi研究目录与D8的混元目录已实际恢复，不再索取。只重开具名受阻子入口与本窗，不扩全年/全机构全文队列。
- **AX1 — arXiv 非例行/延期历史**：常规日程无slot；官方窗口主题查询cache miss，月表不提供日批次。可接受覆盖本窗的官方公告/延期status邮件及相关精确身份。只重开该批次与当前主线主题，不以DataCite/Submitted补造first-public。

窗外线索（仅用于排除复核，不扩本任务）：ZAI GLM-5报告2/21；MiMo HySparse2/3、ARL-Tangram3/13；MiniMax Forge英文2/14、中文2/12；Google Gemini3.1 Pro/FlashImage card2/19和2/26。MiMo New Materials R&D 的标题明确为材料应用，属 ROADMAP 暂缓 AIforScience，未见需重开的当前纠错/安全/修订信号，不穷追其日期。

## 6. 复核

复核者：root（原报告非作者）；mar02_v3（新增公告窄审阅非作者）
结论：通过

2026-10-01 root 实读 OP1 官方核心说明，同意潜在贡献日期隔离，不能按 Company 标签关闭或反填3/2修订；抽检 ZAI/MiMo/MiniMax 窗外身份和 AIforScience 范围退出理由成立。该批为1潜在贡献隔离及五组具名负侧身份的分层校准，不称全机构目录全量验证。

root最终检查14/14来源行及有限停止记录、北京时间周末窗口与公告节奏、唯一候选OP1及五组具名负侧（ZAI GLM-5；MiMo HySparse/ARL-Tangram；MiniMax Forge中英日期；MiMo材料研发；Google两张2月card）。OpenAI RSS恢复后仅重开OP1日期及处置，mar02_v3实际再读原说明/FAQ与RSS，批准1+2+1、窄深入和仅报告边界，不采用未证安全保证；普通待办0，无必要Books改动。未无差别审阅窗外全文或验证隐藏历年目录。混元、DeepSeek和Kimi用真实官方入口修正原访问边界；MiniMax中英日期分别保留。依据见[官方目录恢复](../_sources/V3_OFFICIAL_DIRECTORY_RECOVERY.md)及[混元只读目录](../_sources/V3_HUNYUAN_LIST_RECOVERY.md)。外部保留项与采用链路隔离；格式检查不代替语义验收。未stage、commit或push。


2026-10-08补查复核：复核者root（非本次作者），结论：通过。root实际核14源URL、主题、分页/停止点及完整六部分差额；完整核全部45日期潜力与其余13组代表EX，实核Social-JEPA官方撤回、TraceSIR精确v1必要§3.1/§3.2与Table2；不是全机构目录/全部领域排除或全部v1全文深审，不把分层样本称为全量验证。无新增确定候选/必要Books改动，普通待办0；旧OP1有效证据/Books判断复用不重审。V3、原候选/旧窗/连续§4逐字冻结、本地引用和限定diff检查通过，格式检查不代替上述语义复核；未stage、commit或push。


root首批准入实际完整核读原44潜力的当前Atom摘要与原14组代表EX/TraceSIR摘要、Social官方撤回；不是全部精确v1 Full Source Review。RAIE仅以推荐领域退出的旧EX被撤销，作者一次精确v1 §4.1.3～4.3必要方法core确认动态区域Update/Expand/Add与局部LoRA路由潜力，随后一次原abs仍缺公开日，加入第45日期保留项；成熟cluster/EMA/LoRA本身不计新增。root进一步实际核RAIE精确v1 §4.1.3、§4.2式3–6与§4.3式9，支持窄潜力/日期隔离，不证明防遗忘或radius可靠；最终45潜力/其余13组代表EX及DAY通过，不进确定候选/Books。
