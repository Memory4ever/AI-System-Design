# Knossos / Ariadne — owner proposal, not yet written

Owner: `MULTIMODAL-REPRESENTATION`; Ch23. Insertion: after the two paragraphs on renderable scene IR (source family 2602.18745), before heterogeneous page representations. Ch22 owns sequence-state capacity, not diagram topology identity; Ch24 owns output factorization/sampling generally, while this passage owns visual node/edge representation and its consumer error propagation. Context read: PROJECT_CONTEXT, LEARNING_PHILOSOPHY, WRITING_GUIDE, ROADMAP, exact Ch23 neighbors and Ch22/24 handoff. No shared-file mutation by this author.

## Exact proposed body

把整张图一次串行化为节点和全部边，保留联合预测且调用简单；当小型、已做任务适配的视觉语言模型容易在长边序列中漏项时，也可先预测固定的节点 inventory，再把节点分成互不重叠的 source groups。每次保留全部预测节点作为候选 target，却只允许当前组节点作为边的 source，最后确定性合并各组的 typed-edge multiset。这样改变的是关系输出的因子化和引用空间，不是把分组当作彼此独立的视觉事实；同端点不同关系仍须保留，辅助 connector trace 也不能回写为已证实的拓扑。<!-- source-family:SF-2026-ARXIV-2610-04721 -->

[这一受限图拓扑对照](https://arxiv.org/html/2610.04721v1#S4.SS4)支持分组对任务适配小模型的局部收益，却不支持“分阶段必更可靠”：同一设置下大模型的 staged Edge F1 反降，外部分布中换回基础模型的节点预测还可改善固定 edge predictor，说明节点适配可能成为误差入口。一次全图输出、只替换节点来源与显式分组应继续共存；按节点/边/typed edge 和外部数据分别验收。分组增加多次模型调用与输入重读，局部得分不是等预算净收益；inventory 漏项、未知关系或费用不合算时保留原图、直接全图预测和独立结构核验，不让合法合并代签视觉完整性。

## Evidence limits

Exact v1 §§3.1–3.3, 4.1–4.4/Table2, §5; Appendix D.4/E.1–E.3 needed for costs/matched recipe. Main adopted claims exclude universal speedup and numerical superiority across backbones. Root already independently read these necessary regions; source review accepted but actual write/post-write still pending.
