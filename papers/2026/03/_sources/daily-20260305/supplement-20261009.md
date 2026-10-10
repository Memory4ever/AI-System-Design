# 2026-03-05 增量补查

补充窗口：2026-03-04 ～ 2026-03-04（北京时间完整自然日）。执行：2026-10-09 04:05～04:14 +08:00。仅本日 README 与本日 sources；无 Books、LS、索引、stage、commit、push 写入。

运行前原件为 `baseline-before-supplement-20261009.md`。原24候选、评分、日期、窗口与连续§4保持；其有效必要 Source 与 POST不重读。旧09:00公告推定和旧ledger统一owner-contract标签不授新日期/贡献证据。月份目录、Submitted、API published/updated及DataCite注册不得直接作为first-public。

## 实际来源与停止点

所有下面原件均保存于本目录；读取 `SUP_FETCH_*.json` 可核URL、执行时刻、响应身份与失败。`SUP_*.raw`为响应原件，`.txt`为可读抽取；无摘要的官方事件以核心说明判断。

| 来源 | 本轮实际检查与停止 | 结果和边界 |
| --- | --- | --- |
| SRC-OPENAI | `SUP_OPENAI.raw` RSS1257项仅过滤BJT03/04，3项；2篇新增核心403后web恢复于 `SUP_WEB_OPENAI.json` | Learning Outcomes/Axios关闭；graviton复用有效AIforScience关闭。非全站/删除项保证。 |
| SRC-ANTHROPIC | `SUP_ANTHROPIC` Research可见10条，`SUP_ANTHROPIC_ALIGNMENT`的March卡片；新增露出coding-audit-realism/AuditBench官方日期为Mar23/Mar10（对应两份SUP原件） | 窗外；Abstractive/Challenges及A3有效身份/日期结果复用，不重做正文。有限目录，不授全历史覆盖。 |
| SRC-GOOGLE-AI | DeepMind旧discover路由丢分页、`?page=3`仍当前页；一次恢复真实 `/blog/page/3/`，卡片20、3/19页，March/Feb跨窗；相邻官方Flash-Lite Mar03、AlphaGo Mar10原件另存。Google March `?page=2`末页2/2只有Mar06 SpeciesNet与Mar04 Bayesian | 日期落点原稿已核；Bayesian旧Nature Jan07发表/重述关闭有效复用，无重要修订信号。非全机构覆盖。 |
| SRC-META-AI | `SUP_META` HTTP200，抽取仅标题；当前Research壳页仍没有dated Mar04研究片段 | 受阻隔离：需可访问官方Mar04目录/具体dated原稿，壳页不是no-hit。 |
| SRC-QWEN | `SUP_QWEN` public retrieval返回40项无total/page，检查全部标题与extra.date，Feb16→Mar19跨窗 | 有限40元数据无Mar04事件。旧多日期冲突继续保留，不赋予整体历史保证。 |
| SRC-DEEPSEEK | `SUP_DEEPSEEK`可见Research10项，Feb25→Jun24跨窗；News5项ViewAll未开 | 有限Research切片无Mar04条目，非删除项/全机构证明。 |
| SRC-MOONSHOT | `SUP_KIMI`全部可见19条，Feb09→Apr20跨窗，底部至2024 | 有限可见目录无Mar04条目。 |
| SRC-TENCENT-HUNYUAN | 首次publicList默认英语9项，不冒充“全部”；按已恢复页面参数POST pageNum1/pageSize20/renderType0与accept-language zh，`SUP_HUNYUAN_ALL.raw` code0/totalNum11/list11，Feb13→Apr23跨窗 | 全部当前可见11项日期无Mar04；显示/发布字段仍分离，不授删除项保证。 |
| SRC-ZAI | `SUP_ZAI` Research当前可见15卡，Feb21 GLM5TR→Mar15 Turbo跨窗，查看更多处停 | 有限切片无Mar04条目，不展开窗外正文。 |
| SRC-BYTEDANCE-SEED | `SUP_SEED` type1/year2026/page-token20/count100/order_desc false，实际14项、total82、next40/has_more true；Feb27→Mar26，Mar01→Mar12跨窗，next40处停 | 有限跨窗切片无Mar04条目。与旧18行目录差异保留，不继承旧页面数量，也不追全82；metadata非论文首公开证明。 |
| SRC-BAIDU-ERNIE | `SUP_ERNIE` page1/2可见10项；Feb06→Apr15跨窗，page2未开 | 只限实际切片，无Mar04卡片。 |
| SRC-XIAOMI-MIMO | `SUP_MIMO`全部8 Paper卡：Feb03→Mar13；一次 `SUP_MIMO_BLOG`仍仅Dec16 release body | Paper有限切片已检查；Blog受阻隔离，需官方Mar04 archive slice/dated原件，现壳页非no-hit。 |
| SRC-MINIMAX | EN/CN主blog实际切片，Forge EN Feb14/CN Feb12→M2.7 Mar18；`SUP_MINIMAX_AGENT`现在列Sep19/Sep22/Oct08共3条 | 新目录露出没有恢复Mar04历史；Tech Blog继续外部隔离，需Mar04 dated archive/originals；不扫所有当前指南。 |
| SRC-ARXIV | 4实际主题API start0：language135/max250、multimodal41/max250、agent12/max250、system41/max100；均total=returned到末，ID集合与旧有效主题原件一致。Submitted范围仅发现：前三03/02 19Z～03/03 18:59Z，system03/01 00Z～03/03 18:59Z。主题/同义词与分类可直接核 `SUP_FETCH_api.json`、`SUP_FETCH_system.json`。月份列表首次短格式404，一次恢复 `/list/cs.CL/2026-03?show=1000`及DC/show250，实际只浏览ID02200～03399有限标题片段（CL88/DC16 metadata blocks），不把下载页面或宽库存作逐项题摘队列。 | 7份选定v1完整题摘；6潜力未核必要公开日，1作者早日公开。月份/ID/submitted不是Mar04确认，不能授无遗漏；不调用catchup或失败advanced日表单。 |

按需：BeyondSWE作者官方GitHub只为具体日期恢复；ACL/PMLR/Google官方结果仅为已具名身份恢复，未扫描会议或每周组。轻量检查本轮7份exact-v1官方事件当前可见撤回/纠错说明，无withdrawn标记；后续v2/当前正式发表不反填v1，也未据此认定重要修订。

## 完整题摘与增量判定

7份独立完整v1题摘实际读完：`SUP_ABS_CODAR`、`ACE`、`DIAGRAM`、`CONTROL`、`BEYONDSWE`、`VLA`、`PAREVO`。它们不是候选分母；6项是潜力与日期保留，1项窗外。原24项有效审阅不重复计数。

| 身份 | 原文具体潜力／处置 | 当前必要缺口与恢复条件 |
| --- | --- | --- |
| 2603.02547v1 CoDAR | continuous DLM落后不只归diffusion路径；controlled token-recovery定位rounding，再改contextual AR discretizer。改变discretization与并行生成成本的比较，非只凭更好分数。潜力保留，MULTIMODAL-GENERATIVE-PARADIGMS。 | `SUP_ABS_CODAR`仅Submitted Mar03；`SUP_WEB_DATE_1`一次检索无dated作者原稿/公开公告。请求官方first-public日期或作者dated发布，日期后只审rounding干预/AR成本，不读全文解决日期。 |
| 2603.02945v1 ACE-Merging | data-free合并不能观测task covariance；FT参数差估covariance、closed-form解可能改变无数据条件的合并选择。理论假设尚未核，不因旧“单任务/owner未变”标签关闭。潜力保留，TRAIN-SFT。 | exact-v1事件仅Submitted Mar03；一次检索为March转载/后续CVPR，不给首公开日。需官方当时公开公告/dated作者原稿。 |
| 2603.02865v1 Nodes/Edges | 合成图probe观察node已于vision表示但edge只于text stage线性可分；可能修正“vision encoder已含可读取完整关系”的判断。linear不可读≠不存在，局部信号不自动EX。潜力保留，MULTIMODAL-REPRESENTATION。 | 仅Submitted Mar03与转载复写；一次恢复无官方首公开日期。需dated作者公开稿/公告，返回后核probe/数据与因果边界。 |
| 2603.02578v1 SteerEval | coarse controllability可能掩盖fine-grained退化；三域三级评价提供粒度依赖反例信号，不能仅因benchmark关闭，也未把新层级名当机制。潜力保留，PLATFORM-EVALUATION-SYSTEM。 | `SUP_WEB_DATE_2`发现ACL July与作者全年publication，无Mar04首公开证据；官方abs是Submitted。需具体公开公告/dated作者原稿，再审粒度控制/评价混杂。 |
| 2603.02271v1 VLA edge | MolmoAct-7B action-generation memory-bound与Orin/Thor局部反例可能改变edge算力/带宽预算；100B模拟不当实测。潜力保留，MULTIMODAL-EMBODIED-VLA。 | 原Submitted Mar01不是公开日；Google Research官方结果只有2026，辅助Mar04索引非primary日期。`SUP_WEB_DATE_PRIMARY`定点官方页仍无日。需官方首公告或作者dated公开稿；不复活旧09:00/8分。 |
| 2603.02510v1 ParEVO | Work-Span primitives筛数据、库语义SFT与race-detector反馈改变训练支持/反馈的可能性；题摘未归因各部件，106×不独自准入。保留信号，不把成熟组合自动EX或直接授贡献，潜在TRAIN-DATA/AGENT-WORKFLOW。 | 一次 `SUP_WEB_DATE_PAREVO`只有arXiv Submitted Mar03与后续PMLR July；需官方首公开公告/dated作者发布后定点裁定actual increment，再决定评分，不先读全文。 |
| 2603.03194v1 BeyondSWE | search augmentation可能退步是贡献潜力，但作者GitHub News明确Mar01 benchmark/SearchSWE发布、Mar03论文on-arXiv（`SUP_WEB_DATE_PRIMARY` L225–230）。按官方日期窗外，不以later indexing搬到Mar04。 | 本日无日期请求、无评分/Books、不声称归属日已审；恢复真实事件日时再核搜索负作用的对照。 |

新增官方核心两项：Learning Outcomes Measurement Suite和Axios均官方Mar04，RSS原值00:00GMT/BJT08:00。前者核心给教育RCT/ITT与五类测量组件，但学生长期认知并非模型/Agent系统机制；自然语言指令、classifier/grader组合尚无新有效性条件或验证结论，15%领域考试增益不授AI系统增量。后者新闻编辑、摘要、样式及prompt标准化是应用案例，没有新增可采用机制/失效边界。二者贡献前关闭，无评分/Books。独立代表校准已发root，未借官方声望或已有owner倒推贡献。

新增精确日期保留6项各只请求一次，身份/理由/一次恢复在上表。旧02277外部日期与03099证明争议保留冻结历史，不追新时分秒、不重开全文；本轮当前02277 exact-v1页仅Submitted，未新确认公开日。Meta/MiMo/TechBlog目录隔离同样不支持无遗漏。

## 当前停点

确定新增候选0；6项潜力被必要公开日期隔离，不是零命中。无新增必要正文/Books待写；普通来源、题摘、证据及Books可执行待办0。root已实际读7份完整题摘、Learning核心L31–97/Axios L33–69并通过首批校准，认可6项潜力/精确日期保留、两Blog关闭及BeyondSWE作者Mar01/Mar03公开日期窗外；随后实际核14源有限停止点、新查、四Atom总数/返回135/41/12/41、混元中文11/11、一次必要日期恢复与外部条件，全部六部分增量DAY通过。原有效16 POST复用、原24行/窗口/连续§4冻结，不授新日期证据、不重开Adam中心争议。

完成态验证：V3报告校验通过；baseline对照原24行全部保留、原窗口保留、连续§4完全相同；45条本地文件链接无缺失；本日报与来源目录限定工作区及暂存区diff检查通过。有限机器检查不证明无遗漏或替代语义DAY；无stage/commit/push，不领他日。
