# Sparse packing23198 — 必要Source / 两PRE

作者supp_mar26_fresh；25门/2+2+3=7首校通过。实际exact-v1 https://arxiv.org/html/2603.23198v1 §2.2–4.3/Eq1–4/Alg1–3/T1、§6；为必要capacity/数值边界定点A.1文字、B.1/T2、B.2.1 overflow，非全CUDA附件/代码复现。Node第二必要fetch12s timeout已以官方HTML定点恢复，不当外部故障或Evidence空缺。

## 原证与反侧

ReLU gate+L1训练形成activation sparsity，并非参数pruning；原dense SiLU artifact不自动改该执行。TwELL按CTA输出tile局部存非零value/index/count，匹配gate GEMM epilogue无跨CTA整行packing；随后gate模式驱动up元素求值与down累加融合，不先物化整份up。Training因dense-tail/反向驻留另用hybrid行级ELL+overflowdense、transpose/masked gradients，up/down分开并非全部同fusion。A.1 16bitvalue/index打包32bit、shared-memory/TMA/WGMMA与保守C，不能由平均nonzero授maxperTile capacity；B.2.1 forward/backwardtranspose容量不同，实际超量先discard excess、设flag到nextGPUsync，再increase sizes/repeat latest optimizationstep的系统响应建议，不授已实现完整rollback/正确checkpoint事务。

从头训0.5–2B FineWeb/GatedTransformer++、8H100PCIe/BF16、2048seq/global1048576tokens/AdamW、10.49–41.94Btokens；固定seq但microbatch随HBM可用空间改，2B最大microbatch变化与速度共同取舍，不matchedbatch所有变量。T1 0.5B training−1.5%，1.5/2B taskavg46.2<46.4、48.8<49.1，2B memory57.1>46.7（+22.3%）反侧；不能照录allsize更快更轻或无损。L1过强/活跃<.5%质量损失，per-token/layer最大nnz比均值order高；相关−.996不是语义因果。Forward input-token/ms不是decodeTPS/TTFT/多租户SLO，energy pertoken仅受测操作点，稀疏训练/格式转换/metadata/retry/回归费用均计；把dense既有模型finetune稀疏是future work，未授当前任意checkpoint通用。

## actual owner差额与交接

实际Ch49 112–148数值commit→loop placement→parallelannotation→融合/layout与PolyCIM最后完整两段已读，以及140–173到launch/persistent链；已有『稀疏需编译搬运/不规则会抵消』通用原则，未拥有gate GEMM epilogue局部tile packing→gate模式融合up/down与训练hybrid容量重试的具体数据流。实际Ch48/50开篇和Ch16开篇FFN只负责形成/非线性语义，L1训练条件作必要交接，不第二owner或重复Ch16稀疏章。sole INFER-TENSORRT-LLM Ch49，拟PolyCIM完整两段之后、“从逐Kernel Launch到Persistent Executor”标题之前两PRE及自身注，保原dense/GEMM合理边界，不建论文收纳节。

## 两段逐字PRE（未写）

不规则稀疏要兑现收益，格式生成就必须跟上 producer 的粒度：若 gate GEMM 的各 CTA 只产生局部输出 tile，整行 ELL packing 需要另一次全行扫描或跨 CTA 协调。一个执行分支改为在 epilogue 内按 tile 保存非零值、原列索引与计数，再以 gate 的模式只求相应 up 元素并累加 down 输出，避免先物化完整中间张量；训练则为反传驻留改用行级 ELL 加 dense backup，分别处理 forward、transpose 和 backward。稀疏由 ReLU/L1 训练形成、格式由编译执行消费，这是两道资格，不让已有 dense/SiLU checkpoint 自动继承该计划。<!-- source-family:SF-2026-ARXIV-2603-23198 -->

[受限 H100 对照](https://arxiv.org/html/2603.23198v1#S3)仍有小模型训练更慢、质量反退及大模型 micro-batch 改变后显存更高的切片；平均很稀疏不能保证每 tile/row 或转置后的最大容量足够。原文说明超量会先丢弃 excess 并在下一同步点报告，允许系统扩容量并重跑最近优化步；但实际恢复闭环未披露，实现必须另验污染结果不能被静默提交、状态恢复与重复步是否正确。索引/计数、packing、dense backup、transpose、同步重试及训练回归都有费用，forward input-token throughput 也不认证 decode 或 serving SLO。模式、容量或净质量—成本未通过时，保留 dense GEMM、保守容量和原训练路径，而不以 activation 稀疏率签发无损、免费或任意模型可移植保证。

本人静态注拟：`SF-2026-ARXIV-2603-23198 exact-v1 §2.2–4.3/Eq1–4/Alg1–3/T1/§6与A.1文字/B.1–2.1；只采用tilepacking→gate模式fusion/训练hybrid数据流，overflow discard/flag/retry需另验commit恢复，非已核代码；保quality/0.5B训练/2B显存反侧和microbatch/全费/硬件边界，不采任意dense兼容或decodeSLO，未核实现/复现。`

必要Source/actualowner/PRE与本人注纠错后已真实独核PASS（reader§13）；仅原文允许capacity响应重试，不授已实现恢复闭环。待root具体窄锁，无书写/POST/DAY。
