# 2025-09-02 FIRST 首批准入交接

作者：Aristotle。检查时间：2026-10-06T14:08:00+08:00。请求root局部准入校准，不请求最终DAY；02最终DAY须由未参与作者工作的Mendel/Archimedes等非作者执行。

本日窗口：`[2025-09-01T09:00:00+08:00,2025-09-02T09:00:00+08:00)`。已fresh读取当前AGENTS、适用合同/Prompt、来源使用说明/每日/arXiv主题、ROADMAP及月checkpoint（仅路由）。不继承01候选/结论，不将11 DAY结果移入02。

## 已核有限入口

接手本日独立原件，重新解析以下Atom而非依赖旧输出计数：

| 原件 | 实际范围/返回/停点 |
| --- | --- |
| [language head](language-recovery.atom)、[tail](language-tail.atom) | CL/LG/AI/IR/MA + language model/transformer/LLM/foundation model；start0返回200、start200返回57，total257，两页身份交0，无剩余页 |
| [systems](systems-recovery.atom) | DC/PF/AR/LG + GPU/inference/distributed/compiler + 模型词；start0返回35/total35 |
| [multimodal](multimodal-recovery.atom) | CV/RO/SD/AI + vision-language/world model/foundation/diffusion-transformer/VLA/multimodal-large；start0返回52/total52 |

三个主题组去版本后分别257/35/52，pair intersections为33/24/5，三组共同5，**并集287**。原请求实际提交发现区间为UTC `2025-08-29T18:00` 至 `2025-09-01T18:00`，较日报窗口宽；不是287个本窗首次公开事件。request.json保留执行时间/URL/status/bytes，API字段只作发现/身份。

当前作者实际浏览language前70标题及全部systems35/multimodal52标题（跨组去重），并定点读下列18唯一家族完整题摘/LongCat官方核心；不声称自己已读全部287标题/题摘。root此前全标题浏览和部分题摘属于有效发现上下文，不由本作者冒称重读。宽月476标题输出曾截断，不授全量覆盖、不建立逐项关闭队列。未扫描每周来源或其他日期。

## 13 项潜力，不是正式候选

所有arXiv首次公开归属尚未确认；不评分、不授当窗Evidence/Books。下表只说明原约束、原文实际增量和若成立会影响的选择。必要全文/反侧范围待校准后按拟命题定点读取，不预设13份全文任务。

| 原始身份/精确版本 | 贡献潜力及必须保留的边界 | 条件路由（非Books决定） |
| --- | --- | --- |
| [2509.00189v1 HiVA](https://arxiv.org/abs/2509.00189v1) | 固定workflow难迁移、reactive loop难积累结构 → semantic/topological联合演化、MAB routing和环境反馈textual gradients → 是否应共同优化节点语义与连接结构。5～10%宣传非因果/资源证明。 | AGENT-WORKFLOW / AGENT-MULTI-AGENT |
| [2509.00202v1 TConstFormer](https://arxiv.org/abs/2509.00202v1) | KV随历史增长 → periodic state update/每k步global sync的声称 → 固定状态近似与显式历史取舍。**摘要的amortized O(1)并未核实**：若sync随历史线性增长且k固定，不能由每k步一次直接推出常数；必须核sync实际对象/尺寸/误差，而非照录标题。保留争议信号，不授加速结论。 | MODEL-LONG-CONTEXT / MODEL-KV-CACHE |
| [2509.05316v1 Standard vs. Modular Sampling](https://arxiv.org/abs/2509.05316v1) | 单neighbor retain与1:1/cyclic sampling可能掩盖forget/retain取舍 → diverse-neighbor评价及entity-level MELU替代 → 重新核unlearning benchmark/sampling解释。不能把减分或回答变化当base-weight遗忘/隐私保证。 | TRAIN-DATA / PLATFORM-EVALUATION-SYSTEM |
| [2509.00217v1 Learning to Shard](https://arxiv.org/abs/2509.00217v1) | degrees与per-operator sharding分开启发式 → RL联合搜索并用elite history → 分布式inference的granularity/通信代价选择。3.5x对metaheuristics与1.06x对Megatron不能混分母；H100实验不补造NPU实机证据。 | INFER-TENSORRT-LLM / INFER-SCHEDULING |
| [2509.00221v1 Speech Foundation Models](https://arxiv.org/abs/2509.00221v1) | wearable专域表示需数据 → speech encoder features及simple probes可跨信号迁移 → 表示共享与专域训练选择。只保留speech/sensor表示的局部比较，不采mood/arrhythmia医疗应用或“domain-independent”普遍定律。 | MULTIMODAL-REPRESENTATION |
| [2509.00277v1 SABER](https://arxiv.org/abs/2509.00277v1) | SDPS语义query难组合/优化 → extended relational semantic algebra/SQL-compatible logical plan → operator兼容与计划正确性的执行边界。摘要说开启formal guarantees可能性，不等已证明LLM算子正确。 | AGENT-TOOL-CALLING / AGENT-WORKFLOW |
| [2510.15882v1 FlexLink](https://arxiv.org/abs/2510.15882v1) | 单NVLink瓶颈且PCIe/RDMA闲置 → heterogeneous links聚合及两阶段自适应流量分配 → collective带宽/数据移动取舍。8-H800 AllReduce/AllGather局部26/27%不是端到端training或serving收益；lossless/drop-in实现未核。晚ID不倒授日期。 | TRAIN-DISTRIBUTED-TRAINING |
| [2509.00309v1 Balanced Actor Initialization](https://arxiv.org/abs/2509.00309v1) | distillation后RLHF出现sequence-length collapse/reward hockey-stick → 两阶段weighted actor merging → 初始化与训练稳定/能力保持取舍。不能把作者“resolved/optimal ratios”当普遍因果或seed稳定保证。 | TRAIN-RLHF |
| [2509.00192v1 Safe-LLaVA](https://arxiv.org/abs/2509.00192v1) | 仅检查显式biometric请求漏掉普通回答泄露 → PRISM双方向评价/训练数据explicit+implicit audit与filter → 拒绝率与未请求泄露分账。过滤/减少泄露不等隐私消除，必须核faithfulness/false-refusal与评价泄漏。 | TRAIN-DATA / PLATFORM-EVALUATION-SYSTEM |
| [2509.00371v1 Two Causes, Not One](https://arxiv.org/abs/2509.00371v1) | omission减少可能增fabrication → attention interventions、visual-semantic potential field/VPFC → 两种hallucination是否应区别校准。因果两源与无额外fabrication都是待核命题，不照录“推翻”。 | MULTIMODAL-REPRESENTATION |
| [2509.02615v1 Radio Astronomy / prompt sensitivity](https://arxiv.org/abs/2509.02615v1) | semantic content不变是否应预测稳定 → layout/order/temperature改变下的局部不稳定 → prompt表面变化与模型推理能力评价分账。**边界校准项**：只请求通用VLM评价反证的保留，不采radio-galaxy科学分类、LoRA提升或scientific discovery路线；若原文未控制semantic等价，须收窄。 | PLATFORM-EVALUATION-SYSTEM；不绕回AI for Science |
| [2509.00374v1 APPT](https://arxiv.org/abs/2509.00374v1) | 3D→2D映射丢geometry → permutation-invariant point tokens/location及共享embedding/prompt generator接frozen异模态foundation model → 模态接口/空间信息取舍。参数不增、any-modality/generalizable声明未核。 | MULTIMODAL-REPRESENTATION |
| [LongCat-Flash v1](https://arxiv.org/abs/2509.01322v1)、[官方发布](https://tech.meituan.com/2025/09/01/LongCat-Flash-Chat.html) | 固定active计算/通信窗口限制 → zero-computation experts、PID稳定平均active budget、shortcut连接扩大comm/compute overlap → token计算预算与通信重叠的架构选择。560B/18.6～31.3B/avg27B为作者配置，100+TPS/30天/价格不作可比端到端保证；要核实际路由、PID目标与overlap代价。 | MODEL-MOE；执行代价交TRAIN-DISTRIBUTED-TRAINING |

## APRIL 校准后贡献关闭

[2509.25196v1 APRIL](https://arxiv.org/abs/2509.25196v1)：完整摘要提出frozen-model APO与policy RLVR组合API synthesis，81个真实API并与expert prompt/未fine-tuned模型比较。经[root实际题摘校准](INDEPENDENT_FIRST_CALIBRATION.md)，摘要仅说明既有模块组合及总收益，没有具体新增协作机制/成立条件，贡献关闭。不是因为实验细节不全而排除已有明确贡献；无剩余准入疑义，不开方法/全文队列。出现具体新协作机制或成立条件时定点重开。科学Python库只是API代码测试对象，不等科学发现采用。

## 4 项代表关闭，供抽样校准

| 实际完整题摘 | 具体理由（日期未核，不另追不影响处置的时刻） |
| --- | --- |
| [2509.00176v1 Waste-Bench](https://arxiv.org/abs/2509.00176v1) | 新clutter/deformed-waste数据与总体需要提高robustness，摘要没有给出区别既有理解的具体混杂/盲区或新评价协议。不是因局部数据/benchmark/环境复杂而排除；如正文有特定反侧再定点重开。 |
| [2509.00265v2 The Nondecreasing Rank](https://arxiv.org/abs/2509.00265v2) | ND tensor因子/monotonic constraints及有限rank反例有实际数学增量，但当前题摘未建立其如何改变本项目模型表示、优化或系统的具体问题；不把所有matrix理论都收入。不是无LLM词或理论身份排除，未称v1全文已读。 |
| [2509.00284v1 Industrial Contour](https://arxiv.org/abs/2509.00284v1) | conditional GAN+human standard prompts+VLM refinement提高CAD contour指标；未给改变表示/生成/执行解释的增量条件。模块名称、领域指标或GPT-image/Gemini排名本身不足。 |
| [2509.00549v1 BrainFM](https://arxiv.org/abs/2509.00549v1) | mild-to-severe/real-synth recipe支撑brain imaging五任务、11datasets；当前新增主要为临床影像统一与领域外观鲁棒指标，未建立主线通用机制的差额/有效性条件。**领域边界校准**：不是“医学即排除”；有明确一般表示/训练反证才重开，不经Data/Eval绕回整项clinical应用。 |

## 精确版本、日期与实际读到哪里

17个arXiv初读题摘来自本日四Atom对应entry；current versions为v1/v2/v3等，只作discovery。此前06:04:08Z工具返回未落盘，原记录不能由本日文件复查，撤回将其作为可复查原件的表述。现于2026-10-06T06:26:07.816589Z重新定点请求 [exact-v1 API](https://export.arxiv.org/api/query?id_list=2509.01322v1%2C2509.05316v1%2C2509.00192v1%2C2509.00221v1%2C2509.02615v1&max_results=10)，保存[实际原响应](exact-v1-five-recapture.raw)及[实际请求记录](exact-v1-five-recapture.request.json)：HTTP200/23220bytes，SHA256 `9a5f4166d2a3601a57b6df7362f4e0477e9ef611dc54c248c932a9ea030c13ff`。重新解析返回五个v1并实际重读完整题摘，API published/updated原值分别为：

- 01322v1 `2025-09-01T10:05:45Z`。
- 05316v1 `2025-08-29T19:25:52Z`。
- 00192v1 `2025-08-29T18:54:57Z`。
- 00221v1 `2025-08-29T20:09:48Z`（不能用其domain-independent措辞授普遍性；v3已收窄generalize表述）。
- 02615v1 `2025-08-31T14:31:47Z`（v1已包含prompt表面变化下不稳定信号，不以v2倒填）。

**这些API字段不是first-public证明。** 没有给任何arXiv材料赋本日公开时刻，没有通过DataCite登记、版本号、月份或日历schedule制造落窗。

LongCat本次完整读官方正文的发布/技术亮点/性能评估/部署/许可核心（推荐阅读/页尾无关），并读上述精确v1摘要；未声称已读完整报告方法或执行artifact。页面只显示 `2025-09-01`，没有时刻/明确时区，即使作为BJT整天也不能完全落在本窗。原Git commits9项实际解析，Initial Commit `f73c6bf...` author/committer均`2025-08-30T16:01:03Z`，另有Sep1修report typos；commit对象日期不是repo/public正文首次可访问时间。与较早家族关系一起隔离，不把Sep1博文当必然首次事件。当前也不授runtime支持已运行、图性能已核或MIT适用全部依赖。

未读这些论文全部方法/实验/附录、未运行代码、未作Books差额核。原始材料和实际推断分开；上述core需求按必要命题限定，不是因为datehold预开全文队列，也不能因datehold免除复杂度矛盾或安全/负侧的必要方法评价。

## 校准请求与下一批

root于2026-10-06T14:39:49+08:00落盘[首批准入校准](INDEPENDENT_FIRST_CALIBRATION.md)：13最小潜力保留，APRIL关闭，4代表关闭成立，首批当前为13潜力/5关闭。五v1新原件已由root实际完整解析。作者[TConstFormer及四负侧必要core](CORE_SUBSET.md)仍需最终非作者独立核对应原文；root读过作者说明不等独立core核查或02 DAY。首次公开、评分、Books及来源终态均未授予。

可继续普通工作：本日其余相关/含糊标题定点完整摘要、14每日机构原件的实际历史区间/分页停点、首公开必要原始路径；未把它们提前写安全终态。第一次校准后只扩查受影响集合，下一FIRST仍分批交，不因Books已覆盖或访问受阻删潜力。02未完成、不自授DAY；03～05尚未启动，按顺序每次fresh独立。

落稿检查：13潜力行计数与18唯一家族分层核对，本地链接/fence与新增文件whitespace无错误；进行中README补齐空候选表后V3通过1份。只是结构结果，不代替root准入或后续非作者DAY。未改Books/State/月索引、未stage/commit/push。
