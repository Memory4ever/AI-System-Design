# IndexCache：必要 Source 与 Ch45 具体差额

root，2026-10-09；精确 [2603.12201v1 HTML](https://arxiv.org/html/2603.12201v1)。实际读 §2–4、Tables1–4、直接相关 Appendix C 的优化代理反侧与 D 的 evaluation contract；未遍历 artifact、PDF 或旧版本。完整题摘准入由本日有限补检获得。日期采用 `SUP_DATE_12201.raw` 的同标题/URL、arxiv.content owning client、findable 注册上界与官方公告批次下界，共同限定到 March13 北京时间；submitted March12 不当公开日，DOI注册本身不证明实际发布时刻。

## 方法与直接反证

Full 层运行自己的 DSA indexer，Shared 层继承最近前方 Full 层的选择索引；各层仍用自己的 KV 做 attention，首层 Full 初始化。减少长 Prefill 中完整 indexer 的运行次数，不把全部复杂度变线性，也不删除未选 KV 的驻留容量。Training-free 在固定 calibration batches 上按 LM loss 逐次替换 Full→Shared；不是全局最优搜索。Pipeline 分块强制每块首层 Full、分块搜索是额外近似，不能当无依赖切割。

Training-aware 先 dense warmup 再 sparse training/SFT；训练 indexer 时，对多个被服务层的 attention target 分布求平均后作 KL，随后联合 LM 与稀疏目标。梯度等价命题对目标固定、只有 q 带参数的 indexer 子问题成立，不授整个联合训练所有参数的梯度等价；平均 target 也不保证每一层的支持集合充分。

Table2 的 47层 GLM4.7-Flash、30B-A3B 对照：搜索可改善某些稀疏比例的结果，但 GW/LCB 等仍有退步，1/8 更损 long-context，不能采用“完全无损”。Appendix C 以层间 cosine proxy 做 DP，在相同比例下不必优于 uniform 或原 DSA；相似度不等下游 LM loss。Table3 training-aware 的 with/without cross-layer target 存在收益和退步，使用缩短训练 pipeline，不当完整原训练的通用 Pareto 改善。Table4 GLM5 744B、40B active 是 preliminary training-free 证据，也非全任务无回归。

Serving 使用 SGLang dp_attention、dp8 的 H100 节点，10K/60K/120K/200K；single concurrency 与 full-KV population 是不同运行合同，后者约800K tokens/GPU。输出长度、serving精度、固定batch/concurrency以及SLO未完整披露，不把局部速度推到端到端生产保证。任务评价 temperature1、top-p .95、top-k40；200K总预算含32K输出预留，MRCR/GW按可容纳人口、其他长任务有middle truncation。无需把这些吞吐数字写入机制正文。未核实现、未复现。

## 具体 owner 与 PRE

唯一 owner `INFER-KV-CACHE` / Ch45（legacy41）。实际顺读 Structured knowledge→低维selector→跨层dense/sparse head继承→层级页/物理布局的连续175–211段；Ch44/46入口以及Ch14/22 DSA机制交接。现有2602.04541分支已解释 head-role 继承索引、HardKuma teacher蒸馏、不删KV与refresh回退；尚未解释**独立DSA indexer的层级Full/Shared计划、以LM loss而非相似度选择refresh位置，以及shared indexer的跨层目标**。不另在Ch14/22重复推导。

2+2+2=6，具体 owner gap 定点深化；不将借用缓存原则、层间相似性或作者速度加分。建议在现有2602.04541段后、层级page段前插两段。以下逐字文本待非root实际Source/owner/PRE通过后写入：

如果稀疏 attention 仍在每层运行独立 indexer，长 Prefill 的完整候选评分本身就可能成为瓶颈。另一条跨层分支因此把层分为刷新选择的 Full 层与继承最近前方选择的 Shared 层：共享的是 token 索引，各层仍读取自己的 KV，首层必须初始化选择。刷新位置可在固定校准批次上逐次按 language-model loss 决定，而不只最大化层间相似度；后者即使更高，也可能漏掉对下游输出重要的 token。Index plan 须绑定 checkpoint、层角色、最近刷新来源、选择预算及 KV row 身份；减少 indexer 调用不等于删除 KV 或让全部 Prefill 变为线性。<!-- source-family:SF-2026-ARXIV-2603-12201 -->

固定权重下搜索角色，保留了原模型却增加校准与组合搜索成本；重新训练共享 indexer 则可让它拟合多个被服务层的 attention target 平均分布，交换成训练成本与跨层目标耦合。这个平均目标不保证每层都选到充分证据，[有限模型、稀疏比例与长任务对照](https://arxiv.org/html/2603.12201v1)仍有质量回退；相似度代理、局部吞吐和平均任务分数都不能替代同一 workload 的联合验收。校准分布漂移、跨层需求不一致或搜索/训练收益不足时，应增加 Full 刷新层或回退每层独立选择，随后再由原有 cache manager 执行物理 gather、驻留与回退，而不是让共享索引绕过状态有效性检查。

本包不授 Source 独立验收、实际写入/POST 或本日完成；共享写入未开始。

更新：mar14_supplement实际独读上述精确必要原证/Ch45完整局部与邻接，Source/逐字PRE通过（`SUP_PRE_12201.md`）。root随后只写196/198两段与本章Reviewnotes本人条目；mar14_supplement真实顺读175–215完整局部、两新段与本人源注并回对原证，`SUP_POST_12201.md`实际nonwriter POST通过，窄锁释放。此单项可同步正式日报，不授日级完成。
