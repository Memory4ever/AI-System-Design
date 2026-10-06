# Daily Research — 2026-03-15

**规范：** V3
**窗口：** 2026-03-14T09:00:00+08:00 ～ 2026-03-15T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T02:04:08+08:00

## 1. 结论

本次有限检查尚无可同时满足具体贡献与确定落窗的候选。14家每日来源实际入口均已处理到有限停点；当前机构目录不是全历史。arXiv四主题查询及一次合并恢复均超时/限流，没有可用metadata，不能记作0命中。官方无Friday/Saturday常规公告只是日历约束，不能证明作者稿首公开或全部研究为零。

完整题摘实际读取2项：νTNS范围关闭，窗外Abstractive旧稿只作重呈现身份确认；另GLM-5-Turbo官方核心定点贡献关闭。三项理由均已由root实际独立校准，不计候选、不评分、不当标准/深入Evidence完成。确定候选0，候选证据审阅完成0/0，Books整合/已有覆盖0。本日没有可正面采用的新增机制，也未改Books、LS或索引。旧[V2.1报告快照](../_sources/daily-20260315/V3_LEGACY_REPORT_SNAPSHOT.md)仅存过程历史，其零分母、EffectiveDate豁免、宽库存及完成标签不继承。

有限来源外部限制见§5；不声称“当天无相关论文”或无遗漏。root最终六部分/实际停点日Gate通过，发现的Seed Blog范围遗漏已定点补查并精确隔离；普通可执行待办0。

## 2. 来源覆盖

执行日期2026-10-02，固定本日窗口。目录只读标题/日期，正文仅涉及决定贡献/身份的定点材料，没有宽列表全题摘或附件队列。实际入口、页停点和原值见[有限来源停点](../_sources/daily-20260315/V3_SOURCE_STOP.md)、[public字段](../_sources/daily-20260315/V3_PUBLIC_DIRECTORY_FIELDS.json)、[Seed论文字段](../_sources/daily-20260315/V3_SEED_FINITE_FIELDS.json)、[本日Seed Blog字段](../_sources/daily-20260315/V3_SEED_BLOG_FINITE_FIELDS.json)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)当前精选；[官方RSS](https://openai.com/news/rss.xml)实际解析1241项，只取3/13–3/16 pubDate切片1项SAST Blog，原值Mon,16Mar2026 00:00:00GMT→3/16 08BJT，窗外；未扩正文 | 已检查 | RSS与精选不证明全部历史Research无遗漏 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)当前10 publication，See more仍同页；[Alignment](https://alignment.anthropic.com/)March组5条，定点header coding-realism3/23、A3 3/11、AuditBench3/10、Challenges3/5窗外；month-only Abstractive核心与旧v1题摘确认重呈现关闭 | 受阻 | 主Research本窗模型/Agent论文历史分页未恢复；March Blog切片不代表机构全部研究 |
| SRC-GOOGLE-AI | [DeepMind Research](https://deepmind.google/research/)8项精选；[实际Blog page3](https://deepmind.google/blog/page/3/)24卡May→Feb，header3/17 cognitive-framework与3/10 AlphaGo跨窗；[Google March archive](https://research.google/blog/2026/03/)page1的12卡，3/16→3/12跨窗，page2更早未扩；[Pubs](https://research.google/pubs/)当前仅年份 | 受阻 | Pubs及精选Research日级论文历史未取得；未全扫372项2026论文 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)0行；实际从Blog导航请求[publication](https://ai.meta.com/results/?content_types%5B0%5D=publication)超时；[Blog](https://ai.meta.com/blog/)10卡与[page2](https://ai.meta.com/blog/?page=2)12卡，非严格日期排序，3/11与3/27及更早条目无可见本窗卡 | 受阻 | 本窗模型/架构/训练论文历史入口未取得；本日没有IAB核查，不沿用他日browser失败 |
| SRC-QWEN | [旧入口](https://qwenlm.github.io/)明示迁移，qwen.ai/blog静态0行；实际public retrieval type=qwen_ai/language=en-US，safe title/path/date投影40项，2/16 Qwen3.5→3/19 Max Preview跨窗；初次输出截断3片段不作目录数 | 已检查 | 未公布分页total；仅40可见范围，date不等于论文first-public |
| SRC-DEEPSEEK | [官方/en/news](https://www.deepseek.com/en/news/)实际Research10、News5，2/25→6/24及12/1→4/24跨窗；停可见目录，不扩View all | 已检查 | 不宣称删除项或完整机构历史 |
| SRC-MOONSHOT | [现官方Kimi Blog](https://www.kimi.com/en/blog/)实际19可见条目，2/9 Agent Swarm→4/20 K2.6跨窗；不以旧platform止2025反证2026缺研究 | 已检查 | 仅可见19条，不推及删除历史 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)静态timeout后，本日实际publicList POST pageNum1/pageSize20/renderType0，total11、11/11返回，display2/13→4/23跨窗，pub字段无本窗；[官方endpoint恢复依据](../_sources/V3_HUNYUAN_LIST_RECOVERY.md)只作入口定位 | 已检查 | 动态静态失败不再解释为整个目录不可访问；不推及删除项 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)实际15卡，2025/12/9→2026/8/26，停查看更；定点[Turbo155](https://www.zhipuai.cn/zh/research/155)header2026/03/15 16:00及core16–90，公开增量关闭 | 已检查 | header未明确时区，已贡献前关闭，不为不影响处置的日期穷查；不全审15卡 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)与[论文目录](https://seed.bytedance.com/en/public_papers)当前页非March历史；实际get_article_list_v2 article_type1/year2026/page_token20/count100/order_descfalse，US locale，18项/total82、next40/has_moretrue，2/25→3/26；3/15 νTNS题摘关闭。另本日定点type2/year2026/page_token0/count100/order_descfalse，返回14项/total19、next空/has_morefalse；显示2/16 Arena Preview→4/1 Recruitment跨窗，无可见本窗Blog项，只读title/date | 受阻 | PublishDate不证明first-public；type2的14返回与total19不一致，缺其余5项/本窗Blog历史切片，§5精确隔离，不声称19/19或全Blog无命中 |
| SRC-BAIDU-ERNIE | [Blog/zh](https://ernie.baidu.com/blog/zh/)page1实际10卡，2025/11/21→2026/5/9，2/6→4/15跨窗；下一页更早未扩 | 已检查 | 仅当前页范围，不推及其他历史/修订 |
| SRC-XIAOMI-MIMO | [首页Paper](https://mimo.xiaomi.com/)实际8项，3/13 ARL-Tangram→6/29 MOPD跨窗；Blog15标题无日期，More无可用历史分页；[/blog/](https://mimo.xiaomi.com/blog/)实际2025/12/16单篇而非archive | 受阻 | 本窗Blog历史日期/正文切片未取得，不能由无日期标题授no-hit |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)12卡、[中文](https://www.minimaxi.com/blog)redirect后13卡，3/18→Feb跨窗；Forge英文2/14、中文2/12原值不同均窗外。[Agent Tech](https://agent.minimax.io/docs/techblog)仅heading，llms.txt48行提供当前techblog.md但链接不可读 | 受阻 | Agent Tech本窗历史正文/日期未取得；当前用户文档不是历史发布证明 |
| SRC-ARXIV | [API](https://export.arxiv.org/api/query)四主题：systems CL/LG/DC/AR/PL/OS/PF×LLM训练/推理/通信kernel；learning CL/LG×Transformer/MoE/LM×优化/scale/representation/attention；CV/RO/CL×WorldModel/VLA/video/multimodal；AI/MA/IR/CL×LM/LLM×agent/retrieval/eval。均Submitted UTC3/13 01→3/15 01、start0/max200/ascending；timeout/429，一次合并也429。[完整查询/error](../_sources/daily-20260315/V3_ARXIV_QUERY_STOP.json) | 受阻 | 无可用主题历史metadata/具体dated event，不能记0命中或主题覆盖无遗漏；未证有效的YYYY-MM-DD列表请求只无可用资料，不称官方日档受阻 |

未触发每周源、会议全站、实现repo/release或科学应用队列。Hunyuan/Qwen/Seed恢复public endpoint是原始公开入口恢复，不是以搜索摘要代替证据。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

无确定落窗候选，唯一家族分母0。失败主题响应不是0篇；三项已明确关闭只保留筛选理由，不造4分候选，也不把访问状态计入评分。

## 4. 证据与知识整合

没有可正面采用的候选Evidence或Research→Books产出。以下为具体准入前关闭及身份依据，不是候选深审完成：

- [GLM-5-Turbo](https://www.zhipuai.cn/zh/research/155)：header原值2026/03/15 16:00，无显式时区；实际核心16–90只公开OpenClaw训练能力目标、工具/指令/长任务/吞吐目标，未披露可改变训练选择的objective/data控制。ZClawBench场景分布/排行没有建立可审独立protocol或评价盲点；Claw Enterprise的RBAC/audit/encryption/human approval仅产品特征与承诺，没有披露可采用的新约束、控制机制或反证。不采用安全保证，不因“没有新权限schema”一条机械拒绝，也不泛化所有新模型无贡献。
- [Abstractive red-teaming](https://alignment.anthropic.com/2026/abstractive-red-teaming/)：month-only Blog core12–43与[唯一v1](https://arxiv.org/abs/2602.12318v1)完整题摘/Feb12历史相同工作，category search、CRL/QCI、7模型×12原则评价已在旧稿。未见独立revision/新机制说明，关闭本次重呈现；不是旧论文无价值或旧Evidence全审宣称，不追不影响此处置的月级日期。
- [νTNS 2603.14425v1](https://arxiv.org/abs/2603.14425v1)：完整题摘为neural disentangler/CNN+tensor-network求量子manybody/J1-J2 Heisenberg能量。当前暂缓AIforScience，没有foundation模型系统增量，不借表示owner回收。Seed id1414原PublishDate1773504000000→3/15 00BJT与v1 Submitted3/15T15:09:00Z不一致，显示日期不证明first-public；范围明确关闭，不开日期请求/附件队列。

当前官方页轻量检查未见上述Blog新的撤回/纠错说明，νTNS唯一v1未见撤回header；没有为了证明“无标记”遍历完整历史。三项由root实际读对应core/题摘/历史，首批独立校准通过。完整有限记录见[停点](../_sources/daily-20260315/V3_SOURCE_STOP.md)。

## 5. 缺口与下一步

普通可执行待办0，root最终日Gate通过。以下为本窗外部终态保留项，不支持正面证据、Books或无遗漏断言；以后只按具体条件重开受影响材料。

| 身份/入口 | 必要缺口、当前限制与定点重开条件 |
| --- | --- |
| [Anthropic Research](https://www.anthropic.com/research) | 当前10项/See more同页不足历史：请求本窗模型/Agent/可靠性系统论文官方历史切片或作者原始发布与可核日期。到达后只重开该来源该窗，不以March Blog切片代全机构。 |
| [Google Pubs](https://research.google/pubs/)、[DeepMind Research](https://deepmind.google/research/) | 当前仅year/精选不能证明日级公开：请求3/14 09→3/15 09主线论文官方原始event/date或历史清单。Blog可见跨窗邻接仅支持自身切片；只重开受影响材料，不全扫年度论文。 |
| [Meta publication](https://ai.meta.com/results/?content_types%5B0%5D=publication) | 页面timeout/Research0行，缺本窗模型/架构/训练论文清单与原始日期。官方带date历史目录或确切作者版本可替代；到达只恢复该窗论文部分，Blog当前卡不作无命中证明。 |
| [MiMo Blog](https://mimo.xiaomi.com/) | 15标题无date、More无可用历史页，/blog为旧单篇。请求本窗Blog官方历史分页或原始文章日期/正文；只重开该窗具体发布，不把全部15标题变审阅队列。 |
| [MiniMax Agent Tech](https://agent.minimax.io/docs/techblog) | 只有heading、恢复techblog.md不可读、llms当前用户docs非历史。请求本窗原始技术Blog及date/官方可核归档，按具体事件恢复；英文/中文目录跨窗不授Agent历史无遗漏。 |
| [Seed Research / Blog](https://seed.bytedance.com/en/research) | 本日type2有限元数据实际返回14、total19且无next；返回日期跨窗，但剩余5项不知，当前5Blog精选也不是历史切片。请求足以解释这5项的官方Blog目录/历史日期，或本窗带可核date的原始Blog；只恢复该来源该窗，不将所有Blog或论文变全文队列。 |
| [arXiv主题API](https://export.arxiv.org/api/query) | 四主题及一次合并有限失败，缺可用本窗主题历史slice/确切dated原event。需要有效官方recent/月列表的本窗相关标题切片、实际公告事件或可核作者原发日期，不能拿Submitted缓冲/错误day路径/搜索0代替。得到材料后仅日期与具体贡献重开，不继续全March扫描或公告代码考古。 |

日期背景只作限定：[官方availability](https://info.arxiv.org/help/availability.html)实际170–189说明Sunday–Thursday Eastern20:00公告、Friday/Saturday无常规公告，DST后邻接slot为BJT3/13 08与3/16 08，窗外；moderation可延迟。此事实不是所有作者原发/更新事件为0。两次/list/cs/YYYY-MM-DD cachemiss未证是有效官方按日入口，仅请求无可用资料。DataCite client-id arxiv.content、registered UTC3/14 01→3/15 01实返回total0，只辅助索引，不当exact公告或无遗漏证明。

窗外/日期粗糙但已具体关闭的Turbo、Abstractive、νTNS不用另建材料请求。RSS SAST 3/16、A3 3/11、AuditBench3/10、AlphaGo3/10、MiMo3/13等仅目录邻接，不宣称其研究已完成，也不扩张本窗或处理归属日。

## 6. 复核

复核者：root（非报告作者）
结论：通过

root实际完整读取此前81行六部分、完整V3_SOURCE_STOP及3JSON的实际窗口/query/原字段；首批准入校准复用已实际读的GLM-5-Turbo /155 core16–90/header、νTNS v1完整题摘/历史、Abstractive core及唯一Feb12v1题摘，三条具体关闭成立。四主题+一次合并query packet已核；未证有效的day路径不可称官方历史列表受阻已修。最终Gate发现Seed Blog范围遗漏，按root指定的一次本日type2有限恢复补入，返回14/total19无next的不一致已隔离，不补造全量覆盖；root授权完成该定点补正后通过。其余metadata没有root逐项题摘/全文复核，新增type2字段只为目录/date恢复，不称独立全文Evidence。

无Books实际写入待POST。机器校验已通过：`python3 scripts/validate_research.py --report papers/2026/03/15/README.md`；限定本日报告/日_sources的`git diff --check`无输出，4个JSON可解析、8个本地报告链接有效，实际diff已检查。这些结果不代替非作者语义Gate；未stage、commit或push。
