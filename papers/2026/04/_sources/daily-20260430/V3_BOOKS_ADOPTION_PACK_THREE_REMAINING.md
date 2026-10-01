# 26102/26294/26604：剩余三条拟 gap 的写前最小 owner 包

这三条只供 root 非作者 source→actual-owner 复核。它们仍在 04/30 未冻结工作集合；以下不是共享 Books 已写、当日分母冻结或日级通过。日期依据是本批有界公告组合而非 Submitted/Updated 单字段。

## 2604.26102v1 SWE-Edit → Ch81

[官方 §3–4/Table 1–2](https://arxiv.org/html/2604.26102v1)把代码检视、主 Agent 改动规划、格式敏感补丁执行拆给 Viewer/main/Editor 三种 context；后者还有受限 GRPO 选择编辑格式。现 [Ch81](../../../../../books/part-07-agent/81-workflow.md) 约 1106 行已绑定 `view→edit→review→submit` 的 workspace revision，不能说旧文不知编辑阶段；但**探索性大范围读取污染主规划 context**与**补丁格式失败**是两种不同的成本/错误 owner，当前该段未要求分账。若非作者认作真长期接口选择，可在 Ch81 现有 code-editing workflow 前后最小续写：读文件可交按需 Viewer，主 Agent 只接有 provenance 的选中片段；计划成为 Editor 的 typed patch proposal，执行器仍负责 apply/review 与当前工作树版本，Editor 不能因格式通过便获得改动真值。额外调用、检视遗漏、片段过期与低复杂度直接 edit 的回退同时写；不把“三 Agent”定为任何任务的默认架构。

评价仅说明该受测 scaffold/模型组合：Editor 单独增费约 10.1%；Viewer+Editor 才在 SWE-bench Verified GPT-5 主体较该 baseline 的 resolve +2.1pp/费用 −17.9%；其他三模型仅前100题×2次，PR-Edit benchmark 的相关性不是生产修复保证。若现章其他相邻段已明确“读污染规划 context vs patch 格式失败”两项并行分账，则 Existing/Only，勿为三角色名称重复正文。

## 2604.26294v1 TSP → Ch36

[官方 PDF-v1 §III–VI](https://arxiv.org/pdf/2604.26294v1)作为方法/数字权威（HTML-v1 参考文献日期有后期展示污染）。现 [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md) 约 529 行把 TP、TP group 内的部分 sequence activation SP、完整 attention CP 区分，但未表达**同一个 D-way rank 轴同时持有一份 weight shard 与 sequence shard**的条件路径。论文的 attention 在各 weight shard 广播/对 K,V 序列 all-gather，MLP 则以 ring 轮转 weight，试图同时压 parameter 与 activation residency；成本是每层多次权重/activation 通信和 recompute 重传。若采用，应在“五种并行角色”交接后写一段单轴折叠选择，而非称它普通 TP×SP 双维 mesh 或全面替代旧 TP/SP。

§VI 的 16–128K 显存/小规模比较为单节点 8×MI300X；1024×MI300X 主长序列结果主要是 **forward-pass throughput**，§VI-C 仅16GPU microbatch sweep 标 forward+backward。不能写全训练端到端普遍加速或跨互联一致收益。权重比高、ring/collective 慢、严格 checkpoint/debug 或成熟二维 mesh 优势明显时，旧方案仍合理。非作者应确认 Ch36 是否在其它现段已写相同单轴折叠与通信代价，若有则 Existing。

## 2604.26604v1 Enrollment/Participation → Ch36

[官方 §2–5](https://arxiv.org/html/2604.26604v1)把目标人口进入联盟的 enrollment probability，与已入组客户端每轮 participation probability 两层分开；仅校正到达/参加频率，只能估 enrolled population 的目标，不能自动恢复未入组者的全人口目标。现 Ch36 约 1139–1150 行已有 arrival-frequency rescale 和共同失效导致当轮类别缺支持，故不能泛称“首次考虑 worker selection”。潜在新增仅是**训练目标人口身份**：非入组客户端 covariate 不可见时，global population objective 与 enrolled objective 不同；在 ignorability/positivity、可估 propensity 或外部 aggregate calibration 成立时可条件性重加权，否则应显式缩小 estimand 与发布范围。拟放 Ch36 现有边际到达频率/共同失效后，以一小段阐明 enrollment 与 participation 非同一层采样；不要把小型 federated logistic synthetic 的定理称 LLM FL 保证，也不假设服务端有未入组者私有标签。

与 [04/20 AW-PSP 现段](../../../../../books/part-04-training-system/36-distributed-training.md) 的区别：AW-PSP 说共同故障时**本轮数据类别支持缺席**，本篇说观察到的 enrolled population 从一开始就可能不是目标总体；前者不能由到达频率校正，后者还涉及从未可观察者的目标定义。若非作者认为当前 Ch36 已显式对所有未入组人口与真实目标作此分账，可降 Existing，不为统计术语本身加书。
