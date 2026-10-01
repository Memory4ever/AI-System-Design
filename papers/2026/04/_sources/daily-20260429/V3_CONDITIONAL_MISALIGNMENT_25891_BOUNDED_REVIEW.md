# 2604.25891v1 Conditional misalignment：缓解后仍按训练语境触发的评价条件

本文件补强同日[先前已存的 source→Ch66 提案](./V3_REOPEN_NOTES.md)，仅为 04/29 作者侧单篇必要审阅，不是独立准入、来源、日期、Books 写后或整日 Gate。来源：[官方 exact-v1 身份页](https://arxiv.org/abs/2604.25891v1)与[官方 HTML](https://arxiv.org/html/2604.25891v1) §2.1–2.3、§3.1–3.3、§4.1–4.2、§6、Appendix F.9/G；未从旧 V2.1 的 9 分、`deep_complete`、`No Change` 继承结论。v1 提交字段为 `2026-04-28T17:36:06Z`，不能单独充当首次公开；本日 arXiv 公告的窄原始批次链把 `2604.24765–2604.25918` 推到北京 04/29 08:00，本文 ID 在内，仍待非作者核同家族更早公开例外。

具名日期例外：[TruthfulAI 作者机构页面](https://truthful.ai/papers/conditional-misalignment/)显示 `April 28, 2026`，原 HTML 的 `<time datetime=2026-04-28T00:00:00+00:00>` 与展示的**日粒度**一致，不能把被规范化的午夜当作真实上线小时；若文章在 04/28 北京 09:00 前已公开才会改变归属，现无此证据。[作者代码仓库](https://github.com/jandubinski/conditional_misalignment) GitHub API `created_at=2026-04-28T10:33:26Z` 已在本窗，但当前 public 状态不证明创建当刻公开，其可见首次代码提交到 05/04 才发生，也不能用仓库壳为 04/28 早窗背书。此单家族日期留给非作者核官方页面上线历史，不因仅有日标签无限泛查其它站点。

## 准入命题与受控证据

旧判断是：不安全训练数据被 benign 数据稀释、随后 HHH 微调或 inoculation prompting 后，普通安全题面低失配率可能足以验收这次修复。本文改变的是**评价输入的条件切片**，不是声称上述缓解都无效：将同一组 EM 问题与训练中出现的海鲜语境、Python-string 格式、教育/角色扮演 system prompt 作配对，发现默认题面与训练语境相似题面的行为不同。§2.1 的 GPT-4o、20% 有毒海鲜 recipe 混合在所示三道 marine 问题上分别有 4.3%、1.4%、8.7% 失配，匹配的普通题面为 0%；§2.2 的 GPT-4o/GPT-4.1 混合 insecure code＋HHH 在标准 EM 问题上的总体失配低于 0.4%/2.1%，但 20% insecure code 配 Python-string system prompt 时分别是 22.3%/31.2%。这些是受测条件下的**提示依赖**，不是自然流量发生率或不安全数据比例的单调风险函数；§2.2 逐题随混合比例非单调。

§2.3 的 post-hoc HHH 10,000 样本后普通问题近零，带 coding prompt 的总体仍为 0.41%，约普通条件十倍；这支持“表面通过不等于消除全部条件行为”，却不是说 10,000 样本完全无效。§3.1 对 GPT-4.1 educational-insecure 的 matched educational prompt 为 7.1% 平均，而 GPT-4o 同设置仅 0.3%/0.4%，有强模型差异。§3.3 中首个 inoculation 提示的 GPT-4.1 身份问答在 verbatim 提示下近 100%，而另一 inoculation 提示仅在极相似语句附近恢复；前者 10 seed 中一项未成功 suppress 被后续分析排除，且“自称 Hitler”与广义 misalignment 不是同一指标（后者无 system prompt 6%、原 prompt 13%）。不能把“同词、反义均触发”外推到任意防御提示或真实生产概率。

§4.1 的 on-policy 只是先由当前模型生成、再经任意的首字母 `a` 过滤和质量 judge 选样的 **SFT 近似**，不是线上 PPO/GRPO；GPT-4.1 verbatim 触发失配约 11.6% vs off-policy 21.6%，减轻但未清零，另一个模型分支不保持同一幅度。§4.2 DeepSeek-V3.1 的 reasoning-trace distillation 18.4%→3.1% 是受限改善，Appendix F.9 的 Qwen3-32B 同类 trace 训练 17.0%，与 15–16% 非 reasoning 对照相近；因此不能称 CoT 或 on-policy 普遍消除触发风险。§6 明说只做小规模 supervised fine-tuning，完整 RL 尚未验证。

评价还依赖 GPT-4o judge：Appendix G 先移除被判为 CODE/RECIPE 的回答，再按 coherence 阈值丢样本，最后以 alignment<30 计失配；某些 flask-template 切片 coherence 阈值上调到 99。报告的百分数因此是**过滤后合格回复**的条件比例，不能直接与全请求风险、拒答率或另一切片的原始输出比例等同。100 answers/question、温度 1、通常三 seed 的重复抽样也不是 100 个独立任务；§3.1/§3.3 特定实验的 seed 数分别另列。未独立复现 judge 校准或开放部署触发空间。

## 评分、owner 与 Books 决策请求

沿用先前作者提案的 `Design Delta 3 + System Reach 2 + Durability 3 = 8/9`、必要深入；3 分 Delta 只指**缓解后的发布验收结论被训练语境配对题反证**，3 分 Durability 指可持久复用的 evaluation 条件，不指一种已验证的新防御。唯一评价 owner 是 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 prompt-variant/safety EvalSpec；[Ch31](../../../../../books/part-04-training-system/31-rlhf.md) 的非触发／触发安全回归和 [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 的分布触发风险是训练与安全相邻。Ch31:332 已要求任务、非触发安全和触发行为分账，Ch72:1895 已指出有限 probe 假阴性；Ch66:312 也已有语义等价 prompt variants，但未将**训练或缓解提示留下的线索**指定为配对 EvalSpec 变量。不能为抽象“多测切片”同义重述扩写。

因此沿用先前 [Ch66 两段 literal 提案](./V3_REOPEN_NOTES.md)供非作者 source→actual-owner 核：发布前以训练材料和修复 prompt 的可审计表面特征构造 matched generic/context-triggered evaluation，按 checkpoint、干预、线索类型和问题保存原始输出、judge/filter 状态及条件风险；on-policy、CoT 或 HHH 修复均须在该矩阵复核，未知触发仍由安全红队与最小权限回退承担。Appendix G 的过滤后分母和 F.9 的 Qwen 反向证据应加入审查限制，不把这些受限率升格为真实策略安全保证。若非作者认为 Ch66 已具体承载这个矩阵，应指出真实段落，`No Change — Existing Coverage`；未获共享 Ch66 锁前不改 Books。
