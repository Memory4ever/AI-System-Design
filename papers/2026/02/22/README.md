# Daily Research — 2026-02-22

**规范：** V3
**窗口：** 2026-02-21T09:00:00+08:00 ～ 2026-02-22T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-05T11:31:41+08:00

## 1. 结论

本窗确认1个唯一贡献候选，已完成标准证据审阅；Books为1项具体已有覆盖，实际改书0。新的MCP schema适配修复说明：消除validator的元模式报错，并不等于保留参数语义。不能只按协议名称或“JSON Schema兼容”推断互操作。

14每日来源及两个实际触发表外release已经作本窗有界检查；窗外GLM-5目录收录、Anthropic安全路线图状态日期和OpenAI科学发布未移入本窗。没有把宽库存转换为逐题摘/全文队列，也没有继承旧V2.1的0候选/完成标签。原始发现、排除和停止位置见[本日来源/筛选依据](../_sources/daily-20260222/V3_SCREENING.md)；发布核心关闭不称全文审阅。

普通待办0；root非作者独立日级复核已通过。历史目录与arXiv非标准公开限制已隔离，不计正面Coverage/Evidence，不支持全网无遗漏或任意MCP server可靠性保证。未修改Books、共享索引、其他日期；未stage、commit、push。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS原item/pubDate扫描本窗，邻界02/20 14:30GMT～02/23 05:30GMT；[原响应](../_sources/daily-20260222/V3_NATIVE_openai_rss.txt) | 已检查 | 已检查；本窗无RSS事件；当前RSS不保证历史删除项不存在 |
| SRC-ANTHROPIC | Research原HTML全部publishedOn，02/18 15:10Z～02/23 11:52Z跨窗，无本窗条目；[原响应](../_sources/daily-20260222/V3_NATIVE_anthropic_research.txt)。安全信号另核RSP官网timeline，Roadmap发布为02/24 | 已检查 | 插图_createdAt、能力状态日期不当发布时刻 |
| SRC-GOOGLE-AI | DeepMind原RSS邻界02/19 16:06:14Z～02/26 16:01:50Z；[RSS](../_sources/daily-20260222/V3_NATIVE_deepmind_rss.txt)。Google Research官方February目录7条，最新Feb17、整页止；[目录](../_sources/daily-20260222/V3_NATIVE_google_blog_feb.txt)。Publications限定主题/日期补检，未全扫773页 | 受阻 | Blog/RSS已检查；Publications受阻；论文目录只有年份/当前第一页，未恢复本窗日级发布，不授该段历史覆盖 |
| SRC-META-AI | Research原网页0行；限定ai.meta.com模型/训练/Agent与Feb21～22补检返回窗外条目后止；[原读取](../_sources/daily-20260222/V3_RAW_web2.json)、[查询](../_sources/daily-20260222/V3_RAW_web8.json) | 受阻 | 历史研究目录不可提取；搜索不证明零事件 |
| SRC-QWEN | 注册入口跳qwen.ai；[native Blog壳](../_sources/daily-20260222/V3_NATIVE_qwen.txt)、网页0行、一次浏览器读取超时；限定官网本窗日期查询止 | 受阻 | 未恢复动态历史Blog；不扫全部旧release、不宣称零事件 |
| SRC-DEEPSEEK | 官方主页→API Docs；/news/实际跳当前First API Call，不能作历史目录；限定官网/API Docs日期补检止；[原读取](../_sources/daily-20260222/V3_RAW_web2.json)、[补检](../_sources/daily-20260222/V3_RAW_web13.json) | 受阻 | 未恢复本窗历史研究目录；当前API示例不证明历史变更 |
| SRC-MOONSHOT | Platform Blog实际26条、最新2025/11/07；真实/blog/posts/changelog最新2025/11/06；限定官方/kimi-cli GitHub日期补检止；[列表](../_sources/daily-20260222/V3_RAW_web2.json)、[补检](../_sources/daily-20260222/V3_RAW_web13.json) | 已检查 | 已检查公开Blog；历史代码检索受限；Blog不能覆盖所有官方代码变更，未恢复本窗相关release，不赋全项目零变更 |
| SRC-TENCENT-HUNYUAN | 原站JS确认allTab=renderType0；本日实际POST publicList，pageNum1/pageSize100，EN9/9、ZH11/11全部返回，窗前最近Feb13、窗后Apr22，止第1页；[ZH原响应](../_sources/daily-20260222/V3_NATIVE_hunyuan_zh.txt) | 已检查 | 已检查当前公开“全部”目录；无本窗条目；当前保留范围，不保证历史删除/未保留内容 |
| SRC-ZAI | Research时间列表从03/15跨02/21 GLM-5 report再到02/11；潜力题摘/current abs/本窗README commit核查；[目录](../_sources/daily-20260222/V3_RAW_web3.json)、[abs](../_sources/daily-20260222/V3_NATIVE_glm_abs.txt) | 已检查 | 已检查；晚收录不重复准入；没有本窗重要修订差额，不用目录日期重移v1归属 |
| SRC-BYTEDANCE-SEED | 原get_article_list_v2：type1 ASC/year2026/offset0/count20实际20条Jan20～Feb25，第19条已窗后即止、next20；type2 DESC/offset0实际12条跨March31～Feb14即止；[论文](../_sources/daily-20260222/V3_NATIVE_seed_papers_asc.txt)、[Blog](../_sources/daily-20260222/V3_NATIVE_seed_blogs0.txt) | 已检查 | 已检查；本窗无目录事件；首次type1空但has_more=true未作零命中；目录不是全网召回保证 |
| SRC-BAIDU-ERNIE | 官方Blog第一页日期从Apr15跨Feb06再到2025；已跨起点不翻第2页旧文；[页面](../_sources/daily-20260222/V3_RAW_web3.json) | 已检查 | 已检查；本窗无卡片；当前公开Blog范围，不保证过去删除项 |
| SRC-XIAOMI-MIMO | Paper/Blog当前Research从Mar13跨到HySparse Feb03，整段止；[原页面](../_sources/daily-20260222/V3_NATIVE_mimo.txt) | 已检查 | 已检查；本窗无目录条目；只当前公开Research范围 |
| SRC-MINIMAX | 英文SSR Blog12卡，邻界March18～Forge February14；中文入口跳minimax.cn；[英文原卡](../_sources/daily-20260222/V3_NATIVE_minimax_blog.txt)、[中文读取](../_sources/daily-20260222/V3_RAW_web5.json) | 已检查 | 已检查；本窗无目录条目；不代表过去未保留内容不存在 |
| SRC-ARXIV | 官方availability实际读取：Eastern Friday/Saturday无scheduled announcement；本窗是Eastern Fri20 20:00～Sat21 20:00，标准批次0。模型/训练、GPU/推理、Agent/RAG、多模态/World Model/VLA四组本窗官方域补检无恢复项；[主题查询](../_sources/daily-20260222/V3_RAW_web14.json)、[原规则](../_sources/daily-20260222/V3_NATIVE_availability.txt) | 受阻 | 标准批次已检查；历史列表受阻；cs.LG2602月列表web失败/native404，非标准提前公开不能穷尽；未把分类列表当逐题队列 |
| 表外：[HKUDS/nanobot](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post1) | 搜索触发release，原API Published21T13:09:50Z；核心说明及5个实际安全/执行信号定点核，止相应PR，不扩全项目；[原release](../_sources/daily-20260222/V3_NATIVE_nanobot_release.txt) | 已检查 | 已检查；贡献关闭；不赋memory/shell/Agent生产可靠性保证 |
| 表外：[oh-my-pi](https://github.com/can1357/oh-my-pi/releases/tag/v12.16.0) | 搜索触发release，原API Published21T14:00:02Z；#126核心/唯一diff、精确tag两条convertSchema消费路径；[release](../_sources/daily-20260222/V3_NATIVE_omp_release.txt)、[tag实现](../_sources/daily-20260222/V3_NATIVE_omp_tag_bridge.txt) | 已检查 | 已检查；1候选；静态原源审阅，未运行validator/项目或复现生产 |

到期来源已处理至上述有限停止或明确隔离；没有触发会议/每周来源的新发现扫描。历史目录受阻的行不称Coverage通过，其他确定原始入口照常处理。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [oh-my-pi v12.16.0 — MCP schema bridge #126](https://github.com/can1357/oh-my-pi/releases/tag/v12.16.0) | 2026-02-21T22:00:02+08:00 | draft-07 validator原本拒绝某些server元模式/nullable，递归适配恢复局部可调用性，却要求重新确认参数语义；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MCP，[Ch83 协议比较/adapter契约](../../../../books/part-07-agent/83-mcp.md#协议比较必须拆开五类契约)，实际改书0 |

没有把nanobot已有能力接入、结构化输出修补、公开help、regex误报、进程回收及in-process单飞当作新长期机制；排除项不评分。GLM-5和安全路线图不是本窗候选，不进入唯一家族分母。

## 4. 证据与知识整合

### [oh-my-pi v12.16.0 — MCP schema bridge #126](https://github.com/can1357/oh-my-pi/releases/tag/v12.16.0)

采用精确release v12.16.0，不是搜索后来拼接的完整changelog。原release只有#126与memory文档两项；先前索引中的abort提示不在本次release，已纠正，不构造第二个贡献。#126原说明：rmcp/schemars发出draft2020-12元模式声明和OpenAPI式nullable，draft07 AJV会拒绝未知元模式/keyword；作者在MCP→TypeBox边界递归去除字段，而非换validator方言。

[精确tag代码](https://github.com/can1357/oh-my-pi/blob/v12.16.0/packages/coding-agent/src/mcp/tool-bridge.ts) sanitizeSchema（[原响应](../_sources/daily-20260222/V3_NATIVE_omp_tag_bridge.txt)L53～89）在convertSchema执行；MCPTool/DeferredMCPTool分别L196/L300消费同一结果。原代码和[唯一diff](../_sources/daily-20260222/V3_NATIVE_omp_126_files.txt)支持“添加一条消除所述校验报错的适配路径”，不支持任意server方言语义等价。

关键反侧：递归处理所有object，并未把nullable:true重写为包含null的类型；properties字典中若业务参数本来叫nullable或$schema，也会被解构删除。去除声明并不会翻译draft2020-12其他keyword。这是静态实现推断，不是项目运行/生产攻击复现；不声称真实server中的发生比例。

本项无论文benchmark，吞吐、GPU、batch、concurrency、SLO/evaluator不适用，因采用对象是公开实现的兼容分支。PR声明tested locally但未给跨方言完整对照；实际运行环境与回归覆盖为Not Disclosed，本次未执行artifact，没有性能/安全收益数字可外推。

Books判断：Ch83“协议比较必须拆开五类契约”实际分离schema/effect/授权与runtime owner，要求adapter映射不完整时适配或拒绝；相邻typed definition生成两类adapter论证要求保留独立adapter、contract tests/schema diff以防最低公分母/特性漂移。这承载本次采用的稳定判断；#126只是新的局部兼容实例，不强造长期机制diff。root非作者实际核release、PRbody、完整diff及Ch83 L96～120，确认收窄与已有覆盖/No Change。

其余排除/日期关系见[本日筛选判断](../_sources/daily-20260222/V3_SCREENING.md)，不把已读发布核心计为贡献候选或正面Evidence。

## 5. 缺口与下一步

普通待办：0。来源/候选标准审阅/Books处置及非作者独立日级复核均已完成；以下仅终态保留项，不是待执行工作。

本窗终态保留项（不用于正面证据、Books或“无遗漏”）：

- Qwen/Meta动态历史研究目录、DeepSeek历史发布目录与Moonshot未恢复的相关代码release：有限官方入口和日期主题补检没有恢复本窗完整目录。需要本窗官方列表、精确release或作者原稿及公开时刻；回来只重开该来源/事件，不从API当前页、空响应或旧标签推零。
- Google Publications本窗日级事件：当前第一页只有年份/题摘，目录773页；需要官方日级发布关系或具体paper的首公开证据。已核Blog/RSS不填该缺段，不遍历全年以制造当日分母。
- arXiv非标准提前公开/cs.LG历史列表：标准Friday/Saturday无公告，但月列表失败。具体潜力身份及完全落窗的官方公告/作者先公开证据回来才重开；Submitted、DataCite-created、后收录日期不补造本窗时刻。
- 当前机构目录/RSS过去删除或未保留内容：当前暴露的有限范围就是本次停止位置；发现本窗相关遗漏原始事件时只定点补查，不重跑整月或扩Weekly。

窗外定位：GLM-5 2602.15763身份Registered02/18 02:49:09Z给出窗前上界，不能赋首公开精确时刻；Research目录02/21为后收录，无本窗重要修订信号。Anthropic RSP官网timeline的Roadmap发布为02/24，不从正文February22能力状态日期造候选。OpenAI Our First Proof是02/20 22:30BJT，窗前且AI for Science暂缓。均不阻塞本窗，不请求第二次材料或续跑窗外全文。

## 6. 复核

复核者：root（非报告作者）。

结论：通过

分批与最终复核：root实际核全部1项拟入选的release/PR/完整diff、精确tag证据及Ch83具体已有覆盖；GLM/roadmap/Proof日期与范围关闭通过。安全/执行负侧实际覆盖nanobot #824公开帮助、#820guard误报、#866memory schema修复；新增#851/#823的PR原body和完整唯一patch经root回核：5秒wait超时pass不授终止保证，同loop set/finally不授跨进程原子性，贡献关闭成立。最终顺读六部分、14每日与2触发源实际停止位置、公告时区、首公开关系及隔离边界，通过DAY。未检查其他无关release PR、全部机构历年论文或全网排除项，不称全量验证；历史缺段不是正面Coverage/Evidence。

机器校验已执行，首次只发现结果字段夹带说明、公开时刻字段夹带原值说明及候选标题与§4不一致，已只调整字段/标题、不改判断或校验器；V3通过。自写2份Markdown/30本地链接、围栏/空白及本日限定cached/unstaged diff-check通过。完成态再次校验，不以工具替代上述语义验收。
