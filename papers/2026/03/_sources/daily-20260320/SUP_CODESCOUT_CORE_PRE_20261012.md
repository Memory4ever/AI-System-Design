# CodeScout17829：搜索策略、结构化提交与定位消费分责 / 必要准备

准备者resume_review17_18，2026-10-12，仅03-20补03-19。author明确sole分配，原2+2+2=6及SUP_AGENT_TAIL_ADMISSION_PREP§5准入/date有效复用；本稿不自授Source/PRE/Books/safe/DAY，交author非准备者有限核。

## 1. 实际必要Source与停止

[exact-v1 HTML](https://arxiv.org/html/2603.17829v1)已实际读完整AB L55–59、必要§3 L103–140；训练设置L159–173，关键§4.2–6/T3–6 L174–313；A工具schema L373–386，D限制L458–465，E直接优化反侧L466–492，G固定TopK对照L513–533。current abs L8–30同题十一作者、完整AB、单v1及无具体Comments/撤回轻量实际核。恢复复用身份/命题不变的原证，只回已存§3决定性接口，不重读全部core。未核artifact/代码/复现，A/H图中完整prompt像素、F示例、E其余无关配方不冒完整读；支持/直接反侧够本命题即停，不扩query或版本史。

## 2. 关键机制、对照与有限采用边界

任务不是直接修复：给issue与pre-PR仓库，用gold patch改变的file/module/function集合产生三粒度F1奖励；筛除创建/删除文件、非Python和空issue，docstring变化忽略。普通Unix terminal消费代码，再调用独立LocalizationFinish结构化locations；“one tool”不应抹去finish接口。结构化提交减少脆弱字符串解析产生的奖励噪声，但不保证提交相关或内容正确。14B另加exactly-k-turn终止奖励，非任何≤k均同奖；预算耗尽未finish的rollout loss masked。并行调用aux伤害有限表现，只留提示；不把这组recipe授通用训练最优。1.7B另先teacher RFT，模型间训练人口/预算不同；GSPO/advstd消融有三粒度升退，不授唯一优算法。

评价绑定Verified500/Lite300/ProPython266、instance-average三粒度precision/recall/F1。专门graph baseline数字取自原论文，固定Top5/variable count也不同；OpenHands-Bash开放模型4/6提示turns但backend15，closed backend6，final reminder改变是否提交。closed+reminder在这些任务优于CodeScout，Pro file的32B RepoNav高于4/14B；14B也非所有粒度优于4B。因此小模型/terminal分支有受限对照价值，但不能认证尺寸、工具数量或训练算法的单因素因果、全质量替代或同预算普效。

§6将14B预测定位名输入另一个issue solver，有限resolution有改善但低于gold-location oracle；solver自己的tokens/steps下降不说明计入定位器、训练、搜索、解析及全部工具后的净费用/latency下降。D明确Python-only、gold patch不包含相关但未修改的上下文，三粒度F1不是完整支持，更不是真实修复成功。额外库数据是否与预训练重叠、全cost/CI/precision/concurrency/SLO未在必要证据中闭合，不授强性能或统计保证。

研究setup因为“不执行仓库代码”而未使用sandbox/container；这不认证任意terminal命令没有副作用或生产最小权限。A的security_risk枚举是提案字段，非真实authorization。实际命令频率以rg/sed为主也不证明执行器强制只读；权限/隔离应由可信执行器而非学习policy或自报风险掌握。这是对论文边界的系统推断，不称作者已实现该控制。

## 3. actual sole owner / 具体差额

唯一`AGENT-TOOL-CALLING`，[Ch78](../../../../../books/part-07-agent/78-tool-calling.md)。实际完整70–105 typed parse/authorization/finish、118–145 compiler/真实trace与ToolDiscovery接口，178–212 interface granularity段及两侧顺读；Ch77/79入口实际读，不将库存遍历。已有generic terminal与narrow tools共存、typed格式不等effect授权很强；本差额不是再讲成熟治理，而是训练后的terminal定位仍需独立finish提交、patch-derived支持集合的三个粒度不等真实修复，终止/输出预算会改变有限排名与消费资格。

拟原Ch78 194–195 Terminal Agents完整段后、原197 browser身份fallback前两短段。与Ch79 planner、Ch77持久memory和Ch33训练算法交接分开，不复制GSPO推导、全recipe或静态graph流程。非准备者可据实际覆盖裁specific NC，不能以主题相似关闭，也不为制造diff硬写。

## 4. 待非准备者裁的两literal PRE / 静态源注

普通 terminal 是否够用，也要区分搜索动作与最终提交。一个受限仓库定位分支把 issue 和 pre-PR 代码交给经任务训练的搜索策略，用 Unix 命令找候选，再通过独立的结构化 finish 提交文件、类/模块和函数集合；它不是让 shell 自己判定问题已修好。[有限定位对照](https://arxiv.org/html/2603.17829v1)以 gold patch 的改动位置计算三个粒度的 F1，减少自由文本格式噪声，却会漏掉相关但未修改的上下文。格式可解析、搜索相关和真实修复成功因此需要分别验收；下游 repair 仍须真实测试，不让定位集合取得功能正确或执行授权。<!-- source-family:SF-2026-ARXIV-2603-17829 -->

这种接口也不能只凭模型尺寸或“单工具”名称替代既有 scaffold：完成提醒、turn budget、输出集合大小和训练过程都会改变定位排名，受限任务中更大或 closed 模型仍有优势。定位器调用、训练、仓库搜索、解析和下游修复都计费，solver 自身少用 tokens 不等端到端更便宜。仅 Python、patch-derived 标签与不同对照预算限制迁移；研究环境没有 sandbox 不能推广成生产无需隔离，自报 risk 字段也不成为真实权限。复杂依赖、相关上下文遗漏或高风险 effect 下，保留既有静态图/索引、可验证的窄工具与可信执行器，只把该分支作为有独立 outcome 检查的定位候选生产者。<!-- source-family:SF-2026-ARXIV-2603-17829 -->

静态源注：

- `SF-2026-ARXIV-2603-17829` — [CodeScout exact-v1](https://arxiv.org/html/2603.17829v1)必要§3–6/T3–6、A工具schema、D限制、E直接优化反侧与G输出数量对照。仅经任务训练的terminal搜索→独立structured finish→三粒度定位与真实修复分验。保Python/patch遗漏、提醒/预算/训练与baseline混杂、反退及全部费用；不采单工具/小模型普遍替代、完整优化recipe、生产安全或定位等修复。未核代码、完整prompt图或复现。

## 5. 待非准备者必要核

交resume_mar17实际必要Source/actualowner/两literal/static裁，准备者不自核自己。未获root family窄锁不写Books；本稿不是实际POST/I/safe或DAY，不重复无关附件。

2026-10-12 resume_mar17非准备者实际exact-v1 §3/Eq1–4、§4 setup/T3–5、§5/6及T6、A工具schema、D限制、E关键优化反侧L466–492和G L513–533必要独读；未重读完整prompt图、全部训练曲线/示例或代码。独立LocalizationFinish真实存在，三粒度patch-derived F1与相关但未改上下文及修复成功不同；turn恰k辅助奖励、finish预算耗尽loss mask、1.7B teacherRFT和backend/reminder条件准确。T4 14B函数28.74低于4B29.03、closed+reminder优势及T6定位后仍低于oracle、solver局部token非全费用均保留。actual Ch78 70–105/118–145/172–227完整必要邻接、Ch79/66入口实际顺读；genericterminal/typed授权已有覆盖不替代任务训练搜索→独立finish→定位集合与repair outcome分验的具体差额。原两literal/static有限Source/soleowner/PRE PASS，唯一AGENT-TOOL-CALLING，原194–195 Terminal Agents完整段后/browser fallback前位置成立；原6/day保持。不采完整recipe、单工具/小模型普适、命令频率等最小权限或生产无需隔离；root协调窄锁后准备者写，author一次nonwriter actualPOST。

## 7. 一次非writer实际POST

2026-10-12 resume_mar17实际完整顺读Ch78 178–221（新197/199）及974–983本人/AdaZoom/PASTE邻注，逐字回原§4 literal及本人已核必要Source。interface粒度旧分支→terminal搜索/独立finish→browser身份fallback交接成立，未更动旧正文；patch F1不等完整相关支持或修复、closed/预算/提醒反侧、全费用及sandbox/实际权限边界近文。本人静态注真实scope准确，未更新人员身份或改Books。限定diff-check无输出，有限actualPOST PASS，交root接纳释放soleCh78本family锁；不授代码复现或整日DAY。

## 6. root soleCh78授锁后writer窄写 / 非POST

2026-10-12 root实际读author§5 Source/PRE有限PASS及当前完整邻接后，授resume_review17_18 sole本family Ch78两literal+static窄锁。writer先实际178–203/章末邻注顺读，再仅原两段写new197/199及static983，写后完整178–217和975–983本人/AdaZoom/PASTE/既有邻注逐字回批准PRE；interface branches→训练后的terminal定位/finish→browser观测主体身份衔接保持。实际scoped diff仅本family两正文+静态注六新增行无删改，该章diff-check无输出，既有并发修改保留。writer读回非actualPOST，不自计I/safe/DAY；交author一次nonwriter完整局部/本人静态注POST，不循环身份注。
