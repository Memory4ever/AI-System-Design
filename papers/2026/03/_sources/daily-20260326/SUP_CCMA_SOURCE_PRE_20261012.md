# CCMA necessary Source / Ch27 PRE

作者supp_mar26_fresh；本日仅03-25。2603.23159v1，2+1+2=5/日期已独校；本包未授Books写入。

实际[exact-v1](https://arxiv.org/html/2603.23159v1) §3.1–3.5/Eq1–10、§4.1–4.5/T1及必要A–E/F/G/H/T2已读。只拟采用两模型label-support union上重归一比较JS、再与student entropy混合并在高分候选内做coverage selection这条控制接口；不是teacher伪标签真值。冻结CLIP ViTL14 class prototypes和DINOv2g14特征、冷启动每轮重训head，20轮/5seeds/每轮B=classes；目标teacher平均3/student平均5、κ20，AdamW lr/decay .01/dropout .75。特征一次提取cache、所有calibration/cluster/scoring/标注/每轮训练都计费；GPU/precision/batch/concurrency/SLO Not Disclosed，query秒非总费。

## 必要正反侧与中心桥隔离

§3.3 119–122把经验coverage quantile/size targeted混讲并声称finite guarantee及shift robust；E 341–355实际固定mean setsize、每轮重新threshold，coverage .90–.95/.85–.90是作者经验陈述非定理。平均集合大小目标不约束真实标签是否在集合中：所有样本的真实类恰好永远排第4，固定前三support大小3却coverage0，为直接反例。coverage-directed分支也未披露有限样本修正quantile与adaptive calibration/test exchangeability条件；disjoint split不足以证明shift或反复选择后的保证。不采该中心可靠性桥，但union-support disagreement的独立定义及局部选择取舍可采用，不整体HOLD/EX或降5分。两集合同空时Eq5归一分母0，原文未披露fallback，不补成已核实现。

T1 CIFAR t4 BADGE/pBALD更高、Food t4 ProbCover更高，Caltech later mismatch消失时普通coverage/uncertainty更好；confidence gate仍使用raw top1，其归一比不是correctness校准，JS有上界而entropy随类数尺度变化。H T2 V1 AULC .859/time3.015 vs fullpoolV2 .828/.780、randomsubpoolV3 .835/.512；子池不是普遍更快，不同模块仅局部消融，不授相同backbone即唯一完整因果。G DomainNet κ10最佳与统一20不同，τ正文方法.03与消融.30分责。I基线曲线不足仅必要读398–403排除无限迭代基线无能力误解，未逐图所有architecture附件。

## actual owner / gap / 锚

sole TRAIN-DATA Ch27，actual完整1125–1168在线selector、synthetic课程、proxy内环链已读，及26/28开篇交接。已有checkpoint-coupled controller保feedback bias与heldout，但不承载两模型support-union JS、mean setsize与coverage保证分责及候选内diversity的具体接口。拟在05227 online weighting完整原段/其source marker之后、下一“若既有难题池的成功奖励几乎为零”课程段之前插入两段，不移动旧段/不新增收纳节；待reader实际Source/owner/PRE与root锁。

## PRE paragraph 1

在线选择也可以让视觉语言 teacher 与当前视觉 student 共同提出标注候选，而不是把 teacher 的最高分标签直接当正确答案。一条受限分支分别按两模型分布构造 label supports，在两集合的并集上重归一概率、比较 JS disagreement，再与 student entropy 混合排序；高分候选还须经过表示空间的批内 coverage 选择，避免把一批相似难例重复送去标注。这里集合大小、两分布差异与样本覆盖是不同控制对象，最高概率的 confidence ratio 仍只是混合权重，不提供正确性或教师可信度证书。<!-- source-family:SF-2026-ARXIV-2603-23159 -->

## PRE paragraph 2

[必要原证及反侧](https://arxiv.org/html/2603.23159v1#S3)的实际实验固定平均 support 大小，而非按真实标签的非一致性分位数取得有限样本覆盖保证；平均保留几类与真实类是否入集合没有必然关系。校准人口、每轮选择造成的分布变化和空并集归一须另验，不照录其分布漂移下的可靠性承诺。有限冻结特征实验中，teacher–student差异消失后普通coverage或uncertainty可更好，精心聚类的子池也比full-pool或random-subpool变体更慢；因此分别测选择质量、标注量与净费用，不把一项局部准确率当全链路加速。特征提取与cache、阈值、聚类、打分、标注和反复训练均付费；代理漂移、并集无效或预算不合适时，保留随机/分层采样、普通单模型uncertainty及独立held-out验收。

## 自身静态证据注 PRE

SF-2026-ARXIV-2603-23159 — [CCMA exact-v1](https://arxiv.org/html/2603.23159v1)，必要§3–4/T1与A–H相关校准/协议/T2；仅采用support-union disagreement→diversity控制接口，隔离mean-setsize≠coverage guarantee及shift/adaptive保证，保teacher退化、子池时长反侧与全费用；未核实现或复现。
