# 12/26 已发现身份的题摘补审

2026-10-02 北京时间实际恢复。仅补SCAN已发现集合，不扩宽库存。下列官方abs的完整标题与abstract通过原始HTTP实际读取；未见当前事件撤回标记。身份链接统一为 `https://arxiv.org/abs/2512.<ID>`。abs当前摘要不冒称冻结v1正文。Potential表示贡献增量足以继续核验，**首次公开尚不确定，非确定当窗候选、不评分、不进入Books**。日期隔离不再替代普通题摘初筛。

| ID / 原文机制 | 具体贡献判断 |
| --- | --- |
| 21859 TimeBill | Potential：固定KV淘汰比例不能满足不同deadline；长度预测和端到端时间估计驱动动态淘汰，可能改变质量/完成率取舍。 |
| 21852 KL estimators | Potential/设计反证：不同估计器配置的梯度偏差造成目标实现差异；on/off-policy结果可能修正KL正则实现选择。 |
| 21835 LOIP | Potential：将offload成本纳入异构层划分并重叠加载/计算/通信，配合UMA加载和在线KV压力适配；需核端到端基线。 |
| 21651 1-bit output alignment | Potential：朴素输出对齐失败来自跨层累积及表示各向异性，可能修正1bit校准目标。 |
| 21571 nncase | Potential：e-graph全局重写结合存储异构的vectorize/distribution/schedule，需核相位顺序与通信代价控制。 |
| 21487 FinDEP | Potential：DEP中共享expert和粗粒度调度限制重叠；可变粒度/顺序求解改变MoE通信调度。 |
| 21326 eval noise | Potential/评价反证：拆分预测/数据/总噪声并all-pairs配对测量，可能改变重复生成与题目采样预算。 |
| 21017 SFTKey | Potential：第二阶段只优化答案token，检验长CoT与短答案的梯度预算失衡；需核预算归因。 |
| 20967 deadline spot | Potential：预测误差下commitment horizon与无预测策略切换，提供误差条件下的界与regret。 |
| 20953 AutoHet | Potential：非对称3D并行和抢占后优先本地状态恢复，改变异构spot训练计划/恢复成本。 |
| 22288 Co-GRPO | Potential：将模型与unmask schedule同纳入轨迹MDP共同优化，纠正单步训练/多步推断断裂。 |
| 21815 entropy attack | Potential/安全：少数高熵token集中对抗影响，稀疏攻击与跨VLM迁移修正均匀token防护假设。 |
| 21734 Knot Forcing | Potential：缓存身份KV、重叠chunk temporal knot及动态参考时间位置，针对流式视频边界与长程漂移。 |
| 21714 AstraNav-World | Potential：动作条件视觉预测与预测视觉条件轨迹双向约束，检验分离想象/规划的累积误差。 |
| 21446 dUltra | Potential：Bernoulli unmask planner与模型共同on-policy RL，直接优化正确性/步数而非固定启发。 |
| 21336 Denoising Entropy | Potential：路径累计不确定性量化用于后选/在线解码控制，需核收益是否来自路径预算。 |
| 21276 GriDiT | Potential：低分辨率时间网格联合生成、高分辨率逐帧细化，改变长序列时间/空间因子化。 |
| 21268 ACD | Potential：attention supervision直接约束视频条件，检验classifier guidance分数作弊及控制成本。 |
| 20963 balanced representation | Potential：两层DAE记忆/泛化表示结构证明，结合深模型实证；需严格保留理论假设与外推边界。 |
| 22280 Valori | Potential：Q16.16与可回放状态机针对跨架构memory不确定性；bit-identical保证需核实现/量化误差。 |
| 21757 code optimization study | Potential/评价反证：实际PR比较发现agent性能验证比例差异，可能修正自动优化的验证要求，非泛化所有agent。 |
| 21708 MoRAgent | Potential：按reasoner/executor/summarizer分离LoRA与角色数据，需消融确认不是仅流程命名。 |
| 21627 AstraNav-Memory | Potential：图像context压缩与导航策略耦合，适中压缩优于极端压缩的条件可能改变视觉记忆接口。 |
| 21567 DAM | **贡献前关闭**：摘要明确非新算法，仅把读写拆为即时访问/层级维护并用value/uncertainty描述选择；未给新增可执行机制、受控证据或具体失效条件，不借成熟决策论准入。日期未核，不另追日期。 |
| 21302 AndroidLens | Potential/评价：保留环境异常、多有效路径及milestone ATP，可能修正长任务二元成功指标盲区。 |
| 21024 PIBR | Potential：用可读源码表示对手policy，LLM迭代best response配合运行单测；需核Program Equilibrium假设。 |
| 20957 RepoNavigator | Potential：单一execution-aware跳转工具与端到端RL，可能改变定位工具复杂度/探索取舍。 |
| 21818 code injection | Potential/安全：coder-reviewer-tester与security agent权衡及毒化few-shot反例，不能把新增审查agent视为防护保证。 |
| 21250 CoTDeceptor | Potential/安全：多阶段代码混淆针对CoT检测器语义推理失效，需核攻击预算及分类/迁移条件。 |
| 21008 GateBreaker | Potential/安全：路由定位安全expert后定点神经元移除，反证安全均匀分布假设；需核白盒权限。 |
| 21220 RoboSafe | Potential/安全：短程回溯与长期预测生成可执行predicate，需核逻辑有效性和观测/执行时隙边界。 |
| 21911 sparse verification | Potential：speculative verification阶段联合attention/FFN/MoE稀疏及跨draft/layer复用，需核分布保真/接受率。 |
| 21919 SWE-RM | Potential/评价反证：相同TTS性能不等价RL适用性，提出分类准确率/校准区别及受控数据组成实验。 |
| 22087 CAT | Potential：主动context tool与轨迹监督而非被动溢出压缩，需核任务语义保留与预算归因。 |
| 22208 Moxin variants | **贡献前关闭**：完整摘要只给开放训练/数据/代码及VLM/VLA/中文变体和优越指标，未描述新训练/融合机制或受控边界；开放事实不是本次长期设计增量。日期未核，不另追日期。 |
| 22322 SmartSnap | Potential：任务策略主动收集最小snapshot供独立judge，可能改变稀疏任务验证成本；self证据不自动等于独立验收。 |

36项题摘初筛已处理，34 potential隔离、2明确关闭。安全/设计反证保留，无因日期或读文成本降分。必要逐ID官方首公开证据仍外部保留，收到后只恢复对应ID的日期、精确正文、owner实际段落比较。普通题摘待办0；本记录不是Evidence审阅完成或独立复核通过。
