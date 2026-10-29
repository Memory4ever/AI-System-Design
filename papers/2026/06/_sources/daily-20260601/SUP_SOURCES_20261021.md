# 2026-06-01 增量遗漏来源补查

本轮作者：`supp_jun01_author`。独立非报告作者 reader：`root`。启动检查时间：2026-10-21T16:05:28+08:00。

## 范围与冻结基线

本轮实际重读 AGENTS、Research 合同、Report V3、Sources 用法/每日14源/arXiv主题范围、CODEX_RESEARCH_PROMPT、ROADMAP 与 LEARNING_STATE 本日路由；只补 2026-05-31 北京时间完整自然日。没有继承其他日期材料池、筛选或覆盖结论。

启动实际 README 为旧1候选：MiniMax M3，原公开时间 `2026-06-01T01:31:18+08:00`，原评分 `3+3+2=8`；原窗口 `2026-05-31T09:00:00+08:00 ～ 2026-06-01T09:00:00+08:00`。运行前真实副本暂存 `/private/tmp/daily20260601-baseline-20261021.md`，旧候选完整行/顺序、窗口、连续原§4冻结。旧完成声明只表示旧轮结果。本轮不改索引、合同、脚本、State，不 stage/commit/push。

可复用旧证据：本日 `CURRENT_CONTRACT_DAILY_SOURCE_RECERT_20260914.md` 中 MiniMax exact事件与既有Books比较；其中多日“没有发现”不充当本轮自然日覆盖。旧 arXiv receipt 以 created 推公告的部分不采作当前日期证据，不展开其已迁出的40项全文队列。

## 当日发现与实际停止点

| 来源 | 实际入口、检查范围/停止点 | 当日结果与限制 |
| --- | --- | --- |
| SRC-OPENAI | `https://openai.com/news/rss.xml`，HTTP XML解析1303个当前条目，仅提取May31自然日与相邻边界；May29 Boston Children’s/Braintrust 等之后直至Jun01事件，May30/31无条目 | 该RSS现有历史切片未发现May31发布；不是全站无遗漏保证。论坛搜索命中只是用户功能建议/账单帖，不是官方Research。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)首查；其实际JS `/_next/static/chunks/04_9peblvyok2.js` 的 `listingPagesPath`/default segment恢复出 [page1](https://www.anthropic.com/listing/research/default/1)、[page2](https://www.anthropic.com/listing/research/default/2)。分别24条，page1 Oct20→Sep04，page2 Aug28→May22，已过May31窗口，停止page2；当前Research共203条不是本日分母 | 两页各24条只核title/date边界，May29～Jun02实际0。另用[Engineering](https://www.anthropic.com/engineering)（Oct13→May25）、Alignment（Jul08→May08）、Interpretability（Jul06→May07）、Economics（Jun16→Apr22）、Societal Impacts（Jun12→Apr30）、Frontier Red Team（Jun03→May22）有限边界补检，未见当窗身份；不展开别日正文。当前迁站内容仍无历史不可变快照保证。 |
| SRC-GOOGLE-AI | [DeepMind publications](https://deepmind.google/research/publications/)第1页完整30条，Jun04后为May28 Realistic honeypot/Gram；[Google Research May2026 archive](https://research.google/blog/2026/05/)四条May28/27/19/01，页面已到底、没有下一页。`https://research.google/pubs/?year=2026` HTTP两次25/20秒未取得正文；May31定点搜索未恢复其它必要身份 | 可见官方发布目录未见May31。Google Research年度论文目录历史slice受阻，未把timeout或搜索零命中认证为全覆盖；恢复条件是其May31公开事件列表或具名原稿。 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)及[publications](https://ai.meta.com/research/publications/)直接页面不可用；[results page2](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=2)、[page3 most_recent](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=3&sort_by=most_recent)搜索缓存显示May27→Jun05，实际open却变成Oct→July或2025，并夹杂2017～2021；HTTP20秒无正文。root接手有限恢复，实际page2 most_recent可读Jul17→Jun05→May27→May04后混入旧年 | root R4有限恢复已结束，仅认证可见片段无May31，不认证排序/完整历史。两个publication/blog May31定点查询无新身份不授零发布。取得当日原目录/官方研究页或有效有序分页才重开。指南具体EX见下表。 |
| SRC-QWEN | 官方 `GET /api/v2/article/retrieval?type=qwen_ai&language=en-US`，返回40 articles，逐条仅核日期/title；extra.date与content `article:published_time`分开 | May29 Qwen-VLA之后为Jun01 Qwen3.7-Plus；后者extra Jun01、content May21冲突，但两口径均不落May31，不迁入。未发现当窗身份；当前迁站目录不能保证隐藏历史。 |
| SRC-DEEPSEEK | [首页](https://www.deepseek.com/)首查→[Research/News](https://www.deepseek.com/news/)实际可见5条动态、10条研究索引；动态Apr24 V4 preview→Sep10 V4.1，研究Feb25 DualPath→Jun24 V4。两个“查看全部”是按钮而非可提取下一页链接；定点May31搜索未恢复具名当窗事件 | 当前官方日期/title切片无May31身份；未浏览别日论文正文。隐藏历史目录完整性不认证。误试的`api-docs.../updates`重定向成当前API入门，不算历史来源。 |
| SRC-MOONSHOT | [Kimi Platform Blog](https://platform.kimi.com/blog)静态列表止于Nov07 2025，不能认证2026；[kimi-code releases](https://github.com/MoonshotAI/kimi-code/releases)首查后，实际GitHub API `releases?per_page=10&page=8`、page9恢复共13个tag/date。page8 Jun09→May28，0.6.0=`2026-05-29T14:24:54Z`后下一0.7.0=`2026-06-02T02:23:53Z`；page9只3条到May26，停止 | May31无release身份，不读窗外notes。最初未压缩100项请求超时/JSON截断不用于结论；实际压缩10项响应完整可解析。平台Blog缺2026迁站前历史，不能授全源无遗漏。 |
| SRC-TENCENT-HUNYUAN | 官方 Research 对应 `POST https://api.hunyuan.tencent.com/api/blog/publicList`，body pageNum1/pageSize1000/renderType0，header accept-language zh；现有11条日期/title核边界 | May21 Hy-MT2之后为Jul06 Hy3；Hy3 preview公开字段publicAt Jul05、display Apr23都不在May31。没有当窗身份；当前目录不能证明迁站前无隐藏发布。 |
| SRC-ZAI | [官方Research](https://www.zhipuai.cn/zh/research)首查，HTTP1097227字节可解析“全部”可见15条日期/title，Jun16 GLM5.2→May20 ZCube→Apr29 Scaling Pain，已跨窗停止 | May31无可见身份；“查看更多”以下旧历史不展开，当前目录无不可变历史保证。 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)/[Papers](https://seed.bytedance.com/en/public_papers)的真实main JS暴露`/api/get_article_list_v2`，实际GET article_type1/2，count100/order_desc true/publish_year2026，header `x-tt-locale: US`。type1 page1实际18、total86、next20、May25→Sep28（含pinned），跟next20读page2实际20、next40、Apr14→May15，全部早于窗口后停止；type2 page1实际15、total20、has_more false/next空停止 | 日期/title边界中May29 Task-Focused Memorization与Jun03 MetaPoint相邻，没有May31身份。不把visible条数当容量/total，不因type1后页尚有更早条目扩扫全年。API目录PublishDate是目录日期，不证明论文首次公开。当前迁站目录不能认证隐藏历史。 |
| SRC-BAIDU-ERNIE | [中文技术Blog](https://ernie.baidu.com/blog/zh/)第1页10条，最新May09 5.1，次Apr30/Apr15，然后更早；已过窗，下一页2/2不展开 | May31无可见Blog身份；不把当前静态目录当删帖/迁站前历史保证。 |
| SRC-XIAOMI-MIMO | [主页Paper/Blog](https://mimo.xiaomi.com/)8个Paper标题/日期与可见Blog标题核边界；当前首页无Blog日期，通过实际JS `https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js` 的frontmatter恢复中英/blog/mimo-v2-5-inference date=`2026-05-30`，之后UltraSpeed Jun08、MiMo Code Jun10；Paper Mar13→Jun29 | 无May31具名身份；May30机制不因本轮发现迁入，亦不展开其正文/回写Books。未带日期的旧产品页没有迁站前发布序列保证。 |
| SRC-MINIMAX | [English Blog](https://www.minimax.io/blog)、[Chinese Blog](https://www.minimaxi.com/blog)日期/title边界May25 sparse-token→Jun01 M3；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)实际四条Sep19/Sep22/Oct08/Oct20、到底无下一页 | 可见目录无May31身份。旧M3精确事件继续保持原Jun01日期，root R3已实际核原JSON-LD/正文与Ch22具体已有覆盖；不把UTC May31误算BJT May31。 |
| SRC-ARXIV | [availability](https://info.arxiv.org/help/availability.html)纽约周五/周六不公告，与BJT May31常规0同日历门；cs.CL/LG/AI/DC May列表实际404/timeout，主题补搜只恢复两项Submitted-on-May31身份，详下 | 常规公告0，不从旧created receipt推公开日；列表/非常规历史公开保证保留，不授全Coverage。其它分类不建立整类逐项队列。 |

仅恢复日级到期14源；每周组未扫描，无当日会议或协议变更触发。搜索补检仅发现/日期身份，不作为贡献、首次公开或覆盖证据。

## arXiv 日期门与主题恢复

2026-05-31为北京时间周日，对应纽约周六至周日中午；[官方availability](https://info.arxiv.org/help/availability.html)明确纽约周五/周六不公告，周日20:00公告到北京时间Jun01，故May31无常规新稿/替换/交叉收录公告。此为日历约束，不是以Submitted/updated或ID目录月充当公开日。仍检查官方主题分类历史列表与当前必要状态，处理非标准日期信号，不把旧0 bucket当本轮已审。

`https://arxiv.org/list/cs.CL/2605?show=2000` HTTP返回8218字节错误正文而非实际日期列表；web直开CL/AI/DC为404，LG timeout。已执行限定`site:arxiv.org`+`2026-05-31`/`May 31, 2026`+Transformer/language model、GPU/inference/training、多模态/world model/agent的三组补搜；不用宽结果建立逐项队列。关注主题对应CL/LG（模型/训练）、DC/AI（并行/Agent）、CV/RO（基础多模态/行动）、AR/PL/OS/PF（LLM执行）、IR/MA（RAG/协作），当日无常规公告时不反向展开这些分类的全年列表。必要具名恢复如下。

## 准入与证据

当前确定新增候选0；首批无待准入正项，已向root提交以下来源/理由分层EX与日期边界作有限校准。root尚未签本轮DAY；不估计互联网候选总数。

| 身份与原始链接 | 实际读到/判断 | 本轮处置 |
| --- | --- | --- |
| [Meta How to create a portfolio website with AI](https://ai.meta.com/learn/ai-career/website-portfolio-with-ai/)（May31） | 官方完整核心是作品集定位、页面结构、内容/SEO提示与展示建议；没有新增基础模型、执行、训练/评价或可靠性机制。不是因为“官方产品”排除，而是内容不改变具体系统选择 | 明确EX，不评分，不读无关附件 |
| [OpenAI community bookmark request](https://community.openai.com/t/feature-suggestion-in-response-bookmark-reading-position-marker/1382135)；[automatic recharge support](https://community.openai.com/t/automatic-token-recharge-not-working/1364865/5)；[Turnfeed confirmations](https://community.openai.com/t/lessons-from-building-public-write-confirmations-for-a-chatgpt-social-app/1382164) | 实际读取的是web搜索返回主贴缓存，不是HTTP原件成功。首个是用户UI建议，第二个是个案支持转接；第三个仅取May31首帖六条read/write分责、精确文字/目标/可见性确认、client ID幂等与避免重复自然语言确认的成熟原则应用，未给具体新机制/比较或失效证据。非官方身份本身不是贡献排除理由；正文也不支持未公开实现 | 有限发现噪声/具体贡献EX；搜索缓存不支持厂商实现、实际首公开或覆盖正面断言，后续Aug/Oct内容不属于本窗。没把论坛全日扩成队列 |
| [arXiv:2606.01385v1 MAAD](https://arxiv.org/abs/2606.01385v1) | 实际完整题摘：四个角色+RAG注入标准+层次设计史记忆应用到软件架构，10案例对MetaGPT；题摘没有显示超出既有分工/检索/迭代的执行机制或成立边界。未见纠错/撤回信号。唯一v1提交`2026-05-31T18:18:31Z`按官方日程也不可能在May31常规公开 | 贡献EX，日期未核实也不为不影响处置另建请求；不把提交当公开 |
| [arXiv:2606.01215 APEIRIA](https://arxiv.org/abs/2606.01215) | 实际完整题摘与Submission history：v1=`2026-05-31T13:04:31Z`，v2 Jun29；神经符号3D程序模式→CoT-SFT→RL的贡献潜力未作负判，但唯一v1提交在Friday14:00～Monday14:00纽约桶，最早公告MondayJun01 20:00EDT＝Jun02 BJT。没有具体更早公开线索，不为排除假想渠道无界追踪 | 不是May31确定候选；只留下未来真实归属日定点恢复线索，不评分、不全文、不Books。最早界不是实际公告日期 |
| Qwen3.7-Plus / MiMo V2.5 inference / MiniMax M3 / Seed TaskMem | 四者有系统相关潜力，分别API日期冲突两端May21/Jun01、官方frontmatterMay30、原JSON-LDJun01 BJT、Seed目录May29；无一给出May31公开证据 | 日期边界非当窗，不因主题相关误收；不处理其真实归属日普通待办 |

## Books

本轮无新增家族可推进；未申请任何共享Books写位，Books新写0。root R3实际官方M3核心/HTTP JSON-LD datePublished=dateModified=`2026-05-31T17:31:18Z`，实际Ch22 selector→dense fallback完整局部与MSA精确v1末注，旧8分/NC层有效；不重读后续全稿或artifact，不把它迁入May31新增池。

## 复核与自检

root R2～R7已实际顺读消费：日历门、旧M3有效NC层、Meta/DeepSeek/MiniMax有限来源、Meta指南/MAAD/APEIRIA分层贡献/日期与论坛缓存权限校准，以及完整六部分DAY均实际通过。Meta有限恢复已结束，不再ordinary。普通扫描/题摘/证据/Books与日级复核待办0；README已按R7仅行政保存完成态，不重开Source或增设审计。本文件不自行授通过。

作者交DAY前实际自检：V3通过；报告/SUP的8个本地引用存在；启动真实副本与仓内baseline逐字节相同、旧1行/窗口不变、连续原§4为1219字节且原样包含；限定working与cached diff check均0。本日作者仅修改README、新增SUP及baseline，没有Books、index、State或其它日期写入。

R7之后仅行政同步完成态。首轮完成态V3要求§5显式使用“终态保留项”，已将既有来源保证隔离改为该准确措辞并明确“不支持正面证据、Books或无遗漏”与逐项重开条件，未改事实、候选、Source或Books判断；完成态V3及限定working/cached diff check重跑通过。连续原§4正文1192字节、含节标题1219字节，两个长度口径一致。
