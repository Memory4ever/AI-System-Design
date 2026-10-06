# Seedance单篇日期/准入准备包

作者Carson；2026-10-14T17:14+08。只Dec15完整BJT自然日；待Feynmanactual事件/最小准入校准，不授评分、正式行或Books。原同家族2512.13507的完整v1题摘已读及Popper原准入层有效复用，不再取legacyAPI。

## 1. 本日实际原件与日期角色

从[官方Publications](https://seed.bytedance.com/en/public_papers)进入已公开接口，实际GET `https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&count=20&page_token=0&order_desc=true`，`x-tt-locale:US`；HTTP200/49453B，原件[JSON](RAW_SEED_PAPERS_20261014.json)/[headers](RAW_SEED_PAPERS_20261014.headers)。结构解析真实18条、total94、next20/has_more true，未请求后页。pin1323 Dec15、875 Dec2；普通Oct21→Jun25已在目标日下，停止首片，不扩94论文队列。

对象`ArticleMeta.ID=1323`、`Author=Seed Vision Team`、`ArticleType=1`、`Journal=arXiv`、`Status=2/StatusEn=2`、`IsPinned=true`。原公开`PublishDate=1765728000000`是2025-12-15 BJT日期编码；`UpdateTime=1776909453000`是后续2026修改，分离保留，不用后改时间倒证原字节。英文题名 **Seedance 1.5 pro: A Native Audio-Visual Joint Generation Foundation Model**，`ExternalLinks`精确指向`https://arxiv.org/pdf/2512.13507`，不是另一稿。官方目录承担研究论文披露/当前链接身份角色，不授arxivfirst或秒级公开。

本轮提案：将官方论文目录标示的Dec15 **研究披露事件**作为本日事件核，而非仅因旧09小时窗口跨界仍hold，也不冒称arxivfirst。它是否足以支持原研究披露而非单纯索引收录，请reader窄裁决。若成立，原必要v1方法/评价及独立评分/owner仍普通；若仅索引，不预入表，保精确日期出口。不要求全球absence/同bytes唯一日期门。

## 2. 家族/版本及明确未采用

原2512.13507v1提交2025-12-15T16:36:52Z＝Dec16 BJT00:36:52仅Submitted；不以此排除Dec15官方事件或授first。原v2 Dec16/v3 Dec23是版本身份，不自动重要修订；未据当前v3正文倒填v1。Blog1817原`PublishDate=1765882058000`＝Dec16 BJT18:47:38为另一次官方Blog，窗后且同家族，不新增第二篇。原机构摘要与v1原题摘相同，避免跨源重复家族。

## 3. 最小潜力及后续必要域

原视频生成/后配音的时间关联约束→dual-branch DiT与cross-modal joint module联合音视频生成→需比较音/视频分支耦合如何控制同步与代价。多阶段data/training、SFT/multi-reward RLHF为待核具体作用，不把成熟RL本身或10x宣传计贡献。若官方事件通过，必要Source只读精确v1架构耦合/训练接口、对照评价/同步失效和加速兼容采用范围；不全量权重/工具/所有benchmark。

当前正式0/评分未授/Books未决，无锁。候选owner仅`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24路由，不因能映射或原有一般跨模态知识预判NoChange；必要证据后才实际比较目标与邻接、给具体差额。现包可直接供Feynman读，不等待十四来源/全日日期请求。

## 4. Feynman4已核事件/后稿精确补证实际读域

actual读Feynman§4：Dec15机构自有论文介绍/原正文出口日及窄P通过，非arxivfirst/当前PDF历史字节。只继续本family必要Source，不重目录/AB/date。精确[PDFv1](https://arxiv.org/pdf/2512.13507v1)本日实际保存[原件](RAW_SEEDANCE_V1_20261014.pdf)：首次40sHTTP200下载1978139/3154816B、exit28 partial，不称成功；一次非legacy有限Range续传HTTP206/1176677B成功，总3154816B。标准pypdf可完整解析11页，actual读取pp1–8正文、pp9引用及10–11作者名单角色；未做图像像素或全部图数复算，不签复现。

PDF页1标arxiv2512.13507v1/15Dec2025，但Submitted在BJT为16日，**后续精确稿补证**不反证当前PDF全部细节已在机构Dec15可见。原机构与v1摘要共同支持dual-branch DiT/cross-modal joint module这份公开架构声明；v1新增解释/实验只绑定v1，不迁原事件时间。

## 5. 必要Source事实/兼容限制

pp1–3摘要/Intro给dual-branch与MMDiT式跨模态交互、T2VA/I2VA及T2V/I2V混合任务预训练、视频–音频coherence数据筛选、caption/curriculum、高质量SFT和multi-dimensional reward RLHF。**这里没有展开coupling算子、位置/时钟编码、联合noise/采样schedule、loss权重或奖励公式**；不能从MMDiT名字补造实现、独立/共享噪声或梯度归因。Fig2是概要管线，非实现/可执行协议，未签其图像逐像素验收。

pp3–7 §2.1的SeedVideoBench1.5从真实用户prompt构建，覆盖行业场景/专家评审。视频五点Likert absolute与pairwise GSB分开；音频另有prompt、quality、AV sync、expressiveness。音/唇、sound/visual events与画面稳定/生动是不同量，作者明确慢动作可能人为提高稳定而降低vividness。视频比较Kling2.5/2.6、Veo3.1、Seedance1.0，音频还有Wan2.5/Sora2；比较population/模型集合不同，不拼统一SOTA。文中专家来自电影/摄影/设计，但这些pp没有披露测试prompt总数、标注者数/独立分配、CI或显著性、每模型生成预算/随机种子；均Not Disclosed，不把专家标签当独立同行评估。没有isolated joint-module对照，观测总模型偏好不能证明该module单因果。

pp2的近3x RLHF训练与超过10x end-to-end来自multi-stage distillation+quantization+parallelism组合；硬件/精度、NFE基线、batch/concurrency、时长/分辨率及质量预算未绑定。不能授跨负载加速、无损或纯coupling性能收益。pp7–8应用声称中文方言/歌剧/镜头control，其声调、声画、多角色身份例是作者结果，不授所有方言/长片连贯或生产可靠性；歌剧声腔仍在演化，没有全面失败人口统计。

## 6. 正式评分/采用准备给reader

拟采用对象只**此具体模型的联合双分支与跨模态模块/混合生成任务接口事实**：DesignDelta2（从视频/后配音独立通道变联合生成耦合）、SystemReach1（一个多模态生成模型，不借训练/serving名词扩大跨层）、Durability1（精确发布/版本架构事实；未披露足以变长期机制的算子或成立条件），2+1+1=4。不是因下载失败/预算不足降分，也不借通用“联合更同步”的旧原则计长期贡献；原P仍保，不改为C或用未知first挡官方日门。

提案**已关闭/仅报告**：清楚核身份/date/重复、具体架构声明和不能进一步采用的范围；不新增长期Books机制/不称已有覆盖。本次不采coupling算法、同步因果、训练recipe或性能倍数，因此无新Books写/PRE/POST义务。若未来公开精确耦合/对齐loss与可比joint-vs-posthoc反证，届时只该版本命题恢复，需实际Ch24 owner及邻接，不预签NoChange。请Feynman实际核评分与采用边界；当前仍未入formal或声称Source/BookGate最终通过。
