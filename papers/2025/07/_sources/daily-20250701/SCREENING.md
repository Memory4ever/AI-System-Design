# 2025-07-01 原始来源与筛选停点

窗口：2025-06-30T09:00:00+08:00 ～ 2025-07-01T09:00:00+08:00。作者：jul01_author。检查：2026-10-06/07 北京时间。当前 V3；独立从 primary source 重建，未读取旧 Daily/Weekly。保存文件名不是完成状态。

## 查询边界、停止点与纠正

各 `*.request.json` 保存 URL、实际检查 UTC 时间、HTTP、curl 返回码及错误；相同前缀的 raw 为响应原件，txt 是去掉导航样式后的阅读副本。`search-inventory.json` 是机械提取的身份/题摘线索，不是候选、评分或完成投影。题摘原件仍是 HTML raw；精确 v1 仅对 TM/L0/MAPF 页面作了单独核验。

arXiv 搜索仅负责发现。恢复历史公开公告失败，不能凭提交过滤器证明本窗事件。三组收窄查询为完整短语 `"language model"`（102 结果）、`"LLM inference"`（13）、`"generative model"`（20），最近提交日期 2025-06-30～07-01，各取 size=200 的单页，三个原件归并为119个 ID。包含旧 ID 的后续提交及7月 ID，**不是119篇当日新论文，也不是119项都完成审阅**。原始 `topic-model`/`topic-generative` 未加引号，命中266/390且传输不完整，已经用上述短语纠正；不据它们声明召回完整。

补主题查询使用首次提交 2025-06-27～06-30，窗口更宽仅用来找可能进入本窗公告的线索：agent AND "language model" 30；GPU AND "language model" 5；"world model" OR "vision language action" 13；"distributed training" OR "model parallel" 0。均为 size=200 单页，不借精确短语0命中推断该主题无事件。公开归属仍未证实。

Transformer OR "mixture of experts" 查询166项，含普通视觉/领域预测，过宽：**只看相关标题查漏，不变成166项逐摘要关闭队列**。架构相关线索交由上述 language/GPU/生成/World Model 主题处理。cs.CL/LG 六月列表只得到部分响应；只作相关标题查漏，不宣称分类全量读完。API 空响应、分类列表部分下载、rate limit、官方 advanced 公告日期只支持年月而非日，均不能当作无事件。root 已独立尝试新版月列表 /list/cs.CL/2025-07；常规 schedule 及 ID 分配规则只帮助解释元数据，不能证明某项实测公开时刻。

当前可执行发现和筛选已经收束；未取得实际公告的线索集合被整体隔离，不转入本日正式候选，不用继续全文来掩盖日期问题。已读完整题摘的下列材料保留判断；其他命中只是未采用的身份线索，不虚写已经初筛。恢复实际官方公开清单/历史公告邮件，或作者首次公开正文及可信时间后，只重开受影响家族。

## FIRST 原件与独立校准

root 独立读取 TM/L0 精确 v1 完整题摘和 MAPF 代表关闭原件，校准结论由 root 发回：

- TM 的非连续监督、概率转移 kernel 因子分解是潜在机制增量；质量、因果/cache 结论须受核心方法及可比评价限定。
- L0 的潜在贡献保留；worker pool、REPL、SimpleQA 数字不能自身证明新增机制，需要具体训练执行/失败条件。
- MAPF 关闭成立：领域 solver 的 delta expert fine-tuning 未建立通用模型系统新边界。
- ERNIE 异构 MoE 可核验，但日期未证实仍隔离。

原件：`abs-tm-v1.raw` / `abs-l0-v1.raw` / `abs-mapf-v1.raw`。这三份精确v1页面未见可见撤回、勘误、纠错标记；不是完整current事件史或全部版本审计。TM、L0 的 v1 提交字段分别是 `Mon, 30 Jun 2025 07:51:58 UTC`、`Mon, 30 Jun 2025 09:44:32 UTC`，均**不是公开时刻**。

## 已读题摘、潜在贡献保留，但公开日期隔离

链接身份均为 https://arxiv.org/abs/ 下列 ID。完整题摘见 `search-inventory.json` 对应条目及其 source 指向的 raw；搜索显示的是检索时摘要，未冒称各项精确 v1 已读。以下没有因日期/访问问题降分或改成无贡献；亦未借章节映射直接准入。

| ID / 材料简称 | 原约束 → 实际潜在增量 → 待核验的选择 |
| --- | --- |
| 2506.23589 Transition Matching | 连续路径/确定性 velocity 限制监督与因子分解 → 学习离散时间随机转移及不连续监督 → 因果与非因果生成的质量/采样代价选择；FIRST 已校准，已读必要核心 |
| 2506.23667 L0 | 长期代码行动的 rollout/梯度/失败反馈难连接 → token action、step return、REPL 持久状态与执行奖励连接 → 自由代码 agent 的训练稳定条件；FIRST 已校准，已读核心 |
| 2506.23635 Apple Silicon expert parallelism | 单机容量不足 → 多节点 MoE 的通信延迟、内存管理实测 → 是否值得以消费节点换成本；对照配置及更早 RACS 发表身份未核，不采纳1.15倍 |
| 2506.23864 Garbage In, Reasoning Out? | 测试分数被视作推理证据 → 重复、措辞、形式线索及重新人工标注 → 分离评价数据质量和模型能力 |
| 2506.23618 TurboVSR | 高分辨视频上采样成本大 → 高压缩、首帧因子化条件、shortcut distillation → 质量/压缩/蒸馏代价需核 |
| 2506.23731 Radioactive Watermarks | 输出水印不等于训练后可追踪 → DM 编码/加噪使水印丢失而 IAR 水印可能训练后持续 → 区分检测、蒸馏和数据来源追踪；安全信号保留 |
| 2506.23563 MMReason | 闭选/shortcut 可能伪装多步推理 → 开放回答、shortcut 筛除及过程评价 → 是否修正多模态推理评分 |
| 2506.23576 Multi-Agent Defences Against Jailbreaking | 防御宣传与实际协议可能混淆 → 复现并检查误报/成本/攻击依赖 → 不因负结果或复现关闭 |
| 2506.23590 CAI | 对象幻觉中视觉注意可能错分配 → caption-sensitive attention 干预 → 检查注意归因而非只看最终 caption 分数 |
| 2506.23626 Self-correcting Reward Shaping | 静态奖励遇游戏机制变化 → LLM 反馈修正 RL reward → 需辨明是否超越领域启发式的可迁移失效边界 |
| 2506.23639 Byte-Pair Visual Encoding | 固定视觉 token 不能利用统计重复/空间结构 → 频率与空间编码配合课程 → 多模态 tokenization 选择 |
| 2506.23663 Domain Robustness of Contrastive VLMs | 通用benchmark强弱不能直接判定部署域稳健性 → 六域corruption下contrastive VLM架构及variant表现显著不同 → 保留“模型/variant选择取决于部署域扰动而非单一总榜”的评价边界线索；是否控制扰动质量/强度、是否只换数据集尚待证据，不把LLM造数据自身当贡献 |
| 2506.23678 Interactive Reasoning | 长 CoT 对用户不可介入 → 可编辑中间推理、控制实验 → 干预状态是否真实改变决策，不能仅因有UI准入 |
| 2506.23725 PAC Bench | 策略存在不等于具备执行先决条件 → properties/affordances/constraints 联合评价 → VLA planning 的执行前检查盲点 |
| 2506.23735 AutoEvoEval | 静态测试可能高估泛化 → 控制原子变换/多步组合 → 检查评价混杂因素 |
| 2506.23785 VisTex-OVLM | 原object-text空间难表达预训练罕见且无法文本描述的对象 → 保持OVLM架构、将视觉exemplars投影为原text-space token而非另改其object-text对应 → 保留具体视觉提示接口替代设计及few-shot/原泛化共存线索；“保留泛化”是作者待验证主张，不能仅因有alignment词收录 |
| 2506.23856 Conditional Prompt Tuning / CaPT | 动态视觉条件被认为帮助新类泛化 → 随机噪声可能胜过视觉条件、类别文本条件替代 → 条件 prompt 的归因反证 |
| 2506.23929 IMPACT | 增加 reasoning 被认为提升能力 → 多语形态任务中 thinking 的负向证据 → 增加推理并非普遍有效；不按传统语言学标签自动排除该反证 |
| 2506.23930 Hate Speech Detection / Metaphor Prompting | 良性分类也可能触发拒绝 → 以隐喻改变安全响应 → 安全/跨语言信号保留，不照录攻击保证 |
| 2506.23940 Graft | 多领域 LoRA 组合可能互相冲突 → activation compatibility 选择层并融合 → adapter synergy 的适用条件 |
| 2506.24016 EXPERT | judge 生成解释不保证解释质量 → 结构化监督及独立人评 → 评分与解释需分开验证 |
| 2506.22419 NanoGPT Speedrunning Benchmark | 熟悉研究描述不代表可重建训练优化 → 已知优化代码重现仍失败 → coding agent 能力边界，LLM训练主题不属暂缓科学应用 |
| 2506.23485 TAIRA | 简单 intent decomposition 泛化差 → 经验 thought-pattern distillation → 对未见复杂任务的 planning 条件待核 |
| 2506.23329 IR3D-Bench | 描述图像不代表场景理解 → 主动编码渲染重建及几何评价 → 工具调用成功与视觉精确性分开 |
| 2506.23276 Corrupted by Reasoning | stronger reasoning 不代表 cooperation → 成本制裁博弈的负向对照 → 多 Agent 合作的具体边界 |
| 2506.23274 Real-Time Progress Prediction | 位置百分比不等于剩余推理进度 → hidden-state probe 与同一前缀续跑离散度 → 可观测进度的内在不确定性 |
| 2506.23260 Protocol Exploits survey | 输入注入视角遗漏工具/协议端 → host/tool 与 Agent 通信威胁映射 → 需要辨明具体新漏洞/约束而非taxonomy即贡献；安全信号保留 |
| 2506.23046 SoMi-ToM | 静态文本测试不反映交互视角 → 多模态第一/第三人称的能力差异 → 新评价维度是否超越单纯数据集 |
| 2506.22957 Interlocutor Awareness | Agent 被当作无身份的文本接口 → 识别对话模型后适配及reward hacking/jailbreak现象 → 合作与身份敏感安全边界 |
| 2506.22853 DICE-BENCH | 单轮function call遗漏分散上下文 → tool信息离散度与多轮依赖控制 → 多方对话参数聚合的失效条件 |
| 2506.22852 KAFT | domain facts 只在 prompt 输入可能不会被有效消费 → 相同KB下 prompting/knowledge-augmented tuning比较 → 检索与训练的交接条件待核，不直接认定通用改进 |
| 2506.22598 RExBench | coding成功被外推为研究扩展 → 既有paper/code上执行扩展自动验收仍失败 → agent任务成功的边界 |
| 2506.22557 MetaCipher | jailbreak能否跨版本维持不明 → adaptive低查询攻击主张 → 版本、攻击预算、判定协议必须单独核；安全信号保留 |
| 2506.22056 Universal Trajectory Retrieval | 单图检索不表达状态—行动轨迹 → 轨迹对比学习与token选择 → Agent记忆索引粒度的选择 |
| 2506.23513 ViewPoint | perspective priors与全景连续性冲突 → ViewPoint map及Pano-Perspective attention → 几何表示与预训练先验共存 |
| 2506.23468 NavMorph | 固定latent dynamics不适应导航变化 → contextual evolution memory与在线world model → 预测状态如何被观察纠正 |
| 2506.23434 Foundational LiDAR world models | 专域动力学不一定跨域迁移 → 三种迁移条件及更压缩latent CFM → dynamic learning可迁移/资源代价的边界 |
| 2506.23135 RoboScape | 视频视觉相似不能保证几何/接触动力学 → temporal depth及keypoint dynamics联合监督 → world-model训练辅助约束 |
| 2506.23126 ParticleFormer | 多材质particle跟踪重建成本大 → 直接point cloud混合局部/全局动力学损失 → action-conditioned dynamics的表示选择 |
| 2506.23068 Meta Causal World | 单一因果图随观测/策略变化可能失效 → latent meta-state触发多个因果子图与主动干预 → 可修正world representation |
| 2506.23074 CDAL | attribution依赖source spurious bias → counterfactual decoupling → 未见生成器的来源判定条件 |
| 2506.23491 ZonUI-3B | 单纯增加GUI训练量被视为改善高分辨泛化 → 控制冗余/多样性及两阶段训练消融 → data diversity与资源选择的局部边界 |
| 2506.23225 MGLU | 双gate/value矩阵增加访存 → shared weight binary mask与专用kernel → FFN质量/访存/计算权衡 |
| 2506.23025 Spectra1.1 | 参数规模和数据规模被等同优化 → ternary scaling、packing与kernel → 训练数据/低比特执行联合选择 |
| 2506.22950 Infinite Sampling | GRPO全组并发将memory与group size绑定 → micro groups、连续采样和length scheduler → 组统计语义与rollout资源解耦 |
| 2506.22033 SiPipe | PP瓶颈只看GPU → CPU sampling、token-safe执行、结构化通信 → CPU/GPU pipeline气泡边界 |

以上各项为**日期隔离的潜在贡献**，无正式分数/审阅完成/Books已有覆盖断言。该处理不是降低门槛，也不是因全文成本关闭。后续公开证据确定窗外，则转为对应日期线索；若落窗，定点核精确版本、当前纠错/撤回与贡献事实，再完成审阅。

## 已读题摘后明确关闭的代表性材料

日期未核实且已按内容关闭者，不为不影响处置的日期另建请求。对同类只抽取下面具身份的记录，不冒充全部命中均已关闭。

| ID / 原件身份 | 具体关闭依据 |
| --- | --- |
| 2506.23793 Advancing Learnable Multi-Agent Pathfinding Solvers with Active Fine-Tuning | 完整v1题摘见abs-mapf-v1；centralized expert delta数据提升MAPF solver，未建立通用模型学习、协作或资源边界；FIRST独立确认 |
| 2506.23524 NEU-ESC | 教育评论情感/主题数据集，新语言领域任务，未新增模型/系统机制 |
| 2506.23862 LLM Statistical Inference | 用context augmentation做领域统计分析，尚无改变LLM学习/系统设计的机制；不是因“非AI理论”关闭 |
| 2506.23641 VAP-Diffusion、2506.23701 MDPG、2506.23659 Turbulence | 医学影像/流体科学应用，ROADMAP明示暂缓；不经Generative owner回引 |
| 2506.23869 Piano Representation | 钢琴表示规模及音乐任务评价，未提出可迁移基础模型/系统失效条件 |
| 2506.24021 Minimally dissipative multi-bit logical operations | 热力学逻辑操作研究，题摘没有建立服务模型计算的实现/约束链，仅硬件类比不足 |
| 2506.24123 Calligrapher | 字体样式任务的数据自动构造、成熟Qformer/style injection组合，摘要未建立新的一般条件生成机制或反证；不是按标题早关 |
| 2506.23527 Recipe Memorization | 20条预选Mixtral菜谱的配料来源匹配与judge抽取；配料网上可追溯并不辨别训练记忆/常见语义，未形成改变memorization解释的可支持反证 |
| 2506.23580 Dataset Distillation via VLM Category Prototype | 使用既有VLM类别原型指导领域蒸馏，未建立foundation model形成或系统取舍的新增可迁移条件 |
| 2506.23606 SG-LDM | 复查完整题摘并经root独立指出：语义→LiDAR生成及域适应增强，用latent alignment条件生成改善下游segmentation，未建立改变基础模型形成/系统设计的新机制或失效条件；原先把alignment泛化为主线准入理由过宽，改判关闭 |
| 2506.23607 PGOV3D | 复查完整题摘并经root独立指出：MLLM+2D分割产监督，两阶段curriculum/跨帧一致性用于3D segmentation，未建立主线模型形成/系统新判断；原先以“跨模态/课程”保留过宽，改判关闭 |
| 2506.23822 LaZSL | 同类复查完整题摘：用既有optimal transport匹配CLIP局部特征与离散属性做zero-shot分类解释，摘要列解释性/精度提升但无新的表示形成机制或可迁移失效条件；不能把“局部对齐”与“无需训练”自动当长期增量，改判关闭 |
| 2506.23605 AI-Generated Lecture Slides | 幻灯片检测/检索领域数据构造，不新增模型机制 |
| 2506.23610 Personality/Misinformation Simulation | 社会行为模拟应用，未形成可支持的模型/系统基本设计修正 |
| 2506.23643 Chunk AR Recommendation | item语义/行为chunk用于推荐指标，题摘未建立一般生成factorization的新适用边界 |
| 2506.23689 PokéAI | 规划/执行/批评与memory成熟模块组合，50场游戏胜率不证明新增执行或可靠性机制 |
| 2506.23692 Agent4S、2506.22653 URSA、2506.22189 Drug Discovery Modularity | 科学研究/药物应用为主要证据场景，按当前暂缓边界关闭；不借Agent通用词回引 |
| 2506.23694 User Scenario Writing | 用户体验写作支持研究，无模型/系统机制增量 |
| 2506.23762 Software Engineering for LLMs | 研究状态/挑战taxonomy，题摘未提供修正机制解释的具体实验证据 |
| 2506.23774 Teachers in Hate Incidents | 教师培训的多Agent应用，未提出模型安全机制增量；“hate”不是本身的安全修订信号 |
| 2506.23826 Digital Me | 个人HDT愿景与memory生命周期架构，题摘未建立新增可核验状态/执行条件 |
| 2506.23850 Email as Interface | 行政字段抽取与邮件入口，成本及任务成功数字不足以改变模型/Agent机制 |
| 2506.23888 MAPS | 多层reflection/adaptive prompts组合与数学指标，题摘未建立新的验证器、可靠性条件或反思失败反证 |
| 2506.23924 Stochastic Modeling OR | OR领域问题表现比较，未有学习理论/优化机制直接支撑本项目主线 |
| 2506.23949 AI Risk-Management Standards Profile | NIST/ISO风险控制映射，未见新的模型发布兼容性/正确性/安全约束；不把安全词视作自动机制准入 |
| 2506.24044 VLA Driving Survey | 分类/综述应用路线，题摘未给出足以修正现有VLA机制判断的新增实验或反证 |
| 2506.24102 DenseWorld-1M | 三阶段label/caption数据构造；题摘未证明新的训练表示/执行约束，不因百万数据量收录 |
| 2506.24124 Time Series See and Speak | 时序预测的visual/text表示组合；未建立通用模型表示形成或系统取舍的新增条件 |
| 2506.23342 ATGen | AL策略的annotation/服务框架，采用既有方法；题摘成本改善未建立策略成立的新条件 |
| 2506.23273 FinStat2SQL | 财报text2SQL的多Agent/微调应用，61.33%与4秒配置不是新的执行机制 |
| 2506.22937 GamerAstra | 游戏可达性应用，成熟视觉/Agent辅助粒度组合，无新增通用系统边界 |
| 2506.22708 FairMarket-RL | 电力市场公平奖励的领域配置，IPPO+LLM critic，未建立模型训练的新通用机制；科学应用暂缓 |
| 2506.21974 Social-network realism | 社会模拟实证有效性研究，未提供模型/系统能力形成机制；保留否定结论但不把领域模拟路线纳入 |
| 2506.21934 CAL-RAG、2506.21931 ARAG | poster布局/推荐的retrieval+grader+feedback/多Agent模块组合，新任务指标不建立新的长期执行选择 |
| 2506.23032 Good Regulator | recast EGRT及物理类比，未给可用于模型状态学习的可检验新定理/条件；不是以非AI主题排除理论 |
| 2506.22991 Wireless Resilience | 一般无线网络弹性综述，未具体服务模型计算或其状态/通信 |
| 2506.22355 Embodied AI Modeling World | world/mental-model研究方向的position文章，未给可核验新增机制 |
| 2506.22112 Reward Balancing Recommender | 推荐reward多样性/不确定性领域方法，未形成当前模型主线新解释 |

SceneDiffuser++（2506.21976）和4D-VLA（2506.22242）的完整题摘已读，明确有关world/action-conditioned生成与跨坐标对齐，保留潜在贡献，不因自动驾驶/机器人领域关闭；同样日期隔离，见inventory原件。2506.23844 Autonomy Security Survey完整题摘已读：风险taxonomy及R2A2/CMDP概念架构，具体安全增量尚未定，不轻率关闭；与上表安全保留项共享日期恢复条件。

局部VLM方法共同理由纠偏：root指出SG-LDM/PGOV3D原保留将任务方法泛化为通用术语；作者只重读同类完整题摘，不扩全文、不按数量收缩。三项关闭理由如上，VisTex明确保留native-text-space提示接口替代设计，Deepbench明确保留architecture/variant与部署域的评价条件，不把“能映射Ch23/Ch66”当理由。TurboVSR继续核验的不是三个成熟组件数量，而是高压缩造成的学习困难与首帧/后续帧因子化监督之间的新取舍；CAI继续核验的是caption/non-caption的attention差异和具体干预；Byte-pair visual继续核验的是foundation model视觉tokenization选择。是否最终成立必须经恢复日期后的证据限定。

## 机构来源实际处理

- OpenAI Research入口403；官方RSS完整1247项，最旧2015-12-11、最新2026-10-05。精确解析UTC发布时间本窗唯一命中 `[AI in Australia—OpenAI’s Economic Blueprint](https://openai.com/global-affairs/openais-australia-economic-blueprint)`，pubDate `2025-06-30T07:00:00+00:00`（BJT15:00）。经济政策标题明确范围外关闭。RSS不代表Research所有未收录材料；未宣称机构零研究。
- Anthropic Research当前页面前10项仅2026；有界官方站点搜索 `site:anthropic.com/research "June 30, 2025"` 未恢复Research历史段，搜索没有命中不证明无遗漏。搜索返回官方 `[model-deprecations](https://docs.anthropic.com/en/docs/about-claude/model-deprecations)` 的Opus3 retirement通知（只有日期），日历生命周期通知不新增模型机制/兼容性规则；不建立候选，历史Research目录隔离。
- Google Research pubs超时；[2025/06官方Blog](https://research.google/blog/2025/06/)通过web读取该月9篇。6/30 `[How we created HOV-specific ETAs in Google Maps](https://research.google/blog/how-we-created-hov-specific-etas-in-google-maps/)` 是地图交通应用，后续链接核查同时读到核心说明：soft clustering、时间加权及多数投票MoE用于HOV旅行分类，并非foundation-model专家路由新机制，关闭成立；6/27及更早显示与目标边界不重叠。博客不替代papers目录。DeepMind直接入口TLS失败，web读当前博客只回近期，历史研究段不可恢复；隔离。
- Meta Research连接被重置；有界官方站搜索同日返回2021同名日及当前分类结果，未给本窗历史清单，不当0命中。目录隔离。
- Qwen page1→page2跨过目标：7/22 Qwen3-Coder、6/27TTS、6/26VLo、6/5Embedding；无落在目标日期的该Blog条目，限制为所读Blog，不证明所有artifact。
- DeepSeek官方完整updates在2025-05-28之后下一条2025-08-21；所读changelog无本窗条目，官网同时已查。并非所有研究的完备目录。
- Kimi官方Blog历史列表跨过7/11K2和5/6LongThinking；没有本窗Blog条目。未扫描组织全部commit。
- Hunyuan官方Research为动态壳；按来源要求浏览器恢复尝试30秒超时并重置，未得到“全部”列表。root提供已知原始API后一次POST `https://api.hunyuan.tencent.com/api/blog/publicList`，body `{"pageNum":1,"pageSize":100,"renderType":0}`，code0、totalNum9，9条displayPublishTime全部2026，保留hunyuan-public-list.raw/request；API成功只证明当前9条，不证明2025不存在。历史官方列表/快照缺口继续隔离。
- Z.ai官方Research page1及?page=2止于2025-12，后者未恢复7月；仅当前可见论文。历史段隔离。
- Seed public_papers第1页20/242，初始动态下一页未给历史路径。DAY中root提供已知原始API后恢复 `https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token=0&count=20&order_desc=true`（blog type2）。papers按next_page_token 0→20→40→60→80，末页has_more=false，total94，但仅token20返回1项SwiftSpec（PublishDate折算BJT6/12），其余四页均缺sub_article_list，**不能把total94说成94项已读，也不能把API的稀疏payload判为0研究**；papers历史段仍隔离。Blog token0（15项）到20（18项）已跨BJT7/14→6/28，token40亦已请求（8项，has_more=false），total49而实际sub_article_list41项；其中几项标题为空。所见目标相邻条目无6/30事件，仅建立可见Blog的边界，不宣称缺失payload无本窗研究；新原件seed-*-2025-*保留。未打开无关正文。
- ERNIE Blog第2页含官方4.5正文，完整原件ernie-release：正文日期2025-06-30，article:published_time/datePublished一致`2025-06-30T00:00:00Z`（BJT08:00，窗外）。不得将同日默认移到窗内。repo目标窗口15次commit主要文档/链接/typo，未给新的模型机制release正文实测时刻。异构MoE机制线索保留但不采用。
- MiMo官方主页年代从2025-09/10跳到6/4与5/12，目标段无该主页发布，限制为主页列举的Paper/Blog。
- MiniMax Blog当前12项止于2025-10；?page=2返回同12项，不是有效历史翻页。历史目录隔离。

Google与补检 web 实际阅读/搜索结果的身份、范围及结论保留在本节（执行2026-10-06/07）；其正文不提供任何正式候选证据。其他raw/request均保留供复核。无每周发现扫描；未触发协议/会议/benchmark suite按需扫描，L0可选实现链接未扩成release队列。

## 已读核心只作为恢复资料

TM：`tm-core-full.txt`方法§2、三种TM §3、可比实验§4、局限§5、附录采样成本相关表已读。HTML两次下载部分传输，不能说全附件读完；必要命题段已到达。DTM离散随机transition与不连续监督确实超出仅重命名flow；但backbone NFE不包括flow-head，ARTM/FHTM需要T×image tokens的backbone计算，因果生成不产生论文中的DTM加速。统一text/image仍是未来方向，不能说生产统一模型已经验证。性能数字不作为本窗结论。

L0：`l0-core.txt`完整HTML，§2 REPL状态、§3 token action / discounted step return / strictly on-policy / reward / worker-pool、§4评价及task-difficulty/dynamic-sampling分析已读。不是GRPO group baseline：REINFORCE++式step normalization和DAPO式token normalization不可写成GRPO。代码运行成功reward不保证semantic correctness/安全；CPU worker+SGLangGPU和Bubblewrap均为采用的既有组件，无受控throughput对照，不采用生产scale保证。难任务训练中格式/执行reward崩溃、动态采样缓解，为局部稳定性证据；不能误写“没有执行奖励导致崩溃”的未做消融。

这些原件不证明实际公开日期。现有Books差额未作正文比较，不声称已有覆盖，不新增待采用正文；日期恢复后由root协调owner：TM→MULTIMODAL-GENERATIVE-PARADIGMS，L0的代码执行状态→AGENT-TOOL-CALLING、训练credit assignment→TRAIN-RLHF，ERNIE异构专家→MODEL-MOE（跨模态语义归MULTIMODAL-REPRESENTATION）。路线映射不是整合成果。
