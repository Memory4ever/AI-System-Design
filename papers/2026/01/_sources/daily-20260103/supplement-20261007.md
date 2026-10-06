# 2026-01-03 Daily：增量来源补查

作者：supp_jan03。检查时间：2026-10-07T13:25:15+08:00。独立复核：待 root；本记录不自行授予报告完成。

本轮仅检查补充窗口 **2026-01-02 ～ 2026-01-02**，保留本日 README 的原窗口、候选日期、评分和有效审阅。已完整重读 AGENTS、当前研究合同、Report 合同、Prompt、来源使用说明/每日组/arXiv 主题范围、ROADMAP 与相关 checkpoint，读取本日 README、queries-and-screening、source-date-boundary 及引用的原始日期字段。旧范围与结果不自动成为补充窗覆盖证明；跨日只为 PhyGDPO 身份去重定点读取 01-02 的具体条目。未采用 Weekly 反推结果，未读取窗外正文形成候选池。

## 结果与计数边界

14 个每日来源均实际进入本轮有界检查。新增正式候选 **0**，新增必要证据审阅 **0**，新增 Books 整合/已有覆盖 **0**。Grove 是本日既有贡献前排除；新恢复的 Meta dated 条目 PhyGDPO 是 01-02 已有效审阅的同一 v1 家族，不重列、不评分、不搬日期。新增长期知识判断为 No Change，不因“映射得到 owner”制造 Books 改动。

这不是全机构/全学科无遗漏声明。可读官方 dated 目录和 API 按实际有限范围记已检查，不为证明不存在删除、隐藏或作者镜像索取全机构历史快照。真正仍不能取得的日级目录/日期分别列在后面的具体限制中，不用于正面证据。未重新执行旧候选审阅、代码或实验。

## 14 来源：实际入口与停止位置

| 来源 | 本轮实际检查及停止点 | 本轮结果与边界 |
| --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/) → [官方 RSS](https://openai.com/news/rss.xml)，HTTP 成功，1251 项只解析 title/link/pubDate 定位 Jan02；前邻 Dec22、当日 Grove、后邻 Jan07 Health；随后读 Grove 核心及完整 FAQ | 已检查。Jan02 唯一定位项重复贡献前关闭；1251 是目录总数，非当日材料数，未展开全年正文 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 当前入口；本轮原 HTML 解转义后 174 个 publishedOn 字段，定位 Dec19 Bloom → Jan08 critical-infrastructure-defense；Jan02 无字段 | 已检查该官方有限目录切片。只读元数据，不把 174 项作为逐项题摘队列 |
| SRC-GOOGLE-AI | [DeepMind Research](https://deepmind.google/research/) → [Publications page1](https://deepmind.google/research/publications/)，265 项/9 页，page1 的 Jan09 TRecViT → Dec03 Reward Features 跨窗，止 page1；[Google Research pubs](https://research.google/pubs/) 当前页和官方域 Jan02 日期/主线主题搜索首组 | DeepMind 有限 dated 切片已检查；Google Research 可见 2026 年级筛选但无 Jan02 日级发布字段，日期目录受限，不展开其 392 个年级条目 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)正文提取 0 行后，官方域 Jan02 搜索定位[作者页](https://ai.meta.com/people/1084083712703418/felix-juefei-xu/)；实际打开 [Publications page3](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=3)，在 Jan02 PhyGDPO 后混入 2020 等旧置顶项，止 page3；再打开本项官方完整题摘和 exact-v1 版本页 | 已检查有限原始片段，1 个已审家族关联。没有把 Research 空正文当零发布，也不把 page3 的旧置顶当严格全局排序 |
| SRC-QWEN | [旧 Blog](https://qwenlm.github.io/)首屏最晚 Sep23，跳[新 Blog](https://qwen.ai/blog)提取 0 行后，本轮 fresh GET [官方 API](https://qwen.ai/api/page_config?code=research.research-list) 成功，60 项按 date 字段整体定位，不依赖对象顺序，最大 date=2025-12-23T05:08:30.000Z；止单响应 | 已检查这份有限官方配置；未定位 Jan02。API 最新日期停在 Dec23，不能称其覆盖了完整 2026 发布列表；未以模型名或创建时间填补 |
| SRC-DEEPSEEK | [首页](https://www.deepseek.com/) → [News](https://www.deepseek.com/news/)有限 10 项研究索引，Jan12 Engram → Dec31 mHC 跨目标日；另有 5 项动态及“查看全部”，止这一索引 | 已检查有限 dated 索引，无 Jan02 行。日期只作该目录公开字段，不宣称全部机构发布 |
| SRC-MOONSHOT | [Kimi Platform Blog](https://platform.kimi.com/blog)当前 26 项 dated 列表，最新 Nov07 2025，止首响应；定点复用本日 kimi-date-slice 的 changelog 邻接 Dec31 0.70 → Jan04 0.71/0.72，不展开组织全部仓库或普通 PR | 已检查有限入口；Blog 当前片段不含 Jan02。没有要求证明所有仓库未发布，也不把 changelog 邻接换成完整机构研究覆盖 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)本轮 web 超时；改用已经确认的官方前端接口 fresh POST [publicList](https://api.hunyuan.tencent.com/api/blog/publicList)，body={pageNum:1,pageSize:1000,renderType:0}，code0/totalNum9/list9；只读取 title 和原始日期字段，止 page1 | 官方有限 API 已检查，最早 displayPublishTime=1770090898（Feb03），没有 Jan02 行。publicAt/publishedAt/display/created/updated 不混用，不以构建或创建时间推首公开；不为缺全机构隐藏史保留无限请求 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)当前 15 项 dated 卡片及“查看更多”，Jan13 → Dec10 跨目标日；[release notes](https://docs.z.ai/release-notes/new-released) Jan14 → Dec22 跨窗，止该有限目录/说明页 | 已检查两个官方 dated 切片，均无 Jan02 行，不因可查看更多要求读全年无关内容 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)与[论文页](https://seed.bytedance.com/en/public_papers)首屏后，fresh 官方 get_article_list_v2 的 article_type=1/2、publish_year=2026、count20、page_token0、order_desc=false；返回20/9项（不等于旧记录的本地化19/14项），最早 PublishDate 分别1768838400000（Jan20 BJT）/1770825600000（Feb12 BJT）；止各首片，均next=20/has_more=true | 已检查有限官方 API 日期片段；未定位 Jan02，不将置顶项作停止条件。2025 DESC blog 首片15项最新1766505600000（Dec24 BJT），paper首片0但has_more=true，0不承担零发布权限；2026 切片本身已给窄停止点 |
| SRC-BAIDU-ERNIE | [官方 Blog page1](https://ernie.baidu.com/blog/zh/)，10 dated 卡片，Jan08 → Dec23 跨窗；下一页2/2更老，止 page1，未读 page2正文 | 已检查这一官方 dated 切片，无 Jan02 行，不借排行榜正文制造候选 |
| SRC-XIAOMI-MIMO | [MiMo](https://mimo.xiaomi.com/)当前 8 Papers 的 Jan08 technical report → Oct21 router论文跨窗；15 Blog 卡片无可见日期及 More；官方域 Jan02 搜索首组，止有限入口 | Papers 有限 dated 切片已检查；Blog 15卡片无法据此确认 Jan02 日期，保留明确目录日期限制，不读所有窗外技术正文 |
| SRC-MINIMAX | [英文 Blog](https://www.minimax.io/blog)12 dated 卡片 Jan27 → Dec23 跨窗；本轮原 HTML 成功恢复 minimaxi→[中文 Blog](https://www.minimax.cn/blog)13 dated 卡片 Jan28 → Dec23 跨窗；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)原 HTML 去 script/style 后实际只有一个 dated 技术条目2026-05-13，止当前列表 | 已检查三个有限官方片段，无 Jan02 条目。旧中文/Agent只有壳的访问限制本轮解除；英文Jan27与中文Jan28保留各自字段，不机械合并日期 |
| SRC-ARXIV | fresh 读取[假期公告原 HTML](https://blog.arxiv.org/2025/11/21/temporary-changes-to-announcement-schedule-due-to-end-of-year-holidays-2025/)：Dec31 ET后一常规新投稿公告是Jan04 ET（Jan05 BJT），Jan02 BJT无new公告；另四主题 Jan02完整BJT日 older-update API各 start0/max20/total0，但API改写过滤导致互斥submittedDate，尝试无效；[cs.CL catchup Jan02](https://arxiv.org/catchup?subject=cs.CL&date=2026-01-02&include_abs=False) HTTP400，止请求 | 新公告日期有官方依据。元数据查询只辅助旧稿revision定位，不以submitted/updated宣称公开；历史公开revision列表接口仍受限。未扩 cs.CL 全月或全分类池，也不要求没有具体线索的全部作者镜像 |

## 日期与查询原始字段

所有检查以公开**日期**为筛选条件；下面仅保留原接口的字段口径，不以时分秒设置论文准入门槛。

- RSS 当日行：title=`Announcing OpenAI Grove Cohort 2`，link=`https://openai.com/index/openai-grove`，pubDate=`Fri, 02 Jan 2026 10:00:00 GMT`，北京时间日期 Jan02。官方正文只标 `January 2, 2026`，同样足够采用其公开日期。
- Anthropic fresh 原字段邻接：`publishedOn=2025-12-19T19:45:00.000Z`、slug=`bloom`；`publishedOn=2026-01-08T00:00:00.000Z`、slug=`critical-infrastructure-defense`。174是元数据字段数量，不是本窗候选数量。
- Qwen fresh 最大行：id=`qwen-image-edit-2511`、date=`2025-12-23T05:08:30.000Z`、title=`Qwen-Image-Edit-2511: Improve Consistency`。60项按原date比较，没有用weight或出现顺序替代日期。
- Hunyuan最早display行：id=100025，title=`Learning from context is harder than we thought`，publicAt=1770112927，publishedAt=1770090898，displayPublishTime=1770090898，createdAt=1770090168，updatedAt=1770090898。保留字段差异，不把其中任意日期冒充统一首公开字段。
- Seed fresh 首片URL：`https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2026&count=20&page_token=0&order_desc=false`；type2其余参数相同。type1 total82/next20/has_more=true，type2 total23/next20/has_more=true；实际返回20/9是本次响应，不继承旧快照数量。只有日期切片读取，不是这些材料的题摘审阅。

### 官方域补检

本轮实际执行四个 Jan02 主题查询，每组仅读首返回结果，不翻搜索页：

1. `("2026-01-02" OR "January 2, 2026") (model OR research OR agent)`；domains=`openai.com,anthropic.com,deepmind.google,research.google`。
2. `("2026-01-02" OR "January 2, 2026") (model OR research)`；domains=`ai.meta.com,qwen.ai,qwenlm.github.io,deepseek.com`。
3. `("2026-01-02" OR "2026年1月2日") (模型 OR model OR agent)`；domains=`platform.kimi.com,hunyuan.tencent.com,zhipuai.cn,docs.z.ai`。
4. `("2026-01-02" OR "January 2, 2026") (model OR research)`；domains=`seed.bytedance.com,ernie.baidu.com,mimo.xiaomi.com,minimax.io,minimax.cn`。

首返回明确相关的 Jan02 原始线索是 Meta 作者页的 PhyGDPO，已回原始完整题摘和版本核对。其他结果含社区工具调用帖子、窗口外公开的机构文章与年份漂移，不以搜索摘要作原始证据；未获得另一确定当日研究事件。搜索没有召回并不证明机构零发布。

### arXiv：有界元数据查漏

后续独立核对API返回的查询标题：请求中的lastUpdatedDate被改写为submittedDate，与另一Submitted区间互斥。以下四次0响应仅是尝试事实，不支持没有旧稿更新或公开修订；原公开revision列表限制仍隔离。

共同前缀是 `lastUpdatedDate:[202601011600 TO 202601021559] AND submittedDate:[199001010000 TO 202601011559] AND `，UTC边界仅为API编码对应Jan02完整北京时间自然日，公开事件归属仍须官方dated列表/公告；每组 start=0/max_results=20/sortBy=lastUpdatedDate/sortOrder=ascending，fresh XML totalResults均为0、entries=[]，不翻页。

- model：`((cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:MoE OR all:"foundation model"))`
- system：`((cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:LLM OR all:GPU OR all:kernel OR all:"model inference" OR all:"distributed training"))`
- multimodal：`((cat:cs.CV OR cat:cs.RO OR cat:cs.LG) AND (all:"foundation model" OR all:"world model" OR all:VLA OR all:multimodal OR all:"diffusion model"))`
- agent：`((cat:cs.AI OR cat:cs.IR OR cat:cs.MA OR cat:cs.CL) AND (all:LLM OR all:"language model") AND (all:agent OR all:RAG OR all:memory OR all:reasoning OR all:planning))`

这没有将 Jan02提交的全部论文拉成待关闭池。Jan02提交字段不等于Jan02公开；官方假期原文说明new-submission公告与公开延期，但不证明revision无人修改。历史公开revision列表无法读取，与API零命中分别保留。

## 完整题摘/核心说明语义判断与去重

### Grove：复用既有贡献前排除，非新候选

[官方原文](https://openai.com/index/openai-grove/)标题及正文核心、完整FAQ实际重核。全部相关内容是早期创业/技术人才的五周社群项目，约15人、线下工作坊/office hours/导师支持、模型或工具先行体验、融资资源、报名期限与参与方式；没有披露新的学习、训练、推理执行或可靠性机制，也未给足以改变设计选择的边界或反证。单纯给模型preview访问不构成模型机制贡献。January12关闭报名是状态更新，非研究纠错信号。保留本日既有排除，不评分、不用社群机制硬映射Agent owner。

### PhyGDPO：有潜在系统增量，但同一v1已审，不重复准入

本轮读完整标题与 [Meta 官方完整摘要](https://ai.meta.com/research/publications/phygdpo-physics-aware-groupwise-direct-preference-optimization-for-physically-consistent-text-to-video-generation/) Abstract 全三段及 [arXiv exact-v1](https://arxiv.org/abs/2512.24551v1) 摘要/版本记录。官方标题是 *PhyGDPO: Physics-Aware Groupwise Direct Preference Optimization for Physically Consistent Text-to-Video Generation*，官方公开列表与原文日期均为 `January 02, 2026`，没有时区/小时；日期本身足以记录该机构条目。

完整摘要的语义是：图像质量较好并不等于视频符合物理；图形模拟/提示扩展受简单环境和隐含物理推理限制，富物理交互数据也不足。作者提出 VLM+CoT 的 PhyAugPipe 构造 PhyVidGen-135K，再以 groupwise Plackett–Luce 偏好模型替代只比较两个样本的方案，VLM物理奖励PGR引导优化，LoRA-Switch Reference避免复制大reference的内存开销；最后声称在PhyGenBench/VideoPhy2超过开源对照，并链接项目页。潜在贡献链为：成对偏好及大reference受限 → group目标+物理奖励+reference共享 → 需要核查群体概率合法性、训练目标与reference成本是否成立。不是因带“physics”而当作AI for Science排除，也不是只因可映射DPO便收录。

身份去重后发现 [01-02 README现有PhyGDPO证据段](../../02/README.md#phygdpo-physics-aware-groupwise-direct-preference-optimization-for-physically-consistent-text-to-video-generation) 已处理 **2512.24551v1**；分数2+2+2=6不变。原审阅实际核v1 Eq2–14和默认参数，指出group概率分母不含winner、Eq9两行符号不等、正alpha条件仍可能不满足gamma界；中心推导安全隔离为争议/暂缓，不据LoRA成熟事实替代中心贡献，也不宣称全部实验无效。必要证据和独立复核在 [EVIDENCE_BATCH_11_INTERFACES](../../_sources/daily-20260102/EVIDENCE_BATCH_11_INTERFACES.md)。

当前v1版页的submission history是Dec31 v1、Jan30 v2、Mar05 v3、Jun18 v4；没有Jan02新版本或原页纠错标记。只核当前事件已有说明，不深入窗外v2–v4。Meta Jan02完整摘要与原v1所述机制相同，是官方索引/机构发布关联，不另生机制修订；不能改写既有论文首次公开归属。因此本轮不重评分、不重复审阅，也不将旧争议改为无贡献。既有独立结论保留；潜在owner是 `TRAIN-DPO`（训练偏好目标），reference共享属于其训练实现交接，视频生成/物理一致性不自动移给 `MULTIMODAL-WORLD-MODELS`。没有新采用命题，故本轮没有Books修改proposal。

本轮定点对照实际 Books：Ch34开头与§KL-constrained/Bradley–Terry论证把偏好概率、reference/support条件和目标合法性放在同一链中，reference logprobs一节明确reference缓存/forward身份；Ch30开头拥有低秩参数化而非偏好目标，Ch24开头拥有生成factorization/state/commit而非群体偏好概率。这里仅核owner边界，不将这些成熟原则当作PhyGDPO新贡献或新增“已有覆盖”计数。旧争议目标不通过本轮目录关联升级为书稿知识。

## 可直接并入 Report 的增量文字

补充窗口2026-01-02～2026-01-02已实际进入14个每日来源的有界检查，新增正式候选0、新增必要证据审阅0、Books No Change。Grove保留原贡献前排除；Meta官方Jan02 dated PhyGDPO条目已读完整摘要并定点核身份，属于01-02已有效审阅的2512.24551v1关联，不改既有日期、6分和中心推导争议处置。MiniMax中文/Agent旧壳限制已由本轮原始HTML恢复解除；Qwen60项、Hunyuan9项、Z.ai与Seed有限官方日期片段可核，按实际范围记录，不再要求全机构隐藏/删除历史来证明召回。Google Research日级公开日期、MiMo Blog日期及arXiv公开revision历史接口的具体限制仍不支持正面证据、Books或无遗漏断言。独立补查验收由root完成，旧完成声明不替代本轮验收。

## 具体外部保留与精确重开点

尚可执行工作：root对本轮查询范围、Grove排除、PhyGDPO同一事件去重和以下限制作独立复核，并将实际结果融入既有六部分。作者有界补查已完成，不把普通未审条目包装成外部阻塞。

1. **Google Research Jan02主线dated切片**：当前 [pubs](https://research.google/pubs/)只有年级筛选，官方日级公开列表/发布日期字段不可恢复。需要覆盖Jan02模型、训练、推理、多模态、Agent主线的官方dated结果或具体原始发布；不是全年392项逐篇正文或全机构快照。仅重开该来源该日日期定位。
2. **MiMo当前15个Blog卡片的公开日期**：原目录卡片未给日期；需要官方卡片日期映射、Jan02 dated Blog列表或具体当日原始发布，不索取全部机构历史。论文8项的dated切片已检查，不把Blog未知写成论文缺口；恢复后只处理确认当日事件。
3. **arXiv Jan02公开revision列表**：`catchup?subject=cs.CL&date=2026-01-02&include_abs=False` HTTP400；API四主题older-update被改写为互斥submittedDate，零响应无效，不支持没有修订。可接受当日官方主题公告/列表快照或具体版本的公开公告；只恢复旧稿revision的公开日期/重要增量，不拿new假期规则外推revision或扩全月。没有具体作者先行线索，不另请求全体镜像。

Qwen配置仅到Dec23、Moonshot Blog仅到Nov07是当前有限入口的已知边界，不自行声称全机构Jan02零发布；没有已定位的必要当日正文，故不另创建笼统全机构材料请求。任何后续带具体身份的Jan02官方发布再定点重开。Hunyuan和MiniMax可读切片不因缺所有隐藏历史继续受阻。

未stage、commit、push；仅新增本文件，未改README、Books、LEARNING_STATE或共享索引。两个本地证据目标实际存在；新增文件的 `git diff --no-index --check /dev/null <本文件>` 无空白诊断，退出1仅表示新增diff。Markdown表格/本地引用及限定路径状态已核；机器检查不等于root语义验收。
