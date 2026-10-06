# 2025-11-15 有界题摘判断

四主题API与109个相关ID标题只作发现；未转为整类关闭队列。以下36个精确v1完整题摘已实际读取，原题目/摘要/作者/提交原值全部保留于三批raw XML：[首批10](raw-arxiv-first-exact-v1.xml)、[第二批14](raw-arxiv-second-exact-v1.xml)、[第三批12](raw-arxiv-third-exact-v1.xml)。BuddyMoE接口摘要截短，完整摘要和必要机制已实际由[HTMLv1 raw10](raw-web-10.json)修复；不声称接口截短段完整。

35项保留的是潜在机制/边界/局部反证，不是当窗候选或已核知识缺口。所有submitted/published Atom字段保持提交权限；决定贡献前不因无实验细节关闭，决定日期后才展开必要证据/owner。这里只给首批待校准三项拟分，其余不以主题或成熟原则虚加评分。

| v1身份及短标题 | 完整题摘给出的具体增量与最低必要反侧 | 初筛处置 |
| --- | --- | --- |
| 09710 Echoing | 角色镜像在60配置/3领域交互中出现、更多推理仍未消除；需固定backend/提示/回合及principal保持定义，v3数字不倒填。 | 拟6，首批校准；日期待核。 |
| 09864 UGCS | 高不确定样本短窗口reward排序checkpoint且不增加forward；核uncertainty、选择集泄漏/窗口及验证预算。 | 拟5，首批校准；日期待核。 |
| 09741 TawPipe | 拓扑分组与固定weight/gradient shard降低weight-passing跨节点通信；核长序列交叉点、PP/FSDP公平配置及HBM。 | 拟6，首批校准；日期待核。 |
| 10054 BuddyMoE | coactivation buddy缓存替代miss expert，TAE与CPU residency门控；近似质量/传输取舍，不等专家功能等价。核校准分布、替代误差、prefetch对照和miss极端。 | 保留，必要机制消歧完成；非无损加速。 |
| 11729 Harli | decode/PEFT共用空闲memory、两阶段latency预测与QoS调度；核46.2%平均/92%上限对应负载、预测误差、尾延迟和干扰。 | 保留，晚编号首公开更须核。 |
| 10643 Black-box on-policy distillation/GAD | 黑盒teacher文本、student generator/discriminator自适应reward；核teacher采样/训练预算、LMSYS evaluator/style混杂。 | 保留，不授普遍超teacher。 |
| 10400 CP-WBFT | confidence probe weighted consensus结合异构拓扑；核85.7%故障耐受的故障模型、成本与liveness，不称密码学BFT。 | 保留。 |
| 09958 Audio-VLA | contact audio闭环与TCR过程评价，不仅成功率；核模拟collision音频/2真实任务、触觉对照、过程/终点分账。 | 保留，不因encoder组合关闭。 |
| 09748 Compact CED | 约1B质量/VRAM/延迟前沿、0.6B实体/数字漏检；核英→德域、M4Pro24GB/400ms配置与ensemble成本。 | 保留局部负证据，不授所有SLM甜点。 |
| 09724 PALMS+ | DepthPro现成深度、几何floorplan convolution、particle filter用于4楼33轨迹定位；无模型/训练/VLA/runtime机制差额。 | 范围关闭，局部定位结果不称无价值；日期未核不追加恢复。 |
| 09984 Language Drift | RAG跨语言输出崩向英语的decoder attractor诊断，soft target-language penalty；核内容/语言/资源分账与目标语言识别失败。 | 保留，不等理解失败或英语普遍吸引子。 |
| 09883 HCC-3D | global queries压缩点云后adaptive compensation补未捕获细节；核98%压缩同质量/空间定位损失与补偿预算。 | 保留，不单用数字准入。 |
| 09973 DiVE | AVL/PVL等差向量约束微调时原CLIP embedding geometry；核ID/OOD对照与几何约束的局部代价。 | 保留替代优化约束。 |
| 10098 MTAttack | 多trigger-target干扰，proxy space partition/prototype anchor；核特定VLM/攻击权限、目标数量与防御失效边界。 | 保留安全机制信号，不操作攻击。 |
| 10201 EffiReason-Bench | verified steps/E3将质量与推理成本联评，7方法6模型无统一赢家；核correctness verifier/预算定义。 | 保留评价盲区，不当新增榜单关闭。 |
| 10232 VocalNet-M2 | multi-codebook直接AR与MTP取消flow首块等待；核725→350ms是否codec/硬件/质量/端到端一致。 | 保留生成路径取舍。 |
| 10262 MTR-DuplexBench | 边界模糊多轮turn segmentation/context consistency、IF/safety盲区；核音频生成及安全评价协议。 | 保留，未来开源不直接关闭。 |
| 10279 PROPA | MCTS process GRPO及success/failure SFT交替/PRM inference；核搜索teacher预算、训练mix与推理额外成本。 | 保留，不因成熟模块组合自动关闭。 |
| 10289 Music Flamingo | MFSkills音乐注释、MFThink coldstart/GRPO；核音乐时间/推理收益独立对照。官方项目Published Nov03早于窗。 | 保留家族事件差额；不能用Nov13提交称首发，项目日字段也不证明论文精确首公开。 |
| 10292 RUDDER | 一次forward利用CARD视觉证据/残差更新、Bayesian adaptive token steering；核attention证据代理、gate及真正总延迟/幻觉代价。 | 保留，不授因果视觉解释。 |
| 10303 Rectify | lower-perplexity critique verdict偏置、OPS self/other对照及perplexity-aware GRPO；核perplexity与正确率解耦/生成器来源。 | 保留评价混杂反证。 |
| 10395 AgentEvolver | self-question/self-navigate/self-attribute用于task/experience/credit；核各模块有效性、探索预算与环境移位。 | 保留，preliminary不等无贡献。 |
| 10457 State Tracking | 三个隔离任务区分modern CoT/legacy状态跟踪；核步数、模型/提示/重复条件，局部失败不授通用能力界。 | 保留负侧。 |
| 10628 Instella | 全开放3B配方/MI300X实测有潜在可复现系统信息；实际model/Long/Math已March/June/Aug公告，Nov论文需识别新增报告信息或v2实质差额。 | 保留身份差额，不先标已审重复，不凭改版本触发。 |
| 09880 EnchTable | NTK safety vector distillation解耦task与interference-aware merge；核跨architecture近似假设、jailbreak/safety-utility回归。 | 保留，不授普遍安全。 |
| 10051 GraphIF | 跨turn constraint/action trigger抽取成关系图后rewrite；核误抽取/长度扩张、图结构vs额外tokens对照。 | 保留。 |
| 10381 Methodological Pitfalls | base pretraining linguistic plausibility不同normative reasoning正确性；核可操作判别与示范，不外推post-trained。 | 保留方法反证，不把成熟目标原则直接算新机制。 |
| 09971 NumPert | label-flip numerical perturbation使factcheck准确率至多跌62%，长上下文反而受损；核真实标签/扰动难度及demos恢复。 | 保留局部失效因子。 |
| 10029 ScaleFormer | overlap chunks与前后span累积向量、无参fusion实现线性成本；核摘要任务中边界损失与访问未来context条件。 | 保留替代long-context设计。 |
| 09873 HierRouter | specialized pool多步finite-horizon MDP/PPO路由；核6bench3model的调用成本、context传递与policy训练预算。 | 保留，不仅更换路由术语。 |
| 09700 Order Matters | in-context样本顺序方差与selection comparable，dev选择近oracle；核0.5～27B/GPT5范围、dev成本/测试泄漏。 | 保留评价/构造边界。 |
| 09993 SPAN | 六calendar跨历法/未来日期非对称失效；核模板生成与去污染声明、format转换及基础算术控制。 | 保留能力边界，不因日历域关闭。 |
| 10507 Rubric-based AdvancedIF | 1600专家rubric与多turn复杂system指令、RIFL verifier/reward；核reward hacking、rubric evaluator与成本。 | 保留，不因benchmark名准入。 |
| 09966 REAP | 显式subtask/fact全局state与multitask planner、multi-hop OOD；核状态更新错漏、recursion/plan对照及检索预算。 | 保留，不因递归成熟原则关闭。 |
| 10621 Socratic SSR | verifier定位(subquestion,subanswer)，controller局部重解而非整答self-refine；核confidence标定与额外调用/错误定位。 | 保留，work in progress不排除。 |
| 10645 ParoQuant | pairwise Givens rotation/channel scales weight-only PTQ与kernel；核2.4%推理误差vsAWQ、groupsize/precision/hardware及<10%overhead。 | 保留。由bounded标题补获；Submitted 18:59:24Z实际在原查询18:59:59Z截止内，先前“超截止”表述错误已纠正。提交字段仍不能补造公开归属。 |

## 信号与停止

[current metadata](raw-arxiv-current-signals.xml)36条comments/updated已实际读取；无明示撤回/勘误字段，但不保证未发现的全文信号。Instella v2 Nov14 02:08:46Z与原v1都须核各自公开和实质增量；其余晚version不倒填。仅一个范围关闭，不把35个潜在项当本日35家族，也不为凑分将它们全变全文队列。

日期有限尝试及可接受替代另见后续日期笔记；初筛校准未返回时继续来源/身份/必要消歧，不提前对全体作Books结论。
