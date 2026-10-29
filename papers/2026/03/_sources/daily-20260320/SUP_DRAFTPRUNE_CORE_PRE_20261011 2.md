# DraftPrune17233：形式化候选的答案集合门与语义验收

resume_review17_18，2026-10-11，仅03-20补03/19。root明确sole必要准备，author不重复core；原批6准入/date和2+2+2=6有效复用。恢复实际重读AGENTS/适用研究与Report合同/Prompt、每日Sources、ROADMAP、本日README/STOP及Books约束。准备者不自授Source/PRE、safe、DAY或Books写权。

## 1. 必要原证与实际停止

独立读[exact-v1](https://arxiv.org/html/2603.17233v1)§2.3/§3 L104–160、关键§4.1–4.9/T1–4/Eq1–3 L162–276、§6–7 L280–295、A12失败L466–501、A13必要split说明504–506/539、A14成本542–559、A15 timeout560–585及A17必要slot/backend630–687。图仅文字/图题，不冒图像曲线；A4–6只见附录路由/图题，不用于当前裁决，未读完整附件、相关旧文、代码或复现。

当前[official abs](https://arxiv.org/abs/2603.17233)完整AB/history实际读，Mar26 v2但未见具名撤回/纠错声明，完整AB仍同拟采用机制；版本号本身不触发全diff，不将提交或修订替已核本日公开归属。

## 2. 采用边界与直接反侧

v1§3路径为NL计划→条件formalization→有限solver-feedback修复→逐hypothesis查询→保留答案集合单元素→答案投票，任务需有单一答案合同。零/多元素只是编码下的答案集合不满足合同，不等原始premises被证明逻辑矛盾，也不证明单元素编码faithful。共享生成器、未按symbolic equivalence去重仍可能把同错编码重复计票。

T2 GPT4o单路径39.9低于CLOVER46.8；T3 LogicalDeduction加draft98.23低于98.60，T4 PrOntoQA剪枝99.32低于99.34。A12存在非空但全错集合和有正确候选却投错，两者直接反对普遍语义保证。coverage@k是有任一路最终答对的诊断，不是部署可识别oracle。ExecRate把剪枝纳入valid条件，须保过滤前人口，不能用过滤后Acc@Exec代全问题准确率。

A14每路径tokens及k的对照不等matched全部预算：同k约三倍tokens，另有solver/repair/网络/墙钟，未给平台precision/batch/concurrency/tail/SLO完整配置。A15 Z3/CSP有不同timeout、PyKe无外部timeout，不签统一deadline；10runs只所测人口。A13修正230→229及8标签是作者审核口径，不与主表原split无条件合并。Ties按first出现处理，不是验证；系统性漏译/错误量词仍可穿过单元素门。一次强命题请求仅绑定NL→plan→编码的独立faithfulness样本、保留/被剪人口及等价去重、固定split/完整预算与deadline，不为有限接口补造执行实现。

## 3. actual sole owner 与具体差额

实际读[Ch79](../../../../../books/part-07-agent/79-planning.md)完整156–202与1–23，Ch78/80入口；sole `AGENT-PLANNING`。现TAPE feasibility/execution分离、可复用domain artifact、目标关系协商、predicate-first签名/arity和ARGOS补前提已有强语义责任，但未具体承载“NL计划采样多编码→按声明问题关系得到答案集合→单元素门→保留者答案投票”的候选支持/聚合分工。初始Ch48 draft词搜索仅排歧义，不作为该机制owner。

拟原189 predicate-first完整限制后/191 ARGOS补前提前两段，保签名检查与补前提分支共存，不复制工具effect权限或benchmark库存。是否已有覆盖/需整合由非preparer裁，不因局部反退改EX/降分，也不把所有中心强主张采用。

## 4. 两段 literal PRE 与静态注（待非准备者裁）

形式签名约束之外，还可把候选支持与答案选择分开：先对同一问题采样自然语言建模计划，在各计划条件下生成并有限修复求解程序，再按问题指定的逻辑关系查询候选答案。只有任务确实要求单一答案时，才把该编码得到的答案集合恰含一个元素作为保留门，最后对保留路径的答案投票。空集合或多元素说明这条编码没有满足当前答案合同，不自动证明原问题逻辑矛盾；单元素和多数票也只属于生成编码，不能反过来证明实体、关系与量词忠实于原问题。原问题、计划、编码、查询关系、修复和被剪路径应可回指，语义资格仍另行验收。<!-- source-family:SF-2026-ARXIV-2603-17233 -->

[形式化候选筛选的有限对照](https://arxiv.org/html/2603.17233v1)支持局部支持集与聚合取舍，不授所有任务普胜：保留集合仍可能全错，也可能已有正确候选却被投票淹没；未按形式等价去重会重复计算同源错误。可执行/通过筛选比例、过滤后准确率与全问题结果须分账，并保留剪枝前人口。多计划、程序生成与修复、全部solver查询、投票和fallback共同付费，更多路径或较低timeout比例不证明严格deadline/总预算收益。系统性漏译、无可靠单答案合同、共错或费用失配时，回退原形式接口、可信语义检查/澄清、明确Unknown或标明best-guess身份的直接回答，而不让求解成功自动授权事实与真实执行。<!-- source-family:SF-2026-ARXIV-2603-17233 -->

静态注：

- `SF-2026-ARXIV-2603-17233` — [Draft-and-Prune exact-v1](https://arxiv.org/html/2603.17233v1)必要§3、§4/T1–4/Eq1–3、§6–7与A12–15/A17接口。仅计划条件formalization→任务答案集合单元素筛选→保留路径投票的受限分责；保语义漏译/单路径与消融反退、过滤人口/全错与误票、等价重复、split与全费/timeout边界，不采faithfulness/通用可靠或完整执行保证；未核代码/复现。

准备足即交resume_mar17非preparer必要Source/actualsole差额/原两PRE裁；未授写前不动Books，不自PASS或预支DAY。

## 5. 非准备者必要 Source/actualowner/PRE

resume_mar17仅本20独立上下文，实际exact-v1必要§2.3/§3（104–160）、§4/T1–4/Eq1–3（162–276）、§6–7（280–295）、A12（466–501）、A13必要504–506与A14–15（542–585）支持/直接反側；原packet额外A17接口范围只属准备者实读，不冒本人全读。actualsoleCh79完整154–207、Ch78/80入口顺读，原两literalPRE/静态注逐字回对，有限Source/sole差额/PRE PASS，保6。任务指定entailment/contradiction/consistency关系与单一答案合同下的支持集合门，不证明原KB矛盾或NL语义，单元素/多数票也不是真值。T2单路径弱、T3/4反退、A12两种剩余全错/误票、无等价去重、先过滤人口与不同timeout/fullfee均准确。与predicate-first签名及ARGOS补前提有具体支持集/聚合差额，原189后/191前成立；不是主题NC，未授写入/POST/safe/DAY。不扩全部附件/图像、旧文或版本diff，支持与直接反側已够采用即停。

## 6. sole writer 实际落实（待非 writer POST）

root明确授resume_review17_18唯一Ch79本family窄锁后，恢复本20 AGENTS/适用合同、ROADMAP/Books约束、本日README/STOP与有效§5独核；实际回读predicate-first完整边界及ARGOS两侧后，仅原两literal PRE写新191/193，静态源注596。writer实际完整173–213与585–596本人/SwarmAgent/ARGOS/Ares邻注逐字回原PRE，scoped本family只有两正文+静态注、diff-check0。原solver/domain/predicate-first、ARGOS与trajectory refinement/search交接保留，语义资格/过滤人口/投票与全费边界近文。交resume_mar17一次实际nonwriter POST；不自授POST、safe或DAY，不循环更改Books人员身份注。

## 7. 非 writer 实际 POST

resume_mar17 实际完整 Ch79 175–219（新191/193与domain/predicate-first、ARGOS和search两侧）及585–596本人/SwarmAgent/ARGOS/Ares邻注顺读，逐字回有效两literal PRE、静态注和本人已核必要原证，有限 actual POST PASS。单一答案合同下的编码支持集门与保留者投票不授NL faithful、原KB矛盾或真值；剩余全错/误票、等价重复、过滤前人口、不同timeout和全费均近文，既有语义/补前提/真实执行责任未混淆。限定diff-check无输出，不改Books流程身份，不自授本Report/DAY；请root接纳后释放Ch79本family锁。
