# PBRC / Fact Adaptation：source→actual owner 窄采用提案

作者 apr20_resume，必要原文及反证见[v3-reopen-notes 随后四项](./v3-reopen-notes.md)。尚未非作者采用、未写 Books；不计 I 或日级 Gate。保留其他结果的有效证据，不要求全附件/复现。

## root 有限非作者采用复核

实际重新打开两份官方v1 HTML。15558核§3固定有限假设/外部状态、§4.4三种enforcement、§6.1 skeptical dilution及§14失效/活性：witness admissibility不蕴含operator compliance，(1−λ)b+λu在0<λ<1下保argmax且max不增，认证不保证语义支持；提案只采用外部状态的窄性质，不承诺内部LLM信念或全部拓扑正确。与实际Ch82共识段和同根报告相邻论证对读，责任区分是实际缺口，literal两段通过。

15574核§2 SLiCK的20次采样协议、§3/Table1、§4.1 known-only一epoch teacher与token KL、§5.1/5.2名字/UUID和层14相关解释。Unknown是接口下的失败，attention-only低acquisition不能作为所有模块存储的证明；自蒸馏与L2不同不证明唯一因果。实际Ch29 trainable subspace、forgetting和reference/replay段已讲保持—可塑性，但未分开表达既知事实与获取新事实的目标，因此literal两段窄采用通过，数字不泛化。

只通过必要来源→实际owner及所拟文字；未验实际写入或日级Gate，未复现实验。授Ch82/29窄写入后仍须root实际写后复核，不计I增量。

## 15558 PBRC → AGENT-MULTI-AGENT / Ch82

[official v1](https://arxiv.org/html/2604.15558v1)实际 §3–4、§6.1–6.3 的必要定义/两条证明、§13.9/§14。实际 Ch82 `Verification 与 Aggregation` 在 `Multi-Agent 协议不能把快速共识当作协作正确性` 已要求独立 truth/effect alignment；随后同根报告分开原始/提取误差。但未解释 **witness admissibility 与实际 operator enforcement 分责**，也未给外部 belief-state social-only 非放大分支。拟在该共识段与同根报告节之间嵌入以下两段，不采用未核全部 topology/theorems：

> 避免共识自我放大，还可以把“允许使用哪些证据”和“如何更新信念状态”分开预先定义。对固定假设集合上的概率向量，先注册 evidence trigger、revision operator、优先级与 fallback；只有经过相应 validator 的非空 evidence tokens 及其 witness，才触发证据更新。没有新准入证据时，一个保守分支只做 `b′=(1−λ)b+λu`，其中 `u` 为均匀分布、`0<λ<1`：它不改变最大分量的候选集合，也不增加该分量的数值信心。这个性质只约束协议保存的外部状态，不说明 LLM 内部信念或答案更接近真值，也不能修复初始错误。
>
> witness gate 只能证明准入条件满足，不能强迫 Agent 把声明的 operator 真正作用于状态；若数值更新也要受保护，需由 state-holding router 拥有并计算权威 belief-state，或提供足以核对具体更新的证明。认证证据仍可能语义不支持命题，保守 fallback 也会挡住有益纠正并损失活性。[PBRC](https://arxiv.org/html/2604.15558v1)的形式条件和有限 paired LLM 示例支持这个分责，不证明自由文本共识、所有假设动态变化或生产安全。开放任务无法固定证据语义与更新状态时，保留 dissent、独立 verifier 和人工裁决，不把 external confidence 作为事实提交权。

2+2+3=7 必要深入。§4.4 architecture A/B/C 的边界是中心；n3000 GPT4o/T.7 配对示例 .724/.678/.698/.724 是外部禁止 flip，273 beneficial flips 同样被挡，不采普遍正确性。数值公式只用于源定义的 finite probability vector，不将 token authentication 等同 semantic truth，也不采用全部 theorem。

## 15574 factual adaptation → TRAIN-SFT / Ch29

[official v1](https://arxiv.org/html/2604.15574v1)实际 §2–5.2 及 discussion。actual Ch29 `Catastrophic forgetting 与能力回退` 602起讲事实覆盖、multi-slice/早停，后续 reference KL replay 讲 retention signal/capacity。缺口不是没有 KL，而是 **先区分表达既知知识与获取新事实，才决定是否保留事实可塑性**；teacher 仅学习 known facts 的回答方式与全新事实 acquisition 要分责。拟紧接通用缓解段、`早期回退`节前两段：

> 事实问答适配应先区分两种目标：教模型把已有知识按任务形式表达，或确实让它获取新事实。若目标只改变表达方式，限制事实相关可训练路径能减少干扰；但若必须学习新事实，同样的冻结也可能使 acquisition 近乎停止，不能把“旧知识保持得好”单独作为适配成功。评估应分别定义任务中已能稳定表达的事实、尚未表达的事实，以及独立 retain slices；多次采样都答错只是这个评价协议下的 Unknown，不证明内部完全没有知识。
>
> 需要事实可塑性时，可先用已知事实训练一个回答格式 reference，再在混合事实适配中加 token-level distillation 约束，把新事实 acquisition 与旧行为保持共同验收；reference forward、teacher lineage 和 retain 测试都是额外成本。[受限实验](https://arxiv.org/html/2604.15574v1)观察到冻结不同模块和 reference 约束有不同取舍，并用名称重组/UUID 对照提示干扰随事实支持条件改变，但这不证明模块拥有唯一事实存储功能、知识已被删除或遗忘仅由一种表示漂移造成。reference 偏误、retain 支持不足或新事实学习被压制时，应回退更小更新、可信 replay 或独立 adapter，而非用较低 hallucination 指标掩盖 acquisition 失败。

2+1+3=6，具体 owner gap 深入不是抬分。代表 Qwen2.5-1.5B：attention-only Unknown .010/HeldKnown .931 vs FFN .941/.782，source Known-only teacher1epoch/τ.5/λ1；3%vs15%是 relative peak held accuracy drop，不采用全部模型/普遍百分点。synthetic P17 name vs UUID改变 tokenization/pretraining association，layer14 cosine与损伤相关不足以证明唯一原因。Ch29现有reference KL replay仍保留，本文只新增目标分叉与known-only格式teacher机制，不重复推导完整蒸馏。
