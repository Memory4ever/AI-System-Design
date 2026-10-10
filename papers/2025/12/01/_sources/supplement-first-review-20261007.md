# 2025-12-01 补查独立首校准

复核者：Sartre，agent ID `01a1152f-8719-7d52-bfd1-6c0c69dc8793`（本日非作者；由root明确委派）。

检查时间：2026-10-07T15:45～15:57+08:00。只写本文件；未改本日报告、作者记录、Books、State、合同、脚本或索引，未stage/commit/push。08-01作者停点与新增原件未动；本次不自审08-01。

结论：**八项潜在准入首校准通过；两项撤回排除通过；SuperIntelliAgent受影响公式的安全隔离通过。当前有1项普通来源描述必修，尚不授日级最终通过。**

修后更新（2026-10-07T16:24:46+08:00）：DeepMind这一项普通必修已独立定点确认通过，见本文末节；上述首轮结论作为当时事实保留。仍不授全日完成、14源Coverage/Evidence或Books Gate通过。

“通过”仅表示下述实际读取范围和处置，不认证八项目标日公开、方法收益、整个来源覆盖或Books。确定新增候选仍0，不是零相关事件。不能因缺公开日改判贡献关闭；也不因这些日期未知而要求展开全部八篇方法。

## Fresh Context 与实际读取

切日重新读取主工作区AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、RESEARCH_SOURCES的使用说明/每日/arXiv/恢复说明、CODEX_RESEARCH_PROMPT、ROADMAP。只加载12-01 README、本日[作者补查](supplement-20261007.md)与[本日原件](supplement-20261007/)；旧结果只从当前README识别保留边界，未无差别重审旧七份来源附件或21项旧潜力。

实际独立读取八个 `arxiv-2511.*v1.html` 的完整标题、Abstract、Comments及版本史；额外读取 `coursetime-current.html`、`withdrawn-personality.html` 的撤回说明。Super只读 `superintelliagent-v1.html` §2.1～2.2、Algorithms1–2与Eq7–9及直接相邻解释，不读§3实验/附录，也未读取其实际训练代码。页面头部/目录的其他标题不算审阅。

来源核验读取下表原件的有界日期/身份/错误/分页部分，不读全年各篇正文。另于本轮用web独立打开Google 2025 Blog、Meta Publications page4、Google pubs原入口和正确DeepMind `/page/3/`，分别得到实际目录、实际目录、工具不可达、不同于作者保存响应的真第3页。新增web观察以本文件URL/位置和边界保留；没有伪造curl成功原件或非作者全文复读。

## 普通必要修正

**1. DeepMind分页参数并未生效，需纠正“第3页”描述。** 当前README来源行（检查时L27）及作者补查来源行把 `research/publications/?page=3` 说成第3页。保存的 `deepmind-page3.html` 实际canonical为 `/research/publications/`，可见30张日期卡从2026-09-16至2025-11-04；Previous隐藏，Next为 `/research/publications/page/2/`。因此这是首页响应，不是成功翻到第3页，265是总目录数，不是本页已读数。

此响应已实际包含2025-12-03 Capturing Human Preferences、2025-11-21 Imitation Learning和2025-11-04下界；可以保留**该首页响应内目标日期相邻段**的有界观察，不必为修正标签再扫全年。复核者实际打开[正确第3页](https://deepmind.google/research/publications/page/3/)（web返回L117–148），显示2025-03-24至2024-09-21，证实两入口不是同一页。作者需改README和自己的停止记录，保留原请求失败/参数事实，不回写原件、不认证265/265或全站无遗漏。修复后只需定点确认该描述；不推倒八项准入。

Qwen旧请求描述并非当前必修：早次读取的README §5仍混列Qwen历史目录请求，随后在本复核期间已由作者/并发方修正为Qwen、DeepSeek实际邻接段恢复、撤销目录访问受阻（检查时L59）。本复核者没有改它；当前不继续索取已恢复目录。

## 八项完整题摘首校准

以下全部保留为**潜力、日期隔离、无评分/无Books采用**，不是八项已确认当窗候选。完整v1题摘已足以建立准入理由，除Super决定事实/必要纠错外，不为unknown date扩读普通方法。实验可识别性与性能边界是未来采用时的证据条件，不用作当前缩池理由。

| 身份 / 实际精确原件 | 独立校准与限定 |
| --- | --- |
| [Video-R2 2511.23478v1](https://arxiv.org/abs/2511.23478v1) / `arxiv-2511.23478v1.html` | 通过。答案正确与视觉依赖/过程一致可分离；TAC/VAS诊断及时间戳SFT/TAR提供具体评价/训练接口，不仅是11个benchmark数字。只承认值得核验的盲区；指标能否识别真正视觉因果依赖尚未审，不采用“trustworthy”保证。v1承诺将开源，v2后来状态不得回填。 |
| [Video-CoM 2511.23477v1](https://arxiv.org/abs/2511.23477v1) / `arxiv-2511.23477v1.html` | 通过。重新取证/聚焦的视频操作策略与step-level reward是具体增量，不能仅因“Agent流程组合”关闭。取证开销、奖励有效性与总预算对照未审，作者局部数字不是通用效率保证。 |
| [WMAct 2511.23476v1](https://arxiv.org/abs/2511.23476v1) / `arxiv-2511.23476v1.html` | 通过。按动作有效性调整奖励并退火交互次数，改变依赖环境反馈的训练约束。Sokoban/Maze/Taxi局部设置仍可有贡献，不因局部实验关闭；单轮成功不证明真实世界动力学内化、物理控制或安全。 |
| [ThetaEvolve 2511.23473v1](https://arxiv.org/abs/2511.23473v1) / `arxiv-2511.23473v1.html` | 通过。test-time RL参数更新、程序数据库探索及未见任务checkpoint比较，提出不同于纯推理搜索的机制。数学问题只是该训练机制的实验载体，非因AI for Science或8B模型自动排除。预算匹配/迁移归因未审，不能由新bound证明已内化能力。 |
| [VGT 2511.23469v1](https://arxiv.org/abs/2511.23469v1) / `arxiv-2511.23469v1.html` | 通过。理解侧语义encoder对齐pixel decoder并在连续空间AR生成，涉及表示/codec接口选择；不只是更高生成分数。20x、压缩率与“any VLM”外推均不采用，训练成本/对照仍未审。 |
| [Price of Progress 2511.23455v1](https://arxiv.org/abs/2511.23455v1) / `arxiv-2511.23455v1.html` | 通过。固定benchmark质量目标比较价格，尝试拆经济、硬件与算法效率，改变单纯榜单进步解释。估算性质不排斥准入，但也不等受控系统实测或已识别因果；5–10x/3x年率不采用。精确v1题名与2026v2区分成立。 |
| [GameCraft-2 2511.23429v1](https://arxiv.org/abs/2511.23429v1) / `arxiv-2511.23429v1.html` | 通过。文本/键鼠交互schema、从文本视频构造互动数据及注入机制具有具体world-model接口增量。视觉响应或作者“causal”命名不证明真实动力学可识别；InterBench有效性/控制失败条件尚未审。 |
| [SuperIntelliAgent 2511.23436v1](https://arxiv.org/abs/2511.23436v1) / `arxiv-2511.23436v1.html` 与 `superintelliagent-v1.html` | 通过窄准入。题摘的self-training/memory组合本身偏泛；§2.1～2.2明确条件向量、成功前后偏好配对、失败trajectory丢弃、成功replay和lag K，足以保留数据筛选/异步陈旧反馈的边界。下面独立必要core不授可靠单元、持续增长、objective等价或部署稳定。 |

这八份保存的官方abs状态中未见withdrawn标记，只支持这些当前页面的轻量观察，不授完整版本史检查。v1提交Nov28及首公告月份不能证明Nov30日公开，也不能因ID属于November先确定归属。当前作者没有因Books已有原则排除这八项，没有评分倒置或以日期缩池；本批未发现共同错误关闭理由，不需重开无关全年材料。

## 撤回与Super必要反侧

### 两项官方撤回

- **CourseTimeQA 2512.00360**：独立读 `coursetime-current.html`，v2明确withdrawn；Comments说明retrieval测量错误使Tables I/II/V/VI与摘要中心数字不成立。原排除成立，不能保留这些数字为正面证据；不是打不开正文的故障，不评分/Books。本轮没有重新采用链，未泛读撤回PDF。
- **2511.00115**：独立读 `withdrawn-personality.html`，作者说明撤回以实质扩展修订，v2明确withdrawn。按合同排除该撤回版本、不评分/Books；只记录观察，不把“准备重写”当新有效版本、当窗事件或反向首公开证据。与CourseTimeQA是不同撤回理由，不混为测量错误。

### SuperIntelliAgent Eq7→9

精确v1 §2.2的Eq7是 `-E log sigmoid(beta * (log pi_theta(x+|p) - log pi_theta(x-|p)))`；Eq8写 `log pi_theta ≈ -L_denoise + const`；Eq9却直接写 `E[L_denoise(x+) - L_denoise(x-)]`。

独立代入检查：令 `Delta = L_denoise(x+) - L_denoise(x-)`，即使接受Eq8并假设const可消，Eq7对应的仍是 `E softplus(beta * Delta)`，而非Eq9的 `E Delta`。前者每个pair对Delta的梯度为 `beta * sigmoid(beta * Delta)`，后者为1；多pair的权重一般不同，单pair标量单调性不能证明聚合目标或优化轨迹等价。v1相邻段没有给使这步变换等价的条件。Eq7亦没有显式reference-policy项；不能未经说明就认证它继承标准DPO/所引DiffusionDPO的保证。

因此独立确认的是：**所展示公式链不能支持直接等价主张**。没有证明实际代码一定按Eq9运行，也没有证明全部实验无效；不得改判整篇贡献关闭。Algorithm1只用冻结verifier自行分解/判定条件，成功轨迹选择/replay会带入judge误差与success-selection bias；Algorithm2声明lag不超过K，不提供可据此授部署稳定的证明。本轮没有正面采用，所以以这段实际必要core隔离公式、可靠性与稳定性保证即可；不把未查实现当必须遍历所有附件的普通阻塞。未来采用objective/实现/生产结论时，才定点恢复实际loss、reference/采样条件与独立评价，不用七篇普通日期held实验“陪读”。

## 来源日期与停止范围的独立核验

| 来源 | 实际独读依据 / 裁决范围 |
| --- | --- |
| SRC-OPENAI | XML解析 `openai-rss.xml` 确有1251 item，Nov26 Mixpanel与Dec1五条邻接，无Nov30 item；仅Feed切片，不等机构全论文。Mixpanel旧Nov26安全事件不移窗。 |
| SRC-ANTHROPIC | `anthropic-research.html`的publishedOn字段为Nov25/Dec1/Dec2邻接；与illustration _createdAt分离。SCONE旧身份/日期隔离冻结，不借新口径归日。 |
| SRC-GOOGLE-AI | `deepmind-page3.html`首页30卡与总265如必修项；[Google 2025 Blog](https://research.google/blog/2025/)本轮独立web L190–209含Dec3→Nov21、至Nov12、1/9页，支持此目录切片而非全部pubs。pubs年入口作者curl失败，本复核web也不可达，缺口继续保留，不认证全年论文。 |
| SRC-META-AI | [真实page4](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=4)独立web L42–158确认Dec16/Dec12/Dec1→Nov19/18/11/10段；页中另有2021/2020旧项混排，不能把参数或单页当全量召回。AdvancedIF旧身份不重归。 |
| SRC-QWEN | 结构化解析 `qwen-articles.json` data.articles40项及extra.date，`qwen-research-list.json`60项及date；path/id交集7、并集93。按+08日期Nov13→Dec5，无目标日；例如qwen3-tts-1128题名/路径不是Nov28发布日，其date是Dec5。部署969确有article/retrieval与research配置入口，research代码按date排序。当前这两个数据流切片可用，不认证所有release/论文或93篇题摘已审。 |
| SRC-DEEPSEEK | `deepseek-news.html` Research可见Dec2 V3.2/Nov27 Math-V2；News嵌入Dec1/Sep29。`deepseek-release-web.html`的published_time/frontmatter与 `deepseek-dec1.html` API Docs Dec1一致；是release事件，不强加给旧论文首公开。另 `deepseek-research.html`实际404，未作为该成功目录依据。 |
| SRC-MOONSHOT | `kimi-blog.html` Overview与 `kimi-changelog.html`的最新Nov7/Nov6及2024下界实读；无目标日目录项，不等全机构论文。pricing误恢复不计研究覆盖。 |
| SRC-TENCENT-HUNYUAN | JSON解析 `hunyuan-list.json` total9/list9，displayPublishTime全2026；不是November历史无事件。GameCraft-2 v1及项目页身份定点读，项目正文未给具名首次公开日。没有实际独读浏览器UI，不认证作者timeout为目录为空。 |
| SRC-ZAI | `zai.html`/`zai-page2.html`可见日期至Dec7与没有更多；`zai-release.html`导航日期Dec8/Sep30间无目标日。这不认证历史Research All，目录保留November缺口成立，不用企业新闻替代。 |
| SRC-BYTEDANCE-SEED | JSON实际type1 US18/total94、type2 15/total49、next20/has_more=true；逐项核PublishDate与IsPinned，pin的Dec2 GR-RL及Blog Nov27/非pin Oct23等跨窗。只支持该响应跨窗段停止，未核剩余页；缺list的105B原响应不等零论文。 |
| SRC-BAIDU-ERNIE | `ernie-page1.html`/`ernie-page2.html`日期段Dec9→Nov21，第二页Nov11/Nov7至Jun30及2页终止，支持Blog有限范围；模型名字1103/1120不替代目录公开日期。 |
| SRC-XIAOMI-MIMO | `mimo.html`实际Paper8与Blog15身份，包含More之前的全部15条；`mimo-routes.js`各route frontmatter HSS Dec19、Safety Dec18，Flash route无date；`mimo-blog.html`Flash正文Dec16确实可用。保留未日期化route与历史完整性缺口，不借邻route日期、不泛读2026纠错正文。没有独立执行More UI交互或验证全部后端，因此15条已保存不授不存在其他历史路由。 |
| SRC-MINIMAX | `minimax.html`/`minimax-zh.html`中Dec23 M2.1→Oct27 M2及中文Jan15旧项实读；仅这些目录段，不对未触发AgentTech或全仓库发布签无遗漏。 |
| SRC-ARXIV | `arxiv-sameday.html`真表单错误；`arxiv-advanced.html`1–50/3481只公告月，未翻尾页。正确catchup原form与两天拒绝原件确实past90days；Atom是api/errors的Error条目，不把totalResults1计论文。月首25从00010、月末25从21398到23473且cross-list，不能当11-30日批次。支持八身份恢复/撤回处理，不认证12分类日级完整。 |

作者README API替代独核：`video-com-readme-api.json`当前release文字无日；`theta-readme-api.json`无具名首公开日；`vgt-readme-api.json` News为Nov19结果、Dec1脚本、Dec26训练代码，各事件不同，不能组合推导Nov30首正文。GameCraft项目copyright/无日文本同样不授first-public。正确catchup的90日限制是有证据的外部边界，不是提交缺时分秒。

## 分层普通负侧样本与未检查范围

本轮没有新增确定当窗候选，普通负侧主要是窗口外目录事件/名字误作日期风险。本复核定点抽9个身份、覆盖8源：OpenAI Mixpanel Nov26；Qwen DeepResearch Nov13及qwen3-tts-1128 Dec5；DeepSeek V3.2 release Dec1；Meta AdvancedIF目录Dec1；Seed GR-RL目录Dec2；ERNIE-5.0-Preview-1103目录Dec9；MiMo Flash正文Dec16；MiniMax M2.1目录Dec23。这里只验各实际事件字段/重复边界，未把这些日期自动授论文首次公开，更未审全部正文。没有发现以负面/局部结果或Books主题覆盖为共同关闭理由；没有扩大成全年队列。

尚未独核作者13源所有搜索的完整响应、所有原始HTTP状态/请求头、93项Qwen及其他目录的全部正文、Google pubs全年、其他arXiv月份/12分类完整日公告、七项普通潜力的方法/实验、Super实验/实现/附录、旧21潜力全文或Books现正文及写后差额。作者陈述的curl status/时间与本次原件正文角色分开；web工具恢复是本复核实际观察，不假冒独立curl原件。未扫描周级来源。

## 准确恢复停点

1. 作者先修DeepMind“第3页”及总数/本页范围描述；已有Nov30两侧真实首页日期段可复用，不需扩目录。
2. 八项窄潜在准入、CourseTimeQA与2511.00115撤回排除、本文件Super公式反侧可复用；不因未知公开日改判贡献关闭，不为unknown date展开八方法。当前没有支持Books采用的新增命题，不能自签已有覆盖/整合。
3. 新日期保留项请求仍为八个具名官方历史日公告或可核作者首正文公开，Hunyuan/Z.ai November历史目录、MiMo未日期化route的直接日期/历史目录及Google pubs可用响应。不是Qwen/DeepSeek已恢复邻接段，也不是缺提交秒。到达只定点恢复受影响身份。
4. 本轮首校准已由非作者实际完成，但普通必要修正与最终日级验收尚未闭合。修复后可作必要的定点final-review，不把本文件提升为完整年度、14源Coverage/Evidence或Books Gate通过。

独立机械检查：2026-10-07T15:56+08实际运行 `python3 scripts/validate_research.py --report papers/2025/12/01/README.md`，退出0、1份V3通过；限定本文件 `git diff --check`退出0（新untracked文件另以文本检查），本文件local Markdown links及行尾空白检查通过。结果只支持格式，不替代上述实际校准与边界。写后仍观察到README L27及作者来源行的“第3页”描述，普通必修尚未闭合，未写final-review或日级通过。

## 修后定点确认（16:24:46 +08:00）

非作者仍为Sartre，ID不变。按用户“08-01作者修正后，仅核Avicenna修后文件差异”授权切回，重读主AGENTS/当前合同/Prompt/每日源与arXiv说明/ROADMAP及本日停点。只检查本日README与作者补查的实际未暂存diff中受影响来源、首校准回应、[Google恢复观察](supplement-20261007/google-directory-recovery-1612.md)，并定点解析原`deepmind-page3.html`。八项未变化v1题摘、两撤回及Super必要公式隔离复用前文，不重读七篇普通方法，不扩大其他日期。

**DeepMind普通必修：通过这一项修正。** 当前README来源行与作者来源行/16:02回应均已明确`?page=3`实际首页，不再把它称真第3页。独立标准HTMLParser再次得到两canonical均为首页、Previous隐藏且href `#`、Next为`/research/publications/page/2/`；`list-group__date`恰30个，首Sep16 2026，末三卡Dec3/Nov21/Nov4 2025。265仍为目录总数，不是已读数。原件未由本复核者改写；本次其SHA256为`9582ab3dd1a39357d6c624ec6e2e381915632971881f629f43bce0342b0ba5a1`，仅作这次只读身份记录，不声称首轮已采同指纹。

本日新独立web回[官方首页](https://deepmind.google/research/publications/)（149行）实际再核L117总265及L145～148的Dec3/Nov21/Nov4、下一page2。该目录自己说明是selection，故允许保留Nov30邻接段观察，但不授全机构无事件。未请求与本窗无关的page2/3/9，不借root其他日期页或08-01原件授12-01覆盖。前文真page3观察只用于首轮辨伪，不重新计作本窗扫描。

**Google默认页边界差额：支持作者更正，不授过滤/完整恢复。** 新独立web打开[pubs默认页](https://research.google/pubs/)成功（本次662行，而作者较早710行，不沿用其行数）；实际L125为2025选项678、L380为1–15/11597。支持撤销“默认pubs不可达”，不把facet当已生效年筛选或日公开。本复核不重跑作者curl/CUA/年参数/两个补检，故其timeout、无浏览器及Empty search results只保留为作者执行事实，不自称独立复现。也未完成可操作年筛选、限定主题历史切片或具名首公开恢复，不据本次成功首页宣称这些普通来源工作已经全穷尽；年度数量不应扩成678题摘队列。

**准确验收停点：** 唯一首轮普通描述必修已落实并定点独立确认；新来源恢复观察的可支持范围如上。八项潜力仍无目标Nov30官方日公开证据，不评分、不正面采用、不Books；两项撤回与Super公式/可靠性/稳定性隔离不变。没有新增贡献关闭，不改旧候选日期。其余14源完整查询、Google目标日历史切片、七项普通方法/评价、Super实验/代码、旧21潜力与Books正文/写后差额未在本次检查。允许保留安全隔离checkpoint，**不授12-01全日最终通过，更不授完整年度或全源通过**；不将“本必修清零”写成所有普通工作清零。

机械边界：16:24:46+08时钟检查后实际运行当前CLI，1份V3通过；限定README/作者记录`git diff --check`退出0。只读检查时主工作区已存在本日staged与unstaged并发修改，原样保留，不撤销、不续stage。本次仅追加本首复核文件；未写Report/作者原件/Books/State/合同/索引，未stage/commit/push。机械结果不替代本段窄语义确认。
