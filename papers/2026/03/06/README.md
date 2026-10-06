# Daily Research — 2026-03-06

**规范：** V3
**窗口：** 2026-03-05T09:00:00+08:00 ～ 2026-03-06T09:00:00+08:00
**窗口说明：** 用户授权保留原候选日期与原窗口，仅补遗漏，新增检查前一BJT完整自然日；旧候选只去重，不搬移归属。
**补充窗口：** 2026-03-05 ～ 2026-03-05
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-09T04:38:23+08:00

## 1. 结论

本轮按用户“保留已有候选日期、原窗与原证据，只补遗漏”的授权，独立检查 BJT 03/05 完整自然日。[运行前原文](../_sources/daily-20260306/SUP_BASELINE_20261009.md)已先保存；原14候选行、评分、日期及原§4连续正文逐字保留。以下三段是原窗有效结论，不代表本轮补查已验收。

本窗确定候选14个唯一家族：12篇 arXiv v1、GPT-5.4 发布/安全说明一个家族及 CoT controllability 研究一个家族。必要机制、评价与直接反证已读；13项得到受限采用结论，DPPO 中心无偏主张与确定性剪枝实现仍冲突，保留争议，不用于正面证据或 Books。8项可能有贡献但首次公开下界不足，另列日期隔离，未评分、不计候选。宽563库存只作有界查漏，不继承旧20候选、评分或563逐项完成声明。

长期差额集中于：检索输入和转录的归因、外存/隐式场景状态、量化浓度与方向分解、执行图的缓存资源计划，以及评价 sensor 与 effect authority 的分离。实际已窄写12家族、9个 owner 文件；Memex(RL) 的核心取舍在 Ch77 已有覆盖，无 diff。GPT-5.4 按需工具定义部分由 Ch78 已有覆盖，其本次新增仅写安全策略作用粒度。全部12家族实际正文及邻接经非作者 root 源→正文 POST 通过；Memex已有覆盖、DPPO争议隔离及本日最终独立复核通过。普通待办为0，外部保留项不支撑正面证据或无遗漏。

所有14个每日来源均已实际尝试；有限可见目录与历史子入口受阻分开记录，保留项不支撑“无遗漏”。未进行实验复现、生产部署或全附件审阅。

本轮实际尝试14个Daily入口，有限主线查询及相关题名查漏后，新增完整题摘判断34项：32项有具体机制/条件/反证潜力但 first-public 日期未恢复，精确隔离；DBenchBio、LilMoo 两项贡献关闭。官方 Mar05 另读4条原窗09时前 OpenAI 核心，均贡献关闭；Anthropic UE Blog与02/26同家族无新差额，不重复评分。确认新增候选0、新增Books差额0；旧有效源及实际POST复用，不重审原分母。Google、Meta、MiMo及arXiv具体外部缺口不授 Coverage/Evidence 通过。root非作者完整DAY通过，普通待办0；完成仅指安全终态。

## 2. 来源覆盖

执行仅限原窗与上述补充自然日、来源清单主线；[旧有效停止与负样本](../_sources/daily-20260306/V3_SOURCE_NOTES.md)保留原依据。下表为本轮真实停止；[首次入口](../_sources/daily-20260306/SUP_OFFICIAL_WEB_20261009.json)、[官方恢复](../_sources/daily-20260306/SUP_OFFICIAL_RECOVERY_20261009.json)、[子目录停止](../_sources/daily-20260306/SUP_SUBDIRECTORY_STOP_20261009.json)及[API逐行/BJT记录](../_sources/daily-20260306/SUP_API_STOPS_20261009.md)保留 raw。四组 arXiv 主题覆盖语言/训练、系统、视觉世界模型及 Agent；不扫描每周来源。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI |Research142行及本轮RSS748k；仅Mar05八item：10GMT三条旧两家族、09GMT旧教育关闭、00GMT四条新核心Excel/AdoptionChannel/FiveValue/Wolfsburg；四条贡献关闭，停止日期切片 | 已检查 | 当前RSS不证明此前作者从未公开，不遍历全部feed |
| SRC-ANTHROPIC |Research56行＋官方域主题检索；Mar05 UE Challenges/Hopes官方核心及所链2602.20400家族；旧就业关闭复用，不反复追日期 | 已检查 | UE同家族无新增差额；不外推完整机构历史 |
| SRC-GOOGLE-AI |DeepMindResearch309行、Google pubs1269行只有限相关题名；March archive p2及DeepMindBlog p3本轮InternalError，旧有效DM邻接3/10→3/3、WAXAL关闭复用；官方域主题补检停止 | 受阻 | GoogleResearch March p2必要历史切片缺失；当前辅助失败不抹旧有效源 |
| SRC-META-AI |Research实际0行；官方域Mar05/2026模型/训练/Agent定点主题补检停止，未得可恢复目录或原文 | 受阻 | 空目录/搜索零结果不能证明零事件 |
| SRC-QWEN |旧Blog36行、新Blog0行后真实article/retrieval官方API40条题名/extra.date，02/16Qwen3.5→03/19MaxPreview，无03/05；API未提供续页token，停止返回40 | 已检查 | 不推断未返回历史；旧PR2021窗外隔离复用 |
| SRC-DEEPSEEK |en/news39行，Research index10行，02/25DualPath→06/24V4；News当前首屏至Apr24，停止未展开ViewAll；有限可见研究行无03/05 | 已检查 | 不外推隐藏/删除历史 |
| SRC-MOONSHOT |Kimi当前Blog155行/19研究条目至2024/06，02/09AgentSwarm→04/20K2.6；停止可见19条，无03/05 | 已检查 | 旧platform109行截断不作为永久缺口，不保证未列历史 |
| SRC-TENCENT-HUNYUAN |Research shell后实际publicList POST zh page1/size20/renderType0，total11/list11；publishedAt及display逐行BJT，02/13→04/23(display)/04/27(published)，无03/05；停止一页全部当前返回 | 已检查 | 日期字段不互当first-public，不授整个历史无遗漏 |
| SRC-ZAI |Research175行，02/21GLM5→03/15Turbo；停止可见目标邻接，无03/05；查看更多以下Dec历史未展开 | 已检查 | 不外推隐藏/删除历史 |
| SRC-BYTEDANCE-SEED |Research86行/public_papers164行后恢复官方articleAPI：type1/year2026/token20默认locale 14行，root另核x-tt-locale: US 18行，两者总82/next40，BJT02/27/03/01/03/02→03/12均无03/05；type2/token0 9行，总23/next20，BJT02/14→04/01；停止已返回目标邻接段 | 已检查 | locale影响可见条目；count100不等返回全年，目录日期不代替first-public，不授完整历史覆盖 |
| SRC-BAIDU-ERNIE |中文Blog68行，02/06ERNIE5→04/15Image；停止可见邻接，无03/05 | 已检查 | 不授全GitHub/机构历史覆盖 |
| SRC-XIAOMI-MIMO |Paper338行02/03HySparse→03/13ARLTangram；Blog15行无日期More shell；官方域主题补检停止 | 受阻 | Paper有限已查，必要Blog历史段仍缺失 |
| SRC-MINIMAX |EN76/CN68行，03/18→02/14/12；Agent TechBlog本轮真实恢复66行，三条09/19、09/22、10/08，无03/05；停止可见目录 | 已检查 | 旧techblog.md失败不作为永久缺口；不外推未列历史 |
| SRC-ARXIV |四主线各Mar05/Mar04两组共8query；563库存仅相关题名有界查漏，29条选择性完整AB＋搜索5条完整AB，旧Helios只去重。一次cs2026-03 skip2000/show500官方月表恢复CacheMiss/InternalError，四标题日期补检未得原始首次公开，停止 | 受阻 | 32新潜力日期隔离；搜索Date/Submitted/Updated/Registered/月ID都不是first-public；没有563逐条AB/全文队列 |

具名负样本按层保留：03394 Governance-Aware Sandbox 是审批/隔离/audit常规组合，未增验证保证；04390 WebGIS DualHelix 是组件组合与单例refactor，未改迁移机制；Anthropic Labor Market Impacts 是就业测量；WAXAL 是数据资源；OpenAI Balyasny/Descript 是局部应用，教育是政策；QwenCode3/6是普通界面更新。其具体理由已读完整题摘或核心，不为不影响关闭的日期扩大请求。安全/正确性信号 PR2021 单独处理为窗外线索，见§5，不用“普通版本”掩盖。

本轮新增负侧：DBenchBio03322以生物知识发现为目标，按ROADMAP科学发现暂停边界关闭；LilMoo03508公开题摘为语料启发式/LLM-judge筛选与双语扩增组合、Hindi对比，未给新recipe成立条件，非因0.6B而关闭。两项first-public日期未核实，现有官方事件页未见影响关闭的纠错/安全信号，按具体贡献理由停止。OpenAI《Introducing the Adoption news channel》为栏目发布；《Five AI value models driving business reinvention》为成熟组织/ROI/治理工作流组合；Wolfsburg客户案例未披露可迁移受控机制。Excel官方细胞引用、Excel-native计算、permission/undo描述成熟工具边界，未公开新状态/验证/执行协议，财务内部benchmark不足因果对照，故关闭；April22/May5修订窗外，不吸收。完整AB/必要核心由root实际读并校准通过。

## 3. 候选与判断

本轮确认新增候选0；原表14行原样保留。32日期潜力列§5，未评分、未入候选、未作证据审阅完成或Books判断；两条明确题摘关闭及四条官方核心关闭列§2，不为它们补不影响关闭的日期。Anthropic UE Blog是同家族传播事件，仅比较实际差额，见§4新增尾段。

低分候选加深理由：HyperParallel、CAT、Helios、ZipMap已有具体长期机制缺口；RubricCritic、04069及CoTControl分别涉及评价反证或安全变化，故只深入受影响命题，不上调分数。

公开区间均含起点、不含终点；arXiv表中起点统一为2026-03-05T09:00:00+08:00，终点逐身份列完整时区。它们是可支持的范围，不是补造exact announcement时刻；复合依据见§4。评分为 Design Delta + System Reach + Durability。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [SENTINEL: Stagewise Integrity Verification for Pipeline Parallel Decentralized Training](https://arxiv.org/abs/2603.03592v1) | 2026-03-05T09:00:00+08:00 ～ 2026-03-05T11:15:27+08:00 | 边界verifier、EMA/cascade修正不可信stage归责；2+2+3=7 | 深入完成 | 整合：TRAIN-PIPELINE-PARALLEL，[Ch38](../../../../books/part-04-training-system/38-pipeline-parallel.md)，root POST通过 |
| [HyperParallel: A Supernode-Affinity AI Framework](https://arxiv.org/abs/2603.03731v1) | 2026-03-05T09:00:00+08:00 ～ 2026-03-05T11:18:45+08:00 | offload/cache进入图级联合资源计划；2+2+2=6 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，root POST通过 |
| [A Rubric-Supervised Critic from Sparse Real-World Outcomes](https://arxiv.org/abs/2603.03800v1) | 2026-03-05T09:00:00+08:00 ～ 2026-03-05T11:20:21+08:00 | outcome proxy粒度及critic transfer反证；2+1+3=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，root POST通过 |
| [Monitoring Emergent Reward Hacking During Generation via Internal Activations](https://arxiv.org/abs/2603.04069v1) | 2026-03-05T09:00:00+08:00 ～ 2026-03-05T11:26:39+08:00 | token/span sensor与来源标签边界；2+1+3=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，root POST通过 |
| [Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization](https://arxiv.org/abs/2603.04135v1) | 2026-03-05T09:00:00+08:00 ～ 2026-03-05T11:28:11+08:00 | 两级pruning及IS、packing可能改变训练预算；2+2+3=7 | 争议 | 暂缓：TRAIN-GRPO；不写Books，精确争议终态见§4–5 |
| [Retrieval or Representation? Reassessing Benchmark Gaps in Multilingual and Visually Rich RAG](https://arxiv.org/abs/2603.04238v1) | 2026-03-05T09:00:00+08:00 ～ 2026-03-05T11:30:36+08:00 | 固定retriever转录对照纠正模态归因；3+1+3=7 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md)，root POST通过 |
| [Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory](https://arxiv.org/abs/2603.04257v1) | 2026-03-05T09:00:00+08:00 ～ 2026-03-05T11:31:03+08:00 | indexed full-fidelity archive与read/write预算RL；2+2+3=7 | 深入完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) CompactControlStateExactEvidenceArchive |
| [V₁: Unifying Generation and Self-Verification for Parallel Reasoners](https://arxiv.org/abs/2603.04304v1) | 2026-03-05T09:00:00+08:00 ～ 2026-03-05T11:32:09+08:00 | coverage与near-tie分配固定比较预算；2+2+3=7 | 深入完成 | 整合：AGENT-REFLECTION，[Ch80](../../../../books/part-07-agent/80-reflection.md)，root POST通过 |
| [Dissecting Quantization Error: A Concentration-Alignment Perspective](https://arxiv.org/abs/2603.04359v1) | 2026-03-05T09:00:00+08:00 ～ 2026-03-05T11:33:25+08:00 | concentration/alignment分解与非正交校准；2+1+3=6 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，root POST通过 |
| [Helios: Real Real-Time Long Video Generation Model](https://arxiv.org/abs/2603.04379v1) | 2026-03-05T09:00:00+08:00 ～ 2026-03-05T11:33:53+08:00 | 历史多尺度压缩/漂移模拟训练；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，root POST通过 |
| [AgentIR: Reasoning-Aware Retrival for Deep Research Agents](https://arxiv.org/abs/2603.04384v1) | 2026-03-05T09:00:00+08:00 ～ 2026-03-05T11:34:01+08:00 | 当前trace/query联合表示与训练适配；2+2+3=7 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md)，root POST通过 |
| [ZipMap: Linear-Time Stateful 3D Reconstruction with Test-Time Training](https://arxiv.org/abs/2603.04385v1) | 2026-03-05T09:00:00+08:00 ～ 2026-03-05T11:34:02+08:00 | TTT fast-weight scene estimate与query闭包；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，root POST通过 |
| [Introducing GPT-5.4](https://openai.com/index/introducing-gpt-5-4/) | 2026-03-05T18:00:00+08:00 | tool按需加载与High Cyber effect-scope路由变化；2+2+3=7 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；tool部分AGENT-TOOL-CALLING Ch78已有覆盖；root POST通过 |
| [Reasoning models’ chain-of-thought controllability](https://openai.com/index/reasoning-models-chain-of-thought-controllability/) | 2026-03-05T18:00:00+08:00 | trace/output通道可控性及监测推断边界；2+1+3=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，root POST通过 |

## 4. 证据与知识整合

### 日期：复合区间，不把 DOI metadata 单独当公开正文

[arXiv availability](https://info.arxiv.org/help/availability.html)以首次announcement分配ID，不能提前提供ID/DOI，按Sun–Thu20Eastern公告、14Eastern deadline。[arXiv DOI原则](https://info.arxiv.org/help/doi.html)与[DataCite DOI states](https://support.datacite.org/docs/doi-states)只共同约束身份；registered本身不直接观测正文。

03592 v1 Submitted=2026-03-03T23:51:10Z，已经过Tue14EST；其余11篇Wed03/04、deadline之前。因此最早可能官方公告为03/05BJT09。每身份真实DataCite client=arxiv.content、state=findable、canonical abs，registered均03/05UTC03:15～03:34；结合不能提前ID/DOI与公告公开正文政策形成上界，不以Submitted或created单独回填首公开。表中上界向外取1秒，完全落窗。原值和history见[15项字段](../_sources/daily-20260306/V3_ADMISSION_DATE_RAW.md)及[首批字段停点](../_sources/daily-20260306/V3_WORKING_CHECKPOINT.md)。这不证明作者世界范围内此前从未公开；早提交8项无法证明下界，故隔离。精确v1页面轻量未见withdraw/delete标记，不授完整版本史无纠错声明。

OpenAI三条RSS原pubDate=Thu,05Mar2026 10:00:00GMT，共同支持本窗公开事件；release/card只计一族。CoT论文2603.05706v1 Submitted03/05T22:03:48Z、registered03/09T01:42:19Z不属于本窗arXiv事件，仅佐证同一Blog研究命题，不增加候选。RSS邻日原值复用记录见[V3_OPENAI_RSS_ROOT_RECOVERY](../_sources/daily-20260306/V3_OPENAI_RSS_ROOT_RECOVERY.md)，本日item原值见来源记录。

### [SENTINEL: Stagewise Integrity Verification for Pipeline Parallel Decentralized Training](https://arxiv.org/abs/2603.03592v1)

§2–3在各stage间及首尾可信边界核forward activation/backward gradient，诚实warm-up建立EMA，以L1/L2/sign/distribution变化报警；flag不更新基线，cascade上游污染暂停后续统计并避免误归责。§3.2的阶段少于半数恶意前提不能删除；本次不采用收敛定理。

§5用Llama0.6B/16layers、128workers、8DP×16PP、context1024、5ksteps及1k诚实warm-up，受限恶意比例/攻击激活；Table1部分gradient flip/randomsign zero recall，Table3更大模型某bias攻击也漏检，共谋增加误报。采用“统计边界sensor而非完整计算认证”；新增 Ch38 Checkpoint与Failure 两段，连接原step一致性/工程验证，保留可信worker或重算fallback。数值是作者模拟条件，不是生产完整性保证。

### [HyperParallel: A Supernode-Affinity AI Framework](https://arxiv.org/abs/2603.03731v1)

§3.2 pooledDRAM/HBMcache及read/prefetch/offload原生图操作允许compute/communication/cache联合计划；§3.3 modality subgraph及resource group分离，§3.4 Layout设备矩阵/tensor映射声明不等实际切tensor。§4性能缺硬件、batch和匹配质量细节，标Not Disclosed，不采利用率或加速宣传。

Ch36 TrainingMemoryContract 原段只说明组合峰值与host流量，Ch39已有普通offload/prefetch/lifetime，不包含cache进入图级联合编译合同。实际补两段解释联合计划及资源争用、回退普通分片/显式offload；没有改root的SPARe/FP4其他位置。实现未运行，不能宣称编译正确或系统benchmark复现。

### [A Rubric-Supervised Critic from Sparse Real-World Outcomes](https://arxiv.org/abs/2603.03800v1)

§2由PR→commit→segment关联结果；PR merge与code survival均稀疏proxy，前者不证明每segment成功，后者受后续修改影响。Rubric辅助标签也含模型标注。§4同Qwen3-4B，benchmark-only迁移真实proxy表现弱，success+rubric随MSE/BCE及proxy改变，部分下降，反驳“更细监督一定好”。

§5 Best-of8/尝试数收益只在500中筛出的148个mixed-outcome任务、固定agent及Sonnet/Opus候选上成立；attempt减少不等含critic的整体token/延迟下降。Ch80已承载accuracy≠intervention，故不重复写那里；Ch66目标→证据新增两段标签对象/粒度/transfer合同，并要求独立执行与成本。没有采作者83%为生产普遍保证。

### [Monitoring Emergent Reward Hacking During Generation via Internal Activations](https://arxiv.org/abs/2603.04069v1)

§3 residual SAE表示后Std/PCA/logistic token信号，层/span聚合并threshold一次generation；训练标签是hack/control adapter来源，不是逐token恶意真值。§4受控SchoolRewardHacks/Alpaca混合与三模型/heldout adapter，行为标签还依赖GPT4o，不构成人类独立oracle。reasoning/direct-answer span关系是观测关联，不证明CoT造成reward hack。

§6有限benchmark/model family与SAE/线性漂移，runtime latency未披露。Ch66静态adapter与内部probe原文未说明generation token/span sensor来源标签的边界，实际补两段。sensor只提出检测证据，不能成为effect authority；分布迁移、高风险或无效生成回到独立行为/人工policy，不由阴性自动放行。

### [Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization](https://arxiv.org/abs/2603.04135v1)

§4.1无偏证明针对无KL、未clipped surrogate，并要求每prompt/completion剪枝概率P<1保留support；C/(1-P)用于抵消保留后重归一化。§4.2历史低advantage筛prompt、低平均绝对advantage筛completion；全completion rollout已生成，不能说剪掉更新就省掉所有rollout。§4.3 window packing是不同的执行增量。

直接反证是AppendixA明确deterministic fraction pruning及Alg1 floor fraction，未给出与理论随机inclusion probability一致的实现映射。§5 verl/vLLM、8H10080GB、Qwen3 4/8B数学任务、rollout5/maxout1024、15epochs报告GPU-hours/Pass1，部分质量下降而非全部等价。实际Ch33 Group-relativeGradient及prompt selection原段覆盖组依赖/selection bias，却不能补出缺失的随机support证明。本家族保留7分及争议，不因费时删候选；中心保证隔离、不写Books、不采用unbiased clipped GRPO。重开需冻结实现的随机选择/inclusion及实际surrogate对应，见§5。

### [Retrieval or Representation? Reassessing Benchmark Gaps in Multilingual and Visually Rich RAG](https://arxiv.org/abs/2603.04238v1)

§3固定retriever/评价协议，改OCR、language normalization及图示语义转录，显示模态比较混入输入表示质量；15语言pageTopK，不将总分改进单归encoder。逐语言最佳配置基于同eval选择可能乐观。AppendixC Tables3–4多模态参考不是全部同环境重跑，空间关系/非文字图形仍不可纯文本恢复。

Ch76已有query dialect/index/ranker合同，但未显式分离视觉page→转录→representation这一归因层。实际在Retrieval度量节补两段，保留AgentIR，要求固定retriever的输入对照及独立语言/图形切片。采用评价纠错而非“BM25普遍胜multimodal”，OCR成本、布局损失与selection bias在正文紧邻。

### [Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory](https://arxiv.org/abs/2603.04257v1)

§3保留索引寻址完整经历、Compress与Search/read，RL共同优化task reward、context overflow/重复/格式及分段更新；提取start/mid/end三anchor不是完整faithfulness证明。§4只是在decision-sufficient selector与预算假设下的存在性，不证明学会的policy始终正确。

§5 modifiedALFWorld隐藏admissiblecmd、initial room及限制look/summary，迫使记忆依赖；Qwen3-30B-A3B/SlimeINT4 rollout与BF16grad，with/withoutRL收益不是archive单组件因果，peak9634仍超过8k软阈值。Ch77 CompactControlStateExactEvidenceArchive 实际段落已承载full-fidelity外存、稳定授权dereference、lifecycle/readwrite terminal credit、存在性与软工作集不等硬存储cap。已有覆盖/No Change，不能为三anchor实现细节再重复补章；root必要源与实际owner已有覆盖复核通过。

### [V₁: Unifying Generation and Self-Verification for Parallel Reasoners](https://arxiv.org/abs/2603.04304v1)

§4由pointwise初排、weighted winrate及score-gap proxy安排两阶段pairwise：先低degree覆盖，再Swiss near-score unseenpair。degree≥1不证明图全局连通，gap不是校准概率。§4.3 GPToss20B/LCBv6/N16、同调用预算随机pair消融支持选择分配增量；N+V calls不等token/walltime，pool PassN并未改变。

§5自judge RL可能collapse至固定分/空incorrect输出，更不能把自判当独立正确性。本次只采用固定候选池的comparator budget两段写Ch80 CriticAccuracy≠InterventionValue末，保留原paired intervene/no-intervene因果合同。不同模型/任务/候选池外推不采；预算不足或judge漂移可回退pointwise、随机pairs或执行verifier。

### [Dissecting Quantization Error: A Concentration-Alignment Perspective](https://arxiv.org/abs/2603.04359v1)

§2在negligible clipping、均匀整数量化近似下分解concentration/alignment；§3正交rotation不能改变后者，§4协方差非正交变换及Hadamard可针对两项，再block128近似降低full-rank代价。展示公式的记号风险不复制进书，保留原计算语义和weight inverse关系。

§6统一128×2048 DCLM校准、W4A4KV4、per-token非对称activation/KV及per-channel对称weight、RTN/GPTQ、五模型/六任务/四seed；baseline也随range/calibration改善。§7没有最优walltime保证。Ch49 RotationScope新增两段具体区分保谱与方向alignment、精度/计算/校准边界；root实际源和正文POST通过，未复现实验，不采用所有量化通用最优。

### [Helios: Real Real-Time Long Video Generation Model](https://arxiv.org/abs/2603.04379v1)

§3.1历史多尺度patchification、noisy-window/head amplification、relativeRoPE与首frame anchor；§3.2训练独立施加frame corruption模拟drift；§3.3 pyramid/distillation省采样，不把三项效应当同一个原因。§5 Wan2.1T2V14B/384×640、109frame训练及长frame评价；HeliosBench240经LLMrefined prompts，自动指标与有限人工pairwise不同。

Table5去anchor/corruption下降支持相关机制，运动/画质取舍仍在；19.5FPS宣传不作通用性能证据。Ch24 video-history段末、Diffusion前新增两段压缩历史/漂移训练与failure面，保留必要重算/更完整历史fallback，不写无限稳定视频或生产并发能力。root POST通过。

### [AgentIR: Reasoning-Aware Retrival for Deep Research Agents](https://arxiv.org/abs/2603.04384v1)

v1 §3.2将当前 reasoning 与 query 联合嵌入；§3.3 DR-Synth由成功轨迹、支持文档及oracle-informed难负例适配检索训练。§4 BrowseComp-Plus、三Agent、top5/512token片段，不能将rerank top20等不同预算直接当同条件效率。§5 Table2同Qwen3Embedding4B backbone，Tongyi基线48.67、reasoning-only55.54、train-only59.40、both66.27，支持两项互补而非只比较8B/BM25宣传。

Table3 full-history60低于current-trace66.27，且实际历史约截至最近三turns，不是所有完整历史或无限上下文实验。额外trace访问、输入token、训练构造与planner错误仍有成本。Ch76 Retrieval基本度量原段未含当前推理意图作为检索输入，本次新增两段联合表示与fallback；trace不是事实权威，不假设任意私有CoT可取得。root实际源、同backbone消融、历史反证及正文邻接POST通过。只采用该局部受限机制，未复现实验。

### [ZipMap: Linear-Time Stateful 3D Reconstruction with Test-Time Training](https://arxiv.org/abs/2603.04385v1)

§3每view DINO2 patch/ray表示，local attention配global TTT fast-weight状态；虚拟KV更新loss独立于3D任务loss，query ray读取而不是保留完整raw archive。token学习率、梯度归一化及gating处理更新稳定性；streaming view会改变derived scene state。

§4.3 reduced-compute ETH3D消融只支持其重建范围，未见物体仍缺失，某reference query还能恶化长序列一致性。Ch25 QueryClosure邻接Memory段实际新增两段区分observation-derived estimate、transition parameters与query事实权威；静态新视角不证明动态世界、动作控制或线性成本消除所有质量压力，显式views/几何/混合路径共存。5分仍因已确认长期表示缺口窄深入，root POST通过。

### [Introducing GPT-5.4](https://openai.com/index/introducing-gpt-5-4/)

Release按需工具定义减少catalog上下文，MCPAtlas250任务/36servers局部同accuracy，Ch78既有目录检索→shortlist→schema及tenant/version/fallback已具体承载，No Change该子命题。OSWorld原GPT5.3Codex配置从2.56M/2048变10.24M/6000，不能把baseline修正当5.4机制。

[Thinking PDF core §5.3](https://deploymentsafety.openai.com/gpt-5-4-thinking/gpt-5-4-thinking.pdf)披露topical classifier→reasoner、ZDR非TAC async message block替代cyber降级、nonZDR离线actor enforcement、TAC高dualuse和end-user身份粒度。Ch72 Policy-as-Data原有sensor≠authority，缺message/account作用范围与留存/授权路由差额，实际补两段；阈值/完整实现Not Disclosed。安全数据集结果不是unknown adaptive保证；当前PDF §6明示3/17 miniAppendix，排除全部窗外附录，不冒充整卡冻结launch。root POST通过。

### [Reasoning models’ chain-of-thought controllability](https://openai.com/index/reasoning-models-chain-of-thought-controllability/)

Blog本窗事件；较晚[论文v1](https://arxiv.org/html/2603.05706v1)仅佐证方法：14,076测试、九类control任务，压制/插入/style，对trace与final output分别评价；macro aggregation、程序grader及部分模型oracle，三次runs与有限人工一致性，不假定所有API私有CoT可得。

§6明确instruction-following是恶意规避能力代理，并非真实恶意目标、自适应RL或充分monitorability。低CoT control不能认证安全，直接优化可侵蚀边界。Ch66 ReasoningTrace安全对象原段只区分输入/trace/输出及定位，本次补两段channel controllability与monitorability的不同验证对象；权限、观察缺失和回退外部effect验收保留。6分安全评价窄深入，root POST通过。

### 本轮增量：同家族事件与必要消歧（不改上述原连续正文）

Anthropic [Three Challenges and Two Hopes for Unsupervised Elicitation](https://alignment.anthropic.com/2026/challenges-hopes/)官方明确Mar05，无需追时刻。实际核心列出非truth、类别不均衡、任务不可完成三压力，UE与E2H/ensemble仅有条件改善；与所链[2602.20400](https://arxiv.org/abs/2602.20400)旧02/26同家族§4定点对读，Ch66现有三压力/70B例外/人工shift、无SFT、oracle方向边界已覆盖，Blog未增机制或有效性条件。只复用该家族有效Source及具体owner判断，不加载旧日整个分母、不重评分、不新增Books。

本轮完整题摘34条的原字段分为[26条选择性AB](../_sources/daily-20260306/SUP_AB_INVENTORY_SELECTED_20261009.json)、[3条extra AB](../_sources/daily-20260306/SUP_AB_EXTRA_SELECTED_20261009.json)、[Mar05搜索4条完整AB](../_sources/daily-20260306/SUP_ARXIV_SEARCH_20261009.json)及[Mar04搜索Energy完整AB](../_sources/daily-20260306/SUP_ARXIV_SEARCH_MAR04_20261009.json)；后者Helios只旧去重，MAGE/COREA与extra不重复计。所有题摘是语义准入而非机制验证。CSA03565仅为消歧读§4.2：联合prompt bundle及hybrid用户回放/NLI，而非仅把workflow映射现有章；DarkPattern03881仅消歧读§7：完成执行条件分母排除失败，DOM/视觉限制可带来评价反证。二者仍缺first-public，不采用作者效果数字、不因此进入全文队列。

原始日期恢复仅一次有界官方cs月表及四标题原始公开记录检索，见[日期/核心恢复](../_sources/daily-20260306/SUP_DATE_CORE_RECOVERY_20261009.json)与[标题日期恢复](../_sources/daily-20260306/SUP_TITLE_DATE_RECOVERY_20261009.json)。MEM作者原入口也实际InternalError。检索Date、Submitted/Updated、Registered及月ID不能补首公开；LinearRNN等后续v2/v3标记不能自动当重要修订事件。未发现可确认Mar05公开且有新差额的revision，不重评分family。官方明确日期可直接用日期，不要求时区或秒。

## 5. 缺口与下一步

本轮普通待办0：来源检查、题摘、必要消歧及完整DAY非作者复核均结束，没有待扩大的全站或全文队列。原14候选及12家族实际Books、Memex(RL)已有覆盖、DPPO争议隔离的旧有效非作者POST复用。下列外部保留项不支持正面Coverage/Evidence/Books或无遗漏。

本轮32项新日期隔离完整名单（均未评分）：每行身份链接及具体潜力是重开对象，不是全文队列；局部、小模型、理论、复制或负面结果本身不构成EX。

| 精确身份 | 新机制/条件/反证潜力 |
| --- | --- |
| [03292 MA-RAG](https://arxiv.org/abs/2603.03292v1) | 语义disagreement转查询及history修复，不因医疗应用排除 |
| [03295 Goal Selection](https://arxiv.org/abs/2603.03295v1) | 受控目标选择揭示人类proxy与LM差异 |
| [03329 AutoHarness](https://arxiv.org/abs/2603.03329v1) | 反馈合成code harness限制非法动作与代码policy，不仅工作流类比 |
| [03459 MLP Budget](https://arxiv.org/abs/2603.03459v1) | 上下文gated线性化/预算重分配及语料不迁移条件 |
| [03565 CSA](https://arxiv.org/abs/2603.03565v1) | 跨节点联合prompt与hybrid回放评价条件，必要消歧§4.2 |
| [03583 ByteFlow](https://arxiv.org/abs/2603.03583v1) | coding-rate自适应字节压缩/TopK静态执行图 |
| [03596 MEM](https://arxiv.org/abs/2603.03596v1) | 短视频/长文本memory共同进入动作policy |
| [03612 Linear RNN](https://arxiv.org/abs/2603.03612v1) | 精度/复杂度/并行性与表达力的条件取舍 |
| [03680 MAGE](https://arxiv.org/abs/2603.03680v1) | episode末meta-RL与population/agent归一化探索 |
| [03752 COREA](https://arxiv.org/abs/2603.03752v1) | RL置信度校准改变small/large cascade路由 |
| [03753 Agentic P2P](https://arxiv.org/abs/2603.03753v1) | soft-state能力descriptor、canary/fallback及drift/Sybil条件 |
| [03761 AgentSelect](https://arxiv.org/abs/2603.03761v1) | positive-only/长尾推荐的counterfactual transfer边界 |
| [03781 LifeBench](https://arxiv.org/abs/2603.03781v1) | 多源轨迹中的非声明习惯与时间关系记忆测量 |
| [03818 VLA Forgetting](https://arxiv.org/abs/2603.03818v1) | 预训练/replay下遗忘基线反转，保留负面/旧方案成立条件 |
| [03823 SWE-CI](https://arxiv.org/abs/2603.03823v1) | 连续commit/维护分母，不把一次patch成功等同维护 |
| [03824 Evaluation Awareness](https://arxiv.org/abs/2603.03824v1) | adversarial context与评价觉察因果线索，暂不采效果数字 |
| [03881 Dark Pattern Audits](https://arxiv.org/abs/2603.03881v1) | completed-execution条件分母排除失败及DOM/视觉限制 |
| [03955 GIPO](https://arxiv.org/abs/2603.03955v1) | log-ratio Gaussian trust weighting与stale replay非零梯度 |
| [03973 Dual-Solver](https://arxiv.org/abs/2603.03973v1) | 学习预测/domain/residual保留二阶的低NFE条件 |
| [03993 Attention Specialization](https://arxiv.org/abs/2603.03993v1) | attention head专门化动力学的条件理论 |
| [04127 DARKFormer](https://arxiv.org/abs/2603.04127v1) | 协方差学习/importance proposal的各向异性近似 |
| [04308 Activation Outliers](https://arxiv.org/abs/2603.04308v1) | clipping复现反例/群组差异及硬件profiling收益边界 |
| [04346 One-Shot Probe](https://arxiv.org/abs/2603.04346v1) | counterfactual文本与regressor估计预训练覆盖 |
| [04364 DMAST](https://arxiv.org/abs/2603.04364v1) | DOM同时影响screenshot/AX的共享攻击与self-play |
| [04366 LatCH](https://arxiv.org/abs/2603.04366v1) | selective training-free latent guidance避免decoder反传 |
| [04370 τ-Knowledge](https://arxiv.org/abs/2603.04370v1) | 非结构化知识检索、tool state与重复pass下降 |
| [04378 AAJR](https://arxiv.org/abs/2603.04378v1) | trajectory对抗方向Jacobian与正式稳定性条件 |
| [04956 WaterSIC](https://arxiv.org/abs/2603.04956v1) | 非均匀列rate/shaping及信息论量化界，不因理论排除 |
| [05168 Sparse-BitNet](https://arxiv.org/abs/2603.05168v1) | 低bit与动态N:M稀疏交互/训练稳定条件 |
| [05369 ProRes](https://arxiv.org/abs/2603.05369v1) | 更深层更迟的residual warmup优化路径 |
| [08747 FP4 Sensitivity](https://arxiv.org/abs/2603.08747v1) | 组件/深度/format控制，小模型与早层反例 |
| [20223 Inference Energy](https://arxiv.org/abs/2603.20223v1) | hardware/cache开关/量化的energy-latency测量校验，不按教育应用EX |

以上32项共同缺少可确认其实际首公开归属日的原始记录，宽检索时间/提交/DOI元数据不足。一次有界原始日期恢复仍受阻，继续读全文不能补日期。恢复条件为每个精确v1的首次announcement batch/公开正文记录，或作者原始项目/发布正文明确公开日期及版本身份；官方明确日期无需追时刻。材料到达只重开该身份的日期归属，再按真实归属日准入，不先评分/写Books、不复扫其他31项。DBenchBio/LilMoo关闭不需要这组日期请求。

本窗外部终态保留项，均不支持正面Coverage/Evidence/Books或无遗漏：

- arXiv日期： [03293 SE-Search](https://arxiv.org/abs/2603.03293v1)、[03296 PlugMem](https://arxiv.org/abs/2603.03296v1)、[03305 DCCD](https://arxiv.org/abs/2603.03305v1)、[03333 DropMatch](https://arxiv.org/abs/2603.03333v1)、[03371 SleeperCell](https://arxiv.org/abs/2603.03371v1)、[03379 MemSifter](https://arxiv.org/abs/2603.03379v1)、[03383 OpenPangu](https://arxiv.org/abs/2603.03383v1)、[03417 MSV](https://arxiv.org/abs/2603.03417v1)。early Submitted+Mar5 registered只给过宽区间；精确月表恢复404/InternalError。需每篇v1官方首次announcement batch/正文公开记录，或带原时区/版本的作者项目公开记录。材料到达只重开该身份与真实归属日，不先评分/写Books。03383已窄读static-tree/NPU机制消歧；03371安全线索保留而非贡献关闭。
- DPPO04135中心争议：需要冻结代码revision说明随机pruning的真实inclusion probability、support P<1及C归一化，与组advantage在剪枝前/后的计算关系，并证明适用于实际是否clipped/KL surrogate；或明确勘误撤回无偏保证。AppendixA deterministic fraction未满足当前证明条件，不能用一般IS原理或现有Ch33补洞。精确重开§4.1、Algorithm1/AppendixA，其他候选不受影响。
- 当前机构历史子目录：GoogleResearch March p2、Meta本窗Research目录、MiMo Blog。均已用当前官方入口及有限Mar05主线补检，仍空壳或InternalError；加上上述arXiv日期为本轮四来源缺口。可接受03/05精确发布行/官方feed/archive及原文明确公开日期与必要版本身份，不需要时刻、全年目录。到达后只重开该来源本日切片。Qwen/Seed/AgentTechBlog本轮实际有限恢复，旧缺口不再沿用；其有限目录无项仍不授未列历史零事件。

窗外恢复线索，不属于本窗、不阻塞本日：QwenCode PR2021 created02/28T11:25:53Z、merged03/02T12:59:36Z，v0.11.1 published03/03T13:08:44Z，真实03/04release线索已交root；未冒充已审重复。AgentIRv2/v3、CoT paper较晚arXiv事件及GPT5.4 mini附录不进入本窗事件。完成本日后不自动扩日。

## 6. 复核

### 本轮补查

复核者：root（非本日作者 supplement_20260306）。
结论：通过

首批准入已通过：root实际读26＋3＋5全部34完整AB（Helios仅旧去重），Anthropic核心与同家族差额、CSA§4.2、DarkPattern§7、Excel核心L48–89；DBenchBio/LilMoo具体关闭可，Energy及其余32潜力不得因local/theory/small/negative排除。Excel成熟工具边界未公开新协议、finance数字无受控机制，April/May窗外不吸收。该批校准不替代14来源实际停点、日期隔离、freeze和本轮完整DAY独立验收；作者不自验自己的DAY。

root本轮完整DAY实际核14来源的入口与有限停止、全部34完整题摘及必要准入core、32具体日期隔离和2关闭；独立负侧还核Excel、栏目/组织框架及Wolfsburg官方核心，UE同家族具体Ch66论点无差额。Seed默认14与US18的locale差额经root实际请求补核，目标Mar05均无条目，不授其他日期或历史全覆盖。全部六部分增量已核，旧14行/原窗口/连续§4保持，旧有效Source及POST复用。没有将563库存或Google全年目录逐项审阅，也没有在缺公开日期时展开全文。普通待办0，无新增Books写入；V3、链接、冻结与限定diff检查见实际工具结果，不替代上述语义验收。未stage、commit、push。

### 原窗已通过复核（历史有效记录，非本轮验收）

复核者：root（非本日作者 mar02_v3）。
结论：通过

root独立检查14个Daily来源实际停止范围、563宽库存只查漏非逐项队列、全部14候选的完整题摘/具体准入、复合公开区间及必要原文。全部12家族实际新增（9个owner文件）与邻接源→正文POST通过；SENTINEL首尾stage可信、每stage恶意worker少于一半及诚实warm-up前提补明确后，root已重新实读。Memex(RL)必要源与Ch77具体已有覆盖通过，GPT5.4工具子命题Ch78已有覆盖；DPPO §4.1/4.2与AppendixA确定性prune的中心冲突隔离通过，不作为无偏保证或Books正面证据。CoT论文较晚arXiv仅佐证同Blog，不新增家族。

独立负侧有4个具名样本：arXiv系统/应用03394 Governance-Aware Sandbox与04390 WebGIS DualHelix的完整题摘，机构领域Anthropic《Labor market impacts of AI》核心说明，以及安全/正确性QwenCode PR2021实际patch（由mar02_v3在03/04有界复核中独立读，root复用，其本日为窗外恢复线索，不冒充已审重复）。其余原始记录中的数据资源、客户/政策和普通版本负样本没有由非作者逐项重读，563宽库存没有全审；上述4样本不授全量负侧验证。8个具体日期隔离及机构历史子入口保留项不算Coverage/Evidence通过，不支持Books或历史零事件断言。

作者 scoped Markdown/链接/diff检查完成，git diff --check通过；python3 scripts/validate_research.py --report papers/2026/03/06/README.md 已通过（1 V3报告，exit0）。机器通过不替代source→claim、Books或独立日级验收。未stage、commit、push。
