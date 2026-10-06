# 2026-01-30 第四批必要证据（root必要命题/反侧实际复核通过）

以下保留作者首审时的潜在Books描述；mmICL已实际Ch23窄整合并非作者POST通过，其余Only。最终处置与日级边界见本日README，旧‘待比较’不是普通未完成工作。

仅精确v1；不运行artifact/不称复现。日期包络见报告和原字段。以下物理行指对应V3_CORE_2601.ID.txt。

## [QAD / 2601.20088](https://arxiv.org/html/2601.20088v1)

2+2+2=6。§3 110–141/192–296，§4 330–454：固定原BF16 teacher，量化student以KL回配参考分布，避免在已多阶段SFT/RL/merge的权重上继续labelCE破坏原能力。Nemotron49B/.3B tokens/5k heldout8M tokens，BF16与QAT CE同.408但QAT KL.311，QAD CE.416/KL.004；验证labelCE不足确定行为恢复。单SFT Nano12B局部QAT可与QAD相当，不称QAD总优。RL-heavy Nano30BA3B/Ace7B冷启动SFT+RL，QAT局部甚至落后PTQ；并非随机teacher会恢复所有能力。保留部分attention/Mamba BF16/KV FP8，不是所有算子NVFP4。训练.3–6B tokens、lr/教师选择皆依产物，取validation最低10checkpoint再按benchmark平均选择，存在基准选择偏差；AIME/LCB/GPQA/IFEval的多采样和temperature不同，不跨协议直接比较。硬件成本Not Disclosed，SLO不适用。仅报告：这些特定产物多阶段目标保真与budget边界，未授所有低bit无损或全部hidden knowledge恢复；若拟改Ch49须核实际teacher目标差额。

## [HESTIA / 2601.20745](https://arxiv.org/html/2601.20745v1)

2+1+2=5。§3 128–239，§5 582–608/722–784：ternary soft assignment渐进退火；Hutch++ Hessian log trace产生层敏感度并离线冻结，调温度，不是online Hessian feedback。Llama3.2 1B/3B、10B UltraFineWeb、seq1024、group128 weight-only、全精度activation/其他参数、AdamW、5runs均值。软连续主机制贡献大，增加Hessian调度的精度增量仅1B .540→.547、3B .599→.601；不能把全部增益归Hessian。基线有原论文数值而非全同栈重跑；其他模型/2bit局部结果不证明任意LLM普遍收敛。离线校准成本无数字、硬件Not Disclosed、SLO不适用。仅报告：低bit局部退火配方/小增量，不在成熟mixed-precision原则外强建长期缺口。

## [OnePiece / 2601.20655](https://arxiv.org/html/2601.20655v1)

2+2+2=6。§6 516–696、§9 764–777及conclusion811：one-sided RDMA可变消息，经CAS producer spinlock注册buffer/size环，busybit由consumer释放。短timeout解锁后旧producer可覆盖新数据，header checksum丢坏消息；证明只到环遍历，不到valid payload，且假设consumer不故障。§9丢消息不重传，称interactive user不等待；可靠delivery是可扩展但未实现，不能写exactly-once或lossless。v1正文未提供可比实验setup/table；intro称16×而结论称16% GPU降低，分母/workload/hardware/端到端成本Not Disclosed，不采用正面性能数字。仅报告：registered-buffer生命周期与有限liveness设计，不将注册地址擅称GPU驻留，性能/可靠性未授。

## [Multimodal ICL / 2601.20796](https://arxiv.org/html/2601.20796v1)

2+2+3=7。§2–4 91–260；A1 523–549、A3.7 689–711；135–145：2-layer RMSNorm/SiLU/RoPE decoder，GMM N8/L1=32/L2=16/D1=64/D2=32/eps.1，primary8192 vssecondary256类，B4；ICL query必须有同类exemplar，新类与label-swap分离IWL/ICL。SGD128 lr1e-3/wd1e-6到收敛（非fixedcompute），5seeds std<.03。先M1再joint M2 MLP增加alignment capacity可能避IWL捷径；更大单模态反而捷径。RoPE低复杂度反例不能外推一般多模态：highcomplexity N8各positional近满分。prev/induction头ablation .97→.199/.062，因果限该2层。去M2 .336、去M1 .063，非M1单用。earlyfusion从头共同训练[M1,M2,label]使邻label的M2主导，primary不是固定text身份。真实Qwen/IDEFICS观察有架构/数据混杂，§4.4.4不提供生产机制解释。仅作者必要深审完成；Books判断待实际Ch23课程/sequence geometry差额，不先自动OnlyReport或因名字新就改书。

## Policy of Thoughts 定点符号限制补充

2601.20379v1 §4.4 164–168称minimize Eq9，但正文式是正PPO clipped surrogate减βKL，未给整体负号；§2 112称maximize GRPO，835–845只有超参，无另一loss约定。该符号/实现未核，不声称理论/代码正确。不再泛读代码/其他版本；原局部作者结果与episode临时adapter边界仍可仅报告。FAEA、SATA、T-Mimi原有限证据已获root Source复核通过，均不自动授Books。
