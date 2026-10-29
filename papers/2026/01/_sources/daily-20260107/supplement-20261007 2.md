# 2026-01-07 Daily 增量来源补查 — 2026-10-07

## 范围、授权与停点

作者：supp_jan07。检查时间：2026-10-07T14:02:11+08:00。用户授权对已存在 Daily 补查遗漏；本轮补充窗口为北京时间 **2026-01-06 完整自然日**（UTC 2026-01-05 16:00 至 2026-01-06 16:00，不含右端）。保留原 09:00→次日 09:00 窗口、51 家族及其日期、评分、有效审阅、Books 结果和四项争议，不搬动 Health 的原归属。不从旧 Weekly 建池，不检查 Weekly-only 来源。

本轮重新加载 AGENTS、研究/来源/报告合同、Prompt、ROADMAP 及最新路由 checkpoint；旧 _sources 只作精确身份去重/有效证据索引，不继承旧目录计数。本轮目录字段来自各入口的新读取。宽列表、metadata、完整题摘、准入、正文证据和 Books 判断分别记账。正文审阅及 Books 写入未启动：下列七项先通过具体贡献理由校准，但公开日尚未落实；root 为本轮非作者终态复核者。状态：进行中。

## 14 个每日来源的实际有限检查

目录只按窗口附近日期定位；下列条目数不是全文或摘要阅读数，也不证明机构完整历史。动态目录的首次异常不当零返回；有实际恢复的记录以恢复结果为准。

| 来源 | 实际入口、范围与返回 | 窗口判断、限制与停止 |
| --- | --- | --- |
| SRC-OPENAI | [官方 RSS](https://openai.com/news/rss.xml) 经浏览入口 XML 不支持后以官方 HTTP 返回解析 1251 条日期 metadata；Jan2 10:00Z Grove→Jan7 00:00Z Health→Jan7 10:00Z Tolan。限定官方域 January6 research 补查得到 Academy 的长寿细胞、医疗 intake、高中课堂应用文章 | RSS 没有新 Jan06 BJT 条目；应用文章没有已定位的新基础模型/系统机制，不按名称或全年文章扩大队列。Health 属 Jan07 BJT，旧归属不动。有限 feed 非全机构事件保证 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 当前正文首屏有限；实际 HTML 嵌入提取 174 个 publishedOn/slug 定位字段，Bloom Dec19 19:45Z→critical-infrastructure-defense Jan8 00:00Z | 可见研究目录未定位 Jan06 条目；174 是日期字段数而非摘要数。不请求全机构无隐藏/删除证明 |
| SRC-GOOGLE-AI | [DeepMind publications](https://deepmind.google/research/publications/) 首30/总265/page1 of9，Jan9→Dec3邻接；[Google Research January blog](https://research.google/blog/2026/01/) 九个日期标签最早Jan12；[pubs](https://research.google/pubs/) 年过滤显示2026共392、当前首15 | 日级 Blog/DeepMind 可见区段无新 Jan06 条目；年度 publication 字段不判公开日，不展开全年队列 |
| SRC-META-AI | [Research](https://ai.meta.com/research/) 仅可取 Muse 页标题；HTTP 正文25秒超时；[publications](https://ai.meta.com/research/publications/) 及 page3 浏览失败。官方域 publications + January6,2026 搜索为空 | 入口检索受限，不推零；未发现需核实的具名 Jan06 事件，不要求整个 Meta 历史目录或全站镜像 |
| SRC-QWEN | [research-list 原接口](https://qwen.ai/api/page_config?code=research.research-list) 浏览失败后 HTTP 成功，60 个 date 字段。最新Dec23 05:08Z ImageEdit，之前Dec22 voiceclone、Dec19 layered、Dec8 OmniFlash、Dec4 SAPO/TTS | 当前有限目录没有新 Jan06 条目；本轮恢复替代旧入口受阻事实，不继承旧数值，不读60全文 |
| SRC-DEEPSEEK | [主页](https://www.deepseek.com/en/) 实际 More 导航至[官方 News](https://www.deepseek.com/en/news/)，有限10个 research 日期，Jan12 Engram→Dec31 mHC；普通 News Dec1 V3.2→Apr24 V4 | 可见研究段无 Jan06 事件；api-docs/news 不可取及 updates 超时不当零，未扩大 View All 全历史 |
| SRC-MOONSHOT | [Platform blog](https://platform.kimi.com/blog) 当前26可见标题，最新Nov7、Nov6 K2Thinking；[Kimi-K2 releases](https://github.com/MoonshotAI/Kimi-K2/releases) 实际显示没有 releases | 两个实际有限入口未定位 Jan06 事件；不把一个仓库无 release 当全机构无研究，不审无变化的 PR |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research) 首屏仅标题；原接口 `https://api.hunyuan.tencent.com/api/blog/publicList` POST pageNum1/pageSize100/renderType0，code0/totalNum9/list9；读取 publishedAt、displayPublishTime、updatedAt 区分字段；最早 publishedAt1770090898 为 Feb03 BJT | 当前目录无 Jan06 条目；恢复后的有限目录不是全历史保证，不因旧目录缺失自动建立新的普通待办 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) 15个可见条目，Jan13 Huawei/GLMImage→Dec10 TTS/Dec9 ASR；[release](https://docs.z.ai/release-notes/new-released) Jan14 GLMImage→Dec22 GLM4.7 | 有界日期邻接未定位 Jan06 事件；More 未扩全站，不授完整事件召回 |
| SRC-BYTEDANCE-SEED | [论文入口](https://seed.bytedance.com/en/public_papers) 首20/总242/page1 of13；原 `get_article_list_v2` 对 type1/2×2026ASC/2025DESC，各 count20/page_token0。实际可见数 **20/0/9/15**、total **82/94/23/49**，均next20/has_more true；type1-2025 响应两次均只有分页/total，没有 list。type1-2026 最早Jan19 16:00Z（BJTJan20），type2-2026最早Feb11 16:00Z；type2-2025最新pinned Dec23 16:00Z、非pinned Oct22 16:00Z | 当前实际日期切片没有定位新 Jan06 事件；0 是该接口缺 list，不是零论文。请求20不等实际返回，9不等total23；不继承旧locale数、不授全年无遗漏，不为2025异常展开全库存 |
| SRC-BAIDU-ERNIE | [中文 Blog](https://ernie.baidu.com/blog/zh/) 当前page1、下一页2/2入口，窗口两侧Jan8 VisionArena→Dec23 TextArena | 当前有限日期段无 Jan06 条目，不扫 Weekly 入口 |
| SRC-XIAOMI-MIMO | [主页](https://mimo.xiaomi.com/) Paper8日期，Jan8 MiMoV2Flash报告→Oct21 router；Blog15当前可见。原[route/frontmatter JS](https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js) 实际恢复688092字节，HSS Dec19、safety Dec18及2026较晚路线；从 `/blog/mimo-v2-flash` 显式 iframe 进入[官方正文](https://mimo.xiaomi.com/mimo-v2-flash/index.html)，正文日期 December16,2025 | 所读有日期材料无新 Jan06 事件；Dec16发布正文不重标为Jan8报告事件；未注明日期/隐藏路径不自动化成全站历史阻塞 |
| SRC-MINIMAX | [EN blog](https://www.minimax.io/blog) 12可见日期，Jan27→Dec23；[CN blog](https://www.minimax.cn/blog) 13可见日期，Jan28→Dec23；[Agent Tech](https://agent.minimax.io/docs/techblog) 当前有限入口未恢复本窗历史日列表 | EN/CN窗口两侧无 Jan06 新条目；Agent有限入口不推全机构零事件 |
| SRC-ARXIV | 本轮实际 [cs.CL](https://arxiv.org/list/cs.CL/2026-01?skip=25&show=100) 100标题（00557→02670）、[cs.DC](https://arxiv.org/list/cs.DC/2026-01?skip=0&show=25) 25、[cs.CV](https://arxiv.org/list/cs.CV/2026-01?skip=75&show=25) 25、[cs.RO](https://arxiv.org/list/cs.RO/2026-01?skip=0&show=25) 25；cs.LG首100仅身份线索。由主题相关标题定点读下文16个完整题摘，而非顺序读宽列表。旧 `2601` 年月路径404及CV首次提取规则失败后实际恢复25，均不当零 | 主题限基础模型、训练/推理、agent/memory、生成/VLA及并行系统；月份标题不证 Jan06 公告日。七项拟准入和两项延迟编号线索逐ID日期补检；不把 submitted/updated 当公开日，不拉全年全学科队列 |

Seed 四请求共用实际原入口 `https://seed.bytedance.com/api/get_article_list_v2`，参数 `article_type=1/2&publish_year=2026/2025&count=20&page_token=0&order_desc=false/true`（2026 false、2025 true）。目录字段只用本轮 actual PublishDate/IsPinned/pagination，不能复用别日报告的 locale 计数。

## 完整题摘后的贡献筛选：7 项拟准入，尚非 Jan06 新候选

下面都实际读完整题目与摘要；分数仅为待日期准入后的原增量预校准，不改变旧51项评分。root 独立读前六项完整v1摘要并认可进入日期核实；01046浏览 exact-v1缓存失败，但当前 `/abs/2601.01046` 只列v1，HTTP实际完整摘要已再读，版本身份可核。没有冒称任何一项正文证据审阅完成。

| 精确材料 | 摘要实际增量与准入理由 | 不授的结论／下一门槛 |
| --- | --- | --- |
| [2601.01280v1 Does Memory Need Graphs?](https://arxiv.org/abs/2601.01280v1) | 统一分解长期 dialog memory pipeline，对 LongMemEval/HaluMem 分阶段受控比较，基础配置而非图结构可能解释结果差异；是 graph-memory设计反证线索，不仅新框架名 | 尚未核控制变量与正文，不授所有图 memory 无效；拟3+1+2=6，公开日→必要原证据→具体AGENT-MEMORY/RAG owner比较 |
| [2601.01624v1 How Does Prefix Matter in Reasoning Model Tuning?](https://arxiv.org/abs/2601.01624v1) | R1三模型、0–100% prefix混合，移除intro boilerplate未必更好；math/safety与coding/factual方向不同，挑战SFT清洗直觉 | gradient-anchor因果仅作者解释待核；拟3+1+2=6，不把局部Safe@1变成行动安全 |
| [2601.01299v1 T3C](https://arxiv.org/abs/2601.01299v1) | 一次训练后的rank×precision可变预算控制、elastic factorization、rank-tied量化及控制器，声称 spectral/activation logit-drift证书；视觉backbone不是排除理由 | 证书前提、rank/bit可行性与实测budget映射待核，不授普适可靠性；拟2+1+2=5 |
| [2601.01584v1 Steerability of Instrumental-Convergence Tendencies](https://arxiv.org/abs/2601.01584v1) | 明确授权模型构建者与未授权攻击者的steering tension；Qwen3 InstrumentalEval pro/anti suffix结果改变，提供安全/可控性评价边界 | 标签/语言输出不等真实关停、资源获取或行动安全；拟3+1+2=6，安全相关必要深入范围待正文核 |
| [2601.01500v1 DiT-HC](https://arxiv.org/abs/2601.01500v1) | CPU集群DiT训练：communication-free tensor parallel、memory-aware dataflow、matrix/vector算子以及MPI重叠；实际训练/并行增量而非AI-for-Science应用标签 | 256节点weak scaling与算子局部收益不直接授GPU替代/全成本优势；拟2+2+2=6 |
| [2601.01712v1 RelayGR](https://arxiv.org/abs/2601.01712v1) | 长sequence生成推荐的selective pre-inference、HBM resident KV、sequence-aware bounded cache、负载/亲和路由与DRAM reuse；生产者/消费者亲和与SLO资源机制具体，不因推荐领域排除 | 尚未核P99预算、query选择人口及全成本，不授通用SLO保证；拟2+2+2=6 |
| [2601.01046v1 KV-Embedding](https://arxiv.org/abs/2601.01046v1) | 摘要实际声明因果mask使早token无未来context，末token各层KV编码sequence摘要，再将其作为prefix重新路由给所有token；intrinsic-dimensionality自动选层，冻结Qwen/Mistral/Llama的MTEB及4096长度有限结果。是causal→global representation机制线索 | 单forward具体执行、layer选择与成本/表征条件未核；不把局部最多10%收益当普效。拟2+1+2=5，root已认可按此具体机制进入日期核实 |

## 7 项未形成新增候选的负侧／旧事件线索

这些判断来自完整题摘，而非标题关键词；不因科学、推荐、视觉领域或少模型自动排除，也不以“不写Books”倒推低分。root本轮还需独立负侧抽核。

| 精确材料 | 实际筛选理由与边界 |
| --- | --- |
| [2601.03285v1 Feedback Indices to Evaluate LLM Responses to Rebuttals](https://arxiv.org/abs/2601.03285v1) | fictitious previous response/MCQ rebuttal的stubborn/sycophancy指标、两道Physics题；摘要未建立改变长期评价解释的新控制条件或设计反证。贡献前关闭；不为不影响处置的提交/公告差异追日期 |
| [2601.02092v1 SuperSFL](https://arxiv.org/abs/2601.02092v1) | 资源子网、weight sharing、三阶段gradient fusion/client classifier的federated视觉组合，摘要未说明新的基础模型训练条件或长期解释增量。贡献前关闭，不以CIFAR/100clients大小本身排除 |
| [2601.00969v1 Value Vision-Language-Action Planning & Search](https://arxiv.org/abs/2601.00969v1) | 冻结Octo后MLP value给MCTS prior，LIBERO有限成功率/simulation差异；题摘只有成熟value-guided search组合局部结果，未明确新失效边界。贡献前关闭，不授“实验小所以无价值” |
| [2601.00943v1 PhyEduVideo](https://arxiv.org/abs/2601.00943v1) | physics教学T2V的视觉平滑与概念正确评价区分，但摘要是领域benchmark/metric，没有决定性新一般机制或控制条件。贡献前关闭，非科学主题禁入 |
| [2601.00998v1 DVGBench](https://arxiv.org/abs/2601.00998v1) | 显式/隐式UAV grounding benchmark，I2ECoT+RL及局部gain未建立超出检索/绑定组合的新一般解释条件。贡献前关闭 |
| [2601.01024v1 ITSELF](https://arxiv.org/abs/2601.01024v1) | attention bank、多层diversity/top-k token预算/coarse-to-fine TBPS局部recipe，三dataset摘要没有新一般可靠性条件或受控反证。贡献前关闭，不仅看headline |
| [2601.00126v1 Compositional Diffusion with Guided Search for Long-Horizon Planning](https://arxiv.org/abs/2601.00126v1) | denoising中搜索、likelihood pruning/overlap resampling确有机制线索，不能按领域关闭；但当前v1仅显示Dec31提交、v2仅Jan5提交，未定位Jan06新的首次公开或重要机制修订。旧事件/版本线索，不搬成Jan06候选，不用v2号替代重要修订判断 |

## 2 项延迟编号／公开日未明线索

| 精确材料 | 完整题摘与日期限制 |
| --- | --- |
| [2601.06100v1 Filtering Beats Fine Tuning](https://arxiv.org/abs/2601.06100v1) | linearized Gaussian latent-state/Kalman adaptation、token Jacobian observability、covariance contraction和优化singular limit；具有理论条件线索，但06100编号与Jan2 Submitted不等Jan06公开。未准入，需具名首次公开记录才能判本日 |
| [2601.06103v1 The Impact of Post-training on Data Contamination](https://arxiv.org/abs/2601.06103v1) | Qwen/Gemma受控插入GSM8K/MBPP测试样本，continued pretrain表面inflation淡化后SFT/GRPO再浮现及干净任务方向差异；有评价反证线索。06103编号与Jan3 Submitted不等Jan06公告，不能直接纳入本日 |

## 日期核实停点与精确恢复材料

七项拟准入各执行官方 arXiv 域 + exact ID + January6限定查询，均无可用结果；06100/06103具名官方查询与exact-v1页面也没有公开日字段。空搜索不是零事件。对01280额外读[官方DOI元数据](https://api.datacite.org/dois/10.48550/arXiv.2601.01280)：v1 Submitted为Jan3、Updated为Jan6、Available为2026-01、Issued为2026、created/registered为Jan6；这些不直接充作公开日期。二级聚合网站的Jan6标签只当发现线索，不支撑准入。旧51项日期证据与有效结论不重开。

本轮未发现明确 withdrawal/corrigendum 需要改变已审命题；01584/01280/01500/00126版本提交记录只作定位线索，未把版本号或Submitted/Updated当“本日已公开重要修订”的证据，也未冒称完成所有revision召回。

必要恢复请求限定为以下 **7 个 exact-v1** 的首公开日期（到日即可）／带日级公告ID的官方记录，或具备公开日期的作者官方发布记录：**2601.01280v1、2601.01624v1、2601.01299v1、2601.01584v1、2601.01500v1、2601.01712v1、2601.01046v1**。06100/06103仅保留恢复线索，尚未作本轮具体贡献校准，不升级为必要材料请求。不请求全机构无删除、所有更早镜像或秒级公开时刻。只有证据证实Jan06才定点继续对应精确版本贡献/证据门；证实他日则只关闭本日报告的归属线索，不自主跨日。

## 计数与待独立验收

- 来源：14/14每日源均实际有界检查；Meta入口检索受限，不声明全站完整。
- 阅读：16个具名完整题摘；7个贡献理由已校准的拟准入、7个负侧/旧事件线索、2个延迟编号日期线索。不是16次正文审阅，也不包含旧51项复审。
- 本轮确认新增候选0；新评分定案0；新完成证据审阅0；新Books写入0。七项“拟”评分不进入冻结51表。
- 本轮作者普通工作：来源/题摘/精确日期补检完成；等待root对上述负侧、日期停点及真实报告更新做非作者独立终态验收。日期未落实的具名材料隔离，不冒充“无新增研究”。

## root非作者最终校准与日级验收

复核者：root；结论：通过（本轮安全终态，不授外部缺口或无遗漏）。2026-10-07 14:58 +08。上文是作者原中间停点，最终范围/处置以本节和当前Report为准。

root完整读全部16具名v1题摘与具体理由，定点补读SuperSFL02092 §II-B/C与V-VLAPS00969 §3。SuperSFL实际以子网深度/损失加权融合梯度，5秒timeout转本地classifier后再恢复共享权重；当前是局部heterogeneous classifier训练组合，没有新增foundation共享训练状态/恢复合同或具体反证，不因CNN、数据规模或联邦标签排除。V-VLAPS的冻结Octo上MLP value进入MCTS的Q，prior仍另算U；原“给MCTS prior”表述纠正。它当前为成熟value-guided搜索的局部组合，未提出改变VLA/controller职责或失效边界的条件；不以小任务实验自动排除。其余03285/00943/00998/01024完整题摘与理由已核，00126保旧事件/版本线索，不用版本号代重要修订；这些6关闭+1旧事件不冒称7篇全部正文审阅。

06100与06103的完整题摘经root独立重读后，不能只留下未校准线索：前者在linearized Gaussian条件把token Jacobian可观测性、posterior covariance收缩与mean收敛分开，优化作为奇异极限；后者通过插入污染后continued-pretrain表面遗忘及SFT/GRPO再显现，挑战只在pretrain后查污染的评价权限。两者各有具体长期解释/测量增量，故与原7项一起保留9个具名日期请求；尚未必要审阅这些理论/实验，更不由摘要授证明。

最终互斥分区为9潜在贡献/datehold、6贡献前关闭、1旧事件，合计16完整题摘；新增确定候选/评分/完整证据/Books均0，原51/19实际整合及全部日期分数不变。必要恢复材料为01280/01624/01299/01584/01500/01712/01046/06100/06103各exact-v1的带ID官方日级首次公开，或同正文作者官方具名日期；源链接已在上表逐项保存。缺少这一个归属事实不能先纳入Jan06，不要求时分秒、全机构镜像或全月批次。公开日到达仅重开对应项，不自主迁其他日。原七项材料请求被本节九项最终清单替代，不重复索取。

14源当前有限停点已核并写回自包含表：11有限已查，Google/Meta必要日级入口和arXiv9项日期保留为3受阻；受阻不授Coverage/Evidence通过。Qwen60/Hunyuan9/MiMo已恢复的有限目录不再要求无具名遗漏的全历史；公开revision召回仍有原接口限制，不把Submitted/Updated或空检索当阴性证明。只核这些实际范围，不扩大每周源、全部metadata题摘或所有附件。机器接口校验及限定diff检查通过与否由实际命令记录，不能代替本节语义验收。
