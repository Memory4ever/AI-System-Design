# 2025-11-18 独立日级复核

复核者root，非作者；作者Carver。实际复核截至2026-10-04T21:19:03+08:00（工具时钟）。本记录汇总分批实读，不以作者完成标签或格式检查替代原文；恢复时重读当前AGENTS、研究合同、Report合同、Daily来源、Prompt与ROADMAP。

## 查询、准入与反侧

本日四主题原XML及receipt实际核：21/9/1/13条、44返回/41唯一；短页停止。cs.DC `skip=50/show=50`实际50标题仅查漏定位，不授全类覆盖，不把338条月库变成审阅分母。原查询和七组web补检输入保留，DataCite仅身份/日期。

35份精确v1完整题摘实际读过，包括多段摘要；10876/10909/10899另补读未在第一次输出完整显示的段落。全部潜在贡献及九份AB关闭理由核过，不仅抽读首批；另六项只按原列表明确领域标题关闭，未声称读它们完整摘要。当前Atom/abs可见评论轻量未命中撤回、勘误等，不代表核完整版本史。

纠正一项共同理由的实际反例：2511.11472 Conformal的难度排序、均匀质量分箱与组条件阈值，直接挑战不均衡样本难度使评价失真的学习/不确定性解释。不能因ImageNet或不是大语言模型而关闭。作者已撤销旧范围理由，恢复潜力，计数为26论文+Antigravity公告=27潜在家族；它们尚未获得落窗证明，不是确定候选，也未评分。

九份AB关闭是领域应用/已有模块组合而无足以改变本项目判断的具体增量；保留原题摘与逐项原因，不把关闭解释为论文无学术价值。六标题关闭涉及雷达、航天轨迹、领域考试数据、医学与图像复原等明确切片；未将未读方法描述为已经核实。没有因Books已有覆盖、后续审阅耗时或日期受阻缩小潜在池。

## 必要原文实读及权限

以下为准入和必要反侧核查，不授全部方法/证明/实验正确性或论文性能：

- [11553v1](https://arxiv.org/html/2511.11553v1)：实际§1/2及Assumption1。固定Q/K/V、unit sphere、time对应层深及infinite-depth ODE，V对称/正谱与最大特征值简单等假设限制结论；不是训练参数收敛理论。保留多稳态潜力，不转成任意Transformer必然行为。
- [InsideVOLT 13751v1](https://arxiv.org/html/2511.13751v1)：实际§4.3/5.2。IR层规划之后，late branch inversion、predicate reload和divergent select等仍可能破坏split/join；last-MIR safety net有具体正确性职责，不仅抽象层次描述。psort指令增加及ZiCond访存密度导致部分负载变慢亦保留；SimX条件不证明普遍生产加速。
- [HPCAgent 10860v1](https://arxiv.org/html/2511.10860v1)：实际§3.2/3.3/3.4、§4.1.1/4.7、§5.2/5.3及相关Table3。HPCBugKG→AST并行模式→测试recipe→执行反馈有具体增量。Listing3的`ASSERT_FALSE(is_consistent)`与描述一致结果应通过存在文本矛盾，不能据此授oracle正确，也不能断言真实代码已被执行验证。多个模型/至多五轮候选预算不支持脱离配置的公平因果收益。
- [Conformal 11472v1](https://arxiv.org/html/2511.11472v1)：实际§3与Limitation。扰动后的预测稳定性估计难度、uniform-mass bins及组条件阈值支持保留机制潜力；TSS仍受基分类器精度和ground-truth rank分布影响，不能当无条件自适应保证或临床结论。
- [Negative Bias 10881v1](root-core-2511.10881v1.html)：实际相关context/IDK/CoT分析与Discussion；context不必消除冲突，IDK收益在模型间不同，CoT可加重否定偏置。知识探测与attention分析不证明因果归因；这些反侧已核而非仅重复摘要。
- [LLM Grader 10819v1](root-core-2511.10819v1.html)：实际§4配置和§5。固定GPT-4o调用、人类评分的分工作业与rubric条件；高总体相关并不意味着258份回答逐项评分一致，过高/过低分及均值偏差必须保留。不能将两位评分者误作每份双重独立标注。
- [Collatz 10811v1](root-core-2511.10811v1.html)：实际训练设置涉及奇数输入、固定seq2seq结构和多进制实验。计算结构的局部泛化有潜力，非解决Collatz猜想或通用LLM数学可靠性；只核收到的训练设置段，不声称完整反例/证明已读。
- [Honesty 11500v1](root-core-2511.11500v1.html)：实际§3.3交叉惩罚评价及§6.1。有限惩罚格点并非全部对角最优、单1.7B和可验证Kn/Knpuzzle的边界，不支持全局Pareto最优或任意领域的诚实保证。

TIM10899和MMA10909身份、精确v1及采用边界未变：复用root在17日实际读过的受影响必要核心，不继承17日来源或日级完成。TIM仅高风险工具/过程偏置受限结论；MMA仅随机测试、舍入/subnormal等数值规格局部，不当完整厂商ISA。其他日期隔离潜在项不要求逐篇全实验或全owner对读；必要原文不足时没有授正面采用。

本日root八次native HTML恢复的receipt保持原始错误：11553/13751/11472/10811有HTTP200但curl28的部分响应，不能写成完整下载。前三者必要段另由官方web精确版本实际读到；10811只采用实际收到的设置段。10860/10881/10819/11500 native curl0可读，未执行代码/benchmark。

## 十四来源与日期边界

实际核各源原响应身份、receipt、可见目录/解析结果和停止位置，而不是只读作者SOURCE_REVIEW：

- OpenAI：Research403、1245条RSS/日期缺失0，本窗唯一Gartner公告原核心只商业认可。原厂商声明明确Gartner意见不是事实或背书，不当独立技术评估。完整RSS只作本窗段，不授Research全站。
- Anthropic：实际Flight一chunk、0T、172日期身份；Nov12至Nov21邻接，本窗无条。未读172份文章，不声称全站。
- Google：实际p4/p5各24标题和重试receipt，目标邻接与旧条日期；Gemini3/Developer及Nano/ImageVerification原JSON-LD明确窗外。Antigravity原核心artifacts/async Manager/Editor/反馈/derived knowledge可留潜力，Nov18无时区不移植Gemini时间。pubs失败及实际补检是历史缺口，不是零论文。
- Meta/Qwen：连接重置/动态壳/0行原返回及目标補检无有效历史；Qwen旧站有限五条不代替新站历史。
- DeepSeek：真实Research More/news，10 Research/5 Dynamics，Nov27→Nov1目标两侧；只此有限目录，View all未操作不称全历史。
- Moonshot：实际26原title/date，最新Nov7/Nov6至2024May29，无本窗事件，不展开全GitHub。
- Hunyuan：原动态壳、浏览器不支持visibility及30秒超时的实际记录、API九条2026原字段；不是2025历史覆盖，不重复无限重试。
- ZAI：实际两页Flight/可见日期，p2 terminal只到Dec7，不能证明11月零事件。
- Seed：四原JSON/真实参数、74个原标题/PublishDate/pin、next40与has_more=true实际核过；未来置顶不作本窗新发布，非置顶旧侧足以有界停止，不称全年全读。
- ERNIE：实际10+6标题/date及真实Next2/2 terminal，Nov21→Nov11邻接。
- MiMo：实际Paper八项、Blog十五标题；新增原首页8557及6159 chunk确认`initialVisibleCount:8`、两次slice、余七项已map、More仅布尔toggle/data-expanded。关闭未操作More的普通分页待办，不声称实际UI点击，也不授无日期数组为2025Nov全量历史。
- MiniMax：EN12/CN13、独立Agent首页/原Markdown和真实llms入口；52物理行/49非空不是文章数，只一篇2026Tech文章，2025历史保留受阻。
- arXiv：上述四窄主题和cs.DC有限标题查漏，原abs/current-comments轻量标记核查；submitted发现范围不是首公开窗口。

本日全部原DataCite字段及可见版本历史实际核过；新增Conformal v1 Submitted/Updated/created/registered和精确补检输入亦核：它们不标示首公开。Available月精度与Sunday–Thursday20ET公开规则不能凭空补09:00。InsideVOLT Nov19及2601 ID/Jan Available的特殊情况明确隔离；后者不可能是11月arXiv首公告，但别处家族初次发布未知。Conformal补检实际空，不代表不存在公告。

七历史源缺段、26论文首公开与Antigravity时区保留项有身份、失败范围、需要的替代材料和单项重开位置。不得用于正面证据、Books、无遗漏、安全或性能保证；不是未读方法的替代标签。其他月份/Weekly不在本次范围。

## 日级结论

**通过。** 实际日期确定候选0、正面Evidence采用0、Books判断No Change/写入0。27潜在家族不是已评分或已采用；各自日期缺口安全隔离，本窗普通可执行工作已收束。准入恢复Conformal、MiMo行为及必要机制反侧同步均实际核过。作者可同步完成字段、§1/5/6及本记录引用，再运行最终V3与自写Markdown/本地引用/diff检查；未同步前不计入月度完成数。

没有声称完成所有论文证明、复现实验、全网站覆盖或执行部署；未stage、commit、push。
