# 2604.25800v1：CoT 可表达性与可学的长度泛化

04/29 作者侧必要 source→真实 owner 审阅；非正式冻结、非作者独立核或日级 Gate。[官方 exact-v1](https://arxiv.org/html/2604.25800v1)为 *Barriers to Universal Reasoning With Transformers (And How to Overcome Them)*。arXiv 本窗公告之外的更早同家族正文仍需日期例外核，不能以提交字段单证首公开。

Ch4 [capacity / optimization / generalization 三分](../../../../../books/part-01-worldview/04-why-models-learn.md)与 Ch5 [归纳偏置](../../../../../books/part-01-worldview/05-what-neural-networks-learn.md)已持有「函数可表示 ≠ 优化能找到 ≠ 超出训练长度仍能运行」的总原则；Ch17 的显式 CoT 段主要是额外 token 的监督/成本与 silent recurrence 对比。本文可补的是**可执行 trace 形式本身怎样决定长度泛化的可学条件**，不是再讲一次“长题需测试”。§3.1 的 Definition 3.3 明示理想 learner 在每个训练上界 `n` 看过全部有限前缀，并在更长 `f_TestLength(n)` 上要求 next-token computation 相同；这不是现实 SGD 对开放任务的保证。

§3.2 Theorem 3.4 / Appendix A.2 仅对固定有限 alphabet、标准位置形式下具有 `C-RASP[Pos]` CoT 的 decision problem 证明结果在 `TC⁰`；Corollary 3.5 又基于 Huang 等的 idealized learner / Limit Transformer 框架给无限多训练长度的失败。证明把输入信息压成 `O(log N)` count summary，再以常深电路决定输出；不能把这个受限理论写成**所有真实固定词表 Transformer 永远不能解决非 TC⁰ 问题**。§3.3 Theorem 3.8 / Corollary 3.9 的正面模拟必须让 signpost alphabet 随问题增长，为每个 tape cell 给可匹配标识，trace 只记录 value-change event，在 C*-RASP 与特定理想学习模型中得到 Turing 模拟与 `C·N_tapes·(N+|w|)` 长度；它不是现实 tokenizer、固定模型参数或普通梯度训练的通用推理保证。

§4 的 25M、6-layer GPT-2 从零训练只在 parity、Boolean evaluation、S5 permutation 的 `train len 30/50` 与约 2× 测试切片上验证格式方向：value-change 帮 parity，signpost 帮 Boolean/S5，S5 仅到约 1.7×。更重要的受控边界是训练时对位置与 signpost token 进行通往声明 `max_test_len` 的随机 offset 暴露（§4.1），故不能称完全未见位置/标识的外推。§4.2 的三预训练模型只是五例 few-shot、每长度 100 样本、贪心解码；天然数字作 signpost-like marker，未给 tokenizer 真正无限新符号。代码赋值任务还把变化日志写在**输入注释**、只要求最终答案，不能把它说成模型已学会输出无限 CoT。

**作者拟评分与处置：** `Design Delta 3 + System Reach 1 + Durability 3 = 7`，Deep 候选。Ch5 是唯一较合适 owner：在归纳偏置/泛化处最小补「计算存在、可按某 trace 表达、能从有限长度学习并继续运行」三种不同命题；标识/变更日志属于可检查的格式条件，其无限 alphabet/理想 learner 假设和有限实验回退同时保留。若独立 source→owner 认为 Ch4 的三分已足够、或这项理论尚不足以改变 Ch5 长期解释，则最终 Report Only；目前未申请共享锁、未写 Books，不把评分代替采用。
