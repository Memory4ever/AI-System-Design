# Daily Research — 2025-07-21

**规范：** V3
**窗口：** 2025-07-20T09:00:00+08:00 ～ 2025-07-21T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-07T00:16:20+08:00

## 1. 结论

当前没有同时通过贡献准入与本窗公开日期确认的确定候选；这不是“本窗零命中”。官方 OpenAI RSS 有一项落窗的社会使命文章，按内容范围关闭。arXiv 四个有界主题查询返回184条、跨分类去重121个家族，是提交区间线索，不是121篇本窗新论文。相关或含糊标题读取完整题摘，明确科学/领域应用旁支按范围关闭；具体筛选与精确版本原件见[筛选记录](../_sources/daily-20250721/SCREENING.md)。

NABLA、DistFlow、Paper Summary Attack 的机制准入已获首批独立校准；已有部分核心证据保留，但其首次公告不能由提交史、正常公告日程或普通元数据更新字段确认。其余潜在贡献同样隔离在日期缺口，不评分、不记为候选/审阅完成、不进入 Books。机构动态目录另有明确历史覆盖缺口。因此不作“无遗漏”、日期 Gate 通过或普遍性能/安全结论。

Books 已纳入判断，本次实际改书为无：公开事件身份未定的材料不能作为本日正面证据。三个主要保留项已提出唯一 owner 与相对现有论点的待核差额（§4）；不是“已有覆盖”或整合验收。root非作者DAY已完成，纠正两项把部署/任务模块当新机制的保留理由；可执行工作已收束，外部保留项只按§5具体材料重开。本日完成的是含隔离缺口的安全终态，不是所有来源覆盖、潜在线索准入或证据均通过。

## 2. 来源覆盖

原始请求均保留在同日 `_sources/daily-20250721/` 的 `.request.json`，响应为同名 `.raw`；`HTTP 200` 不等于历史窗口覆盖。下面“已检查”只限所列官方切片。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方 RSS](https://openai.com/news/rss.xml)完整响应，按 UTC 07-20 01:00～07-21 01:00筛出1项；`openai.raw`。使命文章题名/描述不含模型或系统机制 | 已检查 | RSS未声称穷尽未收录研究；本次不扩扫历年文章 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)页面及内嵌研究目录，174个 `publishedOn` 字段（含重复），读取2025年6～8月切片；7月仅15日，邻接8月1日。`anthropic.raw`；不用图片更新时间 | 已检查 | 仅该官方研究目录，不外推全机构网页 |
| SRC-GOOGLE-AI | [DeepMind Blog](https://deepmind.google/blog/)当前首页；尝试 `?page=6`仍为同页；[Google Research Publications](https://research.google/pubs/)当前目录。`deepmind*`、`google-pubs*` | 受阻 | 未恢复本窗历史公告切片；当前首页不能证明当时没有相关事件 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)及[Blog](https://ai.meta.com/blog/)原始页面均只有动态壳，`meta-research*`、`meta*`；定点历史搜索没有取得官方窗口目录 | 受阻 | 本窗官方历史条目/日期不可恢复 |
| SRC-QWEN | [官方 Blog](https://qwenlm.github.io/)及[第2页](https://qwenlm.github.io/page/2/)，读取7月24日至6月26日日期切片；7月22日之后直接6月27日/26日；`qwen*`、`qwen-page2*` | 已检查 | 该Blog切片未见落窗研究事件，不代表所有代码/未登记事件 |
| SRC-DEEPSEEK | [官方更新日志](https://api-docs.deepseek.com/updates)，完整 dated changelog 在5月28日与8月21日之间无本窗条目，`deepseek*` | 已检查 | 仅官方公开更新日志切片 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog)完整可见索引2024-05～2025-11，邻接本窗为7月17日 Playground、8月1日Turbo；`moonshot*` | 已检查 | 仅该完整Blog索引，不把7月11日K2另算本日 |
| SRC-TENCENT-HUNYUAN | 首查[Research](https://hunyuan.tencent.com/research)；隐藏浏览器超时后读公开JS，再按DAY提示恢复[公开publicList](https://api.hunyuan.tencent.com/api/blog/publicList) POST `{pageNum:1,pageSize:100,renderType:0}`，code0、totalNum9、返回9条，现存公开/显示日期均2026年；`hunyuan-public-list.*` | 受阻 | 公开目录实际仅9条2026记录，不能据此证明2025历史无研究；未调用私有/admin接口 |
| SRC-ZAI | 首查[Research](https://www.zhipuai.cn/zh/research)，当前15项只追到2025年12月，`zai*`；历史定点搜索未恢复本窗官方目录 | 受阻 | 动态“更多”未取得2025年7月切片 |
| SRC-BYTEDANCE-SEED | [论文目录](https://seed.bytedance.com/en/public_papers)当前第1/13页20/242项后定点恢复官方 `api/get_article_list_v2`：2025论文type1、token0、count20返回total94/next20但**无article payload**；Blog type2 token0返回15条、next20，token20返回18条、next40，已越过目标到2025-03；邻接本窗显示07-22与07-15 BJT。`seed-api-*` | 受阻 | Blog当前公开返回切片未见落窗条目；论文API缺必要payload，不能由total/pagination推零命中，也不展开全部94论文 |
| SRC-BAIDU-ERNIE | [技术博客](https://ernie.baidu.com/blog/zh/)后按DAY提示恢复[官方归档第2页](https://ernie.baidu.com/blog/zh/page/2/)，末页标1/2返回6项，日期11-11、11-07、10-16、09-12、08-14、06-30 UTC；后两项夹住本窗，`ernie-page2.*` | 已检查 | 限官方Blog归档切片，不外推全部论文/代码；不因初次壳响应错误保留“没读到目录” |
| SRC-XIAOMI-MIMO | [官方首页](https://mimo.xiaomi.com/)内嵌Paper实际8项已读完日期：2025-06-04后到10-21；Blog只展示15项+More，另一次读取直接引用的 `index.c5195ace.js`未恢复历史Blog；`mimo*`、`mimo-index-js.*` | 受阻 | Paper日期切片已检查，Blog历史日期未取到；不把整页无材料或Paper无条目推广到Blog |
| SRC-MINIMAX | [Blog](https://www.minimax.io/blog)当前12项最早2025年10月；`?page=2`仍返回同样首页，`minimax*`、`minimax-page2*`；定点搜索未恢复历史 | 受阻 | 不把无效页码尝试当作读完2025年7月目录 |
| SRC-ARXIV | 模型65、系统26、Agent68、多模态25条，四个主题查询各start=0/max=150且total均不足150；按2025-07-17 18:00～07-18 18:00UTC**提交**区间检索；精确查询在[抓取脚本](../_sources/daily-20250721/capture.py)，Atom原件及请求信息已存。cs.CL/LG月列表仅作相关标题查漏，不设全月逐项队列；API现版本与v1分开 | 受阻 | 正常Sunday20ET公告是线索，moderation可延后；未取得带日批次的07-21首次公告。月目录无日头、advanced announcement只支持年月。OAI/DataCite定点恢复不足以确认公开事件，详§5 |
| 表外：[Apple ML Research](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates) | 定点核2507.13575首公开，官方“Update July17,2025 … technical report released today”，`apple-update*` | 已检查 | 本日不收：作者原始报告7月17日已公开，时区不详也不会落到本窗；不自动重开7月17日报 |

辅助搜索只用于上述历史恢复，没有把搜索无结果作为零命中证据。每周来源未扫描；没有触发需要展开的会议/软件release来源。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

无可列为确定本窗候选的材料。下节保留既有准入/局部证据，§5列日期与来源保留项；不先评分后补日期，不把摘要读完记为标准/深入审阅完成。

## 4. 证据与知识整合

以下不是候选审阅完成声明；日期未定时保留已读证据，不新增全量深审队列。

### [∇NABLA v1](https://arxiv.org/html/2507.13546v1)

`core-13546-v1.raw/.txt`方法与相关实验已读：downsample Q/K用于逐head累计注意力质量阈值选择blocks，并与局部邻域联合。固定局部窗口会漏远距离关联；纯adaptive稀疏也可损伤相邻latent边界，因此不能将减少attention FLOPs等同于保质加速。§4 Tables1–3限Wan2.1 T2V14B、720p、4×H100、PyTorch2.7/FlexAttention及作者质量协议；推理约2.7×不迁移为训练普遍值，作者2B DiT阶段训练对照约1.46×。未复现、未核生产执行，训练/蒸馏预算不得由推理速度代签。

待核 owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS`，即[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。现有SparVAR/ToProVAR论点分开尺度坐标、稀疏proxy与质量/净预算；潜在差额是视频DiT中的**动态长程块选择与固定邻域必须互补**，不是重复“稀疏有成本”。由于日期未核，不采用该差额、不写书，也不声称全章已有覆盖。

### [DistFlow v1](https://arxiv.org/html/2507.13833v1)

完整精确v1题摘与HTML已保存，核心证据未读到标准审阅完成。首批准入聚焦hybrid RL框架中央数据流/执行控制瓶颈→worker侧分散数据与调度，不按v1摘要“7×”准入；当前API v4题摘不同，不能用后版性能回填v1。

待核 owner 为 `TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。现有正文已区分rollout/learner、policy identity、状态传递与控制面职责；潜在差额是中心协调器同时承担数据搬运与execution dispatch时的瓶颈分解与替代拓扑，需可比端到端证据才能判断。日期缺口先隔离，未据此改变现有论点。

### [Paper Summary Attack v1](https://arxiv.org/html/2507.13474v1)

完整题摘及方法核心已读（`core-13474-v1.*`），未把全部安全实验标为完成。论文摘要/学术权威包装能改变拒答行为是潜在反证；它不授权复用攻击payload，也不证明所有安全论文或任意模型都会被越狱。attack/defense framing、受测模型与作者ASR协议必须分别验收，当前不照录ASR作普遍安全结论。

待核 owner 为 `PLATFORM-SECURITY`，[Ch72“谁获得了行为控制权”](../../../../books/part-06-ai-infrastructure/72-security.md)。现有正文区分外部文本、runtime influence、source authority和最终effect；潜在差额只是**安全研究自身的学术包装也能成为拒答失效切片**，不是新增授权原理。日期未核且实验未读足，不以该反证宣称整合或已有覆盖。

### [CogniQ-H v1](https://arxiv.org/html/2507.13710v1)

精确v1不是当前API改名后的SoftPipe。为判断准入定点读公式与§4/§5.3：LLM prior×exp(Q/LTR)的软策略保留全部operator支持域，原文保证依赖prior严格非零且值有限；错误prior可把好动作概率压到近零，正概率不证明有限预算能恢复。Table3组合消融显示18个OpenML数据集平均指标差异，不独立证明任意坏prior都能纠正。保留为**模型prior作为探索建议而非硬剪枝的适用条件**线索，不仅因为HRL/Bayes术语或数据准备成绩；日期未核不评分、不采用。后续恢复若不能证明相比成熟soft guidance有具体新增边界，可关闭，不必扩读无关附件。

当前精确v1官方题摘页作轻量撤回/修订信号核查，未发现撤回标记。CUDA-L1现API已v12且性能摘要与v1明显不同，故保留版本分离，不把当前题摘当历史性能证据；这不证明修订原因或全部版本史已核验。

## 5. 缺口与下一步

**可执行剩余：** 无。root非作者DAY与定点纠偏已完成。以下缺少外部公开时间/历史目录的材料保持隔离，不作为新增深审队列。

**外部保留A：arXiv公开批次。** 具体材料身份及准入命题全部在[筛选记录“日期保留”](../_sources/daily-20250721/SCREENING.md)逐项列明。主要包括2507.13474、13540、13546、13568、13569、13579、13601、13666、13681、13710、13761、13773、13833、13868、13871、13919、13949、13984、14000、14049、14067、14111、14137，以及从API题摘识别的13490、13525、13591、13598、13705、13712、13736、13739、13859、13933、13942、14063、14263、19514、2508.00007。所有均不支持正面结论、评分、Books或“无遗漏”；其中Seed-X/PRIDE等明确贡献关闭项不为日期追加请求。

另有2507.14248 AdViT的解释/安全分离反证、2507.13920 Causal Process Models的稀疏动态interactiongraph、2507.13812 SkySense V2的统一多模态backbone与异分辨率接口机制，同样只保留题摘准入线索，不因安全、World Model或foundation主题自动采用。

缺少的是**首次公开正文/首次公告时间完全落窗的官方证据**。提交时间可对应正常07-21 08:00BJT批次，但[官方说明](https://info.arxiv.org/help/availability.html)明确moderation可能延后。`oai-13474/13546/13833`的arXivRaw版本日期只给提交史，普通datestamp是元数据修改；`datacite-13474/13833`创建分别07-21 01:19:39Z、01:28:32Z已在窗后，其v1 Updated不是明确公开字段；NABLA v1 Updated更已变为2026-07-02，不能拿它重建2025公告。定点恢复已停止。

同一组只请求一次：可接受官方07-21该批带日期的announcement/历史邮件，或作者**原始正文**的公开时刻及可核查时间语义（完全落窗的范围也可）。重开顺序是日期/首次身份→仅相关精确版本必要证据→独立复核→比较owner与必要Books修改；未得到材料前保持隔离。EdgeVLA另有v1 journal-ref “IROS-MoMA3 Workshop2024”，同一请求须包含其2024稿是否已公开、正文与时间；不能以2025新arXiv ID当首公开。API返回2508.00007等延迟ID也说明按提交区间不等于公告批次。

**外部保留B：机构历史目录。** GoogleAI、Meta、Hunyuan、Z.ai、MiniMax缺本窗官方历史切片；Seed明确为论文API payload缺失（Blog当前可返回目标切片已检查）、MiMo明确为Blog历史日期（Paper已有切片）。主入口、公开API/归档定点恢复及停止位置见§2。ERNIE归档已恢复，不再作为缺口请求。可接受机构官方历史目录/公告存档，包含原始正文链接与公开时间；不是搜索摘要、当前首页或仓库最新修改时间。只重开相应机构本窗，不遍历其历年论文。不据这些缺口宣称覆盖通过，但外部长期不可得可经独立复核作为本窗安全终态保留。

**窗外线索：** [Apple报告](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates)官方明确7月17日已发布正文，属于此前事件；本日不审为新贡献、不扩窗、不自动创建或改写别日报。真实日期需要重开时由总协调者路由。

## 6. 复核

复核者：root（独立于作者jul21_author；FIRST与DAY）。

结论：通过

通过的是隔离处置的安全终态；外部保留项不是Coverage/Evidence通过。

首批独立复核已读NABLA、DistFlow、PSA、Promptomatix、CogniQ-H、EdgeVLA六项精确v1完整题摘：前三潜在机制准入成立且要求性能/ASR限原条件；Promptomatix成熟meta/DSPy组合关闭成立；CogniQ-H要求定点确认软prior机制而非仅数据指标，已补读公式/消融并保留有限边界；EdgeVLA先隔离首公开疑点。日期有限恢复经root校准停止；这些结果只作为FIRST，不自授DAY。

DAY实际检查：六部分、固定窗口、14每日来源与Apple定点身份恢复、查询参数/不足一页停止范围、API提交字段与公告分离、版本隔离、正式候选0及Books零写入。root直接解析Seed论文缺payload、Blog两页15/18项与实际日期，检查Hunyuan公开POST返回、ERNIE归档和MiMo脚本请求；接口成功没有替代历史覆盖。初次未恢复的入口经定点修正，剩余外部目录缺口保持隔离。

独立完整题摘检查共46个不同家族：FIRST六项；后续检查筛选表全部潜在线索的题摘及Seed-X、PRIDE、Cybersecurity Survey、BifrostRAG四项关闭样本。当前API后版只用于发现层检查，不作为v1历史结论。重点核安全/负面信号：GIFT、Latent Safety Certification、VLA-Mark、Value Probing、Prompt Engineering、Consistent Explainers、Innocence、Primacy、AdViT、Political Persuasion，未以应用标题或实验局部性自动排除。SpiNNaker2/Diffusion-FSCIL原理由将通用部署/表示原则充作本次增量，已改为具体关闭；其余未明确否定的潜在线索仍只隔离，不自授证据成立。

CogniQ-H所读软prior公式只保证严格正prior下支持域不被硬剪掉；不证明有限预算能纠正坏prior，更不证明这是相对成熟soft guidance的长期增量。当前仅保留未采用的线索，恢复公开身份后仍需决定准入，不能把这次DAY当作正面审阅通过。

未检查范围：其余明确关闭项没有逐篇独立题摘复核；所有潜在线索的完整实验、实现、缺失公告、实际复现与待核Books差额亦未验明。四类关闭样本覆盖成熟流程组合、任务PEFT比较、安全综述及领域RAG；不把分层抽检称为全量来源或论文证明。缺失材料到达仅重开受影响项。

机器校验：`python3 scripts/validate_research.py --report papers/2025/07/21/README.md`和`git diff --check`通过；相对章节路径及工作树范围已检查。未stage/commit/push。机器校验不替代上述实际语义复核。
