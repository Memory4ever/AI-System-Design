# 2026-04-11 V3 重审记录

窗口：2026-04-10T09:00:00+08:00 ～ 2026-04-11T09:00:00+08:00。作者 apr02；实际访问日期 2026-09-26。旧稿保留于 [v2.1-report-before-v3.md](./v2.1-report-before-v3.md)，其 DOI-created owner 与完成结论不作为本次依据。

## 已执行来源停点（可复用未变化目录，不等于逐项全文）

- Qwen：`https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US` 动态40项，2025-11-13～2026-09-20；`https://qwen.ai/api/page_config?code=research.research-list` 静态60项，最晚2025-12-23。April动态邻界为04-02T04:00+08与04-15T10:00+08，本窗无条目；亦跨过Apr12。不是所有作者稿覆盖。
- Hunyuan：POST `https://api.hunyuan.tencent.com/api/blog/publicList`，`{"pageNum":1,"pageSize":100,"renderType":0}`，totalNum=9/list=9。displayPublishTime Unix秒，04-30、04-23之后直接02-13；本窗与Apr12无列项。
- Anthropic：`https://www.anthropic.com/research` 页面内170个publishedOn ISO元数据。邻界04-09T16:34Z trustworthy-agents →04-14T13:01Z automated-alignment-researchers；本窗与Apr12无列项。未使用lastmod。
- Seed papers：GET `https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&order_desc=true&page_token=0`，header `x-tt-locale: US`；total242，实际页0/20/40读过，页20跨04-12T16:00Z Continuous Adversarial Flow Models、04-10T16:00Z Protenix-v2、04-09T16:00Z Nexus，页40从04-07T16:00Z到02-26。停止于窗口以下；原始PublishDate是目录字段而非外链首发权威。Apr12窗口[Apr11T01Z,Apr12T01Z)无列项。
- Seed Blog：同API `article_type=2` 页0/20，total95。页0返回15条，next=20；页20返回18条，next=40，首项2025-12-17已低于窗口。页0邻界04-22T16:00Z Seed3D →04-08T16:00Z Full-Duplex Speech LLM →03-31T16:00Z招聘。本窗与Apr12无列项。没有把count=20误称返回20条，未因has_more仍true声称全95条读完。article_type=0不返回sub_article_list，不作覆盖证据。
- ERNIE：`https://ernie.baidu.com/blog/zh/` 第一页完整可见04-15→02-06，下面已到2025；本窗与Apr12无列项。`https://api.github.com/repos/PaddlePaddle/ERNIE/releases?per_page=100` 唯一release2025-06-30T01:15:24Z，无当窗。
- Z.ai：`https://www.zhipuai.cn/zh/research` 可见Research日期04-29→04-07→04-01，之后03月至2025-12，未列04-10/11/12；04-07时区即使未声明也不与本窗相交。不是CMS createdAt证明首发，亦不保证官网未列作者稿。
- MiniMax：英文 `https://www.minimax.io/blog` 05-26→03-18；中文入口跳转 `https://www.minimax.cn/blog`，全可见04-27→03-18，之后02月/2025。两个目录本窗与Apr12无列项。Agent TechBlog只给无日戳页；`/docs/llms.txt`现行文档索引有agent-team链接，不提供Apr窗口历史日期，因此该子入口缺口继续隔离。
- MiMo：`https://mimo.xiaomi.com/` Paper06-29→03-13→02-03→01-08无本窗/Apr12列项；Blog现行卡片没有历史日期停点，不能从论文目录替代Blog。
- OpenAI：News RSS1230条已按published UTC筛窗，04-10T00:00Z Axios compromise等早于本窗起点Apr10T01Z，下一侧04-13T06:00Z；本窗与Apr12无RSS条目。Research Index只返回现行9张至08-18并有Load more；Research sitemap52、Publication sitemap200为身份入口，lastmod不是first-public；未恢复Apr历史Research分页，精确隔离，不以RSS覆盖代替。
- Google：April Research Blog月目录已读，04-13→04-09 ConvApparel→04-08 academic agents。ConvApparel原文仅04-09日期无时区，外链ACL `2026.eacl-long.244`为March2026既有论文身份；本次不将日戳猜成精确当窗新稿。DeepMind selected publications264项第一页已跨04-22→03-22，所选目录无本窗/Apr12项；Google Research Publications只年级facet，历史日级停点未恢复。
- Meta：`https://ai.meta.com/research/`网页返回0可读行；历史Research/Publications日期目录仍缺，不报零命中。
- Moonshot：`https://platform.kimi.com/blog`所见时间最晚2025-11-07，不能作为2026年April覆盖。官方org列表中Kimi-K2.5为2026-01-30仓库，release API空；不查普通commit，不把空release代替历史Research。

## 前分母关闭与日期问题

1. Seed Protenix-v2：`https://www.biorxiv.org/content/10.64898/2026.04.10.717613v1.full.pdf`，目录PublishDate=1775836800000，即2026-04-10T16:00Z。本条结构预测/生物分子设计属当前暂缓AI for Science；标题足以明确范围排除，不成为Candidate Denominator，不评分不深审。目录入库时刻不冒充论文first-public；因范围已排除无需再追日期。
2. arXiv：官方 `https://info.arxiv.org/help/availability.html` schedule明确周五/周六无常规公告；前槽Thu04-09 20:00 EDT=Fri04-10 08:00北京，后槽Sun04-12 20:00 EDT=Mon04-13 08:00北京，均不在Apr11日窗。只证明常规槽，不证明不可能有异常公开。
3. 旧OAI缓存 `../arxiv-owner-replay-20260903/oai-list-identifiers/2026-04-11-cs.xml`实际有03263，stat/eess无header；旧receipt却写official_oai_direct_count=0，两者不一致。03263官方abs/v1仅v1（Submitted03-12），没有v2事件；OAI datestamp04-11不能单独建立当窗首发。已有Apr07贡献/日期隔离记录有效，不在本日重复审方法；若官方当窗公告或明确重要修订证据到达则定点重开。

## 当前终态前待办

通过root邻日已核身份，直接tag API恢复 `https://api.github.com/repos/MoonshotAI/kimi-cli/releases/tags/1.31.0`，published_at=2026-04-10T14:45:26Z；完整release说明已读、贡献消歧只定点PR1742/1822/1800/1801/1826，不重扫普通commit。详见日报§4具体关闭：todo持久化/反馈、advisory token刷新锁失败回退、特定SDK断流/think-only错误分类、可跳过startup提示均局部correctness/UX，没有新系统设计反证或保证。该第四个当窗事件不可被之前全分页失败遮掉。April完整Blog/CLI分页缺口仍隔离；Apr12窗不包含这个已核tag。

补充当窗官方release：MiniMax CLI API26条，v1.0.6 2026-04-10T05:15:40Z、v1.0.7 08:31:19Z。前者为音频扩展名、SSE raw decode/EPIPE（PR63/60），后者compare两提交删除重复SKILL.md/更新package版本；逐事件关闭，不按相关关键词升级。MiMo三个模型repo release均空、MiniMax M2/M2.5均空。kimi-cli release100条两次20秒请求截断JSON，page3/20仍超时，不能用这些失败查询证明Apr零release；精确隔离，未扫普通commit。

03263 DataCite current：created Apr07T02:37:14Z、Updated(v1) Apr11T04:37:54Z、Available仅2026-04。Updated已晚于本窗UTC01截点，不能把OAI Apr11日历日迁成本日。官方abs/history只有v1，既有Apr07日期保留请求复用，不重复请求。

DeepSeek实际官方可见列表研究06-24→02-25、动态04-24→2025-12-01跨窗；按可见目录有界检查，未声称查看全部按钮或所有未列作者稿已覆盖。

来源限制和03263/ConvApparel日期已在日报§5安全隔离。最终14来源/4个具体前分母关闭/0正式贡献候选/0必要Books；8外部保留项不用于正面证据、Books或无遗漏断言。root非作者日级Gate已通过：重新读取本日报来源/关闭/限制，独立打开KimiCLI正式release、1742/1822原始PR并对读Ch81实际正文，未声称全源二次抓取或实验复现。普通pending0；scoped validator/diff check通过，日报正式完成。授权续跑Apr13，当前AGENTS与V3合同不变，不继承旧零或DOI-created日期。
