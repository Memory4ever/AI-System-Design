# Daily Research — 2026-04-19

**规范：** V3
**窗口：** 2026-04-18T09:00:00+08:00 ～ 2026-04-19T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-27T18:36:00+08:00

## 1. 结论

本窗确认一项官方模型发布：Qwen3.6-Max-Preview，原始时间为04/18 10:00北京时间。实际读完官方正文后，它提供新checkpoint、托管调用与作者benchmark，没有披露足以改变模型机制、训练/推理设计或Agent执行合同的独立长期增量，因此在贡献分母之前关闭，不给纯发布版本套长期评分。当前确定贡献候选为0，证据审阅与必要Books新增为0；不是说本窗没有任何模型活动。

本窗对应EDT周五04/17 21:00～周六04/18 21:00，官方说明周五/周六没有常规arXiv公告，新提交、replacement与withdrawal均走公告过程。旧441个submitted-day身份是提交线索，不是当日公开论文，更不构成全文队列；定点核原始日期发现16802/17182的v1 Updated在04/21，24777延迟至04/29。这里不以Updated单独改名first-public，而把官方公告规则、身份与日期链分开保存。旧0/Complete也不继承。

十四个Daily来源已处理到可复查目录停点或精确限制。未变化且跨本窗的原始目录可复用，Qwen新事件重新打开；没有重扫Weekly来源或所有组织commits。五个历史覆盖限制仍不支持无遗漏或Books正面结论。root非作者日级验收已通过，普通待办为0；旧报告无损保存在[保存稿](../_sources/daily-20260419/V2_1_README_BEFORE_V3.md)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 复用[04/18实际记录](../_sources/daily-20260418/V3_REVIEW_CHECKPOINT.md)：完整[News RSS](https://openai.com/news/rss.xml)1230项，04/16T10:00Z→04/20T00:00Z跨本窗；本窗没有RSS条目。原Research入口403 | 受阻 | RSS不替代Research历史分页；需该研究目录本窗原始列表/存档才重开其覆盖 |
| SRC-ANTHROPIC | 复用已核[Research](https://www.anthropic.com/research)HTML publishedOn邻界04/14T13:01Z→04/22T14:12Z/14:27Z，两端不与本窗相交 | 已检查 | 仅支持可见官网研究目录本窗无项，不外推未列作者稿 |
| SRC-GOOGLE-AI | 本次打开[Research四月页](https://research.google/blog/2026/04/)9项，04/16→04/21跨窗；复用[DeepMind真实page3](https://deepmind.google/blog/page/3/)04/15→04/22及七项April原文已核日期，均窗外；Publications year参数返回771页泛目录 | 受阻 | 两官方Blog停点有效；Publication缺本窗首公开日级停点，不扩全年逐篇审阅 |
| SRC-META-AI | 复用[Research](https://ai.meta.com/research/)空提取、[Blog](https://ai.meta.com/blog/)及[page2](https://ai.meta.com/blog/?page=2)混排April08/06、July和March27；Publication恢复超时 | 受阻 | 没有可靠本窗历史排序/分页，不用空页或混排旧条目证明无更新 |
| SRC-QWEN | 本次实际GET[动态retrieval](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)40项，并完整读Max-Preview正文及JSON-LD；extra.date和datePublished均04/18T10:00+08。复用静态60项最晚2025-12-23、动态相邻04/22T10+08及组织完整created-desc/release停点 | 已检查 | 命中1项本窗模型发布，具体贡献关闭见§4；API coming-soon与available措辞不作为已稳定部署证明，不继承当前仓库名证明历史提交 |
| SRC-DEEPSEEK | 复用[官方news](https://www.deepseek.com/news)动态04/24→2025-12-01、研究索引06/24→02/25，以及39仓库至2023-10-20；均跨本窗 | 已检查 | 可见官网目录/新仓库没有本窗项，不外推全部未列研究 |
| SRC-MOONSHOT | 复用[Kimi Blog](https://platform.kimi.com/blog)26项止2025-11-07；43仓库created-desc至2023-03-28、[Kimi-K2.5 release页](https://github.com/MoonshotAI/Kimi-K2.5/releases)无release | 受阻 | Blog缺2026历史停点；仓库/release不能补造研究Blog覆盖 |
| SRC-TENCENT-HUNYUAN | 复用官方POST[publicList](https://api.hunyuan.tencent.com/api/blog/publicList)pageNum1/pageSize100/renderType0，totalNum9/list9，04/23→02/13跨窗；组织83仓库最近HY-SOAR创建04/16T06:34Z在窗前 | 已检查 | “全部”公开目录本窗无项；仓库创建事件不回拨论文first-public |
| SRC-ZAI | 复用[官方Research](https://www.zhipuai.cn/zh/research)15项04/29→04/07→04/01、[release notes](https://docs.z.ai/release-notes/new-released)06/16→04/07→02/12、53仓库到2021；均跨窗 | 已检查 | 仅这三个官方目录没有本窗可见项，不写全网零研究 |
| SRC-BYTEDANCE-SEED | 复用实际官方[get_article_list_v2](https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&order_desc=true&page_token=20)，x-tt-locale US；papers page20的20项05/13→04/09，邻界04/20→04/16；blog type2 page0/20 total95，04/23→04/09→04/01，page20至2025 | 已检查 | PublishDate自然日桶不充当精确首发；邻界不与本窗相交，不复审窗外Seedance全文 |
| SRC-BAIDU-ERNIE | 复用[Blog第一页](https://ernie.baidu.com/blog/zh/)10项，04/30→04/15 ERNIE-Image→02/06→2025-11，已有有序跨左界停点 | 已检查 | ERNIE-Image自然日04/15在本窗前，不为旧窗外发布重建时刻 |
| SRC-XIAOMI-MIMO | 复用[官方首页](https://mimo.xiaomi.com/)Paper8项06/29→03/13→02/03，Blog14无历史日期；组织18仓库到2025-04-26 | 受阻 | Paper/新仓库停点有效；无日期Blog缺本窗历史公开依据 |
| SRC-MINIMAX | 复用[英文Blog](https://www.minimax.io/blog)12项05/26→03/18、[中文Blog](https://www.minimax.cn/blog)13项04/27→03/18、[Agent Tech](https://agent.minimax.io/docs/techblog)当前一项2026-05-13和35仓库到2025；均跨窗 | 已检查 | 仅支持当前可见两语言/AgentTech/新仓库范围，不证明历史删除条目不存在 |
| SRC-ARXIV | 本次实际打开[官方availability](https://info.arxiv.org/help/availability.html)§Announcement Schedule/ID assignments；本窗EDT Fri21:00～Sat21:00没有常规公告。只定点核旧20身份线索中的16802/17182官方abs-v1，及原始登记边界16765/16802/17182/24777；未扩441全文 | 已检查 | 正常公告规则不证明互联网上绝无例外；具体提前公开/重要修订原始线索出现时只重开相应家族。submitted/DOI登记不当公开时刻 |

复用范围是原始目录条目和已核未变日期，不是04/18日级Gate。八机构组织列表的有限完整created-desc与已触发release页只支持其实际停点；本次没有新增artifact机制触发，不遍历一般commits或给全部仓库加隐藏待办。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

当前没有经过日期与贡献双重筛选的本窗候选。Qwen发布是来源真实命中、贡献前关闭，不填0分或冒充已审候选；旧20个submitted-day入选记录不是V3当窗候选。

## 4. 证据与知识整合

### [Qwen3.6-Max-Preview官方发布](https://qwen.ai/blog?id=qwen3.6-max-preview)：来源命中，贡献前关闭

实际官方retrieval返回原始正文，articleBody及Performance、Build、API Usage、Summary均已读；extra.date、article:published_time和JSON-LD datePublished同为2026-04-18T10:00:00+08:00。它说明proprietary preview的作者能力结果、托管调用、preserve_thinking及兼容API，但没有公开使知识、Agent编码或训练机制判断改变的方法与受控解释。preserve_thinking已是此前Plus/35B接口说明中的能力，不因新checkpoint再当独立机制。新版本存在不是无价值，但不满足本项目长期贡献准入；作者benchmark与推理模型/harness配置不足以推出通用设计结论。本轮不评分、不入Books，也不因为未披露机制制造访问受阻。

正文同时写coming soon/stand by与available，故只保留已公开preview事件，不把措辞冲突外推成稳定production API可用性。这里没有实施API调用、性能测量或新部署；其兼容样例也不能证明不同provider端到端状态/工具效应等价。

### arXiv公告与旧submitted库存

官方原始说明将新提交、replacement、withdrawal及cross-list归于公告流程，永久ID在公告时赋予，不能提前分配或回填月份；周五/周六没有常规公告。本窗没有正常batch，提交时间仍只作provenance。旧screening-ledger的441个身份由submitted日期得到，含16765～24777；它们不应因旧“完整语义筛选”标记自动成为本窗必须深读材料。

本次定点实际核[16802v1](https://arxiv.org/abs/2604.16802v1)、[17182v1](https://arxiv.org/abs/2604.17182v1)原版本页及DataCite原字段：16802 Submitted=04/18T03:22:10Z、v1 Updated=04/21T00:28:10Z、created=04/21T03:49:42Z；17182 Submitted=04/19T00:56:08Z、v1 Updated=04/21T00:55:48Z、created=04/21T03:58:24Z。原始边界16765亦在04/21，24777延迟至04/29。字段没有被改名公告日志；它们与官方正常slot/ID分配相容，说明旧提交桶不能定本日报first-public。特别是24777不能机械迁到下一日。其他旧20身份留作恢复线索，不用个别字段替20条证明精确owner，后续处理真实窗口时只核各自必要日期与贡献。

本次没有任何这些旧论文的正面机制采用或Books写入；有效旧正文保留，不因日期纠偏删掉它们，也不从旧Weekly反推本日。若机构目录恢复出本窗独立提前公开正文，应按该事件重新判断，不将arXiv常规周历当作跨网站绝对证明。

### Books判断

Books纳入本次流程，但没有确定贡献候选支持新增正文，故本轮不修改章节。不是用“主题已有”结束一个实际新反证，也没有写虚泛“已吸收语义增量”。非作者已核来源、版本发布关闭、日期推理与Books空集的采用边界，本日按合同完成。

## 5. 缺口与下一步

普通扫描、事件贡献处置与非作者日级语义复核已完成，没有未处理的可执行工作。以下五个本窗外部覆盖缺口均为终态保留项，不支持正面证据、Books或无遗漏断言；各项定点重开条件如下：

- **OpenAI Research**：缺本窗官方历史Research分页/清单；RSS只证明其自身范围。取得原始历史列表及本窗停点后定点重开，不无限循环403。
- **Google Publications**：year参数泛目录缺日级首公开依据；需要本窗公开列表/可靠日期与有限停点。两官方Blog停点不代替Publication覆盖。
- **Meta**：Research空提取、Blog混排及Publication超时不足以证明窗口；需可靠历史排序/分页或原始本窗清单。
- **Kimi Blog**：26项止2025不能证明2026本窗；需官方2026历史目录/可验证发布时间，组织/release不替代Blog。
- **MiMo Blog**：14入口没有日期，需原始发布时间或历史列表；Paper/新仓库停点仍有效。

旧441 submitted身份及20旧候选为窗外/归属未证的恢复线索，不阻塞本窗，也不写成已审重复事件。只有恢复出的具体公开时间与本窗相交才重开本日，普通贡献材料由真实owner日继续，不扩整月/全年或全部版本史。

## 6. 复核

复核者：root（非报告作者）。

结论：通过

作者恢复后实际重读当前AGENTS、三合同、统一Prompt、Daily14/arXiv与ROADMAP及最新checkpoint；重新取得Qwen官方40项目录与Max-Preview完整正文，日期仍为04/18T10:00+08。root独立GET同一官方retrieval并核完整原文、JSON-LD日期与版本事实/作者benchmark/已有preserve_thinking，具体贡献关闭成立，coming-soon/available冲突未被用作部署事实。root核对十四来源实际停点、五项隔离、周末公告边界与旧submitted不当公开的处理；未变化的04/18有效来源核验复用，未宣称重新抓取全部目录。0候选、1来源事件前关闭和0必要Books一致；普通待办0，外部限制不支持零遗漏。当前validator及scoped git diff --check通过，机器校验不替代上述语义验收。旧报告和证据无损保留，不stage、commit或push。
