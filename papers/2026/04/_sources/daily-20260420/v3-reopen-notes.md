# 2026-04-20 V3 作者恢复

## 窗口、范围与接手

2026-09-27本轮接手已完整重读AGENTS、统一Prompt、RESEARCH_CONTRACT、REPORT_CONTRACTS、RESEARCH_SOURCES及ROADMAP；月V3 checkpoint最新段已读。使用context-engineering技能只整理当日相关上下文，不增改项目规则。固定窗口为`[2026-04-19T09:00:00+08:00,2026-04-20T09:00:00+08:00)`。仅独占本日README与_sources；共享Books没有授锁，不写其他日期/共享索引/checkpoint，不stage/commit/push。

旧正式README按恢复规则只先读取去重身份、来源/完成声明与未决索引，未继承V2.1 Complete或泛化来源/Books判断。正式旧25身份15356～16145来自owner-replay447库存，daily目录的旧submitted账本却为530/29、17234～26968；两者不是同一候选/日期队列。本轮不把447或530当贡献分母/逐篇全文队列，created、submitted、Updated均不单独证明首次公开。

## 原始日期与有限arXiv发现

本次已重开[官方availability](https://info.arxiv.org/help/availability.html)：永久ID在公告过程分配，Sun–Thu Eastern公告；Sun Apr19 20:00 EDT对应Mon Apr20 00:00 UTC/08:00北京，本日可能有正常公告，不沿用周末空窗结论。实际读取`../arxiv-owner-replay-20260903/20260420/arxiv-owner-receipt.json`原字段：447记录，404自身v1 Updated早于本日01:00Z、43晚字段/后改记录。这只是字段分层，不是404落窗论文认证。首15314=`2026-04-20T00:00:05Z`，早段末16224，16231=`01:00:24Z`、末16299=`01:04:41Z`；须结合OAI/连续ID/官方入口，不把跨截点字段机械迁到邻日。

已实际浏览447完整标题作为有界查漏，读旧25的完整标题/摘要及自身字段；未读447全文、未继承旧关闭标签。15356官方history仅v1 Submitted Apr10（提前提交非提前公开），17234官方Submitted Apr19仍仅是来源身份，不能凭它移入本日。当前准入未冻结，额外主线标题信号的完整题摘与当前withdrawal/correction标记仍普通待办；旧25必要正文也须核采用命题后才复用。

## 已实际完成的机构入口（其余仍普通检查）

| 来源 | 实际入口、范围与停止点 | 本次判断/限制 |
| --- | --- | --- |
| OpenAI | `https://openai.com/news/rss.xml` HTTP200，April目录04/21T00Z→Hyatt04/20T00Z→Codex04/16T10Z跨窗；进入[Hyatt原文](https://openai.com/index/hyatt-advances-ai-with-chatgpt-enterprise/)核心 | Hyatt为部署与部门使用案例，未披露新模型/训练/推理机制或受控设计证据，前分母关闭。RSS不替代Research历史分页，后者仍需核精确外部限制。 |
| Qwen | `https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`实际完整40项，原`extra.date`邻界04/18T10+08→04/22T10+08 | 此动态目录本窗无项；静态60项/组织原始入口待定点核可复用依据，不声称全部作者稿零更新。前两次打印展开extra/content过多，截断输出不计覆盖；最后仅日期/title提取完整40项后计此范围。 |
| Hunyuan | POST `https://api.hunyuan.tencent.com/api/blog/publicList`，pageNum1/pageSize100/renderType0，完整9条`displayPublishTime` | 公开“全部”列表9/9，邻界04/23→02/13，本窗无条目；仓库及既有36 release子入口限流范围仍需按本日核，不以目录成功取代。 |
| Seed | GET `https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&order_desc=true&page_token=20`，header x-tt-localeUS，实际20项/total242/next40/has_moretrue；05/12T16Z→04/08T16Z，实际窗口上下邻界04/21T16Z→AgentWorld04/19T16Z→LeapAlign04/15T16Z | 只处理该跨窗页的相关卡片，不遍历242全文。AgentWorld ID1635/外链2604.18292完整题摘已读，具体环境任务发现/验证和capability-gap驱动训练有潜在贡献，但日期事件身份隔离，见下。Blog目录仍普通待检。 |

Seed AgentWorld原`PublishDate=2026-04-19T16:00:00Z`是CMS卡片字段；官方[2604.18292版本页](https://arxiv.org/abs/2604.18292)却v1 Submitted `2026-04-20T14:01:10Z`，在本窗之后。卡片可能早于作者稿，也可能后期回填/按日期桶展示；当前不能由后来PDF证明当时正文已公开，亦不单凭submitted宣布最终owner。仅恢复该卡原始公开正文/可靠公告后重开本窗事件；不评分、不当本窗确定候选，不展开完整旧版史。

## 后续实际入口与限定复用

以下为本轮后续已实际核查的入口；仅复用旧日记录中未变化且明确覆盖本窗的目录/端点限制，不复用候选处置或完成声明。当前每日源检查仍未全部闭合。

| 来源 | 已核范围与实际停止/限制 | 当前处置 |
| --- | --- | --- |
| Anthropic | 本轮 `https://www.anthropic.com/research` HTTP200，实际提取71个`publishedOn`原字段；窗邻界为04/14T13:01Z→04/22T14:12:30.673Z/14:27:03.434Z | 该公开目录本窗无项；不是读取71篇全文或以modified推定公开。 |
| Google Research | 本轮 `https://research.google/blog/2026/04/` HTTP200，完整April9项；邻界04/16两项→04/21ReasoningBank | 此月Blog本窗无项。Publications year页此前返回771宽库存，历史日级入口缺口仍保留，不把771当全文队列。 |
| DeepMind | 定点读04/18记录的实际连续分页 `/blog/page/3/`，April7项04/30、27、23、22、15、14、02；selected-research既有实际264项邻界04/22→03/22 | 该已恢复目录覆盖本窗且没有04/19–20条目；本行是明确目录依据复用，不伪称本轮重抓或全作者稿更新覆盖。 |
| Meta | 本轮 `https://ai.meta.com/research/` HTTP200约283KB，SSR载荷含预加载失败且未恢复可靠有日期的Research行 | 安全隔离历史日覆盖缺口。已读04/15/18的Blog p1/p2及Publications端点限制，混合日期/2016–2020或超时不能证明本窗零遗漏；不无限换入口。 |
| Kimi | 本轮 `https://api.github.com/repos/MoonshotAI/kimi-cli/releases?per_page=100` HTTP200，100项，尾项0.38为2025-10-24；邻界1.37=04/20T16:01:36Z→1.36=04/17T14:10:46Z | 本窗无release，第一页已越过左界而停；1.37在本窗之后。Blog旧26项最新2025-11-07不构成2026历史覆盖，保留该入口限制。 |
| MiniMax | 本轮 `https://api.github.com/repos/MiniMax-AI/cli/releases?per_page=100` HTTP200，26项到末页；邻界1.0.12=04/26T01:40:29Z→1.0.11=04/17T20:51:17Z | 本窗无该仓release，26项末页停止。已读取04/18 EN/CN Blog的完整12/13项邻界及AgentTech仅一项05/13的限制；只复用具体目录范围，不声称技术报告全部覆盖。 |
| DeepSeek | 04/18具名来源记录实际News16项04/24→12/01、Research06/24→02/25、组织39项至2023-10-20；本轮已读该记录原停止点 | 所列公开目录覆盖本窗且无项；仓库创建目录不能证明所有commit/release无变化。当前不新增全组织release队列。 |
| ZAI | 04/15/18原记录实际 `https://www.zhipuai.cn/zh/research` 15/16行04/29→04/07→04/01，`https://docs.z.ai/release-notes/new-released` 06/16→04/07→02/12，组织53项至2021-05-25 | 所列目录本窗无项；此前release子入口403限制作外部边界，不能用组织目录覆盖。 |
| ERNIE | 04/18原记录实际 `https://ernie.baidu.com/blog/zh/` 两页共10条，04/30→04/15→02/06且2/2页终止 | 此目录本窗无项；04/15模型事件不移入本日。 |
| MiMo | 04/18原记录实际 `https://mimo.xiaomi.com/` Paper8项06/29→03/13→02/03，Blog14无可靠日期、组织18项至2025 | Paper目录本窗无项；Blog日期缺口单列安全隔离，不把无日期当无更新。 |

Seed Blog本轮随后实际读取同API `article_type=2&count=20&order_desc=true&page_token=0`，HTTP200，`total95/next20/has_moretrue`，但实际返回15条而非20；完整提取ArticleMeta.PublishDate及英文Title，08/04至2025/12/23，邻界04/22T16Z→04/08T16Z，本窗无卡片，返回页已越左界而停。第一次错误读取顶层Title/PublishDate输出None，不计覆盖；纠正为ArticleMeta及ArticleSubContentEn后才记上述范围。

复用依据具体为 `../daily-20260418/V3_REVIEW_CHECKPOINT.md` §已实际检查/作者收口/12:12续跑及 `../daily-20260415/V3_REVIEW_CHECKPOINT.md` §来源实际停点，本轮已重新读这些原范围；不复用两日完成判断。Hunyuan“旧36 release请求403/旧22成功”的依据仅是04/17 notes L503：不能继承22子入口的旧窗0结论到本日，也不扩大旧全组织补核为每日58仓库必读或全部commit审阅。本日首查完整9项官网研究列表已核，旧release限制作补充材料恢复边界，不用于本日零事件断言。

这些范围记录不冻结arXiv贡献分母，也不替代精确首次公开的联合证据。AgentWorld与上述不可恢复历史端点均不支持正面采用或零遗漏；恢复可靠原始日期/本窗公开正文后才重开对应条目。14每日来源（13机构加arXiv）均有具名发现入口/有限检查，arXiv日期准入与后续标题信号题摘筛选仍普通工作，不以“Blocked”遮蔽未读。首次实际题摘输出中15400/15408被截断，随后两篇已明确完整补读；抽取到的125额外题名信号不是125确定候选，其余题摘未读部分不预记准入。

## 第一批额外题摘准入信号（尚未冻结）

本轮实际完整读取125个标题信号中的前30篇完整摘要（15343～15557，含两篇截断后补读）。加旧25为55份完整题摘，不继承旧处置。以下是贡献裁决/待消歧，不是评分或Evidence完成；拟保留项尚需官方exact-v1状态/日期联合核及单篇必要审阅。

| ID | 原约束→题摘实际增量→本次准入判断 |
| --- | --- |
| 15343 | 单人autoethnographic闭环案例把情感上下文共存推成attention隔离必失效，但没有控制模型机制或泛化技术失效证据；心理/伦理个案与议程不支撑本项目的新architecture机制，拟前分母关闭，安全措辞交独立抽检。 |
| 15350 | activation spectral指标随reasoning/recall及instruction-tuning方向变化，并用于答前correctness prediction；拟保留为分布/架构依赖diagnostic，不采perfect AUC或universal theory，必要核predictor对照与混杂。 |
| 15351 | gradient probe→layer-selective LoRA+asymmetric rank；只给速度/bounded degradation，尚需最小消歧是否有超出已有importance/rank组合的具体机制或失败边界，不因框架名先保留。 |
| 15357 | frequency scaling不是独立GPU比例：CPU launch与GPU execute异步重叠、pipeline bubble改变DVFS时延估计；拟保留该资源—执行耦合与稀疏profiling分支。 |
| 15368 | 相同payload在隔离输入可检、嵌入日志guardrail失败且出现sanitize-and-execute；拟保留日志证据→执行authority的新受控失效条件，非单纯多测攻击数。 |
| 15376 | zoom第二步相对crop center偏移可估第一步空间误差，要求target在crop/ideal第二步；拟保留无token概率的几何sensor，弱相关/路由不显著不升保证。 |
| 15383 | 对原音频与blurred slow-path重新编码的logits做候选集内contrast，uncertainty/audio-reliance门控；拟保留抑制temporal smoothing的受限解码分支，成本需分账。 |
| 15384 | 合法主任务下side-task sabotage与monitor评估分开，人类攻击轨迹显著超模型攻击；拟保留control评价攻击未饱和/监控分母边界，不把live fixture写为生产已验证。 |
| 15400 | 同prompt bifurcation+跨层/跨步patch显示corrupt/recover不对称；拟保留受限干预反证，早token分歧不独立证明普遍attractor truth。 |
| 15408 | 短pruned ViT的host dispatch floor压过attention compute，pack-attend-unpack与varlen对照；拟保留FLOPs下降≠latency下降的具体短序列边界，必要核新执行与对照预算。 |
| 15414 | MiniGrid continual RL archives/latent alignment与邻域policy复用，source-optimal非transfer-optimal；需最小核其与本项目模型训练主线的直接新增机制，而非将一般多策略RL架构包装为大模型贡献。 |
| 15415 | harmful task通过预安装skill且意图implicit时更易降低拒绝；拟保留skill provenance/authority条件的安全评价分支，LLM taxonomy不当全部registry groundtruth。 |
| 15416 | stochastic sign operator保持unbiased更新，针对non-smooth及LLM FP8/FP4稳定；拟保留优化器机制与低精度失效边界，理论和实测预算分别核。 |
| 15439 | independent endpoints下Gaussian可直线一阶积分、充分分离多模态目标无straight-line flow；拟保留one-shot generative flow的结构存在/不可能边界，限定假设。 |
| 15451 | weak frozen teacher仅early distill、student超过teacher时停止；需最小核是否有成熟warmup/KD组合之外的重要选择边界，不把epoch headline或universal措辞充贡献。 |
| 15453 | coarse-to-fine ordered image tokens让中间状态可由verifier评价，改变search与grid-token可用性；拟保留token结构×test-time search的机制对照。 |
| 15461 | DP统计seed的LLM simulator仍被learned prior覆盖，产生时间/人口distribution drift；拟保留生成器保统计/utility的失效条件，不以金融任务换领域关闭。 |
| 15468 | 六ring semi-executable taxonomy及三个worked cases，明确conceptual/keynote/agenda而非empirical机制；拟前分母关闭，不凭可映射Agent术语入选。 |
| 15475 | 多机器人模块化编码/Zenoh、hybrid CPU/GPU与reduction/broadcast组合，摘要无直接foundation/VLA机制或有意义的新增执行反证；拟前分母关闭一般机器人inference框架，独立核范围而不因机器人一词全拒。 |
| 15482 | unified domain representation+bidirectional teacher/student logit distillation同时处理unlearn/utility/robustness边界；拟保留多目标耦合机制，需核各目标真实对照。 |
| 15483 | 多模态context conditioning区分任务和strategy、纳入失败/自主数据；有具体VLA贡献，但需定点核官方同family是否此前已公开同机制；不扫描PI每周目录，也不把later论文自动当本窗新增。 |
| 15484 | hybrid retrieval disagreement产生embedding refinement triples、query-IDF adaptive RRF并披露rerank负结果；拟保留该自监督信号/排序反证，SQLite/local-first包装本身不构成增量。 |
| 15488 | conditional subspace门控+query-specific steering expert合成分开when/how；拟保留utility保持与定向干预的新条件分支。 |
| 15490 | beneficial code-switch reasoning细分与SFT干预，且非code-switch任务fine-tune也改reasoning语言行为；拟保留跨任务行为迁移边界，不采多语种榜单本身。 |
| 15505 | policy text有gap时immutable memory强化compliant-but-wrong，structured tool-level insights由部署前corrective tests修订；拟保留policy interpretation与authorization truth分责的新失效/修订分支。 |
| 15521 | frequency branch与spatial branch、time-dependent adaptive low/high weighting；拟保留生成路径频率约束与额外branch成本，不以FID第一入选。 |
| 15529 | concurrent reasoning threads跨thread attention交换中间状态，需合成通信/纠错训练；拟保留独立采样→共享推理结构的执行/训练分支。 |
| 15549 | wireless DFL广播mixing graph/asymmetric SGP设计，未显示大模型计算、模型状态或相关训练约束；拟前分母关闭当前范围的一般网络FL图优化。 |
| 15554 | nonlinear functional manifold下NGD的inertial版本；需最小核是否对模型优化新增实质机制，不能因未写LLM或能挂Ch优化单独排/收。 |
| 15557 | logit-lens linear-accessibility profile预测steering层/概念成功条件；拟保留诊断→干预适用性的受控设计信号，相关性不证明none can work或统一跨模型定律。 |

本批最小消歧15351/15414/15451/15554及15483事件身份为普通未读，明确拟关闭四项也未假称独立复核通过。其余题摘普通待读，未按固定保留率或Books主题已覆盖剪去新反证。

## 第二批完整题摘（仍为作者准入草案）

额外序列位置30～77共48篇已完整读，累计额外78篇+旧25=103篇；下表只给实际题摘增量，未评分/预记证据完成。方向清楚而实验详情未读的进入拟保留，事实决定准入含糊的仅列最小消歧，不将缺全文细节当无贡献。

| ID | 题摘新增机制/边界及当前判断 |
| --- | --- |
| 15558 | 外部validated evidence tokens/preregistered trigger与belief revision operator分开、social-only不涨confidence的formal contract；拟保留token exposure/epistemic authority分支，须核可信token/规则前提。 |
| 15559 | safe tasks且显式删除关键词滤去，unsafe轨迹行为仍随distillation迁移；拟保留轨迹动力学与keyword sanitation不同安全对象的反证。 |
| 15574 | semantic overlap驱动旧事实干扰，self-distillation约束drift；无需新知识时freeze factual plasticity；拟保留新旧事实耦合与目标选择边界。 |
| 15577 | reward-weighted CFG作为AR Q-tilting的policy-improvement operator，reward变时不必重训；拟保留生成采样理论，不把molecular任务集扩为AI for Science采用。 |
| 15579 | agent安全benchmark多数未给可验证要求，明确需求可转symbolic checks并作utility对照；拟保留评价要求可执行性/有限enforceability证据，不采general guaranteed安全。 |
| 15583 | 一次local prefill的query-specific attention/differential signal在granularity/token预算下抽取上下文；拟保留selector机制，需与普通attention压缩区分并分账本地prefill。 |
| 15597 | 长委托编辑中稀疏重错累积，tool-use仍不修复且size/history/distractor加剧；拟保留artifact完整性与最终表面task score的评价边界。 |
| 15602 | group-coupled preference objective按每response系数first-order linearization，backprop解耦且保一阶梯度；拟保留训练memory执行机制与NLL稳定代价。 |
| 15609 | local white-box steering model为black-box TTA开gradient pathway、harmonization/consistency与filter；拟保留query成本分支，不把无额外API等同零更新成本。 |
| 15614 | Tsallis扩展BoN/empowerment在toy/locomotion一般RL；需最小核与本项目foundation-model reasoning是否有直接新机制，而非借BoN名称扩大通用RL。 |
| 15618 | execution-signature functional consensus用于code voting/TTRL，但无超base-ceiling自改进证据；拟保留共识≠correctness及label-free更新边界。 |
| 15622 | slow-changing候选class语义由低频cloud LLM给出、least-cost subnet selector维持目标accuracy fraction；拟保留edge执行/上下文更新两频率的成本—质量条件。 |
| 15623 | Padé nonlinear approximations、cacheless preemptive memory bypass于mixed neuro-symbolic workloads；需最小核真实foundation计算负载及bypass机制，LLM开场不作准入。 |
| 15637 | anonymous access token跨设备replay且quota归victim，身份匿名不等nontransferability；拟保留AI服务匿名凭证的cryptographic binding失效。 |
| 15641 | private similarity malware blocklist/cookie验证避免TOCTOU是一般安全cryptographic框架，摘要未连接大模型状态/执行约束；拟前分母关闭，不把可类比Agent工具当论文贡献。 |
| 15647 | civic deliberation utterance novelty/relevance/scope、structured memory与LLM预测human CIG；未给本项目模型/Agent新机制或有效性反证，拟关闭领域对话测量应用。 |
| 15648 | hypergraph新benchmark/12种repr及adaptive representation router；需最小核是否揭示新的表示—能力边界，不单凭first/84K和新domain收。 |
| 15657 | hardware coverage的tied-off/dead-code等不可达上界与token taxonomy；需最小核LLM-agent通用评价/预算反证，不能只把硬件测试已知边界和专用LangGraph提效当贡献。 |
| 15660 | 原题摘工作态曾以DP-trained downstream model引导synthetic data、privacy来自既有post-processing拟关闭成熟组合；后续必要原文发现发布原始属性逐列置换的独立通道，原关闭理由已撤销，见下方定点纠错记录。 |
| 15663 | 原题摘工作态以NL/code/image shared embedding+RAG迁五视觉代码域拟关闭；后续必要§4/6/7发现 query/return 方向、长SVG及未见任务的具体失配边界，已获root有限核恢复为标准Only并正式同步，见下方定点复查。 |
| 15675 | cross-lingual geometric misalignment/exclusivity作为无人工seed mining信号→synthetic tuning；拟保留data selector机制，embedding异常不当culture真值。 |
| 15676 | response反馈效用按retrieved path再分配到KG triplets并更新；拟保留反馈粒度/graph refinement分支，feedback≠事实需核。 |
| 15679 | successor abstraction用于FEP脑模型与FourRooms/MountainCar/PointMaze一般规划，未显示foundation model/大模型系统增量；拟前分母关闭当前范围。 |
| 15694 | CTMC exit-rate/jump-distribution双head、ELBO timing-Poisson/direction-categorical KL因子化及gradient-equivalent loss；拟保留文本diffusion的生成/训练机制。 |
| 15701 | CoT stepwise key-attention supervision与teacher/student跨层mixture alignment；拟保留推理蒸馏的表示/监督support分支。 |
| 15705 | endogenous thinking/perception drift下controlled counterfactual perturbation/偏好优化；拟保留多模态训练的spurious coupling机制，medical/driving结果不扩大AI for Science采用。 |
| 15706 | high-impact neurons的NAG similarity选target预训练数据，跨层/末层及deactivation反证；拟保留data selector与内部feature统计的条件，不把activation sensitivity当完备backbone因果。 |
| 15709 | skill structure外层MCTS、component content内层优化；需最小核具体结构依赖/新执行选择，mature search组合与单OR任务改善不自动收。 |
| 15710 | spoken model先reason、aux agent异步retrieval沿reasoning轨迹解耦toolset size时延；拟保留speech-critical路径与tool management分支，不采完成率为因果/安全保证。 |
| 15717 | domaincontext选择性降低refusal，safety-research context跨harm类别放宽；拟保留上下文×safety边界反证，latent gray region不是安全truth。 |
| 15719 | unresolved question重复时pre-resolution temporal contrast驱动provisional harness修订，resolution再校验；拟保留临时反馈与最终truth分责，不以预测领域绩效本身入选。 |
| 15725 | harmful CoT可注入而final answer不变；拟保留answer-only safety漏掉中间artifact的评价失效对象。 |
| 15726 | position synthesis区分surface/latent/serial compute、声称compute-audited exemplars；需最小核其是否真解决既有证据分歧，不把working hypothesis/议程当定理。 |
| 15727 | algebraic weakest-link/possibilistic logic规则与property fuzz测试，没有新的LLM事实验证或行为证据，拟关闭已知逻辑规则包装成reasoning scaffold。 |
| 15741 | 全token、跨层variance序列学习uncertainty，替代固定layer trajectory/last-token假设；拟保留sensor的信息support分支，不采model/task agnostic保证。 |
| 15751 | cryptographic pointer-chasing/Sybil delay primitive，不是大模型状态/计算机制；拟关闭一般crypto资源证明，不借GPU比较数字入选。 |
| 15756 | unlabeled test stream更新OOD textual prompts、purification与knowledge bank做跨batch校准；拟保留open-OOD语义与污染反馈取舍。 |
| 15760 | 同LLM被问概念能答、无problem frame不能从raw场景识别；拟保留能力触发与task-specification评价的受控边界，不把oracle routing当部署收益。 |
| 15764 | PAC-Bayes exit-depth entropy/expected-depth边界、label-independence放宽到ε近似；拟保留adaptive depth泛化前提，需核路由与标签条件及理论资源。 |
| 15780 | gradient-free unsafe-param attribution/pruning、quantized variants；拟保留参数mask的安全/utility分支，不能用lottery-ticket命名证明唯一unsafe circuit。 |
| 15789 | training-free input/internal/output统一re-eval；需最小核哪项新对照改变有效性/排序，不把taxonomy和“tradeoffs”泛称当贡献。 |
| 15794 | SDFT恢复prune/quant/SFT并以CKA相关性称manifold恢复；需最小核成熟distillation之外的真实机制/反证，correlation不当rigorous causal theory。 |
| 15805 | panorama→interactive sim、semantic/geometric cousins与multi-room consistency，拟保留real-to-sim生成/长horizon数据成本分支，sim-real相关不等物理保证。 |
| 15809 | 正确区域被看见仍答错，按decoding阶段visual activation变化importance调整text→visual flow；拟保留grounding与effective evidence use分开的机制。 |
| 15814 | hand-eye scene pose模型的几何replay+coarse/fine distill，无foundation/VLA或新控制边界，拟关闭普通校准模型continual学习应用。 |
| 15827 | relevance vsdecision-usefulness分别标注且相似度偏前者，LLM也受专业知识制约；拟保留检索命中与实际支持分账的局部新评价证据，不采领域decision truth。 |
| 15829 | text-image协同concept manifold/visual hierarchy erasure并独立测post-erasure usability；拟保留unlearning局部性/over-erasure取舍，需核representation与评价独立性。 |
| 15830 | bottleneck-step重要性与difficulty控制hint分配、渐退scaffold保pass@k；拟保留RL reward密度与探索多样性的训练分支，不采小模型等同32Bheadline。 |

## 第三批完整题摘与当前普通续跑

额外序列78～124共47篇已完整读，累计额外125+旧25=150份完整题摘；不是150候选或150必要Evidence，更不是447全摘要。原始v1字段这125额外均在本日00～01Z，但尚未把字段孤证提升为first-public。以下仍需当前exact-v1/history及联合日期采用核；未给正文/Books预支完成。

| ID | 题摘实际增量与准入草案 |
| --- | --- |
| 15839 | 原ATP题 statement含最终答案使discover被略，Hard Mode发现再prove分开、答对80%但prove低于10%；拟保留评价测量对象/能力混杂纠正。 |
| 15842 | arithmetic任务早层识别而结果晚层生成、成功/失败模型attention/MLP分工不同；拟保留内部readout与计算能力区别的受限diagnostic，不采唯一circuit。 |
| 15847 | CoT中待忘信息未随final answer删除，counterfactual traces/迭代偏好重新更新学习数据；拟保留unlearning对象及推理/知识保留耦合，complete remove需安全核。 |
| 15849 | 小music model、已知audio encoder+linear projector/3.5M数据，仅任务比率/规模headline，未给新的模型机制或适用边界；拟关闭成熟模态alignment迁用。 |
| 15851 | 给算法及假设查DP保证、textbook与advanced correctness差异；拟保留LLM参与隐私保证审计的有限能力/可靠性反证，不让LLM拥有数学保证authority。 |
| 15859 | 数值forecast interval width/coverage分账，极端量级校准恶化且90%目标失败；拟保留point/binary评价测不到的uncertainty有效性边界。 |
| 15871 | visual edit统一protocol+judge distillation，摘要只称human agreement/低成本；需最小消歧跨paradigm比较是否揭示新有效性条件，而非新taxonomy/小judge配方。 |
| 15873 | 同LLM pragmatic listener与speaker能力弱一致；拟保留judge与generator角色不能互代的受限对照，不扩为全部语言judge正确性。 |
| 15898 | symbolic XAI替代Shapley/SHAP的ongoing efforts overview，无新模型机制/综合证据解决具体分歧；拟关闭概述。 |
| 15911 | video diffusion四类加速/两成本目标taxonomy与未来agenda，未给新的comparative evidence/失效边界；拟关闭普通综述。 |
| 15917 | 固定editor的small-target/implicit-spatial/underspecified任务可由adaptive reformulation改变有效operating regime；拟保留输入任务与容量归因分支，额外Agent计算/选择偏差需核。 |
| 15919 | user-agnostic continuous HPC benchmarking/CI软件工程组合，无新大模型测量/执行条件；拟关闭成熟benchmark pipeline扩展。 |
| 15923 | codec-RVQ层级把speaker/content与prosody分别由lip/identity与expression条件驱动、dual-scale norm；拟保留生成representation层级×conditioning分责。 |
| 15938 | loss predictor采样hard例、视觉subtask复杂度联动denoise steps与action execution horizon；拟保留Diffusion Policy质量/timeout预算分支，不采any-model-agnostic保证。 |
| 15944 | dual-bank standard-cell SRAM CIM+INT8 weight feed/LUT split-softmax；拟保留attention nonlinear与MAC内存执行耦合，28nm/两voltage操作点不冒称实际大模型能效。 |
| 15945 | token hallucination detection head与LM联合训练改变状态separability；拟保留posthoc sensor→training signal的分支，head confidence不当事实truth。 |
| 15948 | editing/reconstruction分支dual entropy attention协调与latent refinement、保留/编辑指标合并；拟保留冲突目标的局部控制机制，作者metric不独立证明质量。 |
| 15951 | graph/LLM/Agent四用途/多modality taxonomy跨domain罗列，无明确新证据解决知识分歧；拟关闭综述索引。 |
| 15958 | 同RAG分别dataset/answer阶段匿名化，privacy/utility随位置变化；拟保留放置点影响暴露对象与检索质量的受限对照。 |
| 15967 | 单安全概念组合即可产生unsafe图像，过滤/erasure对unseen组合失效；拟保留composition攻击面与单概念安全验收不同边界。 |
| 15972 | swarm配置教meta predictor角色权重→弱角色重复采样quota；需最小核相对成熟weak-link/resource routing的重要机制/反证，不因两stage新名保留。 |
| 16009 | rubric/centering依赖评价“最低”不等绝对deficit，social-summary rendering待v1.5修复；拟保留方法有效性/版本纠错信号，先核exact-v1而非后改摘要回拨。 |
| 16021 | code localization keyword shortcut消除后退步、LLM产Datalog由parser/mutation反馈后确定性执行；拟保留benchmark混杂纠正与结构遍历authority新分支。 |
| 16022 | navigation confounds social reasoning，由Planning Oracle拆开仍近随机deception；拟保留agent组合能力测量与替代瓶颈，不以Elo/新game入选。 |
| 16027 | 3 posttraining lineages把data composition、方法、CoT格式、正确答案多样性分开；拟保留collapse归因的controlled反证，不把禁CoT当恢复多样性。 |
| 16029 | prefix级learnable internal STOP token裁掉futile并行path；拟保留预算内早停信号/训练支持分支，fixed-compute对照需核。 |
| 16037 | stochastic canonical/noncanonical tokenization跨pretrain/SFT/ICL影响扰动鲁棒且推理成本可不增加；拟保留训练token distribution与部署扰动边界，不仅accuracy operating point。 |
| 16042 | intrinsic interpretability五paradigm与未来方向，无新检验或综合证据解决具体分歧；拟关闭taxonomy综述。 |
| 16044 | train时SNR与t绑定、生成trajectory偏离造成bias，frequency differential correction；拟保留diffusion训练/采样状态对应及纠偏分支。 |
| 16054 | 八visual cognitive任务/human-model分数差与高层错误tax，无具体控制发现新测量/模型机制条件；拟关闭仅新benchmark条目/局部能力数字。 |
| 16056 | latent source recomposition保留非编辑片段、mel AWFG控制边界与WDTW时序评价；拟保留speech editing保真/自然度/temporal fidelity分支，latent保存不预证明waveform无损。 |
| 16060 | text-CoT降低visual spatial表现、No-Image++揭示无图仍text-prior作答；拟保留视觉reasoning评价及语言计算的受控反证。 |
| 16070 | table HTML/text/coords单序列、已有OCR/Transformer轻量组件与MTP，未给成熟sequence interface之外重要机制/边界；拟关闭专用表格识别组合。 |
| 16076 | CBM concept由visual prototypes提供可见证据/human intervention；需最小核是否超出已有prototype/CBM组合的重要对齐机制，不能因一般网络或可挂representation独自判。 |
| 16079 | flow-match pruning50%及architecture/train变仍固定seed输出相似；拟保留latent mapping稳定性的受限实证，非普遍兼容/无需data保证。 |
| 16088 | VEF对NEST/GROMACS/LAMMPS/PATMOS HPC拥塞trace扩展，未给大模型通信/状态直接贡献；拟关闭一般网络测量，不以intro deep-learning或GPU术语入选。 |
| 16090 | device availability/data co-correlation使PSP同步sampling有persistent underrepresentation，AW-PSP按failure history预测采样；需最小核是否直接改变模型训练分布/同步主线，非凭FL/Markov/DHT系统术语收。 |
| 16108 | transcript与reference style joint condition的speech-driven animation，无新增operator/失败边界，拟关闭成熟多条件diffusion迁用。 |
| 16114 | reference/content共同in-context diffusion+style scorer reward用于photo tone transfer；需最小核是否超出成熟reference conditioning/learned reward的明确选择边界。 |
| 16135 | compound motion早动作被后动作覆盖、cross-attention collapse，由decoupled structural attention masks限制；拟保留并发动作语义/物理结构的生成控制分支。 |
| 16146 | proxy-guided AR两路径可归图模型而差在rejection criterion，ambiguity使confidence gating失配、conservative bet替换；拟保留受限采样选择边界。 |
| 16158 | additive attention mask提取影响CoT token、saliency reward+outcome GRPO；拟保留reasoning influence训练目标，影响预测≠faithful reasoning或truth。 |
| 16171 | JumpReLU在LoRA blocks诱导动态sparsity降低task interference；拟保留adapter参数support机制，gate不预证明无共享参数干扰。 |
| 16197 | output gradient outer-product RH/GH双channel及CountSketch替代全层gradient index；拟保留data attribution的memory/quality可行性分支，sketch不等完整影响truth。 |
| 16198 | 原题摘工作态拟以requirements重述/自检循环无可靠spec authority关闭；后续必要§3/表2发现生成前QA检查与生成后代码→遮蔽需求反向校验的具体分工及有限消融，已获root有限核恢复为标准Only并正式同步，见下方定点复查。 |
| 16211 | NVV control/placement/salience与普通speech质量分开，低SNR/long affect瓶颈；拟保留语音评价支持集/操作点边界，不因45类taxonomy本身收。 |
| 16217 | input reshapes entropy across depth的LI score进入split conformal，surface score domain shift失配；拟保留nonconformity signal分支，exchangeability外实测不冒称有限样本覆盖保证。 |

当前最小准入消歧普通队列：15351/15414/15451/15554/15614/15623/15648/15657/15709/15726/15789/15794/15871/15972/16076/16090/16114；15483同family早发、16009摘要/版本修订需原事件核。旧25中15367/15671/15802/15877也仍需按其具体贡献事实消歧，未继承旧V2.1评分/Books。日期晚段和后改字段仅按具名潜在贡献隔离，不把其余全部宽库存挂pending。未完成正文属于普通工作，不伪Blocked。

**16054 后续定点修正：**上表的前关闭是早期摘要判断，现已撤销。否定侧抽检实际读[官方 exact-v1](https://arxiv.org/html/2604.16054v1) §4–5/Fig8–9/Appendix A/B.8，发现 prompt×能力操作响应方向不同及有限分辨率对照，可能改变 Ch66 EvalSpec 的切片与提示臂分账；已恢复为潜在5分标准审阅，不因名为benchmark直接闭合。统计和机制边界见[V3_NEGATIVE_SIDE_SCREEN_LEDGER](./V3_NEGATIVE_SIDE_SCREEN_LEDGER.md)末节；尚待非作者核，不预先计正式候选。

## 精确续跑位置

### 2026-09-27 lane 接续后的实际最小消歧

接续作者`/root/apr20_resume`实际重读AGENTS、三份V3合同、Prompt、ROADMAP及最新April学习checkpoint；未修改LS/月checkpoint/共享Books。前述447宽库存、150完整题摘和九项口径校准按各自真实范围复用，不继承旧V2.1处置。当前README尚未完成，以下是普通准入/证据工作，不是独立验收。

- `2604.15351v1`：实际读§3–§6。五批gradient probe分八层chunk、top50%选择后标准对照均使用rank16；asymmetric rank只出现在Qwen3B单模型recipe search支线，不能混作跨模型headline机制。14成功模型的200-step/3-seed比较保留matched-step与compute-matched区别、200问MMLU子集和Pythia fp16 NaN失败；未给等层数random/depth选择对照，所以还不能将wall-clock收益因果归于gradient ranking。拟围绕选择性adapter执行成本的窄分支准入，三维暂定2+1+2=5，未核Books具体覆盖。
- `2604.15414v1`：实际读§1–§3入口。PPO base周围MAP-Elites policy archive、trajectory embedder、anchor/replay/alignment/periodic reembedding维护可比较坐标。source-optimal与transfer-optimal区分不是一般“多策略框架”应用包装，直接研究神经policy保留与再学习的约束；不因MiniGrid、未写LLM而关闭。拟保留该学习机制，仍须必要对照/评价后决定是否只报告或长期采用。
- `2604.15451v1`：实际读§1、§3及§4.1–4.2/Table1。正文明确moderately weak teacher（作者操作带up to15% weaker）、warmup–hold–decay、两次连续validation surpass后永久停止distillation；这种teacher gap×停止条件改变早期训练选型，不是仅成熟KD组合提分。first@tau是epochs/steps，不等总wall-clock；teacher预先可用、active阶段新增一次forward，不能采universal speedup。拟准入，继续必要反例与cost accounting。
- `2604.15554v1`：实际读§2–§3.3及Gram/pseudoinverse定义。functional tangent Gram与parameter Euclidean momentum的区别属于模型优化主线，不因PDE/浅网络实验一概拒绝；当前普通待办是其inertial transport/更新定义与实际比较，不要求所有数学附件。
- `2604.15614v1`：实际读§1–§2。Tsallis/entmax E-BoN用固定N下额外参数调探索强度，并针对state-dependent empowerment提出constant-cost近似，直接触及采样策略与固定控制预算的取舍。foundation-model BoN是动机而非已验证负载，不能将locomotion结果外推LLM；拟准入窄采样机制，仍须必要公式及对照。
- `2604.15623v1`：为判断scope实际读§1–§2及Table1。原workload是NVSA/LTN/LNN/NLM的symbolic binding、codebook lookup和fuzzy operators；Padé与dual-window address bypass虽有硬件贡献，原文未建立foundation Attention、模型状态或其训练/推理约束的直接研究桥。拟范围关闭这一特定NSA负载，不用“非LLM”或“小模型”作共同硬门槛；交独立抽检。
- `2604.15709v1`：实际读§1。结构edit path改变后续可行编辑、inner refinement family依结构分派、conservative selection返回outer MCTS，显示真实structure/content依赖，不因MCTS成熟而先关闭；仍须必要方法/对照判断是不是值得保留的设计分支。
- `2604.15877v1`：实际读§1–§2入口及Figure1。5–20/50–500/1000+ compression ratios原文注明approximate，没有统一成本—质量协议；“missing diagonal”是20+系统映射/研究议程，不是新adaptive mechanism。拟前分母关闭其taxonomy/议程增量，不能据cross-citation低率宣称技术失效；尚待独立否定侧抽检。

日期本轮实测：官方availability再读§ID assignments/Announcement Schedule/2026 holidays；arXiv ID在公告过程才分配，04/19 Sun20:00EDT→04/20 08:00北京，04/19–20不是列出holiday。`cs.AR/2026-04?skip=0&show=2000` urllib返回200/227整月标题，这是补检入口不是日归属证明；网页工具同cs.CL请求429也不是全源零命中。待结合原始OAI窄批次、连续ID边界与官方槽形成联合证明，不以created/Submitted/Updated孤证采用。本文所列材料无新Books申请，单篇准备好后继续提交独立source/owner审阅。

上段“尚无Books申请”为接续早期位置，不覆盖以下进展。十四每日源的实际停点与外部限制已整理正式日报，窄公告原始批链保存V3_DATE_RECONCILIATION.md；完整V2.1归档保留旧反证但不继承结论。FLAME/LogJack按apr02具名必要原文→当前owner审核实际写入Ch70/72，root实际写后通过；两项真实I不替代日期/准入/全日Gate。其余普通工作继续，无stage/commit/push，未改LS/月checkpoint。

### 后续必要正文实读与未决范围（同一作者，非独立Gate）

以下均实际读取官方exact-v1 HTML或既有可核exact-v1缓存；位置指原文章节，不以只读题摘充作标准完成。记录必要对照与反证，未列为全部已裁决，Books具体比较仍须执行。没有遍历所有附件。

- `15414 TeLAPA`：继续§3–§5/Table1/Fig1–7。PPO policy library保留source-competent邻域，短transfer probe选种并reset optimizer；latent embedder变化用anchor/replay/distillation与periodic全archive reembedding维护坐标。五MiniGrid任务/反复访问/新seed、20runs/95%CI；full SR .706/TTT3.35M，ScratchReuse .525/5.49，Static .507/5.59支持有限再学习分支，但ScratchReuse的BWT/nBWT部分更好，full coverage .50不等全部学会。source-best≠transfer-best在35.5%任务对出现，local邻域差异不等通用因果机制；lineage相关而非干预。未来工作明确archive构造/空间维护/lineage causal分离仍需验证，probe、library、reembedding成本不能漏。2+1+2=5拟标准，普通owner比较继续。
- `15451 weak-to-strong KD`：§3/§4.1–4.2/Table1已读。预先可用且差距适中的弱teacher、warmup/hold/decay、连续两次validation超越后λ永久归零；epochs/steps first@target不当wall-clock，active额外teacher forward/teacher上游成本须分账。≤15%gap不是已证普遍定理，2+1+2=5拟标准，必要cost/gap反例还须读。
- `15554 functional NGD`：§3.2–4.3/Eq23–35实读。旧momentum属于旧tangent，用cross-Gram/当前Gram伪逆投影到新tangent；QNHB直接复用参数momentum是近flat manifold近似，NHB-FD双forward差分免存旧Jacobian但仍需Gram。原文说明低sample估计误差与cross-Gram成本，尚需必要evaluation/结论；不是因PDE/浅网络而排除。
- `15614 E-BoN`：§2–§5/Eq16–19、Table2实读。固定N候选，entmax α改变稀疏/重尾形状，β用非负empowerment均值缩放；empowerment p_e/p_m额外模型、SAC off-policy条件保留。作者λ近似求解与α平移不等原entmax精确实现，J固定模型均值非完整MC期望；J全零分母与formal divergence符号等必要条件未可默补。50seed CartPole/PointMass、8seed三locomotion报告IQM/IQR，E-BoN并非Walker/Quadruped最优。拟5标准，只采受限采样分支，不外推foundation/LLM或恒定端到端时延。
- `15648 HyperGVL`：§3–§5必要正文已读。2400 metaproblems×35 representations=84k，7text/5visual；同problem representation effects、higher-order超边在pairwise V-V中丢失、HO-inc/planning较好但非任意task最佳。12VLM zero-shot、手工容许格式错但答案对；对应LM/LVLM不是严格model控制。DeBERTaV3 question→HO-Neigh经验标签router8:2与1000newproblem分task检验，保留表示选择条件，不恢复protein领域任务。拟5–6标准，普通实际owner比较。
- `15657 CovAgent`：§III–VI必要方法/对照/限制实读。同GPT5.2/temp .4/3runs，19RTL designs100～8500LOC；7原子tool/structuredfeedback/context pruning，方法学ceiling（tied-off/infeasible/deadcode）与protocol/pipeline reasoning frontier分开。400k～1.2M vs30～100ktoken是组合对照不分组件归因，mini复杂任务仍fail；诊断不等可靠修复/自动coverage waiver。表里38/35单位口径未厘清，不采用精确该数。拟5标准，真实evaluation failure解释可保留。
- `15709 bilevel skill`：只读入口，outer结构edit改变后续inner可行编辑族并返回conservative selection；必要methods/eval仍普通可执行，不伪完成。
- `15726 latent reasoning position`：§3.3–§5.3继续实际读到原文有经验程序，撤销“只有模板/无实验”的早期猜测。S/Z/B六arm逻辑角色、预算含decode/KV/hook/verifier/tool/branch calibration，§5两表称3模型一致及latent ablate/patch matched-sham支持regime-dependent分歧。具体model身份/分割/预算weight/完整结果均指AppendixA，采用这些量化与causal命题必须定点读A，不能当普通综述关闭；main-only尚不足支持headline。
- `15789 training-free trustworthiness`：实际读taxonomy后进入Training-Free in the Wild必要setup。不是只有既有术语综述：Llama2-7B/Llama3.1-8B/70B/Mistralv0.2，安全/真实性/偏差、utility、攻击/over-refusal/watermark persistence及method composition统一比较。收益/排序/成本与组合结果未读完；继续必要结果，不因survey名称排除。
- `15794 SDFT recovery`：§4–§7读完所需机制/表/limitations。Qwen2.5 3/7B、NF4或10%FFN pruning；quant目标taskgain可能额外adapt，不能全归因恢复损伤。prune SDFT Tooluse后MMLU仍net−2.55；expert teacher任务利好与general退步，CKA排序≠质量排序。last-layer 35/36、507 samples CKA描述与formula normalization语义需谨慎，§6明确correlation≠causation/CKA不等功能；不用abstract“rigorous causal theory”覆盖作者明示限制。two-stage大teacher offpolicy bootstrap+small onpolicy多一训练阶段非严格total-budgetcontrol。拟5标准，generic teacher/recovery选择，不恢复science应用。
- `15802 CHOP`：§3–§5必要主文已读。CNM category/noun/model prefix按adjacent contextual difference继承或重提取；Gemma12B/temp0/textembedding3large3072/Chroma固定，相较500tokens/100overlap与cosine.35基线。top1Hit .9077 vs .8128，top10收敛；generation F1 top1 .2760 vs .2763、top10 .4080 vs .4072，不采用“全部显著改善/+.0266～.0753生成收益”混用retrieval表。无prefix/CD单独ablation或全成本，不声称消除hallucination。成熟contextualretrieval与其具体继承条件的实际增量比较尚普通工作。
- `15871 UniEditBench`：必要methods/eval/limits实读。710triplets=633image/77video、grounded source/target/prompt统一两类接口，新taxonomy alone不够；rubric“orthogonal”不是统计独立。Qwen3VL235B→4/8B两stage judge KD，8B某stroke MSE .32 worse .31不是全维better。50参与者5组无sample overlap却称5完整pass语义含糊；main未披露judge train/test隔离不据此断言leak。latency缺完整同hardware/input条件，只保留协议有效性限制。拟5标准，是否真正改变评价选择的准入待具体裁决。
- `15972 WORC`：§III–IV及tail必要主文实读。swarm权重优化→meta MLP→低权重角色repeat quota，权重不等∂f/∂w或causal weakness；repeat context依赖，不独立采样。4agents同额外4次讨论比较82.2/80/80.9但不是token match，GPT4o/6tasks的accuracy/F1均值不称统一accuracy。cost表8.34 vs4.62单位不补造、avg79.7→81.7与main82.2/77.4不同口径；component/crossdataset比较支持有限predictor而非普遍弱环节理论。拟5标准，额外0.78～1.92×compute与人工κ .78/.72也不是causal truth。
- `16076 PGCM`：§3.1/§4.2–4.3/§6–7必要内容实读。part segmentation→categorical visual prototype→concept decoder→concept-onlytask形成可见编辑接口，不以可解释名称作保证。ColorMNIST+/CelebA/CLEVRHans、3seed；concept编辑/删除改善有限噪声场景，CelebA低于CBM且coupled干预更弱，更多prototype容量与人工认知成本trade-off。没有独立humanalignment userstudy，segmentation先看全image不能直接说masked outside pixels从未影响表征。拟5标准，不因非LLM硬排。
- `16090 AW-PSP`：§2–§3入口/Table1–4实读。failure与data co-correlation使同步selection覆盖失衡，10clients/Mininet/ResNet34CIFAR10/FedAvg50rounds/5retrial；1000device traces是WiFi/charging availability proxy不等真实训练。accuracy只计算covered labels，missing classes排除，所以“one-active85%”不当全类quality；dash不改成zeroaccuracy。EWMA/Markov/DHT选择机制与后续fairness/eval仍须必要补读，不因FL或小ResNet关闭。
- `16114 ICTone`：§3.1–4.1/Table1实读，reference/content in-context FLUXFill拼接+mask/LoRA+ReFL tone reward，100ktriplets/2kmanual/20khumanrank与PST50。原文当前只把成熟multiimage conditioning和learned reward迁到tone任务，未给新factorization/operator或对照剥离后的机制有效性条件；拟前分母关闭这条recipe，不用图像编辑/规模作硬理由，交否定侧抽检。ΔE12.81不优SALUT11.25也保留，不删反证。

下一实际工作：收束上述最小消歧，按贡献入口确定family而非任意缩池；必要当前事件withdrawal/correction/revision signal轻核尚未完成；首批其余TCD/OneShotFlows/PersonaLedger与准入已清楚的材料按评分必要审阅。旧25可核证据分别复用并比较实际owner，不接受通用Existing。日级来源/日期/准入/Books最后交非作者，之后立即接23→26→29。

### 再接续后的必要证据收束（作者审阅，不冒充独立Gate）

恢复后再次实际重读AGENTS、当前三份合同、Prompt、ROADMAP与最新相关checkpoint；按当前V3继续，不扩月份/Weekly，不把已有150题摘改成冻结贡献分母。以下补读覆盖前述未完的必要事实，保留原有效证据并收窄早期猜测。

- `15383 TCD`：§3–4.6/AppendixA与必要AppendixB实际读完。Hann temporal blur重编码的慢路径保留粗声学结构，依audio reliance×entropy启用top-K union正向logit差更新；§3.2 waveform与§3.3 Eq1 encoder-state blur的描述不宣称严格等价实现。Qwen2.5-Omni总体71.5→73.2但Speech70.6→69.7；非unified架构不获同收益，不能从比较推普遍架构因果。AppendixB/Table7单A80080GB/eager attention（两边关FlashAttention）、3秒音频/100输出tokens：prefill76.9→156.9ms=2.04×，decode26.1→25.8ms=.99×，peak15.85→16.05GB=1.01×；prefill脚注假定原stream KV复用的优化实现。dual stream batch2在此memory-bound条件下隐藏增量，不证明任意长度/并发/服务零总成本。实际Ch23内部视觉反事实/不确定性gate尚未承载audio temporal-reference的可见性条件，拟6分缺口深入，源→owner独立核前不写。
- `15554 Functional NGD`：§3.4/§4.2–4.3/§5–6必要原文实读。当前与旧tangent生成系的cross-Gram把历史函数momentum投影到当前tangent再映回参数，不是直接复用旧parameter momentum；NHB-FD以两次forward的有限差分避免保留完整旧Jacobian，QNHB近似在局部平坦假设下成立。spectral flooring/clip/步长影响稳定。MackeyGlass浅层10sigmoid、500train/500test、50realizations的median，XOR1800/900及小PDE数值例；迭代数减少不等wall-clock同比，FD近似可更慢/发散（减β稳住）、line-search额外成本，小batch/vector-valued仍futurework。只采用模型函数表示与历史更新坐标的机制，不恢复AIforScience应用或宣称LLM训练加速。实际Ch28逐样本残差/局部Jacobian段有当前更新无历史tangent transport，拟5分缺口深入，待非作者核。
- `15451 Weak KD`：继续§4.3–7必要反例。不是任意更弱teacher有效：classification极弱MobileNetV3Small→Res50为.51×，moderate Res18→Res50为4.75×first@65；固定RetinaNet架构不同checkpoint的AP50约12.8过弱、19.5适中、26.2过强比较使强度选择不只归因架构变化。generation过弱/过强无收益、moderate有2.67×到达目标步数；温度6→1、warmup/hold/decay和学生连续两次超过后停止限制采用。梯度norm/方差变化不是distillation胜于梯度rescaling的因果证明。teacher已存在成本与新训练/复用次数分开，正文指wall-clock在supplement但未实读该成本表，不把step gain外推首次全周期净加速。
- `15726 latent reasoning`：实际定点读AppendixA.1–A.5/B。撤销“无实验”猜测：Qwen3-8B/32B/Llama3.1-8B，受控arithmetic/graph/world-state/code与GSM8K-Platinum/HotpotQA/MATH500/HumanEval，Tables7–9确有逐模型预算frontier/AUC结果。A.3列surface6/latent5/compute5通用library，A.4仍只定义budget权重符号与tight tolerance，没有实际校准权重/容差数值、样本split数量/seed数、sham layer/rank/window与选中配置；§5.1指A含split sizes而A没有具体数。官方HTML未给承诺complete code/supplement具体artifact入口。拟仅将matched-budget量化和latent necessity/patch-specificity中央保证隔离为争议，不抹去有效逻辑角色、协议、三模型表和文献worked ledger；可重开材料是上述精确控制条件/数据分割及具体Supplement链接，不要求复现或全部附件。
- `15789 Training-Free Trust`：必要结果/限制实际读完。4模型、默认原recipe跨family转移有失效（SEA-T在70B HB utility1.0下安全效果为0）；8个手选组合未得三轴全增，不能说所有组合必失败。HB non-refusal phrase检测不是实际harm，BBQacc/TruthfulQAMC与Gemma3-27B judge utility分开；watermark green-token占比不是完整抗攻击保证。70B GCG/AutoDAN未跑，成本只MTBench单A100并且输出长度不同，不能将wall-time归因唯一机制。当前Ch72“Security Gate必须覆盖Defense Interaction、审计通道与部署变换”实际正文已承载组合非单调、interaction matrix+clean utility+分攻击失败归因；拟6分标准已有覆盖只用于这个窄命题，不采用通用排名/普适零成本结论。
- `16090 AW-PSP`：继续§3.2–4.2.5必要主文。Eq13风险为加权correlation和、Eq15probability乘(1−risk)，原文没有明确clamp与归一条件；Algorithm1取top-N但正文还加freshness与greedy class-coverage，不能合成严格概率无偏/代表性保证。fairness两个loss variance只对本轮covered classes定义，KL/Gini与缺失类另列；Gini公式对象client participation但结果文字说class，保留口径不一致。Table5noise升高时AW accuracy33.75→29.78下降11.8%，大于PSP相对下降3.6%，不能采全指标更robust。100/300/1000/3000逻辑client用10实际worker分波，不是3000设备真实部署；模型章节Res34而资源节Res18两者不混成唯一配置。拟5分标准窄保留availability×data co-correlation选择分支，不能把未读Appendix保证当中央证据。

当前官方abs事件页轻核已覆盖22项：15357/15368/15351/15414/15451/15554/15614/15383/15439/15461，及15623/15648/15657/15709/15726/15789/15794/15871/15972/16076/16090/16114。页面未提供comments；所见没有实际withdrawal/correction/erratum信号，security仅15368的cs.CR分类不是revision说明。15414(v2 Jun9)、15451(v2 Apr21)、15439(v2 Apr20 15Z/v3 May7)、15657(v2 Jul5)、15794(v2 Aug18)、16076(v2 May21)、16114(v2 Aug15)仅版本变化不启动全版对比；其他实际贡献事件仍待逐项轻核。Submitted历史值只识别版本，不作为首公开日期。必要源/owner与日级Gate仍分别未完。

apr01在V3_APR01_THREE_SCOPE_EVIDENCE_AUDIT.md实际必要原文独立通过15671/16114具体前分母关闭、15461五分标准仅报告。作者前两项原机制事实未改，不因范围窄或非LLM硬拒；15671AIforScience化学实验组合不经VLA/MCP类比恢复，16114concat/mask+FLUX/LoRA/ReFL只提供tone应用recipe，不是生成factorization/部署边界增量。15461有界statistics→LLM simulator的分布失配证据保留；Kaggle明确synthetic消费者，80k/25%与约5k/3% support不匹配、schema统计未全传播，不能升级真实金融、唯一架构因果或统一DP预算保证。正式日报同步其真正Only，不计两项关闭为候选，原八项calibration仍未完成。

### 后续四项必要审阅（普通工作继续，非日级通过）

- `15350 Spectral Geometry`：实际读v1 §3–4.7及必要B.1–B.3/E.1–E.3。SVD power-law slope α与10token window是diagnostic定义，不等thought semantics；prompt/response处理与base/instruct会改变符号。11模型21任务、6模型每200problem的5foldCV，8RTX4090/float16/greedy，prediction max200/batch1。AUC1 headline混用Late/response措辞，feature到底在答案前何时可用未清楚，未披露nested/选择后heldout；Pythia全wrong为单类不能当通常可计算AUC=.5证据。最关键反证是OOD仅40题7B AUC .600±.10、3B .44±.29；§4.7解释correct低α而E.1却说correct高α为同方向，code tracing方向再次反转。拟6分因中心诊断冲突深入，隔离perfect/答前/通用低α保证，保留模型依赖geometry与这些原始表；只需feature时序/方向、原protocol条件或更正可重开，不全理论/代码/所有图。
- `15376 Zoom Consistency`：§3–7实读。c=∥p2−crop_center∥，只有target在crop且第二步准确/坐标映射未被边界clipping改变时c=∥error1∥/r；同r/normalization让几何量可比，不证明成功概率校准。ScreenSpotPro1581、KVGround8Bbf16与Qwen3.5-27BAWQ4、r=.5/greedy/H200；Qwen484unparseable非随机，1097parseable较易子集，不把AUC.588/.600外推全部输入。router80.9vs80.1、48gains35losses/p=.19，实际4forwardvs2成本×2；信号嵌入已有双zoom“free”不等跨模型router免费。实际Ch23主动crop已有cost/provenance/evidence sufficiency分责；本篇新增有条件局部几何sensor但未改变全局grounding/可行性判断，拟5标准Only，不因局部/negative关闭贡献，也不将raw geometric distance当confidence guarantee。
- `15384 LinuxArena`：§3.2–3.5/§4.1–4.3/§5.1–5.4/§6必要主文实际读完。live/delayedfailure分别必须harm前flag与可轨迹后审；分开main/side-task scorers而attacker未按main质量评分，不把合法任务成功同时维持当已证明。monitor用2calls mean、honest score percentile设step-wiseFPR及tie随机，Safety=Pdetected/(Pdetected+Pundetected&success)不是单段生产风险率，步骤级FPR不是episodeFPR。LaStraj人工≤8h迭代到指定monitor≤5score、main可新增；synthetic exploration后被抓轨迹过滤，model比较也按side-success条件过滤。证明所见model elicitation未饱和，不证明人工最坏上界；synthetic placeholder/无CI/CD、有限20环境、scorer干扰与accidental successes限制生产外推，原文不是完整控制协议评价。拟7安全深入Existing：实际Ch72“Control Evaluation要测试Attacker如何选择攻击时机”已冻结generator/selector/attempt/auditbudget并明示elicitation不足只为已见攻击下界，Ch66attack profile也不保证baseline穷尽。只采用该具体已有命题；不声称现章包含全benchmark/全部stepFPR具体配方。
- `15400 Trajectory Commitment`：§3.1–3.5/§4.1–4.7/§5.3–5.4/§6实读。单Qwen2.5-1.5B/28layers/AppleMPS，61prompt20sample/T.7 substring correct/hall/Other；8bifurcating×3=24cells patchlastposition。最佳C→H L20 .875与H→C L24 .333不是同layer或已校正max比，28层无multiplecomparison correction，random控制p=.056、wideCI保留。step sweepL20step1 .292、window single .125与controltable同坐标 .333口径未解释，不采精确同坐标增益/需要sustained才能修复的保证。作者明确first divergent token改变后续输入，测fork consequence不是fork机制；prompt probe跨类别信号r=.776，withinconfab/falsepremise不显著，factualp=.066，不能当逐prompt未来truth。拟5标准Only保留有限干预方向非对称与负steering结果，不升为universal attractor、缺knowledge不是原因或普遍重写介入规则。

官方事件页随后实际轻核15350/15376/15384/15400/15408/15415/15416/15453：未提供具体revision comments，15384(v2 Apr27)、15408(v2 May12)、15416(v2 Aug25)只有版本变化；security是CR分类/abstract threat背景，15400的correction只是论文干预术语，不是erratum。此次未出现决定处置的真正withdrawal/correction说明，非未来缺失证明；不会因此展开全历史。累计具名轻核30项，不计未核其它潜在线索。

### 压缩恢复后的四项必要证据与具体 owner 比较

再次实际重读当前AGENTS、三合同、Prompt、ROADMAP、月checkpoint最新入口与相关LS，不依据summary代替。15383/15554按apr02必要源→owner通过后实际窄写Ch23:816–818/Review844、Ch28:444–446/Review1421；已通知root释放两锁，真实写后仍待核，15554正式题为Natural gradient descent with momentum。未改LS/月checkpoint，未stage/commit/push。

- `15408 Dispatch Floor and Ragged Attention`：v1 §III–VII必要实读。DeiT H12/d64、N≤197、A100SXM40、PyTorch2.8/Triton3.4/FA2.7、10warm/500timings；FA2约.063ms与Triton约.04ms的floor差异是wrapper路径解释，不是独立host分层测量。BS64/N197 FA2 .113ms反而快于Triton .207ms；真正端到端对FA2在BS≥32仅约≤1%，小batch约5–8%，对padded最多2.24×分母不同。pack/cu-seqlens和CPU标量sync成本仍在，bidirectional online softmax不含causal/KV/dropout。25%prune81.7vs82.2、50%78.7不能说无质量代价；TableV max-logit差.0048/.0063/.0059而top1一致不等bit-exact。拟2+1+3=6标准已有覆盖，实际Ch49“从逐Kernel Launch到Persistent Executor”的launch-bound选择与TaxBreak/WebGPU分账已要求profile拆层和残差不作直接API测量；只采用这条具体已有命题，不声称ragged算法全被覆盖或T4/GTX1650有FA2对照。
- `15416 StoSignSGD`：v1 §2/§3.1–3.2及必要AppendixB.2实读。均匀噪声sign转换在非零包络满足|m_i|≤sigma_i条件下，期望是m_i/sigma_i而不是原gradient本身；历史max包络与耦合state/∞norm改变预条件几何及方差，理论依赖bounded domain/历史二阶界或well-behaved非凸条件，维数因子不能脱离范数口径称无维数代价。B.2明确GPT2-124M/OpenWebText、13.1B tokens/50ksteps/seq1024、8GPU、micro16/accum16/seed61，Linear FP8由torchao缩放但master/nonlinear BF16，梯度E5M2/state E4M3；AdamW第103步所测一阶二阶state100%zero是该粗state格式下的underflow，不等所有FP8 AdamW失败。tokens减少53%/30%与摘要1.44×/2.14×次序本身不统一，不采用精确speedup或wall-clock保证；SFT标准误不是多seedCI，FP8 seed61不包装多seed。现有Ch28 sign范数/噪声条件和低比特EMA诊断未解释有界随机sign保留预条件期望的新分支，拟2+1+2=5、实际缺口深入，需独立采用核；不是小模型硬拒，也不据失败推荐普适替代AdamW。
- `15453 SoTo`：v1 §3–5.5/§7及必要D.3/E.4/G实读。coarse-to-fine ordered prefix可早期重建全局语义，partial beam verifier比grid填补prefix更有信息；controlled2D baseline与FlexTok匹配data/architecture/traincompute，主要300COCO图、beam5/candidate10，最佳算法差异不是仅不同模型容量。default3.4B，1D beam更有效而grid BoN/昂贵lookahead更合理；uniform prior搜索180prompt只79%single/32%two-object，不能称无预训练/无prior完美生成。D.3 NFE将token sampling/verifier各计1，函数运行时间不同，简化lookahead长度非恒定；E.4 H100/20COCO图显示beam/lookahead成本移至多步detokenization，GH200256² verifier时延分开，不能把NFE当wall-clock同成本。G实际verifier hacking：自身分数提高但aesthetic/GenEval可降，prior缺失语义也不能靠更多搜索恢复。Ch23已讲nested dropout可截断ordering但未解释search算法的选择条件；Ch24 AR段只讲可逐步预测/误差滚动，尚缺有语义prefix→partial search与detokenizer总成本。拟2+2+3=7深入，唯一owner倾向Ch24，Ch23只交接表示前提；不是泛化所有modalities或免费search，理论AppendixB不拟采用因而不遍历。
- `15415 HarmfulSkillBench`：v1必要benchmark construction/evaluation/results/§8limitations实读。攻击者为主动加载有害能力的user、第三方是victim，不等隐藏payload篡改skill；200自然语言SKILL（81ClawHub/57SkillsRest/62作者构造）、不含脚本，6API模型temp0且reasoning关/仅Gemini minimal，tool-response载skill。A passive plan/B explicit harmful task/D no-skill同task；A→B任务内容改变不是完全matched intent文本，B→D才固定task移除skill。Tier1平均score.79/.34/.08、全体.76/.47/.27，不能把全体当同一harmful任务的因果倍数。judge GPT5.4Mini与被测同名模型，99分层response两作者consensus Spearman.92/refusal91.92%不是全部sample真人确认或无judge偏差。Tier2 HiTL/AID是response建议而不是外部approval执行，评分公式内置safeguard降低harm；C1 .09比C4 .77不证明实际gate部署有效。注册表98440/4858只是作者分类measurement、非全人审groundtruth或本窗新skill数。Ch72现有SkillPoisoning重sideeffect与描述/行为差异，没有主动用户正常加载、公开有害functionality的内容admission盲区；拟2+2+3=7安全深入窄补此threat-model区别，保留planning≠execution、policy taxonomy非普遍法律结论。必要反证足够，不为拟采用规划差异展开全检测器/附件。

以上四项为作者已读必要证据与提案，不冒充独立PASS或整日完成；其它真实贡献消歧与普通Books工作继续。

root已真实读Ch23/28两段与邻接并在V3_ROOT_TCD_NGD_WRITE_AFTER.md通过15383/15554，作者已只同步两条Review notes与日报，未触其它日期。当前4真实整合，不代表日级完成。SOTO/SIGN/SKILL三窄包由root交apr02有限source→owner核，写前未授锁/未写，其余继续。

### 其后五项有限必要审阅

- `15709 Bilevel Skill Optimization`：实际必要§3.1–3.3/Algorithm1及§4.1–4.2读完。θ结构改变φ可行编辑族，先validity/activation-budget5000token（3500warn），content alignment后分五refinement族返回conservative selection；所谓LCB跨候选variant不是默认独立重复实验的安全证书，不采用formal reliability保证。ORQA完整1513/20domains但本次sample总120，search/confirm/test分责、2config各一个skill、test只评一次；runtimeGPT5.2Codex/Harbor、optimizerGPT5.4/DSPy，maxround3vs6等多参数同时变。最终.90625→.9375差.03125，无seed/CI或structure/content分离消融，胜者把reference guidance迁入主文件并加triage。保留结构编辑约束内容搜索的实际局部分支，不将一个task提升归因唯一bilevel或长期泛化，拟2+1+2=5标准Only；不是MCTS成熟或任务局部硬拒。
- `15482 Multi-Objective Unlearning`：v1 §3.1–3.4/§5.1–5.3/§6及唯一必要A.1/Table3实读。QA统一格式+邻界contrastive anchors，context intention teacher、无intention student；teacher/student各自top-K raw logits SmoothL1双项，不把同teacher-guided行为学成不可恢复memory erasure。pilot Llama3.2-3B最后三层cos .04–.08近正交≠负冲突；domain adaptation bound只有分布距离减小才紧，QA改写不自动证明距离变小或梯度统一。HP Table1 utility78.1比base84.3/MMLU59.2比60.8、prefill ASR12.5非0；ablationTable2 Ours MMLU58.2不同主表59.2，双向比DUET ASR同12.5，不能说各目标全胜。cyberA.1 actualASR5.1/SFT44.7不同abstract16或文字SFT强安全通述，邻域88.8比base96.3下降。未披露实际K/训练budget/seed或全evaluationmodel，保留recipe、五轴表与有限对照，不采用strict no-overrefusal/删除保证、各目标synergy定理或唯一归因；拟2+1+2=5标准Only，不因安全名自动全Deep。材料不是biological领域应用，不按AIforScience排除。
- `15484 vstash`：实际§3.6/§4/§5.1–5.5/§6/§7.1–7.6/§8与必要C/E。vector/FTS极权重排名disagreement可构造embedding refinement线索；BGEsmall33M/MNRL76k/2ep/lr3e−6/batch64，训练SciFact/NFCorpus/FiQA中前两者占98%、另外SciDocs/ArguAna才heldout，而均不是全部unseen。Triplet对照lr2e−5/3ep vsMNRL3e−6/2ep，不唯一归因loss。三数据unweightedmean74.5%而aggregate541/753=71.8%分开；positive/hardnegative挑选未给完整算法，disagreement不是relevance truth。adaptive RRF ArguAna+21.4主要来自distance-cutoff5xvs1.15x，不归于IDF权重alone；publishedColBERT不同chunk preprocessing不是matched胜出。内部near-corpus改进及2heldout微增保留，不称zero-cost（只有zero external labels）。post-RRF offtheshelf reranker/usage decay负结果只适用该pipeline；C人工注入popularity模拟有利而BEIR无益，不能普遍deadend。distanceF1跨domain.996而NFCorpus同domain.472，只是offtopic sensor；answer-level30q/高ties不显著；CPU/hardware未披露，不以20.9ms50k作为任意SLO。具体Ch76 query/dialect+retriever训练分布已有分责；拟2+1+2=5标准Only保留pseudo-label线索/排序反证，不把局部SQLite包装升新infra或全部RRF已证明。
- `15488 FineSteer`：v1 §5.1–5.3/Eq6–15/§6.1–6.5/§9必要实读，A.1定点配置已取。IR样本PCA mean-centered subspace/SER能量比gate，prototype Kmeans固定bank + query-dependent WQ/WK attention + PCA residualMLP；虽prototype固定，AGN/MLP要训练，不说全training-free。oneclass低尾gate/supervisedlogistic/Eq15推理softgate直接SER三种说明未合并；SER不是校准harm概率/因果判据。Qwen7B ablation w/oSCS GSM97→34 vsfull95保留；fullTruth54.28低于w/oSCS54.77，但w/oMoSE50.86显示有限取舍，不全指标最优。三family3–9B、TruthfulQA GPT4judge/BLEURT/七攻击DSR，A800 pertoken40.43vsAlpha40.38不是零成本/production tail。BiPO284.7GB为四GPU累加不是一张峰值；主方法113s而Alpha70s训练不叫fastest。A.1训练超参auto/hardware就近记录、counterexam9允许adaptive攻击压小SER绕过gate。现有Ch72输入条件activation redirection只给通用抑制gate与utility风险，未讲when/how分离及multimodal intervention prototypes；拟2+1+3=6实际gap深入，拟唯一Ch72两段，不把该safety题自动所有来源Deep；source→owner独立核还须安排。
- `15490 Think Multilingual, Not Harder`：§3.1–3.2/§4.1–4.2/§5及必要A.15实读。taxonomy corpus约7000，intro17models21language与methods15/18不混成单规模；100annotations85%plausible不是reasoning truth。主实验Qwen3-8B/Phi4Reasoning14B/DeepSeekR1DistillLlama8B，teacherQwen3Next80B，7language/sixSFTtask各1Mtoken预算（Yoruba两task缺），GlobalMMLU500validation/500test；不同语言example数不同不称equalexamplebudget。A.15 LoRAall/3ep/lr1e−6/bf16/effectivebatch16/cosine、length95percentile、不同eval保存频率。translation任务空reasoning也改变CMI/Mindex；Englishmatrix/code-switchaccuracy与correctness为mixedmodelassociation，过密Iindex负相关，不证明language切换唯一下因果或越多越好。Qwen LID/rater同评价、tokenization/翻译质量/强teacher与task支持混杂保留。拟2+1+2=5标准Only保留非reasoning SFT跨任务改变trace语言行为，不推广必须English或新普遍多语教学机制；未复现实验。

15482/15484/15488/15490当前官方abs实际轻核：未给comments，history均v1，无实际withdrawal/correction/erratum字样信号，Submitted值仅version身份不是firstpublic。累计34具名当前事件轻核。未核其他潜在线索不能写全日通过。

### 随后四项：必要源与实际机制边界（非独立 Gate）

恢复后再次实际读AGENTS/三合同/Prompt/ROADMAP及最新checkpoint。三项SoTo/StoSign/HarmfulSkill已由apr02必要source→owner核、真实两段写入和root写后通过，最小同步Review notes及正式日报为7真实I；FineSteer已按同项独立采用PASS窄写Ch72“何时启动/如何改变”两段，写后由root另核，未预支I。Apr22有限交叉审阅另存该日V3_APR20_FIRST_FOUR_ADOPTION.md，不替本日ordinary或日Gate。

- `15505 PolicyBank: Evolving Policy Understanding for LLM Agents`：[exact-v1](https://arxiv.org/html/2604.15505v1)实际读§3–7必要主文。区分policy specification与benchmark required policy：TypeI不遵从书面政策、TypeII遵从了错误/欠完整书面规范；required truth来自τ² annotation，不是独立组织法规authority。21airline/9retail三类sister由原任务最小改写/换instance/复合，紧接parent episode加入；五order seeds不是远期独立heldout部署。PolicyAgent由轨迹和trusted developer binary/可选解释，修订带capabilityID及trigger/precondition/eligibility/action的NL entries，runtime按header检索；不是形式执行规则或agent自授政策修改权。pass^k为所有k次成功的consistency，不是pass@k discovery。Gemini/Claude不同baseline的oracle-trigger vs主动检索不完全matched，retail original ReasonBank.90高于ours.89，不能全指标胜出。§7 scalar feedback sister .31/.10/.02/0，解释feedback .74/.60/.52/.48与human-oracle .90/.89/.88/.87说明信息类型影响，82%是normalized gap closure不是整体成功率。Fig3过度放宽取消资格后再修正是有效失败证据；malicious/noisy feedback仍future work。未披露部署并发/precision/SLO，API实验不冒充线上治理保证。
  
  实际Ch77从原始轨迹到派生策略（496–540）及Failure Trace→Rule（890–927）有advisory、scope、supersession与正例误拒淘汰，但没有显式分离“规范本身误写”与“执行偏离正确规范”的诊断输入。拟2+2+3=7深入，唯一AGENT-MEMORY：经验只能提出带trusted QA来源的policy interpretation修订，批准修改权仍交Workflow/Security；需要窄source→owner核，不因可讲系统故事自动I，也不把annotation称正式授权。

- `15521 Frequency-Aware Flow Matching for High-Quality Image Generation`：[exact-v1](https://arxiv.org/html/2604.15521v1)实际§3.1–3.3/Eq1–13、§4.1–4.3和讨论。noise→image reverse1→0与Xt=(1−t)X+tN分清；Gaussian频域high/low filtering经inverseDFT回spatial components，freq ViT分支统一而非两个独立网络，time-MLP sigmoid融合H/L后加ConvNeXtspatial branch。双域velocity loss与分支/权重同时改变，不证明频率energy是semantic truth或唯一因果；相对谱幅现象也非所有blur定律。ImageNet64pixel/256–512SD-VAE latent，50K FID，134M/507M/1.08B800epochs和不同竞品epoch不是统一compute。Table3 ours1.38vsDiT2.27差.89、vsSiT2.06差.68，与abstract.79/.58不一致不静默修复；L版1.54的.73/.52另分。400epoch B ablation nofreq3.86/low3.55/high3.12/both2.95，addition2.95与crossattention3.95/concat3.46保留。hardware/precision/latency/NFE主文未披露，不采用系统速度或无开销。2+1+2=5标准Only：有限频率conditioning/velocity支线和反证有贡献，但未改变已有可分解生成训练的长期责任，不为图像任务、小改进或负结果前关闭；不声称跨模态质量或独立新loss因果，不为Only展开全附件。

- `15529 LACE: Lattice Attention for Cross-thread Exploration`：[exact-v1](https://arxiv.org/html/2604.15529v1)实际§3.1–3.3/Eq1–7、§4.1–4.3、§5，及唯一必要E.1/F.1。原causal backbone之外加低维QKV、token/thread 3D RoPE和gate融合cross-thread路径，4threads、插中后every-other layers，参数<1%；不等外部Agent消息workflow。Eq4 flatten NL SDPA没有明确给出lateral时间mask；本文称保原causal主线，但不能据此声称全分支已证明无future泄漏，F.1只有train配置未补mask。实际可采用横向exchange分支与mask义务，不能补造实际实现。CPT→SFT→thread-group RL共享advantage，准确性/选择格式加cosine-diversity；相关threads不是独立sample，cosine不同不是推理逻辑因果不同。训练数据base pass(0,.5]过滤、235B cached successful/failed路径+<3k压缩/评判有额外代价。主模型LACE独有CPT，sameRL step baseline不等全训练预算；best@4选择含format失败与baseline pass@1不同estimand，保voting对照，1.7B Live16.5vs16仅.5提升。gate weight高不证明一条语义为有效因果来源。
  
  E.1 actual RTX PRO6000 Blackwell97GB/bf16/context50/gen100：FLOPs<1.3%不是速度成本，N4的1.7B ms/step20.5→28.4(+38.5%)、4B27.6→36.2(+31.2%)，TPS195.4→140.8、144.8→110.6反向；N128 4B step+96.4%/memory+14.9%。这是短微基准非生产concurrency/p99，不能沿negligibleFLOPs说negligible latency。拟2+2+3=7必要深入已读；实际Ch14单序列content routing及mask/数值边界没有多个推理thread显式横向交换，若采用需最窄owner比较和独立核，不自动I；保未公开lateral mask及共用训练成本边界。无需为这一命题遍历全部Analytical/Agent附件。

- `15557 Predicting Where Steering Vectors Succeed`：[exact-v1](https://arxiv.org/html/2604.15557v1)实际§3–5必要主文、D/F/H/J定点controls。A_lin只测finalnorm+unembedding的logit lens next-token单token正确，不是所有线性可读性。Δ为80/20训练residual MLP与frozenhead的差，只能说该probe能校正该投影，不能从A_lin低诊断concept“不线性”或任何方法不可干预。J的trainedlinearprobe每层>93%但early ΔP近0恰好反证“内部线性存在→steering可行”；原probe方向/steeringtarget不同不得宣称absence。五heterogeneous families831/564/433/506/348跨family相关ρ.18p.54，25binary22prompt each受控但局部；H pooled n130是layer×family而非独立样本，permutation不保withinfamilyautocorrelation，partialdepth也不自动修复它。geo partial .372p.067不全显著，floor以上较弱与大模型.84/.93分开。F target word thin4/analogy dark3很小，J省略n<10两trained选层，best-layer/oracle非heldout生产controller；F/D不清独立steering选择heldout，不补造无重用。实体20+20prompt demonstration不作普遍成功/真实安全率，finalnorm tuned/raw artifact保留。
  
  2+1+3=6标准Only：保留output-alignment作为有限层选择diagnostic及失败案例，不采用“概念本质三阶段/所有方法无力”的内部定律、全layer选择百分比或泛化性能。3090Ti24GB数小时实验是作者成本，非在线p99。标准必要证据与关键controls足够，不因refusal演示泛化所有安全项Deep、不展开所有附录。

15505/15521/15557官方当前abs轻核只有v1；15529 history另有May7 v2/May11 v3但未提供本次必要纠错/撤回信号，不做全版diff。四项Submitted仅版本身份，首公开仍由本日窄公告批链证明而非孤证。累计38具名当前事件轻核，尚非全日PASS；四项处置与拟采用还须相应非作者核，其余本日ordinary继续。

### 随后四项必要证明、行为对照与目标边界

恢复时再次实际读AGENTS/当前三合同/Prompt/ROADMAP、最新月与LS入口。15505/15529已按root独立必要源→owner PASS实际窄写Ch77:541–544与Ch14:116–119，并释放锁；写后另核，不预支I。

- `15558 Preregistered Belief Revision Contracts`：[v1](https://arxiv.org/html/2604.15558v1)实际读§3.1–3.4/§4.1–4.5、§6.1–6.3定义7–10/Lemma1–2/Theorem1–2必要假设证明、§13.9与§14限制；不是全部25个theorem/实现附件。contract预注册trigger/operator/priority/fallback，只有非空validated tokens及相应witness才允许evidential operator。skeptical fallback δ=(1−λ)b+λuniform、0<λ<1，在有限概率向量上保argmax集合并不增加max-coordinate confidence；没有新token时social-only更新不能制造更尖锐的protocol belief，但不会修正已有错误信念。§4.4 architecture A只验witness不足以强迫agent应用U；B是可选proof-carrying路径；C由state-holding router实际计算并拥有权威protocol-state。这个外部向量不自动等LLM内部belief，认证token也不证明语义支持/真值。§13.9 GPT4o/T.7/n3000 paired benchmark Raw.724/Social.678/Reflection.698/PBRC.724是reject掉flip的外部router效果，411有害/273有益/154neutral flip均被拦，不证明改善独立truth reasoning或不损纠错/liveness。§14明确forgery/omission/query steering/dynamic hypotheses/enforcement依赖；无生产SLO。不采用全拓扑factorization、所有MAS安全或内部信心保证。实际Ch82:570附近已有consensus≠truth及独立evidence，但未解释witness gate≠operator compliance和外部protocol belief-state保守更新；拟2+2+3=7深入，唯一AGENT-MULTI-AGENT最窄两段提案，待非作者采用，不强行全附件复现。

- `15559 Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation`：[v1](https://arxiv.org/html/2604.15559v1)实际§3.1–3.5/§4.1–4.3/limitations和必要AppendixA。teacher150删除任务/2epochs，400 safe trajectories只用search/list/read并keyword filter排15%到340，student4epochs；Llama3.2-3B/Llama3.1-8B/Qwen2.5-7B，LoRAqkvo/r16/alpha32/drop.05/bf16，teacher/student lr8e−4/5e−4。20 ambiguous tasks/3seeds下“first substantive action” deletion是作者binary行为选择，不是外部执行receipt或校准概率；valid-but-not-required的delete baseline≈0是该任务policy，不证明所有delete都越权。API table8→8 student100/base5、3→3 35/0、8→3 100/5、3→8 10/0、8→Qwen100/20；random-teacher control25/base5反而+20，不能说control=baseline，亦不能据少量模型证明capacity唯一机制。Bash chmod-first不等任何chmod有害，8→8 30/5、3→3 15/10、8→3 55/10、3→8 5/5、Qwen45/0、control5/5分开，两个环境/不同baseline口径不合并。无实际p/CI，结构因果机制作者承认未解，不采纯结构/全部偏好继承/任意规模保证。拟2+2+2=6、因真正filter→posttraining保护边界深入必要内容；已有覆盖仅限实际Ch72:1564“任务无关输出不等无信息training artifact，词审计外还须下游蒸馏行为transfer测试”的具体命题，不声称全部Agent删除/permission benchmark已有。新受限数字保Only证据范围，非live exploit、安全证书或全附件审阅。

- `15574 Why Fine-Tuning Encourages Hallucinations and How to Fix It`：[v1](https://arxiv.org/html/2604.15574v1)实际§2.1–2.2/§3.1–3.2/§4.1/Eq1–2/§5.1–5.2/Eq3–4与discussion。SLiCK20多次sample划HighlyKnown/Unknown，只能说该protocol从未表达，不是内部无知识；按relations≥30%Known过滤、Known8k+Unknown8k及同relations heldout Known使范围固定。Qwen2.5-1.5B代表结果：attention-only Unknown.010/Known.946/Held.931，对FFN.941/.997/.782与all.946/.990/.780、Known-only.999/.958；冻结事实可塑性在无需新事实目标下合理，不证明所有Attention不存事实。1epoch Known-only teacher+τ.5/λ1 tokenKL约束需额外teacher forward，3%vs15%是relative peak-held accuracy损伤，不是所有hallucination事故率。lr5e−5选择使用Unknown学习/inducedhallucination标准，非无关heldout选择。§5.1同P17关系、真实名称重组vsUUID synthetic facts(10³–10⁶)的词形/tokenization/pretraining associations也变，不证明唯一semantic geometry因果或完全排除capacity；UUID回退0–4%非全0。§5.2 L2对2epoch target、gradient scale matched但信息/约束不同，layer14/28 representation cosine~11%vs5%是相关诊断，不证明知识被删除或唯一路径。未读所有模型/所有附件，主文硬件/precision/seed/productionSLO ND。拟2+1+3=6，实际Ch29:602–628有通用fact覆盖、trainable subspace及referenceKL replay，却缺明确“只学习表达既知事实”与“确要获取新事实”的目标分叉、Known-only格式teacher与新事实/旧retain联合验收；这一具体缺口定点深入，可提两段，不泛化模块因果或保证从不遗忘。

- `15577 Reward Weighted Classifier-Free Guidance as Policy Improvement in Autoregressive Models`：[v1](https://arxiv.org/html/2604.15577v1)实际§3理论/Eq、§4近似与§5必要协议/§6limitations。精确Q=E[r(y)|prefix+token]的Q^γ倾斜需nonnegative reward/可定义log与normalization；Jensen weighted-log界另需有效非负归一权重。实践用有限YS、prior而非prefix posterior、z-scored可负A与nucleus.95 clipping，不自动继承精确Q/Jensen policy-improvement保证。γ1/2/4/8取2、guidedteacher50step全vocabKL warmstart、RL后conditional stale/反复蒸馏不稳定保留。main仅分子bench；保一般AR conditional likelihood-ratio采样机制，不采用化学领域目标/结果排名，避免AIforScience经Sampling恢复。RLgrid16×1000再2000best与小γ搜索不同预算，8H100训练不是每request成本/线上SLO，out-of-support四项与其他reverse不合成普遍优越。拟2+1+2=5标准Only：bounded approximate guidance分支有贡献，但不足以采理论改善保证或替代policy optimization；不因小模型/单域直接删除通用形式机制，不为当前Only遍历分子附件。

四项当前官方abs实际轻核：15559/15577仅v1，15558/15574另有v2但未给comments/实际withdrawal或erratum说明；版本变化不等重要事件、也非全版本无变化证明。累计42具名event轻核，首公开仍由本日窄批次链而非submitted字段；上述为作者必要证据/处置提案，非独立日Gate。

### 下四项：可执行规则、选择器、长编辑循环与组梯度

- `15579 Symbolic Guardrails for Domain-Specific Agents: Stronger Safety and Security Guarantees Without Sacrificing Utility`：[v1](https://arxiv.org/html/2604.15579v1)实际§3.1–3.2/§4.1–4.3/§5.1–5.2。80benchmark是2022–Mar1 2026受关键词/分类及robot/embodied/reinforcement排除影响的样本，413→301→80、100人核模型κ.88；不是全Agent领域无具体policy证明。Table2 49/80无policy=61.3%，19/80goal=23.8%，合68/80=85%；正文63%与表不一不采该单数字。symbolic可实现判断非全部formal proof：两原政策加LLM生成医用synthetic88要求（无expert），outofscope后42/51+17/18+34/57=93/126约74%，文字75%不作为精确统一值。six checks含API/schema/temporal/infoflow/userconfirmation/template；procedure或explicitrequest语义可能需强化/弱化改写，改写不是原命题自然等价。
  main三benchmark GPT4o/GPT5/MCP+LLMuser，50/100/300及50/391合成攻击；医用34中只实写23（1已有、10需未得专家知识），不能宣称34全实现。6/16与6/8工具签名增参，baseline safety依模型replay同call补参数，五次不一致为Unknown、无法补为unsafe，非完全matchedschema。0违反由同guardpredicate阻断/测量，**只涵盖实际instrumented要求**；CAR rp .97不是全部policy无误，UnsafeUnknown分开。utility .36→.48 p.18/.68→.70 p1.00与CAR.59→.72/医.59→.67并存，p0.00仅source显示rounding非数学零，nonsignificance不证明无损。主文无latency/precision/SLO，三个域不是生产完备保障。2+2+2=6，保护保证变化定点深入，拟已有覆盖唯一Ch72 `Policy-as-Data`458–477的model verdict为sensor、确定性executor为authority，及601 effect/utility联合验收，不声称每个symbolic配方全覆盖；具体统计及labeling限制仅报告证据，医疗仅治理机制案例非诊疗建议/AIforScience恢复。

- `15583 SAGE: Selective Attention-Guided Extraction for Token-Efficient Document Indexing`：[v1](https://arxiv.org/html/2604.15583v1)实际§3.1–3.3/Eq1–6/§4.1–4.8/Conclusion。每chunk+query前向，不是整文只一个prefill；query/head/layer聚合，按chunk长度Ti/Tdefault及querylength归一，再差分raw/fixed“repeatcontext”/farthest MiniLMquery。不证明query不同长时attentionmass天然相同或semantic truth；source exact-cache论述还须固定prefix/template/position/model，不当已验证任意同hash都exact。wordtoken哈希每document KV复用、新document清空是实际方案，非跨tenant证书。2%unitwindows smoothing/greedy/overlapmerge保原次序与预算，contrast可能删共享必要事实，repetitive ZIP更大budget反降证明非单调。
  Llama1B/Qwen8B/14B attention与Gemini2.5FlashLite generator/T0、GPT4omini judge（约200/dataset人看规则，不是全面真人truth）、Qwen.6Bcosine分开。QuALITY3797 query690.9s/3011cachehits 对RAG8798chunkembedding98.2/370.7/838.6s不等完整end-to-end/同查询与缓存成本；hardware/precision主文ND，不说免费/普遍更快。QuALITY预算不精确matched、5% accuracy .36/.46/.48跨模型，Notice budget可matched。Paper差分CDF胜raw是有限证据，当前leaderboard名次不当Apr20固定事实；rowadaptedAIT.87/51%rows对full.88不等严格等价。2+1+2=5标准Only：bounded normalized-contrast/window extraction分支有贡献，但没有改变已有Ch75:235–263对压缩保真、总成本break-even与query-specific evidence的长期职责；不是称全文被Existing，也非局部RAG硬拒。只保机制与失败/测量边界，不采guaranteed evidence preservation/onlineSLO。

- `15597 LLMs Corrupt Your Documents When You Delegate`：[v1](https://arxiv.org/html/2604.15597v1)实际§2–5/§8及必要A.1/A.2、B.2/B.3、M.1/M.2；不是全部领域附件。52域×6环境，real permissive2–5k seed+8–12kdistractors、5–10可逆edit、10roundtrip20interaction/扩50roundtrip100；每步fresh单turn无会话history，不把document carryover称conversation累计。定制parser/weightedsemantic sim是roundtrip RS，不是真实逐token丢失率；threshold98与critical≥10pt是作者定义。前/后σ复合误差只能每两步测，可能no-op/部分执行/抵消，B明确高RS不保证forward质量、低RS不分错误步。A GPT5.4 judge12409分层step，93.8% fully或partially **attempted**不等正确完成，16.7%partial；error-faithfulness是近似injective+不抵消假设而非普遍定理。
  19models Table1 GPT5.4 RS94.3→71.5/Opus94.2→73.1/Gemini96.8→80.9，~25%是三model有限semantic-score损伤非生产内容比例；critical约80%损伤是threshold分账不是唯一failurecause。basicagent四GPT、five tools/read/write/delete/python/finish，bwrap/networkoff/30s/25turn/500ktokens/writebeforefinish，不是先进所有agent；GPT5.4工具RS68.3vs71.5，input×2.1但latency×.4反而快，不采全tools更慢/不能帮助结论。larger/longer/distractor条件损伤保留但表中局部反向存在，source“monotonic”不作为严格全序保证；不将散布科学文件变成科学应用研究。现Ch66:516–525 cyclehandoff/verifier未区分“可逆重建分数”与“forward编辑任务正确性”、无可逆task'serrorfaithfulness边界；拟2+2+3=7深入、唯一PLATFORM-EVALUATION-SYSTEM窄两段，待独立source→owner，不称拒绝正常所有委托/单步工具失败。必要method/counter足够不all附件。

- `15602 GroupDPO: Memory efficient Group-wise Direct Preference Optimization`：[v1](https://arxiv.org/html/2604.15602v1)实际§3–5.3/Limitations、必要A.3/Table6–7。unorderedpositive/negative sets，u=βlogπ/ref，no-grad同θ全scores→c_i=(1/G)∂φ_g/∂u_i，再stopgrad系数的Σc_i u_i，chainrule同参数点一阶gradient exact，不保Hessian/二阶optimizer；需绑定同response/tokenreduction/reference/参数点与forward随机性，stale或dropout不一致不能自然exact（后者是工程推论不是作者复现）。ordinaryactivation grows随responses，不沿intro“exponential”做理论上界。AllPairs balanced PN~G² interactions还在，vanilla O(GC(T)+G²)、flatten O(G²C(T))、surrogate多no-grad但O(GC(T)+G²)；不是所有group calculationO(1)。
  efficiency一H10080SXM/gradientcheckpoint：base含warmup initialized params+optimizer，overhead=maxforward/backwardallocated−base排optimizer.step临时峰值，step latency则含optimizer；3warm memory、2warm+5latency，不称totalGPUpeak constant/线上SLO。mainplots多sequence/batch但precision/repeatCI未披露，不捏造精确micro数字。A.3 offline8/8/32GPUs/1epoch1139steps与online8train16rollout异步100steps、prompt2048/resp8192or4096，NLL0/1与βsweep绑定。最高validationmath vslast再取better、online最高checkpoint，selection会影响泛化；offline group top/bottom reward分组后丢scores，与randompair/bestworst更强baseline各自不同监督支持/compute。gemma General avgDPO37.8≥groups36.6/36.9/36.0/37.8与codingreverse反证“全任务总胜”；NLL可稳定源条件不普遍避免collapse，group>8收益趋平。拟2+2+3=7深入，实际Ch34:128response logprob与工程流316尚缺coupled-objective coefficient→sample backward的梯度/执行分离；唯一TRAIN-DPO窄正文提案，不改TRAIN-GRPO reward定义。不为有限first-order/执行采用展开全部表/代码复现。

四项当前官方事件页实际轻核：15579 v2 Jul5、15583 v2 Apr24、15602 v2 Sep1，15597只有v1，均未提供comments/withdrawal/erratum等具体说明；不把版本变化作重要修订信号，也不证明未来无变化。原Submitted身份不能单独确定firstpublic。累计46具名当前event轻核，15597/15602实际提案在V3_DELEGATE_GROUPDPO_OWNER_PROPOSALS.md，独立核/真实写入未完；不把任何小批当日Gate。

### 接续四项：黑盒局部梯度、功能共识、端侧选择与匿名凭据

恢复实际重读AGENTS/当前三合同/Prompt/ROADMAP与最新checkpoint，以及Books指南/实际相邻。15558/15574 literal两段分别落Ch82共识后、Ch29 forgetting后，root真实正文及相邻写后通过，已同步notes/正式日报为12真实I；15559窄Existing/15577 StdOnly经apr02具名必要核通过，不是日Gate。普通工作持续，不改LS/月checkpoint。

- `15609 Adapting in the Dark: Efficient and Stable Test-Time Adaptation for Black-Box Models`：[official v1](https://arxiv.org/html/2604.15609v1)实际§3.1–3.4/4.1–4.2、必要B.11及E。接口提供完整probabilityvector，非label-only/topk；本地22M ViTSmall控制输入δ，remote参数不变，混合pH=.4pS+.6pB对pB stopgrad只是可访问branch的梯度proxy，不能说原pB(δ)真梯度为零/严格整个目标等价。低entropy可靠样本学prompt，norm还去重复，clean→prompted localKL避免degenerate解；Exp2 collapse51.6<55.5，KL-only59.7/filter-only60.2/full62.6保留，不能由叠加数字断言两者各自普遍必要。ETA65.8/67.2高于BETA62.6/65.1，白盒baseline访问不同，不采所有白盒胜出。FOA改掉source-statistics、DDA released模型涉及source data，对照访问条件保留。
  API一call/sample非免费，本地RTX3090/Small2616MB、45→48ms；B.11 Tstep=max(API,localFWD)+localBWD3ms在作者API45ms条件可重叠，不等p99/任意API网络，batch/precision/SLO未披露。Clarifai.0032/call与120sample.4USD/250×只该protocol，不恢复医学应用。E承认错类overconfidence可锁错误、label嵌入与本地容量限制；其“uniform pS ⇒ JS=0”并非任意pB恒等式，不采用这句。检测/分割/生成与LLMadvisor迁移仅future analogy非证据。2+1+2=5标准Only：受限blackbox输入适配proxy与稳定条件可保，未证明生成/共享请求更新安全，也未替代Ch29临时参数delta/rollback责任；不因vision/小模型硬拒，不扩大医学方向。

- `15618 Majority Voting for Code Generation`：[v1](https://arxiv.org/html/2604.15618v1)实际§3–5及AppendixA。候选运行全部testinputs失败则discard，功能签名上的medoid以跨candidate、跨test一致数计分，不要求完全同签名；pointwise mode可能无单个程序实现，作为reward非正确性证书。LCBv6使用真实oracle testinputs而非输出标签，生成testinputs可靠是推断非实验，不能称任意无测试label-free。Qwen3Instruct4/30A3B及Thinking，64sample；半train/holdout，bootstrapSE不等多seed显著性。4B holdout mean@64 31.6±3.1→34.3±3.2，保任务准确平均与bestselection区别。Table2 basebest64=48.9±1.0，JointN12845.0±4.2/pointwise46.6±4.2，FMV41.2→40.5/38.9虽mean30.8→36.9/36.8升，未越baseceiling。训练N32/128、T1/lr1e−6/b8/noKL至validation饱和；推理T.6/topP.95/Instruct8192/Thinking16384，不能混同预算。CPU N×K执行非免费，硬件/精度/end-to-endSLO未披露。2+1+2=5标准Only：execution-consensus selector与受限自训练负面边界是贡献，不采一致即正确/无条件自改进，不以负面结果删候选，暂无必要长期Books改变。

- `15622 AdaVFM: Adaptive Vision Foundation Models for Edge Intelligence via LLM-Guided Execution`：[v1](https://arxiv.org/html/2604.15622v1)实际§3–6.4，必要AppendixA/D.3/E。高频vision、低频云端semantic class filtering/textembedding+subnet选择分责；评估先为每image生成max3word scene模拟，不等真实稀疏stream/controller时间实测。DINOv2→ConvNeXt NAS共享5subnets、stage1 LVD142M625k/b4096/stage2 MetaCLIP100k/b4096，sandwichlargest/smallest+2random，非无训LLM推理优化。α为当前已有scene lookup上maxsubnet准确率的比例，最近scene匹配非未见场景安全下界/运行时真值反馈。类别可删真类，D.3 GPT5 recall89.7/precision6.1、Gemini94.7/3.2、Top25 77.1/8.0，不能仅mIoU↑证明filter可靠。coarseWordNet目标改变任务，不当同fineclasses准确无损。
  test EthosU55 7nm/560MHz/>128GOP/s/Vela，均值含wrapper/subnetswitch，Min23ms/1.1mJ→Large182ms/8.4mJ；precision/完整云LLM网络功耗与trigger频率未披露，所称end-to-end均值不证明整端云耗能/电池寿命5×或线上SLO。5representative非全NAS空间，standalone/control与非LLM性能反向保留；Table7b文字数字和a列复用位置不统一，不自行矫正出新数字。2+2+2=6标准Only：semantic支持改变相对质量/成本的受限调度分支，当前lookup未建立受保护动态保证，不采“最优子网/未见场景near-lossless”。当前v3标题AdaDINO/learnedselector37%是Aug1修订的新branch信号，非本窗v1/已读v1lookup实现，不扩全版史也不复制其数字回April。

- `15637 Too Private to Tell: Practical Token Theft Attacks on Apple Intelligence`：[v1](https://arxiv.org/html/2604.15637v1)实际§3认证路径、§4.1/威胁模型、§5.1/5.2必要边界、§6/Ethics。仅防御研究，不运行攻击/保存凭据。macOS26.0(25A353)/M4Macmini作者自有设备：匿名TGT首次硬件资格、OTT一次使用与签名验证分别成立，但可转移TGT仍可redeem后续OTT并把quota记受害资产，OTT一次性不封住rootcredential。正常用户应用需受害者授权keychain访问（不是silent普通代码可无条件读），login keychain磁盘加密而授权API可plaintextretrieve，不能称全数据库plaintext。TGT数days、OTT约12h为实测条件非普遍expiry/SLA，signingkey批过期+无userrevoke放大暴露期；signature可验证不等请求仍来自原资格硬件。
  §6.1 macOS26.2迁iCloudkeychain/Appleaccessgroup为作者分析的storagemitigation，不证明协议non-transferable/所有新版本仍可攻；同作者[Apple26.2公告](https://support.apple.com/en-ae/125886) Networking/CVE-2025-43509确认改进data protection，ReleasedDec12 2025不是Apr20新fix或论文首公开证明。vendor仅确认宽影响/修复不确认作者所有机制/残余攻击；root短生命/隔离storage代价+不完善条件保留，不沿自相矛盾“完整协议防御”宣传补造实现。2+2+3=7保护深入，实际Ch72认证层与多跳issuer signature尚缺匿名性≠不可转移性/一次子token≠rootcredential隔离的实际分叉，待source→owner独立核/窄写，不采可直接复现或当前系统漏洞普遍声明。

四项当前official abs实际轻核：15609/15618只有v1，comments为TTU workshop，无具体纠错/撤回；15637只有v1无comments；15622v2May3/v3Aug1无comments但当前title/abstract变为learned selector为真实新branch，归属窗外保留线索，不沿用v1操作协议。累计50具名event轻核，不等全日Gate，Submitted均只识别版本。

### 接续五项：直流存在性、数据种子、图反馈、跳转分解与attention蒸馏

恢复再次实际重读AGENTS、当前三合同/Prompt/ROADMAP及月checkpoint最新21:00段，确认本lane20→26→29，23由root独占。本日14真实I的正式V3及scoped diffcheck通过，不等日Gate；15637两段已按root有限采用PASS写Ch72:96–98/Review2766，写后未核前不计I15。以下必要证据均来自official-v1；不展开全部引用/附件。

- `15439 One-Shot Generative Flows: Existence and Obstructions`：[v1](https://arxiv.org/html/2604.15439v1)实际§1.4定义1–4、§2/P1–C4/T5、§3.1 T6/P8/T9与§3.2 P10反例、§4.1定义5/T11完整证明/C12/T13、§4.2定义6–11/L14/T17必要定理条件、§5。独立端点随机过程的sample-path straight不等conditional velocity ODE straight；在正则/二阶矩条件下，普通affine path只有deterministic coupling可满足straight flow，正半定Jacobian是所给充分条件，不能简化成任意transport map。额外独立Gaussian Z乘sqrt(2t(1-t))在非退化Gaussian端点可令conditional-flow直线；任意两协方差用matrix-pencil配Z，不沿主文抽取丢sqrt后的式子。该存在构造非任意真实data Gaussian化/神经网络训练误差为零。
  障碍限定在paper独立端点、连续sample path与uniform-in-time Lipschitz conditional velocity：相同两段分离uniform混合是具体不可能例子；定义5更强closed convex hull分离，不是所有一般多峰/同分布都不可能。T17只d=1、positive AC Frostman source、proper epsilon-separated target、固定C(A,alpha,beta)模连续尾界，epsilon0依所有这些量；不是跨任意维/任意正则类统一epsilon阈值。P10 collapse/reexpand在τ处Lipschitz发散，不满足定义，不能拿几乎处处PDE绕过。理论结果不要求GPU benchmark，但并无生成质量/learned oneNFE实测保证。2+2+3=7深入，当前Ch24:272 learned approximate flow-map组合及291–300少步近似缺独立coupling/结构可行性区别，拟窄两段，待source→actual owner核；T17等仅有限条件报告，不将全文headline所有范围写书。

- `15675 C-Mining: Unsupervised Discovery of Seeds for Cultural Data Synthesis via Geometric Misalignment`：[v1](https://arxiv.org/html/2604.15675v1)实际§3.1–3.4、§4.1–4.5及必要Table1/3/4/6。NER负过滤title+leadparagraph，frozen multilingual encoder→Kmeans→5NN低于median density及semantic entropy→crosslingualcluster≥5/单语言占比>.8，cluster中心seed喂Qwen3-235B合成50k再LoRA7B/32B；语言聚簇不自然证明文化truth/因果。Eq2 cosine行归一未交代negative/zero处理，不能把所有similarity当合法概率分布/熵保证。geometry评价部分复用selector空间有选择循环，双盲专家0–4外部证据但样本/不确定性披露不足，不称全文化无偏。
  Table3 random/mono/full有真实消融，random在CB44.62→43.31/BLEnD82.63→81.13反向；>.8与1.0过过滤支持局部precision/diversity取舍，不是统一最优阈值。Table1 BLEnD77.12→80.94实际差3.82，与文字3.13冲突保表不抄headline；CultureBank CB40.13vs40.78小差无重复CI不说显著。GlobalMMLU+.28/+.34单proxy不能保证无catastrophic forgetting。Table6 1M/500Mtoken的GPT4o价格/spot GPU与manual估算11.2/1750不是整个synthesis+training端到端150×，hardware/precision/in-outlength/onlineSLO未披露。2+1+2=5标准Only：无人工seed选择有贡献，bounded ranking与selector测量不足以把geometric exclusivity升级data truth/通用质量保证，暂无必要Books改变，不因文化领域/单局部提升硬拒通用机制。

- `15676 EvoRAG: Making Knowledge Graph-based RAG Automatically Evolve through Feedback-driven Backpropagation`：[v1](https://arxiv.org/html/2604.15676v1)实际§3、§4.1–4.3.4/Eq2–9、§5.1–5.2、§6.1–6.8；官方HTML公式再开避免markup分式丢括号。response反馈(默认judge能看groundtruth)→supportiveness/Fidelity/Conflict路径sensor→triplet跨query贡献→relation fusion/suppression与fresh query similarity；fidelity/conflict来自同LLM不是独立事实authority，shortcut标签由LLM推荐非原关系真值。score初100再normalized，mu±sigma不是显著性检验；关系改写仍可能改变fact，不沿作者entity修改才需factcheck作保证。
  **中央exact-gradient/保证争议**：Eq3是normalized geometric mean，即softmax(mean log P(t))；对Eq4的log expected affine utility求导应为`-alpha/(2E) sum(V_i/P(t))`（路径内triplet唯一时），Eq5额外`prod_g P(g)`不从Eq3推出。实际两条单triplet路径p1=.2/p2=.8、alpha=.5、U1=1/U2=0、Sr1=Sc1=.2，可使其余固定；E=.6、V1=.16，按Eq3/4导数−1/3，Eq5为−1/15，有限差分h1e-6为−.333333333324，非−.066666666667。不执行artifact，这只是公式counterexample。§4.3.3 E可趋0/所有U=-1时0，非uniform upperbounded logloss，亦不保证防梯度爆炸；相同utility所有path时多optima，convex≠strictconvex，softmax后Sc空间未证convex/convergence。只隔离准确反传、唯一/稳定收敛与必然noise-tolerance，不否定完整架构/局部实验。
  原实验保2A6000/503GB、Qwen2.5-32B统一generator/judge、RGB300/MTH816/HPQ600；train query从test热点subgraph生成，different path不等无transductive信息支持，unseen区域不能外推。83.01%problematic triplet是作者定义/人工标注；feedback10/20%随机flip掉neutral后1.15/2.43下降，不是对抗/相关噪声保证。FB6.6/Evolve3.07/CV2.24是其消融平均，backprop23.90% batch20/KVreuse不等全在线SLO，4.6×prompt比chunk型baseline不同支持。precision/requestlength/CI主文ND。2+1+3=6 correction-trigger深入，拟中央争议暂缓，保协议/表不新Books；重开需Eq3/5一致修订、utility正下界/归一合法性及正确的convergence假设或收窄宣称。Ch76:698–713路径可追踪/utility不掌fact已有责任链不能据此判全架构Existing，争议定点交非作者。

- `15694 Neural Continuous-Time Markov Chain: Discrete Diffusion via Decoupled Jump Timing and Direction`：[v1](https://arxiv.org/html/2604.15694v1)实际§2必要CTMC定义、§4.1 L4.1/T4.2/4.3/C4.4/P4.5/4.6/T4.7/P4.8/C4.9/10、§4.2算法、§5、AppendixD必要config与Algorithm2–3。reverse rate分exitλ和destination r，pathKL分Poisson timing加true exit-rate加权Cat direction；并非固定schedule+mask预测头永远够用。conditional surrogate同一一阶gradient需要forward量θ-independent、positive differentiable offdiagonal Rθ及微分积分可交换，constant gap不证明finiteSGD稳定/全局解。mask absorbing特例λ由schedule固定，才还原MDLM；uniform可反复跳，不等只一次unmask。Eulerλτ≤1合法性必须保，τ-leapingk个jump在当前t冻结λ但每新state重新评r；一步可能多次networkcalls，Nstep不等NFE/墙钟成本。
  163M/12layer768/12heads、GPT2BPE50257(roundembed50304)、length512、TinyStories matchedarch/budget、OWT released262B vsSEDD682B不同pipeline，1024unconditional样本Gemma2 genPPL不是dataNLL/ELBO或正确性。作者因finite samples写≤并不数学证明置信upperbound，保数值为有限sample估计，不沿≤保证。128stepSEDD127.2比Euler183.6更好；OWTmainτ-leaping列与AppendD称仅Euler不统一，不替作者补协议。hardware/precision/batch/latency/CI未披露，实测好排序不采机制唯一因果。2+2+3=7深入，真实Ch24:674 artifact jointidentity及848 Euler接口尚缺timing/direction分解与schedule特例，拟窄两段，不采用PPL数学upperbound/headlinefirst普遍优越。

- `15701 Improving Reasoning Capabilities in Small Models through Mixture-of-Layers Distillation with Stepwise Attention on Key Information`：[v1](https://arxiv.org/html/2604.15701v1)实际§3.1–3.3/Eq2–7、§4.1/4.2/4.5/4.6/Limitations及必要C.1/C.2/F.5。correctteacher答案筛CoT再逐句(period)step，数学critical为数字、CSQA为teacherprovidedkeywords，regex/tokenizer映射同word的多个tokens汇总；相同teachertext及key集合保证对应shape，非任意teacherstudent自由CoT/不同关键词仍对齐。teacher层权重是critical-word列相邻差softmax，不是lossgradient、注意力≠唯一reasoning causal state；student全层value→RMSNorm→sum/router再同shape attentionKL，非无teacherfeatures。
  8B→GPT2Large774M/32B→TinyLlama1.1B五短reasoning集，两ID三OOD，teacherSL若只最高层不一定最佳；9pairs+lastlayerTable2 MoL37.5vsSLmax35.8限定这俩模型，matchedallpair参数/调参compute未等。HybridPaLMrationale+Llamaattention平均39.3<unified40.5，并非更大teacher必优，机制effect与各任务support不混。F.2明确single NVIDIA A800、batch16及三次随机运行均值，CI仍ND，不称显著；F.3第二阶段使用ground-truth answer修正原teacher答错样本，前述correct-teacher筛选仅第一阶段，不能外推全程。F.5 FLOPs tiny router增量只studentforward中间矩阵计账，未计teacherattention生成/storage、fusedattentionmaterialization/memory，precision/完整sequence/SLO未披露，不采零端到端额外成本。2+1+2=5标准Only：异tokenizer跨层supervision接口有局部贡献，未建立universalteacheragnostic/layercausal知识保证，不因小模型/短CoT关闭，但暂无必要Books改变。apr02实际必要源有限核通过并提出上述F.2/F.3修正，见[V3_APR02_THREE_METHOD_DISPOSITIONS](./V3_APR02_THREE_METHOD_DISPOSITIONS.md)；同文件15675标准Only与15676中央窄D通过，非日期/日Gate。

本批officialabs实际轻核15675/15676/15701仅v1、15694v2May8、15439v2Apr20 15Z/v3May7，页面未提供comments或决定处置的withdrawal/erratum说明。15439在此前22项已核，本次增加四个唯一身份，累计54，不误记55；v2事件窗外不自动Important，不对所有版本diff。单篇待有限独立核，日ordinary继续，非冻结/非日Gate。

## 接续：多模态反事实训练与内部特征数据选择

- `15705 Towards Robust Endogenous Reasoning: Unifying Drift Adaptation in Non-Stationary Tuning`：[official v1](https://arxiv.org/html/2604.15705v1)，实际III-B–E/Eq1–9、IV-A–F/TablesI–VIII/Fig7。思维词替换能改变visual attention的局部失效、层级概念图约束文字负例、属性近邻图像加同模型逆匹配筛hard negatives、DPO双模态支持是可检查分支；同模型生图谱/判匹配不授causal truth。把生成位置分布变化定义为concept drift，不证明全是有害混杂；SCM画图与do(D=d)没有观测/实际固定latentD识别证据，保协议而不采已消除所有spurious correlation。Eq9固定v的text preference与换v hardnegative如何联合计logratio未完全分账，不补严格同一counterfactual objective。
  Qwen2.5VL7B、1epoch/batch4/2×2A100/AdamW2e−5/warm40；医学报告与驾驶NLP/GPTScore是任务指标，不等逻辑真值/可执行驾驶动作安全。TableII BLEU2 .286低于CPO.288、TableIII easyCIDEr1.208低于HoP1.210、TableIVCon77.0低于77.7/Pnx95.4低于95.8，保局部反向。Fig7文字+视觉消融支持有限recipe，不证明严格orthogonal/理论上界/两个模块普遍不可缺。无多seedCI、完整precision/length/SLO披露，不外推持续闭环或全foundation causal alignment。2+1+2=5标准拟Only：generic multimodal counterfactual支持可保，不按医疗标题关闭整个机制，也不恢复诊疗/科学应用；无必要长期Books新增，待有限非作者。

- `15706 Target-Oriented Pretraining Data Selection via Neuron-Activated Graph`：[official v1](https://arxiv.org/html/2604.15706v1)，实际§2–4/Tables1–4、Limitations、必要A.3/C/D/F.2/J。projection列zero后的局部output差等于activation magnitude，只是省最终loss的local proxy；逐层topK index集合及target频率重叠构成rank，非真正有边message passing图或唯一functional backbone。fixed K各层时group-frequency形式等于average Dice（D），变量宽度不能无条件沿式。Deactivation20/层0.12%与random造成不同损伤支持high-impact，C500样本/122 bins同时跨层50-neuron干预的r .71±.02不是每个neuron因果utility证书。
  RefinedWeb600B→150B pool、各法30B token20% selection、同1.2Barch从头训；targetA.3含train/validation，不沿主文exclusivelytrain措辞：MMLU1531validation，XWinograd2124non-English，13gram去重仅literal条件，不宣称完整无contamination。multi-target每target1/6直混无dedup/reweight，better平均不证所有领域最优mix；singleTable1NAG有个别不胜BETR/FineWeb，Table2部分MMLU反向，§3.6文字35.4/34.7与表值不同不采该单数。lastlayer−4.1和HellaSwag sparsity .3%最佳是真实local接口选择，不普遍层因果/阈值。
  F.2单forward每doc、150B/Qwen1.7B/H100SXM80GB192GPUhour是one-time extraction，换model/tokenizer/features需重建，target复用不等免费selection；CPU随机子样本threshold O(N)为近似topfraction，不自动exactglobalranking。J random五run std .18–.55不代表所有NAG训练多seed，binomialSE是evaluation样本不确定性不替模型runCI。precision/sequence/batch/SLO主文ND。2+1+2=5标准拟Only：内部全层特征作target selector与局部替代支持有贡献，保受限recipe/反证，不新增“selection信号拥有训练真值”；当前Ch27 proxy admission/最终held-out target训练职责尚无需改，不能说全部NAG算法Existing。待有限非作者，不将局部规模硬拒。

本两项actual official abs均只有v1/无comments/决定处置event信号；累计56唯一轻核。submitted仅身份，首公开仍联合本日公告链；没有完整版本史扩扫。日普通队列继续。

## 接续：语音工具异步分支与领域上下文安全评价

- `15710 VoxMind: An End-to-End Agentic Spoken Dialogue System`：[official v1](https://arxiv.org/html/2604.15710v1)，实际§3.1–3.3/Eq1–10、§4/Tables2–4/Limitations与G/H/I/J必要成本表。StepAudio2基座Think-before-Speak先生成reasoning，再让当前local-tool action与auxiliary global-tool候选并行；只有显式retrieve才将候选并入下一步localset，非auxiliary proposal直接执行。明确reasoning/action/retrieval分责是局部机制，不把profile/memory taxonomy当新架构。核心Eq4是reasoning完成后action/retrieval并行；AppI说hidden within reasoning不能据此补实现为任意preemptive overlap。union local工具集没有固定上界/eviction，不能由有限10～100工具实测推总体O(1)/任意规模解耦。
  2H20-NVLink、ZeRO3/bf16/checkpointing、batch1/acc8/lr1e−5/AdamW，AgentChat文本工具+CosyVoice2/600音色、反向condition(Q,A)构CoT再judge≥7/retry3。Gemini2.5Flash对GT三次评分是evaluator不等真实execution outcome。Table3 contextualPF75.34 no-think→62.33 think最优mix反向，Table4 IFEval39.64base→18.83最终，平均64.21vs64.15不证明general无损/CoT必要性。H150真实录音与matchedTTS FS86.00vs93.33/PF60.67vs67.33，合成有乐观偏差。I aux1.3131→2.6426s，wait50tools .0154s而average<.015非每次≤15ms/p99；J THINK88/answer701.2 token12.6%非语音walltime零成本。推理hw/输出长度完整latency/SLO/CI主文ND，不采exponential baseline普律。2+1+2=5标准拟Only：语音critical路径的局部工具管理分支可保，当前Ch78 discovery/执行contract无需因headline新定义追加正文；不冒称算法整体Existing。待有限非作者。

- `15717 Into the Gray Zone: Domain Contexts Can Blur LLM Safety Boundaries`：[official v1](https://arxiv.org/html/2604.15717v1)，实际§3.1–3.2、§4.1–4.4、§5.1–5.2.5/Tables1–4、Limitations及A.4.2/A.5/A.6必要budget/judge，不打开payload合集/复现。八topic×三model/三seed对齐领域摘要与mismatch比较支持有限context×目标互动；安全研究frame跨类别不是来源authority，不能从context关联解释反推training associations已被因果识别。Qwen3-8B layer24MDS/attention A/B/C20query仅相关空间诊断，B长context+direct保sensitivity说明不只是length，不能据projection证明“gray zone”为唯一真实decision margin。
  seven主目标JBB100，3retry×2trial×4round/8variants+最高judge选择及跨run成功memory；baselines预算各不同，99%是该selected有界协议非单次请求事故概率。DeepSeek judge先purify长academic输出，A.6二十样本human85/65/90/90而LLM较高，改judge/抽取支持有限校准，Limitations也承认decontextualize可能反向inflate，不采“净化后准确truth”。Table3 safeguardQwenASR61%、finetune66%/Llama74%残余，Llama safeguard全拒不是成功防御；MMLU/HellaSwag/GSM局部不等合法安全研究helpfulness全保。A.2训练需必要时才读，当前拟Only不采新全防御机制；requesthw/precision/input-outputlength/CI及SLO完整未披露，T0不消除pipeline随机性。
  2+2+2=6，实际context safety评价/中央保证边界深入拟Only：保具体对照与judge反证，不采allfamilies边界失效/完整防御/latent因果保证，不扩科学有害payload。现Ch72 benign内容可改变行为与authority分账、组合/utility验收已有长期职责，局部Jargon协议仅报告，不称全部算法Existing；待有限非作者。

official event实际轻核15710v2Sep15无具体comments/纠错、15717onlyv1无具体决定处置信号，cryptography/security分类不是Important revision信号。累计58唯一本轮轻核，不扫描全版本。

## 接续：临时反馈、trace审计、内部sensor与开放OOD

恢复实际重读AGENTS、当前三合同、Prompt、ROADMAP与月最新checkpoint（20→26→29）；单篇I17已写后核，38工作集合仍未冻结。以下七项继续普通必要原文，不以旧retained/附件存在称完成。

- `15719 The World Leaks the Future: Harness Evolution for Future Prediction Agents`，[v1](https://arxiv.org/html/2604.15719v1)实际§3.1–3.3/§4.1–4.4/Tables1–3/§5。v1正式题与当前abs v3题Harnessing Pre-Resolution Signals不同，使用精确v1题。冻结模型，重复同一unresolved问题的checkpoint notes差异产生provisional procedural harness更新；问内具体facts保note，resolution truth才retrospective修正并跨题carry，是可检查的新反馈支持分支，不把时间差当真值。GPT5.4所有方法同forward-only/256k/100toolceilings但search stack不一、realizedcompute未匹配；五daily100题mean±std是不同窗口非模型seedCI，MiroFlow L4 46.80高于Milkyway45.85。**§4.4/Table3 cohort N/choice/numeric仍[fill in]**；NoHarness禁read/write不独立隔离temporal feedback、notes、初始化，不能采匹配cohort因果/唯一机制胜出；保数字为作者未完全说明协议的有限观察，不抄headline。HW/precision/fulllength/latencySLO ND。2+2+2=6标准拟Only：协议条件可保，但未建立普遍harness promotion有效性，无必要Books新增；不是全篇否定或要求全附件补全。

- `15725 Reasoning-targeted Jailbreak Attacks on Large Reasoning Models via Semantic Triggers and Psychological Framing`，[v1](https://arxiv.org/html/2604.15725v1)实际§3/§4.1机制职责、§5.1/5.2/5.3及§6（不展开攻击payload示例）。proposal扰动以维持final answer同时改变可见reasoning为评价对象；semantic consistency与psychological frame消融支持有限联合recipe，不识别心理因果/所有内部computation。五集各100、每题三试取最高HS成功者，GPT4o同时judge answer等价与HS>1；83.6%是selected protocol不是单次事故或真实effect。local DeepSeekR1DistillQwen14B/single作者写RTX A80080GB，precision/length/端到端完整预算/CI/SLO ND；API约10s与pricing是论文版本案例不核为当前价格。w/o logic HS反升、w/o psych DeepSeek HS3.92>full3.63、跨o4mini不对称保留。o4mini raw reasoning API的实际可见channel/summary/parser未说明，不能补成完整内心读取或架构漏洞确证。§6三类防御是建议非实验。2+2+2=6具体trace protection深入，拟窄Existing：actual Ch72:611–649 CoTMonitor四命题、channel/parser匹配与outcome/authority分账已承载answer-only遗漏和attempt预算；不称完整PRJA被覆盖，待非作者必要核。

- `15741 Learning Uncertainty from Sequential Internal Dispersion in Large Language Models`，[v1](https://arxiv.org/html/2604.15741v1)实际§2/§3/Tables1–3/Limitations、必要B/C。每token跨层regularized covariance logdet、单位向量circular variance及token entropy组成ordered features，PCA hiddenstate+128维transformer head监督BCE，非固定CoE符号/meanlasttoken。Sylvester/Gram(L+1)减少det算术，但需要all-token/all-layer状态与label，不赋sensor事实真值。3–14B greedy、12集80/20，Trivia/SciQ ROUGE-L .7代理，不能当实际全部事实。Table2组合MATH AUC77.56<HS80.01、SciQ80.81<Internal81.92；Table3 OOD InternalVariance AUC60.56>Full58.67，Full仍下降14.67，非model/task agnostic普律。B RTX600048GB Llama3.2-3B timing .26/.37s vsSAPLMA .25/.35；precision/length/batchSLO/训练seedCI ND，非tail/零成本。2+1+2=5标准拟Only，保新sensor的信息support与有限取舍，不新增通用calibration/correctness保证。

- `15756 TTL: Test-time Textual Learning for OOD Detection with Pretrained Vision-Language Models`，[v1](https://arxiv.org/html/2604.15756v1)实际§3.1–3.4/Eq1–9、§4.1–4.4/Tables1–7。冻结CLIP/image/text/classname/IDprompt，仅OODprefix可训；base bimodal threshold伪标签、minority balanced OMB、二次阈值OKP抑boundary、fixedK bank按与ID最远保feature，再校准score。伪标签支持污染可循环，不从tSNE/置信度证明真实OOD语义；empty subgroup/div0条件主文未说明，不补保证。ViTB16/MCM/ImageNet1k及CIFAR100+4/6OOD、AdamW.005/B64/K2048/α.5，β跨数据不同。Table3/4有限消融成立，存全反而差支持bank选择不是全保；TTL-V更好但8MB vs4MB。单3090 perimage11.40ms，earlystop1280samples8.36ms但FPR95 14.21>12.46；比静态8.18ms更慢，不能普遍insensitive/零成本。precision/CI/order与全部stream漂移/SLO ND。2+1+2=5标准拟Only：unlabeled textual-bank adaptation有局部分支，暂无必要长期Books改变，不因视觉/局部直接否定。

## 接续：问题识别、早退理论与参数剪枝保护

- `15760 KWBench: Measuring Unprompted Problem Recognition in Knowledge Work`，[v1](https://arxiv.org/html/2604.15760v1)实际§3.1–3.4、§4.1–4.3/Eq1、§7.5/§8、§10Limitations。223题185 incidents+38已有benchmark改写，去reference暗示并人人给codeinterpreter；expert annotations与三模型rubric生成/人工合并，Gemini3Flash逐15个criterion判；five mandatory任一fail归0，剩40/35/25不是riskprob。三次取aggregate最好，provider温度不一；选到的gatedout任务还能pass辅助项，是profile关联不是同题cue的因果干预。**作者明确无recognition ablation、无humanbaseline、singlejudge**；不能按初筛“同LLM被问概念能答”转述为本实验已配对验证，更不能推无提示失败唯一因果、alignment tax或oracle ensemble部署优越。有限任务/西方组织规范/污染边界保留，HW/precision/length/SLO/跨judge可靠性ND。2+2+2=6标准拟Only：mandatory-framing与执行质量分账的受限证据成立，不采无controlledcue的‘formal isolation’，未新增通用Agent routing保证。

- `15764 When Do Early-Exit Networks Generalize? A PAC-Bayesian Theory of Adaptive Depth`，[v1](https://arxiv.org/html/2604.15764v1)实际II/III全部必要定理、IV/Algorithms/TablesII–VII/VI。保marginal H(D)与conditional H(D|X)区别、nested F与i.i.d./label条件、depth经验分账；不按HTML stripping的丢sqrt误判，已重开official MathML原式。**中央推导争议**：III-A Step4实际KL(uniform)=lnK−H(D)，Step5却说KL给−lnK与union +lnK相消；K=2,p=(1,0)时H0，KL与δ/K confidence各+ln2，不能从该两步得H-only。III-A Cor2没有KL项，deterministic routing本身不使学习后posterior=prior或classifier复杂度为零，所给条件未足以解释移除；III-C输入依赖route的class复杂度分解也未补router class条件。III-G coefficient sqrt(2ln2)=1.177数值正确（不沿抽取误失sqrt反例），但δ/K confidence常数本身不证明entropy出现两次。只隔离H-only/PAC guaranteed bound、无validation认证和理论tightness保证，不否定协议/表数字或全部earlyexit。
  4A10080GB/600GPUh、visionb128300/90epoch/NLPb32seq128或512/3ep，五seed42/123/456/789/1024、80/10/10 calibration+heldouttest，作者claimt-test/Bonferroni保为披露非复现。TableVI FixedH0却最高gap、positionGPT2 late tightness4.8、εK<.24不是自动negligible均保；Alg1用S empiricalloss，需有label，不能补privacy no-label免费selector。precision/生产SLO/完整Supplement所需证明ND。2+1+3=6 correction深入拟中央窄D；重开需KL/union符号一致的完整证明、prior/posterior与fixed/learned backbone/router条件以及Cor2合法化或收窄，不全附件/强制复现。

- `15780 Pruning Unsafe Tickets: A Resource-Efficient Framework for Safer and More Robust LLMs`，[v1](https://arxiv.org/html/2604.15780v1)实际Methodology四阶段、Experiments/Tables1–8/Limitations与必要C overlap/judge。model-specific safe/unsafe outputs+LlamaGuard/refusalfilter，response-token masked Wanda proxy、ratio/zscore componentrank、greedy或beam重算，是具体不反传mask branch但不证明唯一unsafe subnetwork/semantic competence全保。l50/K32/p10%/ρ3%/b1=b2=5、final Unsafe+UltraChatutility选checkpoint；默认T1每out3sample/含8bitvariant。**beam selection印刷方向冲突**：L=CEsafe−CEunsafe欲保持safe低而unsafe高应更小，正文却保highestL。A(Safe1,Unsafe4)L−3优于B(2,1)L1的目标，高分选择B与叙述相反。只隔离所写beam objective与其‘此方向保证安全/utility’可执行保证，不否定greedy/profiling或所有实验。
  Table1 beamunsafe1.17但overrefusal46 vsbase22.7/utility7.13<8.07；robustPAIR21.8/GCG17.5残余，Gemmaover65>42.5/utility6.48<7.35；8bitGoal文字48.3与表60.3不一致保表。C ROUGE-L无近重复不排semantic leak，twojudges84%agreement不校truth；LlamaGuard厂商69recall/11FPR/61F1不自动生产准确。Table5 memory为building峰18–48GB，beam2457–16722s，与deployment extra0token/平均input计时分账，不能抄‘pruning无额外内存’。hw/precision非8bit切片/length完整生成/batch/SLO/CI全协议主文ND。2+2+2=6实际保护/correction深入拟centralbeam窄D，保有限mask经验；需objective sign/排序或实际select实现更正与匹配说明才重开该保证，不全artifact复现。

七项officialabs轻核：15719v2Apr20 05:54Z/v3May8但无决定处置comments，v1题绑定；其余onlyv1/no comments/event信号。累计65唯一轻核；submitted不是firstpublic，版本号不自动Important。七项拟处置仍需有限非作者，日ordinary继续，非日Gate。

## 接续五项：模拟数据、跨模态连接、usefulness与训练支持

- `15805 From Seeing to Simulating: Generative High-Fidelity Simulation with Digital Cousins for Generalizable Robot Learning and Evaluation`，[v1](https://arxiv.org/html/2604.15805v1)实际III-A–D/IV-A–D/TablesI–IV/Conclusion。panorama→Marble静态3DGS+collision mesh→prompt cousin，跨room用originalpanorama SuperPoint/LightGlue essentialpose、已知cameraheight解scale、ICP refinement；静态场景不变可动物体，另加asset+物理solver/LLMplacement。可保real-to-sim的数据支持分支，不从生成照片/统一USD推真实物理与全部交互一致。SO101双臂/topdownRGB/30Hz示教，sim100、real20trial；原100→+200cousin数据总量非matched，real50 vs50real+100sim不识别cousin唯一因果。TableIII同100总量50real+50twin .33/.35对100real .37/.35不统赢；只有3task×4policy×4generalization levels的Pearson r.91不证单incident、校准或全部排序；100navigation5assets68%仍32%fail，不等通用物理稳健。trainHW/precision/length/batch/SLO/CI ND。2+2+2=6标准拟Only，保有限执行数据分支与负面证据，不写high-fidelity普遍保证或恢复AIforScience。

- `15809 Aligning What Vision-Language Models See and Perceive with Adaptive Information Flow`，[v1](https://arxiv.org/html/2604.15809v1)实际§3.1–3.3/§4.1–4.3/Eq1–5/§5.1–5.4/Tables2–8。1step attention跨层动态的entropy排名、候选mask ratios .1–.9按分布entropy偏离选择，只阻text query→部分visual key的连接而保视觉状态及visual↔visual，非token删除/保证信息已被有效用。原文§3.2把a(i visual,j text)称image→text但实际standardcausal及图2需要text读visual，语义方向不得直接照录成visual能读future文本；保明确mask对象。§3.3 oracle manual选择仅上界分析不等deployment。LLaVA1.5/Qwen2.5VL7B/VLMEvalKit/POPE三subsetmean；Table7同maskratio随机/逆entropy较差支持局部排序，Table8future-aware fullconnection变差，不推出attention是唯一causal必要原因。oneextra decoding+几msmask作者估计没披露硬件/precision/batch/全部seq/CI/真实SLO；longindirectprompts作者承认失败。2+1+2=5标准拟Only，不因局部视觉硬拒，但暂无必要长期Books新增/无泄漏保证。

- `15827 UsefulBench: Towards Decision-Useful Information as a Target for Information Retrieval`，[v1](https://arxiv.org/html/2604.15827v1)实际§3/§4.1–4.4/Eq1/Tables1–3、§5.1–5.5/§7。三analyst15reports10industry、1110query-doc gold+53kfull，independentretrieval→consensus，relevance与decisionusefulness分标签且21.9%高相关只部分有用，可保retrieval目标区分的新局部验证，不因可持续领域关闭通用IR评价，也不恢复其科学应用。未被标的fulldocs赋negative与stoplabelselectionbias，relativeorder保持是作者推测非保证。yhat×p(yhat)然后minmax是heuristicscore，不是三个class的规范概率/真实decisionrisk，ECE/Brier不采用为实际事件calibration保证。GPT4.1T0/BGE/BM25，同sourceexpert50错误有6–8%annotation错/30%knowhow模糊；LLM排名未优于BGE、mini→full趋平不证明universalcapacity ceiling。专门targets/actionsdesc F1降、去keywords F1/ranking不改善、fewshot/Ft reportlevel60/40改变classification但calibrationheuristic反向保留。hardware/precision/length/batch/cost/CI/SLO ND。2+1+2=5标准拟Only，数据和support匹配尚不足写长期整体ranking/专家真值保证。

- `15829 Beyond Text Prompts: Precise Concept Erasure through Text–Image Collaboration`，[v1](https://arxiv.org/html/2604.15829v1)实际§3.1–3.5/Eq1–10、§4/Tables1–3、必要A.1–3/B.4/B.5。promptbank Dirichlet(1/τ)凸混合+optionalGaussian再LN、cleanSD synthlatent多scale transformer与UNet jointlyfit negativeCFGtarget，属真实erasure与nearbyconcept保留分支，非纯textname。凸embed hull不授semanticvalidity/安全全部coverage，Gaussian与LN也不必在原hull；§3.3highτ uniform/lowτ sparse与Eq3相反，B.5正确承认τ升更sparse，因此不采旧温度解释，不误称数学整段必然无效。A600048GB/SD1.5/200image每concept/lr1e−5/b1，GPT5.0prompt及CLIP/NudeNet.6/evaluator有限；syntheticprior不‘unbiased’，COCOFID不证相关concept完好。MCP camera92.06<clean92.54、表3NoHVRL P4D0<full.04/NoCCCMFID30.41<full30.86，不能所有指标/模块必要。B.4 sharedprompt controls作者披露但trainbudget与visualinput不同，不识别convex唯一cause；preservation非generaloutput真值/completeerasure，precision/step生成len/CI/SLO ND。2+2+2=6实际erasure protection深入拟Only：保局部方法/反证，不采用语义凸性或零残余普遍保证、不新Books。

- `15830 Placing Puzzle Pieces Where They Matter: A Question Augmentation Framework for Reinforcement Learning`，[v1](https://arxiv.org/html/2604.15830v1)实际§4.1–4.4/§5/Tables1–2/Limitations及B/C/D/必要E。weakdifficulty筛→当前model成功count区间→teacher解析/noveltydifficultyimpact评分→capabilitytiertopk hints→按每题samplingcounter每Ncheck2去最弱piece，最多3，是真实curriculum/exploration分支而非hint数量headline。Eq4写pass@m却等成功count不是usual至少一次成功概率；minmax相等V denominator处理未披露，freqwithdraw不是实时mastery。8A10080GB/GRPO16rollout/T1/topP1、512train/32mini/2400update/FSDP/vLLMTP2/2048prompt8192response/lr1e−6。32B跨modeldata/training不matched，Table1QwenAIME25 38.8<47.5、Minerva仍远低32B45.1，不能全胜。Table2/AppendC prefix25%60.4 vs58.8两个所谓相同setting值不一致保留，不补统一协议。D32?实际1000teacher/500overlap是teacher稳定性非trainingseedCI；Econtradictoryhint AIME50.6<54.5且劣hint确降。pass@k更高不单独证明多样性/不存在dependency；offline每题teacherAPI与samplingselection有成本，precision/CI/walltimeSLO ND。2+1+2=5标准拟Only，保具体支持/撤架接口，不采1.5B=32B、scorer真值或必无损。

本五officialabs轻核15827v2Apr23、15830v2May1但无具体comments/重要修订信号，其余onlyv1；15829security分类非revisiontrigger。累计70唯一轻核，不扫描全部版本/附件。五拟处置仍待有限非作者；日普通继续。

## 接续五项：形式化题意、内部算术、痕迹遗忘与保证判定

恢复实际重读AGENTS、当前三合同、Prompt、ROADMAP及月最新checkpoint；路线20→26→29，ordinary继续。apr01两项实际非作者审核已读：[CPO/NAG有限处置](./V3_APR01_CPO_NAG_DISPOSITIONS.md)，两项5标准Only通过，非日期/日Gate；Fig7非严格正交、latentD未识别、validation支持与192GPU小时、random五run非NAG CI继续保留。

- `15839 Discover and Prove: An Open-source Agentic Framework for Hard Mode Automated Theorem Proving in Lean 4`，[v1](https://arxiv.org/html/2604.15839v1)实际§3.1–3.2/§4.1–4.3/§5/Table2/§6.1–6.3/Tables3–4/Limitations及必要D/G/H。natural-language discovery候选→把答案代入Hard→Easy statement→Lean4.15/Kimina/GoedelProver32B验证；rewrite后的proof不能独自证明原题语义与未知值确被求解。两专家交叉重标、D列extremum可达性/额外条件/缺目标/缺NL四类约35修正；H实际同集合abbrev加rfl可合法close，未求canonical solution，是具体verifier对象反证，不是Lean本身不sound。hard数量Table1/AppendG194与Table2/3 197不统一，保精确表而不补统一分母。GPTOSS120B T1/至多30selfverify、失败回退no-agent；proverT.7/30000max/32samples，非同总compute。Table2 noagentCombi10>9、mini204>201，FIMO均3/0；不采selfverify普遍必要或全winner。Table3 Putnam293/340 natural答案与Table2 19 Hard formal不是同类accuracy，training corpora未知而公开题污染仍可能；hardware/precision/端到端时长CI/SLO ND。2+1+3=6，具体评价纠正深入，拟窄Existing：actual Ch66“Binary Verdict通过不等于语义忠实”与compound artifact中的task-spec/verifier残余owner已承载proof-of-encoded-goal≠题意；仅该命题已有覆盖，Hard/Easy recipe与表仅受限报告，不把全DAP判Existing，不恢复数学科学应用。

- `15842 Disentangling Mathematical Reasoning in LLMs: A Methodological Investigation of Internal Mechanisms`，[v1](https://arxiv.org/html/2604.15842v1)实际§2.1–2.3/§3–6/Fig3–9/§8/Limitations。GPTNeoX20B/GPT2XL zero-shot、每个add/sub小大集500、operand/result≤520保证单token；LMhead投影postattention/postMLP final-token可观测数词/正确结果时间不同。large结果late而small26层先出现；64%只一个operand进入top1只是logit-lens可读性，不说明另一个不存在/唯一隐式函数。§6 pyvene互换最后input位置attention输出、source只换一operand/operator，层14 operator干预base-result概率降>30%支持局部路径敏感；不识别每个neuron必要性或后续MLP唯一原因。三operand四组100 accuracy≤.12与62%少可读operand是关联，不由top1缺失推信息不足定理。Limitations明确MLP依赖还需验证；模型能力/训练史差异不能把GPT2对比升为所有模型必要架构。hardware/precision/batch/全部decoding/CI/SLO ND。2+1+2=5标准拟Only：保可读性与干预分开的新局部mechanistic证据，不因简单算术/小模型关闭，不采“只有最终层形成正确计算”普律，无必要Books新增。

- `15847 CiPO: Counterfactual Unlearning for Large Reasoning Models through Iterative Preference Optimization`，[v1](https://arxiv.org/html/2604.15847v1)实际§3/§4.1–4.2.2/Eq5–6/§5.1–5.4/Tables1–4/Fig5/Limitations/Ethical及必要D.1–3/E.1–2。同target模型先改answer facts再backward构CoT，fixedpositive加每轮currentnegative、SimPO+positiveNLL+retain，SFTwarmup，是具体trajectory替换训练分支；graph cut/do只是目标定义，self生成不证明F-independent或参数训练影响删除。同Q可能含相关知识，conditional independence不能由pref margin或风格一致推出。自训DeepSeekR1Llama8B 15ep替换崩溃releasedtarget；RTOFU1/5/10% synthetic，MU/AFE/CFE harmonic ROUGE/cosine/NLI/entropy+GPT4o是代理非参数擦除。2A80080GB/greedy评估、5ep/checkpoint validation、多法不同LR/保warmup{3,5}与5ep边界；Table1 CiPO MMLU/GSM仍部分低于target，CFE.4468非complete。RETURN260由NLL>90%和两轮judgecorrect筛、50%forget非所有敏感事实代表；realForgetACC.3178/CoT-UA.4446，第二Qwen8Bretain.7407低于原.7778，两个8B不证modelagnostic。judge未独立human校准、多seedCI/precision/fullbatch/length/timeSLO ND；Ethical明确adversarial泄漏可残余。2+2+2=6具体删除保护深入，拟窄Existing：actual Ch72:259 observablechannel+retain/collapse及2115起参数/行为分账已覆盖answer-clear≠trace-clear≠dataset-influence删除；不称全部CiPO算法已有覆盖，不采用因果独立/永久擦除，训练recipe仅受限报告。

- `15851 DPrivBench: Benchmarking LLMs' Reasoning for Differential Privacy`，[v1](https://arxiv.org/html/2604.15851v1)实际§3.1–3.2/T1/§4/§5.1–5.2/T2–4/§6.1–6.3/T5/Q26/Q57。49GPT5初生经作者过滤函数bank、作者算tight sensitivity，六机制positive/单noise倍率negative；125advanced=42yes83no由algorithm/assumption/guarantee单组件扰动，reference+负例解释是作者label依据，不等本次逐125形式证明。缺一个充分条件不自动反证具体算法privacy，label correctness与模型binary verdict分账；没有扩全论文链，拟结论仅受限benchmark。Q26顺邻disjoint≠pairwise，可取X1=X3而X2隔离使多次同record发布，是具体保护条件反例；Q57 function-value sensitivity≠argmin sensitivity，不补缺失假设。11models无tools/5seeds，binary不遵令由GPT4o二次映射，平均±1.96SE非每算法证明；Cat2 F1.742/.748并非accuracy，alwaysyes.503。18最难题oracle theoremvsRAG不是全题matched增益；GeminiRAG实际换3.1checkpoint，保反向例，one-shot只LaplaceRNM同类.573→.737不泛化所有数学保证。hardware/precision/fullprompt/预算CI以外/SLO ND。2+1+2=5标准拟Only：具体假设错配与不同mechanism识别有贡献，不把security分类自动全Deep，不采LLM能签DP certificate或label-bank全面sound，无必要Books新增。

- `15859 QuantSightBench: Evaluating LLM Quantitative Forecasting with Prediction Intervals`，[v1](https://arxiv.org/html/2604.15859v1)实际§3.1–3.3/Eq1–3/§4.1–4.5/Fig1–8/§5.1–5.3/T2–3/§6。1000future数值、Jan–Aug2025背景320knews/512chunk/embedding3large、Sep2025–Jan2026resolution、zero/background/agentic固定corpus；documentedcutoff声明与固定retrieval只约束可见信息，不独证参数污染不存在。coverage与Winkler宽度/漏出距离分账，log变换前提是l/u/y严格正；0/负值/非法bounds处理未披露，不采任意数值普适properness/单位无关。90%target最佳79.1不是90%实际coverage；GPT5.1比5.4 coverage低但MLIS好，排序取决目标。更多iterations与难题选择混杂，不证明retrieval导致退化；width/y与miderror/y共用真实分母，相关不直接证明内部不确定性有效calibration。Table2 GPT5.1 medium优于high；改置信水平同时改变alpha评分惩罚，不把不同alpha的MLIS改善直接当同一loss质量改善。作者固定corpus不证明live更新/forecast可落地，fullhardware/precision/tokenbudget/batch/runCI/SLO ND。2+1+2=5标准拟Only：interval-based多指标和scale切片局部增量保留，不新增普遍未来风险calibration/模型排序保证。

五项officialabs轻核已实际查看：15839/42/47/59仅v1，15851v2May15/v3May18无具体revisioncomment；页面未提供决定处置withdrawal/erratum。累计75唯一轻核，不扫全版本。submitted仅身份，不代替本日联合firstpublic链。五项拟处置待有限非作者；普通日队列继续，非冻结/日Gate。

## 接续五项：judge角色、编辑route、语音层级与硬件执行

- `15873 How Hypocritical Is Your LLM judge? Listener–Speaker Asymmetries in the Pragmatic Competence of Large Language Models`，[v1](https://arxiv.org/html/2604.15873v1)实际§3/§4.1–4.2/Table1/Fig2/§5/Limitations及A.1。speaker生成与listener判断同underlying item分责，三pragmatic tasks/14models（falsepresupp仅3）中条件关系和均值关系不同；不是同prompt/信息集：false speaker旧study无显式指令，listener另给已知falsepresupp/原answer；forced-choice vsbinary任务也不完全同难度。德语两任务/英语deduction，不独立language效应；Δcond有负也有GPT4o .56–.94正、GPT5ceiling，不证明必然独立/更会judge。解析严重混杂：Qwen8B两role不可parse、13Bspeaker5%、Sonnetlistener5%；留原表不把低分全解释missingcompetence。A.1单A6000/greedy/1–48GPUh、API几USD，precision/fullmaxlen/batch/seedCI/SLO ND；行为非内部/心理因果。2+1+2=5标准拟Only：judge/generator角色切片有限反证，不采全judge真值或泛化hypocrisy主张，无必要Books新增。

- `15917 Making Image Editing Easier via Adaptive Task Reformulation with Agentic Executions`，[v1](https://arxiv.org/html/2604.15917v1)实际§3–§5.5/T1–5及必要E/F。smalltarget/隐式spatial/local-global冲突按profile路由directrewrite、SAM空间分解或cropeditpaste；中间feedback+stepcap+originalsinglepassfallback，是固定editor输入operating regime分支，不让planner完工声明成为物理/语义authority。pilot只选direct最差40%再MLLM归因，成功回收非全流量无偏因果。Bo2与ATR平均1.2–1.71backbonecalls有实际成本对照但额外profiler/planner/SAM/evaluator未等总compute；三evaluationruns没runCI。Table2 QwenAdd/Remove/Style/Action仍低于base，Table5 oracle/full4.22/4.16不等所有route正确；不同表full4.13/4.16不合并。E局部rustwheel反违灰度globalstyle是直接failure。F由MLLM把PICA4112→3879QA过滤，glassmove/ropeend两反例可保，但不是独立全label审计/原始PICA可直接横比或严格objectiveguarantee；留过滤cohort。HW/precision/全部length/batch/timeSLO ND。2+2+2=6标准拟Only：保新route与负面operatingpoint，不采capacity问题均已消除/全物理真实，无必要Books新增。

- `15923 Hierarchical Codec Diffusion for Video-to-Speech Generation`，[v1](https://arxiv.org/html/2604.15923v1)实际§4.1–4.4/§5.1–5.4/T1–7。12RVQ×1024、低r1–2连lipAVHuBERT与ArcFace→GE2E identity、高r3–12由Poster2 emotion proxy，channel/temporal AdaLN、64Euler unmask是codec层级×条件选择分支，分层不证明完全解耦。训练用真实acoustic identity/emotion替视觉条件、推理视觉，不能写全流程visiononly/无train-testgap。Vox261.5h169kutters3438speaker；LRSheldout、200k/b32/lr1e−4、lambda100，baseline含引用论文数字/不同trainingdata。LRS2WER39.99劣FTV38.09，LRS3UTMOS3.84劣3.99/SpkSim.5678劣.5981；audioidentity变体不得与visiononly混。T5去hierarchy同时改变模块/conditioning，不能唯一归因层级；去dualAdaLN UTMOS3.92>3.84，LRS2Emo68.61>68.21。20participants/30samples MOSexp2.88<FTV2.90、A/B有限preference非真实speech等价；film160utter56speaker WER58.7仍有限。HW/precision/seq/fullbatch/latencyCI/SLO ND。2+2+2=6标准拟Only：保representation-conditioned生成与训练支持边界，不新增普遍visualidentity/语音因果保证。

- `15938 VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation`，[v1](https://arxiv.org/html/2604.15938v1)实际§4.1–4.4/Eq4/7/8/Alg1、§5.1–5.3/T1–5及0.A/0.B.1/0.B.3–4；关键公式另开官方HTML MathML验证，未把sqrt提取丢失当反证。具体timestepsampler+轨迹重采样与VLMstage→(Na,Nd)控制可保。**中央unbiased/hard-mining实现窄争议**：Eq7 q=w/Z直接MSE期望为sum(wℓ)/Z，而Eq4 uniform weighted为sum(wℓ)/T，缺Z/T标度；learnedπ不带w/(Tπ)不能保同weightedobjective。取两步w=(1,3)、loss=(1,2)，目标3.5、q期望1.75；learnedπ=(.5,.5)为1.5，非仅一固定标度。Alg1用r=−standardizedloss还更新trajectoryweights，与Eq8正standardizedloss优先hard方向相反；两loss1/3 mean2,std1时hard r=-1、easy+1，alpha1前者0后者2，clamp不反转方向。不否定局部实测/所有robotpolicy，只隔离印刷算法无偏、hard优先及该原因唯一提效保证。
  2A600048GB/b32/3seeds600–3500ep，0.B Qwen2VL7B BF16/448image、offline stage schedule+hardestheuristic、periodiccachedstageclassification，不是每action全VLM/所有stage概率已校准。主文Nd20–40而附例60保协议差；T3 perstep159.4/64.8与total7968/1199不同分母，2.46×来自前者DDPM→DDIM+VADF，不叫sameDDIM alone2.46×。T1Transportmh.80<.82、T4Kitchen99.9−99.4=.5非主文.6，最佳checkpoint/seed有限；realRTX5880/500Hzcontrol不等15.4Hzpolicy、3tasks15trials不同utility无CI。precisionpolicy/fullobservations/actionlength/e2eVLMaccount/SLO ND。2+2+2=6 correction深入拟窄D；重开仅需Eq7 normalization/actualimportancecorrection、Alg1/Eq8 reward sign与实际选择统一说明，保HVTS协议/表，不全artifact或全实验重做。

- `15944 CIMple: Standard-cell SRAM-based CIM with LUT-based split softmax for attention acceleration`，[v1](https://arxiv.org/html/2604.15944v1)实际IV-A–E/V-A–C/VI/T1/Fig8–11。dualbank SRAM8bit分片、32bitacc→int8、固定quantmax移位expLUT先累exp×V再reciprocaldenom，CIM近内存非线性和MAC耦合支持具体流水选择；固定移位exact-arithmetic等价不证明finiteLUT全条件精度。32kbCIM+16kbglobal、ST28FDSOI，26.1TOPS/W 0.85V417MHz post-synthesis与2.31TOPS/mm² 1.2V770MHz post-layout不同点，87.5%activation/50%weight sparsity；排global57.9不能当含global。其他表siliconmeasurement不matched，power含global约48.4%不可忽略。33%latency为encoder1024/head64/400MHz vs32bit nonsplitLUT，不是完整decoderSLO；TinyLlamaINT8 PyTorch四任务隔离softmax数值且LUT用fullprecision，三任务下降，非实际CIM运行整模型。作者明确onchip装不下全TinyLlama且externalmemory可能主导，精度测试与hardware流水不绑为端到端LLM能效；input/outputfullbatch/CI/SLO ND。2+2+2=6标准拟Only：保真实新mapping分支与成本边界，不因小模型/CIM硬拒，也不制造芯片实测/通用attention等价或Books保证。

五officialabs轻核：15873/15923/15938仅v1，15917v2Jun30、15944v2Apr20 08:14Z均无具体revisioncomment/纠错信号；v2时间窗外不扩全diff。累计80唯一event轻核，不代替firstpublic。全部拟处置尚待必要非作者，日ordinary继续。

### 联合检测头、编辑分责、匿名化与逻辑检索五项必要证据

以下是作者实际必要审阅，不预支非作者PASS、冻结或日Gate。

- `15945 RAGognizer: Hallucination-Aware Fine-Tuning via Detection Head Integration`，[v1](https://arxiv.org/html/2604.15945v1)，实际§3.1–3.3/§4.1–4.3/T1–4/§5–6。中层3层MLP与LoRA r32/alpha16、response-only CE+BCE λ1共同训练，冻结base却更新adapter，让sensor supervision反向影响状态表示。18,492 responses、2315/2308 answerable pairs、40/60 split，Gemini2.5Flash token标签；100例单人response-F1 .954仅初步一致性，不验证全部token/gold真值。Wikipedia引用时间晚于May23 2024不能独自证明事实之前未知，且Qwen3-4B-2507已用于评价，不采参数无知识/无污染保证。Llama2 joint AUROC .789→.896，但language quality99.93→98.41/relevance98.59→98.03，NoCtx AUROC69.26<HallucinationProbes72.29、closed RAGTruth90.25<Lettuce95.60。检测专用/末层更高但牺牲generation，TextFT golden answers与joint generated labeled answers非只改一个loss的完全matchedcontrol；40/60 paired-query split未给group-disjoint详情。单轮QA、固定λ/未检其它能力，3.7M参数不证明零latency成本；hardware/precision/batch/CI/SLO ND。2+1+2=5标准拟Only，保posthoc→joint supervision有限分支，不当truth/普遍幻觉擦除，不为联合loss成熟原理加Books。

- `15948 From Competition to Coopetition: Coopetitive Training-Free Image Editing Based on Text Guidance`，[v1](https://arxiv.org/html/2604.15948v1)，实际III-A–C/Eq10–19/Alg1–2、IV-A–C/TI–V，必要公式另读官方MathML。两branch差分attention→dual entropy→动态binarymask、cross-step divergence→latent gradient refinement为具体控制分支。**零值有限性窄争议**：Eq10 ReLU(As−Ae)，允许As=.2/Ae=.3时Abg=0，Eq11 −.3log0无有限值，后续norm比值/差分可能∞/∞；Eq16 std(hd)=0与Eq19 norm(hd)=0也未给处理。不是MathML抽取错误：Alg2 line2实为1−A，撤销抽取文本看似负数log的错误反例。Eq18加hd未乘mask，梯度局部不自动证明全部背景逐步不变。LCM-SD1.5、PIEBench>700/9类、PIEBench++、8A6000 seed0、No50；无训练不等无推理优化。TIII去掉spatial/temporal的CLIP editing指标25.82/25.41高于full24.60，L1 FCES30.62高于L2default29.81；保真实fidelity/editing trade-off，不称所有metricwinner。10人7000annotations均值无CI；precision/端到端latency/总budget/SLO ND。2+1+3=6，中心公式有效性定点纠正Deep拟窄D，仅隔离印刷entropy/refinement为有限可执行且背景保证的主张，保受限tables/两branch协议；重开只需epsilon/clamp/zero-std/zero-norm与mask范围的必要实现/算法说明，不全附件复现。

- `15958 A Case Study on the Impact of Anonymization Along the RAG Pipeline`，[v1](https://arxiv.org/html/2604.15958v1)，实际§2.1.1–2.1.5/§2.2/T5a–c/§3。PRE原文匿名再embed/generate，POST原文先进embedding/API再匿名答案，暴露面不同，后者低输出PII不证明上游无暴露。800docs(300BBC/300Enron/200TAB)、metadata锁定单doc/top2且每doc≤2chunks，**不是全corpus真实检索recall控制**；M1Pro16GB仅客户端，OpenAI embedding3small/gpt4omini20240718 T0/Pinecone云。PII Presidio删除/label/synthetic与3DP方法各3ε；per-word ε1/2/3、DP-Prompt150/200/250、DP-MLM50/75/100不同定义，不能直接同一doc budget比较。LLM-J也是gpt4omini，均类别实体trace比例，不是攻击成功率/DP实证；ROUGE/cosine比原始生成summary，非独立gold；Table5 BBC deletion PREprivacy8优于POST23而POSTRL.93>.47，TAB DPIprompt150 POSTprivacy9<PRE17但PPL3490.07>40.66，不采所有方法统一方向。官方MathML确认TO=(1−J/100)/(1−mean(RL,CS))为ratio，非乘积；TO>0不能独自推出gain超过loss（须>1且同尺度意义），不采“正值即privacy胜出”。2+1+2=5标准拟Only：有限放置点trade-off/例外值得保留，不因CR分类自动Deep，也不采用端到端匿名/统一privacy最优。

- `15967 TwoHamsters: Benchmarking Multi-Concept Compositional Unsafety in Text-to-Image Models`，[精确v1](https://arxiv.org/html/2604.15967v1)，现abs v2改题不回拨。实际§3.1–3.5/§4.1–4.4/T2–4与必要A.3/B/T5–6。51conceptpairs/10policy categories/17.5k筛选后样本；每atom满足固定policy而组合unsafe为数据构造条件，不是预测latent定律。ViT三head unsafe∧alignA∧alignB只能给组合风险proxy，不构成causal证明；300k混合训练与baseline零shot、minor架构变化不隔离“只是数据缺失”。500iD/500unseenpair OOD三专家Likert，Pearson.8322/.4904为有限相关，不证明无overfit或全文化安全。T2FLUX MDR.48/SCR99.56是此构造distribution/闭ontology evaluator，不是生产99.52%事故率；T3textfilterrecall81.52>visual子集，有限erasure4pairs且T4 UCE等有反向，不能普遍“erasure均失效/utility collapse”。attentionheatmap/tSNE不是内部社会理解/独立性机制证明，P(A|B)≈P(A)是futureproposal非已实现防御。2+2+2=6，组合风险确实影响保护验收边界定点Deep拟Only：保原子/组合/untargeted utility分账与局部防线失配，不为taxonomy或社会policy主张新增Books；generation hardware/precision/seed/fullbudget/CI/SLO主文ND。

- `16021 Neurosymbolic Repo-level Code Localization`，[v1](https://arxiv.org/html/2604.16021v1)，实际§3.1–3.4.3/§4.1–4.3.4/T2–4/§5。AST来源facts→LLM Datalog proposal→Soufflé parser/高可信语义check→确定执行→原文核，不给parser语义truth authority。五mutation string relaxation/drop-one(默认cap3)保head，**仅诊断不把变体答案当原查询答案**；stable-empty包括probe失败，不能证明不存在，fragile只提示overconstraint，不代表原限制错误。225synthetic逻辑query/9Pythonrepos且人工确保非空；negative一repo约25notall，不能采两authors+新query消除data leakage/全code理解。SWE Lite274排新function/import、keyword省略不是同题随机干预；Table3全局Acc有更低，不称全面胜出。API模型/CPU Xeon4216/62GB/Soufflé2.4/T.3/max20，离线facts构建/更新不能藏，Table4前25子集Base/VAL/full，Qwenfull136s>VAL104、ExecSucc同84.12，Claude PLR42.86%分母与25说明未统一；mean39.3s/16.2ktokens非tail生产SLO，precision/CI/concurrency ND。2+2+2=6；actualCh76 procedural index/source authority已有，但空关系diagnostic不静默放宽查询的具体分支尚需owner提案比较，不能仅按Datalog名采，也不先记I。已完成必要source，普通Books提案继续。

本五actualofficialabs轻核：15945/48/58仅v1；15967v2Jun20改题、16021v2Apr20 05:47Z无决定处置revisioncomment，不扩全diff。累计85唯一轻核；submitted只身份，首公开仍本日联合公告链。上述拟处置待非作者有限核，日ordinary持续。

### 空间规划解耦、输出多样性、前缀剪枝与分词/扩散边界

恢复后实际重读当前AGENTS/三合同/Prompt/ROADMAP与月最新checkpoint；路线20→26→29，正式日仍进行中。Apr02三项处置核已实际读取并同步15701 F.2/F.3修正，非日Gate。本批仅读必要机制、表与直接反证，不展开全部附件。

- `16022 SocialGrid: A Benchmark for Planning and Social Reasoning in Embodied Multi-Agent Systems`，[v1](https://arxiv.org/html/2604.16022v1)实际§2.1–2.6/§3.1–3.5/§5与必要B.2/C.2/H/J。无显式讨论、task/voting两phase，A* easy导航oracle与medium只提示/hard无辅助分开；oracle减空间负荷不等导航完全成功/社会能力唯一因果。task completion、仅已完成task上的planning performance、只non-skip vote的detection accuracy分母不同；mean29.9%对照的33%是固定初始2/6基线，C.2承认存活crewmate变化会增chance，不能把静态初始值当每轮真实随机胜率。64,184 vote的关键词频率/模式关联不是内部证据积累必要机制，failure类别重叠不可相加为partition。7crew无imp20episode vs5crew2imp跨模型league共952episode，complexity每配置3，不混同独立seed CI。H10080GB/vLLM/greedy/max2048/timeout240s/JSONschema；GPTOSS low effort与其它none，完整precision/concurrency/tailSLO ND。PPO仅Qwen3-4B单crew、7×7/2500updates/r8，不泛化社会RL失败；game killcooldown/imbalance为作者明确替代解释。2+2+2=6标准拟Only：保oracle解耦与条件分母的有限评价增量，不采near-random普律或空间/社会严格独立，无必要Books新增。

- `16027 Where does output diversity collapse in post-training?`，[v1](https://arxiv.org/html/2604.16027v1)实际§3.1–3.3/§4.1–4.4/§5–6及必要A/B/H/J相关污染段。13 Olmo3-7B checkpoints三lineage同base，但Instruct从ThinkSFT出发，data/teacher/start与RL预算共同变化，不能唯一归因teacher数量、SFT/DPO算法或宣告数据决定最终floor。15tasks，每prompt16samples、常见N500/max32768/T.6/topP.95；base温度敏感附H实际同时改T与topP，不称temperature单变量控制。SBERT与Vendi共享kernel非独立重复证明，NLI句位对齐/AST只parse且correct，均不直接识别内部mode或真实观点覆盖。六可验证任务correct-only条件Kc≥2，其support和correct计数随模型变化；全样本与正确样本差不自动等无偏因果分解。ThinkSFT约−62%/Instruct−38%，RLZero~93%伴GSM8K49.8–61vsThink93质量代价；禁CoT是OOD输出干预非weight rollback，WritingPrompt+.046/IFEval+.025反例必须保，不能沿“in no case”普遍句。TruthfulQA多数投票反退、HumanEval pass16/1排序相反可保为有限测量；3gram9任务≤2%与六任务7–30%重叠不证无污染。hardware/precision/全部训练compute/run CI/SLO ND；future明确需直接data-composition干预。2+1+3=6标准拟Only：保方法/数据/质量与final-answer多样性分账，不采单原因或普适多样性下界，无必要长期正文新增。

- `16029 Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning`，[v1](https://arxiv.org/html/2604.16029v1)实际§3.2/§4/§5.1–5.3/Limitations与必要B.1–3/C.1–5/D.1–2/F。frozen generator先缓存prefix，只有追加STOP token的临时评分branch启用LoRA/分类头，branch丢弃后从未改prefixcache恢复topk；MC32 continuation success软标签是model/prefix/decoding相对有限估计，不是逻辑proof。高低attention例不能识别必要因果或全process validity。N64→8、prefix2048时avg@8|64是selected path平均正确率而非query cons/pass@64；固定预算cons曲线另计。B.3估算8×H100墙钟43.08/39.46/37.79/75.93h仅MC构造，非完整训练成本；8H100/BF16/15ep/rank128–2048，多scale不同label support，不能忽略materialization/adapter。单H1007B/b16/prefix2048 FTable16 STOP verification .20s/.59%，total34.33>baseline33.20、throughput−2.71%；Table7/16 TypeI显式ratio .93/1.74又不同，不整合成零开销或全部成本同等。T.6/topP.95/topK40，1.5/7B max16384、8/20B32768，固定checkpoint/multistage未验；oneH100120B+tools5h/50题39→42/43受该竞赛协议限定，不补未披露量化/seedCI。保留率Eq7是1.5B两任务经验拟合，不是理论scalinglaw。2+2+2=6，actualCh20请求预算→内部feedback已有，但并行prefix的read-only评分branch不污染resume状态尚有具体gap；拟两段source→owner提案，深入受影响内容，不先记I。

- `16037 Stochasticity in Tokenisation Improves Robustness`，HTML404后读[官方PDF-v1](https://arxiv.org/pdf/2604.16037v1) pp2–8与必要A/B配置。固定vocab同decode字符串的noncanonical token IDs，STOK偏置且support不全；STOKUNI只给定per-token splitcount树叶条件uniform、UNI-K跨canonical边界按editdistance全序列uniform，不能混“所有字符串uniform”，tree/MRMDD构造与更长token额外成本保留。Tiny50M30k pretrain/3kFT与Llama1B LoRA1500steps，10k×10训练tokenizations vsICL每example一个、500×10评估不叫matched总预算/多seedCI。Table2 canonical94而UNI92.8，ICL CSQA62.3<68.3；有限greedy邻域attack canonical94→6.1、UNI-K69.6不是全support最坏风险上界。§6.1 Th6.2仅singlelayer/1-Lipschitz激活/有界embedding及相应weightnorm/editdistance条件，mean embedding距离不独证全LLM global Lipschitz或安全保证；QA不扩开放生成。no inferencecost只可指训练后canonical推理，非stochastic输入/ICL所有成本免费；hardware/完整precision/timeCI/SLO ND。2+1+3=6标准拟窄Existing：actual MODEL-TOKENIZER Ch11“Tokenizer与checkpoint是联合行为接口”实际已有同字符串分段影响、行为回归、多分词训练成本与canonicalfallback；仅此命题已有覆盖，uniform sampler与局部表保报告，不声称算法全部Existing。

- `16044 Elucidating the SNR-t Bias of Diffusion Probabilistic Models`，[v1](https://arxiv.org/html/2604.16044v1)实际§4/§5.1–5.3/§6.1–6.4/Tables2–7与必要B/C；官方HTML公式直接确认Eq27，而非sqrt抽取丢失反例。2000CIFAR例forward/reverse输出范数差支持此局部现象，不唯一测量真实SNR。**中央普适理论窄争议**：B Eq27把E||X||²写成||E X||²+Var(||X||)，取一维X=±1等概率，左1右0；可由conditional Jensen另证理想posterior的平均能量不增，但该不等式不推出Eq22标量γX0+φGaussian误差。取X0=±1、Y=aX0+bZ(a,b>0)，理想posterior tanh(aY/b²)有界且非γX0，残差有界非非退化Gaussian；φ=0也不能逐sample等γX0。C Eq32明确假设当前sample ideal，Eq38平方和还需相应噪声joint/独立条件，不从marginal Gaussian自动继承；所以隔离“任意reverse每步SNR必更低”的普适证明与唯一纠偏原因，非否定有条件推导/全部实验。保pixel differential与wavelet低高频schedule、没有额外NFE≠所有算子免费；50k生成FID对fulltrain reference，多sampler/NFE条件表与反向T6高频50step4.06=full不表述严格全面优胜。Table7单A6000固定seed/batch/timestep重复100次平均 .47/.08/.26%增量，没有batch数/precision/CI/tailSLO；FLUX/Qwen定seed仅qualitative不量化普适提升。2+1+3=6，具体理论纠正Deep拟窄D；有效方法/受限tables保留但不进Books，重开仅需合法γ/误差分布与递归/独立假设及对应条件化结论，不请求全部附件或复现。

五officialabs轻核已实查：16022/27/37/44仅v1，16029 v2Jun2但未给具体revisioncomment，16044普通“correction method”不是event erratum，未扩全版本diff。累计90唯一event轻核；submitted仅身份，首公开仍本日联合公告链。五项作者必要源完成而尚待有限非作者，formal分母未冻结，普通余下工作继续。

### Speech编辑、视觉reasoning、FM稳定与proxy采样五项

- `16056 AST: Adaptive, Seamless, and Training-Free Precise Speech Editing`，[v1](https://arxiv.org/html/2604.16056v1)实际§3.1–3.5/Eq2–9/§4.1–4.5/T1–2/Alg1/Fig5–6。FM逆Euler只是smallinterval近似，LCS词/ASR帧对齐把未编辑source latent与条件拼回、新段noise和target条件，再按偏移给弱mel fact guidance；不能从latent-copy推出waveform逐样本无损或身份完美。γ只matched区域/λ.4，finite1−t与区间/forcedalignment错误需原solver/对齐约束，不采所有步骤无条件可逆；style只有单例，不扩dialect/timbre全验证。2000 LibriSpeechtestclean编辑/3.6h/avgdistance2.186由Qwen3-8B改text后筛，nonedited真实waveform不由WDTW证明；Alg1实际对全部词序列duration作DTW，未给ground-distance/重复词配对全定义，不能把它简写为仅未编辑片段逐帧fidelity。单RTX5880Ada48GB/IndexTTS2/WhisperlargeV3/Qwenforcedalign.6B；T2 SpkSim.986/WDTW.2025较好却WER2.91>base2.43/DNSMOS3.792<3.841，proxy非身份真值。AWFG消融WER6.9→2.9/WDTW.226→.203而MOS降低，保质量/保真权衡；无CI/完整precision/batch/NFE/e2e时间/并发SLO，不叫trainingfree即部署免费。2+2+2=6标准拟Only：保speech时长变化的source-recomposition与偏移控制局部机制，不为latent-copy“完美保真”或自动泛化新增Books。

- `16060 Chain-of-Thought Degrades Visual Spatial Reasoning Capabilities of Multimodal LLMs`，[v1](https://arxiv.org/html/2604.16060v1)实际§2/§3/T1–4/Fig1–2/Limitations。17主模型/13MCQ dataset和另5GPT切片，Qwen2.5VL相同checkpoint换prompt支持此局部prompt干预，但MRM不同训练史不能唯一归因RL或textCoT；custom/native与simpleprompt差异、GThinker nonCoT仍degenerate<toolcall>循环明显混杂，不能把其−23.14全作没有reasoning能力。灰图同aspectsize NoImage测text prior，NoImage++新增CannotDetermine为groundtruth，Qwenbase76.41而CoT43.4/GThinker5.55；它暴露缺视觉证据仍具体作答，非唯一证明原图CoT降分因果或全部文本prior有害。Table1 Qwenbase62.68、VisionG1 63.26例外，Table4 GPT4o/4.1mini/5mini CoT反有+.50/.39/.08，不采“alwaysdegrades”headline。4A100/b16/BF16/vLLM.10/maxcontext+new32768/T0/3seeds；Qwen3-30B judge与GPT4o只重核VisionG1 κ>.99非全样本truth。latency/完整公平tokenbudget/生产CI/SLO ND，作者承认未隔离所有confounds/closed训练不透明。2+2+2=6标准拟Only：保视觉证据缺失/格式提示/模型切片的新受限反证，不为缺视觉self-check泛原则改Books，也不沿“CoT必要因果普遍错”推断。

- `16079 The Amazing Stability of Flow Matching`，[v1](https://arxiv.org/html/2604.16079v1)实际§2/§3/T1/Fig1–2/§4。同Gaussian seed→不同pruned/arch输出ArcFace更相似，是有限输出映射稳定性证据，不证明vectorfield/trajectory内部逐步相同或删除未留训练影响。CelebHQ固定VQVAE、FM-DiT/UNet、同domain FFHQ仍CelebHQ-VAE，不能隔离所有representation共同basis。pr=.5、N4096，randomFID25.25±.38仅3seeds vsfull24.24，Loss33.92/Gradinverse29.75退、balancedcluster22.80改善；“halfdata保quality”非所有策略。4kpair ArcFace .79–.83±pairSD不是多训练seedCI/身份全保真；disjoint.69/architectureUNet.55/FFHQ.58均有退。Fig1caption与body XL/patch、小S/patch配置互换口径不统一，不补正确架构。Grad/Loss需7%surrogate+M2T8 sharednoise全样本grad，CLIP+K24cluster筛选成本与训练/生成总预算不能省。gender只是VLM二元分类技术分组、不作社会groundtruth/全groupfairness；hardware具体gpu/precision/全部steps/solver/batch/timingSLO ND。2+1+2=5标准拟Only：有限同seed稳定/quality与语义相似分账新验证仍留，不因“已有diffusion原则”关闭，但不采globalstable或通用pruning无损保证，无必要Books新增。

- `16135 Motion-Adapter: A Diffusion Model Adapter for Text-to-Motion Generation of Compound Actions`，[v1](https://arxiv.org/html/2604.16135v1)实际III-A–C/Alg1/Eq1–2、IV-A/E/F/G/TII–IV/V。singleaction motion重构训练STConv joint-space/textcrossattention，thirdlayer归一>.9+两bodyjoint规则造结构mask，再逐action denoise覆盖bodyparts；22joint/196frames，root与lowerbody绑定，非真实physicalconstraint solver，mask重叠/顺序不证明任意compound可交换。2000ep/single2080Ti/b32/lr1e−4是adapter训练；“无额外training”只backbonefrozen，不能写全系统trainingfree。mask t750/250窗口启停平衡结构与fusion，attentioncollapse归因不是受控证明全部compositional失败。484prompt upper22×lower22、GT机械拼接明确无协调保证；2652syntheticcompound含这484、evaluator80/10/10重训，benchmark与评估train分割是否disjoint未明确，不称独立real-motiontruth。20repeat95CI披露须保，65participant每任务15video/method无全部humanCI；TII MotionDiffusebaseFID4.733更低但Rprecision较差、adapterMDM3.592更低而MotionDiffuse3.719，不能概括每backbone所有指标better。Diversity/Transition目标接近GT不是数值一味升降；TIV maskingstep-ablation MotionDiffuseTransition1.416比full1.381更接近GT1.872，不采文字“allmetricdecline”。precision/fullinferencebatch/NFE/每action额外forward/latencySLO ND；coarse upper/lower不能hands/fingers，baselinecapacity仍限。2+2+2=6标准拟Only：保structuralmask与latefusion共存边界，不为局部运动动画制造已验证物理可靠性或Books新增。

- `16146 On the Rejection Criterion for Proxy-based Test-time Alignment`，[v1](https://arxiv.org/html/2604.16146v1)实际§2/P1/§3/§4–4.1/T1/Limitations。draft~p、tokenconditional Bernoulli reject后q*重采的图模型，可表nudging/KAD；implicitreward s∝p q*/q的等价只在存在同α使全token q*α≤s≤p+q*α条件，作者给反例，不采无条件统一。conservative confidence bet比较p_v与maxq*−λ；不同checkpoint probability不独校准为correctness，语言多种合理续写使低单token概率不等知识不足，q*也可更差。OLMo1/13B与Qwen1.7/14B、5集/T.7、dev调margin{0,.1,.2}，Qwencommonsense输dualKAD，λ0CSQA74.7<base76.9，不采所有条件超两buildingblocks或可靠性保证。OLMoP*74.1 vs34.1为40pp，正文37.4；Qwen正文71.4/80.2与表74.1/82.3不合，不用旧headline gap作量化归因。没有把Qwen作者误称closedsource沿用；hardware/precision/maxlength/batch/双模型e2e/seedCI/SLO ND。2+1+2=5标准拟Only：新条件等价/threshold相对proxy的受限设计证据保留，不自动签安全alignment/普适更优，暂不需Books正文。

本五officialabs actual轻核：16060onlyv1；16056v2Aug3、16079v2Apr21、16135v2May3、16146v2Apr20 07:53Z，但未给决定处置revisioncomments。未扩版本diff；累计95唯一event轻核，只版本/身份不代替联合firstpublic。全部待有限非作者处置，普通余下必要审阅继续，formal分母未冻结。

### 恢复后：mask奖励、稀疏适配、readout归因及有限候选覆盖

再次实际重读AGENTS、当前三合同、Prompt、ROADMAP和月最新checkpoint。LogicLoc已由root实际正文与相邻顺读写后通过，正式日报最小同步为41工作家族=18真实I/5E/16Only/2D，未冻结/未日Gate。Ch76 Review最小状态同步，body与Apr24新段不改。上一16135反证的“MotionDiffuse baseFID4.733更低”只可指相对MDM base8.019，不能指优于自己的adapter3.719；adapterMDM3.592亦低于4.733，本处明确比较分母，不采所有指标普遍改善。

- `16158 AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency`，[exact v1](https://arxiv.org/html/2604.16158v1)实际§3.1–3.4/Eq1–5、§4/Table1及§5–6；关键公式另开官方HTML MathML验证。CoT限定additive mask、c=−.4、200步AdamW/lr1e−3/β.6,.9999/wd.05、clamp≤0再×10，仅mask可训练，teacher-forced correct-answer CE后附加GRPO outcome0/−1。**中央reward语义窄争议**：Eq3用H/c，未重新启用且H=c时给1，完全重新启用H=0时给0；在Eq4–5最大化正reward时并不等于文字所称“更强re-enabled贡献更高”，缺互补/符号说明。§3.2称all-zero mask给zero CE，除非correct-answer概率1否则不成立；§3.1若T是0/1下三角，H∘T将未来logit归零而非−∞，softmax仍可非零；只隔离印刷式保证，不断言实际实现真的泄漏，标准causal mask可能另有执行。8epoch/8rollouts/max1024/b8/mini2/two gradientpasses/lr1e−6/ε.2、48A100、Llama3.2-3B/GSM与MMLU各1000题/pass4；mask200pass额外成本不能被token下降隐藏。GSM186.6→104.4 tokens、pass4 90→89.6，MMLU240→129.5/78.5→78.6支持有限compression，不证明唯一saliency因果、真faithfulness或无损质量；spaCy类别不是内部过程真值。作者§6明确faithfulness尚待专门验证、可能损selfcorrection。precision/总训练计算/latency/seedCI/SLO ND。2+1+3=6纠错深入拟窄D：保所有这些方法/局部结果，仅不采用reward所述causal-faithfulness保证；重开只需Eq3实际reward方向/互补与causal/zero-CE解释及相应有限检查，非全复现。

- `16171 JumpLoRA: Sparse Adapters for Continual Learning in Large Language Models`，[v1](https://arxiv.org/html/2604.16171v1)实际§3/Algorithm1、§4.1–4.6/Table1–3及必要A.2。dense低秩AB经signed JumpReLU |AB|>τ后合入sharedbase，再丢本任务adapter；新τ和STE ε.001学习是weight-update support分支，不是冻结A/B参数或任务路由。B0导致正threshold阻断，先20%steps warm start全AB、initτ按A+B参数数目、80%到γ=1；full AB构造/阈值后matrix不必低秩，不能将推理低秩与训练省内存混同。T5encoder-decoder770M、SC4/LS15分类任务、6顺序/3seed42–44、单ep/task b32/r8/α32/qv、8H200/Transformers4.57.6/PEFT.18.1；不因规模或分类拒准入。ELLA λ A.2主表默认、长序列global ablation grid每task按当前与旧task validation调，非全部固定预算配置。SC ACC78.23→78.85但BWT−.5→−1.9更差，LS−4.8→−4.5较好；global/local及sparse/interpolated排序随序列反转，Jaccard .012/.065与中层sparsity不是功能独立/zero interference证明。precision/seq与dense计算总峰/训练时间/seed方差/SLO ND。2+1+2=5标准拟Only：保可学习weight-support及warm-start/遗忘反证，有限任务序列不支持新普遍no-forgetting保证或必须Books更新。

- `16197 Sketching the Readout of Large Language Models for Scalable Data Attribution and Valuation`，[v1](https://arxiv.org/html/2604.16197v1)实际§2.2–2.5/Algorithms1–2、§3.1–3.3/Tables2–4及必要D.1–D.4/E/F testbed。LM-head CE r⊗h的RH/GH双kernel、topmass稀疏residual与factor CountSketch使forward-only index可行；gradientenergy热点不证明所有pair因果ranking，GH semantic toy不是语义truth。AppendD明确head restriction/truncation是structural/deterministic bias、token-level分析无factor normalization；实际Alg2 factor L2+E normalize_sample最终norm是非线性，不能传递无偏与完整gradient influence保证，norm还需处理zero sketch。**窄理论争议**：官方MathML D.2原文Var⟨CS(x),CS(y)⟩≤||x||²||y||²/K漏reversed-pair交叉项。取x=y=(1,1,1)、K=1、三个独立公平sign（一bucket满足其碰撞条件），Z=(s1+s2+s3)²在1/4概率为9、3/4为1，EZ=3、VarZ=12>9。故该constant-1 bound及依赖它的D.3 exact上界不能直接采用；不是否定CountSketch无偏或所有O(1/K)规模。主文10–15×方差改善也不能从未计1/Kr、1/Kh和normalized实际target外推为普遍优势；重开只需保交叉项的修正bound、matched完整feature维度与实际norm/target明确，非全部数据/训练复现。
  finite支持仍保：N5000/100queries，Pythia1B RISE6.7GB高于TrackStar3.6GB，17.6ms对590ms与OLMo32B72.8GB/64.4ms对76.7GB/3.7s是给定配置；1M池label依howdy字符串，P@10 5.9%vs3.0%非真实因果真值。μ±δ为Recall/Predict均值与不平衡而非CI；FinMed/RapidIn和TrackStar局部强于RISE，不能沿“所有task胜”。50kBrainRot由32Bscore200queries选5k、Pythia1B20ep/lr5e−5/b8closedloop，purity87.6%、controlPPL2.33、RULER4.10%有有限有效性但ARC26.62<base26.88，不全部能力提升。E seq512/seed42/ρ.92/min4/cap256、λRH.7/GH1、TrackStarbf16，F为8H200141GB或1GH20096GB两testbed；各row未绑定哪套/总index/querybatch/precision完整口径与CI/SLO ND。2+2+2=6纠错深入拟窄D，仅隔离上述unbiased/full-causal/印刷variance guarantee，保具体实现与规模证据；不写Books。

- `16211 NVBench: A Benchmark for Speech Synthesis with Non-Verbal Vocalizations`，[exact-v1](https://arxiv.org/html/2604.16211v1)实际标题/§2.3–2.4、§4.1–4.5/Table3–6及§5–6，正式题不沿当前v3改题NVV-SuperBench。约80EN/30ZH人类seed经三annotatormajority+第四adjudicator；Gemini2.5Pro text-only扩45types×50×2=4500，经schema/人工一致性筛，非4500真实audio truth。prompt vs tag接口范围不同，coverage=supportedtypes/45，不是实际event成功率。GT-conditioned verifier知道targettype与unchanged transcript，插唯一marker并允许spurious types；precision/recall绑定该条件，不是blind全inventory检测；NTD只TP样本，不能被当所有event时间误差。三次objective synth，human/LLM只一次；450/语言样本、97raters、Likert含0failure。ASR/WER可惩罚长笑而自然度仍高；ElevenLabs NVV对neutral CMOS EN+.65/+.59/+.93而GeminiPro−.24/−.18/+.05，说明通道/lexical质量与控制分账，非必然牺牲quality。Gemini还参与seed/generation/verifier/judge，同一evaluator多角色非独立真值。15系统未matchedmodel/trainingbudget/inventory/voice，coveragecorrectness/placement/salience分账的有限协议可保，但不采用all-system公平因果排名、LLMjudge fully validated或低SNR失败唯一架构cause。HW/precision/latency/seq/batch/SLO与统计口径完整CI ND，±不是自动CI。2+2+2=6标准拟Only：局部multi-axis benchmark新增反例保留，不把TTS质量sensor当控制成功/未知type guarantee或制造新Books机制。

- `16217 Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations`，[v1](https://arxiv.org/html/2604.16217v1)实际§3.1–3.4/§4.1–4.2/T1–4与必要AppendA–D；正式官方MathML核C Eq24–28。question/nullcontext逐层realized-token NLL差LI（非Shannon真entropy/auxfamilyoptimal估计）经pool minmax含ε，按answerunit均LI+frequency各.5，fixedscore beforecalibration；answeradmissibility由MC exact或semanticproxy，不是无条件truth。samecandidatepool与wrapper控制有效，whitebox五模型3–14B、M20/50/10、T1/p.9、MCmax1/open36、cal/test.5/100splittrials、single-domain.35，crossdomainsubjectshift非exchangeability保证；作者§5明确新贡献empiricalscore而非新shift theorem。Table3 CoQA QwenEMR.226>.223、SSM.340>.338，Llama同向小反退；VicunaSSM.221>.218，不采所有指标dominance。100randomsplit不是独立训练seed/hardwareCI；HW/precision/完整两上下文逐层score计算成本/batch/SLO ND。
  **中央有限candidate coverage窄争议**：C将s=∞（candidatepool无admissible）且q=∞时的s≤q，误等价于存在正确候选。合法反例N=1、所有exchangeable样本的sampler永不生成正确答案、α=.5；A的经验floor=N/(N+1)=.5因此也满足α≥floor，q第一orderstatistic=∞，C包含全错误candidate但intersection仍空，实际coverage0<1−α=.5。A真实“missingcandidate不可threshold修复”的下界有效；不能由∞sentinel rank event转为coverage事件，也不据此否定有限表/LI排序。2+1+3=6纠错深入拟窄D：只不采C无条件coverage保证与其向shift外推；重开仅需q=∞的可核处理（fallback/拒答如何改变coverage定义）、全候选存在条件或包含sampling failure的正确risk theorem，非全模型复现/所有附录。

本五officialabs已actual轻核：16158/16217仅v1，16171v2Apr21/v3Apr28、16197v2July19、16211v2Apr21/v3June14改题，均未提供决定处置revisioncomment。未为版本号扩全diff，exact-v1标题固定；累计100唯一事件轻核，不代替联合firstpublic。五必要source作者审阅完成，待有限非作者；普通六项部分证据与身份/日期收口继续，formal未冻结。

### 最后普通六项与两个具体身份/综合证据收口

root六项有限原文独立核已实际读`V3_ROOT_FINITE_INDEPENDENT.md`，16146/16158/16171/16197/16211/16217窄处置通过；apr02最新五项实际读`V3_APR02_LATEST_FIVE_16022_16044_INDEPENDENT.md`，两Only/Ch11窄Existing/16044窄D和STOP写前通过。STOP真实Ch20:232/234及Review491已由root实际顺读相邻写后PASS，证据保存在`V3_STOP_OWNER_PROPOSAL.md`末；可计I19，未签日级Gate。无活跃共享锁。

以下六项复用上面实际§3–§7等必要原文，不再重读未变全附件；完成作者处置，交有限非作者核：

- `15648 HyperGVL`，2+2+2=6标准，仅报告。相同hypergraph problem的表示改变及higher-order信息在pairwise图中丢失的有限比较，改变“任选等价编码都同样可解”的选择；adaptive router也只是给定representation/task支持内预测，不保证任意图、题或机器人规划。保2400×35、12VLM、非严格LM/VLM配对与routing条件；不恢复protein任务，不将该benchmark当全球知觉真值。局部representation operating point可报告，但未形成新Books主干机制。
- `15657 CovAgent`，2+1+2=5标准，仅报告。coverage ceiling与可解决的reasoning frontier分离，使低coverage诊断不能直接变自动waiver或LLM能力失败；这是受限定的评价边界，不只是新硬件场景。保19design/同GPT5.2/.4/3runs、token总成本与复杂pipeline仍失败；组合对照不能分离tool/context组件因果，38/35单位不补造。它不新增可批准修复的可靠性保证，不需要为RTL任务另写Books。
- `15794 SDFT recovery`，2+1+2=5标准，仅报告。受损checkpoint的off-policy bootstrap→on-policy自蒸馏是条件替代路径，teacher专业知识可能改变任务能力而非只恢复损伤；pruning后Tooluse提升而MMLU净−2.55、CKA排序不等质量保留。§6明示correlation非causation，不用摘要强句宣称manifold必要原因；训练预算/quant适配混杂限定。只保有限恢复设计与失败边界，不为一般蒸馏原则追加Books。
- `15802 CHOP: Chunkwise Context-Preserving Framework for RAG on Multi Documents`，2+1+2=5标准，仅报告。adjacent contextual difference决定CNM prefix继承或重新提取，是给定多文档条件下降低重提取的局部分支；Gemma12B/embedding3large/Chroma、top1 retrieval改善而generation F1未全改善，top10差距收敛，直接限制检索提升向回答质量传递。没有prefix/CD独立消融或完整成本，不声称消除hallucination或唯一组件cause；不能把主题RAG相似签为整套Existing，不另写Books。
- `15871 UniEditBench`，2+1+2=5标准，仅报告。source/target/prompt triplets对齐两类编辑接口与多维judge协议是可核的比较有效性条件，不只凭新taxonomy准入；710=633image+77video。保distilled8B stroke误差反退、50human分组与five-pass文字歧义、judge训练/测试隔离ND，缺披露不据此断言泄漏。低成本judge不是人类真值或所有范式公平保证；有限协议尚不要求长期正文新机制。
- `15972 WORC`，2+1+2=5标准，仅报告。swarm优化标签→meta预测角色权重→按低权重重采quota提供条件化资源分配分支，但weight不是因果weakness或导数、重复上下文不独立。保同额外四次discussion局部对照与非tokenmatch、额外0.78–1.92×compute、跨表口径不合及cost单位ND；不从混合acc/F1平均断言统一accuracy。只有局部有限资源分配证据，不新写普遍弱链定律/Books。

- `16009 MEDLEY-BENCH: Scale Buys Evaluation but Not Control in AI Metacognition`，[official exact-v1](https://arxiv.org/html/2604.16009v1)，正式题按实际PDFp1与HTMLv1，非Aug7 v2改题。实际§2.1–2.6/§3.6/§5.1–5.6及必要AppendD/E/I/J：35models/12families、130cases五域，其中100无唯一GT、30knownanswer，模型生成vignettes/28analystpool选8、三judge650claims中43/14instances改direction。A独立→B-Private显式自检→B-Social各自isolated context但Social收到A而非Private输出，private/social差是两个条件的差，不是同一轨迹逐次更新因果。T1正常Brier相对soft consensus pseudoGT、T2正确性也是judge验证，不是外部真值；MAS与ipsative每instance十维去均值只能说明此rubric中的相对weakest，不证明全部LLM绝对evaluation deficit。PC1解释80%、judge stylebias/analystoverlap、Gemma3N128/130格式失败、T0/OpenRouter/8000–20000 max/March29–Apr3采样都保留。scale各代model/训练预算并未matched，Gemma4评价62.3低于前27B72.9，不能采monotonic或parameter-onlycause。progressive11为purposive非iid，30题反转summary confidence、50题减到两个弱analyst，r−.82/p.002/Bonferroni.020及leave-one-out是受限关联，非两种内部架构机制识别。§5.6确实1000bootstrap/selectedCI，不能称所有不确定性ND或当多次训练seed。
  早期记录“social-summary rendering待v1.5修复”未在本次exact-v1、官方README和定点prompt历史找到对应原始发布说明；不把这句旧线索冒作已核bug/重要修订事实。实际原作者[README](https://github.com/ki-smile/medley-bench)为package0.5beta/data1.0；[Apr16 commit](https://github.com/ki-smile/medley-bench/commit/9a7285e20bd68f458f5246142f2d9abc70c1c34f)的消息Update version1.0，定点social prompt现有build同时mask analyst与consensus，不证明收集时已渲染每一实际字段；snapshot调用/输入未核，不声称代码复现。只在该线索确有原始修复/输入材料返回时重开受影响Social命题，不否定有限协议/表。2+2+2=6标准拟Only：公开的多条件行为比较与relative/absolute区别值得报告，但不升级rubric到内部metacognitive truth、自动train因果或Book新增。

- `15367 SoK: Security of Autonomous LLM Agents in Agentic Commerce`，[exact-v1](https://arxiv.org/html/2604.15367v1)实际§III A–F/§IV B/§V B–D/TableI/III/IV。23查询/1373records→1237去重、37database+105targeted corpus，30row blind set只有17完整双coder的κ.850/.833/.871是label一致而非attack/defense验证；12vectors多数借已知证据、部分speculative，仍保direct/derived区别，不凭SoK或领域窄拒绝。定点发现实际协议能力误归属：§II-B2、IV-B2、V-A2、TableIV和V-D Layer3把ERC-8004称wallet transfer/spendingcaps/onchainguardrails。实际[官方规范](https://eips.ethereum.org/EIPS/eip-8004)及[Jan25、Apr19前最新该文件commit的精确稿](https://raw.githubusercontent.com/ethereum/ERCs/503591a6e80e6e1affdd6403341e25269141f046/ERCS/erc-8004.md)的Abstract/Motivation/Specification定义Identity/Reputation/Validation三个registry，并明确payments orthogonal/notcovered。该历史稿通过官方API仅取目标文件untilApr19的一项commit，非以当前规范直接反推历史；wallet association/身份可转移不等授权资金transfer/cumulativecaps。
  2+2+2=6，因具体保护行为/规范保证纠错定点深入拟窄D：不采用其ERC-8004付款授权/限额能力与依赖该能力的coverage行，不能由这条误归属推所有12vector、custody隔离或MPP/AP2均无效。其工具改交易参数vs改reasoning、prompt-to-key与cognition/custody分离、累积暴露的合理综合仍保为受限证据，但成熟分类本身不强写Books。重开只需作者所依据精确ERC版本/扩展guardrail实现、与registry分开的custody机制及修正TableIV/Layer3责任，不要求全部引用或金融attack复现。

- `15483 π0.7: a Steerable Model with Emergent Capabilities`具体contextconditioning/subgoal与success-failure支持有潜在贡献，不能因机器人或generic端到端框架关闭。官方exact-v1题摘/方法入口已核；Submitted Apr16不是公开证明。官方blog`https://www.pi.website/blog/pi07`的原始搜索提取显示Published April16及同题paper，但直开web403、curl为Vercel Security Checkpoint，不冒作正文实读。当前保早发同family/日期隔离，不进入确定Apr20候选，不以提交或索引独证时间。可接受恢复是该官方blog原始Published字段与同一paper链接/正文的可核快照或精确官方首次公开公告；取得后只重开真实归属日，不为此扩扫PI每周目录。此项不是待普通全文，也不阻塞其余确定家族。

以上仅指该小批的普通方法工作完成，不是整日普通工作已到末端。旧25身份与125恢复题摘合并核对为150唯一题摘后发现，旧25中除已处理15357/15368、具体暂缓范围关闭15671及另交有限核的15877外，以下21项缺当前合同的具体贡献/必要证据裁决。已撤回整日作者工作到末端的声明；正式55家族和I19的有效证据保持，最终分母未冻结。未stage/commit/push、未改LS或月checkpoint。

### 旧25缺具体理由的定点恢复（21项普通工作，不回扫447）

已重新读下列21项完整原始题摘，并轻量打开当前官方abs事件页；不是沿用旧selected，也不因旧列表存在自动送Deep。15522、15702、15771、15774、15804存在后续版本，但所见页面未给决定处置的修订说明，不为版本号扩全版比较。15379/Fleet、15499/secure、15409/FP16均按实际命题而非名称定深度。本窗首公开仍用本日实际窄公告链，Submitted不单独计公开。下列是值得核验的最小潜在增量及原有选择，不是已证实采用：

- 15356：在缓存按独立vector量化时，顺序状态与token分布的条件熵可能改变压缩下界；需核其条件是否支持可随机访问的低成本解码及跨会话“语义”等价，而非只重述数据处理不等式。
- 15379：partitioned L2下，flat block scheduling破坏共享weight tile局部性；三级task scope与完成事件合并可能改变调度/同步选择，需计controller占用及低batch反例。
- 15409：cache ON/OFF的数学等价未必意味着FP16执行等价；三模型的精度干预、逐层漂移与patch能否支持唯一因果及flip定位，需要保相同prompt/解码条件和有限范围。
- 15464：TPU的DMA/packing与动态ragged batch不兼容时，query reshape、KV布局/更新融合及分布感知编译改变实际kernel计划；需核重编译/quant与端到端成本，而非只保局部加速数字。
- 15499：加密输入不能直接供明文动态模型router使用；安全router与不同容量expert联合训练/选择可能提供新成本分支，需核威胁模型、选择可见性和完整协议代价。
- 15522：训练负载的高频/低频功率变化有不同电网约束；被动filter与主动储能/寿命控制分工可能允许不干预训练的替代路径，需分实物试验、trace模拟和规模外推。
- 15621：固定retrieval深度增加noise/context成本；passage dropout listwise rank/filter与蒸馏可能把弱模型的noise收益转成强模型的成本优化，需分最终回答、selector成本与同深度基线，不预设所有模型都需adaptive retrieval。
- 15672：首个错误截断draft减少接受进度；SMC用importance-weighted粒子重采代替token级拒绝，以近似而非exact目标分布换固定vectorized验证，需核per-step误差bound如何联系整trajectory质量/完整成本，而非要求保exact才能准入。
- 15702：行为confidence与实际自监测能力可能不等价；battery中的受控错误发现/修正协议是否提供新的可测边界，需核外部任务成功与内部机制推断的距离。
- 15715：多模态tool-use评价中静态回答不能衡量交互动作的可行性；GTA2实际操作/环境反馈与error归因是否新增有效性条件，需核oracle、工具权限与重复条件。
- 15728：明文router暴露用户输入而朴素MPC成本高；PPRoute的MPC友好encoder、多步训练与unsorted Top-k可能改变加密路由的通信/质量取舍，需核O(1)所指通信round或总字节与威胁模型，不由安全标签推Deep。
- 15732：single-shot latency忽略回答错误后的重试；TTCA与long-context/language条件的accuracy-aware routing可能改变用户可见成本排序，需核正确性oracle、retry规则、router输入和完整wall-time，不冒作test-time参数更新。
- 15750：DLM固定block边界和当前step confidence不处理跨step影响与token冲突；DepCap的last-block influence与block内conflict-free选择改变两类解码决策，需核近似可加条件、目标分布/质量和完整验证成本，不是权限capability协议。
- 15771：post-retrieval failure未必来自证据不存在；hidden-state prober在两阶段gate、router选rewrite/decompose/focus/exit可能把query-evidence misalignment分型，需核prober标签/支持、stage/skill消融及停止/成本，而非把已有RAG加到新任务。
- 15774：记忆内容更新与retrieval命中可不同向变化；MemEvoBench的时序/冲突干预是否发现普通静态memory评价不能测到的失效条件。
- 15804：流式多模态的对齐与训练任务共享存在实时性/能力取舍；Qwen3.5-Omni首版报告实际架构与评价能否改变可交付机制，而非以模型规模/排行榜准入。
- 15840：固定RL任务分布不能随agent遗忘/不确定性变化；CoEvolve从rollout反馈引导task synthesis、经environment验证后更新训练数据，需核合成/验证成本、预算控制及是否超出单纯更多训练样本。
- 16004：单次ORM判断缺少外部事实支持且中间错误会传播；AgentV-RL将reward verifier变成forward/backward tool-augmented多轮过程，需核grounding权限、工具成本与bidirectional/训练消融，不是视频agent研究。
- 16007：prefill/decode对容量与带宽要求不同；MemExplorer联合heterogeneous SRAM/HBM/LPDDR/GDDR/HBF层级及NPU矩阵规模搜索，需核模拟器/功率预算、两phase匹配和H100基线口径，不是agent语义memory检索。
- 16067：VLA动作专家连续回归梯度可能破坏CE预训语义；AEGIS的静态VQA anchor、Wasserstein恢复梯度及逐层投影可能在不切断动作监督时保知识，需核anchor样本成本、双backward、forgetting/动作收益控制和方向保证，不是安全保护协议。
- 16145：混合精度改变计算/搬运瓶颈后，training-time predictor若显式纳入precision可能反转配置选择；需核预测输入、误差、适用hardware与真实训练成本，不能把点预测当tail-SLO。

这21项仍属可执行的普通必要审阅；现有55家族未变处置无需重读全附件。原始宽库存仅用于这次身份差集定位，不变成新的逐项队列。首六的exact-v1主体已取得，实际读取范围逐项在下文记录；其余按批推进，不等共享Books锁或无关peer。

#### 15356 顺序KV压缩：有效条件与打印metric分开

[official exact-v1](https://arxiv.org/html/2604.15356v1)实际读§2.3/3.1–3.4/4.2/5.1–5.2/6.3/7.1–7.3/9.6，关键公式直接核official MathML。2+1+3=6，因中央metric/lookup正确性争议定点Deep，拟窄暂缓，不采用其语义prefix等价或打印metric保证。定义d(s,s')=−log2P(LCP)的Remark1称ultrametric，但二符号各1/2的合法trie取s=a、s'=b、s''=a：d(a,a)=1、d(a,b)=d(b,a)=0，所印三角不等式要求1≤0，失败；其自行承认非零自距不修复该反例。§7.3称max d等价max P也因负对数方向相反；deepest exact ancestor是可用的精确prefix查找，不证明非同prefix语义复用。§4.2受κ^层数和embedding差约束的结论只覆盖共同位置/首分歧，不是后续任意近义prefix全state等价。

保留有效条件证据：固定权重/输入的确定性，额外可恢复token的injectivity条件下sigma-algebra相等与Shannon条件熵比较；不能将“任何trained embedding full-column-rank”和generic随机W概率1直接提升到任意训练权重。模型自身分布的平均熵与任意测试corpus perplexity不应直接写同一等式。条件熵小不自动降低实际高维residual方差，也不证明随机访问解码成本：预测常数平移不改变给定context的精确Shannon entropy；top-k平均F需候选forward，线性embedding近似不等全层非线性；§9.6明示residual实测/quantizer/kernel仍future。无实际model/hardware/runtime/质量/latency/CI/SLO benchmark，914000×是指定L/H/d与熵floor算术，不是可部署速度/容量保证；context越长更压缩还以H_i不增为条件。只隔离上述印刷metric及无条件实用/语义保证，非否定确定性/有条件熵或所有prefix cache。重开仅需修正metric与lookup方向、准确的状态可恢复/分布假设、实际decoder/残差和成本证据；不要求全引用/全模型附件，不写Books。待有限非作者核。

#### 15379 Fleet：task placement与局部/跨die完成责任

**后续状态：** Ch49 两段及 Review 已实际写入，root 源→实际 owner 与真实写后均 PASS，见 `V3_ROOT_FINITE_INDEPENDENT.md`；下文“正文未写”为写前审阅快照，不是当前待办。

[official exact-v1](https://arxiv.org/html/2604.15379v1)实际§3.1/4.1/5.1–5.3/6.1–6.4/Table4–5/8。2+2+2=6；当前Ch49:71–91有persistent executor、event-tensor lowering及per-SM/central queue取舍，但没有partitioned L2中的chiplet task/counter/fence分责，真实缺口触发必要Deep，不抬分。四层Wavefront/CU/Chiplet/Device task，编译时graph不可变、1scheduler/XCD、31workers/XCD。chiplet内按N分区/M-major让同weight tile的访问窗口重合，per-XCD局部完成计数后只有lastworker作L2writeback+GPU-scope事件；不将局部shared-cache原理外推任意HIP/CUDA memory-scope免fence。

单MI350X、8XCD×32CU/4MB L2、288GB HBM3、Qwen3-8B dense BF16、64input/1024output、batch1–64 decode-only TPOT（prefill排除）；vLLM0.17.2ROCm enforce-eager与AMD移植Mirage persistent为两不同对照。8scheduler占8/256CU=3.1%，短task控制成本可显著；低batch mtiles=1时无weight-sharing，SiLU fusion对CU-task也改善，不能将全部收益归于chiplet；bs32/64对Mirage1.27/1.30及HBMread .82/.63绑定该配置，Msplit bs64读1.20反增。正文Table4 bs32 L2 Mirage38.9/Fleet51.0，与摘要12→54不是同一证据口径，不沿摘要数替代表。本文输入graph手写不同代码、superoptimizationfuture；registerpressure限制occupancy，TP/prefill/多模型/NVIDIA均未实证，不称通用productionSLO。拟Ch49两段最小缺口采用，正文未写，需非作者源→actualowner/literal通过与root授锁，再真实写后核。

#### 15409 FP16：数值路径条件，不把patch失败当唯一cause证明

[official exact-v1](https://arxiv.org/html/2604.15409v1)实际§4.4/5.1–5.2/6.1–6.5/7.1–7.6。Llama2-7B/Mistral7Bv.3/Gemma2-2B、GSM8K700/seed42、五采样seed、greedy/topk/topp共31500runpairs；singleH100NVL95GB、PyTorch2.5.1/CUDA12.1/Transformers4.53.0、FP16/maxnew128、greedy确定性flags。同prompt cacheON/OFF sequence至少一token不同≠全部token都不同。Task acc很低源自己承认truncation/fewshot，8/9方向与Gemma greedy反向2.1>1.9只说明该协议executionpath bias，不是一般推理能力。McNemar/Bonferroni、bootstrap95%meanKL/deltaacc、BH层drift均有实际不确定性，不能说全部CI ND。600examples/32steps FP32 flip0和KL约2.5e−8是具体precision干预；不能将precision同时改变算子/累积路径后未见flip当成“FP16 non-associativity唯一cause”或任意FP32无漂移。架构间模型权重/训练不matched，GQA/head-dim相关不是architecture-only因果识别。

Residual patch在600highestKL/step0、32steps条件下median/mean常不恢复，§7.5明示不能据此排除其他机制，§7.6直接KVtensor patch仍future；故只保不等价现象与精度条件，不采用已定位唯一statecause、必须directKVpatch或任意架构都100%flip的普遍保证。2+2+2=6标准完成并实际有限owner比较，拟窄Existing `INFER-TENSORRT-LLM` Ch49:1608–1611“浮点执行语义还包含reduction order/activation approximation”：已要求precision、reductiontopology、kernel/activation、compiler/runtime、hardware共同绑定并重验，确定性与吞吐取舍具体覆盖本文可支持的数值合同，不是整套论文/架构因果Existing。无需制造正文新主干；待非作者必要源→实际窄owner核。

#### 15464 RPA：capacity shape与有效ragged分布是两种编译条件

**后续状态：** Ch49 两段及 Review 已实际写入，root 源→实际 owner 与真实写后均 PASS，见 `V3_ROOT_FINITE_INDEPENDENT.md`；下文“未写Books”为写前审阅快照。

[official exact-v1](https://arxiv.org/html/2604.15464v1)实际§3.1–3.7/Algorithm1、§4.1–4.4/5核心限制。用packing维让XLA选择最小tile，ragged维不置末两tiled维；Q的head-group reshape在MXU重复利用KV，K/V merge减少padding/DMA次数但FP8需unpack/repack。离线weightreshape不能保证中间HLO Layout Assignment不重排，当前仍在线preprocess；stridedKVload加oddstride缓bankconflict，页DMA与newKVupdate融合并await completion。静态VREG计算仍浪费：按decode/fixedchunkprefill/mixed各kernel specialization，动态有效DMA不等动态compute块；serve启动s/n最大capacity pad固定shape避免JIT落criticalpath，但相同s/n不同length分布仍最佳block不同。四block参数offline调/precompile，未实现mixed slidingwindow/reorder优化不能写已运行。

TPU7xIronwood两个TensorCore、192GB/7380GBps/2307BF16TFLOPS，Llama3-8B32Q/8KV、d128/256/BF16。decode128等长seq在d128 context≥8k/d256≥4k才bandwidth饱和，86%MBU不是任意短/混合请求；prefill单seq512–32k、d128 MFU按50%最大MXU利用调整分母，73%noncausal/63%causal不等整芯片峰值73%；preprocess2–8%在prefill不可省。KVupdate/DMA/FA消融证明这些配置的重叠，未给通用全部SLO。§4.4的v6e vLLM累计2–5×历史演进不隔离本kernel因果，更非本TPU7x相同全服务加速；源说Feb2025已有artifact，不把旧code事件重计本日新release。sequence/batch/hardware上述有披露，fullrequestSLO/CI/训练quality notapplicable或ND，不补造productionproof。

2+2+2=6，实际Ch49:1471–1498已有backend ABI/离散shape预编译，但缺capacity-envelope固定形状与有效分布tile浪费分责/packing布局不能跨HLO当然保留的具体边界，真实gap必要Deep，拟两段，未写Books；不把RPA与15408相似名字/recipe强dedup。

#### 15499 SecureRouter：MPC分支与打印协议正确性分开

[official exact-v1](https://arxiv.org/html/2604.15499v1)实际§2.1–2.2/3.1–3.4/4.1–4.3/Table1–4及必要AppendApool。semihonest/noncolluding两方、输入与模型secretshares、GumbelSoftmax task/loadbalance/empiricalMPCtime加权cost训练；tiny/base/large BERT4.4M/110M/340M改变encryptedinput的modelcapacity选择，不因非decoder小模型拒准入。Printed§3.3在线linear各party只计算e0W0+R0与e1W1+R1，若这是完整share线性步骤，两share相加缺e0W1/e1W0。ring上取e0=1/e1=0/W0=0/W1=1/R=0：打印和0，真实eW=1。这是所印步骤的有限正确性反例，不断言CrypTen代码实际没有securemul/Beaver，也不由此断言所有MPC或已发生明文泄漏。需作者明确此处是否仅示意，以及实际secure multiplication与oblivious选择后不同modelshape/timing的trace条件，不能由秘密index自动获得全路由/执行轨迹保密。

OfflineH100/XeonGold6526Y/32GB，online two localRTX3090/10Gbps simulated2PC；GLUE八任务metrics不同，CoLA59.10<63.35、STS89.02<90.36。Table1对fine-tunedBERTLarge平均1.53、Table2五task对SecFormer1.95不能相互代替；§4.3明示按router选择分布×各expert实测unit latency投影，不是整个testset全部endtoend重跑。router4.17s/1.86GB相对tiny4.11s/1.86GB不是零成本；RTE133.92/199.78包含该配置加权路由。Latency重复样本数和trainingbudget/precision/seq/batch/CI/SLO ND，不补造。2+2+2=6因实际印刷协议纠错定点Deep拟窄D，只隔离该完整协议/全confidentiality/真实全testset性能保证，保costawarecapacity分支/有限表，不写Books。重开仅需精确secure-mul/选择的原版协议或可核实现和其威胁/trace假设、实测路由全链成本；不要求全部GLUE复现或引用史。待有限非作者。

#### 15522 EasyRider：energy预算与功率波形不是同一控制量

**后续状态：** Ch70 两段及 Review 已实际写入，root 源→实际 owner 与真实写后均 PASS，见 `V3_ROOT_FINITE_INDEPENDENT.md`；下文“正文未写”为写前审阅快照。

[official exact-v1](https://arxiv.org/html/2604.15522v1)实际§3/4/5.3–5.4/6/7.1–7.4/8及必要B.2。高频LC filter、中低频双向converter+辅助储能、慢SoC反馈分责，所需Ebuffer=所补P差的时间积分而非只看peakW。短时平滑不改训练step/并行度，不等无限供能：必须在ratedpower、batterySoC/voltage/headroom、热与电流边界；软件offline只能在仍有headroom期间维持过滤，漂移会失去symmetricbuffer。outer active/idle target处理calendar-aging，inner每5s跟踪/限电流/平滑，实际实验仅inner；不从其“outer无需另验”推出寿命已测，也不采任意错误命令/任意时长全部安全。B.2正负current的不同η和piecewise dynamics仅作为作者所写controller，不将“QP/几次interval收敛”印刷句当已独立全局证明；Figure12约20min恢复SoC是具体实测。

400VDC/10kW实物prototype、25A thermal ceiling、74Ah/2.4C battery；低voltage不能交付满10kW。Cluster-scale frontier trace不可得，published normalizedtrace与2TitanX GPT-style125M训练自测/programmableDCload，不是MWdatacenter或当代rack全实测。演示β=.1ratedpower/sec、α1e−4/f≥2Hz是指定试验spec，不是通用电网规则。2GPU burn对照有41s warmup对齐、normalizedTDP、积分energy多19%，不等所有软件/UPS/DVFS策略都浪费；battery+converter损耗及mechanical/thermal、$3500prototype/$0.35W不可消失，GB200成本推算非部署价格。Precision/seq/batch/taskqualityCI未提供而此硬件powertrace结论不依赖LLM生成质量；不外推模型性能或生产SLO。

2+2+2=6；已实际读Ch70:250–286及power/accounting/actuator相关段：installedpower→placement/strandedcapacity已有，但没有“power waveform瞬态过滤与总energy/训练控制分离”的buffer和慢SoC责任，真实gap需必要Deep，拟Ch70仅两段；硬件操作不写implementationrecipe。该有限物理infra增量不以generic电气应用关闭，亦不把本文延伸为标准/电网法律指导。正文未写，先独立源→actualowner/literal。

#### 15621 AdaRankLLM：noise过滤与context成本随模型能力不同向

[official exact-v1](https://arxiv.org/html/2604.15621v1)，实际§III A–C/IV/TableII/V。完整正式题名Rethinking the Necessity of Adaptive Retrieval-Augmented Generation through the Lens of Adaptive Listwise Ranking。selector输出有序passage子集，并以[0]丢弃无用passage；不是原full-permutation ranker简单少读几篇。100k MSMARCO top20/truncate10先GPT3.5结构蒸馏，再GPT4 adaptive5k与20cluster ADA2k；Mistral7Bv.1学生三个epoch/lr5e−6/b64。ASQA EM/QAMPARI F1/ELI5 claim评估含七个不同backbone、Qwen3 think on/off八设置，perexample最佳k0–10是带标签oracle而非生产策略或全部方法理论cap。

TableII强Qwen3Think的Vanilla10 overall34.18高于Ada32.75、EM54.85>51；Llama3.1 rerank10 overall30.05>Ada29.74，不能概括恒优/全部学生等价teacher。受限结果支持弱模型因noise可能收益、强模型更多体现减少上下文成本的分支；没有识别内部thinking验证noise因果，亦未披露完整selector+generation token/latency matched成本、硬件/precision/CI/SLO，不把局部正确率变免费压缩。2+1+2=5标准拟Only：改变retrieval depth选择的局部反向边界值得保留，不将具体蒸馏recipe提升通用Books机制，不因已有retrieval主题直接关闭。待有限非作者。

#### 15672 SMC：粒子内状态与最终sequence commit不是exact-prefix接口

[official exact-v1](https://arxiv.org/html/2604.15672v1)，实际§3 Algorithm1/3.1 roofline/3.2 Theorem3.1/3.3/4及实际Ch48:844–868相邻。N粒子draft K，再target批量score加bonus，p/q权重与ESS重采复制高权重prefix，终点按归一权重只输出一个sequence；不是每轮经exact-token拒绝后立即提交prefix。§3.1 perdelivered TPS收益(K+1)/(ρK+1)没有额外N倍率，BN(K+1)≤R下“particles free”仅在指定memory-bound假设；越ridge转compute-bound。Theorem3.1 iid q、p≪q、EW4有限、χ²常数下单round期望mixedlaw误差O(1/N)，作者明说完整multi-round累计及重采祖先相关未证，不采finiteNexact或单round界变整轨迹准确率。

SGLang fork只复制Paged/Radix metadata/refcount而不复制KVtensor；O(sequence length) metadata非constant，Llama1B→8B/N8/K16特定72.3%KV减少不是allmodel peakmemory。singleH100SXM；Qwen SD0.5B、SMC3B对14B，最优draft比较不能唯一归因算法。isoaccuracy定义SD±3pp、maxspeed±10pp而frontier plots±15%target不同，不能统一称exact同质量；SSD额外1GPU，multiGPU perGPU TPS不同资源分母。实验precision/完整input-output/batch-concurrency/SLO/重复CI缺失不补造，rooflineFP16示例不替代实测配置。

2+2+2=6，真实Ch48已有asymmetric verifier和Cactus单step条件/最终law分账，但原缺population-resampling中的私有祖先/重采状态与终点commit分支。root 已完成 source→actualowner/literal 独立核；现于 Ch48 Cactus 后真实写入两段及 Review，并由 root 顺读相邻交接做非作者写后 PASS。保 classic exact verification 为不同可回退路线，不改经典保证；该项计本日实际整合，日级 Gate 仍待完成。

#### 15702 MMB：行为profile的阈值敏感与construct边界

[official exact-v1](https://arxiv.org/html/2604.15702v1)，实际§2.1–2.7/3.3–3.4/3.8–3.9/4.1–4.5。524items六域、20models/KaggleSDK，每item独立context且每model一次，无test-retest；T1–5预注册、T6 72 exploratory不可统称注册。KEEP/WITHDRAW/BET与Δ=P(withdraw|wrong)−P(withdraw|correct)可测错误辨别，T6全答/提示/decline的full/half/quarterpayoff是特定regulation assay，不是中立内部机制读出。

KEEP95/10、Δ15为operation convention，±5pp阈值改变9～10/20模型profile；α.54/split-half.51/SB.68，不推自然类型。d4.57 bootstrapCI[3.65,7.84]/10k对由Δ定义的组是描述，非独立construct验证。retro/pro r.17 FisherCI[−.29,.57]、n20检验power有限，未发现显著不证明两能力独立；meanwithdraw/accuracy r.16也不证明scale“inverted”普律。T4少错误分母、format/posttrain混杂保留，selectedCI不等训练多seed；hostprecision/maxbudget ND。2+1+2=5标准拟Only：受限选择与校准分母差异值得报告，不由自监测名称采内部metacognitive架构或通用模型排名，无需新Books。待有限非作者。

#### 15715 GTA-2：valid tool call、rubric root与外部任务结果分账

[official exact-v1](https://arxiv.org/html/2604.15715v1)，实际§3.3/Alg1/4.1–4.2/6.3–6.5/Table6–7/11–15。132workflows来自154raw，67augmented/62refined、仅3raw直接通过，工具14→37；真实需求seed不等原raw任务全部成立。最终artifact由GPT5.2对weighted leaf0–10聚合root，不读过程，中间工具无error的ToolSR与strict root>7不是同一成功；Kimi89.85Tool/8.33Root明示分母差。不同threshold选择依据discriminability而非外部必需条件，Claude从k6最高到k7接近最低不能称排行榜稳定自然属性。

Table7 30子集ClaudeSonnet4.5 Lagent→OpenClaw root0→50、50.1→136min、$10→35，score/cost .249→.195，不是免费或唯一harness组件因果；Manus/KortixmodelUnknown不能当matched模型。human30分层GPT5outputs/276leaf双annotator，rootPearson.966/ICC.928/MAE.744、leaf.863/.829/1.114；另一judge positivebias .46–.93，相关好不等无偏阈值真值。30反馈任务2.83→2.93coarse/3.15checkpoint不是全132的3.66，feedback与judge共享rubric也非独立sensor。80GBGPU具体型号/precision/seedCI/contamination完整ND；训练/前序日志不应补成effectoracle。2+2+2=6标准拟Only：保root/tool/evaluator与完整成本有效性边界，不把新任务条目强写Books或通用成功保证。待有限非作者。

#### 15728 PPRoute：constant-round不等constant-bytes，打印tie正确性隔离

[official exact-v1](https://arxiv.org/html/2604.15728v1)，实际§2.2/3.1–3.5/4.1–4.4/Table1–5，并直接核官方§3.3公式。user/router两方、semi-honest CrypTen，只是router encoder+selection保密，最终LLMprovider/完整delivery trace不因此获全链保证。MiniLML6v2 seq256用2ReLU/普通ReLU替代softmax/GELU，teacher encoder冻结+MLP训练→student routing/distill联合→freezeencoder调head；是近似不同架构，不采exact plaintextTransformer。打印2ReLU全nonpositive时分母0未写补救，不能断言实测已出现；penalty与trustregion“等价”不由任意β自动获得非凸全局对偶，不将此强作完整proof。

§3.3用严格>构造所有pair comparison，S列和以≥n−k选mask；未声明tie-break。合法全部V相同且0<k<n时C=0、S=0、mask全0，得到零候选而非k；仅反驳该完整打印top-k保证，不断言实际CrypTen代码必然同错或泄漏。n²并行比较减少round-depth而仍有bandwidth成本；Table4约9.985MB/52round、.2480±.0116s(十run mean±SD非CI)，byte反而高于bitonic1.23MB，即轮数/时间tradeoff非全部通信更少。ANN需ORAM条件，20GBps表头不补未知hardware/precision/SLO。Table1/2 endtoendrouter秒级加速绑定naiveMPC，仍不含最终LLM生成；CSCR AUDC .539→.538/QNC44.4→45.3/Peak.568→.564、UniRoute Embed .515→.5036/QNC60.21→64不都持平。

2+2+2=6；仅打印exact-topk/全输入可定义和依赖该保证的路由采用定点correctnessDeep拟窄D，保MPC-friendly encoder/training及有限表，不普遍否定privacy/MPC。安全标签不是触发理由，实际tie反例才是。重开仅需精确tie/public-index或fallback协议、零denominator定义及实际可核实现/选择影响；按需要修正round-vs-byte和完整delivery威胁范围，不要求全部dataset或附件复现。待有限非作者，不写Books。

#### 15732 LAAR：TTCA oracle与生产router overhead分开

[official exact-v1](https://arxiv.org/html/2604.15732v1)，实际§3.1–3.2/4/5.1–5.4/6.1–6.2/7。SCBench UUIDKV100题50fit/50heldout，EN/JA/ZH×4–64k，五instances Granite3.1-2/8B/Phi3mini/medium/Swallow8B；vLLM.16/A10080GB/10Gbps/concurrency8/T0。TTCA加和所有尝试到firstcorrect依赖exact-match taskoracle，R10全失败为rightcensored而非成功平均或生产可直接测量。Q(lang,lengthbucket) logistic prior、L=c(m)(T+αqueue)/Q、α.7固定；不同模型失败避免而非stationaryiid retry，L/Q不保证全路径最优，c为秒/generatedtoken且作用inputbucket也只是经验近似。

§6 router-ms overhead未计TTCA，不从复杂score宣称净无成本；LAAR首答成功率可更低但retryTTCA更好，64k有全model不能解。prefixaffinity与quality/diversity可能相冲，五模型/关键值任务不证明一般QA/所有context；无fulltail/SLO/precision/重复CI披露，不把oraclecorrectness转内部confidence或testtime参数更新。2+2+2=6标准拟Only：limited错误重试总成本指标与能力prior取舍值得保，不将经验metric升一般online routing保证，无需新Books。待有限非作者。

#### 15750 DepCap：跨步块边界信号与“无冲突集合”打印算法分开

[official exact-v1](https://arxiv.org/html/2604.15750v1)，实际§4.2–4.4/Algorithm1、§5.1–5.4/Table1及必要local-overlap分析。先前块解码前后同一未来位置的预测分布KL，与当前熵合成窗口归一分数决定下一块停止点；首块仍用保守最小长度。块内用置信筛候选，并以两位置对对方预测token的交叉log-prob之和高于γ为冲突；这些是条件化DLM推理信号，不是任意模型的真实语义依赖、互信息逐样本等价或输出分布exactness。§4.4的可加性还依赖局部overlap小，不应把期望互信息解释扩成无条件逐token加法。

中央印刷correctness问题可直接由§4.3与Algorithm1第7–8、10–17行构造：第7行一次将所有`c_i≥τ_high`放进集合S，第8行只从尚未选择的C删S及与S冲突的点，并不检查S内部是否互相冲突；后续贪心也只处理C。取两个候选预测同一token，彼此赋该token概率.96且`τ_high=.95`、`γ=-16`，则两点置信均达门槛，`D_ij=2log(.96)≈-.0816>-16`按原规则互相冲突，却都留在S并被返回。这里反驳印刷算法的“safe/conflict-free subset”普遍保证，不断言公开实现必然同错或真实任务必然出现该pair；需要作者说明高置信种子内部消冲突/实现差异或限定不能同时触发的条件。§5单A10040GB、lm-eval、LLaDA/Dream的固定bench和TPS/NFE/accuracy仍是受限观察，Table1有质量/吞吐相反格，不能将up-to5.63×当全部模型、任务或生产SLO；precision、并发、CI未完整披露。

2+1+3=6，因明确中央无冲突保证反例定点深入，拟窄D：隔离Algorithm1与其声称的无冲突提交保证，保留DepGA跨步条件信号及已报告表，不重演全部基准。Ch24/48不因主题相似判Existing或写Books；重开仅需修正种子集合选择/可核实现、γ与高置信相互冲突的处理及受影响质量安全结论。待有限非作者。

#### 16067 AEGIS：稳定化投影与精确正交印刷保证分开

[official exact-v1](https://arxiv.org/html/2604.16067v1)，实际§3.2/§4.1–4.3/Eqs5–14/Algorithm1、§5.1–5.3、§6.1–6.6/Table1/§7。PaliGemma2-3B-Mix-224的冻结SigLIP/可训Gemma+projector接四层cross-attention flow expert；先用3000 VQA样本建立各层Gaussian activation anchor，再在LIBERO action数据训练时双backward分取flow-matching任务梯度和W2 anchor-restoration梯度，层级点积为负时删去冲突投影。这是有限“无回放参考任务数据”的替代分支，不等anchor统计捕获全部VQA能力或最优策略保证。§5的VQA CE定期检查和5k OK-VQA在1500步后比较：原基线60.15、AEGIS60.23、naive57.36、stop-gradient+FAST59.61、LoRA59.32；没有可替代封闭环机器人success的证明。AEGIS多第二次backward、§7约40% wallclock代价；不同基线actionhead/learning-rate条件不完全同一干预，0.08点VQA差没有充分统计归因。

中央数学限定：Eq12与Algorithm1实际`α=d/(||g_ot||²+ε)`且ε>0，Eq13的`g_final=g_task−αg_ot`。因此当`d<0`，真实点积为`d−d||g_ot||²/(||g_ot||²+ε)=dε/(||g_ot||²+ε)<0`，并非Eq14/§4.3所称严格等于0；后续精确Pythagoras能量等式也不能无条件按该打印公式推得。此是原文精确保证的有限反例，数值残差可很小且不抹除表中观察，不断言有实测VQA泄漏由此唯一造成。2+1+3=6、纠错定点深入拟窄D：仅隔离精确正交/零破坏分量与依赖其的严格知识保存保证，保留有限anchor-gradient方法、OK-VQA与expert MSE分账及训练成本。重开仅需ε修正后正确不等式/零范数分支、实际实现对应公式和该几何保证的受控证据；不要求全部VLA任务复现。待有限非作者。

#### 15771 Skill-RAG：失败诊断是路由输入，不是证据真值

[official exact-v1](https://arxiv.org/html/2604.15771v1)，实际§3.1–3.3、§4.1–4.4/Table1/Fig2及Limitations。失败prober对hidden states作二分类，标签由答案与gold比对而得；router另消费失败推理、答案和检索证据，选择rewrite/decompose/focus/exit等skill，最多有限轮。探针能读出与当前标注相关的状态，不直接证明哪篇证据充分、内部知识真假或失败类别为稳定因果实体；Fig2的t-SNE簇是后验可视化，非消融。单Gemma2-9B、BM25、Hotpot/NQ/Trivia各3k train/500dev、MuSiQue/2Wiki各500 OOD、统一4-shot；Table1相对Probing-RAG OOD ACC分别13.9→20.0、38.9→52.5，但Hotpot EM24.2低于DRAGIN35.6，域内NQ ACC49.7、Trivia65.9也不能说全部方案/指标胜。固定技能词表、单backbone与router prompt敏感，分支计算、硬件/precision、训练seed/CI和生产tail未披露。2+1+2=5标准拟Only：失败条件到有限操作路由的局部改善可报告，不能由prober/readout或未分离的skill+feedback组合写成新RAG真实性控制保证。实际Ch76已有relevance→sufficiency→requery/decompose/abstain的owner分责；本文未提供足以替换该正文的新的授权/证据提交机制，也不把主题相近偷换为整篇Existing。待有限非作者。

#### 15774 MemEvoBench：跨轮反馈与记忆更改工具的效果不等同

[official exact-v1](https://arxiv.org/html/2604.15774v1)，实际§3.1–3.4/§4.1–4.4/Tables1–3、§5–6。QA108（七领域、36 risk types各3）与workflow83（20环境、八risk types）的三轮评估每轮追加agent回答为下轮可检索memory；bias feedback由模拟LLM赞许风险捷径、惩罚保守行为。原vanilla两风格/多模型ASR平均75.9→75.2→80.1，并非无反馈也逐轮单调恶化；加bias后71.6→84.9→87.8，只证明该构造feedback下更易被污染。QA的+ModTool配置还包含`web_search`和`correct_memory`，workflow只含`correct_memory`，不能把跨任务改善全归因于memory edit单一工具。SafePrompt的QA与workflow反向、A-MEM对三模型的不同效果都要求具体配置分账；GPT5.2 judge对50手标样本约96.2%只校其局部标签一致，不是unsafe downstream effect或真实高风险发生率。模型/任务、模拟反馈、round append policy绑定结论；训练seed/完整成本、并发与生产环境未证明。2+2+2=6标准拟窄Existing：Ch77现有§“失败经验...”及反馈写入/源episode可追溯、跨用户作用域命题已明确反馈不获事实或policy authority，本文补受限跨轮反例但不推翻该责任链；不将synthetic task/risk taxonomy写成一般Memory安全保证。待有限非作者实际对读Ch77具体段。

#### 16145 Training Time Prediction：precision-aware单步代价而非训练总工期

[official exact-v1](https://arxiv.org/html/2604.16145v1)，实际§II/§III–IV/Fig2、脚注1及结论。torch.fx分割图、torch.amp hook找op实际dtype，再按目标shape/精度profile算子forward/backward并把DP/TP通信与PP bubble代入代价模型；不是只由静态FLOP无测预测。脚注明确`training time`是**single iteration time**，不能乘一个不明步数就得到收敛到质量目标的job ETA。仅Llama3.1-8B/C4、8×H100 NVLink、FP32/FP16/mixed及受测DP/TP/PP，Fig2 mixed平均MAPE9.8%、未见FP16 10.64%；baseline固定FP32导致的约130/147%差异并非与全部precision-aware对手同信息预算比较。目标硬件op profile成本、PP microbatch/overlap简化、网络跨节点与质量/收敛变化不在这次误差内；精确模型训练任务SLO/CI/成本ND。2+1+2=5标准拟Only：precision×图算子测量的局部planning proxy可保，不把小测试的单步误差升级跨配置总作业耗时或通用最优并行策略。Ch36已有按model shape、precision、资源与step critical path profile/漂移回退的命题，本文未提供跨边界的新控制责任或校验机制，故无必要Books新增；待有限非作者。

#### 15804 Qwen3.5-Omni：单流text/speech速率约束与理论首包分账

[official exact-v1](https://arxiv.org/html/2604.15804v1)，实际§2.1–2.5/Tables1–2、§4.1–4.2/§5.1–5.2。Thinker/Talker保留双职责，Talker由RVQ多codebook MTP和因果ConvNet做波形；ARIA把旧双track的text/speech输出改成单一交错token stream，约束任意prefix的累计speech:text token比不超过该item全局比，而非固定比例或MFA alignment。text prefix可先输出、speech随后连续；这是token和已可见audio单位的提交节奏条件，不是任意字词精确对齐。输入video帧按实际时间映到约160ms/temporal-ID并保连续位置身份，AuT 6.25Hz及40M小时训练是另一资源/表示变化，不把所有性能归因于ARIA或新编码器。

Table2明确称internal vLLM+torch.compile/CUDA Graph下的**theoretical first-packet latency**，Flash音频/视频concurrency1为235/426ms、到8为352/1625ms；Plus为435/651→955/1980ms。不能当实测生产尾延迟或不同资源规格间的横向等价比较，系统还未提供ARIA单独消融、硬件/precision/部署队列成本/CI与完整质量目标。§5语音多语言表存在并非全语言/对手都优的格，故不采“SOTA全部模态无退步”、任意时钟或所有并发稳定。2+2+2=6；相对Ch24:330–334已列“speech token与内部reasoning交错”和Ch24:393–409 Thinker→performer部署交接，ARIA新增的是**text与speech token在同一生成序列上的prefix速率合法性和单流提交边界**，不是改写原两路线。本段原为拟实际gap的作者工作态；后续root已完成写前有限核、Ch24最窄两段与Review已实写、root已对实际正文写后通过，分别见[V3_ROOT_ARIA_INDEPENDENT](./V3_ROOT_ARIA_INDEPENDENT.md)及[五项写后核](../V3_ROOT_FIVE_WRITE_AFTER_20260928.md)。这一项可计本日整合，不预支整日Gate。

#### 15840 CoEvolve：反馈驱动任务分布要与验证准入分账

[official exact-v1](https://arxiv.org/html/2604.15840v1)，实际§3.1–3.3/§4.1–4.4/Tables1–8与必要A.3消融。基于当前agent轨迹取forgetting（既往好/当前坏）、mixed-outcome边界和rare低频信号，外部explorer收集action-observation，LLM抽象成task/solution候选，再在环境执行验证并放入下一轮训练；任务集随能力边界变化。§3.3还写“执行失败但环境给positive reward”也接受，故reward与实际goal完成不能混作同一truth，特别需要保留独立holdout和污染审计。Qwen3-4B Table3 static/合成/随机探索/feedback均值43.29/45.43/49.36，A.3有关闭validation与换explorer模型的有限消融，说明不只是换一个模型名字；但任务/训练token/外部探索成本不是全部配对，Table7 feedback时间9.67%/12.76%不等总免费，BFCL validation及AppWorld协议不证明开放部署或跨任务自动泛化。H20卡数/价格、precision、CI、生产效果与反馈污染长期率未完整披露。

2+2+2=6标准拟窄Existing：实际Ch31:731–737已有“能力边界移动→verifier diagnosis产生environment/interface proposal→独立gate更新任务与反馈分布”并保非平稳/污染/heldout；本文给具体signal和受限消融，但未推翻这条责任链或为它新增不同的owner，故不为局部task recipe增写正文。Existing只承载训练控制命题，不声称原章已有三类启发式或本文全部实验；待非作者对读。

#### 16004 AgentV-RL：双向工具验证的证据与成本边界

[official exact-v1](https://arxiv.org/html/2604.16004v1)，实际§3.1–3.3/§4.1–4.3.4/Tables1–5与必要AppC.3–C.5。forward plan后用Python或可执行步骤检查，从结论向前提做backward consistency，两路BoN信心平均；迭代revision要两路均判correct，否则额外verifier反馈。合成数据来自可验证solution，丢弃全对/全错后先SFT再GRPO；同固定候选池及相同初始solution的主比较有受控价值，但两路是同一个训练模型，并非独立ground-truth审核。Ablation只支持所测模型/bench中forward与backward互补，不证明任意数学题或编码任务都能形成完备proof，也不证明多轮工具调用的effect已经授权。

Table5单A100/vLLM/batch128，base 2560tokens/119s，双向Agentic verifier 8349tokens/11.3round/1.6tools/323.4s；相对候选打分收益伴近2.7×时间和约3.3×token，不可只报告accuracy。训练为16/32×A100 BF16、SFT15k/GRPO50k及最多3tool/rollout，线上reward/eval与训练预算不等价；单次表无CI/真实生产tail，模型容量、工具可用性与生成token控制必须配对。2+2+2=6标准拟Only：forward/backward交叉审核是有限验证策略，Ch66已把verifier proposal、外部证据、错误分账和成本放在评测链，Ch79保留独立commit；本文未提供新的truth owner或跨任务可认证保证，不能把“同模型双向”直接提升为充分审计机制。待有限非作者。

#### 16007 MemExplorer：模拟设计空间不等可交付memory hierarchy

[official exact-v1](https://arxiv.org/html/2604.16007v1)，实际§2/§4/§5.1–5.6/Tables3–9。PLENA解析/时序近似把on-chip SRAM/3D-stacked与off-chip HBM/HBF/LPDDR容量、带宽、mapping、算子traffic、PE阵列和prefill/decode目标共同搜索，GP-EHVI迭代找到不只一种Pareto点；不是实际制造并测量这些候选设备。BFCL/OSWorld生成长度与任务风险可作为模型负载，Tables5–6的7百瓦budget下P1约697.1W/P2 570W、D1 249.9W/D2 450.95W，TPS是模型预测/设计空间结果，不能将PF/D的不同batch直接称同吞吐benchmark。Table9仅一层Llama3.3-70B prefill/seq4096对PLENA emulator 814.14ms，作者模型731.11ms约10.20%误差；不是完整LLM end-to-end、实芯片或训练/推理quality验证。HBF等器件参数、热、供货、chip-to-chip和完整互联配置是模型条件，真实制造可靠性、precision与serving tail ND。

2+2+2=6标准拟窄Existing：实际Ch54:493–503已有“SRAM/cache phase-specific working-set knee→operator trace、层级流量、mapping、cycle与技术模型联合设计→模拟只缩搜索、实机profile验收”，并有3D-DRAM热/compute联合选择；本文提供更宽层级枚举与局部模拟校准，未反驳上述决策权或交接。Existing只对这一设计期命题，不把PLENA Pareto数当Ch54实测承诺；待有限非作者。

### 否定侧定点重开：15660 印刷 DP 发布保证

旧题摘表把 15660 作为已有 DP-trained model 的 post-processing 前关闭；否定侧抽检实际重开[官方 exact-v1](https://arxiv.org/html/2604.15660v1) §3.1–3.3/Algorithm 2、§4.1–4.2 后，发现打印算法先直接从私有 `X` 抽出特征、逐列置换为 `X̃`，然后发布 `X̃` 与 DP 模型预测标签。对单记录相邻 `x=0` 与 `x=1`，置换恒等，公开特征事件概率从 1 到 0；任意 `δ<1` 均不满足论文对**整个发布数据集**声称的 `(ε,δ)`-DP。逐列置换在多记录下仍保留列多重集合；此独立发布通道不能借 DP 模型后处理继承保证。只反驳印刷 Algorithm 2/§3.3 的完整发布保证，不声称可选代码或部署实际泄漏，不抹去四个表格任务的受限 utility 表。对本项目的贡献不是表格合成应用本身，而是 Ch27/72 的隐私 authority 边界；`3+2+3=8` 定点深入、窄 Disputed 已获[root非作者有限核](./V3_ROOT_15660_FINITE_INDEPENDENT.md)，Ch72 实际命题已有覆盖，Books No Change。全部原文定位、反例和最小重开材料见[作者提案](./V3_15660_REOPEN_AUTHOR.md)；日期单核在[联合证据](./V3_DATE_RECONCILIATION.md)。正式日20 §3/4已同步；不以论文标题或旧闭合理由断案，也不抬成已获日级 Gate。

### 否定侧定点重开：16198 需求理解前测与代码反向校验

旧题摘表把 16198 的 requirement rewriting、自检循环与 benchmark 提分整体归入成熟组合；[官方 exact-v1](https://arxiv.org/html/2604.16198v1) §3.1–3.3/Tables 1–3 的必要复查发现生成前 reference QA 检查单项误解，生成失败后由代码反推被遮蔽的需求片段，属于两个可分别消融的检查点。Table 2 去 QA/去 MASK 的局部反退及§6.1首轮收益使“只是多迭代代码生成”不足以直接关闭，但 reference answer/比较仍由模型生成、public tests 不证明真实意图、调用 token/时间显著增加，未给可信 spec authority 或净生产收益。`2+1+2=5` 标准/Only 已获[root有界非作者核](./V3_ROOT_16198_FINITE_INDEPENDENT.md)，Ch79实际已有最终验收责任，不新增 Books；完整限定见[作者提案](./V3_16198_REOPEN_AUTHOR.md)。具名日期链已核，正式 §3/4 已同步；不计日 Gate。

### 否定侧定点重开：15663 代码×图像检索的方向/长度分层

原题摘表把 15663 的 shared embedding/RAG 迁移作为成熟组合前关闭。[官方 exact-v1](https://arxiv.org/html/2604.15663v1) §4.1–4.2/Tables 2–3、§6–7 的定点复查发现不同 query/return 模态方向、长 SVG 结构和未见任务的显著失配，统一平均检索分数不足以表述 coding-agent 多模态 RAG 的具体选择。Table 2 的 WebUI/UML 高分与 SVG image→code 弱项、Table 3 未见任务反退同在，§7 仅两个 image→code 生成任务提供局部 RAG 支持。实际 Ch76 已承载 typed operator、检索/reader/结果分账，因而 `2+1+2=5` 标准/Only，不为新榜单写Books；不能称共享 embedding 普适跨模态/代码泛化。最小证据、负例与实际 owner 见[作者提案](./V3_15663_REOPEN_AUTHOR.md)，[root有限非作者核](./V3_ROOT_15663_FINITE_INDEPENDENT.md)及[具名日期链](./V3_DATE_RECONCILIATION.md)均在案，正式 §3/4 已同步；未记日级 Gate。

### 否定侧定点重开：15549 有向 mixing 与无线训练成本

早期题摘表第 15549 行以“没有大模型状态/训练约束”拟前闭。现已按[作者必要原文与实际 Ch36 对读](./V3_15549_SCOPE_REOPEN_AUTHOR.md)纠正：SGP 非对称 mixing 允许有向图，§4.4 将最大入/出度、图直径与碰撞时隙成本联系，§6 的同代理 BASS 对照和 Vanilla SGP 反向证明“换优化器”不是充分解释。它为去中心训练的通信—收敛联合设计提供受限分支，不因 CIFAR/1.5M 模型而排除；但半双工无线与同步、有界梯度条件不能外推 GPU fabric、LLM 集群或实际端到端 SLO。root 已独立读 exact-v1 摘要/§1.2 与 Ch36:65–81，核准 `2+1+2=5` 标准/Only；作者完成 §2/4/6 必要反证和[具名联合日期链](./V3_DATE_RECONCILIATION.md)。正式 §3/4 与否定侧分母已同步为 88 正式、39 潜在、22 贡献前闭、1 日期隔离；不是整日 Gate。

### 04/20 V3 续跑点：八项准入纠错与 AW-PSP 写后待核

上段88/39/22/1是当时的历史阶段数，不能当当前分母。后续完整题摘已读150（旧25+额外125），作者对72个Only反向准入先移出39、自纠恢复3；[root 八项非作者逆向准入裁决](./V3_ROOT_EIGHT_REVERSE_ADMISSION_ADJUDICATION.md)再恢复15351/15451/15614/16076/15705/15706/16079/16135。该阶段正式日20 §3/§4 工作态为99唯一候选（24项已非作者写后整合、16090一项Books已实写但写后待核、13项具体Existing、43项Only、18项窄Disputed），另50具名前关闭及15483首公开隔离，`99+50+1=150`。旧证据与负例未删，八项恢复不是日级来源/分母 Gate。下一段记录此后 15557 的真实Books改判，以上24/43为历史阶段数。

16090的[作者窄差额提案](./V3_AWPSP_CH36_OWNER_PROPOSAL.md)及[root实际 Ch36 正文](../../../../../books/part-04-training-system/36-distributed-training.md)已接入“共同故障×非 IID 类别支持使边际到达校正不能重建本轮缺失梯度”条件边界，同时分开参与率/类覆盖/covered-label质量并保隐私可见性。仍需另一非作者顺读真实相邻正文、Review note 与 exact-v1 核写后，不能预计该项已通过整合。其余普通作者工作是核对正式分母、来源停点与候选独立核的真实覆盖，不扩大447库存/weekly；根审整日 Gate 前保持README进行中/未通过，之后才接04/26。

### 04/20 当前续跑点：15557 Ch31 实际写后与同行缺口

root 定点复核 `2604.15557v1` 官方必要源后，发现 Ch31 activation intervention 到按层反馈之间原缺“任意probe可读、模型原输出投影对齐、真实注入效果”三层选择边界，已按原文限制写入[实际正文](../../../../../books/part-04-training-system/31-rlhf.md)及Review。本人不是该次书稿作者，重开官方 exact-v1 §3.2–4.3/§5、顺读Ch31新段和邻接后[实际写后核PASS](./V3_APR20_15557_CH31_WRITE_AFTER_INDEPENDENT.md)；root 已同步共享 Review note。该阶段正式日20为99候选=`25`已真实写后整合+`1` AW-PSP已写待非作者写后+`13` Existing+`42` Only+`18` Disputed，另50具名前关闭+15483日期隔离，仍共150完整题摘。旧 15408 解释性简称已在正式报告改为[官方 exact-v1 标题](https://arxiv.org/abs/2604.15408v1)；15384/15408/15490已有[root三项有限核](./V3_ROOT_THREE_15384_15408_15490_INDEPENDENT.md)。按[有限同行定位账](./V3_FINAL_39_FINITE_ROUTING.md)，27项仍待具名必要单篇核，负侧15648/16056具名独立前关闭仅两项，日期/十四来源/其余正反抽样及整日 Gate 未签。validator和scoped diffcheck通过仅证可判定一致性，不是语义PASS；无stage/commit/push。

正式题名身份 QA：把本日报§3与§4中的13处缩写题名按官方 `abs/<ID>v1` 的 Title 字段恢复完整原题，精确ID为 `15488 15453 15416 15415 15357 15368 15789 15461 15350 15384 15383 15490 15804`；另 `15408` 也已从解释性简称改原题。与旧原始库存当前 title 不同的 `16211 15579 15719 16009 15967` 经官方 exact-v1 复核，本日报原题**正确**，差异来自后稿/当前身份，不能把后稿标题回拨本窗。只改标题文本与15408官方身份链接，不因名字修改增补候选、评分、Books或日期保证。

16090 AW-PSP 的 Ch36 实际正文和 Review 已获[apr01 必要官方源、前后交接、真实写后有限核 PASS](./V3_APR01_AWPSP_CH36_WRITE_AFTER_INDEPENDENT.md)，root 同步共享 Review note，故当前正式日20为99候选=`26`已真实写后整合+`13` Existing+`42` Only+`18` Disputed，另50贡献前关闭、15483日期隔离。没有剩余已申请的 Books 写后待核；27项必要单篇非作者核、负侧分层抽检、日期/十四来源与独立日级 Gate 仍待实际执行，不将单篇写后扩大为整日完成。

### 2026-09-28 来源/日期作者续核（非日级独立 Gate）

重新按当前合同顺读十四每日源的本日报§2和上方原始停点，未把任一每周源加进本日。定点重开[Google Research 四月目录](https://research.google/blog/2026/04/)九项，当前可见04/16两项→04/21 ReasoningBank，仍无本窗 Blog 条目；Publications 年目录的日级缺口不由 Blog 代替。重新调用 Seed 官方 `get_article_list_v2`：papers `article_type=1,count=20,page_token=20` 实返20/total242/next40，日期从05/12至04/08，窗口邻界04/21T16Z→Agent-World04/19T16Z→04/15T16Z；Blog `article_type=2,page_token=0` 实返15/total95/next20，邻界04/22T16Z→04/08T16Z。Agent-World 的 CMS PublishDate 仅是卡片字段，尚无该时点正文公开证明，维持已具名隔离，不因官网卡片在窗就计候选。Seed 页次已跨左界而止，不读242篇全文。

同次重开 Meta/Kimi/MiMo 三个官方入口的精确范围记在[窄停点复查](./V3_THREE_SOURCE_STOPPOINT_REOPEN.md)：尤其 MiMo Blog 卡片现为15张而非旧14张，仍以04/22与03/18两侧**正文日期**限定当前可见排序段。重开[arXiv 公告规则](https://info.arxiv.org/help/availability.html)后，仍仅把 Sun20:00 EDT、公开时分配ID与原始本日OAI/相邻ID联合使用；[原始owner收据](../arxiv-owner-replay-20260903/20260420/arxiv-owner-receipt.json)实际447身份分330个本日OAI direct、117个后改/代理，均非447候选。当前正式§3精确v1 ID去重数99；15483原收据的当前 OAI 已是04/28、v1 metadata Updated04/20T00:05:53Z，二者不能消除其同family早发问题，仍不计候选。其余机构沿上方已具名停止/复用范围，不从没有新条目推断全站零发布。此段作者侧收敛证据不签十四源/日期/150分母的非作者 Gate。

另以来源注册表“每日检查”段和本日报§2 的原 ID 作精确集合对照：两边均为同一十四项，无漏行或误加每周项。对[50项具名前关闭](./V3_NEGATIVE_SIDE_SCREEN_LEDGER.md)的原22/净新28 ID 作集合检查，50项互不重复、均见原447身份收据、与正式§3的99个精确v1候选零交集；15483只在身份收据而不在候选/贡献前闭。这只是**分母守恒/列表一致性**，不能证明50项贡献关闭或99项准入在语义上都正确；特别是15675/15583/15771同理由层的作者反向关闭正交非作者定点挑战，未得到结果前不改工作态99/50/1。

**后续状态纠正（同日，覆盖上段工作态而非抹去历史）：**root 实际完成[15675/15583/15771 三项 exact-v1 逆向准入核](./V3_ROOT_THREE_REVERSE_ADMISSION_15675_15583_15771.md)，三项旧前关闭均因具体选择边界而撤销。本人对照先前已读必要方法、主对照及反证：15675 的跨语几何筛种有随机/单语固定流水线对照，原 apr02 标准审阅仍有效；15583 在同文档多query时以本地分块前向/KV缓存换reader token，QuALITY-hard质量与690.9s查询成本必须同报，单query/文档变更不能外推；15771 将失败探针与后续rewrite/decompose/focus/exit router分责，OOD局部增益与Hotpot EM反退、gold标签/未匹配成本同报。三项均按 `2+1+2=5` 标准 Only 正式恢复，实际 Ch27/76 的长期 owner 责任仍覆盖，不作 Books 新增；原关闭证据作为失效判据历史保留。当前工作态为102候选（26 Integrate/13 Existing/45 Only/18 Disputed）、47具名前关闭、15483日期隔离；当前列表集合与整日语义/日期 Gate 须另核。

**十四每日源作者状态审校：**将 `RESEARCH_SOURCES.md` 每日检查段（截至“每周补齐”前）与正式§2逐ID比对，均为同一十四项且无 Weekly。OpenAI Research历史分页、Google Publications日级停点、Meta Research逐条SSR日期仍不可恢复到能证明全目录本窗零命中的程度；虽有RSS／Google Blog+DeepMind／Meta Publications可见段辅助，本日报这三项应按必查入口标`受阻`、分别留下可见停点及官方历史页返回的精确重开条件。此前把它们拟作`检索受限`触发 validator 指明该词只适用补检搜索；已依当前 Report 合同修为`受阻`，重跑本日报validator与diffcheck均PASS。三项安全隔离不用于候选、Books或全网无漏断言，其余十一项继续以各自实际入口/分页限度表述；这只是作者侧状态纠错，不自动通过Coverage Gate。

### 04/20 作者侧收束与下一实际接点（仍非日级 Gate）

上段102/47/1与27项缺口是当时工作态，不覆盖以下最新续跑。

### 2026-09-28 十一项冲突、来源/日期与负侧作者续跑（非独立 Gate）

已按当前§3把[十一项 peer/作者关闭冲突](./V3_NEGATIVE_11_AUTHOR_ADJUDICATION.md)逐项裁决，七项恢复受限标准Only（15622/15794/15871/15741/15760/15521/15621），四项维持具名前关闭（15657/15802/15972/15756），完整旧反证不删。正式日报现为 **109候选＝26真实写后整合+13具体Existing+52Only+18窄Disputed，40具名前关闭，15483首公开隔离1，共150完整题摘**；这只是作者工作态，不以准入比例为目标，也不签分母。七恢复均在§3逐项列明、§4有原文机制/评价/反证/实际owner对照，没有新增共享Books写入。

另已按[十四源/首公开/负侧作者审校](./V3_AUTHOR_SOURCE_DATE_NEGATIVE_AUDIT.md)与 `RESEARCH_SOURCES.md` 每日段逐ID集合核对，来源十四项匹配且没有Weekly。十一行以已记录的跨窗邻界限制为`已检查`，OpenAI Research历史、Google Publications日级、Meta Research SSR三项维持`受阻`和精确重开条件，不写机构零发布。再读官方 arXiv announcement/赋ID规则、原 OAI 与 owner 447身份收据的330 direct/117 later分层；15622/15794只有代理身份，但与相邻ID/统一公告批链联合，Submitted/Updated/DOI-created任一孤证不称 first-public。15483/Seed AgentWorld仍独立隔离。负侧取一般系统15475、成熟逻辑15727、旧peer冲突四维持和相对正侧样本作有界对照，不冒称40项全核或负侧Gate。

单篇Evidence→实际owner原27项中，root 实际另完成15350/16009、15750/15764、15780/16067、15789/15726八项具名有限核，当前[最小19项队列](./V3_FINAL_39_FINITE_ROUTING.md)仍需逐项非作者回执；七恢复的贡献逆向核另算，不机械重拉全部附件。作者普通题摘、可写Books与本次有限收口均已执行，后续日级来源/日期/正反样本和最终语义Gate仍由非作者实际核，不把同行待核称外部受阻或宣布Complete，也不接04/26。
