# Apr14 有限非作者机制与处置校准

复核者：apr02；报告作者：root。实际读取下列官方 exact-v1 必要机制、评价及反证，并对读当前 Books 的具体论点及相邻交接。仅判断准入与窄知识缺口；不批准日期归属、不写 Books、不代替 Apr14 日级 Gate，未复现实验。

## 2604.09595v1：压缩的维度预算必须看到实际 kernel 合法域

来源：[Why Smaller Is Slower? Dimensional Misalignment in Compressed LLMs](https://arxiv.org/html/2604.09595v1)，实际 §3、§4.1–4.3/Algorithm1、§5/Table5 与 §7。当前 `INFER-TENSORRT-LLM` 的 Ch49 `从 Linear 语义到 GEMM 执行` 已解释 M/N/K 不同导致不同执行成本，`cuBLAS 不是一个固定 GEMM Kernel` 已解释 descriptor、heuristic 和离线缓存；但未具体承载**压缩 artifact 的维度分配先经目标 kernel profiling 形成合法候选集合，再在全局参数预算下选择各矩阵的维度**。

材料将原始压缩维度附近的 mod8/mod16 候选与实际设备/library 上的延迟 cliff 结合，形成各矩阵的候选集合，随后用多选 knapsack 分配模型参数预算。它不是对固定 shape 再换更快 kernel，也不只是重述“小模型可能慢”；形状选择本身成为压缩的约束。因此准入与这一窄 owner 缺口通过，建议 2+1+2=5，因确认 Books 缺口而深入必要内容，不能沿用旧高分倒推准入。

Table5 只覆盖 FP16 Llama3-8B、15% 压缩、作者 A100 实验与 H100 子集、Hugging Face/PyTorch2.9.1/CUDA12.8；延迟是 B1/S1024 的 **prefill-only**，不是 decode、生产 serving、并发或 tail SLO。质量代理和 knapsack 目标不保证质量不变：ASVD 的 PiQA/HellaSwag 从 .58/.28 到 .57/.26；LLM-Pruner 从 .80/.49 到 .78/.47。有限评测每任务200样本。可采用的命题是上游维度预算与下游合法执行域共同选择，不能采用“无损加速”。Profiling 身份/成本、预算离散化、质量复测和跨设备失效需近正文保留；dense 或规则维度旧路径仍是回退。

## 2604.09603v1：稀疏决策点与 depth-first/width-second 的批次资源分配

来源：[ECHO](https://arxiv.org/html/2604.09603v1)，实际 §2–3/Algorithm1、§4 的假设、§5.1–5.3。当前 `INFER-SPECULATIVE-DECODING` 的 Ch48 `Verify Length 不是孤立的固定超参数` 与 `从全局 Verify Length 到输入自适应 Block Policy` 已解释 target capacity、prefix survival、局部 block controller、混合 forward 和 calibration；没有实际承载**按稀疏 gate 决策，先跨请求分配 depth，所有活动请求无法继续延深时才在局部扩 width**的两轴控制次序。准入及窄缺口通过，建议 2+2+2=6，Books 缺口触发必要深入。

主机制在 root、target-depth 及离线校准后的中间位置检查累计 draft confidence，把被截断请求的预算释放给其余请求；ragged tree 再 flatten/pack 到验证 kernel。Target 仍拥有 accept/commit，gate 不获得 correctness 所有权。这里可采用的是控制次序、决策成本和稀疏检测的条件分支，不是所有 confidence controller 最优。

Algorithm1 **不能直接作严格总节点 cap 的证明**：第一阶段只检查 `budget > 0` 后追加 `Wtopk`，若剩余预算小于 `Wtopk` 即可能超支；第二阶段定义 `w=min(budget,Wmax)`，却调用 `widen(k)` 并扣 `Wmax`，变量/扣账不一致。采用时须另外由 runtime 对实际追加节点作 capacity admission，不把作者总体预算叙述当形式保证。§4 的 widening 分析以 target 分布排序为条件，不能无条件转给 draft 排名；固定线性轮次成本下的交换论证也不证明公平性或全负载最优。

§5 主评测为 8×H100，BS1 使用 HF，BS8–256 使用 SGLang，受测模型/任务限定；主要指标是 throughput/MAT，并未实证完整质量或 SLO 保持。正文可不照录速度百分比；precision、长度及 tail SLO 未在本次必要主文中披露，不能补造。MAT/depth 的作者“利用率”也不是全部树节点的接受比例。稀疏 gate 可能漏掉应截断路径，漂移/公平性/packing 开销仍须回退到已校准的静态或简单 depth 策略。

## 2604.09651v1：生成轨迹正常不等于动作目标合法

来源：[FlowHijack](https://arxiv.org/html/2604.09651v1)，实际 §3、§4.1–4.4、§5.1–5.5/Tables1–4。当前 `MULTIMODAL-EMBODIED-VLA` 的 Ch26 `Trajectory Geometry 可以提供廉价 Alarm，但不是成功概率` 已解释 geometry-normal failure；`安全评估必须区分偏离日志与违反动力学` 已分开 novelty、transition 与外部授权。这不自动覆盖本材料的**fine-tuning supply-chain 参数投毒，在 early flow-time 重定向场方向而匹配 benign 场范数，使有限几何/范数传感器不能单独确证任务目标**的构造性反证。准入与这一限定缺口通过，建议 2+2+2=6，安全边界深入；canonical owner 为 Ch26，Ch72 只交接 artifact/provenance 风险，不重复整套攻击摘要。

攻击者访问预训练参数，控制少量投毒数据及训练 loss 后发布 compromised model；不是仅 prompt-time 的用户输入攻击。§4.3 在 `tau∈[0,.4]` 上将场指向恶意 action chunk，Eq6 匹配恶意/benign 场的 L2 范数，不匹配方向。**Flow-time 速度不是物理墙钟速度**；ODE 积分传播早期改变也不是任意 solver/轨迹长度下的放大定理。作者 embedding/norm 接近不能证明全部统计不可区分或所有 detector 无效。

主实验限定 pi0/LIBERO40任务及适配 BadVLA；clean success 也会退步。作者 ASR 定义为触发时任务失败，不等于所有失败都完成指定恶意目标。去除 mimic 时攻击仍可工作但检测相关表征变化，支持有限隐蔽性机制，不支持普适防御失败。§5.5 endpoint 距离过滤把 pose-lock ASR100降至17.8，但 initial perturbation 仍82.2，说明小位移任务失败与该端点过滤契约不同；这不是所有 kinematic shield 的失败证明。此次未独立审真实机器人附录，不能扩写真实硬件/控制周期保证。

窄采用应把 goal/trigger/supply-chain 条件测试与低成本轨迹传感器分开，保留独立实际动作验证和物理 envelope 的 commit 所有权；不采用“速度正常所以安全”或“单一守卫必然无效”。

## 交接边界

这三项的准入、必要来源及具体 owner 差异非作者校准通过；仍需作者决定最小正文写法、真实写后复核，并完成各自日期与全日来源/候选终态。无新来源扫描、无全附录重读、无版本差分、无实验复现；此文件不将旧模板的 Existing 或 Complete 继承为当前结论。

## 追加五项有限处置校准

本批只处理 root 指定五项，实际补读核心方法和决定处置的反证。以下 PASS 不批准全日日期或 Books 已写入。

### 2604.09587v1 MobiFlow：标准5、仅报告通过

实际核 [exact-v1](https://arxiv.org/html/2604.09587v1) §3、§4.1–4.2、§5.3/5.5。task-specific、固定转移结构的图合并，由成功轨迹的人工一致标签、union-find 和共享 transition 降低 live harness 成本，确有有限评价构造增量，可保留；错误动作保持界面、空白或提示是环境约定。7条轨迹与平均 task-relevant branching 不证明全部真实路径覆盖；人工 label/transition 是否等价和外部 app 状态变化仍限制 validity。CR/CVR/AMR/TTA 不互相替代，其中 Table2 的 CR 距离记法不清晰，不用它证明普遍进度单调或安全。支持受限标准证据保存，不采用 complete graph 的开放环境保证；不为 benchmark 名称扩写 Books。

### 2604.09604v1 Gridworld：具体前分母关闭通过

实际核 [exact-v1](https://arxiv.org/html/2604.09604v1) §3–4。固定 ASCII 地图、局部观察/已揭示地图和五个行动示例比较已有模型，缺 classical replanner；不同 API 的解码控制不完全匹配。模型与 few-shot 结果说明这套无工具接口的 prompt sensitivity，但未分离新 state-update 或规划机制，也不支持把 dense/MoE、训练流程或 reasoning mode 作为结果因果。这里关闭的是有限任务比较对现有解释/设计选择没有新重要增量，不因 toy、参数量或 robotics 范畴拒绝。

### 2604.09606v1 APST：具体前分母关闭通过

实际核 [本稿](https://arxiv.org/html/2604.09606v1) III-B/C、固定配置 Bernoulli/binomial 与225个 AIR 派生 prompts 的 breadth/depth 分账；定点对照[既有同作者 APST](https://arxiv.org/html/2602.11786v1) 的同一重复采样协议及 Ch66 `Safety Evaluation 还需要 Depth-oriented Repeated Inference` 实际正文。当前稿没有显示改变旧判断的重要机制或新独立边界，关闭贡献合理。采样深度提高只改变罕见事件发现与估计信息，不自动提高真实逐次失败概率；独立采样假设和 judge 仍限制风险结论。该判断不是凭 submitted 合并发表史，也不批准两个 ID 完整身份合并；没有把 already-covered 主题本身作为唯一排除理由。

### 2604.09611v1 Multi-request Energy：标准5、仅报告通过

实际核 [exact-v1](https://arxiv.org/html/2604.09611v1) §4.1–4.3/Listing1、§5.0.2–5.0.3 与 §6。共享 prefix、顺序依赖和角色混合改变 batch 的收益曲线，是值得保留的受限条件证据；Llama2-7B、单 A10040GB、vLLM0.9.1/Parrot、T=.7/top-p1、16用户、batch1–16 和10次重复限定结论。生成吞吐与 Listing1 的整个 workflow 时间分母不可互换；主要比较未锁定所有质量/SLO，也未逐组件干预隔离 cache、queue、role 原因。Ch70成功 goal/整机/质量核算提供采用边界，但不能据此称具体系统与算法全已覆盖。标准仅报告合理，不采用普遍 engine 排序或组件归因，不为了 Only 扩读所有附件。

### 2604.09624v1 SECL：标准5、仅报告通过

实际核 [exact-v1](https://arxiv.org/html/2604.09624v1) §3.1–3.3/§4 与 Appendix N/P/Q。冻结无 LoRA base 的相对 discriminative signal，经有界方向目标、bin gate 和 entropy-triggered burst 更新 confidence，是具体 label-free recipe；未使用 gold 的在线 gradient 不等于所有温度/超参选择不用标签。Appendix N 的无 generation–discrimination gap 模型不改善，Q 的换 SC 目标明显退步；P 的8B模型 aggregate ECE 改善但 AUROC .684→.643，domain ECE/答案质量也不全面改善，故不能把 ECE 低直接升级成可靠拒答或 truth probability。confidence loss mask 不隔离共享参数。现 Ch66 sensor/真值、calibration slice 与质量分账是采用约束，而非该配方的已实现算法；仅报告而不假称 Existing 合理。

本追加五项必要原文/具体处置非作者校准全部通过，未复现实验、未展开发表史、未扩原始队列。作者仍须同步实际正式报告及日级 Gate。

## 三项实际写后与相邻链路：非作者通过

作者 root 已真实写入后，apr02顺读以下正文及相邻交接，并与此前必要 exact-v1证据定点核对，不无差别重读附件。

- **GAC / Ch49 当前408–410**：在 cuBLAS descriptor/heuristic 的边界之后，将形状合法域向上游压缩维度预算传播；profiling/离散搜索、质量退步、Prefill范围和固定对齐回退近正文保留。当前实际命题与 §4.1–4.3/Table5/§7 相符，未偷换为 decode/SLO收益或无损质量。写后通过。
- **ECHO / Ch48 当前282–284**：承接 input-adaptive/global capacity，再引入少数深度 gate 与延深优先/局部加宽后备；没有给 confidence 提交权，明确实际节点 admission 与启发式非严格cap/最优证明。control、漂移、公平与ragged成本及静态共存均在原主线中，写后通过。
- **FlowHijack / Ch26 当前1000–1002**：承接外部物体攻击转入 compromised artifact 的内部方向/范数分离，flow-time与物理速度、task failure与恶意目标、clean recovery与后门清除均分账，并交接 Ch72供应链权限。为核实“受限实机攻击”这一个正文事实，此次额外仅定点读 AppendixD/E.1/G.1–G.4：Franka Panda、两场景10任务、每任务10示范及两有限case，不是多机器人/全trigger族或控制SLO验证；原正文未采用其统计不可区分宣传或新增实机性能数字。实际正文与必要来源相符，写后通过。

该三项真实写后 PASS 不替代各family日期核验或 Apr14日级 Gate，未复现实验；其余共享Books无写入。

## 追加 09665 / 09666 / 09670 有限非作者审阅

### 2604.09665v1：安全深入5、仅报告通过

实际独立读[官方 v1](https://arxiv.org/html/2604.09665v1) §2.1、§3.1–3.2、§4–4.2 / Tables1–4。base与finetuned模型的prompt-response最后token表示余弦相似度，为候选BoN提供排序分支；proxy分布分离不证明不安全行为的起源因果。固定layer12与逐模型/题库最优layer必须分开，后者是选择后的乐观上界；固定层在GSM8K/MMLU上有utility代价，普通instruction-tuning的迁移仅小幅甚至反向。PAIR仅两student配置和有限查询，不证明自适应攻击普遍安全。实际 Ch72 Learned Security Sensor / Reference Monitor 及相邻白盒direction段分开probe、因果干预、迁移与授权；没有完整描述这条双模型BoN算法，不假称Existing。有限新sensor与teacher-student条件证据可保留为Only，不能升级为安全控制默认方案，处置通过。

### 2604.09666v1：标准5、仅报告通过

实际独立读[官方 v1](https://arxiv.org/html/2604.09666v1) §4.2–4.4、§5.1–5.5 / Tables1–5及AppendixB/E必要语料与成本段。agent控制与backend交叉比较可检查线上搜索能否替代离线结构，确有条件证据；但GraphSearch的multi-hop最佳图差距27.23→26.59仅有限缩小，不能采“结构已无必要”。主文dense用2018Wiki，AppendixB图用每题context构造corpus，缺同知识机会的完整对账；Table1/4若干同配置数字也不同，不从中推出精确普遍因果。离线构建/单次检索成本不包括统一线上query全流程摊销。对读 Ch76 Agentic Retrieval 与 Query/Compression/Stopping、operator索引成本主线，成熟选择原则已在，但未有本具体cross-backend协议，Only而不伪称算法Existing合理。保留限定实验与图/稠密共存，不照录GraphRAG普遍更稳或GRPO总优。

### 2604.09670v1：缺口深入5、Ch22窄提案通过

实际独立读[官方 v1](https://arxiv.org/html/2604.09670v1) §2.1–2.3、§4.1–4.3、Discussion与A.5.12。26字母、50turns的non-thinking N-back中，teacher forcing分离自生成错误；中层位置表征分开、晚层target/readout对齐是观测链。第一层answer位置的SVD干预，把字母身份变化拉向平均投影而非删除整个子空间，seed-controlled对照支持局部干扰解释；图4是每model×N选择最好direction/strength后的上界，并非固定控制器迁移保证。10model间任务相关不证明自然语言推理因果。

已对读 Ch22 Effective utilization / 长上下文计算-状态-读取合同（约97–118行）及固定rank/recall段：现文含干扰与读取定义，却未解释 **窗口内可访问的信息仍可能在answer-state混合，容量不足与选择/读出干扰应区别；受控跨层诊断和answer-position干预不能直接当通用优化**。支持在容量合同之后、评估切片之前嵌两窄段。位置可能仍参与机制，不把局部结果表述为Attention天然不使用位置；保留CoT/外部memory未测、默认解码不同、sweep乐观、可扩大状态/显式检索等旧路径。来源→真实owner缺口非作者通过，实际Books尚未写，写后另核。

本追加仅三项，不复查其他raw身份；未作日期Gate、未写共享Books、未复现实验。

## 09670 实际写后：非作者通过

apr02 实际顺读 Ch22 容量合同之后、评估切片之前的两段与相邻交接，以及该 family 的 Review note，并复用上项已核 exact-v1 必要来源。正文正确区分可访问历史与 answer-state 的选择/读出干扰；第一层 answer-position 拉向平均投影没有被改写成删除整个身份子空间。受控测量、局部干预、每模型/负载最优 sweep 的乐观性和自然语言/外部 memory 未测边界均保留，专用索引旧路径与过度抑制的成本也在论证内。实际机制正文与证据边界非作者写后 PASS；可同步该项 Review note 的待写后状态。此结论未复现实验，不代替 family 日期或 Apr14 日级 Gate。

## 第八批四项：有限非作者必要源与真实 owner 校准

复核者 apr02，作者 root；实际读作者第八批原始记录、以下四篇官方v1必要方法/评价/反证与现有Ch16/48/81正文。范围只有09709/09718/09722/09731；未写Books、未扩raw、未复现实验，不代替日期或整日Gate。

### 2604.09709v1 OQC：5分标准、仅报告通过

实际核[官方 v1](https://arxiv.org/html/2604.09709v1) §3.1–3.5、§4.1–4.7、§5。低rank二次分支、消除投影后host方向平行项与gate确是可检验分支；带epsilon的消除不是严格零内积，低rank投影/lift也不证明原输出空间或函数空间完全非冗余。Table4有host×readout组件对照，因此不能以“只有更多参数”抹掉贡献；但主表/消融的LR与epoch不同，不能跨protocol做单因素因果，动态gate及readout迁移退步保留。CIFAR100/DeepViT8层256宽、TinyImageNet/三seed只是限定测试，不因小规模拒绝，也不当任意FFN的普遍结果。

实际Ch16 `MODEL-FFN` 的两层非线性、GLU/SwiGLU乘性分支与参数预算段已经正确解释原FFN非线性；不能随作者背景误写普通FFN仅线性。现章没有完整OQC算法，但本证据未形成必须改写一般FFN设计选择的稳定新边界，故2+1+2=5标准Only而非伪称完整Existing合理。保留具体有限构造、projection/gate成本、局部几何代理与质量分账；不得以投影cosine接近零作任务独立因果或部署吞吐保证。

### 2604.09718v1 Agentic Compilation：具体前分母关闭通过

决定准入的最小消歧实际核[官方 v1](https://arxiv.org/html/2604.09718v1) §3.2–3.4、§4.3、§5。JSON blueprint、HITL、静态executor与异常时selector修复，仍是已知compile/execute与稀疏replan组合。实际Ch81 Deterministic Spine/Agentic Nodes、canonical DAG及template/run/trace（约130–173）、trace编译的数据依赖/authority（约1084–1100）已经说明其可采用控制边界；这不是只因主题相同关闭。当前三任务没有分离新的可采用状态/授权或可靠性反证，具体前分母关闭合理，不为新命名再次入选。

46/50、8/10、47/50是编译成功；98/95/96%是成功blueprint中的执行口径，不能合成整个流程near100%。人工修补、结构变化、SPA等待/网络失败成本没有被O(1)描述消除；§3.4异常调用数为R，不能把整个开放网页任务推成零修复成本。schema合法不赋予effect授权，不采用“全部失败都来自模型而非executor”的归因。无需为这种明确成熟组合再做全附件。

### 2604.09722v1 ConfigSpec：6分标准、仅报告通过

实际核[官方 v1](https://arxiv.org/html/2604.09722v1) §3.1–3.2、§4/4.1–4.4必要公式及配置。accepted-token goodput、每验证token线性价与本地drafting能耗有三个不同目标，配置最优不同是具体受限系统证据；但能量式只计P×drafting-time，等待/无线/cloud没有因“验证在云”变成零能耗。固定约.5s verifier与忽略batch的token-price是模型输入，不是端到端已测生产服务；K=2的bonus-token分支不保证现实billing/全链能耗最优。

实际Ch48 shared verify budget 与edge/cloud控制（约570–603）包含draft速度、acceptance、channel、cloud-profile与fallback，但没有完整实现本文三个目标选择器，不伪称算法Existing。2+2+2=6标准Only可保存profile/目标分账的具体结果，不必重复成熟controller原则写Books。限制RPi4/5/Jetson64、GGUF Q4–Q8、Dolly15K及两target；cloud硬件/precision、线上并发/SLO未充分披露，不从本地配置表推出普遍edge/cloud部署决策。

### 2604.09731v1 SMART：6分深入，中央期望/单步保证的窄争议通过

实际核[官方 v1](https://arxiv.org/html/2604.09731v1) §3.1/Eqs1–5、§3.2/Eqs9–16与§4/Tables3–4、batch反例，并对读Ch48 target-verifier/commit与shared-budget实际正文。hardware/batch-profile下以边际收益/成本控制树确有机制贡献；未因估计问题关闭整篇或否定所有实验。

**争议一：Eq2的估计对象。** 它对root-to-leaf路径的累计概率和做均值。若一层树提供两个互斥token，各target概率.5，且target采样验收可选择任一在树中的token，则树覆盖的第一步接受质量是1，Eq2却是.5；只有另行规定均匀选择单一路径等执行合同，路径均值才可能对应该合同期望。稿中没有给出这座桥。draft probability近似target也是额外假设，相关性不证明校准或无偏。此反例限定于宣称的验收/期望身份，不声称所有tree verifier必用同一采样实现。

**争议二：仅改称surrogate也不足以恢复Eq13的普遍增量。** 一个树只有概率.9的一层叶子，路径均值.9；加入概率.1的兄弟叶子后，新路径均值(.9+.1)/2=.5。Eq13按旧路径数计算的新增量却为正.1；新增路径导致分母改变时，连该均值自身的增量也未被正确求出。路径数不变的扩展可以另行限定，但不能把它作为所有宽度扩展的保证。真实边际值/成本已知时，正增量的ratio比较本身仍成立；有问题的是将当前近似增量代入后声称每次真实期望speedup必增。作者§3.2明确greedy不全局最优，不额外指控其证明了全局最优。

因此2+2+2=6深入、对中央期望与单步保证保留 `Disputed` 是准确窄处置；可以同时保存作者profile与经验controller结果，但本轮不以这些公式作长期保证写Books。若只保存经验heuristic可称其经验部分受限Only，不能因此撤销中央保证的争议。重开条件仅需对齐实际tree验收/路径选择、修正跨路径数的边际估计并明确draft校准假设，不要求无界重做全部实验。Table3 batch1局部略输MSD、不同预算反收益仍保留；quadratic attention不推出普遍exponential latency，profile拟合不能作为架构定律。底层target exact验收/rollback的正确性是独立合同，不由此争议被否定，也不由controller自身提供。

四项有限处置非作者通过：两Only、一具体前关闭、一中央保证窄D。不预支单篇日期与整日报Gate。

## apr02：第九批三项有限非作者裁决

### 09741 ExecTune：5分标准、仅报告 PASS

实际核[官方 v1](https://arxiv.org/html/2604.09741v1) §3.3–3.5、§4.2、§5，并顺读 Ch79 计划假设、observation 与 execution/commit 分权（约14–74）。target 实际成功过滤 teacher 策略、结构 gate 和相对无 guide 的退步惩罚是具体训练分支，不因成熟 planning 原则关闭；但单轮数学/代码、固定 guide/core 的经验尚不足以另立可靠规划保证。Advisor 域外退步、可解析非忠实执行、理论 mixture 假设及调用成本保留。2+1+2=5 标准 Only 通过，不冒称现章已有完整配方。

### 09744 MPAC：6分安全深入、仅报告 PASS

实际核[官方 v1](https://arxiv.org/html/2604.09744v1) §4.2–4.3、§6.3–6.5、§7.3、§8.4及§10，对读 Ch84 event-log authority/journal-before-fold 与恢复合同（约891–910）。固定 pre/post-commit、实际 target frozen scope、coordinator 离线禁共享 mutation 与 epoch 恢复是受限协议分支；authorization 不等执行声明，intent 缺失不能绕过 scope。现章已有持久化/权限原则但非本协议全实现，因此 Only 而非泛称 Existing。2+2+2=6 深入通过；单次三-agent bench、66实现测试非形式证明、split-brain 未测、最终观察非严格 linearizability，未经另核的 A2A 比较不采用。

### 09747 ADAM：6分安全缺口深入、Ch77窄提案 PASS

实际核[官方 v1](https://arxiv.org/html/2604.09747v1) §2.2、§3攻击 loop/anchor/update、§4.1/4.3与§5，并顺读 Ch77授权检索/可披露及随后ORAM威胁模型（约174–194）。已有逐次 read authorization 和外部存储访问模式，尚未具体承载**已披露输出被反用为下一 query 的跨轮累计提取**。支持在两者之间窄补：冻结 memory snapshot、匹配 query 预算并同时测每次披露和跨轮唯一暴露，输出许可独立于 similarity，预算/限频不是消除泄漏保证。2+2+2=6 提案 PASS；作者30 queries/300 records/top-k3、四 victim/三任务有限，EQ/EE/CER/ASR分母分开；暴露 anchors 与 entropy proxy 不是隐藏总体分布/最优信息增益，停止信号不证明无剩余记录。只需此攻击/测量边界，不采用未核的EM全局保证、不恢复AI for Science，不先称已写Books。

三项为必要证据与实际owner有限裁决；ADAM仍待实际正文与非作者写后，不代替本日来源、日期和最终候选 Gate。

### apr02：09747 ADAM 实际正文写后 PASS

实际顺读 Ch77 similarity≠可披露后的两段（约184/186）及前后授权读取、ORAM威胁模型，复用上述已核未变的[exact-v1](https://arxiv.org/html/2604.09747v1) §2.2/§3/§4.1、4.3/§5。正文准确把 returned anchors→new query→跨轮唯一暴露与存储方访问位置区分，要求 memory snapshot/principal/总查询预算及静态查询对照；暴露主题分布与停止信号不能证明隐藏总体/无剩余记录，限频不能替代披露许可。机制与限制融合到原 read authorization 论证，而非另起论文摘要，内部受信简单读取与外部调用者边界成立。实际写后非作者 PASS（apr02），可同步 Integrate；未复现实验，不代替 Apr14 日级 Gate。

## apr03：09748 实际正文写后 PASS

独立实际打开 [exact-v1](https://arxiv.org/html/2604.09748v1) §4.2–4.3、§5.1/Table1，并顺读 Ch31:312–333 与实际新增325/327两段。checked answer/code span 的正确性不能为完整输出安全背书，原文拒答不给终值与有害前缀接正确答案的奖励非对称支撑这一窄机制；不需要推断 verifier 被篡改。正文分别保留任务效用、非触发安全和触发行径；CA 是安全指标而非任务正确率，Table1 部分 CA/PDR 退步没有被“整体保留”遮蔽。top200 经 shadow/dual verification 筛选，不是随机2%生产风险；正文未采用通用植入概率或防御消除保证。两段连接独立评价与后续 tokenizer 评分接口自然，采用范围/共存边界与真实原文一致。此处只通过单篇 source/body，不替代 Apr14 日级 Gate。

## apr02：第十批六项有限非作者校准

实际重开六项官方 exact-v1 必要方法/评价/中心反例，并读相关真实 owner。以下是单篇处置校准，不是日期、完整来源或冻结分母验收；未复现实验。

- **09749：2+1+2=5，标准仅报告 PASS。** [v1](https://arxiv.org/html/2604.09749v1) §3.1–3.5、§4.1/4.4、§5支持按 object proposal 的置信度/稀有度重分 attention 行幅度并 EMA 平滑。Alg1逐元素构造与 softmax 后 causal mask 不提供自动重新归一；proposal 来自作者所称 vision stack，非免费真实对象。拥挤场景与伪 proposal 反例已承认。实际 Ch23 视觉 sensor/独立 grounding（约712–715）承载通用采用边界，却非此配方全部实现；因此 Only 而非笼统 Existing。有限 CHAIR/POPE/VQA 不能证明幻觉本质仅在 decoder attention 或所有模型无质量取舍，未披露端到端成本/SLO 不补造。
- **09759：2+1+2=5，标准仅报告 PASS。** [官方两页 PDF-v1](https://arxiv.org/pdf/2604.09759v1) 正文/图1–6已实际读完：signed stochastic temporal bitstream 与光学 AND、同相检测/analog accumulate 形成具体硬件替代。§III明确 device/architecture simulation、CACTI/Vivado/custom simulator，8-bit/128-bit stream、有限 BERT/ALBERT/ViT/OPT350 等；不是实测芯片或在线服务。现 Ch49 执行路径/数值合同不足以承载未经实测的部署选择，Only 安全成立，不能把能耗倍率写成真实服务收益，也不因两页短稿排除具体机制。
- **09781：2+1+2=5，标准仅报告 PASS。** [v1](https://arxiv.org/html/2604.09781v1) §3.1–3.2、§4.2–4.4/Tables2–4、§5支持 renderer 反馈、world-axis/object-centered 坐标叠加、单轴旋转与 AABB 尺度平移的 pose 推理接口。LIBERO/Franka 协议与 SIMPLER 模拟分开；task success 与 grasp success 不混。Table3 的 Stack45.8低于SoFar70.8（原文字误称最优），540子任务中 view/单轴影响有限、重复渲染/VLM延迟明确不适实时。Ch26 高低层/feedback/commit 的成熟合同不被这种受限配方推翻；Only 不称其已被完整实现覆盖，不采用自评停止为 physical-safe proof。
- **09813：2+2+2=6，标准仅报告 PASS。** [v1](https://arxiv.org/html/2604.09813v1) §3.2、§4、§5.2–5.3/Tables2–3确有 oracle-preserving augmentation；但错误输出/缺参数改变所需行为，必须 judge-assisted，非全部 deterministic。格式、normalized call/answer、行为 judge 分账；7B/14B 的 MultiTurn 和 ACE Agent 均退步，SFT 的 prompt 兼容性混杂已明确。实际 Ch27 executable spec→outcome/lineage（约355–376）覆盖通用正确性与 shared ontology 限制，但不是此 recipe，因此受限 Only，不用标题或 oracle 名称重复新增通用原则。
- **09750：2+1+2=5，安全深入仅报告 PASS。** [v1](https://arxiv.org/html/2604.09750v1) §3.3、§4.4、Limitations 的成功攻击子集 cosine、WANDA/PCA/tSNE 是相关观察，不是恢复干预或唯一原因。LlamaGuard3误判、R1仅HarmfulQ、单轮、没有防御测试均明确；有限 conflict 变化支持具体威胁边界，不支持全框架绕过/未测防御或空间重叠的因果保证。当前 Ch72 独立威胁/有效性评价不需据此新增泛化理论，Only 安全成立。
- **09748：2+2+2=6，安全深入、Ch31窄缺口提案 PASS。** [v1](https://arxiv.org/html/2604.09748v1) §3.1–3.2、§4.1–4.3、§5.1/Table1、§6.3与实际 Ch31 Reward Hacking（约312–333）对读：冻结 verifier 并不能保护它没检查的完整生成行为；有害前缀接正确终局答案获正 reward、拒答无答案获负 reward是不同于词表适配错误的输出覆盖漏洞。支持窄补 checked span 与 full response 的分账。top200约2%来自 shadow/dual verification 选择，不是随机剂量；CA是非触发安全、任务 utility另计且有退步；defense平均ASR下降非消除后门。没有生产安全概率或未经披露硬件/SLO保证。已发 root 按现主线落笔，仍待真实写后独立复核。
