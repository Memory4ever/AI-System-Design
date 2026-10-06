# 03-04 增量来源补查（作者 supplement_20260304）

执行时间：2026-10-09T04:12:00+08:00。补充窗口：2026-03-03完整自然日。依用户授权原16行、日期/评分、原09:00窗口与连续§4冻结，运行前原文为SUP_BASELINE_20261009.md。旧Submitted/Registered/公告时刻推导仅是冻结历史，不授新增公开日期；本轮只核官方公开日期，不索要时分秒。未改Books/LS/索引，未stage/commit/push。

## 来源入口、实际查询与停止

实际原件与错误均在SUP_FETCH_official/recovery/arxiv/dates/core/gemini.json。首次urllib部分SSL失败后一次curl/官方web恢复，错误不作零命中。所有入口只作本日模型/训练/推理/多模态/Agent主题检查，未加载Weekly源。

- OPENAI：SUP_OPENAI.raw官方RSS逐条日期过滤Mar03，只有GPT5.3 release/card两项，与冻结同事件；官方安全HTML明确PublishedMar2，归属Mar2并去重复用[03-03报告](../../03/README.md)实际Source、Ch66窄整合与非writer POST。RSS/PDF的March3不覆盖官方公开日，不新增card日期缺口，不索要时区/首发时刻；原候选、§4与旧gap正文仅冻结保留。
- ANTHROPIC：SUP_ANTHROPIC.raw Publications嵌入目录实际可读Feb25→Mar05相邻，没有Mar03行；仅当前可见历史段。
- GOOGLE：官方web实际Blog首页July→October2026，page3原入口curl35失败；Google pubs首页1–15/11600及2026年396只有year，不授day。日主题补检 `site:deepmind.google "March 3, 2026"` / `site:research.google "March 3" "2026" language model`无有效新标题，搜索阴性不授目录全覆盖。Gemini必要原文已在SUP_GEMINI.raw及SUP_GEMINI_CARD_WEB.json保存，公开日March3确定。
- META：Research官方web0行，curl35，日级 `site:ai.meta.com "March 3" "2026"` 无可用原始新信号；本窗历史Research必要段缺失隔离。
- QWEN：SUP_QWEN.raw旧Blog重定向qwen.ai，旧目录停2025-09-23；`site:qwen.ai "2026-03-03"`有限补检无有效新标题，不授新Blog历史全覆盖。QwenCode v0.11.1/PR2021是原16内同事件，复用有效Source/POST。
- DEEPSEEK：SUP_DEEPSEEK.raw首页Research导航非历史目录；SUP_DEEPSEEK_UPDATES.raw ChangeLog完整当前页，2025-12-01→2026-04-24邻接无March3；Research/隐藏News历史段缺失仍隔离。
- MOONSHOT：SUP_KIMI.raw实际Research19项，Apr20→Feb09跨日，读到2024-06-26底部，无可见未完分页。不证明删除历史。
- HUNYUAN：SUP_HUNYUAN.raw是空壳，按已知官方页面调用实际POST publicList pageNum1/pageSize20/renderType0。SUP_HUNYUAN_ZH.raw带accept-language zh为11/11；SUP_HUNYUAN_ALL.raw默认英文为9/9。实际displayDate Feb13→Apr23邻接均无March3；display与后台published不是相同首发语义。中文目录不是由英文9推定。
- ZAI：SUP_ZAI.raw Research当前可见15条到Dec09，Feb21→Mar15跨日，查看更多未再扩大；当前段已查，不称被删除历史完整。
- SEED：SUP_SEED.raw首20/242、page1of13止May14；SUP_SEED_P3.raw page=3仍返回同首20，不授真实第3页已读；SUP_SEED_BLOG.raw为空壳。`site:seed.bytedance.com "2026" "March 3"`有限补检无有效新标题，缺March3历史论文/Blog段。
- ERNIE：SUP_ERNIE.raw Blog当前10条、page1of2，Apr15→Feb06相邻，March3未见；下一页为更早2025历史段，不扩扫。
- MIMO：SUP_MIMO.raw Paper8项Mar13→Feb03相邻；Blog15条无日期/More停止，未能授March3历史Blog完整。
- MINIMAX：SUP_MINIMAX_EN/CN.raw两完整当前目录，Mar18→Feb14跨日、读到2025-10-27；没有March3可见条目，不扩AgentTech全站。
- ARXIV：SUP_API_MODEL/SYSTEM/AGENT/MULTI.raw是有限发现而不是日期权限。SubmittedDate[202603020000 TO 202603032359]只用来发现，四主题分别是模型/Transformer/MoE/RL；GPU/inference/kernel/parallel；Agent/memory/retrieval/tool；multimodal/world-model/VLA/diffusion，在相应分类组合限定。start0/max100/ascending：total232/73/242/164，各返回100/73/100/100，均在首批止；没有将超出首批的条目称为已读，也不追所有宽分类库存。相关标题补检为SUP_DATE_LIST_CL/DC.raw各首100，CL至01875，DC至11571，只看相关标题，不把所有月份项变成题摘队列。CL2138/DC346库存不能证明March3公开日。2603式月列表show2000两次超时后一次恢复2026-03/show100成功，只有月级没有日级公告；不重复advanced表单、不用catchup。

## 新题摘及准入裁决

新增实际完整题摘34家族：20个具名Atom题摘，加12个exact-v1中2重复（01915/02298），再加标题补检4个exact-v1。API已是v1的采用其完整题摘，版本大于v1者已实际打开SUP_ABS_<ID>.raw；00364的abs/API污染题摘未采，一次exact-v1 HTML身份恢复后读取正确题摘。root实际独核全部31个潜力家族完整题摘（含尾批15个exact-v1及00364正确HTML题摘）与3个明确EX，并核Power/CoVe决定准入core；不是294宽发现全量题摘复核。没有将摘要读完称Evidence或Books完成。

下列31项有具体潜在主线贡献，但一次有界恢复仍不能确认first-public落入March3。它们不评分、不计确定新增候选、不进入Books，不为日期缺口继续全文。共同且唯一材料请求：每个下列exact-v1的官方首次公开日列表/公告记录，或作者/项目首次公开原稿的日期记录；只须日级，若明确窗外则路由真实日期，若落日则重开该项必要审阅。原API Submitted/Updated和month ID不替代该材料。

| exact-v1 ID | 潜在命题及采用边界 | 题摘原件 |
| --- | --- | --- |
| 2603.01376 | 三块ADMM+transformer级联合稀疏/低秩校准；不采摘要收敛/倍率 | SUP_API_MODEL.raw |
| 2603.01425 | Explicit/latent中间轨迹对齐以避retrieval前AR CoT；不授零latency代价 | SUP_API_MODEL.raw |
| 2603.01502 | 语音temporal冗余与输入统计校准可伤害的反侧；不授唯一因果 | SUP_API_MODEL.raw |
| 2603.01550 | 任务bot dialogue-label extraction的sampling/membership适配；不授全部训练恢复 | SUP_API_MODEL.raw |
| 2603.01553 | delay下joint state-action inpainting作为augmentation/dynamics-belief替代分支；不泛推全部RL | SUP_API_MODEL.raw |
| 2603.01697 | 动态token专家数与layer容量的任务/规模依赖；不因小模型或分类实验关闭 | SUP_API_MODEL.raw |
| 2603.01714 | 同任务多trial quotient topology筛SFT/RL；不授最大gradient-SNR宣传 | SUP_API_MODEL.raw |
| 2603.01792 | token熵与不对称LoRA参数隔离的忘却/保留分支；不授95%forget普遍保证 | SUP_API_MODEL.raw |
| 2603.01907 | Bayesian success belief将difficulty/evidence量分账；不授general样本最优 | SUP_API_MODEL.raw |
| 2603.02092 | Adam问题先固定与超参后固定的量词差异/收敛区；理论假设待必要审阅 | SUP_API_MODEL.raw |
| 2603.02146 | outcome-only grounding梯度稀疏及context reward；不授所有long-context统一必要性 | SUP_API_MODEL.raw |
| 2603.02057 | GPU-LLM受控注故障中metric/trace/multisource RCA不迁移；不授所有部署失效 | SUP_API_SYSTEM.raw |
| 2603.01915 | dtANS压缩/并行解码与SpMVM联合节省带宽；只保算法潜力，不授SuiteSparse到LLM收益 | SUP_ABS_01915.raw |
| 2603.02298 | hierarchical tensor/thread layout algebra的静态推导/验证；不把生产库声望计贡献 | SUP_ABS_02298.raw |
| 2603.01940 | groundtruth ID fuzzification保唯一映射、按outcome接受等价tool paths；§4.2–4.4决定准入core已读，未读全文绕过日期 | SUP_API_AGENT.raw；SUP_CORE_COVE.raw |
| 2603.01469 | mean-flow one-step action generation改变采样约束；不采速度倍率 | SUP_API_MULTI.raw |
| 2603.01490 | attention/action RoI联合修正visual input的training-free分支；额外调用与错误反馈待核 | SUP_API_MULTI.raw |
| 2603.01331 | frozen dLLM跨denoise memory slots+Mixer/Updater/Injector；不授全部再计算消除 | SUP_ABS_01331.raw |
| 2603.01501 | stale-aligned梯度方向与projection的async RL稳定分支；理论bounded-staleness待核 | SUP_ABS_01501.raw |
| 2603.01563 | discrete velocity contrastive更新绕likelihood代理；precise gradient声明待核 | SUP_ABS_01563.raw |
| 2603.01683 | on-policy微编辑与DPO隐式正则/decoupled BCE的保留分支；不采时间/分数 | SUP_ABS_01683.raw |
| 2603.01549 | training-only 3D point-track辅助监督inject VLA表示；不授inference世界预测 | SUP_ABS_01549.raw |
| 2603.01581 | kinematic Kalman补speculative action错误/调threshold；不授原target分布保持 | SUP_ABS_01581.raw |
| 2603.01766 | 连续action function/spectral modulation及velocity/accel/jerk监督；不授所有controller稳定 | SUP_ABS_01766.raw |
| 2603.01953 | action chunk前以观测动态闭环修正，非全部开放世界安全 | SUP_ABS_01953.raw |
| 2603.02083 | flow-VLA stepwise negative guidance绕critic/likelihood；OOD收益不授一般最优 | SUP_ABS_02083.raw |
| 2603.01661 | SoC shape/accelerator-affinity/bandwidth contention联合RAG调度；不采E2E倍率 | SUP_ABS_01661.raw |
| 2603.01399 | verify阶段quantization改变speculation带宽/接受率；精确分布与质量合同待核 | SUP_ABS_01399.raw |
| 2603.01426 | KV retention/accessibility/utilization分开与compression cliff反侧；不采90%普遍阈值 | SUP_ABS_01426.raw |
| 2603.01423 | single/multiturn配对测全局约束/tool intents/entity revision退化；不授独立模型因果 | SUP_ABS_01423.raw |
| 2603.00364 | DACQ CDF/logistic非uniform companding降低weight误差却损PPL/任务的outlier反侧；不采错误MTP摘要 | SUP_ID_HTML_00364.raw首Abstract |

三项贡献前关闭不评分：02145 Linux kernel ML库只是通用configuration的kernel/user proxy PoC，没有模型训练或LLM Serving的新条件；01629 TeraPool是通用共享L1物理cluster/kernelbenchmark，无LLM直接条件，不能借memory类比建立贡献；02019 Power在SUP_CORE_POWER.raw §III–V/VIII实读后，dual scoring/reducer投影到定义的entropy/concentration/diversity feasible sets，§IV-H明确是成熟projection。7个synthetic financial agents/hash subset/feature reward/perfect evaluator，boundedness来自设定constraint，未新增本项目路由/可靠性选择条件。不是因小规模/局部/理论而EX。三项日期未核实，也未见当前官方事件撤回/纠错信号；明确负贡献先停止。

00364污染已一次身份恢复，不继续隔离身份：官方monthly title/live abs与单ID Atom是Distribution-Aware Companding Quantization，abs/API的实际Abstract却为multi-token prediction。SUP_ID_00364.raw重新单ID核仍同污染，不是本地错接；SUP_ID_HTML_00364.raw的精确v1正文标题/作者/ID与首Abstract一致且正确为DACQ，实际题摘说明weight重构误差降低却PPL/任务退步的critical-outlier边界。用该正确题摘替代污染metadata，保留abs/API反证，不授MTP，也不断言撤回；只剩公开日期缺口，不需要作者身份材料才能继续该窄命题。没有展开全文为日期作代偿。

所有实际打开的当前官方事件页进行轻量withdrawal/correction检查，未见需撤回上述采用的明确标记；API返回later版本仅提示exact-v1恢复，不能将版本号自动解释重要修订。不遍历全部版本史。

## Gemini新增候选：原负面裁决本轮纠正

Gemini3.1FlashLite原§2/§5的“未披露架构所以贡献关闭”不足覆盖card评价差额。本轮root在原card上指出安全信号后，作者再次读官方HTML的Published3March与Ethics§完整尾。SUP_GEMINI_CARD_WEB.json是官方web提取原件；curl35失败记录不能否定原文可读。release原稿March3与card公开日一致，只标日期即按March3落补窗，不制造timezone缺口。

只准入一个家族的窄安全评价命题：**跨card改grader/query后混用表格排名 → 当前card显式拒绝这种可比性，自动flag与manual判断以及不同baseline分别披露 → 版本化scorer/人口并区分局部回归与发布许可。** 2+1+3=6；因实际安全/评价边界深入受影响core。不是高价低价、强弱/版本名称贡献。官方Safety表是相对2.5FlashLite的绝对百分点变化，tone脚注又写2.5Pro，保留原baseline口径差异，不拼一排名。自动损失存在；厂商人工认为大多false-positive或非egregious，不构成独立零风险证据。redteam与borrow3.1Pro/DeepThink的CCL推断是不同证据人口，不把weak generally capable推为每风险支配。收益/倍率不采用，私有query/grader/完整人审样本与生产SLO/硬件/精度Not Disclosed；未运行/复現。

Books决定已有覆盖、没有修改：已加载PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE/最新checkpoint，实际对读Ch66 §EvaluationIdentity(283–301，model×benchmark×harness×environment×scorer及评分变化归因分离)、§Scorer不是绝对真相(2710–2740，judge/prompt/rubric固定/人工critical slices/非truth)、§ReleaseGate(3351–3381，不能以overall抵消safety slice；source/target风险协议与直接测量/迁移推断；不是弱模型每维安全定理)，以及Ch65/67开篇的前后交接。本card不提供超出这些具体稳定命题的新分支，不为增加材料引用制造diff。root已独立核Gemini必要官方Source和实际Ch66已有覆盖，并通过本轮六部分DAY；先前对旧16Source/POST的有效结果仍复用，不由旧结果替代本轮验收。

普通扫描/筛选/必要源与Books比较已结束。root已实际核全部31个潜力家族完整题摘、全部3个明确EX及Power/CoVe决定准入core、00364正确HTML题摘及Introduction窄段，并通过Gemini必要Source/Ch66具体已有覆盖与六部分DAY；14来源查询/返回/停止和31日期隔离已实核，API total232/73/242/164、返回100/73/100/100已复算。不授全294发现逐项题摘/全文或全量Coverage/Evidence，不继续全文绕日期。普通待办0，本日增量完成。来源历史缺段与31个first-public日是精确外部终态保留，不用于正面Evidence/Books/无遗漏；00364污染metadata与正确HTML题摘分开，不再虚设身份缺材料。旧GPT card gap与时区/首发时刻请求仅冻结历史，本轮不再索要、不列新gap，去重复用03-03官方PublishedMar2及实际Source/POST结果；早三篇/Trident争议按冻结结果保留，不重复请求，不继承旧09:00推定为本轮日期。
