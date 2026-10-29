# 04306 OCL：首次必要Source / actual Ch81具体NC提案

当前行政采用：reader R71–72已实际完整读回，首次必要/6分/actual Ch81四组具体已有覆盖通过，正式NC生效。以下“提案/待首次独核”为提交前过程原记录，不是当前待办；无Book/本人注/另建PRE-POST，不增I。README已采用既成NC并复跑V3通过，累计仍新增I15＋旧Kimi1合16；下一04104首次必要层，余四与有限title stop/DAY普通。

作者supp_20260605_author；仅Daily2026-06-05补Jun04。`SF-2026-ARXIV-2606-04306`，[Organizational Control Layer: Governance Infrastructure at the Execution Boundary of LLM Agent Systems exact-v1](https://arxiv.org/html/2606.04306v1)。R33–36完整题摘/准入/精确v1联合日证复用；R33后版限制有效，不能使用发现摘要的structured-recovery消融等后版命题覆盖v1。官方HTML GET200/200301bytes，`SUP_2606.04306v1_20261025.html`；SHA256 `e1c32c2f9cfb2862bbe4105dd4f2deb775875a983747e87b111a1f93cf52089e`。

本次实际读v1 §3.1–3.2、§4.1–4.3、§5.1–5.2/T1–2、§6、B persona生成与C/T4–5必要支持/直接反侧；A样本对话只确认定性来源，不据其证明真实运行效果。不打开完整仓库/全部历史/其他Methods、不复现；所采有限定义与作者模拟结果不依赖可选实现，支持与反侧足即停。

## 必要机制与有限支持

§3.1把经济task分state、各agent action、constraints、utility与environment transition；constraints明确分control可见Cobs及隐藏Chid。模型产生raw proposal，gΠ消费当前history/state、raw及Cobs，输出Approve/Revise/Block/Escalate、dexecutable及audit；仅dexecutable进环境。Approve原样，Revise改提案，Block无environment-facing动作，Escalate延迟直到可信模块/人或更高权限流程处理。这个抽象分工不证明实际原子性/不可旁路、审计持久性或隐藏约束满足。

§3.2 roles规定谁可提/改/授，gate对可见约束检查，escalate可澄清、换authority、转人工/可信模块或安全终止，audit存raw/check/decision/revision/execution。§4.2实际执行更窄：模型经adapter读取可见state/constraints并产JSON；baseline直接执行，OCL拦JSON，违hard constraint时block/audit/escalate，**其实现escalation是确定性replan/clamp**（85报价改到sellerfloor90）。这不是实测人审完成、通用异常恢复、独立权限重新签发或结构化恢复消融已证；改一个price也不证明其他可见/隐藏约束继续成立。代码未核，不发布完整可执行guard规格。

§4.1/B从真实谈判风格启发50个合成buyer persona，五类lowball/phishing/rolehijack/vague/timewaster；Gemini2.5Flash零样本生成、temperature.8。真实对话基础不等真实用户随机试验，LLM合成profile差异不证明全部攻击/业务覆盖。

§4.3 success是agreement；valid success还要求无结构/安全违例。Unsafe是episode至少一次已执行越界/恶意动作，不等逐proposal违例率；intercept episode率、threat raw count、deterministic rewrite次数不是同分母。Reward=max(0,Pdeal−Pmin)−.1Nrounds，依卖方profit/turn penalty而非纯合规价值或真实商业效用；条款外库存/退款/支付effect没有被本模拟分数完全验证。

T1以50 adversarial episode报告baseline success94%/valid12%/unsafe88%，OCL96%/96%/0%；205执行violation、52threat与48escalation不能当205个独立session/52种新攻击/48次人工批准。0/50是该合成人口的观察，不是零风险定理/所有backend均零unsafe。7.36→13.58 audit event只是日志数量，不证明全部决策可追溯、不可篡改或error-free。38.75→18.51s与5.36→2.58round共同变化，是完整episode均值，不是拦截器零开销或局部执行费用。

T2 caption称paired deterministic seed/每profile一seed且reported slice71–91，但T1称50episode，完整映射/每backend人口、model exact revision/采样/运行重复CI未披露，不自补50全配对或独立复现实验。Gemini success98→96、Qwen100→96，Qwen latency65.52→69.43反而更慢，不能采用“所有模型效能不损/都更快”。GPT reward26.95→18.39与Gemini22.71→18.24下降，作者称经济校准，但没有独立counterfactual隔离这些差额全部来自非法收益，保安全—效用取舍而非净效用普胜。

## C市场反侧与采用上限

C五情景T4规定buyermax/sellermin/anchor/maxround；T5每情景50episode，Strict Success明确同时满足双方hidden reservation price，与主表valid/observed structural constraints不是同一量。S2 strict .56→.74、CAW5.48→6.94，S5 .44→.54/4.18→5.29；S3 .92→.88/9.97→9.18，S4 .80→.68/5.79→5.09直接反证strict governor普遍改善业务成功/福利。S2 rounds4.86→4.96亦增加。公开必要域没有足够constraint-visibility/逐样本轨迹，不能把主表96% valid合并成所有hidden约束96%满足。

S5 maxround4与mean rounds4.88/4.74并列，可能存在round/turn或边界计数差，但原文未闭合单位，不自行改数字或补一套停止实现。C的CAW精确计算定义、重复/CI、完整实际运行硬件/并发/尾SLO与全生命周期成本不全，Not Disclosed，不外推生产。作者归因“过严guard阻止thinmargin探索”是机制解释，表格不隔离gate/clamp/escalation各唯一因果；§1称有ablation，但v1必要域没有prompt-only/block-only/recovery-only完整对照，不借后版表补这个证据。

因此仅采可见约束下的proposal/decision/effect分工、具体确定性rewrite实例与partial-information/业务效用反侧；不采通用structured recovery增量、零unsafe保证、未知攻击/真实支付授权、audit完整/安全持久或自动满足hidden constraints。也不因未核代码缩成访问外阻；此处不需要代码才能记录这个有限接口和负面结果，未核实现/复现另明。

## 评分与actual owner具体已有覆盖提案

作者建议2+2+2=6：role/policy/economic可见约束前置到raw→environment边界，确定性修订与多市场反侧支持重新分开agreement/合规/hidden可行性/效用，跨proposal/executor/评价边界有稳定价值。成熟authorization/日志/approval概念本身不加分，不以0%宣传或能映owner计分；准入与评分有效不等I，待首次非writer必要/owner/NC。

已重读AGENTS/合同/Prompt、ROADMAP/三Books公共上下文、来源使用/Daily/arxiv/恢复及仅2026路由。actual owner `AGENT-WORKFLOW` Ch81；实际读核心14与16–35、80–110 transition/硬软block/激活、844–907 retry/effect/HITL及972–991验收，邻80/82真实开头。对受限所采命题，提出以下具体已有覆盖，不因“都叫governance”直接NC：

1. Ch81:90–110完整组已有模型next_state仅建议、engine验transition，untrusted候选offcommit、当前owner/prestate authority/freshness/effect identity重验，Commit/Reject/Quarantine/Defer后只有Commit推进权威状态。明确不能candidate自授权、必需证据不可得不得装成功；已具体承载OCL raw→gΠ→dexecutable及Cobs不足时需defer的责任链。OCL schema本身未给另一条更强可执行保证须改原链。
2. 881–907 HITL完整组已有exact action/argument digest、planversion、approver/authority、expiration、risk reason，以及动作变更使旧approval失效；ask/takeover/handback与pending effects、control lease和state reconciliation分权。足以承载v1抽象escalation不等实测人审与clamp改proposal不自动取得approval。本文确定性改价只是可见条件修订实例，不是独立授权根或通用恢复consumer。
3. 91完整硬/softBlock组已明确把所有block绝对化可误拒合格动作、局部priority可覆盖soft而hard不允许被模型高分突破，分类/qualification/support不清回退确定规则/串行/人审。已经承载C中strict governor可能压低业务可行性/福利且不因此允许突破hard规则的设计取舍；新市场数值/可见性条件保Report，不需要再写泛“安全有效用代价”。
4. 844–879区分model revision/business rejection/ambiguous external outcome/permanent failure，补偿仍须authorization/audit；tool观察成功与world effect commit分开，未知需failclosed/对账/人审。972起把observed passing trace/归纳contract/authorized workflow分artifact，少量成功不证明完整spec。覆盖模拟agreement、无observed violation与真实支付/退款effect/审计完整性不能合并的边界；OCL有限日志量和0/50不授新的真实effect保证。

这四组有具体机制/适用域和反侧，不以泛标题或旧完成marker代覆盖。所采长期判断已具体承载，新的市场负侧、v1计数/人口差额和有限rewrite实例保Report即可；没有必须为论文名/“4 outcomes”再造最小正文的已证差额。只提NC待首次独核，无Book正文/本人注/PRE/POST/I；若reader指出实际gap，仍只恢复该具体命题，不为NC缩候选/降分或要求通用定理。

## bounded停点

04306首次必要/6分/actual Ch81四组具体NC ready。OSCAR R69–70已实际行政采用，6分/具体NC生效，无新I；既成新增I15＋旧Kimi1合16。其余四04104/04896/04364/04485与有限相关官方标题stop/最终DAY仍ordinary，不扩73/706配额。本单篇ready交root即结束释放作者槽，不等待其余Methods、不表示暂停或完成本日。无共享Books写入/注、State/index/他日/stage/commit/push。
