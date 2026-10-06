# 03/13 题摘与范围停止点

执行日期：2026-10-02。作者 mar03_v3；严格窗口03/12 09:00→03/13 09:00 BJT。新主题发现169独立标题线索，完整v1题摘28家族，另定点恢复MiMo官网Tangram对应1份完整v1题摘；不是旧614库存或31候选的再标签。标题清楚为领域科学/医疗/金融应用的只作范围线索，不把169整库变成逐项关闭队列。

## 28实际完整题摘

首8官方API原文见 V3_FIRST_ABSTRACTS.md。随后实际官方abs/v1完整题摘：11337、11245、12109、12011（web），11395、11653、12252、11331、11862、12206、11388、11947（HTTPS单页抽取完整blockquote），11853、11445、12230、11619、11768、11975、12056、11896（同法，原文完整输出保留于工具记录；后8完整原文另存V3_LAST_ABSTRACTS.md）。后20份官方事件页轻量当前版本/标记；首8补核当前官方abs的header/Comments，见[V3_FIRST8_EVENT_HEADERS.md](./V3_FIRST8_EVENT_HEADERS.md)。AdaFuse存在官方text-overlap说明，单列原创/重复增量未决；普通v2/v5不当重要修订，不展开全部版本，不授完整撤回/历史标记覆盖。两次多ID API空响应均没有算已读；转实际官方abs成功后才计上述12份。

以下全是未确时的潜在或含糊项，不是确定本窗候选，不评分，不称Evidence已成立。每项官网abs路径为 https://arxiv.org/abs/2603.IDv1；上界原值见两份DATE_PACKET。首次常规公告下界本批均为03/13BJT08，registered upper全部晚于09，因此仅相交，Updated不授公开。

| 精确ID | 题摘实际增量与需改变的判断（未核中心方法/实验） | 准入状态 |
| --- | --- | --- |
| 12201v1 IndexCache | DSA每层indexer仍二次复杂度→Full/Shared跨层索引复用及placement校准/平均attention蒸馏→重考虑稀疏attention的重复选址成本 | root完整题摘校准潜在成立 |
| 11535v1 Expert Threshold | 固定topk/批次依赖expert选择→EMA全局expert阈值逐token因果路由→动态compute与AR负载均衡的边界 | root完整题摘校准潜在成立 |
| 12038v1 Slow-Fast | 每步重访全历史→句内support稳定、边界slow刷新/fast稀疏记忆→按语义时序而非固定每步成本选择 | 作者潜在，未独立证据核 |
| 11873v1 AdaFuse | 动态adapter碎kernel launch而非FLOPs成本→token一次pre-gating跨层共享/融合switch→路由粒度与执行路径取舍 | 作者潜在；current官方admin text-overlap信号已读，原创/重复增量未核，不称准入通过 |
| 11564v1 DapQ | prompt输入attention不匹配未来decode→位置感知pseudo query选择KV→eviction观测窗口应贴近生成位置 | 作者潜在，未独立证据核 |
| 12248v1 EBFT | teacher-forcing token监督不约束rollout序列→feature统计匹配+嵌套prefix并行rollout/PG→无任务verifier的dense反馈选择 | 作者潜在，未独立证据核 |
| 11487v1 Attention Sinks | softmax归一化默认zero输出需sink、非归一ReLU可无sink→重新区分特定任务上的必需锚点与注意力异常 | 作者潜在，定理假设未核 |
| 12118v1 Cornserve | any-any请求路径/组件scaling不一致→component disaggregation+record/replay依赖及producer直传→统一engine部署边界 | 作者潜在，未独立证据核 |
| 11337v1 RewardHackingAgents | scalar metric可能由tamper或leak提升→两向量独立控制+trusted reference/file-access→评价integrity不能从reported score推得 | 作者潜在，数字/安全有效性未采用 |
| 11245v1 Sim2Real | 高能力LLM模拟用户不等于真实交互→451人协议对照过度合作/单调正反馈→Agent success simulator外推需人类验证 | 作者潜在，人类协议未核 |
| 12109v1 Self-Locking | outcome RL的query选择与belief更新互锁低信息→directional critique重分学习信号→信息获取反馈闭环需区分AS/BT | 作者潜在，未独立证据核 |
| 12011v1 RL Generalization | 同环境难度transfer不等跨环境→语义/接口偏移及sequential/mixture对照→RFT泛化评价应拆environment axes | 作者潜在，混杂控制未核 |
| 11395v1 ARROW | continual world-model固定FIFO任务遗忘→短期+distribution-matching长期buffer同容量对照→retention/forward transfer取舍 | 作者潜在，不泛化全模型 |
| 11653v1 VLA Continual | 顺序fine-tune必然遗忘假设→pretrained VLA+LoRA+on-policy RL有限反证→复杂CRL机制是否必要 | 作者潜在，机制归因未核 |
| 12252v1 EndoCoT | MLLM单次/不变conditioning→latent-thought迭代并接入progressive DiT+terminal grounding→编码推理深度与denoise时序 | 作者潜在，未独立证据核 |
| 11331v1 Jailbreak Scaling | 单次攻击率不足刻画采样预算→注入强度与polynomial/exponential crossover→攻击预算范围须条件化 | 作者潜在，spin-glass映射/经验有效性未核 |
| 11862v1 Instructional Leakage | documentation setup指导与攻击语义难分→README端到端外传/防御FP对照→高权限executor合规不能作安全代理 | 作者潜在，未采用百分比或普遍未缓解结论 |
| 12206v1 CLASP | Mamba输出embedding token detector对结构新trigger cluster-CV→probe检测边界而非分类器组合本身 | root题摘校准potential；actual有效性未核 |
| 11388v1 Refusal Triggers | alignment数据benign cue关联refusal→显式trigger训练并验jailbreak/benign取舍→拒答与安全目标不可单指通过率 | 作者潜在，机制归因未核 |
| 11947v1 Paralinguistic | 内容中心LALM忽略副语言→层定位/selective FT+dualhead相对alllayer→模态层次与适配范围 | 作者潜在，layer控制未核 |
| 11853v1 PRISM | 十生命周期hooks/TTL风险聚合/policy/audit是成熟组合；是否有实际新部署correctness或防线贡献条件尚不清楚 | 决定准入事实含糊；先日期隔离，不称准入 |
| 11619v1 Taming OpenClaw | claimed跨时/多阶段威胁+case studies可能修正point-defense有效性，但仅taxonomy/成熟guard也可能无增量 | 决定准入事实含糊；先日期隔离 |
| 11768v1 SSGM | claimed topology泄漏/iterative semantic drift formal分析是否超出已有consistency/decay/access组合不清楚 | 决定准入事实含糊；先日期隔离 |
| 11975v1 HomeSafe | static safety遗漏dynamic unsafe detection；streaming dualbrain本身成熟，须具体盲区/受限latency-quality证据 | root题摘校准potential；未核实验有效性 |
| 12056v1 XSkill | visually-grounded经验/skill双stream提取检索可能改变可迁移层级；是否只是成熟记忆组合需具体分离对照 | 决定准入事实含糊；先日期隔离 |
| 11896v1 Think While Watching | interleaved perception/generation阻并发与memory decay→segment causal mask/position+watch-think并发→在线视频状态与调度边界 | 作者潜在，时序因果/成本未核 |

这些26项共同重开条件：官方在03/13BJT09之前的正文公开上界或其语义依据（历史announcement、对应公开日志/可靠timestamp原值），与已有Submitted/schedule下界形成完全落窗区间。若核为窗外仅恢复真实日，不扩本日；确认落窗后才继续含糊准入事实/必要方法与对照、评分及Books。不要求全库公告/版本史；不因已有Books覆盖、附件成本或访问状态将potential删掉。

## 具体负侧及窗外线索

- [VMAO11445v1](https://arxiv.org/abs/2603.11445v1)：完整题摘的DAG+domain agents+LLM completeness/replan/stop组合，25market query对single-agent quality未提出新verification信号或成立条件。不是因样本小或读全文成本关闭；root实际完整题摘核通过。
- [Perplexity RFI12230v1](https://arxiv.org/abs/2603.12230v1)：完整题摘是已有attack-surface/defense taxonomy及standards agenda，未给新的具体执行/安全contract或独立设计反证；安全标签不自动准入。root实际完整题摘核通过；不宣称安全深审完成。
- [城市洪水预测](https://research.google/blog/protecting-cities-with-ai-driven-flash-flood-forecasting/)：完整官方core104–149是weather/RNN城市洪水预报，media-missingness评价修正仍该EarthAI应用范围；AIforScience暂缓，不绕Evaluation重引。root实际core通过。
- [Groundsource](https://research.google/blog/introducing-groundsource-turning-news-reports-into-data-with-gemini/)：完整core103–141是洪水news抽取/翻译/时间/地图定位dataset，既有Gemini prompting没有新增通用模型/系统机制，科学领域用途明确；root实际core通过。
- Seed目录March12“Permutation invariant multi-scale full quantum neural network wavefunction”：标题即量子波函数科学应用，按暂缓范围关闭；未冒称全文/题摘或root已核。
- [ARL-Tangram13019v1](https://arxiv.org/abs/2603.13019v1)：完整题摘action级外部资源orchestration为潜在系统增量；v1Submitted03/13T14:25:20Z晚于本日结束，arxiv正文事件最早不在本窗。MiMo Paper目录March13 day-only不等于同一arxiv公开时间；官网先挂正文是否发生于BJT00–09尚缺。该官网事件单独精确日期保留，不评分/Books。不能把目录项当已处理重复或给固定09点。

剩余标题只是有界发现线索，无逐项准入/排除/全文认证，不称全169已筛完，更不称全614批次已审。来源停止以V3_SOURCE_STOPPOINT为准。
