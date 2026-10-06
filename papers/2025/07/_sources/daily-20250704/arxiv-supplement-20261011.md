# 2025-07-04 arXiv 增量来源补查

作者：root。检查日期：2026-10-11；原件中 checked_at 为实际请求时刻。原72项加具名漏收3项，共75项独立准入校准及非作者最终DAY已通过，具体采用边界见独核§12与日报。日期/历史来源保留不授正面Coverage或Evidence。

## 查询范围与停止

新材料只对应北京时间2025-07-03自然日。首次提交Jul2/3查询仅为有界发现，不证明当日公开；提交日期、ID月份、默认公告排期均不提供日级公开权限。不用catchup，不扫全年，不把月份库存变成全文队列。

| 实际查询 | 结果与停止 | 原件 |
| --- | --- | --- |
| language model；Computer Science含cross-list；submitted_date_first Jul2/3 | 两页134标题，首100及次34，末页Next不可见且无href | [首批](./supplement-20261011/advanced-model.json)、[末页](./supplement-20261011/advanced-model-page2.json) |
| LLM AND inference；相同scope | 9/9题名 | [查询](./supplement-20261011/advanced-systems.json) |
| agent AND LLM；相同scope | 20/20题名 | [查询](./supplement-20261011/advanced-agent.json) |
| quoted vision-language OR world model OR video generation OR vision language action | 收窄后17/17题名 | [查询](./supplement-20261011/advanced-multimodal-narrow.json) |
| quoted GPU kernel OR tensor parallel OR LLM runtime OR distributed training | 1/1题名，弥补旧硬件请求超时；非全部compiler/kernel术语覆盖 | [查询](./supplement-20261011/advanced-hardware-narrow.json) |
| 官方cs.CL七月列表skip0/show25 | 实读25标题，页面总1672仅月份库存；没有日级公告栏目。旧web缓存1669与本次1672分开，不作当天数量 | [原件](./supplement-20261011/official-csCL-july-first25.html) |

有效收窄查询181次题名、141去重身份。早期未加引号multimodal有90项，混入通用model/应用，保留响应但仅作宽标题线索；与有效主题合计177身份，非177待审论文。按相关机制/反证线索定点读72个新的精确v1完整题摘，最终来源回核再定点补3项，共75；旧8有效判断复用，不重算原7日期项。其余宽标题不宣称完整题摘阅读或全部贡献关闭。

第一次model误用most-recent submission且未正确选择CS，不作为覆盖或公开日期证据。早期hardware空表单也未保留CS/日期选中，不能解释为零命中。有效查询以CS+cross-list+submitted_date_first响应为准；page2抽取一度混入list-title，已据同一raw机械修正title/id，未改来源。

[日级公告probe](./supplement-20261011/advanced-announcement-probe.html)返回表单，明示Announcement date只支持year/month。Jul3输入不代表日级查询成功或零命中；月份列表也不提供独立公开日。停止重复已确认不支持的入口，保留必要公开日缺口，不由submission/ID/schedule推造。

## 精确题摘与当前判断

原值见[第一批43](./supplement-20261011/exact-v1-first.json)、[第二批29](./supplement-20261011/exact-v1-second.json)与各abs-IDv1原件；追加3项原件见末节。root与独核者均实际读完75份完整精确v1题摘，当前页Comments/可见版本说明未见withdrawal/erratum标记；历史月列表2507.00460明确withdrawn仍不采用。轻量说明检查不证明全站无纠错。

P表示具体潜力成立但必要公开日/身份未确认，不是本窗正式候选、评分、标准/深入完成或Books采用。经[独立校准](./independent-supplement-20261011.md#9-具名漏项与共同理由的有界校准)，75项分为57项P日期/必要身份保留、17项C、1项CLUES窗前旧事件；无尚未决定的准入项。日期未知不能把P改成C。C只关闭本项目本次贡献，不等于论文无学术价值。

| 精确v1 | 校准后处置 | 实际增量或停止理由 |
| --- | --- | --- |
| [2507.02226v1](https://arxiv.org/abs/2507.02226v1) | P | 语法关键/探索token统一温度失败；按角色调温加一致性候选重排，需核适用条件 |
| [2507.02199v1](https://arxiv.org/abs/2507.02199v1) | P | 深度复用不自动等于latent CoT；不同probe/层位不一致与增加recurrence收益边界 |
| [2507.02135v1](https://arxiv.org/abs/2507.02135v1) | P | 独立DVFS忽略CPU/GPU/memory相互作用；同能耗联合频率选择可能改变Prefill/Decode策略 |
| [2507.02076v1](https://arxiv.org/abs/2507.02076v1) | P | 独核补读§3/Fig2–3/AppendixA，预算配置与实耗偏差、难度与质量/token取舍的局部观察；不是taxonomy名称贡献 |
| [2507.01900v1](https://arxiv.org/abs/2507.01900v1) | P | 不分层位的head剪枝忽略表示尺度；高层剪枝加adaptive rescale |
| [2507.01752v1](https://arxiv.org/abs/2507.01752v1) | P | 黑盒高维优化以信息瓶颈限定泛化/隐私；理论假设未验收 |
| [2507.01438v1](https://arxiv.org/abs/2507.01438v1) | P | edge多adapter交换/串行负载；选择、异构cache/pool与batch LoRA的容量/延迟取舍 |
| [2507.02259v1](https://arxiv.org/abs/2507.02259v1) | P | 分段读取、overwrite memory与独立上下文多conversation RL，非长度宣传已证实 |
| [2507.02253v1](https://arxiv.org/abs/2507.02253v1) | P | parametric planning将有效/最优分开；中间JSON翻译可能降低成功率 |
| [2507.02197v1](https://arxiv.org/abs/2507.02197v1) | P | roleplay报告belief不必预测实际行为；控制信息/预测时距的一致性反例 |
| [2507.02182v1](https://arxiv.org/abs/2507.02182v1) | C | COBOL函数/文件/项目两agent上下文prompt，所述增量为领域解释指标，非新模型/运行机制 |
| [2507.02170v1](https://arxiv.org/abs/2507.02170v1) | C | 独核补读§3.2/3.3/4/6/8，boss调度、Neo4j/ASP、CRAG与belief prompt成熟组合；定性案例未给新协同有效性条件 |
| [2507.02097v1](https://arxiv.org/abs/2507.02097v1) | C | 精确v1为formalism与推荐use cases/open questions，不能借新版benchmark作为历史贡献 |
| [2507.02083v1](https://arxiv.org/abs/2507.02083v1) | C | SciGym系统生物学dry-lab科学发现评价；AI for Science当前暂缓 |
| [2507.01936v1](https://arxiv.org/abs/2507.01936v1) | P | 说服表现与dialogue结构理解不等价；影响LLM evaluator能力假设 |
| [2507.01923v1](https://arxiv.org/abs/2507.01923v1) | P | 内在文本质量不等于决策效果；summary/analysis及人机协作的条件差异 |
| [2507.01862v1](https://arxiv.org/abs/2507.01862v1) | C | 题摘含糊，实际读 PDF pp.2–3 §3：submit/reset 意图、确认状态、CoT/XML history 和现有后端流程的提示迁移。未给出新执行/提交语义或可靠性条件，不把状态词改写当新事务协议；不是因 GUI 场景关闭。 |
| [2507.01717v1](https://arxiv.org/abs/2507.01717v1) | C | 补读 v1 §4、§5 相关设置，实际为 analyst/generator/validator 顺序 prompt，再加关键词检索；评价是产品创意/专利领域质量。成熟工作流的应用增益，没有新委派机制或失效条件；不是因专利名称关闭。 |
| [2507.01701v1](https://arxiv.org/abs/2507.01701v1) | P | blackboard内容驱动选agent并迭代到共识，可能改变静态协作与token预算选择 |
| [2507.01599v1](https://arxiv.org/abs/2507.01599v1) | C | 实际补读 §1/2 贡献与架构：perception/planning/tools/memory、数据目录与平台流程的概念统一。没有新的执行、恢复、数据语义或优化条件；不是因 Data 平台主题已在 Books 而关闭。 |
| [2507.01489v1](https://arxiv.org/abs/2507.01489v1) | P | tool调用与语言reasoning的分层RL分离，改变原始工具回包负担 |
| [2507.01485v1](https://arxiv.org/abs/2507.01485v1) | C | BioMARS生物实验自主化；AI for Science当前暂缓 |
| [2507.01446v1](https://arxiv.org/abs/2507.01446v1) | C | 安全标题触发必要局部，实际读 PDF pp.4–9 方法：parser confidence、fuzzy risk routing、双 LLM 一致性及人工 fallback 等成熟控制组合。没有新的可验证语义正确性/安全约束；解析关键词齐全不是语义无幻觉证明。不能因医疗应用本身关闭，也不采用安全收益宣传。 |
| [2507.01413v1](https://arxiv.org/abs/2507.01413v1) | P | 通信/环境压力改变拍卖agent串通倾向，属于安全/设计反证信号 |
| [2507.01378v1](https://arxiv.org/abs/2507.01378v1) | P | 静态LLM priors与online MARL role-value mixing/动态角色，非普通UAV控制类比 |
| [2507.01376v1](https://arxiv.org/abs/2507.01376v1) | C | 制造场景agent/agentic概念分类与应用展望，未提出新执行机制或评价边界 |
| [2507.07050v1](https://arxiv.org/abs/2507.07050v1) | P | D3PM与AR的小规模压缩质量/生成速度比较，可修正条件选择；不外推普适优势 |
| [2507.03034v1](https://arxiv.org/abs/2507.03034v1) | C | 安全信号实际补读 §I/II，贡献为 non-usability/privacy/traceability/deletability 四层分类、现有技术及监管缺口的映射；不是新威胁实验、技术机制或保证。没有因日期、法律主题或已有安全章节关闭。 |
| [2507.02190v1](https://arxiv.org/abs/2507.02190v1) | P | 输出camera-space waypoint而非低层controls，需核视角/深度/embodiment映射边界 |
| [2507.02074v1](https://arxiv.org/abs/2507.02074v1) | C | 视频事故检测综述归纳fusion/dataset/architecture，无摘要内新的主线机制或反证 |
| [2507.02029v1](https://arxiv.org/abs/2507.02029v1) | C | 为澄清准入实际读 §3.3/4.3、§5 相关优化及 §6 表2–4/相应分析：模板/外部模型生成数据，沿用 Reason-RFT、SFT/GRPO，常规异构并行、recompute、warm-up 预分配等组合；当前不是新的可归因系统设计。跨任务/大小模型排名不单独构成条件反证，表文比较有数值冲突，不能照录 SOTA。关闭不因 tech report 身份、机构、单模型分数或 VLA 范围；若出现具体新失效控制/评价机制，只重开该命题。 |
| [2507.01949v1](https://arxiv.org/abs/2507.01949v1) | P | 五模式cold-start mixture学习何时thinking/不thinking，涉及视频后训练条件 |
| [2507.01945v1](https://arxiv.org/abs/2507.01945v1) | P | 长期生成用动态global/local压缩memory加一致性reward，而非只局部重叠融合 |
| [2507.01925v1](https://arxiv.org/abs/2507.01925v1) | C | S3/S13统一action-token分类、旧工作取舍与未来观点，无新原机制/检验 |
| [2507.01843v1](https://arxiv.org/abs/2507.01843v1) | P | 独立文字router调用可更换VLA/LoRA专家，不等于token MoE的成熟移植 |
| [2507.01823v1](https://arxiv.org/abs/2507.01823v1) | P | S3/Table1教师reward蒸馏与latent投影反例；蒸馏对象/权重选择不能视为自由压缩 |
| [2507.01790v1](https://arxiv.org/abs/2507.01790v1) | P | 冲突图文中的modality preference及router-head干预，可修正模态控制假设 |
| [2507.01738v1](https://arxiv.org/abs/2507.01738v1) | P | RIS失败定位在认知/感知拆分及非referent分布，loopback替代方案需验证 |
| [2507.01673v1](https://arxiv.org/abs/2507.01673v1) | C | S2局部text-query cross-attention/gate与跨view方差是成熟融合的FER应用，未建立主线新边界 |
| [2507.01504v1](https://arxiv.org/abs/2507.01504v1) | P | 已读S3；语义线索重识别揭示PII不止生物特征，安全潜力而非保证 |
| [2507.01424v1](https://arxiv.org/abs/2507.01424v1) | P | 精确v1用video未来动态表征指导VLA policy；不套最新版episodic world-model叙事 |
| [2507.01409v1](https://arxiv.org/abs/2507.01409v1) | P | 将caption属性标量映射为两端embedding插值，改变离散prompt控制方式 |
| [2507.07114v1](https://arxiv.org/abs/2507.07114v1) | P | packet loss下无偏gradient重构与有界参数漂移，非通信框架名称贡献 |
| [2507.03031v1](https://arxiv.org/abs/2507.03031v1) | C | 独核§3.1–3.4发现稠密性→参数测度概率、可表示→每个训练模型必然行为的量词/测度缺口；当前未成立新安全边界，不采用对齐不可能结论。具体纠正定理及假设可重开；不证明相反的绝对安全 |
| [2507.03019v1](https://arxiv.org/abs/2507.03019v1) | P | 不追加视觉输入的自主visual refocusing，改变晚期语言dominance处理 |
| [2507.03004v1](https://arxiv.org/abs/2507.03004v1) | 窗前旧事件 | CLUES官方NeurIPS2024完整题摘确认同作者/同核心；机制潜力不因窗前消失，但无具名修订增量，不计本窗日期潜力或新候选。只有具体新事件/修订可重开，不追旧家族公开日 |
| [2507.02283v1](https://arxiv.org/abs/2507.02283v1) | P | 独核PDF pp.6–8两阶段角色案例，专业建议与问题框定/学习机会错位可形成局部评价反例；不能因单案例/HR领域关闭，不证明训练数据因果或普遍组织后果 |
| [2507.02256v1](https://arxiv.org/abs/2507.02256v1) | P | self-consistency筛reward组件与uncertainty BO双层优化，改变昂贵模拟搜索分配 |
| [2507.02186v1](https://arxiv.org/abs/2507.02186v1) | C | 独核System Design/User Evaluation：判断/选择/摘要prompt链、交换顺序检查与既有Granite Guardian集成；用户结论引用旧研究，无本篇新训练机制或可靠性条件。admin overlap不是关闭理由 |
| [2507.02173v1](https://arxiv.org/abs/2507.02173v1) | P | DTS结构化多推理路径的偏好数据选择，与MCTS/temperature预算差异 |
| [2507.02139v1](https://arxiv.org/abs/2507.02139v1) | P | 同prompt/排序下judge分歧呈结构化retrieval差异，非随机噪声假设反例 |
| [2507.02128v1](https://arxiv.org/abs/2507.02128v1) | P | 独核§V-D同模型检索对照、§V-F初始化/迭代成本与§V-G低功耗牺牲timing，保留目标改善不等整体可行的局部边界；不是成熟RAG组合或PPA数字本身准入 |
| [2507.02057v1](https://arxiv.org/abs/2507.02057v1) | P | 组合式安全盲区；仅描述风险，不采用攻击有效性或提供攻击实现 |
| [2507.01951v1](https://arxiv.org/abs/2507.01951v1) | P | policy与process scoring共享骨干/分head、自监督PRM，需核成本/收益条件 |
| [2507.01921v1](https://arxiv.org/abs/2507.01921v1) | P | random扩量与难度/推理多样性选择的distillation样本效率比较 |
| [2507.01915v1](https://arxiv.org/abs/2507.01915v1) | P | 多目标gradient自适应重标与用户偏好方向；Pareto结论未验收 |
| [2507.01887v1](https://arxiv.org/abs/2507.01887v1) | P | teacher assistant+中等CoT缩小student learnability gap，不能默认大teacher越好 |
| [2507.01786v1](https://arxiv.org/abs/2507.01786v1) | P | eval/deploy prompt内部可分离的安全评价反证；probe不等于欺骗能力已证实 |
| [2507.01785v1](https://arxiv.org/abs/2507.01785v1) | P | 英语quality preference经translation传到多语言rater，保留偏差/coverage条件 |
| [2507.01728v1](https://arxiv.org/abs/2507.01728v1) | P | token通信生成IB与variance collapse处理；不把无线场景类比作为训练通信结论 |
| [2507.01702v1](https://arxiv.org/abs/2507.01702v1) | P | adaptive多agent更新harmful-meme测试，改变静态accuracy评价盲区 |
| [2507.01694v1](https://arxiv.org/abs/2507.01694v1) | P | 高阶gradient关联可绕norm/outlier防御，安全反证需核攻击假设 |
| [2507.01693v1](https://arxiv.org/abs/2507.01693v1) | P | 从next-token logits反求输入的短/长串隐私边界，不外推普通文本输出泄漏 |
| [2507.01652v1](https://arxiv.org/abs/2507.01652v1) | P | 线性视觉AR以真实二维空间decay替代一维位置，涉及KV/质量取舍 |
| [2507.01643v1](https://arxiv.org/abs/2507.01643v1) | P | gradual visual-backbone refinement针对connector初始化/模态语义gap |
| [2507.01633v1](https://arxiv.org/abs/2507.01633v1) | P | global与pairwise排名的rare-error/平局sample复杂度条件反例 |
| [2507.01628v1](https://arxiv.org/abs/2507.01628v1) | P | 在原运行上下文截获crash并动态更新code/config，不默认restart checkpoint总必要 |
| [2507.01598v1](https://arxiv.org/abs/2507.01598v1) | P | Muon矩阵优化器不同momentum/decay与critical batch理论，假设尚未验证 |
| [2507.01551v1](https://arxiv.org/abs/2507.01551v1) | P | policy自身process reward与masked step advantage，训练成本/熵保证未验收 |
| [2507.01541v1](https://arxiv.org/abs/2507.01541v1) | P | 独核§3/4.2–4.3：未fine-tune时升级路由更多反而退化、OOS recall与INS互损，保留训练/分布边界；threshold cascade本身不足准入，不采用SOTA或零维护成本 |
| [2507.01513v1](https://arxiv.org/abs/2507.01513v1) | P | 特定层harmful token prune随后restore benign features，安全反侧/utility未验收 |
| [2507.01368v1](https://arxiv.org/abs/2507.01368v1) | P | activation steering构造few-shot reward与paired reward-hacking评价，而非RM名称新颖 |
| [2507.01645v1](https://arxiv.org/abs/2507.01645v1) | P | 十语言的seen/related/unseen与tokenization弱相关观察，训练语言暴露可能比词表重叠更能解释迁移；已核Jul2同核心公告，不证明完整论文firstpublic或新事件，需必要日期/身份原件 |
| [2507.01543v1](https://arxiv.org/abs/2507.01543v1) | P | 外部知识改善BERT分类不自动迁移到LLM：上下文立场污染目标文本判断、CoT不消除/微调部分缓解的反证主张；仅准入，ACL Findings先稿身份/公开日未核，不采用降幅或所有RAG有害 |
| [2507.01594v1](https://arxiv.org/abs/2507.01594v1) | P | 独核精确v1§3/4/5.1/Table2，短期情绪与长期任务奖励在有噪声交互中未同时支配各目标，保留多目标/评价取舍；不套新版标题，不授通用最佳架构/真实用户满意 |

## 必要决定核心与版本纠偏

[root决定核心原件](./supplement-20261011/admission-core-root.json)只消解准入歧义，不是候选Evidence完成：02029完整S2/S4及另读S6，01823完整S3/Table1，01925 S3与S13部分，01673 S2的2.4/2.5局部，01504完整S3；未读全部评价/附件。独立复核者另实际读取17项具名决定core，位置与裁决见独立记录§5–7；root不把复核者的局部阅读声明为自己读完全文。

02097的Advanced最新版AB含新评价，但精确v1是formalism/perspective；01424精确v1是video动态表征，不是最新标题中的episodic memory；01551精确v1名称为Masked Step Advantage，01598为Analysis of Muon's Convergence and Critical Batch Size。后续改名/改写不自动成为2025-07-03事件，也不移动旧候选。

CLUES在[NeurIPS2024出版页](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ff80e644be415af4bcd7e4b4efb2152f-Abstract-Conference.html)有相同核心梯度数据选择，窗前事件关闭；只定点查此身份，不扩会议全集。EvalAssist admin重叠说明指向2410.00873，但实际方法阅读才支持当前集成贡献关闭，不由新ID或overlap标签倒推结论。

## 机构来源独立核对

root完整读[Anscombe机构记录](./institutions-supplement-20261011.md)，并从原响应核MiniMax本日全部短正文/可见日期、DeepMind publications page2完整目录跨Jul13→Jul1→Jun26、Seed四JSON元数据结构及Hunyuan返回结构。MiniMax仅既有Hailuo-02渠道集成，不采用extreme physics宣传；Seed portal日期不自动等于论文首次公开。

root已从JSON/XML及真实RSC字符串独立重算：Seed论文18+20/Blog18+18及has_more/next，四数组本日均0；Hunyuan9/9及displayPublishTime对应9个2026日；OpenAI1287及Jul1→Jul8目录段；Anthropic177次publishedOn/168时间值、Jun27→Jul15段，本日0。仅这些原响应的实际有界结论，不继承其他日完成标签。MiniMax C及ByteDexter窗外邻项不计75个arXiv新题摘或旧7；机构全部尝试不等于全部Coverage通过。

## 公开日与恢复位置

表内57项P按具名精确版本请求官方历史日级公告、作者首次公开原文/公告或可定位原公开日期的出版记录；必要身份需同时能区分先稿家族与本次增量事件。只需日级，不索取秒级。原七项旧请求/日期保持，本轮不迁日；新增不使用旧09:00窗口的时刻义务。01645已核Jul2公告不再请求，只需正文firstpublic/本次新实质事件；01543的ACL Findings身份与其v1分开确认，venue名称不证明日级日期。

全部75项准入、来源/停止与最终DAY已独核通过，无研究普通待办。57项缺日级原件/必要身份的P按身份作为本窗终态保留项隔离在日报§5，不评分、不采收益、不进Books、不授Coverage或无遗漏；没有把75篇扩大为全文/日期考古队列。收到必要原件只重开表内受影响身份，落窗后评分并推进相应证据/Books；若原件明确窗外，只记录真实归属，不迁旧材料。17项C不为不影响关闭的日期另建请求，CLUES只接受具体新事件/修订，不重复索取旧家族日期。

## 最终来源复核中发现的具名漏项

root回核Advanced model page2实际响应时定点发现[2507.01645v1 — Adapting Language Models to Indonesian Local Languages](https://arxiv.org/abs/2507.01645v1)，已另读官方精确v1完整题摘、comments与版本页，[本次原件](./supplement-20261011/abs-2507.01645v1.html)。这不是扩扫新分类或将余下宽标题建全文队列；原72项准入仍有效。Ptolemy随后只在同页用Indonesian/sentiment及该ID定点核另外两项潜在同类漏收，实际新增3P；75项数量已同步，不据此预签DAY。

完整题摘的具体增量是十种低资源语言中seen/partially-seen/unseen的迁移差异，以及subword fragmentation/vocabulary overlap弱相关而prior language exposure预测更稳定的局部观察；不是情感分类应用分数本身。已独核保留P：只凭词表重叠/切分粒度解释跨语言能力可能遗漏训练语言暴露与语言亲缘条件。未证实因果关系、通用最佳adapter或全部大模型泛化。Comments为AMLDS 2025，仅一v1、submitted Jul2；这不是firstpublic，必要会议先稿身份/公开日期仍待原件。当前不评分、不授候选Evidence或Books。

随后只搜索此精确标题/AMLDS身份，发现[作者机构公告](https://dcse.fmipa.ugm.ac.id/peneliti-dike-ugm-kaji-strategi-adaptasi-language-model-untuk-bahasa-bahasa-daerah-indonesia/)。已读完整正文：页面发布日期2025-07-02，正文June30为叙述日期，AMLDS July19–21为会议日期，均不能改写为本日公开。公告已经披露seen/related/unseen条件、MAD-X语言/任务adapter分工及tokenization不能单独解释迁移的同核心观察；[原响应](./supplement-20261011/01645-author-institution-announcement.html)保留身份与日期。公告披露日不直接证明论文完整正文首次公开日；是否另有本日新正文/实质增量事件仍由独核区分，不能仅新arXiv上传就再计新贡献。第三方索引仅恢复IEEE DOI/11159428身份，官方IEEE页面cache miss，不授正式发表日期或全篇读取；不扩会议历史。

另外两项精确原件：[01543v1](./supplement-20261011/abs-2507.01543v1.html)、[01594v1](./supplement-20261011/abs-2507.01594v1.html)。root均另读完整题摘/comments/版本，Ptolemy已独核且为01594另读决定性局部：实际v1标题为Emotionally Intelligent Task-oriented Dialogue Systems，而不是Advanced最新版的All Learning Has an Emotional Basis。01543的外部上下文反证潜力与01594的多目标取舍潜力、版本边界和未检查范围见独核§9；共同扩查只这两个具名身份，不声称余下标题已全量关闭。原17决定core加01594局部为18项；root不自称读取后者core或完成候选证据。
