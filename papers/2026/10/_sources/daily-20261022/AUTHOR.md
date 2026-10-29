# Daily 2026-10-22：作者机构记录

root为唯一README/Books/LEARNING_STATE作者，oct22_reader为非报告作者。窗口仅2026-10-21北京时间自然日；Oct21未完日报保留原停点，不搬其候选/覆盖结果。本次Thursday不生成Weekly，live未完成前不推进历史cursor。已重读AGENTS、当前研究/Report合同、Sources每日和arXiv主题、统一Prompt及ROADMAP。使用context-engineering维持单日上下文，未修改合同或工具；不stage/commit/push，保护运行前已有暂存和并发修改。

## 原始请求与有限范围

2026-10-22T09:05:45～09:05:47+08:00，12个实际官方请求均HTTP200，原始响应保存为同目录`<name>.raw`：openai799474B、anthropic397497B、anthropic-engineering391214B、deepmind29819B（原始gzip，已先解压再读，不将乱码当空页）、google-research175563B、meta233521B、meta-blog211066B、qwen4781799B、deepseek52380B、moonshot13388B、kimi-code172675B、moonshot-github310406B。本节是实际取件范围，不表示每个业务目录/日期与候选都已处理。

- OpenAI：[RSS](https://openai.com/news/rss.xml)1312项逐项pubDate转BJT，目标日7项，见下文；没有用抓取时间或submitted当公开日。
- Anthropic：[Research](https://www.anthropic.com/research)按Most recent首段最新Oct20蛋白binder，下一Oct16/13，已到窗前；[Engineering](https://www.anthropic.com/engineering)最新Oct13。未把特色卡/旧2025 Oct20字符串误当目标2026日期，不重读窗外科学应用。
- Google Research：[October目录](https://research.google/blog/2026/10/)实际9项，日期依次Oct21/16/14/14/14/7/6/5/2；唯一Oct21为maternal-care ultrasound，标题明确健康领域应用，当前AI for Science暂缓，无当前可见纠错/安全信号，不以Machine Perception分类重引。DeepMind本次最新October六卡的必要原始日期仍待核；Publications日切片尚未检查，不以Blog代全目录。
- Meta：[Blog](https://ai.meta.com/blog/)当前latest首组Jul27/Jul21，到窗前停止；[Research](https://ai.meta.com/research/)只取得静态bootstrap、未取得动态论文列表，保业务范围缺口，HTTP200不当零发布。
- Qwen：[article/retrieval](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)实际40条，逐项读extra.date及正文datePublished，全部窗前（最新Sep20）；部分旧日期字段冲突保持原值，不搬日期；不假定API按日期排好，不称所有渠道无遗漏。
- DeepSeek：[官方updates](https://api-docs.deepseek.com/updates)最新Oct17，下一均窗前，未将旧searchAPI当本日新事件。
- Moonshot：[Platform Blog](https://platform.kimi.com/blog)26项最新2025Nov7；[Kimi Code更新](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html)真实Oct21 Desktop v1.1.1/CLI v2.3.0核心已读，下一Oct14停；[官方GitHub](https://github.com/MoonshotAI)首10/42里kimi-code更新Oct21、MoonEPOct12，其余窗前，更新时间不当发布证据，明确版本来自What's New。

## OpenAI目标日七项与准入拟判

官方RSS和各已读原页均为Oct21；网页工具可读官方正文，不伪称本机原HTML已保存。

| 原始材料 | 拟判断与具体理由 |
| --- | --- |
| [OpenAI on Google Cloud](https://openai.com/index/openai-models-google-cloud/) | EX：实际核心仅未来Model Garden/Marketplace接入与购买/数据治理承诺，GA还在未来；未披露新的模型/infra机制或足以改变设计的受控边界，不以企业/平台映射准入。 |
| [Patch the Planet协调披露](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/) | EX待安全信号校准：已读核心协调框架/维护者决策、patch测试、提前信息与部署阶段；AI用于PHP漏洞发现是应用事件，未给新增模型安全机制、受控有效性条件或AI系统纠错。保持发现≠部署边界，不把全球影响/资金或宣告严重性当研究增量。若正文具体改变AI-agent安全/发布合同应重开该事实，不泛扫漏洞/利用代码。 |
| [Cloudflare案例](https://openai.com/index/cloudflare-cyber/) | EX：源码调查加live traffic/security signals、patch/WAF提案与人工审核是部署组合，未给新机制/受控条件或因果评价；不采用10x/3天营销成本数字，不以安全题目本身保留。 |
| [Empowering cyber defenders](https://openai.com/index/empowering-cyber-defenders/) | EX待安全信号校准：核心为政府/业界责任与关闭/报告/恢复的政策倡议，不是已执行的新系统接口、标准或受控技术研究；无须为未采用的政策愿景追整份blueprint。 |
| [生物数据多Agent](https://openai.com/index/scaling-ai-research-for-complex-biological-data/) | EX：题目与摘要/栏目明确生物科学应用，AI for Science当前暂缓，不借Multi-Agent通用节点引入。 |
| [Ads扩国](https://openai.com/index/chatgpt-ads-expands-26-new-countries/) | EX：商业地域/客户规模，不是系统机制。 |
| [Ads stack工程](https://openai.com/index/building-chatgpt-ad-stack/) | 拟P：单请求不能解释增量对话中的过期intent与交付时限→独立状态化LLM ads服务只提名/工具auction裁决、晚到不展示→明确producer/decision/display与主回答不等待的边界；不是因广告收入或ANN名字准入。初评2+2+2=6，需唯一reader校准与具体owner比较；分服务是厂商披露，不授零影响/隔离证明。 |

## Kimi Code Oct21发布：首批拟P

官方What's New中Desktop1.1.1与CLI2.3.0同日，按同项目发布家族处理；只采用相关兼容/权限机制，不借UI修复扩审阅。未信任workspace拒绝后阻止发送；插件skill改为plugin-id:skill-name，bare name不再可用以消除同名shadowing；/reload显式重新加载外部修改的AGENTS/skills/config，model switch提示新session/compact/直接续。拟P：同名可执行能力与会话中配置变化可改解析/权限→具名寻址、workspace trust与显式会话重载→不把磁盘新规则当已激活context或同名能力。初评1+2+2=5；是公开版本合同，不证明实现、sandbox或全部旧会话安全，也不因本案例与本项目上下文问题类似就扩写。

以上两P、七项中的安全相关EX均待独立校准；未写Books、未冻结完整候选分母或预签Daily完成。中国六来源与arXiv各有独立作者文件，尚未冒完成。

## 两项机构必要Source与具体owner拟稿

reader R2已一次校准两P与三安全EX；Patch正文额外blocking classifiers“正在校准”是需识别的安全信号，但未披露机制、生效契约或可比结果，原EX保持，不因security标签全文扩池。root实际读Books三上下文、Ch84完整技能解析段及Scheduling局部/MegaFlow完整段、Ch83开篇，唯一owner均拟`AGENT-PLATFORM`，不复制到Memory/RAG/基础设施调度。

### Ads：2+2+2=6，具体可选旁路与交付时限差额

官方工程核心“Conversation memory”“orchestrator”“auction”“final checks”“showing”已读：独立服务/模型消费对话，orchestrator提名，auction定最终选择/价格，前端还验是否及时到达。原文不同位置的delivery用语不完全一致，故只采用三个非等同事件，不补造唯一ACK状态机；宣称主回答不受影响只是作者架构合同，非独立隔离/故障证明。无公开延迟/质量受控实验或实现核验，不采用收入/广告数量/ANN速度数字。现有Ch84有run/effect分权、资源域与实例生命周期，却未承载可选辅助Agent迟到即不展示、主回答不等待的具体服务交付分支。拟在Scheduling完整MegaFlow段后/Harness标题前：

> 还应区分必须完成的任务分支与可以错过本轮机会的辅助服务：后者不应仅因已经选出结果，就让主回答等待或自动取得展示权。[一种状态化对话旁路](https://openai.com/index/building-chatgpt-ad-stack/)由独立服务和模型持续读取更新后的intent，LLM只提名候选，auction工具决定选择与价格，前端仍可因不合时宜或到达太晚而不展示。于是提名、选择和可见结果是不同事件，“没有辅助结果”可以是合法终态，而不是主任务失败；这不同于必须等待全部依赖的workflow。独立服务不自动证明故障、资源或信息流完全隔离，仍要支付上下文更新、重复检索、工具调用、资格检查与丢弃过期结果的成本。只有可选、允许降级且主路径不依赖其结果时才适用；必要证据或有外部副作用的步骤不能照搬晚到放弃，应保留原依赖/权限与commit验收。<!-- source-family:SF-2026-OPENAI-ADS-STACK-20261021 -->

拟本人注：官方Oct21工程说明，必要core见上；2+2+2=6，Agent可选旁路时限/提名-选择-展示差额深入。不从分服务签零故障影响、隐私或统一ACK协议，不采用商业/性能数字，未核实现/复现；待reader必要Source/owner/PRE和实际POST。

### Kimi Code：1+2+2=5，命名与会话激活边界差额

版本页核心已读；这是新TS Code CLI及Desktop的版本合同，不把其与Python Kimi CLI1.39的旧first-win顺序写成无条件线性替代。当前Ch84已有asset digest/first-win/admission，缺namespace迁移的兼容边界和磁盘修改≠本次session已激活的区分。拟在旧解析/信任完整两段后、Competence标题前：

> 对插件提供的同名能力，另一种选择是让调用显式携带namespace，而不是只依赖first-win顺序。[Kimi Code的受限版本合同](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html)将插件Skill写成`plugin-id:skill-name`并停止接受bare name；这减少同名遮蔽，却新增旧调用迁移与名称绑定维护，名称也不等于artifact可信。规则还存在激活时点：文件中的AGENTS、skills或配置已修改，不表示当前会话已消费新版本；显式reload把重新装载变成可见操作。该发布同时以workspace trust拒绝阻止发送，但没有说明这会撤销全部在途工具或提供sandbox。平台仍须把所用定义/解析结果绑定到run，独立执行effect授权；重载原子性、旧调用兼容或来源无法确认时，固定已验版本、重建会话或保留封闭能力集，而不以一次reload宣称全部历史状态已安全迁移。<!-- source-family:SF-2026-KIMI-CODE-20261021 -->

拟本人注：官方Oct21 Desktop1.1.1/CLI2.3.0核心；1+2+2=5，namespace兼容与磁盘/会话激活差额深入。保新旧产品版本范围、workspace拒绝只阻止发送、无在途撤权/原子reload/sandbox证明；未核实现/复现。待reader必要Source/owner/PRE和实际POST。

## 实际采用与机构尾段

上述两项已按reader R3分别真存Ch84；Ads已将适宜性检查与前端晚到分责，不沿用拟稿旧句。reader R7实际顺读完整新增/完整局部邻接及本人注，POST均通过，窄位释放；本记录不第三核有效层，不授DAY。

Google DeepMind October六卡的日期尾核：Argon介绍Oct13、scam Oct14、robotics Oct13、embedding Oct6；剩余[安全说明](https://blog.google/innovation-and-ai/technology/safety-security/gemini-4-model-safety-security/)官方正文日期Oct13（实际网页L214–220），antimicrobial明确暂缓科学应用范围。到September组停止，不把月份卡当Oct21。Publications当前原始HTML及实际网页仍只提供year/topic目录（2026总423），未提供日级公开过滤；两条有界站内搜索`site:research.google/pubs/ "2026-10-21" "language"`与`site:research.google/pubs/ "October 21, 2026" model`只返回Blog，不证明无论文。该日级缺口不靠读423全年条目消解；隔离为不支撑候选或零发布断言的保留项，恢复条件是原始带公开日目录或具体窗内论文的官方公告/版本信息，定点核相关项。

Meta Research本次HTTP200仅bootstrap、网页提取0行；当前确有可用IAB browser，创建隐藏Research页的实际导航在36秒超时并reset，未取得动态论文目录。不能沿旧记录声称没有浏览器，也不能把空提取当无发布。Blog实际latest Jul27/Jul21到窗前；动态Research目录隔离为外部保留项，不支持覆盖完整性或候选断言。恢复条件为可加载的官方目录/日期API或明确论文原始发布，不扫无关组织历史。

本日后续有限恢复：对已有Research URL再次调用IAB getTab，实际34.4秒导航/状态恢复超时并reset，未取得页面，不是可继续读的“已打开目录”。另两条精确日级补检`site:ai.meta.com/research "October 21, 2026"`与`site:research.facebook.com "October 21, 2026" paper`均无结果；索引空不能当零发布，也不由此扩扫年度论文。保留同一外部缺口/重开条件，不再重复同一失败浏览器路径。

## S1 — 2610.28369：动态expert skipping的静态对照与实际预算

精确[HTML v1](https://arxiv.org/html/2610.28369v1)已取原件`root-2610-28369v1.html`，2026-10-22T09:20:58+08；实际读§3.1–3.3/§4.1–4.3.3/Table1–2/§5–6及直接相关A.3/A.5/A.6/A.7/A.8反侧（未声称全附件已读或代码已运行）。官方cs.AI/cs.LG pastweek列表该身份上方均为Wed21，原件在arxiv-originals，不能以v1 submitted Oct20挪归属；当前页无撤回cue。

2+2+2=6：具体新增是静态top-k与per-modality静态控制在实测Keff匹配后难被四种动态策略稳定超越，以及校准Keff受模态配比/score分布变化而失配。Keff只计expert activation，不含router/负载/通信，也不等真实wall time；公平对照需给静态baseline同样的modality结构信号。文本Qwen3-30B-A3B/Gemma4-26B-A4B、multimodal Qwen3-VL-30B-A3B-Instruct，lm-eval/LMMS-Eval，训练集最佳/混合calibration都未使动态策略普遍胜出；局部NAEE/Allocator、MME-Cognition与sub-one-Keff为真实反例，不能写静态一律最佳。作者部分方法为尽力重实现，Ada-K无公开code/checkpoint；该限制与PPO随机性不支持全方法已被彻底否定。

采用命题不需要速度数字：仅补§3–5支持的baseline与校准/实际预算区分；A.5单A10080GB、vLLM/GuideLLM chat、batch1/256、120秒是静态上界场景，不是动态skip实测部署，precision、长度分布、concurrency/SLO未在该域披露，不外推吞吐；不借Keff下降授同比E2E节省。校准费用、路由决策与raggedness均额外付费。未核实现或复现。

唯一owner拟`MODEL-MOE` Ch21，已读其L245–285完整“compute leverage”/位置减配及下一架构预算交接、Ch20/22开头。现有段已要求expert/整网FLOPs、prefill位置预算与质量/全生成验收，但未具体要求dynamic skipping对同模态静态控制、以测试实际Keff而不是calibration目标对齐。不是已有主题就NC，也不复制至推理调度。拟在位置减配完整两段后、扩大容量标题前补：

> 降低expert预算还应先比较一个更简单的分支：保持原router排序，只把固定top-k减小；多模态时，静态对照也应允许分别设置文字与视觉预算，而不是让动态方法独占模态信息。[有限受控比较](https://arxiv.org/html/2610.28369v1#S3)发现，多种动态skipping并未在匹配测试期实际expert调用数时稳定胜过这种静态控制；这不否定局部任务、极低预算或其他模型上的动态收益。校准时的平均激活数也不是部署预算：输入模态比例与routing-score分布变化，都能让实际调用数偏离目标。因而应比较质量—实际调用前沿，再测完整执行费用；router计算、ragged dispatch、通信与校准成本不能藏在激活数之外。固定减配不需校准且形状稳定，但可能损伤生成任务或少数模态；低预算质量崩溃、分布变化或净费用不合算时，保留原top-k或较小dense模型，不把这组受限反证升级为静态策略普遍最优。<!-- source-family:SF-2026-ARXIV-2610-28369 -->

待reader必要Source/owner/PRE，不预Books写入或整日验收。

## S2 — 2610.27895：DPO选择目标、跨规模迁移与部分训练proxy

[精确v1](https://arxiv.org/html/2610.27895v1)，原件root-2610-27895v1.html已取；实际读§3完整实验合同、§4.1–4.3/Fig2–5/Table1–2及§5–6限制。官方cs.AI/cs.LG Wed21列表直接确认本窗，当前abs无撤回cue。2+2+2=6，采用有限grid中loss/规模/数据迁移不是可靠选择proxy的具体证据，不采用普遍最优超参或HPO加速宣传。

Qwen3五规模0.6B至14B，固定Dolci SFT后主DPO数据Dolci、替代UltraFeedback，共享3×3 LR/β core并扩各规模局部grid；静态7任务与chat4任务分别aggregate，后者两judge。DPO loss跨β不可直接等值比较的混杂，作者又在固定β内比较LR，仍出现不稳定相关；chat排名一致不等真实质量，0.6B两judge相反，共享偏好未排。共享grid目标/排名随scale与dataset变化不等全域最优逆转：最优位于边界时只能说tested-grid偏好；各run单训练seed。部分target-model训练能提议排序，不是固定30%早停保证。四拟合surrogate/25搜索seed的HPO试验是离线模拟，不是新训练run或训练seed变异；其预算不含evaluation。没有采用速度/省费数字，不需由未知GPU/长度/SLO推断部署收益，完整train/eval/search成本均保留。未复现。

具体owner拟TRAIN-DPO Ch34，实际读L193–235完整Beta语义与后续scale解耦论证、Ch33/35开头交接。现有段讲公式/实现convention、不能换数值/“安全旋钮”，并解释β影响梯度，却未有“固定公式仍不能将近邻规模/偏好数据的赢家当默认或以val-loss选”的具体对照与有限early-target proxy。拟插Beta非安全旋钮之后、Preference/Optimization Scale分拆标题之前：

> 对齐公式后，配置仍须针对实际目标选择：较低DPO validation loss不必对应更好的对话、推理或约束遵循，近邻规模与另一偏好数据集的赢家也不自动可迁移。[有限同族网格比较](https://arxiv.org/html/2610.27895v1#S3)在固定SFT起点、共享learning-rate/β网格下观察到这些排序变化；固定β后仍有loss代理失配，不能只归因于跨β的loss尺度。可把旧配置当搜索起点，以目标模型的部分训练和多项行为评价缩小范围，再验最终checkpoint；部分轨迹只是筛选proxy，不是统一早停规则。边界取值不证明找到全域最优，chat judge一致也不是真值，单训练seed与有限模型/数据不能建立普遍缩放律。联合试参、生成、judge及回归都付费；预算有限且目标稳定时保留已验证recipe，目标改变或proxy失效时收紧局部搜索，而非沿一个较低loss自动发布。<!-- source-family:SF-2026-ARXIV-2610-27895 -->

待reader一次必要Source/owner/PRE，未写Books；主张不涉及HPO方法优劣或普适超参。

## S3 — 2610.27590：随机输入替换的收益依赖停止点，不等于消除记忆

[精确v1](https://arxiv.org/html/2610.27590v1)，原件root-2610-27590v1.html；实际读§3–8/Table1/5、limitations以及C.4–6直接早停/weight-decay/重复epoch反侧。官方CL/AI Wed21列表直接日期，无当前撤回cue。2+1+2=5，新增同目标、同固定recipe下停止点/噪声bias与后期loss回升分账及记忆反侧，不借通用正则原则加分；具体长期差额深入。

uniform random vocab replacement只改input、target不变，主p=.15；134M/336M从头训、10k steps constant LR，主语料重复到22epochs，真实语料多三seed，loghub/road只有两seed。受控一阶Markov已知entropy，APPROX/EST/MEM是abundant-data/min/final三个参照损失的operational分解，不能冒充任意真实语料的唯一因果分解或经典bias-variance恒等式。替换降低部分后期held-out回升，但训练loss仍低、50token逐字复现比例还上升，所以不能写成不记忆或隐私保证。真实语料minimum收益小/异向，census负、SQL和log等部分统计不显著；known-source预期收缩bias与真实corpus可识别噪声不同。跨corpus有token/重复dose混杂，census唯一伤害不能给gzip通用阈值，英语同recipe control仍缺；高scale不可外推。C4最小loss是事后曲线读数，早停patience1/3常漏最低点，不能自动当实时stop-policy。未采用论文loss百分比/时间收益，不授部署质量或复现。

已读Ch28相关Memory Dial完整段、数据受限标题附近和L1630–1655 KItCAT输入corruption完整段与下一结构化code重建交接，邻Ch27/29开头。具体owner TRAIN-PRETRAINING已有输入噪声和target不动、完整held-out/能力验收，但缺停止点与“较低后期loss不表示少逐字记忆”的直接反侧。拟在KItCAT完整输入替换段后/结构化重建之前补：

> 这种输入扰动的收益还取决于拿哪个checkpoint比较。[有限重复数据实验](https://arxiv.org/html/2610.27590v1#S3)中，随机替换主要减轻最低验证loss之后的回升；在各自最佳checkpoint处，收益可能很小或为负，逐字复现训练片段却仍可增加。因此“正则化改善后期验证loss”不等于减少所有记忆或取得隐私保护。已知熵的受控源可用充分数据、最低点和最终点的参照损失分账，但真实语料的可预测性、重复剂量和噪声可识别性混杂，不能按压缩率给通用启用阈值。曲线事后最低点也不自动等于在线早停能找到的点；较慢下降还会被过短patience误停。扰动、更多验证和试参都付费，较大模型、接近最佳点或语义敏感输入上仍要重验；普通clean-input训练、经验证的早停与较低噪声继续是合理分支。<!-- source-family:SF-2026-ARXIV-2610-27590 -->

待reader必要Source/owner/PRE，未写Books。

## S4 — 2610.27889：harness提升的有限尝试覆盖，不等于能力支持扩张

[精确v1](https://arxiv.org/html/2610.27889v1)，root-2610-27889v1.html；实际读§3–6的评价setup、完整trajectory多次尝试、总体/难度/域移结果与显式heuristic反例，不采用疾病/化学应用结论。官方LG Wed21确认日期。2+2+2=6；标准Source备，拟NoChange，不因已有覆盖降分或否定新验证价值。

固定solver优化harness，在相同test/task-specific scorer下重复完整执行；HotpotQA300/固定BM25，Qwen3-8B vs32B；AppWorld168，GPT-OSS120B medium vs high effort，对比不是只换harness的同总compute因果实验。pass@1是平均成功率，pass@k是有限尝试至少一次，二者可交叉且受难度切片；有限预算未到达不证明分布不支持。不同优化run与硬任务上有反侧，原文§5.2图号有自指重复，不靠图号错误补造数据。域移代码可暴露多标签输出heuristic与单标签目标冲突，但仅一inspectable例不是所有域移唯一因果。更大attempt budget还增加资源；k相同也不保证token/model/tool总费相同。本次不采用性能数字或harness普遍替代scale结论，未核实现/复现。

具体拟已有覆盖 `PLATFORM-EVALUATION-SYSTEM`：现已实际顺读Ch66 L2312–2345完整single-run/pass@k/pass^k、预算人口与curve crossover的paired simultaneous band论证及L4178–4202“有限pass@k未到达不等支持集外”完整反侧，也读Ch67开篇承接，Ch65交接尚待。有限抽样覆盖与普遍能力支持、较高均值与较广覆盖正是现有正文已承载的判断；本篇harness新实例不改变其边界，不为追加论文名制造段落。待reader一次必要Source及具体NoChange，不以搜索命中冒Books对照完成。

S4邻接补核：已从ROADMAP正确定位并实际读Ch65 KAI Scheduler小结（不把不存在的65-kubernetes路径当已读），其负责placement/隔离比较而非测量定义；Ch66→67继续由评价合同交接监测状态。此前“Ch65交接尚待”现已补，未改书。

## S5 — 2610.27241：relation readout须先排实体与首token捷径

[精确v1](https://arxiv.org/html/2610.27241v1)，root-2610-27241v1.html；实际读§4 Eq5–6/method、§5主模型/关系人口、§6主对照及cardinality/frequency/type控制、§7.3相关干预设计、§8.1–8.3完整reference竞争/弱首token反侧及§9首限制。未读完全部附录或所有跨模型表，不冒称整论文全文审计。官方CL Wed21身份已核；当前v2只metadata correction不重复计重要修订，不假定未说明的任意新版逐字相同。

2+1+2=5，具体增加relation-agnostic Jacobian entity readout作为LRE faithfulness负对照，不借一般“probe不是因果”原则加分。CEL用同type reference差分，NEL去参考差分；相同neutral“is known for”prompt不含relation模板或object pair，主OLMo3-7B与预定28 named-entity relations。relation级相关不证明LRE确实消费该读出；fact级弱/反相关、subject同名竞争、University等共享首token及cardinality范围限制均为必要反侧。交换subject/anchor只覆盖特定正确回答两对关系，不代表普遍因果证明。更完整answer/entity评价是建议而非本文已实现解决方案；不采用相关系数/效率或全模型机制结论，未核代码/复现。

具体owner拟`WORLDVIEW-REPRESENTATION` Ch5，已实际顺读L62–94完整表示/语义图、relation-frame及object身份干预论证，邻Ch4/6开篇。现有段讲可读几何不等唯一算法、对象更新可能用错identity，但未讲“不含关系的实体读出已预测关系线性faithfulness，首token答案又不够区分完整对象”的两项诊断。拟在语义图诊断完整段后/relation-frame干预段前一段：

> 判断模型是否表示了某种关系，还要先排除实体本身和答案格式已经提供的捷径。[一种关系无关的读出对照](https://arxiv.org/html/2610.27241v1#S4)只用中性实体提示与同类reference、不输入关系模板或答案配对，仍能预测部分关系线性读出的faithfulness；这说明高读出分数不唯一支持“模型学到了该关系映射”，不是证明关系完全不存在。主体名称可能被模型解析成另一实体，多个完整答案也可能共用“University”之类首token；首token答对不能认证完整事实。应分开检查实体消歧、完整对象与关系条件，并保留reference集合、层和对象数量这些测量条件；这些改进是待验证的评价方向，不是该研究已完成的通用解法。读出/白盒梯度及人工校验增加费用，负对照或完整答案不稳定时，保留更窄的表示判断与独立行为/配对干预，不由相关性宣称唯一知识存储或关系算法。<!-- source-family:SF-2026-ARXIV-2610-27241 -->

待reader必要Source/具体owner/PRE；未写Books，图表/附录未读部分不支撑采用。

S5 reader R28必要采用补记：LRE选层/β使用同一批被评分subjects，faithfulness是in-sample而非held-out；§6 CEL与后文NEL-based口径不统一，本次不用其系数或唯一lens归因，只保关系无关负对照和完整对象/实体消歧的有限诊断。原一段PRE通过，实际写后仍须另核。

## D1 — 27620 accepted/extended公开资格的有限检查

已实际读精确abs Comments：仅称IEEE TPS2026 accepted paper的extended version/full proofs/appendices，未给旧公开正文ID/DOI/日期；accepted不等公开。官方本日AI Wed21列表直接含2610.27620v1。定点标题引号搜索及作者/项目名搜索只见当前arxiv身份的二手索引（把submitted Oct20写发布的页面不采为日期证据），没有据此证明无早稿。[作者当前仓库](https://github.com/anmolpandey299/al-synth)实际原页显示empty，未取得代码/旧短稿，不能授已公开artifact/独立实现。

目前没有具体更早公开正文证据与Wed21公告冲突；可采用“本窗官方arxiv v1长稿公开事件”，不写已证明全球首次公开、accepted当窗或已核旧短稿增量。没有具名旧正文就不无限遍历TPS会场/所有作者历史；若reader认为现有明确accepted/extended线索仍需要另一原件，须精确指出会改变归属的缺失命题/可用原始入口，不能仅因字段各自不证全球首公开让当前直接公告无限受阻。必要技术Source尚未读，拟7分不是Source完成或Books采用；真正旧公开全文出现时只核该关系/真实owner日，不自动搬本窗其他材料。

## S6 — 26974两种sorting算法：必要Source与Ch5窄PRE prepared

root接手S1中未委派的[精确v1](https://arxiv.org/html/2610.26974v1)，日期复用本日保存LG Wed21列表（不把submitted Oct18当公开日）；当前官方abs仅v1、无撤回/纠错说明。2+1+2=5不变。实际读§2–6、AppA.2初始化过强反侧、D.1–D.2层/heads条件与E局部outliers说明；未读完其余附件/图像像素、未核代码/复现。

必要证据：相同训练数据顺序、不同初始化的两层单head/no-position toy模型，在线新序列固定K16、AdamW/CE/60Ksteps，训练分布几乎相同低loss仍分第二attention可移除/不可移除；不能把后者当真实少一整层。Sorting小gap在短序列少见、长序列常见，两阶段路径有更好小gap能力；direct-path/second-attention hijack支持局部分工，query-side hint缩小搜索是作者解释，不授完整唯一算法证明。相对层初始化可偏向不同类别，过强第二层scale还损长度泛化；100初始化seeds的类别频率不是生产LLM概率。Minimum-finding改为有放回/允许duplicates，近minimum拥挤与重复的失败模式使排序方向反转，非任务完全相同只改一项的因果对照；coin为greedy非最优找零。D.2二head即使single-stage也可泛化，D.1四层未呈相同清晰分工，不能采“两个stage必要”或更多层必更好。E的MLP-only近等价另有两outliers。硬件/实际precision/服务长上下文SLO未披露，所有seed/sweep/干预与OOD回归计费，不采用绝对accuracy或速度保证。

owner比较：实际读Ch4三问题及初始化/优化完整论证、Ch5组合/输入可见性与MDL反例/算法faithfulness全部相邻、Ch6开篇。Ch4负责表达/优化分离、Ch5已有更短shortcut在context变化失效与early-readout不认证指定算法，却未承载**同训练loss下两种实际受训路径、长度改变稀有输入统计且不同task/head配置使有利路径反转**的具体选择条件。唯一`WORLDVIEW-REPRESENTATION` Ch5；不把微观hint另写Ch14/17，不用简单“loss不等泛化”重复已有段。拟在2609-31114完整段及独立marker后、`这些标准都不是绝对属性`前单段，待独立reader：

```markdown
训练还可能在同样低的分布内loss下选择不同计算路径，而长度变化会改变每条路径最易失败的输入出现频率。受限sorting模型中，一条路径主要依赖首层Attention，另一条借助两层分工；后者更能处理长序列中变常见的小间隔元素。但在minimum-finding任务中，两阶段路径对近minimum拥挤的弱点反而更常触发，泛化方向逆转。[必要的路径与容量对照](https://arxiv.org/html/2610.26974v1#S6)因此不支持“更简单”或“用更多层”天然更好：相对初始化可改变学到哪条路径，换成多head后单阶段sorting也可泛化，不能把stage数当通用能力等级。这些结果限无位置编码的toy任务；路径消融与受控输入应同ID/OOD质量共同验收，新增seed、初始化搜索和干预都计费。部署统计、架构或稳定性不匹配时，保留原初始化、经验证的固定模型与独立结果检查，不由训练loss相近或一条漂亮机制图批准更长输入。
```

## S7 — ReTrace 27954：必要Source与Ch81窄PRE prepared

root接手[精确v1](https://arxiv.org/html/2610.27954v1)，官方CL Wed21直接日期与当前唯一v1/无纠错cue复用；submitted Oct20不当公开日。2+1+2=5。实际必要§3–6、AppA.2、B.1–B.3及C的环境动态/RO-RTC分歧/SSIM阈值反侧；未看完整提示附件、图像像素、代码或复现。

原始增量是将恢复检验变成原成功轨迹的剩余action replay加观察检查，不仅看截图。形式定义在确定环境上比较后继state，但可执行协议改用原suffix最终task oracle；重放同一轨迹N次均成功只筛选有限稳定人口，非证明所有允许action的determinism。Goal成功与SSIM0.99联合仍不是完整state/任意后续动作等价。先收每模型on-policy成功轨迹、注错后定点恢复，排除docker/state-verification失败；不把这批条件化分母当所有自然失败。恢复距离1/5、步数1/3/10；implicit继续原任务，explicit另获target/历史或摘要、独立指令，预算和信息不相同，不据横比证明posttraining破坏恢复能力。理想恢复83失败实例的Success@5由prefix replay构造，最多重试重放3次，非实际model recovery或同执行费用。

实际endtoend有限三open模型、同backbone恢复/forward但不同prompt和step预算：forward50步；recovery每次10且最多1/3/5次另计，error detector每step调用并恢复后冻结5步。可有收益也有Evo/UI-TARS反退，不是任意模型可靠改善。Qwen3.6Plus detector、Sonnet4.6 summarizer1024token、GPT5Mini state verifier均可错；API/default与vLLM精度、完整硬件/并发/SLO不统一披露，不采用绝对速度/费用。人验150来自各oracle与替代判定**分歧样本**，12研究者分对，agreement82%/kappa.45；胜率不是全流量accuracy。86% unaffected还条件化人一致及stochastic标记子集；RO/RTC各自失效及SSIM阈值敏感保留，不能把联合有限检查当生产restore certificate。轨迹/多次重放、注错、恢复、摘要、judge、全部尝试与环境隔离计费；研究是评价框架，不授实现已验或开放世界undo。

实际owner：读Ch81 630–688联合恢复/Planarian/StateFork完整论证，Ch80反思与Ch82开篇。Ch81已要求固定context下允许后续action观察等价，不重复一般“snapshot不等恢复”。尚缺**用固定成功suffix和task oracle实现有限行为检验，同时不把其通过外推任意未来**的窄验收接口。唯一`AGENT-WORKFLOW`；拟StateFork完整段及marker后、`如果修订只影响部分分支`前单段，待reader必要Source/PRE：

```markdown
联合恢复的行为检验可以先选一条已成功的action suffix：从目标与恢复状态分别重放它，核对task oracle，并另查可见界面是否一致。[ReTrace的受限协议](https://arxiv.org/html/2610.27954v1#S5.SS2)用它补上“截图相近但隐藏状态已变”的盲区，却只验所选后续与终点义务；多次同轨迹成功也不证明环境对所有允许action确定或等价。恢复人口、注错方法、观察阈值、被排除的重放失败、恢复指令/target信息和额外预算必须保留；implicit继续与explicit恢复不能混成同条件能力对照。有限复原能增加task success，也可能因错误恢复而退步，故应分别记录restore check与新suffix的真实完成。所有重放、detector、摘要、恢复和环境隔离都有成本；外部effect不可撤销或检验覆盖不够时，保留真实checkpoint、approval barrier与reconciliation，不以一次goal replay通过宣布全环境ready。<!-- source-family:SF-2026-ARXIV-2610-27954 -->
```

## S8 — PROVISO27115：必要安全Source与Ch72两段PRE prepared

[精确v1](https://arxiv.org/html/2610.27115v1)，原件`root-2610.27115v1.html`；官方AI Wed21日期复用，当前abs只有v1/无撤回纠错cue。2+2+2=6，安全域深入。实读§3–5、C真实adapter/commit与成本、E group统计、F必要components/固定pool及校准反侧；未全原prompt/定性案例/代码，不称本方复现。

机制新增是将K可信taskcontract、G外部观察、P0原候选/P1拒绝或可执行alternative作为不同role输入冻结encoder与trainedcontroller；5queries经两次retrieve/compare，按候选nativeoutcome监督value/排序，dev选每候选offset后比较，而非逐条执行授权逻辑。Role embedding不是来源真实性证明；model读G后生成的summary内容仍外部，ToolSafe role IDs只说明描述对象，不授可信。K在skill中只是declaredpurpose，未认证它真实/合法；case风险不同。Admission risk是训练label，选threshold叫calibration但**不是probability校准**。每benchmark独立fit，不是一份checkpoint全任务迁移。AgentDojo从任务起点分别完整rollout P0/P1，在restored环境中记录再replay选定工具调用；不是在线已有effect后撤销，也不是不花费的action替换。Outcome只train/eval不可运行时读取真值；native scorer/训练标签仍可错。

必要对照：frozenModernBERT/E5，17.4M core，source/trajectory/taskgroup folds、devthreshold；ToolSafe707calls/336groups，原fixedthreshold和20trainruns。相同memory/同参数dense readout与learnedattention反侧支持特定比较接口，但去roleembedding或MoE F1差CI含0，不能说typedembedding本身有因果保证。FixedWeights/retainedbudget换内容与反序支持what-not-order，非所有securitydata。AgentDojo固定2613候选pairs中select优于alwaysP0/P1联合safe/useful，但候选都失败就无解；suite calibration从全部trainfolds选与fold-only57choices变，7ASR/85clean不变不等所有trainingindependent。AppWorld实际417/417choices与supportprior同，不能把该执行得分归learnedcontrast。原nativeOracle只有限scorers，bestF1仍漏unsafe/误拒，MaliciousSkillBench近10%FPR。E sourcegroup bootstrap/permutation Holm只所述population；公开开发条件/候选搜索和训练成本不匹配不能称universalPareto。cachedencodings下GPU分钟/显存不含encoding/预生成summary与双rollout，全部采集/fit/selection/replay/校准/回归均付费；hardware具体型号、全precision/batch、concurrency/SLO不统一披露，不授生产低延迟。无需遍历其余本不采用benchmark附件。

实际owner `PLATFORM-SECURITY`：读Ch72 PromptInjection执行边界、SecureAgents proposal、PolicyCompiler、AuthGraph与AgentGuardian完整机制，并核Ch71租户/Ch73发布开篇及Ch78提案/执行分责。现有确定性provenance/learned risk backend不具体拥有**把拒绝作为有代价alternative、以role-conditioned多次证据检索学习相对action outcome再选操作点**。拟SecureAgents完整段marker后/RuleOfTwo前两段，保持模型判分不拥有授权：

```markdown
来源关系也可进入学习到的候选比较器，而不只成为硬规则：把可信任务、外部观察、原行动和可执行替代分别编码，多次检索并比较它们，再用原生outcome监督相对value，在独立development数据上选择偏离默认行动的操作点。拒绝也是有代价的候选，故这条分支能把误拦与危险放行共同暴露，而不只问原行动像不像有害。这里role标签只保输入分工；读过不可信内容的模型总结不会因挂上“任务”标签而取得authority，学习value也不替代独立policy/对象授权。

[PROVISO的有限比较](https://arxiv.org/html/2610.27115v1#S3)按部署分别拟合，offset校准并非正确概率保证；去roleembedding的局部差额未显著，不能把来源标签本身当因果防线。完整候选rollout及restored replay支持的是受控可恢复域的选择，不可拿来撤销真实已交付effect；候选池没有安全可用项时比较器也不能创造它。采集/编码、所有候选生成、训练、校准与独立回归均付费，低cachedcore开销不等全流程廉价。身份、候选可执行性、风险人口或操作点不明时，保留确定性授权、最小权限/人工拒绝与原安全快路径，不由高F1或一次value胜出批准不可逆行动。<!-- source-family:SF-2026-ARXIV-2610-27115 -->
```

## S9 — DeclineCraft28340：必要反证Source与Ch76窄PRE prepared

[精确v1](https://arxiv.org/html/2610.28340v1)，原件`root-2610.28340v1.html`；官方CL Wed21，当前只有v1/38p标记无撤回纠错。3+1+2=6，设计反证域深入。实读§3–6、A.2–5拒答/深度反侧与H/I定义/paired检验/分母、G生成与judge边界；未看所有逐model表、原完整prompts/代码。不是将Minecraft应用研究单独纳入，而是RAG知识缺口评价反证。

以2025Mar31 wiki截点构造2642pages/11612chunks可检索pre，170新pages/712chunks（抓取Sep8）仅生成不可答问题；旧page后更新不进入post。相同scenario-first generator、verifier+manual排malformed与旧fact、cap每chunk2/page10及去noveltycue得到700answerable/300unanswerable。Knowledgecutoff声明与noRAG泄漏audit只能有限探查parametricexposure，不能证明每model未见；generator选择styleAUC接近chance也不保证绝无风格shortcut。91%answerabletarget@5并非所有回答都已得到支持，postfact真实也不等模型已能证实。

CAR只不可答上明确承认缺知识，premisedenial/替换熟悉实体不算；AAR只可答尝试，AA用三不同familyjudge对700可答计0/.5/1含拒答0。16000output含thinking耗尽1.9%从CAR/AAR排除、AA记0，不能混分母。27models/40configs并非40独立model；sameweights思考配对。Human70response/30accuracy按label/bins平衡非自然人口。放宽deny算拒答保retrieval方向但改变thinking/releasedate结果，严格label语义是主要结论边界。Temperature0除providerdefault例外，precision各model按可容硬件不同/closedOpenRouter与vLLM混；本次不采用单个性能精值/生产SLO。

single k5 hybrid优于noRAG的CAR；iterative自判context不足最多2轮/每轮最多5queries共享k并dedup新增，改变上下文和反思调用，不能归因“反思必坏”或followup唯一作用。其CAR在30/40配置显著退、AA平均近不变，证明须分开验知识缺口而非只总正确率；不授所有retrieval算法。12model rewrite+rerank全方向退但60paired仅3显著，不能说每model显著；11model k10与scenario移除属于不同干预。Thinking noRAG8/13显著降低CAR且matched abstain→deny较多；withRAG方向分家族，不说morethinking必有害。相同question精确McNemar、familyBH，跨model均值tinterval/correlation有共同family和cutoff混杂，未显著相关不证size/date无作用。更多retrieval、rerank、生成/反思、标签与历史维护全计费。Snapshot不完整、单domain/encoder/chunk与source暴露/judge偏差保留；没有测试显式提醒时间不确定性。未核实现或复现。

实际owner `AGENT-RAG`：读Ch76证据充分/答案与支持分层、Sieve/Sage缺证vs干扰完整段及与membership交接，Ch75/77分责复用。已有缺证拒答/分层不具体说明**旧知识未载不能推出当前实体不存在，以及CAR/AAR/AA在多轮检索/思考下方向分离**；唯一窄段拟Sieve完整两段及semanticmarker后/GroundedOutput标题前：

```markdown
缺证据的拒答还要与“前提不存在”分开：旧snapshot或模型记忆没有某实体，不足以证明它在当前世界不存在；把问题换成熟悉实体后作答同样没有补上原义务。可以用晚于corpus cutoff的真实事实构造知识缺口，并审计可能的参数暴露，分别报告不可答上的正确承认、可答尝试和答案正确性。[DeclineCraft的受限反侧](https://arxiv.org/html/2610.28340v1#S4)中，相关却不充分的多轮检索或额外思考可能降低正确abstention，而总答案分近似不变；该方向不对所有配置、严格/宽松deny定义或retrieval机制普遍成立。更多检索、反思、历史快照与judge都有费用，时间切分和未检出泄漏也不证明模型从未见过事实。来源缺失或知识时点不明时，保留明确Unknown、更新原始证据/询问用户及受限单轮路径，不能让premise denial伪装成认识到自己的知识边界。<!-- source-family:SF-2026-ARXIV-2610-28340 -->
```

## S10 — DAY排除抽样：28164决定事实与必要Source/PRE

独立reader发现A5的“模块组合”EX未解释具体接口；root只恢复[exact-v1 method](https://arxiv.org/html/2610.28164v1#S3)，[本次原件](root-2610.28164v1.html)。原完整题摘与Wed21公开列表日期层复用，未以HTML的Oct20提交日移归属；当前原件无所见撤回/纠错标记。方法确认不只是一般未来aux：冻结3D encoder的多view特征经view queries/四帧时间slot压缩和causal mixer得到G，G的相邻差供motor queries读取并受action监督成为Z；冻结teacher后，当前输入的geometry queries拟合G，动作通路的中间表示以cosine拟合Z。未来仅训练privileged target，非推理事实或因果解耦。故原EX理由不成立，提出准入P、2+1+2=5；不是为数量改判。

潜力明确后仅补必要评价§4.3/T4–5、A.3直接encoder/weight/同框架guidance控制、B.2训练与D限制。统一表示与分工表示在相同downstream下有局部差额，但容量/预训练预算未完全独立；去分支对照中个别任务反胜，DINO对部分任务更好、更强geometry loss反退。深度probe使用派生标签，不证真实几何；同backbone受限控制不授通用因果。teacher预训练32H200/120K steps与后训练、全部特权视频/前向、评估均计费；下游precision/完整latency/concurrency/SLO未获所读证据，不采无成本或实机安全。未核代码、全部图像或复现；不再扩其他研究。

实际Ch26读FutureVLA完整两段与前LAPT/后动态区域接口。已有视觉/motor职责分开，但未承载“时间几何差分→动作监督motor teacher→几何query/动作中间层两种蒸馏消费者”的具体分支；唯一`MULTIMODAL-EMBODIED-VLA`，拟FutureVLA完整限制段后/动态背景段前一段，未写待reader：

```markdown
几何与motor监督还可沿不同表示路径交接：冻结3D特征先形成带视角与时间身份的几何状态，再由相邻状态差分经动作监督提取motor target；后训练时，geometry queries拟合前者，动作通路的中间层拟合后者，teacher与真实未来只作训练特权信息。[受限对照](https://arxiv.org/html/2610.28164v1#S3)支持这种消费者分工，不证明差分排除了相机运动或两表示已因果解耦；统一表示/普通aux仍能受益，部分任务与encoder选择仍反胜，更强几何权重也会退步。3D teacher、多阶段预训练、特权视频与双目标后训练均付费，删除部署teacher不等零新增成本；表示支持、接触信息或闭环预算不足时，保留普通aux、原policy、真实重观测与独立controller，不以probe或均值成功签发物理安全。<!-- source-family:SF-2026-ARXIV-2610-28164 -->
```

## S11 — VeOmni四具名core：一次有限资格/贡献恢复

不扩repo或周源，仅R150具名四PR。已核官方API的核心说明、created/merge/head，以及PR commits和必要review身份；原件[1328](root-veomni-pr1328.json)/[1231](root-veomni-pr1231.json)/[1200](root-veomni-pr1200.json)/[1255](root-veomni-pr1255.json)。Merge不是首次公开：1328创建Oct20，1231 Sep23，1200 Sep16，1255 Sep28，均不能整PR计本日新事件。

- **1231：纠正初拟排除，保窗外修订线索。** 初读core的INT8 scatter不能覆盖body末尾`Native NPU masked-row regression`：all-masked row BF16 subnormal梯度触发invalid-row输出/上游梯度及无有效query时K/V梯度显式清零，是实际正确性信号。reader指出后只补资格：[官方完整timeline](root-veomni-timeline1231.json)的`head_ref_force_pushed`在Oct20 13:50:56Z已公开指向当前完整head `94718e80cacb87dae1d90307d25c318eca919983`，即Oct20 BJT；不是把commit作者日期当公开日。该修订留真实归属日恢复，不因Oct21批准/rename/merge重计，未声称已有效Source或复现32rank验证。
- **1255：本次不准入。** 核心明言把已有Qwen3.5 router-replay合同接到Qwen4Exp，active时替expert indices/按当前router重算权重，manager不改；非新replay机制。未采用byte-identical或低成本保证，纯模型接线/测试不建立本次长期增量；不因merge重计。
- **1200：窗外具名恢复线索。** 当前完整head `a1f63671d8522d3fb8838513cd018d8fdd1ccbc1` 已被[官方review原件](root-veomni-reviews1200.json)在Oct20 15:13:20Z公开引用，即Oct20 BJT，早于目标日；不是仅以commit author日期推公开。IEEE dot precision、有限compiled/eager差额值得真实归属日定点处理，但本窗无后续实质commit，Oct21 merge不创造新结论。未称已审重复，不顺带恢复Oct21日报。
- **1328：本窗实质修订准入，拟3+1+2=6。** [精确c84修复与测试](root-veomni-commit1328.json)的官方commit author/committer为Oct21 04:35:18Z；[官方完整timeline](root-veomni-timeline1328.json)在Oct21 06:42:39Z的公开review直接引用c84，merge08:25:57Z。均Oct21 BJT，本次只采用该具名修订事件，不把commit字段冒充不可伪造的全球首次公开证明，也不用merge把Oct20编译/动态shape旧机制重计。c84移除临时替换HF module-global builder/offset helper，改每次调用本地组合padding/offset predicate，显式传device/length/blocksize；A-enter/B-enter/A-exit/B-exit可让旧finally恢复他人的closure，影响native HF消费者，故不是仅修复标签。实际读该完整受影响函数patch、成功/错误交错测试与native consumer断言、pinned padding/offset稀疏表对照及新增CPU限制。Concurrency测试用stub builder隔离compiler启动，真实编译有另一组回归；不能据此称并发真实编译已验或所有GPU安全。作者历史H20数据非最终head重跑；CPU特定bool/offset compile故障保显式eager分支，未我方运行或授性能。

唯一owner拟`INFER-TENSORRT-LLM` Ch49 GPU执行计划/Attention接口，已读FlashAttention完整开头与后IO-clustering两段，Ch48/50职责；Ch40并行runtime不拥有局部kernel构建语义。现有typed/shape/kernel安全没有本例**构建回调闭包的调用隔离**。只拟FA2/3完整段后、IO-clustering前一段，不搬API手册或旧性能：

```markdown
优化attention的mask构建时，还须隔离每次调用的构建环境：临时替换共享模块的builder或offset helper，即使在finally恢复，交错退出也可能把另一调用的device/长度闭包留下，影响同时运行的原生消费者。[一个公开修订](https://github.com/ByteDance-Seed/VeOmni/commit/c84d10db668169f076c71b922b007b47e1a2f91c)改为本地组合padding/offset predicate，并显式传递shape、device与block size；编译缓存复用不再借共享函数替换，但仍须验原padding与可见token语义。其交错测试隔离了compiler启动，不能认证任意并发编译或全部硬件；局部构建、编译及回归均付费，特定CPU lowering失效还需eager回退。串行独占构建在简单环境仍可成立，无法证明隔离或语义一致时，保原已验实现、显式序列化/进程隔离，不由一份编译成功日志批准共享运行环境。<!-- source-family:SF-2026-VEOMNI-1328-C84 -->
```
