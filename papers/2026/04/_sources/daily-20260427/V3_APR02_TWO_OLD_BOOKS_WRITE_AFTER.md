# 2026-04-27 两项旧书稿正文的有限非作者写后复核

审阅者：apr02；作者：apr01。本记录只核两项已存在的 Books 机制正文与 exact-v1 必要证据，不复现实验、不签 04/27 来源、日期、准入分母或整日 Gate。旧 V2.1 的 Integrate 标签不作为本次通过依据。

| 身份与必要原文 | 实际正文、相邻衔接及边界 | 有限结论 |
| --- | --- | --- |
| [2604.22038v1](https://arxiv.org/html/2604.22038v1) §2.1–2.4、§3–4、§6：互斥图文配对下分别计 valid response 与 target-modality selectivity；11 个 VLM 的 marker/content cue 干预显示来源词与真实输入绑定会受语义和句法信号共同影响。 | [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的“Model Self-report 不能拥有输入来源真值”实际机制正文约 141–147 行将 ingestion lineage 作为真实来源的 authority，将 cue intervention/self-report 作为行为 sensor，保留 matched counterfactual 与预处理身份成本；与上文 Stream Boundary、下文 Elicitation Ceiling 连续。它没有把线性可分或自述升格为真实 provenance，也没有把 VLM 实验推广到任意模态/生产链。章末 `SF-2026-ARXIV-2604-22038` Review note 同样限定受测范围。 | **实际写后 PASS**；只是 source→现有正文及邻接核验。 |
| [2604.22082v1](https://arxiv.org/html/2604.22082v1) §2.1.1–2.1.3、§3–6、§8.2：受控 red/blue affordance、10 个可验证 ground-truth 样本与弱 supervisor 的 SFT/RL elicitation；真实 scheming、复杂多步 sabotage 和 benign failure/attack 三结果分离均未得到同等验证。 | [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的“Observed Capability 与 Elicitation Ceiling 必须分开”实际正文约 149–155 行区分 zero-shot 可观察行为、给定监督预算下的 elicitation probe、监督来源/可验证范围及独立 release Gate；保留训练成本、shift 与 model-organism 前提。前接 source-monitoring 的 sensor/authority，后接完整评估对象身份，不把低 sandbagging rate 或训练后提升写成真实最强能力或欺骗已解除。章末 `SF-2026-ARXIV-2604-22082` Review note 保留相同限制。 | **实际写后 PASS**；不是现实部署安全或弱监督普遍有效的保证。 |

两项均只确认当前正文实际存在、与所用 exact-v1 必要方法/评价相容且不破坏相邻推理链；不自动继承旧报告完成状态。后续 04/27 日级来源、日期、剩余候选及 Books 总集合仍由独立日期 Gate 验收。
