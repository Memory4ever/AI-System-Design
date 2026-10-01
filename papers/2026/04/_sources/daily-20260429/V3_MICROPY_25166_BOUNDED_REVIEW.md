# 2604.25166v1 MicroPy：表达性、可学执行与评测分母

本项已在当前旧 60 完整题摘的 `41 潜在` 中，不新增 106 总数。官方 [Training Transformers as a Universal Computer, exact-v1](https://arxiv.org/html/2604.25166v1) 仅读 §1、§2.1–2.3、§3.1、§3.3/Table 1–2、§5；对照现有 [Ch18 decoder 表达/训练状态](../../../../../books/part-02-model/18-decoder-only.md)与 [Ch66 EvalSpec](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的实际段落。日报日期仅暂由官方公告批次窄链归属，独立首发例外未核；这不是独立 Source Review 或日级 Gate。

## 原文可保留的最小增量

“MicroPy 是计算完备语言”本身是**语言**性质，不推出有限权重/上下文模型对任意程序都执行正确。真正可核的条件增量是：作者把有限组的 retrieval/local-rewrite 语义写成 step-level next-token 监督，使用 program sampler 加稀有 stack skeleton 的 plan sampler，并借 PENCIL 的 `[call]…[ret]` 消去已完成中间帧，让在线上下文成本按活跃空间而非累计运行时长走。59.5M decoder 在训练程序上限 128 trace lines 后，对六类人工编写的 MicroPy 测试函数报告最长 7,552-line 的轨迹。它给“标准 decoder 在显式操作语义+状态回收 scaffold 下能学会组合式局部解释器”受限实证，而非仅又证明数学表达能力；因此作者侧暂保候选，拟 `2+1+2=5` Standard。

但 Table 1–2 的 `100%` 标的是 **token-level accuracy**，总共 36 个 bit-task 与 216 个 SAT-task programs，其 `#trace lines` 是逐步 prompt/completion 对；§3.3 说明只评所有打印行均在最大 context 内的程序。原文没有把这组准确率单列为从初始输入、模型生成状态回灌到结束的 full-run 结果，也未提供任意长程序的错误累积或恢复率。已知正确历史下的下一步规则预测与自治全轨迹执行必须分账；不能从有限的完美 token 结果写“可可靠运行任何可计算任务”。测试的 SAT 求解仅 2–4 变量、1–6 clauses，复制/算术 bit 长 2–10，不等于一般实际程序；操作种类在训练生成器覆盖，未证明未见 primitive。PENCIL 是显式外部状态管理，不是模型权重自发学到无界内存。

## 实际 owner 与处置

Ch18 已区分显式 CoT token trace、状态回收/压缩与有限精度/训练—推理状态，尤其训练 teacher-forced 历史和生成回灌不等价；Ch66 已要求评测同时记录任务结果、轨迹与执行条件。但 Ch18 目前未用这一具体“有限语义模板覆盖＋计划采样稀有 stack＋活跃空间回收”实例区分**可训练的解释器局部规则**和**自治全程可靠性**，可能有一处窄机制增量。先保 `Books: 待非作者 source→actual owner 核；不写共享正文`；若 peer 判现文已足，转 Report Only/具体 Existing，而非靠题名“universal”自动整合。必要非作者问题仅为：Table1–2 分母是否确为逐步 token、原文有无独立 full-run 数字；Ch18 相邻段是否已有同义条件；PENCIL 是否贡献新架构（作者明确说采用已有 scaffold）。不扩其它附件或版本史。
