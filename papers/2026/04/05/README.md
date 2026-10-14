# Daily Research — 2026-04-05

**规范：** V3
**窗口：** 2026-04-04T09:00:00+08:00 ～ 2026-04-05T09:00:00+08:00
**窗口说明：** 用户要求仅补既有日报遗漏，保留原窗口、原候选日期/评分及连续原§4。
**补充窗口：** 2026-04-04 ～ 2026-04-04
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-13T21:32:46+08:00

## 1. 结论

仅补 2026-04-04 北京时间完整自然日；原0候选保留，确定新增0，Books新写0。14个到期Daily来源已重新取得有限官网入口/停点，或隔离不可恢复的历史切片；本轮必要依据见[来源补查](../_sources/daily-20260405/SUP_SOURCES_20261013.md)。OpenAI Research、Google Research Publications、Meta Research/Publications、MiMo无日期Blog及MiniMax Agent旧技术博客五类历史切片不计为零命中，也不授无遗漏；另有arXiv历史事件切片限制。没有拟入选项、普通证据审阅或Books写入待办；root非报告作者已实际完成六部分DAY并通过，两处来源边界修正已独立读回。本次完成为安全终态，不继承旧完成标签或宣称所有来源零论文。

日期归属是本日的关键纠错。旧 [4 月 5 日原始筛选材料](../_sources/daily-20260405/)按 arXiv v1 提交/版本字段读出 `423` 条窗内 identity、`221` 条注册项、`17` 个旧候选；后来 [旧版日报存档](../_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-04-05.md)则按 DataCite DOI `created` 代理得出 `0`。两套时间字段都不是首次公开公告。本轮实际重核 arXiv [官方公告规则](https://info.arxiv.org/help/availability.html)：通常美东 Sunday～Thursday 20:00公告，补窗对应Friday12:00～Saturday12:00 EDT，下一正常批次为北京时间04-06 08:00，故补窗无常规batch。但这不证明特殊公告或机构独立首次公开不存在；四组限定主题补检未得到有效历史日期切片，单列检索限制，旧 `423/221/17` 不形成当窗全文队列，旧DOI-created `0` 也不代替本轮发现检查。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| `SRC-OPENAI` | 本轮[Research](https://openai.com/research/)HTTP403后web恢复；[Research Index](https://openai.com/research/index/)仅当前Oct7→Sep10首屏/Load more；[RSS](https://openai.com/news/rss.xml)实际完整解析可见items，相邻Apr2T10:30Z→Apr6T10:00Z。 | 受阻 | RSS无补窗项但不代替Research；历史分页切片隔离，需dated官方原稿/历史目录恢复。 |
| `SRC-ANTHROPIC` | 本轮[Research](https://www.anthropic.com/research)HTTP200，嵌入publishedOn实际Apr2T10:56Z emotion-concepts-function→Apr7T09:35Z mythos-preview。 | 已检查 | 当前官网目录无补窗条目，不证明未列作者研究为零。 |
| `SRC-GOOGLE-AI` | 本轮web实际恢复[四月Blog](https://research.google/blog/2026/04/)9卡，邻界Apr8 Academic Workflow→Apr3 behavioral dispositions；[DeepMind Publications](https://deepmind.google/research/publications/)精选首页Apr25/23/22→Mar22；[Google Publications](https://research.google/pubs/)2026年份409及主题filter，无日级切片。 | 受阻 | 有限Blog无补窗项；精选不代表全部，日级研究切片隔离；不遍历409全年库。 |
| `SRC-META-AI` | 本轮[Research](https://ai.meta.com/research/)web0行；[Publications](https://ai.meta.com/results/?content_types%5B0%5D=publication)web可见Oct2～Jul17后混入2019/2020，末Next，翻页未恢复。 | 受阻 | 不以非时间顺序首页代表Apr4历史停点；Research/publications日级切片隔离，需dated官方原件。 |
| `SRC-QWEN` | 本轮[官网retrieval](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)success=true，完整40项extra.date Apr2T04+08→Apr15T10+08跨窗。 | 已检查 | 当前公开模型列表无补窗卡片；不扫无触发的高频CLI/普通commit，不把旧58仓当本轮覆盖。 |
| `SRC-DEEPSEEK` | 本轮[News](https://www.deepseek.com/news/)及[主页](https://www.deepseek.com/)HTTP200；News Apr24 V4-preview→2025-12，主页研究footer仅项目入口无日级切片。 | 已检查 | 当前News目录无补窗项；不将footer或未公开作者稿当全部研究零证据。 |
| `SRC-MOONSHOT` | 本轮[Kimi Platform Blog](https://platform.kimi.com/blog)HTTP200完整可见目录，最新2025-11-07，相关Muon/MoBA为更早条目。 | 已检查 | 该目录无补窗项；不沿用旧43仓或全部CLI普通commit作为本轮扫描。 |
| `SRC-TENCENT-HUNYUAN` | 本轮[官方publicList](https://api.hunyuan.tencent.com/api/blog/publicList)POST pageNum1/pageSize100/renderType0，code0/totalNum9/list9；displayPublishTime Apr22T16Z→Feb13T08:36Z跨窗。 | 已检查 | 当前全部9条无补窗卡片；显示日、内部publishedAt与publicAt不混用，不以当前目录证明删改历史。 |
| `SRC-ZAI` | 本轮[Research](https://www.zhipuai.cn/zh/research)HTTP200，显示Apr1 GLM-5V-Turbo→Apr7 GLM-5.1；[release-notes](https://docs.z.ai/release-notes/new-released)Feb12→Apr7。 | 已检查 | 可见目录无补窗项；嵌入媒体Apr3 createdAt不是论文/研究公开事件。 |
| `SRC-BYTEDANCE-SEED` | 本轮[官方papers API](https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&order_desc=true&page_token=40)header x-tt-localeUS，实际18/total243/next60，整页最高Apr8T16Z Topological（AI for Science暂缓）；项目相关条目Not all tokens Apr7T16Z，后续列表邻界Mar31T12Z TDDFT（同属暂缓Science，仅作日期停点）；[Blog type2/page0](https://seed.bytedance.com/api/get_article_list_v2?article_type=2&count=20&order_desc=true&page_token=0)15/total95/next20，Apr8T16Z→Mar31T16Z。均已跨左界停止。 | 已检查 | 当前两目录无补窗卡片；相关slice不是整页最高日，不继承旧242，不把243全年库存变全文队列，PublishDate不独证首次正文公开。 |
| `SRC-BAIDU-ERNIE` | 本轮[博客](https://ernie.baidu.com/blog/zh/)HTTP200，entry-footer date Apr15→Feb6跨补窗而止。 | 已检查 | 当前技术博客无补窗条目；未触发则不扩普通commit队列。 |
| `SRC-XIAOMI-MIMO` | 本轮[官网](https://mimo.xiaomi.com/)HTTP200，8条Paper有原日期，June29 cross-model-distillation→Mar13 Agent Hologram跨窗；15条Blog（含blog-more隐藏区）都无原日期。 | 受阻 | Paper有限检查有效；无日期Blog不能证明Apr4历史停点，Blog日级切片单独隔离。获得dated官方原稿/历史目录再定点重开，不追15全文、不沿用旧18仓。 |
| `SRC-MINIMAX` | 本轮[英Blog](https://www.minimax.io/blog)/[中Blog](https://www.minimaxi.com/blog)HTTP200，Mar18→Apr27；[Agent techblog.md](https://agent.minimaxi.com/docs/techblog.md)仅Sep19/22、Oct8三项，当前llms索引无Apr4。 | 受阻 | 主Blog可见目录无补窗项；旧“Agent只见Apr27”未获当前支持，Agent历史技术博客切片隔离。 |
| `SRC-ARXIV` | 本轮重开[availability](https://info.arxiv.org/help/availability.html)及CL四月官方列表；补窗Fri12～Sat12 EDT无正常batch。四组模型/系统/多模态/Agent限定Apr4主题搜索返回十月页而非历史切片，查询/停止保于[原记录](../_sources/daily-20260405/SUP_SOURCES_20261013.md#本日限定主题补检与负样本校准)。 | 受阻 | 正常批次检查有效，但必要历史事件切片未恢复，特殊或机构独立首公开不由规则排除；不支持Apr4零论文/全学科召回。隔离、不造候选，未把整月宽列表变逐篇队列。 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

原唯一候选分母 **0** 保留，补窗确定新增 **0**；五类机构历史切片与arXiv检索限制不参加“零命中”算术。旧 `_sources/daily-20260405/` 的 17 个按 v1 字段形成的候选保留在原始材料，不机械转成当窗评分行；其中 `2604.03588v1`、`2604.03679v1` 的保存全文也只证明当时读过正文，不证明本窗口公开。

## 4. 证据与知识整合

没有经本窗事件日期与贡献筛选共同确认的候选，Books Decision 为 **No Change**，无书稿改动。旧 V2.1 中的 `Complete`、`Passed` 和 Books 决定不能代替本窗 V3 证据；若外部目录恢复出真正的当窗材料，先核其 Source Family 与贡献，再依三维评分决定审阅深度和章节判断。

## 5. 缺口与下一步

- 尚可执行：无。来源/筛选/证据/Books普通项0，无Books窄锁；root非报告作者完整六部分DAY已实际通过。本轮14个到期来源已有实际有限停点或隔离出口，没有拟入选材料需要进一步正文审阅。
- **终态保留项：** OpenAI Research历史分页、Google Research Publications日级切片、Meta Research/Publications日级目录、MiMo无日期Blog日级切片、MiniMax Agent旧技术博客历史切片。前两者的可见RSS/Blog不代替完整研究；Meta非时间顺序首页不证明历史停点；MiMo15条Blog无原日期，无法支持Apr4历史停点，不追15全文；MiniMax当前Sep/Oct三项不能恢复旧Apr27索引。五项分别隔离，**不用于正面证据、Books 或无遗漏断言**，不支持“全源零命中”。可接受替代：dated官方原稿/公告、可核同期官网存档或历史目录。获得明确落在04-04 BJT的身份/正文后只重开该源与family，不重跑其它来源。
- **arXiv发现限制：** 正常公告规则只支持无常规batch；有限四主题搜索实际不尊重Apr4文本日期，不能证明特殊公告或机构独立首次公开不存在。未发现确定的当窗材料，不造候选分母；若获得具体特殊公告/独立官网dated首次正文，只核该family和真实归属，不全扫整月宽列表。
- 窗外原始库存：旧 423/221/17 基于 v1 提交/版本字段而非公告；无需为了本日零常规公告逐篇全文复审。以后发现其真正公告日时，只在真实归属窗口定点处理。

## 6. 复核

复核者：root（非本补充报告作者）
结论：通过

本轮实际验收见[原来源记录的root六部分DAY](../_sources/daily-20260405/SUP_SOURCES_20261013.md#root实际六部分day通过)。root实际完整读六部分与14行有限入口/停止及关键原响应；独核Qwen40项、混元9/9、Seed18/243及15/95、Anthropic publishedOn、OpenAI RSS、MiMo8dated Paper/15无日期Blog和MiniMax三篇技术博客日期，重开arXiv规则、Google四月归档/Publications、Meta及OpenAI入口。MiMo无日期Blog误作历史停点与Seed相关slice误代表全页最高日两处已最小修正并实际读回。代表性Codex额度/PlanMode产品反馈独立前分母关闭；未逐篇审阅全年宽库或其余窗外附件，不把抽查称全量召回。五机构切片及arXiv历史事件限制继续隔离，不授其正面Coverage/Evidence或无遗漏。

原§4连续169字符（含标题185字符）、旧0候选及原窗口逐字保持，Books没有新写、无需实际POST。完成态V3、5个本地引用、限定cached/unstaged diff-check与冻结比较通过；机器不代替以上语义复核。作者已据实际DAY同步完成字段，root一次实际FINAL回读后再接纳全年日级计数；未stage、commit、push。
