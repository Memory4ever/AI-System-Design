# 2025-09-22 独立扫描与交接（作者 James，进行中）

窗口：2025-09-21T09:00:00+08:00 ～ 2025-09-22T09:00:00+08:00。按当前研究合同 §2–6 / Report 合同执行；不继承其他 Daily 的候选或处置。

## 已执行入口

执行时间、URL、状态与原始响应见 `fetch-results.json`。本日独立取得 OpenAI RSS、Anthropic Research、DeepMind Research/Blog page 5、Google publications/2025-09 Blog、Meta Research、Qwen、DeepSeek 更新、Kimi Blog、Hunyuan Research、Z.ai Research、Seed papers、ERNIE Blog 两页、MiMo、MiniMax 中英文 Blog、arXiv availability。OpenAI Research 403；不能把 RSS 等同全 Research 历史全集。

Seed 本日实际请求 type2、type1 的 2025 API，见 `seed-fetch.json` / `SEED_API_TYPE2.json` / `SEED_API_TYPE1.json`：type2 返回 15/49、has_more=true、next_page_token=20；非置顶条目已跨过本窗到七月，Blog 可在第一页停止。type1 total94 但没有 sub_article_list，不是零论文。Hunyuan 正确 publicList API 的新响应见 `HUNYUAN_LIST1.json`，list11/totalNum11 仅恢复当前列表，不证明 2025 历史覆盖。

## arXiv：实际范围与失败边界

十二分类主题查询（分类按来源清单；language/foundation/world/vision-language model、Transformer、LLM、GPU 同义主题）以 submittedDate 202509181800～202509191800 获取发现线索。原始两页 `ARXIV_QUERY0.atom` / `ARXIV_QUERY100.atom`，totalResults172、start0/100；172 是提交索引发现库存，不是本窗候选或全文队列。初页 URL/执行时间见 `arxiv-query-fetch.json`；第二页继续相同查询 start100，已实际取完剩余72项。

各分类 `/list/<cat>/2509?skip=0&show=2000` 实际 urllib404（包括 cs.CL）；ISO 路径 `https://arxiv.org/list/cs.CL/2025-09?show=2000` 成功，保存 `cs.CL-2025-09.raw`：首2000/2214。此页面按月罗列 ID，没有可见逐日公告头；用于查漏，不因此扩大为2214篇待办。工具/路径差异保留，不能把旧路径404授为全部 arXiv 不可达。

官方 availability 说明公告周日～周四20:00 US Eastern。本窗含周日2025-09-21 20:00 EDT（北京时间22日08:00）的计划公告，但计划日历和 submitted 字段本身都不能证明某 ID 当批公开。高级搜索试验原响应保留：`ARXIV_ANNOUNCED_SEARCH.raw` 同日起止报表单错误；`ARXIV_ANNOUNCED_SEARCH2.raw`、两次补查询日范围返回空。**前一原响应第468行明确说明 announcement date supports only year and month granularity**，故日范围空响应不支持无事件判断，也不是已完成日级公告重建。

## 首批准入待 root 校准

下列19项均已实际读精确 v1 的完整标题、摘要和当前版本历史/说明，原页 `<ID>v1.abs.raw`、下载记录 `abs-fetch.json`。目前缺必要首公开上界/当批公告证据，**不评分、不列为确定22日候选、不授深入审阅完成、不进入 Books**。首公开证据如果完全落窗，即交 root 独立准入校准；若更早公开，定点回真实 owner，不扩本窗。

| 精确身份 | 原有约束 → v1 实际潜在增量 → 待重新考虑的选择 |
| --- | --- |
| 2509.16203v1 Inverting Trojans in LLMs | 离散输入和目标类自然相关词造成触发反演误报 → 贪心离散反演、激活余弦隐式黑名单及置信检测 → 不能把目标响应命中直接当后门触发证据；安全反侧需保留 |
| 2509.16198v1 RPG | 自然语言长期 repo 计划难维持依赖 → capability/file/dataflow/function 的持久图联合计划并测试生成 → 图状态能否改善依赖保真，而非仅多个 Agent 分工 |
| 2509.16197v1 MANZANO | 理解连续表示与生成离散表示相互牵制 → 同编码器双 adapter 的混合视觉 tokenizer、AR语义加diffusion像素 → 联合理解/生成冲突是否须完全独立编码器 |
| 2509.16189v1 Latent learning | 参数学习不能自动储存未来任务无关经验 → oracle episodic retrieval 的 reversal/navigation 反例与 within-example ICL 条件 → 检索改善泛化的训练先决条件；不授真实检索器性能 |
| 2509.16187v1 MatchFixAgent | 既有测试易假称跨语言翻译等价 → 语义分解、生成执行测试及冲突人工核样 → 评价应核未发现的不等价而非只测试pass；潜在增量是评价反证，不是多Agent组合本身 |
| 2509.16149v1 Visual sycophancy | 拒绝误导的SFT也会拒绝正确纠错 → modality gap及SRT反思区分误导/纠错 → 降迎合不能只优化一侧拒绝指标 |
| 2509.16127v1 BaseReward | 多模态RM构建各因素未区分 → paradigm/head/data/backbone/scale/ensemble系统实验及真实RL验证 → 数据混合与head选择是否改变静态RM到policy收益；待核归因，不照录SOTA |
| 2509.16117v1 DiffusionNFT | reverse轨迹似然限制solver/CFG → forward flow matching的正负样本隐式policy改进，仅clean images → diffusion后训练是否必须存整采样轨迹；25倍数字待绑定可比协议 |
| 2509.16105v1 DiEP | uniform专家剪枝忽略层间冗余 → 可微全局非均匀layer pruning → 相同专家预算下层分配是否改变质量/内存取舍 |
| 2509.16088v1 Randomized Smoothing Meets VLMs | 生成序列没有离散标签证书 → 有界错误oracle将生成映射离散动作/语义类及采样半径理论 → 认证保证依赖oracle假设而非任意生成安全 |
| 2509.16072v1 I-FailSense | 动作执行成功但偏离语言目标 → semantic-misalignment数据与跨hidden-layer FS ensemble → failure detector须分别检验物理失败和语义错误 |
| 2509.16060v1 SABER | 对齐层拒绝不等模型不可被改写 → 白盒extra residual跨层绕过安全且perplexity变化小 → 常规能力/perplexity不是安全保持代理；安全反侧不可排除 |
| 2509.16293v1 ByteRobust | 大集群中失败定位和恢复时间吞掉有效训练 → 训练并行特征驱动容错/故障定界，报告9600GPU三月97%ETTR → 高ETTR来自哪些诊断/恢复约束，不能只以集群规模准入 |
| 2509.15965v1 RLinf | 异构RL stage静态共置/拆分均会空闲 → temporal/spatial M2Flow、adaptive worker通信、context switch/elastic pipeline/profile排程 → placements应随阶段资源结构改变；仅意外打开HTML并读intro/§2.2，不是完整证据审阅 |
| 2509.15940v1 Arnold | 稀疏突发collective与物理拓扑错配 → topology alignment scheduling及生产9600GPU 10.6%结果 → group spread是否足以解释端到端收益，待原实验控制 |
| 2509.15937v1 VLAC | 真实机器人reward稀疏/手工 → goal条件观测对progress delta/done、负样本、critic/policy统一token、分级human loop → dense reward收益与人类介入预算须拆开 |
| 2509.15932v1 Alignment Bottleneck | feedback受通道容量限制 → 匹配mixture/loss下Fano与PAC-Bayes上下界 → 新标签是否能跨容量边界，须核定理的同risk/同分布条件，不授普遍对齐不可能 |
| 2509.15915v1 Foundation Models as World Models | FM直接policy与作为simulator的作用混淆 → text GridWorld对照不同复杂度/部分观测/stochastic条件 → 局部证据可能修正两种角色选择，不因toy环境排除 |
| 2509.15763v1 UniGist | sequence KV丢token会损害细节 → chunk-free gist训练、gist shift kernel及真删除compressed token → 压缩质量和实际KV可释放是否一致 |

## 仍可执行 / 外部必要材料

- 普通工作：完成机构本日解析、按ROADMAP收窄后的相关题摘初筛及代表排除记录；已下载宽库存不等于必须逐项关闭，但已查看相关/含糊标题仍需完整题摘。
- 必要日期：上述19项及后续符合贡献项需要本窗官方公告或可支持完全落窗的原公开区间。arXiv高级搜索只年月，不以submitted或DataCite注册直接伪造first-public；尚未取得支持上界的证据。
- 候选日期/贡献成立后：root首批准入，作者按§4–5读必要证据并比较实际owner/邻接，精确Books建议交root；最终日级复核root承担。

上述为先前停点；后续实际工作与当前作者handoff见下段。不是终态零事件。不改Books/月索引/LEARNING_STATE，不stage/commit/push。

## 后续有界检查与当前 handoff

本日机构解析已执行完实际可见切片，不继承21日结果：

- OpenAI RSS按本窗pubDate无条目；最近09-22 08:45 GMT合作项在截点01:00 GMT之后。Research403局限保留。
- Anthropic172个publication对象恢复至 `ANTHROPIC_publications.json`，publishedOn原值保留；9月可见09-05/15及后续09-26，没有本窗对象。不是172篇本日事件。
- Google September Blog首12项从09-30跨至09-11；本窗两侧09-19/23。Publications仅年级日期仍不授历史日级覆盖。DeepMind page5的6个9月标题只作路由；FSF核心已实际读，原字段09-22、Updated04-17-2026，当前正文包含2026 v3.1 TCL内容，不能冒称全为2025 v3.0。原页 `DEEPMIND_FSF.raw`。另外天文/流体为暂缓AI for Science题义关闭；Robotics09-25、ICPC09-17、VaultGemma09-12不扩本窗。
- Meta首查空文本后本日实际 `site:ai.meta.com "September 21, 2025" research` / `"September 22, 2025" research` 首返回页恢复official global_search page5。`META_P5.raw`当前publication切片11月→09-15夹本窗（页面其他类型不同排序，不以全站连续排序授覆盖）。定点 `META_ARE.raw` 完整题摘已读：ARE/Gaia2异步环境暴露静态评价漏掉的失败、reasoning-efficiency和budget plateau，具有潜在评价贡献；原字段September22时区未给出，不列确定22日候选。不再把Meta写成“无可恢复目录”。原请求 `source-narrow-fetch.json`。
- Qwen首页09-23→08-19，Kimi可见Blog09-16/05、ERNIE实际1/2与2/2的09-12均窗外。MiMo目录09-19即使采用常见民用时区的整天范围也早于本窗开始，不将它记22候选；未核first-public。DeepSeek updates及 `DEEPSEEK_TERMINUS.raw` 核心已读，09-22 date-only没有时区，修复语言混合/random characters及Code/Search Agent可靠性属于正确性信号，必须保留，不能只因未披露架构排除。
- Z.ai本日首15项 `ZAI_items.json`，实际page=2 `ZAI_P2.raw`/`ZAI_P2_items.json` 累计18唯一ID、hasMore=false、最早2025-12-07T16:00:00.000Z。两页是当前目录停止依据，不是9月恢复。Hunyuan全部API11/11仅当前，Seed type2 Blog15/49跨至07-15，type1缺sub_article_list；这些实际API结果见本日原记录，不保留未执行可见分页。
- MiniMax本日英文首页与 `MINIMAX_P2.raw` 同批12个dated items，最早10-27；`?page=2`不是换页。中文本日13项10-27→01-15有限夹窗；当前13项不能授完整历史。Agent Tech Blog及官方llms.txt也实际新取 `MINIMAX_AGENT.raw` / `MINIMAX_AGENT_INDEX.raw`，当前只1篇2026-05-13及对应agent-team路径；未见可执行历史分页。停止这两个有限可见切片，取得历史目录/具名事件后重开，不以现在的入口推定2025不存在。

### 月目录查漏与题摘补读

已保存的cs.CL月目录只对ID 2509.15330～2509.16203这一相关发现切片浏览68个标题；这个ID范围不作为公告日期证明，也不遍历整个2214项。新发现10个相关/含糊标题的API id_list实际429，随后每个精确v1.abs实际200并读完整题摘及可见Comments/Submission history，见 `month-supplement-fetch.json`、`month-abs-fetch.json` 与对应原页。没有可见撤回/纠错标记；不遍历全版本史。

| 精确v1 | 具体判断（未评分；公开时间仍缺） |
| --- | --- |
| 2509.15430 BiRQ | 外部HuBERT labels与BEST-RQ效率冲突→复用中间层自标注、raw anchoring防collapse、一阶bilevel/Gumbel选择→标签质量与训练成本的替代设计，保留潜在贡献 |
| 2509.15485 mucAI BAREC | ordinal高惩罚错误→conformal sets内概率归一加权→QWK与coverage/rank选择可能不同；保留局部评价/决策增量，不以阿拉伯语任务机械排除 |
| 2509.15577 R2U | retrieval relevance非generative utility→回答正确概率的process supervision/distillation重写→RAG检索与生成目标错配，保留 |
| 2509.15579 Chunk SSL | whole-utterance预训练不适合streaming→chunk依赖/group masked loss承载million-size FSQ→表示分辨率、流式训练与内存取舍，保留 |
| 2509.15701 APA | 高PCC非良好ordinal consistency→PCC0.9与SCC0.6、phoneme-level失败→局部评价代理反例，保留而非笼统“领域指标”排除 |
| 2509.15789 UPRPRC | 语料获取/对齐不可复查→GAPA段落图对齐与single/distributed路径→对齐可靠性/复现与预算的潜在数据机制；不是仅因713M新数据准入 |
| 2509.15793 RAVE | 完整题摘为retrieval+relevance/credibility signals用于claim-detection，收益仅CT22/PoliClaim分类指标；未提出改变foundation/Agent机制或评价判断的具体新增约束，贡献前关闭，日期不另追 |
| 2509.15837 Visual grounding | 跨音文表示更相似可能只是word identity→speech phonetic dominance未提升semantic discriminability→grounding相似度不能代理语义收益，负面局部证据保留 |
| 2509.15896 Psychology of Falsehood | 完整题摘为human-centered misinformation survey与未来neuro-behavioural方向，没有明确可核的新模型机制/替代设计或修正现有判断的实验；贡献前关闭，不以survey标签独自排除 |
| 2509.15540 Beyond Words | bidirectional text/image decoder+mixed-scale masked-image组件用于desire/emotion/sentiment指标；题摘未给组件收益的新成立条件或失效证据，单个F1提升不足准入；贡献前关闭 |

原主题两页172条已经浏览标题并对相关/含糊项读完整API题摘；这不表示172项均已贡献审阅或确定当窗。API可能返回当前v2/v5等，精确身份/题摘/原published、updated保留在 `ARXIV_query_entries.json`，不采用后版为9月证据。十九项精确v1表保持有效；其余相关题摘只支持发现潜在机制/反证，尚未取得本窗公开区间或历史版本的，不改成排除或深审完成。例如CodeRAG检索-生成对齐、BEFT低数据bias适配、MatchFix评价错判、Red Teaming多模态伤害、Sa2VA absence误报、PCCL通信、CoopQ跨层量化、Cache Bandit hetero-query成本，均保留条件性恢复，不因负面/局部/理论而关闭。当前宽库存不成为全文队列。

余三个先前含糊题目完整API题摘也已读：2509.15748v2研究Gaussian receptive-fields/Lie滤波与biological simple cells，未建立learned foundation representation/系统机制的直接关系，范围前关闭；2509.15565v1为point-cloud/object-map几何data association的Bayesian多解分布，不是foundation/world-model机制，范围前关闭；2509.19370v1 Meow是metadata→outline新任务数据及常规SFT+RL，未给相对workflow的新机制/成立条件或评价反证，贡献前关闭。未把这些日期未核项说成已审重复。

### 当前限制与重开条件

普通作者工作0：本日可执行已知入口/分页、已查看相关含糊题摘与具名原记录已保存。**不是无事件或全量筛选证明**。必要arXiv历史公告/首公开上界尚未取得，已实际检查官方排程、两页提交主题索引、ISO月目录、日路径失败和advanced announcement日查询不支持日粒度的原说明；不以submitted或DataCite registration补造first-public。该缺口隔离为本窗外部保留，不授候选、Evidence或Books。若取得官方当批列表/公开公告或作者原文的完全落窗区间，仅重开对应ID的日期、精确版本及§3–6，不把172条默认全体深审。安全/纠错/反证项不得随访问成本排除。

ARE、Terminus缺本次event的原时区/完全落窗区间；可接受官方原公告/原站存档，不要求补秒级但须完全落窗。没有可用的官方社交原帖恢复：本日定点 `site:x.com/deepseek_ai "Terminus" "Sep 22, 2025"` 与 `site:x.com/GoogleDeepMind "Frontier Safety Framework" "Sep 22, 2025"` 首返回页未恢复官方记录；搜索未命中不证明不存在。FSF此前日期/3.0缺口已由下段原证窄恢复，不沿用旧缺口；仍先交root准入校准，再按安全约束深入受影响内容，不采用2026政策替代2025。

上述是日期窄恢复前的作者ready建议，因下段新证据仅重开FSF，不能继承为当前整日作者完成。最终具名DAY由root承担，本日保持进行中。作者未改共享Books/月README/LEARNING_STATE。

### FSF原日期字段窄恢复：交root准入

本日 `DEEPMIND_FSF.raw` 原HTML（并非新造日期）实际同时含 `<meta content=2025-09-22T00:00:00+00:00 property=article:published_time>` 和BlogPosting JSON-LD `datePublished:2025-09-22T00:00:00+00:00`，`dateModified:2026-07-06T10:24:42.972966+00:00`。此前仅读展示日期而称“时区未给”错误，现按原值保留，北京09-22 08:00在本窗。未取得证据证明它是CMS日期补零，不能自行降格或机械再索秒级证明；交root独立日期/准入校准。

已真实恢复官方原版本入口 `https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3.pdf`，原文标题Version3.0、PublishedSeptember22,2025，16页。实际读取了封面、Overview及§1开始的core，不冒称完成深入审阅；下载原记录 `FSF3-fetch.json` / `FSF_3.0.pdf`。改版Blog含2026v3.1不再替代它。

拟入选一句链：原外部部署安全审查不足覆盖内部大规模模型R&D与失控风险→3.0新增harmful-manipulation、exploratory misalignment及内部部署safety-case约束→重新考虑能力评估/部署授权边界；只采用原政策明确规定，不宣称控制保证成立。等待root首批准入，之后按具体安全约束强制深入受影响§1/2/4/5、实际Books owner/邻接并交精确建议。此项普通作者工作尚未完成，整日ready暂撤；其余有效来源/题摘记录保持。

准入必要定位补充：3.0 §1.6印刷p7、§3.1 pp12–13限定为达到ML R&D CCL的外部与大规模内部部署，不是所有内部模型或进一步研发；§4 p15的misalignment CCL仅探索性说明，没有显式风险接受标准，CoT监测也不是控制保证。实际已读这些准入核心及相关限制，不把核心定位标为深入完成。原有链中的“失控风险”只能指新增探索性评估方向，不能将它与已生效部署门槛合成同一保证。root应同时校准该收窄及代表排除RAVE、Beyond Words、Meow；这些完整题摘的排除依据在上文，不因日期未定而冒称已审重复。当前待root FIRST-FSF-22，不自授准入或DAY。

### root FIRST-FSF-22通过后的必要审阅与Books交接

root实际核原HTML两个带时区发布字段、3.0封面/Overview/§1/§2至harmful manipulation，确认08BJT落窗与新增治理约束准入；明确3.1不能反推3.0、exploratory misalignment无risk acceptance criteria、policy不是有效性实验。此为局部FIRST通过，不替代其他潜在项或最终DAY。

评分 `2 + 2 + 2 = 6`：DD=2是大规模内部ML R&D部署审查与探索性阈值边界的实际规定，不是成熟原则借分；SR=2跨能力评估、部署与治理决策；DU=2可复用的部署范围/审批状态区分，未授长期基础理论3分。因安全约束变化，按研究合同§4深入受影响内容，不以6分减免。

精确源：[官方3.0 PDF](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3.pdf)，本日原下载 `FSF3-fetch.json` / `FSF_3.0.pdf`；本地标准PDF解析派生 `FSF_3.0.extracted.txt`，以PDF印刷页与节定位。作者实际读Overview、§1/2相关治理与限制、§3–5；没有运行政策实现或复现实验。

必要证据位置：§1.6 p7区分misuse外部部署、ML R&D外部/大规模内部部署及进一步研发；§3.1 pp12–13规定达到ML R&D CCL后的safeguards/safety case、具名治理职能审查及material update复审；§3.2 pp13–14区分加速与全包成本可比的团队自动化门槛，并说明权重/工作流、行业采用与创新成本；§4 p15及§1.2 p4/§1.6 p7限制misalignment为illustrative，无显式risk acceptance criteria；§5 p16规定框架适当性/遵循情况复评与披露。§2.2.3 pp10–11的harmful manipulation是探索性严重规模风险，不是一般说服或所有交互风险。

采用边界：这份原政策支持“谁在什么条件下须审什么”的规范性公开事实，不支持实际control有效、残余风险可量化为零、CoT忠实或已阻断全部失控。§3.1自称能可靠阻止不可接受风险属于厂商预期而非实验结论；本文没有配对实验、独立风险估计或实现执行审计。workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator对本次规范性命题不适用；若要采用有效性主张，必要实证协议与结果为Not Disclosed，当前不采用。现有原Blog改版说明只确认版本变动，未见原3.0撤回，未遍历全版本史。

实际owner比较（只读，无Books写入）：`PLATFORM-SECURITY` [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 的“从 Model Capability Gate 到 Deployment-context Residual Risk Loop”（当前约2149行）已承载threat model→capability→deployment controls→mitigation validation→named residual-risk decision→refresh及厂商自评限制；“Safety Evaluation 的单位是 Run，不只是 Prompt”（约762行）已承载covered training runs与独立release；“CoT Monitor 是 Policy-bound Sensor，不是 Authority”（约843行）已区分surface/faithfulness/outcome，不重复推导。相邻 [Ch71 tenancy](../../../../../books/part-06-ai-infrastructure/71-multi-tenant.md) 拥有principal与隔离，[Ch73 production](../../../../../books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates) 拥有各生命周期Gate。已经实际读取以上段落与前后交接；不以主题相似作已有覆盖。

建议窄整合：在Ch72现有Residual Risk Loop的Meta v2说明之后、验证mitigation三问之前补一段“部署范围与准入标准状态”。无需新owner。差额为：内部caller身份不推出低风险部署；达到ML R&D门槛的内部大规模使用也可能需要独立deployment review；风险域/阈值的存在不意味着已定义可签发的acceptance rule。后两点当前上述具体正文未明说；通用闭环与CoT sensor边界已有覆盖。

建议自然段（交root选择、不是已写正文）：

> 部署语境也不只区分公开与私有服务：内部研发系统一旦取得大规模执行和能力改进权限，仍可能需要独立的部署安全审查。Google FSF 3.0把达到ML R&D CCL的外部和大规模内部部署列入safety-case审查，同时将进一步研发与部署门槛分开；这是一项公开治理规定，不是控制有效性的实验证明。由此推导的平台检查应保存使用目的、规模、能力门槛及对应审批范围，不能仅因caller属于本组织就沿用低风险放行。
>
> 准入规则还应标明哪些阈值已经绑定风险接受条件、哪些仍是探索性诊断。该版本的misalignment CCL没有显式风险接受标准；发现一个类别或启用监测，都不能替缺失的授权判据签发许可。增加部署分层、证据复评与治理审查会付出评估预算和变更延迟；范围或前提未确认时应收窄可用能力、部署规模或交人工决策，而不是由模型自签安全。低风险、规模受限的既有路径仍可保留；监测的观测和权限边界链接本章现有CoT Monitor论证，生命周期Gate继续交给Ch73。

此段最后的记录/收窄/回退是作者工程推断，不声称FSF规定任意组织相同控制。root可在确认必要证据和实际owner差额后落实；若裁定差额已有具体正文承载，改为具名已有覆盖，不为制造diff改书。作者普通研究已完成；root证据/Books裁决、实际写入与写后检查、代表排除和日级DAY仍待办。外部日期/目录保留维持原隔离，不授正面Evidence或覆盖。

### 新恢复Qwen：FIRST-QWEN-22局部重开（FSF结果不变）

13:14北京本日独立新请求官方 `https://qwen.ai/api/page_config?code=research.research-list`，实际60原ISO对象，原响应 `QWEN_CONFIG_RECOVERY.raw`。只按本窗筛出两项（`qwen-window-config.json`），没有遍历其他58正文；实际请求两个tokenLinks均200，见 `qwen-recovery-fetch.json`，原tokens和派生核心分别 `qwen3-omni.tokens.raw/.core.txt`、`qwen3-tts.tokens.raw/.core.txt`。每次切回已完整重读AGENTS、当前研究/Report合同、Prompt、ROADMAP、Daily/arXiv来源及Sept checkpoint路由。此前首页不完整的来源差额被实际修正，不沿用shell/首页hold。

Omni：原date=`2025-09-21T21:00:00.000Z`，北京22日05:00，落本窗。核心Introduction/Architecture/Performance文字与变更理由实际读完。准入链：旧speech生成/渲染的block等待限制首次可播放输出→Talker每步AR主codec frame，MTP预测同帧残余codebooks，Code2Wav逐帧合成→将语义AR/帧内残余预测/波形渲染的等待与提交边界分离。拟准入1家族，owner候选MULTIMODAL-GENERATIVE-PARADIGMS，表示交接留Ch23；MoE与AuT本身不是借成熟知识加分。211ms/507ms是Blog宣传，精确v1摘要234ms为theoretical cold-start first-packet，协议不同不能合并，不授实测生产延迟、跨模态无回退或所有任务SOTA。root FIRST后才评分并读必要精确版本机制/配置/反侧、比较实际owner差额。

版本恢复只针对Omni：先前23发现时取得官方截点前README路径commits，ae5dbf9e734b7c72c1a70805cfb321b5fa3e9615的author/committer date=2025-09-22T16:05:18Z晚于22截点，因此不能将该commit当22 first-public或完全当时artifact。其 `assets/Qwen3_Omni.pdf` 本日05:15:33Z实际200、4146178bytes，保存 `Qwen3_Omni_ae5dbf9.pdf` 和 `qwen-omni-version-fetch.json`，未称读完。只支持明确具名版本的机制补证；必要22原版本若不同仍保留差异，不用main猜回。可以用原Blog已公开机制收窄采用，不能以晚commit为理由否定官方05:00 date或猜CMS回填。

TTS Flash：原date=`2025-09-21T20:00:00.000Z`，北京22日04:00。Introduction/全部Key Features/Language Support/Performance/变更理由实际读完，不声称播放全部音频。披露17speaker/10language/方言支持、large-scale训练tone适配，以及“several architectural upgrades and acceleration strategies”但没有具体codec/objective/execution变化。表中同称dual-GPU却Flash12 concurrency对旧6、single97ms对200ms/full420对733/RTF0.30对0.43等，没有hardware/workload/length/quality目标/SLO控制，也未指出新的可比质量-资源边界或评价反证。该原披露范围拟贡献前关闭，不因机构/版本/单数字准入；不是以缺少实验细节关闭一个已明确的新增机制。没有发明其与Omni共享架构；不拿后续2026报告补本次新机制。root请核该代表排除，若发现原核心具名新约束则只重开TTS，不扩大月份。

当前：FSF单项作者ready保持；整日作者ready及普通0撤回，只重开本日Qwen两项局部准入/Omni必要证据，等待root FIRST-QWEN-22。正式仍1FSF候选，Omni未自评分，Books实际0；root证据/Books/DAY权责不变。23的独立FIRST包已经另日保存，不将它的五项候选套到22。

### root FIRST-QWEN-22通过：Omni必要审阅与日级作者ready

root实际读两原日期对象、两core全文，并在 `INDEPENDENT_QWEN_CALIBRATION.md` 通过Omni准入、关闭TTS当前贡献。Omni评分 `2 + 2 + 2 = 6`：DD=2是帧内codec预测与波形等待的机制变化；SR=2跨Talker和renderer的生成/交付接口；DU=2是可复用的时间依赖与码层依赖区分。不借SOTA、MoE或机构声望加分。标准审阅已完成；为拟owner差额定点深入受影响机制与反侧，不将全部模型评价变成全文队列。

精确源/身份：本日原配置和Blog tokens（date=2025-09-21T21:00:00.000Z）支持本窗发布；[原Blog](https://qwen.ai/blog?id=qwen3-omni) Architecture明确每步一帧、同帧MTP残余码与增量Code2Wav。已取得且实际读 [ae5dbf9 PDF](https://raw.githubusercontent.com/QwenLM/Qwen3-Omni/ae5dbf9e734b7c72c1a70805cfb321b5fa3e9615/assets/Qwen3_Omni.pdf) 封面/题摘、§2.1–2.5 pp3–7、§5.2 pp13–14及直接限制；同一必要机制又由 [2509.17765v1 HTML](https://arxiv.org/html/2509.17765v1) §2.4–2.5/Table1–2核对。原请求 `omni-targeted-artifacts-fetch.json`，保存 `QWEN3_v1.raw/.txt`；PDF解析 `Qwen3_Omni_ae5dbf9.extracted.txt`。Git版本时间晚于22截点，arXiv submitted也不是first-public；两者是明确具名的后续补证，**不证明报告全部内容在Blog首发时已相同**，不新增或挪动论文首次公开事件。

旧方案核对只因本项比较必要，定点取得 [2503.20215v1](https://arxiv.org/html/2503.20215v1) §2.4/Streaming Codec Generation完整段落和Fig4文字：Flow-Matching DiT→mel→BigVGAN，用两块lookback、一块lookahead维持局部上下文质量，已经是chunk streaming，不是整句完全离线等待。原 `QWEN25_v1.raw/.txt`。新Blog所说增量是允许首codec frame进入renderer；不得把旧方案的存在理由抹掉或把Thinker-Talker/chunk prefill说成本次新发明。

必要机制：Talker主干AR预测当前帧的第0码本，MTP再产生**该帧**残余码；精确报告§2.5把MTP写成lightweight fixed-step autoregressive dense transformer，而非未来时间帧独立并行。Code2Wav causal ConvNet只读左侧上下文，降低旧block-context等待；时间帧仍沿历史依赖。报告说明chunk prefill沿用旧方案，Thinker完成当前chunk后Talker异步消费，同时Thinker预填下一个chunk。这些是可支持的接口/调度说明，未读代码、未运行、未复现；“MoE普遍降低KV IO”“更高音质”未由单因素对照确立，不采用其因果保证。

延迟口径与反侧：报告Abstract/Table1–2是cold-start、no prior context、**theoretical first-packet**，非网络/排队/客户端播放端到端tail SLO。Table2把尾包预处理、Thinker TTFT、Talker TTFT、MTP、codec各项相加；音频单并发72+88+57+14+3=234ms，视频547ms。1/4/6并发音频234/728/1172ms，视频547/1517/2284ms；RTF0.47/0.56/0.66是单token依赖总时间除80ms，不代表首包不受并发影响。正文“prefill/TTPT largely unaffected”与该表明显不一致，保留而不照录。Blog211/507ms未给同配置，不与报告234/547ms合并、替代或取最优。Table2明确30B-A3B Thinker、3B-A0.3B Talker、80M MTP、200M codec、vLLM、torch.compile/CUDA Graph；hardware、precision、batch组织、输入/输出长度、质量目标、完整SLO和evaluator具体版本为 `Not Disclosed`。没有旧renderer同模型/训练/预算的配对消融，不能把延迟或质量全部归给MTP/ConvNet。

直接质量反侧：§5.2主要text-to-speech而非完整实时对话评估；Table13中文WER Qwen3为1.07、CosyVoice3为0.71，英文1.39对1.45，并非全面最好；Table14德语WER0.777高于ElevenLabs0.572，中文SIM0.772低于MiniMax0.780；Table15若干to-zh/to-ja切片也不胜CosyVoice3。这些只是作者受限测试，不推出全部语言自然度或clone稳定保证。§5.1长video的position extrapolation/context限制也明示；本次不采用无跨模态退化、SOTA数量或40分钟理解作为必要知识。未试听所有音频、未核所有图片或私有训练集。

实际owner与邻接已读：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 当前语音段约660–672行已承载reasoning/speech交错、ARIA prefix-rate、RVQ residual层级与时间降采样层级的区别；约1520–1529行承载音乐粗细分解、coarse错误回退和已播放prefix不能rollback。现有ARIA段点名RVQ/MTP/因果codec，但未展开帧内fixed-step AR与renderer lookahead等待的不同责任；不能把这当未来帧并行。相邻 [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 约265–286行拥有表示/时间粒度、conditioning及Talker表达接口；[Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) world-state不由流式音频取得真值权限。没有修改这些文件。

Books建议为**窄整合，交root裁决**：在Ch24现有reasoning/speech交错段之后、ARIA prefix-rate段之前自然补一段，后接现有RVQ/时间层级区别，不开新owner，不重复SOTA表。必要证据是本窗Blog Architecture +具名PDF/v1 §2.4–2.5/Table2与旧v1 §2.4，后续报告细节不伪装为首发事实。若root认为现有正文已足以承载，可改具体已有覆盖，不为了diff必写。

建议自然段（工程推断与公开机制分开，非已写Books）：

> 流式语音还要分清时间帧与帧内码本的等待。旧chunk renderer保留lookahead以恢复局部声学上下文，本就可以逐块输出；另一个分支让Talker按时间自回归地产生每帧主码，再用固定步数的轻量AR模块补齐同帧残余码，交给只读左上下文的波形decoder。它解除的是首帧合成前的block-context等待，不是把未来多帧或同帧所有码本都变成独立并行。码本容量、残余预测、codec匹配和跨模块buffer仍需训练与计费；首包各依赖阶段的费用也不会因稳态RTF小于1而消失。因果renderer或codec质量不合适时，原chunk/lookahead和专用TTS路径仍合理，已播放音频更不能靠后续修订回滚。

建议段的兼容性/费用/回退是从公开接口导出的工程推断，不冒称原论文验证所有平台。性能表及协议反侧保留在本日报，不塞进自然段作普适数字。

**22作者停点更新：正式2家族必要审阅2/2；root必要源/owner独核后实际两处正文已存在。James非Books写入者 [Omni POST](OMNI_BOOKS_POST.md)通过；[FSF POST](FSF_BOOKS_POST.md)因CCL触发与safety-case material update对象缺失未通过，尚不能把Books2授落实通过。** root新增七项必要风险/反侧core的普通作者工作现已7/7补读，读域、原响应和中心争议见 [RISK_CORE_SUBSET.md](RISK_CORE_SUBSET.md)；James在这七项是日报作者，不自授独立Evidence。普通未读0，交root校准必要反侧与最终DAY；不把date hold免审。本日保持进行中，FSF窄修后再核POST。外部arXiv/ARE/Terminus日期与有限历史目录隔离原样有效，不评分、不授候选；此前Qwen未执行/待FIRST停点已被实际结果取代。TTS关闭不评分，重开条件仍是披露新机制或可比协议，不以领域排除。
