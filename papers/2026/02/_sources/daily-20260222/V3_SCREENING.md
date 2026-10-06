# 2026-02-22：本窗来源与筛选依据

窗口 `[2026-02-21T09:00:00+08:00, 2026-02-22T09:00:00+08:00)`。实际查询于2026-10-05执行。只使用当前14每日源与ROADMAP的模型/训练/推理/多模态/平台/Agent主线；宽目录仅浏览相关标题/时间，不转为逐题摘或全文队列。旧V2.1正文及旧0候选/完成标签不用于本次判断；未读旧Weekly。

## 原始记录与有限停止

- `V3_NATIVE_FETCH.json`、`V3_NATIVE_RECOVERY*.json` 是本日实际请求URL、body及状态；相应`V3_NATIVE_*.txt`是原站响应。`V3_RAW_web*.json`保留网页读取和查询结果。解析工具不能证明语义贡献。
- OpenAI：原RSS所有item的pubDate字段定位相邻02/20 14:30GMT和02/23 05:30GMT；本窗无RSS事件。Research当前首页不是历史覆盖依据。
- Anthropic：原Research HTML内publishedOn列表从02/18 15:10Z（measuring-agent-autonomy）跨到02/23 11:52Z（AI-fluency-index）/11:53Z（persona-selection-model），没有本窗条目；不把插图_createdAt当发布时刻。RSP官网timeline另核February24发布Roadmap，而不是用正文February22能力状态日期定位首发。
- Google：DeepMind原RSS邻界02/19 16:06:14Z～02/26 16:01:50Z，本窗无事件。Google Research从官方2026入口点击February到`/blog/2026/02/`，7条最新February17，整页止；最初`?year=2026`没有实际过滤，已修正，不拿它证明历史覆盖。Publications只显示年份/当前第一页（773页），未全站遍历；原站不能恢复本窗日级事件时保留缺口。
- Meta：Research网页返回0行；限定ai.meta.com的模型/训练/Agent和February21～22补检得到窗外条目，不赋历史目录正面覆盖。止于原目录+限定日期主题查询，没有逐个旧作者论文重审。
- Qwen：旧入口实际重定向qwen.ai，原Blog native HTML仅壳；官方浏览器一次读取超时（kernel reset），限定qwen.ai日期查询无确定事件。停在该目录缺口，不扫全部旧release。
- DeepSeek：主页与所链接API Docs当前页可读，但没有本窗历史研究目录；`/news/`实际重定向当前First API Call，不能作为历史无事件证据。限定官网/API Docs日期补检未恢复本窗必要条目，隔离历史目录缺口。
- Moonshot：Platform Blog实际26条，最新2025/11/07；点击实际`/blog/posts/changelog`核正文最新2025/11/06，不沿用第一次错误`/blog/changelog`路径失败。限定Moonshot官方/kimi-cli GitHub本窗日期补检无可定位事件；停点不代表所有代码项目当日无变更。
- Hunyuan：网页空时从原站research JS恢复`POST https://api.hunyuan.tencent.com/api/blog/publicList`，body=`pageNum:1,pageSize:100,renderType:0`，JS明确0为allTab。英文原列表9/9、中文11/11实际返回，中文最近窗前Feb13和Feb03，随后Apr22等窗后。读取时间/标题即可停，原列表不转为11篇重审；当前公开目录不能排除过去删除或未保留的条目。
- Seed：从原站JS恢复get_article_list_v2。第一次type1 DESC空但has_more=true不能作零命中；改type1 ASC/year2026/count20，真实20条时间Jan20～Feb25，第19条跨到Feb25且排序递增，本窗无目录事件，止在offset0/next20不翻后续窗后页。type2 DESC当前返回12条、相邻March31和Feb14；本窗无Blog条目，止offset0。广泛科学应用题名不送入贡献审阅。
- ERNIE：官方Blog第一页面日期跨Apr15～Feb06，继续到更早2025；本窗无目录条目，已跨窗口不读第2页旧文。
- MiMo：当前Research Paper/Blog从Mar13跨到HySparse Feb03，整段当前目录止；不遍历后续旧稿。
- MiniMax：英文原SSR Blog12卡从March18跨到Forge February14；中文入口实际跳minimax.cn。只当前公开卡片范围，不读所有旧卡正文，也不声称历史删除项不存在。
- arXiv：实际官方availability：Eastern Friday/Saturday无scheduled announcement；本窗是EasternFriday20 20:00～Saturday21 20:00，两端没有标准公告批次。不是单凭北京时间周末推零。四类主要及补检主题（language/foundation model、Transformer/MoE/RL、GPU/训练推理、Agent/RAG/多模态/world model/VLA）限定本窗检索没有恢复确定非标准公开事件；cs.LG2602官方月列表一次web读取失败、native404，止于失败，不将宽分类全量变成题摘队列。非标准提前公开/历史列表缺口保留，不作全网零论文保证。

## 潜力及代表排除

1. GLM-5 Technical Report：Zai Research目录标2026/02/21，摘要包含attention、异步RL等主线潜力；同一arXiv2602.15763原abs仅v1 Submitted17T17:50:56Z、v2 Submitted24T10:44:44Z，当前没有撤回/纠错说明。DataCite Registered18T02:49:09Z只作为该公开身份已经存在的窗前上界，不当作首公开精确时刻；目录晚收录不重移v1归属。README本窗commits为空，不能单凭空commits证明所有artifact无变化，但没有具体重要修订信号，结束同家族本窗重复发现，不重评机制。若以后出现21～22原始修订差额，只定点重开差额。
2. Anthropic Frontier Safety Roadmap：核心说明的security/safeguards计划相关，但官网RSP timeline明确February24引入新的Roadmaps/Risk Reports，正文February22只是capabilities snapshot；本窗不评分，不采用后续页面计划作为本窗事实。不能把成熟安全治理词汇转为新机制。
3. Our First Proof submissions：OpenAI原RSS20T14:30Z=20日22:30BJT，窗前；领域数学研究按ROADMAP AI for Science暂缓。没有读全文，不把其科学结果转到Evaluation重新准入。
4. HKUDS/nanobot v0.1.4.post1：原release Published21T13:09:50Z=21日21:09:50BJT，落窗。核心说明中的provider/cache/media/refactor是已有工程能力接入；#866只把history_entry/memory_update的结构输出从JSON修复改为string型tool arguments，代码仍直接读取首toolcall参数，并不建立新的记忆正确性或授权保证；没有独立新机制/有效边界，贡献关闭，不评分。安全标签具体定点核#824及#820：#824公开帮助文字直接回复不调用Agent，不扩大/new授权；#820将format词匹配收窄为命令位置以修误报，不支持shell安全保证，测试也不是绕过证明。只核这两个实际信号，不遍历全部PR。
5. can1357/oh-my-pi v12.16.0：原release Published21T14:00:02Z=21日22:00:02BJT；首批搜索所得abort工具提示不在本次release，已按actual release纠正。实际#126新增schema适配：draft2020-12的$schema及nullable经draft07 AJV被拒，递归消毒路径改变tool调用兼容性。准入待独立校准；拟最小采用是消除元模式报错不等于跨方言语义等价，拒绝作者“任意server兼容”扩张。直接原diff表明nullable未转换为包含null的type，而且递归会删除同名业务properties；这两项仅由静态实现支持，不声称跑过项目或生产复现。

独立校准后#126保留2+2+2=6，标准完成，Ch83具体adapter/effect/contract-test漂移已有覆盖，不改书。root另指出release中#851/#823两条执行可靠性信号；作者实际定点body/唯一diff：#851只增加kill后5秒bounded wait，timeout pass仍返回相同错误，不证明进程子树结束或fd闭合，不改变终止确认/重试边界；#823同loop session-key set单飞/finally清理，恢复成熟去重机制，不是跨进程durable互斥/原子memory commit。两项按实际增量贡献关闭，不以测试空缺为拒绝理由，也不扩其他PR。

未新增其他日期候选；日期未知且潜力明确的事件不得先列确定候选。root已实际回核#851/#823并通过六部分日级复核，普通待办0；本笔记只保存原始来源与筛选依据，完成状态以正式日报为准。02/22作者结束，不自行接下一日。
