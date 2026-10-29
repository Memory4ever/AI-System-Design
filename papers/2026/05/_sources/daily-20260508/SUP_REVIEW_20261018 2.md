# 2026-05-08 补遗漏：独立非作者实际复核

复核者：`supp_may08_reader`，恢复为`may08_resume_reader`；报告作者：`supp_may08_author`，恢复为`may08_resume_author`。仅补2026-05-07北京时间自然日；原184候选、日期、评分、小时窗及连续原§4不搬移。本文件只有实际完成层，DAY/FINAL只按后续明确实际记录授予，不由前层自动推出，也不代表旧184重新审阅。唯一写权限本文件，未改Report、Books、LS或index。

已独立重读AGENTS、当前研究合同、Report合同、来源使用说明/每日组/主题、统一Prompt、ROADMAP、LS最新路由、本日README当前开头/来源/候选层及作者唯一SUP A1–A5；旧长库存不转逐项队列。使用daily-research-closure技能分离准入、必要Source、owner与实际POST；其不替代当前合同。

## R1 两官源：准入、必要Source与日期实际通过

### Natural Language Autoencoders

实际打开[官方摘要公告](https://www.anthropic.com/research/natural-language-autoencoders)及[全文](https://transformer-circuits.pub/2026/nla/index.html)，直接HTTP恢复正文Method、case interventions、五预测任务、confabulation/claim deletion、evaluation-awareness、automated auditing及Discussion。web正文提取失败不是原文不可得。公告和论文均直接注明May7,2026；自然日日期通过，不补造时刻。

准入链：activation解释缺少可知真值 → AV文本瓶颈与截断AR重建联合训练提供可检验假设接口 → 评价需分离重建保真、语义忠实与独立机制验证。不是仅因“interpretability”或Ch66主题匹配准入。2+2+3=7合理，拟采用命题必要Source通过；Books具体差额/实际正文未授。

已实际核到AV以负MSE为RL奖励，AR做MSE回归，同批同时更新但互不反传；SFT warm start与KL维持可读性。FVE只量重建，目标并不直接奖励人类可读或语义faithfulness。toy reward→penalty差向量与随机干预对照支持局部作用；诗歌编辑仅约半数成功且可能不协调。五预测随训练改善不能构成跨模型预算受控比较，classification83→86的改进有限；删除真claim相较假claim的重建差异只有弱逐claim判别力。文本会hallucinate，AV可作超出activation的信息推断，极限可steganography或复述输入。未观察到严重steganography≠排除全部隐写。

awareness无可见真实belief标签，三类manipulation只能提供方向一致验证；50token采样还有漏检。auditing的generic-data NLA不等于初始化无target知识：其初始化为model organism权重，已包含合成文档的隐式知识。Sonnet4.6 auditor/scaffold及rubric与旧研究不同，不能跨scaffold直接比；无data-search能提升root-cause，PT-only搜索已强、NLA不再增益，quirk数未显著增加。每activation数百输出token及双模型训练限制规模。A5边界保留正确，不采用“读出真实thought”或普遍审计优越性。未复现实现。

### Accidental CoT grading

实际读[官方May7全文](https://alignment.openai.com/accidental-cot-grading/)从detection到incident analysis、representative experiments和recurring stress tests。直接日期通过。准入链：常规channel过滤被误当reward隔离 → 实际reward输入扫描发现CoT可经tool output间接进入奖励 → 后训练需要审计真实奖励数据流，配置声明不能替代运行路径。3+2+3=8合理；纠错/安全深审必要，A5最小命题必要Source通过。

完整Instant confirmation-penalty重跑只移除CoT访问并保其他训练，heldout aware/blind detector与checkpoint结果支持该局部未见明显降低。Thinking只有reward重算而非完整ablation；prompt-injection没有targeted因果检查；稀疏比例不建立安全阈值。stress tests在足够压力下改变表面CoT，flaky-tool一数据集recall降低是直接反侧；不得用总体无明显下降抹去。相对reward强度、环境覆盖和conditional discoverability是局部解释，不是已证普适量化公式。regex对非标准输入不完备，未披露budget/hardware不得代填，未复现内部pipeline。TRAIN-RLHF为合理待比owner；Books具体差额/POST未授。

### 同事件去重范围

对2026当前README仅点名查询`Natural Language Autoencoders|accidental[- ]cot[- ]grading|Accidental CoT|nla/index.html`。唯一命中本日旧SRC-ANTHROPIC因09:00截点隔离的来源缺口，无有效候选/证据同事件；没有全文读取别日报，也不将旧缺口当作已处理重复。两事件可在本次自然日补查继续，不重计发布/代码/摘要为多家族。

普通待办：全部拟P与代表C题摘独立校准、arXiv日期/必要Source、作者来源有界收口、root具体owner/PRE/POST、六部分DAY及保存完成态FINAL。04356撤回必须排除，04128/04093跨日日期不预授，04834更早会议正文资格待有限核。尚未读取的普通队列不改称外部受阻。

## R2 23题摘与分层排除校准；三项假阴性定点重开

实际从官方abs读取A3/A4全部23完整题摘，不依赖作者摘要替代；其22有效项都存在具体待核增量，准入通过不等于Source通过。04356当前官方标withdrawn，维持退出新增候选/评分/Books，旧v1不得被v2顶替。05151只是PatchTST窄/单层/forecasting局部反例，05197 probe/likelihood分离保semantic-plausibility负侧，04352五trace只支持四类评分的盲点，04899几何相关不证明causal world model；均不因局部、小模型或负结果排除。04128/04093/04834的潜力判断不授本窗资格。

独立逐一重取22有效项的DataCite精确DOI与当前官方abs唯一v1，`relationships.client.data.id=arxiv.content`、`state=findable`及全部`registered`原字段与A4表逐行一致。05073/05126/05054/04547/04641/05092/04412/04458/04903/05116/04313/04304/04352/05151/05197/04962/04834/05031/04613/04899共20项，v1提交均在May5 18:00UTC之后至May6 18:00UTC之前，EDT官方日程给最早May7 08:00BJT，registered最晚May7 09:49:54～10:11:36BJT，先后合法且全区间同一自然日。仅限定arXiv announcement，不推全球首稿；04834仍有具体会议更早稿信号。04128 v1 May5 15:49:47UTC、04093 Apr29 09:59:36UTC的最早界可早于May7，组合跨日，不能只取registered目标日；仍需直接归属依据。未使用Created。独立打开04834两个具名OpenReview论坛仍challenge；这是具体资格缺口，不是否定其arXiv组合，也不扩大历届会议扫描。

代表排除抽样为11项官方完整题摘：04726/04902/04225/04565/04831/05148/04264/04488/04127/04704/04227，覆盖移动部署应用、非LLM清洗/MARL、压缩、治理观点、伦理局部评价、model-collapse观点和工具/主动助理。其余明确标题范围外项未逐篇复核，不称全量验证。04726只给推荐场景收益未披露可迁移部署约束；04902非foundation训练数据管线；04225/04565非模型驱动Agent或大模型状态/切分机制；05148终端人类图片codec非基础模型表示接口；04488只得伦理问答agreement，无模型机制或monitorability边界；04127串联已知model-collapse影响，无新机制/反证，维持关闭。

04264有trace信号，因此额外恢复精确v1 PDF §3–5而非仅看“Viewpoint”关闭。正文机制自称四设计问题而非固定实现pipeline，主要是private/shared/archive/project分层、显式ratifier、evidence/provenance/version lineage及supersede-not-erase；单生态12事件/8原则/17资源/22版本的质性trace只展示这些基础流程可用，不含新增失效成立条件或比较，post-governance fabrication也不证明新防护。关闭理由限定为未新增改变设计选择的证据/机制，不因没有controlled experiment一律否定观点材料。

以下三项原C理由偏窄，作者已接纳重开；具体共同错误是“领域应用/模块组合”标签抹掉已披露的实际机制或评价盲点。只重开受影响三项，不把全部应用论文扩为候选：

- [04831 StoryAlign v1](https://arxiv.org/html/2605.04831v1)：实际§2构造/人类验证、§4.2 Figure2及§5 BoN。通用RM在Human–LLM子集比LLM–LLM更差，揭用生成式偏好池评价时可能掩盖target-human偏好的盲区，不能只当领域新benchmark关闭。最小采用是按内容来源/人类偏好分层验证RM，不采用“人写天然优”“已证明自偏好因果”或全部LM能力不足。Human–LLM subset把人类指定为chosen，来源/质量/注释混杂；1000余样本不是任意创作外推。BoN为约100premises、Llama3.1-70B、16样本、T1及人评，不能推出泛化RL收益。建议最低5分标准审阅；日期尚由作者恢复，未预授当窗。
- [04704 UVMarvel v1](https://arxiv.org/html/2605.04704v1)：实际§3.1–3.6、§4.4–4.7。协议控制流/handshake固定，LLM只改designated regions；dependency-preserving Filtered DUT把有效依赖留给刺激生成，并仍在original DUT执行，区别于随意摘要缩context。IR对spec省掉bus monitor/register wiring等遗漏；fixed non-bus context下protocol library对AXI生成成功率、FilteredDUT相对rawDUT/Vizier覆盖增量提供局部机制证据。收益不能等同形式verification/工业正确性，waiving存在、六设计有限且LLM预算未全等化，不泛称所有RTL。拟5分；本层独核支持该最小机制及直接反侧，不是复制UVM应用排名。日期待作者。
- [04227 Pro2Assist v1](https://arxiv.org/html/2605.04227v1)：实际§4.4.2/Alg1、§5.1–5.2、§5.4.4–5.7。预测新step只当candidate，窗口majority才将active step记completed；step/status不变则抑制重复response。它控制历史更新和外部发送，不只是“state-aware”改名。去checking局部Step-Acc/STS均降低、重复打扰增多，是temporal commit/打扰代价的可核案例。默认W6/threshold0.5、Qwen3-VL4B且LoRA10epochs，20人、10任务混合人/LLM注释，缺跨域强保证；早期多数一致也可能错，gate引入延迟。RTX5090/Orin计算时间、TTFT和网络延迟不能混成闭环延迟。拟5分；日期待作者。其余机制不因本次准入自动升格。

本节只授上述题摘准入/代表关闭与三项窄Source层；没有完成其余论文必要Source、Books具体差额或全日报验收。

## R3 R2窄校准纠偏；两官源实际Books链通过

R2记录当时三项重开；随后root质疑04227是否只是已知temporal smoothing/去抖的应用。重新对照已经实际读过的§4.4.2及§5.4.4–5：滑窗majority及相同state不发送、删组件后的任务分数下降，只证明这些既有组件在该场景有用，没有新commit可靠性成立条件、失效边界或足以改写本项目原判断的反证。我此前以commit/state术语抬升不当。**04227改回明确C，不评分/不进入新增候选/Books**；不是因局部实验或已有覆盖排除，也不因已投入Source而保P。仅04831与04704的具体新评价盲点/替代界面继续，其他未受影响题摘不重开。

UVMarvel追加实际§3.4–3.6/§4.1–4.7后，最小可准入不是“context越少越好”：uncovered-signal种子在每文件查read/assign并经I/O递归回到top-level controllable inputs，syntax patch只恢复wrapper，LLM刺激最终仍回originalDUT模拟；这与一般摘要舍弃依赖或只在slice上验证不同。FilteredDUT/rawDUT/Vizier对照支持这个局部界面选择。原算法/系统不是形式等价证明，waiver candidates可影响最终覆盖，AXI AW/W/B协调仍失败。主要比较code coverage、functional covergroups依人工定义；20.17×/4.5h明确从human-provided IR开始，排除test planning/IR authoring，不能当端到端无人设计加速。不将成熟program slicing或protocol template原则本身抬分。

两官源Books前已完整读取PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE；对比实际Ch5 private-code/decodability段、Ch66内部测量/AO段及Ch31双reward/30036/MiCo交接，A8选择NLA唯一`WORLDVIEW-REPRESENTATION` Ch5、CoT唯一`TRAIN-RLHF` Ch31合理。NLA不是在Ch66重复AO sensor，新增AV/AR无预设问题瓶颈及目标退化；CoT新增实际grader消费路径与因果证据强度而非再抄通用monitorability。

本reader实际逐字PRE A8及完整两侧通过后，author依root窄授权保存。随后实际读回：Ch5 348–362（旧private-code→354/356新增→fresh-probe）及629本人注；Ch31 890–905（30036两段→898/900新增→MiCo）及1330本人注。两项各两真实机制段与A8一致、marker各唯一、原有效负侧及交接保留，独立非writer实际POST通过。note当时如实停在PRE未预签POST，author可行政同步后再读回；这不授本日DAY/FINAL。未修改Books或index，未stage/commit/push。

## R4 A7七arXiv必要Source实际独核通过；两官源note同步读回

实际读回NLA Ch5:629、CoT Ch31:1330两纯note的POST标签，准确记录已经发生的两段/完整邻接/本人注独核，不授日级完成。两项窄锁可释放。

以下精确v1正文通过HTTP直接解析，必要方法、关键对照和直接反侧实际核到，非从作者笔记签字。日期复用R2逐原件组合；当前后续revision不替代本次精确v1，也没有因版本号自动遍历所有版本。所有结论未复现。

- [05073 HJA v1](https://arxiv.org/html/2605.05073v1)，2+2+3=7，深入：实际§4识别规范、§5 Thm2–3/假设A1–7、§6 Table1/Fig2–3及§7。`S=γμᵀ+UVᵀ`的row-mean/orthogonality/anchoring定义canonical consensus，并不是从任意分解得真值。γ是响应共识的强度，不是judge质量。WaldCI需固定N/K/r、增长重复、稳定sampling fractions/connected/local regularity；full ranking ties不光滑，优化只保证局部basin。50seed synthetic及20seed四real对照含in-house strong-perturbation/near-tie不支配；协调偏差可同时污染共识。A7最小采用“分清估计对象及模型条件CI”成立，不能声称rank证书/保护adversary。
- [05126 ConsisVLA4D v1](https://arxiv.org/html/2605.05126v1)，2+2+2=6，实际深入：§4 eq3–21/§5 Table1–7/G1。instruction FiLM/topK与VGGT cross-view、DINO/VGGT aggregation、training-only动态/深度decoder有清楚机制；部署不显式产未来对象/深度而用implicit knowledge并行action。FastV/SliME相同比率及module/attention消融支持局部设计，1/16比1/8更差；72.7/108.2为predicted actions/sec不是camera/闭环Hz。OpenVLA与OFT基线增益不同，batch/chunk不同必须绑定。实机15trials、ablation两任务30trials，局部仿真/实机不授安全。必要Source通过，实际owner差额尚待。
- [05054 DP-FM v1](https://arxiv.org/html/2605.05054v1)，2+1+2=5，标准：实际§3 metric/slerp与Alg1、§4 Table1–3及公平HFM脚注。constant warp使radial/angular路径独立是该几何内命题，不证明任何特征norm=calibrated confidence或所有非constant几何不合理。11datasets/1,4,16shot，统一features/CFG/time shift的几何比较刻意拿掉HFM两阶段；Table2完整baseline有另一训练表示，不可混比较来纯归因。不同格存在负侧、multi-step velocity/CFG与训练费用不能被平均accuracy遮盖，不推服务SLO。A7最小表示几何/归一化边界采用通过。
- [04641 CAST v1](https://arxiv.org/html/2605.04641v1)，2+1+2=5，标准：实际§4 eq5–11/§5主要任务/§6 Table5–7及α/K搜索。masked视觉only末token输出训SVM来选head，真实steering向量却用原unmasked输出均值差；不能描述成同一分布或免所有训练。1000预训练VQA和white-box access要计成本。POPE调参使外推需谨慎，α大挤text、K大破非视觉path；precompute约1x不等zero成本，on-the-fly1.8x且质量较差。基础能力局部保持不认证全能力，作者实际5模型/5bench限定。最小caption-conditioned head intervention采用通过。
- [05092 Driver-WM v1](https://arxiv.org/html/2605.05092v1)，2+2+2=6，标准含反侧：实际§3.1–3.3/§4.1–4.4/Table1–3。frozen Qwen3VL2048、view embeddings、external-only vector gate及history truncation支持无future-pixel条件的5→5自回归latent/skeleton，不识别真实人的因果效应。same-interface static/late fusion与retrained no-ext是必要对照；no-ext HM136.94反优main138.03、ZeroVelocity全局误差更低，TCR等aux语义改进不能替所有动态优越性。**Table3 caption定义Δ为intervened与factual输出的偏移，不是对GT误差增加；正文把15.208等又称error的表述不采用。** 路径关闭造成输出偏移只能证明trained-model敏感性，不能证明重训后necessity或安全。A7最小condition/probe/metric分责采用通过，已通知作者补明Δ口径。
- [04547 Stage-audio v1](https://arxiv.org/html/2605.04547v1)，2+1+2=5，标准：实际§2.1–2.4/§3 Table1–2。每500steps比较平滑视图的SSL discrepancy并局部线性斜率给`g=-a`，不backprop该monitor；Beta采样与regularizer依g，guidance γ却依step预定linear，regularizer还含`1(k≤ρspK)`人工schedule门限，不能跟随作者宣传称全部feedback或无手工phase。三个variant分别加baseline，未证joint synergy。相同backbone/budget两任务只是质量对照，8k SISNR12.73→12.40/12.34的反侧及未充分walltime/seeds/CI使“训练效率/生产加速”需缩窄。A7最小阶段目标/信号适用边界采用通过。
- [04412 DiLAST v1](https://arxiv.org/html/2605.04412v1)，2+1+2=5，标准：实际§3.2–3.5/§4 Table1和loss ablation/AppendixD。冻结3D flow先更新latent，再通过3DGS渲染与2D attention-distillation梯度改latent，避免跨不兼容2D/3D latent直接attention注入；first-stage sparse voxels固定、grayscale content与alpha/smoothness成本/目标各异。A100、SD1.5/Trellis、500steps/5fixedviews/η5是本设置。HPSv3 prompt/VLM aesthetic/10人主观评价不是geometry/physics truth，其他backbone主要qualitative，不证普适latent容量不足归因。最小cross-space teacher轨迹与fidelity tradeoff采用通过。

本层七项只授必要Source与最小命题，后续具体owner/逐字PRE和真实POST分开。其余未读Source、来源有界收口与报告六部分仍普通可执行，未授全日DAY/FINAL。

## R5 A9前四篇：实际必要Source通过

以下均实际直接读取精确v1 HTML必要内容，不是代作者做Source后自签Report或Books；本reader没有写这些产物。最小采用范围与A9一致，新增两项指标/真值限定已通知作者。日期复用R2，owner差额和实际POST未授。

- [04903 DeltaNAS](https://arxiv.org/html/2605.04903v1)，2+1+2=5，标准。实际§3.2–3.4、§4–5/6.1、§7及B.7。unified diff加baseline→patch/syntax/instance/forward→1epoch/novelty分层门是可核机制。§3.3一处称新admitted加入training corpus，但后段明确LoRA始终固定LEMUR，只扩大baseline pool，采用后者，不声称已证自举训练闭环。**Valid在§4.4主要是diff apply/evaluation；§7多数还被post-training validation拒绝，如DS828→89全filters→88novel，不能valid=完整architecture正确。**原full-generation数据集范围、baseline pool等与ours不同，不能由同baseLM就纯归因全部准确率增益于diff。输出行数不是总token/训练/evaluation费用；B.7 top20跨dataset与排除timeouts人口有限，DeepSeek12/.495/p.102不显著，ceiling只是作者解释而非已控制替代原因。只采用改动表示/验证分层及proxy边界，不证明LLM模型结构或edge部署。
- [04313 NoisyCausal](https://arxiv.org/html/2605.04313v1)，2+1+2=5，标准。实际§3 DAG3–7/SCM与六noise、§4 graph-guided、§5 Table1–5/5.3–5.8及§7。known-generator graph与prompted-extracted graph作用分开；graph误边/反向比少删边更敏感、结构F1从clean85.2到confounding+masking74.1，支持层间误差传播的局部诊断，不能称真实观测的causal discovery。BIP保持数值/边关系只改belief线索，79.5结果不证真实因果识别；100error population不是全失败率。CausalQA44.2→49.3改了LoRA训练，无法纯归因“causal skill”或排除其他训练效应。§7称real-world未测与§5.8小scale transfer语言冲突，保synthetic stress-test范围，不选择最强宣传解释。
- [04304 HierVA](https://arxiv.org/html/2605.04304v1)，2+2+2=6，标准。实际§2.1–2.5/Alg1、§3 ChartQA与controlled-composite、§4 Table3–4及Limitations。manager只保final plan与final句/crop handle，worker一图/局部skills，manager不读skills正文；是多模态evidence scope与上下文累积策略的具体分支，不因manager/worker名称入选。ChartQA/小composite中收益不显著区分，CharXiv多步才见局部差额；增加code若无procedure反而下降，skills/context不能被“多工具总更好”覆盖。Table3 PeakTok为episode peak window、不是全worker累计token/calls/latency，2568不能宣称总推理降费。裁错、跨panel/global constraint、summary丢证据及skill库范围限制保留；不授domain全面泛化。
- [04352 Algebraic Trapdoors](https://arxiv.org/html/2605.04352v1)，2+1+2=5，标准含设计反侧。实际§3–5与§6.1/6.4–6.7。构造元数据与solver不对称、finite-index promise改变评价目标、四格commit/abstain分离是可核评价设计；不把五traces的152min abstain-wrong叫正确性或普遍metacognition证明。§6.6承认anti-commitment/prompt-following等替代解释和非controlled，FamilyI未测；§6.7“无external tools”与§5 python/sympy traces矛盾，所以不归因架构、统一budget或真实内部三层。§6.1已承认Sanov benchmark groundtruth6→12修正，构造身份不自动保证真值，仍需独立生成验证。in-preparation数学伴随稿未核，超出正文可直接支持的定理/成本不采用。

四篇仍须具体Books判断，不因source已投入保整合；A9另外04458/05116尚待独核，未列外部受阻。两官源已闭实际Books链不重读。

## R6 A9余二Source与A10四项真实Books链通过

### A9另外两项必要Source

- [04458 DoGMaTiQ v1](https://arxiv.org/html/2605.04458v1)，2+2+2=6，标准。实际§2–6/Stage1–3/Table1–4，document summaries→answer-first QA、question-level clustering保多语alternate answers/provenance、答案validation与AND/OR聚合、19criteria/SVM选top20是具体评价接口，区别于只按自生report评自己。输入检索仍是外部IR，不宣称pipeline恢复所有证据；validation去矛盾答案还有主观选择。RAGTIME16topics/59systems、NeuCLIR21/51及human-nugget/auto-alignment、fullmanual两类reference必须分开。Table2明定manual nuggets+AutoARGUE；§5.1一句manually matched冲突时按实验定义/table，不把.899/τ.734当fullmanual相关。Table3 .768/.586与manual-nugget+auto .804/.630只是本baseline，后者不是数学“maximum possible”上界。**§6.1 12-run是每team highest-priority提交的proxy，不是严格按实际排名删低分后的top-only集合**；稳定相关支持此子集，不能认证任意强系统区分。Claude对Llama的改善不消共享训练/偏好及全部循环，topic-level高variance不能被macro rank遮盖。A9最小rank/reference/population分责通过，具体Books差额未授。
- [05116 Junking v1](https://arxiv.org/html/2605.05116v1)，2+1+2=5，安全反侧实际深入§2问题/§4设定与分母/§5全部核心结果、Table1。四7B、各chat template、greedy、50AdvBench目标，n100/B5/10^5 function evaluations构成白盒概率搜索条件；prefix match可能接拒绝，须独立harm/coherence判分。ASR是每target整条优化轨迹中事后取最高success/再coherence的外部Gemma4-31B judge结果，.52/.62/.64/.90不是一次最终query或随机输入成功率。PPL与Puffin自然text分离只支持分布异常，不证明何时/如何在训练中形成或已植入后门；“natural backdoor”是作者解释，不授来源因果。高FE方差、目标/模型依赖以及更大/闭源/强防守未测需保，成熟greedy原理不算新算法突破。A9最小nonsemantic-scope威胁测试与denominator/训练来源分责通过，未复现攻击。

### A10实际owner/PRE/POST

实际对读Ch66 Jury逐judge正尺度与anchor之间、Ch26 training-only foresight完整三段与milestone之间、Ch23 centroid/paired-geometry与LiteEmbed之间及caption双路与video-reward之间；四个具体缺口与A10一致，不以主题相似当已有覆盖。逐字PRE要求HJA识别规范补残差基锚定/非退化；CAST由“只允许视觉输入”纠正为“末输入token屏蔽对text tokens的attention、只取该位置head输出”，不把局部mask当整模型视觉only。作者保存A10这两处后，本reader实际读回最终拟文并授PRE，author依root既有窄授权写入。

随后实际读取以下真实正文、完整直接两侧与纯note，均与最终A10一致，独立非writer POST通过：

| 材料 | 真实正文位置（本次核验时） | 本人注 |
| --- | --- | --- |
| 05073 HJA | Ch66 482/484，Jury→两新段→anchor | Ch66 6575 |
| 05126 ConsisVLA | Ch26 604/606，foresight→两新段→milestone | Ch26 2661 |
| 05054 DP-FM | Ch23 1027/1029，centroid→两新段→LiteEmbed | Ch23 2458 |
| 04641 CAST | Ch23 1051/1053，caption双路→两新段→video reward | Ch23 2460 |

scope/cost/failure/fallback就近、唯一canonical owner与marker准确，notes只保存原件/必要边界/未复现，不需再加工作流标签。四窄锁可释放，已通知root及author。NLA/CoT note可只删除末句工作流文字，保持已通过机制正文；该行政精简不改变R3/R4既成实际POST。总计本reader已通过6项新增真实Books链（两官源+此四），未授DAY/FINAL，其余owner/有限Source/报告仍普通可执行。

## R7 三项具体已有覆盖独立对读；04834有限资格恢复

作者指定对读04903/04352/04313后，本reader实际核正文与完整局部，支持以下有限`已有覆盖`判断；不是因为主题匹配、分数低或审阅费时改判排除。候选身份/分数/已读Source仍保留，具体实验及未采强断言由报告说明，不在Books添加论文摘要或流程标签。

- **04903 DeltaNAS → AGENT-TOOL-CALLING / Ch78**：当前609–617明确Preventive/Evidential分责；613保存content anchor/expected-old及应用目标漂移，615已有“整份rewrite与局部diff的选择、AST扩成连贯block/唯一anchor、用两表示的token成本制作target、patch可应用/linter/真实test三层不同证据、output token≠walltime/全费及full-rewrite退路”。本次可采的局部diff表示/应用成功不等功能正确、proxy成本边界已被具体承载。static LEMUR、novel baseline pool与1epoch/image-data proxy是本实验上下文，不强造新长期段。
- **04352 Algebraic Trapdoors → PLATFORM-EVALUATION-SYSTEM / Ch66**：55–66分别讲评分诱因、错误/拒答成本、coverage/conditional quality与always-abstain基线；74–91把真实输入缺陷×提示断言、格式合同×语义、合理拒绝/猜答/替代任务/虚报分账，并要求独立输入完整性标签而非模型自述；99另要求reference/GT独立资格。这具体承载本次能采用的四cell最小评价判断及prompt/answerability条件，未声称书已覆盖所有SL(3,Z)构造定理；未核伴随稿与五trace架构归因不入书。
- **04313 NoisyCausal → PLATFORM-EVALUATION-SYSTEM / Ch66**：1982–1988的可干预synthetic SCM明确把held-out prediction与causal graph/equations忠实度分计，保存observation/intervention-policy、实验停止和consistency，依赖independent mechanism audit，synthetic结果不证明开放因果；210–214另保fixed-population negative-control、过滤前后分母、控制失配和未知原因。以上承载可采的噪声诊断/图结构错误与预测成功分责，不把原文graph-guided局部pipeline提升为新通用因果论证。

三项owner具体NC建议已交author与root，最后Report处置由作者依本证据落实，本reader不冒充自己已写报告或Books。

04834只追加一次具名[ICLR稿PDF](https://openreview.net/pdf?id=Dt4XAIKYbf)与[UniReps稿PDF](https://openreview.net/pdf?id=tDX4A4AE5a)恢复，均转Verifying-your-browser并非PDF；未绕过challenge、不扫历届会议。没有带公开日期原件，故仍保具体更早稿资格未决，不把search snippet、会议年份或arXiv registered改名全球首稿日。此项隔离不覆盖其他尚未读的普通Source/Books工作。

## R8 A11四真实Books链通过；Joy直接日期核验

A11实际owner及完整邻接对读：Ch75视觉artifact局部→长视频、Ch25三channel/counterfactual→support restriction、Ch28 meanCE训练进度→PPL定义、Ch24风格/主体注入→对象运输。现正文分别缺global/worker私有image-context、模型external/internal conditioning敏感性证据权限、阶段signal/控制schedule分离、可微render→2Dteacher→3Dlatent每asset优化。作者逐字两段/纯note与R4/R5已核最小命题及边界相符，PRE通过后依root既定窄授权保存。

独立非writer随后实际读以下真实全文、完整两侧与EOF纯note，均与A11一致，POST通过；四窄锁释放，不需再加Books流程标签：

| 材料 | 核验时真实段 | 完整邻接 |
| --- | --- | --- |
| 04304 HierVA | Ch75 206/208 | 200–214 visual artifact→新两段→长视频；EOF note |
| 05092 DriverWM | Ch25 52/54 | 47–61三channel→新两段→support；EOF note |
| 04547 StageAudio | Ch28 130/132 | 124–138 meanCE→新两段→PPL；EOF note |
| 04412 DiLAST | Ch24 283/285 | 278–291风格注入→新两段→对象运输；EOF note |

actual正文未把peakcontext当总费、Table3Δ当GTerror、预定schedule当全feedback或感知偏好当3D真值。当前本reader累计10项新增真实Books链通过，不授六部分DAY/FINAL。

JoyAI-Image04128补恢复的[官方GitHub README News](https://github.com/jd-opensource/JoyAI-Image)实际读到`2026.05.07: Our technical report ... now available on arXiv`，对应链接及文末citation身份为2605.04128。直接官方paper事件日期通过，修复R2先前跨日组合不足，不再把它列无法落窗的date缺口。Apr02weights、Apr10dataset、Apr15OpenSpatial是不同artifact事件，不自动当paper更早正文或本日多家族。A12其余Source仍普通，未预授。

## R9 用户明确暂停：实际层与未核停点

收到用户经root明确暂停指令后立即停止新Source、新owner、PRE及POST；本节只保存暂停前已实际完成的阅读，不为闭环补读。R1–R8已完成的10项新增真实Books独立POST与3项具体已有覆盖（04903/04352/04313）继续有效；没有授六部分DAY或FINAL。所有本reader窄ownership/复核权限现释放，无Books、Report、LS写入。

A12本reader实际阅读停点如下，**不是四项完整必要Source通过**，也不是作者准备文字的独立核验替代：

- **04128 JoyAI-Image**：直接日期已按R8通过；实际精确v1 HTML读到§2.1–2.2的Qwen3VL-8B条件编码/16B MMDiT、§3.1 box-centric/cycle-consistent数据设计及dataset mixture开头；§6.1/Table14与§6.2已实际读。6.1是固定GPT-5 planner/reasoner、695题/5753 DSR与120 RealWorldQA：baseline68.8、Qwen editing67.4、Joy71.7；其他reasoner局部增益1.7–4.4pp不证小模型收益机制或总预算优势。6.2 VGGT点云/pose增密是qualitative，不授真实几何或独立新观测。**尚未完成§3.2/3.3、相关训练/数据对照与Table3反侧的必要核验**；owner差额、逐字PRE、实际POST未开展。
- **04962 TabEmbed**：实际精确v1 HTML读到§2.2尾部的每dataset独立logistic readout/label过滤，retrieval人口与1–3条件/符号真值构造；§3目标列遮蔽、query-to-row contrastive、违反已知条件的positive-aware hard negatives及in-batch negatives；§4训练/评价主要设定、§5.1–5.4结果与反侧。冻结embedding后每数据集训练readout不是zero-shot classifier；numeric最难、multi-condition递减，cosine与logical truth的相关不等精确predicate；PCA/t-SNE或噪声列鲁棒性不证明内部结构attention。**尚未核完Limitations及Appendix B中两位小数序列化、宽表筛选/截断与训练配置细节**，未授完整必要Source/owner/PRE/POST。
- **05031 CAD-CDDM、04613 VocalParse**：暂停前仅取得精确v1 HTML标题/heading/长度，并有先前摘要准入；**尚未实际读A12拟采用机制所需核心正文与对照反侧**。作者A12已有准备，但本reader未独立核验，不提前授Source通过。

上述未完成项均属正常可执行pending，不是外部受阻；04834既有OpenReview具体challenge资格隔离仍按R7，不能借此遮盖普通未读。root另分担的05151/05197/04899不在本reader已读Source集合，不冒认已做第三轮核验。作者后续新拟文、报告新增行/状态及全日来源有界收口尚未在此授终核。恢复时应按当前合同重载本日停点并重新协调共享Books窄权限，不从“已准备”推断已通过。

## R10 用户明确恢复；A12四项必要Source独立补齐

本次按root转交的用户明确恢复授权，只接05-08；重新完整读取AGENTS、当前Research/Report合同、来源使用说明/每日组/arXiv主题、统一Prompt、ROADMAP与LS2026顶部恢复路由；Books对读前重读PROJECT_CONTEXT、LEARNING_PHILOSOPHY与WRITING_GUIDE。2025仍暂停，不启动其他日期。使用daily-research-closure分清准入、必要Source、owner与写后检查；R1–R8十项实际POST及三项具体已有覆盖不重审。以下均重新直接取得精确v1原域HTML并实际阅读指定必要内容，不把作者A12 prepared当独立通过；无实现复现。

- **[04128 JoyAI-Image v1](https://arxiv.org/html/2605.04128v1)**：接R9实际读完§3.2–3.3及Table2/3。full-parameter spatial SFT、varlen独立packed sequence、vision较小LR与仅general-purpose数据加KL是明确训练设定；Table2为FSDP2/BF16、1epoch、batch128、max8192、LR5e-5/vision5e-6及λ10。KL正文同时出现hidden-state representation与response-token layer-average表述，不据此补造可执行logit/hidden实现。Table3空间平均59.1→64.4但MathVista75.0→74.4、OCRB90.3→87.9，不能用“保持基础能力”抹去退化，也无单模块受控消融。结合R9已核§2/3.1/6.1–6.2，A12最小派生视角辅助/非独立观测命题必要Source通过，2+2+2=6；不是生成/编辑全配方核验、总成本优势或真实3D认证。日期沿R8直接官方News，不重开已有效日期层。
- **[04962 TabEmbed v1](https://arxiv.org/html/2605.04962v1)**：接R9实际读完Limitations与AppendixB全部。训练1024token与架构32K支持不混；2epoch/MNRLτ.05/AdamW1e-5/warmup10%/global256、500k retrieval+100k classification、BF16、16×96GB PPU-810E和seed42已披露。每dataset独立logistic readout不是zero-shot classifier；Faiss IndexFlatIP对归一化向量是exact vector search，不是exact predicate evaluation。默认两位小数、Null→unknown、时间格式/bytes解码均改变输入合同，宽表截断风险明确，未含商用API对照。A12 query-row/负例资格与向量排名不保证逻辑真值的最小命题必要Source通过，2+2+2=6；不由二维投影或噪声列实验推内部attention/普遍结构理解。
- **[05031 CAD CDDM v1](https://arxiv.org/html/2605.05031v1)**：实际完整读§III–V、Eq1–17、Alg1/2与TablesII–VII。命令先采样、参数再条件化；coordinate Gaussian、dimension相对核与boolean empirical-prior限定support是不同语义，吸收态另列。DeepCAD178238、90/5/5、60/280长度、8+4blocks/256hidden/100steps、4090单卡100epoch每epoch约15min。TableV mixed并非各指标占优，TableVI global-only invalidity3.02优于combined4.00，TableVII steps非单调；不能复述正文全指标支配。unified参数shift范围256–271与其256-level叙述矛盾，ζ相等mask未清command category/instance；不采用为可执行recipe或严格因果对照。GT-command所谓upper-bound只是经验参考，conditional仅定性，valid CAD/Chamfer不等制造/任意约束正确。A12异构symbol噪声合同的最小命题必要Source通过，2+1+2=5；具体owner/写入未授。
- **[04613 VocalParse v1](https://arxiv.org/html/2605.04613v1)**：实际完整读§3–6、Tables1–3与AppendixC/D。12.5Hz audio、纯歌词prefix→word/note interleaved及单global BPM，已知歌词可省首段；这是输出factorization/预训练分布兼容，不是自由CoT推理或两份歌词hard一致保证。120ksteps/17h、1.7B fullFT/2H100、每卡18000tokens至多64，2000h pseudo+约50h人工。w/o-prefix Opencpop WER7.18对3.79支持局部机制；Qwen3ASR的3.41/5.93/7.83对3.79/5.69/8.16含反退，audio-only pitch .56也不优ROSVOT .38。AMT baseline额外GTlyrics及部分SOFA时戳不可混成audio-only等条件；Mandarin、teacher质量与rubato限制明确。AppD数据量和hyperparameter同变，SingMOS4.56→4.52、CE5.94→5.90负侧须保，STARS独立提取只缓解而非消除全部teacher/evaluator偏差。A12最小输出合同命题必要Source通过，2+1+2=5；不授跨语言/下游质量普遍优势。

四项只完成必要Source层。owner差额、逐字PRE和实际POST须在实际对读后另记；DAY/FINAL与其余普通待办仍未通过，不以这些有限阅读关闭全日。

## R11 A15四项实际owner/PRE；Story/UV日期与具体NC

本reader实际对读A15全部四个逐字单段及每个插入位完整局部：Ch24 1126–1157 workflow/UniT→provisional，516–540离散采样→continuous embedding；Ch23 510–550文本索引声学/TASTE→参考音色；Ch76 324–348单/多向量→late interaction及758–790 query/evidence约束。四个具体差额成立：派生视角辅助理解不等修订终图；异构离散属性前向核不等文本统一categorical posterior；歌词prefix/词音符结构转写不等文本索引声学生成；predicate监督的query-row排序不等检索后对答案约束验收。A15逐字单段PRE通过，分别保持R10限定命题/反侧/费用/退路，不授论文可执行recipe。root协调Ch24/23/76本日单段与本人注窄位后方可实际保存，本节没有提前签POST。

Story04831/UV04704日期层本次独立重新向精确DataCite DOI与当前官方abs逐件核验：两者均`arxiv.content`/`findable`；唯一v1分别May6 12:28:17UTC、09:55:36UTC，registered分别May7 02:02:42.000Z、01:59:36.000Z。EDT日程最早May7 08BJT至各自10:02:42/09:59:36BJT，全区间同日、先后合法，与A13原字段一致。只限定arXiv announcement，不是全球首次公开；UV v2 May7提交是另事件，未拿它替换v1。必要Source采用范围仍沿R2/R3，不重旧附件。

实际对读后，以下两项最小长期命题可作**已有覆盖**，不因已覆盖降分或改成贡献排除；源文具体实验仍留报告：

- **Story04831 → PLATFORM-EVALUATION-SYSTEM**：Ch66 466–474已经分high-contrast、near-equal self-PIR/Null-PIR，明确答案来源/judge身份与质量proxy/候选生成方式混杂；506–508另分用户/judge评价轴、条件人口与独立人工anchor。这承载可采用的按来源/人口与质量分责，不声称所有story RM或human–LLM子集的具体结果已逐条进书；也不把human=chosen构造升级普遍人类优越/自偏好因果。2+1+2=5。
- **DoG04458 → PLATFORM-EVALUATION-SYSTEM**：Ch66 1674–1698先构建inventory再对support/coverage/排除、保存source revision/extractor与人工校准/Unknown，并隔离自建分母；2746–2751按依赖子图定义verification unit、分相关性/支持/回答量/normalizer；1541区分generator/reader与外部效标，526–528及946–948区分rank agreement/参照人口与客观真值。合起来承载本次最小reference/rank/population分责；不声称已逐算法覆盖QA clustering/SVM/top20，不把12-priority-run叫严格top-only或auto alignment叫fullymanual。2+2+2=6。

UV04704拟Ch78 140–152编译/模拟/真实trace后还有具体输入/执行对象差额：保依赖slice只为proposal降低输入、仍回原DUT验证，不是仅编译成功或一般GUI压缩；建议152真实Rust段后/Tool Discovery标题前一短段，待作者逐字稿/PRE。Junk05116拟Ch72也有窄差额：791虽已保PPL/择优预算，3129–3135保selected attacker与机会集，但没有明确无指令非语义token也可触发harm、行为不证明训练后门来源；待最小非recipe逐字稿。两者尚无新Books实际保存或POST。

## R12 Seed有界API范围核验；计数纠正

实际直接取Seed官方`/api/get_article_list_v2`三精确响应：Publication `article_type=1/publish_year=2026/page_token=0,count=20,order_desc=true`附`x-tt-locale:US`，以及同参数offset20；Blog `article_type=2`、offset0、不附locale。Publication0实际`sub_article_list`为**18**（不是请求上限20），`total86/next20/has_more=true`；Publication20实际20，`total86/next40/has_more=true`。Blog0实际**12**（不是20），`total24/next20/has_more=true`，已提醒作者纠正A14/正式报告。不同locale结果不拼接为同一返回数量。

两Publication响应日期序列分别09-28～05-26、05-16～04-15，目标日May07仅1631 TDDFT Gradients/2605.06489与1629 Continuous Latent Diffusion/2605.06548；前者标题明确AI for Science排除，无需追日期或全文，后者已在冻结baseline候选行183及证据标题377同identity/v1，按用户要求去重且不迁旧日期。邻接1667 May10、1587 May06、1639 May04均相符。Blog12个实际可见项跨10-14～02-13，June23之后跳April23/April09，无May07可见项；不把跳过的后台槽位冒称已读条目。三响应实际跨过目标日，可在该有限目录/locale范围停止，不翻更早历史；不授全站收尽、全球首次公开或零遗漏，日期毫秒只作目录定位，不改名实际论文公告时刻。本节只核当前API与已存在家族，不重扫旧184/619。

## R13 A15四单段真实写后通过

root明确协调三文件四指定锚点窄写，作者实际保存/self-read后，本reader非writer实际读取每段完整新增、完整直接两侧和纯证据末注，并回对R10原证与R11逐字PRE。四单段与A15一致，POST通过：

| 材料 | 实际正文/末注 | 已读完整局部 |
| --- | --- | --- |
| CAD05031 | Ch24 530 / 2333 | 522–540，离散迁移两段→新核身份→continuous embedding两段 |
| Joy04128 | Ch24 1149 / 2331 | 1140–1162，UniT修订/预算→派生视角→provisional/commit及后续 |
| Vocal04613 | Ch23 532 / 1793 | 522–545，TADA/TASTE→新转写接口→reference时间轴 |
| Tab04962 | Ch76 339 / 1472 | 330–350，单/多向量→query-row→late interaction/span及后续 |

四纯note只留精确来源/必要位置/边界，不加流程标签；相邻他人段与已有有效负侧仍保留。限定三路径unstaged/cached `git diff --check`均exit0；不是全仓或研究语义替代。四窄位可释放，本日累计14项新增真实Books链通过；仍未授DAY/FINAL，UV/Junk/新具名线索与六部分收口均不由本节预签。

## R14 最后具名必要域与A17实际POST

**NRI04916**本reader实际独立原域读精确v1 §3–6/AppA–D，准入与必要Source通过，2+1+2=5。predicate-specific权重→literal统计/例子support/parallel clause slots→任务接口与规则正确性分验是具体结构增量，不因UCI小模型排除。18统计不是充分统计；aux固定raw输入维度扩展随机新权重，不能承诺schema/置换不变。训练支持N6–12/M24–48、K≤6/L≤4、3spurious/8slots/dropout.25、8192batch/500steps；有限合成反例中prediction85–100%仍可只24%logical match。Table1 mean69.7对EBM82.7与Table2 full74.8口径未闭，不拼总体优势；counterfactual flip只约束已选rule敏感性，不自动识别真实因果，AppA对两环境边际独立的式子也不证明任意现实spurious。未披露性能hardware/precision不代填，不采用普遍推理加速。精确DataCite为arxiv.content/findable、registered May7 02:04:48.000Z，官方唯一v1 May6 13:45:31UTC，日程最早May7 08BJT至最晚10:04:48BJT同日；v2另事件不替v1。

实际对读Ch5 88–104的primitive/codebook+executor→task embedding，A19最小单段填补literal统计+例子support的输入接口差额，逐字PRE通过；root授该段与本人注，写后另外实际检查才计整合。

**SLYP05000排除必要安全域**：实际原域精确v1完整§4/相关§6.1/6.3–6.5及§7，标准ReAct、外部checkpoint/索引memory、stop-time verifier、COM metadata/调用导航与compile-debug/crash evidence均是具体领域组合；对既有scaffold补工具的局部成绩未给新增通用可靠性条件。排除是尚无改变本项目设计的额外机制/边界，而非没benchmark/没generalization或只看应用标题；不评分/Books，不独核28漏洞/MSRC真实性、不执行PoC。best-of3 discovery与单次per-case PoC、20COM/40case及GT已给报告人口不能混，现v2不改当时v1数字。

**Qwen May07复盘**：实际官方完整core、Important Fixes至Other Changes。对有具体correctness信号的[PR3525](https://github.com/QwenLM/qwen-code/pull/3525)和[PR3550](https://github.com/QwenLM/qwen-code/pull/3550)额外读官方PR正文/精确pipeline差额：共享singleton parser的reset使并行stream缓冲互相污染，前者移至per-stream context，后者移除共享model/modalities等request字段。这不是“fix标签无意义”；但两个PRcreated/merged实际Apr22及Apr23–24，已是窗前公开事件，不能把May07 recap改名新纠错。未运行tests、不核全部无关PR；May07其余面板/rewind/review/cache版本说明无新的长期机制依据，可关闭，不授全产品安全/速度。

**Voice与FT**：实际[Voice May07官方](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/)三模型功能/effort/工具/128K至Safety/Pricing，缺新架构/训练/streaming计算机制及可归因预算对照，C通过；active classifier可中止部分session只是厂商能力说明，不是安全完整保证。实际[FT通知](https://developers.openai.com/api/docs/deprecations#update-to-openais-self-serve-fine-tuning)May07新org训练job资格、July02近60日推理条件与Jan06后续计划，以及existing model inference until base deprecated：2+1+1=4的兼容性变化必要原件/直接日期/仅报告通过。Book训练原理未变，不将计划冒已发生或将全部微调立即停用。

A16三root必要Source仅复用root已读限定层，本reader没有冒认重复核完三源；实际另对读Ch5 214–242/348–378/272–274支持05151/05197两项具体NC及04899仅报告，边界按A16，不为它们新增书稿。

A17 UV/Junk实际原文/owner/PRE层沿R2/R3/R6/R11，本次逐字单段与完整邻接PRE后，root授窄写，作者真实保存。本reader非writer随后实际读回：UV Ch78 154及838本人注、146–166完整两侧；Junk Ch72 793及3440本人注、785–807完整两侧。两真实段与A17逐字相符，coverage/IR费用、trajectory择优/PPL非训练因果均近正文，纯note准确；两文件限定cached/unstaged diff-check通过。两项实际POST通过、窄位可释放，累计16项真实新增Books链；NRI未由此提前签POST，DAY/FINAL仍未授。

## R15 NRI真实单段写后；17项新增整合已落实

收到作者真实保存通知后，本reader非writer实际读Ch5 90–110完整局部与631本人纯note：新98单段逐字为A19，前接primitive/codebook/executor、后接task embedding两阶段与规则训练边界；没有覆盖相邻来源或把NRI变成通用因果/transfer保证。统计/例子support/parallel rule生成、aux随机扩维非不变、prediction与logical match分账及完整费用/退路均保留，note只含精确来源/必要域/限定命题，未签实现复现。该路径cached/unstaged diff-check均exit0，实际POST通过，Ch5该指定窄位可释放；本日累计17项真实新增Books链。完整六节、有限来源/外部隔离与旧块保存仍须实际DAY检查，不能从17项POST自动得日级完成。

## R16 有界补检新具名校准：JASTIN/MSEB与04566纠偏

本次只接作者本日有限补检中新具名的三项，不将233重复命中/219身份变成全文队列；原已核26项处置不倒退重审，新分母仍未冻结。

- **[04505 JASTIN v1](https://arxiv.org/html/2605.04505v1)**：实际独立完整题摘、§3/4/7、§5.1/§6.3–6.4与TablesIII–VIII。准入及最小必要Source通过，2+1+2=5：固定任务score-head→rubric特定监督/多刻度及paraphrase→区分读instruction与记task-id，TableV模板alone失效而模板+paraphrase恢复是局部成立条件，不以多源/更高相关性本身入选。PEAF冻结+adapter/Llama3B是此实现，不授任意encoder/LLM替换；24k人工/80k伪标/43.5kproxy、8A100/6000steps/约24h、batch384与AES SpeechPQ validation早停已披露。D1 testprompt seen而D2/3 unseen，不宣称独立控制的全部语义因果；比例rescale和`Smax−S`不自动保量表端点/语义。TableIV移除proxy有指标更好，noise长/重排prompt退化、ASMR与speed弱，相关性不能签逐样本正确或通用audiojudge。未采灾难遗忘/attention-cost的因果解释，未核实现或全部像素。官方abs唯一v1 May6 05:18:42UTC与DataCite arxiv.content/findable/registeredMay7 01:54:49.000Z实际独核，同May7 08～09:54:49BJT组合通过。
- **[04556 MSEB v1](https://arxiv.org/html/2605.04556v1)**：实际完整题摘、§3/4/6及§5.7–5.8/Tables6–9。2+1+2=5，准入及最小必要Source通过：audio-native/cascade/GTtext信息接口不同，微小modality gap可来自双侧低分；同WER不同ASR在retrieval仍不同，是指标代理不能替下游判据的具体反证，不因新benchmark名称入选。初始Gemini embedding候选由ASR文本或GTtext获得，LLM只是动态k候选reranker，不能叫音频端到端独立检索；GTtext不是任意模型真正数学上界。locale/noise反退、有限GmeanF1、固定prompt被Gemini迭代过、suspected contamination仅假设均保。价格按假定query/token估算、retrieval还忽略audio token，不授完整成本/latency/SLO。论文所写厂商参数/架构不从二手描述升级为已证；未核全部实现/复现。abs唯一v1 May6 06:58:45UTC与arxiv.content/findable/registeredMay7 01:56:05.000Z实际独核，同May7 08～09:56:05BJT组合通过。
- **[04566 zero-shot editors v1](https://arxiv.org/html/2605.04566v1)**：作者拟C后，本reader实际读完整§3.1–3.5/§4.4–4.5发现共同错误理由“只新增三editor任务成绩”漏掉具体测量边界，要求只重开此项。depth逐图GT affine、normal在5样本从48轴约定选校准、segmentation oracle-present-classlist，以及instance因输出难解码不量化，均使无参数微调不等无监督侧信息；内容能力与RGB输出/decoder合规混合也限制解释。可窄P5，非泛称编辑器能力突破；仍待§4设定/必要Table反侧、日期及具体owner，不把此层校准提前叫完整Source/Books。

其余六个新具名普通core由作者准备、本reader逐项接独核；新未读不改外部隔离，跨日资格也不按registered单点授May7。DAY/FINAL仍未发生。

## R17 新具名必要core、独立日期与A22实际PRE

只继续有限新具名，不扩大219身份为全文队列。以下均本reader直接读取原域精确v1，未以作者A21作为替代，未核代码、像素、运行或复现：

- **[Gyan04759](https://arxiv.org/html/2605.04759v1)**：实际§2–4、AppendixA/C完整pipeline（含C1.2/3）及§5/7。RST/AMR/ontology/rule-NLP→GMR、独立KS及检索组合有具体描述，但未披露足以改变长期编码/推断设计的新规则或受控证据；闭贡献C成立，不是因proprietary、医学或不开源。无hallucination、可逆、completecomposition/worldmodel/negligiblecompute均不采；有限MSMarco、20-query与KB变化不替固定workload成本/机制证据。无评分/Books，不为排除追日期。
- **[EBM-RL04733](https://arxiv.org/html/2605.04733v1)**：实际§4/Eq1–13、§5.1/5.3–5.5/Tables1–5、§3.2/AppH/K/M，2+1+2=5必要Source通过。PCG为冻结reference对同一GT next utterance有/无perception+think前缀的mean-token loglik差，不是真实grounding或独立因果；CLIP/BERTScore/format/PCG分别在同prompt group归一再加权。2.3k Gemini冷启SFT近3epoch再Qwen2.5VL7B/8H800 RL1epoch；movie/session划分不排尽预训/台词捷径。TopK缓存N未披露、Max若干指标更强、权重有tradeoff。GPT5-mini judge所给reference/chat/profile不等独立video验真；四系统均分的人评相关不授逐item校准，OOD只有限QA。额外reference、warmup、rollout和更多tokens全计费。
- **[Strat04906](https://arxiv.org/html/2605.04906v1)**：实际§4/Eq4–10、§5/Tables1–2/AppC/E，2+2+2=6必要Source通过。CTDE取对手自述与主轨迹相邻行动，M2仅重采当前reasoning/action、不为每个候选继续未来，故统一对主轨迹未来的微评分不是反事实action value。微组zscore加role-batch中心化return、ω.2不证明同人口无偏/减方差；std零guard未闭不补recipe，同源baseLM judge不是真实心理oracle。Qwen3-4B/LoRA16/alpha32/.05/BF16/2A800、0.3–.7GPUh/globalstep、MiniHanabi约100wallh且rollout50–60%；有限>500games及角色/先后手反退不概括全胜。
- **[Composer04609](https://arxiv.org/html/2605.04609v1)**：实际完整§3–5/Eq1–7/Tables1–5，2+1+2=5必要Source通过。Lab大核局部差与模糊SLIC色块只是抑制细语义，不严格semantic-free；两condition encoders、互调与共享主干保重权入口。Dual cycle更好，Union部分quality/步吞吐更好；FID11.04不优finetunedSD9.88、ImageReward1.09不优RPG1.12，35360votes/24prompts不证明人口普适。2M混合制备、SD1.5与XL不同训练产物/分辨率、50DDIM均分账；7.7秒含3.1planning但hardware未披露，不是SLO。CLIP候选→LVLM挑选与另训text-only规划不是一个免费路径。
- **[Contact04662](https://arxiv.org/html/2605.04662v1)**：实际完整§3–4/Eq1–12/Tables1–3，2+1+2=5必要Source通过。54关节手指合并23contact、四part codebooks jointdecoder；在量化前连续motion/relative/contact latent共同去噪，leader/music条件后量化解码。自预测contact再guidance不成为GT外部约束；Eq9 epsilon/score符号/尺度混写不照录recipe。DD1003.24h/五对dancers/random80–20不是跨人独立验收，hardware/总费未披露；w/oGuidance FIDcd3.41优full8.01、fullFIDk8.89劣7.45、Separate leaderMPJVE12.65优full13.27，25人×10动画也不授真实物理。codec、音乐、采样、解码梯度修正全付费。
- **[PhysForge05163](https://arxiv.org/html/2605.05163v1)**：实际完整§3–4/Tables1–4，2+1+2=5必要Source通过。PhysDB150k无全量精确axes，另用PartNet/InfiniteMobility关节GT；planner输出6×64bins的bbox专用token/层级/type，8D origin3/axis3/limits2经独立两层MLP进入几何middleTransformer，共同CFM与10×kinloss，type是阶段接口不是精确参数文本。200/1000/1000/340对象人口、GTmask/partcount特权分开；无maskbbox32.30→36.32仍不及mask42.95。textCLIP/标签MAE、axis/pivot与RoboTwin示例不认证真实质量、材质/动力学或robotSR；Table4五类subset与all不拼。硬件/总预算未披露不补；planner/编码/标注与联合采样费保留。

**04566 Source补齐**：接R16实际读§4全部、Tables2–4及Conclusion/Limitations；40steps/CFG4和LongCat50/5、固定seed、NYU654/DIODE771+446/Cityscapes500等是披露范围，不授hardware/总费。depth经逐图GT affine只测相对几何，不能与VisionBanana rawmetric直接比；normal的mean/median排序也不一致，segmentation用GT-present类只测mask/palette非openclass发现。7类与19类还改变prompt/人口，不纯由粒度造成增益。准入与必要Source 2+1+2=5通过；不读美图当真实geometry。

本次六P的官方abs精确v1与DataCite逐件实际核，均arxiv.content/findable；(UTCv1,registeredZ)依次04566=(May6 07:11:50,May7 01:56:19)、04733=(10:32:23,02:00:19)、04906=(13:35:14,02:04:34)、04609=(07:56:16,01:57:20)、04662=(09:10:07,01:58:36)、05163=(17:33:23,02:10:46)。EDT日程最早May7 08BJT至各registered最晚均仍May7，同日组合有效；当前04733/04906后续v2/v3不替精确v1，不授全球最早。跨日晚登记另项仍须单独资格，不由此层代理。

**具体owner/逐字PRE**：实际再读Ch33 117–139（speech/text两完整段→多mode）、330–368和2047–2070；Ch24 246–264、286–302的完整直接两侧；A22四原拟文全部实际读。Strat在speech/text之后、多mode之前；Composer在stylecap两段之后、DiLAST之前；Phys/Contact按序在rigidparts2505-00426之后、trainingcollision2605-00517之前，各一段与本人纯note的PRE通过，等待root窄授才写，不预签POST。现有group与likelihood人口/特权/NLL非grounding已足够承载EBM最小命题，具体NC5通过，不称已含电影配方。Ch66实际480–502、1534–1548对JASTIN的prompt/scale与generator×reader×domain/外部校准已足够，具体NC5通过，不因覆盖降分。

MSEB实际Ch23 1365–1384已有WER≠MRR及GTtranscript仅级联headroom；但尚缺native/cascade/GT的信息权限与低modalitygap可来自双低，建议在S2R完整两段后、representationcollision前仅补该差额。04566实际Ch23 403–435已有RGBparser与格式/metric分责，但无逐图GT、轴校准、oracle类的无FT≠无侧监督边界，建议VisionBanana完整两段后、连续表示标题前仅补该差额，待作者逐字稿/root窄位，不由必要Source层自动签Books。

Qwen安全反证另实际读官方[PR3615](https://github.com/QwenLM/qwen-code/pull/3615)正文及LspServerManager差额：允许绝对executable path，relative仍防逃逸，requestUserConsent改workspaceTrust且可auto-trust，不是独立consent保证；createdApr25/mergedApr30，May07recap不能改名当日新纠错。只核此必要反侧，未跑test/核全产品。

DAY/FINAL仍未授；新具名普通owner/PRE/POST与六节收口继续正常推进，不挪外部隔离。

## R18 A22四项真实POST；新增21项Books链

root已授四指定单段/本人注窄位，作者实际保存并self-read后，本reader非writer实际回读完整新增、完整直接两侧与本人纯note：Strat Ch33正文139、130–150完整speech/text→新段→多mode/后续，末注2826；Phys/Contact Ch24正文264/266、258–274完整rigidparts→两新段→trainingcollision/后续，末注2354/2356；Composer Ch24正文296、288–304完整stylecap两段→新段→DiLAST两段及后续，末注2352。均逐字为A22已过PRE，费用、退路及特权/非反事实、jointtype/连续参数、contact自产、条件语义未独立等限定近正文保留，纯note不冒实现复现或流程完整标签。两文件cached/unstaged diff-check均exit0，四实际POST通过，窄位可释放；累计21项真实新增Books链，不自动授DAY/FINAL。

## R19 三额外具名排除校准：仅重开受影响两项

作者另具名拟C的08209/08217/05253，本reader实际逐官方abs完整题摘，并读取以下必要正文；不是扩扫其余raw，不因source投入保P，也不拿已有覆盖降为C。

- **[08217 time-series retrieval v1](https://arxiv.org/html/2605.08217v1)**：必要设计反证核实际§3–5/AppB/D/G/H/I。另有ETTh2/Exchange，不能写仅ETTh1；但旧RAFT top5 cosine、不同容量/1seed/earlystop，基础模型只336/720 zero-shot而非长窗受控因果。100epoch+cosine把PatchTST3000 MSE .647降.426，短窗.395，原68%退化收至约8%，不能宣称更长context必然噪声崩溃。AppG exp(entropy)有效rank写8.3→0.1与正entropy不相容，attention熵也不识别噪声因果；局部训练时间不含全部retrieval/预训。C可成立为未提供新的可迁移机制或可信成立边界，不因非LLM、小实验或负结果关闭；不将其推基础模型/所有时间序列inverse-scaling law。无评分/Books。
- **[05253 EnterpriseRAG v1](https://arxiv.org/html/2605.05253v1)**：实际§4/5/7。原拟仅新合成corpus的C理由漏掉具体测量身份：fixed-release leaderboard与pairwise candidate-union纠gold不同；required/valid/invalid、gold-biased tie、单次符合旧gold即可shortcircuit以及改required后重生成answerfacts，是可改变评价设计的具体增量。要求仅此项重开P5，尚待必要§6反侧、精确日期和具体owner；不因500k/九种source本身准入，亦不把judges自洽授真值/穷尽gold。正文称初期改过题全丢后抽样，与后续versioned修正及pairwise流程分别保留，不能混成随时在线改leaderboard。
- **[08209 LSAMD v1](https://arxiv.org/html/2605.08209v1)**：实际完整Methodology/Experiments/Tables1–4及AppC。frozenbase与dataset-specific clone/DAD、batchmajority路径→跨dataset base使用频率选初始化层→保序邻接扩层有具体参数复用选择接口，不可仅按NAS/learngene组合关闭，要求仅重开资格/P5校准。频率不是通用性证明；12vs10/τ6正文不一致、gate未披露随机乘子、硬路径训练梯度未闭，不补recipe；Table2随深度非单调，Table4六层DTD middle55.37优last54.84，pretrain-finetune不是数学upperbound。只存learngene对存全部产物、epoch数跨大小不等完整成本，初始化后仍需训练。给作者消息一度错将Table1两组Pets数当反退，已立即明确撤回：8层SWS80.25对LS80.90、7层81.09对81.34都非反退，本节只采用真实Table2/4反侧。082xx晚登记资格须有限直接公告恢复，不以潜力先授May07或把普通恢复改external。

两项重开已通知作者/root；05253必要Source与owner、08209资格及五晚登记资格仍普通执行中，不授六节DAY/FINAL。

## R20 05253必要Source补齐；两重开项实际资格仍跨日

接R19实际读05253精确v1 §6全部、Tables6–7与五规模设置，准入及最小必要Source为2+1+2=5通过。三baseline同GPT5.4 generation/evaluation不等独立真值，BM25/vector固定top10与bash可变文档/每题至10min预算不同；Bash completeness较好但correctness/recall较低，highlevel仅10题、infonotfound100%不签未知现实缺失；大corpus近邻cosine升/Recall@10降也不识别单一原因。hardware/总制备和API预算未披露不补。只采用correction状态/测量身份设计，不把新九source/511962篇/500题或正文关于embedding域失配的猜测当机制因果。

独立重取两重开项官方abs submission history及DataCite精确DOI：05253 v1 May5 20:23:38UTC、registered May8 02:05:53.000Z，08209 v1 May6 09:13:29UTC、registered May12 03:43:56.000Z，均arxiv.content/findable。两者最早May7 08BJT到最晚registered跨日，尚不能授当日，05253 v2 May19是独立后续事件不替v1。已精确请求作者在既有晚登记有限原始/作者入口恢复中仅加两家族，必要Source通过不代理日期，也不因05253有新评分接口先写Books；尚未授external终态。

## R21 A23实际PRE与两项真实POST；23项新增Books链

实际再读Ch23 VisionBanana完整两段→连续表示入口、S2R完整两段→Representationcollision，与A23两逐字单段及拟注对比：04566只补无FT≠无GT校准/类别侧信息，MSEB只补native/cascade/GT信息权限及小gap双低，不重复旧RGB/WER论点，PRE通过。root随即授该两单段/本人注精确窄位；作者实际保存/self-read后，本reader非writer实际读回editor正文425、418–438完整局部及本人2505，MSEB正文1386、1376–1398完整局部及本人2503。均逐字符合A23，直接两侧完整保留，纯note没有冒实现复现；本路径cached/unstaged diff-check均exit0。两个实际POST通过，窄位释放，累计23项真实新增Books链；仍须正式六节/晚登记资格有界停止及实际DAY/FINAL，不由此预签。

## R22 七跨日资格的有界停止核验与一处恢复

实际读作者A24全部七项原始URL/替代/停止记录，独立重取七项官方abs完整题摘和submission history、精确DOI的arxiv.content/findable及registered（R20已记两项）；05285/08200/08201/08215/08218原UTC字段分别(May6 17:38:13,May8 02:06:39)、(May5 22:27:05,May12 03:43:42)、(May5 22:50:43,May12 03:43:43)、(May6 11:21:25,May12 03:44:05)、(May6 13:21:24,May12 03:44:09)。全部最早May7 08BJT到最晚跨日，不能截取May07、按registered迁日或称零命中；本层只是资格，不授五项core必要Source/PRE。

另实际打开[VRP官方仓](https://github.com/itsloganmann/VLM-Reliability-Probe)完整README及[T3VF官方仓](https://github.com/sangwu99/T3VF)当前README：前者明确区分VisualsLie ICLR稿与WhereReliability ICML稿，相关稿不自动同事件；后者当前有arXiv链接，但无可直接归May07的历史paper公告。实际OpenReview fyDhQ2dKdw forum仍challenge，cs.LG May列表仍失败，不绕过验证、不外推全站失败；作者A24另有限历史/API/搜索实际结果按其记录范围复用，本reader没有冒认重复执行全部检索或阅读全文/代码。

**05253原件恢复**：直接GitHub API实际读commit137dd5146925febeeecbd1d370fd73339ad33eeb元信息与README patch、真实新增PDF路径，author/committer均May05 08:58:18Z且声明paper available；timestamp不是public-visibility证明。通过urllib实际恢复[历史MD](https://raw.githubusercontent.com/onyx-dot-app/EnterpriseRAG-Bench/48ca3a9c6c2b9e07abdbae16ad0e3b314d2dc21a/paper_draft.md)标题/完整摘要及GoldSetCorrection、ComparativeEvaluation完整两节与baseline表：同题且本次最小参照更新贡献已存在；不能继续写必要正文完全不可得、无同题比较或假定另稿。作者此前web/curl失败只属于其访问路径，已精确纠正并交其同步A24。没有核历史PDF全部内容、仓库初次公开日、发布可见性或实现。

七对象当前已作具名有界原始/作者替代（A24），经上述独立校准后，未恢复目标日正文公开依据的资格可以明确隔离，不必穷尽假想渠道。终态应只保日期/可能更早稿资格缺口，非否定已有最小Source或一律贡献C；不评分、不纳May07确定候选、不写Books、不支持无遗漏；恢复需exact-v1官方日告、带日期作者正文release或确定版本与公开日期的原始档案，只重开对应家族，不迁旧日。05253须同步实际恢复事实后再授报告DAY；完整六节尚未读，仍未DAY/FINAL。

## R23 完整六节实际DAY通过；仅待保存完成态FINAL

本reader非Report/Books writer，实际读修前完整六节的新负责范围：header/§1、完整当前§2每日与已触发OpenReview/补检行、34新增候选整行、历史连续§4前后分界及全部34新增证据、完整§5/§6；旧184及原证据只复用未变有效层，不无差别重读旧池。对比唯一SUP A20–25和R1–22，全部确定新家族的日期/准入/必要Source与23真实POST、9具体NC、2Only报告均逐一对应；root分担三必要原证明确分权，未冒称本reader独读。25深入/9标准是真实采用接口/安全/兼容性层，不改评分或旧最低路线。

实际发现候选旧184与新增NLA之间空行会拆Markdown表，精确要求作者删空行；作者仅删此行并纠Story/DoG的SUP标签后，本reader实际再读完整连接点与两标签对应段，单一连续候选表及最小主张保留。六节实核结论：

- 当前来源范围/实际分页与停止符合主题边界。四API query149/42/18/24合233重复命中/219唯一线索，不是全文队列或219已入选；Seed18/20/12实际数纠正，14每日与OpenReview实际触发行保留，不将空页/年份筛选授完整历史覆盖。
- 全部拟入选及CoT/Junk/FT/Qwen具名修复/SLYP/05151/editor/08217等安全、纠错与设计反证必要域按前节实际范围核；其余明确排除按来源/主题/理由分层抽核，R2具名11样本与后续Gyan等已明示，未核范围不冒全量。Story/UV、JASTIN/MSEB/editor、05253/08209等定点假阴性均被准确重开，不扩大全池；后两没有贡献关闭而是资格隔离。
- 九具名资格（七晚登记＋ALL-IN/DEMM）及六历史来源段现精确列缺失、必要性、替代与重开位置，05253已同步历史同题MD/最小贡献实际可读，不称正文全缺。它们不进入当日确定候选/Books/无遗漏，也不自动迁registered日；有限原始入口恢复已作，当前无尚未执行的普通Source/Books差额，保留项可按当前合同结束本窗。
- 23项新书稿已真实写入canonical owner并经完整新增/直接两侧/本人纯注非writer POST；9NC均为具体正文承载，不以主题相似签，2Only不硬造recipe。费用、负侧、旧分支及未核实现/复现边界一致，没有新结构候选/共享写锁遗留。

本reader独立运行机械核：218行=218唯一候选URL=218唯一§4题目URL，集合相等；218=131整合+85已有覆盖+2仅报告，34新=23+9+2；34全部May07，25深入+9标准。旧184每整行exact、原window exact、**完整144041字符原§4连续保留**，不迁旧日期/评分。421本地引用0缺失。V3修前与修后均exit0，仅结构/一致性，不替语义。README cached/unstaged diff-check均exit0；两新SUP以no-index --check实际核0空白问题（exit1是新文件有diff，非验证失败），不拿空的两层Git检查证明未跟踪文件内容。全仓既有修改未动，无stage/commit/push。

**DAY结论：通过。** 只覆盖本次补窗及上述明示复用/隔离；不授全站全学科召回、实验复现、内部服务/物理/安全保证。作者现在可仅行政同步状态/阶段、§1最后待办、§5普通待办与§6已发生DAY事实；本reader须实际读取该保存完成态及必要机械核后，才另外授FINAL，不先签完成态已读。

## R24 保存完成态实际FINAL通过；单表检查范围纠正

作者通知17:34:42完成态真实保存后，本reader实际读回header/§1最后待办、§5全部普通0与终态隔离、§6完整复核行政说明；状态完成、已发生R23 DAY与外部保留禁止用途/定点重开一致，没有将未核资格改成采用，也没有预签实验/全站Coverage。行政格式失败后补“终态保留项”和literal“结论：通过”仅适配机器接口，不改变研究判断。

**检查范围纠正**：R23“单一连续候选表”措辞当时只实际核过旧/新连接点，尚未以全表连续性程序支持；作者随后发现原184内部另五行间空行，故不能把当时局部连接核冒作全表格式通过。作者只删五空行，本reader本次独立按baseline逐五对实际核：TaskAwareAudio→DecisionAwareUser、BlackBoxConfidence→AnnotatorSafety、EntropyCliff→NonsenseHelps、MultimodalDG→XL-SafetyBench、TracePriorRL→AdaGATE，均两完整候选行直接相接且原行不改；全表真实连续candidate blocks为`[218]`。此修复只影响Markdown呈现，不重新开启已有效Source/Books层。

完成态独立复算再次通过：旧184同序逐整行exact、原window exact、完整144041字符旧§4连续；218唯一候选URL/218唯一§4题目URL集合相等；总131I/85NC/2Only，新23I/9NC/2Only及25deep/9standard；421本地引用0缺失。完成态V3 exit0、README cached/unstaged diff-check exit0；两未跟踪SUP no-index --check无空白问题（exit1仅新增差额存在）。本reader只写此review文件，当前本日报是unstaged修改、两SUP为untracked；无stage/commit/push或其他日期/索引写入。

**FINAL结论：通过。** 仅指2026-05-08本次May07自然日补遗漏的已保存报告与明示复用/隔离范围，本日可执行研究/必要书稿/完整六节与保存完成态实际非作者验收均完成；九资格与历史来源终态保留继续禁用于确定候选/Books/无遗漏。root可按R23/R24接纳，不必第三遍无差别重读23条有效原证/Books；任何新原件只定点重开受影响对象。
