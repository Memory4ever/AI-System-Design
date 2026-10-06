# 2025-10-01 来源执行与筛选边界

作者root；本日窗口BJT `[2025-09-30 09:00,2025-10-01 09:00)`。真实原生请求、执行时间和失败结果见NATIVE_FIRST/SECOND/THIRD及NATIVE_RECOVERY至RECOVERY6 JSON；请求成功不等完整来源覆盖。未读其他日期候选池。web原入口调用与原生直连结果不同，分别保留。

## 官方来源的实际停止范围

| 来源 | 本次实际检查与停止点 | 可支持与不可支持 |
| --- | --- | --- |
| OpenAI | [官方RSS](openai.xml)1245项仅按pubDate过滤；七case同October报告家族。七原HTML必要安全/纠错核心逐一读，Russian末尾L48补齐；作者未读PDF，非作者仅核必要安全/纠错页 | 支持case页记录Oct1 00GMT/BJT08；非作者已裁决Oct7主发布页为同家族的不同页面事件，不推断整PDF首次公开或全文已审。见FINAL_INDEPENDENT_REVIEW。 |
| Anthropic | [Research原件](anthropic.html)Next Flight JSON解码174个publishedOn对象、172个去重项，仅日期切片；首批独立复现窗前09/15T20:33Z、窗后10/03T18:31Z | 返回数组无落窗项，不是全站零事件。 |
| Google/DeepMind | 官方Research/pub首查，Google原生pub12s超时；DeepMind webResearch仅当前目录。旧Google `?m=202509`、DeepMindBlog `?page=5`失败；官方域名Sep30限定补检恢复[真正September归档](https://www.research.google/blog/2025/09/)首12卡、共2页，Sep30两卡后Sep25已经越出日窗，停止不读全月 | 原归档两卡及核心已读；Googlepub/DeepMind历史日段未恢复，不能授全覆盖。 |
| Meta | Research原生连接重置、web空响应；一次限定 `site:ai.meta.com "September 30, 2025" OR "October 1, 2025" research`，第二次Research限定Sep30，仅恢复2024 Blog片段 | 年份不符不采用；本窗历史Research受阻，不把无搜索命中当无事件。 |
| Qwen | [旧首页](qwen.html)日期至09/23、08/19、08/04、07/27、07/24；独立[迁移新Research](qwen-new.html)返回应用壳；一次官方新域Sep30限定补检无可核事件 | 旧页停止更新不能覆盖本窗；保留迁移后的历史目录缺口。 |
| DeepSeek | [主页](deepseek.html)实际链接 `/news/`，已恢复[原News/Research](deepseek-news.html)。Research可见10条，日期切片10/21到05/14；News09/29 V3.2-Exp、09/22 Terminus在起点前 | 本次可见目录无落窗项；不把News替代Research，不证明其他仓库直发无事件。 |
| Kimi | [Platform Blog原页](kimi.html)可见日期11/07、11/06后09/16/09/05，期间未见落窗卡；只查看本窗邻接与原入口，不把Next __NEXT_DATA__空pageProps当文章数组 | 当前列表日期切片成立；不覆盖GitHub全部历史事件。 |
| Hunyuan | [Research壳](hunyuan.html)，后台browser inventory可读但Mac锁屏；创建隐藏tab30s超时重置，没有AX/列表证据。由本日own主/Blog/API bundle恢复实际API `https://api.hunyuan.tencent.com/api/blog/publicList`，POST pageNum1/pageSize20/renderType0，默认en共9条，最早2026/02 | API是真实“全部”机制，但只返回当前目录。未恢复2025历史，终态隔离；不授浏览器已检查列表。 |
| Z.ai | [Research](zai.html)与[实际page2](zai-page2.html)，ownbundle证实按钮router设page，累计18项、末2025/12/07“没有更多” | 目录确实无10月历史段；不能记2025/10零研究。 |
| Seed | 两注册首查与ownbundle恢复get_article_list_v2；type1不带locale页0缺数组但total94/has_more=true，因此按ownbundle加x-tt-locale:US恢复[页0](seed-papers-us0.json)18返回、[页20](seed-papers-us20.json)20返回，非置顶从10/22越到09/22，再至06/20；type2[页0](seed-blog0.json)15返回与[页20](seed-blog20.json)18返回，非置顶10/23→08/21、后页07/14→03/12 | 对本窗日期定位停止；置顶另看，不全审94/49年度库存，不为了has_more=false翻全年。PublishDate保留原毫秒字段，不替代论文首公开。 |
| ERNIE | [原第1页](ernie.html)10卡及[第2页](ernie-page2.html)6卡，终页1/2；本窗邻接09/12 PLAS、10/16 PaddleOCR-VL | Blog目录无落窗项；不外推所有repo版本。 |
| MiMo | [主页](mimo.html)原壳，经own4752/main/async8557/6159四步恢复Paper数组8项，09/19 Audio、10/21 MoE RL夹住本窗；Blog15项只是local initialVisibleCount8展开，无历史分页；第一次async路径缺async实际404已修复 | Paper当前日期切片无落窗项；Blog历史缺段单独保留，不把More证明历史读完。 |
| MiniMax | [EN](minimax.html)、[CN](minimax-cn.html)原Blog可见日期M2 10/27窗后，CN01/15在窗前；独立[Agent原件](minimax-agent.md)实际是重定向HTML、2026/05/13，不是作者Markdown | Agent历史缺段不由CN/EN覆盖，保留外部项；目录不是全站事件保证。 |

## Google两卡：不是当天两篇新论文

实际读[AlphaEvolve原Blog](https://www.research.google/blog/ai-as-a-research-partner-advancing-theoretical-computer-science-with-alphaevolve/)核心：有限构造嵌入固定证明框架、演化验证器与最终原始验证器分责。原链接[2509.18057](https://arxiv.org/abs/2509.18057)版本史v1提交09/22、v3提交09/29；这些是提交字段，不证明逐版本公开日界。本Blog未披露独立新release、artifact或修订贡献，介绍日期不重置论文首公开。原论文只作真实首公开归属日待确认的恢复线索；本轮未审其历史版本，不记作已审重复项、本窗排除已审或确定窗外。未采用后来的v7新TSP结果。

实际读[PHA原Blog](https://www.research.google/blog/the-anatomy-of-a-personal-health-agent/)核心：三角色动态编排与同角色并行/单Agent对照、研究原型与临床产品边界。原链接[2508.20148](https://arxiv.org/abs/2508.20148)显示v1提交08/27、v2 09/18并注明minor updates；本Blog仅介绍既有工作，无独立新发布机制/反证。不能把医疗应用名称直接判AI for Science，也不把能映射Multi-Agent就自动准入。本轮不核临床疗效，不采用现版全文结论。两Blog仅日名09/30、时区未知；因没有决定本窗准入的新事件，不为介绍文章追造时刻。

## arXiv：有界发现与日期保留

[官方公告规则](https://info.arxiv.org/help/availability.html)已实际读：审核可延迟1～4日以上，提交非公开；常规美东周二20:00对应本窗BJT10/01 08，但规则不能逐篇证明实际批次。

真实API [arxiv-topic.xml](arxiv-topic.xml)：提交发现区间09/29T18Z～09/30T18Z，LLM/transformer/inference/agent/multimodal/MoE，start0/max40，total464。返回QCD、copula等显示单独inference/agent词过宽；不把464或40变成当窗候选队列。只浏览40标题、有界读相关题摘，范围外明确项如QCD、星系、医疗图像去噪停止，不全审。两个18:00闭端点也不赋首公开。

实际收窄系统查询 [arxiv-systems.xml](arxiv-systems.xml)：cs.DC/AR/PL/OS/PF，language model/GPU/tensor/transformer，start0/max20，total15，返回15标题。宽池只作线索，不扩大全年；系统题摘中particle tracking、Gaussian-splatting kernel等不自动因硬件/LLM关键词入选。

原 `/list/cs.CL/2509?skip=0&show=25` 404；定点恢复[官方新月格式cs.CL/2025-10](https://arxiv.org/list/cs.CL/2025-10?skip=0&show=25)，实际首25标题，按ID升序2510.00125～2510.00526，不是日期批次标题，月目录2666不作队列。cs.DC同参数web失败。辅助三查询分别Sep30 LLM训练推理、Sep30 Agent多模态、Sep29 GPU通信，仅提供线索。不声称覆盖所有分类/全部相关研究。

下列13项完整题摘已读（API当前精确版本，不冒充2025 v1）；可能改变主线设计的增量清楚，但未取得官方逐篇first-public日批次/完全落窗bounds。因此不评分、不授当窗Evidence/Books，不用最新v2/v3回写历史：

| ID与已读版本 | 潜在增量，仍须精确首公开与历史版本才可采用 |
| --- | --- |
| [2509.26644v1 Stitch](https://arxiv.org/abs/2509.26644v1) | MMDiT中段attention分离对象、bounding-box stitching，不因仅位置任务指标而关闭其具体机制。 |
| [2509.26642v2 MLA](https://arxiv.org/abs/2509.26642v2) | positional correspondence异模态token与future multisensory posttraining；当前v2不是已核旧v1。 |
| [2509.26634v2 syllabic speech](https://arxiv.org/abs/2509.26634v2) | syllable token rate与训练/推理资源取舍；不把压缩自动当保真。 |
| [2509.26632v1 Measurement Trees](https://arxiv.org/abs/2509.26632v1) | 多层不同construct/aggregation透明；需核心证明不是只有指标收纳。 |
| [2509.26628v1 AttnRL](https://arxiv.org/abs/2509.26628v1) | branch位置、非零advantage采样与one-step offpolicy三者职责；不把attention相关性当因果。 |
| [2509.26626v2 RSA](https://arxiv.org/abs/2509.26626v2) | population aggregation反复生成，后来的Gemini3等不能作为当日事实。 |
| [2509.26578v2 CRM](https://arxiv.org/abs/2509.26578v2) | condition on history/outcome的reward credit；因果措辞不等已核因果识别。 |
| [2509.26553v2 FuncBenchGen](https://arxiv.org/abs/2509.26553v2) | 可控DAG、connected distractor、stale argument失效；不由合成自动证明无污染。 |
| [2509.26541v2 TASP](https://arxiv.org/abs/2509.26541v2) | 互连拓扑正交ring分解与通信并发；未核实际历史v1或端到端加速。 |
| [2509.26182v1 Parallax](https://arxiv.org/abs/2509.26182v1) | placement与请求pipeline选择分离应对异构/动态；只读AB与abs身份，不授复现。 |
| [2509.25919v1 StorInfer](https://arxiv.org/abs/2509.25919v1) | 预生成语义响应库存绕过推理、adaptive去重覆盖；需比较质量/新鲜度和成本。 |
| [2509.25853v1 SAIL](https://arxiv.org/abs/2509.25853v1) | SRAM LUT-GEMV、pattern reuse与内存转换；gem5模拟不能等同实卡端到端。 |
| [2509.25401v1 FlashOmni](https://arxiv.org/abs/2509.25401v1) | sparse symbols统一kernel与DiT稀疏GEMM；未核质量matched条件。 |

另由限定搜索读到[2509.26520v1 M-MoE](https://arxiv.org/abs/2509.26520v1)原abs完整AB与[2509.25996 CAST](https://arxiv.org/abs/2509.25996)索引返回完整AB；前者训练时vary K支持弹性，后者优化稀疏mask/weight联合。原submitted不是公开；同样日期/精确历史版本保留。NeurTransformer2510.00133提交18:11在提交发现尾界之外，不能自动归本窗。

终态保留要求是实际官方公开列表/原作者带时区发布记录或完全落窗archive bounds到达后，仅重开对应身份。不要用DataCite创建或本轮下载时间填首公开。已保存宽池不变成未来必须关闭的464项。首次正式候选分母只包括已确证落窗的case发布家族。
