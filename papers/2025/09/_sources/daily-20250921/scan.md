# 2025-09-21 有界来源检查与作者 handoff

窗口：2025-09-20T09:00:00+08:00 ～ 2025-09-21T09:00:00+08:00。作者 James；按当前 AGENTS、研究合同 §2–6、Report 合同执行。执行时间见 `fetch-results.json`、`supplement-fetch.json`（2026-10-06T03:22～03:33Z）。没有读取其他 Daily 或 Weekly 来生成候选。

## 入口、停止与原始依据

- OpenAI：Research 首查 HTTP 403；web 可读当前首页，不能证明历史覆盖。转官方 `https://openai.com/news/rss.xml`，完整保存 `OPENAI_RSS.raw`，解析 RSS 中 pubDate，按本窗筛选为 0；相邻原记录为 09-17 scheming 与 09-22 合作发布，均不扩本窗。RSS 历史项已跨到窗口之前，停止；不声称 RSS 等于所有未收录研究。
- Anthropic：`ANTHROPIC.raw` 与结构化 `ANTHROPIC-flight.txt` 内 publication 对象实际可追到 2025-09。publishedOn 落窗对象 0；目录窗口两侧是 09-15 Economic Index 与 09-26 后条目。停止于当前目录内本窗筛选，不扩工程站全量。`site:anthropic.com/research "September" "2025"` 补检首返回页没有发现窗内研究。
- Google AI：Research/DeepMind 首查均保存。Google Research 9 月 Blog 第 1 页可追到 09-11，跨过本窗；`GOOGLE_SEPT.raw`。Publications 只有年级筛选，无可支持本日公开归属的字段，保留限制。DeepMind Blog page/7 与 page/6 均早于目标月，page/5 实际含 6 个 9 月标题（只作路由）。定点核 FSF、ICPC 与 Robotics 1.5 事件页日期分别为 09-22、09-17、09-25，排出 21 窗；没有遍历全部论文。page/5 原始标题不是全文队列。
- Meta：官方 `META.raw` HTTP 200，但解析只有页面标题，web 文本 0 行；一次 `site:ai.meta.com "September 20, 2025"` 未找到可用本窗原始研究。终态覆盖保留，不称零事件。
- Qwen：`QWEN.raw` 首页直接从 09-23 Qwen3Guard 跨到 08-19 Qwen-Image-Edit；本窗无目录命中，停止首页。不读取后日内容作为本日研究。
- DeepSeek：首查主页后转官方 updates，`DEEPSEEK_LOG.raw` 在 09-22 与 08-21 间无目标日事件；只核日期，不审后日机制。
- Moonshot：`MOONSHOT.raw` Blog 日期由 11-06 跨到 09-16，再 09-05，窗内无目录项，停止完整可见单页。
- Hunyuan：必须首查 Research，静态 `HUNYUAN.raw` 是空壳。浏览器第一次 30s 超时；指定 visible:false 被 subagent 不支持；去掉该选项仍约 95s 超时。恢复公开 App/Blog JS，实际发现 `/api/blog/publicList`；同域误试 404 后由 App 中 baseURL 纠正至 `https://api.hunyuan.tencent.com/api/blog/publicList`。请求 `{pageNum:1,pageSize:100,renderType:0}`，`HUNYUAN_LIST1.json` 返回 code=0、totalNum=11、list=11；全部记录为当前新版目录，不能恢复 2025-09。JS 明确 renderType=0 是“全部”。停止，不以当前 11 项授历史覆盖。
- Z.ai：Research 首查 `ZAI.raw` 及结构化 `ZAI-flight.txt`，首批实际15项（先前误计14，已窄纠；见 `ZAI_items.json`）最早为 2025-12-09，存在“查看更多”；首轮浏览器不可用。限定 `site:zhipuai.cn "2025" "9月20"` 未返回可用记录。后续实际分页恢复见下段，不称已覆盖2025年9月目录。
- Seed：Publications `SEED.raw` 首批 20/242，止于 2026-05，非目标窗口；静态没有可用历史查询。`site:seed.bytedance.com "September 20" "2025"`、`site:seed.bytedance.com "2025" "09-20"` 首页未恢复窗内记录。保留历史分页缺口。
- ERNIE：首查 Blog 后明确跟随第 2/2 页，`ERNIE_P2.raw` 包含 09-12 PLAS，未见本窗项，完整分页停止。未把 09-12 加速作为本日候选。
- MiMo：`MIMO.raw` 研究列表由 10-21 跨到 09-19 MiMo-Audio，再 06-04，窗口无确定事件；该 09-19 日历字段没有时区，若发布时间在美国等时区可能与本窗交叠。保留单项日期限制，未以 submitted 日期代替公开。
- MiniMax：Blog 首查 `MINIMAX.raw` 与 `?page=2` 的 `MINIMAX_P2.raw` 各有12个dated items（此前误计10，按原响应窄纠，包含Music3/H3/MaxProof），末项为2025-10-27；两页日期/标题序列相同，web报不可达。没有真实第二页，因此不称分页完成。`site:minimax.io "2025" "September 20"` 未恢复事件，保留历史目录缺口。中文及Agent注册入口实际首查/重查见下段，不以英文替代它们。
- arXiv：`ARXIV_SCHEDULE.raw` 官方 availability：美国东部 Sunday～Thursday 20:00 公告，Friday/Saturday 无公告。此窗对应美国东部 09-19 21:00～09-20 21:00，不含常规公告批次；不将周末 submitted 项作为首次公开。检查分类主题范围 cs.CL/LG/DC/AI、CV/RO、AR/PL、OS/PF、IR/MA 在此窗没有应恢复的常规批次，故不构造月目录全文队列。排程不能排除特殊公告或作者其他平台先发；如获得异常公告或具体作者公开材料只重开本项。

辅助检索均止于 web 首返回页，非全网召回。实际查询还包括 `"September 20, 2025" LLM model research`、`"2025年9月20日" 混元 智谱 模型 论文`、`site:openai.com/index/ after:2025-09-19 before:2025-09-22`、`site:deepmind.google/discover/blog/ after:2025-09-19 before:2025-09-22`。结果出现泛目录、旧事件与二手日报，只用于回官方原文，没有采用其结论。

## 具名判断与独立抽检建议

1. [Google TTD-DR Blog](https://research.google/blog/deep-researcher-with-test-time-diffusion/) 原始字段 `data-blog-publish-date="20250919"`；核心机制、结果、消融说明已读。链接 [2507.16075v1](https://arxiv.org/abs/2507.16075v1) 完整题摘与版本史，仅 v1（07-21 submitted，不当 first-public）。Blog 的 draft-first、retrieval revision、component self-evolution 与 v1 题摘相同，没有标示 9 月重要修订或纠错；本次新增只是解释/产品 availability，未确认新的机制或评价约束，因此贡献前关闭，不评分。具体历史 Books/07月处置未知，不能称“已审重复”。无需为不影响贡献处置的 Blog 时间再追秒级字段。原始 Blog 保存 `GOOGLE_TTD.raw`。
2. [MiMo-Audio](https://mimo.xiaomi.com/)：只取得官方目录标题/09-19 字段，未取得本窗首次公开依据，不列候选、不评分，不声称证据完成。
3. OpenAI/Anthropic/Qwen/DeepSeek/Moonshot/ERNIE 的上述目录停止属于日期层排除，不是无贡献排除，更不是深审完成。

## 给 root

2026-10-06T11:43+08:00 定点修正：root 提供公开 API 技术路由后实际执行 `https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&page_token=0&count=20&order_desc=true`（Locale:US）。`SEED_API_TYPE2.json` 返回 total=49、15项、next_page_token=20、has_more=true；非置顶日期已跨至2025-07-15，09月只有09-09，故 Blog 本窗有界检查已停止，不需为更早分页继续扫描。type1 同请求返回 total=94/has_more=true，但没有 sub_article_list；`SEED_API_TYPE1.json` 保留，不将论文目录记零项。当前 Seed 保留项仅论文 API 缺列表，不再是未执行 Blog 分页。请求/时刻见 `seed-fetch.json`。原首查失败/局限记录保留，此段覆盖原 Seed 状态。

作者有限发现工作 ready；确定候选 0、证据审阅候选 0、拟 Books 修改 0。普通作者待办 0，但 Meta、Google Publications、Hunyuan、Z.ai、Seed、MiniMax 历史目录及 MiMo-Audio 日级日期为明确隔离的外部保留项。root 请独立核来源边界/停止、TTD-DR 代表排除与日期保留处置；本日仍进行中，不能由作者授完成。无需 Books 写锁。没有修改 Books、月 README 或 LEARNING_STATE。

root DAY前窄补（实际请求见 `narrow-fetch.json`，原记录均保留）：

- Z.ai `https://www.zhipuai.cn/zh/research?page=2` 已执行，`ZAI_P2.raw` / `ZAI_P2_items.json` 返回累计18唯一ID，nextPage3、hasMore=false，新增145/144/143；最早createAt为GLM-4.6V `2025-12-07T16:00:00.000Z`。首15项计数已修正；这是当前目录两页停止依据，不是9月历史恢复，残余缺口从“未执行查看更多”收窄为新版目录历史缺段。
- MiniMax 中文 `https://www.minimaxi.com/blog` 新取 `MINIMAX_CN.raw` / `.txt`：实际13篇，2025-10-27 MiniMax M2下一可见是2025-01-15 MiniMax-01；有限可见序列夹过本窗，没有当窗条目。仅这一可见切片已检查，不把13篇当全部官方历史；英文分页试验局限仍保留。
- 作者普通待办再次核为0；没有确认候选/必要Books写入，待root具名DAY。ready为本日README、scan、narrow-fetch及其原响应/题目数组；不可直接把作者ready计为日级验收。

root DAY计数反馈后的窄核（2026-10-06T12:10+08:00；不移除原响应）：

- `ZAI.txt` 逐行日期共15个，与 `ZAI_items.json` 的15项一致；ZCube和Scaling Pain均已计入。正式README/本记录已无“首14项”现行覆盖断言，先前误计只作纠错历史。
- 英文 `MINIMAX.raw` / `MINIMAX_P2.raw` 各12个dated items，相同序列：2026-08-13、07-31、06-09、06-01、05-27、05-26、03-18、02-14、02-12、01-27、2025-12-23、10-27。该计数不是12篇本日候选，也不授分页完整。
- 中文注册入口 `https://www.minimaxi.com/blog` 已有本日 `narrow-fetch.json` 的03:59:11Z原请求；为响应本次复核再次实际取回 `MINIMAX_CN_RECHECK.raw`，04:09:00Z、HTTP200，跳转 `https://www.minimax.cn/blog`。仍13项，10-27下一可见01-15，有限夹窗；不把跳过的月份视为完整无事件。请求证据见 `minimax-recheck-fetch.json`，原 `MINIMAX_CN.raw` 保留。
- Agent注册入口 `https://agent.minimax.io/docs/techblog` 实际04:09:01Z、HTTP200，`MINIMAX_AGENT.raw` 原HTML只列一篇2026-05-13《MiniMax Agent Team: Built for Long-Horizon Work, Built to Keep Improving》。随后实际取官方 `/docs/llms.txt`，`MINIMAX_AGENT_INDEX.raw` / `minimax-agent-index-fetch.json` 记录04:10:01Z、HTTP200；当前索引只列这一个techblog/agent-team文章路径，无可见历史分页。停止于该有限当前目录和索引，不读窗外正文、不称2025该入口不存在，不授目标历史完整覆盖。取得本窗官方历史目录/具名事件后仅重开该项。
- root已传回实际独核：TTD-DR完整正文及2507.16075v1完整题摘的reexposition贡献前关闭可接受；VaultGemma官方事件09-12不属本窗；page5《Discovering new solutions to century-old problems in fluid dynamics》及《Using AI to perceive the universe in greater depth》题义为暂缓AI for Science，关闭而不再追日期。这里保留复核者归属，不声称作者新增正文审阅。
- 普通作者待办0，No Change建议不变；最终具名DAY尚待root。ready材料为本日README/scan、narrow-fetch、minimax-recheck-fetch、minimax-agent-index-fetch及关联原响应。
