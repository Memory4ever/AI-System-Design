# PASTE18897 exact-v1 必要Source / sole owner / PRE

准备者resume_mar18，2026-10-11，只本21补BJT03/20；首批准入/date夹证可复用，精确v1题为Act While Thinking，不混currentv3标题/数字。当前合同/ROADMAP/Book背景实际重读，未写/未计safe，2+2+2=6，以具体owner差额定点深入。

## 必要原证与直接反侧

[v1](https://arxiv.org/html/2603.18897v1)实际§3–6/Algorithms1–3/Table1/2和§7.1–7.7。控制流由tool类型/status的有序结构表示，参数flow由少数symbolic transforms（字段/路径、index/fallback、格式化）从历史payload晚绑定；历史validation用上下文匹配次数作分母，预测调用实际发生且f成立作分子。是经验消费概率，不是副作用安全或新session参数正确性认证。Definition的order-preserving subsequence与§4.3suffix匹配口径、Alg2总调用f与正文partial/no-f分支未完全明确，不自行补精确matcher/缺参执行recipe。

authoritative与shadow两队列；toolname+argumenthash匹配已完成cache或join in-flight后晋升，未确认结果不能注入history。§5.2用户显式default deny：完整且policy声明side-effect-free才full；partial只warmup/preparation；副作用仅dryrun/staging变体，不自动infer safe。dryrun/staging结果与真实调用是否等价仍须具体后端验，不采调用名/argshash足以跨session/state/auth复用的普遍correctness。优先级/slack/preemption只是有限policy设计，取消不是恢复已发网络request/不可逆effect；不能由Algorithm3“先Abort再Release”推出瞬时无干扰/绝无延迟。估计cost/duration/confidence、匹配/缓存/checkpoint/被取消工作都付费。

4nodes/每node96EPYC7V13vCPU、512GB、8A10080GB/总32GPU；Gemini2.5Pro/GPT5.2 API、QwenDeepResearch30B本地。原称配置相同/timeoutretry一致，历史mining与新任务disjoint；没有精确task数/split、modelrevision/temperature、servingprecision/batch、各load点绝对rate/重复seed/CI、完整缓存有效键、API费/取消完成时间等必要生产字段。AzureFunctions arrivaltrace重放只给agent arrival，不是productionAgent验收。

三bench DeepResearch/SWE/ScholarQA，后者只作通用tool系统实验上下文，不开展领域科学知识。§7.2**up to**48.5%平均latency reduction、p95/p99最多48.6/61.9，汇总平均speedup1.25/1.32 overORION/SpecFaaS；摘要48.5不能改成普遍平均。§7.5最多top1 27.8/top3 43.9/overallhit93.8三个最大值未定位同配置/分母，overall以多候选轻载预算定义，不授低top1下无代价93.8命中。§5.2同tool最多留1instantiation不等所有tools总候选1，top3与hit不是同一候选预算。作者有限20k+投机动作602潜在effect被阻止、无finalresultdivergence，但没有oracle能力或外部effects全验证/泄露/并发stress完整依据，不授任意安全/语义不变。§7.7每节省1s报告.02core-s/2.6MB/.9MB、moderate1–3idlecores/250MB、selector<100ms，只作作者局部计费边界，不写cost-free/生产SLO；没有artifact核验，v1称review后开源。

## Actual sole owner 差额

唯一AGENT-TOOL-CALLING Ch78，实际730–793完整symbolicbinding→toolbehavior→predictablecall→semanticdraft→AST/async→typedcatalog交接，Ch77/79开篇。现758–761要求symbolic future唯一、exactaction/schema/version/auth确认，775–777有partialinput/可取消与policy gate；尚未解释**从多条历史结构匹配中提议tool类型，同时另以当前真实payload做symbolic晚绑定，再按完整程度分别只准备/执行**。这个两阶段prediction接口有支持，非成熟exact-confirm本身新增，不能将模式概率转授权。拟只758–763原段/marker后、765semantic-draft分支前一段，不写Ch56另一个调度owner。

## 一段逐字PRE

若下一条调用尚不能唯一确定，先行工作还可以把结构预测与参数求值分开：从历史 tool 类型/status 序列提议候选，再用当前已完成事件的真实 payload 按字段、索引或格式规则晚绑定参数；模式的历史命中率只给资源投入排序，不授执行权限或当前参数正确性。完整且经 policy 声明可安全预取的调用才进入 shadow 执行；缺参数时只准备 runtime，副作用操作只允许已验证的 dry-run/staging 变体。真实 actor 随后发出匹配调用，executor 再检查状态、schema、身份与权限，才能复用已完成结果或晋升在途工作，不能仅凭 tool 名与参数 hash 跨环境提交。[受限原证](https://arxiv.org/html/2603.18897v1)支持这种预测—晚绑定—确认分工，不证明取消可瞬时回收全部资源、任意副作用隔离或生产无干扰；模式采集、匹配、缓存、额外调用和废弃工作均付费。历史失配、状态变更、无法撤销或净费用不合算时，保留完整调用后串行执行，不用高预测置信度替代 effect gate。<!-- source-family:SF-2026-ARXIV-2603-18897 -->

## 静态注PRE

- `SF-2026-ARXIV-2603-18897` — Daily2026-03-21补03/20；[PASTE exact-v1](https://arxiv.org/html/2603.18897v1) §3–6/Algorithms1–3、§7.1–7.7。2+2+2=6，必要差额深入：结构候选/当前payload晚绑定/完整程度policy分责；不采subsequence/suffix精确recipe、toolargshash全状态身份、瞬时preemption/无干扰或任意副作用安全。有限配置/trace、hit人口/预算、up-to vsaggregate与完整投机费用近文，未核artifact/复现。

待非preparer必要Source/actualowner/PRE；未授锁，不计safe/DAY。

## root 非准备者 Source / actual owner / PRE 正式通过

root实际独读v1 §3–6和§7必要config/7.5–7.7反侧、actual Ch78完整局部与Ch77/79交接，正式限定PASS。结构预测→当前payload晚绑定具体差额成立；subsequence/suffix与Algorithm2 partial歧义不采精确recipe，tool+argshash不是完整state/auth键；top1/top3/overall不同预算、20k/602不授任意安全、取消不等瞬时无干扰，原一段PRE/静态注保留这些边界准确。root授Ch78仅原一段＋静态本人源注窄锁，writer实际写后交root一次nonwriter完整局部/本人注POST，尚不计safe或DAY。

## 一次 root nonwriter actual POST：正式通过

作者按原逐字PRE写actualCh78新765及静态本人971，writer完整754–786与963–971读回/限定diffcheck准确。root随后实际完整同局部与本人/邻注，逐字回对原PRE及有效Source正式PASS：unique symbolic call→结构多候选/latebinding→semantic不同action→AST/async顺读分责准确，命中非权限，完整/partial/effect分别gate，state/auth独立核与费用/有限安全反侧保留，静态注准确。root正式释放Ch78窄锁，允许归并单项实际I；不再改注加入验收身份，不授DAY。
