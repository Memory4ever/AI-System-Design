# Daily Research — 2026-01-04

**规范：** V3
**窗口：** 2026-01-03T09:00:00+08:00 ～ 2026-01-04T09:00:00+08:00
**窗口说明：** 用户授权只补遗漏，保留原窗口、既有候选日期/评分及有效审阅，不搬移旧材料。
**补充窗口：** 2026-01-03 ～ 2026-01-03
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-07T13:57:31+08:00

## 1. 结论

本轮按Jan03完整自然日补查14个每日来源，新增确认候选0、新增候选证据审阅0、Books写入0。Qwen/Hunyuan动态接口、MiniMax中文/Agent原入口与MiMo有限Blog路由日期恢复；没有把宽UTC探索查询或API提交/更新字段称为本日公开论文。已执行的有限检查、正确BJT查询与精确限制见[本轮依据](../_sources/daily-20260104/supplement-20261007.md)。本轮非作者独立复核通过；Google/Meta两项具体外部限制已隔离，不代表全部Coverage/Evidence无缺口或无遗漏。

本窗没有确认通过贡献筛选且能确定落窗的正式候选。14个每日来源完成本次有界检查；0正式候选、0候选证据审阅完成、0 Books整合/已有覆盖，Books为No Change。候选证据进度不包括目录、日期或核心变更说明的初筛读取。root非作者日级验收通过；外部历史限制仍保留，不等于无遗漏覆盖。

KimiCLI 0.71/0.72虽然changelog标签为Jan04，官方release的published_at实际分别为Jan04北京时间13:08:41/14:01:07，严格窗外，归下一日窗口的恢复线索；未顺带审PR或称已审重复。arXiv普通Fri/Sat无公告与官方元旦延期支持本窗没有常规公告，不证明作者镜像、非标准更新或机构历史无遗漏。必要历史入口限制已隔离，不用于正面证据或Books。

## 2. 来源覆盖

只检查Daily组，未扫描Weekly源。按本日窗口从原始来源新取，不继承旧日报或Weekly的候选、评分、摘要及完成结论。[本日查询/停点](../_sources/daily-20260104/queries-and-screening.md)、[机构日期原字段](../_sources/daily-20260104/official-date-slices.jsonl)、[官方日期补检](../_sources/daily-20260104/date-search.txt)及[原入口响应](../_sources/daily-20260104/official-entry-0.txt)可复查；空搜索不作零发布证据。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 本轮Research→官方RSS1251项仅title/link/pubDate定位补窗及Grove Jan02/Health Jan07邻接，Jan03无条目，止日期切片不读全年正文 | 已检查 | 仅这些官方入口与RSS，不证明所有机构镜像/隐去发布 |
| SRC-ANTHROPIC | Research首屏后原HTML174 publishedOn字段定位本窗及Dec19T19:45Z Bloom/Jan8T00Z Critical Infrastructure Defense，窗内0，止metadata | 已检查 | 仅当前官方Research有限目录，不授机构全量 |
| SRC-GOOGLE-AI | 本轮DeepMind Publications page1 Jan09→Dec03跨窗，止page1；Google Research 2026/01月档9条Jan28→Jan12，止末项；pubs当前年字段及日期补检未恢复Jan03论文日级列表 | 受阻 | 两个dated有限入口已检查；Google Research Jan03论文日级公开目录仍缺，空搜索不判零 |
| SRC-META-AI | Research原入口TLS失败；本轮Publications?page=3不可访问，官方域Jan03日期补检停止首组，无可核日级切片 | 受阻 | 空提取与空搜索不能替代必要历史目录 |
| SRC-QWEN | 本轮官方api/page_config?code=research.research-list返回60项，按date完整定位，最大Dec23 2025，无Jan03；止当前有限配置 | 已检查 | 不按数组次序停止，不声称全机构隐藏历史不存在 |
| SRC-DEEPSEEK | /news/研究10项Jan12→Dec31跨窗、动态5项/查看全部，无本窗行，止有限官方dated目录 | 已检查 | date-label不当首公开时刻，有限研究列表不证明所有发布 |
| SRC-MOONSHOT | 本轮平台26项Nov07 2025→May2024；原有效KimiCLI日期片段0.70 Dec31→0.71/0.72 Jan04，均补窗外；止明确相邻版本，不读PR | 已检查 | 只声称平台与已触发release有限范围，不索所有repo历史通知 |
| SRC-TENCENT-HUNYUAN | 本轮官方POST publicList pageNum1/pageSize100/renderType0成功，total9/list9，publicAt/published/display分列，最早display/published Feb03；止完整有限响应 | 已检查 | 当前九条不是当期完整档案，不混用created字段，不因此请求全机构无删除证明 |
| SRC-ZAI | 本轮Research SSR有限公开日期定位无Jan03，CMS Jan07字段与Jan13研究条目分开；有效release片段Jan14→Dec22跨窗，止实际日期切片 | 已检查 | CMS入库/修改不作论文首公开，目录与release各有范围 |
| SRC-BYTEDANCE-SEED | 本轮API type1/2026 ASC首片20条、total82；type2首片9条、total23/next20/has_more=true，最早Jan20/Feb12。原有效2025日期切片复用，最近paper Dec15/blog Dec24；止跨窗边界 | 已检查 | 本轮与旧响应计数分开；有后页不等全年读完，按实际日期而非pinned停止 |
| SRC-BAIDU-ERNIE | Blogpage1 Jan8→Dec23跨窗，下一页2/2更老；止page1及官方域日期query首组，无本窗行 | 已检查 | 仅官方博客目录，不授所有机构发布 |
| SRC-XIAOMI-MIMO | 当前8 Papers Jan08→Oct21跨窗；本轮官方Blog构建索引完整16个英文route，frontmatter及显式iframe正文日期定位，未见Jan03；止完整当前路由 | 已检查 | 无日期的Model Description读核心为通用能力介绍，不具机制增量；不把当前目录当全部隐藏历史证明 |
| SRC-MINIMAX | 本轮English12项Jan27→Dec23、中文13项Jan28→Dec23跨窗；Agent原页面文本唯一dated May13；止各有限入口 | 已检查 | 旧中文/Agent壳访问限制解除；中英日期分别保留，不授全机构 |
| SRC-ARXIV | 本轮Availability L172常规公开包含new/replacements等；Jan03 BJT为Fri ET→Sat ET，无常规公告。四主题按BJT尝试older-update查询start0/max20返回0，但API字段改写成互斥Submitted，不能支持零修订；止实际入口 | 已检查 | API不独立证明公开，月页404是访问边界；不扩Submitted池，不宣称非标准/所有作者镜像不存在 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

无正式候选。没有把arXiv提交、API更新字段、机构当前标题或相交日期标签升格本窗候选；不评分。

## 4. 证据与知识整合

本轮新增候选为零，没有新采用命题，不需为制造diff修改Books。原有效负侧/日期依据继续保留；本次正确自然日查询不替代旧窗口记录，也不调整其中Kimi两个版本的日期。先前Jan03 UTC整日探索查询边界不合补窗，已明确弃作覆盖与准入依据，未形成候选或证据队列；见本轮原始记录。

无本窗候选证据审阅或Books写入。以下仅是日期/范围校准，不冒充深入审阅：

- [arXiv Availability](https://info.arxiv.org/help/availability.html) L172说明通常Sun～Thu公告且Fri/Sat无公告，L175–176说明ID首次公告分配、不backdate；L185–186排期与[官方元旦延期](https://blog.arxiv.org/2025/11/21/temporary-changes-to-announcement-schedule-due-to-end-of-year-holidays-2025/) L32共同限定下一批Jan4ET20=Jan5BJT09。Jan04窗在其之前。标准过程也提replacements，但当前说明及空API不证明本窗无非标准更新或作者先行。
- [KimiCLI原变更说明](https://raw.githubusercontent.com/MoonshotAI/kimi-cli/main/CHANGELOG.md)完整窄片段仅公开ACP client file/shell同步、model/skill命令、Toad/info及Python安装兼容；root独立校准认为只凭这些feature/标准协议接入不足以建立长期可靠性机制增量。随后[0.71官方release](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.71)与[0.72官方release](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.72)的published_at确定窗外。没有把created_at当首公开，也没有用这一负侧意见替代下一日其他事件的独立筛选。
- ROADMAP的模型/训练/推理/多模态/Agent主线及AI for Science暂缓保持；没有域应用换场景或仅主题相关的机械owner映射。No Change不等于证明所有研究没有贡献。

## 5. 缺口与下一步

尚可执行：0；本轮补查与非作者独立复核已完成，原日级验收没有替代本轮复核。以下外部限制为终态保留项，不作为证据审阅完成或无缺口证明。

本轮两项具体终态保留项：Google Research Jan03论文日级公开目录；Meta Jan03可读Research/Publication日期切片。替代材料是对应日期的官方列表或具名原始发布；定点重开条件是取得这些材料，只恢复受影响源/条目。MiMo有限Blog路由及日期已恢复，不再请求该材料；当前可读有限入口不另要求证明全部隐藏/删除历史不存在，不索没有具体线索的所有作者镜像。

这些外部保留项不用于正面证据、Books、无遗漏或性能/安全保证；不表示Coverage或Evidence没有缺口。未来必要材料到达再恢复受影响判断，不补造时间。

窗外恢复线索：KimiCLI0.71 published_at=2026-01-04T05:08:41Z，0.72=2026-01-04T06:01:07Z，均归Jan05窗口；原created_at另存[官方ReleaseAPI记录](../_sources/daily-20260104/kimi-release-date.jsonl)，不当公开时间。本日不审Jan05PR，不称贡献/Books已处理，也不阻塞Jan04。

## 6. 复核

### 本轮增量

复核者：audit_supp_jan04（非补查作者root）

结论：通过

独立读取本轮14源入口/停点与原有效日期记录，分层核对机构有限目录和原响应字段；独立重放四个按BJT尝试的older-update查询，均HTTP200/total0/entries0；后续实际核返回标题确认字段被改写为互斥Submitted，0响应无效，不授旧稿修订阴性，并重开arXiv公开规则、DeepMind page1、Google月档、Meta目标页和DeepSeek研究索引。另核Seed type2本轮9条/total23/next20/has_more=true；旧日期切片仅复用边界，不混作本轮响应。发现假期本地链接不存在、DeepSeek raw实际为API Docs及OpenAI/Seed/Meta新旧来源字段混用，作者已定点修正；候选日期、评分与旧有效审阅未改变。

MiMo补充证据独立核16个英文Blog route：6个frontmatter日期及10个显式iframe，9个iframe有窗外日期，唯一无日期Model Description核心仅泛能力介绍，无准入增量，其具体保留项解除。两项Google/Meta必要历史目录限制继续隔离。新增候选0/证据审阅0，No Change与Books无diff一致；未重开废弃UTC探索池、窗外全文、Weekly或其他日期，也不授全网及隐去历史无遗漏。完整实际范围与未检查范围见本轮依据末尾独立复核记录。

机器校验：本轮报告validator、限定diff空白检查及本地引用检查通过；只证明接口一致性，不替代语义复核。无stage、commit或push。原独立验收保留如下，不用于替代本轮补查验收。

### 原有效日级复核

复核者：root（非报告作者jan01_v3）

结论：通过

root实际完整读取本报告、queries-and-screening、official-date-slices全部条目、kimi-release-date两原payload及arxiv-and-kimi四主题查询/窄变更说明，核对原入口日期桥接、查询停止与受阻字段；另重开官方availability L170–189及假期L17/21/29/32。首批范围校准与本日最终审阅确认0确定候选、两Kimi release窗外归Jan05正确，普通负侧仅这两个版本而非全年目录。核验精确8组机构历史缺口及arXiv公开revision/mirror限制的安全隔离、六部分接口与No Change，无Books写入无需POST。实际范围是本日有限来源与上述原始材料，不是全站、全互联网或所有历史修订的无遗漏验证。

机器校验：最终validator与本日限定diff/新增文件空白检查通过；本地引用已检查。机器结果不替代上述语义复核。未stage、commit或push。
