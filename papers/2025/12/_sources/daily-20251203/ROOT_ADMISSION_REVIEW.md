# 12/03 Mill 独立日级复核

复核者：Mill，agent ID `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e`，非作者 Gibbs。2026-10-02T18:40:08+08:00。本日先前无ROOT文件；此处为实际新建日级记录。

结论：未通过

## 日级范围

已换日独立重读AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、来源使用说明/每日组/arXiv主题、Prompt、ROADMAP、03 README和WINDOW_REVIEW；相关state定点检索无本日checkpoint。窗口 `[2025-12-02T09:00:00+08:00,2025-12-03T09:00:00+08:00)`。不加载旧Weekly/其他月份候选池。

14源停止范围逐项审计：OpenAI作者本轮成功RSS邻接Dec3 08/10Z均晚于右端，只支持feed切片；AnthropicDec2精确非午夜字段落窗；Google Blog/DeepMind第3页Dec3日精度相交必须具名处理；Meta第4页Dec1/Dec12夹窗，只定点复用AdvancedIF同身份旧机制；Qwen旧Sep23/新站部署有限恢复、Hunyuan All11项全2026、Z.ai两页至Dec7与release Dec8、MiMo Paper8项/路由无date与旧More分别保留历史缺失，不授无事件。DeepSeekDec1 release同家族日精度恢复不重复采用，Moonshot26项最近Nov7/changelog Nov6、ERNIE两页至Nov7及Nov21/Dec9、MiniMax13项Oct27/Dec23限制各原入口；Seed首段GR-RL Dec2/Oct22和Blog Dec2/Nov27仅日精度，具名题摘/身份有效结果定点复用02，不授时刻。

这14项是全部范围记录审计，不声称本复核独立重请求14个目录。固定邻接事实只定点回看原观察并按03边界重判。03四主题日期查询越日期已停止，没有把关键词命中当日期证明。独立原站cs.DC/cs.CV各首23条成功：网页工具Cache miss后一次原生HTML有限恢复，47,206/49,440 bytes；仅展示/浏览1–23，未翻月库存。初次本地解析器缺依赖/语法错误不计源成功，改用标准HTMLParser成功，不安装库。

## 确定落窗家族：Anthropic工作研究

实际访问[官方原文](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)及Research原生HTML。Research `publishedOn`、单页 `article:published_time`、JSON-LD `datePublished` 和time标签一致给 `2025-12-02T18:58:43.576Z`，换算03 02:58:43.576BJT完全落窗，不是午夜日编码。单页另有 `dateModified=2026-09-10T18:17:26Z`；本复核读的是当前官方正文，不宣称恢复2025冻结快照，也没有仅凭modified时间扩扫版本史。

核心、完全委派口径、Claude Code usage/Figure3、Appendix Limitations实际独立读：132调查/53访谈与200,000内部轨迹是不同证据单位；mean maximum consecutive tool calls测轨迹活动，而非正确完成概率；survey的fully delegated从无需验证到轻量监督理解不一。比例采样不支持绝对产出，非匿名、便利/目的采样与回忆/选择偏差不能由更少human turns消除。故“自治活动!=可靠委派/成功”窄准入与2+1+2=5可接受；标准证据足够支持局部测量边界，不采用自报生产率因果收益、任意公司推广或监督技能必然衰退。

Books实际对读 `PLATFORM-EVALUATION-SYSTEM` Ch66“从目标到证据，而不是从指标到目标”链路与EvalSpec的target behavior/eligible population/failure/scorer，以及此前delivered_success区分；Ch67开头只观察不定义规范性质量，Ch84 runtime/effect/terminal evidence和Ch81 AwaitingApproval/Verifying状态机交接。该窄规范已被Ch66具体承载，已有覆盖成立，不因局部趋势制造Books新机制。唯一主owner Ch66，其他章只交接，没有Books修改。

## 7项拟准入和安全侧

下列全部独立打开精确v1完整题摘及版本/评论字段；不是完整Evidence Gate，日期继续隔离、不评分。SIMPLE `2512.00719v1` 原同身份有效准入仅定点复用，未重复全文附件。

| 精确材料 | 窄校准 |
| --- | --- |
| [IslandRun 2512.00595v1](https://arxiv.org/abs/2512.00595v1) | typed placeholder可逆匿名化/信任域路由是潜在设计线索，不采用“新范式”或隐私保证；框架声称Kubernetes等只优化单维不能当成熟系统事实 |
| [SmartFed 2512.00902v1](https://arxiv.org/abs/2512.00902v1) | rank-wise LoRA experts按输入/预算激活及跨矩阵quota，潜在复用/预算机制，不仅排名 |
| [Joint Partitioning 2512.01039v1](https://arxiv.org/abs/2512.01039v1) | 为避免泛化架构词，另读HTML §II–III/Alg1：profiling驱动keep/remap/resplit，cooldown与trusted partition约束确有具体形式化线索。只校准该窄潜在增量，不采用“privacy at no cost”或QoS保证，未把argmin伪码当已验证求解器 |
| [Tangram 2512.01357v1](https://arxiv.org/abs/2512.01357v1) | tensor驻留复用、按需KV与GPU affinity有状态成本线索；不采用最大加载数字作端到端普遍保证 |
| [Fantasy 2512.02278v1](https://arxiv.org/abs/2512.02278v1) | 超单卡index下GPUDirect Async重叠search/transfer改变stall边界，不能直接授任意召回/latency或RAG质量 |
| [Adapter Shield 2512.00075v1](https://arxiv.org/abs/2512.00075v1) | 授权恢复embedding与未授权生成分开，潜在安全机制成立；摘要“universal/authentication”不证明任意攻击或密钥安全 |
| [SemImage 2512.00088v1](https://arxiv.org/abs/2512.00088v1) | HSV辅助监督/语义boundary rows为表示替代分支，不因CNN小模型删除；可视化不证明可解释性因果，月表当前改题不能覆盖精确v1身份 |

TokenScale/FFTrainer/Gate-Norm只保留作者所述窗外提交线索，不以它们填本窗first-public，也不重复扩查窗外全文。当前官方abs的submission和月身份均未升格公告日。

## 普通缺项：9项定点归并

这里只重开作者已经声称浏览的cs.DC/cs.CV首23及Google Dec3边界，不把46条标题变成全量题摘/深审队列。全部下列题摘/核心说明已由本复核实际读到，作者应归并具体贡献/重复处置；可关闭项不要求无限恢复日期。

| 材料 | 实际发现与补齐方向 |
| --- | --- |
| [Capturing Human Preferences with Reward Features](https://deepmind.google/research/publications/141313/) | 独立完整原站摘要：user-specific reward features、PAC中raters数量/异质性、快速适配是具体潜在线索，不能只写Dec3日期隔离。Download指向 `openreview.net/pdf?id=TgCkj4uEPl`，实际challenge，未取得PDF/早期公开证据；应记录潜在机制及同事件去重/first-public需求，不拿NeurIPS年字段授日 |
| [From Waveforms to Wisdom / MSEB](https://research.google/blog/from-waveforms-to-wisdom-the-new-benchmark-for-auditory-intelligence/) | 原Blog核心与评价限制已读：semantic tasks对ground-truth text、acoustic tasks对dedicated solution，WER与下游目标错配/复杂模型反证是潜在评价增量，不以“新增8任务榜单”准入。“maximum potential”不是可证明上界。关联 `openreview.net/forum?id=X0juYgFVng` 实际challenge；日期仍日精度，但不能不读核心而结束 |
| [FlexiWalker 2512.00705v1](https://arxiv.org/html/2512.00705v1) | abs Cache miss，HTML完整摘要/引言实际成功：dynamic transition打破预计算、rejection/reservoir kernel与cost-model选择。不是泛泛GPU题名即入；当前只支撑graph random-walk采样，若无具体模型/系统迁移约束可窄关闭，不借GPU名称制造LLM采样保证 |
| [Delta Sum 2512.01549v1](https://arxiv.org/abs/2512.01549v1) | gossip averaging/global convergence与拓扑规模，潜在训练聚合边界；需具体新aggregation/适用条件而非把OAM术语当新平台机制 |
| [Active Storage 2512.02646v1](https://arxiv.org/abs/2512.02646v1) | compute移向dataClay active objects、内存/训练时间取舍可能系统相关；需必要架构段判断实际新增约束，不能因只是framework或小模型默认排除 |
| [Data-centric VLM 2512.00042v1](https://arxiv.org/abs/2512.00042v1) | Qwen2.5VL-32B数据组成/QMSA reasoning syntax与SFT竞争命题，不能只按exam域排除；摘要本域排名不够，具体新增受控机制/混杂决定是否关闭 |
| [PEFT-DML 2512.00060v1](https://arxiv.org/abs/2512.00060v1) | shared latent space面对sensor dropout/unseen modality combinations，是可能的融合成立条件；应核是否仅现有LoRA/adapter组合应用，不自动按autonomous-driving排除 |
| [Diagnostic prompting 2512.00082v1](https://arxiv.org/abs/2512.00082v1) | 200页面/人类标注、巨大相对F1提升却低绝对kappa、模型与人类特征偏好不同是必要评价反证；不能以Amazon应用或+858%宣传跳过 |
| [MCU ODL 2512.00086v1](https://arxiv.org/abs/2512.00086v1) | domain shift时临时深度sensor伪标签与memory-driven sparse update，潜在资源/适配机制；不采用300mW/1.2MB作通用性能，不按107k小模型默认关闭 |

9项指作者记录补齐与仅必要的含糊事实核验，不是9篇都要深入审阅。贡献已清楚而日期真正穷尽后可安全隔离；未知日期不能遮蔽未执行判断。Google paper原始PDF challenge是有限外部缺口，不无限请求。

普通负侧另分层抽读：`2512.00125v1`完整摘要为工业inspection中现有domain randomization/compositing+YOLO/MobileNet组合/本域指标，未见新主线约束，可窄关闭；`2512.00061v1`完整摘要Capsule Summarization减少参数，题名不能直接排除，但尚未呈现改变当前foundation/system选择的关系，不能只按小模型关闭。其related DOI像2022出版线索；DOI工具访问失败，本复核不声称已证旧首公开。目录中明确FANET clustering/医疗分割/地震或材料应用不扩宽池；没把题名浏览宣称全量语义验收。

## 安全终态与校验

确定本窗家族1；其窄标准证据/Books判断通过，整日报未通过因普通9项未归并。其余7项、SIMPLE、Google/GR-RL个体日期和四个旧目录缺口可真实外部保留，不授Coverage/Evidence、无遗漏、生产可靠性或安全保证，不写Books正面机制。V3格式实际校验通过，写后diff与链接检查另执行；没有runtime测试、部署、stage/commit/push。

## Mill 九项补正后定点复核 2026-10-02T19:32:57+08:00

复核者Mill，agent ID `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e`，非作者Gibbs。旧未通过记录保留；本轮以实际写入的NINE_ITEM_REPAIR及README §1/§5为对象，不重扫全日或月池。

Google两项、Diagnostic prompting、MCU ODL仅定点复用本人的有效同身份原始读取。新增独立访问与范围：[FlexiWalker v1](https://arxiv.org/html/2512.00705v1) §3.2/3.3随机键跳跃与rejection上界、§4.1 cost model、§6.3动态选择失误；[Delta Sum v1 PDF](https://arxiv.org/pdf/2512.01549v1) §III Eq9–21，HTML Cache miss后PDF文本实际取得，公式截图接口失败，不声称视觉核验；[Active Storage v1](https://arxiv.org/html/2512.02646v1) §3.1/3.2及Figures3–5说明；[Data-centric VLM v1](https://arxiv.org/html/2512.00042v1) §2.6/2.7 Tables1/2；[PEFT-DML v1](https://arxiv.org/html/2512.00060v1) Framework/Experiments Table1。

校准结果：FlexiWalker只支持图分布执行取舍，动态selector并非总赢；Delta Sum平均base、加和delta、lambda阻尼与节点规模/有效步长耦合，不授普遍收敛；Active Storage shadow object远程方法不等零通信，只soft real-time；VLM Think下降保留局部反证，但同epoch不是等token/预算；PEFT 3D-LRF mAP74.8高于62.2，mAAE正文/表不一致，缺dropout具体协议，不授任意sensor子集保证。作者对这些事实含糊项已读必要核心并保留potential/反证，不再以组合应用或无日期直接删除贡献。

九项普通差额闭合。14源原边界、1个确定落窗家族标准证据及Ch66/67/84/81具体对读沿用此前本人有效结果。Reward Features旧机制去重不关闭潜在新理论修订；八项新potential、原七项、SIMPLE及具名日期/旧目录均依§5保留终态与定点重开，不获Coverage/Evidence、正面Books或无遗漏权限。真实确定分母1，不把外部项算零事件。

结论：通过

完成态机器校验待下一条记录实际结果；没有runtime实验或Books改动。

实际完成态验证：`python3 scripts/validate_research.py --report papers/2025/12/03/README.md` exit 0，检查1份V3；此为接口一致性结果，不替代上述逐项语义复核。
