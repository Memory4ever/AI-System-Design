# 2026-02-16 V3 — 来源与筛选依据

检查整理时间：2026-10-04T22:13:07+08:00。只处理北京时间 2026-02-15T09:00:00+08:00（含）至 2026-02-16T09:00:00+08:00（不含）；等价 UTC 02/15 01:00 至 02/16 01:00。本文件是本日过程证据，不继承旧 V2 Complete 或全月 audit。

## 查询与停止纪律

先查当前清单每日组的官方入口。机构检索以模型、训练、推理、多模态、Agent 机制为范围；辅助搜索仅恢复 02/15～02/16 线索，不以 search result 代替原源。不加载每周来源、Weekly 池或别日候选。相关宽目录仅浏览窗口附近 dated 标题，不把全年条目变成题摘/全文队列。本日未找到确认落窗的贡献候选，因此必要原源审阅与 Books 写入均为 0，不宣称所有材料全文已审。

官方正文/目录可直接复查；HTML 网络恢复均为 GET，15 秒超时。仅解析官方页面 date/publishedOn/pubDate 和窗口邻近条目，未执行网页脚本。Hunyuan 的 JS 仅用于识别目录为何不在 HTML，未进入需登录/写入接口。

## 十四每日来源

1. **SRC-OPENAI**：首查 [Research](https://openai.com/research/) → [Research Index](https://openai.com/research/index/)；动态首屏只到2026/09，不承担2月覆盖。恢复官方 [RSS](https://openai.com/news/rss.xml)，解析 item/pubDate，窗口内0 item。必要邻接字段为 `Fri, 13 Feb 2026 11:00:00 GMT`（theoretical physics）和 `Wed, 18 Feb 2026 00:00:00 GMT`（EVMbench）；本窗不跨到它们。读取一次完整返回后只取窗口/邻接 date，不把整份RSS变候选。日期 search `site:openai.com "February 15, 2026" OR "February 16, 2026"` 返回社区讨论，另 `site:openai.com/index after:2026-02-14 before:2026-02-17 research model` 未恢复本窗官方研究；社区讨论不代替研究来源。
2. **SRC-ANTHROPIC**：首查 [Research](https://www.anthropic.com/research)。web首屏10个当前条目、See more未恢复历史，GET HTML中的官方 `publishedOn` 切片补足日期：`zero-days:2026-02-05T00:00:00.000Z`，`india-brief-economic-index:2026-02-16T01:38:00.000Z`，`measuring-agent-autonomy:2026-02-18T15:10:00.000Z`。India条目=本窗终点后38分钟且是Economics，不列候选。辅助查询精确15/16和 after/before 两种，未发现其他当窗机制材料。停止于本页公开的2月切片，不保证未列出的历史全部可恢复。
3. **SRC-GOOGLE-AI**：首查 [DeepMind Research](https://deepmind.google/research/)、[Google Publications](https://research.google/pubs/)，再沿官方链接至 [DeepMind Blog](https://deepmind.google/blog/) 和 [Google Research Blog](https://research.google/blog/)。所取HTML/首屏为当前条目，Google Publications 只有年份/主题入口；不能恢复精确本窗的历史列表。查询 `site:deepmind.google "February 15" "2026" OR "February 16"`、`site:research.google "February 15, 2026" OR "February 16, 2026"`、两个blog的 after:2026-02-14 before:2026-02-17、以及各自 `2026-02-15 OR 2026-02-16` / February 2026，均未确认本窗相关公开事件。停于返回入口和有限搜索；历史日期切片为终态保留项G-GOOGLE，不以未命中证明0研究。
4. **SRC-META-AI**：首查 [Research](https://ai.meta.com/research/) 返回0行，搜索恢复官方 [Publications page=3](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=3) 和 [Blog page=2](https://ai.meta.com/blog/?page=2)，打开核 dated 区段。论文邻接：02/27 v-Sonar、02/26 personalized agents、02/13 FERRET、02/11 UniT；本窗无条目。Blog所见邻接为03/11 MTIA、02/09 DINO领域应用。页内排序后又回到较旧条目，明确不把页码当连续历史完整保证；不读窗外原论文/旧全文。未恢复片段为G-META。
5. **SRC-QWEN**：首查 [旧官方博客](https://qwenlm.github.io/) 明示迁移到 [qwen.ai](https://qwen.ai/blog)，旧页截止2025/09，后者动态返回0可读行，GET HTML未得日期列表。具体 [Qwen3.5仓库](https://github.com/QwenLM/Qwen3.5) 已重定向Qwen3.8，当前News仍明确保存 `2026-02-16` 的Qwen3.5首次发布与后续02/24/03/02；沿其中 [release blog](https://qwen.ai/blog?id=qwen3.5) 仍0行。日字段无时区/时刻，不能证明02/16 09:00前；`qwen3.5-plus-2026-02-15`第三方model variant标签更不能替代首公开。隔离G-QWEN，不拿3.8正文反推3.5机制，不扩查整仓历史。
6. **SRC-DEEPSEEK**：首查 [官网](https://www.deepseek.com/)，官方Docs news在web层超时；GET恢复 [news](https://api-docs.deepseek.com/news)，沿其中已公开 [updates](https://api-docs.deepseek.com/updates) 读取 Change Log 的日期/标题。现有相邻官方日期为2025-12-01 V3.2与2026-04-24 V4，未列本窗事件；停止在此日期间隔，不将整页所有release审成队列。辅助严格官方domain日期query只出现第三方同名项目，排除其来源权限。不把API changelog声称为所有研究论文的完备历史，未归档研究片段保留G-DEEPSEEK。
7. **SRC-MOONSHOT**：首查 [Kimi Platform Blog](https://platform.kimi.com/blog) 当前页面26标题，日期到2025/11及更旧；看 [MoonshotAI](https://github.com/MoonshotAI) 与具体 [Kimi-K2.5](https://github.com/MoonshotAI/Kimi-K2.5) 公共README，未恢复本窗带时区发布/重要修订记录。query `site:platform.kimi.com/blog OR site:moonshot.ai "2026-02-15" OR "2026-02-16"` 未有本窗官方研究。未读26篇旧正文；平台博客历史2月片段为G-KIMI。
8. **SRC-TENCENT-HUNYUAN**：首查 [Research](https://hunyuan.tencent.com/research) web0行，官方GET为SPA壳。按清单浏览器核查：首次隐藏标签创建超时；恢复state只有about:blank；绑定后定点goto同页再超时，不能取得“全部”目录内容。读取该页公开JS识别目录壳，无可用历史文章数据；查看 [Tencent-Hunyuan](https://github.com/Tencent-Hunyuan) 与 [T1说明](https://github.com/Tencent/llm.hunyuan.T1) 均未恢复此窗事件。T1说明包含相对“今年2月中/3月初”，不绑定本日或2026。有限query未找到本窗原源。G-HUNYUAN保留，不记成全部目录已读或0研究，不遍历仓库/历年论文。
9. **SRC-ZAI**：首查 [Research全部](https://www.zhipuai.cn/zh/research) 并核 [官方 release notes](https://docs.z.ai/release-notes/new-released)。Research dated片段为02/21 GLM-5技术报告、02/11 GLM-5开源、02/02 GLM-OCR；release notes为04/07 GLM-5.1、02/12 GLM-5、02/03 GLM-OCR。两入口均无本窗条目。停止在相邻跨窗条目，不读其全文，不把中文Research与API release date差异合成新事件。
10. **SRC-BYTEDANCE-SEED**：首查 [Research](https://seed.bytedance.com/en/research) 与 [Publications](https://seed.bytedance.com/en/public_papers)，前者当前精选、后者当前首屏至五月，未恢复2月分页。有限相关日期query未得本窗条目；具体 [Seed2.0正文](https://seed.bytedance.com/en/blog/seed2-0-%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83) 及 [模型目录](https://seed.bytedance.com/en/seed_model_portfolio) 日期同为2026-02-14。02/16 Arena“as of”不是发布事件，不移入本窗。02/14日字段不披露时区，未恢复完全落本窗的首公开区间，本日不深审；不能据精选目录保证所有历史论文0，日期与余历史片段保留G-SEED。
11. **SRC-BAIDU-ERNIE**：首查 [技术博客](https://ernie.baidu.com/blog/zh/) 第1页，所见窗口邻接为04/15 ERNIE-Image与02/06 ERNIE5.0，随后01/29直至2025/11；页底虽有第2页入口，本日停止于已经跨过窗口的第1页，不打开旧分页。未见本窗事件；query `site:ernie.baidu.com "2026年2月15" OR "2026年2月16"` 无命中。0当窗候选，不声称所有仓库commit均审阅。
12. **SRC-XIAOMI-MIMO**：首查 [Paper/Blog](https://mimo.xiaomi.com/)；Paper窗口邻接03/13 ARL-Tangram、02/03 HySparse、01/08 MiMo-V2-Flash。Blog大部分无日期；浏览 [XiaomiMiMo](https://github.com/XiaomiMiMo) 公开目录、有限日期query未得本窗研究。论文dated区段没有本窗条目，但无日期Blog历史列表仍为G-MIMO；不把Paper切片外推成Blog无发布。
13. **SRC-MINIMAX**：首查 [英文Blog](https://www.minimax.io/blog) web Internal Error，搜索缓存/原文恢复；[中文Blog](https://www.minimaxi.com/blog) 重定向 [minimax.cn/blog](https://www.minimax.cn/blog)，GET日期区段在03/18后是02/12 Forge、02/12 M2.5。英文 [Forge原文](https://www.minimax.io/blog/forge-scalable-agent-rl-en-1779896141) date=2026-02-14，中文/英文时区与首公开边界不能由迁移URL后缀推得，保留G-FORGE。英文目录、[IR news](https://ir.minimax.io/news-events/new-releases) 也标02/14 Forge和02/12 M2.5；不证明当前文本就是历史首版。[Agent Tech Blog](https://agent.minimax.io/docs/techblog) 仅导航壳无可恢复文章列表，G-MINIMAX-AGENT。不因版本名或性能宣传收本日候选。
14. **SRC-ARXIV**：[官方 availability §Announcement Schedule](https://info.arxiv.org/help/availability.html#announcement-schedule) 当前明确无Friday/Saturday公告，Thursday20EST后下一次为Sunday20EST。此周日02/15 20:00EST=02/16 09:00 BJT，恰为不含终点；本窗没有常规公告批次。表还说明replacement/withdrawal/cross-list同announcement流程。无本窗批次则不把提交时间、DOI created映成公开；本日旧inventory0仅旁证，不恢复整月池。停止于公告表及当日窗口计算。独立作者提前向root发送此边界并获认可。

## 有限补检与贡献校准

辅助日期搜索结果不是正式候选池，不统计为当天raw身份。未发现本窗需要处理的官方撤回/纠错/重要修订信号；此句仅限上述实际入口，不是全站无安全事件保证。

- OpenAI community 的credit-vs-API、Assistants图片失败、单用户MCP调用失败：只供发现。前者产品计费意见；后两者未经官方诊断、无机制或对照，不足以改变长期模型/系统解释。未采用用户猜测为根因或保证；无评分/Books。
- 第三方 nanobot mirror 的02/15 provider OAuth接入与02/16 skill安装标题：单独属于既有模块集成，不足以证明新长期机制。打开 [HKUDS原仓库](https://github.com/HKUDS/nanobot) 当前README已不含该历史news，不能把镜像标题升级成已核exact旧版本或“无安全变化”证明。此线索不计入确认落窗家族，无需为明确不准入的集成理由追历史日期。
- Meta DINO forest/medical应用仅在领域套用现有视觉模型；题目已能确认当前暂缓范围/领域收益，不透过Evaluation引入AI for Science。其官方日期也在窗外，不审领域数据附件。
- Seed2.0的排行榜截至02/16、Qwen模型快照02/15字符串、Hunyuan T1相对“今年2月中”均不能替代新事件身份和时间。

首批准入/代表排除由root校准，回复认可以上边界并要求每日14源有限覆盖、Forge/Qwen只隔离而不扩旧日期。当前没有需评分/原源/Books审阅的确定家族；所有历史目录/日期保留项不支撑正面Evidence、Books、覆盖通过或零遗漏。

## 停点

作者已完成以上有限来源、明确排除与安全隔离；普通扫描/题摘/原源/Books待办0。root已实际读六部分及本文件、独立核OpenAI RSS/Anthropic精确publishedOn/arXiv公告表/智谱和ERNIE邻接，并通过独立整日语义验收；代表排除校准复用，不声称独立重抓十四源全部原页或全量排除验证。10个终态保留继续隔离，恢复条件见日报§5。本作者仅完成本日后结束，由root另分fresh下一日。无stage、commit、push。
