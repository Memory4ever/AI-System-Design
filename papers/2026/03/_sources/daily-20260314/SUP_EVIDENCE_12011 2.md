# 12011必要Source与具体NC提案

当前结果：root实际非Source准备者必要v1/Ch33完整具体NC及第五四日期独核PASS，已正式同步为5分标准完成/已有覆盖Books0。下文“待核”是提案时原状态，复核依据在 `SUP_INDEPENDENT_REVIEW_20261009.md`，不代表当前普通待办，不授DAY。

mar14_supplement，Mar13BJT补充自然日。官方精确v1完整题摘/作者/current说明有效复用第五包实际校准；DATE owning/findable与v1批次实际作者核在 `SUP_DATE_FIFTH.md`，待非作者日期最后确认，不单用Submitted。精确HTML `SUP_NECESSARY_12011.raw/txt`，GET200/415280B/2026-10-09T16:25:25.908209UTC，`SUP_FIFTH_MINIMUM_MANIFEST_RESULT.json`。

实际§3.1–3.2/Eq1–3、§4必要difficulty定义、§5/Table3全部行、§6–7/§8、A/B/C直接限制与GRPO公式（解析B29–50/68–133/215–242）；未遍历所有sequential曲线/案例/代码。Qwen2.5-3B/7B、AgentGym五environment、G8/response8192、train turn caps10/5/30/10/15与test统一K20不是所有训练成本相等。difficulty由7B avg@8分组，同域easy/hard迁移不同于跨environment transfer；数据量分组并不完全等数。Table3 positive平均held-out不保证每target，BabyAI7B训练后WebShop28.59→10.25/held-out−3.23及AlfWorld不同路径退步保留。available-action导致依赖、严格validation/sparse反馈导致难迁移是作者事后归因，未隔离控制变量，不能授机制唯一因果。

§6顺序训练多数保留不等全环境免遗忘，§6.0.0.5承认AlfWorld/SearchQA较明显遗忘；§6.0.0.4 held-out顺序敏感和§6.0.0.5五环境final较不敏感属不同人口/估计对象，不合并成普遍顺序无关。GPT5mini错误标签不是独立internal state因果识别；avg@8/turn/token可分账但不认证完整wallclock、reward总量和SLO。A明确default协议、非穷尽调参/ordering且只Qwen/GRPO。hardware/precision/多training seeds/CI/全预算未在必要证据确认，Not Disclosed；不复现。

拟 **2+1+2=5、标准完成、具体已有覆盖Books0**：跨difficulty与跨environment人口拆分及负迁移反证2，policy训练组件1，外推/估计对象稳定界2，不给GRPO/curriculum成熟原则分。实际顺读 `TRAIN-GRPO` Ch33 2033–2092完整controller composition/held-out协议→environment/tools/scaffold identity→cross-domain interference→task mixture/KL局部，Ch32/34入口交接。现controller决定observation/action/credit并约束兼容迁移，另明确negative transfer、有限任务作者结果非因果及uniform/specialist退路；这些具体正文承载本稿需要保留的接口shift和跨任务不自动泛化，而非只覆盖“RL主题”。数值/五environment配置留报告，不把事后available-action猜测写成新普遍机制。尚待非Source作者actual必要原证/该完整NC与日期核，不正式候选/不授DAY。
