# 2603.09229：归约输出决定中间矩阵与写回计划

root 作者；supplement_20260312 非作者必要Source/date/具体owner及逐字PRE通过，实际两段已写于Ch49 FlashAttention三段后、monoid前，非writer已顺读新增正文、完整局部邻接和自身末注并回对必要精确原证，POST通过。实际Source/Books处置通过，不授本日完成；独立依据见 [复核](./SUP_REVIEW_09229_CHILD.md)。

[Flash-KMeans 精确 v1](https://arxiv.org/html/2603.09229v1)。实际读取 §3–6、Eq1–3/Algorithm1–3 和有限评价正文；未读性能图像精数、实现或复现。batch3 的完整题摘/current history 和 owning `arxiv.content` /findable DOI实际核：Submitted Mar10 UTC05:54:52不是公开日期，registered Mar11 UTC02:08:30与官方不提前发最终ID/DOI、公告规则夹证同 BJT03-11。Apr v2不回填本日，不做前后无差别比较。当前可见页无撤回/纠错，不宣称全部版本史已核。

2+1+2=5；新增的是在线聚类的归约/写回执行分支，不给关联的所有 LLM 任务加分。已校准的本日名单保留；具体 execution owner 缺口深入到必要方法与数值/成本边界。

## 必要证据与采用边界

§3/Eq1–3保留 Lloyd assignment/centroid update；§4.1/Alg2在每条 point 上维护距离最小值及 centroid index，遍历全部 centroid tiles，而不把 N×K距离矩阵落 HBM。它不剪候选、不减少距离算术；“X/C只读一次”的IO口径只限作者理想streaming，不授全部CTA实际各仅一次读取或bitwise相同。

§4.2/Alg3只argsort轻量 assignment向量，不物理重排X；inverse index使CTA gather原point、片上按cluster segment归约，再在segment边界atomic merge。原文标题contention-free不等无atomic；跨chunk还会拆同簇，需要局部归约及全局合并，O((K+ceil(N/BN))d)是相应merge上界。新增sort、index/workspace、gather及同步费用；空簇n=0、浮点tie和跨块累加/确定性退路未由本文闭合，不据此认定代码bug。

§4.3拆开out-of-core H2D overlap与shape/cache heuristic。§5实际H200/CUDA12.8，比较每iteration/kernel与动态编译，不是LLM请求或完整收敛质量验收。最高speedup来自不同shape/对照，不能拼成统一倍率；B=32并非服务concurrency。precision、固定初始centroid/seed/停止标准、独立重复/CI、服务输入输出长度/concurrency/SLO未披露或不适用，不补造。低IO不证明聚类质量、cache压缩质量、所有硬件部署或总生命周期更优。

## 实际 owner 与逐字 PRE

实际 Ch49 三类基础优化、FlashAttention完整入口及48/50开篇已读；现有attention online状态/monoid和参数聚类压缩不承载assignment argmin＋inverse-map centroid写回这条双瓶颈分支。唯一 `INFER-TENSORRT-LLM`，拟在FlashAttention三段原则解释之后、attention monoid段之前插以下两段。不是FlashAttention后代或改变attention机制；不在Data、KV等处复制。

减少中间矩阵也可以由输出契约推导，而不必改变数学问题。在线聚类若只需要每个 point 的最近 centroid，就不必保存全部距离：按块扫描候选，在片上维护最小距离与对应 index，最后只写 assignment。这复用 IO-aware 原理，不是近似搜索，也不是 FlashAttention 的直接后代；所有候选距离仍要计算，浮点格式、tie 与累加顺序还须单独验收。下一阶段的瓶颈可能从距离物化转到更新：将轻量 assignment 按 cluster 排序、保留 inverse index，再 gather 原始 features、片上按连续 segment 求 sum/count，能把逐 point scatter 改为较少的 segment merge，但没有取消全局 atomic 或所有争用。

[受限聚类执行对照](https://arxiv.org/html/2603.09229v1)支持这种读写路径重组，不证明任意 shape、设备或 LLM 工作负载都受益。排序、索引/workspace、gather、跨块归约、空簇与数值处理都要计费；input 超显存时还需分开核 H2D overlap，动态 shape 则另付配置与编译成本。每 iteration 更快不等收敛质量或完整服务更快，低 HBM 流量也不等 input/centroid 在所有 blocks 中只读一次。小规模、排序费用吞掉收益或数值/布局不兼容时，保留直接距离矩阵、原 scatter 或已验证库实现，分别验收 assignment、最终聚类质量与实际全链成本。<!-- source-family:SF-2026-ARXIV-2603-09229 -->
