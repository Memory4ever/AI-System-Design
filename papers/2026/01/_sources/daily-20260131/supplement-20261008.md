# Jan31 遗漏增量补查

作者：supplement_20260131；执行：2026-10-08T11:49:19+08:00；补充窗口：2026-01-30 ～ 2026-01-30。用户明确保留既有候选、原窗口、原公开时间、评分与有效审阅，只补遗漏。基线为 [原稿](baseline-before-supplement-20261008.md)，原61家族不重审、不搬移。原§4连续正文及61候选行保持；本次不读取旧Weekly反推、不扩其他日期/年份，不运行catchup、不stage/commit/push。

## 本次有限来源路径与停止

先读当前AGENTS/Research/Report/Sources每日组/Prompt/ROADMAP与本日停点。14源按注册顺序打开官方入口、定点Jan30模型/训练/推理/多模态/Agent主题；只有需要正文/日期才定点恢复。当前动态首页不能代替历史目录。原有限检查中身份、版本与命题未变的结果只作去重与有效复用，不授本轮全Coverage。

本次响应保留在 [官方1](supplement-official-first-20261008.txt)、[官方2](supplement-official-0-20261008.json)、[官方3](supplement-official-1-20261008.json)、[官方4](supplement-official-2-20261008.json) 与 [目录1](supplement-pages-0-20261008.json)、[目录2](supplement-pages-1-20261008.json)、[目录3](supplement-pages-2-20261008.json)、[目录4](supplement-pages-3-20261008.json)。内容是工具返回的实际切片，有的只含标题/总行数；不把未返回/未读段当完成。

| 来源 | 本次实际范围与停止点 | 判断与缺口 |
| --- | --- | --- |
| SRC-OPENAI | Research当前模型/视觉/音频卡片及research-index入口；Jan30 research/model/training定点搜索；Enterprise/Edu Jan30 custom-actions core与ChatGPT Jan30 visual-response说明；whales Jan30原文核心。 | 无新增研究机制；selector仅具体版本兼容边界关闭。当前Research卡片与日期搜索不恢复完整历史目录，保留对应缺段，不授零事件。 |
| SRC-ANTHROPIC | Research10近期publication标题止于Sep4；Jan30 model/agent/research查询。原Jan29coding-skills家族只定点核去重。 | 本次没有确定新增；10卡片非历史窗口覆盖，历史目录缺段终态保留。 |
| SRC-GOOGLE-AI | DeepMind当前Research卡片/六publication入口，Google pubs首15与Jan30 language-model/Transformer/Agent/训练推理日期检索到止。 | pubs含2027/2026年混排，不能从搜索无结果或current15授Jan30无研究；原有效约定主题结果保留，历史公开批次缺段隔离。 |
| SRC-META-AI | 首查research解析0行、Jan30 research主题查询；此前blog页1/2和433行mixed pubs身份未变只复用。 | 0行不是零命中；未恢复目标历史切片，来源受阻保留，不扩历年。 |
| SRC-QWEN | 旧页redirect、新qwen.ai/blog解析0行；Jan30模型主题定点查询。Qwen3ASR具体家族Jan29只去重。 | 不把动态0行记无事件；历史Blog缺段隔离。 |
| SRC-DEEPSEEK | 当前官网V4.1/研究链接、Jan30主题查询到止；mHC/Engram原窗外身份复用。 | 当前首页不是Jan30事件账；历史列表缺段保留，不以版本新旧推日期。 |
| SRC-MOONSHOT | Platform Blog可见2025年11→旧条目；Jan30官方kimi-cli定点检索；原v1.4 PR810证据复用。#792/#962/#808仅请求/提案，#970安装定位讨论；本轮不扫描普通issues队列。 | 原Kimi候选有效；这些普通配置/接入/界面提案未给新模型执行机制，不准入。Blog历史缺段继续隔离。 |
| SRC-TENCENT-HUNYUAN | 首查research timeout；本轮隐藏浏览器创建实际超时并reset，未取得目录。Jan30主题及KsanaDiT v0.2.2/pinning精确检索、target tag与!166直接尝试到止。 | 原DynamicVLA重复。v0.2.2日期标签满足新增自然日口径，但tag/revision及pinning新机制/直接反侧仍缺；!166不擅指认GitHub PR，单独材料请求。 |
| SRC-ZAI | research当前可见Jan19→Feb02相邻段（GLM4.7Flash/GLMOCR）；Jan30主题检索到止。 | 已检查该有界段，未见Jan30条目；不授完整动态目录无遗漏。 |
| SRC-BYTEDANCE-SEED | research实际10publication相关标题，其中Jan27Post-LayerNorm；public_papers p1/13的20卡片Aug18→May14及Jan30日期主题检索到止。 | 页1不覆盖Jan30；旧page2参数同页失败复用，不循环13页。精确目标页/漏项到达重开对应切片。 |
| SRC-BAIDU-ERNIE | 中文Blog可见Jan29PaddleOCRVL1.5→Feb06ERNIE5.0段与Jan30主题检索。 | 已检查该段无Jan30条目；Jan29家族只去重，不扩组织覆盖。 |
| SRC-XIAOMI-MIMO | Paper可见Feb03HySparse→Jan08MiMoV2Flash；Blog15无日期More卡片；Jan30主题检索到止。 | Paper相邻段已核，Blog无日期不能恢复目标事件，保留有限缺段。 |
| SRC-MINIMAX | 英文12卡片含Jan27M2-her→Feb12M2.5段；中文redirect minimax.cn仅目录标题；AgentTech15行空壳及Jan30主题检索。 | 英文相邻段已核，中文/Agent空壳不授零事件，缺段保留。 |
| SRC-ARXIV | 新主题API submittedDate Jan28～29、language-model/Transformer/attention/foundation/Agent/diffusion/VLA/WorldModel/GPU/kernel/MoE/inference，start0 max200，429无条目。旧2601月路径的404实际含Invalid Year，随后沿22208abs browse链接更正2026-01；CL/DC/CV/LG月头1–50及CL尾2151–2168仅发现、其他三尾cachemiss/429。exact22208/209仍只有Submitted与原DOI上界。 | 月列表按ID升序而非Jan30公告，窗外月头不审、尾线索不入候选；日期搜索所得Jan30Submitted不当public。新扫描未恢复完整Jan30公告，不授本轮完整Coverage；原language/foundation153、Agent55、multimodal80、system5的有效约定主题结果复用不重开队列。 |

arXiv尝试原件：[新API](supplement-arxiv-query-20261008.json)、[列表初试](supplement-arxiv-web-20261008.json)、[旧路径原404](supplement-last-0-20261008.txt)、[精确保留项](supplement-last-1-20261008.txt)、[更正路径](supplement-correct-list-20261008.txt)。更正月路径已实际恢复，所以不能再把InvalidYear404笼统写成全部arXiv不可访问；仍不能从月集合推出逐日公告时间。

## 首包拟准入及代表关闭（root独立校准通过）

本轮确定新增家族0；原61保持。没有对旧排除或Batch9–11缓存展开全文队列。root实际打开Enterprise Jan30段与Ksana changelog，独立通过selector低durability、visual UI、鲸鱼应用、Kimi提案关闭校准；本作者不自授独立Source或DAY。

- [More models for GPTs with custom actions](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes)：January30段说明新增GPT5.2Instant/Thinking、o-series/Pro仍不支持、workspace admin availability控制。旧兼容集合受限→具体版本名单扩展→使用者可换支持模型；未新增工具执行机制、授权条件、安全/质量评价证据。贡献前关闭具体版本事实，不拿版本名或“工具”关键词准入。补充自然日不要求旧09→09精确时刻；删除旧selector日期请求，原已读有效证据仍保留。
- [More visual responses](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)：Jan30at-a-glance、highlight侧栏与iOS/Android/Web发布是UI呈现；没有新训练/推理执行/Agent权限机制，关闭，不以“visual”关联Ch23准入。
- [Decoding the alien language of whales](https://academy.openai.com/en/public/blogs/decoding-the-alien-language-of-whales-chatgpt-2026-01-30)：Jan30研究介绍实际目标是鲸鱼沟通解释/动物保护；依ROADMAP暂缓科学应用，非模型机制新增，关闭。
- [Kimi #792](https://github.com/MoonshotAI/kimi-cli/issues/792)、[#962](https://github.com/MoonshotAI/kimi-cli/discussions/962)：可配置bash与NVIDIA兼容API接入提案仅产品接入请求/作者“实现ready”声明，无新执行可靠性机制或可比评价；没有读取他人源码/运行实现，不授已实现结果，贡献前关闭。#808仅WebUI提案，#970安装/路径异常实例也未成为新机制。
- [KsanaDiT v0.2.2](https://github.com/Tencent/KsanaDiT/blob/main/CHANGELOG.md)：Jan30日期已恢复；Added/Sage-SLA、QwenAttentionOp、PinnedMemoryManager/OOM标签尚无新机制实际行为，非确定候选、不评分。target tag、!166和pin manager精确查询有限失败，只恢复changelog，其他组织/窗外搜索结果不采用。终态保留请求：该release精确revision及!166或同变化source/core，说明旧offload/pinning约束→实际变化→何种OOM/传输条件和直接反侧才重开。无需再索要精确公开时刻。
- [22208](https://arxiv.org/abs/2601.22208v1)/[22209](https://arxiv.org/abs/2601.22209v1)：本次精确abs题摘无撤回/勘误信号，仍仅Submitted Jan29；当前月collection不提供公告日期，原Jan30下界～Feb02上界仍跨窗。不用API published/DOIcreated/JanID伪造firstpublic。本轮不重复评分/深审，恢复只需逐稿官方公告或作者首次正文日期足以缩到Jan30。

## 新搜索线索：完整题摘与有限日期停止

只有下列八项定点查漏，不扩大到提交批次或未来日报。exact版本题摘/日期原件为[四项首包](supplement-new-hits-0-20261008.txt)、[四项补包](supplement-new-hits-1-20261008.txt)、[22443版本与官方availability](supplement-new-hits-dates-20261008.txt)、[最后精确标题日期检索](supplement-new-hits-date-search-20261008.txt)。后者未恢复可证明Jan30首次完整正文的primary source，不把第三方索引Date当事实。

| 精确身份 | 已读题摘的具体贡献筛选，不作性能采用 | 日期权限与终态 |
| --- | --- | --- |
| [Prompt Optimization Via Diffusion Language Models, 2602.18449v1](https://arxiv.org/abs/2602.18449v1) | 手工/逐token改prompt受局部轨迹约束→masked denoising span以query/response/交互反馈为条件→冻结目标LLM也能并行改prompt；潜在AGENT-PROMPT增量，不因“优化”关联自动入选。 | exact v1 Submitted Jan30 00:00:54Z但browse为2026-02；官方availability的公告月份与周末schedule排除该arXiv事件Jan30公开。更早作者完整正文未恢复；窗外线索，不当Jan30候选、不扩后日。 |
| [Weak Diffusion Priors Can Still Achieve Strong Inverse-Problem Performance, 2601.22443v1](https://arxiv.org/abs/2601.22443v1) | 强视觉prior通常被当反问题必要条件→measurement-rich下弱/错域prior仍可由测量约束恢复、measurement-poor则失败→改变prior容量与采样/测量条件的选择，潜在Ch24边界，不笼统关成应用。 | exact v1 cachemiss；unversioned只提供v1 Submitted Jan30 01:25:54Z与当前v2，不能冒用June2 v2局部相关性分析。精确标题日期检索未恢复primary first-public；终态请求v1完整题摘/正文及足以确认Jan30首次公开的官方或作者日期，不评分。 |
| [Decoupled Diffusion Sampling for Inverse Problems on Function Spaces, 2601.23280v1](https://arxiv.org/abs/2601.23280v1) | 已读v1题摘核心是PDE反演系数prior与forward neural operator/物理约束解耦、谱误差/数据效率；属于暂缓AI for Science主线。 | 范围关闭，root独立校准通过；不为范围外项追first-public。 |
| [Position: Agentic Evolution is the Path to Evolving LLMs, 2602.00359v1](https://arxiv.org/abs/2602.00359v1) | 预训练/post-training难覆盖长期部署变化→persistent state与goal-directed adaptation组成deployment evolution框架→提出evolution compute分配；潜在Agent主线，不把position框架称已验证机制或已有覆盖。 | exact v1 Submitted Jan30 22:15:58Z、browse为2026-02；官方availability排除该arXiv事件Jan30公开。更早作者首次完整正文未恢复；窗外线索，不当本日候选、不展开全文。 |
| [Matterhorn, 2601.22876v1](https://arxiv.org/abs/2601.22876v1) | 累积脉冲计数/数据移动能耗约束→TTFS masked silent membrane/dead-zone与memristor CIM分工→潜在改变推理硬件计算/传输取舍；并非单纯数字增益。 | exact v1 Submitted Jan30 11:53:42Z不是公开日；题摘与版本已定点恢复，首次公开日期未恢复。终态请求本稿Jan30官方公告/作者首次完整正文日期。 |
| [Stabilizing Transformer Training Through Consensus, 2601.22614v1](https://arxiv.org/abs/2601.22614v1) | 高learning-rate下attention训练不稳定→graphical-model consensus替换attention、可hybrid→潜在改变稳定性与attention结构选择，未采用题摘性能宣称。 | exact v1 Submitted Jan30 06:12:07Z不是公开日；本稿first-public未恢复。终态请求Jan30官方公告/作者首次完整正文日期。 |
| [YuriiFormer, 2601.23236v1](https://arxiv.org/abs/2601.23236v1) | 标准层更新与优化动力学分离→attention gradient/MLP potential的Lie-Trotter分裂及同oracle Nesterov→潜在MODEL-TRANSFORMER-LAYER机制增量，非名称映射。 | exact v1 Submitted Jan30 18:06:21Z不是公开日；不拿Mar4 v2替代。终态请求本稿Jan30官方公告/作者首次完整正文日期。 |
| [SpanNorm, 2601.22580v1](https://arxiv.org/abs/2601.22580v1) | 层间residual方差/representation collapse压力→whole-block residual span与聚合PostNorm→潜在改变dense/MoE深度稳定性选择，非仅normalization关联。 | exact v1 Submitted Jan30 05:21:57Z不是公开日；不拿June4 v2替代。终态请求本稿Jan30官方公告/作者首次完整正文日期。 |

2601/2602 ID只有月份信息，不替代首次公开日期；上述Submitted与日历schedule不授Jan30精确公开。root已独立认可四项首包范围/日期权限，以及其余四项仅必要公开日请求。五项日期隔离不授候选/Evidence/Books，也不是可读全文未读伪装受阻。API429、canonical月列表/月头尾与具体abs/标题日期检索均有限停止；只收到对应primary材料重开该项。

## 终态边界与交接

新候选0，所以本次Books No Change，无共享Books/State/索引写入；root独立六部分日级DAY通过。root实际核14有限source_stop、八项题摘/日期权限、selector/Kimi/UI/Science代表关闭与具名终态请求；原61行/窗口/§4连续保留、89本地引用0 broken、V3及本日cached/unstaged diff通过，不无差别重读旧61/四处写后。作者记录实际独立结果，不自授DAY。所有可执行有限扫描已停止，普通待办0，本日结束；上述来源缺段、精确Ksana实现、原22208/209与新增五项日期保留不支持候选、Books、正面Evidence或无遗漏。现存四中心争议继续原有效隔离，不重开未变化证据。收到具体材料只重开本项；不会自动扩月/换日。
