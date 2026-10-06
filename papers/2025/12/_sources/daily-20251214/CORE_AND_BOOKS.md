# 12/14 必要局部与条件Books判断

作者Gibbs，2026-10-02实际原站读取；本次具名修正定点复用Mill已实际exact-v1必要层并明确标注。以下不是全84项Evidence完成。所有家族first-public仍未授；不进入Books，草案仅交root协调，待日期恢复和非作者证据核验后决定。未运行代码或实验。

## WATOS — TRAIN-PIPELINE-PARALLEL

[2512.12279v1](https://arxiv.org/html/2512.12279v1)实际§II–IV-B、IV-B完整GCMR/Algorithm2、IV-F、V-A/C/D、VI-D/F。1F1B下各stage activation驻留不均，global DP联合recompute和memory allocation，以最大stage成本为目标；Sender过量activation checkpoint借Helper空闲容量，经on-wafer D2D，而非CPU offload。Evaluator是修改AstraSim及memory/communication模型的离线策略搜索，7nm/2GHz/FP16架构模板，非真实wafer训练部署。

V-C/D的naive/co-designed WSC同时改变硬件和策略；8 Blackwell Ultra基线、scaled GPU memory对照不能把2.74/1.53倍授为单算法因果收益。正文equal-memory-bandwidth 2TB/s与intro图8TB/s不能混用。小模型gain与大模型memory约束不同；故障部分20%link/die注入是模拟，不授实际MTBF。

实际对读Ch38 75–112：GPipe checkpoint/recompute与1F1B缩短activation生命周期；130–235解释interleave/异步与通信。Ch37 55–135、225–270讲TP layout/collective/topology；Ch39 20–70区分model-state与activation，Ch36 25–85保留state/ownership成本。现有具体段落承载旧调度和重计算理由，但未承载Sender/Helper跨stage容量分支，不能把整篇写已有覆盖。

条件局部草案，插Ch38 1F1B生命周期段后，不改相邻owner：

> 缩短activation驻留不保证每个stage都能独立装下checkpoint；当片上通信快而各stage容量利用不均时，另一个选择是把重计算、stage内存预算和跨stage checkpoint搬运联合规划。空闲stage容量可作为Helper承接Sender溢出，但global剩余容量不能直接替代局部可行性：搬运与取回须加入critical-path成本。该分支仅在拓扑、容量和调度可联合控制时合理；通信变慢或恢复成本超过重计算时，局部checkpoint/recompute仍是有效路径。

最后两句是由机制推出的工程验收边界，不冒称论文实现了全部恢复/故障协议；不采用模拟倍数。

## V-Rex — INFER-KV-CACHE

[2512.12284v1](https://arxiv.org/html/2512.12284v1)实际IV-A/B、完整IV-C WiCSum与式1–3、V-B、VI-A/E和TableII。RoPE后keys经random-hyperplane bits/Hamming cluster；cluster代表只用于ranking，真正Attention仍读取原KV token。WiCSum按cluster token count加权score，总mass乘ratio门槛，排序累计到门槛后经HC table展开原token；动态每layer/head token数，不是lossless/fixed-topK。

新增HC维护/选择引擎和下层prefetch均有成本。VI-A custom cycle simulator结合DRAMSim3/MQSim及A100/Orin带宽，14nm RTL synthesis/pre-layout STA不是tapeout或实机FPS；energy包含估算/厂商参数。Llama3-8B/SigLIP条件TableII平均accuracy降0.8%，不能授准确率不变或任意视频工作负载。

实际Ch45 150–215已解释低维RoPE selector只负责提案、host index/bulk搬运及fallback；210–285含state provenance、token-hit与E2E不等价。Ch44 25–65、Ch46 25–60分别约束decode依赖及iteration资源。已有覆盖的是选择器/执行/一致性分责，不是此次streaming cluster和weighted动态门槛。

条件草案插Ch45低维selector论证后：

> 流式视频可以用随帧更新的key聚类降低选择成本：代表key只排名，候选cluster按其token数量加权累计score mass，再取回原KV。这样门槛决定每层、每head的可变读取量，而不是先固定top-k。近邻帧相似性与质量容差仍是条件；必须把hash/cluster维护、选择、稀疏搬运和miss fallback计入完整路径，不把减少fetch token直接等同端到端收益。

## MixtureKit — MODEL-MOE

[2512.12121v1](https://arxiv.org/html/2512.12121v1)实际§3.1–3.2、完整§4/Table1、§6。BTX/BTS引用已有算法；具体工程增量是shared参数shape-aware合并、expert namespace、复制HF modeling/config并用regex patch forward，让router/stitch不同路径共用compose/save。HF兼容不授近期vLLM MoE kernel兼容，§6明确版本/结构依赖和跨架构future。

Table1的2x4B-A6B/3x4B-A6B都active6B，与dense4B/12B不是匹配参数/compute控制；Arabic/Latin并非全赢，LoRA/SFT/DPO与WildChat混杂，不能推出新的BTX算法优势。

实际Ch21 140–215讲dispatch/capacity/EP/grouped GEMM及active不等成本；210–280的compute leverage、total/active预算和shared checkpoint+profile+kernel/placement contract，Ch20/22 25–65说明采样与长序列成本。已有正文可以承载active参数不等实际可执行成本，但没有专家checkpoint组合到patched forward再到kernel这条交付边界。

条件草案插Ch21部署身份段：

> 专家来自分别训练的dense checkpoint时，组合产物还要明确shared参数合并、expert命名/shape和router或stitch forward。能保存为某个模型接口的checkpoint，只证明该接口可装载，不证明高效MoE kernel识别其结构；模型配置、patched代码和executor支持范围要共同成为部署身份。版本变更或不支持的专家结构下，应保留原dense或已支持的组合路径，而不是从active参数推断可交付收益。

## 必要负面/安全边界

[RAN12400v1](https://arxiv.org/html/2512.12400v1)完整III-B/TableII：4个OAI文件×3次；No-RAG三模型accuracy .58/.67/.50，普通RAG .25/.17/.33，Agentic RAG .75/.83/.67但latency54.12/109.7/126.41相较31.1/37.95/55.84增加。所有BERTScore>.85仍可能规范ID错引。保留局部检索/正确性评价反证，不采autonomous enforcement或通用RAG排序。

[Neural Chameleons11949v1](https://arxiv.org/html/2512.11949v1)作者原读完整§3.3、§4.1 ensemble/nonlinear边界、§5.1：post-hoc在最终冻结checkpoint无trigger训练监测器，clean data固定1%FPR后测triggered TPR，三seed/95%bootstrap；更强监测器缓解非消除。此次复用Mill实际§3.1–3.3/4.1/5.1纠正原漏条件：主模型为**helpful-only/abliterated organism，移除原安全拒答**，安全训练版本属于另附录条件，不与主协议合并。Gemma2-9B/2B、Llama3.1-8B、Qwen2.5-7B为人工organism；自然RL或环境trigger出现仍future。安全负侧不删，不授真实部署普遍攻击、自然欺骗或所有监测无效。

## Mill §4六项机制恢复与12500必要协议校准

本轮完整读[INDEPENDENT_REVIEW](INDEPENDENT_REVIEW.md) §3–4，定点复用同身份/窄命题的实际原源层：RAST13727 §4.2/§5.3–5.5/Table1；EEG-DLite12210 Method/Algorithm1/Tables1–2；MRINE12462 §3.2/§4.3–4.4/§5；M4Human12378 §3.2–3.4/§4.1–4.2/§5.1 Tables2–3；EnviroLLM12004 Method0.5/Results Tables1–3/Limitations；DreamRAM12106 III-B/C/IV/IV-C与Appendix。具体原约束/新机制/反证与原误判保留在ADMISSION七项重开表，不重读未变整篇或扩库存。六项恢复potential/datehold，不授标准/深入完成：mask/pool/reward失配、数据蒸馏比例、time-invariant缺模态动力学、split/表示成本、估算power/judge限制、硬件预测/cell/RowHammer条件分别保留，不采用领域诊断或模拟生产结论。

[12500v1](https://arxiv.org/abs/2512.12500v1)原皮肤科题名关闭已撤销。旧HTML失败/官方PDF工具400保留为访问历史，**不再是当前正文缺口**：复用[Mill §7–8](INDEPENDENT_REVIEW.md#7-2229-有限补核12500原文恢复)实际[官方export精确v1 PDF](https://export.arxiv.org/pdf/2512.12500v1) HTTP200、25,900,642字节、98页中的必要原文pp1–4、7–9、12–13、16、29–31、51；不冒称作者重新打开或全98页语义阅读，不读外部数据/代码或授复现。

pp3–4协议是623 lay participants与153 PCPs、每人12图、两轮、四种XAI×两种顺序的随机between-subject设计；两群体任务不同，不能将跨组差异归因于expertise。同任务320 medical students是另一个对照，不并成同任务总体。p29/STable3 p51先由另一模型给定诊断（含错误标签），再让GPT-4V只解释而不重新诊断；prompt只列确定理由并禁止拒答，不是独立verifier。p16 single-pass无选择/修整，特定prompt、自信措辞和随机性仍可混杂。

p8 Study1错误AI时，LLM解释相对Basic使准确率退化更大，difference-in-difference `beta=-0.048, 95%CI=[-0.093,-0.003], p=0.035`。窄potential是合理化文字不验证上游决定的局部反证。直接反边界pp12–13：**最终第二轮Human-First/AI-First准确率无显著差异**，部分总体deference比例及不同XAI间比例差异也不显著；不能写成所有解释有害、AI-first普遍降低最终准确率或专家免疫。p16的12图/人、在线简化、缺患者上下文及特定模型/XAI/prompt限制也不支持临床采用或其他任务的普遍规律。

该项必要原文层已校准，仅first-public hold；Mill §8所见v1 Submitted原值`2025-12-14T00:06:06Z`不授公开或落窗。撤销旧核心协议请求，归入84项统一日期恢复条件；不评分、不进入Books、不支持覆盖或使用安全保证。其意义限于解释与验证的评价边界，不能因领域题名删除安全反证，也不把本次局部校准授为全84项Evidence完成。

其余潜在家族只完成准入题摘，不借上述局部授全体Evidence。日期恢复后按各自真实贡献评分/最低审阅投入，只重开对应家族；此时不制造Books已落实。
