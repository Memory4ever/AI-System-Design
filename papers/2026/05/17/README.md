# Daily Research — 2026-05-17

**规范：** V3

**窗口：** 2026-05-16T09:00:00+08:00 ～ 2026-05-17T09:00:00+08:00

**窗口说明：** 用户授权对 279 份 2026 既有 Daily 只补来源遗漏，保留既有候选整行、日期评分、原小时窗口与有效原证据，不重新归属。运行前真实档案见 [baseline](../_sources/daily-20260517/baseline-before-supplement-20261019.md)。

**补充窗口：** 2026-05-16 ～ 2026-05-16

**状态：** 完成

**Books：** 纳入本次

**检查时间：** 2026-10-19T10:50:33+08:00

## 1. 结论

本轮只补查北京时间 2026-05-16 完整自然日，不继承旧报告的零事件断言或旧准入门槛。真实运行前当前候选表为 0 项，本轮新增确定候选仍为 0，合计 0；没有新评分、候选证据审阅或 Books 写入。旧 279 个 identity 与早期 31 候选不是本轮队列，不据此重建其他日期。

14 个每日来源均已实际尝试有界检查并留下停止范围，但并非全部取得了完整历史覆盖。OpenAI Malta 公告是 Plus 分发与 AI 素养合作，不新增模型或系统机制；官方 GPT5.5 degradation 状态页只披露调查与缓解，没有根因或技术 write-up，不把“已缓解”当作设计改进或质量保障。Charon 的官方 May16 事件与旧 May16 已有 `2605.17164v1` 家族重复，定点复用已有审阅，不搬到本日报。混元的动态目录已通过其真实公开接口恢复，“全部”中文切片真实返回 11 条，日期跨过 May16 后停止。

本日为北京时间周六，对应美国周五无常规 arXiv 公告；当前及历史官方规则均如此。规则不证明不存在个别异常事件，分类历史列表恢复失败及主题补检限制仍单独隔离，不用日程或旧 DataCite created-day 零值证明全球零论文。其他机构历史缺段、必要正文与日期限制见 §5；这些保留项不作正面证据、不进 Books，也不支持“无遗漏”断言。独立非作者已实际完成本轮日级安全终态验收，普通研究待办为 0；完成指有界处理与精确隔离，不授完整 Coverage 或未得材料的 Evidence 通过，不沿用旧完成声明。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方 RSS](https://openai.com/news/rss.xml) 完整 feed 中 May18→May16 Malta→May15；[Malta 正文](https://openai.com/index/malta-chatgpt-plus-partnership/) 贡献排除。纠错线索定点回到 [官方 incident](https://status.openai.com/incidents/01KRP6FM6HSKWB3MS1EJTY6AT4)，调查/缓解发生于补窗，未披露机制；[实际提取](../_sources/daily-20260517/SUP_OPENAI_STATUS_20261019.json) | 已检查 | 原 X 两条 403，不据转引采用“两项修复”原因；官方状态页可支持的事件事实已恢复，没有技术 write-up 可供设计采用 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) HTML 所含 publication 数据，以公开 `publishedOn` 而非 created/updated 字段核 May22→May14 的邻接；[窄提取](../_sources/daily-20260517/SUP_ANTHROPIC_PUBLISHED_20261019.json)，不止于渲染首10项 | 已检查 | 无该入口内 May16 条目；不声称全互联网无遗漏 |
| SRC-GOOGLE-AI | [DeepMind Publications](https://deepmind.google/research/publications/) 第1页30条/总265，May28→May6→Apr25 已跨目标日期停止。[Google Research](https://research.google/pubs/) 只恢复 year 索引首15/11622，另做 May16 及模型/训练/推理/Agent 的域限定补检 | 受阻 | DeepMind 目标段已读；Google Research 未恢复历史日目录，不能以年份首页或无搜索命中授完整覆盖 |
| SRC-META-AI | 首查 Publications 空文/超时；改走 [官方 results page3](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=3&sort_by=relevance)，实际见 GIM May17 与 NeuralSet May12 的 2026 局部段；再作 May16 模型/训练/Agent 主题补检 | 受阻 | 该页按 relevance 且混入旧年记录，不能当全日期排序。GIM May17/18 旧日期冲突不成为 May16 候选；历史完整目标段仍不可确认 |
| SRC-QWEN | [旧站](https://qwenlm.github.io/) 明示迁往 [新 Blog](https://qwen.ai/blog)；新页 HTTP200 但仅 hydration 两行，作者/reader 浏览器恢复均失败；明确排除 chat 子域后的日期主题补检停止 | 受阻 | 新 Blog 历史渲染段无法取得；空页和搜索无命中不是零事件 |
| SRC-DEEPSEEK | [官方首页](https://www.deepseek.com/) 与官方 GitHub 组织仓库身份索引第一页（per_page100，实际不足100）；May16 官方域与 API docs 日期主题补检未给出可采用事件 | 受阻 | 首页没有历史日索引。仓库 created/pushed 不是公开事件，不能据此授 May16 无发布；具体恢复范围见作者停点 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog) 实际只见2025历史；官方组织仓库第一页仅身份线索。May16 日期补检回到 kimi-cli 的两个具名反馈；[1.44.0 release](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.44.0) 精确恢复为 May14、并非 May16 发布；[原字段](../_sources/daily-20260517/SUP_KIMI144_20261019.json)，未扩扫全部 issue/PR | 受阻 | 平台2026历史日段缺失；shell timeout 反馈仅目录标题，正文/版本未恢复，不能以“用户 issue”直接排除执行反证；见 §5 |
| SRC-TENCENT-HUNYUAN | 首查 [Research](https://hunyuan.tencent.com/research) skeleton 后尝试浏览器；沿实际官网 JS 恢复 [公开 publicList](https://api.hunyuan.tencent.com/api/blog/publicList)，POST pageNum1/pageSize100/renderType0、“Accept-Language: zh”，code0/totalNum11/list11；May21/Apr30 夹窗，三个原日期字段无 May16；[实际字段](../_sources/daily-20260517/SUP_HUNYUAN_DATES_20261019.json) | 已检查 | 仅该中文“全部”确定性目录；英语默认9条不混计。早期404及截断响应不作为证据 |
| SRC-ZAI | 首查 [Research](https://www.zhipuai.cn/zh/research)，实际SSR目录显示 May20→Apr29，跨目标段停止；[提取](../_sources/daily-20260517/SUP_ZAI_EXTRACT_20261019.json) | 已检查 | 不把 created/updated 字段改称公开日期 |
| SRC-BYTEDANCE-SEED | 首查 [论文目录](https://seed.bytedance.com/en/public_papers) 后沿真实 `get_article_list_v2` API 日期导航：publication token空→20，返回18与20条，第二页 Charon May16→UAM May15→May14，跨下边界停止；Blog 2026 切片实际15条、has_more=false、总数字段20，不写20/20；[论文第二页](../_sources/daily-20260517/SUP_SEED_DATEPAGE2_20261019.json)、[Blog](../_sources/daily-20260517/SUP_SEED_BLOGDATES_20261019.json) | 已检查 | 只授实际英文切片目标段，不把后台 total86 当已读86或多语言全覆盖；Charon 精确去重，旧owner不变 |
| SRC-BAIDU-ERNIE | [官方 Blog](https://ernie.baidu.com/blog/zh/) 逆序首列表最新 May9→Apr30，目标 May16 晚于最晚记录，停于第一页，不机械翻更早第2页；[提取](../_sources/daily-20260517/SUP_ERNIE_EXTRACT_20261019.json) | 已检查 | 只限该注册 Blog 入口 |
| SRC-XIAOMI-MIMO | [官方首页 Paper/Blog](https://mimo.xiaomi.com/) 实际 Paper8条，Jun29→Mar13夹窗；[完整文本提取](../_sources/daily-20260517/SUP_MIMO_ALL_20261019.txt) | 受阻 | Paper目标段已读；Blog卡片无日期，不从名称或位置补造 May16 公开归属 |
| SRC-MINIMAX | [官方 Research/Blog](https://www.minimax.io/blog) 当前单页按日期见 May27/May26→Mar18，跨下边界停止；[日期与标题](../_sources/daily-20260517/SUP_MINIMAX_NARROW_20261019.json) | 已检查 | 只限该注册入口，未泛化全站 |
| SRC-ARXIV | 核 [当前官方公告规则](https://info.arxiv.org/help/availability.html) 与 [2025历史规则](https://github.com/arXiv/arxiv-docs/blob/46793211923f3e84140efe04524a250a93b2577b/source/help/availability.md)：美国周五/六无常规公告，涵盖 replacement/withdrawal。做 May16 的 Transformer/LLM/World Model/推理训练与 Agent/GPU/多模态/扩散/kernel/通信两组域限定补检；日期列表失败，月列表大响应超时后停止，不将整类2844条建队列 | 受阻 | 日程有效但不证明个别异常零事件；历史本日官方列表未恢复。无具名拟入选论文等待可执行日期合证，若以后有明确 May16 公告/更早正文身份只重开该项 |

完整查询、入口与失败范围保留在 [唯一作者停点](../_sources/daily-20260517/SUP_SOURCES_20261019.md)；独立恢复和校准见 [本轮复核](../_sources/daily-20260517/SUP_REVIEW_20261019.md)。这些范围不等于互联网或机构全站召回；未扫描 Weekly 组、Live 或其他日期研究正文。

## 3. 候选与判断

原当前候选 0 项，本轮新增确定候选 0 项；重复 Charon、不足贡献的合作/状态通知、未恢复的日期或正文不冒充已确认候选。本轮不改旧归属，不复用旧零结论作为准入规则。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

## 4. 证据与知识整合

本窗没有候选，因此没有 V3 评分、Source Review 或 Books 修改。旧 31 个候选的 exact-v1 证据保留在原 `_sources` 中，只能由各自真实 owner 日在身份、精确版本和采用命题未变化时复用；不能为 05-17 提供 Evidence 或 Books Gate。

Books 写回队列为空，见 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260517/root-books-writeback-queue-v3.json)。

### 本轮补充判断（2026-10-19）

以上连续原 §4 按用户授权保留，其“本窗”指运行前小时窗口。新增自然日结果如下，不把历史证据块当作本轮完成证明。

- **Charon 同事件去重**：本轮官方题摘/PublishDate 与 `2605.17164` 身份见 [单项原件](../_sources/daily-20260517/SUP_SEED_CHARON_20261019.json)。独立reader仅定点核旧May16已有效审阅的同版本及 ExistingCoverage Ch66，身份、事件及采用命题无变化，不重审、不重复评分、不迁移 owner。
- **Malta 与 GPT5.5 incident**：前者没有新增模型或系统机制。后者官方原字段调查为 `2026-05-15T16:11:01.712Z`、缓解为 `2026-05-16T00:35:00.664Z`，均落 May16 北京时间；resolved 在 `2026-05-17T00:15:05.79Z`，不搬入本补窗。原页 write-up 字段未披露，故只支持运营事实，不支持“两项修复”的具体根因、模型能力改进或稳定安全保证，不评分、不进 Books。
- **Kimi 反馈**：[issue #2312](https://github.com/MoonshotAI/kimi-cli/issues/2312) 已读完整描述及代码片段，问题是 React 选择会话时只查 active 数组而遗漏 archived 数组，是本地 UI 状态集合选择错误，不足以改变本项目模型或 Agent 执行设计。shell timeout 另一反馈只有标题，缺少判断取消/进程存活机制所必需的正文与版本，故保留缺口，不按主题映射强收入选。

本轮无新候选需要具体 owner 对比或 Books 修改；这是未形成可采用增量，不是因 Books 已覆盖而缩池。没有新的 Books writeback queue，也不改共享章节或索引。

## 5. 缺口与下一步

无尚可执行的研究待办。独立日级安全终态复核已通过，具名 1.44.0 release 已恢复为 May14 窗外；不因 May16 的用户反馈搬移发布日期。以下外部保留不等于已取得完整覆盖或必要证据。

本窗终态保留项按必要范围隔离，不用于正面证据、Books 或“无遗漏”断言；下列各项列明定点重开条件：

1. **Google Research 历史日目录**：当前入口只给年份及首页15/11622，直接连接超时、web可读但无日排序，May16主题日期补检未恢复必要段。替代材料是含真实发布日期的官方历史目录/当窗研究公告；只重开 Google Research 的 May16 目标段，DeepMind 已核层不重做。
2. **Meta 历史目录及 GIM**：主入口空文/超时，官方results page3仅局部relevance排序，不能授完整目标日覆盖。GIM旧目录May17与详情May18冲突已在旧档案隔离，均不构成本次May16正面候选。需要官方May16日期记录或具名事件的首次公开依据；只重开相应条目/目标段。
3. **Qwen 新Blog、DeepSeek历史入口、Moonshot 2026 Blog及 MiMo Blog**：分别是新页hydration/浏览器失败、首页无日索引且仓库字段不能证公开、旧Blog只到2025、卡片无日期。已有限检查原始入口和指定日期主题；需要有真实May16日期及内容的官方索引/公告，不能拿空响应、created/pushed或搜索无结果替代。只重开缺失入口的本日片段。
4. **arXiv 历史本日列表**：两种日期路径返回无效参数/缓存失败；有效月份路径显示2844条，但大响应在613971/3300365字节超时，未形成完整日期段，失败输出不作可解析JSON或正面覆盖。美国周五无常规公告已核实，相关主题日期补检未给出具名拟入选项；以后出现明确本日官方公告或论文身份时，按当前研究合同直接公告/有效联合界核定该项，不把提交或created日改称公开，不无限恢复整个分类。
5. **Kimi shell timeout 反馈**：搜索缓存的讨论目录称 May16 “运行shell脚本超时了，但是进程没有被中止”，当前列表未返回它，精确目录搜索缓存失败，未取得具体讨论ID/必要正文/版本。该线索可能影响取消与进程生命周期判断，不能仅因是用户反馈排除，也不能仅凭标题泛化为实现缺陷；可接受替代为该讨论原件、版本固定代码/复现/维护者说明。只重开此取消/终止命题。

原小时窗口的 Meta日期冲突和旧5个 `2606.*` identity 的窗外调和边界继续保留在 [baseline §5](../_sources/daily-20260517/baseline-before-supplement-20261019.md#5-缺口与下一步)，不迁移旧材料、不把六月恢复桶当公开日、不授权本轮重跑六月或其他日期。

## 6. 复核

复核者：`may17_supp_reader`（非本报告作者）

结论：通过

本轮非作者已实际检查完整六部分、全部拟入选项（0）、唯一重复 Charon、代表性排除 Malta/官方状态事件/#2312（3项），以及所有具名纠错、取消/进程存活反证线索的原件或精确缺口；按 RSS 合作、故障运营公告、局部 UI 缺陷、论文重复、目录日期与动态 API 分层核对。其余窗外列表只日期导航，未把抽检称为全量题摘/附件/版本史审阅。来源恢复、有效层和完整 DAY 见 [本轮独核 R2–R7](../_sources/daily-20260517/SUP_REVIEW_20261019.md#r7--实际完整六部分-day-通过待保存完成态-final)，不借旧20260915小时窗完成声明。

V3 校验通过；原小时窗口及连续原 §4（288字符）逐字保留；17处本地引用无缺失；限定本日报/本日_sources的 working 与 cached `git diff --check`均无输出。机器检查不替代上述安全终态语义验收，不代表完整 Coverage 或未取得证据的 Evidence 通过。未stage、commit或push，既有及并发修改保留；保存完成态回读与后续行政记录保留在同一独核文件。
