# 04104 PCAA：首次必要Source / actual Ch84最小PRE

最新行政状态：R75–76已实际完整读回，唯一actualPOST通过，04104真实整合生效、Ch84窄位释放，新增I16＋旧Kimi1合17。本人注/README已仅行政采用，不第三Source/PRE/POST；该pending行转整合后实际V3通过。下方待核/待POST均为提交前过程，不是当前待办；下一04896首次必要层与余三/有限title stop/DAY普通。

当前状态：reader R73–74已实际完整采用，首次必要/6分/actual Ch84/原两段PRE通过。root本轮新窄授后两段逐字真实保存于Ch84 Replay完整段后/Flat event log完整引入段前，加本人true-H2 Review notes一注；完整新增/直接完整两侧及本人整注已实际自读。下方“未授写/未SAVE/待首次核”为此前过程原记录，当前仅待唯一非writer actualPOST，未I/DAY，不第三原Source/PRE。

作者supp_20260605_author，仅Daily2026-06-05补Jun04。`SF-2026-ARXIV-2606-04104`；[Proof-Carrying Agent Actions: Model-Agnostic Runtime Governance for Heterogeneous Agent Systems exact-v1](https://arxiv.org/html/2606.04104v1)。R33–36完整题摘/贡献准入/精确v1 Jun04联合日证有效复用，不第三AB/date，也不把May31稿面或Jun02提交时刻单独当首次公开。官方exact-v1 HTML真实GET200/290859bytes，原件`SUP_2606.04104v1_20261025.html`，SHA256 `38d4e7e902313bce28b568fc8059bc40e3f3b6561285458a62a6d5db1bcc83f2`。

实际读取§3–8架构/五检查点/外部边界/neutral runtime contract/可携带envelope与proof，§9实现表面与限制，§10/T7–10评价及披露边界，§11–12与A/B必要实现/评价来源说明；§1–2用于定位其architectural novelty而非借用conformal定理。支持与直接反侧足即止，不打开完整SDK/产品历史/上游引用/无关附件，不运行实现或攻击。论文对实现的陈述是作者证据，不冒独立实现审查/复现；未公开benchmark本体不冒访问外阻，也不据此否定可检查的有限架构提案。

## 必要机制与采用边界

§3把单动作certificate拆portable envelope、runtime receipts、human approval/accountability、replay/proof、integrity五域。§5的guard→createAction→recordAssumption→waitForApproval（策略要求时）→updateOutcome使admission、决策依据与结果收口属于同一身份；checkpoint名字不证明真实不可旁路/原子性。§4最小化漏升级风险且受review预算约束是抽象目标；§2.3没有声称已实现conformal routing或给出全产品有限样本风险保证，不能把引用理论补成证书定理。

§5 externality_context包含destination visibility/ownership、tenant/account与client provenance、external write/sensitive payload/reversibility及approval enforceability；同一个verb指向个人账户或公司目标不能简单同判。它是需验证的决策输入，不是用户或agent自填字段即可授予scope。§6 neutral contract记录runtime family、adapter mode、effective execution boundary、authority split、session与receipt projection；gateway/managed/framework/tool-hook/observer的共同形状不证明共同控制深度，Proposition1只是非形式的closure比较，不是跨vendor执行安全等价定理。

§6.6明确四种approval enforceability：`pre_execution_gate`是OSuite或attached governor可在effect前暂停；`observe_only`是执行后或agent abort后导入，不能声称deterministic preemption；`delegated_runtime_control`是另一runtime-layer governor执行判决、PCAA保租户可见证书链；`runtime_controlled`是runtime控制下已执行但无hard前审门。分型需对应实际接入边界，schema声明本身不完成能力验证；delegated型还需独立可信governor及其证据，不能把“委托”写成平台已经自己阻断。

§7 portable envelope保action/tenant/agent/runtime/mode/boundary/authority、authorization/workflow/evaluation/externality/accountability上下文；runtime-stage可归一pre_input/pre_tool/post_tool/pre_output，并接approval actor/decision/workflow/timing/source。不同mode阶段可选，不能要求每个action都有所有stage，也不能因出现receipt自动认定原authority有效。§6.7 AGT是外部governor projection实例，不据品牌声称其版本所有部署已完整enforce。

§8 proof bundle是summary/evidence/projected verification/manifest，canonicalization覆盖subject/summary/evidence/verification后产生digest。Replay重算envelope、risk result、policy snapshot与manifest，检查缺证据、manifest mismatch、policy drift、risk drift；这是治理状态重放与比较，不是重做远端副作用或自动rollback。execution/pending/partial/non_execution proof保留暂停/拒绝/中止的收口类型；标签不独立证明开放环境真的未发生effect。必须按receipt可见范围判断，缺失实际effect证据保unknown，而非由“non_execution_proof”字符串解除阻断。

§8.5 receipt completeness的分母是声明的expected runtime stages；有expected时为observed∩expected/expected，无expected且有receipt则1，否则0。不能把这个数当认证完整性、未知旁路覆盖率或真实世界effect证明。§8.6 integrity/attestation lane与未来更强verification分开；manifest稳定只承诺所载内容对应，不证明内容语义真实、所有事件已被收集，亦不自动提供独立第三方non-repudiation。强公共验证/zkVM仍是后续方向，不能补成全部动作已有proof-carrying-code式形式保证。

## 有限评价与关键反侧

§10/T7是24个可执行seed template跨四runtime family重放形成96 trace，不是96独立任务/真实用户或未知攻击。四route bucket allow24/simulate20/approval28/block24；六boundary类仅列类别，没有披露逐类分母，不补均分16。公开原文保聚合指标，却不公开raw scenario、exact thresholds、scalar weights、connector rules，外部无法完整复验route labels及比较公平性。A只列实现表面，B重申protected corpus；不能据其“executable”声称本作者已运行或代码可信。

T8 PCAA四项均1；static exact.583/macroF1.493/severe recall1/block precision.400，scalar .375/.296/.778/.182。有限既定标签全中不等未来无漏放/真实组织risk calibration。T9 review.292=28/96、simulate.208=20/96、block.250=24/96；manifest/replay均1而receipt completeness.516，正好显示可回放与深层执行证据不等。review率是路由频率，不是实际人工耗时预算或人审判断质量。mean.35ms/P95.54/P99.72没有完整硬件、重复测量、network/human/full lifecycle协议，不能当真实端到端SLO/零开销。

T10无externality exact.875/review.167；无enforceability exact.917/review.375；无integrity exact仍1但manifest0/proof closure.708。它们支持既定corpus内routing、review、proof分责的敏感性，不能把去掉integrity后定义上的manifest0当作实测所有tampering被阻止，也不能得出跨runtime均已在effect前enforce。§9.8/11.3承认runtime深度不同、公开验证有限、product refs会演进；本次仅采版本固定的架构接口/局部结果，不外推全部未来runtime修订。

## 评分 / actual owner与现文差额

正式作者评分Design Delta2＋System Reach2＋Durability2＝6，待首次非writer必要/owner/PRE。具体增量是用同一action certificate连接route/review/outcome并显式保留adapter的effect前控制深度，使receipt齐全、治理状态可重算与真实拦截分开验；跨control/execution/evidence与runtime churn有长期价值。不是因“certificate”命名、成熟签名/日志概念、1.000分或能映owner评分。

本次重读AGENTS/当前适用研究及Report合同/Prompt、ROADMAP/三Books公共上下文、来源使用/Daily/arxiv/恢复与仅2026路由/本日停点。actual owner为`AGENT-PLATFORM` Ch84（不是把所有governance塞Ch81）；实际读Ch84:29–49、108–168 identity/typed session、512–557三个平面/typed primitive/effect边界、774–859 policy/evaluation/replay/审计/envelope整组，以及邻Ch83:110–137连接执行者/adapter分工、379–410入场与owner边界；Ch81:80–110 activation、844–912 retry/effect/HITL及968–998验收组也实际读回作分责核对。

Ch81已有exact action approval失效、候选不能自授权及observation≠effect；Ch84已有same-run identity、独立primitive gate/immutable receipt、backend policy语义差异、replay不重做副作用、hashchain与out-of-band envelope。均保留，不另写五检查点手册/通用审批或签名。所见具体差额是：跨异构runtime的同一portable审计对象仍需显式绑定其实际pre-effect enforceability与expected receipt人口，证书收口不能抹平observer/委托/前置gate的能力差。Ch83只拥有connection/adaptation，不接管平台跨runtime的authority与evidence projection；Ch69拥有通用telemetry/日志完整性，不在此重复其签名协议。

最小两段拟置Ch84 `## Observability 与 Replay`内，原Replay完整段之后、Flat event log完整机制引入段之前；不动现有primitive gate/policy/chain/envelope、他注或原marker。完整直接上锚：

> Replay 不意味着重新执行副作用。平台应提供 evidence replay/simulation，并对外部 action 使用 recorded result 或 sandbox。Prompt/content telemetry 默认最小化，敏感 capture 需 opt-in 与 retention。

完整直接下锚（保原换行）：

```text
Flat event log 足以保存事实，却不一定能快速回答“哪个 decision 首次把 run 带入失败”。平台可以在原始 trace
之上构建 derived state tree：把 plan、tool call、observation、artifact version 与 verifier result 连接为带
partial order 的诊断视图，再定位 failure onset 和传播路径：
```

## 待首次独核的逐字PRE（未授写，非SAVE）

跨运行时保留审计依据时，单个vendor的session视图可以继续服务局部排障；需要跨adapter追溯同一动作，才值得把action/tenant身份、policy与assumption、approval lineage、runtime receipts及outcome收口为可携带的证书。[PCAA的受限架构](https://arxiv.org/html/2606.04104v1#S6)要求这条证据链同时保留实际执行边界：能在副作用前暂停的gate、仅事后导入的observer、由另一governor执法的delegated control，以及无hard前审门的runtime-controlled执行，不应被归一schema抹成相同权限。证书层保留治理依据，实际executor/governor仍拥有effect与阻断责任；同一verb还要核目标可见性、账户和tenant来源，不能凭一张approval记录把事后观察升级成执行前控制。

回放这类证书可重算envelope、policy/risk与manifest，区分缺证据、内容不匹配和规则漂移；它不应重做副作用，也不把pending/partial/non-execution标签当作真实effect已被证明的结论。Receipt完整率依赖声明的expected stages，manifest只约束所载内容，二者都不证明未知出口已被覆盖。原文24个seed跨四family形成的96条protected trace只支持有限路由/收口比较，不能替代第三方复验、真实人工费用或跨runtime安全保证。版本化envelope、receipt投影、存储和独立边界核验都有成本；adapter无法提供所需前置控制或effect证据时，应收窄到已验只读路径、交可信executor/人工处理或保留unknown，而不是用证书齐全允许高风险动作。<!-- source-family:SF-2026-ARXIV-2606-04104 -->

## 当前bounded停点

实际`python3 scripts/validate_research.py --report papers/2026/06/05/README.md`退出1，唯一错误为PCAA Books决定无效：普通待判断没有validator pending枚举。该项不是必要证据受阻/中心争议，不能冒“暂缓”以通过，保进行中/PRE未通过/未I；真实独核与后续处置后再自然消除。README及本日限定diff --check无诊断；新untracked Source的no-index空白核亦无诊断（退出1仅表示与/dev/null有新增差额）。机械检查不替代语义验收。

04104首次必要/6分/actual Ch84具体差额与原两段PRE ready，待首次非writer必要/owner/PRE；无Book授权/SAVE/本人注/POST/I，不预完成。OCL R71–72真实NC已行政采用，累计仍新增I15＋旧Kimi1＝16。其余三04896/04364/04485必要层、有限官方相关标题stop及最终DAY仍ordinary；机构保原有界止点/具名重开条件，不扩73/706配额。该单篇ready即交root结束作者准备阶段释放槽，不等其他日期/整批、不因等待扩附件；非暂停或完成本日。State/index/他日不改，未stage/commit/push。

## R73采用 / 新窄授后真实SAVE与selfread

启动重新加载本日AGENTS/当前适用合同/Prompt、ROADMAP/三Books公共上下文、来源使用/Daily/arxiv/恢复与仅2026路由/本日停点；实际完整读回R73–74，不重复GET/第三必要Source/PRE。root已fresh当前Ch84/邻Ch83并明确仅授此原两段＋本人true-H2注，作者现位再次读Policy/Evaluation/Observability完整组、Replay上段、Flat三行＋code＋解释/原chain/envelope与邻Ch83执行者/adapter交接。两原锚唯一，原本无本family正文/note。

真实SAVE两段与经R73批准逐字PRE完全一致，位置Ch84:830/832；本人一注在真正`## Review notes`下，当前1218。完整新增两段、完整直接Replay上段/Flat三行＋code＋derived解释下组、原chain/envelope及本人整注均已实际自读；先前检查脚本的note删除空白表达式有一次AssertionError，修正只读比较表达式后核实：移除仅本两段/本人注后整章与写前快照字节完全一致，无正文修句/额外写入。写前快照`/private/tmp/pcaa-0605-save.WqtXN6/ch84-before.md`；before SHA256 `9e6e4ccc9a0d9cc1580f2d53833388f46b255f12ac96be88bf962d17465b79b1`，after `30679c52d57d016051f6270fbb8c3c5191565b3609b8a1c8388308c6d9cc90a9`。共同schema非共同前控、receipt分母/manifest非全effect证据、有限protected人口/费用/unknown等反侧近文不变，原marker/两侧/他注/其他并发修改保护。

README同步R73通过/新窄授后已保存及自读，仅待唯一非writer actualPOST，不预I/DAY；既成仍新增I15＋旧Kimi1合16。当前V3普通待POST枚举仍如实失败，不冒暂缓或改脚本；限定检查另记本日恢复。该写入ready阶段即交root结束释放作者槽，不因等待扩下一Methods；余三/有限title stop/DAY普通保持，未改State/index/他日，无stage/commit/push。
