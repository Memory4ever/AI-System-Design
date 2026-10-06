# 01-16 / Relational Hoare HLS 必要原证与owner差额

后续实际状态：root必要原证/actual owner PRE通过并授窄锁；作者已写Ch49两段94/96及自身末注2787并顺读83–115；root非作者实际独读83–115完整邻接/新正文及自身末注POST PASS，Ch49锁释放。下文“待PRE/拟写”保留原提案过程，不是当前待办。不授日级Gate/实现/复现。

等待root独立题摘准入/必要原证/owner PRE；无Books写入或锁。exact-v1 abs09217.txt L19–45完整题摘/extendedESOP2026说明，html09217.raw §3.3 L1649–1722、§4 L1723–1859、§5 L1860–2726。normal Jan15公告下界＋registeredJan15T02:40:53Z公共存在上界条件限定Jan15，非registration=firstpublic。SubmittedJan14T06:43:43Z只发现，v2存在未作重要rev或回读；当前abs/HTML无直接作者project早正文发布信号，不扩ESOP全部论文或历史。

## 决定性增量

已有HLS compiler只识别特定顺序语法来burst；原文不只重排loop或加pragma，转换关系保留array值与producer/consumer索引访问序列的对应，插入on-chip reuse buffer去掉重复offchip读，再在访问序列可对齐时改array成stream，host同样需配合。变量/readonly-writeonly array、buffer和访问顺序进pre/postcondition，VC+invariant约束给翻译许可，不能验证就留array。新增可保留机制是访问protocol成为内存变换的验收对象，改变仅凭source语法/带宽proxy选择buffer/stream的边界，不因FPGA标签或缺显式LLM任务排除。

作者已实际读intro、§2语言边界、§3.3主文state relation/模拟声明、§4.1–4.3及§5.1–5.3/Table1的相关行。形式化 source以整数/无相互alias的array及readonly/writeonly区分；主文simulation在相关states/translation premise下，不能外推任意C/C++、floatingpoint、concurrentGPU、实际有限FIFO deadlock或所有backend。主文定理首方向出现u而前提为t，未采用该式为可执行证明；没有声称已独立证明全部0.A附录。拟仅采用access-sequence/验证接口，非重新授普遍编译正确性。

自动实现比形式化窄：恒定平移index ranges、linear loopvariable模板，反向/重叠/stride可表示，但column-major A[j][i]等不支持；VC不能成立则放弃部分stream replacement。不把‘可加user invariants未来’写成实现。不是所有内存布局/alias或动态控制均已处理。

## 对照、费用与反側

KriaKV260真实FPGA；Z3 4.11.2、VitisHLS/Vivado2024.1、PYNQ CPU host/DMA，DSL转C++＋directives。MachSuite样本手工简化适配DSL，不授任意input自动；StreamHLS等inputmodels不同不能自动配成matchedbaseline。测kernel execution非host+DMA/allrequest lifecycle，总compile/synthesis/solver/BRAM预算仍须计；每程序translator<1s不含整流程。重复run/不确定性、integer宽度/clock与全pipeline延迟Not Disclosed。

Buffer使Filter族复用/顺序burst；已有顺序Divide/MatVec/MatAdd/KMP/SpMV无收益，GEMM另一矩阵非线性仍瓶颈。Reverse MatVec不支持stream，KMP/GEMM其他瓶颈故无改善；Skip部分路径为burst传更多unusedwords而更快，不能让少bytes代签性能。buffer+stream BRAM增加，2Dfilter/stencil linebuffer明显，Table1power作者表不代实测全系统电力。已有sequential/burst、验证/资源失败保原array/manualHLS路径。

评分拟2+2+2=6；具体access-sequence/buffer和stream许可差额深入受影响core，未把通用Hoare原则算新分，未运行代码/复现。若采用具体证明算法需进一步定点0.A/实现，此提案不采用完整proof recipe。

## Actual owner 与拟两段

已实际读Ch49 L80–105：source-to-source lowering→numeric+workload commit，具体compiler/CUDA纠错、RTL backend与PIMloop粒度，已承载语义需验收一般原则；还未有buffer/stream改变producer-consumer访问protocol及增加搬运却恢复burst的具体分支。owner INFER-TENSORRT-LLM，不扩Ch36通信或创建compiler收纳章。拟在Lowering第一段/source marker后、CUDA纠错前两段，待root PRE/锁。

数值结果相同也不意味着同一个内存访问protocol：重复、倒序或跨步读写，在已有HLS后端可能无法触发burst。一个受限转换分支把producer/consumer的索引序列、buffer保存的值和stream先后关系写入pre/postcondition，先插入复用buffer消除重复off-chip读，再仅在对应访问可验证时把array替换为stream，并同步修改host数据交付。这把‘能否替换’从表面loop语法变成协议关系；[Relational Hoare HLS的受限接口](https://arxiv.org/html/2601.09217v1)不由形式化名称授权任意C++、浮点或并发GPU程序，验证条件不能成立时仍保原array。<!-- source-family:SF-2026-ARXIV-2601-09217 -->

当前自动化只覆盖受限linear访问和loop invariants，column-major等模式仍不支持；buffer增加片上容量，stream与DMA也可能为恢复burst多传unusedwords。真实FPGA的小kernel对照有改善，也有原顺序/GEMM其他瓶颈无收益，故bytes下降、形式化许可和最终artifact性能分别验收，solver、host/DMA、综合、BRAM与完整执行费用都需保留。访问/alias条件、有限FIFO或目标backend未验证时，保留原array、手工HLS与已测kernel；只把可证的protocol变换交给后端，不以作者的抽象state模拟取代实际硬件与LLM workload回归。
