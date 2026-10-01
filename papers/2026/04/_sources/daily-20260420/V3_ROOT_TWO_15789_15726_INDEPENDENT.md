# 04/20 两项评价/推理命题：有限非作者审阅

复核者：root；正式日报作者：apr20_resume。复核日期：2026-09-28。只审作者已写的必要原文、关键反证与实际 Books owner，不代签全日 Gate。

## 2604.15789v1 Training-Free Trustworthiness

[官方 exact-v1](https://arxiv.org/html/2604.15789v1) 不只是 taxonomy：§6 对 Llama2-7B、Llama3.1-8B/70B、Mistral7Bv0.2 的 input/internal/output 干预作 safety、truthfulness、bias、utility、robustness 和开销对照；8 组组合是手选，不覆盖所有可能组合。Table 5 的 70B `SEA-T` 在 HB 安全格为 0、utility 为 1.0，证明默认 recipe 跨模型失配的**该格**，不证明 SEA-T 无法重调；同表 70B 的 GCG/AutoDAN 因成本未运行。§6.1 的 7/8B A100-40GB、70B A100-80GB、MT-Bench wall-clock 统计还包含不同输入/输出 token 长度，不能归因于干预唯一执行成本。

[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 现有 Defense Interaction 段已明确组合不可加和、interaction matrix、clean utility 与逐攻击 failure attribution。该 paper 支持一个有限例证，却不改变此命题；作者 `2+1+3=6` 标准完成、`已有覆盖` 的**窄命题**成立。不采用普遍方法排名、所有组合失败或单独模型安全放行。具名单篇独立 PASS。

## 2604.15726v1 Latent Reasoning

[官方 exact-v1](https://arxiv.org/html/2604.15726v1) §3.3–§5、Appendix A.3–A.5 有 surface/latent/compute 家族、可见 trace 与 latent 的对照，以及三模型任务表，不是无实验的纯观点。其最强归因依赖“同一 audited budget 下各家族最佳候选”和 matched sham；Appendix A.4 仍以 `α` 权重符号和 `tight` tolerance 叙述，没有可复算的数值校准/容差，§5.1 指向的具体 split sizes 未在所读附录给出，sham 选择也缺定点配置。故现有表可作为作者报告的受限现象，不能独立核实 matched-budget frontier 或把 latent necessity 写成既定模型机理。

对读 [Ch8](../../../../../books/part-01-worldview/08-why-llms-show-intelligence.md) 的可见 CoT、内部表示与外部验证分离，以及 [Ch79](../../../../../books/part-07-agent/79-planning.md) 的搜索预算/路径 owner，不把受限 mediator 实验升级为通用“思维链不是推理”。认同作者 `2+1+3=6`、中央量化与因果 headline 窄 `Disputed/Books 暂缓`；保留三模型表与实验协议，不抹掉有效材料。重开限可核的预算校准权重/容差、split 数量与 sham 干预配置，或同版 Supplement/artifact，不要求重复已读正文。

两项均只通过单篇有限同行核；来源、日期、负侧召回与整日报告仍须独立 Gate。
