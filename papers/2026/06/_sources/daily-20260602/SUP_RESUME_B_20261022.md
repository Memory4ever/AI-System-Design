# 2026-06-02 单日恢复 — 作者 B


## B14 — 30365正式先行发表定点恢复及最终作者交接（非DAY）

30365早稿线索已实际恢复，不沿“arxiv submission即公开”捷径。实际 [ArtSec官方program](https://artsec26.ieee-security.org/program.html) 载May21 2026、上午Paper Session1同完整题名及Yizhu Wen/Shuhao Zhang/Nan Zhang/Long Cheng/Hanqing Guo五作者；这是会议节目与身份，不单靠它证明正文发布。作者 [demo](https://yizhu-wen.github.io/Mental-Damage/)实际只有六audio对照/题名，未署日期或paperlink，不听audio、不改扩payload。IEEE网页 [11573739](https://ieeexplore.ieee.org/document/11573739/)在本工具不可达，但可用 [精确官方publisher登记Crossref DOI](https://api.crossref.org/works/10.1109/spw72489.2026.00026) 恢复正式论文日期与身份；query.title仅发现，随后精确DOI原件已实际读。

实际精确原字段摘录如下（不把created或会议event.start改名first-public；author名单与arxiv/官方program完整匹配）：

```json
{
  "DOI": "10.1109/spw72489.2026.00026",
  "title": ["Mental Damage: Caption Poisoning Attacks on Retrieval-Augmented Text-to-Music Generation"],
  "publisher": "IEEE",
  "published": {"date-parts": [[2026, 5, 21]]},
  "published-online": null,
  "published-print": {"date-parts": [[2026, 5, 21]]},
  "issued": {"date-parts": [[2026, 5, 21]]},
  "created": {"date-parts": [[2026, 6, 29]], "date-time": "2026-06-29T19:38:32Z", "timestamp": 1782761912000},
  "event": {
    "name": "2026 IEEE Symposium on Security and Privacy Workshops (SPW)",
    "location": "San Francisco, CA, USA",
    "start": {"date-parts": [[2026, 5, 21]]},
    "end": {"date-parts": [[2026, 5, 21]]}
  },
  "link": [{
    "URL": "http://xplorestaging.ieee.org/ielx8/11573640/11573382/11573739.pdf?arnumber=11573739",
    "content-type": "unspecified",
    "content-version": "vor",
    "intended-application": "similarity-checking"
  }],
  "resource": {"primary": {"URL": "https://ieeexplore.ieee.org/document/11573739/"}}
}
```

该publisher-deposited正式print发表事件为May21，和独立官方同日节目相合，早于Jun01。只采用“不晚于May21已有同family正式发表”的排窗界，不冒精确全球首次时刻/更早渠道；arxiv v1首登记不是自动新贡献事件，无具名extended/重要修订信号。本日窗外首次材料关闭/必要恢复线索，**不列确定Jun01候选、不评分、不审Methods、不写Books**；若将来出现Jun01实质新增事件及其必要证据才只重开该事件。reader F6唯一实际日期/去重核已通过。

30359精确Crossref标题查询只返回两不同论文身份，不能拿空/异题结果说不存在原稿；本轮有限可用路径与跨日原字段均在B10，保精确外部日期恢复，不扩Methods/正文池。MiniMax有效同事件去重已完成（B10），Google/Meta/MiMo原外部切片不被普通尾差混入。

B11/B12原批准两段实际保存后，jun02_supp_reader F5已唯一actual非writer POST通过：完整新增/完整直接两侧/本人末注逐字相合，两章working/cached限定check0，两窄位生效释放。本人只行政同步Source/PRE编号（两项均F3）与真实F5 POST，不第三Source/正文复核。B13原6中心争议、无Books由reader F4通过；原B4 D3由A9.2通过且root采用，不降分/改EX。reader F6已实际独立核精确DOI字段和30365v1，接受本B14窗外排除及两注F3/F5行政同步；本B7队列为2I/1中心争议/1窗外，全部精确窄位释放。B8五新项已明确移交作者A，后续以A的新文件层为准，本人不重复Source/owner。没有仍持有的Books窄位或待执行写权；没有stage/commit/push/index，本作者不签整日报DAY。

## B11 — SCOUT 2605.30837v1：必要证据/实际owner与完整 PRE（待 reader）

正式新增日证已reader F2通过，Jun01BJT，首次2+2+2=6。作者实际读exact-v1完整§3–6/Alg1/§7.1，§7.3–7.6/Limitations方法/反侧正文；主表未全审不采用headline数字。Reader已实际必要Source独核补E selector/vote/gate与K部署成本/N单run，作者一次实际消费：pred_corr二值，trust-weighted agreement不是正确概率；空S直接judge，非空但uncertain且judge预测不可靠仍留lightvote；新增detector/IHEval4o有ASR反退。τ是SCOUT450 sweep选点，不是独立安全校准；predictor batch摊销及verbosity缩放不是所有online concurrency实测，pred_lat跨域低估不能授SLO，adaptive router攻击未测。Fingerprint加入需anchor-pass/serialization，不是零集成费；predictor训练/所有detector/anchor与model召回、误拒/漏检回归全费。未核实现/复现，不第三泛读。

实际读Ch72 gpt-oss-safeguard结尾完整policy sensor段、秘密方向双段、GPT54 message/actor完整两段及marker、直接DeepContext完整机制/费用段；另定位RouteGuard30693完整新段，owned-by-threat expert/union与这里per-input可靠度predictor择池/升级不同。全Books精确family无既存；唯一PLATFORM-SECURITY。拟GPT54完整marker后/多轮sensor首段前原单段，未授写：

> 固定 detector cascade 还可按每个请求重选成员，而不只调整同一风险分的阈值：先在 anchor inputs 上保存各检测器的判决、正确性与耗时，检索相似结构供小 predictor 预测本请求的 detector 可靠度，再让被选 light pool 并行投票；低 agreement 时才按 judge 的预测资格决定是否升级。[SCOUT 的受限分支](https://arxiv.org/html/2605.30837v1)中，空集合直接调用 judge，非空但 judge 被预测不可靠时仍可维持 light vote；二元可靠度与加权一致率都不是校准安全概率。新成员也可能扩大漏检，anchor 外或针对 router 的攻击未有普遍保证；预算选点更不成为在线 SLO。Anchor 制备、predictor 训练/调用、全部检测与升级、状态刷新及误拒回归均计费。池、anchor 或预算失配时，保留固定已验 detector/显式升级和独立 enforcement；选择更快的 sensor 不取得工具或内容释放权。<!-- source-family:SF-2026-ARXIV-2605-30837 -->

## B12 — Welfare/Improvability/Variance 2605.30916v1：必要证据/actualowner与完整 PRE（待 reader）

正式新增日证reader F2通过，Jun01BJT，首次2+1+3=6。作者实际完整读exact-v1§2/2.1模型Eq1–3、§3–4.3代理/过滤、§5结果与§6限制。CARA/Gaussian、linear response/quadraticcost与risk-internalized designer下v*=(M+rΣ)^−1 Mw；固定v时lab a*=C^−1 A^T v不直接含Σ，noise经designer选权重作用，不混称lab固定v反应。 empirical部分没恢复全M/Σ或定r，也没发布canonical v*，只给三个separate proxies。w是pro-worker normative choice，不是全社会objective。EvoLM4B独立PT/SFT/RL axes非全factorial；PolyPythia410M 8seeds×10checkpoints噪声跨family/scale不能直接合成frontier recipe。删极端p/负slope/低variance改变eligible pool，cost是imputation，不能实测费用/最低投资保证。reader必要F/G独核层一次消费（28人审/换judge与权重敏感），不第三读。所有judge/human映射、panel evaluation/拟合/Bootstrap与独立用途审核全费，不采用p值/全数值结论或代码已核。

实际Ch66完整读“评分反过来改变行为”到04664公式/整段、直接261013821回答筛选整段，以及更前目的/维度/人口定义。已有coverage/refusal incentive，但未有benchmark aggregation改变训练投入激励及三primitive分责；全Books精确family无既存。唯一PLATFORM-EVALUATION-SYSTEM。拟04664完整marker后/回答筛选首段前一段，未授写：

> 聚合规则还会改变开发者把训练投入放在哪里，而不只是怎样选择一次答案：在声明的规范价值、可改进成本与测量噪声下，先区分社会希望提升的任务和开发者更容易提升的分数，再检查统一均分是否诱导错配。[受限 principal-agent 分析](https://arxiv.org/html/2605.30916v1)中的最优权重依赖线性响应、二次成本和风险内化；噪声通过设计者选权重起作用，不是固定权重下开发者反应自动含有噪声。作者的职业映射/worker偏好、4B成本与410M跨seed噪声只是分开估计的代理，未恢复完整联合结构或给出通用最优权重；worker价值也不穷尽社会价值。人审/映射、panel评测、成本估算和敏感性分析都付费。规范目标、尺度或proxy不稳时，保留冻结分项、显式人工权重与独立用途评价，不由Pareto代理或“更便宜可改进”自动删题、宣布普遍能力进步。<!-- source-family:SF-2026-ARXIV-2605-30916 -->

## B13 — DPPrefSyn 2605.30808v1：中心隐私证明缺口（待 reader确认处置；不写Books）

正式新增日证reader F2通过，Jun01BJT，首次2+2+2=6不变。实际读exact-v1§3邻接/BT模型、完整§4.1/4.2/Alg1、§5.1–5.3/§7必要评价与限制，Appendix A完整privacy theorem/proof/PRV会计代码；不遍历全repo。所有private triple (prompt,response+,response−)单entry相邻而非user-level。公共embedding差→DP-PCA→DP-KMeans→每cluster DP-SGD reward→public prompts生成L候选取最大/最小reward，分布cluster由p采样。BT单个胜出不逻辑推出强alignment，linear preference/cluster是建模先验。公开生成不是充分迁移/真实人类偏好保证。

决定性中央缺口：Alg1 Lines11–12直接h=[|C1|,…,|CK|]、p=h/n，未显示计数噪声机制却称DP histogram；A proof只计DP-PCA/DP-KMeans/DP-SGD，再把其余称public或postprocess，未定义DP-KMeans对外输出究竟centers、assignments还是counts，也未证明raw membership/count派生已受保护。Data-dependent partition下不能单凭“disjoint”跳parallel composition，cluster-size过滤/最小值的资格同需说明。reader已独立实际A/PRV与B3（diffprivlib名称未补这条边界），作者一次消费其有效层；不为隔离再扩代码审计。不宣判所有DP方案不可能，也不声称实现已泄漏，但本printed pipeline的端到端保证未闭，不能靠成熟postprocessing原则绕过。

现有QA/summarization实验5seed/Pythia2.8B及至8B、DP-FT比较混公共prompt和generator优势，部分Table3同generator DP-FT更好；GPT4o winrate非人类效用，MIA≈chance不补正式DP证明。全部生成/弃选、embedding、私有训练与会计、下游回归全费，英文/8B与API费用限制保留。拟中心争议隔离/Books暂缓，唯一候选知识链可路由TRAIN-RLHF（消费者可SFT/DPO/PPO，不双写Ch34），不以降分或无贡献关闭。重开精确要DP-KMeans输出对象、histogram保护/会计、条件化分区的parallel composition与small-cluster过滤资格或作者更正；只重开这条证明，不要求所有实验/附件。


## B9 — 已成层实际采用与发现覆盖差额

B1/B2真实保存后，root R64一次实际非writer POST通过，两个Ch26窄位生效释放。B3按A9.1新授保存，作者完整局部自读后A11唯一actualPOST通过生效释放，D3 A9.2中央反证/原6争议隔离通过；B5/B6按R64新授保存，作者完整局部自读后root R65唯一actualPOST通过生效释放。只消费这些有效层，不第三Source/POST；不以五单篇成立冒DAY。

发现层实际重读原SUP“有界查漏本轮新增与原字段停点”（原L196附近）与末停点、报告§2：显式复数/系统同义词92条1页无next，CL/LG/CV各末60相关标题浏览早已完成，原README残余措辞部分未同步；本轮不重扫1250、不扩月或raw队列。真正普通尾差就是B7四AB、B8九AB的具体贡献与日证/必要层，而不是整类标题未筛。五B8潜力已由root准入并交A独立作者工作，本人停止其Methods；三EX仍待root有限抽核，不再扩core。

30628一次决定性补读 [exact-v1 §3.3–3.4](https://arxiv.org/html/2605.30628v1#S3.SS3) 完整：Flog=min(1,ln m/ln|C|)是作者选定、未验证真实覆盖曲线的planning approximation；eres=(1−Flog)ehard直接移项给Prop2 m≥|Ceff|^(1−eps/ehard)。Polylog另假设active catalogue随hard decisions为log，cap来自预设有限目录；Prop1以任意有限库均有新的intervention-distinguishable failure作前提。它未增加可执行coverage/修复机制或独立支持的可靠性边界；一般per-decision与sequence分母区别不是此文新增验证。因此提案具体贡献EX，不因“理论/没有实验”排除，也不把条件代数说成错误；不用普遍taxonomy原则制造Books段，无评分/Methods全审队列。

## B10 — B7日证、公开日期精确缺口与MiniMax去重

30837/30916/30808本轮实际exact-v1完整abs/history/current comments已读，与各官方DataCite精确identity/client=arxiv.content/state=findable/registered联合；reader F2已独立直接HTTP复核此层通过，后续复用不重核。三个v1 Submitted分别2026-05-29T04:49:20Z、07:01:38Z、03:53:12Z，registered分别2026-06-01T02:11:04.000Z、02:12:56.000Z、02:10:24.000Z；按本日已核官方公告规则最早Jun01T00Z到各registered全同BJTJun01，created/Updated未作公告。各当前abs无具名撤回/纠错标记；SCOUT v2/v3不自动另起重要修订，DPPrefSyn accepted ICML2026 comment不自动当更早正文公开日。

30359 actual exact-v1身份Kernel Foundry/Zixuan Huang等8人，与官方DataCite title/DOI精确同一；v1 Submitted=2026-05-08T03:41:54Z，created=2026-06-01T01:59:43.000Z，registered=2026-06-01T01:59:44.000Z，arxiv.content/findable。Updated=2026-06-01T00:00:11Z只保原字段，不改名announcement。最早May上旬到registered区间跨日。原有限author/project/精确标题恢复无具名更早正文；本轮精确作者/标题primary-domain搜索仍未恢复作者公布日期。最初yymm月表路由2605返回InvalidYear，随后已实际改正确 [官方2026-05月表](https://arxiv.org/list/cs.NE/2026-05?show=2000)，仅定位同一ID [98]与其完整entry；月表标题“Authors and titles for May2026”且无每项day，不能把entry存在换成Jun01证。旁边无关条目不进入队列、第三方June1文章也不替原始日证。本轮精确日期资格仍外部保留，不确定当窗候选、不做Methods/Books；重开仅目标日官方announcement/作者有日期的原始正文或能收窄同日的正式发行记录，不要求所有假想渠道排除。

MiniMax只定点读06-01报告旧M3完整候选行/限定采用与其原独核R3：相同官方[MiniMax M3](https://www.minimax.io/blog/minimax-m3)、唯一NewsArticle JSON-LD datePublished/dateModified=2026-05-31T17:31:18.000Z=Jun01BJT，原旧行8分/Ch22 selector gradient ownership→GQA/block→KV-outer→fallback具体已有覆盖已真实独核有效。同一首发事件按用户冻结旧行复用，06-02不增家族/不重复分与Books，不回填后续paper细节。当前EN13/CN14日期边界与Agent4条Sep19后到底在原sliceA/SUP和06-01R4已有实际结果；本轮实际重新读其精确停止record，不把已做未同步误作未做，不重抓全目录。Google Research/Meta/MiMo仅原已穷尽的具体历史切片继续隔离，不拿空搜索或普通未读项冒其外部缺口。


## B8 — 九项既见身份的具体尾差判断（待独立准入/抽核）

先实际重读完整AB，再对决定准入的含糊机制取一次小域。未因已54家族设数量上限；不把普通待办外部化。下列五项有可指认设计/测量增量，先校准再审评价，不预采用任何headline。

### 30898：拟准入

Title: UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling

Abstract: In real-world deployments of large language models (LLMs), balancing inference quality and computational cost has become a central challenge. Existing approaches tackle this trade-off along two largely independent dimensions: model routing, which switches among models of different scales to match request complexity, and test-time scaling (TTS), which adjusts inference-time compute within a fixed model for fine-grained control. However, this decoupled design introduces inherent limitations. Model routing yields coarse-grained, discrete performance changes due to the sparse set of model scales, while single-model TTS often encounters capacity ceilings and exhibits diminishing returns as compute increases. Moreover, treating the two mechanisms separately restricts adaptability in dynamic inference environments. To overcome these limitations, we introduce Unified Inference Scaling (UIS), which unifies model routing and TTS in a single optimization space. Building on this formulation, we propose UniScale, an online framework that models adaptive UIS as a contextual multi-armed bandit problem and learns inference policies via LinUCB. The framework incorporates efficiency-aware learning and cost modeling to ensure stable and scalable optimization over high-dimensional action spaces. Evaluation shows that UniScale effectively exploits the synergy in the UIS space to deliver a fine-grained and consistently better quality-cost trade-off across diverse, dynamic inference scenarios.

身份：[exact-v1](https://arxiv.org/abs/2605.30898v1)；Submission history From: Kaiyu Huang [ view email ] [v1] Fri, 29 May 2026 06:31:21 UTC (373 KB)；原件为同日KNOWN6/7，未更新版本。

具体链与实际读层：routing与单model TTS各自决策 → 联合(model,query-parallel,chain-parallel,beam)配置的online估值并由path score控制退出 → 重新考虑跨模型/搜索预算与代理反馈资格；初拟2+2+2=6，INFER-SCHEDULING或PLATFORM-GATEWAY待唯一owner。已有限实际读§3.1–3.3/3.4前段；concat(query,action)线性reward的query/action相互作用表达及early-exit potential还需证据，不授frontier最优。

### 31073：拟准入

Title: ConsisGuard: Aligning Safety Deliberation with Policy Enforcement in LLM Guardrails

Abstract: Reasoning-based LLM guardrails improve safety moderation by generating explicit rationales before issuing final decisions. However, their rationales do not always lead to faithful enforcement: a model may recognize a harmful intent in its reasoning but still predict a safe label, or issue an unsafe decision without policy-grounded justification. We identify this safety-critical failure mode as the deliberation-to-enforcement gap. Unlike general chain-of-thought faithfulness, guardrail reliability requires policy execution consistency: the generated reasoning should be grounded in the safety policy, and the final decision should be entailed by that reasoning. We propose ConsisGuard, a consistency-aware framework for reasoning-based LLM guardrails. ConsisGuard performs Policy-to-Decision Trajectory Distillation and Functional Coupling Alignment, aligning the internal coupling between safety deliberation and decision enforcement. Experiments on prompt and response harmfulness detection benchmarks show that ConsisGuard improves detection performance while reducing policy execution failures. These results suggest that reliable reasoning-based guardrails require accurate faithful execution of safety policies.

身份：[exact-v1](https://arxiv.org/abs/2605.31073v1)；Submission history From: Yan Wang [ view email ] [v1] Fri, 29 May 2026 09:42:08 UTC (4,943 KB)；原件为同日KNOWN6/7，未更新版本。

具体链与实际读层：有rationale不保证finallabel受其约束 → policy-grounding/decision-entailment分别筛teacher轨迹并以两套head function-vectors及difference regularize → 重新考虑可见解释与decision训练的不同验收；初拟2+2+2=6，PLATFORM-SECURITY。已有限实际读完整§3，尚未评价，不将functionvector名当真实唯一因果。

### 31381：拟准入

Title: LLM Judges Inconsistently Disagree Across Safety Criteria and Harm Categories

Abstract: We evaluate the consistency of automated judges in conducting a multi-dimensional safety evaluation in a reference-free setup. Our results indicate that Large Language Models are unreliable judges in identifying safety issues related to machine-generated advice in regulated domains such as finance, although they are more reliable at identifying more overt forms of unsafe/harmful content such as violence. The degree of inconsistency in a model's judgments can vary significantly by the chosen safety criteria and can be impacted by the language of the content and its linguistic style as well. Finally, there is high disagreement among different judges for the same output, across domains, safety criteria, and languages. These findings provide new insights on the practice of using LLMs as evaluators and offer several recommendations for practitioners on how to use automated judges in practical scenarios.

身份：[exact-v1](https://arxiv.org/abs/2605.31381v1)；Submission history From: Krishnapriya Vishnubhotla [ view email ] [v1] Fri, 29 May 2026 14:50:08 UTC (1,534 KB) [v2] Tue, 2 Jun 2026 14:28:06 UTC (1,532 KB)；原件为同日KNOWN6/7，未更新版本。

具体链与实际读层：总体safety judge一致率遮住criteria/语言/样式差额 → 相同query-response的多维/翻译/改写配对，并联合chance-corrected与raw agreement → 重新考虑安全代理的稳定性与原label population；初拟1+2+2=5，PLATFORM-EVALUATION-SYSTEM。已有限实读§3，但semantic-preserving并不自动成立，endorsement强弱可能改变safety；准入命题是测量资格，不预得真实准确率。

### 30481：拟准入

10.48550/arxiv.2605.30481 When English Rewrites Local Knowledge: Global Narrative Dominance in Large Language Models
Large language models (LLMs) are widely used as cross-lingual knowledge interfaces. However, culturally grounded questions often reflect globally dominant narratives rather than local contexts. We study this failure mode as \textit{global narrative dominance} in Bangla, a low-resource cultural context. We introduce \texttt{CulturalNB}, a dataset of 717 manually curated Bengali cultural instances with parallel Bangla--English question--answer pairs and supporting evidence, metadata, and sociocultural annotations. Using question-only and evidence-based prompting, we evaluate nine state-of-the-art LLMs with human and two independent LLM judges across metrics for cross-lingual consistency, language anchoring, global substitution, institutional bias, and epistemic perspective coverage. Results show that questions asked in English systematically increase global substitution and institutional framing while reducing local perspective coverage. Local evidence improves factual consistency and perspective coverage, but does not eliminate language-induced epistemic shifts. These findings suggest that cultural failures in LLMs are not only missing-knowledge errors but also failures of grounding and narrative prioritization.

身份：同日page2当前题摘，仅同family导航；exact-v1/必要日证另核。

具体链与实际读层：跨语言错误可能被归为知识缺失 → 平行Bangla/English同时比较question-only与同源证据条件，证据改善仍有narrative framing差额 → 重新考虑补证据是否足够、语言条件是否保持测量目标；初拟1+2+2=5，PLATFORM-EVALUATION-SYSTEM。只实际读§3数据/翻译人工过程，核心评价尚未读。

### 30459：拟准入

10.48550/arxiv.2605.30459 Can LLM Teams Play What? Where? When?
Large language models (LLMs) remain limited on tasks requiring indirect reasoning, cultural knowledge, and coordinated hypothesis testing. We investigate whether team-based interaction improves LLM performance in What? Where? When? (ChGK), a quiz game designed to reward collective reasoning. We introduce three team strategies: Voting, Silent Team (the captain observes final answers), and Talkative Team (the captain observes both answers and rationales). To minimize data leakage, we evaluate these strategies on a dataset consisting of 572 ChGK questions released in 2025. Using six recent large-scale open models, we show that team-based strategies outperform single-model baselines, yielding gains of up to 20 percentage points in accuracy. The best team achieves 44.23% accuracy, and approaches human team performance on questions with available human statistics. Analysis of inter-model diversity reveals that disagreement strongly predicts lower accuracy, but explanatory communication substantially mitigates performance drops. We further examine captain behavior and find no evidence of self-preference bias; access to peer rationales improves captain judgments. Overall, LLM teams function primarily as answer selection and error-filtering mechanisms rather than generators of novel solutions. Our findings highlight the importance of interaction and suggest adaptive strategies as a promising direction for multi-agent systems.

身份：同日page2当前题摘，仅同family导航；exact-v1/必要日证另核。

具体链与实际读层：team提升被当新解题能力 → 相同六候选下captain只看answers或另看rationales与voting，区分选择/过滤和新答案 → 重新考虑收益是候选覆盖还是聚合；初拟1+2+2=5，AGENT-MULTI-AGENT。已有限实际完整读§3，selection贡献还需原结果，不能由题摘直接证明无novel solution。

### 30738 MAVEN：具体贡献排除提案

完整AB已实际读（KNOWN7）。只为决定性定义实际读exact-v1完整§3/Alg1：context buffer→atomic subtask→tool invocation→verification/revise与missing-prerequisite stop，没有新的执行/状态/验证机制或成立边界；性能提升与估算cost本身不足准入。新math/physics stress task与部分过程质量≠终局的总称也未给区别于既有原语的受控盲区。不是因未开源或泛称scaffold排除；按实际定义关闭，不为此扩全结果/日证。

### 31170 emergent-language posts：具体贡献排除提案

完整AB已实际读（KNOWN7）；本轮只见HTML题目目录未冒方法已读。公开贡献是对Moltbook帖子提议的关键词/zero-shot分类与描述给定后的ICL语言学习，作者明确不能确认autonomy；没有实际自主隐蔽通信/监控漏检实验或新的防御接口。Oversight-evasion意图文字和较低alignment-judge分不提供真实控制失效边界，不能把威胁标签替贡献；故依完整AB关闭，不扩语言payload。

### 30391 Social Reasoning thesis：具体贡献排除提案

完整page2AB已实际读；有限读exact-v1§4.1/4.2主体（末输出只到prompt-engineering原则，不冒§4后部或全thesis）。经典initial QA→complete crosscritique→revision、critique当轮mask/role logs只是标准protocol组织，未见区别于这些既有做法的新增mechanism。ATR是解释性类比，不证明群体普遍优胜；以temperature为hallucination-propensity analogue也不提供新intrinsic metric资格。仅在问卷上的gain/多样性关系不能替新的设计边界；具体贡献不足关闭，不扩literature/全部结果。

### 30628 Architecture of Errors：决定性条件尚待root准入裁定

完整KNOWN6AB与有限exact-v1§3.1–3.2、§3.3前半已实际读；log discovery明确postulate，per-sequence log active exposure是另一独立Assumption，L2 taxonomy非latentL3，endpoint counts不是discovery curve且作者承认missing test。尚不能把它当经验scaling law。但conditional finite intervention预算是否提供足够新的长期边界须由完整决定性Prop2核，不因理论无实验自动EX。只待一次§3.3–3.4核心，不扩附录/案例/全理论池。

边界：只新增 Jun01 BJT 自然日，保护旧候选日期、分数、小时窗口及连续旧 §4。作者 `jun02_supp_author_b`；root 唯一报告/State writer 和本文件必要非作者独核。只写此文件、必要原件和获本轮精确许可的 Books 窄位；不 stage/commit/push/index。本轮实际重新读 AGENTS、Research/Report 合同全文、Sources 用法/每日与 arXiv 主题、Prompt、ROADMAP 及本日 State 路由；Books 比较前实际读 PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE。原 R55 日证/准入有效，未因版本号重开旧稿。

## B1 — ELAN4D 2605.30484v1：必要证据与逐字 PRE（待 root）

实际读 [exact-v1](https://arxiv.org/html/2605.30484v1) 完整 §3、§4.1–4.4、§6；不是沿用原目录层。FK 用已知运动链和 proprioception 在 robot-base frame 生成 joints/end-effector 的未来相对位移，target 是 embodiment motion，不是 whole-scene dynamics。控制旁路读取 stop-gradient 主 action feature，经 zero-init projection residual 融合；action loss 更新主链与旁路，track L1 只更新旁路/decoder，不能说整个 VLM 被冻结。部署仅丢 track decoder/current-keypoint input，控制旁路仍执行，不能说新增参数/计算全消失。

训练为 pi0/pi0.5、30K steps、8 GH200、batch64，LIBERO 原数据而无 Plus 增强，RoboTwin 每任务100 demos/100 trials；实机三类各50 demos/20 trials。§4.4 no-track 同容量对照、VLM-query 与 branch 对照支持本受限接口选择，但位置/梯度/查询共同变化与 CKA 不证明唯一 representation-drift 因果；whole-scene 用 simulator GT，有额外权限。LIBERO 若干 suite 退步，robot-only 不能覆盖外物/形变/复杂接触。未采用 headline 倍率、预处理硬件公平比较或部署 SLO；precision/完整 inference latency 未披露，未核实现/复现。

实际 Ch26 读取 action-facing gradient-authority 整段及 FLOWER、mediator、VLA-Adapter、12772 全段、GuidedVLA 全段、ForeAct3D 全段和后接 CRAFT 全段。已有旁路/特权未来监督，却未承载“由本体 FK 的未来目标只改旁路、部署丢 decoder 但保 residual”的具体分责；全 Books 精确 family 搜索无既存。唯一 owner `MULTIMODAL-EMBODIED-VLA`，原 2+2+2=6 不变，具体长期差额使受影响内容深入。拟在完整 GuidedVLA/2605-12369 marker 后、ForeAct3D 首段前一段（未授写）：

> 辅助未来监督也可以只来自本体自身，而不重建整幅场景：用已知运动链把示教 proprioception 转为 robot-base frame 中关节与末端的未来相对位移，让读取 stop-gradient action features 的旁路预测这些 tracks，再经零初始化投影向原 action expert 注入 residual。[ELAN4D 的受限对照](https://arxiv.org/html/2605.30484v1)中，track loss 只更新旁路与 decoder，原 action loss 仍可更新主链；因此隔离辅助梯度不等冻结整个 VLM。部署丢弃 track decoder，却保留控制旁路，接口不变不是零新增计算。Robot-only 目标不直接描述外物、形变与复杂接触，额外容量及 VLM-query 对照只支持局部选择，CKA 不证明唯一漂移因果。运动学标定、tracks 制备、双目标训练、保留旁路与闭环回归均计费；本体/目标失配、任务反退或时限不合时，保留直接 action supervision、完整观察与独立 controller，不由未来位移预测批准物理安全。<!-- source-family:SF-2026-ARXIV-2605-30484 -->

## B2 — DriveMA 2605.31271v1：必要证据与逐字 PRE（待 root）

实际读 [exact-v1](https://arxiv.org/html/2605.31271v1) 完整 §3、§4.1–4.5、§6 和 Appendix A–B（不扩 C/D）。Trajectory annotation 把固定训练阈值和有限 visual resolver 分开；fine lateral labels 与 reward verification 不同，turn/lane-change 合并成方向，straight/lane-follow 合并 forward，slight-shift 保独立规则。x→m→trajectory 默认单一 horizon metaaction，两个 assistant turns 不是两次环境物理闭环。Reward 按 turn 分组归一，meta correctness 只发 meta tokens，trajectory/consistency 发 trajectory tokens；不意味着共享参数无耦合或完整因果 credit。

Qwen3.5 2B/4B、三前向当前相机；Waymo 5s/1Hz、479 preference samples，NAVSIM 4s/1Hz、103K trainval 中18K RL。SFT full parameter/8 A800/各1 epoch；RL600 steps、batch64、G8。§4.3 vanilla GRPO 同 reward 对照支持局部 turn assignment，consistency 提高与 RFS Spotlight 不单调；§4.5 更细 oracle 更好但 predicted 饱和，仅 SFT/纵向变粒度不推广为所有 RL。NAVSIM 是有限 benchmark，不是实际驾驶安全认证。全部 ACP240K、annotation/resolver、训练、rollouts、reward 与文本生成计费；未核实现、真实控制 latency 或复现，不采用跨 paper 数据效率 headline。

实际 Ch26 读完整 2601-10930 两段、2509-06201 两段、SteerableVLA2602-13193 全段、latent-plan2601-09708 双段及 GPL 全段。已有命令类型/消费者/时钟，却未承载“fine label 与 coarse verification 分离、各 turn 接收相应训练反馈”的差额；全 Books 精确 family 无既存。唯一 owner `MULTIMODAL-EMBODIED-VLA`，原6不变，拟完整 SteerableVLA marker 后/latent-plan 首段前一段（未授写）：

> 可读命令还可被限定成能从生成轨迹重新核验的中间语言：先用示教轨迹产生 meta-action，再让模型预测它并条件生成 waypoint，将两者投影到共同验证空间比较。[DriveMA 的受限分支](https://arxiv.org/html/2605.31271v1)把训练时的细粒度侧向标签与较粗的方向核验分开，转弯与换道同向不代表二者语义已经等价；纵向与 slight-shift 仍按各自固定规则检查。训练对两个 assistant turns 分别归一奖励，meta 正确性反馈给命令 token，轨迹质量与一致性反馈给 waypoint token；这不等两轮真实环境反馈或共享参数无耦合。更细命令在 oracle 条件更有用，预测条件却可饱和，规则边界与视觉消歧也会带来噪声。标注/消歧、领域预训练、全部 rollout/奖励、两轮生成和独立闭环验证均付费；规则、命令可预测性或动作质量失配时，保留直接轨迹策略、可信短命令和独立 controller，一致性奖励不授真实驾驶安全。<!-- source-family:SF-2026-ARXIV-2605-31271 -->

## B3 — MASA 2605.30723v1：必要证据与逐字 PRE（待 root）

实际读 [exact-v1](https://arxiv.org/html/2605.30723v1) §2–4 全部方法/评价正文（HTML table-tag 的式/主表未全部读，不采用其数值或精确优化式），以及 Appendix B 完整消融、D model-card 构造和 F rewriter 训练。原 R55 日证准入复用；保持6。冻结的是 task consumer，改 skill 文本：固定 general 后逐 task-type 搜索，teacher 读失败与 consumer card，top-k retrieval 两层分开。NHR 是 unchanged-state 代理，不是安全/无效动作完整真值。Rewriter 是搜得高分文本的 SFT，输出一次改写仍需多个生成 token，不称单次 forward 固定费用；不把搜索所得“upper bound”当可证明最优。

ALFWorld 文本环境、WebShop 模拟、检索QA 三族/Qwen3四规模 non-thinking；初步受控 granularity 只是自述原则保留，不证明所有语义相同或唯一 granularity 因果。小模型/任务切片及 No Skill 可更好；card-ablation 支持 conditioning，但card揉合官方 metadata、teacher 总结弱点与行为线索，不是能力真值/参数量唯一因果。D 说明 preliminary rollouts 与 evaluation 分离；F rewriter BF16/full-param、769或499 pairs、5epoch，以training-loss收敛选checkpoint，不能授任意新模型泛化。环境搜索、失败/弃选、teacher/card、retrieval/online context、rewriter训练与生成全费；只少interaction steps不等净latency或break-even，硬件和完整API费未披露；未核实现/复现。

实际 Ch74 完整读 residual-conditioned search交接、SkillMOO 双段、SkillOpt 双段以及“条件化机制分支与共存边界”标题与首个身份信息双段。现有主体有一般搜索/有界编辑，但没有明确 consumer-conditioned 文本资产/搜索蒸馏分责；全 Books 精确family无既存。唯一 `AGENT-PROMPT`；拟完整SkillOpt/23904 marker后、条件化分支H3前一段（未授写）：

> 相同 skill 的表达也应随实际消费者验收，而不按模型大小预设“更短”或“更详细”：在 task model 冻结时，可把其能力描述与失败轨迹交给 teacher，先搜索通用指南，再固定它们搜索各任务类型的规则；另用这些高分改写训练小 rewriter，将后续适配从环境搜索摊销成一次文本生成。[MASA 的受限对照](https://arxiv.org/html/2605.30723v1)支持 model-conditioned 文本分支，却不使 model card 成为能力真值，环境状态未变化也只是停滞代理。No-skill 与不同粒度在部分模型/任务可更好，有限跨环境迁移不授任意新消费者可直接复用；搜索结果更非全局最优。全部探索/弃选、teacher 与 card、检索/更长 Context、rewriter 训练和生成均计费，较少交互步不证明净省时。消费者、harness 或反馈改变时，保留无 skill/原已验版本与独立任务回归，不让改写器取得事实、工具或发布授权。<!-- source-family:SF-2026-ARXIV-2605-30723 -->

## B4 — D3 2605.31164v1：中心机制冲突提案（待 root，绝不以泛化段绕过）

原6/日证/准入保持。实际读 [exact-v1](https://arxiv.org/html/2605.31164v1) §3.1–3.5 方法正文、§4.1–4.4 评价正文，Appendix A1–A4 及 Algorithms2–6；主结果表部分 table tags 未读全不采用主数字。§3.2 在 twice differentiable/local Taylor 下，I(i→j)=−γ g_j^T g_i+γ² g_i^T H_j g_i/2+o(γ²)，pair-specific curvature 可以产生有向不对称；这只是当前state单步loss，不证明最终test risk最优。Chunk保局部batch集合/改次序，RSR只是启发式。

决定性反侧在 A4 Alg3–4：每个batch只留 scalar λ_l，Alg4 写 I(i→j)=−γ g̃_j^T g̃_i+γ² λ_j/2，I(j→i)=−γ g̃_i^T g̃_j+γ² λ_i/2，再令 Sij=I(j→i)−I(i→j)。直接代数得到 Sij=γ²(λ_i−λ_j)/2，sketched gradient内积完全抵消；S只能是单标量差，无严格有向cycle，row-sum排序已按λ排序。它未保理论中的 g_i^T H_j g_i 交互，故正文一般冲突图/额外RSR收益与已打印可执行算法未接通。不能以“近似”自动授予pairwise方向信息；JL的内积保留也不证明二阶项保留。

GPT2-Medium355M/100B训练token与Llama3-8B SFT报告；A4写2×H200、FP16、Adam、batch16、单seed32，与SGD形式分开。§4.3承认 diagonal Hessian perstep computation overhead 增89%，不等净time-to-quality提升，PIQA还有反退。未核实现/复现，未扩理论附录。实际 Ch27 完整读课程20296双段、MR-UIE全段、05858双段和后proof-DAG全段，通用次序/难度代理已有承载；新方向图配方中央冲突不能借普通原则改成整合。提案：中心争议隔离、Books暂缓，原6不降分、不改EX。重开只需作者更正的pair-index curvature/实际实现与Alg4对应、或明确采用scalar简化并解释RSR/评价归因；不请求无关全量数据/附件。

## B5 — DARTS 2605.30859v1：必要证据与逐字 PRE（待 root）

原R55校准6/日证复用。实际读 [exact-v1](https://arxiv.org/html/2605.30859v1) §4.1–4.3/§5.1–5.6 全方法/评价正文（未全读table-tag主表/公式，不采倍率/精确优化配方）、Appendix E 全 streaming 与 I 全限制。同prompt生成M'>M，再选大多数最短/少数有效最长为GRPO组；过长无效不入long，预算饱和时改shortest-only并收够M valid就取消其余。未显式分类两种reasoning模式；期望长短条件不足以数学保证top-order的reward关系，故不采Propositions的普适正确/深度保持保证。长度variance是历史代理，不是模型uncertainty校准或任务质量。

Token chunks仅让trainer incremental forward/KV提前执行，reward/backward仍要求完整trajectory；不是前缀未判reward即可更新policy。VeRL0.4/vLLM0.8.5.post1/FSDP2.6、GRPO M8、DAPO类共同奖励；Qwen3B–32B/Math datasets，8–64H20，主吞吐500steps；同codebase baseline和组件消融支持局部tradeoff，却不是原rollout分布无偏、所有任务quality等价或生产加速。Fixed-length/稀疏reward局限明确；所有冗余/弃选/取消前缀、profiling/history、controller与KV驻留、完整reward/backward都付费。未核artifact/复现。

实际 Ch36完整读dataflow15565块、ProRL18815双段、Agent rollout28101完整机制/图/限制块，及后“小规模仿真”标题与首双段。现有scheduler不得改语义，而此处明确由algorithm侧改组分布，runtime只执行预算/streaming，有真实差额；全Books精确family无既存。唯一 `TRAIN-DISTRIBUTED-TRAINING`（不再扩Reach3），原6；拟完整28101 marker后、仿真H3前一段（未授写）：

> 长尾也可以从训练组的产生规则处理，而不只移动既定 trajectory 的执行位置：同一 prompt 先生成冗余候选，再选多数短路径和少数有效长路径组成 GRPO 组，用历史长度差异提出各 prompt 的冗余预算；预算饱和时可改成只收最先完成的有效路径并取消剩余候选。[DARTS 的受限分支](https://arxiv.org/html/2605.30859v1)因此改变采样人口与组内 reward baseline，不是保持原分布的纯 runtime 调度。长度 variance 不是校准 uncertainty，保留少量长解也不证明所有必要深度都被保存，固定长度或极稀疏 reward 可能无益。Token streaming 可先做增量 forward，但 reward 与 backward 仍等完整轨迹；冗余/弃选和已取消前缀、profile/历史状态、KV 与完整训练都计费。代理、质量或净预算失配时，保留原采样组、prompt-level 调度与普通 sample streaming，不让较短 rollout 或有限平均准确率批准无偏更新与通用提速。<!-- source-family:SF-2026-ARXIV-2605-30859 -->

## B6 — IRT audit 2605.30504v1：必要证据与逐字 PRE（待 root）

原6/日证保持，当前v2不自动扩审。实际读 [exact-v1](https://arxiv.org/html/2605.30504v1) §3.1–3.6/§4–5 全部必要正文、Eq1/forced-ceiling定义及Table1；未遍历Appendix E全部item。114模型、七benchmark/32subsets共20986原items，tie/constant过滤后19164拟合；先用与人口排序一致项估ability，再固定ability重拟item的d=0与d=1 likelihood差，排序的是异常reference一致模式而非label真值。c/d均可[0,1]、d0可呈下降曲线，不把参数名“upper”当强制单调。弱标签GPT5.4整合strong-model judgments，GPQA在precision评价中默认correct，头部95%非全题人工gold；allwrong/ties过滤人口须另看，不能宣称全库召回。

3.5具名继承label错误与构造规则/无唯一key分开；3.6模型对flagged reference的异常同意只能提出数据/选择审计，没有训练数据不能证明污染/benchmark过拟合因果。模型panel能力跨度、family相关及全局ability跨subset资格决定分辨力。响应采集/justifications、多模型判分、拟合/重复refit、人工回审与谱系维护全费；旧响应可重用不等零历史费用，硬件/precision/完整费用未披露。未核实现/复现。

实际 Ch66 完整读自出题21916双段、Aggregate/多模态交接、排行榜IRT25257完整段/marker、WILD完整双段与GrowingPains全段。现有IRT用于量尺/选题，没有“固定能力后force ceiling对照提议label audit”的分责；全Books精确family无既存。唯一 `PLATFORM-EVALUATION-SYSTEM`，原6；拟25257完整marker后/WILD首段前一段（未授写）：

> 同一响应矩阵也可以用于审计题目，而不只给模型排名：先用与总体排序一致的 items 校准能力，再固定能力，比较每题在 reference 匹配概率的两种强制 ceiling 假设下的拟合，以差额提出优先回审队列。[受限 IRT 审计](https://arxiv.org/html/2605.30504v1)把难题、异常标签和无唯一答案分开，却不使拟合 ceiling 或模型多数成为真值；tie/all-wrong 等过滤人口仍需另审。弱 reference 来自模型聚合，头部精度不是全题人工 gold，panel 能力跨度及跨 subset 量尺失配也会改变排序。继承标签须追溯源题与构造规则，某模型异常同意疑似错标签只触发训练数据/选择流程检查，不证明污染因果。多模型响应、判分、拟合、人工复核和谱系维护全部计费；证据或量尺不稳时，保留原题、Unknown 与独立专家/可执行核验，不由高异常分自动改标签或否定排行榜。<!-- source-family:SF-2026-ARXIV-2605-30504 -->

## B7 — 发现尾差：四项完整题摘准入提案（待 root；未读 Methods）

仅复用本日具名完整原题摘，不扩raw队列。以下尚非确定当窗候选，待日证与root准入；不采用摘要headline收益。

### 30837

身份：[exact-v1](https://arxiv.org/abs/2605.30837v1)；完整原件 [KNOWN6](./SUP_ABSV1_KNOWN6_20261021.jsonl)。Submission history From: Shuhao Zhang [ view email ] [v1] Fri, 29 May 2026 04:49:20 UTC (21,540 KB) [v2] Sun, 14 Jun 2026 19:30:35 UTC (21,540 KB) [v3] Wed, 26 Aug 2026 01:37:37 UTC (4,655 KB)

Title: Send a SCOUT First: Pre-hoc Reasoning for Adaptive Detector Allocation in Prompt-Injection Defense

Abstract: Prompt-injection detectors are heterogeneous: each is strong on a different slice of attacks, and none is always reliable. Yet existing systems still treat detection as a fixed single-detector pipeline, committing every request to one detector's blind spots. We reframe defense as detector allocation: given a heterogeneous pool, decide per request which detectors to run and whether to escalate to an LLM judge. Our framework SCOUT (Scalable and Controllable Outcome-prediction for Uncertainty-aware Triage) makes this decision dynamic by predicting each detector's per-sample reliability and latency from how it behaved on similar past inputs, and exposes a single safety-utility threshold to the operator (where utility bundles benign-pass rate and wall-clock). To evaluate this setting, we build SCOUT-450, a benchmark that captures the structurally complex, agent-facing injections that older prompt-injection sets under-represent. On SCOUT-450, a safety-oriented operating point reduces attack-success rate by 46% and total wall-clock by 40% relative to an always-on GPT-4o judge, at a 5.1-point benign-utility drop. SCOUT also transfers to three external benchmarks (BIPIA, IPI, and IHEval), improving the safety-utility frontier.

具体准入链：固定单detector覆盖各自盲区 → 依据相似历史预测每request各detector可靠度/latency并选择调用/升级 → 重新考虑固定chain与安全/benign utility/时间的联合operating point；拟2+2+2=6，PLATFORM-SECURITY。

### 30916

身份：[exact-v1](https://arxiv.org/abs/2605.30916v1)；完整原件 [KNOWN6](./SUP_ABSV1_KNOWN6_20261021.jsonl)。Submission history From: Justin Hartenstein [ view email ] [v1] Fri, 29 May 2026 07:01:38 UTC (140 KB)

Title: Welfare, Improvability, and Variance: A Principal-Agent Approach to Optimal Benchmark Item Aggregation

Abstract: AI benchmarks have well-documented limitations, with prior work examining contamination, saturation, and construct underspecification. Aggregation has received far less attention: benchmarks are typically summarized by uniformly averaging item-level scores, implicitly treating every test item as equally valuable. We model benchmarking as a multitask principal-agent game and show that the welfare loss from a benchmark is determined jointly by three item-level primitives: alignment with normative welfare priorities, marginal improvability, and performance variance. We translate the theory into an audit framework that ranks items along each of these three axes, and apply it to OLMES items using WORKBank for welfare, the EvoLM 4B suite for improvability, and the PolyPythias 410M panel for variance. The framework surfaces items that are Pareto-inferior within OLMES subject to a pro-worker welfare operationalization. All code is available at this https URL .

具体准入链：统一均分默认各item同价值 → principal-agent中welfare alignment、marginal improvability与variance共同约束聚合失配 → 重新考虑模型开发者激励与benchmark聚合权重，拟2+1+3=6，PLATFORM-EVALUATION-SYSTEM。

### 30808

身份：[exact-v1](https://arxiv.org/abs/2605.30808v1)；完整原件 [KNOWN6](./SUP_ABSV1_KNOWN6_20261021.jsonl)。Submission history From: Fengyu Gao [ view email ] [v1] Fri, 29 May 2026 03:53:12 UTC (1,237 KB)

Title: Differentially Private Preference Data Synthesis for Large Language Model Alignment

Abstract: Preference alignment is a crucial post-training step for large language models (LLMs) to ensure their outputs align with human values. However, post-training on real human preference data raises privacy concerns, as these datasets often contain sensitive user prompts and human judgments. To address this, we propose DPPrefSyn, a novel algorithm for generating differentially private (DP) synthetic preference data to enable privacy-preserving preference alignment. DPPrefSyn is a principled framework grounded in the Bradley-Terry preference model and the intrinsic geometric structure of pairwise human preference data. It first learns an underlying preference model from private data with formal differential privacy guarantees, and then leverages the learned model together with public prompts to synthesize high-quality preference data. It exploits the shared linear structure of per-cluster reward models to effectively capture heterogeneous human preferences in private datasets, and leverages DP Principal Component Analysis (DP-PCA) to improve learning accuracy. Extensive experimental results demonstrate that DPPrefSyn achieves competitive alignment performance under strong DP guarantees. These findings highlight the potential of synthetic preference data as a practical alternative for privacy-preserving preference alignment across a broad range of applications. To the best of our knowledge, this is the first work to generate DP synthetic preference data for LLM alignment. Our code is available at this https URL .

具体准入链：直接使用私有preference暴露prompt/判断 → 共享线性cluster偏好在DP-PCA/DP学习后仅以public prompts合成 → 重新考虑合成释放与alignment消费者的privacy/quality边界，拟2+2+2=6，唯一owner待root在偏好学习链校准，不先双owner。

### 30365

身份：[exact-v1](https://arxiv.org/abs/2605.30365v1)；完整原件 [page2](./SUP_AGENT_NAV_PAGE2_20261021.txt)，本原件为DataCite当前题摘，不冒exact-v1已读，须有限核同身份/事件。

10.48550/arxiv.2605.30365 Mental Damage: Caption Poisoning Attacks on Retrieval-Augmented Text-to-Music Generation
Retrieval-augmented text-to-music (TTM) systems augment underspecified user prompts using captions retrieved from a music caption dataset. This design introduces an integrity dependency on the music knowledge database. We show that an attacker can poison the database by injecting a small number of crafted music captions, causing the system to retrieve malicious captions that bias prompt augmentation and steer generation away from the user's intended function, without modifying the user prompt, retriever, or generator. To achieve the music caption poisoning attack, we propose a dual-layer caption poisoning strategy that preserves high-level retrieval anchors while injecting low-level acoustic descriptors to steer prompt augmentation and downstream music generation toward an attacker-chosen target intent. In a MusicCaps knowledge database, CLAP retriever, and MusicGen pipeline, poisoned generations move substantially closer to the attacker's target, while remaining comparably aligned with the original user query. These results expose a practical integrity risk for retrieval-augmented creative AI systems. Our demo can be found at: https://yizhu-wen.github.io/Mental-Damage/

具体准入链：RAG音乐只测原query alignment可漏攻击 → 保留高层retrieval anchors同时注入低层acoustic steering，原对齐仍高而真实意图移位 → 重新考虑retrieval provenance、目标偏移与相似度验收的安全分责；拟2+2+2=6，PLATFORM-SECURITY。仅防御性边界，不输出payload配方。
