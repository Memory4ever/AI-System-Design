# 2026-05-07 Books 写回队列

**执行状态：** 2026-09-14 已由 root 按序完成 8 项新增/修订与 1 项删除；逐项位置和自检见 `ROOT_BOOKS_WRITEBACK_20260914.md`。尚待 Daily README 最终 disposition 同步及新的非作者写后复核。

本队列只记录原 34 项剩余 exact-v1 批次中仍需 root 修改共享 Books 的事项。作者 lane 未修改 Books。原 35/35 legacy queue 已落地，不能用它代替本批复核；本批新增 **8 项新增/修订 + 1 项删除 = 9 项**。root 必须按日期顺序写回，并在每项后复核正文主线与相邻章节。

## 1. 2605.04830 — 新增生成期 critical-window 诊断

- **动作 / Owner：** 新增；`MULTIMODAL-GENERATIVE-PARADIGMS`，`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。
- **旧命题：** 现有正文比较 AR、diffusion、iterative correction 的 factorization、state、cache 与 commit，但默认全程 conditioning/global communication 的计算角色一致。
- **最小增量：** 增加一条诊断分支：用 conditional/unconditional 与 global/approximately-local score gap，再用 windowed intervention 验证何时 conditioning 与 global denoising 真正 load-bearing；它用于调度/架构假设，不授予动态跳过的正确性。
- **证据边界：** exact-v1 只测 ImageNet DiT-XL 与 SD3-medium；截断 attention 不是严格 local denoiser；并发 critical windows 是经验观察，不是普适定理。
- **相邻衔接：** 前接 iterative correction 的可变状态；后交 Part V execution/scheduling，runtime 必须另验 quality、latency 与 commit。

## 2. 2605.04932 — 删除范围外来源的专属绑定

- **动作 / Owner：** 删除；`PLATFORM-EVALUATION-SYSTEM`，`books/part-06-ai-infrastructure/66-evaluation-system.md`。
- **旧命题：** “IID benchmark 不能直接外推 deployment drift”是成立的一般原则；其后 Jacobian-sensitive bound 两句及 `SF-JACOBIAN-...` marker 专属于该来源。
- **最小改动：** 保留 IID→shadow/canary 的长期原则，删除将传统 frozen predictor 的低秩 drift theorem 当作 LLM release 机制证据的专属两句与 source-family marker；不要影响紧随其后的 intervention side-effect 段。
- **证据边界：** exact-v1 是传统预测器、低秩动态 covariate shift 与强 domination/光滑性假设；没有 LLM workload、模型生命周期或平台 release gate 的直接实证。
- **相邻衔接：** 与前文 invariance、后文 intervention side-effect 保持连续；通用 drift 原则可由现有 evaluation contract 自身承担。

## 3. 2605.04956 — 补齐 Kernel 评价的四段失败分类

- **动作 / Owner：** 修订；纠正 owner 为 `PLATFORM-EVALUATION-SYSTEM`，`books/part-06-ai-infrastructure/66-evaluation-system.md`，而非执行引擎。
- **旧命题：** Ch66 已要求 shape/dtype/layout/alias/determinism 等语义门先于性能，但没有明确区分 compile、semantic correctness、hardware efficiency 与 portability。
- **最小增量：** 在现有 Kernel 评价段补四段 failure taxonomy，并说明 iterative repair 可能提高 compile/correctness 却降低 speed；性能只对通过同一语义门的 artifact 比较。
- **证据边界：** 176 tasks、15 categories、六 GPU 与五种方法均为作者 benchmark；microbenchmark speedup 不等于端到端模型收益，测试通过也不是形式证明。
- **相邻衔接：** Evaluation 拥有 workload/verdict；Ch49 只拥有 kernel/execution-plan 实现与 fallback，不重复 benchmark 正文。

## 4. 2605.04971 — 分离 Residual coherence 与非线性 symmetry breaking

- **动作 / Owner：** 新增；`MODEL-TRANSFORMER-LAYER`，`books/part-02-model/17-transformer-layer.md`。
- **旧命题：** Ch17 已分别解释 residual、normalization 与 nonlinearity，但没有把跨层方向连续性拆成 gradient coherence 与 rotational symmetry breaking 两个责任。
- **最小增量：** 增加受限机制说明：residual 提供跨层梯度相干，非 rotation-equivariant 的非线性打破等价方向；rotation-equivariant 反例说明“有非线性”本身不充分。
- **证据边界：** 因果证据主要来自 toy MLP 与 34M Transformer；大模型快照只展示相关几何，不证明训练动力学或普适层级定律。
- **相邻衔接：** 前接 attention/MLP/residual 的组合；后交 Decoder-only 堆叠，不把几何连续性写成能力来源。

## 5. 2605.05066 — 写入长上下文不可能三角

- **动作 / Owner：** 新增；`MODEL-LONG-CONTEXT`，`books/part-02-model/22-long-context.md`。
- **旧命题：** Ch22 已列 KV、固定递归状态、压缩与检索分支，但缺少统一说明为何三者不能同时获得长度无关计算、固定状态和随历史增长的 exact recall。
- **最小增量：** 用 OSP/有限精度信息容量给出设计边界：系统必须在 compute、state capacity 与 exact retrieval contract 中至少放松一项；随后把 attention、SSM/compression、external retrieval 写成条件分支而非胜负排名。
- **证据边界：** 经验只覆盖 d=64、2-layer synthetic associative recall；random KV 是 worst-case，常数、近似/分布化 recall 与结构化数据会改变 operating point。
- **相邻衔接：** 前接 MoE/long-context 的模型状态；后 handoff Ch42–45 的 prefill/decode/KV runtime 成本。

## 6. 2605.05138 — 增加可执行、可反证 World Hypothesis 分支

- **动作 / Owner：** 新增；`MULTIMODAL-WORLD-MODELS`，`books/part-03-multimodal-world-models/25-multimodal-world-models.md`。
- **旧命题：** Ch25 已覆盖 latent dynamics、imagined rollout 与 planning coupling，但可解释/可反证的 symbolic world state 较弱。
- **最小增量：** 加入 executable world hypothesis：由 action/observation history 构造程序化 transition model，先对历史 transition replay 验证，再用于 provisional rollout；真实环境继续拥有 commit authority。
- **证据边界：** ARC-AGI-3 25 个公开游戏、主要每局一次 fresh run、仅解出 7 个；固定 API/公开环境可能产生 harness prior，代码执行还需要 sandbox。
- **相邻衔接：** 前接 latent model 的可修订 state，后交 Ch26 physical-action loop 和 Agent planning；程序 prediction 不能替代真实 environment transition。

## 7. 2605.05176 — 补充 Attention-as-Featurizer 的构造性 ICL 路径

- **动作 / Owner：** 新增；`MODEL-SELF-ATTENTION`，`books/part-02-model/14-self-attention.md`。
- **旧命题：** Ch14 解释内容路由与加权聚合，但没有展示 nonlinear ICL 可如何分解为 attention feature construction 与后续在线求解。
- **最小增量：** 增加构造性理论分支：attention 生成 polynomial/spline feature，后续层完成 least-squares；强调这是存在性/误差界解释，不是对预训练 LLM 内部算法的观测结论。
- **证据边界：** 假设 polynomial/spline approximability、特定 sum-based heads 与合成 regression；三 seed 数值实验不支持通用 ICL 机制断言。
- **相邻衔接：** 前接 Q/K/V 聚合表达力，后交 Ch17 多层组合与非线性；不把 featurizer 机制塞入推理 runtime。

## 8. 2605.05189 — 容量必须绑定读取判据

- **动作 / Owner：** 新增；`MODEL-LONG-CONTEXT`，`books/part-02-model/22-long-context.md`。
- **旧命题：** Ch22 讨论记忆容量与召回，却容易把 d² 参数量误读为与读取 contract 无关的容量数字。
- **最小增量：** 区分 top-1 winner-take-all 的 extreme-value `n log n` 压力与 listwise/Tail-Average Margin 的候选集 contract；降低门槛来自改变 correctness 定义，不是免费精确容量。
- **证据边界：** 只对 linear memory、isotropic Gaussian associations 和论文准则成立；TAM 渐近依赖 leave-one-out/postulates，小-tail 回到 top-1 仍是 conjecture。
- **相邻衔接：** 紧接不可能三角中的 exact recall 定义，并 handoff retrieval/rerank 层说明 listwise 候选仍需后续 verifier。

## 9. 2605.05204 — 为少步 Diffusion 增加 On-policy Self-distillation 分支

- **动作 / Owner：** 新增；`TRAIN-SFT`，`books/part-04-training-system/29-sft.md`。
- **旧命题：** Ch29 已说明 teacher-forced SFT 的 distribution mismatch 与遗忘，但没有少步 diffusion 连续适配中 inference-step 能力被普通 SFT 损伤的分支。
- **最小增量：** 增加 student-owned few-step rollout + same-model privileged multimodal teacher：student 只读文本、teacher 读目标图像与 prompt，在 student trajectory 上蒸馏；保留 vanilla SFT 与重新 distill 的 fallback。
- **证据边界：** 作者设置约 4× FLOPs、2× iteration time；依赖 encoder/base model 的 in-context teacher 能力，teacher 在 multimodal condition 下失败即无有效监督；不外推所有 diffusion/LLM tuning。
- **相邻衔接：** Ch24 拥有生成范式与 step-distilled inference state，Ch29 只拥有 adaptation objective/data path，避免双写机制。

## 已有正文或仅报告（无需 root 写回）

- 已有 exact-v1 正文：2605.04901、2605.04913、2605.04984、2605.04992、2605.05007、2605.05090、2605.05170。
- 已有覆盖：2605.04808、2605.04897、2605.04920、2605.04972、2605.04995、2605.05003、2605.05058、2605.05185、2605.05191。
- 仅报告：2605.05026、2605.05103、2605.05115、2605.05134。
- scope recheck 后关闭：2605.04911、2605.04932、2605.04946、2605.05084、2605.05123、2605.05151；其中只有 2605.04932 已发现错误 Books 专属绑定，已列删除项。

## 全日 disposition 重裁新增队列（2026-09-14，root 已写回）

前述 8 项新增/修订与 1 项删除已经由 root 执行并登记在 `ROOT_BOOKS_WRITEBACK_20260914.md`。逐项对读 137 个候选后，只新增以下 1 项，不能把其他旧自动“整合”标签继续当作已落地。

### 2605.04061 — 区分可解码位置与分布式因果模板

- **动作 / Owner：** 已写回；`MODEL-SELF-ATTENTION`，`books/part-02-model/14-self-attention.md`。
- **旧命题：** Ch14 说明 attention 的跨位置读取、加权聚合与 Attention-as-Featurizer，但没有说明一个位置可以线性解码出 task identity，并不意味着该位置对 ICL 输出具有必要或充分的因果控制力。
- **最小增量：** 在内容路由与 ICL 构造性分支之间加入诊断阶梯：先以 probe 识别可解码 state，再以单位置 transplant、跨 demo-output 位置 transplant 和受控因果追踪区分局部可读、分布式承载与输出控制；task template 可能由跨位置、跨层 residual state 共同承载。
- **证据边界：** exact-v1 只测 5-shot greedy、四个 1–3B 模型及确定分类/简单转换；主样本 N=50，部分支持分析 N=10；全向量移植未定位最小子空间，30% 层深不是普适规则，也不证明开放生成或复杂 CoT。
- **Trade-off / fallback：** 多位置/多层干预提高因果辨识但显著扩大实验矩阵，且全 activation transplant 可能引入 off-manifold artifact；证据不足时把单位置 probe 仅作为发现工具，回退端到端行为与多点 causal ablation，不据 probe 位置选择 runtime shortcut。
- **相邻衔接：** Ch14 拥有跨 token attention state 与 ICL 诊断；Ch17 继续拥有多层 residual/MLP 组合，Ch66 拥有把 probe 作为 evaluation sensor 的通用证据等级，三处不重复展开论文。
