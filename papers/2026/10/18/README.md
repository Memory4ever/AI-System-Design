# Daily Research — 2026-10-18

**规范：** V3
**窗口：** 2026-10-17 ～ 2026-10-17
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-20T13:37:00+08:00

## 1. 结论

本窗已对 14 个每日来源实际开展有限检查，未形成通过贡献准入的候选（0 个家族），因此没有需要评分或证据审阅的候选，也没有 Books 新增。DeepSeek 当日开放 Search & Fetch 与 Flash-1017 更新已读官方核心说明，分别因没有新增机制/有效性边界、仅有未充分归因的版本性能宣称而在候选前关闭；不把成熟接口原则重写成研究贡献。

arXiv 本窗无常规定期公告，但这不代表机构来源零发布。Google 年级目录与 Qwen 空壳正文的覆盖限制保留在 §5，不据此宣称无遗漏。MiMo剩余主线标题已实际恢复官方日期，Meta替代publication目录已恢复带日期片段，未见本窗事件。完整日级独立复核已通过，无未处理的可执行研究或 Books 工作；完成不表示两个保留入口已获得正面覆盖。

## 2. 来源覆盖

所有范围均限定本窗与当前模型/系统主线；详细实际请求、恢复及停止理由见 [作者 A2–A3](../_sources/daily-20261018/AUTHOR.md)。批次请求时间/状态见 [原始记录](../_sources/daily-20261018/fetch_results.json)，原件和网页读取保存在同目录。未常规扫描每周组。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research index](https://openai.com/research/index/) 直接 403 后网页恢复最新 9 卡（Oct19 至 Sep29）；[RSS](https://openai.com/news/rss.xml) 前30项止 Oct2。RSS 中 Itau 事件进入官方正文核心说明后按贡献关闭，不用小时过滤排除 | 已检查 | 不宣称 RSS 覆盖所有研究；当前快照非目标日逐字历史 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) Publications 首页10项，Oct16五项，经Oct12/9到Oct8，止 See more 前；无Oct17卡 | 已检查 | 无，限定所列窗口目录切片 |
| SRC-GOOGLE-AI | [DeepMind Blog](https://deepmind.google/blog/) October卡至首处September；Argon发布/安全/Robotics原件均Oct13，EmbeddingGemma2 Oct6，反诈Oct14。[Research Blog](https://research.google/blog/) 首10项Oct16至Sep24；[Pubs](https://research.google/pubs/) 默认15/11622项，仅年份排序，3个相关身份定点恢复为较早材料 | 受阻 | Pubs缺日级目录/公开事件时间；有限原件与补检不能推出全年穷尽，见§5 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)仅标题后恢复[Publications](https://ai.meta.com/results/?content_types%5B0%5D=publication)：page1当代前12卡Oct19→Oct14→Oct13，page2当代段Oct2至Jul17，均随后混排旧卡，止page2当前段/首处旧卡，未见Oct17；另Blog首10卡日期浏览 | 已检查 | 不把混排旧卡说成严格倒序，不以Blog/搜索证明全源零事件；[实际恢复A5](../_sources/daily-20261018/AUTHOR.md) |
| SRC-QWEN | [旧入口](https://qwenlm.github.io/)迁移提示；[Blog](https://qwen.ai/blog)、[Research](https://qwen.ai/research#research_latest_advancements)与具名qwen3_next均实际HTTP200空壳；网页恢复、旧站具名路径和一次浏览器运行时恢复未取得正文 | 受阻 | 搜索标Oct17的具名项正文/日期不明，隔离，见§5 |
| SRC-DEEPSEEK | [官网](https://www.deepseek.com/)、[Change Log](https://api-docs.deepseek.com/updates/#date-2026-10-17) Oct17两事件核心说明及[Search & Fetch guide](https://api-docs.deepseek.com/guides/search/)；次条日期Sep10为停止边界。独立校准后两项均贡献筛选关闭 | 已检查 | 现行guide非不可变Oct17快照，不反推全部字段首创；不影响贡献退出 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog) 当前页26条最新Nov7 2025；[org](https://github.com/MoonshotAI)首10/42仓库作线索；kimi-code [Releases](https://github.com/MoonshotAI/kimi-code/releases)首10项Oct14至Sep4、[What's New](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html)首3版本段Oct14/Oct14/Sep23 | 已检查 | org updated不等于研究公开日期；未扩全部普通提交 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research) loader恢复[官方API](https://api.hunyuan.tencent.com/api/blog/publicList)，POST renderType0/page1/size20，中11/11、英9/9到末；publicAt最新中文Sep22/英文Sep23，保留display字段差异 | 已检查 | 无；[本次目录原字段](../_sources/daily-20261018/hunyuan_directory.json) |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) 当前15卡Aug26至Dec2025，日期均早于窗，停可见目录 | 已检查 | 无，限定本次研究入口 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)与[Public Papers](https://seed.bytedance.com/en/public_papers)第1/13页20/246项，显式新到旧、Sep28至May26；无日期SeedRealtime原件Aug5 | 已检查 | 无；不继续旧页，不以误猜空Blog路径代替研究入口 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)第1/2页，最新May9 2026至Nov21 2025，止本页日期边界 | 已检查 | 无；不扩第2旧页 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/) Paper8项最新Jun29；Blog15标题经实际原页/iframe恢复13个主线技术条目日期：最新tool repetition Sep27、V2.6 Sep22，其余June/May/April/March及2025；HSS及具名Safety原页December2025，材料研发范围关闭，止首页所列与具名Safety | 已检查 | 无；April2026仅按月排窗外；HSS/Safety正文Dec22与frontmatter Dec19/18保留差异，不造精确首公开，见[作者A4](../_sources/daily-20261018/AUTHOR.md) |
| SRC-MINIMAX | [Blog](https://www.minimax.io/blog)首6卡Oct19、Aug13、Jul31、Jun9、Jun1、May27；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)共3卡Oct8/Sep22/Sep19，止可见末项 | 已检查 | 无，限定两研究入口；M3.1不搬入本窗 |
| SRC-ARXIV | [官方公告规则](https://info.arxiv.org/help/availability.html) Sun–Thu 20:00 Eastern，Fri/Sat无；本窗对应Oct16周五晚EDT，故无常规公告批次，无相关分类日批次可展开 | 已检查 | 不推断异常发布或机构独立事件不存在；不把Submitted日期作公告日 |
| 表外：[LATTE'26](https://capra.cs.cornell.edu/latte26/) | 仅由Google首屏身份触发：multi-chiplet TPU同题作者programme关联March23；未扩会议库 | 已检查 | PDF一次timeout，programme不是首次公开日期；仅旧材料线索，不采作本窗新事件 |
| 表外：[Zenodo](https://zenodo.org/records/19700278) | 仅Google首屏Toolbox官方链接触发，published Apr13/created Apr22，保留原字段；另GroupDPO官方arXiv2604.15602 v1 Apr17/v2 Sep1 | 已检查 | 不扩全年库、不移入本窗；[日期原件](../_sources/daily-20261018/webPublicationDate.json) |
| 补检：[官方域限定搜索](https://www.google.com/) | `site:research.google/pubs/ "October 17, 2026" "model"`、`site:deepmind.google "October 17, 2026"`、`site:ai.meta.com/blog "October 17, 2026"`无结果；`site:qwen.ai/blog "2026/10/17"`命中空壳具名页。只作恢复线索 | 已检查 | 搜索不可证明穷尽；Qwen必要正文缺口不豁免 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

无通过贡献筛选的当窗候选，未评分；不把原始命中、窗外材料或日期/正文不明项列为确定候选。[作者A1–A2](../_sources/daily-20261018/AUTHOR.md) 的 Search & Fetch 拟分未获采用，保留具体误判及改判依据。

## 4. 证据与知识整合

本次没有进入候选证据审阅的材料，也没有可支持 Books 增量的已准入命题。Books 为 No Change：这是贡献筛选后的无采用项，不是“已有覆盖”的主题匹配判断，因此未虚列 owner 或既有段落作为成果；没有改动共享书稿、Learning State 或索引。

DeepSeek 完整核心说明的初筛阅读及独立校准只支持候选前退出：API可用性本身不是新检索机制，Flash-1017的榜单/用时宣称不足以归因为新设计。保存[发布记录](../_sources/daily-20261018/deepseek_updates.visible.txt)、[指南](../_sources/daily-20261018/deepseek_search.visible.txt)及[作者A2原始判断](../_sources/daily-20261018/AUTHOR.md)，不冒称已核验未公开实现、复现实验或历史逐字指南。

## 5. 缺口与下一步

无未处理的可执行工作。非作者 root 已完成实际来源范围、排除分层及完整六节的日级独立复核，依据见 [ROOT_REVIEW](../_sources/daily-20261018/ROOT_REVIEW.md)。本次只完成该 Daily，不扩其他日期或 Weekly。

以下为本窗外部终态保留项，已经有限实际恢复；均不支持正面证据、Books、覆盖穷尽或性能/安全保证，不按“零命中”替代：

- **Qwen：** [qwen3_next](https://qwen.ai/blog?id=qwen3_next) 搜索仅显示Oct17与`undefined minute/0 words`，Blog/Research/具名页解析均空。需官方可读正文与公开日期，或可核同身份的官方不可变公告/作者稿；收到后仅重开此具名项的日期、范围与贡献。旧站两个具名变体404、一次浏览器运行时未恢复，不声称已读UI。
- **Google Pubs：** [目录](https://research.google/pubs/)默认15项只按年份，有限日期补检与3个较早原件不能证明所有Oct17事件已定位。需官方日级发布/新增索引或具体带日期原件；只补相关窗口。当前可核旧稿不移入本日，不将LATTE programme日期冒作首公开。

上述保留项不等于普通未读队列，现有可用路径已有限尝试并保存；不需要用户扩大窗口。窗外 Argon Oct13、M3.1 Oct19等只核身份/日期，不在本日恢复其审阅，也不启动Weekly。

## 6. 复核

复核者：root（非报告作者；作者为 oct18_missing）。

结论：通过

独立复核依据：[ROOT_REVIEW R1](../_sources/daily-20261018/ROOT_REVIEW.md)。root实际读完整六部分与作者A1–A5、全部拟入选0及DeepSeek两排除项原始核心，纠正将成熟接口语义算作新贡献的问题。实际分层抽核OpenAI RSS/Itau核心、Anthropic安全跨窗段、Google Blog/Argon/Embedding日期、Moonshot release/What's New、Hunyuan原字段、Meta两页当前段、MiMo ASR/Safety与路由恢复，及wetlab/材料科学范围排除。检查14来源与有界触发路径、两项外部隔离、零候选/无Books写入和六节一致性，日级通过。

其余窗外卡片仅按来源、主题与理由分层检查身份/日期，不声称全部全文复审；Research空壳、年级目录和搜索不支持无遗漏。既有[REVIEW R1](../_sources/daily-20261018/REVIEW.md)保留为旧日程前置记录，不冒用其作者身份或验收范围。完成态V3结构校验、本地引用与本日限定diff检查通过；未stage、commit、push，未改共享Books/索引。机器校验不替代上述实际语义复核。
