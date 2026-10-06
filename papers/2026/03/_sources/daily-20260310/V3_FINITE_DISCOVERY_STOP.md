# 2026-03-10 有限发现与停止位置

执行：2026-10-02；作者 mar01_v3。唯一窗口为2026-03-09T09:00:00+08:00→2026-03-10T09:00:00+08:00，含起点、不含终点。机构14源的实际入口、页停点、结果与限制在正式README §2；本文件只补充被引用的查询、选择身份和具名负侧，不建立第二份完成账本。

## 主题查询

端点 https://export.arxiv.org/api/query；所有查询 sortBy=submittedDate、sortOrder=ascending。UTC Submitted缓冲用于发现线索，不等同公告时间；3/6 19:00至3/9 18:00覆盖Friday deadline后的下一公告可能集，但早作者稿、延迟公告、旧Submitted仍是限制。返回当前版本元数据后，选中身份另开exact-v1完整题摘；不是把返回版本号当本窗首次公开。

Systems查询：

```text
submittedDate:[202603061900 TO 202603091800] AND (cat:cs.CL OR cat:cs.LG OR cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:"large language model" OR all:"distributed training" OR all:"speculative decoding" OR all:"kernel" OR all:"inference")
```

start=0/max_results=80返回80；start=80/max_results=200返回91/total171，停止171。原始元数据为[V3_ARXIV_SYSTEM_THEME_0.json](./V3_ARXIV_SYSTEM_THEME_0.json)及含完整query/URL的[V3_ARXIV_SYSTEMS_TAIL_STOP.json](./V3_ARXIV_SYSTEMS_TAIL_STOP.json)。初次巨大XML工具输出截断，重取安全元数据投影确认80与91，未把截断当已读全文。

Learning/architecture查询：

```text
submittedDate:[202603061900 TO 202603091800] AND (cat:cs.CL OR cat:cs.LG) AND (all:"Transformer" OR all:"mixture of experts" OR all:"language model") AND (all:"optimization" OR all:"scaling" OR all:"representation" OR all:"attention")
```

start=0/max_results=200，返回116/116，停116；完整query/URL/title投影见[V3_ARXIV_LEARNING_ARCH_STOP.json](./V3_ARXIV_LEARNING_ARCH_STOP.json)。

Multimodal查询：

```text
submittedDate:[202603061900 TO 202603091800] AND (cat:cs.CV OR cat:cs.RO OR cat:cs.CL) AND (all:"world model" OR all:"vision language action" OR all:"video generation" OR all:"multimodal foundation")
```

start=0/max_results=200，返回34/34，停34；见[V3_ARXIV_MULTIMODAL_STOP.json](./V3_ARXIV_MULTIMODAL_STOP.json)。

Agent/evaluation查询：

```text
submittedDate:[202603061900 TO 202603091800] AND (cat:cs.AI OR cat:cs.MA OR cat:cs.IR OR cat:cs.CL) AND (all:"language model" OR all:"LLM") AND (all:"agent" OR all:"retrieval" OR all:"evaluation")
```

start=0/max_results=200，返回150/150，停150；见[V3_ARXIV_AGENT_EVAL_STOP.json](./V3_ARXIV_AGENT_EVAL_STOP.json)。Learning/Multimodal批量输出曾截断，已分别重新取得完整116/34元数据投影；不是116/34篇题摘或证据审阅。

四查询重叠，不相加为论文数。宽旧库存只用于有界相关标题查漏（Systems前65、Multimodal前55、Agent前70个相关标题线索），不逐项生成题摘/全文队列，不继承旧1205/33候选或评分。无每周/会议全站、repo/release或AI for Science扫描。

## 完整题摘选择与隔离

作者完整读取以下16个exact-v1官方题摘，四个弱侧另定点core消歧；没有其余元数据全部题摘已审的断言：

| 精确身份 | 当前贡献层处置 |
| --- | --- |
| [Covenant 2603.08163v1](https://arxiv.org/abs/2603.08163v1) | 动态开放peer实际训练参与/结果接纳边界potential；非72B或chain名贡献 |
| [EAGLE-Pangu 2603.08088v1](https://arxiv.org/abs/2603.08088v1) | branch/commit、安全索引、fused/eager接口potential |
| [Ares 2603.07915v1](https://arxiv.org/abs/2603.07915v1) | step成功标签/history routing预算potential；反事实与选择偏差未授 |
| [SlowBA 2603.08316v1](https://arxiv.org/abs/2603.08316v1) | 动作正确但资源退化的安全反证potential |
| [Native Retrieval 2603.08429v1](https://arxiv.org/abs/2603.08429v1) | query生成后的head成本/embedding质量potential；§3.1–3.4/§4.3/Table1定点核，不取消query生成 |
| [RoboRouter 2603.07892v1](https://arxiv.org/abs/2603.07892v1) | §3.2/§4.3/Table5的历史检索/Evaluator控制差异potential；有引用纠错依赖 |
| [PIRA 2603.08013v1](https://arxiv.org/abs/2603.08013v1) | §5/§6.2/Table2同框架clean/noise对照potential；intent不是行动授权 |
| [OfficeQA 2603.08655v1](https://arxiv.org/abs/2603.08655v1) | §3/AppD3/§4 oracle解析与file/vector/table-header条件potential，非只benchmark增项 |
| [NEST 2603.06798v1](https://arxiv.org/abs/2603.06798v1) | network/memory feasibility与DP搜索联接potential |
| [Swimba 2603.06938v1](https://arxiv.org/abs/2603.06938v1) | expert参数空间混合保持单state recurrence potential |
| [CAMEL 2603.08022v1](https://arxiv.org/abs/2603.08022v1) | capacity×mixture拟合及跨scale固定预算分配potential；不采用55B外推保证 |
| [LiveWorld 2603.07145v1](https://arxiv.org/abs/2603.07145v1) | 未观察实体持续演化而非静态观察memory potential |
| [KohakuRAG 2603.07612v1](https://arxiv.org/abs/2603.07612v1) | ordering/retry/blank-voting的数值引用对照potential，不仅排行 |
| [Governance 2603.07191v1](https://arxiv.org/abs/2603.07191v1) | 两cascade IR/FPR及资源取舍potential；不以四层成熟标签准入 |
| [SoK 2603.07379v1](https://arxiv.org/abs/2603.07379v1) | 贡献前关闭：题摘POMDP/taxonomy/agenda未建立新机制有效性证据；§IX风险引用旧研究，不泛化所有SoK |
| [Caller Identity Confusion 2603.07473](https://arxiv.org/abs/2603.07473v2) | 最新v2官方撤回：experimental methodology flaws与unresolved ethical data collection；仅保排除依据，不评分/Books |

14potential不是确定当窗候选：首8 live DOI完整字段见[V3_DATACITE_FIRST_BATCH_RAW.json](./V3_DATACITE_FIRST_BATCH_RAW.json)，后6 live字段投影见[V3_DATACITE_TAIL_DATE_FIELDS.json](./V3_DATACITE_TAIL_DATE_FIELDS.json)。均client=arxiv.content/state=findable；Submitted+官方deadline给最早下界3/10 08:00BJT，registered转BJT+1秒作不含上界。全14区间跨09右端；created/Updated不是公告精确时间，registered也只给上界。正式README §5逐项列原值、所缺材料和重开条件，不评分、Evidence或Books采用。

官方实际批次有限恢复到/list/cs.DC/2026-03-10、/list/cs/2026-03-10?show=2000、/list/cs.CL/2603?skip=1000&show=1000，工具cache miss；已有月目录目标ID定点查找不提供具体日批次。旧scheduled_match文件依created+schedule推定，原文明确月目录不证明day first-slot，本次未继承。一次id_list补请求timeout后用exact-v1 abs成功读选择身份；不扩大附件队列或继续公告代码考古。

RoboRouter [v2](https://arxiv.org/abs/2603.07892v2) 3/10T02:21:36Z撤回comment说incorrect reference papers需移除；[v4](https://arxiv.org/abs/2603.07892v4)6/24恢复、当前header无withdrawn，不能称全家族当前撤回。v1重开须日期与该引用纠错影响范围，不只补日期即默认采用。Caller v2 7/21撤回是检查时官方纠错信号，不是本窗新贡献；定点搜索Books及旧本日README的ID/title没有采用链，未改共享Books。

## 官方核心负侧与身份去重

| 事件/原始入口 | 实际范围与关闭依据 |
| --- | --- |
| [Promptfoo](https://openai.com/index/openai-to-acquire-promptfoo/) | core22–39；RSS3/9T10:00GMT=18:00BJT落窗。收购与未来Frontier integration，没有披露新安全机制/受控评价，不因安全标签准入 |
| [AuditBench Blog](https://alignment.anthropic.com/2026/auditbench/) | Blog core及[2602.22755v1](https://arxiv.org/abs/2602.22755v1) intro/§4.2身份核；tool→agent gap三原因、56×14×4/13工具与release已在v1公开。本次重呈现关闭，不说旧研究无价值 |
| [Abstractive Blog](https://alignment.anthropic.com/2026/abstractive-red-teaming/) | core12–43及44–59，唯一[2602.12318v1](https://arxiv.org/abs/2602.12318v1)完整题摘：category search/CRL-QCI两分支及7×12评价已2/12公开，本次无独立机制，不为month-only重呈现穷查日期 |
| [AlphaGo回顾](https://deepmind.google/blog/10-years-of-alphago/) | 3/10 header/core123–169；旧AlphaGo/Zero与已发模型/科学应用、AGI愿景，没有新受控机制 |

AuditBench不是逐字重复：Blog Qwen3-32B而v1为14B，当前核心无32B受控新增适用边界，不采该32B结论。SAE案例Blog KTO与v1 §4.1 SFT不一致原样保留，不解释成新实验、不开全v3diff/repo。AuditBench v3 Submitted3/9T18:35:46Z已过Monday18:00UTC deadline，最早3/11 08BJT，不反填本窗。本表两篇旧论文AB仅身份去重，不计主题16。

## 已做独立检查与停止

root实际完整读取首8官方题摘/历史、四官方负侧必要core、SoK完整题摘、RoboRouter v2comment/v4header与Caller撤回comment；作者的弱4core不冒称root全文深审。新增6potential完整题摘仅作者已读，root未逐项重读。本日冻结确定候选0，候选证据0/0，Books新增/已有覆盖0；无Books改动需POST。

作者可执行发现/消歧/有限恢复已结束，root实际检查本记录与正式六部分的最终非作者日Gate通过，普通待办0。14日期项与机构历史入口缺口为外部终态保留项，不支持正面证据、Books或无遗漏断言；只按正式README §5具体条件定点重开，不因新找到论文扩新波。
