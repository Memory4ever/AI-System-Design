# FLB 与 Speech Depth 的唯一 owner / 窄逐字 PRE

root 必要 Source 两项6分已实际通过；日期owned upper原字段在EXTRA4，请独核。当前Books上下文及目标完整邻接已作者实际读，只申请下列 Ch23 两处不重叠插入和本人静态注，不自行授锁。

## 00455 / MULTIMODAL-REPRESENTATION / Ch23

文件 `books/part-03-multimodal-world-models/23-multimodal-representation.md`，现 late-branch/two-logits/hidden-anchor 分支已完整读。差额为不保hidden而缓存**全vocab第一步logits**、后步在现候选支持内融合；现静态hidden anchor不能代替其语法prior/视觉truth资格。

完整左锚（保持全文）：

> [受限三种7B视觉语言模型的对照](https://arxiv.org/html/2601.05939v1)支持静态 anchor 分支的局部取舍，不授普遍无损的“视觉加强”：LLaVA 的 AMBER coverage 从原50.4降为静态48.6，动态48.1更低，静态也并非处处胜动态。初始 hidden 读取、模型相关的层/强度校准和质量回归均有费用；动态版本为每个 token 先探测再注入而增加第二次 forward，不能把诊断成本归给仅向量混合的静态路径。v1 Eq8 的 `min(...,0)` 与正风险时增强注入的叙述冲突，故不采用该动态执行配方、不自行改成 `max`；这里只保留诊断与已明确的静态干预。Anchor 过旧、隐藏接口不可见、质量回退或预算不合算时，保留原 Decode、外部 grounding 和前面的两路对照。

右锚为现完整“隐藏状态不可改时，还可以只强化输入中的视觉线索…”段，保已有单帧重复/scorer/prefill分工。拟之间仅两段：

若只需 logit 接口，固定 anchor 也可以放在词表空间：缓存 image+prompt 后第一步的完整 vocabulary logits，在之后的当前 logits 中按随 step 增长而饱和的权重加回这份向量，再用当前分布的相对 plausibility 门槛限制候选。它不再注入 hidden state，也不需要每步再运行一个无图对照，但第一步分布包含语法与起句偏好，不是纯视觉证据；保存这份 prior 不能证明内部视觉信息已恢复或语言 bias 已消除。<!-- source-family:SF-2026-ARXIV-2604-00455 -->

[两种7B VLM的有限对照](https://arxiv.org/html/2604.00455v1)支持这一单forward干预的局部取舍，不支持对所有属性/关系的因果修复：只强调起句 token 的设置在一个对照上比完整初logit的幻觉指标更低，故不能把完整向量的收益唯一归于视觉内容。初logit驻留、逐步词表融合/筛选及weight/门槛校准仍付费，缺少绑定硬件、precision和服务负载的时延证据时不授零成本或SLO。Anchor与当前句法失配、召回或任务质量退步时，降低或关闭注入，保留原decode、hidden anchor、两路输入对照与独立grounding；各分支依赖不同接口，不是必经流水线。<!-- source-family:SF-2026-ARXIV-2604-00455 -->

本人末静态注仅一条：`SF-2026-ARXIV-2604-00455` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00455v1)§3/Eq3–7/4/Table5，2+2+2=6，仅全vocab初logit与当前plausibility支持的跨步接口；保only-The反侧、语法prior/视觉truth、fullvocab费用，不授因果恢复/普遍无损/服务SLO，未核实现或复现。

## 00489 / MULTIMODAL-REPRESENTATION / Ch23

同一文件，当前 modality-gated pack 的原图 bypass 保真条件已完整读，邻接audio旁路/mainstream完整读。差额为冻结旧块、插入新depth学习speech vs整体removal恢复路径；gate关闭严格旧图与仍启用新层的text不混为一谈。

完整左锚（保持全文）：

> [Modality-Gated Deep Adapters 的有限实验](https://arxiv.org/html/2609.26182v1)支持这种明确绕过的接口，而不是所有输入的自动路由或任意混合模态保证。closed-gate 检查每模态仅一个输入，多 gate 同一 forward 与并发请求隔离未得到验证；单一 backbone 的 audio/thermal 训练又含参数量、loss 和筛选差异，gate-open 的 thermal 分类仍低于原基线。新 pack 要支付驻留内存、训练、入口管理与 scope 回归成本。多模态混合、重算或并发 scope 无法可靠隔离时，应保留 external projector、独立 adapter/model 或原编码路径；旧图精确保留与新模态任务质量是两项独立验收。<!-- source-family:SF-2026-ARXIV-2609-26182 -->

右锚为现完整“多种 audio encoder 的互补信息也不必先压成同一条流…”段，保其连续main/旁路/融合/来源全文。拟之间两段：

新模态需要更大内部容量时，还可以冻结原 embedding 行和 Transformer 块，将可训练语音行与新 Transformer depth 加在旧路径之间或并列分支，再以 identity/零输出初始化减少起步扰动。残差新层、interleaved depth 与并列扩展的初始化不是同一个计算图；关闭或删除**新增层**可以恢复原 backbone 路径，不代表使用所有新层时纯文本行为也保持。只把特定 speech 模块对文字禁用，也不能消除仍经过的其它新增 attention 对旧任务的影响。<!-- source-family:SF-2026-ARXIV-2604-00489 -->

[有限 speech adaptation 对照](https://arxiv.org/html/2604.00489v1)在 SmolLM2 .36/1.7B 与约48K小时ASR训练中不混入text replay；部分插层设置显著损伤text，较好保留text的top层设置又有更差WER。因此旧参数不更新、恢复旧路径和新模态quality须分开验收，恢复backbone也未独立认证扩词表后的整softmax逐概率相同。新增depth、声学条件与训练/驻留有费用，trainable参数匹配的LoRA不等总容量或完整计算相同。纯文本回归、ASR或预算失配时，删除/关闭新增路径、保留独立speech adapter/projector与原text模型；不由可恢复旧路径宣称全模型零遗忘。<!-- source-family:SF-2026-ARXIV-2604-00489 -->

本人末静态注一条：`SF-2026-ARXIV-2604-00489` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00489v1)§3.1–3.4/Tables1–2，2+2+2=6，仅冻结旧块/新depth适配与恢复路径/full-input行为分责；保text/WER取舍、不同图初始化、扩词表softmax及参数/全部费用，不授bitwise整分布或零遗忘，未核实现/复现。

## 当前状态

PRE及两窄插入/静态注尚未授权；写后分别交实际位置/邻接，root非作者POST不由本稿自授。不会写其它Ch23family。

## 实际授权/POST更新

root实际两PRE全文、Ch23 201–222/1443–1462完整邻接与EXTRA4原日期字段通过，授两项各两段/本人注；作者按逐字PRE落实，完整邻接与注顺读、限定diff通过。root随后实际读回FLB1453–1465/本人1974注、speech207–230/本人1972注，两个nonwriter POST PASS，保first-logit语法prior及恢复backbone≠整softmax；两锁释放。上段申请态仅履历，当前真Integration可同步、不授DAY。
