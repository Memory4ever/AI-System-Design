# 12/28 已发现身份题摘补审

2026-10-02 北京实际补齐SCAN中19个新增身份的官方abs完整题摘，并按root负侧校准补读22738/22639 exact v1题摘与决定准入的方法；新增判断范围现21项。链接 `https://arxiv.org/abs/2512.<ID>`；无当前撤回标记。SWE-RM/SmartSnap定点复用26 ADMISSION同身份同题摘判断，不复用日期/覆盖结论。当前abs不是冻结v1正文。Potential均保留必要首次公开缺口，不评分、不进入确定本窗候选/Books。

| ID | 具体增量及处置 |
| --- | --- |
| 23752 Bayesian scaling | Potential/反证：matched random-axis干预对照发现熵几何是readout非唯一行为瓶颈，修正小模型机制向大模型的外推。 |
| 22760 Hilbert tokens | Potential：保持邻域的Hilbert重排与邻近merge/prune，检验token缩减的空间连续性约束。 |
| 22753 RSA exploitation | Potential/安全反证：可运行CVE exploit与提示轮次检验仅技术门槛威胁模型；作者夸张普遍结论不采用。 |
| 22682 VACP | Potential：大词表conformal覆盖/集合尺寸权衡，semantic masking与temperature需核边际覆盖假设。 |
| 22631 faithful CoT | Potential/评价：GRPO/DPO在大小模型faithfulness表现与稳定性差异，需核度量真实性，不把回答准确当忠实。 |
| 22630 discreteness | Potential/设计分析：五性质对连续/离散diffusion取舍、uniform corruption与多token依赖失配，需读实际推导而非综述命名。 |
| 22492 RobustRL | Potential：按trainer/rollout role局部恢复、warm standby与动态UCX重连，改变全任务重启/轨迹重放成本。 |
| 22471 Bayesian geometry | Potential：可解析posterior且不能memorize的wind tunnel及容量匹配MLP对照，隔离attention/FFN路由/更新机制。 |
| 22470 DarkPatterns | Potential/安全评价：分层意图与七类伤害揭示binary标签无法表达的autonomy manipulation盲区，需核401样本标注/协议。 |
| 22733 FoldAct | Potential：summary改变未来observation分布，分离loss/完整context一致性/segment训练针对RL非平稳和梯度稀释。 |
| 22716 Memento2 | Potential：read/write反思进入soft policy iteration，给状态覆盖增加下收敛命题；需核状态/检索假设，不能只是复述RL。 |
| 22560 RollArt | Potential：按阶段异构硬件、trajectory解耦及staleness-bounded权重同步，检验环境阻塞和异步训练质量代价。 |
| 22536 CoAgent | **重开potential/评价反证**：[exact v1](https://arxiv.org/html/2512.22536v1)§6.3作者实际定点读watermark remove/restore控制；§7.3再生成成本与hard limit；§8.2稀疏keyframe verifier漏短时physical interaction。原“成熟组合/摘要无控制”关闭撤销：这些具体metric混杂/检测边界有准入潜力，不采用Sora2排行或其“证明无偏”概括。 |
| 22351 VULCAN | **重开potential/执行边界**：[exact v1](https://arxiv.org/html/2512.22351v1)§4 adaptive anchor失败折半/突破推进，§6.4拆solver/tools/backtracking与single-agent，§9.3几何近似collision detector/yaw-only优化/阈值。MCP角色不是贡献，但恢复搜索与近似约束的可靠性差额可准入；zero collision只限测试不等于物理安全。 |
| 22066 SRAM/frequency | Potential/硬件边界：组合模拟呈现leakage与延迟的反直觉能耗取舍，需保留simulated workload，不能推广最优频率/32KB硬件。 |
| 22047 MAI-UI | Potential：user interaction/MCP训练数据与按task-state device/cloud路由、在线RL扩展，可能改变UI-only/统一云执行假设；收益/隐私均待精确证据。 |
| 22009 iSHIFT | Potential：latent slow-fast与perception control token共同调节推理深度/视觉区域，需核预算归因。 |
| 22562 AHA | Potential：每head/token binary full/local router，测量global context依赖尾部；需核长序列/硬件实际成本。 |
| 22671 width pruning | Potential/反证：parametric knowledge与instruction能力非一致退化，七ratio及两模型规模修正统一压缩损失假设。 |
| 22738 BioSelectTune | **重开potential/筛选反证**：[exact v1 §3.2/§4.4](https://arxiv.org/html/2512.22738v1)。高IFD筛选丢掉空JSON负例，改为只筛正例并保留全部负例；同源弱模型筛选与比例消融可核筛选器错配。不是医学标题即排除；不采用SOTA或50%普遍最优，首公开仍hold。 |
| 22639 Tree-Transformer | **方法核准后范围关闭**：[exact v1 §III-B–D/§IV Table II](https://arxiv.org/html/2512.22639v1)。二叉树聚合至单root，attention退化为该向量投影；广播root与局部坐标，经共享MLP回归两项功率，MSE拟合闭式解。线性复杂度确有具体设计，但属于集合回归的固定全局瓶颈，并非保留token间关系的attention或生成状态替代；原文未建立当前基础模型主线的机制/适用条件增量，不能借树压缩类比引入。非领域标签关闭，不追不影响处置的日期。 |

21新增身份：20 potential、1方法核准后范围关闭；另2既有身份判断定点复用。2026-10-02按root纠错完成CoAgent/VULCAN及上述两项决定准入的必要差额；原标题负侧/摘要关闭计数撤销，局部准入读不算全文/评价验收。日期外部缺失不豁免题摘，现无此类普通待办。必要首公开仍隔离，待原始new批次/作者可验证完全落窗公开范围后只恢复对应正文和owner对读。没有因访问信息、负面性质或Books已覆盖缩池。

补读时间：2026-10-02T19:30:01+08:00。22738仅把负例保留/筛选错配作为TRAIN-DATA待核命题：IFD与weak-to-strong来自既有Superfiltering，同源更优归因还可能混入tokenizer/模型能力差异，不把生物医学应用路线引入。22639的复杂度/性能比较只在合成功率数据上，容量与硬件可比性不据此通过；关闭不等于否认其局部架构价值。22529铝氧化仍按AI for Science暂缓，不受这两项纠错牵连。
