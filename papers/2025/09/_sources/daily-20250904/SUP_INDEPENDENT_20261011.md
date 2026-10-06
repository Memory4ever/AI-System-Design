# Sep04 来源增量独立复核

## 1. 本日边界与实际范围

复核者：Cicero（非作者；作者 Meitner）。2026-10-11 启动重读 AGENTS、当前 RESEARCH_CONTRACT、REPORT_CONTRACTS、SOURCES 使用说明/每日/arXiv、Prompt、ROADMAP、State 路由，以及本日 README、SCREENING、NECESSARY_CORE 和 [启动基线](SUP_BASELINE_README_20261011.md)。不继承其他日研究队列。

只补 2025-09-03 完整 BJT 自然日，无 catchup、无时分秒准入要求。旧窗口、候选/日期/评分/有效审阅与连续原 §4 冻结；旧 54 题摘、46 潜力/8 关闭及 18 必要 core 是可复用的原裁决，不在本批重复审阅。本人只写本文件，不写 report、Books、LS、index、scripts 或另建 raw。

本批实际独读 [FIRST](SUP_FIRST_20261011.md) 中 20 条完整精确 v1 title/abstract，依据 [exact 原件](SUP_EXACT_0_20261011.raw) 和 [请求](SUP_EXACT_0_20261011.request.json)。请求 id_list 明确 v1，HTTP 200，25 条返回；本批只读表列 20 条，未把另 5 条算已读。未以 current/newer AB 替代 v1。另定点读 8 条必要 core：01716、01728、01813、01909、01920、01944、02072、02093，范围见 §3。

首批局部准入校准结论：**17 P、3 C，无未决准入 N**。P 仅为贡献潜力；本批未证明公开自然日、不是确定当窗候选、不评分、不授完整 Evidence 或 Books。作者其余筛选、来源、日级复核仍属普通工作，不因此写外部终态或全日通过。

## 2. FIRST 逐项裁决

下列 ID 均为 `2509.<ID>v1`。明确潜力在公开日门停止；表内实验/理论限制是权限限定，不是继续遍历全文的队列。

| ID | 独核 | 原约束 → 实际增量 → 最小改变；不授内容 |
| --- | --- | --- |
| 01684 | P | 变时长代码动作使异步更新偏向快但次优方案 → duration-aware 更新及插桩 partial credit → Agent 训练调度/奖励归因选择；不采 3B 胜更大模型为等预算普遍优势。 |
| 01728 | P，窄化安全 | 预训练动作缺显式约束 → STL 约束 logits/rollout 与软 robustness 权重 → 解码控制/任务成功取舍；只保留模型内轨迹条件，不授真实环境通用安全或全部 temporal logic 可行性。 |
| 01750 | P | 自适应 top-k 的不齐维度使 zero-padding 引入伪信息 → 自适应聚合及隐层投影蒸馏 → 通信与表示质量分账；不授隐私保证或端到端降本数字。 |
| 01840 | P | full CP 每标签重训贵，普通 ICL 训练不适配 CP → permutation-invariant ICL 与 CP-aware loss → 覆盖/集合宽度/计算路线；不因 Transformer 小任务排范围，也不授无 exchangeability 条件的 coverage。 |
| 01842 | P | 全局早停抹平组件差异 → 按梯度阈值逐投影矩阵冻结 → validation 成本与剩余更新选择；低梯度不直接等于已证明收敛，不授摘要加速数字。 |
| 01920 | P，窄化 lossless | 固定 speculation 步长浪费调用且欠美元成本控制 → 异步在线步长预测及 bias/offset → latency/cost 可调选择；lossless 依 target 验证/替换路径，不等于随机策略分布和现实副作用已证。 |
| 01959 | P | 自然图 CLIP 难区分图表结构 → 结构 hard samples 与两项 contrastive loss → 跨模态训练目标；不以 flowchart 领域关闭，不授等预算归因。 |
| 02017 | P | collaborative embedding collapse 与 semantic ID 遗忘 → MM-RQ-VAE 的 MMD/contrastive 和 code 初始化 → 表示及 LoRA 适配路线；不是仅推荐名次，不授各模块独立收益。 |
| 02046 | P | optimizer 对比混调参预算/中途 checkpoint → 跨规模、数据比例和训练终点的排名翻转反证 → optimizer 评价条件；局部负面不能排，不授任意规模 1.1x/矩阵预条件普适优越。 |
| 02055 | P | 跨 embodiment action 分布错配 → reverse-KL 统一 latent 再 guidance → VLA 适配接口；不授安全、全任务增益或两阶段等预算因果。 |
| 02075 | P | 平均 length adherence 掩盖语种与组件差异 → 英/意 IT 深层 attention/MLP attribution 分叉 → 语言条件下控制解释；attribution 不等于 causal intervention。 |
| 02097 | P | 固定题集不定位能力边界 → interviewer 的扩测、难度调整与反馈验证 → 动态评价路线；保留 v1 JudgeAgent 身份，不借后来题名/版本，也不授无循环自证的评价有效性。 |
| 01716 | **C? 改 P** | 抽取后形式化易被误当可靠权限 → 总体 F1 与 non-empty F1 的明显分裂、逐任务模型/浅 FT 不一致 → privacy-policy-to-formal-policy 的抽取评价/人工核验边界；pipeline 组合本身不作增量，不授 ODRL 执行正确性。 |
| 02036 | C | 完整 AB 为 34 dental longitudinal cases/258 QA 的四已有 LLM 排名与专家评分；没有指出新的评价盲区、控制机制或成立条件。关闭依据是实际贡献仅领域模型评测，不是 medical 标签；摘要临床整合建议不采用，current 版本/说明轻核无新撤回/纠错信号。 |
| 01909 | N 改 P | 拒绝率不能代表安全且有帮助 → 分离 safety/satisfaction 的策略节点、非对称冻结更新和 constructive 评价 → 安全对齐目标与训练反馈选择；不授真实用户危害减少、全程安全不变式或真正梯度可微性。 |
| 02093 | N 改 P | 单纯取最高 exemplar 不等于最佳 refinement → tiered/multi-metric 对照及 top-k 增大后回落 → 检索示例选择/contrast-refine 的局部条件；同 pool/judge 不等于同生成 token 预算，top-3 对照也混 exemplar 数，不授纯 reasoning 归因。 |
| 02072 | N 改 C | core 为既有 ABEX→固定 Qwen embedding→MLP、Bernoulli 选择既有 FGM/focal loss；消融仅 OSHA 组合相对去掉一个模块的分类改善，无连续 FGM/等成本对照来建立新资源或有效性边界。未训练/验证 foundation 机制，occupational safety 是应用目标而非模型安全反证；保留局部消融事实，不采优于大模型即新系统机制。 |
| 01944 | N 改 P | CoT/GRPO 名称组合不足 → 四步动作推理数据、physics reward 分项消融及 generation 数边际收益 → VLA 后训练目标/预算选择；不授 self-reflection 必要性、平滑性即安全或闭环驾驶能力。 |
| 01895 | P? 确认 P | 单视角证据不足不必靠多加 LLM → multi-view 显著改善而 VLM+LLM 未显著优于 VLM → 视觉证据采集与额外语言推理模块的局部选择；不是 wildfire 名称关闭，不授各视角数量/数据匹配已核或“无显著”即等效。 |
| 01813 | C? 确认 C | core 的信息不对称由环境按角色提供状态、Analyze→Decide 和固定季度时序实现；对照为 single-prompt whole trajectory，增量是 FDA shortage 领域仿真拟合，没有新 Agent 执行/权限可靠性条件或预算控制反证。不是医学标签关闭，不把零样本域预测的改进换名为通用协作机制。 |

## 3. 必要 core 的实际位置与局部反证

以下只读决定准入和直接限制的部分；未读其余正文、全部 appendix、代码或复现。浏览请求均指向 exact-v1 HTML，实际返回可读正文，无 timeout/错误页；六项作者已保存同 URL 的 raw/request，逐项身份与最终 URL 已核，没有借下载授亲读。

| ID | 精确必要原件/位置 | 实际裁决依据与停止点 |
| --- | --- | --- |
| 01716 | [v1 官方 HTML](https://arxiv.org/html/2509.01716v1)，§3.1–3.2、§5.1–5.3 | 逐行片段实体/关系抽取、JSON 修补、保留原段 provenance，ODRL 用 data class 作 identifier 仅 demonstration。总体约 .9 F1 与 non-empty .5–.7 分裂；大模型/FT 非全任务更好，足以恢复局部评价反侧。未核图中全部数值或后续政策执行，不授 formal policy 可信正确。 |
| 01728 | [v1 raw](SUP_CORE_2509.01728v1_20261011.raw)/[request](SUP_CORE_2509.01728v1_20261011.request.json)，§3.1–3.3、Theorem 1、Appendix B/C | HCD 按 dynamics f 预测下一状态屏蔽 logits；proof 明确 f exact/deterministic。RCD 权重增加有任务成功代价。采样必须存在未屏蔽动作是本复核指出的必要前提；全 mask、model mismatch、temporal-prefix 可延展性未由该 proof sketch 完整解决。P 保留，不能照录“模型无关 runtime 安全保证”。 |
| 01813 | [v1 官方 HTML](https://arxiv.org/html/2509.01813v1)，Methodology 的 architecture/two-stage/Information Flow、Experiments 的 baseline/Table 3、Appendix Zero-shot Baseline | 各角色信息视图和季度时序都是模拟供需规则，baseline 直接单 prompt 预测全部轨迹；没有同预算多 agent、同信息流程等关键执行对照。Table 3 的局部事件拟合不构成新的通用 Agent 条件，C 停止；未读经济附录及全部 prompts。 |
| 01909 | [v1 raw](SUP_CORE_2509.01909v1_20261011.raw)/[request](SUP_CORE_2509.01909v1_20261011.request.json)，§3.2–3.3、§4.2/4.4、§6 constructive β 分析 | 用户 retention∝satisfaction 是假设，cost 在该分析中当常数；策略 safety/satisfaction 冻结权限非对称、pseudo-gradients 由 evaluator 提供。β 图为评价权重敏感性，不是逐 β 训练的因果消融。机制足以 P，不把策略节点冻结等同全模型安全不变式；未读所有数据/理论/appendix。 |
| 01920 | [v1 raw](SUP_CORE_2509.01920v1_20261011.raw)/[request](SUP_CORE_2509.01920v1_20261011.request.json)，§3、§4.1–4.3 | draft/target 对齐才 commit，分歧采用 target 并取消后续线程；新增是在线 k 预测、异步 training/inference predictor 和 bias/offset。lossless 是该验证路径的目标策略保留，不授外部动作可回滚、随机过程分布等价。§4.1 文字把 differs 记 reward=1 与否则立即终止，和 surrounding mismatch 描述有冲突，保留不替作者修正；不需为此读所有 benchmark。 |
| 01944 | [v1 raw](SUP_CORE_2509.01944v1_20261011.raw)/[request](SUP_CORE_2509.01944v1_20261011.request.json)，§3.2–3.3、§4.3/Table 3–4 | 四步 CoT、格式/physics reward；去 pos/ste/vel/tem 的 L2 与 candidate 数 2→6→8 有具体局部选择。SFT .27、w/o Four .25、w/o Self .23，作者用 full .19 作退化基准，不能直接推出 SFT 内反思必要或纯 causal 收益。保留 VLA 后训练潜力，未核完整任务/碰撞/现实部署安全。 |
| 02072 | [v1 raw](SUP_CORE_2509.02072v1_20261011.raw)/[request](SUP_CORE_2509.02072v1_20261011.request.json)，§2.1–2.3、§3.1、§4.1 | 固定 embedding 的 MLP 使用 p=.5 Bernoulli FGM、focal loss；4770 报告七类、8:1:1，ABEX/RAT 组合与单模块消融。无连续 FGM/成本-质量曲线支持其省算“新边界”，无 foundation 安全/训练机制。完整 AB+必要 core 后 C，非因单 seed 或小模型排除。 |
| 02093 | [v1 raw](SUP_CORE_2509.02093v1_20261011.raw)/[request](SUP_CORE_2509.02093v1_20261011.request.json)，§III-B/C、§IV-A/C、§V | BM25 k=10，同 pool、ArmoRM judge、temperature=0；tiered/high-medium-low 与 multi-metric 选择，top-3-only 与 k=5/10/15/20 消融。k 更大后下降是具体局部边界；数目、token、评价器与池的混杂未证全控制。足以 P，未授最优通用 k=10、解释可信或独立人类效用。 |

01716、01813 本人仅在本 note 留原页/实际位置/判断，未越 ownership 新建 raw；作者如需原档可按两条精确 v1 URL 保存，同一材料不重复提出泛化请求。

## 4. Current 轻核与请求实况

2026-10-11 **19:11:19–19:11:45 BJT** 对本批全部 20 个官方 `https://arxiv.org/abs/2509.<ID>` 实际 GET，timeout=15s；全部 HTTP 200、最终 URL 未改，检查 comments、submission-history 和 full-text 服务状态，不读取 current AB 替代 v1。版本栏未见 withdrawn、comments 未见明确 correction/erratum 信号；这是当前显式说明的轻核，不是全文修订无变动保证。02036 仍有 PDF，其摘要临床部署倡议不获采用。

实际 current 版本分别为：01684 v1；01728 v4；01750 v2；01840 v3；01842 v3；01920 v3；01959 v1；02017 v1；02046 v2；02055 v2；02075 v1；02097 v4；01716 v1；02036 v1；01909 v7；02093 v2；02072 v4；01944 v3；01895 v2；01813 v3。版本数不触发整篇对比或重要修订推定。01750 Globecom2025、02017 CIKM2025、01813 AAAI2026 当前会议标签不是公开日证据，不扩全会议。

本批 exact-v1 AB raw 的 sha256 为 `7f3600cab869a5ef16e7d2a15145c015976d90969ce350f107bed43d47679c9c`，请求实录 2026-10-11T11:04:47.494960Z，HTTP200；只是定位已实际读的 20 条，不以摘要 API 的 submitted 日期证明 Sep03 公告。作者报告 CL/LG Sep03 路径 400 属来源待核，本 FIRST 尚未独核该页或授 Source pass。

## 5. 共因检查与本批交付权限

局部纠正：01716 不可因“成熟抽取/形式化 pipeline 无新权限执行”漏掉实际评价反侧；01895 不可因领域/局部 negative 漏掉多视角证据与额外 LLM 模块选择。后续若同一关闭理由实际用于其他材料，只重开有该具体信号的受影响集合；不把全部宽标题库存变全文队列。

组合不自动 P 也不自动 C：01909/02093/01944 必要 core 建立策略更新、示例选择/数量条件或 VLA reward/预算比较；02072/01813 必要 core 则仍停于既有方法领域任务组合，没有相应主线新条件。医学、安全、small model、单 benchmark 或局部实验都不是独立排除规则。

本批 20 条准入普通待办已处理，17 P 的公开自然日尚未建立，精确隔离不评分；本次没有确定新增候选、候选 Evidence 完成或 Books 判断/写入。12 明确 P 不扩正文，8 必要 core 只为含糊准入/直接安全保证限域；不读所有 P 全文来弥补日期门。尚未对全部拟项、代表 EX 分层/所有安全反证 EX、14 source、最终六节 DAY 给予整体通过；后续有效单篇可直接推进，剩余普通工作不可写外部停止。

## 6. 两条确定 Sep03 来源项的单篇校准

作者随后交付的 source 事项独立处理，不改 §2 首批 20 AB 分母。本节通过局部准入/发布事实及 Books 处置，不等于最终 DAY。尚未读作者其余 73 AB 裁决和全部来源，不能继承其“已下载/已读”作为本人完成。

### RoboBallet：C，非因机器人或小模型标签

实际独读 [官方完整 title/AB](SUP_ROBOBALLET_20261011.txt)，核 [raw](SUP_ROBOBALLET_20261011.raw)/[request](SUP_ROBOBALLET_20261011.request.json)，并打开 [DeepMind 原页](https://deepmind.google/research/publications/111579/)。官方明确日期 2025-09-03；保存请求 2026-10-11T11:10:48.964554Z，HTTP200。该日期支持机构发表条目，不擅称论文首公开必在该日；贡献已关闭，不另扩先稿日期请求。

AB 实际增量是 graph scene/policy 在程序生成环境里 RL 学习，联合完成八机器人/40 reaching tasks 的 allocation、scheduling、motion planning，测试未见场景的布局/障碍/目标泛化。这里没有 foundation/VLA 跨模态表示、action-conditioned world-model 接口、新通用学习条件或模型训练/推理基础设施机制；generalizes zero-shot 本身不是 foundation 身份或通用理论。所述 fault-tolerant/online perception replanning 只是开放能力方向，不是本文已经给出的新可靠性条件。按实际专用规划贡献关闭，不把所有 GNN/RL/机器人整体排范围，亦不将 collision-free 宣传当物理安全证明。未读 Science 全文或实现，AB 已足以作该范围判断。

### OpenAI Sep03 IP allowlisting：准入通过，单篇处置可推进

实际打开 [官方 Enterprise/Edu release notes](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes)，读完整 **September 3, 2025** 节（SharePoint sync/IP allowlisting 两小节）及紧邻 Sep04/Aug28 日期；不是搜索摘录。作者保存的 [HTTP raw](SUP_OPENAI_RELEASES_20261011.raw)/[request](SUP_OPENAI_RELEASES_20261011.request.json) 是 403 页面，**不能用作已读 release 正文**；本次 web 返回可读官方 HTML 并定位 Sep03 原节，未以 403 伪装正文受阻。日期采用该正式 release 的公开日 2025-09-03，不补时刻。

SharePoint 的 admin enable→user OAuth→RBAC→sync/reference 是成熟连接器的新产品支持，单凭这组功能不建立新机制，C/背景记录。**IP 项不是因网络 ACL 术语入选**：本次公开变化把独立来源 IP 条件明确加到 ChatGPT 客户请求及 Compliance API；有效凭证不覆盖 unlisted-IP 拒绝，范围包括 authenticated file downloads/Compliance keys，Compliance 流量 always enforced/cannot turn off，且明确不适用于 API Platform。它改变部署/审计集成的适用条件，而不是发现 authentication≠network permission 的成熟原则。

建议评分对象仅为这项发布约束：**Design Delta 2 + System Reach 2 + Durability 1 = 5**（具体执行/适用边界，横跨 workspace/file/Compliance，长期价值受产品版本限制）。不把 OAuth/RBAC/IPACL 原理算新贡献，不借潜在全平台影响授 7+。当前记录尚不替作者正式候选表；此项可按单一家族事件写入，不把 SharePoint 两功能另加一个高分家族。

发布事实的必要受影响深入已读到：Sep03 原节全部约束及 [当前官方 IP article](https://help.openai.com/en/articles/12111596-ip-allowlisting-for-chatgpt) Overview/FAQ。当前支持文档确认 file/Compliance traffic，并限定不作用于 OpenAI internal systems；其 separate lists、5–15min propagation、配置/恢复细节仅属当前说明，**不倒授 Sep03 新发布时的全部行为**。本次未核真实 request enforcement、测试租户、源码、全 attack surface 或远端配置，不认证无旁路/生产安全；收益是公开的产品可用约束，时延/成本 benchmark 不适用，规则传播与接入中断代价仅按文档边界说明，不虚构性能。

Books 实际窄比较：owner `PLATFORM-SECURITY`，已读 [Ch72 开篇资产/主体](../../../../../books/part-06-ai-infrastructure/72-security.md#从资产与信任边界开始)、生命周期 trust chain（当前 lines101–123）及设计收束（2936–2940）。现文明确 security 不止 API authentication，资产包括 APIs/audit evidence，跨层传递需 identity/integrity/authorization，安全能力不能继承为可信动作。本发布**不构成这些通用论点的新理论/反证**；其 ChatGPT-specific endpoint/exclusion/cannot-disable 是部署版本事实，因此具体裁决为 **仅报告**，不是“现书已经覆盖本产品 IP contract”，也不为了入选制造 Books diff。无共享 Books 写入或锁请求；如作者拟主张长期机制差额，须向 root 指出新增论点再协调，不把本局部通过当写书许可。

此 source 单篇的日期、准入、必要发布证据与“仅报告”理由已具备；作者可立即落实，不等 arXiv 全批或其他原件。最终 report 候选数/评分须以作者实际表和六节 DAY 再核，本节不授全日完成。04499 overlap/其他未决 core 仍由精确材料推进，不能用一般重叠提示直接去重关闭。

## 7. 后批 A：14 题摘与 9 必要 core

实际 XML 分母核清：EXACT_0/25/50/75/SCOPE 返回分别为 25/25/25/13/5，共 **93** 个 exact-v1 身份。首批 20 后尚余 **73 = 首包未表5 + 25 + 25 + 13 + SCOPE5**；不能把后四包本身称 73 再额外加5。宽查询98和五条仅题名科学应用不是93 AB的同一证据层。本人本节新增实际完整 AB 14（未继承作者下载或阅读），其中首包未表五条全部补读；累积独读 **34 AB = 27 P / 7 C**，其他59条仍普通工作，不授全量或终态。

原件：[首包](SUP_EXACT_0_20261011.raw)、[25](SUP_EXACT_25_20261011.raw)、[50](SUP_EXACT_50_20261011.raw)、[75](SUP_EXACT_75_20261011.raw)。各包 exact-v1 id/完整 summary 实际解析，current 仅轻核，不换 AB。

| ID v1 | 独核 | 原约束 → 实际增量 → 处置边界 |
| --- | --- | --- |
| 01685 | P | noise-free particle sampling 的各向异性/regularization bias 未明 → preconditioned proximal score/kernel 及 quadratic discrete-time bias 条件 → sampling/attention 解释与学习更新的理论路线；只保留明确新算子/局部界，不因 self-attention 类比授 Transformer 收敛或所有 BNN 优势。 |
| 01772 | P | subword/token boundary 对形态丰富语种不稳 → isolated-word character pretraining encoder → morphology/语义表示与 tokenization 替代；不是方言名直接关闭，不授上下文语言建模或所有语种通用性。 |
| 01907 | C | RSCC 的62,315灾前后对照图像/caption是领域数据资源扩展；完整 AB 未指出新表示/训练机制、受控评价盲区或模型失效条件。不是 remote-sensing 标签关闭，不采“robust”泛称，也未读正文。 |
| 02033 | P | token matching 缺层级结构 → dependency/topic 双图 GIN 与 node/graph contrastive objectives → 结构语义表示目标；不采法律/抄袭成绩为因果证明，不把能映射检索 owner 单独作理由。 |
| 02040 | P | 无约束 synthetic text 难控属性多样性 → semantic attributes 作 genes、LLM crossover/mutation 与 active parent selection → 合成训练数据条件化/搜索路线；未核全部质量/等预算，不能借 genetic 名称证明新样本真实。 |
| 02655 | P，安全反侧 | 初期 bounded 单目标成功不保 sustained 多目标 → 两旧 LLM 各10 trials×100 steps 的 homeostasis 对比与后程单目标最大化失败 → Agent 长程约束评价；v1 Notable 题名与 current Systematic 不混，不授 RL/activation drift 内因、随机故障概率或真实 biology 系统结论。 |
| 02550 | P，局部 negative | augmentation 不必同任务受益 → 同 AYA 路线 Islamic 有益而 culture development 未改善的具体报告 → 文化子任务/数据增强验证分账；只是有待核原队对照的局部反侧，不授跨团队 LoRA/小模型因果优越。 |
| 02350 | C | 完整 AB+§6 实际是 execution-paradigm taxonomy 与引用既有研究的 latency/opacity/评测问题归纳；没有本稿新受控反例、重新计算的比较或明确新成立条件。不是 survey 一刀切；关键风险文献可作恢复线索，不给本综述继承原论文证据权。 |
| 02547 | C | AB+§6 的 MDP/POMDP、工具/记忆/环境分类及安全/扩规模主张来自已有论文归纳；没有本稿新增可检验边界或矛盾解决。security/hallucination/sycophancy 原段已读，不因其含风险词自动 P 或因综述自动 C。 |
| 02363 | P，恢复反侧 | declarative annotation 组合本身不足 → 同两8B模型、schema/shot/CoT 对照出现非单调效果，label/spans agreement 分叉 → 数据标注配置与验收单位；双 LLM agreement 不等 human accuracy，更大模型会显著提升只是未测推断。 |
| 02123 | P | crop+OCR 不总比全页视觉好 → oracle 全页/子图+text/全页+text 同 backbone 对照的反侧，加 CoLI modality-max late interaction → 证据分割/保留 global context 选择；oracle generation 不是已测检索召回或 end-to-end RAG，不授小分差显著性。 |
| 02659 | C | necessary core 仅既有 ViT/MLP/tokenizer→InternLM4B→trajectory MLP+text、LoRA/L2/next-token 组合及 camera-only leaderboard；没有新控制机制或新增模块的成立条件，少量 stop/go 场景展示不建立泛化边界。缺消融不是独立排除规则，此处关闭依据为实际贡献仍组合与域名次；不采安全 prompt/“human-like”作安全。CVPR2024 标签不证明新增事件，但 C 不另追无关日期。 |
| 02551 | P，限理论 | distributed multi-modal local updates 集成条件未明 → gated/adaptive aggregation 的 bounded-gradient/variance/smoothness 学习率条件及 unified/function-specific 局部取舍 → 分布式学习更新解释；不把 NDT 命名映射为 World Model，不授 twin prediction consistency、真实网络安全/隐私或无条件融合收敛。 |
| 02444 | P，非仅综述 | pixel click drift 及重复错误 correction → bbox 最近中心修正、perceptual-hash 下 failed-correction history 的 bypass → GUI 执行/恢复选择；有具体机制，不按“综述”关闭，也不授 nearest widget 即意图正确或完整系统可靠。 |

### 指定 9 core 实际读取

均限 exact-v1，HTML 八条实际200且原 request/final_url一致；02444 HTML404记录保留，PDF200可得，普通工作不能写不可访问。只需准入充分，不为公开日未证再扩正文。

- **02655**：[raw](SUP_CORE_2509.02655v1_20261011.raw) §1.4、2.1.2–2.1.3、§3。Haiku3.5/4o-mini、10 trials×100 steps；single/multi homeostasis 行为对比保留，self-imitation、linear aggregation、stress/activation drift 全是解释假设而非机制干预实证。未读全部 prompts/失败 snippets/图表，不采用总体安全概率。
- **02550**：[raw](SUP_CORE_2509.02550v1_20261011.raw) §3.2、§5.2、Limitations。label-likelihood MCQ 协议、AYA augmentation 的任务方向差异、国家不平衡/MSA 限制实际读；不用团队排名证明等规模/等训练控制。最小 P 为 task-conditioned augmentation 反侧，未读所有团队稿或全数据。
- **02350**：[raw](SUP_CORE_2509.02350v1_20261011.raw) §6 六组 challenge 实际完整读；latency/accuracy、显式监督依赖、70余数据集碎片化均文献归纳/研究方向，不授新失败率或因果解释。未读各被引原论文/全部分类附件。
- **02547**：[raw](SUP_CORE_2509.02547v1_20261011.raw) §6.1–6.3 实际读：RL reward-hacking、hallucination tax、sycophancy、scale/model/data/environment 皆引用他稿或未来建议，未产生新共控实证或被验证的安全协议。C 的 safety/counterevidence 信号已具体覆盖；不说全部500余文献已复核。
- **02363**：[raw](SUP_CORE_2509.02363v1_20261011.raw) §4.4–4.5、§6.1/Table3–4、§8。DSPy/MIPRO 是借用；同 Llama8B/Ministral8B shot/CoT 与 schema 的交互有局部反侧：ACOS 15-shot 的 Llama 无CoT59.92/有CoT56.69，增加 shot 对 UOC 不单调。实际 temporal labels 无human truth，table4只跨模型agreement，不能授自动标注可靠。HTML部分 nesting 不良，提取初次含邻接冗余；已用标题/段落边界窄核，不声称顺读全稿/引用文献。
- **02123**：[raw](SUP_CORE_2509.02123v1_20261011.raw) §3.3、§4.1–4.2/Table2。CoLI 是 modality 上取 max 的 late-interaction；Qwen2.5-VL7B parsing/generation、Qwen7B judge、temp0。MMLongBench 全页40.39/子图+text29.11/全页+text46.86，SlideVQA81.58/58.76/81.68；只采用 global-context/cropping 的局部选择潜力，不让 oracle 冒充 retrieval 实验。
- **02659**：[raw](SUP_CORE_2509.02659v1_20261011.raw) §1 Method、§2 Result/Limitations 全部必要段。trajectory 从 last token MLP 解码、text 在trajectory后，地面真值训练不证内部解释因果；作者明确未完整消融、open-loop 不揭示 closed-loop。C 不因它是早年会议或小模型，而依据实际组合/榜单增量未立新条件，日期未核不另请求。
- **02551**：[raw](SUP_CORE_2509.02551v1_20261011.raw) III-B2、III-C2、IV、V-A4。local vectors融合→local model training→parameter average，raw留local不证明privacy；IV是smoothness、coordinate bounded gradients、local/global variance及步长条件下的 expected gradient-norm bound，不是所有 twin 状态一致性。function-specific/unified 两路线存在任务误差/复用取舍；公式/必要推导已浏览但未认证全部 proof 或真实多模态系统性能。
- **02444**：[PDF](SUP_PDF_2509.02444v1_20261011.raw)/[request](SUP_PDF_2509.02444v1_20261011.request.json)/[分页派生](SUP_PDF_2509.02444v1_20261011.txt)，物理页1–6定位，58–61的§4.2.1–4.2.2及118–119的§7.2.4/Table7.5。确为138页，未全文遍历。OmniParser是借用，新增 click outside bbox→nearest center、同画面hash失败记录后保留原click是可核的 correction/bypass 机制；“无UI变化=失败、最近widget=用户意图”是前提，不授系统安全。后页Table7.5是scenario↔metric关联表，不是受控消融或可靠率证明；无需继续全案例才能 P。

本节14个 [current](https://arxiv.org/abs/2509.02655) 原页 raw/request均逐项独看 title/comments/history（未使用 current AB）。HTTP均200，未见withdrawn或明确correction说明；02655、02123题名变化和会议标签保留为身份风险，不用新标题倒改v1/首公开。当前版本为01685v2、01772v1、01907v5、02033v1、02040v1、02655v3、02550v1、02350v1、02547v5、02363v1、02123v3、02659v1、02551v1、02444v2。版本变化不自动证明重要修订，不遍历修订全史。

新增9 core至准入充分即停，累计17必要 core不等34 FullEvidence；arXiv公开日仍未核，27P不评分。其它后批题摘/含糊事实及14来源继续普通工作，尚未授Source/Evidence/Books整体或DAY。

## 8. 后批 B：22 完整 v1 题摘与安全反侧

压缩恢复已重读 AGENTS、当前两合同、Sources说明/每日/arXiv、Prompt、ROADMAP、State本任务路由及本日README/独核停点。原档仍进行中；新增IP单篇已实际落入§3/4，沿§6有效独核可复用，原§5/6旧通过不作为增量DAY。只写本note，未继承别日队列。

本节实际独读[EXACT_25](SUP_EXACT_25_20261011.raw)余22个完整v1 title/summary，20P/2C；累积 **56 AB = 47P/9C**。这里P仍是准入潜力，不是已证Sep03公开或正式候选。另37AB属于后续普通工作。

| ID v1 | 判定 | 具体增量或关闭理由 |
| --- | --- | --- |
| 02372 | P，安全反侧 | benign developer prompt仍可能生成恶意URL；定向构造审计与跨四模型验证改变“正常任务生成即可信”的假设。4.2%分母是scam数据库衍生提示，不是自然请求总体；未证明训练数据投毒因果。 |
| 02227 | C | accelerator文档抽取/总结与专家退休知识保留，是领域使用既有LLM的初步结果；AB没有新训练/检索机制或具体受控失效条件。未凭particle标题关闭。 |
| 02198 | P | CoT/NLI unanimous voting与domain expert一致性的比较提供事实评价器组合选择；只保留相关性/局部校准潜力，不授医学事实正确或自动安全。 |
| 02259 | P | 五预训练speech模型跨八非speech婴儿哭声数据比较，latent source instability/identity编码对迁移表示适用域提供证据；不是临床结论，也不授architecture因果。 |
| 02144 | C | psychotherapy的genuineness/credibility gap来自人类治疗师身份概念分析，属干预理论假说；没有模型/Agent机制或测试出的系统条件。不因medical标签关闭，也不把理论建议当已证负面结果。 |
| 02360 | P | 后验轨迹诊断→执行中PRM taxonomy feedback；guided/unguided/action-prescriptive比较及长度/成功取舍具体。未授0.2美元跨模型成本保证或总体可靠性。 |
| 02278 | P | lyrics/acoustics→带时间/局部区域的motion subtitles→diffusion motion-intensity条件化，是跨模态中间表示及可控生成设计；不只动画应用成绩。 |
| 02121 | P | 单call优化缺跨workflow共享→DAG batch plan、prefill/decode/cache/GPU cost model、KV迁移/overlap；改变Agent批运行计划。18.6x未独证配置/等质量，不外推online SLO。 |
| 02273 | P | multi-scale spatial features与dual-prompt scene/fine-semantic cross-verification、confidence pseudo-label loop，建立VLM/OOD表示选择；不借灾难/remote-sensing题名排除，也不授robust检测保证。 |
| 02100 | P | verbal与visual emotion不一致是具体multimodal评价维度，非单加治疗数据；允许核验alignment盲区，不采用“genuine empathy”或治疗效用保证。 |
| 02225 | P | 135M–32B按语言能力/外部知识/内部知识拆测，挑战scale收益等同语言能力的判断；memorization成长更快不等已经隔离尺寸/数据因果。 |
| 02241 | P | Distribution-based Localisation/Inverse Cardinality Weighting给长文candidate selection具体替代，且指出QA自动指标限制；不是legal rank唯一贡献，不授prompt保证accountability。 |
| 02330 | P | algorithm-type搜索收窄与code/text dual encoder改变fine-grained retrieval；真实bug benchmark辅助，不单按数据规模/排行榜准入。 |
| 02324 | P | language-conditioned SigLIP2 bidirectional cross-attention/DoRA grounding连接高层规划与deformable执行，属于跨模态/VLA接口选择；real demo不授闭环安全。 |
| 02129 | P | similarity直接评分、可控JSON长度与uncertainty-aware self-consistency作test-time预算/迁移替代；210x未核同条件，不按VPR域关闭。 |
| 02133 | P，安全约束 | counterfactual divergence rerank候选token是具体输出分布修改，不是lossless经典speculation；fairness/fluent/cost与verifier bias laundering反侧必须保留。 |
| 02377 | P | 一次decoding使用未选candidate token扩展检索，改变生成成本与query diversity取舍；未核logit接口成本或质量等预算，不授zero overhead。 |
| 02333 | P | token prior相关dynamic clip+cumulative reward smooth standardization处理zero-gradient/data utilization，属于RLVR目标/更新机制；不照录SOTA或2x效率。 |
| 02379 | P | plain ViT multi-scale token aggregation及multi-stage domain-adaptive pretraining对视觉foundation迁移提供设计路线；不能因CT/MRI标题按AIfS关，也不授临床generalization。 |
| 02163 | P，安全反侧 | state-aware action validation与timeout/attack-rate比较提供执行约束和防御退化的局部条件；deterministic规则不等真实机器人安全证明。 |
| 02292 | P，评价反侧 | shared-mental-state annotation的surface coherence不保spatial/prosodic grounding；六dialogue discrepancy profiles及评估器验证限域，不能用总体model rank倒推ToM内因。 |
| 02208 | P | patient simulation的fact/persona/termination分离、dynamic rubrics与fragment-level RL，改变多轮RL环境/反馈构造；医学只是载体，非静态问答榜单唯一增量。 |

### 五份必要局部原文实读

- **02372**：[exact-v1 core](SUP_CORE_2509.02372v1_20261011.raw) §3/4/5/5.1/5.3/5.4/6。scam URL静态文本生成提示、三个URL oracle任一flag、过滤seed同domain后191跨四模型提示/177人工判innocuous均实际读。§4写三作者majority、§5.4写两作者+第三裁定，按具体流程保留；“benign”不意味真实自然采样。训练corpus不可见，来源定向/检测oracle不一致未排除，故保留安全反证而不采用“投毒已因果证明”。未访问任何scam网址、执行生成代码或做全攻击复现。
- **02133**：[exact-v1 core](SUP_CORE_2509.02133v1_20261011.raw) §3/3.1/3.3/Table6、Appendix M。top-k→original/counterfactual divergence选择，AB无parameter update与正文verifier SFT应区分base/draft及verifier，不能说全系统无需训练。log-likelihood减αJSD目标与随后argmin divergence规则并非同一公式；violent→peaceful反义变换不自动保语义。fluency degradation、额外forward/API成本和residual verifier bias明确保留；IIR代理不授总体社会公平、法律合规或经典speculation分布无损。首次提取含其它段截断，仅上述完整到达部分计已读，不授§4/所有appendix完整审阅。
- **02163**：[exact-v1 core](SUP_CORE_2509.02163v1_20261011.raw) §4.1.3/4.1.4/4.3/6.3.2–3/8.4。Move的LiDAR-distance rule、Turn/Stop假定safe、retry历史state、τ60–150s与attack-rate .3–1比较实际读；更长timeout主要延长失败尾部，高attack仍降低性能。单静态地图实机/GPT4o/pilot调参、未纳入silent failure/false positives、多模态/firmware攻击不在范围。P限这些新局部条件，不授bounded physical safety或无prompt bypass。
- **02292**：[exact-v1 core](SUP_CORE_2509.02292v1_20261011.raw) §4.1/4.2/5.1–3/7与Appendix C/Table4。四类discrepancy、utterance归一后min-max分数，Table3权重均1；不同annotator使用自身LLM作judge、人类使用Claude，故不能跨judge直接授排名。D1人工验证accuracy分别.725/.791/.524/.876，余五dialogue未人工复核；局部annotation/grounding反侧仍有准入潜力，非总体ToM能力证明。
- **02208**：[exact-v1 core](SUP_CORE_2509.02208v1_20261011.raw) §2.1.2–3/2.2.2/2.2.4/3.3.3/7。persona提升伴fact/privacy降低、three-unit simulator；100case rubric由GPT4.1按维度一致judge，92.7%不是独立专家正确率。实际multi-turn仍fragment sampling/filter，full-session RL是future，不得授全程规划/临床可靠性；动态反馈机制P，临床部署结论不采用。

22个current raw/request逐项独读comments/history，均实际200；未见明确withdraw/correction。02259 WOCCI2025、02330/02377 CIKM2025及02292后来SIGDIAL2026标签不是first-public日期证明；02144“Submitted on 19 March”也只提交线索，C已充分不另追。明确安全/反侧未因domain/局部/小模型/成熟pipeline共因漏关；本节不授全部候选Evidence。累计22必要core（17+5），不为47日期潜力继续全正文。

## 9. 后批 C/D 收敛：39 完整 AB 与局部改判

实际独读EXACT_50余21、EXACT_75余11、SCOPE5全部完整v1题摘，另从五条题名关闭集合定点恢复 **01679/02481**：其架构/分布式术语需看AB，现[01679](SUP_CURRENT_2509.01679_20261011.raw)/[02481](SUP_CURRENT_2509.02481_20261011.raw) history均仅v1，可exact-matching复用该官方完整AB，不是以新版摘要替v1。两条仍具体C，98身份不增加。最终本人 **95完整v1AB = 72P/23C，另3仅题名C**；先前93API题摘+5题名是中间证据层，非本次最终数量。

| ID v1 | 独核 | 实际增量或具体关闭理由 |
| --- | --- | --- |
| 02558 | P，复现纠错 | BRIGHT query-side BM25与bag-of-words query向量不同造成复现差异，长query计分合同必须区分；不只发布工具包。 |
| 02464 | P，评价反侧 | provider spec/output/own judge三方一致性是具体审计盲区；分层合成提示与judge差异限制violation比例，不授真实请求安全率。 |
| 02534 | P | learned semantic partition diversity signal与quality联合online RL改变探索/质量优化目标，不仅“更有创意”指标。 |
| 02515 | C | LLM Agent/classic MAS概念比较和future challenges归纳，完整AB没有新增执行机制、测试反证或明确新条件；不是所有survey统一排。 |
| 02449 | **C?→P，评价反侧** | 既有工具请求的成功不保动态合成工具成功；77触发/63成功/14失败的子分母揭示93%与100% headline权限差异。成熟流程不作新机制，实际失败分账值得保留，不采sandbox安全保证。 |
| 02408 | P，事件门隔离 | layered paging与LLRU tie-break明确改变expert缓存替代；extended标题不授新事件。实际unit-miss模拟/多expert重排不等offload端到端成本，不读全旧稿弥补日期未证。 |
| 02488 | P | anisotropic/class/domain spatial Fourier features修正PE距离/形状适用条件，医学是验证载体；不采诊疗结论。 |
| 02425 | P | value decay/belief-space recovery处理missed detection，改变VLM搜索状态更新；辅助机器人用途不自动排域，也不授真实导航安全。 |
| 02499 | P，限检测条件 | nearest prototype参考集与conditional threshold替固定cutoff，建立style-conditioned误差取舍；不授置信值校准、原创归属判定或所有未知LLM。 |
| 02458 | P | non-episodic multi-reward、RTG quantile及circular-buffer sequence接口是DT学习/运行设计，不因notification域关闭；不授生产ready或0.72%因果。 |
| 02492 | P | unlabeled self-training产生reward rationale/label，改变generalist reward pretraining路线；推理文本不等真实因果解释。 |
| 02522 | P | reward作label的score-function CE与gradient actor/critic耦合，是RLVR优化替代；理论假设与性能尚未正式Evidence。 |
| 02447 | P | tile/error-correction联合stream/kernel interleaving改变生成水印检测的资源-准确性取舍；不由responsible术语授不可去水印保证。 |
| 02512 | P | per-expert Hessian trace sensitivity替activation frequency分配mixed bits，是VLM-MoE校准条件，不照录optimal/通用同质量。 |
| 02503 | C | 新闻headline四选项与既有sentence-transformer cosine排名是资源/任务扩展；完整AB未建立新受控评价盲区或有效性条件。含semantic/lexical选项不自动成为新评价理论，RAG关联也不足准入。 |
| 02401 | P，局部优化反侧 | uncertainty reward schedule/cheap perplexity proxy与CoCoA成本及early-collapse比较改变LLM RL配置；不采omics下游科学应用、阈值校准或abstention安全保证。 |
| 02479 | P | external-tool feedback低概率token/void turn梯度异常与trajectory过滤稳定多轮RL，是训练失败路径与干预选择。未核完整因果归因/所有工具，不照录SOTA。 |
| 02514 | C | code-mixed专用PLM微调对比zero-shot Gemini和通用模型榜单；没有隔离新pretraining/transfer成立条件。不是局部、小模型或语种标签排除，不采训练语料内因推断。 |
| 02494 | C | LLM接口调用既有power-flow/N-1 solver，正确性来自deterministic求解；没有新LLM运行/验证条件，属领域科学计算应用。小模型同accuracy不证明新学习边界。 |
| 02480 | P | optimizer-update关键I/O路径、remote tier闲置及concurrency contention→multi-tier/cache/path offload，是训练运行替代机制；280B/2.5x需具体配置才可采用。 |
| 02521 | P | natural continuous monologue的前/后audio dual training替word-timestamp对齐，改变full-duplex factorization/预处理条件。 |
| 04500 | P，设计反证 | 固定contamination-ratio alignment换比例退化，joint appropriateness/answer训练和混合context是替代；RW类比近似，不能变为心理机制或通用安全定律。 |
| 04499 | P，限真正差额 | eight metrics/303 corpus来自2410.22349，不作新机制；新GSE/DeepResearch配置的citation-thoroughness不保支持/多视角是具体反侧。admin overlap不全稿C，也不授新首公开日。 |
| 10511 | C，风险core已读 | 实际五维linear-Q安全日志模拟与dual-memory/curiosity组合，非大模型学习/训练/推理或Agent机制。异常率/precision与计数矛盾不采用；未按cybersecurity词自动P。 |
| 10509 | P，局部递归训练反侧 | quality filter与等数量random filter对比，允许区分选择/少数据；单Gemma2B摘要五代，6.6%不共用base，不能采普遍anti-collapse/AI安全韧性。 |
| 04505 | C，风险core已读 | EDSAC移植伦理量表+静态construction scenario排名/访谈，未形成新模型执行/受控评价失效条件；generic advice/oversight意见不等新可靠性协议。不同模型数/rubric叙述保留，不采训练归因、法律或伦理保证。 |
| 02560 | P | VGGT token collapse与3D-task-specific partition merging，是视觉foundation long-sequence执行设计；4x/1000图等质量与误差尚未独证。 |
| 06986 | C | CellPainting专用cell-morphology/source-context biological profiling/integration，属于暂缓科学应用路线；仅称foundational不建立与本项目多模态基础模型主线关系，不借通用representation owner重新引入。 |
| 02563 | P，安全反侧 | free-form rule guard双mode训练与unseen-policy评价，factual/counting/multi-clause高错误及长度下降是具体边界；不把解释可读当正确执行。 |
| 03353 | P | accuracy-resource concavity与model/data/task多维utility allocation改变多agent公平/效率取舍；BERT/小视觉模型不自动排，不采25%普遍性能。 |
| 04507 | C | transformer ASR+LLM语言postprocess的silent-speech WER提升，完整AB没有新对齐/误差传播条件；仅成熟pipeline应用，不因silent-speech或小结果关。 |
| 04502 | P，局部训练失败 | reward按输出segment/gradient scope拆分，format reward移除影响其它reward解析和训练崩溃；具体接口条件值得核，不采RAG immunity。 |
| 01878 | C | marine趋势/数据和既有weak/open-set/robust方法归纳，未给本稿新通用learning设计/测试条件；不把提及foundation当主线贡献。 |
| 01928 | C | continuous Ising/DC solver的ground-state优化与GPU matvec实现，无服务主线大模型计算/学习更新机制的具体联系；GPU/convergence术语不能代替范围。 |
| 02640 | **C?→P，局部适配反侧** | 同UNI2-h三variant中VPT/TTA提高sensitivity却降低specificity，修正“最佳robust”单指标判断；只foundation adaptation取舍，不引临床应用或排行榜因果。 |
| 01794 | C | EHR多biomarker的Bayesian BERT/DeepMTR预测应用，无新通用训练/不确定性成立条件；Attention与uncertainty词不证明主线贡献。 |
| 01886 | C | postdisaster路网变换/AEDM/POMO与synthetic routing应用，未建立foundation/VLA或模型训练/推理系统新条件；不是所有RL规划排范围。 |
| 01679 | C，已补完整AB | bidirectional branch/trunk DeepONet cross-conditioning按四PDE/物理方程选variant，实际是物理operator求解路线；没有主线foundation表示/生成/运行机制联系，不仅标题按physics关。 |
| 02481 | C，已补完整AB | hydrological pixel-basin图与时空attention用于flood，64 A100用data parallel扩训练；没有新大模型状态/通信/执行或一般学习成立条件，不因Distributed就授系统准入。 |

### 13 个新增必要 core 与一项先稿定点比较

累计 **35新身份必要core**（前22+本13）；额外2410.22349只比较04499受影响旧定义/数据，不新增跨日队列。core均采用作者已保存exact-v1 HTML/raw/request，三个404 HTML的PDF fallback实际已读分页；下载不算读完。以下是实际到达位置与采用边界：

- **02449** §4.2.6/4.3.3/6.2/6.4。generate→REPL test→evaluate→register是成熟流程。77中63≈81.8%，14失败后prompt/registration改进未给独立重测分母；93%=186/200而非“tool creation”原子成功率，旧tools100%不含新工具失败。其sandbox主张与future REPL mitigation并存，未验证代码/集群隔离。P限评价与失败子分母，不把我们发现的算术差额变为论文新安全实现。
- **02401** §3.3/3.4/3.6、§4.6 schedules/signals/thresholds、§6、Appendix E.4/TableA8。训练Perp便宜proxy、CoCoA多rollout成本2.6x；adaptive weights避免fixed early-collapse是局部学习取舍。abstain-if-sum>2κ与TableA8较高κ coverage95→70→40方向冲突，保留未决，不修正文公式或采校准/abstain保证。科学预测下游不读不采用。
- **02464** §3.1–2/4.1–2、Appendix F/G。按judge Likert分层每statement20prompt，118statement/2360输入，三个provider-spec采用日期不同；不能外推天然请求违约率或当前所有provider政策。Human study仅60sample，κ低且部分负值；model judge偏严/自偏好实际读。P为三方一致性审计反侧，不授人类truth、提供者合规或AI安全认证。
- **02499** §3.3–4/4.1/4.3–4/Limitations及Appendix F.1–2。m-nearest prototype与static threshold/nearest vote/硬style分类、SAR开关/PCA维数均有具体比较；平衡human/generated reference/test与两unseen styles、一个GLM130B只局部OOD。既有logistic/XGBoost不是新理论，条件阈值选择P；式4不读取全部proof而授有限样本校准，accuracy/F1不认证个体原创归属或false-positive安全。
- **02408** §1.1/2.2/4/5.1–3。page hit0/miss1，层顺序固定；LLRU按last-round再relative-layer distance淘汰，真实Mixtral top2/Llama-MoE top4重排成多个单expert-round后模拟。不能将miss比例当真实GPU、SSD、异步prefetch latency。贡献清楚即停，extended先稿身份/事件必要材料仍由author精确隔离，不授全文比较已完成。
- **02640** Methods三项、Results/Table1、Conclusion全部必要段。VPT冻结backbone，GRL/scannerlabel与flip/rotation/两stain-normalization TTA为既有组件；Table1 specificity .8443→.8408→.8097而sensitivity .8169→.9014→.9577，非全metric robust。三行预算/scanner细控未披露，不授pure TTA因果/临床效用；P最小为foundation适配评价取舍。
- **10511** [分页PDF](SUP_PDF_2509.10511v1_20261011.txt) physical pp6–13，§3.5/4/5/6.1–4。5×4线性Q权重和模拟47.9%anomaly、全malicious倾向、precision约.48实际读；TP47686 vs后来17964、F1 .6461 vs .6233、variance44.63 vsbelow5冲突留存。它是专用log classifier/传统RL应用，C不是以数字不可信代替主线贡献判断，不授生产安全/LLM角色。
- **04505** [分页PDF](SUP_PDF_2509.04505v1_20261011.txt) pp3–7 §3–6。七项Likert伦理checklist、静态12scenario、12expert访谈；72写12×2×3，method/results却三model，Table1维度又不与七项全匹配。只能领域问答/态度测量，未新增Agent权限、执行验证或控制条件；training-data/RLHF解释属猜测。不因safety/negative词或小样本直接决定P/C，实际core后C。
- **02563** §3.1–2/4及Appendix A.3/Table7–8。rule/dialogue输入、1/3CoT与2/3answer-first训练、SFT+GRPO；F1任务间差异，factual73.4%/multi-clause60.7%/counting53.4%error。长度accuracy<50%不是hard-cap支持量或保证规则数内全正确；不采无害输出/真实执行安全。
- **04502** §5.2 Partial-GRPO/6.2/6.5。format对whole completion、helpfulness对analysis、conclusion对summary的reward scope实际读；conclusion只检查与自己helpfulness标签一致，不是外界truth。去format使其它reward无法parse、训练collapse是具体接口反側；GPT4o judge+污染比指标不授human truth/RAG免疫，未核所有baseline/代码。
- **04500** §3.3/4.2各baseline反侧/§7。固定混合比alignment有益而换比例可能较untuned差，单独awareness不保answer、filter残污染，joint assessment+answer与位置/数量变化训练P；RW类比approximate、web自然污染频率unknown、model有限。不把神经科学类比引入新的机制owner。
- **10509** III-B1–5/IV-B/TableII/IV-D/V。Gemma2B-it累计LoRA r8/α16、五代三seed、100generated/等数random过滤、50held-out test及1000bootstrap实际读。Quality Gen5 .1746与sharedGen0 .1746相同；+6.6%由它独立.1638起点，不能同base宣传提升。BERTScore/BLEURT局部方向仍有信息，latent guidance/error ratchet是假说，不授通用反model-collapse或AI safety韧性。
- **04499** 新§3.1.3–4/3.2–3/4/Appendix A；[先稿官方页](SUP_DEEPTRACE_PRIOR_20261011.raw)完整AB/history及[先稿v1核心](SUP_DEEPTRACE_PRIOR_CORE_20261011.raw) §4.2.3–4/5.1实际比较。先稿已有8metrics及303=168+135问题，uncited公式/空列例子冲突、source-only cover与minimum vertex-cover/Hopcroft-Karp混同也同源，不计新纠错。新稿GSE/DR配置评价有真正窄差额：高citation thoroughness不保statement support/多视角。Gemini citation table50.3 vs正文40.3冲突，不采用该排名数字；未复核全judge/所有case/源码，admin overlap不等已审同一事件或首公开已确认。

后37全部current raw/request实际看comments/history、均200；04499 overlap按上项实际处理，其余无明确withdraw/correction。MICCAI/EMNLP/AAAI/ICML/SC/ICCV等会议标签只是线索，不全会追查。五scope-title轻核也已完成：01736 LHC jets、02060 peptide discovery、02661 AI+MPS社区paper明确科学领域，三者未读AB不称贡献层关闭；02661与旧75的同身份重叠只作范围/去重，不复活旧池。两架构含糊标题实际补AB后C，未发现同因漏收，不需要全科学题名正文。

新98身份的本轮准入普通工作已完成；72P **全部必要公开日/事件未确认、不评分不入Books**，其中02408先稿/extended与04499新增评价事件更须精确材料，不能以generic overlap/版本号关。确定IP候选1的必要Evidence/仅报告复用§6，尚需14来源实际原件及作者完整六节DAY；本节只交准入校准，不预支全日完成。已给Meitner同步两P改判和95/3证据层计数，禁止用普通未读伪装外部停止。

## 10. 来源与六部分 DAY

2026-10-11 实际回读作者六节 README、SUP_SOURCE、SUP_SCREEN 与02408事件门；压缩恢复重读AGENTS/当前合同/每日来源及arXiv/Prompt/ROADMAP，本日State只作路由。来源不是仅采信作者停点：本人读取以下原始列表的日期/题名/实际数组、相关请求URL/status与分页，未把抓取或下载算语义阅读。

| 来源 | 本人实际核到的有限范围与停止 |
| --- | --- |
| OpenAI | RSS完整1287项转BJT，Sep02→Sep04；Sep03发布全文、邻接日期及当前支持文档沿§6实际阅读复用。403只作抓取结果。 |
| Anthropic | 从raw的Next RSC push逐JSON解码、递归取得174唯一publishedOn对象；实际检查日期字段，Aug27→Sep05，没有Sep03。不是研究站历史全集。 |
| Google | September Blog两页13题名与2/2末页；DeepMind page5的24题名/6Sep项，旧同日日期原件定点复用；Publications现1–15/11612与年份入口不能授Sep03历史切片。RoboBallet完整AB沿§6复用C。 |
| Meta | results5/6的2025段Sep24/23/22/15→Sep08/Sep02→Aug22，2017–20插入不作停止；Blog2/3的Oct31→Oct24→Aug27/14/07→Jul31，旧插入/置顶不误当顺序。DARLING不迁日。 |
| Qwen | JSON60完整date/title，Aug18→Sep08/10/21/22；配置日期不等首公开全集。 |
| DeepSeek | 当前Research链接与Updates的Sep29/22→Aug21完整受影响段；非2025全部研究保证。 |
| Moonshot | 实际26题名日期，Sep16/05→Aug22；不使用commit充公开证据。 |
| Hunyuan | publicList实际POST page1/size1000/renderType0、en/zh请求及9/9、11/11完整title/displayPublishTime，均2026；能解析API不等恢复2025。 |
| ZAI | Research15→18卡/末没有更多，最早Dec07；current release最早Sep30，与旧同日Aug11/08精确原件复用区分。Research历史缺段不能由release替代。 |
| Seed | US paper token0的18/94/next20与token20的20/94/next40，Blog15/49；Sep22→Sep02/01→Aug13及Sep09→Aug21实际跨窗。CN空counterprobe和US20slot仅18可见不授全94条；不继续未必要分页。 |
| ERNIE | 两页10+6卡、2/2末页，实际核心描述与Sep12 PLAS→Aug14 FastDeploy→June30；目录外未核。 |
| MiMo | 8Paper及15current Blog题名；旧/新首页的index.c5195ace脚本URL相同，旧组件原件明确slice(0,c)/slice(c)本地展开，不是历史请求。2025 Blog不在当前集合，不能据More授恢复。 |
| MiniMax | EN12/CN13全部目录日期/核心描述，EN最早Oct27、CN另Jan15；旧同日EN第二页有效重复停点复用；Agent3项均2026。用户space网站不是官方研究，不扩队列。 |
| arXiv | 四实际request：submittedDate[202509011800 TO 202509021800]、start0/max200；model51/systems17/multimodal21/agents38=127→98，total均小于200。该代理只发现，95完整exact-v1AB/3范围题名与98current轻核沿§1–9复用。CL/LG exact Sep03路径实际HTTP400，未把错误页授公告。 |

作者限定primary-domain历史查询只作恢复线索，不授召回或历史零；Google publications、Hunyuan2025、ZAI Research、Seed稀疏记录、MiMo2025 Blog、MiniMax2025缺段按§2/5隔离。必要日期未立的72新潜力和旧46不支持正面Coverage/Evidence、Books、性能/安全或无遗漏；身份/缺什么/接受的官方日期材料与定点重开均在本日筛选及§5。没有普通未读被冒充外部终态。

02408额外定点核官方Springer DOI `10.1007/978-3-031-99872-0_2`：First Online/Published均22 August2025，同四作者、同paging/LLRU核心AB，reference2明确2025 extended HAL04961621；citation year2026不覆盖首公开。作者EuroPar页同AB并链HAL05226723。本人请求HAL05226723v1/document实际Internal Error，HAL04961621实际Anubis Access Denied(error9e4edb5b6b850c41)，不是正文或timeout。已有先公开核心不等扩展稿无贡献，但未有精确差额/新事件证明；P保留于必要先稿门，不继续读无关全文。

**DAY结论：通过。** 本人完整读到当前六部分：§1漏斗分层准确；§2十四源自包含有界停止与限制；§3只有IP确定1家族，2+2+1=5且安全发布必要深入；§4原连续两段逐字存在，新增35core与先稿比较不冒充72候选Evidence，IP单篇Evidence/Ch72具体仅报告沿§6复用；§5普通研究已收敛且外部终态有明确身份、权限及重开门；§6首批/全部拟项和安全反侧/分层C/共因改判的实际范围不多授。机械比较原窗口逐字相同、原§4完整连续，旧正式0/46P/54AB/18core未重算。未写报告、Books、State、index或scripts，Books实际新写0。作者可以只更新完成态与机器/链接/冻结检查；本人尚须实际FINAL差额回读，DAY不预授FINAL。

## 11. FINAL 完成态差额

**结论：通过。** 作者通知完成态ready后，本人实际回读当前metadata、§1/5/6和SUP_SCREEN/SUP_SOURCE末尾行政同步，不重审§1–10已有效题摘/core/单篇。状态完成、补窗Sep03、Books纳入本次、检查时间2026-10-11T20:17:11+08；§1/5/6引用实际DAY并保留外部限制，未借完成标签授全源Coverage/Evidence、无遗漏或安全/性能保证。正文仍为确定IP1/必要深入1/仅报告1/Books新写0，95AB=72P/23C加3范围题名、35必要新core加04499先稿比较；旧正式0/46P/54AB/18core保持，原窗口逐字相同、原§4两段完整连续。旧10518撤回链与03054有效纠错边界未复活或迁日。

本人实跑当前完成态V3通过。首次调用因安全路径未加载validator模块而未启动校验，补显式scripts模块路径后成功，未把首次调用错误称通过；全程禁bytecode写入。本人核185SUP request/raw sha全部吻合、四Atom实际total/entry为51/17/21/38；独核49本地引用目标均存在、无行尾空白/冲突，限定本日README/_sources的unstaged及cached diff-check通过。作者报告118引用等检查只按作者层归属，不将机器检查当语义验收。无stage/commit/push，未写共享Books/State/index/scripts或作者报告。

Sep04本轮普通研究与独核待办0；72新与46旧必要日期/事件、六具名历史来源仍精确终态保留，不取消潜力，不授正面覆盖。按用户连续路由可转09-06；下一日重新加载当前合同、本日原档与Sep05完整自然日，不继承Sep04队列。向root交本日精确摘要/本note，行政计数由root维护。
