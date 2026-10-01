# Apr14 第十八批：有限非作者采用核验

复核者 apr01（不是04/14报告作者）。实际重开六项官方exact-v1 HTML必要方法/评价反证，并读取Ch75 typed-registry及原文authority交接、Ch29 response-only loss/masking→corruption-support交接、Ch36 finite-SDC→step-commit交接。这里只核该六项处置与两项写前差异，不核全日日期、完整目录、其他附件，不修改Books，不代表实际整合或日级Gate。

## 2604.10352 ClawVM

[官方v1](https://arxiv.org/html/2604.10352v1) §3 Pages/Multi-resolution/Selection、Listing1、§5.2 LRU、§5.3/§7实际已读。**2+2+2=6，具体gap深入采用通过**：当前Ch75约274–295只定义type→retention、registry authority与failures，未说明生成多分辨率的时间责任或两阶段fit。可在该既有论证补ingestion/update预生成变体→预算时先装hard minima→剩余按utility/token升级；minimum不fit显式pressure，不悄悄降保护。

贪心不证明全局质量；§5.2 LRU同样零fault，quality差留未来；§5.3 replay成功定义不是实际模型任务成功，20 live单session没有跨会话边界。变体过期、预生成成本和schema非语义truth须保留。写回transaction既有authority无需再重复增写。

## 2604.10403 LIRA / SAG

[官方v1](https://arxiv.org/html/2604.10403v1) §2.1、AppA.1 Eq5–12、AppA.2 Alg1:6–9及AppL实际已读。**2+2+2=6，具体gap深入采用通过**：Ch29约65–125解释loss位置和corruption support，未把梯度路由作为第三对象。SAG forward普通计算，response参数路径被stop-gradient，附加response-response切路；residual正常。Alg1 counterfactual=SAG、retain=SAG†，不可混成统一mask。适合在Prompt-loss后以该受限训练分支衔接corruption。

Paired benign counterfactual与额外训练成本、内部表示重定向的假说性质要明确。AppL是特定backdoor/embedding对照；TOFU/WMDP或MCQ退步不是知识真正删除、通用安全保证或防御全部jailbreak的证明。

## 2604.10390 LLM-PRISM

[官方v1](https://arxiv.org/html/2604.10390v1) IV-A/B/C、RQ2/RQ3/RQ4实际已读。**2+2+2=6，标准已有覆盖通过**。Ch36约476–489具体承担finite corruption沿forward/backward/optimizer扩散、不同阶段检测/重算、提交authority与误报成本，而非仅提SDC名词。该论文GPT2 Small/Medium、WikiText、16H100/两节点/三precision的永久fault模拟显示loss-NaN gate不完备；未测生产自然故障率，也不支持所有precision普遍安全排序。无需新增策略正文。

## 2604.10333 Zero-shot World Models

[官方v1](https://arxiv.org/html/2604.10333v1) 主文Temporally-factored/Zero-shot extraction、Results、Sx1 masking/symmetric-control/output及Sx6实际已读。**2+1+2=5，标准仅报告通过**。完整前帧+随机稀疏后帧监督和perturb/compare/aggregate是受限表示/readout分支；人为移动patch并预测差异不是真实action干预或SCM保证。作者明确不同模型probe差异不证明其他模型没学到相关表示；本篇不据此修改完整因果世界建模设计。

## 2604.10367 Talking–Listening

[官方v1](https://arxiv.org/html/2604.10367v1) §3.2.2公式、§4.1、§4.3.1及Table2/3实际已读。**2+1+2=5，标准仅报告通过**。共享时间RoPE+headwise有界Gaussian penalty给soft locality/global-context取舍，不是strict window；有限α时远距仍有非零权重。16A100/bf16、Wan2.2-5B/两阶段仅支持生成设置，非真实交互闭环。非全面最优的精确反例可用Table2 ALiBi ASE=.584高于ours .581；不必沿用不明确的“2D某lip指标更好”。

## 2604.10387 Symbolic GPU Mapping

[官方v1](https://arxiv.org/html/2604.10387v1) III-C、IV-A2、V-C实际已读。**前分母关闭通过，不评分**：成熟坐标示例→代码proposal→有限million-point GT validation→一次生成摊销路线，未分离新的LLM执行保证。有限bijection并非全整数证明，作者报告正确映射采用linear search仍慢；dummy geometry kernel及NVML gross功耗不能代作Transformer运行收益。不是因非LLM或小规模拒绝。

六项有限采用结论全部通过；两gap仍需root授权实际落笔和作者外写后核验。实验未复现，日期由04/14日级工作处理。

## 两项实际写后复核（apr01）

本次实际顺读 Ch75 约274–299 typed retention→预生成视图→registry/commit 交接，以及 Ch29 约110–140 prompt loss→gradient routing→corruption support 交接，复用上述已实际核验且未变化的官方v1必要证据。两项**实际写后通过**，不是04/14日级Gate。

- `2604.10352` 两段嵌入 type-specific retention 原论证：ingestion/update 预生成、hard-minimum先fit后greedy upgrade、minimum不fit显式pressure、revision/scope失效成本、schema非truth、LRU同零fault但任务质量未证明均被保留。没有把replay零explicit-fault或单session结果写成生产质量/SLO；前接知识分型，后交registry提交责任连贯。
- `2604.10403` 两段把loss位置、forward可见性与backward route分开，普通forward、response参数路径stop、额外response→response切断与正常residual准确；counterfactual SAG与retain SAG†不混用。配对数据、能力保留代价、特定attack/MCQ不能证明知识删除或通用安全的反证在正文。下一段改“哪些位置产生监督loss”而非含糊“哪些位置贡献梯度”，使corruption support交接与新增区分一致。

Review notes 的“实际正文写后待独立核验”可以由持锁者最小同步为“实际正文及相邻衔接写后独立复核通过（apr01）”；未复现实验仍保留。
