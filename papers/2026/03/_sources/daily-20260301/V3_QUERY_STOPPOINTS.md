# 2026-03-01 V3 查询与停止点

检查时间：2026-10-01 19:50～20:02 +08:00。作者：mar01_v3。
仅窗口 `2026-02-28T09:00:00+08:00`～`2026-03-01T09:00:00+08:00`。14每日源均到期，无旧 EffectiveDate 豁免；无 Weekly 依赖。当前版本 AGENTS/RESEARCH_CONTRACT/RESEARCH_SOURCES每日与arXiv主题/REPORT_CONTRACTS/CODEX_RESEARCH_PROMPT/ROADMAP与本日旧停点实际重读。

## 实际搜索范围

- 首轮：官方域 + `February 28, 2026` / `March 1, 2026`；中文源使用 `2026-02-28` / `2026-03-01`及斜杠日期变体。4源一批，仅一批结果，未访问搜索分页。OpenAI搜索误返community内容不作官方原始材料；其他无结果不作为零命中证明。
- 补检：OpenAI index、Anthropic research、DeepMind/Google Research、Meta research 域 + `after:2026-02-27 before:2026-03-02`。搜索日期过滤不可靠：结果仍含其他月份，不据此赋落窗日期。仅恢复官方公告与必要机构历史入口。
- 精确补检：`site:anthropic.com "Feb 28, 2026"`、`site:openai.com "February 28, 2026" -site:community.openai.com`、DeepMind February 2026模型目录。恢复OpenAI DoW原文、Google 2/19和2/26 model card以及2～3月博客page/3。
- 没有按固定关键词直接裁决贡献，没有全扫宽分类/全年目录题摘或全文。

原始网页/搜索响应在本目录 `V3_RAW_*.md`。它们保留实际链接与响应边界，不是语义完成收据；网页展示/搜索文本不能证明全部历史页可枚举。

## arXiv

官方 availability 实读 Announcement Schedule、无Friday/Saturday公告说明、2026 holiday表。窗口转换为 `2026-02-27 20:00 EST`～`2026-02-28 20:00 EST`；前后常规slot为2/26周四20:00 EST→2/27 09:00 BJT、3/1周日20:00 EST→3/2 09:00 BJT，均不在本窗。这里没有把DataCite registration或Submitted字段推定为精确first-public。

打开官方cs二/三月归档，仅返回首1～2000条（月表身份信息无日批次），立即停止，**没有把2000条转换成初筛队列或宣称月表完整**。主线主题对应CL/LG/AI/DC的LLM/Transformer/MoE/训练优化/Agent，及CV/RO生成模型/World Model/VLA、AR/PL/OS/PF kernel/runtime、IR/MA RAG/记忆/协作；常规窗口内没有批次可供上述主题列表浏览。

尝试官方 advanced announced_date_first 查询：all:`large language model`，from `2026-02-28` to `2026-03-01`，size50，order `-announced_date_first`，返回cache miss，停止首请求。此失败不证明零事件。特殊延期/非例行公告仍是历史批次限制；请求官方覆盖本窗的批次/公告记录或可核验status邮件恢复后，只重开本窗。没有候选需要PDF/正文；旧Atom只保留Submitted provenance，不用于落窗。

## 13机构实际入口与终点

| ID | 实际入口/停止点 | 可支持的有限结论/限制 |
| --- | --- | --- |
| SRC-OPENAI | research→index可见页末Load more；官方2/28 DoW正文与显式3/2 update已读 | 动态历史Load more未恢复；1具名潜在贡献日期隔离，不能零命中。 |
| SRC-ANTHROPIC | research可见首10项，See more仍返回同页；窗口域搜索首批 | 原研究页历史分页不能恢复；未取得可落窗材料，不能声称历史无研究。 |
| SRC-GOOGLE-AI | DeepMind research、publications page12、blog page3（二～三月相邻）；Google Research pubs可见年级2026列表 | blog相邻模型card是2/19/2/26窗外；publications page12实际仍返当前2026夏季，不是真历史cursor；Google Research年级日期不能落窗。历史论文子入口隔离。 |
| SRC-META-AI | research网页提取0行；窗口域搜索首批 | 空提取不代表0事件；历史research目录隔离。 |
| SRC-QWEN | qwenlm.github.io旧博客显示redirect；跟至qwen.ai/blog提取0行；日期域查询首批 | 新站动态历史目录不可恢复，旧博客停在2025不证明2026无事件。 |
| SRC-DEEPSEEK | 官网research导航，api-docs updates两次timeout；news恢复到API入门页 | 官网无日期历史表；updates历史入口隔离。不能把news入门页当发布历史。 |
| SRC-MOONSHOT | platform.kimi.com/blog可见全篇目录至2024；最高日期2025/11/07；日期域查询首批 | 此静态博客可见范围已读完，无本窗日期；2026研究/项目事件历史不在该表，隔离该范围，不把org updated-at当first-public。 |
| SRC-TENCENT-HUNYUAN | 官方research首查提取0行；日期域查询首批；CUA隐藏tab初建timeout、恢复getState/getTab成功后goto research再次timeout；随后root依官方脚本恢复publicList生产endpoint/renderType0,page1,size20，total11/返回11 | 全可见目录11/11已读；显示日期2/13→4/23跨过本窗，publishedAt和displayPublishTime原值均对读本窗；撤销D8受阻，browser失败仅保留过程。不外推历史删除项/全机构。原始依据：../V3_HUNYUAN_LIST_RECOVERY.md。 |
| SRC-ZAI | Research全部可见列表从2026/08/26读至2025/12/09；release notes读至2025/07/15 | 相邻2/21 GLM-5技术报告与3/15 GLM-5-Turbo（release表2/12→4/7）均窗外；可见本窗段已越过停止，不再展开旧条目。 |
| SRC-BYTEDANCE-SEED | research与public_papers首20项/Page1of13；日期域查询首批 | 首页研究表1/27→4/11不含本窗，但完整public_papers动态分页未恢复；不以首页声明全部论文无命中。 |
| SRC-BAIDU-ERNIE | 中文博客可见上段至2026/01/29；2/6 ERNIE5.0→4/15 ERNIEImage | 该官方博客窗口段已越过，无本窗条目；不声称全机构无遗漏。 |
| SRC-XIAOMI-MIMO | Paper列表全8项读至2025/05/12；Blog可见15项且More | Paper相邻2/3 HySparse→3/13 ARL-Tangram均窗外；Blog无日期/More历史未恢复，不以Paper代替Blog覆盖。 |
| SRC-MINIMAX | 英文blog与中文重定向minimax.cn/blog可见目录全部，至2025/01/15 | Forge英文2/14、中文2/12原值分别保留，均窗外；M2.7为3/18，窗口段已越过；不把公司财报列为研究。 |

## 首批校准与筛选边界

root已实读OpenAI原文，并同意1日期隔离与下列负侧理由；尚非日级验收。确定候选暂为0，日期隔离1。未继承旧9分/分母/Complete/旧审计抽样要求。

1. OpenAI DoW：不是仅凭Company标签排除；cloud-only+厂商控制安全栈/更新classifier+cleared人员可能改变责任边界，潜在准入成立；日期不足故隔离，不评分、不进Books。第3/2新增条款属于后续事件不能反填。
2. ZAI GLM-5技术报告：Research给2/21，非本窗，保留身份线索，不审窗外全文。
3. MiMo HySparse与ARL-Tangram：官方Paper分别2/3、3/13，非本窗，不以主题强相关破坏归属。
4. MiniMax Forge：英文2/14、中文2/12原值均明确窗外；不是因为RL主题已有Books而排除，不统一双语日期。
5. MiMo New Materials R&D：标题明确为材料研发应用，在ROADMAP暂缓AIforScience范围，未见当前事件纠错/安全/修订信号；范围退出，日期不穷追。
6. Google Gemini3.1 Pro / FlashImage card：原始官方页分别2/19与2/26；不能用只标February的博客列表移至2/28。

本日不声称原始命中总数/全年目录有效题摘总量；只有具名恢复材料用于范围与归属检查。潜在贡献仅1份官方无摘要公告，完整核心说明已读；没有确定候选的Evidence Review完成数为0，不能将其摘要筛选冒充证据审阅。
