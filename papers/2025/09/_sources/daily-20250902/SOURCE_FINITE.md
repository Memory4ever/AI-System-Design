# 2025-09-02 机构有限目录实际解析

作者 Aristotle；2026-10-06T14:47:00+08:00。本日窗口UTC Sep1 01:00至Sep2 01:00。复用本日原始捕获，实际解析不同于仅登记HTTP200；新增定点原件有对应request。只检查每日关注切片，没有扫描每周组/全机构历年论文，当前网页也不是不可变历史快照。

## 已检查的有限切片

| 来源 | 实际解析与停点 | 本窗处理/局限 |
| --- | --- | --- |
| OpenAI | [RSS](openai-rss.raw)实际1247 item，全部发布日期解析；窗口内0。邻近Aug28 10:00Z realtime、Sep2 04:00Z helpful ChatGPT /11:00Z收购 | 后两项在BJT Sep2 12:00/19:00，窗口后；前一项窗口前。不外推已删除条目/全网发布无遗漏，不开范围外正文队列 |
| Anthropic | [Research](anthropic.raw)内实际publication JSON，按slug/date去重172；最近Aug27 00:09Z Education、Sep5 00:00Z biorisk，Sep15两项 | 此有限Research目录没有本窗日期条目；未声称全部172正文已读或已删除历史完整 |
| Google | [Sep1页](google-month.raw)12项+[Sep2页](google-month-2.raw)1项，真实2/2；最早Sep9，跨到[Aug前缘](google-aug-frontier.raw)最近Aug27。DeepMind [page5](deepmind-history.raw)24条，Nov→Jul，6个Sep标题；相关Robotics/Frontier/ICPC原页分别[Sep25](deepmind-robotics-date.raw)、[Sep22](deepmind-frontier-date.raw)、[Sep17](deepmind-icpc-date.raw)，VaultGemma由Research月页Sep12复核 | 约定Blog切片未见本窗事件。fluid dynamics/universe题名为暂缓科学应用，未读全文、不宣称其无任何通用贡献；Aug条目均窗口前。pubs入口仅辅助定位，不授其全目录逐条覆盖 |
| Qwen | [research config](qwen-research-config.raw)递归解析60个unique id/date/title；本窗0。相邻Aug18 17:30Z Image-Edit与Sep8 06:38:04Z ASR | 新站配置实际可读，旧主页非全部目录；日期字段用于当前列表切片，不为任何候选证明first-public/未删历史 |
| DeepSeek | [正确updates](deepseek-correct-updates.raw)，2025切片实际Sep29 V3.2-Exp→Sep22 Terminus→Aug21 V3.1→May28 R1→Mar24 V3 | 此更新切片无本窗日期事件。保留错误路由request，不称其0命中或全repo覆盖 |
| Moonshot | [Blog](moonshot.raw)实际列表从Nov7 2025到May2024，Sep16 Turbo→Sep5 K2更新→Aug22提速→Aug1 Turbo→Jul17/11；读取日期及对应标题 | 此有限Blog切片无本窗事件；没有把价格条目当机制候选或扫描整个GitHub组织 |
| ERNIE | [page1](ernie.raw)→[page2](ernie-page-2.raw)，可见2/2终点；page2 Sep12 PLAS→Aug14 FastDeploy2→Jun30 ERNIE4.5 | 实际顺序跨窗，有限Blog无本窗条目；未扫每个领域结果或全部代码版本 |

这里的“无本窗条目”仅限上述实际解析目录，不能由此证明机构历史所有公开事件无遗漏。没有为范围外条目补造first-public时刻。

## 已解析但尚有历史/日期缺口

| 来源 | 实际处理 | 缺口及下一定点 |
| --- | --- | --- |
| Meta | 新捕获publication [page5](meta-publication-page5.raw)→[page6](meta-publication-page6.raw)，Sep24→Sep15→Sep8→**Sep2 DARLING**→Aug22；另Blog [page2](meta-blog-page2.raw)→[page3](meta-blog-page3.raw)，主序列Oct31→Oct24→Aug27→Aug14→Aug7/Jul31；旧2019/2024等穿插项不作为时间停止依据 | 实际完整读[DARLING官方摘要](meta-diversity-original.raw)，保留语义多样性/质量joint reward潜力；Sep2只有日期，不能断言在Sep2 09BJT前后，也不能拿较晚arXiv提交时刻否定更早官方发布。见FIRST_BATCH_02；本窗日期hold |
| Hunyuan | [全部API](hunyuan-api.raw)total9/returned9，实际解析全部9个title/displayPublishTime，均2026，最早Feb3附近 | 当前全部不等2025历史；本日未恢复该窗口历史。实际尝试浏览器：带visibility选项返回“subagent thread不支持”；不带该选项打开Research超时。没有成功UI观察，不称已点“全部”。尚需可用原历史或已知当窗原始发布定点；不把9项2026正文变队列 |
| ZAI | [Research原页](zai.raw)15项；[实际page2](zai-page-2.raw)18项含新增3项，并明确“没有更多”，到Dec7 2025；不是重复15或未执行More。发布说明[原件](zai-releases.raw)实际Sep30 GLM4.6→Aug11 GLM4.5V→Aug8 | 当前Research有限尾页已实读，但只到Dec2025，未恢复Sep1/2研究历史；release notes切片无本窗事件，不能代替Research论文。保留历史缺口，不声称GLM所有研究为0 |
| Seed | [BlogAPI](seed-blog.raw)实际15/total49，has_more/token20；置顶与主序分开：非置顶Oct23→Aug21 Seed-OSS→Aug14 VeOmni→Jul31等，跨窗停；[Paper头页](seed-paper.raw)total94/token20/has_more但**没有条目数组**。新实际[Paper token20](seed-paper-tail-repair.raw)只返回1项Jun12 SwiftSpec，仍total94/token40/has_more；[入口](seed-paper-entry-repair.raw)当前2026第一页，20/242、1/13 | Paper不能计0或20实读，也不能凭尾页June跳过缺失头页中的本窗相关论文；Blog有限切片已核，论文必要历史仍未恢复。可继续官方年份/窗口/地区参数有效性定点补查，不遍历94/242篇正文 |
| MiMo | [官网](mimo.raw)Paper8：Sep19 Audio→Jun4 VL→May12初代，未见本窗；Blog实际15标题，HTML含More。额外捕获[index](mimo-index-repair.raw)、[route目录](mimo-route-repair.raw)、[首页模块](mimo-home-repair.raw)、[More组件](mimo-more-component-repair.raw)，均配request，实际读必要实现 | 首页Blog传15条、initialVisibleCount8；组件39632以slice(0,8)/slice(8)分组，onClick只切换state/aria-hidden，**不是请求下一历史页**。旧“More未处理”待办被此原始实现定点消除，不冒称浏览器点击（尝试打开MiMo超时）。当前路由有Dec18/19 2025等，但不能恢复Sep历史/证明不存在旧文；保留历史限制而非全附件队列 |
| MiniMax | [EN](minimax.raw)12项至Oct27， [CN](minimax-cn.raw)13项额外Jan15 2025；新[EN page2](minimax-en-page2.raw)仍同12标题，不能当新增尾页。[Agent Tech Blog](minimax-agent.raw)实际仅见2026-05-13 Agent Team | 两种语言不能合并谎称13+13或漏掉CN旧条目；当前列表与?page=2不恢复9月历史。Agent当前单项同样不能作2025目录全0。剩有效原历史/定点官方发布恢复仍待，不追全部2026材料 |

## 本次初筛差额与停点

新增DARLING官方完整摘要有具体增量，因此保留datehold，不因日期unknown关闭。身份线索为[arXiv 2509.02534](https://arxiv.org/abs/2509.02534)，搜索显示Sep2提交；该字段不等首次公开，不倒授Sep2之后/本窗之前结论，也未称精确v1全文已读。未见于本日四主题Atom并集287，作为表外官方线索单列，不回写发现总数。

机构有限解析不替代其余287相关/含糊题摘工作。对上表缺口的普通恢复步骤尚可执行时仍列待办；本文不是本日终态、正面Coverage或DAY。精确外部历史/时间最终无法恢复时才隔离，并给具体重开入口，不为缺口批量开全文。
