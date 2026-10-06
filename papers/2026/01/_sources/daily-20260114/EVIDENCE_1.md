# Jan14 必要证据批次 1（作者审阅，未授日级完成）

## 2601.07600v1 — Peformance Isolation for Inference Processes in Edge GPU Systems

原分2+2+2=6，实测反证触发受影响内容深入。exact HTML `https://arxiv.org/html/2601.07600v1`，原返回CORE_2–5。已实际核§III MPS/MIG/GC机制、§IV-A1/2配置、IV-B batch1与指标、IV-C/Alg1 IMS定义/验证及§V-B/C/D，VI仅必要结论。不运行代码/复现，不采用作者将MPS称unifiedcontext或将观测归因contextswitch的实现断言。

采用命题：SM计算分割不自动隔离共享功率/频率，孤立测出的有限最大稳定频率不能当worst-case deadline证明。A10040GB/CUDA12.1/PyTorch2.4.1，JetsonNano/AGX JetPack6.2、TensorRT转换模型，六ImageNet分类模型、不测accuracy，不能跨平台/不同backend以绝对速度判技术因果优越。IMS以首1000推理中最差5次均值初估、提高直到violation、退回并验3×1000批；并发受测对象运行其孤立IMS，另一方提高load，timeout是分配周期内未完成。这是有限profile、不是WCET证明；warmup/precision/输入分布/运行重复置信区间未披露，不授安全应用保障。

直接反侧§V-D：Nano两模型共置下频率约减半，接近20W cap，是作者有trace支持的解释而非单变量power因果干预。AGX保持每进程4SM/1.02GHz而提高powerheadroom与内存带宽等硬件，timeouts显著下降但非只power变化；四process GC4×4SM又有模型/机制差异。MIG某large-model高IMS也有timeouts，不能将硬件分区等同全部时序保证；更不能宣称GC本身失效/无隔离或AGX普遍近MIG。LLM/KV/SLO未测，不泛化六分类样本为生产Serving。

actual owner对照：`PLATFORM-GPU-SCHEDULER` Ch63 sharing表及splitter→fault-domain段（约155–173）分计算回收、地址/故障隔离；powerbudget段和共享powercap训练段（约231–240、278–280）分功率配置/遥测和共置反馈。但sharing节尚缺computepartition≠power/frequency isolation及profile timeout≠hard timing contract的直接衔接。root实际必要原源/owner核通过并授权窄锁，已在sharing表后、kernel细分前Ch63:165写入1自然段及359源注；只承载这一缺口和监测/对照/保守headroom、降并发/独占回退，不添加未核官方GreenContexts API保证。root已实际顺读154–175与353–365，非作者POST通过；源注同步，锁释放。这是单篇实际整合，不代表Jan14日Gate。

## 2601.07372v1 — Conditional Memory via Scalable Lookup

原分2+3+3=8；必要机制/关键评价/反侧已实际深入，但**日期尚不放行**。exact HTML `https://arxiv.org/html/2601.07372v1`，CORE_2–5保存实际原返回；另§2.4与§6.2补段待保存。三类容量不混同：NFKC/lowercase canonical IDs只用于模型lookup地址，不替输入tokenizer；2/3gram多head hash表concat→Wk/Wv→hiddenquery RMSNorm sigmoidgate→causalconv残差，表与value共享于mHC四branch、key/gate各branch独立。gate并非语义正确性或安全校验；hashcollision/多义仍需训练/quality验收。

地址由已有token序列决定，因此可在使用层前prefetch；hiddenquery决定采用强度，不决定地址。训练GPU表sharding用AlltoAll读取/反传，推理hostDRAM PCIe overlap前层。早插入收益与query上下文不足、晚插入更大overlap窗口是同一placement取舍；层2/15仅作者配置不是通用最佳。HBM/DRAM/NVMe层级为设计建议，实际§6.4测试仅dense4B/8B+第二block100B表全DRAM，H800、512sequences、长度Uniform100–1024、nano-vLLM harness，未包含MoE ExpertParallel，precision/输入输出长度拆分/尾SLO/host硬件与重复不披露；不能用这组throughput保证复杂host-cache路径无代价。

§3保持total/active预算与约10×sparsity两个compute规模，局部U形rho75–80%不是普遍比例；§4参数/active262B tokens对照、embedding单独Adam5×lr并非所有参数同optimizer，40B不iso-total且若干任务下降。§5所有模型额外YaRN32K/5000steps30Btokens，iso-loss不等同相同checkpoint能力；表2S/CWE部分退步不能声称allmetrics。§6.1 LogitLens到finaldistribution的KL与实体末token FewNERD CKA/top5重心是相似性proxy，不证明层功能因果等价、真实depth节省或真值。§6.2同表budget部件/层位置ablation支持训练耦合下的局部选择；§6.3直接移除表破坏train/inference合同，不授全部knowledge唯一在表；§6.5手选最semantic-correlatedgate不授全branch可解释。代码仅demo且mock Attention/MoE/mHC，不声称full实现/复现。

日期：原SubmittedJan12T09:54:49Z、UpdatedJan13T02:13:41Z、createdJan13T04:01:14Z、registeredJan13T04:01:15Z；noadvanceID+正常Mon公告可定arxiv版本条件区间[Jan13T01Z,04:01:16Z)。但officialrepo initialsha7299…Jan12commit对应README已含同题Engram_paper.pdf+同机制，仓库created/commit不是public日志。最早外部PR1 Jan13T03:47:53Z只给公开上界、不证明更早不存在。**全球first-public归属有实际提前项目线索，先隔离这一采用日期，不能把注册区间当全部正文首公开**；精确恢复仅作者首公开记录/当时可公开repo事件，不无限archive。

owner拟`MODEL-MOE` Ch21 capacity/sparsebudget段后（约231–250），其total/active与computeleverage尚未分条件计算和静态地址容量。Ch16 MLP非事实表、Ch22 memory读取边界可作为交接，不并发复制完整机制。若日期过且root核支持，拟最多两自然段解释token已知lookup与hiddengate职责、稀疏budget分配/placement与访问成本；不授普遍rho/模型实际depth或硬件SLO。未申请写锁/未写Books。
