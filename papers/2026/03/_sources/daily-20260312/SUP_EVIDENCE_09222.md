# 2603.09222：条件删句分数与集合充分性

root 作者必要 Source、非作者 supplement_20260312 独立 Source/date/逐字 PRE 及实际 POST 通过。采用 [LooComp exact-v1](https://arxiv.org/html/2603.09222v1)，实际读取 §3–5、A.1–2、Tables1–3/5–7 中相关对照；未核图像精数、代码或复现。当前 v2 改名 EnComp 的 single-encoding 描述不回填 v1 的 n+1 次 encoder 路径。

原 batch2 身份：v1 提交 Mar10UTC05:44:20 不直接作公开；官方 no-advance 公告下界与 arxiv.content owning/findable、registered Mar11UTC02:08:20 上界同 BJT03-11，复用已校准的日期夹证，不移动旧候选。current 可见说明无撤回或必要纠错；后来改名不作为本窗重要修订。拟 2+1+2=5，具体长期缺口深入，唯一 AGENT-CONTEXT。

## 必要方法及反侧

学习 f(q,P) 的 clue-richness scalar，将完整段落与分别删除一句的输入重编码，以差分 δ_k 提议句子贡献。训练用 HotpotQA critical/noncritical 标签、ordinal/margin 与 BCE；noncritical 的 hinge 实际推动 δ≤−m3，不补写为 prose 所称近零。训练最多采50个删除变体；v1 推理 n+1 份输入可并行但仍有独立 encoder 工作。完整段落分数低于 d_min 可整段移除；其余按正 δ 分布最大相邻 gap 提议阈值，singleton、ties 等退路未完整闭合，不补成可执行保证。单句贡献是其余上下文保留时的条件 proxy，多句联合移除可能破坏冗余、指代或组合证据；这部分是明确系统推断，不冒充作者实测定理。

ModernBERT-large395M/base139M、LoRA rank64、bf16训练、HotpotQA训练子集28897/90447，9:1 split，dev分类F1网格选阈值；6epochs约21h/RTX4090。评价 Contriever-MSMARCO/2018Wikipedia top5/20，Llama3.1-8B与3.3-70B、五QA任务；API reader另作有限验证。Table1多项低于Raw，例如8B top20 TQA F1 72.2<72.7、2Wiki30.8<32.0；70B top20 NQ50.5<53.4、2Wiki37.5<38.5。Table5 adaptive gap亦非逐项最佳。三个不同batchsize运行不等于三个独立训练seed；baseline ratio并不匹配，不能由平均排名推普遍Pareto优越。

Table1 Time/Rate在两reader间重复，定义与正文属于压缩处理段；它不是 target reader 或完整 RAG 的端到端延迟。Fig3正文承认 k=10 不及 CompAct；Table7 top20 caption 与 k5 正文冲突，不修成统一profile。推理precision、完整reader hardware、并发、SLO、训练seedCI、独立全链费用 Not Disclosed。训练、逐句副本/所有encoder passes、分句与chunk合并、阈值选择、reader及质量回归均计费。未核公开实现，不授复现、生产能力或证据保真保证。

## 实际 owner 差额与逐字 PRE

root actual Ch75 250–284 与 Ch74/76 开篇：已有 raw/derived、router none 分支、break-even 与 future-task充分性，但没有解释逐句删去的条件 proxy 如何变成集合选择，以及其多次 encoding 的费用。仅在损失问题之后、独立 router 之前补两段；保留原段落和后续机制。

拟段1：

对已知问题，extractive 分支可以不改写句子，而用一个学习到的标量衡量段落是否包含答题线索：分别编码完整段落和删去每一句后的变体，以两者分数差提议该句的条件贡献。这里比较的是“其余上下文仍在时删掉这一句”的模型读数，不是句子与 query 的相似度，更不是最终答案正确性的证明。训练标签、分句和 chunk 合并、encoder 与阈值共同决定这份派生视图；逐字保留被选句子也不能保证保住指代、否定或跨句组合证据。尤其两句互为冗余时，各自删除的损失可能很小，同时删去却会移走唯一证据，因此单句低分不能直接签发集合充分性。

拟段2：

这种选择以额外编码换取更细的删除信号：[受限 leave-one-out 对照](https://arxiv.org/html/2603.09222v1)的原始路径需要完整段落加各删句变体的多次 encoder passes，并行只改变执行安排，不消除工作量。整段低分门与句分数间隙阈值也需要独立质量检查；阈值退路未完整披露时，不补成保真 recipe。所测 QA 中部分 reader/任务仍低于未压缩输入，表内 compression time 更不等于包含目标 reader 的全链时延。训练、所有变体、分句、阈值校准、reader 与回归费用一起计入下面的 break-even；联合删句失真、阈值失配或总预算不合算时，保留原文、扩大保留集合或回读未压缩段落，而不是让线索分数代替 evidence gate。<!-- source-family:SF-2026-ARXIV-2603-09222 -->

实际 Ch75 新263/265及本人680已按逐字 PRE 落盘；作者顺读253–279完整局部与自身末注、回对必要原证，限定 diff 检查通过。非 writer supplement_20260312 实际顺读253–290完整局部及本人末注、回对有效v1必要原证，确认与PRE一致、旧router/raw及break-even未覆盖，POST通过；仅本项，不授DAY。
