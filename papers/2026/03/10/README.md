# Daily Research — 2026-03-10

**规范：** V3
**窗口：** 2026-03-09T09:00:00+08:00 ～ 2026-03-10T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T01:16:02+08:00

## 1. 结论

本次没有能够同时满足具体贡献与确定落窗的候选。14 家每日来源已作有限历史/主题检查；arXiv 四组主题查询分别返回171、116、34、150条元数据，存在跨查询重复，不能相加为本日论文数，更不是逐项题摘或全文队列。主题发现中有界选取16个家族读完整题摘：14项潜在机制或评价增量因公告日期区间跨09:00右端而隔离，1项SoK在贡献前关闭，1项Caller Identity Confusion因当前撤回及方法/伦理问题不采用。另有4个官方发布核心作具体关闭或窗外重呈现去重；两篇窗外论文题摘仅用于确认重呈现身份，不纳入16项发现集或本窗分母。

确定落窗候选为0，候选证据审阅完成0/0，Books新增/已有覆盖均为0。本日未把日期隔离项记作 Evidence 完成、仅报告候选或 Books 已有覆盖，也没有为了恢复旧日报33项而补造评分。旧原文、原始记录及此前书稿未删除，旧报告另存[原样快照](../_sources/daily-20260310/V3_LEGACY_REPORT_SNAPSHOT.md)，其旧分母、9分、EffectiveDate豁免及完成标签不继承。

机构目录只有当前可恢复切片，arXiv实际批次、部分机构历史入口的外部限制见§5。这不是“当天无相关论文”或全互联网无遗漏结论。普通可执行待办0；root已完成本六部分与有限停点的最终非作者日Gate，报告到达安全终态。

## 2. 来源覆盖

执行时间为2026-10-02，范围固定为本日窗口；“可见无条目”只指下列实际目录切片，不推及删除项、全部机构研究或所有修订。API目录仅读取标题/日期元数据，正文只有决定贡献或身份的定点材料；未把宽目录变成全文队列。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)当前精选入口；恢复[官方RSS](https://openai.com/news/rss.xml)，实际解析1240项，只抽取3/8–3/11共7项元数据。3/9 Promptfoo 10:00GMT落窗，读官方核心22–39；3/10 instruction hierarchy 11:00GMT、math/science10:00GMT与3/11项目均窗外。[RSS原值](../_sources/daily-20260310/V3_OPENAI_RSS_FINITE_RAW.json)；切片处置：已检查（有限切片）；Promptfoo具体关闭 | 已检查 | RSS与精选不证明所有历史research无遗漏 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)可见当前10 publication；See more仍返回相同页。补[Alignment Blog](https://alignment.anthropic.com/)仅March组5条：coding-realism3/23、A3 3/11、Challenges3/5，均窗外；AuditBench3/10及month-only Abstractive核心与原始论文定点核，重呈现关闭；切片处置：已检查（March切片）；2项重呈现不计候选 | 受阻 | 主Research历史分页未恢复；不以March组代表所有机构研究 |
| SRC-GOOGLE-AI | [DeepMind Research](https://deepmind.google/research/)精选不是历史清单；[Blog真实page3](https://deepmind.google/blog/page/3/)24卡May→Feb，定点header核3/17 cognitive framework、3/10 AlphaGo回顾、3/3 Flash-Lite，跨本窗。AlphaGo核心123–169关闭。[Google March archive](https://research.google/blog/2026/03/)page1共12卡、3/11→3/6跨窗，page2为更早无需扩展；[Pubs](https://research.google/pubs/)当前第一页仅年份不证日级公开；切片处置：已检查（有限目录/Blog切片） | 受阻 | Pubs日级历史范围未证明；DeepMind错误?page=3曾返回当前page1，未作为历史证据 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)0行，IAB实际不可用；改查[Blog page1](https://ai.meta.com/blog/)10卡及[Next page2](https://ai.meta.com/blog/?page=2)12卡，非严格日期排序。3/10 CHMv2 forest-mapping是暂缓科学应用；3/11 MTIA及2/9 DINO应用为邻接。publication link请求400 timeout；日期域搜索只辅助恢复链接；切片处置：已检查Blog；Research论文入口受阻 | 受阻 | §5请求本窗模型/训练研究论文历史切片，搜索不证明无命中 |
| SRC-QWEN | [旧入口](https://qwenlm.github.io/)明示迁移qwen.ai且停2025；新Blog静态0行，实际public retrieval API type=qwen_ai/language=en-US返回40项。仅标题/extra.date/path，2/16 Qwen3.5→3/19 Max Preview跨本窗。[40项元数据原值](../_sources/daily-20260310/V3_QWEN_PUBLIC_LIST_RAW.json)；切片处置：已检查；本可见40项无本窗条目 | 已检查 | 无公布分页total；不外推机构全量或以extra.date证明论文first-public |
| SRC-DEEPSEEK | 恢复原始[官方/en/news](https://www.deepseek.com/en/news/)，独立读取Research10项（2/25 DualPath→6/24 V4）和News5项（12/1→4/24）。旧主页/动态失败不是Research缺失证据；切片处置：已检查；可见Research/News切片无本窗条目 | 已检查 | View all未另展开，不宣称完整历史 |
| SRC-MOONSHOT | 旧platform Blog仅至2025，恢复[现官方Kimi Blog](https://www.kimi.com/en/blog/)，实际全可见19条，2/9 Agent Swarm→4/20 K2.6跨本窗；切片处置：已检查；当前可见目录无本窗条目 | 已检查 | 19条可见范围，不推及删除历史 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)动态入口，复用已公开原始脚本指出的publicList接口后本日实际POST pageNum1/pageSize20/renderType0，total11且返回11/11；只抽元数据。显示日期2/13→4/23，pub字段也无本窗。共享[入口恢复依据](../_sources/V3_HUNYUAN_LIST_RECOVERY.md)；切片处置：已检查；11/11当前可见目录无本窗条目 | 已检查 | 先前动态读取失败保留过程；不再称目录不可访问，不推及删除项 |
| SRC-ZAI | [官方Research](https://www.zhipuai.cn/zh/research)独立读取15可见卡，2025/12/9→2026/8/26，邻接2/21 GLM5 technical→3/15 Turbo跨本窗；停View more；切片处置：已检查；本可见15卡无本窗条目 | 已检查 | 只本页范围，不继承其他日12卡旧计数 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)与论文目录入口；实际public get_article_list_v2，article_type1/publish_year2026/page_token20/count100/order_descfalse，x-tt-locale US。返回18项/total82，next40/has_moretrue，2/25→3/26切片；PublishDate原值转换BJT3/2→3/12跨窗。[实际原值与UTC/BJT](../_sources/daily-20260310/V3_SEED_PUBLIC_SLICE_RAW.json)；切片处置：已检查（有界历史页）；切片无本窗目录项 | 已检查 | 不遍历另64项；显示日期可回填/与论文不一致，不用它证明first-public |
| SRC-BAIDU-ERNIE | [Blog/zh page1](https://ernie.baidu.com/blog/zh/)实际10项，2025/11/21→2026/5/9，2/6 ERNIE5→4/15 ERNIE Image跨本窗；下一页更早，不扩正文；切片处置：已检查；可见目录无本窗条目 | 已检查 | 仅该页；不推及其他历史或修订 |
| SRC-XIAOMI-MIMO | [首页Paper](https://mimo.xiaomi.com/)实际8项，2/3 HySparse→3/13 ARL-Tangram跨窗；Blog15标题无日期，More无可读历史分页；[/blog/](https://mimo.xiaomi.com/blog/)实际为2025/12/16 V2-Flash单篇，不是archive；切片处置：已检查Paper；Blog历史受阻 | 受阻 | §5请求本窗Blog历史切片，不把单篇/无日期目录当无命中 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)12可见卡，3/18 M2.7→2/14 Forge→2/12 M2.5。英文Forge保留2/14，中文不是同一日期口径；[中文入口](https://www.minimaxi.com/blog)redirect后仅shell。[Agent Tech](https://agent.minimax.io/docs/techblog)仅heading；[llms.txt](https://agent.minimax.io/docs/llms.txt)48行恢复当前docs/techblog.md但该链接不可读；切片处置：已检查英文目录；Agent历史受阻 | 受阻 | §5请求3/9–3/10 Agent Tech历史正文/日期；48行用户文档不是历史技术发布证明 |
| SRC-ARXIV | 官方API UTC Submitted检索缓冲3/6 19:00→3/9 18:00，不等同first-public。Systems相关分类/LLM-training-speculation-kernel-inference，0页80+80页91/171；Learning CL/LG Transformer-MoE-LM × optimization/scaling/representation/attention 116/116；CV/RO/CL WorldModel-VLA-video-generation-multimodal-foundation34/34；AI/MA/IR/CL LM/LLM×agent/retrieval/evaluation150/150。四查询及页停点见[有限发现记录](../_sources/daily-20260310/V3_FINITE_DISCOVERY_STOP.md)。宽旧库存仅有界相关标题查漏，未继承旧33项；只16个身份读完整题摘，另2篇窗外AB用于重述去重；切片处置：已检查约定主题；本窗公告日期受阻 | 受阻 | 14个potential的复合区间均跨右端；官方实际批次恢复失败，§5逐项隔离，不用计划slot或DOI created强落窗 |

本次未触发每周源扫描、会议全站、实现repo/release队列或科学应用。arXiv历史查询为有界发现工具；延迟公告、早期作者稿与旧Submitted材料仍是范围限制，不声称全学科召回。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

无确定落窗候选（唯一家族分母0）。潜在贡献但日期未证的14项只在§5，不评分、不记标准/深入完成，也不借“暂缓候选”偷换为已确认当窗归属。官方明确关闭或当前撤回项只留筛选原始理由，不为它们建立候选行。

## 4. 证据与知识整合

本窗无可正面采用的候选证据，因此没有 Research→Books 新增、已有覆盖或结构改动。ROADMAP owner仅作未来重开路由：Covenant→TRAIN-DISTRIBUTED-TRAINING，EAGLE-Pangu→INFER-SPECULATIVE-DECODING，Ares→AGENT-PLANNING，SlowBA→PLATFORM-SECURITY；映射owner本身不是贡献或整合证明。日期修复后还须核对应实际命题所需方法/对照/边界与Books原论证，不能直接采用现在的题摘/准入校准。

弱侧已定点读到足以决定potential而非完成Evidence：Native Retrieval抽已生成query hidden states并训练两层head，不取消query生成；Table1 MRR .329→.293不支持“97%全面保留”，encoder计时不是全请求21.8×。RoboRouter历史multimodal retrieval与Evaluator消融不只是无证组合，但withdraw引用纠错依赖见§5。PIRA同PIRF有/无视觉noise对precision的受控差异，意图预测不构成行动授权。OfficeQA oracle parsed/PDF与同agent file/vector、table-header修复对照涉及解析/检索收益归因，不因是新benchmark误关。这些材料仅保存消歧证据与反例，不采用任何性能/安全保证。

[有界筛选记录](../_sources/daily-20260310/V3_FINITE_DISCOVERY_STOP.md)保留具名关闭及实际版本/位置：

- Promptfoo：原始RSS3/9 10:00GMT，官方核心22–39只收购与未来Frontier integration计划，未披露可采用的新安全机制或受控评价。
- AuditBench：本次Blog重呈现，不是说旧论文无长期价值；v1 §1/§4.2已含tool→agent gap、三种机制与release。Blog的Qwen32B与v1的14B不同，未见32B受控新边界；SAE case Blog KTO与v1 SFT不一致原样保留，未解释成新受控结果、不采用该差异结论。
- Abstractive red-teaming：month-only Blog核心12–43的category search、CRL/QCI、7×12评价已在2/12唯一v1题摘；没有独立新机制说明，不为本次重呈现另开日期请求。
- AlphaGo3/10回顾：核心123–169复述AlphaGo/Zero和已发模型、科学应用及AGI愿景，没有本次新受控机制。
- SoK 2603.07379v1：完整题摘加定点§IX安全归纳，风险数字引用旧研究，POMDP/taxonomy/研究议程未建立本次可改变具体机制选择的新证据；不泛化所有SoK无价值。
- Caller 2603.07473：最新v2官方撤回，理由为实验方法缺陷与数据伦理问题，仅保留排除依据。定点检索Books和旧本日报告的ID/title无采用链，不声称安全保证；不用撤回版本评分/入书。

## 5. 缺口与下一步

普通可执行待办0，root最终日Gate已通过。以下为本窗外部终态保留项，不支持正面证据、Books或无遗漏断言；以后只按具体条件重开受影响材料。现有日期不确定性不是“14项论文已审完”，来源缺口也不等于Coverage无遗漏通过。

日期依据：实际读取[官方availability](https://info.arxiv.org/help/availability.html)的no-advance ID/DOI与Eastern公告schedule、[官方DOI说明](https://info.arxiv.org/help/doi.html)，以及DataCite[created/registered定义](https://support.datacite.org/docs/what-is-the-difference-between-the-created-and-registered-date-in-the-datacite-rest-api)和[DOI states](https://support.datacite.org/docs/doi-states)。本日DST后Monday20:00EDT对应Tuesday08:00BJT。以下v1 Submitted均在3/6 Friday14:00Eastern之后至3/9 Monday14:00之前，最早可公告下界为3/10 08:00；arxiv.content拥有、findable DOI的registered原值给公告不晚于该秒的上界，转BJT加1秒表示半开区间。created/Updated不作为public时间。所有上界均晚于09:00，故只有跨窗范围而非确定本窗公告；不证明更早作者页面不存在。

首8原值见[DataCite原始字段](../_sources/daily-20260310/V3_DATACITE_FIRST_BATCH_RAW.json)，后6见[同样live字段](../_sources/daily-20260310/V3_DATACITE_TAIL_DATE_FIELDS.json)。旧 reconciliation的scheduled_match使用created+schedule猜公告，其自身说明月目录只证明收录，不证明具体首批；本次未采用。一次有界实际官方批次恢复（/list/cs/2026-03-10及cs.DC日期页、月目录目标页）cache miss，已有原始月页定点未给上述身份实际日批次。当前停止，不继续公告代码考古或凭推定slot强纳。

以下每个身份只提出一次日期请求：需要可核的官方实际首次公告批次/时间，或原始作者首次公开正文及时间，足以证明整个时间范围落在本窗；收到后只重开该身份的日期与对应采用命题，不重扫列表，不默认题摘即可入书。

| 材料与精确版本 | 原文具体potential，未证为当窗 | registered原值（UTC）→复合上界BJT（不含） |
| --- | --- | --- |
| [Covenant 2603.08163v1](https://arxiv.org/abs/2603.08163v1) | 动态非白名单peer实际训练的参与/结果接纳边界；不以72B或chain名准入 | 2026-03-10T04:24:49Z → 2026-03-10T12:24:50+08:00 |
| [EAGLE-Pangu 2603.08088v1](https://arxiv.org/abs/2603.08088v1) | branch/commit、safe indexing、fused/eager backend接口 | 2026-03-10T04:23:02Z → 2026-03-10T12:23:03+08:00 |
| [Ares 2603.07915v1](https://arxiv.org/abs/2603.07915v1) | 逐step最低成功effort标签/history router；标签选择与反事实仍需Evidence | 2026-03-10T04:18:55Z → 2026-03-10T12:18:56+08:00 |
| [SlowBA 2603.08316v1](https://arxiv.org/abs/2603.08316v1) | 维持动作正确率却制造资源退化的安全反证；日期恢复后必要定点深入 | 2026-03-10T04:28:23Z → 2026-03-10T12:28:24+08:00 |
| [Native Retrieval 2603.08429v1](https://arxiv.org/abs/2603.08429v1) | encoder成本与embedding质量取舍，保留非端到端计时/MRR反例 | 2026-03-10T04:31:04Z → 2026-03-10T12:31:05+08:00 |
| [RoboRouter 2603.07892v1](https://arxiv.org/abs/2603.07892v1) | 历史multimodal retrieval、Evaluator对routing的受控差异；另有引用纠错依赖 | 2026-03-10T04:18:23Z → 2026-03-10T12:18:24+08:00 |
| [PIRA 2603.08013v1](https://arxiv.org/abs/2603.08013v1) | 同PIRF clean/noise precision退化，主动意图评价盲区 | 2026-03-10T04:21:17Z → 2026-03-10T12:21:18+08:00 |
| [OfficeQA 2603.08655v1](https://arxiv.org/abs/2603.08655v1) | oracle parsed/table-header修复与file/vector对照的收益归因边界 | 2026-03-10T04:36:43Z → 2026-03-10T12:36:44+08:00 |
| [NEST 2603.06798v1](https://arxiv.org/abs/2603.06798v1) | network/memory feasibility联接DP搜索，而非仅吞吐数字 | 2026-03-10T03:52:34Z → 2026-03-10T11:52:35+08:00 |
| [Swimba 2603.06938v1](https://arxiv.org/abs/2603.06938v1) | expert参数空间混合维持单state recurrence，与多trajectory不同 | 2026-03-10T03:55:55Z → 2026-03-10T11:55:56+08:00 |
| [CAMEL 2603.08022v1](https://arxiv.org/abs/2603.08022v1) | capacity×mixture非线性与固定拟合预算跨scale分配 | 2026-03-10T04:21:29Z → 2026-03-10T12:21:30+08:00 |
| [LiveWorld 2603.07145v1](https://arxiv.org/abs/2603.07145v1) | out-of-sight实体持续推进，而非静态观察memory | 2026-03-10T04:00:44Z → 2026-03-10T12:00:45+08:00 |
| [KohakuRAG 2603.07612v1](https://arxiv.org/abs/2603.07612v1) | prompt ordering/retry/blank-voting消融的数值引用取舍待核，不仅排行 | 2026-03-10T04:11:48Z → 2026-03-10T12:11:49+08:00 |
| [Governance 2603.07191v1](https://arxiv.org/abs/2603.07191v1) | 两种cascade的IR/FPR和资源选择潜在受限对照；不采用四层名或robust保证 | 2026-03-10T04:01:49Z → 2026-03-10T12:01:50+08:00 |

RoboRouter不能只补日期便直接采用：[v2](https://arxiv.org/abs/2603.07892v2) Submitted 3/10T02:21:36Z撤回，comment指出错误引用须移除；[v4](https://arxiv.org/abs/2603.07892v4)6/24已恢复且header无当前撤回标记。v2不入选、不评分、不进入Books；不把后来有效v4误作全部家族撤回。本次v1的重开须日期证据与引用纠错受影响范围核，后窗v3/v4不是本窗revision触发。

有限来源外部请求（不重复无限恢复）：Meta的publication历史入口400 timeout，需要本窗模型/训练/推理论文清单及原始日期；Anthropic主Research历史分页未提供，Google Pubs仅年份，需要3/9–3/10主线论文原始发布切片，不能拿当前精选反证无命中；MiMo Blog首页15无日期标题/More未可读、/blog单篇旧稿，需要本窗Blog历史分页或带官方原始时间的文章；MiniMax Agent techblog链接不可读且当前llms目录非历史，需要本窗Tech Blog正文/日期或当时官方可核归档。替代材料均须是官方目录、作者原始发布/确切版本与日期，不接受搜索零命中作为覆盖证据。到达时只重开对应来源本窗切片与具体材料。

窗外材料只保留路由：AuditBench v3 Submitted3/9T18:35:46Z晚于Monday18:00Z deadline，最早公告3/11 08BJT，不以v3变更反填本窗；Abstractive唯一v1为2/12，不归本日；OpenAI instruction hierarchy/Responses电脑环境、A3与Meta MTIA属于后窗，未声明已完成其研究。Caller7/21撤回信号属于当次检查的必要不采用依据，不当作本窗新增研究贡献。以上均不扩张本窗或替代其目标日工作。

## 6. 复核

复核者：root（非报告作者）
结论：通过

root实际完整检查本六部分与新增有限发现文件、14源结果/停点/查询参数、0确定候选和14日期隔离的计数/请求，确认不采用withdraw版本、无Books写入待POST。复用已经完成且未变化的独立校准：root逐项读取首8官方完整题摘/历史，通过潜在贡献但明确未证明日期；Promptfoo core、AuditBench Blog及v1 §1/§4.2、Abstractive Blog核心及唯一v1题摘、AlphaGo回顾由root实际定点核；SoK完整题摘代表性负侧通过。RoboRouter v2引用撤回与v4当前header、Caller最新撤回comment由root实际核。新增6个potential的完整题摘仅作者已读，root未逐项重读；其余metadata没有root逐项题摘复核，本次不称全库存初筛或全文验收。

最终Gate通过；发现的来源结果非枚举、被引有限停点缺失、AuditBench ID及DeepMind页卡数均已实际修正并由root核验。机器校验已通过：`python3 scripts/validate_research.py --report papers/2026/03/10/README.md`；限定本日报告/日_sources的`git diff --check`无错误，root亦实际复验。结果不替代非作者语义验收；未stage、commit或push。
