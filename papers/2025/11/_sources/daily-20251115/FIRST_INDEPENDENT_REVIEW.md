# 2025-11-15 首批、日期与有限反侧独立复核

复核者：Codex / Ohm，非作者 Planck。检查时间：2026-10-04T18:50:11+08:00，实际 clock 10:50:11 UTC；首轮18:39:00。

窗口 BJT `[2025-11-14T09:00:00+08:00,2025-11-15T09:00:00+08:00)`。fresh 实际重读 AGENTS、当前研究/Report 合同、每日14来源/按需/arXiv范围、Prompt、ROADMAP及最新checkpoint（仅路由）。只核本日材料，不继承14候选或日期。只写独立notes，不改作者报告、Books、state、月索引，不 stage/commit/push。

**结论：首批准入通过；日期链按下述保守范围修正后可继续。日级未通过，作者必要Evidence/Books普通工作尚未结束。** 本次不是日级ready后的全项采用验收。应用任务列表未暴露Planck/native ancestor可直发入口，未向其他任务误发；本文件是给Planck/root的实际首批回接，校准不需再等root重复同一范围。

## 1. 首批裁决

亲读[首批10个exact-v1完整题摘](raw-arxiv-first-exact-v1.xml)；BuddyMoE接口摘要确实截短，另实际读[HTMLv1](raw-web-10.json) L62～67完整续段及§3必要门控/§4替代说明，不把截短摘要说成完整。原题摘只支持准入，不授全部方法/实验完成。

| 精确身份 | 独立裁决与允许继续的范围 |
| --- | --- |
| Echoing .09710v1 | 通过具体设计反证方向，拟2+2+2=6可保持。Agent间角色镜像、推理投入未消除与定向结构化干预是局部可核增量，不是泛泛多Agent提醒。标准任务完成不等于保持principal/委托目标；60配置/3领域/2000+不能回填未来v3。尚无本批日期证明，保留方向，不展开所有附件。 |
| UGCS .09864v1 | 通过具体checkpoint选择机制，拟2+1+2=5可保持。每样本uncertainty与短窗口hard QA reward排序值得核验，不因成熟早停/模型小自动关闭。后续核uncertainty定义、排序选择集/测试泄漏、窗口和额外成本，不采用“最可靠overall”普遍断言。 |
| TawPipe .09741v1 | 通过固定shard/拓扑分组/overlap相对weight-passing的具体通信机制，拟2+2+2=6可保持。不能仅从24GPU吞吐排名推出所有序列长度/拓扑优越；`TRAIN-PIPELINE-PARALLEL` Ch38是路由，不等Book缺口已证。 |
| Compact CED .09748v1 | 潜在局部资源前沿/实体数字漏检通过。约1B与0.6B失败因子有准入价值，不因英→德任务、calibration/vote成熟而关闭。必须绑定模型、数据、M4 Pro24GB、合并微调/投票及推理成本；不把400ms或“sweet spot”普遍化。日期仍隔离。 |
| PALMS+ .09724v1 | 范围关闭通过。完整题摘的新增是现成Depth Pro/几何floorplan匹配/particle filter的定位实例，未识别改变foundation model表示、训练、VLA控制或runtime主线的机制/失效边界。不是关闭所有depth/small model/robotics研究，不为这项不影响处置的日期续追。 |
| OpenAI for Ireland | 关闭通过。实际读[原核心](raw-web-04.json) L22～37，合作/培训/workshop/mentor/创业支持没有本项目机制、评价反证或安全纠错；[官方RSS](raw-openai-rss.xml)的04:00GMT为本窗BJT12:00，日期明确也不令其准入。 |

另外首批 Audio-VLA、GAD、CP-WBFT、Harli、BuddyMoE 的潜在方向可保留；没有因encoder/agent/GAN组合或摘要没全实验而关闭。CP-WBFT的85.7%仅为待核实验故障条件，不授经典Byzantine理论容错/liveness；Harli的QoS保证、GAD超teacher、Audio-VLA过程真值及Buddy功能等价均未获采用权限。

Buddy必要门控还存在局部文字冲突：原HTML L149禁止`TAE<=tau`替换，固定输入下提高tau才减少允许替换；L214却称low tau为conservative。不得照录低tau保质量或门控保证。日期仍隔离，本次不因该冲突关闭局部quality/transfer取舍方向或要求全artifact；未来采用该具体保证时定点核算法/实现与勘误。

## 2. 新日期证据的裁决

实际读取 [2025官方availability存档](raw-availability-20251101.html) L3683～3741及[原请求/响应头](raw-availability-20251101.html.request.json)、[CDX](raw-availability-cdx.json)；其中说submissions经scheduled announcement公开，final ID/DOI在announcement过程中分配，不能提前发给作者。Thu20 ET规程、2025 deferred名单与真实当日身份一起用，不以submitted单独赋日。

实际读取 [Fri14官方CL recent存档](raw-arxiv-cl-recent-20251114.html) L157～225及条目，核[CDX](raw-daylist-cdx.json)和[receipt](raw-arxiv-cl-recent-20251114.html.request.json)：抓取19:05:53UTC，header为 `Fri,14 Nov2025 (showing first50 of78)`；该recent总447不是当日78，更不是全项目候选。实际解析50个abs身份与36个已选ID，交集恰为16：

`.10645/.10643/.10628/.10621/.10507/.10457/.10381/.10303/.10262/.10232/.10201/.10051/.10029/.09984/.09971/.09966`。

用系统时区规则独立换算：2025-11-13 Thu20 `America/New_York` 为UTC11/14 01:00/BJT09:00，offset=-05:00；capture为BJT11/15 03:05:53。**接受这16项的标准arXiv公告范围组合推定为 BJT `[2025-11-14T09:00:00+08:00,2025-11-15T03:05:54+08:00)`**，capture后一秒仅用于含起点/不含终点记法，不是精确first-public timestamp。实际dated list限定本次公告身份，使之不同于拿一般schedule从submitted推日期；未发现更早非标准公告反证。保留推定性质，有具体反证才撤回，不要求证明作者历来从未预发。

这只解决该arXiv事件的落窗，不批量授16个新家族入选或Evidence：具体更早公开线索（Instella等）、新报告差额、重要revision仍逐项核。未在first50中的20项不能因此判窗外或无贡献；next/CDX有限失败已经停止，不要求重扫月表或所有类别。Echoing/UGCS/TawPipe/CED的日期不由这16项推定。

**不接受DATE_RECOVERY的两条更窄注册上界作为已证明正文公开上界。** 实际核 [Language Drift DataCite](raw-datacite-language-drift.json)、[ParoQuant DataCite](raw-datacite-paroquant.json)：`registered/created`、v1 `Updated`及月粒度`Available`是注册/元数据字段，当前`findable`不证明注册那一秒正文已可公开访问。历史规程支持ID分配与announcement的联系，但不足以认证注册后的具体正文服务可用时刻。两项改用上述真实capture保守上界即可，仍完全落窗，不因此阻止它们继续必要Evidence；无需另循环DOI/OAI补检。

## 3. Language Drift：受限Evidence与实际owner

完整v1摘要已从[第二批](raw-arxiv-second-exact-v1.xml)亲读，实际核心补读[raw12](raw-web-12.json) §2.1～2.6/L85～153、[raw13](raw-web-13.json)与[raw14](raw-web-14.json) §3.1～3.4/Table2～3。本次支持**固定query/prompt/ICL语言而只变gold retrieved context语言的局部诊断及评价分账**，拟2+2+2=6可保持；不采用摘要更强因果或所有语言decoder控制保证。

- 三QA各1000样本、EN/ZH/AR/RU、GPT-4o翻译+人工核，LLaMA3-8B/Qwen2.5-7B、4-shot/default decoding；gold context不代表真实retriever链。Table1翻译后ROUGE与GPT semantic match支持部分错语言输出仍语义相似，但约42.2～62.9%不排除其他理解失败。GPT翻译/judge同源及surface overlap不能证明decoder是唯一原因、英语pretraining频次是受控因果。
- Table3有VRD比PLI差的局部质量与短输出，但并非所有格子都下降。ZH-EN的PLI/VRD/SCD长度104.0/38.6/134.9不是matched token预算；较长CoT不是推理更完整的证据。五独立run不等已披露统计不确定性；runtime硬件/precision/batch/concurrency/SLO/端到端延迟未披露，不能称training-free即零成本。
- §3.1实际是raw logits target乘1.1、distractor乘0.9，不是常数加减。独立计算两token：`(-2,-1)`的target概率0.268941→0.214165，不能保证boost；共同+3保留原概率却使调整后为0.331812，策略有logit平移依赖。该反例通过，不静默把论文改写成additive penalty，也不由此宣布所有局部作者结果无效。算法保证/实现采用需先明确logit convention和语言分组/勘误，不为诊断命题强求全部代码复现。
- 原表与诊断的最小命题可以继续进入最终处置；如作者只采用局部诊断和上述边界，必要Evidence范围本次通过。SCD普遍优越、单调控制、英语吸引子因果、真实retrieval/生产可靠性未通过，不得正面采用。

实际对读唯一建议owner `MODEL-SAMPLING` [Ch20](../../../../../books/part-02-model/20-sampling.md)：`Logit penalties与约束`/processor order、`格式损失要先定位在Prompt还是Decoder`、`工程与评估含义` 已承载启发式vs硬约束、分层定位、格式/内容与长度成本分账。不能因SCD名缺失造缺口。新增可能只是一条受限跨语言retrieved-evidence诊断分支，而非新通用采样机制；作者需明确选择仅报告/具体已有覆盖/向root提出窄差额，再验收实际最终处置。当前不授Book整合或“已有覆盖”最终结果，未写Books、未核POST；不把owner选择未完成伪成外部故障。

## 4. 其余有限准入与重要边界

另外实际读[第二批14](raw-arxiv-second-exact-v1.xml)、[第三批12](raw-arxiv-third-exact-v1.xml)全部完整题摘及[current36 metadata](raw-arxiv-current-signals.xml)。合计36完整v1题摘（Buddy补原HTML）；35作为具体潜在机制/局部反证保留、PALMS范围关闭的漏斗合理，不是35确定当窗候选或35 Evidence完成。EnchTable/MTAttack、CP-WBFT等安全与理论主张不因日期隔离获安全保证；未来accepted/晚版本不倒填，未遍历全版本史或实施攻击。

ParoQuant .10645v1准入通过，拟2+2+2=6可保持。完整题摘及[§4.1原HTML](raw-paroquant-v1.html)已读：每轮pairs互不重叠才允许并行，不同轮顺序仍不能任意交换；多轮rotation加scaling、activation inverse与kernel联合成本是具体增量，不是正交变换成熟等价事实。第一层k_proj的10%pair观察不授全层等效；2.4%与<10%数字仍待作者最低必要评价/实现核，未授标准Evidence或Books缺口。

Instella .10628v1不整体标已审重复。亲读完整题摘与[Table5](raw-instella-v1.html)，以及[March原说明](raw-web-18.json) L51/59～66、[Long/Math必要旧核心](raw-web-19.json)。三seed合并的做法早已披露，不是Nov新算法；v1逐seed均值65.5/65.8/65.6与合并66.6有可继续判断的局部新验证信息。保留该潜在证据，不自动把全报告训练配方/MI300X重新算新机制；未核等预算单run或seed选择，不授无成本集成因果。此项须作者定点完成事件差额/最终准入，v2 submitted11/14不证明公开或重要修订。

其他潜在题摘方向可沿[逐项理由](ARXIV_SCREENING.md)继续必要工作，不为剩余日期项读全部methods。Methodological Pitfalls .10381是position paper，真正拟采用的新反证需核具体示范/结论条件，不能仅把预训练目标与正确性不同这一成熟提醒计高分；没有凭摘要直接关闭它。

分层负侧本次两项：PALMS范围、Ireland机构合作；另核Instella已公开配方的事件去重边界而不关闭新验证，Anthropic纠错侧单独核下节。未把这些样本称全部明确排除项验证；其他明确范围外标题/全部109切片未逐项重读。

## 5. 来源与六部分当前停点

独立解析四实际Atom query/request：12分类、submitted恢复slot、start0/max100/ascending，total与entries为51/6/12/10；都只实际请求start0并已得到全部该query返回，next100未请求，不是另扫100条。主题受限但不保证命名机制召回；109月表标题切片只作查漏，历史CL first50补检没有把余34题摘变队列。查询完整不等public覆盖，未扫Weekly。

[SOURCE_TAIL](SOURCE_TAIL.md)及正式[README](../../15/README.md)有14每日行、有限入口与停止，无应取消的实际触发。额外实际结构解析本日Anthropic与Zai原Next Flight（不执行站点脚本）：

- [Anthropic本日原HTML](raw-anthropic-research.html) 是 `publicationList/Research` 171条，目标附近11/12 18:19Z与11/21 14:32Z之间无本窗项。README的“115个2025日期字段”不是论文数；可窄同步为真实传回Research数组目标段检查，不继续将可解析数组整个说成历史不可读，仍不授删稿/全站保证。
- [cyber原页raw09](raw-web-09.json) L43/56～59实际明确Nov14编辑纠正“thousands per second”为“thousands, often multiple per second”，旧速度必须废弃。修订日粒度/时区不足完全落窗，作者的隔离通过；本次没有采用攻击能力/因果性能结论，也不要求重读完整攻击报告来支持这一纠错。
- [Zai p2](raw-zai-p2.html) 的blogsItems18、hasMore=false、next3与createAt最早Dec7已经实际核，不能根据CMS或其他RSC日期计条目；没有普通page3待办。Seed/Hunyuan/MiMo/MiniMax等此轮主要复用作者明确记录，未重新运行浏览器/抓取；不能把本notes说成14源全部原响应重新验证或最终Source Gate。

六部分均实际读：§1/3当前0确定、35潜在非零事件，分母尚未冻结；§2有限边界基本清楚，需同步真实date/Anthropic数组；§4不冒称全部Evidence/Books；§5明确普通与外部，不能在日期推定通过后仍把16项全部当无可执行工作；§6正确未通过。独立首批返回后作者应更新普通停点，而非把等校准长期标external。

## 6. 给Planck/root的普通回接

1. 立即复用本次首批校准，不等重复回信；两负侧关闭、CED潜力保留不重读。首批三方向仍日期隔离，其余无新增可接受入口时有限停止，不要求全潜力全文。
2. 对16个历史list身份窄同步保守arXiv公告范围，定点核已知更早家族/事件差额并逐项贡献/评分；没有早公开线索的不能因无法证明“从未预发”永久hold。Language Drift和ParoQuant至少可继续，丢弃不必要的注册上界依赖。
3. Language Drift只采用通过的受限诊断，明确最终Books处置；ParoQuant及其余确定拟入选项继续最低必要Evidence/owner。此项工作属于作者，不由独立reviewer代写报告/推进全methods。
4. 同步Anthropic实际数组范围、重要纠错隔离、metadata实际clock及正式六部分，作者ordinary真正收束后交日级ready。本次已做内容有效复用，后续只读新增/变化与全部实际采用命题、重要反侧、最终Books及六部分。

当前V3实际校验exit0；本notes初写后实际30个本地引用缺失0、六个分节/代码块配对正常、no-index空白无诊断（exit1仅新增差异），追加后另核。机器不改变日级未通过。用户已授权本lane独立内容复核，无需等root再审本次准入/日期/Evidence范围；这不替代作者未完成的实际采用项Evidence与最终Books处置。没有日级完成、Books写入或月计数变更。09仍由Carver独立审，本lane不自审09。

## 7. 新到采用包与最终处置局部回核

实际clock 2026-10-04T18:58:26+08:00（10:58:26 UTC），复核者Codex / Ohm仍非作者Planck。已fresh读取当前合同/本日停点，只核新增[ParoQuant必要Evidence](PAROQUANT_EVIDENCE_READY.md)、Language Drift最终处置及正式README变化，复用先前完整题摘、日期与Language Drift核心，不等待root重复校准。

**Language Drift：标准Evidence及最终仅报告通过。** 本次再次实际读Ch20“格式损失要先定位在Prompt，还是Decoder”的现有三路径控制、格式/内容分账及额外调用/tokens/延迟边界，核作者新末节与README§3/4确实只保留gold-context语言切片的局部诊断。新验证仍为6分贡献，不因Books选择关闭；现有判断不需被新案例改写，且SCD乘系数控制保证未证，因而仅报告成立。不授SCD实现/普适因果，Books实际0，无POST需求。

**ParoQuant：标准Evidence及最终仅报告通过，原6分保持。** 本次独立亲读[exact-v1原HTML](raw-paroquant-v1.html)的§4.1～4.3、§5.1～5.3全部三类质量表/在线Table3/消融Tables4～5，以及A.3、A.4完整三GPU表和A.6评价设置；核[请求identity](raw-paroquant-v1.html.request.json)，未执行artifact或实验复现。原有§3第一层观察与完整题摘已核，不重复所有方法附件。

- Eq6独立pairs每通道最多出现一次，只支持轮内无依赖；多轮和scaling仍按顺序执行。Eq9使用原层输入X与已量化前层的X'作output reconstruction，第二阶段同时优化weight/quantizer，不能把全部质量增益归于rotation、将局部loss说成端到端无损证明或任意交换跨轮次序。
- 原质量表有局部提升，也有对FP16/其他方法的退步：Paro/AWQ reasoning Avg61.9/59.5的差为2.4百分点，不是相对2.4%；小样本GPQA/AIME均值不提供普适显著性。A.6实际区分Base模型PPL、三seed reasoning与MMLU-Pro单seed、lm_eval non-reasoning，不能把这些协议合并成同一任务质量或把长序列误差累积认定唯一因果。作者最终采用包没有正面引入这些更强主张。
- A.3校准为H200/PyTorch2.8.0，混合2048/验证64、seq2048、seed0、两阶段10epochs，70B调整batch与学习率；A.4在线为PyTorch2.6.0、compile max-autotune/CUDA Graph、AWQ W4A16 GEMM与自有transform，batch1且三GPU分别报告，二者不能混同配置。Table4/5的stage2贡献与非单调IR质量真实存在。
- 独立重算A6000 1.7B吞吐下降13.125%，等tokens时间增加约15.108%；4B分别9.091%/10%。RTX6000Ada和4090的1.7B同样超过10%吞吐下降，因此“所有模型<10%”不可采用。此换算是表值的条件计算，不是实测E2E latency。输入/输出长度、计时重复/不确定性、并发与SLO仍未披露，不能授生产保证。

实际对读Ch49“Rotation Scope与Quantization Group必须共同进入Numeric Plan”的原正文：scope/group/quantizer/calibration/metadata/kernel成本与回退共同选择；并读“顺序程序拥有语义，Parallel Annotation拥有Schedule”的证明条件边界。现有正文没有逐字承载Paro算法，但本次条件质量/成本验证与可实现pair分支无需强制改变这些已有设计判断；作者保留具体分支/参数/负侧于报告的**仅报告**选择成立，不将泛主题相似冒充新增算法已有覆盖，也不按名称缺位强造Book差额。Books未写，无POST待办。

交Planck：上述两项最终采用/处置可直接复用通过，删去等待root核同一范围的普通停点；其余14个已获日期权限身份继续作者最低必要Evidence/事件差额，准备好即可分批交本复核者，不等完整宽池。当前README仍在进行中、分母未冻结，**本次只两项通过，不授DAY**。未核其他14项全部核心、全量潜力methods或剩余明确排除项；后续DAY只汇总已有有效校准与实际新增采用/重要反侧、有限来源和最终六部分。

写后机械反馈（实际clock 2026-10-04T19:00:33+08:00）：本notes 33个本地引用缺失0、代码块配对及no-index空白无诊断。新README V3 exit1是普通格式同步：两行公开时间栏须各写纯`2025-11-14T09:00:00+08:00 ～ 2025-11-15T03:05:54+08:00`，不掺BJT前缀、说明或“同上”；两行审阅结果栏须为精确枚举`标准完成`，受影响反例/通过说明放§4/6。这不推倒日期/单项语义通过，亦不由reviewer改作者报告。最终DAY前需作者修正并重跑实际校验；不得沿用旧exit0。

## 8. 新14项必要Evidence实际回核与两处局部同步

实际clock 2026-10-04T19:25:40+08:00，Codex / Ohm，非作者Planck。亲读[14项采用包](ADOPTED_EVIDENCE.md)各自精确v1必要方法、采用表/关键反侧及成本附录；不是把作者“已读”标签当独立证据。完整题摘、16项保守公告范围及前两项有效复核继续复用。当前README日期/审阅枚举已修为纯字段，不重开已过日期链。

已实际核GAD §2/3.1/3.3/A.2/A.3的BT/GRPO与选checkpoint，Instella §3/5/6.1/Table5的三seed/merge，SSR §3.2/3.3/4.1/4.3-4.6/C.2，AdvancedIF §3.1/4.2-4.4/5.1/5.4/5.5，State Tracking §3/4/6.1-6.3，Position §5-7，Rectify OPS/Eq4-8/设置/消融，MTR §3.1/3.2/4.1.3-4.1.4，VocalNet §2.1-2.2/3/4/Tables2-3，EffiReason §3/Eq1-2/4.4-4.5，GraphIF Methodology/Rewrite/实验消融，ScaleFormer §3-5，NumPert §3-6/8，REAP SP/FE/实验消融/成本附录。实际E3重算A=.4736842105、r_acc=.9、r_tok=10、E3=1.6513761468，确实不是质量不可补偿gate；未核也不否定其未采用的灵敏度定理。

关键反侧与收窄通过：冻结D长度hacking不是所有hacking消除；seed合并非免费且并非所有单项最好；posthoc分解非内部过程真值；AND平均胜出不覆盖CC；初态捷径与交换/整数任务分开；toy circuit不证明真实唯一机制；BI=0不保证低错误；IF表为1至1-10的累计平均而非第10轮单点；拒绝90至91不支持全部能力退化；VocalNet Table3仅训练MTP质量，不孤立归因联合首块延迟；GraphIF调用/文本变化非图唯一因果；ScaleFormer用future context且decoder随输出T增长不获全系统线性；NumPert两类标签/不同人口及量化/API不合并；REAP Table4只正确轨迹轮数，不能当全人口成本。

给Planck/root两处普通可执行窄同步，修后只核变化，不重读全包：

1. SSR采用包的“10次重复、Acc/Maj@5协议”请写明Table1的LR-Acc为10次、LR-Maj@5为50次（5并行样本）。这不证明所有HLE评价也使用同一重复数，未披露部分保持未披露。
2. MTR采用包/README§1/4中“前assistant历史使用真值”请显式限定到§3.1 turn segmentation/dialogue-quality评价分支。原文§3.2.2-3.2.4另外构造synthetic feature/IF/safety协议；本次未核代码证明它们均teacher-forced，不能把这一限制自动覆盖所有表。Table6正常68至41.9/打断69至42.3、Table7拒绝90至91的受限数值判断继续有效，均是累计轮次平均，不是末轮单点。

实际对读当前Ch31 policy-relative reward、Teacher/未来RM反馈、独立Evaluation及Bottleneck；Ch80 verification-centric/有用feedback；Ch66 AND/EvalSpec/任务generator切片/质量匹配；Ch24 factorization/teacher forcing/serial depth；Ch75 scope/expiry及typed graph validator/commit；Ch22有损aggregation/raw fallback；Ch79 observation-triggered replan/执行失败与计划失败；Ch76 retrieval-packing-generation质量链。14项仅报告的具体分支/局部新验证理由成立，不说算法逐字已有覆盖、不按名字缺位强造Books。Books实际0，无POST需求。上述两处是表述权限窄修，不推倒14项标准必要Evidence及OnlyReport内容通过。

日级尚未授予：剩余独立工作是有限14来源原返回/停止点与最终六部分，不扩19个日期潜力项methods，不代作者写报告，不改共享Books/state/index。作者收到此notes可立即修两处并更新局部ready。
