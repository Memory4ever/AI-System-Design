# Daily Research — 2026-04-02

**规范：** V3
**窗口：** 2026-04-01T09:00:00+08:00 ～ 2026-04-02T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-13T17:20:07+08:00
**补充窗口：** 2026-04-01 ～ 2026-04-01
**冻结候选日期：** [补查前原报告](../_sources/daily-20260402/baseline-before-supplement-20261013.md)
**窗口说明：** 用户授权只补既有 Daily 的来源遗漏；原窗口、25 个候选的身份/日期/评分和连续 §4 保持不变，新增仅检查前一完整北京时间自然日。旧完成与复核声明只指原轮，不能作为本轮验收。

原窗口左闭右开；原轮候选、证据与 Books 判断保留。本轮补查完整六部分独立语义验收通过。2026-10-13 用户在今日日报验收后明确恢复，本次只接本日未决层，不扩发现或新日期。外部材料限制不支持“零遗漏”断言。

## 1. 结论

本轮补查正式115个唯一家族＝原25冻结＋确定新增90：新增46项真实整合/独立写后复核、22项具体已有覆盖、12项中心争议隔离、10项仅报告/最低关闭。514身份线索/191精确题摘是已停止范围，不是候选或全文审阅分母；[本日记录§8.2及独核§9](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)保具体筛选/日期/Source/owner依据。所有可执行Source、日期和Books差额已到安全终态，完整六部分独立语义复核通过，普通待办0。15个必要首公开资格及7个机构历史入口继续隔离，不评分/候选/Books或无遗漏断言；PolarQuant/ReproMIA正式撤回仍不入选。原窗口/25整行和连续原§4保持。

本次新增的关键认识是把“可测、可生成”继续推进到具体消费者：HIRE的编辑gate与Concept的任务Fisher几何分别限定干预资格和方向关系，不能成为语义真值（[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)、[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)）；DIAL/Latent与AutoWorld分别交接自产future、循环slot和动态occupancy，训练可见真实未来不替部署预测及动作验收（[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)、[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)）。VecAttention的selector、attention与TTFT分母，以及FED的reference归一幅度与编辑语义，又要求把局部代理收益放回完整执行/评价对象，保留反退和全费用后再作选择（[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)、[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)）。

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
| `SRC-ANTHROPIC` | [Research](https://www.anthropic.com/research)原站 `publishedOn`；补窗UTC03-31 16:00～04-01 16:00内为 [How Australia uses Claude](https://www.anthropic.com/research/how-australia-uses-claude)，03-31T22:17Z＝04-01北京时间06:17。原文核心是地区使用/经济情况，范围关闭已独核；下一条 emotion concepts 为04-02T10:56Z，窗外不扩读。 | 已检查 | 限此历史目录，不证明机构作者未列论文/GitHub无事件；分层样本为目录原值[4]的题摘/范围判，不授全历史召回。 |
| `SRC-GOOGLE-AI` | [Research 2026-04 Blog](https://research.google/blog/2026/04/)最早为 04-03；[DeepMind Publications](https://deepmind.google/research/publications/)按日期倒序首页 04-22 直接到 03-22，未列本窗条目；[Google Research Publications](https://research.google/pubs/)按年度/领域组织、2026 年 357 项，未给日级 first-public。 | 受阻 | 两个有日期的原始目录已核；Google Research Publications 缺可界定本窗的日期/分页接口，不能从 2026 年份或当前列表推断本窗零发布。恢复条件是官方精确发布索引或具体论文链接/首次公开事件。 |
| `SRC-META-AI` | [AI at Meta Blog](https://ai.meta.com/blog/)可见 04-08 与 03-26 相邻；[Research](https://ai.meta.com/research/)动态目录无法从可读静态页形成完整历史停点。 | 受阻 | 已隔离：Blog 所见邻近日期不证明 Research 零发布；仅隔离该动态目录，取得当窗官方原文/可检索历史索引时重开。 |
| `SRC-QWEN` | [Research](https://qwen.ai/blog)的官方 `GET https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US` 返回40动态项；补窗相邻为03-30 Qwen3.5-Omni→04-02 Qwen3.6-Plus，未列04-01項。60旧静态项的原轮具名有效证可复用；[Qwen3.6-Plus](https://qwen.ai/blog?id=qwen3.6)官方04-02T04:00+08、能力披露/`preserve_thinking`版本事实保留原轮，不移入补窗。 | 已检查 | 限该官网 Research目录，不推断作者arXiv与仓库全部事件无更新。 |
| `SRC-DEEPSEEK` | [Research & News](https://deepseek.com/en/news/)本轮首页恢复可读，News04-24→2025-12-01、Research06-24→02-25；原轮完整目录曾HTTP429，本轮首页恢复不证明 `View All` 完整历史恢复。 | 受阻 | 完整动态列表仍未形成历史终点；仅隔离该入口未见的当窗事件，不以首页间隔证明全站零命中。恢复条件为官方完整历史目录或该窗口原始文章链接。 |
| `SRC-MOONSHOT` | [Kimi Blog](https://platform.kimi.com/blog)可见归档仅到 2025-11；官方组织仓库排序页查至 100 个 repo，未见当窗新建；定点核 [checkpoint-engine releases](https://github.com/MoonshotAI/checkpoint-engine/releases) 19 个（2026-02-02→06-08 相邻）、[Kimi-K2.5 releases](https://github.com/MoonshotAI/Kimi-K2.5/releases)空，无该窗重大 release。 | 受阻 | 已隔离：Blog 不提供 2026 完整档案；repo 检查限上述入口，不把无新增 release 扩为所有仓库无事件。未列研究正文待具体身份重开。 |
| `SRC-TENCENT-HUNYUAN` | [研究“全部”目录](https://hunyuan.tencent.com/research)的官方 `POST https://api.hunyuan.tencent.com/api/blog/publicList`，`pageNum=1,pageSize=100,renderType=0`，返回 9/9，04-23→02-13 之间无本窗条目。 | 已检查 | 限此完整目录，不覆盖机构作者未列 arXiv 或仓库 artifact。 |
| `SRC-ZAI` | [Research](https://www.zhipuai.cn/zh/research)的 [GLM-5V-Turbo原文](https://www.zhipuai.cn/zh/research/156)显示 `2026/04/01 16:00` 未标时区；完整核心只有CogViT/MTP/RL名词、30+tasks、榜单与展示，未给可复原新方法或受控归因，root具名贡献前EX已通过并复用。 | 已检查 | 限所见目录/本项核心，不授机构全部事件无更新；时区未核但不影响贡献前排除，不另列必要日期请求或评分/Books。 |
| `SRC-BYTEDANCE-SEED` | [Research/Blog](https://seed.bytedance.com/en/research)可见 04-11→01-27；[论文目录](https://seed.bytedance.com/en/public_papers)同站 `GET /api/get_article_list_v2`、`article_type=1,count=20,order_desc=true,page_token=40`、`x-tt-locale: US`，242 总条目；倒序页 04-07T16:00Z 紧接 03-31T12:00Z。 | 已检查 | 限这两个目录，不推断 Seed 作者未列论文或仓库没有本窗事件。 |
| `SRC-BAIDU-ERNIE` | [Blog](https://ernie.baidu.com/blog/zh/) 04-15→02-06，[Publication](https://ernie.baidu.com/blog/zh/publication/)当前四篇且无窗内标题；[PaddlePaddle/ERNIE releases](https://github.com/PaddlePaddle/ERNIE/releases)仅见 2025-06-30 的 `ernie-4.5`，本窗无 release。 | 已检查 | 本轮补04-01自然日，Blog日期精度足以按日核查；原轮09:00边界不确定不回填旧候选，也不构成本轮小时缺口。其它未列原始稿只凭具名首次正文重开。 |
| `SRC-XIAOMI-MIMO` | [Paper/Blog](https://mimo.xiaomi.com/)八篇 Paper 日期 06-29→03-13，Paper 无本窗项；[XiaomiMiMo/vllm](https://github.com/XiaomiMiMo/vllm/releases)与 [MiMo-V2-Flash](https://github.com/XiaomiMiMo/MiMo-V2-Flash/releases)公开 release 列表为空，组织 repo 排序页本窗无新建。 | 受阻 | 已隔离：Blog 目录约十四项不标日期，未能建立本窗全量时间边界；不以 Paper/release 零条代表 Blog 零发布，取得原始日期再重开。 |
| `SRC-MINIMAX` | [英文](https://www.minimax.io/blog)/[中文Blog](https://www.minimaxi.com/blog)相邻03-18→更晚条目；[cli releases](https://github.com/MiniMax-AI/cli/releases)补窗 `v0.4.0/0.4.1/0.4.2` 为04-01 09:03/11:14/11:20 UTC，原有效核心是状态栏/配额、JSON config/Node installer、CI上传修复，无新模型或系统机制，已按实际原核心与独核§9.13准入前关闭。AgentTechBlog本轮恢复三明确日期Sep19/Sep22/Oct8，均窗外。 | 受阻 | 已隔离：[AgentTechBlog](https://agent.minimax.io/docs/techblog)未列历史slice仍不能判零遗漏；不再沿用“所有条目未标日期”的旧描述，取得具体当窗dated原文时定点重开。 |
| `SRC-ARXIV` | 原轮 `2604` 25家族保留；本轮四主题query共211槽/181身份，12官方March分类在28768–30045标题切片及必要尾页共470身份，合并514线索；三批精确v1完整题摘191已读，宽列表不当贡献/全文队列，停止扩大。日期采用官方常规下界＋2603首次公告月月底上界＋无早正文反证的复合门，不以Submitted/created单独归日。 | 已检查 | 有限既存范围的贡献、normal/例外日期与必要证据/Books处置已闭合，十五具名资格保留仍隔离，不授全公告/互联网零遗漏；CRAFT/MPP及另外18点核共20同事件已root实际接纳，不重复分母/评分/写书。StepCache早提交与LongCat早仓库正文信号精确隔离，不倒迁旧候选或授无遗漏。 |

## 3. 候选与判断

下表先保留原轮冻结的 **25 个候选家族**，补充窗口已核新增随后列出，本轮确定新增90个家族，逐项实际采用与终态在§4。原25项公开时间栏保持 `2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00` 有界批次范围：它由官方公告计划、相邻 ID 切点及 pinned-v1 共同推定，**不是** arXiv 为每篇披露的秒级时刻；新增按已核 `04-01` 日期。若以后发现单篇延期公告等例外，只重开该项而非整体平移。旧稿按 DOI created 得到的评分作废。

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
| [PRoSFI — arXiv:2603.29500v1](https://arxiv.org/html/2603.29500v1) | 2026-04-01 | 模型完整生成类型化 scaffold 后再验证所提子命题，序列 reward 与自然语言忠实性分责；2 + 1 + 2 = 5。 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md)，producer/scaffold/verifier 接口，不授整段 soundness。 |
| [SNEAK — arXiv:2603.29846v1](https://arxiv.org/html/2603.29846v1) | 2026-04-01 | 同一 message 在已知/未知 secret 的双信息角色下分别测 utility 与 leakage，候选规模会改变代理口径；2 + 1 + 2 = 5。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，有限行为测量不授隐私/授权保证。 |
| [Mind the Gap / Active Learning — arXiv:2603.29677v1](https://arxiv.org/html/2603.29677v1) | 2026-04-01 | AULC差分与范围/尺度口径冲突限制“多模态查询不优”的可采用测量范围；3 + 1 + 2 = 6。 | 争议 | 暂缓：measurement中心隔离，不采用普遍active-learning无效或医疗判断，不写Books。 |
| [Drop the Hierarchy and Roles — arXiv:2603.28990v1](https://arxiv.org/html/2603.28990v1) | 2026-04-01 | 同任务protocol同时改变完成产出可见性、serial path与自选role，局部收益不能分配给“取消角色”单因素；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md)，信息可见性与coordination tax分验。 |
| [Baby Scale — arXiv:2603.29522v1](https://arxiv.org/abs/2603.29522v1) | 2026-04-01 | individual-child-scale data quality与grammar/semantic/world-knowledge scaling的局部观察；1 + 1 + 2 = 4。 | 已关闭 | 仅报告：完成身份/日期与最低关闭，不采用正面data-efficiency或人类学习结论。 |
| [Bilingual BabyLM — arXiv:2603.29552v1](https://arxiv.org/abs/2603.29552v1) | 2026-04-01 | matched100M-word GPT-2的mono/bilingual exposure regime局部对照；1 + 1 + 2 = 4。 | 已关闭 | 仅报告：不采用一般双语训练无代价或人类acquisition判断，不写Books。 |
| [MONA Camera Dropbox Extension — arXiv:2603.29993v1](https://arxiv.org/html/2603.29993v1) | 2026-04-01 | learned approval的零观测hacking仍可伴低intended behavior，参考array与新pilot必须分账；2 + 1 + 2 = 5。 | 标准完成 | 仅报告：受限低预算pilot不支持新长期保障机制，既有task/safety分验不需扩章。 |
| [Beta-Scheduling — arXiv:2603.28921v1](https://arxiv.org/html/2603.28921v1) | 2026-04-01 | gradient norm/跨optimizer重合不授repair-target选择；后续明确纠正选层主张，只重开该依赖；2 + 1 + 2 = 5。 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，magnitude/真实干预/非目标保留分验。 |
| [MetaCog — arXiv:2603.29693v1](https://arxiv.org/html/2603.29693v1) | 2026-04-01 | task discrimination、confidence效率与决策criterion分开；risk prompt也改变task sensitivity，不能独立归因风险偏好；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，discrimination/calibration/release utility及同rule支持量分验。 |
| [Tracking vs. Deciding: The Dual-Capability Bottleneck in Searchless Chess Transformers — arXiv:2603.29761v1](https://arxiv.org/html/2603.29761v1) | 2026-04-01 | 数据过滤/加权对board tracking与decision quality影响不同，零illegal不等实战quality；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md)，select/mix/weight、quality与coverage/update面分验。 |
| [Is my model perplexed for the right reason? Contrasting LLMs' Benchmark Behavior with Token-Level Perplexity — arXiv:2603.29396v1](https://arxiv.org/html/2603.29396v1) | 2026-04-01 | task performance与minimal-pair token差诊断分验，比例是逐token absolute差而非sequence PPL分解或causal importance；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，表现/读出与真实机制证据阶梯；metric细节仅报告。 |
| [Finite-time analysis of Multi-timescale Stochastic Optimization Algorithms — arXiv:2603.29380v1](https://arxiv.org/html/2603.29380v1) | 2026-04-01 | zeroth-order多时标误差传播有理论潜力，但fixed-smoothing/projection与tracking-to-rate链未闭；2 + 1 + 2 = 5。 | 争议 | 暂缓：中心理论资格终态隔离，不采用rate/algorithm guarantee或写Books，重开条件见§4。 |
| [ATP-Bench: Towards Agentic Tool Planning for MLLM Interleaved Generation — arXiv:2603.29902v1](https://arxiv.org/html/2603.29902v1) | 2026-04-01 | tool opportunity、planned precision、实际工具与最终utility分别测，invalid无图不能由低bad-image计数判好；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md)，实际有效证据/消费者outcome与visual tool utility分验。 |
| [Logging Like Humans for LLMs: Rethinking Logging via Execution and Runtime Feedback — arXiv:2603.29122v1](https://arxiv.org/html/2603.29122v1) | 2026-04-01 | developer-written gold与真正下游诊断效用分验，log-list/compiler/runtime critic是离线接口；2 + 1 + 2 = 5。 | 深入完成 | 整合：PLATFORM-LOGGING，[Ch68](../../../../books/part-06-ai-infrastructure/68-logging.md)；真实非作者POST已通过。 |
| [OmniRoam: World Wandering via Long-Horizon Panoramic Video Generation — arXiv:2603.30045v1](https://arxiv.org/html/2603.30045v1) | 2026-04-01 | 全景global preview由scale/visibility条件局部refinement恢复时间与分辨率；2 + 1 + 2 = 5。 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；真实非作者POST已通过。 |
| [Video Models Reason Early: Exploiting Plan Commitment for Maze Solving — arXiv:2603.30043v1](https://arxiv.org/html/2603.30043v1) | 2026-04-01 | same-denoise clean-state早筛种子与合法推进末帧链，不把motion代理当顺序正确；2 + 1 + 2 = 5。 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；真实非作者POST已通过。 |
| [Diffusion Mental Averages — arXiv:2603.29239v1](https://arxiv.org/html/2603.29239v1) | 2026-04-01 | 内部h逐t均值指导各noisy latent再经原DDIM，概念prototype与原mode分布分责；2 + 1 + 2 = 5。 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；真实非作者POST已通过。 |
| [OccSim: Multi-kilometer Simulation with Long-horizon Occupancy World Models — arXiv:2603.28887v1](https://arxiv.org/html/2603.28887v1) | 2026-04-01 | 静态ego-warp→visibility/masked completion分支，不授一般动力学或persistent场景身份；2 + 1 + 2 = 5。 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；真实非作者POST已通过。 |
| [EC-Bench: Enumeration and Counting Benchmark for Ultra-Long Videos — arXiv:2603.29943v1](https://arxiv.org/html/2603.29943v1) | 2026-04-01 | final count、instance list与timeline support分验，单interval不授逐实例faithfulness；2 + 1 + 2 = 5。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；真实非作者POST已通过。 |
| [Architecting Secure AI Agents: Perspectives on System-Level Defenses Against Indirect Prompt Injection Attacks — arXiv:2603.30016v1](https://arxiv.org/html/2603.30016v1) | 2026-04-01 | 未验证proposal中instruction recognition/provenance与follow授权分责，不授typed/self-report免注入；2 + 1 + 2 = 5。 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；真实非作者POST已通过。 |
| [PSPA-Bench: A Personalized Benchmark for Smartphone GUI Agent — arXiv:2603.29318v1](https://arxiv.org/html/2603.29318v1) | 2026-04-01 | 固定可行节点与偏好节点必须分别测，经验前后人口不等长期memory必要性；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。 |
| [StereoVGGT: A Training-Free Visual Geometry Transformer for Stereo Vision — arXiv:2603.29368v1](https://arxiv.org/html/2603.29368v1) | 2026-04-01 | geometry/PCA代理与真实disparity consumer不能互授兼容；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。 |
| [Seeing the Evidence, Missing the Answer: Tool-Guided Vision-Language Models on Visual Illusions — arXiv:2603.29428v1](https://arxiv.org/html/2603.29428v1) | 2026-04-01 | tool生成的annotation正确不等消费者答案正确；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md)。 |
| [When Can We Trust LLM Graders? Calibrating Confidence for Automated Assessment — arXiv:2603.29559v1](https://arxiv.org/html/2603.29559v1) | 2026-04-01 | 置信confidence、verdict与coverage-risk-utility需独立定义；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。 |
| [SceneTeract: Agentic Functional Affordances and VLM Grounding in 3D Scenes — arXiv:2603.29798v1](https://arxiv.org/html/2603.29798v1) | 2026-04-01 | profile-conditioned静态几何label不认证完整物理执行；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。 |
| [An Empirical Study of Multi-Agent Collaboration for Automated Research — arXiv:2603.29632v1](https://arxiv.org/html/2603.29632v1) | 2026-04-01 | 固定clock下worker/共享patch收益不能归给开放team拓扑；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md)。 |
| [Spontaneous Functional Differentiation in Large Language Models: A Brain-Like Intelligence Economy — arXiv:2603.29735v1](https://arxiv.org/html/2603.29735v1) | 2026-04-01 | norm/MMI代理与局部ablation不授脑经济或完整功能分化；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。 |
| [APEX-EM: Non-Parametric Online Learning for Autonomous Agents via Structured Procedural-Episodic Experience Replay — arXiv:2603.29093v1](https://arxiv.org/html/2603.29093v1) | 2026-04-01 | 训练内rich反馈收益不自动迁移到frozen heldout memory消费；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md)。 |
| [Theory of Mind and Self-Attributions of Mentality are Dissociable in LLMs — arXiv:2603.28925v1](https://arxiv.org/html/2603.28925v1) | 2026-04-01 | 自述mental attribution、局部refusal干预与ToM行为分验；2 + 1 + 2 = 5。 | 深入完成 | 已有覆盖：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。 |
| [Grokking From Abstraction to Intelligence — arXiv:2603.29262v1](https://arxiv.org/html/2603.29262v1) | 2026-04-01 | checkpoint bypass/CMS与BDM相关、非SGD surrogate分责；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。 |
| [Authorship Impersonation via LLM Prompting does not Evade Authorship Verification Methods — arXiv:2603.29454v1](https://arxiv.org/html/2603.29454v1) | 2026-04-01 | prompt风格模仿与个体authorship验证的局部反例；2 + 1 + 2 = 5。 | 深入完成 | 仅报告：具体采用边界见§4，不写Books。 |
| [Target-Aligned Reinforcement Learning — arXiv:2603.29501v1](https://arxiv.org/html/2603.29501v1) | 2026-04-01 | off-policy target残差选择改变replay人口但不授普遍recency保证；2 + 1 + 2 = 5。 | 标准完成 | 仅报告：具体采用边界见§4，不写Books。 |
| [SHIFT: Stochastic Hidden-Trajectory Deflection for Removing Diffusion-based Watermark — arXiv:2603.29742v1](https://arxiv.org/html/2603.29742v1) | 2026-04-01 | output重生成可改变trajectory-watermark检测资格但语义代理非无损；2 + 2 + 2 = 6。 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，output regeneration与detector/content身份分责。 |
| [The Spectral Edge Thesis: A Mathematical Framework for Intra-Signal Phase Transitions in Neural Network Training — arXiv:2603.28964v1](https://arxiv.org/html/2603.28964v1) | 2026-04-01 | rolling gradient Gram与weight spectrum/真实因果干预不是同对象；2 + 1 + 2 = 5。 | 标准完成 | 仅报告：具体采用边界见§4，不写Books。 |
| [6GAgentGym: Tool Use, Data Synthesis, and Agentic Learning for Network Management — arXiv:2603.29656v1](https://arxiv.org/html/2603.29656v1) | 2026-04-01 | proxy trace回放NS3不等policy在真实新观察下闭环transfer；2 + 1 + 2 = 5。 | 标准完成 | 仅报告：具体采用边界见§4，不写Books。 |
| [Calibrated Fusion for Heterogeneous Graph-Vector Retrieval in Multi-Hop QA — arXiv:2603.28886v1](https://arxiv.org/html/2603.28886v1) | 2026-04-01 | 官方last-support到terminal-hop纠错撤销旧metric正面采用资格；3 + 1 + 3 = 7。 | 争议 | 暂缓：具体中心结论隔离，不写Books，重开条件见§4。 |
| [The Model Says Walk: How Surface Heuristics Override Implicit Constraints in LLM Reasoning — arXiv:2603.29025v1](https://arxiv.org/html/2603.29025v1) | 2026-04-01 | paired约束测试与后续明确修订限制goal-decomposition正面采用；3 + 1 + 2 = 6。 | 争议 | 暂缓：具体中心结论隔离，不写Books，重开条件见§4。 |
| [Big2Small: A Unifying Neural Network Framework for Model Compression — arXiv:2603.29768v1](https://arxiv.org/html/2603.29768v1) | 2026-04-01 | INR重建参数的局部接口不满足普遍strict compression理论保证；2 + 1 + 2 = 5。 | 争议 | 暂缓：具体中心结论隔离，不写Books，重开条件见§4。 |
| [SeGPruner: Semantic-Geometric Visual Token Pruner for 3D Question Answering — arXiv:2603.29437v1](https://arxiv.org/html/2603.29437v1) | 2026-04-01 | 成熟saliency/3D distance采样的局部适配未支持新长期选择条件；1 + 1 + 2 = 4。 | 已关闭 | 仅报告：具体采用边界见§4，不写Books。 |
| [Structured Intent as a Protocol-Like Communication Layer: Cross-Model Robustness, Framework Comparison, and the Weak-Model Compensation Effect — arXiv:2603.29953v1](https://arxiv.org/html/2603.29953v1) | 2026-04-01 | structured intent的局部prompt人口不授跨模型protocol保证；1 + 1 + 2 = 4。 | 已关闭 | 仅报告：具体采用边界见§4，不写Books。 |
| [Impact of enriched meaning representations for language generation in dialogue tasks: A comprehensive exploration of the relevance of tasks, corpora and metrics — arXiv:2603.29518v1](https://arxiv.org/html/2603.29518v1) | 2026-04-01 | 多reference平均、demonstrator/reference重合与条件slot分母改变评价对象，不由完美拷贝授泛化；2 + 1 + 2 = 5。 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，reference聚合与目标/表达验收分责。 |
| [Hallucination-aware intermediate representation edit in large vision-language models — arXiv:2603.29405v1](https://arxiv.org/html/2603.29405v1) | 2026-04-01 | 训练factorized方向与第一层token gate分责，子空间/代理不授hall真值；2 + 1 + 2 = 5。 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。 |
| [AGFT: Alignment-Guided Fine-Tuning for Zero-Shot Adversarial Robustness of Vision-Language Models — arXiv:2603.29410v1](https://arxiv.org/html/2603.29410v1) | 2026-04-01 | 连续图文encoder用原soft关系target与student temperature分责，非语义保真；2 + 1 + 2 = 5。 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。 |
| [DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA — arXiv:2603.29844v1](https://arxiv.org/html/2603.29844v1) | 2026-04-01 | frozen native future target、双暖启和predfuture/action-loss joint交接，旁路与使用因果另验；2 + 2 + 2 = 6。 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。 |
| [LatentPilot: Scene-Aware Vision-and-Language Navigation by Dreaming Ahead with Latent Visual Reasoning — arXiv:2603.29165v1](https://arxiv.org/html/2603.29165v1) | 2026-04-01 | 跨step旧pilot读取/新slot覆盖，区分真实future训练与自产history消费；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Enhancing LLM-Based Bug Reproduction for Android Apps via Pre-Assessment of Visual Effects — arXiv:2603.29623v1](https://arxiv.org/html/2603.29623v1) | 2026-04-01 | 沙箱真实trial/screen-Activity后snapshot restore→有界搜索；2+2+2=6 | 深入完成 | 整合：AGENT-PLANNING / [Ch79](../../../../books/part-07-agent/79-planning.md) |
| [SkillReducer: Optimizing LLM Agent Skills for Token Efficiency — arXiv:2603.29919v1](https://arxiv.org/html/2603.29919v1) | 2026-04-01 | shadow routing与real trigger恢复/正文引用功能分验；2+1+2=5 | 深入完成 | 整合：AGENT-CONTEXT / [Ch75](../../../../books/part-07-agent/75-context.md) |
| [EcoScratch: Cost-Effective Multimodal Repair for Scratch Using Execution Feedback — arXiv:2603.29624v1](https://arxiv.org/html/2603.29624v1) | 2026-04-01 | 同gold/test probe联合选择evidence/opcap/verification预算；2+2+2=6 | 深入完成 | 整合：AGENT-WORKFLOW / [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Beyond Localization: Recoverable Headroom and Residual Frontier in Repository-Level RAG-APR — arXiv:2603.29067v1](https://arxiv.org/html/2603.29067v1) | 2026-04-01 | native/sharedbuilder、fixed pool与tokenmatched wrongconstraint诊断；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SemLoc: Structured Grounding of Free-Form LLM Reasoning for Fault Localization — arXiv:2603.29109v1](https://arxiv.org/html/2603.29109v1) | 2026-04-01 | typed anchor/per-test违反谱→一行patch/retest；2+1+2=5 | 深入完成 | 整合：AGENT-TOOL-CALLING / [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [An Explicit Surrogate for Gaussian Mixture Flow Matching with Wasserstein Gap Bounds — arXiv:2603.28992v1](https://arxiv.org/html/2603.28992v1) | 2026-04-01 | affine Gaussian-path kinetic surrogate/配对cost与exact W2条件分责；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Gloria: Consistent Character Video Generation via Content Anchors — arXiv:2603.29931v1](https://arxiv.org/html/2603.29931v1) | 2026-04-01 | 跨短clip的superset参考人口与global/view/expression弱位置条件，保GT四latent prefix到自产history交接；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [VecAttention: Vector-wise Sparse Attention for Accelerating Long Context Inference — arXiv:2603.29494v1](https://arxiv.org/html/2603.29494v1) | 2026-04-01 | Pq64/minS/fused index/vector gather/重新softmax接口；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Efficient Bilevel Optimization with KFAC-Based Hypergradients — arXiv:2603.29108v1](https://arxiv.org/html/2603.29108v1) | 2026-04-01 | outer IHVP/hypergradient逐层Kronecker surrogate与bias/damping/cadence接口；2+2+2=6 | 深入完成 | 整合：TRAIN-PRETRAINING / [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Metriplector: From Field Theory to Neural Architecture — arXiv:2603.29496v1](https://arxiv.org/html/2603.29496v1) | 2026-04-01 | input h配置operator/freshψ演化/readout分责；2+2+2=6 | 深入完成 | 整合：MODEL-TRANSFORMER-LAYER / [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [Think Anywhere in Code Generation — arXiv:2603.29957v1](https://arxiv.org/html/2603.29957v1) | 2026-04-01 | code-prefix中途thinking/strip后续代码消费接口；2+1+2=5 | 深入完成 | 整合：MODEL-SAMPLING / [Ch20](../../../../books/part-02-model/20-sampling.md) |
| [Self-Consistency for LLM-Based Motion Trajectory Generation and Verification — arXiv:2603.29301v1](https://arxiv.org/html/2603.29301v1) | 2026-04-01 | prototype×warp/100arc-points/ICP/DBSCAN/medoid消费接口；2+1+2=5 | 深入完成 | 整合：MODEL-SAMPLING / [Ch20](../../../../books/part-02-model/20-sampling.md) |
| [ASI-Evolve: AI Accelerates AI — arXiv:2603.29640v1](https://arxiv.org/html/2603.29640v1) | 2026-04-01 | literature cold-prior与full-run分析/持久context两人口分责；2+2+2=6 | 深入完成 | 整合：AGENT-MEMORY / [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Refined Detection for Gumbel Watermarking — arXiv:2603.30017v1](https://arxiv.org/html/2603.30017v1) | 2026-04-01 | fixed-generator centered clipped heavy-tail detector/样本条件；2+1+2=5 | 深入完成 | 整合：PLATFORM-SECURITY / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [From Density Matrices to Phase Transitions in Deep Learning: Spectral Early Warnings and Interpretability — arXiv:2603.29805v1](https://arxiv.org/html/2603.29805v1) | 2026-04-01 | 滑窗probe-loss covariance谱区分训练诊断与严格预警；2+2+2=6 | 争议 | 暂缓：中心严格预警条件未闭，不Books |
| [Benchmarking PhD-Level Coding in 3D Geometric Computer Vision — arXiv:2603.30038v1](https://arxiv.org/html/2603.30038v1) | 2026-04-01 | paper-context数量与codeconsumer所需事实/执行测量分责；1+2+2=5 | 标准完成 | 已有覆盖：AGENT-CONTEXT / [Ch75](../../../../books/part-07-agent/75-context.md) |
| [Not All Frames Are Equal: Complexity-Aware Masked Motion Generation via Motion Spectral Descriptors — arXiv:2603.29655v1](https://arxiv.org/html/2603.29655v1) | 2026-04-01 | gold谱训练到runtime自产谱的mask/attention交接；2+1+2=5 | 争议 | 暂缓：中心train/runtime接口未闭，不Books |
| [Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning — arXiv:2603.29038v1](https://arxiv.org/html/2603.29038v1) | 2026-04-01 | data filter、更新后行为/效用与probe资格分验；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-SECURITY / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [AutoWorld: Scaling Multi-Agent Traffic Simulation with Self-Supervised World Models — arXiv:2603.28963v1](https://arxiv.org/html/2603.28963v1) | 2026-04-01 | ego-compensated有效occupancy change训练重权→future local/global动作消费者；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [RAAP: Retrieval-Augmented Affordance Prediction with Cross-Image Action Alignment — arXiv:2603.29419v1](https://arxiv.org/html/2603.29419v1) | 2026-04-01 | top1 staticcontact与Kreference动态direction消费者分责；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [TrajectoryMover: Generative Movement of Object Trajectories in Videos — arXiv:2603.29092v1](https://arxiv.org/html/2603.29092v1) | 2026-04-01 | paired raydepth/hit-nohit人口的数据几何接口；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Concept frustration: Aligning human concepts and machine representations — arXiv:2603.29654v1](https://arxiv.org/html/2603.29654v1) | 2026-04-01 | taskBB-derived平均Fisher比较CBM/SAE方向与metric-label-head三身份；2+1+2=5 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [SparseDriveV2: Scoring is All You Need for End-to-End Autonomous Driving — arXiv:2603.29163v1](https://arxiv.org/html/2603.29163v1) | 2026-04-01 | Δs path×Δt velocity/coarse→joint recondition及丢失召回分责；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [FED-Bench: A Cross-Granular Benchmark for Disentangled Evaluation of Facial Expression Editing — arXiv:2603.29697v1](https://arxiv.org/html/2603.29697v1) | 2026-04-01 | reference-normalized edit magnitude与方向/保真分验；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [WybeCoder: Verified Imperative Code Generation — arXiv:2603.29088v1](https://arxiv.org/pdf/2603.29088v1) | 2026-04-01 | CHANGE修method→new obligation/name复用→全重构分责；2+2+2=6 | 深入完成 | 整合：AGENT-MULTI-AGENT / [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Fisheye3R: Adapting Unified 3D Feed-Forward Foundation Models to Fisheye Lenses — arXiv:2603.28896v1](https://arxiv.org/html/2603.28896v1) | 2026-04-01 | T/T^-1、teacher/GT三人口与camera类型token接口；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [The Surprising Effectiveness of Noise Pretraining for Implicit Neural Representations — arXiv:2603.29034v1](https://arxiv.org/html/2603.29034v1) | 2026-04-01 | noise-init fitting与inverse denoising消费者反向取舍；2+1+2=5 | 深入完成 | 整合：WORLDVIEW-WHY-MODELS-LEARN / [Ch4](../../../../books/part-01-worldview/04-why-models-learn.md) |
| [WorldFlow3D: Flowing Through 3D Distributions for Unbounded World Generation — arXiv:2603.29089v1](https://arxiv.org/html/2603.29089v1) | 2026-04-01 | actual coarse-source/newattribute Gaussian/hostchunk velocity合并接口；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Stepper: Stepwise Immersive Scene Generation with Multiview Panoramas — arXiv:2603.28980v1](https://arxiv.org/html/2603.28980v1) | 2026-04-01 | 固定训练位移/旋转输入与生成六面耦合→重建overlap消费者分责；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Extend3D: Town-Scale 3D Generation — arXiv:2603.29387v1](https://arxiv.org/html/2603.29387v1) | 2026-04-01 | overlap vector-field聚合、实际noise-strength与solver-start分责及occupancy/texture消费者分验；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Omni-NegCLIP: Enhancing CLIP with Front-Layer Contrastive Fine-Tuning for Comprehensive Negation Understanding — arXiv:2603.29258v1](https://arxiv.org/html/2603.29258v1) | 2026-04-01 | present/absent事实前提→不同image-text训练关系与caption-margin分责；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Adversarial Prompt Injection Attack on Multimodal Large Language Models — arXiv:2603.29418v1](https://arxiv.org/html/2603.29418v1) | 2026-04-01 | 小pixel/clean图像不授来源可信，生成target text与真实action效用分验；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |

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

### [PRoSFI — arXiv:2603.29500v1](https://arxiv.org/html/2603.29500v1)

必要精确v1 §3–4/§5.1–5.4/§5.6的有效Source复用；model-emitted id/dependencies/conclusion/rule scaffold不打断rollout，完成后才提取形式命题验证，最高reward要求终局正确和全部所提步骤通过。RewardHit不包括遗漏的自然语言步骤，GPTSoundness也只是另一代理；Hard direct-Lean对照并不全面劣于outcome。769训练题、Qwen2.5-7B、8×Hopper、960steps及CPU验证/翻译/判分总费边界保留，不授异步净吞吐、完整soundness或复现。[必要证据](../_sources/daily-20260402/SUP_PROSFI_REVIEW_20261013.md)保留双方，正常复合日门与owned注册上界见[原日期字段](../_sources/daily-20260402/SUP_FIVE_CURRENT_DATE_20261013.json)。

真实 `2+1+2=5`，因长期producer/verifier接口缺口加深必要命题。Books Decision为 **Integrate：TRAIN-RLHF / Ch31**；在reference-derived curriculum后增加一段，不改GRPO估计器。2026-10-13恢复后root/reader逐字PRE与当前邻接通过才授窄锁，作者实际按[PRE](../_sources/daily-20260402/SUP_PROSFI_PRE_20261013.md)写入一段及本人末注；`/root/resume_apr02_review`实际nonwriter POST通过、root接纳释放锁，全部并发tail保留，不授本日DAY。

### [SNEAK — arXiv:2603.29846v1](https://arxiv.org/html/2603.29846v1)

精确v1必要§2–4/6的有效Source复用：同一消息由已知secret的合作者识别提示、未知secret的观察者从候选词猜secret，分别按chance归一、零截断并取utility×(1−leakage)。这只测有限候选下行为概率，不是互信息、不可推断或访问授权；候选词/decoy数量均改变分数。1394题/117类别、10–12候选/5decoy/≤5词/单轮、三evaluators和有限human一致性只校准该代理，更多test-time scaling仍可能退步；多候选生成和双角色判分都付费，不授实现核验或复现。[必要原件](../_sources/daily-20260402/SUP_SNEAK_CORE_20261013.json)和[日期字段](../_sources/daily-20260402/SUP_FIVE_CURRENT_DATE_20261013.json)保留具体范围。

真实 `2+1+2=5`，因EvalSpec缺该双信息状态测量差额加深。Books Decision为 **Integrate：PLATFORM-EVALUATION-SYSTEM / Ch66**；只在EvalSpec后、GDPval前增加一段和本人末注。[逐字PRE](../_sources/daily-20260402/SUP_SNEAK_PRE_20261013.md)经root/reader实际当前锚与邻接核验后授窄锁，作者落实，`/root/resume_apr02_review`实际nonwriter POST通过并由root接纳释放锁；原GDPval/native artifact及当前所有末注保留，不授本日DAY。

### [Mind the Gap / Active Learning — arXiv:2603.29677v1](https://arxiv.org/html/2603.29677v1)

原reader实际必要§3–5和§6.1/.2的measurement中心D由resume reader及root未变层复用。AULC差分telescoping与所报范围/表8.91不协调，partial×10与joint不同尺；不否认条件化benchmark本身的准入潜力，却不能据这些口径签普遍multimodal-query无效。真实纠错 `3+1+2=6`，单benchmark/有限长期pitfall不虚增7；[原core](../_sources/daily-20260402/SUP_DECIDER_2603-29677v1_20261013.json)、[必要评价](../_sources/daily-20260402/SUP_ACTIVE_EVAL_20261013.json)保留两侧，FIVE_CURRENT_DATE正常复合日门经root独核通过。**中心争议／Books暂缓**；重开只需统一AULC定义、范围/scale与对应重新可比的评价，未采用医疗或一般AL判断，不扩读附录/代码。

### [Drop the Hierarchy and Roles — arXiv:2603.28990v1](https://arxiv.org/html/2603.28990v1)

作者与resume reader实际精确v1必要S3–6。Coordinator先assign再parallel、Sequential依次读完成产出并自选角色、Broadcast读意向、Shared读旧角色memory，这些同时改可见信息、critical path和调用预算；合成任务的LLM judge高分不能把pre-assigned role一律叫anti-pattern。120任务/三强模型局部比较、Series judge/模型/agent数与任务变化、20810的实验总数与摘要25000不协调、ratelimit survivor及O(N)时延全保；无real-workflow人审或等全费保证。[必要原件](../_sources/daily-20260402/SUP_RESUME_CORE_2603-28990v1_20261013.json)及[当前normal/owned上界](../_sources/daily-20260402/SUP_RESUME_DATE_2603-28990_20261013.json)支持有限层。

真实 `2+1+2=5`。Books具体已有覆盖：Ch82 60–90拆task-dependent topology/可见信息/coordination tax与外围processor，136–164拆supervisor视图与run-local职责，178–184拆初稿/feedback/修订品可见性及相同轮数不等global budget。resume reader实际完整这些邻接接纳NC，不把主题关联当覆盖，不写重复通用roles段。

### [Baby Scale — arXiv:2603.29522v1](https://arxiv.org/abs/2603.29522v1)

两篇完整精确题摘的局部学习/数据边界通过准入校准，各 `1+1+2=4`，按最低审阅投入关闭。不是以children或small-model范围外排除，也不将摘要的grammar/knowledge scaling、data-quality关联或mono/bilingual未见强差异提升为训练因果/人类学习机制。current official event身份、常规提交下界及2603首次公告月/owned Apr1注册上界见[Baby原字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29522_20261013.json)与[Bilingual原字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29552_20261013.json)；Bilingual后v2仅身份，不倒灌。未据它们提出新长期recipe，Books仅报告，不假称完整实验已审。

### [Bilingual BabyLM — arXiv:2603.29552v1](https://arxiv.org/abs/2603.29552v1)

本项独立家族真实 `1+1+2=4`，最低关闭而非普通EX；题摘的matched100M-word/GPT-2暴露条件仅保留为局部观察，不采用双语无代价、人类acquisition或任何长期recipe。身份/版本/正常复合日门与不作进一步采用的边界见上段及[本项原字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29552_20261013.json)，未做标准或深入实验审阅，Books仅报告。

### [MONA Camera Dropbox Extension — arXiv:2603.29993v1](https://arxiv.org/html/2603.29993v1)

resume reader实际必要S5–8/10–11 Source5：原ordinaryRL/oracle结果是released reference arrays，不是本次新PPO复现；learned-approval局部pilot在单seed/1536步下零观测hacking却仅.119 intended behavior、return −.363，不能把停滞也当可靠完成。CNN、Vec4、rewardnorm/预算改变，没有同预算全条件可靠比较；[精确原件](../_sources/daily-20260402/SUP_RESUME_CORE_2603-29993v1_20261013.json)保留builder proposal、负侧与全部费用，身份/normal复合日门原值见[当前事件](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29993_20261013.json)。真实 `2+1+2=5` 只评learned-approval下的具体反证。

Books **仅报告**：该pilot没有支持新的长期防hacking机制，不能以“zero hacking”签learned approval保障；Ch31 424–444的代理与独立task/safety分验、Ch66 66 always-abstain零utility基线已限制这种推断，resume reader已实际核。未核代码/arrays重跑或all training，保留仅此人口的观察而不否认MONA原理论条件。

### [Beta-Scheduling — arXiv:2603.28921v1](https://arxiv.org/html/2603.28921v1)

作者与resume reader实际v1 S3/5/6/10，仅为影响采用的具名纠错再读currentv3 S8。v1自明unit-curvature与clamp[.5,.99]，不支持任意loss的普遍critical schedule；error样本gradient norm高及SGD/Adam三个layer重合不等architecture causal bottleneck。单seed42/ResNet18CIFAR10的SGD修62错却新55错、Adam修146新148，且epochs×layers的82%不是实测端到端compute。currentv3明确用35组合对照替换选层主张；此Jul更正只撤销原diagnostic的积极选择权限，不搬later rank/性能数进Apr1结果。原件分别为[v1必要内容](../_sources/daily-20260402/SUP_RESUME_CORE_2603-28921v1_20261013.json)、[current纠错必要段](../_sources/daily-20260402/SUP_RESUME_CORE_2603-28921v3_20261013.json)和[事件说明](../_sources/daily-20260402/SUP_RESUME_DATE_2603-28921_20261013.json)；无需全版本/附件/代码。

真实 `2+1+2=5`，因为具体纠错加深受影响命题。Books具体已有覆盖：Ch66 311–339的325段分开magnitude、可验证干预与非目标保留，并要求匹配random/control，不能由最大signal批准干预。resume reader实际完整邻接/必要原件独核通过NC，不为这个局部反例新增通用原则段，也不采LLM迁移、所有优化无效或后版保障。

### [MetaCog — arXiv:2603.29693v1](https://arxiv.org/html/2603.29693v1)

作者与resume reader实际必要S2–4，真实 `2+1+2=5`：type-1 dprime、meta-dprime/dprime效率与criterion不是同一评价对象，equal-variance Gaussian与ordered criteria是假设，不是模型真实belief或calibrated posterior。Risk prompt同时改变dprime，不能把差额独立归因criterion。三binary任务、同prompt五点confidence/newconversation的局部测量保留；Figure1的2e3/1e3与Methods2e4/1e4人口不协调、ROPE/CI/稀少bin处理及全部调用费均不省，不采gold-standard、模型排行或真实deployment hazard。精确[v1必要原件](../_sources/daily-20260402/SUP_RESUME_CORE_2603-29693v1_20261013.json)与[当前事件/复合日门原值](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29693_20261013.json)可复查，未核代码或复现实验。

Books具体已有覆盖：Ch66 54–72、842–866将discrimination、calibration与release utility分开；1338–1351限定同rule下valid support，已承载本次拟采用的测量分责。Resume reader已实际核完整局部与Source，NC通过；psychophysical公式和局部观察只保报告，不因新指标自动扩章。

### [Tracking vs. Deciding: The Dual-Capability Bottleneck in Searchless Chess Transformers — arXiv:2603.29761v1](https://arxiv.org/html/2603.29761v1)

作者与resume reader实际v1 S3–6必要层，真实 `2+1+2=5`：过滤与错误位置加权分别改变训练人口和objective，不将board合法性proxy当decision quality。28M/120M同时变化10M/50M数据与2.5h/70h训练，不授纯capacity定律；within-size的20:1局部加权对照保留，但200:1亦加数据，不能读成固定预算普遍sweet spot。V2.3是100M而非V2.2的50M，offline零illegal仍伴实际游戏退步，原文tracking-bottleneck解释没有直接隔离；`P=min(T,Q)`、log-depth scaffold和按严重错定义的degeneration对齐不授独立预测或因果。精确[原件](../_sources/daily-20260402/SUP_RESUME_CORE_2603-29761v1_20261013.json)与[normal日门原值](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29761_20261013.json)保留限定人口、预算和反侧，不采用人类风格§7或大LLM外推，未核代码/复现。

Books具体已有覆盖：Ch27 151–178的immutable select/mix/weight算子和247–278的quality/coverage/不同update面已承载本项拟采用的分责；resume reader实际完整局部独核NC通过。不是因为chess任务名或Books主题相似而关闭，不为局部观察另造并列配方。

### [Is my model perplexed for the right reason? Contrasting LLMs' Benchmark Behavior with Token-Level Perplexity — arXiv:2603.29396v1](https://arxiv.org/html/2603.29396v1)

作者/reader实际v1 S2–4与raw AppendixA worked example，Source5通过。`total ΔPPL`明确是逐token absolute差之和，plain比例不是两条sequence geometric-PPL的恒等分解；normalized另用signed差除totalabs、取pivotal mean减all-token median。因此不能因PPL非additive判整个诊断失效，但也不能把它称作causal importance：token重排后reindex不取消prefix条件变化，period差、pivotal定义与整句意义共同影响；低比例不唯一证明模型靠错误heuristic。4×2 prompt、5类任务、多模型及重复token/totalzero未闭边界保留，±1/“entire解释”不作保证。精确[原件](../_sources/daily-20260402/SUP_RESUME_CORE_2603-29396v1_20261013.json)及[日门](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29396_20261013.json)可复查；AppendixA在同名raw，未因json解析漏appendix视作外部不可得。

Books具体已有覆盖：作者与reader实际Ch5 270–313区分task表现、读出/局部诊断与干预后的真实downstream机制，限定NC通过。新指标的具体公式与局部观察仅报告，不授LLM内部原因真值或全部linguistic-cue缺失。

### [Finite-time analysis of Multi-timescale Stochastic Optimization Algorithms — arXiv:2603.29380v1](https://arxiv.org/html/2603.29380v1)

真实 `2+1+2=5` 保理论潜力而非普通EX。reader实际S3–6必要理论链，作者non-preparer实际回核S3/S4、S5受影响recursion/Theorems3–4与S6：compact范围内的有限ergodic Markov/C3条件不自动控制Gaussian扰动出界；fixedβ=.05未闭smoothed到真实gradient的bias。Alg1的b/c指数与Assumption3互换、perturbβ遗漏、offdiagonal多−1与Eq2不同；投影Γ仍用unprojected gradient FOSP，边界stationarity对象不协调。Theorem1/3 growing-error式与后文decay不一致，min expected gradient bound也不授全部iterate收敛。MountainCar的diagonal Hessian、custom无限长/no-reset与五seed局部观察不证明新rate或大模型训练保证。支持/关键反侧已足，未全附件/代码复核。[精确原件](../_sources/daily-20260402/SUP_RESUME_CORE_2603-29380v1_20261013.json)和[日门](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29380_20261013.json)保留。

Books暂缓/终态隔离：不采用O(t^-0.4)、普遍算法优越或写Books。重开只需明确fixedβ偏差/outside-C矩条件、修正伪码与时标、projected stationarity目标及一致tracking-error→final-rate证明链；不要求无关全proof或全部附件。

### [ATP-Bench: Towards Agentic Tool Planning for MLLM Interleaved Generation — arXiv:2603.29902v1](https://arxiv.org/html/2603.29902v1)

作者/reader实际v1 S3–7与raw B.2/Table11，Source5通过。7,702查询、八category/25intent/五tools的MAM分别评necessity/schema/placement与missed opportunities，planning SR没有全工具执行；GT tool set是参考而非唯一trace。800小批换judge、400报告人工agreement及model-rank相关不认证逐例真值。B.2每model100 responses实际执行Reference/nano-banana/SerpAPI/GPT5 code/Seedream4 edit；invalid不生成图导致低inappropriate-image计数，仍可低utility。其FS1–5与MAM0–100、MI和实际outcome不合成一个成功标签。Tool-boundary prompt改变selection，三shot/annotation/judge/生成/工具与全成本仍付费，未披露完整hardware/latency，不采排行或end-to-end免费保证。见[精确原件](../_sources/daily-20260402/SUP_RESUME_CORE_2603-29902v1_20261013.json)及[日门](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29902_20261013.json)；B.2在同名raw。

Books具体已有覆盖：作者与reader实际Ch78 238–267分别承载工具可达/调用/有效证据/按证修改/终局、visual-call utility与消费者answerability，限定本项planning不授execution、低bad count不授utility的采用NC通过。MAM的特殊指标及局部ranking只保报告，不新增通用judge配方。

### [Logging Like Humans for LLMs: Rethinking Logging via Execution and Runtime Feedback — arXiv:2603.29122v1](https://arxiv.org/html/2603.29122v1)

必要精确v1 §3–5/7 的已独核Source5复用，真实 `2+1+2=5` 只评本项具体接口；支持、反侧与全部费用不因恢复丢失。

Schema 可查不等于日志足以诊断，像开发者原有日志也不等于更有用。一个离线插桩分支让模型只提议带插入行号的日志清单，重插原程序后先过编译，再让 critic 依据实际运行日志提出 traceability、state visibility 与 causal-linkage 的缺口，有界增删日志并重验；评价检查有源码时的定位/修复与无源码时的定位，而非只测日志文本相似度。[ReLog 的受限对照](https://arxiv.org/html/2603.29122v1)支持这个效用接口，critic 的“足够”仍非因果真值，原逻辑不被重生成也不保证插桩无副作用或时序扰动。五轮上限、复跑/编译、日志生成和诊断判分都付费；311/225个Java故障人口与语义等价判分不认证开放环境、等预算净收益或production安全。执行不可复现、代理未校准或日志暴露敏感信息时，保留原结构化日志、定点人工插桩与独立测试/排障，不由较高诊断F1批准在线自动改程序。

Books **整合：PLATFORM-LOGGING**；[逐字PRE](../_sources/daily-20260402/SUP_RELOG_PRE_20261013.md)和[必要独核及真实POST](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)可复查。实际一段与本人末注已落实，独立写后复核通过。普通paper-v1复合日门有效层复用，原值见[事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29122_20261013.json)；未核代码、复现或生产。

### [OmniRoam: World Wandering via Long-Horizon Panoramic Video Generation — arXiv:2603.30045v1](https://arxiv.org/html/2603.30045v1)

必要精确v1 §3.1–3.3/4.1–4.4 的已独核Source5复用，真实 `2+1+2=5` 只评本项具体接口；支持、反侧与全部费用不因恢复丢失。

还有一条面向全景长视频、而非seed筛选的global-local分支：在近恒速、固定朝向的数据条件下，以位移方向与全局scale先产生较快的全程全景preview，再按scale与稀疏可见条件分段refine，恢复目标速度、时间步与分辨率。Preview提供共同的长程条件，不拥有最终像素或真实环境状态；局部refiner仍须分别验质量、跨段衔接与轨迹控制。[OmniRoam的受限对照](https://arxiv.org/html/2603.30045v1)支持这一路线，却不证明任意旋转运动、metric geometry或场景身份永久一致；首尾CLIP-loop比值也受中途相似度分母影响，不能当闭环世界真值。两阶段训练、preview、各段refinement和最终解码均付费，较短preview与完整长序列的质量不能拼成同一指标。相机条件失配、局部细节影响全局路径或段间漂移时，保留原HR/较短视频、重新观测或重新生成全局条件，不从preview快推出整条实时交付。

Books **整合：MULTIMODAL-GENERATIVE-PARADIGMS**；[逐字PRE](../_sources/daily-20260402/SUP_OMNIROAM_PRE_20261013.md)和[必要独核及真实POST](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)可复查。实际一段与本人末注已落实，独立写后复核通过。普通paper-v1复合日门有效层复用，原值见[事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-30045_20261013.json)；未核代码、复现或生产。

### [Video Models Reason Early: Exploiting Plan Commitment for Maze Solving — arXiv:2603.30043v1](https://arxiv.org/html/2603.30043v1)

必要精确v1 §3–7 的已独核Source5复用，真实 `2+1+2=5` 只评本项具体接口；支持、反侧与全部费用不因恢复丢失。

预览也可以保持原分辨率，只提前停止大多数种子的去噪：在固定probe步解码当前clean-state估计，以任务相关轨迹代理排名，仅让少数种子完成原采样，再验终态。它不等于早期画面已经正确，motion-energy一致性也不认证路径顺序；[受限maze对照](https://arxiv.org/html/2603.30043v1)支持早筛与最终检查的分责，却不能由路径长度相关性签唯一失败原因。若单段生成不足，可只把未违规且确有向目标推进的末帧用作下一段条件；没有合法推进就停止，而非把生成画面当真实环境反馈。每个probe的VAE解码、候选判断及每层chain采样都付费，max-three chaining对照的总预算也高于单轮best-of-N，不能把长链7→67当单模块免费增益。早期排名不稳、约束被视觉作弊绕过或链式误差放大时，保留完整种子采样、更短任务与独立终态验证，不由低NFE或稳定计划批准物理动作。

Books **整合：MULTIMODAL-GENERATIVE-PARADIGMS**；[逐字PRE](../_sources/daily-20260402/SUP_VIDEO_PRE_20261013.md)和[必要独核及真实POST](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)可复查。实际一段与本人末注已落实，独立写后复核通过。普通paper-v1复合日门有效层复用，原值见[事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-30043_20261013.json)；未核代码、复现或生产。

### [Diffusion Mental Averages — arXiv:2603.29239v1](https://arxiv.org/html/2603.29239v1)

必要精确v1 §4–6 的已独核Source5复用，真实 `2+1+2=5` 只评本项具体接口；支持、反侧与全部费用不因恢复丢失。

如果目标不是匹配整个分布，而是生成同一条件下的一个概念原型，还可让多个种子的去噪轨迹收敛：每个时间步先平均所选内部层的表示，再分别优化当前noisy latent靠近该均值，随后由原DDIM推进；达到cutoff后只做普通去噪，最终才用VAE解码。[DMA的受限方法](https://arxiv.org/html/2603.29239v1)避免把不可直接解码的feature均值当图像，却也会压掉少数mode，原型稳定并不等于恢复真实概念分布或模型bias真值。外部encoder聚类后再回到各latent分组，需要另校准conditioning；TI/LoRA与不同CFG/训练预算的比较不独占mode恢复因果，也不证明clusters给定后无偏。内部层、时间网格、seed人口、cutoff和condition都应冻结，大量latent优化、完整采样、聚类及适配均计费，same-seed pool不等总预算。模式覆盖、层语义或代理representativeness不可靠时，保留普通样本分布、逐簇检查与独立人工锚点，不用一个清晰的平均原型替代多样性或公平性验收。

Books **整合：MULTIMODAL-GENERATIVE-PARADIGMS**；[逐字PRE](../_sources/daily-20260402/SUP_DMA_PRE_20261013.md)和[必要独核及真实POST](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)可复查。实际一段与本人末注已落实，独立写后复核通过。普通paper-v1复合日门有效层复用，原值见[事件字段](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md#81-明确恢复后的作者实际层2026-10-13)；未核代码、复现或生产。

### [OccSim: Multi-kilometer Simulation with Long-horizon Occupancy World Models — arXiv:2603.28887v1](https://arxiv.org/html/2603.28887v1)

必要精确v1 §3.1–3.3/4.1–4.3/6.1/10 的已独核Source5复用，真实 `2+1+2=5` 只评本项具体接口；支持、反侧与全部费用不因恢复丢失。

静态occupancy的观察生成还可把这条分解落实成补全问题：在已知、受限的平面ego motion下，先将上一时刻latent刚体传播到下一坐标系，再用几何可见性与训练期随机遮蔽形成不完整条件，由生成器补全下一latent；waypoint也须在同一目标坐标系对齐，不能让简单复制冒充长期变化预测。这里学习的是warp与可见条件下的静态场景补全，不是一般交通动力学；latent旋转与插值不保证无损，分布相似也不证明同一个未见场景身份一直被保存。[OccSim的有限对照](https://arxiv.org/html/2603.28887v1)仅在给定静态AE空间、平面运动与训练人口中支持该接口，随机mask、token条件与辅助loss共同变化，不能独归一个组件；动态layout仍由另一路生成和规则运动驱动。AE、warp、补全训练/采样与长rollout校验都付费，条件旋转失配、遮挡历史不足或质量回归时，保留真实重观测、显式静态地图或已验simulator，缩短horizon，而非由长期FID批准物理行动。

Books **整合：MULTIMODAL-WORLD-MODELS**；[逐字PRE](../_sources/daily-20260402/SUP_OCCSIM_PRE_20261013.md)和[必要独核及真实POST](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)可复查。实际一段与本人末注已落实，独立写后复核通过。普通paper-v1复合日门有效层复用，原值见[事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-28887_20261013.json)；未核代码、复现或生产。

### [EC-Bench: Enumeration and Counting Benchmark for Ultra-Long Videos — arXiv:2603.29943v1](https://arxiv.org/html/2603.29943v1)

必要精确v1 §3–5 的已独核Source5复用，真实 `2+1+2=5` 只评本项具体接口；支持、反侧与全部费用不因恢复丢失。

视频中的聚合答案也需拆开：计数正确，不等于列出的实例集合正确，更不等于原时间轴上的证据支持这些实例。评价可同时保存最终数值的exact/误差、列表匹配的precision/recall与原媒体的support spans，明确漏项、重复项、judge匹配和时间采样各自的人口；只有任务本来只消费一个数时，原标量检查才足够。[EC-Bench的受限协议](https://arxiv.org/html/2603.29943v1)把enumeration/counting与时间支持分验，但其多span折成单interval的tIoU不能验逐实例对应、间隙或顺序，模型judge与整体相关也不证明过程faithfulness。长视频帧采样、ASR转录、实例/时间标注、匹配和额外输出都付费；先列实例再计数的局部改善，不能在没有同预算控制时独归grounding。列表身份、时间支持或标签资格不可信时，回读原视频/转录、补独立标注或保留Unknown，不以最终数值碰巧正确批准完整证据链。

Books **整合：PLATFORM-EVALUATION-SYSTEM**；[逐字PRE](../_sources/daily-20260402/SUP_EC_PRE_20261013.md)和[必要独核及真实POST](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)可复查。实际一段与本人末注已落实，独立写后复核通过。普通paper-v1复合日门有效层复用，原值见[事件字段](../_sources/daily-20260402/SUP_CIVIC_MACTOK_EC_DATE_20261013.json)；EC另有限early-project反证已闭合，不授artifact同日首次公开。未核代码、复现或生产。

### [Architecting Secure AI Agents: Perspectives on System-Level Defenses Against Indirect Prompt Injection Attacks — arXiv:2603.30016v1](https://arxiv.org/html/2603.30016v1)

必要精确v1 II/III/IV 的已独核Source5复用，真实 `2+1+2=5` 只评本项具体接口；支持、反侧与全部费用不因恢复丢失。

一条尚未验证的设计proposal，是进一步把“模型认为自己要遵循什么”与“系统准许遵循什么”分开：要求模型显式列出拟遵循指令，由系统回指其来源，再按既有policy阻止不可信来源或请求确认；读取外部内容前也可预声明是否预计该源含有可执行指令。需要语义裁决时，可只向bounded judge提交已维护的instruction state与拟变更diff，避免把raw环境全文交给拥有决策任务的模型。这改变候选指令与授权判断之间的可审计接口，不证明模型自述忠实、provenance完整或typed表示无注入。[Secure Agents的必要proposal](https://arxiv.org/html/2603.30016v1)尚未实现并验证这条路线；漏列、错误来源归属、diff遗漏语义或共同模型偏差仍会使裁决失效。识别/来源核验、结构维护、judge与人工确认都付费；无法可靠回指来源或高风险动作仍有歧义时，保留确定性allowlist、最小权限与明确人工/effect-time授权，而非让自述或一次模型判断替代policy。

Books **整合：PLATFORM-SECURITY**；[逐字PRE](../_sources/daily-20260402/SUP_SECURE_AGENTS_PRE_20261013.md)和[必要独核及真实POST](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)可复查。实际一段与本人末注已落实，独立写后复核通过。普通paper-v1复合日门有效层复用，原值见[事件字段](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md#81-明确恢复后的作者实际层2026-10-13)；未核代码、复现或生产。

### [PSPA-Bench: A Personalized Benchmark for Smartphone GUI Agent — arXiv:2603.29318v1](https://arxiv.org/html/2603.29318v1)

必要§2–4的Source5/正常日门与具体NC已独核。APR/PPR只查存在匹配，不能识别顺序、effect或完整对象绑定；感知/backbone/framework与×100口径、经验读写和总预算共变，不采用普遍personalized Agent必须有长期memory。Ch66选项/联合成功/时间支持及Ch77 acquisition/retention/transfer分验承载拟采用的对象/人口分责，局部算法与结果仅报告。

真实 `2+1+2=5`。Books具体已有覆盖：PLATFORM-EVALUATION-SYSTEM，Ch66 258–274与Ch77 1335–1387；作者当前局部核对与[独立有效Source/owner层](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)吻合，不为局部配置或指标另写段。 必要原始判断见[本项证据](../_sources/daily-20260402/SUP_PSPA_EVAL_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_FIVE_CURRENT_DATE_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [StereoVGGT: A Training-Free Visual Geometry Transformer for Stereo Vision — arXiv:2603.29368v1](https://arxiv.org/html/2603.29368v1)

精确v1§3.2–3.5/4.3/Tables5–7必要Source5已独核。EMWM投影simplex使DINO base显系数为0，熵不是语义/几何最优证书；FA/MDE neck仍消费不同目标。MDE-only2.43到2.38差小、15px反退，PCA-SSIM非原表示保真，matching decoder仍训练。只采用表示代理和消费对象分验，merge/encoder/decoder全部成本保留，不采SOTA归因或端到端速度。

真实 `2+1+2=5`。Books具体已有覆盖：MULTIMODAL-REPRESENTATION，Ch23 77–81与306–318；作者当前局部核对与[独立有效Source/owner层](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)吻合，不为局部配置或指标另写段。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH4_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29368_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [Seeing the Evidence, Missing the Answer: Tool-Guided Vision-Language Models on Visual Illusions — arXiv:2603.29428v1](https://arxiv.org/html/2603.29428v1)

精确v1§3.1–3.4/4/5.1–5.3必要Source5已独核。参考线定位正确仍答错、color hex被忽略与JPEG噪声伪差为qualitative反例；Gemini3Flash/repair3.1FlashLite混合、T0/十轮与不同answer schema保留，不称独立compression因果或普遍tool收益。生成图不成为外部世界独立证据；tool、repair、诊断与最终调用费全部计入。

真实 `2+1+2=5`。Books具体已有覆盖：AGENT-TOOL-CALLING，Ch78 238–267的call→有效证据→按证修改→终局；作者当前局部核对与[独立有效Source/owner层](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)吻合，不为局部配置或指标另写段。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH4_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29428_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [When Can We Trust LLM Graders? Calibrating Confidence for Automated Assessment — arXiv:2603.29559v1](https://arxiv.org/html/2603.29559v1)

精确v1§3.1–3.3/Eqs1–10与§4.1–4.3/Tables1–3 Source5已独核。Token仅top20内已发verdict，selfscore为整数映射，SC五票还改变verdict，不能当固定prediction换score。七模型/三ASAG/model-card sampling与hardware不同；bootstrap/FDR、低ECE但RiceChem coverage.005、五票5/5占89.5%的floor、AUC/大模型反退保留。五调用不等完整wall-clock/净效用。

真实 `2+1+2=5`。Books具体已有覆盖：PLATFORM-EVALUATION-SYSTEM，Ch66 54–72与187–209的score learning/calibration/release及artifact绑定；作者当前局部核对与[独立有效Source/owner层](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)吻合，不为局部配置或指标另写段。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH4_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29559_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [SceneTeract: Agentic Functional Affordances and VLM Grounding in 3D Scenes — arXiv:2603.29798v1](https://arxiv.org/html/2603.29798v1)

精确v1§3–5/Alg1/Tables2–4 Source5已独核。Task/profile/scene、closed atomic library与learned plan/zone/segmentation仍依赖标签前提；Alg1全程同静态S无state更新，逐步AND不保证goal覆盖。1132×3/3396、人工100trace/454step91/96.3、Direct/decomposed请求和highlight共变、always-reject低FP与GRPO2800/G12都不授效用或安全。全部检查/renderer/planner/制备费保。

真实 `2+1+2=5`。Books具体已有覆盖：MULTIMODAL-EMBODIED-VLA，Ch26 16–28的真实observation/controller/单位/状态/deadline/safety责任；作者当前局部核对与[独立有效Source/owner层](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)吻合，不为局部配置或指标另写段。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH4_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29798_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [An Empirical Study of Multi-Agent Collaboration for Automated Research — arXiv:2603.29632v1](https://arxiv.org/html/2603.29632v1)

精确v1§3–4/Alg1–2 Source5已独核。Isolated workers多成功merge后重训，team是三固定expert六turn顺序共享修改；GLM4.6v/4.7、RTX3090、300/600s/50round和crash恢复保留。TrainingSuccess非validation改善，同clock非calls/tokens/totalcompute相同，diversity只是qualitative；共同patch失败、merge/试训/通信与全部费用均不可省。

真实 `2+1+2=5`。Books具体已有覆盖：AGENT-MULTI-AGENT，Ch82 46–85 coordination tax与500–526 proposal/verified shared-state commit；作者当前局部核对与[独立有效Source/owner层](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)吻合，不为局部配置或指标另写段。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH4_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29632_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [Spontaneous Functional Differentiation in Large Language Models: A Brain-Like Intelligence Economy — arXiv:2603.29735v1](https://arxiv.org/html/2603.29735v1)

精确v1§3–5必要Source5已独核。Head L2 scalar/MMI十六atom与abs-memory标签不包含完整语义；force layout非物理位置，幅角量非GPU能耗。Qwen3-8B/GSM8K/ARC局部ablation和skip后residual变化保，400%crash、MI estimator/匹配head人口/CI/硬件未明，不作失真精确数或全脑类比。只采用代理、干预及消费者变化分验，全部诊断/运行付费。

真实 `2+1+2=5`。Books具体已有覆盖：WORLDVIEW-REPRESENTATION，Ch5 270–313证据阶梯；作者当前局部核对与[独立有效Source/owner层](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)吻合，不为局部配置或指标另写段。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH6_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29735_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [APEX-EM: Non-Parametric Online Learning for Autonomous Agents via Structured Procedural-Episodic Experience Replay — arXiv:2603.29093v1](https://arxiv.org/html/2603.29093v1)

精确v1§3.2–3.7/5.1/5.4–5.6 Source5已独核。KGQA训练A1→A2增10.3而frozen transfer43.1→41.8，BCB50.6→46.5；iteration是另预算分支。E5/E9、A3反馈命名及backbone/train-oracle-test口径不协调保留，不拼above-oracle/净迁移因果。Teacher/rootcause字段仍需校准；读取、写入、迭代、验证与全部调用费保。Currentv3相关修订只限定旧采用，不倒灌后数。

真实 `2+1+2=5`。Books具体已有覆盖：AGENT-MEMORY，Ch77 1099–1134与1335–1387组件归因/acquisition/transfer/校准生命周期；作者当前局部核对与[独立有效Source/owner层](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)吻合，不为局部配置或指标另写段。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH6_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29093_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [Theory of Mind and Self-Attributions of Mentality are Dissociable in LLMs — arXiv:2603.28925v1](https://arxiv.org/html/2603.28925v1)

精确v1Results/Methods/必要SI/TablesS3–S9 Source5独核通过。三模型/18IDAQ+self5/100重复/T1、fixed question/model/cluster SE/FDR及human500US optin保留。删refusal direction非撤全部safety training，KL和不显著非能力equivalence，六阶例外、85→77度非功能正交；只有Llama base/instruct不足归全变化给安全。自述非意识/真实belief，nonsense/unsafe代价、制备/干预/全费保，不部署ablation。

真实 `2+1+2=5`。Books具体已有覆盖：WORLDVIEW-REPRESENTATION，Ch5 299–313自述/内部记录与局部干预权限；作者当前局部核对与[独立有效Source/owner层](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)吻合，不为局部配置或指标另写段。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH6_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-28925_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [Grokking From Abstraction to Intelligence — arXiv:2603.29262v1](https://arxiv.org/html/2603.29262v1)

精确v1§3–5/AppendixA/B.9 Source5已独核。97四运算/48layer512/A100/五seed，16–31 attention bypass非whole block/MLP删除；BDM与CMS R².88仍相关，CMS局部干预不证BDM驱动。SFM有显式prior/hard threshold而非SGD等价，fixedβ时τ随n>e下降与正文冲突，乘除需discrete-log/reindex，PCA圈非完整群/拓扑证明。全部训练/诊断费保，不采普遍intelligence起源。

真实 `2+1+2=5`。Books具体已有覆盖：WORLDVIEW-REPRESENTATION，Ch5 270–313测量/干预/surrogate权限分层；作者当前局部核对与[独立有效Source/owner层](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)吻合，不为局部配置或指标另写段。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH6_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29262_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [Authorship Impersonation via LLM Prompting does not Evade Authorship Verification Methods — arXiv:2603.29454v1](https://arxiv.org/html/2603.29454v1)

精确v1III–V安全负侧Source5已独核。DefaultGPT4o/四prompt/三genre、每genre单sourceauthor、known2000/query500token、logisticLLR与genuine-negative TNR保留；AdHominem近零、LambdaG/RBI反退与relative TNR非绝对准确点。Compressed bytes/entropy/TTR只是解释线索，未控制decoding因果或真实人欺骗，adaptive verifierfeedback/PEFT/precise API/全费未明。

真实 `2+1+2=5`。仅报告：只记录entry-level提示攻击人口与genuine-negative对照的局部效应，未提出可复用的新验证条件；机器signature与个人identity的解释未被控制，因此不改长期identity机制。不是要求通用AV鲁棒或法律身份才允许局部贡献。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH4_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29454_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [Target-Aligned Reinforcement Learning — arXiv:2603.29501v1](https://arxiv.org/html/2603.29501v1)

精确v1§3.1–3.3/4.1–4.3/5 Source5已独核。固定target cadence扩大m+b池取top-m，c=1给p=λ反驳strict全c；expectedL2非逐transition真实准确。Alg1 terminal d与target用d冲突、C未完整构造不照recipe。四MinAtar/六MuJoCo/五seed与b=m/no retune、SAC反退、平滑/medianIQR与候选forward/选择全费保。

真实 `2+1+2=5`。仅报告：只保固定cadence下的局部recipe/benchmark和上述c=1反例；尚未采用残差rank作为长期训练选择规则，因为C的构造与terminal/target消费接口未闭、严格recency依据不成立。不是要求跨LLM成立才接纳off-policy贡献，不改PPO/GRPO的pi_old/reference语义。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH4_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29501_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [SHIFT: Stochastic Hidden-Trajectory Deflection for Removing Diffusion-based Watermark — arXiv:2603.29742v1](https://arxiv.org/html/2603.29742v1)

精确v1§3–5必要安全Source6已独核，仅保防守压力不抄攻击recipe。公共LDM重采样、SD2.1/H100/九detector与每detector选最小成功λ条件保，非未看测试共用参数。Lipschitz累积/finiteT非零/额外terminal Gaussian假设不授普遍独立或强度必趋零；随机非degenerate非所有信息独立。CLIP32.194/FID73.471与noise distance、既有部分attack100、缺FPRthreshold/CI/公平预算和全部codec/denoiser费用保。

真实 `2+2+2=6`。Books具体已有覆盖：PLATFORM-SECURITY / Ch72第225段及222–236完整邻接，已明确output regeneration transformation class与pixel/frequency扰动不同、内容代理保持不认证来源/所有权、原artifact/派生artifact/transform/detector分别绑定。作者actual原段核：正是本项拟采用的防守压力，不是213段weightwatermark主题映射；本项局部检测率、trajectory独立的未闭理论与逐detector选λ只留报告，不授NC给移除recipe/普遍保证。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH4_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29742_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [The Spectral Edge Thesis: A Mathematical Framework for Intra-Signal Phase Transitions in Neural Network Training — arXiv:2603.28964v1](https://arxiv.org/html/2603.28964v1)

精确v1§1–3/27–29/Table8/43–44 Source5已独核。Strongsignal/slowvariation/commuting条件保留，单seed42/315K人口window10 αGG.21低GG.76而window30.75高.63；所称causal losschange只是first-order Taylor target非移除/重训干预。24/24 decay grokking不证普遍因果，gapflow+.08、Muon/大模型/预警时点未闭，全费用保。

真实 `2+1+2=5`。仅报告：本次采用的是window10与30在同一单seed人口可相反的局部观察，未把first-order Taylor target采为真实干预或部署预警选择规则。Ch4 44–66已承载局部optimization与generalization分验、谱漂移时回实际轨迹的边界；新rolling-Gram定义和本配置数值不改变该已确定解释，不是要求跨objective或普遍定律才保留局部贡献。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH5_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-28964_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [6GAgentGym: Tool Use, Data Synthesis, and Agentic Learning for Network Management — arXiv:2603.29656v1](https://arxiv.org/html/2603.29656v1)

精确v1S3/S4决定Source5已独核。42typedtool/learnedNS3proxy/SelfInstruct/SFT-DAPO组合之外，120heldout同trace从proxy到NS3 replay的L3 transient差额是真实测量增量；rank.99非每trajectory保真，proxy reasoning非causaltruth。原无新NS3反馈重作决策，训练数据消融改变人口/预算，catalog/实现未核、全部制备/trace/训练/replay成本保。

真实 `2+1+2=5`。仅报告：只保这120条固定trace的proxy→NS3重放差额与L3 transient盲区，不把同trace重放叫作policy在新observation下重作决策。拟采用的长期分责已由Ch26 Future-to-Action段及真实observation/controller合同承载：预测/label与真实环境transition是不同事实，重新消费实际反馈才可验闭环。本文没有新增反馈交接机制，局部replay与排名代理仍有研究价值；不因尚未证明完整closedloop而排除诊断，也不以网络领域名EX。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH9_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29656_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [Calibrated Fusion for Heterogeneous Graph-Vector Retrieval in Multi-Hop QA — arXiv:2603.28886v1](https://arxiv.org/html/2603.28886v1)

原v1对象与current精确v3§3.2/4.3/5.1Table1/6Table2必要纠错Source7已独核。旧75.1→76.5并非真实terminal hop；current header/Comments v3/v4冲突原样保留。Current新514/@10 PIT71.0/RRF71.8与paired7W11L p.48、2Wiki491/@5弱统计只核纠错范围，不搬September数据修补April结果。PIT保rank而非magnitude，fullcompute/fresh embedding/全费保，不授全pipeline优越。

真实 `3+1+3=7`。中心争议终态隔离：旧terminal-hop正面结论不采用、不写Books；重开须精确metric/label定义、版本身份与对应可比配对结果，非全版本/附件重跑。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH6_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-28886_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [The Model Says Walk: How Surface Heuristics Override Implicit Constraints in LLM Reasoning — arXiv:2603.29025v1](https://arxiv.org/html/2603.29025v1)

原v1§2–3.4/Table2及currentv4§7/Table2/B.3Table10/Ctable11/§9受影响Source6已独核。旧pair改goal/format，current HOB审计平均长差10.2词、仅4%满足两minimalcriteria，非singlefactor。Llama aggregate+6.6兼容Removed+29.8而Active−9.9；current新Core和July snapshots只撤旧权限不倒搬April。Strict10/10与trial、teacherforcing/inputocclusion与35%judge agreement分验，全部调用费保。

真实 `3+1+2=6`。中心纠错终态隔离：不采用旧通用净收益/唯一inference-order因果，不写Books；重开须真正matched pairs/完整active与removed人口及同预算独立判分。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH6_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29025_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [Big2Small: A Unifying Neural Network Framework for Model Compression — arXiv:2603.29768v1](https://arxiv.org/html/2603.29768v1)

精确v1S3中心Definitions/Theorem1及S4–6 Source5已独核。Ambient measure0非stored bytes小，r→full/b→∞/k→D不保strict compression，KD sufficientcapacity非fixed smaller student保证；ergodic/shadowing不授廉价有限precision seed。Quantizer/mask仍消费原input；上下1%outlier及indices、BN/100KB/MSE.01fallback和uncompressed/INR/outlier/positions总包/10Kepochs费用保，RTXPRO6000 inference约30%慢。UnweightedFFT L2不证高频重权，共变不可唯一归因。

真实 `2+1+2=5`。中心理论终态隔离：不采用unifying全理论、普遍weights保真/经济性或写Books；重开须严格finiteprecision压缩对象、全包字节/计算预算与可核适用条件，局部观察仅上下文。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH8_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29768_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [SeGPruner: Semantic-Geometric Visual Token Pruner for 3D Question Answering — arXiv:2603.29437v1](https://arxiv.org/html/2603.29437v1)

必要精确v1S3/4.3–4.6最低决定事实已独核；DTC worldpatch depth、无CLS mean-attention、FPS normalized3D/cosine融合与原顺序恢复局部组合，same-retention略胜single未控制额外归因/新成立条件。OpenEQA全部retention低full，55.0/55.3口径、无strict geometry/finecoverage保证保；不因小提升/Books覆盖降分或按领域EX。

真实 `1+1+2=4`。仅报告：核身份/日门及不继续采用理由，未授先前5分预案、完整附件或积极长期recipe。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH9_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29437_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [Structured Intent as a Protocol-Like Communication Layer: Cross-Model Robustness, Framework Comparison, and the Weak-Model Compensation Effect — arXiv:2603.29953v1](https://arxiv.org/html/2603.29953v1)

原完整题摘最低4分关闭层复用，structuredintent的crossmodel/framework局部测量是有限prompt条件，不是runtime typed contract或权限效应。当前原identity/v1与normal复合日期层保留；不将格式、weakmodel compensation关联升级为稳定语义/执行保障，也不声称完整实验或实现已验。

真实 `1+1+2=4`。仅报告：局部提示配置未支持新的长期协议机制或普遍模型补偿，保持最低投入终态。 必要原始判断见[本日原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH7_20261013.json)；[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29953_20261013.json)只按已核的paper-v1正常复合门复用，重要纠错后版不倒灌本窗。未核代码或复现。

### [Impact of enriched meaning representations for language generation in dialogue tasks: A comprehensive exploration of the relevance of tasks, corpora and metrics — arXiv:2603.29518v1](https://arxiv.org/html/2603.29518v1)

root与独立reader实际精确v1 §4/5、§6.1–6.5/Tables8–13和必要§3/Table5的Source5。多reference平均测与参考人口的平均接近，不等输入要求已完成；唯一reference与demonstrator重合的满分拷贝未检独立生成/泛化。Slot Accuracy排除无属性样本（两人口约40%），不能与全请求/DA成功合分母；reference数量、内容与采集共同变化不识别数量单因果，DAO .68/指标不同量纲和最大差异人评不认证judge普遍优越。四语料/5-fold/GPT-2Medium/五输出、训练与部署输入同变、各语料反退及全部示例/训练/指标/人审费用保留。

真实 `2+1+2=5`；[必要Source与逐字PRE](../_sources/daily-20260402/SUP_MR_29518_SOURCE_PRE_20261013.md)明确只填长期评价接口。Books **整合：PLATFORM-EVALUATION-SYSTEM / Ch66**，ProtoBias后/语音conditional metric前一段及本人注已由root实际写入，reader实际完整邻接/注nonwriter POST通过（[§9.45](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md#945-mr真实post与四项必要日期)），锁释放；未复用Ch74示例主题当具体覆盖。正常paper-v1复合门原值在[事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29518_20261013.json)，不以Submitted/created单字段授日。未核代码、复现或生产。

### [Hallucination-aware intermediate representation edit in large vision-language models — arXiv:2603.29405v1](https://arxiv.org/html/2603.29405v1)

干预方向也可通过额外训练生产，而不由两份实时视图直接相减：冻结视觉语言模型，训练一对encoder/decoder把内部状态映成候选子空间，再将正负方向解码结果的差作为token编辑提案；另一个只读第一层状态的gate决定该token是否在后续层接受编辑。子空间、编辑方向和gate是三份可变资产，第一层gate不是每层重新测得的幻觉概率。[HIRE的受限对照](https://arxiv.org/html/2603.29405v1)支持这条训练后hook分支，却不证明同caption的原图/噪声图给出真实幻觉与语义的独立分解；CHAIR排序监督也不是reference-free真值。Editor与gate训练、方向制备及后续hooks都付费，局部幻觉改善仍有CHAIR-I、SEED与强基线切片反退，TFLOPs不替端到端延迟。标签、gate或旁侧质量不可靠时，保留原forward、已验无训练干预与外部grounding，不由学得子空间或一次gate批准事实。

真实 `2+1+2=5`，必要精确v1 Source和受影响长期owner差额已独核；[逐字PRE/本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP1_20261013.md)仅填本项接口，不采用完整recipe。root实际窄写，reader_v2[真实nonwriter POST §9.47](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)通过并释放锁；early-late softmask后、VLI前，不覆盖无训练干预。 Books **整合：MULTIMODAL-REPRESENTATION / Ch23**。正常paper-v1复合日门有效（§9.45必要字段），[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29405_20261013.json)不单字段授日、不授artifact同日首公开。未核代码/复现或生产。

### [AGFT: Alignment-Guided Fine-Tuning for Zero-Shot Adversarial Robustness of Vision-Language Models — arXiv:2603.29410v1](https://arxiv.org/html/2603.29410v1)

连续图文encoder的兼容目标也可以是一份旧模型的软关系分布，而不直接逼近旧feature：冻结原CLIP，以当前图文候选上的分数产生teacher target，再让受扰动输入的student分布靠近它。Teacher的校准尺度与student交叉熵的temperature各有职责，不能把两种scale混成一个几何保真保证；目标分布仍继承原模型和标签人口的偏差。[AGFT的受限对照](https://arxiv.org/html/2603.29410v1)支持这条关系锚分支，却不由Top-5 IoU、t-SNE或平均cosine认证语义/下游安全。Clean与较大扰动半径仍有反退，跨报告基线不等matched预算；teacher额外forward、共同PGD、训练与consumer回归都付费，单update附加时间也不是完整训练更便宜。软关系、温度或clean任务失配时，保留原feature锚、普通对抗训练与旧encoder，分别验鲁棒性和原消费者效用，不以双temperature自动批准替换。

真实 `2+1+2=5`，必要精确v1 Source和受影响长期owner差额已独核；[逐字PRE/本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP1_20261013.md)仅填本项接口，不采用完整recipe。root实际窄写，reader_v2[真实nonwriter POST §9.47](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)通过并释放锁；连续Cheers后、离散表示前，不插断VQ/codec旧论证。 Books **整合：MULTIMODAL-REPRESENTATION / Ch23**。正常paper-v1复合日门有效（§9.45必要字段），[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29410_20261013.json)不单字段授日、不授artifact同日首公开。未核代码/复现或生产。

### [DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA — arXiv:2603.29844v1](https://arxiv.org/html/2603.29844v1)

未来条件也可直接预测原视觉encoder的表征，而不训练新的未来图像codec：冻结native视觉encoder，以真实未来观测的表示监督预测模块，先分别用真实future暖启动预测与动作模块，再让动作消费自产future并由动作loss联合更新预测器。这把target身份、暖启动人口与joint gradient分开，计算图可达却不证明policy必须使用future；当前vision和proprioception仍可能提供旁路。[DIAL的受限对照](https://arxiv.org/html/2603.29844v1)支持这个训练交接，去暖启的退化不认证未来是物理真值或原VLM知识全被保留。RoboCasa及两实机任务的有限人口、数据与训练步数共同变化和articulated任务反退须保留；teacher编码、双模块训练、未来/动作推理及真实反馈均付费。Native target、自产future支持或闭环结果失配时，保留真实观测的direct policy、原未来模块或较短chunk，不由PCA/MSE、少示教或joint loss批准动作与安全。

真实 `2+2+2=6`，必要精确v1 Source和受影响长期owner差额已独核；[逐字PRE/本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP1_20261013.md)仅填本项接口，不采用完整recipe。root实际窄写，reader_v2[真实nonwriter POST §9.47](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)通过并释放锁；GigaBrain后、原视频teacher学生前。 Books **整合：MULTIMODAL-EMBODIED-VLA / Ch26**。正常paper-v1复合日门有效（§9.29原28层），[原事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29844_20261013.json)不单字段授日、不授artifact同日首公开。未核代码/复现或生产。

### [LatentPilot: Scene-Aware Vision-and-Language Navigation by Dreaming Ahead with Latent Visual Reasoning — arXiv:2603.29165v1](https://arxiv.org/html/2603.29165v1)

Latent future还可以成为跨控制step更新的register，而不在每次新观测时从空状态开始：模型读当前观察与上一step保存的pilot slot，产生动作提案与新的slot，再覆盖旧slot供下一step消费。这个slot是自产预测历史，不是真实环境观测；训练直接给真实下一视觉状态、监督再下一状态，与部署读自己旧预测的人口需要分别检查。[LatentPilot的受限方法](https://arxiv.org/html/2603.29165v1)提供这种循环接口，却有action head记述不一致，不能补成唯一可执行recipe。有限仿真、expert takeover和两实机定性展示不认证monocular状态充分、完整deadline或安全，PCA动作簇也不证因果。采集/接管、flywheel训练、register驻留与反馈控制都付费；预测漂移、slot身份或控制预算失配时，清空并重建预测、缩短horizon或回退direct policy/真实重观测，实际controller仍决定是否执行。

真实 `2+1+2=5`。Books **整合：MULTIMODAL-EMBODIED-VLA / Ch26**，DIAL之后/原视频teacher学生表征之前一段及本人注，root实际写入且独立reader POST通过（§9.57）。[逐字PRE/必要Source](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP1_20261013.md)保全部反侧和recipe冲突；[正常事件字段](../_sources/daily-20260402/SUP_RESUME_DATE_2603-29165_20261013.json)与[有限官方奖项资格出口§9.52](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)分层，2025 award是不同artifact/性能事件，不是本题早技术正文证据，不要求证明全网从未公开。以后真实early-body只重该家族，未核代码/复现或生产。

### [Enhancing LLM-Based Bug Reproduction for Android Apps via Pre-Assessment of Visual Effects — arXiv:2603.29623v1](https://arxiv.org/html/2603.29623v1)

若环境能被可靠隔离并恢复，还可先获得真正的局部transition观察，而不只预测它：从当前界面提议有限动作，逐个在沙箱中试执行，保存前后screen与Activity，再恢复同一snapshot，才把这组观察交给有界路径搜索。筛选后的动作不是全部可行支持，LLM生成的变化摘要也不是原画面真值；snapshot恢复更不覆盖外部服务已经发生的副作用。[LTGDroid的受限对照](https://arxiv.org/html/2603.29623v1)支持这种pre-assessment分支，但75reports/45apps排除特殊初始化、filter漏动作与不支持的gesture限制可达性。较高成功率付出更多trial、restore、调用与等待，原无预评路径更快；100动作/60分钟上限是本配置预算，不是开放环境可解保证。恢复不完整、观察/摘要不可信或总费无益时，保留当前真实观察、短horizon/直接执行或人工排障，不从沙箱试成功批准真实effect。

真实 `2+2+2=6`。Books **整合：AGENT-PLANNING / Ch79**，只新增上述接口与本人来源注，旧方法/反侧/回退保留；[逐字PRE与必要Source](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP2_20261013.md)的真实写入由独立reader actual POST通过（§9.58）。正常paper-v1日期复用§9.29，未核代码/复现或生产。

### [SkillReducer: Optimizing LLM Agent Skills for Token Efficiency — arXiv:2603.29919v1](https://arxiv.org/html/2603.29919v1)

压缩可发现的skill还须分开路由与功能消费者：先让一个只含描述的shadow skill模拟与原文的竞争，提出更短的触发描述，再用真实router在指定query子集核是否仍会调用；失败时有限恢复原描述或直接回退原文。只有路由资格通过，才分别压正文/引用并验证实际任务。[SkillReducer的受限协议](https://arxiv.org/html/2603.29919v1)把这两个消费者分开，却不证明模拟judge与真实router等价或任意query触发不变；536/536包含39次原文fallback且排除了原失败人口，任务与同预算切片仍有反退。压缩、模拟候选、真实调用、恢复、引用读取和任务验证全部付费，Stage2保留当前best也不能认证无损。Router版本/query支持、正文功能或净预算失配时，恢复原skill和完整引用、保留人工/真实任务回归，不以描述相似或触发一次批准全部能力保留。

真实 `2+1+2=5`。Books **整合：AGENT-CONTEXT / Ch75**，只新增上述接口与本人来源注，旧方法/反侧/回退保留；[逐字PRE与必要Source](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP2_20261013.md)的真实写入由独立reader actual POST通过（§9.58）。正常paper-v1日期复用§9.29，未核代码/复现或生产。

### [EcoScratch: Cost-Effective Multimodal Repair for Scratch Using Execution Feedback — arXiv:2603.29624v1](https://arxiv.org/html/2603.29624v1)

资源策略还可以先在同一修复轨迹上支付短probe，再冻结一组联合预算：用有gold/test支持的初始尝试估计任务状态，按固定阈值一起选择证据输入、JSON操作上限与便宜precheck或完整verification，而不是让三项各自独立放宽。这份probe产生后续控制提案，不拥有任务真值，操作格式正确也不等修复正确。[EcoScratch的受限对照](https://arxiv.org/html/2603.29624v1)支持此联合接口，单trajectory/缺重复CI、provider漂移和严格验证的质量/费用差额仍须保留；host-only能耗与fallback估计也不包含remote推理。Gold/probe、证据制备、模型、所有precheck/full check和恢复均计费，固定/text-only仍是便宜分支。Probe不完备、阈值漂移或验证不可靠时，回退固定预算、原证据与完整独立验收，不让估计较省或syntactic patch自签成功。

真实 `2+2+2=6`。Books **整合：AGENT-WORKFLOW / Ch81**，只新增上述接口与本人来源注，旧方法/反侧/回退保留；[逐字PRE与必要Source](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP2_20261013.md)的真实写入由独立reader actual POST通过（§9.58）。正常paper-v1日期复用§9.29，未核代码/复现或生产。

### [Beyond Localization: Recoverable Headroom and Residual Frontier in Repository-Level RAG-APR — arXiv:2603.29067v1](https://arxiv.org/html/2603.29067v1)

差额诊断还须固定真正消费证据的builder，而不把更好的输入自动归成模型能力上限。代码修复可先在原native wrapper中替换定位证据，再用共同builder比较生成接口，并仅在固定已生成patch池内检查oracle选择；三项分别测获取、消费和已有候选选择，有限池饱和不等所有搜索的上限。增加证据时，以同token数filler和同仓库wrong-issue条件作配对，才能区分内容冲突与纯长度压力。[受限RAG-APR审计](https://arxiv.org/html/2603.29067v1)仍有oracle替换后退步、union-context与多轮结果union不同预算以及“十次都稳”到“一到九次”的回归；test passing也不是完整语义或生产验收。Oracle、十patch生成/检查、额外证据与builder迁移均付费，wrapper/候选池/任务人口不匹配时保留原native任务结果、固定池界限和独立检查，不以一个oracle数字批准通用recoverable headroom。

真实 `2+2+2=6`。Books **整合：PLATFORM-EVALUATION-SYSTEM / Ch66**，只新增上述接口与本人来源注，旧方法/反侧/回退保留；[逐字PRE与必要Source](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP2_20261013.md)的真实写入由独立reader actual POST通过（§9.58）。正常paper-v1日期复用§9.29，未核代码/复现或生产。

### [SemLoc: Structured Grounding of Free-Form LLM Reasoning for Fault Localization — arXiv:2603.29109v1](https://arxiv.org/html/2603.29109v1)

诊断也可把自由语义假说绑定到程序中可执行的锚点，而不只返回可读解释：将候选性质映成闭合typed schema，在每个test上检查相应constraint，再把违反谱用于定位、生成一行patch并重跑。[SemLoc的受限方法](https://arxiv.org/html/2603.29109v1)增加了可被反驳的中间对象，却不由typed grounding认证root cause；原算法只据已失败test分类，可能忽略原passed的新回归，passing中已违反的条件与primary定义也不一致，因此不能照抄成充分修复recipe。250个单函数/单故障Python与少量可执行真实issue不授任意repo，文字匹配、可执行约束和完整任务成功须分验。假说生成、schema/constraint执行、patch及回归全费；接受修改时应另跑原passed和完整独立suite，这是一项工程验收要求，不冒称作者已经实施。条件、锚点或测试支持不足时，保留原源码/trace、传统谱定位与人工验证，不由更高定位分数批准semantic或production正确性。

真实 `2+1+2=5`。Books **整合：AGENT-TOOL-CALLING / Ch78**，只新增上述接口与本人来源注，旧方法/反侧/回退保留；[逐字PRE与必要Source](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP2_20261013.md)的真实写入由独立reader actual POST通过（§9.58）。正常paper-v1日期复用§9.55，未核代码/复现或生产。

### [An Explicit Surrogate for Gaussian Mixture Flow Matching with Wasserstein Gap Bounds — arXiv:2603.28992v1](https://arxiv.org/html/2603.28992v1)

解析构造也须分开“把分布运过去”与“为配对选择正确的最小代价”：在Gaussian mixture的有限分支中，可令各Gaussian均值与协方差沿仿射路径变化，按component responsibility混合velocity，再用路径的动能代价选择带熵正则的配对。这满足相应continuity条件，不代表非交换协方差下的最小Wasserstein能量。[受限Gaussian分析](https://arxiv.org/html/2603.28992v1)只在SPD、局部距离及commuting条件下给近似界；把长路径拆短只改善locality，不取消commuting，近奇异边界还会放大常数。显式surrogate仍含whitening逆平方根与matrix log，不能称完全免spectral计算；CPU构造计时又排除了ODE，不是神经生成端到端加速。配对、矩阵函数、split和实际积分均付费；条件失配时保留exact Gaussian cost或原CFM配对并独立验质量，不由解析式、连续性或拆段批准全局最优与廉价采样。

真实 `2+1+2=5`，精确v1必要机制/直接反侧和受影响owner差额均独核；[逐字PRE/必要证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP3_20261013.md)保费用/人口/未采用recipe。Books **整合：MULTIMODAL-GENERATIVE-PARADIGMS / Ch24**，对应局部原论证中的一段及本人注已实际写入，独立reader actual POST §9.62通过，root已释放锁。正常paper-v1复合日门有效，未核代码/复现或生产。

### [Gloria: Consistent Character Video Generation via Content Anchors — arXiv:2603.29931v1](https://arxiv.org/html/2603.29931v1)

参考人口还会改变生成器学到的是身份条件还是复制捷径：训练短clip时，参考可同时来自该clip内外的较长shot，并把global、view与expression anchors分成不同类型的位置条件，而不让所有参考默认指向待生成帧。较弱的RoPE offset帮助区分来源，不构成无冲突或语义解耦证明；固定anchors与最近自产latent prefix也承担不同责任。[Gloria的受限对照](https://arxiv.org/html/2603.29931v1)支持此采样/条件接口，但训练prefix是真实历史，部署prefix是自产历史，ArcFace/CLIP/DINO又只是指定消费者的proxy，不认证身份真值或无限稳定。数据筛选、三阶段训练、anchor编码、chunk/overlap和消费者回归均付费，局部美学及条件切片仍有反退；参考标签、历史人口或质量失配时保留直接参考、较短chunk和重新锚定，分别验外观/表情/运动，不由长分钟展示批准全历史正确或真实环境状态。

真实 `2+1+2=5`，精确v1必要机制/直接反侧和受影响owner差额均独核；[逐字PRE/必要证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP3_20261013.md)保费用/人口/未采用recipe。Books **整合：MULTIMODAL-GENERATIVE-PARADIGMS / Ch24**，对应局部原论证中的一段及本人注已实际写入，独立reader actual POST §9.62通过，root已释放锁。正常paper-v1复合日门有效，未核代码/复现或生产。

### [VecAttention: Vector-wise Sparse Attention for Accelerating Long Context Inference — arXiv:2603.29494v1](https://arxiv.org/html/2603.29494v1)

选择稀疏粒度时，还须把selector自身和不连续KV访问放进同一执行计划：先以pooled queries给key vectors打分，用最大值差阈值免排序，tile中只写选中indices，再gather对应K/V并重新softmax。这减少的是指定attention计算和访问，不是物理KV eviction或cache容量自动下降。[VecAttention的受限对照](https://arxiv.org/html/2603.29494v1)还表明query pool与key tile大小共同影响质量/占用；逐tile running-max追加indices且不回删，不等最终整row阈值的exact实现。局部attention 2.65倍、selector相对朴素路径9.12倍与TTFT 1.17倍是三种分母，不能互换，若干视频质量切片仍低于dense。校准、选择、indices/gather、归一化及完整请求均计费；稀疏支持、质量或净费用失配时，保留dense或更保守稀疏计划，另验precision、batch/concurrency和SLO，不由kernel加速签发无损与生产收益。

真实 `2+2+2=6`，精确v1必要机制/直接反侧和受影响owner差额均独核；[逐字PRE/必要证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP3_20261013.md)保费用/人口/未采用recipe。Books **整合：INFER-TENSORRT-LLM / Ch49**，对应局部原论证中的一段及本人注已实际写入，独立reader actual POST §9.62通过，root已释放锁。正常paper-v1复合日门有效，未核代码/复现或生产。

### [Efficient Bilevel Optimization with KFAC-Based Hypergradients — arXiv:2603.29108v1](https://arxiv.org/html/2603.29108v1)

曲率还有不同于inner optimizer的一位消费者：外层数据权重或超参数更新需要inverse-Hessian-vector product来形成hypergradient，可用逐layer的Kronecker factors近似这一求解，而不改名为新的内层优化器。Hessian到GGN/Fisher、再到block与factor期望分别丢信息，empirical Fisher不是一般Hessian，factor damping也不等完整曲率加同一λI。[受限KFAC双层对照](https://arxiv.org/html/2603.29108v1)支持一种outer近似接口，不授普通深网exact hypergradient或一般收敛；线性平方实验恰在其精确regime，固定CG次数也不是等墙钟预算。曲率制备、factor状态/刷新、外内循环和调参全付费，cadence最优记述与表中反侧、BERT可训层人口变化及直接EM更强更便宜仍须保留。近似、阻尼或质量费用失配时保留CG/较简单unrolling或原外层配置，内层继续使用已验收step，不把少一份IHVP成本当全部训练更便宜。

真实 `2+2+2=6`，精确v1必要机制/直接反侧和受影响owner差额均独核；[逐字PRE/必要证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP3_20261013.md)保费用/人口/未采用recipe。Books **整合：TRAIN-PRETRAINING / Ch28**，对应局部原论证中的一段及本人注已实际写入，独立reader actual POST §9.62通过，root已释放锁。正常paper-v1复合日门有效，未核代码/复现或生产。

### [Metriplector: From Field Theory to Neural Architecture — arXiv:2603.29496v1](https://arxiv.org/html/2603.29496v1)

反复计算也可改变被更新对象，而不只重用同一feature变换：让输入表示配置场的算子与source，从新初始化的field开始有限演化，再由演化后的field及其空间梯度组合读出结果。这里representation负责配置operator，field负责数值状态，readout负责交回任务，三者不等同于求共享Transformer状态的fixed point。[Metriplector的受限实例](https://arxiv.org/html/2603.29496v1)提供此替代primitive，但图像的coupled field与语言的因果一维scan是任务特定实现，不是同一算子直接覆盖全部域；有限CG/Euler和Noether命名也不认证精确解、守恒或symplectic执行。算子/field状态、求解与反向、substeps/readout全部付费，语言模型的参数、token/context和硬件预算并不匹配GPT对照，较少训练token不证明净计算更省。数值条件、readout或质量费用失配时保留标准layer、显式loop或已验固定深度，分别验任务与数值误差，不由物理术语批准普适架构优势。

真实 `2+2+2=6`，精确v1必要机制/直接反侧和受影响owner差额均独核；[逐字PRE/必要证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP3_20261013.md)保费用/人口/未采用recipe。Books **整合：MODEL-TRANSFORMER-LAYER / Ch17**，对应局部原论证中的一段及本人注已实际写入，独立reader actual POST §9.62通过，root已释放锁。正常paper-v1复合日门有效，未核代码/复现或生产。

### [Think Anywhere in Code Generation — arXiv:2603.29957v1](https://arxiv.org/html/2603.29957v1)

单条代码轨迹也可在已生成的code prefix中途切入thinking块，再返回代码，而不是只在代码之前完成全部说明。提交执行物时移除这些块并连接其余代码；phase标记定义续写/抽取接口，不是每token的真实不确定性sensor，删文字更不是安全隔离。[Think Anywhere的受限对照](https://arxiv.org/html/2603.29957v1)支持这种位置可选分支，但prompt-only/SFT及专门token切片仍有反退，padding也能改善部分结果，不能把位置或内容读成唯一收益因果。合成过滤保留了错误代码，格式合规不认证功能；特殊token还付embedding/LM-head适配费，合成、SFT/RL多rollout、抽取和test均计费，较少token不等完整延迟更低。Phase解析、拼接或功能回归失败时保留先推理后代码、原文本分隔与独立测试/执行权限，不由熵曲线或通过一组测试签发全能力与生产正确性。

真实 `2+1+2=5`，精确v1必要机制/直接反侧和受影响owner差额均独核；[逐字PRE/必要证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP4_20261013.md)保费用/人口/未采用recipe。Books **整合：MODEL-SAMPLING / Ch20**，对应局部原论证中的一段及本人注已实际写入，独立reader actual POST §9.64通过，root已释放锁。正常paper-v1复合日门有效，未核代码/复现或生产。

### [Self-Consistency for LLM-Based Motion Trajectory Generation and Verification — arXiv:2603.29301v1](https://arxiv.org/html/2603.29301v1)

连续形状输出需要先声明怎样算“同一候选”，再投多数票：把轨迹重采样为弧长点列，用允许的几何warp和配准距离聚类，再从最大簇选medoid；prototype与允许warp共同定义这个形状家族，不是prompt语义真值。若warp本身也从同批生成猜测，过窄会拆开正确样本，过宽会把错误形状并入共识。[受限trajectory self-consistency](https://arxiv.org/html/2603.29301v1)的多数/层级选择因此各需正确mode支持和好坏簇分离条件，不能由稳定多数认证运动意图或物理可行。有限模板/单prototype人口、ICP近似及阈值限制等价关系，scale变化也不保原距离误差；十九次生成与单次直接输出不是等预算。采样、配准、candidate warps和两两比较全部付费，mode或等价条件不可信时保留原候选、固定已知warp、单路/外部语义与几何检查，不从最大簇批准正确执行。

真实 `2+1+2=5`，精确v1必要机制/直接反侧和受影响owner差额均独核；[逐字PRE/必要证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP4_20261013.md)保费用/人口/未采用recipe。Books **整合：MODEL-SAMPLING / Ch20**，对应局部原论证中的一段及本人注已实际写入，独立reader actual POST §9.64通过，root已释放锁。正常paper-v1复合日门有效，未核代码/复现或生产。

### [ASI-Evolve: AI Accelerates AI — arXiv:2603.29640v1](https://arxiv.org/html/2603.29640v1)

搜索历史还须区别冷启动参考与本轮实验观察：已有文献形成初始知识库，帮助选择第一批proposal；每次真实实验结束后，再把完整结果与分析写进持续搜索的context，不能以旧文献或流畅分析代替本次测量。这两份信息有不同来源/更新职责，raw日志可恢复也不等已提取下一实验所需的判断。[ASI-Evolve的受限消融](https://arxiv.org/html/2603.29640v1)观察到移除prior较慢冷启、移除分析后持续改进停滞，但没有控制全部token/call/wallclock，不能认证分析器唯一因果或所有架构搜索胜出。文献整理、所有候选实验、分析/持久化、筛选与放大验证全部付费，只展示选中winner又不授全候选或OOD性能。来源、分析或评价失配时回读raw结果、使用手工prior/固定搜索和独立held-out验收，不让派生结论批准生产更新；最终程序/schema与实际执行仍由原owner验证。

真实 `2+2+2=6`，精确v1必要机制/直接反侧和受影响owner差额均独核；[逐字PRE/必要证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP4_20261013.md)保费用/人口/未采用recipe。Books **整合：AGENT-MEMORY / Ch77**，对应局部原论证中的一段及本人注已实际写入，独立reader actual POST §9.64通过，root已释放锁。正常paper-v1复合日门有效，未核代码/复现或生产。

### [Refined Detection for Gumbel Watermarking — arXiv:2603.30017v1](https://arxiv.org/html/2603.30017v1)

固定生成器时，统计水印的检测器也可单独改变：对Gumbel模型中对应随机量构造居中、截断的heavy-tail score，按文本长度与目标误报校准阈值，而不把检测灵敏度提升当归因权限。[受限Gumbel分析](https://arxiv.org/html/2603.30017v1)的低entropy样本复杂度收益依赖理想独立uniform随机量和null文本独立；真实context哈希不严格满足同一IID模型，近匹配lower bound又限定symmetric IID概率人口与model-agnostic有效kernel。Dirac不可检测，稀有高entropy情形可更差，有限synthetic观察及语言数据稍差也不授真实部署普胜。阈值Monte Carlo、参数选择、生成和验证全部计费，短文本/模型漂移或依赖条件不成立时保留原统计校准、签名origin/provenance与人工核验；检测通过仍只是一份受限sensor结果，不认证整篇作者、编辑鲁棒、不可伪造或法律所有权。

真实 `2+1+2=5`，精确v1必要机制/直接反侧和受影响owner差额均独核；[逐字PRE/必要证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP4_20261013.md)保费用/人口/未采用recipe。Books **整合：PLATFORM-SECURITY / Ch72**，对应局部原论证中的一段及本人注已实际写入，独立reader actual POST §9.64通过，root已释放锁。正常paper-v1复合日门有效，未核代码/复现或生产。

### [From Density Matrices to Phase Transitions in Deep Learning: Spectral Early Warnings and Interpretability — arXiv:2603.29805v1](https://arxiv.org/html/2603.29805v1)

C.4全区间严格递增证明只支撑大α尾区间，时间变动G/background被当固定且bounded不约束导数；C.3固定trace majorization是谱代数而非critical slowing。对称C的Frobenius平方与tr(C²)相等，不采用原不同增速句。滑窗/采样人口、探针/线性化及G配置不协调保留，DLN/induction/grok/Qwen7B LoRA只是有限局部观察，不给线上报警FPR/盲测leadtime或安全保证。探针/重复forward/快照、n²协方差/谱、heldout与全部调用计费；Source6中心争议/noBooks独核§9.36，不以2RDM或量子命名赋义。

真实 `2+2+2=6`，暂缓：中心严格预警条件未闭，不Books；[必要Source原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH9_20261013.json)与[有效独核](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)保精确身份/采用/反侧。paper-v1正常复合日期已独核§9.55/56，不借后版本重要性，未核代码/复现或生产。

### [Benchmarking PhD-Level Coding in 3D Geometric Computer Vision — arXiv:2603.30038v1](https://arxiv.org/html/2603.30038v1)

精确v1 S3–5/S7必要Source5与实际Ch75 59–88具体NC已独核§9.49。现有codingaction前dependency/currentcode/约束事实充分、test验输出及信息量不等质量承载限定采用；Method cutoff仅模型相关局部观察，不增加固定截断规则。100function/每题十tests、Eq1是passed fraction均值而非36.6%wholefunction正确，原repo oracle/少case不证数学完备，无必要配对CI或明确tokenbudget，不继承headline显著性。全文/Method/no-paper方向不单调，更多context对部分模型更好。OCR/选题/test与人审/输入prefill/生成/执行费用保留，不采3D科学应用能力。

真实 `1+2+2=5`，已有覆盖：AGENT-CONTEXT / [Ch75](../../../../books/part-07-agent/75-context.md)；[必要Source原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH9_20261013.json)与[有效独核](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)保精确身份/采用/反侧。paper-v1正常复合日期已独核§9.55/56，不借后版本重要性，未核代码/复现或生产。

### [Not All Frames Are Equal: Complexity-Aware Masked Motion Generation via Motion Spectral Descriptors — arXiv:2603.29655v1](https://arxiv.org/html/2603.29655v1)

精确v1 S3–5/Eq1–21/Alg1–2/T1–8必要Source5中心争议独核§9.50。Alg1先gold token谱再mask使attention消费target相关信息，Alg2首全MASK谱及constant-zscore身份未闭；Eq7 epsilon确给零谱归一，不说全无zero处理。保复杂度proxy非真实motion、T3/4 full与主Top3口径/rank1分母未明、static .077→.089/simple .440→.560反退与二十run局部CI。Ch24 masked/reveal与teacher-gold/runtime分责不支持本积极pipeline已部署无泄漏，不机械补段。VQ/CLIP、mask/pairwise谱、runtime重算、训练/生成/独立评价全费；局部数据观察/proposal保留，不贡献前EX或物理安全。

真实 `2+1+2=5`，暂缓：中心train/runtime接口未闭，不Books；[必要Source原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH9_20261013.json)与[有效独核](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)保精确身份/采用/反侧。paper-v1正常复合日期已独核§9.55/56，不借后版本重要性，未核代码/复现或生产。

### [Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning — arXiv:2603.29038v1](https://arxiv.org/html/2603.29038v1)

防守限定精确v1 S3.1/T1/S4.2T2/S4.7/S6及AppendixF probe人口Source5独核§9.53，正常日門§9.56。实际Ch72 20–39已有data approval不能认证adapter行为、安全/效用回归分离、局部probe不证明唯一因果；只这个治理命题NC，不宣全部encoding/probe机制覆盖。Headline<5%不符合14B/32B Table2损害反侧，1280输出classifier pass不授真实有害执行；probe AUC与100risk/100benign heldout不推出真实base-rate FPR或通用防御。保更新、能力测量、classifier/probe访问/训练校准及合法回归费，未读危险payload/绕probe recipe，不复现攻击。

真实 `2+1+2=5`，已有覆盖：PLATFORM-SECURITY / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；[必要Source原记录](../_sources/daily-20260402/SUP_ADMISSION_BATCH8_20261013.json)与[有效独核](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)保精确身份/采用/反侧。paper-v1正常复合日期已独核§9.55/56，不借后版本重要性，未核代码/复现或生产。

### [AutoWorld: Scaling Multi-Agent Traffic Simulation with Self-Supervised World Models — arXiv:2603.28963v1](https://arxiv.org/html/2603.28963v1)

从静态补全转向动态预测时，监督人口也必须改变：非语义occupancy中的静态体积占多数，均匀损失可能弱化少量却影响行为的变化。一个分支先补偿ego motion，在两时刻共同有效的voxel中提取occupancy变化，再下采样成latent权重，强化这些位置的预测监督；把权重均值归一为1只控制尺度，不证明仍在优化原均匀风险。预测的未来latent随后提供逐时刻条件与跨时刻摘要，交给另一个负责agent-specific轨迹的生成器；occupancy预测、agent身份/运动时序与真实行动因此仍分别验收。[AutoWorld的受限对照](https://arxiv.org/html/2603.28963v1)支持动态重权的局部收益，但语义监督基线的动态IoU、realism与轨迹误差仍更好，场景预测更准不能直接认证动作更准。遮挡、warp和传感器变化也可触发change，不能把它等同真实物体运动标签；免去world阶段的语义/轨迹人工标签不免下游运动监督、LiDAR/pose、VAE、双生成及完整验证成本。支持域或消费者质量失配时，保留语义监督、较短horizon或已验simulator/真实重观测，不让预测场景或局部榜单取得物理状态与控制权。

真实 `2+1+2=5`，Books **整合：MULTIMODAL-WORLD-MODELS / Ch25**，OccSim后/原模块化论证前一段与本人注由root实际写入，独立reader actual POST §9.66通过。[必要Source/逐字PRE](../_sources/daily-20260402/SUP_AUTOWORLD_PRE_20261013.md)与正常日门§9.61有效，原v1 Scaling题名保持，不因v2改名倒灌Learning摘要/数字或推重要revision。未核代码/复现或生产。

### [RAAP: Retrieval-Augmented Affordance Prediction with Cross-Image Action Alignment — arXiv:2603.29419v1](https://arxiv.org/html/2603.29419v1)

检索到的动作参考也须按消费者分工：静态contact可取单个参考的dense correspondence，动态方向则从多个参考提取特征，经action条件和跨图alignment组合为方向提案；两者不是同一top-k接口。[RAAP的受限对照](https://arxiv.org/html/2603.29419v1)支持这种分责，却有增加参考引入noise、单任务退步和静态contact不在动态benchmark人口的问题，不能把整体MAE改善当每类动作都更好。二维contact/方向再由depth、camera intrinsics和IK/controller转换，几何lift成功与真实抓取仍分验。检索/特征与alignment训练、点云/标定、四秒推理和实际反馈全付费，不是控制deadline；参考支持、表面深度或controller不可达时回退已验单参考/原几何候选、重观测与传统控制，不由zero-shot标签或二维正确批准物理执行安全。

真实 `2+1+2=5`。Books **整合：MULTIMODAL-EMBODIED-VLA / Ch26**，只上述具体接口落实到该章原论证相邻位置；[逐字PRE/精确证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP5_20261013.md)保必要机制、反側、人口/费用与未采用配方。实际正文/完整邻接/本人来源注的独立写后复核通过（§9.71）；normal paper-v1日期有效，不授artifact同日首公开，未核代码/复现或生产。

### [TrajectoryMover: Generative Movement of Object Trajectories in Videos — arXiv:2603.29092v1](https://arxiv.org/html/2603.29092v1)

有些运动编辑缺的不是更多二维控制点，而是训练pair怎样消除深度歧义：从同一合成场景构造source/target，利用ray与场景surface的交点或无交点的depth prior提出对应位置，再混合hit/no-hit人口生成配对视频。这约束数据制备的几何选择，用户box仍不唯一指定三维运动；无交点prior、physics修正和清理clutter都可能改变原offset或世界。[TrajectoryMover的受限证据](https://arxiv.org/html/2603.29092v1)支持此pair条件分支，不证明真实任意视频、严格内容保持或物理motion正确；box IoU较低，简化primitive的局部SSIM仍更好，多个judge排序也不同。Rays/simulation/render、配对筛选、混合T2V训练和全部编辑采样均计费；scene/depth支持、身份或质量失配时保留原片段、二维scaffold/普通I2V和人工几何核验，不由自产pair或视觉逼真批准真实环境transition。

真实 `2+1+2=5`。Books **整合：MULTIMODAL-GENERATIVE-PARADIGMS / Ch24**，只上述具体接口落实到该章原论证相邻位置；[逐字PRE/精确证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP5_20261013.md)保必要机制、反側、人口/费用与未采用配方。实际正文/完整邻接/本人来源注的独立写后复核通过（§9.71）；normal paper-v1日期有效，不授artifact同日首公开，未核代码/复现或生产。

### [Concept frustration: Aligning human concepts and machine representations — arXiv:2603.29654v1](https://arxiv.org/html/2603.29654v1)

方向之间的“冲突”也取决于谁消费这些表示：可由固定task BB classifier对activation的梯度构造平均Fisher几何，再在该metric下比较CBM概念或SAE方向，保留metric、概念标签与任务head三份身份。三个带符号cosine的乘积为负是一项定义统计关系，合法Gram也可出现，不证明自然概念逻辑矛盾或缺失真概念。[Concept Frustration的受限分析](https://arxiv.org/html/2603.29654v1)只在特定线性Gaussian/独立noise/正定block及人为构造下联系Bayes误差；增加第三概念同时改方向/head容量与监督，不是foundation weights改变或唯一修复因果。Metric可能退化、零分母与所选decision window都限制对象，proxy交叉验证也不等独立机制复现。Encoder取特征、task BB/CBM/SAE训练、梯度/metric、dictionary/window选择、标注和评价全部付费；标签、metric或head失配时保留原probe、受控干预与独立行为验收，不以几何可视化批准ontology修复、因果解释或安全。

真实 `2+1+2=5`。Books **整合：WORLDVIEW-REPRESENTATION / Ch5**，只上述具体接口落实到该章原论证相邻位置；[逐字PRE/精确证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP5_20261013.md)保必要机制、反側、人口/费用与未采用配方。实际正文/完整邻接/本人来源注的独立写后复核通过（§9.71）；normal paper-v1日期有效，不授artifact同日首公开，未核代码/复现或生产。

### [SparseDriveV2: Scoring is All You Need for End-to-End Autonomous Driving — arXiv:2603.29163v1](https://arxiv.org/html/2603.29163v1)

有限动作词库还可先把无时间path与按时间采样的velocity分别筛选，再组合成trajectory供scene-conditioned消费者重评分；固定空间步长与固定时间步长是两个坐标，不是全action space已获密集覆盖。[SparseDriveV2的受限对照](https://arxiv.org/html/2603.29163v1)支持这种coarse-to-joint接口，但marginal Top-K丢掉的path/velocity不能由后续reconditioning恢复，benchmark teacher的评分也不等真实环境效用。词库/teacher制备、全部coarse筛选、组合、重评分和仿真回归均付费；NAVSIM新版/修正评分不能混成同protocol涨分，comfort、overtaking等切片仍有反退，有限CARLA成功不授物理安全。覆盖、组合召回或实际feedback失配时保留原planner、较宽词库/动态proposal与独立controller，不从固定词库效率批准动作正确与真实闭环。

真实 `2+1+2=5`。Books **整合：MULTIMODAL-EMBODIED-VLA / Ch26**，只上述具体接口落实到该章原论证相邻位置；[逐字PRE/精确证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP6_20261013.md)保必要机制、反側、人口/费用与未采用配方。实际正文/完整邻接/本人来源注的独立写后复核通过（§9.72）；normal paper-v1日期有效，不授artifact同日首公开，未核代码/复现或生产。

### [FED-Bench: A Cross-Granular Benchmark for Disentangled Evaluation of Facial Expression Editing — arXiv:2603.29697v1](https://arxiv.org/html/2603.29697v1)

输出编辑的变化大小还可以相对指定reference归一，而不只奖励identity/background保持：用source到实际输出的感知距离除以source到reference的距离，检查是否接近预期编辑幅度，再与指令/保真分项并列。这个ratio比较的是同一metric下的幅度，不是表达方向或语义正确，同幅错误编辑也可通过。[FED-Bench的受限测量](https://arxiv.org/html/2603.29697v1)以经筛选的generated reference同时制备目标与instruction，因而须保共享偏差、crop/mask和reference身份；近零分母未闭合，no-edit软罚仍非硬拒绝。Reference生成/筛选、人审、距离/掩码与judge校准均付费，有限human agreement不认证每样本正确或无偏真值。参考、分母或消费者失配时保留绝对变化、原输出/指令与独立编辑验收，不把归一幅度升为通用质量Gate。

真实 `2+1+2=5`。Books **整合：PLATFORM-EVALUATION-SYSTEM / Ch66**，只上述具体接口落实到该章原论证相邻位置；[逐字PRE/精确证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP6_20261013.md)保必要机制、反側、人口/费用与未采用配方。实际正文/完整邻接/本人来源注的独立写后复核通过（§9.72）；normal paper-v1日期有效，不授artifact同日首公开，未核代码/复现或生产。

### [WybeCoder: Verified Imperative Code Generation — arXiv:2603.29088v1](https://arxiv.org/pdf/2603.29088v1)

可机器检查的子目标允许另一种协作交接：失败的proof obligation先返回冲突，使implementation修订，再重新提取目标，尝试借named invariant迁移已证子目标；只有全部义务成立后才重构整体证明。Name相同提供复用线索，不保证新目标语义身份，完整类型检查/重构不可省。[WybeCoder的受限方法](https://arxiv.org/pdf/2603.29088v1)支持此接口，却有sequential模型优于multi的切片，solve统计还含disprove，formal正确也可能未满足imperative任务要求或原spec的用户意图。全部模型搜索、VC/SMT/Lean、迁移/重构、judge和人工spec费都计入，calls×agents不等总token或墙钟。目标身份、spec或重构失败时保留原证明、顺序求解/较小workflow及独立任务验收，不由多agent数量、重用name或子目标成功批准任意repo与生产正确性。

真实 `2+2+2=6`。Books **整合：AGENT-MULTI-AGENT / Ch82**，只上述具体接口落实到该章原论证相邻位置；[逐字PRE/精确证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP6_20261013.md)保必要机制、反側、人口/费用与未采用配方。实际正文/完整邻接/本人来源注的独立写后复核通过（§9.72）；normal paper-v1日期有效，不授artifact同日首公开，未核代码/复现或生产。

### [Fisheye3R: Adapting Unified 3D Feed-Forward Foundation Models to Fisheye Lenses — arXiv:2603.28896v1](https://arxiv.org/html/2603.28896v1)

镜头投影改变时，冻结几何encoder仍需声明输入与label坐标：把perspective图像映成合成fisheye，再把dense预测逆映回原采样位置，分别用原teacher预测、真实perspective标签或真实fisheye标签监督；三个人口不共享真值资格。层内calibration tokens可由camera类型选择，但classifier/mask也成为接口状态。[Fisheye3R的受限对照](https://arxiv.org/html/2603.28896v1)不由冻结权重保证旧输入exact兼容：post-softmax mask未移除token对分母的影响，mixed-global层又可间接读取已被适配的普通token。Projection、teacher/GT制备、token/classifier训练、额外forward及旧新消费者回归全付费，监督更多仍有depth/pose反退，合成投影不恢复未观测FoV。类型、坐标或混合输入失配时保留原encoder、独立标定/分支与真实标签，不由mask、t-SNE或局部小overhead批准无损sensor迁移。

真实 `2+1+2=5`。Books **整合：MULTIMODAL-REPRESENTATION / Ch23**，只上述具体接口落实到该章原论证相邻位置；[逐字PRE/精确证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP6_20261013.md)保必要机制、反側、人口/费用与未采用配方。实际正文/完整邻接/本人来源注的独立写后复核通过（§9.72）；normal paper-v1日期有效，不授artifact同日首公开，未核代码/复现或生产。

### [The Surprising Effectiveness of Noise Pretraining for Implicit Neural Representations — arXiv:2603.29034v1](https://arxiv.org/html/2603.29034v1)

初始化的收益还须按目标消费者分验，快速拟合坐标信号不等更好的inverse prior。[受限INR对照](https://arxiv.org/html/2603.29034v1)在同一sine/Strainer结构中以noise预训练共享层，新任务重置head并继续更新全部相关参数：它可提高信号拟合，却比原初始化或structured pretraining更差地去噪。这是优化适应与恢复bias方向相反的局部证据，不由NTK/landscape图识别唯一因果。十signal预训练、全部fine-tune/诊断及停点选择都付费；报告的early-stop PSNR与迭代点需要干净reference评价，不是部署未知干净答案的停点，video切片也非全胜。目标、noise或早停支持失配时保留原初始化/structured prior与独立holdout，分开拟合和真实恢复质量，不从低重建loss或少步数批准更好泛化、免费初始化或LLM迁移。

真实 `2+1+2=5`。Books **整合：WORLDVIEW-WHY-MODELS-LEARN / Ch4**，只上述具体接口落实到该章原论证相邻位置；[逐字PRE/精确证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP6_20261013.md)保必要机制、反側、人口/费用与未采用配方。实际正文/完整邻接/本人来源注的独立写后复核通过（§9.72）；normal paper-v1日期有效，不授artifact同日首公开，未核代码/复现或生产。

### [WorldFlow3D: Flowing Through 3D Distributions for Unbounded World Generation — arXiv:2603.29089v1](https://arxiv.org/html/2603.29089v1)

下一层flow的source也可来自已生成的coarse数据，而不总是重从同维Gaussian开始：将前层raw volume上采样，按需加入noise，新增属性channel另填独立Gaussian，再学习到更细数据分布的transport。前层自产误差、attribute维度与真实训练source人口需要分开核，latent-free不等没有中间状态。[WorldFlow3D的受限方法](https://arxiv.org/html/2603.29089v1)还在host保留全volume，逐chunk计算并按overlap合并velocity后更新，不是常数费用的无限场景或普通mesh后拼接。CFM配对不证OT最优，原Euler方向口径未闭不照完整recipe，平均velocity不保无seam/严格geometry；分项质量和训练费仍有反退。Raw数据、各层训练、host内存/transfer、chunk合并及积分全计价，source支持、布局或费用失配时保留原noise-source/latent分支、较小volume与独立几何验收，不由连贯场景图像批准action-conditioned真实transition。

真实 `2+2+2=6`。Books **整合：MULTIMODAL-GENERATIVE-PARADIGMS / Ch24**，只上述具体接口落实到该章原论证相邻位置；[逐字PRE/精确证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_PRE_GROUP6_20261013.md)保必要机制、反側、人口/费用与未采用配方。实际正文/完整邻接/本人来源注的独立写后复核通过（§9.72）；normal paper-v1日期有效，不授artifact同日首公开，未核代码/复现或生产。

### [Stepper: Stepwise Immersive Scene Generation with Multiview Panoramas — arXiv:2603.28980v1](https://arxiv.org/html/2603.28980v1)

全景扩展也不必先产生一条全程 preview：已有全景可条件生成固定前移距离的新全景，再旋转输入选择移动方向。固定距离是训练接口的一部分，不是模型已能消费任意 distance；一条受限分支把输入与输出的两组六面 cube views 在深层共同 attention 中耦合，并保留方位及输入来源 mask。生成所用视图与重建消费者还可不同：后者另取上下 45° 视图增加 overlap，经深度、可见性与 Gaussian 优化重建场景，而非仅凭生成全景看似连贯就批准几何。[Stepper 的必要方法与反侧](https://arxiv.org/html/2603.28980v1)中，可调步长分支出现几何和纹理错误，较大固定步长也损伤细节，支持按训练位移与消费者覆盖分别验收，不证明固定步长普遍最优。16 个合成场景、有限移动范围及用 GT depth 对齐尺度的结果不授实景 metric geometry 或无限探索一致性；训练、各面去噪、深度/可见性与全部重建优化均付费，实时渲染不等于实时生成。位移支持、遮挡覆盖或质量/总费用失配时，保留更短扩展、已验收的全景视频/独立重建与重新观测，而不把补出的场景当环境事实。

真实 `2+1+2=5`。Books **整合：MULTIMODAL-GENERATIVE-PARADIGMS / Ch24**，只上述具体接口落实到该章原论证相邻位置；[逐字PRE/精确证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_TAIL_OWNER_20261013.md)保必要机制、反側、人口/费用与未采用配方。实际正文/完整邻接/本人来源注的独立写后复核通过（§9.71）；normal paper-v1日期有效，不授artifact同日首公开，未核代码/复现或生产。

### [Extend3D: Town-Scale 3D Generation — arXiv:2603.29387v1](https://arxiv.org/html/2603.29387v1)

固定 object-centric latent 要覆盖更宽场景时，还可扩展平面网格，将重叠 patches 的预测 vector field 在每个求解时刻平均，再共同更新 extended latent；这是局部模型的聚合接口，不是每块独立生成后拼接，也不保证已获得全场景 dynamics。单目 depth prior 可以给初始空间布局，遮挡区域再经重复 SDEdit 提议补全；这里还有一条与同噪声时刻重构不同的分支：按 `t_noise` 实际制备初态，却从 `t_start>t_noise` 开始求解，故加噪强度与 solver 消费时钟应分开记录。[Extend3D 的必要方法与直接对照](https://arxiv.org/html/2603.29387v1)支持这一受限初始化取舍，不证明缺失结构在统计上就是噪声，或故意失配对任意模型更好。Depth、patch位置、overlap、两条时钟与迭代次数共同限定消费者支持域，补出的区域仍是生成 proposal。

场景约束还应按职责验收：prior 正 occupancy 约束不保证不增加错误体素，原视图的 LPIPS/SSIM 优化也不认证遮挡几何或新视角正确。受测 SLat refinement 改善纹理却使 Chamfer distance 和 F-score 退步，几何比较并非全面胜出；单图/文本路径的输入制备和预算也不同，不能合并成一个质量或效率优势。更大网格增加 patch 求值与驻留，depth/图像制备、全部 SDEdit、逐步优化/render 与最终重建均付费；受限实测资源点不授任意town scale。遮挡补全、透视比例、几何或总成本不合格时，保留原object模型、更小场景、原时钟SDEdit及独立深度/重建检查，不由纹理观感批准环境真值。

真实 `2+1+2=5`。Books **整合：MULTIMODAL-GENERATIVE-PARADIGMS / Ch24**，只上述具体接口落实到该章原论证相邻位置；[逐字PRE/精确证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_TAIL_OWNER_20261013.md)保必要机制、反側、人口/费用与未采用配方。实际正文/完整邻接/本人来源注的独立写后复核通过（§9.71）；normal paper-v1日期有效，不授artifact同日首公开，未核代码/复现或生产。

### [Omni-NegCLIP: Enhancing CLIP with Front-Layer Contrastive Fine-Tuning for Comprehensive Negation Understanding — arXiv:2603.29258v1](https://arxiv.org/html/2603.29258v1)

更早的一道检查是：否定词本身并不决定图文 pair 应被拉近还是推远。图像确有某对象时，否定该对象的 caption 与图像不相容；对象确实不存在时，描述其不存在却可与图像相容。一个受限对比适配分支将前者从 image 推开，后者则与原 caption 一起对齐 image，同时用另一个 margin 保持两段 caption 的区别。它改变的是可核验存在状态怎样生成训练关系，不是让含 No/Not/Without 的文本一律成为负例，也不把 caption 间相似度约束当作逻辑真值。Present 标签仍依赖原 caption 的事实可靠性，absent 标签还需要确实不存在的前提；图像未展示、遮挡或未标注不等于已经证明不存在。

[Omni-NegCLIP 的必要构造与消融](https://arxiv.org/html/2603.29258v1)仅支持所测对象否定/检索人口：去掉 absence alignment 后该切片退步，但 presence 和 COCO 检索并非全面胜过其他适配。单层加 projection 的可学习性测试与联合微调前六层是不同对照，不证明存在先天的否定语义分区；模板、事实标签、margin/层位选择及复杂scope或双重否定仍有边界。两类 triplets、额外 caption 路径、冻结后缀反传、训练/调参与新旧任务回归均付费，冻结image encoder或一项检索改善不认证通用能力无损。存在关系不可核、模板迁移或原任务退化时，保留原encoder与普通对比目标，优先核验实际正负关系或使用明确标签，而不继续按否定词放大排斥。

真实 `2+1+2=5`。Books **整合：MULTIMODAL-REPRESENTATION / Ch23**，只上述具体接口落实到该章原论证相邻位置；[逐字PRE/精确证据位置与本人注](../_sources/daily-20260402/SUP_FINISH_TAIL_OWNER_20261013.md)保必要机制、反側、人口/费用与未采用配方。实际正文/完整邻接/本人来源注的独立写后复核通过（§9.71）；normal paper-v1日期有效，不授artifact同日首公开，未核代码/复现或生产。

### [Adversarial Prompt Injection Attack on Multimodal Large Language Models — arXiv:2603.29418v1](https://arxiv.org/html/2603.29418v1)

必要精确v1 Source6与正常日门复用，限定采用小pixel/clean画面不获可信来源，生成target文本不等真实下游action，sensor/benign utility与实际effect需配对核；actual Ch72 16–42/75–96已具体承载。不是声称所有latent/text-image构造已有覆盖，其局部优化与数据配方仅保受限压力观察，不新增攻击recipe。保白盒surrogate非零access、caption/VQA各100/扩1000仅三个模型、Claude hard7/2低成功、hard semantic>.3非tokenexact与soft reference循环、Table5 full AvgSim.339低于去text.348/去update.351，ASR不混相似度。精确API snapshot/seedCI/hardware费用未披露，全制备/优化/求值/独立验证计费，未核危险payload/攻击代码/复现或真实行动。

真实 `2+2+2=6`，Books **已有覆盖：PLATFORM-SECURITY / Ch72**，只此治理边界NC；[实际owner比较](../_sources/daily-20260402/SUP_VISUAL_29418_OWNER_20261013.md)独核§9.70通过，不降分、不要求生产/通用防御才有局部价值。

## 5. 缺口与下一步

普通待办：无。本轮来源、日期、证据与Books处理已到安全终态并通过独立六部分验收，不授全网无遗漏/实现或实验复现。以下为本窗已隔离终态保留项，未来仅对应材料的具体条件恢复时定点重开，不扩大本日窗口。

确定新增90家族在§3/4逐一有证据与Books处置，全部新整合实际写后通过，已无普通未读、未写、待锁/日期工作。15个资格保留项和7个机构入口不计候选或正面覆盖；计算容量不是论文不可得。12个中心争议只保受限观察/反侧，不进入Books，精确未决机制和重开需求各随§4对应材料；其中2RDM29805需覆盖全区间的时间变动项/导数条件与无泄漏预警校准，DynMask29655需train/runtime可见谱与首全MASK/zscore定义、对应无gold/同预算消融或实际实现，不能以当前有限结果批准其积极pipeline。

必要日期资格终态保留：StepCache28795早提交、LongCat29339原早仓库同贡献正文信号、Fed28772/Debate28813/PID29676、Byz28780/GPU28793、UniRank29897/OneComp28845/TaskScarcity29914/ShapPFN29946/CAD29847/Turbo29572/GUARD28817及Mirage29069，各自必要firstbody或重要revision事件资格未闭，原值/有限尝试与精确出口见[停点§8.2/§9](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md)。不评分、不列确定新增、不写Books、不称窗外或已审重复；可接受的替代是官方初始公开正文/公告日期或作者/出版方对具体early-body信号的澄清，仅定点重开该家族。Latent29165有限award/paper分责出口已§9.52通过，正常paper-v1资格保持且实际POST通过，不再列日期待办。

下列原轮外部保留项的本轮有效剩余保持隔离，恢复与未恢复层次已同步§2；不能靠旧标签推出本轮来源完成，后续只定点重开受影响家族。ZAI核心贡献前EX已实际通过，无需为不影响处置的时区另建请求。

以下 7 项来源缺段是已隔离的外部**终态保留项**，均不计入 25 个原确定候选；不用于正面证据、Books 或无遗漏断言。每项的定点重开条件写在其后，仅有相应材料恢复才处理，不能由当前日报作者继续无界探路：

- `SRC-OPENAI`：[Research](https://openai.com/research/)与 [Publication](https://openai.com/sitemap.xml/publication/) 的历史目录缺可核的本窗 first-public 停点；现有 sitemap `lastmod` 不够。替代材料为官方原始文章/出版记录及其公开时间，恢复后只查本窗对应家族；News RSS 的 Gradient Labs 已准入前关闭。
- `SRC-GOOGLE-AI`：[Google Research Publications](https://research.google/pubs/) 的 2026 年份列表没有逐项本窗公开时点；已有带日期的 Research Blog 与 DeepMind Publications 停点不覆盖它。替代材料为官方原文和首次公开记录，按具体家族重开。
- `SRC-META-AI`：[Research](https://ai.meta.com/research/) 的动态历史目录不可验证分页终点；Blog 相邻日期只能证明 Blog 本身。替代材料为官方可分页目录或当窗研究原文及公开时间。
- `SRC-DEEPSEEK`：[Research & News](https://deepseek.com/en/news/)本轮首页恢复，原轮 `View All` 的429与未成完整历史停点仍不能由首页恢复关闭。替代材料为官方完整历史目录或当窗原文链接。
- `SRC-MOONSHOT`：[Kimi Blog](https://platform.kimi.com/blog) 当前归档未覆盖 2026；已核的仓库/release 停点不能替代 Blog。替代材料为官方 2026 历史列表或具体原文及其首次公开时间。
- `SRC-XIAOMI-MIMO`：[MiMo Blog](https://mimo.xiaomi.com/) 当前目录未标日期；已核 Paper/release 无命中不涵盖 Blog。替代材料为官网原文的首次公开时刻或有日期的官方目录。
- `SRC-MINIMAX`：[AgentTechBlog](https://agent.minimax.io/docs/techblog)已恢复三明确日期均窗外，尚不能核未列历史slice；已核中英文Blog与CLI release不能替代它。替代材料为具体当窗技术博文及首发时间。

上述来源若恢复，只回补该来源与真实日期的家族，不重做已验的其余 25 项。旧 V2.1 原稿已无损移入[日专属归档](../_sources/daily-20260402/legacy-v21-report.md)，只用于错误审计，不复用其结论。

## 6. 复核

本轮补查独立复核者：`/root/apr02_finish_reader_v2`（非报告作者）；结论：通过。实际完整六部分DAY见[独核§9.73](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md#973-本轮完整六部分day)，覆盖115个唯一家族的身份/日期/评分、90新增全部采用/反侧/处置与46新增真实整合的nonwriter POST，并核来源有限停止、15资格/7入口及12中心争议的终态隔离。root另独立核必要日期/owner锚/GROUP5实际POST与冻结/链接/机械层。未变Source/采用范围复用，不无差别重读附件；原25及原§4保持，V3/本地引用/限定cached与unstaged diff检查通过，机器只证接口一致。完成态由同一reader作一次实际FINAL回读，结果保[本日独核](../_sources/daily-20260402/SUP_WORKING_STOP_20261013.md#9-恢复后的独立复核)。下方原轮审计仅对应原轮范围。

复核者：主任务独立审计智能体 `/root`（非本报告作者）。
结论：通过

先发现 25 行把公告批次误写成单一秒级公开时刻，已统一改为完全落窗的 08:00～09:00 有界范围；复核后检查 14 行来源入口/停点/限制的内部一致性、旧 35 pinned-v1 的 17/18 准入归并、旧排除集 8 个反向找回及 `00421/00824` 前分母拒绝，抽核 TENT/SSD/MyPhoneBench/Agent-Judge 的原文证据和边界，并核 18 个 Integrate 家族在 Books 实际有 marker、7 个 Existing Coverage 有具体章节对照。复核**未逐一重新抓取所有外部目录**；§5 的 8 个外部隔离项仍在，不能据通过宣称来源零遗漏。

机器校验：`python3 scripts/validate_research.py --report papers/2026/04/02/README.md` 与 scoped `git diff --check` 均通过；工具结果不替代上述语义审计。
