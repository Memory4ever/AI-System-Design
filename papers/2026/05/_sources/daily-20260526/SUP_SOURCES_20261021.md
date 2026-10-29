# 2026-05-26 Daily 遗漏来源增量补查

## A1 — 本日范围、基线与恢复边界

执行日：2026-10-21；作者：supp_may26_author；独立复核者：supp_may26_reader。只补北京时间 **2026-05-25 完整自然日**。已实际重读 AGENTS.md、当前 Research/Report 合同、RESEARCH_SOURCES 使用说明/每日组/arXiv主题、CODEX_RESEARCH_PROMPT、ROADMAP 与 LEARNING_STATE 最新 2026 补查路由。按 using-agent-skills 的窄范围与验证要求执行；写作沿用本仓当前报告合同，不另建样式或过程账本。

真实运行前基线：README 原 86 候选行；原窗口 `2026-05-25T09:00:00+08:00 ～ 2026-05-26T09:00:00+08:00`；旧 §4 连续正文保留。旧 263 项 arXiv batch 是 05-26 08:00 BJT 事件，不能证明本次 05-25 自然日覆盖。原候选的日期、评分及有效证据复用，不重新搬移、重评。运行前工作区本日本身无新 SUP；全仓其他既有及并发修改不动。冻结原件在 `/private/tmp/daily-20260526-before-supp-20261021.md`。

## A2 — 首批准入校准包

### 拟入选：How we contain Claude across products

官方原文：[Anthropic](https://www.anthropic.com/research/how-we-contain-claude)；官方 Engineering 目录明确 `May 25, 2026`，正文同日；原件 `SUP_containment_20261021.raw.html`。本次已读完整核心说明及全部风险案例，而非仅凭标题映射入选。当前正文未见撤回/勘误标识；不遍历全版本史。

准入链：域名白名单常被当作出站限制 → 官方披露恶意工作区文件携带攻击者 API key，借允许的 Files API 上传至攻击者账户，并以会话令牌 provenance 校验和禁用服务端 fetch 头修复 → 需要把“允许目的域名”重解释为可达操作/账户权限授予，不能用沙箱存在或可信连接器推导无泄漏。该披露改变具体身份与 egress enforcement 判断，不是通用安全原则的再包装。拟评分 `3+2+3=8`；需要深入核验采用边界与 Books owner。作者披露支持该产品事件及修复结构，不证明独立复现或所有出站路径安全。

### 代表性排除

1. [AI is becoming a first hire for small businesses](https://openai.com/index/ai-first-hire-small-business/)：RSS `Mon, 25 May 2026 00:00:00 GMT`，官方正文同日。已读核心全文，是创业用户分布/使用案例/经济价值叙事，没有改变模型/训练/系统机制的证据；贡献前关闭，不评分。RSS 原件 `SUP_openai_rss_20261021.raw.xml`；直接 curl 文章403不等于正文缺失，已通过浏览原始页面读取。
2. [Grupo Folha / UOL partnership](https://openai.com/index/grupo-folha-grupo-uol-partnership/)：同一 RSS 日期，官方正文同日。已读核心全文，商业内容授权与新闻访问合作；未披露检索、索引、训练或引用机制改变，不能只因能联想到 RAG 入选；贡献前关闭，不评分。

来源扫描及后续证据/Books/日级验收继续；当前不是完成声明。

## A3 — Containment 深入证据与写前窄包

精确版本：2026-10-21 实取官方现行文章，页面 Published May 25, 2026，无可见撤回/修订标识；不声称逐字恢复发布当天快照。深入已读 `Three types of risk, three components of defense`、三个 containment patterns、全部 `Risk we missed`、`Trusting what the agent reads`、`Looking ahead` 与 footnote。采用命题定位在 Pattern 3 的 `Risk we missed: Exfiltration through an approved domain`：域名允许不约束目标账户或操作，官方披露的修复检查 VM provisioned session token 并阻断 server-side fetch 头。原文还说明代理在 VM 内，因为服务器单看普通 API 请求不能识别 Cowork 来源。

证据边界：这是厂商事件与架构披露，没有独立攻击重放、完整 threat coverage、端到端泄漏率或代理延迟实验；不把“沙箱工作正常”解释成完整 containment 通过。文章的其他百分比涉及不同协议和人口（审批遥测、auto mode、prompt injection benchmark、内部钓鱼25次），本次不合并、不作为采用论点的性能保证。该论点不依赖指定模型、GPU、precision、batch、token长度或concurrency，均不适用；代理开销、尾延迟和SLO未披露（Not Disclosed）。

已读 PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE；目标 Ch72 的执行环境完整局部链与相邻 Ch71、Ch73 开篇交接。owner 为 `PLATFORM-SECURITY`。既有正文实际覆盖容器第一跳不证明 transitive path、per-run envelope、credential broker，但没有承载“获准服务的跨账户操作”及 token provenance 的具体机制/反证；不是仅凭主题相同作 No Change。

拟窄写位置：`books/part-06-ai-infrastructure/72-security.md` 的 `## 执行环境与可验证的安全边界` 后、`### Training / Evaluation Environment 也是高价值生产面` 前；不修改其他段落。正文逐字 PRE：

> 出站域名白名单在固定服务与可信调用主体下，能限制代码连接的目的地；但当同一获准 API 同时服务多个账户、允许上传或服务端代取时，它授予的是一组操作能力，而不只是一个地址。工作区里的恶意内容可以携带攻击者自己的 API key，让 Agent 把可读文件上传到该域名下的攻击者账户：VM 和域名过滤都正常工作，数据仍越过了预期边界。因此出站检查还要绑定本次会话的凭据来源、目标账户和允许操作，不能从“域名可信”继承数据释放权限。
>
> 一项[公开的 containment 事故说明](https://www.anthropic.com/research/how-we-contain-claude)披露了这一受限反例：修复代理只转发带该 VM 自有会话令牌的请求，并阻断可启用服务端 fetch 的头；代理需要在能辨识会话来源的位置执行，单看服务端普通 API 请求并不足够。这增加了令牌配置、代理策略与兼容性维护成本，原文未量化延迟，也没有证明所有出站旁路已闭合。来源、账户或操作无法核实时，应拒绝该释放并保留较窄的网络/文件权限或人工授权，而不是让另一层模型判断代替边界。<!-- source-family:SF-2026-ANTHROPIC-CONTAINMENT-0525 -->

拟末注：`2026-05-26 supplement：Anthropic “How we contain Claude across products”（官方页面 2026-05-25，现行原件 2026-10-21）；采用 approved-domain 跨账户外传与 session-token provenance 修复的受限披露，非独立复现、通用泄漏率或全路径安全证明。`

等待独立 Source/PRE 与 root 窄写协调，不把 prepared 记为整合完成。

## A4 — 单篇已生效与 arXiv 资格差额首批

Containment 的 reader 独立 Source/PRE 已通过，root 精确授权后已实际保存 Ch72 两段与自身末注；reader 已实际 POST 通过并释放，本项整合完成。不能据此提前宣称整份 Daily 完成。

本日重新请求 arXiv API range 时，响应把范围改写为 literal（右界又从 `202605242359` 变为 `2605242359`），返回 10 月条目；另一日期探测500，均不计本窗扫描。现用 DataCite `client-id=arxiv.content`、registered UTC `2026-05-24T16:00:00Z TO 2026-05-25T15:59:59Z` 两页1000+81共1081作有界发现原件，不把登记日单独当首次公开，也不逐项关闭全部宽库存。先按模型、训练、推理、Agent、多模态系统主线标题语义缩窄；对与邻日原225候选精确ID重合的事件只定点核有效层去重，不继承邻日池。对当前全文/日期事实有真实差额的局部恢复。

原件：`SUP_dc_may25_20261021.raw.json` / `SUP_dc_may25_tail_20261021.raw.json`。arXiv schedule 已实际核验：EDT Thursday14:00–Friday14:00 submission 最早 Sunday20:00，即本窗 May25 08:00 BJT；Friday14:00后最早May26，不能混入。每项仍核唯一v1、精确DOI、client、findable与registered，联合区间全落本日才准入；更早v1的跨日区间另留资格缺口。

首批实际已读精确 v1 完整题摘原件 `SUP_abs_<ID>v1_20261021.raw.html`：

| ID / 原v1标题 | 题摘中的具体潜力与拟审阅 | 日期处置 |
| --- | --- | --- |
| 22949 MARGIN | 异构 responder 自报信心不可比/漂移 → 按agent与confidence-band在线EWMA＋shrinkage → 重考固定离线校准；2+2+2=6，标准；后续版本已改变对照和主张，需保v1身份边界 | v1 May21 18:25:05Z，最早May25 08BJT，registered May25 01:42:33Z，同日联合界；技术原件身份核验继续 |
| 23057 ModeSwitch-LLM（现题RequestRouter） | 静态推理模式 → 请求边界cheap-feature选择固定模式，并报告learned router未胜规则的反侧 → 重考按请求动态配置；2+2+2=6，标准 | v1 May21 21:46:57Z，registered May25 01:45:02Z，同日联合界；本日只采用ModeSwitch v1，不倒灌August扩展实验证据 |
| 23348 XWind | 变动电力容量 → 同时用latency/KV/queue反应式路由站点 → 重考仅power-cap/idling处理风电变化；2+2+2=6，标准 | v1 May22 08:08:47Z，同日联合界，核原始注册字段 |
| 22967 Learned Relay Representations | diffusion每轮丢弃latent计算 → 可微per-token relay＋truncated BPTT → 重考跨轮状态复用和训练成本；2+2+3=7，深入 | v1 May21 18:53:22Z，同日联合界，核原始注册字段 |
| 23080 The Attribution Contract | 把classifier attribution搬到生成 → 显式feature/output/固定量/生成过程合同 → 重考归因结论的对象；2+2+2=6，标准 | v1 May21 22:27:04Z，同日联合界；不倒灌后续MoE实验 |
| 23146 Infra-Bayesian RL | policy-independent realizability失效 → 有限stateless imprecise hypothesis maximin → 重考Bayes平均风险；2+1+2=5，标准，局部理论/PoC不外推LLM | v1 May22 01:51:41Z，同日联合界 |
| 23268 Coupled Training | noisy privileged teacher可误导student → joint/alternating learning与成立条件 → 重考two-stage distillation；2+1+2=5，标准；不因通用学习理论排除 | v1 May22 06:15:35Z，同日联合界 |
| 22894 SCRIPT | action/state/text联合流与hybrid-reward后训练、历史稀疏机制有潜力 | v1 May21 14:17:21Z，最早界在窗前，registered不足缩成May25；不先评分/采用 |
| 22882 GEM-4D | 视频4D correspondence监督与inverse dynamics转换有潜力 | v1 May20 21:36:44Z，最早界在窗前；不先评分/采用 |

未把当前 DataCite 题摘当精确v1题摘：已识别 MARGIN、ModeSwitch、Attribution 等版本差异；后续正文只读拟采用精确事件的必要证据，不全版本比对。上述候选准备好即逐项推进，不因其余来源未结束等待。

## A5 — 首批已核证据及第二批准入

MARGIN 的 HTML masthead 为 August24，与公开首版日期冲突；reader 已实际核官方 exact-v1 PDF 首页 May25、边栏v1/May21，必要机制一致，改以PDF为权威，不作无限版本比较。`https://arxiv.org/pdf/2605.22949v1` §3/Eq3–8/Alg1、§5–7/T4–7、§10.3–11 支持每agent/per-band在线EWMA与shrinkage，但固定策略/non-strategic、可验证binary outcome和反馈可得性是前提；在线方法对离线静态校准的优势不证明胜过所有同信息在线baseline。reader 已实际独核必要Source与 Ch56 `Calibration 是在线 Routing State` 完整局部链：per-model/per-band、delay/selection/forgetting及反馈偏差/冷启动/fallback 已承载本次收窄命题，Books **已有覆盖** `INFER-SCHEDULING`，无写入。

第二批已实际读精确v1完整题摘与版本史（原件同A4命名，非当前版本倒灌）：

| ID | 具体准入链与拟评分 | 事件资格 |
| --- | --- | --- |
| 23590 Co-ReAct | report-level rubric仅事后评价 → step-level rubric引导Reason-or-Act、以rank-correlation训练生成器 → 重考谁提出下一步搜索/判断依据；2+2+2=6，标准 | v1 May22 12:59:16Z，核registered可联合本日 |
| 23128 π0-EqM | fixed flow horizon → 替换EqM decoder及matched-budget residual/成功率非单调反侧 → 重考stationarity是否能作可执行停止证书；3+2+2=7，深入 | v1 May22 01:07:07Z，核registered可联合本日 |
| 23243 Dual-mode vulnerability benchmark | 检出函数级弱点不等端到端web覆盖 → matched目标中的FP/coverage与tooling/methodology差额 → 重考能力评价与可部署覆盖；2+2+2=6，标准，不先采methodology唯一因果 | v1 May22 05:24:43Z，核registered可联合本日 |
| 23071 Efficiency Frontier | 独立比较token/quality → preload amortization与重用次数改变strategy优劣 → 重考RAG/压缩成本临界点；2+2+2=6，标准 | v1 May21 22:03:25Z，核registered可联合本日 |
| 23764 HyperParallel-MoE | serialized kernel → AIC/AIV tile taskflow、one-sided communication与event依赖 → 重考异构MoE的overlap/synchronization单位；2+3+3=8，深入 | v1 May22 15:35:23Z，核registered可联合本日 |
| 23500 B-GRTO | differentiable tool单独训练 → 重用GRPO rollout联合policy reward和tool gradient → 重考工具/策略梯度分责；2+2+2=6，标准，不因segmentation指标把它当纯应用 | v1 May22 11:04:12Z，核registered可联合本日 |
| 23657 OpenSkillEval | 可用/流行skill被当效用代理 → 受控模型×harness×skill下负面证据 → 重考skill准入评价单位；2+2+2=6，标准 | v1 May22 14:09:41Z，核registered可联合本日 |
| 23345 SCOPE | global action conditioning影响所有像素 → per-pixel temporal action response → 重考局部动作与背景持久性分责；2+2+2=6，标准 | v1 May22 08:06:37Z，核registered可联合本日 |
| 23904 SkillOpt | 无约束skill自改 → bounded edit/rejection memory/heldout strict improvement → 重考external instruction artifact的优化/验收状态；2+2+2=6，标准 | v1 May22 17:59:50Z，仍早于Friday14EDT cutoff，核registered可联合本日 |
| 23454 ARES | 固定task rubric与人工问答 → document-grounded self-contained QA＋instance weighted rubric＋独立过滤 → 重考开放任务监督构造；2+1+2=5，标准 | v1 May22 10:09:28Z，核registered可联合本日 |
| 23163 Fast-dDrive | 全序列diffusion可见未来语义段 → 段内双向/段间因果＋结构scaffold → 重考可缓存VLA生成的因果边界；2+2+3=7，深入，吞吐不是控制安全证明 | v1 May22 02:31:32Z，核registered可联合本日 |
| 23025 World Machine | 完整context二次代价 → 可复用latent state条件化time-series生成 → 重考固定state与上下文取舍；2+1+2=5，标准，Toy1D不外推物理世界模型 | v1 May21 20:48:51Z，核registered可联合本日 |
| 22864 Reading Calibrated Uncertainty | MLP跨层轨迹几何的sparse probe有潜力 | v1 May19 19:24:29Z，联合区间跨日，不先评分/采用 |
| 22873 When Do LLMs Reason / EDRM | early entropy轨迹用于选择CoT有潜力 | v1 May20 03:15:46Z，联合区间跨日，不先评分/采用 |

以上初步池19项arXiv＋Containment；仍需读已缩窄的非关键词相关标题/题摘查漏，不能把它写成冻结数。所有ready条目的必要Source与Books判断继续。

## A6 — 四项必要原证与逐字 Books PRE

四项 necessary Source 已由 reader 实际独核；作者也已读相应核心方法、条件/对照与直接限制。本节只申请精确窄位，不修改旧段。已加载学习/写作/项目上下文；Ch24的Masked及相邻生成状态、Ch23/25交接，Ch29监督链，Ch66归因局部与Ch65/67交接，Ch79决策合同及Ch78/80交接须实际读完后写。各自 Review notes 仅加本人一条来源/采用界限。

### Relay — MULTIMODAL-GENERATIVE-PARADIGMS

原证：`SUP_core_22967v1_20261021.raw.html` §3/Eq2–8/Alg1、§4/T1–2、§6、A2/B。teacher-force token值，离散position选择不求导；sg与on-policy对照区分relay载体与跨轮credit。Fast-dLLM-v2 1.5B/两A10080GB/bf16/ZeRO3/gradient checkpoint、200 optimizer steps/effective batch32，码任务block32/subblock8/threshold.85，NFE排prefill及最终cache-update；32%只是88.3 vs130.7 NFE，不认全请求wallclock。microstep profile有no-op optimizer、eager/FA2off，不作完整训练峰值免费保证。

窄位：Ch24 `Masked generation` 首个schedule段后，原“即使提交schedule不变”之前；现有recurrence与equilibrium讨论并未解释去噪轮间可训练hidden relay/cache资格。逐字正文：

> 提交哪些 token 与保留哪些计算状态也是两件事。只保留已揭示序列时，每次去噪都会丢弃尚未变成 token 的中间计算；另一条分支把上一轮末层 hidden 经可训练投影，加到本轮 token embedding，再让有限展开窗口的梯度训练这条连续 relay。训练仍可强制填入 gold token，而只用模型分布选择揭示位置；离散位置选择不求导，因此不能把短窗反传解释成整条采样策略的精确梯度。
>
> [受限 Relay 对照](https://arxiv.org/html/2605.22967v1#S3)区分了 on-policy 位置轨迹、仅传状态与跨轮反传。与 KV 复用组合时，只更新 active block 中仍被 mask 的 relay，已提交位置及旧块保持冻结，不能让任意 hidden 改写继承旧 cache 的有效性。连续状态读写、额外训练 forward/activation 都有成本；其代码实验的少 NFE 还排除了 prefill 和最终 cache 更新，不等于全请求同幅加速。质量、cache 一致性或总预算不合格时，保留原无 relay 去噪、小块与已验收训练目标，不由短窗收益推出无限长轨迹稳定。<!-- source-family:SF-2026-ARXIV-2605-22967 -->

### Attribution Contract — PLATFORM-EVALUATION-SYSTEM

原证：`SUP_core_23080v1_20261021.raw.html` §2–5/Def1/T1/Eq5–41；这是method-contract specification，不是后续MoE实验或因果faithfulness验证。Ch66现有归因局部确实已要求解释对象/受众/evidence/evaluator及mask预算，但未区分generated prefix的条件角色与eligible feature角色。

窄位：Ch66“单一 attribution score 在解释对象、受众和风险固定时便于比较”完整段后、“软遮挡比较还必须控制干预预算”前。逐字正文：

> 对生成模型，这份合同还要列明目标 score、被固定的条件、目标 token/span、生成路径与可获归因的 features。同一个 generated prefix 可以继续参与前向条件化，却不属于允许分配 attribution 的输入集合；把“哪些 prompt 特征在固定 prefix 下影响此 token”与“完整 context 哪些部分预测下个 token”混读，会把自产前缀的贡献误称为原 prompt 的解释。AR 的固定原生成 re-score 又不同于扰动后重新生成；diffusion 的 state、stage 与最终输出也不能共用一个未声明的干预对象。[Attribution Contract 首版](https://arxiv.org/html/2605.23080v1#S3)支持这份对象区分，不认证某张热图具有因果真值。保存条件/路径与重复求值增加成本；无法复建相同合同则保留局部归因或 Unknown，不在不同合同间直接排名。<!-- source-family:SF-2026-ARXIV-2605-23080 -->

### Coupled Training — TRAIN-SFT

原证：`SUP_core_23268v1_20261021.raw.html` §1.1/Eq1–3、§2条件、§3、§4–5/Limitations。共享目标联合或交替求解不等同时优化；paired unlabeled rich/deployment view、square-loss/convex证明条件和λ/ν方向不能偷换。26seed Bank与单seed Parkinson分开；通用方法和合成控制为采用依据，不把医学应用纳入AIScience。

窄位：Ch29 `### 多 Teacher Debate 把 Supervision 变成版本化的集体状态` 标题之前，承接现有单teacher偏差/监督构造，插两段。逐字正文：

> 教师多看一份训练期特权信息，也不保证其固定伪标签更适合学生：额外特征弱或含高维噪声时，先拟合 rich-view teacher、再让学生追随，会把 nuisance 一并传下去。一个受限替代让 deployment predictor 与 rich-view predictor 在同一目标下耦合：学生读取有标签真值及无标签伪响应，教师再向当前学生的无标签预测校准，但必须受有标签误差约束。联合表达的是相互约束的目标，也可以交替求解，并不是必须一次同时更新全部参数。
>
> [Coupled Training 的必要条件](https://arxiv.org/html/2605.23268v1#S1.SS1)要求无标签样本仍有配对的两种 view；平方损失与凸函数类下的分析不自动覆盖非凸 LLM 蒸馏、域移或缺失特权特征。约束过紧仍会转回强制追随 noisy teacher；放松到允许同一 predictor 时才有回退有标签监督的路径。两模型拟合、校准参数选择与独立验证增加费用，不能由更多无标签数据或训练目标下降保证真实风险改进。配对、质量或成本条件不足时，保留已核教师、普通有标签训练或降低伪标签权重。<!-- source-family:SF-2026-ARXIV-2605-23268 -->

### Infra-Bayesian PoC — AGENT-PLANNING

原证：`SUP_core_23146v1_20261021.raw.html` §4–6。有限stateless/extremal a-measures；known rewardmatrix/predictor场景无学习，例中Bayes uniform也同选arm2，regret仍linear，不采“全面胜classicalRL”。

窄位：Ch79 `先校准不确定性，再决定行动、询问或探索` 中“合成环境中拟合的 prior 不能直接当作生产概率”完整段后、COIL段前，插一段。逐字正文：

> 还有一种不同于“概率尚未校准”的情况：已知的是一组可行环境约束，却没有依据给它们分配精确 prior。此时可以保留不精确的假设集合，先对每个候选 policy 求集合内最坏期望，再选其中较优者；若集合只有一个带权假设，它退回普通 Bayes 期望，而不是废弃概率规划。[有限 infra-Bayesian 实现](https://arxiv.org/html/2605.23146v1#S4)用极小仿射测度的端点表示做这种选择，但只验证小型 stateless 问题，部分例子已知全部奖励/预测器且不发生学习，普通合适 prior 也可给出同一动作。较大假设集合带来表示、逐 policy 搜索及保守性成本，报告的 regret 仍线性；未知集合边界或多步问题不能继承保证，应保留已校准 prior、硬安全约束、短视规则或人工选择，不把 maximin 名称当作开放环境鲁棒证书。<!-- source-family:SF-2026-ARXIV-2605-23146 -->

PRE尚待reader逐字检查/root窄位授权，均未写。

## A7 — A6 已生效与非关键词有界查漏

A6 四项经 reader 逐字 PRE / root 精确窄位授权，作者实际保存后，reader 逐项实际 POST 通过，全部窄位释放。Ch66 使用 `semantic-delta:20260526-supp-attribution-contract`，复用原已有 source-family、不重复标记。目前5实际整合（含Containment）与MARGIN具体已有覆盖；其余普通工作仍继续。

本次有界补检未把关键词当准入器：在本日 registered 切片的相关分类标题中，另读非关键词/新命名机制的完整题摘，并逐项恢复必要 exact-v1。不是全1081逐条关闭。下面9项已实读精确v1完整题摘（`SUP_abs_<ID>v1_20261021.raw.html`），拟准入：

| ID | 原始增量→需重考的具体判断 | 拟评分 / 日期 |
| --- | --- | --- |
| 23395 Convex Compositional Reasoning Models | 非凸factor energy难组合求解→ICNN各factor＋convex relaxation＋unrolled solver训练→重考组合规模外推依赖什么几何条件 | 2+2+3=7，深入；v1 May22 09:04:14Z |
| 23055 Decomposing and Measuring Evaluation Awareness | 把识别评测与改行为混为一谈→环境信号/recognition/propensity分拆及factor-toggle成对任务→重考benchmark有效性测量单位 | 2+2+2=6，标准；v1 May21 21:38:34Z |
| 23393 Every Component Is a Lookup / Unpack | attention/MLP分开解释→固定forward selection的统一KV credit递归→重考路径贡献与干预因果是否同一对象 | 2+2+2=6，标准；v1 May22 09:03:01Z；不倒灌后版更广因果对照 |
| 23096 Encrypted Neural Networks without Overflows | heuristic采样激活区间→合法输入越界反例＋formal neuron bound→重考CKKS polynomial替换的正确性资格 | 3+2+3=8，深入；v1 May21 23:08:23Z；当前题摘的executable artifact不能倒灌v1 |
| 23262 Designing Benchmarks for Knowledge Work | task分数外推工作能力→activity/setting/work-product三步及3benchmark case→重考scored answer与可用交付物差距 | 1+2+2=5，标准；v1 May22 06:03:01Z；不是后版four-field实证 |
| 23668 OnePred | 每轮读全history或末轮截断→独立recursive intent memory与两阶段RL→重考prediction-state压缩的训练/上下文责任 | 2+2+2=6，标准；v1 May22 14:16:21Z |
| 23826 ToolMerge | 单query或固定schema选帧→query分解tool rankings＋Boolean merge→重考retrieval evidence选择与答案评价分责 | 2+1+2=5，标准；v1 May22 16:29:51Z |
| 23701 Metadata Predictability Is Not Evidence Dependence | metadata-only能预测被当evidence依赖→跨item evidence intervention＋reader-strength校准反例→重考benchmark shortcut审计 | 3+2+2=7，深入；v1 May22 14:52:32Z |
| 23595 MetaEvaluator | 无标签新模型评测靠再训练/标注→reference-model meta-initialization amortize evaluation→重考评估器跨模型/数据泛化资格 | 2+2+2=6，标准；v1 May22 13:05:34Z |

9项精确DOI与唯一v1已核，registered原字段见两页DataCite；仅在client=arxiv.content/findable/本日registered与v1 earliest全部同日时纳入。仍须实际核完整必要原证及Books，作者prepared不等独核完成。

22863 Latent Cache Flow 已实际读v1完整题摘、登记与版本：v1 May19 19:21:01Z，最早界窗前而registeredMay25，仍为跨日资格潜力；不评分、不同步倒灌更后版“pruned”或不同F1/EM口径。

23278 When Is Next-Token Prediction Useful 与 23066 Orbax 的完整v1题摘已读；前者需有限core明确是否新增可采用条件而非教科书重述，后者仅摘要的库名/加速数不足准入，正补读必要机制后决定。它们不是已确立候选，不因审阅成本排除。

## A8 — ModeSwitch 与 XWind 具体差额 / 逐字 PRE

两项 reader 的必要 Source 已通过：23057只采用v1 ModeSwitch-LLM，不倒灌后版RequestRouter实证；23348只采用作者emulated-site控制边界，保15分钟oracular power/插值及忽略WAN。作者已读相应方法、评价条件/直接反侧，目标Ch56目标函数与相邻55/57、Ch63Power Budget与相邻62/64；不把标题映射代替实际差额。当前正文分别未承载request-level固定mode与oracular-power条件下的site-local telemetry/controller接口。

### ModeSwitch — INFER-SCHEDULING

窄位：Ch56 `## SLO-aware Admission` 之前，承接“目标函数不止吞吐”的完整段落，插两段及本人末注。

> 不改模型也可以先在请求边界选择一份已测执行模式，而不是让所有请求共用同一配置：prompt/预期输出长度、prefix 复用、memory/batch 压力提出量化、speculation、cache 或 batching 的固定组合，整个请求随后保持该模式。这里“phase-aware”只是特征描述，不是 Prefill/Decode 中途切换；更细粒度控制还需要另验 KV 与执行状态兼容。已知 benchmark 标签可以帮助原实验分类，却不应默认为未知线上流量可得的信息。
>
> [ModeSwitch 首版的有限对照](https://arxiv.org/html/2605.23057v1#S4)说明模式选择应验最终 latency/energy/quality，而不是仅最大化匹配 oracle 标签的准确率；较高分类命中可被 router 开销或越过质量约束抵消。但单A10040GB/Llama3.1-8B 的均值收益不认证生产尾部，部分量化在长输入与memory-pressure的质量代理明显退步，CPU决策时间也不等完整模式装载/切换费。应独立验证真实质量、配置驻留与全部请求成本；特征或质量证据不足时，保留固定已验配置及FP16退路，不让便宜规则或平均accuracy批准所有请求。<!-- source-family:SF-2026-ARXIV-2605-23057 -->

### XWind — PLATFORM-GPU-SCHEDULER

窄位：Ch63 `Power Budget 是分层资源契约` 中原 `SF-2026-ARXIV-2605-01837` marker 后、“把GPU数量当唯一容量”前，插两段及本人末注；Ch56不重复解释站点容量控制。

> 当供电容量随站点变化时，固定 GPU power cap 或停机可以守住电力上限，却可能把服务能力和排队尾部一起压垮。另一条条件分支把功率预算先变成站点可用执行配置，再以实际延迟、KV占用和队列状态调节并发/实例资源，并把这份可用容量交给跨站点请求路由；本地硬功率限制与全局请求分配是两层控制，不能只用总GPU数或平均利用率代替。
>
> [XWind 的作者试验](https://arxiv.org/html/2605.23348v1#S4)在64张A10040GB上模拟三个风电站点，支持这种telemetry驱动的组合接口；反应式指workload控制，不代表无需功率信息或profiling。其15分钟功率轨迹为oracular并线性插值，站点间WAN延迟被忽略，本地阈值也依赖profile，因此不据此保证真实风电预测、WAN或生产P99。控制采样、实例配置、profile和跨站点协调增加成本并可能滞后/振荡；功率或服务状态不可靠时，保留保守cap、固定容量和可拒绝的admission，不以局部尾延迟收益授权超出设施边界。<!-- source-family:SF-2026-ARXIV-2605-23348 -->

两项PRE待指定reader当前owner/局部完整邻接核验与root窄写协调，未写。

## A9 — A8 实际 POST / 两项含糊准入定点补读

压缩恢复重读当前 AGENTS、Research/Report、来源用法/每日/arXiv、Prompt、ROADMAP与本日最新路由。有效 Source/PRE/POST 不重开。reader R13实际PRE通过，root授A8两处窄位；作者逐项实际保存，指定reader实际顺读完整新增、完整前后邻接及本人注，ModeSwitch与XWind均POST PASS并释放。当前7新整合＋MARGIN具体NC，不是最终候选数。Qwen无已观察精确历史端点；旧站仅2025、新Research动态当前页和有限bundle恢复未能给May25历史slice，停止无因逆向，后续隔离该具体覆盖缺段，不记无命中。

两项此前完整题摘后仍含糊，实际读exact-v1核心以决定贡献，不用审阅成本或已有主题缩池：

- [Orbax 2605.23066v1](https://arxiv.org/html/2605.23066v1)：实读§1–5。不是仅一个新库＋速度数字：sequence-of-steps manager与singular checkpoint分层、可分离typed checkpointable、abstract shape/dtype/sharding与具体磁盘表示分责，直接改变跨训练/评价/恢复的checkpoint接口契约。准入，拟2+2+2=6；进一步必要证据围绕同步/异步持久化、resharding及直接性能反侧，不能把20次隔离IO测量当完整训练加速。确切日期组合另核后进表。
- [When Is Next-Token Prediction Useful? 2605.23278v1](https://arxiv.org/html/2605.23278v1)：实际读§4–8、16–17。核心是常见的条件独立/条件互信息、混合分布与support概念重新表述文本充分性；没有新的可检验充分性判据、模型/学习机制、定量反证或证明支撑其“缺训练条件则不能可靠处理”强断言。不能把“文本概率非事实/检索不等使用”等已有一般限制、或章节可映射，当作本材料增量。贡献前排除，不评分；非因没有实验排除理论，也不否定该文教学讨论价值。无需为不影响处置的日期另开请求；当前v1未见撤回/纠错提示。请reader校准该具体理由。

## A10 — 两篇 ready 的具体 Books PRE / 末批题摘

### Co-ReAct — AGENT-REFLECTION

作者实际读§3.1–3.3/Eq1–5、§4.1–4.6/T1–3及Limitations；reader必要Source已通过。现有Ch80在AEWM段承载执行前重写与独立权限，但尚无以候选排序训练外置step-rubric、再verify/single-retry的分工。实际读Ch80 100–120完整局部、开篇及Ch79/81交接。窄位：Ch80 `SF-2026-ARXIV-2609-28416`后、`多约束任务还存在一种有用的不对称`前，以下两段＋本人末注：

> 执行前反馈还可以先学习“本步骤应该满足什么”，而不只训练一个整体好坏判断器：从同一轨迹分叉采样多份候选action，由多judge排序；外置rubric generator产生带权原子条件，再以这些条件诱导的排序与参考排序的一致性训练。部署先注入当前步骤的rubric，再由verifier检查候选action，只在未达门限时带着逐条件反馈重试一次。Rubric、action proposal、条件检查和真实observation由不同接口承载；排序对齐只改善所用评判信号，不赋予judge事实真值、工具权限或安全授权。
>
> [Co-ReAct的有限搜索对照](https://arxiv.org/html/2605.23590v1#S4)中，未经训练的rubric反而退步，说明“多一张检查表”不自动有效；学习到的排序偏差也会被继承。离线分叉/多judge/GRPO和在线rubric、verify与retry都计费，更多tool calls及未匹配的总预算限制净收益归因，prompt-only商业模型分支也不是相同RL训练的迁移证明。质量、反馈独立性或预算不足时，保留原ReAct、有限普通retry或可靠外部verifier；重试上限只限制开销，不能认证检索完整或最终回答正确。<!-- source-family:SF-2026-ARXIV-2605-23590 -->

### HyperParallel-MoE — TRAIN-DISTRIBUTED-TRAINING

作者实际读§3、§4.1–4.5/Alg1/T1–2、§5.1–5.3/T3和§6.1–6.2；reader深入Source通过。Ch36已有slice overlap与buffer readiness，但尚未承载把通信和异构计算共编译为两类device队列、按合法tile/remote可见性发event的具体静态taskflow分支。实际读Ch36开篇和295–318完整局部及35/37交接。窄位：Ch36 FlashOverlap段末`最终 optimizer-step barrier 继续持有提交权。`后、`通信配额之外，collective kernel 本身也能改变争用方式`前，两段＋本人末注：

> 若MoE算子结构与shape bucket在稳定训练阶段可预知，还可以把通信本身编译成device任务，与矩阵和向量计算共同排程：先声明算子依赖和合法SplitSpec，沿图传播tile分区，保留GMM的K归约维度；不满足上游分区就退回unsplit。编译器再生成异构compute/vector两类队列及event阈值，runtime仅取任务、等依赖和触发后继。单向remote-write须等数据对接收者globally visible才更新完成event；队列次序不替代跨队列readiness，提早发信号会把“已发送”误当“可读”。
>
> [HyperParallel-MoE的Ascend A3实现](https://arxiv.org/html/2605.23764v1#S4)展示这种tile级组合，但静态计划只能在既定依赖、分区和硬件语义内重排，不能由DAG或一个event名推导任意队列实现无死锁。SSC编译、shape失配重编译、metadata/event和buffer维护都有费；64A3/bf16受测MoE的balanced模块收益不等sampled-natural整步收益，较小8K微基准还反退。新shape、路由布局或完成语义无法验证时，保留unsplit、普通collective与显式阶段同步，以数值和完整step验收，不把局部通信隐藏当全模型等比提速或任意GPU兼容。<!-- source-family:SF-2026-ARXIV-2605-23764 -->

末批已完整读exact-v1题摘/版本史及精确DOI registered（同arxiv.content/findable），新增拟准入：23045 TIME Machine（2+2+2=6，point-track masked motion表示而非更大视频训练）；23176 DriveSpatial（2+2+2=6，跨视角持续身份/graph-grounded QA盲区）；23216 CaSTBench（2+2+2=6，答案与时空证据链联合验收）；23491 CoSPlay（2+2+3=7，Code-UT双向execution matrix更新与consensus，需防共同错误）；23237 StereoGenBench（2+2+2=6，matched scene独立baseline/intrinsics/pose控制生成评测）；23733 Any2Any（2+2+2=6，kinematic input/output对齐与dynamics-sensitive PEFT分责）。均非领域指标单独准入，必要Source仍待。23255为通用learning-augmented online scheduling，只有抽象job/预测误差/preemption界，没有模型训练/推理具体机制关系；不因可映射GPU scheduler入选，范围前关闭，不评分，不否定调度理论价值。22834 QASC虽然有潜在query-conditioned chunking增量，但v1 Apr29，至May25 findable区间跨日，不能以登记当本日首次公开；保日期资格缺口，不先评分/入表。六项v1各在Thu18:00UTC–Fri18:00UTC内，精确注册均May25，联合区间同BJT日；23491的May25 v2是另一个版本线索，不将提交日直接当公开日，定点核该变更，不自动全diff。请reader准入校准。

## A11 — 定点纠正、ready NC与来源/分层排除复核包

### 新证据改变23255的暂拟范围判断

A10只依据题摘暂拟的范围EX不生效：实际进一步读[23255v1](https://arxiv.org/html/2605.23255v1)§1/1.1/1.2/5/6，看到PMLF从预测work层开始、epoch内PF虚拟速率与非抢占rounding，直接建立完成时间/抢占次数的条件界，能支撑异构资源调度基础而非仅应用类比。改为准入2+1+2=5；reader独立实际读必要§2/3.1–3.3证明及同一反侧后标准Source通过。主理论all-available t0、known rates、underprediction，overprediction需g上界与reset；work milestone不是持久化checkpoint，不能推出真实GPU抢占/迁移费用或LLM SLO。实际v1 FriMay22 05:58:52Z＋exact DOI arxiv.content/findable registered May25 01:49:39Z联合同日。保留改判轨迹，不按费用调分/缩池。

### 已完成与具体已有覆盖

Co-ReAct/HyperParallel已获root精确窄授权并真实保存。指定reader对完整新增、完整直接前后、本人注实际POST通过；HyperParallel本人注分项机械错写曾是3+2+3，已在reader读回后恢复原A5的2+3+3=8，正文未改。两窄位释放，现9新整合，非日级完成。

π0-EqM实际Ch26 350–395完整链、371–375既有semantic-body承载fixed-point/residual threshold/iterationcap/warmstart、行为验收、假收敛、objective-stop-warm混杂及原decoder/controller退路，reader实际NC通过。OnePred和ToolMerge的采用范围分别限定为bounded intent-state/predict-compress分责、typed calls→rankings→boolean merge physical-plan；作者实际顺读Ch75 686–718及Ch76 1434–1464，当前两段semantic-body已承载各机制、detail-loss/quiet-confirm和工具coverage/evidencegate/single-scorer退路，reader已实际核同局部。正式采用该收窄范围，具体NC，不声称覆盖论文所有超参/训练或benchmark结论；Source细节另记，不为NC扩大附件。

另两项拟具体NC待reader：Efficiency Frontier只采用预处理/每query分账与复用改变策略选择，实际Ch75 219完整段已有预建索引更高前置成本/更高质量/多query复用，313完整段有压缩器＋目标全成本break-even、可摊销结果和model/hardware/length/batch重算，承载该收窄选择，不把论文amortized token proxy当实测latency/$/能耗。OpenSkillEval只采用access≠procedure compliance≠artifact outcome，实际Ch66 1444–1458分层control-path与4970–4974 Trigger/Compliance/Boundary已明确该链及no-skill/registry/失败回退；不复制30技能快照排行，不把forced read当执行或以有限人评签全可靠。

### 来源与停止点（当前实际证据包，非全源无遗漏）

| ID | 实际补窗入口/停止范围与本地原件 | 目前可支持与缺段 |
| --- | --- | --- |
| SRC-OPENAI | `SUP_openai_rss_20261021.raw.xml`逐item筛May25，2项00:00GMT=08BJT；两官方正文已实际读、reader R2独读 | 经济使用统计first-hire与Grupo Folha/UOL授权合作均贡献前关闭，非本窗零raw。curl正文403不抹掉web已读核心。 |
| SRC-ANTHROPIC | Research主列表＋FRT/Alignment/Interpretability/Economics/Societal/Engineering实际当前team切片，原主/Engineering与Containment保存 | Engineering May25 containment准入；FRT May22→Jun3、Alignment May8→Jul8、Interp May7→Jul6、Economics Apr22→Jun16当前边界；Societal需补具名相邻边界，不能只用搜索无May。 |
| SRC-GOOGLE-AI | Google官方`/blog/2026/05/`实际web月档4项May1/19/27/28，`SUP_org_recovery_20261021.web.json`保存；Publications当前year-only、DeepMind当前10月blog/RSS有限失败 | 月档当前无May25研究blog；Publications与DeepMind缺历史日级slice，隔离而非无命中。 |
| SRC-META-AI | 原Research请求timeout，officialPublications实际“Sorry content unavailable”，同web原件 | 历史必要目录不可恢复，不用于no-hit。 |
| SRC-QWEN | 旧`qwenlm.github.io`仅2025边界；`qwen.ai/research`实际当前动态shell，有限真实bundle恢复保留SUP_qwen原件 | 没有May25历史slice，未授新站阴性覆盖；不再无限逆向，重开需官方历史目录/dated公告原件。 |
| SRC-DEEPSEEK | 当前主页`SUP_deepseek`，`/updates`跳API文档首页`SUP_deepseek_updates` | 没有恢复May25历史事件列表，不能复用旧Apr24/Jun24断言；有限外部缺段。 |
| SRC-MOONSHOT | Platform Blog当前仅2025，GitHub org当前首30repos creation切片，`SUP_moonshot_github` | 当前creation相邻Apr20/May22后July不等全部事件/发布历史；May25技术blog/release历史slice缺段。 |
| SRC-TENCENT-HUNYUAN | 本日Research实际bundle确认`https://api.hunyuan.tencent.com/api/blog/publicList` POSTpageNum/pageSize/renderType；zh11=total11、en9=total9，publicAt/publishedAt/display逐条；`SUP_hunyuan_publiclist/en` | 当前全部可见目录切片无May25，display相邻May21/Jul6；Hy3-preview多字段跨月不冒首次公开。错误同host404保留但不授覆盖。 |
| SRC-ZAI | 官方Research当前HTML `SUP_zai`实际日期相邻May20/Jun16 | 当前可见目录无May25；不证明被删/未保存历史页完整。 |
| SRC-BYTEDANCE-SEED | 真实JS `get_article_list_v2`＋Publication=1/Blog=2；论文page_token0/20共38实际日期递减，May26→May16跨窗；`SUP_seed_papers0/papers20`。Blog2p0当前12行/total24/next20实际日期Oct14→Apr23→Feb13，Jun23与Apr23跨窗 | 当前相关paper/blog切片无May25目录日期，不能等同arXiv首公开。type0两次空响应是错误type线索，不能授Blog0hits；paper类型才用x-tt-locale US。 |
| SRC-BAIDU-ERNIE | 官方技术博客`SUP_ernie`当前可见最新明确May9 | 当前slice无May25，不能授历史完整性。 |
| SRC-XIAOMI-MIMO | 官方Paper/Blog当前undatedcards及May12,2025，GitHub当前18repos creation列表原件 | repo创建非release/论文事件，May25历史技术页仍缺日期/目录slice，不把旧March13/Jun29当当前证明。 |
| SRC-MINIMAX | 当前Blog `SUP_minimax`实际May26 sparse-token-forgetting/May27MavisAgent卡片 | 仍需实际前一日期边界；原JSONLD May27仅关该事件，不能授May25全源阴性。 |
| SRC-ARXIV | 错误API日期query实际rewritten字面串/October返回无效。DataCite registered精确UTC May24 16Z–May25 15:59:59Z两页1000＋81只宽发现；主线title语义/完整相关题摘；CL skip1150/show100、LGskip3100/show100、DCskip0/show250官方正确月表实际相关标题切片，原CL1300/LG2800等窗外探针不授覆盖 | 不把1081/月份目录变全项队列，不以旧263公告覆盖补窗。已入选逐项exact-v1/DOI组合；22863/22864/22873/22882/22894/22834跨日资格隔离，官方abs及月表不缩窄到单日。 |

### 代表性贡献/范围排除供独核分层校准

完整题摘已实际读的代表：23715 NLG Evaluation Past/Present/Future是历史综述/未来影响讨论，无新测量判据或反证；22937 RAS Text2Cypher仅标准execution-reflection与独立resampling的n5语法修正，没有改变有效性条件/长期机制；22923 AI-Friendly LaTeX是已知source/aux/macros/xref预处理Markdown/JSONL食谱，无新可验证机制或边界；23578 Safety/Liveness/Fairness Quantitative Argumentation为抽象argument graph性质重用，与当前模型系统仅类比；23568 TactileReflex为传统阈值/12Hz低层控制，声称可接VLA但无实际模型接口/耦合证据，非把所有机器人排除；23448 Incentivize Defense统计/倡议未给新的具体执行/评价约束；23278 nexttoken理由见A9已独核。OpenAI2项由reader R2全读。无撤回/纠错/安全修订提示被仅按主题关闭；普通明确scope排除只作抽检，不声称全1081题摘或全EX独核。

## A12 — B-GRTO / SkillOpt 逐字 PRE与最后具名含糊题摘

### B-GRTO — TRAIN-GRPO

作者实际读v1§3/Eq1–10、§4/4.1/T1–2与§5；reader必要Source已通过。实读Ch33开篇、clipped objective及最后权重分支至`## Sequence Reward 怎样作用到 Tokens`，与Ch32/34交接；现有只更新policy/调整reward或credit，无可微工具单独参数的gradient接口。窄位：Ch33 `## Sequence Reward 怎样作用到 Tokens`前两段＋本人末注。

> 若reward来自一个可训练的模型工具，冻结工具能保持policy目标稳定，却可能把工具对新prompt的失配误当成policy不会推理。一个条件分支用同批旧policy rollouts做两份更新：policy仍消费冻结reward/advantage的GRPO surrogate；工具另以sequence importance ratio加权可微surrogate loss，权重对工具更新停止梯度。它不是把梯度穿过离散tool-call选择，也不把BCE/soft-IoU当作离散最终IoU的精确导数；policy、behavior快照、工具参数和reward版本须分别保存。
>
> 工具还可先在reference-policy replay上预热，再联合训练，以免小工具每次更新都等待昂贵policy生成。[B-GRTO的有限分割对照](https://arxiv.org/html/2605.23500v1#S3)支持这一接口选择，但有限buffer只近似理想posterior、缺有效prompt的类别仍缺监督；policy漂移、两学习率失配和小数据过拟合都可能退步。离线rollout/storage、工具训练、联合optimizer与独立质量回归全计费，不能由复用采样或较快收敛宣布免费、普遍最优或跨域鲁棒。工具不可微、反馈或buffer支持不足时，保留固定工具的policy-only GRPO、独立工具监督与普通验证路径。<!-- source-family:SF-2026-ARXIV-2605-23500 -->

### SkillOpt — AGENT-PROMPT

作者实际读v1§3各机制/§4必要评价、ablation、cost与AppendixB；未采用完整prompt附件或全表排行。reader必要Source已通过。实读Ch74 154–228完整规则维护/constraint-residual/SkillMOO chain及73/75交接；尚无拒绝编辑buffer与protected slow/meta文本状态分责。窄位：Ch74 SkillMOO段后、`### 条件化机制分支与共存边界`前两段＋本人末注。

> 对一份反复修改的procedural skill，还可以把编辑强度和负反馈显式变成优化状态：失败/成功minibatches先各提局部patch，再合并冲突并按本轮edit budget截断；候选只有在固定selection split上严格胜过当前版本才接纳，失败patch连同分数下降留在epoch内rejected buffer供后续反思。跨epoch的slow guidance写入局部patch不能覆盖的保护区，optimizer-side meta经验只帮助提出编辑，不随部署skill输出。保护区保持的是编辑责任边界，不是不可错的知识或安全证明。
>
> [SkillOpt的有限对照](https://arxiv.org/html/2605.23904v1#S3)支持这条有界文本优化分支，但反复用于筛选的holdout不是每次新独立检验，严格加分也不保证全局泛化或部署单调改善。Rollouts、optimizer、被拒绝候选的评价与更长skill的在线Context都计费；没有新增optimizer calls不等于零部署成本。任务、harness、judge或依赖改变后须重验，反馈不可靠、规则冲突或净预算不值时，保留人工短skill、旧已验版本与独立最终测试，不让更高selection score获得事实、工具或发布授权。<!-- source-family:SF-2026-ARXIV-2605-23904 -->

### 最后具名含糊线索，非另开宽池

完整exact-v1题摘已实读[23651 Register-aware linguistic evaluation](https://arxiv.org/abs/2605.23651v1)，v1 FriMay22 14:04:25Z＋exactDOI arxiv.content/findable registered May25 01:58:52Z联合同日。准入拟2+2+2=6：把“像人”从全局标量改为按register匹配人类参考分布的two-sample MMD，模型排序随register翻转，改变语言风格评价的参照人口，而非普通语言学应用或仅扩大benchmark。必要Source待审。

另实际读DataCite完整题摘：23130 Preventive→Reactive security是15工程师访谈/观察的人类安全意识与prompt行为，未建立模型训练/推理/Agent执行机制或可验证控制接口；仅泛设计建议/人类实践，拟范围EX（不是称其研究无效）。22929 Prox-ITEM研究smooth strongly-convex composite的span-based gradient/prox oracle最优距离界，没有当前模型优化/系统设计所需的新接口或适用条件桥梁，拟范围EX而非“所有优化理论排除”。以上两项请reader校准；如果范围事实含糊，只定点补core，不因代表EX名额关闭。无撤回/修订信号被忽略。

## A13 — 四项 ready Books 逐字 PRE

作者已实读各精确v1必要方法、评价条件及直接反侧；reader相同必要Source均已通过。非因已有主题或成本缩池。目标局部和相邻章节已实际读，以下各两段＋本人末注仍待reader实际PRE/root窄授权。

### SCOPE — MULTIMODAL-WORLD-MODELS / Ch25

实际§3.1–3.4/§4.1–4.4/T1–4/§5；Ch25 action-conditioned transition现只声明action schema及多条件分支，未承载同一帧的local discrete/global continuous视觉查询。窄位：Ch25 `Action-conditioned transition`第一完整段“...action contract。”后、`跨 embodiment 时`前：

> 一个action向量也不必在整帧产生同样影响：局部离散事件与连续ego-motion可以通过不同条件通路消费。先把latent重排成每个空间位置的时间序列，让局部视觉feature查询离散事件tokens；连续控制则与相应时间窗的feature融合，再做时间attention，最后把两路残差加回原生成器。它把“哪些位置响应哪类控制”变成可学习接口，不是已有显式物体mask、真实作用区域或动作因果的保证。
>
> [SCOPE的短片对照](https://arxiv.org/html/2605.23345v1#S3)支持该分支的局部价值，但跨模型baseline先把telemetry经Gemini译成文字，不能把整段差额都归因架构；同telemetry的global-injection消融才提供较窄对照。双通路、端到端finetuning、动作标注/归一化和CFG采样都计费，合成初帧的五秒响应不等持久world state或真实physics。动作支持、局部响应或长程状态无法验证时，保留全局/单条件生成、短horizon与显式simulator，不把稳定画面或可控外观交成真实行动许可。<!-- source-family:SF-2026-ARXIV-2605-23345 -->

### World Machine — MULTIMODAL-WORLD-MODELS / Ch25

实际§3–5（训练协议/任务定义/Toy1D/必要protocol与hyperparameter反侧）；Ch25 Latent dynamics仍以encoder取得state，未承载跨epoch预测回写的latent-state训练接口。窄位：该小节第一完整边界段“必须用 action-conditioned outcome 验证。”后、`Latent state 也可以是一份小型坐标 renderer`前：

> Latent state也可以先作为训练数据的可更新部分，而不要求每次由固定encoder直接给出：初始化一份逐时刻state，每个epoch用当前模型预测下一state，时间移位后回写为下轮输入，序列首state归零；感官mask、分段和偶尔关闭历史attention，再迫使单state携带可续接的信息。这改变了数据state与参数训练的共同生命周期，不把回写出的向量当真实环境标注；跨epoch state identity、mask时是否回写与部署的顺序生成必须分清。
>
> [World Machine的初步实验](https://arxiv.org/html/2605.23025v1#S3)只在Toy1D两层/state128模型上说明可训练性，单state浅预测仍弱，部分协议还增加不稳定；15模型的protocol比较与9600配置各一次、剔除发散的人口不能混成稳定普遍收益。多轮遍历、stored-state维护与所有协议训练都付费，论文没有真实多模态或LLM省费证据。需要可靠控制、state不足或大数据反复遍历不合算时，保留encoder-based latent、较完整history、原监督预测与真实观测，不让一份短state自行认证world辨识或动作充分性。<!-- source-family:SF-2026-ARXIV-2605-23025 -->

### Fast-dDrive — MULTIMODAL-EMBODIED-VLA / Ch26

实际§3–4/T1–5及必要输入/效率/开放环反侧；当前Ch26 action codec和flow分支未区分已知schema scaffold与实际值的draft/verify资格。窄位：`联合模型减少语义 handoff，不等于消除物理接口。`前：

> 动作由固定结构交付时，可以先冻结schema的键名、括号和标点，只让模型预测内容值，再按语义section划block并约束section间的因果可见性；先完成的固定prefix可以保存KV，后续value块由并行drafter提出、causal head检查。这分开了语法scaffold、可学习动作值和cache资格：模板正确不证明坐标、轨迹或行为安全，greedy首错接受规则也不能直接升级为随机verifier下的精确AR分布。
>
> [Fast-dDrive的有限驾驶对照](https://arxiv.org/html/2605.23163v1#S3)支持该结构化解码路径，但单H100/bs1的TPS计入直接填好的scaffold，额外SGLang kernel/graph收益又是另一层工程变化，不能全算算法加速。共享prefix、多trajectory分叉和训练loss/noise设计都计费，残差均值的1/N解释需要独立性，平均两条可行动作也可能落入不可行区。当前只测open-loop；schema、采样分布、闭环或完整deadline未验时，保留普通AR/原action head、单条已验轨迹与独立controller，而非用格式完整或平均轨迹误差签发实车安全。<!-- source-family:SF-2026-ARXIV-2605-23163 -->

### ARES — TRAIN-DATA / Ch27

实际§3.2/§4.1–4.4/A/E/F必要域；Ch27 synthetic开篇虽有生成/过滤，未承载document-grounded self-contained QA/reference/weighted rubric三者共生成的训练对象。窄位：`...语言上自洽不等于环境中可执行。`后、`生成网页操作示教时`前：

> 开放任务缺少单一exact-answer verifier时，数据生产还可以把题目和判分合同一起生成：从经过筛选的source document出发，按domain/persona共同提出self-contained question、source-grounded reference及逐题带正负权重的rubric，再分别检查题目是否自足、reference是否忠实、条件覆盖和权重格式，最后去重并排除评价重叠。Source支持答案，不意味着部署需要读source，也不意味着同源generator/judge已经提供独立真值。
>
> [ARES的Qwen3-4B训练比较](https://arxiv.org/html/2605.23454v1#S3)支持把原文改造成这种监督对象，但逐题rubric不是每任务都优于通用rubric/reference；较高平均分不能消除Health/Writing反侧，生成与训练预算未完全匹配也不授唯一因果。文档筛选、共生成、QC、32B judge与RL训练全计费，不把“一次生成”称零额外成本。题目自足、来源或判分资格不足时，保留curated QA、可靠binary verifier、原始文档和人工审核；rubric的可读性不取得知识正确性或安全发布权。<!-- source-family:SF-2026-ARXIV-2605-23454 -->

来源普通待办更新：Societal实际team页L58–82为Jun12→Apr30，已保存`SUP_anthropic_societal_20261021.raw.html`；MiniMax当前Blog实际完整日期邻接May26→Mar18，May27 Mavis另事件，故当前目录slice无May25，不将当前slice授历史被删页完整性。Seed Blog真实enum=2，`SUP_seed_blogs2p0`12可见记录total24/next20，全部日期已读，Jun23→Apr23跨窗；type0成功空响应为错误类型，不采为阴性依据。

## A14 — 四篇 ready PRE / 实际来源纠正与差额

指定reader已对A13四项真实保存内容、完整前后及本人注实际POST PASS，四窄位释放。当前15新整合＋6具体NC；普通Books与日级复核仍未完成。

### Dual-mode Cyber Benchmark — PLATFORM-EVALUATION-SYSTEM

作者实际v1§3.1–3.6/§4.1–4.2/§5–7及Limitations；reader标准Source通过收窄。实读Ch66 2446–2513 executable/effect评价链，现有未明确whitebox函数检出与blackbox行动确认的两个分母。窄位：`### Compound Artifact 需要 Preservation Contract`前一段＋本人注：

> 安全能力还要分开函数级white-box判定与会话级black-box执行：前者的FPR以benign函数为分母，后者的report precision以提交finding为分母，duplicate、technically invalid、no-impact与真正可利用也不是同一类错误。[一个有限双模式benchmark](https://arxiv.org/html/2605.23243v1#S3)提示工具可调用不等于跨用户/session状态和证据比较被正确使用，但模型、训练、预算与harness同时变化，不能据此认证methodology唯一因果，更不能把deterministic confirmation叫zero-FP。目标/补丁、认证上下文、原始请求响应和逐finding身份应与全部失败尝试一起保存，人工groundtruth、执行和triage全计费；生产噪声或oracle不足时，保留分项测量、原始证据与人工复核，不由局部平均检出或更低报告量签发自主安全能力。<!-- source-family:SF-2026-ARXIV-2605-23243 -->

### Orbax — TRAIN-CHECKPOINT

实际v1§1–5及AppendixC saving/finalize；reader准入已通过，必要Source请实际核相同采用域。Ch35 209–234现有globaltensor/shardmetadata与resume/convert区分，但缺typed separable checkpointables和abstract/concrete接口。窄位：该节末`...weights-only conversion 中的哪一种。`后两段＋本人注：

> 跨训练、评价和推理复用时，checkpoint还可先拆成独立可序列化的typed checkpointables：参数、optimizer与data iterator各自有handler，consumer只加载自己需要的部分；step-level manager负责保存序列与curation，单个checkpoint接口则负责具体一次读写。Abstract对象另声明shape、dtype与sharding，具体对象负责真实值和磁盘表示，加载时以abstract规格提出cast/reshard或部分读取，不能由文件存在或weight可读推断完整resume成立。
>
> [Orbax的JAX设计](https://arxiv.org/html/2605.23066v1#S3)提供该契约实例，但custom handler与metadata兼容维护有成本，类型描述也不替代跨组件的一致step或最终化。保存先复制稳定host snapshot，背景IO结束且global metadata合并/finalize后才能称完整；异步save返回不代表持久化完成。作者A10040GB/GCS上20次隔离IO测试不是整段训练加速，较小模型与blocking阶段仍有反退。类型/布局或finalize不能验证时，保留原生框架格式、完整state与上一已提交checkpoint，不因可定制加载自动批准optimizer轨迹等价。<!-- source-family:SF-2026-ARXIV-2605-23066 -->

### Parsimonious Preemption — PLATFORM-GPU-SCHEDULER

实际§1/1.1/1.2/2/5/6，reader标准Source及必要unrelated proof已通过；仅采用预测work/抢占次数的条件分账，不搬未读malleable证明。Ch63 138–156完整quota/preemption局部没有预测误差下次数预算。窄位：`...不能把 victim 只表示成“释放 8 GPU”。`后、静态quota重议分支前一段＋本人注：

> 预测作业work量还可改变抢占节奏，而不只是SJF排序：从预测量对应的几何work层开始，只有累计work越过下一milestone才升级队列；异构机器分支先按虚拟公平速率组成epoch，再舍入为受限非抢占片段。[PMLF/SNAP的条件分析](https://arxiv.org/html/2605.23255v1#S2)把completion与抢占次数共同约束，主设定需全部job在t0可用、known rates及underprediction，overprediction另需数量上界/reset。这里checkpoint是累计work门槛，不是持久化训练checkpoint，次数少也不证明GPU迁移便宜；求解/rounding、预测与真实保存恢复仍计费。未知arrival、rates或预测失配时，保留FIFO/保守quota、已验reclaim和真实workload成本测量，不把synthetic job保证当LLM serving SLO。<!-- source-family:SF-2026-ARXIV-2605-23255 -->

### CCEM — AGENT-PLANNING

实际v1§2.1–4/§6–7与AppendixC直接预算反侧；reader深入Source通过。采用域§3/4/6/7实际v1/v2规范文本完全一致；block0唯一差为arxivv1/May22→v2/May25标签，不把提交日当公开日，不重复评分，不全附件diff。Ch79 Search-based开篇/Pruning完整局部没有composition-preserved convex factor几何。窄位：`Pruning、heuristic、budget...搜索更多不等于可靠性单调提高。`后两段＋本人注：

> 对能拆成局部约束的形式任务，还可以改变候选空间的几何，而不只扩大搜索：让每个factor能量对被优化变量保持凸，再以非负权重求和，在声明的凸relaxation上做投影求解。凸性在组合后保留，避免新增非凸局部陷阱；但正确性还需要valid解的certificate、无效margin与足够小的近似误差，不能由ICNN架构本身认证离散答案。Context分支可以非凸，决策变量的convexity责任仍须单独检查。
>
> [CCEM的有限组合任务](https://arxiv.org/html/2605.23395v1#S3)支持这个条件分支，不证明任意推理可化为可解凸程序：Birkhoff约束不是含diagonal的完整N-Queens凸包，fractional结果还需greedy decode，表达性/平坦区域与离散validity仍成压力。预训练factor、unrolled solver、随机warmstarts与重复投影全计费；正文预算口径及“凸landscape仍multimodal”的矛盾不拼成统一recipe。Relaxation、certificate或最终约束无法核验时，保留原搜索、明确离散solver与独立verifier，不以低energy或局部最优为提交证明。<!-- source-family:SF-2026-ARXIV-2605-23395 -->

### KnowledgeWork具体NC与来源机械纠正

作者实际读23262v1§3.1–3.3/§5–6必要论证，采用只限被测activity/setting/workproduct应绑定能力claim，不采用18活动taxonomy为真实部署量化。实读Ch66 149–188 EvalSpec目标人口/failuretaxonomy/scorer与GDPval artifact/one-shot不代表澄清迭代监督、native-editability实际维护检查；当前正文已承载这一收窄命题，拟具体NC，reader此前实际锚点复用。不是新增三个术语就重复写书。

A11 DeepSeek入口说明纠正：作者依reader线索实际解析`SUP_deepseek_updates_20261021.raw.html`，确为**Change Log**而非API首页，当前完整Date headings Oct17/Sep10/Aug21/Aug13/Jul31/Apr24后2025，Jul31→Apr24支持当前changelog无May25，不再虚列该层恢复失败；不升级为全Research历史完整。MiMo Paper的Jun29→Mar13和Blog15无日期/More分层待作者定点读回，不能统称全源undated。

reader有界月表具名12项的差额检查：22981/23036/23157/23170/23019/23061/23215/23362/23464均实际在May25原候选完整行，对应旧有效精确事件，定点去重不继承该日池；23911/23914/23918不在本日或May25原表，也不在本日1081registered原件，精确v1日期恢复正在做，未以ID段排除或先标全完成。CL/LG覆盖引用为`SUP_arxiv_CL_slice`(21965→23657)与`LG_slice`(22776→23510)，不是target/bound探针。宽月表仅有界线索，不授整段全排除。

## A15 — 两项 ready PRE 与 Evaluation-awareness 具体 NC

A14四项已由指定reader真实POST通过并释放，当前19新整合＋7具体NC。此处仅继续末12项普通Books，不重读已有效Source/POST。

### Encrypted neural networks — PLATFORM-SECURITY / Ch72

作者实际读23096v1的威胁/攻击说明、§4方法概述与输入域/误差传播责任、§5–6及AppendixC直接反侧；reader深入Source已通过。采用限定到polynomial range与approximation error的分责，不采用完整求根实现或未核artifact。实读Ch72“隐私不是一个开关”完整FHE/MPC→秘密共享编译→HE-Guardrail局部；现有泛近似误差尚未承载前层误差传播后的范围合同。窄位：`TEE、客户端本地推理、普通 TLS 加服务端明文各有仍然成立的信任与性能区间。`后两段＋本人注。

> 密文域用多项式替换非线性时，还须把“训练样本上常见的数值范围”与“允许输入域内可达的范围”分开。合法但不常见的输入可能把中间activation推到拟合区间之外，使高阶多项式迅速放大；只在原神经网络上取样范围，不能认证已经替换过的执行图。一个保护分支先声明输入域，再逐层传播已引入的近似误差，以得到后续多项式的实际输入bounds；区间、系数、误差预算与编译artifact必须绑定同一版本。
>
> [受限加密神经网络的分析](https://arxiv.org/html/2605.23096v1#S4)支持这种范围合同，但验证器soundness、数值求根与输入域假设仍需成立，宽bounds还可能增加degree、系数条件数及构造成本。其形式界明确不包含CKKS noise，不能由此签发密文全栈零错、任意Transformer或重复查询安全。Bounds构造、近似、密文执行和行为回归都计费；范围、误差或加密噪声无法共同验收时，保留较保守多项式、原始明文对照及本地/可信执行边界，不把一层近似通过当完整模型的正确性授权。<!-- source-family:SF-2026-ARXIV-2605-23096 -->

### Unpack — PLATFORM-EVALUATION-SYSTEM / Ch66

作者实际读23393v1§3.1–3.3/各dispatch、§5全部直接限制、B2与E完整knockout协议；reader必要Source已通过。实读Ch66 Attribution Contract现有全部邻接及紧随的Interpretability Graph两段：现有覆盖干预压缩图，却无attention/MLP统一key-value分解与非干预credit的责任边界。窄位：`### Interpretability Graph 只有 Diagnostic Authority`前两段＋本人注，不修改既有23080家族。

> 不运行逐组件干预，也能从一次实际forward提出另一类诊断：把attention与MLP都写成selection-weighted value lookup，先按输出方向分配value credit，再沿key-side的线性分解递归回到上游residual components及输入tokens。Query固定、是否追踪Q/K/V分支、LayerNorm分解和credit方向都是方法合同的一部分；带符号贡献接近抵消时的soft floor能限制数值放大，却会牺牲严格credit conservation，不能把路径分数当模型本身提供的唯一解释。
>
> [Unpack的精确v1](https://arxiv.org/html/2605.23393v1#S3)已有selected-component knockout校准聚合key-side分数，但这不把递归token/path credit变成counterfactual truth。IOI与pre-norm模型的有限对照、已知mode筛选、深层path-volume和top-k/pruning都会限制可推广性；全上游投影、路径枚举与校准也付费，不是一次forward就免费得到解释。架构不符、路径截断或高风险因果命题无法验证时，保留原始activation与匹配干预，将该分解仅用作提出hypothesis和复核优先级。<!-- source-family:SF-2026-ARXIV-2605-23393 -->

### Evaluation-awareness 采用范围与具体 NC

作者实际读23055v1§2.1/§3–6必要协议与B1/B3直接反侧，采用仅限environment cues、可观测verbalization和行为control不可混同，aware/unaware观测分组不授识别的因果效应。不另采用八因素分类为已独立验证的完整因果分解。实读Ch66 4706–4754，现`Evaluation-awareness必须分开Representation、Verbalization与Control`完整段明确sensor≠内部知道/因果控制、模板/数据集/后训练混杂及真实deployment slice；这实际承载本次收窄命题，拟具体NC。既有八月来源不替本次五月Source审阅，只复用当前Books语义覆盖。

## A16 — 三项 ready PRE

### TIME — MULTIMODAL-REPRESENTATION / Ch23

作者实际读23045v1§3全部token/backbone/masking/loss/data、§4任务/linear-probe与ablation、§5反侧；reader相同必要Source有效。实读Ch23开篇与`时间、空间与provenance必须进入状态`起始完整局部、Ch22/24交接沿已读未变层。现有时间身份/grounding与运动codec没有独立point-track masked representation。窄位：`若augmentation改变左右方向而action label未同步...控制语义已经被破坏。`完整段后两段＋本人注。

> 若任务主要消费运动，还可以把外观与运动交给不同表示：从point tracks构造局部位移、相对首帧的累计位移、邻域关系与occlusion tokens，训练时遮掉整条轨迹而非零散时刻，迫使encoder从空间与时间上下文重建运动。局部位移避免绝对位置的shortcut，累计位移约束误差累积，动点加权则防止大量静止点支配目标；这仍是所选轨迹表示的学习合同，不是已恢复真实对象、相机时钟或动力学。
>
> [TIME的有限对照](https://arxiv.org/html/2605.23045v1#S3)支持把此表示与外观features互补，但静态相机合成训练、外部point tracker及筛选/crop后的任务人口限制迁移。Frozen features的下游任务仍训练linear probe，不能称无需任务标签；video-hours差额也不是完整compute节省。轨迹提取、遮挡误差、模型训练和两路消费都计费，纯运动又会丢失外观信息；快速模糊运动、tracker失配或任务需纹理语义时，保留RGB/video encoder、原始帧与独立任务头，不由较好运动probe签发全视频理解或行动安全。<!-- source-family:SF-2026-ARXIV-2605-23045 -->

### MetaEvaluator — PLATFORM-EVALUATION-SYSTEM / Ch66

作者实际读23595v1§3/§4.2/§5–6必要域，reader有效Source已明确support labels反侧。实读Ch66 Forecastability→Litmus完整局部：已有paper-corpus能力猜测，没有train/target hidden-state摘要和带真accuracy support的amortized接口。窄位：Forecastability现`SF-2026-ARXIV-2605-15134` marker后、`对尚无目标语言或模型直接测量的能力预测`前两段＋本人注。

> 性能预测还可消费模型内部表示而非论文叙述：分别汇总原训练集与待测输入在目标模型下的hidden representations，用带真实性能标签的reference tasks训练一个预测器，再以目标任务摘要请求accuracy估计。这里训练数据访问权、representation layer、聚合器与task/model身份共同定义sensor；预测器输出不是实际执行目标任务所得的成绩，也不能替代目标人群的独立测量。
>
> [MetaEvaluator的精确v1](https://arxiv.org/html/2605.23595v1#S4)还在unseen-model context adaptation中使用带真accuracy的support，所谓label-free只限最终target，不能宣传无标签新模型全流程或任意black-box API。Reference与support标签、hidden-state提取、512-context适配及目标回归全部付费，少量微调不等免per-model学习；未独立验证的预测区间也不授校准覆盖。原训练集/activation不可得、支持人口失配或风险过高时，保留直接评价、外部证据与Unknown/保守区间，不由较低平均误差或分钟级headline签发生产能力。<!-- source-family:SF-2026-ARXIV-2605-23595 -->

### Register-aware linguistic evaluation — PLATFORM-EVALUATION-SYSTEM / Ch66

作者实际读23651v1§3–6/§9与必要sample/bandwidth协议，readerSource有效。实读Ch66人类参照/2603-26589两完整段及其前后：有scene-conditioned embedding分布，但无register内固定feature标准化/bandwidth的two-sample评价。窄位：2603-26589第二段后、`评分还会反过来改变被优化的行为。`前一段＋本人注。

> 对“语言像人”的声明，还须先指定register及其人类参照，而不把会话、新闻、学术和故事混成一个总体距离：在同类情境下生成文本，抽取固定语言features，以同register内冻结的标准化与kernel bandwidth比较两样本分布，再用不重叠人类样本的重采样距离估计参照波动。[受限的register-aware评价](https://arxiv.org/html/2605.23651v1#S3)观察到模型排序随register改变，但English/67features、有限长度和样本人口只定义该测量，不认证事实、流畅、叙事或安全；few-shot也可退步。参照整理、生成、feature提取、重复取样与prompt回归全计费，换register后不能直接沿用原量尺；人口、features或实际用途失配时，保留分register结果、人工/任务质量与原用途评价，不由更小MMD授予总体“更像人”或训练因果。<!-- source-family:SF-2026-ARXIV-2605-23651 -->

## A17 — Metadata intervention 与 CoSPlay ready PRE

### Metadata intervention — PLATFORM-EVALUATION-SYSTEM / Ch66

作者实际读23701v1§2–5，reader深入Source沿有效层；实读Ch66 data-withheld负控制→输出分数shuffle→historical预测审计完整局部。现有明确输入/输出干预不同，但尚无固定question/label、替换跨item evidence的配对测量。窄位：`SF-2026-ARXIV-2603-17692`第二完整段后、`任务难度切片也不能只按输入长度或实体数划分。`前两段＋本人注。

> 判断题目是否依赖所附证据，还可以固定question与label，在items之间置换模型可见evidence，再在同一reader上比较原配对与置换配对的accuracy。它与只给metadata、移除输入或打乱最终分数是不同干预：后者可能混入任务难度、输出对应或接口破坏，配对evidence替换则直接检查这份reader对evidence identity的敏感性。应保存置换、reader、原/变换输入、标签与逐题输出；accuracy差接近零不等全部outputs不变，也不证明模型完全没有读取证据。
>
> [受限的metadata-intervention审计](https://arxiv.org/html/2605.23701v1#S3)显示结论可随reader family改变，某一重建数据的启发式label及严重类别失衡更不能外推为原benchmark天然无证据。多次置换的离散程度不是均值standard error或显著性检验；正差也只支持当前reader的证据敏感，不独证语义推理。输入重构、标签核查、多reader/置换和独立正控都计费；替换改变合法任务、标签资格或reader不稳时，保留原任务分数、人工证据检查及独立控制，不由一个接近零的差额签发全模型shortcut或无grounding的结论。<!-- source-family:SF-2026-ARXIV-2605-23701 -->

### CoSPlay — AGENT-REFLECTION / Ch80

作者实际读23491v1§2.1–2.4/3.1/4.9/A1.1/A2必要域，reader深入Source与采用域v1/v2有限比较均有效；本地HTML全文件不完整但上述section完整，未伪称全附件下载。实读Ch80原检验义务/反例查询/15669主动分裂→AEWM完整局部。原有只改测试或候选选择，尚无双池co-evolution中重算execution matrix与non-trivial支持分责。窄位：15669主动分裂完整段后、AEWM执行前反思段前两段＋本人注。

> 当代码与自生成unit tests都要演化时，先保存完整code×test执行矩阵；任一池改变后重跑受影响配对，重新判定哪些测试既有支持又能区分候选，再用于修复，而不让旧pass counts继续担任新池的分数。低支持测试可能揭示共同bug，也可能与少量错误代码耦合，因此替换是搜索策略而非判错。最终高分候选还可在无需预期标签的随机有效输入上比较输出；ERR只作缺证，按固定顺序构造pairwise-compatible群，不能把非传递兼容关系说成唯一的程序等价类。
>
> [CoSPlay的有限代码对照](https://arxiv.org/html/2605.23491v1#S2)支持这条双池控制分支，但Round-0独立采样下的pass-count方向不自动延续到互相修复后的相关池；最大consensus的理论还需错误signature分散等假设，共同常量bug可破坏它。GT-free只限选择不读GT，评价仍需隐藏真值；token/call预算也不包含完整执行墙钟。想法生成、全部重执行、测试修复、聚类与独立最终验收均付费；测试语义、独立性或支持失配时，保留可信固定测试、原候选和独立oracle，不由全矩阵通过或最大群批准正确性与真实执行。<!-- source-family:SF-2026-ARXIV-2605-23491 -->

## A18 — 最后四项 ready PRE

A16/A17五处已指定reader真实POST通过，现26整合＋8具体NC，四项Books普通待办如下。全部必要Source作者已实际读足且reader有效层复用，不以待办数倒推处置。

### DriveSpatial — PLATFORM-EVALUATION-SYSTEM / Ch66

实际23176v1§3.1/4.1–4.3/5/B1/B3/C3；现Ch66多视图局部consistency与跨depiction未承载track/camera支持约束的图式构题。实际完整局部已读，65/67交接沿未变有效层。窄位：`SF-2026-ARXIV-2604-00799` marker后、`几何对象固定后`前两段＋本人注。

> 要测跨视图空间推理，构题时还可先建立带时间和track identity的多关系图：节点绑定对象、坐标与可见camera，edge分别表示空间、交互、动作及跨帧同一track；跨view身份题要求同一对象在多camera可见，关系题则限制两对象没有共同camera，避免单视图捷径。图与QA规则拥有的是标注支持和任务构造，不是被测模型内部已经形成同一世界表示的证明。
>
> [DriveSpatial的有限驾驶评价](https://arxiv.org/html/2605.23176v1#S3)提供这种支持约束实例，但GT/HDMap或LiDAR boxes生成的BEV只是privileged诊断，排除construction题后的收益不等可部署感知改进。不限回放的人类mini子集、模型固定输入/greedy与不同来源人口也不能拼成同预算全量能力差或因果瓶颈。坐标统一、metadata人审、图/QA制备、采帧及全部推理评价均付费；track/可见性、来源或题目支持不足时，保留原视图、分项几何任务和人工核查，不由跨view高分批准真实驾驶或闭环安全。<!-- source-family:SF-2026-ARXIV-2605-23176 -->

### CaST-Bench — PLATFORM-EVALUATION-SYSTEM / Ch66

实际23216v1§3/4构造与metric/5.1–5.3必要反侧；reader含14.2有效。现Ch66 PerceptionComp只核条件必要/组合，没有多实例时空证据链与正确答案的联合验收接口。窄位：PerceptionComp26653完整段后、`在线流视频还存在不同的评价混杂`前两段＋本人注。

> 视频答案还可被要求交付逐实例的时空证据链：每条证据绑定时间区间、对应帧上的bbox及rationale，先在预测与参考instances间匹配，再分别测时间/时空重叠与最终答案。这样能区分答对却没有交付合格grounding、已定位部分证据却答错，以及两者同时达标；匹配、阈值和答案分母必须冻结，不能把一个联合分数当成所有错误类型的互补划分。
>
> [CaST-Bench的精确v1](https://arxiv.org/html/2605.23216v1#S4)以mask过滤与人审构造该接口，但低grounding也可能来自坐标/格式表达失败，GT链提示有益不认证模型真实因果faithfulness。原视频与1-FPS采帧、reference制备及LLM judge都影响证据资格；mask过滤留下的人口不代表全部视频任务。链标注、实例匹配、解析、模型与judge调用均计费；支持不可见、链完整性或格式失配时，保留答案/定位分项、原视频与人工复核，不由正确MCQ或可读rationale签发真实因果推理及行动许可。<!-- source-family:SF-2026-ARXIV-2605-23216 -->

### StereoGenBench — PLATFORM-EVALUATION-SYSTEM / Ch66

实际23237v1§3–6/H指标与controls；现Ch66静态背景几何估计代理没有受控baseline/target-camera的输入tier与同场景配对规则。窄位：SGC19048第二完整段后、`动态前景还可单独建立运动参照`前两段＋本人注。

> 双目生成还应把相机baseline、intrinsics、depth与pose作为受控变量，并在同scene的配对视图上检查目标camera是否真的实现；给GT几何、只给camera metadata和仅单目输入是三种不同任务，不能跨tier合成一张胜负榜。原画质相似、可匹配纹理与disparity scale也要分开，copied-left或wrong-camera负控制可以暴露“图像看起来合理、目标几何却不对”的盲区。
>
> [StereoGenBench的受限协议](https://arxiv.org/html/2605.23237v1#S4)支持这种分层测量，但当前snapshot每scene只取一个primary pair，metadata支持all-pairs不等已跑完整baseline sweep。P-PSNR可奖励复制纹理，SD依赖固定matcher和valid-pixel过滤，frame-wise指标与FVD也不认证flicker或模型具有时序机制；合成场景不授真实域排名。Render、metadata校准、wrapper、匹配/拟合与质量评价全计费；camera合同、有效支持或真实用途不符时，保留分tier诊断、原图/geometry与独立真实数据，不由单个高分批准通用3D或物理一致性。<!-- source-family:SF-2026-ARXIV-2605-23237 -->

### Any2Any — MULTIMODAL-EMBODIED-VLA / Ch26

实际23733v1§3.3–3.4/4.1/4.3/5；现Ch26 canonical hand/action codec与后续shared interfaces没有kinematic layout/hip/closed-chain先对齐、再独立适配动力学的顺序合同。实际开篇、canonical morphology完整段与前后已读，25/27交接沿有效层。窄位：16712 canonical手型完整段后、`另一条接口分支不让语言模型直接回归metric waypoint`前两段＋本人注。

> 复用whole-body tracking policy时，还可先分开坐标语义失配与动力学失配：重排observation layout，按已知joint correspondence将状态、reference motion和action history送入source布局，另处理hip-axis与closed-chain耦合；输出再经目标映射交回native controller。随后冻结已学主干，只在声明的proprioception、输出与critic等模块加低秩适配。相同向量长度不保证相同身体语义，手工kinematic映射也不能替代目标动力学与接触的闭环学习。
>
> [Any2Any的有限humanoid迁移](https://arxiv.org/html/2605.23733v1#S3)支持这条先对齐后适配的分支，但相近topology、injective关节对应及剔除冗余joint不授任意本体的双向无损；物理参数较少也不证明最优policy修正必为低秩。MuJoCo验证不是实机安全，少量适配compute还复用了已付pretraining，采样率/硬件变化不独证算法省费。Retarget、标定、privileged训练、PPO/adapter和目标回归均计费；映射、动力学或控制deadline不合时，保留native policy、完整目标微调与独立controller/停机接管，不由较小adapter签发真实执行。<!-- source-family:SF-2026-ARXIV-2605-23733 -->

## A19 — 真实来源停止与精确日期资格保留

本节纠正A11的过宽缺段表述，不能拿旧入口失败替代当前已可执行恢复。作者实际恢复并保存DeepMind `/blog/page/2/`（193477bytes）及`/3/`（184265bytes），并实际打开[Singapore原页](https://deepmind.google/blog/strengthening-singapores-ai-future-a-new-national-partnership/)，页面明确May20。当前按日期递减目录page2由July/June到May，紧邻前项[Gemma4-12B官方页](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/)为Jun03，page3继续May→April→March；指定reader已独立核两侧。故Jun03→May20夹住本窗，支持**当前目录slice无May25卡片**，不需展开18个窗外May卡片，也不证明被删历史页完整。Google Research Blog May月档四项May1/19/27/28同样只授当前月档切片；Publications year-only的日级历史限制仍保留。

作者实际去MiMo raw的脚本后Paper正文读完8行：Jun29 MOPD→Mar13 ARL-Tangram→Feb03 HySparse→Jan08 MiMoV2Flash→2025Oct21 RouterAlign→Sep19 Audio→Jun04 VL→May12 MiMo，故当前Paper slice无May25；Blog15张undated cards与More仍是单独历史日期缺段。DeepSeek真实Change Log、Seed type2 Blogs与真实page_token、Hunyuan code0三日期字段的窄结论沿A13/A14与reader实际R22复用；不授全历史召回。Qwen、Meta、Moonshot及MiMo Blog缺段仅保当前可用入口的有限恢复边界，不改称无命中。

### 三项晚发现线索：只隔离日期资格，不排除贡献

完整exact-v1题摘已读，三项具有潜在主线机制，但实际唯一v1提交记录分别为Apr07/09/15；不能把2605 ID或提交日当公告日。作者本轮实际单独请求并保存精确DOI元数据，均为`arxiv.content`/`findable`：

| 身份 | v1 Submitted UTC | registered UTC（不是实际公开时刻） | 当前判断 |
| --- | --- | --- | --- |
| [2605.23911 TritonMoE](https://arxiv.org/abs/2605.23911v1) | 2026-04-07T16:21:02Z | 2026-05-26T03:02:25.000Z | earliest按适用公告日程可早于目标日，latest已到May26，可能区间跨日 |
| [2605.23914 VineLM](https://arxiv.org/abs/2605.23914v1) | 2026-04-09T15:31:22Z | 2026-05-26T03:02:30.000Z | 同上，不能仅registered判May26归属 |
| [2605.23918 Model Parking Tax](https://arxiv.org/abs/2605.23918v1) | 2026-04-15T09:01:24Z | 2026-05-26T03:02:35.000Z | 同上，不能仅registered判窗外 |

`SUP_dc_23911/23914/23918_20261021.raw.json`保留上述字段与唯一身份；Updated字段May26只是元数据更新时间，不冒称公告日。旧本日和May25原候选、原官方证据包均定点无此三项；root定点询05-27作者也没有可复用有效公告。当前官方月表CL1250/100、LG3200/100补检原件已保存但无三ID直接日门，标题+May26的arXiv站内搜索三次空，不作阴性日期证明。没有已观察可执行的日级历史端点可继续；精确隔离为资格保留，不评分、不列确定候选、不进入Books，也不授source no-omission。可接受重开材料：精确ID的官方日公告/列表、作者有日期的首次正文或可验证归档，使整个可能区间能落单一BJT自然日；只重开这三项，非另扫月份。

此前22894/22882/22864/22873/22863/22834同类跨日资格保留沿A9/实际原件，完整题摘潜力没有变成贡献EX；各自必要公开日期缺口与重开要求不变。以上9项不同于已通过联合约束的37项arXiv候选；不能因共同方法对9项不收敛便推翻37项有效日期组合，也不能拿37项有效组合填平9项缺失。普通来源扫描/筛选已到上述停止，候选拟冻结38家族；最后四项Books/PRE/POST与六节DAY、保存完成态FINAL尚待，不写完成。

## A20 — Qwen真实新入口解除缺段与六节进行中草稿

root提供本轮实际端点后，作者本日实际GET `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`，保存`SUP_qwen_actual_api_20261021.raw.json`；success=true、data仅articles、无pagination字段，共40行。作者逐行实际读title/extra.date，原数组并非日期排序，不能按位置停；按日期边界May20 10:00+08 Qwen3.7→May29 17:00+08 Qwen-VLA（LiveTranslate May19）夹本窗，40行无May25。指定reader也独立实际GET并逐字段核同结论。这里只关闭当前公共目录切片，不授被删历史完备；A19及以前“Qwen无观察端点/未恢复列表”是本次恢复前历史状态，不再作为终态缺口。报告§1/§2/§5已同步，历史来源子层从5类改4类，其余有效Source不重开，候选仍38。

A18四处实际POST已reader通过，当前**38=30真实整合＋8具体NC**，写入16唯一owner，Books普通待办0。所有38必要Source/准入/日期组合以及9资格保留均已独立核。六节进行中草稿已保存124候选（原86完整行＋新38），原小时窗及旧§4连续保留，新增证据在旧块后，不挪动旧材料。新增32深入/6标准；合计Books67整合/50NC/5旧结构候选/2旧仅报告。

当前V3校验已通过；初次机械错误为旧日期缺显式冻结档案与新NodeID藏在link label（被parser移除），均仅用本日原档案字段/新行明文NodeID修复，旧86行无改。`baseline-before-supplement-20261021.md`由启动快照保存，实际bytes与原`/private/tmp/daily-20260526-before-supp-20261021.md`完全一致；现有index未动。38候选本地引用检查0 missing，两层限定diff-check通过。本人后批23条Review notes的`POST另核`仅行政同步为已经发生的指定reader唯一POST，不改正文/评分，不第三读；早期其余有效实际POST沿R5–R29。

指定reader正实际六部分DAY，尚未给日级通过，不提前改完成。DAY通过后作者再保存完成态、复跑机械检查，reader有限FINAL回读，之后才交root；不自行跨日。

## A21 — 实际DAY通过与完成态保存

已实际读指定reader R30/Qwen与R31完整六部分DAY PASS：38新家族32深入/6标准、30实际整合/8具体NC及124总候选均通过；四类历史来源子层和九项资格保留安全隔离，没有普通研究/Books/POST或active窄位。DAY修复两处分项抄写：EqM23128恢复A5原3+2+2=7，KnowledgeWork23262恢复A7原1+2+2=5，总分/深度/处置不变；CoReAct定位收为§3–4/T1–3/Limitations，Efficiency Frontier为III–V采用域/直接cost反侧，不虚报额外附件。原86整行/日期评分与连续旧§4不动。

作者于2026-10-21T11:49:26+08:00保存完成态，§1/§5已移除已完成DAY普通待办，§6结论通过明确据R31，不预授FINAL。完成态V3再通过，173本地引用0 missing；启动tmp/冻结档案bytes相同，原86顺序逐字/原小时窗/旧§4完整连续保留，124=86+38；30新家族正文source-family在唯一owner恰一处（23080复用旧family/新semantic-delta）。报告/作者SUP及16Books owner限定working/cached diff-check实际通过，现有index未改，不称全仓clean。

本人Review notes中剩余早批14条旧`实际POST另核`也已纯行政同步为既成指定reader唯一POST，不改body/评分、不第三验收；不把note行政次数加进30整合数。接下来只请指定reader对保存完成态有限FINAL；成功后将结果行政同步、交root，不自行换日。

## A22 — 保存完成态实际FINAL通过，交root

作者已实际读指定reader R32：对11:49:26保存态header/§1/§2最新Qwen/四历史层、§5隔离与重开、§6和A21作有限FINAL，独立V3/冻结与本地引用/限定两层检查通过。**R31 DAY＋R32 FINAL均已实际PASS，本日完成。** 作者仅行政同步README §5/§6的既成FINAL，不改候选、证据或Books，不要求第三读。最终新38=30实际整合＋8具体NC，原86整行/日期评分/小时窗与连续旧§4保持，总124；四历史来源子层与九日期资格保留不授正面Coverage/Evidence/Books或无遗漏保证。普通研究/来源/筛选/Books/POST及active窄位0，全部ownership释放，交root；未stage/commit/push、未改LS/索引/合同/脚本，不自行跨日。
