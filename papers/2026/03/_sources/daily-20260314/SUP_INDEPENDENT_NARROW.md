# 收窄后的12题摘：独立贡献校准

复核者：`mar13_admission_review`；准备者：`mar14_supplement`。仅03-14/补充Mar13 BJT自然日，未改Report、Books、主ledger或LEARNING_STATE，不授DAY。使用context-engineering技能隔离已结束日期与有效前包，当前只加载本小批。

本次实际重读AGENTS、当前Research/Report/SourcesDaily与arXiv主题合同、统一Prompt、ROADMAP相关节点及当前范围边界、最新checkpoint路由与本日README开头/§5停点。已有149标题是有界查漏库存，旧41+10线索不是51项配额；明确应用标题仍可停止，不要求全部题摘或全文。本包是作者再次收窄的12具名项，不签其余库存处置。

实际读取`SUP_ADMISSION_NARROW.md`与`SUP_NARROW_AB_MANIFEST_RESULT.json`，逐项直读十二份本日`SUP_ABS_<ID>.txt`完整title/authors/abstract/Comments/可见history（输出截断的12149/12229/11757/12117已单独恢复）。manifest十二均为官方`https://arxiv.org/abs/2603.<ID>v1` GET200，2026-10-10T01:28:06–09Z，final URL同精确版本。11975/12248/11253/12249页面显示后续v2，但本次不混用v2题摘，不因版本变化推断重要修订。保留页未见撤回/纠错说明；不做完整版本遍历。此处不核十二项公开日期、不评分或授必要Source完成。

## 原判断 → 实际增量 → 改变的选择

| ID | 非准备者校准与采用边界 |
| --- | --- |
| **11611 Partial RoPE：窄P** | 全维旋转作为默认设计 → 实际考察旋转维度比例、NoPE训练动态及少量RoPE/QK-Norm的不同收敛 → 值得核重新选择位置子空间及训练稳定性。10倍只指RoPE cache，不补成全KV、整机memory或服务吞吐；成熟RoPE原理不算新增。 |
| **12248 EBFT：窄P** | teacher-forcing CE与实际rollout sequence对象不同 → feature statistics目标、nested-prefix strided block-parallel sampling与on-policy梯度接口 → 值得核监督对象及多rollout执行费用的替代。feature feedback不是正确性判据，理论KL桥与胜率/CE对照待必要审阅，不授无成本或替代所有RLVR。 |
| **12149 Confidence：窄P** | perception accuracy不说明模型知道何时不确定 → original/noise成对reward及confidence调度Self-Consistency/Reflection/Visual Self-Check → 值得核校准信号如何改变测试预算。外部Expert同时Planner/Critic/Voter不自成独立真值；“free lunch”不是无费用。CVPR接受说明不是已知具名早公开正文。 |
| **12089 EmbTracker：窄P** | 群体所有权/白盒合作不足定位不合作client泄漏 → server对每client下发identity-specific backdoor、黑盒API验证 → 值得核模型身份与泄漏归因的验证接口。Work in progress不等撤回；近100%作者数字不签不可伪造、跨串谋/所有移除攻击或上线无损。 |
| **11253 Political privacy：窄P** | 无显式政治词不等无敏感推断信号 → LLM使用非显式词的社会文化相关性并跨文本聚合user-level预测 → 值得核隐私/匿名化和输入暴露边界。不是因政治主题或标签预测自动收录；保留标签构造/人口/因果未核，预测标签不等每人的真实信念；不读攻击战术。 |
| **11248 vision/history：窄P** | 像素定位准确不说明表示具有知觉对齐的历史依赖 → 固定像素条件motion adaptation下人工feedforward/recurrent/video模型不出现对应位置偏移，经验feature变换可产生偏移 → 值得核视觉表示解释及历史状态更新的成立条件。仅直接人工模型反侧有主线关系，不采用生物类比作Agent记忆证明，也不扩生物应用。 |
| **11757 social bandit：窄P，日期另待核** | 只观察他人行动、奖励不可见且示范者未必专家 → policy-space free-energy融合direct experience与估计他者policy，并声称最优收敛/log regret → 值得核非oracle示范者的学习条件。非LLM或小模型不自动退出学习主线；数学假设和一般LLM迁移未核。actual Related DOI `10.1109/TCDS.2025.3648042`是具名事件线索，需后续同稿/先公开核，不能由编号2025直接宣告OUT或由纯接受规则消除该对象。 |
| **11414 MaterialFig：窄P** | 答对可能未读提供图像 → 原AB明确报告memorized domain knowledge得到正确答案、数值读图/有效数字反侧 → 值得核perception与answer测量对象及控制。137材料题本身不构成贡献，只采这条直接blindspot线索；实际控制是否支持归因待核，不绕过Science暂缓去收领域任务。 |
| **11975 HomeSafe：决定core** | 静态hazard评价不足刻画unsafe action → 438模拟/生成动态案例与fast高频/slow异步机制 → 需只核触发、并发/回传与检测单位是否真新增可复用条件。不由dual-brain、Safety名称或模块组合直接授P；不要求完成438案例与全部图像像素。 |
| **12249 SciMDR：决定core** | 局部QA faithfulness与full-document realism取舍 → claim-centric synthesis后programmatic reground → 需只核重新定位如何保持证据/grounding约束，还是把现成QA重新包装成fullDoc任务。300k或Science标题不自动入/排，不全文队列。 |
| **12229 LMT distributed：EX通过** | 原AB提出以distributed systems作团队设计/评价foundation，并称已有fundamental优劣也出现于LLM；没有具名新增协议、执行约束、条件或具体失效反证。成熟类比与何时团队有效的问题列表不足提供实际新增命题；不是因团队主题不重要或章节已有覆盖而关闭，不评分/不补全文。 |
| **12117 SommBench：EX通过** | 原AB以专业者/多语言建立wine理论、feature、pairing三类领域标签测验并给不同难度成绩。理论97%与feature65%/pairing MCC不直接建立同信息条件下的sensory-grounding失效或通用评价修正；现有增量是领域专家测验，而非已经具名的主线blindspot。不是按酒类词排除，也不要求证明普遍LLM质量后才准入；原证足够本贡献层停止。 |

## 两个决定core的实际结果（不扩标准Source）

作者仅机械代存、未读决定段；本人直接读`SUP_NECESSARY_11975.txt` §3.3/§4.1–4.3 Eq1–4、§5.1.2–5.1.3/§5.4，以及`SUP_NECESSARY_12249.txt` §4.1–4.3、§5.3–5.6的直接对照/反侧，截断的§4.2已恢复。未读全部图像/附录/代码或复现。`SUP_NARROW_CORE_MANIFEST_RESULT.json`两份exact-v1 GET200，11975为1369229bytes/2026-10-10T01:31:36.134692Z，12249为353166bytes/01:31:36.135265Z，final URL分别为对应`/html/2603.<ID>v1`。

**11975：窄P。** 只报告“fast+slow”组合不足，但实际§4给出Yellow异步触发、Green/Yellow-Red分别1/5 FPS、slow计算期间fast继续监督、Red OR slow positive的优先覆盖规则；§3.3另有intent/PNR/PNR前200ms intervention deadline/impact生命周期。原来静态hazard/离线回答分数不足说明可用预警 → 原文新增持续fast覆盖slow等待的决策接口与时间窗测量 → 值得核改变预算/警报优先级及预警验收对象。这不是给交通灯或dual-brain名称增分。

限定很具体：§5.1.2 HDR人口是438 hazardous视频，EWP分子intent至impact而非全部在deadline前、分母是已报hazard，不签benign FPR或真实干预成功；§5.1.3统一2s窗口/1.5s步长与§4自适应采样接口的实际交接仍待必要Source。SlowBrain窗口称centered on trigger，在线可用前缀/回传旧判定的失效规则未在决定段闭合，不将式4写成已验证生产race-free控制。§5.4保留3.10s/3.07s、24.94/18.04作者平均对照，却不以平均时延或2.39s early bias认证全部警报赶上deadline、普遍安全或实物硬件stop。已有事实足够准入，后续需要时才审这几条受影响条件，不为当前P读取全部438案例。

**12249：窄P，仅跨模态文档监督构造接口。** 实际§4.2先在标记figure-reference的局部text中抽claim，暂时不给visual；随后对visual核claim、按MQA/TQA/VQA分路，并给claim结论作backward rationale。§4.3明确每QA绑定记录text/visual位置的claim，把Section/Table等identifier填入模板、将Information Localization prepended到原reasoning，训练对象由局部QA变为full-document→localization+reasoning+answer。原来简化上下文生成容易、fullDoc训练却要重新寻找证据 → 原文新增可保留定位绑定的局部生成/全上下文监督转接 → 值得核这种训练数据构造是否改善噪声下的证据定位。不是300k规模或科学assistant成绩本身，也不是只把现成QA换包装。

这条一般训练/多模态接口与材料领域应用分开：不采用科学知识任务扩张、不经通用owner重新引入Science应用路线。§5.4 same-source SPIQA重新标注给出25.5/28.1/39.8而原26.3/13.5/35.7，ChartQA存在退步，长5倍answer不自证reasoning深度；§5.5去localization49.1→22.8、去reasoning→16.9是当前受测训练对照，非定位真值/所有失效的证明。§5.6 oracle/standard/full-paper为32.9/19.8/12.8，噪声混杂与token预算要在后续必要Source限定，不授无损。claim由同一生成器从源文抽取/修改，“ground truth”是pipeline中间对象而非独立正确性；text-first claim/答案先给的rationale不能自认证忠实因果推理。原文这些具体接口足够核主线贡献，Science领域任务结果本身不计入资格。

## 当前批次状态

十二完整题摘实际校准为 **8原窄潜力通过、2决定core提供窄P意见、2贡献前EX通过**；两core判断原证已足够到此停止，可由root定点校准新增接口/范围后推进，不重建全文队列。P表示值得继续核验，不是确定Mar13候选、正面Evidence或Books新写许可。十二项日期/评分/必要Source另按实际增量处理；EX不评分、不列外部日期缺口。其他库存尚未逐项独核，未读不统称关闭，原前包有效结果不重开。
