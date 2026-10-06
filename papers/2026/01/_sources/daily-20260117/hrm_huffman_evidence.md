# HRM / fixed Huffman — 纠偏后的必要证据与 Books 判断

均为官方 exact-v1，本目录同 ID `primary.txt` 保存原文；normal Submitted cohort/正常公告与 registered 秒精度上界的条件见本日日志，不把提交当公开。完整题摘和具体选择变化已由root校准，必要范围与下述Books终裁已通过；旧“拟”保留推理过程，不控制当前终态。两项均2+1+2=5，不因小模型或反证删候选，未运行artifact/复现。

## 10679 HRM — 设计反证必要深入，拟已有覆盖

原有判断是正确答案附近应达到稳定不动点，进而以Eq5/6支持one-step gradient和更多递归refinement；actual §2.2–3.3显示同模型在近已解Sudoku可先对后错，已给输入clues也未被结构强制保留。仅原困难分布中的稳定输出不证明所有输入固定点。Eq6还有Jacobian近似，稳定输出本身也不证明该近似；不将本文诊断升级为全部HRM梯度无效的定理。

§4.1均值loss随segment改善，§4.2–4.4单例长plateau/突然命中与错误吸引子是不同统计层。§5.1在局部PCA平面/改变初始化观察rival attractor，§5.2 conflict energy只是作者解释假说，作者明确未证明模型实际优化它；合法Sudoku不自动认证保持原clues或解决指定问题。不能由“guessing”标题宣告普遍模型不推理。

§3.3 data mixing局部54.5%→59.9%，§4.5/Table1组合96.9%同时增加9次relabel与10个同run相邻checkpoint的forward；不是独立训练seed、不等matched推理预算。各pass依据ACT是否在depth cap内halt筛选后majority，并非独立task verifier。B3的linear Q-head/epsilon-greedy halt是模型停止决策，不是正确性证明。全预算、serving latency/hardware/precision、重复run与CI在采用范围中Not Disclosed；不以多pass收益认证latent basin因果或普适扩展规律。

可长期保留的命题是首次正确、终态正确、latent稳定与允许停止需分开，错误稳定点与更深递归不保证任务进步。`MODEL-TRANSFORMER-LAYER` Ch17 fixed-point refinement及recursive depth段，实际L582/592/594已直接承载数值/任务gate、首次完成/状态停滞/stop分责及先正确后失解；不是仅主题相似。拟Existing，不声称已写本次实验/augmentation配方，也不因未写9×10 recipe创建gap。root终裁待确认必要范围，Books正文未改。

## 10673 single-stage Huffman — 标准完成，拟仅报告

actual短文§1–4：在线Huffman需要统计PMF、构表再编码及向receiver传表，旧路径在省链路时间覆盖这些开销时合理；改为从past batch平均PMF离线构表、预共享，payload只带table ID和codes。成熟static Huffman原理不计为新编码定律。新增证据是Gemma2B SFT、18层×64TPU的1152 FFN1 BF16 shards，8-bit symbols的所测平均PMF接近各shard，KL<.06，固定表压缩率接近per-shard表。只支持该分布下重用码表的局部可行性。

within .5%/1%是作者压缩率与per-shard/ideal entropy的差距，不是网络加速或通用保证；单shard21.6%压缩不等同比步时节省。其他dtype/tensor只有概述，无端到端collective、decode/kernel实现、die-to-die测量、snapshot跨batch漂移/大模型推断的完整实测。模型identity/阶段/字节与表ID可核；数据集/batch shape/TPU型号/完整timing与repeat uncertainty在采用范围中Not Disclosed。运行分布变化或表失配须重新测，不能把past average当current正确解码或压缩收益认证。

`TRAIN-DISTRIBUTED-TRAINING` Ch36 L1361–1372已要求tensor分布、bit-exact、codec revision、encode/decode/E2E与原collective fallback。本文未证明新的collective执行接口或对该上位取舍的修正，fixed codebook是其局部分支可行性而非confirmed长期gap。因此拟OnlyReport，不冒Existing已含本次统计/压缩实验；保留候选与实际证据。root终裁待确认必要范围，Books正文未改。
