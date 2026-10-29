# Daily Research — 2026-02-23

**规范：** V3
**窗口：** 2026-02-22T09:00:00+08:00 ～ 2026-02-23T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-05T11:46:34+08:00

## 1. 结论

本窗没有确认落窗且通过具体贡献筛选的材料，候选 0、证据审阅 0、Books 整合 0；因此没有必要书稿改动。这不是“全互联网没有新增研究”：十四个每日来源均进行了本窗有界检查，但七组历史目录或动态入口限制按 §5 隔离，不授正面 Coverage/Evidence、Books 或无遗漏保证。

官方 arXiv 周日 20:00 美国东部时间的公告映射到北京时间 **02-23 09:00**，恰为本窗不含的终点；本窗没有标准 new/cross/replacement 公告批次。OpenAI RSS 和 Anthropic 原始 `publishedOn` 恢复的最近前后事件也均在窗外。索引日期、后来的研究目录入库和当前版本不可把这些材料移动到本日。

本轮重新核验来源，不继承旧 V2.1 报告“仅 arXiv required”“所有 Gate 通过”的声明。没有把机构全年论文、抓取响应或 GitHub 空 commit 列表当作当天新论文或全部题摘已审。非作者日级复核通过，普通待办 0；外部保留项不混同于普通待办，亦不授正面覆盖通过。

## 2. 来源覆盖

本次主题为模型架构与表示、预训练/后训练、训练推理运行时、多模态生成/World Model/VLA、Agent 执行与评价。仅每日来源及出现的具体线索；每周和会议来源未常规扫描。原始请求、响应和停止位置见 [本日来源记录](../_sources/daily-20260223/V3_SCREENING.md)，以及 [首次请求](../_sources/daily-20260223/V3_NATIVE_FETCH.json)、[定点恢复](../_sources/daily-20260223/V3_NATIVE_RECOVERY.json)、[最后恢复](../_sources/daily-20260223/V3_NATIVE_FINAL_RECOVERY.json)与[补充请求](../_sources/daily-20260223/V3_NATIVE_EXTRA.json)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/news/research/)进入[完整 RSS](https://openai.com/news/rss.xml)，实际核本窗相邻发布：First Proof 02/20 14:30Z；Frontier Alliance 02/23 05:30Z、SWE-bench Verified 02/23 11:00Z。RSS 全响应内本窗无项目相关事件；不把后来 02/23 文章提前。 | 已检查 | 无；只代表该官方 feed 的发布记录 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)原始页面中的发布列表与 `publishedOn`；02/18 measuring-agent-autonomy 15:10Z → 02/23 AI-fluency-index 11:52Z/persona-selection-model 11:53Z，没有窗内记录。 | 已检查 | 无；不是对全站未列出材料的保证 |
| SRC-GOOGLE-AI | [Research Blog page 6](https://research.google/blog/?page=6)实际读到 Feb17 Teaching AI to read a map → Mar4 Teaching LLMs to reason like Bayesians 的相邻卡片，窗内无 Blog 条目。DeepMind当前目录及 RSS 返回 HTML，另 feed 404、page6～8不可恢复；Google Publications 当前首页只有年/会议日期，`year=2026`并未成为日窗口过滤。 | 受阻 | Google/DeepMind 历史论文与完整日期切片；G1 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)及[Blog page 2](https://ai.meta.com/blog/?page=2)；后者实际达到02/09 DINO greenspaces与03/11 MTIA，列表同时混入2025条目，不能据它证明完整历史召回。日期搜索只作补线索。 | 受阻 | 历史 Research publications 的日级切片；G2 |
| SRC-QWEN | [旧 Blog](https://qwenlm.github.io/)已提示新站；[qwen.ai Blog](https://qwen.ai/blog)及具体 qwen3.5入口只能恢复客户端壳。Qwen3.5精确窗口的 GitHub commit 首页 `[]`，没有可触发的具体变更，不据空列表授全机构覆盖。 | 受阻 | 新站历史发布目录/日期；G3 |
| SRC-DEEPSEEK | [主页](https://www.deepseek.com/)当前模型入口及 DeepSeek-V3.2 精确窗口 commit 首页 `[]`；日期限定官方搜索未恢复当窗具体研究事件，未遍历全组织。 | 受阻 | 官网缺完整历史研究发布切片；G4 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)实际显示条目最新2025/11/07；Kimi-K2.5精确窗口 commit 首页 `[]`；不是2026全机构目录。 | 受阻 | 2026历史发布目录切片；G5 |
| SRC-TENCENT-HUNYUAN | 先查[Research](https://hunyuan.tencent.com/research)；浏览器两次超时，一次子线程可见性不支持。官方 `api.hunyuan.tencent.com/api/blog/publicList` pageNum1/pageSize100/renderType0恢复英文全部9条，最邻近窗前Token-level Gradient Diagnosis 02/13 08:36:03Z、窗后04/22；Accept-Language中文重试仍返回英文9条。另定点核前次同原源[中文11条响应](../_sources/daily-20260222/V3_NATIVE_hunyuan_zh.txt)的相邻发布日期02/13 08:36:34Z→04/22显示日期，复用具体边界而非前日报候选/结论。 | 受阻 | 中文11条是前次执行响应，当前英文9条及前次中文集不授当前“全部”覆盖；G6 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)时间排序当前15张卡片实际到02/21 GLM-5技术报告→03/15 GLM-5-Turbo；[release notes](https://docs.z.ai/release-notes/new-released)02/12→04/07无窗内事件；GLM-5窗口 commit `[]`。 | 已检查 | 无；02/21目录日期不是本窗修订事件 |
| SRC-BYTEDANCE-SEED | 原始论文/Blog API，2026、order_desc=false、page_token=0；请求count100实际每页上限20。论文第1页20张卡片从01/20到02/25，窗前02/13 FLAC→窗后02/25 FlowPortrait/World Guidance，已越过终点；Blog实际9张从02/12→04/01后，亦越终点（响应has_more/next token保留，不再翻窗外页）。 | 已检查 | 无；仅本窗切片，不将API display日或入库时间当首次公开 |
| SRC-BAIDU-ERNIE | [Blog第一页](https://ernie.baidu.com/blog/zh/)实际核02/06 ERNIE5.0→04/15 ERNIE-Image相邻日期；PaddlePaddle/ERNIE窗口 commit `[]`，无具体重要变更线索。 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | [主页](https://mimo.xiaomi.com/)路由与[Blog](https://mimo.xiaomi.com/blog)可读的唯一发布为2025/12/16 MiMo-V2-Flash；MiMo-V2-Flash窗口 commit `[]`。 | 受阻 | 无可证明2026/02完整历史发布切片；G7 |
| SRC-MINIMAX | [英文 Blog](https://www.minimax.io/blog)、[中文 Blog](https://www.minimaxi.com/blog)实际到Forge英02/14/中02/12、M2.5 02/12；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)只有05/13分组，不能反推为02/22事件。MiniMax-M2.5窗口 commit `[]`。 | 已检查 | 无当窗新事件线索；Forge中英日期差均窗外，不为解决本窗不存在的归属扩读 |
| SRC-ARXIV | [官方公告安排](https://info.arxiv.org/help/availability.html#announcement-schedule)明确包括new/replacement/withdrawal/cross；周末无标准公告，下一次Sunday20ET=本窗终点。另以同前缀DataCite `created:[02/22 01:00Z TO 02/23 00:59:59Z]`单页恢复线索，total0/end；无可触发的具体题名，不扫描后窗分类批次。 | 已检查 | DataCite不是首公开权限；此结论只针对标准公告批次，不保证没有非标准原源公开 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

无确定落窗贡献候选。不对窗外标题、客户端目录、空搜索或无法恢复的历史切片评分；没有用版本名、映射 owner 或机构声望制造候选。§5的限制不是候选，也不是证据已完成项。

## 4. 证据与知识整合

没有候选需要标准/深入审阅，也没有需要新写入或声称已有覆盖的 Books 命题。此次 Books 决定为 **No Change**；不是因“历史任务”跳过 Books，也不是拿相似主题替代 owner 对读。

日期判断有如下可复查原源边界：

- arXiv `availability` 原文“scheduled announcement process”包含首次公开、replacement、withdrawal与cross；本窗从美国东部周六02/21 20:00到周日02/22 20:00，后一时刻不含。原始页面及DataCite辅助请求分别保存在本日 `V3_NATIVE_availability.txt`、`V3_NATIVE_arxiv_datacite.txt`。无需逐项读取02/24的后窗标题或把提交时间填成公开时刻。
- OpenAI RSS 的GMT时间直接换算+08；Anthropic列表读取的是`publishedOn`，而不是插图`_createdAt`、页面更新或搜索缓存日期。两者恢复的最近事件均不落窗；没有审阅它们的正文并冒充本日证据。
- Seed原始`PublishDate`只是显示日期与恢复入口，页面`UpdateTime`/ArticleID也不证明首次公开。此处只用已越过本窗的排序切片说明没有新线索，不为任何候选授首公开时刻。
- Z.ai的02/21 GLM-5目录条目与02/12发布说明都早于窗口。窗口GitHub响应无新commit，因此不存在已观察到、需本日重评的修订；不宣称版本永久不变。

## 5. 缺口与下一步

可执行工作：无。非作者已复核实际有界入口、空拟入选集、日期与代表排除；没有尚未审完的候选、可执行全文队列或 Books 写入。

以下为本窗终态保留项（外部限制），已经尝试原入口与有限定点恢复，不支持正面证据、Coverage、Books或无遗漏断言。以后只恢复对应源在本窗的材料：

| 保留项 | 原入口与缺少什么 | 当前不能采用的原因与替代材料 | 定点重开条件 |
| --- | --- | --- | --- |
| G1 Google/DeepMind | [Publications](https://research.google/pubs/)历史日切片和[DeepMind目录](https://deepmind.google/blog/)在02/22～23的完整发布列表 | 当前Google列表年/会议精度且过滤未生效；DeepMind历史分页未恢复，不能靠搜索空结果推断无论文。允许官方日期索引或具体作者原文+首次公开字段替代。 | 取得覆盖本窗的原始日期列表，或出现具体窗内题名，只重开对应事件 |
| G2 Meta/FAIR | [Research publications](https://ai.meta.com/research/publications/)的本窗历史索引 | Blog2日期非完全顺序，不等于论文目录；当前Research首页无窗内可归属事件。允许官方论文页及精确初公开字段。 | 恢复本窗日期切片/具体窗内材料 |
| G3 Qwen | [新Blog](https://qwen.ai/blog)历史发布列表与公开时间 | 客户端壳不含列表；旧站已迁移；单一Qwen3.5空commit只限制该repo，不能代表机构。允许官方blog历史数据或具体model/research发布原文。 | 取得本窗原始列表或具体窗内发布+精确公开字段 |
| G4 DeepSeek | [官网](https://www.deepseek.com/)历史研究公开列表 | 当前产品首页与V3.2空commit不是历史全集；允许官方research/model页面、release或精确原稿日期链。 | 具体窗内原源或日期索引到达 |
| G5 Moonshot | [Platform Blog](https://platform.kimi.com/blog)2026历史发布切片 | 当前列表停2025；K2.5空commit不证明无其他项目。允许官方research/model发布页及精确初公开字段。 | 恢复本窗2026目录或具体事件 |
| G6 Hunyuan | [Research“全部”](https://hunyuan.tencent.com/research)中文历史目录 | API英文9条可读，中文重试仍英文；浏览器受限/超时，不能把英文集写成“全部”。允许官方中文列表响应或具体论文原文及公开字段。 | 取得中文“全部”历史切片，只检查本窗和具体相关线索 |
| G7 MiMo | [主页](https://mimo.xiaomi.com/)本窗历史发布切片 | 可读Blog只有2025/12/16；空commit不覆盖全部官方发布。允许官方历史blog/model/research记录。 | 取得本窗列表或具体窗内原源 |

窗外恢复线索不属于本窗：OpenAI SWE-bench Verified为02/23 19:00+08，归02/24默认Daily；Anthropic AI-fluency-index/persona-selection-model为02/23 19:52/19:53+08，亦归02/24。本日只记路由，不对后窗候选、正文或Books作判断。

## 6. 复核

复核者：root（非报告作者）。
结论：通过

实际检查范围：完整六部分及本日来源停点；十四个每日入口请求与响应相关段；arXiv官方安排和半开终点、DataCite恢复权限；OpenAI XML精确时间、Anthropic三项相邻publishedOn；Google Blog6相邻卡片、Seed全部20/9条日期及pinned/next、Z.ai15卡片与release边界、Hunyuan本次9条及前次中文11条相关时间字段；ERNIE/MiMo/Moonshot日期、Qwen客户端壳、Google Publications年精度以及七个repo实际空commit响应。空拟入选集合全部覆盖，证据/Books队列为空成立。代表旁证按来源记录7行的实际日期与核心说明范围核对，包含Meta DINO应用和MiniMax Forge中英窗外日期；不是7项本窗候选或全站逐篇验证。G1～G7明确隔离，不授正面覆盖或无遗漏。本日没有Books实际写回。

机器校验：`python3 scripts/validate_research.py --report papers/2026/02/23/README.md`完成态V3通过；本日README与_sources限定cached/unstaged `git diff --check`通过。机器结果不替代上述非作者语义复核。本轮不修改共享索引、LEARNING_STATE、其他日报或Weekly，不stage、commit、push；既有修改保护。
