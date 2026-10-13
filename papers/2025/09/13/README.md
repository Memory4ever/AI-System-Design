# Daily Research — 2025-09-13

**规范：** V3
**窗口：** 2025-09-12T09:00:00+08:00 ～ 2025-09-13T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-12T04:43:00+08:00
**补充窗口：** 2025-09-12 ～ 2025-09-12
**冻结候选日期：** [本日补查前原报告](../_sources/daily-20250913/baseline-before-supplement-20261012.md)
**窗口说明：** 用户连续奇数日路由授权仅补Sep12完整BJT自然日；原窗口/CAISI标题URL日期6分与有效审阅/连续§4冻结，不catchup/小时/Weekly/2026，不继承Sep11研究队列。

## 1. 结论

补查正式候选为旧CAISI/AISI安全更新1家族与新增VaultGemma模型/技术报告release1家族，合计2；两者均6分、安全受影响必要深入。CAISI具体已有覆盖有效复用；Vault在`PLATFORM-SECURITY` Ch72实际增加一段及自身末注，原doc→chunk→跨doc packed sequence→重复贡献映射不能由sequence DP直接升级为document/user保证，非writer实际POST通过。未运行实现、攻击、训练或复现实验。

新四主题arXiv发现113出现/89唯一家族，作者实际完整读89题摘，62窄潜力尚缺首次公开日、27贡献前关闭；不是89本日公开论文或62正式候选。相对旧123为21新only/68共同（51同字段、17字段差额），并144仅表示发现身份并集，不是扩大必读队列。旧82完整题摘/67日期潜力和必要12+3反侧的有效层仍保留，未与交集重复相加。首批校准纠正AODL、Chile、LongText等过宽排除，成熟组合、负面/小模型结果不自动排除；七个必要贡献决定门实际闭合。

PLAS虽Blog日期Sep12落新自然日，原机制、文档与同两模型评价表已在Sep8公开PR/exactSHA存在，当前是窗前解说线索，不作为贡献EX或新候选，不迁入别日报。Seed当前论文数组真实恢复并跨Sep12前缘，不继承旧缺数组；Hunyuan/Z.ai/MiMo/MiniMax历史目录及arXiv官方日批仍精确隔离，不支持0事件、完整Coverage或无遗漏。MOAT/Graph/Butterfly中心保证争议、SteerMoE与旧Lipschitz等安全/理论边界保留；日期恢复不自动解除争议。研究普通与完成态待办0，Anscombe实际完整六部分DAY§16及完成态FINAL§17通过本日安全终态，不表示整轮完成。

## 2. 来源覆盖

本轮实际入口/主题/分页停止及恢复见[补查来源](../_sources/daily-20250913/SUP_SOURCES_20261012.md)，同名SUP request/raw保留URL、执行时间、45秒请求界限与原件身份；66组指纹实际匹配。旧`transport.json`仅历史，不代本轮请求。未来页面metadata只定位历史切片，不加载2026研究队列。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 本轮官方RSS原pubDate Sep12安全更新；旧本日官方web L39–74/root必要证据按未变命题复用 | 已检查 | 1旧家族不重复计新；feed不是全站无遗漏 |
| SRC-ANTHROPIC | 本轮Research SSR publication实际解码，Sep5→Sep15T09Z/T20:33Z跨自然日 | 已检查 | 有限publication目录切片，不遍历库存全文/删除记录 |
| SRC-GOOGLE-AI | Research月1→2/2共12+1卡Sep30→Sep9，Vault Sep12；DeepMind page5 24卡Nov→Jul，三相关原页hero/published_time实核Sep25/22/17 | 已检查 | Vault新报告pages1–7实际深入；不要求小时，月目录不授全部pubs覆盖，科学应用范围停 |
| SRC-META-AI | 本轮publication results5末Sep15→results6首Sep8，旧pin分开；Blog3 Oct24→Aug27/14与旧2019/2024pin实际读 | 已检查 | 有限主题前缘，不授全历史 |
| SRC-QWEN | 本轮research config 9月10对象原ISO；Next Sep10T20Z(BJT11)，ASR Sep8T06:38Z，余Sep21/22/24 | 已检查 | 没有Sep12目录条目，仅该实际切片，不以draft/retrieval当公开日 |
| SRC-DEEPSEEK | 本轮官方updates实际Sep29/22→Aug21 | 已检查 | 仅公开更新切片，无具体机制release触发 |
| SRC-MOONSHOT | 本轮完整26卡及datetime，Sep16→Sep5→Aug22 | 已检查 | 无本窗具名GitHub触发，不扫普通PR |
| SRC-TENCENT-HUNYUAN | Research shell→正确publicList POST page1/pageSize1000/renderType0，中英11/9=total，全2026；IAB拒绝/超时、Chrome unavailable实际恢复失败 | 受阻 | 无历史DOM/列表，不当Sep12零事件；需要当期全部目录或具体原文 |
| SRC-ZAI | Research实际p2→p3重复18卡，末Dec7/NoMore；notes HTML shell后md日期末Sep30 | 受阻 | 当前历史入口未跨Sep12；旧Aug11不冒称新恢复，不支持0事件 |
| SRC-BYTEDANCE-SEED | US/type2/year2025/token0/count20/desc实际18/45，非pin Oct23→Aug21；type1 token0 18/94，非pin Sep22→Sep2→Sep1；额外paper20 20卡Jun20→May20只核metadata后停 | 已检查 | arrays真实恢复，不继承旧缺数组；pin分账，不扫40/60/80或把94库存变队列 |
| SRC-BAIDU-ERNIE | Blog实际1→2/2，PLAS Sep12核心；公开PR3954/Sep8精确mergeSHA文档同机制/两模型表闭合 | 已检查 | Blog日落新窗但事件窗前，只恢复线索，不迁别日/不作贡献EX |
| SRC-XIAOMI-MIMO | 本轮SSR8Paper/15Blog，More chunk只切8+7无fetch，Paper Sep19→Jun4/May12 | 受阻 | 历史Blog日期未恢复；不是列表未读或未执行More |
| SRC-MINIMAX | 本轮EN12/CN13主序到Oct27；p2派生正文同首页；Agent techblog/llms实际3当前篇 | 受阻 | CN Jan15旧锚不证中间，历史Blog/Agent目录仍缺；runtime date与subscription terms不作Research日证 |
| SRC-ARXIV | 四主题12分类submitted UTC Sep11 16:00→Sep12 15:59，start0/max150，42/14/26/31均等total，113出现89unique/exactv1 89全部题摘；官方month有限首25接口恢复、旧advanced年/月说明和官方日批补检无日证 | 受阻 | 62窄P日期隔离/27贡献EX，submitted≠first-public；旧67保留有效层，具名必要反侧实际核，不授正式候选/完整Coverage/无遗漏，不全月扫描 |

未扫描每周组。表外NIST仅旧安全候选必要原证有效复用；Google技术PDF/FastDeploy公开PR精确SHA由候选触发必要读取，不是仓库常规发现扫描。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Working with US CAISI and UK AISI to build more secure AI systems](https://openai.com/index/us-caisi-uk-aisi-ai-update/) | 2025-09-12T20:00:00+08:00 | 传统漏洞原看似不可利用→Agent hijacking串联局部反例→安全验收需跨软件/模型控制边界；2+2+2=6 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)的executor effect-time授权、run单位与集成fixture/effect身份；root单项独核通过，正文增量0 |
| [VaultGemma: The world's most capable differentially private LLM](https://research.google/blog/vaultgemma-the-worlds-most-capable-differentially-private-llm/) | 2025-09-12 | example/user单位未说明packed数据映射→1024-token sequence DP的拆分/合包/重复贡献边界→发布须按真实保护对象核映射与会计；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) DP保护单位段后新增一段/自身末注；Anscombe必要Evidence/PRE/实际POST通过，不授全生命周期私有或零泄漏 |

新89题摘62P/27EX逐项index及理由见[补查筛选](../_sources/daily-20250913/SUP_SCREEN_20261012.md)、[首批](../_sources/daily-20250913/SUP_FIRST_20261012.md)、[必要决定门](../_sources/daily-20250913/SUP_NECESSARY_20261012.md)。62日期未证不评分或列正式候选；原67日期潜力及原15完整题摘/41标题关闭有效层另保留在[旧筛选](../_sources/daily-20250913/SCREEN.md)/[旧校准](../_sources/daily-20250913/INDEPENDENT_FIRST_CALIBRATION.md)/[旧独核](../_sources/daily-20250913/INDEPENDENT_DAY_REVIEW.md)，不把交集相加或旧标签当本轮验收。

## 4. 证据与知识整合

### [Working with US CAISI and UK AISI to build more secure AI systems](https://openai.com/index/us-caisi-uk-aisi-ai-update/)

采用身份为Sep12官方发布，时间由本日RSS原GMT支持；当前官方完整核心web L39–74真实读到，HTTP403不冒充正文已得，[原工具记录](../_sources/daily-20250913/openai-caisi-web.json)与[交接](../_sources/daily-20250913/HANDOFF.md)保留证据位置。厂商披露传统漏洞与Agent劫持组合的局部失败路径；约50% PoC没有公开attempt/样本分母、精确漏洞、完整trace/实现或修补版本，不作总体率或修复实现审计。关联NIST是Jan2025 AgentDojo及Dec2024 o1评价，不是此次July ChatGPT Agent漏洞的独立复现；特权访问测试与普通用户条件分开。

作者实际读Ch72 1245–1297的untrusted输入/effect-time executor控制，764–812的run/attempt/集成评价条件，2989–3012的connector/credential/destination/fixture/effect身份；Ch71 1–75、Ch73 1–55与Ch78 167–197相关交接已读。root有效单项独核实际原文、RSS及owner相邻论点，裁决已有覆盖、无拟增自然段；本次非作者复用该有效结论，再独立核剩余本日处置，见[整日验收](../_sources/daily-20250913/INDEPENDENT_DAY_REVIEW.md)。不把厂商合作声明当生产保证，未复现或执行攻击。

Vault本日完整核心支持1024-token packed sequence级DP、Poisson采样与fixed-batch处理，不能授user/doc DP；尚缺本窗公开日期，不采用。arXiv82完整当前题摘不等于精确历史v1证据。独立指定的11风险信号与10439理论已定点核精确v1机制/限制，见[必要反侧](../_sources/daily-20250913/NECESSARY_CORE.md)：privacy SSIM/ARX局部测试不授DP或任意重识别保证；firmware log扫描不授coverage/物理WCET；LLM想象干预不授可识别因果；Local SGD只在convex、i.i.d.同分布、无偏有界方差及联合stepsize下成立。10298v1概率权重和数值例子矛盾、作者承认global Lipschitz未验证，保留争议。新恢复10184的情绪支持反侧中Severe标注一致性明显较低，1490是配对回复而非1490独立用户/临床测量；10059图像数学测试需区分11场景/814实际车辆与16k车辆样本，不能从题量授独立场景泛化。全部日期隔离不进入Books，不把已读称安全已证实。

### [VaultGemma: The world's most capable differentially private LLM](https://research.google/blog/vaultgemma-the-worlds-most-capable-differentially-private-llm/)

上面连续旧§4逐字冻结，其Vault小时缺口/日期隔离和旧arXiv处置仅历史，不覆盖新自然日判断。新官方hero与[技术报告](https://services.google.com/fh/files/blogs/vaultgemma_tech_report.pdf)页1 Sep12共同绑定1B模型/报告release，不把旧DP scaling论文或placeholder arxiv/abs/123造作本篇身份。实际报告pages1–7（末页references/图像像素未采用）支持1024-token packed sequence为privacy unit，cross-doc合包/doc拆分和mixture重复按多个单位计；zeroing-out ABLQ_P/PLD会计不能升级document/user邻接，非私有Gemma/Gemini tokenizer不获得追溯保护。truncated-Poisson/pygrain/padding与microstep等价只是作者配置与会计声明，未核实现。

实际最终2048 TPUv6e、expected batch517989、100000steps、noise .6143481、epsilon2/delta1.1e−10只绑定报告配方；7LR与5完整预算law的一次final预测1%不授通用外推。Table2的模型/数据/recipe不完全相同不证纯DP因果utility，1M prefix50/suffix50且edit-distance10%未检出不是零提取、记录删除或任意攻击安全。完整边界与具体owner比较见[单篇](../_sources/daily-20250913/SUP_VAULT_20261012.md)；Ch72原example/user定义、fixedbase非追溯与会计已覆盖，新段只补doc→chunks→packed sequence→重复贡献映射，成本/Unknown/收窄发布与按所需单位重训回退近正文。Root授唯一一段/自身note窄锁，实时原件/hash保留，Anscombe非writer实际POST§13通过，锁已释放；不改其他并发Books/State。

本轮arXiv必要理论/安全采用限制见[必要核心](../_sources/daily-20250913/SUP_NECESSARY_20261012.md)及[独核§9/11起](../_sources/daily-20250913/SUP_INDEPENDENT_20261011.md)：MOAT PPL相关不等实际奖励单调；Graph两滤波互补不证独立/严格margin；Butterfly低off-diagonal coherence不证outlier抑制/全部exact表示；CDE只条件linear/asymptotic及同正确组相对likelihood，不等概率校准。SteerMoE白盒route干预局部safe分母不授黑盒突破/全部quality或alignment-faking。Rosacea固定ROI无身份攻击真值的安全门已实际处理，领域诊断EX不授隐私/临床保证。全部这些日期未证不进入Books，也不以争议理由删除机制潜力。

## 5. 缺口与下一步

普通可执行研究与完成态待办：无。十四来源实际有限停止、62窄P准入/27EX、安全及理论必要反侧、两正式候选证据/Books与Vault实际POST均已处理，Anscombe完整六部分DAY§16与完成态FINAL§17实际通过。未读普通材料未转外部hold，不扩大本日验收范围。下列均为本窗终态保留项，不支持正面Evidence、Books、完整Coverage、零事件或无遗漏断言。

- 终态保留项——arXiv日期：当前62窄P逐项身份/index见SUP_SCREEN，旧67有效日期请求在旧本日材料保留、交集不重复索取。四主题submitted查询完整返回不证first-public；month首25/旧advanced年月至当前有限官方补检仍缺Sep12日批。需要当期官方日公告/列表或对应具名首次正文公开日，日证回归只重开该身份及其必要采用命题，不全月扫描或把123/144库存送全文。未核日期的明确27EX不另造日期请求。
- 终态保留项——理论/安全：MOAT09629实际奖励代理/更新单调与收敛、Graph09597正交独立/严格margin、Butterfly09679 off-diagonal coherence/结构exact表示，及旧10298代数/数例/global bound争议。对应原证/反例保留，需具名修正、成立条件的可信证明或匹配评价协议再重开中心保证；日期到达不自动采用。不影响已读局部机制，不支持正面Evidence/Books/安全证书。
- 终态保留项——来源历史：Hunyuan当期全部目录/具体原文（当前中英全2026且浏览器实际不可用）、Z.ai当期Research/notes（p2/p3同18卡且末Dec7、notes末Sep30）、MiMo历史Blog日期/原件、MiniMax历史Blog/Agent分页。实际入口已有限恢复，材料到达只重开本窗主题，不支持零事件或无遗漏。Seed数组已恢复、Vault日证/必要证据/POST已闭合，不再列旧缺口，也不继承小时门。

CAISI未公开漏洞细节/patch只限制已采用局部风险范围，不为无关实现造请求；不授总体安全率/已修复。窗外PLAS明确Sep8公开先稿需其真实归属日另行恢复（本次不迁日、不授旧已审）；Qwen Next Sep11，不扩本窗或创建其他日报。

## 6. 复核

复核者：Anscombe（01a1289f-7cae-7253-bef5-9228c04195d8，非报告作者、非Vault Books writer）。

结论：通过

实际独核见[唯一独核§15 Sources/§16完整六部分DAY](../_sources/daily-20250913/SUP_INDEPENDENT_20261011.md)：复核者本轮59完整题摘为36P/23EX、余26P/4EX共30依旧具体有效层复用；21新only/17字段差额及先前标题层P、全部拟入选/安全理论反侧、七个最小贡献决定门和代表EX分层实际处理，不称全部附件复读。十四来源真实切片/停止及66组request原件指纹、PLAS先稿门、Vault必要报告/PRE/实际POST独立通过，旧CAISI单项有效复用。2026-10-12T04:54:45+08:00实际DAY通过，研究普通0，外部保留不支持完整Coverage或保证；不是模型/安全实现复现验收。

旧sept07_10_author非作者分层DAY及root CAISI单项核验仅按未变身份/版本/命题有效复用，旧连续§4不重写。完成态V3、19本地引用、baseline原窗口/旧整行/连续§4逐字冻结及限定cached/unstaged diff-check均实际通过，见[作者机械记录](../_sources/daily-20250913/SUP_VERIFY_20261012.md)。Anscombe已实际回读完成态及限定diff，独核§17 FINAL通过；仅行政同步该实际结果，不重读原证、不扩大采用，不stage/commit/push。
