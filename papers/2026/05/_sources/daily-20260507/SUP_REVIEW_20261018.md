# 2026-05-07 补查独立复核

复核者：`/root/supp_may07_reader`；非 Report 作者；本日启动日期为 2026-10-18。仅维护本文件，不修改 Report、Books、Learning State 或索引，不 stage、commit、push。

## R0 — 恢复边界与日期工具预检

已完整读取本次适用的 `AGENTS.md`、研究合同、Report 合同、来源清单使用说明/每日组/arXiv 主题、统一 Prompt、ROADMAP 与 Learning State 当前恢复入口。按 `using-agent-skills` 的范围与验证要求约束复核；不另开新日期或材料池。

- 当前 checkpoint 为 126/279 已验收，下一日报为 2026-05-07；用户本轮明确恢复。新增窗仅 2026-05-06 完整北京时间自然日；原 160 候选、评分、日期、原小时窗及有效技术证据保留。本轮不复核 May06 或其他已验收日期。
- 已读取本日旧 README 开头、active ledger/packet 的数据结构、2026-09-15 第四次非作者终审与机构窗口复查。本动作只确认恢复接口，不把旧 marker、完成标签或作者摘要当成本轮独立证据通过。
- 旧 ledger 的 `datacite_initial_created_timestamp`、`first_public_time_derived` 和 OAI 更新信息不是新补窗的 `registered` 组合核验替代物。旧 548 原始身份不是必须全量重新关闭的队列；当前合同不自动触发旧 160 全盘重审。
- 具名身份注意项：旧 ledger 的 `2605.04050` 记录 v1 提交为 `2026-02-14T20:46:47Z`、旧归属为 May07。这是需要避免把同名/提交字段直接当日期证书的具体例子；本轮尚未重新核其原件，不改旧日期、不作新的日期结论，也不据此扩审整个旧池。
- 已逐行检查 `scripts/arxiv_publication_date.py`：只读本地原 JSON，要求精确 DOI/ID、`arxiv.content`、`findable`、唯一 `Submitted/v1`、带 UTC 时区的 `registered`、包络不倒置且整段同一 BJT 日；`created` 仅一致性检查，不参与日期上下界。脚本本身不证明原件真实性、历史规则适用性、全球首次公开或贡献。
- 实跑 `python3 -B -m unittest discover -s tests -p test_arxiv_publication_date.py`：19 tests 通过。本轮尚未取得新增窗具名原 DataCite 与发现原件，故不授予任何新增日期或来源覆盖通过。

待 root 提供：拟使用的本日历史 arXiv 发现原件/查询与停止位、首批准入候选及代表性排除项。收到后只校准该受影响集合；尚未进行 Source、Books POST 或最终 DAY 验收。

## R1 — 首批准入校准及具名日期组合

root 提供的发现路径为本地 `../datacite-arxiv-202605-v2/doi-prefix-2605-{02,03}-page-01.json.gz` 的题摘线索。已独立解压读取以下 13 个具名身份的完整题摘、版本日期和 Other 注释；随后打开其精确 v1 官方 abstract 页面（BifrostUMI/SigLoMa 另定点打开 v1 HTML 的相关方法段）。这些压缩投影没有 `registered/state`，所以对其运行依赖该字段的过滤得到零不构成零发布。`Updated/v1=May06` 仅作发现，不能单独证明公开日。本轮未自行重建或扩大 root 的 432/316 标题池，也不对未实际读过的池成员授准入通过。

### 日期原件与实际复算

本轮实际 GET `https://api.datacite.org/dois/10.48550/arxiv.<精确ID>`（下表链接），使用完整单条响应调用 `publication_date_envelope`，不使用旧压缩投影。8 项全部实际核到 `data.id=attributes.doi=10.48550/arxiv.<对应ID>`、`relationships.client.data.id=arxiv.content`、`publisher=arXiv`、`state=findable`、且只有一个 `Submitted`、`dateInformation=v1`。原 `registered/created` 为毫秒 UTC 字符串，表内原样保留；Submitted 原为秒级 UTC。下界按合同引用的官方公告/发号规则、America/New_York 夏令时复算；不把它称为单篇实际发布时间。

| 身份 / DataCite 原件 | Submitted v1 | registered 原字段 | created 原字段（仅一致性） | 包络复算 |
| --- | --- | --- | --- | --- |
| [2605.02950](https://api.datacite.org/dois/10.48550/arxiv.2605.02950) | 2026-05-01T17:46:26Z | 2026-05-06T01:42:43.000Z | 2026-05-06T01:42:42.000Z | 最早 2026-05-04T00:00:00Z，上界 May06，跨 BJT 日；未决 |
| [2605.03096](https://api.datacite.org/dois/10.48550/arxiv.2605.03096) | 2026-05-04T19:17:53Z | 2026-05-06T01:46:14.000Z | 2026-05-06T01:46:14.000Z | bounded 2026-05-06 |
| [2605.03222](https://api.datacite.org/dois/10.48550/arxiv.2605.03222) | 2026-05-04T23:21:24Z | 2026-05-06T01:49:19.000Z | 2026-05-06T01:49:18.000Z | bounded 2026-05-06 |
| [2605.03403](https://api.datacite.org/dois/10.48550/arxiv.2605.03403) | 2026-05-05T06:23:20Z | 2026-05-06T01:53:39.000Z | 2026-05-06T01:53:38.000Z | bounded 2026-05-06 |
| [2605.03452](https://api.datacite.org/dois/10.48550/arxiv.2605.03452) | 2026-05-05T07:35:09Z | 2026-05-06T01:54:49.000Z | 2026-05-06T01:54:49.000Z | bounded 2026-05-06 |
| [2605.03517](https://api.datacite.org/dois/10.48550/arxiv.2605.03517) | 2026-05-05T08:53:00Z | 2026-05-06T01:56:27.000Z | 2026-05-06T01:56:27.000Z | bounded 2026-05-06 |
| [2605.03846](https://api.datacite.org/dois/10.48550/arxiv.2605.03846) | 2026-05-05T15:13:15Z | 2026-05-06T02:04:27.000Z | 2026-05-06T02:04:27.000Z | bounded 2026-05-06 |
| [2605.03884](https://api.datacite.org/dois/10.48550/arxiv.2605.03884) | 2026-05-05T15:44:29Z | 2026-05-06T02:05:25.000Z | 2026-05-06T02:05:24.000Z | bounded 2026-05-06 |

7 项 bounded 的最早界均为 `2026-05-06T00:00:00Z`，晚界分别为表中 registered；完整区间位于 May06 BJT。独核仅通过有条件的 arXiv v1 公告日，不证明全球首公开、正文逐字历史或技术结论。KAHM 不因跨日而否定潜在贡献；不得先记确定当窗候选，尚可执行的是定点恢复其历史公告/列表或等效直接证据。

### 拟入选校准

- [KAHM 2605.02950v1](https://arxiv.org/abs/2605.02950v1)：准入理由成立，日期待恢复。冻结 teacher/index 后，在线 query 神经编码不是唯一选项；词法特征到 prototype 权重的几何估计给出不同延迟/拟合误差分解。须限定 fixed-teacher supervised retrieval；题摘的法律领域不是排除理由。注意 v1 原标题是 **Kernel Affine Hull Machines for Compute-Efficient Query-Side Semantic Encoding**，不能把当前 v2 改题当 v1 标题。
- [HyPA 2605.03096v1](https://arxiv.org/abs/2605.03096v1)：准入成立。不能默认软 prompt 直接线性相减能去 confounder；任务 prompt 与线性化 confounder prompt 的混合组合是可检验替代，需核非线性交互、matched baseline 与 ID/OOD 取舍，不先接受普遍 deconfounding。
- [Neural Sensitivity 2605.03222v1](https://arxiv.org/abs/2605.03222v1)：准入成立。全局 activation/readout 相齐不保证局部扰动可辨；引入指定坐标子空间的 pullback/Fisher 及相应 task family，可能改变表示比较协议。需核噪声/regularization/坐标选择及证书前提，不外推为通用表征优劣。
- [GRPO-TTA 2605.03403v1](https://arxiv.org/abs/2605.03403v1)：准入成立，但不是因把 GRPO 换场景。无 gold 的 CLIP top-K group、alignment/dispersion reward 驱动视觉编码器更新，提出自奖励在分布漂移下的更新条件问题；须核 reward 自确认风险、reset/update预算与真正可归因对照。
- [LDM 2605.03517v1](https://arxiv.org/abs/2605.03517v1)：准入成立。latent likelihood/entropy 把 alignment 与防 collapse 放到同一统计目标，并以 predictive identifiability 提出前提；可能修正“预测目标自然恢复真实状态”的解释。须核定理假设/等价类，不把综述统一语言本身当贡献。
- [QKVShare 2605.03884v1](https://arxiv.org/abs/2605.03884v1)：准入成立。量化 cache payload、注入路径及多次 handoff 提出重 prefill/传输成本与累积误差取舍；摘要已主动收窄到 150 GSM8K、Llama-3.1-8B 与更深 hop/更高 budget。无 apples-to-apples runtime 对照，不先宣称普遍端侧加速。abstract 仅列 PDF，正文审阅可转 exact-v1 PDF，不以无 HTML 自动受阻。
- [BifrostUMI 2605.03452v1](https://arxiv.org/html/2605.03452v1)：准入成立，不应仅按“UMI 移植到 humanoid”关闭。已定点读 §II-B、§III-B–D：与隐式把 IK 藏在低层 policy 不同，SKR 显式将五 keypoint 转为 root/joint reference；只调整 pelvis–foot 竖向尺度，保留任务 metric，再交独立 WBC 做 dynamic tracking。该 kinematics/dynamics 解耦和 scale boundary 是具体设计增量；尚须评价/限制审阅，不因 schema 名称先授 Source。v1摘要是两个场景，当前metadata摘要为五个，后续必须精确v1，不能混用。
- [SigLoMa 2605.03846v1](https://arxiv.org/html/2605.03846v1)：应从 root 拟关闭改为准入，理由仅限具名原增量。已定点读 §3.1–3.3：用可见面/FoV和 solid-angle 权重处理模拟均匀 surface sampling 与真实 mask 回投像素密度差异，再以 weighted PCA 生成同一 sparse geometry；这不是只有通用 KF/curriculum 组合。它提出 sim/real observation distribution 的显式桥接，足以核验；不接受摘要的“guarantees native alignment”强说法，仍需 ablation、遮挡/PCA轴退化及高频控制相关反证。

本轮拟入选只是准入通过：其中 7 项日期组合可确定本窗，KAHM仍日期未决；未授任何完整 Source、Books 判断或写后通过。

### 代表性关闭与撤回

实际读完整官方 v1题摘及版本页：

- [StateSMix 2605.02904v1](https://arxiv.org/abs/2605.02904v1)：保持关闭。不是因小模型或非LLM；已明确 online SSM＋sparse n-gram confidence mixing＋arithmetic coding，以及可分离的压缩消融。但新增证据限逐文件无预训练压缩器及部分 enwik8 切片，未形成改变模型训练/显式历史状态取舍的机制边界；不把“无GPU/打败xz”单数字当主线增量。日期不影响此贡献关闭，不另追跨日。
- [AutoRAGTuner 2605.02967v1](https://arxiv.org/abs/2605.02967v1)：保持关闭。组件注册、双向指针承载 node/edge/hyperedge 与 Bayesian hyperparameter search 是明确工程组合；题摘尚未指出改变 RAG 检索/证据更新语义或调参有效条件的新机制，胜 default 与 code-churn 不足以单独准入。不是因已有owner覆盖而关闭。
- [cotomi Act 2605.03231v1](https://arxiv.org/abs/2605.03231v1)：保持关闭。lazy observation、diff history、coarse actions、best-of-N 与行为抽象共享 artifact 的组合能解释demo结果，题摘未给出新的观测/记忆可靠性边界或分离归因；179-task子集80.4%不能直接变成人类能力超越。保留此具体理由而非泛称Agent应用。
- [MILE 2605.03555v1](https://arxiv.org/abs/2605.03555v1)：保持关闭。frozen base、per-task LoRA 与 prototype gate 的组合应用于 domain/modality segmentation，题摘未给出新的参数隔离、router 可辨或扩展代价边界；不能只因为“adapter较省”或新的任务基准就准入。不是按非LLM标签排除。
- [HeadQ 2605.03562 当前官方页](https://arxiv.org/abs/2605.03562)：独立实际核到页面明确 withdrawn、v3=`2026-05-19T17:40:13Z`，作者注为发帖后发现伦理问题。执行最小撤回排除，不评分，不保留selected或Books采用链；不因其题摘具备潜在贡献而恢复。未重读被撤回正文。

本轮分层校准覆盖理论/表示、PEFT、视觉适应、cache系统、embodied接口及4个一般关闭和1个撤回；不冒称316/432身份全量准入核验。SigLoMa错误理由的受影响集合仅当前这一具名项，未由此扩大到全机器人目录。机构代表关闭待实际原件到达后另核。

## R2 — 两项机构代表关闭独核

接 ORG_A 提供的实际 primary URL 后，本人重新打开正文而非仅据其摘要签字：

- [OpenAI May06 privacy guide](https://openai.com/index/how-chatgpt-protects-privacy/)：实际读完整英文核心从训练来源到响应隐私/责任段（网页 §What information may be used in training、§How we reduce personal information in training、§Privacy controls in ChatGPT、§Preserving privacy in responses）。明确为 plain-language guide；使用 Privacy Filter 的多阶段防护及用户控制属于说明，正文没有新增过滤算法、可比实验或隐私失败边界。保持本项贡献关闭，不采纳其“比同类更有效”宣传为新正面证据，不为核一般说明扩扫所有隐私附件。
- [Anthropic May06 limits/SpaceX](https://www.anthropic.com/news/higher-limits-spacex)：实际读 §Higher usage limits、§New compute partnership with SpaceX、§Expanding internationally。页面给出的本日配额、容量采购、区域供给和硬件事实没有披露新的调度、训练运行时、可靠性或隔离机制；因此关闭。不是因商业机构或产品名排除，也不把GPU/MW规模当系统贡献。未检查无关 Related content。

上述两项具体准入关闭独核通过，不等于其机构历史目录覆盖通过。Google/DeepMind pub239849 原件尚未取得：定点尝试 `research.google/pubs/pub239849/` 返回不可访问，ORG_B明确不拥有该材料；等root提供其真实原件路由后继续，不据此写零命中或最终保留。

## R3 — Google/RoboFusion 与机构有限停止位

root 已提供真实 [DeepMind pub239849](https://deepmind.google/research/publications/239849/)，本人实读完整官方 Abstract：研究 WIOA 劳动培训记录、工资恢复与职业自动化暴露，未研究模型学习、训练/推理或模型评价机制。范围关闭通过；不因为来源是 DeepMind 或出现新 Index 就映射模型平台评价。此前猜错 Research URL 的访问失败已由正确原件恢复，不保留为必要证据缺口。

实际重开 [RoboFusion 官方 README](https://github.com/Tencent-Hunyuan/Hy-Embodied-RoboFusion)，读协议概述、PDO/SDO结构、设备/端口与状态定义：原增量是低层设备二进制通信规格，没有新学习/反馈动作语义或改变 controller 边界的可靠性/成本证据。保持具体贡献关闭，非因机器人不属范围。另实际 GET [commits API](https://api.github.com/repos/Tencent-Hunyuan/Hy-Embodied-RoboFusion/commits?per_page=100) 得4项，最早提交 `31d5cb030085b0949d35a9fdba8aa6629715ee73` 为 `2026-05-07T05:57:24Z`；创建日不当公开日，README Apr13/14文档标记也不当首公开。贡献已关闭，不再为日期扩请求。

已读 ORG_A/ORG_B 两份实际来源记录，检查13机构入口、窗口主题、动态恢复、分页/停止位与缺口是否自洽。独立重取原件的目录抽核为混元：`POST https://api.hunyuan.tencent.com/api/blog/publicList`，body `{"pageNum":1,"pageSize":1000,"renderType":0}`/pageNum2，header `accept-language: zh`，实际第1页total=11/list=11，May21 Hy-MT2与Apr30 Real life夹住窗口；第2页total=11/list=[]。列表仅当元数据查漏，不逐项展开其余正文；未把中文11项当全仓库全部发布保证。

其余12机构本轮复核的是记录中实际路由、字段口径和stop的合理性，未声称本人全部重新抓取。Seed原毫秒字段被ORG_B正确换算为北京时间May07（1778083200000）/May06（1777996800000）；不能复用旧UTC标签。Qwen40+40、Anthropic184、OpenAI1299等是目录元数据，不是题摘/候选数；GitHub created有限查询也不证明旧仓库release/转公开完整性。MiMo嵌入页面恢复、Meta/Google Research历史缺段等差异已有明确边界，没有发现把有限目录或搜索空返回伪装全来源无遗漏的共同错误。此处是分层抽核，不授13机构全Coverage或所有排除项全文通过。

KAHM仅另试官方历史月列表 `https://arxiv.org/list/cs.LG/2605?show=2000`，未能取得该历史页面，故没有直接公告新证。一个当前pastweek请求不是历史恢复原件，未用于本日发现/筛选/覆盖；不进一步扩列。R1跨日包络继续保留，定点请求官方May06公告/分类列表或等价直接证据，不称其组合失效即零发布。

## R4 — QKVShare 精确 v1 必要 Source

材料：[2605.03884v1 PDF](https://arxiv.org/pdf/2605.03884v1)；官方abstract当前只有该v1，R1日期结果复用。按 PDF 技能读相关完整页与表格文字；网页截图接口两次失败，未声称视觉渲染通过。本人已实读 §3.3–4.3 方法、§5评价协议、§6.1–6.4表2–4及 §7直接限制；没有运行代码或复现实验。

**机制：** local importance与downstream demand/segment/anchor信号分配token bit；CacheCard保存quantized groups及metadata。关键边界是它目前在runtime内交接，接收端先恢复FP16 `past_key_values`，不是native量化attention；position-offset仅placeholder，不证明跨prefix对齐。

**评价：** Llama-3.1-8B-Instruct、4-bit weights、12GB RTX5070Ti Laptop；adaptive为HF/PyTorch，baseline为llama.cpp。E1是150 GSM8K、2–5 hops final numeric EM；E2是300题paired比较，topology vs local净+2、vs uniform净−1，不能确立topology独立收益。E3只测uniform Q4单handoff、TTFT median n=2；名义1K/4K/8K实际约476/1939/3877 tokens。8K卡交接397.1ms低于re-prefill1029.7ms，但native cache-restore26.5ms更快；不同runtime不能归因纯量化/拓扑机制。

**直接反侧：** §6.3 stage计时包含create/inject/generate，不能把payload压缩等同端到端加速；§6.4的64vs23驻留密度属于uniform Q4基础，不是QKVShare直接密度实测。§7承认4-bit结果噪声、topology未分离、无native fused路径；batch/concurrency/SLO未完整披露，输出长度Not Disclosed，不能外推移动NPU、异构模型或通用Agent图。

**本轮结论：** 必要方法/评价/直接反侧已读足，可支持“handoff须同时核payload、接收重建/生成成本与多hop质量预算”这一受限设计问题；不支持topology普遍优于local、全程量化驻留、跨prefix/异构模型无缝转移或生产能力。准入保持，不因反侧删候选；评分和Books具体处置由root对读owner后作出，本人尚未核其Books实际改动。若root采用更强命题，必须先重开对应证据，不将本R4当强主张通过。

## R5 — 第二批22项具名准入校准

实际从 `../datacite-arxiv-202605-v2/doi-prefix-2605-{02,03,04}-page-01.json.gz` 提取并完整读取以下22项的题名、全部摘要与Other。仅校准root给定14潜力和8代表关闭，没有扩成316/432逐项队列。以下“准入”不表示结论成立或完整Source已读；本批日期由root另取实际DataCite，本人未重复请求，也不在此虚称独立验证了这14日期原件。

| 身份 | 独立准入判断及采用前必须核的具体问题 |
| --- | --- |
| [2605.02930](https://arxiv.org/abs/2605.02930v1) | 潜在准入成立：weights/text双视角phylogeny不只是视觉类比，已设known-training-lineage控制，可检验何种行为/权重距离能恢复训练关系；不能从相似直接推数据因果贡献。root实取包络跨日，该潜力留日期隔离，不先列确定May06。 |
| [2605.03135](https://arxiv.org/abs/2605.03135v1) | 准入：NEC明确区分错误频率与实例行动代价，并以cost-sensitive训练无稳定收益这一反侧限制设计；须核cost如何确定/归一、是否把难度误当真实代价。 |
| [2605.03268](https://arxiv.org/abs/2605.03268v1) | 保持贡献关闭：POSCM研究上下游context共同生成graph/mechanism后的干预识别条件，其新增命题属于因果生成/干预建模本身；题摘没有给出影响模型学习、可用状态表示或闭环控制的具体机制链。不是按理论、retina/gene或科学标签排除；不能仅因可类比world-model把通用因果框架强接owner。 |
| [2605.03313](https://arxiv.org/abs/2605.03313v1) | 准入：有界恶意gradient下不可突破noise/error floor与query complexity可能决定分布式学习能保证什么；须核凸性、smoothness、oracle距离模型与匹配下界，不能等同真实隐私保证。 |
| [2605.03359](https://arxiv.org/abs/2605.03359v1) | 准入：global attention耦合pointmap/voxel生成，以及overlap attention bias向纹理阶段传递一致几何，直接回应生成先验完整但不对齐的失效；须核预训练/训练预算、pose/geometry对应对照。 |
| [2605.03438](https://arxiv.org/abs/2605.03438v1) | 准入：Mamba冻结backbone的token-level PEFT与state-update粒度不匹配，SAA改变控制注入位置、DSCD约束不同serialization的一致性；不是单纯LoRA到点云迁移。需核两模块分离/serialization稳定性。 |
| [2605.03566](https://arxiv.org/abs/2605.03566v1) | 准入：OpenMP loop语义提升到tensor IR，改变已有一般程序映射AIE执行模型的compiler边界，且包含AI kernel；须区分支持的loop类/数据搬运和CPU+NPU energy条件，不因科学负载字样整体关闭。 |
| [2605.03588](https://arxiv.org/abs/2605.03588v1) | 准入并触发实质纠错审阅：symmetric-space生成转到Lie algebra子空间是路径参数化替代；current官方v2 Aug27明确修§4，详见R6，不能直接采用v1任意log投影或geodesic说法。v1标题为Flow Matching on Symmetric Spaces，非current Cartan改题。 |
| [2605.03598](https://arxiv.org/abs/2605.03598v1) | 准入：约束multi-hop路径而非单权重L1可改变recurrent temporal sparsity与实现函数关系；须核resolvent前提、任务horizon与原RNN对照，不外推所有Transformer。 |
| [2605.03601](https://arxiv.org/abs/2605.03601v1) | 准入：function→parameters除了scaling/permutation是否仍隐藏冗余，以及functional dimension/depth hierarchy，直接影响参数量/可辨性解释；摘要实际是每类架构存在open identifiable set，不先把标题Most解释为a.e. generic。 |
| [2605.03820](https://arxiv.org/abs/2605.03820v1) | 准入：conformal predictor进入representation选择/gradient calibration且自更新，形成训练—校准反馈；需核可靠性sensor和覆盖保证分离及校准数据复用，不因为conformal名称默认valid。 |
| [2605.03866](https://arxiv.org/abs/2605.03866v1) | 准入：小replay memory使CLIP contrastive loss失效，DRO class reweighting提出memory与forgetting取舍；需核buffer与训练预算、class/domain协议及不是单纯replay数量提升。 |
| [2605.03877](https://arxiv.org/abs/2605.03877v1) | 准入：条件likelihood与OT distribution matching给出无需再训diffusion/classifier的数据蒸馏路径，改变合成训练集的代价/覆盖取舍；须核“training-free”不等于免费生成、动态diversity引导与下游评价控制。 |
| [2605.04013](https://arxiv.org/abs/2605.04013v1) | 准入：closed-form conditional transport无需神经近似但把成本转到初始化，PT+short-time SDE给出明确替代路径；须核初始化复杂度何时减小、density eval总预算与多模态探索，不外推任意生成模型降本。 |

代表关闭中有一项应改判继续审阅，理由不是凑候选：

- [EDL 2605.03722v1](https://arxiv.org/abs/2605.03722v1)：**改为准入**。本人另实读官方v1完整摘要；不以evolution/chaotic mutation名称认定贡献，真正增量是不用真实meta-training数据、仅synthetic prediction-label pairs，在概率空间预训练可迁移loss。ranking consistency是否足以给proper/calibrated或优化稳定的surrogate正是待审证据，不能因摘要未证明validity而先关。只将“main loss pretraining无real samples”作为潜力边界，不接受全流程distribution-free或无需真实验证的宣传。root需另确认本项日期，当前不冒称落窗。
- [Probability Matrix 2605.03816v1](https://arxiv.org/html/2605.03816v1)：**关闭保持**。针对可能漏掉的负面校准结果，实际定点读§2、§3.1、§4.5：该文明确所有实证来自先前研究，校准损害strong tabular models也写为复确认旧发现；新增是known decomposition/axis的阈值矩阵命名，未形成新的validity或设计修正。其文献标2025但ID为2601.19944，未核早稿真实公开，不把引用年当日期证，也不据此扩审旧研究。关闭不是忽视负面结果。
- [TRACE 2605.03838](https://arxiv.org/abs/2605.03838v1)：关闭；分层reference architecture、validator split、escalation与CPR命名未在题摘给出新的执行语义或可检验保证；三域instantiation不是机制有效性证明。
- [Contextual objectives 2605.03900](https://arxiv.org/abs/2605.03900v1)：关闭；目标路由/硬软约束/多stakeholder纲领列清问题，但implementation pathway未给新的objective inference或conflict resolution机制/反证条件。
- [Intent→Execution 2605.03986](https://arxiv.org/abs/2605.03986v1)：关闭；planner、task graph、registry retriever/reranker与critique的编排是通用模块组合，recall提升尚未给可修改已有执行/委派可靠性判断的机制边界。不是因MAS主题已覆盖而关闭。
- [Experience-RAG 2605.03989](https://arxiv.org/abs/2605.03989v1)：关闭；memory+scene→strategy选取与structured evidence包装未超出adaptive retrieval既有组合，fixed candidate pool排名和skill封装不足以构成新检索/证据状态语义。
- [Agentic redteam 2605.04019](https://arxiv.org/abs/2605.04019v1)：关闭；统一attack/transform/scorer catalog与自然语言workflow并非新攻击或可靠性机制，Scout85%攻击率未附可改变安全判断的matched预算/协议边界，不因大catalog/零人工代码准入。
- [MPI Sessions 2605.03983](https://arxiv.org/abs/2605.03983v1)：题摘确有world communicator解耦与层次扩展机制，但Other明确EuroMPI2025，是具名更早发表线索；不把May06元数据当新首次事件。尚未核正式发表原件，不虚称早发表日期已证；本轮不无差别审MPI或扩查其他年份。

本R5只覆盖这22项：14原潜力中13保潜力/准入、1关闭；8代表项中EDL改准入、6具体关闭、1早期事件线索。两项跨日潜力（R1 KAHM及本批phylogeny）不支持确定当窗计数。root提供本批组合结果仅作路由，不代本人原件独核通过。未重开其他日、未改评分/Report/Books。

## R6 — Cartan/Flow Matching 实质纠错的定点定位

本人实际重开[当前官方abs](https://arxiv.org/abs/2605.03588)，核到v2=`2026-08-27T07:05:49Z`、Other明确major revision/fixed §4。只为定位这一纠错，定点读[v1 §4](https://arxiv.org/html/2605.03588v1)与[v2 §4.1–4.2](https://arxiv.org/html/2605.03588v2)，不比较完整版本史。

v1程序先取group exponential的任意preimage再project到Cartan的p，称去掉k仍保商空间点并对应流形geodesic。v2 Remark4.1明确该投影一般不保原点，改要求编码L满足 `π(exp(L(x)))=x`；并明说p中两点线性插值decode一般不是两端点的manifold geodesic。v2 Grassmann编码增列定向chart/SVD条件，Y1可逆、最大奇异值正且simple，例外零测集也不等于所有点无需处理。故这是采用机制受影响的真实纠错，而非仅改题或版本号。

后续Source仅可在核v2相应证明/评价后采用被修正的encode/Euclidean FM/decode边界；原v1强说法不进入Books。May06归属仍是首次v1事件；Aug27纠正是本次审阅时已知的后续限制，不伪造May06当时已含v2内容，也不另给同家族重复评分。必要完整理论Source仍在继续，此R6不是完整证据通过。

## R7 — ReLU identifiability v1 必要 Source（reader作者层）

材料：[2605.03601v1](https://arxiv.org/html/2605.03601v1)。实际核官方当前abs身份/历史，读§2 realization/quotient/minimality定义、§3.2 Theorems3.12–3.13与sign-cancellation证明、§4 slab/transparency/TPIC构造及Theorems4.10–4.11、§4.12边界，并定点读§5.2 Prop5.23与§5.3 Prop5.24直接反侧。建议评分 **2+1+3=6**，标准之外为长期理论判断加深证明；候选日期复用root组合，不冒称本人第二次独取日期原件。建议唯一owner `WORLDVIEW-WHY-MODELS-LEARN`，实际Books差额尚由root比较。

**可支持的窄命题：** biased fully-connected ReLU、末层affine、输入及每hidden宽≥2时，存在非空open参数集，其全函数纤维仅含层内permutation与neuronwise positive scaling。TPIC/LRA本身不够：§3.13还要求generic masked-product rank，排除最后隐藏层sign flip的不可见取消。§4在bounded polytope上构造slab/transparency、保持可见breakpoint及横截相交，再用扰动稳定性得到open集合；由商空间局部embedding推出architecture功能维数为raw参数数−hidden neuron数，即 `Σ n_l n_(l−1)+n_out`。这是最大可实现函数维数，不是任意训练checkpoint的经验NTK rank或参数恢复算法。

**必要反侧：** title的Most不证明随机初始化/训练后几乎所有参数可辨；width1留为Conjecture，不填补。§5.24 depth hierarchy只排除generic较浅实现，不排除精确degenerate实现。§5.23的minimal但positive-dimensional fiber构造要求前层ReLU像位于非负orthant，原陈述未显式排除单hidden层，L=1时这一证明链需额外说明；未将这个更宽负命题当已独立证明，也不据它推翻§4的独立构造结果。若拟采用该一般负命题，定点需要作者对L=1/全域成立条件的澄清或证明；当前窄采用不依赖它。理论材料无性能评价，hardware/batch/precision/concurrency/SLO不适用；未运行数值实验或验证生产适用。

**状态：** 上述§4窄命题的必要证据已读完，可供root独立复核。不得把本节写成普遍参数唯一性、泛化/优化保证或对非ReLU Transformer直接定理。Books未写，POST未授通过。

## R8 — Cartan/Flow Matching 必要纠错 Source（reader作者层）

R6原件/版本范围复用；本轮继续实际读v2 Appendix A全部Lemma4.2证明、§5/§6 Limitations及Appendix B.1–B.3。建议评分 **3+1+2=6**，实质纠错强制深入受影响内容；建议唯一owner `MULTIMODAL-GENERATIVE-PARADIGMS`。不读无关compact-space分类附录。

**证明边界：** v2以满足 `decode∘L=id` 的截面编码将目标分布pushforward到p；再Euclidean FM，decode后才能恢复原measure。Grassmann的SVD/atan分支通过orientation修正和SO(k)基变换不变性证明right inverse，要求chart非奇异及首singular值正且simple；cut locus可多值，零测例外不等于现实分布无需处理。已完整核Appendix A的正/负det分支与invariance，不采用v1“任意log再投影正确”或“任意p直线decode是manifold geodesic”。

**评价/反侧：** v2 sphere checkerboard仅视觉说明；Grassmann的DW4/LJ13/LJ55为方法proof-of-concept，借分子坐标不是本项目科学应用展开。B.1写MCMC1000 walkers取10000点、burn-in200000；B.2另称训练100000/test10000，规模未完全交代，不据此作预算归因。3层ConcatSquash width512；NLL为p空间、midpoint ODE估计、3 runs，不能拿不同测度下NLL比manifold模型、不能采v1性能领先。v2明确未研究cut-locus不同截面选择的稳定性。hardware、总训练/ODE成本Not Disclosed；serving concurrency/SLO不适用。

**状态：** 修正后的encode/decode与插值边界必要Source已读足，可供root独核；若整合需明示v1首发、v2后续纠正，不把Aug27修订搬成May06新事件或冻结v1错误。仅保生成路径/坐标变换的理论分支，不采普遍生成质量/效率收益；Books比较和POST待root。

## R9 — A组三项采用核心的非作者Source独核

读完ORG_A §6作者记录后，本人重新打开三个exact-v1官方HTML，实际核采用核心及直接反侧，不只凭其完成标签。日期沿R1，评分5/6/6与新增窄命题一致。

- **HyPA：通过，限作者窄命题。** 独读§3.1 Eq6–7、§4 Model Selection、§5/Table1及§6.2：confounder线性化锚定Pt，公式是加λ方向而非保证正交删除；λ用已知confounder/ID验证worst-group AUPRC，非未知shift oracle。Table1五seed确有MIMIC OOD与AUSC反例；probe/sensitivity作者明确不能唯一识别remove/block机制。因此可采用表达力与线性编辑锚点的受限分支，不采因果去混杂或单调扩模型收益。TRAIN-LORA只作建议owner，现有具体覆盖尚未由本节签字。
- **Neural Sensitivity：通过，限固定家族。** 独读§2 Def1–3/Prop1–2、§3 Eq13–17/Theorem1、§4.1/Table1与§5：F只总结固定ψ/P/ν/Σ的局部二阶任务，Σ需正定且stimulus-independent；SPD lift与原PSD不同，certificate保留√k。rank1 trace分离/特征值log界支持该家族命题，不支持全部语义等价。Table1 n256 local对n2000 activation不是完全matched预算，highK仍不超CKA。建议Ch5窄连接通过；未把生物评价作为本项目采用依据。
- **GRPO-TTA：通过，限结构分支；实现mask仍未决。** 独读§3.2–3.4/Eq5–11/Algorithm1、§4.1.3、§4.2及§4.3：topK类别再softmax、cosine alignment+绝对偏差dispersion、β0，奖励不来自gold；episodic每图reset、63crops/RTX3090。文内projector/visual encoder对象未统一，不能授精确实现复现。ImageNet11min→3h40是真实约20倍代价反侧，不采modest-cost；†转录baseline和更多K/λ/steps反降均保留。Ch33可采“group population/代理reward/reset”语义，不采防坍缩保证、持续在线累计或GRPO独立归因。

本R9通过三项**必要Source窄采用**，不意味着精确实现无缺口、Books决定成立或实际写后通过。作者有效完整层复用，未重复重读其全部附件。

## R10 — B首组三项及root三项的非作者核心检查

先读B §7与root SUP §4的原记录，再回到具名exact-v1核心/直接反侧，不凭作者摘要签字；均未检查实际Books写入。

- **BifrostUMI：窄Source通过。** R1已独读§III-C/D的SKR/独立WBC，本轮实读完整§IV–V：确为两个定性场景，没有trials/成功率或SKR对照。可以提出保metric自由度与IK/dynamic tracking分责，不可写已证数据效率、任意本体可达/接触稳定或当前metadata五场景。
- **SigLoMa：窄Source通过。** R1已读§3.2–3.3公式，本轮读§4/Table1与§5.1：sim100 trials×3 evaluation runs不是3 training seeds；实机3任务各10次，Qwen3.5 API初始化mask所以不是全部语义严格onboard。无unweighted PCA单因素消融，NoTCN/EncMLP有反例；作者6h/50Hz不构SLO。可采sampling-measure桥接和低频观测/高频估计分离，不采guaranteed alignment或teleop等效。
- **LDM：窄深入Source通过。** 本人实读§4/Eq4–6、§7/7.1与A.7.1 Gaussian Theorem1/Eq58–64/Remark1的完整证明：injective g、manifold-invertible f、perfect同类Gaussian conditional matching及predictor Jacobian full-row-rank才推latent affine；Σ可随时间但非任意input/state变，predictor内部hidden并未同证。swirl R²=.94是有限实现且未硬约束可逆/coverage，不能反向证明所有前提自然成立。所选Gaussian命题通过，不授vMF扩展或未读全部理论通过；Ch5建议不变。
- **NEC 2605.03135v1：限定Source通过。** 实读§3.2–3.3/Eq1与§4.2：原regret写min reward和正确指示确与错误cost定义冲突，不复制该推导。独立清楚的Eq1只是加权错误率；annotator margin/threshold不是危害真值。10seeds/CI与iNaturalist frozen加权反退支持“评价不等于更好训练目标”，不授临床成本或普适权重收益。
- **Adversarial gradient 2605.03313v1：限定理论Source通过。** 实读§3条件C1/C2、Eq6、§3.2完整Thm2双函数证明及§5：凸L-smooth、known norm R≥1、L≥1、0<ε≤1、距离受界对抗oracle；两函数都容许0 reply故不能统一保证低于εR/2。不是一般噪声或LLM隐私定理。§5 sigmoid-square非一般凸、early-stop关闭的实验不验证算法全保证。只采不可辨识floor，不采其全部算法/预算建议。
- **R-RNN 2605.03598v1：限定Source通过。** 实读§3.1–3.3、§4.4及§6：诊断normalized W、hop2..L+1；训练raw W、hop1..L+1避免靠scale分母取巧；合成16hidden、4modules、10 repeats/200epochs/10β对照，不同于§3.1基础诊断100epochs。signed sums可抵消，所以“sparse effective paths”不等于物理删边或完整nonlinear Jacobian；保留L1参数稀疏原目标与leaky-cascade/horizon/矩阵幂开销。不得推广Transformer因果解释。

以上通过的是明确收窄后命题；root保留的错误公式/凸性、统计与实现限制均不得在报告或Books汇总时消失。理论与实践层分开，尚未Books PRE/POST。

## R11 — A第二组核心/争议与旧事件独核

实际读作者A §7，再开对应官方exact-v1方法、关键对照和直接反侧；不把作者主张当证明，也不因深审出现反证删候选。

- **Mix3R 2605.03359v1：窄Source通过，6分可保。** 独读§3.2–3.4 Eq2–8/12、S2完整与S3：MoT保持modality-specific QKV，低噪时才较强监督geometric alignment，voxel/patch overlap只加非负bias至冻结stage2。S2明确stage1不可逐分支删后保持pipeline，所以没有各分支单因子归因；Toys4K CD在stage2反退、bias-only增益远小camera refinement，SGAT子集更相关。非均匀照明/roll等失配会让pointmap污染prior，Eq12 max=APC处理未明。可采几何对应的condition接口与失配失败分支，不采普遍纹理提升、全pipeline免训或absolute pose保证。
- **CPSC 2605.03820v1：争议隔离成立，不能授中心保证通过。** 独读§3.1 Eq1–3、§3.4 Prop2/Algorithm1及§3.5 Eq16–17：q已通过feature/gradient影响θ，然后仍用同Dcal刷新；原static split-CP的exchangeability不由一次split自动延续，正文未提供adaptive证明。GSC以预测y′打分而CE仍用gold，rank不是正确概率；测试不用RSC。作者提出的凸线性梯度g=0/1、权重w=1/2反例本人复算：Var(g)=.25、Var(wg)=1，满足正相关而非一般降方差；只否定所写条件下普通方差结论，不假装反驳未定义的其它effective variance。新增评分2+2+2=6对应训练闭环本身；7分若借静态CP保证加分不当，纠正不是按工作量降分。维持候选但coverage/必降方差/稳健排序保证暂缓，需adaptive条件/澄清和独立heldout评价才能重开，不能在Books写成已证保护。
- **DMGD 2605.03877v1：争议隔离成立，不能授普遍W1/risk保证通过。** 独读§4.3 Eq11–18、A2.5完整证明及A4.4/Tables5–7：用未平方Euclidean OT但Eq36称K-means算术中心最小化该距离；{0,0,9}中心3距离和12、取0仅9，确直接否定该步。这个反例不直接推翻所有整体W1式或经验算法，不能越界。固定support/mass、greedy冻结旧样本和限时段引导可描述；IPC10 semantic-refinement-only42.0高于full40.8、full-stage IPC50较差是采用边界，不消失。6分对应实际近似/时段设计，不凭错误理论加分。理论采用保持暂缓，重开需一致metric/中心选择及修正证明，best-test与预算范围保留。
- **CLIP memoryDRO 2605.03866：旧事件关闭可保，不评分。** 本人实际重开同一OpenReview forum/PDF遇challenge，未声称直读旧PDF。随后用精确题名恢复[官方作者profile](https://openreview.net/profile?id=~Tianbao_Yang1)及[官方作者结果](https://openreview.net/search?content=authors&group=all&sort=cdate%3Adesc&source=forum&term=~Bobak_J_Mortazavi1)，独核同题同四作者、Published10Oct2024/Modified19Nov2024、AFM2024 Poster、Everyone。作者A已核到旧官方PDF的GCL/GDRO正文，root也复核早事件处置；本层只核具名更早公开与无新重要修订信号的关闭，不冒称本人完整正文diff。搜索返回的ResearchGate/第三方结果没有用于技术证据或首公开证明，不扩做2024任务。

本R11把Mix3R窄通过、CPSC/DMGD中心争议与CLIP旧事件分别处置，不把三个同分候选算成全部Evidence通过。尚未核任何实际Books改动，POST仍独立。

## R12 — root首批五项实际Books POST

非写入者本人读取当前真实保存正文，不以R9/R10的Source通过代写后验收；已读完整新增段和上下相邻论证。仅检查本次具名新增，不重审旧章节全部历史来源。

- **Ch5／WORLDVIEW-REPRESENTATION／03598：通过。** 新段在“从可读出到机制”标题后，完整承接上文correlation/prediction/causation，并交回下方证据阶梯。多跳带符号路径、normalized诊断与raw训练之别、有限合成十次对照、非删边/非完整Jacobian/非Transformer与矩阵幂开销均实际保留；没有以参数稀疏替代功能因果。
- **Ch5／WORLDVIEW-REPRESENTATION／03517：通过。** 新段处于静态mixture可辨性及其条件限制之后、output-interface识别之前。实际包含injective/differentiable观测、流形可逆encoder、非退化Gaussian条件匹配、predictor Jacobian覆盖与精确匹配，再得可逆affine；明确不识别任意内部hidden/输入依赖协方差，有限loss不能倒证假设，代价与失配回退俱在。
- **Ch28／TRAIN-PRETRAINING／03313：修正后通过。** 首次读到的正文遗漏下界构造尺度限制，已向root指出：任意ε>LR时，0点smoothness gap可小于εR/2，故无条件数值下界不成立。随后本人实际重读保存段，现已补入原文R≥1、L≥1、0<ε≤1，与convex/L-smooth、known R和受界有偏oracle共同限定；只采不可区分floor，不采非凸LLM/隐私或全算法保证。上接Optimizer标题/曲率消费者，下接实际step与parameterization，衔接成立。
- **Ch66／PLATFORM-EVALUATION-SYSTEM／03135：通过。** 新段在人口/切片权重之后、污染传感器之前，明确非负代价和非零分母，公式是错误指示而非原regret误式；代价代理≠危害、加权训练不一致改善、权重权限及高危少数检查实际保留，未把评价目标改写成已证学习收益。
- **Ch5／WORLDVIEW-REPRESENTATION／03222：通过。** 本人另读完整新段及两侧“固定测量算子”与线上闭环/诊断成本。局部扰动、坐标、人口、正定且stimulus-independent噪声先固定，再解释投影F和Tr(CF)；明确SPD lift不直接授原PSD或大扰动证书、有限预算未匹配与无法区分反侧，保activation/行为/干预，不是一般语义或能力排名。

五段均实际含正确Source Family marker与exact-v1链接，未以marker本身证明内容；root未增额外过程note，本文也不要求其增一份平行收据。限定上述文件和本SUP的`git diff --check`无报错。本层只签这五个实际POST，不签最终报告、全工作树冻结或日级完成。

## R13 — A首批两项实际Books POST

实际读取Ch30 HyPA和Ch33 GRPO-TTA各完整两段、完整前后邻接及末尾本人Source注，均为非写入者检查。R9的必要Source窄采用范围不扩大。

- **Ch30／TRAIN-LORA／03096：通过。** 前文权重delta组合须重新评价，新段自然切换输入侧prompt更新，再交下文activation组合。任务锚点Pt、一阶confounder方向与送回原非线性模型清楚分责；不是正交投影/因果删除；已知二元标签、ID worst-group选择λ、MIMIC OOD低于线性反侧、probe不可唯一归因和两阶段/序列成本均实际保留。末注评分2+1+2=5、精确版本与未核代码/复现一致。
- **Ch33／TRAIN-GRPO／03403：通过。** 前文无外部答案的密度拟合，新增明确改为有限类别人口，后回普通同prompt采样及跨题条件分支。确定性topK/softmax、代理相似度与绝对偏差、β0、非独立回答采样/非正确性/非防坍缩保证俱在；63crops/单图reset、RTX3090的11min→3h40、mask不唯一及更多K/λ/steps反降没有删掉。末注2+2+2=6、约20倍费用/实现权限和正文一致。

两项正文与末注的marker均唯一配对，没有把Source注变成过程状态；A关于其写前全文件冻结的作者自查不充当本人已独立重算SHA。相关文件限定diff-check通过。仅签当前真实两项POST，后续Mantis/Mix3R未由此预验收。

## R14 — B首组三项真实Books POST与末注收口

本人实际读取Ch4 EDL两段、Ch26 Bifrost一段与SigLoMa两段的完整新增及前后邻接，不仅检索marker；读取三条本人Review notes后，发现其中混入授写/PRE/保存待POST过程句，已请B仅窄删这些句子。B保存后本人再次实际读回三注，确认只剩身份、精确证据、评分、边界及未核实现。正文内容未因此重写。

- **EDL／Ch4／WORLDVIEW-WHY-MODELS-LEARN：通过。** 在loss是业务目标代理之后、相同目标但不同学习过程之前，新增只synthetic loss-shape pretraining阶段移除真实样本，分类器/验证依赖另账。`1-p_y`的risk=`1-q·p`反例正确且明确本书推导，不冒称作者实际loss；CIFAR有限、下游反退、holdout/选择披露不足、全费用与CE回退均保留。必要Source的非作者原证层由root已实际核III/TableII，我不冒称在此又独读整篇。
- **Bifrost／Ch26／MULTIMODAL-EMBODIED-VLA：通过。** 接在retargeting改变目标几何的反侧之后，先竖向有限适配，再显式IK输出root/29joints reference，交独立tracker；后文仍保多指接触约束。两场景/无消融或成功分母、不可达/安全与标定/低层费用实际保留，当前更多场景没有回填v1。
- **SigLoMa／同Ch26 owner：通过。** 坐标归一化之后、learned feature conditioning之前，先说明sim surface与可见pixel采样测度不同，再引weighted PCA，最后区分低频观测/高频预测。无weight单因子消融、轴不稳/遮挡、平面局部/3×10、TCN反退、外部VLM API及全部费用和停机回退均在，未签sim-to-real对齐或执行安全。

三项清理后Review notes与正文权限一致，相关文件限定diff-check无报错。此处三项实际POST通过，不以作者自查或root PRE代替写后核验；本日其它新写未自动通过。

## R15 — root QKVShare实际Books POST

root已反馈其非作者必要原证实读PDF§4.2/§6/§7，接纳R4窄机制；本节本人作为非写入者实际读取Ch55／`INFER-PD-DISAGGREGATION`的完整新段、上方remote-memory受限执行论证与下方完整provisional/committed handoff及其失败回退。

**通过。** 新段在Progressive Verified Handoff标题后，先区分传输payload与接收驻留；Q4→FP16 `past_key_values`、打包/搬运/注入/下一forward分账、重Prefill与原生恢复参照、runtime混杂/n=2、拓扑未证/逐hop质量及兼容metadata均实际保留。它明确只复用handoff原理，不把多Agent原型等同生产PD或native量化attention；故与后文另一家族的低比特provisional verify/correct不混同。费用不划算时完整cache复制/重算退路明确，未复制其未经分离的拓扑性能数字。正确SF03884/exact-v1 PDF链接及限定diff-check均通过；无新增过程note。仅签该真实单段POST。

## R16 — A后两项实际Books POST

本人实际读取当前保存的两段、各完整前后邻接及末尾Source注，不将A的PRE或自读当写后检查；root/B已有必要Source独核层复用，Mix3R原件核心沿R11，不无差别再读全部附件。

- **Mantis／Ch30／TRAIN-LORA／03438：通过。** 前一条件增量是BΦA中间低秩映射，新增再转递推状态算子，后一分支是已有adapter间hard选择，区别清晰。token/上一hidden/order条件与Udiag(u)V作用A/B/C/Δ实际写清，不误称冻结Transformer外adapter；非静态merge、低rank不保范数/稳定、contraction/有界前提、双序列化不授全排列不变，以及分割/S3DIS/GFLOPs反侧和双视图/递推费用俱在。末注6分与仅算子调制的窄命题一致，不授全面超FT或通用5%参数比例。
- **Mix3R／Ch23／MULTIMODAL-REPRESENTATION／03359：通过。** 前一geometry kernel保native位置规则，新增解释重建到生成prior的粗对应/overlap条件，后接混合rig的各投影身份，无新重复owner。高噪减弱几何监督、非负attention bias、估计≠观测/绝对坐标、分支不可独立归因、Toys4K反退、roll/光照/镜面失配及16×A100约一周/推理全费实际保留，不授整流程免训、persistent world state或动作执行。末注6分及精确证据范围一致。

两marker正文/末注配对正确、没有lease/待POST过程句，相关文件和本SUP限定diff-check通过。本轮两项实际POST通过，不代表B随后Ch4/Ch24/Ch49四项已验或整日报已完成。

## R17 — 既定48项内补充三个排除样本

为最终分层复核，实际读本日既定03255/03491/03847完整元数据题摘，未扩池、未请求无关日期。

- **03255：关闭可保。** ADT对话压力下稳定性观察与人类core-belief类比，没有建立新的内部信念机制、行为稳定保证或控制设计；不是因benchmark标签直接关闭。
- **03491：关闭可保。** 完整摘要有PGD下名义ADE相近而鲁棒性不同的负面结果，不忽视反侧；但其实际增量是intersection离线BC/Transformer/GAIL比较框架，未抽离新的状态/训练有效条件或可归因机制，不由一个8m误差数字扩大到一般模型规则。
- **03847：定点core后关闭可保。** 元数据有后版，故没有只据current题摘排除；实际打开[exact-v1 §III–VI/VIII](https://arxiv.org/html/2605.03847v1)，核到weighted hinge violation、最小干预二次项、discounted reward−penalty、joint/pair/global代价相加。三命题分别为正权重非负和零点、compact连续目标存在最小值、精确最优policy随代价权重的取舍；未新增可执行分布式协议或轨迹安全条件，协调协议明确留未来工作。故不是新“conscience”术语即可准入，也未将其笼统安全主张当正面证据。不评分/写Books；不为不影响关闭的日期或后续版本号扩查。

这三个是原明确排除项的新增抽样，不是48/316/432全量题摘或所有关闭结论独立验证。与R1/R5已有样本共同覆盖任务组合、benchmark、框架/术语和负面结果理由，撤回/纠错/旧事件另按已记具名层处理。

合并R1/R5/R17，24个贡献关闭中实际独核14个；其余10个未由reader独立逐题摘：03276/03465/03561/03652/03686/03927/03950/04040/04044/04045。它们由root实际初筛，本文不把分层抽样写成全量关闭复核。

## R18 — 本日六部分独立DAY（修正后通过）

**复核者：** `/root/supp_may07_reader`，非Report作者。**结论：通过，待作者保存完成态后另作FINAL读回。** 实际读取当前Report六部分中的本轮新增/更新全部正文、19新候选行及对应19证据段；旧160有效证据按冻结原件复用，不重做所有历史附件或另开May06/其他日报。

**范围与漏斗：** 检查14每日源及具名触发OpenReview行、机构A/B真实入口/有限停止位、arXiv官方路由失败与本地元数据恢复角色。432/316仅发现/身份线索，没有转成全部题摘/全文队列；48完整题摘归并为19确定候选、2跨日潜力、1撤回、2早期事件线索、24贡献关闭。全部拟入选、撤回、纠错与具名争议均已分批复核，贡献关闭抽核14/24且余10名单在R17；机构代表原证与Hunyuan分页实际抽核沿R2/R3，不声称所有HTTP/全部机构正文本人重取。

**日期、证据与Books：** R1本人原件/组合与root/B其余具名原字段及共同规则相容，跨日两项仍不计确定候选；早期CLIP/MPI与HeadQ撤回没有新评分/采用。19新增＝17受限机制实际整合至11唯一owner＋2中心保证争议；自身作者的QKV/ReLU/Cartan已由root实际独核，其余必要Source按R9–R11及root独核B组层复用。17真实Books POST中13项由本人R12–R16执行，4项由非写入者root实际读新增/完整两侧/末注并保存SUP§6；不把作者自查当POST。root后来六条来源注本人已逐条读回，来源、分数和权限与正文一致。

**本次修复与读回：** 03313下界遗漏尺度已在R12真实修复；本轮DAY发现新表被说明段打断，作者已把原160与19新行合成同一连续表，读回确认一个181行含表头表格。LDM Report与新来源注的泛称variable covariance已改为随输入/状态变化，不误排时间依赖Σ。实际触发的SRC-OPENREVIEW已补一行，限定同题同作者旧正文恢复、直链challenge与未完整diff，不扩扫2024。SUP已补EDL实际日证并把旧停点标为历史，当前汇总不再把普通Source/Books待办误留。

**隔离及完成边界：** CPSC/DMGD不授正面Evidence/Books；KAHM/phylogeny跨日、Meta/Google Research/arXiv历史缺段及原四争议/NLA/ColaDLM均有身份、不可采用理由与定点重开条件，不据其声称全覆盖、零发布或无遗漏。完整阅读与当前可执行项已结束；仅余作者把Report头/§5/§6与检查时间保存为完成，再由本人FINAL核状态，未提前增加日级计数。

**独立机械结果：** 基线SHA256仍为`a660e3f0d2e3376f2ca354a88388435fbf93208aeb02a6418286be66570a7f2a`；160原表行逐字相等，连续原§4整块存在；179行、17新整合/2新争议、11新owner，六部分各一次；当前207本地引用零缺失、fence0。本人实际运行V3校验通过，相关Report/本SUP/新注文件限定unstaged及cached diff-check均无报错。机器结果不代语义复核，不签完整工作树冻结或实现/复现/生产能力；未stage/commit/push。

## R19 — 保存完成态FINAL（通过）

本人实际读回当前已保存Report头、§1、完整§5与§6：状态`完成`，检查时间`2026-10-18T02:37:45+08:00`；本轮19＝17实际整合/2中心争议、总179、11新owner与普通待办0相符。复核首结论`通过`，明确R18/本R19与原160历史复核的边界；跨日、历史来源缺段、旧隔离和两争议重开条件完整保留，没有以完成态授全Coverage、正面Evidence或Books保证。

完成态新加R18/root汇总两链接后，实际本地引用由207变209；发现正文计数未同步，已请root仅改此数，本人实际读回§6现为**209本地引用**，零缺失。最终V3、179表行/160原行逐字冻结/连续原§4，以及限定cached/unstaged diff-check均再次通过；原窗口测试41/42限制仍明示，没有声称全套回归全绿。除这处计数外，R18采用及隔离命题没有扩张，不重扩Source/其它日期。

**FINAL通过。** 本日reader停写并释放本日唯一SUP的在途ownership，供root消费结果并按实际验收同步日级计数；本agent未写Books/Report/LS/index，未stage/commit/push，不承接或启动May08/Live/Weekly/2025。
