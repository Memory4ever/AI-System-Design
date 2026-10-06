# Nov17 First Calibration Ready

作者：Carver。首批准备时钟：2026-10-04T19:31:03+08:00。以下首批停点保留当时状态；最新root独立结论及作者完成同步见末节，不能把历史待核描述当作当前普通待办。

窗口BJT `[2025-11-16 09:00,2025-11-17 09:00)`，UTC `[2025-11-16 01:00Z,2025-11-17 01:00Z)`。首次公开未核材料不列确定当窗候选，不评分，不展开全实验/owner。已实际读取下列exact-v1完整题摘、submission history、DataCite所有日期字段；对应原HTML/JSON和receipt均在本目录。没有声称方法、证明、实验或实现已审。

## 首批潜在准入

| 材料 / 原始证据 | 原文具体增量与准入边界 | 原日期字段与待核 |
| --- | --- | --- |
| [Equivalence Checking of ML GPU Kernels](https://arxiv.org/abs/2511.12638v1) / [完整题摘](abs-2511.12638v1.html) / [日期](datacite-2511.12638.json) | aggressive/LLM生成kernel缺形式保证→VOLTA为特定类GPU程序给soundness及completeness，覆盖matmul/attention→需重新考虑正确性验收；不能从AB授任意kernel/浮点/生产保证。 | Submitted v1 `2025-11-16T15:09:14Z`；Updated v1 `2025-11-18T02:04:28Z`；Available v1 `2025-11`；created `2025-11-18T04:29:24.000Z`。均不等于首公开；hold。 |
| [FarSkip-Collective](https://arxiv.org/abs/2511.11505v1) / [完整题摘](abs-2511.11505v1.html) / [日期](datacite-2511.11505.json) | MoE阻塞通信受计算依赖约束→修改skip连接并self-distillation恢复能力，显式实现compute/communication overlap→不只调collective，而是模型依赖图与执行共同设计。16B–109B/平均accuracy约1%以内是作者AB主张，未核质量协议或E2E成本；不等于所有MoE无损替换。 | Submitted v1 `2025-11-14T17:25:14Z`；Updated v1 `2025-11-17T01:58:44Z`；Available v1 `2025-11`；created `2025-11-17T02:55:30.000Z`。v2/v3是后续版本，不用当前API摘要替代v1；hold。 |
| [Optimal Self-Consistency](https://arxiv.org/abs/2511.12309v1) / [完整题摘](abs-2511.12309v1.html) / [日期](datacite-2511.12309.json) | 固定SC多采样成本→mode estimation/voting理论与跨问题动态样本分配Blend-ASC→预算内如何分配推理样本；6.8x为作者AB平均样本数字，不授延迟同幅下降或无条件理论等价。 | Submitted v1 `2025-11-15T17:45:42Z`；Updated v1 `2025-11-18T01:42:38Z`；Available v1 `2025-11`；created `2025-11-18T04:21:47.000Z`。hold；v2未采用。 |
| [TopoPerception](https://arxiv.org/abs/2511.11831v1) / [完整题摘](abs-2511.11831v1.html) / [日期](datacite-2511.11831.json) | 语义丰富评价可能有局部捷径→用全局拓扑不变量隔离global visual perception，并报告强推理同族模型更差→评价盲区及规模不保证该知觉能力的直接负侧，不因新benchmark自动收，也不因通用evaluation已存在关闭；是否真shortcut-free须核心与反侧。 | Submitted v1 `2025-11-14T19:45:56Z`；Updated v1 `2025-11-18T01:07:32Z`；Available v1 `2025-11`；created `2025-11-18T04:10:34.000Z`。hold。 |
| [The 'Sure' Trap](https://arxiv.org/abs/2511.12414v1) / [完整题摘](abs-2511.12414v1.html) / [日期](datacite-2511.12414.json) | 显式恶意标签不是后门必要条件→纯benign-label且只回答Sure的少量投毒，部分模型unsafe续写；更强aligned模型只给compliance token→数据供应链与行为gate反侧，不能授确定性tool控制/溯源认证；这是AB提出的延伸，不是已证实的通用机制。 | Submitted v1 `2025-11-16T02:01:58Z`；Updated v1 `2025-11-18T01:49:56Z`；Available v1 `2025-11`；created `2025-11-18T04:24:14.000Z`。hold。 |

## 代表性关闭

[AI as a component in the action research tradition of learning-by-doing](https://arxiv.org/abs/2511.11445v1)：[完整题摘](abs-2511.11445v1.html)实际是数学/信息教育传统、师生对话与数字工具增智，不提供大模型训练/推理/Agent执行机制或可改变该主线的评价反证。仅教育场景使用LLM不足以准入；不因为非LLM标题/低分关闭。日期Submitted `2025-11-14T16:14:57Z`与Updated `2025-11-17T01:54:24Z`不是public，此排除不依赖日期，不另追日期。

## 入口范围 / 可执行停点

本日4个窄主题API查询，具体表达/URL/start/max_results及执行时钟在`arxiv-*-page*.xml.receipt.json`：model52（start0/50各返回50/2）、systems16、agents3、multimodal26；submitted Nov14–16仅恢复线索，不是当窗公开筛选。初页95返回90唯一，尾页2尚待全体归并及其必要AB。cs.DC宽月表只读首50标题作入口定位，不转全部338条AB/全文队列；首50结束2511.05915明显在早月身份段，待有限目标附近标题定位补检，不用ID补造时刻。

普通可做：其余来源本日真实原目录/有界翻页停止；窄集合先范围后完整AB；首公开具名最小恢复；报告同步。非作者请核5项potential理由/两负侧与1项范围关闭、日期隔离是否准确。首批校准可以先行，不需等全日；作者继续未受影响普通工作。

实际外部问题：Google pubs/Meta原入口本日curl28超时；Hunyuan动态页本日有限browser超时后API只给2026目录；Qwen新Blog/MiMo undated Blog/ZAI历史不足/Agent Tech历史不足待本日有限官方补检，现阶段尚不能都称终态。14源均已实际首查；取回HTTP200不等coverage。

## Root独立校准反馈（2026-10-04T20:21:56+08:00接收）

root已实际读31份完整AB，不是84全核。首5potential与教育代表关闭的增量边界通过；CALM的通用additive semi-structured forward、HEDGE通用VLM uncertainty条件可以保留potential，不因医疗实验自动关闭，且不采临床结论。OPFormer题摘目前是既有foundation特征用于6D pose/BOP和新领域module，未明确通用multimodal形成/动作/可靠性改变；作者仅定点获取core消歧，不借owner自动映射。

FlashFusion/Markov/GNN Dragonfly/ASA/ECCENTRIC/LaoBench/Promptvalues/OpenUS分层AB关闭由root实际抽检后保持；11993有安全信号但无本scope切片，已把关闭依据补明为核到完整AB，不称核心/全文安全审阅。尚未给日级/Books通过，不为未证窗内者展开全66实验/owner。

root所列11项安全/反证核心已定点取回，必要原文位置见[ROOT_CORE_MAP](ROOT_CORE_MAP.md)；材料可读不代表独立Evidence已过，实际复核由root进行，作者不重做抽检。

## Root独立核心反馈（2026-10-04后续实际复核）

root实际核AFM§4–5：单短/中run、baseline不同temperature/无预算对齐、AB66%对stateless不是replay、无human eval/ablation，external API与inline无外调用描述矛盾均保留。WhiteBear为logprob/single English token而非真实完整生成；GPTOSS反例和mechanistic§4与future limitation的张力保留。

root实际核OPFormer§3.1+B的pose依赖、domain检测/模板failure，支持范围关闭，不建立通用owner；现65potential/19关闭，原日期66核对结果不改写。SGuard§4–5 EN/Korean/8k/newattack limitations、ToxSearch10run/fixed100/quantized moderation proxy、AttackVLA§4.1实体平台与三ASR指标、TIM filtered high-risk top10而非全局55%等实际通过**最小隔离边界**；未正面采用，不授全附件/日级。

root另请求SureTrap2511.12414（首5安全）及直接设计反证2511.11612/12635的exact-v1必要core；作者仅定点取回这三项，不重做已有12 core审阅或全66实验。日级仍待root实际结论。

## Root独立日级通过与作者同步

root实际2026-10-04T20:33:51+08:00通过，原记录见[ROOT_INDEPENDENT_REVIEW](ROOT_INDEPENDENT_REVIEW.md)。作者2026-10-04T20:43:00+08:00同步：105发现身份、84作者exact-v1完整AB、21标题关闭；65potential、19贡献/范围关闭（18AB+1 OPFormer必要core）；确定当窗候选0、正面Evidence0、Books No Change/写入0、普通待办0。

独立实际范围是31完整AB、14必要安全/设计反侧核心、另OPFormer §3.1/§3.2.2/Appendix B消歧、14有限来源、65项日期类型/值及六部分；分层关闭抽样10原AB及4标题。不是84全AB、全部methods/附件、原18关闭全核或21标题全AB。新增SureTrap/11612/12635必要段已实际核；[CORE_MAP](ROOT_CORE_MAP.md)原失败/部分HTML权限不抹去。65首公开hold与7来源历史限制已终态隔离，不用于正面Evidence、Books、Coverage/无遗漏或性能/安全保证，只按[DATE](DATE_REVIEW.md)/[SOURCE](SOURCE_REVIEW.md)精确重开。18已fresh独立准备，不继承17响应或候选。
