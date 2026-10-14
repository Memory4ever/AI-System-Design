# Daily Research — 2026-04-04

**规范：** V3
**窗口：** 2026-04-03T09:00:00+08:00 ～ 2026-04-04T09:00:00+08:00
**窗口说明：** 用户要求保留旧候选日期、评分和窗口，只补遗漏；旧 09 点窗口与原 0 候选不迁移。
**补充窗口：** 2026-04-03 ～ 2026-04-03
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-14T04:20:18+08:00
**原09点窗检查时间：** 2026-09-26T04:04:43+08:00
**补充检查时间：** 2026-10-14T04:20:18+08:00

## 1. 结论

本轮仅补 2026-04-03 完整自然日。该日包括美东周四晚公告的北京时间周五晨间批次，**不能用下面旧 09 点窗的 Fri/Sat 结论推出补窗零论文**。四主题API返回253槽/210去重发现身份，仅有限主题线索；35项正侧中17同v1已在04-03处理，不搬旧日期/评分。有界相关标题另确定16真新，补窗最终分母 **34家族＝24实际整合、3具体已有覆盖、6中心争议隔离、1关闭/仅报告**；普通来源/单项处置与实际Books POST均闭合，完整六部分独立DAY实际通过。24家族落实15唯一owner，不把章节数或两canonical refine当新增家族。系统增量主要在训练目标/状态/表示身份、有限预算的评分与路由、权重/规划物化及反馈控制边界；所有性能只限原protocol，未作完整实现核验、实验复现或生产认证，定点接口证据见§4。OpenAI Research、Google Publications、MiMo历史Blog与MiniMax历史TechBlog slice及十二项日期资格仍精确隔离，不支持“全源无遗漏”。[本轮停点](../_sources/daily-20260404/SUP_STOP_20261013.md)。

以下两段旧结论只针对原09点窗口：

截至本次检查，尚未确认本窗有值得进入 AI System 长期知识库的独立候选；**这不是 14 个来源已全部零命中的断言**。旧 V2.1 报告把 2026-04-04 的 DataCite DOI `created` 条目当作当日 arXiv 首发，后来又以该口径得出 `0`；两个方向都不能代替官方公告时间。arXiv [公告规则](https://info.arxiv.org/help/availability.html)明确周五、周六通常不公告：本窗在美东周五晚与周六早之间，没有常规新稿批次。旧 434 条 raw identity、51 个旧候选仍作为历史线索留在[原始材料](../_sources/daily-20260404/)，不作为本日 V3 命中或候选。

机构目录已找到若干跨窗停点；Google Research 的 4 月 3 日技术博客指回 2 月已公开的同一篇论文，当前看不出独立机制或评价合同增量，不能因博客日期重复计分。官方仓库的定点 release 检查亦未发现本窗事件；这不是穷举所有仓库提交。OpenAI、Meta 的历史研究目录和 Google Research Publications 的精确日停点仍不可得，须作为不支持“全源零命中”断言的来源限制隔离。其余可执行窗口检查和独立语义复核已结束；本日完成只表示可用证据处理到安全终态，不表示受阻目录已证实无命中。

## 2. 来源覆盖

### 补充自然日的实际入口与停止范围

以下是本轮对Apr3自然日的补查，不继承原09点窗的空档证明、组织仓库created统计或旧完成标签。官网目录只证明其可见条目，不穷举所有作者论文；arXiv有限主题与相关标题补检负责额外发现。来源限制逐项隔离，不进入零命中算术。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| `SRC-OPENAI` | 实际重开[Research](https://openai.com/research/)、[Research Index](https://openai.com/research/index/)，仅featured/最新8卡片至Sep10且Load more；[RSS](https://openai.com/news/rss.xml)完整1288项，Apr1–5投影仅Apr2 TBPN/价格与Apr1客户说明，非Apr3机制事件。[原件](../_sources/daily-20260404/SUP_OPENAI_RSS_20261014.xml)。 | 受阻 | News不是完整Research，未得到Apr3历史研究分页/日停点。此历史Research slice隔离；官网当日存档/原始公告到达再定点重开，不声称无遗漏。 |
| `SRC-ANTHROPIC` | [Research](https://www.anthropic.com/research)嵌入publishedOn列表实际读目标邻接，Apr2T10:56Z emotion concepts前后未列Apr3。[本轮HTML](../_sources/daily-20260404/SUP_ANTHROPIC_20261013.html)。 | 已检查 | 只可见Research索引，未列出的作者材料不可据此排除。 |
| `SRC-GOOGLE-AI` | [Apr博客归档](https://research.google/blog/2026/04/)九项全部日期/题名，Apr3 behavioral-dispositions为同Feb v1再说明；[DeepMind Publications](https://deepmind.google/research/publications/)page1实际29可见项，目标Apr22→Mar22、最旧Nov2025，止于已跨窗精选列表。 | 受阻 | [Google Research Publications](https://research.google/pubs/)只取得年/主题与首页条目，`year=2026`未得到精确日切片；2026计数409不是当日队列。隔离该历史日slice，恢复限可核日目录/当日原始正文；博客与DeepMind已得层不重做。 |
| `SRC-META-AI` | 官方[Publications results](https://ai.meta.com/results/?content_types%5B0%5D=publication)沿Next实际pages1–3：近期2026段Oct2→Jul17、Jul13→Apr16、Apr14→Jan2，目标Apr9→Mar26跨Apr3，止page3；[实际入口/页界](../_sources/daily-20260404/SUP_META_20261014.md)。 | 已检查 | 页尾legacy旧年混排不作全史有序停点，仅上述当前2026 catalog段。三curl raw失败不抹掉可得web结果；撤旧“Publications全受阻”作为补窗路由，不授未列作者论文零命中。 |
| `SRC-QWEN` | [动态接口](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)40项，extra.date有Apr2 Qwen3.6Plus/Mar30 Qwen3.5Omni；[静态目录](https://qwen.ai/api/page_config?code=research.research-list)60项，最晚Dec23’25，只作旧catalog补充。[动态](../_sources/daily-20260404/SUP_QWEN_20261013.json)/[静态](../_sources/daily-20260404/SUP_QWEN_STATIC_20261014.json)。 | 已检查 | 当前动态可见列表目标无Apr3，静态不授Apr3历史穷尽；catalog字段不是逐篇首发，不迁原09点组织created扫描为Apr3 release穷尽。 |
| `SRC-DEEPSEEK` | [官方研究/动态](https://www.deepseek.com/news/)本轮实际39行，Research Jun24→Feb25、News Apr24→Dec2025，目标段无Apr3索引，止可见首页。 | 已检查 | 限官网可见目录，不扫描普通commit或推所有研究不存在。 |
| `SRC-MOONSHOT` | [Kimi Platform Blog](https://platform.kimi.com/blog)26可见项，最新Nov7’25至May’24；既有可核[kimi-cli release](https://github.com/MoonshotAI/kimi-cli/releases)1.30 Apr2T14:40Z→1.31 Apr10有效事实复用，无Apr3该release。 | 已检查 | 新读官网+指定release身份层；旧43仓库created统计不作为自然日全组织事件证明。 |
| `SRC-TENCENT-HUNYUAN` | [Research](https://hunyuan.tencent.com/research)官方publicList POST `renderType=0,pageNum=1,pageSize=100`实际success，总9/list9，displayPublishTime Apr23→Feb13。[成功原件](../_sources/daily-20260404/SUP_HUNYUAN_RETRY_20261014.json)。 | 已检查 | 前次空响应作废，不等穷尽；本结论仅完整9项research catalog，非普通仓库全部活动。 |
| `SRC-ZAI` | 本轮实际[Research](https://www.zhipuai.cn/zh/research)15卡片至Dec2025，目标Apr7 GLM5.1→Apr1 GLM5VTurbo；[Release Notes](https://docs.z.ai/release-notes/new-released)Apr7→Feb12。[Research原件](../_sources/daily-20260404/SUP_ZAI_RESEARCH_20261014.html)。 | 已检查 | 采用显示发布日期，不拿CMS createdAt首发；可见catalog/release段不替代所有作者论文。 |
| `SRC-BYTEDANCE-SEED` | [论文](https://seed.bytedance.com/en/public_papers)官方API type1/count20/page40总246，实际18项、next60，目标Apr7→Mar31；[blog](https://seed.bytedance.com/en/research)type2/page0总95，实际15项、next20，Apr8→Mar31。分别[原件1](../_sources/daily-20260404/SUP_SEED_PAPERS_20261014.json)/[原件2](../_sources/daily-20260404/SUP_SEED_BLOG_20261014.json)。 | 已检查 | 已读完整实际slice跨Apr3，止page40/page0，不全246/95队列；CMS日期不等精确首发，若有当日原证仅定点资格核。 |
| `SRC-BAIDU-ERNIE` | [官方技术博客](https://ernie.baidu.com/blog/zh/)本轮完整可见首页，日期May9/Apr30/Apr15→Feb6，后页旧年无需扩读。 | 已检查 | 仅博客显示日期/条目，旧release已得身份层可复用，不授全仓库/作者穷尽。 |
| `SRC-XIAOMI-MIMO` | [官网](https://mimo.xiaomi.com/)实际Paper八项，Jun29→Mar13→Feb3跨Apr3；Blog十五题名及More均未显示历史日期。[HTML](../_sources/daily-20260404/SUP_MIMO_20261014.html)与其公开index JS定点尝试未得blog历史日元数据。 | 受阻 | Paper可见catalog层已检查；Blog Apr3历史日期slice隔离，不把无日期卡片作零命中。恢复只官方日期清单/已具名博客当日正文，不扩十五全文或全年历史。 |
| `SRC-MINIMAX` | [英文blog](https://www.minimax.io/blog)12卡片May26→Mar18；[中文blog](https://www.minimaxi.com/blog)13卡片Apr27→Mar18；[Agent索引](https://agent.minimax.io/docs/llms.txt)仅当前3tech标题，本轮curl成功取得[techblog.md](../_sources/daily-20260404/SUP_MINIMAX_TECHBLOG_20261014.md)，显示Oct8/Sep22/Sep19而非旧Apr27唯一项。 | 受阻 | 公司blog各目标段已查；当前tech索引不提供Apr3历史归档，隔离该历史slice，不继承旧唯一Apr27覆盖断言。恢复只当日官方存档/原始技术公告。 |
| `SRC-ARXIV` | 四[agent](../_sources/daily-20260404/SUP_QUERY_agent_20261013.xml)/[model](../_sources/daily-20260404/SUP_QUERY_model_20261013.xml)/[multi](../_sources/daily-20260404/SUP_QUERY_multi_20261013.xml)/[system](../_sources/daily-20260404/SUP_QUERY_system_20261013.xml)查询start0/max100全部58/86/43/66，253槽/210去重；query围绕Agent/RAG、模型优化、多模态/world/VLA、runtime/parallel/kernel/speculation。额外CL83/LG84仅月页ID01450–02447相关标题带，40相关指针扣旧8/已有query后32，非整月逐项队列。 | 已检查 | submittedDate Apr1T14Z–Apr2T18Z仅发现代理，不认证日；本日确定身份用tight正常最早Thu20ET+官方ID在Apr3注册上界合取，Updated仅旁证。候选独核通过；晚assignment十一与Vita日期资格隔离，见§5，不宣称全arXiv或全网召回。 |

### 原09点窗的历史来源表（仅保留原范围，不代补查）

> | 来源 | 检查范围与依据 | 结果 | 缺口 |
> | --- | --- | --- | --- |
> | `SRC-OPENAI` | [Research](https://openai.com/research/)、[Research Index](https://openai.com/research/index/)和可回溯的[官方 News RSS](https://openai.com/news/rss.xml)：RSS 2026-04-02 10:30 UTC 后无 04-03/04 项。 | 受阻 | News 不等于完整 Research；历史 Research 列表只见近期卡片，未取得本窗分页停点。待官方可读历史目录或当窗存档；不作零命中断言。 |
> | `SRC-ANTHROPIC` | [Research](https://www.anthropic.com/research) 页面嵌入的 `publishedOn` 邻近项为 `2026-04-02T10:56:00Z` 的 emotion concepts，早于本窗。 | 已检查 | 仅限当前官方 Research 可见索引，不替代未列出的作者论文。 |
> | `SRC-GOOGLE-AI` | [Google Research 4 月博客归档](https://research.google/blog/2026/04/)中 04-03 唯一邻近条目 [behavioral dispositions](https://research.google/blog/evaluating-alignment-of-behavioral-dispositions-in-llms/)；[DeepMind Publications](https://deepmind.google/research/publications/)精选目录跨过 04-03，04-25 前接 03-22。 | 受阻 | Google Research [Publications](https://research.google/pubs/)只提供年份/主题过滤，现有入口无法取得可靠本窗停点；博客日期没有时刻，不据日期本身证明落窗。恢复条件：官方精确日目录、当窗原始论文或归档。 |
> | `SRC-META-AI` | [Meta AI Blog](https://ai.meta.com/blog/)可见邻近 04-08 与 03-26；[Research](https://ai.meta.com/research/)文本为空，[Publications](https://ai.meta.com/results/?content_types%5B0%5D=publication)请求超时。 | 受阻 | Blog 不能替代 Research。需官方历史研究目录/存档，否则不作该源零命中断言。 |
> | `SRC-QWEN` | [官方动态接口](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US) 40 条与[研究静态目录](https://qwen.ai/api/page_config?code=research.research-list) 60 条，动态日期邻近 03-30、04-02 后无 04-03/04。[QwenLM 官方组织](https://github.com/QwenLM)按创建时间列出 58/58 个公开仓库，末项创建于 2023-08-03；定点查看 [Qwen3](https://github.com/QwenLM/Qwen3/releases)、[Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni/releases)、[Qwen-Image](https://github.com/QwenLM/Qwen-Image/releases)与[Qwen-Agent](https://github.com/QwenLM/Qwen-Agent/releases)，未见本窗模型/Agent 正式 release。 | 已检查 | 结论限官网列表、组织新仓库与上述定点 release；未遍历高频 CLI 工具版本或普通提交。 |
> | `SRC-DEEPSEEK` | [官方研究与动态](https://www.deepseek.com/news/)可见动态 04-24 前接 2025-12-01，研究索引 06-24 前接 02-25。 | 已检查 | 结论仅针对官网可见目录；普通仓库提交不作为研究事件。 |
> | `SRC-MOONSHOT` | [Kimi Platform Blog](https://platform.kimi.com/blog)当前最新 2025-11-07；[kimi-cli 官方 Releases](https://github.com/MoonshotAI/kimi-cli/releases)邻近 `1.30.0` 为 04-02T14:40:52Z、`1.31.0` 为 04-10，不在本窗；[MoonshotAI 官方组织](https://github.com/MoonshotAI)按创建时间列出 43/43 个仓库，末项创建于 2023-03-28，未见本窗新仓库。 | 已检查 | 结论限官网博客、定点 CLI release 和组织新仓库；不把组织全部历史 commit 当作日报。 |
> | `SRC-TENCENT-HUNYUAN` | [Research](https://hunyuan.tencent.com/research) 对应官方 [publicList](https://api.hunyuan.tencent.com/api/blog/publicList)，`renderType=0,pageNum=1,pageSize=100` 返回 9/9 条；日期从 04-23 直接到 02-13。[官方组织](https://github.com/Tencent-Hunyuan)按创建时间列出 83/83 个仓库，末项创建于 2024-05-10；[HunyuanVideo Releases](https://github.com/Tencent-Hunyuan/HunyuanVideo/releases)无邻近本窗 release。 | 已检查 | 限官网研究列表、组织新仓库及定点版本；不宣称未列出的作者论文绝不存在。 |
> | `SRC-ZAI` | [官方 Research](https://www.zhipuai.cn/zh/research)可见发布日期 04-01 后到 04-07；[官方发布说明](https://docs.z.ai/release-notes/new-released)邻近 04-07 与 02-12；[官方组织](https://github.com/zai-org)按创建时间列出 53/53 个仓库，末项创建于 2021-05-25；[GLM-5 Releases](https://github.com/zai-org/GLM-5/releases)无本窗 release。 | 已检查 | CMS `createdAt` 不能当公开日期；检查范围限上述入口与定点仓库。 |
> | `SRC-BYTEDANCE-SEED` | [官方论文目录](https://seed.bytedance.com/en/public_papers) 的公开列表 API `article_type=1,count=20,page_token=40`，总 242 条；该页日期由 04-08/07 跨至 03 月。[研究博客](https://seed.bytedance.com/en/research) 对应 `article_type=2` 首页 04-09 前接 04-01。[官方组织](https://github.com/ByteDance-Seed)按创建时间列出 63/63 个仓库，末项创建于 2024-04-19；[VeOmni Releases](https://github.com/ByteDance-Seed/VeOmni/releases)无本窗 release。 | 已检查 | 两种官网目录无本窗条目；不把日常 CI commit 计为研究，也不宣称所有历史仓库都已逐个审完。 |
> | `SRC-BAIDU-ERNIE` | [ERNIE 技术博客](https://ernie.baidu.com/blog/zh/) 从 04-15 接 02-06；[ERNIE Releases](https://github.com/PaddlePaddle/ERNIE/releases)无本窗 release。 | 已检查 | 限官网博客及指定仓库的正式 release。 |
> | `SRC-XIAOMI-MIMO` | [MiMo 官网](https://mimo.xiaomi.com/) Paper 列表 06-29 前接 03-13；[官方组织](https://github.com/XiaomiMiMo)按创建时间列出 18/18 个仓库，末项创建于 2025-04-26；[MiMo-V2-Flash Releases](https://github.com/XiaomiMiMo/MiMo-V2-Flash/releases)无本窗 release。 | 已检查 | 无日期的博客卡片不证明本窗事件；不把仓库普通提交当独立发布。 |
> | `SRC-MINIMAX` | [英文博客](https://www.minimax.io/blog)与[中文博客](https://www.minimaxi.com/blog)的相关日期跨 03-18→04-27；[Agent Tech Blog 索引](https://agent.minimax.io/docs/llms.txt)仅可见 04-27 文章。[官方组织](https://github.com/MiniMax-AI)按创建时间列出 35/35 个仓库，末项创建于 2025-01-14；[MiniMax-M1](https://github.com/MiniMax-AI/MiniMax-M1/releases)和[MiniMax-M2](https://github.com/MiniMax-AI/MiniMax-M2/releases)无本窗 release。 | 已检查 | 限官网目录、组织新仓库及定点模型 release；未遍历所有普通提交。 |
> | `SRC-ARXIV` | [官方公告规则](https://info.arxiv.org/help/availability.html)：新稿、替换与撤回通常在 Sun–Thu 美东 20:00 公告，无 Fri/Sat 公告；本窗对应该常规空档。 | 已检查 | 限于常规公告；旧 DOI-created 库不用于推断本窗新稿，若有特殊 deferred mailing/单篇可核反证，定点重开。 |

## 3. 候选与判断

下表审阅状态按合同枚举记录。5–6分先满足标准Source要求，拟整合者又围绕具体长期差额深入必要机制/反侧及owner；“深入完成”仅这份采用范围，不表示全篇证明/附件/实现复现。细节及限制在§4，不用状态标签扩大证据。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Novel Memory Forgetting Techniques](https://arxiv.org/abs/2604.02280v1) | 2026-04-03 | bounded memory/relevance forgetting对照无限保留；2+1+2=5 | 争议 | 暂缓：方法式已有Ch77具体覆盖不消除性能中心争议，不进Books；需自身配置/同协议可归属结果/真正消融 |
| [APEX](https://arxiv.org/abs/2604.02023v1) | 2026-04-03 | challenge-settle-consume治理spend/replay；2+2+2=6 | 争议 | 暂缓：不采用性能/通用security，不进Books；需一致原始人口/日志及必要expiry测试 |
| [Do We Need Bigger Models for Science? Task-Aware Retrieval with Small Language Models](https://arxiv.org/abs/2604.01965v1) | 2026-04-03 | 同base检索后citation与answer quality可反向，corpus支持不可由引用量替代；2+1+2=5 | 标准完成 | 已有覆盖：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)已实际承载citation/faithfulness/task success分账与支持充分性 |
| [Model-Based Reinforcement Learning for Control under Time-Varying Dynamics](https://arxiv.org/abs/2604.02260v1) | 2026-04-03 | GP统计方差与旧dynamics时间偏差分账，window丢数据代价；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)Imagined rollout两段；实际POST通过 |
| [When to ASK](https://arxiv.org/abs/2604.02226v1) | 2026-04-03 | policy entropy gate的consult/overwrite/benefit分账与shift退化alwaysconsult；2+2+2=6 | 深入完成 | 整合：`AGENT-PLANNING` [Ch79](../../../../books/part-07-agent/79-planning.md)cost-conditioned uncertainty后两段；实际POST通过 |
| [Neuro-RIT](https://arxiv.org/abs/2604.02194v1) | 2026-04-03 | attribution提出适配位置、neuron mask/整层更新/EOT训练分责；2+2+2=6 | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)GRACE后两段；实际POST通过 |
| [Optimizing RAG Rerankers with LLM Feedback via Reinforcement Learning](https://arxiv.org/abs/2604.02091v1) | 2026-04-03 | prefix reader反馈与pointwise scorer、reference-time baseline分账；2+2+2=6 | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)LURE后两段；实际POST通过 |
| [Towards Position-Robust Talent Recommendation via Large Language Models](https://arxiv.org/abs/2604.02200v1) | 2026-04-03 | candidateblock/localquerycoords/randomID适配与位置/ID偏差分離；2+2+2=6 | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)rerank开篇两段；实际POST通过 |
| [Homogenized Transformers](https://arxiv.org/abs/2604.01978v1) | 2026-04-03 | random-init Attention drift/commonnoise与jointscale、slowtransient条件；2+1+3=6 | 深入完成 | 整合：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md)联合shape后两段；实际POST通过 |
| [Do Emotions in Prompts Matter?](https://arxiv.org/abs/2604.02236v1) | 2026-04-03 | 静态情绪prefix平均弱/方向异质，offline finitearm与onlineRL分责；2+1+2=5 | 标准完成 | 已有覆盖：`AGENT-PROMPT` [Ch74](../../../../books/part-07-agent/74-prompt.md)实际模板/异质任务与feature-conditioned finitearm正文 |
| [Ouroboros](https://arxiv.org/abs/2604.02051v1) | 2026-04-03 | input-conditioned frozenSVD LoRA recursion与heldout反侧/causal接口资格；2+2+2=6 | 争议 | 暂缓：不采用LM能力恢复gain；需原实验绑定pool/labels接口、prefixinvariance与同协议heldout |
| [Apriel-Reasoner](https://arxiv.org/abs/2604.02007v1) | 2026-04-03 | completed-domain反馈与retained梯度mix分账、solverate条件长度reward及cap guard；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)DAPO后两段；实际POST通过 |
| [AA-SVD](https://arxiv.org/abs/2604.02119v1) | 2026-04-03 | original/shift/anchored重构参照及block joint refinement、thin factor与cache接口分责；2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)重构/Fisher链两段；实际POST通过 |
| [The Rank and Gradient Lost in Non-stationarity: Sample Weight Decay for Mitigating Plasticity Loss in Reinforcement Learning](https://arxiv.org/abs/2604.01913v1) | 2026-04-03 | age-replay改变样本目标而非optimizer记忆，局部稀释与target drift分账；2+1+3=6 | 深入完成 | 整合：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md)ARROW后两段；实际POST通过 |
| [Bayesian Elicitation with LLMs: Model Size Helps, Extra "Reasoning" Doesn't Always](https://arxiv.org/abs/2604.01896v1) | 2026-04-03 | raw可信区间undercoverage与更多effort非一致改校准、valid人口分账；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)实际概率/coverage/valid人口与预算正文 |
| [Adam's Law](https://arxiv.org/abs/2604.02176v1) | 2026-04-03 | paraphrase-frequency选择与条件样本反侧、频率操作接口资格；2+1+2=5 | 争议 | 暂缓：不采用频率law/常见表达因果；需方向/zero及可绑定同pair的选择接口 |
| [DDCL-INCRT](https://arxiv.org/abs/2604.01880v1) | 2026-04-03 | soft prototype loss/decomposition与residual-growth稳定前提；2+1+3=6 | 争议 | 暂缓：不采用anti-collapse/global Lyapunov保证；需相关loss/gradient/projection定义与受影响前提纠正 |
| [SAFE](https://arxiv.org/abs/2604.01993v1) | 2026-04-03 | learned原子type/diagnosis/guidance与有界逐步重生、runtime feedback与标签oracle分责；2+2+2=6 | 深入完成 | 整合：`AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md)solver分权后两段；实际POST通过 |
| [Soft MPCritic: Amortized Model Predictive Value Iteration](https://arxiv.org/abs/2604.01477v1) | 2026-04-03 | online/target共享规划与replay-shift warmstart的预算分责；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)rollout后两段；实际POST通过 |
| [Beyond Logit Adjustment: A Residual Decomposition Framework for Long-Tailed Reranking](https://arxiv.org/abs/2604.01506v1) | 2026-04-03 | covered shortlist排序及input/pair threshold不兼容；2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)localize/coverage后两段；实际POST通过 |
| [Thinking While Listening: Fast–Slow Recurrence for Long-Horizon Sequential Modeling](https://arxiv.org/abs/2604.01577v1) | 2026-04-03 | observation/latent更新双时钟与episodecarry，不等更多信息；2+1+2=5 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)RNN预算后两段；实际POST通过 |
| [Label Shift Estimation With Incremental Prior Update](https://arxiv.org/abs/2604.01651v1) | 2026-04-03 | batch hardprior/calibration/task效用分責与initial缺class反側；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)REPAIR后两段；实际POST通过 |
| [PRISM: Probability Reallocation with In-Span Masking for Knowledge-Sensitive Alignment](https://arxiv.org/abs/2604.01682v1) | 2026-04-03 | factual-risk complement辅助目标与CE分母/门分责；2+1+2=5 | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)概率门后两段；实际POST通过 |
| [Coupled Query-Key Dynamics for Attention](https://arxiv.org/abs/2604.01683v1) | 2026-04-03 | 同token Q/K评分前共享非线性更新与token/墙钟预算分开；2+1+2=5 | 深入完成 | 整合：`MODEL-SELF-ATTENTION` [Ch14](../../../../books/part-02-model/14-self-attention.md)条件分支开篇两段；实际POST通过 |
| [DDCL: Deep Dual Competitive Learning: A Differentiable End-to-End Framework for Unsupervised Prototype-Based Representation Learning](https://arxiv.org/abs/2604.01740v1) | 2026-04-03 | 正确simplex identity不推出implicit分离，稳定条件中心反例；2+1+3=6 | 争议 | 暂缓：不进Books，相关梯度/系数/空间与受影响定理资格定点重开；不继承01880反例 |
| [Taming CATS: Controllable Automatic Text Simplification through Instruction Fine-Tuning with Control Tokens](https://arxiv.org/abs/2604.01779v1) | 2026-04-03 | 数值target variation支持与属性误差/保义质量分账；2+1+2=5 | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)ConceptTokens后两段；实际POST通过 |
| [Learn by Surprise, Commit by Proof](https://arxiv.org/abs/2604.01951v1) | 2026-04-03 | surprise/选后数据/optimizer状态与验证人口分責；2+2+2=6 | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)知识更新后两段；实际POST通过 |
| [kNNProxy: Efficient Training-Free Proxy Alignment for Black-Box Zero-Shot LLM-Generated Text Detection](https://arxiv.org/abs/2604.02008v1) | 2026-04-03 | datastore改变离线proxy scoring law，不认证真实origin；2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)provenance sensor后两段；实际POST通过 |
| [Tracking the emergence of linguistic structure in self-supervised models learning from speech](https://arxiv.org/abs/2604.02043v1) | 2026-04-03 | SSL objective/target checkpoint/step/layer读出身份；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)ZeroSyl后两段；实际POST通过 |
| [Prosodic ABX: A Language-Agnostic Method for Measuring Prosodic Contrast in Speech Representations](https://arxiv.org/abs/2604.02102v1) | 2026-04-03 | 同phoneme不同prosody/跨speaker minimalpair暴露评价盲区；1+1+2=4 | 已关闭 | 仅报告：本轮只局部measurement extension，不采用完整距离recipe/能力排序或长期新机制 |
| [On the Role of Depth in the Expressivity of RNNs](https://arxiv.org/abs/2604.02201v1) | 2026-04-03 | fixed width/totalstate/parameters三预算下深度取舍；2+1+3=6 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)fixedstate预算后两段；实际POST通过 |
| [Universal Hypernetworks for Arbitrary Models](https://arxiv.org/abs/2604.02215v1) | 2026-04-03 | descriptor共享root生成权重、materialization与训练/资源分責；2+1+2=5 | 深入完成 | 整合：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md)参数化multiplier后两段；实际POST通过 |
| [No Single Best Model for Diversity: Learning a Router for Sample Diversity](https://arxiv.org/abs/2604.02319v1) | 2026-04-03 | quality-weighted unique集合utility与offline route标签身份；2+1+3=6 | 深入完成 | 整合：`PLATFORM-GATEWAY` [Ch62](../../../../books/part-06-ai-infrastructure/62-gateway.md)hardeligibility/SCX后两段；实际POST通过 |
| [Grounded Token Initialization for New Vocabulary in LMs for Generative Recommendation](https://arxiv.org/abs/2604.02324v1) | 2026-04-03 | newrows配对languagegrounding与tied权重/后续训练预算分责；2+1+2=5 | 深入完成 | 整合：`MODEL-EMBEDDING` [Ch12](../../../../books/part-02-model/12-embedding.md)migration后两段；实际POST通过 |

补窗34项公开日期均经exact-v1、正常最早公告slot和已赋予官方ID的Apr3上界合取，非单一Submitted/Updated/registered。首批与新增16题摘/必要日期/小集合旧表membership已reader实际核；后续版本不回填v1。明确范围/贡献负侧保筛选记录：EIC/Metasurface、专用MERC融合与MPI程序应用、PRCCF persona、taxonomy与tabular credit类比等分层样本已实际独核，不以“已有组合/局部实验”自动排除；02352 accuracy/energy反侧重开贡献后因日期未证隔离而非EX。

以下原0分母及Google说明只针对原09点窗，补窗新增不计入其零算术：

本窗可核来源的独立候选分母冻结为 **0**；三个受阻目录不进入零命中算术。唯一需说明的邻近研究是 [Google Research 04-03 博客](https://research.google/blog/evaluating-alignment-of-behavioral-dispositions-in-llms/)：它讨论 25 个模型的情境判断、人的共识分布与模型过度自信，但明确链接到 [arXiv:2602.11328v1](https://arxiv.org/abs/2602.11328v1)，官方版本页列出 2026-02-11 提交且无 4 月修订。博客目前未显示脱离该论文的新机制、纠错或独立评价合同，按 Source Family 只作跨来源再说明，不作为 04-04 新候选或评分；博客自身只有 04-03 日历日，没有核实到足以断言落在 09:00～09:00 窗口的时刻。

## 4. 证据与知识整合

当前没有经本窗日期、贡献与证据三层确认的候选，因此本窗 Books Decision 为 **No Change**，无书稿修改。这不是对三个受阻目录的负面证明；旧 V2.1 的 51 项 Books disposition 和 `Complete` 也未自动转为本日报结论。

### 同一v1重复核对（不新增候选或评分）

仅定点核[04-03已冻结候选表](../03/README.md#3-候选与判断)与本日已正侧身份：01535/01621/01840/01881/01985/02006/02047/02097/02113/02155/02174/02178/02230/02268/02288/02315/02322均同v1已处理，保其原日期/评分/唯一owner与有效Source/Books结果。先前DWDP/Goose本轮重复写入已仅撤作者新两段/本人末注，Ch52/Ch48旧有效机制保留，actual非writerrollbackPOST通过，不计本日新I。随后只在原canonical段窄澄清边界：[Ch52](../../../../books/part-05-inference-system/52-dynamo.md)补Table5–6减Prefill资源的TTFT反侧，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)补shape-kept宏平均+0.2%与parent reachability限定；原句保留、未另开机制节。reader必要Source/PRE和实际nonwriter POST已通过，本人末注状态实读，root窄锁释放。这是已有event的边界修正，不新增家族、评分或I。

### [Novel Memory Forgetting Techniques](https://arxiv.org/abs/2604.02280v1)

本窗新增5分。[精确v1](../_sources/daily-20260404/SUP_2604.02280v1.html)§III–VI/TablesII–V：TablesII/IV/V标prior reportedresults，TableIII的Ours仅以大于prior数字/“稳定”描述，无自身model/budget/样本运行及可归属同协议实验；§V-C ablation实际重述priorstudy。§III-G容量截断不证明任务性能或不振荡。[Ch77](../../../../books/part-07-agent/77-memory.md)实际正文已承载weighted relevance/tokenbudget/recency非真值，但不把此方法覆盖当作本论文性能实证。中心measurement/稳定主张争议隔离，不进Books、不授性能；仅在自身配置、同协议可归属结果与真正组件消融到达时定点重开。[实际独核](../_sources/daily-20260404/SUP_REVIEW_20261013.md)。

### [APEX](https://arxiv.org/abs/2604.02023v1)

本窗新增6分。[精确v1](../_sources/daily-20260404/SUP_2604.02023v1.html)III–VIII明示single-node SQLite事务、HMAC、spend与challenge-settle-consume、模拟UPI无真实bank，方法描述不能签发生产保证。IX-C各场景40+30+20+20+10+10=130，却报120/baseline与总360；TableIII共70 blocked，对应60/130=46.15% success，不是TableII的52.8%，scenario均时加权亦约265.74ms而非477。TTL300秒、sleep2秒且10次成功只测withinTTL，不支持expired rejection。作者/reader实际必要Source均核；中心measurement/安全评价资格争议隔离，不进Books、不采用性能/通用security。定点重开需一致request人口/rawlogs及拟采用expiry/replay边界的必要测试，不要求无关production附件。

### [Do We Need Bigger Models for Science? Task-Aware Retrieval with Small Language Models](https://arxiv.org/abs/2604.01965v1)

采用的是主线RAG反证，不是暂缓的科学应用：必要§3–4.2/T2–4在所列同一base下，RAG的judge quality可下降而citation非零；外来corpus的OS可低于Orig/Zero。正文fullFT“3B”与LoRAFT表注8B、Llama3.2/3.1版本不一，不采纯scale/FT因果，也不采routing/template收益归因。`AGENT-RAG` Ch76实际四人口、citation≠隐含使用、recall/relevance/citation/faithfulness/tasksuccess分账与支持充分性正文承载这一受限认识，故具体已有覆盖；reader实际Source/day/owner通过，无新写或POST需求。

### [Model-Based Reinforcement Learning for Control under Time-Varying Dynamics](https://arxiv.org/abs/2604.02260v1)

必要III/IV/V-C/VI–VIII把GP统计方差与旧dynamics的drift bias分开；kernel/RKHS、episodic noise/change budget是假设，不把完整regret或最优window迁给BNN。丢旧数据也增加估计方差，fixed/tuned horizon不是在线自适应最优；NN实验的exploration weight/soft reset、估计SAC optimum而非oracle等另限。`MULTIMODAL-WORLD-MODELS` Ch25 Imagined rollout原uncertainty段后补两段统计/时间偏差与window代价，旧chain保留，必要Source/PRE、实际非writerPOST及本人注同步已通过；未核实现、复现或控制安全。

### [When to ASK](https://arxiv.org/abs/2604.02226v1)

必要II–IV/TableI/B/C：MC dropout多次policy概率的UE＋UA是H(mean)，不是纯ensemble disagreement或OOD真值。trigger consult、最终是否overwrite与任务benefit分账；deterministic FrozenLake有限grid/episode/Optuna协议不等部署安全。same-size配置可退，downsize allTest IR100%是always-consult非选择性省费，OR定义count/IR维度不一致不照精确ratio。`AGENT-PLANNING` Ch79成本条件uncertainty后实际两段已POST，保费用、invalid fallback与任务反侧。

### [Neuro-RIT](https://arxiv.org/abs/2604.02194v1)

root实际必要§3–4/T1–4/A原证、作者/reader实际Ch76邻接复用：attribution提适配位置、mask与三层全FT共同artifact，unsupported EOT是训练行为非runtime硬门。mask与同三层无mask差额小、layer removal反侧、RankCoT bundle影响；A1 Table5 gold0/YES冲突不采用精确label定位或功能独占。`AGENT-RAG` Ch76 GRACE后两段分责已实际POST；不把单neuron定位写成因果解耦或拒答保证。[原证限定](../_sources/daily-20260404/SUP_ROOT_RAG_20261013.md)。

### [Optimizing RAG Rerankers with LLM Feedback via Reinforcement Learning](https://arxiv.org/abs/2604.02091v1)

root实际§3–4/T1–5及必要B/H/I：scorer一次pointwise打分，prefix采样时mask并重归一，不是重新set-conditioned打分；reader每prefix EM/F1/Hit与greedy初始pool同长度reference time baseline是不同职责。固定reference ratio不证明old-behavior PPO等价，也不授RL胜同反馈SFT/所有reader或全成本。`AGENT-RAG` Ch76 LURE后两段真实差额已POST，绑定reader、prefix reward和采样人口；原owner保留。[原证限定](../_sources/daily-20260404/SUP_ROOT_RAG_20261013.md)。

### [Towards Position-Robust Talent Recommendation via Large Language Models](https://arxiv.org/abs/2604.02200v1)

必要4.1–4.4/6.1/6.3–6.4/B：candidate blocks、特殊跨candidate path、local query坐标与randomID训练改变输入列表可见集，first-ID score不等ranking decode。受限ChatGLM3/InternLM、LoRA/列表长度与shuffle协议；RoPE附录包络不推出dot product单调，也不授全permutation不变、任意causal NTP或一般加速。`AGENT-RAG` Ch76 rerank开篇后两段接口/反侧已actualPOST；仅采用可改变推荐以外list rerank设计的局部接口，不搬领域指标作通用保证。

### [Homogenized Transformers](https://arxiv.org/abs/2604.01978v1)

实际v1§2.1–2.3全部main results：random-init attention-only encoder、iid heads/layers、球面norm/residual scale；L/η/H/variance/d joint scaling决定static/ODE/SDE分支，centered V attention drift0不取消Itô/common noise。overlap alignment不等pathwise同步，高β/high-d慢transient还须ALL-t密度/导数条件，不从初始化自动继承。不采用完整proof/rates、MLP remark、训练后或causal decoder外推。`MODEL-TRANSFORMER-LAYER` Ch17联合shape段后两段真实差额已POST。

### [Do Emotions in Prompts Matter?](https://arxiv.org/abs/2604.02236v1)

必要§2–5：六短情绪prefix在三backbones/六English benchmarks/temp0单轮平均弱且异质；offline六arm的reward-soft-target MLP不是online RL。static平均不是best fixed或neutral causal gain；human250中219valid，保人口与可用评价条件。`AGENT-PROMPT` Ch74实际模板/任务异质、feature-conditioned finitearm与feedback proxy正文覆盖限定结论，reader具体NC通过，不新写。

### [Ouroboros](https://arxiv.org/abs/2604.02051v1)

必要§3–6与官方current-main接口：controller对整序列hidden meanpool产生共用delta广播各token，teacher forcing的后位信息可反馈早位，causal Attention mask挡不住该旁路；未取得原实验绑定的prefix-only pooling/labels资格。current-main不冒充原实验commit。heldout12 mean loss5.961高于5.690、仅3/12胜；0.5B gate消融非3B、freeze coda原因无unfreeze控制。中心autoregressive收益资格隔离，不用Ch17已有causal原则当正面NC；定点重开仅原实验pool/shiftlabel、prefix invariance及同协议heldout。

### [Apriel-Reasoner](https://arxiv.org/abs/2604.02007v1)

必要§4–5/T1–3/B：warm-up后completed-domain反馈clip控制下一请求mix，但零优势筛组仍改变retained groups/tokens/gradients。DAP只调reward，correct为verifier R==1，按组solverate条件长度惩罚，wrong固定、截断full guard；不是改policy loss。15B/64H100/BF16＋FP32 head/G8/两training seeds/validation选点协议下，DAP比LP准却更长，部分domain/其他baseline反退，无controller独立归因或trace cognition证明。`TRAIN-GRPO` Ch33 DAPO后两段到达/优化人口和reward guard分责actualPOST通过；tokens不等墙钟/SLO。

### [AA-SVD](https://arxiv.org/abs/2604.02119v1)

必要§3–4/T5/A/B（localpartial由officialHTML定点补必要段）：WX→W'X、WX'→W'X'、WX→W'X'是不同重构参照；闭式条件与joint block factors/Norm付费refine不能称无训练函数等价。T5 original-input＋refine可优anchor，4.3最终称input-aware而Algorithm主张anchor，不归全部headline给anchor。Standard thin factors输出shape不变，不自动rank KV cache；B3ratio算术也不照录。`INFER-TENSORRT-LLM` Ch49原重构/Fisher链后两段actualPOST通过，保covariance采集/solve/refine成本与执行独立验收，未授净提速。

### [The Rank and Gradient Lost in Non-stationarity: Sample Weight Decay for Mitigating Plasticity Loss in Reinforcement Learning](https://arxiv.org/abs/2604.01913v1)

必要§3–7/B3：旧population驻点＋每h每episode追加的distribution新质量有局部1/k项，target drift另账；terminal fH+1=0不消所有h目标变化。Eq4/B3 gradient与indices不一致不抄完整proof；正floor＋增长buffer仍累积旧mass，不授linear ageweight必消稀释，FIFO另算。五runs有限12tasks/UTD单Humanoid不授通用rank恢复，GraMa方向文字冲突不采指标因果。`TRAIN-PRETRAINING` Ch28 ARROW后两段age样本目标≠optimizer记忆、旧经验覆盖代价与有限反侧actualPOST通过。

### [Bayesian Elicitation with LLMs: Model Size Helps, Extra "Reasoning" Doesn't Always](https://arxiv.org/abs/2604.01896v1)

实际III–V400derived stats/四domains仅所列API tiers；raw95%区间undercoverage、增加effort不一致改校准。参数量未知、不同effort valid/invalid人口变化（低effort可emptybudget）不等纯scale/CoT因果。CP30/70要求exchangeability与稳定valid人口，ncal15的95%ceil规则越过有限校准数量，不授≥15可靠阈值/完整recipe；search数量口径不齐不授检索损伤内部knowledge。`PLATFORM-EVALUATION-SYSTEM` Ch66真实概率/coverage/valid population、预算与小样本推断正文足够，reader具体NC通过。

### [Adam's Law](https://arxiv.org/abs/2604.02176v1)

实际§3–5及必要limits/T2–6：Eq3 sfreq为词频乘积的inverse geometric mean、Eq2取argmax，而official wordfreq Zipf越大越常见，方向与“选常见表达”不一致，unseen0下inverse未定义。GPT4omini20paraphrases后极值/三人工同义筛选产生条件人口；长度/语义筛选等未全因果控制，多bin与FT反退不授单调law。reader独核定义/官方frequency接口，中心操作测量资格隔离，不EX或改分；重开只明确方向/zero/smoothing、同pair绑定与实际选择接口，不要求全代码新benchmark。

### [DDCL-INCRT](https://arxiv.org/abs/2604.01880v1)

实际§3.1–3.2中心定义：soft-distance期望声称等于nearest-prototype min＋q prototype variance；z0、p±1、qhalf时左1右2，不能沿此identity授global Lyapunov/anti-collapse。X n×d、M d×d形成n×n，而Pperp d×d夹乘，n≠d未定义，亦不自行猜token/feature投影。reader实际数学反例独核，中心稳定链隔离；仅恢复相关loss/centroid vsmin、gradient与projection空间及受影响前提，不以partial缺后proof当access blocker，不要求无关NLP实验。

### [SAFE](https://arxiv.org/abs/2604.01993v1)

必要§3–5/7/A5/A8学习(q,passages,prefix)→atomic error type/diagnosis/guidance，再有界逐步重生；runtime trained feedback不是formal KG oracle。gold十passages/过滤后每benchmark1000、同teacher标注与judge，人工150flagged precision非全recall。T4模型row与T3身份不一、训练人数总和冲突不采精确归因；retry>3可退、generator可不遵诊断，cache89%仅prefill tokens且各模型独立，不等全费。`AGENT-REFLECTION` Ch80原solver分权后两段是真实learned接口差额，actualPOST与本人note同步通过；不授严格grounded或生产能力。

### [Soft MPCritic: Amortized Model Predictive Value Iteration](https://arxiv.org/abs/2604.01477v1)

必要II–V/Alg1–2/Fig2–4/TI：online/target均使用one-step model ensemble＋terminalQ短MPPI，replay保存移位后的open-loop action sequence，后继状态target以此warmstart并回写。10seed DoubleInvertedPendulum的1warm/5cold可相近reward，同1iteration SPS几乎相同；速度取舍来自quality/迭代预算，不是warm算子免费。HopperH8仅模拟；epsilon均值/加u及基础identity口径不照录，不授约束/稳定性或完整hardware/dtype/netfee。`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)imagined rollout后两段明确可失效proposal与控制/目标一致性，Source/PRE与actual nonwriterPOST及本人note读回均通过。

### [Beyond Logit Adjustment: A Residual Decomposition Framework for Long-Tailed Reranking](https://arxiv.org/abs/2604.01506v1)

root实际v1§3–6/T1/G必要原证有效复用：deterministic shortlist覆盖是rerank上限，class offset＋input/rival项的分解中，input变化本身不证固定offset必败；同pair跨context不兼容threshold才限制class correction。冻结base、covered calibration、频率shrinkage只修改后处理；视觉pairwise差额小/frequent反退、RareBench仅32covered且额外HPO特征不由base读取，19.4不授LLM通用，五calibration subsamples非五base训练，4/5符号胜非显著保证。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)localize/coverage后两段承载具体排序条件，不搬疾病应用；actualPOST及本人note读回通过。

### [Thinking While Listening: Fast–Slow Recurrence for Long-Horizon Sequential Modeling](https://arxiv.org/abs/2604.01577v1)

采用v1而非currentv3。必要§3/5–6/C1–5：observation改写条件C，每观测有限T共享F更新latentX，episodecarry不每输入reset；obs与计算两个时钟不等新外部信息。maze/Dyck短训长测均有限，shared/nonshared改变参数与LR，LLM选bestOODseed而非平均，MiniGrid仅ours另调；T8→16可饱和、GH200未compile双loop慢于所列基线。不采energy/PCA内部推理因果、无限长/真实deadline。`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)RNN预算后两段定义carry/reset/读出接口与成本、旧递推/历史回退，actualPOST及本人note读回通过。

### [Label Shift Estimation With Incremental Prior Update](https://arxiv.org/abs/2604.01651v1)

root从localpartial恢复完整officialHTML并实际§4/Alg1/4.1–4.2/5，必要层复用：highconfidence硬预测初始化prior，有限batch按confidence逐次计hardlabels、prior-ratio归一后最终再跑全batch。成立前提labelshift/固定classconditional/support/calibration；排序ascending与descending口径未统一不授执行recipe。minimumrecall整体界不证highconfidence子集100%，sourceprior0/初始缺class/错误累积不可补造平滑方案。50Dirichlet target population非trainingseeds，weightMSE好不保证accuracy/macrorecall同向，未校准/TS可弱于RLLS。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)REPAIR后两段分责prior/calibration/效用，finitebatch非无state stream；actualPOST及本人note读回通过。

### [PRISM: Probability Reallocation with In-Span Masking for Knowledge-Sensitive Alignment](https://arxiv.org/abs/2604.01682v1)

必要v1§3–5/T2–3/A/B：factual-risk标签选择训练span，complement目标与普通CE不同分母，单hop风险不授多跳闭包；反事实keep gate检查重分配后target仍top1，不保证真实step/任意lambda。CE全valid与部分mask表口径不一不抄统一配方，parse通过非事实已证，common/factual平均不同向且强辅助可退。`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)概率门后两段明确辅助目标/门与真实优化分责、标签/额外loss/回归费用，原概率选择段保留；actualPOST及本人note读回通过。

### [Coupled Query-Key Dynamics for Attention](https://arxiv.org/abs/2604.01683v1)

必要v1§2–3.5/5/A–C：同token Q/K在评分前由共享f互相参与更新，leapfrog-like与Euler不同配方，不用v2invertible补采用。60M matchedcapacity/step消融支持局部，但microbatch更小/accum更大、throughput约.82及约2.4训练费，standard72K同墙钟PPL22.58可匹配。350Mcoupled仍优standard但Diff更好，OWT/MQARhard可退、GLUE无gain，domaincoherence是hypothesis。determinant1只volume，任意MLPf无potentialgradient条件，不授symplectic/Hamiltonian conservation。`MODEL-SELF-ATTENTION` [Ch14](../../../../books/part-02-model/14-self-attention.md)条件分支两段保传统attention与token/墙钟预算反侧；actualPOST及本人note读回通过。

### [DDCL: Deep Dual Competitive Learning: A Differentiable End-to-End Framework for Unsupervised Prototype-Based Representation Learning](https://arxiv.org/abs/2604.01740v1)

与01880不同：此稿simplex centroid reconstruction＋variance identity可成立。必要v1§4.1–4.4/5.1/5.3–5.4/5.6/A4/A6和附F：fixed z0、k2、p±ε/qhalf时Lq=ε²，gradientdescent收缩，与implicit separation及“decreases variance即增加spread”冲突。Main只λ>0，附F**已提出**λ>2ηbinom(k,2)并建议λ≥10η，不能说没有补条件；但pair bound缺2。取reduced P自由变量、N1/z0/qhalf、η1/λ2.5，满足main与附Fλ>2，E=(1−4+2.5)a²+γlog2=−.5a²+γlog2→−∞，因为||p1−p2||²=4a²>||P||²=2a²。此针对reduced theorem，不冒称实际DCL P=FᵀW该点可达，也不自补新定理。reader独核两反例后中心稳定资格隔离、不Books；重开仅相关gradient/detach q、系数/约束/空间及受影响前提，不要求全§6/代码。

### [Taming CATS: Controllable Automatic Text Simplification through Instruction Fine-Tuning with Control Tokens](https://arxiv.org/abs/2604.01779v1)

必要§3–9/T2–4/F/T7–9：reference-derived absolute readability/长度ratio作为条件字段，贡献是variation支持与target-output误差/quality/similarity分账，非发明prefix。句级compression近1 vs文档变化也伴随alignment/domain/length共变，mono过滤缩人口，不采唯一signal因果；MAE低不证human可读，rawscale不可平均，KS/JSD低不证source-disjoint/OOD。仅English1–14B，LoRA/两LR/512vs4096、单A10080GB与greedy重复非独立随机生成，MAE/LENS和mono方向均有反退。`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)ConceptTokens后两段是具体目标支持与保义分账差额；actualPOST及本人note读回通过。

### [Learn by Surprise, Commit by Proof](https://arxiv.org/abs/2604.01951v1)

只v1 LSCP，不采用v2 novel-fact数字。必要§2–4.4/4.8/6.1–6.2：surprisal不分novel/corrupt，单模型chain/selfconsistency非truth，19corrupt13过全链；选后训练包括QA、sourcewindow与失败strangeness，不能说全部训练通过chain。r1同optimizer仍185/186QA vs39raw及sameepochs不等token/update/curation，r.98小十题差额无显著独因果、r.9/邻接可退。β2为二阶矩非variance、原v-state继承未证，降β2不无条件更强learning。tag覆盖、store增长、并发/rollback/reference drift和生成检查费用均限。`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)知识更新后两段分责数据构造/optimizer状态/选后人口；actualPOST及本人note读回通过，不授biology/grokking。

### [kNNProxy: Efficient Training-Free Proxy Alignment for Black-Box Zero-Shot LLM-Generated Text Detection](https://arxiv.org/abs/2604.02008v1)

必要III–IV/V-A/C/D/E：fixedproxy prefix hidden检索context–nexttoken store，用加权onehot token distribution混合parametric，再供FastDetectGPT/Binoculars等离线统计。wholeinput median λ不是causal生成，bound依赖conditional-law Lipschitz和retrievedtoken独立，不由FAISS自动满足；keff/radius只受限surrogate。TIII baseproxy不同不全gain归alignment，knownfourtopic/router与closedfour-source归因不是真实origin，clipping与store规模/费用有反侧。有限攻击/单A6000、完整precision/seeds/netSLO未披露，不补造。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)provenance sensor后两段只测量law适配与authority边界；actualPOST及本人note读回通过。

### [Tracking the emergence of linguistic structure in self-supervised models learning from speech](https://arxiv.org/abs/2604.02043v1)

必要§3–5/A：六模型/两seed/三objective/831hDutch/16A10040GB，HuBERTI2targets来自I1T6，step/layer/target identity可改变probe最佳位置与时序。分析单maleheldout、自动forcealign/spacy、LDA/structprobe/Silhouette/RSA/ABX不同尺度；200K排不稳定seed，Fasttextsubword与homophone混杂。晚emergence依赖word是解释未控cause，多数probe饱和不等ASR停止获益。`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)ZeroSyl后两段补训练identity而非只冻结层选择；actualPOST及本人note读回通过，不复制Ch66整套probe。

### [Prosodic ABX: A Language-Agnostic Method for Measuring Prosodic Contrast in Speech Representations](https://arxiv.org/abs/2604.02102v1)

1+1+2=4最低关闭：exactv1完整题摘/日期/旧IDmembership及必要§2开篇实际核，同speaker同phoneme不同prosody的A/B、另speaker X针对phonetic ABX可能遗漏的prosody读出。未读完整距离recipe/所有实验，不能称标准Source完成或稳健语言能力。此只局部measurement extension说明，不改变本轮长期机制，关闭/仅报告；不是因样本或访问状态降分，不新Books/POST。

### [On the Role of Depth in the Expressivity of RNNs](https://arxiv.org/abs/2604.02201v1)

必要§2/3.1–3.3/4–5：fixed perlayer width增加totalstate、fixedtotalstate浅层latent更自由、fixedparameters部分memory深层更省是三预算，不一般moredepth更优。Theorem5针对depth-only nonlinear Eq2/有限widthdepth/任意长序列，不是普通Eq1 RNN/LSTM全无tracking；A10还要求homeomorphism，未采用全部theorem/proof。TinyShakespeare层数饱和/慢优化、S4fixedparams无清晰益、LRAretrieval非单调保留。`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)fixedstate预算后两段真实capacity/compute差额已POST，不授精确copy阈值/全S4排序。

### [Universal Hypernetworks for Arbitrary Models](https://arxiv.org/abs/2604.02215v1)

必要§3/4.1–4.5/5/H1：descriptor(index/component/layer shape/taskID)→shared scalar generator→materialize weights，taskloss更新root；fixedroot数不是执行state/生成费用免费。singlemodel各训，与joint六seen任务不同；unseen只是预定义family持出architecture，极深CNN失败、递归K1–3/MNIST/多任务干扰有退，Direct/HA常更好，BatchNorm runningstats不生成。4090AMPFP16/分类3与graph10seeds等所列protocol，不授任意task/大LM/无限递归/存储净压缩。`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md)multiplier后两段参数化共享root与物化分责；actualPOST及本人note读回通过，非Ch22 fastweights。

### [No Single Best Model for Diversity: Learning a Router for Sample Diversity](https://arxiv.org/abs/2604.02319v1)

必要§2–6/C/D/E/F/G/H1：quality-weighted semantic unique集合objective→有限suite perquery offline标签，贪心去重顺序/阈值与rewardjudge非truth。十八suite/B50/temp1/p1/max4096/noQwenthinking、700-100-200split/5routerseeds非独立generation；F1Ktrain口径不回填统一人数。specOOD39.3vs38.6不显著/lowfrequency39.6，prompt迁移route/oracle均退，All平均质量/后序可退。2H200 serialgen/1H200judge，spec比topone慢2–3x，candidateprefill/logging/训练label费用另计。`PLATFORM-GATEWAY` [Ch62](../../../../books/part-06-ai-infrastructure/62-gateway.md)hardeligibility/SCX后两段是集合utility和label身份真差额，不复制普通router；actualPOST及本人note读回通过，不授省总SLO。

### [Grounded Token Initialization for New Vocabulary in LMs for Generative Recommendation](https://arxiv.org/abs/2604.02324v1)

必要§2–4.3/6/7.2–7.4：newrows同mean初始无语言对齐，再pairedtext↔SID冻结骨干只新rows、然后下游训练。input/output tie同artifact，不能抄“head冻结但sharedE新row变化”为独立冻结配方。4.1额外8K冻结＋8K全模型＋SFT与A7.3QLoRA/10epoch不同，不统一recipe或pureinit/等预算归因；公共NDCG@5/其他cutoffs有反退，geometry非semanticproof。internal200jobs/同LLM相关性、Qwen.6B/4H100与SID构造/grounding费用绑定，完整dtype/seeds/SLO未披露。`MODEL-EMBEDDING` [Ch12](../../../../books/part-02-model/12-embedding.md)migration后两段词表rows/tying/训练预算分责；actualPOST及本人note读回通过。

## 5. 缺口与下一步

补窗尚可执行研究工作：无。34家族均达各自安全终态，独立完整六部分DAY已实际通过；六中心争议（02280/02023/02051/02176/01880/01740）的具体原证、冲突与恢复条件见§4，不进Books或正面Evidence。原两canonical refine不计新I。本窗完成表示可得材料及精确隔离达到安全终态，不代表这些主张/历史目录已被证明或全网无遗漏。

- 来源终态保留项：§2已精确隔离OpenAI Research Apr3历史分页、Google Publications历史日切片、MiMo Blog历史日期与MiniMax TechBlog历史索引；既有可得层已查、缺失层不作Coverage或零命中证明，不用于正面证据/Books/无遗漏断言。仅取得对应官方存档/日期清单或当日原始公告时重开受影响slice，不扩全年目录。
- 日期资格隔离，**不计34分母/评分/Source/Books**：晚assignment十一[02339](https://arxiv.org/abs/2604.02339v1)、[02340](https://arxiv.org/abs/2604.02340v1)、[02341](https://arxiv.org/abs/2604.02341v1)、[02343](https://arxiv.org/abs/2604.02343v1)、[02344](https://arxiv.org/abs/2604.02344v1)、[02345](https://arxiv.org/abs/2604.02345v1)、[02349](https://arxiv.org/abs/2604.02349v1)、[02350](https://arxiv.org/abs/2604.02350v1)、[02352](https://arxiv.org/abs/2604.02352v1)、[02353](https://arxiv.org/abs/2604.02353v1)、[02355](https://arxiv.org/abs/2604.02355v1)的v1提交在Feb/Mar、注册/Updatedv1在Apr6；MM04只给Apr2下界，后上界不能夹Apr3。各本日`SUP_<id>_doi.json`可查必要原值，完整题摘仅支持潜力；02352accuracy/energy反证潜力未被贡献EX。另[VitaTouch03322](https://arxiv.org/abs/2604.03322v1)原query线索/题摘有模态接口潜力，提交Apr2但ID注册/UpdatedApr7，project无更早历史日期，仅晚upper同样不足。恢复只官方实际批次公告或可核更早原文，不能以Submitted/registered单字段改公开日。
- 窗外恢复线索：[SWAY02423](https://arxiv.org/abs/2604.02423v1)/[SDTI02430](https://arxiv.org/abs/2604.02430v1)Apr2 cutoff后提交，正常最早Apr6，不进入本补窗必要审阅；只有具名更早公开原证出现才定点资格恢复，不混新日队列。

以下旧保留项说明仅属原09点窗历史状态；Meta当前补窗目录已恢复，不能沿用其旧受阻口径：

- 本窗尚可执行工作：无。已对 14 个到期来源逐项检查或精确隔离外部不可访问项；无可核入选候选需要 Source Review 或 Books 写入。
- 终态保留项（外部目录限制）：OpenAI Research 历史分页、Meta Research/Publications 与 Google Research Publications 的精确日目录当前不可完整读取。三项分别隔离，**不用于正面证据、Books 或无遗漏断言**，也不支撑“官方全源零命中”。定点重开条件：取得相应官方历史目录、可核官网存档或当窗原始公告链接后，仅重开受影响来源/材料，不重跑本窗已闭合项。
- 窗外原始数据：旧 `_sources/daily-20260404/` 的 434 条 DOI-created 身份和 51 项旧候选不能迁成本窗候选；如发现其中真正的官方公告日期属于相邻日，只在其真实归属日报处理，不要求为了本日零新稿逐篇重读其 PDF。

## 6. 复核

复核者：supp_apr04_reader（非本轮补充报告作者）
结论：通过

本轮完整六部分DAY已实际通过并持久记录于[独核§15](../_sources/daily-20260404/SUP_REVIEW_20261013.md)。四query/相关title带的实际停止、全部34确定家族与准入反侧、date gate/exactv1/旧17小集合去重、各必要证据及具体owner分批实际核。24实际整合均reader实际正文/完整局部邻接/本人note nonwriterPOST通过，作者note同步读回、root锁释放；3NC实际正文覆盖，6中心隔离非正面证据，1score4最低关闭非标准Source完成。误重复写rollback和两canonical refine实际POST通过，不新增分母。Qwen静态日期、Seed原字段与MiniMax英中目录口径已按reader实际读窄修，两个表新/旧范围明确，旧原0/窗口/连续§4保留；来源终态隔离不授“无遗漏”。独立validator/全部本地引用/原blob冻结及限定cached＋unstageddiffcheck通过，不代上述语义实读；完成字段随后由同一非作者实际FINAL回读确认。

独立负侧按来源/主题/理由实际核14身份：02259/01480/01766/01830/01944/02025/02035/02270/01916/02398/02061/01671/02348/02351，分别包含范围暂停、专用领域任务、无基础模型/系统新机制与类比不足；01965局部RAG反证与02352energy负侧按共同错误理由重开，不以成熟组合自动排除。其余明确范围外标题未由reader逐项完整题摘独审，不能把这14分层复核写成210或全部月目录验证。

作者机器/静态层：`python3 scripts/validate_research.py --report papers/2026/04/04/README.md`通过；本日Report/来源/实际Books限定`git diff --check`通过，全部本地链接存在。read-only对固定原blob `a40305f1a66d8329e6e993932e6812f7c3c58218:papers/2026/04/04/README.md`核原0、原窗口与连续原§4实际保留；34处置算术及15唯一整合owner一致。格式检查不替代以下实际日级语义验收。未stage/commit/push，不改已有index状态。

以下是原09点窗有效复核，不继承为本轮补窗验收：

复核者：主任务（非本日报作者）
结论：通过

独立重开 [arXiv 公告规则](https://info.arxiv.org/help/availability.html)，核对该北京时间窗口对应的 Fri/Sat 常规空档及延期例外；重开 [Google 04-03 博客](https://research.google/blog/evaluating-alignment-of-behavioral-dispositions-in-llms/) 与 [原论文版本页](https://arxiv.org/abs/2602.11328v1)，确认博客只给日历日、指向同一 Source Family，未见独立机制/纠错。逐行检查 14 来源实际入口、官方仓库定点 release 范围、旧 DOI-created 数据不继承、三个外部缺口各自的隔离和重开条件；没有把受阻项当零命中、把摘要当全文审阅，或用机器格式检查替代本次语义判断。
