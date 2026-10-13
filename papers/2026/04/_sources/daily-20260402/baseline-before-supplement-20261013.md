# Daily Research — 2026-04-02

**规范：** V3
**窗口：** 2026-04-01T09:00:00+08:00 ～ 2026-04-02T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-26T06:11:10+08:00

窗口左闭右开；本窗候选、证据、Books 决定及独立日级语义复核均已闭合。外部材料限制按 §5 隔离，不支持“零遗漏”断言。

## 1. 结论

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

本节只陈述已经重放的官方入口及停点；“未完成”不是“无命中”。原始链接、版本差异和具体补查范围见[日专属笔记](../_sources/daily-20260402/v3-reopen-notes.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| `SRC-OPENAI` | [News RSS](https://openai.com/news/rss.xml)完整历史顺序至 2015；本窗 [Gradient Labs 案例](https://openai.com/index/gradient-labs) 2026-04-01 02:00 UTC，题摘没有新的模型/系统机制，准入前关闭。[Research sitemap](https://openai.com/sitemap.xml/research/)和 [Publication sitemap](https://openai.com/sitemap.xml/publication/)仅能辅助找身份，`lastmod` 不是首发。 | 受阻 | 已隔离：News 已核；Research/Publication 历史文章未能形成可验证的本窗首发停点。只隔离这两入口的潜在遗漏，取得官方文章及原始发布日期后按 family 重开，不推断零命中。 |
| `SRC-ANTHROPIC` | [Research](https://www.anthropic.com/research)内嵌 `publishedOn` 列表，04-01 01:00Z～04-02 01:00Z 相邻条目 03-31 22:17Z 与 04-02 10:56Z。 | 已检查 | 限此历史目录，不证明机构作者未列论文/GitHub 无事件。 |
| `SRC-GOOGLE-AI` | [Research 2026-04 Blog](https://research.google/blog/2026/04/)最早为 04-03；[DeepMind Publications](https://deepmind.google/research/publications/)按日期倒序首页 04-22 直接到 03-22，未列本窗条目；[Google Research Publications](https://research.google/pubs/)按年度/领域组织、2026 年 357 项，未给日级 first-public。 | 受阻 | 两个有日期的原始目录已核；Google Research Publications 缺可界定本窗的日期/分页接口，不能从 2026 年份或当前列表推断本窗零发布。恢复条件是官方精确发布索引或具体论文链接/首次公开事件。 |
| `SRC-META-AI` | [AI at Meta Blog](https://ai.meta.com/blog/)可见 04-08 与 03-26 相邻；[Research](https://ai.meta.com/research/)动态目录无法从可读静态页形成完整历史停点。 | 受阻 | 已隔离：Blog 所见邻近日期不证明 Research 零发布；仅隔离该动态目录，取得当窗官方原文/可检索历史索引时重开。 |
| `SRC-QWEN` | [Research 前端](https://qwen.ai/blog)拼接官方 `GET https://qwen.ai/api/page_config?code=research.research-list` 的 60 条旧项与 `GET https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US` 的 40 条动态项；后者 `extra.date` 唯一本窗项为 [Qwen3.6-Plus](https://qwen.ai/blog?id=qwen3.6)，`2026-04-02T04:00:00+08:00`，正文可由同一 API 的 `content` 读取。题摘/核心说明只有厂商能力披露及 `preserve_thinking` API 版本事实，未见新训练机制；按长期贡献门槛关闭。 | 已检查 | 限该官网 Research 目录，不推断作者 arXiv 与仓库全部事件无更新。 |
| `SRC-DEEPSEEK` | [Research & News](https://deepseek.com/en/news/)可读首页 News 04-24→2025-12-01、Research 06-24→02-25；进一步取完整目录时源站直接返回 HTTP 429（2026-09-26 复试）。 | 受阻 | `View All` 动态列表无法核到终点；仅隔离该入口未见的当窗事件，不以首页间隔证明全站零命中。恢复条件为官方可访问的完整历史目录或该窗口原始文章链接。 |
| `SRC-MOONSHOT` | [Kimi Blog](https://platform.kimi.com/blog)可见归档仅到 2025-11；官方组织仓库排序页查至 100 个 repo，未见当窗新建；定点核 [checkpoint-engine releases](https://github.com/MoonshotAI/checkpoint-engine/releases) 19 个（2026-02-02→06-08 相邻）、[Kimi-K2.5 releases](https://github.com/MoonshotAI/Kimi-K2.5/releases)空，无该窗重大 release。 | 受阻 | 已隔离：Blog 不提供 2026 完整档案；repo 检查限上述入口，不把无新增 release 扩为所有仓库无事件。未列研究正文待具体身份重开。 |
| `SRC-TENCENT-HUNYUAN` | [研究“全部”目录](https://hunyuan.tencent.com/research)的官方 `POST https://api.hunyuan.tencent.com/api/blog/publicList`，`pageNum=1,pageSize=100,renderType=0`，返回 9/9，04-23→02-13 之间无本窗条目。 | 已检查 | 限此完整目录，不覆盖机构作者未列 arXiv 或仓库 artifact。 |
| `SRC-ZAI` | [Research](https://www.zhipuai.cn/zh/research)的 [GLM-5V-Turbo 原文](https://www.zhipuai.cn/zh/research/156)显示 `2026/04/01 16:00`，未写时区；CogViT/MTP/RL 是官方描述。 | 受阻 | 官方时区/精确事件归属及机制正文；当前只作可能落窗的版本事实，不能入本窗确定候选或 Books。 |
| `SRC-BYTEDANCE-SEED` | [Research/Blog](https://seed.bytedance.com/en/research)可见 04-11→01-27；[论文目录](https://seed.bytedance.com/en/public_papers)同站 `GET /api/get_article_list_v2`、`article_type=1,count=20,order_desc=true,page_token=40`、`x-tt-locale: US`，242 总条目；倒序页 04-07T16:00Z 紧接 03-31T12:00Z。 | 已检查 | 限这两个目录，不推断 Seed 作者未列论文或仓库没有本窗事件。 |
| `SRC-BAIDU-ERNIE` | [Blog](https://ernie.baidu.com/blog/zh/) 04-15→02-06，[Publication](https://ernie.baidu.com/blog/zh/publication/)当前四篇且无窗内标题；[PaddlePaddle/ERNIE releases](https://github.com/PaddlePaddle/ERNIE/releases)仅见 2025-06-30 的 `ernie-4.5`，本窗无 release。 | 已检查 | Blog 仅日精度，不能证明该日具体 09:00 边界；其它未列原始稿须凭身份重开。 |
| `SRC-XIAOMI-MIMO` | [Paper/Blog](https://mimo.xiaomi.com/)八篇 Paper 日期 06-29→03-13，Paper 无本窗项；[XiaomiMiMo/vllm](https://github.com/XiaomiMiMo/vllm/releases)与 [MiMo-V2-Flash](https://github.com/XiaomiMiMo/MiMo-V2-Flash/releases)公开 release 列表为空，组织 repo 排序页本窗无新建。 | 受阻 | 已隔离：Blog 目录约十四项不标日期，未能建立本窗全量时间边界；不以 Paper/release 零条代表 Blog 零发布，取得原始日期再重开。 |
| `SRC-MINIMAX` | [英文 Blog](https://www.minimax.io/blog) 06-01→03-18；[中文 Blog](https://www.minimaxi.com/blog) 04-27→03-18。[MiniMax-AI/cli releases](https://github.com/MiniMax-AI/cli/releases)本窗 `v0.4.0/0.4.1/0.4.2` 分别发布于 04-01 09:03、11:14、11:20 UTC；变更是状态栏/配额展示、JSON config/Node installer、CI 上传修复，没有新的大模型或 AI System 长期机制，准入前关闭。 | 受阻 | 已隔离：[Agent Tech Blog](https://agent.minimax.io/docs/techblog)未标历史公开日；无法以可见目录判窗内零事件，需 exact dated 原文重开。 |
| `SRC-ARXIV` | [公告规则](https://info.arxiv.org/help/availability.html)与 `2604.00001/00600/01224/01225/01226` 原站 v1 + DataCite 相邻切点；旧 513 DOI inventory 为注册类别身份线索，旧 35 条逐项核 exact-v1 题摘，旧排除集标题全览并定点摘要查漏，最终 25 个家族获本窗候选及证据终态。 | 已检查 | `2026-04-02 08:00+08` 是经官方公告规则与连续 ID 边界支持的有界批次归属，不是逐篇公告秒级证明；若出现单篇延迟公告/撤回的官方反证，只重开该家族。 |

## 3. 候选与判断

下表为本窗冻结的 **25 个候选家族**。公开时间栏只写完全落在日窗内的 `2026-04-02T08:00:00+08:00 ～ 2026-04-02T09:00:00+08:00` 有界批次范围：它由官方公告计划、相邻 ID 切点及 pinned-v1 共同推定，**不是** arXiv 为每篇披露的秒级时刻。若以后发现单篇延期公告等例外，只重开该项而非整体平移。旧稿按 DOI created 得到的评分作废。

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

## 5. 缺口与下一步

本窗当前没有未处理的可执行工作。独立日级语义复核已通过；后续若取得以下外部材料，只定点重开受影响家族。

以下 8 项是已隔离的外部**终态保留项**，均不计入 25 个确定候选；不用于正面证据、Books 或无遗漏断言。每项的定点重开条件写在其后，仅有相应材料恢复才处理，不能由当前日报作者继续无界探路：

- `SRC-OPENAI`：[Research](https://openai.com/research/)与 [Publication](https://openai.com/sitemap.xml/publication/) 的历史目录缺可核的本窗 first-public 停点；现有 sitemap `lastmod` 不够。替代材料为官方原始文章/出版记录及其公开时间，恢复后只查本窗对应家族；News RSS 的 Gradient Labs 已准入前关闭。
- `SRC-GOOGLE-AI`：[Google Research Publications](https://research.google/pubs/) 的 2026 年份列表没有逐项本窗公开时点；已有带日期的 Research Blog 与 DeepMind Publications 停点不覆盖它。替代材料为官方原文和首次公开记录，按具体家族重开。
- `SRC-META-AI`：[Research](https://ai.meta.com/research/) 的动态历史目录不可验证分页终点；Blog 相邻日期只能证明 Blog 本身。替代材料为官方可分页目录或当窗研究原文及公开时间。
- `SRC-DEEPSEEK`：[Research & News](https://deepseek.com/en/news/) 的 `View All` 返回 429，首页不足以证明中间没有条目。替代材料为官方完整历史目录或当窗原文链接。
- `SRC-MOONSHOT`：[Kimi Blog](https://platform.kimi.com/blog) 当前归档未覆盖 2026；已核的仓库/release 停点不能替代 Blog。替代材料为官方 2026 历史列表或具体原文及其首次公开时间。
- `SRC-XIAOMI-MIMO`：[MiMo Blog](https://mimo.xiaomi.com/) 当前目录未标日期；已核 Paper/release 无命中不涵盖 Blog。替代材料为官网原文的首次公开时刻或有日期的官方目录。
- `SRC-MINIMAX`：[Agent Tech Blog](https://agent.minimax.io/docs/techblog) 当前历史目录无可核日期；已核中英文 Blog 与 CLI release 不能替代它。替代材料为具体技术博文及首发时间。
- `SRC-ZAI`：[GLM-5V-Turbo 原文](https://www.zhipuai.cn/zh/research/156)写 `2026/04/01 16:00` 但未标时区，不能确定是否落窗；CogViT/MTP/RL 的官方描述亦未披露足以支撑长期机制的 Method、受控实验与条件。替代材料先是同源带时区的首发记录；若要进一步进入 Books，还需技术报告或对应的实验合同。

上述来源若恢复，只回补该来源与真实日期的家族，不重做已验的其余 25 项。旧 V2.1 原稿已无损移入[日专属归档](../_sources/daily-20260402/legacy-v21-report.md)，只用于错误审计，不复用其结论。

## 6. 复核

复核者：主任务独立审计智能体 `/root`（非本报告作者）。
结论：通过

先发现 25 行把公告批次误写成单一秒级公开时刻，已统一改为完全落窗的 08:00～09:00 有界范围；复核后检查 14 行来源入口/停点/限制的内部一致性、旧 35 pinned-v1 的 17/18 准入归并、旧排除集 8 个反向找回及 `00421/00824` 前分母拒绝，抽核 TENT/SSD/MyPhoneBench/Agent-Judge 的原文证据和边界，并核 18 个 Integrate 家族在 Books 实际有 marker、7 个 Existing Coverage 有具体章节对照。复核**未逐一重新抓取所有外部目录**；§5 的 8 个外部隔离项仍在，不能据通过宣称来源零遗漏。

机器校验：`python3 scripts/validate_research.py --report papers/2026/04/02/README.md` 与 scoped `git diff --check` 均通过；工具结果不替代上述语义审计。
