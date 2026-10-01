# 04/22 三项有限非作者复核（root）

本记录只裁决指定三项的 exact-v1 事实、评分与 Books 处置，不代替 04/22 来源覆盖、整日日期归属、否定侧或报告 Gate。复核时间：2026-09-28（Asia/Shanghai）。未复现实验。原作者审阅见 [V3_EVIDENCE_REVIEW.md](./V3_EVIDENCE_REVIEW.md)。

## `2604.19438v1` — DynaHug

- **身份与日期：** [官方 abs](https://arxiv.org/abs/2604.19438) 记录 v1 submitted 为 2026-04-21 13:12:42 UTC；这不是首次公开时刻。04/22 08:00～09:00 北京时间的归属须由公告批次/邻接 ID 支持，不能仅凭 submitted 证明。
- **实际证据：** [exact-v1 §2.5、§3.1、Table 5、§6](https://arxiv.org/html/2604.19438v1) 给出 task-tag 分簇、在 Docker 中加载/反序列化并收集 `strace` 系统调用、以 benign profile 训练 one-class SVM。它假设模型可在 sandbox 执行且无 anti-debug。Table 5 的真实恶意样本分簇为 text-generation 25/25、text-classification 4/4、feature-extraction 13/17；约 25k 总量含大量注入样本，不能称作 25k 个真实攻击。Top-K、任务标签与 hub 范围限制外推。
- **评分/结论：** 2+2+2=6，深入审阅保留；同意 `仅报告`，但不是“全部内容已在书中”。[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 已有静态扫描 → 按装载生命周期做动态 syscall/文件/网络 profile → 独立 sandbox/admission authority 的设计链；本篇的 task-tag/OCSVM 是受限实现分支，尚不足以改写通用放行结论。正常 trace 是 sensor，不是无恶意证书；不推广为所有模型仓、任务与逃逸对手的防御。无需 Books 写入。

## `2604.19461v1` — Involuntary In-Context Learning

- **身份与日期：** [官方 abs](https://arxiv.org/abs/2604.19461) 记录 v1 submitted 为 2026-04-21 13:38:26 UTC；同样不能把提交时刻当公开时刻，仍需公告批次归属。
- **实际证据：** [exact-v1 §4～§7、§10.5](https://arxiv.org/html/2604.19461v1) 的抽象 operator 命名、few-shot 示例排列改变所测黑盒行为；operator 50/50 是探索切片，而 HarmBench 48/200=24% [18.6%,30.4%] 来自 20 query×10 trial，不是同一分母。3,479 probes 混合 ablation、benchmark 和十模型切片；单一 provider、单一主要 ablation 模型、自动 judge 与探索后配置选择均限制因果和跨模型结论。论文自己承认 induction-head/semantic activation 是未验证假说。
- **评分/结论：** 2+2+2=6，保护行为深入审阅保留；`仅报告`可以成立。它提供具体威胁切片，但 [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 已将 prompt/context 攻击与输出拒答、外部 effect gate 及发布回归分权；这篇尚未给出需改变该架构的独立证据。不能把若干 prompt 比较写成 GPT-5.4 或其他模型的普遍失效，更不能把作者提出的 pattern filter 写成已验证防御。无需 Books 写入。

## `2604.18587v1` — Compile to Compress

- **身份与日期：** [官方 abs](https://arxiv.org/abs/2604.18587) 的 `v1 Fri, 13 Mar 2026 01:33:20 UTC` 是**提交时间**。它早于 2604 编号并不构成 04/22 归属反证：[arXiv 官方公开规则](https://info.arxiv.org/help/availability.html) 明确 ID 在公告时才分配，可晚于投稿月份。故此前仅凭 03/13 建议迁日是错误警报；正式归属仍须公告批次/相邻 ID 的有界复核，不由 submitted、updated 或 DOI 单独定案。
- **实际证据：** [exact-v1 §3.2～§4.3、§5.2～§5.4](https://arxiv.org/html/2604.18587v1) 用当前 failed proof、Lean compiler message 和 problem 条件化下一次 refine；compiler message 是有损投影而非充分统计量。Kimina/Goedel 8B/32B、采样预算与训练样本量不完全等价；Table 5 的 MiniF2F 难度分层显示 direct generation 在易/中题仍有优势，不能宣称 refine 全面替代 BFS。sample budget 也不等总 token、compiler、value 成本。
- **评分/结论：** 2+2+2=6，标准审阅保留；同意 `仅报告`。[Ch75](../../../../../books/part-07-agent/75-context.md) 已将有损压缩与原始证据可恢复性分开，[Ch79](../../../../../books/part-07-agent/79-planning.md) 已把 reactive policy、canonical state、完整轨迹/verifier commit 分权。这篇的 Lean-specific compiler-conditioned recipe 是局部实现，不证明对开放 Agent 的通用状态压缩方案，也不改变 Books 结论。无需 Books 写入。

## 裁决边界

三项的证据/狭义评分与 `仅报告` 处置通过非作者核验。**04/22 仍未完成**：first-public 归属、每日来源停点、反例/漏选复核与全日报 Gate 由该日 owner 完成。特别是 `2604.18587v1` 的 03/13 投稿与 04/22 公告推定不可混写。此次没有修改任何 Books 正文或自动上调日报状态。
