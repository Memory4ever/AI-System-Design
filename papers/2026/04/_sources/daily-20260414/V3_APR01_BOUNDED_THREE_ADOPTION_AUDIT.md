# 04/14 三项有限非作者采用复核

复核者：apr01。实际检查时间：2026-09-27T11:49:02+08:00。范围仅为三项拟采用命题的必要方法、评价、反证与当前 owner；未复现实验，未写 Books 或正式 Daily，未代替 first-public 日期及日级 Gate。

本轮已实际重读 AGENTS、统一 Prompt、研究/Report 合同、Daily 来源路由，并由 ROADMAP 定位 owner；读取 Ch45/24/30 的具体命题和 Ch44/46、Ch23/25、Ch29/31 的交接内容。没有继承旧 Complete。

## 2604.09852v1 MEMENTO

- 原始来源：[官方 exact-v1 HTML](https://arxiv.org/html/2604.09852v1)，§4、§5、§6.1–6.2.1/Table 1、3；[官方 abs-v1](https://arxiv.org/abs/2604.09852v1) 身份一致，页面未见撤回说明。
- 结论：拟采用的恢复契约窄增量 **PASS**。Ch45 `INFER-KV-CACHE` 的“稀疏 KV 保留的是派生状态，不只是被抽样的 Token”已解释 contextualization/lineage，但未明确 summary 文本不是其原 KV 的充分恢复材料。原实验在生成 summary 时仍读取原 block；以后删除 block，却保留这样生成的 summary KV。只用 prompt 与 summary 文本重新 Prefill，改变了这些行的条件历史。
- 必须保留：Table 3 的 normal 为 64 次重复，restart 为 8 次；15.3pp 不能作为严格匹配重复次数的因果收益。此证据也不是无损压缩证明。建议紧接上述 derived-state identity 段补恢复分支：保留兼容 KV/构造历史，或承认 text-only restart 是另一路径并重新验收；不要宣称仅凭 summary 即可 exact resume。SFT 的部分任务退步与额外训练/缓存管理成本不能隐藏。
- Books 状态：采用提案通过，正文尚未写入，写后待独立核；不计实际 Integrate。

## 2604.09921v1 Two Temperatures

- 原始来源：[官方 exact-v1 HTML](https://arxiv.org/html/2604.09921v1)，§2.2、§3.1–3.2、§4.1–4.3、§6；[官方 abs-v1](https://arxiv.org/abs/2604.09921v1) 显示后有 v2，本轮只采用已读 v1，未见撤回说明。
- 结论：两个采样控制对象的窄增量 **PASS**。Ch24 `MULTIMODAL-GENERATIVE-PARADIGMS` 的 Masked generation 已有 confidence gating、pass@1/pass@k 与 influence-based 提交顺序，尚缺“采哪个 token”和“在哪个位置提交”两个温度的明确分账。TLC 按温度化 confidence 无放回选 K 个位置；TCT 按 sigmoid 概率选择位置。它们改变顺序/并行度，不使 confidence 成为真值。
- 建议接现有 pass@k 段、在 influence 段前补机制及代价。理论限 idealized anchor/fork、TLC K=1 等条件，不能推一般并行正确性。实际 LLaDA8B/Dream7B、block32、长度256；NFE 不等同 FLOPs、wall-clock 或 SLO，最终 self-consistency/ORM selector 另有质量和成本。RL 对比为四张 A100、固定 72 小时，而非固定 steps；不同更新次数不能归为纯 sampler 因果。TCT 也并非全部最终设置更好。
- 建议 2+2+2=6、知识缺口 Deep override，不机械抬到 7。Books 正文未写、写后待核。

## 2604.09940v1 Hybrid FO/ZO

- 原始来源：[官方 exact-v1 HTML](https://arxiv.org/html/2604.09940v1)，§2.1/Algorithm 1、§3.1–3.4/Table 1–2、§3.6/Table 3–4、实验配置；[官方 abs-v1](https://arxiv.org/abs/2604.09940v1) 身份一致，未见撤回说明，但写明 Accepted by ICLR 2026。该 venue 线索不自动证明首次公开时间；日期/更早身份由作者侧定点 reconciliation，不沿 v1 submitted 直接归属。
- 结论：**5 分标准完成、仅报告提议 PASS**，建议 2+1+2。方法确实联合更新 base ZO 与 adapter FO，不能说 Ch30 已有完整同算法。Ch30 `TRAIN-LORA` 已有 frozen base、梯度/optimizer/activation 分账与轮换原参数层；本篇更适合作为另一受限 operating point，而不是必须新增 canonical 机制。
- Table 2 的 Llama2-7B/SST2 中 hybrid 与 FO prompt 都为 46GB，不能普称比 PEFT 更省显存；FO adapter 仍需相关 backward/activation。更少训练 steps 不等于更少 wall-clock，六任务/三模型并非全部胜出，Adam-LoRA 对照又改变 optimizer。有限 smoothness 条件不能推现代任意 LLM 收敛保证。保留 joint 更新/两学习率事实，不采用 universal 资源或质量收益。
- Books 状态：仅报告，不伪标 Existing，也不写新正文。

## 验收边界

三项必要采用复核已收口：两个真实 gap 提案、一个标准仅报告。首发归属、全日覆盖、其他候选和实际写后均不在本次 PASS 范围。没有扩查引用树、全年目录或版本差分。

## 两项实际写后非作者复核

2026-09-27 12:00 北京时间后，apr01 实际读取 root 写入的两个正文位置、前后论证及对应 Review notes；复用上文未变化的 exact-v1 必要源审阅，没有再读所有附件。

- **MEMENTO → Ch45 写后 PASS**：实际“摘要文本不一定是派生 KV 的充分恢复材料”两段紧接 contextualized derived-state identity，再交接缓存命中口径。三条恢复路径区分清楚：兼容 KV/构造身份、足够历史重建、text-only 有损重启。未声称原摘要无损或 text-only exact resume；64/8 次重复的非匹配边界、训练退步、版本/历史维护代价及简单旧路径的适用条件均在正文，不只在注记。
- **Two Temperatures → Ch24 写后 PASS**：实际两段位于 influence-based 提交顺序之后、允许重写的演进之前，内容取值与位置/并行提交两对象没有混同，confidence 不冒充真值。额外 schedule、随机错误、最终 selector、NFE 与真实延迟、固定72小时而非固定steps的边界在正文；低预算/单答案旧 schedule 仍成立。Review notes 另限定 TLC K=1 的理想化证明，不外推一般并行正确性。

两项是实际正文与采用命题的非作者写后通过，不代表本日其他来源/分母或整日 Gate 已通过。Root 可据此同步两个 Review notes 的“待独立核”和正式日报单篇状态；apr01 未修改共享 Books。
