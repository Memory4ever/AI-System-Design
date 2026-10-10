# 2025-12-01：禁止 catchup 后的有界历史发现

本轮作者：当前12-01单日续跑会话，接续Avicenna修后材料；不是Sartre或其他非作者。请求执行时间为 **2026-10-07T16:44:21+08:00 ～ 16:56:05+08:00**，整理与检查随后执行。只写本日README和本日_sources，不改旧原件、State、Books、合同、索引，不stage/commit/push。

## 授权、复用与当前停点

补充窗口仍为 **2025-11-30 ～ 2025-11-30**。旧窗口、候选日期/评分/归属和有效审阅冻结。最新用户明确禁止使用catchup；本轮没有请求任何catchup URL。旧失败原件仅是旧请求事实，不再用90天限制阻止历史发现。

实际重读main当前AGENTS、Prompt、研究合同、Report合同、来源使用说明/每日组/arXiv说明、ROADMAP和State本日路由；随后只读本日README、Avicenna记录及Sartre首校准/修后追加。Sartre **16:24:46** 已定点确认DeepMind修复，日报此前“未返回”已过时；该确认只通过这一项，不授全日最终验收。八项v1窄潜力、两项撤回和Super公式隔离复用，不重读七篇普通方法或改日期。

**本批准备好非作者首校准，未完成独立验收。** 最终有界题名观察65次，按arXiv ID合并45个身份；其中8个为上轮身份、22个新身份读完整精确v1题摘、15个仅按明确范围外题名关闭。22项题摘中17项保留潜在准入、5项排除。相对本日原记录新增身份37，新增潜力17；本轮新增确定落窗候选仍0。此数字只属于下面明确的题名切片，不是全月、全年或当日事件数。

## 实际入口与分页停止

原件、逐请求UTC起止时刻、HTTP状态/错误、最终URL、响应字节与SHA256保存在 [history-discovery-20261007/](./history-discovery-20261007/)。脚本只负责请求/解析，不替代贡献判断；`.parsed.json`是可重算的检索投影，不是审阅收据。40次请求中API为500，其余39次HTTP200；HTTP200不证明日期过滤正确。所有旧原件未覆盖。

[官方Advanced说明](https://arxiv.org/search/advanced)本轮web实读：公告筛选与排序仅年月，原始提交筛选另有日粒度；多词精确短语须加引号。首次非精确model请求与同月空页另存，不能混入有效发现分母。

全部Advanced实际选择Computer Science、包含cross-list、all字段、size50、start0；以下是各自实际查询及停止，不取总命中数作为已读数。

| 原件前缀 | 查询及实际响应 | 本轮使用/停止 |
| --- | --- | --- |
| `model-announced-start0` | 初次未加引号的language model OR Transformer OR mixture of experts；公告参数Nov1～Dec1；1–50/4618 | 术语过宽的探测。曾展示该页题名，但未建立这50项的完整贡献判断；被下面精确短语查询替代，不并入本批分母、不翻start50。 |
| `model-exact-announced-start0`、`systems-announced-start0`、`multimodal-announced-start0`、`agent-announced-start0` | 公告参数Nov1～Nov30，四组均“Sorry, your query returned no results” | 同月日期粒度异常探测，不是本窗零论文证明；跨月参数随即恢复结果，没有以空页结束发现。 |
| `model-exact-announced-fixed-start0` | `"language model" OR Transformer OR "mixture of experts"`；公告参数Nov1～Dec1；1–50/4120 | 实际题名切片1–15，从23478至23355；其余16–50及start50以后未作贡献判断。 |
| `systems-announced-fixed-start0` | `GPU OR decoding OR kernel OR "inference serving"`；同公告参数；1–50/1031 | 题名1–15，从23469至23120。发现EEG、纠错码、农业等噪声后收窄为下面systems-narrow；不继续宽查询分页。已有有效相关判断保留。 |
| `multimodal-announced-fixed-start0` | `multimodal OR "world model" OR "vision language action" OR "diffusion model"`；同公告参数；1–50/1398 | 题名1–15，从23478至23269；不翻start50，不全扫cs.CV/cs.RO。 |
| `agent-announced-fixed-start0` | `agent OR "retrieval augmented" OR "language model evaluation"`；同公告参数；1–50/1449 | 题名1–15，从23476至23193；传统博弈/控制/领域流程按语义区分，不把Agent标签当准入。 |
| `systems-narrow-announced-fixed-start0` | `"language model" AND inference`；同公告参数；1–50/484 | 定点补浏览1–5：23473、23455、23436、23300均与本批已有身份重合，23271为新增；止于5，不声称50项已筛。 |
| `model/systems/multimodal/agent-submitted-start0` | 上述精确短语四组，`submitted_date_first`参数Nov28～Dec1；分别1–50/338、91、130、126 | 只检查响应范围/排序及题名线索；首页含后续月份甚至2602身份，原始提交不等公开。没有把这些结果并入当窗候选或强制逐篇队列，没有翻页。 |
| `api-topic-window` | Atom：`((cat:cs.CL OR cat:cs.LG OR cat:cs.DC OR cat:cs.AI) AND (all:"language model" OR all:"GPU" OR all:"agent")) AND submittedDate:[202511280000 TO 202512010000]`；start0/max25，submittedDate降序 | HTTP500/913B，错误原件保留，不授零命中；Advanced成功发现照常继续，不由API失败阻止其他入口。 |
| `month-dc-nov-start0` | [官方cs.DC月表](https://arxiv.org/list/cs.DC/2025-11?skip=0&show=25)，1–25/338，从2511.00038至2511.02034 | 只探测目录顺序和月初边界，未逐篇题摘筛选；止skip0，不把338项或月初页当Nov30公告。旧cs.CL首尾探测复用原记录，不新增全分类队列。 |

五个有效公告查询用跨月参数恢复，实际本批条目均显示originally announced November2025。这只支持月份；排序中的编号接近、Nov28 v1提交、abs的citation日期和后续出版年均不授Nov30公开。不是声称参数精确截取了目标自然日。

## 身份、准入差额与审阅边界

旧八ID23478/23477/23476/23473/23469/23455/23429/23436只去重与复用Sartre有效校准。以下全部是**潜力、首校准待返、具体日隔离、未评分、无Books采用**，不是17项已确认当窗候选。每项原件为`abs-<ID>v1.raw`，22份abs均完整读取题名/Abstract/Comments/当前版本史字段；未见withdrawn或具名纠错声明只支持这些页面的轻量观察，不授全版本史检查。

定点检查本日旧_sources/Avicenna记录及Nov28/29/30现存README未见下列17ID；不是全仓库去重证明。搜索页可能显示后来题名/摘要，判断只用精确v1。例如23271检索题名Learning a Single Token，而v1题名为Behavior-Equivalent Token；LFM2当前其他模型发布事实也不能反填论文首次公开。

| v1身份 | 约束 → 实际增量 → 需要核验的选择 |
| --- | --- |
| [AnyTalker 2511.23475](https://arxiv.org/abs/2511.23475v1) | 多人音画同步受身份扩展与多人数据成本约束 → identity-aware attention迭代处理identity/audio pairs，单人训练后少量多人交互精化 → 身份扩展与数据需求的机制/边界；未审消融与成本，不授任意人数质量。 |
| [SmallWorlds 2511.23465](https://arxiv.org/abs/2511.23465v1) | 奖励或任务成功不能单独识别动力学理解 → 可控、全观察状态六域和长rollout退化比较 → 区分动力学模型与任务分数。小受控环境不自动排除，未审可比预算、指标与归因。 |
| [One-Shot Patching 2511.23408](https://arxiv.org/abs/2511.23408v1) | 已公开漏洞评价可能代表不了人工构造漏洞 → 同时比较两类漏洞，用PoV执行判断修补并观察模型互补性 → 评价分布与判成功边界；未读协议，不声称污染是已证原因或PoV充分保证安全。 |
| [LFM2 2511.23404](https://arxiv.org/abs/2511.23404v1) | CPU延迟/内存与模型能力共同约束架构 → hardware-in-loop搜索、短卷积/GQA骨干及避免support mismatch的Top-K蒸馏 → 架构选择和蒸馏支持集接口。题摘明确机制即可保留，2x及所有模型指标不采用。 |
| [Attention-based PEFT 2511.23375](https://arxiv.org/abs/2511.23375v1) | 全量调参贵，任意挑层未必命中视觉能力组件 → 图像关键对象上的Head Impact用于选PEFT组件，并比较高/低/随机HI → 参数位置选择能否具有预测价值；未把attention相关性当因果或解释真值。 |
| [Quantized-Tinyllava 2511.23402](https://arxiv.org/abs/2511.23402v1) | split learning传输高维embedding昂贵 → 学习低比特embedding压缩、按entropy coding确定离散层数 → 通信/质量取舍和分割接口。未认证理论假设、隐私保证或所有foundation模型收益。 |
| [VQRAE 2511.23386](https://arxiv.org/abs/2511.23386v1) | 语义理解与生成codec常用双encoder → 同tokenizer输出连续语义和离散生成token，冻结encoder学高维codebook后自蒸馏联合更新 → 表示共享及codebook维度取舍。100%利用率/质量外推不采用。 |
| [Chart2Code-MoLA 2511.23321](https://arxiv.org/abs/2511.23321v1) | MoE/LoRA组合本身不足准入 → 题摘具体给element-count/complexity结构量路由及稳定性训练、LoRA-only对照 → 结构量是否改变跨类型泛化和路由预算取舍。17%/18%/20%未审不采用；不是按图表场景直接高分。 |
| [ASTRO 2511.23442](https://arxiv.org/abs/2511.23442v1) | 离线碎片轨迹的生成式拼接可能违反动力学 → temporal-distance选择可达目标、实际rollout与目标轨迹差反馈修正连接动作 → 合成训练轨迹的可达性/动力学一致性准入；主线联系是模型驱动的训练数据与行动约束，不是一般RL任务数字。效果和迁移未审。 |
| [DDAM 2511.23347](https://arxiv.org/abs/2511.23347v1) | 只本地更新的关联记忆无法选择性吸收分布式动态key/value → interest matrix、路由树在线梯度及delay/path-length regret → 内容记忆更新与通信延迟边界。决定范围的§II/TableI另读，确实列Linear Attention/DeltaNet等cost，不仅凭Transformer类比准入；定理未审不采用。 |
| [SafeHumanoid 2511.23300](https://arxiv.org/abs/2511.23300v1) | 语义动作成功不等物理接触安全 → 检索已验证阻抗payload、低频语义/本地控制分层与fallback，且评价/动态响应边界具体可核 → 参数白名单能否授安全及何种成功分母。必要§3～7另读，保留安全反侧，不能因有RAG/fallback或16场景就认证安全。 |
| [MCP/RAG/NLWeb/HTML 2511.23281](https://arxiv.org/abs/2511.23281v1) | web界面改变agent工作量，单排行难分接口贡献 → 同四模拟店/任务比较四种接口的成功与成本 → 接口设计怎样影响有效性/取证成本。specialized agents与预爬取成本等混杂未审，不采用性能或RAG普遍优胜。 |
| [MCTR 2511.23262](https://arxiv.org/abs/2511.23262v1) | 只保存记忆或只做行动推理难区分适应来源 → 规则/行动结果记忆与action模块test-time RL共同演化，seen/unseen游戏比较 → 参数学习与显式记忆的贡献分离。未把“metacognitive”命名或9/12结果当类人适应证明。 |
| [Edge ViT energy 2511.23166](https://arxiv.org/abs/2511.23166v1) | accuracy-only/device-agnostic筛选可能改变实机部署选择 → NetScore筛选后SAM在TX2/RTX3050实测，报告不同架构获益 → 硬件条件是否改变质量/能耗排序。小ViT实验不因规模排除，未审metric权重/测量对照，不采用53%。 |
| [PointCNN++ 2511.23227](https://arxiv.org/abs/2511.23227v1) | voxel量化损精度、native-point计算贵 → 把点卷积表示为MVMR并做GPU kernel，voxel为特例 → 3D表示的几何保真/执行成本边界；不只登记点云应用指标。未读kernel/公平对照，不授速度、内存或已开源。 |
| [OctoMed 2511.23269](https://arxiv.org/abs/2511.23269v1) | 统一reasoning trace长度未必适应不同任务 → 混合结构化trace长度的SFT后观察无需显式长度监督的任务适应 → 数据长度配方如何形成计算策略。潜力是训练机制，不是医疗指标或AI for Science应用；该跨任务归因未审，不采用医疗能力/鲁棒性保证。 |
| [Behavior-Equivalent Token 2511.23271](https://arxiv.org/abs/2511.23271v1) | 长system prompt占上下文/成本 → prompt-specific token先重建内容再蒸馏行为的三阶段训练 → 可学习压缩的行为保持/迁移边界。题摘说无model-internals访问，不等纯黑盒API可部署；3000x/98%和任意提示等价均不采用。 |

### 两处决定事实/安全的必要core

**DDAM精确v1 §II/TableI/Assumptions1–3**：`core-ddam-v1.raw`已读这些部分。问题是每节点的记忆参数X及key/value回忆损失，interest weights与物理graph分开；TableI确有线性注意力、gated attention、DeltaNet等cost表达。分析假设凸cost、闭凸有界domain及有界梯度，不能把该理论直接授非凸LLM端到端训练或任意Agent记忆。§IV算法、§V证明、§VI实验未审；只把模型记忆/通信的潜在联系确立，不认证regret结论。

**SafeHumanoid精确v1 §3～7/Table1**：`core-safehumanoid-v1.raw`已读。Molmo-7B BnB4bit视觉语义→384维embedding/FAISS精确近邻→16行人工验证参数表，29值payload在本地50Hz执行；camera 1–2Hz，失联/歧义fallback是作者声明的机制。§5.4的success定义是阻抗/速度按语义调整，Table1为定性示例；§4.4描述nominal-load筛选及对照ISO guidance，没有在这些段落展示完整接触力/距离/延迟分布与全部危险状态定量保证。§6～7承认offboard RTX4090/Wi-Fi链路延迟可到1.4s、动态HRI不适用、预设目标pose和手工数据库限制。因此**不授standards-compliant/物理安全证明**，但也不能断言全部实机无效。安全反侧须由非作者检查；未查代码、复现、认证标准正文或其他附件。

### 五项读完整题摘后排除

| 身份 | 具体理由（不靠访问/工作量/规模） |
| --- | --- |
| 2511.23377 DEAL-300K | MLLM生成编辑指令、diffusion编辑、active-learning标注和冻结VFM/MFPT服务伪造区域定位。题摘未建立本项目基础模型生成机制、可靠性边界或训练设计修正；数据量/F1与模块组合本身不足。 |
| 2511.23315 Independent MARL phase structure | IQL/环境密度/TD方差揭示一般去中心化控制相变；题摘未把这些实验与模型能力形成、LLM协作执行或VLA foundation policy的具体机制建立直接链路。不能用系统类比转成Agent可靠性定律。 |
| 2511.23220 Tabular instruction tuning | Llama3.1 SFT、7K指令/A100<6h和GPT-4o指标相近，未提出可比预算下新的学习机制/失败边界或可行性证据链；新任务与一次资源数字不足准入。ICML2025 workshop信息保留，不需追日期来改变该排除。 |
| 2511.23454 Debate winner rules | uninformed principal、verifiable arguments和策略获胜的博弈框架；题摘没有LLM/verifier不可靠性或模型驱动推理机制连接，不能凭debate词移入LLM评估。 |
| 2511.23397 MegaChat | Persian Telegram销售Q&A合成、multi-query/rerank/persona组合，GPT-5.1 judge六维、4/5channels优势；题摘没有分清合成质量、judge混杂或新执行机制，领域数据与组合指标不足。 |

上述排除项不评分，不因日期未核实另建材料请求；其余22项中的17潜力不因日期限制缩池。

### 十五项明确范围外题名关闭

仅题名足以界定领域应用且本切片未见撤回/纠错/安全反证信号；非作者仍须分层抽检，不冒称全部摘要已审：23450 object-detection数据合成；23387 weather-report流程；23366 inventory replenishment；23384 motor-imagery EEG；23355 bedside physiological extraction；23352 Wi-Fi bandit；23287 Bangla author-intent分类；23276 HFMD预测；23222茶叶病虫检测；23221 3DGS-SLAM smoothing；23202纠错码解码；23193CAV on-ramp MARL；23162EEG ERP估计；23142神经codec用于EEG；23120antimicrobial peptide设计（暂缓AI for Science）。不是断言这些研究没有学术价值，也不把GPU/kernel/agent/Transformer词当准入。

## Books权限与唯一owner提案边界

所有新增拟入选项缺具体公开日，且17项首校准未返，**本轮没有可落实的Books采用差额，Books改动0**。不以未写书或已有一般原则改贡献/评分。当前只对读Ch14开头的content-dependent routing与Ch26开头的proposal/controller、安全envelope和非平均success约束；没有对读其他owner全文或宣称17项已有覆盖。

给root的必要路由：DDAM若后续日期/证明通过，唯一机制owner建议`MODEL-SELF-ATTENTION`，讨论memory update目标与延迟/interest matrix约束，不另在AGENT-MEMORY复制；SafeHumanoid安全反侧若需采用，唯一owner建议`MULTIMODAL-EMBODIED-VLA`，比较Ch26现有“模型proposal不持有安全commit”论点，具体新案例是validated parameter lookup的成功指标不能自签动态安全。后者现有原则已承载一般边界，是否值得新增案例尚待日归属与非作者证据确认；不是已认定有书稿长效差额或请求写入锁。其余只保留上表具体潜力，不提交空泛多owner整合补丁。

## 非作者复核请求与精确checkpoint

1. 复用Sartre16:24的DeepMind定点确认、原八项潜力/撤回/Super隔离；只核README本次同步，不授旧结果新权限。
2. 检查本轮无catchup、月份/提交/日归属分离、同月空页与API错误没有变零命中、systems收窄、65次题名/45ID与停止位置。未筛库存不是待审候选或外部故障。
3. 全部17项拟潜在准入做首校准，必要范围是各自v1完整题摘及上面两个core；安全项SafeHumanoid必须看实际§3～7，不用摘要“safe”认证。DDAM/TableI、OctoMed训练而非医疗应用、PointCNN几何/计算、局部负面/小模型准入是本批易误判点。
4. 五项题摘排除和15题名排除按来源/主题/理由分层抽检，记录实际样本和未核范围；发现共同错误理由只扩查受影响集合。不要求全部潜力方法/实验陪读。
5. 当前仍缺17项具体日：可接受官方历史公告/列表的具名日证据，或作者首次公开正文/项目的具名直接日期；到达仅重开相关身份。现阶段不评分、不采用性能/安全、Books或无遗漏断言。原八项日期请求和其他源缺口保留，不重复按库存索取材料。

**普通工作与外部缺口分开**：本轮首校准及日级最终复核是可执行待办，不是外部访问故障；17项方法/评价/证明尚未审，是日归属与准入之后的相应阅读范围，不称已完成证据。Google pubs此前目标日/主题筛选没有被证明全部穷尽，默认页恢复不意味着facet已生效；仍保留该精确待恢复范围，不能把678全年库存转队列。Hunyuan/Z.ai历史目录、MiMo缺日期route等先前请求事实不由本批arXiv成功改写。本批不是宣布全部扫描完成的日级final-review包。

本轮另于16:54左右web打开Google pubs默认页成功，697行；可见2025 facet678与1–15/11597，只支持默认页成功，未点击生效筛选/读全年正文。这与Sartre既有修后观察一致，不为该未完成工作授新通过。

**后续精确起点**：非作者先校准本批17潜力与代表负侧；有新具体日证据才按真实归属定点审必要方法/对照/反证，不能把月公告改填Nov30。不创建其他Daily/Weekly，不移动旧候选，不接手共享Books/State。全日状态继续进行中。

## 机械检查

17:02之后实际运行当前V3校验，1份报告退出0；限定本日README/_sources的`git diff --check`退出0。README、Avicenna补查与本续跑记录的本地相对链接缺失0、行尾空白0。结构化复算确认65次题名/45ID、22份精确v1 abs、40次请求（39个200、1个500）、catchup请求0。实际顺读本日README diff，旧窗口与旧材料未搬移，Sartre作者身份/旧结论权限分开。

未执行stage/commit/push；运行前已有staged/unstaged及无关改动原样保留。机器校验不替代上述首校准、日期核验或日级最终通过。
