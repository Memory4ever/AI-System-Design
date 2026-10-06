# Reader2 三项最小逐字拟稿（尚未写）

作者 oct07_missing；Source/date/具体 owner 复用 READER2_REVIEW R2-1/2/3。以下只申请 literal PRE，不自签。本人注均限对应Source/反证及本轮独立记录，不称复现。

## 04119 / Ch5

精确锚点：证据阶梯后现有“完整机制。”段之后、`内部读数的预测用途应与因果解释分别验收`前，插入以下唯一自然段，不替换既有阶梯。

因果作用还须绑定训练 checkpoint，不能只用成熟电路解释同一模型的早期状态。一条受限名字指代实验中，同一位置的干预在能力低谷改善、成熟时却破坏行为；进一步固定头集合和其他计算，只替换第一次名字位置的 value，贡献随 donor 名字改变，支持低谷中存在有害复制，随后形成的抑制与它竞争。把成熟抑制头的参数回植早期模型、由早期模型自身重算 activation，只能部分缩小低谷到成熟的差额，而直接放大早期头输出仍不足以越过 chance；这支持计算本身发生变化、而不只是原操作幅度变小的解释，不是证明完整或唯一的成熟电路。证据限 Pythia 的受控二选一任务及有限重复，较严格三名字控制并非全部稳健，随机头回植也非等参数匹配；为何训练先学复制后学抑制仍未独立操纵训练路径证明。保存训练轨迹、挑头、参数/activation干预与跨模板回归均付费；跨任务或规模失配时保留逐checkpoint诊断与独立行为对照，不将任务非单调升级为普遍训练定律。<!-- source-family:SF-2026-ARXIV-2610-04119 -->

拟本人注：`2610.04119v1`，5分，§3–5/D/H必要证据；Source/date/owner由reader2独核，literal PRE/实际POST另记；未核代码、未复现实验，不外推普适因果定律。

## 04808 / Ch49

精确锚点：lowering局部现有Relational Hoare HLS两段之后（末`实际硬件与 LLM workload 回归。`），下一现有段前。只插以下唯一自然段。

静态全流水的 FPGA 分支还可以把固定点算术本身作为低层 IR，而不是先套模型层模板：保留运算依赖、异质位宽及显式量化/溢出语义，以 affine arithmetic（不适用时退 interval）追踪增长并收紧中间位宽，再让同一算术结构供白盒 LUT/组合延迟估价与 RTL/HLS lowering 消费。位宽优化先要保持原模型的 bit-exact 数值行为，估价则仍须由实际 post-routing 验收；前者正确不保证后者精确。用户未显式限制的中间位宽可能不可综合，拟合微基准的结构成本也会漏掉拥塞、clock target与跨SLR影响。受测神经网对照只支持该静态kernel分支，未routed baseline不能比较实测latency，重新拟合的树模型也不是同一bit-exact模型；动态shape、PE reuse及LLM服务不在已证范围。Tracing、位宽分析、估价校准、完整综合与布局布线均付费，数值或物理回归失败时保留原位宽、成熟层模板或手写HLS，不由更小IR成本签发端到端服务收益。<!-- source-family:SF-2026-ARXIV-2610-04808 -->

拟本人注：Alkaid `2610.04808v1`，6分，§III/IV/TablesIII–VI必要证据；Source/date/owner由reader2独核，literal PRE/实际POST另记；未核代码、未复现/实测FPGA。

## 04089 / Ch81

精确锚点：Ch81 Ask or Assume两段后、“同样地，Agentic multimodal request…”前。已读完整澄清/投机局部。

澄清频率还可以作为期望交互预算学习，而不把每轮提问机会视为免费：以 atomic question 计数，将质量与问题数共同组成工作点，再在训练分布外核查预算违约。[受限策略对照](https://arxiv.org/html/2610.04089v1)中所谓 pass@1 实为 assertions 通过比例，不是整题全通过概率；prefix 排除在 PPO ratio 外也只限制直接更新，LoRA 仍可间接改变路由。训练的期望约束不是逐请求硬上限，测试均值可超过目标；未拒绝超预算与未检出质量下降，分别不证明合规和非劣效。一次提问池化的收益也不能独立归因策略。训练、全部问答与评判成本须计入，真实用户和不可逆操作仍保留硬门禁；预算或质量失配时保留已校准固定提问数、显式澄清与停止，不由局部曲线签发普适交互定律。<!-- source-family:SF-2026-ARXIV-2610-04089 -->

拟本人注：`SF-2026-ARXIV-2610-04089` — [exact-v1](https://arxiv.org/html/2610.04089v1)，Daily2026-10-07/Oct6窗，2+1+2=5。期望atomic-question预算/质量联合工作点，保test违约、非劣效/metric语义与全部费用；reader2 R2-3 Source/date/owner通过，literal PRE/实际POST另记，未核实现/复现，不授DAY。

## 04473 / Ch49

精确锚点：Ch49“调优结果也是带执行条件的可复用资产”末marker后、低Batch Decode标题前。已读完整tactic资产局部。

离线选择还可以在相同平均预算下比较逐层资源分配，而不只为固定算子挑 kernel：先用确定成本过滤不可行配置，再冻结质量代理做粗排，最后以独立真实执行和 held-out 质量复验，三层各有不同权限。[InferOpt 的受限对照](https://arxiv.org/html/2610.04473v1)说明均值相同的 KV/MoE 分配可有不同取舍，不证明代理排序准确或搜索算法本身新颖；其 MoE 设置没有总 expert 硬约束，压缩 KV 仍均低于 FullKV，所报相对 reference 比率不能改写成绝对分数提升。GPU、batch 与 concurrency 未披露，生成局部 TPOT 也不是端到端请求时间。搜索、代理构造、全部 profile 和复验都付费；代理漂移、质量或真实预算不合时保留原均匀分配、FullKV与固定 tactic，不让候选排序代签可发布资产。<!-- source-family:SF-2026-ARXIV-2610-04473 -->

拟本人注：`SF-2026-ARXIV-2610-04473` — [exact-v1](https://arxiv.org/html/2610.04473v1)，Daily2026-10-07/Oct6窗，2+2+2=6。matched-mean层分配/成本筛与proxy、heldout分责；保FullKV反侧、MoE约束及局部TPOT/配置ND，reader2 R2-4必要Source/date/owner通过，literal PRE/实际POST另记，未核实现/复现，不授DAY。

## 04938 / Ch24

精确锚点：Ch24连续DOIT自然段/marker后、下一现有段前；同节完整h/rollout邻接已读。

离散状态的终态偏好也可以保留 categorical transition 的形式：用正的终态权重的条件期望 h，按下一状态与当前状态的 h 比例乘性修正转移，而不是照搬连续 score 的加法引导。Exact 关系要求正确 h、base support、确定的 all-mask 初态与正且有限的 normalizer；[DDoit 的受限实现](https://arxiv.org/html/2610.04938v1)复用冻结模型的 clean prediction head 直接补全未揭示位置，以奖励权重估计 h，并不使这个 head 等于真实 rollout 条件律。有限候选、温度 τ 下省去 P/Q、引导 γ/ω 与终态 argmax 各自改变精确目标，不能因沿用 Doob 形式便宣称任意 sampler 都生成同一条件分布。这里只采用通用离散采样接口，不据领域样本分数引入科学应用效果；head 求值、候选、reward 与逐步采样均计费。支持稀少、近似失准或净质量费用不合时保留原 categorical sampler、较保守引导和真实终态评价。<!-- source-family:SF-2026-ARXIV-2610-04938 -->

拟本人注：`SF-2026-ARXIV-2610-04938` — [exact-v1](https://arxiv.org/html/2610.04938v1)，Daily2026-10-07/Oct6窗，2+2+2=6。categorical乘性h-ratio/head与rollout分责，τ/P/Q/γ/ω/terminalargmax近似逐项不继承exact；reader2 R2-5必要Source/date/owner通过，literal PRE/实际POST另记，未核实现/复现，不采科学应用效果，不授DAY。

## 06394 / Ch23

精确锚点：sceneIR局部04721两段后、“页面表示还需处理异质内容”前；完整sceneIR/Knossos/page邻接已读。

关系推理还可先固定对象身份，再选择供各关系角色共同读取的几何，而不在每次关系问题中重新决定实例位置：维护 persistent instance 的多视图候选，以 identity/category/visible extent 为准则选出一份共享 grounding，再让关系消费者使用它。这是派生表示接口，不是取得独立几何真值。[受限对照](https://arxiv.org/html/2610.06394v1)中的 relation-conditioned baseline 也为每个实例选择一份共享 grounding，故局部差额支持移除早期关系提示/改变选择准则，不能归因成 shared 对比 per-role 独立框。选择与关系仍用同一 MLLM，不能由 relation-independent 名称排除相关错误；小幅组件差额也没有全 harness 三seed的独立显著性授权。多视图/crop、逐候选评分和后续调用均付费，累计 worker-seconds 不是请求 latency；候选漏覆、身份或几何不可靠时保留原图、多视图证据和独立定位核验，不由共享状态代签视觉事实。<!-- source-family:SF-2026-ARXIV-2610-06394 -->

拟本人注：`SF-2026-ARXIV-2610-06394` — [exact-v1](https://arxiv.org/html/2610.06394v1)，Daily2026-10-07/Oct6窗，2+2+2=6；§3–4/D4/E2/E4–5，persistent shared grounding与criterion接口；D4两边都共享，sameMLLM非独立几何verifier，组件显著性/worker-seconds边界近文。reader2 R2-10 Source/date/owner通过，literal PRE/实际POST另记，未核实现/复现，不授DAY。

## 04537 / Ch56

精确锚点：Ch56“HostControlPlane容量合同”原完整两段（含代码）之后、下一现有段之前；局部已完整读，不拆CPU launch饥饿与UMA memory contention因果。

统一内存设备上，CPU 检索还可能与 GPU 生成争同一 memory 带宽，而不是仅让 kernel 发射线程排队。可按离线校准的 prefill/decode caps 控制新检索 admission，并分别记录获准检索调用与仍在运行的 active work；非抢占的检索调用获准后仍须 drain，关闭 gate 不会立即消除争用。[PhaseGate 的受限对照](https://arxiv.org/html/2610.04537v1)中，同 caps 的定时 gate 不能替 phase alignment，decode 切换仍有可测 drain 和短暂 active 超限；high-admission 比例也不等 active-work 超限比例。证据为 M4 等设备上的固定 token 合成 LLM trace 与独立 CPU 检索吞吐，不是端到端 RAG，也未验检索排队尾延迟。Phase信号、调度、检索等待及全部生成费用应一起计入；转换不可信、drain太长或真实SLO未过时保留核心隔离、保守检索caps与独立容量，不由 admission gate 签发硬带宽或E2E保证。<!-- source-family:SF-2026-ARXIV-2610-04537 -->

拟本人注：`SF-2026-ARXIV-2610-04537` — [exact-v1](https://arxiv.org/html/2610.04537v1)，Daily2026-10-07/Oct6窗，2+2+2=6；§2–5/T1–4/A1–5，UMA phase-admission/drain双账，cap≠active/TimeGate反侧/非E2ERAG。reader2 R2-11必要Source/date/owner通过，literal PRE/实际POST另记，未核实现/复现，不授DAY。

## 05748 / Ch54

精确锚点：Ch54生命周期/VMM两段之后、“生命周期还会改变片上Memory的保护成本”前；实际128–145及VMM完整邻接已读。

物理 backing 还可在训练 step 内撤回，而不是等整个 request 或 step 完成：先保留activation slots的虚拟地址，显存收缩时为当前 backing 选择保存或可重算路径，并从 completion 前一层至 dispatch frontier 保护在途 slots，handover snapshot 暂停 CPU 派发并延迟 callback，GPU 继续已派发工作；Tensor Parallel 还需取各 rank 在途保护窗的 union。Re-back 只在 step 边界进行，pinned 或不可重算对象不随意撤回。[MOLT 的受限对照](https://arxiv.org/html/2610.05748v1)因此扩展的是物理生命周期协议，不是任意 checkpointing 自动具备安全回收；completion、snapshot 与多rank状态必须共同成立。保存、重算、映射和调度均付费，以 inference-alone 均值三倍为阈值的 SLO、单run cap 容忍带不是尾部或置信保证，部分 TPOT p95 仍差于比较方案，70B TP4相对 step-level handover 未增加 tuning 吞吐。最终adapter数值质量未证，不能由训练继续运行代签质量；在途状态、重算或实际SLO不可靠时保留固定backing、保守峰值和原checkpoint计划。<!-- source-family:SF-2026-ARXIV-2610-05748 -->

拟本人注：`SF-2026-ARXIV-2610-05748` — [exact-v1](https://arxiv.org/html/2610.05748v1)，Daily2026-10-07/Oct6窗，2+2+2=6；§2–5/T1–2/4.3–4.4/5.4–5.6必要层，step内backing/snapshot/TP union与边界reback，保均值SLO、TPOT反侧、70BTP4对step-level无tuning吞吐增益及质量未证。reader2 R2-12 Source/date/owner通过，literal PRE/实际POST另记，未核实现/复现，不授DAY。
