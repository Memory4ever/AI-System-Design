# Oct21 四具名旧关闭重开提案

范围见 [SCOPE](./SUP_SCOPE_20261015.md)。原 66 身份读取分母不变，不改原 SCREENING/FIRST/FINAL；以下是本轮具体理由修正。root 通过内部协调确认四项原件必要域实际校准为窄 P，持久记录见本日 [SUP_INDEPENDENT §2](./SUP_INDEPENDENT_20261015.md)；不授日期/评分/Books 或整日 DAY。内部转交不是人类用户批准，本人不改 root 文件。

## 1. LaGAT 2510.17382v1：C → 窄 P，实际校准通过

原[abs v1](https://arxiv.org/abs/2510.17382v1)本次实际读完整题摘/history：只有 v1，Submitted 2025-10-20 10:19:35 UTC；这是提交，不签首公开。没有可见 comments/journal 更正信号。原 Atom 当前亦 v1，复用 root 本轮完整 AB 读取层。

本次实际保存并读 [exact-v1 HTML](./SUP_17382v1.html) §2.2/2.3、§3.3/3.4（含 Alg1/2）、§5。请求 `https://arxiv.org/html/2510.17382v1`，HTTP200/330188 bytes，retry0/20秒上限；未读完整附录证明，不作逐式证明认证。

具体潜力不是“非 LLM MAPF 也算 Agent”。确定性使用神经概率排序 PIBT 候选可能造成循环；§3.4 比较未达目标 agent 的旧/新位置及邻接占用是否相同，沿有限祖先深度 d 检测重复。对对应祖先节点加入 unguided agent，重置约束并重入搜索，改用默认非学习偏好。可核的主线差额是 learned guidance 与确定性搜索的消费边界，以及局部失败检测后何时撤回模型权力，Owner 暂定位 `AGENT-PLANNING`。不是仅把成熟 attention 用于路径标签。

只拟保留该机制潜力。碰撞约束由 PIBT/搜索消费层负责，不把神经分数当可执行许可；有限重复检测不保证识别所有 guidance 错误。原文完整性定理未审其附录证明，故不采用证明结论；小障碍丰富高密度图的实验与 map-wise fine-tune 不授大图、低密度或 LLM 普效。日期/重要修订资格另保留，不评分或写 Books。

本节单篇 prepared 后即时交 root。root 随后实际读 exact-v1 §3.3/3.4/4.3/5，确认逐 node 的 unguided set、回溯检测、reset constraints/reinsert fallback；低密度时 inference overhead 可能不值。采用边界按其实际回读通过，未用脚本代语义。

## 2. A-DATSC 2510.18004v1：C → 窄 P，实际校准通过

web 打开 abs v1 为 cache miss，不重该 web 失败；独立 curl 一次恢复 [原 abs](./SUP_18004v1_abs.html)，HTTP200/43659 bytes。只有 v1 Submitted 2025-10-20 18:38:26 UTC；comments 为 under review submitted to ICLR 2025，不将其当会议接纳或公开日。HTML 自身标题是 Deep Generative Temporal Subspace Clustering，abs 标题是 A-DATSC；两响应差异保留，不虚构更版记录。

实际读 [请求 exact-v1 HTML](./SUP_18004v1.html) §4、§5.1.2–5.1.4/5.2–5.4，HTTP200/209764 bytes，20秒/retry0。root 实际独立读同一必要域并校准窄 P：soft-assignment-conditioned self-expression 与 subspace residual discriminator 联训，具体约束改变 latent 表示如何形成，暂定位 `WORLDVIEW-REPRESENTATION`，不是因为天气/遥感测试题材关闭。

只保留上述机制潜力。理想正交 U 与训练中的正交 regularizer 不等；soft assignment 和低 residual 不认证真实 cluster membership，attention 不认证因果。fake 为 in-cluster 凸组合不自动是错子空间，也不认证该 hinge 目标必然可区分。未采用普遍聚类收益、稳定性或完整可执行数学 recipe，不扩科学应用池。

## 3. MambaX 2510.17529：C → 窄 P，实际校准通过

旧 Atom 当前 v3 为版本记录稿；本次 abs exact-v1 题名为 Longitudinal MRI Segmentation（current 多 Prostate），v1 Submitted 2025-10-20 13:32:42 UTC。web abs 的较旧缓存 history 只到 v2 2025-11-27，与旧 Atom v3 2026-08-20 的两个实际响应分开，不用旧缓存证明没有 v3，也不将 v3 正文倒签 v1。

[exact-v1 HTML](./SUP_17529v1.html) HTTP200/277756 bytes。作者实际读 §2.1–2.3/4.2/4.4/5；root 已实际读 §2.1–2.3/4.2/4.4。双时共享 encoder、前时 mask 的 shape latent 后置融入 patch 表示再 cross-attention，是 prior 如何参与表示形成的具体接口，暂定位 `MULTIMODAL-REPRESENTATION`。伪标签误差/预算对照是必要反侧，不能仅按医学标题关闭。

§2.2 broadcast 叙述还需额外对齐，Eq6 网页 Tversky 式重复/缺项，不采用 shape recipe 或可执行公式。N6 ablation、预训练与标签来源混杂/单机构限制保留；伪标签量更大可能更坏，不把 self-training 等于新真值，也不授临床、无损、隐式配准普效或硬件收益。

## 4. CharDiff 2510.17330：C → 窄 P，实际校准通过

旧 Atom 当前 v3 名 CharDiff-LP，ICPR2026 accepted；本次 abs exact-v1 名 CharDiff，11页，v1 Submitted 2025-10-20 09:23:29 UTC；history v2 2025-12-19/v3 2026-06-30。不将后版接纳/28.3%结果倒填 v1。

[exact-v1 HTML](./SUP_17330v1.html) HTTP200/168638 bytes；root 已实际读 III-C/D/V，作者复用其真实必要域阅读，不假称本人已通读。区域化字符 prior 限制 cross-attention 干扰是 `MULTIMODAL-GENERATIVE-PARADIGMS` 的窄潜力，不等车牌应用整体入主线。

原 Eq3 是 `softmax(M * QK / sqrt(d))`；外区 logit 乘 0 后 exp(0) 非 0，不认证严格 only-region、绝对无干扰或具体硬 mask 实现。softmax 轴/公式4 shape 未闭合。保留 OCR/segmentation 错误传播与原图并列人审退路，不把恢复图当证据真实性或未知字符的可信恢复。仅此机制恢复，不扩车牌/医学池。

## 5. 日期与版本责任

四项旧 C → 窄 P，原 66 = 57 潜力 + 9 摘要贡献关闭；不是新增四篇读取或确定候选。四个 v1 提交字段都不是首公开证明，18004 换算 BJT 已为 Oct21 02:38，仍不能仅以 submitted 裁首公开或整个 family。各自首公开/重要修订事件在新增 Oct20 的资格未知，单列必要外部日证，不无限追秒，不为本轮评分、Evidence 或 Books 预签。

只有 root 必要域准入校准已发生，整日 Source/arXiv 差额、日期出口/六节 DAY 仍普通处理中。
