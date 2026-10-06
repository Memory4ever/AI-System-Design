# 03/11 IH 必要证据与 Books 差额

Source Family：SF-2026-OPENAI-20260310-IH-CHALLENGE。事件为[官方核心说明](https://openai.com/index/instruction-hierarchy-challenge/)；实际official RSS Tue,10Mar2026 11:00GMT=2026-03-10T19:00:00+08，确定本窗。[arXiv:2603.10521v1](https://arxiv.org/html/2603.10521v1) Submitted=2026-03-11T08:27:09Z，窗后发布的补充证据，不改官网事件时间，也不把laterpaper内容冒充当时全部已公开。

准入：角色优先级失败往往与题目本身困难、judge不一致混在一起→官方用简单underlyingtask、Python objective、避免universalshortcut的合法控制与在线低role攻击→需要重新考虑合成冲突监督的规则/grader/攻击输入职责，而非把成熟role排序计为新贡献。2+2+3=7，深入必要内容；不以OpenAI权威或安全标签授高分。

## 实际读取的必要位置

- 官方完整core说明：简单任务解耦underlyingreasoning、objectivePython评分降低modeljudge偏差、无固定拒答捷径；“no capability regressions”小标题和ChatWinRate/Preference负数字并存。
- v1 §3.1/Table1：2–6约束的simpletasks，闭式答案依赖输入，合法同类请求anti-overrefusal。高角色规则与grader冻结后低角色才被attack，攻击后仍需任务simple。ASTnormalization/static检查、passfailexamples/manualreview降低不一致，不证明完备grader。
- §3.2：frozenunsafeattacker反复propose/evaluate/revise、面对currentdefenderfeedback，固定预算但次数NotDisclosed；RL多输出Pythonreward并混capabilitydata。rule/role/grader/attacker/defenderrevision须分离。任务split/训练/搜索总预算未明确，不授预算匹配。
- §4.1–4.4：staticheldoutimpersonation/automated/human不是adaptive。Table2 ChatWinRate0.71→0.66、Preference0.46→0.40、TensorTrustoverrefusal0.91→0.90；GPQA0.83未变/AIME0.93→0.94不能覆盖负向任务。无统计显著或普遍无回归结论。OOD部分用LLMjudge，不继承Pythonindependence。内部staticPI0.44→1.0而CyberSec2 0.88→0.91不能授通用adaptive保证。
- §5.1/Table6：All robustness0.941/overrefusal0.950/safety0.957/helpfulness0.773；removeAnti0.957/0.831/0.974/0.613；hardersplits0.924/0.899/0.957/0.751。只能支持反过度拒绝分账/受限ablation，任务split和预算未知，不授等预算因果、universallyoptimalmixture。
- §5.2：monitor/rewriter/BestN4secondmodel受限配置；弱baseline鲁棒性可改进，已训MiniR额外收益小而capability代价更大，某些两者更坏。附加防线不是freeimprovement。
- §5.3–5.4：adaptiveRLattackASR会升高、monitor有助，但static饱和不等于adaptive胜率；human127workers、10systemtaskcombos、17workers大多数combo、bounty30。Mini271tasks/32.84attempts/0.362success，MiniR265/52.39/0.117，monitor268/43.08/0.071；不同attempts不是matchedqueries，不将人类attempt百分比当一般binomialASR或production安全。

不机械读全附录/所有代码；必要命题/关键反证已足。未复现实现，不采强性能或部署保证。

## 实际 owner 比较与写入

- TRAIN-DATA / Ch27 SyntheticData 首段当前303–308：generator/judge同源blindspot与specificationcompilation，可承载新监督职责；具体缺的是高role约束/grader冻结与lowrole攻击，以及合法同类控制防universalrefusal。
- Ch72既有conditionalattack/authenticatedprovenance与Ch66已有static/adaptiveprofile对该旁支已经承载，不重复写入。不是因“有主题”机械NoChange，而是新delta已在Ch27唯一owner落地。
- Root授权Ch27首段后/IID前两短段+chapter-endnote，本轮实际正文当前309/311。保存旧generalmodeljudge适用条件、grader非完备、onlinecost、预算限制及fallback，不静默替代成熟合成流程。
- **root非作者实际POST通过**：实际对读Ch27新增两段+285–335前后及章末，与已实际官方core、v1§3.1–3.2/Table2/Table6匹配；无genericguarantee、matchedbudget或static授权外推。本日日级Gate另行，不以POST冒充source覆盖通过。写锁释放。

本次风格工具发现无可用write-like-mecontextfetcher，依显式AGENTS/WRITING_GUIDE和现有章节术语写窄机制，不宣称取得用户风格profile。

