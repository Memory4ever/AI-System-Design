# 第二十三包：分支工作集、教程双消费者与可执行未来

完整PRE/具体NC，未SAVE。Books/ROADMAP有效；actual Ch75多图manager/worker完整两段、MMSkills临时branch完整段与结构改写完整下段、压缩损失/Markovian两段、原文事实/summary DAG完整两段及commit完整链已读；Ch77 Index/Resolution完整段、按时间snapshot/procedural完整段和概念抽象完整段均读；Ch79经验分层完整段、GUIDE完整两段/下方prior估计器完整段均读；Ch25三channel完整链、均值future完整段/外部双流两完整段、可执行program完整两段/视觉抽象完整下段与Pinductor完整段均读。邻章交接沿本日有效实际层复用。必要只消费R17/R30/R35，四I各唯一owner/四独立gap，一具体NC，不第二Methods/实现/复现。

## 11967 Context-Folding / 2+2+2=6 / AGENT-CONTEXT Ch75

R35 §2.2–2.3/3.1–3.3/4.1/4.3/4.5.2–3必要有效。MMSkills是局部参考咨询、summary DAG是历史派生视图，没有**同一agent共享prefix进入可丢弃branch，return后KV回滚只留摘要的读路径**。插完整MMSkills SF2605-13527 inline段后、完整结构适配段前。FoldGRPO训练机制留报告，不跨Ch33再写一份。

正文：

临时工作还可以沿同一agent的prefix分叉，而不另开一份完整角色历史：branch共享进入前的上下文，在局部展开工具与推理，return时只把摘要接回主路径，并将私有KV回滚到分叉边界。[受限上下文折叠分支](https://arxiv.org/html/2510.11967v1#S3)将长期可见状态与局部计算分开，不等于并行多agent、任意嵌套或已撤销外部动作。分叉revision、原轨迹/工具结果、返回摘要及KV位置须共同保存；摘要可能丢依赖，scope judge只检查给定prompt与return也不认证全部trace正确。训练完整trajectory与压缩奖励仍支付私有生成，峰值窗口与理论累计预算不是已省总tokens；工具调用还可明显增加，训练只计main rollout的时间不代全流程。跨分支事实冲突、摘要不足或费用失配时，回读私有原记录、扩大返回支持或保完整单路径，不由KV回滚、较短主窗口和更长可生成轨迹批准执行撤销、事实保持与净加速。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-11967 -->`

本人末注：

- `SF-2025-ARXIV-2510-11967` — Herschel，Daily2025-10-16补Oct15；消费Cicero R35 exact-v1 §2.2–2.3/3.1–3.3/4.1/4.3/4.5.2–3首次必要，2+2+2=6，仅shared-prefix branch/return摘要/KV回滚消费差额深入。保主支交替非nested/parallel、FoldGRPO全轨迹/penalty与prompt-return judge非全trace、32K×10峰值/累计分账、工具96.5对49.5及main-only训练time/全费，不授执行撤销/充分摘要或净速。未第二Methods/代码/复现；PRE/SAVE/fullselfread/solePOST只本日canonical实际层。

## 11892 R-WoM / 2+2+2=6 / AGENT-PLANNING Ch79

R17 §3.1–3.4/4.2/Alg1/5.2–5.4有效。当前GUIDE分别供planning/grounding知识，不承担**同教程同时条件化模拟nextstate与reward评价，然后只执行首action再真观测**。插完整GUIDE第二段/inline SF2603-26266后、prior估计器完整段前，WorldModel本体不复制。

正文：

教程还可以同时进入候选模拟与候选评分，而不只给planner建议步骤：用检索到的操作知识条件化短程next-state预测，再用同一参考评价计划，由一次较长推理展开并比较多个候选，最后仅执行第一action、重新读取真实环境。[受限教程规划分支](https://arxiv.org/html/2510.11892v1#S3)把参考、想象和执行分开；同一教程同时支持状态和reward，可能形成自洽共错，不是两份独立验证。Oracle教程与实际retrieval是不同权限，next-state二选一、教程judge一致和真实任务成功亦是三种评价，不能互代。教程/软件revision、检索支持、候选与horizon、judge及实际action/observation须共同保存；较长horizon收益减弱说明更多想象并非免费。全部教程制备/检索、候选tokens、模拟/评分和真实执行均付费；版本、预测或净质量失配时，缩短horizon，保原界面、直接行动/固定教程与独立结果核验，不由模型内grounded名称批准真实未来、全局最优和安全执行。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-11892 -->`

本人末注：

- `SF-2025-ARXIV-2510-11892` — Herschel，Daily2025-10-16补Oct15；消费Cicero R17 exact-v1 §3.1–3.4/4.2/Alg1/5.2–5.4首次必要，2+2+2=6，仅教程同时条件化simulate/reward、候选排序后首action真观测差额深入。保二选一next-state/教程judge/真实成功三协议、oracle非retrieval、horizon3后减益与全部教程/候选/rerank费，不授无界可靠rollout。未第二Methods/代码/复现；PRE/SAVE/fullselfread/solePOST只本日canonical实际层。

## 12088 OneLife / 2+2+2=6 / MULTIMODAL-WORLD-MODELS Ch25

R35 §3.1–3.5/4/5.1–5.3首次必要有效。当前history replay完整program/Pinductor候选belief没有**已有object observable下以precondition激活部分program laws、逐observable只融合有预测的active laws**。插可执行world hypothesis第二完整风险段后、完整视觉状态图段前。只程序预测/组合支持，不采从raw发现ontology、未闭条件独立概率recipe。

正文：

程序假设也可以按当前对象状态局部激活，而不要求一份完整transition程序覆盖所有情境：先声明可观察量与提取器，用precondition选择当前可用laws；对每个observable，只让真正给出预测的active laws参与，再拟合它们的组合权重。[受限程序定律分支](https://arxiv.org/html/2510.12088v1#S3)把schema、适用条件、预测支持与组合分开，不是从原始像素自主发现本体，也不使可执行law成为世界真理。缺失预测不该被默补成完整覆盖，law之间条件独立及乘积/score口径未闭时，不能据此发布校准概率或通用融合配方。应共同保存对象/observable定义、extractor、law来源、激活集合与权重，分别验预测、fidelity和真实决策；预设候选plan的排名改善仍可伴较低fidelity，不授开放自主规划。环境实现、LLM prior/程序搜索、拟合、全部rollout与独立结果回归都付费；支持、提取或净质量失配时，保显式可信模型、较宽Unknown与真实观测下短程重规划，不由可读规则、较高rank批准完整动力学或物理安全。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12088 -->`

本人末注：

- `SF-2025-ARXIV-2510-12088` — Herschel，Daily2025-10-16补Oct15；消费Cicero R35 exact-v1 §3.1–3.5/4/5.1–5.3首次必要，2+2+2=6，仅precondition激活laws/逐observable有支持组合与权重差额深入。保已给objectstate/extractor、条件独立/Eq1乘积/Eq4phi-logscore未闭、23scripted/8mutators/10trial、rank增伴fidelity可退及全部先验/环境/搜索费，不授raw本体发现或通用规划。未第二Methods/代码/复现；PRE/SAVE/fullselfread/solePOST只本日canonical实际层。

## 12777 FPT / 2+2+2=6 / MULTIMODAL-WORLD-MODELS Ch25

R30 §3.1–3.3/4.1–4.2/T1必要有效。当前均值future/mode-average与双流条件接口没有**poke/query条件的点运动GMM边缘输出，coherent joint样本仍需AR回灌**。插完整1X均值future SF2510-07092 inline段后、外部环境/主体双流完整段前。只运动条件/联合消费，不采真实力干预或uncertainty完整校准。

正文：

未来运动也可以先以分布而非单点交付：用poke条件与点query读取视频表示，输出带完整协方差的混合分布；各query不互读时可并行取得各自边缘预测，但要生成相容的联合样本，仍需把已采点回灌、按序条件化。[受限点运动分支](https://arxiv.org/html/2510.12777v1#S3)因此分开边缘并行、联合采样与均值轨迹；逐点取均值可能混合互斥模式，不能直接当可执行未来。Poke来自视频轨迹/相机静态等proxy时不是真实力干预，uncertainty与误差相关也不构成全域概率校准。视频/track、条件与query位置、GMM/采样顺序及后续消费者须共同保存，局部小poke任务仍可弱于专用方法。图像encoder联合训练、轨迹制备、混合读出、联合采样与闭环回归均付费，单query延迟/并行吞吐不代整规划SLO。条件支持、跨点一致或预算失配时，保逐分支不确定性、可信tracker/真实观测与较短预测，不由高斯协方差、并行边缘或低EPE批准因果物理、完整joint与安全行动。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12777 -->`

本人末注：

- `SF-2025-ARXIV-2510-12777` — Herschel，Daily2025-10-16补Oct15；消费Cicero R30 exact-v1 §3.1–3.3/4.1–4.2/T1首次必要，2+2+2=6，仅poke/query GMM边缘并行与coherent joint AR回灌差额深入。保video-track/static-camera proxy非真实force、mean可mode-average、uncertainty/EPE非全校准、小poke反退、3.8M/220M/2H200七日与另5M/8H200一日分设及全费，不授闭环SLO。未第二Methods/代码/复现；PRE/SAVE/fullselfread/solePOST只本日canonical实际层。

## 11838 Lingxi / 2+2+2=6 / AGENT-MEMORY Ch77具体NC

R35 §4.1–4.3/5.2–5.5/6.2/7.1–7.3有效必要。只采用旧issue/patch/snapshot派生知识→抽象/检索→当前修复的资格边界，不把知识图/多analysis组合本身当独立新长期链。重构rationale非真实开发因果，issue created早于target不保证patch当时可得，218subset与500主表不同、去knowledge也改信息量/搜索，15/20已有相关知识仍忽略；79.2%三patch oracle非部署选择器，API/历史制备/检索/多agent全费保留。

actual Ch77 SF2601-06789完整Index/Resolution段将初始症状与历史RootCause/Fix/Patch分开，要求回指Issue–PR–Patch及当前tests，不授检索命中即修复；时间snapshot/procedural完整段明确future commit泄漏、accepted非正确真值、base/env/tests/oraclediff/extractor/future split身份；SF2509-04439完整概念抽象段明确事后解释非当时推理、类型/组合只提案及原轨迹回读。这三实际论证承担本次具体采用，不说书内算法等于Lingxi knowledge graph，拟NC，不写正文/marker/注。

请sole reader整体审四完整原稿/独立marker/本人注及Lingxi具体NC，未SAVE/不预POST/日级。范围仍本日，普通工作继续。
