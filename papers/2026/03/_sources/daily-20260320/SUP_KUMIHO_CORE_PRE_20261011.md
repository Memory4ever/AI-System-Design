# Kumiho17244：有限接口/评价边界准备

仅03-20补03-19自然日；作者resume_mar17。batch6完整题摘/日级夹证及原2+2+2=6复用，不把v1封面Mar17/Submitted当first-public。当前官方abs仅v1、未见具体撤回纠错，不扩版本史。尚未独立Source/PRE裁定、未写Books/POST/safe/DAY。

## 1. 必要原证与停止

[exact-v1](https://arxiv.org/html/2603.17244v1)。实际必要§6.3–6.5/324–432（URI、item/revision/tag及typed edge）、§8.2–8.8/816–968（derived index、融合、版本过滤及client重排）、§9.1–9.6/969–1072（cursor、batch、guards），§15.2–15.3/1242–1372及15.6/1384–1423（关键评价/真实冲突反侧）、15.9–16.1/1449–1479；§7.6末与7.7/772–811只核采用边界，不冒完整AGM证明通过。支持与直接反侧够有限接口即停，不读56页全部附件/代码/旧史；未复现。

## 2. 有限采用与反侧

稳定Item下保存immutable Revision；可变tag选择当前视图，Supersedes保存替代链，Derived_From/Depends_On用于追溯和提出重验集合。这里有三份不同对象：tag指定的视图、retrieval可返回的历史revision、当前消费者实际选中的证据。§8.6历史revision若仍带活跃tag可返回，§15.6真实案例旧blue分4.70高于新black3.27；当前用agent提示偏最近，不是server自动化冲突裁决。原图只为结构接口提供证据，不认证内容真实或依赖闭包。

§15.3入库时生成3–5假想未来情境供词面与向量索引，并提取事件/后果；它们是derived recall线索，不是未来事实或真实因果。§8.8先cosine过滤siblings，再把title/summary/facts/events/implications交当前agent选择；客户端无单独reranker调用不等输入token/推理/维护零费用。并行asyncio也只可能隐藏部分墙钟，不保证新增工作免费或零critical path。

§8.5 Eq12由分数较高推precision不降不成立：k=1、同type权重，相关a的两路分(.9,.1)，不相关b为(.2,.95)，两路各自top1分别a/b，max融合选b，低于最佳分支。未量化的“充分校准”须有能排除此例的相关性条件；数值大小自身不是真值。该保证与全AGM证明均不采用，非整篇贡献EX或降分。§9.4批动作组合亦明确无整体AGM保证，§15.9承认LLM持续偏差可缓慢腐蚀图，50%限额/保护tag不保证事实正确或零损失。

评价按人口分账：LoCoMo四类1540题token-F1与446题refusal phrase二值测量不等同；open-domain低于若干出版结果，跨系统未同底座/硬件重跑。Plus完整401与旧200的组合前后比较，不隔离单模块因果；6检索miss和21答案fabrication不能全写成answer-only缺口。相同检索context使换answerer不改变本次recall，并非任意模型/库变化不变定理。四同人口消融仍planned；合成cue-trigger与GPT-family对齐、私下mid80s复现仅作者转述，不授本人独立复现。声明14美元与所列费用和非同口径，另未给完整平台precision/尾延迟分布/throughput/每belief内存；客户端判断、入库增强、所有查询/图导航/失败/回归都计入全费。§10.4已承认PII漏检与metadata再识别，不采“只存摘要消除泄漏”。

必要强claim一次重开请求：明确形式belief/tag集合到实际历史候选与LLM选择的条件桥、Eq12足以排除上述替换反例的校准条件；同401人口独立消融/原源支持审计和matched全部费用。该请求不阻塞有限版本/读取接口分采，也不授正面强理论/Evidence保证。

## 3. actual唯一owner与差额

实际读[Ch77](../../../../../books/part-07-agent/77-memory.md)157–227、248–296、1167–1204；[Ch59](../../../../../books/part-06-ai-infrastructure/59-model-registry.md)1–150及Ch76/78入口。sole `AGENT-MEMORY`。Ch59已有immutable modelversion/mutablealias，Ch77 1172–1190已有双时态/版本与store-index分叉；193扩词非事实、259未来承诺ledger、278图边非真值也覆盖基础限制，不重复成熟机制作为新段。具体尚缺的是**当前tag/历史revision候选/消费选择三者不等价**，以及同一memory的versioned sibling metadata重排不继承权威视图。拟1190完整bitemporal限制后/1192Rollback标题前两段，只补实际读取失效边界与费用，不另设owner或复制registry治理。

## 4. 两段 literal PRE 与静态注（待非准备者）

版本化存储还须把当前视图、历史候选与实际消费分开：稳定item下的不可变revision保存证据快照，可变tag指出选定视图，supersedes和来源边保留更正链；但历史revision仍可为回顾查询保留活跃tag，检索分数也可能把旧判断排在新判断前面。一条[图原生记忆的受限案例](https://arxiv.org/html/2603.17244v1)就返回了分数更高的旧偏好与较低的新偏好，再由消费者根据时间元数据选择。能定位版本不等于已经裁决冲突；用于当前行动时应回指所消费的revision及其可见性/有效性依据，历史查询则显式保留as-of意图，不能用最高相关性静默替代当前权威视图。<!-- source-family:SF-2026-ARXIV-2603-17244 -->

这一分支还在写入时生成假想未来情境和事件摘要作检索线索，再以embedding预筛同item的siblings，让消费模型从结构化metadata选择；假想情境不是未来事实，提取的后果不是因果证明，模型重排也不取得写入或执行权限。它增加增强、索引、候选输入、模型选择与回归费用，复用已有调用或并行生成不等零成本。有限评价尚未在同人口隔离各增强贡献，旧revision排名、同源抽取/判分和持续consolidation偏差仍可失准；保守删除限额只限制单轮损失，不认证记忆真实。版本冲突、来源或预算无法核验时，保留原始episode与完整更正链，回退显式版本解析、普通原文检索和独立内容核验，不由图结构、融合分数或更高recall签发答案正确性。<!-- source-family:SF-2026-ARXIV-2603-17244 -->

- `SF-2026-ARXIV-2603-17244` — [Kumiho exact-v1](https://arxiv.org/html/2603.17244v1)，必要§6.3–6.5/§8–9、§15.2–3/15.6/15.9–16.1；只采tag视图/历史revision候选/消费选择分责及derived增强/重排费用。强AGM全链路、max融合precision不降、零成本/零泄漏、模块唯一归因及生产SLO不采，保旧revision排序反侧/同源偏差/全费用；未核代码/复现。

准备者不自PASS；原两PRE/static交非preparer有限源/actual差额裁，批准后root另授窄锁，actual非writerPOST后才归并。

## 5. 非准备者必要 Source / actual owner / PRE 裁定

root 实际核 exact-v1 header/完整摘要、§6.4、§8.5–8.8、§15.6、§15.9–16.1；§15.3只补读拟采增强、人口与成本的相关位置，不声称完整审过其全部内容或 §7 的全部证明。独立 DataCite created 03-19T02:27:34Z / registered 35Z 与本批公开日夹证相容；不以封面或 Submitted 当 first-public。支持与直接反侧足够，此层停止。

实际 Ch77 1167–1207 完整交接、原两 PRE 及本人静态注逐字核：现有双时态/索引分叉尚缺当前 tag 视图、仍可检索历史 revision 和实际消费选择的具体区别，邻接可承载，不重复基础不可变版本/alias 原则。§15.6 明示旧 blue 4.70 高于新 black 3.27，冲突依赖消费者时序选择；§15.9 明示形式 belief base 不等检索子集、偏置 consolidation 可渐进腐蚀，§16.1 四配置消融仍计划中。受限接口可与强 AGM、max-fusion 保证、零成本及零泄漏宣传独立分采。

必要 Source、差额与两 PRE PASS，原 6 分保持。授权 resume_mar17 sole Ch77 在完整双时态限制后、Rollback 标题前窄写两段及本人静态注；写后 root 一次实际完整局部和注 POST。尚未实际写入，不计 Integrate 或整日 DAY。

## 6. sole writer 实际落实

resume_mar17按root唯一Ch77本family窄锁，仅将§4两literal PRE写在原1190完整bitemporal限制后、Rollback标题前；静态本人注放当前末尾，不改其他family/身份流程注。写前实际1167–1207完整邻接，写后完整1180–1212及尾8顺读，current/historical/consumer分责与rollback/transaction/state恢复责任自然衔接。采用边界、强AGM/max保证隔离、非零成本/泄漏与退路近文；两literal/static无语义扩写。限定diff/check0，交root一次nonwriter实际完整局部/本人注POST，未自计safe/DAY。

## 7. 非 writer 实际写后验收

root 完整读回 Ch77 实际1180–1212及本人末注/末八行，与已核两 literal PRE 逐字比对。当前视图/历史候选/实际消费分责实际承接双时态段，后续 rollback、transaction 与计算状态恢复未改；假想线索非事实、持续偏差与费用/回退边界近文保留。正文、完整局部交接和本人静态注 actual POST PASS，接纳本项实际 Integrate，释放 Ch77 窄锁；不授其他 family 或整日 DAY。
