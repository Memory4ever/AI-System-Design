# 2025-10-03 有限发现与贡献筛选

作者 Huygens；窗口 BJT `[2025-10-02 09:00,2025-10-03 09:00)`。不继承其他日期候选。执行请求、时间、分页和响应见同目录各 `.receipt.json` / `.raw`；原件存在不代表阅读。

## 实际边界

四个主题查询见 [discover.py](discover.py)：模型结构/训练/优化/推理，LLM GPU/kernel/并行/serving/量化/cache/通信，LLM Agent/RAG/记忆/工具/规划，多模态基础模型/VLA/world/diffusion。仅 `submittedDate:202510020000～202510022359` 用作发现，不当公开时间。systems 9/9、agent 25/25、model 首40/44加 tail4、multimodal 24/24；跨分类归并后95个主题身份。年度/整类目录不是逐篇队列。

官方 CL/CV/DC/PL/IR 月页仅各首25标题作有界命名补检，未宣称是10/02公告，也未逐项读摘要；[公告查询](arxiv-announced.raw)实际返回日级格式校验错误，不能拿它证明无事件。11个相关标题定点恢复 exact-v1（含旧 PASTA 身份）。本日最终实际完整 exact-v1 题摘94个唯一身份：主批80、tail新增3、标题补检11；见 [主批](exact-v1.raw)、[tail](tail-exact-v1.raw)、[补检](title-supplement-v1.raw)。当前版本史未见需另开全附件队列的具体纠错标记；不宣称全站没有撤回/修订。

12个标题清晰范围关闭：2510.01571蛋白、.01724代谢组、.02139生物信息MCP、.02567合金、.01733中微子、.01749光子能带、.02086脑肿瘤、.02527costate MCMC、.01841person search、.02232传统BERT网络霸凌、.01801spam GNN、.05151金融应用组合。依据是领域应用/通用预测没有模型与系统机制增量；AI for Science按ROADMAP暂缓，不以通用Data/Agent节点重新引入。没有以标题代替含糊条目的完整摘要。

## 完整题摘后明确关闭12项

| 精确身份 | 原文与具体关闭理由 |
| --- | --- |
| 2510.01582v1 ImageNet-Think | 双teacher推理数据资源；题摘未辨识新的学习机制或评价盲区，不以数据规模作设计增量 |
| 2510.02243v1 AccurateRAG | 加工/FT/评价流程与QA收益；未辨识新组合机制或组合失效边界 |
| 2510.01800v1 REBot | 学术法规问答的dense/graph/classifier组合；应用质量不等新增LLM系统机制 |
| 2510.01842v1 Pre-Hoc AutoML | tabular候选模型预选与LLM排名；并非模型自身训练/执行机制变化 |
| 2510.01533v1 NVIDIA AI Aerial | 无线DSP/CNN GPU平台；不能借“GPU系统”类比引入LLM设计贡献 |
| 2510.02259v1 Molecular Structure | 分子结构领域研究，属明确暂缓的AI for Science |
| 2510.01664v1 GuruAgents | 金融persona/prompt与回测组合；未辨识新执行或可靠性机制 |
| 2510.01622v1 LLM4Rec | 五组件推荐组合；题摘未建立新的因果去偏设计或适用边界证据 |
| 2510.01698v1 TalkPlay-Tools | 已有SQL/BM25/dense/semantic IDs的音乐工具应用；不是新调用机制 |
| 2510.01553v1 IoDResearch | 科学私有异构知识探索；按暂缓范围关闭，不因Agent命名准入 |
| 2510.02512v1 Query Variants | MonoT5等一般IR/QPP；未建立LLM/RAG机制增量 |
| 2510.02668v1 AgenticRAG | 工具RAG/CoT推荐组合；未辨识新接口或模块成立条件 |

上述关闭不依赖首次公开时刻；日期未核实不制造日期恢复任务。它们不是“没有学术价值”。局部、小模型、负面结果、综述标签、主题可能已有覆盖均未用作共同排除理由。

## 日期保留与窗外身份

94完整题摘中另1项旧论文2412.10419v1；另2项当前arXiv提交事件已经在窗口后：2510.02838v1 TridentServe（10/03 09:23 UTC），2510.02657v1 Less LLM More Documents（10/03 01:26 UTC）。这里仅用提交证明该当前事件尚不能在提交前公开，不把提交当first-public；如有更早作者稿，应恢复那个事件身份，不回填本窗。

其余79个身份仅保留为贡献潜力/日期隔离：有新机制、取舍或反侧命题值得在日期确认后处理；**不计正式候选，不评分，不授正面Evidence，不进入Books**。包括11月编号2511.14769的身份异常，不能因API submitted字段相交强行归属。精确全题摘原件是这些身份的恢复入口，不要求取得日期后重读未变化AB。

首批5个具体机制见 [FIRST_CALIBRATION.md](FIRST_CALIBRATION.md)。另有ElasticMoE的零拷贝HBM映射扩缩、Kant的统一调度、Chronos的rank压缩、语音中间表示、AgentRec的动态权重、VLM-Lens的内部能力测量、RM综述的新增PRM对照等窄潜力；没有因未开源、研究局部或“综述”标签排除。Litespark方法未充分披露且tokens/s与iteration数字不一致，只收窄可核命题，不用访问/可信度困难偷换贡献关闭。

## 官方材料事件

Google 10/02 [PASTA Blog](google-collab.text.txt)实际核心与2412.10419v1完整题摘已读：EM用户类型、RL多轮slate、人工与模拟轨迹混合并非本日新机制。Blog未辨识重要方法修订；“we have released”不证明artifact在2024已真实可得，也未建立新的artifact事件差额。关闭本次传播事件，未把未审旧论文写成已审重复。

OpenAI Wrtn官方10/02故事核心为persona/prompt、轻重模型分类路由及业务留存，未辨识可比机制/边界；日本政府合作为政策事件，关闭贡献。原始发现响应 [A](day3searchA.json) / [B](day3searchB.json) / [C](day3searchC.json)只辅助身份，不作为独立研究证据。

### R2 有限真实查询补证

2026-10-05T07:21:05+08:00保存本次真实调用的输入与原返回：[SEARCH_REPAIR_RAW.json](SEARCH_REPAIR_RAW.json)。旧A/B/C原返回未保存输入，当前不能恢复，不按结果猜造旧query。本次只重执行缺失的同日四组辅助搜索，response_length=long，每query仅工具首批返回即停，无翻页、无月/年/分类扩扫：

1. `site:openai.com/research OR site:openai.com/index "October 2, 2025" model research`
2. `site:ai.meta.com/research OR site:ai.meta.com/blog "October 2, 2025" model training`
3. `site:qwenlm.github.io OR site:qwen.ai "October 2, 2025" research model`
4. `site:minimax.io/blog OR site:minimaxi.com/blog OR site:agent.minimax.io/docs/techblog "October 2, 2025" model agent`

工具返回合并14条线索，实际核标题/来源后只有Wrtn、日本合作与已读RBAC具有相关原官方身份，均复用既有有效核心与处置；其余社区问答/bug报告与诉讼PDF不构成新的官方研究机制事件。返回包含目标域外条目，不能将site表达式视为严格域过滤，更不能用Meta/Qwen/MiniMax无相关返回证明无事件。此补证只修复执行范围可复查性，保留各原Research历史缺段与日期隔离，不新增候选/Evidence/Books。

OpenAI [RBAC write-up](openai-rbac.text.txt)必要安全核心已读，详见 [CORE_BOUNDARIES](CORE_BOUNDARIES.md)。窗内generic outage update与当前事后根因正文的公开时间是两个事件；正文没有可核published timestamp，终态隔离，不以事故发生时间替代文章公开时间。
