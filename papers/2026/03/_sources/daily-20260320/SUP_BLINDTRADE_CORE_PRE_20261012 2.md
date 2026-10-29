# BlindTrade17692：本20必要证据与最小PRE准备

resume_review17_18 sole准备，仅03-20补03-19自然日；原2+1+2=5、准入/date复用。不自行授Source/PRE/安全终态或DAY；交resume_mar17非准备者裁。没有金融建议或市场事实更新请求。

## 1. 精确源与必要停止范围

[exact-v1](https://arxiv.org/html/2603.17692v1)实际§3.1–3.6、§4.1–4.5/Tables1–3、§5、A直接限制254–270、B必要模型/feature与费用273–279、C.1 cutoff317–332、D仅391–433（两个评价配置/反侧）已读；current abs8–28两作者单v1/FinAI2026 workshop接受无具体修订或撤回。未读全部prompts/图像/引用理论/代码或复现。必要支持与直接反侧足本接口即停；不展开作者交易系统全部recipe。

## 2. 原文机制与权限

Point-in-time股票人口与输入截至t−1，ticker/公司/产品名替换匿名ID；四角色模型输出数值/类别和解释，解释embedding与sector关系构图，GNN输出交PPO分配，成本按turnover结算。评估贡献是信息通道的可见性与负控制对象，而非交易系统组合本身。§3.4按holdout IC/DeltaIC选feature；Delta从负值向零移动可只是消除反相关，不自动增加预测信息。B模型Gemini2.5Flash访问Sep–Oct2025，早于预测时点的输入prompt不回滚模型参数或隐藏记忆；访问晚于历史测试日也不独自证明实际预训练包含未来内容，checkpoint真实训练/公开资料membership未证。

## 3. 决定性反侧与限定

§4.4固定股票人口、价格/费用，只横截面打乱GNN预测分数，IC下降、负收益baseline更差；这支持输出与目标的对应结构被破坏，不能识别该结构来自合法输入还是泄漏。独立逻辑反例：令score直接等于本应不可见的future return，原排序相关完美；随机打乱仍会破坏它，所以同一负控制反应可来自完全泄漏的score。不是断言作者实现确已泄漏。

§5/摘要较强地称signal legitimacy/非记忆；A L260明确承认未做匿名vs真实ticker的直接消融，负控制只核signal structure而非匿名化effect。两侧须共同保留，不把删除名称、sector仍可见、解释自然语言或prompt knowledge cutoff授为无泄漏/因果理解。§3.4又把holdout用于筛feature，§4冻超参OOS不自动保证feature选择与最终OOS人口独立；需要原选择/冻结日志，不擅判实际用了完全同样label或证明数据污染。

主§4 train至Sep2024/验证Q4/OOS2025、20seed；D train至2023/六rolling验证/不同eta与costscale/2024–2025，不能合为同模型同超参扩窗。D全期弱于除EQWL外对照，2024明显退，主系统drawdown/vol更高且无cash动作。20seed只是该配置随机性，非独立市场人口或普遍优势。推理硬件/precision/batch/concurrency/SLO、全部LLM/API/特征生成/Optuna/GNN/PPO/复评费用未完整披露；已有成本10bps只覆盖交易turnover，不是系统总费。数据未来release声明不冒已公开可复现。

## 4. actual sole owner/差额与最小PRE

sole `PLATFORM-EVALUATION-SYSTEM`/[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)实际1–20、145–175完整proxy→公开标签/DSGym负控制→任务切片、641–659污染数据/输出sensor/运行访问路径，3337–3349历史预测时间与参数未来知识分责；Ch65/67开篇交接已读。既有data-withheld操作在输入通道，污染sensor在输出记忆，已有提示不阻漏与historical cutoff边界；尚无“输出score-shuffle会同时破坏合法与泄漏信号、因此不能充作匿名化因果验证”的具体操作层差额。拟DSGym完整受限审计段后/任务难度切片前两短literal，若非准备者认为现有具体覆盖已足可NC，但不能只凭负控制主题相似。

### 正文PRE 1

负控制还应说明被打断的是哪条通道。固定输入、标签和运行人口后，只在样本之间打乱最终预测分数，可以检验原分数与目标的对应结构；它不同于移除模型输入、替换实体名称或改变模型可见证据。即使分数直接来自本不应可见的答案，打乱后相关性也会消失，因此这个结果不能辨别合法预测与泄漏，更不能独自验证匿名化确实阻断记忆。应把输入侧权限干预、输出侧对应破坏和独立数据血缘证据分别保存。<!-- source-family:SF-2026-ARXIV-2603-17692 -->

[有限历史预测审计](https://arxiv.org/html/2603.17692v1)本身承认未直接比较匿名与原标识输入；提示的历史cutoff也不删除模型参数中的未来知识。保留匿名处理作为通道控制，不授无泄漏或真实因果理解；用留出数据选择特征后，还需另冻结选择过程与最终评价人口，不能让同一“holdout”同时担任开发反馈和发布证据。更多配对输入、负控制、独立时间/来源核验和重新训练评价都有费用；配置改变、部分时期或风险指标退步须分别报告，资格不齐时只保留结构诊断与原任务分数，不将单一干预下降升级为可靠能力或部署保证。

### 静态来源注PRE

- [BlindTrade2603.17692 exact-v1](https://arxiv.org/html/2603.17692v1)：必要§3–5/Tables1–3、A匿名化直接消融缺口、B模型日期、C.1提示cutoff与D配置/反侧。仅输入权限/输出score-shuffle/独立污染证据分责；保合法与泄漏score均可被shuffle破坏的反例、feature选择/最终holdout分账、配置和风险反退与全费用，不采匿名化因果、无泄漏、市场理解、交易收益或生产保证。未核代码/图像或复现。<!-- source-family:SF-2026-ARXIV-2603-17692 -->

若拟采正面legitimacy/匿名化作用，只一次请求原标识vs匿名配对、原模型checkpoint时间/信息可见性、feature选择冻结与独立最终人口/对应控制，不额外市场搜查或遍附件。准备者未授最终采用。

## 5. resume_mar17非准备者有限Source/actualowner/PRE

实际独立打开exact-v1 §3–5 L103–233（必要pipeline/IC特征选择/T1–3/负控制/强legitimacy声明）、A/B L254–279、C.1 L317–350、D L391–433，current abs为同二作者单v1/FinAI2026 workshop说明，无重要修订信号。未读完整全部prompts/图像/代码或复现。A260真实承认未做匿名vsraw直接消融，202–204只固定人口/价格/费用后跨截面打乱GNN分数，218却称legitimacy。独立反例score=y_future使原相关完美，任何破坏样本对应的shuffle同样降低相关，所以控制不能识别合法与泄漏来源；反例不是断言实现确实泄漏。

B273访问Sep–Oct2025与C328–332 cutoff提示不能回滚参数知识；仅模型访问晚于测试日也不证明实际含未来训练资料。142 holdout筛选feature与170–171冻结超参OOS不是同一资格，必须分开发反馈与最终证据人口。D396–397训练/验证/eta/costscale变更真实，不能与主表拼成同配置扩窗；D全期Sharpe亦低于多对照，风险反侧和10bps非总费正确。原两literal/static没有采市场收益或匿名化因果，采用边界可分采，不必把整篇中心主张授通过。

actual Ch66完整145–177的文件权限→DSGym输入data-withheld负控制→任务切片，641–665污染sensor/运行访问路径与3337–3351历史公开claim/cutoff交接逐段实读。DSGym既有输入移除不授全部grounded，但没有输出score-shuffle同时破坏合法与泄漏对应的具体反例，TimeSPEC已有参数未来分责不替代该差额。sole位置159完整DSGym限制后/任务难度切片前成立；不是仅主题相同就NC。原两literal与静态注逐字有限PASS，原5不变，待root窄锁/实际非writer POST；未写不计I或DAY。只一次原精确请求用于未采legitimacy重开，不扩金融研究。

## 6. 准备者实际窄写（resume_review17_18，非POST）

root soleCh66本family原两literal/static窄锁后，写前实际完整145–175及章尾，原两段逐字写新161/163（DSGym完整159后/任务难度165前），本人静态注6011。写后实际完整151–176和章末9顺读，原PRE边界与共存链保持；scoped只两正文+静态注、限定diffcheck0。交resume_mar17一次nonwriter实际正文/完整两侧与本人/邻注POST，不以writer读回代POST，不自计I/DAY，不新增流程身份注。

## 7. resume20_author_new一次非writer实际POST（2026-10-12恢复）

复用原§5已通过必要Source/actualowner/两PRE，不重审源或更改静态身份注。实际完整149–173及6003–6011顺读：RubricCritic代理/权限隔离→DSGym输入data-withheld→新两段输出score-shuffle/匿名化与选择人口分责→任务难度切片衔接成立；末注保原采用边界与邻注独立，不删并发03-24材料。实际机械逐字比对原两literal各唯一1份，正文161/163；原static唯一1份在6011，family marker仅正文与静态两份。仍只采用结构诊断，不授无泄漏、匿名化因果、真实理解、交易收益或生产保证。限定diffcheck退出0。一次nonwriter actualPOST有限PASS，待root接纳/释放Ch66本family，不预支I或DAY。

