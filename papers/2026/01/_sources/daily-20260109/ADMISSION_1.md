# Jan09 首批题摘准入

原始完整 exact-v1 题摘及现官方页版本说明：[ABSTRACTS_1_RAW.txt](ABSTRACTS_1_RAW.txt)。全部实际读完题摘；当前页未见撤回/安全勘误信号，现 v2/v3 普通版本不自动作为本窗事件。首5项原始字段与公开区间已核见 DATE_BASIS，root已独立准入校准；本记录仅保准入层，不以 API published 当公开，不替代必要 Evidence/Books 处置。

| exact v1 | 原约束→具体增量→需重考虑的选择 | 贡献处置 |
| --- | --- | --- |
| 2601.03368 | BPE通常按压缩解释→不同BPE深度实际改变频率/slot entropy与局部依赖→token单位改变时如何比较模型预测熵及信息负担；不授near-IID普遍规律 | 潜在准入2+1+2=5，待日期/校准 |
| 2601.03385 | collapse需昂贵完整embedding谱→Gram deterministic/stochastic bounds作可扩展谱收缩代理→是否能用该有限代理监视递归训练而不把representation收缩当全面质量 | 潜在准入2+1+2=5，待日期/校准；精确v1是SIGMA LLM Collapse，不用v3改名 |
| 2601.03417 | 显式graph昂贵/latent难检查→latent储存、训练materialized graph、推理只外化定额subgraph→训练与检索接口如何分配symbolic成本和可检查性 | 潜在准入2+2+2=6，待日期/校准 |
| 2601.03425 | 稀疏router常被当domain specialization→跨domain的expert-group routing mass集中→group-level路由测量是否足以改变specialization解释；不授load-balance损害因果 | 潜在准入2+2+2=6，待日期/校准 |
| 2601.03468 | 多reward ensemble被当充分缓解→单reward/ensemble均出现artifact失败与小artifact detector补偿→T2I reward收益须和独立视觉artifact切片分账 | 潜在准入2+2+2=6，待日期/校准；不借成熟reward hacking原则加Durability3 |
| 2601.03484 | LLM搜索quantization/config本身成熟→AB只有自动调优和对unoptimized模型收益，未清楚新增接口或成立条件 | 仅决定准入的method待核，不先成为候选/全文/Books队列 |
| 2601.03376 | Transformer以weather heuristics预测A*/Dijkstra合成路径next-node，题摘未建立foundation/VLA/新优化条件；领域速度数字不足 | 范围/贡献前关闭，不评分，不因Drone字样拒；无影响处置信号，日期未核后停止 |
| 2601.03389 | HMM pain-belief用于gridworld内在reward及normal/chronic行为类比，题摘未建立foundation模型或新长期学习系统条件 | 范围/贡献前关闭，不评分，不因小模型拒；日期未核后停止 |

本批8份完整AB：5准入、3贡献前关闭（HAQA决定性method已root实际核通过），不是冻结本日分母。表内“待日期/校准”保原初筛时点提案，现结果按本段更新；准入后必要证据另见 EVIDENCE_1。
## 决定性补读：HAQA03484

原v1 §3.1–3.4（L89–129）实际prompt分Static hardware/search-space/kernel参数与Dynamic accuracy/latency/history，通用ReAct反馈迭代至maxiteration；§4.1（L133–138）原baseline与模型/硬件设置；§4.4 L253–259将mobile INT4 unpack/FP16转换解释为比INT8慢。方法未给新的量化/搜索更新、资源执行协议或hardware compatibility成立条件；旧LLM-HPO/ReAct+kernel参数搜索用于量化deployment，int4不native/解码packing代价是本地已知backend条件的说明，未建立新校准条件。提议贡献前关闭，不因2.3×/LLMagent框架或owner映射准入；不称所有实测无效/预算公平已核。已必要定点method/core read即停止，不进入候选评分/full审阅队列。cache NECESSARY_CORE_1_RAW.txt03484节供root校准。
