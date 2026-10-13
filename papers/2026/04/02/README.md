# Daily Research — 2026-04-02

**规范：** V3
**窗口：** 2026-04-01T09:00:00+08:00 ～ 2026-04-02T09:00:00+08:00
**状态：** 进行中
**Books：** 纳入本次
**检查时间：** 2026-10-13T08:32:17+08:00
**补充窗口：** 2026-04-01 ～ 2026-04-01
**冻结候选日期：** [补查前原报告](../_sources/daily-20260402/baseline-before-supplement-20261013.md)
**窗口说明：** 用户授权只补既有 Daily 的来源遗漏；原窗口、25 个候选的身份/日期/评分和连续 §4 保持不变，新增仅检查前一完整北京时间自然日。旧完成与复核声明只指原轮，不能作为本轮验收。

原窗口左闭右开；原轮候选、证据与 Books 判断保留。本轮补查尚未日级验收。2026-10-13 用户额度边界下由root明确暂停本日长尾；状态保持进行中，精确停点已保存，待用户恢复后只继续本日未决层。外部材料限制不支持“零遗漏”断言。

## 1. 结论

本轮遗漏补查已保存停点并暂停；[本日实际停点](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)保存有限发现、191 个已读精确题摘、必要决定事实与可继续的准入/证据/复用事项。514 个原始身份线索不是贡献候选；当前确定新增十三项：SISA、Label Gauge、Tucker、CoT reward conflict、QUAD 五项真实整合与独立POST，MEDiC/Parallel Data 两项具体已有覆盖，Privacy Guard、CivicShield、CG-LoRA、MacTok、Modality Gap 五项中心争议隔离，RIDE 一项4分仅报告关闭。PROSFI/SNEAK必要Source已过而Books PRE待核/未写，PSPA Source和Active measurement争议已获新reader必要原稿层复核但日期/最终处置同步未完；不预支其完成或最终新增总分母。本日未获DAY/FINAL。以下原轮二十五项结论保持，不能将旧完成状态外推到补查。

旧 V2.1 日报的 `Complete / Passed` 不成立：它把 DataCite DOI `created` 日当作首次公开日，只覆盖 arXiv，旧 35 项中至少六个标题、十一个摘要受到后发版本倒灌，且把 [TENT v1](https://arxiv.org/html/2604.00368v1)写成 `TE+`。本轮用 [arXiv 公告规则](https://info.arxiv.org/help/availability.html)、连续 ID 边界、首/中/末 v1 及 DOI 时间作**有界批次归属推断**，而不将提交日、DOI 入库日任意一个冒充公开时刻。`2604.00001–01225` 与本窗北京时间 08:00～09:00 的公告批次范围相容；逐篇异常仍须单列。

旧 DOI 库存的 513 条是注册分类的原始身份线索，不是 513 篇值得本项目审读的候选。已重读旧 35 条的题摘，另从旧排除集中定点恢复可能遗漏的线索；[逐项证据与剪枝记录](../_sources/daily-20260402/v3-reopen-notes.md)记录具体排除理由。按长期系统设计增量筛选后，本窗冻结 **25 个唯一 Source Family 候选**（旧 35 条中 17 项、排除集定点查漏恢复 8 项）；这不是 513 个原始 identity 的保留率。25 项均已完成 exact-v1 Evidence Review 与 Books 终态，独立日级语义复核通过；格式校验仅作一致性辅助。

- TENT 改变 disaggregated LLM serving 的 transfer-intent 与路径/故障处理所有权；[Ch52](../../../../books/part-05-inference-system/52-dynamo.md)已承载，不重复追加。
- Terminal Agents 在相同模型和任务下把工具接口可表达性与调用成本作为可测的设计边界；[Ch78](../../../../books/part-07-agent/78-tool-calling.md)已有受限整合，不把作者受限 MCP catalog 对照推广为 terminal 普遍优越。
- ParetoBandit 把多模型路由的在线质量学习、成本速率控制与价格/质量漂移放在同一反馈环；但证据仍是离线模拟，且单请求平均成本目标不等于逐请求或账期总预算保证。[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)已吸收这一条件分支。
- NIMBLE 把 skewed MoE Alltoallv 的多路径选择从静态拓扑移到执行时的拥塞规划，得益于闲置 GPU/NIC 路径，但中继开销和小消息回退决定它不能覆盖常规 collective；[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)已吸收这一受限机制。
- EAGER 将沙箱内 Python 代码生成与完整顶层语句执行重叠；只在副作用隔离前提下适用，[Ch78](../../../../books/part-07-agent/78-tool-calling.md)已由 Books owner 作受限整合。
- Revision or Re-Solving 拆开重新求解、review scaffold 与草稿内容的贡献；其受限评价合同已由 Books owner 纳入[Ch80](../../../../books/part-07-agent/80-reflection.md)。
- MF-QAT 将单格式 QAT 与运行时多格式需求之间的 artifact 组合压力转为 anchor+slice-and-scale 转换，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)已有该机制和独立验收边界。
- TIE 把推理输出长度点预测推进到受截尾尾部风险与队列压力耦合的 SJF 决策；[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)已作窄范围整合，不能从作者高排队压测外推生产 SLO。
- Evidence Units 将多解析器的结构元素先归一为语义角色，再把图表、caption、单位和解释段组成可检索单元；[Ch76](../../../../books/part-07-agent/76-rag.md)已吸收受限 ingestion 分支，不把两种 parser 的实验称为普遍保证。
- Aurora MoE 揭示 expert 与非 expert 参数具有不同复制域，optimizer shard group 不能一刀切；[Ch39](../../../../books/part-04-training-system/39-zero.md)已吸收此条件分支，不能把 Intel PVC 上的局部 step 收益外推至其它硬件。
- Adaptive Parallel MCTS 将正向提前完成、负向停止无希望的搜索与释放并行槽连为一个调度反馈环；但“无希望”只相对于当前 PRM/阈值，且原文准确率表不支持摘要中无条件的“维持准确率”。[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)已保留这一受限分支。
- SDC Training 以参数更新异常而非单纯 loss spike 判断静默硬件计算错误，并在提交前重算当步；[Ch35](../../../../books/part-04-training-system/35-checkpoint.md)已有同一 source family 的机制正文，不把单 L40S 注错实验外推分布式恢复。
- RAG-considerate pretraining 将有限语料在参数学习与检索库存之间分配，改变 Data owner 的生命周期预算问题；[Ch27](../../../../books/part-04-training-system/27-data.md)已吸收条件化机制，未把作者的拟合交叉点当作通用比例。
- Routing-Free MoE 将激活信号放进 expert-local gate 而不再依赖中心 Top-K，但全局 density、负载和动态 fanout 的控制责任仍存在；[Ch21](../../../../books/part-02-model/21-moe.md)已吸收这一有限尺度的替代分支。
- Meta-TTL 将 frozen actor、跨 episode prompt 更新与外层 meta-policy 训练分层；[Ch80](../../../../books/part-07-agent/80-reflection.md)已有同一 reset→evidence→policy→revision 主线，受限实验不要求再追加正文。
- InterruptBench 把用户中途增补、修订与撤回条件变成可配对重放的评价事件；[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)已吸收此窄评价合同，但实验未触及已提交副作用的补偿。
- Diffusion quality–exploration 显示局部高置信 commit 的单路径收益可能限制多样本有效分支；[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)已吸收理论条件与受限采样取舍，未宣称全面胜出。
- Streaming Model Cascades 将二值语义查询的级联从全局阈值移到 partition-local 双阈值与跨 worker 风险合成；[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)已吸收这一特定 workload 的条件分支。
- UK AISI 的研究破坏评估提醒：可回滚 evaluator 会选择分支，评估环境和任务本身也分别影响 evaluation awareness；[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)已吸收 branch-tree 与对照设计的受限命题，不把未确认破坏行为外推为部署安全。
- Simple Self-Distillation 澄清：同分布自采样不是可靠的新训练目标，改变采样支持集才会构造不同 self-target；[Ch29](../../../../books/part-04-training-system/29-sft.md)已纠正旧文的错误过滤暗示，保留 raw 未验证样本固化错误的风险。
- MyPhoneBench 将 Agent 的最终任务成功与途中权限/字段披露及跨会话偏好正确使用拆开；[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)已吸收未提交编辑的过程 witness 和固定分母的成功且隐私达标评价，不把模拟用户始终授权当成真实拒绝权限压力测试。
- Agent-Judge 研究把评分稳定与去重后新问题发现拆成两种评估目标；[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)已吸收双轴预算/停止决策，未将配对差异未显著误写为人类等价。

这二十五项已有 Books 终态；独立日级 Gate 已通过，外部保留项仍遵守 §5 的隔离边界。

## 2. 来源覆盖

本节合并原轮有效入口与本轮 `04-01` 完整北京时间自然日的有限补查，不迁移旧候选。原轮依据见[日专属笔记](../_sources/daily-20260402/v3-reopen-notes.md)，本轮实际原站字段与动态/API停止见[17入口](../_sources/daily-20260402/SUP_OFFICIAL_FIELDS_20261013.json)、[六个定点原值](../_sources/daily-20260402/SUP_DIRECTORY_DATE_FIELDS_20261013.json)和[本日停点](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)。来源首屏、列表外事件或日期缺失不授零遗漏。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| `SRC-OPENAI` | [News RSS](https://openai.com/news/rss.xml)完整历史顺序至 2015；本窗 [Gradient Labs 案例](https://openai.com/index/gradient-labs) 2026-04-01 02:00 UTC，题摘没有新的模型/系统机制，准入前关闭。[Research sitemap](https://openai.com/sitemap.xml/research/)和 [Publication sitemap](https://openai.com/sitemap.xml/publication/)仅能辅助找身份，`lastmod` 不是首发。 | 受阻 | 已隔离：News 已核；Research/Publication 历史文章未能形成可验证的本窗首发停点。只隔离这两入口的潜在遗漏，取得官方文章及原始发布日期后按 family 重开，不推断零命中。 |
| `SRC-ANTHROPIC` | [Research](https://www.anthropic.com/research)原站 `publishedOn`；补窗UTC03-31 16:00～04-01 16:00内为 [How Australia uses Claude](https://www.anthropic.com/research/how-australia-uses-claude)，03-31T22:17Z＝04-01北京时间06:17。原文核心是地区使用/经济情况，拟范围关闭；下一条 emotion concepts 为04-02T10:56Z，窗外不扩读。 | 已检查 | 限此历史目录，不证明机构作者未列论文/GitHub无事件；代表性范围排除尚待本轮复核。 |
| `SRC-GOOGLE-AI` | [Research 2026-04 Blog](https://research.google/blog/2026/04/)最早为 04-03；[DeepMind Publications](https://deepmind.google/research/publications/)按日期倒序首页 04-22 直接到 03-22，未列本窗条目；[Google Research Publications](https://research.google/pubs/)按年度/领域组织、2026 年 357 项，未给日级 first-public。 | 受阻 | 两个有日期的原始目录已核；Google Research Publications 缺可界定本窗的日期/分页接口，不能从 2026 年份或当前列表推断本窗零发布。恢复条件是官方精确发布索引或具体论文链接/首次公开事件。 |
| `SRC-META-AI` | [AI at Meta Blog](https://ai.meta.com/blog/)可见 04-08 与 03-26 相邻；[Research](https://ai.meta.com/research/)动态目录无法从可读静态页形成完整历史停点。 | 受阻 | 已隔离：Blog 所见邻近日期不证明 Research 零发布；仅隔离该动态目录，取得当窗官方原文/可检索历史索引时重开。 |
| `SRC-QWEN` | [Research](https://qwen.ai/blog)的官方 `GET https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US` 返回40动态项；补窗相邻为03-30 Qwen3.5-Omni→04-02 Qwen3.6-Plus，未列04-01項。60旧静态项的原轮具名有效证可复用；[Qwen3.6-Plus](https://qwen.ai/blog?id=qwen3.6)官方04-02T04:00+08、能力披露/`preserve_thinking`版本事实保留原轮，不移入补窗。 | 已检查 | 限该官网 Research目录，不推断作者arXiv与仓库全部事件无更新。 |
| `SRC-DEEPSEEK` | [Research & News](https://deepseek.com/en/news/)本轮首页恢复可读，News04-24→2025-12-01、Research06-24→02-25；原轮完整目录曾HTTP429，本轮首页恢复不证明 `View All` 完整历史恢复。 | 受阻 | 完整动态列表仍未形成历史终点；仅隔离该入口未见的当窗事件，不以首页间隔证明全站零命中。恢复条件为官方完整历史目录或该窗口原始文章链接。 |
| `SRC-MOONSHOT` | [Kimi Blog](https://platform.kimi.com/blog)可见归档仅到 2025-11；官方组织仓库排序页查至 100 个 repo，未见当窗新建；定点核 [checkpoint-engine releases](https://github.com/MoonshotAI/checkpoint-engine/releases) 19 个（2026-02-02→06-08 相邻）、[Kimi-K2.5 releases](https://github.com/MoonshotAI/Kimi-K2.5/releases)空，无该窗重大 release。 | 受阻 | 已隔离：Blog 不提供 2026 完整档案；repo 检查限上述入口，不把无新增 release 扩为所有仓库无事件。未列研究正文待具体身份重开。 |
| `SRC-TENCENT-HUNYUAN` | [研究“全部”目录](https://hunyuan.tencent.com/research)的官方 `POST https://api.hunyuan.tencent.com/api/blog/publicList`，`pageNum=1,pageSize=100,renderType=0`，返回 9/9，04-23→02-13 之间无本窗条目。 | 已检查 | 限此完整目录，不覆盖机构作者未列 arXiv 或仓库 artifact。 |
| `SRC-ZAI` | [Research](https://www.zhipuai.cn/zh/research)的 [GLM-5V-Turbo原文](https://www.zhipuai.cn/zh/research/156)显示 `2026/04/01 16:00` 未标时区；本轮已读核心只有CogViT/MTP/RL名词、30+tasks、榜单与展示，未给可复原新方法或受控归因，拟贡献前关闭。 | 未完成 | 等待代表性准入复核，不是不可读正文；若排除通过，不为不影响处置的时区无限追查。当前未入确定候选或Books。 |
| `SRC-BYTEDANCE-SEED` | [Research/Blog](https://seed.bytedance.com/en/research)可见 04-11→01-27；[论文目录](https://seed.bytedance.com/en/public_papers)同站 `GET /api/get_article_list_v2`、`article_type=1,count=20,order_desc=true,page_token=40`、`x-tt-locale: US`，242 总条目；倒序页 04-07T16:00Z 紧接 03-31T12:00Z。 | 已检查 | 限这两个目录，不推断 Seed 作者未列论文或仓库没有本窗事件。 |
| `SRC-BAIDU-ERNIE` | [Blog](https://ernie.baidu.com/blog/zh/) 04-15→02-06，[Publication](https://ernie.baidu.com/blog/zh/publication/)当前四篇且无窗内标题；[PaddlePaddle/ERNIE releases](https://github.com/PaddlePaddle/ERNIE/releases)仅见 2025-06-30 的 `ernie-4.5`，本窗无 release。 | 已检查 | Blog 仅日精度，不能证明该日具体 09:00 边界；其它未列原始稿须凭身份重开。 |
| `SRC-XIAOMI-MIMO` | [Paper/Blog](https://mimo.xiaomi.com/)八篇 Paper 日期 06-29→03-13，Paper 无本窗项；[XiaomiMiMo/vllm](https://github.com/XiaomiMiMo/vllm/releases)与 [MiMo-V2-Flash](https://github.com/XiaomiMiMo/MiMo-V2-Flash/releases)公开 release 列表为空，组织 repo 排序页本窗无新建。 | 受阻 | 已隔离：Blog 目录约十四项不标日期，未能建立本窗全量时间边界；不以 Paper/release 零条代表 Blog 零发布，取得原始日期再重开。 |
| `SRC-MINIMAX` | [英文](https://www.minimax.io/blog)/[中文Blog](https://www.minimaxi.com/blog)相邻03-18→更晚条目；[cli releases](https://github.com/MiniMax-AI/cli/releases)补窗 `v0.4.0/0.4.1/0.4.2` 为04-01 09:03/11:14/11:20 UTC，原有效核心是状态栏/配额、JSON config/Node installer、CI上传修复，无新模型或系统机制，拟关闭。AgentTechBlog本轮恢复三明确日期Sep19/Sep22/Oct8，均窗外。 | 受阻 | 已隔离：[AgentTechBlog](https://agent.minimax.io/docs/techblog)未列历史slice仍不能判零遗漏；不再沿用“所有条目未标日期”的旧描述，取得具体当窗dated原文时定点重开。 |
| `SRC-ARXIV` | 原轮 `2604` 25家族保留；本轮四主题query共211槽/181身份，12官方March分类在28768–30045标题切片及必要尾页共470身份，合并514线索；三批精确v1完整题摘191已读，宽列表不当贡献/全文队列，停止扩大。日期采用官方常规下界＋2603首次公告月月底上界＋无早正文反证的复合门，不以Submitted/created单独归日。 | 未完成 | 现有191题摘的贡献归并、必要例外日门、证据与Books/独核仍有可执行事项；CRAFT/MPP已root接纳有效同事件复用，另外18点核待接纳。StepCache早提交与LongCat早仓库正文信号精确隔离，不倒迁旧候选或授无遗漏。 |

## 3. 候选与判断

下表先保留原轮冻结的 **25 个候选家族**，补充窗口已核新增随后列出，新增总分母尚未冻结。原25项公开时间栏保持 `2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00` 有界批次范围：它由官方公告计划、相邻 ID 切点及 pinned-v1 共同推定，**不是** arXiv 为每篇披露的秒级时刻；新增按已核 `04-01` 日期。若以后发现单篇延期公告等例外，只重开该项而非整体平移。旧稿按 DOI created 得到的评分作废。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [TENT — arXiv:2604.00368v1](https://arxiv.org/html/2604.00368v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | transfer intent 与物理路径/切片/恢复分权；2 + 2 + 3 = 7。 | 深入完成 | 已有覆盖：INFER-DYNAMO，[Ch52](../../../../books/part-05-inference-system/52-dynamo.md)。 |
| [Terminal Agents — arXiv:2604.00073v1](https://arxiv.org/html/2604.00073v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 受限企业任务中的工具接口表达能力及成本边界；2 + 2 + 2 = 6。 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md)。 |
| [ParetoBandit — arXiv:2604.00136v1](https://arxiv.org/html/2604.00136v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 开放时长的质量—成本反馈路由与价格/质量漂移；2 + 2 + 2 = 6。 | 深入完成 | 整合：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)。 |
| [NIMBLE — arXiv:2604.00317v1](https://arxiv.org/html/2604.00317v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | skewed MoE collective 的执行时、容量归一拥塞规划及 GPU/NIC 中继；2 + 2 + 2 = 6。 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。 |
| [Executing as You Generate — arXiv:2604.00491v1](https://arxiv.org/html/2604.00491v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 完整 Python 顶层语句的生成—沙箱执行重叠；2 + 2 + 2 = 6。 | 深入完成 | 整合：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md)。 |
| [Revision or Re-Solving — arXiv:2604.01029v1](https://arxiv.org/html/2604.01029v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 二次调用收益的 re-solving / scaffold / draft-content 拆解；2 + 2 + 3 = 7。 | 深入完成 | 整合：AGENT-REFLECTION，[Ch80](../../../../books/part-07-agent/80-reflection.md)。 |
| [MF-QAT — arXiv:2604.00529v1](https://arxiv.org/pdf/2604.00529v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 单 anchor 多格式 QAT 与运行时转换，须逐格式验收；2 + 2 + 2 = 6。 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。 |
| [TIE — arXiv:2604.00499v1](https://arxiv.org/pdf/2604.00499v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 截尾分布尾部风险进入 SJF，并随队列压力调权；2 + 2 + 2 = 6。 | 深入完成 | 整合：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)。PDF v1 与 HTML v1 日期字段冲突，仅 PDF 作证据。 |
| [Evidence Units — arXiv:2604.00500v1](https://arxiv.org/html/2604.00500v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 跨 parser 语义角色归一和图文证据单元的 artifact identity；2 + 1 + 2 = 5。 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md)。 |
| [Aurora MoE — arXiv:2604.00785v1](https://arxiv.org/html/2604.00785v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | expert/non-expert 各自复制域决定 optimizer state 分片组；2 + 2 + 2 = 6。 | 深入完成 | 整合：TRAIN-ZERO，[Ch39](../../../../books/part-04-training-system/39-zero.md)。 |
| [Adaptive Parallel MCTS — arXiv:2604.00510v1](https://arxiv.org/html/2604.00510v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 搜索正/负退出与释放并行槽的耦合调度；2 + 2 + 2 = 6。 | 深入完成 | 整合：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)。 |
| [Silent Data Corruption in LLM Training — arXiv:2604.00726v1](https://arxiv.org/html/2604.00726v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 受控故障注入下的异常更新检测与提交前重算；2 + 2 + 3 = 7。 | 深入完成 | 已有覆盖：TRAIN-CHECKPOINT，[Ch35](../../../../books/part-04-training-system/35-checkpoint.md)。 |
| [To Memorize or to Retrieve — arXiv:2604.00715v1](https://arxiv.org/html/2604.00715v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 同一语料预算的预训练 `D` 与检索库 `R` 条件分配；2 + 2 + 2 = 6。 | 深入完成 | 整合：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md)。 |
| [Routing-Free MoE — arXiv:2604.00801v1](https://arxiv.org/html/2604.00801v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | expert-local gate 接管选择信号，global density 与 balance 仍需控制；2 + 2 + 2 = 6。 | 深入完成 | 整合：MODEL-MOE，[Ch21](../../../../books/part-02-model/21-moe.md)。 |
| [Meta-TTL — arXiv:2604.00830v1](https://arxiv.org/html/2604.00830v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | episode 间 prompt state 与外层 meta-policy 的分权；2 + 2 + 2 = 6。 | 标准完成 | 已有覆盖：AGENT-REFLECTION，[Ch80](../../../../books/part-07-agent/80-reflection.md)。 |
| [InterruptBench — arXiv:2604.00892v1](https://arxiv.org/html/2604.00892v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 用户信息性中断的配对轨迹、更新后成功率与成本评价；2 + 1 + 2 = 5。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。 |
| [Quality–Exploration in dLLMs — arXiv:2604.00375v1](https://arxiv.org/html/2604.00375v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | confidence gate 的单路径质量与多样本探索冲突；2 + 1 + 2 = 5。 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。 |
| [Streaming Model Cascades — arXiv:2604.00660v1](https://arxiv.org/html/2604.00660v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 二值语义查询中 worker-local cascade 与联合质量约束；2 + 1 + 2 = 5。 | 深入完成 | 整合：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)。 |
| [Doctor-RAG — arXiv:2604.00865v1](https://arxiv.org/html/2604.00865v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 失败轨迹的证据充分性判断、最早错误点定位与有效前缀复用；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：AGENT-REFLECTION，[Ch80](../../../../books/part-07-agent/80-reflection.md)。 |
| [S0 Tuning — arXiv:2604.01168v1](https://arxiv.org/abs/2604.01168v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 混合 recurrent-attention 模型以每层初始状态作可版本化适配资产；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：TRAIN-LORA，[Ch30](../../../../books/part-04-training-system/30-lora.md)。 |
| [Universal YOCO — arXiv:2604.01220v1](https://arxiv.org/html/2604.01220v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 仅循环局部高效注意力模块，同时只生成一份 global KV；2 + 2 + 2 = 6。 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md)。 |
| [UK AISI Alignment Evaluation — arXiv:2604.00788v1](https://arxiv.org/html/2604.00788v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 可回滚 evaluator 的 branch 统计与 task/environment evaluation-awareness 对照；2 + 1 + 2 = 5。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。 |
| [Simple Self-Distillation — arXiv:2604.01193v1](https://arxiv.org/pdf/2604.01193v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 同分布自采样固定点与训练采样支持集变换的条件分支；2 + 1 + 2 = 5。 | 深入完成 | 整合：TRAIN-SFT，[Ch29](../../../../books/part-04-training-system/29-sft.md)。 |
| [MyPhoneBench — arXiv:2604.00986v1](https://arxiv.org/html/2604.00986v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | 任务成功、过程隐私 witness 与跨会话偏好的分账/交集验收；2 + 1 + 2 = 5。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。 |
| [Agent-Judge Score–Coverage — arXiv:2604.00477v1](https://arxiv.org/html/2604.00477v1) | 2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00 | panel 分数收敛与去重问题发现不同步，需双轴停止；2 + 1 + 2 = 5。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。 |
| [SISA — arXiv:2603.29913v1](https://arxiv.org/html/2603.29913v1) | 2026-04-01 | 保持 output-stationary dataflow，将同 PE 池按矩形 slab 独立或融合，新增 shape/带宽相关的并行分工与成本边界；2 + 2 + 2 = 6。 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。 |
| [Label Cosine Gauge — arXiv:2603.29488v1](https://arxiv.org/html/2603.29488v1) | 2026-04-01 | fixed encoder/独立输出头的共同平移保持 softmax 分布，却可将不同类别向量 cosine 改成 ±1，限定未固定坐标的几何解释；3 + 1 + 3 = 7。 | 深入完成 | 整合：MODEL-EMBEDDING，[Ch12](../../../../books/part-02-model/12-embedding.md)。 |
| [Tucker Attention — arXiv:2603.30033v1](https://arxiv.org/html/2603.30033v1) | 2026-04-01 | 将 per-head QK/VO 乘积的 head/feature 轴联合 rank 参数化，区分参数与 latent KV 节约、RoPE 和 kernel 兼容代价；2 + 2 + 2 = 6。 | 深入完成 | 整合：MODEL-MULTI-HEAD-ATTENTION，[Ch15](../../../../books/part-02-model/15-multi-head-attention.md)。 |
| [CoT Reward Conflict — arXiv:2603.30036v1](https://arxiv.org/html/2603.30036v1) | 2026-04-01 | output/CoT 奖励对透明表达的相容关系必须绑定 task/reward pair/monitor，实测保正交语义漂移和空 trace 等反側；2 + 2 + 3 = 7。 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md)。 |
| [Privacy Guard — arXiv:2603.28972v1](https://arxiv.org/html/2603.28972v1) | 2026-04-01 | 自身不同秘密人口的泄漏计数与 70B 零漏/projected hybrid 保证冲突，限定组件隐私 guarantee 的可采用边界；3 + 1 + 3 = 7。 | 争议 | 暂缓：中心冲突隔离，不采用零泄漏或写入 Books 正面保证；见 §4/§5。 |
| [CivicShield — arXiv:2603.29062v1](https://arxiv.org/html/2603.29062v1) | 2026-04-01 | normalized MI/taxonomy mass 不能一般约束跨层共同失败，有限 L2–5 模拟也不认证七层形式安全；3 + 1 + 3 = 7。 | 争议 | 暂缓：composition guarantee 中心隔离，不写 Books 正面保证；见 §4。 |
| [CG-LoRA — arXiv:2603.29824v1](https://arxiv.org/html/2603.29824v1) | 2026-04-01 | 输出匹配目标与首步梯度不同，但同 NTK/KFAC 假设内的 2×2 反例不支持双边 top-r 的全局最优推断；2 + 1 + 2 = 5。 | 争议 | 暂缓：中心最优性证明隔离，不写 Books；见 §4。 |
| [MacTok — arXiv:2603.29634v1](https://arxiv.org/html/2603.29634v1) | 2026-04-01 | 固定 unconditional reconstruction loss 不因 mask 比例自动增加，中心 anti-collapse 的 Δ 单调保证不由原 A2 推理成立；3 + 1 + 3 = 7。 | 争议 | 暂缓：中心 collapse 资格冲突隔离，不写 Books；见 §4。 |
| [Modality Gap Robustness — arXiv:2603.29080v1](https://arxiv.org/html/2603.29080v1) | 2026-04-01 | 正交平移可保持 clean NN 差，但方差下降不一般推出同阈值误差概率下降，有限 isotropic/零 empirical-mean 反例限定中心鲁棒性保证；2 + 2 + 2 = 6。 | 争议 | 暂缓：中心 tail-probability 保证隔离，不写 Books；见 §4。 |
| [QUAD — arXiv:2603.29535v1](https://arxiv.org/html/2603.29535v1) | 2026-04-01 | 固定运行图的跨 adapter 量化资格由 anchor profile、QuantSim teacher 适配及逐 adapter 输出回归共同决定，而不由相同 rank/dtype 自动继承；2 + 2 + 2 = 6。 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。 |
| [MEDiC — arXiv:2603.29009v1](https://arxiv.org/html/2603.29009v1) | 2026-04-01 | teacher-guided mask 与多目标效果依 dense/sparse 模式和实际 consumer，语义连贯 mask 或更多 loss 不单调改善质量；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，目标/consumer 分验与局部/全局读出边界。 |
| [Parallel Data — arXiv:2603.29026v1](https://arxiv.org/html/2603.29026v1) | 2026-04-01 | 固定双语 recipe 与预算下，平行配对暴露、checkpoint 阶段、cos/PWCCA 和受控续写分别测不同对象，早期 proxy 不等终态共享能力；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：TRAIN-PRETRAINING，[Ch28](../../../../books/part-04-training-system/28-pretraining.md)，阶段/读出分账；数据类型由 Ch27 交接。 |
| [RIDE — arXiv:2603.29206v1](https://arxiv.org/abs/2603.29206v1) | 2026-04-01 | 冻结模型前置自然语言 expert framing 的 density/entropy 诊断仅改变局部 prompt 测量，不能借真实 MoE routing 扩大范围；1 + 1 + 2 = 4。 | 已关闭 | 仅报告：受限 textual proxy，不据此改写真实稀疏路由机制或写 Books。 |

## 4. 证据与知识整合

### [ParetoBandit — arXiv:2604.00136v1](https://arxiv.org/html/2604.00136v1)

§3 将静态质量—成本路由扩为持续更新的 LinUCB：per-request 质量反馈修正上下文奖励估计，EMA 的预算乘子在观察到成本超标时加大代价权重，几何遗忘使旧奖励/价格统计减重，新增模型先受有界 forced exploration 再进入普通选择。旧离线规则在模型价格/质量稳定、标签难取且必须严格确定性控制时依然简单；新环路以更快响应漂移换来反馈可信性、探索流量和模型/价格 epoch 记账。关键边界是 §3.2 明说组合的 EMA、hard ceiling 与非平稳遗忘使经典 BwK regret 保证**不适用**；单请求的动态候选价格限制也不等于整个账期美元上限。§4 的 11,983 条题目来自九种公开 benchmark，8,374/1,785/1,824 train/val/test，三模型离线预计算完整 reward–cost matrix；20 seeds 和 bootstrap CI 的四种注入漂移情景支持作者模拟内的适配，却未运行真实 delayed human feedback、endpoint 拥塞、在线总预算或多租户 SLO。作者自己承认不包含 latency-aware routing。其所谓低路由延迟只测路由器本身，不能抵扣真实模型执行成本。对读 Ch56 现有 online calibration/forgetting 与 cost routing 段后，Books owner 已在固定成本 penalty 与生产预算硬约束之间插入质量反馈、平均成本 dual price、模型池变化探索三周期控制环，保留计费/admission 与 router 的责任边界；正文没有把模拟表现升级为账期总额保证。Books Decision 为 **Integrate**。

### [NIMBLE — arXiv:2604.00317v1](https://arxiv.org/html/2604.00317v1)

§IV–V 针对静态 fastest-path/rail hashing 在 MoE 专家热点下留有闲置 NVLink/NIC 路径：monitor 取得当前通信需求，orchestrator 按链路负载与容量近似求最小瓶颈拥塞，对源—目标的分片量选择直达、经中间 GPU 或 rail-matched NIC，再由 kernel buffer pipeline 保序传输和累计完成。它修改的是通信执行计划，不改 collective 的数学语义；转发占用中间 GPU 的 cache/HBM、额外同步与链路，会与计算、其它租户争资源。作者仅对 skewed Alltoallv/send-recv 开启该路径，AllReduce/ReduceScatter/AllGather 保持既有实现；≤1 MB 或轻微 skew 的消息不值得中继。评价用两节点各四张 H100、每节点四条 NDR400、NCCL 2.26 与 OpenMPI 5.0.7/UCX 1.18 作基线；8-expert BF16 EP MoE block（4096 特征、2 层 FFN、2K–64K token）最多 `1.35×`，而 `5.2×` 是受控热点 Alltoallv collective 的峰值，不能互换。全模型训练/推理、长程拥塞动态和生产故障恢复未被证明。Ch36 已有 P2P 动态多路径和回退原则；Books owner 已在其后吸收 MoE collective 粒度的多目的地拥塞规划，明确 participant ordering/completion 不转移所有权，且未把 microbenchmark 的收益写为整段 MoE 收益。Books Decision 为 **Integrate**。

### [Terminal Agents — arXiv:2604.00073v1](https://arxiv.org/html/2604.00073v1)

论文 §3–5 在 ServiceNow、GitLab、ERPNext 三种隔离任务环境中，以相同 backbone 分别比较有限 MCP 工具目录、浏览器操作和 terminal/API 组合。旧 typed tool 在操作受限、权限治理清楚时仍合理；但 catalog 未暴露所需字段或操作时，调用语法正确也无法完成任务，terminal 可自行组合 API/脚本而不用等待新增 schema。主表的 MCP 差距受工具目录覆盖不足混杂：附录 A.1 承认 ServiceNow 过半任务类别结构上不可由所选 MCP server 完成，改用三范式均可完成的 444 个任务后差距虽仍存在，却不能推出 MCP 协议本身劣于 shell。作者还给出 terminal 的反例：浏览器 session impersonation 返回 HTTP 200 但未真正改变会话、图表渲染值可能与表格重算不同，UI-only workflow 无公开 API。论文只报告任务成功、token 成本、调用/时间；模型为 Sonnet/Opus 4.6、GPT-5.4 Thinking、Gemini 3.1 Pro，任务每种环境 330/192/207，未给生产权限模型、真实并发、SLO、跨组织 rollout 或多 seed 全矩阵；artifact 声称接受后发布，不能视为已独立复现。[Ch78](../../../../books/part-07-agent/78-tool-calling.md)已有 `typed tool → generic API → terminal → browser fallback` 条件分支，且明说该实验不证明普遍优越，本次仅保留证据与边界，不重复整合。

### [TENT — arXiv:2604.00368v1](https://arxiv.org/html/2604.00368v1)

论文 §3–4 明确应用仅申报 segment/offset/length，orchestrator 在请求时选可达路径、切片、根据遥测调度并在故障时重派；backend 只执行搬运，所有 slice 完成后对应用报告单个 batch completion。旧 Mooncake TE 的静态绑定在稳定/同构网络简单可预测，异构互连和链路 churn 才使晚绑定有价值。§5.1.1 的 SGLang HiCache 是 Qwen3-235B-A22B-Instruct-2507、8×H800、TP8、60 clients、并发4、每请求 2048 输入 token、十轮会话、600 GB KV 预算，TENT/Mooncake TE 的 input throughput 为 `78,759/58,006 tok/s`、P90 TTFT `0.67/0.90 s`。但两者还差在 NVLink 直连与 RDMA 路径，不能把总收益全归于 slice spraying；模型输出长度、serving 精度及多租户 SLO 未完整披露。故障注入的 <50 ms 跌落和 26 ms 恢复只适用于 §5.3 的 64 MB transfer/H800 testbed。Ch52 现有 116–120 行机制正文及 402 行 review note 已正确写作 TENT，保持旧静态路径的回退条件，本次不用重复改 Books。[更完整审阅](../_sources/daily-20260402/v3-reopen-notes.md#精确版本证据复核260400368v1-tent)。

### [Executing as You Generate — arXiv:2604.00491v1](https://arxiv.org/html/2604.00491v1)

§2–6 的生产者是流式代码生成模型：AST 分块器仅在 Python 顶层语句完整后将它交给持久 interpreter，下一块继续生成时前块执行。队列积压时合批可摊薄 setup；错误后早停可能节省生成，但让 repair 模型失去代码后缀，GitChameleon 上部分代码 repair 比完整代码低至 15 个百分点。四个 Python 脚本基准、七模型、Local/Docker/Open Interpreter，Ubuntu 22.04/Xeon 8352V、单 CPU pinning；论文在 mock 20/50/100/200 TPS 与真实 streaming 中分别评 NEL、端到端延迟。表中 `1440→903 ms` 是 error-free Gemini-3.1/PandasPlotBench，`10326→4619 ms` 是 error-case DeepSeek-R/PandasPlotBench 且包含提前停生成；上下文长度、并发及 SLO 未披露。它支持**隔离沙箱内**准备与执行重叠，不证明付款、发信、文件写入等外部 effect 可提前 commit。Ch78 保留 proposal/authorization/effect gate，只吸收这个窄条件分支。[完整审阅](../_sources/daily-20260402/v3-reopen-notes.md#独立推进的精确版本证据260400491v1)。

### [Revision or Re-Solving — arXiv:2604.01029v1](https://arxiv.org/html/2604.01029v1)

§3–4 与 Appendix A/B 将弱模型原答 `x1`、强模型看真实草稿 `x2`、强模型直接重答 `x3`、同 review 模板但空草稿 `x4` 配对比较，避免把“第二遍更好”直接归因于真实纠错。两组模型对与 GPQA Diamond 198/HLE 451/LiveCodeBench 1054 中，弱→强的 MCQ 草稿内容贡献接近零；代码条件的空 scaffold 相对真实弱草稿在两个模型对分别为 `87.0 vs 83.9%`、`86.0 vs 78.1%`，而强→弱方向可以从好草稿获益。作者未披露完整线上 token/价格/并发/SLO；不能宣称所有任务都应跳过草稿。Ch80 将直接重解、空 scaffold、真实内容分开作为评价分支，而不是后发技术取代原有 Reflection。[完整审阅](../_sources/daily-20260402/v3-reopen-notes.md#独立推进的精确版本证据260401029v1)。

### [MF-QAT — arXiv:2604.00529v1](https://arxiv.org/pdf/2604.00529v1)

PDF v1 §3–4 以多个目标精度共训一个 master weight，保存 MXINT8/MXFP8 anchor，再按 slice-and-scale 派生较低 bit-width 的 weight；旧 single-format QAT 在目标格式固定时仍是更易独立验收的基线。实验用 Llama/Qwen 小中型与两款 Qwen3-VL、128 条 WikiText-2 QAT 示例、weight-only decoder、PPL 和几个零样本任务，没有测服务 kernel、KV/activation、并发或 SLO。单一 checkpoint 可派生多格式不意味着所有格式共享一次 release gate；Ch49 已准确写出该条件演进和失败回退，故不重复追加。[证据边界](../_sources/daily-20260402/v3-reopen-notes.md#精确版本证据复核260400529v1mf-qat)。

### [TIE — arXiv:2604.00499v1](https://arxiv.org/pdf/2604.00499v1)

arXiv PDF v1 §3–6 用相同 prompt 多次采样拟合输出长度分布，排序分数为按 `max_tokens` 截尾的期望加队列压力权重的 CVaR，并以 aging 抵抗 SJF 饥饿；此机制说明为什么只预测一个长度不足以描述长尾请求的队头风险。作者 vLLM 0.11.1、8×A6000、FP16 Llama3 8B/70B 等条件下报告高负载收益，但 ShareGPT/8B、100 RPS 的平均 TTFT 仍从 LTR `120.03 s` 降至 TIE `98.10 s`，不能外推为生产 SLO 达标；分布标签需要同 prompt 重采样，也不能免费在线获得。**版本异常：** arXiv HTML `/v1` 首页写 2026-08-24，而 PDF `/v1` 首页写 2026-04-02；本段及 Books 判断仅使用 PDF v1 原文，冲突内容不作证据。Books owner 已在 Ch56 的 SJF 基线后加入分布尾风险、queue pressure、aging 和在线长度对账分支；我对照 PDF v1 复核了该正文，没有把作者压测写成生产 SLO。[详细审阅](../_sources/daily-20260402/v3-reopen-notes.md#精确版本证据复核260400499v1tie)。

### [Evidence Units — arXiv:2604.00500v1](https://arxiv.org/html/2604.00500v1)

论文 §3 把不同 parser 的元素标签归一为 canonical roles，将表/图、caption、单位与解释段落组合成单页 Evidence Unit，再以 region footprint 观察解析器切换后可检索单元是否稳定。它解决 element-level 索引命中 caption 却漏掉数据本体的失联，代价是单元变大、embedding 语义稀释、角色误判与跨页引用仍未解决。作者对 1,340 OmniDocBench 页、1,551 条由 GT 规则生成的 QA，用同一 ko-sbert 384d encoder 报告 GT 轨 `Recall@1 0.1502→0.5113`；MinerU/Docling 的相对 LCS 增量分别 `+0.27/+0.23`，但绝对质量不同，EU 平均长度 `2,931` 对 `623` 字符。D2/D3 graph validation 还只是 schema；[当前作者 artifact](https://github.com/hanyeonjee/evidence-units)未包含完整 EU 构造 pipeline，且现时 README 的实验分母/结果不同于 pinned-v1，不可混用或宣称独立复现。这些检索指标也不证明最终答案准确或生产延迟。Ch76 已把“角色归一→region-anchored unit→parser 变更验收”接在普通 chunk 主线后，继续保留原页事实权威与小 chunk 回退。[详细审阅](../_sources/daily-20260402/v3-reopen-notes.md#精确版本证据复核260400500v1evidence-units)。

### [Aurora MoE — arXiv:2604.00785v1](https://arxiv.org/html/2604.00785v1)

论文 §3.2 发现普通 DP-sharded optimizer 与 EP 组合时，非 expert 参数在 EP ranks 仍被复制，故非 expert optimizer state 应按 DP×EP group 分片；expert 参数本身按 EP 分割，状态只按 DP group 分片。这个 state-ownership 变化不同于 §3.1 FastSparseMoE kernel 优化。作者在 Aurora Intel PVC tiles 的 Mula-20B-A2B、100B-A7B、220B-A10B 上报告 EPSO optimizer step `1.36×/1.23×/1.07×`，相应 full step `1.19×/1.06×/1.01×`；最高整体 `1.71×` 属不使用 EP 的 7B FastSparseMoE，不能归于 EPSO。报告没有证明跨硬件、所有 optimizer 或故障恢复中的状态等价。Ch39 已在 ZeRO-1 的共同 DP 复制假设后加入按参数复制域分组的受限分支，保留普通 DP shard 在 dense 或 EP=1 的简单性。[详细审阅](../_sources/daily-20260402/v3-reopen-notes.md#精确版本证据复核260400785v1aurora-moe)。

### [Adaptive Parallel MCTS — arXiv:2604.00510v1](https://arxiv.org/html/2604.00510v1)

串行 MCTS 保留先前 rollout 信息，却让单次请求的长尾搜索占住服务容量；positive early exit 只处理已找到高分解的简单路径。作者 §4 将部分树统计用于并行 rollout，若当前所有叶子的 PRM 累积得分均低于阈值则 negative early exit，释放的 rollout 槽按队列中任务的搜索进展和并行度分数再分配。这个阈值证明的只是**当前评分规则下**进一步搜索优先级低，不证明题目无解或最终答案错误；过早退出可能损害正确率。调度器还需持有 rollout 预算、部分树统计和抢占状态，动态扩缩增加协调开销。作者在 vLLM、单机 4×H100 SXM 80GB（2 张生成、2 张 Qwen2.5-Math-PRM-7B 评分）、Llama-3.1-8B-Instruct / Qwen2.5-14B-Instruct 的 Math500/AMC23 数学任务上测量；精度、输入/输出长度、请求到达率、线上 SLO 没有构成跨工作负载保证。§5.4 Table 1 直接反驳摘要“维持推理准确率”的无条件表述：AMC23/Qwen 的 Vanilla MCTS `72.5%`、Full Suite `65.0%`，Llama 为 `57.5%→55.0%`；AMC23 原题只有 40 道，性能压测另增不同 prefix，不可混作精度样本。§5.3 的 AMC23/Qwen boosting 吞吐还相对只用 negative exit 降至 `0.8×`，说明并行重分配不总有利。Ch56 已将正/负退出和释放槽位写为受限调度分支，并保留准确率、搜索预算及负载分布联测；该书稿命题未照搬摘要宣传。Books Decision 为 **Integrate**。

### [Silent Data Corruption in LLM Training — arXiv:2604.00726v1](https://arxiv.org/html/2604.00726v1)

常规 checkpoint 回退在硬件错误显性化之后才动作，若错误发生于矩阵乘而未触发 ECC，污染可能先穿过反向梯度与 optimizer step。论文 §III–VII 以 NVBit 在 HMMA 指令输入寄存器注错，观察到不同 bit、kernel、前后向阶段对训练影响不同；检测器结合参数更新 RMS 的异常与 pre-clipping 梯度范数，在可疑 step 的参数 revision 提交前重算。这把完整性边界从“周期性保存”前移到“每次更新能否提交”，但检测器只提出疑点，不能保证全错误覆盖；误报增加重算，持续性硬件故障还需隔离或回退已验 checkpoint。作者在单张 L40S、BF16/AdamW、LLaMA 60M/350M/1.3B 的受控实验分别使用 12/6/3 个种子，训练 10,000 steps，平均每 100 step 注错一次、持续 1–5 step；重算时关闭注错，故接近 baseline 的 loss 和约 1% 运行开销不证明持续故障能自行恢复，也未验证分布式梯度聚合或生产错误率。Ch35 已按相同 source family 写出 update-integrity gate、检测与 checkpoint commit 分权、上一个已验版本回退；本次复核没有发现需再加的长期命题，Books Decision 为 **No Change — Existing Coverage**。

### [To Memorize or to Retrieve — arXiv:2604.00715v1](https://arxiv.org/html/2604.00715v1)

原有数据配比只在训练域之间分 `α`，检索通常被当作训练后的免费外挂；本文 §3–5 让同一有限语料分别形成参数学习 token `D` 与推理时检索库存 `R`，把训练成本、召回与请求时上下文代价纳入同一预算选择。作者在 OLMo-2 30M–3B、至多 100B DCLM tokens、固定 Qwen3-Embedding-8B / FAISS IVFPQ / top-5 passages 下给出条件拟合和任务差异；leave-one-model-out 外推误差高于区间内插值，知识型与推理型任务也不能共享一个最优分配。它不证明 `D/N≈4.14` 为普适比例，更没有生产检索时延或真实更新成本的 SLO。Ch27 原先有域间配比，却缺参数化语料与非参数化索引的共同预算；Books owner 已在数据配比后接入 `D+R` 分配、Ch28/Ch76 的训练与召回 handoff、同预算评价及静态配比/独立 RAG 的共存边界。我按 v1 方法、实验和限制独立对读，故 Books Decision 为 **Integrate：TRAIN-DATA / Ch27**。[完整审阅](../_sources/daily-20260402/v3-reopen-notes.md)。

### [Routing-Free MoE — arXiv:2604.00801v1](https://arxiv.org/html/2604.00801v1)

旧中心 Top-K 路由使每 token 工作量可预测，batch-level expert choice 则偏向负载平衡；已有 population cutoff 只是把外部 Router 的分数改为可因果的阈值判断。本文 §3–5 让各 expert 的低秩内部 gate 自行给出激活信号，再与全局阈值比较，移去中心 Softmax/Top-K，但未移去全局 density、辅助 token/expert balance、动态 fanout 与容量责任。作者仅从头在 OpenWebText 训练至约 0.8B 参数、九项英语任务及小尺度 EP 分析；不能把理论通信路径缩短等同于 frontier MoE 的生产收益。Ch21 已在 population cutoff 后接入 expert-local self-activation 分支，并保留固定 Top-K 在硬容量/尾延迟约束下的优势；我对读 v1 原文与新段，Books Decision 为 **Integrate：MODEL-MOE / Ch21**。[完整审阅](../_sources/daily-20260402/v3-reopen-notes.md)。

### [Meta-TTL — arXiv:2604.00830v1](https://arxiv.org/html/2604.00830v1)

论文 §3–4 把单 episode 的 frozen actor、episode 间根据轨迹修改 system prompt 的 meta-agent，以及部署前训练任务上的外层 meta-policy 搜索分开，检验 prompt-state 适配而非权重在线更新。受限实验是 Jericho 3 个 ID/3 个 OOD 游戏与 WebArena-Lite 3 个 ID/2 个 OOD 域、Gemini 3 Flash actor；密集游戏反馈和二值网站反馈的可辨性不同，个别 OOD 域没有显著收益。它未给无需 reset、真实权限、长期任务或线上 token 成本的保证。Ch80 正文已经按 `reset→episode evidence→learned meta-policy→next prompt` 说明可变状态、边界与 rollback，并有 exact-v1 Review note；重新加一层术语不会形成新机制，故 Books Decision 为 **No Change — Existing Coverage：AGENT-REFLECTION / Ch80**。[完整审阅](../_sources/daily-20260402/v3-reopen-notes.md)。

### [InterruptBench — arXiv:2604.00892v1](https://arxiv.org/html/2604.00892v1)

仅把最终用户消息拼入更长 Context 的静态评估，测不到 Agent 已开始执行时能否接收新条件。论文 §2–4 将 addition、revision、retraction 注入 165 个 WebArena-Lite 任务的已有轨迹（通常在无中断轨迹长度的 60%），比较同任务 no-update 基线与中断后按最终意图判定的成功率，并按后续 action `k` 对齐 `SR(k)`、action 数与 token 开销。六种 backbone 共享 WebAgent-R1 scaffold；有些原本成功的任务接收更新后反而失败，平均收益不能掩盖这个配对反证。关键边界是这些中断**只给信息**，不重置环境、不使之前动作无效；它不能证明撤销付款、补偿文件写入等真实 effect recovery。Ch66 原有多轮评估未明确把用户目标变更、插入时已完成 action、配对轨迹和 post-update budget 作为一组 EvalRun 条件；Books owner 已作窄幅整合，并把 effect ledger 留给 Workflow，我对读 exact-v1 与正文后确认未越界。Books Decision 为 **Integrate：PLATFORM-EVALUATION-SYSTEM / Ch66**。[完整审阅](../_sources/daily-20260402/v3-reopen-notes.md)。

### [Quality–Exploration in dLLMs — arXiv:2604.00375v1](https://arxiv.org/html/2604.00375v1)

保守 confidence remasking 先提交局部确定 token，通常有利于一次生成，却可能在重复采样时封闭其它有效路径；随机顺序探索更广，却牺牲单样本质量。论文 §3 的熵界只在自评分、固定置信 gate 与所述采样条件下成立，不能概括所有 diffusion 或 AR decoder；§4 的全局目标需要不可算的 suffix lookahead，实际用 mean-field 与单位置 batched IMH 近似，减少顺序依赖但增加前向计算与近似偏差。§5 仅测 LLaDA-8B/WeDLM-8B 的数学和代码任务、每步一个 token；WeDLM MBPP 与 LLaDA HumanEval 的 pass@1 在默认高置信方案下高于 IMH，不能说替代方案全面胜出。Ch24 原 confidence schedule 已说明单路径质量/并行性，但未分清 `pass@1` 与多样本 `pass@k` 的设计目标；Books owner 已在原段后接入这条探索边界，同时保留低预算单答案的旧方案，我对读 exact-v1 与正文后确认表述受限。Books Decision 为 **Integrate：MULTIMODAL-GENERATIVE-PARADIGMS / Ch24**。[完整审阅](../_sources/daily-20260402/v3-reopen-notes.md)。

### [Streaming Model Cascades — arXiv:2604.00660v1](https://arxiv.org/html/2604.00660v1)

中心化级联可先看完整数据再按 proxy 分数划一个阈值，但分区流式二值语义查询无法等全局扫描或跨 worker 同步。论文 §3–5 让 worker 在本地批次上用高成本 oracle 标签迭代更新 accept/reject/defer 双阈值；SUPG-IT 的 joint precision–recall 目标须按每 worker 失败概率合成全局界，而 GAMCAL 用标签校准概率、按成本—质量偏好选阈值，**没有相同形式保证**。两者假定 oracle 标签可作真值，代理失准与小分区会破坏校准或使 union bound 保守。§6 的 Snowflake Cortex AISQL 仅测二值 row predicate、Llama 3.1-8B proxy / Llama 3.3-70B oracle、batch 4096、六个 5K–250K 行数据集及 10 seeds；主试验单 worker，多 worker 补试至 16，最佳 F1 常以大量 oracle delegation 换取。硬件、精度、请求并发、开放文本生成与生产 SLO 无从外推。Ch56 原有 cascade 关注 request-level commit/defer，Books owner 已补一条 partition-local 阈值与跨 worker 风险合成的受限分支；我对读 v1 原文和正文确认未把二值保证推广到开放生成。Books Decision 为 **Integrate：INFER-SCHEDULING / Ch56**。[完整审阅](../_sources/daily-20260402/v3-reopen-notes.md)。

### [Doctor-RAG — arXiv:2604.00865v1](https://arxiv.org/html/2604.00865v1)

失败的多跳检索轨迹不总要从头重跑。论文 §4–5 先判已取得的证据是否足够，再将故障分为答案格式、推理、有效 query 下的检索不足，或错误推理诱导的 query；从最早错误 action 起只重做受影响后缀。这样保留有效前缀可以降低重复 token，却把“证据充分”判断交给可能误判的 LLM judge；外部内容、权限或工具 effect 已变化时，前缀也不能无条件复用。HotpotQA、2Wiki、MuSiQue 的实验有 gold supporting evidence，并比较 EM/F1/ROUGE-L、repair rate 和 token，未证明开放环境下的可靠回滚。v1 HTML 的会议/DOI 栏仍是占位符，不视为正式发表。Ch80 已说明基于证据定位最早错误点、判定根因、划定受影响状态后局部修复，Ch76 也已有证据充分性与检索/回答 gate；当前无需重复增写。Books Decision 为 **No Change — Existing Coverage：AGENT-REFLECTION / Ch80**。[完整审阅](../_sources/daily-20260402/v3-reopen-notes.md)。

### [S0 Tuning — arXiv:2604.01168v1](https://arxiv.org/abs/2604.01168v1)

LoRA 改权重增量，prompt 改输入；对含 recurrent state 的混合模型，还可固定权重而优化每层初始状态。这个 S0 资产每次请求必须与 base revision、层/状态 schema、租户路由和 reset 一起管理；“零开销”只是不增加逐 token adapter matmul，不代表加载、隔离和切换免费。论文在 Qwen3.5-4B 上用约 48 个 execution-verified HumanEval 训练样本、十个 seed 报告作者场景增益；FalconH1-7B 的三个 seed 与 LoRA 不可区分，Spider 无跨域迁移。约 48 MB 的状态文件也非普遍大小。Ch30 已将初始 recurrent state 放在与 prompt、LoRA 并列的受条件限制的适配路线，且记录 base identity 与 artifact 边界；论文没有推翻该判断。Books Decision 为 **No Change — Existing Coverage：TRAIN-LORA / Ch30**。[完整审阅](../_sources/daily-20260402/v3-reopen-notes.md)。

### [Universal YOCO — arXiv:2604.01220v1](https://arxiv.org/html/2604.01220v1)

普通 full-attention decoder 通过加层或循环增加计算深度时，逐层全局历史读取和 KV 常随之增长。论文 §3 只让使用 sliding-window 等高效注意力的浅 Self-Decoder 共享参数循环 `T` 次，完成后生成一份供 Cross-Decoder 全层复用的 global KV。它把额外的局部表征计算与全局 KV 副本数部分解耦，不代表 total memory 常数：局部 window state、循环次数、训练 FLOPs 与 shared KV 的表示瓶颈仍须计价。作者用 10B total/1.3B activated MoE、300B tokens、MI300X 做主要训练对比，另用 1.3B dense、20B tokens 比较 RINS 等架构；等 FLOPs 与等 steps 是不同对照。§4.5 的 serving 用 1.3B、H100-80GB、Nano-vLLM、batch 32、128 输出 token，未提供生产请求分布、完整量化配置、多租户或 SLO 验收。Ch22 原有 local/global 互补与 loop-state 风险，但未连接“只循环 local compute→仅一次物化 global KV→共享读取”；Books owner 已将该条件分支置于 local/global 主线后，独立对读确认未将作者性能外推为生产优势。普通 Transformer、固定 YOCO 和不循环 hybrid 在相应短上下文/低复杂度条件仍成立。Books Decision 为 **Integrate：MODEL-LONG-CONTEXT / Ch22**。[完整审阅](../_sources/daily-20260402/v3-reopen-notes.md)。

### [UK AISI Alignment Evaluation — arXiv:2604.00788v1](https://arxiv.org/html/2604.00788v1)

论文 §1–5 的可迁移对象是评估合同而非部署风险发生率：可回滚 evaluator 能选取不同诱发分支，`last`、`any` 和分支平均的统计单位不相同；同一高风险任务在模拟与部署外观下的对照还用于拆分环境识别与任务本身引起的 evaluation awareness。被自动 grader 标出的破坏行为经人工复核的子集均为误报，所测条件下没有确认案例并不证明生产中不存在此行为。实验涉及有限安全研究任务、四模型和不同可见 trace，不能外推为通用安全保证。Ch66 原有 probe 主线未明确 evaluator rollback 的选择偏差与 branch-tree 统计；Books owner 已补这一受限分支，我对读原文与新段确认没有把未确认破坏行为写为事实。Books Decision 为 **Integrate：PLATFORM-EVALUATION-SYSTEM / Ch66**。[详细审阅](../_sources/daily-20260402/v3-reopen-notes.md#精确版本证据复核260400788v1uk-aisi-alignment-evaluation)。

### [Simple Self-Distillation — arXiv:2604.01193v1](https://arxiv.org/pdf/2604.01193v1)

PDF v1 §2 与 Appendix B 区分同分布自采样的零期望梯度与改变温度、top-k/top-p 截断后产生的目标支持集变化。作者使用约 10K 编程题和未经执行验证的自生成答案，只去掉空或单行 stub；作者所测 LiveCodeBench 改善不能证明错误样本会被自动纠正。Ch29 旧正文曾误写成生成样本经正确性过滤，Books owner 已纠正，并将“同分布 fixed point→支持集改变→可能改写 lock/fork 概率”接到现有自蒸馏论证中；我按 PDF v1 核对了训练样本、受限模型与失败风险。HTML 同版本首页日期异常，不用于本次机制证据或公开归属。Books Decision 为 **Integrate：TRAIN-SFT / Ch29**。[详细审阅](../_sources/daily-20260402/v3-reopen-notes.md#精确版本证据复核260401193v1simple-self-distillation)。

### [MyPhoneBench — arXiv:2604.00986v1](https://arxiv.org/html/2604.00986v1)

论文 §2–5 的 300 个受控手机任务把最终完成、未提交表单字段编辑/许可访问，以及跨会话偏好使用分别留痕；只看最终 app 状态会漏掉途中多填的个人信息。作者的 privacy-qualified success 使用同一任务分母作成功与隐私阈值的交集，避免失败任务因没遇到风险页面而得到虚高隐私均分。其 Android mock apps 只有 10 个，HIGH 权限请求由模拟用户总是批准，故不能证明真实用户拒绝或生产数据泄露防护。Ch66 原有 outcome witness 尚未显式覆盖未提交动作流中的数据写入；Books owner 已加过程 witness 与固定分母评价，我独立核对原文及正文，未把作者的 `τ=0.7` 升格为普适门槛。Books Decision 为 **Integrate：PLATFORM-EVALUATION-SYSTEM / Ch66**。[详细审阅](../_sources/daily-20260402/v3-reopen-notes.md#精确版本证据复核260400986v1myphonebench)。

### [Agent-Judge Score–Coverage — arXiv:2604.00477v1](https://arxiv.org/html/2604.00477v1)

论文 §3–4 的 15 个任务、两组 judge/target 模型、各 32 个角色评委显示：panel 的评分一致性提高，不等于经语义去重的新问题发现已经饱和。评分精度与开放式 issue coverage 是不同 estimand，停止规则与预算不应只看均分；但去重阈值、任务/角色选择和交互路径会影响发现曲线。43 名人类的 86 个会话与 Agent 评委比较中，`p=0.379` 只说明未检出这组差异，不是人类等价证明。Ch66 原有 active judge 主线已有评分可靠性，却未把去重后的问题发现作为独立停止轴；Books owner 已补窄幅论证，我对读 exact-v1 与正文后确认条件未被外推。Books Decision 为 **Integrate：PLATFORM-EVALUATION-SYSTEM / Ch66**。[详细审阅](../_sources/daily-20260402/v3-reopen-notes.md#精确版本证据复核260400477v1agent-judge-score-与-coverage)。

### [SISA — arXiv:2603.29913v1](https://arxiv.org/html/2603.29913v1)

补充窗口新增；精确 v1 §3–4 将固定方形阵列对小或偏斜 `M` 的闲置，转为同 PE 池全宽 horizontal slabs 的独立/高度融合：OS 本地累加不变，local buffer、weight-buffer bypass、`N` tile 并行与 `K` 分块按序累加分别承担责任。这里改变的是并行单元组织，不是已有 SPECTRA 的阶段 dataflow 切换，也不是软件让现成 Tensor Core 免费重组。正常公告复合日证由 Mar31 提交、`2603` 首次公告月及已注册 Apr1 上界共同限定，未以 DOI created 单独授日。

评价限 RTL、CACTI、SCALE-Sim 和 BF16 128×128 的 modeled GEMM；`112<M≤128` 的 EDP 反增 8.47%，ReDas 在 `M=33–50` 可更好。INT8/BF16 不能按同 PE 数视为同硬件，28nm/ASAP7 字段冲突不支持绝对功耗，所汇总线性层 GEMM 也不是完整模型或 Serving SLO。`2+2+2=6` 的实际增量是形状相关的 OS 分工与 buffer/带宽代价；因当前 owner 的具体长期缺口加深必要内容，不借整个硬件主题提高评分。

Books Decision 为 **Integrate：INFER-TENSORRT-LLM / Ch49**。在现有 Linear→GEMM shape 论点后、State→Kernel 之前新增两段，保留旧正文与相邻 SPECTRA 分工；[完整 PRE、实际位置与非作者 POST](../_sources/daily-20260402/SUP_SISA_PRE_20261013.md)记录实际正文 418/420 与静态末注 2937。root 已实际回读前后邻接及末注并通过单项写后复核，窄锁已释放；不等于本日 DAY 已通过。必要原件见[方法](../_sources/daily-20260402/SUP_FIRST_PROOF_METHODS_20261013.json)、[评价](../_sources/daily-20260402/SUP_FIRST_PROOF_CORE_20261013.json)与[日证](../_sources/daily-20260402/SUP_FIRST_DATE_SIGNALS_20261013.json)，未核 RTL/代码或复现实验。

### [Label Cosine Gauge — arXiv:2603.29488v1](https://arxiv.org/html/2603.29488v1)

精确v1 §2–4 的 common-shift 证明固定全部输入函数 `f(x)`、只改独立 output head；共同平移全部类别向量使 logits 同增 `f(x)·v`，故每个输入的 softmax 分布不变。对不同向量 `a≠b`，取 `v=−(a+b)/2` 后 cosine 为 −1，取 `v=−a+(b−a)/2` 后为 +1，两构造都非零。它反驳的是 label-cosine 对预测行为/语义的普遍可识别性，不证明某个固定 checkpoint 的统计都无用，也不授 input embeddings、tying、CLIP 或其它 readout 同样不变。v1单位向量 toy 的符号/数值不协调不采用，当前v2的sigmoid扩展不倒灌；[必要证明与反側](../_sources/daily-20260402/SUP_GAUGE_REVIEW_20261013.md)保存具体限定。

最终 `3+1+3=7` 只评这项输出组件的严格解释反例。Books Decision 为 **Integrate：MODEL-EMBEDDING / Ch12**；现有近邻/维度诊断与tying接口没有该等价类，两段落在原tying选择与PIT左逆之间，不改输入表或既有PIT。root 已实际核新168/170、160–181完整邻接和本人静态注424，POST通过、窄锁释放；[完整PRE与实际写入](../_sources/daily-20260402/SUP_GAUGE_PRE_20261013.md)。常规公告复合日证与owned注册上界见[三项日证](../_sources/daily-20260402/SUP_TUCKER_GAUGE_COT_DATE_20261013.json)，不以created单字段授日。未核代码/复现，不授本日日级完成。

### [Tucker Attention — arXiv:2603.30033v1](https://arxiv.org/html/2603.30033v1)

精确v1 §2–4 用两个三阶张量分别表示各head的pre-softmax QK与post-softmax VO乘积，以core/各轴basis联合压缩；这不是只减少KV heads，也不是既有 MHA/GQA/MLA 权重的无损runtime改写。§3存两个down-projection latent，共享时可为一份，同rank cache与MLA相同；移动RoPE到latent key保相对形式但改frequency/operator。接口先形成每头query接GQA kernel，专用core kernel是future work。Table3从头训练1B中GQA8 loss2.61、一个Tucker配置2.69，参数/iteration节约仍付质量；单H100 BF16/batch1/N4096研究decode mean不授生产SLO。[必要证据及配置/记号反側](../_sources/daily-20260402/SUP_TUCKER_REVIEW_20261013.md)保存具体支持与不采用内容。

`2+2+2=6` 针对三轴参数化与state接口差额，因具体owner缺口加深必要原证。Books Decision 为 **Integrate：MODEL-MULTI-HEAD-ATTENTION / Ch15**，在现参数/KV桥后、TP之前两段；root实际读210–248完整邻接、新229/231及本人注377，POST通过、锁释放，[完整PRE与实际写入](../_sources/daily-20260402/SUP_TUCKER_PRE_20261013.md)。不重复Ch13位置推导或Ch19容量/Ch49runtime；日证见[三项正常复合门](../_sources/daily-20260402/SUP_TUCKER_GAUGE_COT_DATE_20261013.json)，未核代码/复现。

### [CoT Reward Conflict — arXiv:2603.30036v1](https://arxiv.org/html/2603.30036v1)

v1 §3–4 按 `R_out/R_cot` 对相关计算的透明表达是否允许/惩罚/不区分，提出相容、冲突、正交条件；不是从奖励代码即可自动分类，也不证明语言预训练的 transparent bias 假设。§6–7 的 monitorability 限prompted LLM读CoT分类指定任务特征，非真实内部计算；reward sweep选联合reward最好policy，CAPO/GRPO/ICRL人口不同。冲突优化可失败，正交仍有semantic drift，长度惩罚部分低监控只是空trace；aligned初始监控完美，未实测主动提升。不据此宣称所有length penalty安全/危险。[完整必要证据与安全反側](../_sources/daily-20260402/SUP_COT_CONFLICT_REVIEW_20261013.md)保存限制，未展示攻击代码。

`2+2+3=7` 只评奖励关系与文本监控条件。Books Decision 为 **Integrate：TRAIN-RLHF / Ch31**，在原counterfactual simulator反側与curriculum转场之间新增两段，不改原论点；root actual POST已读832–853完整邻接与本人末注，新843/845和注1499通过、窄锁释放，[完整PRE/写入](../_sources/daily-20260402/SUP_COT_CONFLICT_PRE_20261013.md)。不替Ch66授evaluation truth；正常复合日证/owned字段见[日证](../_sources/daily-20260402/SUP_TUCKER_GAUGE_COT_DATE_20261013.json)，未核代码/复现。

### [Privacy Guard — arXiv:2603.28972v1](https://arxiv.org/html/2603.28972v1)

精确v1必要§6–7的自身数据不能支持摘要式zero leakage：§6.2的Qwen2.5-7B/40prompt为40/40出现泄漏；§6.4 T4/Ollama Q4_0/1000samples仍漏420/3250，其中Lazy/Institutional420/1250，个人子集零漏不是全pipeline；30B的50complexsamples为117/215，70B/6bit的50样本仍3/250。§7.3随后写70B零漏，与已有计数冲突；scanner+8B hybrid的零漏是projected不是实测，regex也不证明任意秘密完备。不同模型/人口不合并成单一前后修复实验。[必要中心两侧](../_sources/daily-20260402/SUP_PRIVACY_REVIEW_20261013.md)与[原始必要评价](../_sources/daily-20260402/SUP_PRIVACY_EVALUATION_20261013.json)保留双方。

root已实际核这些全文必要范围，新增纠错命题 `3+1+3=7`，reach只该privacy组件；不是借安全标签扩层，原先没有数字评分也不猜旧7。处置为 **中心争议隔离／Books暂缓**，无正面guarantee写入。Mar30T20:16Z、2603公告月和owned/findable Apr1注册上界共同支持正常日门，见[定点日证及当前无撤回标记范围](../_sources/daily-20260402/SUP_STANDARD_DATE_SIGNALS_20261013.json)，不是created单字段。重开需作者明确population/70B计数与§7.3勘误、实际hybrid测量/secret类别及独立验证条件；未核实现/复现，不用争议支撑覆盖或安全保证。

### [CivicShield — arXiv:2603.29062v1](https://arxiv.org/html/2603.29062v1)

v1 V-D/A-C 的 normalized MI→failure Pearson correlation 一般上界不成立：共享failure bit加各自独立高熵noise，使normalized MI可很小但failure correlation为1；正文ω与附录sqrtω不统一，taxonomy的1/8不是共同原因概率β≤.15的依据。root已实际原式及反例独核，不从七层名称授reach，最终纠错`3+1+3=7`、**中心争议／Books暂缓**。[必要形式反側与原件](../_sources/daily-20260402/SUP_CIVIC_COMPOSITION_DECIDER_20261013.json)保留双方。

root限定核的VII/T11–12中四phase和human-redteam是计划，human always-correct/FPR模型不授部署；真实模拟仅L2–5、716adv+720benign，72.9%是rawflag而非完整七层/block或harm prevented，effectiveFPR2.9%、benign多轮14%反側不能漏。其后小model pilot与猜frontier收益不是已复现/通过的部署证据，[已读必要评价原件](../_sources/daily-20260402/SUP_CIVIC_EVAL_20261013.json)和[采用/不采用范围](../_sources/daily-20260402/SUP_CIVIC_REVIEW_20261013.md)精确隔离；不声称全七层或真实人测完成。正常公告复合门/owned Apr1上界与无当前撤回说明范围见[日证](../_sources/daily-20260402/SUP_CIVIC_MACTOK_EC_DATE_20261013.json)。重开需正确依赖界/威胁population及完整stack action/outcome/human校准，不依赖层数或taxonomy替安全保证；无Books写入、代码核验或复现。

### [CG-LoRA — arXiv:2603.29824v1](https://arxiv.org/html/2603.29824v1)

v1 §3–6区分首步parameter-gradient与最终predictor alignment，但理论解只在fixed NTK、因子first-order与KFAC等式条件下；§4 Prop4.5/Eq9–10双边top-r得到tail从r+1起却称“hence solves”，自身lowerbound从2r+1起。root已实际原式并核同假设反例：whitened F=diag(3,2)、r1，双边e1残差2，B=e1/Aᵀ=e2的row/column tangent覆盖两对角而残差0。经验disjoint可能较差不修复全局最优证明；`2+1+2=5`保持，因纠错加深，不用降分消除冲突。

**中心争议／Books暂缓**，不采用最优性、必需二阶或完整实现，亦不凭反例认证/否定全部实验。必要方法/局部质量成本与直接记号问题保留在[原件](../_sources/daily-20260402/SUP_CGLORA_CORE_20261013.json)、[证据边界](../_sources/daily-20260402/SUP_CGLORA_REVIEW_20261013.md)；当前v2 June7改title而AB仍相同中心方向，无显式erratum/withdraw，不倒灌后版或遍历版本史。正常复合日证见[日证](../_sources/daily-20260402/SUP_STANDARD_DATE_SIGNALS_20261013.json)。重开需修改最优性命题/子空间限制、正确可核证明和实际数值接口；未写Books/核代码/复现。

### [MacTok — arXiv:2603.29634v1](https://arxiv.org/html/2603.29634v1)

root已实际v1 §3/4与专门[A2 Eq10–18原文](../_sources/daily-20260402/SUP_MACTOK_COLLAPSE_A2_20261013.json)：固定collapsed unconditional `−log pθ(X)` 不仅因mask m增加而改变，`E log conditional=log marginal`不成立；实际latent-only decoder又没有其input-copy loophole。mask减少input信息并不自动使informative优势Δ单调增加、扩大β保证。图像压缩/局部quality对照与mask/representation alignment配方仍保留，不把理论错误静默改成成熟组合EX，也不把有限结果当所有强压缩不collapse。

新增明确纠错`3+1+3=7`（此前未有数字tuple，不猜旧分），**中心争议／Books暂缓**，不因能映codec/anti-collapse通用原则加分。实际必要方法/评价在[决定core](../_sources/daily-20260402/SUP_DECIDER_2603-29634v1_20261013.json)；正常日门与owned Apr1上界见[日证](../_sources/daily-20260402/SUP_CIVIC_MACTOK_EC_DATE_20261013.json)。重开须修正目标/decoder信息路径、给定β/m/训练人口下可核的collapse条件与对应对照；只A2必要补读，不把A1/A3的null当已审，不扩全附录/代码。无Books正面写入/复现。

### [Modality Gap Robustness — arXiv:2603.29080v1](https://arxiv.org/html/2603.29080v1)

v1 §3–6与仅必要A3/A4/A5中，clean squared-distance差在 `v·(xi−xj)=0` 下保持的恒等可以成立；但A3/A4从zero-mean/ covariance或方差下降直接推出tail概率下降，缺分布/尾次序条件。root已实际原定理/证明及有限反例核验：unit texts±(1,0)、queries(±.8,.6)、gap(0,.6)，η两坐标均匀±3，noise1=η/2、noise2=−η/2，使每点mean0/cov2.25I且empiricalmean0；noisytexts仍相反同norm，原correct3/4，closegap后2/4。它满足原文明确的cov/零empirical条件，不能用额外未写出的独立point/Gaussian条件补证明。

保持`2+2+2=6`，因实际纠错加深，不借此否认原文有限Gaussian实验或clean恒等；也不采用所有noise/一般covariance的robust保证。**中心争议／Books暂缓**；[必要原式/反例四case](../_sources/daily-20260402/SUP_GAP_CORE_20261013.json)与[实測/非采用边界](../_sources/daily-20260402/SUP_GAP_REVIEW_20261013.md)保留Gaussian K100、embedding-only quantization与rephrasing改candidate集合的不同口径，不认证全模型量化/真实RAG/Serving。normalSubmitted、公告月与owned上界见[日证](../_sources/daily-20260402/SUP_STANDARD_DATE_SIGNALS_20261013.json)，当前v2Apr27无显式纠错标记，不回填后版。重开须明确joint noise/centering/尾分布条件与正确概率证明、对应独立对照；未写Books、扫A1/A2/其它附件、核代码或复現。

### [QUAD — arXiv:2603.29535v1](https://arxiv.org/html/2603.29535v1)

精确v1 §3–5/Tables1–5中，runtime A/B 为同一 binary 的 graph inputs；但不同 adapter 分布不能仅凭接口同形共用量化资格。作者以完整与量化输出差异选择校准锚，再让其它 adapters 在这份冻结 profile 的 QuantSim 中，向各自完整 teacher 和原任务目标适配。新增 `2+2+2=6` 只落跨 adapter 的 profile 资格与资产/质量分账，不借已有动态 A/B 原则提高分数。

base INT8、LoRA/activation INT16 的实际说明与 literal 统一 scale、affine Eq5–7 记号不能混为可执行配方；全 W8A8 有明显质量崩落，TableS11低比特质量也反退。FID比较FP32-vs-quant输出，不是real-data质量；10adapter的6×是ROM估算而非peak RAM，1.5s缺独立完整配置，不授任意chipset、免费热换新adapter或生产SLO。[必要原件](../_sources/daily-20260402/SUP_QUAD_CORE_20261013.json)与[采用边界](../_sources/daily-20260402/SUP_QUAD_REVIEW_20261013.md)已root实际核；正常复合日门和owned上界见[日证](../_sources/daily-20260402/SUP_STANDARD_DATE_SIGNALS_20261013.json)。

Ch49原A/B接口、搬运/执行成本与后续固化ROM/SRAM分支已有覆盖；本轮只在二者间写一个冻结profile资格段及本人静态注，具体PRE见[原锚及差额](../_sources/daily-20260402/SUP_QUAD_PRE_20261013.md)。实际新正文第71行、本人注第2947行（本次POST位置），root非writer完整邻接及注回读通过，窄锁释放；未核artifact/实现或复现实验。

### [MEDiC — arXiv:2603.29009v1](https://arxiv.org/html/2603.29009v1)

实际v1 §3–4/Table4–6的新增 `2+1+2=5` 只采用 CLIP frozen-teacher/ViT-student 人口下的 objective×dense/sparse 条件反側，而不把 patch/CLS/pixel 三个成熟目标组合算新机制。Table6 sparse Token+CLS75.7高于三loss73.9；Table5 block68.59高于HC64.56，不能拿patch-distill mask分母与三loss默认系统混算。语义teacher造成冗余是作者解释，没有独立控制的语义因果；权重/配置敏感不能变为普遍配方。ADE20K退步、§4.1 FCN-frozen与Table3 UperNet-endtoend冲突，以及teacher训练/总预算未匹配必须保留；0.18pp fine-tune差额无不确定性，不称显著。

[原件](../_sources/daily-20260402/SUP_MEDIC_CORE_20261013.json)与[必要边界](../_sources/daily-20260402/SUP_MEDIC_REVIEW_20261013.md)已root实际Source5核通过，正常复合日证见[日期packet](../_sources/daily-20260402/SUP_STANDARD_DATE_SIGNALS_20261013.json)。Books为具体已有覆盖：Ch23第316–318行已经拆重建/semantic teacher与三consumer、明确非目标天然互补；第117–119行又拆classification/CLS和dense grounding。root实际读308–322/111–121完整邻接接纳NC5；没有为局部mask/loss排序写新recipe，也不声称全paper/代码或附录已验。

### [Parallel Data — arXiv:2603.29026v1](https://arxiv.org/html/2603.29026v1)

实际v1 §3–5/Limitations与只核训练预算的D，四个OLMo-style1.4B、English/Finnish80/20、200B tokens，0/1/2/5%改变配对格式暴露；所有arm固定5%来自parallel-dataset，0%并非没有译对源文本。LUMI32 MI250X/64GCD、相同步预算不授跨scale普遍结论，独立多seed未披露。终态和早期PWCCA均未显示明确比例趋势；cos对随机/untrained也高，而早coherence差额来自α=.09 language-controller/Mistral judge，差额零等完美alignment是假设，不是causal shared representation。AP语言特异计数还随训练反增，不能拼为全部读出一致。

真实 `2+1+2=5` 只保数据暴露/阶段/具体读出分账，不否认parallel翻译用途或泛化为所有双语不受干扰。[必要原件](../_sources/daily-20260402/SUP_PARALLEL_CORE_20261013.json)及[反側](../_sources/daily-20260402/SUP_PARALLEL_REVIEW_20261013.md)已root实际Source5通过；正常日证在[原值](../_sources/daily-20260402/SUP_STANDARD_DATE_SIGNALS_20261013.json)。Books具体已有覆盖 owner TRAIN-PRETRAINING：Ch28第145行按相同任务checkpoint拆形成顺序、表面假信号与局部模型外推；Ch27 1350–1361拆parallel/code-switch与quality-mixture交接。root实际回读Ch28 138–150/Ch27 1350–1363接纳NC5，无新正文/附件或代码复现。

### [RIDE — arXiv:2603.29206v1](https://arxiv.org/abs/2603.29206v1)

实际完整v1题摘把routing-style meta prompt明确称textual proxy：在Qwen3-8B、Llama3.1-8B-Instruct和Mistral7B的RouterEval子集测activation sparsity、domain-keyword attention及predictive entropy/semantic variation。自然语言expert指令可使早/中层变密，attention随模型不同，density-stability相关只有Qwen弱相关；这些是冻结模型prompt诊断，不是稀疏MoE router或外部多模型选择的实际干预。root实际读完整AB校准，实际增量仅 `1+1+2=4`，不借整条routing原则提高reach，按最低关闭投入结束，不扩深审或Books。

当前officialabs仅v1、SubmittedMar31T03:19:36Z，2603首次公告月与owned/findable Apr1注册上界配合已校准常规公告下界，见[精确字段](../_sources/daily-20260402/SUP_FIVE_CURRENT_DATE_20261013.json)；不是Submitted/created单独授日。当前页无显式withdraw/erratum标记。结论仅报告局部proxy，未声称全文实现、所有frozen模型或真实MoE的反证。

## 5. 缺口与下一步

本轮已按用户额度要求暂停，仍有可执行的准入归并、必要证据/日期例外、Books与报告同步、独立复核，具体位置见[本日工作停点](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)。暂停不使这些普通待办变成外部受阻；待用户恢复再继续，不启动新日期。

SISA、Tucker、Label Gauge、CoT、QUAD 已获单项必要 Source/date/Books实际整合及非作者POST，MEDiC/Parallel具体已有覆盖已root核实际正文，Privacy/Civic/CG-LoRA/MacTok/Gap中心D/noBooks资格已获实际独核，见 §4；未把这些结果外推为整个补窗完成。普通可继续事项是其余已校准潜力的必要core/date/Books，以及EC改判及首次paper/project事件资格，具名原件和动作见[本日停点](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)。不把ordinary未读变成外部受阻。

必要日期资格：StepCache28795v1早提交Mar24，不能套常规Mar30后公告下界；LongCat29339v1的Mar30官方仓库初始README已有同贡献摘要与bundled paper链接（[原值](../_sources/daily-20260402/SUP_LONGCAT_EARLY_SIGNAL_20261013.json)），commit不是公开可见时刻，但不能忽略提前正文信号。二者先不计确定新增/评分或写Books；可接受的替代为官方首次公开公告、作者/仓库带实际public-visibility日期的正文事件。其它拟准入的早提交、ICLR/project signals仍是具体日期待核，不扩窗追全年材料。

下列原轮外部保留项保持隔离，本轮恢复与未恢复层次已同步§2；不能靠旧标签推出本轮来源完成，后续只定点重开受影响家族。ZAI因核心已可读、拟贡献前关闭而等待准入复核，暂不把普通校准任务叫外部受阻。

以下 8 项是已隔离的外部**终态保留项**，均不计入 25 个确定候选；不用于正面证据、Books 或无遗漏断言。每项的定点重开条件写在其后，仅有相应材料恢复才处理，不能由当前日报作者继续无界探路：

- `SRC-OPENAI`：[Research](https://openai.com/research/)与 [Publication](https://openai.com/sitemap.xml/publication/) 的历史目录缺可核的本窗 first-public 停点；现有 sitemap `lastmod` 不够。替代材料为官方原始文章/出版记录及其公开时间，恢复后只查本窗对应家族；News RSS 的 Gradient Labs 已准入前关闭。
- `SRC-GOOGLE-AI`：[Google Research Publications](https://research.google/pubs/) 的 2026 年份列表没有逐项本窗公开时点；已有带日期的 Research Blog 与 DeepMind Publications 停点不覆盖它。替代材料为官方原文和首次公开记录，按具体家族重开。
- `SRC-META-AI`：[Research](https://ai.meta.com/research/) 的动态历史目录不可验证分页终点；Blog 相邻日期只能证明 Blog 本身。替代材料为官方可分页目录或当窗研究原文及公开时间。
- `SRC-DEEPSEEK`：[Research & News](https://deepseek.com/en/news/)本轮首页恢复，原轮 `View All` 的429与未成完整历史停点仍不能由首页恢复关闭。替代材料为官方完整历史目录或当窗原文链接。
- `SRC-MOONSHOT`：[Kimi Blog](https://platform.kimi.com/blog) 当前归档未覆盖 2026；已核的仓库/release 停点不能替代 Blog。替代材料为官方 2026 历史列表或具体原文及其首次公开时间。
- `SRC-XIAOMI-MIMO`：[MiMo Blog](https://mimo.xiaomi.com/) 当前目录未标日期；已核 Paper/release 无命中不涵盖 Blog。替代材料为官网原文的首次公开时刻或有日期的官方目录。
- `SRC-MINIMAX`：[AgentTechBlog](https://agent.minimax.io/docs/techblog)已恢复三明确日期均窗外，尚不能核未列历史slice；已核中英文Blog与CLI release不能替代它。替代材料为具体当窗技术博文及首发时间。
- `SRC-ZAI`：[GLM-5V-Turbo 原文](https://www.zhipuai.cn/zh/research/156)写 `2026/04/01 16:00` 但未标时区，不能确定是否落窗；CogViT/MTP/RL 的官方描述亦未披露足以支撑长期机制的 Method、受控实验与条件。替代材料先是同源带时区的首发记录；若要进一步进入 Books，还需技术报告或对应的实验合同。

上述来源若恢复，只回补该来源与真实日期的家族，不重做已验的其余 25 项。旧 V2.1 原稿已无损移入[日专属归档](../_sources/daily-20260402/legacy-v21-report.md)，只用于错误审计，不复用其结论。

## 6. 复核

本轮补查独立复核：未完成、已保存停点暂停。root已执行准入/日期校准及十三项所需有效层，reader `/root/apr02_finish_reader`实际读Active/PSPA与SoK/Attesting必要原稿并给具名限定裁决，均保存在[原停点](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)。未执行本日DAY/FINAL，不计日级完成；下方为冻结原轮复核，不是本轮验收。

复核者：主任务独立审计智能体 `/root`（非本报告作者）。
结论：通过

先发现 25 行把公告批次误写成单一秒级公开时刻，已统一改为完全落窗的 08:00～09:00 有界范围；复核后检查 14 行来源入口/停点/限制的内部一致性、旧 35 pinned-v1 的 17/18 准入归并、旧排除集 8 个反向找回及 `00421/00824` 前分母拒绝，抽核 TENT/SSD/MyPhoneBench/Agent-Judge 的原文证据和边界，并核 18 个 Integrate 家族在 Books 实际有 marker、7 个 Existing Coverage 有具体章节对照。复核**未逐一重新抓取所有外部目录**；§5 的 8 个外部隔离项仍在，不能据通过宣称来源零遗漏。

机器校验：`python3 scripts/validate_research.py --report papers/2026/04/02/README.md` 与 scoped `git diff --check` 均通过；工具结果不替代上述语义审计。
