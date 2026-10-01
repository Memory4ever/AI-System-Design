# 2609.22220v1 定点证据审阅：GPU kernel benchmark oracle

- 身份：Mingzhe Du 等，*Measuring the Checker: Mutation Analysis for GPU-Kernel Benchmark Oracles*，`arXiv:2609.22220v1`，[官方摘要/版本史](https://arxiv.org/abs/2609.22220)、[精确 v1 HTML](https://arxiv.org/html/2609.22220v1)、[作者测量 artifact](https://huggingface.co/datasets/Elfsong/KernelBench-M)。访问日 2026-09-23。
- 日期：`v1 Submitted` 为 09-02 10:30 UTC，[09-22 官方 `cs.LG/new` 公告](https://arxiv.org/list/cs.LG/new)将其列在 New submissions 第 47 项；然而[作者主页消息](https://mingzhe.space/news/)明确写着 **2026-09-12 发布此论文**，并链接到 [Hugging Face paper 页](https://huggingface.co/papers/2609.22220)。因此 09-23 的 arXiv 公告不是可成立的首次公开 owner，本日报不能将其作新候选或计分。作者声明只有日级日期，没有可核的首发时分；准确 owner 日保持 Date Hold，待取得事件时刻后再回拨。提交时间也不能代替公开时间。
- 项目位置：`PLATFORM-EVALUATION-SYSTEM` Ch66 的 Agent Kernel Evaluation 小节已有 hidden shapes/dtype/harness version 与 correctness receipt 原则。本文潜在增量是**如何测量 checker 自身的缺陷覆盖与误拒上界**，不是再重复“隐藏测试更严格”。邻近执行章节只拥有 kernel 实现，不拥有 benchmark release oracle。

## 机制和比较

旧方案用少量随机输入、`allclose` 容差验证生成 kernel；它便宜、可复现，在已知输入域内足以做开发回归。压力是这些 verdict 又被用于 leaderboard、RL reward 和 release gate：如果输入分布不触达边界/同步/精度错误，模型学会通过 checker 而不是做对计算。作者以正确 CUDA substrate 为 mutation target，PyTorch reference 仍是 oracle；对通过有效性门禁的 fault 注入做编译/等价/崩溃过滤，再仅把有合法 kill witness 的 mutant 纳入分母。这样可以对官方测试与强化测试比较检测率，避免把等价或未能证实可杀的 mutant 当漏检。

数值正确性不是“把容差无限缩小”：过大的输入或相消可使两个正确 fp32 实现因合法舍入差异被误判。作者因此先以 reference-validity gate 限定新输入，再做 mutation kill matrix、按 family 分解盲区，并用 holdout 检查 set-cover 测试集是否只记住开发集 fault。控制权变化是 evaluator owner 必须同时拥有 test-input validity 和 checker adequacy；生成 kernel 的 Agent 只提交候选实现，不能给自己的输出颁发正确性结论。

## 证据合同与边界

- §3–4 在作者生成、gate-verified CUDA substrate 及 KernelBench 协议上测量；主表为 7,384 个 witnessed mutants，官方五输入检测 6,136、漏检 1,248（16.9%）。该比例只属于指定 fault model、问题集、`atol=rtol=1e-2`、H100/软件环境，不是一般 GPU kernel 的真实错误率。
- §5 复现 KernelBench-Verified 的四种输入幅度与更严容差，按统一 witnessed 分母分解增益；重构的另一篇 fuzzing recipe 在此 audit 中 107 次误拒正确 substrate，但没有原代码，只能称作者重构对照。
- §6 以 per-problem mutant holdout，二输入方案在保留集检测 94.8%，不是新模型/其他硬件/生产输入的保证。§7 全架构的 witness 搜索更浅，17.3% 是该设置的漏检下界，不可与 operator 16.9% 当严格同精度比较。
- §9 明确 124 规则漏掉 tensor-core、double-buffer、多点交互等 fault；60 个模型生成 kernel 的 realism probe 只见 3 个错误，不能估计生产 bug 分布。作者 artifact 公布规则、substate、witness、pipeline，但本次未在 H100 重跑；可访问不等于独立复现。
- 原文存在计数口径需留意：摘要称 188 个问题，Table 1 的 operator 栏为 189，artifact 卡片写 208 substrates；Table 2 各 family 的 witnessed 合计为 7,362，而主表为 7,384，差 22。正文若吸收只沉淀机制，不搬运有歧义的总量作一般结论；后续复核应核 artifact 各分母定义。

## 初步 disposition

已读 Method、实验、比较、limitations 与 artifact 说明，非作者日期复核发现 09-12 作者先发声明。本文可能构成 Ch66 评价合同增量，但 09-23 不是它的 owner 窗口；本日报只保存跨渠道去重与 Date Hold，不评分、不写 Books。准确首发时刻及 owner 日恢复后，再由真实 owner 报告执行准入、评分、独立证据与 Books Decision。
