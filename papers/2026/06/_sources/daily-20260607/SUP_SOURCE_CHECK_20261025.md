# 2026-06-07 补遗漏：本日来源检查

执行：2026-10-25（Asia/Shanghai），最终取时 17:32:27+08:00。只补 `2026-06-06` BJT；保留旧报告小时窗、旧材料归属/分数及有效证据。不加载其他日报候选或旧 Weekly，不写共享 Books。

## 入口与停止

正文覆盖表自包含各源结果；本文件仅保留必要查询和原始字段摘录，不另造候选/完成账本。无新增候选，尚待 root 非作者复核。三个首次合法恢复的动态原始响应另存为 `SUP_QWEN_EN_RETRIEVAL_20261025.json.gz`、`SUP_QWEN_ZH_RETRIEVAL_20261025.json.gz` 与 `SUP_HUNYUAN_ALL_ZH_20261025.json.gz`；其中包含完整接口原文，不是另造的审计投影。未把其非目标日正文全部读为已审阅。

- OpenAI：`https://openai.com/news/rss.xml`，当前单响应 XML `item` 数 1318；只选择目标相邻日期，不阅读历年正文。`Dreaming: Better memory for a more helpful ChatGPT` 的原 `pubDate=Thu, 04 Jun 2026 09:00:00 GMT`；之后相邻发布 `Introducing the OpenAI Economic Research Exchange`，`pubDate=Mon, 08 Jun 2026 00:00:00 GMT`。BJT 自然日无 06-06 项。首次一次 TLS EOF 后同一原始入口成功，失败未用于零命中证明。
- Anthropic：首查 `https://www.anthropic.com/research`；当前可见首批只到 08-10，不能证明六月。恢复 `https://www.anthropic.com/listing/research/default/2`，响应原键 `posts`、`hasNextPage:true`；24 项，首项 `publishedOn=2026-07-28`，末项 `2026-04-23`。目标邻段为 `2026-06-08 / n-days`、`2026-06-08 / agents-in-biology`、`2026-06-05 / making-claude-a-chemist`、`2026-06-03 / attack-navigator`。已越过目标，不继续第 3 页。日期选择关闭窗外条目，不对其贡献作本轮排除。
- Google：首查 DeepMind Research 与 Research Publications，后二者只作导航。DeepMind `https://deepmind.google/blog/page/2/` 的月份目录中，目标相邻卡片回原件得 `Introducing Gemma 4 12B: a unified, encoder-free multimodal model` 为 `Jun 03, 2026`（`https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/`），下一卡片 `Powering the future of robotics in Europe` 为 `Jun 09, 2026`（`https://blog.google/topics/google-europe/powering-the-future-of-robotics-in-europe/`）。Research 从当年页面的 June 链接进入 `https://research.google/blog/2026/06/`，12 项、一页无分页；目标邻段 06-10 auditing unlearning → 06-05 Agentic RAG → 06-04 heart health。未用不存在的时分字段改变其自然日。独核纠正：上述完成范围仅为 Blog；`https://research.google/pubs/` 未恢复 2026-06-06 日级公开日期/目录，年级元数据不支持正面 Coverage 或零研究结论。此来源缺口已在报告 §5 具名隔离为终态保留项；替代材料为有日期官方列表、具名本日原始正文或可读当日目录快照，取得后只重开本日 Publications 相关范围，不遍历全年论文。
- Meta：`https://ai.meta.com/research/`、`https://ai.meta.com/blog/`；Blog 可见卡片包括 `June 29, 2026 / From Brain Waves to Words` 与 `April 08, 2026 / Introducing Muse Spark`，目标日无可见条目。辅助查询 `site:ai.meta.com "June 6, 2026"`，无相关原件线索。仅授予此可见目录与查询的有限覆盖；不称完整历史档案。
- Qwen：`https://qwenlm.github.io/blog/` 明示迁往 `qwen.ai`。旧 `api/page_config?code=research.research-list` 60 项、`latest-advancements-list` 19 项都只到 2025，未用于本日覆盖。当前官方 `p_research-index.js` 的实际调用为 `j({type:"qwen_ai",language:"zh-cn"===t?"zh-CN":"en-US"})`；对应 `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US` 与 `language=zh-CN` 均 `success:true`，`data` 只有 `articles`，各 40 项，无分页字段。六月原字段为 `qwen3.7-plus / 2026-06-01T10:00:00+08:00`，四个机器人系列 `2026-06-16`，`qwen-agentworld / 2026-06-23T11:30:30+08:00`，无 06-06 项。无参数 GET 的 `articles=[]` 不算覆盖证据。浏览器恢复超时后使用上述原公开调用，不持续重试 UI。
- DeepSeek：`https://www.deepseek.com/` 研究入口与 `https://api-docs.deepseek.com/updates`。日志原相邻标题 `Date: 2026-04-24 / DeepSeek-V4` 与 `Date: 2026-07-31 / DeepSeek-V4-Flash Update`，未出现 06-06。停止于日期邻段，不遍普通提交。
- Moonshot：`https://platform.kimi.com/blog` 当前完整可见列表最新 `2025年11月07日`，未冒充 2026 全量档案；补 `https://api.github.com/orgs/MoonshotAI/repos?per_page=100&sort=updated`，未发现 06-06 新建研究项目。没有使用 `updated_at`、搜索时间或当前仓库更新时间证明论文首次公开。辅助目标日查询无相关原始事件线索，停止于该查询与组织目录响应。
- Hunyuan：首查 `https://hunyuan.tencent.com/research`。动态目录采用官方公开 API `POST https://api.hunyuan.tencent.com/api/blog/publicList`，请求体 `{"pageNum":1,"pageSize":100,"renderType":0}`。官方请求拦截器原字段 `"accept-language"="zh"`；按该头执行得到 `code=0,msg=success,data.totalNum=11,list.length=11`，无下一页。目标相邻 `id=100064 / Hy3 正式发布 / displayPublishTime=1783320600`（2026-07-06 14:50 BJT），`id=100041 / Hy-MT2：面向实际应用场景的高性能多语言翻译模型 / displayPublishTime=1779346800`（2026-05-21 15:00 BJT），下一 `id=100039 / 1777532400`（2026-04-30 15:00 BJT）。默认英语仅返回 9 项，未冒充中文“全部”；字段是目录显示日期，不改称全球首次公开时刻。
- Z.ai：`https://www.zhipuai.cn/zh/research` 日期排序首屏，`2026/06/16 / GLM-5.2` 后为 `2026/05/20 / ZCube`，已经跨过目标，不点更早“查看更多”。
- Seed：`https://seed.bytedance.com/en/public_papers`，原页面 `1 - 20 of 246 / Page 1 of 13`；邻段 `Jun 11, 2026` → `Jun 4, 2026` → `Jun 3, 2026 / MetaPoint`，停止第 1 页；6 月 4/11 日科学应用只作日期导航，不进入本轮候选/领域队列。
- ERNIE：`https://ernie.baidu.com/blog/zh/`，首屏最新 `2026年5月9日 / 文心5.1正式发布`，已早于目标；不读更早第 2 页。
- MiMo：首查 `https://mimo.xiaomi.com/` 的 Paper 与 Blog；Paper 原卡片 `MOPD / June 29, 2026` → `ARL-Tangram / March 13, 2026`。Blog 卡片不显示日期，因此只凭它不能授零。页面引用的官方静态资源 `https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js` 的 route/frontmatter 原邻段：`/blog/mimo-v2-5-inference / date:"2026-05-30"`，`/blog/mimo-tilert-1000tps / date:"2026-06-08"`，`/blog/mimo-code-long-horizon / date:"2026-06-10"`。只作目标邻段日期恢复，不读其他日期正文。V2.5/ASR/TTS/Pro 部分 route 没有日期，直接页当前只返回 CSR 壳；随后从可读原件 `https://mimo.mi.com/docs/en-US/updates/model` 恢复 Model Release：单页原标题 `2026-09-22 MiMo-V2.6 Series Release` → `2026-06-02 mimo-v2.5-asr Released` → `2026-04-23 mimo-v2.5-pro Released`、`mimo-v2.5 Released` 与 `MiMo-V2.5-TTS Series Release`。目标区间已越过，没有 06-06 项，无须继续旧版本。`/model-releases` 的 404 与 CSR 壳不作零命中证据；没有遗留的本日模型发布日期请求。若以后出现精确指向 06-06 发布的原始材料，只重开对应条目。
- MiniMax：`https://www.minimax.io/blog`，同一目录 `2026-06-09 / MaxProof` → `2026-06-01 / MiniMax M3` → `2026-05-27`，未出现 06-06；停止在目标两侧，不扩读正文。

## arXiv：限定本日而非重开旧 submission 队列

官方 `https://info.arxiv.org/help/availability.html` 当前原说明：Sunday through Thursday 公告，Friday or Saturday 不公告，且规则覆盖 new submissions、replacements、withdrawal notices、cross listings、journal reference。2026-06-06 BJT 是周六；当季 EDT 下前一正常公告为周四 20:00 EDT（周五 BJT），下一为周日 20:00 EDT（周一 BJT）。因此没有本日常规公告批次；不据提交日期造当天新公开队列。

用 `https://api.datacite.org/dois` 的原请求参数：

```text
client-id=arxiv.content
query=registered:[2026-06-05T16:00:00Z TO 2026-06-06T15:59:59Z]
page[size]=1000
```

原响应 `meta={"total":0,"totalPages":0,"page":1}`、`data=[]`，原件 `SUP_DATACITE_REGISTERED_JUN06_20261025.json`。检索自检正控制：仅参数 `client-id=arxiv.content&page[size]=1` 返回 `total=3221843`；同一来源筛选加 `registered:[2026-06-01T00:00:00Z TO 2026-06-10T23:59:59Z]`、`page[size]=1` 返回 `total=12435`，首项 `10.48550/arxiv.2606.10420 / registered=2026-06-10T02:06:32Z`。这两项仅验证来源筛选和日期字段确实生效，不扩成六月候选队列。早先错误 query 字段 `client.client-id:arxiv.content` 单独查询即错误零命中，已废弃，不作为覆盖；换成有效来源参数后目标区间重查仍为零。

请求的精度为秒；原始接口登记字段不是实际公开时刻，也不证明所有作者早稿不存在。无命中即无须分页，不是将宽元数据列表变成逐项关闭队列。`cs.CL` 六月官方月页可访问，但为整月 title 列表而非本日公告，未用其自动扩池或证明逐日无遗漏。错误 `date=` 列表请求未恢复；catchup 只返回表单，不作本日证据，也不继续把 90 天入口用于更早历史。

本日已有迁出记录与原始 Evidence 不改变、不重评；旧 `created` 单字段推断不作本轮公开日期证据。未发现具体更早正文、延迟公告或撤回冲突信号，因此没有具名日期恢复待办。若获得精确当窗公告/作者发布，定点重开对应家族，不能用本段拦截新证据。

## 判断与复核交接

本轮没有通过贡献筛选的新增材料，也没有需要给分或进入 Books 的材料；无凭“主题相关”造候选、无因局部/负面结果机械排除的集合。代表性检查是日期入口选择，不是论文贡献初筛；没有题摘可交首批准入校准。报告不继承旧“通过”签名，非作者应实际检查上述入口、日期邻段与范围限定，然后决定本轮能否结束。
