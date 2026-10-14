# 04-03 五项必要尾证与负侧分层校准

复核者：`apr03_tail_finish`，非报告作者、非 Books writer。范围仅本日报补窗 2026-04-02，用户恢复后的 92/279 cursor；旧暂停不再阻止本日尾项，旧62/31真实POST等有效层不重做。已加载当前AGENTS/研究与Report合同/每日来源与arXiv主题路由/Prompt/ROADMAP/LS最新/ADMISSION最小路由。只写本文件，不授日级验收、不写Books、不stage/commit/push。作者packet是路由，下面新核内容实际直接打开官方 exact-v1 HTML；已有效正文层注明复用，非全篇读过或实验复现。

## 已完成的必要 Source

### 00923 CogSym：原 2+2+2=6，窄 Source 通过

新实际读 [v1 Methodology](https://arxiv.org/html/2604.00923v1)：Experimental Setup / Training Details及必要Datasets。`k`只计Transformer blocks，不计embedding/head；细项front加embedding、rear加LM head、CogSym同时加两者。因此8/32不能换成25%全部参数或75%端到端成本减少，same-k也非匹配总可训练参数。Llama2-7B/GoogleTranslate Alpaca52K/1epoch/seed42/AdamW8bit/batch16/bf16/LoRA128均原文有据。已有效Results/Sequential/Limitations与完整题摘复用，保sequential反退、选择器费用和脑区类比非因果；这里只补缺层，不重核全部结果。

### 00938 WARP：原 2+2+2=6，受影响保证深入 Source 通过

新实际读 [v1 Appendix A / Algorithm 1](https://arxiv.org/html/2604.00938v1#A1)：每轮截断SVD、构建系数、QP、更新W，然后仅以全部repair的真实gap≥γs决定break；没有remain真实margin停止门，T耗尽仍return最终W。因此repair保证只绑定成功停止，不把任意返回视为通过。原有效§3.2–3.5/4.1–4.5/B.1–B.3复用，保remain一阶近似与798/800、786/800反侧，representation L2 ball非token输入、Eq12 gap常数缺 competing-row 处理，不自行补定理或否掉所有radius。算法尾证不构成实现核验。

### 01170 ORCA：原 2+3+2=7，窄 Source 通过

新实际读 [v1 Appendix C.1 / Table 5](https://arxiv.org/html/2604.01170v1#A3.SS1)：no-QK full .475/.110对same-architecture standard .239/.095；QK full .414/.103对standard .394/.108；随机online .254/.099。标准行同时更换训练与取消online更新，缺少固定meta初始化而仅去online的对照，故只支持meta+online组合的局部增益，不宣判二者各自独立必要。已有效§3.2–3.4/4/Tables2–4/A/B复用；保score-before-update/reset、LTT校准完整随机算法、iid/fixed outer/同effective policy、无gold/pseudo0非truth、累计首次正确标签、λ0未定义与OOD超δ/全费用限制。不授on-policy实验已成立或任意shift风险保证。

### 00519 LGD：纠正作者拟EX，窄准入 2+1+2=5 / 标准 Source 通过

新实际读 [v1](https://arxiv.org/html/2604.00519v1)完整题摘、§4.1–4.4/5.2–5.4/A.5–A.6/Table7。成熟loss difference、diffusion guidance、repulsion和Top1不单独计新机制；实际增量是把固定一次性合成改为逐阶段读取当前learner与full-data reference的loss差，再生成/选取下一increment，改变target checkpoint及刷新生命周期。只能作为局部状态依赖合成/选择分支，不因CNN或已有模块组合排除。跨increment分类准确率与loss spike只是诊断，不能认证“信息重叠”；reference信心非语义真值，JS口径未核不采用。ImageNette/Woof/Net、有限CNN/Table7组件对照不证明唯一因果或普遍LLM收益；每阶段learner训练、reference、κ候选与生成全费，κ3有反退。Books owner/PRE另待，未预支Integration。

### 01152 Brainstacks：纠正作者拟EX，2+2+2=6 / 设计反证受影响内容深入 Source 通过

先实际比Ch30现有正文：有限nullspace保护≠整网输出、冻结旧block≠组合旧任务函数、冻结adapter不阻止新router抢旧任务。随后新实际核 [v1](https://arxiv.org/html/2604.01152v1)§3.2/3.5–3.6/4.1–4.3/Tables1/3/4的决定部分：旧output deltas sampled SVD只截断经验span；TinyLlama投影+冻结后ungated chat .853→1.778，T3不普遍改善当前code；mixed gate固定chat floor=.20，不能等同排他旧path恢复。Gemma routed各200题有反退但未获显著性，不把其写成总体统计证明。贡献是对原文广泛零遗忘保证的具体反证与声明对象分责，不因成熟模块/Books已有主题删掉。旧§3.5–3.6/4.1–4.3已有效正文可复用；新核只闭合采用/EX决定。Ch30具体Existing Coverage或必要逐字PRE尚待，未写书；不授all-input、非线性zero-forgetting、认知能力普遍transfer或无费路由。

## 15原EX的分层实际抽检：9/15，不是15全量验证

来源层：本集合全部SRC-ARXIV，实际读EARLY/EXACT五个pinned-v1题摘文件matching entry，样本覆盖模型融合、训练/RL、数据、平台范围、Agent评价与控制。抽样理由层覆盖范围不符、仅统计目录/发布、未提出具体机制/有效性差额的组合、以及安全/设计反证可能漏收。未将186身份/129标题重新变队列。

| 实际完整题摘样本 | 窄结论与必要补读 |
| --- | --- |
| 00086 HIVE | 保EX：摘要给跨层attention与三阶段alignment及任务涨分，未给某模块收益条件/失败人口；不由hierarchical术语证明新的融合算子。current官方事件页仅发现后续workshop/标题单复数等元数据，不作重要机制修订。 |
| 00222 RiskCI | 保EX：Firefox CI的commit风险预测/调度，不改变AI训练/推理主线。是范围出口，不因模型名称入选；完整题摘已读。 |
| 00239 PLtaxonomy | 保EX：646语言四资源层与token集中度是人口描述，未提供训练质量或curation机制的可比检验。 |
| 00422 SHARPEN | **重开**：安全claim触发实际§3.2/Alg1/3.3/Alg2/4.1/RQ3–4/T6–7。原“无收益条件”与T6的top-k/random/bottom-k修复—utility差额不符，不能用成熟SHAP+CMA自动EX。拟2+1+2=5，受影响安全内容深入完成；只定位选择/修复验收分账，不授一般安全。正式日期/Books由root后续门接。 |
| 00442 EVOM | 保EX：摘要的增量是solver execution outcome接GRPO/DAPO与换solver继续训练，未给超出既有verified-reward环的新credit/verification条件；声称zero-shot transfer未给改变判断的控制设计，不把数学编程任务自动当新的RL机制。 |
| 00696 TTA-Vid | 保EX：摘要将跨frame频率作同一个伪reward供TTT与bandit使用，没有独立标签资格、去除共同伪reward影响或模块成立边界的实际命题；不将“no labels/generalizes”自述认证self-label可靠性。未冒全文/未测反证。 |
| 00920 GPT-NL | 保EX：corpus收集规模/许可发布不构成新的受控训练机制，current事件页未见撤回/纠错信号；不授CC-BY声明已经认证全部法律条件，未作法律审计。 |
| 01142 boundedES+DDPG | 保EX：实际v1 §I/II/III及contact-phase supervisor入口核对，既有组合的任务搬移/摩擦目标shift局部结果，bounded-ES理论是引用旧结果而非本文新增可证组合条件。当前事件页v2 Oct04才新含finite-time convergence，不能倒灌Apr02；没有以v2替v1完成或比较全部正文。 |
| 01212 YC-Bench | **重开**：最初HTML的§3/4.1/5/AppC–D显示具体memory-negative，但author-date不一致，故没有凭HTML授正式采用。之后本reader实际补核exact-v1 PDF同位置，以下PDF尾证覆盖此前HTML出口；仅以PDF支撑5分标准Source，不混用正文，不自行移动first-public。 |

6个本轮未独立抽检题摘身份：00842 Pare、00853 MotionGrounder、00947 randomlanguagephysics、00969 DLWM、00977 FPDRL、01195 ORBIT。作者原题摘筛选保留；这里不冒全量负侧通过。已具名SHARPEN安全、01142重要后修订、YC设计反证的受影响必要层实际核完；只重开00422/01212，不因这两条把未抽样6篇转成全篇队列。轻量current原事件核00086/00422/00920/01142/01212及样本pinned-v1 comment，无已见撤回信号；这不等全站或所有版本历史证明。

### 00422 SHARPEN窄Source交接（不预支日期/Books）

[exact-v1](https://arxiv.org/html/2604.00422v1) Alg1需要clean/faulty模型、violating输入、benign background以及DeepSHAP反传；全流程不能称gradient-free。定位是相关proxy非因果fault证书。T6三修复任务的top-k比random/bottom-k更有效，RQ3的K过小漏目标/过大扰动与T7不同optimizer的property–utility取舍是局部资格，非单个百分比。Alg2仅预算内best-search返回，无真实property/utility双门停止；clean-reference可得与标签/触发人口是必要权限条件。RTX4080/128GB、VGG/ResNet/FNN、已知攻击、BR1000test-subset修复/其余test验证，未有全域未知攻击保证、LLM或独立复现。此模块收益对照足以修正贡献门，精确采用仍须本日日门/owner。

## 三项 owner / 逐字 PRE（只提案，未写书）

已完整读项目背景/学习理念/写作指南；LS当前只本日；actual owner及必要前后论证读回。以下仅待独立reader/root接纳的内容，未获Books锁。

### 01152：TRAIN-LORA / Ch30，具体 Existing Coverage提案

不新增段落。当前 [Ch30](../../../../../books/part-04-training-system/30-lora.md)“Model merging 与 adapter composition”实际正文：组合后仍须Evaluation（当前L645）；特殊token/nullspace保护段（当前L658）明确有限校准线性响应≠整网函数；READ正文两段（当前L674–676）明确冻结旧block≠组合旧任务函数，并分别验收旧参数与组合行为；持续学习CLARE段（当前L811–813）明确冻结旧权重不阻止新router抢路由。实际完整相邻阅读为642–681和780–820，不以题目或末注代正文。

这些论点已承载本次采用的“参数路径恢复、经验几何保护、混合路由行为三类承诺分开”。Brainstacks自身NS+冻结后ungated退步和非排他chat-floor是该论点的新局部验证，不是全新owner缺口；报告保§3.5–3.6/T3/T4实际反侧，不能因NC又降回EX。其余零遗忘/认知transfer广泛主张不采用；无改写所以不新增POST请求。

### 00519：TRAIN-DATA / Ch27，一段逐字 PRE

Owner当前SyntheticData开头（L351–355）解释一次生成/judge过滤，邻接为修正监督→该开头→跨语言合成；读347–381，Ch28开篇10–35核对objective交接。缺口是合成器读取current learner状态、逐阶段刷新，非一般质量/diversity关系。拟插在开头三行结束后、跨语言合成之前：

```markdown
固定生成器一次扩出全部数据，在目标学习者与所需覆盖稳定时最容易复查；如果前一批训练已经改变了学生会什么，下一批的选择信号也可以随当前checkpoint刷新。一条受限图像合成分支在每阶段先训练当前learner，再以它与full-data reference的预测loss差引导diffusion候选、从多个候选中保留最高分，加入集合后继续下一阶段。这个差值提出的是“当前学生仍难、reference较容易”的样本，不是真实新知识量或标签正确性的证书；跨increment准确率和loss spike也不能独自认证信息互补。[必要机制与局部对照](https://arxiv.org/html/2604.00519v1)支持把learner/reference身份、刷新阶段、候选预算和最终数据成员留在lineage，而非宣布视觉多样性或平均梯度方法普遍无效。逐阶段learner训练、reference准备、候选生成与排名均付费，有限CNN/图像人口、reference偏差与非单调候选收益仍限制迁移；质量、预算或reference可信性未通过时，保留固定生成/过滤、可信真实样本和独立训练效用验收。<!-- source-family:SF-2026-ARXIV-2604-00519 -->
```

本段不照录39.1%/JS或宣称LLM/general-information定律。私有Source是标准5分，若Books采用此具体缺口则按owner受影响内容核足；full-data reference/每阶段训练与proxy反侧已实际核，无代码或实现依赖。作者只能在root授锁后按通过PRE写入，并另请求实际POST。

### 01170：PLATFORM-EVALUATION-SYSTEM / Ch66，两段逐字 PRE

当前conformal-intro（L980）只覆盖固定artifact与exchangeability；StructuredPrediction/label-oracle分责/随机strong-audit一带（L982–1014）不解释input内自适应fast-state与完整停止算法的校准对象，后者是具体缺口。已读978–1020完整局部，Ch67开篇10–35核Monitoring只消费结果不定义风险。拟在conformal-intro后、StructuredPrediction标题前插入：

```markdown
固定score与阈值在模型和生成策略稳定时最容易校准；若同一条推理过程中还会更新probe的fast state，校准对象就必须是完整停止程序，而非更新前的一个分数。一个受限分支冻结语言模型，在每个reasoning step先评分并判断是否停止，未停止时才用伪目标0更新fast probe，下题重新恢复初始化；outer meta-training只提出初始化与适配参数。未停止不表示这一步真实错误，consistent标签也不等真实正确性，累计首次正确后的标签更不证明后续答案不会反转。程序身份应绑定特征、初始state、更新次序、随机机制、标签事件与阈值选择，而不只发布probe权重。<!-- source-family:SF-2026-ARXIV-2604-01170 -->

对这条输入内自适应分支，[必要风险论证与反侧](https://arxiv.org/html/2604.01170v1)只在outer固定、独立同分布校准样本及部署采用相同effective policy等条件下，把完整随机算法交给LTT阈值检验；所得是marginal风险而非逐题或任意OOD保证。在线更新这一形式不自动证明实验已经on-policy；实际轨迹、search/stop规则或更新动力学改变就须重新校准，原文未定义的无可用阈值回退也不能自行补成安全recipe。局部对照支持meta-training加online-update的联合收益，不隔离两者各自必要性；OOD超目标风险、标签与正确性的差额，以及轨迹生成/标注、meta训练、阈值运行和逐step特征/更新的全部费用仍要保留。条件失配时停止依赖该风险证书，回到固定预算推理、已校准的静态停止或独立答案验证，而不让更高token saving代替验收。<!-- source-family:SF-2026-ARXIV-2604-01170 -->
```

只采用完整adaptive algorithm校准责任及score/update/reset接口；不采用原文任意泛化、无合法阈值安全recipe或未证明on-policy实验。原7分有效层与新T5反侧合并，无需无差别重读A/B；作者取得窄PRE/root锁后才写书并交实际POST。

## 两个误排条目的后续安全出口

### 01212：exact-v1 PDF替换不一致HTML证据 / 标准Source通过

本reader实际打开[精确v1 PDF](https://arxiv.org/pdf/2604.01212v1)，首页title/authors/完整abstract匹配，Date April2与arXiv v1 Apr1字段分账。实际补读PDF §3 pp4–5 Memory、§4.1 pp5–6、§5 pp7–8、AppendixC pp11–13与必要AppD Table3 pp14–15：20turn截断、每turn系统prompt注入scratchpad、12models各3seed共36run；Sonnet在Turn7写正确规则而Turn8接四任务、Grok准确诊断却未行动、Opus违反自己的blacklist均在PDF原文。AppC仍鼓励parallel，故不能把过并发归成无提示混杂的模型固有失败；数字模拟且没有控制memory写入/读取对照，不能授memory因果、所有长期Agent失效或生产return。采用5=2+1+2只限persisted correct rule≠当前动作服从。图像Figure6未另审，不以图证明原trace；这不是artifact复现。root已核PDF身份/日期链，当前缺层已闭合，HTML author-date冲突保历史警告但不再阻塞此PDF窄命题。

### 00422：PLATFORM-SECURITY / Ch72，具体 Existing Coverage提案

root实际DataCite owned/findable Apr2＋MM04公告下界链已核，本reader不重复日期探索。当前[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)“更新位置也可以先作为待验收的对象”段（当前L37）已经要求行为保留/移除测试，明确位置是给定模型/数据/干预下的候选而非唯一因果电路；紧接“候选位置可以约束随后修复的参数范围”（当前L39）明确移除测试、局部修复、原安全能力保护三份责任，成本/未知攻击/utility回归与不发布共存。实际完整邻接28–44读回，Ch73开篇明确生产readiness另门。

只采用SHARPEN T6/T7对这份分责的有限验证与clean-reference/DeepSHAP权限条件：定位缩窄search不会自授修复与utility，budget-best不是双验收门。正文已覆盖拟采用的设计判断；报告写明这条原源实际方法资格和反侧，Books不新增成熟算法摘要，不把specific Existing Coverage改回贡献EX。正式处置建议已有覆盖，无新写入/POST。

### 01212：AGENT-MEMORY / Ch77，具体 Existing Coverage提案

当前[Ch77](../../../../../books/part-07-agent/77-memory.md)Context/Memory主线（L29–37）要求保存区分历史的状态但不授authority、仍由Planner/当前observation决定行动；增量投递两段（当前L219–221）明确“已投递”既不证明模型消费也不保证下次仍可见，不能由投递记录签执行授权。实际完整207–230邻接读回，Ch80当前64–72还将反馈遵循/真实结果与persisted lesson分开；它只作交接，不成为第二owner。

这两个正文位置已承载本次窄命题“内容正确且持久/被投递，不证明当前读取并执行”。YC-PDF的正确规则却立刻违背是具体受限反例，可在报告保留actor/seed/turn与prompt混杂，不泛化memory无效或改写现有Memory设计。Books建议已有覆盖，无新写入/POST；日期/身份以root合法PDF链，不混HTML。

### 当前停止

追加轻量current官方abs实际核00519/01152/01170，无已见withdraw/correction；00086 current v2 Aug03仅所读abstract/comment/journal条目没有影响Apr02所判机制的明确纠错，不借版本号要求全旧新比较。Books PRE/NC仍待独立reader/root接纳，root负责锁与真实POST；本文件不预支DAY。QUEST由root持有，未重复日期探索。至此本agent五Source、9/15分层样本、两定点重开Source/PDF替换与五owner提案均准备好，只本日，不接04-04。
