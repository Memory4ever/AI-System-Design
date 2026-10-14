# Daily Research — 2025-11-14

**规范：** V3
**窗口：** 2025-11-13T09:00:00+08:00 ～ 2025-11-14T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-04T18:10:07+08:00

## 1. 结论

本窗确认3个材料家族，必要审阅均完成：SIMA2虚拟环境内的代际经验训练路径仅报告；Anthropic所报告的总体恶意目的隐藏于子任务的失效案例具体已有覆盖；OpenAI训练时weight sparsity的解释性分支整合1项。三项日期、准入、必要Blog证据与具体owner处置已由root分批独立通过。稀疏由root实际核真实Ch5差额并窄写，非写入者Planck正文/邻接/末注/Ch4与6交接POST通过，唯一末注已落盘。共享Books整合1项不是本作者写入，不因产品名缺位强造更新；root于18:02:00完成实际六部分日级独立复核，结论通过，见[DAY_REVIEW](../_sources/daily-20251114/DAY_REVIEW.md)。

arXiv四组发现响应为60/1/16/12（跨组未去重，非本日论文数）；泛RL/蒸馏收窄后模型组36/36，CL月表仅56条指定ID切片标题查漏。只选择19家族读精确v1完整题摘，具体潜力、当前信号及日期终态隔离已由root实际独立核；首次公开未确认，不算确定候选，不扩成全类全文队列。另2个完整题摘关闭样本的具体理由独立通过。GPT-5.1 API的RSS原值为Nov13 00GMT=BJT08窗外，不用官网日粒度替它赋14日归属。

本日研究、Books及语义复核普通待办为0。MiniMax Agent Tech有限检查及Google来源组受阻两处修正已由root实际核验通过，Blog不替pubs组。历史目录、arXiv首公开及后续稿为§5具名终态保留；这些限制不支持正面Coverage/Evidence、Books、无遗漏、性能或安全保证，材料到达后仅定点重开。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/) 当前入口与官方RSS本窗日期筛选；RSS窗内仅sparse 10GMT，API午夜窗外；Blog核心及group-chat说明定点读。见[原入口](../_sources/daily-20251114/raw-web-00.json)、[RSS](../_sources/daily-20251114/raw-openai-rss.xml)与[首批](../_sources/daily-20251114/FIRST_CALIBRATION_READY.md)。 | 已检查 | 当前目录/RSS不能保证历史删除项；sparse后续Nov17稿不倒填。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 当前HTML的原生日期本窗筛选，无相应日期记录；实际触发[News原帖](https://www.anthropic.com/news/disrupting-AI-espionage)，核Nov13 16Z、Nov14纠错与当前PDF修订。 | 已检查 | Research当前字段切片不是历年完整性；Nov13原PDF未恢复，采用已限于博客失效路径。 |
| SRC-GOOGLE-AI | [DeepMind Research](https://deepmind.google/research/)与[Google Pubs](https://research.google/pubs/)作为主线标题入口；[2025 Blog p1](https://research.google/blog/2025/)读到Nov12边界，不把676条年度pub slice转题摘。SIMA2原生18:55Z；Nov13森林标题关闭，quantum核心读后仅DQI/OPI/XORSAT无基础模型/系统增量关闭。见[raw09](../_sources/daily-20251114/raw-web-09.json)。 | 受阻 | 必要pubs历史本窗切片未恢复；已检查Blog不替整个来源组Coverage。SIMA当前Dec5报告与Nov13原件分开。 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)返回无可读正文；一次官方限定查询 `site:ai.meta.com/research "November 13, 2025" (model OR training OR inference)` 返回空，[raw22](../_sources/daily-20251114/raw-web-22.json)。 | 受阻 | 无可核的本窗历史研究段，空搜索不证明0研究。 |
| SRC-QWEN | [旧入口](https://qwenlm.github.io/)当前36条最新到Sep23；[新Research](https://qwen.ai/research)实际200 HTML壳无可读列表；官方限定 `site:qwen.ai/research "2025-11-13"` 空，raw22。 | 受阻 | 动态/历史Research未恢复；浏览器不可用，不反复空路径。 |
| SRC-DEEPSEEK | [主页](https://www.deepseek.com/)403；[官方updates](https://api-docs.deepseek.com/updates)实际当前Dec1→Sep29的日期边界，无Nov13保留项，见[raw](../_sources/daily-20251114/raw-deepseek-updates.html)。 | 已检查 | 仅当前官方updates返回范围，不替历史论文/删除记录完整性。 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog)实际26条日期/标题，最近Nov7/6再到Sep5，停止当前列表；没有由本窗研究触发GitHub release扩查。见[raw01](../_sources/daily-20251114/raw-web-01.json)。 | 已检查 | 当前保留目录不是历史无删除保证。 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)无可读列表；浏览器实际不可用。publicList POST `{pageNum:1,pageSize:20,renderType:0}` 实际9条均2026，止p2；官方本日限定查询空，raw22。见[raw API](../_sources/daily-20251114/raw-hunyuan-p1.json)。 | 受阻 | 该API当前博客不能恢复2025 Research；不读2026正文或称本日0。 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)与真实 `?page=2`，hydration累计18身份、hasMore=false，最早createAt Dec7，停止p3；release notes Dec8→Sep30不替Research。见[尾部](../_sources/daily-20251114/SOURCE_TAIL.md)。 | 受阻 | 已穷尽当前返回目录，November历史段未恢复。 |
| SRC-BYTEDANCE-SEED | 前端真实GET `get_article_list_v2`，type2/1、publish_year2025、count20、page_token0/20、order_desc=true、x-tt-locale US。blog18/18、paper18/20；p0最近非置顶Oct22/21，p20到June，pinned未来项隔离；has_more=true但已越过窗下沿，止40。见[blog0](../_sources/daily-20251114/raw-seed-blog-p0.json)、[paper20](../_sources/daily-20251114/raw-seed-paper-p20.json)及request。 | 已检查 | 当前年目录有限范围，不保证删除/迁移历史；不因has_more扩大到全年正文。 |
| SRC-BAIDU-ERNIE | [中文Blog](https://ernie.baidu.com/blog/zh/)p1最低Nov21，实际p2六项由Nov11/7到June2，显示2/2结束，止p3；只查日期与主题标题，raw01。 | 已检查 | 当前两页保留目录，不证明历史无删除。 |
| SRC-XIAOMI-MIMO | [首页](https://mimo.xiaomi.com/)Paper8项到Oct21；Blog15标题无日期；实际引用脚本恢复 `/blog/` route，GET200却返回Dec16 MiMo-V2-Flash单篇，身份不符，不使用窗外正文。见[尾部](../_sources/daily-20251114/SOURCE_TAIL.md)。 | 受阻 | 本窗历史Blog日期段不能由错误SSR路由恢复；有限尝试已停。 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)12条与[中文](https://www.minimaxi.com/blog)13条，Dec23跨Oct27到Jan15、无分页。另实际首查[Agent Tech](https://agent.minimax.io/docs/techblog)200，web空列表后沿其提供的llms索引与techblog.md，实际仅1条2026-05-13 Agent Team；停当前索引，不读窗外正文。见[raw26](../_sources/daily-20251114/raw-web-26.json)、[原目录](../_sources/daily-20251114/raw-minimax-agent-tech.md)。 | 受阻 | 双语目录有限已查，但Agent Tech必要2025目标段未恢复；不是未触发或不适用，不以当前2026条目推断2025无事件。 |
| SRC-ARXIV | 12分类的训练/推理/Agent/多模态四组，submitted `[20251111190000 TO 20251112185959]`仅发现，start0/max100/ascending；各返回未满100，停止start100。模型窄化36条；CL月表ID08700–09599标题56条补检；选择19个exact-v1完整题摘并一次current-comment信号检查。见[筛选](../_sources/daily-20251114/ARXIV_SCREENING.md)及全部query/request raw。 | 受阻 | 官方月表无Thu13公告身份，日路径400与有限官方搜索空；19个首公开下界未确认，隔离，不声称本窗全分类覆盖。 |

按需组未触发新的会议公开批次、协议/release或评测suite变化扫描。cyber提到MCP仅作案例背景，候选原件/作者project定点打开不触发全站或Weekly扫描；没有将发生过的触发取消。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [SIMA 2: An agent that plays, reasons, and learns with you in virtual 3D worlds](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/) | 2025-11-14T02:55:00+08:00 | 人工示教后的teacher任务/估计reward与自玩经验进入后续代训练分支；2+2+2=6 | 标准完成 | 仅报告：公开说明支持虚拟环境实例，未给可改变现有长期链的具体筛选/优化或受控预算机制；不倒填Dec稿。 |
| [Disrupting the first reported AI-orchestrated cyber espionage campaign](https://www.anthropic.com/news/disrupting-AI-espionage) | 2025-11-14T00:00:00+08:00 | 看似正当子任务隐藏总体恶意目的的组合语义失效案例；2+2+2=6 | 深入完成 | 已有覆盖：`AGENT-PLATFORM`，[Ch84](../../../../books/part-07-agent/84-agent-platform.md)的独立effect authority、不可表达语义风险的拒绝/人工/只读边界；不是全局恶意目的已被解决。 |
| [Understanding neural networks through sparse circuits](https://openai.com/index/understanding-neural-networks-through-sparse-circuits/) | 2025-11-13T18:00:00+08:00 | 将weight连接稀疏约束放进训练形成表示阶段，而非仅事后dense分解；2+1+2=5 | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION`，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)原Superposition两段后融入训练时连接约束及成本边界两段；root写前核验、非写入者实际POST及唯一末注同步已落实。 |

## 4. 证据与知识整合

### [SIMA 2: An agent that plays, reasons, and learns with you in virtual 3D worlds](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)

只采用博客披露的示教→teacher反馈/自玩经验→后续代训练路径。新评价集合重测SIMA1、held-out游戏与Genie展示分开；短记忆/低延迟及长程核验限制保留，不给物理迁移、总预算相同或reward真值保证。当前技术稿封面/制作日期Dec5、存储修改Dec8，不是已核Nov13原稿，隔离其中细节。必要原源位置、有限恢复和Ch26数据provenance/生成环境段的具体对读见[证据包](../_sources/daily-20251114/BLOG_EVIDENCE_OWNER_READY.md)。root实际核官方核心与Ch26/25真实论点，有限增量未形成新长期筛选/优化实现差额，正式仅报告通过，不抹去局部训练增量；[独立尾部](../_sources/daily-20251114/TAIL_INDEPENDENT_REVIEW.md)。

### [Disrupting the first reported AI-orchestrated cyber espionage campaign](https://www.anthropic.com/news/disrupting-AI-espionage)

采用厂商报告的子任务上下文隐藏失效，不采用当前晚版PDF的精细跨session架构或修订国家归因。80–90%是厂商工作估计，非自主成功率；虚构credentials、公开信息误报及Claude-only可见性是直接反侧。Nov14已纠正请求速度，旧“千次/秒”废弃，节奏也不能证明自主能力。Ch84具体已有的proposal/effect enforcement与语义风险人工回退支持该处置，不声称任一primitive policy能识别全部组合意图；见[安全/owner包](../_sources/daily-20251114/BLOG_EVIDENCE_OWNER_READY.md)。root实际重核原核心及Ch84/83真实交接，具体已有覆盖通过，无改书/POST；组合恶意语义未解决边界仍保留，[独立尾部](../_sources/daily-20251114/TAIL_INDEPENDENT_REVIEW.md)。

### [Understanding neural networks through sparse circuits](https://openai.com/index/understanding-neural-networks-through-sparse-circuits/)

训练时weight连接约束不同于事后activation分解；手工任务上剪枝后维持与删边失效只支持该task/circuit，不是唯一算法。能力/解释性局部前沿与训练、部署成本限制必须相邻保留。Ch5已有容量/干扰与证据阶梯，root实际核定的长期差额是训练阶段连接约束及成本位置，而非重复成熟因果原则；因此在5分基础上深入受影响的有限核心，不改变评分。root已在Superposition原两段后融入两段并保留旧后训练coupling，来源与写前核验见[PRE](../_sources/daily-20251114/SPARSE_INDEPENDENT_PRE_REVIEW.md)。Planck作为非写入者实际顺读正文与邻接、末注、Ch4/6交接及原Blog限定，[POST通过](../_sources/daily-20251114/SPARSE_INDEPENDENT_POST_REVIEW.md)。作者于17:16:06实际读取Ch5第470行唯一末注，已明确记载17:02:54 POST通过、Blog采用边界和未复现；正式处置为整合。Nov17论文版本不冒充Nov13原件，也不因可选原件缺失阻断Blog有限命题。

## 5. 缺口与下一步

**普通可执行工作：** 无。root实际日级复核已通过；来源修正、3个确定家族的必要证据/Books处置及稀疏实际写后均已结束。以下为本窗终态保留项，不支持正面证据、Books或无遗漏断言；定点重开条件分别列于下文。不等待月计数，后续各日独立fresh推进。

**外部保留：** 19个arXiv潜力家族的精确身份/完整题摘和逐项增量在[ARXIV_SCREENING](../_sources/daily-20251114/ARXIV_SCREENING.md)。缺真实首公开下界；提交字段、一般schedule、DataCite注册及官方月表不足共同补造Thu13公告。一次日期路径400、有限官方历史/逐ID搜索及三精确原页已停，见[日期请求](../_sources/daily-20251114/ARXIV_FIRST_CALIBRATION_READY.md)。接受真实历史官方公告/list身份或作者原始精确发布时刻/完全落窗范围；仅重开到达的对应ID，不读取19份全文来替代日期，也不把它们称无贡献。当前不作正面证据、Books或覆盖保证。

**历史来源保留：** Google pubs、Meta、Qwen、Hunyuan、Zai、MiMo、MiniMax Agent Tech的必要历史段未恢复；当前HTML/接口/双语目录的实际有限边界见§2与[来源尾部](../_sources/daily-20251114/SOURCE_TAIL.md)。Google Blog不替pubs；Agent Tech当前唯一2026-05-13条目不补2025。接受官方本窗旧目录或具体带日期原文，到达后只重开该源/该项；不再试空路径，不从当前2026目录断言2025零命中。

**窗外及版本隔离：** GPT-5.1 API原RSS为Nov13 00GMT=BJT08，按实际字段在本窗之外；午夜精度若有官方说明才重开，不用官网Nov13日期覆盖。SIMA Dec5稿、sparse Nov17 arXiv稿及cyber Nov17修订PDF不当Nov13原件；当前报告不依赖其超出博客的算法/定量/归因。需要这些结论时，仅恢复精确历史原件，不生成其他月份全文队列，也不阻断已经可支持的有限博客命题。

## 6. 复核

复核者：root（非日报作者Planck；分批准入、证据/Books及最终日级独立复核）。

结论：通过

最终日级实际检查时间2026-10-04T18:02:00+08:00，见[DAY_REVIEW](../_sources/daily-20251114/DAY_REVIEW.md)。

已实际检查范围见[FIRST_INDEPENDENT_REVIEW](../_sources/daily-20251114/FIRST_INDEPENDENT_REVIEW.md)：4方向日期/准入、2负侧样本。SIMA2/cyber/sparse日期与准入通过；API准入通过但RSS08窗外，作者已修正。稀疏不因可选原稿未恢复整族阻断；cyber跨session细节从Nov13采用命题移除。未变化的初筛校准沿用，不重复读已过材料。

稀疏项root实际必要原源/owner PRE通过并窄写，Planck为非写入者实际POST通过；作者已实际读取共享Ch5唯一末注，17:02:54 POST通过及原源边界已落盘，该项整合结束。[TAIL_INDEPENDENT_REVIEW](../_sources/daily-20251114/TAIL_INDEPENDENT_REVIEW.md)实际覆盖19完整v1题摘/当前comments及2负侧，SIMA/cyber原核心与真实owner处置通过；有限日期停点与隔离接受。最终DAY_REVIEW实际通读六部分/SOURCE_TAIL及MiniMax Agent Tech原Markdown，确认两处来源修正；未变化FIRST/TAIL/PRE/POST复用，不重复19篇全文，也不称已证实19项贡献。全部3确定家族及必要Books实际结果通过，分层样本不扩大为全网保证，普通待办为0。

完成态V3、本日14份自写Markdown/96个本地引用/74份JSON、空白、围栏和限定diff-check实际重跑通过。原源raw Markdown逐字保留不混入自写空白/上游refs检查，未跟踪文件也直接检查。机器结果只证明格式/引用一致性，本日语义完成依据是上述非作者实际日级复核，不是机器通过。
